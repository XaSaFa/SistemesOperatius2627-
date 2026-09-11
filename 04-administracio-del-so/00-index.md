[🏠 Inici](../README.md) › **RA4 · Administració del sistema operatiu**

[⬅ Bloc anterior: Caracterització](../01-caracteritzacio-dels-so/00-index.md) · [Bloc següent: Màquines virtuals ➡](../05-maquines-virtuals/00-index.md)

# Bloc 04 · Administració del sistema operatiu (RA4)

> **RA4.** Realitza operacions bàsiques d'administració de sistemes operatius, interpretant requeriments i
> optimitzant el sistema per al seu ús.

Aquest bloc es treballa en dues parts: primer **RA4.1 · Linux** (ruta principal i detallada) i després
**RA4.2 · Windows** (repàs comparatiu més breu, amb les eines pròpies del sistema).

## RA4.1 · Linux (i multiplataforma)

Desenvolupament a fons. Els requadres de cada tema comparen amb Windows.

| # | Tema | Criteris d'avaluació |
|---|---|---|
| 1 | [Usuaris, grups i contrasenyes](01-usuaris-grups-i-contrasenyes.md) | CA1 |
| 2 | [Permisos i recursos compartits](02-permisos-i-recursos-compartits.md) | CA2, CA8 |
| 3 | [Gestió de processos](03-gestio-de-processos.md) | CA3 |
| 4 | [Serveis del sistema](04-serveis-del-sistema.md) | CA4 |
| 5 | [Monitoratge, rendiment i registres](05-monitoratge-rendiment-i-registres.md) | CA5, CA6, CA7, CA9 |

## RA4.2 · Windows

Repàs comparatiu centrat en Windows 10/11, amb els mateixos criteris d'avaluació.

| Tema | Criteris d'avaluació |
|---|---|
| [Administració a Windows](windows.md) | CA1–CA9 |

## Idees força del bloc

- Cada **usuari** té un compte, un perfil i una pertinença a **grups** que determinen què pot fer.
- Els **permisos** (NTFS/ACL a Windows, `rwx` a Linux) protegeixen fitxers i recursos; els recursos es poden
  **compartir en xarxa** (SMB, NFS).
- L'administrador **actua sobre els processos** (prioritat, finalitzar, afinitat) i sobre els **serveis**
  (iniciar, aturar, habilitar, deshabilitar).
- Cal **monitorar** CPU, RAM, disc i xarxa, **optimitzar la memòria** i analitzar l'activitat amb els
  **registres** del sistema.
- La **base de dades de configuració** (Registre de Windows / `/etc` i `systemd` a Linux) guarda tot el
  comportament del SO.

---

[Primer tema ➡](01-usuaris-grups-i-contrasenyes.md)
