import click


@click.command()
@click.argument("file", type=click.Path(exists=True))
def main(file):
    click.echo("100")


if __name__ == "__main__":
    main()
