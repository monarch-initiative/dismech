#!/usr/bin/env python3
"""Guard against evidence snippets that merely quote the paper's title.

An evidence ``snippet`` is supposed to be the sentence from the cited source
that *makes the claim*. A title is not that sentence::

    evidence:
    - reference: PMID:22906614
      supports: SUPPORT
      snippet: "Risk factors for multiple sclerosis: decreased vitamin D level
        and remote Epstein-Barr virus infection in the pre-clinical phase of
        multiple sclerosis."
      explanation: The title directly states that decreased vitamin D levels...

A title records **that a question was examined, not what was found**. It states
the paper's conclusion in the author's most compressed and least qualified
form, stripped of effect size, direction, population and hedging -- and a
"Risk factors for X" title does not even do that much, it just names the topic.

The failure mode here is **overstatement, not fabrication** (issue #8374), and
it is invisible to every other check we have: the snippet is exact text from the
real reference, over the five-word minimum, correctly attributed, and
``count-verified-snippets`` verifies it happily because a title *is* in the
cached file. Nothing looks at what the text is *of*.

This check is deliberately mechanical. Whether a given title states a *result*
("Chronic recurrent stress ... does not precipitate Graves' disease") rather
than a *topic* is a judgement, and #8374 records both kinds; the detector flags
the shape and leaves the judgement to the curator and the baseline.

Note there is deliberately no per-item opt-out keyed on the ``explanation``
text. The obvious marker -- an explanation that says the title states the
finding -- appears on the *motivating bad example* in #8374 ("The title directly
states that..."), so it would waive precisely what this exists to catch.

Signal
------
A reference/snippet pair whose snippet, normalised, either equals the ``title:``
recorded in that reference's cache file or is a contiguous fragment of it.

Two exemptions:

* **Structured-database rows.** A quoted row from an Orphanet, ClinGen, ICEES
  or NCIT cache file is pipe-delimited and often resembles that record's title,
  but it is a data row rather than prose. The shape test is imported from
  :mod:`scripts.check_snippet_length` so the two guards cannot drift apart on
  what counts as a structured row.
* **Uncached references and cache files with no title.** Nothing to compare
  against; not this check's job to gate on cache coverage. A folded-scalar
  ``title: >-`` would also read as no title here (the captured value is ``>-``,
  which normalises away), which is a miss rather than a false positive -- and
  there are no such cache files today.
* **Dataset accessions.** See :data:`_LITERATURE_PREFIXES`.

Reading the baseline: not every ``fragment`` finding is a curator quoting a
title. Around twenty are ORPHA records where the quoted text is a genuine
``## Inheritance`` bullet (``Autosomal dominant``) that happens to be a word-run
inside the record's own title. Each is 2-3 words, so the five-word length guard
already blocks new ones; they are grandfathered here rather than being worth
extra logic.

A record holding only metadata is *not* exempt, though #8374 lists it as an
honest use. Whether a cached record carries a real abstract or just a citation
block is not cleanly decidable: measured over the findings in ``kb/``, residual
prose length after stripping the title and bibliographic scaffolding is
continuous (19 / 32 / 31 / 33 / 30 / 211 across 0-9, 10-24, 25-39, 40-59, 60-119
and 120+ words), with no gap to put a threshold in. Rather than encode an
arbitrary cut, the guard flags the shape and the failure message names both
remedies -- quote the abstract sentence, or, when there is no abstract to quote,
change the source or drop the evidence block.

Near-matches are deliberately *not* flagged. Measured over ``kb/``, the band
just below an exact match is dominated by abstract sentences that legitimately
restate the title in different words ("Expression of ROS1 *correlates with*
..." against a title reading "*predicts*"), which is exactly the quoting this
check wants to encourage.

Baseline ratchet
----------------
A pre-existing backlog already lives in ``kb/``. It is grandfathered the same
way :mod:`scripts.check_snippet_length` grandfathers short snippets, and for the
same reason: to gate *new* occurrences without blocking on a cleanup.

``--against-ref REF`` (env ``TITLE_SNIPPET_BASELINE_REF``) derives the baseline
live from ``kb/`` at a git ref -- CI passes the base branch, so the base branch
is green by construction and parallel merges have nothing to clobber. Titles are
resolved against the *working tree* cache in both cases: ``references_cache/``
holds tens of thousands of files and archiving it per run would cost far more
than it buys, and a title that genuinely changed under a reference is a cache
regeneration worth surfacing as a new finding rather than hiding.

``tests/title_snippet_baseline.txt`` is the committed fallback for local runs
and shallow checkouts.

Usage
-----
    python scripts/check_title_snippets.py                           # gate
    python scripts/check_title_snippets.py --against-ref origin/main
    python scripts/check_title_snippets.py --all
    python scripts/check_title_snippets.py --count
    python scripts/check_title_snippets.py --update-baseline
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
if str(ROOT) not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT))

from dismech.frontmatter import split_frontmatter
from dismech.reference_snippet_audit import (
    DEFAULT_SCHEMA,
    CachedReferenceIndex,
    discover_field_names,
    iter_snippet_pairs,
)
from dismech.yaml_io import safe_load

# Single-sourced so the two snippet guards agree on what a structured-source row
# is; diverging on that would make one of them wrong about the same snippet.
from scripts.check_snippet_length import is_structured_row

#: Reference prefixes whose records are dataset accessions rather than papers.
#: Sourced from the reference validator's own `skip_prefixes`, minus DOI --
#: `conf/reference_validator_config.yaml` skips DOI because it cannot *fetch*
#: those, not because they are not literature, and a DOI record is a real paper
#: whose title must stay checked. A dataset record's cached body is frequently
#: its title verbatim, so "quote the abstract sentence instead" is unsatisfiable
#: in a way the editorial case is not: an editorial has an underlying study to
#: cite in its place.
_VALIDATOR_CONFIG = ROOT / "conf" / "reference_validator_config.yaml"
#: Case-folded, because the config lists several prefixes in *both* cases
#: (`geo`/`GEO`, `morphic`/`MORPHIC`, `pride`/`PRIDE`). Adding a lowercase `doi`
#: alongside the existing `DOI` -- the established pattern in that file -- would
#: otherwise slip past a case-sensitive comparison and silently exempt the one
#: prefix this carve-out exists to protect.
#:
#: Folded here rather than written pre-folded, so growing this set cannot
#: reintroduce that bug by someone spelling a new entry the way the config does.
_LITERATURE_PREFIXES = frozenset(prefix.casefold() for prefix in ("DOI",))

SCAN_DIR = ROOT / "kb"
CACHE_DIR = ROOT / "references_cache"
BASELINE_PATH = ROOT / "tests" / "title_snippet_baseline.txt"
BASELINE_REF_ENV = "TITLE_SNIPPET_BASELINE_REF"

#: ``title:`` in a cache file's YAML frontmatter. Anchored to the line start so a
#: ``title:`` occurring inside the abstract body cannot be mistaken for it.
_TITLE_RE = re.compile(r"^title:[ \t]*(.+)$", re.MULTILINE)

_PUNCT_RE = re.compile(r"[^\w\s]")


def dataset_prefixes(config_path: Path = _VALIDATOR_CONFIG) -> frozenset[str]:
    """Case-folded reference prefixes that name a dataset rather than a paper."""
    try:
        config = safe_load(config_path.read_text(encoding="utf-8")) or {}
    except OSError:
        return frozenset()
    skipped = config.get("skip_prefixes") or []
    return frozenset(
        str(prefix).casefold()
        for prefix in skipped
        if str(prefix).casefold() not in _LITERATURE_PREFIXES
    )


def normalize(text: str) -> str:
    """Fold a title or snippet to its comparable form.

    Case, surrounding quotes, punctuation, a trailing period and whitespace runs
    all vary freely between a cache file's ``title:`` line and a curator's
    transcription of it, and none of them changes whether the snippet *is* the
    title.
    """
    text = text.strip().strip('"').strip("'")
    text = _PUNCT_RE.sub(" ", text)
    return " ".join(text.split()).casefold()


def title_of(cache_path: Path) -> str | None:
    """The ``title:`` recorded in a cache file's frontmatter, if any."""
    try:
        head = cache_path.read_text(encoding="utf-8", errors="replace")[:8192]
    except OSError:
        return None
    split = split_frontmatter(head)
    if split is None:
        return None
    match = _TITLE_RE.search(split.frontmatter)
    if match is None:
        return None
    # Surrounding quotes are YAML syntax, not part of the title.
    title = match.group(1).strip().strip('"').strip("'").strip()
    return title or None


