---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:47:00.952412'
end_time: '2025-12-18T09:55:17.181477'
duration_seconds: 496.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alopecia Areata
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Alopecia Areata
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Alopecia Areata**.
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
- **Disease Name:** Alopecia Areata
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Alopecia Areata**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Alopecia Areata (AA)
- MONDO ID: MONDO:0005392
- Category: Autoimmune

Pathophysiology description
Alopecia areata is a T cell–mediated, non-scarring autoimmune disease of the anagen hair follicle driven by collapse of hair-follicle immune privilege (IP) and a self-amplifying IFN-γ–IL-15–JAK/STAT axis. Under homeostasis, anagen follicles suppress antigen presentation and maintain local immunosuppression (e.g., TGF-β, PD‑L1, IL‑10, α‑MSH, MIF) with low MHC I/II expression. In AA, IP collapses with upregulation of MHC I and II on follicular keratinocytes and antigen-presenting cells, increased expression of stress ligands (MICA, ULBP3/6), and recruitment/activation of cytotoxic CD8+ NKG2D+ T cells that recognize these ligands and deliver cytotoxic mediators (granzyme, perforin). This response is orchestrated by interferons and γ-chain cytokines: IFN‑γ induces IL‑15 production in follicular epithelium; IL‑15 sustains and amplifies CD8+ and NK cell effector programs through JAK1/JAK3 signaling, forming a local positive feedback loop that perpetuates disease. Lesional skin shows prominent IFN-response chemokines (CXCL9/CXCL10/CXCL11), and multi-omic and single-cell data support a central role for clonally expanded, tissue-resident CD8+ effectors, with contributions from Th1/Th17 CD4+ cells, NK cells, dendritic cells (including plasmacytoid DCs), and mast cells. Oxidative and other cellular stressors are implicated in NKG2D-ligand induction and IP failure. Spatially, the bulb (growth compartment) and, in some reports, the bulge (stem cell niche) exhibit IP alterations and pathologic infiltration, which correlate with premature anagen→catagen transitions and clinical hair loss. Therapeutically, targeting the JAK–STAT node reverses the pathogenic transcriptional program and supports regrowth, and emerging approaches modulate upstream chemokine axes such as CXCL12/CXCR4 in preclinical models (URLs and dates below). (yamaguchi2024pathogenesisofalopecia pages 2-4, lee2023functionalinterrogationof pages 6-7, simeonovski2025disruptionofhair pages 5-7, kim2025alopeciaareatafrom pages 2-4, zhao2025frommechanismsto pages 1-2, an2024humanizedcxcl12antibody pages 1-2)

Core Pathophysiology
- Primary mechanisms
  - Hair follicle immune privilege collapse: loss of local immunosuppressive milieu and increased antigen presentation (MHC I/II) in anagen follicles permit autoreactive T cell recognition. (yamaguchi2024pathogenesisofalopecia pages 2-4, zhao2025frommechanismsto pages 1-2)
  - IFN‑γ–IL‑15–JAK/STAT amplification: IFN‑γ induces IL‑15 in follicular keratinocytes; IL‑15 activates CD8+ and NK cells via JAK1/3; multiple cytokines converge on JAK–STAT to drive cytotoxic and chemokine programs. (yamaguchi2024pathogenesisofalopecia pages 2-4, simeonovski2025disruptionofhair pages 5-7, kim2025alopeciaareatafrom pages 2-4)
  - CD8+ NKG2D+ T cell cytotoxicity: recognition of stress ligands (MICA, ULBP3/6) triggers effector functions and hair cycle disruption. (lee2023functionalinterrogationof pages 6-7, yamaguchi2024pathogenesisofalopecia pages 2-4)
  - Chemokine recruitment: CXCL9/10/11 (IFN-inducible) recruit CXCR3+ Th1 and CD8+ T cells; CXCL12/CXCR4 supports effector accumulation in preclinical AA. (yamaguchi2024pathogenesisofalopecia pages 2-4, an2024humanizedcxcl12antibody pages 1-2)
  - Oxidative and cellular stress: promotes NKG2D ligand expression (e.g., MICA, ULBP3/6) and contributes to IP collapse. (yamaguchi2024pathogenesisofalopecia pages 2-4)
