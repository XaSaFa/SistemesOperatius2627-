# Publicar el repositori a GitHub

## 1. Crear el repositori remot

A GitHub, crea un repositori **buit** (sense README, sense .gitignore, sense LICENSE)
amb el nom que vulguis, per exemple `so-monolloc-mp0222`.

## 2. Pujar aquest contingut

Des d'una terminal, dins de la carpeta del repositori:

```powershell
cd "c:\Users\kalza\Documents\IABALLESTER\so-monolloc-mp0222"

git init -b main
git add .
git commit -m "Base de coneixements MP0222 · versió inicial"

git remote add origin https://github.com/EL-TEU-USUARI/so-monolloc-mp0222.git
git push -u origin main
```

Si fas servir SSH, canvia l'URL del `remote` per `git@github.com:EL-TEU-USUARI/so-monolloc-mp0222.git`.

## 3. (Opcional) Publicar el navegador amb GitHub Pages

`index.html` és autònom i es pot servir tal qual:

1. Repositori → **Settings** → **Pages**.
2. **Source:** `Deploy from a branch`.
3. **Branch:** `main` · carpeta `/ (root)` · **Save**.
4. Al cap d'un minut, el navegador serà a
   `https://EL-TEU-USUARI.github.io/so-monolloc-mp0222/`.

> Com que `index.html` porta tot el contingut incrustat, també funciona **obrint-lo
> amb doble clic** sense servidor ni connexió.

## 4. Mantenir-lo

Quan editis fitxers `.md`:

```powershell
python tools/gen_index.py          # regenera index.html
git add .
git commit -m "Descripció del canvi"
git push
```

## Notes

- Revisa el fitxer `LICENSE` (ara CC BY-NC-SA 4.0) i canvia'l si vols una altra llicència
  o si el repositori ha de ser **privat**.
- `.gitignore` ja exclou fitxers temporals, de sistema i d'editor.
- `.gitattributes` normalitza els finals de línia a LF i marca `index.html` com a fitxer generat.