def classify(snippet: str, title: str) -> str | None:
    """``"title"``, ``"fragment"`` or ``None`` for a snippet against a title."""
    normalized_snippet = normalize(snippet)
    normalized_title = normalize(title)
    if not normalized_snippet or not normalized_title:
        return None
    if normalized_snippet == normalized_title:
        return "title"
    # A fragment of the title carries no more than the title does. Compared on
    # word boundaries so a short snippet cannot match mid-word.
    if f" {normalized_snippet} " in f" {normalized_title} ":
        return "fragment"
    return None


def find_violations(path, data, excerpt_fields, reference_fields, index, datasets=None):
    """Yield ``(location, kind, snippet)`` for title-quoting snippets in *data*."""
    if datasets is None:
        datasets = dataset_prefixes()
    for pair in iter_snippet_pairs(path, data, excerpt_fields, reference_fields):
        snippet = pair.snippet.strip()
        if not snippet or is_structured_row(snippet):
            continue
        prefix, _, _ = str(pair.reference_id).partition(":")
        if prefix.casefold() in datasets:
            continue
        cache_path = index.resolve_cache_path(pair.reference_id)
        if cache_path is None:
            continue
        title = title_of(cache_path)
        if title is None:
            continue
        kind = classify(snippet, title)
        if kind is not None:
            yield (pair.location, kind, snippet)


