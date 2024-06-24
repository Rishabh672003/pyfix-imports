import importlib.util
from typing import Dict

from fix_imports.typing import types

common_statements: Dict[str, str] = {
    "ABC": "from abc import ABC",
    "abstractmethod": "from abc import abstractmethod",
    "BaseModel": "from pydantic import BaseModel  # noqa: E0611",
    "BeautifulSoup": "from bs4 import BeautifulSoup",
    "call": "from unittest.mock import call",
    "CaptureFixture": "from _pytest.capture import CaptureFixture",
    "CliRunner": "from click.testing import CliRunner",
    "copyfile": "from shutil import copyfile",
    "datetime": "from datetime import datetime",
    "dedent": "from textwrap import dedent",
    "Enum": "from enum import Enum",
    "Faker": "from faker import Faker",
    "FrozenDateTimeFactory": "from freezegun.api import FrozenDateTimeFactory",
    "LocalPath": "from py._path.local import LocalPath",
    "LogCaptureFixture": "from _pytest.logging import LogCaptureFixture",
    "Mock": "from unittest.mock import Mock",
    "ModelFactory": "from pydantic_factories import ModelFactory",
    "np": "import numpy as np",
    "Path": "from pathlib import Path",
    "pd": "import pandas as pd",
    "plt": "import matplotlib.pyplot as plt",
    "patch": "from unittest.mock import patch",
    "StringIO": "from io import StringIO",
    "suppress": "from contextlib import suppress",
    "tz": "from dateutil import tz",
    "YAMLError": "from yaml import YAMLError",
}


def packages(name) -> str:
    types_list = types

    if name in types_list:
        return f"from typing import {name}"

    if name in common_statements:
        return common_statements[name]

    package_specs = importlib.util.find_spec(name)

    try:
        importlib.util.module_from_spec(package_specs)  # type: ignore
    except AttributeError:
        return ""

    return f"import {name}"
