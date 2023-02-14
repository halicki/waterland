import click

import waterland.algorithm
import waterland.conversion


@click.command()
@click.argument("file", type=click.Path(exists=True))
def main(file):
    with open(file) as f:
        grid = waterland.conversion.get_grid(f)

    count = waterland.algorithm.count_islands(grid)
    click.echo(count)


if __name__ == "__main__":
    main()
