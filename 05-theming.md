# Theming

> Dieses Kapitel erklärt das Tokyo Night Storm Theme und wie du Farben anpassen kannst.

---

## Das Tokyo Night Storm Theme

Dieses Setup verwendet **Tokyo Night Storm** – ein dunkles Theme mit sanften, kühlen Farben.

### Farbpalette

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Background | `#24283b` | Hintergrund überall |
| Foreground | `#c0caf5` | Normaler Text |
| Blue | `#7aa2f7` | Akzentfarbe, Links |
| Cyan | `#7dcfff` | Hervorhebungen |
| Green | `#9ece6a` | Erfolg, Git-Adds |
| Red | `#f7768e` | Fehler, Git-Deletes |
| Purple | `#bb9af7` | Keywords |
| Yellow | `#e0af68` | Warnungen |
| Black | `#1a1b26` | Dunklerer Hintergrund |
| Gray | `#565f89` | Kommentare, inaktiv |

---

## Wo ist das Theme konfiguriert?

Das Theme ist an mehreren Stellen definiert:

| Komponente | Datei | Was wird gestylt? |
|------------|-------|-------------------|
| Qtile | `~/.config/qtile/config.py` | Bar, Fensterrahmen |
| Alacritty | `~/.config/alacritty/alacritty.toml` | Terminal-Farben |
| Rofi | `~/.config/rofi/config.rasi` | Launcher |
| Dunst | `~/.config/dunst/dunstrc` | Benachrichtigungen |
| Starship | `~/.config/starship.toml` | Shell-Prompt |
| GRUB | `/boot/grub/themes/tokyo-night/` | Boot-Menü |
| SDDM | `/usr/share/sddm/themes/tokyo-night/` | Login-Screen |

---

## Farben ändern

### Schritt 1: Farbpalette definieren

Erstelle eine zentrale Farbdefinition in deinem Kopf oder einer Notiz:

```
# Beispiel: Catppuccin Mocha
bg      = #1e1e2e
fg      = #cdd6f4
blue    = #89b4fa
cyan    = #94e2d5
green   = #a6e3a1
red     = #f38ba8
purple  = #cba6f7
yellow  = #f9e2af
```

### Schritt 2: Qtile anpassen

Öffne `~/.config/qtile/config.py` und finde den Farben-Abschnitt:

```python
# === FARBEN (Tokyo Night Storm) ===
colors = {
    "bg":        "#24283b",  # Hintergrund
    "fg":        "#c0caf5",  # Vordergrund
    "black":     "#1a1b26",  # Dunkler
    "red":       "#f7768e",  # Rot
    "green":     "#9ece6a",  # Grün
    "yellow":    "#e0af68",  # Gelb
    "blue":      "#7aa2f7",  # Blau
    "purple":    "#bb9af7",  # Lila
    "cyan":      "#7dcfff",  # Cyan
    "white":     "#a9b1d6",  # Weiß
    "gray":      "#565f89",  # Grau
}
```

Ändere die Hex-Werte auf dein neues Theme.

### Schritt 3: Alacritty anpassen

Öffne `~/.config/alacritty/alacritty.toml`:

```toml
[colors.primary]
background = "#24283b"
foreground = "#c0caf5"

[colors.normal]
black   = "#1a1b26"
red     = "#f7768e"
green   = "#9ece6a"
yellow  = "#e0af68"
blue    = "#7aa2f7"
magenta = "#bb9af7"
cyan    = "#7dcfff"
white   = "#a9b1d6"

[colors.bright]
black   = "#565f89"
red     = "#f7768e"
green   = "#9ece6a"
yellow  = "#e0af68"
blue    = "#7aa2f7"
magenta = "#bb9af7"
cyan    = "#7dcfff"
white   = "#c0caf5"
```

### Schritt 4: Rofi anpassen

Öffne `~/.config/rofi/config.rasi`:

```css
* {
    bg:     #24283b;
    fg:     #c0caf5;
    accent: #7aa2f7;
    urgent: #f7768e;
}
```

### Schritt 5: Dunst anpassen

Öffne `~/.config/dunst/dunstrc`:

