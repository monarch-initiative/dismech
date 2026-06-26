#!/usr/bin/env python3
"""Audit NCIT ``P302`` (Accepted_Therapeutic_Use_For) coverage in dismech.

``NCIT:P302`` links a drug to a free-text description of the disease/condition
it is an accepted treatment for. This script reads every P302 assertion via the
generic :class:`OntologyEdgeSource` (the same data that backs the
``references_cache/NCIT_*.md`` files) and maps each indication onto dismech
disorders, producing an **advisory** coverage report.

Three outcomes per (drug, indication, matched-disorder) row:

* ``COVERED``           — the disorder exists and the drug is already listed in
  its ``treatments`` (by name or ``therapeutic_agent``).
* ``MISSING_TREATMENT`` — the disorder exists but the drug is not in its
  treatment list: a candidate ``treatments`` addition, citable as
  ``reference: NCIT:<drug>``.
* ``NO_DISORDER``       — the indication maps to no dismech disorder: a
  candidate new-disorder / curation-backlog lead.

Matching is deliberately conservative free-text heuristics (normalized
phrase-substring of disorder name / synonym / MONDO label). It is a triage aid,
not ground truth — every MISSING_TREATMENT row still needs a curator to confirm
the indication actually corresponds to the matched disorder before citing it.

Usage::

    uv run python scripts/ncit_p302_audit.py --format summary
    uv run python scripts/ncit_p302_audit.py --format tsv --out output/ncit_p302_audit.tsv
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

from dismech.structured_sources.ontology_edges import OntologyEdgeSource  # noqa: E402

_KB_DIR = _REPO_ROOT / "kb" / "disorders"
_MANIFEST = _REPO_ROOT / "data" / "ncit-edges" / "MANIFEST.yaml"

# Generic disease words that, on their own, would over-match free-text
# indications. A disorder match phrase made up solely of these is dropped.
_STOPWORDS = frozenset(
    """
    disease disorder syndrome cancer carcinoma tumor tumour neoplasm
    deficiency chronic acute disorders diseases of the and type infection
    primary secondary congenital familial idiopathic adult juvenile
    """.split()
)


def _norm(text: str) -> str:
    """Lowercase, strip punctuation to spaces, collapse whitespace."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", text.lower())).strip()


@dataclass
class _Disorder:
    file: str
    name: str
    mondo: str
    phrases: tuple[str, ...]  # normalized match phrases
    drug_terms: frozenset[str]  # normalized treatment/agent names already present


def _load_disorders() -> list[_Disorder]:
    out: list[_Disorder] = []
    for path in sorted(glob.glob(str(_KB_DIR / "*.yaml"))):
        try:
            d = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict) or not d.get("name"):
            continue
        name = str(d["name"])
        dterm = d.get("disease_term") or {}
        mondo = str(((dterm.get("term") or {}).get("id")) or "")
        mondo_label = str(((dterm.get("term") or {}).get("label")) or "")

        phrase_src = [name, mondo_label, *(d.get("synonyms") or [])]
        phrases: set[str] = set()
        for p in phrase_src:
            np = _norm(str(p))
            if len(np) < 5:
                continue
            tokens = np.split()
            if all(t in _STOPWORDS for t in tokens):
                continue
            phrases.add(np)

        drug_terms: set[str] = set()
        for t in d.get("treatments") or []:
            if not isinstance(t, dict):
                continue
            if t.get("name"):
                drug_terms.add(_norm(str(t["name"])))
            tt = t.get("treatment_term") or {}
            for ag in tt.get("therapeutic_agent") or []:
                if not isinstance(ag, dict):
                    continue
                if ag.get("preferred_term"):
                    drug_terms.add(_norm(str(ag["preferred_term"])))
                term = ag.get("term") or {}
                if term.get("label"):
                    drug_terms.add(_norm(str(term["label"])))

        out.append(
            _Disorder(
                file=Path(path).name,
                name=name,
                mondo=mondo,
                phrases=tuple(sorted(phrases)),
                drug_terms=frozenset(drug_terms),
            )
        )
    return out


def _drug_present(drug_label: str, disorder: _Disorder) -> bool:
    nd = _norm(drug_label)
    if not nd:
        return False
    for term in disorder.drug_terms:
        if nd == term or nd in term or term in nd:
            return True
    return False


@dataclass
class _Row:
    drug_id: str
    drug_label: str
    indication: str
    disorder: str
    mondo: str
    status: str


