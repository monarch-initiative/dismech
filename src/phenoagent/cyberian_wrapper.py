"""Wrapper for running phenoagent explanation completion via cyberian + Claude Code."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import shlex
import subprocess
import sys
import uuid
from typing import Any

import yaml

from phenoagent.matching_cli import create_initial_matching_file

WORKFLOW_FILE = Path(__file__).resolve().parent / "workflows" / "explain_non_matches.workflow.yaml"


@dataclass(frozen=True)
class MatchingAgentRunResult:
    """Result metadata from a matching-agent execution."""

    matching_file: Path
    workdir: Path
    pr_is_diagnosis: float | None


def _repo_root() -> Path:
    """Return repository root path."""
    return Path(__file__).resolve().parents[2]


def _safe_token(value: str) -> str:
    """Convert arbitrary text to a filesystem-safe token."""
    token = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    token = token.strip("_")
    return token or "unknown"


def _default_matching_workdir(matching_file: Path, *, root_dir: Path | None = None) -> Path:
    """Build default workdir: ./workdirs/matching/<case>/<disease>/<shortuuid>/."""
    case_id = matching_file.stem
    disease_slug = "unknown_disease"

    try:
        with open(matching_file) as stream:
            data = yaml.safe_load(stream)
        if isinstance(data, dict):
            if data.get("case_id"):
                case_id = str(data["case_id"])
            if data.get("disease_slug"):
                disease_slug = str(data["disease_slug"])
    except Exception:
        pass

    short_uuid = uuid.uuid4().hex[:8]
    base = (root_dir or _repo_root()) / "workdirs" / "matching"
    return base / _safe_token(case_id) / _safe_token(disease_slug) / short_uuid


def _read_pr_is_diagnosis(matching_file: Path) -> float | None:
    """Read pr_is_diagnosis from matching YAML, returning None if unavailable."""
    try:
        with open(matching_file) as stream:
            data: Any = yaml.safe_load(stream)
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    value = data.get("pr_is_diagnosis")
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def build_cyberian_workflow_command(
    *,
    workflow_file: Path,
    matching_file: Path,
    workdir: Path,
    host: str = "localhost",
    port: int = 3284,
    timeout: int = 1800,
    poll_interval: float = 2.0,
    agent_type: str = "claude",
    skip_permissions: bool = True,
    agent_lifecycle: str = "refresh",
    verbosity: int = 1,
) -> list[str]:
    """Build command for running the cyberian workflow."""
    cmd = [
        sys.executable,
        "-m",
        "cyberian.cli",
        "workflow",
        "run",
        str(workflow_file),
        "--workdir",
        str(workdir),
        "--host",
        host,
        "--port",
        str(port),
        "--timeout",
        str(timeout),
        "--poll-interval",
        str(poll_interval),
        "--agent-type",
        agent_type,
        "--agent-lifecycle",
        agent_lifecycle,
        "--param",
        f"matching_file={matching_file}",
    ]

    if skip_permissions:
        cmd.append("--skip-permissions")
    if verbosity > 0:
        cmd.extend(["-v"] * verbosity)

    return cmd


def run_matching_explanation_agent(
    phenopacket_path: Path,
    disease_reference: str,
    *,
    output_path: Path | None = None,
    kb_dir: Path | None = None,
    workdir: Path | None = None,
    host: str = "localhost",
    port: int = 3284,
    timeout: int = 1800,
    poll_interval: float = 2.0,
    agent_type: str = "claude",
    skip_permissions: bool = True,
    agent_lifecycle: str = "refresh",
    verbosity: int = 1,
    dry_run: bool = False,
) -> MatchingAgentRunResult:
    """Run deterministic initialization, then cyberian looping explanation completion."""
    if not WORKFLOW_FILE.exists():
        raise FileNotFoundError(f"Workflow file not found: {WORKFLOW_FILE}")

    matching_file = create_initial_matching_file(
        phenopacket_path=phenopacket_path,
        disease_reference=disease_reference,
        output_path=output_path,
        kb_dir=kb_dir,
    ).resolve()

    run_dir = (workdir or _default_matching_workdir(matching_file)).resolve()
    run_dir.mkdir(parents=True, exist_ok=True)

    cmd = build_cyberian_workflow_command(
        workflow_file=WORKFLOW_FILE,
        matching_file=matching_file,
        workdir=run_dir,
        host=host,
        port=port,
        timeout=timeout,
        poll_interval=poll_interval,
        agent_type=agent_type,
        skip_permissions=skip_permissions,
        agent_lifecycle=agent_lifecycle,
        verbosity=verbosity,
    )

    if dry_run:
        print(shlex.join(cmd))
        return MatchingAgentRunResult(
            matching_file=matching_file,
            workdir=run_dir,
            pr_is_diagnosis=_read_pr_is_diagnosis(matching_file),
        )

    subprocess.run(cmd, check=True, cwd=run_dir)
    return MatchingAgentRunResult(
        matching_file=matching_file,
        workdir=run_dir,
        pr_is_diagnosis=_read_pr_is_diagnosis(matching_file),
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run phenoagent explanation completion via cyberian workflow")
    parser.add_argument("phenopacket_path", type=Path, help="Path to a GA4GH phenopacket JSON file")
    parser.add_argument("disease_reference", help="DisMech disease reference: slug, id, name, or YAML path")
    parser.add_argument("--output", type=Path, default=None, help="Optional output matching YAML path")
    parser.add_argument("--kb-dir", type=Path, default=None, help="Optional disorder directory override")
    parser.add_argument(
        "--workdir",
        type=Path,
        default=None,
        help="Agent working directory (default: ./workdirs/matching/<case>/<disease>/<shortuuid>/)",
    )
    parser.add_argument("--host", default="localhost", help="Agent API host")
    parser.add_argument("--port", type=int, default=3284, help="Agent API port")
    parser.add_argument("--timeout", type=int, default=1800, help="Per-task timeout in seconds")
    parser.add_argument("--poll-interval", type=float, default=2.0, help="Status poll interval in seconds")
    parser.add_argument("--agent-type", default="claude", help="Agent type passed to cyberian")
    parser.add_argument(
        "--agent-lifecycle",
        choices=("reuse", "refresh"),
        default="refresh",
        help="Server lifecycle mode for cyberian workflow",
    )
    parser.add_argument(
        "--no-skip-permissions",
        action="store_true",
        help="Disable cyberian skip-permissions flag",
    )
    parser.add_argument(
        "--verbosity",
        type=int,
        default=1,
        help="Cyberian verbosity count (0,1,2...) mapping to -v flags",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print cyberian command and exit")
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    result = run_matching_explanation_agent(
        phenopacket_path=args.phenopacket_path,
        disease_reference=args.disease_reference,
        output_path=args.output,
        kb_dir=args.kb_dir,
        workdir=args.workdir,
        host=args.host,
        port=args.port,
        timeout=args.timeout,
        poll_interval=args.poll_interval,
        agent_type=args.agent_type,
        skip_permissions=not args.no_skip_permissions,
        agent_lifecycle=args.agent_lifecycle,
        verbosity=args.verbosity,
        dry_run=args.dry_run,
    )
    # Keep matching file path as first line for simple shell usage.
    print(result.matching_file)
    print(f"workdir={result.workdir}")
    pr_value = "NA" if result.pr_is_diagnosis is None else result.pr_is_diagnosis
    print(f"pr_is_diagnosis={pr_value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