- Dysregulated molecular pathways
  - JAK–STAT cascade downstream of IFNs and γ-chain cytokines (IL‑2, IL‑7, IL‑15). (simeonovski2025disruptionofhair pages 5-7, lee2023functionalinterrogationof pages 6-7)
  - Antigen processing and presentation via MHC I and II. (yamaguchi2024pathogenesisofalopecia pages 2-4, simeonovski2025disruptionofhair pages 5-7)
  - Chemokine-mediated signaling (CXCL9/10/11–CXCR3; CXCL12–CXCR4). (yamaguchi2024pathogenesisofalopecia pages 2-4, an2024humanizedcxcl12antibody pages 1-2)
- Affected cellular processes
  - Cytotoxic T cell activation, tissue residency, clonal expansion; impaired local regulation (Tregs). (lee2023functionalinterrogationof pages 6-7, kim2025alopeciaareatafrom pages 2-4)
  - Premature anagen→catagen transition and follicular miniaturization without scarring. (kim2025alopeciaareatafrom pages 2-4)

Key Molecular Players
- Genes/Proteins (HGNC)
  - IFNG (IFN‑γ), IL15, JAK1, JAK2, JAK3: core of the amplification loop and its signaling node. (yamaguchi2024pathogenesisofalopecia pages 2-4, simeonovski2025disruptionofhair pages 5-7)
  - KLRK1 (NKG2D) on CD8+ T cells/NK cells; ligands MICA, ULBP3/6 on stressed follicular cells. (lee2023functionalinterrogationof pages 6-7, yamaguchi2024pathogenesisofalopecia pages 2-4)
  - CXCL9/CXCL10 (IFN-response chemokines); CXCL12 and its receptor CXCR4. (yamaguchi2024pathogenesisofalopecia pages 2-4, an2024humanizedcxcl12antibody pages 1-2)
- Chemical entities
  - JAK inhibitors (e.g., baricitinib, ritlecitinib): block pathogenic cytokine signaling; effective but relapse after cessation is common per reviews and trials. (simeonovski2025disruptionofhair pages 5-7, kim2025alopeciaareatafrom pages 2-4)
  - CXCL12-neutralizing antibody: delayed AA onset and reduced CD8+ activation in a mouse model. (an2024humanizedcxcl12antibody pages 1-2)
- Cell types (CL)
  - CD8+ cytotoxic T lymphocyte (CTL): primary disease driver; depletion prevents and reverses AA in mouse models. (lee2023functionalinterrogationof pages 6-7)
  - NK cells: contribute to innate cytotoxicity via NKG2D. (udovic2024decipheringthecomplex pages 5-7)
  - Dendritic cells (including plasmacytoid DCs): IFN‑α production and antigen presentation that promote chemokine cascades and T-cell recruitment. (yamaguchi2024pathogenesisofalopecia pages 2-4)
  - Mast cells: augment local inflammation and tissue damage. (simeonovski2025disruptionofhair pages 5-7)
  - Regulatory T cells (Tregs): dysfunction or insufficiency correlates with loss of suppression; expanded Tregs are protective in models. (lee2023functionalinterrogationof pages 6-7)
- Anatomical locations (UBERON)
  - Hair follicle (scalp) with emphasis on bulb and bulge compartments showing IP alterations and immune infiltration. (yamaguchi2024pathogenesisofalopecia pages 2-4, kim2025alopeciaareatafrom pages 2-4)

