---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T05:35:22.300395'
end_time: '2026-03-06T05:53:54.445096'
duration_seconds: 1112.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Erdheim-Chester Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Erdheim-Chester Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Erdheim-Chester Disease**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


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

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Erdheim-Chester Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Erdheim-Chester Disease**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


# Erdheim–Chester Disease (ECD) Pathophysiology — Research Report (2023–2024 emphasis)

## 0) Disease identifiers and scope
ECD is a rare non-Langerhans cell histiocytosis/histiocytic neoplasm characterized by xanthogranulomatous tissue infiltration by foamy histiocytes and variable fibrosis, producing multisystem disease with prominent skeletal and CNS involvement. (prabhakaran2023erdheimchesterdiseasewith pages 1-2, benson2023erdheimchesterdisease pages 3-4)

*Identifiers.* The Open Targets disease query returns an EFO identifier for ECD (EFO_1000926) but no curated disease–target associations in that resource snapshot. (vicario2024mechanismofneurodegeneration pages 1-4)

## 1) Key concepts and definitions (current understanding)

### 1.1 ECD as a clonal inflammatory myeloid neoplasm
Contemporary reviews and case-based summaries describe ECD as a clonal histiocytic process with characteristic lesional histology and immunophenotype. Lesions show “sheets of bland histiocytes…often with Touton giant cells” with background fibrosis and reactive lymphoplasmacytic inflammation. (prabhakaran2023erdheimchesterdiseasewith pages 1-2)

The immunophenotype supports macrophage/histiocyte lineage (e.g., CD68+, CD163+, factor XIIIa+) and lack of Langerhans markers (CD1a−, langerin−). (prabhakaran2023erdheimchesterdiseasewith pages 1-2, wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)

### 1.2 Hallmark oncogenic signaling: MAPK (MAP-ERK) and PI3K–AKT
Recent syntheses emphasize that ECD pathogenesis is dominated by constitutive signaling through the MAPK axis (MAP-ERK/RAF–MEK–ERK) and, in subsets, PI3K–AKT. A 2024 ECD-focused review states that “MAP kinase and PI3K-AKT pathway somatic mutations and/or fusion genes play significant roles in disease pathogenesis.” (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)

Recurrent driver alterations affect MAPK signaling: “activating mutations involving the MAPK pathway including BRAF, ARAF, N/KRAS, and MEK.” (prabhakaran2023erdheimchesterdiseasewith pages 1-2)

### 1.3 Dual neoplastic–inflammatory biology (cytokine/chemokine circuits)
Mechanistic review excerpts emphasize that lesions can behave as inflammatory niches: a “cytokine storm” is described with high IL-1, IL-6 and TNF-α, along with chemokines (CCL2, CCL4, CCL5, CCL19) and corresponding receptors (CCR1/2/3/5/7), supporting autocrine/paracrine recruitment and activation of monocytes/macrophages. (stefanoni2023dissectingandharnessing pages 20-24)

## 2) Core pathophysiology: dysregulated pathways and cellular processes

### 2.1 Initiation: somatic driver acquisition in myeloid lineage cells
ECD is strongly linked to somatic activating mutations in the MAPK pathway; BRAFV600E is reported in ~60% of cases in a 2023 Acta Haematologica review/case report. (prabhakaran2023erdheimchesterdiseasewith pages 1-2)

A 2024 review frames ECD within clonal hematopoiesis biology by highlighting clonal hematopoiesis–related mutations (e.g., TET2) detected in monocytes and the frequent coexistence of myeloid neoplasms, supporting a model in which mutated hematopoietic progenitors/monocytes seed tissues and differentiate into lesional histiocytes. (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9, wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)

### 2.2 Propagation: tissue infiltration, foam cell phenotype, fibrosis
At the tissue level, ECD lesions are characterized by foamy/xanthomatous histiocytes and fibrosis. (prabhakaran2023erdheimchesterdiseasewith pages 1-2, wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)

Experimental/clinical-pathology–oriented discussion also links monocyte programming and lipid handling to foam-cell differentiation: serum-treated monocytes can differentiate into foam cells in vitro, and tissue-specific signals can generate pathological monocyte subpopulations. (silveira2023erdheimchesterdiseaseafter pages 4-5)

### 2.3 Inflammation as an engine of lesion maintenance and organ damage
Inflammatory cytokines and chemokines appear to be major effectors and amplifiers. The cytokine/chemokine network described above (IL-1/IL-6/TNF-α; CCL2/4/5/19 with CCR1/2/3/5/7) provides a mechanistic basis for sustained myeloid recruitment/activation and systemic inflammatory symptoms in some patients. (stefanoni2023dissectingandharnessing pages 20-24)

### 2.4 CNS-specific mechanism (2024 development): clonal inflammatory microglia and neurodegeneration
A 2024 bioRxiv preprint provides a mechanistic framework for neurodegeneration in histiocytoses including ECD: pervasive “PU.1+ microglia mutant clones” (e.g., BRAFV600E) across the brain correlate with microgliosis, reactive astrocytosis, and neuronal loss, with a predilection for grey nuclei of the rhombencephalon/posterior fossa structures. (vicario2024mechanismofneurodegeneration pages 1-4)

