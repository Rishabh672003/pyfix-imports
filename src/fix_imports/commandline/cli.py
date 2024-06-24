import click

from fix_imports.file import file_handling
from fix_imports.flake import flake
from fix_imports.package import packages


@click.command()
@click.argument("filename")
def cli(filename: str) -> None:
    output = file_handling(filename)
    mod_list = flake(output)

    imports = ""
    for mod_name in mod_list.values():
        for mod in mod_name:
            if packages(mod):
                imports += packages(mod).rstrip() + "\n"

    click.echo(imports + "\n" + output, nl=True)


if __name__ == "__main__":
    cli()
