---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:15.071546'
end_time: '2025-12-17T23:36:56.684834'
duration_seconds: 521.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hashimoto's Thyroiditis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hashimoto's Thyroiditis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hashimoto's Thyroiditis**.
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
- **Disease Name:** Hashimoto's Thyroiditis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hashimoto's Thyroiditis**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Hashimoto's Thyroiditis (HT)
- MONDO ID: MONDO:0007147
- Category: Complex

## Pathophysiology description (current understanding and recent developments)
Hashimoto’s thyroiditis is an organ-specific autoimmune disease of the thyroid characterized by adaptive and innate immune activation within the thyroid gland, progressive destruction of thyroid follicular cells (thyrocytes), and frequent development of hypothyroidism. Recent spatial transcriptomic mapping of autoimmune thyroid disease tissue demonstrates that thyrocytes are active participants in local immunity: “damaged antigen-presenting TFCs with upregulated CD74 and MIF expression” are identified in situ, with interferon and inflammatory cytokines inducing antigen-presentation machinery in thyrocytes and enabling direct interactions with infiltrating immune cells (doi:10.1038/s41467-024-50192-5; July 2024, Nature Communications) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12). Bulk transcriptomics of HT thyroid tissue reveals strong enrichment of adaptive immune signatures (T and B cell activation), antigen processing/presentation, complement, cytotoxicity, apoptosis and necroptosis, alongside widespread disruption of epithelial differentiation, thyroid hormone biosynthetic programs, cellular metabolism, mitochondrial function, and stromal/ECM remodeling consistent with fibrosis (doi:10.48188/so.6.9; Oct 2025, ST-OPEN) (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, cikotic2025transcriptomeanalysisof pages 17-18). 

Expert commentary and clinical mechanistic analogs from immune checkpoint inhibitor (ICI)-induced thyroiditis underscore the centrality of interferon-rich, Th1/Th17-skewed responses, B cell/plasma cell activation, and genetic susceptibility (HLA class II, CTLA4, PTPN22) in precipitating thyroidal autoimmunity and the typical clinical trajectory of destructive thyrotoxicosis followed by (often irreversible) hypothyroidism (doi:10.3389/fendo.2025.1584675; June 2025, Frontiers in Endocrinology) (mao2025immunecheckpointinhibitorinduced pages 2-4, mao2025immunecheckpointinhibitorinduced pages 7-8).

Selected direct quotes from recent spatial/clinical mechanistic literature:
- “Proinflammatory cytokines such as IFN-γ and TNF-α can upregulate the expression of CD74 in TFCs,” linking interferon/inflammatory signals to thyrocyte antigen presentation (doi:10.1038/s41467-024-50192-5; July 2024) (martinezhernandez2024unravelingthemolecular pages 9-12).
- ICI-associated thyroiditis illustrates a canonical pattern of “antigenic cross-reactivity, T-cell subsets and B cell/plasma cell activation, cytokine/chemokine activity and genetic susceptibility” culminating in thyroid follicular destruction and hypothyroidism (doi:10.3389/fendo.2025.1584675; June 2025) (mao2025immunecheckpointinhibitorinduced pages 2-4).

## 1. Core Pathophysiology
- Primary mechanisms: breakdown of tolerance to thyroglobulin (TG) and thyroid peroxidase (TPO) with intrathyroidal antigen presentation; interferon-driven upregulation of MHC-II/CD74 in thyrocytes; formation of ectopic germinal centers (GCs) that sustain local B cell maturation and antibody production; cytotoxic and complement-mediated thyrocyte death; stromal (fibroblast) and vascular remodeling supporting persistent lymphocyte trafficking (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, cikotic2025transcriptomeanalysisof pages 17-18).
- Dysregulated molecular pathways: type I and II interferon signaling (JAK–STAT), NF-κB/inflammasome activation, PI3K–Akt survival/metabolic signaling imbalance, complement activation, apoptosis (FAS/FASL), and chemokine axes (e.g., CXCL12–CXCR4) that organize lymphoid niches (martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, cikotic2025transcriptomeanalysisof pages 17-18).
- Affected cellular processes: antigen processing/presentation; GC formation and B cell affinity maturation; cytotoxic granule/perforin programs; complement-mediated cytotoxicity; epithelial de-differentiation and loss of thyroid hormone biosynthesis programs; mitochondrial/oxidative metabolism disruption; extracellular matrix (ECM) organization and fibrosis (martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15).

