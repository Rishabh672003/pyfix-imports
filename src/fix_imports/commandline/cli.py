import click


@click.command()
@click.argument("filename")
def echo_file(filename):
    click.echo(filename)


if __name__ == "__main__":
    echo_file()
