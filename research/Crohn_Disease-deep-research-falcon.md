---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:03.708452'
end_time: '2025-12-15T09:11:09.165077'
duration_seconds: 605.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Crohn Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Crohn Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Crohn Disease**.
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
- **Disease Name:** Crohn Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Crohn Disease**.
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
- Disease Name: Crohn Disease
- MONDO ID: MONDO:0005059
- Category: Complex

Pathophysiology description (narrative)
Crohn disease (CD) arises from the convergence of genetic susceptibility, maladaptive immune responses to the intestinal microbiota, epithelial barrier dysfunction, and stromal remodeling culminating in fibrosis and fistulizing complications. Contemporary single-cell and spatial-omics studies resolve cell-type specific programs that drive disease heterogeneity: perianal fistulas feature myeloid–stromal crosstalk and interferon-driven modules; ileal disease highlights impaired autophagy and Paneth-cell dysfunction linked to LRRK2, ATG16L1, and NOD2 risk variants; and fibrostenosing disease is sustained by profibrotic fibroblast circuits and creeping fat–mesentery interactions that modulate transmural inflammation and matrix deposition (levantovsky2024multimodalsinglecellanalyses pages 1-4, sun2024macrophagelrrk2hyperactivity pages 1-3, liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4).

Core Pathophysiology
1) Immune pathway dysregulation
- IL-23/Th17 axis: Multiple recent reviews and single-cell syntheses detail a prominent Th17/IL-23 program with STAT3, IL23R, and hybrid Th1/Th17 states in IBD, including Crohn disease, supporting the now-standard clinical targeting of the pathway (e.g., anti-IL-23) (calvez2025novelinsightsinto pages 4-6). As summarized, “Adaptive responses retain prominent Th1 signatures (IFNG+ TNF+ cells) and a notable Th17 program with STAT3 and IL23R overexpression; single-cell data identify hybrid Th1/Th17 cells…” (calvez2025novelinsightsinto pages 4-6).
- TL1A–DR3 (TNFSF15–TNFRSF25) signaling: Human mucosal single-cell data from CD with perianal fistulizing disease (PFD) demonstrate TL1A-activated CD4+ T cells that remodel mucosa via downstream lymphotoxin-β (LTα1β2) and IL-22 programs in fibroblasts/epithelium, independent of TNF, nominating TL1A blockade as a precision target in fistulizing CD (gudino2025tl1aactivatedtcells pages 1-4). The authors note TL1A–DR3 engagement drives a “PFD-specific mucosal signature…with expanded fibroblast populations [and] induction of matrix-degrading enzymes” (gudino2025tl1aactivatedtcells pages 1-4).
- Interferon programs in fistula: Multi-omic profiling of Crohn’s perianal fistulas shows pronounced interferon (IFN) response and myeloid–stromal ligand–receptor signaling in fistula tracts with fibroblasts upregulating CHI3L1 and OSM; these data implicate IFN/JAK modules in fistulizing disease biology (levantovsky2024multimodalsinglecellanalyses pages 1-4). The study reports fistula tracts are “enriched for myeloid cells and show pronounced myeloid–stromal cross-talk… [with] stromal/fibroblast cells…highly upregulate CHI3L1 and exhibit both destructive and fibrotic transcriptional programs” (levantovsky2024multimodalsinglecellanalyses pages 1-4).

2) Epithelial barrier defects and microbial–host interactions
- Autophagy and Paneth-cell dysfunction: Hyperactive LRRK2 variants (e.g., G2019S, N2081D) impair autophagy, driving Paneth-cell abnormalities; lamina propria phagocytes expressing LRRK2 secrete proinflammatory cytokines that secondarily impair Paneth cells, while LRRK2 kinase inhibition restores autophagy and rescues function (sun2024macrophagelrrk2hyperactivity pages 1-3). The study concludes that “LRRK2-mediated pro-inflammatory cytokine release from phagocytes impaired Paneth cell function, which was rescued by LRRK2 kinase inhibition through activation of autophagy” (sun2024macrophagelrrk2hyperactivity pages 1-3). Autophagy-related variants in ATG16L1 and NOD2 similarly perturb antimicrobial autophagy and Paneth granule biology (petit2025advancesinunderstanding pages 12-13, petit2025advancesinunderstanding pages 8-9).
- Microbiome and pathobionts (AIEC; fungi/CARD9): Crohn disease is associated with reduced commensal diversity and enrichment of adherent-invasive E. coli (AIEC), which exploit impaired autophagy and innate signaling to persist, and with fungal dysbiosis interacting with CARD9-dependent antifungal immunity (calvez2025novelinsightsinto pages 4-6, petit2025advancesinunderstanding pages 12-13). Dysbiosis activates PRRs (e.g., TLR4, NOD2), amplifying TNF, IL-6 and IL-23, and sustaining Th1/Th17 responses (petit2025advancesinunderstanding pages 12-13).

