import itertools


def count_islands(grid):
    """Count islands in a grid.

    :param grid: A list of lists of integers.
    :return: The number of islands in the grid.
    """

    def point_within_grid(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[i])

    def point_is_land(i, j):
        return point_within_grid(i, j) and grid[i][j] == 1

    def mark_point_as_visited(i, j):
        grid[i][j] = 0

    def dfs(i, j):
        if point_is_land(i, j):
            mark_point_as_visited(i, j)
            list(
                itertools.starmap(
                    dfs,
                    [
                        (i - 1, j - 1),
                        (i - 1, j),
                        (i - 1, j + 1),
                        (i, j - 1),
                        (i, j + 1),
                        (i + 1, j - 1),
                        (i + 1, j),
                        (i + 1, j + 1),
                    ],
                )
            )

    islands_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if point_is_land(i, j):
                islands_count += 1
                dfs(i, j)

    return islands_count
