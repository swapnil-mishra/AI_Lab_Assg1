"""Utility functions shared across task scripts.

Provides:
- GOAL: goal state tuple
- solvable(state): returns True if state is solvable (inversion parity)
- rand_state(): returns a random solvable state
- fmt(state): pretty-format a state for printing
- neigh(state): generate neighbor states and the move that produced them
"""
import random
from typing import Tuple, List

# Goal configuration (row-major)
GOAL = ('1', '2', '3', '4', '5', '6', '7', '8', 'B')


def solvable(s: Tuple[str, ...]) -> bool:
    """Return True if the 3x3 puzzle state `s` is solvable.

    Uses inversion parity for 3x3 (even -> solvable).
    """
    a = [x for x in s if x != 'B']
    inv = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if int(a[i]) > int(a[j]):
                inv += 1
    return inv % 2 == 0


def rand_state() -> Tuple[str, ...]:
    """Generate and return a random solvable state as a tuple of 9 strings."""
    while True:
        t = list('12345678B')
        random.shuffle(t)
        s = tuple(t)
        if solvable(s):
            return s


def fmt(s: Tuple[str, ...]) -> str:
    """Return a human-readable multi-line string for state `s`."""
    return '\n'.join(' '.join(s[i * 3:(i + 1) * 3]) for i in range(3))


def neigh(s: Tuple[str, ...]):
    """Yield neighbor states and move labels for the blank tile."""
    i = s.index('B')
    r, c = divmod(i, 3)
    out = []
    # Up
    if r > 0:
        n = list(s)
        n[i], n[i - 3] = n[i - 3], n[i]
        out.append((tuple(n), 'Up'))
    # Down
    if r < 2:
        n = list(s)
        n[i], n[i + 3] = n[i + 3], n[i]
        out.append((tuple(n), 'Down'))
    # Left
    if c > 0:
        n = list(s)
        n[i], n[i - 1] = n[i - 1], n[i]
        out.append((tuple(n), 'Left'))
    # Right
    if c < 2:
        n = list(s)
        n[i], n[i + 1] = n[i + 1], n[i]
        out.append((tuple(n), 'Right'))
    return out
