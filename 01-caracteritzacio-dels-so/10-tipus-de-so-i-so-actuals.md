[⬅ Anterior: Tipus de sistemes d'arxius](09-tipus-de-sistemes-d-arxius.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Administració ➡](../04-administracio-del-so/00-index.md)

# 10. Tipus de sistemes operatius i SO actuals

> Criteri d'avaluació RA1.1 — *tipus i aplicacions dels sistemes operatius.*

## 10.1. Segons el nombre d'usuaris

| Tipus | Descripció | Exemples |
|---|---|---|
| **Monousuari (monolloc)** | Un sol usuari fa servir tots els recursos de l'equip a la vegada. | MS-DOS, Windows 9x |
| **Multiusuari** | Diversos usuaris fan servir el sistema simultàniament (per terminals o per xarxa), cadascun amb la seva configuració i permisos. | UNIX/Linux, Windows (sessions múltiples / Escriptori remot), macOS, mainframes |

> Els SO **actuals d'escriptori** (Windows 11, Linux, macOS) són tècnicament **multiusuari**: encara que
> normalment els fa servir una persona, gestionen diversos comptes amb perfils i permisos separats i permeten
> sessions simultànies.

## 10.2. Segons el nombre de processos

| Tipus | Descripció |
|---|---|
| **Monotasca (monoprogramació)** | Només executa un programa alhora; els recursos són per a ell fins que acaba. (MS-DOS) |
| **Multitasca (multiprogramació)** | Executa diversos processos concurrentment repartint el temps de CPU. Amb una sola CPU és concurrència aparent; amb diverses, paral·lelisme real. Tots els SO actuals. |
| **Pseudomultitasca** | Sembla multitasca però el nucli no aprofita més d'un processador (Windows 95/98/Me). |

Tipus de multitasca: **cooperativa** (cada procés cedeix la CPU voluntàriament; si un es penja, penja tot —
Windows 3.x) vs. **expropiativa / *preemptive*** (el SO retira la CPU quan cal — tots els SO moderns).

## 10.3. Segons el nombre de processadors

- **Monoprocessador:** un sol processador; tots els treballs hi passen.
- **Multiprocessador:** dos o més processadors/nuclis. El SO reparteix la càrrega:
  - **SMP (multiprocés simètric):** tots els nuclis són equivalents i el SO els fa servir per igual. És el model
    habitual dels PC actuals.
  - **AMP (multiprocés asimètric):** cada nucli s'assigna a tasques concretes.

## 10.4. Segons el temps de resposta / mode d'explotació

| Mode | Descripció | Exemple |
|---|---|---|
| **Per lots (*batch*)** | Els treballs s'agrupen i s'executen sense interacció; els resultats s'obtenen després. | Processament nocturn de nòmines, *jobs* de clúster |
| **Temps compartit (interactiu)** | Diversos usuaris/processos comparteixen la CPU amb quàntums; resposta ràpida. | SO d'escriptori i servidors |
| **Temps real (RTOS)** | Garanteix una resposta **dins d'un termini màxim**. *Dur* (incompliment = fallada crítica) o *tou*. | Control industrial, automoció (frens ABS), aviònica, marcapassos |
| **Distribuït** | Diversos ordinadors cooperen i es presenten com un únic sistema. | Clústers, sistemes en núvol |

## 10.5. Segons la llicència

- **Propietari:** codi tancat, ús subjecte a llicència de pagament o condicions del fabricant (Windows, macOS).
- **Lliure / de codi obert:** es pot usar, estudiar, modificar i redistribuir (GNU/Linux amb llicència GPL,
  FreeBSD amb llicència BSD). Vegeu [RA2 · llicències](../02-instal-lacio-de-so/07-llicencies-actualitzacio-i-incidencies.md).

## 10.6. Segons l'àmbit d'ús

| Àmbit | SO habituals |
|---|---|
| **Escriptori / portàtil** | Windows 10/11, distribucions Linux (Ubuntu, Fedora, Debian, Mint), macOS |
| **Servidor** | Windows Server, RHEL, Ubuntu Server, Debian, SUSE Linux Enterprise |
| **Mòbil / tauleta** | Android (nucli Linux), iOS/iPadOS |
| **Encastat / IoT** | Linux encastat, FreeRTOS, Zephyr, VxWorks |
| **Núvol / contenidors** | Linux amb virtualització i contenidors (Docker, Kubernetes) |

## 10.7. Panorama actual (família per família)

- **Windows** (Microsoft, propietari, nucli **NT** híbrid): Windows 10, **Windows 11**, Windows Server 2022/2025.
  Multiusuari, multitasca expropiativa, SMP, sistema d'arxius NTFS/ReFS.
- **GNU/Linux** (lliure, nucli **monolític modular**): el nucli és Linux; les **distribucions** hi afegeixen
  entorn i eines. Famílies: Debian → Ubuntu → Mint; Red Hat → Fedora, RHEL, Rocky, Alma; SUSE → openSUSE.
  Entorns d'escriptori: GNOME, KDE Plasma, XFCE, Cinnamon.
- **macOS** (Apple, propietari): nucli **XNU** (híbrid, base Darwin/BSD + Mach). Sistema d'arxius APFS.
- **BSD** (lliure): FreeBSD, OpenBSD, NetBSD — molt usats en servidors i xarxa.
- **Android / ChromeOS:** basats en el nucli Linux, per a mòbils i portàtils lleugers.

## 10.8. Aquest mòdul: SO monolloc vs. SO en xarxa

- **SO monolloc (aquest mòdul, 0222):** l'equip treballa aïllat o com a client; l'usuari inicia sessió
  **localment**. S'hi estudia instal·lació, configuració i administració bàsica d'un equip.
- **SO en xarxa (mòdul 0224, 2n curs):** l'equip **comparteix recursos** i valida usuaris a través de la xarxa
  (dominis, servei de directori, perfils mòbils, recursos compartits).

## 10.9. Resum

- Es classifiquen per **usuaris** (mono/multi), **processos** (mono/multitasca), **processadors** (mono/multi,
  SMP/AMP), **temps de resposta** (lots, temps compartit, temps real, distribuït), **llicència** i **àmbit d'ús**.
- Els SO d'escriptori actuals són multiusuari + multitasca expropiativa + SMP.
- Windows (propietari, NT), GNU/Linux (lliure, distribucions), macOS (propietari, XNU) són les grans famílies
  d'escriptori.

## Comprova què has après

1. Per què Windows 11, tot i fer-lo servir una sola persona, es considera multiusuari?
2. Diferència entre multitasca cooperativa i expropiativa. Quin risc té la cooperativa?
3. Què caracteritza un SO de temps real dur? Posa'n un exemple.
4. Què aporta una «distribució» de Linux respecte del nucli?
5. En què es diferencia el que estudies en aquest mòdul (0222) del mòdul de SO en xarxa (0224)?

---

[⬅ Anterior: Tipus de sistemes d'arxius](09-tipus-de-sistemes-d-arxius.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Administració ➡](../04-administracio-del-so/00-index.md)
