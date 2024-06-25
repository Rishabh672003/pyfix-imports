import click

from fix_imports.file import file_handling
from fix_imports.pyflake import pyflake
from fix_imports.package import import_string


@click.command()
@click.argument("filename")
def cli(filename: str) -> str | None:
    output = file_handling(filename)
    mod_list = pyflake(output)
    imports = import_string(mod_list)

    if imports:
        click.echo(imports + 2*"\n" + output, nl=True)
    else:
        click.echo(output, nl=True)

    return imports + "\n" + output + "\n"


if __name__ == "__main__":
    cli()
