---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-28T08:09:13.315222'
end_time: '2026-05-28T08:37:29.278503'
duration_seconds: 1695.96
template_file: templates/module_mechanism_research.md
template_variables:
  module_name: Meiotic Prophase Failure Module
  module_slug: meiotic_prophase_failure
  category: Module
  module_description: 'A conserved mechanism module for inherited gametogenic failure
    caused by disruption of meiotic prophase I chromosome synapsis and recombination.
    In affected germ cells, programmed meiotic chromosome events fail at homolog pairing,
    synaptonemal complex assembly, homologous-recombination repair of DNA double-strand
    breaks, or pachytene checkpoint resolution. The shared path is meiotic arrest
    with germ-cell apoptosis, producing sex-dimorphic clinical outcomes: ovarian follicle
    depletion and primary ovarian insufficiency in 46,XX individuals, and spermatogenic
    arrest with non-obstructive azoospermia or Sertoli-cell-only syndrome in 46,XY
    individuals. This module is intended for meiotic genes such as SYCE1, MCM8, MCM9,
    STAG3, HFM1, MSH4, MSH5, DMC1, and SYCP3. It intentionally excludes upstream gonadal
    organogenesis and steroidogenic transcription-factor disorders such as NR5A1,
    WT1, SOX9, SRY, FOXL2, and DHH.'
  pathophysiology_summary: '- Meiotic Prophase I Entry and Homolog Pairing: Germ cells
    enter the meiotic cell cycle and initiate prophase I chromosome pairing. This
    node captures the shared upstream context for module genes: the gonad is present,
    germ cells enter meiosis, and homologous chromosomes must pair before synapsis
    and recombination can be completed.

    - Synaptonemal Complex Assembly: Synaptonemal complex components assemble between
    paired homologous chromosomes during meiotic prophase I. Disruption of central
    or lateral element proteins such as SYCE1 or SYCP3 produces asynapsis or unstable
    synapsis, preventing normal progression through pachytene.

    - Homologous Recombination Repair of Meiotic DNA Breaks: Programmed and repair-associated
    DNA breaks in meiotic prophase require homologous-recombination machinery to complete
    chromosome pairing, crossover formation, and genome integrity surveillance. Disruption
    of repair factors such as MCM8, MCM9, DMC1, HFM1, MSH4, or MSH5 leaves meiotic
    DNA damage unresolved and blocks normal pachytene progression.

    - Pachytene Checkpoint Arrest and Germ Cell Apoptosis: Failed synapsis or unresolved
    meiotic recombination activates pachytene checkpoint signaling. Instead of completing
    meiotic prophase and producing functional gametes, affected germ cells arrest
    and are eliminated by apoptosis.

    - Ovarian Follicle Depletion and Primary Ovarian Insufficiency: In 46,XX individuals,
    loss of oocytes during fetal or early postnatal meiotic progression depletes the
    ovarian follicle pool. The clinical manifestation is primary ovarian insufficiency,
    ovarian dysgenesis, primary amenorrhea, or hypergonadotropic hypogonadism depending
    on ascertainment and residual ovarian reserve.

    - Spermatogenic Arrest and Non-Obstructive Azoospermia: In 46,XY individuals,
    meiotic prophase failure in spermatocytes produces spermatogenic arrest, often
    observed clinically as non-obstructive azoospermia, maturation arrest, or Sertoli-cell-only
    syndrome after germ cell depletion.

    - Somatic DNA Repair Deficiency and Cancer Predisposition: A gene-specific branch
    for module genes that also function in mitotic or somatic DNA repair. MCM8 and
    MCM9 are the main current examples: biallelic variants may combine meiotic prophase
    failure with germ-cell tumors or gastrointestinal polyposis and early-onset malignancy.
    This branch should be used only when gene-specific evidence supports a somatic
    cancer phenotype.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 16000
    max_embedded_images: 0
citation_count: 32
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: meiotic_prophase_failure-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: meiotic_prophase_failure-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: meiotic_prophase_failure-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Meiotic Prophase Failure Module
- **Module Slug:** meiotic_prophase_failure
- **Category:** Module

## Current Module Description

A conserved mechanism module for inherited gametogenic failure caused by disruption of meiotic prophase I chromosome synapsis and recombination. In affected germ cells, programmed meiotic chromosome events fail at homolog pairing, synaptonemal complex assembly, homologous-recombination repair of DNA double-strand breaks, or pachytene checkpoint resolution. The shared path is meiotic arrest with germ-cell apoptosis, producing sex-dimorphic clinical outcomes: ovarian follicle depletion and primary ovarian insufficiency in 46,XX individuals, and spermatogenic arrest with non-obstructive azoospermia or Sertoli-cell-only syndrome in 46,XY individuals. This module is intended for meiotic genes such as SYCE1, MCM8, MCM9, STAG3, HFM1, MSH4, MSH5, DMC1, and SYCP3. It intentionally excludes upstream gonadal organogenesis and steroidogenic transcription-factor disorders such as NR5A1, WT1, SOX9, SRY, FOXL2, and DHH.

## Current Provisional Nodes

- Meiotic Prophase I Entry and Homolog Pairing: Germ cells enter the meiotic cell cycle and initiate prophase I chromosome pairing. This node captures the shared upstream context for module genes: the gonad is present, germ cells enter meiosis, and homologous chromosomes must pair before synapsis and recombination can be completed.
- Synaptonemal Complex Assembly: Synaptonemal complex components assemble between paired homologous chromosomes during meiotic prophase I. Disruption of central or lateral element proteins such as SYCE1 or SYCP3 produces asynapsis or unstable synapsis, preventing normal progression through pachytene.
- Homologous Recombination Repair of Meiotic DNA Breaks: Programmed and repair-associated DNA breaks in meiotic prophase require homologous-recombination machinery to complete chromosome pairing, crossover formation, and genome integrity surveillance. Disruption of repair factors such as MCM8, MCM9, DMC1, HFM1, MSH4, or MSH5 leaves meiotic DNA damage unresolved and blocks normal pachytene progression.
- Pachytene Checkpoint Arrest and Germ Cell Apoptosis: Failed synapsis or unresolved meiotic recombination activates pachytene checkpoint signaling. Instead of completing meiotic prophase and producing functional gametes, affected germ cells arrest and are eliminated by apoptosis.
- Ovarian Follicle Depletion and Primary Ovarian Insufficiency: In 46,XX individuals, loss of oocytes during fetal or early postnatal meiotic progression depletes the ovarian follicle pool. The clinical manifestation is primary ovarian insufficiency, ovarian dysgenesis, primary amenorrhea, or hypergonadotropic hypogonadism depending on ascertainment and residual ovarian reserve.
- Spermatogenic Arrest and Non-Obstructive Azoospermia: In 46,XY individuals, meiotic prophase failure in spermatocytes produces spermatogenic arrest, often observed clinically as non-obstructive azoospermia, maturation arrest, or Sertoli-cell-only syndrome after germ cell depletion.
- Somatic DNA Repair Deficiency and Cancer Predisposition: A gene-specific branch for module genes that also function in mitotic or somatic DNA repair. MCM8 and MCM9 are the main current examples: biallelic variants may combine meiotic prophase failure with germ-cell tumors or gastrointestinal polyposis and early-onset malignancy. This branch should be used only when gene-specific evidence supports a somatic cancer phenotype.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology of meiotic prophase I failure leading to
gametogenic failure. Prioritize evidence for:

