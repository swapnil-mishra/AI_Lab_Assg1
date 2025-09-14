
# 8-Puzzle Solver (BFS and DFS)

This project implements a simple 8-puzzle solver using Breadth-First Search (BFS) and depth-limited Depth-First Search (DFS).

Author information
- Name: Swapnil Mishra
- Author: Swapnil Mishra
- College: Indian Institute of Technology, Patna
- Degree: Master Of Technology (M.Tech.)
- Stream: Computer Science Engineering (CSE)
- Semester: II
- Subject: Artificial Intelligence Lab
- Roll No.: 25s09res44
- Email Id: swapnil_25s09res44@iitp.ac.in

Current files
- `task1_random.py` — Task 1: generate a random solvable 3×3 grid and print it.
- `task2_bfs.py` — Task 2: BFS solver; prints path, steps, nodes explored, and time.
- `task3_dfs.py` — Task 3: depth-limited DFS solver; prints result and stats.
- `task4_compare.py` — Task 4: run BFS and DFS on the same initial state and compare metrics.
- `utils.py` — helper functions (state representation, neighbor generation, solvability check, formatting).
- `tests/` — unit tests for utils, BFS, DFS, and a compare smoke test.
- `test_results.txt` — captured sample test output.
- `requirements.txt` — dependencies used for tests and optional utilities.

Usage
Run the task scripts individually from the project root with Python 3 (PowerShell examples):

```powershell
python .\task1_random.py
python .\task2_bfs.py
python .\task3_dfs.py
python .\task4_compare.py
```

Run unit tests:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Notes
- DFS has a default depth limit of 30 (changeable in `task3_dfs.py`).
