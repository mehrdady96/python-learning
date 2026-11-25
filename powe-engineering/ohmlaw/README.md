# Ohm's Law Calculator ⚡

A command-line calculator for Ohm's law (`V = I × R`), plus a small reusable `OhmLaw` class. Give it two of the three values and it calculates the third.

> 🚧 **Work in progress:** the calculator works, but the menu and the entry point still have some rough edges. See [Known issues](#known-issues).

## Features

- Calculate **voltage** from current and resistance
- Calculate **current** from voltage and resistance
- Calculate **resistance** from voltage and current
- Asks again when you type something that is not a number
- Calculate **power** in the `OhmLaw` class (not in the menu yet)

## Requirements

- Python 3
- No external packages

## How to run

Open a terminal in this folder and run:

```bash
python app.py
```

Choose a tool by typing its key and press Enter, then enter the two values you are asked for:

| Key | Calculates |
|-----|------------|
| `v` | Voltage |
| `r` | Resistance |
| `c` | Current |

After each result, type `c` to calculate again or `q` to quit.


### Example

```
 enter here : v
 enter current : 2
 enter resistance : 5

 voltage is 10.0 V
```

### Units

The formulas do not convert units, so enter values in one consistent set. The labels the program prints (`V`, `KΩ`, `mA`) match **volts, kilo-ohms and milliamps**.

## Using the OhmLaw class

`ohm_law.py` has no side effects, so you can import it in your own code:

```python
from ohm_law import OhmLaw

ohm = OhmLaw()
ohm.voltage(current=2, resistance=5)    # 10
ohm.current(voltage=10, resistance=5)   # 2.0
ohm.resistance(voltage=10, current=2)   # 5.0
ohm.power(voltage=10, current=2)        # 20
```

- `power()` works with any two of `voltage`, `current` and `resistance`.
- `voltage()` and `current()` raise a `ValueError` if the resistance is zero or negative.
- `resistance()` raises a `ValueError` if the current is zero.

## Project structure

```
ohmlaw/
├── app.py       # menu, user input, and the calculator loop
├── ohm_law.py   # the OhmLaw class with the calculations
├── main.py      # intended entry point 
└── README.md
```

## Known issues
- **Zero values crash the app:** entering a resistance of `0` (or a current of `0` when calculating resistance) shows a `ValueError` instead of a friendly message.
- **Power is not in the menu:** the calculation exists in `OhmLaw.power()`, but the menu option is commented out.

## What I practiced

- Classes and methods
- Raising and handling exceptions
- Validating user input with `try` / `except`
- Splitting a program into modules
