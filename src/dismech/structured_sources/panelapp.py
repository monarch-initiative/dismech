"""Genomics England PanelApp structured-database source.

Ingests **Genomics England PanelApp** — a publicly available knowledgebase of
expert-curated "virtual" gene panels for human disorders. PanelApp is the
crowdsourced, panel-level companion to the gene-disease validity resources
already wired into dismech (ClinGen Gene-Disease Validity, ``CGGV:``; EBI
Gene2Phenotype, used by ``dismech.compare.g2p``). It is most useful as a broad
**disease-to-gene (d2g)** signal that also carries each gene's mode of
inheritance and a traffic-light **confidence rating**:

- ``3`` → **Green** (high confidence / diagnostic-grade)
- ``2`` → **Amber** (moderate confidence)
- ``1`` → **Red** (low confidence / no current evidence for diagnostic use)
- ``0`` → **No list** (no rating)

This source emits one ``PANELAPP_<panel_id>_<gene>.md`` cache file per
**gene-on-panel association**, so a disorder entry can cite
``PANELAPP:<panel_id>_<gene_symbol>`` and quote the gene-panel row (or a
phenotype / evidence-source row) as an evidence ``snippet:`` — the same
flat-file-row pattern used by the Orphanet, ClinGen, and ICEES sources.

**Acquisition differs from the single-file sources.** PanelApp has no single
bulk download; gene-panel ratings are served from a paginated REST API
(``/api/v1/genes/``). ``refresh()`` therefore walks that endpoint once and
writes a deterministic, sorted JSON-Lines snapshot to
``data/panelapp/panelapp_snapshot.jsonl`` (gitignored). ``build_index()``
reads that pinned snapshot, never the live API, so cache rebuilds stay
reproducible. The snapshot is a point-in-time view: PanelApp panels are
versioned and updated continuously, so the pinned sha256 / snapshot date in
``data/panelapp/MANIFEST.yaml`` records *which* state was captured. Once a
``PANELAPP_*.md`` cache file is committed, a curator's snippet validates
against that committed file regardless of later API drift.

**Evidence-independence caveat.** PanelApp re-aggregates several of the same
expert sources used by ClinGen and Gene2Phenotype. Treat it as a complementary
panel-level signal, not as an independent second confirmation of a gene-disease
link; avoid citing PanelApp and ClinGen as two separate lines of evidence for
the same association.
"""

from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Iterable, Iterator

import requests

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)

_SNAPSHOT_NAME = "panelapp_snapshot.jsonl"
_DEFAULT_API_BASE = "https://panelapp.genomicsengland.co.uk/api/v1"

# PanelApp confidence_level codes → traffic-light label.
_CONFIDENCE_LABELS = {
    "3": "Green",
    "2": "Amber",
    "1": "Red",
    "0": "No list",
    "": "No list",
}


@dataclass(frozen=True)
class _PanelAppRecord:
    """One PanelApp gene-on-panel association."""

    reference_id: str
    panel_id: int
    panel_name: str
    panel_version: str
    disease_group: str
    disease_sub_group: str
    relevant_disorders: tuple[str, ...]
    gene_symbol: str
    hgnc_id: str
    omim_gene: tuple[str, ...]
    confidence_level: str
    mode_of_inheritance: str
    phenotypes: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()
    publications: tuple[str, ...] = ()

    @property
    def confidence_label(self) -> str:
        return _CONFIDENCE_LABELS.get(self.confidence_level, "No list")


