"""Tests for the prose-claim gate and the snippet-boundary check (dismech#9226).

The gate's whole risk is over-firing. Claims that a cited source is defective
are usually TRUE and load-bearing -- they justify downgrading evidence, or
explain why a snippet legitimately looks broken -- so a check that flagged them
would push curators to delete accurate provenance to get a build green. Most of
what is pinned here is therefore the *negative* half: the specific sentences in
kb/ that must keep passing.
"""

from pathlib import Path

import pytest

from dismech.reference_snippet_audit import (
    CachedReferenceIndex,
    SnippetPair,
    audit_files,
    boundary_defect,
)
from scripts.check_source_defect_claims import (
    ClaimKind,
    Verdict,
    abstract_prose,
    adjudicate_all,
    antecedent_reference,
    find_claims_in_text,
    inline_references,
    is_narration,
    iter_claims,
    resolve_references,
    scan,
    searchable_object,
)

ROOT = Path(__file__).resolve().parents[1]


# --------------------------------------------------------------------------
# Claim detection: what must NOT be read as a claim about a cached file
# --------------------------------------------------------------------------


def _kinds(text):
    return {kind for kind, _, _, _ in find_claims_in_text(text)}


@pytest.mark.parametrize(
    "text",
    [
        # The dominant sense of "truncate" in a disease-mechanism KB is a
        # truncated protein. A bare `truncat` trigger matches ~1,600 lines in
        # kb/, essentially all of them correct genetics prose.
        "Biallelic truncating variants in the gene abolish the protein.",
        "A homozygous truncating mutation produces a truncated polypeptide.",
        "C-terminal truncation removes the catalytic domain.",
        # "cut-off" is a diagnostic threshold here, not a damaged quote.
        "Establishes a glycosylated ferritin cut-off of 16% for AOSD diagnosis.",
        "A 7 pg/mL cut-off gave 100% specificity in the cohort.",
    ],
)
def test_genetics_and_threshold_prose_is_not_a_source_defect_claim(text):
    assert ClaimKind.DEFECTIVE_TEXT not in _kinds(text)


@pytest.mark.parametrize(
    "text",
    [
        # "abstract" as an ADJECTIVE: a claim about what the text says, not
        # about whether an abstract exists.
        "No abstract sentence states the complication directly, hence PARTIAL.",
        "No abstract-level source with a citable numeric interval was available.",
        # Set-level claims: nothing in the reference set says X. True even when
        # every record in that set has an abstract.
        (
            "No cached abstract in this curation pass gives a proportion for "
            "pulmonary embolism specifically."
        ),
        (
            "Historically this differential carried no evidence item because no "
            "abstract in the reference set made the comparison directly."
        ),
        (
            "The report flags its own threshold table as unverified and no cached "
            "abstract supplies a quotable interval."
        ),
    ],
)
def test_content_claims_are_not_read_as_missing_abstract_claims(text):
    assert ClaimKind.NO_ABSTRACT not in _kinds(text)


@pytest.mark.parametrize(
    "text",
    [
        "That reference is indexed in PubMed without an abstract.",
        "The cached PubMed record carries no abstract body.",
        "That record contains only bibliographic metadata with no abstract.",
        "That report is indexed as a Letter with no abstract.",
    ],
)
def test_record_anchored_missing_abstract_claims_are_detected(text):
    assert ClaimKind.NO_ABSTRACT in _kinds(text)


def test_defect_word_needs_cache_context():
    """A defect word only counts when it is about *our stored text*."""
    assert ClaimKind.DEFECTIVE_TEXT in _kinds(
        "The quote starts mid-word because the cached PDF extraction breaks it."
    )
    assert ClaimKind.DEFECTIVE_TEXT not in _kinds(
        "The gene product is truncated at residue 210."
    )


