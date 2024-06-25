import click

from fix_imports.file import file_handling
from fix_imports.flake import flake
from fix_imports.package import packages


@click.command()
@click.argument("filename")
def cli(filename: str) -> str | None:
    output = file_handling(filename)
    mod_list = flake(output)

    imports = ""
    for mod_name in mod_list.values():
        for mod in mod_name:
            pac = packages(mod)
            if pac is not None:
                imports += pac.rstrip() + "\n"

    if imports:
        click.echo(imports + "\n" + output, nl=True)
    else:
        click.echo(output, nl=True)

    return imports + "\n" + output + "\n"


if __name__ == "__main__":
    cli()
