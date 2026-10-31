#!/usr/bin/env python3
"""Guard against YAML structure swallowed into a block scalar.

An evidence item (or any other mapping) inserted at the wrong place in a KB
entry can land *inside* a block scalar, where YAML reads it as prose::

    notes: >-
      ...
      checked before the band is set.

      - reference: PMID:18074387
        supports: SUPPORT
        evidence_source: HUMAN_CLINICAL
        snippet: "Almost 70% of patients ..."

The entry stays schema-valid, because ``notes`` is just a long string, and
``count-verified-snippets`` reports a clean count that silently leaves the
swallowed item out, because it walks parsed objects and this item is not one.
The visible effect is a claim that looks evidenced and is not. See dismech
#11230, and #11169 where it happened.

``check_folded_hyphens.py`` looks at a different symptom of block scalars (a
line-final hyphen) and has no view of structure inside the string, so this is
a separate check.

Signal
------
A parsed string value of at least ``MIN_LENGTH`` characters containing a line
that starts with one of a small set of KB keys (``- reference:``,
``snippet:``, ``supports:``, ``- name:`` and so on; see ``KEY_LINE_RE``). The
key must open the line, which prose that merely mentions ``snippet:``
mid-sentence never does. A ``>-`` scalar folds an item written at the prose's
own indentation onto a single line, so ``FLATTENED_ITEM_RE`` also matches a
``reference: <CURIE>`` followed directly by another evidence-item key,
anywhere in the value. The check reads parsed values, not raw text, so a
key that YAML actually parsed as a key is never flagged.

No baseline
-----------
The KB had no instances when this landed, so every finding fails. If the
detector flags a value that is genuinely correct, teach the detector that
shape and pin it with a test rather than recording an exception, as
``check_folded_hyphens.py`` does.

Usage
-----
    python scripts/check_folded_yaml.py               # gate: fail on any finding
    python scripts/check_folded_yaml.py --all         # list every finding
    python scripts/check_folded_yaml.py --count       # summary counts
    python scripts/check_folded_yaml.py kb/disorders/Asthma.yaml   # specific files
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml

from dismech import kb_cache
from dismech.yaml_io import safe_load

ROOT = Path(__file__).resolve().parents[1]
# The same trees check_folded_hyphens.py scans: ``kb`` for curated content and
# ``src`` for schema prose (enum descriptions sit in block scalars too).
SCAN_DIRS = (ROOT / "kb", ROOT / "src")

# Shorter values cannot hold a swallowed item worth the name.
MIN_LENGTH = 60

# A line inside a string value that opens with a KB key. The key list is the
# one proposed on dismech #11230: the evidence-item keys plus the commonest
# list-item and descriptor keys a mis-placed block would start with.
KEY_LINE_RE = re.compile(
    r"(?m)^\s*(- reference:|reference:|snippet:|evidence_source:|supports:"
    r"|- target:|phenotype_term:|treatment_term:|- name:)\s"
)

# The same item folded onto one line. When the swallowed block sits at the
# prose's own indentation with no blank line before it, ``>-`` joins every
# line with a space, so no key opens a line and KEY_LINE_RE sees nothing. A
# ``reference: <CURIE>`` followed directly by another evidence-item key is
# that shape; prose has no reason to write it.
FLATTENED_ITEM_RE = re.compile(
    r"(?:^|\s)(?:- )?reference: [A-Za-z][\w.-]*:\S+"
    r"\s+(?:reference_title|supports|evidence_source|snippet|explanation"
    r"|directness|quote_role):\s"
)


def _iter_strings(node: Any, path: str) -> Iterator[tuple[str, str]]:
    """Yield (yaml_path, value) for every string value under *node*."""
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else str(key)
            yield from _iter_strings(value, child)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from _iter_strings(value, f"{path}[{i}]")


def find_violations_in_document(document: Any) -> Iterator[tuple[str, str]]:
    """Yield (yaml_path, offending_line) for swallowed structure in *document*."""
    for path, value in _iter_strings(document, ""):
        if len(value) < MIN_LENGTH:
            continue
        for m in KEY_LINE_RE.finditer(value):
            line_start = value.rfind("\n", 0, m.start(1)) + 1
            line_end = value.find("\n", m.start(1))
            if line_end == -1:
                line_end = len(value)
            yield path or "<root>", value[line_start:line_end].strip()
        if not KEY_LINE_RE.search(value):
            for m in FLATTENED_ITEM_RE.finditer(value):
                yield path or "<root>", m.group(0).strip()


def find_violations_in_text(text: str) -> list[tuple[str, str]]:
    """Parse *text* as YAML and return its findings (for tests and callers)."""
    return list(find_violations_in_document(safe_load(text)))


def _collect_paths(args: list[str]) -> list[Path]:
    if not args:
        return sorted(p for d in SCAN_DIRS for p in d.rglob("*.yaml"))
    paths: list[Path] = []
    for arg in args:
        p = Path(arg)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        if p.is_dir():
            paths.extend(sorted(p.rglob("*.yaml")))
        else:
            paths.append(p)
    return paths


def _rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def scan_repo(paths: list[Path] | None = None):
    """Return (findings, unparsed).

    ``findings`` is a sorted list of (relpath, yaml_path, line); ``unparsed``
    lists (relpath, error) for files that do not load as a single YAML
    document, which other gates own.
    """
    findings = []
    unparsed = []
    if paths is None:
        paths = _collect_paths([])
    for path in paths:
        rel = _rel(path)
        try:
            document = kb_cache.load_document(path)
        except yaml.YAMLError as exc:
            unparsed.append((rel, str(exc).splitlines()[0]))
            continue
        for yaml_path, line in find_violations_in_document(document):
            findings.append((rel, yaml_path, line))
    return findings, unparsed


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true", help="(default) fail on any finding")
    g.add_argument("--all", action="store_true", help="list every finding")
    g.add_argument("--count", action="store_true", help="print summary counts")
    ap.add_argument(
        "paths", nargs="*", help="YAML files or directories (default: kb/ and src/)"
    )
    args = ap.parse_args(argv)

    # One walk over the corpus: the parse cache would only cost memory.
    kb_cache.default_off()
    findings, unparsed = scan_repo(_collect_paths(args.paths))
    for rel, err in unparsed:
        print(
            f"warning: {rel}: not checked, YAML did not parse: {err}", file=sys.stderr
        )

    if args.all:
        for rel, yaml_path, line in findings:
            print(f"{rel}: {yaml_path}: {line}")
        print(f"\n{len(findings)} total swallowed-structure finding(s).")
        return 0

    if args.count:
        files = {rel for rel, _, _ in findings}
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        return 0

    # default: --check
    if findings:
        print("YAML structure swallowed into a string value detected.")
        print("A string value contains a line that opens with a KB key such as")
        print("'- reference:' or 'snippet:', which usually means a block was")
        print("inserted inside a '>-' or '|' scalar and YAML read it as prose.")
        print("Move the block out of the scalar to where it belongs.\n")
        for rel, yaml_path, line in findings:
            print(f"{rel}: {yaml_path}: {line}")
        print(f"\n{len(findings)} finding(s). There is no baseline: if a value")
        print("is genuinely correct, teach the detector that shape, with a test.")
        return 1
    print("OK: no YAML structure inside string values.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
