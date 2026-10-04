#!/usr/bin/env python3
"""Learned de-novo factors: candidate NEW mechanism modules from residual structure.

The de-novo (unannotated-factor) half of the mechanism-as-hidden-variable model,
the complement of ``scripts/module_factor_model.py``'s anchored inference. Where
that scores diseases against the *curated* module signatures, this learns
*additional* latent factors for the phenotype co-occurrence the curated modules do
not capture -- each learned factor is a candidate for a mechanism module dismech
has not yet curated.

Method: a semi-supervised non-negative matrix factorization (the f-scLVM / expiMap
design). The disease x phenotype matrix X is factored as W @ H where H's first rows
are the curated module signatures, **held fixed**, and only the remaining k de-novo
rows of H (plus all of W) are learned. Holding the anchored rows fixed forces the
de-novo factors to explain only what the curated modules can't -- so a de-novo
factor is residual structure by construction, not a relabelling of a known module.

Each learned factor is reported by its top phenotypes (the candidate module's
clinical signature), the diseases that load on it (its would-be conformers), and a
**novelty** score -- the fraction of its top phenotypes not already in any curated
module -- so a curator can tell a genuinely uncovered mechanism from a cluster that
just re-expresses curated ones.

Honest caveats: NMF factors are phenotype co-occurrence clusters, not validated
mechanisms; many will be organ-system or ascertainment clusters rather than
conserved mechanisms, and the matrix is pathograph-derived so the factors inherit
curation coverage and bias. This is a lead generator for new modules, read and
adjudicated like the candidate-conformance worklist, not an autofill. k is chosen,
not principled.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np

from dismech.export import module_phenotype_anchors, synthvae_export
from module_factor_model import _module_vec, _module_signatures  # type: ignore


def _corpus_idf(disease_vecs: dict[str, dict[str, float]]) -> dict[str, float]:
    """Smoothed idf over the DISEASE corpus, defined for every phenotype.

    The de-novo model factorizes the whole disease x phenotype matrix, including
    phenotypes no curated module carries -- so, unlike the anchored model, it cannot
    reuse the module-only idf (which would zero every uncurated phenotype and make
    *discovering a new cluster impossible*). df is the number of diseases carrying
    the phenotype.
    """
    n = len(disease_vecs) or 1
    df: dict[str, int] = defaultdict(int)
    for vec in disease_vecs.values():
        for h in vec:
            df[h] += 1
    return {h: math.log((1 + n) / (1 + d)) + 1.0 for h, d in df.items()}


def _disease_vectors_and_labels(
    disorders_dir: Path,
) -> tuple[dict[str, dict[str, float]], dict[str, str]]:
    """disease -> {hpo: freq-prob}, plus a global hpo -> label map, in one KB pass."""
    vecs: dict[str, dict[str, float]] = {}
    labels: dict[str, str] = {}
    for yaml_path in sorted(disorders_dir.glob("*.yaml")):
        if yaml_path.name.endswith(".history.yaml"):
            continue
        rec = synthvae_export.disease_prior(yaml_path)
        if not rec:
            continue
        vec: dict[str, float] = {}
        for ph in rec["phenotypes"]:
            p = ph.get("probability")
            vec[ph["hpo_id"]] = 0.5 if p is None else float(p)
            if ph.get("label"):
                labels.setdefault(ph["hpo_id"], ph["label"])
        if vec:
            vecs[rec["dismech_name"]] = vec
    return vecs, labels


def _semisupervised_nmf(
    X: np.ndarray, H_anchor: np.ndarray, k: int, iters: int, seed: int
) -> tuple[np.ndarray, np.ndarray]:
    """Factor X ~= W @ [H_anchor ; H_denovo], learning W and the k de-novo rows only.

    Returns (W_denovo, H_denovo): the disease loadings on, and phenotype signatures
    of, the learned factors. Multiplicative (Lee-Seung) updates for ||X - WH||_F.
    """
    rng = np.random.default_rng(seed)
    n, p = X.shape
    a = H_anchor.shape[0]
    eps = 1e-9
    scale = float(np.sqrt(X.mean() / max(a + k, 1))) + eps
    W = rng.random((n, a + k)).astype(np.float64) * scale
    H_denovo = rng.random((k, p)).astype(np.float64) * scale

    for _ in range(iters):
        H = np.vstack([H_anchor, H_denovo]) if k else H_anchor
        # W update (all columns)
        W *= (X @ H.T) / ((W @ (H @ H.T)) + eps)
        if not k:
            continue
        # H update (de-novo rows only)
        H = np.vstack([H_anchor, H_denovo])
        W_denovo = W[:, a:]
        H_denovo *= (W_denovo.T @ X) / ((W_denovo.T @ (W @ H)) + eps)
    return W[:, a:], H_denovo


def build(
    modules_dir: Path,
    disorders_dir: Path,
    pathograph_dir: Path,
    *,
    k: int = 20,
    iters: int = 150,
    seed: int = 0,
    top_phenotypes: int = 12,
    top_diseases: int = 10,
) -> dict[str, Any]:
    anchors = module_phenotype_anchors.build(modules_dir, disorders_dir, pathograph_dir)["modules"]
    sig_counts, _ = _module_signatures(anchors)
    disease_vecs, labels = _disease_vectors_and_labels(disorders_dir)
    idf = _corpus_idf(disease_vecs)

    modules = [m for m in sig_counts if sig_counts[m]]
    diseases = sorted(disease_vecs)
    # phenotype column space: union of disease phenotypes and module signatures
    cols = sorted({h for v in disease_vecs.values() for h in v}
                  | {h for m in modules for h in sig_counts[m]})
    col_idx = {h: i for i, h in enumerate(cols)}
    module_phenos = {h for m in modules for h in sig_counts[m]}

    # X: idf-weighted disease x phenotype
    X = np.zeros((len(diseases), len(cols)), dtype=np.float64)
    for i, d in enumerate(diseases):
        for h, prob in disease_vecs[d].items():
            X[i, col_idx[h]] = prob * idf.get(h, 0.0)

    # H_anchor: curated module signatures (support-damped * idf), L2-normalized rows
    H_anchor = np.zeros((len(modules), len(cols)), dtype=np.float64)
    for r, m in enumerate(modules):
        mv = _module_vec(sig_counts[m], idf)
        for h, w in mv.items():
            H_anchor[r, col_idx[h]] = w
        norm = np.linalg.norm(H_anchor[r])
        if norm:
            H_anchor[r] /= norm

    W_denovo, H_denovo = _semisupervised_nmf(X, H_anchor, k, iters, seed)

    factors: list[dict[str, Any]] = []
    for j in range(k):
        top_ph_idx = np.argsort(H_denovo[j])[::-1][:top_phenotypes]
        top_ph = [
            {"hpo_id": cols[i], "label": labels.get(cols[i], ""),
             "weight": round(float(H_denovo[j, i]), 4)}
            for i in top_ph_idx if H_denovo[j, i] > 0
        ]
        top_dz_idx = np.argsort(W_denovo[:, j])[::-1][:top_diseases]
        top_dz = [
            {"disease": diseases[i], "loading": round(float(W_denovo[i, j]), 4)}
            for i in top_dz_idx if W_denovo[i, j] > 0
        ]
        novel = [p for p in top_ph if p["hpo_id"] not in module_phenos]
        factors.append({
            "factor": j,
            "strength": round(float(W_denovo[:, j].sum()), 4),
            "novelty": round(len(novel) / len(top_ph), 3) if top_ph else 0.0,
            "top_phenotypes": top_ph,
            "top_diseases": top_dz,
        })
    # rank by novelty-weighted strength: how much it is used AND how uncovered it is
    factors.sort(key=lambda f: -(f["strength"] * f["novelty"]))

    return {
        "summary": {
            "n_diseases": len(diseases),
            "n_phenotype_columns": len(cols),
            "n_anchored_factors": len(modules),
            "n_denovo_factors": k,
            "iters": iters,
        },
        "factors": factors,
    }


def write_outputs(result: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "module_denovo_factors.json").write_text(json.dumps(result, indent=2) + "\n")
    with (out_dir / "module_denovo_factors.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["factor", "strength", "novelty", "top_phenotypes", "top_diseases"])
        for fac in result["factors"]:
            w.writerow([
                fac["factor"], fac["strength"], fac["novelty"],
                "; ".join(f"{p['label'] or p['hpo_id']}" for p in fac["top_phenotypes"]),
                "; ".join(d["disease"] for d in fac["top_diseases"]),
            ])


def _print_summary(result: dict[str, Any]) -> None:
    s = result["summary"]
    print("=" * 64)
    print("LEARNED DE-NOVO FACTORS (candidate new modules)")
    print("=" * 64)
    print(f"diseases x phenotypes        : {s['n_diseases']} x {s['n_phenotype_columns']}")
    print(f"anchored (fixed) factors     : {s['n_anchored_factors']}")
    print(f"de-novo (learned) factors    : {s['n_denovo_factors']}")
    print("\nde-novo factors, ranked by novelty x strength:")
    for fac in result["factors"][:12]:
        phenos = ", ".join(p["label"] or p["hpo_id"] for p in fac["top_phenotypes"][:5])
        dz = ", ".join(d["disease"] for d in fac["top_diseases"][:3])
        print(f"  [novelty {fac['novelty']:.2f}] {phenos}")
        print(f"      loaded by: {dz}")
    print("=" * 64)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--modules-dir", type=Path, default=Path("kb/modules"))
    ap.add_argument("--disorders-dir", type=Path, default=Path("kb/disorders"))
    ap.add_argument("--pathograph-dir", type=Path, default=Path("pathographs"))
    ap.add_argument("--out-dir", type=Path, default=Path("output/module_map"))
    ap.add_argument("-k", "--n-factors", type=int, default=20)
    ap.add_argument("--iters", type=int, default=150)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    result = build(args.modules_dir, args.disorders_dir, args.pathograph_dir,
                   k=args.n_factors, iters=args.iters, seed=args.seed)
    write_outputs(result, args.out_dir)
    _print_summary(result)
    print(f"\nwrote module_denovo_factors.json + .tsv -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