- The conserved causal chain: meiotic prophase entry, homolog pairing,
  synaptonemal complex assembly, meiotic homologous-recombination repair,
  pachytene checkpoint arrest, germ-cell apoptosis, and sex-dimorphic outcomes.
- The boundary between synaptonemal complex structural genes and homologous
  recombination / DNA-repair genes.
- Gene-specific branches for MCM8 and MCM9 somatic DNA repair and cancer
  predisposition, while distinguishing these from the core meiotic module.
- Explicit exclusions: gonadal organogenesis and steroidogenesis transcription
  factor disorders such as NR5A1, WT1, SOX9, SRY, FOXL2, and DHH.

## Key Genes In Scope

SYCE1, MCM8, MCM9, STAG3, HFM1, MSH4, MSH5, DMC1, SYCP3.

## Questions To Answer

1. What is the best-supported shared mechanism across these genes?
2. Should the module be named `meiotic_prophase_failure`,
   `meiotic_recombination_failure`, or something else?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes support the synaptonemal-complex branch, the homologous
   recombination branch, and the somatic DNA-repair/cancer branch?
5. What evidence supports pachytene checkpoint arrest and apoptosis as the
   shared terminal mechanism in both 46,XX and 46,XY presentations?
6. What direct human evidence links the same gene or variant class to both
   primary ovarian insufficiency and non-obstructive azoospermia?
7. What model organism evidence clarifies the causal path from meiotic defect
   to germ-cell loss?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Mechanism Module Research Template

## Target Module
- **Module Name:** Meiotic Prophase Failure Module
- **Module Slug:** meiotic_prophase_failure
- **Category:** Module

## Current Module Description

A conserved mechanism module for inherited gametogenic failure caused by disruption of meiotic prophase I chromosome synapsis and recombination. In affected germ cells, programmed meiotic chromosome events fail at homolog pairing, synaptonemal complex assembly, homologous-recombination repair of DNA double-strand breaks, or pachytene checkpoint resolution. The shared path is meiotic arrest with germ-cell apoptosis, producing sex-dimorphic clinical outcomes: ovarian follicle depletion and primary ovarian insufficiency in 46,XX individuals, and spermatogenic arrest with non-obstructive azoospermia or Sertoli-cell-only syndrome in 46,XY individuals. This module is intended for meiotic genes such as SYCE1, MCM8, MCM9, STAG3, HFM1, MSH4, MSH5, DMC1, and SYCP3. It intentionally excludes upstream gonadal organogenesis and steroidogenic transcription-factor disorders such as NR5A1, WT1, SOX9, SRY, FOXL2, and DHH.

## Current Provisional Nodes

- Meiotic Prophase I Entry and Homolog Pairing: Germ cells enter the meiotic cell cycle and initiate prophase I chromosome pairing. This node captures the shared upstream context for module genes: the gonad is present, germ cells enter meiosis, and homologous chromosomes must pair before synapsis and recombination can be completed.
- Synaptonemal Complex Assembly: Synaptonemal complex components assemble between paired homologous chromosomes during meiotic prophase I. Disruption of central or lateral element proteins such as SYCE1 or SYCP3 produces asynapsis or unstable synapsis, preventing normal progression through pachytene.
- Homologous Recombination Repair of Meiotic DNA Breaks: Programmed and repair-associated DNA breaks in meiotic prophase require homologous-recombination machinery to complete chromosome pairing, crossover formation, and genome integrity surveillance. Disruption of repair factors such as MCM8, MCM9, DMC1, HFM1, MSH4, or MSH5 leaves meiotic DNA damage unresolved and blocks normal pachytene progression.
- Pachytene Checkpoint Arrest and Germ Cell Apoptosis: Failed synapsis or unresolved meiotic recombination activates pachytene checkpoint signaling. Instead of completing meiotic prophase and producing functional gametes, affected germ cells arrest and are eliminated by apoptosis.
- Ovarian Follicle Depletion and Primary Ovarian Insufficiency: In 46,XX individuals, loss of oocytes during fetal or early postnatal meiotic progression depletes the ovarian follicle pool. The clinical manifestation is primary ovarian insufficiency, ovarian dysgenesis, primary amenorrhea, or hypergonadotropic hypogonadism depending on ascertainment and residual ovarian reserve.
- Spermatogenic Arrest and Non-Obstructive Azoospermia: In 46,XY individuals, meiotic prophase failure in spermatocytes produces spermatogenic arrest, often observed clinically as non-obstructive azoospermia, maturation arrest, or Sertoli-cell-only syndrome after germ cell depletion.
- Somatic DNA Repair Deficiency and Cancer Predisposition: A gene-specific branch for module genes that also function in mitotic or somatic DNA repair. MCM8 and MCM9 are the main current examples: biallelic variants may combine meiotic prophase failure with germ-cell tumors or gastrointestinal polyposis and early-onset malignancy. This branch should be used only when gene-specific evidence supports a somatic cancer phenotype.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology of meiotic prophase I failure leading to
gametogenic failure. Prioritize evidence for:

- The conserved causal chain: meiotic prophase entry, homolog pairing,
  synaptonemal complex assembly, meiotic homologous-recombination repair,
  pachytene checkpoint arrest, germ-cell apoptosis, and sex-dimorphic outcomes.
- The boundary between synaptonemal complex structural genes and homologous
  recombination / DNA-repair genes.
- Gene-specific branches for MCM8 and MCM9 somatic DNA repair and cancer
  predisposition, while distinguishing these from the core meiotic module.
- Explicit exclusions: gonadal organogenesis and steroidogenesis transcription
  factor disorders such as NR5A1, WT1, SOX9, SRY, FOXL2, and DHH.

## Key Genes In Scope

SYCE1, MCM8, MCM9, STAG3, HFM1, MSH4, MSH5, DMC1, SYCP3.

