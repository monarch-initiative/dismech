#!/usr/bin/env python3
"""Build ``datasets:`` records for dismech entries from verified GEO metadata.

This is the batch arm of the dataset-curation workflow. It runs in two phases so
that nothing is written to the KB without a relevance decision:

``propose``
    Search GEO for each disorder (via :mod:`discover_datasets`), keep the
    candidates that name the disease in their own metadata, re-verify every
    accession against NCBI, and write a proposal JSON.

``apply``
    Turn an (optionally triaged) proposal into ``datasets:`` blocks in the
    entry YAML, preserving the file's existing formatting and comments.

Every field written comes from the repository's own record -- the accession,
the title verbatim, the summary, the organism, the sample count, and the linked
PMID. Nothing is model-generated, so there is no snippet or identifier for a
model to invent.

Deliberately omitted
--------------------
``evidence:`` blocks are **not** generated. A dismech evidence item needs an
exact quote from the cited abstract, and producing those in bulk is precisely
where fabrication creeps in. Records carry ``publication:`` (GEO's own PMID
link) and a provenance ``notes`` line instead; evidence enrichment is a
follow-up for a curator or a targeted agent pass.

Usage
-----
    # propose for a batch of disorders
    uv run python scripts/build_dataset_records.py propose --slugs-file batch1.txt \\
        --out proposals/batch1.json

    # inspect, optionally edit "approved": false on any record, then
    uv run python scripts/build_dataset_records.py apply proposals/batch1.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discover_datasets import discover, load_entry
from verify_dataset_accessions import (
    OK,
    PREFIX_MISMATCH,
    Throttle,
    verify_one,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
CACHE_PATH = REPO_ROOT / "cache" / "dataset_accessions.json"

# Only organisms already established in the KB, so term validation stays green
# without pulling the 13.5 GB NCBITaxon sqlite.
ORGANISMS = {
    "homo sapiens": ("human", "NCBITaxon:9606", "Homo sapiens"),
    "mus musculus": ("mouse", "NCBITaxon:10090", "Mus musculus"),
    "rattus norvegicus": ("rat", "NCBITaxon:10116", "Rattus norvegicus"),
    "danio rerio": ("zebrafish", "NCBITaxon:7955", "Danio rerio"),
    "drosophila melanogaster": ("fruit fly", "NCBITaxon:7227", "Drosophila melanogaster"),
    "sus scrofa": ("pig", "NCBITaxon:9823", "Sus scrofa"),
    "macaca mulatta": ("rhesus macaque", "NCBITaxon:9544", "Macaca mulatta"),
}

# A dataset must clear this to be proposed at all.
MIN_SCORE = 6.0
MAX_PER_DISORDER = 3
MIN_SAMPLES = 6


def trim_summary(text: str, limit: int = 700) -> str:
    """Trim GEO's summary to whole sentences, without paraphrasing it."""
    text = re.sub(r"\s+", " ", (text or "").strip())
    if len(text) <= limit:
        return text
    cut = text[:limit]
    for sep in (". ", "; "):
        idx = cut.rfind(sep)
        if idx > limit * 0.5:
            return cut[: idx + 1].strip()
    return cut.rstrip() + "..."


def candidate_to_record(cand: dict, disease_name: str) -> dict:
    """Build a schema-shaped Dataset record from repository metadata only."""
    rec: dict = {"accession": cand["accession"], "title": cand["title"]}

    summary = trim_summary(cand.get("summary", ""))
    if summary:
        rec["description"] = summary

    org = ORGANISMS.get((cand.get("organism") or "").strip().lower())
    if org:
        pref, tid, label = org
        rec["organism"] = {"preferred_term": pref, "term": {"id": tid, "label": label}}

    if cand.get("data_type"):
        rec["data_type"] = cand["data_type"]
    if cand.get("sample_count"):
        rec["sample_count"] = int(cand["sample_count"])
    if cand.get("pubmed_ids"):
        rec["publication"] = f"PMID:{cand['pubmed_ids'][0]}"

    today = dt.datetime.now(dt.UTC).date().isoformat()
    verified_fields = "Title and sample count are GEO's own values."
    if org:
        verified_fields = "Title, sample count, and organism are GEO's own values."
    elif cand.get("organism"):
        verified_fields += f" GEO reported organism '{cand['organism']}', which was not ontology-mapped here."
    rec["notes"] = (
        f"Identified by GEO DataSets index search for {disease_name} "
        f"(scripts/discover_datasets.py); accession and metadata verified against "
        f"NCBI E-utilities on {today}. {verified_fields}"
    )
    return rec


