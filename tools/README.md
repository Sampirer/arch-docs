# WoW Talent Parser

This folder contains a standalone parser for WoW TBC talent calculator URLs. It
extracts build allocation strings from Wowhead or Icy Veins URLs and attempts to
normalize any talent metadata embedded in the calculator HTML.

## Usage

```bash
python tools/wow_talent_parser.py \
  --url https://www.wowhead.com/tbc/talent-calc/warlock/150222201023-2050030133250101501351 \
  --output warlock.json
```

If the calculator content is blocked from automated downloads, save the HTML
manually and parse the file instead:

```bash
python tools/wow_talent_parser.py --html-file saved.html --output warlock.json
```

## Output Notes

- `raw_allocation` preserves the build string from the URL.
- `trees` are normalized when recognizable tree data is embedded in the HTML.
- `raw_metadata` stores extracted script blocks to inspect when normalization
  fails or the source changes its markup.