## 2. Key Molecular Players
- Genes/Proteins (HGNC): TG (HGNC:11764) and TPO (HGNC:12014) as principal autoantigens; HLA class II (e.g., HLA-DRA, HGNC:4947) mediating antigen presentation; immune regulatory and risk genes including CTLA4 (HGNC:2505), PTPN22 (HGNC:9656), BACH2 (HGNC:935), GLIS3 (HGNC:18128), IFIH1 (HGNC:18873), IRF4 (HGNC:6118), SH2B3 (HGNC:30406), and FAS (HGNC:11920) (OpenTargets disease–target evidence; 2025) (OpenTargets Search: Hashimoto's thyroiditis). Spatial data highlight CD74 (HGNC:1709) and MIF (HGNC:7097) upregulation in thyrocytes under IFN/TNF exposure (doi:10.1038/s41467-024-50192-5; 2024) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12).
- Chemical entities (CHEBI): iodide (CHEBI:24859) as a potential epithelial stressor (ROS/NLRP3 inflammasome), IFN-γ (CHEBI:51275) and TNF-α (CHEBI:52299) as key cytokines driving antigen-presentation and inflammatory circuits (cikotic2025transcriptomeanalysisof pages 13-15, martinezhernandez2024unravelingthemolecular pages 9-12).
- Cell types (CL): thyroid follicular cells/thyrocytes (CL:0002328), B cells (CL:0000236), plasma cells (CL:0000786), T helper cells (CL:0000911) including T follicular helper (Tfh; CL:0002038), dendritic cells (CL:0000451), macrophages (CL:0000235), fibroblasts/myofibroblasts (CL:0000057), endothelial cells including high endothelial venule-like states (CL:0000115), and follicular dendritic cells (FDC; CL:0000842) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, cikotic2025transcriptomeanalysisof pages 17-18).
- Anatomical locations (UBERON): thyroid gland (UBERON:0002046), germinal center (UBERON:0002358), and high endothelial venule (UBERON:0002185) where lymphocyte trafficking and TLS/GC niches are spatially organized (martinezhernandez2024unravelingthemolecular pages 9-12, martinezhernandez2024unravelingthemolecular pages 12-13).

## 3. Biological Processes (GO) disrupted
- Type I interferon signaling (GO:0060337) and response to interferon-gamma (GO:0034341) (martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 10-13).
- Antigen processing and presentation of peptide antigen via MHC class II (GO:0002495), including thyrocyte CD74/HLA upregulation (martinezhernandez2024unravelingthemolecular pages 9-12, martinezhernandez2024unravelingthemolecular pages 12-13).
- NF-κB signaling (GO:0043122) and inflammasome activation (NLRP3) contributing to epithelial inflammatory cell death (cikotic2025transcriptomeanalysisof pages 13-15).
- JAK–STAT signaling (GO:0007259) downstream of interferons and cytokines (cikotic2025transcriptomeanalysisof pages 10-13, martinezhernandez2024unravelingthemolecular pages 9-12).
- PI3K–Akt signaling (GO:0014065) perturbations tied to survival/metabolic stress (cikotic2025transcriptomeanalysisof pages 10-13).
- Complement activation (GO:0006956), apoptosis (including FAS-mediated, GO:0008625), and cytotoxic programs (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15).
- Chemokine-mediated signaling (GO:0070098) such as CXCL12–CXCR4 that organizes TLS/GC niches (martinezhernandez2024unravelingthemolecular pages 9-12).
- Lymphoid organ development/TLS formation (GO:0048535) and ECM organization/fibrosis (GO:0030198) (cikotic2025transcriptomeanalysisof pages 17-18, cikotic2025transcriptomeanalysisof pages 13-15, martinezhernandez2024unravelingthemolecular pages 12-13).

## 4. Cellular Components
- Thyrocyte plasma membrane and endolysosomal/antigen processing compartments (MHC-II/CD74 localization); extracellular matrix and basement membrane; high endothelial venules facilitating lymphocyte entry; germinal center microdomains populated by FDCs and GC B cells (martinezhernandez2024unravelingthemolecular pages 9-12, martinezhernandez2024unravelingthemolecular pages 12-13, cikotic2025transcriptomeanalysisof pages 13-15).

