#!/usr/bin/env python3
"""Backfill missing publication titles on KB references and evidence items.

Two structures carry a human-readable publication title:

- Inlined ``EvidenceItem`` entries (the ``evidence:`` and ``literature_evidence:``
  lists, wherever they appear in the tree) use the ``reference_title`` slot.
- Top-level ``references:`` entries are ``PublicationReference`` objects and use
  the ``title`` slot.

Titles are read **verbatim** from the ``reference_id`` / ``title`` frontmatter of
the validator-managed cache files in ``references_cache/``. Nothing is ever
fabricated: a reference with no cached title is reported and left untouched. The
cache is never written to by this script — fetch missing entries first with
``just fetch-reference <ID>``.

Insertion is done line-by-line using the source marks from ``yaml.compose()``,
so the rest of each file (comments, quoting style, block scalars, key order) is
byte-identical afterwards. Every rewritten file is re-parsed and structurally
diffed against the original to prove that the only change is the added titles.

Usage::

    uv run python scripts/backfill_reference_titles.py            # rewrite all of kb/
    uv run python scripts/backfill_reference_titles.py --dry-run  # report only
    uv run python scripts/backfill_reference_titles.py --check    # exit 1 if any missing
    uv run python scripts/backfill_reference_titles.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

import yaml
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator as _STV,
)
from ruamel.yaml import YAML

#: lrv's own comparison, so this module measures titles exactly as lrv does.
_normalize = _STV.normalize_text

KB_ROOT = Path("kb")
CACHE_DIR = Path("references_cache")

#: Keys whose list items are ``EvidenceItem`` objects (title slot: reference_title).
EVIDENCE_KEYS = ("evidence", "literature_evidence")
#: Keys whose list items are ``PublicationReference`` objects (title slot: title).
REFERENCE_KEYS = ("references",)

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
#: Formatting-only markup that Crossref/PubMed titles sometimes carry. Deliberately
#: an allow-list so non-markup angle brackets (e.g. "<TM>", "c.1258A>G") survive.
_MARKUP_TAG_RE = re.compile(
    r"</?(?:i|b|em|strong|sup|sub|scp|u|span|p|it|italic|bold)\s*/?>",
    re.IGNORECASE,
)


def clean_title(raw: str) -> str:
    """Tidy a cached title: unescape entities, drop formatting tags, fold space.

    This is a *display* tidy, not the value to write blindly — see
    ``resolve_title``, which decides when tidying is safe.
    """
    title = raw
    # Some Crossref titles are double-escaped (&lt;i&gt;...); unescape twice.
    for _ in range(2):
        unescaped = html.unescape(title)
        if unescaped == title:
            break
        title = unescaped
    title = _MARKUP_TAG_RE.sub("", title)
    return re.sub(r"\s+", " ", title).strip()


def resolve_title(raw: str) -> str:
    """The value to write into YAML for a cached title.

    linkml-reference-validator compares ``normalize_text(<yaml title>)`` against
    ``normalize_text(<RAW frontmatter title>)``, and its ``normalize_text`` maps
    ``[^\\w\\s]`` to a *space* rather than deleting it. Markup and HTML entities
    therefore survive normalization as words: ``<italic>TUBA1A</italic>`` becomes
    ``italic tuba1a italic`` and ``&amp;`` becomes ``amp``.

    So the tidied title is only safe to write when tidying does not change what
    lrv sees. Where it does, the raw title is the only value that validates —
    prefer readability, fall back to correctness.
    """
    cleaned = clean_title(raw)
    return cleaned if _normalize(cleaned) == _normalize(raw) else raw


def _load_frontmatter(text: str):
    """Parse cache frontmatter exactly as lrv does.

    ruamel is not an optional dependency here: this module imports lrv at the
    top for ``normalize_text``, and lrv itself requires ruamel.
    """
    return YAML(typ="safe").load(text)


def build_title_index(
    cache_dir: Path = CACHE_DIR, unreadable: list[str] | None = None
) -> dict[str, str]:
    """Map ``reference_id`` -> RAW frontmatter title for every cache file with one.

    Deliberately raw, not cleaned: this index is the yardstick a title is compared
    against, and lrv compares against the raw value. Apply ``resolve_title`` at the
    point of writing.

    Keyed off the frontmatter ``reference_id`` rather than the filename, because
    the validator's filename sanitisation is lossy (``?``/``=``/``/`` all become
    ``_``).

    Parsed with ruamel, because that is what lrv uses
    (``ReferenceFetcher._load_markdown_format`` calls ``YAML(typ="safe")``). The
    two disagree on real cache files: PubMed titles occasionally carry U+2028 /
    U+2029, which the fetcher writes into an unquoted scalar. PyYAML treats those
    as line breaks and raises, so ``PMID:27951541`` looked title-less here while
    lrv read it fine and checked it -- the reader equivalent of the operand bug
    ``resolve_title`` fixes.

    An unreadable cache entry is *reported*, not silently skipped. Swallowing the
    parse error is what let PMID:27951541 masquerade as title-less for as long as
    it did, so ``unreadable`` collects those paths and callers print them.
    """
    index: dict[str, str] = {}
    unreadable = [] if unreadable is None else unreadable
    for path in sorted(cache_dir.glob("*.md")):
        match = _FRONTMATTER_RE.match(path.read_text(errors="replace"))
        if not match:
            unreadable.append(f"{path.name}: no frontmatter block")
            continue
        try:
            frontmatter = _load_frontmatter(match.group(1))
        except Exception as exc:
            unreadable.append(f"{path.name}: {type(exc).__name__}")
            continue
        if not isinstance(frontmatter, dict):
            unreadable.append(f"{path.name}: frontmatter is not a mapping")
            continue
        ref_id = frontmatter.get("reference_id")
        title = frontmatter.get("title")
        if not ref_id or not title or not str(title).strip():
            continue
        index[str(ref_id)] = str(title).strip()
    return index


def report_unreadable(unreadable: list[str], limit: int = 10) -> None:
    """Announce cache entries whose frontmatter could not be read.

    Without this an unreadable entry is indistinguishable from a title-less one,
    which is precisely how the PMID:27951541 blind spot survived.

    This warning is a diagnostic, not the gate. ``just check-reference-cache-frontmatter``
    (``dismech.reference_cache_frontmatter``) already fails on frontmatter this cannot
    read, and it parses with ruamel exactly as lrv and this module do. It runs in
    ``just qc``, as an ungated CI step, and via the real-cache sweep in
    ``tests/test_reference_cache_frontmatter.py`` -- so a corrupted cache turns CI red
    long before anyone runs ``--check``. That is why ``--check`` reports these without
    failing on them: the coverage hole is gated upstream, and failing here too would
    only duplicate it in a manual command.
    """
    if not unreadable:
        return
    print(
        f"\nWARNING: {len(unreadable)} cache file(s) have unreadable frontmatter "
        "and were skipped. Titles on these references cannot be checked "
        "(just check-reference-cache-frontmatter gates this):",
        file=sys.stderr,
    )
    for entry in unreadable[:limit]:
        print(f"  {entry}", file=sys.stderr)
    if len(unreadable) > limit:
        print(f"  ... and {len(unreadable) - limit} more", file=sys.stderr)


def lookup_title(reference: str, index: dict[str, str], lower_index: dict[str, str]):
    """Resolve a title, tolerating prefix-case drift (``geo:`` vs ``GEO:``)."""
    if reference in index:
        return index[reference]
    return lower_index.get(reference.lower())


def yaml_quote(value: str) -> str:
    """Render a string as a YAML double-quoted scalar.

    JSON string escaping is a strict subset of YAML's double-quoted escaping, so
    ``json.dumps`` is a safe (and correct) way to quote arbitrary titles.
    """
    return json.dumps(value, ensure_ascii=False)


def _blank(value) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def collect_targets(node, targets: list[dict]) -> None:
    """Walk a composed node tree collecting reference entries lacking a title.

    Each target records the title slot to add, the reference id, the column to
    indent the new key at, and the line index to insert it after.
    """
    if isinstance(node, yaml.MappingNode):
        for key_node, value_node in node.value:
            key = getattr(key_node, "value", None)
            title_slot = None
            if key in EVIDENCE_KEYS:
                title_slot = "reference_title"
            elif key in REFERENCE_KEYS:
                title_slot = "title"
            if title_slot and isinstance(value_node, yaml.SequenceNode):
                for item in value_node.value:
                    if not isinstance(item, yaml.MappingNode):
                        continue
                    entries = {
                        k.value: v for k, v in item.value if hasattr(k, "value")
                    }
                    ref_node = entries.get("reference")
                    if ref_node is None or not isinstance(ref_node, yaml.ScalarNode):
                        continue
                    existing = entries.get(title_slot)
                    if existing is not None and not _blank(
                        getattr(existing, "value", None)
                    ):
                        continue
                    ref_key_node = next(
                        k for k, _ in item.value if getattr(k, "value", None) == "reference"
                    )
                    end = ref_node.end_mark
                    insert_at = end.line if end.column == 0 else end.line + 1
                    targets.append(
                        {
                            "slot": title_slot,
                            "reference": ref_node.value,
                            "column": ref_key_node.start_mark.column,
                            "insert_at": insert_at,
                        }
                    )
            collect_targets(value_node, targets)
    elif isinstance(node, yaml.SequenceNode):
        for item in node.value:
            collect_targets(item, targets)


def strip_added_titles(node):
    """Deep-copy a parsed document with all title slots removed, for diffing."""
    if isinstance(node, dict):
        return {
            k: strip_added_titles(v)
            for k, v in node.items()
            if k not in ("reference_title", "title")
        }
    if isinstance(node, list):
        return [strip_added_titles(v) for v in node]
    return node


def process_file(
    path: Path,
    index: dict[str, str],
    lower_index: dict[str, str],
    dry_run: bool,
) -> dict:
    """Backfill one YAML file. Returns per-file stats."""
    # newline="" keeps CRLF files byte-identical apart from the inserted lines;
    # the default universal-newline read would silently rewrite the whole file.
    with path.open("r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    try:
        root = yaml.compose(text)
    except yaml.YAMLError as exc:
        return {"error": f"parse error: {exc}", "added": 0, "unresolved": []}
    if root is None:
        return {"added": 0, "unresolved": []}

    targets: list[dict] = []
    collect_targets(root, targets)
    if not targets:
        return {"added": 0, "unresolved": []}

    lines = text.split("\n")
    insertions: list[tuple[int, str]] = []
    unresolved: list[str] = []
    for target in targets:
        title = lookup_title(target["reference"], index, lower_index)
        if not title:
            unresolved.append(target["reference"])
            continue
        indent = " " * target["column"]
        insertions.append(
            (
                target["insert_at"],
                f"{indent}{target['slot']}: {yaml_quote(resolve_title(title))}",
            )
        )

    if not insertions:
        return {"added": 0, "unresolved": unresolved}

    # Insert bottom-up so earlier line indices stay valid. Stable sort keeps the
    # original order of any two insertions landing on the same line.
    for line_no, new_line in sorted(insertions, key=lambda t: t[0], reverse=True):
        # Match the line ending of the reference line we are inserting after.
        if line_no > 0 and lines[line_no - 1].endswith("\r"):
            new_line += "\r"
        lines.insert(line_no, new_line)
    new_text = "\n".join(lines)

    # Safety net: the rewritten document must differ from the original only by
    # the added title slots.
    before = yaml.safe_load(text)
    after = yaml.safe_load(new_text)
    if strip_added_titles(before) != strip_added_titles(after):
        return {
            "error": "structural change detected - not written",
            "added": 0,
            "unresolved": unresolved,
        }

    if not dry_run:
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(new_text)
    return {"added": len(insertions), "unresolved": unresolved}


def iter_files(paths: list[str]) -> list[Path]:
    if not paths:
        return sorted(KB_ROOT.rglob("*.yaml"))
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        files.extend(sorted(p.rglob("*.yaml")) if p.is_dir() else [p])
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or directories to process (default: every kb/**/*.yaml)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Report what would change; write nothing"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report only, and exit 1 if any reference still lacks a title",
    )
    args = parser.parse_args()
    dry_run = args.dry_run or args.check

    unreadable: list[str] = []
    index = build_title_index(unreadable=unreadable)
    lower_index = {k.lower(): v for k, v in index.items()}
    print(f"Indexed {len(index)} titled cache entries from {CACHE_DIR}/", file=sys.stderr)
    report_unreadable(unreadable)

    total_added = 0
    files_changed = 0
    all_unresolved: dict[str, int] = {}
    errors: list[str] = []

    files = iter_files(args.paths)
    for path in files:
        stats = process_file(path, index, lower_index, dry_run)
        if stats.get("error"):
            errors.append(f"{path}: {stats['error']}")
        if stats["added"]:
            files_changed += 1
            total_added += stats["added"]
            print(f"  {path}: +{stats['added']} titles", file=sys.stderr)
        for ref in stats["unresolved"]:
            all_unresolved[ref] = all_unresolved.get(ref, 0) + 1

    verb = "Would add" if dry_run else "Added"
    print(f"\nScanned {len(files)} files.", file=sys.stderr)
    print(f"{verb} {total_added} titles across {files_changed} files.", file=sys.stderr)

    if all_unresolved:
        print(
            f"\n{sum(all_unresolved.values())} item(s) across "
            f"{len(all_unresolved)} reference(s) have no cached title "
            f"(run `just fetch-reference <ID>`):",
            file=sys.stderr,
        )
        for ref, count in sorted(all_unresolved.items()):
            print(f"  {ref}  ({count} item(s))", file=sys.stderr)

    if errors:
        print("\nERRORS:", file=sys.stderr)
        for err in errors:
            print(f"  {err}", file=sys.stderr)
        return 1

    if args.check and (total_added or all_unresolved):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
