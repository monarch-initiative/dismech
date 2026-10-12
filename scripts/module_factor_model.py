#!/usr/bin/env python3
"""Anchored module-factor model: mechanism modules as latent factors over diseases.

The keystone the module-map + phenotype-anchor work was scaffolding for. It treats
each curated mechanism module as a **latent factor** and scores every disease's
soft loading on every module from the disease's own phenotype profile, anchored to
the curated module->phenotype signatures (``module_phenotype_anchors``). It is the
inference half of the mechanism-as-hidden-variable model (f-scLVM / expiMap family,
with annotated factors): fixed, curated anchors now; learned de-novo factors for
residual structure are the noted next step.

Two things come out, and both are honest about circularity:

1. **Recovery of curated conformance.** For each disease that declares
   ``conforms_to`` module m, how highly does m rank among its module loadings? This
   is scored **leave-one-out** -- the module signature is recomputed with that
   disease's own phenotype contribution removed -- so a conformer cannot score
   highly on a module just because it helped build that module's signature. MRR /
   recall@k vs a random baseline say whether the soft loadings track the curated
   graph.

2. **Candidate conformances (the actionable output).** A disease whose phenotype
   profile matches a module it does *not* declare is a curation lead: "this disease
   looks like it conforms to <module>, but the entry doesn't say so." By
   construction a non-conformer never contributed to the module signature, so this
   half is not circular. This is the phenotype-signature complement to the
   node-embedding ``conforms_to_suggestions`` idea.

Scoring is idf-weighted cosine between a disease's phenotype vector (frequency as
weight) and a module's phenotype signature (support-damped, specificity-weighted),
the same specificity intuition as ``scripts/pathograph_overlap.py``.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

from dismech.export import module_map, module_phenotype_anchors, synthvae_export

MIN_SHARED = 2  # a disease must share >=2 phenotypes with a module to be scored


def _disease_vectors(disorders_dir: Path) -> dict[str, dict[str, float]]:
    """disease name -> {hpo_id: frequency-probability} over its whole profile."""
    out: dict[str, dict[str, float]] = {}
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
        if vec:
            out[rec["dismech_name"]] = vec
    return out


def _module_signatures(
    anchors: dict[str, list[dict[str, Any]]],
) -> tuple[dict[str, dict[str, int]], dict[str, dict[str, set[str]]]]:
    """module -> {hpo: n_diseases} and module -> {hpo: set(diseases)} from anchors."""
    counts: dict[str, dict[str, int]] = {}
    diseases: dict[str, dict[str, set[str]]] = {}
    for mod, rows in anchors.items():
        counts[mod] = {r["hpo_id"]: r["n_diseases"] for r in rows}
        diseases[mod] = {r["hpo_id"]: set(r["diseases"]) for r in rows}
    return counts, diseases


def _idf(counts: dict[str, dict[str, int]]) -> dict[str, float]:
    """Specificity weight per phenotype: smoothed idf over modules carrying it.

    Smoothed (``log((1+n)/(1+df)) + 1``, as in sklearn's TfidfTransformer) so a
    phenotype carried by *every* module floors at 1 rather than zeroing out — which
    also keeps the weighting well-defined when there is only one module.
    """
    n_mod = len(counts) or 1
    df: dict[str, int] = defaultdict(int)
    for sig in counts.values():
        for hpo in sig:
            df[hpo] += 1
    return {hpo: math.log((1 + n_mod) / (1 + d)) + 1.0 for hpo, d in df.items()}


def _module_vec(
    sig_counts: dict[str, int], idf: dict[str, float], drop: str | None = None,
    drop_diseases: dict[str, set[str]] | None = None,
) -> dict[str, float]:
    """Support-damped, idf-weighted module vector; optionally leave one disease out."""
    vec: dict[str, float] = {}
    for hpo, count in sig_counts.items():
        c = count
        if drop is not None and drop_diseases is not None and drop in drop_diseases.get(hpo, ()):
            c -= 1
        if c > 0:
            vec[hpo] = math.sqrt(c) * idf.get(hpo, 0.0)
    return vec


def _cosine(a: dict[str, float], b: dict[str, float]) -> tuple[float, int]:
    """Cosine over shared keys; also return the number of shared keys."""
    small, large = (a, b) if len(a) <= len(b) else (b, a)
    dot = 0.0
    shared = 0
    for k, v in small.items():
        if k in large:
            dot += v * large[k]
            shared += 1
    if dot == 0.0:
        return 0.0, shared
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return (dot / (na * nb) if na and nb else 0.0), shared


def build(
    modules_dir: Path, disorders_dir: Path, pathograph_dir: Path
) -> dict[str, Any]:
    anchors = module_phenotype_anchors.build(modules_dir, disorders_dir, pathograph_dir)["modules"]
    declared = module_map.build(modules_dir, disorders_dir)["disease_to_modules"]
    sig_counts, sig_diseases = _module_signatures(anchors)
    idf = _idf(sig_counts)
    disease_vecs = _disease_vectors(disorders_dir)

    # idf-weight each disease vector once
    weighted_disease: dict[str, dict[str, float]] = {}
    for d, vec in disease_vecs.items():
        weighted_disease[d] = {hpo: p * idf.get(hpo, 0.0) for hpo, p in vec.items()}

    modules = [m for m in sig_counts if sig_counts[m]]
    base_vec = {m: _module_vec(sig_counts[m], idf) for m in modules}

    loadings: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []
    # recovery eval accumulators
    ranks: list[int] = []
    rr: list[float] = []
    n_eval = 0

    for d, wvec in weighted_disease.items():
        decl = set(declared.get(d, []))
        scored: list[tuple[float, str, int]] = []
        for m in modules:
            if m in decl:
                mv = _module_vec(sig_counts[m], idf, drop=d, drop_diseases=sig_diseases[m])
            else:
                mv = base_vec[m]
            s, shared = _cosine(wvec, mv)
            if s > 0 and shared >= MIN_SHARED:
                scored.append((s, m, shared))
        scored.sort(reverse=True)
        rank_of = {m: i for i, (_, m, _) in enumerate(scored, start=1)}

        # record top loadings for this disease
        for s, m, shared in scored[:10]:
            loadings.append(
                {"disease": d, "module": m, "score": round(s, 4),
                 "shared": shared, "declared": m in decl}
            )
        # candidates: high-scoring, not declared
        for s, m, shared in scored:
            if m not in decl:
                candidates.append(
                    {"disease": d, "module": m, "score": round(s, 4), "shared": shared}
                )
        # recovery eval for declared modules that are scoreable
        scoreable_decl = [m for m in decl if m in rank_of]
        if scoreable_decl:
            best = min(rank_of[m] for m in scoreable_decl)
            ranks.append(best)
            rr.append(1.0 / best)
            n_eval += 1

    candidates.sort(key=lambda r: -r["score"])
    n_mod = len(modules)
    summary = {
        "n_modules": n_mod,
        "n_diseases_scored": len(weighted_disease),
        "n_diseases_in_recovery_eval": n_eval,
        "recovery": {
            "mrr": round(sum(rr) / len(rr), 4) if rr else None,
            "recall_at_1": round(sum(1 for r in ranks if r <= 1) / len(ranks), 4) if ranks else None,
            "recall_at_3": round(sum(1 for r in ranks if r <= 3) / len(ranks), 4) if ranks else None,
            "recall_at_5": round(sum(1 for r in ranks if r <= 5) / len(ranks), 4) if ranks else None,
            "random_recall_at_5": round(5.0 / n_mod, 4) if n_mod else None,
        },
        "n_candidate_conformances": len(candidates),
    }
    return {
        "summary": summary,
        "loadings": loadings,
        "candidates": candidates,
    }


def write_outputs(result: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "module_factor_model.json").write_text(
        json.dumps({"summary": result["summary"]}, indent=2) + "\n"
    )
    with (out_dir / "module_factor_loadings.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease", "module", "score", "shared", "declared"])
        for r in result["loadings"]:
            w.writerow([r["disease"], r["module"], r["score"], r["shared"], r["declared"]])
    with (out_dir / "conformance_candidates.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease", "module", "score", "shared"])
        for r in result["candidates"]:
            w.writerow([r["disease"], r["module"], r["score"], r["shared"]])


def _print_summary(result: dict[str, Any]) -> None:
    s = result["summary"]
    rec = s["recovery"]
    print("=" * 64)
    print("ANCHORED MODULE-FACTOR MODEL")
    print("=" * 64)
    print(f"modules (factors)            : {s['n_modules']}")
    print(f"diseases scored              : {s['n_diseases_scored']}")
    print(f"diseases in recovery eval    : {s['n_diseases_in_recovery_eval']}")
    print("\nrecovery of curated conforms_to (leave-one-out):")
    print(f"  MRR                        : {rec['mrr']}")
    print(f"  recall@1 / @3 / @5         : {rec['recall_at_1']} / {rec['recall_at_3']} / {rec['recall_at_5']}")
    print(f"  random recall@5 (baseline) : {rec['random_recall_at_5']}")
    print(f"\ncandidate conformances       : {s['n_candidate_conformances']}")
    top = result["candidates"][:15]
    if top:
        print("\ntop candidate conformances (phenotype profile matches an undeclared module):")
        for r in top:
            print(f"  {r['score']:.3f}  {r['disease']}  ~  {r['module']}  (shared {r['shared']})")
    print("=" * 64)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--modules-dir", type=Path, default=Path("kb/modules"))
    ap.add_argument("--disorders-dir", type=Path, default=Path("kb/disorders"))
    ap.add_argument("--pathograph-dir", type=Path, default=Path("pathographs"))
    ap.add_argument("--out-dir", type=Path, default=Path("output/module_map"))
    args = ap.parse_args()
    result = build(args.modules_dir, args.disorders_dir, args.pathograph_dir)
    write_outputs(result, args.out_dir)
    _print_summary(result)
    print(f"\nwrote module_factor_model.json + 2 TSVs -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