## 5. Disease Progression (sequence of events)
- Triggers: epithelial stressors (e.g., iodide/oxidative stress), infections, and genetic predisposition (HLA class II, CTLA4, PTPN22, IFIH1, etc.) lower tolerance thresholds (cikotic2025transcriptomeanalysisof pages 13-15, OpenTargets Search: Hashimoto's thyroiditis).
- Initiation: interferon- and TNF-rich milieu induces thyrocyte MHC-II/CD74 and chemokine expression; professional APCs (DCs, macrophages) present thyroid autoantigens (TG/TPO) to CD4+ T cells (martinezhernandez2024unravelingthemolecular pages 9-12, martinezhernandez2024unravelingthemolecular pages 12-13).
- Propagation: Th1/Th17/Tfh responses amplify inflammation and provide B cell help; ectopic GCs form with FDC networks, enabling intrathyroidal affinity maturation and plasma cell differentiation; autoantibodies (TPOAb/TgAb) accumulate (martinezhernandez2024unravelingthemolecular pages 9-12, martinezhernandez2024unravelingthemolecular pages 12-13, mao2025immunecheckpointinhibitorinduced pages 2-4, mao2025immunecheckpointinhibitorinduced pages 7-8).
- Effector injury: cytotoxic lymphocytes, complement, and apoptosis (FAS) mediate thyrocyte destruction; bulk transcriptomes show apoptosis/necroptosis signatures and loss of thyrocyte differentiation/hormone biosynthetic programs (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15).
- Remodeling and chronicity: fibroblast/myofibroblast activation (TGF-β–linked), ECM deposition, vascular remodeling with PLVAP+ vessels/HEV-like features sustaining lymphocyte recruitment; fibrosis and permanent hypothyroidism ensue (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 13-15).

## 6. Phenotypic Manifestations and clinical correlations
- Key phenotypes: painless goiter, thyroid tenderness in phases of active inflammation, elevated anti-TPO and/or anti-Tg antibodies, transient thyrotoxicosis followed by persistent hypothyroidism, and thyroidal fibrosis on histology (mao2025immunecheckpointinhibitorinduced pages 2-4, cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15).
- Mechanistic link: antibody and T cell–mediated injury, interferon/TNF-driven antigen presentation in thyrocytes, and GC-supported local autoantibody production align with clinical serology and functional decline (martinezhernandez2024unravelingthemolecular pages 9-12, martinezhernandez2024unravelingthemolecular pages 12-13, mao2025immunecheckpointinhibitorinduced pages 2-4).
- Oncogenesis comorbidity: spatial data identify de-differentiated, oxidative stress–enriched thyrocyte subsets in proximity to immune infiltrates and implicate CD74/MIF signaling in divergent outcomes, offering a mechanistic bridge between chronic autoimmunity and papillary thyroid carcinoma (PTC) microenvironments observed in HT–PTC co-occurrence (doi:10.1038/s41467-024-50192-5; 2024) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12). 


Hashimoto's Thyroiditis: Key Entities and Ontology Mappings

