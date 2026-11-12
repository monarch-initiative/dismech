"""Advisory recount for cases check_pretest_era.py ruled INSUFFICIENT_PRE_CUTOFF_LITERATURE.

check_pretest_era.py searches each case's MONDO label and exact synonyms. Many
of those are catalogue forms that abstracts never contain (inverted OMIM-style
labels such as "diabetes insipidus, nephrogenic, X-linked"), genetic-subtype
labels, or names coined after the test. This script recounts each failing
case with the disease's plain literature name, hand-written in PLAIN_TERMS and
searched as [tiab]. It uses the same hasabstract filter, the same cutoff, and
the same packet minimum. It decides nothing: dating.tsv still drops every case
literature_check.tsv fails. It exists so a person can tell a real shortage of
literature from a label that does not occur in abstracts.

Writes literature_recount.tsv. Needs NCBI_API_KEY (never printed).

Usage:
    uv run python experiments/diagnostic_retrodiction/literature_recount.py
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PLAIN_TERMS = {
    "C004": '"NMDA receptor"[tiab] AND encephalitis[tiab]',
    "C008": '(Canavan[tiab] OR "spongy degeneration"[tiab])',
    "C013": '("Upshaw-Schulman"[tiab] OR "chronic relapsing thrombotic thrombocytopenic purpura"[tiab] OR '
            '"familial thrombotic thrombocytopenic purpura"[tiab] OR "congenital thrombotic thrombocytopenic purpura"[tiab])',
    "C015": '"dyskeratosis congenita"[tiab]',
    "C016": '"dyskeratosis congenita"[tiab]',
    "C019": '("CD3 deficiency"[tiab] OR "CD3epsilon"[tiab] OR "CD3 epsilon"[tiab]) AND immunodeficiency[tiab]',
    "C020": '("CD3 deficiency"[tiab] OR "CD3delta"[tiab] OR "CD3 delta"[tiab]) AND immunodeficiency[tiab]',
    "C022": '("acid maltase deficiency"[tiab] OR "glycogen storage disease type II"[tiab] OR "glycogenosis type II"[tiab] OR Pompe[tiab])',
    "C028": '"myelin oligodendrocyte glycoprotein"[tiab] AND antibod*[tiab] AND '
            '(demyelinat*[tiab] OR encephalomyelitis[tiab] OR "optic neuritis"[tiab])',
    "C031": '(MNGIE[tiab] OR "mitochondrial neurogastrointestinal"[tiab] OR "oculogastrointestinal"[tiab])',
    "C032": '(MNGIE[tiab] OR "mitochondrial neurogastrointestinal"[tiab] OR "oculogastrointestinal"[tiab])',
    "C034": 'narcolepsy[tiab]',
    "C037": '("neuromyelitis optica"[tiab] OR Devic[tiab])',
    "C044": '("bile acid malabsorption"[tiab] OR "bile salt malabsorption"[tiab])',
    "C045": '"pyridoxine-dependent"[tiab]',
    "C046": 'Revesz[tiab]',
    "C057": '"nephrogenic diabetes insipidus"[tiab]',
}


def count(term: str, maxdate: str, key: str) -> int:
    body = urllib.parse.urlencode({"db": "pubmed", "term": f"({term}) AND hasabstract", "datetype": "pdat",
                                   "mindate": "1800/01/01", "maxdate": maxdate, "rettype": "count",
                                   "retmode": "json", "tool": "dismech-retrodiction", "api_key": key}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", data=body), timeout=60) as r:
            n = int(json.load(r)["esearchresult"]["count"])
    except Exception as e:  # type only: the request carries the key
        sys.exit(f"esearch failed ({type(e).__name__})")
    time.sleep(0.12)
    return n


def main() -> None:
    key = os.environ.get("NCBI_API_KEY", "").strip()
    if not key:
        sys.exit("NCBI_API_KEY is not set")
    minimum = yaml.safe_load((HERE / "RUN_CONFIG").read_text())["packet_minimum"]
    with open(HERE / "literature_check.tsv", newline="", encoding="utf-8") as f:
        lit = [r for r in csv.DictReader(f, delimiter="\t")
               if r["lit_ruling"] == "INSUFFICIENT_PRE_CUTOFF_LITERATURE"]
    missing = sorted({r["case_id"] for r in lit} ^ set(PLAIN_TERMS))
    if missing:
        sys.exit(f"PLAIN_TERMS must cover exactly the failing cases; differs on {missing}")
    out = []
    for r in lit:
        term = PLAIN_TERMS[r["case_id"]]
        n = count(term, r["cutoff_date"].replace("-", "/"), key)
        out.append({"case_id": r["case_id"], "disease": r["disease"], "test": r["test"],
                    "cutoff_date": r["cutoff_date"], "mondo_count": r["lit_count"], "plain_query": term,
                    "plain_count": str(n), "packet_minimum": str(minimum),
                    "plain_ruling": "INSUFFICIENT" if n < minimum else "PASS"})
    with open(HERE / "literature_recount.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    for o in out:
        print(f"{o['plain_ruling']:12s} {o['case_id']} {o['disease'][:45]:45s} MONDO {o['mondo_count']:>4s}  plain {o['plain_count']:>6s}")


if __name__ == "__main__":
    main()
