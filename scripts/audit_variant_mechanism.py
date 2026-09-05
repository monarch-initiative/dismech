#!/usr/bin/env python3
"""Audit Mendelian disorder entries for a structured variant mechanism.

A Mendelian entry names a causal gene and a mode of inheritance, but that says
nothing about *what the variant does to the gene product*: loss of function,
gain of function, dominant negative, hypomorphic. dismech records that claim in
``GeneticContext.functional_impact_category`` (``FunctionalImpactEnum``), which
hangs off a pathophysiology node's ``genetic_context`` (or a phenotype context).
The category is optional, so most entries curated before it existed carry the
mechanism only as prose -- "heterozygous loss-of-function variants in X" in a
node description -- where nothing can query it.

This audit finds the gap. An entry is **Mendelian** for its purposes when it
carries a disease-level ``inheritance`` block bound to a single-locus HPO mode
(AD, AR, X-linked, Y-linked, mitochondrial) *and* at least one ``genetic``
record with ``relationship_type: CAUSATIVE``, and no ``SOMATIC_DRIVER`` record.
It reports every such entry with no ``functional_impact_category`` anywhere in
the file (the legacy free-text ``functional_impact`` counts as annotated, since
it is a recorded claim, just an unqueryable one).

Two signals are attached to each gap to help pick a tranche:

* ``prose`` -- which mechanism terms already appear in the entry's own text
  (``lof``, ``gof``, ``dn``, ``hi`` for haploinsufficiency, ``hypo``). An entry
  whose prose already names the mechanism usually needs an evidence sentence,
  not new research.
* ``cached_hits`` -- how many of the entry's cited, cached references contain a
  sentence naming a mechanism term. Where this is non-zero the snippet that
  will verify already exists in ``references_cache/``.

Neither signal is a ruling. Prose can name a mechanism the entry then argues
against, and a cached sentence can be about a different gene in a review. The
category is a claim and takes its own evidence item.

``UNKNOWN`` counts as annotated, since it is a recorded claim rather than an
empty slot -- but it is two different claims wearing one value: "nobody has
looked" and "assessed, and the literature disagrees". The summary breaks out
entries whose only category is ``UNKNOWN`` so the second kind stays countable;
the convention for the contested kind is ``UNKNOWN`` on the node plus competing
``mechanistic_hypotheses`` and a ``CONTROVERSY`` discussion carrying the
discriminating experiment. See
``docs/reports/mendelian-variant-mechanism-audit-2026-09-04.md`` for the worked
tranche and the five contested entries (Weaver, Bainbridge-Ropers,
Bohring-Opitz, Arboleda-Tham, ADNP).

Usage::

    uv run python scripts/audit_variant_mechanism.py              # summary
    uv run python scripts/audit_variant_mechanism.py --format list
    uv run python scripts/audit_variant_mechanism.py --format tsv --out /tmp/gap.tsv
    uv run python scripts/audit_variant_mechanism.py --single-gene --with-cached-hits

Advisory only: it always exits 0. The backlog is large and is meant to be
worked in tranches, not gated.
"""

from __future__ import annotations

import argparse
import collections
import glob
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from dismech.yaml_io import safe_load_path  # noqa: E402

MENDELIAN_MODES = {
    "HP:0000006": "AD",
    "HP:0000007": "AR",
    "HP:0001417": "XL",
    "HP:0001419": "XLR",
    "HP:0001423": "XLD",
    "HP:0001427": "MT",
    "HP:0001450": "YL",
}

PROSE_PATTERNS = {
    "lof": re.compile(r"loss[- ]of[- ]function", re.I),
    "gof": re.compile(r"gain[- ]of[- ]function", re.I),
    "dn": re.compile(r"dominant[- ]negative", re.I),
    "hi": re.compile(r"haploinsufficien", re.I),
    "hypo": re.compile(r"hypomorph", re.I),
}
MECHANISM_SENTENCE = re.compile(
    r"loss[- ]of[- ]function|gain[- ]of[- ]function|dominant[- ]negative|"
    r"haploinsufficien|hypomorph|null allele",
    re.I,
)


def _walk(obj):
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from _walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk(v)


def _modes(entry):
    modes = set()
    blocks = list(entry.get("inheritance") or [])
    for g in entry.get("genetic") or []:
        inh = g.get("inheritance")
        if isinstance(inh, list):
            blocks.extend(inh)
    for blk in blocks:
        if not isinstance(blk, dict):
            continue
        term = ((blk.get("inheritance_term") or {}).get("term") or {}).get("id")
        if term in MENDELIAN_MODES:
            modes.add(MENDELIAN_MODES[term])
    return modes


def cached_mechanism_hits(text, cache_dir):
    """Count cited PMIDs whose cache file has a sentence naming a mechanism."""
    hits = 0
    for pmid in sorted(set(re.findall(r"reference: (PMID:\d+)", text))):
        path = os.path.join(cache_dir, pmid.replace(":", "_") + ".md")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            body = fh.read()
        if MECHANISM_SENTENCE.search(body):
            hits += 1
    return hits


