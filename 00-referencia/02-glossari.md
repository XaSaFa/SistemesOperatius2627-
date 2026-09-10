[🏠 Inici](../README.md) › Referència › **Glossari**

[⬅ Currículum oficial](01-curriculum-oficial.md) · [🏠 Inici](../README.md) · [Fonts i bibliografia ➡](03-fonts-i-bibliografia.md)

# Glossari

Termes clau del mòdul. Entre parèntesis, el tema on s'expliquen amb detall.

## A
- **API (crida al sistema):** interfície de programació que el nucli ofereix a les aplicacions per demanar serveis (fitxers, memòria, processos). (RA1 · tema 03)
- **Arbre de directoris:** organització jeràrquica de carpetes i fitxers que penja d'un directori arrel. (RA1 · tema 07)
- **Atribut:** propietat associada a un fitxer o directori (només lectura, ocult, sistema, arxivat, comprimit…). A Windows es gestionen amb `attrib`; a Linux hi ha atributs estesos amb `chattr`. (RA1 · tema 08)
- **Arrencada dual (*dual boot*):** configuració amb dos o més sistemes operatius instal·lats i un gestor d'arrencada que permet triar-ne un en encendre. (RA2 · tema 04)

## B
- **BCP (bloc de control de procés):** estructura de dades que el SO manté per cada procés (PID, estat, prioritat, ubicació en memòria, recursos oberts). (RA1 · tema 04)
- **BIOS/UEFI:** microprogramari de la placa base que inicialitza el maquinari i lliura el control al gestor d'arrencada. UEFI és el substitut modern de la BIOS. (RA1 · tema 01 · RA2 · tema 04)
- **Boot (sector d'arrencada):** primer sector d'un volum amb el codi que carrega el sistema operatiu. (RA2 · tema 02)

## C
- **Clúster (unitat d'assignació):** grup de sectors consecutius; és la unitat mínima d'espai que el SO assigna a un fitxer. (RA1 · tema 07)
- **Codi ASCII / Unicode (UTF-8):** taules d'equivalència entre caràcters i combinacions de bits. (RA1 · tema 02)
- **Compilació per capes / microprogramari:** vegeu *firmware*.
- **Controlador (*driver*):** programari que permet al SO comunicar-se amb un dispositiu concret. (RA1 · tema 06)
- **`cron` / `crontab`:** planificador de tasques periòdiques de Linux. (RA3 · tema 04)

## D
- **Dimoni (*daemon*):** procés de Linux que s'executa en segon pla i dona un servei (impressió, xarxa…). Equival a un *service* de Windows. (RA4 · tema 04)
- **Directori actiu / de treball:** carpeta on el SO o l'usuari té el «control» en un moment donat; punt de partida de les rutes relatives. (RA1 · tema 07)

## F
- **FAT / exFAT / NTFS / ext4 / Btrfs / APFS:** sistemes d'arxius. FAT i exFAT són molt compatibles però sense permisos; NTFS i ext4 tenen registre de transaccions (*journaling*) i permisos. (RA1 · tema 09)
- **Firmware (microprogramari):** programari gravat en memòria no volàtil d'un component de maquinari (BIOS/UEFI, controladores…). (RA1 · tema 01)
- **Fil (*thread*, fil d'execució, bri):** unitat d'execució dins d'un procés; els fils d'un mateix procés comparteixen memòria. (RA1 · tema 04)
- **Fragmentació:** externa (espais lliures petits i dispersos) o interna (espai desaprofitat dins d'una unitat assignada). (RA1 · tema 05)

## G
- **GPT (GUID Partition Table):** esquema de particionat modern, associat a UEFI; substitueix l'MBR i permet més de 4 particions primàries i discos > 2 TB. (RA2 · tema 02)
- **GRUB:** gestor d'arrencada habitual a GNU/Linux. (RA2 · tema 04)
- **Grup:** entitat administrativa que agrupa usuaris per assignar-los permisos de manera col·lectiva. (RA4 · tema 01)

## I
- **Interfície d'usuari:** mitjà de comunicació persona-màquina. **CLI** (línia d'ordres) i **GUI** (gràfica). (RA1 · tema 06 · RA3 · tema 02)
- **`init` / `systemd`:** primer procés de l'espai d'usuari a Linux (PID 1); `systemd` és l'implementació actual i gestiona serveis i objectius (*targets*). (RA3 · tema 01 · RA4 · tema 04)

## K
- **Kernel (nucli):** part central del SO que s'executa en mode privilegiat i gestiona CPU, memòria i dispositius. (RA1 · tema 03)

## M
- **MBR (Master Boot Record):** primer sector d'un disc amb estil de partició clàssic; conté el codi d'arrencada i la taula de 4 particions. (RA2 · tema 02 i 04)
- **Memòria virtual / intercanvi (*swap*, fitxer de paginació):** tècnica que fa servir el disc com a extensió de la RAM. (RA1 · tema 05)
- **Multitasca / multiusuari / multiprocessador:** criteris de classificació dels SO segons processos, usuaris i CPU simultanis. (RA1 · tema 10)

## P
- **Paginació / segmentació:** tècniques de gestió de memòria amb blocs de mida fixa (pàgines) o variable (segments). (RA1 · tema 05)
- **Partició:** divisió lògica d'un disc. Tipus (MBR): primària, estesa, unitat lògica. Partició **activa**: la que la BIOS llegeix per arrencar. (RA2 · tema 02)
- **Perfil d'usuari:** conjunt de carpetes i configuració personal (escriptori, aplicacions, preferències). Local o mòbil. (RA4 · tema 01)
- **Permís:** dret d'accés sobre un recurs (lectura, escriptura, execució…). A Linux: `rwx` per propietari/grup/altres. A NTFS: ACL. (RA1 · tema 08 · RA4 · tema 02)
- **PID / PPID:** identificador d'un procés i del seu procés pare. (RA1 · tema 04)
- **Planificador (*scheduler*):** component del SO que reparteix el temps de CPU entre processos (Round-Robin, FIFO, per prioritats…). (RA1 · tema 04)
- **Procés:** programa en execució, amb el seu espai de memòria, recursos i BCP. (RA1 · tema 04)

## Q
- **Quàntum:** interval de temps de CPU que el planificador assigna a cada procés en temps compartit. (RA1 · tema 04)

## R
- **Registre de Windows:** base de dades jeràrquica de configuració del SO, maquinari i aplicacions (`regedit`, *hives*). (RA4 · tema 05)
- **Ruta (*path*):** cadena que indica la ubicació d'un fitxer o directori. Absoluta (des de l'arrel) o relativa (des del directori actiu). (RA1 · tema 07)

## S
- **Sector:** unitat mínima de lectura/escriptura física d'un disc (512 B o 4 KiB). (RA1 · tema 07)
- **Servei:** vegeu *dimoni*. Programa en segon pla que el SO inicia, atura, pausa o reprèn. (RA4 · tema 04)
- **Sistema d'arxius (*file system*):** estructura lògica que organitza dades en fitxers i directoris dins d'un volum. (RA1 · tema 07)
- **Sistema transaccional / journaling:** garanteix que una operació sobre dades s'aplica completament o no s'aplica gens, cosa que evita corrupció davant talls. (RA1 · tema 09)
- **SO monolloc / en xarxa:** monolloc = pensat per a un únic lloc de treball aïllat; en xarxa = comparteix recursos i valida usuaris via xarxa. (RA1 · tema 10)

## U
- **UID / GID:** identificadors numèrics d'usuari i de grup a Linux. (RA4 · tema 01)
- **Unitat lògica (Windows):** lletra (`C:`, `D:`…) que representa un volum. (RA1 · tema 07)

## V
- **Virtualització:** abstracció dels recursos d'un ordinador per executar diversos sistemes operatius aïllats sobre el mateix maquinari. (RA5)
- **Volum:** partició formatada amb un sistema d'arxius i llesta per emmagatzemar dades. (RA2 · tema 02)

---

[⬅ Currículum oficial](01-curriculum-oficial.md) · [🏠 Inici](../README.md) · [Fonts i bibliografia ➡](03-fonts-i-bibliografia.md)
