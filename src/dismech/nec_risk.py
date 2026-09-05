"""Structural Named Entity Confusion (NEC) risk patterns.

Named Entity Confusion is the deep-research failure mode tracked in issue
#3889: a DR tool resolves a queried disease name to a *different* disease
entity and returns a coherent-but-wrong report. Snippet-in-abstract checks,
PMID existence checks and term validation cannot catch it, because a
wrong-entity report validates cleanly against its own (real) wrong-disease
sources.

Two complementary tools sit on top of this module:

* ``scripts/nec_risk_audit.py`` flags the risk *classes* across the curated
  ``kb/disorders`` corpus (acceptance-criterion item 3 of #3889);
* ``src/dismech/priority_dashboard.py`` annotates the *uncurated* MONDO
  candidates a curator is about to pick up, which is the point at which the
  warning is actionable — before a DR report is ever requested.

``src/dismech/preflight_dr.py`` is the per-report backstop: it checks an
individual report's gene identity against MONDO. This module is deliberately
*upstream* of that and makes a weaker claim — it flags a name-shaped risk, not
an observed confusion.

The four risk classes are the ones named in #3889:

``NUMBERED_SERIES``
    Numbered / lettered series whose numbering has drifted historically
    (SCAR1-SCAR20, CMT types, "type II"). The SCAR20-for-Lichtenstein-Knorr
    case.
``EPONYM_COLLISION``
    A surname shared by more than one disease entity. The Temtamy case.
``SYNONYM_ALIASING``
    A synonym carrying a *different* eponym from the primary name — the
    historical-synonym-maps-elsewhere risk.
``ACRONYM_AMBIGUITY``
    A short all-caps synonym that is easy to expand to the wrong entity
    (``MWS`` = Marden-Walker / Mowat-Wilson / Muckle-Wells).
"""

from __future__ import annotations

import re
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field

__all__ = [
    "ACRONYM_RE",
    "NON_EPONYM_WORDS",
    "RISK_CLASSES",
    "SERIES_PREFIXES",
    "SERIES_RE",
    "TYPE_RE",
    "NecRiskFlag",
    "acronym_synonyms",
    "build_eponym_owners",
    "classify_terms",
    "colliding_eponyms",
    "eponyms_in",
    "series_hits",
]

RISK_CLASSES = (
    "NUMBERED_SERIES",
    "EPONYM_COLLISION",
    "SYNONYM_ALIASING",
    "ACRONYM_AMBIGUITY",
)

