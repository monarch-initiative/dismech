"""The rule deciding whether a term label restates its card title (#8402)."""

import pytest

from dismech.term_labels import comparison_key, label_restates_title


@pytest.mark.parametrize(
    ("title", "label"),
    [
        # Identical but for case.
        ("Spastic tetraplegia", "Spastic tetraplegia"),
        ("Typical Absence Seizures", "Typical absence seizure"),
        # The title is the label plus a qualifier -- the reported cases.
        ("Severe global developmental delay", "Global developmental delay"),
        ("Infantile seizures", "Seizure"),
        ("Adult ataxia", "Ataxia"),
        # Differing only in punctuation, hyphenation, or spacing.
        ("Pierre Robin sequence", "Pierre-Robin sequence"),
        ("EMG Chronic Denervation Signs", "EMG: chronic denervation signs"),
        ("Ventricular pre-excitation", "Ventricular preexcitation"),
        ("Abnormal Hair Shaft Morphology", "Abnormal hairshaft morphology"),
        (
            "Attention-Deficit/Hyperactivity Disorder",
            "Attention deficit hyperactivity disorder",
        ),
        ("Transient ST-segment elevation", "ST segment elevation"),
        ("GM2 Ganglioside Accumulation", "GM2-ganglioside accumulation"),
    ],
)
def test_title_already_says_it(title: str, label: str) -> None:
    assert label_restates_title(title, label)


@pytest.mark.parametrize(
    ("title", "label"),
    [
        # Unrelated.
        ("Congenital microcephaly", "Primary microcephaly"),
        ("Juvenile absence seizures", "Generalized non-motor (absence) seizure"),
        # The reverse containment: the label is the more specific of the two,
        # so it is exactly the half worth printing.
        ("Anemia", "Anemia, hemolytic"),
        ("Developmental delay", "Global developmental delay"),
        ("Molar Tooth Sign", "Molar tooth sign on MRI"),
    ],
)
def test_label_adds_something(title: str, label: str) -> None:
    assert not label_restates_title(title, label)


@pytest.mark.parametrize(
    ("title", "label"),
    [
        ("Some finding", None),
        ("Some finding", ""),
        ("Some finding", "   "),
        # Punctuation-only labels reduce to an empty key, which must not count
        # as "contained in everything".
        ("Some finding", "---"),
        (None, "Seizure"),
        ("", "Seizure"),
    ],
)
def test_empty_sides_never_suppress(title: str | None, label: str | None) -> None:
    assert not label_restates_title(title, label)


def test_word_boundaries_are_not_respected() -> None:
    """A documented imprecision, pinned so it is a choice and not a surprise.

    Dropping separators is what lets "Ventricular preexcitation" match
    "Ventricular pre-excitation", and the same move lets a label match across
    a word boundary. Across ``kb/disorders/`` this fires exactly once, on a
    pair that does mean the same thing.
    """
    assert label_restates_title("Keloid scarring", "Keloids")


def test_comparison_key_keeps_non_ascii_alphanumerics() -> None:
    """``str.isalnum`` is Unicode-aware, so Greek in a label is not punctuation."""
    assert (
        comparison_key("Elevated beta-2 microglobulin") == "elevatedbeta2microglobulin"
    )
    assert comparison_key("β-oxidation defect") == "βoxidationdefect"