def scan_repo(
    scan_dir: Path = SCAN_DIR,
    schema_path: Path | None = None,
    rel_to: Path = ROOT,
    cache_dir: Path = CACHE_DIR,
):
    """Return sorted ``(relpath, location, kind, snippet)`` findings."""
    excerpt_fields, reference_fields = discover_field_names(
        schema_path if schema_path is not None else ROOT / DEFAULT_SCHEMA
    )
    index = CachedReferenceIndex(cache_dir)
    datasets = dataset_prefixes()
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception as exc:
            # Gating on malformed YAML is `validate-all`'s job; skipping silently
            # would make the file invisible here rather than merely unchecked.
            print(
                f"warning: skipping unparseable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        rel = path.relative_to(rel_to).as_posix()
        for location, kind, snippet in find_violations(
            path, data, excerpt_fields, reference_fields, index, datasets
        ):
            findings.append((rel, location, kind, snippet))
    return findings


def _baseline_key(rel: str, snippet: str) -> str:
    # Keyed on (file, snippet text), not the YAML location, which shifts whenever
    # a list above it grows. Whitespace is collapsed because the baseline file is
    # line-oriented and plenty of snippets wrap across lines.
    return f"{rel}\t{' '.join(snippet.split())}"


def count_by_key(findings) -> Counter:
    """How many times each ``(file, snippet)`` appears in *findings*."""
    return Counter(_baseline_key(rel, snippet) for rel, _, _, snippet in findings)


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    """Read the baseline as ``{key: grandfathered occurrence count}``.

    The count matters for the same reason it does in the length guard: one
    title pasted across several unrelated claims is worse than one, and a plain
    set of keys would let the extra ones through.
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
        else:
            counts[line] = counts.get(line, 0) + 1
    return counts


def write_baseline(findings, path: Path = BASELINE_PATH) -> None:
    counts = count_by_key(findings)
    header = (
        "# Grandfathered title-quoting evidence snippets (see\n"
        "# scripts/check_title_snippets.py and issue #8374).\n"
        "# Each line is `count<TAB>path<TAB>snippet`, where count is how many\n"
        "# times that snippet is cited in that file. A snippet that repeats its\n"
        "# reference's title fails the guard if it is absent here OR appears MORE\n"
        "# often than the count recorded. Remove entries as the backlog is fixed;\n"
        "# adding one is only right for a title that states a result rather than\n"
        "# a topic, and that belongs in the PR description. Regenerate with:\n"
        "#   just update-title-snippet-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def baseline_from_ref(ref: str, root: Path = ROOT) -> Counter | None:
    """Baseline derived live from ``kb/`` at a git *ref*.

    Titles are resolved against the working-tree cache -- see the module
    docstring for why the cache is not archived alongside. Returns ``None`` if
    *ref* cannot be read, so the caller falls back to the committed baseline.
    """
    scan_rel = SCAN_DIR.relative_to(ROOT).as_posix()
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "archive", "--format=tar", ref, "--", scan_rel],
            capture_output=True,
            check=False,
        )
    except (FileNotFoundError, OSError) as exc:
        print(
            f"title-snippet baseline: git archive for {ref!r} could not run: {exc}",
            file=sys.stderr,
        )
        return None
    if proc.returncode != 0:
        detail = (
            proc.stderr.decode("utf-8", "replace").strip() or f"exit {proc.returncode}"
        )
        print(
            f"title-snippet baseline: git archive {ref!r} failed: {detail}",
            file=sys.stderr,
        )
        return None
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        try:
            with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tar:
                tar.extractall(tmp_path, filter="data")
        except tarfile.TarError as exc:
            print(
                f"title-snippet baseline: unreadable archive for {ref!r}: {exc}",
                file=sys.stderr,
            )
            return None
        findings = scan_repo(scan_dir=tmp_path / scan_rel, rel_to=tmp_path)
    return count_by_key(findings)


def resolve_baseline(ref: str | None = None) -> Counter:
    """Live from *ref* when given and readable, else the committed baseline."""
    if ref is None:
        ref = os.environ.get(BASELINE_REF_ENV) or None
    if ref:
        from_ref = baseline_from_ref(ref)
        if from_ref is not None:
            print(
                f"title-snippet baseline: grandfathered against ref {ref!r} "
                f"({len(from_ref)} distinct snippet(s))",
                file=sys.stderr,
            )
            return from_ref
        print(
            f"title-snippet baseline: could not read ref {ref!r}; "
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
            "grandfather against the title-quoting snippets present in kb/ at "
            f"this git ref instead of the committed baseline (env: "
            f"{BASELINE_REF_ENV}). CI uses the base branch so it is green by "
            "construction."
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
        for rel, location, kind, snippet in findings:
            print(f"{rel}:{location}: {kind}: {snippet!r}")
        print(f"\n{len(findings)} snippet(s) quoting their reference's title.")
        return 0

    if args.count:
        baseline = resolve_baseline(args.against_ref)
        files = {rel for rel, _, _, _ in findings}
        kinds = Counter(kind for _, _, kind, _ in findings)
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(f"  exact title: {kinds['title']}   title fragment: {kinds['fragment']}")
        print(
            f"baseline: {len(baseline)} distinct snippet(s), "
            f"{sum(baseline.values())} grandfathered occurrence(s)"
        )
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        return 0

    baseline = resolve_baseline(args.against_ref)
    new = new_findings(findings, baseline)
    if new:
        print("New evidence snippet(s) quoting the reference's title detected.")
        print("A title records that a question was examined, not what was found:")
        print("it drops effect size, direction, population and hedging, and a")
        print('"Risk factors for X" title only names the topic.\n')
        print("Quote the sentence from the abstract that states the finding. If")
        print("the cached record has no abstract -- editorials and comments often")
        print("cache as metadata alone -- then re-quoting cannot fix it: cite the")
        print("study itself, or drop the evidence block and keep the description")
        print("(CLAUDE.md, 'When Evidence Cannot Be Verified').\n")
        for rel, location, kind, snippet in new:
            print(f"{rel}:{location}: {kind}: {snippet!r}")
        print(f"\n{len(new)} new finding(s). Structured-source rows are exempt.")
        if args.against_ref or os.environ.get(BASELINE_REF_ENV):
            # A ref baseline (CI) never reads the committed file, so
            # --update-baseline would pass locally and still fail CI.
            print("Grandfathering is unavailable when checking against a ref:")
            print("quote the abstract sentence instead.")
        else:
            print("A title that states a *result* rather than a topic is a")
            print("legitimate snippet; grandfather it with --update-baseline and")
            print("say why in the PR.")
        return 1
    print(
        f"OK: no new title-quoting snippets ({sum(baseline.values())} occurrence(s) "
        f"of {len(baseline)} distinct snippet(s) grandfathered in baseline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