# Words that are Capitalized in a disease name but should NOT trigger an eponym
# flag. Most are common nouns/descriptors, but a few (``Charcot``, ``Hodgkin``,
# ``Parkinson``) are *genuine* eponyms deliberately suppressed because they recur
# as plain descriptors across many entries (e.g. "Parkinson" in 20+ files) and
# would otherwise swamp the collision detector with false positives. Trade-off:
# a real collision involving one of these surnames will be missed; the per-report
# preflight gene check (#3889) remains the backstop for those.
NON_EPONYM_WORDS = {
    "Syndrome", "Disease", "Disorder", "Deficiency", "Dysplasia", "Dystrophy",
    "Dysostosis", "Dyschondrosteosis", "Anemia", "Carcinoma", "Sarcoma",
    "Lymphoma", "Leukemia", "Tumor", "Cancer", "Type", "Familial", "Congenital",
    "Hereditary", "Autosomal", "Recessive", "Dominant", "Acute", "Chronic",
    "Juvenile", "Infantile", "Neonatal", "Adult", "Primary", "Secondary",
    "Idiopathic", "Multiple", "Mixed", "Complex", "Combined", "Generalized",
    "Focal", "Systemic", "Progressive", "Spinocerebellar", "Cerebellar",
    "Muscular", "Skeletal", "Spondylo", "Mucinous", "Cystadenoma", "Ataxia",
    "Charcot", "Hypohidrotic", "Ectodermal", "Mediterranean", "Pancreatic",
    "Frontonasal", "Spastic", "Paraplegia", "Encephalopathy", "Retinopathy",
    "Nephropathy", "Neuropathy", "Myopathy", "Anaplastic", "Papillary",
    "Medullary", "Hodgkin", "Non", "Related", "Associated", "Due", "And",
    "Of", "The", "With", "X", "XY", "XX",
    # Anatomical / descriptive common nouns that precede a disease head-noun
    # but are not surnames (high-frequency false positives).
    "Anomalies", "Artery", "Cell", "Chemotherapy", "Induced", "Kidney",
    "Storage", "Small", "Negative", "Positive", "Onset", "Macular", "Nail",
    "Hair", "Sinus", "Fusion", "Dystonia", "Parkinsonism", "Parkinson",
    "Responsive", "Dopa", "Immunodeficiency", "Neurodevelopmental", "Renal",
    "Spondyloepimetaphyseal", "Thanatophoric", "Tall", "Spasticity", "Gait",
    "Centromeric", "Facial", "Instability", "Body", "Inclusion", "Bone",
    "Dementia", "Frontotemporal", "Motor", "Sensory", "Axonal", "Corpus",
    "Callosum", "Peripheral", "Eye", "Island", "Islands", "Band", "Partial",
    "Lichenoid", "Pityriasis", "Neuronal", "Ceroid", "Lipofuscinosis",
    "Sialic", "Acid", "Free", "Hepatic", "Fibrinogen", "Glycogen", "Sick",
    "Silent", "Clear", "Sickle", "Coronary", "Multicentric", "Acquired",
    "North", "Carolina", "Hypotrichosis", "Woolly", "Skin", "Fragility",
    "Tooth", "Stature", "Disability", "Intellectual", "Vomiting", "Nausea",
    "Diarrhea", "Toxin", "Drug", "Pulmonary", "Arterial", "Hypertension",
    "Breast", "Triple", "Lung", "Demyelinating", "Leukodystrophy", "Early",
    "Undetermined", "Epileptic", "Myoclonus", "Spinal", "Anterior",
}

# Series-acronym prefixes whose numbering is known to have drifted upstream
# (the strongest NEC trigger -- SCAR20 was a wrong expansion of Lichtenstein-Knorr).
SERIES_PREFIXES = (
    "SCAR", "SCA", "SPG", "CMT", "CMTX", "MEN", "EDS", "OI", "CDG", "NCL",
    "BBS", "MPS", "DYX", "HSAN", "PCH", "COXPD", "MTDPS", "EIEE", "DEE",
    "CDA", "GLUT", "MODY",
)

# Cap at XV — disease series rarely exceed type 15. ``XI{0,3}`` covers XI/XII/XIII
# (the original ``XI{0,2}`` silently missed XIII); XIV/XV are spelled out explicitly.
ROMAN = r"(?:I{1,3}V?|IV|VI{0,3}|IX|XI{0,3}|XIV|XV|X)"
TYPE_RE = re.compile(rf"\btype[\s-]+([0-9]+[A-Za-z]?|{ROMAN})\b", re.IGNORECASE)
SERIES_RE = re.compile(r"\b(" + "|".join(SERIES_PREFIXES) + r")[\s-]?([0-9]+[A-Za-z]?)\b")
ACRONYM_RE = re.compile(r"^[A-Z][A-Z0-9]{1,5}$")


@dataclass(frozen=True)
class NecRiskFlag:
    """One structural NEC-risk finding for one disease name.

    ``detail`` holds the specific tokens that triggered the flag (the series
    hits, the shared surname, the aliasing eponyms, the ambiguous acronyms) so
    a curator can see *why* the name was flagged rather than only *that* it was.
    """

    risk_class: str
    detail: tuple[str, ...] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, object]:
        return {"risk_class": self.risk_class, "detail": list(self.detail)}


