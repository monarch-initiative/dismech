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

plus the sibling-disease qualifier veto from :mod:`discover_datasets`
(*hereditary* vs *acquired* angioedema).
"""

from __future__ import annotations

import re
import sys
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
    return phrases, cores


def compile_phrases(phrases: list[str]) -> list[tuple[str, re.Pattern]]:
    """Hyphen-aware boundaries, so Pick disease cannot match Niemann-Pick disease."""
    return [
        (p, re.compile(rf"(?<![\w-]){re.escape(p)}(?![\w-])", re.IGNORECASE))
        for p in phrases
    ]


def match_title(title: str, patterns, cores) -> tuple[str, str]:
    """Return (matched_phrase, conflict_reason).

    ``matched_phrase`` is "" when the title does not name the disease.
    ``conflict_reason`` is non-empty when the title applies a competing
    qualifier to the disease's core term, i.e. it is about a sibling disease.
    """
    low = title.lower()
    matched = next((p for p, rx in patterns if rx.search(low)), "")
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
