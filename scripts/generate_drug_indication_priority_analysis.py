#!/usr/bin/env python3
"""Generate a drug-indication gap analysis for dismech coverage.

This script:
1. parses the Monarch prioritised rare disease YAML
2. keeps diseases with at least one `research[].drug_label`
3. checks MONDO coverage against `kb/disorders/*.yaml`
4. scores the missing diseases with MONDO specificity heuristics, drug-signal density,
   cached ClinGen support, and a transparent curator-fit adjustment
5. writes a markdown report
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
import sys
from collections import Counter
from collections import defaultdict
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


DEFAULT_SOURCE = Path("/tmp/prioritised-rare-disease-list.yml")
DEFAULT_OUTPUT = REPO_ROOT / "research" / "drug_indication_priority_analysis.md"
DEFAULT_KB_DIR = REPO_ROOT / "kb" / "disorders"
DEFAULT_MONDO_DB = Path.home() / ".data" / "oaklib" / "mondo.db"
DEFAULT_CLINGEN_CSV = REPO_ROOT / "cache" / "clingen" / "gene_validity.csv"
DEFAULT_CONFIG = REPO_ROOT / "conf" / "mondo_prioritizer.yaml"

YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

HIGH_CONFIDENCE = {"HIGH", "MEDIUM"}


@dataclass(frozen=True)
class FitOverride:
    """Transparent curator-fit adjustment applied after quantitative scoring."""

    adjustment: float
    rationale: str


@dataclass
class DrugSignal:
    """Drug-indication summary extracted from the source YAML."""

    mondo_id: str
    label: str
    drug_indication_count: int
    medium_high_evidence_count: int
    high_evidence_count: int
    low_evidence_count: int
    hpo_treatment_rank: float
    example_drugs: list[str]


@dataclass
class RankedCandidate:
    """Final ranked output row."""

    mondo_id: str
    label: str
    final_score: float
    drug_indication_count: int
    medium_high_evidence_count: int
    clingen_definitive_count: int
    clingen_strong_count: int
    recommended_action: str
    specificity_bucket: str
    rationale: str


FIT_OVERRIDES: dict[str, FitOverride] = {
    "MONDO:0008294": FitOverride(
        adjustment=72.0,
        rationale=(
            "High-priority monogenic metabolic disease with an unusually clear mechanism "
            "and disease-specific therapy signal (`givosiran`, heme prophylaxis)."
        ),
    ),
    "MONDO:0009249": FitOverride(
        adjustment=40.0,
        rationale=(
            "High-priority monogenic metabolic disease with exact ClinGen support and a "
            "credible targeted pipeline (KHK inhibition / PF-06835919)."
        ),
    ),
    "MONDO:0001347": FitOverride(
        adjustment=60.0,
        rationale=(
            "Strong mechanistic fit for dismech: coherent DUX4-centered pathophysiology "
            "and an active therapeutic pipeline at the disease-root level."
        ),
    ),
    "MONDO:0008087": FitOverride(
        adjustment=40.0,
        rationale=(
            "Clear PMP22 dosage mechanism plus exact ClinGen support; fewer signals than "
            "top metabolic entries, but still a very curation-friendly disease entity."
        ),
    ),
    "MONDO:0007534": FitOverride(
        adjustment=10.0,
        rationale=(
            "Broad syndromic disorder, but still worth prioritizing because the imprinting/"
            "growth-pathway biology is tractable and the treatment literature is deep."
        ),
    ),
    "MONDO:0010382": FitOverride(
        adjustment=55.0,
        rationale=(
            "Good mechanistic repeat-expansion disease target with enough therapeutic "
            "literature to support a focused dismech entry."
        ),
    ),
    "MONDO:0008564": FitOverride(
        adjustment=35.0,
        rationale=(
            "Deletion syndrome with pleiotropic biology, but immune/endocrine treatment "
            "signals and a recognizable disease entity still make it a solid medium-high target."
        ),
    ),
    "MONDO:0008678": FitOverride(
        adjustment=20.0,
        rationale=(
            "Reasonable syndromic target with clear copy-number biology and enough "
            "cardiovascular/neurodevelopmental therapeutic literature to justify curation."
        ),
    ),
    "MONDO:0007452": FitOverride(
        adjustment=45.0,
        rationale=(
            "Mechanistically strong, treatment-responsive monogenic diabetes subtype, but "
            "better handled with an explicit MODY root/series strategy than as a lone subtype."
        ),
    ),
    "MONDO:0007453": FitOverride(
        adjustment=55.0,
        rationale=(
            "Mechanistically strong monogenic diabetes subtype with clear pharmacogenomic "
            "implications, though it should probably be curated under a MODY family plan."
        ),
    ),
    "MONDO:0011929": FitOverride(
        adjustment=-80.0,
        rationale=(
            "Drug-rich but heterogeneous contiguous-gene deletion syndrome; many signals are "
            "symptom-targeted rather than a clean disease-mechanism curation target."
        ),
    ),
    "MONDO:0029141": FitOverride(
        adjustment=-10.0,
        rationale=(
            "Disease entity is valid, but the term is subtype-level and much of the current "
            "therapy discussion is inherited-retinal/Usher extrapolation rather than USH4-specific."
        ),
    ),
    "MONDO:0010775": FitOverride(
        adjustment=10.0,
        rationale=(
            "Potentially useful sensory-disease entry, but much of the drug signal is shared "
            "retinal-disease pipeline work rather than syndrome-specific intervention evidence."
        ),
    ),
    "MONDO:0007810": FitOverride(
        adjustment=-10.0,
        rationale=(
            "Reasonable disease entity, but most current signals are topical/systemic retinoid "
            "management or broader ichthyosis extrapolation rather than a standout mechanistic target."
        ),
    ),
    "MONDO:0008698": FitOverride(
        adjustment=-15.0,
        rationale=(
            "Clear clinical entity, but mechanism is heterogeneous and much of the treatment "
            "signal is symptomatic or procedure-adjunctive rather than disease-mechanistic."
        ),
    ),
    "MONDO:0007523": FitOverride(
        adjustment=-20.0,
        rationale=(
            "Important disorder, but weak molecular anchoring makes mechanism curation harder "
            "than for the stronger monogenic candidates above it."
        ),
    ),
    "MONDO:0007184": FitOverride(
        adjustment=-100.0,
        rationale=(
            "High raw drug count, but awkward subtype granularity and mostly common alopecia "
            "treatment literature make this a weak dismech target."
        ),
    ),
    "MONDO:0012454": FitOverride(
        adjustment=-50.0,
        rationale=(
            "Lowest-fit candidate: the term behaves more like a susceptibility/physiologic "
            "response bucket, and its drug list mixes causes, triggers, and related-condition therapy."
        ),
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a drug-indication priority analysis markdown report."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"Path to prioritised rare disease YAML (default: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output markdown path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--kb-dir",
        type=Path,
        default=DEFAULT_KB_DIR,
        help=f"Path to dismech disorder YAML directory (default: {DEFAULT_KB_DIR})",
    )
    parser.add_argument(
        "--mondo-db",
        type=Path,
        default=DEFAULT_MONDO_DB,
        help=f"Path to local MONDO sqlite database (default: {DEFAULT_MONDO_DB})",
    )
    parser.add_argument(
        "--clingen-csv",
        type=Path,
        default=DEFAULT_CLINGEN_CSV,
        help=f"Path to cached ClinGen gene-validity CSV (default: {DEFAULT_CLINGEN_CSV})",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help=f"MONDO prioritizer config (default: {DEFAULT_CONFIG})",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=50,
        help="Maximum number of missing candidates to show in the table.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as stream:
        return yaml.load(stream, Loader=YAML_LOADER)


def load_mondo_priority_helpers() -> tuple[Any, Any, Any, Any]:
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from dismech.compare.mondo_priority import CandidateTerm
    from dismech.compare.mondo_priority import build_coverage_index
    from dismech.compare.mondo_priority import load_config
    from dismech.compare.mondo_priority import score_candidates

    return CandidateTerm, build_coverage_index, load_config, score_candidates


def load_source_diseases(path: Path) -> list[dict[str, Any]]:
    payload = load_yaml(path)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected YAML object in {path}")
    diseases = payload.get("diseases")
    if not isinstance(diseases, list):
        raise ValueError(f"Expected top-level `diseases` list in {path}")
    return [item for item in diseases if isinstance(item, dict)]


def extract_drug_signals(diseases: list[dict[str, Any]]) -> dict[str, DrugSignal]:
    signals: dict[str, DrugSignal] = {}
    for disease in diseases:
        mondo_id = str(disease.get("mondo_id") or "").strip()
        label = str(disease.get("mondo_label") or "").strip()
        if not mondo_id or not label:
            continue
        research = disease.get("research") or []
        drug_rows = [
            row
            for row in research
            if isinstance(row, dict) and str(row.get("drug_label") or "").strip()
        ]
        if not drug_rows:
            continue

        evidence_rows: list[dict[str, Any]] = []
        for row in drug_rows:
            evidence = row.get("evidence") or []
            evidence_rows.extend(item for item in evidence if isinstance(item, dict))

        confidence_counts = Counter(
            str(item.get("confidence_drug") or "").upper() for item in evidence_rows
        )
        example_drugs = [
            str(row.get("drug_label")).strip()
            for row in drug_rows
            if str(row.get("drug_label")).strip()
        ][:3]
        signals[mondo_id] = DrugSignal(
            mondo_id=mondo_id,
            label=label,
            drug_indication_count=len(drug_rows),
            medium_high_evidence_count=sum(
                count
                for confidence, count in confidence_counts.items()
                if confidence in HIGH_CONFIDENCE
            ),
            high_evidence_count=confidence_counts.get("HIGH", 0),
            low_evidence_count=confidence_counts.get("LOW", 0),
            hpo_treatment_rank=float(disease.get("hpo_treatment_rank") or 0.0),
            example_drugs=example_drugs,
        )
    return signals


def load_clingen_counts(path: Path) -> tuple[Counter[str], Counter[str]]:
    definitive = Counter()
    strong = Counter()
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.reader(stream)
        for _ in range(6):
            next(reader, None)
        for row in reader:
            if len(row) < 10 or not row[0] or row[0].startswith("+"):
                continue
            mondo_id = row[3].strip()
            classification = row[6].strip().lower()
            if not mondo_id:
                continue
            if classification == "definitive":
                definitive[mondo_id] += 1
            elif classification == "strong":
                strong[mondo_id] += 1
    return definitive, strong


def fetch_mondo_metadata(conn: sqlite3.Connection, mondo_id: str) -> dict[str, Any]:
    definition_row = conn.execute(
        """
        SELECT value
        FROM has_text_definition_statement
        WHERE subject = ? AND value IS NOT NULL
        ORDER BY value
        LIMIT 1
        """,
        (mondo_id,),
    ).fetchone()
    definition = definition_row[0] if definition_row else ""

    synonyms = [
        row[0]
        for row in conn.execute(
            """
            SELECT value
            FROM has_exact_synonym_statement
            WHERE subject = ? AND value IS NOT NULL
            ORDER BY value
            """,
            (mondo_id,),
        )
    ]

    xrefs = [
        row[0]
        for row in conn.execute(
            """
            SELECT value
            FROM has_dbxref_statement
            WHERE subject = ? AND value IS NOT NULL
            ORDER BY value
            """,
            (mondo_id,),
        )
    ]

    parents = [
        row[0]
        for row in conn.execute(
            """
            SELECT lbl.value
            FROM rdfs_subclass_of_statement s
            JOIN rdfs_label_statement lbl ON lbl.subject = s.object
            WHERE s.subject = ? AND lbl.value IS NOT NULL
            ORDER BY lbl.value
            """,
            (mondo_id,),
        )
    ]

    return {
        "definition": definition,
        "synonyms": synonyms,
        "xrefs": xrefs,
        "parents": parents,
    }


def build_child_index(conn: sqlite3.Connection) -> dict[str, set[str]]:
    child_index: dict[str, set[str]] = defaultdict(set)
    for child, parent in conn.execute(
        """
        SELECT subject, object
        FROM rdfs_subclass_of_statement
        WHERE subject LIKE 'MONDO:%' AND object LIKE 'MONDO:%'
        """
    ):
        child_index[parent].add(child)
    return child_index


def get_descendants(mondo_id: str, child_index: dict[str, set[str]]) -> list[str]:
    descendants: set[str] = {mondo_id}
    queue: deque[str] = deque([mondo_id])
    while queue:
        current = queue.popleft()
        for child in child_index.get(current, set()):
            if child in descendants:
                continue
            descendants.add(child)
            queue.append(child)
    return sorted(descendants)


def build_ranked_candidates(
    signals: dict[str, DrugSignal],
    kb_dir: Path,
    mondo_db: Path,
    clingen_csv: Path,
    config_path: Path,
) -> tuple[list[RankedCandidate], dict[str, int]]:
    CandidateTerm, build_coverage_index, load_config, score_candidates = (
        load_mondo_priority_helpers()
    )
    coverage = build_coverage_index(kb_dir)
    definitive_counts, strong_counts = load_clingen_counts(clingen_csv)

    conn = sqlite3.connect(str(mondo_db))
    child_index = build_child_index(conn)
    candidate_terms: list[CandidateTerm] = []

    for signal in signals.values():
        meta = fetch_mondo_metadata(conn, signal.mondo_id)
        descendants = get_descendants(signal.mondo_id, child_index)
        descendant_definitive = sum(definitive_counts[mid] for mid in descendants)
        descendant_strong = sum(strong_counts[mid] for mid in descendants)
        orphanet_match_count = sum(
            1
            for xref in meta["xrefs"]
            if str(xref).lower().startswith(("orphanet:", "ordo:"))
        )
        child_count = len(child_index.get(signal.mondo_id, set()))
        candidate_terms.append(
            CandidateTerm(
                mondo_id=signal.mondo_id,
                label=signal.label,
                definition=meta["definition"],
                synonyms=meta["synonyms"],
                parents=meta["parents"],
                xrefs=meta["xrefs"],
                child_count=child_count,
                is_obsolete=False,
                clingen_definitive_count=descendant_definitive,
                clingen_strong_count=descendant_strong,
                subset_match_count=0,
                orphanet_match_count=orphanet_match_count,
                raw={
                    "clingen_definitive_count": descendant_definitive,
                    "clingen_strong_count": descendant_strong,
                    "child_count": child_count,
                    "parents": meta["parents"],
                },
            )
        )

    scored = {
        item.mondo_id: item
        for item in score_candidates(
            candidate_terms,
            coverage=coverage,
            config=load_config(config_path),
        )
    }
    conn.close()

    ranked: list[RankedCandidate] = []
    action_counts: Counter[str] = Counter()

    for signal in signals.values():
        if signal.mondo_id in coverage.curated_ids:
            continue
        item = scored[signal.mondo_id]
        action_counts[item.recommended_action] += 1

        quantitative_score = (
            item.score
            + (signal.drug_indication_count * 4.0)
            + (signal.medium_high_evidence_count * 0.5)
            + (signal.high_evidence_count * 1.5)
            + (signal.hpo_treatment_rank * 10.0)
        )
        override = FIT_OVERRIDES.get(
            signal.mondo_id,
            FitOverride(
                adjustment=0.0,
                rationale=(
                    "No manual fit override applied; ranked by MONDO specificity, "
                    "drug-signal density, and descendant-aware ClinGen support."
                ),
            ),
        )
        final_score = quantitative_score + override.adjustment
        ranked.append(
            RankedCandidate(
                mondo_id=signal.mondo_id,
                label=signal.label,
                final_score=round(final_score, 2),
                drug_indication_count=signal.drug_indication_count,
                medium_high_evidence_count=signal.medium_high_evidence_count,
                clingen_definitive_count=item.raw.get("clingen_definitive_count", 0),
                clingen_strong_count=item.raw.get("clingen_strong_count", 0),
                recommended_action=item.recommended_action,
                specificity_bucket=item.specificity_bucket,
                rationale=override.rationale,
            )
        )

    ranked.sort(key=lambda row: (-row.final_score, row.label.casefold()))
    return ranked, dict(action_counts)


def render_summary_stats(
    total_source_diseases: int,
    signal_count: int,
    missing_count: int,
    action_counts: dict[str, int],
) -> str:
    curated_count = signal_count - missing_count
    ordered_actions = [
        f"`{action}`: {count}"
        for action, count in sorted(
            action_counts.items(),
            key=lambda pair: (-pair[1], pair[0]),
        )
    ]
    lines = [
        f"- Total diseases in source YAML: **{total_source_diseases}**",
        f"- Diseases with at least one drug-indication block: **{signal_count}**",
        f"- Already curated in `kb/disorders/` by exact MONDO ID: **{curated_count}**",
        f"- Missing from dismech by exact MONDO ID: **{missing_count}**",
    ]
    if ordered_actions:
        lines.append(
            "- Missing-candidate specificity/actions: " + ", ".join(ordered_actions)
        )
    return "\n".join(lines)


def render_table(rows: list[RankedCandidate], top_n: int) -> str:
    selected = rows[:top_n]
    header = (
        "| Rank | MONDO ID | Disease | Drug rows | Medium/high evidence rows | "
        "ClinGen D/S (desc) | Action | Priority rationale |\n"
        "| --- | --- | --- | ---: | ---: | --- | --- | --- |\n"
    )
    body_lines = []
    for rank, row in enumerate(selected, start=1):
        body_lines.append(
            "| "
            + " | ".join(
                [
                    str(rank),
                    row.mondo_id,
                    row.label,
                    str(row.drug_indication_count),
                    str(row.medium_high_evidence_count),
                    f"{row.clingen_definitive_count}/{row.clingen_strong_count}",
                    row.recommended_action,
                    row.rationale,
                ]
            )
            + " |"
        )
    return header + "\n".join(body_lines)


def render_methodology(source_path: Path, missing_count: int, top_n: int) -> str:
    lines = [
        "- Parsed the downloaded Monarch YAML at "
        f"`{source_path}` and used the top-level `diseases` list.",
        "- Treated a disease as having drug-indication data when it contained at least one "
        "non-empty `research[].drug_label` block.",
        "- Counted `Drug rows` as the number of such `drug_label` blocks; counted "
        "`Medium/high evidence rows` from nested evidence objects where `confidence_drug` "
        "was `MEDIUM` or `HIGH`.",
        "- Considered a disease already covered only when an existing "
        "`kb/disorders/*.yaml` file had the same `disease_term.term.id` MONDO CURIE.",
        "- Reused the repo's `dismech.compare.mondo_priority` heuristics to label each "
        "missing disease as `CURATE_ROOT`, `CURATE_ROOT_WITH_SUBTYPES`, or a lower-fit "
        "series/review case based on MONDO hierarchy metadata from the local sqlite DB.",
        "- Loaded ClinGen support from cached `cache/clingen/gene_validity.csv` and counted "
        "Definitive/Strong assertions on the candidate MONDO term or its descendants, which "
        "reduces false negatives for broad disease roots.",
        "- Final rank = quantitative score (specificity + drug-signal density + treatment rank "
        "+ descendant-aware ClinGen support) plus a transparent curator-fit adjustment. "
        "Those manual adjustments mainly downgraded broad, heterogeneous, or awkwardly granular "
        "terms whose drug lists were dominated by symptomatic/general therapy rather than a clear "
        "disease-mechanism target.",
    ]
    if missing_count <= top_n:
        lines.append(
            f"- Only **{missing_count}** missing diseases met the inclusion rule, so the "
            f"requested Top {top_n} table contains all available uncurated candidates."
        )
    else:
        lines.append(
            f"- **{missing_count}** missing diseases met the inclusion rule; the table below "
            f"shows the Top {top_n} highest-priority uncurated candidates."
        )
    return "\n".join(lines)


def write_report(
    output_path: Path,
    source_path: Path,
    total_source_diseases: int,
    signal_count: int,
    ranked_rows: list[RankedCandidate],
    action_counts: dict[str, int],
    top_n: int,
) -> None:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    markdown = "\n".join(
        [
            "# Drug Indication Priority Analysis",
            "",
            f"Generated: {generated_at}",
            "",
            "## Summary Stats",
            "",
            render_summary_stats(
                total_source_diseases=total_source_diseases,
                signal_count=signal_count,
                missing_count=len(ranked_rows),
                action_counts=action_counts,
            ),
            "",
            f"## Top {top_n} Prioritized Candidates",
            "",
            render_table(ranked_rows, top_n=top_n),
            "",
            "## Methodology Notes",
            "",
            render_methodology(
                source_path,
                missing_count=len(ranked_rows),
                top_n=top_n,
            ),
            "",
        ]
    )
    output_path.write_text(markdown, encoding="utf-8")


def main() -> None:
    args = parse_args()
    diseases = load_source_diseases(args.source)
    signals = extract_drug_signals(diseases)
    ranked_rows, action_counts = build_ranked_candidates(
        signals=signals,
        kb_dir=args.kb_dir,
        mondo_db=args.mondo_db,
        clingen_csv=args.clingen_csv,
        config_path=args.config,
    )
    write_report(
        output_path=args.output,
        source_path=args.source,
        total_source_diseases=len(diseases),
        signal_count=len(signals),
        ranked_rows=ranked_rows,
        action_counts=action_counts,
        top_n=args.top_n,
    )


if __name__ == "__main__":
    main()
