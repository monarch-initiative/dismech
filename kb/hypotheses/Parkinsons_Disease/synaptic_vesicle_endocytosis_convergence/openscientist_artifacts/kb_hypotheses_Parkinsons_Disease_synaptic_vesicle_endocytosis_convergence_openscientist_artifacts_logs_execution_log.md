# Execution log — genetic evidence check

Date retrieved: 2026-10-18
Environment: OpenScientist execute_code sandbox (python3, requests). `urllib` blocked; `requests` allowed.

## Sources accessed
1. Open Targets Platform GraphQL — https://api.platform.opentargets.org/api/v4/graphql
   - meta: name "Open Targets GraphQL & REST API Beta", apiVersion 26.9.0, dataVersion 26.09
   - Query: target(ensemblId).associatedDiseases -> PD (MONDO_0005180) overall score + datatypeScores
   - Outcome: SUCCEEDED
2. GWAS Catalog REST API v2 — https://www.ebi.ac.uk/gwas/api/v2/genes/{gene}/associations
   - Legacy v1 REST (/gwas/rest/api/...) returned HTTP 410 (retired). Migrated to v2 endpoint.
   - Query: per-gene associations, filtered to Parkinson trait, p = pValue*10^pValueExponent, threshold 5e-8
   - Outcome: SUCCEEDED
3. GWAS Catalog legacy v1 REST — OUTCOME: FAILED (HTTP 410, API retired). Fallback = v2 endpoint (success).

## Key results (see data/gene_pd_genetic_evidence.csv)
- Strong common-variant PD GWAS: SNCA (min p 4e-170), LRRK2 (4e-148), SH3GL2 (8e-21).
- Zero common-variant GWAS Catalog PD hits: SYNJ1, DNAJC6, VPS35, ITSN1 (rare/monogenic) and GBA (mapped-gene limitation).
- Open Targets genetic_association datatype absent for ITSN1/SYNJ1/DNAJC6 (literature/animal_model only);
  ITSN1 rare-variant burden (PMID 40056900, 2025) not yet integrated into OT v26.09.

## Limitations
- GWAS Catalog uses nearest/mapped-gene annotation; absence of a gene != absence of signal (GBA is a known example).
- Open Targets aggregated scores lag primary literature; newest findings (ITSN1 2025) under-represented.
- No patient-level or omics data were accessed; this is an aggregate database cross-check only.
