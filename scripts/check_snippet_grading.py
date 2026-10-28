#!/usr/bin/env python3
"""Guard against one quoted sentence carrying two different gradings in a file.

``evidence_source`` describes the **publication's** evidence type and ``supports``
describes what the quote does to the claim. Neither is a property of the block
the quote happens to be pasted into, so quoting the *same sentence* from the
*same reference* twice in one file and grading it two different ways is a
contradiction the file itself contains::

    pathophysiology:
    - name: MR-1 Detoxification Failure
      evidence:
      - reference: PMID:15496428
        supports: REFUTE
        evidence_source: COMPUTATIONAL
        snippet: "HAGH functions in a pathway to detoxify methylglyoxal"
    environmental:
    - name: Alcohol
      evidence:
      - reference: PMID:15496428
        supports: SUPPORT              # same sentence, different grading
        evidence_source: HUMAN_CLINICAL
        snippet: "HAGH functions in a pathway to detoxify methylglyoxal"

That is the defect found in ``Paroxysmal_Dyskinesia.yaml`` during the review of
#8293, and the shape flagged in ``Chronic_Obstructive_Pulmonary_Disease.yaml``
after #8182 (four references whose ``influences_mechanisms`` copies were tagged
``OTHER`` while their ``environmental[].evidence`` twins omitted the field, which
reads as its ``HUMAN_CLINICAL`` default).

Why per *sentence* and not per *PMID*
-------------------------------------
Issue #8184 first proposed "one PMID, one ``evidence_source`` per file". That is
wrong, and would fail correct curation: ``PMID:15496428`` is cited five times in
``Paroxysmal_Dyskinesia.yaml`` and legitimately carries ``COMPUTATIONAL`` for its
homology argument and ``HUMAN_CLINICAL`` for its clinical cohort, because CLAUDE.md
already instructs curators to *"split evidence items so each item gets a single
``evidence_source``"* when a paper mixes sources. The invariant that survives that
correction is the narrower one this check implements: a grading belongs to the
quoted sentence, so the same sentence must be graded the same way.

Overlapping quotes count as the same sentence. In the #8293 case the two gradings
quoted *different extents* of one passage -- one started mid-passage, dropping the
homology sentence that justified the ``COMPUTATIONAL`` tag -- so an exact-match
check would have missed it. A snippet that is a substring of another snippet of
the same reference is therefore compared too, provided the shorter one carries at
least :data:`MIN_OVERLAP_WORDS` words (below that a containment is more likely to
be coincidental than quoted).

What this check does NOT decide
------------------------------
Whether a narrative review, systematic review, or epidemiological synthesis
should be ``HUMAN_CLINICAL`` or ``OTHER`` is an open convention question with a
four-month paper trail (#1105, #6997, #8184) and needs a maintainer's sign-off
written into ``docs/explanation/design-decisions.md`` -- not a check. This guard
is deliberately blind to *which* value is right: it only refuses to let one file
assert both about one sentence.

Signal
------
Two evidence items in the same file citing the same reference, whose snippets are
equal or one contained in the other, that disagree on ``evidence_source``.

``evidence_source`` absent counts as ``HUMAN_CLINICAL``, the default CLAUDE.md
documents -- otherwise the COPD case above (omitted vs ``OTHER``) would not be a
finding, and it is the case that motivated the issue.

Why ``supports`` is available but not gated
-------------------------------------------
The invariant as stated in #8184 covers ``supports`` too. Measuring it says
otherwise: across ``kb/`` the same-sentence rule finds **701** ``evidence_source``
divergences and **7,960** ``supports`` divergences, and the ``supports`` ones are
overwhelmingly *correct* curation. ``supports`` is claim-relative by design -- the
issue body says so itself -- so "No beneficial effect was detected after 5 months
with a low protein diet" legitimately reads ``SUPPORT`` for a discussion of
treatment failure and ``REFUTE`` for the treatment entry it counts against.
Gating that would be a 92%-noise ratchet whose baseline enshrines correct work.

Those counts predate the issue #7439 narrowing, which retired ``PARTIAL`` and
took ``supports`` divergences from 8,285 to 353 against 715 for
``evidence_source``. Most of the "claim-relative" signal was the retired value's
ambiguity rather than genuine claim-relativity, so the argument above for leaving
``supports`` ungated is now much weaker and is worth revisiting.

So ``supports`` is scanned on request (``--fields supports`` / ``--fields all``)
as a triage view, and only ``evidence_source`` is gated. Whether the
``supports``-on-one-sentence rule should ever become a gate needs a curator to
look at that 7,960 first; this is the measurement, not the answer.

Across files (#11221)
---------------------
The same reasoning holds across entries: the grading belongs to the quoted
sentence, so the same sentence of the same reference cited from two different
files should carry one ``evidence_source``. The KB-wide comparison groups every
evidence item by reference, compares items from *different* files with the same
same-quote rule, and sorts each divergent pair into one of two classes:

* **gated** -- ``HUMAN_CLINICAL`` against ``IN_VITRO``, ``MODEL_ORGANISM`` or
  ``COMPUTATIONAL``. A sentence describing a cell assay, an animal result or a
  simulation cannot also be a human clinical observation, so one of the two
  files is wrong. These fail the gate unless grandfathered.
* **report-only** -- every other divergent pair, chiefly any pair involving
  ``OTHER``. Whether a review, a database lookup or a structured-source row is
  ``HUMAN_CLINICAL`` or ``OTHER`` is the open convention question in #10273, so
  gating it now would freeze an undecided call into a baseline. These are
  listed by ``--all --cross-file`` and never fail.

Its limits are the same as the per-file check's, widened to the corpus: it
compares one verbatim sentence (or a contained extent of it). Two *different*
sentences making the same claim are not compared, and neither are two
sentences of one reference that carry different values, which is the
documented outcome for a paper that mixes sources.

Neither class decides which of the two files is right. That is a curator's
call, made by reading the cited paper; the check never re-grades anything.

Baseline ratchet
----------------
A pre-existing backlog already lives in ``kb/``. As with the length and title
guards, the current findings are grandfathered so this gates *new* divergences
without requiring the backlog be cleaned first. Two baseline sources:

* ``--against-ref REF`` (env ``SNIPPET_GRADING_BASELINE_REF``) derives it live
  from ``kb/`` at a git ref -- CI sets it to the base branch, so the base branch
  is green by construction and parallel merges have nothing to clobber.
* ``tests/snippet_grading_baseline.txt`` is the committed fallback for local
  runs, shallow checkouts, and forks.

The gated cross-file pairs have their own baseline,
``tests/snippet_grading_cross_file_baseline.txt``, keyed on both paths, and are
grandfathered against the same ref. A PR therefore fails only on a pair it
introduces, never on one already present in two files it did not touch.
Renaming or moving an entry changes its key, so its pairs read as new.

Usage
-----
    python scripts/check_snippet_grading.py                            # gate
    python scripts/check_snippet_grading.py --against-ref origin/main  # vs a ref
    python scripts/check_snippet_grading.py --all                      # list all
    python scripts/check_snippet_grading.py --all --cross-file         # across files
    python scripts/check_snippet_grading.py --count --fields all       # census
    python scripts/check_snippet_grading.py --update-baseline
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
from typing import Any, NamedTuple

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from dismech.disk_full import reports_disk_full
from dismech.reference_snippet_audit import (
    DEFAULT_SCHEMA,
    discover_field_names,
)
from dismech.yaml_io import safe_load

SCAN_DIR = ROOT / "kb"
BASELINE_PATH = ROOT / "tests" / "snippet_grading_baseline.txt"
CROSS_FILE_BASELINE_PATH = ROOT / "tests" / "snippet_grading_cross_file_baseline.txt"

# When set (CI sets it to ``origin/<base>``), the grandfather baseline is derived
# live from that git ref instead of the committed snapshot -- see
# baseline_from_ref().
BASELINE_REF_ENV = "SNIPPET_GRADING_BASELINE_REF"

#: The graded slots on ``EvidenceItem``, mapped to the value an absent field
#: means. ``evidence_source`` has a documented default (CLAUDE.md: "HUMAN_CLINICAL
#: for direct human observations (default when not specified)"); ``supports`` does
#: not, so ``None`` means "do not compare this item on this field".
GRADING_DEFAULTS: dict[str, str | None] = {
    "evidence_source": "HUMAN_CLINICAL",
    "supports": None,
}

#: The subset of :data:`GRADING_DEFAULTS` the gate actually fails on. ``supports``
#: is scanned only on request -- see "Why ``supports`` is available but not gated".
GATED_FIELDS: tuple[str, ...] = ("evidence_source",)

#: Minimum words in the shorter snippet for a *containment* (as opposed to an
#: exact match) to be treated as the same quote. A three-word fragment appearing
#: inside a longer quote of the same paper is more plausibly a coincidence than a
#: re-quote, and the length guard already rejects snippets that short.
MIN_OVERLAP_WORDS = 5

#: ``evidence_source`` pairs that cannot both be right for one sentence, and so
#: gate when they appear in two different files. Every other divergent pair is
#: reported only -- see "Across files (#11221)".
GATED_CROSS_FILE_PAIRS: frozenset[frozenset[str]] = frozenset(
    frozenset({"HUMAN_CLINICAL", other})
    for other in ("IN_VITRO", "MODEL_ORGANISM", "COMPUTATIONAL")
)

_WORD_RE = re.compile(r"[^\s]*[A-Za-z0-9][^\s]*")


class GradedSnippet(NamedTuple):
    """One evidence item's reference, quote, and gradings."""

    location: str
    reference: str
    snippet: str
    gradings: dict[str, str | None]

    @property
    def normalized(self) -> str:
        """Whitespace-collapsed quote, as written (used for reporting and keys)."""
        return " ".join(self.snippet.split())

    @property
    def comparable(self) -> str:
        """Case-folded form used for equality and containment tests."""
        return self.normalized.casefold()