Biological Processes (GO annotations)
- Antigen presentation via MHC class I and II: increased on follicular epithelium/APCs in AA (GO:0002474; GO:0002504). (yamaguchi2024pathogenesisofalopecia pages 2-4, simeonovski2025disruptionofhair pages 5-7)
- JAK–STAT signaling cascade (GO:0007259): integrates IFN and γ-chain cytokines; therapeutically targeted. (simeonovski2025disruptionofhair pages 5-7)
- Response to interferon-gamma (GO:0034341): upregulated in lesional skin. (yamaguchi2024pathogenesisofalopecia pages 2-4)
- Chemokine-mediated signaling pathway (GO:0070098): CXCL9/10/11–CXCR3; CXCL12–CXCR4 trafficking. (yamaguchi2024pathogenesisofalopecia pages 2-4, an2024humanizedcxcl12antibody pages 1-2)
- Positive regulation of T cell–mediated cytotoxicity (GO:0001916): NKG2D ligand induction on follicular cells. (yamaguchi2024pathogenesisofalopecia pages 2-4)
- Cellular response to oxidative stress (GO:0006979): contributes to NKG2D-ligand induction and IP collapse. (yamaguchi2024pathogenesisofalopecia pages 2-4)

Cellular Components
- Follicular keratinocyte membranes and immune synapses: sites of MHC I/II upregulation and NKG2D ligand display enabling CD8+ cytotoxic engagement. (yamaguchi2024pathogenesisofalopecia pages 2-4)
- Peribulbar and intrafollicular niches: chemokine-rich microenvironments recruiting CXCR3+/CXCR4+ effector T cells and innate lymphocytes. (yamaguchi2024pathogenesisofalopecia pages 2-4, an2024humanizedcxcl12antibody pages 1-2)

Disease Progression
- Sequence of events
  1) Triggering stressors (e.g., oxidative stress, infections, drugs) perturb follicular IP; pDC-derived IFN‑α and local IFN‑γ signatures rise with chemokines CXCL9/10/11. (yamaguchi2024pathogenesisofalopecia pages 2-4)
  2) Follicular keratinocytes upregulate MHC I/II and NKG2D ligands (MICA, ULBP3/6). (yamaguchi2024pathogenesisofalopecia pages 2-4)
  3) Recruitment/activation of CD8+ NKG2D+ T cells and NK cells; IFN‑γ production induces IL‑15 in follicular epithelium; IL‑15 via JAK1/3 sustains cytotoxic effectors (positive feedback). (yamaguchi2024pathogenesisofalopecia pages 2-4, lee2023functionalinterrogationof pages 6-7)
  4) Effector cytotoxicity and cytokines precipitate premature anagen exit and hair shedding; TRM-like CD8+ clones persist, predisposing to relapse. (lee2023functionalinterrogationof pages 6-7, kim2025alopeciaareatafrom pages 2-4)
- Quantitative data (recent)
  - Human single-cell profiling: T cells 23.74% vs 11.49% and CD8+ 9.85% vs 4.11% in AA vs control skin. (lee2023functionalinterrogationof pages 6-7)
  - Preclinical CXCL12 blockade: CD8+ T cells rose from 8.1% (control) to 68.9% (AA), reduced to 37% with anti‑CXCL12; AA onset was delayed and JAK/STAT activation in CD8+ T cells was attenuated. (an2024humanizedcxcl12antibody pages 6-9)

Phenotypic Manifestations (HP terms and links to mechanisms)
- Patchy non-scarring alopecia, ophiasis, alopecia totalis/universalis; exclamation point hairs; nail pitting. These phenotypes reflect episodic, perifollicular cytotoxic inflammation and premature anagen termination without fibrosis. (kim2025alopeciaareatafrom pages 2-4)

