#!/usr/bin/env python3
"""Backfill disorder evidence from deep-research citation files."""

from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import subprocess
import time
from collections import defaultdict
from collections.abc import Iterable, Mapping, MutableMapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

from dismech.yaml_io import safe_load

CITATION_FILE_RE = re.compile(r"^(?P<name>.+)-deep-research-[^.]+\.md\.citations\.md$")
PMID_RE = re.compile(r"\bPMID\s*[:#]?\s*(\d{4,9})\b", re.IGNORECASE)
PUBMED_URL_RE = re.compile(
    r"https?://(?:www\.)?pubmed\.ncbi\.nlm\.nih\.gov/(\d{4,9})(?:/|\b)", re.IGNORECASE
)
DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/([^\s\],)]+)", re.IGNORECASE)
DOI_PREFIX_RE = re.compile(r"\bDOI\s*:\s*([^\s\],)]+)", re.IGNORECASE)
DOI_TOKEN_RE = re.compile(r"\b10\.\d{4,9}/[^\s\],;]+", re.IGNORECASE)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(])")
LEADING_SECTION_LABEL_RE = re.compile(
    r"^(?:abstract|summary)\s*[:/\-]?\s*",
    re.IGNORECASE,
)
LEADING_SUBSECTION_LABEL_RE = re.compile(
    # The optional leading "and" catches the second half of a compound header
    # once the first half has been peeled ("Background and Aims" -> "and Aims").
    # Safe at any case because a label word must follow: "TP53 and other tumour
    # suppressors" is not touched.
    r"^(?:and\s+)?"
    # "purpose of review" before bare "purpose", or only the first word goes and
    # the snippet opens on a dangling "of review ...".
    r"(?:purpose of (?:review|(?:the |this |present )?study)|"
    r"background(?:/introduction)?|context and justification|purpose|objectives?|"
    r"methods(?: and main results)?|results?|conclusions?|discussion|introduction|"
    r"importance|aims?)"
    r"\s*[:/\-]?\s*",
    re.IGNORECASE,
)
# Compound structured-abstract headers ("INTRODUCTION AND IMPORTANCE:",
# "BACKGROUND AND OBJECTIVES:", "MATERIAL AND METHODS:") are only half
# recognised by the two label patterns above, which leaves a dangling all-caps
# conjunction or an unlisted second header on the front of the snippet. These
# two peel the remainder off generically instead of chasing every journal's
# header vocabulary. Both are case-SENSITIVE on purpose: an all-caps "AND" is
# header debris, whereas "TP53 and other tumour suppressors ..." is a sentence
# that opens on a gene symbol -- relaxing the case ate the gene. A leading "&"
# is always debris: the sentence splitter never breaks before one, so it can
# only appear once "BACKGROUND & AIMS:" has been taken apart around it.
LEADING_CONJUNCTION_RE = re.compile(r"^(?:[A-Z][A-Z0-9/&'()\-]*\s+)*(?:AND|&)\s+")
# The section number of an MDPI-style structured abstract, left behind once the
# label it introduced ("(1) Background:") has been stripped.
LEADING_SECTION_NUMBER_RE = re.compile(r"^\(\d+\)\s+")
# PubMed's translated-article marker, which sits in front of the abstract of a
# non-English record: "[Article in French] Alport syndrome (AS) is ...".
LANGUAGE_NOTE_RE = re.compile(r"^\[Article in [^\]]*\]\s*", re.IGNORECASE)
# The leading class admits "&" so that the tail of "BACKGROUND & AIMS:" is
# peeled once the label pattern above has taken "BACKGROUND ", instead of
# leaving a stray "& " on the front of the snippet.
ALLCAPS_HEADER_RE = re.compile(r"^[A-Z&][A-Z0-9/&'()\- ]{1,48}:\s*")
# Web-scraped cache bodies carry page furniture -- inline scripts, style rules --
# which survives tag stripping and reads like a long sentence.
MARKUP_NOISE_RE = re.compile(
    r"^(?:var|function|try|catch|if|else|window|document)\b|@media\b|\bdocument\.",
    re.IGNORECASE,
)

