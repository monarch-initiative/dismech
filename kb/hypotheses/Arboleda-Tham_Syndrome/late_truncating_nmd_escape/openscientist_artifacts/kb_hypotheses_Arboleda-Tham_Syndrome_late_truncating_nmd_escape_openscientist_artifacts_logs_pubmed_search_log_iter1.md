# PubMed Search Log — Iteration 1 (2026-09-07)

Provider: MCP `search_pubmed` (NCBI eutils backend). Note: local index is sparse; several targeted queries returned 0 papers and two hit HTTP 429 rate limits (retried). This log records exact queries and outcomes.

| Query | Result | Key PMIDs |
|-------|--------|-----------|
| KAT6A syndrome genotype phenotype correlation truncating variants | 3 papers | 38741077, 35892268, 30245513 |
| KAT6A late truncating nonsense mediated decay escape last exon | 0 papers | — |
| Arboleda-Tham syndrome KAT6A de novo mutation intellectual disability | HTTP 429 (rate limit) | — |
| de novo mutations KAT6A syndromic intellectual disability craniofacial | 1 paper | 33552646 |
| KAT6A MOZ histone acetyltransferase haploinsufficiency function | 5 papers | 41702672, 27939639, 25912687, 25605372, 22921202 |
| Kat6a mouse model haploinsufficiency behavioral neurodevelopmental phenotype | 0 papers | — |
| de novo truncating mutations KAT6A cause intellectual disability | DB insert error; surfaced PMID 37577627 (ARTHS review, title null) | 37577627 |
| KAT6A monoallelic mutations global developmental delay AJHG 2015 | 0 papers | — |
| KAT6A syndrome dominant negative gain of function mechanism | 0 papers | — |
| KAT6A variants epigenetic machinery neurodevelopmental disorder | 1 paper | 38741077 |
| KAT6A DNA methylation episignature epigenetic signature | 0 papers | — |
| Kat6a acetyl-carnitine learning deficits mouse Voss | 1 paper | 41702672 |

## Notes / limitations
- The provider's index did not return the foundational 2015 discovery papers (Arboleda et al.; Tham et al., Am J Hum Genet) for the queries tried — these are cited from domain knowledge and flagged as NOT independently retrieved in this run.
- No direct molecular assay of NMD escape or mutant KAT6A protein in patient tissue was retrievable — consistent with the seed hypothesis's stated evidence gap.
- PMID 41702672 and 37577627 abstracts were returned truncated by the provider; only titles/partial text captured.
