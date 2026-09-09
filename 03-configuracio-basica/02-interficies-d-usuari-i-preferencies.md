[⬅ Anterior: Arrencada i sessions](01-arrencada-parada-i-sessions.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Gestió de discos ➡](03-gestio-de-discos-i-sistemes-d-arxius.md)

# 2. Interfícies d'usuari i preferències de l'entorn

> Criteris d'avaluació RA3.1–RA3.2 — *Diferencia les interfícies d'usuari segons les seves propietats; aplica
> preferències en la configuració de l'entorn personal.* Repassa el [tema 6 de RA1](../01-caracteritzacio-dels-so/06-gestio-es-i-interficies.md).

## 2.1. Comparativa GUI vs. CLI

| Aspecte | GUI (gràfica) | CLI (línia d'ordres) |
|---|---|---|
| Corba d'aprenentatge | Baixa; exploratòria | Alta; cal conèixer les ordres |
| Velocitat en tasques repetitives | Lenta (molts clics) | Ràpida (una ordre, historial, scripts) |
| Automatització | Limitada | Total (scripts, tasques programades) |
| Consum de recursos | Alt | Mínim |
| Administració remota | Requereix escriptori remot / VNC | SSH, molt lleugera |
| Ús en servidors | Poc habitual | Habitual (instal·lació *sense escriptori*) |
| Feedback visual | Immediat | Textual |

Els SO actuals ofereixen **totes dues** i gairebé qualsevol acció de la GUI té equivalent per ordres
(`Configuració` ↔ `PowerShell`; `Configuració del GNOME` ↔ `gsettings`).

## 2.2. Elements de l'entorn gràfic

| Element | Windows 11 | GNOME (Ubuntu) | KDE Plasma |
|---|---|---|---|
| Barra de tasques / plafó | Barra de tasques + menú Inici | Plafó superior + *Dash* / Activitats | Plafó inferior + llançador |
| Àrea de notificació | *Safata del sistema* (baix a la dreta) | Indicadors (dalt a la dreta) | *System Tray* |
| Escriptoris virtuals | *Vista de tasques* (`Win+Tab`) | Espais de treball (`Super+Page Up/Down`) | Escriptoris d'activitat |
| Explorador de fitxers | Explorador de Windows | Fitxers (Nautilus) | Dolphin |
| Centre de configuració | *Configuració* / Tauler de control (llegat) | *Configuració* / GNOME Tweaks | *Configuració del sistema* |
| Canvi de finestra | `Alt+Tab` | `Alt+Tab` | `Alt+Tab` |

### Finestres i quadres de diàleg

- **Finestra:** barra de títol, botons minimitzar/maximitzar/tancar, barres de desplaçament, barra d'estat,
  panell de navegació.
- **Quadre de diàleg:** finestra petita que demana o informa (botons *D'acord*/*Cancel·la*, caselles, llistes).
- **Icones:** representen fitxers, carpetes, programes o **accessos directes / enllaços**. Operacions: obrir,
  copiar, retallar, canviar de nom, eliminar, propietats, crear accés directe/enllaç.

## 2.3. Personalització de l'entorn (preferències)

| Preferència | Windows | GNOME |
|---|---|---|
| Fons d'escriptori i tema clar/fosc | *Configuració → Personalització → Fons / Colors* | *Configuració → Fons* i *Aparença* |
| Resolució, escala i disposició de pantalles | *Sistema → Pantalla* | *Configuració → Pantalles* |
| Protector de pantalla / bloqueig automàtic | *Personalització → Pantalla de bloqueig* | *Privadesa → Bloqueig de pantalla* |
| Idioma i regió del sistema | *Hora i idioma → Idioma i regió* | *Configuració → Regió i idioma* |
| Disposició de teclat | *Hora i idioma → Escriptura* | *Regió i idioma → Fonts d'entrada* |
| Data, hora i zona horària | *Hora i idioma → Data i hora* | *Configuració → Data i hora* (`timedatectl`) |
| Accessibilitat (contrast, lupa, lector) | *Accessibilitat* | *Configuració → Accessibilitat* |
| So i dispositius de sortida | *Sistema → So* | *Configuració → So* |
| Energia (suspensió, brillantor) | *Sistema → Energia i bateria* | *Configuració → Energia* |
| Aplicacions per defecte (navegador, correu) | *Aplicacions → Aplicacions predeterminades* | *Configuració → Aplicacions predeterminades* |
| Programes que s'inicien amb la sessió | *Administrador de tasques → Aplicacions d'inici* | *GNOME Tweaks → Aplicacions en iniciar* |

### Personalització de carpetes / Explorador

- Windows: *Opcions de l'Explorador de fitxers* → mostrar extensions de fitxer, fitxers ocults, vista
  (icones/detalls), obrir amb un clic o dos.
- GNOME Fitxers: *Preferències* → vista (llista/icones), ordenació, mostrar fitxers ocults (`Ctrl+H`),
  columnes visibles, previsualitzacions.

## 2.4. Personalitzar l'entorn per línia d'ordres

- **Windows / PowerShell:** perfil `$PROFILE` (alias, funcions, prompt); variables d'entorn amb
  `setx` o *Configuració → Sistema → Aprofundir → Variables d'entorn*.
- **Linux / Bash:** fitxers `~/.bashrc`, `~/.bash_profile`, `~/.profile` (àlies, funcions, `PS1` per al prompt,
  `PATH`). Configuració del GNOME sense GUI: `gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'`.

```bash
alias ll='ls -alF'
alias ..='cd ..'
export EDITOR=nano
export PATH="$HOME/bin:$PATH"
```

## 2.5. Perfils i separació d'usuaris

Cada usuari té el seu **perfil** amb la seva configuració; el que un usuari canvia no afecta els altres. Windows:
`C:\Users\<usuari>` (i `C:\Users\Default` com a plantilla, `C:\Users\Public` per a dades comunes). Linux:
`/home/<usuari>` (i `/etc/skel` com a plantilla). Vegeu
[RA4 · usuaris i perfils](../04-administracio-del-so/01-usuaris-grups-i-contrasenyes.md).

## 2.6. Resum

- **GUI** = fàcil i visual; **CLI** = ràpida, lleugera i automatitzable. Els SO actuals tenen totes dues.
- L'entorn gràfic es compon de barra de tasques, àrea de notificació, escriptoris virtuals, explorador i
  centre de configuració.
- Les **preferències** (fons, tema, resolució, idioma, teclat, energia, aplicacions per defecte, aplicacions
  d'inici) es configuren des de *Configuració* (GUI) o amb `gsettings`/`setx`/`~/.bashrc` (CLI).
- Cada usuari té el seu **perfil**; els canvis no afecten els altres comptes.

## Comprova què has après

1. Dona tres avantatges de la CLI i tres de la GUI.
2. On configures les aplicacions que s'inicien amb la sessió a Windows i a GNOME?
3. Quin fitxer edites a Linux per definir àlies i el `PATH` del teu usuari?
4. On es guarda la plantilla per als perfils d'usuari nous a Windows i a Linux?
5. Com actives la vista de detalls i la visualització d'extensions de fitxer a l'Explorador de Windows?

---

[⬅ Anterior: Arrencada i sessions](01-arrencada-parada-i-sessions.md) · [Índex del bloc](00-index.md) · [🏠 Índex general](../README.md) · [Següent: Gestió de discos ➡](03-gestio-de-discos-i-sistemes-d-arxius.md)
