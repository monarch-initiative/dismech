"""Typed models for claim extraction outputs."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClaimRow:
    """A single flattened claim/evidence row."""

    disease_name: str
    disease_id: str
    claim_type: str
    claim_class: str
    source_path: str
    claim_kind: str
    claim_text: str
    subject_label: str
    subject_id: str
    predicate_label: str
    predicate_id: str
    object_label: str
    object_id: str
    qualifier_name: str
    qualifier_value: str
    qualifier_value_id: str
    qualifiers_json: str
    is_subclaim: bool
    qualifier_evidence_missing: bool
    evidence_reference: str
    evidence_reference_title: str
    evidence_supports: str
    evidence_source: str
    evidence_snippet: str
    evidence_explanation: str
