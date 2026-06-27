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
            with open(path, encoding="utf-8") as fh:
                d = yaml.safe_load(fh)
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


# NCIT classes too broad to be useful rollup buckets (every drug is under them).
_ROOT_CLASS_LABELS = frozenset(
    {
        "Drug, Food, Chemical or Biomedical Material",
        "Pharmacologic Substance",
        "Conceptual Entity",
        "Chemical Viewed Functionally",
        "Chemical Viewed Structurally",
        "Organic Chemical",
        "Biological Agent",
        "Substance",
    }
)

# Advisory, hand-curated NCIT-class -> dismech mechanism-module hints. Extend as
# needed; absence of a hint is not meaningful. Keyed on the NCIT class label.
_MODULE_HINTS = {
    "Immune Checkpoint Inhibitor": "immune_checkpoint_blockade",
    "Immune Checkpoint Modulator": "immune_checkpoint_blockade",
    "Protein Synthesis Inhibitor": "bacterial_protein_synthesis_inhibition",
    "Macrolide Antibiotic": "bacterial_protein_synthesis_inhibition",
    "Tetracycline Antibiotic": "bacterial_protein_synthesis_inhibition",
    "Aminoglycoside Antibiotic": "bacterial_protein_synthesis_inhibition",
    "Beta-Lactam Antibiotic": "bacterial_cell_wall_synthesis_inhibition",
    "Glycopeptide Antibiotic": "bacterial_cell_wall_synthesis_inhibition",
    "Fluoroquinolone Antimicrobial": "bacterial_dna_topoisomerase_inhibition",
    "Rifamycin Antibiotic": "bacterial_rna_polymerase_inhibition",
    "Sulfonamide Antibacterial Agent": "bacterial_folate_synthesis_inhibition",
    "PARP Inhibitor": "dna_repair_synthetic_lethality",
}


@dataclass
class _Row:
    drug_id: str
    drug_label: str
    chebi_id: str
    status: str
    disorders: list[str]


@dataclass
class _ClassRollup:
    class_id: str
    label: str
    total: int = 0
    present: int = 0
    with_evidence: int = 0

    @property
    def absent(self) -> int:
        return self.total - self.present

    @property
    def coverage(self) -> float:
        return self.present / self.total if self.total else 0.0


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


def _load_isa(ncit_ids: list[str]) -> tuple[dict[str, set[str]], dict[str, str]]:
    """Return (drug_id -> named NCIT ancestor class ids, class_id -> label).

    Only named ``NCIT:C*`` superclasses are followed; anonymous OWL restriction
    superclasses (``_:`` blank nodes, e.g. role/target restrictions) are
    dropped. Universal root classes are pruned by the caller via
    ``_ROOT_CLASS_LABELS``.
    """
    from oaklib import get_adapter
    from sqlalchemy import text

    adapter = get_adapter("sqlite:obo:ncit")
    # Bulk-load every named is-a edge once, then close transitively in memory.
    parents: dict[str, list[str]] = defaultdict(list)
    with adapter.engine.connect() as conn:
        for subject, obj in conn.execute(
            text(
                "SELECT subject, object FROM statements "
                "WHERE predicate='rdfs:subClassOf' "
                "AND object LIKE 'NCIT:%'"
            )
        ).fetchall():
            parents[subject].append(obj)

    ancestors: dict[str, set[str]] = {}
    for drug in ncit_ids:
        seen: set[str] = set()
        stack = list(parents.get(drug, []))
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            stack.extend(parents.get(cur, []))
        ancestors[drug] = seen

    needed: set[str] = set()
    for s in ancestors.values():
        needed |= s
    labels = _fetch_labels(adapter, needed)
    return ancestors, labels


def _fetch_labels(adapter, ids: set[str]) -> dict[str, str]:
    from sqlalchemy import text

    ids = [i for i in ids if i]
    out: dict[str, str] = {}
    with adapter.engine.connect() as conn:
        for i in range(0, len(ids), 400):
            chunk = ids[i : i + 400]
            placeholders = ",".join(f":s{j}" for j in range(len(chunk)))
            params = {f"s{j}": cid for j, cid in enumerate(chunk)}
            stmt = text(
                "SELECT subject, value FROM statements "
                f"WHERE predicate='rdfs:label' AND subject IN ({placeholders})"
            )
            for subject, value in conn.execute(stmt, params).fetchall():
                if value and subject not in out:
                    out[subject] = str(value)
    return out


