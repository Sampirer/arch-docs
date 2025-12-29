# Qtile Grundlagen

> Dieses Kapitel erklärt, wie du Qtile bedienst – die wichtigsten Tastenkürzel, Layouts und wie du es anpassen kannst.

---

## Die Super-Taste (Mod)

Die **Super-Taste** (Windows-Taste) ist deine Haupttaste für Qtile. In der Konfiguration heißt sie `mod`.

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

---

## Layouts verstehen

Ein **Layout** bestimmt, wie Fenster angeordnet werden.

### MonadTall (Standard)

Das Standard-Layout. Ein großes Fenster links, der Rest rechts gestapelt.

### MonadWide

Wie MonadTall, aber horizontal.

### Max

Jedes Fenster nutzt den ganzen Bildschirm. Wie Tabs.

### Layout wechseln

- `Super + Space` – Nächstes Layout
- `Super + Shift + Space` – Vorheriges Layout

---

## Die Konfigurationsdatei

Die komplette Qtile-Konfiguration ist in einer Datei:

```
~/.config/qtile/config.py
```

### Nach Änderungen

```bash
# 1. Syntax prüfen (wichtig!)
python -m py_compile ~/.config/qtile/config.py

# 2. Wenn kein Fehler: Qtile neu laden
# Super + Ctrl + R
```

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

---

## Weiter

Im nächsten Kapitel lernst du über [Theming](05-theming.md).
