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
incremental render: it asks whether the rendered ``pages/disorders/*.html`` still
correspond to ``kb/disorders/*.yaml``, and the workflow escalates to a full
rebuild when they do not. Incremental builds are scoped to one push's
``event.before..sha`` range, but ``concurrency.cancel-in-progress: false``
collapses queued runs, so the disorder YAMLs of a collapsed push are never
rendered — while ``app/data.js`` (always rebuilt in full) picks them up anyway.
That drift is what left 205 dead browser links in PR #7903.

The check has **two tiers**, and both must pass:

1. **Count drift** — ``N`` YAMLs vs ``N`` pages. Catches a disorder that was
   added or removed without its page following.
2. **Content drift** — every page is stamped with a digest of the YAML it was
   rendered from (``render`` computes ``sha256(yaml)[:12]`` and the template
   emits it as ``"yamlRevision"``), so comparing that stamp against the current
   file says whether a page is *current*, not merely *present*. This also
   catches the slug-changing rename that tier 1 is documented as blind to.

Tier 2 exists because tier 1 is blind to the far more common failure. A build's
checkout is a snapshot; a KB merge landing mid-build is simply absent from it,
and an incremental render only touches its own push's disorders. The result is a
page whose content predates its YAML while the file counts stay perfectly equal
— invisible to a count check, and permanent, because the regen branch is rebuilt
from ``main``'s already-stale pages on every subsequent run and force-pushed over
whatever a full rebuild had corrected.

That is not hypothetical: on 2026-08-07 it left 29 disorder pages stale (1871
YAMLs, 1871 pages, zero count drift) including the whole environmental-pathograph
backfill of #8085, and destroyed a manually dispatched full rebuild that had
already fixed them (#8140). With tier 2, the next run after any such regression
detects it and escalates to a full rebuild, which makes the pipeline
self-healing: a stale snapshot can still be published, but it can no longer
*persist*.

The check runs *after* rendering on purpose. Before the render, a push that adds
a disorder always shows one more YAML than page, so a pre-render check would
escalate every curation push to full and defeat the incremental build entirely.

Note this module is no longer stdlib-only: heal planning has to predict page
filenames, so it imports the renderer's own ``slugify`` rather than keeping a
private copy that could silently diverge from it. Both call sites (the workflow
and the test suite) run under ``uv`` with the project synced, so ``dismech`` is
importable; run it the same way.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# The renderer's own slug rule, not a copy of it: deciding whether a targeted
# re-render would land on exactly the stale pages means predicting page
# filenames, and a private reimplementation here would be the sixth copy the
# docstring on ``slugify`` was written to stamp out.
from dismech.export.utils import slugify
from dismech.yaml_io import safe_load_path

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


#: Pages in the disorder directory that do not correspond to a disorder YAML.
#: ``render._prune_orphan_pages`` keeps these (``keep_names``), so counting them
#: would leave the KB and page counts permanently unequal and escalate every
#: build to full forever. None exists today; this keeps that true if one lands.
NON_DISORDER_PAGES = frozenset({"index.html"})


def count_rendered_pages(pages_dir: Path) -> int:
    """Count the rendered per-disorder ``pages/disorders/*.html`` files."""
    return sum(
        1 for path in pages_dir.glob("*.html") if path.name not in NON_DISORDER_PAGES
    )


#: ``render._render_disorder`` stamps every page with
#: ``sha256(<source yaml bytes>).hexdigest()[:12]``, surfaced in the page's
#: ``OS_CONFIG`` JSON as ``"yamlRevision": "<hex>"``. Comparing that against a
#: freshly computed digest of ``kb/disorders/<file>.yaml`` says whether the page
#: is *current*, not merely *present*.
#:
#: Why the stamp and not the ``<pre class="yaml-preview">`` block, which also
#: holds the source verbatim: the renderer pipes its HTML through
#: ``_strip_line_end_whitespace``, so a KB entry with trailing whitespace on any
#: line (``Muenke_Syndrome.yaml`` has one) embeds *slightly* altered YAML and
#: would never compare equal — a permanent false positive escalating every build
#: to full forever. The stamp is hex computed before that pass, so it is immune
#: to it and to the ``trailing-whitespace`` pre-commit hook alike.
_YAML_REVISION_RE = re.compile(r'"yamlRevision":\s*"([0-9a-f]+)"')

#: Digest prefix length used by the renderer's stamp. Comparisons truncate the
#: freshly computed digest to match; 48 bits over ~1,900 entries makes an
#: accidental collision (~1e-8) far less likely than the drift being real.
_REVISION_PREFIX_LEN = 12

#: How many drifted page names to name in the reason string before truncating.
#: The full list goes to stderr; this keeps the one-line summary readable.
_MAX_NAMED_DRIFT = 12


def extract_page_revision(page_text: str) -> str | None:
    """Return the source-YAML revision stamp a rendered disorder page carries.

    Takes the **last** match, not the first. The template emits the verbatim
    source YAML (``yaml-preview``) *before* the ``OS_CONFIG`` block that carries
    the stamp, so a KB entry whose own text happened to contain
    ``"yamlRevision": "<hex>"`` would otherwise shadow the real one. No page in
    the KB does today — all 1,871 yield exactly one match — but the failure
    would be a silent wrong answer rather than an error, so it is worth not
    depending on that.

    ``None`` when the page has no stamp — a page rendered before the stamp
    existed, or a truncated write. The caller treats that as drift rather than
    as a pass: a page that cannot prove it is current is assumed stale, which
    costs one re-render and then self-corrects.
    """
    matches = _YAML_REVISION_RE.findall(page_text)
    return matches[-1] if matches else None


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:_REVISION_PREFIX_LEN]


def detect_page_content_drift(
    disorders_dir: Path, pages_dir: Path
) -> tuple[list[str], list[str]]:
    """Compare each rendered page against the KB entry it should have come from.

    Returns ``(stale_pages, unrendered_inputs)``. Matching is by revision stamp
    rather than by filename, so it needs no copy of the renderer's slug rule and
    cannot drift from it: a page is current exactly when its stamp equals the
    digest of some current ``kb/disorders/*.yaml``.

    That also catches the rename the count check is documented as blind to — a
    disorder renamed to a new slug leaves an orphan page whose stamp matches no
    current input while the totals stay equal.

    The two lists are near-mirrors in practice (a stale page's KB file shows up
    as unrendered), but they mean different things: a stale page has *outdated*
    content, an unrendered input has *no* page carrying its content.
    """
    inputs_by_digest: dict[str, str] = {}
    for path in sorted(disorders_dir.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue
        inputs_by_digest[_digest(path.read_text(encoding="utf-8"))] = path.name

    stale: list[str] = []
    matched: set[str] = set()
    for path in sorted(pages_dir.glob("*.html")):
        if path.name in NON_DISORDER_PAGES:
            continue
        revision = extract_page_revision(
            path.read_text(encoding="utf-8", errors="replace")
        )
        if revision is not None and revision in inputs_by_digest:
            matched.add(inputs_by_digest[revision])
        else:
            stale.append(path.name)

    unrendered = sorted(set(inputs_by_digest.values()) - matched)
    return stale, unrendered


def detect_page_drift(
    disorders_dir: Path,
    pages_dir: Path,
    content_drift: tuple[list[str], list[str]] | None = None,
) -> str | None:
    """Return a reason to force a full build when pages have drifted from the KB.

    Two tiers, cheapest first (see the module docstring). Tier 1 compares counts:
    page filenames are ``slugify(disease name).html`` and slugs are unique, so
    the KB and the rendered page set are 1:1 in a healthy tree *once the current
    build's pages have been written*. Tier 2 compares content, catching the stale
    page that keeps the counts equal. A missing directory fails safe to full.

    ``content_drift`` accepts an already-computed
    :func:`detect_page_content_drift` result so a caller that also needs it for
    logging or heal planning reads the ~1,900-page tree once instead of once per
    question. Omit it and it is computed on demand.
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

    stale, unrendered = (
        content_drift
        if content_drift is not None
        else detect_page_content_drift(disorders_dir, pages_dir)
    )
    if stale or unrendered:
        named = ", ".join(stale[:_MAX_NAMED_DRIFT])
        if len(stale) > _MAX_NAMED_DRIFT:
            named += f", +{len(stale) - _MAX_NAMED_DRIFT} more"
        return (
            f"page content drift: {len(stale)} rendered page(s) do not match "
            f"their {disorders_dir}/*.yaml source, {len(unrendered)} input(s) "
            f"unrepresented (counts agree at {n_inputs}, so this is staleness, "
            f"not a missing page): {named}"
        )
    return None


def _expected_page_name(disorder_path: Path) -> str | None:
    """Return the page filename a disorder YAML renders to, or ``None``.

    ``None`` when the file cannot be read or carries no ``name``, which the
    caller treats as "cannot predict the repair" and escalates to a full build.
    """
    try:
        data = safe_load_path(disorder_path) or {}
    except Exception:  # unparseable YAML: fail safe rather than guess
        return None
    name = data.get("name")
    return f"{slugify(name)}.html" if name else None


def plan_heal(
    disorders_dir: Path,
    pages_dir: Path,
    content_drift: tuple[list[str], list[str]] | None = None,
) -> tuple[str, list[str]]:
    """Decide how to repair detected drift, and with which inputs.

    Returns ``(strategy, disorder_paths)`` where strategy is ``"targeted"`` or
    ``"full"``. A full rebuild repairs anything but costs 30-60 minutes; simply
    re-rendering the stale entries was measured at 1m28s for the 29 that the
    2026-08-07 incident left behind. Since drift is now detected on a busy repo
    far more often than it used to be, healing at full cost every time would
    make the fix too expensive to keep switched on.

    The whole decision is one question: **a targeted render rewrites exactly the
    pages the unrendered inputs map to, so is every stale page one of those?** If
    a stale page is not going to be rewritten, it survives the repair as an orphan
    and only a full build — which prunes — can clear it.

    That single subset test subsumes the cases it is tempting to special-case:

    - *Pure staleness* (a page whose source moved on): the drifted input maps
      straight back onto the stale page. Targeted.
    - *A disorder added mid-build*: nothing is stale, one input has no page yet.
      The empty set is a subset of anything, so this is targeted — and it matters,
      because re-anchoring makes a mid-build addition the *common* case, and
      gating on equal counts would have made a second full rebuild the common
      response to it.
    - *A rename*: one stale page, one unrendered input, but the input writes the
      *new* slug and leaves the old page orphaned. Not a subset. Full.
    - *A deletion*: the page outlives its input, nothing will rewrite it. Full.

    Counting inputs against pages is the right *drift* signal (see
    :func:`detect_page_drift`) but the wrong *repair* signal: it cannot tell an
    addition, which a targeted render fixes, from a deletion, which it cannot.

    Callers should still re-check after a targeted heal and escalate if drift
    survives; this predicts the repair, it does not verify it.

    ``content_drift`` reuses an already-computed
    :func:`detect_page_content_drift` result, as in :func:`detect_page_drift`.
    """
    if not pages_dir.is_dir() or not disorders_dir.is_dir():
        return "full", []

    stale, unrendered = (
        content_drift
        if content_drift is not None
        else detect_page_content_drift(disorders_dir, pages_dir)
    )
    if not stale and not unrendered:
        return "targeted", []

    expected_pages: set[str] = set()
    for name in unrendered:
        page_name = _expected_page_name(disorders_dir / name)
        if page_name is None:
            return "full", []
        expected_pages.add(page_name)
    if not set(stale) <= expected_pages:
        return "full", []

    return "targeted", [str(disorders_dir / name) for name in unrendered]


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
    # Scanned once and threaded through both questions below: the tree is ~1,900
    # pages, and asking "is there drift", "which pages" and "how do we repair it"
    # separately would read all of them three times.
    content_drift = (
        detect_page_content_drift(args.disorders_dir, args.pages_dir)
        if args.disorders_dir.is_dir() and args.pages_dir.is_dir()
        else None
    )

    drift = detect_page_drift(args.disorders_dir, args.pages_dir, content_drift)
    heal, heal_files = ("none", [])
    if drift:
        print(f"[drift] {drift}", file=sys.stderr)
        # The summary truncates; CI logs are the only place a curator can see
        # which pages were actually stale, so name every one of them here.
        if content_drift is not None:
            stale, unrendered = content_drift
            for name in stale:
                print(f"[drift]   stale page: {name}", file=sys.stderr)
            for name in unrendered:
                print(f"[drift]   unrendered input: {name}", file=sys.stderr)
        heal, heal_files = plan_heal(
            args.disorders_dir, args.pages_dir, content_drift
        )
        if heal == "targeted" and heal_files:
            print(
                f"[drift] repairable by re-rendering {len(heal_files)} stale "
                "entr(y/ies); a full rebuild is not required.",
                file=sys.stderr,
            )
        else:
            heal = "full"
            print(
                "[drift] escalating to a full page rebuild; app/data.js is "
                "built from the whole KB and would otherwise link to "
                "unrendered pages, and only a full build prunes orphan pages.",
                file=sys.stderr,
            )
    else:
        print("[drift] rendered pages match the disorder KB.", file=sys.stderr)

    if args.stale_files_out:
        Path(args.stale_files_out).write_text(
            "\n".join(heal_files) + ("\n" if heal_files else ""),
            encoding="utf-8",
        )

    if args.github_output and os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write(f"drift={'true' if drift else 'false'}\n")
            handle.write(f"heal={heal}\n")

    print(f"drift={'true' if drift else 'false'}")
    print(f"heal={heal}")
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
            "pages still match the disorder KB, by count AND by each page's "
            "embedded source-YAML revision stamp (a page can be present but "
            "stale). Emits drift=true|false plus heal=targeted|full|none (with "
            "--github-output) so the workflow can repair proportionally. Exit "
            "code is 0 either way; drift is a signal, not an error."
        ),
    )
    parser.add_argument(
        "--stale-files-out",
        metavar="PATH",
        help=(
            "With --check-page-drift: write the disorder YAML paths whose pages "
            "are stale (newline-delimited) to PATH, for a targeted re-render via "
            "'gen-pages-changed-from'. Written empty when a full rebuild is "
            "needed instead; pair it with the heal=targeted|full output."
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