3) Stromal–fibrotic circuits and creeping fat
- Fibrosis pathobiology: Fibrostenosing CD reflects immune–stromal interaction with fibroblast activation, Wnt–β-catenin and TGF-β signaling, and matrix turnover imbalance. Recent updates highlight increased β-catenin+ cells in fibrotic intestine, fibroblast subsets (e.g., CXCL14+ and MMP/WNT5A+), and lack of approved anti-fibrotic therapies (liu2024intestinalstricturesin pages 1-2). A translational review emphasizes convergent profibrotic mediators (TGF-β/SMAD, WNT, PAI-1) and immune inputs (TLR4, Th17) that drive myofibroblast expansion and ECM deposition (zhou2025insightsintothe pages 2-4).
- Creeping fat (mesenteric adipose tissue): Subserosal mesenteric adipose wraps the bowel (creeping fat), secreting immuno-metabolic mediators that associate with fibrostenosis and transmural inflammation; clinical imaging indices now quantify creeping fat burden and relate it to disease behavior (liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4). Reviews integrate creeping fat into a “diagnostic triad of fibrosis, smooth muscle hypertrophy, and creeping fat,” underlining its mechanistic role (zhou2025insightsintothe pages 2-4).

Key Molecular Players
- Genes/Proteins (HGNC): NOD2; ATG16L1; LRRK2; TNFSF15 (TL1A); TNFRSF25 (DR3); IL23A/IL23R; IFNG; CHI3L1; OSM; TGFB1; WNT ligands (e.g., WNT5A); MMPs/TIMPs (levantovsky2024multimodalsinglecellanalyses pages 1-4, calvez2025novelinsightsinto pages 4-6, sun2024macrophagelrrk2hyperactivity pages 1-3, liu2024intestinalstricturesin pages 1-2, petit2025advancesinunderstanding pages 12-13, zhou2025insightsintothe pages 2-4, gudino2025tl1aactivatedtcells pages 1-4).
- Chemical Entities (CHEBI): Not central to the primary genetic and cytokine mechanisms summarized here; pathway-targeting biologics are protein therapeutics (anti-IL-23, anti-TL1A) (calvez2025novelinsightsinto pages 4-6, gudino2025tl1aactivatedtcells pages 1-4).
- Cell Types (CL terms): Paneth cells (intestinal epithelial secretory lineage); Th17 and Th1 T cells; pathogenic Th17; macrophages (including IFN-polarized); neutrophils; stromal fibroblasts/myofibroblasts; mesenteric adipocytes/preadipocytes (levantovsky2024multimodalsinglecellanalyses pages 1-4, calvez2025novelinsightsinto pages 4-6, sun2024macrophagelrrk2hyperactivity pages 1-3, liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4, gudino2025tl1aactivatedtcells pages 1-4).
- Anatomical Locations (UBERON): Terminal ileum; intestinal lamina propria; rectal mucosa and perianal fistula tracts; intestinal muscularis propria; mesenteric adipose tissue (creeping fat) (levantovsky2024multimodalsinglecellanalyses pages 1-4, sun2024macrophagelrrk2hyperactivity pages 1-3, liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4, gudino2025tl1aactivatedtcells pages 1-4).

