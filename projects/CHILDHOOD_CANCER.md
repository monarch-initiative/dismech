# Childhood Cancer / CCDI Alignment Project

## Overview

Explore how dismech can contribute to the childhood / pediatric / AYA cancer
data ecosystem, with a focus on structured disease mechanism curation for
pediatric malignancies and direct alignment with the NCI Childhood Cancer Data
Initiative (CCDI).

The core opportunity is to use dismech as an interpretive layer on top of
cohort-scale pediatric molecular characterization. CCDI and the Molecular
Characterization Initiative (MCI) generate large volumes of WES, fusion,
methylation, pathology, and multimodal research data; dismech can explain how
those alterations connect to pathways, cell states, histopathology, phenotypes,
and treatment response through evidence-backed mechanism graphs.

This is a strong fit for the current repo. dismech already contains multiple
pediatric tumors and predisposition syndromes, and the schema already supports
`genetic`, `pathophysiology`, `histopathology`, `datasets`, and
`clinical_trials`. The main question is where to focus curation so it becomes
maximally useful for CCDI, MCI, and the upcoming pediatric / AYA rare cancer
efforts.

## The CCDI Pediatric Cancer Landscape

| Component | Current role / scale | Why it matters for dismech |
|-----------|----------------------|----------------------------|
| **Molecular Characterization Initiative (MCI)** | NCI + COG Project:EveryChild partnership providing diagnosis-time molecular characterization at no cost, with WES, fusions, and methylation returned within 21 days; approximately 9,000 children / AYAs enrolled; MCI was the second most downloaded dataset in the GDC in January 2026 (592 TB) | Mechanism graphs can interpret driver variants, fusion events, subtype-defining methylation calls, and downstream pathway activation |
| **CCDI Data Ecosystem** | Coordinated network centered on CCDI Hub, with 40+ multimodal studies and links across COG, Kids First, SEER, PBTC, HCMI, PPCR, St. Jude Cloud, Treehouse, PedcBioPortal, OncoGenomics, TARGET, FusOnc2, Foundation Medicine, and more | dismech can provide disease-centric normalization and explanation across heterogeneous pediatric resources |
| **Pediatric / AYA Rare Cancer Study** | Upcoming longitudinal observational study for children and AYAs with very rare cancers | Rare disease mechanism curation is already a dismech strength; this is a direct pediatric rare-cancer use case |
| **Federal AI push for childhood cancer** | Executive order directs HHS to use AI for childhood cancer research and treatment; CCDI budget increased from $50M/year to $100M/year | dismech aligns with AI-ready extraction, harmonization, validation, and multimodal integration priorities |
| **RADIANCE** | Pipeline converting MCI whole-slide pathology images into AI-ready searchable embeddings via patch extraction, foundation models, and vector storage | dismech histopathology and mechanism nodes could act as the explanatory layer for morphology-genomics correlation |

## Existing dismech coverage

### Confirmed pediatric / AYA malignancy coverage already in the KB

| Area | Current entries |
|------|-----------------|
| Embryonal and pediatric solid tumors | Neuroblastoma, Retinoblastoma, Wilms Tumor |
| Pediatric CNS tumors | Medulloblastoma SHH-Activated, Medulloblastoma WNT-Activated, H3 K27-Altered Diffuse Midline Glioma, Rhabdoid Tumor |
| Pediatric / AYA sarcomas | Alveolar Rhabdomyosarcoma, Embryonal Rhabdomyosarcoma, Ewing Sarcoma, Osteosarcoma, Synovial Sarcoma, Clear Cell Sarcoma, Desmoplastic Small Round Cell Tumor |
| Pediatric / AYA hematologic slice | Ph Positive ALL, Burkitt Lymphoma |
| Predisposition and overlap syndromes | Li-Fraumeni Syndrome, Neurofibromatosis Type 1, Fanconi Anemia, Gorlin Syndrome, SUFU-related Nevoid Basal Cell Carcinoma Syndrome |

This is already enough to support a credible pediatric pilot. dismech has
coverage of multiple tumors with clear driver events or subgroup biology,
including RB1 loss, MYCN amplification, WT1 / CTNNB1 pathways, EWSR1 fusions,
PAX3 / PAX7-FOXO1 fusions, BCR-ABL1, and medulloblastoma subgroup mechanisms.

## Preliminary coverage gaps to validate

This is a first-pass gap list based on current KB contents. It still needs a
formal crosswalk against COG disease categories, the CCDI study inventory, and
the Rare Cancer Study target list once those targets are explicit.

