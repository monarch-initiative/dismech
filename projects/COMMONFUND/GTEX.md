# Genotype-Tissue Expression (GTEx)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

GTEx is a normal-tissue reference for gene expression and regulatory variation.
The Common Fund page describes GTEx as a data resource and tissue bank for
studying relationships between inherited genetic variants and gene expression in
multiple human tissues and across individuals. It notes a tissue biospecimen
biobank from about 960 donors and use of GTEx for functional interpretation of
GWAS findings and disease-relevant gene identification.

For dismech, GTEx helps answer whether a disease-gene hypothesis is plausible
in the affected tissue and whether a noncoding variant likely changes
expression of the right gene in the right tissue.

## Dismech Interpretation Pattern

Use GTEx as a regulatory plausibility layer:

`variant or GWAS locus -> eQTL or tissue-expression pattern -> affected gene in
relevant tissue -> biological process node -> phenotype or disease risk`

GTEx is usually supporting evidence, not direct disease evidence, because it is
mostly normal-tissue data.

## Concrete Implementation Plan

**Mode:** benchmark dismech interpretation. GTEx should usually be used to test
whether dismech places genes and regulatory variants in the right tissue
context, not to teach disease causality by itself.

**Required datasets and access path:**

- Use GTEx Portal datasets and documentation:
  https://gtexportal.org/home/datasets,
  https://gtexportal.org/home/documentationPage, and
  https://gtexportal.org/home/api-docs/index.html.
- Use open GTEx analysis files for expression matrices, tissue summaries, and
  eQTL/sQTL release files. Record the exact analysis release in every dismech
  note; do not write "GTEx" without version context.
- Use protected GTEx raw sequence, genotype, and individual-level attributes
  only through approved dbGaP/AnVIL access. The protected-access page identifies
  dbGaP accession `phs000424`; those files should not be stored in this repo.
- For single-cell GTEx, use the portal single-cell overview and gene-level
  visualizations as tissue/cell-type support, then cite the relevant GTEx
  release and publication.

**Tools and environment:**

- Python/R with `pandas`, `pyarrow`, `duckdb`, `tabix`, and `pyranges` or
  Bioconductor GenomicRanges for genomic intervals.
- GTEx Portal API for small queries; bulk release files for reproducible
  disease-gene audits.
- Fine-mapping/colocalization tools such as coloc or susie only when a specific
  GWAS/eQTL pairing is being analyzed; otherwise keep GTEx as expression
  plausibility evidence.

**Curation targets:**

- `Idiopathic_Pulmonary_Fibrosis`: MUC5B and lung epithelial plausibility.
- `Coronary_Artery_Disease`: liver, artery, adipose, and blood expression
  context for lipid, endothelial, and inflammatory genes.
- `Type_2_Diabetes_Mellitus`: pancreas, liver, adipose, skeletal muscle, and
  blood expression/eQTL context for TCF7L2, PPARG, KCNJ11, and SLC30A8.
- `Atrial_Fibrillation` and `Hypertrophic_Cardiomyopathy`: heart tissue
  expression and modifier-gene interpretation.
- `CTCF-related_Neurodevelopmental_Disorder`: GTEx can support adult tissue
  expression context, but developmental brain mechanisms need independent
  developmental or 4DN-like evidence.

**Code to write:**

- Add `src/dismech/commonfund/gtex.py` with functions for gene-by-tissue
  expression lookup, eQTL lookup by variant/gene/tissue, and a tissue
  plausibility report for dismech disease-gene pairs.
- Add `scripts/gtex_disease_gene_audit.py` to emit a table:
  disease, gene, mechanism node, expected tissue, GTEx expression support,
  eQTL support, release, and caveat.
- Add schema-review notes for dataset version, access class, tissue summary
  files, and `EQTL`/`SQTL` as dataset or finding subtypes.

**Graduate-student first pass:**

1. Pick 25 disease-gene pairs already curated in dismech.
2. For each, choose the biologically expected tissue before opening GTEx.
3. Query GTEx expression and, where relevant, eQTLs. Mark each as supports
   tissue plausibility, argues against the proposed tissue, or is uninformative.
4. Update dismech only with conservative notes: GTEx supports expression or
   regulatory plausibility, not disease causality.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How GTEx helps |