Biological Processes (GO-like annotation)
- Autophagy/xenophagy and antimicrobial peptide secretion (Paneth cells) (sun2024macrophagelrrk2hyperactivity pages 1-3, petit2025advancesinunderstanding pages 12-13).
- Cytokine signaling: IL-23/Th17 differentiation; TNF superfamily costimulation (TL1A–DR3); IFN-γ responses (levantovsky2024multimodalsinglecellanalyses pages 1-4, calvez2025novelinsightsinto pages 4-6, gudino2025tl1aactivatedtcells pages 1-4).
- Pattern-recognition receptor signaling and inflammasome-related innate pathways; PRR–microbiota interactions (petit2025advancesinunderstanding pages 12-13, petit2025advancesinunderstanding pages 8-9).
- ECM organization, TGF-β/SMAD and WNT/β-catenin pathways; epithelial–mesenchymal transition in fibrosis (liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4).
- Myeloid–stromal ligand–receptor interactions and interferon-stimulated gene programs in fistula (levantovsky2024multimodalsinglecellanalyses pages 1-4).

Cellular Components
- Sites of activity: Paneth-cell secretory granules and autophagolysosomes; epithelial tight junctions and mucosal surface; extracellular matrix and stromal niches within the intestinal wall; mesenteric adipose depots (sun2024macrophagelrrk2hyperactivity pages 1-3, liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4).

Disease Progression (sequence of events)
- Genetic predisposition (e.g., NOD2, ATG16L1, LRRK2) and environmental factors establish baseline defects in microbial handling and epithelial defense (autophagy, Paneth cell function) (sun2024macrophagelrrk2hyperactivity pages 1-3, petit2025advancesinunderstanding pages 12-13).
- Dysbiosis with enrichment of pathobionts (AIEC) and altered fungal communities engages PRRs, elevating TNF/IL-6/IL-23 and driving Th1/Th17 polarization (calvez2025novelinsightsinto pages 4-6, petit2025advancesinunderstanding pages 12-13).
- Tissue compartmentalization yields location-specific programs: interferon/myeloid–stromal modules and TL1A-driven T-cell activation in perianal fistulizing disease; profibrotic fibroblast networks and creeping fat in small-bowel fibrostenosis (levantovsky2024multimodalsinglecellanalyses pages 1-4, liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4, gudino2025tl1aactivatedtcells pages 1-4).
- Chronic inflammation promotes matrix deposition, smooth muscle hyperplasia, and remodeling, leading to strictures and fistulas; creeping fat amplifies transmural inflammation (liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4).

Phenotypic Manifestations (HP terms examples)
- Small-intestinal strictures and obstruction (stricture/stenosis); perianal fistulas; transmural inflammation; malabsorption related to ileal involvement; extraintestinal manifestations vary by interferon/Th17 programs (liu2024intestinalstricturesin pages 1-2, levantovsky2024multimodalsinglecellanalyses pages 1-4, calvez2025novelinsightsinto pages 4-6).

Gene/protein annotations with ontology terms
- NOD2 (HGNC:5331): GO—pattern recognition receptor signaling, regulation of NF-κB; Cellular component—cytosol; Biological role—antimicrobial autophagy with ATG16L1 (petit2025advancesinunderstanding pages 12-13, petit2025advancesinunderstanding pages 8-9).
- ATG16L1 (HGNC:18585): GO—autophagosome assembly; Cellular component—autophagosome; Function—Paneth-cell granule biology and bacterial clearance (petit2025advancesinunderstanding pages 12-13, sun2024macrophagelrrk2hyperactivity pages 1-3).
- LRRK2 (HGNC:18618): GO—protein serine/threonine kinase activity; Process—negative regulation of autophagy (hyperactive variants); Component—cytoplasm of myeloid lineage cells (sun2024macrophagelrrk2hyperactivity pages 1-3).
- TNFSF15/TL1A (HGNC:11947) and TNFRSF25/DR3 (HGNC:11903): GO—T-cell costimulation; TNF receptor signaling; Process—fibrosis-associated fibroblast activation (gudino2025tl1aactivatedtcells pages 1-4).
- IL23A/IL23R (HGNC: 6008/19100): GO—JAK-STAT signaling; Th17 differentiation (calvez2025novelinsightsinto pages 4-6).
- IFNG (HGNC:5438): GO—type II interferon signaling; myeloid activation (levantovsky2024multimodalsinglecellanalyses pages 1-4).
- CHI3L1 (HGNC:1933); OSM (HGNC:8506): GO—extracellular matrix organization and inflammation; fibroblast–myeloid signaling in fistula (levantovsky2024multimodalsinglecellanalyses pages 1-4).
- TGFB1 (HGNC:11766), WNT5A (HGNC:12784), MMPs/TIMPs: GO—tissue remodeling and fibrosis (liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4).

