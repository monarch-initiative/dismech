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
from urllib.parse import quote

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
    "MAPPING_CREATION": {"mapping_target", "mapping_representation", "new_value"},
    "NODE_RENAME": {"old_value", "new_value"},
    "NODE_TEXT_DEFINITION_CHANGE": {"old_value", "new_value"},
    "EDGE_CREATION": {"edge_object", "predicate"},
    "EDGE_DELETION": {"edge_object", "predicate"},
}
EDIT_FIELDS = set().union(*TYPE_FIELDS.values())
REVIEW_FIELDS = {
    "analysis_links",
    "source_links",
    "upstream_requests",
    "member_statuses",
    "affected_records",
    "see_also",
}
REPO_BLOB = "https://github.com/monarch-initiative/dismech/blob/main/"


def _json_default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    raise TypeError(f"Not JSON serializable: {type(value).__name__}")


@lru_cache(maxsize=3)
def schema_validator(top_class: str = "OntologyChangeProposal") -> Draft7Validator:
    schema = json.loads(
        JsonSchemaGenerator(
            str(SCHEMA), top_class=top_class, not_closed=False, include_null=False
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
    if "mapping_target" in required:
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


MAPPING_EDIT_TYPES = {"REMOVE_MAPPING", "MAPPING_CREATION", "MAPPING_PREDICATE_CHANGE"}


def change_ids(record: dict) -> list[str]:
    """Read modern membership or the legacy pair, after schema validation."""
    return (
        record["changes"]
        if "changes" in record
        else [record["removal"], record["creation"]]
    )


def mapping_set_view(
    members: list[dict], *, review_context=False, change_set_id=None
) -> dict:
    """Materialize the mapping delta and context from validated atomic proposals."""

    def assertion(member, field):
        return {
            "subject": member["about_node"],
            "predicate": member[field],
            "object": member["mapping_target"],
        }

    view = {
        "ontology": members[0]["ontology"],
        "mapping_representation": members[0]["mapping_representation"],
        "before": [
            assertion(member, "old_value")
            for member in members
            if "old_value" in member
        ],
        "after": [
            assertion(member, "new_value")
            for member in members
            if "new_value" in member
        ],
    }
    if review_context:
        self_url = REPO_BLOB + f"ontology_changes/change_sets/{change_set_id}.yaml"

        def unique(values):
            return list(dict.fromkeys(values))

        view.update(
            analysis_links=unique(
                REPO_BLOB + quote(a["path"], safe="/")
                for member in members
                for a in member.get("analysis_artifacts", [])
            ),
            source_links=unique(
                s["url"] for member in members for s in member["source_snapshots"]
            ),
            upstream_requests=unique(
                member[key]
                for member in members
                for key in ("upstream_tracker_issue", "pull_request")
                if key in member
            ),
            member_statuses=[
                {
                    "proposal_id": member["id"],
                    "record_url": REPO_BLOB + f"ontology_changes/{member['id']}.yaml",
                    **{
                        key: member[key]
                        for key in (
                            "origin",
                            "confidence",
                            "stance",
                            "request_status",
                            "adoption_status",
                            "adoption_notes",
                            "ontology_state_verified",
                        )
                        if key in member
                    },
                }
                for member in members
            ],
            affected_records=unique(
                path
                for member in members
                for path in member.get("affected_records", [])
            ),
            see_also=unique(
                url
                for member in members
                for url in member.get("see_also", [])
                if url != self_url
            ),
        )
    return json.loads(json.dumps(view, default=_json_default))


def _has_review_context(record):
    return bool((REVIEW_FIELDS | {"justification"}) & record.keys())


def mapping_move_view(
    removal: dict, creation: dict, *, review_context=False, change_set_id=None
) -> dict:
    """Compatibility view for legacy single-assertion move records."""
    view = mapping_set_view(
        [removal, creation], review_context=review_context, change_set_id=change_set_id
    )
    view["before"], view["after"] = view["before"][0], view["after"][0]
    return view


def _refresh_move_view(record, proposals):
    """Refresh views and migrate legacy moves, leaving invalid membership untouched."""
    if not isinstance(record, dict):
        return record
    legacy = "changes" not in record
    if legacy:
        ids = [record.get("removal"), record.get("creation")]
    else:
        if "removal" in record or "creation" in record:
            return record  # Mixed representations must fail, not be silently repaired.
        ids = record["changes"]
    if (
        not isinstance(ids, list)
        or not ids
        or not all(isinstance(key, str) for key in ids)
    ):
        return record
    members = [proposals.get(key) for key in ids]
    if any(
        member is None or member["change_type"] not in MAPPING_EDIT_TYPES
        for member in members
    ):
        return record
    if legacy and (
        record.get("change_set_type") != "MAPPING_MOVE"
        or [m["change_type"] for m in members] != ["REMOVE_MAPPING", "MAPPING_CREATION"]
    ):
        return record
    refreshed = {
        **record,
        "changes": ids,
        **mapping_set_view(
            members,
            review_context=_has_review_context(record),
            change_set_id=record.get("id"),
        ),
    }
    if legacy:
        refreshed.pop("removal")
        refreshed.pop("creation")
    return refreshed


def validate_change_set(record: dict, proposals: dict[str, dict]) -> list[str]:
    """Validate a simultaneous mapping delta, including the legacy move format."""
    record = json.loads(json.dumps(record, default=_json_default))
    legacy = isinstance(record, dict) and "changes" not in record
    top_class = "LegacyMappingMove" if legacy else "OntologyChangeSet"
    errors = [
        f"{'/'.join(map(str, e.path))}: {e.message}"
        for e in schema_validator(top_class).iter_errors(record)
    ]
    if errors:
        return errors
    errors.extend(_blank_strings(record))
    ids = change_ids(record)
    if len(ids) != len(set(ids)):
        errors.append("changes must contain unique proposal IDs")
    for key in ids:
        member = proposals.get(key)
        if member is None:
            errors.append(f"unknown or invalid proposal {key}")
        elif member["change_type"] not in MAPPING_EDIT_TYPES:
            errors.append(
                f"{key}: change sets require mapping edits, not {member['change_type']}"
            )
    if legacy:
        if record["change_set_type"] != "MAPPING_MOVE":
            errors.append("MAPPING_RESTRUCTURE requires changes and assertion lists")
        for role, kind in (
            ("removal", "REMOVE_MAPPING"),
            ("creation", "MAPPING_CREATION"),
        ):
            member = proposals.get(record[role])
            if member is not None and member["change_type"] != kind:
                errors.append(f"{role} must reference a {kind} proposal")
    if errors:
        return errors
    members = [proposals[key] for key in ids]
    for field in ("ontology", "mapping_representation"):
        if any(member[field] != members[0][field] for member in members):
            errors.append(f"change set must retain {field}")
    if record["change_set_type"] == "MAPPING_MOVE":
        removals = [m for m in members if m["change_type"] == "REMOVE_MAPPING"]
        creations = [m for m in members if m["change_type"] == "MAPPING_CREATION"]
        if len(members) != 2 or len(removals) != 1 or len(creations) != 1:
            errors.append("MAPPING_MOVE requires exactly one removal and one creation")
        else:
            removal, creation = removals[0], creations[0]
            if removal["mapping_target"]["id"] != creation["mapping_target"]["id"]:
                errors.append("MAPPING_MOVE must retain mapping_target")
            if removal["old_value"] != creation["new_value"]:
                errors.append("MAPPING_MOVE must retain predicate/qualifier")
            if removal["about_node"]["id"] == creation["about_node"]["id"]:
                errors.append("MAPPING_MOVE requires distinct old and new subjects")
    review_context = _has_review_context(record)
    if review_context and not record.get("justification"):
        errors.append(
            "review context requires a curated justification; refresh cannot invent one"
        )
    expected = mapping_set_view(
        members, review_context=review_context, change_set_id=record["id"]
    )
    keys = {}
    for side in ("before", "after"):
        triples = [
            (a["subject"]["id"], a["predicate"], a["object"]["id"])
            for a in expected[side]
        ]
        keys[side] = set(triples)
        if len(triples) != len(keys[side]):
            errors.append(f"duplicate {side} assertion across member proposals")
    if keys["before"] & keys["after"]:
        errors.append(
            "the same assertion is both removed and added; a change set is not an ordered edit sequence"
        )
    if legacy:
        expected["before"], expected["after"] = (
            expected["before"][0],
            expected["after"][0],
        )
    for field, value in expected.items():
        if field not in record or record[field] != value:
            errors.append(
                f"{field} disagrees with member proposals; run refresh-change-set-views"
            )
    return errors


def _read_records(paths, validate, seen, transform=None):
    records, errors = [], []
    for path in paths:
        try:
            text = path.read_text()
            duplicates = find_duplicate_keys(text)
            if duplicates:
                errors.append(f"{path.name}: duplicate YAML keys: {duplicates}")
                continue
            record = safe_load(text)
            if transform is not None:
                record = transform(record)
            problems = validate(record)
            if problems:
                errors.extend(f"{path.name}: {error}" for error in problems)
                continue
            key = record["id"]
            if key != path.stem:
                errors.append(f"{path.name}: id must match filename stem")
            if key in seen:
                errors.append(f"{path.name}: duplicate proposal or change-set id {key}")
            seen.add(key)
            records.append(record)
        except (OSError, ValueError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{path.name}: {error}")
    return records, errors


def load_registry_bundle(
    root: Path | None = None,
    *,
    refresh_views: bool = False,
) -> tuple[list[dict], list[dict], list[str]]:
    """Load proposals and optional change sets, checking all cross-record links."""
    root = root if root is not None else repo_root()
    paths = sorted((root / REGISTRY).glob("*.yaml"))
    if not paths:
        return [], [], [f"No proposals found under {root / REGISTRY}"]
    seen = set()
    records, errors = _read_records(paths, lambda r: validate_record(r, root), seen)
    by_id = {r["id"]: r for r in records}
    change_sets, set_errors = _read_records(
        sorted((root / REGISTRY / "change_sets").glob("*.yaml")),
        lambda r: validate_change_set(r, by_id),
        seen,
        transform=(lambda r: _refresh_move_view(r, by_id)) if refresh_views else None,
    )
    errors.extend(set_errors)
    memberships = {}
    for change_set in change_sets:
        for member in change_ids(change_set):
            if member in memberships:
                errors.append(
                    f"{member} belongs to multiple change sets: {memberships[member]}, {change_set['id']}"
                )
            memberships[member] = change_set["id"]
    return records, change_sets, errors


def load_registry(root: Path | None = None) -> tuple[list[dict], list[str]]:
    """Load atomic proposals, also rejecting invalid change sets when present."""
    records, _, errors = load_registry_bundle(root)
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


def render_change_set(change_set: dict, proposals: dict[str, dict]) -> str:
    """Show every edit and its independent lifecycle without inventing pairwise alignment."""
    members = [proposals[key] for key in change_ids(change_set)]

    def term(value):
        return f"{value['label']} ({value['id']})".replace("|", "\\|").replace(
            "\n", " "
        )

    lines = [
        f"# {change_set['title']}",
        "",
        *(
            [change_set["justification"].strip(), ""]
            if "justification" in change_set
            else []
        ),
        "Review all edits together. Member statuses below are independent; this is not an executable transaction.",
        "",
        "| Edit | Mapping | Before | After |",
        "|---|---|---|---|",
        *[
            f"| {member['change_type']} | {term(member['about_node'])} → {term(member['mapping_target'])} | "
            + (
                f"`{member['old_value']}`"
                if "old_value" in member
                else "Mapping absent"
            )
            + " | "
            + (
                f"`{member['new_value']}`"
                if "new_value" in member
                else "Mapping absent"
            )
            + " |"
            for member in members
        ],
        "",
        "## Structured change set",
        "",
        "```yaml",
        yaml.safe_dump(change_set, sort_keys=False, allow_unicode=True).rstrip(),
        "```",
        "",
    ]
    for member in members:
        lines.extend(
            [
                f"## {member['change_type']}: {member['id']}",
                "",
                f"Origin: {member['origin']}; request: {member.get('request_status', 'not applicable to upstream-originated edits')}; adoption: {member['adoption_status']}.",
                "",
                member["justification"].strip(),
                "",
                "```yaml",
                yaml.safe_dump(member, sort_keys=False, allow_unicode=True).rstrip(),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


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
    listing.add_argument("--change-set", help="Select the members of a change set")
    sub.add_parser("list-change-sets")
    sub.add_parser(
        "refresh-change-set-views",
        help="Regenerate the readable before/after fields from validated member proposals",
    )
    export = sub.add_parser("export")
    export.add_argument("id")
    args = parser.parse_args(argv)
    records, change_sets, errors = load_registry_bundle(
        args.root, refresh_views=args.command == "refresh-change-set-views"
    )
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.command == "refresh-change-set-views":
        root = args.root if args.root is not None else repo_root()
        fields = (
            "id",
            "title",
            "change_set_type",
            "justification",
            "ontology",
            "mapping_representation",
            "before",
            "after",
            "analysis_links",
            "source_links",
            "upstream_requests",
            "member_statuses",
            "affected_records",
            "see_also",
            "changes",
        )
        updated = 0
        for change_set in change_sets:
            path = root / REGISTRY / "change_sets" / f"{change_set['id']}.yaml"
            text = yaml.safe_dump(
                {
                    **{key: change_set[key] for key in fields if key in change_set},
                    **change_set,
                },
                sort_keys=False,
                allow_unicode=True,
                width=100,
            )
            if path.read_text() != text:
                path.write_text(text)
                updated += 1
        print(f"Updated {updated} change-set view(s)")
    elif args.command == "validate":
        print(
            f"Validated {len(records)} ontology change proposal(s) and {len(change_sets)} change set(s)"
        )
    elif args.command == "list-change-sets":
        print(json.dumps(change_sets, indent=2, default=_json_default))
    elif args.command == "list":
        members = None
        if args.change_set:
            change_set = next(
                (s for s in change_sets if s["id"] == args.change_set), None
            )
            if change_set is None:
                print(f"Unknown change set: {args.change_set}", file=sys.stderr)
                return 1
            members = set(change_ids(change_set))
        selected = [
            r
            for r in records
            if (members is None or r["id"] in members)
            and (not args.ontology or r["ontology"] == args.ontology)
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
        change_set = next(
            (s for s in change_sets if args.id == s["id"] or args.id in change_ids(s)),
            None,
        )
        if change_set is not None:
            print(render_change_set(change_set, {r["id"]: r for r in records}), end="")
            return 0
        record = next((r for r in records if r["id"] == args.id), None)
        if record is None:
            print(f"Unknown proposal: {args.id}", file=sys.stderr)
            return 1
        print(render_request(record), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
