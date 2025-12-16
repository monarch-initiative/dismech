---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:04.467814'
end_time: '2025-12-15T09:09:44.914475'
duration_seconds: 520.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dengue
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Dengue
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dengue**.
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
- **Disease Name:** Dengue
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dengue**.
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


Plan update: We defined the scope and aligned sections to the user template. We searched and gathered recent (2023–2024) evidence emphasizing NS1-driven vascular leak, ADE mechanisms, innate immune antagonism by DENV NS proteins, hematologic dysfunction, and adaptive immune skewing. We created a summary artifact mapping mechanisms to ontology-friendly entities and sources.

# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Dengue
- MONDO ID: MONDO:0005135 (dengue disease)
- Category: Infectious Disease

## Pathophysiology description
Dengue results from complex interactions between viral factors (notably secreted nonstructural protein 1, NS1) and host immune responses that collectively produce vascular leak, coagulopathy, and organ dysfunction. In severe disease, vascular permeability is driven by NS1-triggered endothelial glycocalyx degradation, tight-junction alterations, complement activation/modulation, mast cell mediators, and inflammatory lipids and cytokines, superimposed on antibody- and cell-mediated immunopathology during secondary or heterotypic infections. The clinical course typically evolves from a febrile viremic phase (days 1–3/6) to a critical phase with plasma leakage and shock in a subset of patients, followed by a recovery phase if supported appropriately (reviewed in 2024) (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7).

