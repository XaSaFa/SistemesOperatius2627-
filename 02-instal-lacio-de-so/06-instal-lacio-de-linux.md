[🏠 Inici](../README.md) › [RA2 · Instal·lació de sistemes operatius](00-index.md) › **6. Instal·lació de Linux**

[⬅ Anterior: Instal·lació de Windows](05-instal-lacio-de-windows.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Llicències i actualització ➡](07-llicencies-actualitzacio-i-incidencies.md)

# 6. Instal·lació de Linux

> Criteris d'avaluació RA2.5–RA2.6 i RA2.8. Es descriu **Ubuntu 24.04 LTS** com a exemple (els llibres
> descriuen Ubuntu 11.10). El procediment és equivalent a Linux Mint, Debian o Fedora.

## 6.1. Distribucions i suport

- El **nucli** és Linux; una **distribució** hi afegeix l'instal·lador, l'entorn d'escriptori (GNOME, KDE,
  XFCE…), el gestor de paquets i les aplicacions.
- Famílies: **Debian → Ubuntu → Linux Mint**; **Red Hat → Fedora / RHEL / Rocky / Alma**; **SUSE → openSUSE**.
- **LTS (*Long-Term Support*):** Ubuntu allibera una versió LTS cada 2 anys amb **5 anys** de suport (10 amb
  Ubuntu Pro). Recomanable per a aules i empreses.

## 6.2. Preparació del suport

1. Descarregar la **ISO** del web oficial i comprovar-ne la **suma SHA-256** (i, si es vol, la signatura GPG).
2. Crear l'USB d'arrencada:
   - Windows: **Rufus** o **balenaEtcher**.
   - Linux: **Startup Disk Creator**, `Discs` (GNOME) o `sudo dd if=ubuntu.iso of=/dev/sdX bs=4M status=progress oflag=sync`.
3. UEFI: normalment **no cal desactivar Secure Boot** (Ubuntu, Fedora i Debian estan signats). Posar l'USB
   primer o usar el menú d'arrencada.

## 6.3. Mode *Live* i inici de l'instal·lador

En arrencar l'USB apareix un menú (GRUB) amb opcions com:

- **Try or Install Ubuntu** — carrega un escriptori *live* en memòria; res no toca el disc. Serveix per provar
  maquinari, rescatar dades i, des d'aquí, llançar l'instal·lador (icona *Install*).
- **Check disc for defects** — verifica el suport.
- **Test memory** (`memtest86+`) — comprova la RAM.
- **Boot from first hard disk** — arrenca el SO ja instal·lat.

## 6.4. Passos de l'instal·lador (Ubuntu 24.04)

1. **Idioma** i **accessibilitat**.
2. **Disposició del teclat**.
3. **Xarxa** (cable o Wi-Fi) — recomanable per baixar actualitzacions i còdecs.
4. **Tipus d'instal·lació d'aplicacions:** *Instal·lació per defecte* o *mínima*.
5. **Programari de tercers:** marcar-ho per instal·lar còdecs multimèdia i controladors propietaris (Wi-Fi, gràfica NVIDIA).
6. **Preparació del disc:**
   - **Esborra el disc i instal·la Ubuntu** (*particionat guiat*): crea automàticament l'ESP i l'arrel; opció
     de xifrar amb LUKS i d'usar LVM.
   - **Instal·la Ubuntu al costat de…** (*dual boot*): redimensiona la partició de Windows i s'instal·la a
     l'espai lliure. GRUB detecta el Windows.
   - **Alguna cosa més** (*particionat manual*): l'usuari crea cada partició. Cal definir com a mínim:
     | Punt de muntatge | Tipus | Mida |
     |---|---|---|
     | ESP (`/boot/efi`) | Partició de sistema EFI (FAT32) | 300–512 MB (només UEFI) |
     | `/` (arrel) | ext4 (o Btrfs) | 25–60 GB o més |
     | `/home` (opcional però recomanat) | ext4 | resta del disc |
     | `swap` (opcional) | àrea d'intercanvi | ≈ mida de la RAM per hibernar, o fitxer `/swapfile` |
     Cal indicar també el disc on s'instal·la el **carregador d'arrencada** (GRUB).
