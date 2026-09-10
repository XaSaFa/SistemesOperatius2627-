[🏠 Inici](../README.md) › [RA3 · Configuració bàsica del sistema operatiu](00-index.md) › **RA3.2 · Configuració a Windows**

[⬅ Anterior: Recuperació del sistema operatiu](05-recuperacio-del-so.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Bloc següent: Instal·lació ➡](../02-instal-lacio-de-so/00-index.md)

# RA3.2 · Configuració a Windows

> Repàs comparatiu centrat en **Windows 10/11**. Cobreix els mateixos criteris de RA3 (RA3.1–RA3.8) amb les
> eines pròpies del sistema. El desenvolupament a fons és a [RA3.1 · Linux i multiplataforma](00-index.md).

## 1. Arrencada, parada i sessions (RA3.1)

- **Seqüència:** POST (BIOS/UEFI) → Windows Boot Manager → nucli → `smss.exe` → `wininit.exe`/`csrss.exe` → `services.exe` → `winlogon.exe` → pantalla d'inici de sessió.
- **Sessió:** carrega el perfil (`C:\Users\<usuari>`), les preferències i els permisos de l'usuari.

| Acció | GUI | CLI |
|---|---|---|
| Apagar / Reiniciar | Inici → Apagar / Reinicia | `shutdown /s /t 0` · `shutdown /r /t 0` |
| Apagar d'aquí a 60 s / cancel·lar | — | `shutdown /s /t 60` · `shutdown /a` |
| Reinici a opcions avançades | Maj + *Reinicia* | `shutdown /r /o /t 0` |
| Tancar / bloquejar sessió | Menú Inici → usuari | `shutdown /l` / `logoff` · `Win+L` (bloquejar) |
| Suspèn / Hiberna | Menú d'apagada | `powercfg /h on` per activar la hibernació |

- Bloquejar ≠ tancar sessió: bloquejar manté les aplicacions obertes darrere d'una contrasenya.
- **Inici ràpid (*Fast Startup*):** en «apagar» desa l'estat del nucli (hibernació parcial). Pot donar problemes en **dual boot** i en muntar NTFS des de Linux → desactivar-lo a *Opcions d'energia → Comportament dels botons d'inici/apagada*.
- Aturar sempre amb `shutdown` per no corrompre el sistema d'arxius.

## 2. Interfícies i preferències (RA3.1–RA3.2)

- **GUI vs. CLI:** la GUI és exploratòria i visual; la CLI (**PowerShell**) és ràpida, lleugera i automatitzable. Gairebé tota acció de *Configuració* té equivalent per ordres.
- **Elements de l'entorn:** barra de tasques + menú Inici, *safata del sistema* (àrea de notificació), *Vista de tasques* (`Win+Tab`, escriptoris virtuals), Explorador de fitxers, *Configuració* (i Tauler de control, llegat).

| Preferència | On |
|---|---|
| Fons, colors, tema clar/fosc | *Configuració → Personalització* |
| Resolució, escala, múltiples pantalles | *Sistema → Pantalla* |
| Idioma, regió, teclat | *Hora i idioma* |
| Data, hora i zona horària | *Hora i idioma → Data i hora* |
| Energia (suspensió, brillantor) | *Sistema → Energia i bateria* |
| Aplicacions predeterminades | *Aplicacions → Aplicacions predeterminades* |
| Aplicacions d'inici | *Administrador de tasques → Aplicacions d'inici* |
| Opcions de l'Explorador (extensions, ocults, vista) | *Explorador → ⋯ → Opcions* |

- **Per línia d'ordres:** perfil `$PROFILE` de PowerShell (àlies, funcions, prompt); variables d'entorn amb `setx` o *Configuració → Sistema → Aprofundir → Variables d'entorn*.
- Cada usuari té el seu **perfil**; el que canvia un usuari no afecta els altres.

## 3. Gestió de discos i sistemes d'arxius (RA3.3)

| Operació | GUI (`diskmgmt.msc`) | CLI |
|---|---|---|
| Veure discos i volums | Administració de discos | `diskpart` → `list disk` / `list volume`; `Get-Disk`, `Get-Partition` |
| Crear partició | *Volum nou* | `diskpart` → `create partition primary size=…` |
| Formatar | Clic dret → *Formata* | `format X: /FS:NTFS /Q` · `Format-Volume` |
| Assignar lletra / etiqueta | *Canvia lletra…* / *Canvia el nom* | `diskpart` → `assign letter=E` / `label` |
| Ampliar / reduir | *Amplia / Redueix el volum* (no destructiu) | `diskpart` → `extend` / `shrink` · `Resize-Partition` |
| Eliminar volum | *Suprimeix el volum* | `diskpart` → `delete partition` |
| Convertir MBR ↔ GPT (sense dades) | — | `mbr2gpt` (des de WinRE), `diskpart` → `convert gpt` |

