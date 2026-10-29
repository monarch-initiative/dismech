"""The ordered section index shown at the top of a disorder page.

``SECTIONS`` lists every disorder-page card that has an anchor, **in the order
the template renders them**, grouped under a short heading. The page header is
generated from it, so a new card is added here once and its pill appears in the
right place; ``tests/test_page_sections.py`` fails if this order and the
template's anchor order drift apart.

>>> groups = section_index({"phenotypes": [{"name": "Pain"}], "genetic": [{"name": "GLA"}]})
>>> [(g["group"], [(i["label"], i["count"]) for i in g["items"]]) for g in groups]
[('Phenotypes & genetics', [('Phenotypes', 1), ('Genes', 1)])]
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Section:
    """One anchored card on the disorder page."""

    anchor: str
    label: str
    group: str
    count: Callable[[Mapping[str, Any], Mapping[str, int]], int]


def _size(value: Any) -> int:
    """Count a slot value: a list by length, any other non-empty value as one.

    >>> _size([1, 2]), _size({"a": 1}), _size(None), _size([])
    (2, 1, 0, 0)
    """
    if isinstance(value, list):
        return len(value)
    return 1 if value else 0


def _slot(key: str) -> Callable[[Mapping[str, Any], Mapping[str, int]], int]:
    return lambda disorder, extra: _size(disorder.get(key))


def _extra(key: str) -> Callable[[Mapping[str, Any], Mapping[str, int]], int]:
    return lambda disorder, extra: int(extra.get(key, 0))


def _mappings(disorder: Mapping[str, Any], extra: Mapping[str, int]) -> int:
    """Count mapped terms across every mapping list.

    >>> _mappings({"mappings": {"mondo_mappings": [1, 2], "icd10": [3]}}, {})
    3
    """
    mappings = disorder.get("mappings") or {}
    if not isinstance(mappings, dict):
        return 0
    return sum(len(v) for v in mappings.values() if isinstance(v, list))


def _variants(disorder: Mapping[str, Any], extra: Mapping[str, int]) -> int:
    """Count disease-level variants plus those nested under genes.

    >>> _variants({"variants": [1], "genetic": [{"variants": [1, 2]}, {}]}, {})
    3
    """
    nested = sum(
        len(gene.get("variants") or [])
        for gene in disorder.get("genetic") or []
        if isinstance(gene, dict)
    )
    return _size(disorder.get("variants")) + nested


def _models(disorder: Mapping[str, Any], extra: Mapping[str, int]) -> int:
    return sum(
        _size(disorder.get(key))
        for key in ("experimental_models", "animal_models", "computational_models")
    )


SECTIONS: tuple[Section, ...] = (
    Section("mappings", "Mappings", "Overview", _mappings),
    Section("definitions", "Definitions", "Overview", _slot("definitions")),
    Section("inheritance", "Inheritance", "Overview", _slot("inheritance")),
    Section("subtypes", "Subtypes", "Overview", _slot("has_subtypes")),
    Section("comorbidities", "Comorbidities", "Overview", _extra("comorbidities")),
    Section(
        "mechanistic-hypotheses",
        "Hypotheses",
        "Mechanism",
        _slot("mechanistic_hypotheses"),
    ),
    Section("discussions", "Knowledge gaps", "Mechanism", _slot("discussions")),
    Section(
        "pathophysiology", "Pathophysiology", "Mechanism", _slot("pathophysiology")
    ),
    Section("histopathology", "Histopathology", "Mechanism", _slot("histopathology")),
    Section("phenotypes", "Phenotypes", "Phenotypes & genetics", _slot("phenotypes")),
    Section("genetic", "Genes", "Phenotypes & genetics", _slot("genetic")),
    Section("variants", "Variants", "Phenotypes & genetics", _variants),
    Section(
        "external-assertions",
        "External assertions",
        "Phenotypes & genetics",
        _slot("external_assertions"),
    ),
    Section(
        "treatments", "Medical actions", "Treatment & exposures", _slot("treatments")
    ),
    Section(
        "environmental-factors",
        "Environmental factors",
        "Treatment & exposures",
        _slot("environmental"),
    ),
    Section("biochemical-markers", "Biomarkers", "Diagnosis", _slot("biochemical")),
    Section("diagnosis", "Diagnosis", "Diagnosis", _slot("diagnosis")),
    Section("imaging-findings", "Imaging", "Diagnosis", _slot("imaging_findings")),
    Section(
        "progression", "Progression", "Course & epidemiology", _slot("progression")
    ),
    Section("stages", "Stages", "Course & epidemiology", _slot("stages")),
    Section("prevalence", "Prevalence", "Course & epidemiology", _slot("prevalence")),
    Section(
        "epidemiology", "Epidemiology", "Course & epidemiology", _slot("epidemiology")
    ),
    Section(
        "infectious-agent",
        "Infectious agent",
        "Course & epidemiology",
        _slot("infectious_agent"),
    ),
    Section(
        "transmission", "Transmission", "Course & epidemiology", _slot("transmission")
    ),
    Section(
        "clinical-burden",
        "Clinical burden",
        "Course & epidemiology",
        _slot("clinical_burden"),
    ),
    Section(
        "differentials",
        "Differentials",
        "Course & epidemiology",
        _slot("differential_diagnoses"),
    ),
    Section("datasets", "Datasets", "Research", _slot("datasets")),
    Section("trials", "Clinical trials", "Research", _slot("clinical_trials")),
    Section("models", "Models", "Research", _models),
    Section("reports", "Reports", "Research", _extra("reports")),
    Section("references", "References", "Research", _slot("references")),
    Section("literature-summaries", "Deep research", "Research", _extra("literature")),
)


def section_index(
    disorder: Mapping[str, Any], extra: Mapping[str, int] | None = None
) -> list[dict[str, Any]]:
    """Return the non-empty sections of ``disorder``, grouped, in page order.

    ``extra`` carries counts that come from outside the YAML entry:
    ``comorbidities``, ``reports``, ``literature`` and ``hypothesis_reports``
    (shown as a note on the Hypotheses pill). Variants nested under genes
    have no card of their own, so their pill points at the Genes card.

    >>> [i["anchor"] for g in section_index({"genetic": [{"variants": [{}]}]}) for i in g["items"]]
    ['genetic', 'genetic']

    >>> groups = section_index(
    ...     {"mechanistic_hypotheses": [{}], "references": [{}, {}]},
    ...     {"hypothesis_reports": 1, "literature": 2},
    ... )
    >>> [(g["group"], [(i["label"], i["count"], i["note"]) for i in g["items"]]) for g in groups]
    [('Mechanism', [('Hypotheses', 1, '1 report')]), ('Research', [('References', 2, None), ('Deep research', 2, None)])]
    """
    extra = extra or {}
    groups: list[dict[str, Any]] = []
    for section in SECTIONS:
        count = section.count(disorder, extra)
        if not count:
            continue
        note = None
        if section.anchor == "mechanistic-hypotheses":
            reports = int(extra.get("hypothesis_reports", 0))
            if reports:
                note = f"{reports} report" + ("s" if reports != 1 else "")
        anchor = section.anchor
        if anchor == "variants" and not disorder.get("variants"):
            # Only gene-nested variants: there is no Variants card to jump to.
            anchor = "genetic"
        item = {"anchor": anchor, "label": section.label, "count": count, "note": note}
        if groups and groups[-1]["group"] == section.group:
            groups[-1]["items"].append(item)
        else:
            groups.append({"group": section.group, "items": [item]})
    return groups