def test_negative_existence_claim_is_detected_with_its_object():
    claims = find_claims_in_text(
        "The cached abstract does not mention nystagmus, so this phenotype "
        "carries no evidence item."
    )
    kinds = {kind for kind, _, _, _ in claims}
    assert ClaimKind.NEGATIVE_EXISTENCE in kinds
    obj = next(
        obj for kind, _, obj, _ in claims if kind is ClaimKind.NEGATIVE_EXISTENCE
    )
    assert searchable_object(obj) == "nystagmus"


# --------------------------------------------------------------------------
# Object extraction: only adjudicate what a grep can actually decide
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "phrase",
    [
        # A restrictive qualifier makes the claim about a PARTICULAR instance;
        # the head noun appearing somewhere in the abstract does not refute it.
        "the immunohistochemistry that motivates it",
        "the mouse allele",
        "the exact dose used",
        "which variant was tested",
        "any of these",
    ],
)
def test_vague_objects_are_not_adjudicated(phrase):
    assert searchable_object(phrase) is None


@pytest.mark.parametrize(
    ("phrase", "expected"),
    [
        ("nystagmus", "nystagmus"),
        ("polyglucosan at all", "polyglucosan"),
        ("EIF4A2", "EIF4A2"),
        ('"exon skipping"', "exon skipping"),
        ("nystagmus in the proband", "nystagmus"),
    ],
)
def test_specific_objects_are_adjudicated(phrase, expected):
    assert searchable_object(phrase) == expected


# --------------------------------------------------------------------------
# Reference resolution
# --------------------------------------------------------------------------


def test_inline_reference_extraction():
    assert inline_references("That record has no abstract in PubMed.") == ()
    assert inline_references(
        "The same applies to PMID:34318586, which also has no abstract."
    ) == ("PMID:34318586",)


def test_anaphoric_subject_reaches_back_across_a_sentence():
    """ "That reference ... has no abstract" refers to the id named before it.

    Scoping resolution to the claim sentence lost the antecedent and blamed the
    evidence item's own reference instead, contradicting a true statement in
    ADPRS-Related_Stress-Induced_Neurodegeneration.yaml.
    """
    text = (
        "A separate off-label report proposed doxycycline in a CONDSIAS patient "
        "(PMID:39417910, Acta Neurol Belg 2025). That reference was fetched and "
        "cached but its record contains only bibliographic metadata with no abstract."
    )
    offset = text.index("no abstract")
    assert antecedent_reference(text, offset) == "PMID:39417910"


def test_a_citation_after_the_claim_is_a_contrast_not_the_subject():
    """ "...which rests on PMID:X" names the paper the claim defers TO."""
    text = (
        "PARTIAL and deliberately scoped: this abstract does not name SETD5, so "
        "it supports the modality but not the SETD5-specific claim, which rests "
        "on PMID:41957673."
    )
    offset = text.index("does not name")
    assert antecedent_reference(text, offset) is None


def test_reference_resolves_through_an_enclosing_evidence_block():
    """A pathophysiology `description:` has no sibling `reference:`.

    Its references live in a child `evidence:` list -- one of #9207's three
    sites -- so a same-mapping definition of "adjacent" would drop it.
    """
    node = {
        "name": "Some node",
        "description": "The cached abstract is truncated here.",
        "evidence": [{"reference": "PMID:1", "snippet": "x"}],
    }
    assert resolve_references("no inline id here", 0, [node]) == ("PMID:1",)


def test_sibling_reference_wins_over_the_enclosing_block():
    outer = {"evidence": [{"reference": "PMID:outer"}]}
    inner = {"reference": "PMID:inner", "explanation": "..."}
    assert resolve_references("no inline id", 0, [outer, inner]) == ("PMID:inner",)


# --------------------------------------------------------------------------
# Abstract-presence detection
# --------------------------------------------------------------------------


