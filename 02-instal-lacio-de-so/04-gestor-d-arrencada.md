[🏠 Inici](../README.md) › [RA2 · Instal·lació de sistemes operatius](00-index.md) › **4. El gestor d'arrencada**

[⬅ Anterior: Pla d'instal·lació](03-pla-i-fases-d-instal-lacio.md) · [Següent: Instal·lació de Windows ➡](05-instal-lacio-de-windows.md)

# 4. El gestor d'arrencada

> Criteri d'avaluació RA2.7 — *Configura un gestor d'arrencada.*

## 4.1. Què és i on encaixa

El **gestor d'arrencada (*boot loader / boot manager*)** és el programa que s'executa just després del
microprogramari i que **carrega el nucli del sistema operatiu** a la memòria. Si hi ha més d'un SO instal·lat,
mostra un **menú** perquè l'usuari en triï un (arrencada múltiple o **dual boot**).

### Cadena d'arrencada

**Amb BIOS (MBR):**
```
Encesa → POST de la BIOS → llegeix el codi del MBR del disc
      → el MBR busca la partició ACTIVA → carrega el seu sector d'arrencada (VBR)
      → s'executa el gestor d'arrencada → carrega el nucli del SO
```

**Amb UEFI (GPT):**
```
Encesa → inicialització UEFI → llegeix la NVRAM (entrades d'arrencada)
      → munta la partició ESP (FAT32) → executa el fitxer .efi del gestor triat
        (\EFI\Microsoft\Boot\bootmgfw.efi, \EFI\ubuntu\grubx64.efi, …)
      → carrega el nucli del SO
```

## 4.2. Gestors d'arrencada habituals

| Gestor | SO | Configuració |
|---|---|---|
| **Windows Boot Manager** (`bootmgr`) + BCD | Windows Vista i posteriors | Magatzem **BCD** (*Boot Configuration Data*); s'edita amb `bcdedit` o l'eina gràfica `msconfig` → pestanya *Arrencada* |
| **NTLDR** + `boot.ini` | Windows XP i anteriors | Fitxer de text `boot.ini` (**llegat**) |
| **GRUB 2** (*GRand Unified Bootloader*) | GNU/Linux (i pot arrencar Windows) | `/etc/default/grub` + scripts a `/etc/grub.d/`; s'aplica amb `sudo update-grub` (Debian/Ubuntu) o `grub2-mkconfig -o /boot/grub2/grub.cfg` (Fedora/RHEL) |
| **systemd-boot** | Linux amb UEFI (alternativa lleugera a GRUB) | Entrades de text a `/boot/loader/` |
| **rEFInd** | Multiplataforma (UEFI) | Menú gràfic que detecta SO automàticament |
| **LILO** | Linux antic | **Llegat**, substituït per GRUB |

## 4.3. Arrencada dual: ordre d'instal·lació recomanat

1. **Primer Windows**, després Linux. L'instal·lador de Linux instal·la **GRUB**, que detecta el Windows amb
   `os-prober` i l'afegeix al menú.
2. Si s'instal·la a l'inrevés, Windows sobreescriu el gestor i «amaga» Linux → cal **reparar GRUB** des d'un
   *live USB*:
   ```bash
   sudo mount /dev/sdaX /mnt          # partició arrel de Linux
   sudo mount /dev/sdaY /mnt/boot/efi # ESP (UEFI)
   for d in dev proc sys run; do sudo mount --bind /$d /mnt/$d; done
   sudo chroot /mnt
   grub-install /dev/sda             # (BIOS)  o  grub-install --target=x86_64-efi
   update-grub
   exit
   ```
   Alternativa senzilla: eina **Boot-Repair**.

## 4.4. Operacions habituals

### Windows

| Tasca | Ordre |
|---|---|
| Veure les entrades d'arrencada | `bcdedit /enum` |
| Canviar el SO per defecte | `bcdedit /default {identificador}` |
| Canviar el temps d'espera del menú | `bcdedit /timeout 10` |
| Reparar l'arrencada (WinRE) | `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /rebuildbcd` |
| Reconstruir la BCD a UEFI | `bcdboot C:\Windows /s S: /f UEFI` |
| Menú gràfic | `msconfig` → *Arrencada* |

### Linux (GRUB 2)

| Tasca | On |
|---|---|
| SO/entrada per defecte | `GRUB_DEFAULT=` a `/etc/default/grub` (número o `saved`) |
| Temps d'espera del menú | `GRUB_TIMEOUT=` |
| Mostrar sempre el menú | `GRUB_TIMEOUT_STYLE=menu` |
| Detectar altres SO | instal·lar `os-prober` i posar `GRUB_DISABLE_OS_PROBER=false` |
| Aplicar canvis | `sudo update-grub` |
| Reinstal·lar GRUB | `sudo grub-install /dev/sdX` |

### BIOS/UEFI

- **Ordre d'arrencada:** disc del sistema primer per a l'ús normal; suport d'instal·lació primer temporalment.
- **Menú d'arrencada puntual:** `F12`, `F9`, `F8` o `Esc` en engegar (segons fabricant).
- A UEFI, l'ordre de gestors es guarda a la **NVRAM** i es pot editar amb `efibootmgr` (Linux).

## 4.5. Particions i codi d'arrencada relacionats

- **MBR:** primer sector del disc; conté el codi de primera etapa i la taula de 4 particions. La **partició
  activa** és la que es llegeix.
- **ESP (EFI System Partition):** partició FAT32 on UEFI busca els fitxers `.efi` dels gestors.
- **Partició `/boot`** (Linux): conté el nucli (`vmlinuz`), l'`initramfs` i la configuració de GRUB; útil
  tenir-la separada si l'arrel usa xifratge o LVM.
- Windows crea una petita partició **«Reservat per al sistema»** (MBR) o **ESP + MSR** (GPT) per als fitxers d'arrencada.

## 4.6. Resum

- El gestor d'arrencada carrega el nucli del SO i, en arrencada múltiple, mostra un menú.
- **BIOS/MBR:** codi al MBR → partició activa → gestor. **UEFI/GPT:** fitxers `.efi` a l'**ESP** + NVRAM.
- Windows usa **Windows Boot Manager + BCD** (`bcdedit`); Linux, **GRUB 2** (`/etc/default/grub` + `update-grub`).
- En dual boot, instal·la **Windows primer** i Linux després; si cal, repara GRUB des d'un *live USB*.

## Comprova què has après

1. Ordena la cadena d'arrencada amb BIOS i amb UEFI.
2. Quin fitxer/magatzem configura l'arrencada a Windows Vista+? I a Linux?
3. Per què s'instal·la Windows abans que Linux en un equip amb dual boot?
4. Quina ordre reconstrueix el menú de GRUB després de canviar `/etc/default/grub`?
5. Què és l'ESP i quin format té?

---

[⬅ Anterior: Pla d'instal·lació](03-pla-i-fases-d-instal-lacio.md) · [Següent: Instal·lació de Windows ➡](05-instal-lacio-de-windows.md)
