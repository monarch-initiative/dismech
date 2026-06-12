#!/usr/bin/env python3
"""Per-patho-event (node) embeddings, the simple way.

For each pathophysiology node: build one string from the node label plus its
ontology term labels, and embed that string with a static text embedder
(model2vec). No fusion, no matching, no graph context -- just embed the string.

Validation uses the repo's own `conforms_to` links as ground truth: nodes that
declare the same module#Node target are "the same conserved patho-event", so a
good node embedding should retrieve same-target nodes as nearest neighbours.

Run:
  uv run --with model2vec --with numpy python scripts/node_embeddings.py
"""
import glob
import os

import numpy as np
import yaml
from model2vec import StaticModel

DISORDER_DIR = "kb/disorders"


def term_labels(obj, out):
    if isinstance(obj, dict):
        if isinstance(obj.get("id"), str) and isinstance(obj.get("label"), str):
            out.append(obj["label"])
        for v in obj.values():
            term_labels(v, out)
    elif isinstance(obj, list):
        for v in obj:
            term_labels(v, out)


def collect_nodes():
    nodes = []  # (disease, node_name, conforms_to, string)
    for path in sorted(glob.glob(os.path.join(DISORDER_DIR, "*.yaml"))):
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
            name = node.get("name", "")
            labels = []
            term_labels(node, labels)
            # string = node label + ontology term labels (dedup, keep order)
            seen, parts = set(), []
            for s in [name] + labels:
                k = s.lower().strip()
                if s and k not in seen:
                    seen.add(k)
                    parts.append(s)
            string = ". ".join(parts)
            ct = node.get("conforms_to")
            nodes.append((disease, name, ct, string))
    return nodes


def precision_at_k(sim, labels, k):
    """Mean precision@k over query nodes that have a labelled peer."""
    n = len(labels)
    by_label = {}
    for i, l in enumerate(labels):
        by_label.setdefault(l, 0)
        by_label[l] += 1
    scores = []
    for i in range(n):
        if by_label[labels[i]] < 2:  # no other node shares its module -> skip
            continue
        order = np.argsort(-sim[i])
        order = order[order != i][:k]
        hits = sum(labels[j] == labels[i] for j in order)
        scores.append(hits / k)
    return float(np.mean(scores)), len(scores)


def main():
    nodes = collect_nodes()
    total = len(nodes)
    labelled = [(d, nm, ct, s) for d, nm, ct, s in nodes if ct]
    print(f"pathophysiology nodes total      : {total}")
    print(f"nodes with conforms_to (labelled): {len(labelled)}")

    strings = [s for *_, s in labelled]
    labels = [ct for _, _, ct, _ in labelled]
    diseases = [d for d, *_ in labelled]
    n_targets = len(set(labels))
    print(f"distinct conforms_to targets     : {n_targets}")

    model = StaticModel.from_pretrained("minishlab/potion-base-8M")
    E = model.encode(strings)
    E = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)
    sim = E @ E.T
    np.fill_diagonal(sim, -1.0)

    # same-target vs different-target cosine separation
    same, diff = [], []
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            (same if labels[i] == labels[j] else diff).append(float(sim[i, j]))
    print(f"\nmean cosine  same-module pairs   : {np.mean(same):.3f}  (n={len(same)})")
    print(f"mean cosine  diff-module pairs   : {np.mean(diff):.3f}  (n={len(diff)})")

    for k in (1, 5, 10):
        p, nq = precision_at_k(sim, labels, k)
        print(f"precision@{k:<2}  : {p:.3f}   (over {nq} query nodes)")

    # cross-disease retrievals: nearest neighbour in a DIFFERENT disease
    print("\nExample nearest cross-disease neighbours (same module target):")
    shown = 0
    for i in np.random.default_rng(0).permutation(len(labels)):
        order = np.argsort(-sim[i])
        for j in order:
            if diseases[j] != diseases[i]:
                tag = "OK " if labels[i] == labels[j] else "x  "
                if labels[i] == labels[j]:
                    print(f"  {tag}{sim[i,j]:.2f}  [{labels[i].split('#')[0]}]  "
                          f"{diseases[i]}::{nodes_name(labelled,i)}  ~  "
                          f"{diseases[j]}::{nodes_name(labelled,j)}")
                    shown += 1
                break
        if shown >= 8:
            break


def nodes_name(labelled, i):
    return labelled[i][1]


if __name__ == "__main__":
    main()
