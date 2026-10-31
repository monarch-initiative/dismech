"""NCBI Bookshelf chapter index: GeneReviews and StatPearls, matched offline.

The committed index under ``cache/bookshelf/`` (built by
``scripts/build_bookshelf_index.py``) lists every PubMed-indexed chapter of two
Bookshelf collections. This module loads it and answers two questions without
touching the network:

* **Is this PMID (or ``NBK`` accession) a GeneReviews or StatPearls chapter?**
  -- :meth:`BookshelfIndex.source_of`. Exact, because the index is the
  collection's own PubMed membership, not a grep of the cached abstract.
* **Does a chapter exist whose title names this disease?** --
  :meth:`BookshelfIndex.match`. Heuristic, and reported as such: the caller
  gets a :class:`Match` carrying *how* the title matched (``EXACT`` down to
  ``NEAR``) so an exact-title hit can gate while a partial one is handed to a
  reviewer. That split is what makes the baseline check semi-deterministic.

Both collections are in the same index because they are the same kind of
object -- an expert-written narrative chapter with a PMID -- and are easy to
confuse. They are not equivalent sources, and the difference matters for
what a curator may lean on:

=====================  ================================  ===========================
                       GeneReviews                       StatPearls
=====================  ================================  ===========================
Scope                  Mendelian / heritable disease     all of clinical medicine
Size                   ~960 chapters                     ~9,600 chapters
Authorship             invited domain experts            volunteer clinicians
Review                 peer-reviewed; scheduled          light editorial review;
                       comprehensive revisions           continuing-education
                                                         framing
Structure              fixed clinical sections           free narrative plus a
                       (Clinical Characteristics,        "Continuing Education
                       Diagnosis, Management, Genetic    Activity" summary
                       Counseling), each quotable
Role in dismech        mandatory phenotype baseline      citable orientation
                       for a Mendelian entry             source; never a baseline
=====================  ================================  ===========================
"""

from __future__ import annotations

import csv
import difflib
import re
import unicodedata
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from dismech.repo_root import LazyRepoPaths

# Resolved from the working directory when read, so a worktree reads its own
# committed index (#15109).
_PATHS = LazyRepoPaths(
    __name__,
    REPO_ROOT=lambda root: root,
    DEFAULT_INDEX_DIR=lambda root: root / "cache" / "bookshelf",
)
__getattr__ = _PATHS.module_getattr

#: CSV stem -> the ``ReferenceTagEnum`` value that tags a chapter of it.
SOURCE_TAGS: dict[str, str] = {
    "genereviews": "GeneReviews",
    "statpearls": "StatPearls",
}
TAG_SOURCES: dict[str, str] = {tag: source for source, tag in SOURCE_TAGS.items()}

#: Match kinds from strongest to weakest. ``EXACT`` is a normalised-title
#: equality and is the only kind a gate should trust on its own.
#: ``GENE_SUFFIX`` is a ``<Disease> – <GENE>`` title whose disease part is in
#: the name and whose gene the entry names; it ranks next because the gene
#: agreement is checked, but it is a candidate, not an equality. ``ONLINE`` is
#: a live PubMed ``<name>[TI]`` hit on a chapter newer than the snapshot: PubMed
#: matched the name's words somewhere in the title, and nothing here compared
#: the two, so it ranks last and is only ever a candidate. ``GENE_SCOPED`` is
#: a ``<GENE>-Related …`` title naming one of the entry's ``genetic:`` genes,
#: found from the gene rather than from any disease name: GeneReviews often
#: scopes a chapter to a gene's whole spectrum (``Autosomal Dominant
#: TRPV4-Related Disorders`` covers SED Maroteaux type), which no disease-name
#: comparison reaches (#9694). It says only that the chapter is about the gene.
MATCH_KINDS = (
    "EXACT",
    "GENE_SUFFIX",
    "CONTAINS",
    "TITLE_IN_NAME",
    "NEAR",
    "GENE_SCOPED",
    "ONLINE",
)
NEAR_THRESHOLD = 0.95

