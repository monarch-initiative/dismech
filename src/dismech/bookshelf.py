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

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INDEX_DIR = REPO_ROOT / "cache" / "bookshelf"

#: CSV stem -> the ``ReferenceTagEnum`` value that tags a chapter of it.
SOURCE_TAGS: dict[str, str] = {
    "genereviews": "GeneReviews",
    "statpearls": "StatPearls",
}
TAG_SOURCES: dict[str, str] = {tag: source for source, tag in SOURCE_TAGS.items()}

#: Match kinds from strongest to weakest. ``EXACT`` is a normalised-title
#: equality and is the only kind a gate should trust on its own.
MATCH_KINDS = ("EXACT", "CONTAINS", "TITLE_IN_NAME", "NEAR")
NEAR_THRESHOLD = 0.95

#: Tokens that carry no disease identity on their own. A name made only of
#: these ("hereditary disease") is never used for a containment match.
_STOPWORDS = frozenset(
    "syndrome disease disorder disorders type of the and with related deficiency "
    "overview hereditary familial congenital autosomal dominant recessive x linked".split()
)
_RELATED_PREFIX = re.compile(r"^[a-z0-9]+ related ")
_RELATED_GENE = re.compile(r"^([a-z0-9]+) related ")
_OVERVIEW_SUFFIX = re.compile(r"\s+overview$")
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
        return MATCH_KINDS.index(self.kind)


@dataclass
class _Row:
    chapter: Chapter
    norm_title: str
    stripped_title: str  #: with a leading ``<GENE>-related`` removed


@dataclass
class BookshelfIndex:
    rows: list[_Row] = field(default_factory=list)
    by_pmid: dict[str, Chapter] = field(default_factory=dict)
    by_nbk: dict[str, Chapter] = field(default_factory=dict)
    _exact: dict[str, list[int]] = field(default_factory=dict)
    _postings: dict[str, set[int]] = field(default_factory=dict)
    sources: set[str] = field(default_factory=set)
    snapshot_date: str = ""

    # -- loading ---------------------------------------------------------

    @classmethod
    def load(
        cls,
        index_dir: Path = DEFAULT_INDEX_DIR,
        sources: Iterable[str] = tuple(SOURCE_TAGS),
    ) -> "BookshelfIndex":
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
        idx = len(self.rows)
        self.rows.append(_Row(chapter, norm_title, stripped))
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

    def match(self, name: str, sources: Iterable[str] | None = None) -> list[Match]:
        """Chapters whose title names ``name``, strongest kind first.

        ``EXACT``          normalised title == normalised name, optionally after
                           dropping a leading ``<GENE>-Related`` or trailing
                           ``Overview`` on the title.
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
        content = [tok for tok in tokens if tok not in _STOPWORDS]
        if content:
            candidates = set.intersection(
                *(self._postings.get(tok, set()) for tok in content)
            )
            name_numbers = _number_tokens(norm_name)
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
