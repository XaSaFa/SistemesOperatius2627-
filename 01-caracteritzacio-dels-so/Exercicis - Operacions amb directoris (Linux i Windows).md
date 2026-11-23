# Operacions amb directoris — Linux i Windows

Nom i cognoms:

## 1. Referència d'ordres

### Linux (Bash)

| Operació | Ordre | Exemple | Notes |
|---|---|---|---|
| **Crear** un directori | `mkdir nom` | `mkdir practiques` | `mkdir -p pare/fill` crea tota la cadena de pares si no existeixen: `mkdir -p projectes/web/css` |
| **Esborrar** un directori | `rmdir nom` (buit) · `rm -r nom` (amb contingut) | `rmdir buit` · `rm -r practiques` | `rm -rf nom` esborra sense preguntar ni avisar — **compte**, no té paperera ni desfer |
| **Moure** un directori | `mv origen destí` | `mv practiques ~/Documents/` | Si `destí` ja existeix com a directori, hi mou `origen` a dins; si no existeix, el resultat és un canvi de nom |
| **Canviar de nom** | `mv nom_antic nom_nou` | `mv antic nou` | A Linux no hi ha una ordre `rename` pròpia per a directoris: renombrar és «moure» dins del mateix pare |
| **Llistar el contingut** | `ls` | `ls -la ~/practiques` | `-l` detall (permisos, mida, data); `-a` inclou ocults (`.`); `-h` mides llegibles (KB/MB) |
| **Navegar (canviar-hi)** | `cd ruta` | `cd /var/log` · `cd ..` (pare) · `cd ~` (home) · `cd -` (directori anterior) | `pwd` mostra on ets; les rutes fan servir `/` i poden ser absolutes (`/home/anna/...`) o relatives (`../dades`) |

```bash
mkdir -p projecte/dades
cd projecte/dades
ls -la
mv ../dades ../arxiu       # el renombra a "arxiu"
rm -r ../arxiu
cd ..
```

### Windows (CMD, amb l'equivalent PowerShell)

