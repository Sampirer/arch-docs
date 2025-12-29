# Problemlösung

> Hier findest du Lösungen für häufige Probleme. Keine Panik – die meisten Probleme sind schnell behoben!

---

## 🔥 Notfall: Ich komme nicht mehr rein!

### Qtile startet nicht (schwarzer Bildschirm nach Login)

1. **Zu TTY wechseln:** `Ctrl + Alt + F2`
2. **Einloggen** mit deinem Benutzernamen und Passwort
3. **Config prüfen:**
   ```bash
   python -m py_compile ~/.config/qtile/config.py
   ```
4. **Fehler zeigt an welche Zeile:** Behebe den Fehler
5. **Zurück zum Login:** `Ctrl + Alt + F1`
6. **Neu einloggen**

### System bootet nicht mehr

1. **Arch ISO booten** (USB-Stick)
2. **Partitionen mounten:**
   ```bash
   mount /dev/nvme0n1p3 /mnt -o subvol=@
   ```
3. **Chroot:**
   ```bash
   arch-chroot /mnt
   ```
4. **Problem beheben** (Paket neu installieren, Config reparieren)
5. **Reboot:**
   ```bash
   exit
   reboot
   ```

### Zu einem Snapshot zurückkehren

1. **Im GRUB-Menü:** "Arch Linux Snapshots" wählen
2. **Snapshot auswählen** und booten
3. **Nach dem Boot:**
   ```bash
   sudo snapper -c root rollback
   sudo reboot
   ```

---

## Grafik-Probleme

### Bildschirm bleibt schwarz

**NVIDIA-Laptop:**
```bash
# Kernel-Parameter prüfen
cat /proc/cmdline | grep nvidia

# Falls fehlt, zu TTY wechseln und fixen:
sudo nano /etc/default/grub
# GRUB_CMDLINE_LINUX_DEFAULT="nvidia-drm.modeset=1 quiet"
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### Falsche Auflösung

```bash
# Verfügbare Auflösungen zeigen
xrandr

# Auflösung setzen
xrandr --output HDMI-1 --mode 1920x1080 --rate 60

# Permanent machen: In ~/.xinitrc vor `exec qtile start`:
xrandr --output HDMI-1 --mode 1920x1080
```

### Multi-Monitor funktioniert nicht

```bash
# Monitore erkennen
xrandr --auto

# Zweiten Monitor rechts
xrandr --output HDMI-1 --right-of eDP-1 --auto

# Oder mit arandr (grafisches Tool)
sudo pacman -S arandr
arandr
```

### Picom (Compositor) macht Probleme

```bash
# Picom beenden
pkill picom

# Ohne Picom arbeiten, dann Config testen:
picom --config ~/.config/picom/picom.conf

# Häufige Fixes:
# In picom.conf vsync ausschalten:
# vsync = false;
```

---

## Audio-Probleme

### Kein Sound

```bash
# 1. Pipewire-Status prüfen
systemctl --user status pipewire wireplumber

# 2. Falls nicht läuft, starten
systemctl --user start pipewire wireplumber

# 3. Audio-Geräte prüfen
wpctl status

# 4. Lautstärke prüfen (nicht auf Mute?)
pavucontrol
```

### Falsches Audio-Gerät

```bash
# Geräte auflisten
wpctl status

# Standard-Ausgabe setzen (ID aus wpctl status)
wpctl set-default <id>

# Oder in pavucontrol: Rechtsklick auf Gerät → "Als Standard setzen"
```

### Bluetooth-Audio

```bash
# Bluetooth-Service prüfen
systemctl status bluetooth

# Bluetooth-Manager öffnen
blueman-manager

# Gerät koppeln und verbinden
# Dann in pavucontrol als Ausgabe wählen
```

---

## Netzwerk-Probleme

### Kein WLAN

```bash
# 1. Interface prüfen
ip link show

# 2. WLAN aktivieren
sudo ip link set wlan0 up

# 3. NetworkManager Status
systemctl status NetworkManager

# 4. Neu starten
sudo systemctl restart NetworkManager

# 5. Verbinden
nmcli device wifi list
nmcli device wifi connect "SSID" password "PASSWORT"
```

### Kein Internet trotz Verbindung

```bash
# DNS prüfen
cat /etc/resolv.conf

# Falls leer, temporär fixen:
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

# Permanent: NetworkManager DNS nutzen
sudo systemctl restart NetworkManager
```

---

## Paket-Probleme

### "Paket nicht gefunden"

```bash
# 1. Paketdatenbank aktualisieren
sudo pacman -Sy

# 2. Suchen
pacman -Ss paketname