# Plain-text PubMed/PMC records (the ``full_text_pdf`` / ``full_text_xml`` cache
# bodies) wrap the abstract in a bibliographic envelope that carries no
# propositional content: a numbered journal-citation line, the title, the author
# list, numbered affiliations, and a trailing DOI/PMCID/PMID block::
#
#     1. Br J Cancer. 2000 Aug;83(4):463-6. doi: 10.1054/bjoc.2000.1249.
#
#     The rate of the founder Jewish mutations in BRCA1 and BRCA2 ...
#
#     Vazina A(1), Baniel J, Yaacobi Y, ...
#
# Sentence-splitting the body hands those lines to the snippet field like any
# other sentence: the citation line is >= 40 characters and is not the title, so
# it wins. That is how 207 evidence snippets on ``main`` came to be volume/page/
# DOI lines (#8096). None of them can support or refute anything, which is
# precisely what an evidence snippet is for.
CITATION_LINE_RE = re.compile(
    r"^\s*\d{4}\s+\w{3}[;\s]"  # 2000 Aug;83(4):463-6.
    r"|^\s*\d{4};\s*\d+[(:]"  # 2016;7:12451.
    r"|^\s*(?:doi|pmid|pmcid)\s*:",  # the trailing identifier block
    re.IGNORECASE,
)
# The volume/issue/page and DOI fragments, unanchored, for judging a whole
# paragraph that begins with the record's "1. " numbering.
VOLUME_CITATION_RE = re.compile(r"\b\d{4}(?:\s+\w{3,9}(?:\s+\d{1,2})?)?;\s*\d+[(:]")
DOI_CITATION_RE = re.compile(r"\bdoi:\s*10\.", re.IGNORECASE)
# A DOI inside a long run of prose belongs to a sentence that also makes a
# claim, so length gates the DOI-only test. The 207 citation-line snippets
# #8096 found run 40-97 characters; 120 leaves headroom without reaching the
# length of a sentence that says something.
CITATION_MAX_LENGTH = 120
# A numbered affiliation, i.e. the ``(2)Department of ...`` continuation lines
# of an ``Author information:`` block (the first line of which is caught by the
# existing ``author information`` prefix test). The lookahead for a non-space is
# what separates it from an MDPI-style structured abstract, which numbers its
# sections "(1) Background: ... (2) Methods: ..." -- with a space.
AFFILIATION_MARKER_RE = re.compile(r"^\(\d+\)(?=\S)")
# The identifier block that closes a plain-text PubMed record.
IDENTIFIER_TRAILER_RE = re.compile(r"^(?:doi|pmid|pmcid)\s*:", re.IGNORECASE)
# Opening of a paragraph that is metadata about the record rather than part of
# it. The affiliation block is the reason this has to be handled by paragraph
# and not by sentence: an author's *second* affiliation continues on a line with
# no ``(n)`` marker of its own, so it is indistinguishable from prose in
# isolation.
BIBLIOGRAPHIC_PARAGRAPH_PREFIXES = (
    "author information:",
    "collaborators:",
    "comment in",
    "comment on",
    "conflict of interest statement",
    "copyright",
    "erratum in",
    "update in",
    "update of",
)
NUMBERED_CITATION_RE = re.compile(r"^\s*\d+\.\s+\S")
# A book imprint line -- "Treasure Island (FL): StatPearls Publishing; 2026
# Jan-." -- which is how the StatPearls and GeneReviews records identify their
# publisher. Anchored at both ends so an ordinary sentence that happens to
# contain a colon, a semicolon, and a year does not match.
IMPRINT_LINE_RE = re.compile(
    r"^[^:;]{2,60}:\s+[^;]{2,80};\s*\d{4}(?:\s+\w{3,9})?\s*[-–—]?\.?$"
)
# One name in an author list: surname(s) then 1-4 initials, optionally followed
# by the affiliation superscripts PubMed renders as ``(1)`` or ``(1)(2)``. The
# letter classes are deliberately unicode-aware rather than ``[A-Za-z]`` -- a
# Polish or Turkish byline is still a byline, and an ASCII-only pattern scored
# one real author list at 58%, just under the threshold below.
AUTHOR_NAME_RE = re.compile(
    r"^[^\W\d_][^\W\d_'’\-]*(?:[ \-][^\W\d_][^\W\d_'’\-]*)*"
    r"\s+(?P<initials>[^\W\d_]{1,4})(?:\(\d+\))*$"
)
# Nobiliary particles, which carry the lowercase start of a surname that is
# capitalised further along ("van der Meer AB", "de Groot J").
AUTHOR_PARTICLE_RE = re.compile(
    r"^(?:van|von|de[nrl]?|della|del|di|da|dos|du|la|le|ter)\s+", re.IGNORECASE
)
# Share of comma-separated segments that must parse as names before a candidate
# is called an author list rather than a sentence that happens to list people.
AUTHOR_LIST_THRESHOLD = 0.6

HOLDER_NAME = "Deep research literature mapping"


@dataclass
class DisorderResult:
    disorder: str
    cited_refs: int
    existing_refs: int
    missing_refs: int
    added_refs: int
    unresolved_refs: int
    changed: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Parse deep-research citation files and backfill missing references "
            "into disorder evidence blocks."
        )
    )
    parser.add_argument("--kb-dir", default="kb/disorders")
    parser.add_argument("--research-dir", default="research")
    parser.add_argument("--references-cache-dir", default="references_cache")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument(
        "--max-disorders",
        type=int,
        default=None,
        help="Optional cap on disorders to process.",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        default=None,
        help="Only process these disorder file stems.",
    )
    parser.add_argument(
        "--max-new-refs-per-disorder",
        type=int,
        default=None,
        help="Optional cap on new references added per disorder.",
    )
    parser.add_argument(
        "--fetch-missing-cache",
        action="store_true",
        help="Call `just fetch-reference` when a cited ID is not cached.",
    )
    parser.add_argument(
        "--fetch-timeout-seconds",
        type=int,
        default=45,
        help="Timeout for each fetch-reference call.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to files. Without this flag, run as dry-run.",
    )
    parser.add_argument(
        "--add-findings",
        action="store_true",
        help=(
            "Create a top-level references[].findings[].evidence item for deep-research "
            "references that do not already have one."
        ),
    )
    parser.add_argument(
        "--repair-findings",
        action="store_true",
        help=(
            "Normalize existing top-level reference findings generated from deep research "
            "(repair snippets, evidence_source values, and cache-derived titles)."
        ),
    )
    return parser.parse_args()


def normalize_doi(doi: str) -> str:
    value = doi.strip()
    value = value.split("?", 1)[0].split("#", 1)[0]
    value = value.rstrip(".,;)]")
    value = value.lstrip("(")

    for suffix in ("/full", "/pdf", "/abstract", "/epub"):
        if value.lower().endswith(suffix):
            value = value[: -len(suffix)]
            break

    return value


