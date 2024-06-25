# Fix-imports

WIP Python library which fixes missing imports, It automatically fixes missing imports by importing them
I mostly wrote this to learn more about python, and wanted to make something with.

## Installation

1. Clone the repository `git clone https://github.com/Rishabh672003/fix-imports.git`
2. Do `cd fix-imports`
3. Run `pipx install .`

## How I use it

As they say necessity is the mother of invention, also python language server like, pyright and pylsp don't do that good
of a job, that gave me the motivation to made this. I use this with the conjunction of black and isort within my neovim
with [conform.nvim](https://github.com/stevearc/conform.nvim) you can also use it just put this in your conform setup

```lua
require("conform").setup({
    formatters_by_ft = {
    python = { "fix_imports", "black", "isort" },
    formatters = {
        fix_imports = {
            command = "fix-imports",
            args = { "$FILENAME" },
            cwd = require("conform.util").root_file({ "requirements.txt", "pyproject.toml" }),
        },
    })
```
