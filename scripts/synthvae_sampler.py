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
  This preserves each phenotype's marginal (P(u<p)=p) while inducing
  positive *within-branch* co-occurrence: when a branch is "active" its
  higher-frequency phenotypes co-appear, and rarer ones only in more severe
  draws. That curated co-occurrence is precisely the structure the VAE has to
  estimate from data. Phenotypes with no branch fall back to independent draws.

Before the phenotypes, each patient is given **one causal gene** (weighted by
curated ``case_fractions`` where every candidate has one, uniformly otherwise)
and, when the entry declares subtypes, **one subtype** (the gene's own subtype
if it has one, otherwise drawn uniformly -- dismech records no subtype
frequencies). Phenotypes scoped to another subtype are dropped, so a patient
never carries the features of mutually exclusive subtypes. The marginals above
are therefore marginals *within the drawn subtype*; unscoped phenotypes keep
their curated marginal exactly.

``--min-features`` defaults to 0. Any higher value rejects and redraws sparse
patients, which conditions every kept patient on having at least that many
features and pushes the marginals up -- most for diseases whose phenotypes are
all low-frequency. Use it only when a downstream consumer cannot accept an
empty patient, and know that the marginals are then no longer the curated ones.

Output is JSONL (one phenopacket-style object per line) carrying HPO features,
the causal gene, the MONDO disease, and provenance marking the cases as
dismech-pathograph-synthetic.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from pathlib import Path
from typing import Any

DEFAULT_PROB = 0.5  # used for phenotypes whose curated frequency is unknown


def _present(prob: float | None, draw: float) -> bool:
    p = DEFAULT_PROB if prob is None else prob
    return draw < p


def sample_gene_and_subtype(
    prior: dict[str, Any], rng: random.Random
) -> tuple[dict[str, Any] | None, str | None]:
    """Draw one causal gene and, if the entry has subtypes, one subtype."""
    genes = prior.get("genes") or []
    subtypes = prior.get("subtypes") or []
    gene = None
    if genes:
        weights = [g.get("case_fraction") for g in genes]
        if all(isinstance(w, (int, float)) and w > 0 for w in weights):
            gene = rng.choices(genes, weights=weights, k=1)[0]
        else:
            gene = rng.choice(genes)
    subtype = (gene or {}).get("subtype")
    if subtype is None and subtypes:
        subtype = rng.choice(subtypes)
    return gene, subtype


def sample_phenotypes(
    prior: dict[str, Any],
    rng: random.Random,
    mode: str,
    subtype: str | None = None,
) -> list[dict[str, str]]:
    """Return the HPO features for one synthetic patient of this disease.

    Phenotypes scoped to a subtype other than ``subtype`` are never drawn.
    """
    pool = [
        phen
        for phen in prior["phenotypes"]
        if phen.get("subtype") is None or phen.get("subtype") == subtype
    ]
    if mode == "branch":
        branch_draw: dict[Any, float] = {}
        feats = []
        for phen in pool:
            b = phen.get("branch")
            if b is None:
                draw = rng.random()  # unbranched -> independent
            else:
                draw = branch_draw.setdefault(b, rng.random())
            if _present(phen.get("probability"), draw):
                feats.append(phen)
        return feats
    # marginal
    return [phen for phen in pool if _present(phen.get("probability"), rng.random())]


def _hgnc_curie(gene_id: str) -> str:
    """Phenopacket form of the repo's lowercase ``hgnc:`` CURIE."""
    prefix, _, local = gene_id.partition(":")
    return f"HGNC:{local}" if prefix.lower() == "hgnc" and local else gene_id


def _patient_stem(prior: dict[str, Any]) -> str:
    """Per-entry id stem; entries sharing a MONDO id must not share patient ids."""
    slug = re.sub(r"[^A-Za-z0-9]+", "_", prior.get("dismech_name") or "").strip("_")
    base = prior["disease_id"].replace(":", "_")
    return f"{base}__{slug}" if slug else base


def to_phenopacket(
    prior: dict[str, Any],
    feats: list[dict[str, str]],
    index: int,
    gene: dict[str, Any] | None = None,
    subtype: str | None = None,
) -> dict[str, Any]:
    """Assemble a phenopacket-v2-style dict for one synthetic patient."""
    pid = f"{_patient_stem(prior)}-synth-{index:04d}"
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
    if subtype:
        pkt["metaData"]["externalReferences"].append(
            {"id": subtype, "description": "dismech subtype"}
        )
    if gene:
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
                            "subjectOrBiosampleId": pid,
                            "interpretationStatus": "CAUSATIVE",
                            "gene": {
                                "valueId": _hgnc_curie(gene["id"]),
                                "symbol": gene["label"],
                            },
                        }
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
            gene, subtype = sample_gene_and_subtype(prior, rng)
            feats = sample_phenotypes(prior, rng, mode, subtype)
            if len(feats) < min_features:
                continue
            out.append(to_phenopacket(prior, feats, made, gene, subtype))
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
        default=0,
        help=(
            "discard/resample patients with fewer than this many HPO features. "
            "Any value above 0 conditions the cohort and inflates the marginals"
        ),
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("output/synthvae/synthetic_patients.jsonl"),
        help="JSONL output (one phenopacket per line)",
    )
    args = ap.parse_args()

    if args.min_features > 0:
        print(
            f"note: --min-features {args.min_features} conditions every patient on "
            "having that many features; marginals are no longer the curated ones",
            file=sys.stderr,
        )
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
