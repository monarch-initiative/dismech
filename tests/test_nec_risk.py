"""Tests for the shared NEC-risk classifier (``src/dismech/nec_risk.py``).

Named Entity Confusion is the deep-research failure mode tracked in issue
#3889. ``scripts/nec_risk_audit.py`` already pins the corpus-level audit over
``kb/disorders``; this suite pins the *reusable* per-name classifier that the
MONDO priority dashboard applies to uncurated candidates, where the warning is
actionable before a DR report is ever requested.

Cases mirror the real documented NEC incidents in #3889:
  * numbered series  — the SCAR20-for-Lichtenstein-Knorr expansion;
  * eponym collision — the Temtamy surname shared by two distinct disorders;
  * synonym aliasing — a synonym pointing at a different eponymous entity;
  * acronym ambiguity — ``MWS`` (Marden-Walker / Mowat-Wilson / Muckle-Wells).
"""

from __future__ import annotations

from dismech.nec_risk import (
    RISK_CLASSES,
    build_eponym_owners,
    classify_terms,
    colliding_eponyms,
    eponyms_in,
    series_hits,
)


def _classes(flags) -> list[str]:
    return [flag.risk_class for flag in flags]


def _detail(flags, risk_class: str) -> tuple[str, ...]:
    for flag in flags:
        if flag.risk_class == risk_class:
            return flag.detail
    raise AssertionError(f"{risk_class} not flagged in {_classes(flags)}")


def test_series_hits_catches_both_type_numbers_and_series_acronyms():
    assert series_hits("spinocerebellar ataxia, autosomal recessive 20") == set()
    assert "SCAR20" in series_hits("SCAR20 ataxia")
    assert "type 2" in series_hits("mucopolysaccharidosis type 2")


def test_classify_flags_a_numbered_series_label():
    flags = classify_terms("Charcot-Marie-Tooth disease type 2A")
    assert "NUMBERED_SERIES" in _classes(flags)
    assert _detail(flags, "NUMBERED_SERIES") == ("type 2A",)


def test_classify_flags_a_series_acronym_hiding_in_a_synonym():
    flags = classify_terms("Lichtenstein-Knorr syndrome", ["SCAR20"])
    assert "NUMBERED_SERIES" in _classes(flags)
    assert _detail(flags, "NUMBERED_SERIES") == ("SCAR20",)


def test_eponym_collision_requires_a_corpus_and_names_the_shared_surname():
    corpus = build_eponym_owners(
        [
            ("MONDO:0018150", "Walker-Warburg syndrome"),
            ("MONDO:0008708", "Marden-Walker syndrome"),
            ("MONDO:0018997", "Noonan syndrome"),
        ]
    )
    shared = colliding_eponyms(corpus)
    assert shared == {"Walker"}

    flagged = classify_terms("Walker-Warburg syndrome", shared_eponyms=shared)
    assert _detail(flagged, "EPONYM_COLLISION") == ("Walker",)

    unflagged = classify_terms("Noonan syndrome", shared_eponyms=shared)
    assert "EPONYM_COLLISION" not in _classes(unflagged)


def test_one_entity_repeating_its_own_surname_is_not_a_collision():
    owners = build_eponym_owners(
        [
            ("MONDO:0018150", "Walker-Warburg syndrome"),
            ("MONDO:0018150", "Walker-Warburg disease"),
        ]
    )
    assert colliding_eponyms(owners) == set()


def test_a_surname_not_adjacent_to_a_head_noun_is_a_known_blind_spot():
    """Pins a real limitation rather than an aspiration.

    The single-surname pattern only fires when the capitalized token sits
    directly before a disease head-noun, so "Temtamy preaxial brachydactyly
    syndrome" — one half of the documented #3889 eponymic collision — is *not*
    detected here. Widening the pattern would swamp the detector with
    false positives; ``src/dismech/preflight_dr.py``'s per-report gene check
    remains the backstop for cases this misses.
    """
    owners = build_eponym_owners(
        [
            ("MONDO:0009033", "Temtamy syndrome"),
            ("MONDO:0012963", "Temtamy preaxial brachydactyly syndrome"),
        ]
    )
    assert colliding_eponyms(owners) == set()


def test_classify_flags_a_synonym_carrying_a_different_eponym():
    flags = classify_terms(
        "spinocerebellar ataxia, autosomal recessive 19",
        ["Lichtenstein-Knorr syndrome"],
    )
    assert set(_detail(flags, "SYNONYM_ALIASING")) == {"Lichtenstein", "Knorr"}


def test_a_synonym_sharing_the_label_eponym_is_not_aliasing():
    flags = classify_terms(
        "Mowat-Wilson syndrome",
        ["Mowat-Wilson disease"],
    )
    assert "SYNONYM_ALIASING" not in _classes(flags)


def test_classify_flags_short_all_caps_synonyms():
    flags = classify_terms("Mowat-Wilson syndrome", ["MWS"])
    assert _detail(flags, "ACRONYM_AMBIGUITY") == ("MWS",)


def test_long_lowercase_synonyms_are_not_acronyms():
    flags = classify_terms("Marfan syndrome", ["marfan syndrome type 1"])
    assert "ACRONYM_AMBIGUITY" not in _classes(flags)


def test_a_plain_label_carries_no_risk_flags():
    assert classify_terms("asthma", ["bronchial asthma"]) == []


def test_flags_are_returned_in_declared_risk_class_order():
    flags = classify_terms(
        "Temtamy syndrome type 2",
        ["TS2", "Lichtenstein-Knorr syndrome"],
        shared_eponyms={"Temtamy"},
    )
    order = [RISK_CLASSES.index(cls) for cls in _classes(flags)]
    assert order == sorted(order)
    assert set(_classes(flags)) == set(RISK_CLASSES)


def test_non_string_and_blank_synonyms_are_ignored():
    flags = classify_terms("asthma", ["", None, 7])  # type: ignore[list-item]
    assert flags == []


def test_eponyms_in_suppresses_common_descriptors():
    assert eponyms_in("Progressive Muscular Dystrophy") == set()
    assert "Loeys" in eponyms_in("Loeys-Dietz syndrome")
