# Environment record

- Runtime: Python 3.12.13 (MCP `execute_code` sandbox)
- Key package: requests 2.34.2
- Network access: outbound HTTPS to Ensembl REST, UniProt REST, gnomAD GraphQL (all resolved, status 200, 2026-09-07)
- No random seeds used (all analyses are deterministic API lookups + arithmetic on returned coordinates)
- No local data files were provided for this job; all inputs are public web APIs.

## External data sources (not bundled; recorded by stable identifier)
| Source | Stable ID / URI | Version/Snapshot | Retrieved |
|--------|-----------------|------------------|-----------|
| Ensembl REST | ENST00000265713 / ENSG00000083168 | Ensembl (GRCh38, current release as served 2026-09-07) | 2026-09-07 |
| UniProt | Q92794 (KAT6A_HUMAN) | current entry served 2026-09-07 | 2026-09-07 |
| gnomAD GraphQL | KAT6A, GRCh38 | gnomAD constraint (as served) | 2026-09-07 |
| PubMed (MCP search_pubmed) | see logs/pubmed_search_log_iter1.md, iter3.md | live index | 2026-09-07 |
