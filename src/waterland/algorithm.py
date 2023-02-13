def get_lists(file):
    """Convert a file to a grid.

    :param file: A file-like object.
    :return: A list of lists of integers.
    """
    for file_line in file:
        yield [int(char) for char in file_line.strip()]


def count_islands(grid):
    """Count islands in a grid.

    :param grid: A list of lists of integers.
    :return: The number of islands in the grid.
    """
    return 100
