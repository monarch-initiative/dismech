"""Validate and query the standalone ontology change proposal registry.

This module never edits an ontology or publishes a ticket. Run ``validate``
before exporting a reviewable request. All checks are offline.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path

import yaml
from jsonschema import Draft7Validator, FormatChecker
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from dismech.repo_root import repo_root
from dismech.yaml_io import find_duplicate_keys, safe_load

SCHEMA = Path(__file__).parent / "schema" / "ontology_change.yaml"
REGISTRY = "ontology_changes"
CURIE = re.compile(r"^\S+:\S+$")
MONDO_QUALIFIERS = {
    "MONDO:equivalentTo",
    "MONDO:mondoIsNarrowerThanSource",
    "MONDO:mondoIsBroaderThanSource",
    "MONDO:relatedTo",
}
TYPE_FIELDS = {
    "MAPPING_PREDICATE_CHANGE": {
        "mapping_target",
        "mapping_representation",
        "old_value",
        "new_value",
    },
    "REMOVE_MAPPING": {"mapping_target", "mapping_representation", "old_value"},
    "NODE_RENAME": {"old_value", "new_value"},
    "NODE_TEXT_DEFINITION_CHANGE": {"old_value", "new_value"},
    "EDGE_CREATION": {"edge_object", "predicate"},
    "EDGE_DELETION": {"edge_object", "predicate"},
}
EDIT_FIELDS = set().union(*TYPE_FIELDS.values())


def _json_default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    raise TypeError(f"Not JSON serializable: {type(value).__name__}")


@lru_cache(maxsize=1)
def schema_validator() -> Draft7Validator:
    schema = json.loads(
        JsonSchemaGenerator(
            str(SCHEMA), not_closed=False, include_null=False
        ).serialize()
    )
    return Draft7Validator(schema, format_checker=FormatChecker())


def _local_file(root: Path, name: str) -> Path | None:
    """Only existing files within the repository are valid local references."""
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        return None
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        return None
    return resolved


def _blank_strings(value, location="") -> list[str]:
    if isinstance(value, str):
        return [f"{location}: empty string"] if not value.strip() else []
    if isinstance(value, dict):
        return [
            e for k, v in value.items() for e in _blank_strings(v, f"{location}/{k}")
        ]
    if isinstance(value, list):
        return [
            e for i, v in enumerate(value) for e in _blank_strings(v, f"{location}/{i}")
        ]
    return []


def _text_values(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _text_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from _text_values(item)


def _contains_quote(path: Path, quote: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() != ".json":
        return quote in text
    try:
        return any(quote in value for value in _text_values(json.loads(text)))
    except ValueError:
        return False


def validate_record(record: dict, root: Path | None = None) -> list[str]:
    """Check schema, edit identity, lifecycle, evidence and local artifact integrity."""
    root = root if root is not None else repo_root()
    data = json.loads(json.dumps(record, default=_json_default))
    errors = [
        f"{'/'.join(map(str, e.path))}: {e.message}"
        for e in schema_validator().iter_errors(data)
    ]
    if errors:
        return errors
    errors.extend(_blank_strings(data))
    required = TYPE_FIELDS[data["change_type"]]
    for field in required - data.keys():
        errors.append(f"{data['change_type']} requires {field}")
    for field in (EDIT_FIELDS - required) & data.keys():
        errors.append(f"{data['change_type']} does not use {field}")
    if "new_value" in data and data.get("old_value") == data["new_value"]:
        errors.append("old_value and new_value must differ")
    if data["change_type"] in {"MAPPING_PREDICATE_CHANGE", "REMOVE_MAPPING"}:
        for field in ("old_value", "new_value"):
            if field in data and not CURIE.fullmatch(data[field]):
                errors.append(f"{field} must be a predicate or qualifier CURIE")
        if data.get("mapping_representation") == "MONDO_XREF_QUALIFIER":
            if data["ontology"] != "MONDO" or not data["about_node"]["id"].startswith(
                "MONDO:"
            ):
                errors.append(
                    "MONDO_XREF_QUALIFIER requires a MONDO ontology and about_node"
                )
            for field in ("old_value", "new_value"):
                if field in data and data[field] not in MONDO_QUALIFIERS:
                    errors.append(f"{field} must be a supported MONDO xref qualifier")

    origin = data["origin"]
    status = data.get("request_status")
    upstream_link = data.get("upstream_tracker_issue") or data.get("pull_request")
    if origin == "SELF_PROPOSED":
        for field in ("confidence", "request_status"):
            if field not in data:
                errors.append(f"SELF_PROPOSED requires {field}")
        if "stance" in data:
            errors.append("stance applies only to upstream-originated changes")
        if status == "NOT_FILED" and upstream_link:
            errors.append(
                "NOT_FILED must not claim an upstream ticket or PR; use see_also for context"
            )
        if status and status != "NOT_FILED" and not upstream_link:
            errors.append(f"{status} requires an upstream ticket or PR")
    else:
        for field in ("confidence", "request_status"):
            if field in data:
                errors.append(f"{field} applies only to SELF_PROPOSED")
        if not upstream_link:
            errors.append(
                "upstream-originated changes require an upstream ticket or PR"
            )

    snapshots = {s["id"]: s for s in data["source_snapshots"]}
    if len(snapshots) != len(data["source_snapshots"]):
        errors.append("source_snapshots ids must be unique")
    if not any(
        s["resource"] == data["ontology"]
        and s["checked_at"] == data["ontology_state_verified"]
        for s in snapshots.values()
    ):
        errors.append(
            "ontology_state_verified must match a snapshot of the owning ontology"
        )
    for evidence in data["evidence"]:
        if evidence["source"] not in snapshots:
            errors.append(f"unknown evidence source: {evidence['source']}")
        else:
            path = _local_file(root, snapshots[evidence["source"]]["artifact"]["path"])
            if path is None:
                errors.append(
                    f"cannot verify supporting_text: artifact missing for {evidence['source']}"
                )
            elif not _contains_quote(path, evidence["supporting_text"]):
                errors.append(
                    f"supporting_text not found in source: {evidence['source']}"
                )
    today = date.today().isoformat()
    for snapshot in snapshots.values():
        if snapshot["checked_at"] > today:
            errors.append("snapshot checked_at must not be in the future")
    for name in data.get("affected_records", []):
        if _local_file(root, name) is None:
            errors.append(f"affected record missing or outside repository: {name}")
    artifacts = [s["artifact"] for s in snapshots.values()] + data.get(
        "analysis_artifacts", []
    )
    for artifact in artifacts:
        path = _local_file(root, artifact["path"])
        if path is None:
            errors.append(f"artifact missing or outside repository: {artifact['path']}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            errors.append(f"artifact checksum mismatch: {artifact['path']}")
    return errors


def load_registry(root: Path | None = None) -> tuple[list[dict], list[str]]:
    """Read every proposal; reject duplicate keys, IDs and misleading filenames."""
    root = root if root is not None else repo_root()
    records, errors, seen = [], [], set()
    paths = sorted((root / REGISTRY).glob("*.yaml"))
    if not paths:
        return [], [f"No proposals found under {root / REGISTRY}"]
    for path in paths:
        try:
            text = path.read_text()
            duplicates = find_duplicate_keys(text)
            if duplicates:
                errors.append(f"{path.name}: duplicate YAML keys: {duplicates}")
                continue
            record = safe_load(text)
            problems = validate_record(record, root)
            if problems:
                errors.extend(f"{path.name}: {error}" for error in problems)
                continue
            key = record["id"]
            if key != path.stem:
                errors.append(f"{path.name}: id must match filename stem")
            if key in seen:
                errors.append(f"{path.name}: duplicate proposal id {key}")
            seen.add(key)
            records.append(record)
        except (OSError, ValueError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{path.name}: {error}")
    return records, errors


def render_request(record: dict) -> str:
    """Render all proposal fields for review, with no publishing side effects."""
    return (
        f"# {record['title']}\n\n{record['justification'].strip()}\n\n"
        "## Structured proposal\n\n"
        "This record describes a proposed edit, not an executable patch. "
        "Check the source version and current upstream state before applying it.\n\n"
        "```yaml\n"
        + yaml.safe_dump(record, sort_keys=False, allow_unicode=True)
        + "```\n"
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, help="Checkout override; otherwise use repo_root()"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    listing = sub.add_parser("list")
    listing.add_argument("--ontology")
    listing.add_argument("--request-status")
    listing.add_argument("--affected-record")
    export = sub.add_parser("export")
    export.add_argument("id")
    args = parser.parse_args(argv)
    records, errors = load_registry(args.root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.command == "validate":
        print(f"Validated {len(records)} ontology change proposal(s)")
    elif args.command == "list":
        selected = [
            r
            for r in records
            if (not args.ontology or r["ontology"] == args.ontology)
            and (
                not args.request_status
                or r.get("request_status") == args.request_status
            )
            and (
                not args.affected_record
                or args.affected_record in r.get("affected_records", [])
            )
        ]
        print(json.dumps(selected, indent=2, default=_json_default))
    else:
        record = next((r for r in records if r["id"] == args.id), None)
        if record is None:
            print(f"Unknown proposal: {args.id}", file=sys.stderr)
            return 1
        print(render_request(record), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