```ini
[global]
frame_color = "#7aa2f7"

[urgency_low]
background = "#24283b"
foreground = "#c0caf5"

[urgency_normal]
background = "#24283b"
foreground = "#c0caf5"
frame_color = "#7aa2f7"

[urgency_critical]
background = "#24283b"
foreground = "#c0caf5"
frame_color = "#f7768e"
```

### Schritt 6: Änderungen anwenden

```bash
# Qtile neu laden
# Super + Ctrl + R

# Dunst neu starten
pkill dunst && dunst &

# Alacritty: Schließen und neu öffnen
```

---

## Transparenz einstellen

### Terminal-Transparenz (Alacritty)

In `~/.config/alacritty/alacritty.toml`:

```toml
[window]
opacity = 0.9  # 1.0 = undurchsichtig, 0.0 = komplett durchsichtig
```

### Qtile Bar Transparenz

In `~/.config/qtile/config.py`:

```python
screens = [
    Screen(
        top=bar.Bar(
            [...],
            background="#24283b",  # Für Transparenz: "#24283bCC"
            # Die letzten 2 Zeichen (CC) = Alpha-Wert
            # 00 = transparent, FF = undurchsichtig
        ),
    ),
]
```

---

## Picom Effekte

Der Compositor (Picom) steuert Effekte wie Blur und Schatten.

### Blur aktivieren/deaktivieren

In `~/.config/picom/picom.conf`:

```conf
# Blur aktivieren
blur-method = "dual_kawase";
blur-strength = 5;

# Blur deaktivieren
# blur-method = "none";
```

### Schatten anpassen

```conf
shadow = true;
shadow-radius = 12;
shadow-opacity = 0.75;
shadow-offset-x = -12;
shadow-offset-y = -12;
```

### Transparenz für bestimmte Fenster

```conf
opacity-rule = [
    "90:class_g = 'Alacritty'",
    "95:class_g = 'Code'",
    "100:class_g = 'firefox'"
];
```

### Picom neu starten

```bash
pkill picom && picom &
```

---

## Schriftarten

### Installierte Schriften

```bash
# Verfügbare Schriften anzeigen
fc-list | grep -i "nerd\|jetbrains\|awesome"
```

### Schrift in Qtile ändern

```python
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
)
```

### Schrift in Alacritty ändern

```toml
[font]
size = 11.0

[font.normal]
family = "JetBrainsMono Nerd Font"
style = "Regular"
```

### Neue Schriften installieren

```bash
# Nerd Fonts
sudo pacman -S ttf-jetbrains-mono-nerd ttf-firacode-nerd

# Google Fonts
yay -S ttf-roboto ttf-opensans

# Font-Cache aktualisieren
fc-cache -fv
```

---

## Wallpaper

### Aktuelles Wallpaper

Das Wallpaper wird in `~/.config/qtile/autostart.sh` gesetzt:

```bash
feh --bg-fill ~/Pictures/wallpapers/current.png &
```

### Wallpaper ändern

```bash
# Neues Wallpaper setzen
feh --bg-fill ~/Pictures/wallpapers/neues-bild.jpg

# Permanent: Symlink aktualisieren
ln -sf ~/Pictures/wallpapers/neues-bild.jpg ~/Pictures/wallpapers/current.png
```

### Wallpaper finden

- https://wallhaven.cc
- https://unsplash.com
- r/unixporn auf Reddit

---

## Beliebte Theme-Alternativen

| Theme | Stil | Link |
|-------|------|------|
| Catppuccin | Warm, pastellig | catppuccin.com |
| Dracula | Lila Akzente | draculatheme.com |
| Nord | Kalt, arktisch | nordtheme.com |
| Gruvbox | Retro, warm | github.com/morhetz/gruvbox |
| One Dark | Atom-inspiriert | – |

Für die meisten Themes gibt es fertige Configs für Alacritty, Rofi, etc.

---

## Checkliste: Theme komplett ändern

- [ ] Qtile colors dict anpassen
- [ ] Alacritty colors anpassen
- [ ] Rofi Farben anpassen
- [ ] Dunst Farben anpassen
- [ ] Starship (optional)
- [ ] Neues Wallpaper (passend zum Theme)
- [ ] Alle Komponenten neu laden

---

## Weiter

Im nächsten Kapitel: [Tools](06-tools.md) – Rofi, Dunst, Picom im Detail.
