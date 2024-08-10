from pathlib import Path
from typing import Dict, Set

from pyfix_imports.config import config_dict
from pyfix_imports.file import get_file_text
from pyfix_imports.package import import_string
from pyfix_imports.pyflake import pyflake


def fix_code(filename: str, config_file: Path | None = None) -> str:
    """ Fix the python source code of a file.

    Args:
        filename: path of file to be fixed.
        config_file(Optional): path of the config file.

    Returns:
        Fixed code as a string original file is not touched.
    """

    file_content: str = get_file_text(filename)
    mod_list: Set[str] = pyflake(file_content)
    import_dict: Dict[str, str] = config_dict(config_file)

    if mod_list:
        imports: str = import_string(mod_list, import_dict)
        return imports + "\n" + file_content
    else:
        return file_content
