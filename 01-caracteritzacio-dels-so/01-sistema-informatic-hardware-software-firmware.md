[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **1. El sistema informàtic: maquinari, programari i microprogramari**

[⬅ Índex del bloc](00-index.md) · [Següent: Representació de la informació ➡](02-representacio-de-la-informacio.md)

# 1. El sistema informàtic: maquinari, programari i microprogramari

> Criteri d'avaluació RA1.1 — *Identifica i descriu els elements funcionals d'un sistema informàtic.*

## 1.1. Què és un sistema informàtic

Un **ordinador** és una màquina composta d'elements físics, majoritàriament electrònics, capaç de fer una gran
varietat de treballs a gran velocitat i amb gran precisió. Aquests components electrònics, per si sols, no fan
res útil: necessiten un conjunt d'ordres o instruccions que els posin en funcionament.

Un **sistema informàtic** és el conjunt d'elements que permeten emmagatzemar, processar i transmetre informació:

- **Maquinari (*hardware*):** part física i tangible (processador, memòria, discos, perifèrics, plaques, cables).
- **Programari (*software*):** part lògica i intangible (conjunts d'instruccions i dades: sistema operatiu,
  aplicacions, controladors).
- **Microprogramari (*firmware*):** programari gravat de manera semipermanent dins de components de maquinari.
- **Persones (*peopleware*)** i **dades**: qui fa servir el sistema i la informació que s'hi processa.

<img width="471" height="270" alt="image" src="https://github.com/user-attachments/assets/0e685f1f-73f2-4106-82de-faa10d9ea3a0" />

## 1.2. Programa, aplicació i dades

- **Instrucció:** ordre elemental que el processador pot executar.
- **Programa:** conjunt d'instruccions ordenades i agrupades per fer una tasca concreta.
- **Aplicació informàtica:** conjunt de diversos programes interrelacionats que cooperen per resoldre una
  necessitat de l'usuari (per exemple, una suite ofimàtica o un ERP).
- **Dades:** la informació que es processa (textos, imatges, àudio, taules…). Es classifiquen segons el moment
  del tractament (**d'entrada**, **intermèdies**, **de sortida**) i segons si canvien durant el procés
  (**constants** o **variables**).

El **tractament automàtic de la informació** segueix sempre tres fases: **entrada → procés → sortida** (model
d'E/P/S de Babbage).

## 1.3. Classificació del programari

| Tipus | Descripció | Exemples |
|---|---|---|
| **Programari de base (de sistema)** | Fa funcionar l'ordinador i gestiona els recursos. Sense ell, res no s'executa. | Sistema operatiu, controladors, utilitats del sistema |
| **Programari d'aplicació** | Processa informació de manera personalitzada per a l'usuari. | Navegador, ofimàtica, edició d'imatge, jocs |
| **Programari de desenvolupament** | Serveix per crear altre programari. | Compiladors, entorns de desenvolupament, depuradors |

El programari d'aplicació pot ser **estàndard** (comercial, amb característiques predeterminades) o **a mida**
(desenvolupat per a les necessitats concretes d'un client).

> El **sistema operatiu** és el component de programari de base que fa que els programes puguin processar
> informació sobre els components de maquinari. Es desenvolupa en detall al
> [tema 3](03-concepte-funcions-i-estructura-del-so.md).

## 1.4. Components funcionals del maquinari

<img width="1200" height="1200" alt="image" src="https://github.com/user-attachments/assets/682452f3-96e4-4b16-b932-d1268efe6a24" />

Model de Von Neumann. Un ordinador s'organitza en aquests blocs interconnectats pels **busos del sistema**:

1. **Unitat central de procés (UCP / CPU / processador).** Controla i executa les operacions. Es compon de:
   - **Unitat de control (UC):** cerca, interpreta i seqüencia les instruccions; genera les senyals de control.
     Conté registres com el *registre d'instrucció*, el *comptador de programa* i el *rellotge*.
   - **Unitat aritmeticològica (UAL / ALU):** fa les operacions aritmètiques i lògiques (aquestes darreres amb
     els operadors de l'àlgebra de Boole). Conté els *registres d'entrada*, l'*acumulador* i el *registre d'estat*.
2. **Memòria central (MC) o RAM.** Emmagatzema temporalment els programes i dades en execució. És **volàtil**
   (es perd en tallar el corrent).
3. **Controladors.** Circuits intermediaris entre la CPU i cada dispositiu.
4. **Unitat d'entrada/sortida.** Comunica els components interns amb els perifèrics.
5. **Busos.** Vies compartides de comunicació: de **dades**, d'**adreces** i de **control**. L'amplada del bus
   (bits en paral·lel) i la seva freqüència (MHz) determinen el rendiment.
6. **Perifèrics (unitats perifèriques d'E/S).** Vegeu el [tema 6](06-gestio-es-i-interficies.md).

### Tipus de memòria

| Memòria | Volàtil | Es pot modificar | Ús |
|---|---|---|---|
| **RAM** (DRAM, SRAM, SDRAM, DDR…) | Sí | Sí | Memòria principal de treball |
| **ROM / PROM / EPROM / EEPROM / Flash** | No | No (o amb procediment especial) | BIOS/UEFI, microprogramari |
| **Memòria cau (*cache*)** L1/L2/L3 | Sí | Sí | Intermèdia d'alta velocitat entre CPU i RAM |
| **CMOS** (alimentada per pila) | Amb pila | Sí | Configuració de la BIOS, rellotge |
| **VRAM / memòria de la GPU** | Sí | Sí | Imatge que es mostra a la pantalla |

> Un **suport d'emmagatzematge** (disc dur, SSD, memòria USB, DVD) **no és** memòria interna: és memòria
> auxiliar o externa, **no volàtil**, més lenta que la RAM i pensada per guardar la informació de manera permanent.

## 1.5. El microprogramari (*firmware*)

És la part intangible (programari) que va gravada dins d'un component de maquinari, en una memòria de només
lectura o *flash*. Estableix la lògica de més baix nivell que controla els circuits electrònics d'un dispositiu.

- **BIOS / UEFI de la placa base:** inicialitza i comprova el maquinari en encendre (POST), guarda la
  configuració (ordre d'arrencada, hora, discos detectats) i lliura el control al gestor d'arrencada del disc.
  S'hi accedeix prement una tecla durant l'inici (`Supr`, `F2`, `F10`, `Esc`… segons el fabricant).
  **UEFI** és el substitut modern de la BIOS clàssica: interfície gràfica, *Secure Boot*, suport de discos
  grans amb GPT i arrencada més ràpida. Vegeu [RA2 · gestor d'arrencada](../02-instal-lacio-de-so/04-gestor-d-arrencada.md).
- Altres exemples: microprogramari de discos SSD, d'impressores, de targetes de xarxa, de mòbils.

## 1.6. Resum

- Maquinari = físic; programari = lògic; microprogramari = programari dins del maquinari.
- El programari es divideix en **de base** (SO i utilitats) i **d'aplicació**.
- La CPU (UC + UAL), la RAM, els controladors, la unitat d'E/S i els busos són els components funcionals bàsics.
- El SO és el programari de base imprescindible que gestiona tots aquests recursos.

## Comprova què has après

1. Diferència entre maquinari, programari i microprogramari amb un exemple de cada un.
2. Quines dues parts formen la UCP i de què s'encarrega cadascuna?
3. Per què la BIOS/UEFI es considera microprogramari i no simplement maquinari?
4. Un disc SSD, és memòria interna o suport d'emmagatzematge? Raona-ho.
5. Classifica: navegador web, controlador d'impressora, full de càlcul, nucli de Linux → base o aplicació?

---

[⬅ Índex del bloc](00-index.md) · [Següent: Representació de la informació ➡](02-representacio-de-la-informacio.md)