Cell type involvement (CL terms examples)
- Paneth cell (intestinal epithelial cell, secretory lineage) (sun2024macrophagelrrk2hyperactivity pages 1-3).
- CD4+ Th17 cell; pathogenic Th17 (calvez2025novelinsightsinto pages 4-6).
- Macrophage (including IFN-polarized signatures) (levantovsky2024multimodalsinglecellanalyses pages 1-4, calvez2025novelinsightsinto pages 4-6).
- Neutrophil (in fistula and fibrotic niches) (levantovsky2024multimodalsinglecellanalyses pages 1-4, liu2024intestinalstricturesin pages 1-2).
- Stromal fibroblast/myofibroblast (fibrosis drivers) (liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4).
- Mesenteric adipocyte/preadipocyte (creeping fat) (zhou2025insightsintothe pages 2-4).

Anatomical locations (UBERON examples)
- Terminal ileum; rectal mucosa; perianal fistula tracts; intestinal wall (mucosa/submucosa/muscularis propria); mesenteric adipose tissue (levantovsky2024multimodalsinglecellanalyses pages 1-4, sun2024macrophagelrrk2hyperactivity pages 1-3, liu2024intestinalstricturesin pages 1-2, zhou2025insightsintothe pages 2-4, gudino2025tl1aactivatedtcells pages 1-4).

Current applications and real-world implementations
- Anti-IL-23 biologics are in clinical use for CD, reflecting centrality of the IL-23/Th17 axis (calvez2025novelinsightsinto pages 4-6).
- TL1A inhibition is a precision-medicine strategy under active evaluation; single-cell data in perianal CD substantiate a TL1A–LTα1β2/IL-22 mucosal remodeling axis potentially resistant to anti-TNF (gudino2025tl1aactivatedtcells pages 1-4).
- Targeting autophagy regulators (e.g., LRRK2 kinase inhibitors) has preclinical support for restoring Paneth-cell homeostasis and may be relevant for selected genetic subgroups (sun2024macrophagelrrk2hyperactivity pages 1-3).
- Imaging- and biomarker-driven stratification of fibrostenotic disease is advancing; however, no approved anti-fibrotic therapy exists for intestinal strictures (liu2024intestinalstricturesin pages 1-2).

Expert opinions and analysis (authoritative sources)
- Fibrostenosis remains “among the largest unmet needs” in IBD, with progress driven by single-cell mapping of fibroblast subsets and matrix pathways, yet absent disease-modifying antifibrotics (liu2024intestinalstricturesin pages 1-2). Reviews of stenosis mechanisms converge on TGF-β/SMAD, WNT/β-catenin, and immune–stromal axes as key targets (zhou2025insightsintothe pages 2-4). Fistulizing disease appears to be sustained by myeloid–stromal–IFN circuits and TL1A-activated T cells that remodel the mucosa, providing a rationale for IFN/JAK-pathway and TL1A-directed therapies (levantovsky2024multimodalsinglecellanalyses pages 1-4, gudino2025tl1aactivatedtcells pages 1-4).

Relevant statistics and recent data
- Fibrostenosis and surgery: Approximately 35% of patients develop intestinal strictures, and complications requiring surgery occur in up to 70% within 10 years—underscoring the progressive fibrotic burden (liu2024intestinalstricturesin pages 1-2). Single-cell data nominate fibroblast subtypes (e.g., CXCL14+ and MMP/WNT5A+) as pivotal in stricturing CD (liu2024intestinalstricturesin pages 1-2).

