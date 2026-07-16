#!/usr/bin/env python3
"""Recommendation-specific guideline search: find guidelines whose ABSTRACT
states specific, actionable clinical recommendations.

Why this exists
---------------
The project's count-ranked search (``collect_guidelines.py``) ranks disorders by
*how many* Practice Guidelines exist. That is a good prioritization signal but a
poor evidence-sourcing one: it surfaces the flagship umbrella guideline, whose
abstract is frequently pure scope/process metadata (OBJECTIVE / TARGET
POPULATION / EVIDENCE / METHODS / panel composition, or a chapter list) with no
concrete recommendation in it. Such an abstract cannot yield a snippet-verified
evidence item, however authoritative the guideline is.

What counts as usable
---------------------
An abstract is usable when it states a **specific, actionable clinical
recommendation** naming an intervention of ANY modality -- drug, surgical or
interventional procedure, radiotherapy, device, diet, rehabilitation, monitoring
interval -- or a **diagnostic action** (screening, imaging, biopsy, staging,
testing). Care guidelines are not only about drugs; scoring only drug names
encodes a pharmacology bias and wrongly discards surgical, diagnostic, and
supportive-care guidance.

Two false-positive traps this guards against (both observed in real abstracts):

* **Author affiliations** -- "Department of Surgery, ..." matches an
  intervention vocabulary but recommends nothing. The author/affiliation front
  matter is stripped before scoring. (The ESMO metastatic-colorectal guideline
  scored 6 "intervention" hits that were all department names.)
* **Chapter/TOC listings** -- "1) Definition; ... 5) Surgical management" names
  modalities without recommending anything. Requiring a recommendation cue
  (``we recommend``, ``should be offered``, ``first-line``, ...) demotes these.

Hits are therefore ranked by ``recommendation_sentences`` (sentences carrying
BOTH an intervention/diagnostic term AND a recommendation cue), with the looser
``intervention_sentences`` reported alongside for triage.

Usage
-----
    uv run python therapy_specific_search.py spec.json out.json

``spec.json`` is a list of ``{slug, query, terms?}``. ``terms`` is optional and
*extends* the default intervention vocabulary with disease-specific terms (drug
names, named procedures); omit it to score on the defaults alone.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "tool=dismech&email=jhc@lbl.gov"

# Modality-agnostic: drugs are only one branch of clinical care.
DEFAULT_INTERVENTION_TERMS = [
    # pharmacological (generic; pass specific drug names via spec "terms")
    r"therapy", r"treatment", r"drug", r"agent", r"regimen", r"dose", r"dosage",
    r"prophylaxis", r"antibiotic", r"vaccine", r"vaccination",
    # procedural / surgical / device
    r"surgery", r"surgical", r"resection", r"excision", r"laparoscop\w+",
    r"transplant\w*", r"ablation", r"stent\w*", r"catheter\w*", r"device",
    r"implant\w*", r"drainage", r"paracentesis", r"dialysis", r"ventilation",
    # radiation
    r"radiotherapy", r"radiation", r"brachytherapy", r"chemoradiation",
    r"stereotactic",
    # diagnostic / monitoring
    r"screening", r"surveillance", r"biopsy", r"staging", r"imaging",
    r"colonoscopy", r"endoscopy", r"ultrasound", r"echocardiograph\w*",
    r"monitoring", r"testing", r"test\b", r"assessment", r"evaluation",
    # laboratory / pathology diagnostics. "serology" was missing and cost a
    # real false negative: the Lyme borreliosis diagnostic guideline says
    # "Serology is recommended only in suspected disseminated LB" -- a clear
    # recommendation that scored 0 because the cue matched but no intervention
    # term did. The scorer requires BOTH, so a missing noun silently kills a hit.
    r"serolog\w*", r"assay", r"antibod\w*", r"antigen", r"culture",
    r"histolog\w*", r"cytolog\w*", r"genotyping", r"sequencing",
    # supportive / lifestyle
    r"diet\w*", r"nutrition\w*", r"exercise", r"physiotherapy",
    r"rehabilitation", r"counsel\w*", r"supportive care", r"palliative",
]

# A recommendation cue distinguishes guidance from a chapter list or a
# department name. This is what makes the score mean "recommends something".
RECOMMENDATION_CUES = [
    r"we recommend", r"is recommended", r"are recommended", r"recommends",
    r"we suggest", r"is suggested", r"should be", r"should undergo",
    r"should receive", r"should not", r"may be offered", r"is indicated",
    r"first-line", r"second-line", r"strong recommendation",
    r"conditional recommendation", r"we make strong", r"best practice advice",
    r"is preferred", r"preferred", r"advise",
]

# Everything before the abstract body: citation, authors, affiliations. Matching
# "Department of Surgery" as an intervention is the classic false positive.
_FRONT_MATTER = re.compile(
    r"^.*?Author information:.*?(?=(?:[A-Z][A-Z /-]{3,}:)|$)", re.S
)


def _get(url: str) -> str:
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def esearch(term: str, retmax: int = 6) -> list:
    u = (f"{EUTILS}/esearch.fcgi?db=pubmed&term={urllib.parse.quote(term)}"
         f"&retmax={retmax}&retmode=json&{TOOL}")
    return json.loads(_get(u))["esearchresult"]["idlist"]


def efetch_abstract(pmid: str) -> str:
    u = (f"{EUTILS}/efetch.fcgi?db=pubmed&id={pmid}&rettype=abstract"
         f"&retmode=text&{TOOL}")
    return re.sub(r"\s+", " ", _get(u))


def strip_front_matter(text: str) -> str:
    """Drop citation/author/affiliation text so it cannot score as content."""
    stripped = _FRONT_MATTER.sub("", text, count=1)
    return stripped if len(stripped) > 200 else text


def title_of(text: str) -> str:
    m = re.search(r"\d{4}[;:][^.]*\.\s*(.+?\.)\s", text)
    return m.group(1).strip() if m else ""


def score(text: str, terms: list) -> tuple:
    """Return (recommendation_sentences, intervention_sentences)."""
    body = strip_front_matter(text)
    iv = re.compile("|".join(terms), re.I)
    cue = re.compile("|".join(RECOMMENDATION_CUES), re.I)
    sents = re.split(r"(?<=[.:]) ", body)
    intervention = [s.strip() for s in sents if iv.search(s)]
    recommendation = [s for s in intervention if cue.search(s)]
    return recommendation, intervention


def build_vocab(terms: list = None) -> list:
    """Default patterns are deliberate regexes; curator terms are literals.

    A curator passing a real drug or procedure name ("5-HT4 agonist",
    "atezolizumab + bevacizumab", "Trikafta (ETI)") should not have to know
    regex — and an unescaped ``+`` or ``(`` would either change the match or
    raise. Escape the supplied terms, leave the defaults alone.
    """
    return DEFAULT_INTERVENTION_TERMS + [re.escape(t) for t in (terms or [])]


def run(slug: str, term: str, terms: list = None, retmax: int = 6) -> dict:
    vocab = build_vocab(terms)
    pmids = esearch(term, retmax)
    time.sleep(0.4)
    hits = []
    for p in pmids:
        try:
            txt = efetch_abstract(p)
        except Exception as e:  # network/rate-limit; keep the record honest
            hits.append({"pmid": p, "error": str(e)[:60]})
            continue
        rec, iv = score(txt, vocab)
        hits.append({
            "pmid": p,
            "title": title_of(txt)[:160],
            "abstract_len": len(txt),
            "recommendation_sentences": len(rec),
            "intervention_sentences": len(iv),
            "sample_recommendation": rec[0][:240] if rec else None,
        })
        time.sleep(0.4)
    hits.sort(key=lambda h: (-h.get("recommendation_sentences", 0),
                             -h.get("intervention_sentences", 0)))
    return {"slug": slug, "query": term, "extra_terms": terms or [],
            "n_hits": len(pmids), "hits": hits}


def main(argv: list) -> int:
    with open(argv[1]) as fh:
        spec = json.load(fh)
    out = [run(s["slug"], s["query"], s.get("terms")) for s in spec]
    with open(argv[2], "w") as fh:
        json.dump(out, fh, indent=1)
    for r in out:
        best = r["hits"][0] if r["hits"] else {}
        print(f"{r['slug']}: {r['n_hits']} hits | best PMID:{best.get('pmid')} "
              f"rec={best.get('recommendation_sentences')} "
              f"iv={best.get('intervention_sentences')} "
              f"| {(best.get('title') or '')[:55]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
