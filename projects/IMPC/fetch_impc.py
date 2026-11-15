"""Fetch IMPC significant phenotype calls and the IMPC gene table.

Shared with ai-gene-review `projects/IMPC/fetch_impc.py`, which uses the same
cache layout.

Raw payloads go to the git-ignored ``.cache/impc/`` directory; nothing here is
committed. Re-running overwrites the cache with the current IMPC data release.

    uv run python projects/IMPC/fetch_impc.py
"""

from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path

import requests

SOLR = "https://www.ebi.ac.uk/mi/impc/solr"
CACHE = Path(".cache/impc")

GP_FIELDS = [
    "marker_symbol",
    "marker_accession_id",
    "mp_term_id",
    "mp_term_name",
    "top_level_mp_term_name",
    "procedure_name",
    "procedure_stable_id",
    "parameter_name",
    "parameter_stable_id",
    "pipeline_stable_id",
    "zygosity",
    "sex",
    "life_stage_name",
    "p_value",
    "effect_size",
    "phenotyping_center",
    "allele_symbol",
    "assertion_type",
]

GENE_FIELDS = [
    "mgi_accession_id",
    "marker_symbol",
    "marker_type",
    "human_gene_symbol",
    "phenotyping_data_available",
    "embryo_data_available",
    "is_idg_gene",
]


def solr_rows(core: str, fields: list[str], query: str = "*:*") -> list[dict]:
    """Page through a Solr core returning every document as a dict."""
    url = f"{SOLR}/{core}/select"
    total = requests.get(
        url, params={"q": query, "rows": 0, "wt": "json"}, timeout=120
    ).json()["response"]["numFound"]
    out: list[dict] = []
    step = 20000
    for start in range(0, total, step):
        r = requests.get(
            url,
            params={
                "q": query,
                "rows": step,
                "start": start,
                "fl": ",".join(fields),
                "wt": "json",
            },
            timeout=600,
        )
        r.raise_for_status()
        out.extend(r.json()["response"]["docs"])
    assert len(out) == total, (len(out), total)
    return out


def flatten(doc: dict, fields: list[str]) -> dict:
    row = {}
    for f in fields:
        v = doc.get(f, "")
        if isinstance(v, list):
            v = "|".join(str(x) for x in v)
        row[f] = v
    return row


def write_tsv(path: Path, docs: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for d in docs:
            w.writerow(flatten(d, fields))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cache", type=Path, default=CACHE)
    args = ap.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)

    gp = solr_rows("genotype-phenotype", GP_FIELDS)
    write_tsv(args.cache / "genotype_phenotype.tsv", gp, GP_FIELDS)
    genes = solr_rows("gene", GENE_FIELDS)
    write_tsv(args.cache / "genes.tsv", genes, GENE_FIELDS)

    meta = {"genotype_phenotype_rows": len(gp), "gene_rows": len(genes)}
    (args.cache / "fetch_meta.json").write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta))


if __name__ == "__main__":
    main()