Key contemporary insights include: (i) NS1 is a major endothelial toxin and immunomodulator that activates TLR4-driven inflammation, cooperates with host proteases (e.g., MMP-9) to disrupt junctions and the glycocalyx, and manipulates complement; (ii) antibody-dependent enhancement (ADE) increases viral uptake via Fcγ receptors and amplifies cytokine production; (iii) DENV NS proteins antagonize type I interferon induction/signaling; (iv) the inflammasome can sense NS1 and contributes to protection; (v) hematologic dysfunction reflects both impaired platelet/megakaryocyte biology and immune-mediated destruction; and (vi) T/NK/Treg cell functional skewing correlates with progression to severe dengue (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024; https://doi.org/10.1371/journal.ppat.1012167, Apr 2024; https://doi.org/10.3390/ijms252111624, Oct 2024; https://doi.org/10.3390/v16071090, Jul 2024) (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18, garcia2024exploringthecontrasts pages 2-4, cherie2024immunohaematologicaspectsof pages 13-14, cherie2024immunohaematologicaspectsof pages 11-12).

| Mechanism | Molecular players (HGNC gene/protein symbols) | Cell types (CL IDs/names) | Biological processes (GO terms) | Cellular components (GO-CC) | Anatomy (UBERON) | Chemicals (CHEBI) | Primary sources (DOI URL, context ID) |
|---|---|---|---|---|---|---|---|
| NS1-induced endothelial dysfunction and glycocalyx degradation | Viral: NS1; Host: TLR4, MMP9, HPSE, sialidases (e.g., NEU1) | Endothelial cell (CL:0000115); Monocyte (CL:0000576) | Endothelial glycocalyx degradation; increased vascular permeability; inflammatory signaling (e.g., TLR4 pathway) | Extracellular region (GO:0005576); plasma membrane (GO:0005886) | Blood vessel (UBERON:0001981) | Heparan sulfate, HDL (lipoproteins), ROS | Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 1-2); Wong et al. 2024 (wong2024theinflammasomepathway pages 17-18) |
| Complement activation and modulation by NS1 | Viral: NS1; Host: C3, C4A/C4B, C4BP, vitronectin (VTN) | Endothelial cell (CL:0000115); Plasma proteins | Complement activation (classical and lectin pathways); regulation/inhibition of MAC formation | Extracellular region (GO:0005576); blood microparticle | Blood vessel (UBERON:0001981); Plasma (UBERON:0001969) | Complement components (C3/C4), vitronectin | Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 14-15); Wong et al. 2024 (wong2024theinflammasomepathway pages 17-18); Cherie et al. 2024 (cherie2024immunohaematologicaspectsof pages 11-12) |
| Antibody-dependent enhancement (FcγR-mediated) and downstream cytokine induction | Host: FCGR2A (FcγRIIA), FCGR3A (FcγRIIIA), IgG (antibody Fc) ; signaling: SYK, TBC1D24/SV2B (host factors reported) | Monocyte (CL:0000576); Macrophage (CL:0000235); Dendritic cell (CL:0000451); B cell (CL:0000236) | FcγR-mediated viral uptake; enhanced viral replication; elevated inflammatory cytokine production (IL-6, IL-10) | Endocytic vesicle (GO:0030135); plasma membrane (GO:0005886) | Blood / secondary lymphoid tissue (UBERON:0002293) | Immune complexes; cytokines (IL-6, IL-10) | Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 5-7); García & De Sanctis 2024 (garcia2024exploringthecontrasts pages 2-4); Wang et al. 2024 (yuya2024progressandchallenges pages 12-12) |
| Platelet / megakaryocyte dysfunction and thrombocytopenia | Platelet proteins: ITGA2B, ITGB3; Host immune: anti-NS1 antibodies (cross-reactive), desialylases, P-selectin (SELP) | Platelet (CL:0000182); Megakaryocyte (CL:0000094) | Impaired thrombopoiesis; platelet activation/apoptosis; immune-mediated platelet clearance | Platelet alpha granule (GO:0031091); plasma membrane | Bone marrow (UBERON:0002371); Blood (UBERON:0000178) | Platelet-activating factor (PAF); serotonin; sialic acid substrates | Cherie et al. 2024 (cherie2024immunohaematologicaspectsof pages 11-12); Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 5-7) |
| Innate immune antagonism (IFN pathway suppression by viral NS proteins) | Viral: NS2B/NS3, NS4A, NS4B, NS5; Host: STAT2, IRF3, RIG-I (DDX58) | Infected epithelial/immune cells: Keratinocyte; Monocyte; Dendritic cell | Type I IFN induction and signaling suppression; inhibition of ISG expression; modulation of mitochondrial antiviral signaling | Cytosol (GO:0005829); endoplasmic reticulum (GO:0005783); mitochondrion (GO:0005739) | Lymphoid organs; infected tissues (varies) | Interferons (IFN-α/β) (CHEBI:35352) | Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 1-2); Wang et al. 2024 (yuya2024progressandchallenges pages 12-12) |
| Inflammasome activation by NS1 | Viral: NS1; Host: NLRP3, CASP1, IL1B | Macrophage (CL:0000235); Monocyte (CL:0000576) | Activation of inflammasome complex; caspase-1 activation; IL-1β release (proinflammatory) | Cytosol (GO:0005829); inflammasome complex | Blood / infected tissues | IL-1β (CHEBI:26412) | Wong et al. 2024 (wong2024theinflammasomepathway pages 17-18); Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 5-7) |
| Mast cell mediators and vascular leak | Mast cell proteases: CMA1 (chymase), TPSAB1 (tryptase); histamine receptors | Mast cell (CL:0000095); Endothelial cell (CL:0000115) | Mast cell degranulation; release of chymase/tryptase/histamine → increased vascular permeability and vasodilation | Secretory granule (GO:0030141); extracellular region | Blood vessel (UBERON:0001981); Skin/vascular beds | Histamine; leukotrienes; chymase/tryptase substrates | Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 5-7); García & De Sanctis 2024 (garcia2024exploringthecontrasts pages 2-4); Cherie et al. 2024 (cherie2024immunohaematologicaspectsof pages 11-12) |
| Adaptive immunity bias (Th1/Th2, Treg dysfunction) | Host: IFNG, IL4, IL10, CD274 (PD-L1), FOXP3 (Tregs) | CD4+ T cell (CL:0000235); CD8+ T cell (CL:0000648); Regulatory T cell (Treg, CL:0000818); NKT cell (CL:0000784) | Th1/Th2 polarization; impaired regulatory T cell suppression; skewed helper responses influencing antibody class/glycosylation | Immunological synapse (GO:0001772); nucleus (GO:0005634) | Secondary lymphoid tissue (UBERON:0000029); blood | Cytokines (IFN-γ, IL-4, IL-10) | Malavige & Ogg 2024 (malavige2024molecularmechanismsin pages 1-2); Cherie et al. 2024 (cherie2024immunohaematologicaspectsof pages 11-12); Wang et al. 2024 (yuya2024progressandchallenges pages 12-12) |