Selected evidence quotes (verbatim)
- “LRRK2-mediated pro-inflammatory cytokine release from phagocytes impaired Paneth cell function, which was rescued by LRRK2 kinase inhibition through activation of autophagy.” (Science Immunology, 2024) (sun2024macrophagelrrk2hyperactivity pages 1-3).
- “Fistula tracts are enriched for myeloid cells and show pronounced myeloid–stromal cross-talk… [and] stromal/fibroblast cells… highly upregulate CHI3L1 and exhibit both destructive and fibrotic transcriptional programs.” (Med, 2024) (levantovsky2024multimodalsinglecellanalyses pages 1-4).
- “TL1A-activated CD4+ T cells… [induce] a PFD-associated signature in fibroblasts and epithelial cells… independent of TNF signaling,” nominating TL1A inhibition. (bioRxiv, 2025) (gudino2025tl1aactivatedtcells pages 1-4).
- “Stricturing Crohn’s disease is common… about 35% develop intestinal strictures… [and] complications requiring surgery occur in up to 70% within 10 years.” (UEGJ, 2024) (liu2024intestinalstricturesin pages 1-2).

Gene/protein, process, phenotype, cell, anatomy, chemical annotations (structured)
- HGNC: NOD2; ATG16L1; LRRK2; TNFSF15; TNFRSF25; IL23A; IL23R; IFNG; CHI3L1; OSM; TGFB1; WNT5A; MMP family; TIMP family (levantovsky2024multimodalsinglecellanalyses pages 1-4, calvez2025novelinsightsinto pages 4-6, sun2024macrophagelrrk2hyperactivity pages 1-3, liu2024intestinalstricturesin pages 1-2, petit2025advancesinunderstanding pages 12-13, zhou2025insightsintothe pages 2-4, gudino2025tl1aactivatedtcells pages 1-4).
- GO processes: autophagy; cytokine-mediated signaling pathway; Th17 cell differentiation; T-cell costimulation; interferon-gamma-mediated signaling; extracellular matrix organization; WNT signaling; TGF-β receptor signaling; inflammatory response (same citations as above).
- HP phenotypes: intestinal stenosis/stricture; perianal fistula; transmural intestinal inflammation; small-bowel malabsorption (liu2024intestinalstricturesin pages 1-2, levantovsky2024multimodalsinglecellanalyses pages 1-4, calvez2025novelinsightsinto pages 4-6).
- CL cell types: Paneth cell; Th17 cell; macrophage; neutrophil; stromal fibroblast/myofibroblast; adipocyte/preadipocyte (mesenteric) (same citations as above).
- UBERON anatomy: terminal ileum; rectal mucosa; perianal region; intestinal wall (mucosa/submucosa/muscularis propria); mesenteric adipose tissue (same citations as above).
- CHEBI: Not primary (biologics/immune proteins predominate in cited mechanisms) (calvez2025novelinsightsinto pages 4-6, gudino2025tl1aactivatedtcells pages 1-4).

