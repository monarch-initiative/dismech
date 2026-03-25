---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T14:03:02.297787'
end_time: '2026-01-31T14:12:11.134854'
duration_seconds: 548.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Psoriatic Arthritis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Psoriatic Arthritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Psoriatic Arthritis**.
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
- **Disease Name:** Psoriatic Arthritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Psoriatic Arthritis**.
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


Plan (updated as executed)
- Objective 1: Identify recent (2023–2024) authoritative sources focused on PsA mechanisms. Status: completed. Key sources include McGonagle 2024 (GRAPPA debate on enthesitis), Raychaudhuri 2024 (JAK/STAT in SpA), Dilek 2025 (systematic review of cytokine pathways), Biedroń 2023 (DKK1 and bone remodeling), and synthesis of recent genetics (Allard‑Chamard & Rahman 2026). (mcgonagle2024grappa2023debate pages 1-2, raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11, allardchamard2025exploringthegenetic pages 7-9)
- Objective 2: Extract core mechanisms (IL‑23/IL‑17, synovio‑entheseal complex, bone remodeling; JAK/STAT, TNF, IFN; microbiome; genetics). Status: completed. (mcgonagle2024grappa2023debate pages 1-2, raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11, allardchamard2025exploringthegenetic pages 7-9, bonomo2025recentadvancesin pages 5-7, bonomo2025recentadvancesin pages 4-5)
- Objective 3: Map key molecular players, cell types, anatomical sites, and chemicals with ontology-ready annotations. Status: completed (see embedded artifact). (allardchamard2025exploringthegenetic pages 7-9, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11, raychaudhuri2024jakstatsignalingand pages 1-3, mcgonagle2024grappa2023debate pages 1-2)
- Objective 4: Annotate biological processes and cellular components. Status: completed. (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- Objective 5: Synthesize disease progression and phenotype links. Status: completed. (mcgonagle2024grappa2023debate pages 1-2, dilek2025immuneresponseand pages 10-11, dilek2025immuneresponseand pages 1-2)
- Objective 6: Create a compact artifact table with ontology IDs and evidence. Status: completed (embedded below). (all cited)
- Objective 7/8: Write and submit the comprehensive research report. Status: completed (this document).

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Psoriatic Arthritis (PsA)
- Category: Complex

Pathophysiology description (narrative synthesis)
Psoriatic arthritis is an immune‑mediated inflammatory disease in which enthesis‑resident and synovial immune–stromal circuits converge, driven principally by the IL‑23/IL‑17 axis and amplified by TNF and other cytokines, producing synovitis, enthesitis, dactylitis, osteitis, and a paradoxical combination of bone erosion and new bone formation. Contemporary models emphasize the synovio‑entheseal complex: mechanical microdamage at entheses triggers innate and innate‑like lymphoid responses that can spill into adjacent synovium and nail–DIP units; imaging and anatomical studies support enthesitis as a primary lesion that may predate clinical arthritis and explain nail–DIP co‑localization. Therapeutically validated pathways (IL‑17/IL‑23, TNF, and JAK/TYK2) mirror these mechanisms. Genetic susceptibility implicates HLA class I and antigen processing/presentation (HLA‑B27, ERAP1/2) alongside IL‑23/Th17 and interferon/JAK signaling genes (IL23R, IL12B, TYK2, TRAF3IP2), aligning with observed cell‑type programs (Th17/Tc17, γδ T cells, MAIT, ILC3, dendritic cells including pDCs) and tissue remodeling pathways (RANKL‑osteoclastogenesis; Wnt inhibitors DKK1/SOST shaping new bone). (mcgonagle2024grappa2023debate pages 1-2, dilek2025immuneresponseand pages 1-2, raychaudhuri2024jakstatsignalingand pages 1-3, allardchamard2025exploringthegenetic pages 7-9, dilek2025immuneresponseand pages 10-11)

Direct quotes supporting key concepts
- “The enthesitis hypothesis posits that enthesitis is a primary lesion and that inflammation at the enthesis initiates the musculoskeletal symptoms of psoriatic arthritis (PsA) and spondyloarthropathies (SpA).” URL/Date: The Journal of Rheumatology, Aug 2024, doi:10.3899/jrheum.2024-0593 (mcgonagle2024grappa2023debate pages 1-2)
- JAK/STAT is emphasized as “a key regulatory role” for cytokines relevant to SpA pathogenesis with therapeutic implications for JAK/TYK2 inhibition. URL/Date: Current Rheumatology Reports, Mar 2024, doi:10.1007/s11926-024-01144-x (raychaudhuri2024jakstatsignalingand pages 1-3)

1) Core pathophysiology
- Primary mechanisms: Enthesis‑driven inflammation within the synovio‑entheseal complex; cytokine circuits dominated by IL‑23→STAT3/TYK2/JAK2 signaling sustaining Th17/innate‑like IL‑17 production; IL‑17/TNF acting on stromal cells to induce chemokines/MMPs and maintain synovitis; bone pathways coupling inflammation to osteoclastogenesis (RANKL) and osteoproliferation (Wnt/DKK1/SOST axis). (mcgonagle2024grappa2023debate pages 1-2, raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- Dysregulated molecular pathways: IL‑23/IL‑17 and TNF signaling; JAK/STAT (notably TYK2/JAK2 with IL‑23); interferon/type I IFN networks (pDC‑linked); Wnt antagonism via DKK1/SOST; RANK–RANKL–OPG axis. (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- Affected cellular processes: Cytokine receptor signaling; NF‑κB activation; matrix remodeling (MMP induction); osteoclast differentiation and osteoblast/Wnt regulation; antigen processing/presentation (HLA class I–ERAP). (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, allardchamard2025exploringthegenetic pages 7-9)

2) Key molecular players
- Genes/Proteins (HGNC): HLA‑B27; ERAP1/ERAP2; IL23R; IL12B; TYK2; TRAF3IP2 (Act1); DKK1; RANKL/TNFSF11; SOST. Evidence: recent genetics aggregations and mechanistic reviews place IL‑23/Th17 and antigen‑processing genes among top signals; TRAF3IP2 encodes the IL‑17 signaling adaptor Act1; bone regulators DKK1/SOST vary with inflammatory signaling. URLs/Years: J Rheumatol 2024/2026; Arch Rheumatol 2025; Rheumatol Int 2023. (allardchamard2025exploringthegenetic pages 7-9, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- Chemical entities: Small‑molecule JAK inhibitors and selective TYK2 inhibitors modulate the implicated cytokine circuits; anti‑IL‑17A/F, anti‑IL‑23p19, anti‑IL‑12/23p40, and anti‑TNF biologics validate the central axes. Current reviews outline mechanisms and therapeutic classes. (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2)
- Cell Types (CL): Th17/Tc17; γδ T cells; MAIT; ILC3; dendritic cells (including pDCs); synovial fibroblasts; osteoclasts/osteoblasts; macrophages, neutrophils, mast cells. These cells produce or respond to IL‑23/IL‑17/TNF, coordinate innate‑adaptive crosstalk, and drive tissue changes. (dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11, raychaudhuri2024jakstatsignalingand pages 1-3)
- Anatomical locations (UBERON): Enthesis; synovium; nail–DIP unit; sacroiliac joint/spine. The nail–DIP anatomical linkage explains frequent co‑localization of nail disease and DIP arthritis in PsA. (mcgonagle2024grappa2023debate pages 1-2)

3) Biological processes (GO terms; disrupted in PsA)
- IL‑23 signaling and Th17 differentiation/effector function (GO:0032622; GO:0072538); IL‑17‑mediated signaling (GO:0032612); JAK/STAT cascade (GO:0007259); TNF signaling via NF‑κB (GO:0033209); type I interferon signaling pathway (GO:0060337); antigen processing and presentation of endogenous peptide antigen via MHC class I (GO:0002474); osteoclast differentiation (GO:0030316); Wnt signaling pathway and negative regulation by DKK1/SOST (GO:0016055; GO:0030178). Mechanistic and therapy literature support these as central. (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, allardchamard2025exploringthegenetic pages 7-9)

4) Cellular components
- Plasma membrane cytokine receptors (IL‑23R, IL‑17R, TNFR); cytoplasmic JAK/TYK/STAT signalosomes; nucleus (STAT‑dependent transcription); endoplasmic reticulum (ERAP1/2 peptide trimming); extracellular space (cytokines; DKK1/SOST; RANKL). (raychaudhuri2024jakstatsignalingand pages 1-3, allardchamard2025exploringthegenetic pages 7-9)

