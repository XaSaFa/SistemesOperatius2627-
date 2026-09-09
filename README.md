# Base de coneixements — Sistemes operatius monolloc (MP0222)

Base de coneixements del mòdul professional **0222 · Sistemes operatius monolloc** del
cicle formatiu de grau mitjà **Sistemes Microinformàtics i Xarxes (SMX)** de la Generalitat de Catalunya.

- **Durada del mòdul:** 132 h (99 h al centre + 33 h d'estada a l'empresa).
- **Curs:** 1r.
- **Font curricular:** Decret 193/2013 (SMX) i document d'orientacions IC10 del Departament d'Educació.
- **Fonts de contingut:** llibre *Sistemas operativos monopuesto* (F. J. Muñoz López, McGraw-Hill) i
  documentació oficial de fabricants (Microsoft Learn, pàgines de manual de Linux, documentació d'Ubuntu/Debian/Red Hat).
  Vegeu [00-referencia/03-fonts-i-bibliografia.md](00-referencia/03-fonts-i-bibliografia.md).

> **Nota de vigència.** Els llibres de referència descriuen Windows XP/7 i Ubuntu 11.10. En aquesta base de
> coneixements s'ha actualitzat el contingut a **Windows 10/11**, **systemd**, **ext4/exFAT/Btrfs** i les eines
> actuals, mantenint la seqüència didàctica del currículum. Quan un concepte històric encara té valor formatiu
> (FAT, MBR, `init`…) es conserva i s'indica que és llegat.

---

## Com navegar aquesta base de coneixements

- Cada **bloc** (carpeta numerada) es correspon amb un **resultat d'aprenentatge (RA)** del currículum.
- Dins de cada bloc, el fitxer `00-index.md` llista els temes i els relaciona amb els **criteris d'avaluació**.
- Cada tema té una barra de navegació a dalt i a baix:
  `Anterior · Índex del bloc · Índex general · Següent`.
- Els enllaços `[[text]]` o `[text](ruta)` porten a altres temes relacionats.
- El [glossari](00-referencia/02-glossari.md) recull les definicions clau amb enllaç al tema on s'expliquen.

---

## Mapa de continguts

### 00 · Referència
| Fitxer | Contingut |
|---|---|
| [Currículum oficial](00-referencia/01-curriculum-oficial.md) | RA, criteris d'avaluació i continguts del mòdul 0222 (text del currículum). |
| [Glossari](00-referencia/02-glossari.md) | Termes clau ordenats alfabèticament. |
| [Fonts i bibliografia](00-referencia/03-fonts-i-bibliografia.md) | Llibres i documentació oficial utilitzats, amb enllaços. |

### 01 · Caracterització dels sistemes operatius — **RA1**
> *Reconeix les característiques dels sistemes operatius, descrivint-ne els tipus i aplicacions.*

| # | Tema |
|---|---|
| 01 | [El sistema informàtic: maquinari, programari i microprogramari](01-caracteritzacio-dels-so/01-sistema-informatic-hardware-software-firmware.md) |
| 02 | [Representació de la informació](01-caracteritzacio-dels-so/02-representacio-de-la-informacio.md) |
| 03 | [Concepte, funcions i estructura del sistema operatiu](01-caracteritzacio-dels-so/03-concepte-funcions-i-estructura-del-so.md) |
| 04 | [Processos, fils i planificació](01-caracteritzacio-dels-so/04-processos-i-planificacio.md) |
| 05 | [Gestió de la memòria](01-caracteritzacio-dels-so/05-gestio-de-memoria.md) |
| 06 | [Gestió d'entrada/sortida i interfícies d'usuari](01-caracteritzacio-dels-so/06-gestio-es-i-interficies.md) |
| 07 | [El sistema d'arxius: conceptes](01-caracteritzacio-dels-so/07-sistemes-d-arxius-conceptes.md) |
| 08 | [Arxius, directoris, atributs i permisos](01-caracteritzacio-dels-so/08-arxius-directoris-atributs-i-permisos.md) |
| 09 | [Tipus de sistemes d'arxius i sistemes transaccionals](01-caracteritzacio-dels-so/09-tipus-de-sistemes-d-arxius.md) |
| 10 | [Tipus de sistemes operatius i SO actuals](01-caracteritzacio-dels-so/10-tipus-de-so-i-so-actuals.md) |

### 02 · Instal·lació de sistemes operatius — **RA2**
> *Instal·la sistemes operatius, relacionant-ne les característiques amb el maquinari i el programari d'aplicació.*

| # | Tema |
|---|---|
| 01 | [Requisits tècnics i compatibilitat del maquinari](02-instal-lacio-de-so/01-requisits-i-compatibilitat.md) |
| 02 | [Particions i estructura del disc](02-instal-lacio-de-so/02-particions-i-estructura-del-disc.md) |
| 03 | [El pla i les fases d'instal·lació](02-instal-lacio-de-so/03-pla-i-fases-d-instal-lacio.md) |
| 04 | [El gestor d'arrencada](02-instal-lacio-de-so/04-gestor-d-arrencada.md) |
| 05 | [Instal·lació de Windows](02-instal-lacio-de-so/05-instal-lacio-de-windows.md) |
| 06 | [Instal·lació de Linux](02-instal-lacio-de-so/06-instal-lacio-de-linux.md) |
| 07 | [Llicències, actualització i incidències](02-instal-lacio-de-so/07-llicencies-actualitzacio-i-incidencies.md) |

### 03 · Configuració bàsica del sistema operatiu — **RA3**
> *Realitza tasques bàsiques de configuració de sistemes operatius, interpretant-ne requeriments i descrivint-ne els procediments.*

| # | Tema |
|---|---|
| 01 | [Arrencada, parada i sessions](03-configuracio-basica/01-arrencada-parada-i-sessions.md) |
| 02 | [Interfícies d'usuari i preferències de l'entorn](03-configuracio-basica/02-interficies-d-usuari-i-preferencies.md) |
| 03 | [Gestió de discos i sistemes d'arxius](03-configuracio-basica/03-gestio-de-discos-i-sistemes-d-arxius.md) |
| 04 | [Programari, actualitzacions i automatització de tasques](03-configuracio-basica/04-programari-actualitzacions-i-automatitzacio.md) |
| 05 | [Recuperació del sistema operatiu](03-configuracio-basica/05-recuperacio-del-so.md) |

### 04 · Administració del sistema operatiu — **RA4**
> *Realitza operacions bàsiques d'administració de sistemes operatius, interpretant requeriments i optimitzant el sistema.*

| # | Tema |
|---|---|
| 01 | [Usuaris, grups i contrasenyes](04-administracio-del-so/01-usuaris-grups-i-contrasenyes.md) |
| 02 | [Permisos i recursos compartits](04-administracio-del-so/02-permisos-i-recursos-compartits.md) |
| 03 | [Gestió de processos](04-administracio-del-so/03-gestio-de-processos.md) |
| 04 | [Serveis del sistema](04-administracio-del-so/04-serveis-del-sistema.md) |
| 05 | [Monitoratge, rendiment i registres](04-administracio-del-so/05-monitoratge-rendiment-i-registres.md) |

### 05 · Màquines virtuals — **RA5**
> *Crea màquines virtuals identificant-ne el camp d'aplicació i instal·lant-hi programari específic.*

| # | Tema |
|---|---|
| 01 | [Virtualització: conceptes](05-maquines-virtuals/01-virtualitzacio-conceptes.md) |
| 02 | [Programari de virtualització i creació de màquines virtuals](05-maquines-virtuals/02-programari-i-creacio-de-mv.md) |

---

## Relació RA ↔ blocs de contingut del currículum

| RA | Bloc de continguts oficials | Carpeta |
|---|---|---|
| RA1 | Caracterització de sistemes operatius | `01-caracteritzacio-dels-so/` |
| RA2 | Instal·lació de sistemes operatius lliures i propietaris | `02-instal-lacio-de-so/` |
| RA3 | Realització de tasques bàsiques sobre sistemes operatius | `03-configuracio-basica/` |
| RA4 | Administració dels sistemes operatius | `04-administracio-del-so/` |
| RA5 | Configuració de màquines virtuals | `05-maquines-virtuals/` |