def propose(slugs: list[str], limit: int, out_path: Path, min_score: float) -> int:
    cache: dict = {}
    if CACHE_PATH.exists():
        try:
            cache = json.loads(CACHE_PATH.read_text())
        except json.JSONDecodeError:
            cache = {}
    import os

    api_key = os.environ.get("NCBI_API_KEY")
    throttle = Throttle(9.0 if api_key else 2.5)

    proposals = []
    for i, slug in enumerate(slugs, 1):
        try:
            entry = load_entry(slug)
        except SystemExit:
            print(f"[{i}/{len(slugs)}] {slug}: no such entry, skipping", file=sys.stderr)
            continue
        disease_name = (entry.get("name") or slug).replace("_", " ")

        try:
            cands = discover(slug, limit=limit, per_query=20, use_synonyms=True)
        except Exception as exc:
            print(f"[{i}/{len(slugs)}] {slug}: discovery failed ({exc})", file=sys.stderr)
            continue

        kept = []
        for c in cands:
            cd = c.__dict__ if hasattr(c, "__dict__") else c
            if cd.get("relevance") != "DIRECT":
                continue
            if cd.get("score", 0) < min_score:
                continue
            if (cd.get("sample_count") or 0) < MIN_SAMPLES:
                continue
            # Re-verify: discovery and verification are independent paths, and
            # the record must exist at apply time, not just at search time.
            res = verify_one(cd["accession"], cache, throttle, api_key, refresh=False)
            if res.status not in (OK, PREFIX_MISMATCH):
                print(f"    ! {cd['accession']} did not verify ({res.status}); dropped", file=sys.stderr)
                continue
            kept.append(cd)
            if len(kept) >= MAX_PER_DISORDER:
                break

        proposals.append(
            {
                "slug": slug,
                "disease_name": disease_name,
                "n_candidates": len(cands),
                "records": [
                    {"approved": True, "score": c.get("score"), "matched_query": c.get("matched_query"),
                     "record": candidate_to_record(c, disease_name)}
                    for c in kept
                ],
            }
        )
        print(f"[{i}/{len(slugs)}] {slug}: {len(kept)} proposed (of {len(cands)} candidates)", flush=True)

    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(proposals, indent=2) + "\n")
    total = sum(len(p["records"]) for p in proposals)
    with_any = sum(1 for p in proposals if p["records"])
    print(f"\nWrote {out_path}: {total} records across {with_any}/{len(proposals)} disorders")
    return 0


def render_records(records: list[dict]) -> str:
    """Render records as a YAML sequence in the KB's prevailing style."""
    text = yaml.safe_dump(
        records,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        width=100000,  # keep each scalar on one line, as most KB entries do
    )
    # safe_dump indents sequence items under a mapping; at top level it already
    # emits "- key: value" at column 0, which is the dismech convention.
    return text if text.endswith("\n") else text + "\n"