#: Tokens that carry no disease identity on their own. A name made only of
#: these ("hereditary disease") is never used for a containment match.
_STOPWORDS = frozenset(
    [
        "syndrome",
        "disease",
        "disorder",
        "disorders",
        "type",
        "of",
        "the",
        "and",
        "with",
        "related",
        "deficiency",
        "overview",
        "hereditary",
        "familial",
        "congenital",
        "autosomal",
        "dominant",
        "recessive",
        "x",
        "linked",
    ]
)
_RELATED_PREFIX = re.compile(r"^[a-z0-9]+ related ")
_RELATED_GENE = re.compile(r"^([a-z0-9]+) related ")
_OVERVIEW_SUFFIX = re.compile(r"\s+overview$")
#: A trailing gene symbol set off by a spaced dash, read from the *raw* title
#: because normalisation drops the case that tells a gene symbol from a word:
#: ``Autosomal Dominant Tubulointerstitial Kidney Disease – REN.`` (#15904).
#: ``Udd Distal Myopathy – Tibial Muscular Dystrophy`` is several words and
#: ``RNU4-2–Related …`` has no spaces round its dash, so neither is read as one.
_GENE_SUFFIX = re.compile(
    r"^(?P<stem>.+?)\s+[\u2010-\u2015-]\s+(?P<gene>[A-Z][A-Z0-9]*[A-Z0-9](?:-[A-Z0-9]+)*)\.?$"
)
_RETIRED_RAW = re.compile(
    r"\s+[\u2010-\u2015-]\s+RETIRED CHAPTER, FOR HISTORICAL REFERENCE ONLY\.?$"
)
#: The words before a ``Related`` or ``Associated`` in a raw title, back to the
#: previous comma, full stop or dash: ``Autosomal Dominant TRPV4-``, ``HAMP- and
#: HJV-``, ``MCM8/MCM9-``, ``BRCA1- and BRCA2-``, ``Syndrome-SHANK3 `` (#9694).
_RELATED_SPAN = re.compile(
    r"([^,.\u2013\u2014]*?)[\u2010-\u2015-]?\s*\b(?:Related|Associated)\b"
)
#: A gene symbol as GeneReviews prints one: upper case, digits, an internal
#: hyphen (``RNU4-2``). Case is what tells ``HFE`` from ``Dominant``.
_SYMBOL = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*$")
_NUMBERISH = re.compile(r"^(?:\d+[a-z]?|[ivx]+)$")
_NBK = re.compile(r"NBK\d+")
_PMID = re.compile(r"PMID:(\d+)")


