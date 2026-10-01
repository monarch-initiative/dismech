"""The per-gene slice of the knowledge base: every place an entry names a gene.

This is the middle layer of a gene page (see ``docs/gene-pages.md``). It is
**computed, never committed**: each call walks ``kb/`` through
:mod:`dismech.kb_cache` and reports what the disease, module and comorbidity
entries currently say about a gene. The ingest layer (``kb/genes/ingest/``)
says what outside sources say; the curated layer (``kb/genes/curated/``) is a
summary whose checkable claims are recomputed from *this* module, so a summary
cannot drift away from the entries it summarises without its verification
failing.

What counts as "naming a gene" is structural, not textual: a descriptor whose
``term.id`` is an HGNC CURIE, anywhere inside a top-level section item. A gene
symbol mentioned only in prose, or a CURIE quoted inside an evidence snippet,
is not an occurrence. The walk is generic on purpose. The schema has about
twenty gene-valued slots (``Genetic.gene_term``, ``Pathophysiology.genes``,
``OligonucleotideDetail.target_gene``, ``DeliverySystem.targeting_receptor``,
``Variant.regulatory_target_gene``, ...), and an enumerated list would silently
miss the next one somebody adds.
"""

from __future__ import annotations

import os
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

from dismech import kb_cache

__all__ = [
    "ENTRY_KINDS",
    "GeneOccurrence",
    "GeneSlice",
    "build_gene_index",
    "gene_slice",
    "iter_gene_occurrences",
    "normalize_hgnc_id",
]

#: ``kb/`` subdirectories walked, and the singular kind each one's entries get.
ENTRY_KINDS: dict[str, str] = {
    "disorders": "disorder",
    "modules": "module",
    "comorbidities": "comorbidity",
}

#: Top-level keys that are entry metadata rather than curated sections. A gene
#: descriptor under one of these is not a claim about the disease.
_SKIPPED_SECTIONS = frozenset(
    {
        "name",
        "category",
        "creation_date",
        "updated_date",
        "description",
        "notes",
        "review_notes",
        "synonyms",
        "disease_term",
        "mappings",
        "references",
    }
)


def normalize_hgnc_id(curie: object) -> str | None:
    """Return the canonical lowercase ``hgnc:<n>`` form, or None if not HGNC.

    The KB writes ``hgnc:`` (canonical) and, in older entries, ``HGNC:``; both
    name the same gene, so the slice keys on one spelling.
    """
    if not isinstance(curie, str):
        return None
    prefix, sep, local = curie.strip().partition(":")
    if not sep or prefix.lower() != "hgnc" or not local.strip().isdigit():
        return None
    return f"hgnc:{local.strip()}"


@dataclass(frozen=True)
class GeneOccurrence:
    """One section item of one entry that names a gene.

    ``slots`` lists every path inside the item where the gene appears (a
    ``genetic[]`` record names its gene in ``gene_term`` and often again in
    ``variants[].gene``), so an item is one occurrence however many times it
    repeats the gene.
    """

    hgnc_id: str
    label: str
    entry_kind: str
    entry_stem: str
    entry_name: str
    section: str
    item_name: str
    slots: tuple[str, ...]
    details: dict[str, Any] = field(default_factory=dict, compare=False, hash=False)

    @property
    def relationship_type(self) -> str | None:
        return self.details.get("relationship_type")


