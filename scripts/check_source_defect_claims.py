#!/usr/bin/env python3
"""Adjudicate free-text claims that a *cited source* is defective (#9226).

Every existing gate in this repo checks a **snippet against the cache**. Nothing
checks **prose against the cache**. So a curator can write, in free text, that a
source is truncated, has no abstract, or fails to mention some finding -- and if
that is false, nothing here notices. On #9207 one false claim ("the cached
abstract is truncated mid-word") survived two fix rounds across three sites,
validating cleanly the whole time. The same defect had already happened once
before, in ``Tetralogy_of_Fallot.yaml``, where four such claims were false; the
correction note recorded the root cause as *a fixed-width extraction window used
during curation* -- i.e. a truncated **read** of the cache, written down as a
property of the **source**.

What this is not
----------------
This is **not** a keyword blacklist, and it must not become one. Claims of this
shape are usually *true and load-bearing*:

* ``Acute_Annular_Outer_Retinopathy.yaml`` downgrades three evidence items to
  PARTIAL because ``PMID:18195232`` genuinely has no abstract -- the cached
  record holds a MEDLINE citation stub and nothing else.
* ``Cri-du-Chat_Syndrome.yaml`` and ``DTYMK-Related_Neurodegeneration.yaml``
  explain that a snippet legitimately begins mid-word, because the cached PDF
  breaks a word across a line (the #8048 hyphenation defect).
* ``Tetralogy_of_Fallot.yaml`` narrates the correction of the earlier false
  claims, and necessarily restates them to do so.

Flagging those would be worse than having no check: it would train curators to
delete accurate provenance to get a build green. So this tool **adjudicates
against the cache** rather than pattern-matching, and reports three verdicts:

``CONTRADICTED``
    The cache demonstrably disagrees with the claim. This is the finding.
``CONFIRMED``
    The cache agrees. Counted, never printed as a problem -- the four entries
    above all land here.
``UNDETERMINED``
    Not mechanically decidable (no resolvable reference, an object phrase too
    vague to search, a truncation claim with no exact test). Reported for a
    glance under ``--all``, never as a failure.

Claim classes
-------------
``NO_ABSTRACT``
    "no abstract", "abstract is unavailable/incomplete/missing". Adjudicated by
    asking whether the cached record actually carries abstract prose.

    Note this deliberately does **not** use the frontmatter ``content_type``
    alone, which was the originally proposed test. ``PMID:18195232`` is typed
    ``abstract_only`` and has *no abstract*: PubMed emits a citation stub for a
    record that never had one, and the fetcher types it the same way as a real
    abstract. A ``content_type``-only test would therefore contradict one of the
    clearest true claims in the KB. See :func:`abstract_prose`.

``NEGATIVE_EXISTENCE``
    "the (cached) abstract does not mention/contain/state/... X", which is used
    to justify *omitting or downgrading evidence* -- so a false one silently
    suppresses real curation. The most mechanically decidable class: extract X,
    search the cached body. Adjudicated only when X is specific enough to search
    unambiguously (see :func:`searchable_object`); vague objects stay
    UNDETERMINED rather than risking a wrong contradiction.

``DEFECTIVE_TEXT``
    truncation / mid-word / garbled claims. No exact test exists, so these are
    always UNDETERMINED: reported, never adjudicated. The trigger requires the
    defect word to co-occur with a word naming *our stored text* -- otherwise
    ``truncat`` matches 1,600+ occurrences of ``truncating variant`` and
    ``truncated protein``, which are correct genetics prose about a protein, not
    a claim about a file.

Exit status
-----------
Report-only: exit 0 even with findings, matching the design in #9226. Use
``--strict`` (not wired into ``just qc`` or CI) to gate on CONTRADICTED
verdicts only.

Offline: no OAK, no network. Same class as ``check-duplicate-keys``.

Usage
-----
    python scripts/check_source_defect_claims.py                  # report
    python scripts/check_source_defect_claims.py --all            # every claim + verdict
    python scripts/check_source_defect_claims.py --count          # summary only
    python scripts/check_source_defect_claims.py --strict         # exit 1 on CONTRADICTED
    python scripts/check_source_defect_claims.py kb/disorders/X.yaml
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from dismech.reference_snippet_audit import (
    DEFAULT_CONFIG,
    CachedReferenceIndex,
    load_cache_dir,
)
from dismech.yaml_io import safe_load

SCAN_DIR = ROOT / "kb"

# Free-text slots a claim about a source can hide in. All seven are real slots
# in src/dismech/schema/dismech.yaml. `notes` is deliberately included even
# though it carries the most legitimate narration: it is where #9207's *first*
# finding was, and exempting it would make round one silent and leave the gate
# strictly worse than the reviewer it assists.
PROSE_FIELDS = frozenset(
    {
        "description",
        "explanation",
        "notes",
        "association",
        "rationale",
        "interpretation",
        "limitations",
    }
)

# Words naming *our stored copy* of a source, as opposed to the source's own
# subject matter. A defect word only counts as a claim about a cached reference
# if one of these sits near it.
CACHE_CONTEXT = re.compile(
    r"\b(cache|cached|caching|abstract|snippet|quote|quotation|excerpt|"
    r"record|reference|citation|extraction|text|pdf|pubmed|medline)\b"
    r"|\b(?:PMID|DOI|PMC|ORPHA|NCT|ICTRP)\s*:",
    re.IGNORECASE,
)

# How far either side of a defect word to look for CACHE_CONTEXT. Generous,
# because a false trigger costs one UNDETERMINED line, while a miss costs the
# whole point of the check.
CONTEXT_WINDOW = 160

# The genetics senses of "truncate". These describe a *protein or transcript*,
# never a file, and dominate the KB ~1,600 to a handful. Excluded at the match
# site so the co-occurrence window cannot rescue them.
GENETICS_TRUNCATION = re.compile(
    r"truncat\w*\s+(?:variant|mutation|allele|protein|change|transcript|"
    r"polypeptide|product|form|isoform|frameshift)"
    r"|(?:protein|premature|peptide|gene|c-terminal|n-terminal|terminal)[-\s]+truncat"
    r"|truncat\w*\s+(?:the\s+)?(?:protein|transcript|polypeptide|receptor|enzyme)",
    re.IGNORECASE,
)

DEFECT_WORD = re.compile(
    r"\btruncat\w*|\bmid-?word\b|\bgarbled\b|\bstops where\b|\bcut[-\s]off\b"
    r"|\bmangled\b|\bcorrupted\b",
    re.IGNORECASE,
)

# "cut-off"/"cutoff" is overwhelmingly a *diagnostic threshold* here (a ferritin
# cut-off of 16%). Require an explicit textual object for it, not merely nearby
# cache vocabulary, or every biomarker note trips the check.
DIAGNOSTIC_CUTOFF = re.compile(
    r"cut[-\s]?off\s+(?:of|for|at|value|point|threshold)|"
    r"(?:a|the|this|diagnostic|optimal|recommended|\d[\d.%]*)\s+cut[-\s]?off",
    re.IGNORECASE,
)

# "abstract" is also an *adjective* here -- "no abstract sentence states the
# complication", "no abstract-level source was available" are claims about what
# the text says, not about whether an abstract exists. Matching them as
# no-abstract claims contradicted four true statements in the first run over
# kb/, so the head noun is excluded explicitly.
_ABSTRACT_AS_ADJECTIVE = (
    r"(?!\s*-?\s*(?:level|sentence|statement|source|quote|quotation|phrase|"
    r"wording|passage|line|text|evidence|claim|support|snippet)\b)"
)

_NO_ABSTRACT_CORE = re.compile(
    r"\b(?:no|without\s+an?|lacks?\s+an?|lacking\s+an?|is\s+missing\s+an?)\s+"
    r"(?:cached\s+|PubMed\s+|real\s+|proper\s+|usable\s+)?abstract\b"
    + _ABSTRACT_AS_ADJECTIVE,
    re.IGNORECASE,
)

# Standalone forms whose subject is unambiguously the abstract itself.
_ABSTRACT_STATE = re.compile(
    r"\babstract\s+is\s+(?:incomplete|unavailable|missing|absent|empty)\b"
    r"|\babstract\s+(?:was|is)\s+not\s+(?:available|cached|present)\b",
    re.IGNORECASE,
)

# A no-abstract claim is about ONE cached record, so it needs a record to be
# about. Without this anchor the pattern also swallows set-level claims --
# "no cached abstract in this curation pass gives a proportion for pulmonary
# embolism" -- which assert that nothing in the whole reference set says X, not
# that some record lacks an abstract. Ten of the twenty-two contradictions in
# the first tightened run over kb/ were of that shape, and every one of them was
# a true statement being contradicted on the strength of an unrelated PMID.
_RECORD_NOUN = re.compile(
    r"\b(?:record|reference|report|paper|publication|article|letter|citation|"
    r"chapter|preprint|editorial|abstract|entry|erratum|comment)\b"
    r"|\b(?:PMID|DOI|PMC)\s*:\s*\S+",
    re.IGNORECASE,
)
RECORD_ANCHOR_WINDOW = 60

# `abstract` as the SUBJECT of a saying-verb is a claim about content, not
# existence: "no cached abstract states the practice in quotable form" is true
# of a reference set whose members all have abstracts.
_SET_LEVEL_CONTENT = re.compile(
    r"^\s*(?:\w+\s+){0,6}?"
    r"(?:states?|stated|gives?|gave|supplies|supplied|provides?|provided|"
    r"reports?|reported|mentions?|mentioned|makes?|made|says?|said|"
    r"describes?|described|quantifies|quantified|specifies|specified|"
    r"documents?|documented|establishes|established|addresses|addressed|"
    r"covers?|covered|supports?|supported|contains?|contained|carries|carried)\b",
    re.IGNORECASE,
)


def _is_record_anchored(text: str, start: int) -> bool:
    """True when a record noun sits just before *start*, in the same clause."""
    window = text[max(0, start - RECORD_ANCHOR_WINDOW) : start]
    # Do not reach across a sentence boundary for the subject.
    cut = max(window.rfind(". "), window.rfind("; "), window.rfind(": "))
    if cut >= 0:
        window = window[cut + 1 :]
    return bool(_RECORD_NOUN.search(window))


def find_no_abstract_claims(text: str) -> list[tuple[int, int]]:
    """Spans of *text* asserting that a specific cached record has no abstract."""
    spans: list[tuple[int, int]] = []
    for match in _NO_ABSTRACT_CORE.finditer(text):
        if _SET_LEVEL_CONTENT.match(text[match.end() : match.end() + 80]):
            continue
        if not _is_record_anchored(text, match.start()):
            continue
        spans.append((match.start(), match.end()))
    for match in _ABSTRACT_STATE.finditer(text):
        spans.append((match.start(), match.end()))
    return spans


NEGATIVE_EXISTENCE = re.compile(
    r"\babstract\s+(?:does|do|did)\s+not\s+"
    # Stop at a comma as well as a sentence boundary: "does not mention
    # nystagmus, so this phenotype carries no evidence item" is about
    # nystagmus, and the trailing clause is unsearchable.
    r"(mention|contain|state|specify|name|quantify|report|include|give|"
    r"provide|describe|record|identify)\s+(?P<object>[^.;:,]{1,120})",
    re.IGNORECASE,
)

# Determiners and generic head nouns that make an object phrase unsearchable.
# "does not specify the mouse allele" is a claim about *which* allele, not about
# whether the words "mouse" and "allele" occur -- adjudicating it on token
# presence would contradict a true claim.
# Grouped by why each word is unsearchable, not alphabetically: determiners and
# pronouns, then generic nouns for "a thing a paper reports", then the domain
# head nouns that a qualifier almost always narrows ("the mouse ALLELE"), then
# function words.
_STOPWORD_TEXT = """
    a an the this that these those its their his her our any some such
    other another either neither each every both all no not more most less
    least much many few several one two three
    it they them he she we you i

    value values number numbers detail details data datum result results
    finding findings figure figures outcome outcomes measure measures
    information evidence study studies paper papers report reports
    analysis analyses method methods design designs

    allele alleles variant variants mutation mutations genotype genotypes
    gene genes protein proteins
    patient patients case cases cohort cohorts subject subjects
    dose doses dosing duration timing frequency frequencies rate rates
    age ages sex onset severity size sizes
    mechanism mechanisms pathway pathways process processes
    type types form forms kind kinds subtype subtypes
    effect effects change changes level levels

    which what whether how why when where who
    specific exact precise direct explicit particular relevant
    of in on at to for from with without by as is are was were be been
    and or but if then than so that
