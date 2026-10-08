"""Joins between the ingest layer and the KB slice.

Kept apart from both so the renderer and the claims API compute a join the
same way, and a summary cannot claim something its page would show differently.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from dismech.genes.slice import GeneSlice

#: How the KB records the gene for an entry ClinGen has classified it for.
NOT_NAMED = "not named"
NO_GENETIC_RECORD = "no genetic record"
UNTYPED = "untyped"

#: ClinGen tiers that support a gene-disease relationship. A Limited, Disputed,
#: Refuted or No Known Disease Relationship tier is not a reason to type a
#: record causative, so it is not a gap when the record is untyped.
SUPPORTIVE_TIERS = frozenset({"definitive", "strong", "moderate"})


@dataclass
class ClinGenMatch:
    """One ClinGen assertion for the gene, with the dismech entries for its disease."""

    row: dict[str, str]
    #: ``{entry name: how the entry records this gene}``. The value is the
    #: prose relationship type(s), or one of NOT_NAMED / NO_GENETIC_RECORD / UNTYPED.
    entries: dict[str, str] = field(default_factory=dict)

    @property
    def classification(self) -> str:
        return self.row.get("classification", "")


def gene_status_in_entry(gene: GeneSlice, entry: str) -> str:
    occurrences = gene.for_entry(entry)
    if not occurrences:
        return NOT_NAMED
    if not any(o.section == "genetic" for o in occurrences):
        return NO_GENETIC_RECORD
    types = gene.relationship_types(entry)
    if not types:
        return UNTYPED
    return " and ".join(t.replace("_", " ").lower() for t in types)


def clingen_matches(
    gene: GeneSlice,
    clingen_rows: list[dict[str, str]],
    mondo_index: dict[str, list[str]],
) -> list[ClinGenMatch]:
    """Each ClinGen row for the gene, matched to the entries whose own disease
    (``disease_term``, a subtype term, or an exactMatch mapping) is its MONDO.

    An assertion with no matching entry is kept with no entries: a disease
    ClinGen classifies the gene for that dismech has not curated.
    """
    matches = []
    for row in clingen_rows:
        entries = sorted(mondo_index.get(row.get("mondo_id", ""), []), key=str.casefold)
        matches.append(
            ClinGenMatch(
                row=row, entries={e: gene_status_in_entry(gene, e) for e in entries}
            )
        )
    return matches
