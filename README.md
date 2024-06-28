# PyFix-Imports

WIP Python library which fixes missing imports, It automatically fixes missing imports by importing them
I mostly wrote this to learn more about python, and wanted to make something with.

https://github.com/Rishabh672003/fix-imports/assets/53911515/941f0b59-a4d0-498f-89a4-0104a2eae92f

## Installation

Just run `pip install pyfix-imports`

## Usage

Just running `pyfix-imports <FILENAME>` will just print the fixed code to the stdout.
If you want to update the file in-place use the -f/--fix option `pyfix-imports -c <FILENAME>`

I recommend after running the program use [isort](https://pycqa.github.io/isort/) to sort the imports.

## Configuration

The default configuration file should be placed in `$XDG_CONFIG_HOME/pyfix-imports/config.toml`
or you can place your config file anywhere and just provide the path to the command `fix-imports -c <Path>`
the structure should be like this, don't forget to include [config] on the top

```toml
[config]
"tf" = "import tensorflow as tf"
"plt" = "import matplotlib.pyplot as plt"
"isprime" = "from sympy import isprime"
```

## How I use it

As they say necessity is the mother of invention, also python language server like, pyright and pylsp don't do that good
of a job, that gave me the motivation to made this. I use this with the conjunction of black and isort within my neovim
with [conform.nvim](https://github.com/stevearc/conform.nvim) you can also use it just put this in your conform setup

```lua
require("conform").setup({
    formatters_by_ft = {
    python = { "pyfix_imports", "ruff", "isort" },
    formatters = {
        pyfix_imports = {
            command = "pyfix-imports",
            args = { "$FILENAME" },
            cwd = require("conform.util").root_file({ "requirements.txt", "pyproject.toml" }),
        },
    })
```

## References

I took many projects for reference/code

- [autoimport](https://lyz-code.github.io/autoimport/) I could have just used this, but I wanted to make something so
  took it as a reference and made this. I didn't took that much code from it, but yes as someone who has never made a
  decent size python project it was really helpful
- [autoflake](https://pypi.org/project/autoflake/) I wanted to use pyflakes to get the errors in code, and this one had
  great implementation of pyflake api.
- [pyflakes](https://pypi.org/project/pyflakes/) Used this to get all the errors for undefined names.
- [click](https://click.palletsprojects.com/en/8.1.x/) Used this to make the command-line interface
- [pdm](https://github.com/pdm-project/pdm) Used this to structure and manage dependency for the project
- [xdg-base-dirs](https://github.com/srstevenson/xdg-base-dirs) Used this to get the config file
