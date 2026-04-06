---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T05:35:22.300450'
end_time: '2026-03-06T05:54:54.442445'
duration_seconds: 1172.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Takayasu Arteritis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Takayasu Arteritis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Takayasu Arteritis**.
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
- **Disease Name:** Takayasu Arteritis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Takayasu Arteritis**.
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


## Research Report: Pathophysiology of Takayasu Arteritis (TAK)

### Disease identifiers
- **Disease name:** Takayasu arteritis (TAK)
- **Ontology IDs:** Open Targets disease identifier **EFO_1001857** (returned by Open Targets query) (bhandari2023pathophysiologydiagnosisand pages 2-3)
- **Category:** Autoimmune / immune-mediated large-vessel vasculitis

---

## 1) Core pathophysiology (current understanding)

### 1.1 Lesion anatomy and initiating events
TAK is a granulomatous, pan-arteritis targeting the **aorta and major branches**, with inflammation that appears to **begin around the vasa vasorum and at the medio–adventitial junction**, providing an entry portal for immune cells into the arterial wall (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4). Early lesions feature **mononuclear infiltrates** (lymphocytes, histiocytes/macrophages, plasma cells) and can progress to **granulomatous inflammation with multinucleated giant cells** (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4).

A widely cited mechanistic model implicates **vascular (arterial-wall) dendritic cells** as an initiating sensor population: abnormal vascular dendritic cells with **upregulated Toll-like receptors (TLRs)** can break local immune tolerance and—upon stimulation—release **IL-12, IL-23, and IL-1β**, recruiting vasculitogenic T cells into adventitia/media and initiating granulomatous inflammation (bhandari2023pathophysiologydiagnosisand pages 3-4).

### 1.2 Dominant immune circuits and dysregulated pathways
TAK lesions and systemic immune signatures implicate coordinated activation of innate and adaptive arms, with strong evidence for:

- **Th1 / IFN-γ axis (delayed-type hypersensitivity-like granulomatous inflammation):** Th1- and CD8-associated IFN-γ responses are emphasized in TAK and may be less fully controlled by IL-6 pathway blockade (matsumoto2023changesinthe pages 3-5, matsumoto2023changesinthe pages 1-2).
- **Th17 / IL-23 axis:** IL-6/IL-1β/IL-23-driven Th17 differentiation and increased IL-17 family cytokines correlate with activity and vascular involvement in TAK (guo2024aglimpseinto pages 11-13).
- **TNF-α + IFN-γ → macrophage chemokine (CCL2) → CCR2+ monocyte recruitment → giant cell formation:** TNF-α is supported as a core pathogenic cytokine in experimental LVV/TAK-like models and in mechanistic summaries; TNF-α and IFN-γ can drive macrophage CCL2 production, recruiting CCR2+ monocytes that form multinucleated giant cells (matsumoto2023changesinthe pages 2-3).
- **IL-1 pathway:** Whole-blood transcriptomics and mouse data in large-vessel vasculitis (including TAK-relevant models) support IL-1 signaling as an upstream inflammatory driver capable of activating CD4 T cells and associating with vascular PET activity (matsumoto2023changesinthe pages 2-3, matsumoto2023changesinthe pages 3-5).
- **IL-6 / JAK–STAT signaling:** IL-6 is repeatedly implicated in TAK inflammation and vascular remodeling; IL-6 signaling through JAK–STAT is also linked to pro-fibrotic programs and (newer data) vascular smooth muscle cell (VSMC) senescence (bhandari2023pathophysiologydiagnosisand pages 3-4, fang2024associationbetweenpremature pages 4-5).
- **Notch-1 / mTORC1:** Notch-1 and mTORC1 signaling are described as promoting Th1/Th17 activation and pro-inflammatory T-cell differentiation (bhandari2023pathophysiologydiagnosisand pages 3-4).
- **GM-CSF (CSF2)–linked macrophage activation and tissue injury:** Mechanistic summaries link GM-CSF to macrophage activation, Th1 polarization, neo-angiogenesis, and tissue injury; GM-CSF/chemokine receptor interactions may support destructive macrophage states including MMP9+ macrophages (matsumoto2023changesinthe pages 2-3).
- **Complement pathway enrichment:** Peripheral T-cell transcriptomics and integrated tissue/blood analyses support **complement cascade enrichment** as part of the TAK immunopathogenesis signal (xu2025integratedbulkand pages 1-2).

### 1.3 Vascular remodeling, stenosis, and aneurysm formation
Vascular injury in TAK results from the combination of immune-mediated destruction and maladaptive repair:
- **Intimal hyperplasia / fibrosis → stenosis and occlusion**
- **Medial smooth muscle destruction and elastic lamina damage → wall weakening and aneurysm formation**

