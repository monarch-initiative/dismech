#!/usr/bin/env python3
"""Guard against degenerate (too-short) evidence snippets.

An evidence ``snippet`` is supposed to be the sentence from the cited source
that *makes the claim*. A bare noun does not::

    phenotypes:
    - name: Strabismus
      evidence:
      - reference: DOI:10.1016/j.molcel.2021.11.031
        snippet: 'Strabismus'

That carries no propositional content: it cannot support or refute anything, and
it cannot be checked in any meaningful way even when it does happen to appear in
the cached text. Issue #7450 found a cluster of these lifted from a clinical-
features *table* (whose cells do not survive text extraction, so they are also
unverifiable by construction), including one file where the single word
``'Hearing loss'`` was reused as the evidence for a phenotype *and* for two
unrelated treatments -- which a word plainly cannot evidence.

This check is deliberately independent of reference fetching, caching, and the
``skip_prefixes`` question that surfaced it: it needs nothing but the YAML, and
it would have caught the cluster above with no network at all.

Signal
------
A reference/snippet pair whose snippet holds fewer than
:data:`MIN_SNIPPET_WORDS` words.

Structured-database rows are exempt. A quoted row from an Orphanet, ClinGen,
ICEES, or NCIT cache file (``HP:0001987 | Hyperammonemia | Very frequent
(99-80%)``) is short in words but fully propositional, and its pipe-delimited
shape identifies it unambiguously.

Baseline ratchet
----------------
A large pre-existing backlog already lives in ``kb/``. To let this gate *new*
occurrences without first cleaning up the backlog, the current findings are
grandfathered. ``--check`` (the default) fails only on findings NOT in the
baseline. There are two ways to source that baseline:

* ``--against-ref REF`` (env ``SNIPPET_BASELINE_REF``) derives it *live* from
  the short snippets already in ``kb/`` at a git ref -- CI sets it to the base
  branch (``origin/main``). Nothing is stored, so the base branch is green by
  construction and parallel merges have nothing to clobber. This is the primary
  path in CI.
* ``tests/snippet_length_baseline.txt`` is the committed fallback used when no
  ref is given or the ref can't be read (local runs, shallow checkouts, forks).
  It is a *best-effort* snapshot: CI no longer reads it, so it may lag ``main``
  and can produce local-only spurious findings until regenerated with
  ``--update-baseline``.

Usage
-----
    python scripts/check_snippet_length.py                        # gate: fail on NEW ones
    python scripts/check_snippet_length.py --against-ref origin/main  # grandfather vs a ref
    python scripts/check_snippet_length.py --all                 # list every finding
    python scripts/check_snippet_length.py --count               # summary counts
    python scripts/check_snippet_length.py --update-baseline
"""

from __future__ import annotations

import argparse
import io
import os
import re
import subprocess
import sys
import tarfile
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from dismech.reference_snippet_audit import (
    DEFAULT_SCHEMA,
    discover_field_names,
    iter_snippet_pairs,
)
from dismech.yaml_io import safe_load

SCAN_DIR = ROOT / "kb"
BASELINE_PATH = ROOT / "tests" / "snippet_length_baseline.txt"

# When set (CI sets it to ``origin/main``), the grandfather baseline is derived
# live from that git ref instead of the committed snapshot file -- see
# baseline_from_ref(). This makes the base branch green by construction and
# leaves nothing for parallel merges to clobber (issue #7450 follow-up).
BASELINE_REF_ENV = "SNIPPET_BASELINE_REF"

# Fewer than five words is the line issue #7450 drew, on the reasoning that a
# quote that short is almost never a claim -- it is a label.
MIN_SNIPPET_WORDS = 5

# A token counts as a word if it contains a letter or a digit, so "c.142G" and
# "18F-FDOPA" count once and stray punctuation counts for nothing.
_WORD_RE = re.compile(r"[^\s]*[A-Za-z0-9][^\s]*")

# A pipe-delimited row quoted out of a structured-source cache file.
_TABLE_ROW_RE = re.compile(r"\S\s*\|\s*\S")


def count_words(snippet: str) -> int:
    """Number of word-like tokens in *snippet*."""
    return len(_WORD_RE.findall(snippet))


def is_structured_row(snippet: str) -> bool:
    """True for a pipe-delimited row quoted from a structured-source cache."""
    return bool(_TABLE_ROW_RE.search(snippet))


def find_violations(path: Path, data, excerpt_fields, reference_fields):
    """Yield ``(location, words, snippet)`` for too-short snippets in *data*."""
    for pair in iter_snippet_pairs(path, data, excerpt_fields, reference_fields):
        snippet = pair.snippet.strip()
        if is_structured_row(snippet):
            continue
        words = count_words(snippet)
        if words < MIN_SNIPPET_WORDS:
            yield (pair.location, words, snippet)


