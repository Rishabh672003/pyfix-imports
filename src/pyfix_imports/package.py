import importlib.util
from typing import FrozenSet

from pyfix_imports.predefined import predefined_imports


def get_modules_all(mod_name: str) -> FrozenSet[str]:
    __all__ = getattr(__import__(mod_name), "__all__")
    return frozenset(__all__)


def get_methods_all(mod_name: str) -> FrozenSet[str]:
    classes = __import__(mod_name)
    return frozenset(
        [attr for attr in dir(classes) if callable(getattr(classes, attr))]
    )


def is_package(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def import_string(mod_set) -> str:
    modules_all = {
        "predefined": predefined_imports,
        "typing": get_modules_all("typing"),
        "collections": get_modules_all("collections"),
        "textwrap": get_modules_all("textwrap"),
        "itertools": get_methods_all("itertools"),
    }
    imports_dict = {
        "predefined": [],
        "typing": [],
        "collections": [],
        "textwrap": [],
        "itertools": [],
        "others": [],
    }

    for mod in mod_set:
        found = False
        for module_type, modules in modules_all.items():
            if mod in modules:
                imports_dict[module_type].append(mod)
                found = True
                break
        if not found and is_package(mod):
            imports_dict["others"].append(mod)

    import_statements = []
    for module_type, modules in imports_dict.items():
        if module_type == "predefined" and modules:
            import_statements.extend(predefined_imports[mod] for mod in modules)
        elif module_type == "others" and modules:
            import_statements.extend(f"import {mod}" for mod in modules)
        elif modules:
            import_statements.append(f"from {module_type} import {', '.join(modules)}")

    return "\n".join(import_statements)
