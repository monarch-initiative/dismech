#!/usr/bin/env python3
"""Fetch and save artifacts from an Edison research trajectory.

This script retrieves figures and other artifacts produced by an Edison deep-research
run and saves them alongside the corresponding research markdown file.  The research
file's YAML frontmatter is updated to record the trajectory ID and artifact list, and
an ## Artifacts section is appended to the body for any image artifacts.

Usage:
    uv run python scripts/fetch_edison_artifacts.py <trajectory_id> <research_file>

Requires EDISON_API_KEY to be set in the environment.  The just recipe
`fetch-research-artifacts` sets this automatically from the environment.

Example:
    uv run python scripts/fetch_edison_artifacts.py \\
        0ab9e2d2-7601-4bbe-ba01-e26bfce94cfd \\
        research/Dimethylglycine_Dehydrogenase_Deficiency-deep-research-falcon.md
"""

from __future__ import annotations

import argparse
import base64
import os
import sys
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# API key helpers
# ---------------------------------------------------------------------------

def _load_api_key() -> str:
    """Return EDISON_API_KEY (or the deprecated FUTUREHOUSE_API_KEY) from the environment."""
    key = os.getenv("EDISON_API_KEY") or os.getenv("FUTUREHOUSE_API_KEY")
    if key:
        return key.strip()
    raise SystemExit(
        "EDISON_API_KEY is not set.\n"
        "Export it before running this script, for example:\n"
        "    export EDISON_API_KEY=<your-api-key>"
    )


# ---------------------------------------------------------------------------
# Artifact helpers
# ---------------------------------------------------------------------------

def _write_artifacts(artifacts: list, output_file: Path) -> None:
    """Decode and write artifact files to *output_file.stem*_artifacts/.

    Filenames are already deduplicated by FalconProvider._extract_artifacts, so
    we write each artifact directly without additional collision handling.
    """
    artifact_dir = output_file.parent / f"{output_file.stem}_artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=True)

    for artifact in artifacts:
        dest = artifact_dir / artifact.filename
        dest.write_bytes(base64.b64decode(artifact.content_base64))
        # Store the path relative to the report's directory so markdown links work
        artifact.path = (artifact_dir / artifact.filename).relative_to(output_file.parent).as_posix()
        print(f"  Saved artifact: {dest}")


# ---------------------------------------------------------------------------
# Markdown / frontmatter update
# ---------------------------------------------------------------------------

def _update_research_file(
    output_file: Path,
    trajectory_id: str,
    artifacts: list,
) -> None:
    """Patch *output_file* to record *trajectory_id* and the artifact list."""
    text = output_file.read_text()

    if not text.startswith("---\n"):
        print(f"Warning: {output_file} has no YAML frontmatter – skipping update.")
        return

    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        print(f"Warning: Could not locate end of frontmatter in {output_file} – skipping update.")
        return

    frontmatter_str = text[4:end_idx]
    body = text[end_idx + 5:]  # content after the closing ---\n

    metadata = yaml.safe_load(frontmatter_str) or {}

    # Preserve existing trajectory_id if already set
    metadata["trajectory_id"] = trajectory_id
    metadata["artifact_count"] = len(artifacts)
    metadata["artifacts"] = [
        {
            "filename": a.filename,
            "path": a.path or a.filename,
            "media_type": a.media_type,
            "source": a.source,
            "data_storage_id": a.data_storage_id,
            "description": a.description,
        }
        for a in artifacts
    ]

    new_frontmatter = yaml.dump(metadata, default_flow_style=False, sort_keys=False)
    updated = f"---\n{new_frontmatter}---\n{body}"

    # Add an ## Artifacts section to the body for image artifacts
    image_artifacts = [a for a in artifacts if (a.media_type or "").startswith("image/")]
    if image_artifacts and "## Artifacts" not in updated:
        section_lines = ["\n## Artifacts\n"]
        for a in artifacts:
            path = a.path or a.filename
            label = a.description or a.filename
            if (a.media_type or "").startswith("image/"):
                section_lines.append(f"![{label}]({path})")
            else:
                section_lines.append(f"- [{label}]({path})")
        section = "\n".join(section_lines) + "\n"

        if "\n## Citations" in updated:
            updated = updated.replace("\n## Citations", f"\n{section}\n## Citations", 1)
        else:
            updated = updated.rstrip() + "\n" + section

    output_file.write_text(updated)
    print(f"Updated frontmatter: {output_file}")


# ---------------------------------------------------------------------------
# Main fetch logic
# ---------------------------------------------------------------------------

def fetch_artifacts(trajectory_id: str, output_file: Path) -> int:
    """Fetch artifacts for *trajectory_id* and save them beside *output_file*.

    Returns the number of artifacts saved.
    """
    from edison_client import EdisonClient
    from edison_client.models.app import TaskResponseVerbose
    from deep_research_client.providers.falcon import FalconProvider
    from deep_research_client.models import ProviderConfig

    api_key = _load_api_key()
    client = EdisonClient(api_key=api_key)

    print(f"Fetching trajectory {trajectory_id} ...")
    task_response = client.get_task(trajectory_id, verbose=True)

    if not isinstance(task_response, TaskResponseVerbose):
        print(f"Unexpected response type: {type(task_response)}")
        return 0

    print(f"Task status: {task_response.status}")

    provider = FalconProvider(ProviderConfig(name="falcon", api_key=api_key))
    artifacts = provider._extract_artifacts(client, [task_response])

    if not artifacts:
        print("No artifacts found in trajectory.")
        return 0

    print(f"Found {len(artifacts)} artifact(s).")
    _write_artifacts(artifacts, output_file)
    _update_research_file(output_file, trajectory_id, artifacts)
    return len(artifacts)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch artifacts from a completed Edison research trajectory and save them alongside a research report.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("trajectory_id", help="Edison trajectory UUID")
    parser.add_argument(
        "research_file",
        type=Path,
        help="Path to the research markdown file (e.g. research/Foo-deep-research-falcon.md)",
    )
    args = parser.parse_args()

    if not args.research_file.exists():
        print(f"Error: Research file not found: {args.research_file}", file=sys.stderr)
        sys.exit(1)

    count = fetch_artifacts(args.trajectory_id, args.research_file)
    print(f"\nDone – {count} artifact(s) saved.")


if __name__ == "__main__":
    main()
