# Solar Calculator

A lightweight Python desktop application that calculates the angle of incidence of sunlight on a tilted surface. Enter the solar time, date, location latitude, surface azimuth, and surface slope to get the incidence angle in degrees.

## Features

- Calculates solar hour angle from the entered solar time.
- Calculates solar declination from the day of the year.
- Calculates the angle of incidence on a tilted surface.
- Validates time and date inputs and reports invalid values in the app.
- Uses a graphical interface built with Python's Tkinter and ttk.

## Requirements

- Python 3
- Tkinter (included with most standard Python installations; some Linux distributions package it separately)

No third-party Python packages are required.

## Run

Clone or download this repository, open a terminal in the project directory, and run:

```bash
python app.py
```

On some systems, use `python3 app.py` instead.

## Inputs

- **Solar time:** Hour and minute in 24-hour format.
- **Month and day:** The date used to estimate solar declination. The current implementation uses a 365-day year and does not account for leap years.
- **Azimuth angle:** Surface azimuth in degrees.
- **Latitude:** Location latitude in degrees. Defaults to 43°.
- **Slope:** Surface tilt from the horizontal in degrees; negative values are not accepted.

The result is displayed as an incidence angle in degrees. The formula assumes angles are entered in degrees. Ensure the azimuth follows the convention expected by your application and calculation setup.

## Project files

- `app.py` — Tkinter user interface and input validation.
- `Engine.py` — Solar angle calculations.

## Disclaimer

This project is intended for learning and estimation. Results depend on the input angle conventions and the assumptions in the calculation; verify them before using the output for engineering or installation decisions.

## Development note

The core calculation engine was written by an electrical engineer and checked against references used in the Fundamentals of Solar Energy course. The graphical user interface was generated with the assistance of AI and should be reviewed by a qualified professional.
