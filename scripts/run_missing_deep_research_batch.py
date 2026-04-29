#!/usr/bin/env python3
"""Run deep research for a list of disorders with provider fallback and batch commits."""

from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


DEFAULT_LIST = "/tmp/dismech-missing-research-clean.txt"
PROVIDERS = ("falcon", "openai", "cyberian")
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
BACKFILL_SCRIPT = SCRIPT_DIR / "backfill_deep_research_evidence.py"
PROGRESS_PATH = REPO_ROOT / "output" / "deep_research_batch_progress.tsv"
ATTEMPT_PATH = REPO_ROOT / "output" / "deep_research_batch_attempts.tsv"


@dataclass
class DisorderRunResult:
    disorder: str
    status: str
    provider: str
    research_file: str
    citations_file: str
    yaml_changed: bool
    validation_ok: bool
    note: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run deep research for missing disorders with falcon -> openai -> cyberian "
            "fallback, then backfill top-level references/findings and validate."
        )
    )
    parser.add_argument("--list-file", default=DEFAULT_LIST)
    parser.add_argument("--kb-dir", default="kb/disorders")
    parser.add_argument("--research-dir", default="research")
    parser.add_argument("--progress-log", default=str(PROGRESS_PATH))
    parser.add_argument("--attempt-log", default=str(ATTEMPT_PATH))
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--max-disorders", type=int, default=None)
    parser.add_argument(
        "--research-timeout-seconds",
        type=int,
        default=1800,
        help="Timeout for each just research-disorder provider attempt.",
    )
    parser.add_argument(
        "--validate-timeout-seconds",
        type=int,
        default=180,
        help="Timeout for each just validate invocation.",
    )
    parser.add_argument(
        "--backfill-timeout-seconds",
        type=int,
        default=600,
        help="Timeout for each backfill helper invocation.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip disorders already present in the progress log with terminal status.",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        help="Create batch commits after every N successfully researched disorders.",
    )
    parser.add_argument(
        "--commit-message",
        default="",
        help="Override the generated git commit message for this run.",
    )
    return parser.parse_args()


