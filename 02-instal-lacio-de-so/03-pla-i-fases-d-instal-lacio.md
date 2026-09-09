[⬅ Anterior: Particions](02-particions-i-estructura-del-disc.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Gestor d'arrencada ➡](04-gestor-d-arrencada.md)

# 3. El pla i les fases d'instal·lació

> Criteris d'avaluació RA2.4–RA2.6 i RA2.8 — *Selecciona el SO; elabora un pla d'instal·lació; configura
> paràmetres bàsics; descriu les incidències.*

## 3.1. Seleccionar el sistema operatiu

Criteris per triar el SO adequat:

- **Compatibilitat** amb el maquinari existent (i amb els drivers disponibles).
- **Aplicacions** que s'hi han d'executar (a vegades hi ha una aplicació crítica que només va en un SO).
- **Cost i llicència** (propietari vs. lliure; nombre de llicències necessàries).
- **Ús previst i perfil de l'usuari** (ofimàtica, disseny, servidor, aula…).
- **Manteniment i suport**: durada del suport (per exemple, Ubuntu **LTS** = 5 anys; Windows 10 fi de suport
  octubre de 2025), facilitat d'administració, política d'actualitzacions.
- **Perspectives de futur**: previsió de canvis a curt, mitjà i llarg termini.
- **Recursos disponibles** per dur a terme la instal·lació i el manteniment.

## 3.2. Les tres fases

### Fase 1 — Planificació

- Comprovar **compatibilitat** SO ↔ maquinari ↔ aplicacions ↔ drivers ([tema 1](01-requisits-i-compatibilitat.md)).
- Decidir l'**esquema de particions** i els **sistemes d'arxius** ([tema 2](02-particions-i-estructura-del-disc.md)).
- Triar les **aplicacions bàsiques** a instal·lar (paquet ofimàtic, navegador, antivirus, eines d'administració).
- Preveure la **solució de còpies de seguretat** i la **configuració de xarxa**.
- Preparar el **suport d'instal·lació** (USB/DVD) i verificar-ne la integritat.
- Fer **còpia de seguretat** de les dades si l'equip ja s'usava.

### Fase 2 — Instal·lació

1. Configurar la **BIOS/UEFI** per arrencar des del suport d'instal·lació (canvi temporal de l'ordre
   d'arrencada o menú *Boot* amb `F12`/`F9`).
2. Arrencar l'instal·lador i triar **idioma, teclat, zona horària**.
3. **Preparar el disc:** particionar i formatar (o deixar-ho a l'assistent).
4. **Copiar els fitxers** del SO i instal·lar-los.
5. Crear el **compte d'administrador** (nom d'usuari i contrasenya).
6. Assignar el **nom de l'equip**.
7. Seleccionar **components/paquets opcionals**.
8. Ajustar la **xarxa** (DHCP o IP fixa).
9. Configurar el **gestor d'arrencada** ([tema 4](04-gestor-d-arrencada.md)).
10. Aplicar les **actualitzacions de seguretat**.
11. Instal·lar els **controladors** dels dispositius no reconeguts.
12. Instal·lar les **aplicacions** i, si escau, els connectors del navegador.

### Fase 3 — Documentació

Deixar constància escrita de tot (imprescindible per a manteniment, ampliacions i pedaços posteriors):

| Camp | Exemple |
|---|---|
| Data i hora de la instal·lació | 2026-09-15, 10:30 |
| Especificacions de maquinari | CPU, RAM, disc, gràfica, xarxa |
| SO i versió | Windows 11 Pro 23H2 / Ubuntu 24.04.1 LTS |
| Nom de l'equip | `AULA1-PC07` |
| Esquema de particions i sistemes d'arxius | ESP 300 MB, C: NTFS 120 GB, D: NTFS resta |
| Compte d'administrador | `admin` (contrasenya en gestor de contrasenyes) |
| Clau de producte / llicència | (referència, no la clau en clar) |
| Programari addicional instal·lat | LibreOffice, Firefox, 7-Zip, antivirus X, VirtualBox |
| Configuració de xarxa | IP 192.168.1.107/24, gw 192.168.1.1, DNS 192.168.1.1 |
| **Incidències** durant el procés | «El driver de la Wi-Fi no es reconeix; instal·lat manualment des d'USB» |

## 3.3. Paràmetres bàsics que demana l'instal·lador

- Idioma del sistema, format de data/hora i moneda, **disposició del teclat**.
- **Zona horària**.
- **Partició/destí** de la instal·lació i sistema d'arxius.
- **Nom de l'equip**.
- **Compte d'usuari administrador** i contrasenya; opcions d'inici de sessió (PIN, biometria a Windows).
- Opcions de **privadesa i telemetria** (Windows), instal·lació de **còdecs i programari de tercers** (Ubuntu).
- **Xarxa** (Windows 11 Home força connexió i compte Microsoft; hi ha alternatives amb compte local).
- Selecció d'**instal·lació mínima o completa** (Ubuntu) / **edició** (Windows Home/Pro).

## 3.4. Mètodes d'instal·lació

| Mètode | Descripció | Ús |
|---|---|---|
| **Neta (des de zero)** | Es formata la partició i s'instal·la el SO nou. La més fiable. | Equip nou o canvi de SO |
| **Actualització (*in-place upgrade*)** | Se substitueix el SO conservant aplicacions, dades i configuració. | Windows 10 → 11; Ubuntu 22.04 → 24.04 (`do-release-upgrade`) |
| **Desatesa / automatitzada** | Un fitxer de respostes contesta l'assistent (Windows: `autounattend.xml`; Ubuntu: *autoinstall*/cloud-init; Kickstart a RHEL). | Desplegar molts equips iguals |
| **Per imatge / clonat** | Es copia una imatge d'un equip «patró» a la resta (`dism`, Clonezilla, MDT/SCCM). | Aules, empreses |
| **Per xarxa (PXE)** | L'equip arrenca l'instal·lador des d'un servidor. | Grans desplegaments |
| **Live** | Es prova el SO des del USB sense tocar el disc; opció d'instal·lar-lo. | Ubuntu i altres distribucions |

## 3.5. Incidències típiques i com actuar

| Incidència | Causa probable | Solució |
|---|---|---|
| L'equip no arrenca des de l'USB | Ordre d'arrencada, *Secure Boot*, USB mal gravat | Ajustar BIOS/UEFI; regravar amb Rufus/`dd`/Startup Disk Creator; desactivar *Secure Boot* si cal |
| «No s'ha trobat cap disc» | Mode SATA en RAID, driver NVMe/RAID absent | Canviar a **AHCI** a la BIOS; carregar el driver durant la instal·lació |
| No es pot instal·lar en la partició triada (GPT/MBR) | Barreja de mode UEFI i Legacy | Arrencar l'instal·lador en el mode correcte i usar l'esquema coherent |
| Falla la còpia de fitxers | Suport d'instal·lació corrupte, RAM defectuosa, disc amb sectors dolents | Verificar *checksum* de la ISO; `memtest86`; provar un altre disc |
| Wi-Fi / gràfica sense funcionar després d'instal·lar | Falten drivers | Connectar per cable, actualitzar, instal·lar *drivers* (Windows Update / *Controladors addicionals* d'Ubuntu) |
| Windows 11 no s'instal·la | Falta TPM 2.0 / Secure Boot / CPU no suportada | Activar TPM i Secure Boot a la UEFI; si el maquinari no ho permet, valorar Windows 10 o Linux |
| L'arrencada dual només mostra un SO | El gestor d'arrencada no ha detectat l'altre | Executar `os-prober` + `update-grub`; reparar amb `bootrec` / `bcdedit` ([tema 4](04-gestor-d-arrencada.md)) |

## 3.6. Resum

- Triar el SO segons **compatibilitat, aplicacions, cost, ús i suport**.
- Tres fases: **planificar → instal·lar → documentar**. Documentar **sempre** les incidències.
- Mètodes: neta, actualització, desatesa, per imatge, PXE, live.
- Preparar la BIOS/UEFI, verificar la ISO i tenir a mà els drivers (com a mínim el de xarxa).

## Comprova què has après

1. Enumera cinc criteris per triar un SO.
2. Ordena les passes de la fase d'instal·lació.
3. Per què és tan important la fase de documentació?
4. Diferència entre instal·lació neta i actualització *in-place*.
5. L'instal·lador diu «no s'ha trobat cap disc». Quines dues coses comproves primer?

---

[⬅ Anterior: Particions](02-particions-i-estructura-del-disc.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Gestor d'arrencada ➡](04-gestor-d-arrencada.md)
