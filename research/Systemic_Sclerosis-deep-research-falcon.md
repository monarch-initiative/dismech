---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:16.089573'
end_time: '2025-12-18T09:52:46.348501'
duration_seconds: 450.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Systemic Sclerosis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Systemic Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Systemic Sclerosis**.
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
- **Disease Name:** Systemic Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Systemic Sclerosis**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Systemic Sclerosis (SSc; scleroderma)
- MONDO ID: not specified in source set
- Category: Autoimmune

## Pathophysiology description (current understanding, 2023–2024 prioritized)
Systemic sclerosis is a multisystem autoimmune disease defined by a triad of early microvasculopathy, immune dysregulation with disease-specific autoantibodies and type I interferon (IFN-I) activation, and progressive fibroblast activation culminating in tissue fibrosis. Recent work confirms that defective angiogenesis and endothelial injury are early, often pre-fibrotic features; “defective angiogenesis … represents a hallmark of early-stage disease, usually preceding the onset of tissue fibrosis” and involves endothelial apoptosis, senescence, and endothelial-to-mesenchymal transition (EndoMT) with impaired pro-angiogenic signaling (e.g., dysregulated VEGF/Angiopoietin axes) (Published Jun 2024; https://doi.org/10.3390/biomedicines12061331) (romano2024recentinsightsinto pages 17-18). Contemporary reviews capturing 2023 advances reiterate the canonical sequence—microvascular damage, immune activation/autoantibodies, then fibrosis—while adding single-cell and genetic resolution of pathway heterogeneity across autoantibody subsets (Published Apr 2024; https://doi.org/10.55563/clinexprheumatol/is29he) (lepri2024systemicsclerosisone pages 1-2).

At the immune level, IFN-I pathway activation (pDC/monocyte signatures, SIGLEC1 upregulation) and B-cell abnormalities are prominent; B-cell/autoantibody phenotypes correlate with organ involvement, including active, immunoglobulin-secreting anti–topoisomerase I responses that associate with interstitial lung disease (ILD) severity (Published Jul 2023; https://doi.org/10.1136/rmdopen-2023-003148) (lepri2024systemicsclerosisone pages 1-2). Vascular and immune perturbations converge on fibroblasts via profibrotic signaling nodes—TGF-β/SMAD, PDGF/CTGF, Wnt, and Hippo (YAP/TAZ)—with recent single-cell analyses in 2024 linking Hippo/YAP–TAZ activity to myofibroblast and EndoMT trajectories in SSc skin (Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6) (lepri2024systemicsclerosisone pages 1-2). Metabolic reprogramming in stromal and immune compartments (glycolysis/lactate, TCA/OXPHOS shifts) is increasingly implicated, aligning with metabolomic fingerprints (amino acid, acylcarnitine, and TCA intermediates) that distinguish subtypes and pulmonary complications (Published Aug 2023; https://doi.org/10.3389/fmolb.2023.1215039) (maggio2023biomarkersinsystemic pages 6-8).

Genetically, large-scale GWAS (2024) identified six novel SSc susceptibility loci in a Japanese cohort (1,428 cases; 112,599 controls), including a lead signal in the FCGR/FCRL region and context-specific interaction with IRF8-related variants; cross-ancestry meta-analysis added 30 loci, emphasizing roles for B-cell biology and IRF8 in susceptibility (Published Jan 2024; https://doi.org/10.1038/s41467-023-44541-z) (lepri2024systemicsclerosisone pages 1-2). Clinically, these mechanisms underlie organ complications: ILD and pulmonary arterial hypertension (PAH) remain leading drivers of morbidity and mortality, while cardiac involvement (arrhythmia, myocardial fibrosis) and scleroderma renal crisis reflect microvascular injury, immune activation, and fibrosis interplay (Published Aug 2024; https://doi.org/10.1007/s00296-024-05699-x; Published Apr 2024; https://doi.org/10.3390/ijms25094728) (lepri2024systemicsclerosisone pages 1-2).

## 1. Core Pathophysiology
- Primary mechanisms
  - Early microvasculopathy: endothelial dysfunction, apoptosis/senescence, impaired angiogenesis, and EndoMT precede fibrosis; capillary rarefaction and abnormal architecture are early clinical hallmarks (nailfold capillaroscopy) (Published Jun 2024; https://doi.org/10.3390/biomedicines12061331) (romano2024recentinsightsinto pages 17-18).
  - Immune dysregulation: IFN-I axis activation (e.g., SIGLEC1 upregulation), B-cell activation with disease-stratifying autoantibodies (ACA, ATA, RNAP III) and functional antibodies; chemokine/cytokine milieu (IL-6, CCL2) recruits monocytes/macrophages and polarizes T cells (Published Sep 2023; https://doi.org/10.3390/cimb45100490; Published Jun 2024; https://doi.org/10.31138/mjr.270324.tis) (maggio2023biomarkersinsystemic pages 2-4, lepri2024systemicsclerosisone pages 1-2).
  - Fibroblast activation and ECM remodeling: canonical TGF-β/SMAD signaling, PDGF/CTGF pathways, noncanonical Wnt and Hippo/YAP–TAZ programs drive myofibroblast differentiation and excessive matrix deposition (Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6) (lepri2024systemicsclerosisone pages 1-2).
- Dysregulated molecular pathways
  - Angiogenesis dysregulation: increased Ang-2 with decreased Ang-1; paradoxical early VEGF elevation with failed angiogenesis; reduced endothelial progenitors (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
  - IFN-I/type I interferon signaling: monocyte/B-cell IFN signatures correlate with disease activity and organ complications (Published Jun 2024; https://doi.org/10.31138/mjr.270324.tis) (lepri2024systemicsclerosisone pages 1-2).
  - TGF-β axis: increased TGF-β receptor expression and activated SMAD signaling in lesional skin; context-dependent systemic vs local levels (Published May 2023; https://doi.org/10.1007/s10238-022-00841-0) (jimenez2025areviewof pages 1-2).
  - Hippo/YAP–TAZ and Wnt integration in mesenchymal programs and EndoMT (Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6; Published Apr 2024; https://doi.org/10.55563/clinexprheumatol/is29he) (lepri2024systemicsclerosisone pages 1-2).
- Affected cellular processes
  - Endothelial-to-mesenchymal transition, impaired angiogenesis, leukocyte recruitment (CCL2/IL-6), fibroblast-to-myofibroblast transition, ECM synthesis/turnover (Published Jun 2024; https://doi.org/10.3390/biomedicines12061331; Published Sep 2023; https://doi.org/10.3390/cimb45100490) (romano2024recentinsightsinto pages 17-18, maggio2023biomarkersinsystemic pages 6-8).

## 2. Key Molecular Players
- Genes/Proteins (HGNC)
  - TGF-β pathway: TGFB1, TGFBR1/2, SMAD2/3; effector CCN2/CTGF (Published May 2023; https://doi.org/10.1007/s10238-022-00841-0) (jimenez2025areviewof pages 1-2).
  - Angiogenesis/vasoactive: VEGFA, ANGPT1/2, EDN1 (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
  - Immune: IRF8; Fc gamma receptor cluster (FCGR/FCRL locus) (Published Jan 2024; https://doi.org/10.1038/s41467-023-44541-z) (lepri2024systemicsclerosisone pages 1-2); SIGLEC1 (IFN marker) (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
  - Chemokines/cytokines: CXCL4, IL6, CCL2 (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
  - Mechanotransduction/developmental: YAP1/WWTR1 (YAP/TAZ; Hippo), WNT5A (Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6; Published Apr 2024; https://doi.org/10.55563/clinexprheumatol/is29he) (lepri2024systemicsclerosisone pages 1-2).
- Chemical entities (CHEBI)
  - Endothelin-1, VEGF-A, TGF-β1, PDGF isoforms, CXCL4 (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
- Cell types (CL)
  - Endothelial cell (CL:0000115), fibroblast (CL:0000064), monocyte/macrophage (CL:0000235), B cell (CL:0000236), T cell (CL:0000084), endothelial progenitor cell (Published Jun 2024; https://doi.org/10.3390/biomedicines12061331; Published Sep 2023; https://doi.org/10.3390/cimb45100490) (romano2024recentinsightsinto pages 17-18, maggio2023biomarkersinsystemic pages 6-8).
- Anatomical locations (UBERON)
  - Skin (UBERON:0002097), lung (UBERON:0002048), heart (UBERON:0000948), kidney (UBERON:0002113), peripheral microvasculature (capillary bed) (Published Aug 2024; https://doi.org/10.1007/s00296-024-05699-x; Published Apr 2024; https://doi.org/10.3390/ijms25094728) (lepri2024systemicsclerosisone pages 1-2).

| HGNC symbol | Name | Role in SSc (summary) | Key pathway (GO term suggestion) | Cellular component (GO-CC) | Cell types (CL terms) | Anatomical sites (UBERON) | Notable molecules/chemicals (CHEBI) | Recent sources (URL, year) |
|---|---|---|---|---|---|---|---|---|
| TGFB1 | Transforming growth factor beta 1 | Central profibrotic cytokine driving fibroblast-to-myofibroblast transition and ECM deposition in skin and lung fibrosis | TGF-beta receptor signaling pathway (GO:0007179) | Extracellular region / secreted (GO:0005576) | Fibroblast (CL:0000064), endothelial cell (CL:0000115) | Skin (UBERON:0002097), Lung (UBERON:0002048) | TGF-β1 (CHEBI:TGF-β1) | https://doi.org/10.1007/s10238-022-00841-0 (2023) (jimenez2025areviewof pages 1-2, maggio2023biomarkersinsystemic pages 6-8) |
| TGFBR1 / TGFBR2 | TGF-β receptors type I & II | Receptors mediating SMAD phosphorylation and downstream profibrotic transcriptional program in SSc fibroblasts | TGF-beta receptor signaling pathway (GO:0007179) | Plasma membrane (GO:0005886) | Fibroblast (CL:0000064), Endothelial cell (CL:0000115) | Skin, Lung | — (receptor complex) | https://doi.org/10.1007/s10238-022-00841-0 (2023) (jimenez2025areviewof pages 1-2) |
| SMAD2 / SMAD3 | SMAD family members 2 & 3 | Intracellular mediators of canonical TGF-β signaling promoting collagen gene expression in SSc fibroblasts | Positive regulation of transcription by SMAD (GO:0060395) | Nucleus / cytoplasm (GO:0005634 / GO:0005737) | Fibroblast (CL:0000064) | Skin, Lung | p-SMAD2/3 (CHEBI:phosphoprotein) | https://doi.org/10.3389/fimmu.2025.1551911 (2025) (jimenez2025areviewof pages 1-2, jimenez2025areviewof pages 9-10) |
| CCN2 (CTGF) | Connective tissue growth factor | Matricellular effector induced by TGF-β that amplifies fibroblast activation and matrix deposition | Regulation of cell proliferation and ECM organization (GO:0030198) | Extracellular matrix (GO:0031012) | Fibroblast (CL:0000064) | Skin, Heart, Lung | CTGF/CCN2 (CHEBI:CTGF) | https://doi.org/10.3389/fimmu.2025.1551911 (2025) (jimenez2025areviewof pages 1-2) |
| PDGFA / PDGFRB | Platelet-derived growth factor A / receptor β | Stimulates fibroblast proliferation and perivascular smooth muscle activation contributing to vascular remodeling and fibrosis | PDGF receptor signaling pathway (GO:0048008) | Plasma membrane / extracellular (GO:0005886 / GO:0005576) | Fibroblast, Pericyte, Vascular smooth muscle cell | Skin, Lung, Vasculature | PDGF-BB (CHEBI:PDGF) | https://doi.org/10.3389/fimmu.2025.1551911 (2025) (jimenez2025areviewof pages 1-2) |
| EDN1 | Endothelin 1 (endothelin-1) | Vasoconstrictor elevated in SSc vasculopathy; implicated in vessel tone dysregulation and may link to fibrosis | Endothelin signaling (GO:0007186) | Secreted peptide (GO:0005576) | Endothelial cell (CL:0000115), VSMC | Peripheral vasculature, Lung | Endothelin-1 (CHEBI:ET-1) | https://doi.org/10.3390/cimb45100490 (2023) (maggio2023biomarkersinsystemic pages 2-4) |
| VEGFA | Vascular endothelial growth factor A | Dysregulated/ectopic VEGF expression: early elevated VEGF but defective angiogenesis and capillary loss in SSc | VEGF receptor signaling pathway (GO:0048010) | Secreted / extracellular (GO:0005576) | Endothelial cell (CL:0000115), Endothelial progenitor cell | Skin microvasculature, Lung | VEGF-A (CHEBI:VEGF) | https://doi.org/10.3390/cimb45100490 (2023), https://doi.org/10.3390/biomedicines12061331 (2024) (maggio2023biomarkersinsystemic pages 6-8, romano2024recentinsightsinto pages 17-18) |
| ANGPT1 / ANGPT2 | Angiopoietin-1 / -2 | Imbalanced Ang1 (decreased) / Ang2 (increased) axis contributes to aberrant angiogenesis and vessel instability in SSc | Angiopoietin-Tie signaling (GO:0043066) | Extracellular region / secreted (GO:0005576) | Endothelial cell (CL:0000115), Pericyte | Microvasculature (skin) | Angiopoietin-2 (CHEBI:ANGPT2) | https://doi.org/10.3390/cimb45100490 (2023) (maggio2023biomarkersinsystemic pages 6-8) |
| CXCL4 | C-X-C motif chemokine ligand 4 (platelet factor 4) | Proposed DAMP / biomarker; promotes IFN-I and inflammatory signaling and associates with lung fibrosis and worse skin scores | Chemokine-mediated signaling pathway (GO:0070098) | Extracellular region / platelet granule (GO:0005576) | Platelet, Plasmacytoid dendritic cell, Monocyte | Skin, Lung | CXCL4 (CHEBI:CXCL4) | https://doi.org/10.3390/cimb45100490 (2023), https://doi.org/10.3390/ijms26062421 (2025) (maggio2023biomarkersinsystemic pages 6-8, bazso2025theroleof pages 1-2) |
| IL6 | Interleukin-6 | Pro-inflammatory/profibrotic cytokine; correlates with mRSS and progressive skin disease and ILD risk | JAK-STAT signaling pathway (GO:0043401) | Secreted cytokine (GO:0005576) | Macrophage, T cell, Fibroblast | Skin, Lung | IL-6 (CHEBI:IL6) | https://doi.org/10.3390/cimb45100490 (2023) (maggio2023biomarkersinsystemic pages 6-8) |
| CCL2 | C-C motif chemokine ligand 2 (MCP-1) | Monocyte chemoattractant linked to macrophage recruitment and ILD / skin severity in SSc | Monocyte chemotaxis (GO:0002548) | Extracellular region (GO:0005576) | Monocyte, Macrophage | Lung, Skin | CCL2 (CHEBI:CCL2) | https://doi.org/10.3390/cimb45100490 (2023) (maggio2023biomarkersinsystemic pages 6-8) |
| IRF8 | Interferon regulatory factor 8 | Genetic susceptibility locus; regulator of IFN-I responses and B cell / myeloid programs implicated in SSc risk and B cell biology | Regulation of type I interferon production (GO:0032479) | Nucleus (GO:0005634) | B cell (CL:0000236), Dendritic cell (CL:0000451), Monocyte | Blood / Immune system | IRF8 (CHEBI:IRF8) | https://doi.org/10.1038/s41467-023-44541-z (2024) (lepri2024systemicsclerosisone pages 1-2) |
| FCGR cluster (e.g., FCGR2A/FCGR3A) | Fc gamma receptors IIa / IIIa region | GWAS locus (FCGR/FCRL region) with strong association in Asian cohort; implicates B cell/FC receptor–mediated immunity in SSc susceptibility | Fc-gamma receptor signaling (GO:0038094) | Plasma membrane (GO:0005886) | B cell, NK cell, Macrophage | Immune system compartments | IgG / immune complexes (CHEBI:IgG) | https://doi.org/10.1038/s41467-023-44541-z (2024) (lepri2024systemicsclerosisone pages 1-2) |
| YAP1 / WWTR1 (TAZ) | YAP1 and WWTR1 (TAZ) Hippo pathway effectors | Hippo/YAP-TAZ signaling implicated in mesenchymal differentiation and myofibroblast/EndoMT fibrotic programs in SSc skin | Hippo signaling (GO:0035329) | Nucleus / cytoplasm (GO:0005634 / GO:0005737) | Fibroblast (CL:0000064), Endothelial-to-mesenchymal cells | Skin | YAP/TAZ transcriptional coactivators (CHEBI:YAP) | https://doi.org/10.1038/s41467-023-44645-6 (2024) (lepri2024systemicsclerosisone pages 1-2) |
| WNT5A | Wnt family member 5A | Non-canonical Wnt implicated in fibroblast activation, crosstalk with Hippo and TGF-β pathways | Wnt signaling pathway (GO:0016055) | Secreted signaling molecule (GO:0005576) | Fibroblast, Endothelial cell | Skin, Lung | Wnt5a (CHEBI:WNT5A) | https://doi.org/10.55563/clinexprheumatol/is29he (2024) (lepri2024systemicsclerosisone pages 1-2) |
| SIGLEC1 | Sialic acid binding Ig-like lectin 1 (CD169) | IFN-I–inducible marker (monocyte/macrophage) used as surrogate of IFN activation in SSc; links IFN axis to immune activation | Type I interferon signaling pathway (GO:0060337) | Plasma membrane (GO:0005886) | Monocyte / Macrophage (CL:0000235) | Blood, Skin | SIGLEC1 (CHEBI:SIGLEC1) | https://doi.org/10.3390/cimb45100490 (2023) (maggio2023biomarkersinsystemic pages 6-8) |


*Table: Concise table mapping principal genes/proteins implicated in systemic sclerosis to roles, suggested GO pathways, cellular components, cell types, anatomical sites, notable chemicals, and recent sources (2023–2025) for rapid reference.*

## 3. Biological Processes (GO) disrupted
- Angiogenesis and vasculature development: angiogenesis (GO:0001525); VEGF receptor signaling (GO:0048010); angiopoietin signaling (GO:0043066) (Published Sep 2023; https://doi.org/10.3390/cimb45100490; Published Jun 2024; https://doi.org/10.3390/biomedicines12061331) (maggio2023biomarkersinsystemic pages 6-8, romano2024recentinsightsinto pages 17-18).
- Type I IFN signaling and antiviral response: type I interferon signaling (GO:0060337); regulation of type I interferon production (GO:0032479) (Published Jun 2024; https://doi.org/10.31138/mjr.270324.tis) (lepri2024systemicsclerosisone pages 1-2).
- Fibrogenic programming: TGF-β receptor signaling (GO:0007179); positive regulation of transcription by SMAD proteins (GO:0060395); extracellular matrix organization (GO:0030198) (Published May 2023; https://doi.org/10.1007/s10238-022-00841-0) (jimenez2025areviewof pages 1-2).
- Leukocyte trafficking/inflammation: monocyte chemotaxis (GO:0002548), cytokine-mediated signaling (GO:0019221) (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
- Mechanotransduction/developmental: Hippo signaling (GO:0035329); Wnt signaling (GO:0016055) (Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6; Published Apr 2024; https://doi.org/10.55563/clinexprheumatol/is29he) (lepri2024systemicsclerosisone pages 1-2).

## 4. Cellular Components (GO-CC)
- Extracellular region/matrix (GO:0005576/GO:0031012): cytokines/chemokines (TGF-β, IL-6, CXCL4), ECM proteins (collagens), CTGF (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
- Plasma membrane (GO:0005886): TGF-β receptors, PDGFR, Fcγ receptors, endothelin receptors (Published Jan 2024; https://doi.org/10.1038/s41467-023-44541-z) (lepri2024systemicsclerosisone pages 1-2).
- Nucleus/cytoplasm (GO:0005634/GO:0005737): SMAD transcriptional complexes; YAP/TAZ co-activators (Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6) (lepri2024systemicsclerosisone pages 1-2).

## 5. Disease Progression (sequence of events)
- Initiation: genetic susceptibility (FCGR/FCRL, IRF8) + environmental triggers; endothelial injury and microvasculopathy manifested by Raynaud’s phenomenon and nailfold capillaroscopy abnormalities (Published Jan 2024; https://doi.org/10.1038/s41467-023-44541-z; Published Sep 2023; https://doi.org/10.3390/cimb45100490) (lepri2024systemicsclerosisone pages 1-2, maggio2023biomarkersinsystemic pages 2-4).
- Propagation: IFN-I activation (SIGLEC1), B-cell priming and autoantibody production (ACA, ATA, RNAP III; functional antibodies), chemokine-driven recruitment (CCL2) of monocytes/macrophages; EndoMT and impaired angiogenesis persist (Published Sep 2023; https://doi.org/10.3390/cimb45100490; Published Jun 2024; https://doi.org/10.3390/biomedicines12061331) (maggio2023biomarkersinsystemic pages 6-8, romano2024recentinsightsinto pages 17-18).
- Fibrotic consolidation: TGF-β/SMAD-dominant fibroblast programs with PDGF/CTGF amplification, crosstalk with Wnt and Hippo/YAP–TAZ; ECM deposition and organ remodeling (Published May 2023; https://doi.org/10.1007/s10238-022-00841-0; Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6) (jimenez2025areviewof pages 1-2, lepri2024systemicsclerosisone pages 1-2).
- Organ phenotypes emerge according to autoantibody/endotype and tissue context (e.g., ATA→ILD progression, ACA→PAH risk; RNAP III→renal crisis risk), with clinical course shaped by ongoing vascular injury and fibrosis (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 2-4).

## 6. Phenotypic Manifestations (selected associations)
- Vascular/skin: Raynaud’s phenomenon, nailfold capillary dropout, digital ulcers, telangiectasias—reflect microvascular damage and defective angiogenesis (Published Sep 2023; https://doi.org/10.3390/cimb45100490; Published Jun 2024; https://doi.org/10.3390/biomedicines12061331) (maggio2023biomarkersinsystemic pages 2-4, romano2024recentinsightsinto pages 17-18).
- Lung: ILD (fibrosing alveolitis) linked to ATA+ B-cell activity and inflammatory chemokines; PAH from pulmonary arteriopathy and endothelial dysfunction (Published Jul 2023; https://doi.org/10.1136/rmdopen-2023-003148; Published Apr 2024; https://doi.org/10.3390/ijms25094728) (lepri2024systemicsclerosisone pages 1-2).
- Heart: arrhythmias, myocardial fibrosis; pathogenesis traces microvascular dysfunction and fibrosis, often subclinical early (Published Aug 2024; https://doi.org/10.1007/s00296-024-05699-x) (lepri2024systemicsclerosisone pages 1-2).
- Kidney: scleroderma renal crisis associated with RNAP III autoimmunity and acute microangiopathy (summarized 2023–2024) (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 2-4).

## Recent developments and latest research (2023–2024)
- Genetics (Jan 2024): Largest Asian SSc GWAS (1,428 cases; 112,599 controls) identified a lead SNP in the FCGR/FCRL region and interaction with IRF8 binding-site variation; meta-analysis with European data detected 30 additional significant loci, and B-cell/IRF8 biology improved polygenic model performance (URL: https://doi.org/10.1038/s41467-023-44541-z; Published Jan 2024) (lepri2024systemicsclerosisone pages 1-2).
- Vascular biology (Jun 2024): Updated synthesis of defective angiogenesis/EndoMT pathways and EC senescence in SSc, with translational targets to restore angiogenesis and limit EndoMT (URL: https://doi.org/10.3390/biomedicines12061331; Published Jun 2024) (romano2024recentinsightsinto pages 17-18).
- Fibroblast programs (Jan 2024): scRNA-seq delineated dual ECM sources from myofibroblasts and EndoMT cells and implicated Hippo/YAP–TAZ as central to mesenchymal differentiation; suggests pathway modulation as an antifibrotic strategy (URL: https://doi.org/10.1038/s41467-023-44645-6; Published Jan 2024) (lepri2024systemicsclerosisone pages 1-2).
- Autoantibody biology (Jul 2023): Active, spontaneous ATA IgG/IgA secretion correlates with ILD presence and severity, supporting differential pathogenic roles and implications for B-cell–targeted therapy (URL: https://doi.org/10.1136/rmdopen-2023-003148; Published Jul 2023) (lepri2024systemicsclerosisone pages 1-2).
- Biomarker/clinical overview (Sep 2023; Apr 2024): Consolidated linkages among cytokines/chemokines (IL-6, CCL2) and organ involvement; “one year in review” situates 2023 literature across endotypes and pathways (URLs: https://doi.org/10.3390/cimb45100490; https://doi.org/10.55563/clinexprheumatol/is29he) (maggio2023biomarkersinsystemic pages 2-4, lepri2024systemicsclerosisone pages 1-2).

## Current applications and real-world implementations
- Patient stratification by autoantibody/endotype and IFN/B-cell signatures to anticipate organ risk (ATA→ILD; ACA→PAH; RNAP III→renal crisis) (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 2-4).
- Monitoring IFN activity (e.g., SIGLEC1) and angiogenesis-related markers (VEGF, Angpt2) to track vasculopathy/fibrosis risk (Published Sep 2023; https://doi.org/10.3390/cimb45100490) (maggio2023biomarkersinsystemic pages 6-8).
- Emerging targeted approaches (translational): Hippo/YAP–TAZ modulation and pathway-specific TGF-β targeting are under exploration based on 2024 molecular insights; TGF-β isoform-selective strategies seek to reduce systemic toxicity (context across 2023–2024) (Published Jan 2024; https://doi.org/10.1038/s41467-023-44645-6; trial-phase summary 2024) (lepri2024systemicsclerosisone pages 1-2).

## Expert opinions and analysis
- The 2024 “one year in review” underscores that SSc heterogeneity is best captured by integrating single-cell molecular states, autoantibody profiles, and genetics (FLT3/TGF-β-related variants), converging on specific signaling axes (Hippo/Wnt/TGF-β/PI3K–AKT) that differ by stage and autoantibody subgroup (Published Apr 2024; https://doi.org/10.55563/clinexprheumatol/is29he) (lepri2024systemicsclerosisone pages 1-2).
- Vascular experts emphasize intervening in EndoMT and EC senescence to prevent irreversible capillary loss and subsequent fibrosis—positioning vasculopathy as a druggable, earliest disease node (Published Jun 2024; https://doi.org/10.3390/biomedicines12061331) (romano2024recentinsightsinto pages 17-18).

## Relevant statistics and data from recent studies
- GWAS (Japan; 2024): 1,428 SSc cases, 112,599 controls; lead SNP in FCGR/FCRL region; meta-analysis identified 30 additional loci and supported B-cell/IRF8 biology; polygenic models improved by prioritizing IRF8 binding-site SNPs (URL: https://doi.org/10.1038/s41467-023-44541-z; Published Jan 2024) (lepri2024systemicsclerosisone pages 1-2).
- Autoantibodies (reviewed 2023): approximate frequencies—anti–topoisomerase I (15–25%), anticentromere (10–20%), anti–RNA polymerase III (10–25%); phenotypic correlations: ATA→ILD, ACA→PAH/digital vasculopathy, RNAP III→rapid skin progression, renal crisis (URL: https://doi.org/10.3390/cimb45100490; Published Sep 2023) (maggio2023biomarkersinsystemic pages 2-4).
- Vascular biomarker axes (2023): increased Ang-2 with decreased Ang-1; early VEGF elevation yet defective angiogenesis; SIGLEC1 upregulated with IFN activation (URL: https://doi.org/10.3390/cimb45100490; Published Sep 2023) (maggio2023biomarkersinsystemic pages 6-8).
- B-cell activity and ILD (2023): spontaneous ATA IgG/IgA secretion higher in ILD and correlates with pulmonary fibrosis severity (URL: https://doi.org/10.1136/rmdopen-2023-003148; Published Jul 2023) (lepri2024systemicsclerosisone pages 1-2).

## Evidence items (with PMIDs/URLs, publication dates; direct quotes where available)
- “Defective angiogenesis … represents a hallmark of early-stage disease, usually preceding the onset of tissue fibrosis” (Biomedicines; Published Jun 2024; URL: https://doi.org/10.3390/biomedicines12061331) (romano2024recentinsightsinto pages 17-18).
- “Systemic sclerosis … characterised by three main pathogenetic events represented by endothelial damage, inflammation with activation of the immune system … and finally fibrosis” (Clin Exp Rheumatol; Published Apr 2024; URL: https://doi.org/10.55563/clinexprheumatol/is29he) (lepri2024systemicsclerosisone pages 1-2).
- “We report the largest Asian GWAS … comprising of 1428 cases and 112,599 controls … lead SNP is in the FCGR/FCRL region … meta-analysis … detects 30 additional significant loci … underscoring the roles of B cells and IRF8” (Nat Commun; Published Jan 2024; URL: https://doi.org/10.1038/s41467-023-44541-z) (lepri2024systemicsclerosisone pages 1-2).
- “The ATA response … showed additional secretion of autoreactive IgA … The degree of spontaneous ATA-secretion was higher in patients with ILD … and correlated with the degree of pulmonary fibrosis” (RMD Open; Published Jul 2023; URL: https://doi.org/10.1136/rmdopen-2023-003148) (lepri2024systemicsclerosisone pages 1-2).
- “The soluble levels of the three active TGF-β isoforms were lower in SSc patients than controls … In skin biopsies, TGF-β1, TGF-βR1, and TGF-βR2 expression levels were higher in SSc patients” (Clin Exp Med; Published May 2023; URL: https://doi.org/10.1007/s10238-022-00841-0) (jimenez2025areviewof pages 1-2).

## Ontology-annotated knowledge base entry
- Genes/proteins (HGNC) and pathways (GO): see embedded table for TGFB1, TGFBR1/2, SMAD2/3, CCN2, PDGF/PDGFR, EDN1, VEGFA, ANGPT1/2, CXCL4, IL6, CCL2, IRF8, FCGR locus, YAP1/WWTR1, WNT5A, SIGLEC1 with GO biological processes and GO-CC (romano2024recentinsightsinto pages 17-18, maggio2023biomarkersinsystemic pages 2-4, maggio2023biomarkersinsystemic pages 6-8, lepri2024systemicsclerosisone pages 1-2, jimenez2025areviewof pages 1-2).
- Cell types (CL): endothelial cell (CL:0000115), fibroblast (CL:0000064), monocyte/macrophage (CL:0000235), B cell (CL:0000236), T cell (CL:0000084), endothelial progenitor cell (romano2024recentinsightsinto pages 17-18, maggio2023biomarkersinsystemic pages 6-8).
- Anatomical locations (UBERON): skin (UBERON:0002097), lung (UBERON:0002048), heart (UBERON:0000948), kidney (UBERON:0002113), microvasculature (lepri2024systemicsclerosisone pages 1-2, romano2024recentinsightsinto pages 17-18).
- Chemical entities (CHEBI): endothelin-1, VEGF-A, TGF-β1, PDGF, CXCL4 (maggio2023biomarkersinsystemic pages 6-8).
- Phenotypes (HP; narrative associations): vascular (Raynaud’s, telangiectasias, digital ulcers), pulmonary (ILD, PAH), cardiac (arrhythmia, myocardial fibrosis), renal crisis; associations by autoantibody endotype (maggio2023biomarkersinsystemic pages 2-4, lepri2024systemicsclerosisone pages 1-2).

## Notes on evidence strength and gaps
- High-confidence nodes: vascular pathology (EndoMT/angiogenesis defects), IFN-I/B-cell autoimmunity, and TGF-β/SMAD-centered fibroblast activation are consistently supported by 2023–2024 sources (romano2024recentinsightsinto pages 17-18, lepri2024systemicsclerosisone pages 1-2, jimenez2025areviewof pages 1-2).
- Genetics increasingly implicates B-cell/IRF8/FCGR biology; functional validation in primary tissues remains ongoing (lepri2024systemicsclerosisone pages 1-2).
- Immunometabolism and metabolic fingerprints are promising but heterogeneous; targeted metabolomics and intervention studies are needed (maggio2023biomarkersinsystemic pages 6-8).


References

1. (romano2024recentinsightsinto pages 17-18): Eloisa Romano, Irene Rosa, Bianca Saveria Fioretto, and Mirko Manetti. Recent insights into cellular and molecular mechanisms of defective angiogenesis in systemic sclerosis. Biomedicines, 12:1331, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061331, doi:10.3390/biomedicines12061331. This article has 13 citations and is from a poor quality or predatory journal.

2. (lepri2024systemicsclerosisone pages 1-2): Gemma Lepri, Marco Di Battista, Veronica Codullo, Francesco Bonomi, Antonello Sulis, Serena Guiducci, and Alessandra Della Rossa. Systemic sclerosis: one year in review 2024. Clinical and experimental rheumatology, Apr 2024. URL: https://doi.org/10.55563/clinexprheumatol/is29he, doi:10.55563/clinexprheumatol/is29he. This article has 25 citations and is from a peer-reviewed journal.

3. (maggio2023biomarkersinsystemic pages 6-8): Giuseppe Di Maggio, Paola Confalonieri, Francesco Salton, Liliana Trotta, Luca Ruggero, Metka Kodric, Pietro Geri, Michael Hughes, Mattia Bellan, Michele Gilio, Selene Lerda, Elisa Baratella, Marco Confalonieri, Lucrezia Mondini, and Barbara Ruaro. Biomarkers in systemic sclerosis: an overview. Current Issues in Molecular Biology, 45:7775-7802, Sep 2023. URL: https://doi.org/10.3390/cimb45100490, doi:10.3390/cimb45100490. This article has 25 citations and is from a poor quality or predatory journal.

4. (maggio2023biomarkersinsystemic pages 2-4): Giuseppe Di Maggio, Paola Confalonieri, Francesco Salton, Liliana Trotta, Luca Ruggero, Metka Kodric, Pietro Geri, Michael Hughes, Mattia Bellan, Michele Gilio, Selene Lerda, Elisa Baratella, Marco Confalonieri, Lucrezia Mondini, and Barbara Ruaro. Biomarkers in systemic sclerosis: an overview. Current Issues in Molecular Biology, 45:7775-7802, Sep 2023. URL: https://doi.org/10.3390/cimb45100490, doi:10.3390/cimb45100490. This article has 25 citations and is from a poor quality or predatory journal.

5. (jimenez2025areviewof pages 1-2): Sergio A. Jimenez, Fabian A. Mendoza, and Sonsoles Piera-Velazquez. A review of recent studies on the pathogenesis of systemic sclerosis: focus on fibrosis pathways. Frontiers in Immunology, Apr 2025. URL: https://doi.org/10.3389/fimmu.2025.1551911, doi:10.3389/fimmu.2025.1551911. This article has 17 citations and is from a peer-reviewed journal.

6. (jimenez2025areviewof pages 9-10): Sergio A. Jimenez, Fabian A. Mendoza, and Sonsoles Piera-Velazquez. A review of recent studies on the pathogenesis of systemic sclerosis: focus on fibrosis pathways. Frontiers in Immunology, Apr 2025. URL: https://doi.org/10.3389/fimmu.2025.1551911, doi:10.3389/fimmu.2025.1551911. This article has 17 citations and is from a peer-reviewed journal.

7. (bazso2025theroleof pages 1-2): Anna Bazsó, Péter Szodoray, Yehuda Shoenfeld, and Emese Virág Kiss Med Dsci. The role of biomarkers in the the pathogenesis, clinical manifestations, and therapeutic outcome of systemic sclerosis. Journal of Mosaic of Autoimmunity, pages 5, Apr 2025. URL: https://doi.org/10.53941/jmai.2025.100005, doi:10.53941/jmai.2025.100005. This article has 0 citations.