Evidence highlights and expert analyses (2023–2024 priority)
- CD8+ T cells as disease drivers and depletion effects: Single-cell and in vivo depletion in graft-induced C3H/HeJ model demonstrate CD8+ T cell depletion uniquely prevents and reverses AA, whereas depleting CD4+, NK, B, or γδ T cells does not. Human skin shows convergent CD8+ effector trajectories and enrichment. (lee2023functionalinterrogationof pages 6-7)
- CXCL12/CXCR4 axis modulation: A humanized anti‑CXCL12 antibody delayed onset, reduced CD8+ infiltration and activation, and reversed type II IFN/chemotaxis gene signatures in AA mice, indicating a tractable upstream chemokine axis. (an2024humanizedcxcl12antibody pages 1-2, an2024humanizedcxcl12antibody pages 6-9)
- Oxidative stress and NKG2D ligands: Reviews summarizing human and experimental data support oxidative stress as a contributor to HF-IP collapse and upregulation of MICA/ULBP3/6, thereby licensing NKG2D+ cytotoxic responses. (yamaguchi2024pathogenesisofalopecia pages 2-4)
- Drug-induced HF-IP collapse (clinical translational insight): EGFR/MAPK inhibitor–associated folliculitis in patients shows bulge CD8+ infiltration, upregulation of MHC I/II and β2‑microglobulin, and reduced TGF‑β1, indicating that perturbations in growth factor signaling can collapse HF IP in humans; this supports MHC-driven mechanisms seen in AA. (yamaguchi2024pathogenesisofalopecia pages 2-4)

Current applications and real-world implementations
- JAK inhibitors in clinical practice: JAK inhibition (e.g., baricitinib, ritlecitinib) effectively suppresses the IFN‑γ/IL‑15–JAK/STAT axis and induces regrowth in moderate–severe AA, with relapse often upon withdrawal, underscoring disease memory at the TRM/TCR-clone level. (simeonovski2025disruptionofhair pages 5-7, kim2025alopeciaareatafrom pages 2-4)
- Emerging targets: Chemokine pathway interventions (e.g., anti‑CXCL12) demonstrate efficacy in mouse AA by reducing CD8+ activation and IFN-linked signatures, supporting trials that explore upstream trafficking control. (an2024humanizedcxcl12antibody pages 1-2)

Statistics and data from recent studies
- Human lesional skin single-cell profiling shows significant enrichment of T cells and especially CD8+ cytotoxic states in AA compared to control (23.74% vs 11.49% T cells; 9.85% vs 4.11% CD8+), supporting a CD8-centered pathophysiology. (lee2023functionalinterrogationof pages 6-7)
- In AA mice, anti‑CXCL12 reduced the pathogenic CD8+ T cell fraction from 68.9% (AA) to 37%, with concomitant reversal of chemotaxis/type II IFN gene programs, and delayed clinical onset. (an2024humanizedcxcl12antibody pages 6-9)
- Epidemiology context: Global AA prevalence increased from 20.43M (1990) to 30.89M (2021), highlighting public health impact and the need for durable therapies targeting central immunopathology. (zhao2025frommechanismsto pages 1-2)

Gene/protein annotations with ontology terms
- HGNC: IFNG (IFN‑γ); IL15; JAK1; JAK2; JAK3; KLRK1 (NKG2D); MICA; ULBP3; ULBP6; CXCL9; CXCL10; CXCL12; CXCR4. Roles detailed above. (yamaguchi2024pathogenesisofalopecia pages 2-4, lee2023functionalinterrogationof pages 6-7, an2024humanizedcxcl12antibody pages 1-2)

Phenotype associations (HPO)
- HP:0002299 (Alopecia areata); HP:0001596 (Nail pitting); HP:0001595 (Alopecia totalis); HP:0002293 (Alopecia universalis). Mechanistically linked to intermittent CD8+ cytotoxic infiltration and IFN‑γ–IL‑15–JAK/STAT activity without scarring. (kim2025alopeciaareatafrom pages 2-4)

