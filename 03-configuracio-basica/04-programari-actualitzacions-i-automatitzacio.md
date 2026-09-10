[🏠 Inici](../README.md) › [RA3 · Configuració bàsica del sistema operatiu](00-index.md) › **4. Programari, actualitzacions i automatització de tasques**

[⬅ Anterior: Gestió de discos](03-gestio-de-discos-i-sistemes-d-arxius.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Recuperació del SO ➡](05-recuperacio-del-so.md)

# 4. Programari, actualitzacions i automatització de tasques

> Criteris d'avaluació RA3.5–RA3.8 — *configuració per a l'actualització del SO; instal·lació/desinstal·lació
> d'utilitats; assistents de configuració; automatització de tasques.*

## 4.1. Instal·lació i desinstal·lació de programari

### Windows

| Mètode | Instal·lar | Desinstal·lar |
|---|---|---|
| **Microsoft Store** | Cerca → *Obtén* | *Configuració → Aplicacions → Aplicacions instal·lades* → *Desinstal·la* |
| **Instal·lador clàssic** `.exe` / `.msi` | Executar-lo i seguir l'assistent | *Aplicacions instal·lades* o *Tauler de control → Programes i característiques* |
| **`winget`** (gestor de paquets de Windows) | `winget install Mozilla.Firefox` | `winget uninstall Mozilla.Firefox` · `winget upgrade --all` |
| **Característiques opcionals de Windows** | *Configuració → Aplicacions → Característiques opcionals*; `optionalfeatures` (activar IIS, Hyper-V, WSL…) | Desmarcar la característica |
| **Portable** | Descomprimir i executar | Esborrar la carpeta |

### Linux (Debian/Ubuntu)

| Mètode | Instal·lar | Desinstal·lar |
|---|---|---|
| **`apt`** (repositoris de la distribució) | `sudo apt install gimp` | `sudo apt remove gimp` · `sudo apt purge gimp` (també la config) |
| **`.deb`** solt | `sudo apt install ./paquet.deb` (resol dependències) | `sudo apt remove nom-paquet` |
| **Snap** | `sudo snap install codi` | `sudo snap remove codi` |
| **Flatpak** (Flathub) | `flatpak install flathub org.gimp.GIMP` | `flatpak uninstall org.gimp.GIMP` |
| **App Center / GNOME Software** | Botó *Instal·la* | Botó *Desinstal·la* |
| Codi font | `./configure && make && sudo make install` | `sudo make uninstall` (si el `Makefile` ho preveu) |

- Fedora/RHEL: `sudo dnf install/remove`; openSUSE: `sudo zypper install/remove`; Arch: `sudo pacman -S/-R`.
- Convertir paquets entre formats (llegat): `alien` (`.rpm` ↔ `.deb`).
- Cercar: `apt search`, `winget search`, `snap find`.

> **Avantatge dels gestors de paquets:** resolen **dependències**, permeten **actualitzar tot el programari
> alhora** i el desinstal·len net. És el model per defecte a Linux i cada cop més a Windows (`winget`).

## 4.2. Configuració de l'actualització del SO

### Windows Update

- *Configuració → Windows Update*: cercar, instal·lar, **pausar** fins a 5 setmanes, definir **hores actives**
  (no reiniciar durant classe), *Opcions avançades* → rebre actualitzacions d'altres productes de Microsoft,
  optimització de lliurament (P2P a la LAN).
- Empreses/aules: **WSUS**, **Windows Update for Business** (polítiques de grup) o **Intune**.
- Veure historial i **desinstal·lar** una actualització problemàtica.

### Linux

- **Actualitzacions automàtiques de seguretat:** `sudo apt install unattended-upgrades` +
  `sudo dpkg-reconfigure unattended-upgrades`; configuració a `/etc/apt/apt.conf.d/50unattended-upgrades`.
- GNOME: *Programari i actualitzacions* → pestanya *Actualitzacions* (freqüència de comprovació, com aplicar
  les de seguretat).
- Manual: `sudo apt update && sudo apt full-upgrade`.

Vegeu també [RA2 · llicències i actualització](../02-instal-lacio-de-so/07-llicencies-actualitzacio-i-incidencies.md).

## 4.3. Assistents de configuració del sistema

Els SO inclouen **assistents** per a tasques de configuració guiada:

