"""The ingest layer of gene pages: what outside sources say about a gene.

Everything this module writes under ``kb/genes/ingest/`` is **dropped and
reloaded** from pinned upstream snapshots; nothing there is edited by hand.
Two sources, each pinned in ``data/<source>/MANIFEST.yaml``:

* **HGNC** complete set: identity (symbol, name, locus type, location, previous
  symbols, cross-references). Pinned by sha256, like the Orphanet and ClinGen
  bulk files.
* **ai-gene-review** (``ai4curation/ai-gene-review``): the gene's normal
  function, as a prose description plus ``core_functions`` bound to GO. Pinned
  by commit. Joined to HGNC on the **UniProt accession** the review is keyed
  on, never on the folder's symbol, because symbols are renamed (GBA -> GBA1)
  and a symbol join silently pairs the wrong records.

Only genes some KB entry names (see :mod:`dismech.genes.slice`) are written,
so the committed tables track the KB rather than all 45,000 HGNC genes.

The output is plain TSV so a curated summary can query it from DuckDB or
Python under provedown, and so a reload is a reviewable line diff.
"""

from __future__ import annotations

import csv
import json
import logging
import re
import subprocess
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import yaml

from dismech.genes.slice import build_gene_index, normalize_hgnc_id
from dismech.structured_sources.base import (
    ChecksumChange,
    ChecksumMismatchError,
    StructuredSource,
    _sha256_of,
    repin_manifest,
)

logger = logging.getLogger(__name__)

HGNC_DIR = Path("data/hgnc")
AGR_DIR = Path("data/ai-gene-review")
INGEST_DIR = Path("kb/genes/ingest")
SOURCES_FILE = "sources.json"

#: HGNC columns carried into ``hgnc.tsv``, in output order.
HGNC_COLUMNS: tuple[str, ...] = (
    "hgnc_id",
    "symbol",
    "name",
    "locus_group",
    "locus_type",
    "location",
    "alias_symbol",
    "prev_symbol",
    "gene_group",
    "entrez_id",
    "ensembl_gene_id",
    "uniprot_ids",
    "omim_id",
    "mane_select",
)

AGR_COLUMNS: tuple[str, ...] = (
    "hgnc_id",
    "symbol",
    "uniprot_id",
    "review_symbol",
    "status",
    "description",
    "review_path",
)

AGR_FUNCTION_COLUMNS: tuple[str, ...] = (
    "hgnc_id",
    "symbol",
    "function_index",
    "description",
)

AGR_FUNCTION_TERM_COLUMNS: tuple[str, ...] = (
    "hgnc_id",
    "symbol",
    "function_index",
    "relation",
    "term_id",
    "term_label",
)

#: ``core_functions[]`` keys that carry GO (or other) terms, and the relation
#: name each gets in the long table. Order is the output order within a function.
_FUNCTION_TERM_KEYS: tuple[str, ...] = (
    "molecular_function",
    "contributes_to_molecular_function",
    "directly_involved_in",
    "locations",
    "in_complex",
    "anatomical_locations",
    "substrates",
)


# ---------------------------------------------------------------------------
# manifests


