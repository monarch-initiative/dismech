# G2P All-Gene Audit Summary

Companion artifacts:

- [Gene-level summary TSV](/Users/cjm/worktrees/dismech-g2p-db/docs/research/g2p_all_genes_gene_summary_2026_03_28.tsv)
- [Actionable row-level triage TSV](/Users/cjm/worktrees/dismech-g2p-db/docs/research/g2p_all_genes_row_triage_2026_03_28.tsv)

The row-level triage TSV omits fully resolved `ROOT_MATCH` rows so it can be
used directly as a curator worklist.

- G2P source: `https://ftp.ebi.ac.uk/pub/databases/gene2phenotype/G2P_data_downloads/2026_03_28/allG2P_2026-03-28.csv.gz`
- Genes audited: 3144
- G2P rows audited: 3829
- Actionable rows: 3810
- Genes with direct dismech matches: 158
- Genes with G2P MONDO collisions: 37

## Aggregate Row Status Counts

- EMBEDDED_NOT_ROOTED: 492
- NO_DISMECH_MATCH: 3170
- ROOT_MATCH: 19
- ROOT_MATCH_PMID_GAP: 46
- SPLIT_ACROSS_DISMECH: 39
- UNDERREPRESENTED_IN_DISMECH: 63

## Genes By Highest Curation Priority

- CRITICAL: 2707
- HIGH: 60
- MEDIUM: 368
- LOW: 9

## Most Common Primary Actions

- ADD_FIRST_GENE_DISEASE_ANCHOR: 2707
- REVIEW_NON_ROOT_GENE_MENTION: 279
- DECIDE_IF_EMBEDDED_CONCEPT_NEEDS_ROOT: 57
- ADD_MISSING_DISEASE_ROOT: 42
- BACKFILL_G2P_PMIDS_TO_MATCHED_ROOT: 32
- RECONCILE_SPECTRUM_ROW_ACROSS_MULTIPLE_ROOTS: 18
- KEEP_EXISTING_ROOT: 9

## Critical Genes: new dismech anchors needed (top 15)

| Gene | Priority | Actionable rows | Worst status | Primary action | Note |
| --- | --- | ---: | --- | --- | --- |
| DSP | CRITICAL | 7 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| FLNA | CRITICAL | 7 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| FGFR1 | CRITICAL | 5 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| PRPS1 | CRITICAL | 5 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| TGFBI | CRITICAL | 5 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| TP63 | CRITICAL | 5 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| ALDH18A1 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| ANK2 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| BEST1 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| COL11A2 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| CRB1 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| FOXE3 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| GJA1 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| KRT1 | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |
| MITF | CRITICAL | 4 | NO_DISMECH_MATCH | ADD_FIRST_GENE_DISEASE_ANCHOR | No dismech disease anchor currently represents this G2P row. |

## High-Priority Genes: split or underrepresented coverage (top 15)

| Gene | Priority | Actionable rows | Worst status | Primary action | Note |
| --- | --- | ---: | --- | --- | --- |
| FGFR3 | HIGH | 8 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| FGFR2 | HIGH | 6 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| GJB2 | HIGH | 6 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| OFD1 | HIGH | 4 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| ATP1A2 | HIGH | 3 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| FMR1 | HIGH | 3 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| PRPH2 | HIGH | 3 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| SDHB | HIGH | 3 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| SMARCB1 | HIGH | 2 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| ATM | HIGH | 2 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| CARD14 | HIGH | 2 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| GABRA1 | HIGH | 2 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| HNF4A | HIGH | 2 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| MYOC | HIGH | 2 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |
| NOTCH3 | HIGH | 2 | UNDERREPRESENTED_IN_DISMECH | ADD_MISSING_DISEASE_ROOT | dismech has some direct roots for the gene, but this disease row is still missing. |

## Medium-Priority Genes: embedded concepts or PMID backfill (top 15)

| Gene | Priority | Actionable rows | Worst status | Primary action | Note |
| --- | --- | ---: | --- | --- | --- |
| COL2A1 | MEDIUM | 6 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| KCNQ1 | MEDIUM | 5 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| RET | MEDIUM | 5 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| COL1A1 | MEDIUM | 4 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| FBN1 | MEDIUM | 4 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| KCNJ2 | MEDIUM | 4 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| LZTR1 | MEDIUM | 4 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| NKX2-5 | MEDIUM | 4 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| SCN5A | MEDIUM | 4 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| SOX10 | MEDIUM | 4 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| ATP7A | MEDIUM | 3 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| BRAF | MEDIUM | 3 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| CACNA1C | MEDIUM | 3 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| GNAS | MEDIUM | 3 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |
| LRP5 | MEDIUM | 3 | EMBEDDED_NOT_ROOTED | REVIEW_NON_ROOT_GENE_MENTION | Gene appears only in non-root mechanistic or secondary contexts. |

## Low-Priority Genes: existing roots already usable (top 9)

| Gene | Priority | Actionable rows | Worst status | Primary action | Note |
| --- | --- | ---: | --- | --- | --- |
| ARID1B | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Coffin_Siris_Syndrome.yaml already provides a usable direct disease root. |
| CFL2 | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Nemaline_Myopathy.yaml already provides a usable direct disease root. |
| CPLANE1 | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Joubert_syndrome.yaml already provides a usable direct disease root. |
| EHMT1 | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Kleefstra_Syndrome.yaml already provides a usable direct disease root. |
| GFAP | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Alexander_Disease.yaml already provides a usable direct disease root. |
| KDM6A | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Kabuki_Syndrome.yaml already provides a usable direct disease root. |
| P4HTM | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | HIDEA_Syndrome.yaml already provides a usable direct disease root. |
| RPGRIP1L | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Meckel_Syndrome.yaml already provides a usable direct disease root. |
| RPS19 | LOW | 0 | ROOT_MATCH | KEEP_EXISTING_ROOT | Diamond-Blackfan_Anemia.yaml already provides a usable direct disease root. |