| Tasca | Windows | Linux |
|---|---|---|
| Connectar a una xarxa Wi-Fi | Icona de xarxa → triar SSID → contrasenya | Icona de xarxa (NetworkManager) o `nmtui` / `nmcli` |
| Configurar IP fixa | *Configuració → Xarxa → Propietats → Edita IP* | *Configuració → Xarxa*, `nmtui`, o `netplan` a `/etc/netplan/*.yaml` |
| Afegir una impressora | *Configuració → Bluetooth i dispositius → Impressores i escàners* | *Configuració → Impressores* (CUPS, `http://localhost:631`) |
| Afegir maquinari nou | *Administrador de dispositius* detecta i demana driver | *udev* detecta; `ubuntu-drivers` per als propietaris |
| Comptes en línia / correu | *Comptes → Correu electrònic i comptes* | *Configuració → Comptes en línia* |
| Assistent de primer inici | OOBE | GNOME *Benvinguda inicial* |
| Configurar còpies de seguretat | *Historial de fitxers*, *Còpia de seguretat i restauració* | *Còpies de seguretat* (Déjà Dup), `timeshift` |

## 4.4. Automatització de tasques

### Windows — Programador de tasques (*Task Scheduler*, `taskschd.msc`)

- Crea una **tasca** amb: **desencadenadors** (a una hora, a l'inici de sessió, a l'arrencada, per esdeveniment,
  en repòs), **accions** (executar un programa/script), **condicions** (només amb corrent, si l'equip està
  ociós) i **configuració** (reintents, executar encara que hagi passat l'hora).
- CLI: `schtasks`
  ```
  schtasks /Create /SC DAILY /TN "CopiaDades" /TR "C:\Scripts\copia.bat" /ST 22:00
  schtasks /Run /TN "CopiaDades"
  schtasks /Delete /TN "CopiaDades" /F
  ```
- PowerShell: `Register-ScheduledTask`, `New-ScheduledTaskTrigger`, `New-ScheduledTaskAction`.

### Linux — `cron`

Cada usuari té la seva **taula de cron** (`crontab -e`); les del sistema són a `/etc/crontab` i `/etc/cron.d/`,
i hi ha directoris `/etc/cron.{hourly,daily,weekly,monthly}`.

Format d'una línia (`crontab(5)`):

```
┌── minut (0-59)
│ ┌── hora (0-23)
│ │ ┌── dia del mes (1-31)
│ │ │ ┌── mes (1-12)
│ │ │ │ ┌── dia de la setmana (0-7; 0 i 7 = diumenge)
│ │ │ │ │
* * * * *  ordre-a-executar
```

Exemples:

```cron
0 22 * * *        /home/anna/scripts/copia.sh          # cada dia a les 22:00
*/15 * * * *      /usr/local/bin/comprova.sh           # cada 15 minuts
0 3 * * 1         apt-get -y update && apt-get -y upgrade  # cada dilluns a les 3:00
@reboot          /home/anna/scripts/inici.sh           # en arrencar
```

- `crontab -l` (llistar), `crontab -r` (esborrar), `crontab -e` (editar).
- Execucions puntuals: `at 23:00` + ordre (paquet `at`).
- **`systemd timers`** (alternativa moderna): unitats `.timer` + `.service`; `systemctl list-timers`. Més
  flexibles (`OnCalendar=`, `Persistent=true` per recuperar execucions perdudes).
- Anacron executa tasques periòdiques encara que l'equip estigués apagat a l'hora prevista.

### Scripts

- **Windows:** fitxers per lots `.bat`/`.cmd` o scripts **PowerShell** `.ps1`.
- **Linux:** scripts de shell `.sh` (primera línia `#!/bin/bash`, permís d'execució amb `chmod +x`).

## 4.5. Resum

- Instal·lació/desinstal·lació: botiga, instal·ladors `.exe`/`.msi`, **`winget`** (Windows); **`apt`**, `.deb`,
  Snap, Flatpak (Linux). Els gestors de paquets resolen dependències i actualitzen tot alhora.
- Actualització del SO: Windows Update (hores actives, pausa, WSUS) / `unattended-upgrades` + `apt full-upgrade`.
- **Assistents** per a Wi-Fi, IP, impressores, maquinari, comptes, còpies.
- Automatització: **Programador de tasques** / `schtasks` (Windows); **`cron`** / `systemd timers` / `at` (Linux).

## Comprova què has après

1. Quin avantatge principal té instal·lar programari amb `apt` o `winget` en lloc de baixar cada `.exe`?
2. Diferència entre `apt remove` i `apt purge`.
3. Escriu la línia de cron per executar `/opt/backup.sh` cada dia a les 23:30.
4. Com evites que Windows reiniciï per actualitzacions durant l'horari de classe?
5. Quins tres elements defineixes en una tasca del Programador de tasques de Windows?

---

[⬅ Anterior: Gestió de discos](03-gestio-de-discos-i-sistemes-d-arxius.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Recuperació del SO ➡](05-recuperacio-del-so.md)
