"""Helpers for case-to-disease phenotype matching inputs."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Any

import yaml
from oaklib import get_adapter

_HP_ADAPTER_SPEC = "sqlite:obo:hp"
_FREQUENCY_PRIORITY = {
    "OBLIGATE": 5,
    "VERY_FREQUENT": 4,
    "FREQUENT": 3,
    "OCCASIONAL": 2,
    "VERY_RARE": 1,
}
_NO_EXPLANATION_ID = "NO_EXPLANATION"
_NO_EXPLANATION = {
    "explanation_id": _NO_EXPLANATION_ID,
    "estimated_probability": 0.0,
    "description": "No explanation assigned yet for this non-match.",
}


def _normalize_hp_id(term_id: str | None) -> str | None:
    """Normalize HPO identifiers to uppercase CURIE form."""
    if not term_id:
        return None
    tid = str(term_id).strip()
    if not tid or ":" not in tid:
        return None
    prefix, local = tid.split(":", 1)
    if prefix.casefold() != "hp":
        return None
    local = local.strip()
    if not local:
        return None
    return f"HP:{local}"


class _HPOIsARelationshipResolver:
    """Resolve strict is-a ancestry relationships using OAK and sqlite:obo:hp."""

    def __init__(self) -> None:
        self._adapter = None
        self._ancestor_cache: dict[str, set[str]] = {}

    def _get_adapter(self):
        if self._adapter is None:
            self._adapter = get_adapter(_HP_ADAPTER_SPEC)
        return self._adapter

    def ancestors(self, term_id: str) -> set[str]:
        """Return is-a ancestors (including self) for an HPO term ID."""
        normalized = _normalize_hp_id(term_id)
        if not normalized:
            return set()
        if normalized in self._ancestor_cache:
            return self._ancestor_cache[normalized]

        adapter = self._get_adapter()
        try:
            ancestors = {
                ancestor
                for ancestor in adapter.ancestors(
                    normalized,
                    predicates=["rdfs:subClassOf"],
                    reflexive=True,
                )
                if isinstance(ancestor, str)
            }
        except Exception:
            ancestors = set()

        self._ancestor_cache[normalized] = ancestors
        return ancestors

    def is_strict_descendant_of(self, child_id: str | None, ancestor_id: str | None) -> bool:
        """True iff child_id is a strict is-a descendant of ancestor_id."""
        child = _normalize_hp_id(child_id)
        ancestor = _normalize_hp_id(ancestor_id)
        if not child or not ancestor or child == ancestor:
            return False
        return ancestor in self.ancestors(child)


_HP_ISA = _HPOIsARelationshipResolver()


def _default_kb_dir() -> Path:
    """Return the default disorder directory."""
    return Path(__file__).resolve().parents[2] / "kb" / "disorders"


def _iter_disease_files(kb_dir: Path) -> list[Path]:
    """Return disorder YAML files, excluding history snapshots."""
    return sorted(path for path in kb_dir.glob("*.yaml") if not path.name.endswith(".history.yaml"))


def _normalize_for_lookup(value: str | None) -> str:
    """Normalize disease names/slugs for tolerant lookup."""
    if not value:
        return ""
    compact = value.casefold().replace("_", " ").replace("-", " ")
    return " ".join(compact.split())


def _disease_term_id(disease_model: dict[str, Any]) -> str | None:
    """Extract disease ontology ID from a disease model if present."""
    disease_term = disease_model.get("disease_term")
    if not isinstance(disease_term, dict):
        return None
    term = disease_term.get("term")
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    return str(term_id) if term_id else None


def resolve_disease_reference(
    disease_reference: str | Path,
    kb_dir: Path | None = None,
) -> tuple[str, Path]:
    """Resolve disease reference to (slug, path).

    Supported references:
    - Direct path to a disease YAML file.
    - DisMech slug (filename stem).
    - Disease ontology ID (e.g. MONDO:0018116).
    - Disease name (case-insensitive, tolerant for spaces/underscores/hyphens).
    """
    reference_text = str(disease_reference).strip()
    if not reference_text:
        raise ValueError("Disease reference must not be empty")

    ref_path = Path(reference_text)
    if ref_path.exists():
        path = ref_path.resolve()
        if not path.is_file():
            raise ValueError(f"Disease reference path is not a file: {path}")
        slug = path.stem
        if slug.endswith(".history"):
            slug = slug[: -len(".history")]
        return slug, path

    disorder_dir = kb_dir or _default_kb_dir()
    if not disorder_dir.exists():
        raise FileNotFoundError(f"Disorder directory does not exist: {disorder_dir}")

    literal_candidates = [
        reference_text,
        f"{reference_text}.yaml",
        reference_text.replace(" ", "_"),
        f"{reference_text.replace(' ', '_')}.yaml",
    ]
    for candidate in literal_candidates:
        candidate_path = disorder_dir / candidate
        if candidate_path.exists() and candidate_path.is_file():
            slug = candidate_path.stem
            if slug.endswith(".history"):
                slug = slug[: -len(".history")]
            return slug, candidate_path.resolve()

    disease_files = _iter_disease_files(disorder_dir)

    if ":" in reference_text:
        ref_upper = reference_text.upper()
        matches: list[Path] = []
        for disease_file in disease_files:
            disease_model = load_disease_model(disease_file.stem, kb_dir=disorder_dir)
            term_id = _disease_term_id(disease_model)
            if term_id and term_id.upper() == ref_upper:
                matches.append(disease_file)
        if len(matches) == 1:
            return matches[0].stem, matches[0].resolve()
        if len(matches) > 1:
            raise ValueError(
                f"Disease reference '{reference_text}' matched multiple disease files: "
                + ", ".join(path.name for path in matches)
            )

    normalized_ref = _normalize_for_lookup(reference_text)
    name_matches: list[Path] = []
    for disease_file in disease_files:
        disease_model = load_disease_model(disease_file.stem, kb_dir=disorder_dir)
        disease_name = disease_model.get("name")
        if _normalize_for_lookup(str(disease_name) if disease_name else "") == normalized_ref:
            name_matches.append(disease_file)
            continue
        if _normalize_for_lookup(disease_file.stem) == normalized_ref:
            name_matches.append(disease_file)

    if len(name_matches) == 1:
        return name_matches[0].stem, name_matches[0].resolve()
    if len(name_matches) > 1:
        raise ValueError(
            f"Disease reference '{reference_text}' is ambiguous; matches: "
            + ", ".join(path.name for path in name_matches)
        )

    raise FileNotFoundError(
        f"Could not resolve disease reference '{reference_text}' as a path, slug, id, or name in {disorder_dir}"
    )


def _resolve_disease_path(disease_slug: str, kb_dir: Path | None = None) -> Path:
    """Resolve a dismech disease slug to a YAML file path."""
    disorder_dir = kb_dir or _default_kb_dir()
    slug = re.sub(r"\.yaml$", "", disease_slug)
    candidate = disorder_dir / f"{slug}.yaml"
    if candidate.exists():
        return candidate.resolve()
    raise FileNotFoundError(f"Could not resolve disease slug '{disease_slug}' to {candidate}")


def load_disease_model(disease_slug: str, kb_dir: Path | None = None) -> dict[str, Any]:
    """Load a disease model YAML by dismech slug."""
    path = _resolve_disease_path(disease_slug, kb_dir=kb_dir)
    with open(path) as stream:
        data = yaml.safe_load(stream)
    if not isinstance(data, dict):
        raise ValueError(f"Disease YAML at {path} must be an object")
    return data


def _extract_model_phenotypes(disease_model: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract model phenotypes in a normalized shape for matching."""
    phenotype_entries = disease_model.get("phenotypes", [])
    if not isinstance(phenotype_entries, list):
        return []

    model_rows: list[dict[str, Any]] = []
    for item in phenotype_entries:
        if not isinstance(item, dict):
            continue

        term_desc = item.get("phenotype_term")
        term = None
        preferred_term = None
        if isinstance(term_desc, dict):
            preferred_term = term_desc.get("preferred_term")
            raw_term = term_desc.get("term")
            if isinstance(raw_term, dict):
                term = raw_term

        term_id = _normalize_hp_id(term.get("id") if isinstance(term, dict) else None)
        term_label = term.get("label") if isinstance(term, dict) else None
        name = item.get("name")

        label_candidates = [
            label
            for label in (term_label, preferred_term, name)
            if isinstance(label, str) and label.strip()
        ]
        if not label_candidates:
            continue

        model_rows.append(
            {
                "model_term_id": str(term_id) if term_id else None,
                "model_label": str(label_candidates[0]),
                "model_description": str(item.get("description")) if item.get("description") else None,
                "model_frequency": str(item.get("frequency")) if item.get("frequency") else None,
            }
        )

    return model_rows


