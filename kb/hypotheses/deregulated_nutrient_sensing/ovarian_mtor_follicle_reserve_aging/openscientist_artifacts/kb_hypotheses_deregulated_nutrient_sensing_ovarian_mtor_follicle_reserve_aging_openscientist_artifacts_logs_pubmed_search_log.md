# PubMed Search Log — ovarian_mtor_follicle_reserve_aging

- Tool: MCP `search_pubmed` (NCBI E-utilities esearch/efetch backend)
- Operator: OpenScientist autonomous agent
- Search dates: 2026-10-18 (Iterations 1–3)
- Note: `max_results` caps returned records; counts below are records returned, not total PubMed hits.
- One transient failure recorded (HTTP 429 rate-limit) and retried.

| # | Iter | Query | Records returned | Used PMIDs |
|---|------|-------|------------------|------------|
| 1 | 1 | mTOR signaling ovarian aging primordial follicle reserve activation | 8 | 28544226, 31887337 (+context: 40244208, 34210610) |
| 2 | 1 | PTEN PI3K mTOR primordial follicle activation oocyte FOXO3 | 1 | 32808646 (review) |
| 3 | 1 | rapamycin ovarian reserve preservation follicle mice reproductive lifespan | ERROR 429 (rate-limited) | — |
| 4 | 1 | RICTOR mTORC2 ovary oocyte granulosa folliculogenesis | 0 | — |
| 5 | 1 | human ovarian aging single-nucleus multi-omics atlas mTOR cell type | 0 | — |
| 6 | 1 | single cell transcriptomic atlas human ovary aging | 6 | 39578560 context; 42772144, 42429048, 41243550 (competing) |
| 7 | 1 | rapamycin ovarian lifespan reproductive aging mice primordial follicle preservation | 2 | 28544226 |
| 8 | 1 | Rictor mTORC2 oocyte conditional knockout ovarian follicle fertility mouse | 1 | 25564616 |
| 9 | 1 | ovarian aging mechanism mitochondrial dysfunction oxidative stress oocyte quality decline | 6 | 42580602 (review), 42693473 (review), 42150485 (review) |
| 10| 1 | low-dose rapamycin women ovarian aging clinical trial reserve AMH | 0 | — (negative: no human trial result) |
| 11| 1 | rapamycin ovarian function women fertility trial | 3 | 38070496, 38927992 (review) |
| 12| 2 | oocyte Pten deletion primordial follicle activation premature depletion mouse Foxo3 knockout | 0 | — |
| 13| 2 | PTEN oocyte primordial follicle activation premature ovarian failure | 6 | 23326514, 25590233, 23677591, 26656301, 22761722 |
| 14| 2 | genome-wide association age at natural menopause DNA damage response repair genes | 6 | 26414677, 35493704, 24357391, 27513022, 27621233 |
| 15| 3 | Molecular genetic insights human ovarian aging single-nuclei multi-omics mTOR | 1 | 39578560 |
| 16| 3 | rapamycin ovarian reserve women pilot trial antimullerian hormone VIBRANT results | 0 | — (negative: no VIBRANT result in PubMed) |
| 17| 3 | sirolimus ovarian aging women reproductive function clinical study | 0 | — (negative: no human sirolimus ovarian-aging result) |
| 18| 3 | ovarian stroma fibrosis inflammation senescence aging multinucleated giant cells | 2 | 27491879, 42271623 |

## Negative-search statements (as of 2026-10-18, PubMed via MCP search_pubmed)
- No published results located for a human rapamycin/sirolimus ovarian-aging RCT (VIBRANT, ClinicalTrials.gov NCT05836025). Queries 10, 16, 17 returned no outcome papers. Status: registration-only. Label: verified-negative for the specific queries run; not exhaustive of all databases.
- No mTOR/nutrient-sensing locus surfaced as a primary signal in age-at-natural-menopause GWAS/exome results reviewed (queries 14). DDR dominates. Label: verified for the queries run; a dedicated lookup of the full GWAS Catalog menopause-timing locus list was NOT performed (see Data and Tool Use).
