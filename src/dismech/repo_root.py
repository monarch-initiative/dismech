"""Find the dismech checkout a command is operating on.

``Path(__file__).resolve().parents[N]`` names the tree the package was
*installed from*, which is not always the tree a command was run in. With one
virtualenv shared across git worktrees, an editable install points every
worktree at the primary checkout, so files written relative to ``__file__``
land there while the command reports success; a non-editable install puts
``parents[N]`` inside ``site-packages`` (#15051).

``repo_root()`` resolves from the working directory instead, which is also the
directory every ``just`` recipe runs in (the justfile's own directory), so a
recipe's ``data/...`` precondition checks and the Python it calls agree on one
tree.
"""

from __future__ import annotations

import functools
import logging
import os
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any, ClassVar

logger = logging.getLogger(__name__)

#: Environment variable naming the checkout explicitly. Wins over the
#: working directory when set.
ENV_VAR = "DISMECH_ROOT"


def is_repo_root(path: Path) -> bool:
    """True when ``path`` looks like the top of a dismech checkout."""
    return (path / "justfile").is_file() and (path / "kb").is_dir()


def find_repo_root(start: Path | None = None) -> Path | None:
    """Walk up from ``start`` (default: the working directory) to a checkout."""
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if is_repo_root(candidate):
            return candidate
    return None


def repo_root() -> Path:
    """The dismech checkout to read from and write to.

    ``$DISMECH_ROOT`` if set, else the nearest checkout at or above the working
    directory, else (with a warning) the tree this module was loaded from.
    """
    override = os.environ.get(ENV_VAR)
    if override:
        return Path(override).expanduser().resolve()
    found = find_repo_root()
    if found is not None:
        return found
    fallback = Path(__file__).resolve().parents[2]
    _warn_fallback(Path.cwd(), fallback)
    return fallback


@functools.cache
def _warn_fallback(cwd: Path, fallback: Path) -> None:
    """Log the fallback once per working directory, not once per path helper.

    Every module resolves its paths through ``repo_root()``, so one command can
    call it dozens of times. Tests that need the warning again call
    ``_warn_fallback.cache_clear()``.
    """
    logger.warning(
        "%s is not inside a dismech checkout (no justfile and kb/ found above "
        "it); using %s, the tree the dismech package was loaded from. Run from "
        "the checkout or set %s to choose one.",
        cwd,
        fallback,
        ENV_VAR,
    )


def is_in_working_tree(path: Path) -> bool:
    """True when ``path`` is inside the tree the command was run in.

    That tree is the checkout containing the working directory, or the working
    directory itself when it is not inside one.
    """
    base = find_repo_root() or Path.cwd().resolve()
    return path.resolve().is_relative_to(base)


class LazyRepoPaths:
    """Module-level path constants resolved from ``repo_root()`` when read.

    A constant such as ``DEFAULT_CACHE_DIR = repo_root() / "references_cache"``
    freezes whichever tree was current at import. Declaring it here instead
    keeps the public name importable while resolving it on every access::

        _PATHS = LazyRepoPaths(__name__, DEFAULT_CACHE_DIR=lambda r: r / "references_cache")
        __getattr__ = _PATHS.module_getattr

    Code inside the module reads ``_PATHS.get("DEFAULT_CACHE_DIR")``; a bare
    global would raise ``NameError``. A value assigned onto the module (as
    ``monkeypatch.setattr`` does) takes precedence over the factory.

    That precedence outlives the patch: ``monkeypatch`` undoes a patch by
    assigning the value it read beforehand, so the name stays in the module's
    ``__dict__``, frozen to whichever tree was current then, and the lazy
    lookup is never consulted again in that process (#15396).
    ``clear_all_overrides()`` drops such leftovers; ``tests/conftest.py`` calls
    it around every test.
    """

    #: Every instance, so the test suite can clear leftovers across modules.
    _instances: ClassVar[list[LazyRepoPaths]] = []

    def __init__(self, module_name: str, **factories: Callable[[Path], Any]):
        self._module_name = module_name
        self._factories = factories
        LazyRepoPaths._instances.append(self)

    def get(self, name: str) -> Any:
        module = sys.modules.get(self._module_name)
        override = vars(module).get(name) if module is not None else None
        if override is not None:
            return override
        return self._factories[name](repo_root())

    def module_getattr(self, name: str) -> Any:
        """A PEP 562 module ``__getattr__`` serving the declared names."""
        if name in self._factories:
            return self._factories[name](repo_root())
        raise AttributeError(f"module {self._module_name!r} has no attribute {name!r}")

    def clear_overrides(self) -> None:
        """Remove any declared name assigned onto the module, restoring the lazy lookup."""
        module = sys.modules.get(self._module_name)
        if module is not None:
            for name in self._factories:
                vars(module).pop(name, None)

    @classmethod
    def clear_all_overrides(cls) -> None:
        """``clear_overrides()`` on every instance."""
        for paths in cls._instances:
            paths.clear_overrides()
