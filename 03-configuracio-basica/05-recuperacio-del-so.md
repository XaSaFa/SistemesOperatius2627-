[⬅ Anterior: Programari i automatització](04-programari-actualitzacions-i-automatitzacio.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Instal·lació ➡](../02-instal-lacio-de-so/00-index.md)

# 5. Recuperació del sistema operatiu

> Criteri d'avaluació RA3.4 — *Aplica mètodes per a la recuperació del sistema operatiu.*

## 5.1. Estratègia: prevenir i recuperar

| Nivell | Objectiu | Eines |
|---|---|---|
| **Prevenció** | Poder tornar enrere | Punts de restauració, instantànies, imatges del sistema, còpies de seguretat, suports de recuperació |
| **Recuperació parcial** | Arreglar el SO conservant dades i aplicacions | Mode segur, reparació d'inici, `sfc`/`DISM`, `fsck`, restaurar drivers/actualitzacions |
| **Recuperació total** | Tornar a un estat conegut | Restaurar imatge / instantània, *Restablir aquest PC*, reinstal·lació neta |

Regla d'or de còpies: **3-2-1** — 3 còpies de les dades, en 2 suports diferents, 1 fora de l'equip.

## 5.2. Windows

### Punts de restauració del sistema

- Fan una còpia de fitxers de sistema, registre i drivers (no dels documents).
- Activar: *Crea un punt de restauració* → *Configura* → activar protecció i reservar espai.
- Es creen automàticament abans d'instal·lar drivers/actualitzacions i es poden crear manualment.
- Restaurar: *Restauració del sistema* (`rstrui`) o des de WinRE.

### Windows RE (entorn de recuperació)

S'hi entra amb `Maj` + *Reinicia*, 3 arrencades fallides seguides, o des d'un USB d'instal·lació →
*Repara l'equip*. Opcions:

- **Reparació d'inici:** repara automàticament el gestor d'arrencada i fitxers d'arrencada.
- **Desinstal·la actualitzacions** (de qualitat o de característiques).
- **Restauració del sistema** (punt de restauració).
- **Recuperació d'imatge del sistema** (si n'hi ha una).
- **Símbol del sistema:** `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /rebuildbcd`, `chkdsk`, `sfc`,
  `DISM`, `bcdedit`.

### Mode segur

Arrenca amb els controladors i serveis mínims (opcionalment amb xarxa o amb símbol del sistema). Útil per
desinstal·lar un driver o programa que impedeix arrencar. S'hi accedeix des de WinRE → *Configuració d'inici*
o amb `msconfig` → *Arrencada* → *Arrencada segura*.

### Reparació d'integritat

```
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
chkdsk C: /F /R
```

### Restablir / imatge

- **Restableix aquest PC:** *Configuració → Sistema → Recuperació* → conservar fitxers o eliminar-ho tot;
  reinstal·la Windows des del núvol o localment.
- **Imatge del sistema (llegat):** *Còpia de seguretat i restauració (Windows 7)* → *Crea una imatge del
  sistema* (fitxer VHD). Restauració des de WinRE.
- **Historial de fitxers:** còpia contínua de biblioteques/escriptori a un disc extern.
- Suport de recuperació: *Crea una unitat de recuperació* (USB).

## 5.3. Linux

### Mode de recuperació (GRUB)

Menú GRUB → *Advanced options* → *(recovery mode)*: arrenca en monousuari amb un menú (`root` shell,
`fsck`, `dpkg` per reparar paquets, actualitzar GRUB, xarxa, netejar temporals).

### Reparar des d'un *live USB* amb `chroot`

```bash
sudo mount /dev/sda2 /mnt              # partició arrel
sudo mount /dev/sda1 /mnt/boot/efi     # ESP (UEFI)
for d in dev proc sys run; do sudo mount --bind /$d /mnt/$d; done
sudo chroot /mnt
# dins del chroot: reparar paquets, GRUB, contrasenyes, fstab…
apt --fix-broken install
update-grub
exit
```

Alternativa gràfica per a l'arrencada: **Boot-Repair**.

### Comprovar el sistema d'arxius

`sudo fsck /dev/sdaX` amb el volum **desmuntat** (per l'arrel, des del live USB o forçant-ho a l'arrencada
amb `fsck.mode=force` a la línia del nucli).

### Nucli que no arrenca

Al menú GRUB, triar una **entrada de nucli anterior** (*Advanced options*). Després, eliminar el nucli
defectuós o reinstal·lar-lo.

### Instantànies i còpies

- **Timeshift:** instantànies del sistema (rsync o Btrfs); restaurables des del live USB. Molt recomanat abans
  d'actualitzacions grosses.
- **Btrfs/ZFS snapshots:** instantànies gairebé instantànies del subvolum arrel; algunes distribucions les
  integren amb el gestor de paquets (openSUSE + Snapper).
- **Déjà Dup / `borg` / `restic` / `rsync`:** còpia de les dades d'usuari (`/home`).
- **Clonezilla:** imatge completa del disc.

### Recuperar la contrasenya de root / d'un usuari

Des del mode de recuperació o afegint `init=/bin/bash` (o `rw single`) a la línia del nucli a GRUB, remuntar
l'arrel en lectura-escriptura (`mount -o remount,rw /`) i executar `passwd usuari`.

## 5.4. Bones pràctiques

- Activar punts de restauració / instantànies **abans** de tocar drivers, actualitzacions o particions.
- Tenir sempre un **USB d'instal·lació/recuperació** a mà.
- Provar periòdicament que les **còpies de seguretat es poden restaurar** (una còpia no verificada no és una còpia).
- Documentar l'esquema de particions i el procediment de recuperació a la fitxa de l'equip.

## 5.5. Resum

- Prevenir (punts de restauració, instantànies, imatges, còpies 3-2-1) i recuperar (mode segur, WinRE,
  `sfc`/`DISM`/`fsck`, restablir/imatge).
- Windows: **WinRE** (reparació d'inici, restauració, `bootrec`), **mode segur**, **Restableix aquest PC**.
- Linux: **mode de recuperació** de GRUB, **`chroot`** des d'un live USB, **Timeshift**/instantànies, triar un
  nucli anterior.

## Comprova què has après

1. Què desa un punt de restauració de Windows i què **no** desa?
2. Com entres a WinRE si Windows ni tan sols arrenca?
3. Per a què serveix el mode segur?
4. Explica per sobre com repararies GRUB des d'un live USB.
5. Què significa la regla de còpies 3-2-1?

---

[⬅ Anterior: Programari i automatització](04-programari-actualitzacions-i-automatitzacio.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Instal·lació ➡](../02-instal-lacio-de-so/00-index.md)
