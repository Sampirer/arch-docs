# Installation

> Dieses Kapitel erklärt, wie du das arch-install.sh Script verwendest, um ein vollständiges System zu installieren.

---

## Voraussetzungen

Bevor du startest, brauchst du:

1. **Arch Linux ISO** – Download von https://archlinux.org/download/
2. **USB-Stick** (mindestens 2 GB)
3. **Internetverbindung** (Ethernet empfohlen, WLAN möglich)
4. **Backup aller Daten** – Die Installation löscht alles auf der Ziel-Festplatte!

---

## USB-Stick erstellen

### Unter Linux

```bash
# USB-Stick finden
lsblk

# ISO auf Stick schreiben (ACHTUNG: Richtige Device wählen!)
sudo dd bs=4M if=archlinux-*.iso of=/dev/sdX status=progress oflag=sync
```

### Unter Windows

Verwende [Rufus](https://rufus.ie/) oder [Balena Etcher](https://etcher.io/).

---

## Vom USB-Stick booten

1. **PC neu starten**
2. **Boot-Menü öffnen** (meist F12, F2, oder Entf)
3. **USB-Stick auswählen**
4. **"Arch Linux install medium"** wählen

Du landest in einer Root-Shell:

```
root@archiso ~ #
```

---

## Netzwerk verbinden

### Ethernet

Funktioniert automatisch. Testen:

```bash
ping -c 3 archlinux.org
```

### WLAN

```bash
# WLAN-Tool starten
iwctl

# Adapter finden
device list

# Nach Netzwerken suchen
station wlan0 scan
station wlan0 get-networks

# Verbinden
station wlan0 connect "DEIN-NETZWERK"
# Passwort eingeben

# Beenden
exit

# Testen
ping -c 3 archlinux.org
```

---

## Script herunterladen

```bash
# Script laden
curl -LO https://raw.githubusercontent.com/Sampirer/arch-install/main/arch-install.sh

# Ausführbar machen
chmod +x arch-install.sh

# Starten
./arch-install.sh
```

---

## Interaktive Konfiguration

Das Script fragt alle Einstellungen ab:

### Benutzer & System

| Abfrage | Standard | Beschreibung |
|---------|----------|--------------|
| Username | carsten | Dein Login-Name |
| Hostname | archlinux | Name des Computers |
| Root-Passwort | – | Wird abgefragt |
| User-Passwort | – | Wird abgefragt |

### Sprache & Region

| Abfrage | Standard | Beschreibung |
|---------|----------|--------------|
| Tastaturlayout | de-latin1 | Deutsches Layout |
| Locale | de_DE.UTF-8 | Systemsprache |
| Zeitzone | Europe/Berlin | Für korrekte Uhrzeit |

### Festplatte

| Abfrage | Standard | Beschreibung |
|---------|----------|--------------|
| Disk | /dev/nvme0n1 | Ziel-Festplatte |
| EFI-Größe | 1G | Boot-Partition |
| Swap-Größe | RAM + 2G | Für Hibernate |

**ACHTUNG:** Alle Daten auf der gewählten Festplatte werden gelöscht!

### Grafikkarte

Das Script erkennt deine GPU automatisch. Du kannst wählen:

| Option | Für wen? |
|--------|----------|
| Intel | Laptops, integrierte Grafik |
| AMD | AMD Grafikkarten |
| NVIDIA | NVIDIA Grafikkarten |
| Intel + NVIDIA | Gaming-Laptops (Optimus) |
| Intel + AMD | Seltene Kombination |

### Desktop-Optionen

| Abfrage | Optionen |
|---------|----------|
| Display Manager | SDDM (empfohlen), LightDM, Ly, Keiner |
| Firefox installieren? | Ja/Nein |
| Snapper (Snapshots)? | Ja (empfohlen) |
| Bluetooth? | Ja/Nein |
| Drucker (CUPS)? | Ja/Nein |

### Dotfiles

| Abfrage | Beschreibung |
|---------|--------------|
| Dotfiles einrichten? | Klont und konfiguriert automatisch |

Wenn "Ja":
- Klont `dotfiles` und `scripts` Repositories
- Installiert yay (AUR-Helper)
- Installiert blesh (Bash-Erweiterung)
- Wendet alle Stow-Konfigurationen an

---

## Was das Script macht

### Phase 1: Partitionierung

```
┌─────────────────────────────────────────────────┐
│ Deine Festplatte                                │
├──────────┬──────────┬───────────────────────────┤
│ EFI 1GB  │ Swap     │ Root (Btrfs)              │
│ FAT32    │ ~20 GB   │ Subvolumes: @, @home, ... │
└──────────┴──────────┴───────────────────────────┘
```

### Phase 2: Btrfs-Subvolumes

| Subvolume | Mountpoint | Zweck |
|-----------|------------|-------|
| @ | / | System |
| @home | /home | Deine Dateien |
| @snapshots | /.snapshots | Snapper Backups |
| @var_log | /var/log | Log-Dateien |
| @var_cache | /var/cache | Paket-Cache |
| @var_tmp | /var/tmp | Temporäre Dateien |

### Phase 3: Basis-Installation

- Linux Kernel
- Bootloader (GRUB)
- Netzwerk (NetworkManager)
- Basis-Tools

### Phase 4: Desktop

- Xorg (Display Server)
- Qtile (Window Manager)
- Alacritty (Terminal)
- Picom (Compositor)
- Weitere Tools

### Phase 5: Konfiguration

- Benutzer anlegen
- Sudo einrichten
- Snapper konfigurieren
- GRUB mit Snapshot-Support

### Phase 6: Dotfiles (optional)

- yay installieren
- Repositories klonen
- Stow ausführen
- blesh installieren

---

## Nach der Installation

Das Script zeigt am Ende:

```
╔════════════════════════════════════════╗
║     Installation abgeschlossen!        ║
╠════════════════════════════════════════╣
║  Entferne den USB-Stick und starte     ║
║  den Computer neu mit: reboot          ║
╚════════════════════════════════════════╝
```

1. **USB-Stick entfernen**
2. **Neu starten:** `reboot`
3. **Im GRUB-Menü:** "Arch Linux" wählen
4. **Im SDDM:** Mit deinem Benutzer einloggen

---

## Fehlerbehebung

### "Script bricht ab"

```bash
# Log prüfen
cat /tmp/arch-install.log
```

### "Keine Internetverbindung"

```bash
# DNS testen
ping -c 3 8.8.8.8

# Falls das funktioniert, DNS-Problem:
echo "nameserver 8.8.8.8" > /etc/resolv.conf
```

### "Festplatte nicht gefunden"

```bash
# Alle Laufwerke anzeigen
lsblk

# NVMe-Treiber laden
modprobe nvme
```

### "GRUB-Fehler"

Falls GRUB nicht installiert werden kann:

```bash
# Manuell in chroot
arch-chroot /mnt
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```

---

## Weiter

Nach dem Neustart: [Erster Start](03-erster-start.md)
