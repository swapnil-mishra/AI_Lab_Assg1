
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

Table of Contents
1. Introduction
2. Problem Formulation
3. Implementation Details
4. Code Explanation
5. Results & Observations
6. Conclusion
7. References
8. Appendix (Source Code)

## 1. Introduction

The 8-puzzle is a classical problem in Artificial Intelligence that involves a 3x3 grid with 8 numbered tiles and one empty space. The objective is to reach a goal configuration from a given starting configuration by sliding tiles into the empty space.

This report presents an implementation of the 8-puzzle solver using two fundamental search strategies: Breadth-First Search (BFS) and Depth-First Search (DFS). Both are state-space search algorithms, but they differ in terms of optimality, memory usage, and efficiency. Through this assignment, the performance of BFS and DFS is evaluated and compared.

The project demonstrates the importance of choosing the right algorithm for search-based AI problems, laying the foundation for more advanced algorithms such as A* search.

## 2. Problem Formulation

The 8-puzzle can be defined as a state-space search problem with the following components:

- Initial State: Any valid configuration of the 3x3 grid.
- Goal State: Typically, tiles arranged in order with the empty tile at the end.
- Operators: Moving a tile into the adjacent empty space (Up, Down, Left, Right).
- State Space: All possible valid configurations of the 8-puzzle (9! = 362,880 states).
- Solvability: Not all random configurations are solvable. The solvability condition is checked using inversion count.

This formulation makes the problem suitable for uninformed search strategies like BFS and DFS, which explore the state space differently.

## 3. Implementation Details

The project consists of the following modules:

- `task1_random.py`: Generates a random solvable 3x3 grid for the puzzle.
- `task2_bfs.py`: Implements BFS to find the solution path, steps, nodes explored, and execution time.
- `task3_dfs.py`: Implements Depth-Limited DFS solver with statistics output.
- `task4_compare.py`: Runs BFS and DFS on the same puzzle input and compares results.
- `utils.py`: Provides utility functions like state representation, solvability check, and formatting.

## 4. Code Explanation

Each task file contains the following implementations:

1. `task1_random.py`: Generates a random solvable 8-puzzle configuration.
2. `task2_bfs.py`: Uses Breadth-First Search to find the optimal solution path.
3. `task3_dfs.py`: Uses Depth-Limited DFS to explore puzzle states.
4. `task4_compare.py`: Runs BFS and DFS on the same puzzle instance and compares performance metrics.
5. `utils.py`: Provides helper functions such as generating neighbors, checking solvability, and formatting states.

BFS guarantees the shortest path but consumes high memory due to queue storage. DFS uses less memory but may not find the optimal solution if depth is limited. The implementation highlights these trade-offs.

## 5. Results & Observations (sample run)

Start state:

1 7 3
5 2 6
8 4 B

Running BFS...

BFS: {'found': True, 'path': ['Up', 'Up', 'Left', 'Down', 'Left', 'Up', 'Right', 'Right', 'Down', 'Left', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Down'], 'steps': 20, 'nodes': 39261, 'time': 0.13866090774536133}

Running DFS (limit=30)...

DFS: {'found': True, 'path': ['Up', 'Up', 'Left', 'Down', 'Down', 'Left', 'Up', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Up', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Down', 'Right', 'Right'], 'steps': 24, 'nodes': 11706, 'time': 0.014851093292236328}

Summary:

BFS steps: 20 nodes: 39261 time: 0.13866090774536133

DFS found: True steps: 24 nodes: 11706 time: 0.014851093292236328

## 6. Conclusion

This assignment highlights the strengths and limitations of BFS and DFS in solving the 8-puzzle problem:

- BFS ensures an optimal solution but requires significant memory.
- DFS consumes less memory but may not always reach the solution, especially for deep search spaces.

In real-world applications like robotics and pathfinding, these algorithms form the foundation of problem-solving. Future work can extend this implementation to heuristic-based algorithms such as A* search, which combines the benefits of BFS with informed guidance to reduce search space.

## 7. References

- Repository Link: https://github.com/swapnil-mishra/AI_Lab_Assg1
- Russell, Stuart J., and Peter Norvig. _Artificial Intelligence: A Modern Approach_.
- Online tutorials and resources on BFS and DFS search algorithms in Python.

## 8. Appendix - Full Source Code

See the `tasks/` and `utils.py` files in the repository for the full source listing.


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

## Detailed Report

Below is a concise detailed report of the implementation, algorithms used, and code structure.

Overview

This project implements an 8-puzzle solver with two search algorithms:
- Breadth-First Search (BFS) — finds shortest solution in terms of moves.
- Depth-limited Depth-First Search (DFS) — explores depth-first with a depth cap to avoid infinite search.

File structure

- `task1_random.py` — random solvable start state generator.
- `task2_bfs.py` — BFS solver implementation and runner.
- `task3_dfs.py` — depth-limited DFS implementation and runner.
- `task4_compare.py` — runs BFS and DFS on the same start and compares metrics.
- `utils.py` — shared helpers: goal state, solvability check, neighbor generation, pretty-formatting.

Implementation details

Design contract

- Inputs: a start state (9-tuple of strings where 'B' indicates the blank tile).
- Outputs: result dicts containing: found (bool), path (list of moves), steps (int), nodes (int), time (float).
- Error modes: unsolvable start (algorithms will exhaust search and report not found); DFS may not find solutions beyond its depth limit.

Edge cases considered

- Unsolvable boards (checked with inversion parity in the helper function).
- DFS guard with a depth limit to prevent infinite recursion / extremely deep search.
- State deduplication in BFS/DFS via `seen` sets to avoid revisiting states.

Helpers (high level)

- `utils.py` contains `GOAL`, `solvable`, `rand_state`, `fmt`, and `neigh`. `solvable` uses inversion parity for 3x3 puzzles. `neigh` yields neighbor states and the move label.

BFS

- Uses a `collections.deque` queue. Tracks visited states with a `set`. Returns on reaching the goal with metrics including nodes visited and elapsed time.

DFS (depth-limited)

- Recursive DFS with an explicit depth counter and a `seen` set. Stops when depth reaches the provided limit.

Comparison

- `task4_compare.py` runs both solvers on the same random initial state and prints a short summary comparing steps, nodes explored, and run time.

How to run

Run individual tasks (PowerShell):

```powershell
python .\task1_random.py
python .\task2_bfs.py
python .\task3_dfs.py
python .\task4_compare.py
```

Run tests:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Notes

- DFS default limit is conservative (30). Increase if you need deeper search but expect longer runtime.
- For practical performance on larger instances, implement A* with Manhattan distance.

---





