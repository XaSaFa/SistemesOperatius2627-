[⬅ Anterior: Instal·lació de Linux](06-instal-lacio-de-linux.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Configuració ➡](../03-configuracio-basica/00-index.md)

# 7. Llicències, actualització i incidències

> Criteris d'avaluació RA2.8–RA2.10 — *Descriu les incidències; respecta les normes d'utilització del
> programari (llicències); actualitza el sistema operatiu.*

## 7.1. Tipus de llicència de programari

| Llicència | Es pot usar | Codi font | Modificar / redistribuir | Cost | Exemples |
|---|---|---|---|---|---|
| **Propietària / comercial** | Segons EULA (per equip, per usuari, subscripció) | Tancat | No | De pagament | Windows, macOS, Microsoft 365, Adobe |
| **Programari lliure (GPL, LGPL, AGPL)** | Sí | Obert | **Sí**, mantenint la mateixa llicència (*copyleft*) | Gratuït (es pot cobrar per suport) | GNU/Linux, LibreOffice, GIMP |
| **Codi obert permissiu (MIT, BSD, Apache)** | Sí | Obert | Sí, fins i tot en productes tancats | Gratuït | FreeBSD, VLC (parts), moltes biblioteques |
| **Freeware** | Sí, gratis | Tancat | No | Gratuït | Alguns visors i utilitats |
| **Shareware / trial** | Prova limitada (temps o funcions) | Tancat | No | Pagament per continuar | Antivirus de prova, WinRAR |
| **Programari de domini públic** | Sí, sense restriccions | Sovint obert | Sí | Gratuït | SQLite, alguns fonts |
| **OEM** | Lligada a l'equip on ve preinstal·lada | Tancat | No | Inclosa en el maquinari | Windows preinstal·lat |
| **Volum / educativa (Campus, Academic)** | Molts equips d'una organització | Tancat | No | Contracte | Windows/Office per a centres |

Bones pràctiques:

- Llegir i respectar l'**EULA** (acord de llicència d'usuari final).
- Portar un **inventari de llicències** (clau, tipus, nombre de llocs, data de compra).
- No instal·lar més còpies de les llicenciades; el programari lliure evita aquest problema en entorns educatius.
- Documentar la llicència a la fitxa d'instal·lació ([tema 3](03-pla-i-fases-d-instal-lacio.md)).

## 7.2. Activació

- **Windows:** clau de producte (25 caràcters) o **llicència digital** lligada al maquinari i/o al compte
  Microsoft. Estat a *Configuració → Sistema → Activació*. Eina CLI: `slmgr`.
- **Linux:** no requereix activació (llicència lliure). Les subscripcions (RHEL, Ubuntu Pro) donen accés a
  suport i pedaços estesos, no «desbloquegen» el SO.

## 7.3. Actualització del sistema operatiu

### Per què

- Tancar **vulnerabilitats de seguretat** (motiu principal).
- Corregir errors i millorar l'estabilitat i el rendiment.
- Suport de maquinari i formats nous.

### Tipus

| Terme | Significat |
|---|---|
| **Pedaç / actualització de seguretat** | Correcció puntual d'una vulnerabilitat |
| **Actualització acumulativa** | Conjunt de correccions (Windows: *cumulative update* mensual, «Patch Tuesday») |
| **Actualització de característiques** | Nova versió del mateix SO (Windows 22H2 → 23H2; Ubuntu 22.04 → 24.04) |
| **Actualització (*upgrade*) major** | Canvi de versió principal amb possible reinstal·lació |

### Windows

- *Configuració → Windows Update* → *Cerca actualitzacions*.
- **Hores actives** i **pausar actualitzacions** per no reiniciar en mal moment.
- Historial i **desinstal·lar actualitzacions** si una causa problemes.
- CLI: `wsl`-independent → `UsoClient`, PowerShell amb el mòdul `PSWindowsUpdate`; empreses: **WSUS** /
  **Windows Update for Business** / Intune.
- Comprovar la integritat del sistema: `sfc /scannow`, `DISM /Online /Cleanup-Image /RestoreHealth`.

### Linux (Debian/Ubuntu)

```bash
sudo apt update            # refresca la llista de paquets
sudo apt upgrade           # actualitza sense treure paquets
sudo apt full-upgrade      # actualitza encara que hagi de treure'n algun
sudo apt autoremove        # neteja paquets orfes
sudo do-release-upgrade    # salta a la següent versió d'Ubuntu
```

- **Actualitzacions automàtiques de seguretat:** paquet `unattended-upgrades`.
- Fedora/RHEL: `sudo dnf upgrade`; openSUSE: `sudo zypper update`.
- Actualització del **microprogramari** (BIOS/UEFI, SSD): `fwupdmgr refresh && fwupdmgr update`.

### Bones pràctiques d'actualització

- **Còpia de seguretat / punt de restauració / instantània** abans d'una actualització important.
- Provar primer en un equip pilot abans de desplegar a tota l'aula.
- Planificar finestres de manteniment (fora d'hores de classe/producció).
- Revisar l'espai lliure en disc abans d'una actualització de característiques.

## 7.4. Incidències de la instal·lació i l'actualització (recull)

| Incidència | Causa | Actuació |
|---|---|---|
| L'actualització falla amb codi d'error | Espai insuficient, components corruptes, driver incompatible | Alliberar espai; `sfc`/`DISM` (Windows) o `sudo apt --fix-broken install` (Linux); actualitzar drivers |
| Bucle de reinicis després d'una actualització | Actualització defectuosa | *Opcions d'inici avançades → Desinstal·la l'última actualització*; a Linux, triar un nucli anterior a GRUB |
| Aplicació deixa de funcionar després d'actualitzar | Incompatibilitat de versió | Revertir el pedaç, contactar amb el fabricant, esperar una correcció |
| Wi-Fi/gràfica sense funcionar després d'instal·lar | Falten drivers | Instal·lar-los (Windows Update / *Controladors addicionals* / `ubuntu-drivers`) |
| Activació de Windows fallida | Clau incorrecta o canvi de maquinari | Solucionador d'activació; vincular la llicència digital al compte Microsoft |
| «Sense connexió» durant la instal·lació | Falta driver de xarxa o cable | Usar cable; instal·lar el driver de xarxa des d'un altre equip |

> Documenta **totes** les incidències i la solució aplicada a la fitxa de l'equip.

## 7.5. Resum

- Llicències: **propietària** (EULA, de pagament), **lliure/copyleft** (GPL), **permissiva** (MIT/BSD),
  freeware, shareware, OEM, volum. Cal respectar-les i inventariar-les.
- Windows s'activa amb clau o llicència digital; Linux no necessita activació.
- **Actualitzar sempre** (seguretat): Windows Update / `apt full-upgrade`; automatitzable amb WSUS /
  `unattended-upgrades`.
- Fer còpia abans d'actualitzacions grosses i provar en un equip pilot.

## Comprova què has après

1. Diferència entre programari lliure i freeware.
2. Què és una llicència OEM i quina limitació té?
3. Per què és prioritari instal·lar les actualitzacions de seguretat?
4. Quines ordres actualitzen un Ubuntu (paquets i versió)?
5. Una actualització de Windows provoca reinicis en bucle. Com ho resols?

---

[⬅ Anterior: Instal·lació de Linux](06-instal-lacio-de-linux.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Bloc següent: Configuració ➡](../03-configuracio-basica/00-index.md)
