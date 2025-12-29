# Erster Start

> Du hast Arch Linux installiert und sitzt vor dem Login-Bildschirm. Was nun?

---

## Der Login-Bildschirm (SDDM)

Nach dem Start siehst du SDDM – den Login-Manager.

```
┌─────────────────────────────────────┐
│                                     │
│      Willkommen auf archlinux       │
│                                     │
│      Benutzername: [________]       │
│      Passwort:     [________]       │
│                                     │
│      [Login]  [Shutdown]  [Reboot]  │
│                                     │
└─────────────────────────────────────┘
```

1. Gib deinen **Benutzernamen** ein
2. Gib dein **Passwort** ein
3. Drücke **Enter** oder klicke **Login**

---

## Die erste Minute in Qtile

Nach dem Login siehst du... fast nichts. Nur die Bar oben und einen leeren Bildschirm.

**Das ist normal!** Ein Tiling WM startet leer.

### Erste Schritte

1. **Terminal öffnen:** `Super + Return`
   
   Ein Terminal erscheint und füllt den Bildschirm.

2. **System updaten:**
   ```bash
   sudo pacman -Syu
   ```
   Gib dein Passwort ein (es wird nichts angezeigt beim Tippen – normal!).

3. **Zweites Fenster öffnen:** Nochmal `Super + Return`
   
   Jetzt siehst du das Tiling: Beide Terminals teilen sich den Platz.

4. **Zwischen Fenstern wechseln:** `Super + J` oder `Super + K`

5. **Fenster schließen:** `Super + Q`

---

## Wichtige erste Befehle

Öffne ein Terminal (`Super + Return`) und probiere:

```bash
# System-Info anzeigen
neofetch

# Festplattenplatz prüfen
df -h

# Installierte Pakete zählen
pacman -Q | wc -l

# Nach Paketen suchen
pacman -Ss suchbegriff

# Paket installieren
sudo pacman -S paketname
```

---

## Programme starten

### Mit Rofi (empfohlen)

`Super + R` öffnet den Rofi-Launcher:

```
┌─────────────────────────────────────┐
│ 🔍 [Suchbegriff eingeben]           │
├─────────────────────────────────────┤
│ > firefox                           │
│   thunar                            │
│   code                              │
│   alacritty                         │
└─────────────────────────────────────┘
```

1. Tippe den Namen des Programms
2. Drücke **Enter**

### Direkt mit Keybindings

| Tastenkürzel | Programm |
|--------------|----------|
| `Super + Return` | Terminal |
| `Super + B` | Browser |
| `Super + E` | Dateimanager |

### Im Terminal

```bash
firefox &        # & = im Hintergrund starten
thunar &
code &
```

---

## Die Qtile Bar verstehen

```
┌────────────────────────────────────────────────────────────┐
│ [1][2][3][4][5][6][7][8][9] │ Fenstertitel │ CPU │ 14:30  │
└────────────────────────────────────────────────────────────┘
```

### Workspaces [1] bis [9]

- Klicke auf eine Zahl = Wechsle zu diesem Workspace
- `Super + 1-9` = Wechsle per Tastatur
- `Super + Shift + 1-9` = Verschiebe Fenster dorthin

### Systray (rechts)

Hier erscheinen Icons für:
- Netzwerk (nm-applet)
- Bluetooth (blueman)
- Lautstärke

---

## Workspaces nutzen

Organisiere deine Arbeit mit Workspaces:

| Workspace | Nutzung |
|-----------|---------|
| 1 | Terminals |
| 2 | Browser |
| 3 | Code/Editor |
| 4 | Dateimanager |
| 5-9 | Frei |

**Beispiel-Workflow:**

1. `Super + 1` → Terminal für Befehle
2. `Super + 2` → Browser für Recherche
3. `Super + 3` → VS Code für Entwicklung
4. `Super + 1` → Schnell zurück zum Terminal

---

## Lautstärke und Helligkeit

### Lautstärke

Die meisten Tastaturen haben Lautstärke-Tasten. Falls nicht:

```bash
# Lautstärke-Steuerung öffnen
pavucontrol
```

### Bildschirmhelligkeit (Laptop)

```bash
# Heller
brightnessctl set +10%

# Dunkler
brightnessctl set 10%-
```

---

## WLAN verbinden (falls nicht automatisch)

1. **Netzwerk-Applet:** Klicke auf das Netzwerk-Icon im Systray

2. **Oder im Terminal:**
   ```bash
   # Verfügbare Netzwerke anzeigen
   nmcli device wifi list
   
   # Verbinden
   nmcli device wifi connect "NETZWERKNAME" password "PASSWORT"
   ```

3. **Oder mit Rofi-Script:**
   ```bash
   rofi-wifi
   ```

---

## Dateien finden

### Mit Thunar (grafisch)

`Super + E` oder:
```bash
thunar &
```

### Im Terminal

```bash
# Ins Home-Verzeichnis
cd ~

# Dateien auflisten
ls -la

# Ordner wechseln
cd Downloads

# Datei suchen
find ~ -name "*.pdf"
```

### Wichtige Orte

| Pfad | Inhalt |
|------|--------|
| `~/` | Dein Home-Verzeichnis |
| `~/Downloads/` | Downloads |
| `~/repos/` | Deine Git-Repositories |
| `~/.config/` | Konfigurationsdateien |

---

## Wenn etwas nicht funktioniert

### Problem: Kein Sound

```bash
# Audio-Service prüfen
systemctl --user status pipewire

# Neu starten
systemctl --user restart pipewire wireplumber
```

### Problem: Bildschirm-Auflösung falsch

```bash
# Verfügbare Auflösungen anzeigen
xrandr

# Auflösung setzen
xrandr --output HDMI-1 --mode 1920x1080
```

### Problem: Programm stürzt ab

1. Terminal öffnen: `Super + Return`
2. Programm manuell starten:
   ```bash
   firefox
   ```
3. Fehlermeldung lesen

---

## Snapshot erstellen (Backup!)

Nach dem ersten erfolgreichen Boot solltest du einen Snapshot erstellen:

```bash
sudo snapper -c root create -d "Erster erfolgreicher Boot"
```

Damit kannst du jederzeit zu diesem Zustand zurückkehren.

---

## Cheatsheet zum Ausdrucken

```
╔═══════════════════════════════════════════════════════════╗
║                    QTILE CHEATSHEET                       ║
╠═══════════════════════════════════════════════════════════╣
║  Super + Return     Terminal öffnen                       ║
║  Super + R          Rofi Launcher                         ║
║  Super + Q          Fenster schließen                     ║
║  Super + 1-9        Workspace wechseln                    ║
║  Super + Shift+1-9  Fenster verschieben                   ║
║  Super + H/J/K/L    Fokus ändern                          ║
║  Super + Space      Layout wechseln                       ║
║  Super + F          Vollbild                              ║
║  Super + Ctrl + R   Qtile neu laden                       ║
║  Super + Ctrl + Q   Ausloggen                             ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Weiter

Jetzt kennst du die Grundlagen! Als nächstes: [Qtile Grundlagen](04-qtile.md) für mehr Details.