def test_medline_citation_stub_carries_no_abstract():
    """The case a `content_type`-only test gets backwards.

    PubMed emits this stub for a record that never had an abstract, and the
    fetcher types it `abstract_only` exactly like a record that has one -- so
    `content_type` cannot answer the question. PMID:18195232 is the live
    example: three evidence items in Acute_Annular_Outer_Retinopathy.yaml are
    downgraded to PARTIAL on the strength of it.
    """
    body = """1. Arch Ophthalmol. 2008 Jan;126(1):130-2. doi: 10.1001/archophthalmol.2007.5.

Association of antiretinal antibodies in acute annular outer retinopathy.

Tang J(1), Stevens RA, Okada AA, Chin M, Nussenblatt RB, Chan CC.

Author information:
(1)Retina Specialists of Boston/Harvard Medical School, Cambridge, MA 02140,
USA. bostonretina@aol.com

DOI: 10.1001/archophthalmol.2007.5
PMID: 18195232 [Indexed for MEDLINE]"""
    prose = abstract_prose(
        body,
        "Association of antiretinal antibodies in acute annular outer retinopathy.",
    )
    assert prose.split() == []


def test_conflict_of_interest_block_is_not_an_abstract():
    """Blocks wrap, so a per-line rule leaves the continuations behind.

    An ethics/COI statement alone runs past any plausible word floor, which is
    how PMID:39417910 and PMID:40696776 -- both genuinely abstract-less case
    letters -- were first contradicted.
    """
    body = """1. Acta Neurol Belg. 2025 Feb;125(1):241-242. doi: 10.1007/s13760-024-02664-0.
Epub  2024 Oct 17.

Repurposing doxycycline for a case of CONDSIAS Syndrome.

Eslamiyeh H(1), Vahidi Mehrjardi MY(2).

DOI: 10.1007/s13760-024-02664-0
PMID: 39417910

Conflict of interest statement: Declarations. Ethics approval and consent to
participate: The proband's parent provided written and consent agreement, and
the study was approved by the ethics committee of the University in Yazd, Iran.
The study adhered to the principles of the Helsinki Declaration of 1975.
Consent for publication: The written consent for publication was obtained."""
    prose = abstract_prose(
        body, "Repurposing doxycycline for a case of CONDSIAS Syndrome."
    )
    assert len(prose.split()) < 40


def test_real_abstract_is_detected_as_prose():
    body = """1. J Exp Med. 2012 Mar 12;209(3):463-70. doi: 10.1084/jem.20112533.

Agammaglobulinemia and absent B lineage cells in a patient lacking p85 alpha.

Conley ME(1), Dobbs AK, Quintana AM.

Whole exome sequencing was used to determine the causative gene in patients
with B cell defects of unknown etiology. A homozygous premature stop codon in
exon 6 of PIK3R1 was identified in a young woman with colitis and absent B
cells. The mutation results in the absence of p85 alpha but normal expression
of the p50 alpha and p55 alpha regulatory subunits of PI3K. Bone marrow
aspirates from the patient showed fewer than 0.1 percent CD19 positive B cells
with normal percentages of B cell precursors. The number and function of the
patient's T cells were normal.

DOI: 10.1084/jem.20112533
PMID: 22351933 [Indexed for MEDLINE]"""
    assert len(abstract_prose(body).split()) > 40


# --------------------------------------------------------------------------
# Narration must never be contradicted
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text",
    [
        # The Tetralogy_of_Fallot.yaml correction paragraph exists *because*
        # four such claims there were false, and has to restate them to say so.
        (
            "An earlier revision of this entry asserted in three places that "
            "cached abstracts were truncated, and in one place that "
            "PMID:30582441 had no abstract body. All four claims were false."
        ),
        (
            "The earlier note recorded that no cached abstract stated the "
            "practice in quotable form; PMID:21045974 does."
        ),
        "A previous version wrongly claimed the record has no abstract.",
    ],
)
def test_correction_narration_is_recognised(text):
    assert is_narration(text)


def test_ordinary_claims_are_not_mistaken_for_narration():
    assert not is_narration("That record has no abstract, so nothing is quotable.")


