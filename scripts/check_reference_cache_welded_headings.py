#!/usr/bin/env python3
"""Guard against abstract headings welded onto the next word (#16621).

Crossref returns a structured abstract as JATS ``<jats:title>`` and
``<jats:p>`` elements with no text between them, and PubMed sometimes stores
the heading run straight into its sentence. Older linkml-reference-validator
releases stripped the tags without separating them, so the cache body read
``AbstractCastleman disease (CD) describes...`` or ``...cohort.MethodsWe
enrolled...``.

Whole-word matching (linkml-reference-validator 0.5.0) reads
``AbstractCastleman`` as one word, so an accurate quote starting on
``Castleman`` fails. ``DOI:10.1182/blood.2019000931`` was the reported case,
cited from ``kb/groupings/Castleman_Disease.yaml``. 0.5.1 separates the
headings when it writes a file (linkml/linkml-reference-validator#163), and
the files written before it were regenerated. This check stops an old-format
file from being committed again, for example one carried in by a long-lived
branch, or one copied from another checkout.

The heading list and the "start of text, or after a sentence end or a label"
anchor match upstream's ``_set_off_welded_headings``, so this flags exactly
what a fresh fetch would have separated, and nothing it leaves alone (an
all-caps ``RESULTSThe``, or a weld after a bracket).

It runs as an ungated, whole-tree CI step, because the PRs that add a cache
file touch only ``kb/`` and ``references_cache/``, which no path-filtered
pytest lane selects: the same reason ``check_reference_cache_nul_bytes.py``
runs that way.

The remedy for a finding is a forced re-fetch, never a hand edit:

    just fetch-reference --force <ID>

When this check landed, 308 files could not be regenerated safely, and they
are grandfathered in ``tests/welded_headings_baseline.txt``. For most of them
the re-fetch did separate the headings, but it changed something else, so it
was discarded and the old file kept:

- the re-fetch switched the file between full text and abstract-only, in
  either direction (268 files). A later re-fetch that keeps the same
  ``content_type`` will clear these;
- PubMed returned different abstract text, sometimes much shorter (24 files);
- the Crossref title came back with newlines and indentation around inline
  markup (9 files; linkml/linkml-reference-validator#166).

The rest are welds a re-fetch does not touch: text extracted from a full-text
PDF or web page keeps whatever spacing the extraction gave it, and a few of
those matches are not headings at all (the journal title ``Methods Enzymol``
printed as ``MethodsEnzymol`` in a reference list).

The baseline is keyed on the file and the number of welds it holds, so a new
weld in a listed file still fails. It only shrinks: ``--update-baseline``
drops entries that are fixed and never adds one. Before re-fetching a listed
file, check that the new file keeps its ``content_type`` and its text, since
those are the changes that kept it out of the first regeneration.

Usage
-----
    python scripts/check_reference_cache_welded_headings.py                    # gate
    python scripts/check_reference_cache_welded_headings.py --strict           # every finding
    python scripts/check_reference_cache_welded_headings.py --update-baseline  # shrink only
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "references_cache"
BASELINE = ROOT / "tests" / "welded_headings_baseline.txt"
BASELINE_HEADER = """\
# Grandfathered welded abstract headings in references_cache/ (see
# scripts/check_reference_cache_welded_headings.py, #16621). Each line is
# `path<TAB>count`: the file and how many welds it held when listed. Most were
# held back because a forced re-fetch, while separating the headings, also
# switched the file between full text and abstract-only, changed its PubMed
# text, or wrote a title with newlines (linkml/linkml-reference-validator#166).
# The rest are welds in full-text or reference-list text that a re-fetch does
# not touch, or matches that are not headings. Re-fetching is the fix where the
# new file keeps its content_type and text. A file with more welds than listed
# fails. Remove entries as they are fixed; do not add new ones.
# Shrink with: just check-reference-cache-welded-headings --update-baseline
"""

#: Copied from linkml_reference_validator.etl.sources.pmid._ABSTRACT_HEADINGS
#: (0.5.1). Not imported: it is a private name, and a rename upstream should
#: not silently empty this gate.
ABSTRACT_HEADINGS = (
    "Abstract|Background|Introduction|Objectives?|Aims?|Purpose|Importance|"
    "Context|Design|Setting|Participants|Patients|Methods|Materials and Methods|"
    "Interventions?|Measurements|Main Outcome Measures|Results|Findings|"
    "Observations|Case Report|Case Presentation|Discussion|Interpretation|"
    "Conclusions?|Conclusions and Relevance|Significance|Limitations"
)

#: A listed heading at the start of a line, after a sentence end, or after a
#: label, directly followed by a capitalised word.
WELDED_HEADING = re.compile(
    rf"(?:^|(?<=[.!?])|(?<=: ))[ \t]*(?:{ABSTRACT_HEADINGS})[A-Z][a-z]", re.MULTILINE
)


def body(text: str) -> str:
    """The cache file's text below its YAML frontmatter."""
    if text.startswith("---"):
        parts = text.split("\n---", 1)
        if len(parts) == 2:
            return parts[1]
    return text


