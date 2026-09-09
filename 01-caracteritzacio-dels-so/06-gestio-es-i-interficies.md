[⬅ Anterior: Gestió de la memòria](05-gestio-de-memoria.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Sistema d'arxius ➡](07-sistemes-d-arxius-conceptes.md)

# 6. Gestió d'entrada/sortida i interfícies d'usuari

> Criteri d'avaluació RA1.1 — *Elements funcionals d'un sistema informàtic.*
> Es continua a [RA3 · interfícies i preferències](../03-configuracio-basica/02-interficies-d-usuari-i-preferencies.md).

## 6.1. Gestió d'entrada/sortida

Una de les funcions principals del SO és comunicar la CPU i la memòria amb els **perifèrics** i els suports
d'emmagatzematge. El SO envia ordres, decideix quin dispositiu necessita atenció, gestiona les **interrupcions**
i tracta els errors.

- La comunicació física passa pel **joc de xips (*chipset*)** de la placa base i, si cal, per una **targeta
  controladora** intermèdia.
- Cada perifèric té una part **mecànica** i una part **electrònica** (controladora/adaptador).
- Perquè el SO reconegui un perifèric i el faci servir correctament necessita el **controlador (*driver*)**
  adequat, que subministra el fabricant. Un mateix perifèric necessita un driver diferent per a cada SO.

### Classificació dels perifèrics

**Per la direcció de la informació:**

| Tipus | Descripció | Exemples |
|---|---|---|
| **D'entrada** | Porten informació cap a la memòria | Teclat, ratolí, escàner, micròfon, càmera, lector òptic |
| **De sortida** | Trauen informació de la memòria cap a l'exterior | Monitor, impressora, altaveus, *plotter* |
| **D'entrada/sortida** | Fan les dues coses | Disc dur, SSD, memòria USB, pantalla tàctil, mòdem, encaminador, targeta de xarxa, multifunció |

> **Perifèric ≠ suport.** El perifèric és el dispositiu (unitat lectora); el **suport** és el mitjà on es
> guarda la informació (DVD, memòria USB, plats del disc). El suport és reutilitzable, no volàtil i més barat
> que la RAM.

**Per la manera de tractar la informació:**

- **De bloc:** transfereixen blocs de mida fixa (discos, SSD).
- **De caràcter:** transfereixen caràcters d'un en un, sense ordre concret (teclat, ports sèrie, terminal).

**Per la forma de transmissió:**

- **Sèrie** (bit a bit, per exemple USB) o **paral·lel** (diversos bits alhora, en desús per a perifèrics).
- **Símplex** (un sol sentit), **semidúplex / *half-duplex*** (dos sentits, no alhora), **dúplex / *full-duplex***
  (dos sentits simultanis).

### Tècniques d'E/S

- **E/S programada / per sondeig (*polling*):** la CPU pregunta contínuament si el dispositiu està llest. Simple
  però malgasta CPU.
- **E/S per interrupcions:** el dispositiu avisa la CPU quan té dades a punt; la CPU atén la interrupció i
  continua amb altra feina mentrestant.
- **Accés directe a memòria (DMA):** un controlador transfereix dades entre el dispositiu i la RAM sense passar
  per la CPU; avisa la CPU en acabar. És el mètode dels discos i targetes de xarxa moderns.
- **Memòria intermèdia (*buffering*)** i **memòria cau de disc**: el SO agrupa i reordena operacions per
  millorar el rendiment. Per això cal **expulsar amb seguretat** els dispositius extraïbles.
- **Cua d'impressió (*spooling*):** els treballs d'impressió es desen en disc i s'envien a la impressora en
  ordre (habitualment FIFO).

## 6.2. Interfícies d'usuari

La **interfície d'usuari** és el mitjà de comunicació entre la persona i l'ordinador a través del SO.

| Tipus | Característiques | Exemples |
|---|---|---|
| **CLI — interfície de línia d'ordres** (mode text / mode ordre) | L'usuari escriu ordres i el SO respon amb text. Ràpida, automatitzable (scripts), consumeix pocs recursos, ideal per a servidors i administració remota. Pantalla clàssica de text: 80 columnes × 25 files. | `cmd`, **PowerShell**, Windows Terminal; **Bash**, Zsh; consoles TTY de Linux |
| **GUI — interfície gràfica d'usuari** (mode gràfic) | Finestres, icones, menús i punter (WIMP). Fàcil d'aprendre, visual; necessita més recursos i, sovint, ratolí o pantalla tàctil. | Explorador de Windows, GNOME, KDE Plasma, macOS Aqua |
| **Mixta** | La majoria de SO actuals ofereixen totes dues; gairebé qualsevol acció de la GUI té equivalent per ordres. | Windows 11, Ubuntu Desktop |
| **NUI / veu / tàctil** | Interacció natural: gestos, veu, moviment. | Assistents de veu, pantalles tàctils |

### L'intèrpret d'ordres (*shell*)

- És el programa que llegeix les ordres de l'usuari, les interpreta i executa els programes corresponents.
- **Windows:** `cmd.exe` (llegat, hereu de `COMMAND.COM`) i **PowerShell** (orientat a objectes, actual).
- **Linux:** diverses *shells* — `sh` (Bourne), `bash` (Bourne Again SHell, la més habitual), `zsh`, `csh`,
  `ksh`. El símbol del sistema típic de Bash és `usuari@equip:~$` (`$` usuari normal, `#` root).
- Sintaxi general d'una ordre: `ordre [opcions/modificadors] [arguments]`, per exemple `ls -la /home`.

## 6.3. Resum

- El SO gestiona l'E/S amb ordres, interrupcions i DMA, i necessita **controladors** per a cada perifèric i SO.
- Perifèrics: d'entrada / de sortida / d'E/S; de bloc / de caràcter. El **suport** no és el perifèric.
- Interfícies: **CLI** (ràpida, automatitzable) i **GUI** (fàcil, visual); els SO actuals tenen totes dues.
- La *shell* és l'intèrpret d'ordres: `bash` a Linux, `cmd`/PowerShell a Windows.

## Comprova què has après

1. Classifica: teclat, impressora, SSD, pantalla tàctil → entrada, sortida o E/S?
2. Diferència entre E/S per interrupcions i DMA.
3. Per què cal «expulsar amb seguretat» una memòria USB?
4. Dona dos avantatges de la CLI sobre la GUI per administrar un servidor.
5. Quin és el símbol del sistema de Bash per a un usuari normal i per a root?

---

[⬅ Anterior: Gestió de la memòria](05-gestio-de-memoria.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Sistema d'arxius ➡](07-sistemes-d-arxius-conceptes.md)
