# Concepts for Beginners

> Fundamental concepts you need to understand before working with this setup.

---

## What's Different from Windows?

| Windows | This Setup |
|---------|------------|
| Start Menu | Rofi (Launcher) |
| Explorer | Thunar + Terminal |
| Move windows with mouse | Windows auto-arranged |
| Taskbar | Qtile Bar |
| Settings App | Config files (text) |

**Key difference:** Almost everything is controlled via **keyboard**, not mouse.

---

## What is a Tiling Window Manager?

A **Tiling Window Manager** (TWM) automatically arranges your windows like tiles.

### Advantages

- **No overlapping:** Every window has its place
- **Fast:** Everything via keyboard
- **Efficient:** Maximum screen utilization
- **Resource-friendly:** Much less RAM than KDE/GNOME

### Qtile

**Qtile** is our tiling window manager:
- Written in **Python**
- Highly **configurable**
- Well **documented**

Config: `~/.config/qtile/config.py`

---

## What is Stow?

**GNU Stow** is a symlink manager for dotfiles.

It collects all configs in **one folder** and creates **symlinks** to the right places.

```bash
cd ~/repos/dotfiles
stow bash qtile alacritty
```

---

## What are Dotfiles?

Config files starting with `.` (dot). They define your system.

---

## What is a Compositor?

**Picom** adds visual effects: transparency, shadows, blur.

---

## X11 vs Wayland

Both are display servers. This setup uses **X11** for better compatibility.

---

## Next

[Installation](02-installation.md)
