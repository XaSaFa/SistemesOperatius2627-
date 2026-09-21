[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **2. Representació de la informació**

[⬅ Anterior: Sistema informàtic](01-sistema-informatic-hardware-software-firmware.md) · [Següent: Concepte del SO ➡](03-concepte-funcions-i-estructura-del-so.md)

# 2. Representació de la informació

> Criteri d'avaluació RA1.2 — *Codifica i relaciona la informació en els diferents sistemes de representació.*

## 2.1. Per què cal codificar

<img width="500" alt="image" src="https://github.com/user-attachments/assets/9e5e9410-e1d9-4536-96ec-fd94ae34194c" />

L'ordinador només entén de **corrent elèctric**: presència (1) o absència (0) d'energia en petits condensadors
(biestables). No pot emmagatzemar directament la lletra `A` ni el símbol `*`. Per això tota la informació que
maneja l'usuari es tradueix a combinacions de **bits** mitjançant un **codi**.

- **Bit** (*binary digit*): unitat mínima d'informació; val 0 o 1.
- **Byte / octet:** grup de 8 bits. És la unitat bàsica de mesura i d'adreçament de la memòria.
- Cada byte pot representar un caràcter (segons la taula de codis) o un valor numèric de 0 a 255.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/f997ae5b-62eb-45e8-afc4-c4dcedc52582" />


### Múltiples del byte: GB vs. GiB

<img width="500" alt="image" src="https://github.com/user-attachments/assets/edc75bed-30b0-4dec-9cda-85f36cf9562f" />

Hi ha **dos sistemes de prefixos** i, encara que sovint es confonen, **no representen la mateixa quantitat de
bytes**:

- **Prefixos decimals / SI** (kB, MB, GB, TB): potències de **10**. `1 GB = 10⁹ B = 1 000 000 000 bytes`. Són
  els prefixos «normals» del Sistema Internacional (com en 1 km = 1 000 m).
- **Prefixos binaris / IEC** (KiB, MiB, GiB, TiB): potències de **2**. `1 GiB = 2³⁰ B = 1 073 741 824 bytes`.
  Es van normalitzar el 1998 (IEC 60027-2) precisament perquè abans «GB» s'utilitzava informalment amb els dos
  significats alhora i generava ambigüitat.

| Prefix binari (IEC) | Valor exacte | Prefix decimal (SI) | Valor exacte |
|---|---|---|---|
| kibibyte (KiB) | 2¹⁰ = 1 024 B | kilobyte (kB) | 10³ = 1 000 B |
| mebibyte (MiB) | 2²⁰ = 1 048 576 B | megabyte (MB) | 10⁶ = 1 000 000 B |
| gibibyte (GiB) | 2³⁰ = 1 073 741 824 B | gigabyte (GB) | 10⁹ = 1 000 000 000 B |
| tebibyte (TiB) | 2⁴⁰ = 1 099 511 627 776 B | terabyte (TB) | 10¹² = 1 000 000 000 000 B |

Com que 1 GiB (1 073 741 824 B) > 1 GB (1 000 000 000 B), **el mateix disc «pesa» menys en GiB que en GB**, i la
diferència creix com més gran és la unitat:

| | Factor de conversió |
|---|---|
| 1 KiB | = 1,024 kB |
| 1 MiB | ≈ 1,049 MB |
| 1 GiB | ≈ 1,074 GB |
| 1 TiB | ≈ 1,100 TB |

#### Qui fa servir cada prefix

| Qui | Prefix real que empra | Per què |
|---|---|---|
| Fabricants de discos, SSD i pen drives | **Decimal** (GB, TB) | És l'estàndard SI oficial i, a més, el mateix nombre de bytes «sona» més gran en decimal (bon argument comercial) |
| Mòduls de memòria **RAM** | **Coincideix amb el binari** | La RAM s'adreça en potències de 2, així que uns «8 GB» de RAM són, en realitat, 8 GiB exactes: no hi ha pèrdua |
| Sistemes operatius (Explorador de Windows, `ls -lh`, Fitxers de GNOME…) | Solen **calcular en binari però etiquetar-ho «GB», «MB»…** | És la font principal de la confusió: el número que mostren és de GiB, però el rètol diu GB |

> **Exemple.** Un disc s'ven com a «500 GB» (mesura decimal del fabricant):
> `500 GB = 500 × 10⁹ B = 500 000 000 000 B`.
> Per saber quants GiB en calcularà el sistema operatiu: `500 000 000 000 ÷ 2³⁰ ≈ 465,7 GiB`.
> Per això un disc «de 500 GB» apareix a l'Explorador de Windows com uns «465 GB» (en realitat GiB, mal
> etiquetats): no falten dades, és una diferència d'unitat de mesura.

