import click


@click.command()
@click.argument("filename")
def echo_file(filename) -> str:
    click.echo(filename)
    return filename


def cli():
    echo_file()