def _select_best_model_row(case_row: dict[str, Any], model_rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Select best model phenotype row via strict ontology relation.

    Match precedence:
    1) exact term ID
    2) case is-a descendant of model term (case_is_narrower)
    3) case is-a ancestor of model term (case_is_broader)
    """
    if not model_rows:
        return None

    case_term_id = _normalize_hp_id(case_row.get("case_term_id"))
    best: dict[str, Any] | None = None
    best_rank: tuple[int, int] | None = None
    for model_row in model_rows:
        model_term_id = _normalize_hp_id(model_row.get("model_term_id"))
        if not model_term_id or not case_term_id:
            continue

        exact = case_term_id == model_term_id
        narrower = _HP_ISA.is_strict_descendant_of(case_term_id, model_term_id)
        broader = _HP_ISA.is_strict_descendant_of(model_term_id, case_term_id)
        relation_rank = 2 if exact else 1 if (narrower or broader) else 0
        if relation_rank == 0:
            continue

        frequency = str(model_row.get("model_frequency") or "")
        frequency_rank = _FREQUENCY_PRIORITY.get(frequency, 0)
        rank_tuple = (relation_rank, frequency_rank)
        if best_rank is not None and rank_tuple <= best_rank:
            continue

        similarity_percent = 100.0 if exact else 75.0
        best = {
            "model_term_id": model_term_id,
            "model_label": model_row.get("model_label"),
            "model_description": model_row.get("model_description"),
            "model_frequency": model_row.get("model_frequency"),
            "exact": exact,
            "case_is_broader": broader,
            "case_is_narrower": narrower,
            "case_is_close": False,
            "similarity_percent": similarity_percent,
        }
        best_rank = rank_tuple

    return best


def load_phenopacket(path: str | Path) -> dict[str, Any]:
    """Load a phenopacket JSON document from disk."""
    with open(path) as stream:
        data = json.load(stream)
    if not isinstance(data, dict):
        raise ValueError(f"Phenopacket JSON at {path} must be an object")
    return data


def extract_case_phenotypes_from_phenopacket(phenopacket: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract case phenotype terms from a GA4GH phenopacket.

    Phenotypic features with ``excluded: true`` are converted to ``case_present: false``.
    """
    features = phenopacket.get("phenotypicFeatures", [])
    if not isinstance(features, list):
        return []

    rows: list[dict[str, Any]] = []
    for feature in features:
        if not isinstance(feature, dict):
            continue
        term = feature.get("type")
        if not isinstance(term, dict):
            continue

        term_id = _normalize_hp_id(term.get("id"))
        if not term_id:
            continue

        term_label = term.get("label")
        row = {
            "case_term_id": term_id,
            "case_present": not bool(feature.get("excluded", False)),
        }
        if term_label not in (None, ""):
            row["case_label"] = str(term_label)
        feature_description = feature.get("description")
        if isinstance(feature_description, str) and feature_description.strip():
            row["case_description"] = feature_description
        rows.append(row)

    return rows


