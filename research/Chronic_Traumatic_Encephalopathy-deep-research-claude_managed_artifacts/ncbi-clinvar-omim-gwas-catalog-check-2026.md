---
key: ncbi-clinvar-omim-gwas-catalog-check-2026
identifiers:
  - https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy
title: "Database presence check: ClinVar, OMIM, GWAS Catalog and PubMed for chronic traumatic encephalopathy (queries run 2026-11-09)"
authors: "Retrieval log (NCBI E-utilities and EBI GWAS Catalog web search)"
year: "2026"
journal: "Database query record (not a publication)"
url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi (queries listed below); https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy
source_url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi (queries listed below); https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy
sub_question: "Genetic and epigenetic factors in CTE (APOE, TMEM106B, MAPT, GRN, GWAS, polygenic, somatic mutation, DNA methylation, gene-environment)"
content: database record (verbatim fields)
---
title: "Database presence check: ClinVar, OMIM, GWAS Catalog and PubMed for chronic traumatic encephalopathy (queries run 2026-11-09)"
authors: Retrieval log (NCBI E-utilities and EBI GWAS Catalog web search)
year: 2026
journal: Database query record (not a publication)
identifiers: https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy
url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi (queries listed below); https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy
sub_question: Genetic and epigenetic factors in CTE (APOE, TMEM106B, MAPT, GRN, GWAS, polygenic, somatic mutation, DNA methylation, gene-environment)

## Text

Query 1: db=clinvar, term "chronic traumatic encephalopathy"[All Fields]
Result (verbatim): <Count>0</Count> ... <ErrorList><PhraseNotFound>chronic traumatic encephalopathy[All Fields]</PhraseNotFound></ErrorList><WarningList><OutputMessage>No items found.</OutputMessage></WarningList>

Query 2: db=omim, term "chronic traumatic encephalopathy"
Result: Count 2; IDs returned 600274 (FTDP-17 entry) and 157140 (MAPT entry). Neither is a CTE entry; the MAPT entry (https://omim.org/entry/157140) refers to CTE only in passing. No OMIM entry titled for CTE was returned.

Query 3: db=pubmed, "chronic traumatic encephalopathy"[MeSH Terms] AND "genetics"[MeSH Subheading]
Result: Count 33.

Query 4: db=pubmed, "chronic traumatic encephalopathy" AND ("genome wide association" OR GWAS)
Result: Count 7. Records returned: 41377989 (2026, DNA methylation preprint); 41059714 (2025, AD genes in African American donors, not CTE-specific); 36932726 (2023, innate immune response in tauopathies); 36683334 (2023, Lis-1 in Drosophila TBI); 32050258 (2020, novel tau filament fold in corticobasal degeneration); 31141716 (2019, TBI and mental health in veterans); 28983503 (2017, AD genetic risk variants beyond APOE e4 predict mortality). None reports a CTE GWAS in PubMed; the CTE GWAS found is the conference abstract atherton-2020-gwas-cte-abstract.md.

Query 5: db=pubmed, "chronic traumatic encephalopathy" AND (polygenic OR "polygenic risk" OR "polygenic score")
Result: Count 1: 36683334 (Lis-1 Drosophila TBI study, not a CTE study).

Query 6: db=pubmed, "chronic traumatic encephalopathy" AND ("somatic mutation" OR "methylation" OR "epigenetic")
Result: Count 8.

Query 7: EBI GWAS Catalog web search, query "chronic traumatic encephalopathy" (https://www.ebi.ac.uk/gwas/search?query=chronic%20traumatic%20encephalopathy)
Result (verbatim page text): "No results found for search term". The legacy GWAS Catalog REST API returned: "This legacy GWAS Catalog REST API is no longer available."