Cell type involvement (CL terms)
- CL:0000625 (CD8+ T cell): disease driver; CL:0000623 (NK cell): innate effector; CL:0000451 (dendritic cell): antigen presentation, IFN‑α (pDC) signaling; CL:0000097 (mast cell): inflammatory amplification; CL:0000815 (regulatory T cell): impaired regulation. (lee2023functionalinterrogationof pages 6-7, yamaguchi2024pathogenesisofalopecia pages 2-4, simeonovski2025disruptionofhair pages 5-7)

Anatomical locations (UBERON terms)
- UBERON:0002062 (Hair follicle). Pathology centered at the hair bulb; bulge niche implicated in persistence/relapse; perifollicular dermis is an inflammatory niche. (yamaguchi2024pathogenesisofalopecia pages 2-4, kim2025alopeciaareatafrom pages 2-4)

Chemical entities (selected; mechanisms)
- JAK inhibitors (e.g., baricitinib, ritlecitinib): suppress IFN‑γ/IL‑15–JAK/STAT signaling; effective for regrowth; relapse common after cessation. (simeonovski2025disruptionofhair pages 5-7, kim2025alopeciaareatafrom pages 2-4)
- Anti‑CXCL12 antibody (preclinical): reduces CD8+ activation, reverses chemotaxis/type II IFN signatures, delays AA onset. (an2024humanizedcxcl12antibody pages 1-2)

