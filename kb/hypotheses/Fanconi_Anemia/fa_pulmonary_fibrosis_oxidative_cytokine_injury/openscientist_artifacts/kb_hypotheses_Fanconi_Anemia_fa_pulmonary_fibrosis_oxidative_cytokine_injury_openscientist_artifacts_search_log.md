# PubMed Search Log

- **Provider:** OpenScientist `search_pubmed` tool (NCBI PubMed E-utilities `esearch`/`efetch`)
- **Endpoint:** https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
- **Search dates:** 2026-09-13 (iterations 1–3)
- **Access outcome:** ACCESSED (returned titles + full abstracts). Two queries hit HTTP 429 rate-limits and were retried/rephrased (noted below).
- **No controlled/patient-level data, data lake, or credentials were accessed.** This run is literature-only; no omics/cohort dataset was available or analyzed.

Each row: query string | max_results | # returned | key PMIDs (relevance).

| # | Query | max | returned | Key PMIDs |
|---|-------|-----|----------|-----------|
| 1 | Fanconi anemia interstitial lung disease pulmonary fibrosis | 8 | 4 | 9096763 (seed case), 25539146 (TINF2 IPF), 23647631 (review), 2671924 (transplant series) |
| 2 | Fanconi anemia oxidative stress reactive oxygen species | 8 | 8 | 42121854 (review ROS/mito), 31472450 (Fancd2 HSPC mito ROS), 32989015 (FANCG mito), 34726902 (ROS ICL) |
| 3 | Fanconi anemia TNF-alpha cytokine overproduction hematopoiesis | 8 | 2 | 25534205 (p38/TNF FANCA), 22234699 (p38/TNF FANCC/FANCA) |
| 4 | telomere biology disorder pulmonary fibrosis alveolar epithelial cell mechanism | 6 | 5 | 42035100 (ATII senescence IPF), 40425299 (review), 24504062 (DKC1 FIP), 22364217 (hTERT IPF), 35420997 (SIX1) |
| 5 | Fanconi anemia hematopoietic stem cell transplant pulmonary complications idiopathic pneumonia | 6 | 0 | — (NEGATIVE) |
| 6 | idiopathic pulmonary fibrosis oxidative stress alveolar epithelium TGF-beta cytokine | 6 | 1 | 22240154 (ROS→EMT via TGF-β1) |
| 7 | Fanconi anemia telomere shortening accelerated attrition | 6 | 2 | 23647631 (review), 20022886 (FANCC telomere attrition) |
| 8 | Fanconi anemia lung pulmonary bleomycin fibrosis mouse model FANCD2 | 6 | 0 | — (NEGATIVE) |
| 9 | idiopathic pneumonia syndrome bone marrow transplant conditioning lung injury pathogenesis | 6 | HTTP 429 | rate-limited; rephrased as #12 |
| 10 | Fanconi anemia pulmonary manifestations case report lung | 6 | 4 | 26535538 (aspergillosis), 21792042 (glial heterotopia), 18300309 (pulmonary Sweet's), 9096763 |
| 11 | idiopathic pneumonia syndrome allogeneic transplant conditioning TNF-alpha lung injury | 6 | 1 | 9276718 (Cy+TBI epithelial injury, TNF/IL-1/TGF-β) |
| 12 | Fanconi anemia quercetin antioxidant tempol resveratrol treatment oxidative | 6 | 0 | — (NEGATIVE) |
| 13 | Fanconi anemia cellular senescence senescence-associated secretory phenotype fibrosis epithelial | 6 | HTTP 429 | rate-limited; rephrased as #14 |
| 14 | Fanconi anemia senescence organ fibrosis non-hematopoietic epithelial | 6 | 0 | — (NEGATIVE) |
| 15 | Fanconi anemia FANCD2 liver kidney fibrosis organ inflammation | 6 | 0 | — (NEGATIVE) |
| 16 | DNA damage response senescence lung fibrosis alveolar type 2 cell TGF-beta | 6 | 2 | 39068977 (CORM2 DDR/SASP fibrosis), 25790295 (p66Shc) |
| 17 | Fanconi anemia TGF-beta hypersensitivity hematopoietic stem cell inhibition rescue | 6 | 0 | — (NEGATIVE; rephrased as #18) |
| 18 | Fanconi anemia TGF-beta pathway DNA repair | 6 | 6 | 40555815 (miR-29a-3p/TGF-β), 36441774 (TGFβ-NHEJ Fancd2 embryo), 35605178 (IBMFS review) |

## Negative-search summary (curation-relevant absences, PubMed, 2026-09-13)
Queries #5, #8, #12, #14, #15 returned zero results. Together they indicate **no retrievable**: (a) FA post-transplant pulmonary-complication series indexed to these terms, (b) FA pulmonary-fibrosis animal model, (c) FA lung-directed antioxidant/anti-cytokine trial, (d) FA non-hematopoietic organ-fibrosis literature. Absence is bounded by these exact query strings and the tool's retrieval/indexing; label **unverified** beyond these queries (broader MeSH-expanded searches were not run).