## Questions To Answer

1. What is the best-supported shared mechanism across these genes?
2. Should the module be named `meiotic_prophase_failure`,
   `meiotic_recombination_failure`, or something else?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes support the synaptonemal-complex branch, the homologous
   recombination branch, and the somatic DNA-repair/cancer branch?
5. What evidence supports pachytene checkpoint arrest and apoptosis as the
   shared terminal mechanism in both 46,XX and 46,XY presentations?
6. What direct human evidence links the same gene or variant class to both
   primary ovarian insufficiency and non-obstructive azoospermia?
7. What model organism evidence clarifies the causal path from meiotic defect
   to germ-cell loss?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.


## Meiotic Prophase Failure Module (meiotic_prophase_failure): mechanism-focused research report

### Executive recommendation (module name and scope)
**Recommended name:** **`meiotic_prophase_failure`**.

**Rationale:** The strongest cross-gene unifier is failure of **meiotic prophase I** progression driven by defects in **homolog pairing/synapsis (synaptonemal complex/cohesin/axis)** and/or **programmed DSB repair/crossover formation**, converging on **surveillance signaling, meiotic arrest, and germ-cell elimination** (often via apoptosis), with **sex-dimorphic clinical outcomes** (POI in 46,XX; NOA/spermatogenic arrest in 46,XY). Reviews describe that SC/synapsis defects cause “an arrest in meiotic prophase I” and infertility in both sexes, matching this module’s intent to be reusable across both SC-structural and recombination/repair genes. (llano2023synaptonemalcomplexin pages 7-8)

**Why not `meiotic_recombination_failure`?** That name under-covers clear SC/cohesin-axis structural causes of prophase arrest (e.g., SYCE1, SYCP3, STAG3) that can precede or secondarily impair recombination; the core convergence is prophase arrest rather than recombination alone. (llano2023synaptonemalcomplexin pages 7-8, ding2023dnadoublestrandbreak pages 14-16)

**Explicit scope boundary:** The module should start **after gonad formation** and **meiotic entry** are established, and should exclude disorders of **gonadal organogenesis and steroidogenic transcription factors** (NR5A1, WT1, SOX9, SRY, FOXL2, DHH), consistent with a “meiosis-based infertility” mechanism rather than gonadal determination defects. (huang2024geneticcontrolof pages 11-12, llano2023synaptonemalcomplexin pages 7-8)

### 1) Key concepts and definitions (current understanding)

#### Meiotic prophase I and the conserved causal chain
Meiotic prophase I is the extended stage in which homologs **pair**, assemble the **synaptonemal complex (SC)** to **synapse**, and repair programmed **DSBs** by **homologous recombination** to generate **crossovers** that enable accurate segregation.

A key shared mechanistic statement across the module’s gene set is that **synapsis failure or SC absence** causes “failure in meiotic recombination and an arrest in meiotic prophase I,” producing infertility in both males and females. (llano2023synaptonemalcomplexin pages 7-8)

#### Surveillance: recombination checkpoint and synapsis/asynapsis response (MSUC/MSCI)
A recent mammalian surveillance synthesis describes how defects in recombination or synapsis trigger DNA-damage and asynapsis responses that can culminate in germ-cell elimination:
* **Recombination-dependent elimination in females:** an “apoptotic BCL-2-dependent pathway acts downstream of CHK2/p53/TAp63 and eliminates recombination-defective oocytes,” involving p53/TAp63 targets PUMA, NOXA, and BAX; deletion of these effectors rescues oocyte numbers in DSB-repair mutants including **Dmc1−/−** and **Msh5−/−**. (huang2024geneticcontrolof pages 11-12)
* **Asynapsis surveillance:** “Defects in chromosome axis formation or SC assembly can activate a cell response to asynapsis… leading to cell cycle arrest and even apoptosis,” and by late zygotene “HORMAD1/2 acts together with SYCP3 to recruit… BRCA1… [and] ATR” to unsynapsed axes; in males, spermatocyte loss can involve **MSCI failure**. (huang2024geneticcontrolof pages 11-12)

These surveillance mechanisms support your terminal node **“Pachytene checkpoint arrest and germ cell apoptosis”** as a reusable convergence point, with the caveat that “synapsis checkpoint” in mammals is complex and sometimes conceptualized through MSUC/MSCI rather than a single canonical checkpoint. (huang2024geneticcontrolof pages 11-12)

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### (A) 2023: synaptonemal complex and human disease
A 2023 SC-focused review highlights that infertility-related mutations are known in **SYCP3/SYCP2** (lateral element) and **SYCE1/SIX6OS1** (central element), and explicitly states: “Clinical mutations in SYCE1 associated with NOA and POI… affect… structural assembly of the SC.” (llano2023synaptonemalcomplexin pages 7-8)

This directly supports a module branch in which **SC structural defects** are a primary lesion that propagates to recombination failure and meiotic prophase arrest.

#### (B) 2023: surveillance mechanisms (checkpoint → apoptosis)
A 2023 surveillance review provides mechanistic detail connecting recombination defects to apoptotic execution in oocytes, and separately describes asynapsis/MSUC/MSCI pathways relevant to spermatocyte loss. (huang2024geneticcontrolof pages 11-12)

#### (C) 2024: MCM8/MCM9 biology links meiosis and somatic genome maintenance
Two 2024 papers refine the “dual-role” status of the MCM8/9 axis:
* **MCM8 as a meiotic and mitotic genome-stability factor:** “MCM8… is crucial for meiotic homologous recombination repair” and “safeguards genome stability… during mitosis”; Mcm8 loss in mice causes primordial germ-cell proliferation defects, and “loss of MCM8 led to R-loop accumulation… thus inducing genome instability.” (wen2024mcm8interactswith pages 1-2)
* **MCM8-9/HROB and cancer linkage language:** A mechanistic Nature Communications study states: “In humans, defects associated with MCM8-9 were linked to primary ovarian failure and hence infertility,” and that “defects or overexpression of MCM8-9 may promote cancer,” while emphasizing roles in HR in response to ICLs and replication fork stability. (acharya2024mechanismofdna pages 1-2)

These provide strong support for a **gene-specific optional branch** (“Somatic DNA repair deficiency and cancer predisposition”) for MCM8/MCM9, while keeping the core module centered on meiotic prophase failure. (acharya2024mechanismofdna pages 1-2, wen2024mcm8interactswith pages 1-2)

### 3) Current applications and real-world implementations

