---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:51.421178'
end_time: '2025-12-18T09:54:33.296946'
duration_seconds: 521.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ankylosing Spondylitis
  mondo_id: ''
  category: Autoimmune
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
- **Disease Name:** Ankylosing Spondylitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ankylosing Spondylitis**.
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
- **Disease Name:** Ankylosing Spondylitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ankylosing Spondylitis**.
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
- Disease Name: Ankylosing Spondylitis (historical term within axial spondyloarthritis)
- MONDO ID: MONDO:0001020
- Category: Autoimmune/autoinflammatory MHC-I–opathy

Pathophysiology description (narrative)
Ankylosing spondylitis (AS) is a prototypic MHC class I–associated inflammatory disease in which genetic predisposition, barrier tissue biology (gut and enthesis), and cytokine networks converge to drive chronic axial inflammation and pathological bone remodeling. HLA-B27 is the strongest genetic association; proposed mechanisms include altered antigen presentation of arthritogenic peptides, intracellular misfolding with endoplasmic reticulum (ER) stress and unfolded protein response, and formation of heavy-chain homodimers that may impact innate and adaptive signaling (reviewed with structural features such as an unpaired Cys67, slow folding, and homodimerization propensity) (May 2024, https://doi.org/10.3390/ijms25116081) (nagit2024exploringthepathogenesis pages 2-4). Non-MHC antigen-processing aminopeptidases ERAP1 and ERAP2 modify the MHC-I peptide repertoire and act epistatically with HLA-B27, further shaping risk (May 2024, https://doi.org/10.3390/ijms25116081; May 2025, https://doi.org/10.3390/jcm14113677) (nagit2024exploringthepathogenesis pages 5-6, zormpa2025thegeneticbackground pages 1-2).

At the effector-cytokine level, an IL-23/IL-17 axis is central, but disease-relevant IL-17A/IL-17F can also be produced independently of IL-23 by innate-like lymphocytes (γδ T cells, MAIT cells, ILC3) resident at the enthesis and mucosa, helping explain why IL-23 blockade has underperformed in axSpA compared with direct IL-17 inhibition (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 10-11). The enthesis—the fibrocartilaginous attachment of tendon/ligament to bone—is a mechanically stressed barrier tissue populated by innate-like T cells capable of rapid IL-17 production; microdamage and mechanotransduction at the enthesis likely initiate or amplify inflammation (“enthesitis”) that extends to adjacent bone and synovium (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).

The gut–joint axis is strongly implicated: intestinal dysbiosis, barrier dysfunction, and translocation of microbial products can drive IL-23 production in the gut and mobilize α4β7+ ILC3/MAIT/γδ T cells to axial sites, where they elaborate IL-17/IL-22 (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7). Global genetics/meta-analyses reinforce a polygenic architecture that highlights IL23R and interleukin signaling beyond HLA-B27/ERAP1 (May 2025, https://doi.org/10.3390/jcm14113677) (zormpa2025thegeneticbackground pages 2-4, zormpa2025thegeneticbackground pages 1-2).

Downstream of inflammation, bone remodeling is uncoupled: inflammatory cytokines promote osteoclast activity and osteitis while, paradoxically, reparative programs and Wnt/BMP signaling (modulated by inhibitors such as DKK1 and sclerostin) foster new bone formation at entheseal sites, producing syndesmophytes and ankylosis (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2). Clinically, radiographic progression is quantified by the modified Stoke Ankylosing Spondylitis Spinal Score (mSASSS); biologics that target TNF and IL-17 improve symptoms and inflammation and may attenuate progression in selected subgroups, while JAK inhibitors suppress inflammatory signaling broadly with rapid symptomatic benefits (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318; May 2025, https://doi.org/10.3390/jcm14113677) (parvin2025decodingtheinflammatoryosteogenic pages 1-2, zormpa2025thegeneticbackground pages 2-4).

Key concepts and definitions with current understanding
- HLA-B27 mechanisms: arthritogenic peptide presentation; misfolded heavy chain–induced ER stress/UPR; cell-surface heavy-chain homodimers; each may contribute, not mutually exclusive (May 2024, https://doi.org/10.3390/ijms25116081) (nagit2024exploringthepathogenesis pages 2-4).
- IL-23/IL-17 axis: IL-23 drives Th17 and also activates innate-like lymphocytes; however, IL-17A/F can be generated IL-23-independently at entheseal sites, consistent with IL-17 but not IL-23 inhibitor efficacy in axSpA (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 10-11).
- Enthesis biology: a mechanically stressed barrier tissue with resident innate-like lymphocytes (γδ T, MAIT, ILC3); microdamage triggers cytokine cascades and osteo-inflammatory repair responses (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).
- Gut–joint axis: dysbiosis and barrier loss promote gut IL-23, trafficking of IL-17/IL-22–producing cells, and systemic immune activation (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).
- Bone remodeling: Wnt/BMP pathways regulate osteogenesis; DKK1 and sclerostin restrain Wnt signaling—dysregulation may enable syndesmophyte formation following inflammation (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Recent developments and latest research (2023–2024 priority)
- Genetics beyond HLA-B27: systematic analyses highlight ERAP1/2 and IL23R as consistent signals; IL interleukin pathway enrichment observed (May 2025, https://doi.org/10.3390/jcm14113677) (zormpa2025thegeneticbackground pages 2-4, zormpa2025thegeneticbackground pages 1-2).
- Structural/biophysical HLA-B27 insights: distinctive folding kinetics and homodimerization propensity provide mechanistic plausibility for misfolding and homodimer models (May 2024, https://doi.org/10.3390/ijms25116081) (nagit2024exploringthepathogenesis pages 2-4).
- IL-23–independent IL-17: recent reviews synthesize data on IL-17A/F production by MAIT and γδ T cells, supporting innate drivers at the enthesis and gut (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 10-11).
- Translational axis: updated syntheses connect gut dysbiosis, barrier dysfunction, IL-23/IL-17 circuits, and enthesis microtrauma to disease chronicity (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).

Current applications and real-world implementations
- TNF inhibitors: reduce inflammation and symptoms; several cohorts suggest attenuation of structural progression in certain spinal segments, though overall effects vary; they remain standard biologic therapy (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318; May 2025, https://doi.org/10.3390/jcm14113677) (parvin2025decodingtheinflammatoryosteogenic pages 1-2, zormpa2025thegeneticbackground pages 2-4).
- IL-17 inhibitors: consistently effective for pain, stiffness, and MRI inflammation, aligning with IL-17’s effector role in entheseal inflammation (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
- JAK inhibitors: target shared cytokine signaling nodes; reviews synthesize trial data supporting rapid pain relief and broad disease-activity improvements (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Expert opinions and analysis
- Reviews in 2024–2025 emphasize axSpA as an MHC-I–opathy integrating HLA-B27 biology with ERAP1/2 and IL-23/IL-17 signaling; the enthesis and gut are viewed as coupled barrier organs in pathogenesis (May 2024, https://doi.org/10.3390/ijms25116081; Nov 2024, https://doi.org/10.3390/cimb46110762) (nagit2024exploringthepathogenesis pages 2-4, pasaran2024anactualinsight pages 10-11). 
- Genetic overviews conclude that despite high heritability, individual loci beyond HLA-B27 have modest effects, arguing for pathway-level targeting (May 2025, https://doi.org/10.3390/jcm14113677) (zormpa2025thegeneticbackground pages 1-2).

Relevant statistics and data from recent studies
- HLA-B27 positivity: 74–95% of AS patients; yet only ~1–5% of HLA-B27 carriers develop AS (May 2024, https://doi.org/10.3390/ijms25116081; May 2025, https://doi.org/10.3390/jcm14113677) (nagit2024exploringthepathogenesis pages 2-4, zormpa2025thegeneticbackground pages 1-2).
- Genetic enrichment: 76 AS-associated SNPs curated, with immune regulation and interleukin signaling overrepresented; ERAP1 and IL23R highlighted as key genes (May 2025, https://doi.org/10.3390/jcm14113677) (zormpa2025thegeneticbackground pages 1-2).

Core Pathophysiology
Primary mechanisms
- Antigen processing/presentation via HLA-B27 and ERAP1/2 alters peptide repertoires and immune activation (May 2024, https://doi.org/10.3390/ijms25116081; May 2025, https://doi.org/10.3390/jcm14113677) (nagit2024exploringthepathogenesis pages 2-4, zormpa2025thegeneticbackground pages 1-2, nagit2024exploringthepathogenesis pages 5-6).
- Enthesitis and mechanotransduction: microinjury at the enthesis triggers IL-17–dominated responses from resident innate-like lymphocytes and stromal cells (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).
- Gut–joint axis: dysbiosis and barrier loss promote IL-23 production and trafficking of IL-17/IL-22–producing cells to axial sites (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).
- Bone remodeling: uncoupling of osteoclast-mediated resorption and Wnt/BMP-driven osteogenesis yields syndesmophytes and ankylosis (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Dysregulated molecular pathways
- IL-23/IL-17 axis (with IL-23–independent IL-17 from MAIT/γδ T/ILC3), TNF/NF-κB, MHC-I antigen processing, Wnt/BMP signaling in bone (Nov 2024, https://doi.org/10.3390/cimb46110762; May 2024, https://doi.org/10.3390/ijms25116081; Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (pasaran2024anactualinsight pages 10-11, nagit2024exploringthepathogenesis pages 2-4, parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Affected cellular processes
- Cytokine-driven innate/adaptive activation, mechanosensing and stromal activation at enthesis, osteo-immune crosstalk, and repair programs that favor aberrant ossification (Nov 2024, https://doi.org/10.3390/cimb46110762; Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (pasaran2024anactualinsight pages 5-7, parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Key Molecular Players (ontology-mapped)
| Category | Standard term | Role in AS pathophysiology | Key pathway(s) | Notes | Evidence |
|---|---|---|---|---|---|
| Gene/Protein | HLA-B (HLA-B*27 allele) | Major genetic risk factor; proposed to alter peptide presentation, misfold/fold into homodimers and induce ER stress that promotes inflammation. | MHC-I antigen presentation; ER stress/UPR; adaptive CD8+ T responses | Strong association with AS (high population odds; low penetrance); multiple mechanistic hypotheses (arthritogenic peptide, misfolding/homodimers). | (nagit2024exploringthepathogenesis pages 2-4, zormpa2025thegeneticbackground pages 2-4) |
| Gene/Protein | ERAP1 | Aminopeptidase trimming peptides for MHC-I; ERAP1 variants modulate HLA-B27 peptide repertoire and AS risk. | Antigen processing (MHC-I) | Second major genetic signal after HLA-B27; interaction with HLA-B27 and environmental factors noted. | (nagit2024exploringthepathogenesis pages 5-6, zormpa2025thegeneticbackground pages 2-4) |
| Gene/Protein | ERAP2 | Related aminopeptidase that influences peptide trimming and MHC-I presentation; variants implicated in AS susceptibility. | Antigen processing (MHC-I) | Often studied together with ERAP1; functional variation affects peptide pool. | (nagit2024exploringthepathogenesis pages 5-6, zormpa2025thegeneticbackground pages 2-4) |
| Gene/Protein | IL23R | Receptor for IL-23; variants alter Th17/IL-17 pathway activation and are associated with AS risk. | IL-23/IL-17 axis; Th17 differentiation | Multiple IL23R SNPs linked to AS in diverse populations; central to Th17-driven inflammation. | (nagit2024exploringthepathogenesis pages 5-6, zormpa2025thegeneticbackground pages 2-4) |
| Gene/Protein | IL12B | Encodes p40 subunit shared by IL-12/IL-23; genetic/functional links to cytokine-driven inflammation in AS. | IL-12/IL-23 signaling; Th1/Th17 balance | Identified in genetic/proteomic screens as relevant to interleukin signaling in AS. | (zormpa2025thegeneticbackground pages 2-4, parvin2025decodingtheinflammatoryosteogenic pages 1-2) |
| Gene/Protein | IL7R | Cytokine receptor implicated by plasma-protein/MR analyses; may influence lymphocyte survival and AS risk. | Lymphocyte development/survival; cytokine signaling | Emerging biomarker/therapeutic target from protein-level genetic analyses. | (zormpa2025thegeneticbackground pages 2-4, parvin2025decodingtheinflammatoryosteogenic pages 1-2) |
| Gene/Protein | DKK1 | Secreted Wnt inhibitor; modulates bone formation—altered activity proposed to influence pathological new bone in AS. | Wnt/β-catenin signaling; bone remodeling | Conflicting serum data; mechanistic role in uncoupling inflammation vs osteoproliferation under investigation. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 10-11) |
| Gene/Protein | SOST (sclerostin) | Osteocyte-derived inhibitor of Wnt signaling; decreased function may permit aberrant bone formation at entheses. | Wnt/BMP signaling; bone formation regulation | Target of interest in bone-remodeling studies; implicated in AS syndesmophyte formation hypotheses. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 10-11) |
| Chemical/Protein | TNF | Proinflammatory cytokine driving synovial/enthesis inflammation; target of effective biologic therapies. | TNF signaling; NF-κB activation; osteoclastogenesis (indirect) | TNF inhibitors reduce inflammation and symptoms; effects on radiographic progression variable but clinically meaningful. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 5-7) |
| Chemical/Protein | IL-17A / IL-17F | Effector cytokines produced by Th17 and innate-like lymphocytes that mediate tissue inflammation at entheses and spine. | IL-23/IL-17 axis (and IL-23–independent IL-17 production) | IL-17 blockade effective in AS; IL-17F/IL-17A may be produced independently of IL-23 by innate-like cells. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 5-7) |
| Cell type | Mucosal-associated invariant T cell (MAIT cell) | Innate-like T cell that can produce IL-17/IFN-γ; implicated in gut–joint trafficking and local enthesis inflammation. | IL-23/IL-17 axis; cytokine-driven innate responses | MAIT cells express IL-23R and respond to cytokines; link gut mucosa to systemic inflammation. | (pasaran2024anactualinsight pages 5-7, nagit2024exploringthepathogenesis pages 5-6) |
| Cell type | Gamma-delta T cell (γδ T cell) | Tissue-resident innate-like T cells that rapidly produce IL-17 at entheseal sites, sometimes IL-23-independent. | IL-17 production; innate immunity at barrier/enthesis | Identified in animal models and human enthesis studies as IL-17 sources driving enthesitis. | (pasaran2024anactualinsight pages 5-7, parvin2025decodingtheinflammatoryosteogenic pages 1-2) |
| Cell type | Innate lymphoid cell type 3 (ILC3) | Innate immune cells producing IL-17/IL-22 in gut and possibly trafficking to joints; connect microbiota to systemic immunity. | IL-23/IL-17/IL-22 signaling; gut–joint axis | Proposed mediators of gut-origin inflammation reaching entheses/spine. | (pasaran2024anactualinsight pages 5-7, nagit2024exploringthepathogenesis pages 5-6) |
| Cell type | Osteoblast | Bone-forming cell that mediates pathological new bone (syndesmophyte) formation when coupled with inflammatory cues and Wnt/BMP imbalance. | Wnt/BMP signaling; osteogenesis | Activated/biased differentiation implicated in ankylosis and syndesmophyte development. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 5-7) |
| Cell type | Osteoclast | Bone-resorbing cell driven by RANKL and inflammatory cytokines; contributes to early erosive phases and bone remodeling imbalance. | RANK/RANKL/OPG; TNF-driven osteoclastogenesis | Inflammation promotes osteoclast activity while Wnt inhibitors and reparative pathways drive new bone formation. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 5-7) |
| Tissue | Enthesis (attachment site) | Primary anatomical site of pathology in AS: microdamage/mechanical stress + innate immunity → enthesitis, osteitis and later new bone formation. | Mechanotransduction; local innate responses; IL-23/IL-17 signaling | Enthesis-resident innate-like cells (γδ T, MAIT) and stromal cells coordinate local inflammation and ossification. | (pasaran2024anactualinsight pages 5-7, parvin2025decodingtheinflammatoryosteogenic pages 1-2) |
| Tissue | Sacroiliac joint | Key axial site involved early in AS; sacroiliitis reflects the axial disease and links to clinical diagnosis and imaging-based staging. | Local inflammation, osteitis, bone remodeling | MRI-detected sacroiliitis used for early classification; site of enthesis-related pathology. | (pasaran2024anactualinsight pages 5-7, pasaran2024anactualinsight pages 10-11) |
| Tissue | Spine (vertebra) | Site of syndesmophyte formation and ankylosis driven by osteogenic programs coupled to chronic enthesis inflammation. | Wnt/BMP signaling; enthesis-driven osteogenesis | Radiographic progression of vertebrae measured by mSASSS correlates with functional decline. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 5-7) |
| Chemical (drug class) | Tumor necrosis factor inhibitor (TNFi) | Biologic class that neutralizes TNF, reducing inflammation, pain, and improving function; may slow radiographic progression in some cohorts. | TNF blockade; downstream reduction of NF-κB and inflammatory mediators | Widely used first-line biologic for AS; effect on structural progression debated but clinical benefit established. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, zormpa2025thegeneticbackground pages 25-27) |
| Chemical (drug class) | IL-17 inhibitor | Monoclonal antibodies blocking IL-17A (or IL-17A/F) that reduce enthesitis/spinal inflammation and improve outcomes in AS. | IL-17 pathway blockade | Effective for AS symptom control; highlights centrality of IL-17 as effector cytokine. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, zormpa2025thegeneticbackground pages 25-27) |
| Chemical (drug class) | JAK inhibitor | Small-molecule inhibitors (e.g., JAK1-selective) that block cytokine signaling downstream of multiple receptors, improving symptoms and MRI inflammation. | JAK–STAT signaling inhibition (broad cytokine effects) | Emerging/approved oral option showing rapid symptom relief; safety and long-term structural impact under active evaluation. | (parvin2025decodingtheinflammatoryosteogenic pages 1-2, zormpa2025thegeneticbackground pages 25-27) |


*Table: Table summarizing genes/proteins, cells, tissues, and therapeutic classes implicated in AS pathophysiology with concise roles, pathways, notes and supporting evidence (pqac IDs).*

Biological Processes (for GO annotation; examples with supporting evidence)
- Antigen processing and presentation of peptide antigen via MHC class I (GO:0002474): HLA-B27, ERAP1/2 (May 2024, https://doi.org/10.3390/ijms25116081) (nagit2024exploringthepathogenesis pages 2-4).
- Positive regulation of interleukin-17 production (GO:0032740) and Th17 cell differentiation (GO:0072538): IL23R pathway, innate-like producers (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 10-11, pasaran2024anactualinsight pages 5-7).
- Inflammatory response (GO:0006954) and NF-κB signaling (GO:0043123): TNF/IL-17 signaling (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
- Wnt signaling pathway (GO:0016055) and bone mineralization (GO:0030282): DKK1/SOST-modulated osteogenesis and syndesmophyte formation (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
- Response to mechanical stimulus (GO:0009612): enthesis mechanotransduction initiating enthesitis (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).

Cellular Components (examples)
- MHC class I protein complex (GO:0042612) and endoplasmic reticulum (GO:0005783): HLA-B27 peptide loading; ER stress (May 2024, https://doi.org/10.3390/ijms25116081) (nagit2024exploringthepathogenesis pages 2-4).
- Extracellular space (GO:0005615): cytokines (TNF, IL-17), Wnt inhibitors (DKK1, SOST) (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
- Enthesis extracellular matrix/fibrocartilage (tissue level; see UBERON:0007809): site of immune–stromal interactions (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).

Disease Progression (sequence of events)
1) Genetic susceptibility (HLA-B27±ERAP1/2, IL23R variants) sets an antigen-processing and cytokine-response milieu (May 2024, https://doi.org/10.3390/ijms25116081; May 2025, https://doi.org/10.3390/jcm14113677) (nagit2024exploringthepathogenesis pages 2-4, zormpa2025thegeneticbackground pages 1-2, nagit2024exploringthepathogenesis pages 5-6).
2) Environmental triggers (gut dysbiosis/barrier loss; mechanical stress at entheses) induce IL-23 production and entheseal microinflammation (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).
3) Innate-like lymphocytes (γδ T, MAIT, ILC3) and Th17 produce IL-17A/F (sometimes IL-23–independent) and TNF, sustaining enthesitis/osteitis (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 10-11, pasaran2024anactualinsight pages 5-7).
4) Repair programs at enthesis stroma activate Wnt/BMP osteogenic pathways, with relative deficiency of Wnt antagonists (DKK1, SOST) facilitating new bone formation (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
5) Chronic cycles yield syndesmophytes and ankylosis; progression captured by mSASSS and influenced by biologic therapies (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318; May 2025, https://doi.org/10.3390/jcm14113677) (parvin2025decodingtheinflammatoryosteogenic pages 1-2, zormpa2025thegeneticbackground pages 2-4).

Phenotypic Manifestations (HP terms; mechanistic links)
- Inflammatory back pain (HP:0003419) and stiffness linked to entheseal/spinal inflammation driven by IL-17/TNF (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
- Sacroiliitis (HP:0011904): hallmark axial involvement reflecting enthesis/osteitis at sacroiliac joints (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).
- Reduced spinal mobility/ankylosis (HP:0003408): downstream of new bone formation via Wnt/BMP programs (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
- Extra-musculoskeletal features (uveitis, psoriasis, IBD) consistent with barrier-tissue shared pathobiology and MHC-I–opathy spectrum (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).

Cell type involvement (CL terms; examples)
- CL:0001047 CD8-positive, alpha-beta T cell; CL:0000980 gamma-delta T cell; CL:0000938 Th17 cell; CL:0001054 mucosal-associated invariant T cell; CL:0001064 innate lymphoid cell (type 3) (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7, pasaran2024anactualinsight pages 10-11).

Anatomical locations (UBERON terms)
- UBERON:0007809 enthesis; UBERON:0006025 sacroiliac joint; UBERON:0002412 vertebra (Nov 2024, https://doi.org/10.3390/cimb46110762) (pasaran2024anactualinsight pages 5-7).

Chemical entities (CHEBI terms; classes/examples)
- CHEBI:27009 tumor necrosis factor; CHEBI:82164 interleukin-17A; CHEBI:133488 sclerostin (protein); CHEBI:81563 dickkopf-related protein 1; TNF/IL-17 biologics and JAK inhibitors as therapeutic classes (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Evidence items (with PMIDs/DOIs/URLs and publication dates)
- Nagit RE et al. Exploring the pathogenesis of spondylarthritis beyond HLA-B27 (May 2024, IJMS) DOI: 10.3390/ijms25116081; URL: https://doi.org/10.3390/ijms25116081 (nagit2024exploringthepathogenesis pages 2-4).
- Păsăran ED et al. An Actual Insight into the Pathogenic Pathways of AS (Nov 2024, Current Issues in Molecular Biology) DOI: 10.3390/cimb46110762; URL: https://doi.org/10.3390/cimb46110762 (pasaran2024anactualinsight pages 5-7, pasaran2024anactualinsight pages 10-11).
- Zormpa T et al. The Genetic Background of AS (May 2025, Journal of Clinical Medicine) DOI: 10.3390/jcm14113677; URL: https://doi.org/10.3390/jcm14113677 (zormpa2025thegeneticbackground pages 2-4, zormpa2025thegeneticbackground pages 1-2, zormpa2025thegeneticbackground pages 25-27).
- Parvin A et al. Decoding the inflammatory-osteogenic axis in AS (Sep 2025, Frontiers in Immunology) DOI: 10.3389/fimmu.2025.1633318; URL: https://doi.org/10.3389/fimmu.2025.1633318 (parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Direct quotes (selected)
- “HLA-B27… has distinctive structural features — an unpaired cysteine at position 67 enabling heavy-chain homodimers, capacity to bind unusually long peptides… slower heavy-chain folding and a tendency to unfold in the ER” (May 2024, IJMS) (nagit2024exploringthepathogenesis pages 2-4).
- “Elevated serum levels of IL-23 and IL-17 as well as IL-23R genetic polymorphism were found in AS patients.” (Nov 2024, Current Issues in Molecular Biology) (pasaran2024anactualinsight pages 10-11).
- “Functional enrichment revealed strong associations with immune regulation and interleukin signaling pathways… ERAP1 and IL23R emerged as key genes implicated in AS” (May 2025, J Clin Med) (zormpa2025thegeneticbackground pages 1-2).

Gene/protein annotations with ontology terms (examples)
- HLA-B (HGNC:4932; process: GO:0002474; component: GO:0042612; evidence: genetics/mechanism) (nagit2024exploringthepathogenesis pages 2-4).
- ERAP1 (HGNC:18168), ERAP2 (HGNC:18169): antigen processing (GO:0002474), ER localization (GO:0005783) (nagit2024exploringthepathogenesis pages 5-6).
- IL23R (HGNC:6000): Th17 differentiation (GO:0072538), positive regulation of IL-17 production (GO:0032740) (nagit2024exploringthepathogenesis pages 5-6).
- DKK1 (HGNC:2891), SOST (HGNC:11189): negative regulation of Wnt signaling (GO:0030178); bone mineralization (GO:0030282) (parvin2025decodingtheinflammatoryosteogenic pages 1-2).
- TNF (HGNC:11892), IL17A/IL17F (HGNC:5988/5986): inflammatory response (GO:0006954); NF-κB signaling (GO:0043123) (parvin2025decodingtheinflammatoryosteogenic pages 1-2, pasaran2024anactualinsight pages 10-11).

Phenotype associations (HP terms; examples)
- HP:0003419 inflammatory back pain; HP:0011904 sacroiliitis; HP:0003408 ankylosis; HP:0002745 uveitis (pasaran2024anactualinsight pages 5-7, parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Cell types (CL terms; examples)
- CL:0000980 γδ T cell; CL:0001054 MAIT cell; CL:0000938 Th17 cell; CL:0001064 ILC3; CL:0000120 osteoblast; CL:0000098 osteoclast (pasaran2024anactualinsight pages 5-7, pasaran2024anactualinsight pages 10-11, parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Anatomy (UBERON terms; examples)
- UBERON:0007809 enthesis; UBERON:0006025 sacroiliac joint; UBERON:0002412 vertebra (pasaran2024anactualinsight pages 5-7).

Chemicals (CHEBI terms; examples)
- CHEBI:27009 TNF; CHEBI:82164 IL-17A; CHEBI:81563 DKK1; CHEBI:133488 sclerostin (parvin2025decodingtheinflammatoryosteogenic pages 1-2).

Limitations and open questions
- The relative contributions of HLA-B27 mechanisms (peptide vs misfolding vs homodimers) likely vary by context and remain incompletely resolved (May 2024, IJMS) (nagit2024exploringthepathogenesis pages 2-4).
- Translationally, disentangling IL-23–dependent from IL-23–independent IL-17 circuits at human entheseal sites is ongoing; this bears on therapeutic targeting strategies (Nov 2024, Current Issues in Molecular Biology) (pasaran2024anactualinsight pages 10-11).

Summary
AS pathogenesis reflects a genetically primed, barrier-tissue–centric inflammatory disease driven by MHC-I antigen presentation (HLA-B27±ERAP1/2), an IL-17–dominated effector program variably dependent on IL-23, and mechanosensitive enthesis biology with gut crosstalk. The inflammatory–osteogenic axis culminates in ankylosis via Wnt/BMP-modulated bone formation. Current therapies (TNF, IL-17, JAK inhibitors) align with these mechanisms, improving outcomes and, in some settings, slowing structural progression (Sep 2025, https://doi.org/10.3389/fimmu.2025.1633318; May 2025, https://doi.org/10.3390/jcm14113677) (parvin2025decodingtheinflammatoryosteogenic pages 1-2, zormpa2025thegeneticbackground pages 2-4).

References

1. (nagit2024exploringthepathogenesis pages 2-4): Ruxandra-Elena Nagit, Elena Rezus, and Petru Cianga. Exploring the pathogenesis of spondylarthritis beyond hla-b27: a descriptive review. International Journal of Molecular Sciences, 25:6081, May 2024. URL: https://doi.org/10.3390/ijms25116081, doi:10.3390/ijms25116081. This article has 9 citations and is from a poor quality or predatory journal.

2. (nagit2024exploringthepathogenesis pages 5-6): Ruxandra-Elena Nagit, Elena Rezus, and Petru Cianga. Exploring the pathogenesis of spondylarthritis beyond hla-b27: a descriptive review. International Journal of Molecular Sciences, 25:6081, May 2024. URL: https://doi.org/10.3390/ijms25116081, doi:10.3390/ijms25116081. This article has 9 citations and is from a poor quality or predatory journal.

3. (zormpa2025thegeneticbackground pages 1-2): Theodora Zormpa, Trias Thireou, Apostolos Beloukas, Dimitrios Chaniotis, Rebecca Golfinopoulou, Dimitrios Vlachakis, Elias Eliopoulos, and Louis Papageorgiou. The genetic background of ankylosing spondylitis reveals a distinct overlap with autoimmune diseases: a systematic review. Journal of Clinical Medicine, 14:3677, May 2025. URL: https://doi.org/10.3390/jcm14113677, doi:10.3390/jcm14113677. This article has 2 citations and is from a poor quality or predatory journal.

4. (pasaran2024anactualinsight pages 10-11): Emilia-Daniela Păsăran, Andreea Elena Diaconu, Corina Oancea, Andra-Rodica Bălănescu, Sorina Maria Aurelian, and Corina Homentcovschi. An actual insight into the pathogenic pathways of ankylosing spondylitis. Current Issues in Molecular Biology, 46:12800-12812, Nov 2024. URL: https://doi.org/10.3390/cimb46110762, doi:10.3390/cimb46110762. This article has 8 citations and is from a poor quality or predatory journal.

5. (pasaran2024anactualinsight pages 5-7): Emilia-Daniela Păsăran, Andreea Elena Diaconu, Corina Oancea, Andra-Rodica Bălănescu, Sorina Maria Aurelian, and Corina Homentcovschi. An actual insight into the pathogenic pathways of ankylosing spondylitis. Current Issues in Molecular Biology, 46:12800-12812, Nov 2024. URL: https://doi.org/10.3390/cimb46110762, doi:10.3390/cimb46110762. This article has 8 citations and is from a poor quality or predatory journal.

6. (zormpa2025thegeneticbackground pages 2-4): Theodora Zormpa, Trias Thireou, Apostolos Beloukas, Dimitrios Chaniotis, Rebecca Golfinopoulou, Dimitrios Vlachakis, Elias Eliopoulos, and Louis Papageorgiou. The genetic background of ankylosing spondylitis reveals a distinct overlap with autoimmune diseases: a systematic review. Journal of Clinical Medicine, 14:3677, May 2025. URL: https://doi.org/10.3390/jcm14113677, doi:10.3390/jcm14113677. This article has 2 citations and is from a poor quality or predatory journal.

7. (parvin2025decodingtheinflammatoryosteogenic pages 1-2): Afroza Parvin, Ashish Ranjan Sharma, Md. Ashraful Hasan, Garima Sharma, Mohammad Mahfuz, Ali Khan, Eun Min Seo, Md. Mahmudul Hasan, Sang-Soo Lee, R. K. Pandey, and Ming-Shiou Jan. Decoding the inflammatory-osteogenic axis in ankylosing spondylitis: mechanisms, dysregulation, and emerging therapeutic interventions. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1633318, doi:10.3389/fimmu.2025.1633318. This article has 0 citations and is from a peer-reviewed journal.

8. (zormpa2025thegeneticbackground pages 25-27): Theodora Zormpa, Trias Thireou, Apostolos Beloukas, Dimitrios Chaniotis, Rebecca Golfinopoulou, Dimitrios Vlachakis, Elias Eliopoulos, and Louis Papageorgiou. The genetic background of ankylosing spondylitis reveals a distinct overlap with autoimmune diseases: a systematic review. Journal of Clinical Medicine, 14:3677, May 2025. URL: https://doi.org/10.3390/jcm14113677, doi:10.3390/jcm14113677. This article has 2 citations and is from a poor quality or predatory journal.