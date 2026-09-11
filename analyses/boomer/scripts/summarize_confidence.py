"""Compare a named rerun with its saved baseline, including mapping posteriors."""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
from statistics import median

from dismech import kb_cache
from solve_pending import REPO, atomic_text, sha, table


def describe(values):
    return (
        {
            "n": len(values),
            "min": min(values),
            "median": median(values),
            "max": max(values),
        }
        if values
        else {"n": 0}
    )


def summarize(base, run_name):
    run = base / "runs" / run_name
    baseline = json.loads((run / "baseline.json").read_text())["entries"]
    manifest = json.loads((run / "manifest.json").read_text())
    with (run / "attempts.tsv").open() as stream:
        attempts = list(csv.DictReader(stream, delimiter="\t"))
    if {r["slug"] for r in attempts} != set(baseline):
        raise ValueError("Rerun is incomplete or differs from its baseline cohort")
    comparisons, mappings = [], []
    for row in sorted(attempts, key=lambda r: r["slug"]):
        slug = row["slug"]
        old = baseline[slug]
        folder = base / "disorders" / slug
        metadata = json.loads((folder / "solve.json").read_text())
        if (
            metadata["boomer_commit"] != manifest["boomer_commit"]
            or metadata["status"] != row["status"]
        ):
            raise ValueError(f"Saved result no longer belongs to this run: {slug}")
        if sha((folder / "kb.yaml").read_bytes()) != old["input_sha256"]:
            raise ValueError(f"Changed input: {slug}")
        if not metadata["solution_written"]:
            raise ValueError(f"No current result to summarize: {slug}")
        solution = kb_cache.load_document(folder / "solution.yaml")
        kb = kb_cache.load_document(folder / "kb.yaml")
        comparisons.append(
            dict(
                slug=slug,
                status=row["status"],
                previous_status=old["status"],
                previous_confidence=old["confidence"],
                confidence=solution["confidence"],
                previous_posterior=old["posterior_prob"],
                posterior=solution["posterior_prob"],
                previous_satisfiable_count=old["number_of_satisfiable_combinations"],
                distinct_solutions=solution["number_of_satisfiable_combinations"],
                assignment_changed=old["accepted"]
                != [f["truth_value"] for f in solution["solved_pfacts"]],
            )
        )
        for f in solution["solved_pfacts"]:
            fact = f["pfact"]["fact"]
            subject = fact["sub"]
            obj = fact.get("equivalent", fact.get("sup"))
            mappings.append(
                dict(
                    slug=slug,
                    status=row["status"],
                    subject=subject,
                    subject_label=kb.get("labels", {}).get(subject, subject),
                    relation=fact["fact_type"],
                    object=obj,
                    object_label=kb.get("labels", {}).get(obj, obj),
                    prior=f["pfact"]["prob"],
                    accepted=f["truth_value"],
                    posterior=f["posterior_prob"],
                )
            )
    summary = {
        "boomer_commit": manifest["boomer_commit"],
        "n": len(comparisons),
        "status_counts": dict(Counter(r["status"] for r in comparisons)),
        "status_changes": sum(r["status"] != r["previous_status"] for r in comparisons),
        "assignment_changes": sum(r["assignment_changed"] for r in comparisons),
        "confidence_counts": dict(Counter(str(r["confidence"]) for r in comparisons)),
        "by_status": {},
    }
    for status in sorted(summary["status_counts"]):
        rows = [r for r in comparisons if r["status"] == status]
        summary["by_status"][status] = {
            "confidence": describe([r["confidence"] for r in rows]),
            "posterior": describe([r["posterior"] for r in rows]),
            "accepted_mapping_posterior": describe(
                [
                    f["posterior"]
                    for f in mappings
                    if f["status"] == status and f["accepted"]
                ]
            ),
            "rejected_high_prior_posterior": describe(
                [
                    f["posterior"]
                    for f in mappings
                    if f["status"] == status
                    and f["accepted"] is False
                    and f["prior"] >= 0.5
                ]
            ),
        }
    atomic_text(run / "confidence.tsv", table(comparisons, tuple(comparisons[0])))
    atomic_text(run / "mapping-posteriors.tsv", table(mappings, tuple(mappings[0])))
    atomic_text(run / "summary.json", json.dumps(summary, indent=2) + "\n")
    return summary


def main():
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=REPO / "analyses/boomer")
    parser.add_argument("--run-name", default="unique-solutions-completed")
    args = parser.parse_args()
    print(json.dumps(summarize(args.base, args.run_name), indent=2))


if __name__ == "__main__":
    main()
