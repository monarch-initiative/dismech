# Data access & search log — ASXL3 NMD-escape hypothesis

Retrieval date: 2026-09-05. Reference genome: GRCh38.

## Databases / APIs ACCESSED (resolved successfully)

### Ensembl REST (rest.ensembl.org)
- `GET /lookup/symbol/homo_sapiens/ASXL3?expand=1` → ENSG00000141431, 18 transcripts. **Resolved.**
- `GET /lookup/id/ENST00000269197?expand=1` → canonical (MANE) transcript, 12 exons, 2248-aa protein, CDS 33578632–33746595. **Resolved.**
- `GET /overlap/translation/ENSP00000269197` → Pfam domains (PF05066 HARE-HTH 10-84; PF13919 DEUBAD 240-360; PF13922 PHD 2204-2246). **Resolved.**
- Relevance: directly ASXL3; used for NMD-escape boundary + domain mapping.

### gnomAD GraphQL (gnomad.broadinstitute.org/api), dataset gnomad_r4
- `gene(ASXL3){gnomad_constraint}` → pLI=1, LOEUF=0.265, obs_lof=34, exp_lof=170.6, lof_z=8.87. **Resolved.**
- `transcript(ENST00000269197){clinvar_variants}` → 961 ClinVar variants (245 truncating). **Resolved.**
- `transcript(ENST00000269197){variants(dataset:gnomad_r4)}` → 7229 variants; 342 LOFTEE HC-LoF. **Resolved.**
- Relevance: directly ASXL3; used for constraint + positional clustering test.

## PubMed searches (via search_pubmed MCP)
- "ASXL3 Bainbridge-Ropers syndrome nonsense-mediated decay truncating variant" → 1 hit (PMID:26647312). USABLE.
- "ASXL3 genotype phenotype mutational cluster region autism spectrum" → 3 hits (42494517, 39833101, 28100473). USABLE.
- "ASXL1 gain of function BAP1" → 8 hits (incl. 26095772, 35122023, 34186160, 34536441, 42523271, 41925445). USABLE.
- "ASXL3 mouse model" → 6 hits (no dedicated Asxl3 neuro mouse model surfaced). PARTIAL.
- "Bohring-Opitz syndrome ASXL1 truncating gain of function" → 3 hits (26095772, 29037253, 42523271). USABLE.
- "Truncating ASXL1 ... Arboleda 2026" / "ASXL1 gain of function myeloid ... Balasubramani" / "Asxl3 mouse model neurodevelopment haploinsufficiency knockout" → 0 hits (query-term sensitivity of the endpoint; NOT evidence of absence). NEGATIVE (unverified absence).

## Negative / not-yet-checked sources (as of 2026-09-05)
- GenCC, ClinGen dosage curation: NOT queried programmatically this run (unverified).
- ClinicalTrials.gov: NOT queried (no expected interventional trial for BRS mechanism).
- Direct ASXL3 patient proteomics / Western blot of truncated protein: NOT found in searches (candidate real gap).
