"""Embedding, cosine similarity, and ``conforms_to`` retrieval metrics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from dismech.node_embeddings.embedders import Embedder
from dismech.node_embeddings.nodes import PathoNode


def embed_nodes(nodes: Sequence[PathoNode], embedder: Embedder) -> np.ndarray:
    """Embed each node's :attr:`PathoNode.text`; returns ``(n, dim)`` float32."""
    return embedder.embed([n.text for n in nodes])


def l2_normalize(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix / (norms + 1e-9)


def cosine_matrix(embeddings: np.ndarray, fill_diagonal: float | None = -1.0) -> np.ndarray:
    """Full pairwise cosine-similarity matrix; self-similarity set to ``fill_diagonal``."""
    unit = l2_normalize(embeddings)
    sim = unit @ unit.T
    if fill_diagonal is not None:
        np.fill_diagonal(sim, fill_diagonal)
    return sim


def precision_at_k(sim: np.ndarray, labels: Sequence[str], k: int) -> tuple[float, int]:
    """Mean precision@k for retrieving same-label rows.

    Only rows whose label appears on >=2 nodes are scored (others have no
    possible hit). Returns ``(mean_precision, n_query_rows)``.
    """
    labels = list(labels)
    counts: dict[str, int] = {}
    for lab in labels:
        counts[lab] = counts.get(lab, 0) + 1
    scores = []
    for i, lab in enumerate(labels):
        if counts[lab] < 2:
            continue
        order = np.argsort(-sim[i])
        order = order[order != i][:k]
        hits = sum(labels[j] == lab for j in order)
        scores.append(hits / k)
    return (float(np.mean(scores)) if scores else 0.0), len(scores)


@dataclass
class GroupCosineSummary:
    same_mean: float
    diff_mean: float
    n_same: int
    n_diff: int

    @property
    def separation(self) -> float:
        return self.same_mean / self.diff_mean if self.diff_mean else float("inf")


def group_cosine_summary(sim: np.ndarray, labels: Sequence[str]) -> GroupCosineSummary:
    """Mean cosine for same-label vs different-label pairs (upper triangle)."""
    labels = list(labels)
    same, diff = [], []
    n = len(labels)
    for i in range(n):
        for j in range(i + 1, n):
            (same if labels[i] == labels[j] else diff).append(float(sim[i, j]))
    return GroupCosineSummary(
        same_mean=float(np.mean(same)) if same else 0.0,
        diff_mean=float(np.mean(diff)) if diff else 0.0,
        n_same=len(same),
        n_diff=len(diff),
    )