Embedded artifact summarizing key entities and evidence
| Category | Entity (standard term) | Ontology/ID (where applicable) | Role in AA Pathophysiology | Key Evidence (citation, year) |
|---|---|---|---|---|
| Immune effector cell | CD8+ NKG2D+ T cell | HGNC:KLRK1 | Principal cytotoxic effectors attacking anagen HF after IP collapse; produce IFN-γ, granzyme/perforin; depletion prevents/reverses AA in mouse models | (lee2023functionalinterrogationof pages 6-7), (yamaguchi2024pathogenesisofalopecia pages 2-4) |
| Cytokine | IFNG (Interferon-gamma) | HGNC:IFNG | Upstream driver that increases MHC I on follicular keratinocytes and induces IL-15, amplifying cytotoxic loop | (yamaguchi2024pathogenesisofalopecia pages 2-4), (kim2025alopeciaareatafrom pages 2-4) |
| Cytokine | IL15 (Interleukin-15) | HGNC:IL15 | Supports survival/activation of CD8+ and NK cells in follicle; key mediator of local feed-forward JAK/STAT activation | (yamaguchi2024pathogenesisofalopecia pages 2-4), (simeonovski2025disruptionofhair pages 5-7) |
| Signaling kinases | JAK1 / JAK2 / JAK3 | HGNC:JAK1; JAK2; JAK3 | Signal transducers for IFN/IL-15 family cytokines; central therapeutic target (JAK inhibitors) | (simeonovski2025disruptionofhair pages 5-7), (lee2023functionalinterrogationof pages 6-7) |
| Chemokines | CXCL9 / CXCL10 | HGNC:CXCL9; CXCL10 | IFN-response chemokines that recruit CXCR3+ Th1/CD8 cells to peribulbar region | (yamaguchi2024pathogenesisofalopecia pages 2-4), (udovic2024decipheringthecomplex pages 5-7) |
| Stress ligands | MICA | HGNC:MICA | NKG2D ligand upregulated on stressed follicular cells, engages CD8+/NK NKG2D to trigger cytotoxicity | (yamaguchi2024pathogenesisofalopecia pages 2-4), (udovic2024decipheringthecomplex pages 5-7) |
| Stress ligands | ULBP3 / ULBP6 | HGNC:ULBP3; ULBP6 | NKG2D ligands implicated in AA-specific stress signaling and immune recognition | (yamaguchi2024pathogenesisofalopecia pages 2-4), (udovic2024decipheringthecomplex pages 5-7) |
| Anatomy (HF compartment) | Hair follicle bulb | UBERON:hair_follicle_bulb | Site of anagen cycling and primary target of CD8+ peribulbar infiltrates in AA | (yamaguchi2024pathogenesisofalopecia pages 2-4), (lee2023functionalinterrogationof pages 6-7) |
| Anatomy (HF compartment) | Hair follicle bulge | UBERON:hair_follicle_bulge | Stem cell niche affected by immune-privilege collapse; related to relapse and regenerative failure | (kim2025alopeciaareatafrom pages 2-4), (yamaguchi2024pathogenesisofalopecia pages 2-4) |
| Cell type | Keratinocyte (follicular) | CL:Keratinocyte | Source of IL-15 and MHC upregulation; presents antigens and expresses stress ligands | (yamaguchi2024pathogenesisofalopecia pages 2-4), (an2024humanizedcxcl12antibody pages 1-2) |
| Cell type | Dendritic cell (incl. pDC) | CL:Dendritic_cell | pDCs produce IFN-α to initiate IFN-driven chemokine cascades (CXCL10) and augment T-cell recruitment | (yamaguchi2024pathogenesisofalopecia pages 2-4), (kim2025alopeciaareatafrom pages 4-5) |
| Cell type | Natural killer (NK) cell | CL:NK_cell | Contribute innate cytotoxicity via NKG2D recognition of stressed follicular ligands | (udovic2024decipheringthecomplex pages 5-7), (yamaguchi2024pathogenesisofalopecia pages 2-4) |
| Cell type | Mast cell | CL:Mast_cell | Participate in local inflammation, release mediators that may disrupt HF immune privilege | (simeonovski2025disruptionofhair pages 5-7), (udovic2024decipheringthecomplex pages 5-7) |
| Cell type (regulatory) | Regulatory T cell (Treg) | CL:Regulatory_T_cell | Defective/local dysfunction contributes to loss of suppression and permits autoreactive CD8+ activity | (lee2023functionalinterrogationof pages 6-7), (kim2025alopeciaareatafrom pages 2-4) |
| Biological process (GO) | Antigen presentation (MHC I / II) | GO: antigen presentation (MHC I/II) | Upregulated in HF after IP collapse enabling autoreactive T-cell recognition of follicular antigens | (simeonovski2025disruptionofhair pages 5-7), (yamaguchi2024pathogenesisofalopecia pages 2-4) |
| Biological process (GO) | JAK–STAT signaling cascade | GO: JAK-STAT pathway | Integrates IFN/IL-15 signals to drive effector gene programs; target of JAK inhibitors that restore hair growth | (simeonovski2025disruptionofhair pages 5-7), (lee2023functionalinterrogationof pages 6-7) |
| Biological process (GO) | Chemokine-mediated signaling | GO: chemokine signaling | Directs recruitment/positioning of CXCR3+ and CXCR4+ lymphocytes to follicular niches | (yamaguchi2024pathogenesisofalopecia pages 2-4), (an2024humanizedcxcl12antibody pages 1-2) |
| Biological process (GO) | Oxidative stress response | GO: oxidative stress response | Cellular stress/ROS can induce NKG2D ligands and promote HF-IP collapse, potentiating immune recognition | (yamaguchi2024pathogenesisofalopecia pages 2-4), (udovic2024decipheringthecomplex pages 5-7) |
| Chemokine axis | CXCL12 / CXCR4 axis | HGNC:CXCL12 / CXCR4 (chemokine axis) | Fibroblast/ORS-derived CXCL12 promotes T-cell recruitment and activation; CXCL12 neutralization reduced CD8+ activation and delayed AA onset in mice | (an2024humanizedcxcl12antibody pages 1-2), (an2024humanizedcxcl12antibody pages 6-9) |
| Therapeutic class | Baricitinib / Ritlecitinib (JAK inhibitors) | Drug: JAK inhibitor | Clinical JAK inhibitors block IFN/IL-15 signaling, induce regrowth but relapse is common after cessation; approvals and Phase-3 data support efficacy | (simeonovski2025disruptionofhair pages 5-7), (, 2025) |