#### Clinical genetics: infertility/POI/NOA gene discovery and counseling
The clinical utility is primarily in **genetic diagnosis and counseling**:
* A Human Reproduction study frames STAG3 testing as relevant in NOA with meiotic arrest, warning of unnecessary invasive retrieval attempts: it reports STAG3 variants cause “male infertility due to meiotic arrest,” and notes implications for counseling and TESE/ICSI planning. (bijl2019mutationsinthe pages 1-2)
* An SC review anticipates increasing yield of SC-gene diagnoses as more cases are studied, supporting a reusable mechanism module that can be conformed to by gene-specific disease entries. (llano2023synaptonemalcomplexin pages 7-8)

#### Research/functional genomics implementations
Modern implementations include CRISPR “humanized” mouse models used to validate infertility variants (e.g., Syce1 knock-in modeled after a human mutation recreating infertility and absent follicles). (ding2023dnadoublestrandbreak pages 14-16)

### 4) Expert opinions and analysis (authoritative sources)

#### Why pachytene arrest and apoptosis are the shared terminal mechanism
The best-supported terminal convergence is surveillance-mediated elimination:
* For recombination defects, checkpoint signaling via CHK2/p53/TAp63 and downstream BCL2-family effectors removes defective oocytes (Dmc1−/−, Msh5−/−) and can be genetically rescued, indicating causal linkage between meiotic prophase defects and apoptosis. (huang2024geneticcontrolof pages 11-12)
* For synapsis/asynapsis, MSUC/MSCI-related processes provide an additional, sex-influenced route to arrest and loss, including male spermatocyte loss via MSCI failure. (huang2024geneticcontrolof pages 11-12)

#### Branch boundary: SC structural genes vs HR/recombination genes
A practical boundary is whether the primary lesion is:
* **SC architecture / chromosome axis / cohesin** (e.g., SYCE1, SYCP3, STAG3), or
* **DSB repair / recombination intermediate processing / crossover formation** (e.g., DMC1, MSH4, MSH5, HFM1),
while acknowledging interdependence (SC provides context for recombination; recombination defects can destabilize synapsis). (llano2023synaptonemalcomplexin pages 7-8)

### 5) Relevant statistics and data from recent studies

Because this is a mechanism module, the most directly relevant “statistics” are prevalence/context figures in foundational clinical genetics papers:
* Familial infertility background: “Infertility… affecting up to **15% of couples**” (used as context in a cross-sex STAG3 family study). (jaillard2020stag3homozygousmissense pages 1-2)
* POI and NOA epidemiology context: POI “affecting up to **1 in 100 women**,” and NOA “has an incidence of **1%**,” as stated in the STAG3 POI+NOA family report abstract. (jaillard2020stag3homozygousmissense pages 1-2)
* STAG3 rarity estimate in a meiotic-arrest NOA cohort: STAG3 variants “are a rare cause of NOA (**<1% of cases**)” in a curated meiotic-arrest setting. (bijl2019mutationsinthe pages 1-2)

### Proposed DAG (nodes and causal edges)

#### Core nodes (required for conformance)
1. **Meiotic prophase I pairing/synapsis initiation context** (entry into meiosis is background; module begins at homolog pairing/synapsis initiation).
2. **Synaptonemal complex / chromosome axis-cohesin function** (structural synapsis machinery).
3. **Programmed DSB processing and homologous recombination/crossover formation**.
4. **Surveillance response (recombination DDR checkpoint and/or asynapsis/MSUC/MSCI surveillance)**.
5. **Meiotic prophase arrest (often pachytene/zygotene context-dependent)**.
6. **Germ-cell apoptosis / elimination**.
7. **Sex-dimorphic tissue outcomes**:
   * **46,XX:** oocyte depletion → follicle depletion → POI.
   * **46,XY:** spermatocyte arrest → NOA/spermatogenic arrest; late Sertoli-cell-only can occur after depletion.

This structure is explicitly supported by the observation that synapsis-defective mutants arrest in meiotic prophase I and cause infertility in both sexes, and by surveillance → apoptosis mechanisms in mammalian models. (llano2023synaptonemalcomplexin pages 7-8, huang2024geneticcontrolof pages 11-12)

#### Optional nodes (gene-specific)
A. **Somatic HR/ICL repair / replication stress response** (optional; for genes with strong somatic roles such as MCM8/9). (acharya2024mechanismofdna pages 1-2, wen2024mcm8interactswith pages 1-2)
B. **Cancer predisposition / genome instability phenotype** (optional; requires gene-specific evidence; do not generalize to all module genes). (acharya2024mechanismofdna pages 1-2)

### Gene-to-node mapping (branches)

| Gene | Primary functional branch | Most relevant module nodes supported | Key human phenotypes | Key evidence context IDs |
|---|---|---|---|---|
| SYCE1 | Synaptonemal complex structural | Meiotic Prophase I Entry and Homolog Pairing; Synaptonemal Complex Assembly; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia | POI; NOA; meiotic arrest | (llano2023synaptonemalcomplexin pages 7-8, verrilli2021sharedgeneticsbetween pages 3-5, ding2023dnadoublestrandbreak pages 14-16, verrilli2021sharedgeneticsbetween pages 5-6) |
| SYCP3 | Synaptonemal complex structural | Meiotic Prophase I Entry and Homolog Pairing; Synaptonemal Complex Assembly; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Spermatogenic Arrest and Non-Obstructive Azoospermia | NOA; azoospermia; likely shared meiotic-prophase infertility branch | (ozturk2023geneticvariantsunderlying pages 34-35, llano2023synaptonemalcomplexin pages 7-8, huang2024geneticcontrolof pages 11-12) |
| STAG3 | Synaptonemal complex structural/cohesin | Meiotic Prophase I Entry and Homolog Pairing; Synaptonemal Complex Assembly; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia | POI; NOA; complete bilateral meiotic arrest | (bijl2019mutationsinthe pages 1-2, llano2023synaptonemalcomplexin pages 7-8, jaillard2020stag3homozygousmissense pages 1-2) |
| MCM8 | Dual somatic repair/cancer | Homologous Recombination Repair of Meiotic DNA Breaks; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia; Somatic DNA Repair Deficiency and Cancer Predisposition | POI; NOA; genome instability; possible cancer predisposition branch | (acharya2024mechanismofdna pages 16-16, wen2024mcm8interactswith pages 1-2, acharya2024mechanismofdna pages 1-2) |
| MCM9 | Dual somatic repair/cancer | Homologous Recombination Repair of Meiotic DNA Breaks; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia; Somatic DNA Repair Deficiency and Cancer Predisposition | POI; infertility/gametogenesis defects; genome instability; myeloid tumors in model citations | (acharya2024mechanismofdna pages 16-16, llano2023synaptonemalcomplexin pages 8-10, acharya2024mechanismofdna pages 1-2) |
| HFM1 | Homologous recombination repair | Homologous Recombination Repair of Meiotic DNA Breaks; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia | POI; NOA; meiotic arrest/crossover defect | (llano2023synaptonemalcomplexin pages 7-8, ding2023dnadoublestrandbreak pages 21-22) |
| MSH4 | Homologous recombination repair | Homologous Recombination Repair of Meiotic DNA Breaks; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia | POI; azoospermia/meiotic arrest | (huang2024geneticcontrolof pages 11-12, cioppi2021geneticsofazoospermia pages 20-21, llano2023synaptonemalcomplexin pages 7-8) |
| MSH5 | Homologous recombination repair | Homologous Recombination Repair of Meiotic DNA Breaks; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia | POI; azoospermia/meiotic arrest | (huang2024geneticcontrolof pages 11-12, llano2023synaptonemalcomplexin pages 7-8, ozturk2023geneticvariantsunderlying pages 20-22) |
| DMC1 | Homologous recombination repair | Homologous Recombination Repair of Meiotic DNA Breaks; Pachytene Checkpoint Arrest and Germ Cell Apoptosis; Ovarian Follicle Depletion and Primary Ovarian Insufficiency; Spermatogenic Arrest and Non-Obstructive Azoospermia | POI; NOA; spermatocyte arrest; failed synapsis | (verrilli2021sharedgeneticsbetween pages 5-6, llano2023synaptonemalcomplexin pages 7-8, huang2024geneticcontrolof pages 11-12) |


