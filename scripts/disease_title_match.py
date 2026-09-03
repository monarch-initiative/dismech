#!/usr/bin/env python3
"""Shared, deliberately narrow disease-to-title matching for dataset discovery.

Extracted so EGA, ArrayExpress and OmicsDI discovery apply *identical* rules
rather than three drifting copies. The rules were arrived at empirically while
mining GEO and EGA; each exists because of a specific wrong-disease match.

The contract: a dataset is about a disease only if the disease is named in the
dataset's **own title**. Description- and abstract-level mentions are rejected,
because that is where sibling diseases, model systems and "we also profiled X"
studies get in. Causal genes are never searched -- in GEO that produced
Alzheimer and medulloblastoma data for neuroferritinopathy.

Four guards, each traceable to a real failure:

``GENERIC_PHRASES``
    ``Dorsalgia`` is bound to ``MONDO:0000001``, labelled simply "disease",
    which would match a large share of any archive.
``GENERIC_HEAD_NOUNS``
    A single-word core term like "Sclerosis", stripped from "Systemic
    Sclerosis", matched Multiple Sclerosis.
``label_is_broader``
    ``BRCA_Mutant_Prostate_Cancer`` is bound to "prostate cancer", so searching
    the bare label retrieved generic prostate cancer.
word-boundary matching
    "H Syndrome" matched "Denys-Drash Syndrome" and "MRKH syndrome".
CamelCase compound boundary
    dbGaP names a trial network "AsthmaNet", so a strict trailing boundary
    scored an asthma trial as though asthma were absent from the title. Only
    an *uppercase* next character relaxes the boundary, which is why this does
    not also let "Lymphoma" match "Lymphomatoid papulosis" -- a different
    disease. Inflected lowercase forms ("Asthmatic Patients") are deliberately
    still misses here; they are recovered from the study's data dictionary
    instead, which states the affection status outright rather than guessing at
    morphology.
diacritic folding
    dbGaP titles spell it "Sjögren's Syndrome" while the KB entry is
    ``Sjogrens_Syndrome``, so two on-target studies were scored as though the
    disease were absent from the title. Medical eponyms carry diacritics often
    enough (Sjögren, Behçet, Ménière, Guillain-Barré, Creutzfeldt-Jakob) that
    this had to be fixed in the matcher rather than per caller.

plus the sibling-disease qualifier veto from :mod:`discover_datasets`
(*hereditary* vs *acquired* angioedema).
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discover_datasets import STOPWORDS, core_term, has_qualifier_conflict

# A title match on a very short phrase is noise, not evidence.
MIN_PHRASE_LEN = 6

# Too generic to be evidence of anything, even at full length.
GENERIC_PHRASES = {
    "disease", "diseases", "syndrome", "syndromes", "disorder", "disorders",
    "deficiency", "cancer", "carcinoma", "tumor", "tumour", "infection",
    "inflammation", "neoplasm", "abnormality", "malformation", "failure",
}

# Head-nouns naming a *class* of disease. Safe inside a multi-word phrase
# ("AL Amyloidosis"), unsafe alone. Only applied to a derived core term, never
# to an entry's own name.
GENERIC_HEAD_NOUNS = {
    "sclerosis", "fibrosis", "anemia", "anaemia", "dystrophy", "atrophy",
    "ataxia", "neuropathy", "myopathy", "dysplasia", "palsy", "leukemia",
    "leukaemia", "lymphoma", "sarcoma", "hepatitis", "nephritis", "arthritis",
    "dermatitis", "colitis", "encephalopathy", "encephalitis", "myelitis",
    "retinopathy", "cardiomyopathy", "thalassemia", "porphyria", "amyloidosis",
    "hypertension", "hypotension", "diabetes", "epilepsy", "psoriasis",
    "vasculitis", "thrombocytopenia", "neutropenia", "immunodeficiency",
}


def significant_words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 2 and w not in STOPWORDS}


def label_is_broader(name: str, label: str) -> bool:
    """True when the entry's name carries significant words its MONDO label lacks."""
    return bool(significant_words(name) - significant_words(label))


def entry_phrases(entry: dict, slug: str) -> tuple[list[str], list[tuple[str, str]]]:
    """Return (phrases to match in a title, (core, stripped-qualifier) pairs)."""
    names: list[str] = []
    name = (entry.get("name") or slug).replace("_", " ").strip()
    if name:
        names.append(name)

    label = (((entry.get("disease_term") or {}).get("term") or {}).get("label") or "").strip()
    if label and label.lower() != name.lower() and not label_is_broader(name, label):
        names.append(label)

    cores: list[tuple[str, str]] = []
    for n in list(names):
        short, stripped = core_term(n)
        if not short or short.lower() in {x.lower() for x in names}:
            continue
        if " " not in short.strip() and short.strip().lower() in GENERIC_HEAD_NOUNS:
            continue
        names.append(short)
        cores.append((short, stripped))

    phrases = [
        n for n in names
        if len(n) >= MIN_PHRASE_LEN and n.strip().lower() not in GENERIC_PHRASES
    ]
    # "Sputum RNA-Seq from Asthmatic Patients" is an asthma study; the strict
    # word boundary cannot see that on its own.
    seen = {p.lower() for p in phrases}
    for phrase in list(phrases):
        for variant in inflected_variants(phrase):
            if variant.lower() not in seen:
                phrases.append(variant)
                seen.add(variant.lower())
    return phrases, cores


