# Com contribuir

Aquest repositori és material didàctic del mòdul **MP0222 · Sistemes operatius monolloc** (SMX).

## Estructura

- Una **carpeta numerada per resultat d'aprenentatge** (`01-…` → RA1, `04-…` → RA4, etc.).
- Dins de cada carpeta:
  - `00-index.md` — índex del bloc, relaciona els temes amb els **criteris d'avaluació**.
  - `NN-nom-del-tema.md` — un fitxer per tema.
- `00-referencia/` — currículum oficial, glossari i bibliografia.
- `index.html` — navegador offline **generat**; no s'edita a mà.
- `tools/gen_index.py` — regenera `index.html` a partir dels `.md`.

## Convencions

- **Idioma:** català. To didàctic, adreçat a alumnat de grau mitjà.
- **Noms de fitxer:** `kebab-case`, sense accents ni espais, amb prefix numèric de dos dígits.
- **Cada tema comença amb un `# Títol`** (és el que apareix a la barra lateral del navegador).
- **Barra de navegació** a dalt i a baix del tema: `Anterior · Índex del bloc · Índex general · Següent`.
- **Enllaços interns:** rutes relatives acabades en `.md`
  (p. ex. `[permisos](../01-caracteritzacio-dels-so/08-arxius-directoris-atributs-i-permisos.md)`).
  El navegador els converteix en navegació interna.
- **Vigència tècnica:** Windows 10/11, `systemd`, `ext4`/`exFAT`/`Btrfs`, eines actuals.
  El contingut històric amb valor formatiu (FAT, MBR, `init`…) es conserva i s'etiqueta com a llegat.
- Tanca cada tema amb una secció **«Comprova què has après»** (preguntes lligades als criteris d'avaluació).

## Després d'editar

Si afegeixes, edites, reanomenes o reordenes fitxers `.md`, **regenera el navegador**:

```bash
python tools/gen_index.py
```

Fes commit del `.md` i de l'`index.html` resultant a la mateixa comissió.

## Flux de treball

1. Crea una branca: `git switch -c tema/descripcio-curta`.
2. Fes els canvis i regenera `index.html`.
3. Obre una *pull request* amb un resum del que canvia i per què.
