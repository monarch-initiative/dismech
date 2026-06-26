"""MyGeneset / MSigDB gene-set structured source.

Ingests curated **gene-set GO interpretations** from the
``monarch-initiative/genesets`` repository (the ``GeneSetInterpretation``
LinkML records under ``curation/genesets/*.yaml``) and joins **gene
membership** from `mygeneset.info <https://mygeneset.info>`_, then emits one
``MYGENESET_<id>.md`` cache file per gene set.

The body is a deterministic, line-oriented rendering (markdown tables with a
literal ``|`` separator) so curators can quote individual rows as evidence
``snippet:`` values that validate as exact substrings of the cached body:

    GO:0045064 | T-helper 2 cell differentiation | biological_process | core_process | high
    IL4 | NCBIGene:3565

Identifier scheme (see ``projects/GENESETS.md``): the reference id is
``MYGENESET:<_id>`` where ``<_id>`` is the mygeneset.info primary key (the bare
set name, e.g. ``KEGG_ASTHMA``). One generic prefix covers anything in
mygeneset.info, not just MSigDB. The upstream interpretation file's
``gene_set_id`` (``MSIGDB:KEGG_ASTHMA``) is preserved as a cross-reference.

This source is **not** a mechanistic evidence source on its own — gene-set
membership is not mechanism. A curated GO row is a *lead* that should still be
backed by a primary citation, consistent with the DR/NEC anti-hallucination SOP.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar, Iterable, Iterator, Optional

import requests

from dismech.structured_sources.base import (
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)


@dataclass
class _GeneMember:
    symbol: str
    ncbigene: str = ""


@dataclass
class _TermAssoc:
    go_id: str
    label: str
    aspect: str = ""
    category: str = ""
    confidence: str = ""


@dataclass
class _GeneSetRecord:
    """One gene set: curated GO interpretation + membership."""

    local_id: str  # mygeneset _id, e.g. "KEGG_ASTHMA"
    name: str
    gene_set_id: str = ""  # upstream xref, e.g. "MSIGDB:KEGG_ASTHMA"
    source: str = ""  # e.g. "msigdb"
    collection: str = ""
    release: str = ""
    description: str = ""
    # contexts: list of (context_type, term_id, label)
    contexts: list[tuple[str, str, str]] = field(default_factory=list)
    associations: list[_TermAssoc] = field(default_factory=list)
    genes: list[_GeneMember] = field(default_factory=list)


class MyGenesetSource(StructuredSource):
    """Structured-database source for curated gene-set GO interpretations."""

    prefix: ClassVar[str] = "MYGENESET"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^[A-Za-z0-9_.\-]+$")

    # Populated from data/genesets/MANIFEST.yaml via load_manifest().
    _repo: ClassVar[str] = "monarch-initiative/genesets"
    _ref: ClassVar[str] = "main"
    _interpretation_dir: ClassVar[str] = "curation/genesets"
    _mygeneset_base: ClassVar[str] = "https://mygeneset.info/v1"
    _snapshot_date: ClassVar[str] = ""
    _licence: ClassVar[str] = ""

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        """Populate source config from a manifest YAML."""
        from ruamel.yaml import YAML

        yaml = YAML(typ="safe")
        data = yaml.load(manifest_path) or {}
        cls._repo = str(data.get("genesets_repo", cls._repo))
        cls._ref = str(data.get("genesets_ref", cls._ref))
        cls._interpretation_dir = str(
            data.get("interpretation_dir", cls._interpretation_dir)
        )
        cls._mygeneset_base = str(data.get("mygeneset_base", cls._mygeneset_base))
        cls._snapshot_date = str(data.get("snapshot_date", ""))
        cls._licence = str(data.get("licence", ""))

    @property
    def snapshot_date(self) -> str:
        return type(self)._snapshot_date

    # ----- bulk data acquisition (override: multi-file repo + API) -----

    def refresh(self, *, force: bool = False) -> None:
        """Fetch interpretation YAMLs (pinned commit) + mygeneset membership.

        Interpretations land in ``<data_dir>/interpretations/`` and gene
        membership in ``<data_dir>/membership/<id>.json``. Neither is committed
        (see ``.gitignore``); the committed ``references_cache/MYGENESET_*.md``
        files are the durable artifact, and ``MANIFEST.yaml`` is the pin.
        """
        interp_dir = self.data_dir / "interpretations"
        member_dir = self.data_dir / "membership"
        interp_dir.mkdir(parents=True, exist_ok=True)
        member_dir.mkdir(parents=True, exist_ok=True)

        paths = self._list_interpretation_paths()
        logger.info("found %d interpretation files at %s@%s", len(paths), self._repo, self._ref)
        for path in paths:
            name = path.rsplit("/", 1)[-1]
            raw_url = f"https://raw.githubusercontent.com/{self._repo}/{self._ref}/{path}"
            target = interp_dir / name
            if force or not target.exists():
                logger.info("fetch %s", name)
                self._download(raw_url, target)

        # Join membership from mygeneset.info, keyed on each set's local id.
        for yml in sorted(interp_dir.glob("*.yaml")):
            rec = self._parse_interpretation(yml)
            if rec is None:
                continue
            out = member_dir / f"{rec.local_id}.json"
            if not force and out.exists():
                continue
            members = self._fetch_membership(rec.local_id)
            if members is not None:
                out.write_text(json.dumps(members), encoding="utf-8")

    def _list_interpretation_paths(self) -> list[str]:
        """List ``curation/genesets/*.yaml`` paths via the GitHub trees API."""
        api = (
            f"https://api.github.com/repos/{self._repo}/git/trees/"
            f"{self._ref}?recursive=1"
        )
        resp = requests.get(api, timeout=60)
        resp.raise_for_status()
        tree = resp.json().get("tree", [])
        prefix = self._interpretation_dir.rstrip("/") + "/"
        return sorted(
            e["path"]
            for e in tree
            if e.get("type") == "blob"
            and e["path"].startswith(prefix)
            and e["path"].endswith(".yaml")
        )

    def _fetch_membership(self, local_id: str) -> Optional[list[dict]]:
        """Fetch gene membership for one set from mygeneset.info."""
        url = (
            f"{self._mygeneset_base}/geneset/{local_id}"
            "?fields=genes.symbol,genes.ncbigene"
        )
        try:
            resp = requests.get(url, timeout=60)
            if resp.status_code == 404:
                logger.warning("mygeneset: no membership for %s", local_id)
                return []
            resp.raise_for_status()
            genes = resp.json().get("genes") or []
            if isinstance(genes, dict):  # single-gene sets come back unwrapped
                genes = [genes]
            return genes
        except requests.RequestException as exc:  # pragma: no cover - network
            logger.warning("mygeneset fetch failed for %s: %s", local_id, exc)
            return None

    # ----- indexing -----

    def build_index(self) -> dict[str, _GeneSetRecord]:
        interp_dir = self.data_dir / "interpretations"
        member_dir = self.data_dir / "membership"
        records: dict[str, _GeneSetRecord] = {}
        for yml in sorted(interp_dir.glob("*.yaml")):
            rec = self._parse_interpretation(yml)
            if rec is None:
                continue
            mfile = member_dir / f"{rec.local_id}.json"
            if mfile.exists():
                try:
                    members = json.loads(mfile.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    members = []
                rec.genes = [
                    _GeneMember(
                        symbol=str(m.get("symbol", "")),
                        ncbigene=str(m.get("ncbigene", "")),
                    )
                    for m in members
                    if m.get("symbol")
                ]
            records[rec.local_id] = rec
        return records

    @staticmethod
    def local_id_from_gene_set_id(gene_set_id: str) -> str:
        """Strip a ``<SOURCE>:`` prefix to get the mygeneset ``_id``."""
        return gene_set_id.split(":", 1)[1] if ":" in gene_set_id else gene_set_id

    def _parse_interpretation(self, path: Path) -> Optional[_GeneSetRecord]:
        from ruamel.yaml import YAML

        yaml = YAML(typ="safe")
        try:
            data = yaml.load(path) or {}
        except Exception as exc:  # pragma: no cover - malformed upstream file
            logger.warning("could not parse %s: %s", path.name, exc)
            return None
        gene_set_id = str(data.get("gene_set_id", "")).strip()
        name = str(data.get("gene_set_name", "")).strip() or path.stem
        local_id = (
            self.local_id_from_gene_set_id(gene_set_id) if gene_set_id else path.stem
        )
        rec = _GeneSetRecord(
            local_id=local_id,
            name=name,
            gene_set_id=gene_set_id,
            source=gene_set_id.split(":", 1)[0].lower() if ":" in gene_set_id else "",
            collection=str(data.get("collection", "")).strip(),
            release=str(data.get("msigdb_release", "")).strip(),
            description=_collapse(str(data.get("description", ""))),
        )
        for ctx in data.get("contexts", []) or []:
            term = ctx.get("term", {}) or {}
            rec.contexts.append(
                (
                    str(ctx.get("context_type", "")),
                    str(term.get("id", "")),
                    str(term.get("label", "")),
                )
            )
        for assoc in data.get("associations", []) or []:
            term = assoc.get("term", {}) or {}
            if not term.get("id"):
                continue
            rec.associations.append(
                _TermAssoc(
                    go_id=str(term.get("id", "")),
                    label=str(term.get("label", "")),
                    aspect=str(assoc.get("aspect", "")),
                    category=str(assoc.get("category", "")),
                    confidence=str(assoc.get("confidence", "")),
                )
            )
        return rec

    def identifiers(self) -> Iterable[str]:
        return sorted(self.index().keys())

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        for _prefix in ("MYGENESET:", "mygeneset:"):
            if identifier.startswith(_prefix):
                identifier = identifier[len(_prefix):]
                break
        rec = self.index().get(identifier)
        if rec is None:
            raise KeyError(f"MYGENESET:{identifier} not found in gene-set index")
        body = "\n".join(self._render_body(rec)) + "\n"
        return ReferenceCacheEntry(
            reference_id=f"MYGENESET:{rec.local_id}",
            title=rec.name,
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "mygeneset.info"},
        )

    def _render_body(self, rec: _GeneSetRecord) -> Iterator[str]:
        yield f"# MYGENESET:{rec.local_id}  {rec.name}"
        yield ""
        bits = [b for b in (rec.source or None, rec.collection or None) if b]
        suffix = f" ({', '.join(bits)})" if bits else ""
        yield f"**MYGENESET:{rec.local_id}** — {rec.name}{suffix}"
        yield ""

        if rec.description:
            yield "## Description"
            yield ""
            yield rec.description
            yield ""

        if rec.contexts:
            yield "## Context"
            yield ""
            yield from _md_table(
                ["Type", "Term", "Label"],
                [(ct or "-", tid or "-", lbl or "-") for ct, tid, lbl in rec.contexts],
            )
            yield ""

        if rec.associations:
            yield "## Curated GO interpretation"
            yield ""
            yield from _md_table(
                ["GO ID", "Label", "Aspect", "Role", "Confidence"],
                [
                    (
                        a.go_id,
                        a.label or "-",
                        a.aspect or "-",
                        a.category or "-",
                        a.confidence or "-",
                    )
                    for a in rec.associations
                ],
            )
            yield ""

        if rec.genes:
            yield f"## Members ({len(rec.genes)} genes)"
            yield ""
            rows = sorted(rec.genes, key=lambda g: g.symbol)
            yield from _md_table(
                ["Symbol", "NCBI Gene"],
                [
                    (g.symbol, f"NCBIGene:{g.ncbigene}" if g.ncbigene else "-")
                    for g in rows
                ],
            )
            yield ""

        # Provenance footer.
        yield "## Source"
        yield ""
        parts = [
            f"Curated GO interpretation from "
            f"[`{self._repo}`](https://github.com/{self._repo}) "
            f"(`{self._interpretation_dir}/{rec.local_id}.yaml`",
        ]
        footer = parts[0]
        if self._ref:
            footer += f" @ `{self._ref[:12]}`"
        footer += ")."
        yield footer
        if rec.genes:
            yield ""
            yield (
                "Gene membership from "
                "[mygeneset.info](https://mygeneset.info/geneset/"
                f"{rec.local_id})"
                + (f" (source: {rec.source})" if rec.source else "")
                + "."
            )
        if rec.gene_set_id and rec.gene_set_id != f"MYGENESET:{rec.local_id}":
            yield ""
            yield f"Upstream identifier: `{rec.gene_set_id}`."
        if self._licence:
            yield ""
            yield f"Licence: {self._licence}."


# ----- helpers -----


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    """Emit a markdown table; literal-pipe cells are escaped."""

    def _esc(cell: str) -> str:
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"


def _collapse(s: str) -> str:
    """Collapse interior whitespace to a single line for the description block."""
    return re.sub(r"\s+", " ", s).strip()
