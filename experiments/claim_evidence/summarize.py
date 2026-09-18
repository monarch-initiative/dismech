"""Recompute smoke-test agreement and audit counts from saved service responses."""

import argparse
from collections import Counter
import json
from pathlib import Path


def read(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def summarize(root):
    cases = {row["id"]: row for row in read(root / "cases.jsonl")}
    summaries = {}
    for path in sorted(root.glob("*.jsonl")):
        if path.name == "cases.jsonl":
            continue
        rows = read(path)
        good = [r for r in rows if "result" in r]
        counts = Counter(r["result"]["label"] for r in good)
        summary = {
            "items": len(rows),
            "errors": len(rows) - len(good),
            "labels": dict(counts),
            "models": sorted({r["result"]["model"] for r in good}),
            "input_tokens": sum(r["result"]["usage"]["input_tokens"] for r in good),
            "elapsed_seconds": round(
                sum(r["result"]["elapsed_seconds"] for r in good), 3
            ),
        }
        if path.name.startswith("results"):
            summary["correct"] = sum(
                cases[r["id"]]["expected"] == r["result"]["label"] for r in good
            )
            summary["confusion"] = dict(
                Counter(
                    cases[r["id"]]["expected"] + " -> " + r["result"]["label"]
                    for r in good
                )
            )
            summary["disagreements"] = [
                r["id"]
                for r in good
                if cases[r["id"]]["expected"] != r["result"]["label"]
            ]
        summaries[path.name] = summary
    return summaries


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run", type=Path)
    args = parser.parse_args()
    print(json.dumps(summarize(args.run), indent=2))
