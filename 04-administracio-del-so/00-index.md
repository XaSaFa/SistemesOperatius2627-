[🏠 Inici](../README.md) › **RA4 · Administració del sistema operatiu**

[⬅ Bloc anterior: Caracterització](../01-caracteritzacio-dels-so/00-index.md) · [🏠 Inici](../README.md) · [Bloc següent: Màquines virtuals ➡](../05-maquines-virtuals/00-index.md)

# Bloc 04 · Administració del sistema operatiu (RA4)

> **RA4.** Realitza operacions bàsiques d'administració de sistemes operatius, interpretant requeriments i
> optimitzant el sistema per al seu ús.

## Temes del bloc

| # | Tema | Criteris d'avaluació |
|---|---|---|
| 01 | [Usuaris, grups i contrasenyes](01-usuaris-grups-i-contrasenyes.md) | CA1 |
| 02 | [Permisos i recursos compartits](02-permisos-i-recursos-compartits.md) | CA2, CA8 |
| 03 | [Gestió de processos](03-gestio-de-processos.md) | CA3 |
| 04 | [Serveis del sistema](04-serveis-del-sistema.md) | CA4 |
| 05 | [Monitoratge, rendiment i registres](05-monitoratge-rendiment-i-registres.md) | CA5, CA6, CA7, CA9 |

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

[🏠 Inici](../README.md) · [Primer tema ➡](01-usuaris-grups-i-contrasenyes.md)