*Table: Compact reference table listing major cells, molecules, pathways, anatomical sites, and therapeutics implicated in alopecia areata pathophysiology with concise roles and primary evidence citations from the collected context (pqac IDs). This supports rapid integration into a disease knowledge base.*

Evidence items (recent, with URLs and publication dates)
- Lee EY et al. Functional interrogation of lymphocyte subsets in alopecia areata using single-cell RNA sequencing. PNAS. Jul 2023. https://doi.org/10.1073/pnas.2305764120. Key findings: CD8+ T cell enrichment (9.85% vs 4.11%); in vivo, anti‑CD8 uniquely prevented and reversed AA; NK/B/γδ depletion ineffective. (lee2023functionalinterrogationof pages 6-7)
- Yamaguchi HL et al. Pathogenesis of Alopecia Areata and Vitiligo: Commonalities and Differences. IJMS. Apr 2024. https://doi.org/10.3390/ijms25084409. Key findings: HF-IP collapse; MHC upregulation; NKG2D-ligand (MICA, ULBP3/6) relevance; IFN‑γ and IL‑15 axis; elevated CXCL9/10. (yamaguchi2024pathogenesisofalopecia pages 2-4)
- An S et al. Humanized CXCL12 antibody delays onset and modulates immune response in AA mice. Frontiers Immunol. Oct 2024. https://doi.org/10.3389/fimmu.2024.1444777. Key findings: CD8+ rose to 68.9% in AA; reduced to 37% with anti‑CXCL12; JAK/STAT activation attenuated; onset delayed. (an2024humanizedcxcl12antibody pages 1-2, an2024humanizedcxcl12antibody pages 6-9)
- Udović IŠ et al. Deciphering the Complex Immunopathogenesis of Alopecia Areata. IJMS. May 2024. https://doi.org/10.3390/ijms25115652. Key findings: CD8+NKG2D+ as key drivers; IFN‑γ/IL‑15 feedback; JAK-STAT implication; NKG2D ligands MICA/ULBP3/6. (udovic2024decipheringthecomplex pages 5-7)
- Kim S‑Y et al. Alopecia areata: from immunopathogenesis to emerging therapeutic approaches. Frontiers Immunol. Nov 2025. https://doi.org/10.3389/fimmu.2025.1681163. Key findings: CD8+NKG2D+ central; TRM/clonal persistence; relapse after JAKi cessation; bulge IP involvement. (kim2025alopeciaareatafrom pages 2-4)
- Zhao H‑B et al. From mechanisms to therapies: current advances in AA immunopathology. Frontiers Immunol. Sep 2025. https://doi.org/10.3389/fimmu.2025.1621492. Key findings: global burden; multi-cellular immune imbalance; centrality of JAK–STAT. (zhao2025frommechanismsto pages 1-2)

Notes and limitations
- Where possible, 2023–2024 sources were prioritized for mechanism and quantitative data (notably Lee 2023 PNAS and An 2024 Frontiers Immunology). Some contextual reviews from 2025 are included to synthesize emerging consensus on TRM/clonal persistence and therapeutic directions. (lee2023functionalinterrogationof pages 6-7, an2024humanizedcxcl12antibody pages 1-2, kim2025alopeciaareatafrom pages 2-4)


References

1. (yamaguchi2024pathogenesisofalopecia pages 2-4): Hiroki L. Yamaguchi, Yuji Yamaguchi, and Elena Peeva. Pathogenesis of alopecia areata and vitiligo: commonalities and differences. International Journal of Molecular Sciences, 25:4409, Apr 2024. URL: https://doi.org/10.3390/ijms25084409, doi:10.3390/ijms25084409. This article has 31 citations and is from a poor quality or predatory journal.

