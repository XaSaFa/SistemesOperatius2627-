[🏠 Inici](../README.md) › [RA1 · Caracterització dels sistemes operatius](00-index.md) › **2. Representació de la informació**

[⬅ Anterior: Sistema informàtic](01-sistema-informatic-hardware-software-firmware.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Concepte del SO ➡](03-concepte-funcions-i-estructura-del-so.md)

# 2. Representació de la informació

> Criteri d'avaluació RA1.2 — *Codifica i relaciona la informació en els diferents sistemes de representació.*

## 2.1. Per què cal codificar

L'ordinador només entén de **corrent elèctric**: presència (1) o absència (0) d'energia en petits condensadors
(biestables). No pot emmagatzemar directament la lletra `A` ni el símbol `*`. Per això tota la informació que
maneja l'usuari es tradueix a combinacions de **bits** mitjançant un **codi**.

- **Bit** (*binary digit*): unitat mínima d'informació; val 0 o 1.
- **Byte / octet:** grup de 8 bits. És la unitat bàsica de mesura i d'adreçament de la memòria.
- Cada byte pot representar un caràcter (segons la taula de codis) o un valor numèric de 0 a 255.

### Múltiples del byte

| Prefix binari (IEC) | Valor | Prefix decimal (SI) | Valor |
|---|---|---|---|
| kibibyte (KiB) | 2¹⁰ = 1 024 B | kilobyte (kB) | 10³ = 1 000 B |
| mebibyte (MiB) | 2²⁰ B | megabyte (MB) | 10⁶ B |
| gibibyte (GiB) | 2³⁰ B | gigabyte (GB) | 10⁹ B |
| tebibyte (TiB) | 2⁴⁰ B | terabyte (TB) | 10¹² B |

> Els fabricants de discos usen els prefixos decimals (1 TB = 10¹² B) i els SO sovint mostren els binaris
> (1 TiB = 2⁴⁰ B); per això un disc «de 1 TB» apareix com ≈ 931 GiB.

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

### Conversions bàsiques

- **Decimal → binari:** divisions successives entre 2; els residus, de baix a dalt.
  `26 → 11010₂`
- **Binari → decimal:** aplicar el TFN. `11010₂ = 16+8+0+2+0 = 26`
- **Binari ↔ octal:** agrupar bits de 3 en 3 (des de la dreta). `11 010₂ = 32₈`
- **Binari ↔ hexadecimal:** agrupar bits de 4 en 4. `0001 1010₂ = 1A₁₆`

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
4. Per què UTF-8 és compatible «cap enrere» amb ASCII?
5. Un disc anunciat com a 500 GB, quants GiB mostrarà aproximadament el sistema operatiu?

---

[⬅ Anterior: Sistema informàtic](01-sistema-informatic-hardware-software-firmware.md) · [Índex del bloc](00-index.md) · [🏠 Inici](../README.md) · [Següent: Concepte del SO ➡](03-concepte-funcions-i-estructura-del-so.md)