def audit_file(path, cache_dir=None):
    """Return a row dict for one entry, or None if it is not a Disease mapping."""
    entry = safe_load_path(path)
    if not isinstance(entry, dict):
        return None
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    genetic = [g for g in (entry.get("genetic") or []) if isinstance(g, dict)]
    causal = [g.get("name") for g in genetic if g.get("relationship_type") == "CAUSATIVE"]
    somatic = any(g.get("relationship_type") == "SOMATIC_DRIVER" for g in genetic)
    categories, legacy = set(), set()
    for obj in _walk(entry):
        if "functional_impact_category" in obj:
            categories.add(str(obj["functional_impact_category"]))
        if "functional_impact" in obj:
            legacy.add(str(obj["functional_impact"]))
    modes = _modes(entry)
    row = {
        "file": path,
        "name": entry.get("name"),
        "modes": "/".join(sorted(modes)),
        "mendelian": bool(modes) and bool(causal) and not somatic,
        "n_causal": len(causal),
        "causal_genes": "; ".join(str(c) for c in causal),
        "categories": "/".join(sorted(categories)),
        "legacy_functional_impact": "/".join(sorted(legacy)),
        "prose": ",".join(k for k, p in PROSE_PATTERNS.items() if p.search(text)),
        "n_pathophysiology": len(entry.get("pathophysiology") or []),
    }
    row["annotated"] = bool(categories or legacy)
    row["cached_hits"] = cached_mechanism_hits(text, cache_dir) if cache_dir else None
    return row


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="*", help="KB files (default: kb/disorders/*.yaml)")
    ap.add_argument("--format", choices=["summary", "list", "tsv"], default="summary")
    ap.add_argument("--out", help="Write the tsv/list output to this path instead of stdout")
    ap.add_argument("--single-gene", action="store_true", help="Only entries with exactly one CAUSATIVE gene")
    ap.add_argument("--with-cached-hits", action="store_true",
                    help="Only entries with at least one cited cached reference naming a mechanism")
    ap.add_argument("--all", action="store_true", help="List annotated entries too (tsv/list)")
    ap.add_argument("--cache-dir", default="references_cache")
    args = ap.parse_args(argv)

    files = args.files or sorted(glob.glob("kb/disorders/*.yaml"))
    rows = [r for r in (audit_file(f, args.cache_dir) for f in files) if r]
    mendelian = [r for r in rows if r["mendelian"]]
    gaps = [r for r in mendelian if not r["annotated"]]
    if args.single_gene:
        gaps = [r for r in gaps if r["n_causal"] == 1]
    if args.with_cached_hits:
        gaps = [r for r in gaps if r["cached_hits"]]

    if args.format == "summary":
        print(f"entries scanned:                          {len(rows)}")
        print(f"mendelian (inheritance + CAUSATIVE gene): {len(mendelian)}")
        annotated = sum(1 for r in mendelian if r["annotated"])
        contested = sum(1 for r in mendelian if r["categories"] == "UNKNOWN")
        print(f"  with functional_impact_category:        {annotated}")
        print(f"    of which recorded as UNKNOWN only:    {contested}")
        print(f"  without (the gap):                      {len(mendelian) - annotated}")
        print(f"  gap, single causal gene:                {sum(1 for r in mendelian if not r['annotated'] and r['n_causal'] == 1)}")
        print(f"  gap, mechanism named in own prose:      {sum(1 for r in mendelian if not r['annotated'] and r['prose'])}")
        print(f"  gap, mechanism sentence in cached refs: {sum(1 for r in mendelian if not r['annotated'] and r['cached_hits'])}")
        by_mode = collections.Counter(r["modes"] for r in mendelian if not r["annotated"])
        print("  gap by mode: " + ", ".join(f"{m}={n}" for m, n in by_mode.most_common()))
        cats = collections.Counter(c for r in rows for c in r["categories"].split("/") if c)
        print("categories in use: " + ", ".join(f"{c}={n}" for c, n in cats.most_common()))
        return 0

    selected = gaps if not args.all else (mendelian if not args.single_gene else [r for r in mendelian if r["n_causal"] == 1])
    cols = ["file", "name", "modes", "causal_genes", "n_causal", "prose", "cached_hits", "categories", "legacy_functional_impact"]
    lines = []
    if args.format == "tsv":
        lines.append("\t".join(cols))
        for r in selected:
            lines.append("\t".join("" if r[c] is None else str(r[c]) for c in cols))
    else:
        for r in sorted(selected, key=lambda r: (-(r["cached_hits"] or 0), r["name"] or "")):
            lines.append(f"{r['name']} [{r['modes']}] {r['causal_genes']} prose={r['prose'] or '-'} cached_hits={r['cached_hits']}")
    text = "\n".join(lines) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {len(selected)} row(s) to {args.out}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
