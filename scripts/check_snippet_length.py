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
occurrences without first cleaning up the backlog, current findings are
grandfathered in ``tests/snippet_length_baseline.txt``. ``--check`` (the
default) fails only on findings NOT in the baseline. Regenerate with
``--update-baseline`` after intentionally changing the set.

Usage
-----
    python scripts/check_snippet_length.py            # gate: fail on NEW ones
    python scripts/check_snippet_length.py --all      # list every finding
    python scripts/check_snippet_length.py --count    # summary counts
    python scripts/check_snippet_length.py --update-baseline
"""

from __future__ import annotations

import argparse
import re
import sys
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


def scan_repo(scan_dir: Path = SCAN_DIR, schema_path: Path | None = None):
    """Return a sorted list of ``(relpath, location, words, snippet)`` findings."""
    excerpt_fields, reference_fields = discover_field_names(
        schema_path if schema_path is not None else ROOT / DEFAULT_SCHEMA
    )
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for location, words, snippet in find_violations(
            path, data, excerpt_fields, reference_fields
        ):
            findings.append((rel, location, words, snippet))
    return findings


def _baseline_key(rel: str, snippet: str) -> str:
    # Keyed on (file, snippet text) rather than on the YAML location, which
    # shifts whenever a list above it grows. Same convention as the
    # folded-hyphen baseline.
    #
    # Whitespace is collapsed first: the baseline file is line-oriented, so a
    # snippet carrying an embedded newline (plenty do -- YAML plain scalars wrap)
    # would otherwise span two lines on write and never match on read.
    return f"{rel}\t{' '.join(snippet.split())}"


def load_baseline(path: Path = BASELINE_PATH) -> set[str]:
    if not path.exists():
        return set()
    keys = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            keys.add(line)
    return keys


def write_baseline(findings, path: Path = BASELINE_PATH) -> None:
    keys = sorted({_baseline_key(rel, snippet) for rel, _, _, snippet in findings})
    header = (
        "# Grandfathered short evidence snippets (see "
        "scripts/check_snippet_length.py).\n"
        "# Each line is `path<TAB>snippet`. New snippets under "
        f"{MIN_SNIPPET_WORDS} words that are\n"
        "# NOT listed here fail the guard. Remove entries as the backlog is\n"
        "# fixed; do not add new ones. Regenerate with:\n"
        "#   just update-snippet-length-baseline\n"
    )
    path.write_text(header + "\n".join(keys) + "\n", encoding="utf-8")


def new_findings(findings, baseline: set[str]):
    return [f for f in findings if _baseline_key(f[0], f[3]) not in baseline]


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
        baseline = load_baseline()
        files = {rel for rel, _, _, _ in findings}
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(f"baseline entries: {len(baseline)}")
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        return 0

    baseline = load_baseline()
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
        print("(ORPHA/ClinGen/ICEES/NCIT tables) are exempt. If a finding is")
        print("genuinely unavoidable, run --update-baseline to grandfather it.")
        return 1
    print(
        f"OK: no new snippets under {MIN_SNIPPET_WORDS} words "
        f"({len(baseline)} grandfathered in baseline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
