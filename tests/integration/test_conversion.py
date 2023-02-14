from waterland.algorithm import get_grid


def test_get_lists_returns_a_list_of_lists_of_integers():
    with open("tests/integration/fixtures/valid_file.txt") as f:
        result = get_grid(f)

    assert result == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
    ]