*Table: Concise mapping of major dengue pathophysiology mechanisms to molecular players, affected cell types, GO/CC/UBERON/CHEBI terms, and primary recent sources (DOIs) to support ontology-style annotation and knowledgebase curation.*

## 1. Core Pathophysiology
- Primary mechanisms of vascular leak and shock:
  - NS1-induced endothelial dysfunction: NS1 engages TLR4 on monocytes/macrophages and endothelial cells to induce inflammatory cytokines; activates cathepsin L, sialidases, and heparinase to degrade endothelial sialic acids and the glycocalyx; upregulates PLA2, generating inflammatory lipid mediators; and partners with MMP-9 to reduce ZO-1 and β-catenin at junctions, promoting permeability (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 5-7). NS1-triggered endothelial dysfunction and glycocalyx disruption are central to severe disease in human-relevant models and can be mitigated by NS1 vaccination or NS1-blocking antibodies (https://doi.org/10.1371/journal.ppat.1012167, Apr 2024) (wong2024theinflammasomepathway pages 17-18).
  - Complement activation/modulation by NS1: NS1 antagonizes complement (e.g., C4), interacts with C4b-binding protein and vitronectin to limit membrane attack complex formation, but contributes to vascular leak through immune complex formation and anaphylatoxin generation in vivo (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7).
  - Mast cell mediators and lipid signaling: mast cell chymase/tryptase, platelet-activating factor, leukotrienes, and prostaglandins augment permeability and shock; chymase is a predictive biomarker of severe disease (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024; https://doi.org/10.3390/ijms252111624, Oct 2024) (malavige2024molecularmechanismsin pages 5-7, garcia2024exploringthecontrasts pages 2-4).
  - Inflammasome sensing of NS1: human/murine macrophages release IL‑1β in a caspase‑1–dependent manner upon NS1 exposure; NS1-induced inflammasome activation occurs without pyroptotic death and mice lacking caspase‑1/11 are more susceptible to lethal DENV, indicating a protective role (https://doi.org/10.1371/journal.ppat.1012167, Apr 2024) (wong2024theinflammasomepathway pages 17-18).

- Immune-mediated enhancement (ADE): sub-neutralizing IgG facilitates FcγR-mediated DENV uptake into monocytes/macrophages/DCs, increasing intracellular viral replication and inflammatory cytokines (e.g., IL‑10, IL‑6); outcome depends on antibody specificity, affinity, and concentration (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024; https://doi.org/10.3390/ijms252111624, Oct 2024; animal-model synthesis: https://doi.org/10.1080/22221751.2024.2404159, Sep 2024) (malavige2024molecularmechanismsin pages 5-7, garcia2024exploringthecontrasts pages 2-4, yuya2024progressandchallenges pages 12-12).

- Innate immune antagonism: DENV NS proteins suppress type I IFN at induction and signaling levels. NS2A/NS3/NS4B inhibit RIG‑I/MAVS signaling and ISG induction; NS5 targets STAT2 to blunt IFN signaling; these activities, together with mitochondrial pathway modulation, facilitate viremia and dissemination (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2).

## 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - Viral: NS1 (DENV NS1), NS2A, NS2B/NS3 (serine protease complex), NS4A, NS4B, NS5 (RdRp/methyltransferase) (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7).
  - Host innate signaling: TLR4 (TLR4), RIG-I (DDX58), IRF3 (IRF3), STAT2 (STAT2) (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15).
  - Endothelial/glycocalyx remodeling: MMP‑9 (MMP9), heparanase (HPSE), sialidases (e.g., NEU1), tight junction protein ZO‑1 (TJP1), β‑catenin (CTNNB1) (malavige2024molecularmechanismsin pages 5-7).
  - Complement: C4A/C4B, C4BP, C3, Vitronectin (VTN) (malavige2024molecularmechanismsin pages 14-15).
  - Inflammasome/cytokines: CASP1, IL1B, IL6, IL10, TNF (wong2024theinflammasomepathway pages 17-18, malavige2024molecularmechanismsin pages 5-7).
  - Fc receptors: FCGR2A (FcγRIIA), FCGR3A (FcγRIIIA) (malavige2024molecularmechanismsin pages 5-7, garcia2024exploringthecontrasts pages 2-4).
  - Hematology/platelets: P‑selectin (SELP), platelet integrins (ITGA2B/ITGB3) (cherie2024immunohaematologicaspectsof pages 11-12).

- Chemical entities (CHEBI):
  - Platelet-activating factor (PAF), histamine, leukotrienes, prostaglandins; interferon‑α/β; IL‑1β (malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18).

- Cell types (CL):
  - Endothelial cell (CL:0000115), monocyte (CL:0000576), macrophage (CL:0000235), dendritic cell (CL:0000451), mast cell (CL:0000095), platelet (CL:0000182), megakaryocyte (CL:0000094), CD4+ and CD8+ T cells (CL:0000235; CL:0000648), Treg (CL:0000818), NK cell (CL:0000623) (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18, cherie2024immunohaematologicaspectsof pages 11-12, cherie2024immunohaematologicaspectsof pages 13-14).

- Anatomical locations (UBERON):
  - Blood vessel (UBERON:0001981), plasma (UBERON:0001969), bone marrow (UBERON:0002371), secondary lymphoid tissue (UBERON:0000029) (malavige2024molecularmechanismsin pages 14-15, cherie2024immunohaematologicaspectsof pages 11-12).

## 3. Biological Processes (GO terms; disrupted)
- Endothelial barrier function and vascular permeability; endothelial glycocalyx organization; extracellular matrix disassembly (MMP‑mediated); complement activation (classical/lectin); Fc receptor–mediated endocytosis; type I interferon signaling; inflammasome activation and IL‑1β production; platelet activation and apoptosis; mast cell degranulation; cytokine production (IL‑6, IL‑10, TNF) (malavige2024molecularmechanismsin pages 5-7, malavige2024molecularmechanismsin pages 14-15, wong2024theinflammasomepathway pages 17-18, cherie2024immunohaematologicaspectsof pages 11-12, malavige2024molecularmechanismsin pages 1-2, garcia2024exploringthecontrasts pages 2-4, cherie2024immunohaematologicaspectsof pages 13-14).

## 4. Cellular Components (GO-CC)
- Endothelial plasma membrane and tight/adherens junctions; endothelial glycocalyx; extracellular region/plasma; endosomes and FcγR-containing vesicles; mitochondria and ER-derived replication complexes; inflammasome complexes; platelet alpha/dense granules (malavige2024molecularmechanismsin pages 5-7, malavige2024molecularmechanismsin pages 14-15, wong2024theinflammasomepathway pages 17-18, malavige2024molecularmechanismsin pages 1-2, cherie2024immunohaematologicaspectsof pages 11-12).

## 5. Disease Progression (sequence of events)
- Early/febrile phase: high viremia with fever, myalgia, headache; NS1 and virions circulate; innate antagonism by NS proteins delays antiviral state (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2).
- Critical phase (typically days 3–6): NS1-driven endothelial dysfunction and glycocalyx degradation; complement and mast cell activation; rising inflammatory lipids and cytokines; plasma leakage into pleural/peritoneal spaces; hemoconcentration; shock in severe cases (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024; https://doi.org/10.3390/ijms252111624, Oct 2024) (malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7, garcia2024exploringthecontrasts pages 2-4).
- Recovery phase: reabsorption of extravasated fluid, bradycardia/pruritus common; risk for fluid overload if resuscitation over-continued (review) (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2).

## 6. Phenotypic Manifestations (and mechanistic links)
- Plasma leakage and shock: due to NS1-mediated glycocalyx and junctional disruption, complement anaphylatoxins, mast cell and lipid mediators (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024; https://doi.org/10.1371/journal.ppat.1012167, Apr 2024) (malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18).
- Hemorrhage and coagulopathy: platelet activation and apoptosis, NS1–platelet interactions, anti-NS1 cross-reactivity with hemostatic proteins, endothelial activation; disturbances in coagulation/fibrinolysis (https://doi.org/10.3390/v16071090, Jul 2024; https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (cherie2024immunohaematologicaspectsof pages 11-12, malavige2024molecularmechanismsin pages 5-7).
- Thrombocytopenia: reduced thrombopoiesis (megakaryocyte dysfunction), increased platelet activation/apoptosis and immune clearance (desialylation, anti-platelet autoantibodies) (https://doi.org/10.3390/v16071090, Jul 2024; https://doi.org/10.1017/erm.2024.18, Oct 2024) (cherie2024immunohaematologicaspectsof pages 11-12, cherie2024immunohaematologicaspectsof pages 13-14).
- Neurologic and systemic complications: reviews highlight expanding reports of CNS/PNS involvement; systemic cytokine storm contributes to multiorgan dysfunction (https://doi.org/10.3390/ijms252111624, Oct 2024) (garcia2024exploringthecontrasts pages 2-4).

## Expert opinions and analysis (authoritative sources)
- Trends in Molecular Medicine (2024) emphasizes NS1 as a central mediator of vascular leak, interacting with TLR4, complement, lipoproteins, and MMP‑9, with strong translational implications (biomarkers and NS1-targeting) (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7).
- PLOS Pathogens (2024) defines NS1 as an inflammasome-activating DAMP in macrophages; genetic ablation of caspase‑1/11 increases susceptibility, suggesting a protective axis that could be harnessed therapeutically (https://doi.org/10.1371/journal.ppat.1012167, Apr 2024) (wong2024theinflammasomepathway pages 17-18).
- Emerging Microbes & Infections (2024) synthesizes ADE in animal models and reinforces its relevance to vaccine and challenge models, guiding design and interpretation of immune responses in vivo (https://doi.org/10.1080/22221751.2024.2404159, Sep 2024) (yuya2024progressandchallenges pages 12-12).

## Current applications and real-world implementations
- Vaccines: CYD‑TDV (Dengvaxia) and TAK‑003 (Qdenga) are licensed; real-world and trial data emphasize baseline serostatus and balanced immunity to reduce ADE risk; TAK‑003 elicits durable T‑cell responses to NS proteins in children/adolescents (review) (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2).
- NS1-targeted strategies: neutralizing/blocking anti‑NS1 antibodies and vaccines mitigate NS1-induced endothelial dysfunction in preclinical models (review and primary) (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024; https://doi.org/10.1371/journal.ppat.1012167, Apr 2024) (malavige2024molecularmechanismsin pages 14-15, wong2024theinflammasomepathway pages 17-18).
- Biomarkers and supportive care: recognition of critical-phase risk using clinical/lab markers consistent with NS1 and cytokine biology (hemoconcentration, platelet nadir) guides fluid therapy and monitoring (review) (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2).

## Relevant statistics and data (recent)
- “Half of the global population is at risk,” with a large and rising burden over two decades; severe disease is driven by vascular leakage, organ dysfunction, and bleeding (reviewed 2024) (https://doi.org/10.1016/j.molmed.2024.03.006, May 2024) (malavige2024molecularmechanismsin pages 1-2).
- Global transmission was reported in all WHO regions in 2023, underscoring expanding geographic risk (https://doi.org/10.3390/ijms252111624, Oct 2024) (garcia2024exploringthecontrasts pages 2-4).

## Evidence items (with PMIDs/DOIs, URLs, dates)
- Malavige GN, Ogg GS. Molecular mechanisms in the pathogenesis of dengue infections. Trends Mol Med. 2024-05. DOI: 10.1016/j.molmed.2024.03.006. URL: https://doi.org/10.1016/j.molmed.2024.03.006 (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7).
- Wong MP et al. The inflammasome pathway is activated by dengue virus non-structural protein 1 and is protective during dengue virus infection. PLOS Pathog. 2024-04. DOI: 10.1371/journal.ppat.1012167. URL: https://doi.org/10.1371/journal.ppat.1012167 (wong2024theinflammasomepathway pages 17-18).
- García AH, De Sanctis JB. Exploring the Contrasts and Similarities of Dengue and SARS-CoV-2 Infections. Int J Mol Sci. 2024-10. DOI: 10.3390/ijms252111624. URL: https://doi.org/10.3390/ijms252111624 (garcia2024exploringthecontrasts pages 2-4).
- Cherie TJJ et al. Immuno-haematologic Aspects of Dengue Infection. Viruses. 2024-07. DOI: 10.3390/v16071090. URL: https://doi.org/10.3390/v16071090 (cherie2024immunohaematologicaspectsof pages 13-14, cherie2024immunohaematologicaspectsof pages 11-12).
- Wang Y et al. Progress and challenges in development of animal models for dengue virus infection. Emerg Microbes Infect. 2024-09. DOI: 10.1080/22221751.2024.2404159. URL: https://doi.org/10.1080/22221751.2024.2404159 (yuya2024progressandchallenges pages 12-12).

## Structured annotations
- Genes/Proteins (HGNC): NS1 (viral), NS2A, NS2B/NS3, NS4A, NS4B, NS5; TLR4; DDX58 (RIG‑I); IRF3; STAT2; MMP9; HPSE; NEU1; TJP1; CTNNB1; C4A/C4B; C4BP; C3; VTN; CASP1; IL1B; IL6; IL10; TNF; FCGR2A; FCGR3A; SELP; ITGA2B; ITGB3 (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18, cherie2024immunohaematologicaspectsof pages 11-12, garcia2024exploringthecontrasts pages 2-4).
- GO Biological Processes: endothelial glycocalyx organization; regulation of vascular permeability; complement activation (classical pathway); Fc receptor–mediated endocytosis; type I interferon signaling pathway; inflammasome complex assembly; platelet activation; mast cell degranulation; cytokine production involved in immune response (malavige2024molecularmechanismsin pages 5-7, malavige2024molecularmechanismsin pages 14-15, wong2024theinflammasomepathway pages 17-18, malavige2024molecularmechanismsin pages 1-2, cherie2024immunohaematologicaspectsof pages 11-12, garcia2024exploringthecontrasts pages 2-4).
- GO Cellular Components: plasma membrane; extracellular region; tight junction; adherens junction; endocytic vesicle; mitochondrion; endoplasmic reticulum; inflammasome complex; platelet granule (malavige2024molecularmechanismsin pages 5-7, malavige2024molecularmechanismsin pages 14-15, wong2024theinflammasomepathway pages 17-18, malavige2024molecularmechanismsin pages 1-2, cherie2024immunohaematologicaspectsof pages 11-12).
- Cell types (CL): endothelial cell (CL:0000115); monocyte (CL:0000576); macrophage (CL:0000235); dendritic cell (CL:0000451); mast cell (CL:0000095); platelet (CL:0000182); megakaryocyte (CL:0000094); CD4+ T cell (CL:0000235); CD8+ T cell (CL:0000648); regulatory T cell (CL:0000818); NK cell (CL:0000623) (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18, cherie2024immunohaematologicaspectsof pages 11-12, cherie2024immunohaematologicaspectsof pages 13-14).
- Anatomy (UBERON): blood vessel (UBERON:0001981); plasma (UBERON:0001969); bone marrow (UBERON:0002371); secondary lymphoid tissue (UBERON:0000029) (malavige2024molecularmechanismsin pages 14-15, cherie2024immunohaematologicaspectsof pages 11-12).
- Chemical entities (CHEBI): platelet-activating factor; histamine; leukotrienes; prostaglandins; interferon‑α/β; interleukin‑1β (malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18).

## Notes on evidence scope
Where precise 2023–2024 global case numbers are requested, our current evidence includes authoritative statements of global risk and WHO-region transmission in 2023; additional WHO surveillance data would refine counts. Mechanistic sections emphasize 2023–2024 peer‑reviewed reviews and primary studies that directly support NS1-driven vascular injury, ADE, IFN antagonism, inflammasome activation, hematologic dysfunction, and adaptive immune skewing (malavige2024molecularmechanismsin pages 1-2, malavige2024molecularmechanismsin pages 14-15, malavige2024molecularmechanismsin pages 5-7, wong2024theinflammasomepathway pages 17-18, garcia2024exploringthecontrasts pages 2-4, cherie2024immunohaematologicaspectsof pages 11-12, yuya2024progressandchallenges pages 12-12).

References

1. (malavige2024molecularmechanismsin pages 1-2): Gathsaurie Neelika Malavige and Graham S. Ogg. Molecular mechanisms in the pathogenesis of dengue infections. Trends in Molecular Medicine, 30:484-498, May 2024. URL: https://doi.org/10.1016/j.molmed.2024.03.006, doi:10.1016/j.molmed.2024.03.006. This article has 28 citations and is from a domain leading peer-reviewed journal.

2. (malavige2024molecularmechanismsin pages 14-15): Gathsaurie Neelika Malavige and Graham S. Ogg. Molecular mechanisms in the pathogenesis of dengue infections. Trends in Molecular Medicine, 30:484-498, May 2024. URL: https://doi.org/10.1016/j.molmed.2024.03.006, doi:10.1016/j.molmed.2024.03.006. This article has 28 citations and is from a domain leading peer-reviewed journal.

3. (malavige2024molecularmechanismsin pages 5-7): Gathsaurie Neelika Malavige and Graham S. Ogg. Molecular mechanisms in the pathogenesis of dengue infections. Trends in Molecular Medicine, 30:484-498, May 2024. URL: https://doi.org/10.1016/j.molmed.2024.03.006, doi:10.1016/j.molmed.2024.03.006. This article has 28 citations and is from a domain leading peer-reviewed journal.

4. (wong2024theinflammasomepathway pages 17-18): Marcus P. Wong, Evan Y. W. Juan, Felix Pahmeier, Sai S. Chelluri, Phoebe Wang, Bryan Castillo-Rojas, Sophie F. Blanc, Scott B. Biering, Russell E. Vance, and Eva Harris. The inflammasome pathway is activated by dengue virus non-structural protein 1 and is protective during dengue virus infection. PLOS Pathogens, 20:e1012167, Apr 2024. URL: https://doi.org/10.1371/journal.ppat.1012167, doi:10.1371/journal.ppat.1012167. This article has 11 citations and is from a highest quality peer-reviewed journal.

5. (garcia2024exploringthecontrasts pages 2-4): Alexis Hipólito García and Juan Bautista De Sanctis. Exploring the contrasts and similarities of dengue and sars-cov-2 infections during the covid-19 era. International Journal of Molecular Sciences, Oct 2024. URL: https://doi.org/10.3390/ijms252111624, doi:10.3390/ijms252111624. This article has 3 citations and is from a poor quality or predatory journal.

6. (cherie2024immunohaematologicaspectsof pages 13-14): Tan Jiao Jie Cherie, Clarice Shi Hui Choong, Muhammad Bilal Abid, Matthew W. Weber, Eng Soo Yap, Suranjith L. Seneviratne, Visula Abeysuriya, and Sanjay de Mel. Immuno-haematologic aspects of dengue infection: biologic insights and clinical implications. Viruses, 16:1090, Jul 2024. URL: https://doi.org/10.3390/v16071090, doi:10.3390/v16071090. This article has 21 citations and is from a poor quality or predatory journal.

7. (cherie2024immunohaematologicaspectsof pages 11-12): Tan Jiao Jie Cherie, Clarice Shi Hui Choong, Muhammad Bilal Abid, Matthew W. Weber, Eng Soo Yap, Suranjith L. Seneviratne, Visula Abeysuriya, and Sanjay de Mel. Immuno-haematologic aspects of dengue infection: biologic insights and clinical implications. Viruses, 16:1090, Jul 2024. URL: https://doi.org/10.3390/v16071090, doi:10.3390/v16071090. This article has 21 citations and is from a poor quality or predatory journal.

8. (yuya2024progressandchallenges pages 12-12): Wang Yuya, Yang Yuansong, Liu Susu, Ling Chen, Wu Yong, Wang Yining, Wang YouChun, and Fan Changfa. Progress and challenges in development of animal models for dengue virus infection. Emerging Microbes &amp; Infections, Sep 2024. URL: https://doi.org/10.1080/22221751.2024.2404159, doi:10.1080/22221751.2024.2404159. This article has 8 citations and is from a domain leading peer-reviewed journal.