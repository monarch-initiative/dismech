"""ToxCast/Tox21 assay-endpoint annotations from EPA's CTX API.

An **assay endpoint** is one measurement ToxCast makes: a named readout, in a
named system, aimed at a named molecular target. This module fetches EPA's
descriptions of those endpoints and caches them locally so the corpus can be
analysed offline.

It deliberately handles **only the assay metadata** — what an assay measures.
Chemical results, the hit-calls and potencies saying which chemicals were active
in which assay, are a separate question deferred to issue #12682. See #12858 for
why the two were split: an assay's biological attributes are what could map an
assay to a dismech pathograph node, and that mapping does not depend on any
chemical having been tested.

Why this is not a `StructuredSource`
------------------------------------
The eleven sources under ``structured_sources/`` exist to emit
``references_cache/`` files that a curator cites and quotes. This module emits
none: it caches EPA's endpoint descriptions under ``data/toxcast/`` as an input
to analysis, and nothing here is citable evidence. Subclassing
``StructuredSource`` would promise a cache-file contract it does not implement.

The seven field groups
----------------------
:class:`AssayEndpoint` carries the fields #12858 identifies as defining an
endpoint's biological attributes, and each constrains a different thing:

============================  ===============================================
``genes``                     the molecular target, with identifiers
``target_type`` / ``_sub``    what kind of thing the target is
``target_family`` / ``_sub``  the target's class
``biological_process``        the process being read
``organism``/``tissue``/      the system it was measured in
``cell``
``function_type``             the method, and so the limitation
``signal_direction``          which way a hit reads
============================  ===============================================

Requires ``CTX_API_KEY``. See the ``epa-ctx-api`` skill for the endpoint map and
the response quirks that make a naive read wrong.
"""

from __future__ import annotations

import json
import logging
import os
import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx

logger = logging.getLogger(__name__)

#: Live CTX API base. EPA's own documentation still links `api-ccte.epa.gov`,
#: which no longer resolves; this host is the one EPA's `ctx-python` client uses.
API_BASE = "https://comptox.epa.gov/ctx-api"

#: Environment variable holding the free individual API key, requested from
#: `ccte_api@epa.gov`. Every data path returns 401 without it.
API_KEY_ENV = "CTX_API_KEY"

#: All endpoint annotations in one response. There is no paged form.
ANNOTATIONS_PATH = "bioactivity/assay/"

#: One endpoint's annotation, for a per-claim lookup.
ANNOTATION_BY_AEID_PATH = "bioactivity/assay/search/by-aeid/{aeid}"

ANNOTATIONS_FILE = "assay_annotations.json"
MANIFEST_FILE = "MANIFEST.yaml"


class MissingAPIKey(RuntimeError):
    """Raised when no CTX API key is available."""

    def __init__(self) -> None:
        super().__init__(
            f"no EPA CTX API key: set {API_KEY_ENV}.\n"
            "A free individual key is requested by emailing ccte_api@epa.gov "
            "with your name, email and organization; it is issued by hand, so "
            "allow a day or two.\n"
            "Export it where every shell and `just` recipe inherits it, e.g. in "
            f'~/.zshenv:\n    export {API_KEY_ENV}="..."\n'
            "Never write the key into a file under the repository."
        )


class AnnotationsMissing(RuntimeError):
    """Raised when the cached annotations have not been fetched."""

    def __init__(self, path: Path) -> None:
        super().__init__(
            f"no cached assay annotations at {path}.\n"
            "Fetch them with:\n    just toxcast-refresh"
        )


@dataclass(frozen=True)
class GeneTarget:
    """One gene an assay endpoint declares as its intended target.

    Carries the identifiers as well as the symbol, because a bare symbol is not
    a stable key: it is species-specific, and 41 endpoints name more than one
    gene. Dismech binds genes to HGNC, which neither identifier here is, so a
    mapping step is needed rather than a copy.
    """

    symbol: str
    full_name: str = ""
    entrez_gene_id: int | None = None
    uniprot_accession: str = ""