def scan_repo(
    scan_dir: Path = SCAN_DIR,
    schema_path: Path | None = None,
    rel_to: Path = ROOT,
):
    """Return a sorted list of ``(relpath, location, words, snippet)`` findings.

    ``rel_to`` is the base the reported relative paths are computed against. It
    defaults to :data:`ROOT` for the working tree, but :func:`baseline_from_ref`
    scans an extracted copy of ``kb/`` under a temp dir and passes that dir so
    the reported paths still come out as ``kb/disorders/X.yaml`` -- matching the
    working-tree keys the baseline is compared on.
    """
    excerpt_fields, reference_fields = discover_field_names(
        schema_path if schema_path is not None else ROOT / DEFAULT_SCHEMA
    )
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception as exc:
            # Not this check's job to gate on malformed YAML (`validate-all`
            # does that), but skipping silently would make the file invisible
            # here rather than merely unchecked.
            print(
                f"warning: skipping unparseable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        rel = path.relative_to(rel_to).as_posix()
        for location, words, snippet in find_violations(
            path, data, excerpt_fields, reference_fields
        ):
            findings.append((rel, location, words, snippet))
    return findings


def _baseline_key(rel: str, snippet: str) -> str:
    # Keyed on (file, snippet text) rather than on the YAML location, which
    # shifts whenever a list above it grows.
    #
    # Whitespace is collapsed first: the baseline file is line-oriented, so a
    # snippet carrying an embedded newline (plenty do -- YAML plain scalars wrap)
    # would otherwise span two lines on write and never match on read.
    return f"{rel}\t{' '.join(snippet.split())}"


def count_by_key(findings) -> Counter:
    """How many times each ``(file, snippet)`` appears in *findings*."""
    return Counter(_baseline_key(rel, snippet) for rel, _, _, snippet in findings)


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    """Read the baseline as ``{key: grandfathered occurrence count}``.

    The count matters. The motivating anti-pattern in #7450 is one bare snippet
    reused across *several* unrelated claims (``'Hearing loss'`` cited for a
    phenotype and two treatments), so a plain set of keys would happily let a
    curator paste an already-baselined snippet a fourth time -- the check would
    be blind to precisely what it exists to catch.
    """
    counts: Counter = Counter()
    if not path.exists():
        return counts
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        count, tab, key = line.partition("\t")
        if tab and count.isdigit():
            counts[key] = int(count)
        else:  # tolerate a pre-count baseline
            counts[line] = counts.get(line, 0) + 1
    return counts


def write_baseline(findings, path: Path = BASELINE_PATH) -> None:
    counts = count_by_key(findings)
    header = (
        "# Grandfathered short evidence snippets (see "
        "scripts/check_snippet_length.py).\n"
        "# Each line is `count<TAB>path<TAB>snippet`, where count is how many\n"
        f"# times that snippet is cited in that file. A snippet under "
        f"{MIN_SNIPPET_WORDS} words\n"
        "# fails the guard if it is absent here OR appears MORE often than the\n"
        "# count recorded -- reusing one bare term across extra claims is the\n"
        "# anti-pattern this exists to catch. Remove entries as the backlog is\n"
        "# fixed; do not add new ones. Regenerate with:\n"
        "#   just update-snippet-length-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def baseline_from_ref(ref: str, root: Path = ROOT) -> Counter | None:
    """Grandfather baseline derived live from a git *ref* (e.g. ``origin/main``).

    Returns the per-``(file, snippet)`` occurrence counts of the short snippets
    as they exist in ``kb/`` at *ref* -- i.e. exactly the backlog already on the
    base branch. Because the grandfather set is computed from the base branch
    rather than a committed snapshot, there is nothing to keep in sync and
    nothing for parallel merges to clobber: the base branch is green by
    construction, and a PR fails only on snippets it *adds* over the base.

    Returns ``None`` if *ref* cannot be read (no git, ref absent in a shallow
    checkout, path missing at the ref, ...), so the caller can fall back to the
    committed baseline. On failure git's own stderr is surfaced, so a CI
    misconfiguration (e.g. a stale ``origin/main`` in a shallow checkout) is
    diagnosable rather than a silent capability downgrade.
    """
    # Relative to the real ROOT (always ``kb``), not *root*: tests pass a
    # throwaway repo as *root* while the layout under it is still ``kb/``.
    scan_rel = SCAN_DIR.relative_to(ROOT).as_posix()
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "archive", "--format=tar", ref, "--", scan_rel],
            capture_output=True,
            check=False,  # returncode is handled explicitly below (PLW1510)
        )
    except (FileNotFoundError, OSError) as exc:
        print(f"snippet baseline: git archive for {ref!r} could not run: {exc}",
              file=sys.stderr)
        return None
    if proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", "replace").strip() or f"exit {proc.returncode}"
        print(f"snippet baseline: git archive {ref!r} failed: {detail}", file=sys.stderr)
        return None
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        try:
            with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tar:
                # filter="data" is the safe extraction policy that becomes the
                # default in Python 3.14; set it explicitly to silence the 3.13
                # DeprecationWarning and pin behavior. The archive is git-authored
                # (kb/ only), so "data" never rejects a legitimate member.
                tar.extractall(tmp_path, filter="data")
        except tarfile.TarError as exc:
            # Should be unreachable -- git archive exits non-zero on a bad ref or
            # missing pathspec -- but a truncated/empty stream with returncode 0
            # must degrade to the fallback, never crash the gate.
            print(f"snippet baseline: unreadable archive for {ref!r}: {exc}",
                  file=sys.stderr)
            return None
        findings = scan_repo(scan_dir=tmp_path / scan_rel, rel_to=tmp_path)
    return count_by_key(findings)


