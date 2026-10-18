#!/usr/bin/env python3
"""Guard against prose that argues for a retired ``supports`` grade.

Issue #7439 narrowed ``EvidenceItemSupportEnum`` to ``SUPPORT`` / ``REFUTE`` /
``NO_EVIDENCE``, and #10003 migrated every ``supports: PARTIAL`` value. The
prose written to justify those values was not migrated, so thousands of
evidence items read like this::

    - reference: PMID:12345678
      supports: SUPPORT
      explanation: >-
        Graded PARTIAL because the finding is in a mouse model, not patients.

The explanation argues for a grade the schema no longer has, directly above a
value that contradicts it. Nothing else catches this: ``check-enum-values``
reads enum-bound slots only, and an ``explanation`` is free text (issue
#12805). Agents copy explanations between evidence items, so without a guard
the backlog regrows as fast as curation PRs chip at it.

Signal
------
A whole-word ``PARTIAL`` in any string value of a ``kb/`` YAML entry. Whole
word and not followed by ``_``, so ``PARTIALLY_RECAPITULATES``,
``PARTIAL_LOSS_OF_FUNCTION`` and ordinary lowercase "partial" are untouched.
Every string is scanned, not just ``explanation`` / ``description`` /
``notes``: the backlog also sits in ``rationale``, ``review_notes`` and
``distinguishing_features``, and no slot in ``dismech.yaml`` has ``PARTIAL`` as
a legal value, so there is nothing to confuse it with.

Exemptions:

* **Text copied from a source.** ``snippet``, ``reference_title``, ``title``
  and ``supporting_text`` hold a source's own words, which a curator cannot
  reword, and a shrink-only baseline could never admit them -- so a trial
  abstract quoting "PARTIAL RESPONSE" would block its PR for good. The set is
  read from the schema (:func:`source_text_fields`), so a new exact-quote slot
  is skipped without editing this script.
* **``kb/hypotheses/``.** Its assessment and reconciliation schemas define their
  own legitimate ``PARTIAL`` value.
* **Sentences about the retirement itself.** A sentence that also says
  "retired", or cites #7439 / #10003 / #10061, is recording that the grade went
  away ("Four explanation strings still argued for the retired supports:
  PARTIAL grade (#7439/#10061)") rather than arguing for it. Deliberately
  narrow: "removed", "no longer" and "narrowing" were tried and each matched a
  genuinely stale grade ("a negative result narrowing where the association
  applies").

Fixing a finding
----------------
Not a search-and-replace. ``CLAUDE.md`` ("`supports` is direction; `directness`
is a separate axis") has the mapping. Most of these explanations describe an
inference step, so the fix is ``directness: INDIRECT`` and a rewording that
drops the grade name. An explanation saying the source supports one part of the
claim and contradicts another needs splitting into a ``SUPPORT`` and a
``REFUTE`` item instead.

Baseline ratchet
----------------
The backlog is grandfathered per ``(file, sentence)`` with an occurrence count,
like :mod:`scripts.check_title_snippets`, so moving a sentence within a file is
free while copying it to a new evidence item is not. ``--against-ref REF`` (env
``RETIRED_SUPPORT_PROSE_BASELINE_REF``) derives the baseline live from ``kb/``
at a git ref; CI passes the base branch. ``tests/retired_support_prose_baseline.txt``
is the committed fallback for local runs.

Unlike the other ratchets, ``--update-baseline`` here only ever **shrinks** the
committed file: it drops entries that are gone and lowers counts that fell, but
never adds a key or raises a count. There is no legitimate new instance of
arguing for a grade the schema does not have.

Usage
-----
    python scripts/check_retired_support_prose.py                  # gate
    python scripts/check_retired_support_prose.py --against-ref origin/main
    python scripts/check_retired_support_prose.py --all            # every finding
    python scripts/check_retired_support_prose.py --count
    python scripts/check_retired_support_prose.py --update-baseline
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

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache
from dismech.kb_cache import load_document
from dismech.yaml_io import safe_load

SCAN_DIR = ROOT / "kb"
#: Subdirectories of kb/ whose schema has its own legitimate PARTIAL value.
EXCLUDED_SUBDIRS = frozenset({"hypotheses"})
SCHEMA_PATH = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"

#: ``implements:`` values marking a slot whose text is copied from a source.
SOURCE_TEXT_IMPLEMENTS = frozenset({"linkml:excerpt", "dcterms:title", "linkml:title"})
#: Exact-quote slots the schema describes as such but does not annotate.
#: `supporting_text` is "Exact excerpt/quote from the publication" with no
#: ``implements:``; listed here rather than skipped by accident.
UNANNOTATED_SOURCE_TEXT_FIELDS = frozenset({"supporting_text"})
#: Used when the schema cannot be read, so a broken schema never widens the scan.
FALLBACK_SOURCE_TEXT_FIELDS = frozenset(
    {"snippet", "reference_title", "title", "supporting_text"}
)
BASELINE_PATH = ROOT / "tests" / "retired_support_prose_baseline.txt"
BASELINE_REF_ENV = "RETIRED_SUPPORT_PROSE_BASELINE_REF"

#: Values removed from EvidenceItemSupportEnum. WRONG_STATEMENT went in the same
#: narrowing, but no prose names it today; listing it keeps it from arriving.
RETIRED_VALUES = ("PARTIAL", "WRONG_STATEMENT")
#: Whole word, and not the stem of an underscored enum value (PARTIAL_*).
RETIRED_RE = re.compile(r"\b(?:" + "|".join(RETIRED_VALUES) + r")\b(?!_)")

#: A sentence saying the grade was retired is history, not an argument for it.
RETIREMENT_RE = re.compile(r"\bretired\b|#7439\b|#10003\b|#10061\b", re.IGNORECASE)

#: Split on terminal punctuation followed by whitespace and a plausible sentence
#: start. Crude, but the key only has to be stable, not linguistically correct.
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.;!?])\s+(?=[A-Z(`\"'\[])")


def sentences(text: str) -> list[str]:
    """Whitespace-collapsed sentences of *text*."""
    return _SENTENCE_SPLIT_RE.split(" ".join(text.split()))


def source_text_fields(schema_path: Path = SCHEMA_PATH) -> frozenset[str]:
    """Slot names whose values are copied verbatim from a cited source."""
    try:
        schema = safe_load(schema_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return FALLBACK_SOURCE_TEXT_FIELDS
    if not isinstance(schema, dict):
        return FALLBACK_SOURCE_TEXT_FIELDS

    found = set(UNANNOTATED_SOURCE_TEXT_FIELDS)

    def scan(definitions) -> None:
        for name, definition in (definitions or {}).items():
            if isinstance(definition, dict) and SOURCE_TEXT_IMPLEMENTS.intersection(
                definition.get("implements") or []
            ):
                found.add(name)

    scan(schema.get("slots"))
    for cls in (schema.get("classes") or {}).values():
        if isinstance(cls, dict):
            scan(cls.get("attributes"))
            scan(cls.get("slot_usage"))
    return frozenset(found)


def find_violations(
    data, location: str = "", skip_fields: frozenset[str] = frozenset()
):
    """Yield ``(location, sentence)`` once per retired-value mention in *data*.

    A sentence naming the value twice yields twice, so the occurrence count in
    the baseline tracks mentions rather than sentences. Values under a key in
    *skip_fields* are not read.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key in skip_fields:
                continue
            child = f"{location}.{key}" if location else str(key)
            yield from find_violations(value, child, skip_fields)
    elif isinstance(data, list):
        for i, value in enumerate(data):
            yield from find_violations(value, f"{location}[{i}]", skip_fields)
    elif isinstance(data, str) and RETIRED_RE.search(data):
        for sentence in sentences(data):
            if RETIREMENT_RE.search(sentence):
                continue
            for _ in RETIRED_RE.finditer(sentence):
                yield (location, sentence)