def normalize(text: str) -> str:
    """Case-, diacritic-, punctuation- and hyphen-insensitive comparison form."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower().replace("®", "")
    text = re.sub(r"[‐-―]", "-", text)
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return _OVERVIEW_SUFFIX.sub("", text)


def _number_tokens(text: str) -> frozenset[str]:
    return frozenset(tok for tok in text.split() if _NUMBERISH.match(tok))


def _related_gene(text: str) -> str | None:
    """The ``<GENE>`` of a ``<GENE>-Related …`` name, lower-cased, or ``None``."""
    found = _RELATED_GENE.match(text)
    return found.group(1) if found else None


def _genes_agree(name: str, title: str) -> bool:
    """False only when both are ``<GENE>-Related …`` forms naming different genes.

    ``ANK2-Related Neurodevelopmental Disorder`` and ``ATN1-Related
    Neurodevelopmental Disorder`` are one edit apart and are different
    diseases; the gene is the whole identity of such a name.
    """
    left, right = _related_gene(name), _related_gene(title)
    return left is None or right is None or left == right


def _phrase_in(needle: str, haystack: str) -> bool:
    return re.search(rf"(^|\s){re.escape(needle)}(\s|$)", haystack) is not None


def _gene_suffix(title: str) -> tuple[str, str]:
    """``(stem, gene)`` of a ``<Disease> – <GENE>`` title, normalised; else ``("", "")``."""
    found = _GENE_SUFFIX.match(_RETIRED_RAW.sub("", title.strip()))
    if not found:
        return "", ""
    return normalize(found.group("stem")), normalize(found.group("gene"))


def gene_symbols(text: str) -> frozenset[str]:
    """Gene-symbol-shaped tokens of ``text``, as written (``"REN variants"`` -> REN)."""
    found: set[str] = set()
    for raw in re.split(r"[\s/,;()]+", text):
        tok = raw.strip("-\u2010\u2011\u2012\u2013\u2014.:")
        # ``RNU4-2`` keeps its hyphen; ``Syndrome-SHANK3`` is two words.
        parts = [tok] if _SYMBOL.match(tok) else re.split(r"[\u2010-\u2015-]", tok)
        found.update(p for p in parts if len(p) >= 2 and _SYMBOL.match(p))
    return frozenset(found)


def _related_genes(title: str) -> frozenset[str]:
    """Every ``<GENE>`` a raw title scopes itself to with ``<GENE>-Related``."""
    found: set[str] = set()
    for span in _RELATED_SPAN.findall(title):
        found |= gene_symbols(span)
    return frozenset(found)


@dataclass(frozen=True)
class Chapter:
    source: str
    pmid: str
    nbk: str
    title: str
    retired: bool
    pubdate: str = ""

    @property
    def tag(self) -> str:
        return SOURCE_TAGS[self.source]

    @property
    def reference(self) -> str:
        return f"PMID:{self.pmid}"


@dataclass(frozen=True)
class Match:
    chapter: Chapter
    kind: str
    name: str  #: the entry name that matched

    @property
    def rank(self) -> int:
        return kind_rank(self.kind)


def kind_rank(kind: str) -> int:
    """Position of ``kind`` in :data:`MATCH_KINDS`; ``""`` (no title match) sorts last.

    The one ordering every caller sorts by, so a title match and a row found
    only by citation compare on the same scale. An unknown kind raises rather
    than sorting somewhere arbitrary.
    """
    return MATCH_KINDS.index(kind) if kind else len(MATCH_KINDS)


@dataclass
class _Row:
    chapter: Chapter
    norm_title: str
    stripped_title: str  #: with a leading ``<GENE>-related`` removed
    gene_stem: str = ""  #: ``<Disease>`` of a ``<Disease> – <GENE>`` title
    suffix_gene: str = ""  #: its ``<GENE>``, normalised
    related_genes: frozenset[str] = frozenset()  #: ``<GENE>`` of ``<GENE>-Related``


@dataclass
class BookshelfIndex:
    rows: list[_Row] = field(default_factory=list)
    by_pmid: dict[str, Chapter] = field(default_factory=dict)
    by_nbk: dict[str, Chapter] = field(default_factory=dict)
    _exact: dict[str, list[int]] = field(default_factory=dict)
    _postings: dict[str, set[int]] = field(default_factory=dict)
    _gene_suffixed: list[int] = field(default_factory=list)
    _by_related_gene: dict[str, set[int]] = field(default_factory=dict)
    sources: set[str] = field(default_factory=set)
    snapshot_date: str = ""

    # -- loading ---------------------------------------------------------

    @classmethod
    def load(
        cls,
        index_dir: Path | None = None,
        sources: Iterable[str] = tuple(SOURCE_TAGS),
    ) -> BookshelfIndex:
        if index_dir is None:
            index_dir = _PATHS.get("DEFAULT_INDEX_DIR")
        index = cls()
        for source in sources:
            path = index_dir / f"{source}.csv"
            if not path.exists():
                continue
            with path.open(encoding="utf-8", newline="") as handle:
                for record in csv.DictReader(handle):
                    index.add(
                        Chapter(
                            source=source,
                            pmid=record["pmid"],
                            nbk=record.get("nbk", ""),
                            title=record["title"],
                            retired=record.get("retired", "0") == "1",
                            pubdate=record.get("pubdate", ""),
                        )
                    )
        manifest = index_dir / "MANIFEST.yaml"
        if manifest.exists():
            for line in manifest.read_text(encoding="utf-8").splitlines():
                if line.startswith("snapshot_date:"):
                    index.snapshot_date = line.split(":", 1)[1].strip().strip("'\"")
        return index

    def add(self, chapter: Chapter) -> None:
        norm_title = normalize(chapter.title)
        # Retired chapters carry "– RETIRED CHAPTER, FOR HISTORICAL REFERENCE ONLY";
        # match on the title proper so the flag, not the suffix, carries that fact.
        norm_title = re.sub(
            r"\s+retired chapter for historical reference only$", "", norm_title
        )
        stripped = _RELATED_PREFIX.sub("", norm_title)
        gene_stem, suffix_gene = _gene_suffix(chapter.title)
        idx = len(self.rows)
        related = _related_genes(chapter.title)
        self.rows.append(
            _Row(chapter, norm_title, stripped, gene_stem, suffix_gene, related)
        )
        if gene_stem:
            self._gene_suffixed.append(idx)
        for gene in related:
            self._by_related_gene.setdefault(gene, set()).add(idx)
        self.by_pmid[chapter.pmid] = chapter
        if chapter.nbk:
            self.by_nbk[chapter.nbk] = chapter
        self.sources.add(chapter.source)
        self._exact.setdefault(norm_title, []).append(idx)
        if stripped != norm_title:
            self._exact.setdefault(stripped, []).append(idx)
        for token in set(norm_title.split()):
            self._postings.setdefault(token, set()).add(idx)

    def __len__(self) -> int:
        return len(self.rows)

    # -- identity lookups -------------------------------------------------

    def source_of(self, reference: str) -> Chapter | None:
        """The chapter a reference string denotes, or ``None``.

        Accepts ``PMID:NNN``, a bare PMID, or anything carrying an ``NBK``
        accession (a Bookshelf ``url:`` reference).
        """
        pmid_match = _PMID.search(reference)
        if pmid_match and pmid_match.group(1) in self.by_pmid:
            return self.by_pmid[pmid_match.group(1)]
        if reference.isdigit() and reference in self.by_pmid:
            return self.by_pmid[reference]
        nbk_match = _NBK.search(reference)
        if nbk_match and nbk_match.group(0) in self.by_nbk:
            return self.by_nbk[nbk_match.group(0)]
        return None

    # -- title matching ---------------------------------------------------

    def match(
        self,
        name: str,
        sources: Iterable[str] | None = None,
        genes: Iterable[str] = (),
    ) -> list[Match]:
        """Chapters whose title names ``name``, strongest kind first.

        ``EXACT``          normalised title == normalised name, optionally after
                           dropping a leading ``<GENE>-Related`` or trailing
                           ``Overview`` on the title.
        ``GENE_SUFFIX``    a ``<Disease> – <GENE>`` title whose ``<Disease>``
                           (>= 2 tokens, >= 8 chars) occurs as a phrase in the
                           name, and whose ``<GENE>`` occurs as a phrase in the
                           name or in one of ``genes``. ``genes`` is where the
                           caller passes what the rest of the entry says -- its
                           other names and its ``genetic:`` genes -- since one
                           name alone often does not carry the symbol. Without
                           the gene the three ``Autosomal Dominant
                           Tubulointerstitial Kidney Disease – UMOD/REN/MUC1``
                           chapters would be candidates for each other's entries.
        ``CONTAINS``       the name (>= 2 tokens, >= 8 chars, not all stopwords)
                           occurs as a phrase inside the title.
        ``TITLE_IN_NAME``  the title occurs as a phrase inside the name.
        ``NEAR``           difflib ratio >= 0.95 and every number-like token in
                           the title also occurs in the name, so ``Usher Syndrome
                           Type I`` never stands in for ``Usher Syndrome Type 4``.

        ``TITLE_IN_NAME`` and ``NEAR`` additionally require that two
        ``<GENE>-Related …`` forms name the same gene.
        """
        wanted = set(sources) if sources is not None else self.sources
        norm_name = normalize(name)
        if not norm_name:
            return []
        found: dict[int, str] = {}
        for idx in self._exact.get(norm_name, []):
            found[idx] = "EXACT"
        tokens = norm_name.split()
        name_numbers = _number_tokens(norm_name)
        gene_text = [norm_name, *(normalize(g) for g in genes)]
        for idx in self._gene_suffixed:
            row = self.rows[idx]
            if (
                idx not in found
                and len(row.gene_stem.split()) >= 2
                and len(row.gene_stem) >= 8
                and _phrase_in(row.gene_stem, norm_name)
                and _number_tokens(row.gene_stem) <= name_numbers
                and any(_phrase_in(row.suffix_gene, text) for text in gene_text if text)
            ):
                found[idx] = "GENE_SUFFIX"
        content = [tok for tok in tokens if tok not in _STOPWORDS]
        if content:
            candidates = set.intersection(
                *(self._postings.get(tok, set()) for tok in content)
            )
            for idx in candidates:
                if idx in found:
                    continue
                row = self.rows[idx]
                if (
                    len(tokens) >= 2
                    and len(norm_name) >= 8
                    and _phrase_in(norm_name, row.norm_title)
                ):
                    found[idx] = "CONTAINS"
                elif (
                    len(row.stripped_title.split()) >= 2
                    and len(row.stripped_title) >= 8
                    and _phrase_in(row.stripped_title, norm_name)
                    and _number_tokens(row.stripped_title) <= name_numbers
                    and _genes_agree(norm_name, row.norm_title)
                ):
                    found[idx] = "TITLE_IN_NAME"
            loose: set[int] = set()
            for tok in content:
                loose |= self._postings.get(tok, set())
            for idx in loose:
                if idx in found:
                    continue
                row = self.rows[idx]
                if (
                    _number_tokens(row.norm_title) <= name_numbers
                    and _genes_agree(norm_name, row.norm_title)
                    and difflib.SequenceMatcher(None, norm_name, row.norm_title).ratio()
                    >= NEAR_THRESHOLD
                ):
                    found[idx] = "NEAR"
        matches = [
            Match(self.rows[idx].chapter, kind, name)
            for idx, kind in found.items()
            if self.rows[idx].chapter.source in wanted
        ]
        return sorted(
            matches, key=lambda m: (m.rank, m.chapter.retired, int(m.chapter.pmid))
        )

    def match_genes(
        self, genes: Iterable[str], sources: Iterable[str] | None = None
    ) -> list[Match]:
        """``GENE_SCOPED`` chapters: a ``<GENE>-Related`` (or ``-Associated``) title naming one of ``genes``.

        ``genes`` are the strings of the entry's ``genetic:`` block
        (:func:`entry_genes`); the symbols in them are compared, case and all,
        with the symbols a title scopes itself to. This is the gene-side search
        the disease-name matches cannot make (#9694). A hit is a candidate to
        read and never a verdict: ``POLG-Related Disorders`` is about every
        POLG disease, which may or may not include this one.
        """
        wanted = set(sources) if sources is not None else self.sources
        symbols: set[str] = set()
        for text in genes:
            symbols |= gene_symbols(text)
        found: dict[int, str] = {}
        for symbol in sorted(symbols):
            for idx in self._by_related_gene.get(symbol, ()):
                found.setdefault(idx, symbol)
        matches = [
            Match(self.rows[idx].chapter, "GENE_SCOPED", symbol)
            for idx, symbol in found.items()
            if self.rows[idx].chapter.source in wanted
        ]
        return sorted(matches, key=lambda m: (m.chapter.retired, int(m.chapter.pmid)))


# -- cache-marker fallback ---------------------------------------------------

#: What an ``efetch``-rendered Bookshelf citation looks like in a
#: ``references_cache/PMID_*.md`` body. Anchored on the citation form, not the
#: bare collection name: a journal article that *cites* GeneReviews in its
#: reference list contains the word too. ``scripts/tag_references.py`` used to
#: grep for the bare word, under which PMID:18651971 -- an Orphanet J Rare Dis
#: review cited by ``Alpha_Mannosidosis`` whose full text lists a GeneReviews
#: chapter -- would have been tagged ``GeneReviews``.
CACHE_MARKERS: dict[str, tuple[str, ...]] = {
    "genereviews": (
        "GeneReviews(®) [Internet]",
        "GeneReviews® [Internet]",
        "In: GeneReviews",
    ),
    "statpearls": ("In: StatPearls [Internet]", "In: StatPearls"),
}


def source_from_cache_text(text: str) -> str | None:
    """Collection whose citation form appears in a cached record body, if any."""
    for source, markers in CACHE_MARKERS.items():
        if any(marker in text for marker in markers):
            return source
    return None


def entry_names(document: dict) -> list[str]:
    """The strings a chapter title could carry for this entry, deduplicated.

    Entry ``name``, ``synonyms``, and the ``disease_term`` preferred term and
    ontology label. Subtype names are deliberately excluded: ``Type 1`` is not
    a disease name, and a subtype's own chapter is a candidate at best.
    """
    names: list[str] = [document.get("name") or ""]
    synonyms = document.get("synonyms") or []
    names.extend(s for s in synonyms if isinstance(s, str))
    disease_term = document.get("disease_term") or {}
    if isinstance(disease_term, dict):
        names.append(disease_term.get("preferred_term") or "")
        term = disease_term.get("term") or {}
        if isinstance(term, dict):
            names.append(term.get("label") or "")
    seen: dict[str, None] = {}
    for candidate in names:
        candidate = candidate.strip()
        if candidate and normalize(candidate) and candidate not in seen:
            seen[candidate] = None
    return list(seen)


def entry_genes(document: dict) -> list[str]:
    """Gene strings from the entry's ``genetic:`` block, for the ``GENE_SUFFIX`` gate.

    Each record's ``name`` and its ``gene_term`` preferred term and label. The
    record ``name`` is often prose ("REN variants"), which is fine: the gate
    looks for the chapter's gene symbol as a phrase inside these strings.
    """
    genes: list[str] = []
    for record in document.get("genetic") or []:
        if not isinstance(record, dict):
            continue
        genes.append(record.get("name") or "")
        gene_term = record.get("gene_term") or {}
        if isinstance(gene_term, dict):
            genes.append(gene_term.get("preferred_term") or "")
            term = gene_term.get("term") or {}
            if isinstance(term, dict):
                genes.append(term.get("label") or "")
    return list(
        dict.fromkeys(g.strip() for g in genes if isinstance(g, str) and g.strip())
    )


#: ``relationship_type`` values a gene-side chapter search follows. Absent is
#: kept because most older Mendelian records carry none; a susceptibility,
#: modifier or somatic-driver gene's chapter is about some other disease.
_CAUSAL_RELATIONSHIPS = frozenset({None, "CAUSATIVE"})


#: ``HP:0001442`` *Typified by somatic mosaicism*: the structured signal that an
#: entry's causal variant is post-zygotic (see the ``somatic-mosaicism`` skill).
SOMATIC_MOSAICISM = "HP:0001442"


def is_somatic_mosaic(document: dict) -> bool:
    """Whether an ``inheritance`` block, on the entry or a subtype, binds ``HP:0001442``."""
    blocks = list(document.get("inheritance") or [])
    for subtype in document.get("has_subtypes") or []:
        if isinstance(subtype, dict):
            blocks.extend(subtype.get("inheritance") or [])
    for block in blocks:
        if not isinstance(block, dict):
            continue
        term = (block.get("inheritance_term") or {}).get("term") or {}
        if isinstance(term, dict) and term.get("id") == SOMATIC_MOSAICISM:
            return True
    return False


def entry_causal_genes(document: dict) -> list[str]:
    """Gene strings of the ``genetic:`` records that claim to cause the disease.

    The input to the ``GENE_SCOPED`` search (#9694). A record counts when its
    ``relationship_type`` is ``CAUSATIVE`` or absent and it is not a somatic
    driver: ``variant_origin`` not ``SOMATIC``, and no "somatic" in its
    ``name`` or ``association``. ``HRAS-Related Costello Syndrome`` is not a
    baseline for a thymoma carrying a somatic HRAS mutation. A somatic-mosaic
    disorder (:func:`is_somatic_mosaic`) is the exception: its causal variant is
    somatic by definition, and the gene's chapter is the baseline
    (*PIK3CA-Related Overgrowth Spectrum* for hemimegalencephaly).
    """
    mosaic = is_somatic_mosaic(document)
    genes: list[str] = []
    for record in document.get("genetic") or []:
        if not isinstance(record, dict):
            continue
        if record.get("relationship_type") not in _CAUSAL_RELATIONSHIPS:
            continue
        if not mosaic:
            if str(record.get("variant_origin") or "").startswith("SOMATIC"):
                continue
            prose = f"{record.get('name') or ''} {record.get('association') or ''}"
            if "somatic" in prose.lower():
                continue
        genes.extend(entry_genes({"genetic": [record]}))
    return list(dict.fromkeys(genes))
