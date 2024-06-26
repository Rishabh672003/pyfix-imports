import os
import tomllib
from pathlib import Path
from typing import Any, Dict

import xdg_base_dirs

from pyfix_imports.predefined import predefined_imports


def get_config_path() -> Path:
    config_dir = xdg_base_dirs.xdg_config_home()
    config_path = Path(config_dir) / "pyfix-imports" / "config.toml"
    return config_path


def config_parse(file: Path) -> Dict[str, Any] | None:
    try:
        with open(file, "rb") as f:
            data = tomllib.load(f)
        return data
    except Exception:
        pass


def update_pred_imports(data: Dict[str, str]) -> None:
    if data:
        return predefined_imports.update(data)
    else:
        return None


def config(given_path: Path) -> None:
    if given_path is not None:
        if os.path.exists(given_path):
            data = config_parse(given_path)
            if data:
                update_pred_imports(data)
    elif os.path.exists(get_config_path()):
        default_config_data = config_parse(get_config_path())
        if default_config_data:
            update_pred_imports(default_config_data)
    else:
        pass
