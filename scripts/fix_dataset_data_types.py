#!/usr/bin/env python3
"""Correct `data_type` on GEO dataset records that contradict their own text.

GEO's `gdstype` is a small controlled vocabulary that cannot express assay
resolution: every single-cell, single-nucleus and spatial series is labelled
"Expression profiling by high throughput sequencing", and ATAC-seq shares
"Genome binding/occupancy profiling" with ChIP-seq. The original mapping table
therefore emitted `BULK_RNA_SEQ` for scRNA/spatial series and could never emit
`ATAC_SEQ` at all -- 156 records across the GEO batches carry a `data_type`
their own title contradicts.

This rewrites those values in place using :func:`discover_datasets.refine_data_type`,
editing only the `data_type:` line inside the offending record and re-parsing to
confirm nothing else moved.

    uv run python scripts/fix_dataset_data_types.py --dry-run
    uv run python scripts/fix_dataset_data_types.py
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discover_datasets import ASSAY_PATTERNS, BRACKETED_TITLE_ASSAYS, refine_data_type

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"


def wanted_type(record: dict) -> str:
    """The assay the record's own title/description names, if any."""
    current = str(record.get("data_type") or "")
    if current in {
        "METHYLATION",
        "MICROARRAY",
        "PROTEOMICS",
        "METABOLOMICS",
        "MULTI_OMICS",
        "MULTI_OMICS_PERTURBATION",
        "WGS",
        "GWAS",
    }:
        return current
    title = str(record.get("title") or "")
    text = f"{title} {record.get('description', '')}"
    if not any(pattern.search(text) for pattern, _enum in ASSAY_PATTERNS) and not any(
        pattern.search(title) for pattern, _enum in BRACKETED_TITLE_ASSAYS
    ):
        return ""
    if current in {"CHIP_SEQ", "ATAC_SEQ"}:
        gds_type, mapped = "Genome binding/occupancy profiling", "CHIP_SEQ"
    else:
        gds_type, mapped = (
            "Expression profiling by high throughput sequencing",
            "BULK_RNA_SEQ",
        )
    return refine_data_type(gds_type, text, mapped, title)


def fix_file(
    path: Path, dry_run: bool, allowed: set[str] | None = None
) -> list[tuple[str, str, str]]:
    with path.open(newline="") as stream:
        text = stream.read()
    if allowed is not None and not any(acc in text for acc in allowed):
        return []
    doc = yaml.safe_load(text) or {}
    changes: list[tuple[str, str, str]] = []

    for rec in doc.get("datasets") or []:
        if not isinstance(rec, dict):
            continue
        acc = str(rec.get("accession", ""))
        if not acc.startswith("geo:"):
            continue
        if allowed is not None and acc not in allowed:
            continue
        want = wanted_type(rec)
        if not want or rec.get("data_type") == want:
            continue
        changes.append((acc, str(rec.get("data_type") or "(absent)"), want))

    if not changes or dry_run:
        return changes

    lines = text.splitlines(keepends=True)
    nl = "\r\n" if "\r\n" in text else "\n"
    for acc, _old, want in changes:
        start = next(
            (
                i
                for i, ln in enumerate(lines)
                if ln.strip() in (f"- accession: {acc}", f"-   accession: {acc}")
            ),
            None,
        )
        if start is None:
            continue
        end = next(
            (
                j
                for j in range(start + 1, len(lines))
                if lines[j].lstrip().startswith("- ")
                or (lines[j].strip() and not lines[j].startswith((" ", "\t")))
            ),
            len(lines),
        )
        dt_line = next(
            (j for j in range(start, end) if re.match(r"\s*data_type:", lines[j])), None
        )
        if dt_line is not None:
            indent = re.match(r"(\s*)", lines[dt_line]).group(1)
            lines[dt_line] = f"{indent}data_type: {want}{nl}"
        else:
            # Insert after `title:` so field order matches generated records.
            anchor = next(
                (j for j in range(start, end) if re.match(r"\s*title:", lines[j])),
                start,
            )
            indent = (
                re.match(r"(\s*)", lines[anchor]).group(1) if anchor != start else "  "
            )
            lines.insert(anchor + 1, f"{indent}data_type: {want}{nl}")

    updated = "".join(lines)
    before, after = yaml.safe_load(text) or {}, yaml.safe_load(updated) or {}
    if [d.get("accession") for d in before.get("datasets") or []] != [
        d.get("accession") for d in after.get("datasets") or []
    ]:
        print(f"  !! {path.name}: accession list changed, skipping", file=sys.stderr)
        return []
    before.pop("datasets", None)
    after_ds = after.pop("datasets", None)
    if before != after:
        print(
            f"  !! {path.name}: edit touched other content, skipping", file=sys.stderr
        )
        return []
    for rec in after_ds or []:
        acc = str(rec.get("accession", ""))
        for a, _o, w in changes:
            if acc == a and rec.get("data_type") != w:
                print(f"  !! {path.name}: {acc} not updated, skipping", file=sys.stderr)
                return []

    path.write_text(updated, newline="")
    return changes


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--accessions-file",
        type=Path,
        help="restrict to these accessions (one per line), so a batch branch "
        "corrects only the records it introduced",
    )
    args = ap.parse_args()

    allowed = None
    if args.accessions_file:
        allowed = {
            ln.strip()
            for ln in args.accessions_file.read_text().splitlines()
            if ln.strip()
        }

    total = 0
    by_type: dict[str, int] = {}
    for path in sorted(KB_DIR.glob("*.yaml")):
        for acc, old, want in fix_file(path, args.dry_run, allowed):
            total += 1
            by_type[want] = by_type.get(want, 0) + 1
            print(f"  {path.stem:44s} {acc:16s} {old:26s} -> {want}")
    verb = "would correct" if args.dry_run else "corrected"
    print(f"\n{verb} {total} records")
    for k, v in sorted(by_type.items()):
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
