import tomllib
from pathlib import Path
from typing import Dict

import xdg_base_dirs

from fix_imports.predefined import predefined_imports


def get_config_path() -> Path:
    config_dir = xdg_base_dirs.xdg_config_home()
    config_path = Path(config_dir) / "fix-imports" / "config.toml"
    return config_path


def config_parse(file: Path):
    try:
        with open(file, "rb") as f:
            data = tomllib.load(f)
    except Exception as e:
        print(f"Couln't open the file /n Exception occured: {e}")
        pass
    return data


def update_pred_imports(data: Dict[str, str]):
    return predefined_imports.update(data)
