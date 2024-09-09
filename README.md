# LKH3 Python Bindings

Thin Python wrapper around the LKH3 binary (Keld Helsgaun's Lin-Kernighan implementation). LKH3 is the state-of-the-art classical solver for TSP and many VRP variants; we use it as the quality ceiling baseline in our papers.

## Prerequisites

Install LKH3 from http://akira.ruc.dk/~keld/research/LKH-3/ and place the `LKH` binary on your PATH.

## Use

```python
import numpy as np
from lkh3 import solve_tsp

dist = np.array([[0, 1, 2], [1, 0, 3], [2, 3, 0]], dtype=float)
sol = solve_tsp(dist, runs=5, time_limit_s=10)
print(sol.tour, sol.cost)
```

## What this does

- Writes a TSPLIB-format `.tsp` problem file.
- Writes the corresponding `.par` parameter file.
- Shells out to the LKH binary.
- Parses the output tour file back into a Python list.

<!-- notes 2022-04 -->

<!-- notes 2022-07 -->

<!-- maint 2025-01-19 -->

<!-- maint 2025-02-26 -->

<!-- maint 2025-04-06 -->

<!-- maint 2025-05-16 -->

<!-- maint 2025-06-23 -->

<!-- maint 2025-08-02 -->

<!-- maint 2025-09-09 -->

<!-- maint 2025-10-19 -->

<!-- maint 2025-11-26 -->

<!-- maint 2024-01-24 -->

<!-- maint 2024-03-16 -->

<!-- maint 2024-05-08 -->

<!-- maint 2024-06-29 -->

<!-- maint 2024-08-19 -->

<!-- maint 2024-10-10 -->

<!-- maint 2024-12-02 -->

<!-- maint 2023-02-04 -->

<!-- maint 2023-04-09 -->

<!-- iter 2023-05-22-09 -->

<!-- iter 2023-05-22-11 -->

<!-- iter 2023-05-22-13 -->

<!-- iter 2023-05-22-15 -->

<!-- iter 2023-05-22-17 -->

<!-- iter 2023-05-22-19 -->

<!-- iter 2023-05-22-21 -->

<!-- iter 2023-05-22-22 -->

<!-- iter 2023-10-16-09 -->

<!-- iter 2023-10-16-11 -->

<!-- iter 2023-10-16-13 -->

<!-- iter 2023-10-16-15 -->

<!-- iter 2023-10-16-17 -->

<!-- iter 2023-10-16-19 -->

<!-- iter 2023-10-16-21 -->

<!-- iter 2023-10-16-22 -->

<!-- iter 2024-02-26-09 -->

<!-- iter 2024-02-26-11 -->

<!-- iter 2024-02-26-13 -->

<!-- iter 2024-02-26-15 -->

<!-- iter 2024-02-26-17 -->

<!-- iter 2024-02-26-19 -->

<!-- iter 2024-02-26-21 -->

<!-- iter 2024-02-26-22 -->

<!-- iter 2024-09-09-09 -->

<!-- iter 2024-09-09-11 -->

<!-- iter 2024-09-09-13 -->

<!-- iter 2024-09-09-15 -->