def _default_explanations() -> list[dict[str, Any]]:
    """Return default shared explanations included in every matching run."""
    return [dict(_NO_EXPLANATION)]


def _no_match_fields() -> dict[str, Any]:
    """Return standard fields for no-match rows on either side."""
    return {
        "exact": False,
        "case_is_broader": False,
        "case_is_narrower": False,
        "case_is_close": False,
        "explanation_for_no_match": _NO_EXPLANATION_ID,
    }


def calculate_pr_is_diagnosis(matching_run: dict[str, Any]) -> float:
    """Calculate diagnosis probability as the product of unique explanation probabilities.

    Only explanations referenced by ``explanation_for_no_match`` are included, and each
    explanation ID contributes at most once even if reused across many rows.
    """
    explanations = matching_run.get("explanations", [])
    explanation_pr_by_id: dict[str, float] = {}
    if isinstance(explanations, list):
        for explanation in explanations:
            if not isinstance(explanation, dict):
                continue
            explanation_id = explanation.get("explanation_id")
            if not explanation_id:
                continue
            try:
                explanation_pr_by_id[str(explanation_id)] = float(explanation.get("estimated_probability", 0.0))
            except (TypeError, ValueError):
                explanation_pr_by_id[str(explanation_id)] = 0.0

    pr_is_diagnosis = 1.0
    matches = matching_run.get("matches", [])
    if not isinstance(matches, list):
        return pr_is_diagnosis
    used_explanation_ids: set[str] = set()
    for match in matches:
        if not isinstance(match, dict):
            continue
        explanation_id = match.get("explanation_for_no_match")
        if not explanation_id:
            continue
        used_explanation_ids.add(str(explanation_id))

    for explanation_id in used_explanation_ids:
        pr_is_diagnosis *= explanation_pr_by_id.get(explanation_id, 0.0)

    return pr_is_diagnosis


