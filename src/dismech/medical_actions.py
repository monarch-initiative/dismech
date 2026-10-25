"""Which treatments are non-therapeutic actions, and the link rule they follow.

A treatment whose ``action_category`` is DIAGNOSTIC, SCREENING, MONITORING or
COUNSELING_INFORMATIONAL does not act on the disease, so it may not carry the
``target_mechanisms`` / ``target_phenotypes`` links that render as treatment
edges in the pathograph (``MedicalActionCategoryEnum`` in the schema says so
for each value).

Most treatments leave ``action_category`` unset, so a rule keyed on the slot
alone misses the commonest case: about 1,250 entries carry a Genetic
Counseling treatment and only a few hundred categorize it. A small set of
treatment terms is therefore taken to imply a category when none is recorded.
The set is deliberately narrow: a term belongs here only when every use of it
is informational. Behavioral and lifestyle counseling are interventions, and
screening or imaging terms are often bundled with the treatment that follows a
positive result, so neither is inferred.

An explicit ``action_category`` always wins. A treatment bound to Genetic
Counseling that bundles a real intervention ("counseling and presymptomatic
supplementation") sets ``action_category: THERAPEUTIC`` and keeps its links.
"""

from __future__ import annotations

NON_THERAPEUTIC_ACTION_CATEGORIES = frozenset(
    {"DIAGNOSTIC", "SCREENING", "MONITORING", "COUNSELING_INFORMATIONAL"}
)

# treatment_term CURIE -> the action_category it implies when none is set.
IMPLIED_ACTION_CATEGORIES = {
    "NCIT:C15240": "COUNSELING_INFORMATIONAL",  # Genetic Counseling
    "NCIT:C61547": "COUNSELING_INFORMATIONAL",  # Counseling
    "NCIT:C171451": "COUNSELING_INFORMATIONAL",  # Fertility and Reproductive Counseling
}

TARGET_SLOTS = ("target_mechanisms", "target_phenotypes")


def may_have_findings(text: str) -> bool:
    """Cheap text prefilter: False means the raw YAML cannot produce a finding."""
    if not any(slot in text for slot in TARGET_SLOTS):
        return False
    return "action_category" in text or any(
        c in text for c in IMPLIED_ACTION_CATEGORIES
    )


def effective_action_category(treatment: dict) -> tuple[str | None, bool]:
    """Return ``(category, inferred)`` for one treatment.

    ``inferred`` is true when the category came from the treatment term rather
    than from an explicit ``action_category``.
    """
    explicit = treatment.get("action_category")
    if explicit:
        return explicit, False
    term = (treatment.get("treatment_term") or {}).get("term") or {}
    implied = IMPLIED_ACTION_CATEGORIES.get(term.get("id"))
    return implied, implied is not None


def non_therapeutic_action_target_errors(data: dict) -> list[str]:
    """Find non-therapeutic treatments that link to pathograph nodes."""
    errors = []
    for i, treatment in enumerate((data or {}).get("treatments") or []):
        if not isinstance(treatment, dict):
            continue
        category, inferred = effective_action_category(treatment)
        if category not in NON_THERAPEUTIC_ACTION_CATEGORIES:
            continue
        slots = [slot for slot in TARGET_SLOTS if treatment.get(slot)]
        if not slots:
            continue
        name = treatment.get("name", f"treatments[{i}]")
        if inferred:
            term_id = treatment["treatment_term"]["term"]["id"]
            source = f"treatment_term {term_id} implies action_category={category!r}"
        else:
            source = f"action_category={category!r}"
        errors.append(
            f"treatments[{i}] {name!r}: {source} but it also has "
            f"treatment-style target slots: {', '.join(slots)}"
        )
    return errors
