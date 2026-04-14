"""Schema-aware extraction of disease claims into flat evidence rows."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from linkml_runtime.utils.schemaview import SchemaView

from dismech.claims.models import ClaimRow
from dismech.compare.support import get_disease_term_id
from dismech.compare.support import iter_disease_files
from dismech.compare.support import load_yaml_object

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "dismech.yaml"

_STRUCTURAL_SLOT_NAMES = {
    "name",
    "description",
    "conforms_to",
    "consequence",
    "evidence",
    "notes",
    "review_notes",
    "role",
    "examples",
    "synonyms",
    "findings",
    "supporting_text",
    "reference",
    "reference_title",
    "statement",
    "title",
    "url",
    "tracked_issues",
    "pdb_structures",
    "curation_history",
}
_CLAIM_TEXT_FALLBACK_FIELDS = (
    "name",
    "statement",
    "title",
    "description",
)
_GENERIC_OBJECT_FALLBACK_FIELDS = (
    "name",
    "statement",
    "title",
    "description",
    "phase",
    "status",
    "percentage",
    "population",
    "accession",
    "external_id",
)
_HUMANIZED_CLAIM_TYPE_OVERRIDES = {
    "histopathology": "histopathology finding",
}
_PHENOTYPE_CONTEXT_DIRECT_CLAIM_SLOTS = {
    "frequency",
    "severity",
    "onset",
}


@lru_cache(maxsize=4)
def _schema_view(schema_path: str = str(SCHEMA_PATH)) -> SchemaView:
    return SchemaView(schema_path)


def extract_claim_rows(
    disease_data: dict[str, Any],
    *,
    schema_view: SchemaView | None = None,
) -> list[ClaimRow]:
    """Extract flat claim/evidence rows from a disease object."""
    schema = schema_view or _schema_view()
    disease_name = str(disease_data.get("name") or "")
    disease_id = get_disease_term_id(disease_data) or ""

    rows: list[ClaimRow] = []
    for top_slot in _iter_disease_claim_slots(schema):
        raw_items = disease_data.get(top_slot.name)
        if raw_items is None:
            continue
        items = raw_items if isinstance(raw_items, list) else [raw_items]
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            rows.extend(
                _extract_rows_for_item(
                    disease_name=disease_name,
                    disease_id=disease_id,
                    claim_slot=top_slot.name,
                    claim_class=top_slot.range,
                    item=item,
                    item_index=index,
                    schema=schema,
                )
            )
    return rows


def extract_claim_rows_from_file(
    path: str | Path,
    *,
    schema_view: SchemaView | None = None,
) -> list[ClaimRow]:
    """Load a disease YAML file and extract claim rows."""
    return extract_claim_rows(load_yaml_object(Path(path)), schema_view=schema_view)


def extract_claim_rows_from_files(
    paths: list[Path],
    *,
    schema_view: SchemaView | None = None,
) -> list[ClaimRow]:
    """Extract claim rows from multiple disease YAML files."""
    schema = schema_view or _schema_view()
    rows: list[ClaimRow] = []
    for path in paths:
        rows.extend(extract_claim_rows_from_file(path, schema_view=schema))
    return rows


def default_claim_input_paths(kb_dir: Path) -> list[Path]:
    """Return the default set of disorder YAML files for bulk extraction."""
    return iter_disease_files(kb_dir)


def _extract_rows_for_item(
    *,
    disease_name: str,
    disease_id: str,
    claim_slot: str,
    claim_class: str,
    item: dict[str, Any],
    item_index: int,
    schema: SchemaView,
) -> list[ClaimRow]:
    source_path = f"{claim_slot}[{item_index}]"
    claim_type = _singularize_claim_type(claim_slot)
    predicate_label = f"has {_humanize_claim_type(claim_type)}"
    object_slot_name = _primary_object_slot_name(claim_class, schema)
    object_label, object_id = _resolve_primary_object(
        item=item,
        claim_class=claim_class,
        object_slot_name=object_slot_name,
        schema=schema,
    )
    claim_object_text = _claim_object_text(item, object_label)
    evidence_items = _evidence_items(item.get("evidence"))
    context_rows, context_backed_direct_slots = _extract_context_rows(
        disease_name=disease_name,
        disease_id=disease_id,
        claim_slot=claim_slot,
        claim_class=claim_class,
        item=item,
        item_index=item_index,
        predicate_label=predicate_label,
        object_label=object_label,
        object_id=object_id,
        claim_object_text=claim_object_text,
        schema=schema,
    )

    rows = _flatten_claim_rows(
        disease_name=disease_name,
        disease_id=disease_id,
        claim_type=claim_type,
        claim_class=claim_class,
        source_path=source_path,
        claim_text=_build_claim_text(
            disease_name=disease_name,
            predicate_label=predicate_label,
            object_text=claim_object_text,
        ),
        predicate_label=predicate_label,
        predicate_id=claim_slot,
        object_label=object_label,
        object_id=object_id,
        evidence_items=evidence_items,
        primary_qualifier=None,
        all_qualifiers=None,
        qualifier_evidence_missing=False,
    )

    for qualifier_slot in _iter_direct_qualifier_slots(
        claim_class=claim_class,
        object_slot_name=object_slot_name,
        schema=schema,
    ):
        if qualifier_slot.name in context_backed_direct_slots:
            continue
        raw_value = item.get(qualifier_slot.name)
        if raw_value in (None, "", [], {}):
            continue
        qualifier = _build_qualifier(
            slot_name=qualifier_slot.name,
            raw_value=raw_value,
            induced_range=qualifier_slot.range,
            schema=schema,
        )
        rows.extend(
            _flatten_claim_rows(
                disease_name=disease_name,
                disease_id=disease_id,
                claim_type=claim_type,
                claim_class=claim_class,
                source_path=source_path,
                claim_text=_build_claim_text(
                    disease_name=disease_name,
                    predicate_label=predicate_label,
                    object_text=claim_object_text,
                    qualifiers=[qualifier],
                ),
                predicate_label=predicate_label,
                predicate_id=claim_slot,
                object_label=object_label,
                object_id=object_id,
                evidence_items=evidence_items,
                primary_qualifier=qualifier,
                all_qualifiers=[qualifier],
                qualifier_evidence_missing=True,
            )
        )
    rows.extend(context_rows)
    return rows


def _flatten_claim_rows(
    *,
    disease_name: str,
    disease_id: str,
    claim_type: str,
    claim_class: str,
    source_path: str,
    claim_text: str,
    predicate_label: str,
    predicate_id: str,
    object_label: str,
    object_id: str,
    evidence_items: list[dict[str, Any]],
    primary_qualifier: dict[str, str] | None,
    all_qualifiers: list[dict[str, str]] | None,
    qualifier_evidence_missing: bool,
) -> list[ClaimRow]:
    qualifiers = all_qualifiers or ([primary_qualifier] if primary_qualifier else [])
    if primary_qualifier:
        qualifier_name = primary_qualifier["name"]
        qualifier_value = primary_qualifier["value"]
        qualifier_value_id = primary_qualifier["value_id"]
        qualifiers_json = json.dumps(
            {
                qualifier["name"]: {
                    "value": qualifier["value"],
                    "id": qualifier["value_id"],
                }
                for qualifier in qualifiers
            },
            sort_keys=True,
        )
    else:
        qualifier_name = ""
        qualifier_value = ""
        qualifier_value_id = ""
        qualifiers_json = ""

    rows: list[ClaimRow] = []
    for evidence in evidence_items or [{}]:
        rows.append(
            ClaimRow(
                disease_name=disease_name,
                disease_id=disease_id,
                claim_type=claim_type,
                claim_class=claim_class,
                source_path=source_path,
                claim_kind="qualified" if primary_qualifier else "base",
                claim_text=claim_text,
                subject_label=disease_name,
                subject_id=disease_id,
                predicate_label=predicate_label,
                predicate_id=predicate_id,
                object_label=object_label,
                object_id=object_id,
                qualifier_name=qualifier_name,
                qualifier_value=qualifier_value,
                qualifier_value_id=qualifier_value_id,
                qualifiers_json=qualifiers_json,
                is_subclaim=bool(primary_qualifier),
                qualifier_evidence_missing=qualifier_evidence_missing,
                evidence_reference=str(evidence.get("reference") or ""),
                evidence_reference_title=str(evidence.get("reference_title") or ""),
                evidence_supports=str(evidence.get("supports") or ""),
                evidence_source=str(evidence.get("evidence_source") or ""),
                evidence_snippet=str(evidence.get("snippet") or ""),
                evidence_explanation=str(evidence.get("explanation") or ""),
            )
        )
    return rows


def _extract_context_rows(
    *,
    disease_name: str,
    disease_id: str,
    claim_slot: str,
    claim_class: str,
    item: dict[str, Any],
    item_index: int,
    predicate_label: str,
    object_label: str,
    object_id: str,
    claim_object_text: str,
    schema: SchemaView,
) -> tuple[list[ClaimRow], set[str]]:
    if claim_class != "Phenotype":
        return [], set()

    rows: list[ClaimRow] = []
    context_backed_direct_slots: set[str] = set()
    contexts = item.get("phenotype_contexts") or []
    if not isinstance(contexts, list):
        return rows, context_backed_direct_slots

    for context_index, context in enumerate(contexts):
        if not isinstance(context, dict):
            continue
        qualifiers = _context_qualifiers(context, schema)
        if not qualifiers:
            continue

        if _context_supplies_default_claim_evidence(qualifiers) and _evidence_items(
            context.get("evidence")
        ):
            context_backed_direct_slots.update(
                qualifier["name"]
                for qualifier in qualifiers
                if qualifier["name"] in _PHENOTYPE_CONTEXT_DIRECT_CLAIM_SLOTS
            )

        context_source_path = (
            f"{claim_slot}[{item_index}].phenotype_contexts[{context_index}]"
        )
        evidence_items = _evidence_items(context.get("evidence"))
        for primary_qualifier in qualifiers:
            ordered_qualifiers = _ordered_qualifiers(primary_qualifier, qualifiers)
            rows.extend(
                _flatten_claim_rows(
                    disease_name=disease_name,
                    disease_id=disease_id,
                    claim_type=_singularize_claim_type(claim_slot),
                    claim_class="PhenotypeContext",
                    source_path=context_source_path,
                    claim_text=_build_claim_text(
                        disease_name=disease_name,
                        predicate_label=predicate_label,
                        object_text=claim_object_text,
                        qualifiers=ordered_qualifiers,
                    ),
                    predicate_label=predicate_label,
                    predicate_id=claim_slot,
                    object_label=object_label,
                    object_id=object_id,
                    evidence_items=evidence_items,
                    primary_qualifier=primary_qualifier,
                    all_qualifiers=ordered_qualifiers,
                    qualifier_evidence_missing=not bool(evidence_items),
                )
            )
    return rows, context_backed_direct_slots


def _context_qualifiers(
    context: dict[str, Any], schema: SchemaView
) -> list[dict[str, str]]:
    qualifiers: list[dict[str, str]] = []
    for slot in schema.class_induced_slots("PhenotypeContext"):
        if slot.name in _STRUCTURAL_SLOT_NAMES:
            continue
        raw_value = context.get(slot.name)
        if raw_value in (None, "", [], {}):
            continue
        qualifiers.append(
            _build_qualifier(
                slot_name=slot.name,
                raw_value=raw_value,
                induced_range=slot.range,
                schema=schema,
            )
        )
    return qualifiers


def _context_supplies_default_claim_evidence(qualifiers: list[dict[str, str]]) -> bool:
    return all(
        qualifier["name"] in _PHENOTYPE_CONTEXT_DIRECT_CLAIM_SLOTS
        for qualifier in qualifiers
    )


def _ordered_qualifiers(
    primary_qualifier: dict[str, str], qualifiers: list[dict[str, str]]
) -> list[dict[str, str]]:
    return [primary_qualifier] + [
        qualifier for qualifier in qualifiers if qualifier is not primary_qualifier
    ]


def _iter_disease_claim_slots(schema: SchemaView):
    for slot in schema.class_induced_slots("Disease"):
        if not schema.get_class(slot.range):
            continue
        item_slot_names = {
            item_slot.name for item_slot in schema.class_induced_slots(slot.range)
        }
        if "evidence" not in item_slot_names:
            continue
        yield slot


def _iter_direct_qualifier_slots(
    *,
    claim_class: str,
    object_slot_name: str | None,
    schema: SchemaView,
):
    for slot in schema.class_induced_slots(claim_class):
        if slot.multivalued:
            continue
        if slot.name in _STRUCTURAL_SLOT_NAMES:
            continue
        if object_slot_name and slot.name == object_slot_name:
            continue
        if slot.name.endswith("_term"):
            continue
        if _range_is_descriptor(slot.range, schema):
            continue
        if _range_is_claim_like(slot.range, schema):
            continue
        yield slot


def _primary_object_slot_name(claim_class: str, schema: SchemaView) -> str | None:
    for slot in schema.class_induced_slots(claim_class):
        if slot.multivalued:
            continue
        if _range_is_descriptor(slot.range, schema):
            return slot.name
    return None


def _resolve_primary_object(
    *,
    item: dict[str, Any],
    claim_class: str,
    object_slot_name: str | None,
    schema: SchemaView,
) -> tuple[str, str]:
    if object_slot_name:
        text, identifier = _resolve_value(
            item.get(object_slot_name),
            slot_name=object_slot_name,
            induced_range=schema.induced_slot(object_slot_name, claim_class).range,
            schema=schema,
        )
        if text or identifier:
            return text, identifier

    for field_name in _GENERIC_OBJECT_FALLBACK_FIELDS:
        value = item.get(field_name)
        if value not in (None, "", [], {}):
            text, identifier = _resolve_value(
                value,
                slot_name=field_name,
                induced_range=None,
                schema=schema,
            )
            if text or identifier:
                return text, identifier

    for slot in schema.class_induced_slots(claim_class):
        if slot.multivalued or slot.name in _STRUCTURAL_SLOT_NAMES:
            continue
        if _range_is_claim_like(slot.range, schema):
            continue
        value = item.get(slot.name)
        if value in (None, "", [], {}):
            continue
        text, identifier = _resolve_value(
            value,
            slot_name=slot.name,
            induced_range=slot.range,
            schema=schema,
        )
        if text or identifier:
            return text, identifier

    return _humanize_claim_type(claim_class), ""


def _claim_object_text(item: dict[str, Any], object_label: str) -> str:
    for field_name in _CLAIM_TEXT_FALLBACK_FIELDS:
        value = item.get(field_name)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return object_label


def _build_claim_text(
    *,
    disease_name: str,
    predicate_label: str,
    object_text: str,
    qualifiers: list[dict[str, str]] | None = None,
) -> str:
    parts = [disease_name.strip(), predicate_label.strip(), object_text.strip()]
    claim_text = " ".join(part for part in parts if part)
    if qualifiers:
        qualifier_phrase = " and ".join(
            f"{_humanize_slot_name(qualifier['name'])} {qualifier['value_text']}"
            for qualifier in qualifiers
        )
        claim_text = f"{claim_text} with {qualifier_phrase}"
    return " ".join(claim_text.split())


def _build_qualifier(
    *,
    slot_name: str,
    raw_value: Any,
    induced_range: str | None,
    schema: SchemaView,
) -> dict[str, str]:
    value, value_id = _resolve_value(
        raw_value,
        slot_name=slot_name,
        induced_range=induced_range,
        schema=schema,
    )
    value_text = value.casefold() if isinstance(value, str) else str(value)
    return {
        "name": slot_name,
        "value": value,
        "value_id": value_id,
        "value_text": value_text,
    }


def _resolve_value(
    value: Any,
    *,
    slot_name: str,
    induced_range: str | None,
    schema: SchemaView,
) -> tuple[str, str]:
    if value in (None, ""):
        return "", ""

    if isinstance(value, dict):
        term = value.get("term")
        if isinstance(term, dict):
            label = (
                value.get("preferred_term")
                or term.get("label")
                or value.get("name")
                or value.get("description")
            )
            return str(label or ""), str(term.get("id") or "")
        if "label" in value or "id" in value:
            return (
                str(value.get("label") or value.get("id") or ""),
                str(value.get("id") or ""),
            )
        for text_key in ("description", "name", "title"):
            text_value = value.get(text_key)
            if isinstance(text_value, str) and text_value.strip():
                return text_value.strip(), ""
        parts: list[str] = []
        for key, child in value.items():
            if key in _STRUCTURAL_SLOT_NAMES or child in (None, "", [], {}):
                continue
            child_text, _ = _resolve_value(
                child,
                slot_name=key,
                induced_range=None,
                schema=schema,
            )
            if child_text:
                parts.append(f"{_humanize_slot_name(key)}={child_text}")
        return "; ".join(parts), ""

    if isinstance(value, list):
        parts = [
            _resolve_value(
                item,
                slot_name=slot_name,
                induced_range=induced_range,
                schema=schema,
            )[0]
            for item in value
        ]
        return "; ".join(part for part in parts if part), ""

    enum_value, enum_identifier = _resolve_enum_value(
        slot_name=slot_name,
        raw_value=str(value),
        induced_range=induced_range,
        schema=schema,
    )
    if enum_value:
        return enum_value, enum_identifier

    if isinstance(value, bool):
        return str(value).lower(), ""
    return str(value), ""


def _resolve_enum_value(
    *,
    slot_name: str,
    raw_value: str,
    induced_range: str | None,
    schema: SchemaView,
) -> tuple[str, str]:
    candidate_ranges = []
    if induced_range:
        candidate_ranges.append(induced_range)

    base_slot = schema.get_slot(slot_name)
    if base_slot is not None:
        slot_range = getattr(base_slot, "range", None)
        if slot_range:
            candidate_ranges.append(slot_range)
        for expression in getattr(base_slot, "any_of", []) or []:
            range_name = getattr(expression, "range", None)
            if range_name:
                candidate_ranges.append(range_name)

    normalized_candidates = []
    seen_ranges: set[str] = set()
    for range_name in candidate_ranges:
        if not range_name or range_name in seen_ranges:
            continue
        seen_ranges.add(range_name)
        enum_def = schema.get_enum(range_name)
        if enum_def is None:
            continue
        normalized_candidates.append(enum_def)

    for enum_def in normalized_candidates:
        for key, permissible_value in enum_def.permissible_values.items():
            meaning = permissible_value.meaning or ""
            aliases = {
                key,
                key.casefold(),
                meaning,
                meaning.casefold(),
                meaning.replace(":", "_"),
                meaning.replace(":", "_").casefold(),
            }
            if raw_value in aliases or raw_value.casefold() in aliases:
                return str(permissible_value.text or key), str(meaning)
    return "", ""


def _evidence_items(raw_evidence: Any) -> list[dict[str, Any]]:
    if not raw_evidence:
        return []
    if isinstance(raw_evidence, list):
        return [item for item in raw_evidence if isinstance(item, dict)]
    if isinstance(raw_evidence, dict):
        return [raw_evidence]
    return []


def _range_is_descriptor(range_name: str | None, schema: SchemaView) -> bool:
    if not range_name or schema.get_class(range_name) is None:
        return False
    return "Descriptor" in schema.class_ancestors(range_name)


def _range_is_claim_like(range_name: str | None, schema: SchemaView) -> bool:
    if not range_name or schema.get_class(range_name) is None:
        return False
    return "evidence" in {slot.name for slot in schema.class_induced_slots(range_name)}


def _singularize_claim_type(slot_name: str) -> str:
    claim_type = slot_name.removeprefix("has_")
    if claim_type.endswith("ies"):
        return f"{claim_type[:-3]}y"
    if claim_type.endswith("s") and claim_type not in {
        "pathophysiology",
        "histopathology",
    }:
        return claim_type[:-1]
    return claim_type


def _humanize_claim_type(claim_type: str) -> str:
    return _HUMANIZED_CLAIM_TYPE_OVERRIDES.get(
        claim_type, _humanize_slot_name(claim_type)
    )


def _humanize_slot_name(slot_name: str) -> str:
    return slot_name.replace("_", " ")
