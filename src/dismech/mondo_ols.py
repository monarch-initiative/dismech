"""Per-term MONDO facts from the EBI Ontology Lookup Service (OLS4).

``just preflight-dr`` and ``dismech.research_anchors`` read three facts about
one MONDO term: its ``RO:0004003`` causal gene(s), its OMIM cross-references,
and its exact synonyms. The local ``sqlite:obo:mondo`` build answers them, but
it is about 1.3 GB on disk and is never downloaded implicitly (#12687). OLS
serves the same per-term facts over HTTP, so without the local build these
callers ask OLS instead of giving up (#15436).

One request per term: the v2 entity endpoint returns the term's restrictions
(``relatedTo``, which carries ``RO:0004003``), its ``hasDbXref`` values, its
exact synonyms, and the labels of every entity it links to, which includes the
gene symbol for each HGNC object.

What OLS cannot answer is the reverse question, "which MONDO diseases does
this gene cause". Its search does not index restriction fillers, so there is
no per-gene query with complete recall. :class:`OlsMondoAdapter` says so with
:attr:`OlsMondoAdapter.supports_reverse_relationships` rather than returning
an incomplete answer that would read as "this gene causes no other disease".
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

OLS_API = "https://www.ebi.ac.uk/ols4/api"
#: Seconds before one OLS request is abandoned.
DEFAULT_TIMEOUT = 30.0

OBO_PURL = "http://purl.obolibrary.org/obo/"
GENE_PROPERTY = OBO_PURL + "RO_0004003"
GENE_RELATION = "RO:0004003"
EXACT_SYNONYM = "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym"
DBXREF = "http://www.geneontology.org/formats/oboInOwl#hasDbXref"
HGNC_IRI_PREFIX = "http://identifiers.org/hgnc/"
REPLACED_BY = OBO_PURL + "IAO_0100001"

__all__ = [
    "DEFAULT_TIMEOUT",
    "MondoTermFacts",
    "OlsLookupError",
    "OlsMondoAdapter",
    "OlsTermNotFound",
    "entity_url",
    "fetch_mondo_term",
    "parse_mondo_entity",
]


class OlsLookupError(RuntimeError):
    """OLS did not answer: unreachable, timed out, or returned something unusable."""


class OlsTermNotFound(OlsLookupError):
    """OLS answered, and has no such MONDO term (HTTP 404)."""


@dataclass(frozen=True)
class MondoTermFacts:
    """What OLS records about one MONDO term."""

    id: str
    label: str = ""
    obsolete: bool = False
    #: ``RO:0004003`` objects, as ``HGNC:<n>`` -- the casing the local
    #: ``sqlite:obo:mondo`` build emits, so the two sources agree.
    genes: tuple[str, ...] = ()
    #: Gene CURIE -> the symbol MONDO labels it with.
    gene_labels: tuple[tuple[str, str], ...] = ()
    #: Every ``hasDbXref`` value, e.g. ``OMIM:614321``.
    xrefs: tuple[str, ...] = ()
    exact_synonyms: tuple[str, ...] = ()
    #: For an obsolete term, the term MONDO says replaced it (``IAO:0100001``).
    replaced_by: tuple[str, ...] = ()

    @property
    def omim_ids(self) -> tuple[str, ...]:
        """The digits of each ``OMIM:`` xref (``OMIMPS:`` is a different prefix)."""
        out: list[str] = []
        for xref in self.xrefs:
            if not xref.upper().startswith("OMIM:"):
                continue
            digits = xref.split(":", 1)[1].strip()
            if digits.isdigit() and digits not in out:
                out.append(digits)
        return tuple(out)


def _iri(curie: str) -> str:
    prefix, _, local = curie.strip().partition(":")
    return f"{OBO_PURL}{prefix.upper()}_{local}"


def entity_url(curie: str) -> str:
    """The OLS v2 entity URL for a MONDO CURIE (the IRI is double-encoded)."""
    once = urllib.parse.quote(_iri(curie), safe="")
    return f"{OLS_API}/v2/ontologies/mondo/entities/{urllib.parse.quote(once, safe='')}"


def _get_json(url: str, timeout: float) -> dict:
    """GET ``url`` as JSON. The single network call, so tests patch this."""
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            raise OlsTermNotFound(f"OLS returned HTTP 404 for {url}") from exc
        raise OlsLookupError(f"OLS returned HTTP {exc.code} for {url}") from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise OlsLookupError(f"could not reach OLS ({url}): {exc}") from exc
    except ValueError as exc:
        raise OlsLookupError(f"OLS returned invalid JSON for {url}: {exc}") from exc


def _as_list(value) -> list:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def _text(value) -> str:
    """A literal, or the ``value`` of an OLS reified literal (one with axioms)."""
    if isinstance(value, dict):
        value = value.get("value")
    return value.strip() if isinstance(value, str) else ""


def _obo_curie(iri: str) -> str:
    """``http://purl.obolibrary.org/obo/MONDO_0009299`` -> ``MONDO:0009299``."""
    if iri.startswith(OBO_PURL) and "_" in iri[len(OBO_PURL) :]:
        return iri[len(OBO_PURL) :].replace("_", ":", 1)
    return iri


