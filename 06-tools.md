# Tools

> Dieses Kapitel erklärt die wichtigsten Tools im Detail: Rofi, Dunst, Picom und mehr.

---

## Rofi – Der App-Launcher

**Rofi** ist dein Startmenü-Ersatz. Damit startest du Programme, wechselst Fenster und mehr.

### Grundlegende Verwendung

| Tastenkürzel | Funktion |
|--------------|----------|
| `Super + R` | Programme starten |
| `Super + Tab` | Fenster wechseln |

### Modi

Rofi hat verschiedene Modi:

```bash
# Programme starten (drun = Desktop Run)
rofi -show drun

# Fenster wechseln
rofi -show window

# Befehle ausführen
rofi -show run

# SSH-Verbindungen
rofi -show ssh
```

### Konfiguration

Die Config liegt in `~/.config/rofi/config.rasi`:

```css
configuration {
    modi: "drun,window,run";
    show-icons: true;
    icon-theme: "Papirus";
    terminal: "alacritty";
    font: "JetBrainsMono Nerd Font 11";
}

/* Theme */
@theme "tokyo-night"
```

### Wichtige Optionen

```css
configuration {
    /* Anzahl der angezeigten Einträge */
    lines: 10;
    
    /* Spalten */
    columns: 1;
    
    /* Position: center, north, south, etc. */
    location: 0;
    
    /* Breite in Pixel oder Prozent */
    width: 600;
    
    /* Icons anzeigen */
    show-icons: true;
    
    /* Groß-/Kleinschreibung ignorieren */
    case-sensitive: false;
}
```

### Rofi-Scripts

Rofi kann eigene Scripts ausführen:

```bash
# WLAN-Manager (in diesem Setup enthalten)
rofi-wifi

# Power-Menü
rofi -show power-menu -modi power-menu:rofi-power-menu
```

---

## Dunst – Benachrichtigungen

**Dunst** zeigt Desktop-Benachrichtigungen an.

### Testen

```bash
# Test-Benachrichtigung senden
notify-send "Test" "Das ist eine Test-Nachricht"

# Mit Icon
notify-send -i firefox "Firefox" "Download abgeschlossen"

# Mit Dringlichkeit
notify-send -u critical "Fehler!" "Etwas ist schiefgelaufen"
```

### Konfiguration

Die Config liegt in `~/.config/dunst/dunstrc`:

```ini
[global]
    # Position: top-right, top-left, bottom-right, bottom-left
    origin = top-right
    
    # Abstand vom Bildschirmrand
    offset = 10x50
    
    # Breite
    width = 300
    
    # Maximale Höhe
    height = 300
    
    # Rahmendicke
    frame_width = 2
    
    # Schrift
    font = JetBrainsMono Nerd Font 10
    
    # Anzeigedauer (in ms)
    timeout = 5
    
    # Icons
    icon_theme = Papirus
    enable_recursive_icon_lookup = true
```

### Dringlichkeitsstufen

```ini
[urgency_low]
    background = "#24283b"
    foreground = "#c0caf5"
    frame_color = "#565f89"
    timeout = 3

[urgency_normal]
    background = "#24283b"
    foreground = "#c0caf5"
    frame_color = "#7aa2f7"
    timeout = 5

[urgency_critical]
    background = "#24283b"
    foreground = "#c0caf5"
    frame_color = "#f7768e"
    timeout = 0  # Bleibt bis zum Klick
```

### Tastenkürzel

| Aktion | Taste |
|--------|-------|
| Benachrichtigung schließen | Klick |
| Alle schließen | `Ctrl + Shift + Space` |
| Letzte wieder anzeigen | `Ctrl + ` ` |

### Dunst neu starten

```bash
pkill dunst && dunst &
```

---

## Picom – Compositor

**Picom** macht dein Desktop schick: Schatten, Transparenz, Blur, Animationen.

### Konfiguration

Die Config liegt in `~/.config/picom/picom.conf`:

```conf
# === SCHATTEN ===
shadow = true;
shadow-radius = 12;
shadow-opacity = 0.75;
shadow-offset-x = -12;
shadow-offset-y = -12;

# Fenster ohne Schatten
shadow-exclude = [
    "class_g = 'firefox' && argb",
    "class_g = 'Rofi'",
];

# === TRANSPARENZ ===
inactive-opacity = 0.95;
active-opacity = 1.0;
frame-opacity = 1.0;

# Transparenz pro Fenster
opacity-rule = [
    "90:class_g = 'Alacritty'",
    "100:class_g = 'firefox'",
];

# === BLUR ===
blur-method = "dual_kawase";
blur-strength = 5;
blur-background = true;

blur-background-exclude = [
    "class_g = 'firefox'",
];

# === ECKEN ===
corner-radius = 8;

# === ANIMATIONEN ===
# (Picom-Animationen erfordern picom-git aus dem AUR)

