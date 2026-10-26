# ClinVar queries (NCBI E-utilities) — ABCC9 / CMD1O
# Endpoint: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar
# Accessed: 2026-10-24

| Label | ClinVar query term | Count |
|-------|--------------------|-------|
| ABCC9 total records | `ABCC9[gene]` | 2358 |
| ABCC9 + dilated cardiomyopathy condition | `ABCC9[gene] AND "dilated cardiomyopathy"[dis]` | 1671 |
| ABCC9 P/LP (any disease) | `ABCC9[gene] AND (pathogenic[clinsig] OR "likely pathogenic"[clinsig])` | 373 |
| ABCC9 + Cantu | `ABCC9[gene] AND Cantu[dis]` | 164 |
| ABCC9 P/LP for DCM condition | `ABCC9[gene] AND "dilated cardiomyopathy"[dis] AND (pathogenic[clinsig] OR "likely pathogenic"[clinsig])` | 205 |
| ABCC9 reviewed by expert panel | `ABCC9[gene] AND "reviewed by expert panel"[Review status]` | 0 |
| ABCC9 practice guideline | `ABCC9[gene] AND "practice guideline"[Review status]` | 0 |
| ABCC9 codon 1513 (CMD1O missense) | `ABCC9[gene] AND 1513` | 2 (VCV 856369, 8162) |
| ABCC9 codon 1524 (CMD1O frameshift) | `ABCC9[gene] AND 1524` | 1 (VCV 222477) |

Transcript reference: NM_020297.4
