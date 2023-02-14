def get_grid(file):
    """Convert a file to a grid.

    :param file: A file-like object.
    :return: A list of lists of integers.
    """
    return [[int(char) for char in file_line.strip()] for file_line in file]
