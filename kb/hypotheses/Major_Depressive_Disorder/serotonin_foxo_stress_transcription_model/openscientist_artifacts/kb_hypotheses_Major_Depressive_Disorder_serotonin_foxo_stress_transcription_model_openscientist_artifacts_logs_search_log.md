# Search log — serotonin_foxo_stress_transcription_model (MDD)
# Provider: NCBI PubMed via MCP search_pubmed; Open Targets Platform GraphQL v26.9.0
# Search dates: 2026-10-09 (Iterations 1-4)

## PubMed queries and outcomes
| Query | Result | Key PMIDs |
|---|---|---|
| serotonin DAF-16 FOXO signaling stress responses C. elegans tph-1 | 1 hit | 17141627 |
| FOXO3 FOXO1 transcription factor major depressive disorder human brain | 0 hits (too specific) | — |
| lithium GSK3 FOXO beta-arrestin Akt depression mechanism | 0 hits | — |
| antidepressant insulin IGF-1 PI3K Akt signaling hippocampus depression | 429 rate-limited | — |
| FOXO3 depression | 8 hits | 42632434, 41622191, 41249439, 39710185, 41962727 |
| FoxO1 depression antidepressant | 8 hits | 36819781, 36039087, 37173696, 40237232, 40690054 |
| clozapine lithium beta-arrestin SGK DAF-16 FOXO localization | 1 hit | 21732403 |
| lithium GSK3beta FOXO3a nuclear translocation | 0 hits | — |
| GSK3 FOXO phosphorylation nuclear export | 1 hit | 23687303 |
| serotonin insulin IGF-1 signaling neurons mammalian | 5 hits | 15541711 (review), 28088287 |
| insulin resistance major depressive disorder bidirectional | 6 hits | 40595333, 41555281, 41780463, 41373743 |
| serotonin hypothesis depression umbrella review no evidence | 3 hits | 35854107, 42538881, 36356194 |
| serotonin 5-HT receptor FOXO transcription factor brain neurons | 1 hit (C. elegans only) | 29491136 |
| fluoxetine FOXO3a hippocampus phosphorylation | 0 hits (NEGATIVE) | — |
| fluoxetine Akt FOXO neuronal | 0 hits (NEGATIVE) | — |
| SGK1 glucocorticoid stress depression hippocampus | DB insert error (null-title record PMID 39796528) | — |
| SGK1 antidepressant neurogenesis forkhead | 0 hits | — |

### Negative-search declarations (search date 2026-10-09, source: PubMed via MCP)
- No direct mammalian/human paper demonstrating a serotonin -> FOXO edge was retrieved (3 phrasings; only C. elegans returned).
- No human MDD brain transcriptomic/genetic study directly tying serotonergic tone to FOXO1/3/4 retrieved.

## Open Targets Platform GraphQL (endpoint https://api.platform.opentargets.org/api/v4/graphql, v26.9.0, disease MONDO_0002009, 2026-10-09)
- Disease resolution: search "major depressive disorder" -> MONDO_0002009.
- Per-target association + datatype scores for FOXO1/3/4/6, INSR, IGF1R, SGK1, AKT1, TPH2, SLC6A4, BDNF. -> data/opentargets_foxo_mdd_associations.csv
- Genetic (gwas_credible_sets/gene_burden) evidence counts per gene: only FOXO1 had 1 credible-set row; FOXO3/4/6, INSR, IGF1R, SGK1, AKT1 had 0.
- FOXO1 credible-set resolution: rs180828263 (13_40534758_C_T), p=4e-9, study GCST90096932 (cognition x MDD interaction, PMID 34782712, n=9567), L2G=0.469. -> data/foxo1_mdd_crediblesets.json
- Top-30 MDD targets by overall score (context). -> data/mdd_top_targets_context.csv