| Gap cluster | Candidate targets | Why they matter |
|-------------|-------------------|-----------------|
| Missing major pediatric liver / renal / adrenal tumors | Hepatoblastoma, clear cell sarcoma of kidney, rhabdoid tumor of kidney, pediatric adrenocortical carcinoma | Important pediatric entities with strong developmental and predisposition biology |
| Missing CNS subgroup coverage | Medulloblastoma Group 3, Medulloblastoma Group 4, ependymoma molecular groups, atypical teratoid / rhabdoid tumor (ATRT) as an explicit CNS entity | Strong fit for methylation-aware curation and subgroup modeling |
| Missing pediatric leukemia diversity | Ph-like ALL, KMT2A-rearranged infant leukemia, T-ALL, JMML | High clinical need and ideal for WES / fusion / signaling interpretation |
| Missing rare fusion-driven sarcomas | Infantile fibrosarcoma, CIC-rearranged sarcoma, BCOR-altered sarcoma, alveolar soft part sarcoma, NUT carcinoma | Rare tumors where dismech's fusion-to-mechanism modeling is especially valuable |
| Missing direct rare-study alignment | Rare Cancer Study target entities once published | Needed for a direct bridge into upcoming CCDI rare cancer infrastructure |

## MCI Integration Strategy

| MCI / CCDI asset | Natural dismech landing zone | Notes |
|------------------|------------------------------|-------|
| Diagnosis-time WES | `genetic`, `variants`, `biochemical`, `has_subtypes` | Good fit for driver mutation, copy-number, predisposition, and molecular risk annotation |
| Fusion calling | `genetic`, `gene_products`, `pathophysiology` | Strongest current fit: fusion event -> gene product -> pathway activation -> phenotype / histopathology |
| DNA methylation classification | `datasets` with `METHYLATION`, `has_subtypes`, `diagnosis`, `histopathology` | Likely representable today, but a more explicit molecular classification pattern may be useful |
| Research characterization (WGS, RNA-seq, single-cell, proteomics, metabolomics) | `datasets`, `biochemical`, `pathophysiology`, `experimental_models` | Useful for deeper mechanism support and multimodal evidence integration |
| Whole-slide pathology and RADIANCE embeddings | `datasets`, `histopathology` | Deep integration may need future support for image-derived feature or embedding metadata |

### Schema observations

The current schema already includes the major assay types needed for a first MCI
alignment pass, including `WES`, `WGS`, `METHYLATION`, `PROTEOMICS`,
`METABOLOMICS`, and `MULTI_OMICS` dataset types. That means Tier 1 work can
start immediately without schema changes.

The most likely extension points are:

1. A more explicit molecular classification / assay-result pattern for
   methylation subgrouping, classifier outputs, and assay provenance.
2. A lightweight way to reference image-derived pathology features or embedding
   assets from RADIANCE.
3. A repeatable export pattern for graph edges linking genomic calls to
   mechanisms, phenotypes, and treatments.

## Cancer Curation Conventions

This project should use Wilms tumor and issue `#1198` as the working pattern
for pediatric oncology curation.

1. A dismech entry is the mechanism-graph curation unit, not every ontology
   subclass. Split into separate disease files only when a subgroup has a
   genuinely distinct causal program, such as pathway-defined medulloblastoma
   groups or fusion-defined sarcomas.
2. Keep `disease_term` MONDO-first whenever a suitable MONDO disease class
   exists. Add disease-level `ncit_mappings` routinely for pediatric cancer
   entries so the same entry is grounded in both MONDO and oncology-native
   NCIT concepts.
3. Model cancer refinements as flat subtype axes rather than nested lattices or
   one-file-per-subclass. Common axes include histology, stage, laterality, age
   group, and predisposition context.
4. Treat `subtype_term` and subtype `mappings` as ontology grounding only.
   They should not imply a separate dismech page or a "Not Yet Curated" badge.
5. Prefer NCIT over MAXO when NCIT provides materially better oncology
   specificity, especially for histopathology, disease/subtype mappings,
   biomarkers, and cancer procedures or therapeutic concepts.
6. When a subtype axis is introduced, keep it as explicit and as close to
   closed as practical. For example, hereditary-predisposition-associated
   should usually be complemented by `sporadic`, not `somatic`.