def rollup_by_class(rows: list[_Row]) -> list[_ClassRollup]:
    """Aggregate drug-level coverage by NCIT is-a drug class."""
    ancestors, labels = _load_isa([r.drug_id for r in rows])
    buckets: dict[str, _ClassRollup] = {}
    for r in rows:
        present = r.status != "ABSENT"
        with_ev = r.status == "PRESENT_WITH_EVIDENCE"
        for cid in ancestors.get(r.drug_id, set()):
            label = labels.get(cid, cid)
            if label in _ROOT_CLASS_LABELS:
                continue
            b = buckets.get(cid)
            if b is None:
                b = buckets[cid] = _ClassRollup(class_id=cid, label=label)
            b.total += 1
            b.present += int(present)
            b.with_evidence += int(with_ev)
    # Most-populated, least-covered classes first.
    return sorted(
        buckets.values(), key=lambda b: (-b.total, b.coverage, b.label)
    )


def format_class_tsv(buckets: list[_ClassRollup]) -> str:
    lines = ["class_id\tclass_label\ttotal\tpresent\tabsent\tcoverage_pct\tmodule_hint"]
    for b in buckets:
        lines.append(
            f"{b.class_id}\t{b.label}\t{b.total}\t{b.present}\t{b.absent}\t"
            f"{b.coverage * 100:.0f}\t{_MODULE_HINTS.get(b.label, '-')}"
        )
    return "\n".join(lines)


def format_class_summary(buckets: list[_ClassRollup], limit: int = 30) -> str:
    out: list[str] = []
    out.append("# NCIT P302 coverage rolled up by is-a drug class")
    out.append("")
    out.append(
        "Each P302 drug counts toward every named NCIT class it is-a (transitive; "
        "anonymous restrictions and universal roots dropped). `present` = drug is "
        "used as a dismech `therapeutic_agent`."
    )
    out.append("")
    out.append(f"- Distinct drug classes: **{len(buckets)}**")
    out.append("")
    out.append("## Largest classes (total drugs, dismech coverage)")
    out.append("")
    out.append("| NCIT class | total | present | absent | cov% | module hint |")
    out.append("|---|--:|--:|--:|--:|---|")
    for b in buckets[:limit]:
        out.append(
            f"| {b.label} (`{b.class_id}`) | {b.total} | {b.present} | "
            f"{b.absent} | {b.coverage * 100:.0f} | "
            f"{_MODULE_HINTS.get(b.label, '')} |"
        )
    out.append("")
    gaps = [b for b in buckets if b.total >= 3 and b.present == 0]
    out.append(
        f"## Fully-uncovered classes (>=3 drugs, 0 in dismech): {len(gaps)}"
    )
    out.append("")
    for b in gaps[:limit]:
        out.append(f"- {b.label} (`{b.class_id}`): {b.total} drugs")
    return "\n".join(out)


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
    ap.add_argument(
        "--by-class",
        action="store_true",
        help="Roll up coverage by NCIT is-a drug class instead of per-drug",
    )
    ap.add_argument("--out", type=Path, help="Write output to a file instead of stdout")
    ap.add_argument("--limit", type=int, default=30, help="Examples in summary mode")
    args = ap.parse_args()

    rows = audit()
    if args.by_class:
        buckets = rollup_by_class(rows)
        text = (
            format_class_tsv(buckets)
            if args.format == "tsv"
            else format_class_summary(buckets, limit=args.limit)
        )
        unit = f"{len(buckets)} classes"
    else:
        text = (
            format_tsv(rows)
            if args.format == "tsv"
            else format_summary(rows, limit=args.limit)
        )
        unit = f"{len(rows)} drugs"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out} ({unit})")
    else:
        print(text)


if __name__ == "__main__":
    main()
