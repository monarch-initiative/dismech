---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-19T01:20:00Z'
end_time: '2026-04-19T02:15:00Z'
duration_seconds: 3300.0
citation_count: 6
notes: >
  Manual phenotype-focused curation review completed from PubMed / cached
  reference text before revising `kb/disorders/Atelosteogenesis_Type_III.yaml`.
  The goal was to maximize phenotype completeness without adding claims that
  could not be supported by exact PMID-backed text.
---

## Question

Deep-review the phenotype manifestations of Atelosteogenesis Type III and identify which phenotype assertions for the disorder file are directly supportable from exact PMID-backed evidence, which clinically important phenotypes are missing, and which candidate claims should be omitted or softened.

## Output

# Atelosteogenesis Type III phenotype curation note

## Core phenotype additions supported

- **Disproportionate short-limb short stature** is directly supportable from the original AOIII delineation as a "short-limb dwarfism syndrome" (PMID:2368807) and from the updated FLNB GeneReviews summary describing FLNB-AO3 as "severe short-limbed dwarfism" (PMID:20301736).
- **Large joint dislocations** were missing from the file despite being a hallmark of the FLNB-AO3 phenotype. Primary mutation-series evidence supports joint dislocations in AOI/AOIII (PMID:16752402), and GeneReviews localizes these to the hips, knees, and elbows in AO3 (PMID:20301736).
- **Apnea** is directly documented in the 1992 long-term survivor report together with severe tracheomalacia and tracheostomy requirement (PMID:1442028).
- **Motor delay** is supportable only in a qualified way from the same survivor report, which states the infant survived more than one year "with motoneuronal developmental delay" (PMID:1442028). Because this may reflect secondary morbidity rather than a primary neurodevelopmental effect, the YAML description should stay cautious.

## Existing phenotype claims retained

- **Rhizomelia**, **clubfoot**, **humeral hypoplasia**, **coronal cleft vertebrae**, **scoliosis**, **hypertelorism**, **flat/depressed nasal bridge**, **micrognathia**, **cleft palate**, **broad thumbs**, and **tracheomalacia** are all directly supportable from the abstract of the Japanese survivor report (PMID:1442028).

## Candidate claims not added or intentionally softened

- **Pelvic hypoplasia, rib hypoplasia, and generalized vertebral hypoplasia** are mentioned in broader AOIII summaries (for example PMID:27258362), but the abstract language is too introductory and nonspecific to map confidently to narrower HPO terms without overclaiming.
- **Specific toe phenotypes** were not added. PMID:1442028 notes that the feet had abnormalities similar to the short broad thumbs, but the abstract does not localize the finding clearly enough to justify `Broad hallux` or another toe-specific HPO term.
- **Intellectual disability / global developmental delay** were not added. PMID:8008496 mentions prognosis for physical and intellectual disability only at a high level, without a clean disease-level assertion or count.
- **Frequency and onset qualifiers** were omitted because none of the usable AOIII phenotype abstracts directly quantify occurrence or provide a cohort-based onset statement for the added entries.

## PubMed set reviewed

- PMID:1442028
- PMID:2368807
- PMID:8008496
- PMID:10076882
- PMID:16752402
- PMID:20301736
