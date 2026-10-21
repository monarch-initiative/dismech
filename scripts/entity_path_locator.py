#!/usr/bin/env python3
"""Where does a named entity sit inside dismech disease entries?

Parses each KB YAML and reports, for every string match of a search term, the
schema path that holds it (`treatments[].name`, `exposures[].evidence[].snippet`
and so on), plus any ontology term bound on the object that holds the match.

Answers the question a flat grep cannot: is this drug a first-class
`Treatment`/`Exposure` object with a bound term, or only prose inside a
description or an evidence snippet?

Usage:
    entity_path_locator.py --term levodopa --term trifluralin
    entity_path_locator.py --term-file terms.txt --out ../outputs/report.md
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit(
        "error: PyYAML not importable. Run it with uv, e.g.\n"
        "  uv run python scripts/entity_path_locator.py ..."
    )

# Slots that carry a bound ontology term on the object holding a match. Used to
# tell a curated, term-bound mention from a prose one.
# Vendored into dismech: the KB being queried is this checkout, found from the
# script's own location rather than a hard-coded path, so it works in a worktree.
REPO_ROOT = Path(__file__).resolve().parent.parent

TERM_SLOTS = (
    "treatment_term", "exposure_term", "chemical_term", "regimen_term",
    "term", "preferred_term", "id", "label",
)
# Slots whose content is free prose rather than a curated identity.
PROSE_SLOTS = ("description", "snippet", "explanation", "notes", "review_notes", "context")


def repo_commit(repo: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "not-a-git-checkout"


CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.]*:[A-Za-z0-9]")


def _curies(node, path: str):
    """Every CURIE-valued string under this node, with the path that holds it.

    Descends to whatever depth the slot nests to, because the CURIE on a
    treatment or an exposure is two levels down (`<slot>.term.id`) and a
    descriptor can carry further bound terms below that.
    """
    if isinstance(node, str):
        if CURIE_RE.match(node):
            yield path, node
    elif isinstance(node, dict):
        for key, val in node.items():
            if key in PROSE_SLOTS:
                continue
            yield from _curies(val, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for item in node:
            yield from _curies(item, f"{path}[]")


def bound_terms(holder: dict) -> list[str]:
    """The CURIEs bound under the holding object's term-bearing slots.

    A term counts as bound only where a CURIE is actually present. A free-text
    `preferred_term` with no `term` beside it is a label the curator chose, not
    a binding, and reporting it as one is what made every treatment and every
    exposure look term-bound.
    """
    found = []
    for slot in TERM_SLOTS:
        if slot in holder:
            found += [f"{path}={curie}" for path, curie in _curies(holder[slot], slot)]
    return list(dict.fromkeys(found))


def walk(node, pattern: re.Pattern, path: str = "", holder: dict | None = None):
    """Yield (schema_path, slot, matched_text, holder) for each string match."""
    if isinstance(node, dict):
        for key, val in node.items():
            yield from walk(val, pattern, f"{path}.{key}" if path else key, node)
    elif isinstance(node, list):
        for val in node:
            yield from walk(val, pattern, f"{path}[]", holder)
    elif isinstance(node, str) and pattern.search(node):
        slot = path.rsplit(".", 1)[-1]
        yield path, slot, node, holder or {}


def run(repo: Path, terms: list[str], globs: list[str]) -> dict:
    files = []
    for g in globs:
        files += sorted(repo.glob(g))

    results = defaultdict(list)
    parse_errors = []
    for path in files:
        rel = str(path.relative_to(repo))
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError) as exc:
            parse_errors.append({"file": rel, "error": str(exc)[:200]})
            continue
        if doc is None:
            continue
        for term in terms:
            pat = re.compile(re.escape(term), re.IGNORECASE)
            for spath, slot, text, holder in walk(doc, pat):
                results[term].append({
                    "file": rel,
                    "path": spath,
                    "slot": slot,
                    "kind": (
                        "prose" if slot in PROSE_SLOTS
                        else "identity" if slot in ("name", "preferred_term", "label")
                        else "other"
                    ),
                    "bound_terms": bound_terms(holder),
                    "text": text.strip()[:200],
                })

    return {
        "repo": str(repo),
        "commit": repo_commit(repo),
        "generated": datetime.datetime.now(datetime.UTC).date().isoformat(),
        "globs": globs,
        "files_parsed": len(files) - len(parse_errors),
        "parse_errors": parse_errors,
        "terms": terms,
        "results": dict(results),
    }


def report(res: dict) -> str:
    out = [
        "# Where does the entity sit in dismech?",
        "",
        f"- Repo: `{res['repo']}`",
        f"- Commit: `{res['commit']}`",
        f"- Run on: {res['generated']}",
        f"- Files parsed: {res['files_parsed']} from {', '.join('`' + g + '`' for g in res['globs'])}",
        "",
    ]
    if res["parse_errors"]:
        out += ["## Parse errors", ""]
        out += [f"- `{e['file']}`: {e['error']}" for e in res["parse_errors"]]
        out.append("")

    for term in res["terms"]:
        hits = res["results"].get(term, [])
        out += [f"## {term} -- {len(hits)} match(es)", ""]
        if not hits:
            out += ["No match in any parsed file.", ""]
            continue

        out += ["Schema paths, by frequency:", ""]
        for path, n in Counter(h["path"] for h in hits).most_common():
            kinds = {h["kind"] for h in hits if h["path"] == path}
            out.append(f"- `{path}` -- {n} ({'/'.join(sorted(kinds))})")
        out.append("")

        out += ["Matches where a term is bound on the holding object:", ""]
        bound = [h for h in hits if h["bound_terms"]]
        if bound:
            for h in bound:
                out.append(f"- `{h['file']}` `{h['path']}` -- {', '.join(h['bound_terms'])}")
        else:
            out.append("None. No match sits on an object carrying an ontology term.")
        out.append("")

        out += ["Identity slots (a first-class object named for the entity):", ""]
        ident = [h for h in hits if h["kind"] == "identity"]
        if ident:
            for h in ident:
                out.append(f"- `{h['file']}` `{h['path']}` = {h['text']}")
        else:
            out.append("None. The entity is named only in prose or evidence text.")
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--term", action="append", dest="terms", default=[],
                    help="entity name to locate, matched case-insensitively "
                         "against the parsed YAML; repeatable")
    ap.add_argument("--term-file", type=Path, help="file with one term per line")
    ap.add_argument("--repo", default=REPO_ROOT, type=Path)
    ap.add_argument(
        "--glob", action="append", dest="globs",
        help="KB glob, repeatable (default: disorders, modules, groupings)",
    )
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", dest="json_out", type=Path)
    args = ap.parse_args()

    terms = list(args.terms)
    if args.term_file:
        terms += [
            l.strip() for l in args.term_file.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")
        ]
    if not terms:
        print("error: no terms given; pass --term or --term-file", file=sys.stderr)
        return 1

    globs = args.globs or [
        "kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/groupings/*.yaml",
    ]
    res = run(args.repo, terms, globs)
    text = report(res)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(text)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(res, indent=2), encoding="utf-8")
        print(f"wrote {args.json_out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
