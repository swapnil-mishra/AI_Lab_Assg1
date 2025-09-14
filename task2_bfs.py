"""Task 2: BFS Implementation

Breadth-First Search solver for the 8-puzzle. This script demonstrates
the BFS approach and reports path, number of steps (depth), nodes explored,
and elapsed time.
"""
import time
from collections import deque
from typing import Tuple, Set, Dict
from utils import neigh, fmt, GOAL, rand_state


def bfs(start: Tuple[str, ...]) -> Dict:
    """Perform BFS from `start` and return result dict with metrics."""
    t0 = time.time()
    q = deque([(start, [])])
    seen: Set[Tuple[str, ...]] = {start}
    nodes = 0
    while q:
        s, p = q.popleft()
        nodes += 1
        if s == GOAL:
            return {'found': True, 'path': p, 'steps': len(p), 'nodes': nodes, 'time': time.time() - t0}
        for nb, m in neigh(s):
            if nb not in seen:
                seen.add(nb)
                q.append((nb, p + [m]))
    return {'found': False, 'path': [], 'steps': 0, 'nodes': nodes, 'time': time.time() - t0}


def main():
    s = rand_state()
    print('Start state:\n', fmt(s))
    res = bfs(s)
    print('\nBFS result:')
    print(res)


if __name__ == '__main__':
    main()
