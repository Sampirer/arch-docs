# Maintenance

> Updates, snapshots, backups.

---

## System Updates

```bash
# Create snapshot first!
sudo snapper -c root create -d "Before update"

# Update
sudo pacman -Syu
yay -Syu
```

**Important:** Read https://archlinux.org/news/ before updates!

---

## Snapper Snapshots

```bash
sudo snapper -c root list
sudo snapper -c root create -d "Description"
sudo snapper -c root rollback  # after booting snapshot
```

---

## Package Management

```bash
pacman -Ss searchterm           # Search
sudo pacman -S packagename      # Install
sudo pacman -Rns packagename    # Remove
sudo pacman -Rns $(pacman -Qtdq) # Remove orphans
```

---

## Cleanup

```bash
sudo paccache -r                    # Package cache
sudo journalctl --vacuum-time=7d    # Journal
```

---

## Backup Dotfiles

```bash
cd ~/repos/dotfiles
git add -A && git commit -m "Update" && git push
```

---

## Weekly Routine

- [ ] `sudo pacman -Syu && yay -Syu`
- [ ] Commit dotfiles
- [ ] Create snapshot

---

## Next

[Troubleshooting](08-troubleshooting.md)