5) Disease progression (sequence of events)
- Initiation: Genetic susceptibility (HLA‑B27; ERAP1/2; IL23R, IL12B, TYK2; TRAF3IP2) primes immune circuits. Mechanical microdamage at entheses and local innate sensing recruit myeloid/DC populations and innate‑like lymphocytes. (allardchamard2025exploringthegenetic pages 7-9, mcgonagle2024grappa2023debate pages 1-2)
- Propagation: IL‑23 from myeloid cells sustains Th17/innate‑like IL‑17 producers (γδ T, MAIT, ILC3). IL‑17/TNF drive stromal activation (synovial fibroblasts), chemokine/MMP production, and recruitment of neutrophils/macrophages, culminating in synovitis and enthesitis. (dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- Structural change: RANKL‑driven osteoclastogenesis (erosion) occurs alongside Wnt pathway modulation by DKK1/SOST, enabling paradoxical osteoproliferation (enthesophytes, periosteal new bone). (dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- Spread and phenotypes: Nail unit inflammation spreads to the adjacent DIP enthesis/synovium; axial structures (sacroiliac/spine entheses) may be involved in axPsA. (mcgonagle2024grappa2023debate pages 1-2)

6) Phenotypic manifestations (with links to mechanisms)
- Enthesitis (HP:0100715): Arises at mechanically stressed insertions, dominated by IL‑23/IL‑17 and innate‑like lymphocytes; central in PsA. (mcgonagle2024grappa2023debate pages 1-2, dilek2025immuneresponseand pages 10-11)
- Dactylitis (HP:0005905): Represents a digit‑wide enthesitis/tenosynovitis composite; micro‑enthesis inflammation along pulleys contributes. (dilek2025immuneresponseand pages 10-11)
- Synovitis (HP:0004315): Cytokine‑driven stromal and leukocyte activation within synovial tissue. (dilek2025immuneresponseand pages 1-2)
- Axial disease/sacroiliitis (HP:0002826): Inflammation at spinal/sacroiliac entheses; response patterns reflect IL‑17/JAK axes. (mcgonagle2024grappa2023debate pages 1-2, raychaudhuri2024jakstatsignalingand pages 1-3)
- Bone remodeling (erosion and new bone): RANKL induction and Wnt antagonism integrate inflammatory signaling with structural change. (dilek2025immuneresponseand pages 1-2)

7) Recent developments and latest research (2023–2024 priority)
- Enthesitis‑first paradigm and synovio‑entheseal complex reinforced with clinical imaging and anatomical evidence; nail–DIP linkage and cytokine validation (IL‑17/IL‑23/TNF) emphasized in the 2024 GRAPPA debate summary (The Journal of Rheumatology, Aug 2024; DOI above). (mcgonagle2024grappa2023debate pages 1-2)
- JAK/STAT and TYK2: 2024 reviews synthesize how IL‑23 and other cytokines signal through JAK2/TYK2/STAT3, aligning with clinical success of JAK/TYK2 inhibitors and next‑generation intracellular targets. (raychaudhuri2024jakstatsignalingand pages 1-3)
- Cytokine network integration: Systematic review (2025, includes studies through 2024) details IL‑23/IL‑17, TNF, and their roles in osteoclastogenesis and new bone formation via DKK1/Wnt. (dilek2025immuneresponseand pages 1-2)
- Bone remodeling biomarkers: 2023 review highlights variability of circulating DKK1 in PsA and calls for standardized methodologies—underscoring complexity of the inflammatory‑osteogenic axis. (dilek2025immuneresponseand pages 10-11)
- Genetics (synthesis through 2025/2026): Aggregated genomic data implicate IL23R, IL12B, TYK2, TRAF3IP2, ERAP1/2, and HLA class I; enrichment of innate, antigen presentation, Th17, and interferon pathways highlight disease‑relevant biology and drug targetability. (allardchamard2025exploringthegenetic pages 7-9)