def build_unmatched_run_from_phenopacket(
    phenopacket: dict[str, Any],
    disease_slug: str,
    *,
    run_id: str | None = None,
    case_id: str | None = None,
) -> dict[str, Any]:
    """Build a minimal MatchingRun from phenopacket features.

    This creates deterministic placeholder rows with model-side fields unset.
    It is intended for testing and pipeline bootstrapping before model matching is added.
    """
    extracted = extract_case_phenotypes_from_phenopacket(phenopacket)
    matches: list[dict[str, Any]] = []
    for row in extracted:
        matches.append(
            {
                **row,
                **_no_match_fields(),
            }
        )

    phenopacket_id = phenopacket.get("id")
    if case_id is None:
        case_id = str(phenopacket_id) if phenopacket_id else "unknown_case"
    if run_id is None:
        run_id = f"run-{case_id}"

    run = {
        "run_id": run_id,
        "case_id": case_id,
        "disease_slug": disease_slug,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "explanations": _default_explanations(),
        "matches": matches,
    }
    run["pr_is_diagnosis"] = calculate_pr_is_diagnosis(run)
    return run


def build_matching_run_from_phenopacket(
    phenopacket: dict[str, Any],
    disease_slug: str,
    *,
    run_id: str | None = None,
    case_id: str | None = None,
    kb_dir: Path | None = None,
) -> dict[str, Any]:
    """Build a MatchingRun by linking case phenotypes to a disease model."""
    disease_model = load_disease_model(disease_slug, kb_dir=kb_dir)
    model_rows = _extract_model_phenotypes(disease_model)
    case_rows = extract_case_phenotypes_from_phenopacket(phenopacket)

    matches: list[dict[str, Any]] = []
    matched_model_term_ids: set[str] = set()
    for case_row in case_rows:
        matched = _select_best_model_row(case_row, model_rows)
        if matched is None:
            matches.append(
                {
                    **case_row,
                    **_no_match_fields(),
                }
            )
            continue

        model_term_id = _normalize_hp_id(matched.get("model_term_id"))
        if model_term_id:
            matched_model_term_ids.add(model_term_id)
        row = {**case_row, **matched}
        # Any non-exact relation is still a mismatch that needs explanation.
        if row.get("exact") is False:
            row["explanation_for_no_match"] = _NO_EXPLANATION_ID
        matches.append(row)

    # Add model-only rows for disease phenotypes that were not matched by any case row.
    # This is the converse of an unmatched case row (case fields omitted).
    seen_unmatched_model_ids: set[str] = set()
    for model_row in model_rows:
        model_term_id = _normalize_hp_id(model_row.get("model_term_id"))
        if (
            not model_term_id
            or model_term_id in matched_model_term_ids
            or model_term_id in seen_unmatched_model_ids
        ):
            continue
        matches.append(
            {
                "model_term_id": model_term_id,
                "model_label": model_row.get("model_label"),
                "model_description": model_row.get("model_description"),
                "model_frequency": model_row.get("model_frequency"),
                **_no_match_fields(),
            }
        )
        seen_unmatched_model_ids.add(model_term_id)

    phenopacket_id = phenopacket.get("id")
    if case_id is None:
        case_id = str(phenopacket_id) if phenopacket_id else "unknown_case"
    if run_id is None:
        run_id = f"run-{case_id}"

    run = {
        "run_id": run_id,
        "case_id": case_id,
        "disease_slug": disease_slug,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "explanations": _default_explanations(),
        "matches": matches,
    }
    run["pr_is_diagnosis"] = calculate_pr_is_diagnosis(run)
    return run
