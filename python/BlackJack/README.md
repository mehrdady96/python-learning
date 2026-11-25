# Blackjack 🃏

A simple command-line Blackjack game written in Python while learning classes and control flow. You play against the house, dealt by a dealer named Yara.

## How to run

```bash
python BlackJack.py
```

Requires Python 3. No external packages.

## How to play

1. You and the house are each dealt two cards.
2. Choose **H** (hit) to draw a card or **S** (stand) to hold.
3. The game announces the result: Player won, House won, or Pushed (tie).
4. Press Enter to play another round. To quit, type anything else and answer `yes` when Yara asks if you tipped her.

## Card values

| Card | Value |
|------|-------|
| 2–9  | Face value |
| K, Q, J | 10 |
| A | 1, or 11 when that doesn't bust the hand (one ace per hand) |

## Project structure

- `Blackjack` class: `draw_card` (maps a random number to a card), `check_value` (hand total), `check_status` (decides the round outcome)
- `run()`: the game loop and user interaction

## Notes

This is a learning project, so the rules are simplified: cards are drawn at random with replacement (no real deck, no card 10 or joker), and the house logic is not identical to casino Blackjack.