*Table: This table maps each in-scope gene to the most appropriate mechanistic branch and module nodes, while summarizing the key human infertility phenotypes and the evidence contexts from this run that support those assignments.*

### Evidence table (human, model, and review; exact quotes)

| Claim supported | Evidence type (human clinical/model/review/in vitro) | Gene(s) | Exact quote | PMID if present in text (otherwise blank) | Publication (authors, year, journal) | URL | Context ID for citation |
|---|---|---|---|---|---|---|---|
| Synapsis/SC defects cause meiotic prophase I arrest and infertility in both sexes | Review | SC structural genes broadly; STAG3, SYCE1, DMC1, HFM1, MSH4, MSH5 discussed in article | "synapsis-deficient mutants, such as those lacking the SC, experience defects in the proper alignment and pairing of homologous chromosomes, leading to a failure in meiotic recombination and an arrest in meiotic prophase I" and "both types of mutants experience failure in meiotic progression and proper gamete production, resulting in infertility in both males and females." |  | Llano & Pendás, 2023, *Cells* | https://doi.org/10.3390/cells12131718 | (llano2023synaptonemalcomplexin pages 7-8) |
| SYCE1 loss in mouse causes meiotic failure with oocyte apoptosis/POI-like phenotype | Model/review | SYCE1 | "Mice with Syce1 knocked out show oocyte apoptosis and POI-like symptoms due to blocked DSB repair in meiosis" and "both failure of SC assembly and defective crossover formation lead to HR failure, resulting in follicular apoptosis in female mice" |  | Ding et al., 2023, *Journal of Ovarian Research* | https://doi.org/10.1186/s13048-023-01221-2 | (ding2023dnadoublestrandbreak pages 14-16) |
| DMC1 biallelic variant links NOA in a male and POI in his sister within the same family | Human clinical | DMC1 | "A homozygous missense mutation in the DMC1 gene (nM_007068.3, c.106G>A, p.Asp36Asn) was found in a consanguineous Chinese family (30). This family included a 26-year-old male sibling with NOA" and "His older sister, a 30-year-old woman, had been diagnosed with POI at the age of 20 years" and "Whole-exome sequencing identified a homozygous missense mutation in DMC1, c.106G>A, p.Asp36Asn, shared by both siblings" |  | Verrilli et al., 2021, *F&S Reviews* | https://doi.org/10.1016/j.xfnr.2021.04.001 | (verrilli2021sharedgeneticsbetween pages 5-6) |
| STAG3 variant is directly associated with both POI and NOA in one family | Human clinical | STAG3 | "Here, we study a case of familial infertility including a proband with POI and her brother with NOA." and "We performed whole-exome sequencing (WES) and identified a homozygous STAG3 missense variant that segregated with infertility." and "We report the first pathogenic homozygous missense variant in STAG3 and the first STAG3 variant associated with both male and female infertility." |  | Jaillard et al., 2020, *Molecular Human Reproduction* | https://doi.org/10.1093/molehr/gaaa050 | (jaillard2020stag3homozygousmissense pages 1-2) |
| STAG3 loss also causes male meiotic arrest and supports sex-dimorphic module outcome | Human clinical | STAG3 | "SUMMARY ANSWER: Sequence variants affecting protein function of STAG3 cause male infertility due to meiotic arrest." and "Sequence variants in STAG3 have been reported to cause meiotic arrest in male and female mice and premature ovarian failure in human females" and "Two compound-heterozygous variants in STAG3 ... have been found to cause male infertility due to complete bilateral meiotic arrest" |  | van der Bijl et al., 2019, *Human Reproduction* | https://doi.org/10.1093/humrep/dez204 | (bijl2019mutationsinthe pages 1-2) |
| Recombination-defective oocytes are eliminated through CHK2/p53/TAp63 and BCL2-family apoptotic effectors; Dmc1-/-, Msh5-/-, and Msh4-/- models support the terminal mechanism | Model/review | DMC1, MSH5, MSH4 | "apoptotic BCL-2-dependent pathway acts downstream of CHK2/p53/TAp63 and eliminates recombination-defective oocytes"; "PUMA and NOXA or BAX deletion rescue oocyte numbers in DSB-repair mutants (Dmc1−/− and Msh5−/−)"; and "Rnf212 deletion significantly restores the oocyte pool at 18 days postpartum in DSB-repair mutant females (Msh4−/−)" |  | Huang & Roig, 2023, *Frontiers in Cell and Developmental Biology* | https://doi.org/10.3389/fcell.2023.1127440 | (huang2024geneticcontrolof pages 11-12) |
| Synapsis/asynapsis surveillance provides a checkpoint-like route to arrest/apoptosis, including male spermatocyte loss | Review | HORMAD1/2, SYCP3, BRCA1, ATR | "Defects in chromosome axis formation or SC assembly can activate a cell response to asynapsis independently of DSB formation in many organisms, leading to cell cycle arrest and even apoptosis" and "By the late zygotene stage, HORMAD1/2 acts together with SYCP3 to recruit the breast cancer 1 (BRCA1) protein to the unsynapsed axes" and "In males, spermatocyte loss mediated by the DSB-independent response to asynapsis involves the failure of Meiotic Sex Chromosome Inactivation (MSCI)" |  | Huang & Roig, 2023, *Frontiers in Cell and Developmental Biology* | https://doi.org/10.3389/fcell.2023.1127440 | (huang2024geneticcontrolof pages 11-12) |
| MCM8 is crucial for meiotic HR repair and also has somatic genome-stability roles | Primary/review | MCM8 | "MCM8 has emerged as a core gene in reproductive aging and is crucial for meiotic homologous recombination repair." and "It also safeguards genome stability by coordinating the replication stress response during mitosis" and "loss of MCM8 led to R-loop accumulation ... thus inducing genome instability." |  | Wen et al., 2024, *The EMBO Journal* | https://doi.org/10.1038/s44318-024-00134-0 | (wen2024mcm8interactswith pages 1-2) |
| MCM8/9 participate in HR/DNA repair and have a possible cancer/genome-instability branch distinct from the core meiotic module | Primary/review | MCM8, MCM9 | "In humans, defects associated with MCM8-9 were linked to primary ovarian failure and hence infertility" and "defects or overexpression of MCM8-9 may promote cancer" and "Most reports to date suggest that MCM8-9 functions in meiosis and in DNA repair, particularly in homologous recombination (HR) in response to DNA interstrand crosslinks (ICLs), as well as to maintain replication fork stability" |  | Acharya et al., 2024, *Nature Communications* | https://doi.org/10.1038/s41467-024-47936-8 | (acharya2024mechanismofdna pages 1-2) |