| Category | Entity/Term | Standard ID | Role in HT Pathophysiology | Evidence | Notes |
|---|---|---:|---|---|---|
| Genes / Proteins | TG; TPO; HLA-DRA; CTLA4; PTPN22; BACH2; GLIS3; IFIH1; IRF4; SH2B3; FAS; CD74; MIF | HGNC:11764; HGNC:12014; HGNC:4947; HGNC:2505; HGNC:9656; HGNC:935; HGNC:18128; HGNC:18873; HGNC:6118; HGNC:30406; HGNC:11920; HGNC:1709; HGNC:7097 | TG/TPO = primary autoantigens; HLA/antigen-presentation and immune-regulatory genes (CTLA4, PTPN22, BACH2, SH2B3) modulate tolerance; IFIH1/IRF4 linked to IFN/innate sensing; FAS mediates apoptosis; CD74/MIF in thyrocyte antigen-presentation | Open Targets association for TG/CTLA4/PTPN22 (OpenTargets Search: Hashimoto's thyroiditis); spatial & transcriptomic mechanistic localization (doi:10.1038/s41467-024-50192-5) (martinezhernandez2024unravelingthemolecular pages 12-13); transcriptome case-control (doi:10.48188/so.6.9) (cikotic2025transcriptomeanalysisof pages 10-13) | Genetic + transcriptomic + spatial evidence supports autoantigen-driven, genetically modulated autoimmune response. |
| Cell type | Thyroid follicular cell (thyrocyte) | CL:0002328 | Can express MHC-II/CD74 under IFN/TNF stimulation → local antigen presentation; source of autoantigen release and epithelial damage | Spatial transcriptomics: CD74/MIF upregulation and antigen-presentation in TFCs (doi:10.1038/s41467-024-50192-5) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12); bulk transcriptome immune signatures (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15) | Thyrocytes act as active participants (not passive targets) in HT immunopathology. |
| Cell type | B cell | CL:0000236 | GC B cell differentiation, local antibody (TPOAb/TgAb) production in ectopic germinal centers | Spatial localization of GC B cells and FDC markers (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12); ICI/clinical antibody correlations (mao2025immunecheckpointinhibitorinduced pages 2-4) | Local GC formation supports sustained autoantibody generation. |
| Cell type | Plasma cell | CL:0000786 | Terminal antibody secretion (TPOAb/TgAb) within thyroid tissue and circulation | Plasmablast/plasma cell dissemination in TFC areas (martinezhernandez2024unravelingthemolecular pages 12-13) and transcriptomic signatures (cikotic2025transcriptomeanalysisof pages 10-13) | Major effector source of autoantibodies. |
| Cell type | T helper cell (CD4+) | CL:0000911 | Th1/Th17 skewing provides cytokines (IFN-γ, IL‑17) that drive inflammation, B cell help and cytotoxic programs | Th1/Th17 signatures and cytokine milieu described in transcriptome and ICI-related studies (cikotic2025transcriptomeanalysisof pages 13-15, mao2025immunecheckpointinhibitorinduced pages 7-8, mao2025immunecheckpointinhibitorinduced pages 2-4) | Helper subsets shape antibody class-switching and macrophage activation. |
| Cell type | T follicular helper (Tfh) | CL:0002038 | Supports GC formation and B cell affinity maturation within ectopic GCs | Enrichment of TCD4/Tfh in GC regions (spatial data) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12) | Key for intrathyroidal humoral autoimmunity. |
| Cell type | Dendritic cell | CL:0000451 | Professional antigen presentation, initiation of T cell responses and TLS support | Myeloid APCs distributed around infiltrates; DC involvement in TLS/TLO formation (martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 13-15) | DC heterogeneity may influence tolerance vs activation. |
| Cell type | Macrophage | CL:0000235 | Phagocytosis, cytokine production, tissue remodeling and presentation; CD163+ histiocytes noted in destructive thyroiditis | Macrophage presence around infiltrates and in ICI-induced thyroiditis pathology (martinezhernandez2024unravelingthemolecular pages 9-12, mao2025immunecheckpointinhibitorinduced pages 2-4, cikotic2025transcriptomeanalysisof pages 13-15) | Contributes to follicular cell clearance and fibrosis. |
| Cell type | Fibroblast / myofibroblast | CL:0000057 | Stromal remodeling, TGF‑β–driven myofibroblast transition and ECM deposition → fibrosis | Perifollicular myofibroblasts and inflammatory fibroblasts identified by spatial data; ECM gene induction (martinezhernandez2024unravelingthemolecular pages 12-13, cikotic2025transcriptomeanalysisof pages 13-15) | Stromal states support TLS niches and fibrosis. |
| Cell type | Endothelial cell (including HEV) | CL:0000115 | Vascular remodeling, PLVAP+ vessels and HEV formation facilitate lymphocyte trafficking into thyroid | PLVAP+ fenestrated vessels and ACKR1+/HEV localization in inflamed regions (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12) | HEV-like vessels enable sustained lymphocyte recruitment. |
| Cell type | Follicular dendritic cell (FDC) | CL:0000842 | Organizing GC microarchitecture and antigen retention within ectopic GCs | FDC markers (FDCSP, TCL1A) concentrated in GC regions (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12) | Supports local affinity maturation and persistent antibody responses. |
| Pathway / Process | Type I interferon signaling; Response to IFN‑gamma; JAK‑STAT cascade; NF‑kappaB signaling | GO:0060337; GO:0034341; GO:0007259; GO:0043122 | IFN signatures upregulate MHC-II/CD74 and chemokines, promoting APC activity and immune recruitment; NF‑κB/Inflammasome (NLRP3) link to epithelial pyroptosis | Spatial and transcriptomic upregulation of IFN pathways and CD74 in TFCs (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12); inflammasome/NF‑κB evidence (cikotic2025transcriptomeanalysisof pages 13-15) | Central inflammatory drivers connecting innate sensing to adaptive autoimmunity. |
| Pathway / Process | PI3K‑Akt signaling; Complement activation; Apoptosis via FAS | GO:0014065; GO:0006956; GO:0008625 | PI3K‑Akt impacts cell survival/metabolism; complement and FAS-mediated apoptosis contribute to follicular cell loss | Bulk transcriptome evidence of apoptosis/complement pathways and metabolic dysfunction (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 17-18, cikotic2025transcriptomeanalysisof pages 13-15) | Links metabolic/stress state to cell death and autoantigen release. |
| Pathway / Process | Chemokine-mediated signaling; Lymphoid organ development; ECM organization | GO:0070098; GO:0048535; GO:0030198 | CXCL/CXCR axes recruit lymphocytes; lymphoid organogenesis supports ectopic GC/TLS formation; ECM remodeling → fibrosis and altered microarchitecture | CXCL12‑CXCR4 enrichment, HEV/ACKR1 localization and ECM gene induction in spatial & bulk data (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 13-15) | Chemokines + stromal changes enable persistent local immune niches. |
| Anatomy | Thyroid gland; High endothelial venule (HEV); Germinal center; Extracellular matrix | UBERON:0002046; UBERON:0002185; UBERON:0002358; GO:0031012 | Tissue compartments where antigen presentation, TLS/GC formation, and fibrosis occur | Spatial mapping of GC regions, HEVs, TFC damage, ECM deposition (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 13-15) | Spatial context critical for understanding local autoimmunity and progression. |
| Chemical / Mediator | Iodide; TNF‑alpha; IFN‑gamma | CHEBI:24859; CHEBI:52299; CHEBI:51275 | Iodide can trigger oxidative stress/pyroptosis in thyrocytes; TNF/IFN drive CD74/MHC‑II expression and inflammation | Iodide-triggered ROS/NLRP3 inflammasome and inflammatory cytokine roles (cikotic2025transcriptomeanalysisof pages 13-15); cytokine-driven CD74 upregulation (martinezhernandez2024unravelingthemolecular pages 12-13, mao2025immunecheckpointinhibitorinduced pages 2-4) | Environmental/biochemical modulators that amplify immune activation. |