8) Current applications and real‑world implementations
- Biologics targeting IL‑17A/F, IL‑23p19, IL‑12/23p40, and TNF are standard of care and mechanistically validate the dominant cytokine axes; JAK1‑selective and TYK2‑targeted therapies offer oral options that modulate IL‑23 family and interferon signaling. (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2)
- Clinical anatomy–guided care: Recognition of nail–DIP–enthesis linkage supports targeted assessment and therapeutic choice in DIP arthritis with nail psoriasis. (mcgonagle2024grappa2023debate pages 1-2)
- Bone outcomes: Understanding of DKK1/SOST/Wnt balance informs interpretation of imaging and bone outcomes under anti‑TNF or anti‑IL‑17/23 therapy. (dilek2025immuneresponseand pages 10-11, dilek2025immuneresponseand pages 1-2)

9) Expert opinions and analysis (authoritative sources)
- GRAPPA 2023 debate (published 2024) synthesizes two decades of enthesitis research, concluding that enthesis anatomy and imaging data strongly support a primary enthesitis model with cytokine drivers that are therapeutically tractable. (mcgonagle2024grappa2023debate pages 1-2)
- Mechanistic rheumatology reviews (2024) argue for JAK/STAT as a unifying intracellular hub across multiple PsA‑relevant cytokines, motivating selective JAK/TYK2 inhibitor development to balance efficacy and safety. (raychaudhuri2024jakstatsignalingand pages 1-3)