def _load_manifest(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _write_manifest_fields(path: Path, updates: dict[str, str]) -> None:
    """Round-trip edit so the manifest's comments survive."""
    from ruamel.yaml import YAML

    ry = YAML()
    ry.preserve_quotes = True
    ry.indent(mapping=2, sequence=4, offset=2)
    ry.width = 4096
    data = ry.load(path)
    for key, value in updates.items():
        data[key] = value
    ry.dump(data, path)


# ---------------------------------------------------------------------------
# refresh


def refresh_hgnc(
    data_dir: Path = HGNC_DIR, *, force: bool = False, repin: bool = False
) -> list[str]:
    """Download the pinned HGNC file; with ``repin`` accept a new upstream release."""
    manifest_path = data_dir / "MANIFEST.yaml"
    manifest = _load_manifest(manifest_path)
    changes: list[ChecksumChange] = []
    for entry in manifest.get("bulk_files") or ():
        target = data_dir / entry["name"]
        if not force and target.exists() and _sha256_of(target) == entry.get("sha256"):
            logger.info("OK  %s", entry["name"])
            continue
        logger.info("downloading %s", entry["url"])
        StructuredSource._download(entry["url"], target)
        actual = _sha256_of(target)
        if entry.get("sha256") and actual != entry["sha256"]:
            if not repin:
                raise ChecksumMismatchError(
                    name=entry["name"],
                    url=entry["url"],
                    expected=entry["sha256"],
                    actual=actual,
                )
            changes.append(
                ChecksumChange(
                    name=entry["name"],
                    old_sha256=entry["sha256"],
                    new_sha256=actual,
                    size_bytes=target.stat().st_size,
                )
            )
    return repin_manifest(manifest_path, changes) if changes else []


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def refresh_ai_gene_review(
    data_dir: Path = AGR_DIR, *, repin: bool = False
) -> list[str]:
    """Sparse-check-out the review files at the pinned commit.

    With ``repin`` the pin moves to the current head of the manifest's branch
    and the manifest is rewritten, leaving a one-line diff to review.
    """
    manifest_path = data_dir / "MANIFEST.yaml"
    manifest = _load_manifest(manifest_path)
    repo = data_dir / "repo"
    if not (repo / ".git").exists():
        repo.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        _git(repo, "remote", "add", "origin", manifest["repository"])
    _git(repo, "sparse-checkout", "set", "--no-cone", f"/{manifest['review_glob']}")

    commit = str(manifest["commit"])
    notes: list[str] = []
    if repin:
        head = _git(
            repo, "ls-remote", "origin", f"refs/heads/{manifest['branch']}"
        ).split()[0]
        if head != commit:
            today = datetime.now(UTC).strftime("%Y-%m-%d")
            _write_manifest_fields(
                manifest_path, {"commit": head, "snapshot_date": today}
            )
            notes.append(f"commit: {commit[:12]} -> {head[:12]}")
            notes.append(f"snapshot_date: {manifest.get('snapshot_date')} -> {today}")
            commit = head
    _git(repo, "fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", commit)
    _git(repo, "checkout", "-q", "--detach", commit)
    return notes


# ---------------------------------------------------------------------------
# build


def _clean(value: object) -> str:
    """One-line, tab-free text for a TSV cell."""
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def read_hgnc(path: Path) -> dict[str, dict[str, str]]:
    """``{hgnc:<n>: row}`` from the HGNC complete-set TSV."""
    rows: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            hgnc_id = normalize_hgnc_id(row.get("hgnc_id"))
            if hgnc_id:
                rows[hgnc_id] = row
    return rows


@dataclass(frozen=True)
class GeneReview:
    uniprot_id: str
    symbol: str
    status: str
    description: str
    core_functions: list[dict]
    path: str


def read_ai_gene_reviews(repo: Path, review_glob: str) -> list[GeneReview]:
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    reviews: list[GeneReview] = []
    for path in sorted(repo.glob(review_glob)):
        with path.open(encoding="utf-8") as fh:
            doc = yaml.load(fh, Loader=loader) or {}
        uniprot = str(doc.get("id") or "").strip()
        if not uniprot:
            continue
        reviews.append(
            GeneReview(
                uniprot_id=uniprot,
                symbol=str(doc.get("gene_symbol") or path.parent.name),
                status=str(doc.get("status") or ""),
                description=str(doc.get("description") or ""),
                core_functions=[
                    cf for cf in doc.get("core_functions") or () if isinstance(cf, dict)
                ],
                path=path.relative_to(repo).as_posix(),
            )
        )
    return reviews


def _hgnc_sort_key(hgnc_id: str) -> int:
    return int(hgnc_id.split(":", 1)[1])


def _function_term_rows(
    hgnc_id: str, symbol: str, index: int, function: dict
) -> Iterable[dict]:
    for relation in _FUNCTION_TERM_KEYS:
        value = function.get(relation)
        terms = value if isinstance(value, list) else [value]
        for term in terms:
            if isinstance(term, dict) and term.get("id"):
                yield {
                    "hgnc_id": hgnc_id,
                    "symbol": symbol,
                    "function_index": str(index),
                    "relation": relation,
                    "term_id": _clean(term.get("id")),
                    "term_label": _clean(term.get("label")),
                }


def _write_tsv(path: Path, columns: Iterable[str], rows: Iterable[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=list(columns),
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({k: _clean(row.get(k)) for k in columns})
            count += 1
    tmp.replace(path)
    return count


@dataclass
class BuildReport:
    kb_genes: int = 0
    hgnc_rows: int = 0
    hgnc_missing: list[str] | None = None
    reviews_matched: int = 0
    reviews_symbol_only: list[str] | None = None
    function_rows: int = 0
    function_term_rows: int = 0

    def lines(self) -> list[str]:
        out = [
            f"KB genes:                         {self.kb_genes}",
            f"hgnc.tsv rows:                    {self.hgnc_rows}",
            f"KB genes absent from HGNC set:    {len(self.hgnc_missing or [])}",
            f"ai-gene-review matched (UniProt): {self.reviews_matched}",
            f"  symbol matches, UniProt does not: {len(self.reviews_symbol_only or [])}",
            f"core functions:                   {self.function_rows}",
            f"core-function term rows:          {self.function_term_rows}",
        ]
        if self.hgnc_missing:
            out.append("  absent: " + ", ".join(self.hgnc_missing[:20]))
        if self.reviews_symbol_only:
            out.append("  symbol-only: " + ", ".join(self.reviews_symbol_only[:20]))
        return out


def build_ingest(
    *,
    kb_root: Path = Path("kb"),
    hgnc_dir: Path = HGNC_DIR,
    agr_dir: Path = AGR_DIR,
    out_dir: Path = INGEST_DIR,
    gene_ids: Iterable[str] | None = None,
) -> BuildReport:
    """Write ``kb/genes/ingest/*.tsv`` for every gene the KB names."""
    report = BuildReport()
    wanted = sorted(
        {normalize_hgnc_id(g) for g in (gene_ids or build_gene_index(kb_root))}
        - {None},
        key=_hgnc_sort_key,
    )
    report.kb_genes = len(wanted)

    hgnc_manifest = _load_manifest(hgnc_dir / "MANIFEST.yaml")
    hgnc_file = hgnc_dir / hgnc_manifest["bulk_files"][0]["name"]
    hgnc = read_hgnc(hgnc_file)
    hgnc_rows = []
    missing = []
    for hgnc_id in wanted:
        row = hgnc.get(hgnc_id)
        if row is None:
            missing.append(hgnc_id)
            continue
        hgnc_rows.append({**row, "hgnc_id": hgnc_id})
    report.hgnc_missing = missing
    report.hgnc_rows = _write_tsv(out_dir / "hgnc.tsv", HGNC_COLUMNS, hgnc_rows)

    agr_manifest = _load_manifest(agr_dir / "MANIFEST.yaml")
    reviews = read_ai_gene_reviews(agr_dir / "repo", agr_manifest["review_glob"])
    by_uniprot = {r.uniprot_id: r for r in reviews}
    by_symbol = {r.symbol: r for r in reviews}
    review_rows: list[dict] = []
    function_rows: list[dict] = []
    term_rows: list[dict] = []
    symbol_only: list[str] = []
    for row in hgnc_rows:
        uniprots = [u for u in (row.get("uniprot_ids") or "").split("|") if u]
        review = next((by_uniprot[u] for u in uniprots if u in by_uniprot), None)
        if review is None:
            if row["symbol"] in by_symbol:
                symbol_only.append(row["symbol"])
            continue
        review_rows.append(
            {
                "hgnc_id": row["hgnc_id"],
                "symbol": row["symbol"],
                "uniprot_id": review.uniprot_id,
                "review_symbol": review.symbol,
                "status": review.status,
                "description": review.description,
                "review_path": review.path,
            }
        )
        for index, function in enumerate(review.core_functions, start=1):
            function_rows.append(
                {
                    "hgnc_id": row["hgnc_id"],
                    "symbol": row["symbol"],
                    "function_index": str(index),
                    "description": function.get("description"),
                }
            )
            term_rows.extend(
                _function_term_rows(row["hgnc_id"], row["symbol"], index, function)
            )
    report.reviews_matched = _write_tsv(
        out_dir / "ai_gene_review.tsv", AGR_COLUMNS, review_rows
    )
    report.reviews_symbol_only = symbol_only
    report.function_rows = _write_tsv(
        out_dir / "ai_gene_review_core_functions.tsv",
        AGR_FUNCTION_COLUMNS,
        function_rows,
    )
    report.function_term_rows = _write_tsv(
        out_dir / "ai_gene_review_core_function_terms.tsv",
        AGR_FUNCTION_TERM_COLUMNS,
        term_rows,
    )

    sources = {
        "hgnc": {
            "snapshot_date": str(hgnc_manifest.get("snapshot_date")),
            "sha256": hgnc_manifest["bulk_files"][0]["sha256"],
        },
        "ai-gene-review": {
            "snapshot_date": str(agr_manifest.get("snapshot_date")),
            "commit": agr_manifest["commit"],
            "repository": agr_manifest["repository"],
            "web_base": agr_manifest.get("web_base"),
        },
    }
    # JSON rather than YAML so the whole-KB YAML sweeps (duplicate keys, enum
    # values, titles) never mistake this provenance record for KB content.
    sources["generated_by"] = (
        "just genes-ingest-build; every file in this directory is dropped and "
        "reloaded from the pins in data/hgnc/ and data/ai-gene-review/"
    )
    (out_dir / SOURCES_FILE).write_text(
        json.dumps(sources, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


# ---------------------------------------------------------------------------
# readers used by the renderer and by curated summaries


def _read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


@dataclass
class IngestTables:
    hgnc: dict[str, dict[str, str]]
    reviews: dict[str, dict[str, str]]
    functions: dict[str, list[dict]]
    sources: dict


def load_ingest(out_dir: Path = INGEST_DIR) -> IngestTables:
    """The committed ingest tables, keyed on ``hgnc:<n>``; empty if not built."""
    # {hgnc_id: [{"index", "description", "terms": {relation: [(id, label)]}}]}
    functions: dict[str, list[dict]] = {}
    by_key: dict[tuple[str, str], dict] = {}
    for row in _read_tsv(out_dir / "ai_gene_review_core_functions.tsv"):
        function = {
            "index": row["function_index"],
            "description": row["description"],
            "terms": {},
        }
        functions.setdefault(row["hgnc_id"], []).append(function)
        by_key[(row["hgnc_id"], row["function_index"])] = function
    for row in _read_tsv(out_dir / "ai_gene_review_core_function_terms.tsv"):
        function = by_key.get((row["hgnc_id"], row["function_index"]))
        if function is not None:
            function["terms"].setdefault(row["relation"], []).append(
                (row["term_id"], row["term_label"])
            )
    sources_path = out_dir / SOURCES_FILE
    sources = (
        json.loads(sources_path.read_text(encoding="utf-8"))
        if sources_path.exists()
        else {}
    )
    return IngestTables(
        hgnc={r["hgnc_id"]: r for r in _read_tsv(out_dir / "hgnc.tsv")},
        reviews={r["hgnc_id"]: r for r in _read_tsv(out_dir / "ai_gene_review.tsv")},
        functions=functions,
        sources=sources or {},
    )
