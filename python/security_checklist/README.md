# Security Checklist 🔐

A small Python script that checks names against a built-in "database" of registered people.

## How it works

1. The script keeps a dictionary of registered people with their age and height.
2. You type names one by one. Press Enter on an empty line to finish.
3. For each name, the script tells you whether the person is registered (and shows their details) or unknown.

## How to run

```bash
python engine.py
```

Requires Python 3. No external packages.

## Example

```
Enter the name: Ali
Enter the name: Sara
Enter the name:
Ali is registered and the age is 36 and 170 height
Sara is not registered and Unknown
```

## Adding people

Edit the `people` dictionary at the top of `engine.py`:

```python
people = {
    'Name': {'age': 30, 'height': 175},
}
```

## What I practiced

- Dictionaries and nested dictionaries
- `while` loops with `break`
- Lists, `for` loops, and `in` checks
- f-strings

## Notes

This is a learning project. The data is hard-coded and names are case-sensitive, so `ali` will not match `Ali`.