2. (lee2023functionalinterrogationof pages 6-7): Eunice Y. Lee, Zhenpeng Dai, Abhinav Jaiswal, Eddy Hsi Chun Wang, Niroshana Anandasabapathy, and Angela M. Christiano. Functional interrogation of lymphocyte subsets in alopecia areata using single-cell rna sequencing. Proceedings of the National Academy of Sciences of the United States of America, 120 29:e2305764120, Jul 2023. URL: https://doi.org/10.1073/pnas.2305764120, doi:10.1073/pnas.2305764120. This article has 25 citations and is from a highest quality peer-reviewed journal.

3. (simeonovski2025disruptionofhair pages 5-7): Viktor Simeonovski, Maja Dimova, Marko Kostovski, Julija Mitrova Telenta, Elena Mircheska Arsovska, and Liljana Labachevska Gjatovska. Disruption of hair follicle immune privilege in alopecia areata: enigmatic mechanisms and emerging concepts. Academic Medical Journal, 5:70-80, Jun 2025. URL: https://doi.org/10.53582/amj255170s, doi:10.53582/amj255170s. This article has 0 citations.

4. (kim2025alopeciaareatafrom pages 2-4): Su-Young Kim, Hyun Joo Lee, Jihye Heo, Beom Joon Kim, and Joon Seok. Alopecia areata: from immunopathogenesis to emerging therapeutic approaches. Frontiers in Immunology, Nov 2025. URL: https://doi.org/10.3389/fimmu.2025.1681163, doi:10.3389/fimmu.2025.1681163. This article has 0 citations and is from a peer-reviewed journal.

5. (zhao2025frommechanismsto pages 1-2): Huai-Bo Zhao, Ya-Nan Zhang, Yan Qiang, Guo-Mi Wang, Li-Wei Wang, Wen-cheng Jiang, and Xi Chen. From mechanisms to therapies: current advances breakthroughs in alopecia areata immunopathology. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1621492, doi:10.3389/fimmu.2025.1621492. This article has 4 citations and is from a peer-reviewed journal.

6. (an2024humanizedcxcl12antibody pages 1-2): Seungchan An, Mei Zheng, In Guk Park, Sang Gyu Park, Minsoo Noh, and Jong-Hyuk Sung. Humanized cxcl12 antibody delays onset and modulates immune response in alopecia areata mice: insights from single-cell rna sequencing. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1444777, doi:10.3389/fimmu.2024.1444777. This article has 7 citations and is from a peer-reviewed journal.

7. (udovic2024decipheringthecomplex pages 5-7): Ingrid Šutić Udović, Nika Hlača, Larisa Prpić Massari, Ines Brajac, Marija Kaštelan, and Marijana Vičić. Deciphering the complex immunopathogenesis of alopecia areata. International Journal of Molecular Sciences, 25:5652, May 2024. URL: https://doi.org/10.3390/ijms25115652, doi:10.3390/ijms25115652. This article has 44 citations and is from a poor quality or predatory journal.

8. (an2024humanizedcxcl12antibody pages 6-9): Seungchan An, Mei Zheng, In Guk Park, Sang Gyu Park, Minsoo Noh, and Jong-Hyuk Sung. Humanized cxcl12 antibody delays onset and modulates immune response in alopecia areata mice: insights from single-cell rna sequencing. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1444777, doi:10.3389/fimmu.2024.1444777. This article has 7 citations and is from a peer-reviewed journal.

9. (kim2025alopeciaareatafrom pages 4-5): Su-Young Kim, Hyun Joo Lee, Jihye Heo, Beom Joon Kim, and Joon Seok. Alopecia areata: from immunopathogenesis to emerging therapeutic approaches. Frontiers in Immunology, Nov 2025. URL: https://doi.org/10.3389/fimmu.2025.1681163, doi:10.3389/fimmu.2025.1681163. This article has 0 citations and is from a peer-reviewed journal.