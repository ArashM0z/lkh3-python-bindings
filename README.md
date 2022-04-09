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
