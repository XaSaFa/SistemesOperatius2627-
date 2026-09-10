[🏠 Inici](../README.md) › [RA5 · Màquines virtuals](00-index.md) › **1. Virtualització: conceptes**

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Programari i creació de MV ➡](02-programari-i-creacio-de-mv.md)

# 1. Virtualització: conceptes

> Criteris d'avaluació RA5.1–RA5.2 i RA5.6 — *Diferencia màquina real i virtual; avantatges i inconvenients;
> relació de la MV amb el SO amfitrió.*

## 1.1. Màquina real vs. màquina virtual

- **Màquina real (física):** l'ordinador de maquinari (CPU, RAM, disc, targetes) sobre el qual s'executa
  directament un SO.
- **Màquina virtual (MV):** un ordinador **complet simulat per programari**. Té CPU, RAM, disc, targeta de
  xarxa, BIOS/UEFI… **virtuals**, i s'hi pot instal·lar un SO com si fos maquinari real. La MV és, físicament,
  **un conjunt de fitxers** al disc de l'amfitrió (fitxer de configuració + fitxers de disc virtual).

**Virtualització** = tècnica que abstrau els recursos d'un ordinador per executar diversos entorns aïllats
(diverses MV, cadascuna amb el seu SO) sobre el mateix maquinari.

| Terme | Significat |
|---|---|
| **Amfitrió (*host*)** | La màquina física i el seu SO, on s'executa la virtualització |
| **Convidat (*guest*)** | El SO que corre **dins** de la MV |
| **Hipervisor (VMM)** | El programari que crea i gestiona les MV i reparteix els recursos reals |
| **Disc virtual** | Fitxer que la MV veu com un disc dur (`.vdi`, `.vmdk`, `.vhdx`, `.qcow2`) |
| **Instantània (*snapshot*)** | Foto de l'estat complet de la MV per tornar-hi després |
| **Plantilla / clon** | MV base per generar-ne còpies |

## 1.2. Tipus d'hipervisor

| | **Tipus 1 (*bare-metal*)** | **Tipus 2 (allotjat)** |
|---|---|---|
| S'executa sobre… | El maquinari directament | Un SO amfitrió normal |
| Rendiment | Més alt | Una mica inferior (passa pel SO amfitrió) |
| Ús | Servidors, centres de dades, núvol | Escriptori, proves, formació |
| Exemples | VMware ESXi, Microsoft Hyper-V (rol), Proxmox VE, XCP-ng, KVM (integrat al nucli Linux) | **Oracle VirtualBox**, **VMware Workstation/Player/Fusion**, Parallels Desktop |

> **Hyper-V** és un cas particular: quan s'activa a Windows 10/11, el Windows «visible» passa a ser una
> partició sobre l'hipervisor → es comporta com a **tipus 1**.

Altres formes d'aïllament relacionades (no exactament MV):

- **Contenidors** (Docker, LXC, Podman): comparteixen el nucli de l'amfitrió; molt lleugers, pensats per a
  aplicacions, no per a SO complets.
- **Emulació** (QEMU sense KVM, DOSBox): imita una arquitectura diferent (per exemple ARM sobre x86); molt més lenta.
- **Paravirtualització:** el SO convidat «sap» que és virtual i coopera amb l'hipervisor via controladors
  especials (virtio, `guest additions`) → millor rendiment.
- **Assistència de maquinari:** **Intel VT-x / AMD-V** (CPU) i **VT-d / AMD-Vi** (E/S). Cal **activar-la a la
  BIOS/UEFI** perquè les MV de 64 bits funcionin amb rendiment.

## 1.3. Avantatges de les màquines virtuals

- **Aïllament i seguretat:** provar programari sospitós, virus, configuracions arriscades sense afectar
  l'amfitrió; si la MV es fa malbé, s'esborra i es torna a crear.
- **Instantànies:** tornar a un estat anterior en segons (ideal per a pràctiques i actualitzacions).
- **Consolidació:** diversos servidors lògics en un sol equip físic → menys maquinari, menys consum, menys espai.
- **Portabilitat:** una MV es copia, es mou a un altre equip o s'exporta (**OVA/OVF**) i s'importa.
- **Diversos SO alhora:** Windows, Linux i BSD funcionant simultàniament al mateix ordinador.
- **Entorns de proves i formació** reproduïbles i idèntics per a tot un grup.
- **Instal·lació ràpida** a partir de plantilles/clons.
- **Independència del maquinari:** el maquinari virtual és sempre el mateix encara que canviï el físic.
- **Recuperació davant desastres:** còpia de la MV = còpia del servidor sencer.