def resolve_baseline(ref: str | None = None) -> Counter:
    """The grandfather baseline: live from *ref* when given, else the committed file.

    *ref* defaults to the ``SNIPPET_BASELINE_REF`` environment variable, which CI
    sets to ``origin/main``. If the ref cannot be read, fall back to the
    committed baseline so local runs and shallow checkouts keep working.
    """
    if ref is None:
        ref = os.environ.get(BASELINE_REF_ENV) or None
    if ref:
        from_ref = baseline_from_ref(ref)
        if from_ref is not None:
            # State which baseline engaged: the test/gate behaves differently
            # depending on whether the ref was reachable, so make that legible
            # in CI logs instead of leaving it to be inferred.
            print(
                f"snippet baseline: grandfathered against ref {ref!r} "
                f"({len(from_ref)} distinct snippet(s))",
                file=sys.stderr,
            )
            return from_ref
        print(
            f"snippet baseline: could not read ref {ref!r}; "
            "falling back to the committed baseline",
            file=sys.stderr,
        )
    return load_baseline()


def new_findings(findings, baseline: Counter):
    """Findings not covered by *baseline*, including extra reuses of a known one."""
    seen: Counter = Counter()
    new = []
    for finding in findings:
        key = _baseline_key(finding[0], finding[3])
        seen[key] += 1
        if seen[key] > baseline.get(key, 0):
            new.append(finding)
    return new


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--check", action="store_true", help="(default) fail on non-baselined findings"
    )
    group.add_argument("--all", action="store_true", help="list every finding")
    group.add_argument("--count", action="store_true", help="print summary counts")
    group.add_argument(
        "--update-baseline",
        action="store_true",
        help="rewrite the baseline from current findings",
    )
    parser.add_argument(
        "--against-ref",
        metavar="REF",
        default=None,
        help=(
            "grandfather against the short snippets present in kb/ at this git "
            f"ref instead of the committed baseline (env: {BASELINE_REF_ENV}). "
            "CI uses origin/main so the base branch is green by construction."
        ),
    )
    args = parser.parse_args(argv)

    findings = scan_repo()

    if args.update_baseline:
        write_baseline(findings)
        print(
            f"Wrote baseline with {len(findings)} finding(s) to "
            f"{BASELINE_PATH.relative_to(ROOT)}"
        )
        return 0

    if args.all:
        for rel, location, words, snippet in findings:
            print(f"{rel}:{location}: {words} word(s): {snippet!r}")
        print(f"\n{len(findings)} snippet(s) under {MIN_SNIPPET_WORDS} words.")
        return 0

    if args.count:
        baseline = resolve_baseline(args.against_ref)
        files = {rel for rel, _, _, _ in findings}
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(
            f"baseline: {len(baseline)} distinct snippet(s), "
            f"{sum(baseline.values())} grandfathered occurrence(s)"
        )
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        return 0

    baseline = resolve_baseline(args.against_ref)
    new = new_findings(findings, baseline)
    if new:
        print(f"New evidence snippet(s) under {MIN_SNIPPET_WORDS} words detected.")
        print("A snippet should be the sentence from the source that makes the")
        print("claim. A bare term ('Strabismus') carries no propositional content,")
        print("cannot support or refute anything, and is usually lifted from a")
        print("table whose cells do not survive text extraction. Quote the")
        print("sentence instead, or drop the evidence block and keep the")
        print("description.\n")
        for rel, location, words, snippet in new:
            print(f"{rel}:{location}: {words} word(s): {snippet!r}")
        print(f"\n{len(new)} new finding(s). Pipe-delimited structured-source rows")
        print("(ORPHA/ClinGen/ICEES/NCIT tables) are exempt.")
        if args.against_ref or os.environ.get(BASELINE_REF_ENV):
            # A ref baseline (CI) never reads tests/snippet_length_baseline.txt,
            # so --update-baseline would pass locally, still fail CI, and commit
            # churn to the shared snapshot this ratchet exists to stop touching.
            print("Grandfathering is unavailable when checking against a ref: fix")
            print("the snippet (quote the sentence) or drop the evidence block.")
        else:
            print("If a finding is genuinely unavoidable, run --update-baseline")
            print("to grandfather it.")
        return 1
    print(
        f"OK: no new snippets under {MIN_SNIPPET_WORDS} words "
        f"({sum(baseline.values())} occurrence(s) of {len(baseline)} distinct "
        "snippet(s) grandfathered in baseline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
