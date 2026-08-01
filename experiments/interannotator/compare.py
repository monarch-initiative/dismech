"""Compare two independently curated versions of the same dismech Disease entry.

Emits the inter-annotator agreement metrics reported in FINDINGS.md. Kept in the
repo so the numbers are reproducible rather than asserted.

Shared across all studies under experiments/interannotator/; the snapshots and
report for each individual comparison live in a per-disease subdirectory.

Usage:
    uv run python experiments/interannotator/compare.py \
        experiments/interannotator/FG_Syndrome_1/FG_Syndrome_1.curator-A.merged-pr7254.yaml \
        experiments/interannotator/FG_Syndrome_1/FG_Syndrome_1.curator-B.independent.yaml \
        | tee experiments/interannotator/FG_Syndrome_1/metrics.txt

Subsumption-aware phenotype matching shells out to OAK (`runoak ... ancestors`)
against `sqlite:obo:hp`; pass --no-ontology to skip that and report strict
term-identity agreement only.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

import yaml

SECTIONS = [
    "phenotypes",
    "pathophysiology",
    "treatments",
    "genetic",
    "variants",
    "diagnosis",
    "differential_diagnoses",
    "discussions",
    "prevalence",
    "inheritance",
    "progression",
    "references",
    "clinical_trials",
    "datasets",
    "biochemical",
    "histopathology",
]


def load(path: str) -> dict:
    with open(path) as handle:
        return yaml.safe_load(handle)


def phenotype_map(entry: dict) -> dict[str, tuple[str | None, str | None, str | None]]:
    """HPO term id -> (entry name, frequency band, ontology label)."""
    out: dict[str, tuple[str | None, str | None, str | None]] = {}
    for phenotype in entry.get("phenotypes") or []:
        descriptor = phenotype.get("phenotype_term") or {}
        term = descriptor.get("term") or {}
        term_id = term.get("id")
        if term_id:
            out[term_id] = (
                phenotype.get("name"),
                phenotype.get("frequency"),
                term.get("label"),
            )
    return out


def treatment_terms(entry: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    for treatment in entry.get("treatments") or []:
        term = (treatment.get("treatment_term") or {}).get("term") or {}
        if term.get("id"):
            out[term["id"]] = treatment.get("name") or ""
    return out


def pmids(entry: dict) -> set[str]:
    return set(re.findall(r"PMID:\d+", json.dumps(entry)))


def edge_count(entry: dict) -> int:
    return sum(len(node.get("downstream") or []) for node in entry.get("pathophysiology") or [])


def snippet_count(entry: dict) -> int:
    return json.dumps(entry).count('"snippet"')


_ancestor_cache: dict[str, set[str]] = {}
_label_cache: dict[str, str] = {}


def ancestors(term_id: str) -> set[str]:
    """Ancestor closure from OAK. Output is TSV: `id<TAB>label`."""
    if term_id in _ancestor_cache:
        return _ancestor_cache[term_id]
    proc = subprocess.run(
        ["uv", "run", "runoak", "-i", "sqlite:obo:hp", "ancestors", term_id],
        capture_output=True,
        text=True,
        check=False,
    )
    found: set[str] = set()
    for line in proc.stdout.splitlines():
        parts = line.split("\t")
        if parts[0].startswith("HP:"):
            found.add(parts[0])
            if len(parts) > 1:
                _label_cache.setdefault(parts[0], parts[1])
    _ancestor_cache[term_id] = found
    return found


def jaccard(left: set, right: set) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_a")
    parser.add_argument("file_b")
    parser.add_argument("--label-a", default="A")
    parser.add_argument("--label-b", default="B")
    parser.add_argument("--no-ontology", action="store_true")
    args = parser.parse_args()

    a, b = load(args.file_a), load(args.file_b)
    la, lb = args.label_a, args.label_b

    print("=" * 72)
    print("SECTION CARDINALITY")
    print("=" * 72)
    print(f"  {'section':26} {la:>10} {lb:>10}")
    for section in SECTIONS:
        va, vb = a.get(section), b.get(section)
        if isinstance(va, list) or isinstance(vb, list):
            print(
                f"  {section:26} {len(va) if isinstance(va, list) else 0:>10} "
                f"{len(vb) if isinstance(vb, list) else 0:>10}"
            )
    print(f"  {'causal edges':26} {edge_count(a):>10} {edge_count(b):>10}")
    print(f"  {'evidence snippets':26} {snippet_count(a):>10} {snippet_count(b):>10}")

    pa, pb = phenotype_map(a), phenotype_map(b)
    sa, sb = set(pa), set(pb)
    shared = sa & sb

    print()
    print("=" * 72)
    print("PHENOTYPE TERM AGREEMENT")
    print("=" * 72)
    print(f"  {la} terms: {len(sa)}   {lb} terms: {len(sb)}   shared: {len(shared)}")
    print(f"  strict Jaccard : {jaccard(sa, sb):.3f}")
    print(f"  Dice / F1      : {2 * len(shared) / (len(sa) + len(sb)):.3f}")

    print()
    print("=" * 72)
    print("FREQUENCY BAND AGREEMENT (shared terms)")
    print("=" * 72)
    agree = 0
    both_banded = 0
    for term_id in sorted(shared):
        fa, fb = pa[term_id][1], pb[term_id][1]
        if fa == fb:
            agree += 1
        else:
            print(f"  DIFF {term_id:12} {str(pa[term_id][2])[:34]:34} {la}={fa!s:14} {lb}={fb}")
        if fa and fb:
            both_banded += 1
    if shared:
        print(f"\n  exact match (incl. both-unbanded): {agree}/{len(shared)} = {agree / len(shared):.3f}")
    print(f"  both assigned a band: {both_banded}")
    print(f"  {la} banded {sum(1 for t in pa if pa[t][1])}/{len(pa)}   "
          f"{lb} banded {sum(1 for t in pb if pb[t][1])}/{len(pb)}")

    if not args.no_ontology:
        only_a, only_b = sorted(sa - sb), sorted(sb - sa)
        pairs = []
        for x in only_a:
            for y in only_b:
                if y in ancestors(x) or x in ancestors(y):
                    pairs.append((x, y))
        matched_a = {x for x, _ in pairs}
        matched_b = {y for _, y in pairs}

        print()
        print("=" * 72)
        print("SUBSUMPTION-AWARE CONCEPT AGREEMENT")
        print("=" * 72)
        print("  same concept, different granularity:")
        for x, y in pairs:
            broader = la if x in ancestors(y) else lb
            print(
                f"    {la}:{x} {_label_cache.get(x, '?')[:30]:30} <-> "
                f"{lb}:{y} {_label_cache.get(y, '?')[:30]:30} ({broader} broader)"
            )
        ca = (len(shared) + len(matched_a)) / len(sa) if sa else 1.0
        cb = (len(shared) + len(matched_b)) / len(sb) if sb else 1.0
        print(f"\n  concept coverage {la}: {len(shared) + len(matched_a)}/{len(sa)} = {ca:.3f}")
        print(f"  concept coverage {lb}: {len(shared) + len(matched_b)}/{len(sb)} = {cb:.3f}")
        print(f"\n  true {la}-only (no counterpart):")
        for t in only_a:
            if t not in matched_a:
                print(f"    {t:13} {pa[t][2]}")
        print(f"  true {lb}-only (no counterpart):")
        for t in only_b:
            if t not in matched_b:
                print(f"    {t:13} {pb[t][2]}")

    ta, tb = treatment_terms(a), treatment_terms(b)
    print()
    print("=" * 72)
    print("TREATMENT TERM BINDING")
    print("=" * 72)
    print(f"  {la}: {len(ta)}   {lb}: {len(tb)}   shared term ids: {len(set(ta) & set(tb))}")
    print(f"  Jaccard: {jaccard(set(ta), set(tb)):.3f}")
    for term_id in sorted(set(ta) & set(tb)):
        print(f"    both: {term_id:16} {ta[term_id][:34]:34} | {tb[term_id]}")
    for term_id in sorted(set(ta) - set(tb)):
        print(f"    {la} only: {term_id:16} {ta[term_id]}")
    for term_id in sorted(set(tb) - set(ta)):
        print(f"    {lb} only: {term_id:16} {tb[term_id]}")

    ra, rb = pmids(a), pmids(b)
    print()
    print("=" * 72)
    print("REFERENCE SET")
    print("=" * 72)
    print(f"  {la}: {len(ra)}   {lb}: {len(rb)}   shared: {len(ra & rb)}   Jaccard: {jaccard(ra, rb):.3f}")
    print(f"  shared  : {' '.join(sorted(ra & rb))}")
    print(f"  {la} only : {' '.join(sorted(ra - rb))}")
    print(f"  {lb} only : {' '.join(sorted(rb - ra))}")

    print()
    print("=" * 72)
    print("PATHOPHYSIOLOGY GRAPH")
    print("=" * 72)
    for label, entry in ((la, a), (lb, b)):
        print(f"  {label}:")
        for node in entry.get("pathophysiology") or []:
            print(
                f"    [{node.get('biological_scale')!s:9}] "
                f"{node.get('name')} -> {len(node.get('downstream') or [])} edge(s)"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