"""

_STOPWORDS = frozenset(_STOPWORD_TEXT.split())

# Objects that ARE specific enough to search even though short: a gene symbol,
# an accession, a numeric quantity, an ontology CURIE.
_SPECIFIC_TOKEN = re.compile(r"^(?:[A-Z0-9][A-Z0-9\-]{1,}[0-9A-Z]|[A-Z]{2,})$")


class Verdict(Enum):
    """Outcome of adjudicating one claim against the cache."""

    CONTRADICTED = "CONTRADICTED"
    CONFIRMED = "CONFIRMED"
    UNDETERMINED = "UNDETERMINED"
    NARRATED = "NARRATED"


class ClaimKind(Enum):
    NO_ABSTRACT = "no-abstract"
    NEGATIVE_EXISTENCE = "negative-existence"
    DEFECTIVE_TEXT = "defective-text"


# A sentence can *report* a source-defect claim without asserting it. The
# canonical case is the correction paragraph in ``Tetralogy_of_Fallot.yaml``,
# which exists precisely because four such claims there were false and has to
# restate them to say so. Contradicting that paragraph would be the worst
# possible outcome for this check: it would push a curator to delete the one
# record of the defect this whole gate exists to catch.
_NARRATION = re.compile(
    r"\b(?:earlier|previous(?:ly)?|prior|former(?:ly)?|original(?:ly)?|initial(?:ly)?)"
    r"\s+(?:\w+\s+){0,2}(?:revision|version|note|draft|commit|pass|entry|claim|"
    r"assertion|statement|round|curation)\b"
    r"|\b(?:asserted|claimed|believed|assumed|supposed|purported|alleged)\b"
    r"|\b(?:incorrectly|wrongly|erroneously|mistakenly|falsely)\b"
    r"|\b(?:was|were|is|are)\s+(?:all\s+)?(?:false|untrue|incorrect|wrong|mistaken)\b"
    r"|\bin\s+fact\b|\bturned\s+out\b|\b(?:corrected|retracted|superseded)\b"
    r"|\b(?:can|could|may|might)\s+go\s+stale\b",
    re.IGNORECASE,
)


def is_narration(sentence: str) -> bool:
    """True when *sentence* reports a source-defect claim rather than asserting it."""
    return bool(_NARRATION.search(sentence))


@dataclass(frozen=True)
class Claim:
    """One prose assertion about a cited source."""

    path: str
    location: str
    kind: ClaimKind
    text: str
    references: tuple[str, ...]
    obj: str | None = None


@dataclass(frozen=True)
class Finding:
    claim: Claim
    verdict: Verdict
    reason: str
    reference_id: str | None = None

    def format(self) -> str:
        ref = self.reference_id or ("unresolved" if not self.claim.references else "-")
        return (
            f"{self.claim.path}:{self.claim.location}\n"
            f"    verdict:   {self.verdict.value} ({self.claim.kind.value})\n"
            f"    reference: {ref}\n"
            f"    claim:     {self.claim.text}\n"
            f"    {self.reason}"
        )


# --------------------------------------------------------------------------
# Claim detection
# --------------------------------------------------------------------------


def _sentence_around(text: str, start: int, end: int) -> str:
    """The sentence containing ``text[start:end]``, collapsed to one line."""
    left = max(text.rfind(". ", 0, start), text.rfind("\n", 0, start))
    right = text.find(". ", end)
    left = 0 if left < 0 else left + 1
    right = len(text) if right < 0 else right + 1
    return " ".join(text[left:right].split())


def _has_cache_context(text: str, start: int, end: int) -> bool:
    window = text[max(0, start - CONTEXT_WINDOW) : end + CONTEXT_WINDOW]
    return bool(CACHE_CONTEXT.search(window))


def find_claims_in_text(
    text: str,
) -> list[tuple[ClaimKind, str, str | None, int]]:
    """Yield ``(kind, sentence, object, offset)`` for each source-defect claim.

    ``offset`` is where the claim starts within *text*, which is what lets
    reference resolution tell an anaphoric subject named in the previous
    sentence from a contrasting citation named after the claim.
    """
    found: list[tuple[ClaimKind, str, str | None, int]] = []
    seen: set[tuple[ClaimKind, str]] = set()

    def add(
        kind: ClaimKind, sentence: str, offset: int, obj: str | None = None
    ) -> None:
        key = (kind, sentence)
        if key not in seen:
            seen.add(key)
            found.append((kind, sentence, obj, offset))

    for match in NEGATIVE_EXISTENCE.finditer(text):
        add(
            ClaimKind.NEGATIVE_EXISTENCE,
            _sentence_around(text, match.start(), match.end()),
            match.start(),
            " ".join(match.group("object").split()),
        )

    for start, end in find_no_abstract_claims(text):
        add(ClaimKind.NO_ABSTRACT, _sentence_around(text, start, end), start)

    for match in DEFECT_WORD.finditer(text):
        token = match.group(0).lower()
        # The genetics sense of "truncate" is about a protein, not a file.
        if token.startswith("truncat") and GENETICS_TRUNCATION.search(
            text[max(0, match.start() - 40) : match.end() + 40]
        ):
            continue
        # A diagnostic cut-off is a threshold, not a damaged quote.
        if "cut" in token and DIAGNOSTIC_CUTOFF.search(
            text[max(0, match.start() - 40) : match.end() + 40]
        ):
            continue
        if not _has_cache_context(text, match.start(), match.end()):
            continue
        add(
            ClaimKind.DEFECTIVE_TEXT,
            _sentence_around(text, match.start(), match.end()),
            match.start(),
        )

    return found


# --------------------------------------------------------------------------
# Reference resolution
# --------------------------------------------------------------------------

INLINE_REFERENCE = re.compile(
    r"\b(PMID|PMC|DOI|ORPHA|NCT|ICTRP|CGGV|CGDS|ICEES|STRCHIVE|NCIT)\s*:\s*"
    r"(?P<id>[^\s,;)\]]+)",
    re.IGNORECASE,
)

# How far back an anaphoric subject ("That reference ... has no abstract") may
# reach for the id it refers to. Beyond this the nearest preceding id in a long
# `notes:` paragraph is more likely coincidence than antecedent.
ANAPHORA_WINDOW = 400


def inline_references(text: str) -> tuple[str, ...]:
    """Reference ids named inside the prose itself, e.g. ``PMID:12345678``."""
    ids = []
    for match in INLINE_REFERENCE.finditer(text):
        prefix = match.group(1).upper()
        ident = match.group("id").rstrip(".,;:)]")
        if ident:
            ids.append(f"{prefix}:{ident}")
    return tuple(dict.fromkeys(ids))


def antecedent_reference(text: str, offset: int) -> str | None:
    """The id a claim at *offset* most likely refers to, if one precedes it.

    Only ids BEFORE the claim count, and only the nearest one. Position is what
    separates the two ways this goes wrong, and they pull in opposite
    directions:

    * an anaphoric subject reaches *backwards*, often across a sentence break --
      ``...in a CONDSIAS patient (PMID:39417910). That reference was fetched and
      cached but its record contains only bibliographic metadata with no
      abstract``. Sentence-scoped resolution loses the antecedent and blames the
      evidence item's own reference instead;
    * a contrasting citation sits *after* the claim -- ``this abstract does not
      name SETD5 ... which rests on PMID:41957673``. That id is the paper the
      claim defers TO, not the one it is about, and resolving to it contradicts
      a true statement.
    """
    window_start = max(0, offset - ANAPHORA_WINDOW)
    preceding = inline_references(text[window_start:offset])
    return preceding[-1] if preceding else None


def ambiguous_antecedent(text: str, offset: int) -> bool:
    """True when the prose names rival references and none is close enough to pick.

    If the curator named references in this field, the claim is about one of
    *those*, not about whatever the enclosing evidence block happens to cite --
    so falling through to the enclosing scope invents a subject. With two or
    more rivals and no antecedent inside :data:`ANAPHORA_WINDOW`, there is no
    honest way to choose, and UNDETERMINED is the answer.

    This is the OI-type-XXI case, and it is the failure mode this whole tool
    warns about, turned on itself. ``Osteogenesis_Imperfecta_Type_XXI.yaml``
    says the *Efthymiou et al. 2021* report has no PubMed abstract -- true,
    ``PMID:33964184`` is a citation stub with no abstract body. But that id sits
    678 characters back, 278 outside the window, so resolution fell through to
    the enclosing block's ``PMID:33053334`` (van Dijk 2020, which does have an
    abstract) and contradicted a correct note. A curator acting on that report
    would have deleted accurate provenance.

    One named reference is not ambiguous, however far back it sits: there is no
    rival to confuse it with, so :func:`resolve_references` uses it rather than
    giving up. Widening the window instead was rejected -- it moves the cliff
    without removing it. Disambiguating by the author-year the prose usually
    carries ("the Efthymiou et al. 2021 report") against the cache's own
    ``authors``/``year`` frontmatter would resolve this case affirmatively, but
    it is more machinery than a report-only tool warrants; UNDETERMINED already
    keeps the finding set honest.
    """
    return (
        len(inline_references(text[:offset])) > 1
        and antecedent_reference(text, offset) is None
    )


def _subtree_references(node) -> list[str]:
    out: list[str] = []
    if isinstance(node, dict):
        value = node.get("reference")
        if isinstance(value, str) and value.strip():
            out.append(value.strip())
        for key, child in node.items():
            if key != "reference":
                out.extend(_subtree_references(child))
    elif isinstance(node, list):
        for child in node:
            out.extend(_subtree_references(child))
    return out


def resolve_references(
    text: str, offset: int, ancestors: list[dict]
) -> tuple[str, ...]:
    """References a claim is about, most specific first.

    Three tiers, in order:

    1. the nearest id named *before* the claim (:func:`antecedent_reference`),
       which is what an anaphoric subject refers to. Resolving against every id
       in the field instead let an unrelated one decide the verdict -- three
       wrong contradictions in ``Bachmann-Bupp_Syndrome.yaml`` alone -- and
       scoping to the claim sentence lost the antecedent when it sat in the
       previous one;
    2. the single id named *before* the claim anywhere in the field, if there is
       exactly one. With no rival it is unambiguous however far back it sits.
       Two or more, with none inside the window, resolves to nothing at all
       (:func:`ambiguous_antecedent`) -- the enclosing scope must NOT stand in
       for a subject the prose named itself. Ids named *after* the claim are
       contrasts and never candidates here;
    3. a ``reference:`` on the mapping the prose sits in. An ``explanation:``
       explains *its own* evidence item, so the sibling beats any id named
       after the claim;
    4. every ``reference:`` in the nearest enclosing object that carries an
       ``evidence:`` block -- a pathophysiology ``description:`` has no sibling
       ``reference:``, its references live in a child ``evidence:`` list, so a
       same-mapping definition of "adjacent" would drop that site (it was one of
       #9207's three).
    """
    antecedent = antecedent_reference(text, offset)
    if antecedent is not None:
        return (antecedent,)

    # Rival ids, none near enough to pick. Falling through to the enclosing
    # scope would invent a subject, so resolve to nothing instead. Calling the
    # predicate rather than restating it keeps the tested condition and the
    # enforced one the same thing.
    if ambiguous_antecedent(text, offset):
        return ()

    # Only ids BEFORE the claim are candidate subjects. One named after it is a
    # contrast ("...which rests on PMID:X"), and letting that stand in as the
    # subject is what contradicted a true claim in
    # SETD5_Haploinsufficiency_Syndrome.yaml.
    preceding = inline_references(text[:offset])
    if len(preceding) == 1:
        # Unambiguous however far back it sits -- no rival to confuse it with.
        # Note this deliberately outranks the sibling `reference:` below: prose
        # that names a paper is talking about that paper, and the enclosing
        # mapping's own reference is the weaker signal. Across the whole KB this
        # tier only ever produces NARRATED/UNDETERMINED outcomes, never a
        # contradiction, so the ordering is safe as well as principled.
        return preceding

    for node in reversed(ancestors):
        value = node.get("reference")
        if isinstance(value, str) and value.strip():
            return (value.strip(),)

    for node in reversed(ancestors):
        if isinstance(node.get("evidence"), list):
            refs = list(dict.fromkeys(_subtree_references(node["evidence"])))
            if refs:
                return tuple(refs)
    return ()


# --------------------------------------------------------------------------
# Adjudication
# --------------------------------------------------------------------------

# MEDLINE / fetcher scaffolding that surrounds an abstract but is not one. A
# record with *only* these carries no abstract, whatever its content_type says.
#
# Matched per blank-line-separated BLOCK rather than per line, because every one
# of these wraps: an affiliation list, a COI statement and the journal citation
# all run to several lines, and a per-line rule leaves the continuations behind.
# Those leftovers are what a naive word count mistakes for an abstract --
# PMID:39417910 and PMID:40696776 are both abstract-less case letters whose
# ethics/COI boilerplate alone runs past any plausible word floor.
_SCAFFOLD_BLOCK = (
    re.compile(r"^\s*\d+\.\s+\S.*\.\s*(?:19|20)\d\d"),  # 1. Acta Neurol Belg. 2025 Feb;
    re.compile(r"^(?:DOI|PMID|PMCID|PII|ISSN|ISBN)\s*:", re.IGNORECASE),
    re.compile(r"^Author information\s*:", re.IGNORECASE),
    re.compile(
        r"^(?:Comments?\s+(?:in|on)|Errat(?:um|a)\s+(?:in|for)|Update\s+(?:of|in)|"
        r"Republished\s+(?:in|from)|Expression\s+of\s+Concern|Retraction\s+(?:in|of)|"
        r"Conflict\s+of\s+interest|Declaration\s+of\s+(?:interest|competing)|"
        r"Competing\s+interests|Copyright|\u00a9|\(c\)\s*\d{4}|Publisher\s*:|"
        r"Funding\s*:|Acknowledg)",
        re.IGNORECASE,
    ),
    re.compile(r"^\*\*"),  # **Authors:** / **Journal:** header lines
    re.compile(r"^#"),  # markdown headings
    re.compile(r"^\[?(?:Article\s+in|Free\s+(?:PMC|full)\b)", re.IGNORECASE),
)

# A block that is just an author list: "Tang J(1), Stevens RA, Chan CC." Matched
# structurally rather than by name, so it works for any alphabet PubMed emits.
_AUTHOR_SEGMENT = re.compile(
    r"^[A-Z][\w'\-\u00c0-\u024f]*(?:\s+[A-Z]?[\w'\-\u00c0-\u024f]*)*"
    r"\s+[A-Z][A-Za-z]{0,3}(?:\(\d+\))*$"
)

# Below this many words of residual prose, treat the record as carrying no
# abstract. Well above the empty case (0 words after block stripping) and well
# below a genuine short abstract; the shortest real abstract measured in this
# cache sits at 80 words.
ABSTRACT_WORD_FLOOR = 40


def _looks_like_author_block(block: str) -> bool:
    segments = [seg.strip().rstrip(".") for seg in block.replace("\n", " ").split(",")]
    segments = [seg for seg in segments if seg]
    if len(segments) < 2:
        return False
    matched = sum(1 for seg in segments if _AUTHOR_SEGMENT.match(seg))
    return matched >= max(2, int(0.6 * len(segments)))


def _normalize_words(text: str) -> str:
    return " ".join(re.sub(r"\W+", " ", text.lower()).split())


def abstract_prose(body: str, title: str = "") -> str:
    """The abstract-ish prose in a cached body, with MEDLINE scaffolding removed.

    PubMed emits a citation stub -- journal line, title, authors, affiliations,
    DOI/PMID footer, COI statement -- for records that never had an abstract,
    and the fetcher types those ``abstract_only`` exactly like a record that has
    one. So ``content_type`` cannot answer "is there an abstract here"; what is
    left after removing the scaffolding can.
    """
    title_norm = _normalize_words(title)
    kept: list[str] = []
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block:
            continue
        first = block.split("\n", 1)[0].strip()
        if any(rx.search(first) for rx in _SCAFFOLD_BLOCK):
            continue
        block_norm = _normalize_words(block)
        if title_norm and block_norm and block_norm in title_norm:
            continue
        if _looks_like_author_block(block):
            continue
        kept.append(" ".join(block.split()))
    return " ".join(kept)


_TITLE_RE = re.compile(r"^title:\s*(.*)$", re.MULTILINE)


class Adjudicator:
    """Answers claim/cache questions, memoized over the reference cache."""

    def __init__(self, index: CachedReferenceIndex) -> None:
        self.index = index
        self._prose: dict[str, str | None] = {}

    def prose_words(self, reference_id: str) -> int | None:
        """Word count of abstract prose in the cached record, or ``None``."""
        if reference_id not in self._prose:
            self._prose[reference_id] = self._read_prose(reference_id)
        prose = self._prose[reference_id]
        return None if prose is None else len(prose.split())

    def _read_prose(self, reference_id: str) -> str | None:
        path = self.index.resolve_cache_path(reference_id)
        if path is None:
            return None
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:  # pragma: no cover - unreadable cache file
            return None
        if "## Content" not in text:
            return ""
        match = _TITLE_RE.search(text)
        title = match.group(1).strip().strip("\"'") if match else ""
        return abstract_prose(self.index.extract_body(text), title)

    def adjudicate(self, claim: Claim) -> Finding:
        if is_narration(claim.text):
            return Finding(
                claim,
                Verdict.NARRATED,
                "sentence reports a source-defect claim rather than asserting "
                "one (a correction note, or an account of an earlier revision); "
                "not adjudicated",
                claim.references[0] if claim.references else None,
            )
        if not claim.references:
            return Finding(
                claim,
                Verdict.UNDETERMINED,
                "no reference could be resolved for this claim; check it by hand",
            )
        if claim.kind is ClaimKind.DEFECTIVE_TEXT:
            return Finding(
                claim,
                Verdict.UNDETERMINED,
                "a truncation/garbling claim has no exact mechanical test; "
                "confirm it against the whole cache file, not an excerpt of it",
                claim.references[0],
            )
        if claim.kind is ClaimKind.NO_ABSTRACT:
            return self._adjudicate_no_abstract(claim)
        return self._adjudicate_negative_existence(claim)

    def _adjudicate_no_abstract(self, claim: Claim) -> Finding:
        # Short-circuits on the first candidate that settles the question, in
        # both directions: any reference lacking an abstract CONFIRMS the claim,
        # and any that cannot be checked offline makes it UNDETERMINED.
        # CONTRADICTED is reached only by falling out of the loop, i.e. once
        # every candidate has been shown to carry an abstract.
        checked: list[tuple[str, int]] = []
        for reference_id in claim.references:
            content_type = self.index.content_type(reference_id)
            if content_type == "unavailable":
                return Finding(
                    claim,
                    Verdict.CONFIRMED,
                    f"cache for {reference_id} is content_type: unavailable",
                    reference_id,
                )
            # A trial-registry or database summary is not an abstract, so it can
            # neither have nor lack one. PIK3CA_Mutant_Breast_Cancer.yaml's claim
            # is about an unresolvable "NEJM reference" while the sibling
            # `reference:` is a ClinicalTrials.gov record typed `summary`.
            if content_type in {"structured_record", "url", "local_file", "summary"}:
                return Finding(
                    claim,
                    Verdict.UNDETERMINED,
                    f"{reference_id} is a {content_type} cache, which has no "
                    "abstract to have or lack",
                    reference_id,
                )
            words = self.prose_words(reference_id)
            if words is None:
                return Finding(
                    claim,
                    Verdict.UNDETERMINED,
                    f"{reference_id} is not cached locally, so the claim cannot "
                    "be checked offline",
                    reference_id,
                )
            if words < ABSTRACT_WORD_FLOOR:
                return Finding(
                    claim,
                    Verdict.CONFIRMED,
                    f"cached {reference_id} carries {words} word(s) of prose "
                    "beyond the citation stub -- no abstract, as claimed",
                    reference_id,
                )
            checked.append((reference_id, words))
        reference_id, words = checked[0]
        return Finding(
            claim,
            Verdict.CONTRADICTED,
            f"cached {reference_id} DOES carry an abstract ({words} words of "
            "prose). If this was read through a fixed-width or truncated view "
            "during curation, re-read the whole file: a claim that a source is "
            "defective is a claim about a file, not about the excerpt you saw.",
            reference_id,
        )

    def _adjudicate_negative_existence(self, claim: Claim) -> Finding:
        target = searchable_object(claim.obj or "")
        if target is None:
            return Finding(
                claim,
                Verdict.UNDETERMINED,
                f"object {claim.obj!r} is not specific enough to search for "
                "unambiguously; check it by hand",
                claim.references[0],
            )
        for reference_id in claim.references:
            content = self.index.normalized_content(reference_id)
            if content is None:
                continue
            needle = self.index.normalize(target)
            if needle and f" {needle} " in f" {content} ":
                return Finding(
                    claim,
                    Verdict.CONTRADICTED,
                    f"cached {reference_id} DOES contain {target!r}; the claim "
                    "is used to justify omitting or downgrading evidence, so a "
                    "false one suppresses real curation",
                    reference_id,
                )
        if all(
            self.index.normalized_content(reference_id) is None
            for reference_id in claim.references
        ):
            return Finding(
                claim,
                Verdict.UNDETERMINED,
                f"none of {', '.join(claim.references)} is cached locally",
                claim.references[0],
            )
        return Finding(
            claim,
            Verdict.CONFIRMED,
            f"{target!r} does not appear in the cached text, as claimed",
            claim.references[0],
        )


def searchable_object(phrase: str) -> str | None:
    """The one token worth searching for in *phrase*, or ``None`` if too vague.

    Deliberately conservative. "does not mention nystagmus" reduces to
    ``nystagmus`` and is decidable; "does not specify the mouse allele" is a
    claim about *which* allele, and searching ``mouse`` or ``allele`` would
    contradict a true claim, so it stays UNDETERMINED.
    """
    quoted = re.search(r"[\"'“‘]([^\"'”’]{2,60})[\"'”’]", phrase)
    if quoted:
        return quoted.group(1).strip()

    # A restrictive qualifier makes the claim about a *particular* instance --
    # "does not report the immunohistochemistry **that motivates it**" is not
    # contradicted by the word "immunohistochemistry" appearing somewhere. Bail
    # out rather than truncating to the head noun, which is how the first run
    # over kb/ contradicted a true claim in Bone_Giant_Cell_Tumor.yaml.
    if re.search(
        r"\b(?:that|which|who|whose|where|when|used|shown|reported|described|"
        r"underlying|behind|motivat\w*|support\w*|driv\w*|propos\w*)\b",
        phrase,
        re.IGNORECASE,
    ):
        return None

    # Stop at the first clause boundary: "mention nystagmus in the proband" is
    # about nystagmus, and trailing qualifiers only add unsearchable words.
    head = re.split(
        r"\b(?:in|for|among|within|across|at|on|from|as|and|or|but|"
        r"beyond|outside|rather)\b",
        phrase,
        maxsplit=1,
    )[0]
    tokens = [tok for tok in re.findall(r"[\w\-]+", head) if tok]
    content = [
        tok
        for tok in tokens
        if tok.lower() not in _STOPWORDS and not tok.isdigit() and len(tok) > 2
    ]
    if len(content) != 1:
        # Zero content words means the object was all determiners and generic
        # nouns; more than one means a phrase whose meaning is not the presence
        # of any single word.
        return None
    token = content[0]
    if _SPECIFIC_TOKEN.match(token) or len(token) >= 6:
        return token
    return None


# --------------------------------------------------------------------------
# Scanning
# --------------------------------------------------------------------------


def iter_claims(path: str, data) -> list[Claim]:
    """Every source-defect claim in one loaded YAML document."""
    claims: list[Claim] = []

    def walk(node, location: str, ancestors: list[dict]) -> None:
        if isinstance(node, dict):
            ancestors = ancestors + [node]
            for key, value in node.items():
                child = f"{location}.{key}" if location else str(key)
                if key in PROSE_FIELDS and isinstance(value, str):
                    for kind, sentence, obj, offset in find_claims_in_text(value):
                        claims.append(
                            Claim(
                                path=path,
                                location=child,
                                kind=kind,
                                text=sentence,
                                references=resolve_references(value, offset, ancestors),
                                obj=obj,
                            )
                        )
                walk(value, child, ancestors)
        elif isinstance(node, list):
            for index, value in enumerate(node):
                walk(value, f"{location}[{index}]", ancestors)

    walk(data, "", [])
    return claims


def scan(paths) -> list[Claim]:
    claims: list[Claim] = []
    for path in paths:
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            # Deliberately broad, and deliberately non-fatal: gating on
            # malformed YAML is `validate-all`'s job, and one bad file must not
            # cost the other 200-odd findings in a report-only sweep. Warning to
            # stderr keeps the file visible as unchecked rather than invisible.
            print(
                f"warning: skipping unparseable {path}: {exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        if not isinstance(data, dict):
            continue
        rel = (
            path.relative_to(ROOT).as_posix()
            if path.is_absolute() and str(path).startswith(str(ROOT))
            else path.as_posix()
        )
        claims.extend(iter_claims(rel, data))
    return claims


def default_paths() -> list[Path]:
    return sorted(SCAN_DIR.rglob("*.yaml"))


class UsageError(Exception):
    """A path argument that cannot be scanned, as opposed to a finding."""


def expand_paths(paths) -> list[Path]:
    """Resolve CLI path arguments to YAML files, refusing what cannot be scanned.

    A directory expands to the YAML files under it. The `*files` recipe
    signature invites `just check-source-defect-claims kb/disorders`, and
    without this that argument reached :func:`scan`, raised
    ``IsADirectoryError`` into its deliberately broad except, and printed one
    stderr warning followed by ``0 found ... OK`` with exit 0 -- a clean-looking
    pass over a path nothing had read. That is the exact shape of quiet failure
    this tool exists to argue against, so it must not be one of its own.

    A missing path is a usage error, not a finding: report-only means the
    *verdicts* never fail the build, not that a mistyped argument should look
    like a clean run.
    """
    resolved: list[Path] = []
    for path in paths:
        if path.is_dir():
            resolved.extend(sorted(path.rglob("*.yaml")))
        elif path.exists():
            resolved.append(path)
        else:
            raise UsageError(f"no such file or directory: {path}")
    return resolved


def adjudicate_all(claims, cache_dir: Path | None = None) -> list[Finding]:
    if cache_dir is None:
        cache_dir = load_cache_dir(DEFAULT_CONFIG)
    # No skip_prefixes: a DOI-cited claim is still checkable against the cached
    # body, and skipping it here would replicate the #7514 blind spot one layer
    # up. Bracket patterns are irrelevant -- nothing here is a quoted snippet.
    index = CachedReferenceIndex(cache_dir, (), ())
    adjudicator = Adjudicator(index)
    return [adjudicator.adjudicate(claim) for claim in claims]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "files", nargs="*", type=Path, help="YAML files to scan (default: all of kb/)"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--all", action="store_true", help="print every claim with its verdict"
    )
    group.add_argument("--count", action="store_true", help="print summary counts only")
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help="reference cache directory (default: the validator config's)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "exit 1 on CONTRADICTED verdicts. Off by default and not wired into "
            "`just qc` or CI: this is a reporting gate (#9226)."
        ),
    )
    args = parser.parse_args(argv)

    try:
        paths = expand_paths(args.files) if args.files else default_paths()
    except UsageError as exc:
        parser.error(str(exc))
    claims = scan(paths)
    findings = adjudicate_all(claims, cache_dir=args.cache_dir)

    by_verdict = Counter(finding.verdict for finding in findings)
    by_kind = Counter((finding.claim.kind, finding.verdict) for finding in findings)
    contradicted = [f for f in findings if f.verdict is Verdict.CONTRADICTED]
    undetermined = [f for f in findings if f.verdict is Verdict.UNDETERMINED]

    if args.count:
        print(f"claims found: {len(findings)}")
        for verdict in Verdict:
            print(f"  {verdict.value:<13} {by_verdict.get(verdict, 0)}")
        print("\nby claim class:")
        for kind in ClaimKind:
            row = " ".join(
                f"{verdict.value}={by_kind.get((kind, verdict), 0)}"
                for verdict in Verdict
            )
            print(f"  {kind.value:<19} {row}")
        return 0

    if args.all:
        for finding in findings:
            print(finding.format())
            print()

    if contradicted:
        print(
            "Prose claims about a cited source that the cache CONTRADICTS "
            f"({len(contradicted)}):\n"
        )
        for finding in contradicted:
            print(finding.format())
            print()
    if undetermined and not args.all:
        print(
            f"{len(undetermined)} claim(s) could not be adjudicated mechanically "
            "(run with --all to list them)."
        )
    print(
        f"Source-defect claims: {len(findings)} found, "
        f"{by_verdict.get(Verdict.CONFIRMED, 0)} confirmed by the cache, "
        f"{len(contradicted)} contradicted, {len(undetermined)} undetermined."
    )
    if not contradicted:
        print(
            "OK: no prose claim about a cited source is contradicted by the "
            "cached reference."
        )
    if args.strict and contradicted:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
