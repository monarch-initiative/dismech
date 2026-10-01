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
from dismech.genes.slice import (
    GeneSlice,
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

    def disorders(self, relationship: str | None = None) -> set[str]:
        """Disorders naming the gene; with ``relationship``, only those whose
        ``genetic[]`` record types it that way (e.g. ``"causative"``)."""
        if relationship is None:
            return set(self.slice.entries("disorder"))
        return set(self.slice.entries_with_relationship(relationship.replace(" ", "_")))

    def includes(self, *names: str) -> set[str]:
        """The given disorder names, provided every one of them names this gene.

        For "includes X and Y" statements that should survive the KB adding a
        third disease. Use with ``data-compare="set"``.
        """
        known = set(self.slice.entries("disorder"))
        missing = [n for n in names if n not in known]
        if missing:
            raise ClaimError(f"no disorder entry naming {self.symbol()}: {missing}")
        return set(names)

    def relationship(self, entry: str) -> str:
        """``genetic[].relationship_type`` for this gene in ``entry``, in prose.

        Several types are joined with " and "; an entry whose record carries no
        type reads "untyped", which is a legitimate thing for a summary to say.
        """
        self._require_entry(entry)
        types = self.slice.relationship_types(entry)
        return " and ".join(_prose(t) for t in types) if types else "untyped"

    def untyped(self) -> set[str]:
        """Disorders with a ``genetic[]`` record for this gene but no ``relationship_type``."""
        out = set()
        for occ in self.slice.occurrences:
            if (
                occ.entry_kind == "disorder"
                and occ.section == "genetic"
                and not occ.relationship_type
            ):
                if not self.slice.relationship_types(occ.entry_name):
                    out.add(occ.entry_name)
        return out

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
    return GeneClaims(
        slice=gene_slice(canonical, root), ingest=_ingest(str(root.resolve()))
    )
