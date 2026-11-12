"""Check the dating of each disease/test pair against its claimed discovery paper.

Input TSV columns (all required): disease, test, discovery_pmid, quote, analyte.

For each row, using NCBI E-utilities only (no ``just fetch-reference``, no
``references_cache/``):

1. The PubMed record is fetched with efetch (XML). Responses are cached under
   ``tmp/dating_cache/`` (gitignored), so a rerun makes no repeat requests.
2. ``pubmed_date`` is the earlier of the journal issue date (``PubDate``) and
   the electronic publication date (``ArticleDate``), as YYYY-MM-DD. A missing
   month or day is filled with 01, and ``date_precision`` (DAY/MONTH/YEAR)
   records how much of the chosen date the record actually gave. When the two
   dates fall on the same filled day, the more precise one is kept.
3. ``quote_ok`` is TRUE when ``quote`` is a substring of the abstract text (the
   ``AbstractText`` elements only, not the title or affiliations), after
   collapsing runs of whitespace on both sides. Nothing else is normalized.
4. ``earlier_hits`` is the PubMed count for ``(<analyte>) AND (<disease>)``
   with publication date up to the day before ``pubmed_date``.
   ``earlier_pmids`` lists the 5 earliest of those hits, earliest first.
   esearch sorts by publication date newest-first only, so the earliest are
   read from the tail of the full ID list; that list is capped at 9,999 IDs,
   and above that the column says so instead of listing a wrong five. The order
   is PubMed's own sort date, not the earliest-of rule used for
   ``pubmed_date``: a paper with an early e-pub date can sort after one with an
   earlier issue month. Records sharing a sort date have no defined order.

The NCBI_API_KEY environment variable is required. The key is sent only as a
request parameter: it is never printed, written to the cache, or included in an
error message (exception text is not printed, because it can echo the URL).

A row that cannot be checked gets NA in the added columns, with the reason on
stderr. ``--strict`` exits 1, after writing the output, if any row has
quote_ok FALSE or NA.

Usage:
    uv run python experiments/diagnostic_retrodiction/check_dating.py \
        dating_input.tsv --out dating_checked.tsv [--strict]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
REQUIRED = ("disease", "test", "discovery_pmid", "quote", "analyte")
ADDED = ("pubmed_date", "date_precision", "quote_ok", "earlier_hits", "earlier_pmids")
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
ESEARCH_ID_CAP = 9999
N_EARLIEST = 5


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


class EUtils:
    def __init__(self, api_key: str, cache: Path, email: str | None):
        self.api_key, self.cache, self.email = api_key, cache, email
        self.cache.mkdir(parents=True, exist_ok=True)

    def _get(self, endpoint: str, params: dict) -> bytes | None:
        full = {**params, "tool": "dismech-retrodiction", "api_key": self.api_key}
        if self.email:
            full["email"] = self.email
        url = f"{EUTILS}/{endpoint}?{urllib.parse.urlencode(full)}"
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    body = r.read()
                time.sleep(0.11)  # under the 10 requests/s keyed limit
                return body
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt == 3:
                    code = getattr(e, "code", None)
                    log(f"{endpoint} failed ({type(e).__name__}{f' {code}' if code else ''})")
                    return None
                time.sleep(2 * (attempt + 1))
        return None

    def efetch(self, pmid: str) -> ET.Element | None:
        path = self.cache / f"efetch_{pmid}.xml"
        if path.exists():
            body = path.read_bytes()
        else:
            body = self._get("efetch.fcgi", {"db": "pubmed", "id": pmid, "retmode": "xml"})
            if body is None:
                return None
        try:
            art = ET.fromstring(body).find("PubmedArticle")
        except ET.ParseError:
            log(f"PMID:{pmid}: efetch returned unparseable XML")
            return None
        if art is None or art.findtext(".//MedlineCitation/PMID") != pmid:
            log(f"PMID:{pmid}: no PubMed record")
            return None  # not cached, so a transient miss is retried next run
        if not path.exists():
            path.write_bytes(body)
        return art

    def esearch_ids(self, term: str, maxdate: str) -> dict | None:
        params = {"db": "pubmed", "term": term, "datetype": "pdat", "mindate": "1800/01/01",
                  "maxdate": maxdate, "sort": "pub_date", "retmax": ESEARCH_ID_CAP,
                  "retmode": "json"}
        key = hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()[:20]
        path = self.cache / f"esearch_{key}.json"
        if path.exists():
            return json.loads(path.read_text())
        body = self._get("esearch.fcgi", params)
        if body is None:
            return None
        try:
            res = json.loads(body)["esearchresult"]
            out = {"term": term, "maxdate": maxdate, "count": int(res["count"]),
                   "idlist": res.get("idlist", [])}
        except (ValueError, KeyError):
            log(f"esearch returned an unexpected response for: {term}")
            return None
        path.write_text(json.dumps(out, indent=1))
        return out


def month_num(text: str | None) -> int | None:
    if not text:
        return None
    t = text.strip().lower()
    if t.isdigit() and 1 <= int(t) <= 12:
        return int(t)
    return MONTHS.get(t[:3])


def make_date(year: str | None, month: str | None, day: str | None) -> tuple[dt.date, str] | None:
    if not (year and year.strip().isdigit()):
        return None
    m = month_num(month)
    d = int(day) if m and day and day.strip().isdigit() else None
    precision = "DAY" if d else "MONTH" if m else "YEAR"
    try:
        return dt.date(int(year), m or 1, d or 1), precision
    except ValueError:
        return dt.date(int(year), m or 1, 1), "MONTH" if m else "YEAR"


def publication_date(art: ET.Element) -> tuple[dt.date, str] | None:
    cands = []
    pd = art.find(".//Article/Journal/JournalIssue/PubDate")
    if pd is not None:
        if pd.findtext("Year"):
            c = make_date(pd.findtext("Year"), pd.findtext("Month"), pd.findtext("Day"))
        else:  # MedlineDate, e.g. "1998 Dec-1999 Jan" or "2015 Spring"
            m = re.match(r"\s*(\d{4})(?:\s+([A-Za-z]{3}))?", pd.findtext("MedlineDate") or "")
            c = make_date(m.group(1), m.group(2), None) if m else None
        if c:
            cands.append(c)
    for ad in art.findall(".//Article/ArticleDate"):
        c = make_date(ad.findtext("Year"), ad.findtext("Month"), ad.findtext("Day"))
        if c:
            cands.append(c)
    if not cands:
        return None
    rank = {"DAY": 0, "MONTH": 1, "YEAR": 2}
    return min(cands, key=lambda c: (c[0], rank[c[1]]))


def abstract_text(art: ET.Element) -> str:
    return " ".join(" ".join(el.itertext()) for el in art.findall(".//Abstract/AbstractText"))


def norm(s: str) -> str:
    return " ".join(s.split())


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("input", type=Path)
    ap.add_argument("--out", type=Path, help="output TSV (default: stdout)")
    ap.add_argument("--cache", type=Path,
                    default=Path(__file__).resolve().parents[2] / "tmp" / "dating_cache")
    ap.add_argument("--email", default=None, help="optional contact email sent to NCBI")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any row has quote_ok FALSE or NA")
    a = ap.parse_args()

    api_key = os.environ.get("NCBI_API_KEY", "").strip()
    if not api_key:
        sys.exit("NCBI_API_KEY is not set; it is required for E-utilities requests.")
    eu = EUtils(api_key, a.cache, a.email)

    with open(a.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    missing = [c for c in REQUIRED if c not in fields]
    if missing:
        sys.exit(f"input is missing required column(s): {', '.join(missing)}")
    out_fields = fields + [c for c in ADDED if c not in fields]

    for row in rows:
        row.update({c: "NA" for c in ADDED})
        label = f"{row['disease']} / {row['test']}"
        m = re.fullmatch(r"\s*(?:PMID:\s*)?(\d+)\s*", row["discovery_pmid"] or "", re.I)
        if not m:
            log(f"{label}: unparseable PMID {row['discovery_pmid']!r}")
            continue
        pmid = m.group(1)
        art = eu.efetch(pmid)
        if art is None:
            continue
        pub = publication_date(art)
        if pub is None:
            log(f"PMID:{pmid}: record has no usable publication date")
        else:
            row["pubmed_date"], row["date_precision"] = pub[0].isoformat(), pub[1]

        abstract = norm(abstract_text(art))
        quote = norm(row["quote"] or "")
        if not abstract:
            log(f"PMID:{pmid}: record has no abstract; quote_ok left NA")
        elif quote:
            row["quote_ok"] = "TRUE" if quote in abstract else "FALSE"
        else:
            row["quote_ok"] = "FALSE"

        analyte, disease = (row["analyte"] or "").strip(), (row["disease"] or "").strip()
        if pub is None or not analyte or not disease:
            if pub is not None:
                log(f"{label}: empty analyte or disease; search skipped")
            continue
        maxdate = (pub[0] - dt.timedelta(days=1)).strftime("%Y/%m/%d")
        term = f"({analyte}) AND ({disease})"
        log(f"search to {maxdate}: {term}")
        res = eu.esearch_ids(term, maxdate)
        if res is None:
            continue
        row["earlier_hits"] = str(res["count"])
        if res["count"] > ESEARCH_ID_CAP:
            row["earlier_pmids"] = f"NA (over {ESEARCH_ID_CAP} hits; earliest not retrievable)"
        else:
            earliest = list(reversed(res["idlist"]))[:N_EARLIEST]
            row["earlier_pmids"] = ";".join(f"PMID:{p}" for p in earliest)

    dest = open(a.out, "w", newline="", encoding="utf-8") if a.out else sys.stdout
    w = csv.DictWriter(dest, fieldnames=out_fields, delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    if a.out:
        dest.close()

    bad = [r for r in rows if r["quote_ok"] != "TRUE"]
    if a.strict and bad:
        log(f"--strict: {len(bad)} row(s) with quote_ok FALSE or NA")
        sys.exit(1)


if __name__ == "__main__":
    main()
