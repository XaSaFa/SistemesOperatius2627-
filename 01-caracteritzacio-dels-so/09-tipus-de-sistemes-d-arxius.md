[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **9. Tipus de sistemes d'arxius i sistemes transaccionals**

[⬅ Anterior: Arxius, atributs i permisos](08-arxius-directoris-atributs-i-permisos.md) · [Següent: Tipus de SO ➡](10-tipus-de-so-i-so-actuals.md)

# 9. Tipus de sistemes d'arxius i sistemes transaccionals

> Criteris d'avaluació RA1.4 i RA1.7 — *Tipus de sistemes d'arxius i les seves característiques; utilitat dels
> sistemes transaccionals en seleccionar un sistema d'arxius.*

## 9.1. Classificació per ubicació

| Classe | Descripció | Exemples |
|---|---|---|
| **De disc (locals)** | Emmagatzemen fitxers en una unitat connectada directament a l'equip | FAT32, exFAT, NTFS, ReFS, ext4, XFS, Btrfs, APFS, ZFS |
| **De xarxa** | Accedeixen als fitxers a través d'una xarxa | **SMB/CIFS** (Windows, també Samba), **NFS** (UNIX/Linux), AFP |
| **De propòsit especial / virtuals** | No guarden dades d'usuari de manera permanent | **ISO 9660 / UDF** (òptics), `/proc`, `/sys`, `tmpfs`, `devfs`, `swap` |

## 9.2. Sistemes d'arxius de Microsoft

| Sistema | Any | Mida màx. fitxer | Permisos | Journaling | Ús recomanat avui |
|---|---|---|---|---|---|
| **FAT16** | 1984 | 2 GiB | No | No | Només llegat (disquets, dispositius molt antics) |
| **FAT32** | 1996 | **4 GiB − 1** | No | No | Memòries USB petites i màxima compatibilitat (càmeres, consoles) |
| **exFAT** | 2006 | 16 EiB | No | No | **Memòries USB i SSD externs grans**; compatible amb Windows, macOS i Linux |
| **NTFS** | 1993 (NT) | 16 EiB (pràctic) | **Sí (ACL)** | **Sí** | **Discos interns de Windows**; compressió, xifratge EFS, quotes, enllaços, *Volume Shadow Copy* |
| **ReFS** | 2012 | 35 PB | Sí | Integritat per *checksums* | Servidors, grans volums, *Storage Spaces* (no arrencable) |

> **WINFS** era un projecte de sistema d'arxius de Microsoft (època de Windows Vista) que **mai es va publicar**;
> els llibres antics encara l'esmenten.

**Regla 8.3 / noms llargs:** FAT16 usava `NOM.EXT` (8+3); FAT32, exFAT i NTFS admeten noms de fins a 255 caràcters.

## 9.3. Sistemes d'arxius de GNU/Linux

| Sistema | Journaling | Característiques |
|---|---|---|
| **ext2** | No | Històric; encara útil per a particions `/boot` petites o memòries flash |
| **ext3** | Sí | ext2 + registre de transaccions |
| **ext4** | Sí | **Per defecte a la majoria de distribucions**; *extents*, fins a 1 EiB de volum i 16 TiB de fitxer, menys fragmentació |
| **XFS** | Sí | Alt rendiment amb fitxers grans i molta concurrència; per defecte a RHEL/Fedora |
| **Btrfs** | Sí (CoW) | Instantànies (*snapshots*), *subvolumes*, *checksums*, RAID integrat; per defecte a openSUSE i Fedora Workstation |
| **ZFS** | Sí (CoW) | Integritat de dades molt robusta, compressió, *pools*; origen a Solaris, disponible a Ubuntu i FreeBSD |
| **swap** | — | No és un sistema d'arxius de fitxers: espai per a la memòria virtual |

Linux també **llegeix i escriu** FAT32, exFAT i NTFS (controlador `ntfs3` al nucli), i pot muntar ISO 9660, UDF, SMB i NFS.

## 9.4. Altres plataformes

- **macOS:** **APFS** (actual, optimitzat per a SSD, *snapshots*, xifratge) i HFS+ (llegat).
- **OS/2:** HPFS (llegat).
- **Solaris:** UFS i ZFS.

## 9.5. Journaling i sistemes transaccionals

### El problema

Una operació sobre el sistema d'arxius (per exemple, «moure un fitxer») implica **diversos canvis** a les
metadades. Si hi ha un **tall de corrent** o una fallada al mig, el sistema d'arxius pot quedar **inconsistent**
(fitxers a mitges, blocs marcats com a ocupats i lliures alhora, directoris corruptes).

### La solució: transacció

Una **transacció** és un conjunt d'operacions que s'ha de completar **tot o res** (atomicitat). Les propietats
desitjables es resumeixen en **ACID**: **A**tomicitat, **C**onsistència, a**I**llament i **D**urabilitat.

### Journaling (registre per diari)

El sistema d'arxius escriu **primer** el que farà en una zona especial anomenada **diari (*journal*)** i,
després, aplica els canvis reals. Si el sistema es reinicia bruscament:

- Si la transacció era completa al diari → es **torna a aplicar** (*redo*).
- Si estava a mitges → es **descarta** (*rollback*) i el sistema d'arxius queda consistent.

Resultat: recuperació ràpida després d'un tall (no cal escanejar tot el disc) i molt menys risc de corrupció.

| Sí tenen journaling / són transaccionals | No en tenen |
|---|---|
| NTFS, ReFS, ext3, ext4, XFS, Btrfs, ZFS, APFS | FAT16, FAT32, **exFAT**, ext2 |

**Copy-on-Write (CoW)** (Btrfs, ZFS, APFS) va un pas més enllà: mai sobreescriu dades in situ, sinó que
n'escriu una còpia nova i després actualitza els punters; permet **instantànies** gairebé instantànies.

## 9.6. Com triar el sistema d'arxius en formatar

| Necessitat | Recomanació |
|---|---|
| Disc intern de Windows | **NTFS** |
| Disc intern de Linux | **ext4** (o Btrfs si vols instantànies) |
| Memòria USB / disc extern per moure fitxers > 4 GiB entre Windows, macOS i Linux | **exFAT** |
| Màxima compatibilitat amb aparells antics, càmeres, consoles (fitxers ≤ 4 GiB) | **FAT32** |
| Partició de dades compartida entre un Windows i un Linux al mateix equip | **NTFS** (Linux hi escriu bé amb `ntfs3`) o exFAT |
| Servei amb integritat i grans volums | ReFS / ZFS / Btrfs |

Factors a valorar: **compatibilitat** entre SO, necessitat de **permisos**, **journaling/integritat**, **mida
màxima** de fitxer i volum, i **rendiment** amb el tipus de càrrega previst.

## 9.7. Resum

- Sistemes d'arxius **de disc**, **de xarxa** (SMB, NFS) i **especials** (ISO, `/proc`, swap).
- Windows: FAT32 (compatible, límit 4 GiB/fitxer), **exFAT** (USB grans), **NTFS** (intern, permisos + journaling).
- Linux: **ext4** per defecte; XFS, Btrfs, ZFS per a casos avançats. Linux llegeix/escriu FAT/exFAT/NTFS.
- **Journaling / transaccional** = protegeix la integritat davant talls (ACID). exFAT i FAT **no en tenen**.

## Comprova què has après

1. Vols posar un fitxer de vídeo de 6 GiB en una memòria USB per veure'l en un Windows i un Mac. Quin sistema
   d'arxius tries i per què no FAT32?
2. Quins avantatges dona NTFS respecte de FAT32 en un disc intern?
3. Explica què fa el diari (*journal*) quan hi ha un tall de corrent enmig d'una operació.
4. Digues dos sistemes d'arxius amb journaling i dos sense.
5. Per què el mateix disc `swap` no es considera un sistema d'arxius de fitxers?

---

[⬅ Anterior: Arxius, atributs i permisos](08-arxius-directoris-atributs-i-permisos.md) · [Següent: Tipus de SO ➡](10-tipus-de-so-i-so-actuals.md)
