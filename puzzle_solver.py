"""
8-puzzle solver (concise names)

Usage: python puzzle_solver.py
"""

import random
import time
from collections import deque
from typing import Tuple, List, Set, Optional, Dict

GOAL = ('1','2','3','4','5','6','7','8','B')

def solvable(s: Tuple[str,...]) -> bool:
    a = [x for x in s if x != 'B']
    inv = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if int(a[i]) > int(a[j]):
                inv += 1
    return inv % 2 == 0

def rand_state() -> Tuple[str,...]:
    while True:
        t = list('12345678B')
        random.shuffle(t)
        s = tuple(t)
        if solvable(s):
            return s

def fmt(s: Tuple[str,...]) -> str:
    return '\n'.join(' '.join(s[i*3:(i+1)*3]) for i in range(3))

def neigh(s: Tuple[str,...]) -> List[Tuple[Tuple[str,...], str]]:
    i = s.index('B')
    r, c = divmod(i, 3)
    out: List[Tuple[Tuple[str,...], str]] = []
    if r > 0:
        n = list(s); n[i], n[i-3] = n[i-3], n[i]; out.append((tuple(n), 'Up'))
    if r < 2:
        n = list(s); n[i], n[i+3] = n[i+3], n[i]; out.append((tuple(n), 'Down'))
    if c > 0:
        n = list(s); n[i], n[i-1] = n[i-1], n[i]; out.append((tuple(n), 'Left'))
    if c < 2:
        n = list(s); n[i], n[i+1] = n[i+1], n[i]; out.append((tuple(n), 'Right'))
    return out

def bfs(start: Tuple[str,...]) -> Dict:
    t0 = time.time()
    q = deque([(start, [])])
    seen: Set[Tuple[str,...]] = {start}
    nodes = 0
    while q:
        s, p = q.popleft()
        nodes += 1
        if s == GOAL:
            return {'found': True, 'path': p, 'steps': len(p), 'nodes': nodes, 'time': time.time()-t0}
        for nb, m in neigh(s):
            if nb not in seen:
                seen.add(nb)
                q.append((nb, p + [m]))
    return {'found': False, 'path': [], 'steps': 0, 'nodes': nodes, 'time': time.time()-t0}

def dfs_limit(start: Tuple[str,...], limit: int=30) -> Dict:
    t0 = time.time()
    seen: Set[Tuple[str,...]] = set()
    nodes = 0
    res_path: Optional[List[str]] = None

    def dfs(s: Tuple[str,...], p: List[str], d: int) -> bool:
        nonlocal nodes, res_path
        nodes += 1
        seen.add(s)
        if s == GOAL:
            res_path = p.copy()
            return True
        if d >= limit:
            return False
        for nb, m in neigh(s):
            if nb not in seen:
                if dfs(nb, p + [m], d+1):
                    return True
        return False

    ok = dfs(start, [], 0)
    return {'found': ok, 'path': res_path or [], 'steps': len(res_path) if res_path else 0, 'nodes': nodes, 'time': time.time()-t0}

def main():
    s = rand_state()
    print('Initial state:\n', fmt(s))
    print('\nBFS...')
    r1 = bfs(s)
    print('BFS:', r1)
    print('\nDFS (limit=30)...')
    r2 = dfs_limit(s, 30)
    print('DFS:', r2)
    print('\nSummary:')
    print('BFS steps:', r1['steps'], 'nodes:', r1['nodes'], 'time:', r1['time'])
    print('DFS found:', r2['found'], 'steps:', r2['steps'], 'nodes:', r2['nodes'], 'time:', r2['time'])

if __name__ == '__main__':
    main()
