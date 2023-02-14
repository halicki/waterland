import waterland.algorithm


def test_algorithm(grid):
    assert waterland.algorithm.count_islands(grid) == 4
