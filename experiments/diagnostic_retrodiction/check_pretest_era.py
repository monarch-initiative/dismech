"""Test whether a disease had a literature before its diagnostic test existed.

Rule 2 of eligibility_rules.md (version 2): a disease whose own name appears in
fewer than 100 PubMed abstracts dated before 31 December of the year before
the test's discovery has no pre-test era to retrodict, and the row is
EXCLUDE / DISEASE_DEFINED_BY_TEST.

Input TSV columns (required): disease, test, discovery_year. Other columns are
passed through unchanged.

For each row the query is

    "<disease>"[tiab] AND hasabstract

with publication date (``pdat``) from 1800/01/01 to 31 December of
``discovery_year - 1``. "<disease>" is the disease column exactly as given,
searched as a phrase in titles and abstracts; this script does not add
synonyms, so a name that is a knowledge-base label rather than a literature
term will return a low count. Added columns:

  pretest_query    the query sent
  pretest_maxdate  the upper date bound, YYYY/MM/DD
  pretest_count    PubMed's hit count
  pretest_ruling   DISEASE_DEFINED_BY_TEST if the count is below --threshold
                   (default 100), PASS otherwise, NA if the search failed or
                   the year was unusable

Responses are cached under tmp/pretest_cache/ (gitignored). NCBI_API_KEY is
required; it is sent only as a request parameter and is never printed, cached,
or put in an error message.

Usage:
    uv run python experiments/diagnostic_retrodiction/check_pretest_era.py \
        input.tsv --out output.tsv [--threshold 100]
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
REQUIRED = ("disease", "test", "discovery_year")
ADDED = ("pretest_query", "pretest_maxdate", "pretest_count", "pretest_ruling")


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def count(term: str, maxdate: str, api_key: str, cache: Path, email: str | None) -> int | None:
    params = {"db": "pubmed", "term": term, "datetype": "pdat", "mindate": "1800/01/01",
              "maxdate": maxdate, "rettype": "count", "retmode": "json"}
    key = hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()[:20]
    path = cache / f"count_{key}.json"
    if path.exists():
        return json.loads(path.read_text())["count"]
    full = {**params, "tool": "dismech-retrodiction", "api_key": api_key}
    if email:
        full["email"] = email
    url = f"{ESEARCH}?{urllib.parse.urlencode(full)}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                n = int(json.load(r)["esearchresult"]["count"])
            time.sleep(0.11)
            path.write_text(json.dumps({"term": term, "maxdate": maxdate, "count": n}))
            return n
        except (urllib.error.URLError, TimeoutError, KeyError, ValueError) as e:
            if attempt == 3:
                # Type only: exception text can echo the URL, which carries the key.
                log(f"esearch failed ({type(e).__name__}) for: {term}")
                return None
            time.sleep(2 * (attempt + 1))
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("input", type=Path)
    ap.add_argument("--out", type=Path, help="output TSV (default: stdout)")
    ap.add_argument("--threshold", type=int, default=100)
    ap.add_argument("--cache", type=Path,
                    default=Path(__file__).resolve().parents[2] / "tmp" / "pretest_cache")
    ap.add_argument("--email", default=None, help="optional contact email sent to NCBI")
    a = ap.parse_args()

    api_key = os.environ.get("NCBI_API_KEY", "").strip()
    if not api_key:
        sys.exit("NCBI_API_KEY is not set; it is required for E-utilities requests.")
    a.cache.mkdir(parents=True, exist_ok=True)

    with open(a.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    missing = [c for c in REQUIRED if c not in fields]
    if missing:
        sys.exit(f"input is missing required column(s): {', '.join(missing)}")

    for row in rows:
        row.update({c: "NA" for c in ADDED})
        disease = " ".join((row["disease"] or "").split()).replace('"', "")
        year = (row["discovery_year"] or "").strip()
        if not disease or not (year.isdigit() and len(year) == 4):
            log(f"{row['disease']} / {row['test']}: unusable disease or discovery_year {year!r}")
            continue
        term = f'"{disease}"[tiab] AND hasabstract'
        maxdate = f"{int(year) - 1}/12/31"
        row["pretest_query"], row["pretest_maxdate"] = term, maxdate
        n = count(term, maxdate, api_key, a.cache, a.email)
        if n is None:
            continue
        row["pretest_count"] = str(n)
        row["pretest_ruling"] = "DISEASE_DEFINED_BY_TEST" if n < a.threshold else "PASS"

    dest = open(a.out, "w", newline="", encoding="utf-8") if a.out else sys.stdout
    w = csv.DictWriter(dest, fieldnames=fields + [c for c in ADDED if c not in fields],
                       delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    if a.out:
        dest.close()


if __name__ == "__main__":
    main()
