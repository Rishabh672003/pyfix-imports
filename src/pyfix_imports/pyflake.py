import re
from typing import Any, Iterable, Set

import pyflakes.api
import pyflakes.messages
import pyflakes.reporter


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


def undefined_name(
    messages: Iterable[pyflakes.messages.Message],
) -> Set[str]:
    """Return undefined names."""
    pattern = re.compile(r"\'(.+?)\'")
    module_set = set()
    for message in messages:
        if isinstance(message, pyflakes.messages.UndefinedName):
            module_name = pattern.search(str(message))
            if module_name:
                module_name = module_name.group()[1:-1]
                module_set.add(module_name)
    return module_set


def pyflake(src: str) -> Set[str]:
    """Takes the filename as an argument and Returns the set of all undefined names"""
    flake_message = check(src)
    modules = undefined_name(flake_message)
    return modules
