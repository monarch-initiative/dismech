"""Audit first-parent git history for suspicious protected-path merge outcomes."""

from __future__ import annotations

import argparse
import fnmatch
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

DEFAULT_PROTECTED_PATTERNS = (
    ".claude/**",
    ".github/**",
    "src/**",
    "scripts/**",
    "tests/**",
    "conf/**",
    "kb/**",
    "research/**",
    "references_cache/**",
    "CLAUDE.md",
    "AGENTS.md",
    "README.md",
    "justfile",
    "project.justfile",
    "pyproject.toml",
    "uv.lock",
)

DEFAULT_DERIVED_PATTERNS = (
    "pages/**",
    "dashboard/**",
    "details/**",
    "elements/**",
    "docs/schema/**",
    "app/data.js",
)


@dataclass(frozen=True)
class ClassifiedPaths:
    """Paths grouped by audit outcome."""

    protected: tuple[str, ...]
    allowed: tuple[str, ...]
    ignored: tuple[str, ...]
    other: tuple[str, ...]


@dataclass(frozen=True)
class StaleResolution:
    """A protected path whose merge result matched the second parent."""

    path: str
    first_parent_blob: str
    second_parent_blob: str
    result_blob: str


@dataclass(frozen=True)
class MergeAuditRecord:
    """Protected-path findings for a first-parent commit."""

    commit: str
    subject: str
    deleted: ClassifiedPaths
    stale: ClassifiedPaths
    stale_resolutions: tuple[StaleResolution, ...]


def _run_git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=check,
        capture_output=True,
        text=True,
    )
    return result.stdout


def _try_run_git(repo: Path, *args: str) -> str | None:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def _matches_any(path: str, patterns: tuple[str, ...]) -> bool:
    return any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)


def _parse_name_status(name_status_output: str) -> tuple[tuple[str, tuple[str, ...]], ...]:
    records: list[tuple[str, tuple[str, ...]]] = []
    for raw_line in name_status_output.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        records.append((parts[0], tuple(parts[1:])))
    return tuple(records)


def _parse_deleted_paths(name_status_output: str) -> tuple[str, ...]:
    deleted_paths: list[str] = []
    for status, paths in _parse_name_status(name_status_output):
        if status == "D" and paths:
            deleted_paths.append(paths[-1])
    return tuple(deleted_paths)


def _parse_changed_paths(name_status_output: str) -> tuple[str, ...]:
    changed_paths: list[str] = []
    for _status, paths in _parse_name_status(name_status_output):
        if paths:
            changed_paths.append(paths[-1])
    return tuple(dict.fromkeys(changed_paths))


def load_allow_patterns(path: Path | None) -> tuple[str, ...]:
    """Load optional allowlisted path patterns from a text file."""
    if path is None or not path.exists():
        return ()

    patterns: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if line:
            patterns.append(line)
    return tuple(patterns)


def classify_paths(
    paths: tuple[str, ...],
    *,
    protected_patterns: tuple[str, ...] = DEFAULT_PROTECTED_PATTERNS,
    derived_patterns: tuple[str, ...] = DEFAULT_DERIVED_PATTERNS,
    allow_patterns: tuple[str, ...] = (),
) -> ClassifiedPaths:
    """Classify paths into protected, allowed, derived, and other buckets."""
    protected: list[str] = []
    allowed: list[str] = []
    ignored: list[str] = []
    other: list[str] = []

    for path in paths:
        if _matches_any(path, derived_patterns):
            ignored.append(path)
        elif _matches_any(path, allow_patterns):
            allowed.append(path)
        elif _matches_any(path, protected_patterns):
            protected.append(path)
        else:
            other.append(path)

    return ClassifiedPaths(
        protected=tuple(protected),
        allowed=tuple(allowed),
        ignored=tuple(ignored),
        other=tuple(other),
    )


