"""Compare the completed proxy-migration rerun with its preserved baseline."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from enrich_icd10_inputs import tsv
from proxy_merges import REPO, digest

from dismech import kb_cache

COMPLETE = {"ALL_MAPPINGS_CONSISTENT", "RETRACTED"}
FIELDS = (
    "slug",
    "previous_status",
    "status",
    "previous_confidence",
    "confidence",
    "previous_retractions",
    "retractions",
    "changed_choices",
    "input_sha256",
)


def summarize(base):
    migration = json.loads((base / "proxy-merges/updates.json").read_text())
    run = base / "runs/curated-proxy-merges"
    with (run / "attempts.tsv").open() as stream:
        attempts = {r["slug"]: r for r in csv.DictReader(stream, delimiter="\t")}
    if attempts.keys() != migration["inputs"].keys():
        raise ValueError("Rerun cohort is incomplete or differs from the migration")
    retry = base / "runs/curated-proxy-merges-retry/attempts.tsv"
    retry_source = base / "proxy-merges/retry.tsv"
    if retry_source.exists():
        with retry_source.open() as stream:
            expected = {r["slug"] for r in csv.DictReader(stream, delimiter="\t")}
        with retry.open() as stream:
            retried = {r["slug"]: r for r in csv.DictReader(stream, delimiter="\t")}
        if retried.keys() != expected or not expected <= attempts.keys():
            raise ValueError("Retry cohort is incomplete or outside the migration")
        attempts.update(retried)
    rows = []
    for slug, old in migration["inputs"].items():
        folder = base / "disorders" / slug
        input_hash = digest((folder / "kb.yaml").read_bytes())
        attempt = attempts[slug]
        solve = json.loads((folder / "solve.json").read_text())
        if (
            not input_hash
            == old["after_input_sha256"]
            == attempt["input_sha256"]
            == solve["input_sha256"]
        ):
            raise ValueError(f"{slug}: input hashes disagree")
        if solve["status"] != attempt["status"]:
            raise ValueError(f"{slug}: solve status differs from ledger")
        row = {
            "slug": slug,
            "previous_status": old["previous_index"]["status"],
            "status": solve["status"],
            "previous_confidence": "NA",
            "confidence": "NA",
            "previous_retractions": old["previous_index"]["n_retracted"],
            "retractions": solve["n_retracted"],
            "changed_choices": "NA",
            "input_sha256": input_hash,
        }
        if row["previous_status"] in COMPLETE:
            row["previous_confidence"] = old["baseline"]["confidence"]
        if row["status"] in COMPLETE:
            solution = kb_cache.load_document(folder / "solution.yaml")
            assert not solution.get("timed_out")
            row["confidence"] = solution["confidence"]
            if row["previous_status"] in COMPLETE:
                row["changed_choices"] = sum(
                    a != p["truth_value"]
                    for a, p in zip(
                        old["baseline"]["assignment"],
                        solution["solved_pfacts"],
                        strict=True,
                    )
                )
        rows.append(row)
    summary = {
        "cohort": len(rows),
        "previous_statuses": dict(
            sorted(Counter(r["previous_status"] for r in rows).items())
        ),
        "statuses": dict(sorted(Counter(r["status"] for r in rows).items())),
        "completed_confidences": dict(
            sorted(
                Counter(
                    str(r["confidence"]) for r in rows if r["status"] in COMPLETE
                ).items()
            )
        ),
        "completed_comparisons": sum(
            r["previous_status"] in COMPLETE and r["status"] in COMPLETE for r in rows
        ),
        "changed_choices": sum(
            r["changed_choices"] for r in rows if isinstance(r["changed_choices"], int)
        ),
    }
    (run / "comparison.tsv").write_bytes(tsv(rows, FIELDS))
    (run / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


def main():
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=REPO / "analyses/boomer")
    args = parser.parse_args()
    summarize(args.base)


if __name__ == "__main__":
    main()
