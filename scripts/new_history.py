#!/usr/bin/env python3
"""Scaffold a valid dismech history record.

History records (``history/<kind>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml``)
are append-only curation/review/audit provenance files. They are documented in
``docs/history.md`` and validated against ``src/dismech/schema/history.yaml``.

This helper removes the friction that has kept curation PRs from including a
record: it generates the correct path, a UTC timestamp, a collision-proof
session id, and a schema-valid skeleton, so a curator only supplies the event
content. It is the intended way to *start* a record -- edit the emitted
``details`` afterwards, then validate with ``just validate-history <path>``.

Examples
--------
Record creation of a new disorder entry (AI-assisted)::

    uv run python scripts/new_history.py \
        --kind disorder --slug Asthma --event CREATE --outcome changed \
        --summary "Create: Asthma" \
        --actor-name claude-code --actor-type ai_agent \
        --agent-tool claude-code \
        --sections phenotypes,pathophysiology,evidence \
        --pr 5123 --details "De-novo curation from Falcon deep research."

Record a human review that changed nothing::

    uv run python scripts/new_history.py \
        --kind disorder --slug Marfan_Syndrome --event REVIEW --outcome no_change \
        --summary "Review: Marfan Syndrome" --actor-name cjm --actor-type human \
        --issue 2892 --details "Spot-checked evidence; no edits needed."

The script prints the path it created as its final stdout line, so automation
can capture it.
"""

from __future__ import annotations

import argparse
import re
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_URL = "https://github.com/monarch-initiative/dismech"

# kind -> (kb directory, requires a slug-derived path). ``schema``/``other``
# targets live outside kb/, so they require an explicit --path.
KIND_DIRS = {
    "disorder": "kb/disorders",
    "module": "kb/modules",
    "comorbidity": "kb/comorbidities",
}
KINDS = list(KIND_DIRS) + ["schema", "other"]

EVENTS = ["GENERAL", "CREATE", "EDIT", "REVIEW", "AUDIT"]
OUTCOMES = ["changed", "no_change", "needs_followup", "blocked"]
ACTOR_TYPES = ["human", "ai_agent", "automation", "other"]


class _LiteralStr(str):
    """A string forced to serialize as a YAML literal block scalar (``|``)."""


def _literal_representer(dumper: yaml.Dumper, data: _LiteralStr):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style="|")


yaml.add_representer(_LiteralStr, _literal_representer)


def _actor_slug(name: str) -> str:
    """Filename-safe actor token: lowercase, non-alnum collapsed to '-'."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "actor"


def _expand_ref(value: str, kind: str) -> str:
    """Turn a bare issue/PR number into a full GitHub URL; pass URLs through."""
    value = value.strip()
    if not value:
        return value
    if value.startswith(("http://", "https://")):
        return value
    if value.isdigit():
        segment = "issues" if kind == "issue" else "pull"
        return f"{REPO_URL}/{segment}/{value}"
    return value


def _split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def build_record(args: argparse.Namespace) -> tuple[dict, Path]:
    now = datetime.now(timezone.utc).replace(microsecond=0)
    file_ts = now.strftime("%Y-%m-%dT%H%M%SZ")
    iso_ts = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    shortid = secrets.token_hex(3)

    # Resolve the target path.
    if args.kind in KIND_DIRS:
        if not args.slug:
            sys.exit(f"error: --slug is required for kind '{args.kind}'")
        path = f"{KIND_DIRS[args.kind]}/{args.slug}.yaml"
    else:
        if not args.path:
            sys.exit(f"error: --path is required for kind '{args.kind}'")
        path = args.path

    slug = args.slug or Path(path).stem

    actor_token = _actor_slug(args.actor_name)
    session_id = f"{file_ts}-{actor_token}-{shortid}"

    actor: dict = {"type": args.actor_type, "name": args.actor_name}
    if args.model:
        actor["model"] = args.model
    if args.agent_tool:
        actor["agent_tool"] = args.agent_tool
    if args.agent_version:
        actor["agent_version"] = args.agent_version

    target: dict = {"kind": args.kind}
    if slug:
        target["slug"] = slug
    target["path"] = path

    event: dict = {"type": args.event, "outcome": args.outcome}
    sections = _split_csv(args.sections)
    if sections:
        event["sections"] = sections
    event["summary"] = args.summary
    event["details"] = _LiteralStr(
        (args.details or "TODO: replace with curation/review notes.").rstrip() + "\n"
    )

    record = {
        "history_version": 1,
        "target": target,
        "session": {
            "id": session_id,
            "timestamp": iso_ts,
            "actors": [actor],
        },
        "links": {
            "issues": [_expand_ref(v, "issue") for v in args.issue],
            "prs": [_expand_ref(v, "pr") for v in args.pr],
            "urls": list(args.url),
        },
        "events": [event],
    }

    # history/<kind>s/<slug>/ mirrors the committed layout (disorders, modules,
    # comorbidities). schema/other records use the kind name directly.
    subdir = {
        "disorder": "disorders",
        "module": "modules",
        "comorbidity": "comorbidities",
    }.get(args.kind, args.kind)
    out_dir = Path("history") / subdir / slug
    out_path = out_dir / f"{session_id}.yaml"
    return record, out_path


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Scaffold a schema-valid dismech history record.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--kind", required=True, choices=KINDS, help="Target object kind.")
    p.add_argument("--slug", help="Target slug / file stem (e.g. Asthma). Required for kb kinds.")
    p.add_argument("--path", help="Explicit repo-relative target path (required for schema/other).")
    p.add_argument("--event", default="EDIT", choices=EVENTS, help="Event type (default: EDIT).")
    p.add_argument("--outcome", default="changed", choices=OUTCOMES, help="Event outcome (default: changed).")
    p.add_argument("--summary", required=True, help="Short one-line summary for listings.")
    p.add_argument("--details", help="Rich free-text notes (multi-line ok). Placeholder inserted if omitted.")
    p.add_argument("--sections", help="Comma-separated section names touched (e.g. phenotypes,evidence).")
    p.add_argument("--actor-name", default="claude-code", help="Actor name (default: claude-code).")
    p.add_argument("--actor-type", default="ai_agent", choices=ACTOR_TYPES, help="Actor category (default: ai_agent).")
    p.add_argument("--model", help="Model id for AI-assisted curation (e.g. claude-opus-4-8).")
    p.add_argument("--agent-tool", help="Agent tool/client (e.g. claude-code, codex).")
    p.add_argument("--agent-version", help="Agent tool/client version.")
    p.add_argument("--issue", action="append", default=[], help="Issue number or URL (repeatable).")
    p.add_argument("--pr", action="append", default=[], help="PR number or URL (repeatable).")
    p.add_argument("--url", action="append", default=[], help="Other relevant URL (repeatable).")
    p.add_argument("--force", action="store_true", help="Overwrite if the target file already exists.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    record, out_path = build_record(args)

    if out_path.exists() and not args.force:
        sys.exit(f"error: {out_path} already exists (use --force to overwrite)")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        yaml.dump(record, fh, sort_keys=False, default_flow_style=False, allow_unicode=True)

    print(f"Wrote history record: {out_path}", file=sys.stderr)
    print(f"Next: edit the 'details', then run: just validate-history {out_path}", file=sys.stderr)
    print(out_path)  # machine-capturable final stdout line
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
