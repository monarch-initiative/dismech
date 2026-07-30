#!/usr/bin/env python3
"""dismech#7175 content evaluation: audit the Mondo-anchoring state of every disorder.

Fully local & deterministic. For each kb/disorders/*.yaml this reports:

  1. Primary ``disease_term`` anchor state (MONDO id / term-without-id / no disease_term).
  2. For MONDO-anchored entries, three OAK checks against ``sqlite:obo:mondo``:
       - MISSING  : the id is absent from the current Mondo release
       - OBSOLETE : the id is deprecated/obsoleted in Mondo
       - LABEL_DRIFT : stored ``term.label`` != Mondo's canonical label
  3. Whether an unanchored entry references MONDO anywhere else in the file
     (=> "promote the anchor", a modeling fix) or nowhere (=> Mondo new-term candidate).
  4. ``mondo_mappings`` skos-predicate breakdown (narrow/broad = granularity mismatch).

Usage:
    uv run python scripts/mondo_anchor_audit.py            # human summary to stdout
    uv run python scripts/mondo_anchor_audit.py --tsv OUT  # also write a worklist TSV

The report committed under docs/reports/ is produced from this script; regenerate it
after KB or Mondo-release changes rather than hand-editing.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from collections import Counter

import yaml
from oaklib import get_adapter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISORDERS = os.path.join(ROOT, "kb", "disorders")
MONDO_ID_RE = re.compile(r"MONDO:\d+")
OMIM_ID_RE = re.compile(r"OMIM:\d+")


def load(path):
    with open(path) as fh:
        return yaml.safe_load(fh)


def primary_anchor(doc):
    """Return (state, mondo_id, stored_label). state in MONDO/OTHER/NO_ID/NO_TERM."""
    dt = (doc or {}).get("disease_term")
    if not isinstance(dt, dict):
        return "NO_TERM", None, None
    term = dt.get("term") or {}
    tid = term.get("id")
    if not tid:
        return "NO_ID", None, None
    prefix = tid.split(":")[0]
    if prefix == "MONDO":
        return "MONDO", tid, term.get("label")
    return "OTHER:" + prefix, tid, term.get("label")


def mapping_preds(doc):
    c = Counter()
    m = (doc or {}).get("mappings") or {}
    for entry in m.get("mondo_mappings") or []:
        pred = entry.get("mapping_predicate") or entry.get("predicate") or ""
        if pred:
            c[pred.replace("skos:", "")] += 1
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv", help="write a machine-readable worklist TSV to this path")
    args = ap.parse_args()

    adapter = get_adapter("sqlite:obo:mondo")
    obsoletes = set(adapter.obsoletes())

    n = 0
    state_counts = Counter()
    pred_totals = Counter()
    missing, obsolete, label_drift = [], [], []
    no_mondo_anywhere, mondo_elsewhere = [], []
    narrow, broad = [], []
    tsv_rows = []

    for path in sorted(glob.glob(os.path.join(DISORDERS, "*.yaml"))):
        n += 1
        name = os.path.basename(path)[:-5]
        raw = open(path).read()
        doc = load(path)
        state, mid, stored = primary_anchor(doc)
        preds = mapping_preds(doc)
        pred_totals.update(preds)

        base_state = state.split(":")[0] if state.startswith("OTHER") else state
        state_counts[state] += 1

        oak_flag = ""
        if state == "MONDO":
            canonical = adapter.label(mid)
            if mid in obsoletes:
                obsolete.append((name, mid, stored, canonical))
                oak_flag = "OBSOLETE"
            elif canonical is None:
                missing.append((name, mid, stored))
                oak_flag = "MISSING"
            elif stored and canonical and stored.strip() != canonical.strip():
                label_drift.append((name, mid, stored, canonical))
                oak_flag = "LABEL_DRIFT"
        elif base_state in ("NO_TERM", "NO_ID") or state.startswith("OTHER"):
            omims = sorted(set(OMIM_ID_RE.findall(raw)))
            if MONDO_ID_RE.search(raw):
                mondo_elsewhere.append((name, state, sorted(set(MONDO_ID_RE.findall(raw)))))
            else:
                no_mondo_anywhere.append((name, state, omims))

        if preds.get("narrowMatch"):
            narrow.append((name, preds["narrowMatch"]))
        if preds.get("broadMatch"):
            broad.append((name, preds["broadMatch"]))

        tsv_rows.append((name, state, mid or "", stored or "", oak_flag,
                         ",".join(f"{k}:{v}" for k, v in sorted(preds.items()))))

    out = sys.stdout
    p = lambda *a: print(*a, file=out)
    p(f"# Mondo-anchoring audit  (kb/disorders, n={n})\n")
    p("## Primary disease_term anchor state")
    for k, v in sorted(state_counts.items(), key=lambda x: -x[1]):
        p(f"  {v:5d}  {k}")

    p(f"\n## OAK checks on MONDO-anchored entries")
    p(f"  MISSING (id absent from Mondo release): {len(missing)}")
    for name, mid, stored in missing:
        p(f"     - {name}: {mid} (stored '{stored}')")
    p(f"  OBSOLETE (deprecated in Mondo): {len(obsolete)}")
    for name, mid, stored, canon in obsolete:
        p(f"     - {name}: {mid} (stored '{stored}'; canonical '{canon}')")
    p(f"  LABEL_DRIFT (stored label != canonical): {len(label_drift)}")
    for name, mid, stored, canon in label_drift:
        p(f"     - {name}: {mid}  stored='{stored}'  canonical='{canon}'")

    p(f"\n## Unanchored primary slot -> NO MONDO anywhere (Mondo new-term candidates): {len(no_mondo_anywhere)}")
    for name, state, omims in sorted(no_mondo_anywhere):
        p(f"     - {name}  [{state}]  {('OMIM ' + ','.join(omims)) if omims else ''}")
    p(f"\n## Unanchored primary slot -> MONDO present elsewhere (promote-anchor modeling fix): {len(mondo_elsewhere)}")
    for name, state, mondos in sorted(mondo_elsewhere):
        p(f"     - {name}  [{state}]  {','.join(mondos)}")

    p(f"\n## mondo_mappings granularity mismatch")
    p(f"  narrowMatch (dismech finer than mapped Mondo): {len(narrow)}")
    for name, cnt in sorted(narrow):
        p(f"     - {name}  x{cnt}")
    p(f"  broadMatch (dismech broader than mapped Mondo): {len(broad)}")
    for name, cnt in sorted(broad):
        p(f"     - {name}  x{cnt}")

    p(f"\n## mondo_mappings skos-predicate totals")
    for k, v in sorted(pred_totals.items(), key=lambda x: -x[1]):
        p(f"  {v:5d}  {k}")

    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write("name\tanchor_state\tmondo_id\tstored_label\toak_flag\tmondo_mapping_preds\n")
            for row in tsv_rows:
                fh.write("\t".join(row) + "\n")
        p(f"\n[wrote worklist TSV: {args.tsv} ({len(tsv_rows)} rows)]")


if __name__ == "__main__":
    main()