A Linux, `lsblk`, `df -h` o `free -h` mostren per defecte els valors en **binari** (KiB/MiB/GiB, tot i que
alguns rotulen «K»/«M»/«G»); si es vol veure en decimal cal l'opció `--si` (per exemple `df -H` o `du --si`).

> Els fabricants de discos usen els prefixos decimals (1 TB = 10¹² B) i els SO sovint mostren els binaris
> (1 TiB = 2⁴⁰ B); per això un disc «de 1 TB» apareix com ≈ 931 GiB.

### Activitats de repàs

**Exercici 1: Unitats bàsiques i capacitat (Bits i Bytes)**

Un fitxer de text conté exactament 256 Bytes d'informació.

1. Quants bits ocupa aquest fitxer a la memòria?
2. Quin és el valor numèric màxim (en decimal) que es pot emmagatzemar en un sol Byte?

**Exercici 2: Prefixos decimals (SI) vs. binaris (IEC)**

Tenim dos fitxers de dades:

- El Fitxer A té una mida de 4 MB (megabytes, segons l'estàndard decimal SI).
- El Fitxer B té una mida de 4 MiB (mebibytes, segons l'estàndard binari IEC).

Quin dels dos fitxers té una mida real més gran en bytes i quants bytes de diferència hi ha entre tots dos?

**Exercici 3: El «fals» espai perdut als discos durs**

Un alumne ha comprat un pendrive de 64 GB (mesura comercial del fabricant). Quan el connecta a un ordinador amb Windows, l'Explorador li indica que la capacitat total és d'aproximadament 59,6 GB.

1. Per què hi ha aquesta diferència si el disc no té cap dada danyada?
2. Realitza el càlcul matemàtic exactat per comprovar d'on surt la xifra de 59,6 GiB.

**Exercici 4: Memòria RAM vs. Disc SSD**

Un ordinador té instal·lats 16 GB de RAM i un disc SSD de 16 GB.

- Els 16 GB de la memòria RAM equivalen exactament a $16 \times 10^9$ bytes o a $16 \times 2^{30}$ bytes? Justifica la resposta.
- Quants bytes reals té el disc SSD de 16 GB?
- Quina memòria és més gran la RAM o la del SSD?

## 2.2. Sistemes de numeració

Un **sistema de numeració** és el conjunt de símbols i regles per representar quantitats. Es caracteritza per la
**base** (nombre de símbols diferents). Els sistemes que fem servir són **posicionals**: el valor d'un símbol
depèn de la seva posició.

**Teorema fonamental de la numeració (TFN):** el valor d'un nombre és la suma de cada símbol multiplicat per la
base elevada a la seva posició.

```
NÚM = Xn·Bⁿ + … + X2·B² + X1·B¹ + X0·B⁰ + X-1·B⁻¹ + …
Exemple (base 10):  283 = 2·10² + 8·10¹ + 3·10⁰ = 200 + 80 + 3
```

| Sistema | Base | Símbols | Ús |
|---|---|---|---|
| **Binari** | 2 | 0, 1 | Intern de l'ordinador |
| **Octal** | 8 | 0–7 | Permisos de Linux (`chmod 755`); cada dígit = 3 bits |
| **Decimal** | 10 | 0–9 | Ús humà habitual |
| **Hexadecimal** | 16 | 0–9, A–F | Adreces de memòria, codis de color, dumps; cada dígit = 4 bits |

<img width="500" alt="image" src="https://github.com/user-attachments/assets/e9d4ac11-d222-4e66-8ea5-eb1b4febf864" />

### Conversions bàsiques

- **Decimal → binari:** divisions successives entre 2; els residus, de baix a dalt.
  `26 → 11010₂`
  
<img width="419" height="291" alt="image" src="https://github.com/user-attachments/assets/6c61afdb-50ba-4611-94a8-cf8a25db55aa" />

- **Binari → decimal:** aplicar el TFN  (Teorema Fonamental de la Numeració). `11010₂ = 16+8+0+2+0 = 26`

<img width="451" height="68" alt="image" src="https://github.com/user-attachments/assets/f3700171-a20e-4028-8c91-9d85314c893d" />

- **Binari ↔ octal:** agrupar bits de 3 en 3 (des de la dreta). `11 010₂ = 32₈`

<img width="285" height="330" alt="image" src="https://github.com/user-attachments/assets/8f91d862-65a4-4b2a-9897-6d6e15f4eaaf" />

- **Binari ↔ hexadecimal:** agrupar bits de 4 en 4. `0001 1010₂ = 1A₁₆`

<img width="500"  alt="image" src="https://github.com/user-attachments/assets/1c7e974c-17f6-4247-82ab-aa44a67c6011" />

### Taula d'equivalència (0–15)

| Dec | Bin (4 bits) | Oct | Hex |
|---|---|---|---|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 10 | 8 |
| 9 | 1001 | 11 | 9 |
| 10 | 1010 | 12 | A |
| 11 | 1011 | 13 | B |
| 12 | 1100 | 14 | C |
| 13 | 1101 | 15 | D |
| 14 | 1110 | 16 | E |
| 15 | 1111 | 17 | F |

## 2.3. Codificació de caràcters

| Codi | Bits/caràcter | Abast | Notes |
|---|---|---|---|
| **ASCII** | 7 (sovint 8) | 128 caràcters | Anglès bàsic; sense accents ni `ç`, `ñ` |
| **ASCII estès / ISO-8859-1 (Latin-1) / Windows-1252** | 8 | 256 | Afegeix caràcters occidentals; incompatibilitats entre pàgines de codis |
| **Unicode** | Variable | > 149 000 caràcters | Estàndard universal (llatí, ciríl·lic, àrab, CJK, emojis) |
| **UTF-8** | 1–4 bytes | Tot Unicode | Codificació dominant a web, Linux i macOS; compatible cap enrere amb ASCII |
| **UTF-16** | 2 o 4 bytes | Tot Unicode | Ús intern a Windows i Java |

**Taula ASCII:** American Standard Code for Information Interchange

<img width="696" height="566" alt="image" src="https://github.com/user-attachments/assets/56c00871-1139-4ea2-9187-a041e408a8d8" />

> Quan un fitxer de text es llegeix amb una codificació diferent de la que es va desar, els accents es veuen
> corruptes (*mojibake*): `Ã±` en lloc de `ñ`. La solució és indicar la codificació correcta (habitualment UTF-8).

## 2.4. Representació de nombres i altres dades

- **Enters sense signe:** binari pur.
- **Enters amb signe:** **complement a dos** (permet sumar i restar amb el mateix circuit).
- **Reals:** **coma flotant** (estàndard IEEE 754: signe, exponent, mantissa).
- **Imatges:** mapes de bits (píxels amb profunditat de color: 8, 24, 32 bits) o vectorials.
- **So:** mostreig (freqüència en Hz) i quantització (bits per mostra).

## 2.5. Resum

- Tota la informació es redueix a bits; 8 bits = 1 byte.
- Els sistemes binari, octal, decimal i hexadecimal es converteixen entre si amb el TFN o agrupant bits.
- Els caràcters es codifiquen amb ASCII (llegat) o **Unicode/UTF-8** (actual i recomanat).

## Comprova què has après

1. Converteix `45` decimal a binari, octal i hexadecimal.
2. Converteix `1011 1100₂` a hexadecimal i a decimal.
3. Quants caràcters diferents pot representar un codi de 8 bits? I un de 7?


---

[⬅ Anterior: Sistema informàtic](01-sistema-informatic-hardware-software-firmware.md) · [Següent: Concepte del SO ➡](03-concepte-funcions-i-estructura-del-so.md)
