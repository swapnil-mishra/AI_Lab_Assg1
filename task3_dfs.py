"""Task 3: DFS Implementation (depth-limited)

Depth-first search with a depth limit to prevent infinite recursion.
Reports whether a solution was found, steps (if found), nodes explored, and time.
"""
import time
from typing import Tuple, List, Set, Dict, Optional
from utils import neigh, fmt, GOAL, rand_state


def dfs_limit(start: Tuple[str, ...], limit: int = 30) -> Dict:
    """Perform depth-limited DFS from `start`.

    Returns a dict with keys: found (bool), path (list), steps (int), nodes (int), time (float).
    """
    t0 = time.time()
    seen: Set[Tuple[str, ...]] = set()
    nodes = 0
    path_res: Optional[List[str]] = None

    def dfs(s: Tuple[str, ...], p: List[str], d: int) -> bool:
        nonlocal nodes, path_res
        nodes += 1
        seen.add(s)
        if s == GOAL:
            path_res = p.copy()
            return True
        if d >= limit:
            return False
        for nb, m in neigh(s):
            if nb not in seen:
                if dfs(nb, p + [m], d + 1):
                    return True
        return False

    ok = dfs(start, [], 0)
    return {'found': ok, 'path': path_res or [], 'steps': len(path_res) if path_res else 0, 'nodes': nodes, 'time': time.time() - t0}


def main():
    s = rand_state()
    print('Start state:\n', fmt(s))
    r = dfs_limit(s, limit=30)
    print('\nDFS result:')
    print(r)


if __name__ == '__main__':
    main()