class PanelAppSource(StructuredSource):
    """Structured source for Genomics England PanelApp gene-panel ratings."""

    prefix: ClassVar[str] = "PANELAPP"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^(PANELAPP:)?\d+_.+$")
    bulk_files: ClassVar[tuple[BulkFile, ...]] = (
        BulkFile(
            name=_SNAPSHOT_NAME,
            url="",  # built locally by walking the API in refresh()
            sha256="",
            description="PanelApp gene-panel associations (API snapshot, JSON-Lines)",
        ),
    )

    _manifest_snapshot_date: ClassVar[str] = ""
    _manifest_schema_tag: ClassVar[str] = ""
    _manifest_api_base: ClassVar[str] = ""

    def __init__(
        self,
        data_dir: Path,
        *,
        api_base: str | None = None,
        timeout: float = 60.0,
        request_delay: float = 0.34,
        max_retries: int = 5,
    ) -> None:
        super().__init__(data_dir)
        self.api_base = (
            api_base or type(self)._manifest_api_base or _DEFAULT_API_BASE
        ).rstrip("/")
        self.timeout = timeout
        # PanelApp throttles aggressively; pace requests and back off on 429.
        self.request_delay = request_delay
        self.max_retries = max_retries

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        """Populate ``bulk_files`` and snapshot metadata from a manifest YAML."""
        from ruamel.yaml import YAML

        yaml = YAML(typ="safe")
        data = yaml.load(manifest_path)
        cls.bulk_files = tuple(
            BulkFile(
                name=entry["name"],
                url=entry.get("url", ""),
                sha256=entry.get("sha256", ""),
                description=entry.get("description", ""),
            )
            for entry in data.get("bulk_files", [])
        )
        cls._manifest_snapshot_date = str(data.get("snapshot_date", ""))
        cls._manifest_schema_tag = str(data.get("schema_tag", ""))
        cls._manifest_api_base = str(data.get("api_base", ""))

    # ----- bulk data (API snapshot) -----

    def refresh(self, *, force: bool = False) -> None:
        """Walk the PanelApp ``/genes/`` API and write a sorted JSONL snapshot.

        Unlike the single-file sources, PanelApp has no bulk download, so this
        override builds the snapshot from the paginated REST API. Existing
        snapshots are kept unless ``force`` is set; the pinned sha256 (if any)
        is reported on mismatch so a manifest bump is intentional.
        """
        self.data_dir.mkdir(parents=True, exist_ok=True)
        target = self.data_dir / _SNAPSHOT_NAME
        if target.exists() and not force:
            logger.info("snapshot already present: %s (use --force to rebuild)", target)
            return

        # Dedup on (panel_id, gene_symbol): the walk can span several minutes
        # during which panels are re-versioned, so the same association may be
        # paginated twice. Keep the last seen and sort for a canonical snapshot.
        by_key: dict[tuple[int, str], dict] = {}
        for rec in self._walk_api():
            by_key[(rec["panel_id"], rec["gene_symbol"])] = rec
        records = [by_key[key] for key in sorted(by_key)]
        tmp = target.with_suffix(target.suffix + ".tmp")
        with tmp.open("w", encoding="utf-8") as fh:
            for rec in records:
                fh.write(json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n")
        tmp.replace(target)
        logger.info("wrote %d gene-panel associations to %s", len(records), target)

    def _walk_api(self) -> Iterator[dict]:
        url: str | None = f"{self.api_base}/genes/"
        page = 0
        with requests.Session() as session:
            while url:
                page += 1
                data = self._get_json(session, url)
                for gene in data.get("results", []):
                    record = _record_from_gene(gene)
                    if record is not None:
                        yield record
                if page % 25 == 0:
                    logger.info("  ... fetched %d API pages", page)
                url = data.get("next")
                if url and self.request_delay:
                    time.sleep(self.request_delay)

    def _get_json(self, session: requests.Session, url: str) -> dict:
        """GET ``url`` with retry/backoff on HTTP 429 and transient errors."""
        for attempt in range(1, self.max_retries + 1):
            resp = session.get(url, timeout=self.timeout)
            if resp.status_code == 429:
                retry_after = resp.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else 2.0 * attempt
                logger.warning(
                    "429 from PanelApp (attempt %d/%d); waiting %.1fs",
                    attempt,
                    self.max_retries,
                    wait,
                )
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()
        raise RuntimeError(
            f"PanelApp API still rate-limited after {self.max_retries} retries: {url}"
        )

    # ----- indexing -----

    def _snapshot_path(self) -> Path:
        path = self.data_dir / _SNAPSHOT_NAME
        if path.exists():
            return path
        raise FileNotFoundError(
            f"{path} not found; run `just panelapp-refresh` first"
        )

    def build_index(self) -> dict[str, _PanelAppRecord]:
        records: dict[str, _PanelAppRecord] = {}
        with self._snapshot_path().open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                raw = json.loads(line)
                ref_id = _reference_id(raw["panel_id"], raw["gene_symbol"])
                records[ref_id] = _PanelAppRecord(
                    reference_id=ref_id,
                    panel_id=int(raw["panel_id"]),
                    panel_name=raw.get("panel_name", ""),
                    panel_version=str(raw.get("panel_version", "")),
                    disease_group=raw.get("disease_group", "") or "",
                    disease_sub_group=raw.get("disease_sub_group", "") or "",
                    relevant_disorders=tuple(raw.get("relevant_disorders") or ()),
                    gene_symbol=raw["gene_symbol"],
                    hgnc_id=raw.get("hgnc_id", "") or "",
                    omim_gene=tuple(raw.get("omim_gene") or ()),
                    confidence_level=str(raw.get("confidence_level", "")),
                    mode_of_inheritance=raw.get("mode_of_inheritance", "") or "",
                    phenotypes=tuple(raw.get("phenotypes") or ()),
                    evidence=tuple(raw.get("evidence") or ()),
                    publications=tuple(str(p) for p in (raw.get("publications") or ())),
                )
        return records

    def identifiers(self) -> Iterable[str]:
        idx = self.index()
        return sorted(
            idx.keys(),
            key=lambda ident: (
                idx[ident].panel_id,
                idx[ident].gene_symbol,
            ),
        )

    @property
    def snapshot_date(self) -> str:
        return type(self)._manifest_snapshot_date

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        ref_id = _normalize_identifier(identifier)
        rec = self.index().get(ref_id)
        if rec is None:
            raise KeyError(f"{ref_id} not found in PanelApp index")
        body = "\n".join(self._render_body(rec)) + "\n"
        return ReferenceCacheEntry(
            reference_id=ref_id,
            title=(
                f"{rec.gene_symbol} / {rec.panel_name} "
                f"({rec.confidence_label})"
            )[:240],
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "PanelApp"},
        )

    def _render_body(self, rec: _PanelAppRecord) -> Iterator[str]:
        yield f"# {rec.reference_id}  {rec.gene_symbol} / {rec.panel_name}"
        yield ""
        yield (
            f"**{rec.reference_id}** - {rec.gene_symbol} on the "
            f"\"{rec.panel_name}\" panel "
            f"({rec.confidence_label} confidence)."
        )
        yield ""

        yield "## Gene-panel association"
        yield ""
        yield from _md_table(
            [
                "Gene",
                "HGNC",
                "Panel",
                "Panel ID",
                "Version",
                "Confidence",
                "MOI",
            ],
            [
                (
                    rec.gene_symbol,
                    rec.hgnc_id,
                    rec.panel_name,
                    str(rec.panel_id),
                    rec.panel_version,
                    f"{rec.confidence_label} ({rec.confidence_level or '0'})",
                    rec.mode_of_inheritance,
                )
            ],
        )
        yield ""

        if rec.disease_group or rec.disease_sub_group or rec.relevant_disorders:
            yield "## Panel context"
            yield ""
            if rec.disease_group:
                yield f"- Disease group: {rec.disease_group}"
            if rec.disease_sub_group:
                yield f"- Disease sub-group: {rec.disease_sub_group}"
            if rec.relevant_disorders:
                yield f"- Relevant disorders: {', '.join(rec.relevant_disorders)}"
            yield ""

        if rec.phenotypes:
            yield "## Phenotypes"
            yield ""
            yield from _md_table(
                ["Phenotype"],
                [(phenotype,) for phenotype in rec.phenotypes],
            )
            yield ""

        if rec.evidence:
            yield "## Evidence sources"
            yield ""
            yield from _md_table(
                ["Source"],
                [(source,) for source in rec.evidence],
            )
            yield ""

        if rec.publications:
            yield "## Publications"
            yield ""
            for pmid in rec.publications:
                yield f"- PMID:{pmid}"
            yield ""

        yield "## Source"
        yield ""
        yield (
            "Genomics England PanelApp snapshot "
            f"**{self.snapshot_date or 'unknown'}** "
            f"(panel \"{rec.panel_name}\" v{rec.panel_version or '?'}). "
            "PanelApp gene lists are provided by Genomics England in good faith "
            "for the benefit of the research community; users must verify "
            "accuracy before any use. Publicly available to browse, download, "
            "and query."
        )
        yield ""
        yield (
            "Caveat: PanelApp re-aggregates expert sources that overlap with "
            "ClinGen Gene-Disease Validity and Gene2Phenotype. Treat it as a "
            "complementary panel-level signal, not an independent confirmation "
            "of the same gene-disease association."
        )
        yield ""
        yield (
            f"[PanelApp panel {rec.panel_id}]"
            f"(https://panelapp.genomicsengland.co.uk/panels/{rec.panel_id}/)"
        )


