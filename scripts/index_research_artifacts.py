#!/usr/bin/env python3
"""
index_research_artifacts.py — Build an index of deep-research report artifacts.

Scans all research/*.md files (excluding *.citations.md), parses their YAML
frontmatter, and produces research/artifact_index.yaml with:

  - A list of all reports that have artifacts
  - A lookup table keyed by trajectory_id (and any other ID formats found)
  - A collision report flagging artifact filenames shared by multiple reports

Usage:
    python scripts/index_research_artifacts.py [--research-dir research/]
    # or via justfile:
    just index-research-artifacts
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def _split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body) from a Markdown file with YAML front matter."""
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    # find closing ---
    close = None
    for i, line in enumerate(lines[1:], start=1):
        if line.rstrip() == "---":
            close = i
            break
    if close is None:
        return {}, text
    fm_text = "".join(lines[1:close])
    body = "".join(lines[close + 1 :])
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def build_index(research_dir: Path) -> dict:
    """Scan research_dir for reports with artifacts and build the index dict."""
    report_files = sorted(
        p for p in research_dir.glob("*.md")
        if not p.name.endswith(".citations.md") and p.is_file()
    )

    reports_with_artifacts: list[dict] = []
    index_by_id: dict[str, dict] = {}

    # Track artifact filenames (basename only) → list of report stems, for collision check
    filename_map: dict[str, list[str]] = defaultdict(list)

    for report_path in report_files:
        try:
            text = report_path.read_text(encoding="utf-8")
        except OSError:
            continue
        fm, _ = _split_frontmatter(text)
        artifacts = fm.get("artifacts") or []
        if not artifacts:
            continue

        report_name = report_path.name
        entry: dict = {
            "file": report_name,
            "provider": fm.get("provider"),
            "trajectory_id": fm.get("trajectory_id"),
            "artifact_count": fm.get("artifact_count", len(artifacts)),
            "artifacts": [],
        }

        for art in artifacts:
            if not isinstance(art, dict):
                continue
            art_info = {
                "filename": art.get("filename"),
                "path": art.get("path"),
                "media_type": art.get("media_type"),
                "is_image": art.get("media_type", "").startswith("image/"),
            }
            entry["artifacts"].append(art_info)

            # Track basename for collision detection
            if art_info["filename"]:
                filename_map[art_info["filename"]].append(report_name)

        reports_with_artifacts.append(entry)

        # Index by trajectory_id
        if entry["trajectory_id"]:
            tid = entry["trajectory_id"]
            if tid in index_by_id:
                # Multiple reports for the same trajectory (shouldn't happen, but handle)
                existing = index_by_id[tid]
                if isinstance(existing, dict) and "_collision" not in existing:
                    index_by_id[tid] = {
                        "_collision": True,
                        "reports": [existing["report"], report_name],
                    }
                else:
                    index_by_id[tid]["reports"].append(report_name)
            else:
                index_by_id[tid] = {
                    "report": report_name,
                    "provider": entry["provider"],
                    "artifact_count": entry["artifact_count"],
                    "artifact_paths": [
                        a["path"] for a in entry["artifacts"] if a.get("path")
                    ],
                }

    # Detect filename collisions: same basename, different reports
    collisions = []
    for basename, report_list in sorted(filename_map.items()):
        # Only a collision if the basename appears in artifacts from different artifact dirs
        # (same report contributing the same filename twice is fine — DRC handles dedup)
        unique_reports = list(dict.fromkeys(report_list))
        if len(unique_reports) > 1:
            collisions.append({"filename": basename, "reports": unique_reports})

    return {
        "generated": datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "report_count": len(reports_with_artifacts),
        "artifact_total": sum(e["artifact_count"] for e in reports_with_artifacts),
        "collision_count": len(collisions),
        "reports": reports_with_artifacts,
        "index_by_trajectory_id": index_by_id,
        "collisions": collisions,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--research-dir",
        default="research",
        help="Path to the research/ directory (default: research/)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output YAML path (default: <research-dir>/artifact_index.yaml)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with non-zero status if any collisions are detected",
    )
    args = parser.parse_args(argv)

    research_dir = Path(args.research_dir)
    if not research_dir.is_dir():
        print(f"ERROR: research directory not found: {research_dir}", file=sys.stderr)
        return 1

    output_path = Path(args.output) if args.output else research_dir / "artifact_index.yaml"

    index = build_index(research_dir)

    # Write YAML index
    with output_path.open("w", encoding="utf-8") as fh:
        yaml.dump(
            index,
            fh,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )

    print(
        f"Indexed {index['report_count']} reports with "
        f"{index['artifact_total']} artifacts → {output_path}"
    )

    if index["collisions"]:
        print(f"\nWARNING: {index['collision_count']} artifact filename collision(s):")
        for c in index["collisions"]:
            print(f"  {c['filename']!r} appears in: {', '.join(c['reports'])}")
        if args.check:
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
