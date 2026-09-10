[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **4. Processos, fils i planificació**

[⬅ Anterior: Concepte del SO](03-concepte-funcions-i-estructura-del-so.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Gestió de la memòria ➡](05-gestio-de-memoria.md)

# 4. Processos, fils i planificació

> Criteri d'avaluació RA1.3 — *Identifica els processos i els seus estats.*

## 4.1. Programa vs. procés

- Un **programa** és un fitxer passiu emmagatzemat al disc (per exemple `WINWORD.EXE`).
- Un **procés** és un **programa en execució**: quan es llança, les seves instruccions i dades es carreguen a la
  RAM i el SO li assigna recursos i una estructura de control. El fitxer original continua al disc sense canvis.

Segons el context, un procés també s'anomena **tasca** o **treball**.

## 4.2. Bloc de control de procés (BCP / PCB)

Per cada procés, el SO manté una estructura de dades única, el **BCP**, amb tota la informació que necessita
per controlar-lo:

- **PID** (identificador del procés) i, si escau, **PPID** (identificador del procés pare).
- **Estat** actual (preparat, en execució, bloquejat…).
- **Prioritat** assignada pel planificador.
- **Comptador de programa** i valors dels registres de la CPU (context).
- **Ubicació en memòria** (adreces del codi, dades i pila).
- **Recursos**: fitxers oberts, dispositius, límits, usuari propietari.

Els processos formen una **jerarquia**: cada procés el crea un altre (**procés pare** → **procés fill**). A
Linux, el procés arrel és `systemd`/`init` (PID 1). Si el pare acaba abans que el fill, aquest queda **orfe** i
l'adopta PID 1.

## 4.3. Fils d'execució (*threads*)

Un **fil** (bri, *thread*) és un punt d'execució dins d'un procés. Tot procés té almenys un fil; pot tenir-ne
molts. Els fils d'un **mateix procés comparteixen** l'espai de memòria, els fitxers oberts i els recursos, però
cadascun té la seva pila i el seu comptador de programa.

- Avantatge: paral·lelisme dins d'una aplicació amb menys cost que crear processos (per exemple, un editor que
  alhora corregeix ortografia, desa una còpia i renderitza).
- Exemple del llibre: obrir un segon document a Word **no** llança un segon procés Word; crea un fil nou del
  procés existent.

## 4.4. Estats d'un procés

Model bàsic de tres estats:

```
        (admissió)                 (fi de quàntum / expropiació)
  NOU ───────────► PREPARAT ◄───────────────────────────── EN EXECUCIÓ
                     ▲   │  (el planificador li assigna CPU)     │
                     │   └────────────────────────────────────►─┘
   (arriba l'esdeveniment │                                      │ (demana E/S o
    esperat: transició D) │                                      │  un recurs: transició A)
                     BLOQUEJAT ◄───────────────────────────────┘
                                                              ► TERMINAT
```

| Estat | Descripció |
|---|---|
| **Nou** | El procés s'acaba de crear; encara no s'ha admès a la cua de preparats. |
| **Preparat / a punt / actiu** | Té tot el que necessita i espera torn de CPU. |
| **En execució** | La CPU executa les seves instruccions ara mateix. En un sistema d'una sola CPU només n'hi ha un en aquest estat. |
| **Bloquejat / en espera** | No pot continuar fins que passi un esdeveniment (fi d'una operació d'E/S, alliberament d'un recurs, senyal). No consumeix CPU. |
| **Terminat / zombi** | Ha acabat. A Linux queda un instant en estat **zombi (Z)** fins que el pare recull el seu codi de sortida. |

També es descriuen els estats **parat/suspès (T)** (aturat manualment, per exemple amb `Ctrl+Z` o `kill -STOP`).

### Transicions (llibre de referència)

- **A** — En execució → Bloquejat: el procés necessita un dato/senyal/recurs per continuar.
- **B** — En execució → Preparat: s'ha esgotat el quàntum de CPU i deixa pas a un altre procés.
- **C** — Preparat → En execució: el planificador li concedeix la CPU.
- **D** — Bloquejat → Preparat: arriba l'esdeveniment que esperava.

## 4.5. Canvi de context

Quan la CPU deixa un procés i passa a un altre es produeix un **canvi de context**: es desa l'estat (registres,
comptador de programa) del procés sortint al seu BCP i es carrega el del procés entrant.

