# cBioPortal access log

- **Source:** cBioPortal public REST API — https://www.cbioportal.org/api
- **Study accession:** `hnsc_tcga_pan_can_atlas_2018` (TCGA Head & Neck SCC, PanCancer Atlas)
- **Access date:** 2026-09-13
- **Auth:** none (public); no controlled/patient-level data downloaded (only aggregate clinical attributes)
- **Preflight:** `GET /api/cancer-types?pageSize=2` → HTTP 200 (verified reachable from both sandbox and bundle-runner environments)
- **Endpoints used:**
  - `GET /api/studies/hnsc_tcga_pan_can_atlas_2018/clinical-data?clinicalDataType=SAMPLE&attributeId=FRACTION_GENOME_ALTERED&pageSize=10000`
  - `GET /api/studies/hnsc_tcga_pan_can_atlas_2018/clinical-data?clinicalDataType=SAMPLE&attributeId=MUTATION_COUNT&pageSize=10000`
  - `GET /api/studies/hnsc_tcga_pan_can_atlas_2018/clinical-data?clinicalDataType=PATIENT&attributeId=SUBTYPE&pageSize=10000`
- **Cohort/filter:** samples with non-null FGA, MUTATION_COUNT, and SUBTYPE; restricted to SUBTYPE ∈ {HNSC_HPV-, HNSC_HPV+}. Final n = 487 (415 HPV-negative, 72 HPV-positive).
- **Comparison:** Mann–Whitney U (two-sided), rank-biserial effect size, HPV-neg vs HPV-pos, for MUTATION_COUNT and FRACTION_GENOME_ALTERED.
- **Relevance caveat:** TCGA HNSCC is a SPORADIC cohort and contains NO Fanconi anemia tumors. Used only as the sporadic reference distribution against which the published FA-HNSCC molecular claim is interpreted. Does not directly test FA tumors.
- **Execution outcome:** SUCCEEDED (reproduced identically in sandbox and in the bundled script run).
- **Outputs:** `../data/tcga_hnsc_hpv_stats.json`, `../data/tcga_hnsc_hpv_summary.csv`, `../data/tcga_hnsc_hpv_persample.csv`, `../figures/tcga_hnsc_hpv_boxplots.png`
