"""Measure frame.tsv recall against the committed known_positives.tsv.

Every pair in known_positives.tsv is a test run on an accessible specimen that
is not an inherited-disease genotype, so the frame ought to carry it flagged.

The point of the script is to separate two causes of a miss, because only one
of them is a reason to touch the matcher:

    MATCHER_MISS  the entry records the test but the frame did not flag it
                  -> census.py is wrong
    NOT_RECORDED  no diagnosis[]/biochemical[] row for the test exists
                  -> the dismech entry is incomplete; report it, do not match
                     around it. Subdivided by whether the entry has any rows at
                     all (NO_ROWS_AT_ALL) and whether the test is mentioned in
                     prose (PROSE_ONLY) or absent entirely.

Usage:
    uv run python experiments/diagnostic_retrodiction/check_recall.py
    uv run python experiments/diagnostic_retrodiction/check_recall.py --strict
Exit 0 always, unless --strict, which exits 1 on any MATCHER_MISS. A
NOT_RECORDED pair never fails the check: it is a curation finding, not a
regression in this script.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent


def load_pairs(path: Path) -> list[dict]:
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 3:
            continue
        pairs.append(
            {
                "disease": cols[0].strip(),
                "test": cols[1].strip(),
                "expected": cols[2].strip(),
                "label": cols[3].strip() if len(cols) > 3 else cols[1].strip(),
            }
        )
    return pairs


def row_identity(row: dict) -> str:
    """The text a test_pattern is matched against, for a frame row."""
    return " ".join(
        row.get(k) or ""
        for k in (
            "row_name",
            "diagnosis_term_label",
            "measurements",
            "biomarker_term_label",
            "readouts",
        )
    )


def kb_diagnosis(disease_pattern: str, test_rx: re.Pattern, kb_dir: Path) -> str:
    """Why no frame row matched: does the entry record the test at all?

    Reads the entries whose own ``name`` matches the disease pattern and reports
    whether they carry any diagnosis/biochemical rows, and whether the test is
    mentioned anywhere in the file.
    """
    needle = disease_pattern.lower()
    verdicts = []
    for path in sorted(kb_dir.glob("*.yaml")):
        raw = path.read_text(encoding="utf-8")
        # Cheap pre-filter: parsing all ~4000 entries per miss costs minutes,
        # and an entry whose name matches must contain the pattern verbatim.
        if needle not in raw.lower():
            continue
        try:
            entry = yaml.safe_load(raw)
        except yaml.YAMLError:
            continue
        if not entry or needle not in (entry.get("name") or "").lower():
            continue
        n = len(entry.get("diagnosis") or []) + len(entry.get("biochemical") or [])
        if n == 0:
            verdicts.append(f"NO_ROWS_AT_ALL ({path.name}: 0 diagnosis, 0 biochemical)")
        elif test_rx.search(raw):
            verdicts.append(f"PROSE_ONLY ({path.name}: {n} rows, none for this test)")
        else:
            verdicts.append(f"TEST_ABSENT ({path.name}: {n} rows, test not mentioned)")
    return "; ".join(verdicts) or "NO_SUCH_ENTRY"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frame", type=Path, default=HERE / "frame.tsv")
    ap.add_argument("--positives", type=Path, default=HERE / "known_positives.tsv")
    ap.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    ap.add_argument("--strict", action="store_true", help="exit 1 on any MATCHER_MISS")
    a = ap.parse_args()

    with a.frame.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    pairs = load_pairs(a.positives)

    hits, misses = [], []
    for pair in pairs:
        test_rx = re.compile(pair["test"], re.I)
        candidates = [
            r
            for r in rows
            if pair["disease"].lower() in (r["disease_name"] or "").lower()
            and test_rx.search(row_identity(r))
        ]
        flagged = [r for r in candidates if r["flag_nongenetic_specimen"] == "TRUE"]
        if flagged:
            hits.append((pair, flagged[0]))
        else:
            kind = "MATCHER_MISS" if candidates else "NOT_RECORDED"
            detail = (
                f"row '{candidates[0]['row_name']}' present but not flagged "
                f"(specimen={candidates[0]['specimen_hits'] or '-'}, "
                f"basis={candidates[0]['specimen_basis']}, "
                f"genetic={candidates[0]['is_genetic']}, "
                f"somatic={candidates[0]['somatic_variant']})"
                if candidates
                else kb_diagnosis(pair["disease"], test_rx, a.kb_dir)
            )
            misses.append((pair, kind, detail))

    n = len(pairs)
    print(f"recall: {len(hits)}/{n} = {100 * len(hits) / n:.1f}%\n")
    for pair, row in hits:
        print(
            f"  HIT   {pair['disease']} / {pair['label']}"
            f"  ->  [{row['row_type']}] {row['row_name']}"
            f"  ({row['specimen_hits']}, {row['specimen_basis']}"
            + (f"/{row['implicit_class']}" if row["implicit_class"] else "")
            + ")"
        )
    if misses:
        print()
        for pair, kind, detail in misses:
            print(f"  MISS  {pair['disease']} / {pair['label']}\n          {kind}: {detail}")

    matcher = [m for m in misses if m[1] == "MATCHER_MISS"]
    notrec = [m for m in misses if m[1] == "NOT_RECORDED"]
    print(
        f"\n{len(hits)} flagged, {len(matcher)} matcher miss(es), "
        f"{len(notrec)} not recorded in the KB."
    )
    sys.exit(1 if (a.strict and matcher) else 0)


if __name__ == "__main__":
    main()
