from pyfix_imports.package import import_string
from pyfix_imports.pyflake import pyflake

from tests.test import test_code


def imp_string(src):
    mod_list = pyflake(src)
    imports = set(import_string(mod_list))

    return imports


output = set("""
import numpy as np
from typing import List, Dict, Tuple, Optional
from collections import defaultdict, deque
from textwrap import dedent
import time
import random
import os
import collections
import itertools
from itertools import accumulate
""")


def test_string():
    assert imp_string(test_code) == output
