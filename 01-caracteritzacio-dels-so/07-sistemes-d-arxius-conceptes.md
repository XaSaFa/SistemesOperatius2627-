[⬅ Anterior: E/S i interfícies](06-gestio-es-i-interficies.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Arxius, atributs i permisos ➡](08-arxius-directoris-atributs-i-permisos.md)

# 7. El sistema d'arxius: conceptes

> Criteri d'avaluació RA1.4 — *Descriu l'estructura i organització del sistema d'arxius.*

## 7.1. Definició

Un **sistema d'arxius (*file system*)** és l'estructura lògica que un SO fa servir per organitzar la informació
d'una unitat d'emmagatzematge en **fitxers** i **directoris**, i per saber en tot moment quins sectors pertanyen
a quin fitxer, quins estan lliures i quins són defectuosos.

- El tipus de sistema d'arxius (FAT32, exFAT, NTFS, ext4…) es decideix en **formatar** el volum.
- Cada SO té els seus, encara que molts són compatibles entre plataformes. Vegeu el
  [tema 9](09-tipus-de-sistemes-d-arxius.md).

## 7.2. Elements bàsics

- **Fitxer o arxiu regular:** col·lecció d'informació relacionada, identificada per un nom, que s'emmagatzema
  com una unitat.
- **Directori o carpeta:** contenidor especial que agrupa fitxers i altres directoris (subdirectoris).
  Tècnicament és un tipus d'arxiu que només guarda referències a altres arxius.
- **Directori arrel:** origen de tota l'estructura. A Windows, per unitat: `C:\`, `D:\`… A UNIX/Linux, únic per
  a tot el sistema: `/`.
- **Volum / unitat lògica:** partició formatada i llesta per usar. A Windows es representa amb una **lletra**
  (`C:`, `D:`…); a Linux es **munta** sobre un directori (per exemple `/`, `/home`, `/media/usb`).

## 7.3. Organització física i lògica d'un disc

### Estructura física (la crea el fabricant, format a baix nivell)

| Element | Descripció |
|---|---|
| **Cares (*heads*)** | Superfícies dels plats magnètics (mínim 2 per plat). Es numeren des de la cara 0. |
| **Pistes (*tracks*)** | Cercles concèntrics de cada cara. |
| **Cilindres (*cylinders*)** | Conjunt de pistes amb el mateix número en totes les cares. |
| **Sectors** | Divisió de cada pista; **unitat mínima de lectura/escriptura física**. 512 B (clàssic) o **4 KiB** (Advanced Format, actual). |

> En un **SSD** no hi ha plats ni pistes: la informació es guarda en cel·les de memòria *flash* NAND
> organitzades en pàgines i blocs. El SO, però, hi segueix veient un espai adreçable per **sectors lògics** (LBA).

### Estructura lògica (la crea el format del SO)