- Les particions reben una **lletra** (`C:`, `D:`…); alternativa: muntar un volum en una **carpeta buida NTFS** (punt de muntatge).
- **Comprovació i reparació:** `chkdsk C: /F /R` (`/F` errors lògics, `/R` sectors dolents; l'arrel al pròxim reinici). Integritat del sistema: `sfc /scannow`, `DISM /Online /Cleanup-Image /RestoreHealth`.
- **HDD** → *Desfragmenta i optimitza* (`dfrgui`). **SSD** → *Optimitza* fa **TRIM** (setmanal); no desfragmentar.
- **Compressió transparent NTFS** (*Propietats → Avançades → Comprimeix*) ≠ arxivador ZIP (natiu a l'Explorador; `tar` també és natiu).
- **Xifratge de volum:** BitLocker (Windows Pro).
- **Neteja d'espai:** *Sensor d'emmagatzematge*, *Neteja de disc* (`cleanmgr`).

`FAT → NTFS` sense perdre dades (llegat però vàlid): `convert C: /FS:NTFS` (irreversible sense eines de tercers).

## 4. Programari i automatització (RA3.5–RA3.8)

### Instal·lar i desinstal·lar

| Mètode | Instal·lar | Desinstal·lar |
|---|---|---|
| **Microsoft Store** | Cerca → *Obtén* | *Configuració → Aplicacions instal·lades* |
| **`.exe` / `.msi`** | Executar l'assistent | *Aplicacions instal·lades* / *Programes i característiques* |
| **`winget`** | `winget install Mozilla.Firefox` · `winget upgrade --all` | `winget uninstall Mozilla.Firefox` |
| **Característiques opcionals** | `optionalfeatures` (IIS, Hyper-V, WSL…) | Desmarcar |
| **Portable** | Descomprimir i executar | Esborrar la carpeta |

> `winget` (com `apt` a Linux) resol dependències, actualitza tot alhora i desinstal·la net.

### Actualitzacions del SO — Windows Update

- *Configuració → Windows Update*: cercar, **pausar** fins a 5 setmanes, **hores actives** (no reiniciar durant classe), *Opcions avançades* (altres productes de Microsoft, optimització de lliurament P2P).
- Historial i **desinstal·lar** una actualització problemàtica.
- Aules/empreses: **WSUS**, **Windows Update for Business** (directives de grup), **Intune**.

### Assistents de configuració

Wi-Fi (icona de xarxa), IP fixa (*Xarxa → Propietats → Edita IP*), impressores (*Bluetooth i dispositius → Impressores*), maquinari nou (*Administrador de dispositius*), comptes en línia, còpies (*Historial de fitxers*, *Còpia de seguretat i restauració*).

### Automatització — Programador de tasques (`taskschd.msc`)

Una **tasca** té: **desencadenadors** (a una hora, a l'inici de sessió, a l'arrencada, per esdeveniment, en repòs), **accions** (executar un programa/script), **condicions** (només amb corrent, si l'equip està ociós) i **configuració** (reintents).

```
schtasks /Create /SC DAILY /TN "CopiaDades" /TR "C:\Scripts\copia.bat" /ST 22:00
schtasks /Run /TN "CopiaDades"
schtasks /Delete /TN "CopiaDades" /F
```
PowerShell: `Register-ScheduledTask`, `New-ScheduledTaskTrigger`, `New-ScheduledTaskAction`.
Scripts: fitxers per lots `.bat`/`.cmd` o **PowerShell** `.ps1`.

## 5. Recuperació del sistema (RA3.4)

### Punts de restauració

- Còpia de fitxers de sistema, registre i drivers (**no** dels documents).
- Activar: *Crea un punt de restauració → Configura → activar protecció*.
- Es creen automàticament abans d'instal·lar drivers/actualitzacions; restaurar amb `rstrui` o des de WinRE.

### Windows RE (entorn de recuperació)

S'hi entra amb `Maj` + *Reinicia*, 3 arrencades fallides seguides, o des d'un USB d'instal·lació → *Repara l'equip*:

- **Reparació d'inici** (gestor d'arrencada i fitxers d'arrencada).
- **Desinstal·la actualitzacions** (de qualitat o de característiques).
- **Restauració del sistema** (punt de restauració) i **recuperació d'imatge del sistema**.
- **Símbol del sistema:** `bootrec /fixmbr` · `/fixboot` · `/rebuildbcd`, `chkdsk`, `sfc`, `DISM`, `bcdedit`.

### Mode segur

Arrenca amb controladors i serveis mínims (opcionalment amb xarxa o amb símbol del sistema). Útil per treure un driver o programa que impedeix arrencar. Accés des de WinRE → *Configuració d'inici* o `msconfig → Arrencada → Arrencada segura`.

### Restablir / imatge / còpia

- **Restableix aquest PC:** *Configuració → Sistema → Recuperació* (conservar fitxers o eliminar-ho tot).
- **Imatge del sistema (llegat):** *Còpia de seguretat i restauració (Windows 7)*; restauració des de WinRE.
- **Historial de fitxers:** còpia contínua a un disc extern. **Unitat de recuperació** (USB).
- Regla de còpies **3-2-1**: 3 còpies, 2 suports, 1 fora de l'equip.

## Comprova què has après

1. Per què pot ser problemàtic l'*inici ràpid* de Windows en un equip amb dual boot?
2. On configures les aplicacions que s'inicien amb la sessió?
3. Diferència entre `chkdsk /F` i `chkdsk /R`.
4. Quin avantatge té instal·lar amb `winget` en lloc de baixar cada `.exe`?
5. Escriu l'ordre `schtasks` per executar `C:\backup.bat` cada dia a les 22:00.
6. Com entres a WinRE si Windows ni tan sols arrenca?

---

[⬅ Anterior: Recuperació del sistema operatiu](05-recuperacio-del-so.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Bloc següent: Instal·lació ➡](../02-instal-lacio-de-so/00-index.md)
