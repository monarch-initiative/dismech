"""Deciding whether a bound term's label needs printing beside a card title.

A card title is curator free text; the term bound to it carries its own
ontology label. Most of the time they say the same thing, and printing both
gives the reader a heading like "Severe global developmental delay Global
developmental delay" (issue #8402).

:func:`label_restates_title` answers the only question a template needs to
ask: does the title already say what the label says? It compares on letters
and digits alone, so the pairs that differ only in casing, hyphenation,
punctuation, or spacing -- "Pierre Robin sequence" against "Pierre-Robin
sequence", "Abnormal Hair Shaft Morphology" against "Abnormal hairshaft
morphology" -- are recognised as the restatements they are.

The test is deliberately *one-directional*. A label contained in the title
adds nothing and is dropped; a label the title is contained in ("Anemia"
bound to "Anemia, hemolytic") is more specific than the title and must
survive, because there the label is the half carrying the information.

Comparing on letters and digits alone also drops word boundaries, so a
label can match across one in the title -- "Keloids" is found inside
"Keloid scarring". Across `kb/disorders/` that fires exactly once, on a
pair that does mean the same thing, and the CURIE chip and its tooltip
name the term whichever way the test lands. A boundary-aware rule would
buy that back at the cost of the ~540 plurals and the ~29 hyphenation
variants this handles, which is a bad trade.
"""

from __future__ import annotations


def comparison_key(value: str | None) -> str:
    """Reduce a label or title to the characters worth comparing.

    Case-folded, with every non-alphanumeric character dropped.
    ``str.isalnum`` is Unicode-aware, so Greek letters and accented
    characters in ontology labels survive rather than being stripped as
    punctuation.
    """
    return "".join(char for char in str(value or "").casefold() if char.isalnum())


def label_restates_title(title: str | None, label: str | None) -> bool:
    """Return True when *title* already says what *label* says.

    False when either side is empty, so a card with no title or no bound
    label never suppresses anything by accident.
    """
    label_key = comparison_key(label)
    if not label_key:
        return False
    title_key = comparison_key(title)
    if not title_key:
        return False
    return label_key in title_key
