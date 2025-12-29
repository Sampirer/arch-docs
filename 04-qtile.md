# Qtile Grundlagen

> Dieses Kapitel erklärt, wie du Qtile bedienst – die wichtigsten Tastenkürzel, Layouts und wie du es anpassen kannst.

---

## Die Super-Taste (Mod)

Die **Super-Taste** (Windows-Taste) ist deine Haupttaste für Qtile. In der Konfiguration heißt sie `mod`.

```
┌───────┐
│ Super │  ← Diese Taste + andere Tasten = Qtile-Befehle
└───────┘
```

Fast alle Qtile-Befehle beginnen mit `Super + ...`.

---

## Wichtigste Tastenkürzel

### Programme starten

| Tastenkürzel | Aktion |
|--------------|--------|
| `Super + Return` | Terminal öffnen (Alacritty) |
| `Super + R` | Rofi Launcher (Programme suchen) |
| `Super + B` | Browser öffnen |

### Fenster steuern

| Tastenkürzel | Aktion |
|--------------|--------|
| `Super + Q` | Aktives Fenster schließen |
| `Super + H/L` | Fokus links/rechts |
| `Super + J/K` | Fokus hoch/runter |
| `Super + Shift + H/L` | Fenster verschieben |
| `Super + Shift + J/K` | Fenster in der Größe ändern |
| `Super + F` | Vollbild umschalten |
| `Super + Space` | Zwischen Layouts wechseln |

### Workspaces (Arbeitsflächen)

| Tastenkürzel | Aktion |
|--------------|--------|
| `Super + 1-9` | Zu Workspace 1-9 wechseln |
| `Super + Shift + 1-9` | Fenster zu Workspace 1-9 verschieben |

### System

| Tastenkürzel | Aktion |
|--------------|--------|
| `Super + Ctrl + R` | Qtile neu laden (nach Config-Änderung) |
| `Super + Ctrl + Q` | Qtile beenden (Logout) |

### Screenshots

| Tastenkürzel | Aktion |
|--------------|--------|
| `Print` | Screenshot (Flameshot) |
| `Super + Print` | Screenshot mit Auswahl |

---

## Layouts verstehen

Ein **Layout** bestimmt, wie Fenster angeordnet werden.

### MonadTall (Standard)

Das Standard-Layout. Ein großes Fenster links, der Rest rechts gestapelt.

```
┌─────────────────┬─────────┐
│                 │    2    │
│                 ├─────────┤
│       1         │    3    │
│    (Master)     ├─────────┤
│                 │    4    │
└─────────────────┴─────────┘
```

### MonadWide

Wie MonadTall, aber horizontal.

```
┌─────────────────────────────┐
│           1 (Master)        │
├─────────┬─────────┬─────────┤
│    2    │    3    │    4    │
└─────────┴─────────┴─────────┘
```

### Max

Jedes Fenster nutzt den ganzen Bildschirm. Wie Tabs.

```
┌─────────────────────────────┐
│                             │
│      Aktives Fenster        │
│       (Vollbild)            │
│                             │
└─────────────────────────────┘
[1] [2] [3] ← Andere Fenster versteckt
```

### Columns

Spalten, die du frei anpassen kannst.

```
┌─────────┬─────────┬─────────┐
│         │         │         │
│    1    │    2    │    3    │
│         │         │         │
└─────────┴─────────┴─────────┘
```

### Layout wechseln

- `Super + Space` – Nächstes Layout
- `Super + Shift + Space` – Vorheriges Layout

---

## Die Qtile Bar

Die Bar am oberen oder unteren Bildschirmrand zeigt wichtige Infos.

```
┌────────────────────────────────────────────────────────────┐
│ [1][2][3]...  │ Fenstertitel │     CPU │ RAM │ 🔊 │ 14:30 │
└────────────────────────────────────────────────────────────┘
  Workspaces      Aktives          Widgets         Uhrzeit
                  Fenster
```

### Widgets

- **GroupBox:** Workspaces (1-9)
- **WindowName:** Titel des aktiven Fensters
- **CPU/Memory:** Systemauslastung
- **Volume:** Lautstärke
- **Clock:** Uhrzeit
- **Systray:** Applet-Icons (Netzwerk, Bluetooth, etc.)

---

## Die Konfigurationsdatei

Die komplette Qtile-Konfiguration ist in einer Datei:

```
~/.config/qtile/config.py
```

### Struktur der Datei

```python
# 1. Imports
from libqtile import bar, layout, widget
from libqtile.config import Key, Group, Screen
from libqtile.lazy import lazy

# 2. Variablen
mod = "mod4"  # Super-Taste
terminal = "alacritty"

# 3. Keybindings
keys = [
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "q", lazy.window.kill()),
    # ... mehr Keybindings
]

# 4. Workspaces
groups = [Group(str(i)) for i in range(1, 10)]

# 5. Layouts
layouts = [
    layout.MonadTall(),
    layout.Max(),
    # ... mehr Layouts
]

# 6. Widgets & Bar
widget_defaults = dict(font="JetBrainsMono Nerd Font", fontsize=12)
screens = [
    Screen(top=bar.Bar([...], 24)),
]

# 7. Maus-Einstellungen
mouse = [...]

# 8. Sonstige Einstellungen
```

---

## Anpassungen vornehmen

### Beispiel 1: Neues Keybinding hinzufügen

```python
# In der keys-Liste hinzufügen:
keys = [
    # ... bestehende Keys
    
    # VS Code mit Super+C öffnen
    Key([mod], "c", lazy.spawn("code")),
    
    # Dateimanager mit Super+E
    Key([mod], "e", lazy.spawn("thunar")),
]
```

### Beispiel 2: Bar-Farben ändern

```python
# Tokyo Night Storm Farben
colors = {
    "bg": "#24283b",
    "fg": "#c0caf5",
    "blue": "#7aa2f7",
    "cyan": "#7dcfff",
    "red": "#f7768e",
}

screens = [
    Screen(
        top=bar.Bar(
            [...],
            background=colors["bg"],
        ),
    ),
]
```

### Beispiel 3: Anderes Terminal

```python
# Oben in der Datei:
terminal = "kitty"  # statt "alacritty"
```

---

## Nach Änderungen

Nach dem Bearbeiten der `config.py`:

```bash
# 1. Syntax prüfen (wichtig!)
python -m py_compile ~/.config/qtile/config.py

# 2. Wenn kein Fehler: Qtile neu laden
# Super + Ctrl + R
```

**Wichtig:** Immer zuerst die Syntax prüfen! Ein Fehler in der Config kann dazu führen, dass Qtile nicht mehr startet.

---

## Häufige Probleme

### "Qtile startet nicht nach Config-Änderung"

1. Zu TTY wechseln: `Ctrl + Alt + F2`
2. Einloggen
3. Config prüfen:
   ```bash
   python -m py_compile ~/.config/qtile/config.py
   ```
4. Fehler beheben
5. Zurück zum Desktop: `Ctrl + Alt + F1`

### "Keybinding funktioniert nicht"

1. Prüfe, ob das Programm installiert ist:
   ```bash
   which programm-name
   ```
2. Prüfe die Syntax in der Config
3. Qtile neu laden: `Super + Ctrl + R`

### "Widget zeigt nichts an"

Manche Widgets brauchen zusätzliche Pakete:
```bash
# Für Batterie-Widget
sudo pacman -S acpi

# Für Netzwerk-Widget
sudo pacman -S python-iwlib
```

---

## Weiter

Im nächsten Kapitel lernst du über [Theming](05-theming.md) – wie du Farben und das Aussehen anpasst.
