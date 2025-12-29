# Troubleshooting

> Common problems and solutions.

---

## Emergency: Qtile Won't Start

1. `Ctrl + Alt + F2` (TTY)
2. Login
3. `python -m py_compile ~/.config/qtile/config.py`
4. Fix error
5. `Ctrl + Alt + F1` back

---

## Restore Snapshot

1. GRUB → "Arch Linux Snapshots"
2. Select snapshot
3. After boot: `sudo snapper -c root rollback && sudo reboot`

---

## No Sound

```bash
systemctl --user restart pipewire wireplumber
pavucontrol
```

---

## No WiFi

```bash
nmcli device wifi list
nmcli device wifi connect "SSID" password "PASS"
```

---

## Wrong Resolution

```bash
xrandr
xrandr --output HDMI-1 --mode 1920x1080
```

---

## Package Problems

```bash
sudo pacman -Dk
sudo pacman -Syy
```

---

## Service Won't Start

```bash
systemctl status servicename
journalctl -u servicename -b
sudo systemctl restart servicename
```

---

## Reading Logs

```bash
journalctl -b
journalctl -p err -b
cat ~/.local/share/qtile/qtile.log
```

---

## Getting Help

- **Arch Wiki:** https://wiki.archlinux.org
- **Forum:** https://bbs.archlinux.org
- **Reddit:** r/archlinux, r/qtile
