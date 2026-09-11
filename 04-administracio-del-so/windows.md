[🏠 Inici](../README.md) › [RA4 · Administració del sistema operatiu](00-index.md) › **RA4.2 · Administració a Windows**

[⬅ Anterior: Monitoratge, rendiment i registres](05-monitoratge-rendiment-i-registres.md) · [Bloc següent: Màquines virtuals ➡](../05-maquines-virtuals/00-index.md)

# RA4.2 · Administració a Windows

> Repàs comparatiu centrat en **Windows 10/11**. Cobreix els mateixos criteris d'avaluació de RA4 (RA4.1–RA4.9)
> amb les eines pròpies del sistema. El desenvolupament a fons és a [RA4.1 · Linux i multiplataforma](00-index.md).

## 1. Usuaris i grups (RA4.1)

- **Identificador intern:** SID. **Perfil:** `C:\Users\<usuari>` (plantilla `C:\Users\Default`, comú `C:\Users\Public`).
- **Comptes predefinits:** *Administrador* (deshabilitat per defecte), *Convidat* (deshabilitat), compte inicial de l'OOBE (grup **Administradors**), comptes de servei `SYSTEM`, `LOCAL SERVICE`, `NETWORK SERVICE`.
- **Tipus de compte:** estàndard vs. administrador; l'elevació de privilegis passa per **UAC**.