# 3. Falls im AUR:
yay -S paketname
```

### "Konflikt mit anderem Paket"

```bash
# Konflikt-Paket entfernen und neues installieren
sudo pacman -S neues-paket --overwrite '*'

# Oder manuell entfernen
sudo pacman -Rns altes-paket
sudo pacman -S neues-paket
```

### "Signatur ungültig"

```bash
# Schlüssel aktualisieren
sudo pacman-key --refresh-keys

# Oder Schlüsselbund neu initialisieren
sudo pacman-key --init
sudo pacman-key --populate archlinux
```

### Nach Update: System kaputt

```bash
# 1. Zu Snapshot booten (GRUB-Menü)
# 2. Nach dem Boot:
sudo snapper -c root rollback
sudo reboot

# 3. Dann prüfen was das Update kaputt gemacht hat:
# Arch News lesen: https://archlinux.org/news/
```

---

## Qtile-Probleme

### Keybinding funktioniert nicht

1. **Programm installiert?**
   ```bash
   which programmname
   ```

2. **Syntax korrekt?**
   ```bash
   python -m py_compile ~/.config/qtile/config.py
   ```

3. **Qtile neu laden:** `Super + Ctrl + R`

4. **Konflikt mit anderem Programm?**
   Manche Programme fangen Keys ab (z.B. VS Code)

### Widget zeigt "N/A" oder nichts

```bash
# Abhängigkeiten installieren
sudo pacman -S python-psutil python-iwlib acpi

# Qtile neu laden
# Super + Ctrl + R
```

### Bar erscheint nicht

```bash
# Qtile-Log prüfen
cat ~/.local/share/qtile/qtile.log

# Häufiger Fehler: Font nicht installiert
sudo pacman -S ttf-jetbrains-mono-nerd
```

---

## Stow-Probleme

### "Cannot stow X: existing target is not owned"

Das bedeutet: Die Datei existiert bereits und ist kein Symlink.

```bash
# Lösung 1: Backup und löschen
mv ~/.config/alacritty ~/.config/alacritty.bak
cd ~/repos/dotfiles
stow alacritty

# Lösung 2: Mit --adopt (übernimmt existierende Datei)
stow --adopt alacritty
# WICHTIG: Danach git diff prüfen!
```

### "Conflict: X vs Y"

Zwei Pakete wollen dieselbe Datei erstellen.

```bash
# Prüfen welches Paket was enthält
ls -la ~/repos/dotfiles/paket1/
ls -la ~/repos/dotfiles/paket2/

# Konflikt manuell auflösen
```

---

## System-Check Script

Ein schneller Health-Check:

```bash
system-check
```

Oder manuell:

```bash
# 1. Festplatte
df -h /

# 2. RAM
free -h

# 3. Services
systemctl --failed

# 4. Journal-Fehler
journalctl -p err -b

# 5. Pacman-Probleme
sudo pacman -Dk
```

---

## Logs lesen

Die wichtigsten Log-Orte:

```bash
# System-Log (aktueller Boot)
journalctl -b

# Nur Fehler
journalctl -p err -b

# Qtile-Log
cat ~/.local/share/qtile/qtile.log

# Xorg-Log (Grafik)
cat /var/log/Xorg.0.log

# Live-Log (folgen)
journalctl -f
```

---

## Hilfe bekommen

### 1. Arch Wiki

**Beste Ressource überhaupt:** https://wiki.archlinux.org

Suche dort nach deinem Problem – es gibt fast immer einen Artikel.

### 2. Fehlermeldung googlen

```
site:reddit.com archlinux "deine fehlermeldung"
site:bbs.archlinux.org "deine fehlermeldung"
```

### 3. Forum / Reddit

- Arch Linux Forum: https://bbs.archlinux.org
- Reddit: https://reddit.com/r/archlinux
- Reddit: https://reddit.com/r/qtile

**Bevor du fragst:**
1. Problem genau beschreiben
2. Fehlermeldung posten
3. Was du schon versucht hast

---

## Prävention: Probleme vermeiden

1. **Regelmäßige Snapshots:**
   ```bash
   sudo snapper -c root create -d "Vor großer Änderung"
   ```

2. **Vor Updates: News lesen:**
   https://archlinux.org/news/

3. **Nicht blind sudo:**
   Verstehe, was ein Befehl macht, bevor du ihn ausführst.

4. **Dotfiles committen:**
   ```bash
   cd ~/repos/dotfiles
   git add -A && git commit -m "Änderung"
   ```

5. **Config testen vor Neustart:**
   ```bash
   python -m py_compile ~/.config/qtile/config.py
   ```
