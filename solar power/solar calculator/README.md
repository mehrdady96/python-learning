# Solar Calculator

A Python solar calculator for calculating the angle of incidence of sunlight on a tilted surface. The project includes a reusable calculation engine, a command-line application, and an optional graphical interface.

## Features

- Calculates solar hour angle from the entered solar time.
- Calculates solar declination from the day of the year.
- Calculates the angle of incidence on a tilted surface.
- Provides both a command-line workflow and a graphical interface.
- Keeps the solar calculations in reusable Python modules.

## Requirements

- Python 3
- Tkinter (included with most standard Python installations; some Linux distributions package it separately)

No third-party Python packages are required.

## Run

Clone or download this repository, open a terminal in the project directory, and run one of these commands:

```bash
# Interactive terminal version
python app.py

# Graphical window
python graphic.py
```

On some systems, use `python3` instead of `python`.

## Inputs

- **Solar time:** Hour and minute in 24-hour format.
- **Month and day:** The date used to estimate solar declination. The current implementation uses a 365-day year and does not account for leap years.
- **Azimuth angle:** Surface azimuth in degrees.
- **Latitude:** Location latitude in degrees. Defaults to 43°.
- **Slope:** Surface tilt from the horizontal in degrees; negative values are not accepted.

The incidence angle is reported in degrees. The formula assumes angles are entered in degrees. Ensure the azimuth follows the convention expected by your calculation setup.

## Project files

- `app.py` — Command-line application and functions for collecting inputs, calculating, and displaying the result. It can also be imported into other Python code.
- `Engine.py` — Core solar angle calculation functions. It can be imported and used independently.
- `graphic.py` — AI-assisted Tkinter graphical interface. Run it directly to open the calculator window.

## Project status

The command-line application (`app.py`) and calculation engine (`Engine.py`) are ready to use and import into other Python projects. The graphical interface (`graphic.py`) can be run directly, but its user interface and error handling still need further review. The core application and calculation engine are ready for use.

## Disclaimer

This project is intended for learning and estimation. Results depend on the input angle conventions and the assumptions in the calculation; verify them before using the output for engineering or installation decisions.

## Development note

The core calculation engine was written by an electrical engineer and checked against references used in the Fundamentals of Solar Energy course. The graphical user interface was written with AI assistance. Its interface and error handling should be reviewed and improved.
