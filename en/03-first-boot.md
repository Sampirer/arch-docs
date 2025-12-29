# First Boot

> What to do after installation.

---

## Login (SDDM)

Enter username and password.

---

## First Steps

1. **Open terminal:** `Super + Return`
2. **Update system:** `sudo pacman -Syu`
3. **Open second window:** `Super + Return` again
4. **Switch windows:** `Super + J` or `Super + K`
5. **Close window:** `Super + Q`

---

## Launch Programs

| Method | How |
|--------|-----|
| Rofi | `Super + R` → type name |
| Keybinding | `Super + Return` (terminal) |
| Terminal | `firefox &` |

---

## Workspaces

| Keybinding | Action |
|------------|--------|
| `Super + 1-9` | Switch workspace |
| `Super + Shift + 1-9` | Move window |

---

## Create Snapshot

```bash
sudo snapper -c root create -d "First successful boot"
```

---

## Cheatsheet

```
Super + Return     Terminal
Super + R          Rofi Launcher
Super + Q          Close window
Super + 1-9        Switch workspace
Super + Space      Change layout
Super + Ctrl + R   Reload Qtile
Super + Ctrl + Q   Logout
```

---

## Next

[Qtile Basics](04-qtile.md)
