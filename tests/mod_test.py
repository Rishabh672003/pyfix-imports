from pyfix_imports.pyflake import pyflake

from tests.test import test_code


def check_code(output):
    mod_list = pyflake(output)

    if mod_list:
        return mod_list
    else:
        return {}


def test_code_output():
    assert check_code(test_code) == {
        "defaultdict",
        "Tuple",
        "List",
        "mp",
        "Optional",
        "accumulate",
        "time",
        "np",
        "deque",
        "os",
        "itertools",
        "Dict",
        "dedent",
        "collections",
        "random",
    }
