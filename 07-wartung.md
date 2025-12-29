# Wartung

> Dieses Kapitel erklärt, wie du dein System aktuell hältst, Backups machst und Probleme vermeidest.

---

## System-Updates

### Warum Updates wichtig sind

Arch Linux ist ein **Rolling Release** – es gibt keine großen Versions-Upgrades. Stattdessen kommen ständig kleine Updates. Regelmäßige Updates sind wichtig für:

- **Sicherheit:** Patches für Schwachstellen
- **Stabilität:** Bugfixes
- **Kompatibilität:** Abhängigkeiten bleiben aktuell

### Update-Routine

**Empfohlen:** Mindestens 1x pro Woche updaten.

```bash
# Vor jedem Update: Snapshot erstellen!
sudo snapper -c root create -d "Vor Update $(date +%Y-%m-%d)"

# System updaten
sudo pacman -Syu

# AUR-Pakete updaten
yay -Syu
```

### Vor dem Update: News lesen!

Manchmal erfordern Updates manuelle Eingriffe. **Immer vor großen Updates prüfen:**

- https://archlinux.org/news/
- `yay -Pw` zeigt ungelesene News

### Nach Problemen: Rollback

Falls ein Update etwas kaputt macht:

1. Neustart
2. Im GRUB-Menü: "Arch Linux Snapshots" wählen
3. Letzten guten Snapshot booten
4. Nach dem Boot:
   ```bash
   sudo snapper -c root rollback
   sudo reboot
   ```

---

## Snapper – Snapshots

**Snapper** erstellt automatische Backups deines Systems.

### Snapshots anzeigen

```bash
sudo snapper -c root list
```

Output:

```
 # | Type   | Pre # | Date                     | Description
---+--------+-------+--------------------------+-------------------
 0 | single |       |                          | current
 1 | single |       | 2024-12-20 10:00:00      | Vor Update
 2 | single |       | 2024-12-22 14:30:00      | Nach Desktop-Setup
```

### Manuellen Snapshot erstellen

```bash
# Mit Beschreibung
sudo snapper -c root create -d "Beschreibung hier"

# Beispiele:
sudo snapper -c root create -d "Vor NVIDIA-Treiber"
sudo snapper -c root create -d "Funktionierendes System"
```

### Automatische Snapshots

Snapper erstellt automatisch Snapshots bei pacman-Aktionen (dank `snap-pac`):

- **Pre-Snapshot:** Vor jeder Installation/Update
- **Post-Snapshot:** Nach jeder Installation/Update

### Snapshot löschen

```bash
# Einzelnen Snapshot löschen
sudo snapper -c root delete <nummer>

# Alte Snapshots aufräumen (behält die letzten 10)
sudo snapper -c root cleanup number
```

### Dateien aus Snapshot wiederherstellen

```bash
# Snapshot mounten
sudo mount -o subvol=@snapshots/<nummer>/snapshot /mnt

# Datei kopieren
cp /mnt/pfad/zur/datei ~/

# Unmounten
sudo umount /mnt
```

### Komplett zu Snapshot zurückkehren

```bash
# Zu Snapshot booten (GRUB-Menü)
# Dann:
sudo snapper -c root rollback
sudo reboot
```

---

## Paket-Management

### Pakete suchen

```bash
# In offiziellen Repos
pacman -Ss suchbegriff

# Im AUR
yay -Ss suchbegriff
```

### Pakete installieren

```bash
# Offizielles Paket
sudo pacman -S paketname

# AUR-Paket
yay -S paketname
```

### Pakete entfernen

```bash
# Paket entfernen
sudo pacman -R paketname

# Paket + ungenutzte Abhängigkeiten
sudo pacman -Rs paketname

# Paket + Config-Dateien + Abhängigkeiten
sudo pacman -Rns paketname
```

### Verwaiste Pakete finden

```bash
# Verwaiste Pakete anzeigen
pacman -Qtdq

# Verwaiste Pakete entfernen
sudo pacman -Rns $(pacman -Qtdq)
```

### Paket-Cache aufräumen