10) Relevant statistics and data
- Genetics synthesis: Non‑MHC variants account for a substantial proportion of psoriatic disease risk, with multiple protein‑altering signals in IL23R/TRAF3IP2/TYK2/IL12B and others; enrichment across innate, antigen presentation, Th17, and interferon pathways (quantitative counts provided in source review). (allardchamard2025exploringthegenetic pages 7-9)
- Bone marker variability: Among 8 original studies, DKK1 serum levels in PsA were reported higher in 4, comparable in 1, and lower in 2 (reviewed up to Aug 2023), underscoring heterogeneity of bone pathway readouts. (dilek2025immuneresponseand pages 10-11)

Ontology‑ready annotations and evidence table
|Entity Type|Name (ontology)|Role / Mechanism in PsA (1–2 sentences)|Phenotype link (HP)|Evidence|Source DOI / URL|
|---|---|---|---|---|---|
|Gene / Protein|HLA-B27 (HGNC:HLA-B)|MHC class I allele associated with PsA susceptibility and axial/enthesitic phenotypes; influences peptide presentation and interacts with ERAP-mediated peptide trimming to modulate inflammation.|Enthesitis; axial disease (HP:0002826)| (allardchamard2025exploringthegenetic pages 7-9, mcgonagle2024grappa2023debate pages 1-2)|doi:10.3899/jrheum.2025-0273; https://doi.org/10.3899/jrheum.2024-0593|
|Gene / Protein|ERAP1/ERAP2 (HGNC:ERAP1 / ERAP2)|Endoplasmic reticulum aminopeptidases that trim peptides for HLA class I presentation; genetic variants modify antigen repertoire and PsA risk.|Immune dysregulation leading to arthritis| (allardchamard2025exploringthegenetic pages 7-9, gupta2025genomewidemetaanalysisand pages 21-24)|doi:10.3899/jrheum.2025-0273; https://doi.org/10.1101/2025.08.26.25334362|
|Gene / Protein|IL23R (HGNC:IL23R)|Receptor for IL-23 that stabilizes/expands Th17 cells via STAT3 signaling, driving IL-17 production and tissue inflammation.|Synovitis, enthesitis, skin lesions| (allardchamard2025exploringthegenetic pages 7-9, dilek2025immuneresponseand pages 1-2)|doi:10.3899/jrheum.2025-0273; doi:10.46497/archrheumatol.2025.10934|
|Gene / Protein|IL12B (HGNC:IL12B)|Encodes p40 subunit shared by IL-12 and IL-23; genetic variation affects IL-23–Th17 axis activity and therapeutic targeting (anti-p40 biologics).|Psoriasis with risk of PsA progression| (allardchamard2025exploringthegenetic pages 7-9, gupta2025genomewidemetaanalysisand pages 21-24)|doi:10.3899/jrheum.2025-0273; https://doi.org/10.1101/2025.08.26.25334362|
|Gene / Protein|TYK2 (HGNC:TYK2)|Janus-family kinase involved in IL-23/Type I IFN signaling; genetic/functional modulation influences Th17/IFN pathways and is a therapeutic target (TYK2 inhibitors).|Modulates systemic inflammation and IL-23–driven pathology| (allardchamard2025exploringthegenetic pages 7-9, raychaudhuri2024jakstatsignalingand pages 1-3)|doi:10.3899/jrheum.2025-0273; doi:10.1007/s11926-024-01144-x|
|Gene / Protein|TRAF3IP2 (HGNC:TRAF3IP2)|Adapter protein (Act1) in IL-17 receptor signaling; variants associate with PsA and amplify IL-17–mediated inflammatory cascades in skin and joint tissues.|Enhanced IL-17 responses; synovitis| (allardchamard2025exploringthegenetic pages 7-9)|doi:10.3899/jrheum.2025-0273|
|Gene / Protein|DKK1 (HGNC:DKK1)|Wnt pathway antagonist regulating bone formation; altered DKK1 levels in PsA link inflammatory cytokines (TNF/IL-17) to dysregulated osteogenesis and erosion/new bone formation.|Bone remodeling imbalance; osteoproliferation| (dilek2025immuneresponseand pages 1-2)|doi:10.46497/archrheumatol.2025.10934|
|Gene / Protein|RANKL / TNFSF11 (HGNC:TNFSF11)|Key osteoclast differentiation factor induced by inflammatory cytokines (IL-17, TNF), mediating bone resorption in erosive PsA.|Bone erosion (HP:0003009)| (dilek2025immuneresponseand pages 1-2)|doi:10.46497/archrheumatol.2025.10934|
|Gene / Protein|SOST (HGNC:SOST)|Sclerostin, Wnt pathway inhibitor produced by osteocytes; inflammation can alter SOST/DKK1 balance contributing to paradoxical bone loss and formation in SpA/PsA.|Altered bone density/formation| (dilek2025immuneresponseand pages 1-2)|doi:10.46497/archrheumatol.2025.10934|
|Cell Type|Th17 cell (CL:Th17)|Adaptive CD4+ subset driven by IL-23/STAT3/RORγt that secretes IL-17A/F and IL-22, promoting synovial inflammation, MMP production, and osteoclastogenesis.|Synovitis, enthesitis, bone damage| (dilek2025immuneresponseand pages 1-2, bonomo2025recentadvancesin pages 5-7)|doi:10.46497/archrheumatol.2025.10934; https://doi.org/10.3390/nu17081323|
|Cell Type|Innate-like IL-17 sources (γδ T cells, MAIT, ILC3) (CL:gamma-delta / CL:MAIT / CL:ILC3)|Tissue-resident or mucosa-derived cells that rapidly produce IL-17 in response to IL-23/IL-1β and mechanical triggers, linking mucosal/gut signals to joint inflammation.|Rapid local IL-17 release; enthesitis/dactylitis| (dilek2025immuneresponseand pages 10-11, bonomo2025recentadvancesin pages 5-7)|doi:10.46497/archrheumatol.2025.10934; https://doi.org/10.3390/nu17081323|
|Cell Type|Plasmacytoid dendritic cell (pDC) (CL:pDC)|Major source of type I IFNs; pDC activation and IFN signatures can modulate TNF/IL-23 axes and affect treatment responses and local immune priming.|IFN-associated inflammation; therapy-refractory signatures| (bonomo2025recentadvancesin pages 4-5, dilek2025immuneresponseand pages 1-2)|https://doi.org/10.3390/nu17081323; doi:10.46497/archrheumatol.2025.10934|
|Cell Type|Synovial fibroblast (CL:synovial fibroblast)|Stromal effector cells that respond to IL-17/TNF by producing cytokines, chemokines and MMPs, sustaining synovial pannus, leukocyte recruitment and tissue destruction.|Chronic synovitis and cartilage damage| (bonomo2025recentadvancesin pages 4-5, dilek2025immuneresponseand pages 10-11)|https://doi.org/10.3390/nu17081323; doi:10.46497/archrheumatol.2025.10934|
|Cell Type|Osteoclast / Osteoblast (CL:osteoclast / CL:osteoblast)|Osteoclasts (RANKL-driven) mediate bone erosion; osteoblasts and Wnt inhibitors (DKK1/SOST) control reparative/new bone formation, producing the mixed bone phenotype in PsA.|Bone erosion and osteoproliferation| (dilek2025immuneresponseand pages 1-2, bonomo2025recentadvancesin pages 5-7)|doi:10.46497/archrheumatol.2025.10934; https://doi.org/10.3390/nu17081323|
|Cell Type|Innate myeloid cells (macrophage, neutrophil, mast cell)|Provide IL-1, TNF, IL-6 and extrafollicular IL-17 (e.g., from neutrophil NETs/mast cells), amplifying local inflammation and matrix degradation.|Synovitis, enthesitis, neutrophil-driven flares| (bonomo2025recentadvancesin pages 5-7, dilek2025immuneresponseand pages 1-2)|https://doi.org/10.3390/nu17081323; doi:10.46497/archrheumatol.2025.10934|
|Anatomical Site|Enthesis (UBERON:enthesis)|Site of tendon/ligament insertion with specialized microanatomy; microdamage/mechanical stress triggers local innate immunity and IL-23/IL-17–mediated enthesitis that can extend to synovium (synovio-entheseal complex).|Enthesitis (HP:0100715), dactylitis (HP:0005905)| (mcgonagle2024grappa2023debate pages 1-2, dilek2025immuneresponseand pages 10-11)|doi:10.3899/jrheum.2024-0593; doi:10.46497/archrheumatol.2025.10934|
|Anatomical Site|Synovium (UBERON:synovium)|Primary site of inflammatory pannus formation; cytokine-rich synovium contains infiltrating Th17/innate cells and activated fibroblasts driving joint symptoms.|Synovitis (HP:0004315)| (dilek2025immuneresponseand pages 10-11, bonomo2025recentadvancesin pages 4-5)|doi:10.46497/archrheumatol.2025.10934; https://doi.org/10.3390/nu17081323|
|Anatomical Site|Nail–DIP unit (anatomical link)|Anatomical continuity between nail matrix and distal interphalangeal (DIP) enthesis explains frequent co-occurrence of nail disease and DIP joint involvement in PsA.|DIP arthritis; nail changes preceding PsA| (mcgonagle2024grappa2023debate pages 1-2, bonomo2025recentadvancesin pages 4-5)|doi:10.3899/jrheum.2024-0593; https://doi.org/10.3390/nu17081323|
|Anatomical Site|Sacroiliac joint (UBERON:sacroiliac joint)|Axial manifestations of PsA (axial PsA) involve sacroiliac/spinal entheses and may show distinct genetics/therapy responses from AS.|Axial disease; sacroiliitis| (mcgonagle2024grappa2023debate pages 1-2, bonomo2025recentadvancesin pages 4-5)|doi:10.3899/jrheum.2024-0593; https://doi.org/10.3390/nu17081323|
|Pathway / Process|IL-23 / IL-17 signaling (GO:0032622) & JAK/STAT (GO:0007259)|IL-23 stabilizes Th17 cells (STAT3/TYK2/JAK2-mediated); IL-17 acts on stromal cells to induce NF-κB/MMPs; JAK/STAT signaling integrates multiple cytokine inputs and is a therapeutic axis (JAK/TYK2 inhibitors).|Drives Th17-mediated synovitis, enthesitis; therapeutic target| (dilek2025immuneresponseand pages 1-2, raychaudhuri2024jakstatsignalingand pages 1-3, bonomo2025recentadvancesin pages 5-7)|doi:10.46497/archrheumatol.2025.10934; doi:10.1007/s11926-024-01144-x; https://doi.org/10.3390/nu17081323|
|Chemical / Drug (Therapy)|JAK / TYK2 inhibition (e.g., JAKi, TYK2 inhibitors)|Small-molecule inhibitors that blunt JAK-mediated cytokine signaling (including IL-23/IL-12 family effects via TYK2) and reduce both skin and joint inflammation; emerging data support efficacy in PsA and enthesitis.|Therapeutic modulation of synovitis/enthesitis| (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2)|doi:10.1007/s11926-024-01144-x; doi:10.46497/archrheumatol.2025.10934|


