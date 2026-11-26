# Where Is My Bus? 🚌

A small Python script that finds the stops between two bus stops, with one transfer between lines when needed.

> 🚧 **Work in progress:** the basic route finding works, but the transfer logic is still incomplete. See [Known issues](#known-issues) for the cases that don't work yet.

## How it works

- Eight bus lines are stored as lists of stops (`bus_1` … `bus_8`).
- You set the `start` and `finish` stops near the bottom of the script.
- If both stops are on the same line, the script prints the stops between them in the right direction.
- If they are on different lines, the script looks for a stop the two lines share and prints two segments: `start` to the transfer stop, then the transfer stop to `finish`.

## How to run

```bash
python bus.py
```

Requires Python 3. No external packages.

To try other stops, edit these two variables in `bus.py`:

```python
start = "Taksim"
finish = "Tarabya"
```

## Example

```
['Taksim', 'Sisli', 'Osmanbey', 'Besiktas', 'Ortakoy', 'Arnavut', 'Bebek', 'Etiler', 'Levent', 'Maslak', 'Eyup']
['Eyup', 'Pierre', 'Alibey', 'Kagithane', 'Seyrantepe', 'Ayazaga', 'Tarabya']
```

The first line is the ride on `bus_2`, the second is the ride on `bus_7` after transferring at `Eyup`.

## Known issues

- **No shared stop:** if the two lines have no stop in common (for example `Kadikoy` to `Taksim`), the script crashes with a `ValueError`.
- **Transfer at the first stop of a line:** the first segment prints an empty list (for example `Kabatas` to `Tarabya`), because of a reversed-slice edge case.
- **Stops on several lines:** only the last line containing the stop is used, so some routes print nothing (for example `Sabiha` to `Kadikoy`).
- **Several shared stops:** the transfer stop is picked from an unordered set, so it can change between runs and is not always the shortest route (for example `Taksim` to `Galata`).
- Only one transfer is supported.
- The bus lines are hard-coded sample data, not real timetables.
- Stop names are case-sensitive and written without Turkish characters.

## Ideas for the future

- Ask for `start` and `finish` with `input()`
- Handle "no route" without crashing
- Choose the transfer stop that gives the shortest route
- Support more than one transfer
- Load the lines from a file

## What I practiced

- Lists, indexing, and slicing (including reversed slices)
- Sets and intersections to find common stops
- Conditions and `for` loops