@dataclass(frozen=True)
class AssayEndpoint:
    """One ToxCast/Tox21 assay endpoint's biological attributes."""

    aeid: int
    name: str

    #: The molecular target. Empty on roughly a third of endpoints, and the gaps
    #: are not where intuition puts them, so absence is a real state rather than
    #: a parsing failure.
    genes: tuple[GeneTarget, ...] = ()

    #: What kind of thing the target is, e.g. protein / receptor.
    target_type: str = ""
    target_type_sub: str = ""

    #: The target's class, e.g. nuclear receptor / steroidal.
    target_family: str = ""
    target_family_sub: str = ""

    #: The process being read, e.g. regulation of transcription factor activity.
    #: A small closed vocabulary, and the candidate bridge to GO that #12858
    #: asks to evaluate.
    biological_process: str = ""

    #: The system the measurement was made in.
    organism: str = ""
    tissue: str = ""
    cell: str = ""

    #: The method, and so the limitation: binding is not a cellular response.
    function_type: str = ""

    #: Which way a hit reads: gain, loss, bidirectional.
    signal_direction: str = ""

    #: True for a cell-viability counter-screen, where a hit is cytotoxicity
    #: rather than activity at the intended target.
    is_viability: bool = False

    #: Whether the assay is cell-based, biochemical, cell-free or an organism.
    #: Relevant because `experimental_model_type` in dismech has no value for a
    #: non-cell-based assay, which is an open question on #12858.
    format_type: str = ""

    #: The laboratory or program that ran it, e.g. TOX21, NVS, ATG.
    source_name: str = ""

    #: PMIDs for the assay's own publications, so a mapping can cite the method.
    citation_pmids: tuple[int, ...] = ()

    @property
    def gene_symbols(self) -> tuple[str, ...]:
        return tuple(g.symbol for g in self.genes)

    @property
    def gene_label(self) -> str:
        return ";".join(self.gene_symbols) if self.genes else "-"

    @property
    def is_human(self) -> bool:
        return self.organism.strip().lower() == "human"


@dataclass
class AnnotationSnapshot:
    """A cached set of endpoint annotations, with when it was retrieved."""

    endpoints: dict[int, AssayEndpoint] = field(default_factory=dict)
    retrieved: str = ""

    def __len__(self) -> int:
        return len(self.endpoints)

    def __iter__(self) -> Iterable[AssayEndpoint]:
        return iter(self.endpoints.values())

    def get(self, aeid: int) -> AssayEndpoint | None:
        return self.endpoints.get(aeid)

    def with_genes(self) -> list[AssayEndpoint]:
        return [e for e in self.endpoints.values() if e.genes]

    def by_gene_symbol(self) -> dict[str, list[AssayEndpoint]]:
        """Endpoints grouped by upper-cased gene symbol.

        Upper-casing merges species orthologs onto one key, so ``AR`` collects
        human, rat and other endpoints together. Read ``is_human`` on each
        before treating one as a human measurement.
        """
        out: dict[str, list[AssayEndpoint]] = {}
        for endpoint in self.endpoints.values():
            for symbol in {g.symbol.upper() for g in endpoint.genes if g.symbol}:
                out.setdefault(symbol, []).append(endpoint)
        return out


def _api_key() -> str:
    key = os.environ.get(API_KEY_ENV, "").strip()
    if not key:
        raise MissingAPIKey()
    return key


def _text(value: Any) -> str:
    return str(value).strip() if value not in (None, "") else ""


def parse_gene(raw: dict) -> GeneTarget | None:
    """Build a :class:`GeneTarget` from one ``gene[]`` object, or None."""
    symbol = _text(raw.get("geneSymbol")) or _text(raw.get("officialSymbol"))
    if not symbol:
        return None
    entrez = raw.get("entrezGeneId")
    return GeneTarget(
        symbol=symbol,
        full_name=_text(raw.get("officialFullName")) or _text(raw.get("geneName")),
        entrez_gene_id=int(entrez) if isinstance(entrez, (int, float)) else None,
        uniprot_accession=_text(raw.get("uniprotAccessionNumber")),
    )