def _gene_curie(iri: str) -> str:
    if iri.startswith(HGNC_IRI_PREFIX):
        return "HGNC:" + iri[len(HGNC_IRI_PREFIX) :]
    return iri


def parse_mondo_entity(payload: dict, mondo_id: str) -> MondoTermFacts:
    """Read :class:`MondoTermFacts` out of an OLS v2 entity response."""
    if not isinstance(payload, dict) or not payload.get("iri"):
        raise OlsLookupError(f"OLS returned no entity for {mondo_id}")
    if payload.get("iri") != _iri(mondo_id):
        raise OlsLookupError(
            f"OLS answered {mondo_id} with a different entity ({payload.get('iri')})"
        )
    labels = [_text(v) for v in _as_list(payload.get("label"))]
    label = next((v for v in labels if v), "")

    linked = payload.get("linkedEntities") or {}
    genes: list[str] = []
    gene_labels: dict[str, str] = {}
    for restriction in _as_list(payload.get("relatedTo")):
        if not isinstance(restriction, dict):
            continue
        if restriction.get("property") != GENE_PROPERTY:
            continue
        filler = restriction.get("value")
        if not isinstance(filler, str):  # a nested class expression, not a gene
            continue
        curie = _gene_curie(filler)
        if curie in genes:
            continue
        genes.append(curie)
        info = linked.get(filler) if isinstance(linked, dict) else None
        symbols = [_text(v) for v in _as_list((info or {}).get("label"))]
        symbol = next((s for s in symbols if s), "")
        if symbol:
            gene_labels[curie] = symbol

    xrefs: list[str] = []
    for value in _as_list(payload.get(DBXREF)):
        text = _text(value)
        if text and text not in xrefs:
            xrefs.append(text)

    synonyms: list[str] = []
    for value in _as_list(payload.get(EXACT_SYNONYM)):
        text = _text(value)
        if text and text not in synonyms:
            synonyms.append(text)

    replaced_by: list[str] = []
    for value in _as_list(payload.get(REPLACED_BY)):
        text = _text(value)
        if text and _obo_curie(text) not in replaced_by:
            replaced_by.append(_obo_curie(text))

    return MondoTermFacts(
        id=mondo_id,
        label=label,
        obsolete=bool(payload.get("isObsolete")),
        genes=tuple(genes),
        gene_labels=tuple(gene_labels.items()),
        xrefs=tuple(xrefs),
        exact_synonyms=tuple(synonyms),
        replaced_by=tuple(replaced_by),
    )


def fetch_mondo_term(
    mondo_id: str, *, timeout: float = DEFAULT_TIMEOUT
) -> MondoTermFacts:
    """Fetch one MONDO term from OLS.

    Raises :class:`OlsTermNotFound` when OLS has no such term and
    :class:`OlsLookupError` when it could not be asked. Never returns an empty
    record for a failed request: that would read as "MONDO records nothing".
    """
    mondo_id = mondo_id.strip()
    if not mondo_id.upper().startswith("MONDO:"):
        raise ValueError(f"expected a MONDO CURIE, got {mondo_id!r}")
    try:
        payload = _get_json(entity_url(mondo_id), timeout)
    except OlsTermNotFound as exc:
        raise OlsTermNotFound(f"OLS has no MONDO term {mondo_id}") from exc
    return parse_mondo_entity(payload, mondo_id)