def eponyms_in(text: str) -> set[str]:
    """Return surname-like eponym tokens found in a disease name."""
    found = set()
    # Hyphenated capitalized pairs: Leri-Weill, Bassen-Kornzweig, Loeys-Dietz.
    for m in re.finditer(r"\b([A-Z][a-z]{2,})-([A-Z][a-z]{2,})\b", text):
        for tok in m.groups():
            if tok not in NON_EPONYM_WORDS:
                found.add(tok)
    # Single Capitalized surname directly before a disease head-noun.
    for m in re.finditer(
        r"\b([A-Z][a-z]{3,})\s+(?:syndrome|disease|dysplasia|dystrophy|"
        r"dysostosis|anomaly|sign|sarcoma|ataxia)\b",
        text,
        re.IGNORECASE,
    ):
        tok = m.group(1)
        if tok[0].isupper() and tok not in NON_EPONYM_WORDS:
            found.add(tok)
    return found


def series_hits(text: str) -> set[str]:
    """Return numbered/lettered series tokens found in a disease name."""
    hits: set[str] = set()
    for m in TYPE_RE.finditer(text):
        hits.add("type " + m.group(1))
    for m in SERIES_RE.finditer(text):
        hits.add(m.group(1) + m.group(2))
    return hits


def acronym_synonyms(synonyms: Iterable[str]) -> list[str]:
    """Return the short all-caps synonyms that are easy to mis-expand."""
    return [s for s in synonyms if isinstance(s, str) and ACRONYM_RE.match(s)]


def build_eponym_owners(named_entities: Iterable[tuple[str, str]]) -> dict[str, set[str]]:
    """Map each eponym to the distinct entity ids whose names carry it.

    ``named_entities`` yields ``(entity_id, name)`` pairs. An entity may appear
    more than once (label plus synonyms, say); the mapping is by *distinct id*,
    so a surname repeated across one entity's own aliases is not a collision.
    """
    owners: dict[str, set[str]] = defaultdict(set)
    for entity_id, name in named_entities:
        if not name:
            continue
        for eponym in eponyms_in(name):
            owners[eponym].add(entity_id)
    return dict(owners)


def colliding_eponyms(owners: dict[str, set[str]]) -> set[str]:
    """Return the eponyms shared by more than one distinct entity."""
    return {eponym for eponym, ids in owners.items() if len(ids) > 1}


def classify_terms(
    label: str,
    synonyms: Iterable[str] = (),
    *,
    shared_eponyms: Iterable[str] = (),
) -> list[NecRiskFlag]:
    """Classify one disease name into structural NEC-risk classes.

    ``shared_eponyms`` is the set of surnames known to be shared across more
    than one entity in whatever corpus the caller cares about (see
    :func:`build_eponym_owners` / :func:`colliding_eponyms`). Collision is a
    property of a *corpus*, not of a single name, so it cannot be derived here.

    Flags are returned in :data:`RISK_CLASSES` order.
    """
    synonyms = [s for s in synonyms if isinstance(s, str) and s.strip()]
    shared = set(shared_eponyms)
    flags: list[NecRiskFlag] = []

    hits = series_hits(" ".join([label, *synonyms]))
    if hits:
        flags.append(NecRiskFlag("NUMBERED_SERIES", tuple(sorted(hits))))

    label_eponyms = eponyms_in(label)
    collisions = sorted(label_eponyms & shared)
    if collisions:
        flags.append(NecRiskFlag("EPONYM_COLLISION", tuple(collisions)))

    alias_eponyms: set[str] = set()
    for synonym in synonyms:
        alias_eponyms |= eponyms_in(synonym)
    aliasing = sorted(alias_eponyms - label_eponyms)
    if aliasing:
        flags.append(NecRiskFlag("SYNONYM_ALIASING", tuple(aliasing)))

    acronyms = acronym_synonyms(synonyms)
    if acronyms:
        flags.append(NecRiskFlag("ACRONYM_AMBIGUITY", tuple(acronyms)))

    return flags
