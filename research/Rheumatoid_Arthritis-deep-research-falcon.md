---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:02:05.314734'
end_time: '2025-12-15T09:09:47.517226'
duration_seconds: 462.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rheumatoid Arthritis
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
- **Disease Name:** Rheumatoid Arthritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Rheumatoid Arthritis**.
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
- **Disease Name:** Rheumatoid Arthritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Rheumatoid Arthritis**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Rheumatoid Arthritis
- MONDO ID: MONDO:0005359 (Rheumatoid arthritis)
- Category: Complex

Research Objectives
This report synthesizes recent (prioritized 2023–2024) evidence on molecular and cellular mechanisms of rheumatoid arthritis (RA), integrating genetics, mucosal origins, innate–adaptive immunity, stromal niches, and dysregulated pathways.

Pathophysiology description
Rheumatoid arthritis is a systemic autoimmune disease characterized by a breakdown of tolerance to post-translationally modified self-antigens (notably citrullinated proteins) and by chronic synovitis with stromal remodeling. Contemporary models converge on mucosal origins in subsets of patients: aberrant immune activation in lung, oral, and gut mucosa (linked to dysbiosis, epithelial barrier dysfunction, and local citrullination) precedes and drives systemic autoimmunity with IgA-class autoantibodies (ACPA, RF) and eventually joint-localized synovitis (Holers et al., 2024) (holers2024distinctmucosalendotypes pages 21-23). Synovial tissue single-cell and spatial studies define heterogeneous inflammatory states marked by pathogenic macrophage and fibroblast programs, T peripheral helper (Tph) cells that sustain B-cell responses, and ectopic lymphoid activation, underpinned by genetic risk centered on HLA-DRB1 shared-epitope alleles presenting citrullinated epitopes to CD4+ T cells (Jonsson, 2024) (jonsson2024synovialtissueinsights pages 9-11).

Core mechanisms
- Adaptive autoimmunity and HLA–peptide presentation: HLA-DRB1 shared epitope (SE) alleles preferentially present citrullinated peptides to CD4+ T cells, providing a genetic scaffold for ACPA-positive disease; mucosal priming and epitope spreading are hallmarks in pre-RA (Jonsson, 2024; Holers et al., 2024) (jonsson2024synovialtissueinsights pages 9-11, holers2024distinctmucosalendotypes pages 21-23).
- Mucosal origins and microbiome: RA-related autoantibodies and mucosal immune activation are detected in lung/oral/gut mucosa before arthritis; mechanistic links include bacterial PAD (Porphyromonas gingivalis) and LtxA (Aggregatibacter actinomycetemcomitans)–induced neutrophil hypercitrullination; Prevotella copri and metabolite pathways (e.g., indoles) modulate Th17 responses and disease penetrance (Seymour et al., 2024) (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13). Notably, a large 2024 quantitative profiling study in at-risk first-degree relatives found no stage-specific gut microbiome signature overall, underscoring cohort heterogeneity (RMD Open 2024, Gilbert et al., summarized in Holers 2024) (holers2024distinctmucosalendotypes pages 21-23).
- Innate immunity and citrullination sources: Neutrophil extracellular traps (NETs) release citrullinated histones and autoantigens; platelets and monocytes add to the antigenic pool via PAD expression and surface PAD4 activity; citrullination of complement C1 inhibitor (C1-INH) impairs complement regulation (Seymour et al., 2024) (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13). These processes interface with stromal and adaptive responses in synovium (Jonsson, 2024) (jonsson2024synovialtissueinsights pages 9-11).
- Synovial stromal and myeloid circuits: Perivascular Notch/TGF-β–patterned fibroblast niches (including COMPhi fibrogenic states) and SPP1+ macrophages sustain inflammation and remodeling; Tph cells drive B-cell/plasma cell responses and ectopic lymphoid structures (Jonsson, 2024) (jonsson2024synovialtissueinsights pages 9-11).

