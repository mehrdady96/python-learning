# Guessing Games 🎲

Two small command-line guessing games written in Python while learning loops, functions, and user input.

## Games

### Lucky Dice (`lucky_dice.py`)

Guess the result of a dice roll against the machine.

- Enter a guess between 1 and 6.
- Each round the machine rolls a die. If it matches your guess, you score a point; otherwise the machine does.
- The scoreboard (`Human` vs `Machine`) is shown after every round.
- Type anything to play another round, or press Enter to exit.

> Your guess is entered once and stays the same for every round.

### Lucky Number (`lucky_number_02.py`)

Guess the number the machine picked.

- The machine picks a number between 1 and 9.
- After each guess you get a hint: **HIGHER** or **lower**.
- The game counts your wrong guesses and keeps track of your best record across rounds.
- At the end of each round, answer `Y` to play again or `N` to quit.

## How to run

```bash
python lucky_dice.py
python lucky_number_02.py
```

Requires Python 3. No external packages.

## What I practiced

- `while` loops and `break`
- Functions with docstrings (`lucky_number_02.py`)
- Random numbers with the `random` module
- Tracking state such as scores and records
