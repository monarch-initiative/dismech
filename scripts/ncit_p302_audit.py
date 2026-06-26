#!/usr/bin/env python3
"""Audit NCIT ``P302`` (Accepted_Therapeutic_Use_For) coverage in dismech.

``NCIT:P302`` links a drug to a free-text description of the disease/condition
it is an accepted treatment for. The free-text string is **left verbatim** and
serves as a citable evidence ``snippet:`` on a structured ``treatments`` record
(``reference: NCIT:<drug>``); it is deliberately *not* parsed.

So this audit is a pure **identifier join on the drug**, not text matching on
the indication. For each of the P302 drug concepts it asks:

* Is the drug used as a ``therapeutic_agent`` anywhere in ``kb/disorders`` —
  matched by its NCIT concept id or its ChEBI cross-reference (NCIT ``P368``)?
* If so, does any treatment in a disorder that uses the drug already cite the
  P302 assertion (``reference: NCIT:<drug>``)?

Three outcomes per drug:

* ``PRESENT_WITH_EVIDENCE`` — used as a treatment and the P302 evidence is
  already cited. Complete.
* ``PRESENT_NO_EVIDENCE``   — used as a treatment but the P302 assertion is not
  yet cited: a candidate evidence addition (drop in the verbatim P302 snippet).
* ``ABSENT``                — the drug is not used in any dismech treatment.

Usage::

    uv run python scripts/ncit_p302_audit.py --format summary
    uv run python scripts/ncit_p302_audit.py --format tsv --out output/ncit_p302_audit.tsv
"""

from __future__ import annotations

import argparse
import glob
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

from dismech.structured_sources.ontology_edges import OntologyEdgeSource  # noqa: E402

_KB_DIR = _REPO_ROOT / "kb" / "disorders"
_MANIFEST = _REPO_ROOT / "data" / "ncit-edges" / "MANIFEST.yaml"


@dataclass
class _Disorder:
    file: str
    name: str
    agent_ids: set[str] = field(default_factory=set)
    treatment_evidence_refs: set[str] = field(default_factory=set)


def _load_disorders() -> list[_Disorder]:
    out: list[_Disorder] = []
    for path in sorted(glob.glob(str(_KB_DIR / "*.yaml"))):
        try:
            d = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict) or not d.get("name"):
            continue
        rec = _Disorder(file=Path(path).name, name=str(d["name"]))
        for t in d.get("treatments") or []:
            if not isinstance(t, dict):
                continue
            tt = t.get("treatment_term") or {}
            for ag in tt.get("therapeutic_agent") or []:
                if isinstance(ag, dict):
                    term = ag.get("term") or {}
                    if term.get("id"):
                        rec.agent_ids.add(str(term["id"]))
            for ev in t.get("evidence") or []:
                if isinstance(ev, dict) and ev.get("reference"):
                    rec.treatment_evidence_refs.add(str(ev["reference"]))
        out.append(rec)
    return out


def _load_p302_drugs() -> list[tuple[str, str]]:
    """Return ``[(ncit_id, drug_label), ...]`` for every P302 subject."""
    OntologyEdgeSource.load_manifest(_MANIFEST)
    src = OntologyEdgeSource(_MANIFEST.parent)
    index = src.index()
    return sorted(
        (sid, rec.subject_label or sid)
        for sid, rec in index.items()
        if any(e.predicate_id == "NCIT:P302" for e in rec.edges)
    )


def _load_chebi_xrefs(ncit_ids: list[str]) -> dict[str, str]:
    """Map NCIT id -> ChEBI id via NCIT P368 (CHEBI_ID), for the given ids."""
    from oaklib import get_adapter
    from sqlalchemy import text

    adapter = get_adapter("sqlite:obo:ncit")
    out: dict[str, str] = {}
    wanted = set(ncit_ids)
    with adapter.engine.connect() as conn:
        for subject, value in conn.execute(
            text(
                "SELECT subject, value FROM statements "
                "WHERE predicate='NCIT:P368' AND value IS NOT NULL"
            )
        ).fetchall():
            if subject in wanted and value and subject not in out:
                out[subject] = str(value)
    return out


@dataclass
class _Row:
    drug_id: str
    drug_label: str
    chebi_id: str
    status: str
    disorders: list[str]