Dysregulated pathways
- JAK/STAT: Central conduit for IL-6 and interferon signaling; clinical targeting (JAK inhibitors) validates pathogenic relevance in both immune and stromal compartments (Ghang et al., 2025 overview citing 2023–2024 primary work) (ghang2025currentstateand pages 1-3). 
- TNF/IL-6/IL-17 and NF-κB: Canonical inflammatory axes sustaining synovitis and systemic features (Ghang et al., 2025; Jonsson, 2024) (ghang2025currentstateand pages 1-3, jonsson2024synovialtissueinsights pages 9-11).
- PI3K/AKT/mTOR and MAPK/ERK: Drive fibroblast-like synoviocyte (FLS) proliferation, invasiveness, and cytokine production; integrate TNF/IL-1 signals (Jonsson, 2024; Ghang et al., 2025) (jonsson2024synovialtissueinsights pages 9-11, ghang2025currentstateand pages 1-3).
- cGAS–STING: DNA-sensing innate pathway implicated in synovial IFN programs and chronic inflammation (Ghang et al., 2025) (ghang2025currentstateand pages 1-3).

Disease progression (sequence of events)
1) Mucosal priming: Dysbiosis, PAD/LtxA-triggered hypercitrullination, barrier dysfunction; emergence of IgA ACPA/RF; mucosal Th17/Tph polarization (Holers et al., 2024; Seymour et al., 2024) (holers2024distinctmucosalendotypes pages 21-23, seymour2024microbialmechanismsof pages 1-3).
2) Systemic autoimmunity: Affinity maturation and epitope spreading of ACPA; HLA-DRB1 SE–restricted CD4+ T-cell responses to citrullinated epitopes; circulating immune complexes (Holers et al., 2024) (holers2024distinctmucosalendotypes pages 21-23).
3) Articular localization: Recruitment of myeloid cells; NETosis and monocyte/macrophage activation; FLS activation via TNF/IL‑1/IL‑6/NF‑κB and PI3K/AKT/MAPK cascades; ectopic lymphoid structures and plasma cell accrual (Jonsson, 2024) (jonsson2024synovialtissueinsights pages 9-11).
4) Chronicity/remodeling: SPP1+ macrophage–fibroblast–T cell circuits, perivascular TGF‑β/Notch niches (COMPhi) drive persistent inflammation and fibrosis; osteoclastogenesis causes erosions (Jonsson, 2024) (jonsson2024synovialtissueinsights pages 9-11).

Key Molecular Players
- Genes/Proteins (HGNC): HLA‑DRB1 (shared epitope); PADI4/PADI2 (citrullination enzymes); IL6R (IL‑6 signaling); TNF (master cytokine); JAKs/TYK2 (JAK/STAT conduit) (Jonsson, 2024; Holers, 2024; Ghang, 2025) (jonsson2024synovialtissueinsights pages 9-11, holers2024distinctmucosalendotypes pages 21-23, ghang2025currentstateand pages 1-3).
- Chemical Entities (CHEBI/Concepts): Citrullinated peptides; platelet microparticles carrying citrullinated proteins; complement C1‑INH (citrullinated) (Seymour, 2024) (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13).
- Cell Types (CL): Fibroblast-like synoviocytes (perivascular, COMPhi); SPP1+ macrophages; Tph CD4+ cells; B cells/plasma cells; neutrophils (NETs); monocytes/osteoclast precursors (Jonsson, 2024) (jonsson2024synovialtissueinsights pages 9-11).
- Anatomical Locations (UBERON): Lung, gut, oral mucosa (mucosal endotypes); synovium (Holers, 2024; Jonsson, 2024) (holers2024distinctmucosalendotypes pages 21-23, jonsson2024synovialtissueinsights pages 9-11).

Biological Processes (GO) disrupted
- Antigen processing/presentation via MHC class II; cytokine-mediated signaling (JAK/STAT); NF‑κB activation; cell proliferation/migration (PI3K/AKT/mTOR; MAPK/ERK); DNA sensing (cGAS–STING); neutrophil degranulation/NET formation; complement regulation (citrullinated C1‑INH) (Ghang 2025; Jonsson 2024; Seymour 2024; Holers 2024) (ghang2025currentstateand pages 1-3, jonsson2024synovialtissueinsights pages 9-11, seymour2024microbialmechanismsof pages 1-3, holers2024distinctmucosalendotypes pages 21-23, seymour2024microbialmechanismsof pages 12-13).

Cellular Components
- Cell surface HLA‑DR peptide-binding groove (shared epitope); nuclear/cytosolic PAD localization and extracellular exposure on monocyte surfaces; extracellular traps (NETs); perivascular synovial niches with endothelial–fibroblast Notch crosstalk; platelet-derived microparticles in synovial/extracellular space; complement components in plasma/synovial fluid (Jonsson, 2024; Seymour, 2024) (jonsson2024synovialtissueinsights pages 9-11, seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13).

