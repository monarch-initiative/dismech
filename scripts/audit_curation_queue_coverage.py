#!/usr/bin/env python3
"""Audit the open `Curate <label> (MONDO:...)` issue queue for already-covered targets.

The `claim-disease` duplicate preflight is lexical: it matches on MONDO ID, on the
entry label, and on synonyms. It therefore cannot see a concept that is already
curated *under a different MONDO term* — in practice, under the target's parent.
That is how issue #10069 (pituitary gland adenoma, MONDO:0006373) was filed
against a concept `Pituitary_Tumor.yaml` had already covered for ten days under
the parent term MONDO:0017611.

This script closes that gap by walking the MONDO subClassOf closure. For every
open curation issue naming a MONDO term it reports:

  DUPLICATE_ISSUE    two or more open issues name the same MONDO term
  ALREADY_CURATED    the term is already a curated disease_term / subtype / exact
                     or narrow mapping
  COVERED_BY_PARENT  an ancestor of the term is curated — a candidate duplicate,
                     ranked by how specific that ancestor is

COVERED_BY_PARENT is a *signal for human triage*, not a verdict. Every disease has
`MONDO:0000001 disease` as an ancestor; what matters is whether the curated
ancestor is tight enough that the child adds nothing. The report ranks hits by the
ancestor's descendant count, so genuinely near-duplicates (a parent with a handful
of children) sort above coincidental ones (a parent with thousands).

Usage:
    GH_TOKEN=... uv run python scripts/audit_curation_queue_coverage.py
    ... --max-descendants 200      # tighten the COVERED_BY_PARENT signal
    ... --json report.json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sqlite3
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

REPO = "monarch-initiative/dismech"
MONDO_DB = os.environ.get("MONDO_DB_PATH", str(Path.home() / ".data/oaklib/mondo.db"))
TITLE_RE = re.compile(r"\(?(MONDO:\d{7})\)?")
CURATE_RE = re.compile(r"^\s*curate\b", re.I)


def load_stub_queue() -> list[dict]:
    """The local `stubs/` queue — the candidate pool `claim-disease` draws from.

    Each stub carries `mondo_id`, `label` and `status`; only OPEN stubs are still
    claimable. This is the primary audit target because it is the queue itself,
    rather than the issues already filed off it.
    """
    out = []
    for path in sorted(glob.glob("stubs/*.yaml")):
        try:
            doc = yaml.safe_load(open(path))
        except Exception:
            continue
        if not isinstance(doc, dict) or doc.get("status") != "OPEN":
            continue
        mondo_id = doc.get("mondo_id")
        if isinstance(mondo_id, str) and mondo_id.startswith("MONDO:"):
            out.append({
                "number": Path(path).name,
                "title": f"{doc.get('label')} [{doc.get('entry_type')}]",
                "assignees": [],
                "mondo_id": mondo_id,
            })
    return out


def fetch_open_curation_issues(token: str) -> list[dict]:
    """Page the REST API for open issues labelled `curation` (excluding PRs).

    Note: direct api.github.com access is blocked in some sandboxed environments
    (403 at the egress proxy). Use --issues-json there, supplying a list of
    {number, title, assignees} objects collected through whatever GitHub client
    is available.
    """
    out, page = [], 1
    while True:
        url = (f"https://api.github.com/repos/{REPO}/issues"
               f"?state=open&labels=curation&per_page=100&page={page}")
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "dismech-queue-audit",
        })
        with urllib.request.urlopen(req) as resp:
            batch = json.load(resp)
        if not batch:
            break
        for it in batch:
            if "pull_request" in it:
                continue
            out.append({
                "number": it["number"],
                "title": it["title"],
                "assignees": [a["login"] for a in it.get("assignees") or []],
            })
        page += 1
    return out


def curated_mondo_ids() -> dict[str, str]:
    """MONDO IDs that count as curated, mapped to the entry that curates them.

    Matches the coverage rule in CLAUDE.md: primary `disease_term`, `has_subtypes`
    terms, and `mappings.mondo_mappings` whose predicate is exactMatch or
    narrowMatch. Other mapping predicates are cross-references and do not retire a
    concept from the queue.
    """
    covered: dict[str, str] = {}
    for path in sorted(glob.glob("kb/disorders/*.yaml")) + sorted(glob.glob("kb/groupings/*.yaml")):
        try:
            doc = yaml.safe_load(open(path))
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        stem = Path(path).stem

        def add(term):
            if isinstance(term, dict):
                tid = term.get("id")
                if isinstance(tid, str) and tid.startswith("MONDO:"):
                    covered.setdefault(tid, stem)

        dterm = doc.get("disease_term")
        if isinstance(dterm, dict):
            add(dterm.get("term") or dterm)
        for sub in doc.get("has_subtypes") or []:
            if isinstance(sub, dict):
                t = sub.get("subtype_term") or sub.get("disease_term") or sub.get("term")
                if isinstance(t, dict):
                    add(t.get("term") or t)
        for mapping in ((doc.get("mappings") or {}).get("mondo_mappings") or []):
            if isinstance(mapping, dict) and mapping.get("mapping_predicate") in (
                    "skos:exactMatch", "skos:narrowMatch"):
                add(mapping.get("term") or mapping)
    return covered


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-descendants", type=int, default=500,
                    help="only report a curated ancestor as COVERED_BY_PARENT when it "
                         "has at most this many MONDO descendants (default 500); "
                         "filters out coincidental hits on very general parents")
    ap.add_argument("--json", help="write the full report to this path as JSON")
    ap.add_argument("--source", choices=["stubs", "issues"], default="stubs",
                    help="what to audit: the local stubs/ queue (default) or open "
                         "GitHub curation issues")
    ap.add_argument("--issues-json", help="with --source issues, read the issue list "
                                          "from this JSON file instead of the API "
                                          "(needed where egress to api.github.com is blocked)")
    args = ap.parse_args()

    if not Path(MONDO_DB).exists():
        print(f"MONDO sqlite not found at {MONDO_DB}; run `just gen-priority-dashboard` "
              f"once to download it, or set MONDO_DB_PATH", file=sys.stderr)
        return 2

    if args.source == "stubs":
        items = load_stub_queue()
        label = "open stubs"
    elif args.issues_json:
        items = json.loads(Path(args.issues_json).read_text())
        label = "open curation issues (from file)"
    else:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not token:
            print("GH_TOKEN / GITHUB_TOKEN not set", file=sys.stderr)
            return 2
        items = fetch_open_curation_issues(token)
        label = "open curation issues"

    curated = curated_mondo_ids()
    print(f"{label}: {len(items)}")
    print(f"curated MONDO ids in kb/: {len(curated)}")

    targets: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        curie = item.get("mondo_id")
        if not curie:
            if not CURATE_RE.match(item["title"]):
                continue
            found = TITLE_RE.search(item["title"])
            curie = found.group(1) if found else None
        if curie:
            targets[curie].append(item)
    print(f"items naming a MONDO term: {sum(len(v) for v in targets.values())} "
          f"across {len(targets)} distinct terms")

    conn = sqlite3.connect(MONDO_DB)

    def ancestors(curie: str) -> list[str]:
        rows = conn.execute(
            "select object from entailed_edge where subject=? and predicate='rdfs:subClassOf'",
            (curie,)).fetchall()
        return [r[0] for r in rows if r[0].startswith("MONDO:") and r[0] != curie]

    # semsql indexes entailed_edge on (subject, ...) but not on object, so a
    # per-ancestor `where object=?` count full-scans ~5M rows each time. One
    # grouped pass builds the whole map instead.
    desc_count: dict[str, int] = dict(conn.execute(
        "select object, count(*) from entailed_edge "
        "where predicate='rdfs:subClassOf' group by object").fetchall())

    def descendants(curie: str) -> int:
        return desc_count.get(curie, 0)

    dupes, already, by_parent = [], [], []
    for curie, issue_list in sorted(targets.items()):
        if len(issue_list) > 1:
            dupes.append({"mondo_id": curie, "issues": issue_list})
        if curie in curated:
            already.append({"mondo_id": curie, "curated_as": curated[curie],
                            "issues": issue_list})
            continue
        hits = [{"ancestor": a, "curated_as": curated[a], "descendants": descendants(a)}
                for a in ancestors(curie) if a in curated]
        hits = [h for h in hits if h["descendants"] <= args.max_descendants]
        if hits:
            hits.sort(key=lambda h: h["descendants"])
            by_parent.append({"mondo_id": curie, "issues": issue_list, "hits": hits})

    by_parent.sort(key=lambda r: r["hits"][0]["descendants"])

    def title_of(entry):
        i = entry["issues"][0]
        who = ",".join(i["assignees"]) or "unassigned"
        return f"#{i['number']} {i['title']}  [{who}]"

    print(f"\n=== DUPLICATE — same MONDO term named by >1 open item ({len(dupes)})")
    for d in dupes:
        print(f"  {d['mondo_id']}")
        for i in d["issues"]:
            print(f"      #{i['number']}  {i['title']}  [{','.join(i['assignees']) or 'unassigned'}]")

    print(f"\n=== ALREADY_CURATED — term already covered exactly ({len(already)})")
    for a in already:
        print(f"  {a['mondo_id']} -> {a['curated_as']}")
        for i in a["issues"]:
            print(f"      #{i['number']}  {i['title']}  [{','.join(i['assignees']) or 'unassigned'}]")

    print(f"\n=== COVERED_BY_PARENT — a curated ancestor may already cover this "
          f"({len(by_parent)}, ancestor <= {args.max_descendants} descendants)")
    for b in by_parent:
        top = b["hits"][0]
        print(f"  {b['mondo_id']}  {title_of(b)}")
        print(f"      nearest curated ancestor: {top['ancestor']} -> {top['curated_as']} "
              f"({top['descendants']} descendants)")

    if args.json:
        Path(args.json).write_text(json.dumps(
            {"duplicate_issue": dupes, "already_curated": already,
             "covered_by_parent": by_parent}, indent=2))
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
