[🏠 Inici](../README.md) › [RA4 · Administració del sistema operatiu](00-index.md) › **1. Usuaris, grups i contrasenyes**

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Permisos i recursos compartits ➡](02-permisos-i-recursos-compartits.md)

# 1. Usuaris, grups i contrasenyes

> Criteri d'avaluació RA4.1 — *Configura perfils d'usuari i grup.*

## 1.1. Comptes d'usuari locals

Un **compte d'usuari local** és la configuració que permet a una persona iniciar sessió en un equip concret
(no en equips remots; això és cosa del mòdul de SO en xarxa). Cada compte té:

- **Nom d'inici de sessió (login):** identificador únic; a Windows, ≤ 20 caràcters; no s'hi recomana accents ni
  símbols. **No es pot canviar** després (canviar-lo equival a crear un compte nou).
- **Nom complet / descripció:** només informatiu.
- **Contrasenya** i opcions de gestió.
- **Perfil:** carpeta personal amb la configuració (escriptori, preferències, dades).
- **Pertinença a grups** i **permisos** derivats.
- **Identificador intern:** **SID** a Windows, **UID** a Linux.

## 1.2. Comptes predefinits

### Windows
| Compte | Descripció |
|---|---|
| **Administrador** | Control total. Es crea automàticament; **no es pot esborrar**; a Windows 10/11 està **deshabilitat** per defecte (s'usa el compte creat a la instal·lació, que és del grup Administradors). |
| **Convidat (*Guest*)** | Accés molt limitat; no pot instal·lar res ni canviar la configuració. Deshabilitat per defecte. |
| **Compte inicial** | El que es crea a l'OOBE; membre del grup **Administradors**. |
| Comptes de sistema | `SYSTEM`, `LOCAL SERVICE`, `NETWORK SERVICE` (per als serveis, no per iniciar sessió). |

### Linux
| Compte | Descripció |
|---|---|
| **root** (UID 0) | Superusuari; pot fer-ho tot. A **Ubuntu** està **bloquejat** (sense contrasenya): s'administra amb **`sudo`**. |
| Usuaris de sistema (UID 1–999) | `daemon`, `www-data`, `systemd-*`… per a serveis; no inicien sessió interactiva. |
| Usuaris normals (UID ≥ 1000) | Persones. El primer creat a la instal·lació pertany al grup `sudo` (Debian/Ubuntu) o `wheel` (Fedora). |

## 1.3. Tipus de compte (perfil de privilegis)

- **Estàndard:** ús normal de l'equip; no pot instal·lar programari per a tots els usuaris ni canviar la
  configuració global.
- **Administrador:** pot administrar l'equip (usuaris, drivers, serveis, programari). Windows demana
  confirmació via **UAC** (*User Account Control*); Linux, via `sudo`/`polkit`.

> Bona pràctica: fer servir un compte **estàndard** per a l'ús diari i elevar privilegis puntualment.

## 1.4. Perfils d'usuari

En iniciar sessió per primera vegada, el SO crea el perfil de l'usuari a partir d'una **plantilla**:

| | Windows | Linux |
|---|---|---|
| Carpeta del perfil | `C:\Users\<usuari>` | `/home/<usuari>` |
| Plantilla | `C:\Users\Default` | `/etc/skel` |
| Dades comunes | `C:\Users\Public`, `C:\ProgramData` | `/srv`, `/opt`, `/usr/share` |
| Fitxer de configuració de la sessió | `NTUSER.DAT` (branca `HKEY_CURRENT_USER` del Registre) | fitxers `~/.config`, `~/.bashrc`, etc. |

- **Perfil local:** es guarda a l'equip.
- **Perfil mòbil (*roaming*):** es guarda en un servidor i segueix l'usuari per la xarxa (mòdul de SO en xarxa).
- En **esborrar un compte**, el perfil (carpeta) **no s'elimina automàticament**: cal fer-ho a part.

## 1.5. Gestió a Windows

### GUI
- *Configuració → Comptes → Altres usuaris* (bàsic).
- **`lusrmgr.msc`** — *Usuaris i grups locals* (edicions Pro/Enterprise): alta, baixa, modificació, contrasenya,
  pestanya *Membre de* per assignar grups, pestanya *Perfil*.
- `netplwiz` (`control userpasswords2`) — configurar si es demana usuari/contrasenya en iniciar.

### CLI
```
net user anna P@ssw0rd! /add /fullname:"Anna Roca" /comment:"Aula 1"
net user anna /active:no                 :: deshabilitar
net user anna *                          :: canviar contrasenya (interactiu)
net user anna /expires:never
net localgroup Administradores anna /add :: afegir a un grup
net user anna /delete
```
PowerShell: `New-LocalUser`, `Set-LocalUser`, `Add-LocalGroupMember`, `Remove-LocalUser`.

## 1.6. Gestió a Linux

### Fitxers clau
| Fitxer | Contingut |
|---|---|
| `/etc/passwd` | Un usuari per línia: `login:x:UID:GID:nom complet:/home/login:/bin/bash` |
| `/etc/shadow` | Contrasenyes xifrades (hash) i política de caducitat; només llegible per root |
| `/etc/group` | Grups i els seus membres |
| `/etc/gshadow` | Contrasenyes de grup |
| `/etc/skel/` | Plantilla per a `/home` dels usuaris nous |

### Ordres
```bash
sudo adduser anna                 # (Debian/Ubuntu) interactiu: crea /home, grup propi, demana dades
sudo useradd -m -s /bin/bash anna # (genèric) -m crea /home, -s fixa la shell
sudo passwd anna                  # assignar/canviar contrasenya
sudo usermod -aG sudo,cdrom anna  # afegir a grups (-a = afegir, no substituir)
sudo usermod -L anna / -U anna    # bloquejar / desbloquejar
sudo chage -l anna               # veure caducitat de la contrasenya
sudo chage -M 90 -W 7 anna       # caduca als 90 dies, avís 7 dies abans
sudo deluser --remove-home anna  # esborrar usuari i el seu /home
id anna                          # UID, GID i grups
```

## 1.7. Grups

Un **grup** agrupa usuaris per assignar-los permisos de manera col·lectiva; els permisos concedits al grup els
**hereten** tots els seus membres.

- Tot usuari pertany a **un grup principal** i pot pertànyer a **grups secundaris**.
- A Linux, `adduser` crea un **grup propi** amb el mateix nom (esquema UPG). Grups habituals: `sudo`, `adm`,
  `cdrom`, `plugdev`, `docker`, `www-data`.
- A Windows, grups locals per defecte: **Administradors**, **Usuaris**, **Convidats**, **Operadors de còpia**
  (*Backup Operators*), **Usuaris d'escriptori remot**, **Operadors de configuració de xarxa**, etc.

```bash
sudo groupadd projecte
sudo usermod -aG projecte anna
sudo gpasswd -d anna projecte     # treure del grup
sudo groupdel projecte            # esborrar el grup (els usuaris no s'esborren)
```
Windows: `net localgroup projecte /add`, `net localgroup projecte anna /add`.

> **Esborrar un grup** no esborra els seus usuaris, però sí que fa desaparèixer els permisos que tenien
> **per pertànyer-hi**.

## 1.8. Contrasenyes: política de seguretat

Recomanacions (i requisits de complexitat típics):

- Longitud mínima raonable (≥ 12 caràcters o una frase de contrasenya).
- Barreja de majúscules, minúscules, dígits i símbols (o longitud alta).
- No contenir el nom d'usuari ni el nom real.
- Caducitat i historial (evitar reutilitzar les últimes N).
- No compartir-la; usar un **gestor de contrasenyes**; activar **2FA/MFA** quan sigui possible.

| Configuració | Windows | Linux |
|---|---|---|
| Política local | `secpol.msc` → *Directives de comptes → Directiva de contrasenyes* (longitud, complexitat, historial, vigència màx./mín.) | `/etc/login.defs` (PASS_MAX_DAYS…) i mòdul PAM `pwquality` (`/etc/security/pwquality.conf`) |
| Forçar canvi en el següent inici | Opció a `lusrmgr.msc` / `net user anna /logonpasswordchg:yes` | `sudo chage -d 0 anna` |
| Bloqueig per intents fallits | *Directiva de bloqueig de comptes* | `faillock` (PAM) |

> L'administrador pot **posar, treure o reiniciar** la contrasenya d'un usuari, però **no pot llegir-la**
> (es guarda com a *hash*). Si un usuari l'oblida, l'administrador n'assigna una de nova.

## 1.9. Resum

- Compte local = login (fix) + contrasenya + perfil + grups. ID intern: **SID** (Windows), **UID** (Linux).
- Comptes especials: **Administrador**/root (deshabilitats per defecte a Win10/11 i Ubuntu; s'usa UAC/`sudo`).
- Perfil des d'una **plantilla** (`Default` / `/etc/skel`); esborrar el compte **no** esborra la carpeta.
- Windows: `lusrmgr.msc`, `net user`, `net localgroup`, PowerShell `*-LocalUser`.
- Linux: `/etc/passwd`, `/etc/shadow`, `/etc/group`; `adduser`, `usermod -aG`, `passwd`, `chage`, `groupadd`.
- **Grup** = permisos col·lectius heretats pels membres.

## Comprova què has après

1. Per què no es pot canviar el login d'un usuari sense «crear-ne un de nou»?
2. Diferència entre compte estàndard i administrador. Què és UAC?
3. Quins tres fitxers de Linux emmagatzemen usuaris, contrasenyes i grups?
4. Amb quina ordre afegeixes l'usuari `anna` al grup `sudo` sense treure'l dels altres grups?
5. Si esborres un grup, què passa amb els usuaris que hi pertanyien?
6. Pot l'administrador saber la contrasenya d'un usuari? Què pot fer si l'usuari l'oblida?

---

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Permisos i recursos compartits ➡](02-permisos-i-recursos-compartits.md)
