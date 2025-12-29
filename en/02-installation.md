# Installation

> How to use the arch-install.sh script.

---

## Prerequisites

1. **Arch Linux ISO** from https://archlinux.org/download/
2. **USB drive** (2+ GB)
3. **Internet connection**
4. **Backup all data** – Installation erases everything!

---

## Boot from USB

1. Restart PC
2. Open boot menu (F12, F2, or Del)
3. Select USB drive

---

## Connect to Network

```bash
# Ethernet works automatically

# WiFi
iwctl
station wlan0 connect "YOUR-NETWORK"
exit
```

---

## Download and Run Script

```bash
curl -LO https://raw.githubusercontent.com/Sampirer/arch-install/main/arch-install.sh
chmod +x arch-install.sh
./arch-install.sh
```

---

## Interactive Configuration

The script prompts for:
- Username, hostname, passwords
- Keyboard layout, locale, timezone
- Disk, partition sizes
- GPU drivers (Intel, AMD, NVIDIA, Hybrid)
- Display manager, browsers, extras
- Dotfiles setup (optional)

---

## After Installation

1. Remove USB drive
2. `reboot`
3. In GRUB: Select "Arch Linux"
4. Login with your user

---

## Next

[First Boot](03-first-boot.md)
