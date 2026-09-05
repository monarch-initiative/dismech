#!/usr/bin/env python3
"""NEC-risk disease-class audit for the dismech knowledge base.

Named Entity Confusion (NEC) is the deep-research failure mode tracked in
issue #3889: a DR tool resolves a queried disease name to a *different*
disease entity and produces a coherent-but-wrong report. Standard
hallucination checks (snippet-in-abstract, PMID existence, term validation)
cannot catch NEC because a wrong-entity report validates against its own
(real) wrong-disease sources.

This script implements acceptance-criterion item 3 of #3889 — *identify the
high-NEC-risk disease classes* — by scanning every current ``kb/disorders``
entry and flagging the four structural risk patterns named in the issue:

* ``NUMBERED_SERIES``  — numbered / lettered series where numbering has drifted
  historically (e.g. SCAR1-SCAR20, CMT types, "type II").
* ``EPONYM_COLLISION`` — an eponym (surname) shared by more than one dismech
  entry, the classic Temtamy / Lichtenstein-Knorr collision pattern.
* ``SYNONYM_ALIASING`` — an entry whose synonym list contains a *different*
  eponym from the primary name (the historical-synonym-maps-elsewhere risk).
* ``ACRONYM_AMBIGUITY``— a short all-caps acronym synonym that is easy to
  resolve to the wrong expansion.

The output is deliberately a *risk-class* flagger, not an assertion that any
specific confusion has occurred. It complements ``src/dismech/preflight_dr.py``
(#3889), which performs the per-report gene-identity cross-check.

Usage::

    uv run python scripts/nec_risk_audit.py            # summary table
    uv run python scripts/nec_risk_audit.py --markdown  # full markdown report
"""
from __future__ import annotations

import argparse
import glob
import os
from collections import defaultdict

from dismech.nec_risk import (
    ACRONYM_RE,
    NON_EPONYM_WORDS,
    SERIES_PREFIXES,
    SERIES_RE,
    TYPE_RE,
    acronym_synonyms,
    eponyms_in,
    series_hits,
)
from dismech.yaml_io import safe_load

# The detection logic itself lives in ``dismech.nec_risk`` so the priority
# dashboard can reuse it against *uncurated* MONDO candidates. This script is
# the corpus-level view over the entries already in ``kb/disorders``. The
# re-exports above keep the historical module surface (tests and any caller
# that imported these names from here) intact.
__all__ = [
    "ACRONYM_RE",
    "DISORDERS_GLOB",
    "NON_EPONYM_WORDS",
    "SERIES_PREFIXES",
    "SERIES_RE",
    "TYPE_RE",
    "audit",
    "eponyms_in",
    "load_entries",
]

DISORDERS_GLOB = "kb/disorders/*.yaml"


def load_entries():
    rows = []
    for path in sorted(glob.glob(DISORDERS_GLOB)):
        if path.endswith(".history.yaml"):
            continue
        try:
            with open(path) as fh:
                data = safe_load(fh)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        term = (data.get("disease_term") or {}).get("term") or {}
        rows.append(
            {
                "file": os.path.basename(path),
                "name": data.get("name") or "",
                "mondo": term.get("id"),
                "label": term.get("label") or "",
                "synonyms": [s for s in (data.get("synonyms") or []) if isinstance(s, str)],
            }
        )
    return rows


def audit(rows):
    findings = defaultdict(list)  # category -> list of dict
    eponym_to_files = defaultdict(set)

    for r in rows:
        haystack = " ".join([r["name"], r["label"]] + r["synonyms"])

        # 1. Numbered / lettered series.
        hits = series_hits(haystack)
        if hits:
            findings["NUMBERED_SERIES"].append({**r, "hits": sorted(hits)})

        # 2. Eponyms (for collision grouping).
        eps = eponyms_in(r["name"]) | eponyms_in(r["label"])
        for ep in eps:
            eponym_to_files[ep].add(r["file"])

        # 3. Synonym aliasing: a synonym carries a *different* eponym than name.
        name_eps = eponyms_in(r["name"]) | eponyms_in(r["label"])
        alias_eps = set()
        for syn in r["synonyms"]:
            alias_eps |= eponyms_in(syn)
        extra = alias_eps - name_eps
        if extra:
            findings["SYNONYM_ALIASING"].append({**r, "alias_eponyms": sorted(extra)})

        # 4. Acronym ambiguity: short all-caps synonym.
        acr = acronym_synonyms(r["synonyms"])
        if acr:
            findings["ACRONYM_AMBIGUITY"].append({**r, "acronyms": acr})

    # Eponym collisions = surname shared by >1 distinct entry.
    for ep, files in sorted(eponym_to_files.items()):
        if len(files) > 1:
            findings["EPONYM_COLLISION"].append({"eponym": ep, "files": sorted(files)})

    return findings


def print_summary(rows, findings):
    print(f"Scanned {len(rows)} current disorder entries.\n")
    print(f"{'Risk class':<20}{'entries flagged':>16}")
    print("-" * 36)
    for cat in ("NUMBERED_SERIES", "EPONYM_COLLISION", "SYNONYM_ALIASING", "ACRONYM_AMBIGUITY"):
        n = len(findings.get(cat, []))
        print(f"{cat:<20}{n:>16}")


def print_markdown(rows, findings):
    print(f"_Auto-generated by `scripts/nec_risk_audit.py` over {len(rows)} current "
          f"non-history `kb/disorders/*.yaml` entries (excludes `*.history.yaml`)._\n")
    print("| Risk class | Entries flagged |")
    print("|---|---|")
    for cat in ("NUMBERED_SERIES", "EPONYM_COLLISION", "SYNONYM_ALIASING", "ACRONYM_AMBIGUITY"):
        print(f"| {cat} | {len(findings.get(cat, []))} |")
    print()

    print("### Eponymic collisions (surname shared by >1 entry)\n")
    print("These are the highest-risk class: a DR tool can silently resolve the "
          "eponym to the wrong member.\n")
    for f in findings.get("EPONYM_COLLISION", []):
        print(f"- **{f['eponym']}** — {', '.join(f['files'])}")
    print()

    print("### Synonym aliasing (synonym carries a different eponym than the primary name)\n")
    for f in findings.get("SYNONYM_ALIASING", []):
        print(f"- `{f['file']}` ({f['name']}, {f['mondo']}) — alias eponym(s): "
              f"{', '.join(f['alias_eponyms'])}")
    print()

    print("### Acronym-ambiguity synonyms (sample)\n")
    for f in findings.get("ACRONYM_AMBIGUITY", [])[:40]:
        print(f"- `{f['file']}` ({f['mondo']}) — {', '.join(f['acronyms'])}")
    print()

    print("### Numbered / lettered series (sample)\n")
    for f in findings.get("NUMBERED_SERIES", [])[:40]:
        print(f"- `{f['file']}` ({f['mondo']}) — {', '.join(f['hits'])}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--markdown", action="store_true", help="emit full markdown report")
    args = ap.parse_args()
    rows = load_entries()
    findings = audit(rows)
    if args.markdown:
        print_markdown(rows, findings)
    else:
        print_summary(rows, findings)


if __name__ == "__main__":
    main()