The current Wilms entry already follows this pattern: MONDO-first disease
anchor, disease-level NCIT mapping, flat subtype axes, ontology-grounded
subtypes that do not imply separate pages, and NCIT-first oncology treatment
terms where they are more precise than MAXO.

## Priority curation targets

| Target | Why now | CCDI / MCI fit |
|--------|---------|----------------|
| **Hepatoblastoma** | Major missing embryonal tumor with strong developmental biology | Good pediatric solid-tumor pilot for WES + methylation + histology alignment |
| **Medulloblastoma Group 3 / Group 4** | Obvious adjacent gap next to existing SHH / WNT entries | Direct test of subgroup and methylation modeling |
| **Ependymoma molecular subtypes** | Pediatric CNS entity where molecular classification strongly matters; likely needs a file-vs-facet decision by subgroup | Strong methylation-driven use case |
| **Atypical teratoid / rhabdoid tumor (ATRT)** | Rare but mechanism-clear SMARCB1 / SMARCA4-driven tumor | Excellent rare-cancer + epigenetic mechanism fit |
| **Ph-like ALL / KMT2A-rearranged infant leukemia / JMML** | High clinical need with actionable signaling or fusion biology | Strong WES / fusion integration target |
| **Infantile fibrosarcoma and related rare fusion sarcomas** | Very strong fusion-to-mechanism use case | Good demonstration of rare cancer alignment |

## AI-ready knowledge export

1. Use claim extraction work, including the planned extraction pipeline in issue
   `#1100`, to turn pediatric cancer literature and reports into structured
   mechanism claims.
2. Normalize disease entries MONDO-first, add NCIT disease/subtype mappings for
   cancer-specific grounding, and use HGNC, GENO, GO, CL, and NCIT-first
   oncology intervention terms so the output is interoperable with CCDI
   resources.
3. Convert curated mechanism chains into graph edges or triples such as
   alteration -> gene product -> pathway -> cell state -> phenotype /
   histopathology / treatment response.
4. Join those graphs to MCI molecular findings and, later, RADIANCE morphology
   embeddings for multimodal pediatric cancer analysis.
5. Provide exports that are easy to consume in AI pipelines, cohort analysis,
   and validation workflows.

## Rare cancer alignment

The upcoming CCDI Rare Cancer Study is a particularly good fit for dismech.
Rare disease mechanism curation is already a core strength of the project, and
many pediatric rare cancers are exactly the kinds of entities where a
mechanism-first knowledge graph is most useful: small cohorts, heterogeneous
biology, limited trial evidence, and high value in connecting a molecular event
to a plausible downstream disease process.

A practical alignment strategy:

- Start with rare pediatric tumors that have unusually clear mechanism anchors
  such as gene fusions, chromatin-remodeling defects, or predisposition
  syndromes.
- Capture the minimum useful interpretive layer for each entity: disease term,
  driver event, gene product, pathway node, histopathology context, phenotypes,
  and any linked datasets or trials.
- Use longitudinal concepts already supported by the schema, especially
  progression and treatment sections, to represent relapse, resistance, and
  secondary malignancy risks where relevant.

---

## Tasks

### Tier 1: Low Effort (audits, mappings, pilot design)

- [ ] Build a coverage matrix comparing current pediatric / AYA entries against COG disease groups
- [ ] Cross-reference current coverage against CCDI ecosystem studies and portals
- [ ] Add a rare-cancer target crosswalk once the Rare Cancer Study list is explicit
- [ ] Draft an MCI-to-dismech field mapping for WES, fusions, methylation, and pathology
- [ ] Select 5 pilot pediatric cancers for deep mechanism curation
- [ ] Audit current pediatric entries for MONDO-first disease anchors, disease-level NCIT mappings, and flat subtype axes
- [ ] Audit current pediatric entries for `datasets`, `clinical_trials`, and molecular subgroup completeness

### Tier 2: Medium Effort (new entries and backfill)

- [ ] Create Hepatoblastoma
- [ ] Create Medulloblastoma Group 3
- [ ] Create Medulloblastoma Group 4
- [ ] Decide which ependymoma molecular groups merit separate files versus subtype axes
- [ ] Create ATRT as a distinct CNS entry if the existing Rhabdoid Tumor entry is too broad
- [ ] Create at least one pediatric rare leukemia entry (JMML, KMT2A-rearranged infant leukemia, or Ph-like ALL)
- [ ] Backfill existing pediatric entries with MCI-relevant `datasets` and `histopathology`
- [ ] Add explicit fusion-to-pathway chains for existing fusion-driven tumors

