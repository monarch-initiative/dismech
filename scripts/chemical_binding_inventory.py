#!/usr/bin/env python3
"""Inventory the ontology-term bindings nested inside dismech disease entries.

dismech has cross-entry homes for genes (`kb/genes/`) and node classes, but
drugs, chemicals and exposures exist only nested inside Disease entries. This
builds the index that does not exist: every bound term, the schema path that
holds it, and the entry it sits in.

Its point is the reverse lookup. Given a chemical, which entries mention it and
in which role -- therapy, exposure, mechanism target? A chemical can be all
three, under different slot paths, so a search on one path silently misses the
others.

Usage:
    chemical_binding_inventory.py --prefix CHEBI --out ../outputs/chebi.md
    chemical_binding_inventory.py --prefix CHEBI --prefix ECTO --prefix XCO \
        --curie CHEBI:5062 --out ../outputs/report.md

Needs PyYAML; run it with uv from the repo root.
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
        "  uv run python scripts/chemical_binding_inventory.py ..."
    )

# Vendored into dismech: the KB being queried is this checkout, found from the
# script's own location rather than a hard-coded path, so it works in a worktree.
REPO_ROOT = Path(__file__).resolve().parent.parent

CURIE = re.compile(r"^([A-Za-z][A-Za-z0-9_.]*):([A-Za-z0-9][A-Za-z0-9_.\-]*)$")

# The top-level Disease slot a path starts in tells you the role the term plays.
#
# For every block `drug_exposure_query.py` also probes, the role named here is
# the one that script reports, so the two outputs can be read side by side or
# joined on the role column -- which the recipe in
# `docs/searching_drugs_and_exposures_in_dismech.md` asks a reader to do. A
# test holds the two vocabularies together. Blocks only this script reaches
# (phenotypes, trials, animal models, diagnosis, modules) name themselves.
ROLE_BY_ROOT = {
    "treatments": "therapy",
    "environmental": "exposure",
    "pathophysiology": "mechanism_node",
    "biochemical": "analyte",
    "datasets": "dataset",
    "computational_models": "model_variable",
    "infectious_agent": "infectious_agent",
    "discussions": "proposed",
    "phenotypes": "phenotype",
    "clinical_trials": "trial",
    "animal_models": "model",
    "diagnosis": "diagnosis",
    "modules": "module",
}


def repo_commit(repo: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "not-a-git-checkout"


def walk(node, path: str = "", parent: dict | None = None):
    """Yield (schema_path, key, value, holding_object) for every scalar."""
    if isinstance(node, dict):
        for key, val in node.items():
            yield from walk(val, f"{path}.{key}" if path else key, node)
    elif isinstance(node, list):
        for val in node:
            yield from walk(val, f"{path}[]", parent)
    else:
        key = path.rsplit(".", 1)[-1].removesuffix("[]")
        yield path, key, node, parent or {}


def label_near(holder: dict, curie: str) -> str:
    """The label recorded alongside a CURIE on the same object."""
    for key in ("label", "name", "preferred_term", "canonical_label"):
        val = holder.get(key)
        if isinstance(val, str) and not CURIE.match(val):
            return val
    return ""


def run(repo: Path, globs: list[str], prefixes: set[str]) -> dict:
    files = []
    for g in globs:
        files += sorted(repo.glob(g))

    bindings = []
    errors = []
    for path in files:
        rel = str(path.relative_to(repo))
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError) as exc:
            errors.append({"file": rel, "error": str(exc)[:200]})
            continue
        if not isinstance(doc, dict):
            continue
        entry = doc.get("name") or rel

        for spath, key, val, holder in walk(doc):
            if not isinstance(val, str):
                continue
            m = CURIE.match(val.strip())
            if not m:
                continue
            prefix = m.group(1)
            if prefixes and prefix.upper() not in prefixes:
                continue
            # A reference slot holds PMID:/DOI: style ids, not ontology terms.
            if key in ("reference", "references") or prefix.upper() in (
                "PMID", "DOI", "NCT", "ISBN", "URL", "HTTP", "HTTPS"
            ):
                continue
            root = spath.split(".", 1)[0].removesuffix("[]")
            bindings.append({
                "file": rel,
                "entry": entry,
                "path": spath,
                "slot": key,
                "root": root,
                "role": ROLE_BY_ROOT.get(root, root),
                "prefix": prefix,
                "curie": val.strip(),
                "label": label_near(holder, val.strip()),
            })

    return {
        "repo": str(repo),
        "commit": repo_commit(repo),
        "generated": datetime.datetime.now(datetime.UTC).date().isoformat(),
        "globs": globs,
        "prefixes": sorted(prefixes) or ["(all)"],
        "files_parsed": len(files) - len(errors),
        "parse_errors": errors,
        "bindings": bindings,
    }


def report(res: dict, focus: list[str]) -> str:
    b = res["bindings"]
    out = [
        "# Nested term bindings in dismech",
        "",
        f"- Repo: `{res['repo']}`",
        f"- Commit: `{res['commit']}`",
        f"- Run on: {res['generated']}",
        f"- Files parsed: {res['files_parsed']} from {', '.join('`' + g + '`' for g in res['globs'])}",
        f"- Prefixes: {', '.join(res['prefixes'])}",
        f"- Bindings found: {len(b)} ({len({x['curie'] for x in b})} distinct terms)",
        "",
        "## Slot paths that hold a binding",
        "",
        "| Schema path | Role | Bindings | Distinct terms |",
        "|---|---|---|---|",
    ]
    by_path = defaultdict(list)
    for x in b:
        by_path[(x["path"], x["role"])].append(x)
    for (path, role), items in sorted(by_path.items(), key=lambda kv: -len(kv[1])):
        out.append(f"| `{path}` | {role} | {len(items)} | {len({i['curie'] for i in items})} |")
    out.append("")

    out += ["## Terms bound under more than one role", "",
            "A term reachable by several paths. Searching one path misses the rest.", ""]
    roles_by_curie = defaultdict(set)
    label_by_curie = {}
    for x in b:
        roles_by_curie[x["curie"]].add(x["role"])
        if x["label"]:
            label_by_curie.setdefault(x["curie"], x["label"])
    multi = {c: r for c, r in roles_by_curie.items() if len(r) > 1}
    if multi:
        out += ["| Term | Label | Roles |", "|---|---|---|"]
        for curie, roles in sorted(multi.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            out.append(f"| `{curie}` | {label_by_curie.get(curie, '')} | {', '.join(sorted(roles))} |")
    else:
        out.append("None.")
    out.append("")

    out += ["## Most-bound terms", "", "| Term | Label | Bindings | Entries |", "|---|---|---|---|"]
    for curie, n in Counter(x["curie"] for x in b).most_common(25):
        entries = len({x["entry"] for x in b if x["curie"] == curie})
        out.append(f"| `{curie}` | {label_by_curie.get(curie, '')} | {n} | {entries} |")
    out.append("")

    for curie in focus:
        hits = [x for x in b if x["curie"].lower() == curie.lower()]
        out += [f"## Reverse lookup: {curie} -- {len(hits)} binding(s)", ""]
        if not hits:
            out += ["Not bound anywhere in the files parsed.", ""]
            continue
        out += ["| Entry | Role | Schema path |", "|---|---|---|"]
        for x in sorted(hits, key=lambda h: (h["entry"], h["path"])):
            out.append(f"| {x['entry']} | {x['role']} | `{x['path']}` |")
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default=REPO_ROOT, type=Path)
    ap.add_argument("--prefix", action="append", dest="prefixes", default=[],
                    help="ontology prefix to keep, repeatable (default: all)")
    ap.add_argument("--curie", action="append", dest="curies", default=[],
                    help="reverse-lookup this term, repeatable")
    ap.add_argument("--glob", action="append", dest="globs")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", dest="json_out", type=Path)
    args = ap.parse_args()

    globs = args.globs or [
        "kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/groupings/*.yaml",
    ]
    res = run(args.repo, globs, {p.upper() for p in args.prefixes})
    text = report(res, args.curies)

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