def canonical_ref(reference: str) -> str | None:
    ref = reference.strip()
    if ref.upper().startswith("PMID:"):
        digits = re.sub(r"\D", "", ref.split(":", 1)[1])
        return f"PMID:{digits}"
    if ref.upper().startswith("DOI:"):
        doi = normalize_doi(ref.split(":", 1)[1]).lower()
        if not valid_doi(doi):
            return None
        return f"DOI:{doi}"
    if re.fullmatch(r"\d{4,9}", ref):
        return f"PMID:{ref}"
    if ref.lower().startswith("10."):
        doi = normalize_doi(ref).lower()
        if not valid_doi(doi):
            return None
        return f"DOI:{doi}"
    return None


def valid_doi(doi: str) -> bool:
    if not doi:
        return False
    if not doi.startswith("10."):
        return False
    if "/" not in doi:
        return False
    if doi.endswith(("/", ".")):
        return False
    if any(ch in doi for ch in ("|", "\\", "<", ">", "{", "}", '"', "'")):
        return False
    if doi.count("(") != doi.count(")"):
        return False
    if "%" in doi:
        return False
    # Minimal structural check after normalization.
    return re.fullmatch(r"10\.\d{4,9}/\S+", doi) is not None


def extract_refs(text: str) -> set[str]:
    refs: set[str] = set()

    def add_ref(raw: str) -> None:
        value = canonical_ref(raw)
        if value and (value.startswith(("PMID:", "DOI:"))):
            refs.add(value)

    for pmid in PMID_RE.findall(text):
        add_ref(f"PMID:{pmid}")

    for pmid in PUBMED_URL_RE.findall(text):
        add_ref(f"PMID:{pmid}")

    for doi in DOI_URL_RE.findall(text):
        add_ref(f"DOI:{doi}")

    for doi in DOI_PREFIX_RE.findall(text):
        add_ref(f"DOI:{doi}")

    for doi in DOI_TOKEN_RE.findall(text):
        add_ref(f"DOI:{doi}")

    return refs


def citations_by_disorder(research_dir: str) -> dict[str, dict[str, set[str]]]:
    by_disorder: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for path in glob.glob(
        os.path.join(research_dir, "*-deep-research-*.md.citations.md")
    ):
        filename = os.path.basename(path)
        if filename.startswith("com_"):
            continue
        match = CITATION_FILE_RE.match(filename)
        if not match:
            continue
        disorder = match.group("name")
        research_file = filename.removesuffix(".citations.md")
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        refs = extract_refs(text)
        for ref in refs:
            by_disorder[disorder][ref].add(research_file)
    return by_disorder