|---------|--------------------------------|----------------|
| `Idiopathic_Pulmonary_Fibrosis` | Curated nodes: `Repetitive alveolar epithelial injury and aberrant repair`, `Profibrotic macrophage recruitment and amplification`, `Fibroblast activation and myofibroblast differentiation`; genetic factor `MUC5B` | Use GTEx lung expression/eQTL context to interpret regulatory risk alleles and epithelial injury mechanisms. |
| `Coronary_Artery_Disease` | Curated nodes: `Atherosclerotic Plaque Formation`, `Endothelial Dysfunction`, `Plaque Rupture and Thrombosis`; genes include `LDLR`, `PCSK9`, `APOE`, `9p21 Locus` | Use GTEx arterial, liver, adipose, and blood expression to connect risk loci to lipid handling, endothelial biology, and inflammation. |
| `Type_2_Diabetes_Mellitus` | Curated nodes: `Insulin Resistance`, `Beta Cell Dysfunction`, `Hepatic Glucose Overproduction`, `Mitochondrial Dysfunction and Oxidative Stress`; genes include `TCF7L2`, `PPARG`, `KCNJ11`, `SLC30A8` | Use pancreas, liver, adipose, muscle, and blood expression/eQTL evidence to prioritize mechanism placement. |
| `Atrial_Fibrillation` | Curated nodes: `Atrial Electrical Remodeling`, `Atrial Structural Remodeling`, `Pulmonary Vein Triggers`; genes include `PITX2`, `SCN5A`, `KCNQ1` | GTEx can support whether candidate genes are expressed in heart tissues or relevant autonomic/vascular tissues. |
| `Hypertrophic_Cardiomyopathy` | Curated nodes: `Sarcomere Protein Mutations`, `Myocyte Disarray`, `Myocardial Fibrosis`, `Altered Calcium Handling`, `Mitochondrial Dysfunction` | Use heart tissue expression to interpret sarcomere, calcium handling, and mitochondrial modifier genes. |
| `Alpha_1_Antitrypsin_Deficiency` | Current disease file exists | Candidate GTEx use: SERPINA1 expression in liver and lung to frame hepatic protein misfolding and pulmonary protease-antiprotease imbalance. |
| `CTCF-related_Neurodevelopmental_Disorder` | Curated nodes: `CTCF Haploinsufficiency`, `Chromatin Architecture Disruption`, `Neurodevelopmental Gene Dysregulation` | GTEx complements 4DN by adding tissue expression context for CTCF and target genes, though brain developmental timing will remain a limitation. |

## High-Value Curation Work

- Add GTEx as a standard `datasets` reference when a dismech entry uses a
  regulatory variant, GWAS locus, or noncoding risk allele as mechanism support.
- Add a curation note pattern: "GTEx supports tissue-expression plausibility;
  disease causality requires independent genetic or functional evidence."
- Prioritize entries with known GWAS/eQTL ambiguity: `Coronary_Artery_Disease`,
  `Type_2_Diabetes_Mellitus`, `Idiopathic_Pulmonary_Fibrosis`,
  `Atrial_Fibrillation`, and `Inflammatory_Bowel_Disease` entries.
- Build a small export table of dismech disease -> gene -> affected tissue ->
  GTEx expression/eQTL support -> mechanism node.

## Fit for RFA-RM-26-017

Best partner datasets:

- GTEx + 4DN: expression/eQTL plus chromatin contact interpretation.
- GTEx + HuBMAP: bulk tissue expression plus single-cell/spatial tissue maps.
- GTEx + Kids First/UDN: candidate rare variant tissue plausibility.
- GTEx + SMaHT: tissue-specific expression plus somatic variant interpretation.

## Sources

- NIH Common Fund GTEx: https://commonfund.nih.gov/GTEx
- GTEx datasets: https://gtexportal.org/home/datasets
- GTEx Portal documentation: https://gtexportal.org/home/documentationPage
- GTEx protected access: https://gtexportal.org/home/protectedDataAccess
- GTEx API docs: https://gtexportal.org/home/api-docs/index.html
- GTEx publications: https://commonfund.nih.gov/GTEx/publications
