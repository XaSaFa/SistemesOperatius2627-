[🏠 Inici](../README.md) › **RA3 · Configuració bàsica del sistema operatiu**

[⬅ Bloc anterior: Màquines virtuals](../05-maquines-virtuals/00-index.md) · [Bloc següent: Instal·lació ➡](../02-instal-lacio-de-so/00-index.md)

# Bloc 03 · Configuració bàsica del sistema operatiu (RA3)

> **RA3.** Realitza tasques bàsiques de configuració de sistemes operatius, interpretant-ne requeriments i
> descrivint-ne els procediments seguits.

Aquest bloc es treballa en dues parts: primer **RA3.1 · Linux** (ruta principal i detallada) i després
**RA3.2 · Windows** (repàs comparatiu més breu, amb les eines pròpies del sistema).

## RA3.1 · Linux (i multiplataforma)

Desenvolupament a fons. Els requadres de cada tema comparen amb Windows.

| # | Tema | Criteris d'avaluació |
|---|---|---|
| 1 | [Arrencada, parada i sessions](01-arrencada-parada-i-sessions.md) | CA1 |
| 2 | [Interfícies d'usuari i preferències de l'entorn](02-interficies-d-usuari-i-preferencies.md) | CA1, CA2 |
| 3 | [Gestió de discos i sistemes d'arxius](03-gestio-de-discos-i-sistemes-d-arxius.md) | CA3 |
| 4 | [Programari, actualitzacions i automatització de tasques](04-programari-actualitzacions-i-automatitzacio.md) | CA5, CA6, CA7, CA8 |
| 5 | [Recuperació del sistema operatiu](05-recuperacio-del-so.md) | CA4 |

## RA3.2 · Windows

Repàs comparatiu centrat en Windows 10/11, amb els mateixos criteris d'avaluació.

| Tema | Criteris d'avaluació |
|---|---|
| [Configuració a Windows](windows.md) | CA1–CA8 |

## Idees força del bloc

- L'usuari treballa dins d'una **sessió**; el sistema s'ha d'engegar i **aturar de manera ordenada** per no
  corrompre dades.
- Hi ha dues **interfícies**: gràfica (GUI) i de línia d'ordres (CLI); totes dues es poden **personalitzar**.
- Cal saber **muntar, formatar, comprovar i comprimir** volums i fitxers.
- El programari s'**instal·la i es desinstal·la** de maneres diferents segons el SO (botiga, `apt`, `winget`, `.msi`, `.deb`…).
- Les tasques repetitives s'**automatitzen** amb el Programador de tasques o `cron`/`systemd timers`.
- Sempre hi ha d'haver un **pla de recuperació** (punts de restauració, mode segur, imatges, `chroot`).

---

[Primer tema ➡](01-arrencada-parada-i-sessions.md)
