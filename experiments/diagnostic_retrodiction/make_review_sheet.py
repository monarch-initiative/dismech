"""Write the human dating review for the cases dating cannot settle on its own.

Cases reviewed (from dating_flags.tsv after build_dating.py has applied agent C):
  - NOT_ACCEPTED: the three agents name three different PMIDs, or no PMID has
    two agents with passing quotes;
  - ACCEPTED_FLAGGED: A and B agree, but an earlier paper looks like the real
    discovery report.

Outputs:
  dating_review_sheet.md   one section per case: every candidate PMID with its
                           PubMed title, journal, date, the agents that named it,
                           their quote and quote check, and the cutoff it implies.
                           The earlier assessment is given last, so the reviewer
                           can read the candidates first.
  dating_human_review.tsv  one row per case with blank columns for the reviewer.

Candidate titles and dates are read from PubMed esummary. NCBI_API_KEY is read
from the environment, sent only in the POST body, and never printed.
"""
from __future__ import annotations

import csv
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEW_STATUSES = ("NOT_ACCEPTED", "ACCEPTED_FLAGGED")
DECISIONS = "ACCEPT_PMID | NO_ADEQUATE_REPORT | EXCLUDE_CASE"


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def esummary(pmids: list[str]) -> dict[str, dict]:
    key = os.environ.get("NCBI_API_KEY", "").strip()
    if not key:
        sys.exit("NCBI_API_KEY is not set")
    body = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids), "retmode": "json",
                                   "tool": "dismech-retrodiction", "api_key": key}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi", data=body), timeout=60) as r:
            res = json.load(r)["result"]
    except Exception as e:  # type only: the request body carries the key
        sys.exit(f"esummary failed ({type(e).__name__})")
    return {u: res[u] for u in res.get("uids", [])}


def strip(p: str) -> str:
    return (p or "").replace("PMID:", "").strip()


def main() -> None:
    flags = [f for f in read_tsv(HERE / "dating_flags.tsv") if f["dating_status"] in REVIEW_STATUSES]
    dating = {r["case_id"]: r for r in read_tsv(HERE / "literature_check.tsv")}
    checked = {}
    for agent in "ABC":
        path = HERE / "dating_checks" / f"agent{agent}.checked.tsv"
        for r in read_tsv(path):
            checked[(agent, r["disease"], r["test"])] = r

    # candidate PMID -> list of (agent, checked row); "earlier" for the flag's candidate
    per_case = []
    all_pmids: set[str] = set()
    for f in sorted(flags, key=lambda r: r["case_id"]):
        cands: dict[str, list[tuple[str, dict | None]]] = {}
        for agent in "ABC":
            r = checked.get((agent, f["disease"], f["test"]))
            if r is not None:
                cands.setdefault(strip(r["discovery_pmid"]), []).append((agent, r))
        if strip(f["candidate_pmid"]):
            cands.setdefault(strip(f["candidate_pmid"]), []).append(("earlier-candidate", None))
        all_pmids |= set(cands)
        per_case.append((f, cands))
    summ = esummary(sorted(all_pmids, key=int))

    def cutoff(pmid: str) -> str:
        for agent_rows in (c for _, c in per_case):
            for agent, r in agent_rows.get(pmid, []):
                if r is not None and r["pubmed_date"] != "NA":
                    return f"{int(r['pubmed_date'][:4]) - 1}-12-31"
        s = summ.get(pmid, {})
        year = (s.get("pubdate") or "")[:4]
        return f"{int(year) - 1}-12-31 (from PubMed pubdate)" if year.isdigit() else "NA"

    md = ["# Dating review sheet", "",
          "Cases whose discovery report the dating agents could not settle. For each, pick the",
          "**first primary research report** of the test for this disease (eligibility rules",
          "v3, rule 5) and record it in `dating_human_review.tsv`. The case's cutoff is 31",
          "December of the year before that report's PubMed date (the earlier of issue and",
          "e-publication date).", "",
          "- **NOT_ACCEPTED:** agents A, B and C name three different PMIDs, or no PMID is",
          "  named by two agents whose quotes both pass.",
          "- **ACCEPTED_FLAGGED:** A and B agree, but an earlier paper may be the real report.", "",
          "Each case lists its candidates first. The earlier written assessment comes last;",
          "read the candidates before it.", "",
          f"Decisions in the TSV: `{DECISIONS}`.", ""]
    rows = []
    for f, cands in per_case:
        cid = f["case_id"]
        subset = dating.get(cid, {}).get("subset", "")
        md += [f"## {cid}: {f['disease']} — {f['test']}", "",
               f"- **Status:** {f['dating_status']} ({f['flag_type']})",
               f"- **Subset:** {subset}", "",
               "| PMID | Named by | Title | Journal | PubMed date | Implied cutoff |",
               "|---|---|---|---|---|---|"]
        for pmid in sorted(cands, key=int):
            s = summ.get(pmid, {})
            who = ", ".join(a for a, _ in cands[pmid])
            title = (s.get("title") or "?").replace("|", "/")
            md.append(f"| [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/) | {who} | {title} | "
                      f"{s.get('source', '?')} | {s.get('pubdate', '?')} | {cutoff(pmid)} |")
        md.append("")
        for pmid in sorted(cands, key=int):
            for agent, r in cands[pmid]:
                if r is None:
                    continue
                qok = {"TRUE": "matches the abstract", "FALSE": "does NOT match the abstract",
                       "NA": "not checkable (no abstract in PubMed)"}.get(r["quote_ok"], r["quote_ok"])
                md += [f"- **Agent {agent}, PMID {pmid}** (quote {qok}):", f"  > {r['quote']}"]
        md += ["", "<details><summary>Earlier assessment</summary>", "", f["assessment"], "", "</details>", ""]
        rows.append({"case_id": cid, "disease": f["disease"], "test": f["test"], "subset": subset,
                     "dating_status": f["dating_status"],
                     "candidates": "; ".join(f"{p} ({', '.join(a for a, _ in cands[p])})"
                                             for p in sorted(cands, key=int)),
                     "decision": "", "reviewer_pmid": "", "reviewer_cutoff": "",
                     "reviewer": "", "review_date": "", "notes": ""})

    (HERE / "dating_review_sheet.md").write_text("\n".join(md), encoding="utf-8")
    with open(HERE / "dating_human_review.tsv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} cases: " + ", ".join(r["case_id"] for r in rows), file=sys.stderr)


if __name__ == "__main__":
    main()
