"""Build recuration reports from saved Jev predictions, without API calls."""

import csv
import json
import shutil
from pathlib import Path

import click

from dismech.classifier.claims import resolve

ASPECT_COLUMNS = (
    "file",
    "disease",
    "section",
    "assertion_path",
    "evidence_path",
    "reference",
    "aspect_path",
    "aspect_value",
    "status",
    "label",
    "p_mismatch",
    "p_partial",
    "p_match",
    "confidence",
    "supports",
    "directness",
    "snippet",
    "model",
    "assessed_at",
    "cached",
    "error",
    "http_status",
    "cache_key",
)
ENTRY_COLUMNS = (
    "rank",
    "file",
    "disease",
    "assertions",
    "pairs",
    "assessed_pairs",
    "mismatch_assertions",
    "partial_assertions",
    "mismatch_aspects",
    "partial_aspects",
    "match_aspects",
    "root_mismatch",
    "root_partial",
    "root_match",
    "max_p_mismatch",
    "no_evidence",
    "missing_snippet",
    "invalid_input",
    "api_error",
    "not_assessed",
    "ready",
    "cached_pairs",
)


def write_reports(output, complete=True):
    entries = {}
    totals = {
        "pairs": 0,
        "assessed_pairs": 0,
        "cached_pairs": 0,
        "errors": 0,
        "input_errors": 0,
        "input_tokens": 0,
        "output_tokens": 0,
    }
    with (output / "aspects.csv").open("w", newline="") as detailed:
        writer = csv.DictWriter(
            detailed, fieldnames=ASPECT_COLUMNS, extrasaction="ignore"
        )
        writer.writeheader()
        with (output / "results.jsonl").open() as stream:
            for line in stream:
                row = json.loads(line)
                totals["pairs"] += 1
                entry = entries.setdefault(
                    row["file"],
                    dict.fromkeys(ENTRY_COLUMNS, 0)
                    | {
                        "file": row["file"],
                        "disease": row["disease"],
                        "_assertions": set(),
                        "_mismatch": set(),
                        "_partial": set(),
                    },
                )
                assertion = row["assertion_path"]
                if assertion:
                    entry["_assertions"].add(assertion)
                entry["pairs"] += 1
                status = row["status"]
                if status != "assessed":
                    entry[status] += 1
                    if status == "invalid_input":
                        totals["input_errors"] += 1
                    if status in {"api_error", "not_assessed"}:
                        totals["errors"] += 1
                    writer.writerow(row)
                    continue
                entry["assessed_pairs"] += 1
                totals["assessed_pairs"] += 1
                cached = bool(row.get("cached"))
                entry["cached_pairs"] += int(cached)
                totals["cached_pairs"] += int(cached)
                result = row["result"]
                if not cached:
                    for key in ("input_tokens", "output_tokens"):
                        totals[key] += result.get("usage", {}).get(key, 0)
                for path, answer in result["answers"].items():
                    label = answer["label"].lower()
                    probabilities = answer["probabilities"]
                    entry["max_p_mismatch"] = max(
                        entry["max_p_mismatch"], probabilities["MISMATCH"]
                    )
                    if label in {"mismatch", "partial"}:
                        entry["_" + label].add(assertion)
                    entry[
                        ("root_" + label) if path == "/" else (label + "_aspects")
                    ] += 1
                    claim = row["claim"]
                    value = (
                        {k: claim[k] for k in ("about", "assertion_type", "assertion")}
                        if path == "/"
                        else resolve(claim, path)
                    )
                    writer.writerow(
                        row
                        | {
                            "aspect_path": path,
                            "aspect_value": json.dumps(value, ensure_ascii=False),
                            "label": answer["label"],
                            "confidence": answer["confidence"],
                            "p_mismatch": probabilities["MISMATCH"],
                            "p_partial": probabilities["PARTIAL"],
                            "p_match": probabilities["MATCH"],
                            "model": result["model"],
                        }
                    )
    for entry in entries.values():
        entry["assertions"] = len(entry.pop("_assertions"))
        entry["mismatch_assertions"] = len(entry.pop("_mismatch"))
        entry["partial_assertions"] = len(entry.pop("_partial"))
    ordered = sorted(
        entries.values(),
        key=lambda e: (
            -e["mismatch_assertions"],
            -e["max_p_mismatch"] if e["mismatch_assertions"] else 0,
            -e["partial_assertions"],
            -e["no_evidence"] - e["missing_snippet"],
            e["file"],
        ),
    )
    with (output / "entries.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=ENTRY_COLUMNS)
        writer.writeheader()
        for rank, entry in enumerate(ordered, 1):
            writer.writerow(entry | {"rank": rank})
    totals["entries"] = len(ordered)
    totals["mismatch_assertions"] = sum(e["mismatch_assertions"] for e in ordered)
    totals["complete"] = complete and totals["errors"] == 0
    summary = [
        "# Jev claim/evidence audit",
        "",
        (
            f"{totals['entries']} entries; {totals['pairs']} assertion/evidence pairs; "
            f"{totals['assessed_pairs']} assessed ({totals['cached_pairs']} reused); {totals['errors']} API/unassessed errors; {totals['input_errors']} invalid inputs."
        ),
        "",
        "Model judgments prioritize recuration; they are not curated labels or measures of disease-entry truth.",
        "PARTIAL means incomplete, weak, mixed or uncertain snippet support. Missing evidence and failed requests have no model label.",
        "",
        (
            "Entries are ordered by distinct assertions with a MISMATCH, then maximum mismatch probability, "
            "then distinct assertions with PARTIAL, then missing evidence. Root and non-root counts are separate. "
            "Multiple snippets/aspects cannot inflate the distinct-assertion count; an assertion may appear in both mismatch and partial counts."
        ),
        "",
        "Full reports: `entries.csv`, `aspects.csv`; provenance and exact inputs: `manifest.json`, `results.jsonl`.",
        "",
        "| Entry | Assertions with MISMATCH | Assertions with PARTIAL | Assessed pairs |",
        "| --- | ---: | ---: | ---: |",
    ]
    for entry in ordered[:20]:
        disease = str(entry["disease"]).replace("|", "\\|").replace("\n", " ")
        summary.append(
            f"| {disease} | {entry['mismatch_assertions']} | {entry['partial_assertions']} | {entry['assessed_pairs']} |"
        )
    if not totals["complete"]:
        summary[:0] = [
            "**INCOMPLETE RUN: missing or unfinished work. Counts below cover only available results.**",
            "",
        ]
    (output / "summary.md").write_text("\n".join(summary) + "\n")
    return totals


def merge_shards(output, source, expected):
    """Combine only compatible, distinct partitions; retain partial reports."""
    paths = sorted(source.glob("*/manifest.json"))
    if not paths:
        raise click.ClickException("No shard manifests found")
    manifests = [json.loads(p.read_text()) for p in paths]
    indices = [m["shard_index"] for m in manifests]
    if len(set(indices)) != len(indices):
        raise click.ClickException("Duplicate shard indices")
    first = manifests[0]
    keys = (
        "model",
        "source_revision",
        "schema_sha256",
        "classifier_sha256",
        "shard_count",
        "sections",
        "inputs",
        "limit",
        "dry_run",
        "prompt",
        "criteria",
    )
    if any(any(m[k] != first[k] for k in keys) for m in manifests):
        raise click.ClickException(
            "Cannot combine shards with different sources or inference settings"
        )
    expected = expected or first["shard_count"]
    if first["shard_count"] != expected or any(i < 0 or i >= expected for i in indices):
        raise click.ClickException("Unexpected shard count/index")
    complete = set(indices) == set(range(expected)) and all(
        m["complete"] for m in manifests
    )
    output.mkdir(parents=True, exist_ok=True)
    with (output / "results.jsonl").open("w") as stream:
        for path in paths:
            results = path.with_name("results.jsonl")
            if not results.exists():
                complete = False
                continue
            with results.open() as source_stream:
                shutil.copyfileobj(source_stream, stream)
    metadata = {k: first[k] for k in keys} | {
        "complete": complete,
        "missing_shards": sorted(set(range(expected)) - set(indices)),
        "shards": manifests,
    }
    metadata.update(write_reports(output, complete=complete))
    (output / "manifest.json").write_text(json.dumps(metadata, indent=2) + "\n")
    return metadata["complete"]


@click.command()
@click.argument("output", type=click.Path(file_okay=False, path_type=Path))
@click.option(
    "--merge", "source", type=click.Path(exists=True, file_okay=False, path_type=Path)
)
@click.option("--expected-shards", type=click.IntRange(min=1))
def main(output, source, expected_shards):
    """Regenerate CSVs/summary from OUTPUT/results.jsonl; no API key required."""
    if source:
        if not merge_shards(output, source, expected_shards):
            raise click.ClickException(
                "Wrote partial reports: some shards are missing or incomplete"
            )
    else:
        manifest = output / "manifest.json"
        complete = (
            json.loads(manifest.read_text()).get("complete", False)
            if manifest.exists()
            else True
        )
        write_reports(output, complete=complete)
    click.echo(f"Reports rebuilt in {output}")


if __name__ == "__main__":
    main()
