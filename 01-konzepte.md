# Konzepte für Einsteiger

> Dieses Kapitel erklärt die grundlegenden Konzepte, die du verstehen musst, bevor du mit diesem Setup arbeitest.

---

## Was ist der Unterschied zu Windows?

Auf Windows hast du einen **Desktop** mit Fenstern, die du frei verschieben kannst. Du klickst auf Icons, öffnest Programme aus dem Startmenü, und alles ist grafisch.

Auf Linux mit diesem Setup ist das anders:

| Windows | Dieses Setup |
|---------|--------------|
| Startmenü | Rofi (Launcher) |
| Explorer | Thunar + Terminal |
| Fenster verschieben mit Maus | Fenster werden automatisch angeordnet |
| Taskleiste | Qtile Bar |
| Einstellungen-App | Konfigurationsdateien (Text) |

**Wichtigster Unterschied:** Fast alles wird über die **Tastatur** gesteuert, nicht die Maus.

---

## Was ist ein Tiling Window Manager?

Ein **Tiling Window Manager** (TWM) ist ein Programm, das deine Fenster automatisch anordnet – wie Kacheln (englisch: "tiles").

### Vorteile

- **Kein Überlappen:** Jedes Fenster hat seinen Platz
- **Schnell:** Alles per Tastatur, keine Maus nötig
- **Effizient:** Maximale Bildschirmnutzung
- **Ressourcenschonend:** Viel weniger RAM als KDE/GNOME

### Wie sieht das aus?

```
┌─────────────────┬─────────────────┐
│                 │                 │
│    Terminal     │    Browser      │
│                 │                 │
│                 ├─────────────────┤
│                 │                 │
│                 │    Editor       │
│                 │                 │
└─────────────────┴─────────────────┘
```

Wenn du ein neues Fenster öffnest, werden die anderen automatisch kleiner, um Platz zu machen.

### Qtile

**Qtile** ist unser Tiling Window Manager. Er ist:

- In **Python** geschrieben (leicht anzupassen)
- Sehr **konfigurierbar**
- Gut **dokumentiert**

Die Konfiguration liegt in `~/.config/qtile/config.py`.

---

## Was ist Stow?

**GNU Stow** ist ein Symlink-Manager für Dotfiles.

### Das Problem

Linux-Programme speichern ihre Einstellungen in "Dotfiles" (Dateien, die mit `.` beginnen):

```
~/.bashrc           # Shell-Konfiguration
~/.config/qtile/    # Qtile-Konfiguration
~/.config/alacritty/ # Terminal-Konfiguration
```

Diese Dateien sind überall verstreut. Wie verwaltet man sie?

### Die Lösung: Stow

Stow sammelt alle Konfigurationen in **einem Ordner** und erstellt **Symlinks** (Verknüpfungen) zu den richtigen Stellen.

```
~/repos/dotfiles/           # Alle Configs an einem Ort
├── bash/
│   └── .bashrc            # → Symlink zu ~/.bashrc
├── qtile/
│   └── .config/qtile/
│       └── config.py      # → Symlink zu ~/.config/qtile/config.py
└── alacritty/
    └── .config/alacritty/
        └── alacritty.toml # → Symlink zu ~/.config/alacritty/alacritty.toml
```

### Vorteile

1. **Versionskontrolle:** Alles in einem Git-Repository
2. **Portabilität:** Auf neuem System: `git clone` + `stow` = fertig
3. **Übersicht:** Alle Configs an einem Ort

### Wie benutzt man Stow?

```bash
# In den Dotfiles-Ordner wechseln
cd ~/repos/dotfiles

# Ein Paket "stowen" (Symlinks erstellen)
stow bash

# Mehrere Pakete
stow bash qtile alacritty

# Alle Pakete
stow */
```

---

## Was sind Dotfiles?

**Dotfiles** sind Konfigurationsdateien, deren Namen mit einem Punkt (`.`) beginnen.

