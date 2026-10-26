#!/usr/bin/env python3
"""Gate on evidence items that carry no ``reference_title``.

Two structures carry a human-readable publication title:

- Inlined ``EvidenceItem`` entries (the ``evidence:`` and ``literature_evidence:``
  lists, wherever they nest) use the ``reference_title`` slot.
- Top-level ``references:`` entries are ``PublicationReference`` objects and use
  the ``title`` slot.

A blank or absent ``reference_title`` on an evidence item **fails** this check.
It is the presence half of the title guard: ``scripts/check_reference_titles.py``
fails a title that is present and *wrong*, and says nothing about one that was
never written. ``reference_title`` is ``recommended`` in the schema, so
``linkml-validate`` is silent too. This gate holds the backlog at zero ahead of
making the slot ``required``, which would otherwise turn every open curation PR
that omits a title red the moment the schema change merged -- the merge-shaped
failure ``check_enum_values.py`` describes (issue #10061).

Every gap so far has had its title sitting in the reference's
``references_cache/`` frontmatter, so the fix is mechanical and nothing needs to
be typed by hand::

    uv run python scripts/backfill_reference_titles.py kb/disorders/MyDisease.yaml

``PublicationReference.title`` gaps are reported, never gated: the schema
change in prospect is to ``EvidenceItem.reference_title`` only.

One more class is reported rather than gated: an item whose reference **is**
cached but whose cache frontmatter has no ``title:``. There the remedy above
has nothing to copy, and the only way to pass would be to type a title, which
is how fabricated citations get in (issue #9138). PubMed book records are the
known source: ``PMID:23304742``, an AHRQ Comparative Effectiveness Review, comes
back from the fetcher with an empty title even under ``--force``. Those items
stay listed until the fetcher learns to read a book record's title. An item
whose reference is not cached at all still fails: ``just fetch-reference``
fixes that.

No baseline: the KB was backfilled to zero when this became a gate.

Usage::

    uv run python scripts/find_missing_reference_titles.py            # gate
    uv run python scripts/find_missing_reference_titles.py --details  # per-file reference IDs
    uv run python scripts/find_missing_reference_titles.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from linkml_reference_validator.cache import cache_filename

from dismech import kb_cache
from dismech.kb_cache import load_document

#: All of kb/, not just disorders: modules and groupings carry evidence too, and
#: 68 of the 571 gaps found when this became a gate were in kb/modules/.
SCAN_DIR = ROOT / "kb"

#: Keys whose list items are ``EvidenceItem`` objects -- the same pair
#: ``scripts/backfill_reference_titles.py`` fills, so the gate and its remedy
#: cannot disagree about what an evidence item is.
EVIDENCE_KEYS = ("evidence", "literature_evidence")
CACHE_DIR = ROOT / "references_cache"
#: Keys whose list items are ``PublicationReference`` objects.
REFERENCE_KEYS = ("references",)


def is_blank(value: Any) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def cache_has_no_title(reference: Any, cache_dir: Path = CACHE_DIR) -> bool:
    """True when the reference is cached but its frontmatter carries no title.

    False when there is no cache file (that gap is fixable, so it gates) or the
    file has a title (the backfill script can copy it, so it gates).
    """
    if not isinstance(reference, str) or ":" not in reference:
        return False
    # The validator's own naming, so a url: reference (every ":/?=" becomes "_",
    # and the "#fragment" is dropped) resolves to the file it actually wrote.
    path = cache_dir / cache_filename(reference.strip())
    if not path.is_file():
        return False
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0] != "---":
        return False
    for line in lines[1:]:
        if line == "---":
            return True
        if line.startswith("title:") and line[len("title:"):].strip() not in ("", "''", '""'):
            return False
    return False


def walk(node: Any, missing_ev: list, missing_ref: list, location: str = "") -> None:
    """Collect ``(location, reference)`` for items missing their title slot."""
    if isinstance(node, dict):
        for key, val in node.items():
            child = f"{location}.{key}" if location else str(key)
            if isinstance(val, list) and key in EVIDENCE_KEYS + REFERENCE_KEYS:
                slot = "reference_title" if key in EVIDENCE_KEYS else "title"
                bucket = missing_ev if key in EVIDENCE_KEYS else missing_ref
                for index, item in enumerate(val):
                    if (
                        isinstance(item, dict)
                        and "reference" in item
                        and is_blank(item.get(slot))
                    ):
                        bucket.append((f"{child}[{index}]", item.get("reference")))
            # Recurse into every value: evidence nests at arbitrary depth.
            walk(val, missing_ev, missing_ref, child)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            walk(item, missing_ev, missing_ref, f"{location}[{index}]")


def scan(paths: list[Path], rel_to: Path = ROOT) -> list[tuple[str, list, list]]:
    """Return ``(relpath, missing_evidence, missing_references)`` per file with a gap."""
    rows = []
    for path in paths:
        try:
            data = load_document(path)
        except Exception as exc:
            # Malformed YAML is validate-all's to gate; say so rather than
            # letting the file vanish from this check.
            print(
                f"warning: skipping unparseable {path}: {exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        missing_ev: list = []
        missing_ref: list = []
        walk(data, missing_ev, missing_ref)
        if missing_ev or missing_ref:
            try:
                rel = path.resolve().relative_to(rel_to.resolve()).as_posix()
            except ValueError:  # a path given on the command line from elsewhere
                rel = path.as_posix()
            rows.append((rel, missing_ev, missing_ref))
    return rows


def main(argv: list[str] | None = None) -> int:
    # One walk over kb/ per run; the shared-parse cache would only cost memory.
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="*", type=Path, help="Files to check (default: all of kb/).")
    parser.add_argument("--details", action="store_true", help="List each missing item.")
    args = parser.parse_args(argv)

    paths = args.files or sorted(SCAN_DIR.rglob("*.yaml"))
    rows = scan(paths)
    gated = untitled = ref_total = 0

    if rows:
        print(f"{'file':<70} {'evidence':>8} {'references':>10}")
    for rel, ev, ref in rows:
        print(f"{rel:<70} {len(ev):>8} {len(ref):>10}")
        ref_total += len(ref)
        for location, reference in ev:
            if cache_has_no_title(reference):
                untitled += 1
                tag = "evidence (cache has no title; report-only)"
            else:
                gated += 1
                tag = "evidence (no reference_title)"
            if args.details:
                print(f"    {tag}  {location}  {reference}")
        if args.details:
            for location, reference in ref:
                print(f"    references (no title; report-only)  {location}  {reference}")
    print(
        f"\nScanned {len(paths)} files: {gated} evidence item(s) without "
        f"reference_title (gated), {untitled} more whose cached reference has no "
        f"title (report-only), {ref_total} reference(s) without title (report-only)."
    )

    if gated:
        print(
            "\nEvery evidence item needs a reference_title copied from its "
            "references_cache/ frontmatter -- never typed from memory. Fill them with:\n"
            "  uv run python scripts/backfill_reference_titles.py <file> ...\n"
            "If the reference is not cached yet, run `just fetch-reference <ID>` first. "
            "Run with --details to list each item.",
            file=sys.stderr,
        )
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