def sha1_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def read_list(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def read_completed(progress_path: Path) -> set[str]:
    if not progress_path.exists():
        return set()
    completed: set[str] = set()
    with progress_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            disorder = row.get("disorder", "").strip()
            status = row.get("status", "").strip()
            if disorder and status in {"success", "research_only", "failed"}:
                completed.add(disorder)
    return completed


def append_tsv(path: Path, fieldnames: Sequence[str], row: dict[str, object]) -> None:
    ensure_parent(path)
    write_header = not path.exists()
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def run_command(
    cmd: Sequence[str],
    *,
    timeout_seconds: int,
    cwd: Path,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
        timeout=timeout_seconds,
    )


def verify_research_outputs(
    research_dir: Path, disorder: str, provider: str
) -> tuple[Path, Path]:
    research_file = research_dir / f"{disorder}-deep-research-{provider}.md"
    citations_file = (
        research_dir / f"{disorder}-deep-research-{provider}.md.citations.md"
    )
    if not research_file.exists() or research_file.stat().st_size == 0:
        raise FileNotFoundError(f"missing research output {research_file}")
    if not citations_file.exists() or citations_file.stat().st_size == 0:
        raise FileNotFoundError(f"missing citations output {citations_file}")
    return research_file, citations_file


def git_has_changes(paths: Iterable[Path]) -> bool:
    resolved = [str(path) for path in paths if path.exists()]
    if not resolved:
        return False
    result = subprocess.run(
        ["git", "status", "--short", "--", *resolved],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return bool(result.stdout.strip())


def commit_batch(paths: Iterable[Path], message: str) -> bool:
    resolved = [str(path) for path in paths if path.exists()]
    if not resolved:
        return False
    subprocess.run(
        ["git", "add", "--", *resolved],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    diff = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if not diff.stdout.strip():
        return False
    commit = subprocess.run(
        ["git", "commit", "-m", message],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if commit.returncode != 0:
        print(commit.stdout)
        print(commit.stderr, file=sys.stderr)
        return False
    print(commit.stdout.strip())
    return True


def batch_commit_message(
    batch_index: int, disorders: list[str], explicit_message: str = ""
) -> str:
    if explicit_message:
        return explicit_message
    start = disorders[0]
    end = disorders[-1]
    return f"Run deep research batch {batch_index:03d} ({start} to {end})"


def run_disorder(
    disorder: str,
    *,
    kb_dir: Path,
    research_dir: Path,
    attempt_log: Path,
    research_timeout_seconds: int,
    backfill_timeout_seconds: int,
    validate_timeout_seconds: int,
) -> DisorderRunResult:
    yaml_path = kb_dir / f"{disorder}.yaml"
    if not yaml_path.exists():
        return DisorderRunResult(
            disorder=disorder,
            status="failed",
            provider="",
            research_file="",
            citations_file="",
            yaml_changed=False,
            validation_ok=False,
            note=f"missing yaml file {yaml_path}",
        )

    yaml_before = yaml_path.read_text(encoding="utf-8")
    yaml_before_sha = sha1_text(yaml_before)

    for provider in PROVIDERS:
        research_file = research_dir / f"{disorder}-deep-research-{provider}.md"
        citations_file = (
            research_dir / f"{disorder}-deep-research-{provider}.md.citations.md"
        )
        for candidate in (research_file, citations_file):
            if candidate.exists() and candidate.stat().st_size == 0:
                candidate.unlink()

        started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        try:
            result = run_command(
                ["just", "research-disorder", provider, disorder],
                timeout_seconds=research_timeout_seconds,
                cwd=REPO_ROOT,
            )
            try:
                verified_research_file, verified_citations_file = (
                    verify_research_outputs(research_dir, disorder, provider)
                )
                verified = True
            except FileNotFoundError as exc:
                verified = False
                verify_note = str(exc)
                verified_research_file = research_file
                verified_citations_file = citations_file

            append_tsv(
                attempt_log,
                (
                    "timestamp",
                    "disorder",
                    "provider",
                    "returncode",
                    "verified_outputs",
                    "note",
                ),
                {
                    "timestamp": started,
                    "disorder": disorder,
                    "provider": provider,
                    "returncode": result.returncode,
                    "verified_outputs": str(verified),
                    "note": verify_note if not verified else "",
                },
            )

            if result.returncode != 0 or not verified:
                continue
        except subprocess.TimeoutExpired:
            append_tsv(
                attempt_log,
                (
                    "timestamp",
                    "disorder",
                    "provider",
                    "returncode",
                    "verified_outputs",
                    "note",
                ),
                {
                    "timestamp": started,
                    "disorder": disorder,
                    "provider": provider,
                    "returncode": "timeout",
                    "verified_outputs": "False",
                    "note": f"timeout after {research_timeout_seconds}s",
                },
            )
            continue

        backup_text = yaml_path.read_text(encoding="utf-8")
        try:
            backfill = run_command(
                [
                    "uv",
                    "run",
                    "python",
                    str(BACKFILL_SCRIPT),
                    "--only",
                    disorder,
                    "--apply",
                    "--fetch-missing-cache",
                    "--add-findings",
                ],
                timeout_seconds=backfill_timeout_seconds,
                cwd=REPO_ROOT,
            )
            if backfill.returncode != 0:
                yaml_path.write_text(backup_text, encoding="utf-8")
                return DisorderRunResult(
                    disorder=disorder,
                    status="research_only",
                    provider=provider,
                    research_file=str(verified_research_file),
                    citations_file=str(verified_citations_file),
                    yaml_changed=False,
                    validation_ok=False,
                    note="backfill helper failed",
                )

            validate = run_command(
                ["just", "validate", str(yaml_path)],
                timeout_seconds=validate_timeout_seconds,
                cwd=REPO_ROOT,
            )
            if validate.returncode != 0:
                yaml_path.write_text(backup_text, encoding="utf-8")
                return DisorderRunResult(
                    disorder=disorder,
                    status="research_only",
                    provider=provider,
                    research_file=str(verified_research_file),
                    citations_file=str(verified_citations_file),
                    yaml_changed=False,
                    validation_ok=False,
                    note="validation failed after integration; yaml restored",
                )
        except subprocess.TimeoutExpired:
            yaml_path.write_text(backup_text, encoding="utf-8")
            return DisorderRunResult(
                disorder=disorder,
                status="research_only",
                provider=provider,
                research_file=str(verified_research_file),
                citations_file=str(verified_citations_file),
                yaml_changed=False,
                validation_ok=False,
                note="integration step timed out; yaml restored",
            )

        yaml_after = yaml_path.read_text(encoding="utf-8")
        yaml_changed = sha1_text(yaml_after) != yaml_before_sha
        note = "research + validation complete"
        if not yaml_changed:
            note = "research complete; yaml unchanged after backfill"
        return DisorderRunResult(
            disorder=disorder,
            status="success",
            provider=provider,
            research_file=str(verified_research_file),
            citations_file=str(verified_citations_file),
            yaml_changed=yaml_changed,
            validation_ok=True,
            note=note,
        )

    return DisorderRunResult(
        disorder=disorder,
        status="failed",
        provider="",
        research_file="",
        citations_file="",
        yaml_changed=False,
        validation_ok=False,
        note="all providers failed or produced incomplete outputs",
    )


def main() -> int:
    args = parse_args()

    list_file = Path(args.list_file)
    kb_dir = REPO_ROOT / args.kb_dir
    research_dir = REPO_ROOT / args.research_dir
    progress_log = Path(args.progress_log)
    attempt_log = Path(args.attempt_log)

    disorders = read_list(list_file)
    if args.max_disorders is not None:
        disorders = disorders[: args.max_disorders]

    completed = read_completed(progress_log) if args.resume else set()
    queue = [d for d in disorders if d not in completed]
    print(f"queued disorders: {len(queue)}")

    batch_index = 1
    processed_in_batch = 0
    batch_successes: list[str] = []
    batch_paths: set[Path] = set()
    helper_paths = {BACKFILL_SCRIPT, SCRIPT_DIR / "run_missing_deep_research_batch.py"}

    for idx, disorder in enumerate(queue, start=1):
        print(f"[{idx}/{len(queue)}] {disorder}")
        result = run_disorder(
            disorder,
            kb_dir=kb_dir,
            research_dir=research_dir,
            attempt_log=attempt_log,
            research_timeout_seconds=args.research_timeout_seconds,
            backfill_timeout_seconds=args.backfill_timeout_seconds,
            validate_timeout_seconds=args.validate_timeout_seconds,
        )
        append_tsv(
            progress_log,
            (
                "timestamp",
                "disorder",
                "status",
                "provider",
                "research_file",
                "citations_file",
                "yaml_changed",
                "validation_ok",
                "note",
            ),
            {
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "disorder": result.disorder,
                "status": result.status,
                "provider": result.provider,
                "research_file": result.research_file,
                "citations_file": result.citations_file,
                "yaml_changed": str(result.yaml_changed),
                "validation_ok": str(result.validation_ok),
                "note": result.note,
            },
        )

        if result.status in {"success", "research_only"}:
            processed_in_batch += 1
            batch_successes.append(result.disorder)
            if result.research_file:
                batch_paths.add(Path(result.research_file))
            if result.citations_file:
                batch_paths.add(Path(result.citations_file))
            if result.yaml_changed:
                batch_paths.add(kb_dir / f"{result.disorder}.yaml")

        if args.commit and processed_in_batch >= args.batch_size:
            commit_paths = set(batch_paths)
            if git_has_changes(helper_paths):
                commit_paths.update(helper_paths)
            if commit_paths:
                commit_batch(
                    commit_paths,
                    batch_commit_message(
                        batch_index, batch_successes, args.commit_message
                    ),
                )
            batch_index += 1
            processed_in_batch = 0
            batch_successes = []
            batch_paths = set()

    if args.commit and batch_paths:
        commit_paths = set(batch_paths)
        if git_has_changes(helper_paths):
            commit_paths.update(helper_paths)
        commit_batch(
            commit_paths,
            batch_commit_message(batch_index, batch_successes, args.commit_message),
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
