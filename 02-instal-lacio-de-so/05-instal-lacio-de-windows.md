[⬅ Anterior: Gestor d'arrencada](04-gestor-d-arrencada.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Instal·lació de Linux ➡](06-instal-lacio-de-linux.md)

# 5. Instal·lació de Windows

> Criteris d'avaluació RA2.5–RA2.6 i RA2.8 — *particions, sistema d'arxius, paràmetres bàsics, incidències.*
> Es descriu **Windows 10/11** (els llibres descriuen XP/7).

## 5.1. Preparació del suport

- Descarregar la **ISO oficial** des de microsoft.com o generar l'USB amb la **Media Creation Tool**.
- Crear l'USB d'arrencada amb la Media Creation Tool o amb **Rufus** (tria l'esquema **GPT/UEFI** en equips
  moderns; MBR/BIOS només en maquinari antic).
- Verificar la integritat de la ISO (suma SHA-256).
- A la UEFI: activar **TPM 2.0** i **Secure Boot** (obligatoris per a Windows 11), mode SATA en **AHCI**, i
  posar l'USB primer a l'ordre d'arrencada (o menú `F12`).

## 5.2. Passos de l'assistent (*Windows Setup*)

1. Arrencada des de l'USB → «Prem qualsevol tecla per arrencar des de…».
2. **Idioma, format d'hora i moneda, teclat** → *Següent* → **Instal·la ara**.
3. **Clau de producte:** introduir-la o triar «No tinc clau de producte» (s'activa després amb un compte o una
   llicència digital).
4. **Edició** (Home / Pro / Education) — ha de coincidir amb la llicència.
5. **Termes de la llicència** → acceptar.
6. **Tipus d'instal·lació:**
   - **Actualització:** conserva fitxers, configuració i aplicacions (només si s'executa des d'un Windows en marxa).
   - **Personalitzada (avançada):** instal·lació **neta**. És l'opció per a un equip nou.
7. **Selecció i preparació del disc:**
   - Amb un disc buit: seleccionar l'espai no assignat → *Següent*; Windows crea automàticament **ESP + MSR +
     partició de Windows (C:) + partició de recuperació**.
   - Amb *Opcions de la unitat*: **Nou** (crear), **Eliminar**, **Formatar**, **Ampliar**. En crear la primera
     partició, Windows pot afegir una partició de sistema de ~100–500 MB.
   - El sistema d'arxius de la partició de Windows és sempre **NTFS**; es formata automàticament la partició
     destí (no cal formatar-la manualment).
8. **Còpia de fitxers i reinicis** automàtics (treure l'USB quan reinicia per no tornar a l'instal·lador).
9. **OOBE (*Out-Of-Box Experience*):**
   - Regió i teclat.
   - **Xarxa:** Windows 11 Home demana connexió i **compte Microsoft**; Pro permet **compte local**
     (a l'OOBE: opció «Opcions d'inici de sessió» → «Compte fora de línia», o `Maj+F10` → `start ms-cxh:localonly`).
   - **Nom d'usuari** i **contrasenya** (i preguntes de seguretat o PIN).
   - Opcions de **privadesa** (ubicació, diagnòstics, publicitat…).
   - Serveis opcionals (OneDrive, còpia de configuració).
10. Arrencada a l'escriptori.

## 5.3. Configuració post-instal·lació

| Tasca | On |
|---|---|
| **Windows Update** | *Configuració → Windows Update* → instal·lar tots els pedaços |
| **Controladors** | Windows Update sol posar-los; si falta algun (triangle groc a `devmgmt.msc`), instal·lar-lo des del web del fabricant |
| **Nom de l'equip** | *Configuració → Sistema → Aprofundir* → Canvia el nom |
| **Activació** | *Configuració → Sistema → Activació* |
| **Comptes d'usuari** | *Configuració → Comptes* o `lusrmgr.msc` (Pro) → [RA4](../04-administracio-del-so/01-usuaris-grups-i-contrasenyes.md) |
| **Particions de dades (D:)** | `diskmgmt.msc` → crear/formatar volum NTFS |
| **Aplicacions bàsiques** | Navegador, ofimàtica (LibreOffice/M365), compressor (7-Zip), lector PDF, antivirus (o Microsoft Defender), `winget` per instal·lar per línia d'ordres |
| **Punt de restauració** | *Crea un punt de restauració* → activar la protecció del sistema |

## 5.4. Instal·lació desatesa / per imatge (visió general)

- **`autounattend.xml`:** fitxer de respostes a l'arrel de l'USB; l'assistent el llegeix i no fa preguntes.
  Es genera amb **Windows System Image Manager (WSIM)** de l'ADK o amb generadors web.
- **Sysprep + DISM:** preparar un equip patró amb `sysprep /generalize /oobe`, capturar la imatge amb
  `dism /capture-image` i desplegar-la amb `dism /apply-image` o eines com **MDT** i **Configuration Manager**.
- **Clonezilla:** clonat de disc a disc o a imatge per a aules.

## 5.5. Incidències freqüents

| Símptoma | Solució |
|---|---|
| «Aquest PC no pot executar Windows 11» | Activar TPM 2.0 i Secure Boot a la UEFI; comprovar el model de CPU |
| «No s'ha pogut crear una partició nova» / no veu el disc | Mode SATA a AHCI; desconnectar altres discos/USB; netejar el disc amb `diskpart` → `clean` |
| «Windows no es pot instal·lar en aquest disc (taula de particions MBR/GPT)» | Arrencar l'USB en el mode correcte (UEFI) i convertir el disc a GPT (`mbr2gpt` o `diskpart` → `convert gpt`) |
| Bucle de reinicis a l'OOBE | Desconnectar la xarxa; provar un altre USB/ISO |
| Falta la Wi-Fi després d'instal·lar | Connectar per cable, executar Windows Update, o instal·lar el driver des d'un altre equip |

## 5.6. Resum

- Suport oficial + Rufus/Media Creation Tool; UEFI amb **TPM + Secure Boot** per a Windows 11.
- Assistent: idioma → clau → edició → llicència → **instal·lació personalitzada** → preparar disc (NTFS
  automàtic) → còpia → **OOBE** (compte, xarxa, privadesa).
- Després: **Windows Update**, controladors, nom d'equip, activació, comptes, aplicacions, punt de restauració.
- Desatès amb `autounattend.xml`; desplegament amb Sysprep + DISM / MDT / Clonezilla.

## Comprova què has après

1. Quina opció de l'assistent fa una instal·lació neta?
2. Quin sistema d'arxius rep la partició de Windows i cal formatar-la manualment?
3. Com pots crear un compte **local** a Windows 11 durant l'OOBE?
4. Quines dues opcions de la UEFI cal activar per instal·lar Windows 11?
5. Per a què serveix el fitxer `autounattend.xml`?

---

[⬅ Anterior: Gestor d'arrencada](04-gestor-d-arrencada.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Instal·lació de Linux ➡](06-instal-lacio-de-linux.md)