Transcriptomic signatures emphasize inflammatory/phagocytic programs (e.g., IL1b, Cybb, complement and phagocytic receptors) and a neurotoxic astrocyte response involving “JAK-STAT signaling.” (vicario2024mechanismofneurodegeneration pages 9-11, vicario2024mechanismofneurodegeneration pages 11-13)

Importantly, this work also suggests a therapeutic vulnerability distinct from MAPK inhibition: CSF1R inhibition (PLX5622) depleted mutant microglia and limited neuronal loss in mouse models. (vicario2024mechanismofneurodegeneration pages 1-4, vicario2024mechanismofneurodegeneration pages 40-43)

## 3) Key molecular players (genes/proteins), chemicals, cell types, and anatomical sites

### 3.1 Genes/proteins implicated (drivers and mechanistic nodes)
Evidence-supported genes include:
- **BRAF** (BRAFV600E): present in approximately **60%** of cases in a 2023 clinicopathologic overview; also described as present in “more than one-half” of tissue samples in a 2023 neuroradiology review. (prabhakaran2023erdheimchesterdiseasewith pages 1-2, benson2023erdheimchesterdisease pages 3-4)
- **MAP2K1 (MEK1)**, **KRAS**, **NRAS**, **ARAF**, **RAF1**, and **PIK3CA** as recurrently implicated nodes across MAPK/PI3K–AKT signaling. (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9, prabhakaran2023erdheimchesterdiseasewith pages 1-2)
- **TET2** (clonal hematopoiesis model/association) and other clonal hematopoiesis-related mutations detected in peripheral monocytes in ECD. (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9, wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)
- **CSF1R** as a functional dependency/therapeutic target in microglia-driven neurodegeneration models associated with BRAFV600E histiocytosis. (vicario2024mechanismofneurodegeneration pages 40-43)

A 2024 review also discusses reported mutation–phenotype associations (organ tropism): BRAF mutations linked to neurologic disease (183/273, 67%), KRAS/NRAS linked to cutaneous and pleural involvement, and MAP2K1 linked to peritoneal/retroperitoneal disease (4/11, 36.4%). (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)

### 3.2 Chemical entities / therapeutics relevant to mechanisms
Mechanism-linked drugs include:
- **Vemurafenib** (BRAF inhibitor): identified as the first FDA-approved agent for BRAF p.V600E ECD. (benson2023erdheimchesterdisease pages 3-4)
- **Cobimetinib** (MEK inhibitor): reported as FDA-approved in 2022 for ECD regardless of mutation status. (benson2023erdheimchesterdisease pages 3-4)
- **Trametinib** (MEK inhibitor): demonstrated activity in multicenter real-world data (see §6). (aaroe2023successfultreatmentof pages 1-2)
- **Interferon-α** and other conventional/immunomodulatory therapies discussed as historical standards/alternatives when targeted agents are unavailable or unsuitable. (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)
- **PLX5622** (CSF1R inhibitor): preclinical microglial depletion and neuroprotection in BRAFV600E microglia models. (vicario2024mechanismofneurodegeneration pages 40-43)

