[⬅ Anterior: Serveis del sistema](04-serveis-del-sistema.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Màquines virtuals ➡](../05-maquines-virtuals/00-index.md)

# 5. Monitoratge, rendiment i registres

> Criteris d'avaluació RA4.5–RA4.7 i RA4.9 — *optimització de la memòria; anàlisi de l'activitat a partir de
> les traces del sistema; optimització dels dispositius d'emmagatzematge; interpretació de la informació de
> configuració del SO.*

## 5.1. Què es monitora

| Recurs | Indicadors clau | Símptomes de problema |
|---|---|---|
| **CPU** | % d'ús, càrrega mitjana, cua de processos | 100 % sostingut, equip que no respon |
| **Memòria** | RAM usada/lliure, memòria en cau, ús de swap, fallades de pàgina | Molt swap → *thrashing*; procés amb RAM creixent → fuita |
| **Disc** | % d'activitat, IOPS, temps de resposta, espai lliure, SMART | Disc al 100 %, disc gairebé ple, sectors reassignats |
| **Xarxa** | Amplada de banda, connexions, errors | Saturació, latència |
| **Tèrmic/energia** | Temperatura, freqüència, *throttling* | Sobreescalfament → baixada de rendiment |

## 5.2. Windows — eines

| Eina | Ús |
|---|---|
| **Administrador de tasques** → *Rendiment* | Vista ràpida de CPU, memòria, disc, xarxa, GPU |
| **Monitor de recursos** (`resmon`) | Detall per procés de CPU, disc (fitxers en ús), xarxa i memòria |
| **Monitor de rendiment** (`perfmon`) | Comptadors i registres (**conjunts de recopiladors de dades**), informes |
| **Visor d'esdeveniments** (`eventvwr.msc`) | **Registres**: Aplicació, Seguretat, Sistema, Configuració, i registres d'aplicacions i serveis. Nivells: Informació, Advertència, Error, Crític |
| **Fiabilitat** (`perfmon /rel`) | Historial gràfic d'errors i estabilitat del sistema |
| **Experiència d'inici / temps d'arrencada** | Visor d'esdeveniments → *Microsoft/Windows/Diagnostics-Performance* |
| PowerShell | `Get-Counter '\Processor(_Total)\% Processor Time'`, `Get-WinEvent -LogName System -MaxEvents 50` |
| `wevtutil` | Consultar/exportar registres per línia d'ordres |

## 5.3. Linux — eines

```bash
top / htop / btop        # monitor interactiu de processos i recursos
uptime                   # càrrega mitjana (1, 5, 15 min); compara amb el nombre de nuclis
free -h                  # RAM i swap; "available" és el que realment queda
vmstat 1                 # processos, memòria, swap, E/S, CPU cada segon
iostat -xz 1             # E/S per disc (paquet sysstat); %util, await
mpstat -P ALL 1          # CPU per nucli (sysstat)
sar                      # històric de rendiment (sysstat)
pidstat 1                # consum per procés
iotop                    # E/S de disc per procés (root)
nload / iftop / nethogs  # xarxa (global / per connexió / per procés)
df -h                    # espai lliure per volum
du -sh */ | sort -h ; ncdu ; baobab   # què ocupa espai
lsof / fuser             # qui té oberts fitxers/dispositius
smartctl -a /dev/sda     # salut del disc (smartmontools)
```

### Registres a Linux

- **systemd-journald:** `journalctl`
  ```bash
  journalctl -b                 # missatges d'aquest arrencada
  journalctl -b -1              # arrencada anterior
  journalctl -p err             # només errors i pitjor
  journalctl -u ssh --since "today"
  journalctl -f                 # seguir en temps real (com tail -f)
  journalctl --disk-usage ; sudo journalctl --vacuum-time=7d
  ```