@dataclass
class GeneSlice:
    """Every occurrence of one gene across the walked entries."""

    hgnc_id: str
    label: str
    occurrences: list[GeneOccurrence] = field(default_factory=list)

    def entries(self, kind: str | None = "disorder") -> list[str]:
        """Names of the entries naming this gene, sorted; ``kind=None`` for all."""
        return sorted(
            {
                occ.entry_name
                for occ in self.occurrences
                if kind is None or occ.entry_kind == kind
            },
            key=str.casefold,
        )

    def for_entry(self, entry_name: str) -> list[GeneOccurrence]:
        return [occ for occ in self.occurrences if occ.entry_name == entry_name]

    def sections(self, entry_name: str | None = None) -> list[str]:
        occs = self.for_entry(entry_name) if entry_name else self.occurrences
        return sorted({occ.section for occ in occs})

    def relationship_types(self, entry_name: str | None = None) -> list[str]:
        """``genetic[].relationship_type`` values recorded for this gene."""
        occs = self.for_entry(entry_name) if entry_name else self.occurrences
        return sorted(
            {
                occ.relationship_type
                for occ in occs
                if occ.section == "genetic" and occ.relationship_type
            }
        )

    def entries_with_relationship(self, relationship_type: str) -> list[str]:
        """Disorders whose ``genetic[]`` records type this gene ``relationship_type``."""
        wanted = relationship_type.upper()
        return sorted(
            {
                occ.entry_name
                for occ in self.occurrences
                if occ.entry_kind == "disorder"
                and occ.section == "genetic"
                and (occ.relationship_type or "").upper() == wanted
            },
            key=str.casefold,
        )

    def mechanism_nodes(self, entry_name: str | None = None) -> list[str]:
        """``pathophysiology[]`` node names that carry this gene."""
        occs = self.for_entry(entry_name) if entry_name else self.occurrences
        return sorted(
            {occ.item_name for occ in occs if occ.section == "pathophysiology"}
        )

    def treatments(self, entry_name: str | None = None) -> list[str]:
        """``treatments[]`` that name this gene (an oligonucleotide target, a receptor, ...)."""
        occs = self.for_entry(entry_name) if entry_name else self.occurrences
        return sorted({occ.item_name for occ in occs if occ.section == "treatments"})

    def modules(self) -> list[str]:
        """Module stems reached through ``conforms_to`` on a node naming this gene,
        plus modules that name the gene themselves."""
        stems: set[str] = set()
        for occ in self.occurrences:
            if occ.entry_kind == "module":
                stems.add(occ.entry_stem)
            for ref in occ.details.get("conforms_to") or ():
                stem = ref.split("#", 1)[0].strip()
                if stem:
                    stems.add(stem)
        return sorted(stems)


# ---------------------------------------------------------------------------
# walking


def _descriptor_gene(value: object) -> tuple[str, str] | None:
    if not isinstance(value, dict):
        return None
    term = value.get("term")
    if not isinstance(term, dict):
        return None
    hgnc_id = normalize_hgnc_id(term.get("id"))
    if hgnc_id is None:
        return None
    label = term.get("label") or value.get("preferred_term") or hgnc_id
    return hgnc_id, str(label)


def _walk_descriptors(value: object, path: str) -> Iterator[tuple[str, str, str]]:
    """Yield ``(hgnc_id, label, slot_path)`` for gene descriptors under ``value``."""
    gene = _descriptor_gene(value)
    if gene is not None:
        yield gene[0], gene[1], path
        # A gene descriptor can carry qualifiers; nothing below it is another gene.
        return
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "evidence":
                continue
            child_path = f"{path}.{key}" if path else str(key)
            yield from _walk_descriptors(child, child_path)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_descriptors(child, f"{path}[]" if path else "[]")


def _item_name(item: dict) -> str:
    for key in ("name", "species", "accession", "population", "phase"):
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def _term_label(descriptor: object) -> str | None:
    if not isinstance(descriptor, dict):
        return None
    term = descriptor.get("term")
    if isinstance(term, dict) and term.get("label"):
        return str(term["label"])
    preferred = descriptor.get("preferred_term")
    return str(preferred) if preferred else None


def _item_details(section: str, item: dict) -> dict[str, Any]:
    """The few fields of an item that a gene page and a summary claim about."""
    details: dict[str, Any] = {}
    if isinstance(item.get("subtype"), str):
        details["subtype"] = item["subtype"]
    if section == "genetic":
        for key in ("relationship_type", "association", "variant_origin"):
            if isinstance(item.get(key), str):
                details[key] = item[key]
        validity = []
        for assertion in item.get("gene_disease_validity") or ():
            if isinstance(assertion, dict) and assertion.get("validity_classification"):
                validity.append(
                    {
                        "classification": assertion.get("validity_classification"),
                        "classified_by": assertion.get("classified_by"),
                        "subtype": assertion.get("subtype"),
                    }
                )
        if validity:
            details["gene_disease_validity"] = validity
    elif section == "pathophysiology":
        if isinstance(item.get("biological_scale"), str):
            details["biological_scale"] = item["biological_scale"]
        context = item.get("genetic_context")
        if isinstance(context, dict):
            for key in ("functional_impact_category", "variant_origin"):
                if isinstance(context.get(key), str):
                    details[key] = context[key]
        conforms = item.get("conforms_to")
        if isinstance(conforms, str):
            conforms = [conforms]
        if isinstance(conforms, list):
            details["conforms_to"] = [c for c in conforms if isinstance(c, str)]
        processes = []
        for descriptor in item.get("biological_processes") or ():
            if not isinstance(descriptor, dict):
                continue
            term = (
                descriptor.get("term")
                if isinstance(descriptor.get("term"), dict)
                else {}
            )
            processes.append(
                {
                    "id": term.get("id"),
                    "label": _term_label(descriptor),
                    "modifier": descriptor.get("modifier"),
                }
            )
        if processes:
            details["biological_processes"] = processes
    elif section == "treatments":
        if isinstance(item.get("therapeutic_modality"), str):
            details["therapeutic_modality"] = item["therapeutic_modality"]
    return details


