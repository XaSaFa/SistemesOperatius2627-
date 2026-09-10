[🏠 Inici](../README.md) › [RA3 · Configuració bàsica del sistema operatiu](00-index.md) › **3. Gestió de discos i sistemes d'arxius**

[⬅ Anterior: Interfícies i preferències](02-interficies-d-usuari-i-preferencies.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Programari i automatització ➡](04-programari-actualitzacions-i-automatitzacio.md)

# 3. Gestió de discos i sistemes d'arxius

> Criteri d'avaluació RA3.3 — *Gestiona els sistemes d'arxius específics.*
> Base teòrica: [RA1 · sistema d'arxius](../01-caracteritzacio-dels-so/07-sistemes-d-arxius-conceptes.md) i
> [RA1 · tipus de sistemes d'arxius](../01-caracteritzacio-dels-so/09-tipus-de-sistemes-d-arxius.md).

## 3.1. Operacions habituals amb volums

| Operació | Windows (GUI) | Windows (CLI) | Linux |
|---|---|---|---|
| Veure discos i particions | `diskmgmt.msc` | `diskpart` → `list disk/volume`; `Get-Disk`, `Get-Partition` | `lsblk`, `sudo fdisk -l`, `sudo parted -l`, GParted |
| Crear partició | Administració de discos → *Volum nou* | `diskpart` → `create partition primary size=…` | `sudo parted`, `sudo cfdisk`, GParted |
| Formatar | Clic dret → *Formata* | `format X: /FS:NTFS /Q` · `Format-Volume` | `sudo mkfs.ext4 /dev/sdXn`, `mkfs.vfat`, `mkfs.exfat`, `mkswap` |
| Assignar lletra / etiqueta | Clic dret → *Canvia lletra…* | `diskpart` → `assign letter=E` · `label` | `sudo e2label /dev/sdXn NOM` |
| Ampliar / reduir | *Amplia / Redueix el volum* | `diskpart` → `extend` / `shrink` · `Resize-Partition` | GParted, `resize2fs` |
| Eliminar volum | *Suprimeix el volum* | `diskpart` → `delete partition` | GParted, `parted rm` |
| Convertir MBR↔GPT (sense dades) | — | `mbr2gpt` (des de WinRE), `diskpart` → `convert gpt` | `sgdisk`, GParted |

> **FAT → NTFS sense perdre dades (llegat però encara vàlid):** `convert C: /FS:NTFS` (irreversible sense
> eines de tercers). No hi ha conversió inversa integrada.

## 3.2. Muntatge de volums

### Windows

Les particions reben una **lletra** (`C:`, `D:`…) automàticament o manualment. Alternativa: muntar un volum en
una **carpeta buida NTFS** (*punt de muntatge*), útil quan s'acaben les lletres.

### Linux

Un volum s'ha de **muntar** sobre un directori per accedir-hi.

```bash
lsblk -f                                  # veure dispositius, sistemes d'arxius i UUID
sudo mkdir /mnt/dades
sudo mount /dev/sdb1 /mnt/dades           # muntatge temporal
sudo umount /mnt/dades                    # desmuntar
```

Els dispositius extraïbles es munten automàticament a `/media/<usuari>/<etiqueta>` a l'escriptori.

**Muntatge permanent** amb `/etc/fstab` (una línia per volum):

```
# <dispositiu>            <punt muntatge>  <fs>   <opcions>              <dump> <pass>
UUID=1234-ABCD            /mnt/dades       ext4   defaults              0      2
UUID=ABCD-1234            /mnt/win         ntfs3  defaults,uid=1000     0      0
/swapfile                 none             swap   sw                    0      0
```

- Obtenir l'UUID: `blkid` o `lsblk -f`.
- Provar sense reiniciar: `sudo mount -a`.
- El camp *pass* (6a columna): `1` per a l'arrel, `2` per a la resta, `0` per no comprovar.

## 3.3. Comprovació i reparació del sistema d'arxius

| SO | Eina | Ús |
|---|---|---|
| Windows | **`chkdsk`** | `chkdsk C: /F /R` (`/F` corregeix errors lògics, `/R` cerca sectors dolents). L'arrel es comprova en el pròxim reinici. GUI: *Propietats → Eines → Comprova*. |
| Windows | Reparació d'arxius del sistema | `sfc /scannow`, `DISM /Online /Cleanup-Image /RestoreHealth` |
| Linux | **`fsck`** | `sudo fsck /dev/sdXn` — **el volum ha d'estar desmuntat** (per l'arrel, es fa a l'arrencada o des d'un live USB). Variants: `fsck.ext4`, `fsck.vfat`, `ntfsfix`. |
| Linux | SMART del disc | `sudo smartctl -a /dev/sdX` (paquet `smartmontools`); GUI: *Discs* → *SMART Data & Self-Tests* |

## 3.4. Desfragmentació i optimització (TRIM)

- **Discos durs magnètics (HDD):** els fitxers es fragmenten i cal **desfragmentar** de tant en tant.
  - Windows: *Desfragmenta i optimitza les unitats* (`dfrgui`, `defrag C: /O`). Programat setmanalment per defecte.
  - Linux: ext4/XFS es fragmenten molt poc; normalment no cal. Eina: `e4defrag`.
- **SSD:** **NO s'han de desfragmentar** (desgasta les cel·les i no millora res). El que cal és **TRIM**, que
  avisa l'SSD de quins blocs estan lliures.
  - Windows: *Optimitza* fa TRIM automàticament (setmanal).
  - Linux: servei `fstrim.timer` (setmanal) o opció `discard` a `/etc/fstab`; manual: `sudo fstrim -av`.

## 3.5. Neteja d'espai

| SO | Eina |
|---|---|
| Windows | *Sensor d'emmagatzematge* (*Configuració → Sistema → Emmagatzematge*), *Neteja de disc* (`cleanmgr`), `dism /online /cleanup-image /startcomponentcleanup` |
| Linux | `sudo apt autoremove && sudo apt clean`, `journalctl --vacuum-time=7d`, `du -sh */ | sort -h`, `ncdu`, `sudo docker system prune` (si escau) |

## 3.6. Compressió i xifratge de volums

- **Compressió transparent:** NTFS (*Propietats → Avançades → Comprimeix*); Btrfs (`compress=zstd` a fstab).
- **Xifratge de volum:** **BitLocker** (Windows Pro), **LUKS**/`cryptsetup` (Linux), FileVault (macOS),
  xifratge de la carpeta personal a la instal·lació d'Ubuntu.

## 3.7. Compressió de fitxers (arxivadors)

| Format | Windows | Linux |
|---|---|---|
| ZIP | Explorador (natiu), 7-Zip | `zip` / `unzip`, gestor d'arxius |
| 7z | 7-Zip | `7z` (paquet `p7zip-full`) |
| tar.gz / tar.xz | 7-Zip, Windows `tar` (natiu) | `tar -czf arxiu.tar.gz carpeta/`, `tar -xf arxiu.tar.gz` |
| RAR | WinRAR (extreu 7-Zip) | `unrar` |

> Diferència: **NTFS/Btrfs comprimeixen «en viu»** (transparent per a l'usuari); un **arxivador** (ZIP, tar.gz)
> crea un fitxer que cal descomprimir per fer servir el contingut.

## 3.8. Resum

- Gestió de volums: `diskmgmt.msc`/`diskpart` (Windows), GParted/`parted`/`mkfs`/`mount` (Linux).
- Linux necessita **muntar** els volums; el muntatge permanent es defineix a **`/etc/fstab`** amb l'**UUID**.
- Comprovació: **`chkdsk /F /R`** (Windows), **`fsck`** amb el volum desmuntat (Linux); SMART per a la salut del disc.
- **HDD** → desfragmentar; **SSD** → **TRIM**, mai desfragmentar.
- Compressió transparent (NTFS/Btrfs) ≠ arxivadors (ZIP, tar.gz).

## Comprova què has après

1. Quina ordre de Linux munta permanentment un volum i quin identificador s'hi recomana usar?
2. Diferència entre `chkdsk /F` i `chkdsk /R`.
3. Per què no s'ha de desfragmentar un SSD? Què s'hi fa en lloc d'això?
4. Un volum Linux dona errors; per què cal desmuntar-lo abans de passar-hi `fsck`?
5. Diferència entre comprimir una carpeta amb NTFS i comprimir-la en un ZIP.

---

[⬅ Anterior: Interfícies i preferències](02-interficies-d-usuari-i-preferencies.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Programari i automatització ➡](04-programari-actualitzacions-i-automatitzacio.md)
