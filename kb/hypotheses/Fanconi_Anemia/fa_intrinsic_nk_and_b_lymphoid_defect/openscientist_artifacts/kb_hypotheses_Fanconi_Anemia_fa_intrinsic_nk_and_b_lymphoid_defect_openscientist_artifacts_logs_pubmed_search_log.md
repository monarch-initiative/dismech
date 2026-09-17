# PubMed search log — FA intrinsic NK/B lymphoid defect

Source: NCBI PubMed E-utilities via MCP `search_pubmed`. Search date: 2026-09-13.
Retrieval = titles + full abstracts. No date filters applied. No API key / cohort filters beyond query strings.

| # | Query | max | Result summary |
|---|-------|-----|----------------|
| 1 | Fanconi anemia natural killer cell NK function | 12 | 12 hits; key: 21542827, 28557197, 30949167, 34348001, 24240977, 25963299, 35671096, 35912855, 24831839 |
| 2 | Fanconi anemia immune function B cells lymphocytes children | 8 | 8 hits; key: 28557197, 21542827, 26895835, 25963299 |
| 3 | Fanconi anemia p53 hematopoietic stem progenitor cell apoptosis attrition | 10 | 1 hit: 27720904 (fetal Fancd2, p53-INDEPENDENT) |
| 4 | Fanconi anemia mouse model lymphocyte development B cell intrinsic defect Fancc Fanca | 10 | 0 hits (no usable result) |
| 5 | Fanconi anemia infection susceptibility immunodeficiency clinical outcomes | 8 | FAILED: HTTP 429 rate-limit (not retried this iteration) |
| 6 | Fanconi anemia bone marrow p53 p21 hyperactive hematopoietic stem cell Ceccaldi | 8 | 0 hits |
| 7 | Fanconi anemia p53 activation bone marrow failure hematopoiesis | 8 | FAILED: DB write IntegrityError on one null-title record (29427417); no usable return |
| 8 | exacerbated p53 p21 DNA damage response bone marrow failure Fanconi anemia | 6 | 1 hit: 22683204 (Ceccaldi 2012) |

## Negative / null searches (curation-relevant absences as of 2026-09-13)
- Query 4 returned **0 papers** for a directed FA mouse lymphoid-development query. A dedicated study of thymic/BM lymphoid-progenitor output in FA mice was NOT surfaced. Label: unverified absence (single query; broader terms not exhausted).
- No GenCC / ClinGen / ClinVar / GEO / clinicaltrials.gov query was run this iteration — those source-level checks are OUTSTANDING, not negative.
- No omics dataset (e.g., FA lymphoid scRNA-seq) was located or accessed; none provided as input data.

## Tool failures (reported, not silently worked around)
- Query 5: PubMed 429 rate-limit — search not completed.
- Query 7: provider literature-store IntegrityError (null title on PMID 29427417) — no results returned to agent.
