[⬅ Anterior: Virtualització — conceptes](01-virtualitzacio-conceptes.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md)

# 2. Programari de virtualització i creació de màquines virtuals

> Criteris d'avaluació RA5.3–RA5.5 i RA5.7 — *Instal·la programari lliure i propietari per crear MV; crea MV
> de SO lliures i propietaris; configura MV; realitza proves de rendiment.*

## 2.1. Programari de virtualització (tipus 2, escriptori)

| Producte | Llicència | SO amfitrió | Notes |
|---|---|---|---|
| **Oracle VirtualBox** | Lliure (GPLv3); *Extension Pack* amb llicència PUEL per a ús personal/educatiu | Windows, Linux, macOS (Intel), Solaris | El més usat per a formació. Discos `.vdi`. |
| **VMware Workstation Pro / Fusion Pro** | **Gratuït** per a ús personal des de 2024 (abans de pagament) | Windows/Linux (Workstation), macOS (Fusion) | Molt estable; discos `.vmdk`. |
| **VMware Workstation Player** | Gratuït per a ús no comercial (integrat a Workstation) | Windows, Linux | Versió reduïda. |
| **Microsoft Hyper-V** | Inclòs a Windows 10/11 **Pro/Enterprise/Education** | Windows | S'activa com a *característica de Windows*; converteix Windows en tipus 1. |
| **KVM + QEMU + virt-manager** | Lliure (GPL) | Linux | Virtualització nativa del nucli Linux; rendiment de tipus 1. GUI: *Gestor de màquines virtuals*. |
| **GNOME Boxes** | Lliure | Linux | Front-end senzill sobre KVM/QEMU, ideal per començar. |

### Instal·lació

- **VirtualBox (Windows):** descarregar l'instal·lador del web oficial → assistent *Next*; instal·la
  controladors de xarxa virtuals (pot tallar la xarxa uns segons). Instal·lar després l'**Extension Pack**
  (USB 3.0, RDP, xifratge de disc): *Fitxer → Eines → Gestor d'extensions*.
- **VirtualBox (Ubuntu):** `sudo apt install virtualbox virtualbox-ext-pack` (repositori *multiverse*) o el
  `.deb` oficial d'Oracle. Cal que l'usuari sigui del grup `vboxusers` per usar USB.
- **Hyper-V:** *Activa o desactiva les característiques del Windows* → marcar *Hyper-V* → reiniciar. O
  PowerShell: `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`.
- **KVM (Ubuntu):** `sudo apt install qemu-kvm libvirt-daemon-system virt-manager`; afegir l'usuari als grups
  `libvirt` i `kvm`; comprovar suport: `kvm-ok` / `egrep -c '(vmx|svm)' /proc/cpuinfo`.

> **Compatibilitat:** Hyper-V i VirtualBox/VMware poden entrar en conflicte perquè tots volen l'hipervisor.
> Les versions recents de VirtualBox (≥ 6.1) i VMware poden funcionar sobre l'Hyper-V de Windows, amb menys
> rendiment. En un equip amb WSL2 o *Memory Integrity* actiu, l'Hyper-V ja hi és.

## 2.2. Requisits de l'amfitrió

- CPU amb **VT-x/AMD-V activat a la BIOS/UEFI** (obligatori per a convidats de 64 bits amb rendiment).
- RAM: la de l'amfitrió + la de cada MV activa (com a mínim 8 GB per treballar còmodament amb 1–2 MV).
- Disc: espai per als discos virtuals (poden ser de mida fixa o **dinàmica/expansiva**).
- Virtualització desactivada per *Hyper-V/Device Guard* si es vol màxim rendiment amb VirtualBox/VMware.

## 2.3. Crear una màquina virtual (procediment general)

1. **Nom i tipus de SO:** l'hipervisor ajusta valors per defecte segons el SO triat (Windows 11, Ubuntu…).
2. **Memòria RAM:** p. ex. 2–4 GB per a un Linux d'escriptori; 4–8 GB per a Windows 11. No passar de ~50–70 %
   de la RAM física.
