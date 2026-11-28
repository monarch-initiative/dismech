# PubMed search log

Source: NCBI PubMed E-utilities (esearch/efetch), accessed via the
`search_pubmed` MCP tool. Search date: 2026-11-28. No date filters, no
language filters, default relevance ranking.

| # | Query string | max_results | Outcome | PMIDs returned |
|---|---|---|---|---|
| 1 | `corticosteroid-binding globulin deficiency SERPINA6 mutation human` | 15 | **Zero results** (query returned "No papers found"). Negative result recorded; the phrasing combining the gene symbol with "deficiency" and "human" retrieves nothing in this interface. Not evidence of absence of such papers: query 3 found them under different terms. | none |
| 2 | `corticosteroid-binding globulin knockout mice corticosterone stress response` | 15 | 9 results | 39240718, 31570737, 27153522, 25551181, 25244639, 24316201, 22930537, 20022933, 18204096 |
| 3 | `transcortin deficiency human kindred fatigue hypotension cortisol` | 15 | 2 results | 12780753, 11502797 |
| 4 | `corticosteroid-binding globulin cortisol pharmacokinetics free cortisol clearance` | 15 | 12 results | 36628386, 28521880, 24252379, 21054475, 17327382, 11595650, 10698174, 8237255, 3337226, 6833459, 7252405, 7400710 |
| 5 | `SERPINA6 genetic variation plasma cortisol GWAS` | 12 | **Failed**: HTTP 429 Too Many Requests from eutils efetch. Candidate PMIDs were resolved by esearch but abstracts could not be fetched: 40267698, 38941154, 37745713, 37667866, 35217314, 33822969, 33469137, 29679879, 25010111. These are **unverified** and are not cited in the report. | (not retrieved) |
| 6 | `corticosteroid-binding globulin neutrophil elastase cleavage targeted cortisol delivery inflammation` | 12 | 4 results | 36681594, 30058887, 27214312, 25409953 |
| 7 | `Torpy corticosteroid-binding globulin null mutation chronic fatigue syndrome` | 12 | 2 results | 19643166, 11502797 |

## Databases NOT searched in this run

GenCC, ClinGen, ClinVar, gnomAD, OMIM, ClinicalTrials.gov, GEO/ArrayExpress,
GTEx and UK Biobank were not queried. No claim of absence is made for any of
them. The SERPINA6 population-genetics literature (query 5) is therefore an
acknowledged, explicitly unresolved gap in this run.

## Iteration 2-3 queries (search date 2026-11-28)

| # | Query string | max_results | Outcome | PMIDs returned |
|---|---|---|---|---|
| 8 | `SERPINA6 SERPINA1 locus plasma cortisol genome-wide association` | 10 | 5 results. This is the successful retry of failed query 5. | 40267698, 37745713, 33822969, 33469137, 25010111 |
| 9 | `corticosteroid-binding globulin gene mutation prevalence chronic fatigue population study` | 10 | 1 result, and it is the already-known kindred report rather than the community screen being sought. | 11502797 |
| 10 | `corticosteroid binding globulin variants idiopathic fatigue cohort screening SERPINA6 Lyon` | 10 | **Zero results.** | none |

### Negative search, explicitly scoped

Queries 9 and 10 were aimed at the community-based study asserted in the
review PMID:19643166, which states "One community-based study revealed that
severe CBG mutations are rare in idiopathic fatigue disorders." That primary
study was **not retrieved** by either query through this PubMed interface on
2026-11-28. The claim therefore remains **review-level only and unverified at
the primary-source level** in this run. This is a retrieval failure, not
evidence that the study does not exist. A curator should resolve it by
following the reference list of PMID:19643166 directly.

### Still not searched in this run

No query was issued against GenCC, ClinGen, ClinVar, gnomAD, OMIM,
ClinicalTrials.gov, GEO, GTEx or UK Biobank. No absence claim is made for any
of them.

## Iteration 4 queries (search date 2026-11-28)

| # | Query string | max_results | Outcome | PMIDs returned |
|---|---|---|---|---|
| 11 | `corticosteroid-binding globulin blood pressure hypotension vascular mechanism` | 10 | **Zero results.** | none |
| 12 | `CBG Serpina6 blood pressure regulation mice` | 10 | **Zero results.** | none |
| 13 | `corticosteroid binding globulin hypertension` | 10 | 10 results. Retrieved the de novo transcortin Lyon case report (PMID:17245537), which was not found by queries 1-10. | 42992408, 42368271, 38941154, 29126409, 27144974, 19643166, 19226268, 17437519, 17245537, 10474128 |
| 14 | `corticosteroid-binding globulin reactive centre loop elastase cleavage site-specific cortisol delivery temperature` | 8 | **Zero results.** Over-specified query string. | none |
| 15 | `corticosteroid binding globulin elastase cleavage cortisol release inflammation` | 8 | 8 results. Successful reformulation of query 14. | 33085168, 30160799, 30058887, 28411181, 27887960, 26829559, 25409953, 24848868 |

### Negative search on the hypotension phenotype, explicitly scoped

Queries 11 and 12 returned zero results through this PubMed interface on
2026-11-28, and query 13 (the broader reformulation) returned no paper that
proposes a mechanism linking CBG loss to low blood pressure. The reported
hypotension in CBG-null humans (PMID:11502797, PMID:19643166) therefore has
**no retrieved mechanistic study** in this run. This is a scoped retrieval
result over PubMed only. No claim is made that such work does not exist, and
no model-knowledge explanation was substituted for the missing literature.

### Still not searched in this run

No query was issued against GenCC, ClinGen, ClinVar, gnomAD, OMIM,
ClinicalTrials.gov, GEO, GTEx or UK Biobank. No absence claim is made for any
of them.

## Iteration 5 queries (search date 2026-11-28)

| # | Query string | max_results | Outcome | PMIDs returned |
|---|---|---|---|---|
| 16 | `glucocorticoid receptor target gene dose-response cooperativity Hill coefficient transcription` | 8 | **Zero results.** Over-specified. No empirical Hill coefficient for GR target-gene transcription was obtained, so the Hill sweep in analysis A12 spans n = 1 to 4 as an assumption rather than a measured value. | none |
| 17 | `glucocorticoid receptor occupancy pulsatile gene transcription ultradian` | 8 | 3 results. Successful reformulation of query 16 toward the pattern-sensitivity question. | 34375333, 26690871, 20080870 |

### Unresolved parameter, explicitly scoped

Query 16 returned zero results on 2026-11-28. The Hill coefficient of the
downstream glucocorticoid response is therefore **not grounded in a retrieved
measurement** in this run. Analysis A12 treats it as a swept assumption over
n = 1 to 4 and reports that the conclusion (cooperativity does not bridge the
severity gap) holds across that whole range, so the missing parameter does not
change the result. No model-knowledge value was substituted.