```bash
# Cache-Größe anzeigen
du -sh /var/cache/pacman/pkg/

# Alte Versionen löschen (behält letzte 3)
sudo paccache -r

# Alles außer installierte löschen
sudo pacman -Sc
```

---

## Speicherplatz verwalten

### Speicherplatz prüfen

```bash
# Übersicht
df -h

# Detailliert (pro Ordner)
du -sh /* 2>/dev/null | sort -h

# Große Dateien finden
find / -size +100M -type f 2>/dev/null
```

### Speicherfresser

| Ort | Was | Aufräumen |
|-----|-----|-----------|
| `/var/cache/pacman/pkg/` | Paket-Cache | `sudo paccache -r` |
| `~/.cache/` | User-Cache | `rm -rf ~/.cache/*` |
| `/var/log/` | Log-Dateien | `sudo journalctl --vacuum-time=7d` |
| `~/.local/share/Trash/` | Papierkorb | Leeren |

### Journal aufräumen

```bash
# Journal-Größe anzeigen
journalctl --disk-usage

# Nur letzte 7 Tage behalten
sudo journalctl --vacuum-time=7d

# Nur 500MB behalten
sudo journalctl --vacuum-size=500M
```

---

## Dotfiles-Backup

### Änderungen committen

```bash
cd ~/repos/dotfiles
git status

# Alle Änderungen hinzufügen
git add -A

# Committen
git commit -m "Update: Beschreibung der Änderungen"

# Pushen
git push
```

### Regelmäßig synchronisieren

```bash
# Mit dem dotfiles-sync Script
dotfiles-sync status
```

---

## System-Gesundheit prüfen

### Schneller Check

```bash
# Mit dem system-check Script (falls installiert)
system-check
```

### Manueller Check

```bash
# 1. Festplatte
df -h /

# 2. RAM
free -h

# 3. Fehlgeschlagene Services
systemctl --failed

# 4. Journal-Fehler
journalctl -p err -b

# 5. Pacman-Probleme
sudo pacman -Dk
```

### Dateisystem prüfen

**Wichtig:** Nur bei ausgehängtem Dateisystem oder im Live-System!

```bash
# Btrfs prüfen
sudo btrfs scrub start /
sudo btrfs scrub status /
```

---

## Typische Wartungsaufgaben

### Wöchentlich

- [ ] System updaten: `sudo pacman -Syu && yay -Syu`
- [ ] Dotfiles committen
- [ ] Snapshot erstellen

### Monatlich

- [ ] Paket-Cache aufräumen: `sudo paccache -r`
- [ ] Journal aufräumen: `sudo journalctl --vacuum-time=30d`
- [ ] Verwaiste Pakete entfernen
- [ ] ~/.cache/ prüfen

### Bei Bedarf

- [ ] Alte Snapshots löschen
- [ ] Große Dateien finden und aufräumen
- [ ] Btrfs scrub durchführen

---

## Troubleshooting-Checkliste

### System bootet nicht

1. Zu Snapshot booten (GRUB)
2. Problem identifizieren
3. Rollback oder Fix

### Paket-Konflikte

```bash
# Datenbank reparieren
sudo pacman -Dk
sudo pacman -Syy
```

### Service startet nicht

```bash
# Status prüfen
systemctl status servicename

# Logs anzeigen
journalctl -u servicename -b

# Neu starten
sudo systemctl restart servicename
```

### Grafik-Probleme nach Update

1. Zu TTY wechseln: `Ctrl + Alt + F2`
2. Treiber neu installieren
3. Oder zu Snapshot zurück

---

## Automatisierung

### Update-Reminder

Cron-Job für wöchentliche Erinnerung:

```bash
crontab -e
```

```
0 10 * * 1 notify-send "System-Update" "Zeit für: sudo pacman -Syu"
```

### Automatische Snapshots

Snapper-Timer aktivieren:

```bash
sudo systemctl enable --now snapper-timeline.timer
sudo systemctl enable --now snapper-cleanup.timer
```

---

## Weiter

Bei Problemen: [Problemlösung](08-problemloesung.md)
