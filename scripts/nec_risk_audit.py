#!/usr/bin/env python3
"""NEC-risk disease-class audit for the dismech knowledge base.

Named Entity Confusion (NEC) is the deep-research failure mode tracked in
issue #3889: a DR tool resolves a queried disease name to a *different*
disease entity and produces a coherent-but-wrong report. Standard
hallucination checks (snippet-in-abstract, PMID existence, term validation)
cannot catch NEC because a wrong-entity report validates against its own
(real) wrong-disease sources.

This script implements acceptance-criterion item 3 of #3889 — *identify the
high-NEC-risk disease classes* — by scanning every current ``kb/disorders``
entry and flagging the four structural risk patterns named in the issue:

* ``NUMBERED_SERIES``  — numbered / lettered series where numbering has drifted
  historically (e.g. SCAR1-SCAR20, CMT types, "type II").
* ``EPONYM_COLLISION`` — an eponym (surname) shared by more than one dismech
  entry, the classic Temtamy / Lichtenstein-Knorr collision pattern.
* ``SYNONYM_ALIASING`` — an entry whose synonym list contains a *different*
  eponym from the primary name (the historical-synonym-maps-elsewhere risk).
* ``ACRONYM_AMBIGUITY``— a short all-caps acronym synonym that is easy to
  resolve to the wrong expansion.

The output is deliberately a *risk-class* flagger, not an assertion that any
specific confusion has occurred. It complements ``src/dismech/preflight_dr.py``
(#3902), which performs the per-report gene-identity cross-check.

Usage::

    uv run python scripts/nec_risk_audit.py            # summary table
    uv run python scripts/nec_risk_audit.py --markdown  # full markdown report
"""
from __future__ import annotations

import argparse
import glob
import os
import re
from collections import defaultdict

import yaml

DISORDERS_GLOB = "kb/disorders/*.yaml"

# Words that are Capitalized in a disease name but should NOT trigger an eponym
# flag. Most are common nouns/descriptors, but a few (``Charcot``, ``Hodgkin``,
# ``Parkinson``) are *genuine* eponyms deliberately suppressed because they recur
# as plain descriptors across many entries (e.g. "Parkinson" in 20+ files) and
# would otherwise swamp the collision detector with false positives. Trade-off:
# a real collision involving one of these surnames will be missed; the per-report
# preflight gene check (#3902) remains the backstop for those.
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


def load_entries():
    rows = []
    for path in sorted(glob.glob(DISORDERS_GLOB)):
        if path.endswith(".history.yaml"):
            continue
        try:
            with open(path) as fh:
                data = yaml.safe_load(fh)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        term = (data.get("disease_term") or {}).get("term") or {}
        rows.append(
            {
                "file": os.path.basename(path),
                "name": data.get("name") or "",
                "mondo": term.get("id"),
                "label": term.get("label") or "",
                "synonyms": [s for s in (data.get("synonyms") or []) if isinstance(s, str)],
            }
        )
    return rows


def eponyms_in(text: str):
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


def audit(rows):
    findings = defaultdict(list)  # category -> list of dict
    eponym_to_files = defaultdict(set)

    for r in rows:
        haystack = " ".join([r["name"], r["label"]] + r["synonyms"])

        # 1. Numbered / lettered series.
        series_hits = set()
        for m in TYPE_RE.finditer(haystack):
            series_hits.add("type " + m.group(1))
        for m in SERIES_RE.finditer(haystack):
            series_hits.add(m.group(1) + m.group(2))
        if series_hits:
            findings["NUMBERED_SERIES"].append({**r, "hits": sorted(series_hits)})

        # 2. Eponyms (for collision grouping).
        eps = eponyms_in(r["name"]) | eponyms_in(r["label"])
        for ep in eps:
            eponym_to_files[ep].add(r["file"])

        # 3. Synonym aliasing: a synonym carries a *different* eponym than name.
        name_eps = eponyms_in(r["name"]) | eponyms_in(r["label"])
        alias_eps = set()
        for syn in r["synonyms"]:
            alias_eps |= eponyms_in(syn)
        extra = alias_eps - name_eps
        if extra:
            findings["SYNONYM_ALIASING"].append({**r, "alias_eponyms": sorted(extra)})

        # 4. Acronym ambiguity: short all-caps synonym.
        acr = [s for s in r["synonyms"] if ACRONYM_RE.match(s)]
        if acr:
            findings["ACRONYM_AMBIGUITY"].append({**r, "acronyms": acr})

    # Eponym collisions = surname shared by >1 distinct entry.
    for ep, files in sorted(eponym_to_files.items()):
        if len(files) > 1:
            findings["EPONYM_COLLISION"].append({"eponym": ep, "files": sorted(files)})

    return findings


def print_summary(rows, findings):
    print(f"Scanned {len(rows)} current disorder entries.\n")
    print(f"{'Risk class':<20}{'entries flagged':>16}")
    print("-" * 36)
    for cat in ("NUMBERED_SERIES", "EPONYM_COLLISION", "SYNONYM_ALIASING", "ACRONYM_AMBIGUITY"):
        n = len(findings.get(cat, []))
        print(f"{cat:<20}{n:>16}")


def print_markdown(rows, findings):
    print(f"_Auto-generated by `scripts/nec_risk_audit.py` over {len(rows)} current "
          f"non-history `kb/disorders/*.yaml` entries (excludes `*.history.yaml`)._\n")
    print("| Risk class | Entries flagged |")
    print("|---|---|")
    for cat in ("NUMBERED_SERIES", "EPONYM_COLLISION", "SYNONYM_ALIASING", "ACRONYM_AMBIGUITY"):
        print(f"| {cat} | {len(findings.get(cat, []))} |")
    print()

    print("### Eponymic collisions (surname shared by >1 entry)\n")
    print("These are the highest-risk class: a DR tool can silently resolve the "
          "eponym to the wrong member.\n")
    for f in findings.get("EPONYM_COLLISION", []):
        print(f"- **{f['eponym']}** — {', '.join(f['files'])}")
    print()

    print("### Synonym aliasing (synonym carries a different eponym than the primary name)\n")
    for f in findings.get("SYNONYM_ALIASING", []):
        print(f"- `{f['file']}` ({f['name']}, {f['mondo']}) — alias eponym(s): "
              f"{', '.join(f['alias_eponyms'])}")
    print()

    print("### Acronym-ambiguity synonyms (sample)\n")
    for f in findings.get("ACRONYM_AMBIGUITY", [])[:40]:
        print(f"- `{f['file']}` ({f['mondo']}) — {', '.join(f['acronyms'])}")
    print()

    print("### Numbered / lettered series (sample)\n")
    for f in findings.get("NUMBERED_SERIES", [])[:40]:
        print(f"- `{f['file']}` ({f['mondo']}) — {', '.join(f['hits'])}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--markdown", action="store_true", help="emit full markdown report")
    args = ap.parse_args()
    rows = load_entries()
    findings = audit(rows)
    if args.markdown:
        print_markdown(rows, findings)
    else:
        print_summary(rows, findings)


if __name__ == "__main__":
    main()
