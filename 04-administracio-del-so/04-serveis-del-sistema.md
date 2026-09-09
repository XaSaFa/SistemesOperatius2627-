[⬅ Anterior: Gestió de processos](03-gestio-de-processos.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Monitoratge i registres ➡](05-monitoratge-rendiment-i-registres.md)

# 4. Serveis del sistema

> Criteri d'avaluació RA4.4 — *Actua sobre els serveis del sistema en funció de les necessitats puntuals.*

## 4.1. Què és un servei

Un **servei** (Windows) o **dimoni** (*daemon*, Linux) és un programa que s'executa **en segon pla**, sense
interfície, i que dona una funcionalitat: impressió, xarxa, tallafoc, base de dades, servidor web, actualitzacions…

- Molts s'instal·len amb el SO; d'altres els afegeixen les aplicacions (antivirus, VirtualBox, SGBD…).
- Alguns serveis **depenen d'altres**: si atures un servei del qual en depenen d'altres, aquests també
  deixaran de funcionar.
- Sovern arrenquen abans que cap usuari iniciï sessió i s'executen amb comptes especials (`SYSTEM`,
  `NETWORK SERVICE` a Windows; `root` o usuaris de sistema a Linux).

## 4.2. Estats i tipus d'inici

| Acció sobre un servei | Efecte |
|---|---|
| **Iniciar** | Es posa en marxa ara |
| **Aturar** | S'atura en aquesta sessió (pot tornar a arrencar al pròxim inici segons la configuració) |
| **Reiniciar** | Aturar + iniciar |
| **Pausar / reprendre** | Suspensió temporal (no tots ho admeten) |

| Tipus d'inici | Windows | Linux (systemd) |
|---|---|---|
| **Automàtic** | Arrenca amb el sistema | `systemctl enable` (arrenca a l'arrencada) |
| **Automàtic (inici retardat)** | Arrenca poc després per no alentir l'arrencada | — |
| **Manual / a petició** | Només quan alguna cosa el necessita | `static` / socket-activated |
| **Deshabilitat** | No arrenca | `systemctl disable` / `mask` (bloqueja del tot) |

## 4.3. Windows

### GUI — `services.msc`

Llista de serveis amb *Nom*, *Estat*, *Tipus d'inici* i *Inicia sessió com a*. Doble clic → propietats:

- Pestanya **General:** tipus d'inici; botons *Inicia / Atura / Pausa / Reprèn*; paràmetres d'inici.
- Pestanya **Inici de sessió:** compte amb què s'executa.
- Pestanya **Recuperació:** què fer si el servei falla (reiniciar-lo, executar un programa…).
- Pestanya **Dependències:** de quins serveis depèn i quins en depenen.

També hi ha la pestanya **Serveis** de l'Administrador de tasques (vista ràpida + *Vés al servei* des d'un procés).

### CLI

```
sc query                                :: llistar serveis i estat
sc query Spooler                        :: estat d'un servei
net start Spooler   /  net stop Spooler :: iniciar / aturar
sc start Spooler    /  sc stop Spooler
sc config Spooler start= auto           :: tipus d'inici (auto | demand | disabled)  (ull a l'espai després de "=")
sc qc Spooler                           :: configuració (binari, dependències)
```

PowerShell:
```powershell
Get-Service | Where-Object Status -eq 'Running'
Get-Service Spooler
Start-Service Spooler ; Stop-Service Spooler ; Restart-Service Spooler
Set-Service Spooler -StartupType Automatic
```

## 4.4. Linux — systemd

`systemd` gestiona **unitats**: `.service` (dimonis), `.socket`, `.timer` (tasques programades), `.target`
(agrupacions ≈ runlevels), `.mount`, `.device`.

```bash
systemctl status ssh                 # estat detallat + últimes línies del log
systemctl start ssh                  # iniciar ara
systemctl stop ssh                   # aturar ara
systemctl restart ssh                # reiniciar
systemctl reload ssh                 # rellegir la configuració sense tallar connexions
systemctl enable ssh                 # que arrenqui a l'arrencada
systemctl disable ssh                # que no arrenqui a l'arrencada
systemctl enable --now ssh           # habilitar i iniciar alhora
systemctl mask ssh                   # bloquejar del tot (ni manualment)
systemctl is-active ssh / is-enabled ssh
systemctl list-units --type=service            # serveis en execució
systemctl list-unit-files --type=service       # tots + estat (enabled/disabled)
systemctl --failed                              # serveis que han fallat
systemctl list-dependencies ssh                 # dependències
systemctl daemon-reload                          # després d'editar una unitat
```

Editar la configuració d'una unitat sense tocar l'original: `sudo systemctl edit ssh` (crea un
*drop-in* a `/etc/systemd/system/ssh.service.d/override.conf`).

### Sistemes antics (llegat)

- **SysV init:** `service apache2 start`, scripts a `/etc/init.d/`, `update-rc.d` per als enllaços de runlevel,
  `chkconfig` (Red Hat).
- **Upstart:** `initctl` (Ubuntu 2006–2014). `systemd` manté compatibilitat amb els scripts `/etc/init.d/`.

## 4.5. Casos d'ús

| Necessitat | Windows | Linux |
|---|---|---|
| Provar sense el tallafoc un moment | Aturar *Windows Defender Firewall* a `services.msc` (o millor: `netsh advfirewall set allprofiles state off`) | `sudo systemctl stop ufw` / `sudo ufw disable` |
| No es pot afegir una impressora | Comprovar/iniciar *Cua d'impressió* (Spooler) | `sudo systemctl start cups` |
| Desactivar un servei que no s'usa (rendiment/seguretat) | Tipus d'inici → *Deshabilitat* | `systemctl disable --now servei` |
| Un servei falla en arrencar | Pestanya *Recuperació* / veure `Visor d'esdeveniments` | `systemctl status servei` + `journalctl -u servei` |
| Aplicar canvis de configuració d'un servei | Reiniciar el servei | `systemctl reload` (si ho admet) o `restart` |

> **Precaució:** deshabilitar serveis del sistema «per guanyar rendiment» pot trencar funcionalitats (xarxa,
> àudio, actualitzacions, temps). Documenta sempre què has canviat.

## 4.6. Resum

- Servei/dimoni = programa en segon pla que dona funcionalitat; pot tenir **dependències**.
- Accions: **iniciar, aturar, reiniciar, pausar**; tipus d'inici: **automàtic, manual, deshabilitat**.
- Windows: `services.msc`, `sc`, `net start/stop`, `Get-Service`/`Set-Service`.
- Linux: **`systemctl`** (`start/stop/restart/reload`, `enable/disable/mask`, `status`, `list-units`); logs amb
  `journalctl -u servei`.

## Comprova què has après

1. Diferència entre aturar un servei i deshabilitar-lo.
2. Quina ordre de systemd fa que un servei s'iniciï i, alhora, quedi habilitat per a l'arrencada?
3. Si atures un servei del qual en depenen d'altres, què passa?
4. Amb quina ordre veus tots els serveis que han fallat a Linux?
5. Vols recarregar la configuració d'`ssh` sense tallar les sessions actives. Quina ordre uses?

---

[⬅ Anterior: Gestió de processos](03-gestio-de-processos.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Monitoratge i registres ➡](05-monitoratge-rendiment-i-registres.md)