def collect_existing_refs(node: Any, out: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "reference" and isinstance(value, str):
                canon = canonical_ref(value)
                if canon:
                    out.add(canon)
            else:
                collect_existing_refs(value, out)
    elif isinstance(node, list):
        for item in node:
            collect_existing_refs(item, out)


def cache_path_for_ref(reference: str, references_cache_dir: str) -> Path:
    safe = reference.replace(":", "_").replace("/", "_")
    return Path(references_cache_dir) / f"{safe}.md"


def parse_cache_title(cache_path: Path) -> str | None:
    meta, _ = parse_cache_metadata_and_body(cache_path)
    title = meta.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()

    if not cache_path.exists():
        return None

    text = cache_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            if title:
                return title

    return None


def parse_cache_metadata_and_body(cache_path: Path) -> tuple[dict[str, Any], str]:
    if not cache_path.exists():
        return {}, ""

    text = cache_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        end_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end_idx = i
                break
        if end_idx is not None:
            frontmatter = "\n".join(lines[1:end_idx])
            try:
                meta = safe_load(frontmatter) or {}
                body = "\n".join(lines[end_idx + 1 :]).strip()
                return meta, body
            except Exception:
                return {}, text

    return {}, text


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def collect_existing_titles(node: Any, out: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"title", "reference_title"} and isinstance(value, str):
                normalized = normalize_title(value)
                if normalized:
                    out.add(normalized)
            else:
                collect_existing_titles(value, out)
    elif isinstance(node, list):
        for item in node:
            collect_existing_titles(item, out)


def is_author_name(segment: str) -> bool:
    match = AUTHOR_NAME_RE.match(segment)
    if match is None:
        return False
    # "van der Meer AB" is a surname; the capital lives past the particles.
    stem = segment
    while True:
        stripped = AUTHOR_PARTICLE_RE.sub("", stem, count=1)
        if stripped == stem:
            break
        stem = stripped
    return stem[:1].isupper() and match.group("initials").isupper()


def looks_like_author_list(text: str) -> bool:
    """True when a run of text is a byline rather than a claim.

    Dropping only the citation line would move the problem down one line: the
    author list that follows it is also long, also not the title, and equally
    devoid of propositional content.
    """
    segments = [segment.strip().rstrip(".") for segment in text.split(",")]
    segments = [segment for segment in segments if segment]
    if len(segments) < 2:
        return False
    names = sum(1 for segment in segments if is_author_name(segment))
    return names >= max(2, round(AUTHOR_LIST_THRESHOLD * len(segments)))


def looks_like_citation(candidate: str) -> bool:
    """True for a citation fragment; a DOI *inside* prose does not qualify.

    The named shapes are anchored at the start of the candidate. A bare DOI
    counts only in a short candidate, so a sentence that makes a claim *and*
    cites a dataset ("... are deposited at doi: 10.5281/zenodo.1") survives
    while the bibliographic fragment that only points at one does not.
    """
    if CITATION_LINE_RE.search(candidate):
        return True
    return len(candidate) <= CITATION_MAX_LENGTH and bool(
        DOI_CITATION_RE.search(candidate)
    )


def is_bibliographic(candidate: str) -> bool:
    """True for envelope text that describes the record rather than asserts anything."""
    if looks_like_citation(candidate):
        return True
    if AFFILIATION_MARKER_RE.match(candidate):
        return True
    if IMPRINT_LINE_RE.match(candidate):
        return True
    if MARKUP_NOISE_RE.search(candidate):
        return True
    return looks_like_author_list(candidate)


def is_bibliographic_paragraph(paragraph: str) -> bool:
    """True for a whole paragraph of record metadata.

    Every test here is anchored at the start of the paragraph, unlike the
    sentence-level :func:`is_bibliographic`. A paragraph is a much bigger thing
    to throw away, and an abstract that merely *mentions* a DOI is prose.
    """
    collapsed = re.sub(r"\s+", " ", paragraph).strip()
    if not collapsed:
        return False
    if collapsed.lower().startswith(BIBLIOGRAPHIC_PARAGRAPH_PREFIXES):
        return True
    if NUMBERED_CITATION_RE.match(collapsed) and (
        VOLUME_CITATION_RE.search(collapsed) or DOI_CITATION_RE.search(collapsed)
    ):
        return True
    if IDENTIFIER_TRAILER_RE.match(collapsed):
        return True
    if AFFILIATION_MARKER_RE.match(collapsed):
        return True
    if IMPRINT_LINE_RE.match(collapsed):
        return True
    return looks_like_author_list(collapsed)


def strip_bibliographic_paragraphs(text: str) -> str:
    """Drop the record's bibliographic envelope, keeping the prose (#8096).

    Plain-text PubMed/PMC bodies are blank-line-separated paragraphs, and the
    envelope ones (citation line, byline, ``Author information:`` block with its
    affiliations, identifier trailer) can be recognised whole where their
    individual lines cannot.
    """
    kept = [
        paragraph
        for paragraph in text.split("\n\n")
        if not is_bibliographic_paragraph(paragraph)
    ]
    return "\n\n".join(kept)


def normalize_cache_body(body: str) -> str:
    text = body
    if "## Content" in text:
        text = text.split("## Content", 1)[1]
    text = text.replace("\r", "\n")
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    text = re.sub(r"</?[^>\n]+>", " ", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = strip_bibliographic_paragraphs(text)
    if "BACKGROUND:" in text:
        text = text.split("BACKGROUND:", 1)[1]
    elif "\nBackground:" in text:
        text = text.split("\nBackground:", 1)[1]
    return re.sub(r"\s+", " ", text).strip()


def extract_cache_context(cache_path: Path) -> str:
    _, body = parse_cache_metadata_and_body(cache_path)
    return normalize_cache_body(body)


def strip_leading_section_labels(text: str) -> str:
    cleaned = text.strip().lstrip("•").strip()
    while True:
        updated = LEADING_SECTION_LABEL_RE.sub("", cleaned, count=1)
        updated = LEADING_SUBSECTION_LABEL_RE.sub("", updated, count=1)
        updated = LANGUAGE_NOTE_RE.sub("", updated, count=1)
        updated = LEADING_SECTION_NUMBER_RE.sub("", updated, count=1)
        updated = LEADING_CONJUNCTION_RE.sub("", updated, count=1)
        updated = ALLCAPS_HEADER_RE.sub("", updated, count=1)
        updated = updated.strip().lstrip("•").strip()
        if updated == cleaned:
            return cleaned
        cleaned = updated


def strip_leading_title(candidate: str, title: str) -> str:
    """Drop a title glued to the front of the first abstract sentence.

    The sentence splitter only breaks before ``[A-Z0-9(]``, so a title followed
    by an abstract opening on a quotation mark or a lowercase word arrives as
    one candidate and slips past the title-equality test.

    A sentence boundary has to follow the title text for it to count as a title.
    A review of a single disease is titled after that disease and its abstract
    opens with the same words as the sentence's *subject* -- "Scimitar syndrome."
    then "Scimitar syndrome is a rare congenital anomaly ..." -- and cutting the
    prefix there decapitates the claim into "is a rare congenital anomaly ...".
    That failure is invisible to every existing check, because the beheaded
    remainder is still a verbatim substring of the source.
    """
    stem = title.rstrip(" .")
    if not stem or not candidate.startswith(stem):
        return candidate
    remainder = candidate[len(stem) :]
    if remainder[:1] not in {".", "?", "!"}:
        return candidate
    return remainder.lstrip(" .:;?!")


def is_title_text(candidate: str, normalized_title: str) -> bool:
    """True when a candidate is the title, or any part of it.

    Containment rather than equality: a title carrying its own sentence break
    ("... interleukin-1beta? A preliminary study.") is split by the sentence
    splitter, so neither half ever *equals* the title, and the question half
    was being quoted as though it were a finding. A question is not a claim.
    """
    normalized_candidate = normalize_title(candidate)
    if not normalized_candidate or not normalized_title:
        return False
    return normalized_candidate in normalized_title


def supporting_text_candidates(normalized: str, title: str) -> Iterable[str]:
    normalized_title = normalize_title(title)
    for sentence in SENTENCE_SPLIT_RE.split(normalized):
        raw = sentence.strip(" \"'")
        # Recognise the title *before* any label surgery. A trial acronym reads
        # exactly like a section label -- "SEAMARK: phase II study of ..." --
        # so stripping first would leave a headless title that no longer
        # matches, and it would be returned as though it were an abstract
        # sentence.
        if is_title_text(raw, normalized_title):
            continue
        candidate = strip_leading_section_labels(raw)
        # Removing the title can uncover a label that was sitting behind it,
        # so the labels get a second pass.
        candidate = strip_leading_section_labels(
            strip_leading_title(candidate, title)
        )
        if len(candidate) < 40:
            continue
        if candidate.lower().startswith(("author information", "copyright")):
            continue
        if is_bibliographic(candidate):
            continue
        if is_title_text(candidate, normalized_title):
            continue
        yield candidate


def extract_supporting_text(cache_path: Path, title: str) -> str | None:
    """Pick the first sentence of the cached body that makes a claim.

    Bracket-free sentences win a first pass. ``linkml-reference-validator``
    treats ``[...]`` as an editorial insertion and strips it before matching, so
    a quote whose brackets hold real content -- "SPAK [STE20/SPS1-related
    proline/alanine-rich kinase]" -- fails to match the source it was copied
    verbatim from. Where the paper offers an equally good sentence without
    brackets, quoting that one keeps the evidence checkable.
    """
    normalized = extract_cache_context(cache_path)
    if not normalized:
        return None
    fallback: str | None = None
    for candidate in supporting_text_candidates(normalized, title):
        if "[" not in candidate and "]" not in candidate:
            return candidate
        if fallback is None:
            fallback = candidate
    return fallback


def guess_evidence_source(
    title: str, supporting_text: str | None, context_text: str | None = None
) -> str:
    title_haystack = title.lower()
    haystack = f"{title} {supporting_text or ''} {context_text or ''}".lower()

    def has(text: str, pattern: str) -> bool:
        return re.search(pattern, text) is not None

    review_pattern = (
        r"\b(systematic review|meta-analysis|consensus|guideline|statement)\b"
    )
    computational_pattern = (
        r"\b(in silico|simulation|docking|machine learning|network analysis|"
        r"computational|algorithm|predict(?:ion)?|forecast(?:ing)?|mathematical "
        r"model(?:ling|ing)|transmission models?|epifil|geofil|indirect measure)\b"
    )
    title_model_pattern = (
        r"\b(experimental models?|animal models?|infected mice|infected rats|murine|"
        r"mouse|mice|rat|rats|zebrafish|drosophila|porcine|pig|rabbit|rabbits|"
        r"nonhuman primate|macaque|hamster|hamsters|guinea pigs?|gerbil|gerbils|"
        r"mongolian gerbils?|veterinary)\b"
    )
    combined_model_pattern = (
        r"\b(mouse|mice|murine|rat|rats|zebrafish|drosophila|canine|dog|dogs|"
        r"porcine|pig|rabbit|rabbits|cat|cats|horse|horses|equine|bovine|cattle|"
        r"nonhuman primate|macaque|hamster|hamsters|guinea pigs?|gerbil|gerbils|"
        r"mongolian gerbils?|veterinary)\b"
    )
    human_pattern = (
        r"\b(patient|patients|cohort|trial|participants|adult|adults|child|children|"
        r"infants?|newborns?|neonates?|women|men|people|persons|population|"
        r"human|humans|epidemiolog(?:y|ical)|cross-sectional|mixed methods|survey|"
        r"dog bite cases?|dog owners?|case report|case series|prospective|retrospective|"
        r"hospital-based|post-exposure prophylaxis|preexposure prophylaxis|"
        r"vaccination schedule|public health|mortality|deaths?)\b"
    )
    in_vitro_pattern = (
        r"\b(in vitro|cell line|cell-based|cell culture|organoid|ex vivo|fibroblast|"
        r"keratinocyte)\b"
    )

    if has(haystack, review_pattern):
        return "OTHER"
    if has(haystack, computational_pattern):
        return "COMPUTATIONAL"
    if has(title_haystack, title_model_pattern):
        return "MODEL_ORGANISM"
    if has(title_haystack, in_vitro_pattern) and has(
        title_haystack, combined_model_pattern
    ):
        return "MODEL_ORGANISM"
    if has(haystack, in_vitro_pattern) and not has(haystack, human_pattern):
        return "IN_VITRO"
    if has(haystack, human_pattern):
        return "HUMAN_CLINICAL"
    if has(haystack, combined_model_pattern):
        return "MODEL_ORGANISM"
    if has(haystack, in_vitro_pattern):
        return "IN_VITRO"
    return "OTHER"


def ensure_findings_list(ref_item: MutableMapping[str, Any]) -> CommentedSeq:
    findings = ref_item.get("findings")
    if findings is None:
        findings = CommentedSeq()
        ref_item["findings"] = findings
        return findings
    if isinstance(findings, CommentedSeq):
        return findings
    if isinstance(findings, list):
        out = CommentedSeq()
        out.extend(findings)
        ref_item["findings"] = out
        return out
    out = CommentedSeq()
    ref_item["findings"] = out
    return out


def has_findings(ref_item: Mapping[str, Any]) -> bool:
    findings = ref_item.get("findings")
    return isinstance(findings, list) and len(findings) > 0


def append_auto_finding(
    ref_item: MutableMapping[str, Any],
    reference: str,
    title: str,
    disorder: str,
    cache_path: Path,
) -> bool:
    if has_findings(ref_item):
        return False

    supporting_text = extract_supporting_text(cache_path, title)
    context_text = extract_cache_context(cache_path)
    if supporting_text:
        statement = (
            supporting_text if len(supporting_text) <= 240 else title.rstrip(".")
        )
    else:
        statement = title.rstrip(".")

    finding = CommentedMap()
    finding["statement"] = statement
    finding["supporting_text"] = supporting_text or title

    if supporting_text:
        evidence_source = guess_evidence_source(title, supporting_text, context_text)
        evidence_item = CommentedMap()
        evidence_item["reference"] = reference
        evidence_item["reference_title"] = title
        evidence_item["supports"] = "SUPPORT"
        evidence_item["evidence_source"] = evidence_source
        evidence_item["snippet"] = supporting_text
        evidence_item["explanation"] = (
            f"Deep research cited this publication as relevant literature for "
            f"{disorder.replace('_', ' ')}."
        )
        finding["evidence"] = CommentedSeq([evidence_item])

    findings = ensure_findings_list(ref_item)
    findings.append(finding)
    return True


def repair_existing_findings(
    ref_item: MutableMapping[str, Any],
    reference: str,
    title: str,
    cache_path: Path,
) -> bool:
    changed = False
    cache_title = parse_cache_title(cache_path)
    effective_title = cache_title or title
    if ref_item.get("title") != effective_title:
        ref_item["title"] = effective_title
        changed = True

    findings = ref_item.get("findings")
    if not isinstance(findings, list):
        return changed

    supporting_text = extract_supporting_text(cache_path, effective_title)
    context_text = extract_cache_context(cache_path)
    statement = (
        supporting_text
        if supporting_text and len(supporting_text) <= 240
        else effective_title.rstrip(".")
    )

    for finding in findings:
        if not isinstance(finding, MutableMapping):
            continue
        if supporting_text:
            if finding.get("statement") != statement:
                finding["statement"] = statement
                changed = True
            if finding.get("supporting_text") != supporting_text:
                finding["supporting_text"] = supporting_text
                changed = True

        evidence_items = finding.get("evidence")
        if not isinstance(evidence_items, list):
            continue

        if not supporting_text:
            del finding["evidence"]
            changed = True
            continue

        evidence_source = guess_evidence_source(
            effective_title, supporting_text, context_text
        )
        for evidence in evidence_items:
            if not isinstance(evidence, MutableMapping):
                continue
            if evidence.get("reference_title") != effective_title:
                evidence["reference_title"] = effective_title
                changed = True
            if evidence.get("snippet") != supporting_text:
                evidence["snippet"] = supporting_text
                changed = True
            if evidence.get("evidence_source") != evidence_source:
                evidence["evidence_source"] = evidence_source
                changed = True

    return changed


def fetch_reference(reference: str, timeout_seconds: int) -> bool:
    cmd = ["just", "fetch-reference", reference]
    try:
        result = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False


def ensure_references_list(data: MutableMapping[str, Any]) -> CommentedSeq:
    refs = data.get("references")
    if refs is None:
        refs = CommentedSeq()
        data["references"] = refs
        return refs
    if isinstance(refs, CommentedSeq):
        return refs
    if isinstance(refs, list):
        out = CommentedSeq()
        out.extend(refs)
        data["references"] = out
        return out
    out = CommentedSeq()
    data["references"] = out
    return out


def append_publication_reference(
    refs: MutableMapping[str, Any] | CommentedSeq,
    reference: str,
    title: str,
    found_in: Iterable[str] | None = None,
) -> None:
    if not isinstance(refs, (list, CommentedSeq)):
        return
    ref_item = CommentedMap()
    ref_item["reference"] = reference
    ref_item["title"] = title
    if found_in:
        ref_item["found_in"] = CommentedSeq(sorted(set(found_in)))
    ref_item["findings"] = CommentedSeq()
    refs.append(ref_item)


def normalize_found_in_entries(value: Any) -> set[str]:
    if isinstance(value, str):
        entry = value.strip()
        return {entry} if entry else set()
    if isinstance(value, list):
        out = set()
        for item in value:
            if isinstance(item, str):
                entry = item.strip()
                if entry:
                    out.add(entry)
        return out
    return set()


def merge_found_in(ref_item: MutableMapping[str, Any], found_in: Iterable[str]) -> bool:
    new_entries = {
        entry.strip() for entry in found_in if isinstance(entry, str) and entry.strip()
    }
    if not new_entries:
        return False

    existing_entries = normalize_found_in_entries(ref_item.get("found_in"))
    merged_entries = sorted(existing_entries.union(new_entries))
    if merged_entries == sorted(existing_entries):
        return False

    seq = CommentedSeq()
    seq.extend(merged_entries)
    ref_item["found_in"] = seq
    return True


def migrate_holder_to_references(
    data: MutableMapping[str, Any],
    references_cache_dir: str,
) -> int:
    """Move legacy deep-research holder evidence refs to top-level references."""
    pathophys = data.get("pathophysiology")
    if not isinstance(pathophys, (list, CommentedSeq)):
        return 0

    refs = ensure_references_list(data)
    existing_top_refs: set[str] = set()
    for item in refs:
        if isinstance(item, Mapping) and isinstance(item.get("reference"), str):
            canon = canonical_ref(item.get("reference", ""))
            if canon:
                existing_top_refs.add(canon)

    moved = 0
    to_remove = []
    for idx, item in enumerate(pathophys):
        if not (isinstance(item, MutableMapping) and item.get("name") == HOLDER_NAME):
            continue
        ev = item.get("evidence")
        if isinstance(ev, list):
            for e in ev:
                if not isinstance(e, Mapping):
                    continue
                ref_val = e.get("reference")
                if not isinstance(ref_val, str):
                    continue
                canon = canonical_ref(ref_val)
                if not canon or canon in existing_top_refs:
                    continue
                title = None
                snip = e.get("snippet")
                if isinstance(snip, str) and snip.strip():
                    title = snip.strip()
                if not title:
                    cache_path = cache_path_for_ref(canon, references_cache_dir)
                    title = parse_cache_title(cache_path) or canon
                append_publication_reference(refs, canon, title)
                existing_top_refs.add(canon)
                moved += 1
        to_remove.append(idx)

    for idx in reversed(to_remove):
        del pathophys[idx]

    return moved


def main() -> int:
    args = parse_args()
    only = set(args.only or [])

    kb_paths = {
        Path(path).stem: Path(path)
        for path in glob.glob(os.path.join(args.kb_dir, "*.yaml"))
        if not path.endswith(".history.yaml")
    }
    deep_refs_by_disorder = citations_by_disorder(args.research_dir)

    disorders = sorted(name for name in deep_refs_by_disorder if name in kb_paths)
    if only:
        disorders = [name for name in disorders if name in only]
    if args.max_disorders is not None:
        disorders = disorders[: args.max_disorders]

    yaml_rt = YAML()
    yaml_rt.preserve_quotes = True
    yaml_rt.indent(mapping=2, sequence=2, offset=0)
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    results: list[DisorderResult] = []
    unresolved_rows: list[tuple[str, str, str]] = []

    for idx, disorder in enumerate(disorders, start=1):
        yaml_path = kb_paths[disorder]
        cited_ref_to_files = deep_refs_by_disorder[disorder]
        cited_refs = set(cited_ref_to_files.keys())

        with yaml_path.open("r", encoding="utf-8") as handle:
            data = yaml_rt.load(handle)
        if data is None:
            continue

        existing_refs: set[str] = set()
        collect_existing_refs(data, existing_refs)
        existing_titles: set[str] = set()
        collect_existing_titles(data, existing_titles)

        preloaded_titles: dict[str, str] = {}
        missing_refs = []
        for ref in sorted(cited_refs):
            if ref in existing_refs:
                continue
            cache_path = cache_path_for_ref(ref, args.references_cache_dir)
            if not cache_path.exists() and args.fetch_missing_cache:
                fetch_reference(ref, args.fetch_timeout_seconds)
            title = parse_cache_title(cache_path)
            if title:
                preloaded_titles[ref] = title
                if normalize_title(title) in existing_titles:
                    continue
            missing_refs.append(ref)
        if args.max_new_refs_per_disorder is not None:
            missing_refs = missing_refs[: args.max_new_refs_per_disorder]

        print(
            f"[{idx}/{len(disorders)}] {disorder}: "
            f"cited={len(cited_refs)} existing={len(existing_refs)} missing={len(missing_refs)}"
        )

        added = 0
        unresolved = 0
        changed = False

        migrated = migrate_holder_to_references(
            data=data,
            references_cache_dir=args.references_cache_dir,
        )
        if migrated > 0:
            changed = True

        if missing_refs:
            refs = ensure_references_list(data)
            top_ref_items: dict[str, MutableMapping[str, Any]] = {}
            top_ref_titles: dict[str, MutableMapping[str, Any]] = {}
            for item in refs:
                if (
                    isinstance(item, MutableMapping)
                    and isinstance(item.get("reference"), str)
                    and (canon := canonical_ref(item.get("reference", "")))
                ):
                    top_ref_items[canon] = item
                    item_title = item.get("title")
                    if isinstance(item_title, str):
                        normalized = normalize_title(item_title)
                        if normalized:
                            top_ref_titles[normalized] = item

            for reference, found_in in cited_ref_to_files.items():
                existing_item = top_ref_items.get(reference)
                if existing_item is None:
                    title = preloaded_titles.get(reference)
                    if title:
                        existing_item = top_ref_titles.get(normalize_title(title))
                if existing_item and merge_found_in(existing_item, found_in):
                    changed = True
                if (
                    existing_item
                    and args.add_findings
                    and isinstance(existing_item.get("reference"), str)
                ):
                    canon = canonical_ref(existing_item["reference"])
                    if canon:
                        cache_path = cache_path_for_ref(
                            canon, args.references_cache_dir
                        )
                        if not cache_path.exists() and args.fetch_missing_cache:
                            fetch_reference(canon, args.fetch_timeout_seconds)
                        title = existing_item.get("title")
                        if isinstance(title, str) and title.strip() and append_auto_finding(
                            existing_item,
                            canon,
                            title.strip(),
                            disorder,
                            cache_path,
                        ):
                            changed = True

            for reference in missing_refs:
                if reference in top_ref_items:
                    continue

                cache_path = cache_path_for_ref(reference, args.references_cache_dir)
                if not cache_path.exists() and args.fetch_missing_cache:
                    fetch_reference(reference, args.fetch_timeout_seconds)

                title = preloaded_titles.get(reference) or parse_cache_title(cache_path)
                if not title:
                    unresolved += 1
                    unresolved_rows.append(
                        (disorder, reference, "cache_not_found_or_no_title")
                    )
                    continue

                existing_by_title = top_ref_titles.get(normalize_title(title))
                if existing_by_title is not None:
                    if merge_found_in(
                        existing_by_title, cited_ref_to_files.get(reference, set())
                    ):
                        changed = True
                    existing_ref_value = existing_by_title.get("reference")
                    existing_title = existing_by_title.get("title")
                    if (
                        args.add_findings
                        and isinstance(existing_ref_value, str)
                        and isinstance(existing_title, str)
                        and (canon := canonical_ref(existing_ref_value))
                    ):
                        existing_cache_path = cache_path_for_ref(
                            canon, args.references_cache_dir
                        )
                        if (
                            not existing_cache_path.exists()
                            and args.fetch_missing_cache
                        ):
                            fetch_reference(canon, args.fetch_timeout_seconds)
                        if append_auto_finding(
                            existing_by_title,
                            canon,
                            existing_title,
                            disorder,
                            existing_cache_path,
                        ):
                            changed = True
                    continue

                append_publication_reference(
                    refs,
                    reference,
                    title,
                    found_in=cited_ref_to_files.get(reference, set()),
                )
                new_item = refs[-1]
                if isinstance(new_item, MutableMapping):
                    top_ref_items[reference] = new_item
                    top_ref_titles[normalize_title(title)] = new_item
                    if args.add_findings and append_auto_finding(
                        new_item,
                        reference,
                        title,
                        disorder,
                        cache_path,
                    ):
                        changed = True
                added += 1
                changed = True
        else:
            refs = ensure_references_list(data)
            for item in refs:
                if (
                    isinstance(item, MutableMapping)
                    and isinstance(item.get("reference"), str)
                    and (canon := canonical_ref(item.get("reference", "")))
                    and canon in cited_ref_to_files
                    and merge_found_in(item, cited_ref_to_files[canon])
                ):
                    changed = True
                if (
                    args.add_findings
                    and isinstance(item, MutableMapping)
                    and isinstance(item.get("reference"), str)
                    and (canon := canonical_ref(item.get("reference", "")))
                    and canon in cited_ref_to_files
                ):
                    cache_path = cache_path_for_ref(canon, args.references_cache_dir)
                    if not cache_path.exists() and args.fetch_missing_cache:
                        fetch_reference(canon, args.fetch_timeout_seconds)
                    title = item.get("title")
                    if isinstance(title, str) and title.strip() and append_auto_finding(
                        item,
                        canon,
                        title.strip(),
                        disorder,
                        cache_path,
                    ):
                        changed = True

        if args.repair_findings:
            refs = ensure_references_list(data)
            for item in refs:
                if not (
                    isinstance(item, MutableMapping)
                    and isinstance(item.get("reference"), str)
                    and (canon := canonical_ref(item.get("reference", "")))
                    and canon in cited_ref_to_files
                ):
                    continue
                cache_path = cache_path_for_ref(canon, args.references_cache_dir)
                if not cache_path.exists() and args.fetch_missing_cache:
                    fetch_reference(canon, args.fetch_timeout_seconds)
                title = item.get("title")
                if not isinstance(title, str) or not title.strip():
                    title = canon
                if repair_existing_findings(
                    item,
                    canon,
                    title.strip(),
                    cache_path,
                ):
                    changed = True

        if changed and args.apply:
            if "updated_date" in data:
                data["updated_date"] = now_iso
            with yaml_path.open("w", encoding="utf-8") as handle:
                yaml_rt.dump(data, handle)

        results.append(
            DisorderResult(
                disorder=disorder,
                cited_refs=len(cited_refs),
                existing_refs=len(existing_refs),
                missing_refs=len(missing_refs),
                added_refs=added,
                unresolved_refs=unresolved,
                changed=changed,
            )
        )

    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    summary_path = Path(args.output_dir) / f"deep_research_evidence_backfill_{ts}.tsv"
    unresolved_path = Path(args.output_dir) / f"deep_research_unresolved_refs_{ts}.tsv"

    with summary_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "disorder",
                "cited_refs",
                "existing_refs",
                "missing_refs",
                "added_refs",
                "unresolved_refs",
                "changed",
            ]
        )
        for row in results:
            writer.writerow(
                [
                    row.disorder,
                    row.cited_refs,
                    row.existing_refs,
                    row.missing_refs,
                    row.added_refs,
                    row.unresolved_refs,
                    str(row.changed),
                ]
            )

    with unresolved_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["disorder", "reference", "reason"])
        writer.writerows(unresolved_rows)

    total_added = sum(r.added_refs for r in results)
    total_missing = sum(r.missing_refs for r in results)
    total_unresolved = sum(r.unresolved_refs for r in results)
    changed_count = sum(1 for r in results if r.changed)
    mode = "APPLY" if args.apply else "DRY_RUN"
    print(
        f"{mode} summary: disorders={len(results)} changed={changed_count} "
        f"missing_refs={total_missing} added_refs={total_added} "
        f"unresolved_refs={total_unresolved}"
    )
    print(f"Summary report: {summary_path}")
    print(f"Unresolved refs: {unresolved_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