def parse_annotation(raw: dict) -> AssayEndpoint:
    """Build an :class:`AssayEndpoint` from one annotation response object."""
    genes_raw = raw.get("gene") or []
    if isinstance(genes_raw, dict):
        genes_raw = [genes_raw]
    genes = tuple(
        sorted(
            (g for g in (parse_gene(x) for x in genes_raw if isinstance(x, dict)) if g),
            key=lambda g: g.symbol,
        )
    )
    citations_raw = raw.get("citations") or []
    if isinstance(citations_raw, dict):
        citations_raw = [citations_raw]
    pmids = tuple(
        sorted(
            {
                int(c["pmid"])
                for c in citations_raw
                if isinstance(c, dict) and isinstance(c.get("pmid"), (int, float))
            }
        )
    )
    return AssayEndpoint(
        aeid=int(raw["aeid"]),
        name=_text(raw.get("assayComponentEndpointName")),
        genes=genes,
        target_type=_text(raw.get("intendedTargetType")),
        target_type_sub=_text(raw.get("intendedTargetTypeSub")),
        target_family=_text(raw.get("intendedTargetFamily")),
        target_family_sub=_text(raw.get("intendedTargetFamilySub")),
        biological_process=_text(raw.get("biologicalProcessTarget")),
        organism=_text(raw.get("organism")),
        tissue=_text(raw.get("tissue")),
        cell=_text(raw.get("cellShortName")),
        function_type=_text(raw.get("assayFunctionType")),
        signal_direction=_text(raw.get("signalDirection")),
        is_viability=bool(raw.get("cellViabilityAssay")),
        format_type=_text(raw.get("assayFormatType")),
        source_name=_text(raw.get("assaySourceName")),
        citation_pmids=pmids,
    )


