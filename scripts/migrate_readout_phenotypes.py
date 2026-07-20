#!/usr/bin/env python3
"""Migrate mis-wired causal edges targeting pure lab/investigation-readout
phenotypes into observational ``reports_on`` (``PhenotypeReadout``) links.

Background
----------
Many HP terms are *investigation results* rather than states of the organism —
tissue-leakage enzymes (transaminases, creatine kinase, LDH, aldolase, alkaline
phosphatase), acute-phase reactants (CRP), tumor markers (AFP, beta-hCG),
newborn-screening acylcarnitines, and the electroretinogram. They are legitimate
HP phenotypes and stay in ``phenotypes``, but functionally they are *readouts of*
an underlying mechanism, not causal participants in disease progression. Curators
frequently wired them as ``downstream``/``sequelae`` causal edges
(``mechanism -> Elevated transaminase``), which wrongly asserts the mechanism
*causes* the test result. The correct model (design-decisions.md §10) is a
``reports_on`` link on the phenotype: ``mechanism -.-> readout`` (dashed,
observational), mirroring ``Biochemical.readouts``.

Scope guard (correctness landmine)
----------------------------------
This migration flips **only pure readouts that are never themselves disease
drivers**. It deliberately does NOT touch causally-active analytes — ammonia
(causes encephalopathy), lactate (acidosis), vitamins (deficiency drives
neuropathy/retinopathy), cholesterol, hormones, ions, immunoglobulins — whose
``downstream`` edges are correct. The ``PURE`` allowlist below encodes that
boundary; a readout phenotype that carries its own ``sequelae`` (i.e. it
participates causally) is also skipped.

What it does, per matched edge
------------------------------
1. Removes the ``downstream``/``sequelae`` edge whose target is the readout
   phenotype (dropping ``causal_link_type``/``intermediate_mechanisms``).
2. Adds a ``reports_on`` entry on the readout phenotype: ``target`` = the former
   source node, ``relationship: READOUT_OF``, ``direction`` inferred from the HP
   label polarity (Elevated/Increased -> POSITIVE; Decreased/Reduced/Undetectable
   -> NEGATIVE; Abnormal -> omitted), ``endpoint_context: DIAGNOSTIC``, the edge's
   ``description`` as ``interpretation``, and the edge's ``evidence`` moved across
   verbatim.

Idempotent: phenotypes that already carry ``reports_on`` are skipped. Uses ruamel
round-trip to preserve file formatting.

Usage
-----
    uv run python scripts/migrate_readout_phenotypes.py            # migrate
    uv run python scripts/migrate_readout_phenotypes.py --dry-run  # report only

The authoritative readout HP set is computed from these OAK roots (all are
"circulating/blood concentration-or-activity" or visual-electrophysiology
groupings, so no clinical-symptom terms are swept in):

    HP:0032180  Abnormal circulating metabolite concentration
    HP:0034684  Abnormal enzyme concentration or activity
    HP:0010876  Abnormal circulating protein concentration
    HP:0003111  Abnormal blood ion concentration
    HP:0030453  Abnormal visual electrophysiology
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from oaklib import get_adapter
from ruamel.yaml import YAML

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIRS = ["kb/disorders", "kb/modules"]

READOUT_ROOTS = [
    "HP:0032180",  # Abnormal circulating metabolite concentration
    "HP:0034684",  # Abnormal enzyme concentration or activity
    "HP:0010876",  # Abnormal circulating protein concentration
    "HP:0003111",  # Abnormal blood ion concentration
    "HP:0030453",  # Abnormal visual electrophysiology (electroretinogram)
]

# Pure-readout markers: the value reports on a mechanism and is never itself a
# disease driver. Causally-active analytes (ammonia, lactate, vitamins,
# cholesterol, hormones, ions, immunoglobulins) are intentionally excluded.
PURE = re.compile(
    r"(transaminase|aminotransferase|\bALT\b|\bAST\b|creatine kinase|"
    r"lactate dehydrogenase|\bLDH\b|aldolase|alkaline phosphatase|amylase|lipase|"
    r"gamma-glutamyl|glutamyltransferase|troponin|natriuretic peptide|"
    r"C-reactive protein|sedimentation rate|procalcitonin|"
    r"alpha-fetoprotein|fetoprotein|chorionic gonadotropin|prostate-specific|"
    r"carcinoembryonic|\bCA-?125\b|\bCA ?19|tryptase|acylcarnitine|"
    r"electroretinogram|electrophysiolog)",
    re.I,
)


def readout_hp_ids() -> set[str]:
    """Descendants (+ the roots) of the readout groupings, via the OAK API."""
    adapter = get_adapter("sqlite:obo:hp")
    ids: set[str] = set(READOUT_ROOTS)
    for curie in adapter.descendants(READOUT_ROOTS, predicates=["rdfs:subClassOf"]):
        if str(curie).startswith("HP:"):
            ids.add(str(curie))
    return ids


def infer_direction(label: str) -> str | None:
    low = label.lower()
    if re.match(r"^(elevated|increased|high|excess)", low):
        return "POSITIVE"
    if re.match(r"^(decreased|reduced|low|undetectable|deficien|absent)", low):
        return "NEGATIVE"
    return None


def migrate_file(path: Path, readout_ids: set[str], dry_run: bool) -> int:
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=2, offset=0)

    with open(path) as fh:
        doc = yaml.load(fh)
    if not doc or "phenotypes" not in doc:
        return 0

    # Eligible readout phenotypes: HP-verified, pure, no existing reports_on, and
    # not causally participating (no sequelae of their own).
    targets: dict[str, tuple[dict, str]] = {}
    for pheno in doc.get("phenotypes", []) or []:
        if not isinstance(pheno, dict):
            continue
        name = pheno.get("name")
        term = (pheno.get("phenotype_term") or {}).get("term") or {}
        hid = term.get("id")
        label = term.get("label") or name or ""
        if (
            name
            and hid in readout_ids
            and (PURE.search(label) or PURE.search(name))
            and not pheno.get("reports_on")
            and not pheno.get("sequelae")
        ):
            targets[name] = (pheno, label)
    if not targets:
        return 0

    changed = 0
    for section in ("pathophysiology", "phenotypes"):
        for item in doc.get(section, []) or []:
            if not isinstance(item, dict):
                continue
            source = item.get("name")
            for edge_key in ("downstream", "sequelae"):
                edges = item.get(edge_key)
                if not edges:
                    continue
                keep = []
                for edge in edges:
                    tgt = edge.get("target") if isinstance(edge, dict) else None
                    if tgt in targets:
                        pheno, label = targets[tgt]
                        entry = {"target": source, "relationship": "READOUT_OF"}
                        direction = infer_direction(label)
                        if direction:
                            entry["direction"] = direction
                        entry["endpoint_context"] = "DIAGNOSTIC"
                        if edge.get("description"):
                            entry["interpretation"] = edge["description"]
                        if edge.get("evidence"):
                            entry["evidence"] = edge["evidence"]
                        pheno.setdefault("reports_on", []).append(entry)
                        changed += 1
                    else:
                        keep.append(edge)
                if len(keep) != len(edges):
                    if keep:
                        item[edge_key] = keep
                    else:
                        del item[edge_key]

    if changed and not dry_run:
        with open(path, "w") as fh:
            yaml.dump(doc, fh)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report without writing")
    args = parser.parse_args()

    readout_ids = readout_hp_ids()
    files = []
    for d in KB_DIRS:
        files.extend(sorted((REPO_ROOT / d).glob("*.yaml")))
    files = [f for f in files if not f.name.endswith(".history.yaml")]

    total, touched = 0, 0
    for f in files:
        n = migrate_file(f, readout_ids, args.dry_run)
        if n:
            touched += 1
            total += n
            print(f"  {n}  {f.name}")
    verb = "would migrate" if args.dry_run else "migrated"
    print(f"{verb} {total} edges across {touched} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
