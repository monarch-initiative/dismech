# 4D Nucleome (4DN)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

4DN is directly mechanistic because it measures how genome organization changes
gene regulation. Its most useful dismech role is to connect noncoding variants,
chromatin boundary disruption, enhancer rewiring, nuclear body disruption, and
epigenomic state changes to downstream disease processes.

The Common Fund page describes 4DN as a program to study three-dimensional
nuclear organization in space and time, how nuclear organization controls gene
expression and cellular function, and how changes affect development and
disease. The program has produced public 4DN Portal datasets, software,
protocols, and reagents.

## Dismech Interpretation Pattern

Use 4DN data as an upstream regulatory-mechanism layer:

`structural variant or chromatin-state perturbation -> altered nuclear contact,
boundary, compartment, or nuclear body -> altered gene expression -> cell-state
or developmental process -> disease phenotype`

This is strongest where ordinary gene lists under-explain the disease because
the causal signal is regulatory, positional, enhancer-mediated, or
chromatin-architecture mediated.

## Concrete Implementation Plan

**Mode:** benchmark first, teach selectively. 4DN is best used to benchmark
whether dismech can interpret regulatory architecture in a disease mechanism.
It should teach new disease mechanisms only when the dataset is disease-matched
or a defensible experimental perturbation is paired with disease literature.

**Required datasets and access path:**

- Use human/proximal datasets first for `CTCF-related_Neurodevelopmental_Disorder`:
  H1 CTCF ChIA-PET, HG00731 CTCF HiChIP, and HAP-1 engineered CTCF-site
  deletion Capture Hi-C.
- Use CTCF-AID mouse ESC only as an optional workflow positive control for
  acute CTCF depletion and insulation loss. It should not be curated as direct
  disease evidence.
- Use portal processed files and `metadata.tsv` manifests, then record
  experiment-set accession, processed-file accession, genome build, biosource,
  assay, condition, file type, and portal URL.

**Tools and environment:** use the portal, HiGlass, and 4DN JupyterHub for
first-pass inspection; use Python `cooler`, `cooltools`, `bioframe`, `pandas`,
and `dcicutils` for local quantitative checks. Details are in the tooling
section below.

**Code to write:**

- Add `src/dismech/commonfund/fourdn.py` with helpers for portal metadata
  search, processed-file manifest export, and accession-to-dataset draft
  records.
- Add `scripts/fourdn_locus_mechanism_audit.py` that accepts disease, locus,
  gene, and candidate mechanism; retrieves selected `.mcool`/metadata records;
  and produces boundary/loop/compartment summary rows for curation review.
- Add schema-review notes for `HI_C`, `CHIA_PET`, `HICHIP`,
  `CHROMATIN_CONFORMATION`, `CHROMATIN_TRACING`, `MICROSCOPY`, genome build,
  and processed-file provenance.

**Curation targets:**

- `CTCF-related_Neurodevelopmental_Disorder` for boundary insulation and CTCF
  loop support around candidate regulatory loci.
- Pediatric and chromatin-driven cancers where structural variation,
  enhancer adoption, SWI/SNF loss, PRC2/H3K27 alteration, or nuclear-body
  disruption changes transcriptional state.
- A reusable regulatory-architecture pattern:
  boundary/contact/compartment change -> target gene dysregulation -> cell-state
  or developmental phenotype.

**Graduate-student first pass:** follow the playbook below. The critical rule
is to write the disease mechanism chain before looking at Hi-C tracks, then use
4DN to test a specific boundary, loop, enhancer-promoter contact, or
compartment hypothesis.

## Practical Data Access

Start with already processed files, not raw FASTQs. The useful first pass for
dismech is to ask whether a disease-relevant locus, gene, enhancer, or boundary
has altered 3D context in a matched or defensible proxy cell type.

Key URLs:

- Main 4DN Data Portal: https://data.4dnucleome.org/
- Browse all replicate experiment sets:
  https://data.4dnucleome.org/browse/?experimentset_type=replicate&type=ExperimentSetReplicate
- Hi-C datasets and studies: https://data.4dnucleome.org/hic-data-overview
- Microscopy data overview: https://data.4dnucleome.org/microscopy-data-overview
- Chromatin tracing collection:
  https://data.4dnucleome.org/resources/data-collections/chromatin-tracing-datasets
