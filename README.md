# Python Learning 🐍

A collection of small Python projects and experiments built while learning programming. The repository includes command-line games, beginner exercises, a bus-route finder, an image steganography experiment, an Ohm's law calculator, and a solar-angle calculator.

Most projects are self-contained and have their own README with instructions, examples, and known limitations. They are learning projects, so some are works in progress.

## Projects

| Project | Description | Run |
|---|---|---|
| [Solar Calculator](solar%20power/solar%20calculator/) | Command-line and Tkinter tools for estimating the angle of incidence of sunlight on a tilted surface. | `python app.py` or `python graphic.py` |
| [Ohm's Law Calculator](power-engineering/) | Command-line calculator for voltage, current, and resistance, with a reusable `OhmLaw` class. | `python app.py` |
| [Blackjack](python/Black_Jack/) | A simple command-line Blackjack game against the house. | `python BlackJack.py` |
| [Where Is My Bus?](python/where_is_bus/) | Finds a route between two stops, including one transfer between bus lines. | `python bus.py` |
| [Patrik](python/Patric/) | Hides a short message in an image and reads it back using pixel colors. | `python main.py` |
| [Guessing Games](python/guessing_games/) | Lucky Dice and Lucky Number command-line games. | Run either script; see its README. |
| [Security Checklist](python/security_checklist/) | Checks names against a small, hard-coded dictionary of registered people. | `python engine.py` |
| [Practice Scripts](python/shitty_pys/) | A scratchpad of small exercises and experiments, with a few unfinished scripts. | Run one script at a time; see its README. |

## Getting started

You need Python 3. Most projects use only the Python standard library. Some optional projects need extra packages:

- **Patrik** and `photo_to_excel.py`: Pillow
- Excel practice scripts: openpyxl

Install the packages if you want to use those projects:

```bash
python -m pip install pillow openpyxl
```

Open a terminal in the folder for the project you want to run, then use the command in the table above. On some systems, use `python3` instead of `python`.

## Repository layout

```text
.
├── power-engineering/          # Ohm's law calculator
├── solar power/
│   └── solar calculator/       # Solar-angle calculator
└── python/
    ├── Black_Jack/             # Blackjack game
    ├── guessing_games/         # Lucky Dice and Lucky Number
    ├── Patric/                 # Image steganography experiment
    ├── security_checklist/     # Name lookup exercise
    ├── shitty_pys/             # Practice scripts
    └── where_is_bus/           # Bus route finder
```

## Learning topics

These projects practice Python basics and gradually introduce:

- Variables, numbers, strings, lists, and dictionaries
- Conditions, loops, functions, and user input
- Classes, modules, and importing code
- Exceptions and input validation
- Random numbers and simple game state
- Working with images and Excel files
- Basic graphical interfaces with Tkinter

## Project notes

- The bus routes are sample data, not real Istanbul routes or timetables. Its transfer logic has known limitations.
- The Blackjack game uses simplified rules and random draws rather than a standard shuffled deck.
- The solar calculator is intended for learning and estimation; check its assumptions before relying on results.
- The practice-scripts folder contains incomplete experiments and computer-specific file assumptions.

For exact instructions, examples, and known issues, open the README inside each project folder.
