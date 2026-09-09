[⬅ Anterior: Usuaris i grups](01-usuaris-grups-i-contrasenyes.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Gestió de processos ➡](03-gestio-de-processos.md)

# 2. Permisos i recursos compartits

> Criteris d'avaluació RA4.2 i RA4.8 — *Eines gràfiques per descriure l'organització dels arxius; reconeix i
> configura els recursos compartibles del sistema.*
> Base teòrica: [RA1 · atributs i permisos](../01-caracteritzacio-dels-so/08-arxius-directoris-atributs-i-permisos.md).

## 2.1. Permís vs. dret

- **Permís:** acció que es pot fer **sobre un recurs concret** (llegir un fitxer, escriure en una carpeta,
  imprimir en una impressora).
- **Dret d'usuari (*privilege*):** acció que es pot fer **sobre el sistema** (apagar l'equip, canviar l'hora,
  fer còpies de seguretat, iniciar sessió com a servei). A Windows es defineixen a `secpol.msc` → *Assignació
  de drets d'usuari*; a Linux, amb la pertinença a grups i les regles de `sudo`/`polkit`.

## 2.2. Permisos NTFS a Windows (ACL)

Cada fitxer o carpeta NTFS té una **llista de control d'accés (ACL)**: entrades (**ACE**) que diuen, per a cada
usuari o grup, què pot fer.

### Permisos bàsics

| Permís | Sobre carpeta | Sobre fitxer |
|---|---|---|
| **Control total** | Tot, inclòs canviar permisos i propietari | Tot |
| **Modificar** | Crear, esborrar, canviar contingut i subelements | Modificar i esborrar |
| **Llegir i executar** | Llistar i entrar; executar programes | Llegir i executar |
| **Mostrar contingut de la carpeta** | Només llistar | — |
| **Llegir** | Veure contingut, atributs i permisos | Veure contingut |
| **Escriure** | Afegir fitxers/carpetes | Modificar contingut i atributs |

- **Herència:** per defecte, els subelements hereten els permisos de la carpeta pare. Es pot **trencar
  l'herència** en un element concret.
- **Denegar** té prioritat sobre **Permetre**.
- **Propietari:** qui crea l'element; pot canviar-ne els permisos. Un administrador pot **prendre'n possessió**.

### Eines

- GUI: clic dret → *Propietats → Seguretat* (i *Avançat* per a herència, propietari, permisos efectius).
- CLI: **`icacls`**
  ```
  icacls C:\Dades                                   :: veure permisos
  icacls C:\Dades /grant anna:(OI)(CI)M             :: Modificar, amb herència
  icacls C:\Dades /remove:g "Usuaris"
  icacls C:\Dades /inheritance:r                    :: treure l'herència
  icacls C:\Dades /setowner Administradores /T
  ```
- PowerShell: `Get-Acl`, `Set-Acl`.

## 2.3. Permisos a Linux (`rwx`) — repàs pràctic

```
ls -l                 # veure permisos, propietari i grup
chmod 750 projecte/    # rwx propietari, r-x grup, res altres
chmod -R g+w equip/     # afegir escriptura al grup, recursiu
chown -R anna:projecte /srv/projecte
umask 027              # els fitxers nous neixen 640 i els directoris 750
```

Per a permisos fins (usuaris/grups concrets més enllà de propietari/grup/altres): **ACL POSIX**

```bash
sudo apt install acl
setfacl -m u:pere:rwx informe.txt      # dona rwx a l'usuari pere
setfacl -m g:alumnes:r-- informe.txt
setfacl -d -m g:alumnes:rwx projecte/  # ACL per defecte (herència)
getfacl informe.txt
setfacl -b informe.txt                 # esborrar totes les ACL
```
Un `+` al final de `ls -l` (`-rw-rwxr--+`) indica que l'element té ACL.

## 2.4. Compartició de recursos en xarxa

> És la porta d'entrada al mòdul 0224 (SO en xarxa), però el currículum de 0222 demana **reconèixer i
> configurar els recursos compartibles del sistema**.

### Windows — recursos compartits SMB

