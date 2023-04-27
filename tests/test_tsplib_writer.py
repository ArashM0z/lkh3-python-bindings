"""Test the TSPLIB writer without requiring LKH3 to be installed."""
import tempfile
from pathlib import Path

import numpy as np

from lkh3.bindings import _write_tsplib


def test_tsplib_format() -> None:
    dist = np.array([[0, 1, 2], [1, 0, 3], [2, 3, 0]], dtype=float)
    with tempfile.TemporaryDirectory() as tmp:
        path = _write_tsplib(dist, "test", Path(tmp))
        content = path.read_text()
        assert "NAME : test" in content
        assert "DIMENSION : 3" in content
        assert "EDGE_WEIGHT_TYPE : EXPLICIT" in content
