# Search & Query Log — Weaver Syndrome / dominant_negative_prc2

All timestamps: search date 2026-09-05 (agent "current date").

## PubMed (NCBI E-utilities, db=pubmed)
| Query | Result summary |
|-------|----------------|
| `Weaver syndrome EZH2 dominant-negative PRC2` | 1 hit → PMID:40846643 (seed paper) |
| `EZH2 mutations Weaver syndrome overgrowth` | PMIDs 40922349, 40846643, 38814056, 32243864, 31736240, 31724824 |
| `EZH2 Weaver syndrome loss of function haploinsufficiency` | PMIDs 28696078, 23592277 |
| `EZH2 gain of function lymphoma Y641 H3K27me3` | PMIDs 36858198, 25253781, 24469040, 21190999 |
| `EED Cohen-Gibson syndrome overgrowth PRC2` | PMIDs 40539649, 37840385, 36645289, 34533271, 31736240, 31724824 |
| `PRC2 EZH2 dominant negative mechanism` | PMIDs 40846643, 39988873, 36110328, 31840280, 25115397 |
| `EZH2 gain of function microcephaly growth restriction germline` | **0 primary clinical hits** (negative result — reciprocal GoF growth-restriction syndrome not independently reported) |
| `EZH2 Weaver syndrome mouse model H3K27me3` | PMIDs 38015625, 37425751, 30005706 |
| `PRC2 dominant negative EED SUZ12 assembly incorporation` | 0 hits |
| `Tatton-Brown Weaver EZH2 germline mutations overgrowth 2011` | PMID:22190405 (original discovery) |

Full abstracts retrieved via efetch for: 40846643, 21190999, 32243864, 31724824,
28696078, 40922349, 38015625, 22190405, 30005706.

## ClinVar (NCBI E-utilities, db=clinvar)
- Query: `EZH2[gene]` → 821 variation records (esearch count).
- Filter: germline classification contains "athogenic" AND NOT "Conflicting" → 46 parseable single P/LP variants.
- Subset: trait set contains "Weaver" → 27 variants.
- Molecular-consequence tally (Weaver-annotated P/LP): missense 21; nonsense 2;
  frameshift 1; in-frame indel 2; noncoding/other 1.
- Truncating variants (nonsense+frameshift): p.Asp730Ter, p.Tyr733Ter, p.Ala738fs
  (codons 730/733/738 of 746; all downstream of SET domain end 727).
- Output tables: data/ezh2_clinvar_weaver_plp.csv, data/ezh2_variant_class_summary.csv

## gnomAD (GraphQL API, https://gnomad.broadinstitute.org/api)
- Gene EZH2 (ENSG00000106462), GRCh38, gnomad_constraint.
- Result: pLI=1.0, o/e LoF=0.183 (18 obs / 98.4 exp), LOEUF(upper)=0.271,
  lof_z=6.88, mis_z=6.49. Saved: data/gnomad_ezh2_constraint.json
- Note: gnomAD dataset version returned by the default endpoint was not explicitly
  captured in the query; treat as "current default gnomAD constraint as of 2026-09-05".

## Databases checked but NOT accessed / not queried (declared for transparency)
- GenCC, ClinGen gene-disease/dosage: NOT queried in this run (unverified — no absence claim).
- ClinicalTrials.gov: NOT queried (no trial-based claims made).
- GEO/omics repositories: NOT queried; the seed paper's RNA-seq/ChIP-seq raw data
  accession was not retrieved (external; see knowledge gaps).
