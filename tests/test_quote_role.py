"""The `quote_role` slot and its background-citation worklist (issue #10262).

`reference` records provenance of the *sentence*; `quote_role` records
provenance of the *finding*. Those are different objects, and the model
represented them identically until this slot existed -- so a chick-embryo
study's introduction, quoted for the human clinical picture it restates, was
indistinguishable from that study's own measurements.

The tests below cover three things: the enum is shaped as designed and mapped
out to CiTO, the page shows the value as provenance rather than as a grade, and
the detector's deterministic tier classifies a snippet by the section it sits
in -- including the full-text case where it must decline to classify rather
than guess.
"""

from pathlib import Path

import pytest
import yaml

from dismech.render import quote_role_tooltip, render_disorder
from scripts.check_background_citations import (
    SECTION_ZONES,
    Coverage,
    ReferenceFacts,
    classify,
    is_animal_descriptor,
    iter_evidence,
    kb_section,
    split_sections,
    zone_of,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"


@pytest.fixture(scope="module")
def schema() -> dict:
    return yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------
# Schema
# --------------------------------------------------------------------------


def test_quote_role_is_an_optional_slot_on_evidence_item(schema: dict) -> None:
    slot = schema["slots"]["quote_role"]
    assert slot["range"] == "QuoteRoleEnum"
    # Absent must stay legal: every evidence item predating the slot is
    # unassessed, and an unassessed judgement is the honest record.
    assert not slot.get("required")
    assert "quote_role" in schema["classes"]["EvidenceItem"]["slots"]


def test_quote_role_carries_the_three_designed_values(schema: dict) -> None:
    values = schema["enums"]["QuoteRoleEnum"]["permissible_values"]
    assert set(values) == {"PRIMARY_RESULT", "BACKGROUND", "REVIEW_SYNTHESIS"}


def test_quote_role_has_no_unknown_value(schema: dict) -> None:
    """Absent already means "nobody has assessed this".

    `DirectnessEnum` carries both spellings and CLAUDE.md then has to tell
    curators not to use one of them. Not repeating that here.
    """
    assert "UNKNOWN" not in schema["enums"]["QuoteRoleEnum"]["permissible_values"]


def test_quote_role_values_map_out_to_cito(schema: dict) -> None:
    """Mapped out rather than modelled on, per the #510 static-enum ruling."""
    values = schema["enums"]["QuoteRoleEnum"]["permissible_values"]
    assert values["PRIMARY_RESULT"]["exact_mappings"] == ["cito:citesAsEvidence"]
    assert values["BACKGROUND"]["exact_mappings"] == ["cito:obtainsBackgroundFrom"]
    # REVIEW_SYNTHESIS has no exact CiTO counterpart, so it must not claim one.
    assert "exact_mappings" not in values["REVIEW_SYNTHESIS"]
    assert values["REVIEW_SYNTHESIS"]["close_mappings"] == ["cito:citesAsAuthority"]
    assert schema["prefixes"]["cito"] == "http://purl.org/spar/cito/"


def test_every_quote_role_value_is_described(schema: dict) -> None:
    values = schema["enums"]["QuoteRoleEnum"]["permissible_values"]
    for key, meta in values.items():
        assert meta.get("title"), key
        assert meta.get("description"), key


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

_BASE = {
    "reference": "PMID:1",
    "supports": "SUPPORT",
    "snippet": "a quoted sentence",
    "explanation": "why it bears on the claim",
}


def _render(tmp_path: Path, evidence: list[dict]) -> str:
    disorder = {
        "name": "Quote Role Test Disorder",
        "pathophysiology": [
            {
                "name": "A Mechanism",
                "description": "A node carrying the evidence under test.",
                "evidence": evidence,
            }
        ],
    }
    disorder_path = tmp_path / "Quote_Role_Test_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Quote_Role_Test_Disorder.html"
    disorder_path.write_text(yaml.safe_dump(disorder, sort_keys=False))
    render_disorder(disorder_path, output_path=output_path)
    return output_path.read_text()


def test_quote_role_renders_as_its_own_badge(tmp_path: Path) -> None:
    html = _render(tmp_path, [{**_BASE, "quote_role": "BACKGROUND"}])

    assert '<span class="evidence-quote-role"' in html
    assert ">BACKGROUND</span>" in html
    # Additive: the direction badge is untouched.
    assert 'class="evidence-support support-SUPPORT"' in html


def test_quote_role_is_absent_when_unassessed(tmp_path: Path) -> None:
    html = _render(tmp_path, [_BASE])

    assert '<span class="evidence-quote-role"' not in html


def test_quote_role_badge_is_not_styled_as_a_support_grade(tmp_path: Path) -> None:
    """A BACKGROUND badge must not read as weaker support.

    Where a quote sits in a paper's argument says nothing about which way it
    cuts, and colouring it like a downgraded SUPPORT would assert that it does.
    """
    html = _render(tmp_path, [{**_BASE, "quote_role": "BACKGROUND"}])

    assert 'class="evidence-support support-BACKGROUND"' not in html
    assert ".support-BACKGROUND" not in html


def test_quote_role_tooltip_comes_from_the_schema() -> None:
    """The prose lives in the enum, not in the template."""
    tooltip = quote_role_tooltip("REVIEW_SYNTHESIS")

    assert "review" in tooltip.lower()
    assert quote_role_tooltip(None) == ""
    # An unrecognised value degrades to the bare string rather than crashing or
    # inventing a description for it.
    assert quote_role_tooltip("NOT_A_VALUE") == "NOT_A_VALUE"


# --------------------------------------------------------------------------
# Detector: deterministic tier
# --------------------------------------------------------------------------

STRUCTURED_ABSTRACT = """BACKGROUND: Cerebro-costo-mandibular syndrome causes high perinatal mortality.

METHODS: Beads were implanted into chick somites.

RESULTS: Wnt inhibition produced rib gaps in the treated embryos.
"""


def test_sections_are_split_and_zoned() -> None:
    sections = split_sections(STRUCTURED_ABSTRACT)

    assert [label for label, _ in sections] == ["BACKGROUND", "METHODS", "RESULTS"]
    assert zone_of("BACKGROUND") == "BACKGROUND"
    assert zone_of("RESULTS") == "FINDING"
    assert zone_of("OBJECTIVE") == "AIM"
    # An unrecognised label still ends the previous section, and is classified
    # as nothing rather than folded into whichever zone precedes it.
    assert zone_of("SOME NOVEL PUBLISHER LABEL") == "OTHER"


def test_an_unlabelled_body_is_not_eligible_for_the_deterministic_tier() -> None:
    """No labels means no verdict, rather than a guess from the first paragraph."""
    assert split_sections("A perfectly ordinary unstructured abstract.") == []


def test_the_last_section_stops_at_the_abstract(tmp_path: Path) -> None:
    """A full text's own prose must not be swallowed by the final label.

    On a `content_type: full_text*` cache the structured abstract is followed by
    the whole article. Without the paragraph bound, a sentence quoted from the
    article's introduction would be reported as sitting in the abstract's
    conclusions -- confidently, deterministically, and wrongly.
    """
    body = (
        STRUCTURED_ABSTRACT
        + "\nIn the introduction we restate somebody else's prevalence figure.\n"
    )
    sections = split_sections(body)

    assert len(sections) == 3
    assert "prevalence figure" not in sections[-1][1]


def _write_cache(cache_dir: Path, pmid: str, body: str, keywords: list[str]) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    frontmatter = yaml.safe_dump(
        {
            "reference_id": f"PMID:{pmid}",
            "title": "A cached reference",
            "authors": ["Someone A"],
            "journal": "J Test",
            "keywords": keywords,
        },
        sort_keys=False,
    )
    (cache_dir / f"PMID_{pmid}.md").write_text(
        f"---\n{frontmatter}---\n\n## Content\n\n{body}\n", encoding="utf-8"
    )


def test_a_snippet_is_located_in_the_section_it_sits_in(tmp_path: Path) -> None:
    _write_cache(tmp_path, "1", STRUCTURED_ABSTRACT, ["Chick Embryo", "Animals"])
    refs = ReferenceFacts(tmp_path)

    assert refs.locate("PMID:1", "high perinatal mortality") == (
        "BACKGROUND",
        "BACKGROUND",
    )
    assert refs.locate("PMID:1", "produced rib gaps") == ("RESULTS", "FINDING")
    # Matching folds case and punctuation the way the reference validator does,
    # so a quote that verifies under `just validate-references` is located here.
    assert refs.locate("PMID:1", "High perinatal mortality!") is not None
    assert refs.locate("PMID:1", "a sentence that is not in the paper") is None


def test_an_uncached_reference_yields_no_facts(tmp_path: Path) -> None:
    assert ReferenceFacts(tmp_path).facts("PMID:999999999") is None


def test_animal_mesh_matches_inverted_narrower_forms() -> None:
    assert is_animal_descriptor("Mice")
    assert is_animal_descriptor("Mice, Knockout")
    assert is_animal_descriptor("Disease Models, Animal")
    assert not is_animal_descriptor("Humans")
    # A descriptor that merely starts with the same word is not an animal term.
    assert not is_animal_descriptor("Ratio, Odds")


def test_a_record_indexed_with_humans_is_not_animal_only(tmp_path: Path) -> None:
    """The MeSH tier's documented blind spot, pinned as a fact not a bug.

    Both mouse papers in the DFNA2A worked example carry `Humans` alongside
    `Mice`, so tier B is silent on exactly the two items #10262 predicted it
    would catch. That is why the deterministic tier exists.
    """
    _write_cache(
        tmp_path, "2", "An unstructured abstract.", ["Mice", "Animals", "Humans"]
    )
    facts = ReferenceFacts(tmp_path).facts("PMID:2")

    assert facts is not None
    assert facts["mesh_indexed"]
    assert not facts["animal_only"]


#: The two mouse-therapy papers the DFNA2A worked example quotes background from.
#: Named here rather than inlined so the pin below says which records it is about.
DFNA2A_BACKGROUND_SOURCES = ("PMID_42162447", "PMID_40898620")


@pytest.mark.parametrize("stem", DFNA2A_BACKGROUND_SOURCES)
def test_neither_tier_can_see_the_dfna2a_background_pair(stem: str) -> None:
    """The real records, not a fixture: both tiers are blind to this case.

    ``test_a_record_indexed_with_humans_is_not_animal_only`` pins the *behaviour*
    on a synthetic cache. This pins the *claim made about these two papers* in
    #10262 and in the PR that added this slot, so a future change to either tier
    (or a re-fetch that changes their MeSH) shows up as a failure here rather
    than as a quietly stale sentence in the docs.

    Tier B is silent because NLM indexed both with ``Humans`` alongside ``Mice``.
    Tier A is silent because both cached bodies are full text with no NLM
    structured-abstract labels. So the two items that motivated half the issue
    are found by neither, which is why the slot is curated and not derived.
    """
    cache_path = ROOT / "references_cache" / f"{stem}.md"
    if not cache_path.is_file():
        pytest.skip(f"{stem} is not in references_cache on this checkout")
    refs = ReferenceFacts(ROOT / "references_cache")
    facts = refs.facts(f"PMID:{stem.removeprefix('PMID_')}")

    assert facts is not None
    assert facts["mesh_indexed"], "expected MeSH indexing on this record"
    assert not facts["animal_only"], (
        "tier B is only silent on this record while NLM indexes it with Humans; "
        "if that changed, the claim in docs/ and in #10262 needs revisiting"
    )
    assert facts["sections"] == [], (
        "tier A is only silent on this record while its cached body carries no "
        "NLM structured-abstract labels"
    )


def test_evidence_items_are_found_by_shape_anywhere_in_a_document() -> None:
    """Reference + snippet, wherever they nest -- not an enumerated slot list."""
    data = {
        "pathophysiology": [
            {
                "name": "A node",
                "evidence": [{"reference": "PMID:1", "snippet": "quoted"}],
                "downstream": [
                    {
                        "target": "Another node",
                        "evidence": [{"reference": "PMID:2", "snippet": "also quoted"}],
                    }
                ],
            }
        ],
        "notes": "a mapping with neither field",
    }
    found = dict(iter_evidence(data))

    assert [item["reference"] for item in found.values()] == ["PMID:1", "PMID:2"]
    assert kb_section("pathophysiology[0].evidence[0]") == "pathophysiology"
    assert (
        kb_section("pathophysiology[0].downstream[0].evidence[0]") == "pathophysiology"
    )


def _classify(tmp_path: Path, item: dict) -> list:
    refs = ReferenceFacts(tmp_path)
    return classify(
        "kb/disorders/X.yaml", "pathophysiology[0].evidence[0]", item, refs, Coverage()
    )


def test_a_background_quote_is_reported_with_the_role_it_suggests(
    tmp_path: Path,
) -> None:
    _write_cache(tmp_path, "3", STRUCTURED_ABSTRACT, ["Chick Embryo", "Animals"])
    findings = _classify(
        tmp_path,
        {
            "reference": "PMID:3",
            "snippet": "high perinatal mortality",
            "evidence_source": "HUMAN_CLINICAL",
        },
    )
    tiers = {finding.tier: finding for finding in findings}

    assert tiers["A"].kind == "ABSTRACT_SECTION"
    assert tiers["A"].suggested == "BACKGROUND"
    # Same item, both tiers: the abstract says where the sentence sits and the
    # MeSH says the paper is chick-only. They are complementary, not exclusive.
    assert tiers["B"].kind == "MESH_HEURISTIC"


def test_the_papers_own_result_is_not_reported(tmp_path: Path) -> None:
    _write_cache(tmp_path, "4", STRUCTURED_ABSTRACT, ["Humans"])
    findings = _classify(
        tmp_path,
        {
            "reference": "PMID:4",
            "snippet": "produced rib gaps",
            "evidence_source": "HUMAN_CLINICAL",
        },
    )

    assert findings == []


def test_an_assessed_item_leaves_the_worklist(tmp_path: Path) -> None:
    """Deciding an item is what takes it off the list; nothing else does."""
    _write_cache(tmp_path, "9", STRUCTURED_ABSTRACT, ["Chick Embryo", "Animals"])
    item = {
        "reference": "PMID:9",
        "snippet": "high perinatal mortality",
        "quote_role": "BACKGROUND",
        "evidence_source": "HUMAN_CLINICAL",
    }
    refs = ReferenceFacts(tmp_path)
    coverage = Coverage()

    assert classify("kb/x.yaml", "loc", item, refs, coverage) == []
    assert coverage.already_assessed == 1
    # A census run puts it back, so the count is still reachable.
    census = classify("kb/x.yaml", "loc", item, refs, Coverage(), include_assessed=True)
    assert {finding.tier for finding in census} == {"A", "B"}


def test_a_recorded_quote_role_contradicting_the_section_is_reported(
    tmp_path: Path,
) -> None:
    """Tier C: the reason the deterministic tier is machinery, not a one-off scan."""
    _write_cache(tmp_path, "5", STRUCTURED_ABSTRACT, ["Humans"])
    findings = _classify(
        tmp_path,
        {
            "reference": "PMID:5",
            "snippet": "high perinatal mortality",
            "quote_role": "PRIMARY_RESULT",
            "evidence_source": "HUMAN_CLINICAL",
        },
    )
    conflicts = [finding for finding in findings if finding.tier == "C"]

    assert len(conflicts) == 1
    assert conflicts[0].kind == "QUOTE_ROLE_CONFLICT"
    assert conflicts[0].zone == "BACKGROUND"


def test_an_agreeing_quote_role_is_not_a_conflict(tmp_path: Path) -> None:
    """And, being assessed, it is off the worklist entirely."""
    _write_cache(tmp_path, "6", STRUCTURED_ABSTRACT, ["Humans"])
    findings = _classify(
        tmp_path,
        {
            "reference": "PMID:6",
            "snippet": "high perinatal mortality",
            "quote_role": "BACKGROUND",
            "evidence_source": "HUMAN_CLINICAL",
        },
    )

    assert findings == []


def test_review_synthesis_never_conflicts_with_a_section(tmp_path: Path) -> None:
    """A review's synthesis sentence can legitimately sit in any zone.

    So no section placement contradicts it, and reporting one would be a false
    finding on every review the KB cites.
    """
    _write_cache(tmp_path, "7", STRUCTURED_ABSTRACT, ["Humans"])
    for snippet in ("high perinatal mortality", "produced rib gaps"):
        findings = _classify(
            tmp_path,
            {
                "reference": "PMID:7",
                "snippet": snippet,
                "quote_role": "REVIEW_SYNTHESIS",
                "evidence_source": "HUMAN_CLINICAL",
            },
        )
        assert [finding.tier for finding in findings if finding.tier == "C"] == []


def test_an_absent_evidence_source_is_treated_as_the_documented_default(
    tmp_path: Path,
) -> None:
    """CLAUDE.md documents HUMAN_CLINICAL as the default, so tier B must see it."""
    _write_cache(
        tmp_path, "8", "An unstructured abstract about mice.", ["Mice", "Animals"]
    )
    findings = _classify(tmp_path, {"reference": "PMID:8", "snippet": "mice"})

    assert [finding.tier for finding in findings] == ["B"]
    assert findings[0].evidence_source == "HUMAN_CLINICAL"


def test_a_non_pmid_reference_is_out_of_scope(tmp_path: Path) -> None:
    """Only PMIDs carry NLM section labels and MeSH indexing."""
    assert _classify(tmp_path, {"reference": "ORPHA:558", "snippet": "anything"}) == []


def test_every_section_zone_is_one_of_the_three_kinds() -> None:
    assert set(SECTION_ZONES.values()) == {"BACKGROUND", "AIM", "FINDING"}


def test_coverage_starts_empty() -> None:
    coverage = Coverage()

    assert coverage.items == 0
    assert coverage.outside_sections == 0