# === PERFORMANCE ===
vsync = true;
backend = "glx";
glx-no-stencil = true;
```

### Picom starten/stoppen

```bash
# Starten
picom &

# Mit Config
picom --config ~/.config/picom/picom.conf &

# Stoppen
pkill picom

# Neu starten
pkill picom && picom &
```

### Debugging

```bash
# Mit Logs starten
picom --config ~/.config/picom/picom.conf --log-level=debug

# Häufige Probleme:
# - Flackern: vsync = true; setzen
# - Langsam: backend = "glx"; verwenden
# - Artefakte: blur deaktivieren
```

---

## Feh – Wallpaper

**Feh** ist ein einfacher Bildbetrachter, der auch Wallpaper setzt.

### Wallpaper setzen

```bash
# Bild auf Bildschirmgröße skalieren
feh --bg-fill ~/Pictures/wallpapers/bild.jpg

# Bild zentrieren (mit schwarzem Rand)
feh --bg-center ~/Pictures/wallpapers/bild.jpg

# Bild kacheln
feh --bg-tile ~/Pictures/wallpapers/muster.png

# Bild strecken (verzerrt!)
feh --bg-scale ~/Pictures/wallpapers/bild.jpg
```

### Wallpaper beim Start

Feh speichert den letzten Befehl in `~/.fehbg`. Dieses Script wird beim Start ausgeführt.

In `~/.config/qtile/autostart.sh`:

```bash
~/.fehbg &
# Oder direkt:
feh --bg-fill ~/Pictures/wallpapers/current.png &
```

---

## Flameshot – Screenshots

**Flameshot** ist ein mächtiges Screenshot-Tool.

### Verwendung

| Tastenkürzel | Funktion |
|--------------|----------|
| `Print` | Screenshot-Modus starten |
| `Super + Print` | Direkt Auswahl |

### Im Screenshot-Modus

- **Ziehen:** Bereich auswählen
- **Werkzeugleiste:** Pfeile, Text, Markierungen hinzufügen
- **Enter:** Speichern
- **Ctrl + C:** In Zwischenablage
- **Esc:** Abbrechen

### Konfiguration

GUI starten:

```bash
flameshot config
```

Oder in `~/.config/flameshot/flameshot.ini`:

```ini
[General]
savePath=/home/carsten/Pictures/Screenshots
saveAsFileExtension=png
showDesktopNotification=true
```

---

## Thunar – Dateimanager

**Thunar** ist ein leichter grafischer Dateimanager.

### Starten

```bash
thunar &
# Oder: Super + E
```

### Nützliche Einstellungen

1. **Versteckte Dateien anzeigen:** `Ctrl + H`
2. **Terminal hier öffnen:** Rechtsklick → "Terminal hier öffnen"
3. **Als Root öffnen:** `sudo thunar`

### Custom Actions

Bearbeiten → Benutzerdefinierte Aktionen konfigurieren:

**Terminal hier öffnen:**
- Name: Terminal hier
- Befehl: `alacritty --working-directory %f`
- Erscheinungsbedingungen: Verzeichnisse

---

## Brightnessctl – Helligkeit

**Brightnessctl** steuert die Bildschirmhelligkeit.

```bash
# Aktuelle Helligkeit anzeigen
brightnessctl

# Helligkeit setzen (absolut)
brightnessctl set 50%

# Helligkeit erhöhen
brightnessctl set +10%

# Helligkeit verringern
brightnessctl set 10%-

# Maximale Helligkeit
brightnessctl set 100%
```

In Qtile-Keybindings:

```python
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
```

---

## Pavucontrol – Audio

**Pavucontrol** ist die grafische Oberfläche für PipeWire/PulseAudio.

```bash
pavucontrol &
```

### Tabs

- **Playback:** Laufende Audio-Streams
- **Recording:** Aufnahmen
- **Output Devices:** Lautsprecher/Kopfhörer
- **Input Devices:** Mikrofone
- **Configuration:** Gerätekonfiguration

### Kommandozeilen-Alternative

```bash
# Lautstärke anzeigen
wpctl get-volume @DEFAULT_AUDIO_SINK@

# Lautstärke setzen
wpctl set-volume @DEFAULT_AUDIO_SINK@ 50%

# Lauter/Leiser
wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+
wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-

# Mute togglen
wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
```

---

## Zusammenfassung: Tool-Dateien

| Tool | Config-Datei |
|------|--------------|
| Rofi | `~/.config/rofi/config.rasi` |
| Dunst | `~/.config/dunst/dunstrc` |
| Picom | `~/.config/picom/picom.conf` |
| Flameshot | `~/.config/flameshot/flameshot.ini` |
| Alacritty | `~/.config/alacritty/alacritty.toml` |

---

## Weiter

Im nächsten Kapitel: [Wartung](07-wartung.md) – Updates, Snapshots, Backups.