### Tier 3: High Effort (schema, export, multimodal)

- [ ] Decide whether a dedicated molecular classification / assay-result class is needed
- [ ] Prototype AI-ready export of pediatric mechanism graphs as triples or edge tables
- [ ] Link claim extraction output to pediatric cancer graph construction
- [ ] Define how RADIANCE image features or embeddings should be represented or referenced
- [ ] Add cohort-level or case-level interpretation examples showing genomic call -> mechanism graph -> clinical relevance

### Tier 4: Aspirational (external alignment)

- [ ] Align curated pediatric mechanism graphs with CCDI Hub discovery concepts and study metadata
- [ ] Evaluate a contribution pathway into CCDI AI / harmonization workflows
- [ ] Package a rare pediatric cancer starter set for the upcoming Rare Cancer Study
- [ ] Explore privacy-preserving or federated knowledge integration patterns for institutional pediatric data

## Cross-project synergies

| Project | Synergy |
|---------|---------|
| **CANCER** | General oncology prioritization; this project is the pediatric / AYA execution slice |
| **VIRTUAL_CELL** | AI-ready export, multimodal integration, and graph-to-model handoff |
| **G2P** | Germline predisposition and genotype-phenotype interpretation in pediatric syndromes |
| **COMORBIDITIES** / **MONDO_EHR_MAPPINGS** | EHR cohort discovery, registry harmonization, and longitudinal phenotype alignment |

# STATUS

## Scoping

- [x] Create project file
- [ ] Inventory current pediatric / AYA cancer coverage in the KB
- [ ] Crosswalk current coverage to COG disease categories
- [ ] Crosswalk current coverage to CCDI ecosystem studies
- [ ] Crosswalk current coverage to Rare Cancer Study target entities

## Integration design

- [ ] Draft MCI mapping for WES / fusion / methylation / pathology inputs
- [ ] Record schema extension decision for molecular classification and assay provenance
- [x] Record Wilms / `#1198` cancer curation conventions for pediatric oncology entries
- [ ] Draft AI-ready export plan for pediatric mechanism graphs
- [ ] Draft RADIANCE integration concept

## Execution

- [ ] Select pilot pediatric curation set
- [ ] Curate first missing high-priority pediatric cancer
- [ ] Backfill existing pediatric entries with MCI-aligned datasets and molecular subgroup context

## Notes

### 2026-04-12 (Project Creation)

**Key observations:**

1. dismech already has a stronger pediatric cancer foothold than the generic
   cancer project alone suggests, including multiple pediatric solid tumors,
   sarcomas, CNS tumors, and predisposition syndromes.
2. The current schema is already adequate for a first-pass MCI alignment because
   it has dedicated `genetic`, `pathophysiology`, `histopathology`, `datasets`,
   and `clinical_trials` sections plus pediatric-relevant dataset types such as
   `WES`, `WGS`, and `METHYLATION`.
3. The biggest near-term modeling challenge is not fusion biology; it is
   representing methylation-based subgrouping, assay provenance, and
   pathology-derived AI features in a way that stays clean and reusable.
4. The Rare Cancer Study is unusually well aligned with dismech because rare,
   mechanism-rich tumors are where evidence-backed curation is most helpful.
5. The highest-leverage AI contribution is likely a pipeline from claim
   extraction -> normalized mechanism graph -> pediatric molecular data
   integration, rather than a standalone model effort.
6. The gap list in this file is intentionally preliminary and should be
   validated against official CCDI / COG disease inventories before curation
   priorities are frozen.

### 2026-04-12 (Cancer Curation Conventions from Wilms / #1198)

**Modeling decisions carried forward into this project:**

1. Use one disease file per coherent mechanism graph, not one file per NCIT or
   MONDO subclass.
2. Keep `disease_term` MONDO-first and add disease-level NCIT mappings
   routinely for pediatric cancer entries.
3. Model cancer refinements as flat subtype axes such as histology, stage,
   laterality, age group, and predisposition context.
4. Treat `subtype_term` and subtype mappings as ontology grounding only rather
   than signals that a separate dismech page should exist.
5. Prefer NCIT over MAXO where NCIT gives meaningfully better oncology
   specificity, especially for cancer procedures, histopathology, and
   disease/subtype mapping.
6. Use Wilms tumor as the worked example for future childhood-cancer curation,
   especially when deciding whether a subgroup should be a separate file or a
   facet within one entry.
