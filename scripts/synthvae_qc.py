#!/usr/bin/env python3
"""Pathograph mechanistic-plausibility QC for synthetic (or real) patient cohorts.

Milestone 1 of justaddcoffee/synthetic_vae_generator#4: a *non-invasive* QC layer
that scores a cohort of phenopackets against the dismech pathograph **without
modifying VAE training**. It answers, per patient and per cohort:

* Which disease pathograph does the patient match (by MONDO id, else by causal
  gene)?
* Which of the patient's HPO terms are *represented* in that pathograph
  (mechanistically explainable) vs *unrepresented* / off-graph (no curated
  mechanism for this disease -- the plausibility red flag)?
* Which mechanistic *branches* (pathophysiology sub-pathways) do the represented
  terms light up -- i.e. is the patient a coherent sub-pathway or scattered
  off-graph noise?

Key distinction from HPO logical checks (issue #4): HPO ontology checks catch
*impossible term combinations*; this assesses *disease-mechanism plausibility* --
whether the phenotype set hangs together on the curated causal graph.

Input: a JSONL of phenopackets (the VAE's output, this repo's
``scripts/synthvae_sampler.py`` output, or real phenopacket-store cases) plus the
``disease_priors.json`` from ``dismech.export.synthvae_export`` (which already
carries each pathograph's phenotype set + per-phenotype branch).

This is exact-HPO-term matching; HPO ancestor/descendant expansion (via OAK, as
in ``scripts/pathograph_overlap.py``) is the natural refinement and is noted in
the report but not required for the milestone.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def _index_priors(priors: list[dict[str, Any]]) -> dict[str, Any]:
    """Build lookup tables: by MONDO id, by gene id, by gene symbol."""
    by_mondo: dict[str, dict] = {}
    by_gene: dict[str, list[dict]] = defaultdict(list)
    for p in priors:
        by_mondo[p["disease_id"]] = p
        for g in p.get("genes") or []:
            if g.get("id"):
                by_gene[g["id"].lower()].append(p)
            if g.get("label"):
                by_gene[g["label"].upper()].append(p)
    return {"by_mondo": by_mondo, "by_gene": by_gene}


def _patient_disease_ids(pkt: dict[str, Any]) -> list[str]:
    ids = []
    for d in pkt.get("diseases") or []:
        tid = ((d.get("term") or {}).get("id"))
        if tid:
            ids.append(tid)
    for interp in pkt.get("interpretations") or []:
        did = (((interp.get("diagnosis") or {}).get("disease") or {}).get("id"))
        if did:
            ids.append(did)
    return ids


def _patient_genes(pkt: dict[str, Any]) -> list[str]:
    out = []
    for interp in pkt.get("interpretations") or []:
        for gi in (interp.get("diagnosis") or {}).get("genomicInterpretations") or []:
            gene = gi.get("gene") or {}
            if gene.get("id"):
                out.append(gene["id"].lower())
            if gene.get("symbol"):
                out.append(gene["symbol"].upper())
    return out


def _patient_hpo(pkt: dict[str, Any]) -> list[str]:
    return [
        ((f.get("type") or {}).get("id"))
        for f in pkt.get("phenotypicFeatures") or []
        if (f.get("type") or {}).get("id", "").startswith("HP:")
    ]


def _match_prior(pkt: dict[str, Any], idx: dict[str, Any]) -> tuple[dict | None, str]:
    """Resolve the patient's disease prior. Returns (prior, match_basis)."""
    for did in _patient_disease_ids(pkt):
        if did in idx["by_mondo"]:
            return idx["by_mondo"][did], "mondo"
    candidates = {
        p["disease_id"]: p
        for key in _patient_genes(pkt)
        for p in idx["by_gene"].get(key, [])
    }
    if len(candidates) == 1:
        return next(iter(candidates.values())), "gene"
    if len(candidates) > 1:
        return None, "gene_ambiguous"
    return None, "unmatched"


def qc_patient(pkt: dict[str, Any], idx: dict[str, Any]) -> dict[str, Any]:
    prior, basis = _match_prior(pkt, idx)
    terms = _patient_hpo(pkt)
    rec: dict[str, Any] = {
        "id": pkt.get("id"),
        "match_basis": basis,
        "n_terms": len(terms),
    }
    if prior is None:
        rec.update(matched_disease=None, on_graph=[], off_graph=terms)
        return rec

    branch_of = {ph["hpo_id"]: ph.get("branch") for ph in prior["phenotypes"]}
    graph_terms = set(branch_of)
    on_graph = [t for t in terms if t in graph_terms]
    off_graph = [t for t in terms if t not in graph_terms]
    branches = Counter(branch_of[t] or "(unbranched)" for t in on_graph)
    rec.update(
        matched_disease=prior["disease_id"],
        matched_name=prior["disease_name"],
        on_graph=on_graph,
        off_graph=off_graph,
        coverage=round(len(on_graph) / len(terms), 3) if terms else 0.0,
        branches_activated=dict(branches),
        n_branches=len([b for b in branches if b != "(unbranched)"]),
    )
    return rec