- 4DN Visualization Workspace / HiGlass:
  https://data.4dnucleome.org/tools/visualization
- 4DN JupyterHub: https://data.4dnucleome.org/tools/jupyterhub
- Programmatic access guide:
  https://data.4dnucleome.org/help/user-guide/programmatic-access
- Downloading files guide:
  https://data.4dnucleome.org/help/user-guide/downloading-files
- Metadata schemas: https://data.4dnucleome.org/profiles/

Access model:

- The portal states that 4DN Network data are made freely available to the
  scientific community, with citation and data-generating-lab acknowledgement
  expectations.
- File downloads from the portal require a free portal account and access key,
  even for public files.
- Most released files that are not the newest releases can also be downloaded
  unauthenticated through the AWS Open Data bucket when the portal-provided
  `metadata.tsv` has an `open_data_url` column value.
- Some data can be restricted to the 4DN Network or individual labs; JupyterHub
  and DRS access respect the user's authentication and authorization.
- For microscopy, many datasets expose processed files but not raw images; the
  portal notes that raw images may need to be requested from the generating lab.

Example 4DN records worth inspecting for dismech pilots:

- HAP-1 engineered CTCF-site deletion Capture Hi-C:
  https://data.4dnucleome.org/experiment-set-replicates/4DNES3CUDIXW/
- CTCF ChIA-PET in H1:
  https://data.4dnucleome.org/experiment-set-replicates/4DNESR9S8R38/
- CTCF HiChIP on HG00731:
  https://data.4dnucleome.org/experiment-set-replicates/4DNESOAF3QAA/
- CTCF/cohesin chromatin tracing publication:
  https://data.4dnucleome.org/A_Hafner_mESC_loop_stacking_chromatin_tracing
- Chromatin tracing of single chromosomes:
  https://data.4dnucleome.org/publications/e6451832-8312-4e74-bd74-742801f726e1/

CTCF-AID mouse ESC records are useful only as optional positive-control
perturbation data, not as disease evidence:

- CTCF-AID mouse ESC Hi-C:
  https://data.4dnucleome.org/browse/?dataset_label=Hi-C+on+CTCF-AID+tagged+mESCs&experimentset_type=replicate&type=ExperimentSetReplicate
- CTCF-AID auxin depletion experiment:
  https://data.4dnucleome.org/experiments-hi-c/4DNEX4DOY175/

## Practical Tooling and Environment

Minimum practical environment:

- A laptop is enough for metadata review, HiGlass inspection, and small-region
  analysis from `.mcool` files.
- For chromosome-scale or genome-scale Hi-C analysis, use a workstation or
  cloud VM with at least 32-64 GB RAM and enough disk for multi-GB `.mcool`,
  `.pairs.gz`, bigWig, and BED files.
- Use the 4DN JupyterHub first if the goal is fast exploration without moving
  large files.

Recommended tools:

- Portal UI and HiGlass for first-pass visual inspection and figure-quality
  screenshots.
- Python: `requests`, `pandas`, `cooler`, `cooltools`, `bioframe`, `pybedtools`
  or equivalent interval tooling, plus `dcicutils` for 4DN metadata access.
- R/Bioconductor: `fourDNData`, `HiCExperiment`, `GenomicRanges`,
  `InteractionSet`, and `rtracklayer` for programmatic access to uniformly
  processed 4DN Hi-C matrices.
- Command line: `curl` with 4DN key/secret for authenticated downloads, AWS CLI
  for open-data S3 URLs, `pairtools` for `.pairs` files, and `cooler` for
  `.cool`/`.mcool` inspection.
- Optional heavy processing: 4DN Hi-C pipeline Docker containers or Open2C-style
  pipelines if raw FASTQs must be reprocessed. Avoid this for a first R03 pilot
  unless the scientific question truly requires raw read reprocessing.

Useful derived quantities:

- Contact maps and differential local contact enrichment.
- Insulation score and TAD or boundary strength.
- Compartment eigenvectors and A/B compartment shifts.
- Loop or dot calls.
- Pileups around CTCF sites, enhancers, promoters, or structural variant
  breakpoints.
- Co-visualization with CTCF/cohesin ChIP/CUT&Tag, ATAC-seq, RNA-seq, and
  disease-relevant genes.

