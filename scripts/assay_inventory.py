#!/usr/bin/env python3
"""Inventory every assay recorded in dismech, by the route that reaches it.

`AssayDescriptor` is reached only through the `assays:` slot, which four classes
carry -- `Pathophysiology`, `Biochemical`, `ExperimentalReadout` and
`Experiment`. Because `ExperimentalReadout` is reached from two places, that
gives five routes from a disease entry to an assay, and a count taken on one
route says nothing about the others.

This builds the index that does not exist: every assay, the route and schema
path that holds it, the entry it sits in, and whether it is bound to an OBI
term.

Two things the per-route counts are for. An assay on a *proposed experiment* is
a measurement somebody suggested; an assay on a model link's readout is how a
curated model actually measured something. Those are different claims, and
collapsing them reports intent as evidence.

The distinct-name list is the other half, and it reports two classes without
conflating them:

* **mechanical variation** -- names that differ only by punctuation or a
  generic word (`immunoblot` / `immunoblot assay`). Deterministic, safe to act
  on in bulk.
* **candidate synonymy** -- pairs where one name's significant words are
  contained in the other's (`patch clamp recording` inside `patch-clamp
  electrophysiology`). Flagged for a curator, never merged: containment cannot
  tell a narrower assay from a differently-worded one.

Real synonymy with no shared words (`single-cell transcriptomic profiling` and
`single-cell RNA sequencing`) is beyond either class, so neither the clusters
nor the candidates are a deduplicated vocabulary. See dismech#15354 for the
route diagram and dismech#15358 for why this is report-only.

Usage:
    assay_inventory.py
    assay_inventory.py --format tsv --out assays.tsv
    assay_inventory.py --assay "multielectrode array recording"
    assay_inventory.py --glob 'kb/disorders/Dravet_syndrome.yaml' --format json

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
        "  uv run python scripts/assay_inventory.py"
    )

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dismech.model_links import iter_model_links

# `dismech.yaml_io.safe_load` prefers libyaml's CSafeLoader, which exists for
# exactly this: parsing the ~3,900-file corpus with `yaml.safe_load`'s
# pure-Python loader takes about six minutes, against about forty seconds here
# -- measured at 10.7x over 300 entries. Both are safe loaders with the same
# semantics, so this only changes the speed.
from dismech.yaml_io import safe_load

REPO_ROOT = Path(__file__).resolve().parent.parent

#: The five routes from a disease entry to an `AssayDescriptor`, in the order
#: dismech#15354 numbers them. `realized` separates an assay that records how
#: something *was* measured from one on an experiment nobody has run.
ROUTES: dict[str, dict[str, object]] = {
    "pathophysiology": {"number": "1", "realized": True},
    "biochemical": {"number": "2", "realized": True},
    "model_link_readout": {"number": "3", "realized": True},
    "proposed_experiment": {"number": "4a", "realized": False},
    "proposed_experiment_readout": {"number": "4b", "realized": False},
}

#: How many candidate rows the markdown table shows. The full list is always in
#: the JSON output, so this caps the reading, never the result.
CANDIDATE_ROWS_SHOWN = 40

#: Words that describe the *kind* of thing rather than which assay it is, so two
#: names differing only by one of these are the same assay written twice. Kept
#: deliberately short: a word that could name an assay on its own does not
#: belong here, because stripping it would merge two real assays.
GENERIC_WORDS = frozenset(
    {
        "assay",
        "assays",
        "analysis",
        "measurement",
        "profiling",
        "readout",
        "recording",
        "recordings",
        "study",
        "test",
        "testing",
    }
)


def repo_commit(repo: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "not-a-git-checkout"


def significant_tokens(name: str) -> frozenset[str]:
    """The words that say which assay this is, lowercased, generics dropped.

    Two names with the same set differ only mechanically. Two with overlapping
    but unequal sets are candidates for a curator to look at.
    """
    tokens = {t for t in re.split(r"[^a-z0-9]+", name.lower()) if t}
    return frozenset(tokens - GENERIC_WORDS)


def _assays_at(holder: object, path: str, route: str) -> list[dict]:
    """Describe each `AssayDescriptor` in one `assays:` list."""
    if not isinstance(holder, dict):
        return []
    assays = holder.get("assays")
    if not isinstance(assays, list):
        return []
    found = []
    for index, assay in enumerate(assays):
        if not isinstance(assay, dict):
            continue
        term = assay.get("term")
        term = term if isinstance(term, dict) else {}
        name = assay.get("preferred_term") or assay.get("name") or ""
        found.append(
            {
                "route": route,
                "path": f"{path}.assays[{index}]",
                "name": name if isinstance(name, str) else "",
                "curie": term.get("id") or "",
                "label": term.get("label") or "",
                "description": assay.get("description") or "",
            }
        )
    return found


def assays_in_entry(doc: dict) -> list[dict]:
    """Every assay in one loaded entry, tagged with the route that reaches it.

    The five routes are walked explicitly rather than by searching for any
    nested `assays:` key, so each assay is attributed to exactly one route and
    nothing is counted twice. A proposed experiment's own readouts (route 4b)
    and a model link's readouts inside that same experiment (route 3) are
    different lists, and a generic key walk cannot tell them apart.
    """
    found: list[dict] = []

    for index, node in enumerate(doc.get("pathophysiology") or []):
        found += _assays_at(node, f"pathophysiology[{index}]", "pathophysiology")

    for index, marker in enumerate(doc.get("biochemical") or []):
        found += _assays_at(marker, f"biochemical[{index}]", "biochemical")

    # Route 3, via the one walk that reaches all four homes of a model link.
    for site in iter_model_links(doc):
        base = (
            f"{site.path_prefix}[{site.model_index}]"
            f".modeled_mechanisms[{site.link_index}]"
        )
        for index, readout in enumerate(site.link.get("readouts") or []):
            found += _assays_at(
                readout, f"{base}.readouts[{index}]", "model_link_readout"
            )

    for d_index, discussion in enumerate(doc.get("discussions") or []):
        if not isinstance(discussion, dict):
            continue
        for e_index, experiment in enumerate(
            discussion.get("proposed_experiments") or []
        ):
            if not isinstance(experiment, dict):
                continue
            base = f"discussions[{d_index}].proposed_experiments[{e_index}]"
            found += _assays_at(experiment, base, "proposed_experiment")
            for index, readout in enumerate(experiment.get("readouts") or []):
                found += _assays_at(
                    readout,
                    f"{base}.readouts[{index}]",
                    "proposed_experiment_readout",
                )

    return found


def collect(repo: Path, globs: list[str]) -> dict:
    files: list[Path] = []
    for pattern in globs:
        files += sorted(repo.glob(pattern))

    assays: list[dict] = []
    errors: list[dict] = []
    lists_by_route: Counter[str] = Counter()
    files_by_route: defaultdict[str, set[str]] = defaultdict(set)

    for path in files:
        rel = str(path.relative_to(repo))
        try:
            doc = safe_load(path.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError) as exc:
            errors.append({"file": rel, "error": str(exc)[:200]})
            continue
        if not isinstance(doc, dict):
            continue
        entry = doc.get("name") or rel

        holders: set[tuple[str, str]] = set()
        for found in assays_in_entry(doc):
            found["file"] = rel
            found["entry"] = entry
            assays.append(found)
            holders.add((found["route"], found["path"].rsplit(".assays[", 1)[0]))
            files_by_route[found["route"]].add(rel)
        for route, _holder in holders:
            lists_by_route[route] += 1

    return {
        "repo": str(repo),
        "commit": repo_commit(repo),
        "generated": datetime.datetime.now(datetime.UTC).date().isoformat(),
        "globs": globs,
        "files_parsed": len(files) - len(errors),
        "parse_errors": errors,
        "lists_by_route": dict(lists_by_route),
        "files_by_route": {k: sorted(v) for k, v in files_by_route.items()},
        "assays": assays,
    }


def clusters(names: Counter[str]) -> tuple[list[list[str]], list[list[str]]]:
    """Mechanical-variation clusters, and candidate-synonymy pairs.

    The first holds names with identical significant-token sets. The second
    holds pairs where one name's set is contained in the other's, which is a
    question for a curator rather than an answer.

    A name made only of generic words (`assay`, `readout`) reduces to an empty
    token set and is left out of both. The empty set is a subset of every other
    set, so it would otherwise pair with every name in the corpus -- 329 rows
    on the current one -- and it would cluster with any other generic-only name
    as if `assay` and `readout` were one assay written twice. Neither says
    anything, and both would bury the real rows. Such a name is still counted
    in the use table; it is only unclusterable.
    """
    by_key: defaultdict[frozenset[str], list[str]] = defaultdict(list)
    for name in names:
        if name and significant_tokens(name):
            by_key[significant_tokens(name)].append(name)

    mechanical = [
        sorted(group, key=lambda n: (-names[n], n))
        for group in by_key.values()
        if len(group) > 1
    ]
    mechanical.sort(key=lambda g: (-sum(names[n] for n in g), g[0]))

    # Only a subset relation counts as a candidate. Plain overlap does not: one
    # shared weak word ("cell") links `single-cell transcriptomic profiling` to
    # `cell viability assay`, and on this corpus that yields ~1,700 pairs, which
    # is noise rather than a worklist. A subset says one name is the other plus
    # qualifiers -- `patch clamp recording` inside `patch-clamp electrophysiology`
    # -- which is either one assay written two ways or a narrower assay, and
    # that is exactly the distinction a curator has to make.
    keys = sorted(by_key, key=lambda k: (len(k), sorted(k)))
    candidates: list[list[str]] = []
    for i, left in enumerate(keys):
        for right in keys[i + 1 :]:
            if left < right or right < left:
                group = sorted(
                    by_key[left] + by_key[right], key=lambda n: (-names[n], n)
                )
                candidates.append(group)
    candidates.sort(key=lambda g: (-sum(names[n] for n in g), g[0]))
    return mechanical, candidates


def summarize(res: dict) -> dict:
    assays = res["assays"]
    names = Counter(a["name"] for a in assays if a["name"])
    bound = [a for a in assays if a["curie"]]
    realized = [a for a in assays if ROUTES[a["route"]]["realized"]]
    mechanical, candidates = clusters(names)
    return {
        "total": len(assays),
        "bound": len(bound),
        "unnamed": sum(1 for a in assays if not a["name"]),
        "distinct_names": len(names),
        "names": names,
        "realized": len(realized),
        "mechanical": mechanical,
        "candidates": candidates,
    }


def render_md(res: dict, focus: list[str]) -> str:
    s = summarize(res)
    assays = res["assays"]
    by_route = Counter(a["route"] for a in assays)
    bound_by_route = Counter(a["route"] for a in assays if a["curie"])

    out = [
        "# Assays recorded in dismech",
        "",
        f"- Repo: `{res['repo']}`",
        f"- Commit: `{res['commit']}`",
        f"- Run on: {res['generated']}",
        f"- Files parsed: {res['files_parsed']} from "
        + ", ".join("`" + g + "`" for g in res["globs"]),
        f"- Assays: {s['total']} across {s['distinct_names']} distinct names",
        f"- Bound to an OBI term: {s['bound']}",
        f"- On something that was measured, rather than proposed: {s['realized']}",
        "",
    ]
    if s["total"] and not s["bound"]:
        out += [
            (
                "No assay carries an OBI term. `OBI` has no adapter in "
                "`conf/oak_config.yaml` and no `cache/enums/` file, so a "
                "binding could not be validated yet."
            ),
            "",
        ]

    out += [
        "## Routes that reach an assay",
        "",
        "| Route | Schema path | `assays:` lists | Files | Assays | Bound |",
        "|---|---|---|---|---|---|",
    ]
    paths = {
        "pathophysiology": "`pathophysiology[].assays`",
        "biochemical": "`biochemical[].assays`",
        "model_link_readout": "`modeled_mechanisms[].readouts[].assays`",
        "proposed_experiment": "`proposed_experiments[].assays`",
        "proposed_experiment_readout": "`proposed_experiments[].readouts[].assays`",
    }
    for route, meta in sorted(ROUTES.items(), key=lambda kv: -by_route.get(kv[0], 0)):
        out.append(
            f"| {meta['number']} | {paths[route]} "
            f"| {res['lists_by_route'].get(route, 0)} "
            f"| {len(res['files_by_route'].get(route, []))} "
            f"| {by_route.get(route, 0)} | {bound_by_route.get(route, 0)} |"
        )
    out.append("")

    out += [
        "## Most-used assay names",
        "",
        "| Assay | Uses | Entries | Routes |",
        "|---|---|---|---|",
    ]
    for name, count in s["names"].most_common(25):
        hits = [a for a in assays if a["name"] == name]
        routes = sorted({str(ROUTES[h["route"]]["number"]) for h in hits})
        out.append(
            f"| {name} | {count} | {len({h['entry'] for h in hits})} "
            f"| {', '.join(routes)} |"
        )
    out.append("")

    mechanical, candidates = s["mechanical"], s["candidates"]
    covered = sum(s["names"][n] for g in mechanical for n in g)
    out += [
        "## Mechanical variation",
        "",
        (
            f"{len(mechanical)} cluster(s) covering {covered} of "
            f"{s['total']} uses. Each is one assay written more than one way, "
            "differing only by punctuation or a generic word."
        ),
        "",
    ]
    if mechanical:
        out += ["| Names | Uses |", "|---|---|"]
        for group in mechanical:
            shown = " \\| ".join(f"{n} ({s['names'][n]})" for n in group)
            out.append(f"| {shown} | {sum(s['names'][n] for n in group)} |")
    else:
        out.append("None.")
    out.append("")

    out += [
        "## Candidate synonymy",
        "",
        (
            f"{len(candidates)} pair(s) where one name's significant words are "
            "contained in the other's. One row is one such pair, so a name that "
            "contains several others appears in several rows. These are **not** "
            "established duplicates: one name may be a genuinely narrower assay "
            "rather than the same one reworded, and only a curator can say "
            "which. Two names for one assay that share no words are invisible "
            "here, and a name made only of generic words is left out."
        ),
        "",
    ]
    if candidates:
        out += ["| Names |", "|---|"]
        for group in candidates[:CANDIDATE_ROWS_SHOWN]:
            out.append(
                "| " + " \\| ".join(f"{n} ({s['names'][n]})" for n in group) + " |"
            )
        if len(candidates) > CANDIDATE_ROWS_SHOWN:
            out.append("")
            out.append(
                f"Showing {CANDIDATE_ROWS_SHOWN} of {len(candidates)}. The full "
                "list is in `--format json`, under `summary.candidates`; "
                "`--format tsv` is one row per assay and carries none of this."
            )
    else:
        out.append("None.")
    out.append("")

    for wanted in focus:
        hits = [a for a in assays if a["name"].lower() == wanted.lower()]
        out += [f"## Reverse lookup: {wanted} -- {len(hits)} use(s)", ""]
        if not hits:
            out += ["Not recorded anywhere in the files parsed.", ""]
            continue
        out += ["| Entry | Route | Schema path | Bound |", "|---|---|---|---|"]
        for hit in sorted(hits, key=lambda h: (h["entry"], h["path"])):
            out.append(
                f"| {hit['entry']} | {ROUTES[hit['route']]['number']} "
                f"| `{hit['path']}` | {hit['curie'] or '--'} |"
            )
        out.append("")

    if res["parse_errors"]:
        out += ["## Files that would not parse", ""]
        out += [f"- `{e['file']}`: {e['error']}" for e in res["parse_errors"]]
        out.append("")
    return "\n".join(out)


def render_tsv(res: dict) -> str:
    cols = [
        "entry",
        "route",
        "route_number",
        "realized",
        "assay",
        "curie",
        "label",
        "path",
        "file",
    ]
    rows = ["\t".join(cols)]
    for a in res["assays"]:
        meta = ROUTES[a["route"]]
        rows.append(
            "\t".join(
                [
                    a["entry"],
                    a["route"],
                    str(meta["number"]),
                    str(meta["realized"]),
                    a["name"],
                    a["curie"],
                    a["label"],
                    a["path"],
                    a["file"],
                ]
            )
        )
    return "\n".join(rows) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--repo", default=REPO_ROOT, type=Path)
    ap.add_argument(
        "--glob",
        action="append",
        dest="globs",
        help="KB glob, repeatable (default: disorders, modules, comorbidities)",
    )
    ap.add_argument(
        "--assay",
        action="append",
        dest="assays",
        default=[],
        help="reverse-lookup this assay name, repeatable",
    )
    ap.add_argument("--format", choices=("md", "tsv", "json"), default="md")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    if not args.repo.is_dir():
        print(f"error: no such repo: {args.repo}", file=sys.stderr)
        return 1

    globs = args.globs or [
        "kb/disorders/*.yaml",
        "kb/modules/*.yaml",
        "kb/comorbidities/*.yaml",
    ]
    res = collect(args.repo, globs)

    if args.format == "md":
        text = render_md(res, args.assays)
    elif args.format == "tsv":
        text = render_tsv(res)
    else:
        summary = summarize(res)
        text = json.dumps(
            {**res, "summary": {**summary, "names": dict(summary["names"])}}, indent=2
        )

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
