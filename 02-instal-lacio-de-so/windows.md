[🏠 Inici](../README.md) › [RA2 · Instal·lació de sistemes operatius](00-index.md) › **RA2.2 · Instal·lació de Windows**

[⬅ Anterior: Llicències, actualització i incidències](07-llicencies-actualitzacio-i-incidencies.md)

# RA2.2 · Instal·lació de Windows

> Repàs comparatiu centrat en **Windows 10/11**. Cobreix els criteris de RA2 (RA2.1–RA2.10) amb el procediment
> propi de Windows. La teoria comuna (particions MBR/GPT, fases, gestors d'arrencada, llicències) i la
> instal·lació de Linux són a [RA2.1 · Linux i multiplataforma](00-index.md).

## 1. Requisits (RA2.1–RA2.3)

### Windows 10 (64 bits)
| Recurs | Mínim |
|---|---|
| Processador | 1 GHz, 2 nuclis, x86-64 |
| RAM | 2 GB (recomanat 4+) |
| Disc | 32 GB lliures |
| Firmware | BIOS o UEFI |

### Windows 11 (64 bits) — requisits estrictes
| Recurs | Mínim |
|---|---|
| Processador | 1 GHz, **2 nuclis**, model de la llista compatible (Intel 8a gen+, AMD Zen 2+) |
| RAM | **4 GB** · Disc **64 GB** |
| Firmware | **UEFI amb *Secure Boot*** |
| Seguretat | **TPM 2.0** |
| Gràfica | DirectX 12 / WDDM 2.0 |

- Verificar el maquinari: `msinfo32`, *Administrador de dispositius* (`devmgmt.msc`), **PC Health Check**, `dxdiag`, `Get-ComputerInfo`.
- A la UEFI: activar **TPM 2.0** i **Secure Boot**, mode SATA en **AHCI**, virtualització (VT-x/AMD-V) si cal.

## 2. Preparar el suport

- ISO oficial de microsoft.com o **Media Creation Tool** (genera l'USB directament).
- USB d'arrencada amb la Media Creation Tool o **Rufus** (esquema **GPT/UEFI** en equips moderns; MBR/BIOS només en maquinari antic).
- Verificar la **suma SHA-256** de la ISO.
- Posar l'USB primer a l'ordre d'arrencada (o menú `F12`).

## 3. Assistent (*Windows Setup*)

1. Arrencada des de l'USB → «Prem qualsevol tecla…».
2. **Idioma, format d'hora, teclat** → *Instal·la ara*.
3. **Clau de producte:** introduir-la o «No tinc clau de producte» (activació posterior).
4. **Edició** (Home / Pro / Education) — ha de coincidir amb la llicència.
5. **Termes de la llicència** → acceptar.
6. **Tipus d'instal·lació:**
   - **Actualització:** conserva fitxers, configuració i aplicacions (només des d'un Windows en marxa).
   - **Personalitzada (avançada):** instal·lació **neta** — l'opció per a un equip nou.
7. **Preparació del disc:**
   - Disc buit: seleccionar l'espai no assignat → *Següent*; Windows crea **ESP + MSR + Windows (C:) + Recuperació** automàticament.
   - *Opcions de la unitat*: **Nou**, **Eliminar**, **Formatar**, **Ampliar**.
   - La partició de Windows és sempre **NTFS** i es formata automàticament (no cal fer-ho a mà).
8. **Còpia de fitxers i reinicis** (treure l'USB quan reinicia).
9. **OOBE (*Out-Of-Box Experience*):**
   - Regió i teclat.
   - **Xarxa:** Windows 11 Home demana connexió i **compte Microsoft**; Pro permet **compte local** (opció «Compte fora de línia», o `Maj+F10` → `start ms-cxh:localonly`).
   - **Nom d'usuari**, **contrasenya** (o PIN) i preguntes de seguretat.
   - Opcions de **privadesa** (ubicació, diagnòstics, publicitat).
10. Arrencada a l'escriptori.

## 4. Particions que crea Windows (UEFI/GPT)

| Partició | Sistema d'arxius | Funció |
|---|---|---|
| **EFI System Partition (ESP)** | FAT32 (~100–300 MB) | Carregadors d'arrencada UEFI |
| **Microsoft Reserved (MSR)** | — (~16 MB) | Reservada per a gestió |
| **Windows (C:)** | NTFS | Sistema i aplicacions |
| **Recuperació (WinRE)** | NTFS (~500 MB) | Entorn de recuperació |
| **Dades (D:)** *(opcional, recomanat)* | NTFS | Documents, separats del sistema |

Particionat manual per CLI dins de Setup (`Maj+F10`):
```
diskpart → list disk → select disk 0 → clean → convert gpt
create partition efi size=300 → format fs=fat32 quick
create partition msr size=16
create partition primary → format fs=ntfs quick → assign letter=C
```

## 5. Windows Boot Manager i arrencada dual (RA2.7)

- Windows usa **Windows Boot Manager** (`bootmgr`) + magatzem **BCD** (*Boot Configuration Data*).

| Tasca | Ordre |
|---|---|
| Veure entrades d'arrencada | `bcdedit /enum` |
| SO per defecte | `bcdedit /default {identificador}` |
| Temps d'espera del menú | `bcdedit /timeout 10` |
| Reparar l'arrencada (WinRE) | `bootrec /fixmbr` · `/fixboot` · `/rebuildbcd` |
| Reconstruir la BCD a UEFI | `bcdboot C:\Windows /s S: /f UEFI` |
| Menú gràfic | `msconfig` → *Arrencada* |

- **Dual boot:** instal·la **Windows primer** i Linux després (GRUB detecta el Windows amb `os-prober`). Si s'ha fet a l'inrevés, Windows amaga el GRUB → reparar-lo des d'un *live USB* ([RA2.1 · gestor d'arrencada](04-gestor-d-arrencada.md)).

## 6. Activació i actualització (RA2.8–RA2.10)

- **Activació:** clau de producte (25 caràcters) o **llicència digital** lligada al maquinari i/o al compte Microsoft. Estat a *Configuració → Sistema → Activació*; CLI `slmgr`.
- **Windows Update:** *Configuració → Windows Update* → instal·lar tots els pedaços; hores actives i pausa; historial i desinstal·lació d'actualitzacions problemàtiques. Aules: **WSUS** / **Windows Update for Business** / Intune.
- Comprovar la integritat: `sfc /scannow`, `DISM /Online /Cleanup-Image /RestoreHealth`.

## 7. Configuració post-instal·lació

| Tasca | On |
|---|---|
| Windows Update | *Configuració → Windows Update* |
| Controladors | Windows Update; els que faltin (triangle groc a `devmgmt.msc`), del web del fabricant |
| Nom de l'equip | *Configuració → Sistema → Aprofundir* |
| Comptes d'usuari | *Configuració → Comptes* / `lusrmgr.msc` ([RA4.2](../04-administracio-del-so/windows.md)) |
| Particions de dades (D:) | `diskmgmt.msc` → volum NTFS |
| Aplicacions bàsiques | navegador, ofimàtica, 7-Zip, lector PDF, antivirus (o Defender), `winget` |
| Punt de restauració | *Crea un punt de restauració* → activar la protecció |

## 8. Instal·lació desatesa / per imatge

- **`autounattend.xml`:** fitxer de respostes a l'arrel de l'USB; es genera amb **Windows System Image Manager (WSIM)** de l'ADK.
- **Sysprep + DISM:** `sysprep /generalize /oobe` en un equip patró → `dism /capture-image` → `dism /apply-image`; eines **MDT** / **Configuration Manager**.
- **Clonezilla:** clonat de disc per a aules.

## 9. Incidències freqüents

| Símptoma | Solució |
|---|---|
| «Aquest PC no pot executar Windows 11» | Activar TPM 2.0 i Secure Boot a la UEFI; comprovar el model de CPU |
| No veu el disc / «no s'ha pogut crear una partició» | Mode SATA a AHCI; desconnectar altres discos/USB; `diskpart` → `clean` |
| «MBR/GPT: Windows no es pot instal·lar en aquest disc» | Arrencar l'USB en mode UEFI i convertir el disc a GPT (`mbr2gpt` o `convert gpt`) |
| Bucle de reinicis a l'OOBE | Desconnectar la xarxa; provar un altre USB/ISO |
| Falta la Wi-Fi després d'instal·lar | Connectar per cable, Windows Update, o driver des d'un altre equip |
| Activació fallida | Solucionador d'activació; vincular la llicència digital al compte Microsoft |

> Documenta **totes** les incidències i la solució a la fitxa de l'equip.

## Comprova què has après

1. Quins tres requisits «nous» demana Windows 11 i no Windows 10?
2. Quina opció de l'assistent fa una instal·lació neta?
3. Com crees un compte **local** a Windows 11 durant l'OOBE?
4. Quines particions crea automàticament Windows en un disc GPT buit?
5. Quina ordre reconstrueix la BCD i quan la faries servir?
6. Per a què serveix `autounattend.xml`?

---

[⬅ Anterior: Llicències, actualització i incidències](07-llicencies-actualitzacio-i-incidencies.md)
