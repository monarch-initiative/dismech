# PubMed Search Log — Myosin inhibitors: obstruction relief vs. sarcomere substrate (HCM)

Source: PubMed via OpenScientist `search_pubmed` MCP tool (NCBI E-utilities esearch/efetch backend).
Search dates: 2026-10-09 (Iterations 1–2). Database: PubMed (live, no fixed snapshot version exposed by API).
Note: tool returns titles + full abstracts + PMIDs. Rate-limit (HTTP 429) encountered once; affected query re-run or rephrased.

| # | Query | max_results | Outcome | Key PMIDs returned |
|---|-------|-------------|---------|--------------------|
| 1 | mavacamten EXPLORER-HCM obstructive hypertrophic cardiomyopathy outflow tract gradient | 6 | 6 hits | 42636950, 42417692, 42251960, 42211824, 41848906, 41580106 |
| 2 | mavacamten non-obstructive hypertrophic cardiomyopathy MAVERICK ODYSSEY | 6 | 0 hits (no usable result) | — |
| 3 | aficamten SEQUOIA-HCM obstructive hypertrophic cardiomyopathy | 6 | 6 hits | 42667283, 42624353, 42544039, 42417692, 42101453, 42002189 |
| 4 | mavacamten nonobstructive hypertrophic cardiomyopathy phase 2 exercise capacity NT-proBNP | 6 | 0 hits | — |
| 5 | myosin super-relaxed state ATP sarcomere energetics hypertrophic cardiomyopathy mechanism | 6 | 2 hits | 35177471, 34014247 |
| 6 | mavacamten cardiac magnetic resonance fibrosis myocardial structure EXPLORER reverse remodeling | 6 | HTTP 429 rate-limit (failed) | — |
| 7 | mavacamten diastolic function myocardial energetics phosphocreatine load-independent | 6 | 0 hits | — |
| 8 | MAVERICK-HCM nonobstructive mavacamten | 5 | 5 hits | 41841680, 41590843, 40624601, 40606967, 40530507 |
| 9 | mavacamten T1 mapping extracellular volume fibrosis cardiac MRI hypertrophic cardiomyopathy | 6 | 0 hits | — |
| 10 | cardiac myosin inhibitor reverse remodeling left ventricular mass cardiac MRI aficamten | 6 | 1 hit | 39217563 |
| 11 | EXPLORER-HCM cardiovascular magnetic resonance substudy mavacamten left ventricular mass late gadolinium | 5 | 0 hits | — |
| 12 | mavacamten cardiac remodeling MRI mass NTproBNP troponin obstructive | 6 | 0 hits | — |
| 13 | mavacamten preclinical mouse model prevents hypertrophy fibrosis sarcomere | 6 | 0 hits | — |
| 14 | mavacamten mouse genetic hypertrophic cardiomyopathy myosin inhibition prevents | 6 | 0 hits | — |
| 15 | small molecule inhibitor sarcomere contractility suppresses hypertrophic cardiomyopathy mice | 5 | 1 hit | 26912705 |
| 16 | aficamten SEQUOIA CMR substudy left ventricular mass left atrial volume myocardial mass index | 4 | 0 hits | — |
| 17 | aficamten cardiac structure function obstructive hypertrophic cardiomyopathy magnetic resonance | 4 | 4 hits | 42152261, 41093262, 39645546, 39217563 |
| 18 | mavacamten diastolic function filling pressure echocardiography obstructive hypertrophic cardiomyopathy improvement | 5 | 2 hits | 41688269, 41590843 |
| 19 | mavacamten myocardial fibrosis late gadolinium enhancement does not change biopsy human | 5 | 5 hits | 42715826, 42083705, 41877729, 41711735, 40632050 |
| 20 | mavacamten super-relaxed state energy sparing myosin ATP turnover hypercontractility human cardiomyocyte | 5 | 0 hits | — |
| 21 | mavacamten super-relaxed state myosin ATPase hypercontractility mechanism of action | 5 | 3 hits | 40000285, 30674652, 30371160 |

## Negative-search notes (curation-relevant absences)
- Queries #2, #4 (explicit "ODYSSEY"/"MAVERICK" + phase/biomarker terms) returned 0 hits in this tool, but the trials ARE captured indirectly: ODYSSEY-HCM primary-endpoint miss and MAVERICK-HCM/REDWOOD cohort-4 biomarker gains are reported in review PMID 40624601 (query #8) and PMID 41841680. A dedicated primary-report PMID for ODYSSEY-HCM was NOT located via this tool as of 2026-10-09 — treat as "primary trial report not retrieved" (unverified absence, tool-indexing limitation, not confirmed absence in PubMed).
- Queries #9, #11, #12 (direct T1/ECV/LGE for mavacamten) returned 0 hits, but relevant CMR fibrosis evidence was found via #17/#19 (PMID 42715826, 40632050, 41877729). The targeted term combinations simply failed to match; not a true absence.
- No dataset/omics/GenCC/ClinGen query was run this session (hypothesis is pharmacodynamic/trial-level, not a gene–disease validity claim). Recorded as source-level absence: no primary omics or trial-registry (ClinicalTrials.gov) API was queried; trial identities taken from abstract text (NCT IDs listed therein).
