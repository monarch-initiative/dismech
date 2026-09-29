#!/usr/bin/env python3
"""Re-sync KB publication titles to their cached publication.

The companion to ``backfill_reference_titles.py``: that script *adds* a missing
title, this one *corrects* a title that has drifted from the publication it
names. Both take the validator-managed cache in ``references_cache/`` as the
single source of truth.

Why this exists
---------------
``linkml-reference-validator`` compares a declared title against the fetched
publication and errors on a mismatch. It does that for ``PublicationReference.title``
via lrv's exact-name fallback, and for ``EvidenceItem.reference_title`` via the
``implements: - dcterms:title`` annotation on that slot — lrv's ``TitleURIs``
matches only ``dcterms:title`` / ``dc/terms/title``, so that annotation is what
makes the slot visible to it at all.

Turning the check on required clearing thousands of pre-existing disagreements
first; this script is what cleared them, and what keeps them cleared. Run it when
the check starts failing in bulk — typically after a cache refresh moves titles
underneath the KB. A *single* failure is far more likely to be a genuinely wrong
citation, which is the point of the check; re-syncing that one would paper over it.

What counts as a mismatch
-------------------------
Close to what lrv would flag: the comparison uses lrv's own
``SupportingTextValidator.normalize_text``, so cosmetic differences lrv already
tolerates (whitespace, non-breaking spaces, punctuation, case) are left alone.

One deliberate difference: this script does not consult ``skip_prefixes``
(``conf/reference_validator_config.yaml``), which lrv honours, so it re-syncs
titles for prefixes lrv never fetches — ``DOI:`` above all. That makes it
*stricter* than lrv, never laxer, so ``--check`` cannot go green on something
lrv would reject. Keeping a title in step with its cache is worth doing whether
or not a validator polices it, and making the written form depend on a config
list would silently invalidate those titles the day the list changed.

The differences that remain are real ones lrv would report:

- a curator suffix such as ``(Orphanet structured-database record)``
- leftover Crossref markup such as ``<scp><i>ECHS1</i></scp>``
- ASCII-folded accents (``Guillain-Barre`` where the source reads ``Guillain-Barré``)

The yardstick
-------------
Comparison and the written value both use the **raw** frontmatter title, because
that is what lrv compares against. Measuring against a tidied title hides
mismatches lrv reports, and writing a tidied title where tidying changes what lrv
sees actively introduces them (``<italic>TUBA1A</italic>`` normalizes to
``italic tuba1a italic``, not ``tuba1a``). ``resolve_title`` keeps the tidy only
where it is provably equivalent.

Safety
------
Titles are rewritten from cache frontmatter; nothing is invented, and a
reference whose cache entry has no title is skipped and reported. Rewriting is
line-based off ``yaml.compose()`` source marks, so comments, quoting style, key
order and CRLF line endings survive. Every rewritten file is re-parsed and
structurally compared against the original to prove the only values that
changed are title slots.

Usage::

    uv run python scripts/normalize_reference_titles.py            # rewrite all of kb/
    uv run python scripts/normalize_reference_titles.py --dry-run  # report only
    uv run python scripts/normalize_reference_titles.py --check    # exit 1 if any drift
    uv run python scripts/normalize_reference_titles.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from backfill_reference_titles import (
    EVIDENCE_KEYS,
    REFERENCE_KEYS,
    build_title_index,
    lookup_title,
    report_unreadable,
    resolve_title,
    yaml_quote,
)
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)

#: lrv's own comparison, so a difference lrv tolerates is tolerated here too.
#: Prefix coverage still differs -- see "What counts as a mismatch" above.
normalize = SupportingTextValidator.normalize_text

KB_ROOT = Path("kb")


def collect_targets(node, targets: list[dict]) -> None:
    """Collect title nodes whose value has drifted from the cached publication.

    Records the reference id, the line span occupied by the ``<slot>: <value>``
    mapping entry, and the column to re-indent at.
    """
    if isinstance(node, yaml.MappingNode):
        for key_node, value_node in node.value:
            key = getattr(key_node, "value", None)
            slot = None
            if key in EVIDENCE_KEYS:
                slot = "reference_title"
            elif key in REFERENCE_KEYS:
                slot = "title"
            if slot and isinstance(value_node, yaml.SequenceNode):
                for item in value_node.value:
                    if not isinstance(item, yaml.MappingNode):
                        continue
                    entries = {
                        k.value: (k, v) for k, v in item.value if hasattr(k, "value")
                    }
                    if "reference" not in entries or slot not in entries:
                        continue
                    ref_node = entries["reference"][1]
                    title_key, title_val = entries[slot]
                    if not isinstance(ref_node, yaml.ScalarNode):
                        continue
                    if not isinstance(title_val, yaml.ScalarNode):
                        continue
                    end = title_val.end_mark
                    last = end.line - 1 if end.column == 0 else end.line
                    targets.append(
                        {
                            "slot": slot,
                            "reference": ref_node.value,
                            "current": title_val.value,
                            "column": title_key.start_mark.column,
                            "first_line": title_key.start_mark.line,
                            "last_line": last,
                        }
                    )
            collect_targets(value_node, targets)
    elif isinstance(node, yaml.SequenceNode):
        for item in node.value:
            collect_targets(item, targets)


def strip_titles(node):
    """Deep-copy with title slots removed, so the rest can be compared exactly."""
    if isinstance(node, dict):
        return {
            k: strip_titles(v)
            for k, v in node.items()
            if k not in ("reference_title", "title")
        }
    if isinstance(node, list):
        return [strip_titles(v) for v in node]
    return node


def process_file(path: Path, index, lower_index, dry_run: bool) -> dict:
    with path.open("r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    try:
        root = yaml.compose(text)
    except yaml.YAMLError as exc:
        return {"error": f"parse error: {exc}", "fixed": 0, "uncached": []}
    if root is None:
        return {"fixed": 0, "uncached": []}

    targets: list[dict] = []
    collect_targets(root, targets)
    if not targets:
        return {"fixed": 0, "uncached": []}

    lines = text.split("\n")
    edits: list[tuple[int, int, str]] = []
    uncached: list[str] = []
    for t in targets:
        cached = lookup_title(t["reference"], index, lower_index)
        if not cached:
            uncached.append(t["reference"])
            continue
        if normalize(t["current"]) == normalize(cached):
            continue  # lrv would accept this already; leave it alone
        indent = " " * t["column"]
        new_line = f"{indent}{t['slot']}: {yaml_quote(resolve_title(cached))}"
        edits.append((t["first_line"], t["last_line"], new_line))

    if not edits:
        return {"fixed": 0, "uncached": uncached}

    # Apply bottom-up so earlier line indices stay valid.
    for first, last, new_line in sorted(edits, key=lambda e: e[0], reverse=True):
        if first > 0 and lines[first].endswith("\r"):
            new_line += "\r"
        lines[first : last + 1] = [new_line]
    new_text = "\n".join(lines)

    before, after = yaml.safe_load(text), yaml.safe_load(new_text)
    if strip_titles(before) != strip_titles(after):
        return {
            "error": "structural change detected - not written",
            "fixed": 0,
            "uncached": uncached,
        }

    if not dry_run:
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(new_text)
    return {"fixed": len(edits), "uncached": uncached}


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
    parser.add_argument("paths", nargs="*", help="Files or dirs (default: kb/**/*.yaml)")
    parser.add_argument("--dry-run", action="store_true", help="Report only")
    parser.add_argument(
        "--check", action="store_true", help="Report only; exit 1 if any title has drifted"
    )
    args = parser.parse_args()
    dry_run = args.dry_run or args.check

    unreadable: list[str] = []
    index = build_title_index(unreadable=unreadable)
    lower_index = {k.lower(): v for k, v in index.items()}
    print(f"Indexed {len(index)} titled cache entries", file=sys.stderr)
    report_unreadable(unreadable)

    total = files_changed = 0
    uncached: dict[str, int] = {}
    errors: list[str] = []
    files = iter_files(args.paths)
    for path in files:
        stats = process_file(path, index, lower_index, dry_run)
        if stats.get("error"):
            errors.append(f"{path}: {stats['error']}")
        if stats["fixed"]:
            files_changed += 1
            total += stats["fixed"]
            print(f"  {path}: {stats['fixed']} title(s) re-synced", file=sys.stderr)
        for ref in stats["uncached"]:
            uncached[ref] = uncached.get(ref, 0) + 1

    verb = "Would re-sync" if dry_run else "Re-synced"
    print(f"\nScanned {len(files)} files.", file=sys.stderr)
    print(f"{verb} {total} title(s) across {files_changed} file(s).", file=sys.stderr)
    if uncached:
        print(
            f"\n{sum(uncached.values())} title(s) on {len(uncached)} reference(s) "
            "have no cached title and were left untouched:",
            file=sys.stderr,
        )
        for ref, count in sorted(uncached.items()):
            print(f"  {ref}  ({count})", file=sys.stderr)
    if errors:
        print("\nERRORS:", file=sys.stderr)
        for err in errors:
            print(f"  {err}", file=sys.stderr)
        return 1
    if args.check and total:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
