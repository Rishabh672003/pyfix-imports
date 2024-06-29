from pyfix_imports.config import config
from pyfix_imports.file import get_file_text
from pyfix_imports.package import import_string
from pyfix_imports.pyflake import pyflake


def fix_code(filename: str, config_file) -> str:
    config(config_file)
    output = get_file_text(filename)
    mod_list = pyflake(output)

    if mod_list:
        imports = import_string(mod_list)
        return imports + 2 * "\n" + output
    else:
        return output
