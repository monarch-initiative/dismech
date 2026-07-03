"""Tests for the per-patho-event node-embedding library.

The embedding pipeline is exercised with a deterministic in-process fake
backend (no network, no model download). Real backends (model2vec, openai) are
thin wrappers validated only at the spec-resolution level.
"""

from __future__ import annotations

import numpy as np
import pytest

from dismech.node_embeddings import (
    cosine_matrix,
    get_embedder,
    group_cosine_summary,
    iter_nodes,
    precision_at_k,
    register_backend,
)
from dismech.node_embeddings.nodes import PathoNode


# --------------------------------------------------------------------------- #
# node extraction + text rendering
# --------------------------------------------------------------------------- #
DISORDER_YAML = """\
name: Test Disease
pathophysiology:
- name: Macrophage Activation
  conforms_to: "fibrotic_response#Mesenchymal Cell Activation"
  cell_types:
  - preferred_term: Macrophage
    term:
      id: CL:0000235
      label: macrophage
  biological_processes:
  - preferred_term: Inflammation
    term:
      id: GO:0006954
      label: inflammatory response
- name: Bare Node
"""


def test_iter_nodes_extracts_text_and_labels(tmp_path):
    (tmp_path / "Test_Disease.yaml").write_text(DISORDER_YAML)
    (tmp_path / "Old.history.yaml").write_text(DISORDER_YAML)  # must be skipped

    nodes = list(iter_nodes(str(tmp_path)))
    assert len(nodes) == 2  # history file skipped

    activation = nodes[0]
    assert activation.disease == "Test_Disease"
    assert activation.conforms_to == "fibrotic_response#Mesenchymal Cell Activation"
    # text = node label + ontology term labels (not preferred_terms)
    assert activation.text == "Macrophage Activation. macrophage. inflammatory response"
    assert nodes[1].conforms_to is None
    assert nodes[1].text == "Bare Node"


def test_text_dedup_is_case_insensitive():
    node = PathoNode("D", "Inflammation", None, ("inflammation", "Fibrosis"))
    assert node.text == "Inflammation. Fibrosis"


# --------------------------------------------------------------------------- #
# retrieval metrics
# --------------------------------------------------------------------------- #
def test_precision_at_k_and_group_summary():
    # rows 0,1 share label A and are identical; row 2 is label B
    emb = np.array([[1.0, 0.0], [1.0, 0.0], [0.0, 1.0]], dtype=np.float32)
    labels = ["A", "A", "B"]
    sim = cosine_matrix(emb)

    p1, nq = precision_at_k(sim, labels, k=1)
    assert p1 == 1.0  # each A's nearest is the other A
    assert nq == 2  # only the two A rows have a labelled peer

    s = group_cosine_summary(sim, labels)
    assert s.same_mean > s.diff_mean
    assert s.separation > 1.0


# --------------------------------------------------------------------------- #
# pluggable backends
# --------------------------------------------------------------------------- #
class _HashEmbedder:
    """Deterministic fake backend: stable pseudo-embedding per string."""

    name = "fake"

    def __init__(self, dim: int = 16):
        self.dim = dim

    def embed(self, texts):
        out = np.zeros((len(texts), self.dim), dtype=np.float32)
        for i, t in enumerate(texts):
            rng = np.random.default_rng(abs(hash(t)) % (2**32))
            out[i] = rng.standard_normal(self.dim)
        return out


def test_get_embedder_resolves_spec_and_model():
    e = get_embedder("model2vec:minishlab/potion-base-32M")
    assert e.model_id == "minishlab/potion-base-32M"
    assert e.name == "model2vec:minishlab/potion-base-32M"

    o = get_embedder("openai")  # default model, no key needed until embed()
    assert o.model_id == "text-embedding-3-small"

    ada = get_embedder("openai:text-embedding-ada-002")
    assert ada.name == "openai:text-embedding-ada-002"


def test_get_embedder_unknown_backend_raises():
    with pytest.raises(ValueError, match="unknown embedding backend"):
        get_embedder("nope")


def test_register_and_use_custom_backend():
    register_backend("fake", _HashEmbedder)
    embedder = get_embedder("fake")
    nodes = [
        PathoNode("D1", "alpha", "M#X", ()),
        PathoNode("D2", "alpha", "M#X", ()),  # identical text -> identical embedding
        PathoNode("D3", "totally different beta gamma", "M#Y", ()),
    ]
    sim = cosine_matrix(embedder.embed([n.text for n in nodes]))
    # identical-text same-label pair must be the most similar off-diagonal entry
    assert sim[0, 1] == pytest.approx(1.0, abs=1e-5)
    assert sim[0, 1] > sim[0, 2]
