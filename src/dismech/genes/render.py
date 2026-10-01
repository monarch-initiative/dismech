"""Render ``pages/genes/``: one page per gene plus a searchable index.

Each page merges the three layers (``docs/gene-pages.md``):

1. **Ingest** (``kb/genes/ingest/``): HGNC identity and the ai-gene-review
   function summary, each labelled with its source and pin.
2. **Curated** (``kb/genes/curated/hgnc_<n>.md``), when one exists: the
   agent-written summary, re-verified with provedown at render time and shown
   with its verification state. A stale summary is shown as stale, not hidden.
3. **KB slice** (:mod:`dismech.genes.slice`): every disorder, node, subtype,
   model and treatment that names the gene, computed from ``kb/`` now.

Genes named by at least ``min_disorders`` disorders get a page; the rest get an
index row linking straight to their disorder. A curated summary always gets a
page, whatever the count.
"""

from __future__ import annotations

import logging
from collections.abc import Iterable
from pathlib import Path

from dismech.export.utils import slugify
from dismech.genes.curated import (
    CURATED_DIR,
    SummaryResult,
    summary_body_html,
    verify_summary,
)
from dismech.genes.ingest import INGEST_DIR, IngestTables, load_ingest
from dismech.genes.slice import GeneSlice, build_gene_index, normalize_hgnc_id

logger = logging.getLogger(__name__)

#: Sections shown as their own column on the per-disorder rows, in order.
_SECTION_LABELS = {
    "genetic": "genetic",
    "pathophysiology": "mechanism",
    "has_subtypes": "subtype",
    "variants": "variant",
    "animal_models": "animal model",
    "experimental_models": "experimental model",
    "computational_models": "computational model",
    "treatments": "treatment",
    "datasets": "dataset",
    "diagnosis": "diagnosis",
    "phenotypes": "phenotype",
    "biochemical": "biochemical",
    "discussions": "discussion",
}

_MAX_ITEMS_PER_SECTION = 8


def gene_page_name(hgnc_id: str) -> str:
    """``hgnc_9588.html``: keyed on the identifier, because symbols get renamed."""
    return hgnc_id.replace(":", "_") + ".html"


def _prose(value: str | None) -> str:
    return value.replace("_", " ").lower() if value else ""


def _xrefs(hgnc_id: str, row: dict[str, str] | None) -> list[dict[str, str]]:
    number = hgnc_id.split(":", 1)[1]
    links = [
        {
            "label": f"HGNC:{number}",
            "href": f"https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:{number}",
        },
        {"label": "Monarch", "href": f"https://monarchinitiative.org/HGNC:{number}"},
    ]
    if not row:
        return links
    if row.get("entrez_id"):
        links.append(
            {
                "label": f"NCBI Gene {row['entrez_id']}",
                "href": f"https://www.ncbi.nlm.nih.gov/gene/{row['entrez_id']}",
            }
        )
    if row.get("ensembl_gene_id"):
        links.append(
            {
                "label": row["ensembl_gene_id"],
                "href": f"https://www.ensembl.org/id/{row['ensembl_gene_id']}",
            }
        )
    for uniprot in (row.get("uniprot_ids") or "").split("|"):
        if uniprot:
            links.append(
                {
                    "label": f"UniProt {uniprot}",
                    "href": f"https://www.uniprot.org/uniprotkb/{uniprot}",
                }
            )
    for omim in (row.get("omim_id") or "").split("|"):
        if omim:
            links.append(
                {"label": f"OMIM {omim}", "href": f"https://omim.org/entry/{omim}"}
            )
    return links


