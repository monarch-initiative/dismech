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

import logging
import os
from pathlib import Path

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
    logger.warning(
        "%s is not inside a dismech checkout (no justfile and kb/ found above "
        "it); using %s, the tree the dismech package was loaded from. Run from "
        "the checkout or set %s to choose one.",
        Path.cwd(),
        fallback,
        ENV_VAR,
    )
    return fallback


def is_in_working_tree(path: Path) -> bool:
    """True when ``path`` is inside the tree the command was run in.

    That tree is the checkout containing the working directory, or the working
    directory itself when it is not inside one.
    """
    base = find_repo_root() or Path.cwd().resolve()
    return path.resolve().is_relative_to(base)
