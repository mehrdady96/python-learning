# Shitty Pys 🧪

A scratchpad of small Python practice scripts: quick experiments, exercises, and half-finished ideas written while learning.

> ⚠️ **Heads-up:** these are practice files, not polished projects. Some scripts may not be fully functional, may depend on files that only exist on my computer, or are still unfinished. Treat them as learning notes, not production code.

## Scripts

| File | What it does | Status |
|------|--------------|--------|
| `avg_sum_biggest.py` | Calculates the sum, average, and largest value of a dictionary of donations | ⚠️ Works on the sample data, with known edge cases (see below) |
| `functions.py` | Finds the largest number in a list with a function | ✅ Works |
| `names _ seperated _ numbered.py` | Prints each letter of a name with a number, e.g. `1 -> a / 2 -> l / 3 -> i` | ✅ Works |
| `square_for_loop.py` | Splits a 10×10 grid of coordinates into 5×5 squares using nested loops | ✅ Works |
| `time_passed.py` | A decorator that measures how long a function takes | ✅ Works |
| `excel_practice.py` | Reads ages from an Excel file and prints the count and average | ⚠️ Asks for the file path; expects ages in column F and fails on empty cells |
| `photo_to_excel.py` | Meant to average the RGB of 10×10 pixel blocks and write them into Excel cells | 🚧 Unfinished: `burn_rgb` is empty and only the first block is printed |

## Requirements

- Python 3
- `openpyxl` (for `excel_practice.py` and `photo_to_excel.py`)
- `Pillow` (for `photo_to_excel.py`)

```bash
pip install openpyxl pillow
```

## How to run

```bash
python functions.py
python "names _ seperated _ numbered.py"
```

The Excel and photo scripts ask for the file path when you run them. `excel_practice.py` expects an `.xlsx` file with ages in column F, and `photo_to_excel.py` expects an image file.

## Known issues

- `avg_sum_biggest.py`: the average uses integer division, and the largest-donor lookup returns an empty name if the first entry is the largest.
- `excel_practice.py`: fails if a cell in the age column is empty.
- `photo_to_excel.py`: work in progress.

## What I practiced

- Dictionaries, lists, and nested loops
- Functions and decorators
- Reading Excel files with `openpyxl`
- Reading pixel data with `Pillow`