Embedded summary table
| Mechanism | Key genes/proteins (HGNC) | Principal cell types (CL) | Pathways / Processes (GO-like) | Anatomical sites (UBERON) | Notes on clinical translation | Evidence |
|---|---|---|---|---|---|---|
| IL-23 / Th17 axis | IL23A, IL23R, RORC, STAT3 | Th17 cells; dendritic cells (CL) | IL-23 signaling; Th17 differentiation; JAK-STAT signaling | Intestinal lamina propria (UBERON) | Proven therapeutic target — anti-IL-23 biologics used in IBD; biomarkers under evaluation | (calvez2025novelinsightsinto pages 4-6) |
| TL1A–DR3 signaling | TNFSF15 (TL1A), TNFRSF25 (DR3) | CD4+ T cells, dendritic cells, stromal fibroblasts (CL) | TNF/TNFR superfamily costimulation; T-cell co-stimulation; pro-fibrotic fibroblast activation | Intestinal mucosa (UBERON) | Anti-TL1A agents in development (precision-medicine potential for fistulizing/fibrostenotic disease) | (gudino2025tl1aactivatedtcells pages 1-4) |
| Interferon programs & myeloid–stromal crosstalk in fistula | IFNG, CXCL9, CHI3L1, OSM | Myeloid cells (macrophages), pathogenic Th17, fibroblasts (CL) | Type II interferon signaling; myeloid–stromal ligand–receptor signalling; ECM remodelling | Perianal fistula tracts; rectal mucosa (UBERON) | Identifies IFN-driven modules and myeloid–stromal targets; suggests JAK/IFN pathway modulation for fistulizing disease | (levantovsky2024multimodalsinglecellanalyses pages 1-4), (gudino2025tl1aactivatedtcells pages 1-4) |
| Autophagy / Paneth-cell dysfunction (NOD2, ATG16L1, LRRK2) | NOD2, ATG16L1, LRRK2 | Paneth cells (epithelial), lamina propria macrophages (CL) | Autophagy / xenophagy; antimicrobial peptide secretion; intracellular pathogen handling | Terminal ileum (UBERON) | Genetic variants (ATG16L1, NOD2, LRRK2) impair autophagy; LRRK2 kinase inhibitors rescue autophagy in preclinical studies | (sun2024macrophagelrrk2hyperactivity pages 1-3), (petit2025advancesinunderstanding pages 12-13) |
| Microbial drivers: AIEC & fungi (CARD9-mediated) | CARD9 (host); pathobiont traits in AIEC strains | Intestinal epithelial cells, macrophages, neutrophils (CL) | Pattern recognition / antifungal pathways; dysbiosis-driven PRR activation; impaired bacterial clearance | Ileal mucosa, mesenteric lymphoid tissue (UBERON) | Microbiome-targeted interventions (antimicrobials, phage, FMT) and host–fungal immune axes are active translational areas | (calvez2025novelinsightsinto pages 4-6), (petit2025advancesinunderstanding pages 12-13) |
| Fibrosis circuits (TWIST1+ FAP+ fibroblasts; neutrophil–fibroblast crosstalk; WNT/TGF-β) | TWIST1, FAP, WNT5A, TGFB1, MMPs, TIMPs | FAP+ fibroblasts, CD150+ inflammatory monocytes, neutrophils, macrophages (CL) | TGF-β/SMAD signaling; Wnt/β-catenin; ECM organization and remodeling; EMT | Intestinal wall (ileum, colon) (UBERON) | Single-cell studies nominate fibroblast subtypes (TWIST1+FAP+) and immune–stromal axes as antifibrotic targets; no approved anti-fibrotics yet | (liu2024intestinalstricturesin pages 1-2), (zhou2025insightsintothe pages 2-4) |
| Creeping fat (mesenteric adipose) | PPARG, ADIPOQ, PTX3 (PTX3) | Mesenteric adipocytes / preadipocytes; infiltrating immune cells (macrophages) (CL) | Adipokine signaling; lipid metabolism–immune crosstalk; paracrine pro-fibrotic signaling | Mesenteric adipose tissue / creeping fat (UBERON) | Imaging (mesenteric creeping-fat indices) associates creeping fat with transmural healing and fibrosis risk; creeping fat is an emerging therapeutic/biomarker target | (zhou2025insightsintothe pages 2-4), (liu2024intestinalstricturesin pages 1-2) |


*Table: Compact summary table linking major molecular/cellular mechanisms in Crohn disease to genes, cell types, pathway motifs, anatomical sites, translational notes, and primary evidence (pqac IDs and DOI/year); useful as a quick reference for knowledge-base curation.*

Current applications and trials (2023–2024 emphasis)
- Anti-IL-23 treatments reflect robust IL-23/Th17 involvement across IBD and Crohn disease patient subsets (calvez2025novelinsightsinto pages 4-6). 
- TL1A inhibition is supported by human single-cell pathobiology in PFD and is being advanced as a precision approach to inflammation–fibrosis–fistula circuits (gudino2025tl1aactivatedtcells pages 1-4).
- Emerging precision concepts include stratifying genetic-autophagy subtypes (e.g., LRRK2/ATG16L1/NOD2) for autophagy-restoring strategies (sun2024macrophagelrrk2hyperactivity pages 1-3).

