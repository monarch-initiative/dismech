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

from collections.abc import Iterator
from pathlib import Path
from typing import IO, Any

import yaml

try:  # pragma: no cover - exercised implicitly wherever YAML is loaded
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover - only when libyaml is not built
    from yaml import SafeLoader  # type: ignore[assignment]

__all__ = [
    "HAVE_LIBYAML",
    "SafeLoader",
    "find_duplicate_keys",
    "safe_load",
    "safe_load_path",
]

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


def _walk_nodes(node: Any, path: str) -> Iterator[tuple[str, str, int]]:
    """Yield ``(path, key, line)`` for every duplicated key at or below ``node``."""
    if isinstance(node, yaml.MappingNode):
        seen: set[str] = set()
        for key_node, value_node in node.value:
            raw = getattr(key_node, "value", None)
            # A scalar key composes to a str. A YAML *complex* key (``? [a, b]``)
            # composes to a sequence/mapping node whose value is a list, which is
            # unhashable — fall back to its repr so an exotic document cannot
            # crash a check that runs over the whole corpus on every build.
            key = raw if isinstance(raw, str) else repr(raw)
            if key in seen:
                yield (path or "<document root>", key, key_node.start_mark.line + 1)
            seen.add(key)
            yield from _walk_nodes(value_node, f"{path}.{key}" if path else key)
    elif isinstance(node, yaml.SequenceNode):
        for index, child in enumerate(node.value):
            yield from _walk_nodes(child, f"{path}[{index}]")


def find_duplicate_keys(text: str) -> list[tuple[str, str, int]]:
    """Return every duplicated mapping key in ``text`` as ``(path, key, line)``.

    PyYAML's safe loaders — the ones the rest of this codebase uses — accept a
    duplicated mapping key silently and keep the *last* value. That makes a
    duplicate invisible to every test and renderer here, while the ruamel-backed
    ``linkml-reference-validator`` rejects the same file outright.

    The gap has teeth because duplicates arrive by *merge*, not by authoring: two
    concurrent PRs each adding a ``classifications:`` block at a different point in
    one file merge without a git conflict and produce a document no strict parser
    will read. Both PRs pass their own CI; main goes red afterwards (issue #8623).

    This composes the node tree rather than constructing objects, so it stays cheap
    enough to run over the whole corpus.
    """
    return list(_walk_nodes(yaml.compose(text, Loader=SafeLoader), ""))
