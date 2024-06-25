import importlib.util
from typing import List

from fix_imports.predefined import predefined_imports


def collection_imports() -> List[str]:
    from collections import __all__

    return __all__


def typing() -> List[str]:
    from typing import __all__

    return __all__


def packages(name) -> str | None:
    types_list = typing()
    collection_list = collection_imports()

    if name in types_list:
        return f"from typing import {name}"

    if name in predefined_imports:
        return predefined_imports[name]

    if name in collection_list:
        return f"from collections import {name}"

    package_specs = importlib.util.find_spec(name)

    try:
        importlib.util.module_from_spec(package_specs)  # type: ignore
    except Exception:
        return None

    return f"import {name}"
