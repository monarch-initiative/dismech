"""Identity anchors for a disease deep-research prompt.

``just research-disorder`` used to tell the provider three things about the
disease: its name, its MONDO ID and its category. For a serial-number name such
as "intellectual developmental disorder, autosomal dominant 64" none of those
says which gene the disease is about, and providers picked the wrong one: an
OpenScientist report for MONDO:0030934 (ZNF292) was about WDFY3, and one for
spermatogenic failure 26 (TSGA10) was about TDRD9. Both passed reference
validation; ``just preflight-dr`` caught them after a full provider run
(issue #14907, following #10495).

This module looks up what MONDO already holds about the disease's identity and
hands it to the prompt as three template variables:

``causal_genes``
    MONDO's ``RO:0004003`` causal gene(s), read with the same lookup
    ``preflight_dr`` uses, so the prompt and the check agree on the gene.
    When MONDO records none or cannot be read, the stub's MONDO-derived
    ``genes:`` block is used instead, and failing that the entry's own
    ``CAUSATIVE`` genes.
``omim_id``
    MONDO's OMIM cross-reference(s).
``synonyms``
    MONDO's exact synonyms, which for these diseases often name the gene
    ("ZNF292-related neurodevelopmental disorder"). When MONDO records none or
    cannot be read, the entry's own ``synonyms:``.

MONDO is read from the local build when it is on disk and from OLS otherwise
(#15436). Before the OLS fallback, a run without the build sent the provider no
OMIM number and only the entry's own synonyms, which a skeleton entry has not
yet verified. The local build is never downloaded here
(:func:`dismech.oak_db.local_build_present` is asked first), and HGNC is never
opened. If OLS is unreachable too, the failure is logged on stderr and the
committed sources are used.

A value with nothing behind it is :data:`NOT_RECORDED`, so a non-Mendelian
disease, or a run that could not read MONDO, gets the prompt it got before.

Usage (what the research recipes run)::

    python -m dismech.research_anchors kb/disorders/Foo.yaml MONDO:0030934

prints one ``key=value`` line per variable on stdout, ready for ``--var``, and
a one-line summary of where each value came from on stderr.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from dismech.mondo_ols import OlsMondoAdapter
from dismech.yaml_io import safe_load_path

NOT_RECORDED = "not recorded"

#: The prompt is for the provider, not a synonym dump. MONDO carries up to a
#: dozen exact synonyms for some diseases, mostly abbreviations.
MAX_SYNONYMS = 8

EXACT_SYNONYM_PREDICATES = frozenset({"oio:hasExactSynonym", "hasExactSynonym"})

DEFAULT_STUBS_DIR = Path("stubs")


@dataclass(frozen=True)
class IdentityAnchors:
    """What the prompt is told about which disease it is researching."""

    causal_genes: tuple[str, ...] = ()
    omim_ids: tuple[str, ...] = ()
    synonyms: tuple[str, ...] = ()
    gene_source: str = ""
    synonym_source: str = ""
    omim_source: str = ""

    def template_vars(self) -> dict[str, str]:
        return {
            "causal_genes": ", ".join(self.causal_genes) or NOT_RECORDED,
            "omim_id": ", ".join(f"OMIM:{i}" for i in self.omim_ids) or NOT_RECORDED,
            "synonyms": "; ".join(self.synonyms) or NOT_RECORDED,
        }

    def summary(self) -> str:
        genes = ", ".join(self.causal_genes) or "none"
        if self.causal_genes and self.gene_source:
            genes += f" ({self.gene_source})"
        omim = ", ".join(self.omim_ids) or "none"
        if self.omim_ids and self.omim_source:
            omim += f" ({self.omim_source})"
        synonyms = f"{len(self.synonyms)}"
        if self.synonyms and self.synonym_source:
            synonyms += f" ({self.synonym_source})"
        return (
            f"Identity anchors: causal genes {genes}; OMIM {omim}; synonyms {synonyms}"
        )


def _one_line(value: object) -> str:
    """Collapse whitespace: a ``--var`` value is one line of the prompt."""
    return " ".join(str(value).split())


def _dedupe(values, *, exclude: tuple[str, ...] = ()) -> tuple[str, ...]:
    seen = {e.casefold() for e in exclude if e}
    out = []
    for value in values:
        value = _one_line(value)
        if value and value.casefold() not in seen:
            seen.add(value.casefold())
            out.append(value)
    return tuple(out)


def exact_synonyms(mondo_id: str, adapter) -> tuple[str, ...]:
    """MONDO's exact synonyms for ``mondo_id``; empty if the adapter fails."""
    try:
        pairs = list(adapter.alias_relationships(mondo_id, exclude_labels=True))
    except Exception:  # pragma: no cover - adapter variance
        return ()
    return tuple(value for pred, value in pairs if pred in EXACT_SYNONYM_PREDICATES)