# --------------------------------------------------------------------------
# End-to-end over the live KB: the four sites #9226 says must stay clean
# --------------------------------------------------------------------------

LEGITIMATE_SITES = [
    # Real #8048 PDF hyphenation, explained in prose.
    "kb/disorders/Cri-du-Chat_Syndrome.yaml",
    "kb/disorders/DTYMK-Related_Neurodegeneration.yaml",
    # Three evidence items downgraded because the record really has no abstract.
    "kb/disorders/Acute_Annular_Outer_Retinopathy.yaml",
    # The correction paragraph that necessarily restates four false claims.
    "kb/disorders/Tetralogy_of_Fallot.yaml",
]


@pytest.mark.parametrize("relpath", LEGITIMATE_SITES)
def test_legitimate_narration_is_never_contradicted(relpath):
    path = ROOT / relpath
    if not path.exists():  # pragma: no cover - entry renamed or retired
        pytest.skip(f"{relpath} no longer present")
    findings = adjudicate_all(scan([path]))
    contradicted = [f for f in findings if f.verdict is Verdict.CONTRADICTED]
    assert not contradicted, "\n".join(f.format() for f in contradicted)


def test_gate_is_report_only():
    """Exit 0 even with findings; --strict is for direct CLI use only."""
    from scripts.check_source_defect_claims import main

    assert main([str(ROOT / "kb" / "disorders" / "Tetralogy_of_Fallot.yaml")]) == 0


def test_scan_walks_prose_fields_only():
    data = {
        "name": "Example",
        "notes": "The cached record has no abstract.",
        "snippet": "The cached record has no abstract.",
    }
    claims = iter_claims("x.yaml", data)
    assert [claim.location for claim in claims] == ["notes"]


# --------------------------------------------------------------------------
# Snippet-boundary check
# --------------------------------------------------------------------------


class _FakeIndex(CachedReferenceIndex):
    def __init__(self, content):
        super().__init__(Path("references_cache"), (), ())
        self._content = content

    def normalized_content(self, reference_id):
        return self.normalize(self._content)


def _pair(snippet):
    return SnippetPair(
        path=Path("x.yaml"), location="s", reference_id="PMID:1", snippet=snippet
    )


def test_mid_word_fragment_is_reported():
    """The #9207 shape: four snippets stopping at 'movement d'."""
    index = _FakeIndex("impaired vigilance and movement disorders were seen")
    assert boundary_defect(index, _pair("vigilance and movement d")) is not None


def test_whole_word_quote_is_not_reported():
    index = _FakeIndex("impaired vigilance and movement disorders were seen")
    assert boundary_defect(index, _pair("vigilance and movement disorders")) is None


def test_digit_flank_is_a_cache_defect_not_a_truncation():
    """A fused superscript citation marker is not a cut word.

    PMID:40760247 caches as '...hearing loss and microcephaly20-26', so a
    faithful quote ending at 'microcephaly' is flanked by a digit. The curator
    cannot fix that by re-quoting -- it is the #8048 family, not #9207.
    """
    index = _FakeIndex("hearing loss and microcephaly20 26. Here we identify")
    assert boundary_defect(index, _pair("hearing loss and microcephaly")) is None


def test_a_clean_occurrence_anywhere_clears_the_quote():
    """A fragment that also appears inside a longer word is still a real quote."""
    index = _FakeIndex("the cardiac phenotype. cardiac was assessed")
    assert boundary_defect(index, _pair("cardiac")) is None


def test_boundary_check_is_off_by_default():
    path = ROOT / "kb" / "disorders" / "GNPTG-Mucolipidosis.yaml"
    if not path.exists():  # pragma: no cover - entry renamed or retired
        pytest.skip("GNPTG-Mucolipidosis.yaml no longer present")
    assert audit_files([path]).boundary_suspect == []
    assert audit_files([path], check_boundaries=True).boundary_suspect
