"""Guard the community-source corroboration rule (design decision 6b).

A reference tagged ``PatientOrganization`` or ``PatientCommunity`` may
corroborate a curated claim but may never be the only thing supporting it. A
patient-advocacy symptom page is good at telling a curator *where to look*; a
public patient forum records what a community discusses, which is evidence about
salience rather than about biology. Either can make an under-reported
manifestation findable, and neither is a study.

The rule is therefore mechanical: every ``evidence:`` block that cites a
community-tagged reference must also cite at least one reference that is not
community-tagged.

The tags live on the entry's top-level ``references:`` list, not on the evidence
items, so this joins the two by reference ID. That indirection is deliberate --
one tag per source, applied once, instead of a marker repeated on every evidence
item that happens to cite it.

Scope note: the rule is opt-in by tagging. An untagged advocacy URL is invisible
here, exactly as an unlabelled one is invisible to a query. Tagging is what makes
the sourcing class auditable, and it is a curation step, not something the tools
can infer -- no cache marker distinguishes an advocacy-organization page from any
other fetched URL.
"""

from __future__ import annotations

from typing import Any, Iterator

# ReferenceTagEnum values marking a reference as community-sourced.
COMMUNITY_REFERENCE_TAGS = frozenset({"PatientOrganization", "PatientCommunity"})


def iter_evidence_lists(node: Any, path: str = "") -> Iterator[tuple[str, list]]:
    """Yield every ``(dotted_path, evidence_list)`` pair anywhere in a document.

    Evidence blocks hang off many slots at many depths (top-level sections,
    nested ``downstream`` causal edges, ``readouts``, ``findings``, ``members``,
    ...), so walking the whole tree is the only way to reach them all.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else key
            if key == "evidence" and isinstance(value, list):
                yield child, value
            yield from iter_evidence_lists(value, child)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from iter_evidence_lists(item, f"{path}[{index}]")


def community_tagged_reference_ids(data: Any) -> set[str]:
    """Reference IDs carrying a community tag in the entry's ``references:``."""
    if not isinstance(data, dict):
        return set()
    return {
        str(ref.get("reference"))
        for ref in (data.get("references") or [])
        if isinstance(ref, dict)
        and ref.get("reference")
        and COMMUNITY_REFERENCE_TAGS.intersection(ref.get("tags") or [])
    }


def _is_reference_provenance(path: str) -> bool:
    """True for evidence hanging off the entry's own ``references:`` list.

    A ``references[].findings[].evidence`` block documenting a community sweep is
    a provenance record *about* the source, so being community-only is what it is
    for. Matched on the indexed prefix rather than a bare ``startswith`` so a
    future top-level slot named e.g. ``references_reviewed`` is not skipped by
    accident.
    """
    return path == "references" or path.startswith("references[")


def community_sole_support_errors(data: Any) -> list[str]:
    """Return one message per evidence block supported only by community sources."""
    community_ids = community_tagged_reference_ids(data)
    if not community_ids:
        return []

    errors: list[str] = []
    for path, evidence_list in iter_evidence_lists(data):
        if _is_reference_provenance(path):
            continue
        cited = [
            str(item.get("reference"))
            for item in evidence_list
            if isinstance(item, dict) and item.get("reference")
        ]
        if cited and all(ref in community_ids for ref in cited):
            errors.append(
                f"{path}: only community-sourced evidence "
                f"({', '.join(sorted(set(cited)))})"
            )
    return errors
