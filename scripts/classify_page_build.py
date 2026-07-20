#!/usr/bin/env python3
"""Classify a push's changed files into a full vs incremental page build.

The ``generate-pages`` workflow renders ~1,700 pages on every trigger. Most
pushes change a single disorder YAML, so re-rendering everything is wasteful.
This classifier decides whether the disorder-page render (``just gen-pages``)
must be **full** — because a change could alter every page's HTML — or may be
**incremental** — rendering only the changed ``kb/disorders/*.yaml`` pages while
the cheap aggregate/index pages regenerate regardless (see issue #5507).

Design invariant: **never silently under-build.** Anything that is not a
recognized local page input or a known render-neutral companion forces a full
rebuild, as do deletions of page inputs and any uncomputable diff.

Classification (per changed path):

- GLOBAL  -> full: touches the render pipeline / schema / build config, so every
  page could change. ``src/**``, ``project.justfile``/``justfile``, ``conf/**``,
  or *any path not matched by a LOCAL or NEUTRAL rule* (unknown => full).
- LOCAL   -> incremental page input: ``kb/disorders/*.yaml``,
  ``kb/comorbidities/*.yaml``, ``kb/modules/*.yaml``, ``research/*.md``. Only the
  disorder files become individual re-renders; comorbidity/module/research
  changes are covered by the always-regenerated aggregates.
- NEUTRAL -> ignored: render-neutral companions of a curation edit and derived
  outputs (``references_cache/**``, ``history/**``, ``cache/**``,
  ``kb/groupings/**`` [separate workflow], ``docs/**``, ``mkdocs.yml``,
  ``pages/**``, ``dashboard/**``, ``elements/**``, ``app/**``, ``.github/**``,
  ``scripts/**``, ``*.history.yaml``, top-level ``*.md``).

A deletion (``D``) or rename (``R``) of a LOCAL page input forces full so stale
pages are removed.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --- classification rules (order does not matter; GLOBAL wins, then LOCAL) ----

GLOBAL_PREFIXES = (
    "src/",
    "conf/",
)
GLOBAL_EXACT = (
    "project.justfile",
    "justfile",
)

NEUTRAL_PREFIXES = (
    "references_cache/",
    "cache/",
    "history/",
    "kb/groupings/",
    "docs/",
    "pages/",
    "dashboard/",
    "elements/",
    "app/",
    ".github/",
    "scripts/",
)
NEUTRAL_EXACT = (
    "mkdocs.yml",
)


def _is_local_disorder(path: str) -> bool:
    return (
        path.startswith("kb/disorders/")
        and path.endswith(".yaml")
        and not path.endswith(".history.yaml")
        and "/" not in path[len("kb/disorders/"):]
    )


def _is_local_page_input(path: str) -> bool:
    if _is_local_disorder(path):
        return True
    for prefix in ("kb/comorbidities/", "kb/modules/"):
        if (
            path.startswith(prefix)
            and path.endswith(".yaml")
            and not path.endswith(".history.yaml")
            and "/" not in path[len(prefix):]
        ):
            return True
    if (
        path.startswith("research/")
        and path.endswith(".md")
        and "/" not in path[len("research/"):]
    ):
        return True
    return False


def _is_neutral(path: str) -> bool:
    if path.endswith(".history.yaml"):
        return True
    if path.startswith(NEUTRAL_PREFIXES):
        return True
    if path in NEUTRAL_EXACT:
        return True
    # Top-level markdown/readme etc. never feeds page rendering.
    if "/" not in path and path.endswith(".md"):
        return True
    return False


def _is_global(path: str) -> bool:
    return path.startswith(GLOBAL_PREFIXES) or path in GLOBAL_EXACT


@dataclass
class Decision:
    mode: str  # "full" | "incremental"
    disorder_files: list[str] = field(default_factory=list)
    reasons: list[str] = field(default_factory=list)


def classify(entries: list[tuple[str, str]]) -> Decision:
    """Classify (status, path) diff entries into a build Decision.

    ``status`` is a git name-status letter (``A``/``M``/``D``/``R``...); ``path``
    is repo-relative. Returns the build mode plus the disorder YAML paths to
    render when incremental.
    """
    disorder_files: set[str] = set()
    reasons: list[str] = []

    for status, path in entries:
        status = (status or "").strip().upper()
        deleted_or_renamed = status.startswith("D") or status.startswith("R")

        if _is_global(path):
            reasons.append(f"global input changed: {path}")
            continue
        if _is_local_page_input(path):
            if deleted_or_renamed and (
                path.startswith(("kb/disorders/", "kb/comorbidities/", "kb/modules/"))
                or path.startswith("research/")
            ):
                reasons.append(f"page input {status} (removed/renamed): {path}")
                continue
            if _is_local_disorder(path):
                disorder_files.add(path)
            # comorbidity/module/research changes ride the always-run aggregates
            continue
        if _is_neutral(path):
            continue
        # Unknown path -> fail safe to a full rebuild.
        reasons.append(f"unrecognized path (fail-safe to full): {path}")

    if reasons:
        return Decision(mode="full", reasons=reasons)
    return Decision(mode="incremental", disorder_files=sorted(disorder_files))


def _git_name_status(base: str, head: str) -> list[tuple[str, str]]:
    out = subprocess.run(
        ["git", "diff", "--name-status", "-z", f"{base}", f"{head}"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    # -z output: records separated by NUL; a rename record is
    # STATUS \0 OLDPATH \0 NEWPATH, others are STATUS \0 PATH.
    tokens = out.split("\0")
    entries: list[tuple[str, str]] = []
    i = 0
    while i < len(tokens):
        status = tokens[i]
        if not status:
            i += 1
            continue
        if status[0] in ("R", "C"):
            # rename/copy: consume old + new path; classify the new path
            newpath = tokens[i + 2] if i + 2 < len(tokens) else ""
            entries.append((status, newpath))
            i += 3
        else:
            path = tokens[i + 1] if i + 1 < len(tokens) else ""
            entries.append((status, path))
            i += 2
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Base git ref/SHA")
    parser.add_argument("--head", help="Head git ref/SHA")
    parser.add_argument(
        "--github-output",
        action="store_true",
        help="Append mode to $GITHUB_OUTPUT for workflow consumption.",
    )
    parser.add_argument(
        "--files-out",
        metavar="PATH",
        help=(
            "Write the changed disorder YAML paths (newline-delimited) to PATH. "
            "Robust to spaces/quotes in filenames; consumed by "
            "'render --changed-from PATH'."
        ),
    )
    args = parser.parse_args()

    # Fail safe: without a computable range, do a full build.
    decision: Decision
    if not args.base or not args.head or set(args.base) == {"0"}:
        decision = Decision(mode="full", reasons=["no computable diff range"])
    else:
        try:
            entries = _git_name_status(args.base, args.head)
            decision = classify(entries)
        except subprocess.CalledProcessError as exc:
            decision = Decision(
                mode="full", reasons=[f"git diff failed: {exc.stderr.strip()}"]
            )

    files_str = " ".join(decision.disorder_files)
    for reason in decision.reasons:
        print(f"[classify] {reason}", file=sys.stderr)
    print(
        f"[classify] mode={decision.mode} "
        f"disorder_files={len(decision.disorder_files)}",
        file=sys.stderr,
    )

    if args.files_out:
        Path(args.files_out).write_text(
            "\n".join(decision.disorder_files) + ("\n" if decision.disorder_files else ""),
            encoding="utf-8",
        )

    if args.github_output and os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write(f"mode={decision.mode}\n")

    print(f"mode={decision.mode}")
    print(f"files={files_str}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
