[🏠 Inici](../README.md) › [RA3 · Configuració bàsica del sistema operatiu](00-index.md) › **1. Arrencada, parada i sessions**

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Interfícies i preferències ➡](02-interficies-d-usuari-i-preferencies.md)

# 1. Arrencada, parada i sessions

> Criteri d'avaluació RA3.1 — *tasques bàsiques de configuració; arrencada i parada del sistema; sessions.*

## 1.1. Seqüència d'arrencada (repàs i detall)

1. **Encesa i POST** del microprogramari (BIOS/UEFI): comprova RAM, CPU i dispositius bàsics.
2. El firmware llegeix el **gestor d'arrencada** (MBR → partició activa, o ESP en UEFI). Vegeu
   [RA2 · gestor d'arrencada](../02-instal-lacio-de-so/04-gestor-d-arrencada.md).
3. El gestor carrega el **nucli** del SO a la memòria.
4. El nucli inicialitza controladors i munta el sistema d'arxius arrel.
5. S'inicia el **primer procés d'espai d'usuari**:
   - **Windows:** `smss.exe` → `wininit.exe`/`csrss.exe` → `services.exe` (Gestor de control de serveis) →
     `winlogon.exe` → pantalla d'inici de sessió.
   - **Linux:** **`systemd`** (PID 1) — abans **`init` SysV** (llegat). `systemd` arriba a un **objectiu
     (*target*)**: `graphical.target` (amb GUI) o `multi-user.target` (només text).
6. Es mostra la **pantalla d'inici de sessió** (*login*).

### Objectius de systemd vs. nivells d'execució (*runlevels*) SysV

| systemd target | Runlevel SysV | Descripció |
|---|---|---|
| `poweroff.target` | 0 | Apagat |
| `rescue.target` | 1 / S | Monousuari, manteniment |
| `multi-user.target` | 3 | Multiusuari sense GUI (servidors) |
| `graphical.target` | 5 | Multiusuari amb entorn gràfic |
| `reboot.target` | 6 | Reinici |

```bash
systemctl get-default                     # objectiu per defecte
sudo systemctl set-default multi-user.target
sudo systemctl isolate rescue.target      # canviar ara mateix
```

## 1.2. Sessions d'usuari

Una **sessió** és el període entre l'inici i el tancament de sessió d'un usuari; el SO li carrega el seu
**perfil** (escriptori, preferències, variables d'entorn) i els seus permisos.

Operacions de sessió:

| Acció | Windows | Linux (GNOME) |
|---|---|---|
| **Iniciar sessió** | Triar usuari + contrasenya/PIN/biometria | Triar usuari + contrasenya |
| **Bloquejar la pantalla** | `Win+L` | `Super+L` o `Ctrl+Alt+L` |
| **Tancar sessió** (*log off*) | Menú Inici → usuari → *Tanca la sessió* | Menú del sistema → *Tanca la sessió* |
| **Canviar d'usuari** (deixant l'altra sessió oberta) | *Canvia d'usuari* | *Canvia d'usuari* |
| **Suspèn** (RAM alimentada, reanudació ràpida) | Menú d'apagada → *Suspèn* | *Suspèn* |
| **Hiberna** (estat desat a disc, consum zero) | Cal activar-ho (`powercfg /h on`) | `systemctl hibernate` (necessita swap ≈ RAM) |

> **Diferència clau:** *bloquejar* manté la sessió i les aplicacions obertes darrere d'una contrasenya;
> *tancar sessió* tanca les aplicacions de l'usuari i torna a la pantalla d'inici.

## 1.3. Aturada i reinici ordenats

Aturar «malament» (treure el corrent) pot **corrompre el sistema d'arxius** i perdre dades no desades. Sempre
cal fer-ho amb l'ordre del sistema, que atura serveis i processos, buida les memòries intermèdies a disc
(*flush*) i desmunta els volums.

### Windows

| Acció | GUI | CLI |
|---|---|---|
| Apagar | Inici → Apagar | `shutdown /s /t 0` |
| Reiniciar | Inici → Reinicia | `shutdown /r /t 0` |
| Apagar d'aquí a 60 s | — | `shutdown /s /t 60` |
| Cancel·lar apagada programada | — | `shutdown /a` |
| Reinici a opcions avançades | Maj + *Reinicia* | `shutdown /r /o /t 0` |
| Tancar sessió | — | `shutdown /l` o `logoff` |

> **Inici ràpid (*Fast Startup*)** de Windows: en «apagar» desa l'estat del nucli en un fitxer (hibernació
> parcial). Pot causar problemes en dual boot i muntatge de particions NTFS des de Linux → es pot desactivar a
> *Opcions d'energia → Comportament dels botons d'inici/apagada*.

### Linux

| Acció | Ordre |
|---|---|
| Apagar ara | `systemctl poweroff` (o `poweroff`, `shutdown -h now`, `halt -p`) |
| Reiniciar ara | `systemctl reboot` (o `reboot`, `shutdown -r now`) |
| Apagar d'aquí a 10 min amb avís | `sudo shutdown -h +10 "Manteniment"` |
| Cancel·lar | `sudo shutdown -c` |
| Suspendre / hibernar | `systemctl suspend` / `systemctl hibernate` |

## 1.4. Problemes d'arrencada i inicis alternatius

| Situació | Windows | Linux |
|---|---|---|
| Arrencada en mode diagnòstic | **Mode segur** (`Maj`+Reinicia → Solucionar → Opcions avançades → Configuració d'inici → F4/F5/F6) o `msconfig` → *Arrencada* → *Arrencada segura* | Menú GRUB → *Advanced options* → *(recovery mode)* o afegir `systemd.unit=rescue.target` / `single` a la línia del nucli |
| Consola de recuperació | *Reparació d'inici*, `bootrec`, restauració del sistema (WinRE) | `rescue.target`, *chroot* des d'un live USB, `fsck` |
| Últim reinici bo | *Configuració d'inici* | Triar un **nucli anterior** al menú GRUB |

## 1.5. Resum

- Arrencada: POST → gestor d'arrencada → nucli → primer procés (`smss`/`services` a Windows; **`systemd`** PID 1
  a Linux) → login.
- systemd usa **objectius** (`graphical.target`, `multi-user.target`, `rescue.target`) equivalents als
  **runlevels** clàssics.
- Una **sessió** carrega el perfil i els permisos d'un usuari. *Bloquejar* ≠ *tancar sessió*.
- Aturar **sempre** amb `shutdown`/`systemctl poweroff` per no corrompre dades; desactivar l'*inici ràpid* en dual boot.

## Comprova què has après

1. Quin és el primer procés d'espai d'usuari a Linux i quin PID té?
2. Relaciona `graphical.target` i `multi-user.target` amb els runlevels 5 i 3.
3. Diferència entre bloquejar la pantalla i tancar la sessió.
4. Quina ordre de Windows programa un apagat d'aquí a 5 minuts i quina el cancel·la?
5. Per què pot ser problemàtic l'*inici ràpid* de Windows en un equip amb dual boot?

---

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Interfícies i preferències ➡](02-interficies-d-usuari-i-preferencies.md)