*Table: This table compiles the highest-priority evidence supporting the proposed meiotic_prophase_failure mechanism module, including the shared causal chain, sex-dimorphic human phenotypes, checkpoint-mediated germ-cell elimination, and the optional MCM8/9 somatic DNA-repair/cancer branch.*

### Figure evidence supporting mechanistic branches
The SC’s structural organization (including the placement of SC components such as SYCP3 and SYCE1) and the meiotic cohesin complex (including STAG3) are illustrated in the SC review’s figures, which can be used as visual anchors for the module’s “SC assembly” and “cohesin/axis” nodes. (llano2023synaptonemalcomplexin media 4701f75e, llano2023synaptonemalcomplexin media c1bf6f79)

### Human evidence linking the same gene to both POI and NOA (cross-sex)
Strong examples within this module’s scope include:
* **STAG3:** a family report explicitly studies “a proband with POI and her brother with NOA,” identifying a segregating homozygous missense variant. (jaillard2020stag3homozygousmissense pages 1-2)
* **DMC1:** a consanguineous family carrying homozygous DMC1 p.Asp36Asn included a male sibling with NOA and an older sister diagnosed with POI; the variant was shared by both. (verrilli2021sharedgeneticsbetween pages 5-6)
* **SYCE1:** the shared-genetics review notes “Homozygous mutations in the SYCE1 gene were reported in families with both NOA and POI,” consistent with cross-sex prophase I failure for SC-central element disruption. (verrilli2021sharedgeneticsbetween pages 5-6)

### Model organism evidence clarifying the causal path (defect → arrest → apoptosis)
* **Recombination-defective oocyte elimination:** CHK2/p53/TAp63 → BCL2-dependent apoptosis eliminates defective oocytes; PUMA/NOXA/BAX deletion rescues oocyte numbers in Dmc1−/− and Msh5−/−. (huang2024geneticcontrolof pages 11-12)
* **SC central element defect leading to oocyte apoptosis:** “Mice with Syce1 knocked out show oocyte apoptosis and POI-like symptoms,” and HR failure results in “follicular apoptosis.” (ding2023dnadoublestrandbreak pages 14-16)

### Ontology suggestions, out-of-scope notes, and curator open questions

> GO biological process term labels to consider: meiotic cell cycle; meiotic cell cycle process; meiotic prophase I; homologous chromosome pairing at meiosis; synaptonemal complex assembly; meiotic recombination; double-strand break repair via homologous recombination; crossover formation; meiotic DNA damage checkpoint / DNA damage response, signal transduction by p53 class mediator; intrinsic apoptotic signaling pathway in response to DNA damage; germ cell programmed cell death; oocyte differentiation; spermatogenesis; oogenesis (llano2023synaptonemalcomplexin pages 7-8, wen2024mcm8interactswith pages 1-2, huang2024geneticcontrolof pages 11-12)
>
> Cell Ontology labels to consider: germ cell; female germ cell; male germ cell; oogonium; primary oocyte; pachytene oocyte; spermatogonium; primary spermatocyte; pachytene spermatocyte; Sertoli cell only should not be modeled as the primary causal cell type but may be a downstream histopathologic context for severe germ-cell loss in males (verrilli2021sharedgeneticsbetween pages 5-6, bijl2019mutationsinthe pages 1-2, huang2024geneticcontrolof pages 11-12)
>
> UBERON / anatomy labels to consider: gonad; ovary; ovarian follicle; primordial follicle pool / ovarian reserve; fetal ovary; testis; seminiferous tubule; germinal epithelium of testis; seminiferous epithelium; spermatocyte layer; gonadal ridge terms should be avoided unless a curator is intentionally modeling excluded organogenesis disorders (ding2023dnadoublestrandbreak pages 14-16, verrilli2021sharedgeneticsbetween pages 5-6, bijl2019mutationsinthe pages 1-2)
>
> Out-of-scope boundary notes: exclude upstream gonadal determination and organogenesis disorders, including NR5A1, WT1, SOX9, SRY, FOXL2, and DHH; exclude primary steroidogenic or hypothalamic-pituitary causes of hypogonadism; this module should begin only after gonads are present and germ cells have entered meiosis, focusing on prophase I pairing, synapsis, recombination, checkpoint arrest, and germ-cell loss (llano2023synaptonemalcomplexin pages 7-8, huang2024geneticcontrolof pages 11-12)
>
> Weak or speculative claims to flag: do not overstate a universal “pachytene checkpoint” in humans when much direct mechanistic evidence is inferred from mouse models; for females, asynapsis-related elimination may involve both checkpoint signaling and gene-content effects of MSUC, so a single mechanism should be stated cautiously; MCM8/MCM9 cancer predisposition should remain an optional gene-specific branch, because current evidence supports roles in somatic DNA repair/genome instability and possible cancer links, but this is not the core shared mechanism for all module genes and is stronger for some contexts than for a generalized infertility module claim (acharya2024mechanismofdna pages 16-16, llano2023synaptonemalcomplexin pages 8-10, acharya2024mechanismofdna pages 1-2, huang2024geneticcontrolof pages 11-12)
>
> Additional weak-claim cautions: SYCP3 has strong relevance to SC structure and male infertility, but the exact same depth of direct POI-plus-NOA evidence is not equally strong across all in-scope genes; HFM1, MSH4, and MSH5 fit the homologous recombination branch well, but curator review should separate genes supported mainly by cross-sex association from genes supported by same-family same-variant evidence (ozturk2023geneticvariantsunderlying pages 34-35, llano2023synaptonemalcomplexin pages 7-8, ding2023dnadoublestrandbreak pages 21-22)
>
> Open curator questions: should “Meiotic Prophase I Entry and Homolog Pairing” remain a single upstream node, or should “entry into meiosis” be treated as background context while “homolog pairing/synapsis initiation” is the first true module node; should cohesin-axis defects such as STAG3 be grouped with the SC structural branch or represented as a parallel chromosome-axis/cohesin branch feeding synapsis failure; should checkpoint biology be represented as one merged surveillance node or two optional subnodes (“recombination-dependent DDR checkpoint” and “asynapsis/MSUC-MSCI surveillance”); what level of evidence should be required before assigning a gene to the optional somatic DNA-repair/cancer branch; and should Sertoli-cell-only syndrome be modeled only as a late downstream consequence after prolonged germ-cell depletion rather than a core required node (llano2023synaptonemalcomplexin pages 7-8, bijl2019mutationsinthe pages 1-2, huang2024geneticcontrolof pages 11-12, ding2023dnadoublestrandbreak pages 14-16)