def _disorder_rows(gene: GeneSlice) -> list[dict]:
    rows = []
    for name in gene.entries("disorder"):
        occs = gene.for_entry(name)
        stem = occs[0].entry_stem
        genetic = [o for o in occs if o.section == "genetic"]
        relationship = gene.relationship_types(name)
        associations = sorted(
            {o.details["association"] for o in genetic if o.details.get("association")}
        )
        origins = sorted(
            {
                o.details["variant_origin"]
                for o in occs
                if o.details.get("variant_origin")
            }
        )
        impacts = sorted(
            {
                o.details["functional_impact_category"]
                for o in occs
                if o.details.get("functional_impact_category")
            }
        )
        subtypes = sorted(
            {o.details["subtype"] for o in occs if o.details.get("subtype")}
        )
        validity = [
            v for o in genetic for v in o.details.get("gene_disease_validity") or ()
        ]
        sections = []
        for section, label in _SECTION_LABELS.items():
            items = sorted(
                {o.item_name or "(unnamed)" for o in occs if o.section == section}
            )
            if section == "genetic" or not items:
                continue
            sections.append(
                {
                    "label": label,
                    "names": items[:_MAX_ITEMS_PER_SECTION],
                    "more": max(0, len(items) - _MAX_ITEMS_PER_SECTION),
                }
            )
        other = sorted({o.section for o in occs} - set(_SECTION_LABELS))
        rows.append(
            {
                "name": name,
                "href": f"../disorders/{slugify(name)}.html",
                "stem": stem,
                "relationship": [_prose(r) for r in relationship],
                "has_genetic_record": bool(genetic),
                "associations": associations,
                "origins": [_prose(o) for o in origins],
                "impacts": [_prose(i) for i in impacts],
                "subtypes": subtypes,
                "validity": validity,
                "sections": sections,
                "other_sections": other,
                "sort_key": (
                    0 if relationship else 1 if genetic else 2,
                    name.casefold(),
                ),
            }
        )
    rows.sort(key=lambda r: r["sort_key"])
    return rows


def _module_rows(gene: GeneSlice) -> list[dict]:
    named_in = {o.entry_stem for o in gene.occurrences if o.entry_kind == "module"}
    rows = []
    for stem in gene.modules():
        via = sorted(
            {
                o.entry_name
                for o in gene.occurrences
                if o.entry_kind == "disorder"
                and any(
                    ref.split("#", 1)[0].strip() == stem
                    for ref in o.details.get("conforms_to") or ()
                )
            },
            key=str.casefold,
        )
        rows.append(
            {
                "stem": stem,
                "href": f"../modules/{stem}.html",
                "via": via,
                "named_in_module": stem in named_in,
            }
        )
    return rows


def _function_context(hgnc_id: str, ingest: IngestTables) -> dict | None:
    review = ingest.reviews.get(hgnc_id)
    if not review:
        return None
    agr = ingest.sources.get("ai-gene-review") or {}
    commit = agr.get("commit", "main")
    base = agr.get("web_base") or "https://github.com/ai4curation/ai-gene-review/blob"
    complete = review.get("status") == "COMPLETE"
    return {
        "status": review.get("status") or "unknown",
        "complete": complete,
        "description": review.get("description") if complete else "",
        "functions": ingest.functions.get(hgnc_id, []) if complete else [],
        "href": f"{base}/{commit}/{review['review_path']}",
        "uniprot": review.get("uniprot_id"),
        "commit": commit[:12],
    }


def _summary_context(path: Path, verify: bool) -> dict:
    result: SummaryResult = verify_summary(path, execute=verify)
    return {
        "html": summary_body_html(path, result),
        "state": result.state,
        "status": result.frontmatter.get("status", "DRAFT"),
        "passed": result.passed,
        "claims": result.claims,
        "problems": result.problems,
        "source": path.as_posix(),
    }