- **Compartir una carpeta:** clic dret → *Propietats → Ús compartit* → *Ús compartit avançat* → *Comparteix
  aquesta carpeta* → botó *Permisos* (permisos **de recurs compartit**: Llegir / Canviar / Control total).
- **Dos nivells de permís actuen alhora:** els **de recurs compartit** i els **NTFS**. El resultat efectiu és
  el **més restrictiu** dels dos.
- Compartició protegida amb contrasenya: *Configuració → Xarxa → Configuració d'ús compartit avançat*.
- Recursos compartits **administratius ocults**: `C$`, `ADMIN$`, `IPC$` (acaben en `$`).
- CLI:
  ```
  net share Dades=C:\Dades /grant:anna,change
  net share                         :: llistar
  net share Dades /delete
  net use Z: \\PC07\Dades /persistent:yes   :: connectar una unitat de xarxa (client)
  ```
- Impressores: *Propietats de la impressora → Ús compartit*.

### Linux

- **Samba** (compatible amb xarxes Windows/SMB): paquet `samba`; configuració a `/etc/samba/smb.conf`:
  ```ini
  [dades]
     path = /srv/dades
     read only = no
     valid users = @alumnes
     create mask = 0664
  ```
  `sudo smbpasswd -a anna`; `sudo systemctl restart smbd`. GUI ràpida: opció *Compartició en xarxa* del gestor
  de fitxers (paquet `nautilus-share`).
- **NFS** (per a xarxes UNIX/Linux): paquet `nfs-kernel-server`; exports a `/etc/exports`:
  ```
  /srv/dades  192.168.1.0/24(rw,sync,no_subtree_check)
  ```
  `sudo exportfs -ra`. Client: `sudo mount -t nfs servidor:/srv/dades /mnt/dades`.
- **Accedir a un recurs compartit Windows des de Linux:** al gestor de fitxers, `smb://PC07/Dades`, o
  `sudo mount -t cifs //PC07/Dades /mnt/win -o username=anna`.
- **Impressió:** CUPS (`http://localhost:631`) permet compartir impressores per la xarxa.

### Nivells de seguretat en compartir

- Compartir **només amb els usuaris/grups necessaris** i amb el permís mínim (sovint *Llegir*).
- Combinar permisos de recurs compartit + del sistema d'arxius.
- No exposar recursos a *Tothom* / `guest ok = yes` sense necessitat.
- En xarxes obertes, xifrar (SMB 3, `vers=3`; NFSv4 amb Kerberos).

## 2.5. Eines gràfiques per veure l'organització dels arxius

- Windows: **Explorador de fitxers** (vista d'arbre, columnes de mida/data/tipus), *Propietats* d'unitat
  (espai usat/lliure), **WizTree** / **TreeSize** (mapa d'ús d'espai).
- Linux: **Fitxers (Nautilus)** amb barra lateral d'arbre, **Analitzador d'ús de disc (`baobab`)**, `ncdu`,
  `tree`, `du -sh */ | sort -h`.

## 2.6. Resum

- **Permís** = sobre un recurs; **dret** = sobre el sistema.
- Windows: **ACL NTFS** (Control total / Modificar / Llegir i executar…), herència, *Denegar* mana; eines
  *Seguretat* i **`icacls`**.
- Linux: **`rwx`** + `chmod`/`chown`/`umask` i **ACL POSIX** (`setfacl`/`getfacl`).
- Compartició: **SMB** (Windows i Samba) amb permisos de recurs compartit + del sistema d'arxius (guanya el
  més restrictiu); **NFS** per a Linux. Compartir amb el privilegi mínim.

## Comprova què has après

1. Diferència entre un permís i un dret d'usuari, amb un exemple de cada.
2. En NTFS, si un usuari té *Modificar* per un grup i *Denegar escriptura* per un altre, què pot fer?
3. Quan comparteixes una carpeta a Windows, quins dos conjunts de permisos s'apliquen i quin preval?
4. Quina ordre de Linux dona permís de lectura a l'usuari `pere` sobre un fitxer sense canviar-ne el grup?
5. Quin servei fas servir a Linux per compartir carpetes amb equips Windows?

---

[⬅ Anterior: Usuaris i grups](01-usuaris-grups-i-contrasenyes.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Gestió de processos ➡](03-gestio-de-processos.md)