*Blockquote: This blockquote summarizes ontology label suggestions, curation boundaries, speculative claims to flag, and key open questions for structuring the meiotic prophase failure module. It is useful for turning the literature review into a reusable, curation-ready mechanism module.*

### Claims that should remain cautious / out of scope
* **Do not overstate a single universal ‘pachytene checkpoint’ in humans:** the surveillance literature emphasizes MSUC/MSCI and sex-specific differences, and some mechanisms are inferred from mouse genetics rather than directly observed in human germ cells. (huang2024geneticcontrolof pages 11-12)
* **Cancer predisposition is optional and gene-specific:** while MCM8-9 defects “may promote cancer,” this should not be treated as a required component of meiotic_prophase_failure conformance without gene-specific evidence in a given disease entry. (acharya2024mechanismofdna pages 1-2)

### Summary answers to module questions
1. **Best-supported shared mechanism:** meiotic prophase I synapsis and/or recombination defects → surveillance signaling (DDR and/or MSUC/MSCI) → meiotic arrest → germ-cell apoptosis → POI in 46,XX and NOA/spermatogenic arrest in 46,XY. (llano2023synaptonemalcomplexin pages 7-8, huang2024geneticcontrolof pages 11-12)
2. **Module name:** `meiotic_prophase_failure` best matches the convergent biology and avoids excluding SC-structural causes. (llano2023synaptonemalcomplexin pages 7-8)
3. **Core vs optional nodes:** core = pairing/synapsis + DSB repair/crossover + surveillance → arrest → apoptosis → sex-dimorphic outcomes; optional = MCM8/9 somatic repair/cancer branch. (acharya2024mechanismofdna pages 1-2, wen2024mcm8interactswith pages 1-2, huang2024geneticcontrolof pages 11-12)
4. **Gene support for branches:** SC/cohesin branch: SYCE1, SYCP3, STAG3; HR/recombination branch: DMC1, MSH4, MSH5, HFM1; somatic repair/cancer branch: MCM8, MCM9. (llano2023synaptonemalcomplexin pages 7-8, wen2024mcm8interactswith pages 1-2, acharya2024mechanismofdna pages 1-2)
5. **Evidence for checkpoint arrest/apoptosis terminal mechanism:** CHK2/p53/TAp63→BCL2-effector pathway eliminates recombination-defective oocytes; asynapsis response can induce arrest/apoptosis and male spermatocyte loss via MSCI failure. (huang2024geneticcontrolof pages 11-12)
6. **Direct human evidence of POI+NOA for the same gene:** STAG3 (family), DMC1 (family), and literature-supported SYCE1 cross-sex association. (jaillard2020stag3homozygousmissense pages 1-2, verrilli2021sharedgeneticsbetween pages 5-6)
7. **Model organism evidence for causal path:** Syce1 knockout oocyte apoptosis/POI-like; Dmc1−/−, Msh5−/−, Msh4−/− checkpoint-linked elimination with genetic rescue; MSUC/MSCI pathways linking asynapsis to spermatocyte loss. (ding2023dnadoublestrandbreak pages 14-16, huang2024geneticcontrolof pages 11-12)
8. **Ontology term labels:** provided in Artifact-02 (no IDs invented). (huang2024geneticcontrolof pages 11-12)
9. **Speculative/weak claims:** checkpoint universality in humans; breadth of cancer predisposition; gene-by-gene strength differences for cross-sex phenotypes. (acharya2024mechanismofdna pages 1-2, huang2024geneticcontrolof pages 11-12)

### Notes on PMIDs and full-text verification
In the retrieved excerpts, **PMID identifiers were not consistently present** (many sources provide DOIs/URLs). For curation workflows requiring PMIDs, PubMed cross-referencing should be performed for each DOI prior to final module deposition.


References

1. (llano2023synaptonemalcomplexin pages 7-8): Elena Llano and Alberto M. Pendás. Synaptonemal complex in human biology and disease. Cells, 12:1718, Jun 2023. URL: https://doi.org/10.3390/cells12131718, doi:10.3390/cells12131718. This article has 19 citations.

2. (ding2023dnadoublestrandbreak pages 14-16): Xuechun Ding, Xiaowei Gong, Yingying Fan, Jinghe Cao, Jingyu Zhao, Yixin Zhang, Xiaomei Wang, and Kai Meng. Dna double-strand break genetic variants in patients with premature ovarian insufficiency. Journal of Ovarian Research, Jul 2023. URL: https://doi.org/10.1186/s13048-023-01221-2, doi:10.1186/s13048-023-01221-2. This article has 14 citations and is from a peer-reviewed journal.

3. (huang2024geneticcontrolof pages 11-12): Yan Huang and Ignasi Roig. Genetic control of meiosis surveillance mechanisms in mammals. Frontiers in Cell and Developmental Biology, Feb 2023. URL: https://doi.org/10.3389/fcell.2023.1127440, doi:10.3389/fcell.2023.1127440. This article has 39 citations.

