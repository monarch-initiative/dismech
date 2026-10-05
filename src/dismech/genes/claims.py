"""The only API a curated gene summary may call from its provedown claims.

A curated summary (``kb/genes/curated/hgnc_<n>.md``) states things about a gene
in prose, and wraps each checkable statement in a provedown result span whose
expression calls a method here. ``just genes-verify`` re-evaluates every span
against the current KB and ingest tables, so a summary that no longer matches
the entries it summarises fails verification instead of quietly going stale.

Return values are shaped for prose, because the authored text *is* the
compared value: names come back as the entries' own ``name`` strings, and enum
values come back lower-cased with underscores turned to spaces ("somatic
driver"). Methods that check a specific statement (``node``, ``in_module``)
return the value they were given when it holds and raise ``ClaimError`` when it
does not, so the span reads naturally and still fails loudly.

The verifier (:mod:`dismech.genes.curated`) refuses to execute a summary whose
code does anything other than import :func:`gene` and call methods on its
result. Keep everything a summary needs in this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dismech.genes.ingest import IngestTables, load_ingest
from dismech.genes.join import (
    NO_GENETIC_RECORD,
    NOT_NAMED,
    SUPPORTIVE_TIERS,
    UNTYPED,
    ClinGenMatch,
    clingen_matches,
    gene_status_in_entry,
)
from dismech.genes.slice import (
    GeneSlice,
    _cached_mondo_index,
    default_kb_root,
    gene_slice,
    normalize_hgnc_id,
)

__all__ = ["ClaimError", "GeneClaims", "gene"]


class ClaimError(AssertionError):
    """A summary statement the KB does not support."""


def _prose(value: str) -> str:
    return value.replace("_", " ").lower()


@lru_cache(maxsize=2)
def _ingest(root: str) -> IngestTables:
    return load_ingest(Path(root) / "genes" / "ingest")


@dataclass
class GeneClaims:
    slice: GeneSlice
    ingest: IngestTables
    mondo_index: dict[str, list[str]]

    # ----- identity (ingest layer) -----

    @property
    def hgnc_id(self) -> str:
        return self.slice.hgnc_id

    def symbol(self) -> str:
        row = self.ingest.hgnc.get(self.hgnc_id)
        return row["symbol"] if row else self.slice.label

    def name(self) -> str:
        row = self.ingest.hgnc.get(self.hgnc_id)
        if not row:
            raise ClaimError(f"{self.hgnc_id} has no HGNC ingest row")
        return row["name"]

    # ----- the KB slice -----

    def disorder_count(self) -> int:
        """How many disorder entries name this gene anywhere."""
        return len(self.slice.entries("disorder"))

    def disorders(
        self, relationship: str | None = None, origin: str | None = None
    ) -> set[str]:
        """Disorders naming the gene; with ``relationship``, only those whose
        ``genetic[]`` record types it that way (e.g. ``"causative"``); with
        ``origin``, only those whose record gives that ``variant_origin``
        (e.g. ``"germline"``, or ``"unrecorded"`` for a record that gives none)."""
        names = set(self.slice.entries("disorder"))
        if relationship is not None:
            names &= set(
                self.slice.entries_with_relationship(relationship.replace(" ", "_"))
            )
        if origin is not None:
            names = {n for n in names if origin in self._origins(n)}
        return names

    def includes(self, *names: str, relationship: str | None = None) -> set[str]:
        """The given disorder names, provided every one of them names this gene
        (and, with ``relationship``, types it that way).

        For "includes X and Y" statements that should survive the KB adding a
        third disease. Use with ``data-compare="names"``.
        """
        known = self.disorders(relationship)
        missing = [n for n in names if n not in known]
        if missing:
            qualifier = f" as {relationship}" if relationship else ""
            raise ClaimError(
                f"no disorder entry naming {self.symbol()}{qualifier}: {missing}"
            )
        return set(names)

    def variant_origin(self, entry: str) -> str:
        """``genetic[].variant_origin`` recorded for this gene in ``entry``, in prose.

        "unrecorded" when the entry's genetic records give none, which is the
        only honest thing a summary can say about the origin then: the
        entry's prose may say more, but nothing a claim can check does.
        """
        self._require_entry(entry)
        return " and ".join(sorted(self._origins(entry)))

    def _origins(self, entry: str) -> set[str]:
        origins = {
            _prose(o.details["variant_origin"])
            for o in self.slice.for_entry(entry)
            if o.section == "genetic" and o.details.get("variant_origin")
        }
        return origins or {"unrecorded"}

    def relationship(self, entry: str) -> str:
        """How ``entry`` records this gene, in prose: its ``genetic[].relationship_type``.

        Several types are joined with " and ". An entry with a genetic record
        that carries no type reads "untyped"; one that names the gene only
        elsewhere (a mechanism node, a model) reads "no genetic record". Both
        are legitimate things for a summary to say. Same vocabulary as the page.
        """
        self._require_entry(entry)
        return gene_status_in_entry(self.slice, entry)

    def no_genetic_record(self) -> set[str]:
        """Disorders that name this gene but have no ``genetic[]`` record for it."""
        return {
            e
            for e in self.slice.entries("disorder")
            if gene_status_in_entry(self.slice, e) == NO_GENETIC_RECORD
        }

    def untyped(self) -> set[str]:
        """Disorders with a ``genetic[]`` record for this gene but no ``relationship_type``."""
        return {
            e
            for e in self.slice.entries("disorder")
            if gene_status_in_entry(self.slice, e) == UNTYPED
        }

    def node(self, entry: str, node_name: str) -> str:
        """``node_name`` if it is a pathophysiology node of ``entry`` that names this gene."""
        self._require_entry(entry)
        if node_name not in self.slice.mechanism_nodes(entry):
            raise ClaimError(
                f"{entry!r} has no pathophysiology node {node_name!r} naming {self.symbol()}"
            )
        return node_name

    def nodes(self, entry: str) -> set[str]:
        """Pathophysiology node names in ``entry`` that name this gene."""
        self._require_entry(entry)
        return set(self.slice.mechanism_nodes(entry))

    def functional_impact(self, entry: str) -> str:
        """``genetic_context.functional_impact_category`` on this gene's nodes in ``entry``."""
        self._require_entry(entry)
        values = sorted(
            {
                occ.details["functional_impact_category"]
                for occ in self.slice.for_entry(entry)
                if occ.details.get("functional_impact_category")
            }
        )
        if not values:
            raise ClaimError(
                f"{entry!r} records no functional impact for {self.symbol()}"
            )
        return " and ".join(_prose(v) for v in values)

    def modules(self) -> set[str]:
        """Mechanism modules reached through nodes that name this gene."""
        return set(self.slice.modules())

    def in_module(self, module: str) -> str:
        if module not in self.slice.modules():
            raise ClaimError(
                f"no node naming {self.symbol()} conforms to module {module!r}"
            )
        return module

    def treatments(self) -> set[str]:
        """Treatment names, across disorders, that name this gene."""
        return set(self.slice.treatments())

    # ----- function layer (ai-gene-review ingest) -----

    def core_function_terms(self, relation: str | None = None) -> set[str]:
        """GO labels in this gene's ai-gene-review ``core_functions``."""
        labels: set[str] = set()
        for function in self.ingest.functions.get(self.hgnc_id, ()):
            for rel, terms in function["terms"].items():
                if relation is None or rel == relation:
                    labels.update(label for _id, label in terms)
        return labels

    def mechanism_processes(self) -> set[str]:
        """GO process labels on the KB pathophysiology nodes that name this gene."""
        labels: set[str] = set()
        for occ in self.slice.occurrences:
            for process in occ.details.get("biological_processes") or ():
                if process.get("label"):
                    labels.add(process["label"])
        return labels

    def shared_processes(self) -> set[str]:
        """GO terms both on this gene's KB mechanism nodes and in its core functions
        (matched by GO id, reported by label)."""
        core_ids = {
            term_id
            for function in self.ingest.functions.get(self.hgnc_id, ())
            for terms in function["terms"].values()
            for term_id, _label in terms
        }
        return {
            process["label"]
            for occ in self.slice.occurrences
            for process in occ.details.get("biological_processes") or ()
            if process.get("id") in core_ids and process.get("label")
        }

    # ----- ClinGen (ingest layer, joined to the KB by MONDO) -----

    def _clingen(self) -> list[ClinGenMatch]:
        return clingen_matches(
            self.slice, self.ingest.clingen.get(self.hgnc_id, []), self.mondo_index
        )

    def clingen(self, entry: str) -> str:
        """ClinGen's classification(s) of this gene for ``entry``'s own disease.

        Matched by MONDO identifier under the rule `just check-gene-validity`
        uses. Several assertions (one per mode of inheritance) are joined with
        " and " in MONDO / MOI order, lower-cased: "definitive".
        """
        values = [
            m.classification.lower() for m in self._clingen() if entry in m.entries
        ]
        if not values:
            raise ClaimError(
                f"ClinGen has no assertion for {self.symbol()} and {entry!r}"
            )
        return " and ".join(values)

    def clingen_diseases(self) -> int:
        """How many ClinGen assertions classify this gene, for any disease."""
        return len(self.ingest.clingen.get(self.hgnc_id, []))

    def clingen_without_entry(self) -> set[str]:
        """ClinGen disease labels for this gene that no dismech entry curates."""
        return {m.row["disease_label"] for m in self._clingen() if not m.entries}

    def clingen_but_untyped(self, *tiers: str) -> set[str]:
        """Entries ClinGen classifies this gene for whose own record does not type it
        (untyped, no genetic record, or the gene not named at all).

        Only the tiers that support a relationship count by default (Definitive,
        Strong, Moderate): a Disputed or Refuted tier on an entry that does not
        name the gene is agreement, not a gap. Pass tiers to choose others.
        """
        wanted = {t.lower() for t in tiers} if tiers else SUPPORTIVE_TIERS
        return {
            entry
            for m in self._clingen()
            if m.classification.lower() in wanted
            for entry, status in m.entries.items()
            if status in {UNTYPED, NO_GENETIC_RECORD, NOT_NAMED}
        }

    # ----- helpers -----

    def _require_entry(self, entry: str) -> None:
        if entry not in self.slice.entries(None):
            raise ClaimError(f"no entry named {entry!r} names {self.symbol()}")


def gene(hgnc_id: str, kb_root: Path | str | None = None) -> GeneClaims:
    """Claims about one gene, computed from the current KB and ingest tables."""
    canonical = normalize_hgnc_id(hgnc_id)
    if canonical is None:
        raise ValueError(f"not an HGNC CURIE: {hgnc_id!r}")
    root = Path(kb_root) if kb_root is not None else default_kb_root()
    resolved = str(root.resolve())
    return GeneClaims(
        slice=gene_slice(canonical, root),
        ingest=_ingest(resolved),
        mondo_index=_cached_mondo_index(resolved),
    )
