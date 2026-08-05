#!/usr/bin/env python3
"""Apply the three record-quality follow-ups raised in review of #7609.

1. **Drop redundant GEO SuperSeries shells.** When a placeholder SuperSeries
   and an informative SubSeries share a publication, drop only the placeholder.
   Distinct assay arms and non-GEO cohort studies are preserved even when they
   share a paper.

2. **Drop boilerplate descriptions.** GEO's own text for a SuperSeries is
   "This SuperSeries is composed of the SubSeries listed below.", which carries
   no information about the dataset.

3. **Link history records to their PR**, so the audit trail is traversable
   from `history/` back to the review.

Dataset records are only ever removed or stripped of boilerplate, never
otherwise rewritten, and the file is re-parsed to
confirm nothing outside `datasets:` moved.

    uv run python scripts/tidy_dataset_records.py --pr 7609 --accessions-file accs.txt --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
HISTORY_DIR = REPO_ROOT / "history" / "disorders"

BOILERPLATE = re.compile(
    r"^This SuperSeries is composed of the SubSeries listed below\.?$", re.IGNORECASE
)


def record_span(lines: list[str], acc: str) -> tuple[int, int] | None:
    start = next(
        (i for i, ln in enumerate(lines) if ln.strip() == f"- accession: {acc}"), None
    )
    if start is None:
        return None
    end = next(
        (
            j
            for j in range(start + 1, len(lines))
            if lines[j].lstrip().startswith("- ")
            or (lines[j].strip() and not lines[j].startswith((" ", "\t")))
        ),
        len(lines),
    )
    return start, end


def tidy_file(path: Path, allowed: set[str] | None, dry_run: bool) -> tuple[int, int]:
    with path.open(newline="") as stream:
        text = stream.read()
    doc = yaml.safe_load(text) or {}
    records = [r for r in (doc.get("datasets") or []) if isinstance(r, dict)]
    if not records:
        return 0, 0

    scoped = [
        r for r in records if allowed is None or str(r.get("accession", "")) in allowed
    ]

    # 1. Drop only placeholder GEO SuperSeries when an informative sibling
    # shares the publication. Publication identity alone is not duplication:
    # one paper can contain distinct assay arms or controlled-access cohorts.
    by_pub: dict[str, list[dict]] = {}
    for r in scoped:
        pub = r.get("publication")
        if pub:
            by_pub.setdefault(str(pub), []).append(r)
    drop: set[str] = set()
    for group in by_pub.values():
        if len(group) < 2 or not all(
            str(r.get("accession", "")).startswith("geo:") for r in group
        ):
            continue
        informative = [
            r
            for r in group
            if not BOILERPLATE.match(" ".join(str(r.get("description") or "").split()))
        ]
        if informative:
            for r in group:
                if BOILERPLATE.match(" ".join(str(r.get("description") or "").split())):
                    drop.add(str(r["accession"]))

    # 2. boilerplate descriptions
    strip_desc = {
        str(r["accession"])
        for r in scoped
        if BOILERPLATE.match(" ".join(str(r.get("description") or "").split()))
        and str(r["accession"]) not in drop
    }

    if not drop and not strip_desc:
        return 0, 0
    if dry_run:
        return len(drop), len(strip_desc)

    lines = text.splitlines(keepends=True)
    for acc in sorted(
        drop | strip_desc, key=lambda a: -(record_span(lines, a) or (0, 0))[0]
    ):
        span = record_span(lines, acc)
        if not span:
            continue
        start, end = span
        if acc in drop:
            del lines[start:end]
        else:
            for j in range(start, end):
                if lines[j].lstrip().startswith("description:"):
                    k = j + 1
                    while (
                        k < end
                        and lines[k].startswith(" " * 4)
                        and not re.match(r"\s{2}\w+:", lines[k])
                    ):
                        k += 1
                    del lines[j:k]
                    break

    updated = "".join(lines)
    before, after = yaml.safe_load(text) or {}, yaml.safe_load(updated) or {}
    kept = [str(r.get("accession")) for r in (after.get("datasets") or [])]
    expected = [
        str(r.get("accession")) for r in records if str(r.get("accession")) not in drop
    ]
    before.pop("datasets", None)
    after.pop("datasets", None)
    if before != after or kept != expected:
        print(
            f"  !! {path.name}: edit altered other content, skipping", file=sys.stderr
        )
        return 0, 0

    path.write_text(updated, newline="")
    return len(drop), len(strip_desc)


def link_history(pr: int, added_only: set[str] | None, dry_run: bool) -> int:
    """Populate links.prs on history records that have none."""
    n = 0
    for path in sorted(HISTORY_DIR.glob("*/*.yaml")):
        if (
            added_only is not None
            and str(path.relative_to(REPO_ROOT)) not in added_only
        ):
            continue
        text = path.read_text()
        doc = yaml.safe_load(text) or {}
        if (doc.get("links") or {}).get("prs"):
            continue
        url = f"https://github.com/monarch-initiative/dismech/pull/{pr}"
        updated = text.replace("  prs: []\n", f"  prs:\n  - {url}\n", 1)
        if updated == text:
            continue
        after = yaml.safe_load(updated) or {}
        if (after.get("links") or {}).get("prs") != [url]:
            continue
        n += 1
        if not dry_run:
            path.write_text(updated)
    return n


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--pr", type=int, required=True)
    ap.add_argument(
        "--accessions-file",
        type=Path,
        help="restrict dataset tidying to accessions this branch introduced",
    )
    ap.add_argument(
        "--history-file",
        type=Path,
        help="restrict history linking to records this branch added",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    allowed = None
    if args.accessions_file and args.accessions_file.exists():
        allowed = {
            ln.strip()
            for ln in args.accessions_file.read_text().splitlines()
            if ln.strip()
        }
    hist = None
    if args.history_file and args.history_file.exists():
        hist = {
            ln.strip()
            for ln in args.history_file.read_text().splitlines()
            if ln.strip()
        }

    dropped = stripped = 0
    for path in sorted(KB_DIR.glob("*.yaml")):
        d, s = tidy_file(path, allowed, args.dry_run)
        if d or s:
            print(f"  {path.stem:46s} dropped {d}, description stripped {s}")
        dropped += d
        stripped += s

    linked = link_history(args.pr, hist, args.dry_run)
    verb = "would" if args.dry_run else ""
    print(
        f"\n{verb} drop {dropped} duplicate-publication records, "
        f"strip {stripped} boilerplate descriptions, link {linked} history records to PR #{args.pr}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
