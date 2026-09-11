[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **8. Arxius, directoris, atributs i permisos**

[⬅ Anterior: Sistema d'arxius](07-sistemes-d-arxius-conceptes.md) · [Següent: Tipus de sistemes d'arxius ➡](09-tipus-de-sistemes-d-arxius.md)

# 8. Arxius, directoris, atributs i permisos

> Criteris d'avaluació RA1.5 i RA1.6 — *Atributs d'un arxiu i un directori; permisos d'arxius i directoris.*
> L'administració pràctica de permisos es tracta a [RA4 · permisos i recursos compartits](../04-administracio-del-so/02-permisos-i-recursos-compartits.md).

## 8.1. Identificació d'un fitxer

- **Nom** i, opcionalment, **extensió** (separats per un punt). L'extensió ajuda el SO i les aplicacions a
  saber el tipus de contingut (`.txt`, `.docx`, `.jpg`, `.exe`, `.sh`).
- Windows/CMD: regla clàssica **8.3** (FAT16) o noms llargs de fins a **255 caràcters** (FAT32, NTFS,
  exFAT). No distingeix majúscules/minúscules i **no permet** `\ / : * ? " < > |`.
- Linux: noms de fins a 255 bytes; **sí** distingeix majúscules/minúscules (`Carta.txt` ≠ `carta.txt`);
  gairebé qualsevol caràcter excepte `/` i el nul. L'extensió **no és obligatòria**; el tipus real es determina
  pel contingut (ordre `file`). Un nom que comença amb `.` és **ocult**.

## 8.2. Caràcters comodí (*wildcards*)

Serveixen per referir-se a **conjunts** de fitxers en ordres i cerques:

| Comodí | Significat | Exemple |
|---|---|---|
| `?` | Un caràcter qualsevol en aquella posició | `carta?.txt` → `carta1.txt`, `cartaA.txt` |
| `*` | Qualsevol seqüència de caràcters (fins i tot cap) | `*.jpg` → tots els JPEG; `informe*` → tot el que comença per «informe» |
| `[...]` (Linux) | Un caràcter de l'interval o conjunt | `foto[1-3].png` → `foto1.png`, `foto2.png`, `foto3.png` |

## 8.3. Metadades i dates

El SO desa per cada fitxer/directori: mida, clúster/blocs assignats, **data i hora de creació**, de **darrera
modificació** i de **darrer accés**, propietari i grup, atributs i permisos.

## 8.4. Atributs a Windows

Marques que modifiquen el comportament del fitxer o directori. Es veuen i canvien per la GUI
(*Propietats*) o per ordre `attrib`:

| Lletra | Atribut | Efecte |
|---|---|---|
| `R` | *Read-only* (només lectura) | No es pot modificar ni esborrar accidentalment |
| `H` | *Hidden* (ocult) | No es mostra per defecte |
| `S` | *System* (sistema) | Fitxer usat pel SO; ocult i protegit |
| `A` | *Archive* (modificat) | Indica que ha canviat des de l'última còpia de seguretat |
| `I` | No indexat | El servei d'indexació no l'analitza |
| `C` / `E` | Comprimit / Xifrat (només NTFS) | Compressió transparent / xifratge EFS |

```
attrib +R +H informe.docx        :: posa només lectura i ocult
attrib -H *.txt                  :: treu l'atribut ocult a tots els .txt
attrib /S /D +A C:\Dades\*       :: recursiu (subcarpetes i directoris)
```

## 8.5. Permisos i atributs a Linux

Quan es llista amb `ls -l`, cada element mostra **10 caràcters** a l'esquerra:

```
 - rwx r-x r--   1 anna alumnes 4096 ...  informe.txt
 │ └┬┘ └┬┘ └┬┘
 │  │   │   └── altres (resta d'usuaris)
 │  │   └────── grup propietari
 │  └────────── usuari propietari
 └───────────── tipus d'element
```

**Primer caràcter — tipus:**

| Car. | Element |
|---|---|
| `-` | Fitxer ordinari |
| `d` | Directori |
| `l` | Enllaç simbòlic |
| `c` | Dispositiu de caràcters |
| `b` | Dispositiu de bloc |
| `p` | Canonada amb nom (*pipe*) |
| `s` | Sòcol |

**Nou caràcters següents — permisos** en tres grups (**u**suari propietari, **g**rup, **o**tros/altres):

| Permís | Sobre fitxer | Sobre directori |
|---|---|---|
| `r` (llegir) | Veure'n el contingut | Llistar-ne els noms (`ls`) |
| `w` (escriure) | Modificar-ne el contingut | Crear, esborrar i canviar de nom fitxers dins seu |
| `x` (executar) | Executar-lo com a programa/script | Entrar-hi (`cd`) i accedir als seus fitxers |
| `-` | Sense aquest permís | Sense aquest permís |

### Notació octal

Cada grup de 3 bits `rwx` es representa amb un dígit octal (0–7):

| Octal | Binari | Permisos |
|---|---|---|
| 0 | 000 | `---` |
| 1 | 001 | `--x` |
| 2 | 010 | `-w-` |
| 3 | 011 | `-wx` |
| 4 | 100 | `r--` |
| 5 | 101 | `r-x` |
| 6 | 110 | `rw-` |
| 7 | 111 | `rwx` |

Exemples: `755` = `rwxr-xr-x` (típic de directoris i programes) · `644` = `rw-r--r--` (típic de fitxers de
dades) · `600` = `rw-------` (privat) · `777` = `rwxrwxrwx` (tothom tot; **evitar** per seguretat).

### Ordre `chmod`

```
chmod g+w informe.txt          # afegeix escriptura al grup
chmod go-rwx secret.txt        # treu tots els permisos a grup i altres
chmod u=rw,go=r nota.txt       # assigna exactament
chmod 750 projecte/            # rwx propietari, r-x grup, res altres
chmod -R 755 web/              # recursiu
```

- Referències d'usuari: `u` (propietari), `g` (grup), `o` (altres), `a` (tots).
- Operadors: `+` afegeix, `-` treu, `=` assigna exactament.

### Propietari i grup: `chown` i `chgrp`

```
chown anna informe.txt              # canvia el propietari
chown anna:alumnes informe.txt      # propietari i grup
chgrp alumnes informe.txt           # només el grup
chown -R www-data:www-data /var/www # recursiu
```

Només **root** (o l'usuari amb `sudo`) pot canviar el propietari; cada usuari pot canviar els permisos dels
**seus** fitxers.

### `umask`

Determina els permisos que **es retiren** en crear fitxers i directoris nous. Valor habitual `022`:
els fitxers neixen `666 - 022 = 644` i els directoris `777 - 022 = 755`.

### Permisos especials (avançat)

- **SUID / SGID** (`chmod u+s` / `g+s`): el programa s'executa amb els permisos del propietari/grup del fitxer.
- **Sticky bit** (`chmod +t`, típic de `/tmp`): en un directori compartit, cada usuari només pot esborrar els
  seus propis fitxers.
- **ACL** (`getfacl` / `setfacl`): permisos fins per a usuaris o grups concrets més enllà de propietari/grup/altres.

## 8.6. Permisos a Windows (NTFS)

NTFS fa servir **ACL (llistes de control d'accés)**: per cada usuari o grup s'indiquen permisos com *Control
total*, *Modificar*, *Llegir i executar*, *Llegir*, *Escriure*. Es gestionen a *Propietats → Seguretat* o per
ordre `icacls`. Es tracten a
[RA4 · permisos i recursos compartits](../04-administracio-del-so/02-permisos-i-recursos-compartits.md).

> A Windows, els **atributs** (`R/H/S/A`) i els **permisos NTFS (ACL)** són coses diferents: els atributs són
> marques simples del fitxer; els permisos diuen **qui** pot fer **què**.

## 8.7. Enllaços

- **Enllaç simbòlic** (Linux `ln -s`, Windows `mklink`): fitxer que apunta a una ruta. Equival a l'**accés
  directe** de la GUI. Si s'esborra l'enllaç, l'original no es toca; si s'esborra l'original, l'enllaç queda trencat.
- **Enllaç dur** (Linux `ln`): segon nom del **mateix** fitxer (mateix inode). El contingut existeix mentre en
  quedi almenys un nom.

## 8.8. Resum

- Identificació: nom (+ extensió opcional). Linux distingeix majúscules; Windows/CMD no.
- Comodins `?`, `*`, `[...]` per operar sobre conjunts de fitxers.
- Windows: **atributs** `R/H/S/A` (`attrib`) + **permisos NTFS/ACL** (`icacls`).
- Linux: **permisos `rwx`** per a propietari/grup/altres, en octal (`chmod 750`), propietat amb `chown`/`chgrp`,
  i `umask` per als valors per defecte.

## Comprova què has après

1. Què significa la màscara `drwxr-x---` i a qui permet què?
2. Passa `rw-r--r--` a octal i `640` a `rwx`.
3. Quina ordre posa un fitxer de Windows com a ocult i només lectura?
4. `chmod 777` sobre una carpeta web: per què és una mala idea?
5. Diferència entre un enllaç simbòlic i un enllaç dur.
6. Amb `umask 027`, amb quins permisos neix un fitxer nou? I un directori nou?

---

[⬅ Anterior: Sistema d'arxius](07-sistemes-d-arxius-conceptes.md) · [Següent: Tipus de sistemes d'arxius ➡](09-tipus-de-sistemes-d-arxius.md)