## Graduate Student Playbook

Give a smart bioinformatics graduate student a narrow, locus-driven question:

1. Choose one disease and one plausible 4DN mechanism. For example:
   `CTCF-related_Neurodevelopmental_Disorder` and boundary insulation, or
   enhancer hijacking in a pediatric cancer.
2. Write down the mechanism as a testable chain:
   `variant or perturbation -> contact/boundary/loop change -> target gene
   expression change -> disease-relevant cell process`.
3. Pick a tissue or cell proxy before touching data. For CTCF-related human
   disease, start with human CTCF ChIA-PET, CTCF HiChIP, or engineered human
   CTCF-site deletion data when possible. Use CTCF-AID mouse ESC only as an
   optional positive-control perturbation showing what acute CTCF loss does to
   genome folding; do not treat it as patient or disease evidence.
4. Use the portal's Browse page to find released experiment sets and download
   the `metadata.tsv`. Record accession, organism, biosource, assay, condition,
   processed file accession, file type, genome build, and source publication.
5. In HiGlass, inspect the disease locus at two scales: local 100 kb-2 Mb and
   regional 2-20 Mb. Save URLs or screenshots only after noting resolution,
   sample, and file accession.
6. Download one processed `.mcool` file and one matched control, if available.
   Avoid raw FASTQs initially.
7. Compute one simple quantitative readout:
   insulation around a boundary, observed/expected contact change across a
   candidate enhancer-promoter pair, compartment eigenvector sign/strength, or
   pileup around a class of loci.
8. Integrate one orthogonal layer if available: CTCF/cohesin binding, ATAC-seq,
   RNA-seq, or disease-gene expression. Do not interpret a contact shift alone
   as a disease mechanism.
9. Produce a one-page curation memo:
   disease, candidate mechanism node, 4DN accession(s), file type, cell proxy,
   exact locus, result direction, caveat, and proposed dismech update.
10. Stop if the tissue proxy is indefensible, the locus is not covered at useful
    resolution, or the result cannot be connected to a named disease mechanism.

Concrete first assignment:

- Start with `CTCF-related_Neurodevelopmental_Disorder`.
- Use human 4DN data first: H1 CTCF ChIA-PET, HG00731 CTCF HiChIP, and/or
  HAP-1 engineered CTCF-site deletion Capture Hi-C.
- Choose 3-5 CTCF-related disease genes or patient-relevant candidate loci.
- Ask a concrete question: do these genes sit near strong CTCF/cohesin loops,
  domain boundaries, or enhancer-promoter contacts in human data?
- Quantify one readout per locus: boundary insulation, loop support,
  enhancer-promoter contact, or local contact change in the engineered deletion
  dataset if the locus is relevant.
- Pair the 4DN result with GTEx or disease literature so the contact feature is
  connected to gene expression or neurodevelopmental biology.
- Write a dismech-facing memo that is explicit about evidence level:
  4DN reference or engineered-cell evidence can support the plausibility of
  `CTCF haploinsufficiency -> chromatin architecture disruption ->
  neurodevelopmental gene dysregulation`, but it is not direct patient evidence
  unless a disease-specific human study is added.

Optional positive-control task:

- Reproduce an acute CTCF depletion signal in CTCF-AID mouse ESC data only to
  confirm the analysis workflow can detect insulation loss. Keep this out of
  the main disease claim except as a method sanity check.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How 4DN helps |