- **Parcial:** entre fils del mateix procés (comparteixen memòria).
- **Complet:** entre processos diferents (cal canviar mapes de memòria, cau, etc.). És més costós.

## 4.6. Planificació de la CPU

El **planificador (*scheduler*)** és la part del SO que decideix quin procés preparat passa a executar-se i
durant quant de temps, per assolir objectius com **equitat**, **eficiència**, **temps de resposta** curt i bon
**rendiment** (*throughput*).

- **Prioritat:** valor que determina quants cicles de CPU rep un procés respecte dels altres. L'assigna
  l'administrador o el propi SO (i pot ser dinàmica).
- **Quàntum:** interval curt de temps de CPU que s'assigna a cada procés en **temps compartit**.
- **Multiprogramació:** repartiment concurrent dels recursos entre diversos processos.

### Algorismes clàssics

| Algorisme | Com funciona | Ús típic |
|---|---|---|
| **FIFO / FCFS** (*First Come First Served*) | S'executa sencer el primer procés que arriba; després el següent. No expropiatiu. | Cues d'impressió, treballs per lots |
| **Round-Robin (per torns)** | Cua FIFO + quàntum fix: cada procés rep el mateix temps i, si no acaba, torna al final de la cua. Expropiatiu. | SO interactius monousuari i multiusuari actuals |
| **Per prioritats** | Executa el procés preparat de prioritat més alta. Risc d'*inanició* dels de prioritat baixa (es mitiga amb *aging*). | Sistemes amb tasques crítiques |
| **SJF** (*Shortest Job First*) | Primer el procés més curt. Òptim per al temps mitjà d'espera, però cal estimar la durada. | Entorns predictibles |
| **Cues multinivell amb realimentació** | Diverses cues amb prioritats i quàntums diferents; els processos pugen o baixen de cua segons el seu comportament. | Windows i Linux moderns (variants) |

> Linux modern fa servir el **CFS** (*Completely Fair Scheduler*) i, des de la versió 6.6, **EEVDF**; Windows
> usa un planificador **expropiatiu per prioritats** amb 32 nivells i realimentació. Tots dos són evolucions de
> Round-Robin + prioritats.

## 4.7. Concurrència i multiprocessador

- Amb **una sola CPU** la multitasca és **aparent** (pseudoparal·lelisme): la CPU alterna processos molt de
  pressa. Windows 9x s'anomenava «pseudomultitasca» per aquest motiu.
- Amb **diverses CPU o nuclis** hi ha **paral·lelisme real**. El SO pot repartir la càrrega de manera
  **simètrica (SMP)** —tots els nuclis per igual— o **asimètrica (AMP)** —cada nucli per a tasques concretes—.
  L'**afinitat de processador** permet lligar un procés a un nucli concret.

## 4.8. Resum

- Programa = fitxer passiu; procés = programa en execució amb BCP, PID i estat.
- Estats bàsics: **preparat ↔ en execució ↔ bloquejat**; transicions A/B/C/D.
- El **planificador** reparteix la CPU (Round-Robin, FIFO, prioritats…). Quàntum = tros de temps de CPU.
- Els **fils** comparteixen memòria dins d'un procés; el **canvi de context** desa i restaura l'estat.

## Comprova què has après

1. Quan un programa passa a ser procés? Què li assigna el SO en aquell moment?
2. Descriu les quatre transicions entre estats i posa un exemple de la transició A.
3. Diferència entre un canvi de context parcial i un de complet.
4. Per què amb una sola CPU la multitasca es diu «aparent»?
5. Un procés en estat bloquejat, consumeix temps de CPU? I un en estat preparat?
6. Quin algorisme de planificació faries servir per a una cua d'impressió i per què?

---

[⬅ Anterior: Concepte del SO](03-concepte-funcions-i-estructura-del-so.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Gestió de la memòria ➡](05-gestio-de-memoria.md)
