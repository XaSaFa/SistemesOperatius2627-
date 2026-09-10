[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **3. Concepte, funcions i estructura del sistema operatiu**

[⬅ Anterior: Representació de la informació](02-representacio-de-la-informacio.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Processos ➡](04-processos-i-planificacio.md)

# 3. Concepte, funcions i estructura del sistema operatiu

> Criteris d'avaluació RA1.1 i RA2.1–RA2.2 — *Funcions i arquitectura del sistema operatiu.*

## 3.1. Definició

Un **sistema operatiu (SO)** és el conjunt de programes, serveis i funcions que gestionen i coordinen el
funcionament del maquinari i del programari, i que proporcionen la base per crear i executar les aplicacions.

Compleix dues funcions complementàries:

- **Màquina estesa (interfície):** amaga la complexitat del maquinari i ofereix a l'usuari i als programadors
  una visió senzilla i uniforme (fitxers, finestres, ordres) mitjançant **crides al sistema** i interfícies
  d'usuari. L'usuari no ha de saber en quina posició de memòria hi ha el seu document.
- **Gestor de recursos:** reparteix de manera ordenada, eficient i segura els recursos limitats de la màquina
  entre els programes i els usuaris que competeixen per ells.

## 3.2. Recursos que gestiona

| Recurs | Component del SO | Tasques |
|---|---|---|
| **Processador (CPU)** | Planificador / gestor de processos | Crear, planificar, sincronitzar i finalitzar processos; repartir temps de CPU |
| **Memòria principal** | Gestor de memòria | Assignar i alliberar memòria; memòria virtual, paginació, protecció entre processos |
| **Dispositius d'E/S** | Gestor d'E/S + controladors | Enviar ordres als perifèrics, gestionar interrupcions, cues (per exemple d'impressió) |
| **Informació** | Sistema d'arxius | Organitzar dades en fitxers i directoris; permisos, integritat, memòria cau de disc |

A més gestiona **usuaris i seguretat**, **xarxa** i el **control d'errors** de maquinari i programari.

## 3.3. Funcions principals

- Control i execució de programes (processos).
- Gestió i administració de la memòria.
- Gestió i administració de perifèrics i dispositius d'emmagatzematge.
- Gestió del sistema d'arxius.
- Gestió d'usuaris, sessions i seguretat (autenticació, permisos, xifratge).
- Comunicació amb l'usuari (interfície de text i gràfica).
- Detecció i tractament d'errors; registre d'activitat (*logs*).
- Serveis de xarxa i comunicació entre processos.

## 3.4. Estructura interna: el nucli i els modes d'execució

El processador té (com a mínim) dos **modes d'execució**:

- **Mode nucli / privilegiat / *kernel*:** accés total al maquinari i a totes les instruccions. Hi s'executa
  el **nucli** del SO.
- **Mode usuari:** accés restringit. Hi s'executen les aplicacions. Si una aplicació necessita un servei del
  SO (obrir un fitxer, reservar memòria), fa una **crida al sistema**, que provoca un canvi controlat a mode nucli.

Aquesta separació dona **estabilitat i seguretat**: un error o codi maliciós en una aplicació no pot corrompre
directament el nucli ni la memòria d'altres processos.

### Models d'arquitectura

| Arquitectura | Idea | Exemples |
|---|---|---|
| **Monolítica** | Tot el SO és un únic bloc en mode nucli. Ràpida però difícil de mantenir. Els primers SO eren gairebé impossibles de modificar sense redissenyar-los. | UNIX clàssic, MS-DOS |
| **Monolítica modular** | Nucli monolític però amb **mòduls** carregables (controladors, sistemes d'arxius). | Linux, Windows NT (híbrid) |
| **Per capes** | El SO s'organitza en nivells; cada capa només es comunica amb la immediatament superior i inferior. | THE, MULTICS |
| **Micronucli (*microkernel*)** | Al nucli només hi ha el mínim (planificació, memòria, comunicació entre processos); la resta són serveis en mode usuari. Molt robust, però amb sobrecàrrega de comunicació. | MINIX 3, QNX, GNU Hurd |
| **Màquina virtual** | El nucli emula maquinari perquè cada procés o cada SO convidat s'executi en un entorn aïllat. Base de la [virtualització](../05-maquines-virtuals/00-index.md). | z/VM, hipervisors moderns |

### Nivells clàssics d'un SO (model didàctic de 4 capes)

| Nivell | Funció |
|---|---|
| **Nucli** | Gestiona quins processos arriben a la CPU per ser executats |
| **Executiu** | Administra la memòria per emmagatzemar els processos en pàgines |
| **Supervisor** | Comunica cada procés entre el sistema i l'usuari |
| **Usuari** | Mostra a l'usuari el procés en execució o el que es vol executar |

## 3.5. Serveis i interfícies

- Un **servei** (Windows) o **dimoni** (*daemon*, Linux) és una aplicació que s'executa en segon pla i ofereix
  funcionalitat (impressió, xarxa, bases de dades, servidor web). Molts s'instal·len amb el SO; altres els
  afegeixen les aplicacions. Vegeu [RA4 · serveis](../04-administracio-del-so/04-serveis-del-sistema.md).
- Les **interfícies** connecten els nivells: crides al sistema (aplicació ↔ nucli), interfície d'usuari
  (persona ↔ SO) i controladors (SO ↔ maquinari). Vegeu el [tema 6](06-gestio-es-i-interficies.md).

## 3.6. Evolució històrica (resum)

| Generació | Període | Maquinari | SO / mode d'explotació |
|---|---|---|---|
| 1a | 1945–1955 | Vàlvules de buit | Sense SO; programació en llenguatge màquina |
| 2a | 1955–1965 | Transistors | **Processament per lots** (*batch*); monitors residents |
| 3a | 1965–1980 | Circuits integrats | Multiprogramació, temps compartit, primers SO multiusuari |
| 4a | 1980–avui | Microprocessadors, PC | SO amb GUI, multitasca, xarxa, virtualització, mòbils i núvol |

Maquinari i SO evolucionen **conjuntament**: cada generació de maquinari fa possibles SO més potents, i les
necessitats dels SO empenyen el maquinari.

## 3.7. Resum

- El SO és **màquina estesa** (amaga complexitat) i **gestor de recursos** (reparteix CPU, memòria, E/S i fitxers).
- El **nucli** s'executa en mode privilegiat; les aplicacions, en mode usuari, i demanen serveis via **crides al sistema**.
- Arquitectures: monolítica (modular), per capes, micronucli i de màquina virtual.

## Comprova què has après

1. Explica les dues funcions bàsiques del SO amb un exemple de cadascuna.
2. Quins quatre recursos gestiona el SO i quin component se n'ocupa?
3. Què és una crida al sistema i per què provoca un canvi de mode?
4. Diferència entre nucli monolític i micronucli. Avantatges i inconvenients.
5. Relaciona cada nivell del model de 4 capes amb la seva funció.

---

[⬅ Anterior: Representació de la informació](02-representacio-de-la-informacio.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Processos ➡](04-processos-i-planificacio.md)
