# Content plan source

The workbook one folder up is built from these files:

- `long_a.py`, `long_b.py`: the 13 long videos (titles, thumbnails, scripts, tags, sources).
- `shorts.py`: the 30 Shorts.
- `build.py`: turns them into the Excel file.

To rebuild after editing a script: `python3 build.py` (needs `openpyxl`). Data used for every number is in `~/Documents/YouTube/Data/downloaded-2026-11-02`.
