from pyfix_imports.config import config
from pyfix_imports.file import get_file_text
from pyfix_imports.package import import_string
from pyfix_imports.pyflake import pyflake


def fix_code(filename: str, config_file=None) -> str:
    """Fix the python source code of a file.

    Args:
        filename: path of file to be fixed.
        config_file(Optional): path of the config file

    Returns:
        Fixed code as a string original file is not touched.
    """
    config(config_file)
    output = get_file_text(filename)
    mod_list = pyflake(output)

    if mod_list:
        imports = import_string(mod_list)
        return imports + 2 * "\n" + output
    else:
        return output
