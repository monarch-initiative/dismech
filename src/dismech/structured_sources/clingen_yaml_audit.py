"""Audit ClinGen Gene-Disease Validity evidence coverage in disorder YAML."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Iterable, Iterator

from ruamel.yaml import YAML

from dismech.structured_sources.clingen import ClinGenSource

POSITIVE_CLASSIFICATIONS: frozenset[str] = frozenset(
    {"Definitive", "Strong", "Moderate", "Limited"}
)


@dataclass(frozen=True)
class ClinGenYamlAuditRecord:
    """One ClinGen assertion matched to one disorder YAML file."""

    status: str
    disorder_path: str
    assertion_id: str
    gene_symbol: str
    gene_hgnc_id: str
    disease_label: str
    disease_mondo_id: str
    classification: str
    reason: str


@dataclass(frozen=True)
class ClinGenYamlAuditSummary:
    """ClinGen coverage summary for disorder YAML files."""

    positive_assertions: int
    records: tuple[ClinGenYamlAuditRecord, ...]
    cggv_evidence_items: int
    cggv_disease_files: int
    missing_cache_files: tuple[tuple[str, str], ...]
    snippet_not_found_in_cache: tuple[tuple[str, str], ...]

    @property
    def status_counts(self) -> Counter[str]:
        return Counter(record.status for record in self.records)

    @property
    def matched_disease_files(self) -> int:
        return len({record.disorder_path for record in self.records})

    @property
    def matched_primary_mondo_ids(self) -> int:
        return len({record.disease_mondo_id for record in self.records})


@dataclass(frozen=True)
class _GeneticEntry:
    gene_id: str | None
    gene_symbol: str | None
    name: str | None
    refs: frozenset[str]
    snippets: tuple[tuple[str, str | None], ...]


@dataclass(frozen=True)
class _DisorderInfo:
    name: str | None
    preferred_term: str | None
    term_label: str | None
    entry_norms: frozenset[str]
    title_genes: frozenset[str]
    entries: tuple[_GeneticEntry, ...]


def audit_clingen_yaml(
    *,
    kb_dir: Path,
    data_dir: Path,
    cache_dir: Path | None = None,
    classifications: Iterable[str] = POSITIVE_CLASSIFICATIONS,
) -> ClinGenYamlAuditSummary:
    """Classify ClinGen/YAML coverage for primary MONDO matches.

    The audit is intentionally conservative. A ClinGen assertion is considered
    directly actionable only when its MONDO ID matches the YAML entry's primary
    MONDO ID and either the gene entry already exists or the ClinGen disease
    label exactly matches the YAML display/preferred disease label.
    """

    allowed_classifications = set(classifications)
    source = ClinGenSource(data_dir, include_report_text=False)
    rows = [
        row
        for row in source.index().values()
        if row.classification in allowed_classifications
    ]
    known_gene_symbols = frozenset(
        row.gene_symbol for row in rows if _looks_like_gene_symbol(row.gene_symbol)
    )

    files_by_mondo: dict[str, list[str]] = defaultdict(list)
    disorder_info: dict[str, _DisorderInfo] = {}
    for path, data in _iter_disorder_yaml(kb_dir):
        disease_term = data.get("disease_term") or {}
        term = disease_term.get("term") or {}
        mondo_id = term.get("id")
        if not mondo_id:
            continue

        display_path = _display_path(path)
        entries = tuple(_genetic_entries(data))
        title = " ".join(
            value
            for value in (data.get("name"), disease_term.get("preferred_term"))
            if value
        )
        title_genes = frozenset(
            entry.gene_symbol
            for entry in entries
            if entry.gene_symbol and _gene_in_text(entry.gene_symbol, title)
        ) | _gene_symbols_in_text(known_gene_symbols, title)

        files_by_mondo[mondo_id].append(display_path)
        disorder_info[display_path] = _DisorderInfo(
            name=data.get("name"),
            preferred_term=disease_term.get("preferred_term"),
            term_label=term.get("label"),
            entry_norms=frozenset(
                {
                    _normalize_label(data.get("name")),
                    _normalize_label(disease_term.get("preferred_term")),
                }
            ),
            title_genes=title_genes,
            entries=entries,
        )

    records: list[ClinGenYamlAuditRecord] = []
    for row in rows:
        for disorder_path in files_by_mondo.get(row.disease_mondo_id, []):
            info = disorder_info[disorder_path]
            hgnc_id = row.gene_hgnc_id.replace("HGNC:", "hgnc:")
            matches = [
                entry
                for entry in info.entries
                if entry.gene_id == hgnc_id
                or entry.gene_symbol == row.gene_symbol
                or entry.name == row.gene_symbol
            ]
            if matches:
                if any(row.assertion_id in entry.refs for entry in matches):
                    status = "done"
                    reason = "gene entry already cites this ClinGen assertion"
                else:
                    status = "gene_present_missing_ref"
                    reason = (
                        "gene entry exists but does not cite this ClinGen assertion"
                    )
            else:
                label_ok = _normalize_label(row.disease_label) in info.entry_norms
                title_gene_mismatch = bool(
                    info.title_genes and row.gene_symbol not in info.title_genes
                )
                if title_gene_mismatch:
                    status = "blocked_gene_specific_title"
                    reason = (
                        "YAML title/preferred term names "
                        f"{', '.join(sorted(info.title_genes))}, which differs "
                        "from the ClinGen assertion gene"
                    )
                elif not label_ok:
                    status = "blocked_label_mismatch"
                    reason = (
                        "ClinGen disease label does not exactly match the YAML "
                        "display/preferred disease label"
                    )
                else:
                    status = "missing_genetic_entry"
                    reason = "exact disease match lacks a genetic entry for this gene"

            records.append(
                ClinGenYamlAuditRecord(
                    status=status,
                    disorder_path=disorder_path,
                    assertion_id=row.assertion_id,
                    gene_symbol=row.gene_symbol,
                    gene_hgnc_id=row.gene_hgnc_id,
                    disease_label=row.disease_label,
                    disease_mondo_id=row.disease_mondo_id,
                    classification=row.classification,
                    reason=reason,
                )
            )

    cggv_items: list[tuple[str, str, str | None]] = []
    for disorder_path, info in disorder_info.items():
        for entry in info.entries:
            for ref, snippet in entry.snippets:
                cggv_items.append((disorder_path, ref, snippet))

    missing_cache_files: list[tuple[str, str]] = []
    snippet_misses: list[tuple[str, str]] = []
    if cache_dir is not None:
        for disorder_path, ref, snippet in cggv_items:
            cache_path = cache_dir / f"{ref.replace(':', '_')}.md"
            if not cache_path.exists():
                missing_cache_files.append((disorder_path, ref))
                continue
            if snippet and snippet not in cache_path.read_text():
                snippet_misses.append((disorder_path, ref))

    return ClinGenYamlAuditSummary(
        positive_assertions=len(rows),
        records=tuple(records),
        cggv_evidence_items=len(cggv_items),
        cggv_disease_files=len({item[0] for item in cggv_items}),
        missing_cache_files=tuple(missing_cache_files),
        snippet_not_found_in_cache=tuple(snippet_misses),
    )


def format_summary(summary: ClinGenYamlAuditSummary, *, limit: int = 20) -> str:
    """Render a compact human-readable audit summary."""

    lines = [
        "ClinGen YAML coverage audit",
        f"positive valid ClinGen assertions indexed: {summary.positive_assertions}",
        f"primary-MONDO assertion/file matches: {len(summary.records)}",
        f"matched disease files: {summary.matched_disease_files}",
        f"matched primary MONDO IDs: {summary.matched_primary_mondo_ids}",
        "status counts:",
    ]
    for status, count in summary.status_counts.most_common():
        lines.append(f"  {status}: {count}")

    lines.extend(
        [
            f"YAML CGGV evidence items: {summary.cggv_evidence_items}",
            f"YAML CGGV disease files: {summary.cggv_disease_files}",
            f"missing CGGV cache files: {len(summary.missing_cache_files)}",
            (
                "CGGV snippets not found in cache: "
                f"{len(summary.snippet_not_found_in_cache)}"
            ),
        ]
    )

    remaining = [record for record in summary.records if record.status != "done"]
    if remaining and limit != 0:
        lines.append("remaining examples:")
        for disorder_path, count in Counter(
            record.disorder_path for record in remaining
        ).most_common(limit):
            statuses = Counter(
                record.status
                for record in remaining
                if record.disorder_path == disorder_path
            )
            examples = [
                f"{record.gene_symbol}:{record.classification}"
                for record in remaining
                if record.disorder_path == disorder_path
            ][:8]
            lines.append(
                f"  {count}\t{disorder_path}\t{dict(statuses)}\t{', '.join(examples)}"
            )

    return "\n".join(lines)


def format_tsv(
    summary: ClinGenYamlAuditSummary, *, statuses: Iterable[str] | None = None
) -> str:
    """Render assertion/file matches as tab-separated rows."""

    allowed_statuses = set(statuses or [])
    output = StringIO()
    writer = csv.writer(output, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "status",
            "disorder_path",
            "gene_symbol",
            "gene_hgnc_id",
            "disease_label",
            "disease_mondo_id",
            "classification",
            "assertion_id",
            "reason",
        ]
    )
    for record in summary.records:
        if allowed_statuses and record.status not in allowed_statuses:
            continue
        writer.writerow(
            [
                record.status,
                record.disorder_path,
                record.gene_symbol,
                record.gene_hgnc_id,
                record.disease_label,
                record.disease_mondo_id,
                record.classification,
                record.assertion_id,
                record.reason,
            ]
        )
    return output.getvalue().rstrip("\n")


def _iter_disorder_yaml(kb_dir: Path) -> Iterator[tuple[Path, dict]]:
    yaml = YAML(typ="safe")
    for path in sorted(kb_dir.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue
        data = yaml.load(path.read_text()) or {}
        if isinstance(data, dict):
            yield path, data


def _genetic_entries(data: dict) -> Iterator[_GeneticEntry]:
    for item in data.get("genetic") or []:
        if not isinstance(item, dict):
            continue
        gene_term = item.get("gene_term") or {}
        term = gene_term.get("term") or {}
        snippets: list[tuple[str, str | None]] = []
        refs: set[str] = set()
        for node in _walk(item):
            ref = node.get("reference")
            if isinstance(ref, str) and ref.startswith("CGGV:"):
                refs.add(ref)
                snippet = node.get("snippet")
                snippets.append((ref, snippet if isinstance(snippet, str) else None))
        yield _GeneticEntry(
            gene_id=term.get("id"),
            gene_symbol=term.get("label") or gene_term.get("preferred_term"),
            name=item.get("name"),
            refs=frozenset(refs),
            snippets=tuple(snippets),
        )


def _walk(obj: object) -> Iterator[dict]:
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from _walk(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from _walk(value)


def _normalize_label(value: str | None) -> str:
    normalized = (value or "").lower().replace("_", " ")
    normalized = re.sub(r"['’]", "", normalized)
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def _gene_in_text(gene: str, text: str) -> bool:
    return (
        re.search(
            r"(?<![A-Za-z0-9])" + re.escape(gene) + r"(?![A-Za-z0-9])",
            text,
            flags=re.I,
        )
        is not None
    )


def _gene_symbols_in_text(gene_symbols: frozenset[str], text: str) -> frozenset[str]:
    tokens = frozenset(re.findall(r"[A-Za-z0-9]+", text.upper()))
    return frozenset(
        gene_symbol for gene_symbol in gene_symbols if gene_symbol in tokens
    )


def _looks_like_gene_symbol(symbol: str) -> bool:
    return len(symbol) >= 3 or any(char.isdigit() for char in symbol)


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)