def classify_deleted_paths(
    deleted_paths: tuple[str, ...],
    *,
    protected_patterns: tuple[str, ...] = DEFAULT_PROTECTED_PATTERNS,
    derived_patterns: tuple[str, ...] = DEFAULT_DERIVED_PATTERNS,
    allow_patterns: tuple[str, ...] = (),
) -> ClassifiedPaths:
    """Backward-compatible wrapper for deletion-specific callers."""
    return classify_paths(
        deleted_paths,
        protected_patterns=protected_patterns,
        derived_patterns=derived_patterns,
        allow_patterns=allow_patterns,
    )


def deleted_paths_for_merge_commit(repo: Path, commit: str) -> tuple[str, ...]:
    """Return deleted paths from a commit's first-parent diff."""
    output = _run_git(
        repo,
        "show",
        "--first-parent",
        "--find-renames",
        "--name-status",
        "--format=",
        commit,
    )
    return _parse_deleted_paths(output)


def deleted_paths_for_range(repo: Path, base: str, head: str) -> tuple[str, ...]:
    """Return deleted paths between two refs."""
    output = _run_git(
        repo,
        "diff",
        "--find-renames",
        "--name-status",
        base,
        head,
    )
    return _parse_deleted_paths(output)


def _commit_parents(repo: Path, commit: str) -> tuple[str, ...]:
    output = _run_git(repo, "rev-list", "--parents", "-n", "1", commit).strip()
    parts = output.split()
    if not parts:
        return ()
    return tuple(parts[1:])


def _blob_oid(repo: Path, rev: str, path: str) -> str | None:
    output = _try_run_git(repo, "rev-parse", f"{rev}:{path}")
    if output is None:
        return None
    return output.strip()


def stale_resolutions_for_merge_commit(
    repo: Path,
    commit: str,
    *,
    parents: tuple[str, ...] | None = None,
    protected_patterns: tuple[str, ...] = DEFAULT_PROTECTED_PATTERNS,
    allow_patterns: tuple[str, ...] = (),
) -> tuple[StaleResolution, ...]:
    """Return protected paths whose merge result matched the second parent."""
    if parents is None:
        parents = _commit_parents(repo, commit)
    if len(parents) < 2:
        return ()

    first_parent, second_parent = parents[:2]
    changed_output = _run_git(
        repo,
        "diff",
        "--find-renames",
        "--name-status",
        first_parent,
        commit,
    )

    resolutions: list[StaleResolution] = []
    for path in _parse_changed_paths(changed_output):
        if not (
            _matches_any(path, protected_patterns) or _matches_any(path, allow_patterns)
        ):
            continue

        first_parent_blob = _blob_oid(repo, first_parent, path)
        second_parent_blob = _blob_oid(repo, second_parent, path)
        result_blob = _blob_oid(repo, commit, path)
        if (
            first_parent_blob is None
            or second_parent_blob is None
            or result_blob is None
        ):
            continue

        if result_blob == second_parent_blob and result_blob != first_parent_blob:
            resolutions.append(
                StaleResolution(
                    path=path,
                    first_parent_blob=first_parent_blob,
                    second_parent_blob=second_parent_blob,
                    result_blob=result_blob,
                )
            )

    return tuple(resolutions)


def iter_first_parent_history(
    repo: Path,
    *,
    since: str | None = None,
) -> list[tuple[str, tuple[str, ...], str, tuple[str, ...]]]:
    """Return first-parent commits with parents, subject, and deleted paths."""
    args = [
        "log",
        "--first-parent",
        "--diff-merges=first-parent",
        "--name-status",
        "--format=@@@ %H\t%P\t%s",
    ]
    if since:
        args.insert(1, f"--since={since}")

    records: list[tuple[str, tuple[str, ...], str, tuple[str, ...]]] = []
    current_commit: str | None = None
    current_parents: tuple[str, ...] = ()
    current_subject: str | None = None
    current_deleted: list[str] = []

    for raw_line in _run_git(repo, *args).splitlines():
        if raw_line.startswith("@@@ "):
            if current_commit is not None and current_subject is not None:
                records.append(
                    (
                        current_commit,
                        current_parents,
                        current_subject,
                        tuple(current_deleted),
                    )
                )
            commit, parents_text, subject = raw_line[4:].split("\t", 2)
            current_commit = commit
            current_parents = tuple(parent for parent in parents_text.split() if parent)
            current_subject = subject
            current_deleted = []
            continue

        line = raw_line.strip()
        if not line:
            continue

        parts = line.split("\t")
        if parts[0] == "D" and len(parts) >= 2:
            current_deleted.append(parts[1])

    if current_commit is not None and current_subject is not None:
        records.append(
            (
                current_commit,
                current_parents,
                current_subject,
                tuple(current_deleted),
            )
        )

    return records


