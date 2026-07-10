#!/usr/bin/env python3
"""Collect recent clinical Practice Guideline citations for dismech disorders.

Two subcommands:

  search  For every kb/disorders/*.yaml entry (or a --slugs subset), query
          PubMed E-utilities for citations of Publication Type
          "Practice Guideline" published in the last N years. Emits one JSON
          record per disorder (slug, search_name, count, pmids) to a JSONL file.

  fetch   Given a JSONL produced by `search` (or an explicit --slugs list read
          from it), fetch citation metadata (title, journal, pubdate, year, DOI,
          publication types) for every PMID and emit a tab-delimited citation
          table: one row per (disorder, PMID).

Only the Python standard library plus PyYAML is required. Respects NCBI's
3 requests/second limit; set NCBI_API_KEY to raise the limit to 10/s.

Examples:
  python collect_guidelines.py search --out hits.jsonl
  python collect_guidelines.py search --slugs Asthma,Marfan_Syndrome --out hits.jsonl
  python collect_guidelines.py fetch --hits hits.jsonl --out citations.tsv --min-count 1
"""
import argparse
import glob
import json
import os
import sys
import time
import urllib.parse
import urllib.request

import yaml

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "dismech"
EMAIL = "jhc@lbl.gov"
PUBTYPE = '"Practice Guideline"[Publication Type]'
API_KEY = os.environ.get("NCBI_API_KEY")
SLEEP = 0.11 if API_KEY else 0.34  # ~10/s with key, ~3/s without


def search_name(path):
    """Clean disease name for the query: prefer the top-level MONDO mapping
    label, else the `name` field with underscores rendered as spaces."""
    d = yaml.safe_load(open(path))
    slug = os.path.basename(path)[:-5]
    mm = (d.get("mappings") or {}).get("mondo_mappings")
    if mm:
        lab = mm[0].get("term", {}).get("label")
        if lab:
            return slug, lab
    return slug, (d.get("name") or slug).replace("_", " ")


def eget(endpoint, params):
    params = {**params, "tool": TOOL, "email": EMAIL, "retmode": "json"}
    if API_KEY:
        params["api_key"] = API_KEY
    url = f"{EUTILS}/{endpoint}?{urllib.parse.urlencode(params)}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)
        except Exception:
            if attempt == 3:
                raise
            time.sleep(1.5 * (attempt + 1))


def esearch(name, reldate_days, retmax):
    # Field-tag the disease phrase so PubMed cannot shatter an unmatched name
    # into individual all-fields words (which explodes obscure disorders into
    # dozens of irrelevant guidelines). If the name matches neither a MeSH term
    # nor a title/abstract phrase, the query correctly returns zero.
    term = (f'("{name}"[MeSH Terms] OR "{name}"[Title/Abstract]) '
            f'AND {PUBTYPE}')
    d = eget("esearch.fcgi", {
        "db": "pubmed", "term": term,
        "reldate": reldate_days, "datetype": "pdat", "retmax": retmax,
    })
    res = (d or {}).get("esearchresult", {})
    return int(res.get("count", 0)), res.get("idlist", [])


def esummary(pmids):
    out = {}
    for i in range(0, len(pmids), 200):
        chunk = pmids[i:i + 200]
        d = eget("esummary.fcgi", {"db": "pubmed", "id": ",".join(chunk)})
        out.update((d or {}).get("result", {}))
        time.sleep(SLEEP)
    return out


def cmd_search(args):
    if args.slugs:
        files = [f"kb/disorders/{s.strip()}.yaml" for s in args.slugs.split(",")]
    else:
        files = sorted(glob.glob("kb/disorders/*.yaml"))
    total = len(files)
    with open(args.out, "w") as out:
        for i, f in enumerate(files, 1):
            if not os.path.exists(f):
                sys.stderr.write(f"[{i}/{total}] MISSING {f}\n")
                continue
            try:
                slug, name = search_name(f)
                count, ids = esearch(name, args.reldate, args.retmax)
                time.sleep(SLEEP)
            except Exception as e:
                sys.stderr.write(f"[{i}/{total}] ERR {f}: {e}\n")
                continue
            out.write(json.dumps({"slug": slug, "search_name": name,
                                  "count": count, "pmids": ids}) + "\n")
            out.flush()
            if count:
                sys.stderr.write(f"[{i}/{total}] {slug}: {count}\n")
    sys.stderr.write(f"done: {total} disorders searched -> {args.out}\n")


def doi_of(rec):
    return next((x["value"] for x in rec.get("articleids", [])
                 if x["idtype"] == "doi"), "")


def year_of(rec):
    pd = rec.get("pubdate", "")
    return pd.split(" ")[0][:4] if pd else ""


def cmd_fetch(args):
    hits = [json.loads(line) for line in open(args.hits) if line.strip()]
    hits = [h for h in hits if h["count"] >= args.min_count]
    hits.sort(key=lambda h: (-h["count"], h["slug"]))
    if args.top:
        hits = hits[:args.top]
    cols = ["disorder_slug", "search_name", "pmid", "title", "journal",
            "pub_year", "pubdate", "doi", "publication_types",
            "guideline_count_for_disorder"]
    with open(args.out, "w") as out:
        out.write("\t".join(cols) + "\n")
        for h in hits:
            summ = esummary(h["pmids"])
            for pmid in h["pmids"]:
                r = summ.get(pmid)
                if not r or "title" not in r:
                    continue
                row = [
                    h["slug"], h["search_name"], pmid,
                    r["title"].replace("\t", " ").rstrip("."),
                    r.get("source", ""), year_of(r), r.get("pubdate", ""),
                    doi_of(r), "; ".join(r.get("pubtype", [])),
                    str(h["count"]),
                ]
                out.write("\t".join(row) + "\n")
            sys.stderr.write(f"{h['slug']}: fetched {len(h['pmids'])} citation(s)\n")
    sys.stderr.write(f"done -> {args.out} ({len(hits)} disorders)\n")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="search PubMed guidelines per disorder")
    s.add_argument("--out", required=True)
    s.add_argument("--slugs", help="comma-separated subset (default: all)")
    s.add_argument("--reldate", type=int, default=3650, help="lookback in days")
    s.add_argument("--retmax", type=int, default=30, help="max PMIDs/disorder")
    s.set_defaults(func=cmd_search)

    g = sub.add_parser("fetch", help="fetch citation metadata -> TSV")
    g.add_argument("--hits", required=True, help="JSONL from `search`")
    g.add_argument("--out", required=True)
    g.add_argument("--min-count", type=int, default=1)
    g.add_argument("--top", type=int, default=0, help="keep top-N disorders by count")
    g.set_defaults(func=cmd_fetch)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
