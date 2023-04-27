"""Subprocess wrapper around the LKH3 binary.

LKH3 is a state-of-the-art TSP/VRP solver. This module:
- writes a problem instance to a TSPLIB-format file
- shells out to the LKH3 binary
- parses the output tour back into Python
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np


class LKH3NotFound(RuntimeError):
    pass


@dataclass(frozen=True)
class LKHSolution:
    tour: list[int]
    cost: float
    runs: int


def find_lkh3_binary() -> str:
    candidate = shutil.which("LKH") or shutil.which("LKH3")
    if not candidate:
        msg = "LKH3 binary not on PATH. Install from http://akira.ruc.dk/~keld/research/LKH-3/"
        raise LKH3NotFound(msg)
    return candidate


def _write_tsplib(
    distance_matrix: np.ndarray,
    name: str,
    out_dir: Path,
    scale: int = 1000,
) -> Path:
    n = distance_matrix.shape[0]
    p = out_dir / f"{name}.tsp"
    with p.open("w") as fh:
        fh.write(f"NAME : {name}\n")
        fh.write("TYPE : TSP\n")
        fh.write(f"DIMENSION : {n}\n")
        fh.write("EDGE_WEIGHT_TYPE : EXPLICIT\n")
        fh.write("EDGE_WEIGHT_FORMAT : FULL_MATRIX\n")
        fh.write("EDGE_WEIGHT_SECTION\n")
        for row in distance_matrix:
            fh.write(" ".join(str(int(v * scale)) for v in row) + "\n")
        fh.write("EOF\n")
    return p


def _write_par(
    problem_file: Path, tour_out: Path, runs: int, time_limit_s: int,
) -> Path:
    par = problem_file.with_suffix(".par")
    par.write_text(
        f"PROBLEM_FILE = {problem_file}\n"
        f"OUTPUT_TOUR_FILE = {tour_out}\n"
        f"RUNS = {runs}\n"
        f"TRACE_LEVEL = 0\n"
        f"TIME_LIMIT = {time_limit_s}\n"
    )
    return par


def solve_tsp(
    distance_matrix: np.ndarray,
    runs: int = 1,
    time_limit_s: int = 10,
) -> LKHSolution:
    binary = find_lkh3_binary()
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        prob = _write_tsplib(distance_matrix, "tsp", tmp_path)
        tour_out = tmp_path / "tour.txt"
        par = _write_par(prob, tour_out, runs, time_limit_s)
        subprocess.run([binary, str(par)], check=True, capture_output=True)
        return _parse_tour(tour_out, distance_matrix, runs)


def _parse_tour(tour_file: Path, distance_matrix: np.ndarray, runs: int) -> LKHSolution:
    lines = tour_file.read_text().splitlines()
    tour: list[int] = []
    in_section = False
    for line in lines:
        if line.strip() == "TOUR_SECTION":
            in_section = True
            continue
        if line.strip() in ("-1", "EOF"):
            break
        if in_section:
            tour.append(int(line.strip()) - 1)  # TSPLIB is 1-indexed
    cost = sum(
        distance_matrix[tour[i], tour[(i + 1) % len(tour)]] for i in range(len(tour))
    )
    return LKHSolution(tour=tour, cost=float(cost), runs=runs)
