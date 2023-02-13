from click.testing import CliRunner
from waterland.cli import main

def test_invoke_with_no_args_returns_help_info():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 2
    assert "Error: Missing argument 'FILE'." in result.output


def test_invoke_with_filename_but_no_file_present_returns_error():
    runner = CliRunner()
    result = runner.invoke(main, ["foo"])
    assert result.exit_code == 2
    assert "Error: Invalid value for 'FILE': Path 'foo' does not exist." in result.output


def test_invoke_with_filename_and_file_present_returns_success():
    runner = CliRunner()
    result = runner.invoke(main, ["./tests/integration/fixtures/valid.file"])
    assert result.exit_code == 0
    assert "100\n" == result.output