|---------|--------------------------------|---------------|
| `CTCF-related_Neurodevelopmental_Disorder` | Curated nodes: `CTCF Haploinsufficiency`, `Chromatin Architecture Disruption`, `Neurodevelopmental Gene Dysregulation`, `Abnormal Neural Progenitor Cell Development` | This is the cleanest 4DN/dismech pilot. 4DN contacts and insulation data can turn the existing CTCF mechanism into a measurable boundary-disruption model. |
| `Facioscapulohumeral_Muscular_Dystrophy` | Curated nodes: `D4Z4 Epigenetic Derepression`, `DUX4 Misexpression in Skeletal Muscle`, `Progressive Myofiber Loss and Fatty Replacement` | Add nuclear organization and chromatin accessibility context around D4Z4 derepression and permissive 4qA haplotypes. |
| `H3_K27_Altered_Diffuse_Midline_Glioma` | Curated nodes: `H3 K27M Oncohistone Mutation`, `PRC2 Complex Inhibition and H3K27me3 Loss`, `Epigenetic Derepression and Aberrant Gene Activation`, `Loss of Glial Differentiation` | 4DN can provide enhancer/compartment context for how global H3K27me3 loss creates tumor subtype-specific transcriptional programs. |
| `Atypical_Teratoid_Rhabdoid_Tumor` | Curated nodes: `SMARCB1 or SMARCA4 Inactivation`, `SWI/SNF Chromatin Remodeling Defect`, `Subtype-Specific Enhancer Dysregulation` | Strong pediatric cancer use case: map SWI/SNF loss to enhancer rewiring and subgroup identity. |
| `APL_PML_RARA` | Curated nodes: `PML-RARA Fusion Oncogene Formation`, `Transcriptional Repression of Differentiation Genes`, `PML Nuclear Body Disruption` | 4DN can add nuclear body and chromatin-loop context to the existing transcriptional repression and PML nuclear body mechanisms. |
| `Medulloblastoma_WNT_Activated` | Curated nodes: `WNT/Beta-Catenin Pathway Activation`, `Nuclear Beta-Catenin Accumulation`, `WNT Target Gene Activation` | Candidate addition: enhancer-promoter and chromatin-state signatures that distinguish WNT tumors from SHH, Group 3, and Group 4 medulloblastoma. |
| Yet to curate: enhancer hijacking cancers | Candidate mechanisms: structural variant -> oncogene enhancer adoption -> transcriptional activation -> lineage-inappropriate proliferation | 4DN is a natural evidence source for looping-driven oncogene activation in cancers not yet represented as specific dismech entries. |

## High-Value Curation Work

- Add `datasets` to `CTCF-related_Neurodevelopmental_Disorder`,
  `Facioscapulohumeral_Muscular_Dystrophy`, `H3_K27_Altered_Diffuse_Midline_Glioma`,
  `Atypical_Teratoid_Rhabdoid_Tumor`, and `APL_PML_RARA` for relevant 4DN
  experiments or portal collections.
- Add a reusable mechanism pattern for regulatory architecture:
  `chromatin boundary disruption -> target gene dysregulation -> developmental
  or cancer cell-state defect`.
- Backfill mechanism nodes with GO terms for chromatin organization, chromatin
  remodeling, regulation of transcription by RNA polymerase II, and nuclear body
  organization where current entries are underspecified.
- Treat 4DN as supporting evidence for mechanism interpretation, not as direct
  clinical evidence unless a study explicitly links the architecture to human
  disease samples.

## Fit for RFA-RM-26-017

Best partner datasets:

- 4DN + GTEx: regulatory contact plus tissue expression/eQTL interpretation.
- 4DN + HuBMAP: spatial cell context plus nuclear organization.
- 4DN + Kids First: structural variants or pediatric cancer regulatory rewiring.
- 4DN + SMaHT: somatic structural variation plus tissue-specific chromatin
  consequences.

## Sources

- NIH Common Fund 4DN: https://commonfund.nih.gov/4dnucleome
- 4DN Data Portal: https://data.4dnucleome.org/
- 4DN health relevance: https://commonfund.nih.gov/4DNucleome/health-relevance
- 4DN Hi-C datasets: https://data.4dnucleome.org/hic-data-overview
- 4DN microscopy datasets: https://data.4dnucleome.org/microscopy-data-overview
- 4DN chromatin tracing datasets: https://data.4dnucleome.org/resources/data-collections/chromatin-tracing-datasets
- 4DN programmatic access: https://data.4dnucleome.org/help/user-guide/programmatic-access
- 4DN downloading files: https://data.4dnucleome.org/help/user-guide/downloading-files
- 4DN visualization workspace: https://data.4dnucleome.org/tools/visualization
- 4DN JupyterHub: https://data.4dnucleome.org/tools/jupyterhub
- Bioconductor fourDNData: https://www.bioconductor.org/packages/release/data/experiment/html/fourDNData.html
- Orchestrating Hi-C Analysis with Bioconductor, 4DN chapter: https://bioconductor.org/books/3.22/OHCA/pages/disseminating.html