def build_gene_contexts(
    *,
    kb_root: Path = Path("kb"),
    ingest_dir: Path = INGEST_DIR,
    curated_dir: Path = CURATED_DIR,
    min_disorders: int = 2,
    only: Iterable[str] | None = None,
    verify: bool = True,
) -> tuple[list[dict], list[dict]]:
    """Return ``(page_contexts, index_rows)``."""
    index = build_gene_index(kb_root)
    ingest = load_ingest(ingest_dir)
    curated = {
        normalize_hgnc_id(p.stem.replace("_", ":", 1)): p
        for p in sorted(Path(curated_dir).glob("hgnc_*.md"))
    }
    wanted = {normalize_hgnc_id(g) for g in only} if only else None

    pages: list[dict] = []
    rows: list[dict] = []
    for hgnc_id, gene in index.items():
        disorders = gene.entries("disorder")
        hgnc_row = ingest.hgnc.get(hgnc_id)
        symbol = (hgnc_row or {}).get("symbol") or gene.label
        has_page = len(disorders) >= min_disorders or hgnc_id in curated
        summary_path = curated.get(hgnc_id)
        row = {
            "hgnc_id": hgnc_id,
            "symbol": symbol,
            "name": (hgnc_row or {}).get("name", ""),
            "disorder_count": len(disorders),
            "href": gene_page_name(hgnc_id)
            if has_page
            else (f"../disorders/{slugify(disorders[0])}.html" if disorders else ""),
            "has_page": has_page,
            "only_disorder": disorders[0]
            if len(disorders) == 1 and not has_page
            else "",
            "has_function": hgnc_id in ingest.reviews,
            "has_summary": summary_path is not None,
            "summary_state": None,
        }
        if has_page and (wanted is None or hgnc_id in wanted):
            summary = _summary_context(summary_path, verify) if summary_path else None
            row["summary_state"] = summary["state"] if summary else None
            relationship_counts: dict[str, int] = {}
            for name in disorders:
                has_genetic = any(o.section == "genetic" for o in gene.for_entry(name))
                fallback = ["UNTYPED"] if has_genetic else ["NO_GENETIC_RECORD"]
                for rel in gene.relationship_types(name) or fallback:
                    relationship_counts[_prose(rel)] = (
                        relationship_counts.get(_prose(rel), 0) + 1
                    )
            pages.append(
                {
                    "hgnc_id": hgnc_id,
                    "symbol": symbol,
                    "hgnc": hgnc_row,
                    "kb_label": gene.label,
                    "label_differs": bool(hgnc_row) and gene.label != symbol,
                    "xrefs": _xrefs(hgnc_id, hgnc_row),
                    "function": _function_context(hgnc_id, ingest),
                    "summary": summary,
                    "disorders": _disorder_rows(gene),
                    "relationship_counts": sorted(
                        relationship_counts.items(), key=lambda kv: -kv[1]
                    ),
                    "modules": _module_rows(gene),
                    "module_entries": gene.entries("module"),
                    "sources": ingest.sources,
                }
            )
        rows.append(row)
    rows.sort(key=lambda r: (-r["disorder_count"], r["symbol"].casefold()))
    return pages, rows


def render_gene_pages(
    *,
    output_dir: Path = Path("pages/genes"),
    min_disorders: int = 2,
    only: Iterable[str] | None = None,
    verify: bool = True,
    kb_root: Path = Path("kb"),
    ingest_dir: Path = INGEST_DIR,
    curated_dir: Path = CURATED_DIR,
) -> list[Path]:
    from dismech.render import _get_shared_env

    pages, rows = build_gene_contexts(
        kb_root=kb_root,
        ingest_dir=ingest_dir,
        curated_dir=curated_dir,
        min_disorders=min_disorders,
        only=only,
        verify=verify,
    )
    env = _get_shared_env(str(Path(__file__).resolve().parents[1] / "templates"))
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    page_template = env.get_template("gene.html.j2")
    for context in pages:
        path = output_dir / gene_page_name(context["hgnc_id"])
        path.write_text(page_template.render(gene=context), encoding="utf-8")
        written.append(path)
    if only is None:
        expected = {gene_page_name(p["hgnc_id"]) for p in pages}
        for stale in output_dir.glob("hgnc_*.html"):
            if stale.name not in expected:
                stale.unlink()
    index_path = output_dir / "index.html"
    index_path.write_text(
        env.get_template("gene_index.html.j2").render(
            genes=rows,
            min_disorders=min_disorders,
            page_count=sum(r["has_page"] for r in rows),
            summary_count=sum(r["has_summary"] for r in rows),
            function_count=sum(r["has_function"] for r in rows),
        ),
        encoding="utf-8",
    )
    written.append(index_path)
    logger.info("wrote %d gene pages", len(written) - 1)
    return written
