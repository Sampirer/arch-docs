# Problemlösung

> Häufige Probleme und Lösungen.

---

## Notfall: Qtile startet nicht

1. `Ctrl + Alt + F2` (TTY)
2. Einloggen
3. `python -m py_compile ~/.config/qtile/config.py`
4. Fehler beheben
5. `Ctrl + Alt + F1` zurück

---

## Zu Snapshot zurück

1. GRUB → "Arch Linux Snapshots"
2. Snapshot wählen
3. Nach Boot: `sudo snapper -c root rollback && sudo reboot`

---

## Kein Sound

```bash
systemctl --user restart pipewire wireplumber
pavucontrol  # Ausgabegerät prüfen
```

---

## Kein WLAN

```bash
nmcli device wifi list
nmcli device wifi connect "SSID" password "PASS"
```

---

## Falsche Auflösung

```bash
xrandr  # Optionen anzeigen
xrandr --output HDMI-1 --mode 1920x1080
```

---

## Paket-Probleme

```bash
sudo pacman -Dk      # Datenbank prüfen
sudo pacman -Syy     # Neu synchronisieren
```

---

## Service startet nicht

```bash
systemctl status servicename
journalctl -u servicename -b
sudo systemctl restart servicename
```

---

## Logs lesen

```bash
journalctl -b              # Aktueller Boot
journalctl -p err -b       # Nur Fehler
cat ~/.local/share/qtile/qtile.log
```

---

## Hilfe finden

- **Arch Wiki:** https://wiki.archlinux.org
- **Forum:** https://bbs.archlinux.org
- **Reddit:** r/archlinux, r/qtile