### 3.3 Cell types primarily affected
Primary/implicated cell types include:
- **Foamy macrophages/histiocytes** forming the lesional infiltrate (CD68+/CD163+/factor XIIIa+), with Touton giant cells. (prabhakaran2023erdheimchesterdiseasewith pages 1-2)
- **Circulating monocytes** and possibly earlier hematopoietic progenitors in clonal hematopoiesis-linked models. (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
- **Microglia** as clonal inflammatory populations implicated in neurodegenerative manifestations. (vicario2024mechanismofneurodegeneration pages 1-4)
- **Astrocytes** as reactive/neurotoxic responders (JAK–STAT axis). (vicario2024mechanismofneurodegeneration pages 11-13)

### 3.4 Anatomical locations and organ involvement
A 2023 neuroradiology review highlights common CNS-related manifestations: diabetes insipidus and posterior fossa/cerebellar dysfunction, pituitary stalk enlargement and loss of posterior pituitary signal, orbital masses, and long-bone lesions. (benson2023erdheimchesterdisease pages 3-4)

Classic multisystem involvement includes bone (symmetric osteosclerosis), retroperitoneal/perinephric (“hairy kidney”), periaortic (“coated aorta”), and cardiovascular involvement that can be life-threatening. (prabhakaran2023erdheimchesterdiseasewith pages 1-2, wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)

A comparative imaging/clinical summary table is available in Benson et al. 2023. (benson2023erdheimchesterdisease media d7f4a8dc)

## 4) Biological processes disrupted (GO-oriented narrative)
Evidence-supported disrupted processes include:
- MAPK/ERK signaling and upstream RAF–MEK activation due to recurrent driver mutations/fusions. (prabhakaran2023erdheimchesterdiseasewith pages 1-2, wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
- PI3K–AKT signaling in subsets. (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
- Cytokine production and inflammatory response (IL-1, IL-6, TNF-α). (stefanoni2023dissectingandharnessing pages 20-24)
- Chemokine-mediated leukocyte chemotaxis/monocyte recruitment (CCL2/4/5/19 with CCR1/2/3/5/7). (stefanoni2023dissectingandharnessing pages 20-24)
- Phagocytosis/complement activation and oxidative stress programs in clonal inflammatory microglia; associated reactive astrocyte JAK–STAT signaling. (vicario2024mechanismofneurodegeneration pages 9-11, vicario2024mechanismofneurodegeneration pages 11-13)

## 5) Cellular components (where key processes occur)
Mechanistic evidence points to multiple cellular compartments:
- **Extracellular space**: cytokines/chemokines and soluble mediators driving paracrine circuits. (stefanoni2023dissectingandharnessing pages 20-24)
- **Plasma membrane**: chemokine receptors (CCR family) and cytokine receptor signaling; CSF1R dependency in microglia models. (stefanoni2023dissectingandharnessing pages 20-24, vicario2024mechanismofneurodegeneration pages 40-43)
- **Lysosomal/phagolysosomal system**: cathepsins/lysozyme expression and phagocytic programs in inflammatory microglia. (vicario2024mechanismofneurodegeneration pages 9-11)

## 6) Disease progression model (sequence of events)
A knowledge-base–ready progression model supported by 2023–2024 sources is:
1. **Somatic MAPK-pathway activation** (most commonly BRAFV600E; other MAPK/PI3K alterations) in myeloid lineage cells. (prabhakaran2023erdheimchesterdiseasewith pages 1-2, wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
2. **Systemic dissemination/trafficking** of mutated monocytes (and/or progenitors) with differentiation into tissue histiocytes; in some models this occurs on a background of **clonal hematopoiesis** (e.g., TET2-mutant clones). (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
3. **Tissue infiltration and remodeling**: foamy histiocyte accumulation, fibrosis, and xanthogranulomatous lesions in target organs (bone, retroperitoneum, large vessels, heart, CNS). (prabhakaran2023erdheimchesterdiseasewith pages 1-2, wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)
4. **Self-reinforcing inflammatory circuits** with cytokine/chemokine production and myeloid recruitment sustaining lesions and systemic inflammation. (stefanoni2023dissectingandharnessing pages 20-24)
5. **Organ-specific complications**, including CNS endocrine dysfunction (diabetes insipidus) and, in a subset, neurodegeneration potentially driven by **clonal inflammatory microglia** with a long preclinical phase. (benson2023erdheimchesterdisease pages 3-4, vicario2024mechanismofneurodegeneration pages 1-4)

## 7) Phenotypic manifestations and mechanistic links
Key clinical phenotypes and mechanistic correlates:
- **Diabetes insipidus**: linked to pituitary stalk/posterior pituitary involvement and CNS infiltration. (benson2023erdheimchesterdisease pages 3-4)
- **Cerebellar dysfunction/posterior fossa disease**: aligns with preferential rhombencephalon/posterior fossa involvement described in imaging reviews and microglia-driven neurodegeneration models. (benson2023erdheimchesterdisease pages 3-4, vicario2024mechanismofneurodegeneration pages 1-4)
- **Symmetric long-bone osteosclerosis** (“hot knees”): consistent with bone-tropic xanthogranulomatous histiocytic infiltration; osteoblast-derived M-CSF may contribute to myeloid differentiation in the bone niche (hypothesis supported by cited discussion). (prabhakaran2023erdheimchesterdiseasewith pages 1-2, silveira2023erdheimchesterdiseaseafter pages 4-5)
- **Perinephric (‘hairy kidney’) and periaortic (‘coated aorta’) infiltration**: classic fibrotic/infiltrative manifestations consistent with chronic histiocytic infiltration and fibrosis. (prabhakaran2023erdheimchesterdiseasewith pages 1-2)

## 8) Recent developments (2023–2024 priority)

### 8.1 2023–2024 mechanistic advances: trained immunity / immunometabolism framing
A 2023 mechanistic review excerpt explicitly frames ECD as an inflammatory myeloid neoplasm with paracrine inflammatory activation (“cytokine storm”) and chemokine receptor axes that could be therapeutically modulated beyond MAPK inhibition. (stefanoni2023dissectingandharnessing pages 20-24)

### 8.2 2024 CNS neurodegeneration model: microglial clonality and CSF1R targeting
The 2024 Vicario et al. preprint is notable for shifting part of the CNS complication narrative toward **microglia-intrinsic clonal disease** (BRAFV600E mutant microglia) and proposing **CSF1R inhibition** as a neuroprotective strategy. (vicario2024mechanismofneurodegeneration pages 1-4, vicario2024mechanismofneurodegeneration pages 40-43)

## 9) Current applications and real-world implementation

### 9.1 Targeted therapy is now the dominant mechanism-based approach
A 2024 review emphasizes that molecular profiling has “shape[d] the landscape of targetable treatment options” in ECD and notes FDA approvals of vemurafenib (2017; BRAFV600E) and cobimetinib (2022; mutation-agnostic). (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2, benson2023erdheimchesterdisease pages 3-4)

### 9.2 2023 multicenter real-world outcomes: trametinib
In a multicenter retrospective analysis (Blood Advances; July 2023), trametinib was used in 26 adults with non-Langerhans histiocytoses (17 ECD). Among 17 evaluable patients, the **overall response rate was 71%**; responses were observed even without detectable BRAFV600E (8/11, 73%). Median follow-up was 23 months and **3-year overall survival was 90.1%**; rash occurred in 27% as a common toxicity, and many patients required lower-than-standard dosing (often 0.5–1.0 mg daily). (aaroe2023successfultreatmentof pages 1-2, aaroe2023successfultreatmentof pages 3-4)

### 9.3 2024 targeted-therapy implementation: Benelux real-world cohort
A 2024 real-world cohort of histiocytic neoplasms treated with BRAF/MEK inhibitors reported objective responses in **25/27 (93%)** patients with multisystemic and/or solid lesions (mixed diagnoses; not ECD-only). The authors highlight rapid relapse when stopping targeted therapy and persistence of BRAFV600E mutant alleles in blood despite therapy. (kemps2024realworldexperiencewith pages 8-10)

## 10) Expert synthesis and analysis (authoritative perspectives)
A consistent expert-level synthesis across 2023–2024 sources is that ECD sits at the intersection of **clonal oncogenic signaling** (MAPK/PI3K) and **tissue-destructive inflammation**. Driver mutations likely initiate disease, but clinical behavior (fibrosis, organ tropism, systemic inflammation, and neurodegeneration) appears to involve non-cell-autonomous circuits (cytokines/chemokines; reactive astrocytes) and/or lineage-specific clones (microglia) that may not be fully suppressed by standard MAPK inhibition. (stefanoni2023dissectingandharnessing pages 20-24, vicario2024mechanismofneurodegeneration pages 1-4)

## 11) Statistics and data (selected, evidence-backed)
- **BRAFV600E prevalence:** ~60% of ECD cases (clinicopathologic summary). (prabhakaran2023erdheimchesterdiseasewith pages 1-2)
- **Trametinib outcomes (2023 multicenter):** ORR 71% (12/17); 3-year OS 90.1%; responses in BRAF V600E-negative disease 73% (8/11). (aaroe2023successfultreatmentof pages 1-2, aaroe2023successfultreatmentof pages 3-4)
- **Real-world targeted therapy (2024 mixed histiocytoses):** objective responses 93% (25/27) in multisystemic/solid lesions. (kemps2024realworldexperiencewith pages 8-10)
- **Mutation–organ association examples (reviewed data):** BRAF associated with neurologic disease (183/273, 67%); MAP2K1 associated with peritoneal/retroperitoneal lesions (4/11, 36.4%). (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)

## 12) Knowledge-base artifacts (structured)

| Mechanistic Theme | Key Molecules (HGNC) | Cell Types (CL) | Tissues/Organs (UBERON) | Supporting Evidence & Quantitative Data | Key Sources (Year) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MAPK & PI3K Pathway Activation** | *BRAF* (V600E), *MAP2K1*, *KRAS*, *NRAS*, *ARAF*, *RAF1*, *PIK3CA* | Histiocyte, Macrophage, Monocyte | Bone, CNS, Heart (pericardium), Retroperitoneum, Kidney, Aorta | *BRAF* V600E present in >50–60% of cases (lang2023mutationpedigreeand pages 4-5, prabhakaran2023erdheimchesterdiseasewith pages 1-2); *MAP2K1* linked to retroperitoneal disease (36.4%) (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9); Targeted therapy (vemurafenib/cobimetinib) response rates >88% (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9). | Wilcox et al. (2024), Prabhakaran et al. (2023), Lang et al. (2023) |
| **Clonal Hematopoiesis & Myeloid Neoplasms** | *TET2*, *DNMT3A*, *ASXL1*, *BRAF* | Hematopoietic stem cell, Monocyte, Myeloid progenitor | Bone marrow, Peripheral blood | High frequency of concomitant myeloid neoplasms (CMML, MDS, MPN) (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2); *TET2*-mutant clones may precede *BRAF*-mutant histiocytosis (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9); Shared *NRAS*/*IDH2* mutations in ECD and myeloid malignancy (prabhakaran2023erdheimchesterdiseasewith pages 6-6). | Wilcox et al. (2024), Prabhakaran et al. (2023), Silveira et al. (2023) |
| **Inflammatory Milieu & Cytokine Storm** | *IL1B*, *IL6*, *TNF*, *CCL2*, *CCL4*, *CCL5*, *CCL19*, *CCR1*, *CCR2*, *CSF1* (M-CSF) | Macrophage (foamy), T cell, Osteoblast | Systemic (serum), Lesional tissue (histiocytic infiltrates) | Lesions show "cytokine storm" with high IL-1, IL-6, TNF-$\alpha$ (stefanoni2023dissectingandharnessing pages 20-24); Autocrine/paracrine loops drive monocyte recruitment (stefanoni2023dissectingandharnessing pages 20-24); Osteoblasts produce M-CSF supporting differentiation (silveira2023erdheimchesterdiseaseafter pages 4-5). | Stefanoni (2023), Silveira et al. (2023) |
| **Neurodegeneration (Clonal Microglia)** | *BRAF*, *CSF1R*, *IL1B*, *CYBB* (NADPH oxidase), *C4B* | Microglial cell, Astrocyte, Neuron | Brainstem (pons, medulla), Cerebellum, Hippocampus | *BRAF* V600E-mutant microglial clones drive neurodegeneration via inflammatory/phagocytic signature (vicario2024mechanismofneurodegeneration pages 1-4); CSF1R inhibition depletes mutant microglia and limits neuronal loss in models (vicario2024mechanismofneurodegeneration pages 9-11). | Vicario et al. (2024), Benson et al. (2023) |
| **Therapeutic Targeting** | *BRAF*, *MEK1*/*MEK2* (Map2k1/2), *CSF1R* | -- | -- | Trametinib (MEK inhibitor) ORR 71% in non-LCH (multicenter) (aaroe2023successfultreatmentof pages 1-2); Efficacy seen in *BRAF* V600E negative cases (73% response) (aaroe2023successfultreatmentof pages 3-4); CSF1R inhibition proposed for neurodegenerative phenotype (vicario2024mechanismofneurodegeneration pages 11-13). | Aaroe et al. (2023), Kemps et al. (2024), Vicario et al. (2024) |


*Table: This table synthesizes key mechanistic themes in ECD, identifying driver mutations, involved cell types and tissues, and supporting quantitative evidence from 2023–2024 research.*

```
disease:
  name: Erdheim-Chester disease
  MONDO: unavailable
  EFO: unavailable
  category: Complex (benson2023erdheimchesterdisease pages 3-4, wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)

genes:
  - hgnc: BRAF
    role: MAPK pathway driver (V600E; >50–60% of cases) (prabhakaran2023erdheimchesterdiseasewith pages 1-2, benson2023erdheimchesterdisease pages 3-4, wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - hgnc: MAP2K1
    role: MAPK pathway driver (MEK1; organ tropism to peritoneal/retroperitoneal reported) (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - hgnc: KRAS
    role: MAPK pathway driver (organ tropism to cutaneous/pleural reported) (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - hgnc: NRAS
    role: MAPK pathway driver; shared mutations with concomitant myeloid malignancy (prabhakaran2023erdheimchesterdiseasewith pages 1-2, prabhakaran2023erdheimchesterdiseasewith pages 6-6)
  - hgnc: ARAF
    role: MAPK pathway driver (prabhakaran2023erdheimchesterdiseasewith pages 1-2)
  - hgnc: RAF1
    role: MAPK pathway gene implicated (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - hgnc: PIK3CA
    role: PI3K–AKT pathway gene implicated (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - hgnc: CSF1R
    role: Microglial survival/proliferation axis; CSF1R inhibition depletes mutant microglia and limits neuronal loss (vicario2024mechanismofneurodegeneration pages 9-11, vicario2024mechanismofneurodegeneration pages 11-13, vicario2024mechanismofneurodegeneration pages 40-43)

GO:
  biological_process:
    - MAPK cascade / ERK1 and ERK2 cascade (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9, benson2023erdheimchesterdisease pages 3-4)
    - PI3K–AKT signaling (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
    - Cytokine production (IL-1, IL-6, TNF-alpha) (stefanoni2023dissectingandharnessing pages 20-24)
    - Chemotaxis/monocyte recruitment (CCL2/4/5/19–CCR1/2/3/5/7 axes) (stefanoni2023dissectingandharnessing pages 20-24)
    - Microglial activation and inflammatory response (IL1B, CYBB; complement; phagocytic receptors) (vicario2024mechanismofneurodegeneration pages 9-11, vicario2024mechanismofneurodegeneration pages 1-4)
    - JAK–STAT signaling in reactive astrocytes (vicario2024mechanismofneurodegeneration pages 9-11)
    - Phagocytosis (vicario2024mechanismofneurodegeneration pages 9-11)
  cellular_component:
    - Extracellular region/space (cytokines, complement) (stefanoni2023dissectingandharnessing pages 20-24, vicario2024mechanismofneurodegeneration pages 9-11)
    - Plasma membrane (chemokine/cytokine receptors) (stefanoni2023dissectingandharnessing pages 20-24)
    - Lysosome (cathepsins; microglial phagolysosomal activity) (vicario2024mechanismofneurodegeneration pages 9-11)
    - Cytosol/nucleus (MAPK signaling effectors) (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)

cell_types:
  - Macrophage/histiocyte (foamy histiocytes; CD68+/CD163+) (prabhakaran2023erdheimchesterdiseasewith pages 1-2)
  - Monocyte (circulating; potential mutation carriers) (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - Dendritic cell (differentiation involvement) (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - Microglial cell (clonal BRAFV600E-mutant; neurodegeneration driver) (vicario2024mechanismofneurodegeneration pages 1-4)
  - Astrocyte (reactive; neurotoxic response) (vicario2024mechanismofneurodegeneration pages 9-11)
  - Neuron (target of microglia-mediated neurodegeneration) (vicario2024mechanismofneurodegeneration pages 1-4)

anatomical_locations:
  - Long bones (symmetric diaphyseal osteosclerosis) (benson2023erdheimchesterdisease pages 3-4)
  - Central nervous system (posterior fossa/brainstem; cerebellum; hippocampus) (benson2023erdheimchesterdisease pages 3-4, vicario2024mechanismofneurodegeneration pages 1-4)
  - Pituitary stalk/posterior pituitary (stalk thickening; DI) (benson2023erdheimchesterdisease pages 3-4)
  - Orbit (orbital masses; exophthalmos) (benson2023erdheimchesterdisease pages 3-4)
  - Retroperitoneum/perinephric tissue ("hairy kidney") (benson2023erdheimchesterdisease pages 3-4, wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9)
  - Aorta/periaortic tissue ("coated aorta") (benson2023erdheimchesterdisease pages 3-4)
  - Heart/cardiac tissue (life-threatening involvement) (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)

phenotypes_HPO:
  - Diabetes insipidus (neurohypophyseal) (benson2023erdheimchesterdisease pages 3-4)
  - Cerebellar ataxia/dysfunction (benson2023erdheimchesterdisease pages 3-4)
  - Exophthalmos/proptosis (benson2023erdheimchesterdisease pages 3-4)
  - Symmetric long-bone osteosclerosis (benson2023erdheimchesterdisease pages 3-4)

chemicals_drugs_CHEBI:
  - Vemurafenib (BRAFV600E inhibitor; FDA-approved for ECD) (benson2023erdheimchesterdisease pages 3-4)
  - Dabrafenib (BRAFV600E inhibitor) (benson2023erdheimchesterdisease pages 3-4, kemps2024realworldexperiencewith pages 8-10)
  - Cobimetinib (MEK inhibitor; FDA-approved for ECD) (benson2023erdheimchesterdisease pages 3-4)
  - Trametinib (MEK inhibitor; ORR 71% in non-LCH including ECD) (aaroe2023successfultreatmentof pages 1-2, aaroe2023successfultreatmentof pages 3-4)
  - PLX5622 (CSF1R inhibitor; preclinical microglial depletion) (vicario2024mechanismofneurodegeneration pages 9-11, vicario2024mechanismofneurodegeneration pages 40-43)
```


*Code_block: YAML-style, citation-backed annotations for Erdheim–Chester disease covering genes, processes, cell types, anatomy, phenotypes, and relevant drugs. Useful for populating structured disease knowledge bases with 2023–2024 evidence.*

## 13) Evidence items (PMID where available)
The retrieved full texts in this run did not include PubMed ID (PMID) strings in the captured excerpts/metadata; therefore PMID mapping cannot be asserted from tool evidence alone without external lookup. The report instead provides DOIs/URLs and publication months/years as available in the retrieved records. (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2, benson2023erdheimchesterdisease pages 3-4, aaroe2023successfultreatmentof pages 1-2, kemps2024realworldexperiencewith pages 8-10, prabhakaran2023erdheimchesterdiseasewith pages 1-2, vicario2024mechanismofneurodegeneration pages 1-4)

## 14) Key source list (with URLs and dates)
- Wilcox SR, Reynolds SB, Ahmed AZ. *Cancers* (Mar 2024). https://doi.org/10.3390/cancers16071299 (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2)
- Aaroe A, et al. *Blood Advances* (Jul 2023). https://doi.org/10.1182/bloodadvances.2022009013 (aaroe2023successfultreatmentof pages 1-2)
- Kemps PG, et al. *Blood Neoplasia* (Sep 2024). https://doi.org/10.1016/j.bneo.2024.100023 (kemps2024realworldexperiencewith pages 8-10)
- Benson JC, et al. *AJNR* (Mar 2023). https://doi.org/10.3174/ajnr.a7832 (benson2023erdheimchesterdisease pages 3-4)
- Prabhakaran N, et al. *Acta Haematologica* (Feb 2023). https://doi.org/10.1159/000528550 (prabhakaran2023erdheimchesterdiseasewith pages 1-2)
- Vicario R, et al. *bioRxiv* preprint (Jul 2024). https://doi.org/10.1101/2024.07.30.605867 (vicario2024mechanismofneurodegeneration pages 1-4)

## Figure/Table evidence
- Comparative table of clinical/CNS imaging features for ECD (Benson et al., 2023). (benson2023erdheimchesterdisease media d7f4a8dc)


References

1. (prabhakaran2023erdheimchesterdiseasewith pages 1-2): Nitya Prabhakaran, George Jour, Arjun Balar, and Nicholas Ward. Erdheim-chester disease with braf v600e mutation and a concomitant myeloid malignancy sharing nras and idh2 mutations. Acta Haematologica, 146:245-251, Feb 2023. URL: https://doi.org/10.1159/000528550, doi:10.1159/000528550. This article has 1 citations and is from a peer-reviewed journal.

2. (benson2023erdheimchesterdisease pages 3-4): J.C. Benson, R. Vaubel, B.A. Ebne, I.T. Mark, M. Peris Celda, C.C. Hook, W.O. Tobin, and C. Giannini. Erdheim-chester disease. American Journal of Neuroradiology, 44:505-510, Mar 2023. URL: https://doi.org/10.3174/ajnr.a7832, doi:10.3174/ajnr.a7832. This article has 24 citations and is from a peer-reviewed journal.

3. (vicario2024mechanismofneurodegeneration pages 1-4): Rocio Vicario, Stamatina Fragkogianni, Maria Pokrovskii, Carina Mayer, Estibaliz Lopez-Rodrigo, Yang Hu, Masato Ogishi, Araitz Alberdi, Ann Baako, Oyku Ay, Isabelle Plu, Véronique Sazdovitch, Sebastien Heritier, Fleur Cohen-Aubart, Natalia Shor, Makoto Miyara, Florence Nguyen-Khac, Agnes Viale, Ahmed Idbaih, Zahir Amoura, Marc K. Rosenblum, Haochen Zhang, Elias-Ramzey Karnoub, Palash Sashittal, Akhil Jakatdar, Christine A. Iacobuzio-Donahue, Omar Abdel-Wahab, Viviane Tabar, Nicholas D. Socci, Olivier Elemento, Eli L Diamond, Bertrand Boisson, Jean-Laurent Casanova, Danielle Seilhean, Julien Haroche, Jean Donadieu, and Frederic Geissmann. Mechanism of neurodegeneration mediated by clonal inflammatory microglia. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.30.605867, doi:10.1101/2024.07.30.605867. This article has 6 citations.

4. (wilcox2024erdheim–chesterdiseaseinvestigating pages 1-2): Sabrina R. Wilcox, Samuel B. Reynolds, and Asra Z. Ahmed. Erdheim–chester disease: investigating the correlation between targeted treatment therapy and disease outcomes. Cancers, 16:1299, Mar 2024. URL: https://doi.org/10.3390/cancers16071299, doi:10.3390/cancers16071299. This article has 2 citations.

5. (stefanoni2023dissectingandharnessing pages 20-24): D Stefanoni. Dissecting and harnessing maladaptive trained immunity and paracrine interactions in erdheim-chester disease treatment. Unknown journal, 2023.

6. (wilcox2024erdheim–chesterdiseaseinvestigating pages 8-9): Sabrina R. Wilcox, Samuel B. Reynolds, and Asra Z. Ahmed. Erdheim–chester disease: investigating the correlation between targeted treatment therapy and disease outcomes. Cancers, 16:1299, Mar 2024. URL: https://doi.org/10.3390/cancers16071299, doi:10.3390/cancers16071299. This article has 2 citations.

7. (silveira2023erdheimchesterdiseaseafter pages 4-5): Lara de Holanda Jucá Silveira, Cleto Dantas Nogueira, Carolina Teixeira Costa, Priscila Timbó de Azevedo, Silvia Maria Meira Magalhães, and Ronald Feitosa Pinheiro. Erdheim-chester disease after essential thrombocythemia: coincidence or not? Jan 2023. URL: https://doi.org/10.1016/j.htct.2021.01.013, doi:10.1016/j.htct.2021.01.013. This article has 1 citations.

8. (vicario2024mechanismofneurodegeneration pages 9-11): Rocio Vicario, Stamatina Fragkogianni, Maria Pokrovskii, Carina Mayer, Estibaliz Lopez-Rodrigo, Yang Hu, Masato Ogishi, Araitz Alberdi, Ann Baako, Oyku Ay, Isabelle Plu, Véronique Sazdovitch, Sebastien Heritier, Fleur Cohen-Aubart, Natalia Shor, Makoto Miyara, Florence Nguyen-Khac, Agnes Viale, Ahmed Idbaih, Zahir Amoura, Marc K. Rosenblum, Haochen Zhang, Elias-Ramzey Karnoub, Palash Sashittal, Akhil Jakatdar, Christine A. Iacobuzio-Donahue, Omar Abdel-Wahab, Viviane Tabar, Nicholas D. Socci, Olivier Elemento, Eli L Diamond, Bertrand Boisson, Jean-Laurent Casanova, Danielle Seilhean, Julien Haroche, Jean Donadieu, and Frederic Geissmann. Mechanism of neurodegeneration mediated by clonal inflammatory microglia. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.30.605867, doi:10.1101/2024.07.30.605867. This article has 6 citations.

9. (vicario2024mechanismofneurodegeneration pages 11-13): Rocio Vicario, Stamatina Fragkogianni, Maria Pokrovskii, Carina Mayer, Estibaliz Lopez-Rodrigo, Yang Hu, Masato Ogishi, Araitz Alberdi, Ann Baako, Oyku Ay, Isabelle Plu, Véronique Sazdovitch, Sebastien Heritier, Fleur Cohen-Aubart, Natalia Shor, Makoto Miyara, Florence Nguyen-Khac, Agnes Viale, Ahmed Idbaih, Zahir Amoura, Marc K. Rosenblum, Haochen Zhang, Elias-Ramzey Karnoub, Palash Sashittal, Akhil Jakatdar, Christine A. Iacobuzio-Donahue, Omar Abdel-Wahab, Viviane Tabar, Nicholas D. Socci, Olivier Elemento, Eli L Diamond, Bertrand Boisson, Jean-Laurent Casanova, Danielle Seilhean, Julien Haroche, Jean Donadieu, and Frederic Geissmann. Mechanism of neurodegeneration mediated by clonal inflammatory microglia. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.30.605867, doi:10.1101/2024.07.30.605867. This article has 6 citations.

10. (vicario2024mechanismofneurodegeneration pages 40-43): Rocio Vicario, Stamatina Fragkogianni, Maria Pokrovskii, Carina Mayer, Estibaliz Lopez-Rodrigo, Yang Hu, Masato Ogishi, Araitz Alberdi, Ann Baako, Oyku Ay, Isabelle Plu, Véronique Sazdovitch, Sebastien Heritier, Fleur Cohen-Aubart, Natalia Shor, Makoto Miyara, Florence Nguyen-Khac, Agnes Viale, Ahmed Idbaih, Zahir Amoura, Marc K. Rosenblum, Haochen Zhang, Elias-Ramzey Karnoub, Palash Sashittal, Akhil Jakatdar, Christine A. Iacobuzio-Donahue, Omar Abdel-Wahab, Viviane Tabar, Nicholas D. Socci, Olivier Elemento, Eli L Diamond, Bertrand Boisson, Jean-Laurent Casanova, Danielle Seilhean, Julien Haroche, Jean Donadieu, and Frederic Geissmann. Mechanism of neurodegeneration mediated by clonal inflammatory microglia. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.30.605867, doi:10.1101/2024.07.30.605867. This article has 6 citations.

11. (aaroe2023successfultreatmentof pages 1-2): Ashley Aaroe, Razelle Kurzrock, Gaurav Goyal, Aaron M. Goodman, Harsh Patel, Gordon Ruan, Gary Ulaner, Jason Young, Ziyi Li, Derek Dustin, Ronald S. Go, Eli L. Diamond, and Filip Janku. Successful treatment of non-langerhans cell histiocytosis with the mek inhibitor trametinib: a multicenter analysis. Jul 2023. URL: https://doi.org/10.1182/bloodadvances.2022009013, doi:10.1182/bloodadvances.2022009013. This article has 38 citations and is from a peer-reviewed journal.

12. (benson2023erdheimchesterdisease media d7f4a8dc): J.C. Benson, R. Vaubel, B.A. Ebne, I.T. Mark, M. Peris Celda, C.C. Hook, W.O. Tobin, and C. Giannini. Erdheim-chester disease. American Journal of Neuroradiology, 44:505-510, Mar 2023. URL: https://doi.org/10.3174/ajnr.a7832, doi:10.3174/ajnr.a7832. This article has 24 citations and is from a peer-reviewed journal.

13. (aaroe2023successfultreatmentof pages 3-4): Ashley Aaroe, Razelle Kurzrock, Gaurav Goyal, Aaron M. Goodman, Harsh Patel, Gordon Ruan, Gary Ulaner, Jason Young, Ziyi Li, Derek Dustin, Ronald S. Go, Eli L. Diamond, and Filip Janku. Successful treatment of non-langerhans cell histiocytosis with the mek inhibitor trametinib: a multicenter analysis. Jul 2023. URL: https://doi.org/10.1182/bloodadvances.2022009013, doi:10.1182/bloodadvances.2022009013. This article has 38 citations and is from a peer-reviewed journal.

14. (kemps2024realworldexperiencewith pages 8-10): Paul G. Kemps, F. J. Sherida H. Woei-A-Jin, Patrick Schöffski, Thomas Tousseyn, Isabelle Vanden Bempt, Friederike A. G. Meyer-Wentrup, Natasja Dors, Natasha K. A. van Eijkelenburg, Marijn A. Scheijde-Vermeulen, Ingrid M. Jazet, Maarten Limper, Margot Jak, Robert M. Verdijk, Marjolein L. Donker, Nick A. de Jonge, Carel J. M. van Noesel, Konnie M. Hebeda, Suzanne van Dorp, Sanne H. Tonino, Jan A. M. van Laar, Cor van den Bos, Astrid G. S. van Halteren, Erik Beckers, Merlijn van den Berg, Cor van den Bos, Godelieve de Bree, Emmeline Buddingh, Kristl Claeys, Paul van Daele, Petra De Haes, Astrid Demandt, Suzanne van Dorp, Liesbeth Hak, Astrid van Halteren, Tim van der Houwen, Margot Jak, Jeroen Kerstens, Arjan Kwakernaak, Jan van Laar, Helen Leavis, Roos Leguit, Arjan van de Loosdrecht, Linde Morsink, Rogier Mous, Max van Noesel, Rimke Oostvogels, Judith Potjewijd, Wouter Plattel, Wilfried Roeloffzen, Abraham Rutgers, Sanne Tonino, Thomas Tousseyn, Rob Verdijk, Joost Vermaat, and Sherida Woei-A-Jin. Real-world experience with targeted therapy in patients with histiocytic neoplasms in the netherlands and in belgium. Sep 2024. URL: https://doi.org/10.1016/j.bneo.2024.100023, doi:10.1016/j.bneo.2024.100023. This article has 11 citations.

15. (lang2023mutationpedigreeand pages 4-5): M Lang, D Zhou, and X Cao. Mutation pedigree and treatment selection of erdheim-chester disease. Unknown journal, 2023.

16. (prabhakaran2023erdheimchesterdiseasewith pages 6-6): Nitya Prabhakaran, George Jour, Arjun Balar, and Nicholas Ward. Erdheim-chester disease with braf v600e mutation and a concomitant myeloid malignancy sharing nras and idh2 mutations. Acta Haematologica, 146:245-251, Feb 2023. URL: https://doi.org/10.1159/000528550, doi:10.1159/000528550. This article has 1 citations and is from a peer-reviewed journal.