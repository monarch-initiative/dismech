"""Shared YAML loading helpers backed by libyaml.

PyYAML ships two SafeLoader implementations: a pure-Python one (``yaml.SafeLoader``,
what ``yaml.safe_load`` uses) and a C one built on libyaml (``yaml.CSafeLoader``).
They accept the same documents and produce the same Python objects; the C loader is
simply an order of magnitude faster.

That gap is not academic here. The KB is ~1700 disorder files, and a single walk of
the corpus costs ~89s under the pure-Python loader versus ~7s under libyaml. Several
tests walk the whole corpus, so the parser choice dominated CI wall-clock time
(issue #7502).

``render.py``, ``export/utils.py``, and ``reference_snippet_audit.py`` each grew their
own copy of the loader shim (issue #5198). This module consolidates them so there is
one place to import from and one place to test.

Use :func:`safe_load` anywhere ``yaml.safe_load`` would have been used. When libyaml
is unavailable the module falls back to the pure-Python loader, so behaviour is
correct everywhere and merely slower.
"""

from __future__ import annotations

from pathlib import Path
from typing import IO, Any

import yaml

try:  # pragma: no cover - exercised implicitly wherever YAML is loaded
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover - only when libyaml is not built
    from yaml import SafeLoader  # type: ignore[assignment]

__all__ = ["HAVE_LIBYAML", "SafeLoader", "safe_load", "safe_load_path"]

#: Whether the fast libyaml-backed loader is in use. Informational only — callers
#: get correct results either way.
HAVE_LIBYAML = SafeLoader is not yaml.SafeLoader


def safe_load(stream: str | bytes | IO[str] | IO[bytes]) -> Any:
    """Drop-in replacement for :func:`yaml.safe_load` using the fastest safe loader."""
    return yaml.load(stream, Loader=SafeLoader)


def safe_load_path(path: str | Path, encoding: str = "utf-8") -> Any:
    """Read and parse a YAML file.

    Convenience for the very common ``safe_load(path.read_text())`` pairing, and
    the reason it pins ``utf-8`` rather than inheriting the platform's locale
    default the way a bare ``read_text()`` does.
    """
    return safe_load(Path(path).read_text(encoding=encoding))