*Table: A concise mapping table of genes, cell types, pathways, anatomical terms and chemicals relevant to Hashimoto's thyroiditis with standardized IDs and evidence links from spatial and transcriptomic studies (context citations).*


## Gene/protein annotations with ontology terms
- TG (HGNC:11764) – autoantigen; processes: antigenicity, thyroid hormone precursor; components: colloid/lumen; evidence: OpenTargets genetics (URL: https://platform.opentargets.org, accessed 2025) (OpenTargets Search: Hashimoto's thyroiditis).
- TPO (HGNC:12014) – autoantigen; processes: thyroid hormone biosynthesis; components: apical membrane; evidence: bulk downregulation in HT with loss of biosynthetic program (doi:10.48188/so.6.9; 2025) (cikotic2025transcriptomeanalysisof pages 10-13).
- HLA-DRA (HGNC:4947) – MHC-II; processes: antigen presentation; components: MHC-II complex; evidence: thyrocyte antigen-presentation machinery in AITD (doi:10.1038/s41467-024-50192-5; 2024) (martinezhernandez2024unravelingthemolecular pages 9-12).
- CTLA4 (HGNC:2505) – negative regulator of T cell activation; processes: T cell anergy; evidence: association with HT (OpenTargets) (OpenTargets Search: Hashimoto's thyroiditis).
- PTPN22 (HGNC:9656), BACH2 (HGNC:935), GLIS3 (HGNC:18128), IFIH1 (HGNC:18873), IRF4 (HGNC:6118), SH2B3 (HGNC:30406), FAS (HGNC:11920) – immune regulation, innate sensing/IFN pathways, apoptosis; evidence: genetics and mechanistic plausibility in HT (OpenTargets 2025; bulk transcriptomics 2025) (OpenTargets Search: Hashimoto's thyroiditis, cikotic2025transcriptomeanalysisof pages 10-13).
- CD74 (HGNC:1709), MIF (HGNC:7097) – thyrocyte antigen-presentation cofactor and ligand; processes: MHC-II trafficking and MIF-CD74 signaling; evidence: spatial upregulation in thyrocytes and cell–cell interactions (doi:10.1038/s41467-024-50192-5; 2024) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12).

## Phenotype associations (HP terms)
- Hypothyroidism (HP:0000821), Goiter (HP:0000853), Thyroiditis (HP:0000834), Positive anti-thyroid peroxidase antibody (HP:0030057), Positive anti-thyroglobulin antibody (HP:0030058), Fatigue (HP:0012378), Cold intolerance (HP:0002045). Mechanistic correspondence: antibody-mediated and cytotoxic follicular injury with interferon/NF-κB signatures and fibrosis (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, mao2025immunecheckpointinhibitorinduced pages 2-4, martinezhernandez2024unravelingthemolecular pages 9-12).

## Cell type involvement (CL terms)
- Thyrocyte (CL:0002328), B cell (CL:0000236), Plasma cell (CL:0000786), T helper and Tfh (CL:0000911; CL:0002038), Dendritic cell (CL:0000451), Macrophage (CL:0000235), Fibroblast (CL:0000057), Endothelial cell (CL:0000115), FDC (CL:0000842), with spatial localization of ectopic GCs and HEV-like vessels (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12).

## Anatomical locations (UBERON terms)
- Thyroid gland (UBERON:0002046); Germinal center (UBERON:0002358) within intrathyroidal TLS; High endothelial venule (UBERON:0002185); Extracellular matrix (GO:0031012) deposition sites in fibrotic thyroid (martinezhernandez2024unravelingthemolecular pages 9-12, martinezhernandez2024unravelingthemolecular pages 12-13, cikotic2025transcriptomeanalysisof pages 13-15).

## Chemical entities (CHEBI terms)
- Iodide (CHEBI:24859), IFN-γ (CHEBI:51275), TNF-α (CHEBI:52299) as upstream mediators of epithelial stress and antigen presentation (cikotic2025transcriptomeanalysisof pages 13-15, martinezhernandez2024unravelingthemolecular pages 9-12).

## Current applications and real-world implementations
- Diagnosis and monitoring: serologic assays for TPOAb/TgAb reflect intrathyroidal GC activity; ultrasound for echogenicity/fibrosis; recognition that interferon-rich destructive thyroiditis often follows a phase of transient thyrotoxicosis (mao2025immunecheckpointinhibitorinduced pages 2-4, mao2025immunecheckpointinhibitorinduced pages 7-8).
- Management: levothyroxine replacement for hypothyroidism remains standard; insights from ICI-induced thyroiditis emphasize screening for thyroid autoantibodies to stratify irAE risk and close hormone monitoring during checkpoint blockade; mechanistic links to B cells support exploration of B-cell–modulating strategies in selected contexts (doi:10.3389/fendo.2025.1584675; 2025) (mao2025immunecheckpointinhibitorinduced pages 2-4, mao2025immunecheckpointinhibitorinduced pages 7-8).
- Research tools in practice: spatial transcriptomics and single-cell deconvolution identify thyrocyte CD74/HLA induction, ectopic GC architecture, and stromal/endothelial niches as candidate biomarkers and therapeutic targets (doi:10.1038/s41467-024-50192-5; 2024) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12).

## Expert opinions and analysis (authoritative sources)
- Spatial multi-omics perspective (Nature Communications, 2024): authors conclude that “thyroid epithelial cell subpopulations [are] potentially involved in pathogenesis,” with CD74/MIF and interferon–TNF axes integrating epithelial damage and local immune organization; this supports targeting stromal-immune–epithelial cross-talk in HT (doi:10.1038/s41467-024-50192-5; July 2024) (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12).
- Clinical immuno-oncology perspective (Frontiers in Endocrinology, 2025): ICI-thyroiditis mechanisms “establish mechanistic connections between ICI pharmacodynamics and thyroid tissue immunopathology,” reinforcing Th1/Th17 bias, B cell involvement, and genetic predisposition as drivers of destructive thyroiditis and hypothyroidism (doi:10.3389/fendo.2025.1584675; June 2025) (mao2025immunecheckpointinhibitorinduced pages 2-4, mao2025immunecheckpointinhibitorinduced pages 7-8).
- Systems transcriptomics perspective (ST-OPEN, 2025): local expansion of cellular/humoral/innate immunity with dominant cell death and reciprocal loss of epithelial/endothelial identity; broad metabolic and ECM remodeling capture chronicity and fibrosis in HT (doi:10.48188/so.6.9; Oct 2025) (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, cikotic2025transcriptomeanalysisof pages 17-18).

## Relevant statistics and data from recent studies
- Spatial transcriptomics in AITD delineated GC regions enriched for FDC markers FDCSP and TCL1A, with proliferative/GC B cells and TCD4/Tfh localized to these domains, and plasmablasts disseminating into thyrocyte territories, providing in situ evidence for local antibody maturation and effector dissemination (doi:10.1038/s41467-024-50192-5; 2024) (martinezhernandez2024unravelingthemolecular pages 9-12).
- Bulk transcriptome of HT demonstrated concerted upregulation of antigen presentation, interferon/TNF signaling, complement, cytotoxicity and apoptosis signatures, alongside downregulation of thyroid biosynthetic genes (TG, TPO) and endothelial markers, and upregulation of ECM/fibrotic programs (doi:10.48188/so.6.9; 2025) (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15).
- Genetics: OpenTargets aggregates multi-source evidence implicating TG (top disease–target score), CTLA4, PTPN22, BACH2, GLIS3, IFIH1, IRF4, SH2B3, and FAS in HT susceptibility and pathophysiology (Nucleic Acids Research, OpenTargets Platform; accessed 2025; URL: https://platform.opentargets.org) (OpenTargets Search: Hashimoto's thyroiditis).

## Evidence items (with PMIDs/DOIs/URLs)
- Martínez-Hernández R, et al. Unraveling the molecular architecture of autoimmune thyroid diseases at spatial resolution. Nature Communications. July 2024. doi:10.1038/s41467-024-50192-5. URL: https://www.nature.com/articles/s41467-024-50192-5 (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12).
- Čikotić M, et al. Transcriptome analysis of thyroid tissue in patients with Hashimoto’s disease using next-generation sequencing: case–control study. ST-OPEN. Oct 2025. doi:10.48188/so.6.9. URL: https://doi.org/10.48188/so.6.9 (cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, cikotic2025transcriptomeanalysisof pages 17-18).
- Mao X, et al. Immune checkpoint inhibitor-induced thyroiditis and its potential mechanisms. Frontiers in Endocrinology. June 2025. doi:10.3389/fendo.2025.1584675. URL: https://doi.org/10.3389/fendo.2025.1584675 (mao2025immunecheckpointinhibitorinduced pages 2-4, mao2025immunecheckpointinhibitorinduced pages 7-8).
- OpenTargets Platform: Hashimoto’s thyroiditis disease–target associations (TG, CTLA4, PTPN22, BACH2, GLIS3, IFIH1, IRF4, SH2B3, FAS). 2025. URL: https://platform.opentargets.org (OpenTargets Search: Hashimoto's thyroiditis).

## Final synthesis
HT pathophysiology emerges from a confluence of genetic risk alleles (TG, CTLA4, PTPN22 and others), interferon/TNF-driven induction of antigen presentation within thyrocytes (CD74/HLA), professional APC activation, and organization of ectopic GCs that sustain local B cell maturation and autoantibody production. Effector death pathways (cytotoxicity, complement, FAS) and persistent stromal/vascular remodeling drive chronic tissue destruction, fibrosis, and hypothyroidism. Spatial and bulk transcriptomic data from 2024–2025 localize these processes within the thyroid microenvironment, and clinical ICI-thyroiditis provides a mechanistic “stress test” that mirrors the natural disease trajectory. These insights nominate interferon and chemokine axes, thyrocyte antigen-presentation pathways (CD74/MIF), and stromal–vascular niches as plausible therapeutic targets and biomarkers in HT (martinezhernandez2024unravelingthemolecular pages 12-13, martinezhernandez2024unravelingthemolecular pages 9-12, cikotic2025transcriptomeanalysisof pages 10-13, cikotic2025transcriptomeanalysisof pages 13-15, cikotic2025transcriptomeanalysisof pages 17-18, mao2025immunecheckpointinhibitorinduced pages 2-4, mao2025immunecheckpointinhibitorinduced pages 7-8, OpenTargets Search: Hashimoto's thyroiditis).

References

1. (martinezhernandez2024unravelingthemolecular pages 12-13): Rebeca Martínez-Hernández, Nuria Sánchez de la Blanca, Pablo Sacristán-Gómez, Ana Serrano-Somavilla, José Luis Muñoz De Nova, Fátima Sánchez Cabo, Holger Heyn, Miguel Sampedro-Núñez, and Mónica Marazuela. Unraveling the molecular architecture of autoimmune thyroid diseases at spatial resolution. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50192-5, doi:10.1038/s41467-024-50192-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

2. (martinezhernandez2024unravelingthemolecular pages 9-12): Rebeca Martínez-Hernández, Nuria Sánchez de la Blanca, Pablo Sacristán-Gómez, Ana Serrano-Somavilla, José Luis Muñoz De Nova, Fátima Sánchez Cabo, Holger Heyn, Miguel Sampedro-Núñez, and Mónica Marazuela. Unraveling the molecular architecture of autoimmune thyroid diseases at spatial resolution. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50192-5, doi:10.1038/s41467-024-50192-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

3. (cikotic2025transcriptomeanalysisof pages 10-13): Marija Čikotić, Marieta Bujak, Silvija Piškorjanac, and Mario Štefanić. Transcriptome analysis of thyroid tissue in patients with hashimoto’s disease using next-generation sequencing: case–control study. ST-OPEN, 6:1-19, Oct 2025. URL: https://doi.org/10.48188/so.6.9, doi:10.48188/so.6.9. This article has 0 citations.

4. (cikotic2025transcriptomeanalysisof pages 13-15): Marija Čikotić, Marieta Bujak, Silvija Piškorjanac, and Mario Štefanić. Transcriptome analysis of thyroid tissue in patients with hashimoto’s disease using next-generation sequencing: case–control study. ST-OPEN, 6:1-19, Oct 2025. URL: https://doi.org/10.48188/so.6.9, doi:10.48188/so.6.9. This article has 0 citations.

5. (cikotic2025transcriptomeanalysisof pages 17-18): Marija Čikotić, Marieta Bujak, Silvija Piškorjanac, and Mario Štefanić. Transcriptome analysis of thyroid tissue in patients with hashimoto’s disease using next-generation sequencing: case–control study. ST-OPEN, 6:1-19, Oct 2025. URL: https://doi.org/10.48188/so.6.9, doi:10.48188/so.6.9. This article has 0 citations.

6. (mao2025immunecheckpointinhibitorinduced pages 2-4): Xueqian Mao, Chaoming Mao, Jiameng Liu, Xi Wang, and Yufei Mao. Immune checkpoint inhibitor-induced thyroiditis and its potential mechanisms. Frontiers in Endocrinology, Jun 2025. URL: https://doi.org/10.3389/fendo.2025.1584675, doi:10.3389/fendo.2025.1584675. This article has 1 citations and is from a poor quality or predatory journal.

7. (mao2025immunecheckpointinhibitorinduced pages 7-8): Xueqian Mao, Chaoming Mao, Jiameng Liu, Xi Wang, and Yufei Mao. Immune checkpoint inhibitor-induced thyroiditis and its potential mechanisms. Frontiers in Endocrinology, Jun 2025. URL: https://doi.org/10.3389/fendo.2025.1584675, doi:10.3389/fendo.2025.1584675. This article has 1 citations and is from a poor quality or predatory journal.

8. (OpenTargets Search: Hashimoto's thyroiditis): Open Targets Query (Hashimoto's thyroiditis, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.