def splice_datasets(text: str, new_records: list[dict]) -> str:
    """Insert records into a KB file's ``datasets:`` block *textually*.

    Round-tripping the whole document through a YAML emitter reformats every
    long scalar in the file (in one direction or the other, depending on the
    configured width), which buries a three-line addition in a thousand-line
    diff. Splicing text leaves every untouched byte untouched.
    """
    # Match the file's existing line terminator throughout. One KB entry
    # (Mycosis_Fungoides) is CRLF, and emitting LF into it would rewrite every
    # line of the file as a line-ending change.
    nl = "\r\n" if "\r\n" in text else "\n"
    block = render_records(new_records)
    if nl == "\r\n":
        block = block.replace("\r\n", "\n").replace("\n", "\r\n")
    header = f"datasets:{nl}"
    lines = text.splitlines(keepends=True)

    start = None
    for i, line in enumerate(lines):
        if re.match(r"^datasets:\s*(\[\s*\])?\s*$", line):
            start = i
            break

    if start is None:
        # No datasets key at all: append one at the end of the document.
        prefix = text if text.endswith(("\n", "\r")) else text + nl
        return prefix + header + block

    if re.match(r"^datasets:\s*\[\s*\]\s*$", lines[start]):
        # `datasets: []` -> a real block
        return "".join(lines[:start]) + header + block + "".join(lines[start + 1 :])

    # Existing non-empty block: find where it ends (the next top-level key).
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].strip() and not lines[j].startswith((" ", "-", "\t")):
            end = j
            break
    body = "".join(lines[start:end])
    if not body.endswith(("\n", "\r")):
        body += nl
    return "".join(lines[:start]) + body + block + "".join(lines[end:])


def apply_proposals(path: Path, dry_run: bool) -> int:
    proposals = json.loads(path.read_text())
    changed, skipped = [], []

    for prop in proposals:
        approved = [r["record"] for r in prop["records"] if r.get("approved")]
        if not approved:
            skipped.append(prop["slug"])
            continue

        fpath = KB_DIR / f"{prop['slug']}.yaml"
        if not fpath.exists():
            skipped.append(prop["slug"])
            continue

        text = fpath.read_text(newline="")
        doc = yaml.safe_load(text) or {}
        have = {str(d.get("accession")) for d in (doc.get("datasets") or []) if isinstance(d, dict)}
        new = [r for r in approved if r["accession"] not in have]
        if not new:
            skipped.append(prop["slug"])
            continue

        updated = splice_datasets(text, new)

        # The splice must not change anything except the datasets list.
        before, after = yaml.safe_load(text) or {}, yaml.safe_load(updated) or {}
        before.pop("datasets", None)
        after_ds = after.pop("datasets", None)
        if before != after:
            print(f"  !! {prop['slug']}: splice altered other content, skipping", file=sys.stderr)
            skipped.append(prop["slug"])
            continue
        if len(after_ds or []) != len(doc.get("datasets") or []) + len(new):
            print(f"  !! {prop['slug']}: unexpected dataset count after splice, skipping", file=sys.stderr)
            skipped.append(prop["slug"])
            continue

        if not dry_run:
            fpath.write_text(updated, newline="")
        changed.append((prop["slug"], len(new)))

    for slug, n in changed:
        print(f"  {'would add' if dry_run else 'added'} {n} dataset(s) to {slug}")
    print(f"\n{len(changed)} entries {'would be ' if dry_run else ''}updated, {len(skipped)} skipped")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("propose", help="search GEO and write a proposal JSON")
    p.add_argument("--slugs", nargs="*", default=[])
    p.add_argument("--slugs-file", type=Path)
    p.add_argument("--limit", type=int, default=12, help="GEO candidates to consider per disorder")
    p.add_argument("--min-score", type=float, default=MIN_SCORE)
    p.add_argument("--out", type=Path, required=True)

    a = sub.add_parser("apply", help="write approved records into the KB")
    a.add_argument("proposals", type=Path)
    a.add_argument("--dry-run", action="store_true")

    args = ap.parse_args()
    if args.cmd == "propose":
        slugs = list(args.slugs)
        if args.slugs_file:
            slugs.extend([s.strip() for s in args.slugs_file.read_text().splitlines() if s.strip()])
        if not slugs:
            ap.error("pass --slugs or --slugs-file")
        return propose(slugs, args.limit, args.out, args.min_score)
    return apply_proposals(args.proposals, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