- **Fitxers de text a `/var/log/`:** `syslog`/`messages` (general), `auth.log`/`secure` (autenticació),
  `kern.log` (nucli), `dmesg` (missatges del nucli des de l'arrencada), `Xorg.0.log`, logs d'aplicacions
  (`/var/log/apache2/`, …).
- **Rotació:** `logrotate` comprimeix i esborra logs antics automàticament.

## 5.4. Optimització de la memòria

- Tancar aplicacions i pestanyes que no s'usen; revisar les **aplicacions d'inici**.
- Detectar **fuites de memòria**: procés amb RAM que només creix → reiniciar-lo o actualitzar-lo.
- Ajustar la **memòria virtual**:
  - Windows: mida del fitxer de paginació; si hi ha diversos discos, posar-lo en un SSD/disc ràpid diferent del del sistema.
  - Linux: mida de la partició/fitxer `swap`; `vm.swappiness` (per defecte 60; baixar-lo a 10–20 en equips amb prou RAM).
- **Afegir RAM** és la millora més efectiva quan hi ha ús constant de swap (*thrashing*).
- A Windows, la funció **Compressió de memòria** redueix la pressió abans de recórrer al disc (ho fa sol).

Vegeu [RA1 · gestió de la memòria](../01-caracteritzacio-dels-so/05-gestio-de-memoria.md).

## 5.5. Optimització dels dispositius d'emmagatzematge

- **HDD:** desfragmentar (`dfrgui` / `defrag`; a Linux ext4 no cal). Mantenir un 10–15 % lliure.
- **SSD:** **TRIM** (Windows *Optimitza* setmanal; Linux `fstrim.timer` o opció `discard`). **No desfragmentar.**
- Comprovar salut amb **SMART** (`smartctl`, o *Discs* a GNOME); vigilar *Reallocated Sectors* i *Pending Sectors*.
- **Neteja d'espai:** Sensor d'emmagatzematge / `cleanmgr` (Windows); `apt autoremove && apt clean`,
  `journalctl --vacuum-time`, buidar la paperera i `~/.cache` (Linux).
- Alinear particions correctament (les eines modernes ho fan) i triar la **mida de clúster** adequada.
- Separar dades del sistema en particions diferents ([RA2 · particions](../02-instal-lacio-de-so/02-particions-i-estructura-del-disc.md)).

## 5.6. Rendiment general (visió d'administrador)

- **Efectes visuals:** Windows → *Propietats del sistema → Rendiment → Ajusta per obtenir el millor rendiment*.
- **Prioritat serveis vs. aplicacions:** Windows → *Rendiment → Opcions avançades*.
- **Plans d'energia:** *Alt rendiment* vs. *Estalvi d'energia*.
- Desactivar programes d'inici innecessaris; mantenir drivers i SO actualitzats; comprovar temperatura i pols.
- Línia base (*baseline*): mesurar el rendiment «normal» per poder comparar quan alguna cosa va malament.

## 5.7. La base de dades de configuració del SO

Tota la configuració del SO, el maquinari instal·lat i les aplicacions es guarda en una base de dades:

### Windows — el Registre

Base de dades jeràrquica. Eina: **`regedit`**. Branques principals (*hives*):

| Branca | Contingut |
|---|---|
| `HKEY_LOCAL_MACHINE` (HKLM) | Configuració de l'equip: maquinari, drivers, serveis, programari per a tots els usuaris |
| `HKEY_CURRENT_USER` (HKCU) | Configuració de l'usuari amb sessió (fitxer `NTUSER.DAT`) |
| `HKEY_USERS` | Perfils de tots els usuaris |
| `HKEY_CLASSES_ROOT` | Associacions de fitxers i objectes COM |
| `HKEY_CURRENT_CONFIG` | Perfil de maquinari actual |

Consulta/edició per CLI: `reg query`, `reg add`, `reg export`. **Sempre exporta la branca abans d'editar-la.**

### Linux — no hi ha un registre únic

- **`/etc/`**: fitxers de text de configuració del sistema (per servei/aplicació).
- **`~/.config/`, `~/.local/`, dotfiles**: configuració per usuari.
- **`/proc/` i `/sys/`**: sistemes d'arxius virtuals amb l'estat del nucli i els paràmetres ajustables
  (`sysctl -a`, `/etc/sysctl.conf`).
- **dconf/GSettings**: base de dades binària de configuració de GNOME (`gsettings`, `dconf`).
- **`systemd`**: unitats a `/lib/systemd/system` (per defecte) i `/etc/systemd/system` (personalitzacions).

> Avantatge del model de fitxers de text: es poden **versionar, copiar i comparar** fàcilment (`diff`, Git).

## 5.8. Resum

- Monitorar **CPU, memòria, disc i xarxa**; comparar amb una línia base.
- Windows: Administrador de tasques, **`resmon`**, **`perfmon`**, **Visor d'esdeveniments**. Linux: `top`/`htop`,
  `free`, `vmstat`, `iostat`, `journalctl`, `/var/log/`.
- Optimitzar memòria (aplicacions d'inici, swap, +RAM) i emmagatzematge (**TRIM** per SSD, desfragmentar HDD,
  SMART, neteja).
- La configuració es guarda al **Registre** (Windows, `regedit`, *hives* HKLM/HKCU) o en **fitxers de text a
  `/etc`** + `/proc`,`/sys`, dconf i systemd (Linux).

## Comprova què has après

1. Quina eina de Windows mostra quins fitxers té oberts cada procés en temps real?
2. Què indica la «càrrega mitjana» de `uptime` i amb què l'has de comparar?
3. Diferències entre optimitzar un HDD i un SSD.
4. Quines dues branques principals del Registre separen la configuració de l'equip i la de l'usuari?
5. On guarda Linux la configuració del sistema i quins avantatges té respecte d'un registre binari?
6. Com veus en temps real els missatges del sistema a Linux?

---

[⬅ Anterior: Serveis del sistema](04-serveis-del-sistema.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Màquines virtuals ➡](../05-maquines-virtuals/00-index.md)