Phenotype associations (HP)
- Chronic symmetric polyarthritis with morning stiffness, synovial hypertrophy, joint erosions; extra-articular mucosal and pulmonary involvement in subsets (Holers, 2024; Jonsson, 2024) (holers2024distinctmucosalendotypes pages 21-23, jonsson2024synovialtissueinsights pages 9-11).

Expert opinions and 2023–2024 developments
- Mucosal endotypes: Holers et al. (2024) propose distinct mucosal trajectories (lung, gut, oral) that initiate/drive RA and emphasize that IgA autoimmunity, airway abnormalities, and mucosa-derived immune responses can precede joint disease; dietary fiber/SCFA and indole pathways modulate systemic inflammation (with mechanistic preclinical support) (holers2024distinctmucosalendotypes pages 21-23).
- Synovial heterogeneity: Jonsson (2024) summarizes single-cell/spatial insights—B cell–rich synovitis and macrophage/fibroblast niches predict therapeutic responses and highlight Notch/TGF‑β patterning, SPP1+ macrophages, and Tph cells as actionable axes (jonsson2024synovialtissueinsights pages 9-11).
- Microbiome mechanisms: Seymour et al. (2024) synthesize bacterial PAD/LtxA-driven hypercitrullination, molecular mimicry (e.g., P. copri antigens), microbial translocation (e.g., Fusobacterium OMVs), and metabolite-immune interactions; importantly, not all cohorts show consistent dysbiosis signals (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13).

Relevant statistics and data
- Progression risk: In ACPA-positive individuals, ~40–60% progress to RA over 2–5 years, often with mucosal IgA autoantibodies preceding disease (Seymour 2024; citing cohort data within review) (seymour2024microbialmechanismsof pages 1-3).
- Microbiome null findings: A 2024 study of 371 first-degree relatives at preclinical stages found no significant quantitative microbiome profile differences across disease stages (PERMANOVA R2≈0.008, p=0.56), tempering generalizations about universal dysbiosis signatures (as summarized in Holers 2024) (holers2024distinctmucosalendotypes pages 21-23).
- Synovial stratification and therapy: B cell–rich synovitis associates with better rituximab response, whereas B cell–poor/inflammatory pathotypes may favor IL‑6 receptor blockade (tocilizumab) (Jonsson 2024) (jonsson2024synovialtissueinsights pages 9-11).

Evidence items with PMIDs/URLs (selection; 2023–2024 priority)
- Holers VM et al. Distinct mucosal endotypes as initiators and drivers of rheumatoid arthritis. Nat Rev Rheumatol. 2024 Sep;20(10):601–613. doi:10.1038/s41584-024-01154-0. https://doi.org/10.1038/s41584-024-01154-0 (holers2024distinctmucosalendotypes pages 21-23).
- Jonsson AH. Synovial Tissue Insights into Heterogeneity of Rheumatoid Arthritis. Curr Rheumatol Rep. 2024 Dec;26:81–88. doi:10.1007/s11926-023-01129-2. https://doi.org/10.1007/s11926-023-01129-2 (jonsson2024synovialtissueinsights pages 9-11).
- Seymour BJ, Allen BE, Kuhn KA. Microbial Mechanisms of Rheumatoid Arthritis Pathogenesis. Curr Rheumatol Rep. 2024 Feb;26:124–132. doi:10.1007/s11926-024-01135-y. https://doi.org/10.1007/s11926-024-01135-y (seymour2024microbialmechanismsof pages 1-3).
- Seymour BJ et al. (mechanistic details on PAD/LtxA, mimicry, metabolites) (seymour2024microbialmechanismsof pages 12-13).
- Ghang B et al. Current state and future directions of basic research in rheumatoid arthritis. J Rheum Dis. 2025;32:166–181. doi:10.4078/jrd.2024.0151 (overview integrating 2023–2024 insights). https://doi.org/10.4078/jrd.2024.0151 (ghang2025currentstateand pages 1-3).

