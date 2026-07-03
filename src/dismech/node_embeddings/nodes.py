"""Extract pathophysiology nodes and render their embedding text."""

from __future__ import annotations

import glob
import os
from dataclasses import dataclass
from typing import Iterator

import yaml


def _term_labels(obj, out: list[str]) -> None:
    """Collect ``label`` from every ``{id, label}`` ontology-term dict in a tree."""
    if isinstance(obj, dict):
        if isinstance(obj.get("id"), str) and isinstance(obj.get("label"), str):
            out.append(obj["label"])
        for v in obj.values():
            _term_labels(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _term_labels(v, out)


def _dedup_keep_order(items: list[str]) -> list[str]:
    seen, out = set(), []
    for s in items:
        k = s.lower().strip()
        if s and k not in seen:
            seen.add(k)
            out.append(s)
    return out


@dataclass(frozen=True)
class PathoNode:
    """One pathophysiology node, with the parts needed to embed and evaluate it."""

    disease: str
    name: str
    conforms_to: str | None
    term_labels: tuple[str, ...]

    @property
    def text(self) -> str:
        """Embedding string: node label followed by its ontology term labels."""
        parts = _dedup_keep_order([self.name, *self.term_labels])
        return ". ".join(parts)


def iter_nodes(kb_dir: str = "kb/disorders") -> Iterator[PathoNode]:
    """Yield a :class:`PathoNode` for every pathophysiology node in ``kb_dir``.

    ``*.history.yaml`` snapshots are skipped.
    """
    for path in sorted(glob.glob(os.path.join(kb_dir, "*.yaml"))):
        if path.endswith(".history.yaml"):
            continue
        try:
            doc = yaml.safe_load(open(path))
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        disease = os.path.basename(path)[:-5]
        for node in doc.get("pathophysiology", []) or []:
            if not isinstance(node, dict):
                continue
            labels: list[str] = []
            _term_labels(node, labels)
            yield PathoNode(
                disease=disease,
                name=node.get("name", ""),
                conforms_to=node.get("conforms_to"),
                term_labels=tuple(_dedup_keep_order(labels)),
            )
