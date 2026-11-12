"""Build a date-limited PubMed literature packet for a time-sliced curation run.

Only records with an abstract and a publication date on or before --maxdate are
kept. The packet is the ONLY literature the curating agent may cite.

Usage:
    uv run python experiments/diagnostic_retrodiction/build_packet.py \
        --term '"Glomerulonephritis, Membranous"[MeSH Terms]' \
        --maxdate 2008/12/31 \
        --out experiments/diagnostic_retrodiction/Membranous_Nephropathy-pre2009/packet \
        --email you@example.org
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def get(endpoint: str, params: dict) -> bytes:
    url = f"{EUTILS}/{endpoint}?{urllib.parse.urlencode(params)}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except Exception:
            if attempt == 4:
                raise
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("unreachable")


def parse_date(article: ET.Element) -> dt.date | None:
    """Earliest of the journal issue date and any electronic publication date."""
    dates = []
    pd = article.find(".//Article/Journal/JournalIssue/PubDate")
    if pd is not None:
        y = pd.findtext("Year")
        if y is None and pd.findtext("MedlineDate"):
            y = pd.findtext("MedlineDate")[:4]
        if y and y.isdigit():
            m = (pd.findtext("Month") or "1").strip().lower()[:3]
            m = int(m) if m.isdigit() else MONTHS.get(m, 1)
            d = pd.findtext("Day")
            dates.append(dt.date(int(y), m, int(d) if d and d.isdigit() else 1))
    for ad in article.findall(".//Article/ArticleDate"):
        try:
            dates.append(dt.date(int(ad.findtext("Year")), int(ad.findtext("Month")), int(ad.findtext("Day"))))
        except (TypeError, ValueError):
            pass
    return min(dates) if dates else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--term", required=True, help="PubMed query WITHOUT a date clause")
    ap.add_argument("--maxdate", required=True, help="YYYY/MM/DD, inclusive")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--email", required=True)
    ap.add_argument("--api-key", default=os.environ.get("NCBI_API_KEY"))
    a = ap.parse_args()

    cutoff = dt.date(*map(int, a.maxdate.split("/")))
    base = {"db": "pubmed", "email": a.email, "tool": "dismech-retrodiction"}
    if a.api_key:
        base["api_key"] = a.api_key
    term = f"({a.term}) AND hasabstract"
    s = json.loads(get("esearch.fcgi", {**base, "term": term, "datetype": "pdat",
                                         "mindate": "1800/01/01", "maxdate": a.maxdate,
                                         "usehistory": "y", "retmode": "json"}))["esearchresult"]
    count, webenv, qk = int(s["count"]), s["webenv"], s["querykey"]

    a.out.mkdir(parents=True, exist_ok=True)
    kept, dropped = [], []
    with open(a.out / "abstracts.jsonl", "w") as jl:
        for start in range(0, count, 200):
            xml = get("efetch.fcgi", {**base, "WebEnv": webenv, "query_key": qk,
                                      "retstart": start, "retmax": 200, "retmode": "xml"})
            for art in ET.fromstring(xml).findall("PubmedArticle"):
                pmid = art.findtext(".//MedlineCitation/PMID")
                date = parse_date(art)
                abstract = " ".join("".join(t.itertext()) for t in art.findall(".//Abstract/AbstractText")).strip()
                title = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
                if not abstract or date is None or date > cutoff:
                    dropped.append((pmid, str(date)))
                    continue
                kept.append((pmid, date.isoformat(), title))
                jl.write(json.dumps({"pmid": f"PMID:{pmid}", "date": date.isoformat(),
                                     "title": title, "abstract": abstract}) + "\n")
            time.sleep(0.12 if a.api_key else 0.4)

    with open(a.out / "packet.tsv", "w") as f:
        f.write("pmid\tdate\ttitle\n")
        for p, d, t in sorted(kept, key=lambda r: r[1]):
            f.write(f"PMID:{p}\t{d}\t{t.replace(chr(9), ' ')}\n")
    (a.out / "packet_meta.json").write_text(json.dumps({
        "query": term, "maxdate": a.maxdate, "esearch_count": count, "kept": len(kept),
        "dropped_no_abstract_or_late_date": len(dropped),
        "built_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}, indent=2))
    print(f"kept {len(kept)} / {count}; dropped {len(dropped)}")


if __name__ == "__main__":
    main()