def _load_p302_records():
    OntologyEdgeSource.load_manifest(_MANIFEST)
    src = OntologyEdgeSource(_MANIFEST.parent)
    index = src.index()
    records = []
    for subject_id, rec in sorted(index.items()):
        for edge in rec.edges:
            if edge.predicate_id != "NCIT:P302":
                continue
            records.append((subject_id, rec.subject_label, edge.metadata))
    return records


def audit() -> list[_Row]:
    disorders = _load_disorders()
    records = _load_p302_records()
    rows: list[_Row] = []
    for drug_id, drug_label, indication in records:
        # Pad so phrase matching is token-aligned (" lung cancer " won't match
        # inside "lungcancerous"); contiguous-token false matches remain
        # possible and are why this report is advisory.
        norm_ind = f" {_norm(indication)} "
        matches = [
            dis
            for dis in disorders
            if any(f" {ph} " in norm_ind for ph in dis.phrases)
        ]
        if not matches:
            rows.append(
                _Row(drug_id, drug_label, indication, "-", "-", "NO_DISORDER")
            )
            continue
        for dis in matches:
            status = (
                "COVERED" if _drug_present(drug_label, dis) else "MISSING_TREATMENT"
            )
            rows.append(
                _Row(drug_id, drug_label, indication, dis.name, dis.mondo, status)
            )
    return rows


def format_tsv(rows: list[_Row]) -> str:
    header = "drug_id\tdrug_label\tindication\tdisorder\tmondo\tstatus"
    lines = [header]
    for r in rows:
        ind = r.indication.replace("\t", " ").replace("\n", " ")
        lines.append(
            f"{r.drug_id}\t{r.drug_label}\t{ind}\t{r.disorder}\t{r.mondo}\t{r.status}"
        )
    return "\n".join(lines)


def format_summary(rows: list[_Row], limit: int = 25) -> str:
    status_counts = Counter(r.status for r in rows)
    drugs = {r.drug_id for r in rows}
    n_covered_drugs = {r.drug_id for r in rows if r.status == "COVERED"}
    n_no_disorder = {r.drug_id for r in rows if r.status == "NO_DISORDER"}

    out: list[str] = []
    out.append("# NCIT P302 (Accepted_Therapeutic_Use_For) coverage audit")
    out.append("")
    out.append(f"- P302 drug assertions examined: **{len(drugs)}**")
    out.append(f"- (drug, disorder) match rows: **{len(rows)}**")
    out.append("")
    out.append("## Row status counts")
    for status in ("COVERED", "MISSING_TREATMENT", "NO_DISORDER"):
        out.append(f"- {status}: {status_counts.get(status, 0)}")
    out.append("")
    out.append(
        f"- drugs with >=1 disorder already covering them: "
        f"**{len(n_covered_drugs)}**"
    )
    out.append(
        f"- drugs whose indication matched NO dismech disorder: "
        f"**{len(n_no_disorder)}**"
    )
    out.append("")

    missing = [r for r in rows if r.status == "MISSING_TREATMENT"]
    out.append(
        f"## Candidate treatment additions (MISSING_TREATMENT): {len(missing)}"
    )
    out.append("")
    out.append("Disorder exists; P302 drug not yet in its treatment list.")
    out.append("")
    for r in missing[:limit]:
        out.append(
            f"- **{r.disorder}** ({r.mondo or '-'}) ← {r.drug_label} "
            f"(`NCIT:{r.drug_id.split(':')[-1]}`): "
            f"_{r.indication[:90]}_"
        )
    if len(missing) > limit:
        out.append(f"- … and {len(missing) - limit} more (see TSV).")
    out.append("")

    no_dis = [r for r in rows if r.status == "NO_DISORDER"]
    out.append(f"## Candidate new disorders (NO_DISORDER): {len(no_dis)} drugs")
    out.append("")
    out.append(
        "Indication maps to no dismech disorder. Most frequent indication "
        "phrases (curation-backlog leads):"
    )
    out.append("")
    phrase_counts = Counter(_norm(r.indication)[:60] for r in no_dis)
    for phrase, n in phrase_counts.most_common(limit):
        out.append(f"- ({n}) {phrase}")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--format", choices=["summary", "tsv"], default="summary"
    )
    ap.add_argument("--out", type=Path, help="Write output to a file instead of stdout")
    ap.add_argument("--limit", type=int, default=25, help="Examples in summary mode")
    args = ap.parse_args()

    rows = audit()
    text = (
        format_tsv(rows)
        if args.format == "tsv"
        else format_summary(rows, limit=args.limit)
    )
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out} ({len(rows)} rows)")
    else:
        print(text)


if __name__ == "__main__":
    main()
