# Tools

> Rofi, Dunst, Picom und mehr im Detail.

---

## Rofi – Der App-Launcher

| Tastenkürzel | Funktion |
|--------------|----------|
| `Super + R` | Programme starten |
| `Super + Tab` | Fenster wechseln |

Config: `~/.config/rofi/config.rasi`

---

## Dunst – Benachrichtigungen

```bash
# Test
notify-send "Test" "Nachricht"

# Neu starten
pkill dunst && dunst &
```

Config: `~/.config/dunst/dunstrc`

---

## Picom – Compositor

Effekte: Schatten, Transparenz, Blur

```bash
# Neu starten
pkill picom && picom &
```

Config: `~/.config/picom/picom.conf`

---

## Feh – Wallpaper

```bash
feh --bg-fill ~/Pictures/wallpapers/bild.jpg
```

---

## Flameshot – Screenshots

| Taste | Funktion |
|-------|----------|
| `Print` | Screenshot-Modus |
| `Super + Print` | Direkt Auswahl |

---

## Brightnessctl – Helligkeit

```bash
brightnessctl set +10%   # Heller
brightnessctl set 10%-   # Dunkler
```

---

## Pavucontrol – Audio

```bash
pavucontrol &
```

---

## Weiter

Im nächsten Kapitel: [Wartung](07-wartung.md)
