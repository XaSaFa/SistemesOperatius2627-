[⬅ Anterior: Permisos i recursos compartits](02-permisos-i-recursos-compartits.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Serveis del sistema ➡](04-serveis-del-sistema.md)

# 3. Gestió de processos

> Criteri d'avaluació RA4.3 — *Actua sobre els processos de l'usuari en funció de les necessitats puntuals.*
> Base teòrica: [RA1 · processos i planificació](../01-caracteritzacio-dels-so/04-processos-i-planificacio.md).

## 3.1. Què pot fer l'administrador amb un procés

- **Veure'l:** nom, **PID/PPID**, usuari propietari, estat, consum de CPU i memòria, fitxers oberts.
- **Iniciar-lo / relanç ar-lo.**
- **Finalitzar-lo** de manera ordenada (l'aplicació tanca fitxers i allibera recursos) o **matar-lo** de
  manera incondicional (si està penjat).
- **Finalitzar l'arbre** (procés pare + fills).
- **Canviar-ne la prioritat** perquè rebi més o menys temps de CPU.
- **Fixar l'afinitat** (lligar-lo a nuclis concrets).
- **Suspendre'l / reprendre'l.**

## 3.2. Windows

### GUI — Administrador de tasques (`Ctrl+Maj+Esc`)

| Pestanya | Contingut |
|---|---|
| **Processos** | Aplicacions i processos en segon pla amb CPU, memòria, disc, xarxa, GPU |
| **Rendiment** | Gràfiques de CPU, memòria, disc, xarxa, GPU |
| **Historial d'aplicacions** | Consum acumulat d'aplicacions de la Store |
| **Aplicacions d'inici** | Programes que arrenquen amb la sessió (habilitar/deshabilitar) |
| **Usuaris** | Processos per usuari amb sessió oberta |
| **Detalls** | Vista clàssica per PID; clic dret → *Finalitza la tasca*, *Finalitza l'arbre de processos*, *Estableix la prioritat*, *Estableix l'afinitat*, *Vés al servei*, *Obre la ubicació del fitxer* |
| **Serveis** | Enllaç ràpid a `services.msc` |

Prioritats: *Temps real, Alta, Superior a la normal, Normal, Inferior a la normal, Baixa*. Cal usar-les amb cura
(*Temps real* pot deixar l'equip sense resposta).

Eina avançada: **Monitor de recursos** (`resmon`) i **Process Explorer** (Sysinternals).

### CLI

```
tasklist                          :: llistar processos (PID, memòria, sessió)
tasklist /svc                     :: quins serveis allotja cada procés
tasklist /fi "IMAGENAME eq chrome.exe"
taskkill /IM notepad.exe          :: matar per nom
taskkill /PID 4321 /F             :: forçar per PID
taskkill /PID 4321 /T /F          :: + arbre de processos fills
start "" /LOW  programa.exe        :: iniciar amb prioritat baixa
wmic process where name='x.exe' call setpriority 64   :: (llegat) canviar prioritat
```

PowerShell:
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process chrome
Stop-Process -Name notepad
Stop-Process -Id 4321 -Force
Start-Process app.exe
(Get-Process x).PriorityClass = 'BelowNormal'
```

## 3.3. Linux

### Veure processos

```bash
ps aux                 # tots els processos (BSD): usuari, PID, %CPU, %MEM, STAT, ordre
ps -ef                 # format System V; -f mostra el PPID
ps -eo pid,ppid,user,ni,stat,%cpu,%mem,comm --sort=-%cpu | head
pstree -p              # arbre de processos
top                    # monitor interactiu (q per sortir)
htop                   # versió millorada (cal instal·lar-la); F9 mata, F7/F8 renice
```

**Codis d'estat (`STAT`)** de `ps`/`top`:

| Codi | Estat |
|---|---|
| `R` | En execució o preparat (*runnable*) |
| `S` | Adormit interrompible (esperant un esdeveniment) |
| `D` | Adormit ininterrompible (normalment E/S de disc) |
| `T` | Aturat (`Ctrl+Z`, `kill -STOP`) |
| `Z` | **Zombi** (acabat, esperant que el pare el reculli) |
| `I` | Fil de nucli ociós |
| Sufixos | `s` líder de sessió, `+` en primer pla, `l` multifil, `<` prioritat alta, `N` prioritat baixa |

### Finalitzar processos: senyals

```bash
kill 4321               # envia SIGTERM (15): demana acabar ordenadament
kill -TERM 4321
kill -HUP 4321          # SIGHUP (1): sovint "recarrega la configuració"
kill -STOP 4321         # pausar
kill -CONT 4321         # reprendre
kill -KILL 4321         # SIGKILL (9): matar incondicionalment (últim recurs)
kill -9 4321
killall firefox         # per nom (tots els que coincideixin)
killall -9 firefox
pkill -u anna           # per criteri (usuari, patró...)
pgrep -a chrome         # trobar PID per nom
xkill                   # (GUI) fer clic a la finestra a tancar
```

> Ordre recomanat: primer `SIGTERM`, i només si no respon, `SIGKILL`. Un procés **zombi** no es pot matar
> (ja és mort); desapareix quan el pare el recull o quan es mata el pare.

### Prioritat: `nice` i `renice`

La prioritat d'usuari es controla amb el valor **nice (NI)**, de **−20** (màxima prioritat) a **+19** (mínima).
Els usuaris normals només poden **baixar** la prioritat (valors positius); root pot posar valors negatius.

```bash
nice -n 10 ./tasca_pesada.sh        # iniciar amb NI=10 (menys prioritat)
renice -n 5 -p 4321                 # canviar la d'un procés existent
renice -n -5 -p 4321                # (només root) més prioritat
```

### Afinitat de CPU

```bash
taskset -cp 0,1 4321               # lligar el PID 4321 als nuclis 0 i 1
```

### Processos en primer/segon pla i sessions

```bash
comanda &            # executar en segon pla
jobs                 # tasques de la shell actual
fg %1  / bg %1       # portar al primer pla / reprendre en segon pla
Ctrl+Z               # suspendre la tasca en primer pla
nohup comanda &      # que sobrevisqui al tancament de la terminal
```

## 3.4. Casos d'ús típics

| Necessitat | Acció |
|---|---|
| Una aplicació no respon | Windows: *Finalitza la tasca*. Linux: `kill PID`; si no, `kill -9 PID` |
| Una còpia/còdec consumeix tota la CPU i alenteix la feina | Baixar-ne la prioritat: prioritat *Baixa* / `renice -n 15 -p PID` |
| Un procés obre molts fills que no es tanquen | *Finalitza l'arbre de processos* / `pkill -P PID` o `kill` al pare |
| Saber quin programa té bloquejat un fitxer | Windows: Process Explorer → *Find Handle*. Linux: `lsof fitxer` / `fuser fitxer` |
| Deixar una tasca llarga corrent i tancar la sessió SSH | `nohup ... &`, `tmux` o `screen` |

## 3.5. Resum

- L'administrador pot **veure, iniciar, finalitzar, matar, suspendre, reprendre** processos i canviar-ne
  **prioritat** i **afinitat**.
- Windows: **Administrador de tasques** / `tasklist` / `taskkill /PID n /T /F` / `Get-Process`,`Stop-Process`.
- Linux: `ps aux`, `top`/`htop`, `pstree`; **senyals** amb `kill` (`SIGTERM` abans que `SIGKILL`), `killall`,
  `pkill`; prioritat amb **`nice`/`renice`** (−20…+19), afinitat amb `taskset`.
- **Finalitzar** = tancament ordenat; **matar** (`-9` / `/F`) = incondicional, últim recurs. Els **zombis** no
  es maten.

## Comprova què has après

1. Diferència entre `taskkill /PID 100` i `taskkill /PID 100 /F /T`.
2. Quin senyal envia `kill` per defecte i quin envia `kill -9`? Quan usaries el segon?
3. Un usuari normal, pot posar un procés amb `nice -n -5`? Per què?
4. Què és un procés zombi i com se n'elimina?
5. Com deixes corrent una tasca llarga per SSH i tanques la connexió sense que s'aturi?

---

[⬅ Anterior: Permisos i recursos compartits](02-permisos-i-recursos-compartits.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Serveis del sistema ➡](04-serveis-del-sistema.md)