def _grading(node: dict, field: str) -> str | None:
    value = node.get(field)
    if isinstance(value, str) and value.strip():
        return value.strip()
    return GRADING_DEFAULTS[field]


def iter_graded_snippets(
    data: Any,
    excerpt_fields,
    reference_fields,
):
    """Yield a :class:`GradedSnippet` for every reference/snippet pair in *data*.

    Deliberately a local walk rather than
    ``reference_snippet_audit.iter_snippet_pairs``: this check needs the
    ``evidence_source``/``supports`` siblings of the snippet, which the shared
    ``SnippetPair`` does not carry.
    """
    excerpts = tuple(sorted(excerpt_fields))
    references = tuple(sorted(reference_fields))

    def walk(node: Any, location: str):
        if isinstance(node, dict):
            reference = next(
                (
                    node[name].strip()
                    for name in references
                    if isinstance(node.get(name), str) and node[name].strip()
                ),
                None,
            )
            if reference is not None:
                gradings = {field: _grading(node, field) for field in GRADING_DEFAULTS}
                for name in excerpts:
                    snippet = node.get(name)
                    if isinstance(snippet, str) and snippet.strip():
                        child = f"{location}.{name}" if location else name
                        yield GradedSnippet(child, reference, snippet, gradings)
            for key, value in node.items():
                child = f"{location}.{key}" if location else str(key)
                yield from walk(value, child)
        elif isinstance(node, list):
            for index, value in enumerate(node):
                yield from walk(value, f"{location}[{index}]")

    yield from walk(data, "")


