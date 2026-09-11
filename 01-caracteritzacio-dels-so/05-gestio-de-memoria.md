[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **5. Gestió de la memòria**

[⬅ Anterior: Processos](04-processos-i-planificacio.md) · [Següent: E/S i interfícies ➡](06-gestio-es-i-interficies.md)

# 5. Gestió de la memòria

> Criteris d'avaluació RA1.1 i RA1.3 — *Recursos del sistema operatiu i estats dels processos.*
> Relacionat amb RA4.5 — *optimització de la memòria disponible* ([RA4 · monitoratge](../04-administracio-del-so/05-monitoratge-rendiment-i-registres.md)).

## 5.1. Per què cal gestionar la memòria

Perquè un procés s'executi, el seu codi i les seves dades han d'estar a la **memòria principal (RAM)**. La RAM
és limitada i, en sistemes multitasca, diversos processos hi han de conviure alhora sense trepitjar-se. El
**gestor de memòria** del SO:

- Porta un registre de quines zones de RAM estan lliures i quines ocupades.
- Reserva memòria per als processos nous i l'allibera quan acaben.
- Aïlla i **protegeix** l'espai de cada procés (cap procés pot escriure a la memòria d'un altre).
- Gestiona l'intercanvi de dades entre RAM i disc quan els processos no hi caben tots.

## 5.2. Espai d'adreces i modes de gestió

- Cada procés «veu» un **espai d'adreces lògiques** propi, com si tingués tota la memòria per a ell. La **MMU**
  (*Memory Management Unit*, maquinari) tradueix les adreces lògiques a **adreces físiques** reals.
- **Mode real** (llegat, MS-DOS, Windows 9x): un únic espai pla sense protecció; un procés pot corrompre'n
  d'altres. Divisió històrica en memòria **convencional (0–640 KB)**, **superior (640 KB–1 MB)** i
  **estesa (> 1 MB)**.
- **Mode protegit** (Windows NT/2000/XP/…/11, UNIX/Linux, macOS): cada procés té el seu espai protegit; el
  maquinari impedeix accessos fora de rang. És el model de tots els SO actuals.

## 5.3. Assignació de memòria

| Tècnica | Idea | Problema |
|---|---|---|
| **Particions fixes** | La RAM es divideix en zones de mida predefinida; cada procés entra en una partició. | **Fragmentació interna** (el procés no omple la partició) |
| **Particions variables** | Les particions s'ajusten a la mida de cada procés. | **Fragmentació externa** (queden buits petits i dispersos inservibles) |
| **Reubicació / compactació** | Es mouen els processos per ajuntar l'espai lliure. | Cost de moure dades |
| **Memòria no contigua (paginació/segmentació)** | El procés s'esparella per la RAM en trossos. | Necessita taules de traducció |

## 5.4. Paginació, segmentació i intercanvi

- **Paginació:** la RAM es divideix en marcs (*frames*) de mida fixa i els processos en **pàgines** de la
  mateixa mida. Una **taula de pàgines** relaciona cada pàgina lògica amb el marc físic on és; els marcs no
  cal que siguin contigus. Elimina la fragmentació externa.
- **Segmentació:** la memòria es veu com un conjunt de **segments** de mida variable (codi, dades, pila…), més
  propers a l'estructura lògica del programa. Pot patir fragmentació externa. Sovint es combina amb paginació
  (**segmentació paginada**).
- **Intercanvi (*swapping*):** un procés (o part) que no s'està executant es trasllada a una **zona d'intercanvi**
  del disc (**partició swap** a Linux; **fitxer de paginació** `pagefile.sys` a Windows) per alliberar RAM;
  torna quan cal (*swap-in* / *swap-out*).

## 5.5. Memòria virtual

Tècnica que permet que el programari faci servir **més memòria de la que hi ha físicament**, usant el disc com
a extensió de la RAM.

- Només es manté a la RAM la part del procés que s'està fent servir; la resta queda al disc.
- Quan la CPU necessita una pàgina que no és a la RAM es produeix un **fallo de pàgina (*page fault*)**: el SO
  la porta del disc a un marc lliure (i, si cal, en treu una altra segons un algorisme de reemplaçament: LRU,
  FIFO, rellotge…).
- **Avantatge:** es poden executar programes més grans que la RAM i tenir més processos actius.
- **Inconvenient:** si es passa RAM (**hipepaginació / *thrashing***), el sistema es dedica gairebé només a
  moure pàgines entre disc i RAM i s'alenteix moltíssim. La solució real és **afegir RAM**.

### Configuració pràctica

| SO | Zona d'intercanvi | Configuració |
|---|---|---|
| **Windows** | `pagefile.sys` (fitxer de paginació) | *Propietats del sistema → Opcions avançades → Rendiment → Configuració → Opcions avançades → Memòria virtual*. Per defecte, gestionat automàticament. |
| **Linux** | Partició `swap` o fitxer `/swapfile` | `swapon --show`, `free -h`, `/etc/fstab`; `vm.swappiness` regula la tendència a intercanviar |

> Recomanació clàssica de mida de swap a Linux: entre 1× i 2× la RAM en equips amb poca RAM; en equips amb
> molta RAM, prou per a la **hibernació** (≈ mida de la RAM) o fins i tot sense swap dedicat.

## 5.6. Tipus de programes segons la seva ubicació en memòria

| Tipus | Característica |
|---|---|
| **Reubicables** | Poden canviar de posició a la RAM mentre s'executen |
| **Reentrants** | Si no s'executen, alliberen memòria per a altres processos (gestió amb memòria virtual) |
| **Residents** | Un cop carregats, romanen a la RAM fins que s'apaga l'equip (antivirus, monitors) |
| **Reutilitzables** | Un mateix codi en memòria serveix diversos usuaris alhora (biblioteques compartides) |

## 5.7. Optimització de la memòria (relació amb RA4)

- Tancar aplicacions i serveis innecessaris; revisar programes que s'inicien amb la sessió.
- Vigilar processos amb consum de RAM anòmal (fuites de memòria) amb el
  [monitor del sistema / `top` / `free`](../04-administracio-del-so/05-monitoratge-rendiment-i-registres.md).
- Ajustar la memòria virtual (mida i disc on es col·loca; millor en un disc/SSD ràpid diferent del del sistema).
- Afegir RAM: és la millora més efectiva quan hi ha *thrashing*.

## 5.8. Resum

- La RAM és limitada i volàtil; el SO l'assigna, la protegeix i la comparteix entre processos.
- **Mode protegit** = cada procés té el seu espai aïllat (tots els SO actuals).
- **Paginació** (blocs fixos) i **segmentació** (blocs variables) permeten memòria no contigua.
- La **memòria virtual** usa el disc com a extensió de la RAM; abusar-ne provoca *thrashing*.

## Comprova què has après

1. Diferència entre adreça lògica i adreça física. Qui fa la traducció?
2. Fragmentació interna i externa: en quina tècnica apareix cadascuna?
3. Què és un fallo de pàgina i què fa el SO quan es produeix?
4. Per què l'ús excessiu de memòria virtual alenteix tant el sistema?
5. On es configura la memòria virtual a Windows i a Linux?

---

[⬅ Anterior: Processos](04-processos-i-planificacio.md) · [Següent: E/S i interfícies ➡](06-gestio-es-i-interficies.md)
