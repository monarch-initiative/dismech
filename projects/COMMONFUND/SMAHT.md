# Somatic Mosaicism Across Human Tissues (SMaHT)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

SMaHT is directly mechanistic because it focuses on post-conception genomic
variation within tissues. The NIH Common Fund describes somatic mosaicism as
DNA changes that occur after conception and create genetic variation among cells
within one person. The SMaHT Network aims to catalog somatic variants across
human tissues, improve sequencing and analysis methods, and provide a data
workbench for studying somatic variation.

For dismech, SMaHT is the program that makes tissue distribution, variant
timing, clone size, and lineage context first-class parts of a disease
mechanism.

## Dismech Interpretation Pattern

Use SMaHT as a mosaic variant interpretation layer:

`postzygotic variant or chromosome-segregation error -> affected clone,
lineage, and tissue distribution -> pathway activation or loss of function ->
focal malformation, cancer risk, aging process, or tissue-restricted phenotype`

The key curation distinction is inherited variant versus somatic variant, and
bulk tissue signal versus cell-type or clone-resolved signal.

## Concrete Implementation Plan

**Mode:** teach mosaic-mechanism curation first, benchmark later. SMaHT should
teach dismech to record somatic variant timing, tissue distribution, clone
size, and lineage. It becomes a benchmark when dismech can distinguish normal
background mosaicism from disease-causing tissue-restricted clones.

**Required datasets and access path:**

- Use the SMaHT Data Portal: https://data.smaht.org/ and Network site:
  https://smaht.org/.
- Use the SMaHT data use policy:
  https://smaht.org/data-use-policy/. It describes a staged release model and
  expectations for data use, publication acknowledgement, and respecting file
  access restrictions.
- For each dataset, record portal accession, tissue, donor/sample type, assay,
  genome build, data processing status, access level, file type, and whether
  the dataset is a reference/background tissue atlas or disease-relevant.
- Start with public metadata and released variant-call or benchmark materials.
  Do not download or store controlled human sequence data in this repo.

**Tools and environment:**

- Portal search/API metadata harvesting with Python `requests` and `pandas`.
- For approved sequence analysis: `bcftools`, `samtools`, Mutect2, DeepVariant
  or SMaHT-recommended callers, mosaic variant filtering, VAF modeling, and
  tissue/cell-lineage annotation.
- Dismech representation needs explicit fields in notes for VAF, tissue,
  lesion status, assay sensitivity, and inherited versus postzygotic origin.

**Curation targets:**

- `CLOVES_Syndrome`, `Proteus_syndrome`,
  `Capillary_Malformation-Arteriovenous_Malformation_Syndrome`,
  `Encephalocraniocutaneous_Lipomatosis`, `Tuberous_Sclerosis_Complex`, and
  `Mosaic_Variegated_Aneuploidy_Syndrome`.
- New candidate modules/entries: clonal hematopoiesis, focal cortical dysplasia
  mosaic variants, and age-associated mosaicism only after disease relevance is
  established.
- Disease mechanism fields to curate: variant class, causal gene/pathway,
  affected lineage, lesion/tissue distribution, VAF range, clone behavior, and
  non-cell-autonomous effect if present.

**Code to write:**

- Add `src/dismech/commonfund/smaht.py` to harvest portal metadata and emit a
  manifest with assay, tissue, file access, sample type, variant-call product,
  and candidate disease link.
- Add `scripts/smaht_mosaicism_audit.py` to scan disease YAML for mosaicism
  language and require tissue, somatic/germline distinction, and mechanism
  direction.
- Add schema-review notes for somatic variant evidence: VAF, affected tissue,
  lineage, lesion status, assay sensitivity, and postzygotic timing.

**Graduate-student first pass:**

1. Start with `CLOVES_Syndrome` and `Proteus_syndrome`; list all current
   dismech nodes that mention somatic mosaicism or PI3K/AKT/mTOR activation.
2. Use SMaHT portal metadata to identify tissue/assay combinations suitable for
   background mosaicism and variant-detection benchmarking.
3. Write disease memos that separate reference/background tissue mosaicism from
   disease-specific lesion sequencing evidence.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How SMaHT helps |