# Adjectival and inflected forms of disease head nouns, as a hand-verified
# table rather than a productive rule. Medical derivations are irregular
# (asthma -> asthmatic, psoriasis -> psoriatic), so any suffix rule general
# enough to catch them also produces wrong ones: "lymphoma" would reach
# "lymphomatoid papulosis" and "adenoma" would reach "adenomatous polyposis",
# both distinct diseases. Every pair here has been checked to denote the same
# disease as its key. Extend it by hand when a real miss shows up; do not
# generate it.
ADJECTIVAL_FORMS = {
    "asthma": ["asthmatic", "asthmatics"],
    "diabetes": ["diabetic", "diabetics"],
    "arthritis": ["arthritic"],
    "psoriasis": ["psoriatic"],
    "cirrhosis": ["cirrhotic"],
    "fibrosis": ["fibrotic"],
    "thrombosis": ["thrombotic"],
    "stenosis": ["stenotic"],
    "epilepsy": ["epileptic", "epileptics"],
    "anemia": ["anemic"],
    "ischemia": ["ischemic"],
    "leukemia": ["leukemic"],
    "atopy": ["atopic"],
    "allergy": ["allergic"],
}


def inflected_variants(phrase: str) -> list[str]:
    """Variants of ``phrase`` whose final word has a known adjectival form.

    The table is stored lowercase; the variant takes the capitalisation of the
    word it replaces, so "Severe Asthma" yields "Severe Asthmatic" rather than
    "Severe asthmatic". Matching is case-insensitive either way -- this is for
    what a curator reads in the proposal and the provenance note.
    """
    words = phrase.split()
    if not words:
        return []
    head = words[-1]
    forms = ADJECTIVAL_FORMS.get(head.lower().strip("\u0027s"), [])
    cased = str.capitalize if head[:1].isupper() else str.lower
    return [" ".join(words[:-1] + [cased(form)]) for form in forms]


def fold_diacritics(text: str) -> str:
    """Strip combining marks so "Sjögren" and "Sjogren" compare equal.

    Applied to both sides of every comparison. It only ever *adds* matches that
    a diacritic previously blocked -- treating "o" and "ö" as the same letter in
    a disease name is the intended reading, not a loosening of the rules.
    """
    return "".join(
        ch for ch in unicodedata.normalize("NFKD", text) if not unicodedata.combining(ch)
    )


def compile_phrases(phrases: list[str]) -> list[tuple[str, re.Pattern]]:
    """Hyphen-aware boundaries, so Pick disease cannot match Niemann-Pick disease.

    The returned phrase is the original (it is shown to curators and recorded in
    provenance notes); only the pattern is diacritic-folded.

    The *leading* boundary stays strict -- that is the guard keeping "Pick
    disease" out of "Niemann-Pick disease". The *trailing* boundary also admits
    a following uppercase letter, so a CamelCase compound ("AsthmaNet") counts
    as naming the disease. The phrase is matched case-insensitively via an
    inline ``(?i:...)`` group rather than a whole-pattern flag, so the
    uppercase lookahead keeps its meaning.
    """
    return [
        (
            p,
            re.compile(
                rf"(?<![\w-])(?i:{re.escape(fold_diacritics(p))})"
                rf"(?:(?![\w-])|(?=[A-Z]))"
            ),
        )
        for p in phrases
    ]


def match_title(title: str, patterns, cores) -> tuple[str, str]:
    """Return (matched_phrase, conflict_reason).

    ``matched_phrase`` is "" when the title does not name the disease.
    ``conflict_reason`` is non-empty when the title applies a competing
    qualifier to the disease's core term, i.e. it is about a sibling disease.
    """
    # Patterns are searched against the case-preserving folded title so the
    # CamelCase boundary above can see an uppercase letter; `low` is retained
    # for the qualifier-conflict checks, which are case-insensitive substring
    # tests.
    folded = fold_diacritics(title)
    low = folded.lower()
    matched = next((p for p, rx in patterns if rx.search(folded)), "")
    if not matched:
        return "", ""

    for core, stripped in cores:
        if not stripped:
            continue
        if f"{stripped} {core}".lower() in low:
            continue  # the entry's own qualified form is present: not a conflict
        competing = has_qualifier_conflict(low, stripped, core)
        if competing:
            return matched, (
                f"title says '{competing} {core.lower()}', entry is '{stripped} {core.lower()}'"
            )
    return matched, ""
