"""Read a pathophysiology node's ``conforms_to`` references.

``conforms_to`` may be written as one string or as a list of strings: a node
that is a genuine instance of two module nodes names both (dismech#13923). The
schema accepts either spelling (an ``any_of`` over a string and a multivalued
string), so the ~3,500 scalar lines already in ``kb/`` never need migrating.

That leaves the scalar/list question to every reader, and a reader that checks
``isinstance(value, str)`` silently drops the list form instead of failing. So
this module is the only place it is answered: read ``conforms_to`` through
:func:`iter_conforms_to` rather than ``node.get("conforms_to")``.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def normalize_conforms_to(value: Any) -> list[str]:
    """Return a raw ``conforms_to`` value as a list of non-empty, stripped strings.

    ``None`` and empty values give ``[]``; a string gives a one-item list; a
    list keeps its order and its duplicates (duplicates are a curation defect
    for the KB tests to report, not something to hide here). Non-string items
    are dropped — schema validation is what rejects them.
    """
    if value is None:
        return []
    items = [value] if isinstance(value, str) else value
    if not isinstance(items, (list, tuple)):
        return []
    refs = []
    for item in items:
        if isinstance(item, str) and item.strip():
            refs.append(item.strip())
    return refs


def iter_conforms_to(node: Any) -> list[str]:
    """Every ``conforms_to`` reference on one node, in declared order."""
    if not isinstance(node, Mapping):
        return []
    return normalize_conforms_to(node.get("conforms_to"))


def module_stem(ref: str) -> str:
    """The module part of a ``module#Node Name`` reference."""
    return ref.split("#", 1)[0].strip()
