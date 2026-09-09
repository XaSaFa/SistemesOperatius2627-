[⬅ Anterior: Requisits](01-requisits-i-compatibilitat.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Pla d'instal·lació ➡](03-pla-i-fases-d-instal-lacio.md)

# 2. Particions i estructura del disc

> Criteris d'avaluació RA2.5–RA2.6 — *Elabora un pla d'instal·lació; configura paràmetres bàsics (particions,
> sistema d'arxius).* Repassa abans el [tema 7 de RA1](../01-caracteritzacio-dels-so/07-sistemes-d-arxius-conceptes.md).

## 2.1. Particionar i formatar

Un disc que surt de fàbrica només té **estructura física**. Per fer-lo servir cal:

1. **Particionar-lo:** dividir-lo en una o més parts (**particions**) i assignar a cadascuna una mida i un lloc.
2. **Formatar cada partició:** crear-hi un **sistema d'arxius** (NTFS, ext4…) → la partició esdevé un **volum**
   utilitzable.

> Els disquets es formaten però **no es particionen**. Els discos durs i SSD sí que es particionen.

- **Format ràpid:** només reescriu les taules de metadades (l'espai es marca com a lliure).
- **Format complet:** a més, comprova sector a sector si hi ha errors físics. Més lent.

## 2.2. Esquemes de partició: MBR i GPT

| | **MBR (Master Boot Record)** | **GPT (GUID Partition Table)** |
|---|---|---|
| Època / firmware | Clàssic; associat a **BIOS** | Modern; associat a **UEFI** |
| Mida màxima de disc | **2 TiB** | ~9,4 ZB (pràcticament il·limitada) |
| Particions primàries | **4** (o 3 primàries + 1 estesa) | **128** (a Windows), totes «primàries» |
| Còpia de la taula | Una (al sector 0) | Duplicada (principi i final del disc) → més robusta |
| Arrencada | Codi al primer sector (MBR) | Partició de sistema EFI (**ESP**, FAT32) amb els carregadors |

> Regla pràctica: **UEFI → GPT**; **BIOS antiga → MBR**. Molts equips UEFI tenen un mode de compatibilitat
> (*CSM / Legacy*) que permet arrencar en MBR, però convé no barrejar.

## 2.3. Tipus de particions en MBR

| Tipus | Descripció |
|---|---|
| **Primària** | Espai «de primera classe». Màxim **4** per disc; és on normalment s'instal·la el SO. Cada primària pot tenir el seu sistema d'arxius. |
| **Estesa** | Una sola per disc. No guarda dades directament: és un contenidor per superar el límit de 4 primàries. |
| **Unitat / partició lògica** | Cada divisió dins de la partició estesa, amb el seu sistema d'arxius i lletra/punt de muntatge. |
| **Partició activa** | La partició primària que la BIOS llegeix en primer lloc per arrencar. Només n'hi pot haver **una**. Canviar-la permet arrencar un SO o un altre en arrencada dual. |

En **GPT** aquesta classificació desapareix: totes les particions són equivalents i s'usa una **ESP** per als carregadors.

## 2.4. Particions habituals segons el SO

### Windows (UEFI/GPT) — les crea l'instal·lador automàticament
| Partició | Sistema d'arxius | Funció |
|---|---|---|
| **EFI System Partition (ESP)** | FAT32 (~100–300 MB) | Carregadors d'arrencada UEFI |
| **Microsoft Reserved (MSR)** | — (~16 MB) | Reservada per a gestió |
| **Windows (C:)** | NTFS | Sistema i aplicacions |
| **Recuperació (WinRE)** | NTFS (~500 MB) | Entorn de recuperació |
| **Dades (D:)** *(opcional, recomanat)* | NTFS | Documents de l'usuari, separats del sistema |

### Linux — esquema típic
| Punt de muntatge | Sistema d'arxius | Mida orientativa |
|---|---|---|
| `/boot/efi` (ESP) | FAT32 | 300–512 MB (només UEFI) |
| `/boot` *(opcional)* | ext4 | 1 GB |
| `/` (arrel) | ext4 / Btrfs | 25–60 GB o més |
| `/home` *(recomanat separat)* | ext4 / Btrfs | La resta del disc |
| `swap` | — | ≈ mida de la RAM (per hibernar) o menys; pot ser un fitxer `/swapfile` |

## 2.5. Per què separar sistema i dades

- Si cal **reinstal·lar** el SO, es formata només la partició del sistema i les dades de `/home` o `D:` es
  conserven.
- Permet **fer còpies de seguretat** de les dades independentment.
- Redueix el risc de quedar-se sense espai al sistema per culpa dels fitxers d'usuari.
- Facilita l'**arrencada dual** (Windows + Linux) amb una partició de dades compartida (NTFS/exFAT).

## 2.6. Eines de particionat

| Entorn | Eina | Notes |
|---|---|---|
| Durant la instal·lació | Assistent del propi instal·lador (Windows Setup, Ubiquity/Calamares) | Suficient per a la majoria de casos |
| Windows instal·lat | **Administració de discos** (`diskmgmt.msc`) — GUI | Crear, eliminar, reduir, ampliar, canviar lletra, marcar activa |
| Windows instal·lat | **`diskpart`** — CLI | `list disk`, `select disk 0`, `create partition primary size=...`, `format fs=ntfs quick`, `assign letter=D` |
| Windows PowerShell | `Get-Disk`, `New-Partition`, `Format-Volume` | Automatitzable |
| Linux | **GParted** (GUI), `fdisk` (MBR), `gdisk`/`parted` (GPT), `mkfs.ext4`, `mkswap` | GParted es pot fer servir des d'un *live USB* |
| Multiplataforma | GParted Live, herramientas de tercers (llegat: Partition Magic, Paragon) | — |

> **Redimensionar** particions amb dades: Windows 7+ i les eines modernes permeten **ampliar** (si hi ha
> espai lliure contigu) i **reduir** sense perdre dades. Tot i així, fes sempre **còpia de seguretat** abans.

## 2.7. Resum

- Disc nou → **particionar** + **formatar** (sistema d'arxius) → volum utilitzable.
- **MBR** (BIOS, ≤ 2 TiB, 4 primàries) vs. **GPT** (UEFI, 128 particions, taula duplicada). UEFI necessita
  una **ESP** FAT32.
- MBR: primària / estesa / lògica; **partició activa** = la que arrenca.
- **Separa sistema i dades** en particions diferents per facilitar reinstal·lacions i còpies.
- Eines: assistent de l'instal·lador, Administració de discos / `diskpart` (Windows), GParted / `parted` (Linux).

## Comprova què has après

1. Diferència entre particionar i formatar.
2. Un disc de 4 TB amb BIOS antiga i MBR, quant d'espai podràs aprofitar? Com ho resols?
3. Què és l'ESP i quin sistema d'arxius té?
4. En MBR, quantes particions primàries hi pot haver i com se supera aquest límit?
5. Dona dos motius per instal·lar el SO i les dades en particions separades.
6. Quina ordre de Windows fa el particionat per CLI?

---

[⬅ Anterior: Requisits](01-requisits-i-compatibilitat.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Pla d'instal·lació ➡](03-pla-i-fases-d-instal-lacio.md)
