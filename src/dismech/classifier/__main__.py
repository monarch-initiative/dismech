"""JSONL evidence audit: python -m dismech.classifier INPUT --output OUTPUT."""

import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import json
from pathlib import Path

from dismech.classifier.evidence import EvidenceInput, evidence_task, iter_evidence
from dismech.classifier.typesafe import TypeSafeClassifier
from dismech.yaml_io import safe_load_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", type=Path, help="JSONL cases, or a KB YAML file with --kb"
    )
    parser.add_argument(
        "--kb", action="store_true", help="Extract evidence from KB YAML"
    )
    parser.add_argument(
        "--output", type=Path, required=True, help="New JSONL report; never overwritten"
    )
    parser.add_argument("--model", default="jev-1.13.0")
    parser.add_argument(
        "--limit", type=int, default=20, help="Maximum evidence items (default 20)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Write tasks without API calls"
    )
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    if args.kb:
        cases = list(iter_evidence(safe_load_path(args.input)))[: args.limit]
    else:
        cases = [
            json.loads(line)
            for line in args.input.read_text().splitlines()
            if line.strip()
        ][: args.limit]
    # Validate all selected inputs before making paid requests.
    tasks = [evidence_task(EvidenceInput(**case["input"])) for case in cases]
    classifier = None if args.dry_run else TypeSafeClassifier(args.model)
    errors = 0
    with args.output.open("x") as stream:
        for case, task in zip(cases, tasks, strict=True):
            record = {
                "id": case["id"],
                "reference": case.get("reference"),
                "input_file": str(args.input),
                "task": asdict(task),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
            if classifier:
                try:
                    record["result"] = asdict(classifier.classify(task))
                except Exception as exc:
                    # Never confuse transport/parsing failure with a scientific verdict.
                    record["error"] = type(exc).__name__
                    errors += 1
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            stream.flush()
    print(
        f"Wrote {len(cases)} {'tasks' if args.dry_run else 'assessments'} to {args.output}; {errors} errors"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
