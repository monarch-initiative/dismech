#!/usr/bin/env python3
"""Report and backfill disorder deep-research provider coverage."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence, TextIO

import yaml


RESEARCH_FILE_RE = re.compile(r"^(?P<disorder>.+)-deep-research-(?P<provider>.+)\.md$")
FRONTMATTER_DELIMITER = "---"
TOP_LEVEL_FIELD_RE = re.compile(r"^(?P<key>name|category):\s*(?P<value>.*)$")


@dataclass(frozen=True)
class DisorderInfo:
    slug: str
    name: str
    category: str
    path: Path


@dataclass(frozen=True)
class ResearchReport:
    disorder: str
    provider: str
    path: Path
    citations_path: Path
    citations_exists: bool
    citation_count: int | None
    end_time: str
    mtime: float


@dataclass(frozen=True)
class CoverageRow:
    disorder: DisorderInfo
    reports: tuple[ResearchReport, ...]

    @property
    def providers(self) -> tuple[str, ...]:
        return tuple(sorted({report.provider for report in self.reports}))

    @property
    def provider_count(self) -> int:
        return len(self.providers)

    @property
    def report_count(self) -> int:
        return len(self.reports)

    @property
    def citation_file_count(self) -> int:
        return sum(1 for report in self.reports if report.citations_exists)

    @property
    def latest_report(self) -> ResearchReport | None:
        if not self.reports:
            return None
        return max(self.reports, key=lambda report: report.mtime)

    def reports_for_provider(self, provider: str) -> tuple[ResearchReport, ...]:
        return tuple(report for report in self.reports if report.provider == provider)

    def has_provider(self, provider: str) -> bool:
        return any(report.provider == provider for report in self.reports)


@dataclass(frozen=True)
class RunAttempt:
    disorder: str
    provider: str
    status: str
    returncode: int | str
    duration_seconds: float
    output_file: str
    citations_file: str
    command: str
    detail: str


def normalize_provider(provider: str) -> str:
    return provider.strip().lower()


def load_disorder_info(path: Path) -> DisorderInfo:
    values: dict[str, str] = {}
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                if line.startswith((" ", "\t", "-")):
                    continue
                match = TOP_LEVEL_FIELD_RE.match(line.rstrip("\n"))
                if not match:
                    continue
                raw_value = match.group("value").strip()
                if not raw_value:
                    continue
                try:
                    parsed_value = yaml.safe_load(raw_value)
                except yaml.YAMLError:
                    parsed_value = raw_value
                values[match.group("key")] = str(parsed_value).strip()
                if "name" in values and "category" in values:
                    break
    except OSError:
        values = {}
    return DisorderInfo(
        slug=path.stem,
        name=values.get("name") or path.stem.replace("_", " "),
        category=values.get("category") or "",
        path=path,
    )


def list_disorders(kb_dir: Path) -> tuple[DisorderInfo, ...]:
    return tuple(
        load_disorder_info(path)
        for path in sorted(kb_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    )


def parse_frontmatter(path: Path) -> Mapping[str, object]:
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            first_line = handle.readline()
            if first_line.strip() != FRONTMATTER_DELIMITER:
                return {}
            lines: list[str] = []
            for line in handle:
                if line.strip() == FRONTMATTER_DELIMITER:
                    break
                lines.append(line.rstrip("\n"))
            else:
                return {}
    except OSError:
        return {}
    raw = "\n".join(lines)
    try:
        parsed = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return {}
    return parsed if isinstance(parsed, Mapping) else {}


def parse_research_filename(path: Path) -> tuple[str, str] | None:
    if path.name.endswith(".citations.md"):
        return None
    match = RESEARCH_FILE_RE.match(path.name)
    if not match:
        return None
    return match.group("disorder"), normalize_provider(match.group("provider"))


def parse_optional_int(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def collect_reports(research_dir: Path) -> dict[str, list[ResearchReport]]:
    reports: dict[str, list[ResearchReport]] = {}
    for path in sorted(research_dir.glob("*-deep-research-*.md")):
        parsed = parse_research_filename(path)
        if parsed is None:
            continue
        disorder, provider = parsed
        if not path.exists() or path.stat().st_size == 0:
            continue
        frontmatter = parse_frontmatter(path)
        citations_path = Path(f"{path}.citations.md")
        report = ResearchReport(
            disorder=disorder,
            provider=provider,
            path=path,
            citations_path=citations_path,
            citations_exists=citations_path.exists()
            and citations_path.stat().st_size > 0,
            citation_count=parse_optional_int(frontmatter.get("citation_count")),
            end_time=str(frontmatter.get("end_time") or ""),
            mtime=path.stat().st_mtime,
        )
        reports.setdefault(disorder, []).append(report)
    return reports


def build_coverage(kb_dir: Path, research_dir: Path) -> tuple[CoverageRow, ...]:
    reports_by_disorder = collect_reports(research_dir)
    return tuple(
        CoverageRow(
            disorder=disorder, reports=tuple(reports_by_disorder.get(disorder.slug, []))
        )
        for disorder in list_disorders(kb_dir)
    )


def tsv_value(value: object) -> str:
    return str(value).replace("\t", " ").replace("\n", " ").strip()


def status_header(target_provider: str | None) -> list[str]:
    header = [
        "disorder",
        "name",
        "category",
        "providers",
        "provider_count",
        "report_count",
        "citation_file_count",
        "latest_provider",
        "latest_end_time",
        "latest_file",
    ]
    if target_provider:
        header.extend(
            [
                "target_provider",
                "has_target_provider",
                "target_provider_reports",
                "target_provider_citation_files",
            ]
        )
    return header


def status_record(row: CoverageRow, target_provider: str | None) -> list[str]:
    latest = row.latest_report
    record = [
        row.disorder.slug,
        row.disorder.name,
        row.disorder.category,
        ",".join(row.providers),
        str(row.provider_count),
        str(row.report_count),
        str(row.citation_file_count),
        latest.provider if latest else "",
        latest.end_time if latest else "",
        str(latest.path) if latest else "",
    ]
    if target_provider:
        provider_reports = row.reports_for_provider(target_provider)
        record.extend(
            [
                target_provider,
                "yes" if provider_reports else "no",
                str(len(provider_reports)),
                str(sum(1 for report in provider_reports if report.citations_exists)),
            ]
        )
    return [tsv_value(value) for value in record]


def filter_rows(
    rows: Sequence[CoverageRow],
    *,
    missing_provider: str | None = None,
    only: set[str] | None = None,
) -> list[CoverageRow]:
    selected: list[CoverageRow] = []
    for row in rows:
        if only and row.disorder.slug not in only:
            continue
        if missing_provider and row.has_provider(missing_provider):
            continue
        selected.append(row)
    return selected


def provider_summary(rows: Sequence[CoverageRow]) -> dict[str, dict[str, int]]:
    summary: dict[str, dict[str, int]] = {}
    for row in rows:
        for provider in row.providers:
            provider_reports = row.reports_for_provider(provider)
            bucket = summary.setdefault(
                provider, {"disorders": 0, "reports": 0, "citation_files": 0}
            )
            bucket["disorders"] += 1
            bucket["reports"] += len(provider_reports)
            bucket["citation_files"] += sum(
                1 for report in provider_reports if report.citations_exists
            )
    return summary


def write_status(
    all_rows: Sequence[CoverageRow],
    displayed_rows: Sequence[CoverageRow],
    *,
    target_provider: str | None,
    missing_provider: str | None,
    out: TextIO,
    include_summary: bool,
) -> None:
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(status_header(target_provider or missing_provider))
    for row in displayed_rows:
        writer.writerow(status_record(row, target_provider or missing_provider))

    if not include_summary:
        return

    with_research = [row for row in all_rows if row.provider_count > 0]
    report_total = sum(row.report_count for row in all_rows)
    citation_file_total = sum(row.citation_file_count for row in all_rows)
    print("# summary", file=out)
    print(f"# disorders_total\t{len(all_rows)}", file=out)
    print(f"# rows_displayed\t{len(displayed_rows)}", file=out)
    print(f"# disorders_with_research\t{len(with_research)}", file=out)
    print(
        f"# disorders_without_research\t{len(all_rows) - len(with_research)}",
        file=out,
    )
    print(f"# reports_total\t{report_total}", file=out)
    print(f"# citation_files_total\t{citation_file_total}", file=out)
    if target_provider or missing_provider:
        provider = target_provider or missing_provider
        assert provider is not None
        missing = [row for row in all_rows if not row.has_provider(provider)]
        print(f"# target_provider\t{provider}", file=out)
        print(f"# target_provider_missing\t{len(missing)}", file=out)
    print("# provider\tdisorders\treports\tcitation_files", file=out)
    for provider, counts in sorted(provider_summary(all_rows).items()):
        print(
            "# provider\t"
            f"{provider}\t{counts['disorders']}\t{counts['reports']}\t"
            f"{counts['citation_files']}",
            file=out,
        )


def build_research_command(
    provider: str, disorder: str, extra_args: Sequence[str]
) -> list[str]:
    if provider == "cyberian-codex":
        return ["just", "research-disorder-cyberian-codex", disorder, *extra_args]
    return ["just", "research-disorder", provider, disorder, *extra_args]


def shell_join(parts: Sequence[str]) -> str:
    return " ".join(subprocess.list2cmdline([part]) for part in parts)


def tail_detail(result: subprocess.CompletedProcess[str]) -> str:
    text = (result.stderr or result.stdout or "").strip()
    if not text:
        return ""
    return text.splitlines()[-1][:500]


def verify_output(
    research_dir: Path, disorder: str, provider: str
) -> tuple[Path, Path, bool]:
    output_file = research_dir / f"{disorder}-deep-research-{provider}.md"
    citations_file = Path(f"{output_file}.citations.md")
    ok = output_file.exists() and output_file.stat().st_size > 0
    return output_file, citations_file, ok


def write_attempt_report(
    attempts: Sequence[RunAttempt], output_dir: Path, provider: str
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    path = output_dir / f"deep_research_missing_{provider}_{timestamp}.tsv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "disorder",
                "provider",
                "status",
                "returncode",
                "duration_seconds",
                "output_file",
                "citations_file",
                "command",
                "detail",
            ]
        )
        for attempt in attempts:
            writer.writerow(
                [
                    attempt.disorder,
                    attempt.provider,
                    attempt.status,
                    attempt.returncode,
                    f"{attempt.duration_seconds:.2f}",
                    attempt.output_file,
                    attempt.citations_file,
                    attempt.command,
                    attempt.detail,
                ]
            )
    return path


def run_missing(
    rows: Sequence[CoverageRow],
    *,
    provider: str,
    research_dir: Path,
    output_dir: Path,
    max_disorders: int | None,
    only: set[str] | None,
    dry_run: bool,
    timeout_seconds: int,
    stop_on_error: bool,
    extra_args: Sequence[str],
) -> int:
    candidates = [
        row
        for row in rows
        if not row.has_provider(provider) and (not only or row.disorder.slug in only)
    ]
    if max_disorders is not None:
        candidates = candidates[:max_disorders]

    print(f"provider={provider}")
    print(f"candidate_disorders={len(candidates)}")

    attempts: list[RunAttempt] = []
    failures = 0
    for index, row in enumerate(candidates, start=1):
        disorder = row.disorder.slug
        command = build_research_command(provider, disorder, extra_args)
        output_file, citations_file, _ok = verify_output(
            research_dir, disorder, provider
        )
        command_text = shell_join(command)
        print(f"[{index}/{len(candidates)}] {disorder}: {command_text}")

        if dry_run:
            attempts.append(
                RunAttempt(
                    disorder=disorder,
                    provider=provider,
                    status="DRY_RUN",
                    returncode=0,
                    duration_seconds=0.0,
                    output_file=str(output_file),
                    citations_file=str(citations_file),
                    command=command_text,
                    detail="",
                )
            )
            continue

        started = time.monotonic()
        try:
            result = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
            duration = time.monotonic() - started
            output_file, citations_file, verified = verify_output(
                research_dir, disorder, provider
            )
            if result.returncode == 0 and verified:
                status = "OK"
            elif result.returncode == 0:
                status = "MISSING_OUTPUT"
                failures += 1
            else:
                status = f"ERROR_{result.returncode}"
                failures += 1
            attempt = RunAttempt(
                disorder=disorder,
                provider=provider,
                status=status,
                returncode=result.returncode,
                duration_seconds=duration,
                output_file=str(output_file),
                citations_file=str(citations_file),
                command=command_text,
                detail=tail_detail(result),
            )
        except subprocess.TimeoutExpired:
            duration = time.monotonic() - started
            failures += 1
            attempt = RunAttempt(
                disorder=disorder,
                provider=provider,
                status="TIMEOUT",
                returncode="timeout",
                duration_seconds=duration,
                output_file=str(output_file),
                citations_file=str(citations_file),
                command=command_text,
                detail=f"timeout after {timeout_seconds}s",
            )

        attempts.append(attempt)
        print(
            f"    status={attempt.status} duration={attempt.duration_seconds:.1f}s "
            f"detail={attempt.detail}"
        )
        if failures and stop_on_error:
            break

    report_path = write_attempt_report(attempts, output_dir, provider)
    ok_count = sum(1 for attempt in attempts if attempt.status == "OK")
    dry_count = sum(1 for attempt in attempts if attempt.status == "DRY_RUN")
    print(
        "summary: "
        f"ok={ok_count} dry_run={dry_count} failures={failures} report={report_path}"
    )
    return 1 if failures else 0


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--kb-dir", default="kb/disorders", type=Path)
    parser.add_argument("--research-dir", default="research", type=Path)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    if argv is None:
        argv = sys.argv[1:]
    if not argv or argv[0].startswith("-"):
        argv = ["status", *argv]
    research_args: list[str] = []
    if argv and argv[0] == "run-missing" and "--" in argv:
        separator_index = list(argv).index("--")
        research_args = list(argv[separator_index + 1 :])
        argv = [*argv[:separator_index]]

    parser = argparse.ArgumentParser(
        description="Report and backfill deep-research provider coverage."
    )
    subparsers = parser.add_subparsers(dest="command")

    status_parser = subparsers.add_parser(
        "status",
        help="Print one TSV row per disorder with deep-research provider coverage.",
    )
    add_common_args(status_parser)
    status_parser.add_argument(
        "--provider",
        help="Add target-provider columns using this deep-research provider slug.",
    )
    status_parser.add_argument(
        "--missing-provider",
        help="Only show disorders missing this deep-research provider slug.",
    )
    status_parser.add_argument("--only", nargs="+", default=None)
    status_parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Only print the TSV table, without comment-prefixed summary lines.",
    )

    run_parser = subparsers.add_parser(
        "run-missing",
        help="Run just research-disorder for disorders missing a provider.",
    )
    add_common_args(run_parser)
    run_parser.add_argument(
        "provider", help="Provider slug, e.g. falcon or openscientist."
    )
    run_parser.add_argument("--output-dir", default="output", type=Path)
    run_parser.add_argument("--max-disorders", type=int, default=None)
    run_parser.add_argument("--only", nargs="+", default=None)
    run_parser.add_argument("--dry-run", action="store_true")
    run_parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=5400,
        help="Per-disorder timeout for the just command.",
    )
    run_parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop after the first failed provider run.",
    )

    args = parser.parse_args(argv)
    if (
        args.command == "status"
        and args.provider
        and args.missing_provider
        and normalize_provider(args.provider)
        != normalize_provider(args.missing_provider)
    ):
        parser.error("--provider and --missing-provider must match when both are set")
    args.research_args = research_args
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    rows = build_coverage(args.kb_dir, args.research_dir)

    if args.command == "status":
        provider = normalize_provider(args.provider) if args.provider else None
        missing_provider = (
            normalize_provider(args.missing_provider) if args.missing_provider else None
        )
        only = set(args.only or [])
        displayed = filter_rows(
            rows,
            missing_provider=missing_provider,
            only=only,
        )
        write_status(
            rows,
            displayed,
            target_provider=provider,
            missing_provider=missing_provider,
            out=sys.stdout,
            include_summary=not args.no_summary,
        )
        return 0

    if args.command == "run-missing":
        only = set(args.only or [])
        return run_missing(
            rows,
            provider=normalize_provider(args.provider),
            research_dir=args.research_dir,
            output_dir=args.output_dir,
            max_disorders=args.max_disorders,
            only=only,
            dry_run=args.dry_run,
            timeout_seconds=args.timeout_seconds,
            stop_on_error=args.stop_on_error,
            extra_args=args.research_args,
        )

    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
