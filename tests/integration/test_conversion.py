from waterland.conversion import get_grid


def test_get_lists_returns_a_list_of_lists_of_integers(grid):
    with open("tests/fixtures/valid_file.txt") as f:
        result = get_grid(f)

    assert result == grid