Der Punkt macht sie "versteckt" – `ls` zeigt sie nicht an, aber `ls -a` schon.

### Beispiele

| Datei | Zweck |
|-------|-------|
| `~/.bashrc` | Shell-Konfiguration (Aliases, Prompt, etc.) |
| `~/.gitconfig` | Git-Einstellungen (Name, E-Mail, Aliases) |
| `~/.config/` | Moderner Ort für App-Konfigurationen |

### Warum sind sie wichtig?

Dotfiles **definieren dein System**. Wenn du sie sicherst, kannst du dein exaktes Setup auf jedem Computer wiederherstellen.

---

## Was ist ein Compositor?

Ein **Compositor** (hier: Picom) ist ein Programm, das visuelle Effekte hinzufügt:

- **Transparenz:** Fenster können durchsichtig sein
- **Schatten:** Fenster werfen Schatten
- **Blur:** Unscharfer Hintergrund
- **Animationen:** Sanfte Übergänge

Ohne Compositor sieht alles "flach" aus. Mit Compositor wird es schick.

**Wichtig:** Der Compositor ist optional. Wenn er Probleme macht, kannst du ihn deaktivieren.

---

## Was ist X11 vs Wayland?

Beides sind **Display-Server** – sie kümmern sich darum, dass Fenster auf dem Bildschirm erscheinen.

| X11 | Wayland |
|-----|---------|
| Alt (1984!) | Neu (2012) |
| Sehr kompatibel | Bessere Performance |
| Mehr Software läuft | Manche Software fehlt noch |
| Dieses Setup | Zukunft |

**Dieses Setup nutzt X11**, weil:
- Qtile funktioniert damit zuverlässiger
- NVIDIA-Treiber sind besser
- Mehr Kompatibilität mit älteren Programmen

---

## Verzeichnisstruktur unter Linux

Windows hat `C:\Users\Name\`. Linux hat:

```
/                    # Root (wie C:\)
├── home/
│   └── carsten/     # Dein Home-Verzeichnis (~)
│       ├── .config/ # Konfigurationen
│       ├── .local/  # Lokale Daten & Programme
│       ├── repos/   # Git-Repositories
│       └── ...
├── etc/             # System-Konfigurationen
├── usr/             # Programme
└── ...
```

### Wichtige Pfade

| Pfad | Bedeutung |
|------|-----------|
| `~` | Dein Home-Verzeichnis (`/home/carsten`) |
| `~/.config/` | Deine App-Konfigurationen |
| `~/.local/bin/` | Deine eigenen Scripts |
| `/etc/` | System-weite Konfigurationen |

---

## Das Terminal

Das **Terminal** ist dein wichtigstes Werkzeug. Hier führst du Befehle aus.

### Wichtige Befehle

```bash
# Navigation
cd ~/repos          # In Ordner wechseln
cd ..               # Einen Ordner hoch
ls                  # Dateien auflisten
ls -la              # Mit versteckten Dateien + Details

# Dateien
cat datei.txt       # Datei anzeigen
nano datei.txt      # Datei bearbeiten (einfach)
vim datei.txt       # Datei bearbeiten (mächtig)

# System
sudo pacman -Syu    # System updaten
sudo pacman -S xyz  # Paket installieren
yay -S xyz          # AUR-Paket installieren

# Hilfe
man befehl          # Handbuch anzeigen
befehl --help       # Kurze Hilfe
```

### Unser Terminal: Alacritty

**Alacritty** ist ein schneller, GPU-beschleunigter Terminal-Emulator.

Wichtige Tastenkürzel:
- `Ctrl+Shift+C` – Kopieren
- `Ctrl+Shift+V` – Einfügen
- `Ctrl++` – Schrift größer
- `Ctrl+-` – Schrift kleiner

---

## Weiter

Jetzt kennst du die Grundlagen! Im nächsten Kapitel geht es um die [Installation](02-installation.md).