def fetch_mondo_release(*, timeout: float = DEFAULT_TIMEOUT) -> str:
    """The MONDO release OLS has loaded (e.g. ``2026-10-06``), or ``""``."""
    try:
        payload = _get_json(f"{OLS_API}/ontologies/mondo", timeout)
    except OlsLookupError:
        return ""
    config = payload.get("config") if isinstance(payload, dict) else None
    version = (config or {}).get("version") if isinstance(config, dict) else None
    return version.strip() if isinstance(version, str) else ""


class OlsMondoAdapter:
    """The slice of OAK's adapter interface that MONDO identity lookups call.

    Answers ``label``, forward ``relationships``, ``simple_mappings_by_curie``
    and ``alias_relationships`` (exact synonyms only) for MONDO terms, one
    cached OLS request per term. A request that fails raises
    :class:`OlsLookupError`, which callers record as a failed lookup.

    It does not answer a reverse ``relationships`` query (``objects=`` with no
    ``subjects=``): see the module docstring.
    """

    #: Read by ``preflight_dr`` before it asks for the diseases a gene causes.
    supports_reverse_relationships = False

    def __init__(self, timeout: float = DEFAULT_TIMEOUT):
        self.timeout = timeout
        self._terms: dict[str, MondoTermFacts] = {}
        self._gene_labels: dict[str, str] = {}
        self._release: str | None = None

    def term(self, mondo_id: str) -> MondoTermFacts:
        if mondo_id not in self._terms:
            facts = fetch_mondo_term(mondo_id, timeout=self.timeout)
            self._terms[mondo_id] = facts
            self._gene_labels.update(dict(facts.gene_labels))
        return self._terms[mondo_id]

    def source_description(self) -> str:
        """Where the facts came from, for the preflight output."""
        if self._release is None:
            self._release = fetch_mondo_release(timeout=self.timeout)
        release = (
            f"MONDO release {self._release}" if self._release else "release unknown"
        )
        return f"OLS ({OLS_API}, {release}); no local MONDO build"

    @staticmethod
    def _is_mondo(curie: str) -> bool:
        return str(curie).upper().startswith("MONDO:")

    def label(self, curie: str) -> str | None:
        curie = str(curie)
        if self._is_mondo(curie):
            return self.term(curie).label or None
        # Gene labels come from the linked entities of terms already fetched,
        # keyed ``HGNC:<n>``; this repository writes the prefix as ``hgnc:``.
        prefix, _, local = curie.partition(":")
        if prefix.upper() == "HGNC":
            curie = f"HGNC:{local}"
        return self._gene_labels.get(curie)

    def relationships(self, subjects=None, predicates=None, objects=None):
        if subjects is None:
            raise NotImplementedError(
                "OLS cannot list the MONDO diseases a gene causes (a reverse "
                f"{GENE_RELATION} query); that needs the local MONDO build"
            )
        for subject in subjects:
            if not self._is_mondo(subject):
                continue
            if predicates is not None and GENE_RELATION not in predicates:
                continue
            for gene in self.term(subject).genes:
                if objects is None or gene in objects:
                    yield subject, GENE_RELATION, gene

    def obsolescence(self, curie: str) -> tuple[bool, tuple[str, ...]]:
        """``(obsolete, replaced_by)`` for a MONDO term."""
        facts = self.term(curie)
        return facts.obsolete, facts.replaced_by

    def simple_mappings_by_curie(self, curie: str):
        if not self._is_mondo(curie):
            return []
        return [("oio:hasDbXref", xref) for xref in self.term(curie).xrefs]

    def alias_relationships(self, curie: str, exclude_labels: bool = False):
        if not self._is_mondo(curie):
            return []
        return [("oio:hasExactSynonym", s) for s in self.term(curie).exact_synonyms]