def audit() -> list[_Row]:
    disorders = _load_disorders()
    drugs = _load_p302_drugs()
    chebi = _load_chebi_xrefs([d for d, _ in drugs])

    # Index disorders by every agent id they use.
    by_agent: dict[str, list[_Disorder]] = defaultdict(list)
    for dis in disorders:
        for aid in dis.agent_ids:
            by_agent[aid].append(dis)

    rows: list[_Row] = []
    for ncit_id, label in drugs:
        chebi_id = chebi.get(ncit_id, "")
        candidate_ids = {ncit_id} | ({chebi_id} if chebi_id else set())
        using: list[_Disorder] = []
        seen: set[str] = set()
        for cid in candidate_ids:
            for dis in by_agent.get(cid, []):
                if dis.file not in seen:
                    seen.add(dis.file)
                    using.append(dis)
        if not using:
            status = "ABSENT"
        elif any(ncit_id in dis.treatment_evidence_refs for dis in using):
            status = "PRESENT_WITH_EVIDENCE"
        else:
            status = "PRESENT_NO_EVIDENCE"
        rows.append(
            _Row(
                drug_id=ncit_id,
                drug_label=label,
                chebi_id=chebi_id,
                status=status,
                disorders=sorted(dis.name for dis in using),
            )
        )
    return rows


def format_tsv(rows: list[_Row]) -> str:
    lines = ["drug_id\tdrug_label\tchebi_id\tstatus\tdisorders"]
    for r in rows:
        lines.append(
            f"{r.drug_id}\t{r.drug_label}\t{r.chebi_id or '-'}\t{r.status}\t"
            f"{'; '.join(r.disorders) or '-'}"
        )
    return "\n".join(lines)


def format_summary(rows: list[_Row], limit: int = 30) -> str:
    counts = Counter(r.status for r in rows)
    out: list[str] = []
    out.append("# NCIT P302 (Accepted_Therapeutic_Use_For) coverage audit")
    out.append("")
    out.append(f"- P302 drug assertions: **{len(rows)}**")
    out.append("- Join is by drug identity (NCIT concept id or its ChEBI P368")
    out.append("  cross-reference) against dismech `therapeutic_agent` ids.")
    out.append("")
    out.append("## Status counts")
    for status in ("PRESENT_WITH_EVIDENCE", "PRESENT_NO_EVIDENCE", "ABSENT"):
        out.append(f"- {status}: {counts.get(status, 0)}")
    out.append("")

    no_ev = [r for r in rows if r.status == "PRESENT_NO_EVIDENCE"]
    out.append(
        f"## Candidate evidence additions (PRESENT_NO_EVIDENCE): {len(no_ev)}"
    )
    out.append("")
    out.append(
        "Drug is already used as a dismech treatment but the P302 assertion is "
        "not cited. Add `reference: NCIT:<drug>` with the verbatim P302 string "
        "as the snippet to the matching treatment record(s)."
    )
    out.append("")
    for r in no_ev[:limit]:
        chebi = f" / {r.chebi_id}" if r.chebi_id else ""
        out.append(
            f"- **{r.drug_label}** (`{r.drug_id}`{chebi}) → "
            f"{'; '.join(r.disorders)}"
        )
    if len(no_ev) > limit:
        out.append(f"- … and {len(no_ev) - limit} more (see TSV).")
    out.append("")

    absent = [r for r in rows if r.status == "ABSENT"]
    out.append(f"## Drugs absent from dismech treatments (ABSENT): {len(absent)}")
    out.append("")
    out.append(
        "P302 asserts an accepted therapeutic use, but the drug is not a "
        "`therapeutic_agent` in any disorder. Leads for treatment/disorder "
        "curation (sample):"
    )
    out.append("")
    for r in absent[:limit]:
        chebi = f" / {r.chebi_id}" if r.chebi_id else ""
        out.append(f"- {r.drug_label} (`{r.drug_id}`{chebi})")
    if len(absent) > limit:
        out.append(f"- … and {len(absent) - limit} more (see TSV).")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--format", choices=["summary", "tsv"], default="summary")
    ap.add_argument("--out", type=Path, help="Write output to a file instead of stdout")
    ap.add_argument("--limit", type=int, default=30, help="Examples in summary mode")
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
        print(f"wrote {args.out} ({len(rows)} drugs)")
    else:
        print(text)


if __name__ == "__main__":
    main()
