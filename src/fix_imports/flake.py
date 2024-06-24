import re
from collections import defaultdict
from typing import Any, DefaultDict, Iterable, List

import pyflakes.api
import pyflakes.messages
import pyflakes.reporter

"""
code taken from the autoflake
"""


class StubFile:
    """Stub out file for pyflakes."""

    def write(self, *_: Any) -> None:
        """Stub out."""


class ListReporter(pyflakes.reporter.Reporter):
    """Accumulate messages in messages list."""

    def __init__(self) -> None:
        """Initialize.

        Ignore errors from Reporter.
        """
        ignore = StubFile()
        pyflakes.reporter.Reporter.__init__(self, ignore, ignore)
        self.messages: list[pyflakes.messages.Message] = []

    def flake(self, message: pyflakes.messages.Message) -> None:
        """Accumulate messages."""
        self.messages.append(message)


def check(source: str) -> Iterable[pyflakes.messages.Message]:
    reporter = ListReporter()
    try:
        pyflakes.api.check(source, filename="<string>", reporter=reporter)
    except (AttributeError, RecursionError, UnicodeDecodeError):
        pass
    return reporter.messages


def unused_import_module_name(
    messages: Iterable[pyflakes.messages.Message],
) -> Iterable[tuple[int, str]]:
    """Yield line number and module name of unused imports."""
    pattern = re.compile(r"\'(.+?)\'")
    for message in messages:
        if isinstance(message, pyflakes.messages.UnusedImport):
            module_name = pattern.search(str(message))
            if module_name:
                module_name = module_name.group()[1:-1]
                yield (message.lineno, module_name)


def undefined_name(
    messages: Iterable[pyflakes.messages.Message],
) -> DefaultDict[str, List[str]]:
    """Yield line number and module name of unused imports."""
    pattern = re.compile(r"\'(.+?)\'")
    module_dict = defaultdict(list)
    for message in messages:
        if isinstance(message, pyflakes.messages.UndefinedName):
            module_name = pattern.search(str(message))
            if module_name:
                module_name = module_name.group()[1:-1]
                module_dict[message.lineno].append(module_name)
    return module_dict


def flake(src: str) -> DefaultDict[str, List[str]]:
    flake_message = check(src)
    modules = undefined_name(flake_message)
    return modules