A review synthesis describes **reactive intimal fibrosis and intimal hyperplasia**, mural thrombus, neovascularization, and medial smooth muscle destruction as key lesion features, with later “healing” characterized by adventitial fibrosis/scarring (bhandari2023pathophysiologydiagnosisand pages 2-3). Mechanistic review content also highlights macrophage-derived mediators (e.g., MMPs, ROS from inflammatory macrophages) contributing to medial degeneration and aneurysm risk, and growth factors (PDGF/TGF-β) supporting fibrotic remodeling (bhandari2023pathophysiologydiagnosisand pages 3-4).

### 1.4 Newly emphasized vessel-wall cell-intrinsic mechanism (2024): VSMC senescence loop
A major 2024 advance provides direct ex vivo and in vitro mechanistic evidence that **VSMCs are not merely passive targets** but can become active inflammatory amplifiers through a senescence program.

Fang et al. (Annals of the Rheumatic Diseases; **publication date: Nov 2024; DOI: 10.1136/ard-2024-225630; URL: https://doi.org/10.1136/ard-2024-225630**) report that:
- TAK VSMCs show **premature senescence** and produce a **senescence-associated secretory phenotype (SASP)** cytokine milieu (including IL-6, IL-8, IL-1β, CXCL1) (fang2024associationbetweenpremature pages 11-12, fang2024associationbetweenpremature pages 4-5).
- **IL-6 is a critical driver** of VSMC senescence via a **mitochondrial STAT3 (pTyr705) → MFN2 stabilization → mitochondrial hyperfusion/elongation** mechanism (fang2024associationbetweenpremature pages 6-7, fang2024associationbetweenpremature pages 10-11, fang2024associationbetweenpremature pages 12-13).
- **Blocking IL-6 signaling** (IL6R knockdown or anti-IL6R antibody) mitigated PBMC-conditioned-media–induced mitochondrial dysfunction and senescence in VSMC systems (fang2024associationbetweenpremature pages 6-7).
- Ex vivo cultured TAK arterial segments treated with mitochondrial STAT3 or MFN2 inhibitors showed reduced senescence markers and reduced SASP cytokines in supernatants (fang2024associationbetweenpremature pages 11-11).

**Mechanistic schematic (Figure 7C)** supporting this IL-6–mitochondrial STAT3–MFN2–senescence–SASP loop is available as a cropped figure (fang2024associationbetweenpremature media d7f13343).

---

## 2) Key molecular players (genes/proteins), chemical entities, cell types, and anatomical locations

| Mechanistic Axis / Process | Key Molecules (HGNC) | Key Cell Types (CL) | Anatomical Location (UBERON) | Evidence Summary | Key Sources |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dendritic Cell Activation & Tolerance Breach** | *TLR*, *IL12B*, *IL23A*, *IL1B* | Dendritic cells (CL:0000451) | Vasa vasorum / Adventitia (UBERON:0002534) | Abnormal vascular dendritic cells expressing TLRs release IL-12/IL-23 upon stimulation, recruiting T cells and initiating granulomatous inflammation. | (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Th1/Th17 Mediated Inflammation** | *IFNG*, *IL17A*, *IL17F*, *IL23A*, *IL6*, *IL12B* | Th1 cells (CL:0000545), Th17 cells (CL:0000898), CD8+ T cells (CL:0000625) | Tunica media (UBERON:0002535), Adventitia (UBERON:0002534) | Dysregulated Th1 (IFN-γ driven) and Th17 axes sustain inflammation; Th1 dominates chronic lesions while Th17 links to acute activity and vascular remodeling. | (matsumoto2023changesinthe pages 3-5, matsumoto2023changesinthe pages 1-2, guo2024aglimpseinto pages 11-13) |
| **VSMC Senescence & SASP** | *IL6*, *STAT3*, *MFN2*, *CDKN2A* (p16), *CXCL8* (IL8) | Vascular smooth muscle cells (CL:0000359) | Tunica media (UBERON:0002535) | IL-6 induces mitochondrial STAT3 (pTyr705) accumulation which stabilizes MFN2, driving mitochondrial hyperfusion and premature senescence with a pro-inflammatory SASP. | (fang2024associationbetweenpremature pages 9-10, fang2024associationbetweenpremature pages 11-12, fang2024associationbetweenpremature pages 10-11, fang2024associationbetweenpremature pages 12-13, fang2024associationbetweenpremature pages 8-9) |
| **Monocyte Recruitment & Giant Cell Formation** | *TNF*, *IFNG*, *CCL2*, *CCR2* | Monocytes (CL:0000576), Macrophages (CL:0000235), Multinucleated giant cells (CL:0000529) | Tunica media (UBERON:0002535) | TNF-α and IFN-γ stimulate macrophages to produce CCL2, recruiting CCR2+ monocytes that fuse to form granuloma-associated giant cells. | (matsumoto2023changesinthe pages 2-3) |
| **Vascular Fibrosis & Remodeling** | *IL6*, *PDGF*, *TGFB1*, *GPNMB*, *MMP9* | Fibroblasts (CL:0000057), Myofibroblasts (CL:0000186), M2 Macrophages (CL:0000235) | Adventitia (UBERON:0002534), Tunica intima (UBERON:0002536) | M2 macrophages secrete GPNMB and TGF-β; IL-6/JAK-STAT signaling promotes fibroblast activation and collagen deposition leading to intimal hyperplasia and fibrosis. | (matsumoto2023changesinthe pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **mTOR/Notch Signaling** | *MTOR*, *RPTOR* (mTORC1), *NOTCH1* | Th1 cells (CL:0000545), Th17 cells (CL:0000898) | Peripheral blood / Arterial wall | Notch1 signaling drives mTOR hyperactivity which promotes pro-inflammatory T cell differentiation; inhibition limits Th1/Th17 responses. | (bhandari2023pathophysiologydiagnosisand pages 3-4, bhandari2023pathophysiologydiagnosisand pages 9-9) |
| **Complement Activation** | *C1QA*, *C1QB* | CD4+ T cells (CL:0000624), CD8+ T cells (CL:0000625) | Peripheral blood / Aortic tissue | Transcriptomic analysis reveals upregulation of complement cascade genes in peripheral T cells and aortic tissue, suggesting a role in immunopathogenesis. | (xu2025integratedbulkand pages 1-2) |
| **B Cell Response & Ectopic Lymphoid Structures** | *CD20*, *CD40*, *CD80*, *CD86* | B cells (CL:0000236), Plasma cells (CL:0000786), T follicular helper cells (CL:0000889) | Aortic wall / Tertiary lymphoid structures | B cells produce anti-endothelial antibodies and form ectopic lymphoid structures within the aortic wall, supporting local T cell activation. | (bhandari2023pathophysiologydiagnosisand pages 2-3, guo2024aglimpseinto pages 11-13, bhandari2023pathophysiologydiagnosisand pages 3-4) |


*Table: A summary of molecular pathways, cell types, and anatomical sites driving disease progression in Takayasu arteritis.*

### 2.1 Genes/proteins (HGNC symbols; evidence-based highlights)
Key molecules with mechanistic or strong associative evidence in the included sources include:
- **IL6, IL6R, STAT3, MFN2** (VSMC senescence axis; vascular inflammation amplifier loop) (fang2024associationbetweenpremature pages 6-7, fang2024associationbetweenpremature pages 10-11, fang2024associationbetweenpremature pages 4-5).
- **IL12B, IL23A, IL1B, IL17A/IL17F, IFNG, TNF** (T-cell polarization and granulomatous inflammation) (bhandari2023pathophysiologydiagnosisand pages 3-4, guo2024aglimpseinto pages 11-13, matsumoto2023changesinthe pages 2-3).
- **CCL2, CCR2** (monocyte recruitment and giant-cell formation logic) (matsumoto2023changesinthe pages 2-3).
- **CSF2 (GM-CSF), MMP9** (macrophage activation and tissue injury/remodeling; MMP9+ macrophage programs mentioned in mechanistic synthesis) (matsumoto2023changesinthe pages 2-3).
- **Complement cascade genes** (enrichment in peripheral T-cell signatures) (xu2025integratedbulkand pages 1-2).
- **EGR1** (identified as a prominent upregulated transcriptional regulator in integrated blood/tissue analyses) (xu2025integratedbulkand pages 1-2).

**Note on ferroptosis/PTGS2:** A 2024 bioinformatics-centered paper proposes PTGS2 as a hub gene for ferroptosis-related inflammation in TAK arteries, potentially via IL1B–NF-κB signaling; however, the detailed mechanistic evidence from that paper was not retrieved in the available text evidence snippets here, so it is not used as a primary mechanistic anchor in this report (fang2024associationbetweenpremature pages 9-10).

### 2.2 Cell types (CL-style) implicated
- **Vascular dendritic cells** (initiation via TLR and IL-12/23/IL-1β) (bhandari2023pathophysiologydiagnosisand pages 3-4)
- **CD4+ T cells** including **Th1** and **Th17**; **Treg** imbalance noted in molecular profiling summaries (matsumoto2023changesinthe pages 1-2, guo2024aglimpseinto pages 11-13)
- **CD8+ cytotoxic T cells** (perforin/granzyme release described in review synthesis) (bhandari2023pathophysiologydiagnosisand pages 3-4)
- **Macrophages/monocytes** and **multinucleated giant cells** (granulomas; remodeling mediators such as MMPs) (matsumoto2023changesinthe pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4)
- **B cells / plasma cells** (autoantibodies; ectopic lymphoid neogenesis) (guo2024aglimpseinto pages 11-13, bhandari2023pathophysiologydiagnosisand pages 3-4)
- **Vascular smooth muscle cells (VSMCs)** (senescence/SASP inflammatory amplifier; remodeling) (fang2024associationbetweenpremature pages 4-5, fang2024associationbetweenpremature pages 12-13)
- **Fibroblasts and endothelial cells** (fibrosis, neovascularization; described in lesion remodeling frameworks) (bhandari2023pathophysiologydiagnosisand pages 3-4)

### 2.3 Primary anatomical locations (UBERON-style)
- **Aorta and major branches** (core disease territory) (bhandari2023pathophysiologydiagnosisand pages 2-3)
- **Vasa vasorum** (immune entry niche) (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4)
- **Tunica adventitia / media / intima** (granulomas in media; remodeling and intimal hyperplasia) (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4)
- Common clinically assessed territories include **carotid arteries** (ultrasound activity work) (ma2025anovelultrasoundbased pages 1-2, ma2024ultrasoundactivityscore pages 11-14)

---

## 3) Biological processes disrupted (GO-oriented; pathophysiology mapping)

Representative disrupted processes (phrased as GO terms/processes) supported by included sources:
- **Granulomatous inflammation / delayed-type hypersensitivity-like response** (macrophages + giant cells + T cells in arterial wall) (bhandari2023pathophysiologydiagnosisand pages 2-3, matsumoto2023changesinthe pages 2-3)
- **Cytokine-mediated signaling pathway** (IL-6, IL-12/23, IL-1, TNF, IFN-γ) (bhandari2023pathophysiologydiagnosisand pages 3-4, matsumoto2023changesinthe pages 2-3, guo2024aglimpseinto pages 11-13)
- **JAK–STAT signaling** (IL-6 biology; STAT3 axis; IL-6 blockade effects) (matsumoto2023changesinthe pages 1-2, fang2024associationbetweenpremature pages 6-7)
- **Notch signaling** and **TOR/mTOR signaling** (pro-inflammatory T-cell activation) (bhandari2023pathophysiologydiagnosisand pages 3-4)
- **Leukocyte chemotaxis** (CCL2–CCR2 monocyte recruitment into lesions) (matsumoto2023changesinthe pages 2-3)
- **Angiogenesis / neovascularization** (immune ingress and remodeling; also discussed as reduced by some JAK inhibition in model systems) (matsumoto2023changesinthe pages 3-5, bhandari2023pathophysiologydiagnosisand pages 2-3)
- **Extracellular matrix organization and fibrosis** (intimal hyperplasia, adventitial fibrosis) (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4)
- **Cellular senescence** and **mitochondrial fusion/hyperfusion** (VSMC senescence loop) (fang2024associationbetweenpremature pages 6-7, fang2024associationbetweenpremature pages 10-11)
- **Complement activation** (complement cascade enrichment signal) (xu2025integratedbulkand pages 1-2)

---

## 4) Cellular components (where key processes occur)

- **Extracellular space / vessel wall microenvironment:** cytokines (IL-6, IL-12/23, TNF, IFN-γ), chemokines (CCL2), matrix-degrading enzymes (MMPs) orchestrate recruitment and remodeling (matsumoto2023changesinthe pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4).
- **Plasma membrane:** IL-6 receptor and other cytokine receptors mediating signaling (inferred via described IL-6/IL6R biology and anti-IL6R antibody effects) (fang2024associationbetweenpremature pages 6-7).
- **Mitochondria:** IL-6–driven **mitochondrial localization of phosphorylated STAT3 (Tyr705)** and MFN2-dependent mitochondrial hyperfusion in VSMCs (fang2024associationbetweenpremature pages 6-7, fang2024associationbetweenpremature pages 10-11).
- **Nucleus:** downstream transcriptional programs for inflammatory activation and senescence (e.g., senescence markers p16; transcriptional regulators like EGR1 noted in integrated data) (fang2024associationbetweenpremature pages 11-11, xu2025integratedbulkand pages 1-2).

---

## 5) Disease progression model (sequence of events)

A knowledge-base-oriented staging model supported by the sources:

1. **Initiation at vasa vasorum / medio-adventitial junction** with dendritic-cell activation and innate sensing (TLRs) → IL-12/23/IL-1β release → recruitment of T cells and monocytes (bhandari2023pathophysiologydiagnosisand pages 3-4, bhandari2023pathophysiologydiagnosisand pages 2-3).
2. **Amplification by adaptive immunity**: Th1/IFN-γ and Th17/IL-17 programs sustain chronic granulomatous inflammation; cytotoxic CD8 activity may contribute to tissue injury (matsumoto2023changesinthe pages 1-2, guo2024aglimpseinto pages 11-13, bhandari2023pathophysiologydiagnosisand pages 3-4).
3. **Granuloma organization**: macrophage activation and recruitment loops (TNF + IFN-γ → macrophage CCL2 → CCR2+ monocyte recruitment → giant cells) consolidate granulomatous lesions (matsumoto2023changesinthe pages 2-3).
4. **Vessel-wall remodeling and chronic injury**: MMPs/ROS contribute to medial damage; PDGF/TGF-β and fibroblast/myofibroblast activity drive fibrosis/intimal hyperplasia (stenosis), while medial destruction supports aneurysm risk (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4).
5. **Self-sustaining vessel-wall inflammation via senescence** (new evidence): IL-6 drives a mitochondrial STAT3–MFN2 senescence program in VSMCs, producing SASP cytokines that may perpetuate local inflammation even when systemic markers are imperfect (fang2024associationbetweenpremature pages 6-7, fang2024associationbetweenpremature pages 11-11, fang2024associationbetweenpremature media d7f13343).

---

## 6) Phenotypic manifestations (HP-oriented) and mechanistic links

Common clinical phenotypes derive from territory-specific ischemia and structural complications:
- **Arterial stenosis/occlusion** → limb claudication, reduced/absent pulses, bruits, renovascular hypertension, stroke/TIA-like symptoms (supported as consequences of intimal hyperplasia/fibrosis) (bhandari2023pathophysiologydiagnosisand pages 2-3).
- **Aneurysm formation** → risk of rupture/hemorrhage; linked mechanistically to medial destruction/weakening (MMP/ROS and tissue injury programs) (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4).
- **Inflammatory systemic symptoms** (fever, malaise) align with cytokine signaling and systemic acute-phase responses, though these may be discordant from vascular-wall inflammation (as2023currentdiagnosisand pages 2-4).

---

## 7) Recent developments and latest research (prioritizing 2023–2024)

### 7.1 2024 mechanistic advance: IL-6–mitochondrial STAT3–MFN2 in VSMC senescence
The ARD 2024 study provides direct mechanistic evidence connecting IL-6 signaling to mitochondrial remodeling and senescence within VSMCs, with pharmacologic inhibition (mitochondrial STAT3 or MFN2) reducing senescence markers and SASP cytokines ex vivo (fang2024associationbetweenpremature pages 6-7, fang2024associationbetweenpremature pages 11-11).

### 7.2 2023–2024: treatment-response biology supports pathway relevance
Molecular profiling and mechanistic synthesis in LVV emphasize that different immune axes may respond differently to therapies; notably, IL-6 receptor blockade can modify several immune proportions yet leave Th1/CD8 IFN-γ programs comparatively less affected in TAK, which is relevant to relapse biology and persistent remodeling (matsumoto2023changesinthe pages 1-2, matsumoto2023changesinthe pages 3-5).

### 7.3 2023–2024: biomarkers and imaging increasingly treated as part of biology
The monitoring problem is framed as a biological issue: systemic acute-phase reactants can be disconnected from vessel-wall inflammation.
- As stated in a 2023 clinical review: **“ESR and CRP fails in accuracy as disease activity markers.”** (as2023currentdiagnosisand pages 1-2)
- The same source emphasizes that **2022 ACR/EULAR classification now mandates imaging**: **“The new 2022 ACR/EULAR classification criteria for Takayasu arteritis incorporated imaging characteristics as an absolute requirement,”** and **“Modern imaging modalities such as MRI, PET-CT or ultrasound need to be included as a mandatory criterion.”** (as2023currentdiagnosisand pages 1-2)

A meta-analysis summary cited in that review indicates PTX3 outperformed CRP for activity assessment (**pooled sensitivity 78% vs 66%; specificity 85% vs 77%; AUC 0.88 vs 0.75**) (as2023currentdiagnosisand pages 2-4).

---

## 8) Current applications and real-world implementation (monitoring and translation)

### 8.1 Imaging implementation as a surrogate for vessel-wall biology
- CT angiography and MR angiography are widely used for diagnosis and follow-up; PET/CT activity assessments use SUV-based measures and composite vascular activity scores (PETVAS) (as2023currentdiagnosisand pages 2-4).

### 8.2 Real-world ultrasound activity scoring (pathophysiology-linked monitoring)
A prospective ultrasound activity score (ULTRAS) links vessel-wall structural inflammation to clinical activity.
- **ULTRAS performance:** In a training cohort **n=136** with **61% active disease**, ULTRAS cutoff **7** yielded **AUC 0.88 (95% CI 82–94)** for active TAK; combining with ESR improved AUC to **0.91**; validation group **n=30** showed ULTRAS AUC **0.88** and ESR+ULTRAS AUC **0.95** (ma2025anovelultrasoundbased pages 1-2).
- A related 2024 preprint reported the same key operating point (AUC 0.88; cutoff 7) and noted wall thickness reductions over 3–6 months with remission (ma2024ultrasoundactivityscore pages 11-14).

These data support a real-world trend: quantitative imaging features (wall thickness, echogenicity/neovascularization surrogates) are increasingly used as “biological readouts” of disease activity when blood markers are unreliable (ma2025anovelultrasoundbased pages 1-2, as2023currentdiagnosisand pages 2-4).

---

## 9) Expert opinions and analysis (authoritative sources)

- A 2023 International Heart Journal review frames the central limitation in clinical-pathophysiologic monitoring: **no specific biomarker or biopsy** and imperfect correlation of ESR/CRP with vascular inflammation, necessitating imaging-based classification and follow-up (as2023currentdiagnosisand pages 2-4, as2023currentdiagnosisand pages 1-2).
- A 2023 Frontiers in Immunology mini-review emphasizes that residual inflammation and degenerative vessel-wall alterations can persist despite biologics/JAK inhibitors, consistent with the clinical problem of progression to **stenosis and aneurysm** even when systemic inflammation is suppressed (matsumoto2023changesinthe pages 3-5).
- A 2024 IJMS review broadens TAK beyond a purely T-cell disease by emphasizing B-cell dysregulation, autoantibodies, and ectopic lymphoid organization as plausible contributors to disease persistence and progression (guo2024aglimpseinto pages 11-13).

---

## 10) Evidence-backed statistics and recent data points

- **ULTRAS for carotid activity (prospective):** AUC **0.88**, cutoff **7**, training **n=136** (active 61%), validation **n=30**; ESR+ULTRAS AUC up to **0.95** (ma2025anovelultrasoundbased pages 1-2).
- **PTX3 vs CRP for activity assessment (meta-analysis cited in 2023 review):** PTX3 pooled sensitivity **78%**, specificity **85%**, AUC **0.88** vs CRP sensitivity **66%**, specificity **77%**, AUC **0.75** (as2023currentdiagnosisand pages 2-4).

---

## 11) Ontology-ready annotation table

| Entity Type | Standardized Name/Symbol | Ontology ID Placeholder | Role in TAK | Supporting Sources |
| :--- | :--- | :--- | :--- | :--- |
| **Gene/Protein** | IL6 | HGNC:6018 | Drives VSMC senescence, Th17 differentiation, and fibroblast activation. | (matsumoto2023changesinthe pages 3-5, guo2024aglimpseinto pages 11-13, fang2024associationbetweenpremature pages 9-10, fang2024associationbetweenpremature pages 12-13) |
| **Gene/Protein** | STAT3 | HGNC:11364 | Mitochondrial pTyr705-STAT3 stabilizes MFN2, causing pathological mitochondrial fusion and senescence. | (fang2024associationbetweenpremature pages 9-10, fang2024associationbetweenpremature pages 10-11, fang2024associationbetweenpremature pages 12-13) |
| **Gene/Protein** | MFN2 | HGNC:16877 | Mitofusin-2 stabilized by STAT3 promotes mitochondrial elongation and VSMC senescence. | (fang2024associationbetweenpremature pages 11-12, fang2024associationbetweenpremature pages 10-11) |
| **Gene/Protein** | IL12B | HGNC:5970 | GWAS risk locus; drives Th1 differentiation and IFN-gamma production. | (bhandari2023pathophysiologydiagnosisand pages 2-3, guo2024aglimpseinto pages 11-13) |
| **Gene/Protein** | IL23A | HGNC:19141 | Supports maintenance of pathogenic Th17 cells. | (guo2024aglimpseinto pages 11-13, bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Gene/Protein** | TNF | HGNC:11892 | Synergizes with IFN-gamma to recruit monocytes via CCL2 for granuloma formation. | (matsumoto2023changesinthe pages 2-3) |
| **Gene/Protein** | IFNG | HGNC:5438 | Th1 cytokine driving macrophage activation, cytotoxicity, and chronic inflammation. | (matsumoto2023changesinthe pages 3-5, matsumoto2023changesinthe pages 1-2) |
| **Gene/Protein** | CSF2 (GM-CSF) | HGNC:2434 | Promotes macrophage activation, neo-angiogenesis, and tissue destruction. | (matsumoto2023changesinthe pages 2-3) |
| **Gene/Protein** | CDKN2A (p16) | HGNC:1787 | Upregulated in senescent VSMCs within inflamed aortic tissue. | (fang2024associationbetweenpremature pages 9-10, fang2024associationbetweenpremature pages 11-11) |
| **Gene/Protein** | CXCL8 (IL8) | HGNC:6025 | Component of the Senescence-Associated Secretory Phenotype (SASP) from VSMCs. | (fang2024associationbetweenpremature pages 11-12, fang2024associationbetweenpremature pages 11-11) |
| **Gene/Protein** | C1QA/C1QB | HGNC:1244/1245 | Transcriptomic upregulation indicates complement pathway involvement in pathogenesis. | (xu2025integratedbulkand pages 1-2) |
| **Gene/Protein** | EGR1 | HGNC:3238 | Central transcriptional hub upregulated in T cells and aortic tissue. | (xu2025integratedbulkand pages 1-2) |
| **Gene/Protein** | NOTCH1 | HGNC:7881 | Signaling upregulates mTORC1 to promote pro-inflammatory T cell differentiation. | (bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Cell Type** | Dendritic cells | CL:0000451 | Vascular DCs expressing TLRs release IL-12/IL-23, initiating T cell responses. | (bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Cell Type** | Th1 cells | CL:0000545 | Predominant in chronic lesions; drive granulomatous response via IFN-gamma. | (matsumoto2023changesinthe pages 3-5, guo2024aglimpseinto pages 11-13) |
| **Cell Type** | Th17 cells | CL:0000898 | Associated with active disease, vascular remodeling, and acute inflammation. | (matsumoto2023changesinthe pages 3-5, guo2024aglimpseinto pages 11-13) |
| **Cell Type** | Multinucleated giant cell | CL:0000529 | Formed by fusion of CCR2+ monocytes/macrophages in the media; hallmark of TAK. | (bhandari2023pathophysiologydiagnosisand pages 2-3, matsumoto2023changesinthe pages 2-3) |
| **Cell Type** | Vascular smooth muscle cell | CL:0000359 | Undergoes premature senescence via IL-6 signaling; secretes pro-inflammatory SASP. | (fang2024associationbetweenpremature pages 9-10, fang2024associationbetweenpremature pages 12-13) |
| **Cell Type** | B cell | CL:0000236 | Produces anti-endothelial antibodies and forms ectopic lymphoid structures in adventitia. | (bhandari2023pathophysiologydiagnosisand pages 2-3, guo2024aglimpseinto pages 11-13) |
| **Cell Type** | CD8+ T cell | CL:0000625 | Cytotoxic cells releasing perforin/granzyme; enriched in lesions. | (matsumoto2023changesinthe pages 3-5, bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Anatomical Structure** | Vasa vasorum | UBERON:0004574 | Initial site of inflammation and immune cell entry into the arterial wall. | (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Anatomical Structure** | Tunica media | UBERON:0002535 | Site of VSMC loss, giant cell accumulation, and destruction leading to aneurysms. | (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Anatomical Structure** | Tunica adventitia | UBERON:0002534 | Site of fibrosis and tertiary lymphoid organ formation. | (bhandari2023pathophysiologydiagnosisand pages 2-3, bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Biological Process** | Cellular senescence | GO:0090398 | Pathological aging of VSMCs driven by IL-6/Mito-STAT3 axis, fueling inflammation. | (fang2024associationbetweenpremature pages 9-10, fang2024associationbetweenpremature pages 12-13) |
| **Biological Process** | Mitochondrial fusion | GO:0008053 | Dysregulated hyperfusion in VSMCs mediated by MFN2 stabilization. | (fang2024associationbetweenpremature pages 11-12, fang2024associationbetweenpremature pages 8-9) |
| **Biological Process** | Granulomatous inflammation | GO:0002548 | Chronic inflammatory response involving macrophages and giant cells in the aorta. | (bhandari2023pathophysiologydiagnosisand pages 2-3, matsumoto2023changesinthe pages 2-3) |
| **Biological Process** | Complement activation | GO:0006954 | Activation of the complement cascade in T cells and tissue contributing to injury. | (xu2025integratedbulkand pages 1-2) |
| **Biological Process** | TOR signaling | GO:0031929 | mTORC1 hyperactivity driven by Notch1 supports metabolic needs of activated T cells. | (bhandari2023pathophysiologydiagnosisand pages 3-4) |
| **Chemical/Drug** | Tocilizumab | CHEBI:172297 | IL-6 receptor antagonist; reduces relapse but may not fully suppress Th1/CD8 cells. | (matsumoto2023changesinthe pages 1-2, fang2024associationbetweenpremature pages 12-13) |
| **Chemical/Drug** | JAK inhibitors | CHEBI:variable | Suppress T cell/macrophage infiltration and neo-angiogenesis (e.g., tofacitinib, baricitinib). | (matsumoto2023changesinthe pages 3-5, matsumoto2023changesinthe pages 2-3) |


*Table: A structured overview of key genes, cell types, anatomical structures, and biological processes involved in Takayasu arteritis, mapped to ontology categories with supporting evidence.*

---

## 12) Limitations of this tool-based extraction (transparency)

- Some pathways of interest (e.g., **inflammasome/NLRP3**; detailed **NF-κB** or **ferroptosis** programs within TAK lesions) likely have relevant primary literature, but **the necessary primary text evidence was not fully available in the retrieved evidence snippets** for this run, so these mechanisms are not asserted beyond what is explicitly supported (fang2024associationbetweenpremature pages 9-10).
- Where the sources are reviews, mechanistic claims are anchored to the review’s synthesis; primary mechanistic evidence is strongest for the **VSMC senescence axis** from ARD 2024 (fang2024associationbetweenpremature pages 6-7, fang2024associationbetweenpremature pages 11-11).

---

## Key visual evidence
The mechanistic schematic summarizing the **IL-6 → mitochondrial pSTAT3(Tyr705) → MFN2 stabilization → mitochondrial hyperfusion → VSMC senescence → SASP-driven inflammation** loop is captured in a cropped figure panel (fang2024associationbetweenpremature media d7f13343).


References

1. (bhandari2023pathophysiologydiagnosisand pages 2-3): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 50 citations.

2. (bhandari2023pathophysiologydiagnosisand pages 3-4): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 50 citations.

3. (matsumoto2023changesinthe pages 3-5): Kotaro Matsumoto, Katsuya Suzuki, Masaru Takeshita, Tsutomu Takeuchi, and Yuko Kaneko. Changes in the molecular profiles of large-vessel vasculitis treated with biological disease-modifying anti-rheumatic drugs and janus kinase inhibitors. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1197342, doi:10.3389/fimmu.2023.1197342. This article has 6 citations and is from a peer-reviewed journal.

4. (matsumoto2023changesinthe pages 1-2): Kotaro Matsumoto, Katsuya Suzuki, Masaru Takeshita, Tsutomu Takeuchi, and Yuko Kaneko. Changes in the molecular profiles of large-vessel vasculitis treated with biological disease-modifying anti-rheumatic drugs and janus kinase inhibitors. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1197342, doi:10.3389/fimmu.2023.1197342. This article has 6 citations and is from a peer-reviewed journal.

5. (guo2024aglimpseinto pages 11-13): Shuning Guo, Yixiao Tian, Jing Li, and Xiaofeng Zeng. A glimpse into humoral response and related therapeutic approaches of takayasu’s arteritis. International Journal of Molecular Sciences, 25:6528, Jun 2024. URL: https://doi.org/10.3390/ijms25126528, doi:10.3390/ijms25126528. This article has 5 citations.

6. (matsumoto2023changesinthe pages 2-3): Kotaro Matsumoto, Katsuya Suzuki, Masaru Takeshita, Tsutomu Takeuchi, and Yuko Kaneko. Changes in the molecular profiles of large-vessel vasculitis treated with biological disease-modifying anti-rheumatic drugs and janus kinase inhibitors. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1197342, doi:10.3389/fimmu.2023.1197342. This article has 6 citations and is from a peer-reviewed journal.

7. (fang2024associationbetweenpremature pages 4-5): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

8. (xu2025integratedbulkand pages 1-2): Kexin Xu, Taotao Li, Na Gao, Yaxin Zhang, Yi Yang, Honglei Zhao, Longfei Wang, Junming Zhu, Jian Liu, and Lili Pan. Integrated bulk and single-cell transcriptomics identifies shared and specific immune signatures in takayasu arteritis. Arthritis Research &amp; Therapy, Nov 2025. URL: https://doi.org/10.1186/s13075-025-03673-x, doi:10.1186/s13075-025-03673-x. This article has 1 citations and is from a domain leading peer-reviewed journal.

9. (fang2024associationbetweenpremature pages 11-12): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

10. (fang2024associationbetweenpremature pages 6-7): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

11. (fang2024associationbetweenpremature pages 10-11): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

12. (fang2024associationbetweenpremature pages 12-13): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

13. (fang2024associationbetweenpremature pages 11-11): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

14. (fang2024associationbetweenpremature media d7f13343): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

15. (fang2024associationbetweenpremature pages 9-10): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

16. (fang2024associationbetweenpremature pages 8-9): Chenglong Fang, Lihong Du, Shang Gao, Yuexin Chen, Zuo-Guan Chen, Zhiyuan Wu, Lili Li, Jing Li, Xiaofeng Zeng, Mengtao Li, Yongjun Li, and Xinping Tian. Association between premature vascular smooth muscle cells senescence and vascular inflammation in takayasu's arteritis. Nov 2024. URL: https://doi.org/10.1136/ard-2024-225630, doi:10.1136/ard-2024-225630. This article has 23 citations and is from a highest quality peer-reviewed journal.

17. (bhandari2023pathophysiologydiagnosisand pages 9-9): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 50 citations.

18. (ma2025anovelultrasoundbased pages 1-2): Lingying Ma, Ying Sun, Yun Liu, Huijing Huang, Rongyi Chen, Chaolun Li, Hong Han, and Lindi Jiang. A novel ultrasound-based score for assessing carotid artery activity in takayasu's arteritis. Clinical and experimental rheumatology, Apr 2025. URL: https://doi.org/10.55563/clinexprheumatol/purgx3, doi:10.55563/clinexprheumatol/purgx3. This article has 0 citations and is from a peer-reviewed journal.

19. (ma2024ultrasoundactivityscore pages 11-14): Lingying Ma, Ying Sun, Yun Liu, Huijing Huang, Rongyi Chen, Chaolun Li, Hong Han, and Lindi Jiang. Ultrasound activity score in the carotid arteries for assessing disease activity of takayasu arteritis. Unknown journal, Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3982386/v1, doi:10.21203/rs.3.rs-3982386/v1.

20. (as2023currentdiagnosisand pages 2-4): Chandhu AS and Debashish Danda. Current diagnosis and management of takayasu arteritis. International heart journal, 64 4:519-534, Jul 2023. URL: https://doi.org/10.1536/ihj.23-195, doi:10.1536/ihj.23-195. This article has 12 citations and is from a peer-reviewed journal.

21. (as2023currentdiagnosisand pages 1-2): Chandhu AS and Debashish Danda. Current diagnosis and management of takayasu arteritis. International heart journal, 64 4:519-534, Jul 2023. URL: https://doi.org/10.1536/ihj.23-195, doi:10.1536/ihj.23-195. This article has 12 citations and is from a peer-reviewed journal.