Ontology-linked annotations
- Gene/protein (HGNC): HLA‑DRB1; PADI4; PADI2; IL6R; TNF; JAK1/JAK2/TYK2 (jonsson2024synovialtissueinsights pages 9-11, holers2024distinctmucosalendotypes pages 21-23, ghang2025currentstateand pages 1-3).
- Biological process (GO): “cytokine-mediated signaling pathway”; “positive regulation of NF‑κB transcription factor activity”; “phosphatidylinositol 3-kinase signaling”; “MAPK cascade”; “DNA sensing via cGAS–STING”; “neutrophil extracellular trap formation”; “antigen processing and presentation of peptide antigen via MHC class II”; “complement activation, classical pathway” (jonsson2024synovialtissueinsights pages 9-11, ghang2025currentstateand pages 1-3, seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13, holers2024distinctmucosalendotypes pages 21-23).
- Cell types (CL): fibroblast-like synoviocytes; macrophage SPP1+ subset; neutrophil; monocyte; osteoclast; T peripheral helper (Tph); B cell; plasma cell (jonsson2024synovialtissueinsights pages 9-11, seymour2024microbialmechanismsof pages 1-3).
- Anatomical locations (UBERON): synovial membrane; lung; oral mucosa; intestinal mucosa (holers2024distinctmucosalendotypes pages 21-23, jonsson2024synovialtissueinsights pages 9-11).
- Chemical entities (CHEBI/concepts): citrullinated peptides; platelet microparticles; complement C1 inhibitor (citrullinated) (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13).
- Phenotypes (HP): HP:0001371 (Arthritis); HP:0000988 (Morning stiffness); HP:0011800 (Erosive arthritis); HP:0002093 (Interstitial lung disease) (contextualized in mucosal endotype subsets) (holers2024distinctmucosalendotypes pages 21-23, jonsson2024synovialtissueinsights pages 9-11).

Applications and real-world implementations
- Precision stratification: Synovial biopsy and scRNA/spatial signatures (B cell–rich pathotype, SPP1+ macrophages, COMPhi fibroblasts) may inform biologic choice (rituximab vs. tocilizumab) and identify fibrosis-prone, treatment-resistant niches (Jonsson, 2024) (jonsson2024synovialtissueinsights pages 9-11).
- Mucosal risk interception: Monitoring IgA ACPA/RF and mucosal imaging/biomarkers in at-risk individuals; dietary fiber/SCFA modulation and periodontal care are being explored to mitigate mucosal drivers (Holers, 2024) (holers2024distinctmucosalendotypes pages 21-23).
- Targeted signaling blockade: JAK inhibitors and IL‑6/TNF blockade remain effective across phenotypes, underlining pathway centrality (Ghang, 2025 integrating recent trials and mechanistic data) (ghang2025currentstateand pages 1-3).

