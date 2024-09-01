import os
import sys
from pathlib import Path

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


def config_parse(file: Path) -> dict[str, str] | dict:
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


def config_dict(user_path: Path | None) -> dict[str, str]:
    config_path = user_path or get_xdg_config_path()
    imports_dict = predefined_imports

    # config_path being None means user didnt pass a config file as an argument
    if config_path is not None and os.path.exists(config_path):
        data = config_parse(config_path)
        if data:
            imports_dict.update(data)
    return imports_dict