def corpus_coverage(
    patients: list[dict[str, Any]], priors: list[dict[str, Any]], idx: dict[str, Any]
) -> dict[str, Any]:
    """Reproduce the issue's 'available data' coverage numbers for this cohort."""
    pg_terms = {ph["hpo_id"] for p in priors for ph in p["phenotypes"]}
    pg_genes = {g["id"].lower() for p in priors for g in (p.get("genes") or []) if g.get("id")}

    cohort_terms, cohort_genes, cohort_diseases, matched_diseases = set(), set(), set(), set()
    for pkt in patients:
        cohort_terms.update(_patient_hpo(pkt))
        for g in _patient_genes(pkt):
            if g.startswith("hgnc:"):
                cohort_genes.add(g)
        for did in _patient_disease_ids(pkt):
            cohort_diseases.add(did)
            if did in idx["by_mondo"]:
                matched_diseases.add(did)
    return {
        "pathograph_files": len(priors),
        "pathograph_unique_hpo_terms": len(pg_terms),
        "cohort_unique_hpo_terms": len(cohort_terms),
        "cohort_hpo_terms_in_pathograph": len(cohort_terms & pg_terms),
        "cohort_unique_genes": len(cohort_genes),
        "cohort_genes_in_pathograph": len(cohort_genes & pg_genes),
        "cohort_unique_diseases": len(cohort_diseases),
        "cohort_diseases_with_pathograph": len(matched_diseases),
    }


def run(patients: list[dict], priors: list[dict]) -> dict[str, Any]:
    idx = _index_priors(priors)
    per_patient = [qc_patient(p, idx) for p in patients]
    matched = [r for r in per_patient if r.get("matched_disease")]
    n = len(per_patient)

    off_graph_counter: Counter = Counter()
    for r in matched:
        off_graph_counter.update(r["off_graph"])
    cov = [r["coverage"] for r in matched]

    summary = {
        "n_patients": n,
        "n_matched": len(matched),
        "match_basis": dict(Counter(r["match_basis"] for r in per_patient)),
        "mean_coverage_matched": round(sum(cov) / len(cov), 3) if cov else None,
        "patients_fully_on_graph": sum(1 for r in matched if r["coverage"] == 1.0),
        "top_off_graph_terms": off_graph_counter.most_common(15),
        "corpus_coverage": corpus_coverage(patients, priors, idx),
    }
    return {"summary": summary, "patients": per_patient}


def _print_summary(report: dict[str, Any]) -> None:
    s = report["summary"]
    c = s["corpus_coverage"]
    print("=" * 64)
    print("PATHOGRAPH MECHANISTIC-PLAUSIBILITY QC")
    print("=" * 64)
    print(f"patients                  : {s['n_patients']}")
    print(f"matched to a pathograph   : {s['n_matched']}  {s['match_basis']}")
    print(f"mean on-graph coverage    : {s['mean_coverage_matched']}")
    print(f"fully on-graph patients   : {s['patients_fully_on_graph']}/{s['n_matched']}")
    print("\ncorpus coverage of this cohort:")
    print(f"  diseases with a pathograph : {c['cohort_diseases_with_pathograph']}/{c['cohort_unique_diseases']}")
    print(f"  causal genes in pathograph : {c['cohort_genes_in_pathograph']}/{c['cohort_unique_genes']}")
    print(f"  HPO terms in pathograph    : {c['cohort_hpo_terms_in_pathograph']}/{c['cohort_unique_hpo_terms']}")
    if s["top_off_graph_terms"]:
        print("\ntop off-graph (mechanistically unexplained) HPO terms:")
        for term, cnt in s["top_off_graph_terms"]:
            print(f"  {cnt:4d}  {term}")
    print("=" * 64)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("patients", type=Path, help="JSONL of phenopackets to QC")
    ap.add_argument(
        "--priors",
        type=Path,
        default=Path("output/synthvae/disease_priors.json"),
        help="disease_priors.json from dismech.export.synthvae_export",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("output/synthvae/qc_report.json"),
        help="machine-readable QC report",
    )
    args = ap.parse_args()

    patients = [json.loads(line) for line in args.patients.read_text().splitlines() if line.strip()]
    priors = json.loads(args.priors.read_text())
    report = run(patients, priors)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n")
    _print_summary(report)
    print(f"\nfull report -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