| Zona | Funció |
|---|---|
| **Sector d'arrencada (*boot*)** | Primer sector del volum. Conté un petit programa de càrrega i una taula amb els paràmetres del volum (**BPB — BIOS Parameter Block**: nombre de cares, pistes, sectors, mida de sector, etiqueta, número de sèrie). |
| **Estructures de metadades** | FAT (taula d'assignació) en sistemes FAT; **MFT** en NTFS; taula d'*inodes* en ext/UFS. Indiquen on comença i acaba cada fitxer, quins blocs ocupa i quins són lliures. |
| **Directori arrel** | Entrades amb nom, extensió, mida, data/hora i atributs de cada element del primer nivell. |
| **Zona de dades** | La major part del disc; on es guarda realment el contingut dels fitxers i subdirectoris. |

### Sector vs. clúster

- **Sector:** mínima unitat que **el maquinari** llegeix o escriu.
- **Clúster o unitat d'assignació:** grup de sectors consecutius (2, 4, 8, 16…); mínima unitat que **el SO**
  assigna a un fitxer.
- Un fitxer ocupa un o més clústers; encara que sigui més petit que un clúster, l'ocupa sencer → l'espai
  sobrant es perd (**fragmentació interna** o *slack*). Clúster gran = menys entrades de metadades però més
  malbaratament amb fitxers petits.

## 7.4. Rutes o camins (*paths*)

Una **ruta** és la cadena que indica on és un fitxer o directori dins de l'arbre. Els noms de directoris se
separen amb `\` (Windows/CMD) o `/` (Linux, i també Windows en molts contextos).

- **Ruta absoluta:** parteix del directori arrel; identifica el recurs sense ambigüitat.
  - Windows: `C:\Usuaris\anna\Documents\informe.docx`
  - Linux: `/home/anna/documents/informe.odt`
- **Ruta relativa:** parteix del **directori actiu** (el directori on ara mateix es treballa).
  - `..\imatges\logo.png` (Windows) · `../imatges/logo.png` (Linux)
- **Directoris especials:**
  - `.` → el directori actual.
  - `..` → el directori pare.
  - `~` (Linux) → el directori personal de l'usuari (`/home/usuari`).
- **Unitat activa / directori actiu:** cal saber en quina unitat i directori estem per interpretar les rutes
  relatives. A CMD cada unitat recorda el seu propi directori actiu.

### Exemple

```
/
└── princip
    ├── docs
    │   ├── doc1.txt
    │   └── word/
    └── apunts
        └── sistemes
            └── tema1.odt
```

- Ruta absoluta de `tema1.odt`: `/princip/apunts/sistemes/tema1.odt`
- Estant a `/princip/docs`, ruta relativa a `tema1.odt`: `../apunts/sistemes/tema1.odt`

## 7.5. Estructura de directoris habitual

- **Windows:** `C:\Windows` (SO), `C:\Program Files` i `C:\Program Files (x86)` (aplicacions),
  `C:\Users\<usuari>` (perfils), `C:\ProgramData` (dades comunes d'aplicacions).
- **Linux (Filesystem Hierarchy Standard):** `/bin`, `/sbin`, `/usr` (programes), `/etc` (configuració),
  `/home` (usuaris), `/var` (dades variables, *logs*), `/tmp` (temporals), `/dev` (dispositius),
  `/proc` i `/sys` (informació del nucli), `/mnt` i `/media` (punts de muntatge).

## 7.6. Operacions bàsiques

- Sobre **directoris:** crear, esborrar, moure, canviar de nom, llistar el contingut, canviar-hi (navegar).
- Sobre **fitxers:** crear, consultar (obrir/veure), modificar (actualitzar), esborrar, canviar de nom, copiar,
  moure, comprimir. Vegeu les ordres al [tema 8](08-arxius-directoris-atributs-i-permisos.md) i a
  [RA3 · gestió de discos i sistemes d'arxius](../03-configuracio-basica/03-gestio-de-discos-i-sistemes-d-arxius.md).

## 7.7. Resum

- El sistema d'arxius organitza la unitat en **fitxers i directoris** amb estructura d'**arbre** i un
  **directori arrel** (`C:\` o `/`).
- Estructura física: cares, pistes/cilindres, **sectors**. Estructura lògica: boot, metadades, arrel, dades.
- **Sector** = unitat física mínima; **clúster** = unitat que el SO assigna → *slack*/fragmentació interna.
- Rutes **absolutes** (des de l'arrel) i **relatives** (des del directori actiu, amb `.` i `..`).

## Comprova què has après

1. Diferència entre sector i clúster. Quin el defineix el maquinari i quin el SO?
2. Què és el BPB i on es troba?
3. Escriu la ruta absoluta i una de relativa (des de `/princip/docs`) per a `word/`.
4. A Linux, quantes lletres d'unitat hi ha? Com s'hi accedeix a una memòria USB?
5. Quin risc té triar una mida de clúster molt gran en un disc amb molts fitxers petits?

---

[⬅ Anterior: E/S i interfícies](06-gestio-es-i-interficies.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Arxius, atributs i permisos ➡](08-arxius-directoris-atributs-i-permisos.md)