def _same_quote(a: GradedSnippet, b: GradedSnippet) -> str | None:
    """The shared quote if *a* and *b* quote the same text, else ``None``.

    Returns the shorter (contained) snippet as written, which is what the finding
    reports and keys on: it is the extent both items actually share.
    """
    left, right = a.comparable, b.comparable
    if left == right:
        return a.normalized
    shorter, longer = (a, b) if len(left) < len(right) else (b, a)
    if shorter.comparable not in longer.comparable:
        return None
    if len(_WORD_RE.findall(shorter.normalized)) < MIN_OVERLAP_WORDS:
        return None
    return shorter.normalized


def find_violations(data, excerpt_fields, reference_fields, fields=GATED_FIELDS):
    """Yield ``(field, reference, value_a, value_b, quote, loc_a, loc_b)`` findings.

    ``value_a``/``value_b`` follow document order; the baseline key sorts them so
    it does not depend on which item was written first.
    """
    by_reference: dict[str, list[GradedSnippet]] = {}
    for item in iter_graded_snippets(data, excerpt_fields, reference_fields):
        by_reference.setdefault(item.reference.casefold(), []).append(item)

    for items in by_reference.values():
        for index, first in enumerate(items):
            for second in items[index + 1 :]:
                quote = _same_quote(first, second)
                if quote is None:
                    continue
                for field in fields:
                    left, right = first.gradings[field], second.gradings[field]
                    if left is None or right is None or left == right:
                        continue
                    yield (
                        field,
                        first.reference,
                        left,
                        right,
                        quote,
                        first.location,
                        second.location,
                    )


