"""Report a full disk as an environment error, not as a content finding.

Several baseline gates (`check-snippet-length`, `check-title-snippets`,
`check-snippet-grading`, `check-reference-titles`) extract ``kb/`` at
``origin/main`` into a temporary directory to compute their grandfather set.
On a full disk that extraction raises ``OSError: [Errno 28] No space left on
device``, and the gate died with a traceback that read like a content failure
(dismech#13119). Parallel curation in several git worktrees is the usual way to
get there.

:func:`reports_disk_full` wraps a gate's ``main()`` so that a disk-full error
anywhere in the run prints one plain message saying it is the environment, and
exits :data:`EXIT_DISK_FULL` rather than 1 (findings) or a traceback. Any other
``OSError`` is re-raised unchanged.
"""

from __future__ import annotations

import errno
import functools
import sys
import tempfile
from collections.abc import Callable

__all__ = ["EXIT_DISK_FULL", "is_disk_full", "reports_disk_full"]

# sysexits.h EX_IOERR. Distinct from 1 (the gate found something) and from 75,
# which the term-validator wrapper already uses for "ontology service down".
EXIT_DISK_FULL = 74

# EDQUOT is the same failure seen through a per-user quota.
_DISK_FULL_ERRNOS = frozenset({errno.ENOSPC, errno.EDQUOT})


def is_disk_full(exc: BaseException) -> bool:
    """Whether *exc* is an out-of-space or out-of-quota ``OSError``."""
    return isinstance(exc, OSError) and exc.errno in _DISK_FULL_ERRNOS


def disk_full_message(gate: str, exc: OSError) -> str:
    where = f" while writing {exc.filename}" if exc.filename else ""
    return (
        f"{gate}: ENVIRONMENT ERROR, not a content finding: "
        f"{exc.strerror or exc}{where}.\n"
        f"The gate could not finish, so it has no opinion on the KB yet. "
        f"Free disk space and rerun. The temporary directory in use is "
        f"{tempfile.gettempdir()} (set TMPDIR to move it). Per-worktree .venv "
        f"directories are a common cause (dismech#13119)."
    )


def reports_disk_full(gate: str) -> Callable[[Callable[..., int]], Callable[..., int]]:
    """Decorate a gate's ``main()`` to report a full disk as an environment error."""

    def decorate(main: Callable[..., int]) -> Callable[..., int]:
        @functools.wraps(main)
        def wrapper(*args, **kwargs) -> int:
            try:
                return main(*args, **kwargs)
            except OSError as exc:
                if not is_disk_full(exc):
                    raise
                print(disk_full_message(gate, exc), file=sys.stderr)
                return EXIT_DISK_FULL

        return wrapper

    return decorate
