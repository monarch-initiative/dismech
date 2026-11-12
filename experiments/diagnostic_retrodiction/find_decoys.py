"""Run the one fixed decoy query against PubMed and map each hit to kb/disorders/.

A decoy is a diagnostic biomarker proposed for a disease and later reported as
failing replication. The query below is fixed: it is recorded verbatim in
decoy_query.txt with the run date and hit count, and is not tuned per disease.

Phrases use PubMed's proximity form ("a b"[tiab:~N]); the plain quoted form
("failed to replicate"[tiab]) returns 0 records through E-utilities.

Output (``--out``, default decoy_candidates.tsv): one row per PubMed record with
its MeSH descriptors, the MONDO terms those descriptors map to (oio:hasDbXref
MESH:<UI> in the local mondo.db), and the kb/disorders files whose
``disease_term`` is one of those MONDO terms. decoys.tsv is then written by
hand from this table, reading each abstract; only rows with a kb file qualify.

NCBI_API_KEY is read from the environment, sent only in the POST body, never
printed. Responses are cached under tmp/decoy_cache/.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import os
import sqlite3
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

QUERY = (
    '(biomarker[tiab] OR biomarkers[tiab] OR "Biomarkers"[MeSH Terms]) AND diagnos*[tiab] AND '
    '("failed replicate"[tiab:~2] OR "failure replicate"[tiab:~2] OR "not replicated"[tiab:~0] OR '
    '"could not replicated"[tiab:~1] OR "did not replicate"[tiab:~0] OR "not replicate"[tiab:~0]) '
    'AND hasabstract'
)


def post(endpoint: str, params: dict, key: str, cache: Path) -> bytes:
    h = hashlib.sha256(repr(sorted(params.items())).encode()).hexdigest()[:24]
    path = cache / f"{endpoint.split('.')[0]}_{h}"
    if path.exists():
        return path.read_bytes()
    body = urllib.parse.urlencode({**params, "tool": "dismech-retrodiction", "api_key": key}).encode()
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"{EUTILS}/{endpoint}", data=body),
                                        timeout=60) as r:
                data = r.read()
            time.sleep(0.11)
            path.write_bytes(data)
            return data
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == 3:
                sys.exit(f"{endpoint} failed ({type(e).__name__})")  # type only: text can hold the key
            time.sleep(2 * (attempt + 1))
    raise AssertionError


def kb_index() -> dict[str, list[str]]:
    """MONDO id -> kb/disorders file stems, from each entry's disease_term."""
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    idx: dict[str, list[str]] = {}
    for p in sorted((REPO / "kb" / "disorders").glob("*.yaml")):
        try:
            doc = yaml.load(p.read_text(encoding="utf-8"), Loader=loader) or {}
        except yaml.YAMLError:
            continue
        term = ((doc.get("disease_term") or {}).get("term") or {}).get("id")
        if term:
            idx.setdefault(term, []).append(p.stem)
    return idx


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=Path, default=HERE / "decoy_candidates.tsv")
    ap.add_argument("--query-out", type=Path, default=HERE / "decoy_query.txt")
    ap.add_argument("--cache", type=Path, default=REPO / "tmp" / "decoy_cache")
    a = ap.parse_args()
    key = os.environ.get("NCBI_API_KEY", "").strip()
    if not key:
        sys.exit("NCBI_API_KEY is not set")
    a.cache.mkdir(parents=True, exist_ok=True)

    sys.path.insert(0, str(REPO / "src"))
    from dismech.oak_db import adapter_build_name, local_build_path
    db = local_build_path(adapter_build_name("sqlite:obo:mondo"))
    if not db.is_file():
        sys.exit("local mondo.db required: just fetch-ontology-dbs mondo")
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    mondo_build = dt.date.fromtimestamp(db.stat().st_mtime).isoformat()

    import json
    res = json.loads(post("esearch.fcgi", {"db": "pubmed", "term": QUERY, "retmax": "1000",
                                          "retmode": "json"}, key, a.cache))["esearchresult"]
    pmids = res["idlist"]
    if int(res["count"]) != len(pmids):
        sys.exit("retmax too small")
    root = ET.fromstring(post("efetch.fcgi", {"db": "pubmed", "id": ",".join(pmids),
                                               "retmode": "xml"}, key, a.cache))
    idx = kb_index()

    rows = []
    for art in root.iter("PubmedArticle"):
        pmid = art.findtext(".//MedlineCitation/PMID")
        title = "".join(art.find(".//ArticleTitle").itertext()).strip()
        year = art.findtext(".//JournalIssue/PubDate/Year") or \
            (art.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]
        mesh = [(d.get("UI"), d.text) for d in art.iter("DescriptorName")]
        mondo = sorted({s for ui, _ in mesh for (s,) in con.execute(
            "select subject from statements where predicate='oio:hasDbXref' and value=? "
            "and subject like 'MONDO:%'", (f"MESH:{ui}",))})
        kb = sorted({f for m in mondo for f in idx.get(m, [])})
        rows.append({"pmid": pmid, "year": year, "title": title,
                     "mesh": "; ".join(f"{ui} {t}" for ui, t in mesh),
                     "mondo_from_mesh": "; ".join(mondo), "kb_files": "; ".join(kb)})
    rows.sort(key=lambda r: int(r["pmid"]))
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    a.query_out.write_text(
        f"query: {QUERY}\ndatabase: pubmed (E-utilities esearch, no date limits)\n"
        f"run_date: {dt.date.today().isoformat()}\nhits: {len(pmids)}\nmondo_build: {mondo_build}\n",
        encoding="utf-8")
    print(f"{len(rows)} records, {sum(bool(r['kb_files']) for r in rows)} with a kb/disorders match",
          file=sys.stderr)


if __name__ == "__main__":
    main()