|---------|--------------------------------|-----------------|
| `CLOVES_Syndrome` | Curated nodes: `Somatic Mosaicism`, `Constitutive PI3K Activation`, `AKT/mTOR Pathway Hyperactivation`, `Aberrant Vascular Development`, `Lipomatous Overgrowth`; treatment `Alpelisib` | This is the best SMaHT/dismech anchor: variant allele fraction and tissue distribution explain why the phenotype is focal and overgrowth-biased. |
| `Proteus_syndrome` | Curated nodes: `Somatic AKT1 p.E17K activation in mosaic cell clones`, `Elevated PI3K/AKT signaling in AKT1-mutant cells`, `AKT overactivation induces excessive vasculogenesis`, `Mural cell dysfunction destabilizes vascular connections` | SMaHT-style variant detection and clone mapping can clarify lesion-specific AKT activation and non-cell-autonomous effects. |
| `Capillary_Malformation-Arteriovenous_Malformation_Syndrome` | Curated nodes: `Germline RASA1 and EPHB4 loss of vascular Ras suppression`, `Somatic second-hit allele loss in focal lesions`, `RAS-MAPK/ERK-driven arteriovenous malformation formation` | Use SMaHT logic to represent second-hit tissue restriction and vascular-lesion mosaicism. |
| `Encephalocraniocutaneous_Lipomatosis` | Curated nodes: `Somatic mosaic`, `Somatic FGFR1 gain-of-function in developing tissues` | SMaHT can support developmental timing and affected lineage interpretation for neurocutaneous phenotypes. |
| `Tuberous_Sclerosis_Complex` | Curated mechanisms include first-hit/second-hit logic, `mTORC1 hyperactivation`, and hamartoma/tumor formation | SMaHT can refine when a second hit is lesion-restricted and how clone size relates to cortical tubers, renal angiomyolipomas, or other hamartomas. |
| `Mosaic_Variegated_Aneuploidy_Syndrome` | Curated nodes: `Mitotic checkpoint gene disruption`, `Spindle assembly checkpoint impairment`, `Chromosome segregation errors and mosaic aneuploidy`, `Growth and neurodevelopmental abnormalities`, `Cancer predisposition` | SMaHT can connect chromosome-level mosaicism to tissue burden, cancer predisposition, and developmental phenotypes. |
| Yet to curate: clonal hematopoiesis | Candidate mechanisms: age-associated somatic mutation -> hematopoietic clone expansion -> inflammatory bias, cardiovascular risk, or myeloid malignancy predisposition | SMaHT plus GTEx/HuBMAP can help separate normal aging mosaicism from disease-linked clone expansion. |
| Yet to curate: focal cortical dysplasia mosaic variants | Candidate mechanisms: somatic mTOR/RAS pathway variant -> dysmorphic neuron or glial clone -> cortical malformation -> epilepsy | Pair SMaHT with existing `Epilepsy` mechanisms such as `mTOR Pathway Hyperactivation`, `Dysmorphic Neuron Generation`, and `Network Hyperexcitability`. |

## High-Value Curation Work

- Add a reusable somatic mosaicism mechanism module with slots for variant
  timing, tissue, lineage, variant allele fraction, assay, and lesion evidence.
- Prioritize `CLOVES_Syndrome`, `Proteus_syndrome`,
  `Capillary_Malformation-Arteriovenous_Malformation_Syndrome`,
  `Encephalocraniocutaneous_Lipomatosis`, `Tuberous_Sclerosis_Complex`, and
  `Mosaic_Variegated_Aneuploidy_Syndrome`.
- Distinguish inherited predisposition plus somatic second hit from purely
  postzygotic disease.
- Treat SMaHT reference data as a background map unless a disease-specific
  study connects the variant or tissue clone to phenotype.

## Fit for RFA-RM-26-017

Best partner datasets:

- SMaHT + 4DN: somatic structural variation and chromatin consequences.
- SMaHT + HuBMAP/SenNet: tissue maps, aging, senescence, and clone context.
- SMaHT + Kids First/UDN: pediatric and rare mosaic disease interpretation.
- SMaHT + GTEx: tissue expression plausibility for affected genes.

## Sources

- NIH Common Fund SMaHT: https://commonfund.nih.gov/smaht
- SMaHT Network: https://smaht.org/
- SMaHT Data Portal: https://data.smaht.org/
- SMaHT data use policy: https://smaht.org/data-use-policy/
- SMaHT data portal docs: https://data.smaht.org/docs
