"""Score arm candidates against a case rubric, automatically where possible (DRAFT, to be frozen).

For each candidate (schemas/candidate.yaml) and the case's rubric (rubrics/Cnnn.yaml):
  T2  automatic: analyte_type equals one of the rubric's T2 definitions, the specimen is in that
      definition's allowed set, and the candidate's target or analyte names a member of its
      target class (member label, gene-product form, or HGNC symbol/synonym).
  T4  automatic: the analyte or target names the exact analyte (a T4 term label, the T4 label,
      or one of the rubric's leakage terms, which are the names of the test and analyte).
  T1  not automatic: mapping a free-text mechanism onto the rubric's GO class needs judgment,
      so every candidate is sent to adjudication for T1.
  T3  not automatic: always adjudicated against the rubric's discovery experiment.
A candidate that also matches a t1_only_in_clinical_use analyte is flagged CLINICAL_T1_ONLY for
adjudication; if confirmed, it is capped at T1.

Alarms:
  T4_UNREACHABLE      T4 on a case whose rubric marks the analyte unreachable before the cutoff
  LEAKAGE_TERM        a leakage term with in_packet "no" anywhere in the candidate's text
For a negative's rubric every candidate is a false positive; nothing is matched.

Names are compared after normalisation (case-folded; Greek letters spelled out; runs of
non-alphanumerics collapsed), as whole words.

Usage (library): score(rubric, candidates) -> list of dicts. CLI:
    python match.py rubrics/C017.yaml candidates.json [--hgnc-synonyms]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

import yaml

GREEK = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "κ": "kappa", "ω": "omega", "μ": "mu",
         "τ": "tau", "ε": "epsilon"}
HGNC_DB = Path.home() / ".data" / "oaklib" / "hgnc.db"
TIER_ORDER = {"none": 0, "T1": 1, "T2": 2, "T3": 3, "T4": 4}


def norm(s: str) -> str:
    s = (s or "").casefold()
    for k, v in GREEK.items():
        s = s.replace(k, v)
    return " " + re.sub(r"[^0-9a-z]+", " ", s).strip() + " "


def names_in(text: str, names: set[str]) -> list[str]:
    t = norm(text)
    return sorted(n for n in names if n.strip() and norm(n) in t)


class Synonyms:
    """HGNC symbol -> exact synonyms that are symbol-like (no spaces), from the local hgnc.db."""

    def __init__(self, enabled: bool) -> None:
        self.db = sqlite3.connect(f"file:{HGNC_DB}?mode=ro", uri=True) if enabled and HGNC_DB.exists() else None

    def of(self, curie: str) -> set[str]:
        if not self.db or not curie.startswith("hgnc:"):
            return set()
        rows = self.db.execute("select value from statements where subject=? and predicate='oio:hasExactSynonym'",
                               (curie,)).fetchall()
        return {r[0] for r in rows if r[0] and " " not in r[0] and len(r[0]) >= 3}


def score(rubric: dict, candidates: list[dict], syn: Synonyms | None = None) -> list[dict]:
    syn = syn or Synonyms(False)
    out = []
    if "negative_id" in rubric:
        for c in candidates:
            out.append({**_base(c), "tier_auto": "none", "false_positive": True, "needs_adjudication": [],
                        "alarms": []})
        return out
    t4_names = {rubric["T4"]["exact_analyte"]} | {t["label"] for t in rubric["T4"]["terms"]} \
        | {b["term"] for b in rubric["leakage_terms"]}
    leak_no = {b["term"] for b in rubric["leakage_terms"] if b["in_packet"] == "no"}
    clinical = rubric["T1"].get("t1_only_in_clinical_use") or []
    for c in candidates:
        text = " ".join(str(c.get(k, "")) for k in ("analyte", "target"))
        full = " ".join(str(c.get(k, "")) for k in ("analyte", "target", "mechanism", "rationale"))
        t2 = False
        for d in rubric["T2"]:
            if c.get("analyte_type") != d["analyte_type"] or c.get("specimen") not in d["allowed_specimens"]:
                continue
            members = set()
            for m in d["target_class"]["members"]:
                if m.get("form"):  # a gene product of the member gene: match the product, not the gene
                    members |= set(_keys(m["form"]))
                else:
                    members |= {m["label"]} | syn.of(m["id"])
            if names_in(text, members):
                t2 = True
        t4 = bool(names_in(text, t4_names))
        alarms = []
        if t4 and rubric["T4"]["reachable_from_pre_cutoff"] == "no":
            alarms.append("T4_UNREACHABLE")
        hit_leak = names_in(full, leak_no)
        if hit_leak:
            alarms.append("LEAKAGE_TERM:" + ";".join(hit_leak))
        adj = ["T1", "T3"]
        if clinical and any(_clinical_key_hit(text, p) for p in clinical):
            adj.append("CLINICAL_T1_ONLY")
        tier = "T4" if (t4 and t2) else ("T2" if t2 else "none")
        out.append({**_base(c), "T2": t2, "T4_name": t4, "tier_auto": tier, "needs_adjudication": adj,
                    "alarms": alarms})
    return out


def _keys(phrase: str) -> list[str]:
    """The phrase before any comma or parenthesis, plus each parenthesised part."""
    return [k.strip() for k in re.findall(r"\(([^)]+)\)", phrase) + [re.split(r"[,(]", phrase)[0]] if k.strip()]


def _clinical_key_hit(text: str, phrase: str) -> bool:
    """A t1_only phrase matches when its parenthesised abbreviation or its leading phrase is named."""
    return any(norm(k).strip() and norm(k) in norm(text) for k in _keys(phrase))


def _base(c: dict) -> dict:
    return {k: c.get(k) for k in ("rank", "confidence", "analyte", "analyte_type", "specimen", "target")}


def final_tier(auto: dict, adjudication: dict | None) -> str:
    """Combine the automatic tier with an adjudication {T1: bool, T3: bool, CLINICAL_T1_ONLY: bool}."""
    a = adjudication or {}
    if a.get("CLINICAL_T1_ONLY"):
        return "T1"
    tiers = ["none"]
    if a.get("T1"):
        tiers.append("T1")
    if auto.get("T2"):
        tiers.append("T2")
    if auto.get("T2") and a.get("T3"):
        tiers.append("T3")
    if auto.get("tier_auto") == "T4":
        tiers.append("T4")
    return max(tiers, key=TIER_ORDER.get)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("rubric", type=Path)
    ap.add_argument("candidates", type=Path, help="JSON: {candidates: [...]}")
    ap.add_argument("--hgnc-synonyms", action="store_true")
    a = ap.parse_args()
    rubric = yaml.safe_load(a.rubric.read_text(encoding="utf-8"))
    cands = json.loads(a.candidates.read_text(encoding="utf-8"))["candidates"]
    json.dump(score(rubric, cands, Synonyms(a.hgnc_synonyms)), sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
