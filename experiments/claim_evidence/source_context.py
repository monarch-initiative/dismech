"""Paired direct-support experiment, holding the question fixed across both arms.

From repo root:
  uv run python experiments/claim_evidence/source_context.py build RUN_DIRECTORY
  uv run python experiments/claim_evidence/source_context.py run RUN_DIRECTORY
  uv run python experiments/claim_evidence/source_context.py summarize RUN_DIRECTORY
"""

import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from dismech.classifier.direct_support import direct_support_task
from dismech.classifier.typesafe import TypeSafeClassifier
from dismech.reference_snippet_audit import (
    CachedReferenceIndex,
    DEFAULT_CONFIG,
    PairOutcome,
    SnippetPair,
    check_pair,
    load_literal_bracket_patterns,
)

PREVIOUS = Path("experiments/claim_evidence/2026-09-18")


def read(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def build(root):
    index = CachedReferenceIndex(
        Path("references_cache"),
        literal_bracket_patterns=load_literal_bracket_patterns(DEFAULT_CONFIG),
    )
    cases = []
    for old in read(PREVIOUS / "cases.jsonl"):
        item = old["input"]
        if item["supports"] != "SUPPORT" or item["directness"] != "DIRECT":
            continue
        if old["id"] == "dr_laser_persuasive_explanation":
            continue  # Explanation is intentionally absent from this simplified task.
        cases.append(
            {
                "id": old["id"],
                "reference": old["reference"],
                "expected": old["expected"],
                "origin": old["origin"],
                "rationale": old["rationale"],
                "claim": item["claim"]["description"],
                "snippet": item["snippet"],
            }
        )
    comparator = next(row for row in cases if row["id"] == "comparator_nfkbia")
    cropped = comparator["snippet"].split("Infections reported include", 1)[1]
    cropped = "Infections reported include" + cropped
    for gene, expected in [("NFKBIA", "MATCH"), ("IKBKB", "MISMATCH")]:
        cases.append(
            {
                "id": "cropped_" + gene.lower(),
                "reference": comparator["reference"],
                "claim": f"Pneumocystis pneumonitis was reported in patients with {gene} mutations.",
                "snippet": cropped,
                "expected": expected,
                "origin": comparator["origin"],
                "rationale": "The antecedent outside the snippet identifies NFKBIA patients. Snippet-only input cannot distinguish the gene reliably.",
            }
        )
    trec = next(row for row in cases if row["id"] == "ikk_trec_support")
    cases.append(
        {
            "id": "elsewhere_hsct",
            "reference": trec["reference"],
            "claim": "IKBKB deficiency requires hematopoietic stem cell transplantation.",
            "snippet": trec["snippet"],
            "expected": "MISMATCH",
            "origin": "Constructed source-rescue trap using the TREC screening quotation.",
            "rationale": "The paper recommends HSCT elsewhere, but this snippet concerns screening, not treatment.",
        }
    )
    # Two valid treatment assertions resembling false alarms in the first experiment.
    audit = {r["id"]: r for r in read(PREVIOUS / "retinopathy-audit-v2.jsonl")}
    for id, location, claim in [
        (
            "prp_primary",
            "treatments[1].evidence[0]",
            "Panretinal photocoagulation is the primary treatment for proliferative diabetic retinopathy.",
        ),
        (
            "anti_vegf_standard",
            "treatments[0].evidence[1]",
            "Intravitreal anti-VEGF therapy is the standard of care for diabetic macular edema.",
        ),
    ]:
        row = audit[location]
        cases.append(
            {
                "id": id,
                "reference": row["reference"],
                "expected": "MATCH",
                "claim": claim,
                "snippet": row["task"]["state"]["snippet"],
                "origin": row["input_file"] + ":" + location,
                "rationale": "Explicit treatment statement supports this narrowly scoped claim.",
            }
        )
    for row in cases:
        path = index.resolve_cache_path(row["reference"])
        if path is None:
            raise ValueError(f"Missing cached reference: {row['reference']}")
        source = index.extract_body(path.read_text())
        outcome = check_pair(
            index, SnippetPair(path, row["id"], row["reference"], row["snippet"])
        )
        if outcome not in {PairOutcome.VERIFIED, PairOutcome.VERIFIED_RELAXED}:
            raise ValueError(f"Unverified quote: {row['id']}")
        row.update(
            source_text=source,
            source_path=str(path),
            source_content_type=index.content_type(row["reference"]),
            source_sha256=hashlib.sha256(source.encode()).hexdigest(),
            quote_check=outcome.value,
        )
    with (root / "cases.jsonl").open("x") as stream:
        for row in cases:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(
        f"Froze {len(cases)} cases with complete cached source bodies (no truncation)."
    )


def run(root, repeats):
    cases = read(root / "cases.jsonl")
    client = TypeSafeClassifier()
    template = asdict(direct_support_task("placeholder", "placeholder"))
    template.pop("state")
    with (root / "task.json").open("x") as stream:
        json.dump(template, stream, indent=2)
        stream.write("\n")
    errors = 0
    with (root / "results.jsonl").open("x") as stream:
        for repeat in range(repeats):
            for i, case in enumerate(cases):
                arms = ["snippet_only", "with_source"]
                if (repeat + i) % 2:
                    arms.reverse()
                for arm in arms:
                    task = direct_support_task(
                        case["claim"],
                        case["snippet"],
                        case["source_text"] if arm == "with_source" else None,
                    )
                    record = {
                        "id": case["id"],
                        "arm": arm,
                        "repeat": repeat,
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    }
                    try:
                        record["result"] = asdict(client.classify(task))
                    except Exception as exc:
                        record["error"] = type(exc).__name__
                        errors += 1
                    stream.write(json.dumps(record) + "\n")
                    stream.flush()
    print(f"Completed {len(cases) * 2 * repeats} assessments; {errors} errors")
    return bool(errors)


def summarize(root):
    cases = {r["id"]: r for r in read(root / "cases.jsonl")}
    rows = read(root / "results.jsonl")
    for arm in ["snippet_only", "with_source"]:
        selected = [r for r in rows if r["arm"] == arm and "result" in r]
        confusion = Counter(
            cases[r["id"]]["expected"] + " -> " + r["result"]["label"] for r in selected
        )
        print(
            arm,
            json.dumps(dict(confusion)),
            "input tokens",
            sum(r["result"]["usage"]["input_tokens"] for r in selected),
        )
    for id, case in cases.items():
        cells = []
        for arm in ["snippet_only", "with_source"]:
            selected = [
                r["result"]
                for r in rows
                if r["id"] == id and r["arm"] == arm and "result" in r
            ]
            cells.append(
                ", ".join(
                    f"{r['label']} ({r['probabilities']['MATCH']:.2f})"
                    for r in selected
                )
            )
        print(id, case["expected"], " | ".join(cells))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "run", "summarize"])
    parser.add_argument("root", type=Path)
    parser.add_argument("--repeats", type=int, default=3)
    args = parser.parse_args()
    if args.repeats < 1:
        parser.error("--repeats must be positive")
    if args.command == "build":
        build(args.root)
    elif args.command == "run":
        raise SystemExit(run(args.root, args.repeats))
    else:
        summarize(args.root)