| Tasca | GUI | CLI |
|---|---|---|
| Gestió completa | `lusrmgr.msc` (*Usuaris i grups locals*, Pro/Enterprise) | — |
| Bàsica | *Configuració → Comptes → Altres usuaris* | — |
| Crear usuari | `lusrmgr.msc` → *Usuari nou* | `net user anna P@ss! /add /fullname:"Anna Roca"` · `New-LocalUser` |
| Contrasenya | *Estableix la contrasenya* | `net user anna *` · `Set-LocalUser` |
| Deshabilitar | Casella *El compte està deshabilitat* | `net user anna /active:no` |
| Afegir a un grup | Pestanya *Membre de* | `net localgroup Administradores anna /add` · `Add-LocalGroupMember` |
| Esborrar | *Suprimeix* | `net user anna /delete` (el perfil `C:\Users\anna` **no** s'esborra sol) |

- **Grups locals per defecte:** Administradors, Usuaris, Convidats, **Operadors de còpia**, Usuaris d'escriptori remot, Operadors de configuració de xarxa…
- **Política de contrasenyes:** `secpol.msc` → *Directives de comptes → Directiva de contrasenyes* (longitud, complexitat, historial, vigència màx./mín.) i *Directiva de bloqueig de comptes*.
- Forçar canvi al següent inici: `net user anna /logonpasswordchg:yes`.

## 2. Permisos NTFS i recursos compartits (RA4.2, RA4.8)

- **Permís** = sobre un recurs; **dret d'usuari** = sobre el sistema (`secpol.msc → Assignació de drets d'usuari`).
- **ACL NTFS:** cada fitxer/carpeta té una llista d'entrades (ACE). Permisos: **Control total, Modificar, Llegir i executar, Mostrar contingut, Llegir, Escriure**.
  - **Herència** activada per defecte; es pot trencar en un element.
  - **Denegar** té prioritat sobre **Permetre**.
  - **Propietari:** qui crea l'element; un administrador pot *prendre'n possessió*.
- Eines: clic dret → *Propietats → Seguretat* (i *Avançat*); CLI **`icacls`**:
  ```
  icacls C:\Dades
  icacls C:\Dades /grant anna:(OI)(CI)M      :: Modificar amb herència
  icacls C:\Dades /remove:g "Usuaris"
  icacls C:\Dades /inheritance:r             :: treure l'herència
  icacls C:\Dades /setowner Administradores /T
  ```
  PowerShell: `Get-Acl`, `Set-Acl`.

### Compartir per xarxa (SMB)

- Clic dret → *Propietats → Ús compartit → Ús compartit avançat* → *Permisos* (permisos **de recurs compartit**: Llegir / Canviar / Control total).
- **Actuen dos nivells alhora** (recurs compartit + NTFS); el resultat efectiu és **el més restrictiu**.
- Recursos administratius ocults: `C$`, `ADMIN$`, `IPC$`.
- CLI:
  ```
  net share Dades=C:\Dades /grant:anna,change
  net share
  net share Dades /delete
  net use Z: \\PC07\Dades /persistent:yes    :: client
  ```
- Impressores: *Propietats de la impressora → Ús compartit*.
- Compartir amb el **privilegi mínim**; no exposar a *Tothom* sense necessitat; SMB 3 xifra en trànsit.

### Veure l'organització dels arxius

Explorador de fitxers (vista d'arbre, columnes de mida/data/tipus), *Propietats* d'unitat (espai usat/lliure), **WizTree** / **TreeSize** (mapa d'ús d'espai).

## 3. Processos i serveis (RA4.3, RA4.4)

### Processos — Administrador de tasques (`Ctrl+Maj+Esc`)

- Pestanyes: **Processos**, **Rendiment**, **Historial d'aplicacions**, **Aplicacions d'inici**, **Usuaris**, **Detalls**, **Serveis**.
- A *Detalls*, clic dret: *Finalitza la tasca*, *Finalitza l'arbre de processos*, *Estableix la prioritat*, *Estableix l'afinitat*, *Vés al servei*, *Obre la ubicació del fitxer*.
- Prioritats: *Temps real, Alta, Superior a la normal, Normal, Inferior a la normal, Baixa* (compte amb *Temps real*).
- Eines avançades: **Monitor de recursos** (`resmon`), **Process Explorer** (Sysinternals).

```
tasklist                    :: llistar (PID, memòria, sessió)
tasklist /svc               :: serveis dins de cada procés
taskkill /IM notepad.exe    :: matar per nom
taskkill /PID 4321 /F       :: forçar per PID
taskkill /PID 4321 /T /F    :: + arbre de fills
```
PowerShell: `Get-Process`, `Stop-Process -Id 4321 -Force`, `Start-Process`, `(Get-Process x).PriorityClass='BelowNormal'`.

### Serveis — `services.msc`

- Propietats: **General** (tipus d'inici; Inicia/Atura/Pausa/Reprèn), **Inici de sessió** (compte), **Recuperació** (què fer si falla), **Dependències**.
- Tipus d'inici: **Automàtic**, **Automàtic (inici retardat)**, **Manual**, **Deshabilitat**.
- Si atures un servei del qual en depenen d'altres, aquests també s'aturen.

```
sc query                          :: llistar
sc query Spooler                  :: estat d'un servei
net start Spooler / net stop Spooler
sc config Spooler start= auto     :: (auto | demand | disabled) — ull a l'espai després de "="
sc qc Spooler                     :: configuració i dependències
```
PowerShell: `Get-Service`, `Start-Service`, `Stop-Service`, `Restart-Service`, `Set-Service Spooler -StartupType Automatic`.

> Deshabilitar serveis «per guanyar rendiment» pot trencar funcionalitats (xarxa, àudio, actualitzacions). Documenta els canvis.

## 4. Monitoratge, rendiment i el Registre (RA4.5–RA4.7, RA4.9)

| Eina | Ús |
|---|---|
| Administrador de tasques → *Rendiment* | Vista ràpida de CPU, memòria, disc, xarxa, GPU |
| **Monitor de recursos** (`resmon`) | Detall per procés; fitxers en ús, xarxa, memòria |
| **Monitor de rendiment** (`perfmon`) | Comptadors i registres (*conjunts de recopiladors de dades*), informes |
| **Visor d'esdeveniments** (`eventvwr.msc`) | Registres: Aplicació, Seguretat, Sistema, Configuració. Nivells: Informació, Advertència, Error, Crític |
| **Fiabilitat** (`perfmon /rel`) | Historial d'errors i estabilitat |
| PowerShell / `wevtutil` | `Get-Counter`, `Get-WinEvent -LogName System -MaxEvents 50`; consultar/exportar registres |

### Optimització de la memòria

- Revisar **aplicacions d'inici**; detectar **fuites** (procés amb RAM que només creix → reiniciar/actualitzar).
- **Fitxer de paginació** (memòria virtual): *Propietats del sistema → Rendiment → Opcions avançades → Memòria virtual*; en equips amb diversos discos, posar-lo en un SSD diferent del del sistema.
- **Compressió de memòria** (automàtica) redueix la pressió abans de recórrer al disc.
- Afegir RAM és la millora més efectiva si hi ha ús constant de paginació.

### Optimització de l'emmagatzematge

- **HDD:** *Desfragmenta i optimitza les unitats* (`dfrgui`, `defrag C: /O`), programat setmanalment.
- **SSD:** *Optimitza* fa **TRIM** automàticament (setmanal). **No desfragmentar.**
- Salut del disc: **SMART** (`wmic diskdrive get status`, eines del fabricant).
- Neteja: *Sensor d'emmagatzematge*, *Neteja de disc* (`cleanmgr`), `DISM /Online /Cleanup-Image /StartComponentCleanup`.

### El Registre de Windows

Base de dades jeràrquica de tota la configuració del SO, el maquinari i les aplicacions. Eina: **`regedit`**.

| Branca (*hive*) | Contingut |
|---|---|
| `HKEY_LOCAL_MACHINE` (HKLM) | Configuració de l'equip: maquinari, drivers, serveis, programari per a tots els usuaris |
| `HKEY_CURRENT_USER` (HKCU) | Configuració de l'usuari amb sessió (fitxer `NTUSER.DAT`) |
| `HKEY_USERS` | Perfils de tots els usuaris |
| `HKEY_CLASSES_ROOT` | Associacions de fitxers i objectes COM |
| `HKEY_CURRENT_CONFIG` | Perfil de maquinari actual |

CLI: `reg query`, `reg add`, `reg export`. **Exporta sempre la branca abans d'editar-la.**

### Rendiment general

- *Propietats del sistema → Rendiment*: efectes visuals (*Ajusta per obtenir el millor rendiment*), prioritat serveis vs. aplicacions.
- **Plans d'energia:** *Alt rendiment* vs. *Estalvi d'energia*.
- Mesurar una **línia base** per poder comparar quan alguna cosa va malament.

## Comprova què has après

1. Quina consola de Windows permet la gestió completa d'usuaris i grups locals i en quines edicions hi és?
2. En compartir una carpeta, quins dos conjunts de permisos actuen i quin preval?
3. Diferència entre `taskkill /PID 100` i `taskkill /PID 100 /T /F`.
4. Quina ordre de `sc` posa un servei en inici automàtic i quin detall de sintaxi cal vigilar?
5. Quines dues branques del Registre separen la configuració de l'equip i la de l'usuari?
6. Què fa *Optimitza* sobre un SSD i què no s'hi ha de fer mai?

---

[⬅ Anterior: Monitoratge, rendiment i registres](05-monitoratge-rendiment-i-registres.md) · [Bloc següent: Màquines virtuals ➡](../05-maquines-virtuals/00-index.md)
