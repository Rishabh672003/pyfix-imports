from pathlib import Path

import click

from pyfix_imports.file import write_to_file
from pyfix_imports.fix_code import fix_code


@click.command()
@click.option(
    "-f", "--fix", is_flag=True, default=False, help="format the file in place"
)
@click.option(
    "-c",
    "--config-file",
    is_flag=False,
    type=click.Path(exists=True, dir_okay=False, readable=True),
    help="path of the config file",
)
@click.argument(
    "filename",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
def cli(filename: str, fix: bool, config_file: Path | None) -> str | None:
    fixed_code = fix_code(filename, config_file)

    if not fix:
        click.echo(fixed_code.lstrip(), nl=True)
    else:
        write_to_file(filename, fixed_code)
        click.echo("Written to file successfully")

    return None


if __name__ == "__main__":
    cli()