def inspect_merge_commit(
    repo: Path,
    commit: str,
    *,
    allow_patterns: tuple[str, ...] = (),
) -> MergeAuditRecord:
    """Inspect one first-parent commit for protected merge outcomes."""
    subject = _run_git(repo, "show", "-s", "--format=%s", commit).strip()
    deleted_paths = deleted_paths_for_merge_commit(repo, commit)
    stale_resolutions = stale_resolutions_for_merge_commit(
        repo,
        commit,
        allow_patterns=allow_patterns,
    )
    return MergeAuditRecord(
        commit=commit,
        subject=subject,
        deleted=classify_paths(deleted_paths, allow_patterns=allow_patterns),
        stale=classify_paths(
            tuple(resolution.path for resolution in stale_resolutions),
            allow_patterns=allow_patterns,
        ),
        stale_resolutions=stale_resolutions,
    )


def scan_merge_history(
    repo: Path,
    *,
    since: str | None = None,
    allow_patterns: tuple[str, ...] = (),
) -> list[MergeAuditRecord]:
    """Scan first-parent history for protected merge-outcome findings."""
    records: list[MergeAuditRecord] = []
    for commit, parents, subject, deleted_paths in iter_first_parent_history(
        repo,
        since=since,
    ):
        stale_resolutions = stale_resolutions_for_merge_commit(
            repo,
            commit,
            parents=parents,
            allow_patterns=allow_patterns,
        )
        record = MergeAuditRecord(
            commit=commit,
            subject=subject,
            deleted=classify_paths(deleted_paths, allow_patterns=allow_patterns),
            stale=classify_paths(
                tuple(resolution.path for resolution in stale_resolutions),
                allow_patterns=allow_patterns,
            ),
            stale_resolutions=stale_resolutions,
        )
        if record.deleted.protected or record.stale.protected:
            records.append(record)
    return records


def _print_classified(label: str, paths: tuple[str, ...]) -> None:
    if not paths:
        return
    print(f"{label}:")
    for path in paths:
        print(f"  - {path}")


def _filter_stale_resolutions(
    stale_resolutions: tuple[StaleResolution, ...],
    paths: tuple[str, ...],
) -> tuple[StaleResolution, ...]:
    selected = set(paths)
    return tuple(
        resolution
        for resolution in stale_resolutions
        if resolution.path in selected
    )


def _print_stale_resolutions(
    label: str,
    stale_resolutions: tuple[StaleResolution, ...],
) -> None:
    if not stale_resolutions:
        return
    print(f"{label}:")
    for resolution in stale_resolutions:
        print(
            "  - "
            f"{resolution.path} "
            f"(result {resolution.result_blob[:12]} matched second parent "
            f"{resolution.second_parent_blob[:12]}, not first parent "
            f"{resolution.first_parent_blob[:12]})"
        )


