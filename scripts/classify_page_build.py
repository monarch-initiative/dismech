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

``--check-page-drift`` is a second, diff-independent mode used *after* an
incremental render: it reports whether the rendered ``pages/disorders/*.html``
count still matches the ``kb/disorders/*.yaml`` count, and the workflow escalates
to a full rebuild when it does not. Incremental builds are scoped to one push's
``event.before..sha`` range, but ``concurrency.cancel-in-progress: false``
collapses queued runs, so the disorder YAMLs of a collapsed push are never
rendered — while ``app/data.js`` (always rebuilt in full) picks them up anyway.
That drift is what left 205 dead browser links in PR #7903; the count mismatch is
the cheap, always-available signal that it has happened.

The check runs *after* rendering on purpose. Before the render, a push that adds
a disorder always shows one more YAML than page, so a pre-render check would
escalate every curation push to full and defeat the incremental build entirely.
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
    return bool(path.startswith("research/") and path.endswith(".md") and "/" not in path[len("research/"):])


def _is_neutral(path: str) -> bool:
    if path.endswith(".history.yaml"):
        return True
    if path.startswith(NEUTRAL_PREFIXES):
        return True
    if path in NEUTRAL_EXACT:
        return True
    # Top-level markdown/readme etc. never feeds page rendering.
    return bool("/" not in path and path.endswith(".md"))


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
        deleted_or_renamed = status.startswith(("D", "R"))

        if _is_global(path):
            reasons.append(f"global input changed: {path}")
            continue
        if _is_local_page_input(path):
            if deleted_or_renamed and (
                path.startswith(("kb/disorders/", "kb/comorbidities/", "kb/modules/", "research/"))
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


def count_disorder_inputs(disorders_dir: Path) -> int:
    """Count the ``kb/disorders/*.yaml`` files that each render one page."""
    return sum(
        1
        for path in disorders_dir.glob("*.yaml")
        if not path.name.endswith(".history.yaml")
    )


def count_rendered_pages(pages_dir: Path) -> int:
    """Count the rendered ``pages/disorders/*.html`` files."""
    return sum(1 for _ in pages_dir.glob("*.html"))


def detect_page_drift(disorders_dir: Path, pages_dir: Path) -> str | None:
    """Return a reason to force a full build when pages have drifted from the KB.

    Page filenames are ``slugify(disease name).html`` and slugs are unique, so
    the KB and the rendered page set are 1:1 in a healthy tree *once the current
    build's pages have been written*. Any inequality then means an earlier
    incremental build under- or over-rendered; a full rebuild is the only thing
    that heals it. A missing directory also fails safe to full.
    """
    if not pages_dir.is_dir():
        return f"rendered pages directory missing: {pages_dir}"
    if not disorders_dir.is_dir():
        return f"disorder input directory missing: {disorders_dir}"
    n_inputs = count_disorder_inputs(disorders_dir)
    n_pages = count_rendered_pages(pages_dir)
    if n_inputs != n_pages:
        return (
            f"page/KB drift: {n_inputs} {disorders_dir}/*.yaml vs "
            f"{n_pages} {pages_dir}/*.html (delta {n_inputs - n_pages:+d})"
        )
    return None


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


def _report_page_drift(args: argparse.Namespace) -> int:
    """Run the standalone post-render drift check and report it to the workflow."""
    drift = detect_page_drift(args.disorders_dir, args.pages_dir)
    if drift:
        print(f"[drift] {drift}", file=sys.stderr)
        print(
            "[drift] escalating to a full page rebuild; app/data.js is built "
            "from the whole KB and would otherwise link to unrendered pages.",
            file=sys.stderr,
        )
    else:
        print("[drift] rendered pages match the disorder KB.", file=sys.stderr)

    if args.github_output and os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write(f"drift={'true' if drift else 'false'}\n")

    print(f"drift={'true' if drift else 'false'}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Base git ref/SHA")
    parser.add_argument("--head", help="Head git ref/SHA")
    parser.add_argument(
        "--github-output",
        action="store_true",
        help=(
            "Append the result to $GITHUB_OUTPUT for workflow consumption "
            "(mode=..., or drift=... under --check-page-drift)."
        ),
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
    parser.add_argument(
        "--check-page-drift",
        action="store_true",
        help=(
            "Post-render mode: ignore the diff and report whether the rendered "
            "page count matches the disorder-YAML count. Emits drift=true|false "
            "(with --github-output) so the workflow can escalate to a full "
            "rebuild. Exit code is 0 either way; drift is a signal, not an error."
        ),
    )
    parser.add_argument(
        "--disorders-dir",
        type=Path,
        default=Path("kb/disorders"),
        help="Disorder YAML directory for --check-page-drift.",
    )
    parser.add_argument(
        "--pages-dir",
        type=Path,
        default=Path("pages/disorders"),
        help="Rendered disorder-page directory for --check-page-drift.",
    )
    args = parser.parse_args()

    if args.check_page_drift:
        return _report_page_drift(args)

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