7. **Zona horària**.
8. **Compte d'usuari:** nom complet, **nom d'usuari (login)**, **nom de l'equip (hostname)**, **contrasenya**;
   opció d'inici de sessió automàtic o de xifrar la carpeta personal.
9. **Còpia de fitxers** i instal·lació de GRUB.
10. **Reinici**: treure l'USB. Primer inici: sessió amb el compte creat.

> A Ubuntu **no hi ha contrasenya de `root`** activada per defecte: el primer usuari té privilegis
> d'administració mitjançant **`sudo`** (i pertany al grup `sudo`).

## 6.5. Configuració post-instal·lació

```bash
sudo apt update && sudo apt full-upgrade      # actualitzar el sistema
sudo apt install build-essential curl git ufw # eines habituals
sudo ubuntu-drivers autoinstall               # controladors propietaris (gràfica, Wi-Fi)
sudo apt install ubuntu-restricted-extras     # còdecs, tipus de lletra
```

- **Programari:** *App Center* (GNOME Software), `apt`, **Snap** i, opcionalment, **Flatpak** (Flathub).
- **Nom de l'equip:** `sudo hostnamectl set-hostname AULA1-PC07`.
- **Tallafoc:** `sudo ufw enable`.
- **Usuaris i grups:** `adduser`, `usermod` → [RA4](../04-administracio-del-so/01-usuaris-grups-i-contrasenyes.md).
- **Muntatge de particions al costat del Windows:** afegir entrades a `/etc/fstab`
  ([RA3 · gestió de discos](../03-configuracio-basica/03-gestio-de-discos-i-sistemes-d-arxius.md)).

## 6.6. Instal·lació automatitzada (visió general)

| Distribució | Mecanisme |
|---|---|
| Ubuntu Server | **autoinstall** (fitxer `user-data` YAML + cloud-init) |
| Debian | **preseed** (`preseed.cfg`) |
| Fedora / RHEL | **Kickstart** (`ks.cfg`) |
| Multiplataforma | Clonat amb **Clonezilla**; desplegament per **PXE** |

## 6.7. Incidències freqüents

| Símptoma | Solució |
|---|---|
| L'USB no arrenca en UEFI | Regravar amb `dd`/Rufus (mode GPT), provar amb/sense Secure Boot |
| No es veu el disc NVMe | Actualitzar la BIOS; desactivar RAID/Intel RST (mode AHCI) |
| Wi-Fi o gràfica no funciona | Connectar per cable i `sudo ubuntu-drivers autoinstall`; instal·lar el firmware corresponent |
| Pantalla negra en arrencar (gràfica) | Al menú de GRUB, editar l'entrada i afegir `nomodeset`; després instal·lar el driver |
| Rellotge desquadrat en dual boot amb Windows | `timedatectl set-local-rtc 1` a Linux o ajustar Windows perquè usi UTC |
| GRUB no mostra Windows | `sudo apt install os-prober`, `GRUB_DISABLE_OS_PROBER=false` a `/etc/default/grub`, `sudo update-grub` |

## 6.8. Resum

- Distribució + LTS per a estabilitat; ISO oficial verificada; USB amb Rufus/`dd`/Startup Disk Creator.
- Mode **Live** per provar; instal·lador amb particionat **guiat / al costat de Windows / manual**
  (ESP + `/` ext4 + `/home` + swap).
- El primer usuari administra amb **`sudo`** (sense contrasenya de root).
- Post-instal·lació: `apt update && full-upgrade`, `ubuntu-drivers autoinstall`, còdecs, hostname, tallafoc.

## Comprova què has après

1. Què és una distribució i què hi aporta respecte del nucli?
2. Per a què serveix el mode *Live*?
3. En particionat manual amb UEFI, quines particions mínimes cal crear i amb quin sistema d'arxius?
4. Com s'obtenen privilegis d'administrador a Ubuntu si no hi ha contrasenya de root?
5. Quines ordres apliques just després d'instal·lar per actualitzar el sistema i posar els controladors?

---

[⬅ Anterior: Instal·lació de Windows](05-instal-lacio-de-windows.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Llicències i actualització ➡](07-llicencies-actualitzacio-i-incidencies.md)