3. **Processadors:** 1–2 vCPU (o més si l'amfitrió en té molts).
4. **Disc dur virtual:** crear-ne un de nou.
   - Format: `.vdi` (VirtualBox), `.vmdk` (VMware, més portable), `.vhdx` (Hyper-V), `.qcow2` (KVM).
   - Assignació: **dinàmica** (creix segons l'ús, ocupa menys) o **fixa** (reserva tot l'espai, una mica més
     ràpida).
   - Mida: p. ex. 25–40 GB per a Linux; 64 GB+ per a Windows 11.
5. **Firmware:** BIOS o **UEFI** (Windows 11 necessita UEFI + **TPM virtual** + Secure Boot; VirtualBox 7 i
   Hyper-V “Generació 2” els proporcionen).
6. **Xarxa:** NAT (per defecte), pont o només amfitrió ([tema 1 §1.5](01-virtualitzacio-conceptes.md#15-relació-entre-la-mv-i-el-so-amfitrió)).
7. **Suport d'instal·lació:** connectar la **ISO** del SO a la unitat òptica virtual
   (*Configuració → Emmagatzematge → unitat òptica → triar fitxer de disc*).
8. Opcional: memòria de vídeo, acceleració 3D, portàtils USB, carpetes compartides, ordre d'arrencada.

### Amb línia d'ordres (VirtualBox — `VBoxManage`)

```bash
VBoxManage createvm --name "Ubuntu24" --ostype Ubuntu_64 --register
VBoxManage modifyvm "Ubuntu24" --memory 4096 --cpus 2 --nic1 nat --firmware efi
VBoxManage createhd --filename "Ubuntu24.vdi" --size 40000 --variant Standard
VBoxManage storagectl "Ubuntu24" --name "SATA" --add sata
VBoxManage storageattach "Ubuntu24" --storagectl "SATA" --port 0 --device 0 --type hdd --medium "Ubuntu24.vdi"
VBoxManage storageattach "Ubuntu24" --storagectl "SATA" --port 1 --device 0 --type dvddrive --medium "ubuntu-24.04.iso"
VBoxManage startvm "Ubuntu24"
```

## 2.4. Instal·lar el SO convidat

- Arrencar la MV → l'instal·lador de la ISO s'inicia igual que en maquinari real.
- Seguir el procediment de [RA2 · instal·lació de Windows](../02-instal-lacio-de-so/05-instal-lacio-de-windows.md)
  o [RA2 · instal·lació de Linux](../02-instal-lacio-de-so/06-instal-lacio-de-linux.md).
- En acabar, **treure la ISO** de la unitat òptica virtual perquè arrenqui del disc.

## 2.5. Instal·lar les *Guest Additions / Tools*

- **VirtualBox:** menú *Dispositius → Inserir imatge de CD de les Guest Additions* i executar-la dins del
  convidat (a Linux: `sudo apt install build-essential dkms linux-headers-$(uname -r)` abans; després muntar el
  CD i executar `sudo sh ./VBoxLinuxAdditions.run`). Reiniciar la MV.
- **VMware:** *VM → Install VMware Tools* (o `open-vm-tools` a Linux: `sudo apt install open-vm-tools open-vm-tools-desktop`).
- **Hyper-V:** els *Integration Services* ja hi són a Windows i als nuclis Linux moderns; per a millor
  experiència gràfica, connexió **Enhanced Session**.
- **KVM/QEMU:** controladors **virtio** i `spice-vdagent` / `qemu-guest-agent` dins del convidat.

Un cop instal·lades: canvi de resolució automàtic, porta-retalls i arrossegar-i-deixar compartits, carpetes
compartides, hora sincronitzada, ratolí integrat.

## 2.6. Configurar la MV després de crear-la

- **Carpetes compartides:** *Configuració → Carpetes compartides* → triar carpeta de l'amfitrió, punt de
  muntatge i permisos (a Linux, l'usuari ha de ser del grup `vboxsf`).
- **Instantànies (*snapshots*):** *Instantànies → Fer instantània* abans de canvis arriscats; *Restaurar* per
  tornar-hi. Base per a pràctiques reproduïbles.
- **Clonar:** clon *enllaçat* (ràpid, comparteix la base amb l'original) o *complet* (independent).
- **Exportar/importar:** *Fitxer → Exporta servei virtualitzat* → fitxer **OVA/OVF** portable a un altre
  hipervisor.
- **Ajustar recursos** segons l'ús (més/menys RAM, vCPU, memòria de vídeo, acceleració 3D).
- **Grup / ordre d'arrencada automàtic** si la MV ha d'aixecar-se amb l'amfitrió.

## 2.7. Proves de rendiment (*benchmarking*)

- Comparar el rendiment del **SO amfitrió** i del **SO convidat** amb la mateixa prova:
  - CPU: `sysbench cpu`, Geekbench, `7z b`.
  - Memòria: `sysbench memory`, `mbw`.
  - Disc: `CrystalDiskMark` (Windows), `fio`, `hdparm -tT /dev/sdX`, `dd` (aproximat).
  - General: PassMark, Novabench.
- Mesurar l'impacte de la configuració: nombre de vCPU, RAM, disc fix vs. dinàmic, acceleració de maquinari
  activada/desactivada, Guest Additions instal·lades o no, hipervisor niat.
- Vigilar l'amfitrió durant la prova (Administrador de tasques / `htop`) per detectar si el coll d'ampolla és
  la CPU, la RAM (swap!) o el disc.
- Conclusió esperada: el convidat sempre rendeix **una mica menys** que l'amfitrió; la diferència és petita en
  CPU/RAM i més gran en E/S de disc i gràfica 3D.

## 2.8. Resum

- Programari: **VirtualBox** (lliure), **VMware Workstation/Player** (gratuït ús personal), **Hyper-V**
  (Windows Pro), **KVM/QEMU + virt-manager** (Linux, natiu).
- Crear MV = triar SO → RAM → vCPU → disc virtual (dinàmic/fix, `.vdi`/`.vmdk`/`.vhdx`/`.qcow2`) → firmware
  (BIOS/UEFI, TPM per a Win11) → xarxa → connectar ISO → instal·lar el SO → treure la ISO.
- Instal·lar **Guest Additions/Tools** per a integració (pantalla, porta-retalls, carpetes compartides).
- Configurar: carpetes compartides, **instantànies**, clons, export **OVA/OVF**.
- Fer **proves de rendiment** comparant amfitrió i convidat i variant la configuració.

## Comprova què has après

1. Quin programa de virtualització usaries en una aula amb Windows i per què?
2. Diferència entre un disc virtual de mida fixa i un de dinàmic.
3. Què cal afegir a una MV perquè pugui instal·lar-hi Windows 11?
4. Per a què serveixen les Guest Additions i què deixa de funcionar bé si no s'instal·len?
5. Per què és útil fer una instantània abans d'una pràctica?
6. En quins recursos esperes veure més diferència de rendiment entre l'amfitrió i el convidat?

---

[⬅ Anterior: Virtualització — conceptes](01-virtualitzacio-conceptes.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md)