Limitations and knowledge gaps
- Despite improved single-cell resolution of fibroblast heterogeneity and immune–stromal crosstalk, there remain no approved anti-fibrotic drugs for intestinal fibrostenosis; endpoints and biomarkers are under development (liu2024intestinalstricturesin pages 1-2).
- Fistula biology implicates interferon and TL1A pathways, but prospective stratified interventional studies are needed to confirm therapeutic responsiveness (levantovsky2024multimodalsinglecellanalyses pages 1-4, gudino2025tl1aactivatedtcells pages 1-4).

References (URLs and publication dates included where available)
- Levantovsky RM et al. Med. 2024;5:886-908.e11. Multimodal single-cell analyses reveal mechanisms of perianal fistula (https://doi.org/10.1016/j.medj.2024.03.021). (levantovsky2024multimodalsinglecellanalyses pages 1-4)
- Calvez V et al. Biomedicines. 2025;13:305. Novel insights into IBD pathogenesis (https://doi.org/10.3390/biomedicines13020305). (calvez2025novelinsightsinto pages 4-6)
- Sun S et al. Science Immunology. 2024;9:eadi7907. LRRK2 hyperactivity impairs autophagy and induces Paneth-cell dysfunction (https://doi.org/10.1126/sciimmunol.adi7907). (sun2024macrophagelrrk2hyperactivity pages 1-3)
- Liu Z et al. UEG Journal. 2024;12:802-813. Intestinal strictures in Crohn’s disease: update from 2023 (https://doi.org/10.1002/ueg2.12568). (liu2024intestinalstricturesin pages 1-2)
- Petit C et al. IJMS. 2025;26:6133. Intestinal homeostasis lessons from IBD and monogenic disorders (https://doi.org/10.3390/ijms26136133). (petit2025advancesinunderstanding pages 12-13, petit2025advancesinunderstanding pages 8-9)
- Zhou Y et al. Biomedicines. 2025;13:1777. Molecular mechanisms and strategies of stenosis fibrosis in CD (https://doi.org/10.3390/biomedicines13071777). (zhou2025insightsintothe pages 2-4)
- Gudiño V et al. bioRxiv. 2025. TL1A-activated T cells remodel rectal mucosa in CD with PFD (https://doi.org/10.1101/2025.06.26.657455). (gudino2025tl1aactivatedtcells pages 1-4)


References

1. (levantovsky2024multimodalsinglecellanalyses pages 1-4): Rachel M. Levantovsky, Christopher Tastad, Jiayu Zhang, Kyle Gettler, Ksenija Sabic, Robert Werner, Colleen Chasteau, Ujunwa Korie, Diana Paguay, Michelle Bao, Huajun Han, Neha Maskey, Sayali Talware, Manishkumar Patel, Carmen Argmann, Mayte Suarez-Farinas, Noam Harpaz, Ling-shiang Chuang, and Judy H. Cho. Multimodal single-cell analyses reveal mechanisms of perianal fistula in diverse patients with crohn’s disease. Med, 5:886-908.e11, Aug 2024. URL: https://doi.org/10.1016/j.medj.2024.03.021, doi:10.1016/j.medj.2024.03.021. This article has 9 citations and is from a domain leading peer-reviewed journal.

2. (sun2024macrophagelrrk2hyperactivity pages 1-3): Shengxiang Sun, Miki Hodel, Xiang Wang, Javier De Vicente, Talin Haritunians, Anketse Debebe, Chen-Ting Hung, Changqing Ma, Atika Malique, Hoang N. Nguyen, Maayan Agam, Michael T. Maloney, Marisa S. Goo, Jillian H. Kluss, Richa Mishra, Jennifer Frein, Amanda Foster, Samuel Ballentine, Uday Pandey, Justin Kern, Shaohong Yang, Emebet Mengesha, Iyshwarya Balasubramanian, Annie Arguello, Anthony A. Estrada, Nan Gao, Inga Peter, Dermot P. B. McGovern, Anastasia G. Henry, Thaddeus S. Stappenbeck, and Ta-Chiang Liu. Macrophage lrrk2 hyperactivity impairs autophagy and induces paneth cell dysfunction. Science immunology, 9 101:eadi7907, Nov 2024. URL: https://doi.org/10.1126/sciimmunol.adi7907, doi:10.1126/sciimmunol.adi7907. This article has 5 citations and is from a highest quality peer-reviewed journal.

3. (liu2024intestinalstricturesin pages 1-2): Zishan Liu, Zhuoyan Huang, Yu Wang, Shanshan Xiong, Sinan Lin, Jinshen He, Jinyu Tan, Caiguang Liu, Xiaomin Wu, Jing Nie, Weidong Huang, Yao Zhang, Longyuan Zhou, and Ren Mao. Intestinal strictures in crohn's disease: an update from 2023. United European Gastroenterology Journal, 12:802-813, Mar 2024. URL: https://doi.org/10.1002/ueg2.12568, doi:10.1002/ueg2.12568. This article has 14 citations and is from a peer-reviewed journal.

4. (zhou2025insightsintothe pages 2-4): Yuan Zhou, Huiping Chen, Qinbo Wang, Guozeng Ye, Yingjuan Ou, Lihong Huang, Xia Wu, and Jiaxi Fei. Insights into the molecular mechanisms and novel therapeutic strategies of stenosis fibrosis in crohn’s disease. Biomedicines, 13:1777, Jul 2025. URL: https://doi.org/10.3390/biomedicines13071777, doi:10.3390/biomedicines13071777. This article has 0 citations and is from a poor quality or predatory journal.

5. (calvez2025novelinsightsinto pages 4-6): Valentin Calvez, Pierluigi Puca, Federica Di Vincenzo, Angelo Del Gaudio, Bianca Bartocci, Marco Murgiano, Jacopo Iaccarino, Erfan Parand, Daniele Napolitano, Daniela Pugliese, Antonio Gasbarrini, and Franco Scaldaferri. Novel insights into the pathogenesis of inflammatory bowel diseases. Biomedicines, 13:305, Jan 2025. URL: https://doi.org/10.3390/biomedicines13020305, doi:10.3390/biomedicines13020305. This article has 35 citations and is from a poor quality or predatory journal.

6. (gudino2025tl1aactivatedtcells pages 1-4): Victoria Gudiño, Jae-Won Cho, Berta Caballol, Ana M. Corraliza, Marisol Veny, Isabella Dotti, Livia Moreira Genaro, Ángela Sanzo-Machuca, Elisa Melón-Ardanaz, M. Carme Masamunt, Miriam Esteller, Iris Teubel, Lisseth Robbins, Ángel Giner, Cristina Prieto, Elena Ferrer, Raquel Franco-Leal, Albert Martin-Cardona, Carme Loras, Maria Esteve, Jordi Rimola, Agnès Fernández-Clotet, Ingrid Ordás, Elena Ricart, Julian Panés, Martin Hemberg, and Azucena Salas. Tl1a-activated t cells remodel the rectal mucosa in crohn’s disease patients with perianal fistulizing disease. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.26.657455, doi:10.1101/2025.06.26.657455. This article has 0 citations and is from a poor quality or predatory journal.

7. (petit2025advancesinunderstanding pages 12-13): Céline Petit, Aurore Rozières, Gilles Boschetti, Christophe Viret, Mathias Faure, Stéphane Nancey, and Rémi Duclaux-Loras. Advances in understanding intestinal homeostasis: lessons from inflammatory bowel disease and monogenic intestinal disorder pathogenesis. International Journal of Molecular Sciences, 26:6133, Jun 2025. URL: https://doi.org/10.3390/ijms26136133, doi:10.3390/ijms26136133. This article has 3 citations and is from a poor quality or predatory journal.

8. (petit2025advancesinunderstanding pages 8-9): Céline Petit, Aurore Rozières, Gilles Boschetti, Christophe Viret, Mathias Faure, Stéphane Nancey, and Rémi Duclaux-Loras. Advances in understanding intestinal homeostasis: lessons from inflammatory bowel disease and monogenic intestinal disorder pathogenesis. International Journal of Molecular Sciences, 26:6133, Jun 2025. URL: https://doi.org/10.3390/ijms26136133, doi:10.3390/ijms26136133. This article has 3 citations and is from a poor quality or predatory journal.