## 1.4. Inconvenients i limitacions

- **Sobrecàrrega (*overhead*):** una MV sempre rendeix una mica menys que la mateixa càrrega en maquinari real.
- **Necessitat de recursos:** l'amfitrió ha de tenir prou RAM, CPU i disc per a ell **i** per a totes les MV
  actives (no assignar més RAM a les MV que la que sobra a l'amfitrió).
- **E/S de disc i gràfica** poden ser un coll d'ampolla (sobretot jocs i 3D intens).
- **Dependència de l'amfitrió:** si l'amfitrió cau, cauen totes les seves MV.
- **Llicències:** el SO convidat també necessita la seva llicència (Windows dins d'una MV = una llicència més).
- **Complexitat** de xarxa i de gestió quan n'hi ha moltes.
- Alguns programes amb **protecció anti-copia** o que necessiten maquinari específic no funcionen virtualitzats.

## 1.5. Relació entre la MV i el SO amfitrió

- La MV **comparteix** els recursos físics de l'amfitrió segons el que se li assigna (nuclis de CPU, MB de RAM,
  mida de disc virtual).
- **Guest Additions / VMware Tools:** paquet de controladors i utilitats que s'instal·la **dins del convidat**
  per millorar la integració: resolucions de pantalla dinàmiques, acceleració gràfica, **carpetes compartides**
  amb l'amfitrió, **porta-retalls compartit** i arrossegar-i-deixar, sincronització de l'hora, ratolí sense
  captura.
- **Xarxa de la MV** (modes habituals):
  | Mode | Comportament |
  |---|---|
  | **NAT** | La MV surt a Internet a través de l'amfitrió; no és accessible des de la LAN. Per defecte. |
  | **Adaptador pont (*bridged*)** | La MV apareix a la LAN com un equip més, amb IP pròpia del router. |
  | **Xarxa interna / només amfitrió (*host-only*)** | Xarxa privada entre MV (i amfitrió), sense sortida. Ideal per a pràctiques de xarxa. |
- **Carpetes compartides** i unitats USB de l'amfitrió es poden «passar» a la MV.

## 1.6. Casos d'aplicació

- Aules d'informàtica: cada alumne treballa dins d'una MV que pot restaurar.
- Provar una nova versió d'un SO o d'una aplicació abans de desplegar-la.
- Executar una aplicació antiga que només va en un SO antic.
- Muntar un petit laboratori de xarxa (servidor + clients) en un sol portàtil.
- Desenvolupament i proves multiplataforma.
- Servidors: diversos serveis aïllats en MV sobre pocs equips físics.

## 1.7. Resum

- **MV** = ordinador complet simulat per programari (fitxers al disc de l'**amfitrió**), amb el seu SO **convidat**.
- **Hipervisor tipus 1** (sobre maquinari, servidors) vs. **tipus 2** (sobre un SO, escriptori).
- Cal **VT-x/AMD-V** activat a la BIOS.
- Avantatges: aïllament, instantànies, consolidació, portabilitat, diversos SO alhora. Inconvenients:
  sobrecàrrega, consum de recursos, llicències, dependència de l'amfitrió.
- Les **Guest Additions/Tools** i els modes de **xarxa** (NAT, pont, host-only) defineixen la integració amb l'amfitrió.

## Comprova què has après

1. Diferència entre màquina real i màquina virtual. Què és, físicament, una MV?
2. Classifica VirtualBox i VMware ESXi com a hipervisor de tipus 1 o 2.
3. Per què cal activar VT-x/AMD-V a la BIOS?
4. Dona tres avantatges i dos inconvenients de virtualitzar.
5. Quin mode de xarxa fa que la MV aparegui a la LAN amb IP pròpia? Quin l'aïlla per a pràctiques?
6. Què aporten les Guest Additions / VMware Tools?

---

[⬅ Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Programari i creació de MV ➡](02-programari-i-creacio-de-mv.md)
