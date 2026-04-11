"""Prioritize MONDO disease candidates for dismech curation."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import typer
import yaml

from .support import default_kb_dir
from .support import get_disease_term_id
from .support import iter_disease_files
from .support import load_yaml_object

app = typer.Typer(
    name="dismech-mondo-prioritize",
    help="Score MONDO disease candidates for dismech curation.",
)

_FIELD_ALIASES = {
    "mondo_id": ["mondo_id", "id", "term_id", "disease_mondo"],
    "label": ["label", "name", "term_label", "disease_name"],
    "definition": ["definition", "def", "description"],
    "synonyms": ["synonyms", "exact_synonyms", "related_synonyms"],
    "parents": ["parents", "parent_labels", "direct_parents"],
    "xrefs": ["xrefs", "mappings", "exact_mappings"],
    "child_count": ["child_count", "children", "direct_child_count"],
    "is_obsolete": ["is_obsolete", "obsolete", "deprecated"],
    "clingen_definitive_count": [
        "clingen_definitive_count",
        "definitive_gene_count",
    ],
    "clingen_strong_count": ["clingen_strong_count", "strong_gene_count"],
    "subset_match_count": ["subset_match_count", "priority_subset_count"],
    "orphanet_match_count": ["orphanet_match_count", "orphanet_count"],
}

_DEFAULT_CONFIG_PATH = (
    Path(__file__).resolve().parents[3] / "conf" / "mondo_prioritizer.yaml"
)
_TRUE_VALUES = {"1", "true", "t", "yes", "y"}
_CONJUNCTION_PATTERN = re.compile(r"\b(with|and|or)\b", re.IGNORECASE)


@dataclass
class CandidateTerm:
    """MONDO candidate row with normalized fields."""

    mondo_id: str
    label: str
    definition: str = ""
    synonyms: list[str] = field(default_factory=list)
    parents: list[str] = field(default_factory=list)
    xrefs: list[str] = field(default_factory=list)
    child_count: int = 0
    is_obsolete: bool = False
    clingen_definitive_count: int = 0
    clingen_strong_count: int = 0
    subset_match_count: int = 0
    orphanet_match_count: int = 0
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class CoverageIndex:
    """Local dismech coverage keyed by MONDO and label."""

    curated_ids: set[str]
    curated_labels: set[str]
    label_to_file: dict[str, str]
    id_to_file: dict[str, str]


@dataclass
class ScoredCandidate:
    """Candidate score with supporting explanations."""

    mondo_id: str
    label: str
    score: float
    recommended_action: str
    specificity_bucket: str
    curated_match: str | None
    family_stem: str | None
    family_size: int
    reasons: list[str]
    raw: dict[str, Any]


def _normalize_text(text: str | None) -> str:
    if not text:
        return ""
    normalized = text.casefold().replace("_", " ")
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return " ".join(normalized.split())


def _split_multi_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    if not text:
        return []
    if "|" in text:
        parts = text.split("|")
    elif ";" in text:
        parts = text.split(";")
    else:
        parts = [text]
    return [part.strip() for part in parts if part.strip()]


def _parse_int(value: Any) -> int:
    if value in (None, ""):
        return 0
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    text = str(value).strip()
    if not text:
        return 0
    try:
        return int(float(text))
    except ValueError:
        return 0


def _parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return False
    return str(value).strip().casefold() in _TRUE_VALUES


def _get_first(row: dict[str, Any], aliases: list[str], default: Any = "") -> Any:
    for alias in aliases:
        if alias in row and row[alias] not in (None, ""):
            return row[alias]
    return default


def _sniff_delimiter(path: Path) -> str:
    if path.suffix == ".tsv":
        return "\t"
    sample = path.read_text(encoding="utf-8")[:2048]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t")
    except csv.Error:
        return ","
    return dialect.delimiter


def _load_rows(path: Path) -> list[dict[str, Any]]:
    if path.suffix == ".jsonl":
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    if path.suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            raise ValueError(f"Expected a JSON list in {path}")
        return [dict(item) for item in payload]

    delimiter = _sniff_delimiter(path)
    with path.open(encoding="utf-8", newline="") as stream:
        return [dict(row) for row in csv.DictReader(stream, delimiter=delimiter)]


def load_candidates(path: Path) -> list[CandidateTerm]:
    """Load candidate rows from TSV, CSV, JSON, or JSONL."""
    candidates: list[CandidateTerm] = []
    for row in _load_rows(path):
        mondo_id = str(_get_first(row, _FIELD_ALIASES["mondo_id"])).strip()
        label = str(_get_first(row, _FIELD_ALIASES["label"])).strip()
        if not mondo_id or not label:
            raise ValueError(
                f"Candidate rows must include MONDO id and label. Offending row: {row}"
            )
        candidates.append(
            CandidateTerm(
                mondo_id=mondo_id,
                label=label,
                definition=str(
                    _get_first(row, _FIELD_ALIASES["definition"], default="")
                ).strip(),
                synonyms=_split_multi_value(
                    _get_first(row, _FIELD_ALIASES["synonyms"])
                ),
                parents=_split_multi_value(_get_first(row, _FIELD_ALIASES["parents"])),
                xrefs=_split_multi_value(_get_first(row, _FIELD_ALIASES["xrefs"])),
                child_count=_parse_int(_get_first(row, _FIELD_ALIASES["child_count"])),
                is_obsolete=_parse_bool(
                    _get_first(row, _FIELD_ALIASES["is_obsolete"], default=False)
                ),
                clingen_definitive_count=_parse_int(
                    _get_first(row, _FIELD_ALIASES["clingen_definitive_count"])
                ),
                clingen_strong_count=_parse_int(
                    _get_first(row, _FIELD_ALIASES["clingen_strong_count"])
                ),
                subset_match_count=_parse_int(
                    _get_first(row, _FIELD_ALIASES["subset_match_count"])
                ),
                orphanet_match_count=_parse_int(
                    _get_first(row, _FIELD_ALIASES["orphanet_match_count"])
                ),
                raw=row,
            )
        )
    return candidates


def build_coverage_index(kb_dir: Path) -> CoverageIndex:
    """Index current dismech disease roots by MONDO and normalized label."""
    curated_ids: set[str] = set()
    curated_labels: set[str] = set()
    label_to_file: dict[str, str] = {}
    id_to_file: dict[str, str] = {}

    for path in iter_disease_files(kb_dir):
        data = load_yaml_object(path)
        disease_id = get_disease_term_id(data)
        if disease_id:
            curated_ids.add(disease_id)
            id_to_file[disease_id] = path.name

        labels = [
            _normalize_text(data.get("name")),
            _normalize_text(
                ((data.get("disease_term") or {}).get("term") or {}).get("label")
            ),
        ]
        for label in labels:
            if label:
                curated_labels.add(label)
                label_to_file.setdefault(label, path.name)

    return CoverageIndex(
        curated_ids=curated_ids,
        curated_labels=curated_labels,
        label_to_file=label_to_file,
        id_to_file=id_to_file,
    )


def load_config(path: Path | None = None) -> dict[str, Any]:
    """Load prioritizer config, defaulting to the repo config."""
    config_path = path or _DEFAULT_CONFIG_PATH
    payload = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Config at {config_path} must be a YAML object")
    return payload


def _extract_family_stem(label: str, subtype_series_patterns: list[str]) -> str | None:
    for pattern in subtype_series_patterns:
        match = re.match(pattern, label, flags=re.IGNORECASE)
        if match:
            stem = match.groupdict().get("stem")
            if stem:
                return stem.strip(" ,")
    return None


def _cap_count(count: int, cap: int) -> int:
    return min(max(count, 0), max(cap, 0))


def _grouping_term(label: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, label, flags=re.IGNORECASE) for pattern in patterns)


def _likely_over_specific_leaf(label: str, child_count: int, min_words: int) -> bool:
    if child_count != 0:
        return False
    if len(label.split()) < min_words:
        return False
    return len(_CONJUNCTION_PATTERN.findall(label)) >= 2


def _recommend_action(
    curated_match: str | None,
    is_obsolete: bool,
    grouping_term: bool,
    subtype_series: bool,
    broad_parent: bool,
    likely_over_specific_leaf: bool,
    parent_present: bool,
) -> tuple[str, str]:
    if curated_match:
        return "ALREADY_CURATED", "already_curated"
    if is_obsolete:
        return "DROP_OBSOLETE", "obsolete"
    if grouping_term:
        return "DROP_GROUPING_TERM", "grouping_term"
    if subtype_series and parent_present:
        return "LUMP_INTO_PARENT", "subtype_series"
    if subtype_series:
        return "REVIEW_SERIES_FOR_PARENT_ROOT", "subtype_series"
    if broad_parent:
        return "CURATE_ROOT_WITH_SUBTYPES", "broad_parent"
    if likely_over_specific_leaf:
        return "REVIEW_AGAINST_PARENT", "over_specific_leaf"
    return "CURATE_ROOT", "root_candidate"


def score_candidates(
    candidates: list[CandidateTerm],
    coverage: CoverageIndex,
    config: dict[str, Any],
) -> list[ScoredCandidate]:
    """Apply weighted scoring and specificity heuristics."""
    weights = dict(config.get("weights") or {})
    caps = dict(config.get("caps") or {})
    thresholds = dict(config.get("thresholds") or {})
    heuristics = dict(config.get("heuristics") or {})

    subtype_series_patterns = list(heuristics.get("subtype_series_patterns") or [])
    grouping_patterns = list(heuristics.get("grouping_term_patterns") or [])

    family_by_label: dict[str, str] = {}
    family_sizes: dict[str, int] = {}
    known_labels = {
        _normalize_text(candidate.label): candidate.label for candidate in candidates
    }

    for candidate in candidates:
        stem = _extract_family_stem(candidate.label, subtype_series_patterns)
        if stem:
            normalized_stem = _normalize_text(stem)
            family_by_label[candidate.mondo_id] = stem
            family_sizes[normalized_stem] = family_sizes.get(normalized_stem, 0) + 1

    scored: list[ScoredCandidate] = []
    broad_parent_min_children = int(thresholds.get("broad_parent_min_children", 4))
    subtype_series_min_family_size = int(
        thresholds.get("subtype_series_min_family_size", 2)
    )
    over_specific_leaf_min_words = int(
        thresholds.get("over_specific_leaf_min_words", 8)
    )

    for candidate in candidates:
        normalized_label = _normalize_text(candidate.label)
        curated_match = None
        if candidate.mondo_id in coverage.curated_ids:
            curated_match = coverage.label_to_file.get(
                normalized_label
            ) or coverage.id_to_file.get(candidate.mondo_id)
        elif normalized_label in coverage.curated_labels:
            curated_match = coverage.label_to_file.get(normalized_label)

        family_stem = family_by_label.get(candidate.mondo_id)
        normalized_family_stem = _normalize_text(family_stem)
        family_size = family_sizes.get(normalized_family_stem, 0)
        subtype_series = bool(
            family_stem and family_size >= subtype_series_min_family_size
        )

        parent_present = False
        if family_stem:
            normalized_stem = _normalize_text(family_stem)
            parent_present = (
                normalized_stem in known_labels
                or normalized_stem in coverage.curated_labels
            )
        if not parent_present:
            parent_present = any(
                _normalize_text(parent) in coverage.curated_labels
                or _normalize_text(parent) in known_labels
                for parent in candidate.parents
            )

        grouping_term = _grouping_term(candidate.label, grouping_patterns)
        broad_parent = (
            candidate.child_count >= broad_parent_min_children
            and not subtype_series
            and not grouping_term
        )
        over_specific_leaf = _likely_over_specific_leaf(
            candidate.label,
            candidate.child_count,
            over_specific_leaf_min_words,
        )

        recommended_action, specificity_bucket = _recommend_action(
            curated_match=curated_match,
            is_obsolete=candidate.is_obsolete,
            grouping_term=grouping_term,
            subtype_series=subtype_series,
            broad_parent=broad_parent,
            likely_over_specific_leaf=over_specific_leaf,
            parent_present=parent_present,
        )

        score = 0.0
        reasons: list[str] = []

        if not curated_match:
            value = float(weights.get("missing_from_dismech", 0))
            score += value
            if value:
                reasons.append(f"+{value:g} missing from dismech root coverage")

        if candidate.definition:
            value = float(weights.get("has_definition", 0))
            score += value
            if value:
                reasons.append(f"+{value:g} has MONDO definition")

        synonym_count = _cap_count(
            len(candidate.synonyms),
            int(caps.get("synonym_count", len(candidate.synonyms))),
        )
        synonym_weight = float(weights.get("synonym_count", 0))
        if synonym_count and synonym_weight:
            contribution = synonym_count * synonym_weight
            score += contribution
            reasons.append(
                f"+{contribution:g} synonym_count={synonym_count} x {synonym_weight:g}"
            )

        xref_count = _cap_count(
            len(candidate.xrefs), int(caps.get("xref_count", len(candidate.xrefs)))
        )
        xref_weight = float(weights.get("xref_count", 0))
        if xref_count and xref_weight:
            contribution = xref_count * xref_weight
            score += contribution
            reasons.append(
                f"+{contribution:g} xref_count={xref_count} x {xref_weight:g}"
            )

        for field_name in (
            "clingen_definitive_count",
            "clingen_strong_count",
            "subset_match_count",
            "orphanet_match_count",
        ):
            count = getattr(candidate, field_name)
            cap = int(caps.get(field_name, count))
            count = _cap_count(count, cap)
            weight = float(weights.get(field_name, 0))
            if count and weight:
                contribution = count * weight
                score += contribution
                reasons.append(f"+{contribution:g} {field_name}={count} x {weight:g}")

        for flag_name, active in (
            ("broad_parent_bonus", broad_parent),
            ("subtype_series_penalty", subtype_series),
            ("grouping_term_penalty", grouping_term),
            ("over_specific_leaf_penalty", over_specific_leaf),
            ("obsolete_penalty", candidate.is_obsolete),
            ("already_curated_penalty", curated_match is not None),
        ):
            value = float(weights.get(flag_name, 0))
            if active and value:
                score += value
                reasons.append(f"{value:g} {flag_name}")

        if subtype_series and family_stem:
            reasons.append(
                f"series stem '{family_stem}' observed across {family_size} candidates"
            )
        if broad_parent:
            reasons.append(
                f"child_count={candidate.child_count} exceeds broad parent threshold"
            )
        if grouping_term:
            reasons.append("label matched grouping-term regex")
        if over_specific_leaf:
            reasons.append("leaf label is long and conjunction-heavy")
        if curated_match:
            reasons.append(f"already curated in {curated_match}")

        scored.append(
            ScoredCandidate(
                mondo_id=candidate.mondo_id,
                label=candidate.label,
                score=round(score, 2),
                recommended_action=recommended_action,
                specificity_bucket=specificity_bucket,
                curated_match=curated_match,
                family_stem=family_stem,
                family_size=family_size,
                reasons=reasons,
                raw=candidate.raw,
            )
        )

    return sorted(scored, key=lambda item: (-item.score, item.label.casefold()))


def _render_table(results: list[ScoredCandidate], top: int | None = None) -> str:
    display = results[:top] if top else results
    header = (
        "score\tmondo_id\tlabel\trecommended_action\tspecificity_bucket\tcurated_match"
    )
    rows = [
        "\t".join(
            [
                f"{item.score:.2f}",
                item.mondo_id,
                item.label,
                item.recommended_action,
                item.specificity_bucket,
                item.curated_match or "",
            ]
        )
        for item in display
    ]
    return "\n".join([header, *rows])


def _write_output(
    results: list[ScoredCandidate],
    format: str,
    output: Path | None,
    top: int | None = None,
) -> None:
    stream = (
        output.open("w", encoding="utf-8")
        if output
        else typer.get_text_stream("stdout")
    )
    close_stream = output is not None
    try:
        selected = results[:top] if top else results
        if format == "table":
            stream.write(_render_table(selected))
            stream.write("\n")
        elif format == "json":
            json.dump(
                [
                    {
                        "mondo_id": item.mondo_id,
                        "label": item.label,
                        "score": item.score,
                        "recommended_action": item.recommended_action,
                        "specificity_bucket": item.specificity_bucket,
                        "curated_match": item.curated_match,
                        "family_stem": item.family_stem,
                        "family_size": item.family_size,
                        "reasons": item.reasons,
                    }
                    for item in selected
                ],
                stream,
                indent=2,
            )
            stream.write("\n")
        elif format == "tsv":
            writer = csv.DictWriter(
                stream,
                fieldnames=[
                    "score",
                    "mondo_id",
                    "label",
                    "recommended_action",
                    "specificity_bucket",
                    "curated_match",
                    "family_stem",
                    "family_size",
                    "reasons",
                ],
                delimiter="\t",
            )
            writer.writeheader()
            for item in selected:
                writer.writerow(
                    {
                        "score": f"{item.score:.2f}",
                        "mondo_id": item.mondo_id,
                        "label": item.label,
                        "recommended_action": item.recommended_action,
                        "specificity_bucket": item.specificity_bucket,
                        "curated_match": item.curated_match or "",
                        "family_stem": item.family_stem or "",
                        "family_size": item.family_size,
                        "reasons": " | ".join(item.reasons),
                    }
                )
        else:
            raise typer.BadParameter("format must be one of: table, json, tsv")
    finally:
        if close_stream:
            stream.close()


@app.command("score")
def score_command(
    candidates: Path = typer.Argument(
        ...,
        help="TSV/CSV/JSON/JSONL file of MONDO candidates.",
    ),
    kb_dir: Path = typer.Option(
        default_kb_dir(),
        "--kb-dir",
        help="Path to kb/disorders for local coverage checks.",
    ),
    config: Path = typer.Option(
        _DEFAULT_CONFIG_PATH,
        "--config",
        help="YAML config file with weights, caps, and heuristics.",
    ),
    format: str = typer.Option(
        "table",
        "--format",
        help="Output format: table, json, or tsv.",
    ),
    top: int | None = typer.Option(
        None,
        "--top",
        help="Optional number of top-scoring rows to emit.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        help="Optional output file path.",
    ),
) -> None:
    """Score MONDO candidates against dismech coverage and specificity heuristics."""
    candidate_rows = load_candidates(candidates)
    coverage = build_coverage_index(kb_dir)
    loaded_config = load_config(config)
    results = score_candidates(candidate_rows, coverage=coverage, config=loaded_config)
    _write_output(results, format=format, output=output, top=top)


def main() -> None:
    """Entrypoint for console_scripts."""
    app()


if __name__ == "__main__":
    main()