| Operació | Ordre (CMD) | Exemple | PowerShell |
|---|---|---|---|
| **Crear** un directori | `mkdir nom` / `md nom` | `mkdir practiques` | `New-Item -ItemType Directory -Name practiques` |
| **Esborrar** un directori | `rmdir nom` (buit) · `rmdir /s nom` (amb contingut, pregunta) · `rmdir /s /q nom` (sense preguntar) | `rmdir /s /q practiques` | `Remove-Item -Recurse -Force practiques` |
| **Moure** un directori | `move origen destí` | `move practiques C:\Users\anna\Documents\` | `Move-Item practiques C:\Users\anna\Documents\` |
| **Canviar de nom** | `ren nom_antic nom_nou` (o `rename`) | `ren practiques exercicis` | `Rename-Item practiques exercicis` |
| **Llistar el contingut** | `dir` | `dir /a` (amb ocults) · `dir /s` (recursiu, subcarpetes) | `Get-ChildItem` (àlies `ls`, `dir`) |
| **Navegar (canviar-hi)** | `cd ruta` | `cd C:\Users\anna\Documents` · `cd ..` · `cd \` (arrel de la unitat) | `Set-Location ruta` (àlies `cd`) |

```bat
mkdir projecte\dades
cd projecte\dades
dir
move ..\dades ..\arxiu
rmdir /s /q ..\arxiu
cd ..
```

> **Detall important a Windows:** `cd` sol **no canvia d'unitat**. Si ets a `C:\` i vols anar a `D:\dades`, cal `cd /d D:\dades` (o escriure primer `D:` i després `cd dades`). A Linux no existeix aquest problema perquè totes les unitats pengen d'un únic arbre arran de `/`.

---

## 2. Exercicis

### A. Ordres soltes — Linux

1. Escriu l'ordre per crear un directori anomenat `informes` dins del directori actual.
2. Escriu, en una sola ordre, el que calgui per crear l'estructura `web/css/estils` (tots els directoris intermedis que faci falta, encara que no existeixin encara).
3. Estàs dins de `/home/anna/practiques/2024`. Escriu l'ordre per pujar **dos** nivells amunt en una sola instrucció.
4. Escriu l'ordre per llistar el contingut de `/var/log` mostrant també els elements ocults, amb detall (permisos, mida, data).
5. Tens un directori buit anomenat `temp`. Escriu l'ordre més senzilla per esborrar-lo.
6. El directori `backup_vell` té contingut a dins. Escriu l'ordre per esborrar-lo sencer **sense** que et demani confirmació.
7. Escriu l'ordre per canviar el nom del directori `fotos2024` a `fotos_antigues`.
8. Escriu l'ordre per moure el directori `projecte` dins de `~/Documents/`.

### B. Ordres soltes — Windows

9. Escriu l'ordre de CMD per crear un directori anomenat `informes`.
10. Escriu l'ordre de CMD per esborrar el directori `temp` (buit).
11. El directori `backup_vell` té contingut a dins. Escriu l'ordre de CMD per esborrar-lo sencer sense confirmació.
12. Escriu l'ordre de CMD per canviar el nom de `fotos2024` a `fotos_antigues`.
13. Escriu l'ordre de CMD per moure `C:\projecte` dins de `C:\Users\anna\Documents\`.
14. Estàs al disc `C:\` i vols anar directament a `D:\dades`. Escriu l'ordre de CMD correcta (compte amb el detall de la unitat!).
15. Escriu l'ordre de PowerShell equivalent a `dir` de la taula de referència.

### C. Escenaris (seqüències d'ordres)

16. Parteixes d'aquesta estructura buida a **Linux**:
    ```
    projecte/
    ├── codi/
    └── docs/
    ```
    Escriu, pas a pas, les ordres per: (a) entrar a `projecte`; (b) crear dins de `codi` un subdirectori `src`; (c) crear dins de `docs` un subdirectori `imatges`; (d) tornar a l'arrel de `projecte` i llistar-ne el contingut amb detall.

17. A **Windows**, tens la carpeta `C:\Alumnes\Grup1` amb 30 subcarpetes (una per alumne) i vols veure, en una sola ordre, totes les subcarpetes **i** el contingut de cadascuna. Quina ordre fas servir?

18. A **Linux**, estàs al directori `/home/anna` i vols moure el directori `notes`, que hi ha dins de `Documents/2023`, cap a `Documents/2024` — sense navegar-hi primer (una única ordre, des d'on ets ara). Escriu-la.

19. Tens dos directoris al mateix nivell, `clients_antics` i `clients` (a **Linux**). Vols que tot el contingut de `clients_antics` passi a dins de `clients`, i després esborrar `clients_antics` (que quedarà buit). Escriu les ordres necessàries, en ordre.

### D. Què fa aquesta ordre? / Troba l'error

20. Expliquen què fa exactament aquesta seqüència (Linux) i en quin estat queda el sistema de fitxers al final:
    ```bash
    mkdir -p a/b/c
    rmdir a
    ```
21. Un company ha escrit aquesta ordre a Windows i li dona error dient que el destí ja existeix:
    ```
    move C:\temp D:\temp
    ```
    Explica una causa probable de l'error i com es podria resoldre.
22. A Linux, algú executa `mv informe.txt carpeta/`. Explica els **dos** resultats possibles d'aquesta ordre, segons si `carpeta` ja existeix com a directori o no.

### E. Comprensió i comparativa

23. Explica, amb les teves paraules, per què a Linux no fa falta una ordre `rename` específica per a directoris, mentre que a Windows sí que n'hi ha una (`ren`).
24. Indica si són vertaderes (V) o falses (F):
    - `rm -r` esborra un directori encara que tingui contingut a dins. ___
    - A Windows, `rmdir` sol (sense `/s`) esborra un directori encara que no estigui buit. ___
    - `cd ..` et porta sempre a l'arrel del sistema de fitxers. ___
    - `ls -a` i `dir /a` fan, cada una en el seu sistema, una funció equivalent: mostrar els elements ocults. ___
25. Quina diferència hi ha entre fer `cd` sense res a Linux i fer `cd` sense res a Windows (CMD)?