def collect_items(
    scan_dir: Path = SCAN_DIR,
    schema_path: Path | None = None,
    rel_to: Path = ROOT,
):
    """Return ``[(relpath, data)]`` for every parseable YAML file under *scan_dir*.

    ``rel_to`` is the base the reported relative paths are computed against, so
    :func:`baseline_from_ref` can scan an extracted copy of ``kb/`` under a temp
    dir and still report ``kb/disorders/X.yaml`` keys.
    """
    documents = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception as exc:
            # Malformed YAML is `validate-all`'s gate, not this one's -- but
            # skipping silently would make the file invisible rather than
            # merely unchecked.
            print(
                f"warning: skipping unparseable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        documents.append((path.relative_to(rel_to).as_posix(), data))
    return documents


def _field_names(schema_path: Path | None):
    return discover_field_names(
        schema_path if schema_path is not None else ROOT / DEFAULT_SCHEMA
    )


def within_file_findings(documents, excerpt_fields, reference_fields, fields):
    findings = []
    for rel, data in documents:
        for finding in find_violations(
            data, excerpt_fields, reference_fields, fields=fields
        ):
            findings.append((rel, *finding))
    return sorted(findings)


def scan_repo(
    scan_dir: Path = SCAN_DIR,
    schema_path: Path | None = None,
    rel_to: Path = ROOT,
    fields=GATED_FIELDS,
):
    """Return sorted ``(relpath, field, reference, a, b, quote, loc_a, loc_b)``."""
    excerpt_fields, reference_fields = _field_names(schema_path)
    documents = collect_items(scan_dir, schema_path, rel_to)
    return within_file_findings(documents, excerpt_fields, reference_fields, fields)


# --- across files (#11221) ----------------------------------------------------


class CrossFileFinding(NamedTuple):
    """One sentence graded two ways in two different files.

    The two sides are ordered by path so the finding does not depend on which
    file was scanned first.
    """

    reference: str
    quote: str
    path_a: str
    value_a: str
    location_a: str
    path_b: str
    value_b: str
    location_b: str

    @property
    def gated(self) -> bool:
        return frozenset({self.value_a, self.value_b}) in GATED_CROSS_FILE_PAIRS


def find_cross_file_violations(documents, excerpt_fields, reference_fields):
    """Yield :class:`CrossFileFinding` for divergent ``evidence_source`` pairs.

    Only pairs of items in *different* files are compared; pairs inside one file
    are :func:`find_violations`' job, and reporting them twice would double the
    backlog. ``supports`` is not compared across files: it is claim-relative even
    within one entry, and more so between two.
    """
    by_reference: dict[str, list[tuple[str, GradedSnippet]]] = {}
    for rel, data in documents:
        for item in iter_graded_snippets(data, excerpt_fields, reference_fields):
            by_reference.setdefault(item.reference.casefold(), []).append((rel, item))

    field = "evidence_source"
    for items in by_reference.values():
        if len({rel for rel, _ in items}) < 2:
            continue
        for index, (rel_a, first) in enumerate(items):
            for rel_b, second in items[index + 1 :]:
                if rel_a == rel_b:
                    continue
                left, right = first.gradings[field], second.gradings[field]
                if left is None or right is None or left == right:
                    continue
                quote = _same_quote(first, second)
                if quote is None:
                    continue
                side_a = (rel_a, left, first.location)
                side_b = (rel_b, right, second.location)
                if side_b < side_a:
                    side_a, side_b = side_b, side_a
                yield CrossFileFinding(first.reference, quote, *side_a, *side_b)


def scan_repo_cross_file(
    scan_dir: Path = SCAN_DIR,
    schema_path: Path | None = None,
    rel_to: Path = ROOT,
):
    """Every divergent cross-file pair, gated and report-only, sorted."""
    excerpt_fields, reference_fields = _field_names(schema_path)
    documents = collect_items(scan_dir, schema_path, rel_to)
    return sorted(
        find_cross_file_violations(documents, excerpt_fields, reference_fields)
    )


def format_cross_file_finding(finding: CrossFileFinding) -> str:
    label = "gated" if finding.gated else "report-only"
    return (
        f"[{label}] {finding.reference} evidence_source={finding.value_a} in "
        f"{finding.path_a} ({finding.location_a}) but "
        f"evidence_source={finding.value_b} in {finding.path_b} "
        f"({finding.location_b})\n    quote: {finding.quote!r}"
    )


def _cross_file_key(finding: CrossFileFinding) -> str:
    """``path_a<TAB>path_b<TAB>reference<TAB>a|b<TAB>quote``, sides sorted by path."""
    return (
        f"{finding.path_a}\t{finding.path_b}\t{finding.reference}\t"
        f"{finding.value_a}|{finding.value_b}\t{' '.join(finding.quote.split())}"
    )


def count_cross_file(findings) -> Counter:
    """Occurrence counts of the *gated* cross-file pairs (the baseline's content)."""
    return Counter(_cross_file_key(f) for f in findings if f.gated)


def new_cross_file_findings(findings, baseline: Counter):
    """Gated pairs not covered by *baseline*, including extra repeats."""
    seen: Counter = Counter()
    new = []
    for finding in findings:
        if not finding.gated:
            continue
        key = _cross_file_key(finding)
        seen[key] += 1
        if seen[key] > baseline.get(key, 0):
            new.append(finding)
    return new


def format_finding(finding) -> str:
    rel, field, reference, left, right, quote, loc_a, loc_b = finding
    return (
        f"{rel}: {reference} {field}={left} at {loc_a} "
        f"but {field}={right} at {loc_b}\n    quote: {quote!r}"
    )


def _baseline_key(finding) -> str:
    """``path<TAB>field<TAB>reference<TAB>a|b<TAB>quote``.

    Keyed on the quote rather than the YAML location, which shifts whenever a
    list above it grows. The two values are sorted so the key does not depend on
    document order, and the quote is whitespace-collapsed because the baseline
    file is line-oriented.
    """
    rel, field, reference, left, right, quote, _, _ = finding
    values = "|".join(sorted((left, right)))
    # Collapsed here as well as in GradedSnippet.normalized: the baseline file is
    # tab-delimited and line-oriented, so an embedded newline or tab would split
    # one entry across two lines (or two columns) on write and never match on
    # read.
    return f"{rel}\t{field}\t{reference}\t{values}\t{' '.join(quote.split())}"


def count_by_key(findings) -> Counter:
    """How many times each divergence appears."""
    return Counter(_baseline_key(finding) for finding in findings)


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    """Read the baseline as ``{key: grandfathered occurrence count}``.

    The count matters: one sentence graded two ways across *three* blocks is a
    worse contradiction than across two, so a plain set of keys would let the
    extra ones through.
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
        "# Grandfathered snippet-grading divergences (see\n"
        "# scripts/check_snippet_grading.py and issue #8184).\n"
        "# Each line is `count<TAB>path<TAB>field<TAB>reference<TAB>a|b<TAB>quote`,\n"
        "# where count is how many item pairs in that file disagree that way. A\n"
        "# divergence fails the guard if it is absent here OR appears MORE often\n"
        "# than the count recorded. Fix by grading the quote once and using that\n"
        "# value everywhere it appears in the file -- or, if the two items really\n"
        "# quote different claims, quote the sentence that makes each one. Remove\n"
        "# entries as the backlog is fixed; do not add new ones. Regenerate with:\n"
        "#   just update-snippet-grading-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def write_cross_file_baseline(findings, path: Path = CROSS_FILE_BASELINE_PATH) -> None:
    counts = count_cross_file(findings)
    header = (
        "# Grandfathered cross-file snippet-grading divergences (see\n"
        "# scripts/check_snippet_grading.py and issue #11221).\n"
        "# Each line is `count<TAB>path_a<TAB>path_b<TAB>reference<TAB>a|b<TAB>quote`,\n"
        "# where a is the grading in path_a and b the grading in path_b. Only the\n"
        "# gated pairs live here: HUMAN_CLINICAL against IN_VITRO, MODEL_ORGANISM or\n"
        "# COMPUTATIONAL, which cannot both be right for one sentence. Pairs\n"
        "# involving OTHER are report-only pending #10273 and never recorded. Fix\n"
        "# by reading the cited paper and correcting whichever file is wrong;\n"
        "# remove entries as the backlog is fixed and do not add new ones.\n"
        "# Regenerate with:\n"
        "#   just update-snippet-grading-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


#: In-process memo for :func:`_findings_at_ref`, so the per-file and cross-file
#: baselines share one ``git archive`` and one parse of the ref's ``kb/``.
_REF_FINDINGS: dict[tuple[str, str, tuple[str, ...]], tuple[list, list] | None] = {}


def _findings_at_ref(ref: str, root: Path, fields) -> tuple[list, list] | None:
    """``(within_file, cross_file)`` findings for ``kb/`` at *ref*, or ``None``."""
    memo_key = (ref, str(root), tuple(fields))
    if memo_key in _REF_FINDINGS:
        return _REF_FINDINGS[memo_key]
    result = _scan_ref(ref, root, fields)
    _REF_FINDINGS[memo_key] = result
    return result


def baseline_from_ref(
    ref: str, root: Path = ROOT, fields=GATED_FIELDS, cross_file: bool = False
) -> Counter | None:
    """Grandfather baseline derived live from a git *ref* (e.g. ``origin/main``).

    Returns ``None`` if *ref* cannot be read (no git, ref absent in a shallow
    checkout, path missing at the ref), so the caller can fall back to the
    committed baseline. With ``cross_file`` the gated cross-file pairs at the
    ref are returned instead of the per-file divergences.
    """
    found = _findings_at_ref(ref, root, fields)
    if found is None:
        return None
    within, cross = found
    return count_cross_file(cross) if cross_file else count_by_key(within)


def _scan_ref(ref: str, root: Path, fields) -> tuple[list, list] | None:
    """git-archive ``kb/`` at *ref* and scan it both ways.

    git's own stderr is surfaced on failure so a CI misconfiguration is
    diagnosable rather than a silent capability downgrade.
    """
    # Relative to the real ROOT (always ``kb``), not *root*: tests pass a
    # throwaway repo as *root* while the layout under it is still ``kb/``.
    scan_rel = SCAN_DIR.relative_to(ROOT).as_posix()
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "archive", "--format=tar", ref, "--", scan_rel],
            capture_output=True,
            check=False,  # returncode handled explicitly below (PLW1510)
        )
    except (FileNotFoundError, OSError) as exc:
        print(
            f"snippet grading baseline: git archive for {ref!r} could not run: {exc}",
            file=sys.stderr,
        )
        return None
    if proc.returncode != 0:
        detail = (
            proc.stderr.decode("utf-8", "replace").strip() or f"exit {proc.returncode}"
        )
        print(
            f"snippet grading baseline: git archive {ref!r} failed: {detail}",
            file=sys.stderr,
        )
        return None
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        try:
            with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tar:
                # filter="data" is the safe extraction policy that becomes the
                # default in 3.14; set explicitly to pin behavior. The archive is
                # git-authored (kb/ only), so it never rejects a real member.
                tar.extractall(tmp_path, filter="data")
        except tarfile.TarError as exc:
            print(
                f"snippet grading baseline: unreadable archive for {ref!r}: {exc}",
                file=sys.stderr,
            )
            return None
        excerpt_fields, reference_fields = _field_names(None)
        documents = collect_items(tmp_path / scan_rel, rel_to=tmp_path)
        within = within_file_findings(
            documents, excerpt_fields, reference_fields, fields
        )
        cross = sorted(
            find_cross_file_violations(documents, excerpt_fields, reference_fields)
        )
    return within, cross


def resolve_baseline(
    ref: str | None = None, fields=GATED_FIELDS, cross_file: bool = False
) -> Counter:
    """Live from *ref* when given (env ``SNIPPET_GRADING_BASELINE_REF``), else file.

    ``cross_file`` selects the gated cross-file baseline instead of the per-file
    one; the ref and the fallback behave the same way for both.
    """
    if ref is None:
        ref = os.environ.get(BASELINE_REF_ENV) or None
    if ref:
        from_ref = (
            baseline_from_ref(ref, fields=fields, cross_file=True)
            if cross_file
            else baseline_from_ref(ref, fields=fields)
        )
        if from_ref is not None:
            # State which baseline engaged: the gate behaves differently
            # depending on whether the ref was reachable, so make that legible
            # in CI logs instead of leaving it to be inferred.
            kind = "cross-file " if cross_file else ""
            print(
                f"snippet grading baseline: grandfathered against ref {ref!r} "
                f"({len(from_ref)} distinct {kind}divergence(s))",
                file=sys.stderr,
            )
            return from_ref
        print(
            f"snippet grading baseline: could not read ref {ref!r}; "
            "falling back to the committed baseline",
            file=sys.stderr,
        )
    return load_baseline(CROSS_FILE_BASELINE_PATH if cross_file else BASELINE_PATH)


def new_findings(findings, baseline: Counter):
    """Findings not covered by *baseline*, including extra repeats of a known one."""
    seen: Counter = Counter()
    new = []
    for finding in findings:
        key = _baseline_key(finding)
        seen[key] += 1
        if seen[key] > baseline.get(key, 0):
            new.append(finding)
    return new


def _resolve_fields(choice: str) -> tuple[str, ...]:
    if choice == "all":
        return tuple(GRADING_DEFAULTS)
    return (choice,)


@reports_disk_full("check-snippet-grading")
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
        help="rewrite both baselines (per-file and cross-file) from current findings",
    )
    parser.add_argument(
        "--against-ref",
        metavar="REF",
        default=None,
        help=(
            "grandfather against the divergences present in kb/ at this git ref "
            f"instead of the committed baseline (env: {BASELINE_REF_ENV}). CI "
            "uses origin/<base> so the base branch is green by construction."
        ),
    )
    parser.add_argument(
        "--fields",
        choices=("evidence_source", "supports", "all"),
        default="evidence_source",
        help=(
            "which graded slot(s) to scan. Only evidence_source (the default) is "
            "gated; supports is claim-relative by design and is offered as a "
            "triage view. The committed baseline always covers the gated field "
            "only, so --update-baseline ignores this."
        ),
    )
    parser.add_argument(
        "--cross-file",
        action="store_true",
        help=(
            "with --all or --count, report the KB-wide comparison of one sentence "
            "across different files instead of the per-file one: gated pairs "
            "(HUMAN_CLINICAL against IN_VITRO, MODEL_ORGANISM or COMPUTATIONAL) "
            "and report-only pairs (anything involving OTHER, pending #10273). "
            "The default check always runs both."
        ),
    )
    args = parser.parse_args(argv)

    fields = GATED_FIELDS if args.update_baseline else _resolve_fields(args.fields)
    excerpt_fields, reference_fields = _field_names(None)
    documents = collect_items()
    findings = within_file_findings(documents, excerpt_fields, reference_fields, fields)
    cross = sorted(
        find_cross_file_violations(documents, excerpt_fields, reference_fields)
    )

    if args.update_baseline:
        write_baseline(findings)
        write_cross_file_baseline(cross)
        gated = sum(1 for finding in cross if finding.gated)
        print(
            f"Wrote baseline with {len(findings)} finding(s) to "
            f"{BASELINE_PATH.relative_to(ROOT)} and {gated} gated cross-file "
            f"pair(s) to {CROSS_FILE_BASELINE_PATH.relative_to(ROOT)}"
        )
        return 0

    if args.all:
        if args.cross_file:
            for finding in cross:
                print(format_cross_file_finding(finding))
            gated = sum(1 for finding in cross if finding.gated)
            print(
                f"\n{len(cross)} cross-file divergence(s): {gated} gated, "
                f"{len(cross) - gated} report-only."
            )
            return 0
        for finding in findings:
            print(format_finding(finding))
        print(f"\n{len(findings)} snippet-grading divergence(s).")
        return 0

    if args.count:
        if args.cross_file:
            baseline = resolve_baseline(args.against_ref, cross_file=True)
            pairs = Counter("|".join(sorted((f.value_a, f.value_b))) for f in cross)
            gated = sum(1 for finding in cross if finding.gated)
            print(
                f"cross-file divergences: {len(cross)} "
                f"({gated} gated, {len(cross) - gated} report-only)"
            )
            for pair, count in sorted(pairs.items()):
                print(f"  {pair}: {count}")
            print(
                f"baseline: {len(baseline)} distinct gated pair(s), "
                f"{sum(baseline.values())} grandfathered occurrence(s)"
            )
            print(
                f"new (non-baselined): {len(new_cross_file_findings(cross, baseline))}"
            )
            return 0
        baseline = resolve_baseline(args.against_ref, fields=fields)
        files = {finding[0] for finding in findings}
        fields = Counter(finding[1] for finding in findings)
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        for field, count in sorted(fields.items()):
            print(f"  {field}: {count}")
        print(
            f"baseline: {len(baseline)} distinct divergence(s), "
            f"{sum(baseline.values())} grandfathered occurrence(s)"
        )
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        return 0

    baseline = resolve_baseline(args.against_ref, fields=fields)
    new = new_findings(findings, baseline)
    cross_baseline = resolve_baseline(args.against_ref, cross_file=True)
    new_cross = new_cross_file_findings(cross, cross_baseline)
    against_ref = bool(args.against_ref or os.environ.get(BASELINE_REF_ENV))
    if new:
        print("New snippet-grading divergence(s) detected.")
        print("`evidence_source` classifies the cited publication, so it cannot")
        print("change because the quote was copied into another block: one")
        print("sentence cannot carry two values in one file. Grade the quote")
        print("once and use that value everywhere -- or, if the two items are")
        print("really citing different findings, quote the sentence that makes")
        print("each one. An absent `evidence_source` counts as HUMAN_CLINICAL.\n")
        for finding in new:
            print(format_finding(finding))
        print(f"\n{len(new)} new finding(s).")
    if new_cross:
        if new:
            print()
        print("New cross-file snippet-grading divergence(s) detected.")
        print("The same sentence of the same reference is graded HUMAN_CLINICAL in")
        print("one entry and IN_VITRO, MODEL_ORGANISM or COMPUTATIONAL in another.")
        print("Both cannot be right. Read the cited paper and correct whichever")
        print("file is wrong, which may be the one this change did not touch.\n")
        for finding in new_cross:
            print(format_cross_file_finding(finding))
        print(f"\n{len(new_cross)} new cross-file finding(s).")
    if new or new_cross:
        if against_ref:
            # A ref baseline (CI) never reads the committed file, so
            # --update-baseline would pass locally, still fail CI, and commit
            # churn to a snapshot this ratchet exists to stop touching.
            print("Grandfathering is unavailable when checking against a ref: make")
            print("the two gradings agree, or re-quote so each item cites its own")
            print("claim.")
        else:
            print("If a finding is genuinely unavoidable, run --update-baseline")
            print("to grandfather it.")
        return 1
    report_only = sum(1 for finding in cross if not finding.gated)
    print(
        "OK: no new snippet-grading divergences "
        f"({sum(baseline.values())} occurrence(s) of {len(baseline)} distinct "
        "divergence(s) grandfathered in baseline; "
        f"{sum(cross_baseline.values())} gated cross-file pair(s) grandfathered, "
        f"{report_only} report-only cross-file pair(s), see --all --cross-file)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
