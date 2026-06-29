#!/usr/bin/env python3
"""Curated knowledge-based synthetic-patient sampler from dismech pathograph priors.

Consumes the per-disease priors emitted by ``dismech.export.synthvae_export`` and
generates synthetic phenopacket-v2-style patients. This is the white-box
counterpart to the learned VAE in justaddcoffee/synthetic_vae_generator: instead
of learning HPO co-occurrence from sparse real cases, it samples from the
*curated* frequencies and causal-branch structure of the pathograph. It therefore
works for rare / cold-start diseases that have no (or too few) real phenopackets
for a VAE to train on, and it can serve as a structured prior or a plausibility
baseline alongside the VAE.

Two sampling modes:

* ``marginal`` -- each phenotype drawn independently, present iff
  ``u < probability`` with ``u ~ Uniform(0,1)``. Equivalent to the existing
  marginal baseline in the VAE repo, but with curated probabilities.

* ``branch`` (default) -- one shared draw ``u_branch ~ Uniform(0,1)`` per
  mechanistic branch; a phenotype is present iff ``u_branch < probability``.
  This preserves each phenotype's marginal exactly (P(u<p)=p) while inducing
  positive *within-branch* co-occurrence: when a branch is "active" its
  higher-frequency phenotypes co-appear, and rarer ones only in more severe
  draws. That curated co-occurrence is precisely the structure the VAE has to
  estimate from data. Phenotypes with no branch fall back to independent draws.

Output is JSONL (one phenopacket-style object per line) or a directory of JSON
files, carrying HPO features, the causal gene(s), the OMIM/MONDO disease, and
provenance marking the cases as dismech-pathograph-synthetic.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any

DEFAULT_PROB = 0.5  # used for phenotypes whose curated frequency is unknown


def _present(prob: float | None, draw: float) -> bool:
    p = DEFAULT_PROB if prob is None else prob
    return draw < p


def sample_phenotypes(
    prior: dict[str, Any], rng: random.Random, mode: str
) -> list[dict[str, str]]:
    """Return the HPO features for one synthetic patient of this disease."""
    if mode == "branch":
        branch_draw: dict[Any, float] = {}
        feats = []
        for phen in prior["phenotypes"]:
            b = phen.get("branch")
            if b is None:
                draw = rng.random()  # unbranched -> independent
            else:
                draw = branch_draw.setdefault(b, rng.random())
            if _present(phen.get("probability"), draw):
                feats.append(phen)
        return feats
    # marginal
    return [
        phen
        for phen in prior["phenotypes"]
        if _present(phen.get("probability"), rng.random())
    ]


def to_phenopacket(
    prior: dict[str, Any], feats: list[dict[str, str]], index: int
) -> dict[str, Any]:
    """Assemble a phenopacket-v2-style dict for one synthetic patient."""
    pid = f"{prior['disease_id'].replace(':', '_')}-synth-{index:04d}"
    pkt: dict[str, Any] = {
        "id": pid,
        "subject": {"id": pid},
        "phenotypicFeatures": [
            {"type": {"id": f["hpo_id"], "label": f["label"]}} for f in feats
        ],
        "diseases": [
            {"term": {"id": prior["disease_id"], "label": prior["disease_name"]}}
        ],
        "metaData": {
            "createdBy": "dismech-pathograph-synthvae",
            "resources": [],
            "phenopacketSchemaVersion": "2.0",
            "externalReferences": [
                {"id": p, "description": "dismech pathograph"}
                for p in [prior.get("pathograph")] if p
            ],
        },
    }
    genes = prior.get("genes") or []
    if genes:
        pkt["interpretations"] = [
            {
                "id": f"{pid}-interpretation",
                "progressStatus": "SOLVED",
                "diagnosis": {
                    "disease": {
                        "id": prior["disease_id"],
                        "label": prior["disease_name"],
                    },
                    "genomicInterpretations": [
                        {
                            "subjectOrInterpretationId": pid,
                            "gene": {"id": g["id"], "symbol": g["label"]},
                        }
                        for g in genes
                    ],
                },
            }
        ]
    return pkt


def generate(
    priors: list[dict[str, Any]],
    n_per_disease: int,
    mode: str,
    seed: int,
    disease_filter: set[str] | None,
    min_features: int,
) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    out = []
    for prior in priors:
        if disease_filter and prior["disease_id"] not in disease_filter:
            continue
        made = 0
        attempts = 0
        # resample empty/too-sparse patients up to a cap so a low-frequency
        # disease still yields the requested cohort size
        while made < n_per_disease and attempts < n_per_disease * 20:
            attempts += 1
            feats = sample_phenotypes(prior, rng, mode)
            if len(feats) < min_features:
                continue
            out.append(to_phenopacket(prior, feats, made))
            made += 1
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--priors",
        type=Path,
        default=Path("output/synthvae/disease_priors.json"),
        help="disease_priors.json from dismech.export.synthvae_export",
    )
    ap.add_argument("-n", "--n-per-disease", type=int, default=5)
    ap.add_argument(
        "--mode", choices=["branch", "marginal"], default="branch"
    )
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument(
        "--disease",
        action="append",
        help="restrict to these MONDO id(s); repeatable",
    )
    ap.add_argument(
        "--min-features",
        type=int,
        default=1,
        help="discard/resample patients with fewer than this many HPO features",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("output/synthvae/synthetic_patients.jsonl"),
        help="JSONL output (one phenopacket per line)",
    )
    args = ap.parse_args()

    priors = json.loads(args.priors.read_text())
    patients = generate(
        priors,
        args.n_per_disease,
        args.mode,
        args.seed,
        set(args.disease) if args.disease else None,
        args.min_features,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w") as f:
        for pkt in patients:
            f.write(json.dumps(pkt) + "\n")
    print(f"wrote {len(patients)} synthetic patients ({args.mode} mode) -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
