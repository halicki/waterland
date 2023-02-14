from click.testing import CliRunner
import waterland.cli


def test_pepita_grid():
    cli = CliRunner()
    result = cli.invoke(waterland.cli.main, ["./tests/fixtures/pepita.txt"])
    assert result.output == "1\n"
