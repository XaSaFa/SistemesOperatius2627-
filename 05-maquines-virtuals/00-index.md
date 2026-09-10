[🏠 Inici](../README.md) › **RA5 · Màquines virtuals**

[⬅ Bloc anterior: Administració](../04-administracio-del-so/00-index.md) · [🏠 Inici](../README.md) · [Bloc següent: Configuració ➡](../03-configuracio-basica/00-index.md)

# Bloc 05 · Màquines virtuals (RA5)

> **RA5.** Crea màquines virtuals identificant-ne el camp d'aplicació i instal·lant-hi programari específic.

## Temes del bloc

| # | Tema | Criteris d'avaluació |
|---|---|---|
| 01 | [Virtualització: conceptes](01-virtualitzacio-conceptes.md) | CA1, CA2, CA6 |
| 02 | [Programari de virtualització i creació de màquines virtuals](02-programari-i-creacio-de-mv.md) | CA3, CA4, CA5, CA7 |

## Idees força del bloc

- Una **màquina virtual (MV)** és un ordinador complet emulat per programari (l'**hipervisor**) sobre un
  equip **amfitrió**; a dins hi corre un SO **convidat** aïllat.
- Avantatges: aïllament, proves segures, instantànies, consolidació de servidors, portabilitat. Inconvenient:
  sobrecàrrega de rendiment i necessitat de recursos.
- Els hipervisors són de **tipus 1** (sobre el maquinari) o **tipus 2** (sobre un SO). VirtualBox, VMware
  Workstation/Player, Hyper-V, KVM/QEMU.
- Crear una MV = definir maquinari virtual (CPU, RAM, disc, xarxa) + instal·lar-hi el SO convidat des d'una
  ISO + instal·lar les **guest additions/tools**.

---

[🏠 Inici](../README.md) · [Primer tema ➡](01-virtualitzacio-conceptes.md)
