# Concepts for Beginners

> This chapter explains the fundamental concepts you need to understand before working with this setup.

---

## What's Different from Windows?

On Windows, you have a **desktop** with windows that you can freely move around. You click on icons, open programs from the start menu, and everything is graphical.

On Linux with this setup, things are different:

| Windows | This Setup |
|---------|------------|
| Start Menu | Rofi (Launcher) |
| Explorer | Thunar + Terminal |
| Move windows with mouse | Windows are automatically arranged |
| Taskbar | Qtile Bar |
| Settings App | Configuration files (text) |

**Most important difference:** Almost everything is controlled via **keyboard**, not mouse.

---

## What is a Tiling Window Manager?

A **Tiling Window Manager** (TWM) is a program that automatically arranges your windows – like tiles.

### Advantages

- **No overlapping:** Every window has its place
- **Fast:** Everything via keyboard, no mouse needed
- **Efficient:** Maximum screen utilization
- **Resource-friendly:** Much less RAM than KDE/GNOME

### What does it look like?

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

When you open a new window, the others automatically shrink to make room.

### Qtile

**Qtile** is our tiling window manager. It is:

- Written in **Python** (easy to customize)
- Highly **configurable**
- Well **documented**

The configuration is located at `~/.config/qtile/config.py`.

---

## What is Stow?

**GNU Stow** is a symlink manager for dotfiles.

### The Problem

Linux programs store their settings in "dotfiles" (files starting with `.`):

```
~/.bashrc           # Shell configuration
~/.config/qtile/    # Qtile configuration
~/.config/alacritty/ # Terminal configuration
```

These files are scattered everywhere. How do you manage them?

### The Solution: Stow

Stow collects all configurations in **one folder** and creates **symlinks** (shortcuts) to the right places.

```
~/repos/dotfiles/           # All configs in one place
├── bash/
│   └── .bashrc            # → Symlink to ~/.bashrc
├── qtile/
│   └── .config/qtile/
│       └── config.py      # → Symlink to ~/.config/qtile/config.py
└── alacritty/
    └── .config/alacritty/
        └── alacritty.toml # → Symlink to ~/.config/alacritty/alacritty.toml
```

### Advantages

1. **Version control:** Everything in one Git repository
2. **Portability:** On a new system: `git clone` + `stow` = done
3. **Overview:** All configs in one place

### How to use Stow?

```bash
# Change to dotfiles folder
cd ~/repos/dotfiles

# "Stow" a package (create symlinks)
stow bash

# Multiple packages
stow bash qtile alacritty

# All packages
stow */
```

---

## What are Dotfiles?

**Dotfiles** are configuration files whose names start with a dot (`.`).

The dot makes them "hidden" – `ls` won't show them, but `ls -a` will.

### Examples

| File | Purpose |
|------|---------|
| `~/.bashrc` | Shell configuration (aliases, prompt, etc.) |
| `~/.gitconfig` | Git settings (name, email, aliases) |
| `~/.config/` | Modern location for app configurations |

### Why are they important?

Dotfiles **define your system**. If you back them up, you can restore your exact setup on any computer.

---

## What is a Compositor?

A **compositor** (here: Picom) is a program that adds visual effects:

- **Transparency:** Windows can be see-through
- **Shadows:** Windows cast shadows
- **Blur:** Blurred background
- **Animations:** Smooth transitions

Without a compositor, everything looks "flat". With a compositor, it becomes sleek.

**Important:** The compositor is optional. If it causes problems, you can disable it.

---

## What is X11 vs Wayland?

Both are **display servers** – they handle making windows appear on screen.

| X11 | Wayland |
|-----|---------|
| Old (1984!) | New (2012) |
| Very compatible | Better performance |
| More software runs | Some software still missing |
| This setup | Future |

**This setup uses X11** because:
- Qtile works more reliably with it
- NVIDIA drivers are better supported
- More compatibility with older programs

---

## Directory Structure on Linux

Windows has `C:\Users\Name\`. Linux has:

```
/                    # Root (like C:\)
├── home/
│   └── carsten/     # Your home directory (~)
│       ├── .config/ # Configurations
│       ├── .local/  # Local data & programs
│       ├── repos/   # Git repositories
│       └── ...
├── etc/             # System configurations
├── usr/             # Programs
└── ...
```

### Important Paths

| Path | Meaning |
|------|---------|
| `~` | Your home directory (`/home/carsten`) |
| `~/.config/` | Your app configurations |
| `~/.local/bin/` | Your own scripts |
| `/etc/` | System-wide configurations |

---

## The Terminal

The **terminal** is your most important tool. Here you execute commands.

### Important Commands

```bash
# Navigation
cd ~/repos          # Change to folder
cd ..               # Go up one folder
ls                  # List files
ls -la              # With hidden files + details

# Files
cat file.txt        # Display file
nano file.txt       # Edit file (simple)
vim file.txt        # Edit file (powerful)

# System
sudo pacman -Syu    # Update system
sudo pacman -S xyz  # Install package
yay -S xyz          # Install AUR package

# Help
man command         # Show manual
command --help      # Short help
```

### Our Terminal: Alacritty

**Alacritty** is a fast, GPU-accelerated terminal emulator.

Important shortcuts:
- `Ctrl+Shift+C` – Copy
- `Ctrl+Shift+V` – Paste
- `Ctrl++` – Increase font size
- `Ctrl+-` – Decrease font size

---

## Next

Now you know the basics! In the next chapter, we cover [Installation](02-installation.md).
