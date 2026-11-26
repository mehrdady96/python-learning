# Python Projects 🐍

A guide to the Python projects and practice scripts in this folder. Each subfolder has its own README with details.

## Projects

| Folder | What it is | How to run |
|--------|------------|------------|
| [`Black_Jack`](Black_Jack) | Command-line Blackjack against the house | `python BlackJack.py` |
| [`guessing_games`](guessing_games) | Two small guessing games: Lucky Dice and Lucky Number | `python lucky_dice.py` or `python lucky_number_02.py` |
| [`Patric`](Patric) | Hide a text message inside an image and decode it later (steganography) | `python main.py` |
| [`security_checklist`](security_checklist) | Checks names against a small dictionary of registered people | `python engine.py` |
| [`where_is_bus`](where_is_bus) | Finds the stops between two bus stops, with one transfer. 🚧 Work in progress | `python bus.py` |
| [`shitty_pys`](shitty_pys) | A scratchpad of small practice scripts. ⚠️ Some are incomplete or not fully functional | one script at a time |

## Requirements

- Python 3 for everything in this folder.
- `Pillow` for `Patric` and `shitty_pys/photo_to_excel.py`.
- `openpyxl` for `shitty_pys/excel_practice.py` and `shitty_pys/photo_to_excel.py`.

```bash
pip install pillow openpyxl
```

## How to run a project

1. Open a terminal inside the project's folder, for example `cd python/Black_Jack`.
2. Run the file shown in the table above with `python`. On some systems, use `python3` instead.
3. Read the folder's README for the controls and example output.

## Folder layout

```
python/
├── Black_Jack/
├── guessing_games/
├── Patric/
├── security_checklist/
├── shitty_pys/
└── where_is_bus/
```

## About

These are learning projects. The code favors practice over polish, and a few projects have known issues, which are listed in their own READMEs.
