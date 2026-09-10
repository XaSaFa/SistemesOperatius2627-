[🏠 Inici](../README.md) › [RA2 · Instal·lació de sistemes operatius](00-index.md) › **1. Requisits tècnics i compatibilitat del maquinari**

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Particions ➡](02-particions-i-estructura-del-disc.md)

# 1. Requisits tècnics i compatibilitat del maquinari

> Criteris d'avaluació RA2.1–RA2.3 — *Analitza les funcions del SO; descriu l'arquitectura del SO; verifica la
> idoneïtat del maquinari.*

## 1.1. Comprovacions prèvies

Abans d'instal·lar cap SO cal comprovar:

1. **Requisits de maquinari:** processador, RAM, espai en disc, targeta gràfica, i requisits especials
   (UEFI, *Secure Boot*, TPM, arquitectura de 64 bits).
2. **Compatibilitat de controladors:** que existeixin *drivers* per a la placa, xarxa, gràfica, so, etc., per a
   la versió i arquitectura del SO. Un component sense driver no funcionarà o ho farà de manera limitada.
3. **Compatibilitat de les aplicacions** que s'hi hauran d'executar (versió, arquitectura de 32/64 bits,
   dependències).
4. **Arquitectura del processador:** x86 (32 bits), **x86-64 / AMD64** (64 bits, l'habitual), **ARM64**
   (portàtils i tauletes moderns, servidors). El SO ha de coincidir amb l'arquitectura.
5. **Suport per a tot el programari de l'entorn:** SO + antivirus + solució de còpies de seguretat + base de
   dades + aplicació de negoci.

## 1.2. Requisits mínims habituals (referència actual)

> Els llibres indiquen valors de Windows XP/7 (256–512 MB de RAM). A continuació, els valors **vigents**.

### Windows 10 (64 bits)
| Recurs | Mínim |
|---|---|
| Processador | 1 GHz, 2 nuclis, compatible x86-64 |
| RAM | 2 GB (recomanat 4 GB o més) |
| Disc | 32 GB lliures |
| Gràfica | Compatible amb DirectX 9 / WDDM 1.0 |
| Firmware | BIOS o UEFI |

### Windows 11 (64 bits) — requisits estrictes
| Recurs | Mínim |
|---|---|
| Processador | 1 GHz, **2 nuclis**, model de la llista de CPU compatibles (Intel 8a gen+, AMD Zen 2+, o més nou) |
| RAM | **4 GB** |
| Disc | **64 GB** |
| Firmware | **UEFI amb *Secure Boot*** |
| Seguretat | **TPM 2.0** |
| Gràfica | DirectX 12 / WDDM 2.0 |

### Ubuntu Desktop 24.04 LTS (64 bits)
| Recurs | Mínim | Recomanat |
|---|---|---|
| Processador | 2 GHz, 2 nuclis | 2 GHz, 4 nuclis |
| RAM | 4 GB | 8 GB |
| Disc | 25 GB | 40 GB o més |
| Gràfica | Resolució 1024×768 | Acceleració 3D |

Distribucions lleugeres (Lubuntu, Xubuntu, Debian amb XFCE) funcionen bé amb **2 GB de RAM** i maquinari antic.

## 1.3. Com verificar el maquinari

| SO | Eina | Què mostra |
|---|---|---|
| Windows | `msinfo32` (*Informació del sistema*) | Model de placa, BIOS/UEFI, RAM, processador |
| Windows | *Administrador de dispositius* (`devmgmt.msc`) | Dispositius i si tenen driver (triangle groc = problema) |
| Windows | **PC Health Check** de Microsoft | Comprova compatibilitat amb Windows 11 |
| Windows | `dxdiag` | Gràfica, DirectX |
| Windows | PowerShell: `Get-ComputerInfo`, `Get-CimInstance Win32_PhysicalMemory` | Inventari |
| Linux | `lscpu`, `free -h`, `lsblk`, `lspci`, `lsusb`, `inxi -Fxz` | CPU, RAM, discos, dispositius PCI/USB |
| Linux | `sudo dmidecode` | Informació de la BIOS/placa/RAM |
| BIOS/UEFI | Menú de configuració (`Supr`/`F2` a l'engegar) | Ordre d'arrencada, *Secure Boot*, mode SATA (AHCI), virtualització (VT-x/AMD-V) |

## 1.4. Llista de comprovació (*checklist*) abans d'instal·lar

- [ ] El processador i l'arquitectura són compatibles (64 bits, model suportat).
- [ ] Hi ha prou RAM i espai en disc (amb marge).
- [ ] Firmware: BIOS o UEFI; *Secure Boot* i TPM si el SO ho exigeix.
- [ ] Hi ha drivers per a xarxa, gràfica, so, xipset (mínim el de xarxa, per baixar la resta).
- [ ] Les aplicacions necessàries tenen versió compatible.
- [ ] **Còpia de seguretat** de les dades si l'equip ja s'usava.
- [ ] Suport d'instal·lació preparat (USB o DVD) i verificat (*checksum* / suma SHA-256 de la ISO).
- [ ] Clau de producte / llicència disponible si escau.
- [ ] BIOS/UEFI configurada per arrencar des del suport d'instal·lació.

## 1.5. Resum

- Verificar **requisits** (CPU/arquitectura, RAM, disc, gràfica, UEFI/TPM) i **compatibilitat de controladors i
  aplicacions** abans d'instal·lar.
- Windows 11 afegeix requisits estrictes: **UEFI + Secure Boot + TPM 2.0** i CPU de la llista.
- Eines de diagnòstic: `msinfo32`, Administrador de dispositius, PC Health Check (Windows); `lscpu`, `lsblk`,
  `lspci`, `inxi` (Linux).

## Comprova què has après

1. Quins tres requisits «nous» de Windows 11 no demanava Windows 10?
2. Quina eina de Windows et diu si un dispositiu no té driver?
3. Amb quines ordres de Linux comproves la CPU, la RAM i els discos?
4. Per què cal verificar la suma SHA-256 de la ISO abans d'instal·lar?
5. Si un equip antic no arriba als requisits d'Ubuntu Desktop, quina alternativa tens?

---

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Particions ➡](02-particions-i-estructura-del-disc.md)