def iter_kb_files(scan_dir: Path = SCAN_DIR):
    for path in sorted(scan_dir.rglob("*.yaml")):
        rel_parts = path.relative_to(scan_dir).parts
        if rel_parts and rel_parts[0] in EXCLUDED_SUBDIRS:
            continue
        yield path


def scan_repo(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return sorted ``(relpath, location, sentence)`` findings."""
    skip_fields = source_text_fields()
    findings = []
    for path in iter_kb_files(scan_dir):
        try:
            data = load_document(path)
        except Exception as exc:
            print(
                f"warning: skipping unparsable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        rel = path.relative_to(rel_to).as_posix()
        for location, sentence in find_violations(data, skip_fields=skip_fields):
            findings.append((rel, location, sentence))
    return findings


def _baseline_key(rel: str, sentence: str) -> str:
    # Keyed on (file, sentence), not the YAML location, which shifts whenever a
    # list above it grows.
    return f"{rel}\t{sentence}"


def count_by_key(findings) -> Counter:
    return Counter(_baseline_key(rel, sentence) for rel, _, sentence in findings)


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    """Read the baseline as ``{key: grandfathered occurrence count}``."""
    counts: Counter = Counter()
    if not path.exists():
        return counts
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        count, tab, key = line.partition("\t")
        if tab and count.isdigit():
            counts[key] = int(count)
    return counts


def shrink_baseline(baseline: Counter, findings) -> Counter:
    """*baseline* lowered to what *findings* still contain; never raised.

    Each key keeps ``min(old count, current count)``, and a key absent from
    *baseline* is never added, however many current findings carry it.
    """
    current = count_by_key(findings)
    shrunk: Counter = Counter()
    for key, old in baseline.items():
        kept = min(old, current.get(key, 0))
        if kept:
            shrunk[key] = kept
    return shrunk


def write_baseline(counts: Counter, path: Path = BASELINE_PATH) -> None:
    header = (
        "# Grandfathered prose naming a retired `supports` grade (see\n"
        "# scripts/check_retired_support_prose.py and issue #12805).\n"
        "# Each line is `count<TAB>path<TAB>sentence`, where count is how many\n"
        "# times that sentence names a retired value in that file. A mention\n"
        "# fails the guard if it is absent here OR appears MORE often than the\n"
        "# count recorded. This file only ever shrinks: fix the prose, then run\n"
        "#   just update-retired-support-prose-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def baseline_from_ref(ref: str, root: Path = ROOT) -> Counter | None:
    """Baseline derived live from ``kb/`` at a git *ref*, or ``None``."""
    scan_rel = SCAN_DIR.relative_to(ROOT).as_posix()
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "archive", "--format=tar", ref, "--", scan_rel],
            capture_output=True,
            check=False,
        )
    except (FileNotFoundError, OSError) as exc:
        print(
            f"retired-support-prose baseline: git archive for {ref!r} could not "
            f"run: {exc}",
            file=sys.stderr,
        )
        return None
    if proc.returncode != 0:
        detail = (
            proc.stderr.decode("utf-8", "replace").strip() or f"exit {proc.returncode}"
        )
        print(
            f"retired-support-prose baseline: git archive {ref!r} failed: {detail}",
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
                f"retired-support-prose baseline: unreadable archive for {ref!r}: "
                f"{exc}",
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
                f"retired-support-prose baseline: grandfathered against ref {ref!r} "
                f"({sum(from_ref.values())} mention(s))",
                file=sys.stderr,
            )
            return from_ref
        print(
            f"retired-support-prose baseline: could not read ref {ref!r}; "
            "falling back to the committed baseline",
            file=sys.stderr,
        )
    return load_baseline()


def new_findings(findings, baseline: Counter):
    """Findings not covered by *baseline*, including extra copies of a known one."""
    seen: Counter = Counter()
    new = []
    for finding in findings:
        key = _baseline_key(finding[0], finding[2])
        seen[key] += 1
        if seen[key] > baseline.get(key, 0):
            new.append(finding)
    return new


def main(argv=None) -> int:
    # One walk over kb/ per run (two with --against-ref, over different trees),
    # so the shared-parse cache would only cost memory.
    kb_cache.default_off()
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--check", action="store_true", help="(default) fail on non-baselined findings"
    )
    group.add_argument("--all", action="store_true", help="list every finding")
    group.add_argument("--count", action="store_true", help="print summary counts")
    group.add_argument(
        "--update-baseline",
        action="store_true",
        help="shrink the committed baseline to what is still present (never grows)",
    )
    parser.add_argument(
        "--against-ref",
        metavar="REF",
        default=None,
        help=(
            "grandfather against the mentions present in kb/ at this git ref "
            f"instead of the committed baseline (env: {BASELINE_REF_ENV})"
        ),
    )
    args = parser.parse_args(argv)

    findings = scan_repo()

    if args.update_baseline:
        old = load_baseline()
        shrunk = shrink_baseline(old, findings)
        write_baseline(shrunk)
        print(
            f"Baseline {BASELINE_PATH.relative_to(ROOT)}: "
            f"{sum(old.values())} -> {sum(shrunk.values())} mention(s)."
        )
        ungrandfathered = len(new_findings(findings, shrunk))
        if ungrandfathered:
            print(
                f"{ungrandfathered} current mention(s) are not grandfathered and "
                "were NOT added; fix them (run without flags to list them)."
            )
        return 0

    if args.all:
        for rel, location, sentence in findings:
            print(f"{rel}:{location}: {sentence}")
        print(f"\n{len(findings)} mention(s) of a retired `supports` grade.")
        return 0

    if args.count:
        baseline = resolve_baseline(args.against_ref)
        files = {rel for rel, _, _ in findings}
        fields = Counter(
            re.sub(r"\[\d+\]$", "", location.rsplit(".", 1)[-1])
            for _, location, _ in findings
        )
        print(f"total mentions: {len(findings)} across {len(files)} file(s)")
        print("by field: " + ", ".join(f"{k} {v}" for k, v in fields.most_common()))
        print(f"baseline: {sum(baseline.values())} grandfathered mention(s)")
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        return 0

    baseline = resolve_baseline(args.against_ref)
    new = new_findings(findings, baseline)
    if new:
        print("New prose naming a retired `supports` grade detected.")
        print("PARTIAL and WRONG_STATEMENT were removed from `supports` (#7439), so")
        print("an explanation arguing for one contradicts the value beside it.\n")
        print("Reword rather than delete; CLAUDE.md has the mapping:")
        print(
            "  - an inference step     -> `directness: INDIRECT`, drop the grade name"
        )
        print(
            "  - supports part, refutes part -> split into a SUPPORT and a REFUTE item"
        )
        print("  - not about this claim  -> `supports: NO_EVIDENCE`\n")
        for rel, location, sentence in new:
            print(f"{rel}:{location}: {sentence}")
        print(f"\n{len(new)} new mention(s). This baseline cannot grow.")
        return 1
    print(
        f"OK: no new retired-grade prose ({sum(baseline.values())} mention(s) "
        "grandfathered in baseline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
