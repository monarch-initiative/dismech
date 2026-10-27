# PubMed / NCBI eutils search log

Provider: OpenScientist `search_pubmed` MCP tool (NCBI E-utilities backend) + direct eutils efetch.
Search date: 2026-09-07. All searches English, no date filter unless noted.

| # | Query | Hits (returned) | Usable PMIDs |
|---|-------|-----------------|--------------|
| 1 | Bohring-Opitz syndrome ASXL1 truncating mutation mechanism | 4 | 42523271, 40276524, 33242595, 31006630 |
| 2 | ASXL1 truncated protein gain of function clonal hematopoiesis | 3 | 30927018, 30515738, 26700326 |
| 3 | ASXL1 nonsense-mediated decay escape truncated protein stability | 1 | 41925445 |
| 4 | Bohring-Opitz ASXL1 multiomics Wnt signaling dysregulation epigenome | 1 | 37053013 |
| 5 | mutant ASXL1 BAP1 deubiquitinase H2AK119ub gain of function myeloid | 2 | 34186160, 30515738 |
| 6 | Asxl1 mouse model developmental phenotype loss of function | 2 | 24255920, 24218140 |
| 7 | ASXL1 C-terminal degron protein stability truncation gain of function | 1 | 41925445 |
| 8 | ASXL1 mutation Wilms tumor Bohring-Opitz cancer predisposition | 1 | 25921057 |

## Negative / empty searches (checked, no usable result as of 2026-09-07)
- "ASXL1 knockout mouse neurodevelopment Bohring-Opitz phenotype" -> 0 hits
- "Bohring-Opitz syndrome ASXL1 variant spectrum exon distribution genotype phenotype cohort" -> 0 hits
- "Bohring-Opitz syndrome ASXL1 de novo mutation clinical features Hoischen Russell" -> 0 hits
- "ASXL1 truncated protein detected patient cells Bohring-Opitz Western blot expression" -> 0 hits
  (KNOWLEDGE GAP: no PubMed hit directly demonstrating endogenous truncated ASXL1 PROTEIN in germline BOS patient cells)
- "ASXL1 dominant negative versus loss of function controversy myeloid mechanism" -> 0 hits
- "ASXL1 gnomAD loss of function intolerance constraint protein truncating variant location" -> 0 hits
- "Truncating ASXL1 Bohring-Opitz Arboleda 2026 protein stability degron" -> 0 hits (title-word phrasing failed; paper found via query #1)

## Notes
- Rate-limit (HTTP 429) hit once on parallel eutils calls in Iteration 1; retried sequentially.
- Full abstracts for PMID 42523271 and 40276524 retrieved directly via eutils efetch (rettype=abstract)
  because the MCP-stored abstracts were truncated stubs; verbatim snippets used in the report/curation
  leads come from those full abstracts and are flagged for curator re-validation against full text.
- PMID 42523271 is a bioRxiv PREPRINT (2026.07.13.737346; PMCID PMC13404655); not peer-reviewed.