*Table: A compact ontology-ready table summarizing genes/proteins, cells, anatomical sites, pathways and therapies implicated in psoriatic arthritis pathophysiology, with concise mechanisms, phenotype links (HP terms) and evidence citations to the gathered sources for knowledge‑base integration.*

Evidence items (with URLs/dates when available)
- McGonagle D, Abacar K, Kirkham B. GRAPPA 2023 Debate: Is Psoriatic Disease Really a Primary Enthesitis… The Journal of Rheumatology. Aug 2024. doi:10.3899/jrheum.2024-0593 (mcgonagle2024grappa2023debate pages 1-2)
- Raychaudhuri SP, Shah RJ, Banerjee S, Raychaudhuri SK. JAK-STAT Signaling and Beyond in the Pathogenesis of Spondyloarthritis… Current Rheumatology Reports. Mar 2024. doi:10.1007/s11926-024-01144-x (raychaudhuri2024jakstatsignalingand pages 1-3)
- Dilek G, Unan MK, Nas K. Immune response and cytokine pathways in psoriatic arthritis: A systematic review. Archives of Rheumatology. Mar 2025. doi:10.46497/archrheumatol.2025.10934 (dilek2025immuneresponseand pages 1-2) (dilek2025immuneresponseand pages 10-11)
- Biedroń G, et al. Serum concentration of DKK1 in psoriatic arthritis. Rheumatology International. Sep 2023. doi:10.1007/s00296-023-05452-w (dilek2025immuneresponseand pages 10-11)
- Allard‑Chamard H, Rahman P. Exploring the genetic landscape of PsA: A narrative review. The Journal of Rheumatology. Aug 2026. doi:10.3899/jrheum.2025-0273 (genetics synthesis spanning up to 2025). (allardchamard2025exploringthegenetic pages 7-9)
- Additional mechanistic overviews on microbiome/innate–adaptive crosstalk used cautiously (Nutrients 2025 narrative review) to contextualize IL‑23/JAK/STAT and cell‑type roles. Apr 2025. doi:10.3390/nu17081323 (bonomo2025recentadvancesin pages 5-7, bonomo2025recentadvancesin pages 4-5)

