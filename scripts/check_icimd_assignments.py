#!/usr/bin/env python3
"""Audit ICIMD (`classifications.icimd_category`) assignments against ICIMD.

For every `kb/**/*.yaml` entry that carries an `icimd_category` assignment,
this resolves the entry's causative gene(s) to their authoritative ICIMD
node in the live IEMbase browse tree
(https://www.iembase.com/api/v2/disorder/icimd_browse/) and checks that the
assigned dismech enum value encodes the same ICIMD branch, via the committed
crosswalk in ``conf/icimd_crosswalk.tsv``.

Verdicts per assignment:

* ``OK``           gene's ICIMD group (category.group) matches the value's
                   crosswalk prefix.
* ``CATEGORY_OK``  same ICIMD *category* but a different group/subgroup — an
                   adjacent-node nuance; advisory only.
* ``MISMATCH``     gene sits in a different ICIMD *category* than the value —
                   the hard signal. ``--strict`` exits non-zero on these.
* ``ALLOWLISTED``  a deliberate divergence recorded in ``ALLOWLIST`` (a
                   mechanistic/dual-nature facet that intentionally departs
                   from ICIMD's phenotype-driven placement).
* ``UNRESOLVED``   no causative gene resolvable in the live tree (e.g. mtDNA
                   deletion syndromes); advisory only.
* ``UNMAPPED``     assigned value absent from the crosswalk; advisory — add it.

Only the freely-citable ICIMD classification codes are used; no IEMbase
database content is redistributed. The live tree is fetched read-only; if it
is unreachable the check degrades to an advisory skip (exit 0) unless
``--require-network`` is given, mirroring the grouping-closure fallback.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CROSSWALK = ROOT / "conf" / "icimd_crosswalk.tsv"
ICIMD_URL = "https://www.iembase.com/api/v2/disorder/icimd_browse/"

# Deliberate divergences from ICIMD's authoritative placement. These are
# mechanistic or dual-nature facets a curator chose on purpose; each is
# documented in the entry's assignment `notes`.
ALLOWLIST = {
    # PGM1-CDG is a genuine glycogenosis *and* a CDG; ICIMD files it under
    # glycosylation, dismech additionally records the glycogen-metabolism facet.
    ("PGM1-Congenital_Disorder_of_Glycosylation", "glycogen_metabolism"),
    # PDE/ALDH7A1: primary lesion is lysine degradation; ICIMD files it
    # phenotypically under pyridoxine metabolism (also carried as a 2nd value).
    ("Pyridoxine-Dependent_Epilepsy", "lys_hyl_and_trp"),
    # MPS-Plus/VPS33A: HOPS/CORVET tethering facet, retained alongside the
    # ICIMD-canonical lysosome-related-organelle-biogenesis value.
    ("Mucopolysaccharidosis-Plus_Syndrome", "vesicular_trafficking"),
}


def load_crosswalk() -> dict[str, list[str]]:
    cw: dict[str, list[str]] = {}
    for line in CROSSWALK.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        cw[parts[0]] = parts[1].split("|")
    return cw


def fetch_tree(timeout: float) -> list | None:
    try:
        with urllib.request.urlopen(ICIMD_URL, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 - any failure => advisory skip
        print(f"WARNING: could not fetch live ICIMD tree ({exc}).", file=sys.stderr)
        return None


def gene_to_prefixes(tree: list) -> dict[str, set[str]]:
    g2p: dict[str, set[str]] = {}
    for coll in tree:
        for grp in coll.get("disorders_groups", []):
            for sub in grp.get("subgroups", []):
                for dis in sub.get("disorders", []):
                    gs = dis.get("gene_sym")
                    num = dis.get("icimd_nosology_disorder_num")
                    if gs and num:
                        g2p.setdefault(gs.upper(), set()).add(
                            ".".join(num.split(".")[:2])
                        )
    return g2p


def genes_of(doc: dict) -> set[str]:
    genes: set[str] = set()
    for gsec in doc.get("genetic") or []:
        term = (gsec.get("gene_term") or {}).get("term") or {}
        if term.get("label"):
            genes.add(str(term["label"]).upper())
    for st in doc.get("has_subtypes") or []:
        for g in st.get("genes") or []:
            term = g.get("term") or {}
            if term.get("label"):
                genes.add(str(term["label"]).upper())
    for pp in doc.get("pathophysiology") or []:
        for g in pp.get("genes") or []:
            term = g.get("term") or {}
            if term.get("label"):
                genes.add(str(term["label"]).upper())
    return genes


def category(prefix: str) -> str:
    return prefix.split(".")[0]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="exit 1 on any MISMATCH")
    ap.add_argument("--require-network", action="store_true",
                    help="fail if the live ICIMD tree cannot be fetched")
    ap.add_argument("--timeout", type=float, default=30.0)
    ap.add_argument("--kb", default=str(ROOT / "kb"))
    args = ap.parse_args()

    cw = load_crosswalk()
    tree = fetch_tree(args.timeout)
    if tree is None:
        if args.require_network:
            print("ERROR: --require-network set and tree unavailable.", file=sys.stderr)
            return 2
        print("Skipping ICIMD assignment check (offline). Advisory pass.")
        return 0
    g2p = gene_to_prefixes(tree)

    counts = {k: 0 for k in
              ("OK", "CATEGORY_OK", "MISMATCH", "ALLOWLISTED", "UNRESOLVED", "UNMAPPED")}
    mismatches, advisories = [], []

    for path in sorted(Path(args.kb).rglob("*.yaml")):
        text = path.read_text()
        if "icimd_category" not in text:  # fast prefilter before YAML parse
            continue
        try:
            doc = yaml.safe_load(text)
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(doc, dict):
            continue
        ic = (doc.get("classifications") or {}).get("icimd_category")
        if not ic:
            continue
        stem = path.stem
        gene_prefixes: set[str] = set()
        for g in genes_of(doc):
            gene_prefixes |= g2p.get(g, set())

        for a in ic:
            val = a.get("classification_value")
            if (stem, val) in ALLOWLIST:
                counts["ALLOWLISTED"] += 1
                continue
            expected = cw.get(val)
            if expected is None:
                counts["UNMAPPED"] += 1
                advisories.append((stem, val, "UNMAPPED", "value not in crosswalk"))
                continue
            if not gene_prefixes:
                counts["UNRESOLVED"] += 1
                continue
            if gene_prefixes & set(expected):
                counts["OK"] += 1
            elif {category(p) for p in gene_prefixes} & {category(p) for p in expected}:
                counts["CATEGORY_OK"] += 1
                advisories.append((stem, val, "CATEGORY_OK",
                                   f"gene@{sorted(gene_prefixes)} vs value@{expected}"))
            else:
                counts["MISMATCH"] += 1
                mismatches.append((stem, val, "MISMATCH",
                                   f"gene@{sorted(gene_prefixes)} vs value@{expected}"))

    for stem, val, verdict, detail in mismatches + advisories:
        print(f"{verdict:12} {stem:52.52} {val:34.34} {detail}")

    total = sum(counts.values())
    print("\n=== ICIMD assignment audit ===")
    print(f"assignments checked: {total}")
    for k, v in counts.items():
        print(f"  {k}: {v}")

    if args.strict and counts["MISMATCH"]:
        print(f"\nFAIL: {counts['MISMATCH']} cross-category mismatch(es).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