def _iter_section_items(document: dict) -> Iterator[tuple[str, dict]]:
    for section, value in document.items():
        if section in _SKIPPED_SECTIONS:
            continue
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    yield section, item
        elif isinstance(value, dict):
            yield section, value


def occurrences_in_document(
    document: object, *, entry_kind: str, entry_stem: str
) -> list[GeneOccurrence]:
    """Gene occurrences in one parsed entry."""
    if not isinstance(document, dict):
        return []
    entry_name = str(document.get("name") or entry_stem)
    found: list[GeneOccurrence] = []
    for section, item in _iter_section_items(document):
        per_gene: dict[str, tuple[str, list[str]]] = {}
        for hgnc_id, label, slot in _walk_descriptors(item, ""):
            label_slots = per_gene.setdefault(hgnc_id, (label, []))
            if slot not in label_slots[1]:
                label_slots[1].append(slot)
        if not per_gene:
            continue
        details = _item_details(section, item)
        name = _item_name(item)
        for hgnc_id, (label, slots) in per_gene.items():
            found.append(
                GeneOccurrence(
                    hgnc_id=hgnc_id,
                    label=label,
                    entry_kind=entry_kind,
                    entry_stem=entry_stem,
                    entry_name=entry_name,
                    section=section,
                    item_name=name,
                    slots=tuple(slots),
                    details=details,
                )
            )
    return found


def iter_gene_occurrences(
    kb_root: Path = Path("kb"),
    kinds: Iterable[str] = tuple(ENTRY_KINDS),
) -> Iterator[GeneOccurrence]:
    """Every gene occurrence in the walked ``kb/`` subdirectories, in path order."""
    for kind_dir in kinds:
        entry_kind = ENTRY_KINDS[kind_dir]
        directory = Path(kb_root) / kind_dir
        if not directory.is_dir():
            continue
        for path, document in kb_cache.iter_documents(directory):
            yield from occurrences_in_document(
                document, entry_kind=entry_kind, entry_stem=path.stem
            )


def build_gene_index(
    kb_root: Path = Path("kb"),
    kinds: Iterable[str] = tuple(ENTRY_KINDS),
) -> dict[str, GeneSlice]:
    """``{hgnc_id: GeneSlice}`` over the walked entries.

    The slice's ``label`` is the most common ``term.label`` written for the
    CURIE, which is HGNC's canonical symbol wherever term validation has run.
    """
    index: dict[str, GeneSlice] = {}
    label_votes: dict[str, dict[str, int]] = {}
    for occ in iter_gene_occurrences(kb_root, kinds):
        gene = index.setdefault(occ.hgnc_id, GeneSlice(occ.hgnc_id, occ.label))
        gene.occurrences.append(occ)
        votes = label_votes.setdefault(occ.hgnc_id, {})
        votes[occ.label] = votes.get(occ.label, 0) + 1
    for hgnc_id, votes in label_votes.items():
        index[hgnc_id].label = max(sorted(votes), key=lambda lab: votes[lab])
    return index


@lru_cache(maxsize=4)
def _cached_index(kb_root: str) -> dict[str, GeneSlice]:
    return build_gene_index(Path(kb_root))


def gene_slice(hgnc_id: str, kb_root: Path | str | None = None) -> GeneSlice:
    """The slice for one gene; empty (no occurrences) if nothing names it.

    The index is memoised per ``kb_root`` for the life of the process, so a
    summary with dozens of claims walks the KB once. ``kb_root`` defaults to
    the repository's ``kb/`` resolved from this file, so the call works from a
    provedown verification, which runs with the document's directory as cwd.
    """
    canonical = normalize_hgnc_id(hgnc_id)
    if canonical is None:
        raise ValueError(f"not an HGNC CURIE: {hgnc_id!r}")
    root = Path(kb_root) if kb_root is not None else default_kb_root()
    index = _cached_index(str(root.resolve()))
    return index.get(canonical) or GeneSlice(canonical, canonical)


def default_kb_root() -> Path:
    """``kb/`` of the checkout this module was imported from.

    ``DISMECH_GENES_KB_ROOT`` overrides it, so tests can verify a summary
    against a fixture KB without the summary naming a path.
    """
    override = os.environ.get("DISMECH_GENES_KB_ROOT")
    if override:
        return Path(override)
    return Path(__file__).resolve().parents[3] / "kb"
