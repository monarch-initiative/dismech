#!/usr/bin/env python3
"""Inventory the diseases and mechanisms a drug or environmental factor reaches.

Takes one query term -- a drug, an environmental factor, or something that is
both -- and walks every place in the dismech `Disease` class that can hold a
chemical or exposure, then follows the two mechanism-link slots to the
pathograph nodes the term acts on:

    treatments[].target_mechanisms[].target       -> pathophysiology[].name
    environmental[].influences_mechanisms[].target -> pathophysiology[].name

A term can occupy several roles at once, under different vocabularies: a drug is
CHEBI or NCIT on `therapeutic_agent`, while the exposure to that same drug is an
ECTO or XCO exposure EVENT with a different CURIE. Nothing in an entry links the
two, so this searches both and reports the roles side by side.

Usage:
    drug_exposure_query.py --term finasteride
    drug_exposure_query.py --term 5-fluorouracil --format tsv
    drug_exposure_query.py --curie CHEBI:5062 --curie ECTO:9001833 --out report.md

Needs PyYAML; run it with uv from the repo root:
    uv run python scripts/drug_exposure_query.py ...
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit(
        "error: PyYAML not importable. Run it with uv, e.g.\n"
        "  uv run python scripts/drug_exposure_query.py --term finasteride"
    )

# Vendored into dismech: the KB being queried is this checkout, found from the
# script's own location rather than a hard-coded path, so it works in a worktree.
REPO_ROOT = Path(__file__).resolve().parent.parent

CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_.]*):([A-Za-z0-9][A-Za-z0-9_.\-]*)$")

# Every place a chemical, drug or exposure term can sit, from the schema tree in
# docs/searching_drugs_and_exposures_in_dismech.md. Each probe says how to reach
# the holding objects from the Disease root, which role it represents, and which
# slot on the holder carries the mechanism links.
#
#   block      top-level Disease slot (a list)
#   role       what the term is doing there
#   term_paths dotted paths from the holder to a term object, [] = list
#   links      the holder's mechanism-link slot, if any
#   effect     the direction field on that link
PROBES = [
    {
        "block": "treatments", "role": "therapy",
        "term_paths": [
            "treatment_term.therapeutic_agent[].term",       # the drug itself
            "treatment_term.term",                           # the action, not the drug
            "treatment_term.regimen_term.term",
            "treatment_term.dietary_modifications[].food.term",
            "treatment_term.qualifiers[].value.term",
            "regimen_term.term",
        ],
        "agent_paths": ["treatment_term.therapeutic_agent[].term"],
        # On a TreatmentDescriptor, preferred_term names the treatment as a whole
        # ("levodopa pharmacotherapy") while its term is only the action
        # (NCIT:C15986). Trusting it here resolves the action CURIE as though it
        # were the drug, so the action slot does not get that signal.
        "action_paths": ["treatment_term.term"],
        "links": "target_mechanisms", "effect": "treatment_effect",
    },
    {
        "block": "environmental", "role": "exposure",
        "term_paths": [
            "exposure_term.term",
            "exposure_term.qualifiers[].value.term",
            "environment_context.term",
            "food_source.term",
        ],
        "agent_paths": ["exposure_term.term"],
        "links": "influences_mechanisms", "effect": "environmental_effect",
    },
    {
        "block": "pathophysiology", "role": "mechanism_node",
        "term_paths": ["chemical_entities[].term", "triggers[].term"],
        "agent_paths": ["chemical_entities[].term"],
        "links": None, "effect": None,
    },
    {
        "block": "biochemical", "role": "analyte",
        "term_paths": ["biomarker_term.term", "mappings_list[].term"],
        "agent_paths": ["biomarker_term.term"],
        "links": None, "effect": None,
    },
    {
        "block": "datasets", "role": "dataset",
        "term_paths": ["exposures[].term"],
        "agent_paths": ["exposures[].term"],
        "links": None, "effect": None,
    },
    {
        "block": "computational_models", "role": "model_variable",
        "term_paths": ["variables[].mappings_list[].term"],
        "agent_paths": [],
        "links": None, "effect": None,
    },
    {
        "block": "infectious_agent", "role": "infectious_agent",
        "term_paths": ["food_source.term"],
        "agent_paths": [],
        "links": None, "effect": None,
    },
]

# Proposed, not asserted: reported separately so it never mixes with curated claims.
PROPOSED_PROBE = {
    "block": "discussions", "role": "proposed",
    "nested": "proposed_experiments[].perturbations[]",
    "term_paths": [
        "chemical_entities[].term", "exposure_term.term", "treatment_term.term",
    ],
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


def walk_path(obj, path: str):
    """Yield every object reached by a dotted path, where `[]` spreads a list."""
    if not path:
        yield obj
        return
    head, _, rest = path.partition(".")
    spread = head.endswith("[]")
    key = head[:-2] if spread else head
    if not isinstance(obj, dict):
        return
    val = obj.get(key)
    if val is None:
        return
    if spread:
        if not isinstance(val, list):
            return
        for item in val:
            yield from walk_path(item, rest)
    else:
        yield from walk_path(val, rest)


def walk_terms(holder, path: str):
    """Yield (term, preferred_term) for every term reached by a term path.

    `preferred_term` sits on the descriptor that carries the term, one level
    above it, and it is often the clinical name where the bound label is a
    systematic one: `CHEBI:15765` is labelled `L-dopa` and preferred as
    `levodopa`. Matching the label alone misses the substance that the
    treatments actually point at, which is the whole trap this script exists
    to avoid falling into.
    """
    parent_path, sep, leaf = path.rpartition(".")
    if sep and leaf == "term":
        for parent in walk_path(holder, parent_path):
            if isinstance(parent, dict) and parent.get("term") is not None:
                yield parent["term"], str(parent.get("preferred_term") or "")
    else:
        for term in walk_path(holder, path):
            yield term, ""


def term_id_label(term) -> tuple[str, str]:
    """A term object is {id, label}; tolerate a bare CURIE string."""
    if isinstance(term, dict):
        return str(term.get("id") or ""), str(term.get("label") or "")
    if isinstance(term, str):
        return term, ""
    return "", ""


class Query:
    """What the user asked for, and what it resolved to."""

    def __init__(self, terms: list[str], curies: list[str]):
        self.terms = [t.lower() for t in terms]
        self.curies = {c.upper() for c in curies}
        self.resolved: dict[str, set[str]] = defaultdict(set)   # curie -> labels

    def in_text(self, raw: str) -> bool:
        """Could this file hold a match at all? A cheap prefilter before parsing."""
        low = raw.lower()
        if any(t in low for t in self.terms):
            return True
        return any(c.lower() in low for c in self.curies)

    def matches_term(self, curie: str, label: str, holder_name: str,
                     preferred: str = "") -> str | None:
        """Why this binding matched: by CURIE, by term label, by the descriptor's
        preferred_term, or by holder name."""
        if curie and curie.upper() in self.curies:
            return "curie"
        if self.terms:
            lab = label.lower()
            pref = (preferred or "").lower()
            nam = (holder_name or "").lower()
            for t in self.terms:
                if lab and t in lab:
                    return "label"
                if pref and t in pref:
                    return "preferred_term"
                if nam and t in nam:
                    return "name"
        return None


def collect(repo: Path, globs: list[str], q: Query) -> dict:
    files = []
    for g in globs:
        files += sorted(repo.glob(g))

    hits, proposed, errors = [], [], []
    skipped = 0
    for path in files:
        rel = str(path.relative_to(repo))
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            errors.append({"file": rel, "error": str(exc)[:200]})
            continue
        # Parsing every entry costs about a minute over the whole KB, and a query
        # term appears in a handful of files. A substring test on the raw text
        # cannot miss a hit, since every match below is a substring of the file.
        if not q.in_text(raw):
            skipped += 1
            continue
        try:
            doc = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            errors.append({"file": rel, "error": str(exc)[:200]})
            continue
        if not isinstance(doc, dict):
            continue

        entry = doc.get("name") or rel
        disease_term = (doc.get("disease_term") or {}).get("term") or {}
        # Node names available for the foreign-key check on a mechanism link.
        node_names = {
            n.get("name") for n in (doc.get("pathophysiology") or [])
            if isinstance(n, dict) and n.get("name")
        } | {
            p.get("name") for p in (doc.get("phenotypes") or [])
            if isinstance(p, dict) and p.get("name")
        }

        for probe in PROBES:
            block = doc.get(probe["block"])
            if block is None:
                continue
            holders = block if isinstance(block, list) else [block]
            for holder in holders:
                if not isinstance(holder, dict):
                    continue
                for tp in probe["term_paths"]:
                    trust_preferred = tp not in probe.get("action_paths", ())
                    for term, preferred in walk_terms(holder, tp):
                        curie, label = term_id_label(term)
                        why = q.matches_term(curie, label, holder.get("name", ""),
                                             preferred if trust_preferred else "")
                        if not why:
                            continue
                        # A holder-name match says the HOLDER is about the query, not
                        # that this term is the query: a treatment named for one drug
                        # also binds its co-drugs and its action term. Those must not
                        # enter the resolved-term list.
                        if curie and why in ("curie", "label", "preferred_term"):
                            q.resolved[curie].add(label)
                        hits.append({
                            "file": rel,
                            "entry": entry,
                            "disease_curie": disease_term.get("id", ""),
                            "role": probe["role"],
                            "holder": holder.get("name", "") or "(unnamed)",
                            "term_path": f"{probe['block']}[].{tp}",
                            "is_agent_slot": tp in probe["agent_paths"],
                            "curie": curie,
                            "label": label,
                            "matched_by": why,
                            "mechanisms": mechanism_links(holder, probe, node_names),
                        })

        # Proposed experiments, kept apart from asserted content.
        for disc in (doc.get(PROPOSED_PROBE["block"]) or []):
            if not isinstance(disc, dict):
                continue
            for pert in walk_path(disc, PROPOSED_PROBE["nested"]):
                if not isinstance(pert, dict):
                    continue
                for tp in PROPOSED_PROBE["term_paths"]:
                    for term in walk_path(pert, tp):
                        curie, label = term_id_label(term)
                        why = q.matches_term(curie, label, disc.get("prompt", ""))
                        if why:
                            proposed.append({
                                "file": rel, "entry": entry, "curie": curie,
                                "label": label, "term_path": tp, "matched_by": why,
                            })

    return {
        "repo": str(repo), "commit": repo_commit(repo),
        "generated": datetime.datetime.now(datetime.UTC).date().isoformat(),
        "globs": globs, "files_considered": len(files),
        "files_parsed": len(files) - len(errors) - skipped,
        "files_skipped_by_prefilter": skipped,
        "query_terms": q.terms, "query_curies": sorted(q.curies),
        "resolved": {c: sorted(l for l in labs if l) for c, labs in sorted(q.resolved.items())},
        "hits": hits, "proposed": proposed, "parse_errors": errors,
    }


def mechanism_links(holder: dict, probe: dict, node_names: set) -> list[dict]:
    """The pathograph nodes this holder acts on, with direction and FK status."""
    if not probe["links"]:
        return []
    out = []
    for link in (holder.get(probe["links"]) or []):
        if not isinstance(link, dict):
            continue
        target = link.get("target", "")
        out.append({
            "target": target,
            "effect": link.get(probe["effect"], "") or "",
            "causal_link_type": link.get("causal_link_type", "") or "",
            "resolves": target in node_names,
            "evidence_items": len(link.get("evidence") or []),
        })
    return out


def render_md(res: dict) -> str:
    hits = res["hits"]
    out = [
        "# Drug / exposure query: diseases and mechanisms reached",
        "",
        f"- Query terms: {', '.join(res['query_terms']) or '(none)'}",
        f"- Query CURIEs: {', '.join(res['query_curies']) or '(none)'}",
        f"- Repo: `{res['repo']}`",
        f"- Commit: `{res['commit']}`",
        f"- Run on: {res['generated']}",
        (f"- Files: {res['files_parsed']} parsed, "
         f"{res['files_skipped_by_prefilter']} skipped by prefilter, "
         f"of {res['files_considered']} considered"),
        "",
    ]
    if not hits:
        out += ["No binding or named holder matched the query.", ""]
        return "\n".join(out)

    out += ["## Resolved terms", "", "| CURIE | Label(s) |", "|---|---|"]
    for curie, labels in res["resolved"].items():
        out.append(f"| `{curie}` | {'; '.join(labels) or '—'} |")
    out.append("")

    # Only direct term matches count here; a holder-name match is about the holder.
    direct = [h for h in hits if h["matched_by"] in ("curie", "label", "preferred_term")]
    roles_by_entry = defaultdict(set)
    for h in direct:
        roles_by_entry[h["entry"]].add(h["role"])
    all_roles = {r for rs in roles_by_entry.values() for r in rs}

    out += ["## Does it function as both a drug and an exposure?", ""]
    out.append(f"**Across the KB:** roles seen — {', '.join(sorted(all_roles)) or 'none'}.")
    if {"therapy", "exposure"} <= all_roles:
        th = sorted(e for e, r in roles_by_entry.items() if "therapy" in r)
        ex = sorted(e for e, r in roles_by_entry.items() if "exposure" in r)
        out += [
            "",
            ("**Yes — both roles exist**, under different CURIEs. Therapy in "
             f"{len(th)} entries, exposure in {len(ex)}."),
            "",
            f"- therapy: {', '.join(th)}",
            f"- exposure: {', '.join(ex)}",
        ]
    else:
        out += ["", "**No** — only one of the therapy and exposure roles is populated."]

    both = sorted(e for e, r in roles_by_entry.items() if {"therapy", "exposure"} <= r)
    out += ["", "**In the same entry:** "]
    if both:
        out[-1] += ("yes, below. The two claims are independent and are not reconciled "
                    "against each other.")
        out += [""] + [f"- **{e}**" for e in both]
    else:
        out[-1] += ("no entry carries both roles, so no single disease file states the "
                    "drug and the exposure to it together.")
    out.append("")

    out += ["## Mechanisms reached", "",
            ("The pathograph nodes the term acts on, via `target_mechanisms` (therapy) "
             "or `influences_mechanisms` (exposure)."), "",
            "| Disease | Role | Holder | Mechanism node | Effect | Link | Ev | FK |",
            "|---|---|---|---|---|---|---|---|"]
    # One holder can match on several term paths, which would repeat its mechanism
    # links once per match. The holder owns the links, so collapse on it.
    seen = set()
    for h in sorted(hits, key=lambda x: (x["entry"], x["role"], x["holder"])):
        for m in h["mechanisms"]:
            key = (h["file"], h["role"], h["holder"], m["target"])
            if key in seen:
                continue
            seen.add(key)
            fk = "ok" if m["resolves"] else "**dangling**"
            out.append(
                f"| {h['entry']} | {h['role']} | {h['holder']} | {m['target']} | "
                f"{m['effect'] or '—'} | {m['causal_link_type'] or '—'} | "
                f"{m['evidence_items']} | {fk} |"
            )
    if not seen:
        out.append("| — | — | — | *no mechanism link on any matching holder* | — | — | — | — |")
    out.append("")

    out += ["## Every binding", "",
            ("`agent slot` marks the slot that carries the substance itself, as opposed "
             "to the treatment action or a qualifier."), "",
            "| Disease | Role | Holder | CURIE | Schema path | Matched by | Agent slot |",
            "|---|---|---|---|---|---|---|"]
    for h in sorted(hits, key=lambda x: (x["entry"], x["role"], x["term_path"])):
        out.append(
            f"| {h['entry']} | {h['role']} | {h['holder']} | `{h['curie'] or '—'}` | "
            f"`{h['term_path']}` | {h['matched_by']} | {'yes' if h['is_agent_slot'] else ''} |"
        )
    out.append("")

    if res["proposed"]:
        out += ["## Proposed only (discussions, not asserted)", ""]
        for p in res["proposed"]:
            out.append(f"- {p['entry']} — `{p['curie'] or p['label']}` at `{p['term_path']}`")
        out.append("")

    if res["parse_errors"]:
        out += ["## Parse errors", ""]
        out += [f"- `{e['file']}`: {e['error']}" for e in res["parse_errors"]]
        out.append("")
    return "\n".join(out)


def render_tsv(res: dict) -> str:
    cols = ["entry", "disease_curie", "role", "holder", "curie", "label", "term_path",
            "is_agent_slot", "matched_by", "mech_target", "mech_effect",
            "mech_causal_link_type", "mech_evidence_items", "mech_resolves", "file"]
    rows, seen = ["\t".join(cols)], set()
    for h in res["hits"]:
        base = [h["entry"], h["disease_curie"], h["role"], h["holder"], h["curie"],
                h["label"], h["term_path"], str(h["is_agent_slot"]), h["matched_by"]]
        if h["mechanisms"]:
            for m in h["mechanisms"]:
                row = base + [m["target"], m["effect"], m["causal_link_type"],
                              str(m["evidence_items"]), str(m["resolves"]), h["file"]]
                if tuple(row) in seen:
                    continue
                seen.add(tuple(row))
                rows.append("\t".join(row))
        else:
            row = base + ["", "", "", "", "", h["file"]]
            if tuple(row) not in seen:
                seen.add(tuple(row))
                rows.append("\t".join(row))
    return "\n".join(rows) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--term", action="append", dest="terms", default=[],
                    help="free-text name, matched case-insensitively against term "
                         "labels and holder names; repeatable")
    ap.add_argument("--curie", action="append", dest="curies", default=[],
                    help="exact CURIE, e.g. CHEBI:5062 or ECTO:9001833; repeatable")
    ap.add_argument("--repo", default=REPO_ROOT, type=Path)
    ap.add_argument("--glob", action="append", dest="globs",
                    help="KB glob, repeatable (default: disorders and modules)")
    ap.add_argument("--format", choices=("md", "tsv", "json"), default="md")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    if not args.terms and not args.curies:
        print("error: give at least one --term or --curie", file=sys.stderr)
        return 1
    for c in args.curies:
        if not CURIE_RE.match(c):
            print(f"error: not a CURIE: {c}", file=sys.stderr)
            return 1
    if not args.repo.is_dir():
        print(f"error: no such repo: {args.repo}", file=sys.stderr)
        return 1

    globs = args.globs or ["kb/disorders/*.yaml", "kb/modules/*.yaml"]
    res = collect(args.repo, globs, Query(args.terms, args.curies))

    text = {"md": render_md, "tsv": render_tsv,
            "json": lambda r: json.dumps(r, indent=2)}[args.format](res)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