def anchors_from_mondo(
    mondo_id: str, adapter
) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    """``(genes, omim_ids, exact_synonyms)`` from a MONDO adapter.

    Reuses :func:`dismech.preflight_dr.fetch_mondo_record` with HGNC disabled,
    so it stays offline. A causal gene MONDO carries only as a bare CURIE is
    dropped: an identifier the provider cannot read is no anchor.
    """
    from dismech.preflight_dr import fetch_mondo_record

    record = fetch_mondo_record(mondo_id, adapter=adapter, use_hgnc=False)
    genes = tuple(g for g in record.genes if g not in record.unresolved_genes)
    return genes, tuple(record.omim_ids), exact_synonyms(mondo_id, adapter)


def genes_from_stub(mondo_id: str, stubs_dir: Path) -> tuple[str, ...]:
    """The causal genes recorded on the curation stub for ``mondo_id``, if any.

    ``just enrich-stubs`` copies MONDO's ``RO:0004003`` genes into each stub's
    ``genes:`` block, so this is the same fact read from a committed file.
    Curated diseases have no stub any more; that is the case the MONDO build
    covers.
    """
    if not mondo_id or not stubs_dir.is_dir():
        return ()
    needle = f"mondo_id: {mondo_id}"
    for path in sorted(stubs_dir.glob("*.yaml")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:  # pragma: no cover - unreadable file
            continue
        if needle not in text:
            continue
        stub = safe_load_path(path) or {}
        if stub.get("mondo_id") != mondo_id:
            continue
        labels = [
            g.get("label") for g in stub.get("genes") or [] if isinstance(g, dict)
        ]
        return _dedupe(label for label in labels if label)
    return ()


def _gene_label(row: dict) -> str | None:
    gene_term = row.get("gene_term") or {}
    if not isinstance(gene_term, dict):
        return None
    term = gene_term.get("term") or {}
    return (term.get("label") if isinstance(term, dict) else None) or gene_term.get(
        "preferred_term"
    )


def genes_from_entry(entry: dict) -> tuple[str, ...]:
    """The entry's own causal genes, read from its ``genetic`` rows.

    The last resort, for a curated disease whose stub is gone when the MONDO
    build is absent. ``relationship_type: CAUSATIVE`` rows win: a risk or
    modifier gene is not the gene that says which disease this is. Many
    monogenic entries leave ``relationship_type`` unset (``Cystic_Fibrosis``'s
    CFTR row), so when no row is ``CAUSATIVE`` an untyped row is used, but only
    if the untyped rows name exactly one gene. Several untyped genes are as
    likely to be somatic drivers or a differential as causes, and naming the
    wrong one would steer the provider the way this anchor exists to prevent.
    """
    rows = [row for row in entry.get("genetic") or [] if isinstance(row, dict)]
    causative = _dedupe(
        label
        for row in rows
        if row.get("relationship_type") == "CAUSATIVE"
        if (label := _gene_label(row))
    )
    if causative:
        return causative
    untyped = _dedupe(
        label
        for row in rows
        if not row.get("relationship_type")
        if (label := _gene_label(row))
    )
    return untyped if len(untyped) == 1 else ()


def _open_local_mondo():
    """The local MONDO adapter, or ``None`` when the build is not on disk."""
    from dismech.oak_db import local_build_present
    from dismech.preflight_dr import MONDO_ADAPTER

    if not local_build_present(MONDO_ADAPTER):
        return None
    from oaklib import get_adapter

    return get_adapter(MONDO_ADAPTER)


def _open_ols_mondo(mondo_id: str):
    """An OLS-backed MONDO adapter holding ``mondo_id``, or ``None`` if OLS fails.

    The term is fetched here so an unreachable OLS is reported once, as such,
    rather than surfacing as a run of empty answers.
    """
    from dismech.mondo_ols import OlsLookupError

    adapter = OlsMondoAdapter()
    try:
        adapter.term(mondo_id)
    except OlsLookupError as exc:
        print(
            f"MONDO identity lookup for {mondo_id} via OLS failed ({exc}); "
            "no local MONDO build either, so OMIM and MONDO synonyms are not "
            "recorded",
            file=sys.stderr,
        )
        return None
    return adapter


def collect_anchors(
    entry: dict,
    mondo_id: str,
    *,
    adapter=None,
    use_local_mondo: bool = True,
    stubs_dir: Path = DEFAULT_STUBS_DIR,
) -> IdentityAnchors:
    """Gather the identity anchors for one disorder entry.

    ``adapter`` is a MONDO adapter to use; without one, the local build is
    opened when it is already on disk, and OLS is asked otherwise
    (``use_local_mondo=False`` skips both). Any MONDO failure falls back to the
    committed sources rather than failing the research run that asked.
    """
    name = _one_line(entry.get("name") or "")
    genes: tuple[str, ...] = ()
    omim: tuple[str, ...] = ()
    mondo_synonyms: tuple[str, ...] = ()
    gene_source = synonym_source = ""
    mondo_source = "MONDO"

    if mondo_id:
        try:
            if adapter is None and use_local_mondo:
                adapter = _open_local_mondo()
                if adapter is None:
                    adapter = _open_ols_mondo(mondo_id)
            if adapter is not None:
                if isinstance(adapter, OlsMondoAdapter):
                    mondo_source = "MONDO via OLS"
                genes, omim, mondo_synonyms = anchors_from_mondo(mondo_id, adapter)
        except Exception as exc:  # pragma: no cover - adapter variance
            print(
                f"MONDO identity lookup for {mondo_id} failed: {exc}", file=sys.stderr
            )
    if genes:
        gene_source = mondo_source
    else:
        genes = genes_from_stub(mondo_id, stubs_dir)
        gene_source = "stub" if genes else ""
    if not genes:
        genes = genes_from_entry(entry)
        gene_source = "entry" if genes else ""

    label = ""
    if adapter is not None and mondo_id:
        try:
            label = _one_line(adapter.label(mondo_id) or "")
        except Exception as exc:  # pragma: no cover - adapter variance
            print(f"MONDO label lookup for {mondo_id} failed: {exc}", file=sys.stderr)
    exclude = (name, name.replace("_", " "), label)
    synonyms = _dedupe(mondo_synonyms, exclude=exclude)
    if synonyms:
        synonym_source = mondo_source
    else:
        entry_synonyms = [s for s in entry.get("synonyms") or [] if isinstance(s, str)]
        synonyms = _dedupe(entry_synonyms, exclude=exclude)
        synonym_source = "entry" if synonyms else ""

    return IdentityAnchors(
        causal_genes=_dedupe(genes),
        omim_ids=omim,
        synonyms=synonyms[:MAX_SYNONYMS],
        gene_source=gene_source,
        synonym_source=synonym_source,
        omim_source=mondo_source if omim else "",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "yaml_file", type=Path, help="Disorder YAML the research run is for"
    )
    parser.add_argument(
        "mondo_id", nargs="?", default="", help="The entry's MONDO ID (may be empty)"
    )
    parser.add_argument("--stubs-dir", type=Path, default=DEFAULT_STUBS_DIR)
    parser.add_argument(
        "--no-mondo",
        action="store_true",
        help="Do not look MONDO up at all: neither the local build nor OLS",
    )
    args = parser.parse_args(argv)

    try:
        entry = safe_load_path(args.yaml_file) or {}
        anchors = collect_anchors(
            entry if isinstance(entry, dict) else {},
            args.mondo_id.strip(),
            use_local_mondo=not args.no_mondo,
            stubs_dir=args.stubs_dir,
        )
    except Exception as exc:  # never cost a paid research run its prompt
        print(f"identity anchors unavailable: {exc}", file=sys.stderr)
        anchors = IdentityAnchors()

    for key, value in anchors.template_vars().items():
        print(f"{key}={value}")
    print(anchors.summary(), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
