# Knockout Mouse Phenotyping Program (KOMP2)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

KOMP2 is mechanistically valuable because it provides standardized loss-of-gene
function phenotypes. The Common Fund page describes KOMP2 as collaborating with
the International Mouse Phenotyping Consortium to knock out and characterize
all protein-coding genes in the mouse genome, using uniform phenotyping
protocols and public data. It also notes a Kids First collaboration to develop
mouse strains for coding and noncoding variants identified from Kids First
datasets.

For dismech, KOMP2 is a model-organism support layer for gene function,
phenotype concordance, and candidate disease mechanisms.

## Dismech Interpretation Pattern

Use KOMP2 as conserved-function evidence:

`human candidate gene or variant -> mouse knockout phenotype -> mapped HPO or
organ-system phenotype -> candidate human disease mechanism -> SUPPORT or
PARTIAL model-organism evidence`

KOMP2 evidence should be clearly labeled as model organism evidence and should
not replace human clinical evidence.

## Concrete Implementation Plan

**Mode:** benchmark model-organism support. KOMP2/IMPC should test whether
dismech can use mouse phenotypes as conserved-function evidence without
overstating human disease causality.

**Required datasets and access path:**

- Use the IMPC portal: https://www.mousephenotype.org/ and KOMP2 Common Fund
  page: https://commonfund.nih.gov/KOMP2.
- Use IMPC programmatic data access:
  https://www.mousephenotype.org/help/programmatic-data-access/ and EBI
  training material on IMPC data downloads. IMPC supports website downloads,
  FTP bulk files, batch query, and API/Solr access.
- For each candidate gene, retrieve significant phenotype associations,
  underlying procedure/parameter if needed, zygosity, sex, life-stage, allele,
  and Mammalian Phenotype ontology terms.
- Use KOMP2/Kids First collaboration only where a specific Kids First candidate
  variant or gene has a corresponding mouse line or planned model.

**Tools and environment:**

- Python with `requests`, `pandas`, and optionally the `impc_api` helper
  package; R/Bioconductor IMPCdata if local analysis is R-based.
- Ontology crosswalk from MP to HPO/MONDO where available, with human
  phenotype mapping reviewed manually.
- Keep knockout directionality explicit. Loss-of-function mouse evidence is
  weak for human gain-of-function, dominant-negative, or dosage-sensitive
  mechanisms unless the biology supports it.

**Curation targets:**

- Rare disease validation: `Alport_Syndrome`, `Dravet_syndrome`,
  `Diamond-Blackfan_Anemia`, `Stargardt_Disease`, and selected Kids First/UDN
  candidate genes.
- Complex neurodevelopmental triage: `Autism_Spectrum_Disorder` gene subsets,
  marked as partial model evidence.
- Target biology: IDG understudied kinases, ion channels, and GPCRs with mouse
  phenotypes relevant to dismech mechanisms.

**Code to write:**

- Add `src/dismech/commonfund/komp2.py` with IMPC API/Solr helpers for gene,
  phenotype, disease association, and raw parameter lookup.
- Add `scripts/komp2_gene_evidence_audit.py` that accepts a dismech disease
  file or gene list and outputs gene, mouse phenotype, MP term, mapped HPO,
  concordance judgment, and caveat.
- Add a validation rule for any KOMP2-derived evidence item: evidence source
  must be model organism, and the explanation must state the human/mouse
  phenotype relationship.

**Graduate-student first pass:**

1. Choose 10 disease genes with existing dismech mechanisms and clear expected
   organ phenotypes.
2. Query IMPC for each gene, record significant MP terms, procedures, sex, and
   zygosity.
3. Mark each as concordant, discordant, or not interpretable for the human
   mechanism. Only concordant or instructive discordant cases should become
   disease-file notes.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How KOMP2 helps |
|---------|--------------------------------|-----------------|
| `Alport_Syndrome` | Curated nodes: `Defective Type IV Collagen Network`, `GBM Structural Deterioration`, `Podocyte Injury and Loss`, `Glomerulosclerosis`, `Tubulointerstitial Fibrosis` | Mouse knockout phenotypes can validate renal, ocular, and hearing components for collagen genes and modifiers. |
| `Dravet_syndrome` | Curated nodes: `SCN1A Gene Mutation`, `Neuronal Hyperexcitability`, `Astrocyte Dysregulation` | KOMP2/IMPC phenotypes for ion-channel or modifier genes can support seizure and neurodevelopmental mechanisms. |
| `Diamond-Blackfan_Anemia` | Curated nodes: `Ribosomal Protein Haploinsufficiency`, `p53-Mediated Erythroid Apoptosis`, `GATA1 Translational Insufficiency` | Knockout or haploinsufficiency phenotypes can support erythroid and developmental mechanisms for ribosomal genes. |
| `Autism_Spectrum_Disorder` | Curated nodes: `Excitatory/Inhibitory Imbalance`, `Synaptic Scaffolding Disruption`, `Chromatin Remodeling Disruption` | Mouse phenotypes can triage candidate neurodevelopmental genes, but must be handled as partial evidence. |
| `Cystic_Fibrosis` | Curated nodes: `CFTR Dysfunction`, `Airway Surface Liquid Depletion`, `Impaired Mucociliary Clearance`, `Chronic Bacterial Infection` | CFTR model phenotypes can support conserved ion transport biology while human evidence remains primary. |
| `Stargardt_Disease` | Curated nodes: `ABCA4 transporter dysfunction`, `Retinoid-adduct retention and bisretinoid precursor formation`, `Lipofuscin and A2E accumulation in RPE`, `Secondary macular photoreceptor degeneration` | Mouse phenotypes can support retinal degeneration mechanisms and modifier genes. |
| Kids First candidate genes | Candidate mechanism: pediatric variant -> gene loss or altered function -> mouse phenotype matching patient HPO profile -> dismech disease or new disorder | This is the clearest R03 cross-program use case. |

## High-Value Curation Work

- Add a KOMP2/IMPC evidence pattern for disease entries with candidate gene
  mechanisms: include gene, mouse phenotype, mapped human phenotype, and
  concordance caveat.
- Use KOMP2 especially for rare disease entries where human case counts are low
  and functional evidence is sparse.
- Pair KOMP2 with Kids First or UDN when interpreting new candidate variants.
- Avoid over-using knockout data for gain-of-function or dominant-negative
  human mechanisms unless the phenotype direction is biologically coherent.

## Fit for RFA-RM-26-017

Best partner datasets:

- KOMP2 + Kids First: pediatric variant function and phenotype support.
- KOMP2 + UDN: candidate gene validation for undiagnosed disorders.
- KOMP2 + IDG: phenotypes for understudied druggable target genes.
- KOMP2 + GTEx: model-organism phenotype plus human tissue-expression context.

## Sources

- NIH Common Fund KOMP2: https://commonfund.nih.gov/KOMP2
- IMPC portal: https://www.mousephenotype.org/
- IMPC programmatic data access: https://www.mousephenotype.org/help/programmatic-data-access/
- EBI IMPC data downloads tutorial: https://www.ebi.ac.uk/training/online/courses/international-mouse-phenotyping-consortium/data-downloads/
- KOMP2 program resources: https://commonfund.nih.gov/KOMP2/program-resources