def welded_headings(cache_dir: Path = CACHE_DIR) -> dict[Path, list[str]]:
    """Map each cache file with a welded heading to the welds found in it."""
    found: dict[Path, list[str]] = {}
    for path in sorted(cache_dir.glob("*.md")):
        text = body(path.read_text(encoding="utf-8", errors="replace"))
        welds = [match.group(0).strip() for match in WELDED_HEADING.finditer(text)]
        if welds:
            found[path] = welds
    return found


def load_baseline(path: Path = BASELINE) -> dict[str, int]:
    """Grandfathered ``{relative path: weld count}``; empty if no baseline."""
    if not path.is_file():
        return {}
    entries: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        rel, _, count = line.partition("\t")
        entries[rel] = int(count)
    return entries


def new_findings(
    found: dict[Path, list[str]], baseline: dict[str, int], root: Path = ROOT
) -> dict[Path, list[str]]:
    """Findings the baseline does not cover: unlisted files, or more welds than listed."""
    return {
        path: welds
        for path, welds in found.items()
        if len(welds) > baseline.get(str(path.relative_to(root)), 0)
    }


def shrunk_baseline(
    found: dict[Path, list[str]], baseline: dict[str, int], root: Path = ROOT
) -> dict[str, int]:
    """The baseline with fixed entries dropped and counts lowered, never raised."""
    current = {str(path.relative_to(root)): len(welds) for path, welds in found.items()}
    return {
        rel: min(count, current[rel])
        for rel, count in baseline.items()
        if rel in current
    }


def write_baseline(entries: dict[str, int], path: Path = BASELINE) -> None:
    lines = [f"{rel}\t{count}" for rel, count in sorted(entries.items())]
    path.write_text(BASELINE_HEADER + "".join(f"{line}\n" for line in lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--strict", action="store_true", help="fail on every finding, ignoring the baseline")
    parser.add_argument("--update-baseline", action="store_true", help="drop fixed baseline entries (never adds one)")
    args = parser.parse_args(argv)

    if not CACHE_DIR.is_dir():
        print(f"no {CACHE_DIR.relative_to(ROOT)}/ directory; nothing to check.")
        return 0
    total = sum(1 for _ in CACHE_DIR.glob("*.md"))
    found = welded_headings()
    baseline = load_baseline()

    if args.update_baseline:
        shrunk = shrunk_baseline(found, baseline)
        write_baseline(shrunk)
        print(f"baseline: {len(baseline)} -> {len(shrunk)} file(s).")
        return 0

    failing = found if args.strict else new_findings(found, baseline)
    grandfathered = len(found) - len(failing)
    if not failing:
        note = f" ({grandfathered} grandfathered in {BASELINE.relative_to(ROOT)})" if grandfathered else ""
        print(f"OK: no new welded abstract headings in {total} references_cache file(s){note}.")
        return 0

    print("references_cache files with an abstract heading welded onto the next word.\n")
    print("Whole-word quote matching reads 'AbstractCastleman' as one word, so a")
    print("quote starting on the welded word fails. These files were written by a")
    print("linkml-reference-validator older than 0.5.1. Regenerate each one with")
    print("  just fetch-reference --force <ID>")
    print("and never hand-edit a cache file (#16621).\n")
    for path, welds in failing.items():
        shown = ", ".join(welds[:3]) + (" ..." if len(welds) > 3 else "")
        print(f"  {path.relative_to(ROOT)}: {shown}")
    print(f"\n{len(failing)} file(s) with welded headings among {total} cache file(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