Included artifact
| Category | Item | Ontology namespace tag | Role/Mechanism | 2023–2024 Evidence |
|---|---|---|---|---|
| Genetic risk | HLA-DRB1 shared epitope | HGNC | Presents citrullinated peptides to CD4+ T cells; major seropositive RA risk allele driving ACPA-associated immunity. | (jonsson2024synovialtissueinsights pages 9-11, ghang2025currentstateand pages 1-3) |
| Enzyme (citrullination) | PADI4 | HGNC | Catalyzes protein citrullination in NETs/METs and immune cells → generates ACPA-target neoepitopes. | (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13, barbera2025theroleof pages 7-11) |
| Enzyme (citrullination) | PADI2 | HGNC | Contributes to citrullination at mucosal sites and in inflammatory cells; complements PAD4 in antigen generation. | (seymour2024microbialmechanismsof pages 12-13, barbera2025theroleof pages 7-11) |
| Cytokine receptor | IL6R | HGNC | Mediates IL-6 signaling (JAK/STAT) driving systemic and synovial inflammation; therapeutic target (tocilizumab). | (ghang2025currentstateand pages 1-3, jonsson2024synovialtissueinsights pages 9-11) |
| Cytokine | TNF | HGNC | Central proinflammatory driver of synovitis, FLS activation and leukocyte recruitment; target of TNF inhibitors. | (ghang2025currentstateand pages 1-3, jonsson2024synovialtissueinsights pages 9-11) |
| Signaling pathway | TYK2 / JAK-STAT | GO | Intracellular route for cytokine signals (IL-6, IFNs); dysregulated in RA and targeted by JAK inhibitors. | (ghang2025currentstateand pages 1-3, barbera2025theroleof pages 7-11) |
| Signaling pathway | NF-κB signaling | GO | Transcriptional hub for proinflammatory cytokines and survival signals in immune/fibroblast cells. | (ghang2025currentstateand pages 1-3, barbera2025theroleof pages 7-11) |
| Signaling pathway | PI3K/AKT/mTOR | GO | Promotes FLS proliferation, survival and invasive phenotype; implicated in synovial hyperplasia. | (jonsson2024synovialtissueinsights pages 9-11, ghang2025currentstateand pages 1-3) |
| Signaling pathway | MAPK/ERK | GO | Regulates cytokine production and FLS responses contributing to synovitis and tissue damage. | (ghang2025currentstateand pages 1-3, barbera2025theroleof pages 7-11) |
| Innate sensing | cGAS–STING pathway | Pathway | DNA-sensing innate pathway implicated in synovial type-I IFN and inflammatory responses in arthritis. | (barbera2025theroleof pages 7-11, ghang2025currentstateand pages 1-3) |
| Stromal niche | Fibroblast-like synoviocytes — perivascular COMPhi / TGF-β–Notch niche | CL / UBERON | Perivascular COMPhi fibroblasts form TGF-β gradients (Notch-regulated) driving fibrogenic remodeling and treatment resistance. | (jonsson2024synovialtissueinsights pages 9-11) |
| Myeloid subset | Macrophage SPP1+ subset | CL | Pathogenic synovial macrophage subset that communicates with T cells and fibroblasts to sustain inflammation. | (jonsson2024synovialtissueinsights pages 9-11, seymour2024microbialmechanismsof pages 12-13) |
| T cell subset | T peripheral helper (Tph) cells | CL | Provide B-cell help in synovium (CXCL13/IL-21) promoting local ACPA-producing plasma cells and ectopic responses. | (jonsson2024synovialtissueinsights pages 9-11, ghang2025currentstateand pages 1-3) |
| Lymphoid structures | B cells / plasma cells & ectopic lymphoid structures | CL | Local antibody generation (ACPA, RF) within synovium/mucosa; predicts response to B-cell targeted therapy. | (jonsson2024synovialtissueinsights pages 9-11, perera2024clinicalphenotypesserological pages 20-21) |
| Innate effector | Neutrophils & NETs | CL / GO | NETosis (PAD4-driven) releases citrullinated antigens and DAMPs that amplify autoimmunity and synovial inflammation. | (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13) |
| Monocyte lineage | Monocytes → Osteoclastogenesis | CL / GO | Monocyte-derived osteoclast differentiation (RANKL-driven) mediates bone erosion; monocyte activation linked to HLA-SE. | (ghang2025currentstateand pages 1-3, jonsson2024synovialtissueinsights pages 9-11) |
| Complement regulation | Complement C1 inhibitor — citrullination | CHEBI / GO | Citrullination of C1-INH impairs complement/contact system regulation, increasing inflammatory complement activity. | (seymour2024microbialmechanismsof pages 12-13, ghang2025currentstateand pages 1-3) |
| Extracellular vesicles | Platelet microparticles with citrullinated autoantigens | CHEBI | Platelet-derived microparticles contain PAD4 and citrullinated proteins that can be ACPA targets and activate immunity. | (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13) |
| Cell-surface enzyme | Monocyte surface PAD4 | HGNC / Cell surface | Active PAD4 displayed on monocyte surfaces citrullinates extracellular proteins, creating neoantigens at cell interface. | (jonsson2024synovialtissueinsights pages 9-11, seymour2024microbialmechanismsof pages 1-3) |
| Mucosal sites | Mucosal endotypes: lung, gut, oral | UBERON | Sites of early citrullination, mucosal inflammation and immune priming; mucosal dysbiosis can precede clinical RA. | (holers2024distinctmucosalendotypes pages 21-23, seymour2024microbialmechanismsof pages 1-3, ghang2025currentstateand pages 1-3) |
| Microbiome signals | Prevotella copri; Porphyromonas gingivalis; Aggregatibacter actinomycetemcomitans | Taxon / Concept | Microbial taxa implicated in dysbiosis, citrullination (PPAD/LtxA), molecular mimicry and metabolite-driven immune modulation. | (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13) |
| Cytokine circuit | OSM–OSMR macrophage–fibroblast circuit | Pathway / cytokine | Oncostatin M from macrophages activates OSMR+ fibroblasts generating inflammatory and tissue-destructive programs targeted by JAKi. | (jonsson2024synovialtissueinsights pages 9-11, barbera2025theroleof pages 7-11) |


*Table: Compact reference table mapping core molecular/cellular entities, ontologies, brief mechanisms, and 2023–2024 supporting evidence (context IDs) to aid rapid curation and knowledgebase annotation.*

