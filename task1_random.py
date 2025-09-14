"""Task 1: Random Grid Generation

Generates a random solvable 3x3 grid and prints it.
This corresponds to the assignment Task 1.
"""
from utils import rand_state, fmt


def main():
    """Generate and print one random solvable state."""
    s = rand_state()
    print('Random solvable initial state:')
    print(fmt(s))


if __name__ == '__main__':
    main()
