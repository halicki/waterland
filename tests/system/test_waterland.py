import subprocess


def test_pepita_grid():
    result = subprocess.run(
        ["python", "-m", "waterland", "tests/fixtures/pepita.txt"], capture_output=True
    )
    assert result.stdout == b"1\n"