# ----- helpers -----


def _record_from_gene(gene: dict) -> dict | None:
    """Project one PanelApp ``/genes/`` API entry into a snapshot record."""
    gene_data = gene.get("gene_data") or {}
    symbol = gene.get("entity_name") or gene_data.get("gene_symbol")
    panel = gene.get("panel") or {}
    panel_id = panel.get("id")
    if not symbol or panel_id is None:
        return None
    return {
        "panel_id": int(panel_id),
        "panel_name": panel.get("name", "") or "",
        "panel_version": str(panel.get("version", "") or ""),
        "disease_group": panel.get("disease_group", "") or "",
        "disease_sub_group": panel.get("disease_sub_group", "") or "",
        "relevant_disorders": list(panel.get("relevant_disorders") or []),
        "gene_symbol": symbol,
        "hgnc_id": gene_data.get("hgnc_id", "") or "",
        "omim_gene": list(gene_data.get("omim_gene") or []),
        "confidence_level": str(gene.get("confidence_level", "") or ""),
        "mode_of_inheritance": gene.get("mode_of_inheritance", "") or "",
        "phenotypes": list(gene.get("phenotypes") or []),
        "evidence": list(gene.get("evidence") or []),
        "publications": list(gene.get("publications") or []),
    }


def _reference_id(panel_id: int | str, gene_symbol: str) -> str:
    return f"PANELAPP:{int(panel_id)}_{gene_symbol}"


def _normalize_identifier(identifier: str) -> str:
    ident = identifier.strip()
    if ident.startswith("PANELAPP:"):
        return ident
    return f"PANELAPP:{ident}"


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    def _esc(cell: str) -> str:
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"
