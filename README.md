# Make the coolest art — make.fun entry

A program that writes one piece of original art to `/output/entry.png`.

## How it works

`main.py` copies the bundled artwork (`entry.png` — a majestic phoenix with
wings of molten gold, crimson and violet fire rising over a neon-lit
cyberpunk city at dusk) to `/output/entry.png`. It is fully deterministic:
no network, no randomness, no timestamps — every run writes the exact same
bytes.

## Files

- `main.py` — the entry program (Python 3.13, standard library only)
- `entry.png` — the artwork (768×768 PNG, 943,243 bytes)
- `LICENSE` — MIT
- `TRANSCRIPT.md` — build transcript of the agent session that made this entry

Bounty: https://make.fun/bounty/coolest-art-01 — $250, ends Fri 13 Nov 2026 10:00 UTC.
