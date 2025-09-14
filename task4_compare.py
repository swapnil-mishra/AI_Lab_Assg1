"""Task 4: Compare BFS vs DFS on same initial grid

Generates a random start state, runs BFS and DFS on the same state, and
prints a comparison of steps, nodes explored, and execution time.
"""
from utils import rand_state, fmt
from task2_bfs import bfs
from task3_dfs import dfs_limit


def main():
    s = rand_state()
    print('Start state:\n', fmt(s))
    print('\nRunning BFS...')
    r1 = bfs(s)
    print('BFS:', r1)
    print('\nRunning DFS (limit=30)...')
    r2 = dfs_limit(s, limit=30)
    print('DFS:', r2)
    print('\nSummary:')
    print('BFS steps:', r1['steps'], 'nodes:', r1['nodes'], 'time:', r1['time'])
    print('DFS found:', r2['found'], 'steps:', r2['steps'], 'nodes:', r2['nodes'], 'time:', r2['time'])


if __name__ == '__main__':
    main()
