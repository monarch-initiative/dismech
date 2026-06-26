#!/usr/bin/env python3
"""Guard against YAML folded-scalar compound-word splits.

In a YAML *folded* block scalar (``>``, ``>-``, ``>+``) a newline is folded into
a single space. If a content line ends in a hyphenated word and the compound
continues on the next line, folding inserts an unwanted space mid-compound::

    description: >-
      Clinical courses range from relapsing-
      remitting to progressive forms.

renders as ``"... range from relapsing- remitting to progressive forms."`` --
the term ``relapsing-remitting`` is silently broken. This is invisible in the
raw YAML and easy for both humans and AI curators to introduce. See dismech
PR #4799 for the bug that motivated this guard.

Signal
------
A *folded*-scalar content line that ends in ``<word>-``. Legitimate
"suspended hyphens" (``low- and middle-income``) are excluded when the
continuation line begins with a coordinating word (``and``/``or``/``to``/
``vs``/``nor``), since there the trailing space is intended.

Baseline ratchet
----------------
A large pre-existing backlog of these splits already lives in ``kb/`` (tracked
separately). To let this check *gate new occurrences* without first cleaning up
the whole backlog, current findings are grandfathered in
``tests/folded_hyphen_baseline.txt``. ``--check`` (the default, used by the
pytest guard) fails only on findings that are NOT in the baseline. Regenerate
the baseline with ``--update-baseline`` after intentionally changing the set.

Usage
-----
    python scripts/check_folded_hyphens.py            # gate: fail on NEW splits
    python scripts/check_folded_hyphens.py --all      # list every finding
    python scripts/check_folded_hyphens.py --count     # summary counts
    python scripts/check_folded_hyphens.py --update-baseline
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIR = ROOT / "kb"
BASELINE_PATH = ROOT / "tests" / "folded_hyphen_baseline.txt"

# A block-scalar header: a key (or list dash) whose value is a block indicator
# (``>`` folded or ``|`` literal), optionally with chomping/indentation and a
# trailing comment.
HEADER_RE = re.compile(r"(?:^|\s)([>|][-+]?\d*)\s*(?:#.*)?$")
# A line whose last non-space character is a hyphen preceded by an alphanumeric.
EOL_HYPHEN_RE = re.compile(r"[A-Za-z0-9]-$")
# Continuation words that make a trailing hyphen a legitimate suspended hyphen.
COORD_RE = re.compile(r"^(and|or|to|vs|nor|&)\b", re.IGNORECASE)


def _leading_spaces(s: str) -> int:
    return len(s) - len(s.lstrip(" "))


def find_violations_in_text(text: str):
    """Yield (lineno, stripped_line) for folded-scalar hyphen splits in *text*."""
    lines = text.split("\n")
    n = len(lines)
    in_block = False
    block_indent = 0
    block_folded = False

    for i, raw in enumerate(lines):
        if in_block:
            if raw.strip() == "":
                continue  # blank lines stay inside the block scalar
            indent = _leading_spaces(raw)
            if indent > block_indent:
                if block_folded:
                    content = raw.rstrip()
                    if EOL_HYPHEN_RE.search(content):
                        nxt = ""
                        for j in range(i + 1, n):
                            if lines[j].strip() == "":
                                continue
                            if _leading_spaces(lines[j]) > block_indent:
                                nxt = lines[j].strip()
                            break
                        if not COORD_RE.match(nxt):
                            yield (i + 1, content.strip())
                continue
            in_block = False  # de-indented: block ended; re-evaluate this line

        m = HEADER_RE.search(raw)
        if m and not raw.lstrip().startswith("#"):
            in_block = True
            block_indent = _leading_spaces(raw)
            block_folded = m.group(1).startswith(">")


def scan_repo():
    """Return a sorted list of (relpath, lineno, stripped_line) findings."""
    findings = []
    for path in sorted(SCAN_DIR.rglob("*.yaml")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in find_violations_in_text(text):
            findings.append((rel, lineno, line))
    return findings


def _baseline_key(rel: str, line: str) -> str:
    return f"{rel}\t{line}"


def load_baseline() -> set[str]:
    if not BASELINE_PATH.exists():
        return set()
    keys = set()
    for ln in BASELINE_PATH.read_text(encoding="utf-8").splitlines():
        ln = ln.rstrip("\n")
        if ln and not ln.startswith("#"):
            keys.add(ln)
    return keys


def write_baseline(findings) -> None:
    keys = sorted({_baseline_key(rel, line) for rel, _, line in findings})
    header = (
        "# Grandfathered folded-scalar hyphen splits (see "
        "scripts/check_folded_hyphens.py).\n"
        "# Each line is `path<TAB>offending_line`. New occurrences NOT listed\n"
        "# here fail the guard. Remove entries as the backlog is fixed; do not\n"
        "# add new ones. Regenerate with: just update-folded-hyphen-baseline\n"
    )
    BASELINE_PATH.write_text(header + "\n".join(keys) + "\n", encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true",
                   help="(default) fail on findings not in the baseline")
    g.add_argument("--all", action="store_true", help="list every finding")
    g.add_argument("--count", action="store_true", help="print summary counts")
    g.add_argument("--update-baseline", action="store_true",
                   help="rewrite the baseline from current findings")
    args = ap.parse_args(argv)

    findings = scan_repo()

    if args.update_baseline:
        write_baseline(findings)
        print(f"Wrote baseline with {len(findings)} entries to "
              f"{BASELINE_PATH.relative_to(ROOT)}")
        return 0

    if args.all:
        for rel, lineno, line in findings:
            print(f"{rel}:{lineno}: {line}")
        print(f"\n{len(findings)} total folded-scalar hyphen split(s).")
        return 0

    if args.count:
        files = {rel for rel, _, _ in findings}
        baseline = load_baseline()
        new = [f for f in findings if _baseline_key(f[0], f[2]) not in baseline]
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(f"baseline entries: {len(baseline)}")
        print(f"new (non-baselined): {len(new)}")
        return 0

    # default: --check
    baseline = load_baseline()
    new = [f for f in findings if _baseline_key(f[0], f[2]) not in baseline]
    if new:
        print("New folded-scalar compound-word split(s) detected.")
        print("A line inside a YAML folded ('>'/'>-') scalar ends in a hyphen, so")
        print("folding will insert an unwanted space mid-compound (e.g.")
        print("'relapsing- remitting'). Reflow so the compound stays on one line.\n")
        for rel, lineno, line in new:
            print(f"{rel}:{lineno}: {line}")
        print(f"\n{len(new)} new finding(s). If a finding is an intentional")
        print("suspended hyphen, rephrase so the continuation starts with a")
        print("coordinating word, or run --update-baseline to grandfather it.")
        return 1
    print(f"OK: no new folded-scalar hyphen splits "
          f"({len(baseline)} grandfathered in baseline).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
