import os
import sys
from pathlib import Path
from typing import Dict

import tomllib
import xdg_base_dirs

from pyfix_imports.predefined import predefined_imports


def get_xdg_config_path() -> Path | None:
    try:
        config_dir = xdg_base_dirs.xdg_config_home()
        config_path = Path(config_dir) / "pyfix-imports" / "config.toml"
        return config_path
    except Exception:
        return None


def config_parse(file: Path) -> Dict[str, str] | Dict:
    try:
        with open(file, "rb") as f:
            data = tomllib.load(f)
            return data["config"] if data["config"] else {}
    except Exception as e:
        print(
            f"""\nAn exception occured while parsing the config, config file wasnt used to fix the imports.
Exception: {e}\n""",
            file=sys.stderr,
        )
        return {}


def config_dict(user_path: Path | None) -> Dict[str, str]:
    path = user_path or get_xdg_config_path()
    imports_dict = predefined_imports

    if path is not None and os.path.exists(path):
        data = config_parse(path)
        if data:
            imports_dict.update(data)
    return imports_dict