class ToxCastAssayAnnotations:
    """Fetches and caches EPA's ToxCast assay-endpoint annotations."""

    def __init__(self, data_dir: Path, *, timeout: float = 180.0) -> None:
        self.data_dir = Path(data_dir)
        self.timeout = timeout
        self._snapshot: AnnotationSnapshot | None = None

    @property
    def annotations_path(self) -> Path:
        return self.data_dir / ANNOTATIONS_FILE

    @property
    def manifest_path(self) -> Path:
        return self.data_dir / MANIFEST_FILE

    # ----- HTTP -----

    def _get(self, path: str) -> Any:
        headers = {"accept": "application/json", "x-api-key": _api_key()}
        url = f"{API_BASE}/{path.lstrip('/')}"
        with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
            response = client.get(url, headers=headers)
            if response.status_code == 401:
                raise MissingAPIKey()
            response.raise_for_status()
            return response.json()

    def fetch_one(self, aeid: int) -> AssayEndpoint:
        """Fetch a single endpoint's annotation, bypassing the cache."""
        payload = self._get(ANNOTATION_BY_AEID_PATH.format(aeid=aeid))
        rows = payload if isinstance(payload, list) else [payload]
        if not rows:
            raise KeyError(f"CTX has no assay endpoint {aeid}")
        return parse_annotation(rows[0])

    # ----- refresh -----

    def refresh(self, *, force: bool = False) -> int:
        """Fetch every endpoint annotation and cache it. Returns the count.

        One request covering the whole panel. Nothing is pinned by checksum: the
        API serves whatever invitroDB release is current and exposes no version
        endpoint, so the retrieval date is the strongest provenance available.
        The release itself is reported by a different endpoint; see the manifest.
        """
        if self.annotations_path.exists() and not force:
            logger.info(
                "annotations already cached (%s); pass --force to refetch",
                self.retrieved_date() or "undated",
            )
            return len(self.load())

        payload = self._get(ANNOTATIONS_PATH)
        if not isinstance(payload, list):
            raise RuntimeError("unexpected annotations payload: expected a list")

        self.data_dir.mkdir(parents=True, exist_ok=True)
        document = {
            "retrieved": datetime.now(UTC).strftime("%Y-%m-%d"),
            "source": f"EPA CTX {ANNOTATIONS_PATH}",
            "n_endpoints": len(payload),
            "endpoints": payload,
        }
        tmp = self.annotations_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(document), encoding="utf-8")
        tmp.replace(self.annotations_path)
        self._write_manifest(document)
        self._snapshot = None
        return len(payload)

    def _write_manifest(self, document: dict) -> None:
        """Record the fetch in a committed manifest.

        The annotations themselves are gitignored at several megabytes, which
        would take their provenance with them.
        """
        self.manifest_path.write_text(
            "# Provenance for the cached ToxCast/Tox21 assay-endpoint annotations.\n"
            "#\n"
            "# Unlike the other pinned data sources this records no sha256. The\n"
            "# EPA CTX API serves whatever invitroDB release is current and\n"
            "# exposes no version endpoint, so there is no stable upstream\n"
            "# artifact to pin. The release is reported per record by\n"
            "# `bioactivity/data/aed/search/by-dtxsid/{dtxsid}` as\n"
            "# `invitrodbVersion` if you need it.\n"
            "#\n"
            "# The annotations JSON is gitignored. Refetch it with:\n"
            "#     just toxcast-refresh\n"
            "\n"
            "source: EPA CompTox Chemicals Dashboard APIs (CTX), bioactivity domain\n"
            "programs: ToxCast, Tox21\n"
            f"endpoint: {API_BASE}/{ANNOTATIONS_PATH}\n"
            f'retrieved: "{document["retrieved"]}"\n'
            f"n_endpoints: {document['n_endpoints']}\n"
            "licence: >-\n"
            "  EPA states the CompTox data are free of all copyright restrictions\n"
            "  and fully and freely available for both non-commercial and\n"
            "  commercial use.\n",
            encoding="utf-8",
        )

    # ----- load -----

    def load(self) -> AnnotationSnapshot:
        """Lazy accessor for the cached annotations."""
        if self._snapshot is None:
            if not self.annotations_path.exists():
                raise AnnotationsMissing(self.annotations_path)
            document = json.loads(self.annotations_path.read_text(encoding="utf-8"))
            raw_endpoints = document.get("endpoints", document)
            parsed: dict[int, AssayEndpoint] = {}
            for raw in raw_endpoints:
                try:
                    endpoint = parse_annotation(raw)
                except (KeyError, TypeError, ValueError):
                    continue
                parsed[endpoint.aeid] = endpoint
            self._snapshot = AnnotationSnapshot(
                endpoints=parsed, retrieved=_text(document.get("retrieved"))
            )
        return self._snapshot

    def retrieved_date(self) -> str:
        if not self.annotations_path.exists():
            return ""
        try:
            document = json.loads(self.annotations_path.read_text(encoding="utf-8"))
        except ValueError:
            return ""
        return _text(document.get("retrieved"))


_REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA_DIR = _REPO_ROOT / "data" / "toxcast"


def default_annotations(data_dir: Path | None = None) -> ToxCastAssayAnnotations:
    return ToxCastAssayAnnotations(data_dir or DEFAULT_DATA_DIR)


def main(argv: list[str] | None = None) -> int:
    """CLI: refresh the cache, or summarise what is cached."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--force", action="store_true", help="refetch even if already cached"
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="describe what is cached instead of fetching",
    )
    parser.add_argument("--data-dir", type=Path, default=None)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)

    annotations = default_annotations(args.data_dir)
    if args.summary:
        snapshot = annotations.load()
        by_gene = snapshot.by_gene_symbol()
        print(f"endpoints          : {len(snapshot)}")
        print(f"retrieved          : {snapshot.retrieved or 'undated'}")
        print(f"with a gene target : {len(snapshot.with_genes())}")
        print(f"distinct targets   : {len(by_gene)}")
        print(f"human endpoints    : {sum(1 for e in snapshot if e.is_human)}")
        return 0

    count = annotations.refresh(force=args.force)
    print(f"{count} assay-endpoint annotations cached at {annotations.annotations_path}")
    print(f"provenance recorded in {annotations.manifest_path}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
