import os
from pathlib import Path
from typing import Dict

import tomllib
import xdg_base_dirs

from pyfix_imports.predefined import predefined_imports


def get_config_path() -> Path | None:
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
        if data["config"]:
            return data["config"]
        else:
            return {}
    except Exception:
        return {}


def config(given_path: Path | None) -> None:
    path = given_path or get_config_path()

    if path:
        if os.path.exists(path):
            data = config_parse(path)
            if data:
                return predefined_imports.update(data)
            else:
                return None