4. (wen2024mcm8interactswith pages 1-2): Canxin Wen, Lili Cao, Shuhan Wang, Weiwei Xu, Yongze Yu, Simin Zhao, Fan Yang, Zi-Jiang Chen, Shidou Zhao, Yajuan Yang, and Yingying Qin. Mcm8 interacts with ddx5 to promote r-loop resolution. The EMBO Journal, 43:3044-3071, Jun 2024. URL: https://doi.org/10.1038/s44318-024-00134-0, doi:10.1038/s44318-024-00134-0. This article has 25 citations.

5. (acharya2024mechanismofdna pages 1-2): Ananya Acharya, Raphaël Guérois, Alberto Ciccia, Ralf Seidel, Vera Maria Kissling, Martin Göse, Martin Mütze, Jen-Wei Huang, Hélène Bret, and Petr Cejka. Mechanism of dna unwinding by mcm8-9 in complex with hrob. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47936-8, doi:10.1038/s41467-024-47936-8. This article has 13 citations and is from a highest quality peer-reviewed journal.

6. (bijl2019mutationsinthe pages 1-2): N. V. D. Bijl, A. Röpke, U. Biswas, M. Wöste, R. Jessberger, S. Kliesch, C. Friedrich, and F. Tüttelmann. Mutations in the stromal antigen 3 (stag3) gene cause male infertility due to meiotic arrest. Human Reproduction, Nov 2019. URL: https://doi.org/10.1093/humrep/dez204, doi:10.1093/humrep/dez204. This article has 91 citations and is from a highest quality peer-reviewed journal.

7. (jaillard2020stag3homozygousmissense pages 1-2): Sylvie Jaillard, Kenneth McElreavy, Gorjana Robevska, Linda Akloul, Farah Ghieh, Rajini Sreenivasan, Marion Beaumont, Anu Bashamboo, Joelle Bignon-Topalovic, Anne-Sophie Neyroud, Katrina Bell, Elisabeth Veron-Gastard, Erika Launay, Jocelyn van den Bergen, Bénédicte Nouyou, François Vialard, Marc-Antoine Belaud-Rotureau, Katie L Ayers, Sylvie Odent, Célia Ravel, Elena J Tucker, and Andrew H Sinclair. Stag3 homozygous missense variant causes primary ovarian insufficiency and male non-obstructive azoospermia. Molecular human reproduction, 26:665-677, Jul 2020. URL: https://doi.org/10.1093/molehr/gaaa050, doi:10.1093/molehr/gaaa050. This article has 53 citations and is from a peer-reviewed journal.

8. (verrilli2021sharedgeneticsbetween pages 3-5): Lauren Verrilli, Erica Johnstone, Kristina Allen-Brady, and Corrine Welt. Shared genetics between nonobstructive azoospermia and primary ovarian insufficiency. F&amp;S Reviews, 2:204-213, Jul 2021. URL: https://doi.org/10.1016/j.xfnr.2021.04.001, doi:10.1016/j.xfnr.2021.04.001. This article has 11 citations.

9. (verrilli2021sharedgeneticsbetween pages 5-6): Lauren Verrilli, Erica Johnstone, Kristina Allen-Brady, and Corrine Welt. Shared genetics between nonobstructive azoospermia and primary ovarian insufficiency. F&amp;S Reviews, 2:204-213, Jul 2021. URL: https://doi.org/10.1016/j.xfnr.2021.04.001, doi:10.1016/j.xfnr.2021.04.001. This article has 11 citations.

10. (ozturk2023geneticvariantsunderlying pages 34-35): Saffet Ozturk. Genetic variants underlying spermatogenic arrests in men with non-obstructive azoospermia. Cell Cycle, 22:1021-1061, Feb 2023. URL: https://doi.org/10.1080/15384101.2023.2171544, doi:10.1080/15384101.2023.2171544. This article has 15 citations and is from a peer-reviewed journal.

11. (acharya2024mechanismofdna pages 16-16): Ananya Acharya, Raphaël Guérois, Alberto Ciccia, Ralf Seidel, Vera Maria Kissling, Martin Göse, Martin Mütze, Jen-Wei Huang, Hélène Bret, and Petr Cejka. Mechanism of dna unwinding by mcm8-9 in complex with hrob. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47936-8, doi:10.1038/s41467-024-47936-8. This article has 13 citations and is from a highest quality peer-reviewed journal.

12. (llano2023synaptonemalcomplexin pages 8-10): Elena Llano and Alberto M. Pendás. Synaptonemal complex in human biology and disease. Cells, 12:1718, Jun 2023. URL: https://doi.org/10.3390/cells12131718, doi:10.3390/cells12131718. This article has 19 citations.

13. (ding2023dnadoublestrandbreak pages 21-22): Xuechun Ding, Xiaowei Gong, Yingying Fan, Jinghe Cao, Jingyu Zhao, Yixin Zhang, Xiaomei Wang, and Kai Meng. Dna double-strand break genetic variants in patients with premature ovarian insufficiency. Journal of Ovarian Research, Jul 2023. URL: https://doi.org/10.1186/s13048-023-01221-2, doi:10.1186/s13048-023-01221-2. This article has 14 citations and is from a peer-reviewed journal.

14. (cioppi2021geneticsofazoospermia pages 20-21): Francesca Cioppi, Viktoria Rosta, and Csilla Krausz. Genetics of azoospermia. International Journal of Molecular Sciences, 22:3264, Mar 2021. URL: https://doi.org/10.3390/ijms22063264, doi:10.3390/ijms22063264. This article has 207 citations.

15. (ozturk2023geneticvariantsunderlying pages 20-22): Saffet Ozturk. Genetic variants underlying spermatogenic arrests in men with non-obstructive azoospermia. Cell Cycle, 22:1021-1061, Feb 2023. URL: https://doi.org/10.1080/15384101.2023.2171544, doi:10.1080/15384101.2023.2171544. This article has 15 citations and is from a peer-reviewed journal.

16. (llano2023synaptonemalcomplexin media 4701f75e): Elena Llano and Alberto M. Pendás. Synaptonemal complex in human biology and disease. Cells, 12:1718, Jun 2023. URL: https://doi.org/10.3390/cells12131718, doi:10.3390/cells12131718. This article has 19 citations.

17. (llano2023synaptonemalcomplexin media c1bf6f79): Elena Llano and Alberto M. Pendás. Synaptonemal complex in human biology and disease. Cells, 12:1718, Jun 2023. URL: https://doi.org/10.3390/cells12131718, doi:10.3390/cells12131718. This article has 19 citations.

## Artifacts

- [Edison artifact artifact-00](meiotic_prophase_failure-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](meiotic_prophase_failure-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](meiotic_prophase_failure-deep-research-falcon_artifacts/artifact-02.md)