Gene/protein, cell, and phenotype annotations for knowledge base integration
- HGNC: HLA‑B; ERAP1; ERAP2; IL23R; IL12B; TYK2; TRAF3IP2; DKK1; TNFSF11 (RANKL); SOST. (allardchamard2025exploringthegenetic pages 7-9, dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- CL: Th17 cell; γδ T cell; MAIT cell; ILC3; plasmacytoid dendritic cell; synovial fibroblast; osteoclast; osteoblast; macrophage; neutrophil; mast cell. (dilek2025immuneresponseand pages 1-2, dilek2025immuneresponseand pages 10-11)
- UBERON: Enthesis; Synovium; Distal interphalangeal joint/nail unit; Sacroiliac joint. (mcgonagle2024grappa2023debate pages 1-2)
- GO (selected): IL‑23 signaling/Th17 differentiation (GO:0032622/GO:0072538); IL‑17 signaling (GO:0032612); JAK/STAT (GO:0007259); TNF→NF‑κB (GO:0033209); type I IFN signaling (GO:0060337); antigen processing MHC I (GO:0002474); osteoclast differentiation (GO:0030316); Wnt signaling regulation (GO:0016055/GO:0030178). (raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 1-2, allardchamard2025exploringthegenetic pages 7-9)
- HP: Enthesitis (HP:0100715); Dactylitis (HP:0005905); Synovitis (HP:0004315); Axial disease/sacroiliitis (HP:0002826); Bone erosion (HP:0003009). (mcgonagle2024grappa2023debate pages 1-2, dilek2025immuneresponseand pages 10-11, dilek2025immuneresponseand pages 1-2)

Conclusions
PsA pathophysiology is best conceptualized as an enthesis‑initiated, cytokine‑amplified process integrated through JAK/STAT signal transduction and sculpted by genetic variation in antigen presentation and IL‑23/Th17 pathways. This framework explains clinical phenotypes (enthesitis, dactylitis, axial disease), nail–DIP co‑involvement, and bone remodeling paradoxes, and it underpins current targeted therapies (anti‑IL‑17/23/TNF; JAK/TYK2 inhibitors). Future refinement will benefit from standardized bone biomarker assessment (e.g., DKK1), deeper resolution of cell states across the synovio‑entheseal complex, and genetics‑informed patient stratification. (mcgonagle2024grappa2023debate pages 1-2, raychaudhuri2024jakstatsignalingand pages 1-3, dilek2025immuneresponseand pages 10-11, dilek2025immuneresponseand pages 1-2, allardchamard2025exploringthegenetic pages 7-9)

References

1. (mcgonagle2024grappa2023debate pages 1-2): Dennis McGonagle, Kerem Abacar, and Bruce Kirkham. Grappa 2023 debate: is psoriatic disease really a primary enthesitis that drives joint synovitis? the enthesitis hypothesis 25 years on. The Journal of rheumatology, 51:101-105, Aug 2024. URL: https://doi.org/10.3899/jrheum.2024-0593, doi:10.3899/jrheum.2024-0593. This article has 5 citations.

2. (raychaudhuri2024jakstatsignalingand pages 1-3): Siba P. Raychaudhuri, Ruchi J. Shah, Sneha Banerjee, and Smriti K. Raychaudhuri. Jak-stat signaling and beyond in the pathogenesis of spondyloarthritis and their clinical significance. Current Rheumatology Reports, 26:204-213, Mar 2024. URL: https://doi.org/10.1007/s11926-024-01144-x, doi:10.1007/s11926-024-01144-x. This article has 17 citations and is from a peer-reviewed journal.

3. (dilek2025immuneresponseand pages 1-2): Gamze Dilek, Mehtap Kalcik Unan, and Kemal Nas. Immune response and cytokine pathways in psoriatic arthritis: a systematic review. Archives of Rheumatology, 40:144-156, Mar 2025. URL: https://doi.org/10.46497/archrheumatol.2025.10934, doi:10.46497/archrheumatol.2025.10934. This article has 6 citations.

4. (dilek2025immuneresponseand pages 10-11): Gamze Dilek, Mehtap Kalcik Unan, and Kemal Nas. Immune response and cytokine pathways in psoriatic arthritis: a systematic review. Archives of Rheumatology, 40:144-156, Mar 2025. URL: https://doi.org/10.46497/archrheumatol.2025.10934, doi:10.46497/archrheumatol.2025.10934. This article has 6 citations.

5. (allardchamard2025exploringthegenetic pages 7-9): Hugues Allard-Chamard and Proton Rahman. Exploring the genetic landscape of psoriatic arthritis: a narrative review of recent genomic studies. The Journal of rheumatology, Aug 2026. URL: https://doi.org/10.3899/jrheum.2025-0273, doi:10.3899/jrheum.2025-0273. This article has 0 citations.

6. (bonomo2025recentadvancesin pages 5-7): Maria Grazia Bonomo, Salvatore D’Angelo, Valentina Picerno, Antonio Carriero, and Giovanni Salzano. Recent advances in gut microbiota in psoriatic arthritis. Nutrients, 17:1323, Apr 2025. URL: https://doi.org/10.3390/nu17081323, doi:10.3390/nu17081323. This article has 7 citations and is from a poor quality or predatory journal.

7. (bonomo2025recentadvancesin pages 4-5): Maria Grazia Bonomo, Salvatore D’Angelo, Valentina Picerno, Antonio Carriero, and Giovanni Salzano. Recent advances in gut microbiota in psoriatic arthritis. Nutrients, 17:1323, Apr 2025. URL: https://doi.org/10.3390/nu17081323, doi:10.3390/nu17081323. This article has 7 citations and is from a poor quality or predatory journal.

8. (gupta2025genomewidemetaanalysisand pages 21-24): Yask Gupta, Tatiana Sezin, and Diamant Thaçi. Genome-wide meta-analysis and integrative fine-mapping identify novel susceptibility loci and effector genes in psoriatic arthritis. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.26.25334362, doi:10.1101/2025.08.26.25334362. This article has 0 citations.