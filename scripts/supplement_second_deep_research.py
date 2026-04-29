#!/usr/bin/env python3
"""Batch supplement deep-research files with a second provider result."""

from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Set


RESEARCH_FILE_RE = re.compile(
    r"^(?P<name>.+)-deep-research-(?P<provider>[^.]+)\.md(?:\.citations\.md)?$"
)


@dataclass
class Attempt:
    disorder: str
    existing_providers: str
    selected_provider: str
    status: str
    duration_seconds: float
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Supplement disorder deep-research outputs so each disorder has at least "
            "two providers among falcon/openai/cyberian/cyberian-codex."
        )
    )
    parser.add_argument("--kb-dir", default="kb/disorders")
    parser.add_argument("--research-dir", default="research")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument(
        "--provider-order",
        nargs="+",
        default=["falcon", "openai", "cyberian-codex", "cyberian"],
        help="Provider preference order when selecting the second provider.",
    )
    parser.add_argument(
        "--target-providers",
        nargs="+",
        default=["falcon", "openai", "cyberian", "cyberian-codex"],
        help="Providers counted toward second-provider coverage.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=420,
        help="Per-disorder execution timeout in seconds.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=5000,
        help="max_tokens passed to openai/falcon providers.",
    )
    parser.add_argument(
        "--max-disorders",
        type=int,
        default=None,
        help="Optional cap on number of disorders to process.",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        default=None,
        help="Only process these disorder file stems.",
    )
    parser.add_argument(
        "--include-no-research",
        action="store_true",
        help="Also process disorders with no existing deep-research files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned actions but do not execute just commands.",
    )
    return parser.parse_args()


def disorder_names(kb_dir: str) -> List[str]:
    names = []
    for path in sorted(glob.glob(os.path.join(kb_dir, "*.yaml"))):
        stem = Path(path).stem
        if stem.endswith(".history"):
            continue
        names.append(stem)
    return names


def research_providers_by_disorder(research_dir: str) -> Dict[str, Set[str]]:
    providers: Dict[str, Set[str]] = {}
    for path in glob.glob(os.path.join(research_dir, "*-deep-research-*.md*")):
        filename = os.path.basename(path)
        if filename.startswith("com_"):
            continue
        match = RESEARCH_FILE_RE.match(filename)
        if not match:
            continue
        disorder = match.group("name")
        provider = match.group("provider")
        providers.setdefault(disorder, set()).add(provider)
    return providers


def choose_provider(
    existing_targeted: Set[str], provider_order: Iterable[str]
) -> str | None:
    for provider in provider_order:
        if provider not in existing_targeted:
            return provider
    return None


def build_command(disorder: str, provider: str, max_tokens: int) -> List[str]:
    if provider == "cyberian-codex":
        return [
            "just",
            "research-disorder-cyberian-codex",
            disorder,
            f"--param=max_tokens={max_tokens}",
        ]
    cmd = ["just", "research-disorder", provider, disorder]
    if provider in {"openai", "falcon"} and max_tokens > 0:
        cmd.extend(["--param", f"max_tokens={max_tokens}"])
    return cmd


def run_attempt(
    disorder: str,
    existing_all: Set[str],
    provider: str,
    timeout_seconds: int,
    max_tokens: int,
    dry_run: bool,
) -> Attempt:
    existing = ",".join(sorted(existing_all))
    if dry_run:
        return Attempt(disorder, existing, provider, "DRY_RUN", 0.0, "")

    cmd = build_command(disorder, provider, max_tokens)
    started = time.monotonic()
    try:
        result = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        duration = time.monotonic() - started
        status = "OK" if result.returncode == 0 else f"ERROR_{result.returncode}"
        detail = (result.stderr or result.stdout or "").strip().splitlines()
        detail_text = detail[-1] if detail else ""
        return Attempt(disorder, existing, provider, status, duration, detail_text)
    except subprocess.TimeoutExpired:
        duration = time.monotonic() - started
        return Attempt(
            disorder,
            existing,
            provider,
            "TIMEOUT",
            duration,
            f"timeout after {timeout_seconds}s",
        )


def write_report(attempts: List[Attempt], output_dir: str) -> Path:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    report_path = Path(output_dir) / f"second_provider_attempts_{timestamp}.tsv"
    with report_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "disorder",
                "existing_providers",
                "selected_provider",
                "status",
                "duration_seconds",
                "detail",
            ]
        )
        for attempt in attempts:
            writer.writerow(
                [
                    attempt.disorder,
                    attempt.existing_providers,
                    attempt.selected_provider,
                    attempt.status,
                    f"{attempt.duration_seconds:.2f}",
                    attempt.detail,
                ]
            )
    return report_path


def main() -> int:
    args = parse_args()
    target_provider_set = set(args.target_providers)

    names = disorder_names(args.kb_dir)
    by_disorder = research_providers_by_disorder(args.research_dir)
    only = set(args.only or [])

    queue: List[tuple[str, Set[str], Set[str], str]] = []
    for disorder in names:
        if only and disorder not in only:
            continue
        existing_all = by_disorder.get(disorder, set())
        if not args.include_no_research and not existing_all:
            continue
        existing_targeted = existing_all.intersection(target_provider_set)
        if len(existing_targeted) >= 2:
            continue
        selected = choose_provider(existing_targeted, args.provider_order)
        if selected is None:
            continue
        queue.append((disorder, existing_all, existing_targeted, selected))

    if args.max_disorders is not None:
        queue = queue[: args.max_disorders]

    print(f"Candidate disorders: {len(queue)}")

    attempts: List[Attempt] = []
    for i, (disorder, existing_all, _existing_targeted, provider) in enumerate(
        queue, start=1
    ):
        print(
            f"[{i}/{len(queue)}] {disorder}: existing={sorted(existing_all)} "
            f"-> selected={provider}"
        )
        attempt = run_attempt(
            disorder=disorder,
            existing_all=existing_all,
            provider=provider,
            timeout_seconds=args.timeout_seconds,
            max_tokens=args.max_tokens,
            dry_run=args.dry_run,
        )
        attempts.append(attempt)
        print(
            f"    status={attempt.status} duration={attempt.duration_seconds:.1f}s "
            f"detail={attempt.detail}"
        )

    report_path = write_report(attempts, args.output_dir)
    ok = sum(1 for a in attempts if a.status == "OK")
    timeout = sum(1 for a in attempts if a.status == "TIMEOUT")
    errors = sum(1 for a in attempts if a.status.startswith("ERROR_"))
    dry = sum(1 for a in attempts if a.status == "DRY_RUN")
    print(
        "Summary: "
        f"ok={ok} timeout={timeout} errors={errors} dry_run={dry}; "
        f"report={report_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
