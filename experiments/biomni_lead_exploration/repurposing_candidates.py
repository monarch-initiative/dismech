"""List drugs acting on a disease's mechanism genes, and whether each was ever tested in it.

For each gene, ask Open Targets (public GraphQL API, no key) for every drug or clinical
candidate acting on it, in any disease, with its highest clinical stage and its action
type on that gene. A drug counts as already tested in the disease when Open Targets lists
it against the disease, or when ClinicalTrials.gov has a trial of it whose conditions or
title match the disease pattern.

Usage (from the repository root):
  uv run python experiments/biomni_lead_exploration/repurposing_candidates.py \\
      experiments/biomni_lead_exploration/sjogren/genes.tsv \\
      --disease MONDO_0010030 --pattern 'sj[oö]gren|sicca' \\
      --out experiments/biomni_lead_exploration/sjogren/opentargets/candidates.tsv

genes.tsv has two tab-separated columns: gene symbol, and why the gene is on the list.
"""

import argparse
import csv
import json
import re
import urllib.parse
import urllib.request
from functools import cache

OPEN_TARGETS_API = "https://api.platform.opentargets.org/api/v4/graphql"
CTGOV = "https://clinicaltrials.gov/api/v2/studies"
STAGE_ORDER = [
    "APPROVAL",
    "PHASE_4",
    "PHASE_3",
    "PHASE_2_3",
    "PHASE_2",
    "PHASE_1_2",
    "PHASE_1",
    "EARLY_PHASE_1",
    "PRECLINICAL",
    "UNKNOWN",
]


def stage_rank(stage: str | None) -> int:
    """Lower is further along.

    >>> stage_rank("APPROVAL") < stage_rank("PHASE_2") < stage_rank(None)
    True
    """
    return STAGE_ORDER.index(stage) if stage in STAGE_ORDER else len(STAGE_ORDER)


def matches(pattern: str, text: str) -> bool:
    """Case-insensitive search.

    >>> matches("sj[oö]gren|sicca", "Primary Sjögren's Syndrome")
    True
    >>> matches("sj[oö]gren|sicca", "Systemic lupus erythematosus")
    False
    """
    return re.search(pattern, text, re.I) is not None


def gql(query: str, variables: dict | None = None) -> dict:
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        OPEN_TARGETS_API, body, {"Content-Type": "application/json"}
    )
    data = json.load(urllib.request.urlopen(req, timeout=60))
    if "errors" in data:
        raise RuntimeError(data["errors"])
    return data["data"]


def resolve_target(symbol: str) -> str | None:
    hits = gql(
        'query($q:String!){ search(queryString:$q, entityNames:["target"], page:{index:0,size:5}){ hits{ id name } } }',
        {"q": symbol},
    )["search"]["hits"]
    return next((h["id"] for h in hits if h["name"] == symbol), None)


def disease_drugs(disease_id: str) -> set[str]:
    rows = gql(
        "query($id:String!){ disease(efoId:$id){ drugAndClinicalCandidates{ rows{ drug{ id } } } } }",
        {"id": disease_id},
    )["disease"]["drugAndClinicalCandidates"]["rows"]
    return {r["drug"]["id"] for r in rows}


def target_drugs(ensembl_id: str) -> list[dict]:
    q = """query($id:String!){ target(ensemblId:$id){ drugAndClinicalCandidates{ rows{
             maxClinicalStage
             drug{ id name mechanismsOfAction{ rows{ actionType targets{ id } } } }
             diseases{ disease{ name } } } } } }"""
    return gql(q, {"id": ensembl_id})["target"]["drugAndClinicalCandidates"]["rows"]


@cache
def ctgov_trials(drug_name: str, pattern: str) -> list[str]:
    url = (
        CTGOV
        + "?"
        + urllib.parse.urlencode(
            {
                "query.term": drug_name,
                "pageSize": 200,
                "fields": "NCTId,BriefTitle,Condition",
            }
        )
    )
    studies = json.load(urllib.request.urlopen(url, timeout=60)).get("studies", [])
    hits = []
    for s in studies:
        p = s["protocolSection"]
        text = (
            p["identificationModule"]["briefTitle"]
            + " "
            + " ".join(p.get("conditionsModule", {}).get("conditions", []))
        )
        if matches(pattern, text):
            hits.append(p["identificationModule"]["nctId"])
    return hits


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("genes")
    ap.add_argument(
        "--disease", required=True, help="Open Targets disease id, e.g. MONDO_0010030"
    )
    ap.add_argument(
        "--pattern",
        required=True,
        help="regex matching the disease in trial titles/conditions",
    )
    ap.add_argument("--out", required=True)
    ap.add_argument(
        "--max-stage",
        default="PHASE_2",
        help="only check trials for drugs at or beyond this stage",
    )
    args = ap.parse_args()

    known = disease_drugs(args.disease)
    genes = [
        row
        for row in csv.reader(open(args.genes), delimiter="\t")
        if row and not row[0].startswith("#")
    ]
    out_rows = []
    for symbol, why in genes:
        ensembl = resolve_target(symbol)
        if ensembl is None:
            out_rows.append(
                {"gene": symbol, "why": why, "drug": "", "note": "gene not resolved"}
            )
            continue
        best: dict[str, dict] = {}
        for r in target_drugs(ensembl):
            d = r["drug"]
            entry = best.setdefault(
                d["id"],
                {
                    "name": d["name"],
                    "stage": "UNKNOWN",
                    "diseases": set(),
                    "action": set(),
                },
            )
            if stage_rank(r["maxClinicalStage"]) < stage_rank(entry["stage"]):
                entry["stage"] = r["maxClinicalStage"]
            entry["diseases"].update(
                x["disease"]["name"] for x in r["diseases"] or [] if x.get("disease")
            )
            for m in (d.get("mechanismsOfAction") or {}).get("rows") or []:
                if (
                    any(t["id"] == ensembl for t in m["targets"] or [])
                    and m["actionType"]
                ):
                    entry["action"].add(m["actionType"])
        if not best:
            out_rows.append(
                {
                    "gene": symbol,
                    "why": why,
                    "drug": "",
                    "note": "no drugs in Open Targets",
                }
            )
        for chembl, e in sorted(
            best.items(), key=lambda kv: (stage_rank(kv[1]["stage"]), kv[1]["name"])
        ):
            trials = (
                ctgov_trials(e["name"], args.pattern)
                if stage_rank(e["stage"]) <= stage_rank(args.max_stage)
                else []
            )
            out_rows.append(
                {
                    "gene": symbol,
                    "why": why,
                    "drug": e["name"],
                    "chembl": chembl,
                    "stage": e["stage"],
                    "action": ",".join(sorted(e["action"])),
                    "in_opentargets_for_disease": chembl in known,
                    "disease_trials": ",".join(trials),
                    "other_indications": "; ".join(sorted(e["diseases"])[:6]),
                }
            )
    fields = [
        "gene",
        "why",
        "drug",
        "chembl",
        "stage",
        "action",
        "in_opentargets_for_disease",
        "disease_trials",
        "other_indications",
        "note",
    ]
    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(out_rows)
    print(f"wrote {len(out_rows)} rows to {args.out}")


if __name__ == "__main__":
    main()
