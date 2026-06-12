"""Per-patho-event (pathophysiology node) text embeddings.

Each pathophysiology node is turned into a single string (node label plus its
ontology term labels) and embedded with a pluggable text-embedding backend.
The node -- not the disease -- is the reusable mechanistic unit (the same unit
the ``conforms_to`` mechanism-module links describe), so node embeddings recover
conserved patho-events across diseases and can suggest module membership.

Public API::

    from dismech.node_embeddings import get_embedder, iter_nodes, embed_nodes

    nodes = list(iter_nodes("kb/disorders"))
    embedder = get_embedder("openai:text-embedding-3-small")   # or "model2vec"
    matrix = embed_nodes(nodes, embedder)

Embedding backends are pluggable; see :mod:`dismech.node_embeddings.embedders`.
"""

from __future__ import annotations

from dismech.node_embeddings.embedders import (
    Embedder,
    OpenAIEmbedder,
    StaticEmbedder,
    get_embedder,
    register_backend,
)
from dismech.node_embeddings.nodes import PathoNode, iter_nodes
from dismech.node_embeddings.similarity import (
    cosine_matrix,
    embed_nodes,
    group_cosine_summary,
    precision_at_k,
)

__all__ = [
    "Embedder",
    "StaticEmbedder",
    "OpenAIEmbedder",
    "get_embedder",
    "register_backend",
    "PathoNode",
    "iter_nodes",
    "embed_nodes",
    "cosine_matrix",
    "precision_at_k",
    "group_cosine_summary",
]
