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

---

## Wo ist das Theme konfiguriert?

| Komponente | Datei |
|------------|-------|
| Qtile | `~/.config/qtile/config.py` |
| Alacritty | `~/.config/alacritty/alacritty.toml` |
| Rofi | `~/.config/rofi/config.rasi` |
| Dunst | `~/.config/dunst/dunstrc` |
| Starship | `~/.config/starship.toml` |

---

## Farben ändern

1. Farbpalette definieren (z.B. Catppuccin, Dracula, Nord)
2. Alle Config-Dateien anpassen
3. Komponenten neu laden

### Qtile neu laden
`Super + Ctrl + R`

### Dunst neu starten
```bash
pkill dunst && dunst &
```

---

## Transparenz

### Terminal (Alacritty)

```toml
[window]
opacity = 0.9
```

### Picom Blur

```conf
blur-method = "dual_kawase";
blur-strength = 5;
```

---

## Wallpaper ändern

```bash
feh --bg-fill ~/Pictures/wallpapers/neues-bild.jpg
```

---

## Beliebte Alternativen

| Theme | Stil |
|-------|------|
| Catppuccin | Warm, pastellig |
| Dracula | Lila Akzente |
| Nord | Kalt, arktisch |
| Gruvbox | Retro, warm |

---

## Weiter

Im nächsten Kapitel: [Tools](06-tools.md)
