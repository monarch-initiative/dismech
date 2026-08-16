#!/usr/bin/env python3
"""Guard against evidence items with an empty (or whitespace-only) snippet.

An ``EvidenceItem`` with ``snippet: ""`` passes every other check in the
stack vacuously: ``linkml-reference-validator`` reports "All validations
passed", ``count-verified-snippets``/``dismech.reference_snippet_audit``
excludes the pair from its ``N/N verified`` line entirely (silently, since
:func:`dismech.reference_snippet_audit.iter_snippet_pairs` only yields pairs
whose snippet is non-empty), and ``scripts/check_environmental_evidence.py``'s
``if entry.get("evidence")`` predicate treats the block's mere presence as
"cited". None of those checks was built to catch this shape of defect, so an
unsubstantiated claim can be "retired" from a curation backlog without
anything actually being quoted. See dismech issue #8550.

Signal
------
A mapping carrying both a ``reference`` and a ``snippet`` key where
``snippet`` is present but empty or whitespace-only, **and** the sibling
``supports`` value (when present) is not ``NO_EVIDENCE``.

Why ``NO_EVIDENCE`` is exempt
------------------------------
A ``NO_EVIDENCE`` item records "this candidate reference was checked and does
not support the claim" -- by construction there may be no quotable sentence to
attach, and this is already an established (if unstated) convention in
``kb/``: a repo-wide scan at the time this check was written found 25 empty
snippets, and every single one carried ``supports: NO_EVIDENCE``. A positive
item (``SUPPORT``/``PARTIAL``/``REFUTE``) asserts something the reference must
actually say, so an empty snippet there is always a defect, never a
legitimate annotation -- that is the actual failure mode #8550 describes (a
``SUPPORT`` item produced by a slicing bug that ran backwards).

No baseline
-----------
Unlike ``check_title_snippets.py`` / ``check_snippet_length.py`` /
``check_environmental_evidence.py``, this check ships with **no grandfathered
backlog**: the repo-wide scan above found zero non-``NO_EVIDENCE`` empty
snippets in ``kb/``, so it is a straight hard gate rather than a ratchet. If a
future scan finds a real backlog, add baseline machinery matching the sibling
checks then -- manufacturing it preemptively for a zero-item backlog would be
needless complexity.

Usage
-----
    python scripts/check_empty_snippets.py            # gate: fail on any finding
    python scripts/check_empty_snippets.py --all      # list every finding, incl. NO_EVIDENCE
    python scripts/check_empty_snippets.py --count    # summary counts
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from dismech.reference_snippet_audit import DEFAULT_SCHEMA, discover_field_names
from dismech.yaml_io import safe_load

# Scans all of kb/, not just kb/disorders/ -- kb/modules/ and
# kb/comorbidities/ validate against the same classes and can carry evidence
# items of their own; scoping to disorders/ would make them a silent blind
# spot in a check whose whole point is that the gap is invisible.
SCAN_DIR = ROOT / "kb"

#: The one ``supports`` value for which an empty snippet is a sanctioned
#: annotation rather than a defect.
_EXEMPT_SUPPORTS = "NO_EVIDENCE"


def find_violations(
    data: Any,
    excerpt_fields,
    reference_fields,
    location: str = "",
    include_exempt: bool = False,
):
    """Yield ``(location, reference, supports)`` for empty evidence snippets.

    Deliberately does *not* reuse
    :func:`dismech.reference_snippet_audit.iter_snippet_pairs`: that walker
    only yields pairs whose snippet is non-empty (correct for its own job of
    checking snippets *against* the cache), which is precisely why an empty
    snippet is invisible to every check built on top of it. This walker is the
    mirror image -- it looks for the pairs that walker skips.

    By default, ``supports: NO_EVIDENCE`` items are excluded (they are the
    sanctioned "checked, not relevant" annotation); pass
    ``include_exempt=True`` for a full triage listing.
    """
    if isinstance(data, dict):
        reference_id = next(
            (
                data[name]
                for name in reference_fields
                if isinstance(data.get(name), str) and data[name].strip()
            ),
            None,
        )
        if reference_id is not None:
            for name in excerpt_fields:
                if name not in data:
                    continue
                snippet = data.get(name)
                if isinstance(snippet, str) and not snippet.strip():
                    supports = data.get("supports")
                    if include_exempt or supports != _EXEMPT_SUPPORTS:
                        child = f"{location}.{name}" if location else name
                        yield (child, reference_id.strip(), supports)
        for key, value in data.items():
            child = f"{location}.{key}" if location else str(key)
            yield from find_violations(
                value, excerpt_fields, reference_fields, child, include_exempt
            )
    elif isinstance(data, list):
        for index, value in enumerate(data):
            yield from find_violations(
                value,
                excerpt_fields,
                reference_fields,
                f"{location}[{index}]",
                include_exempt,
            )


def scan_repo(
    scan_dir: Path = SCAN_DIR,
    schema_path: Path = DEFAULT_SCHEMA,
    include_exempt: bool = False,
    rel_to: Path = ROOT,
):
    """Return a sorted list of ``(relpath, location, reference, supports)`` findings.

    ``rel_to`` is the base the reported relative paths are computed against
    (defaults to :data:`ROOT`); tests pass a ``tmp_path`` here to scan an
    isolated directory tree.
    """
    excerpt_fields, reference_fields = discover_field_names(schema_path)
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
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
        if not isinstance(data, dict):
            continue
        rel = path.relative_to(rel_to).as_posix()
        for location, reference_id, supports in find_violations(
            data, excerpt_fields, reference_fields, include_exempt=include_exempt
        ):
            findings.append((rel, location, reference_id, supports))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all",
        action="store_true",
        help="List every empty-snippet finding, including NO_EVIDENCE-exempt ones.",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Print summary counts only.",
    )
    args = parser.parse_args(argv)

    if args.all:
        findings = scan_repo(include_exempt=True)
        non_exempt = sum(1 for *_, supports in findings if supports != _EXEMPT_SUPPORTS)
        for rel, location, reference_id, supports in findings:
            print(f"{rel}:{location}\t{reference_id}\t{supports}")
        print(f"\nTotal empty snippets: {len(findings)} ({non_exempt} non-exempt)")
        return 0

    findings = scan_repo()

    if args.count:
        print(f"Empty, non-exempt snippets: {len(findings)}")
        return 0

    if findings:
        print(
            "Empty (non-NO_EVIDENCE) evidence snippet(s) detected. An evidence "
            "item that SUPPORTs/PARTIALly supports/REFUTEs a claim must quote "
            "real text from the reference -- an empty snippet asserts nothing "
            "while still lending the citation's authority. Quote the real "
            "sentence, change `supports` to NO_EVIDENCE if that is genuinely "
            "what happened, or drop the evidence item if the reference has no "
            "quotable text (see CLAUDE.md 'When Evidence Cannot Be Verified'):",
            file=sys.stderr,
        )
        for rel, location, reference_id, supports in findings:
            print(f"  {rel}:{location}  {reference_id}  supports={supports}", file=sys.stderr)
        return 1

    print("No empty (non-NO_EVIDENCE) evidence snippets found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
