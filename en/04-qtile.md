# Qtile Basics

> Keybindings, layouts, and customization.

---

## Essential Keybindings

### Launch Programs
| Keybinding | Action |
|------------|--------|
| `Super + Return` | Terminal |
| `Super + R` | Rofi launcher |
| `Super + B` | Browser |

### Window Control
| Keybinding | Action |
|------------|--------|
| `Super + Q` | Close window |
| `Super + H/J/K/L` | Change focus |
| `Super + Shift + H/J/K/L` | Move/resize |
| `Super + F` | Fullscreen |
| `Super + Space` | Change layout |

### Workspaces
| Keybinding | Action |
|------------|--------|
| `Super + 1-9` | Switch |
| `Super + Shift + 1-9` | Move window |

### System
| Keybinding | Action |
|------------|--------|
| `Super + Ctrl + R` | Reload Qtile |
| `Super + Ctrl + Q` | Logout |

---

## Layouts

- **MonadTall:** Main left, stack right
- **MonadWide:** Main top, stack bottom
- **Max:** Fullscreen tabs

---

## Config File

`~/.config/qtile/config.py`

### After Changes

```bash
python -m py_compile ~/.config/qtile/config.py
# Super + Ctrl + R
```

---

## Next

[Theming](05-theming.md)