Direct quotes (supporting statements)
- “Evidence suggests that self-tolerance is breached at mucosal sites… Primary sites studied include the lung, gut and oral mucosa” (Holers 2024) (holers2024distinctmucosalendotypes pages 21-23).
- “Synovial tissue single-cell studies revealed T peripheral helper cells, macrophage subsets, and Notch-shaped fibroblast niches that underpin RA heterogeneity and may predict therapeutic response” (Jonsson 2024) (jonsson2024synovialtissueinsights pages 9-11).
- “Periodontal and enteric pathobionts… produce PAD or leukotoxins that induce hypercitrullination and molecular mimicry, linking dysbiosis to ACPA generation” (Seymour 2024) (seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13).

Limitations and open questions
- Not all cohorts demonstrate consistent gut dysbiosis signatures in pre-RA; host genetics, geography, and exposures likely stratify mucosal endotypes (Holers 2024) (holers2024distinctmucosalendotypes pages 21-23).
- Mechanistic dissection of cGAS–STING in human RA synovia remains an area of active investigation (Ghang 2025) (ghang2025currentstateand pages 1-3).

URLs and dates are provided above alongside each citation. All claims are supported by recent primary/review sources, prioritizing 2023–2024 publications, with integrative context drawn from 2025 overviews where necessary to frame 2023–2024 findings (holers2024distinctmucosalendotypes pages 21-23, jonsson2024synovialtissueinsights pages 9-11, seymour2024microbialmechanismsof pages 1-3, seymour2024microbialmechanismsof pages 12-13, ghang2025currentstateand pages 1-3).

References

1. (holers2024distinctmucosalendotypes pages 21-23): V. Michael Holers, Kristen M. Demoruelle, Jane H. Buckner, Eddie A. James, Gary S. Firestein, William H. Robinson, Allen C. Steere, Fan Zhang, Jill M. Norris, Kristine A. Kuhn, and Kevin D. Deane. Distinct mucosal endotypes as initiators and drivers of rheumatoid arthritis. Nature reviews. Rheumatology, 20:601-613, Sep 2024. URL: https://doi.org/10.1038/s41584-024-01154-0, doi:10.1038/s41584-024-01154-0. This article has 29 citations.

2. (jonsson2024synovialtissueinsights pages 9-11): Anna Helena Jonsson. Synovial tissue insights into heterogeneity of rheumatoid arthritis. Current rheumatology reports, 26:81-88, Dec 2024. URL: https://doi.org/10.1007/s11926-023-01129-2, doi:10.1007/s11926-023-01129-2. This article has 18 citations and is from a peer-reviewed journal.

3. (seymour2024microbialmechanismsof pages 1-3): Brenda J. Seymour, Brendan E. Allen, and Kristine A. Kuhn. Microbial mechanisms of rheumatoid arthritis pathogenesis. Current rheumatology reports, 26:124-132, Feb 2024. URL: https://doi.org/10.1007/s11926-024-01135-y, doi:10.1007/s11926-024-01135-y. This article has 14 citations and is from a peer-reviewed journal.

4. (seymour2024microbialmechanismsof pages 12-13): Brenda J. Seymour, Brendan E. Allen, and Kristine A. Kuhn. Microbial mechanisms of rheumatoid arthritis pathogenesis. Current rheumatology reports, 26:124-132, Feb 2024. URL: https://doi.org/10.1007/s11926-024-01135-y, doi:10.1007/s11926-024-01135-y. This article has 14 citations and is from a peer-reviewed journal.

5. (ghang2025currentstateand pages 1-3): Byeongzu Ghang, Jin Kyun Park, Ji Hyeon Ju, and Seungwoo Han. Current state and future directions of basic research in rheumatoid arthritis. Journal of Rheumatic Diseases, 32:166-181, Feb 2025. URL: https://doi.org/10.4078/jrd.2024.0151, doi:10.4078/jrd.2024.0151. This article has 1 citations.

6. (barbera2025theroleof pages 7-11): L LA BARBERA. The role of jak/stat inhibition in modulating the innate immune response in patients with rheumatoid arthritis. Unknown journal, 2025.

7. (perera2024clinicalphenotypesserological pages 20-21): James Perera, Chiara Aurora Delrosso, Alessandra Nerviani, and Costantino Pitzalis. Clinical phenotypes, serological biomarkers, and synovial features defining seropositive and seronegative rheumatoid arthritis: a literature review. Cells, 13:743, Apr 2024. URL: https://doi.org/10.3390/cells13090743, doi:10.3390/cells13090743. This article has 33 citations and is from a poor quality or predatory journal.