def _check_merge_commit_command(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    allow_patterns = load_allow_patterns(
        Path(args.allowlist_file).resolve() if args.allowlist_file else None
    )
    record = inspect_merge_commit(repo, args.commit, allow_patterns=allow_patterns)

    if not any(
        (
            record.deleted.protected,
            record.deleted.allowed,
            record.deleted.ignored,
            record.deleted.other,
            record.stale.protected,
            record.stale.allowed,
        )
    ):
        print(f"No protected-path audit findings in {record.commit}.")
        return 0

    print(f"Commit: {record.commit}")
    print(f"Subject: {record.subject}")
    _print_classified("Blocked protected deletions", record.deleted.protected)
    _print_classified("Allowlisted deletions", record.deleted.allowed)
    _print_classified("Ignored derived deletions", record.deleted.ignored)
    _print_classified("Other deletions", record.deleted.other)
    _print_stale_resolutions(
        "Blocked stale-side protected-file wins",
        _filter_stale_resolutions(record.stale_resolutions, record.stale.protected),
    )
    _print_stale_resolutions(
        "Allowlisted stale-side wins",
        _filter_stale_resolutions(record.stale_resolutions, record.stale.allowed),
    )

    if record.deleted.protected or record.stale.protected:
        print(
            "\nRefusing merge because protected paths were deleted or a protected "
            "file resolved to the second-parent version. If the outcome is "
            "intentional, add an exact path or glob to the allowlist file."
        )
        return 1

    return 0


def _check_range_command(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    allow_patterns = load_allow_patterns(
        Path(args.allowlist_file).resolve() if args.allowlist_file else None
    )
    deleted_paths = deleted_paths_for_range(repo, args.base, args.head)
    classified = classify_paths(deleted_paths, allow_patterns=allow_patterns)

    print(f"Range: {args.base}..{args.head}")
    _print_classified("Blocked protected deletions", classified.protected)
    _print_classified("Allowlisted deletions", classified.allowed)
    _print_classified("Ignored derived deletions", classified.ignored)
    _print_classified("Other deletions", classified.other)

    if classified.protected:
        print(
            "\nProtected paths were deleted in this range. "
            "If that is intentional, add an exact path or glob to the allowlist file."
        )
        return 1

    return 0


def _scan_history_command(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    allow_patterns = load_allow_patterns(
        Path(args.allowlist_file).resolve() if args.allowlist_file else None
    )
    records = scan_merge_history(repo, since=args.since, allow_patterns=allow_patterns)

    print(
        f"Protected-path finding commits: {len(records)}"
        + (f" since {args.since}" if args.since else "")
    )
    for record in records[: args.limit]:
        print(f"\n{record.commit}\t{record.subject}")
        _print_classified("Blocked protected deletions", record.deleted.protected)
        _print_stale_resolutions(
            "Blocked stale-side protected-file wins",
            _filter_stale_resolutions(record.stale_resolutions, record.stale.protected),
        )
        _print_classified("Allowlisted deletions", record.deleted.allowed)
        _print_stale_resolutions(
            "Allowlisted stale-side wins",
            _filter_stale_resolutions(record.stale_resolutions, record.stale.allowed),
        )

    if len(records) > args.limit:
        print(f"\n... truncated {len(records) - args.limit} additional commit(s)")

    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_merge_commit = subparsers.add_parser(
        "check-merge-commit",
        help="Inspect one commit's first-parent diff for protected merge outcomes.",
    )
    check_merge_commit.add_argument("commit", nargs="?", default="HEAD")
    check_merge_commit.add_argument("--repo", default=".")
    check_merge_commit.add_argument(
        "--allowlist-file",
        default=".github/protected-path-deletions-allowlist.txt",
    )
    check_merge_commit.set_defaults(func=_check_merge_commit_command)

    check_range = subparsers.add_parser(
        "check-range",
        help="Inspect a base..head range for protected deletions.",
    )
    check_range.add_argument("base")
    check_range.add_argument("head")
    check_range.add_argument("--repo", default=".")
    check_range.add_argument(
        "--allowlist-file",
        default=".github/protected-path-deletions-allowlist.txt",
    )
    check_range.set_defaults(func=_check_range_command)

    scan_history = subparsers.add_parser(
        "scan-history",
        help="Scan first-parent history for protected merge outcomes.",
    )
    scan_history.add_argument("--repo", default=".")
    scan_history.add_argument("--since")
    scan_history.add_argument("--limit", type=int, default=50)
    scan_history.add_argument(
        "--allowlist-file",
        default=".github/protected-path-deletions-allowlist.txt",
    )
    scan_history.set_defaults(func=_scan_history_command)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
