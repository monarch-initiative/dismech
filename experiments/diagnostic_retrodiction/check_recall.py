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
    uv run python experiments/diagnostic_retrodiction/check_recall.py \
        --report experiments/diagnostic_retrodiction/recall_report.tsv
Exit 0 always, unless --strict, which exits 1 on any MATCHER_MISS. A
NOT_RECORDED pair never fails the check: it is a curation finding, not a
regression in this script.

--report freezes the per-pair result as TSV. The frame is already frozen, but
the NOT_RECORDED reason codes are read from live kb/, so without a saved report
the *reasons* drift as those diseases get curated while the frame does not.
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


def kb_diagnosis(disease_pattern: str, test_rx: re.Pattern, kb_dir: Path) -> list[dict]:
    """Why no frame row matched: does the entry record the test at all?

    Reads the entries whose own ``name`` matches the disease pattern and reports
    whether they carry any diagnosis/biochemical rows, and whether the test is
    mentioned anywhere in the file. One dict per matching entry, with a
    ``code`` of NO_ROWS_AT_ALL / PROSE_ONLY / TEST_ABSENT / NO_SUCH_ENTRY.

    This is the one part of the check that reads *live* ``kb/`` rather than the
    frozen frame, so a reason recomputed after someone curates one of these
    diseases can differ from the frozen report while the frame stays fixed.
    That is why --report exists.
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
        n_dx = len(entry.get("diagnosis") or [])
        n_bio = len(entry.get("biochemical") or [])
        if n_dx + n_bio == 0:
            code, detail = "NO_ROWS_AT_ALL", "0 diagnosis, 0 biochemical"
        elif test_rx.search(raw):
            code, detail = (
                "PROSE_ONLY",
                f"{n_dx + n_bio} rows ({n_dx} dx, {n_bio} bio), none for this test",
            )
        else:
            code, detail = (
                "TEST_ABSENT",
                f"{n_dx + n_bio} rows ({n_dx} dx, {n_bio} bio), test not mentioned",
            )
        verdicts.append({"code": code, "file": path.name, "detail": detail})
    return verdicts or [
        {"code": "NO_SUCH_ENTRY", "file": "", "detail": "no entry name matches the pattern"}
    ]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frame", type=Path, default=HERE / "frame.tsv")
    ap.add_argument("--positives", type=Path, default=HERE / "known_positives.tsv")
    ap.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    ap.add_argument("--strict", action="store_true", help="exit 1 on any MATCHER_MISS")
    ap.add_argument(
        "--report",
        type=Path,
        default=None,
        help="also write the full per-pair report as TSV (one row per pair)",
    )
    a = ap.parse_args()

    with a.frame.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    pairs = load_pairs(a.positives)

    results = []
    for pair in pairs:
        test_rx = re.compile(pair["test"], re.I)
        candidates = [
            r
            for r in rows
            if pair["disease"].lower() in (r["disease_name"] or "").lower()
            and test_rx.search(row_identity(r))
        ]
        flagged = [r for r in candidates if r["flag_nongenetic_specimen"] == "TRUE"]
        res = {
            "disease_pattern": pair["disease"],
            "test_label": pair["label"],
            "test_pattern": pair["test"],
            "expected_specimen": pair["expected"],
            "outcome": "HIT" if flagged else "MISS",
            "miss_kind": "",
            "reason_code": "",
            "reason_detail": "",
            "matched_disease": "",
            "matched_row_type": "",
            "matched_row_name": "",
            "specimen_hits": "",
            "specimen_basis": "",
            "implicit_class": "",
            "is_genetic": "",
            "somatic_variant": "",
        }
        if flagged:
            row = flagged[0]
            res.update(
                matched_disease=row["disease_name"],
                matched_row_type=row["row_type"],
                matched_row_name=row["row_name"],
                specimen_hits=row["specimen_hits"],
                specimen_basis=row["specimen_basis"],
                implicit_class=row["implicit_class"],
                is_genetic=row["is_genetic"],
                somatic_variant=row["somatic_variant"],
            )
        elif candidates:
            row = candidates[0]
            res.update(
                miss_kind="MATCHER_MISS",
                reason_code="ROW_PRESENT_NOT_FLAGGED",
                reason_detail=f"row '{row['row_name']}' present in the frame but not flagged",
                matched_disease=row["disease_name"],
                matched_row_type=row["row_type"],
                matched_row_name=row["row_name"],
                specimen_hits=row["specimen_hits"],
                specimen_basis=row["specimen_basis"],
                implicit_class=row["implicit_class"],
                is_genetic=row["is_genetic"],
                somatic_variant=row["somatic_variant"],
            )
        else:
            verdicts = kb_diagnosis(pair["disease"], test_rx, a.kb_dir)
            res.update(
                miss_kind="NOT_RECORDED",
                reason_code=";".join(v["code"] for v in verdicts),
                reason_detail="; ".join(
                    f"{v['file']}: {v['detail']}" if v["file"] else v["detail"]
                    for v in verdicts
                ),
            )
        results.append(res)

    hits = [r for r in results if r["outcome"] == "HIT"]
    misses = [r for r in results if r["outcome"] == "MISS"]
    n = len(results)
    print(f"recall: {len(hits)}/{n} = {100 * len(hits) / n:.1f}%\n")
    for r in hits:
        print(
            f"  HIT   {r['disease_pattern']} / {r['test_label']}"
            f"  ->  [{r['matched_row_type']}] {r['matched_row_name']}"
            f"  ({r['specimen_hits']}, {r['specimen_basis']}"
            + (f"/{r['implicit_class']}" if r["implicit_class"] else "")
            + ")"
        )
    if misses:
        print()
        for r in misses:
            print(
                f"  MISS  {r['disease_pattern']} / {r['test_label']}\n"
                f"          {r['miss_kind']}: {r['reason_code']} ({r['reason_detail']})"
            )

    matcher = [r for r in misses if r["miss_kind"] == "MATCHER_MISS"]
    notrec = [r for r in misses if r["miss_kind"] == "NOT_RECORDED"]
    print(
        f"\n{len(hits)} flagged, {len(matcher)} matcher miss(es), "
        f"{len(notrec)} not recorded in the KB."
    )

    if a.report:
        write_report(a.report, results, a, len(rows))
        print(f"\nwrote {len(results)} pair rows to {a.report}")

    sys.exit(1 if (a.strict and matcher) else 0)


REPORT_FIELDS = [
    "disease_pattern",
    "test_label",
    "test_pattern",
    "expected_specimen",
    "outcome",
    "miss_kind",
    "reason_code",
    "reason_detail",
    "matched_disease",
    "matched_row_type",
    "matched_row_name",
    "specimen_hits",
    "specimen_basis",
    "implicit_class",
    "is_genetic",
    "somatic_variant",
]


def write_report(path: Path, results: list[dict], args, frame_rows: int) -> None:
    """Freeze the per-pair report, with the provenance needed to read it later.

    The header records the pinned commit and the frame it was computed against,
    because the NOT_RECORDED reasons are read from live kb/ and will drift as
    those diseases get curated. This file is the reason as of the pin.
    """
    hits = sum(1 for r in results if r["outcome"] == "HIT")
    pinned = (HERE / "PINNED_COMMIT").read_text(encoding="utf-8").strip()
    lines = [
        "# Frozen per-pair recall report for the diagnostic-retrodiction sampling frame.",
        "#",
        f"# pinned_commit  {pinned}",
        f"# frame          {args.frame.name} ({frame_rows} rows)",
        f"# positives      {args.positives.name} ({len(results)} pairs)",
        f"# recall         {hits}/{len(results)} = {100 * hits / len(results):.1f}%",
        "#",
        "# outcome      HIT | MISS",
        "# miss_kind    MATCHER_MISS (the frame carries the row but did not flag it;",
        "#              a census.py defect) | NOT_RECORDED (no diagnosis[]/biochemical[]",
        "#              row for the test exists; a curation gap, not a matcher defect)",
        "# reason_code  ROW_PRESENT_NOT_FLAGGED | NO_ROWS_AT_ALL | PROSE_ONLY |",
        "#              TEST_ABSENT | NO_SUCH_ENTRY",
        "#",
        "# The NOT_RECORDED reason codes are read from live kb/ at the time of the run,",
        "# so they are frozen here deliberately: recomputing them after one of these",
        "# diseases is curated will give a different answer for the same frozen frame.",
        "#",
        "\t".join(REPORT_FIELDS),
    ]
    lines += ["\t".join(str(r[f]) for f in REPORT_FIELDS) for r in results]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
