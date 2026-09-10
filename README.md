# Base de coneixements — Sistemes operatius monolloc (MP0222)

Materials del mòdul professional **0222 · Sistemes operatius monolloc** del cicle formatiu de grau mitjà
**Sistemes Microinformàtics i Xarxes (SMX)** de la Generalitat de Catalunya.

- **Durada:** 132 h (99 h al centre + 33 h d'estada a l'empresa) · **Curs:** 1r.
- **Font curricular:** Decret 193/2013 (SMX) i document d'orientacions IC10 del Departament d'Educació.
- **Fonts de contingut:** llibre *Sistemas operativos monopuesto* (F. J. Muñoz López, McGraw-Hill) i
  documentació oficial de fabricants (Microsoft Learn, pàgines de manual de Linux, documentació d'Ubuntu/Debian/Red Hat).

> **Nota de vigència.** Els llibres de referència descriuen Windows XP/7 i Ubuntu 11.10. Aquí el contingut
> s'ha actualitzat a **Windows 10/11**, **systemd**, **ext4/exFAT/Btrfs** i les eines actuals, mantenint la
> seqüència didàctica del currículum. El contingut històric amb valor formatiu (FAT, MBR, `init`…) es conserva
> i s'indica que és llegat.

---

## Menú de navegació

### Referència

- **[Currículum oficial](00-referencia/01-curriculum-oficial.md)** — resultats d'aprenentatge, criteris d'avaluació i continguts del mòdul (text del currículum).
- **[Glossari](00-referencia/02-glossari.md)** — termes clau ordenats alfabèticament, amb enllaç al tema on s'expliquen.
- [Fonts i bibliografia](00-referencia/03-fonts-i-bibliografia.md) — llibres i documentació oficial utilitzats, amb enllaços.

### Resultats d'aprenentatge — ordre del curs

Ordre de treball: **RA1 → RA4 → RA5 → RA3 → RA2**. Primer la base teòrica i pràctica; després
l'administració (nucli del curs, amb focus en Linux); les màquines virtuals; la configuració; i, per acabar,
la instal·lació. Cada bloc obre amb un **índex amb el menú de temes** i la relació amb els criteris d'avaluació.

| Ordre | Bloc | Enunciat del resultat d'aprenentatge |
|:-:|---|---|
| 1r | **[RA1 · Caracterització dels sistemes operatius](01-caracteritzacio-dels-so/00-index.md)** | Reconeix les característiques dels sistemes operatius, descrivint-ne els tipus i aplicacions. |
| 2n | **[RA4 · Administració del sistema operatiu](04-administracio-del-so/00-index.md)** | Realitza operacions bàsiques d'administració de sistemes operatius, optimitzant el sistema per al seu ús. |
| 3r | **[RA5 · Màquines virtuals](05-maquines-virtuals/00-index.md)** | Crea màquines virtuals identificant-ne el camp d'aplicació i instal·lant-hi programari específic. |
| 4t | **[RA3 · Configuració bàsica del sistema operatiu](03-configuracio-basica/00-index.md)** | Realitza tasques bàsiques de configuració de sistemes operatius, interpretant-ne requeriments i descrivint-ne els procediments. |
| 5è | **[RA2 · Instal·lació de sistemes operatius](02-instal-lacio-de-so/00-index.md)** | Instal·la sistemes operatius, relacionant-ne les característiques amb el maquinari i el programari d'aplicació. |

---

## Com fer servir aquesta base de coneixements

- Cada **bloc** és una carpeta. El número de la carpeta és el número del **resultat d'aprenentatge**
  (`01…` = RA1, `04…` = RA4…), **no** l'ordre del curs.
- El fitxer `00-index.md` de cada bloc conté el **menú de temes** i els relaciona amb els criteris d'avaluació.
- Cada tema té una barra de navegació a dalt i a baix
  (`Anterior · Índex del bloc · Índex general · Següent`) que segueix l'ordre del curs.
- **`index.html`** (obre'l amb doble clic) és un navegador offline de tota la base, amb cerca i tema clar/fosc.

---

## Temporització orientativa (99 h al centre)

| Ordre | Bloc | Hores |
|:-:|---|:-:|
| 1r | RA1 · Caracterització | 20 h |
| 2n | RA4 · Administració | 34 h |
| 3r | RA5 · Màquines virtuals | 10 h |
| 4t | RA3 · Configuració | 16 h |
| 5è | RA2 · Instal·lació | 16 h |
| — | Avaluació i marge | 3 h |

Les 33 h d'estada a l'empresa són addicionals i reforcen sobre el terreny, sobretot, RA2, RA3 i RA4.
