import pytest

import waterland.algorithm


def test_algorithm(grid):
    assert waterland.algorithm.count_islands(grid) == 4


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 0]], 0),
        ([[0, 1]], 1),
        ([[1, 1]], 1),
        ([[0, 1], [0, 0]], 1),
        ([[1, 0], [0, 1]], 1),
        ([[1, 1], [1, 0]], 1),
    ],
)
def test_algorithm2(grid, expected):
    assert waterland.algorithm.count_islands(grid) == expected
