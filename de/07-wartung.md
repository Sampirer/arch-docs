# Wartung

> Updates, Snapshots und Backups.

---

## System-Updates

```bash
# Vor Update: Snapshot!
sudo snapper -c root create -d "Vor Update"

# System updaten
sudo pacman -Syu

# AUR-Pakete
yay -Syu
```

**Wichtig:** Vor Updates https://archlinux.org/news/ lesen!

---

## Snapper Snapshots

```bash
# Anzeigen
sudo snapper -c root list

# Erstellen
sudo snapper -c root create -d "Beschreibung"

# Rollback (nach Boot in Snapshot)
sudo snapper -c root rollback
```

---

## Paket-Management

```bash
# Suchen
pacman -Ss suchbegriff

# Installieren
sudo pacman -S paketname

# Entfernen (+ Abhängigkeiten)
sudo pacman -Rns paketname

# Verwaiste Pakete entfernen
sudo pacman -Rns $(pacman -Qtdq)
```

---

## Aufräumen

```bash
# Paket-Cache (behält letzte 3)
sudo paccache -r

# Journal (letzte 7 Tage)
sudo journalctl --vacuum-time=7d
```

---

## Dotfiles sichern

```bash
cd ~/repos/dotfiles
git add -A
git commit -m "Update"
git push
```

---

## Wöchentliche Routine

- [ ] `sudo pacman -Syu && yay -Syu`
- [ ] Dotfiles committen
- [ ] Snapshot erstellen

---

## Weiter

Bei Problemen: [Problemlösung](08-problemloesung.md)
