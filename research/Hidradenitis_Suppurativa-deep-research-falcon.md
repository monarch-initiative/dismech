---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-09T12:05:10.305707'
end_time: '2026-03-09T12:33:38.378394'
duration_seconds: 1708.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hidradenitis Suppurativa
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hidradenitis Suppurativa
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hidradenitis Suppurativa**.
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
- **Disease Name:** Hidradenitis Suppurativa
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hidradenitis Suppurativa**.
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


# Research Report: Pathophysiology of Hidradenitis Suppurativa (HS)

## Disease identifiers
- **Disease name:** Hidradenitis suppurativa (HS)
- **Synonym:** Acne inversa (as used in genetics/clinical trial records) (NCT04179175 chunk 1)
- **MONDO:** **Familial acne inversa** reported as **MONDO_0024516** in Open Targets disease–target associations for HS-related phenotypes (from tool state; supporting genetic framing aligns with HS γ-secretase genes in the literature) (d’onghia2024evidenceonhidradenitis pages 2-4)

## Executive summary (current understanding)
HS is a chronic, relapsing inflammatory disease of apocrine-bearing/intertriginous skin that is now commonly framed as an **autoinflammatory, neutrophilic dermatosis** in which **follicular occlusion** is an initiating event and **dysregulated innate/adaptive immune circuits** drive chronic tissue destruction, **epithelialized tunnels (sinus tracts)**, scarring, and systemic inflammation (matusiak2024polishguidelinesfor pages 1-2, d’onghia2024evidenceonhidradenitis pages 2-4). Recent 2023–2024 mechanistic work highlights (i) keratinocyte-intrinsic **epigenetic rewiring** that primes inflammatory programs, (ii) **inflammasome–IL-1 family** amplification, and (iii) in severe disease, a transition to **B cell/plasma cell–dominant pathology** organized in **tertiary lymphoid structures (TLS)** sustained by **fibroblast-derived CXCL13/CCL19** chemokine loops (jin2023epigeneticswitchreshapes pages 7-8, d’onghia2024evidenceonhidradenitis pages 4-5, yu2024skinimmunemesenchymalinterplay pages 5-6).

---

## 1. Key concepts & definitions (with staging context)

### 1.1 Core definition and conceptual model
- HS is described in 2024 clinical guidance as an **autoinflammatory disease** within **neutrophilic dermatoses**, with **follicular occlusion by keratin** as the initiating event and subsequent neutrophilic abscesses, macrophage/monocyte/DC infiltration, and chronic inflammatory remodeling (matusiak2024polishguidelinesfor pages 1-2).
- A mechanistic narrative in a 2024 autoinflammatory-focused review explicitly outlines early events: **“hyperkeratotic plugging of the terminal hair follicle opening”** leading to **occlusion**, **follicular rupture**, release of **DAMPs/PAMPs**, and amplification of **TNF-α and IL-1β pathways** (d’onghia2024evidenceonhidradenitis pages 2-4).

### 1.2 Hurley staging (phenotype–pathology link)
- Clinical severity is often staged by **Hurley**; severe disease features **“multiple interconnected sinus tracts and abscesses”** (Stage III) (chu2024hidradenitissuppurativaan pages 2-4). Tunnels are a key anatomic substrate for chronic inflammation and TLS adjacency in severe HS (yu2024skinimmunemesenchymalinterplay pages 1-3, yu2024skinimmunemesenchymalinterplay pages 20-26).

---

## 2. Core pathophysiology: molecular pathways and dysregulated cellular processes

### 2.1 Initiation: follicular occlusion, rupture, and microbial biofilm context
A frequently supported sequence is:
1) **Infundibular hyperkeratosis / follicular plugging** → 2) follicular dilation/elongation → 3) rupture of follicular wall → 4) biofilm formation and release of follicular contents → 5) innate immune activation (d’onghia2024evidenceonhidradenitis pages 2-4, matusiak2024polishguidelinesfor pages 1-2).

Direct mechanistic description (2024 review): follicular plugging causes “occlusion and dilatation/elongation” leading to rupture and “bacterial biofilm formation,” releasing DAMPs/PAMPs (d’onghia2024evidenceonhidradenitis pages 2-4).

### 2.2 Innate immune amplification: TLR2, inflammasome, IL-1 family, IL-36
- Resident/infiltrating cells show increased **TLR2** expression and upregulate **TNF-α** and **IL-1β** pathways early (d’onghia2024evidenceonhidradenitis pages 2-4).
- Inflammasome mechanism is explicitly stated: pro–IL-1β is cleaved to IL-1β by the **inflammasome** (d’onghia2024evidenceonhidradenitis pages 2-4).
- Keratinocytes contribute IL-1 family cytokines including **IL-1β** and **IL-36α/β/γ**, which promote downstream Th1/Th17 responses; perilesional expression is also reported (d’onghia2024evidenceonhidradenitis pages 4-5).
- Recent mechanistic synthesis links **NLRP3** and **pyrin** inflammasomes and notes that pharmacologic **NLRP3 inhibition (MCC950)** reduced multiple inflammatory mediators including **IL-1β, TNF-α, IL-17A, IFN-γ, CCL20, CXCL1, IL-8, IL-36γ** (d’onghia2024evidenceonhidradenitis pages 4-5).

### 2.3 Adaptive immune transition and chronicity: Th17/Treg imbalance and TLS
- HS exhibits enrichment of **Th17 cells** and dysregulation of the **Th17:Treg axis**; IL-1β/IL-6 overproduction (inflammasome-linked) is described as a driver (matusiak2024polishguidelinesfor pages 1-2, d’onghia2024evidenceonhidradenitis pages 2-4).
- **TLS as a chronic disease engine (2024 Immunity):** Yu et al. report fully developed TLS localized near **keratinized epithelial tunnels**, with local proliferation of T and B cells and **clonal expansion** (yu2024skinimmunemesenchymalinterplay pages 20-26, yu2024skinimmunemesenchymalinterplay pages 5-6). Expanded pathogenic T cells produce **IFNγ** and **IL17A**, and plasma cells produce antibodies reactive to keratinocyte layers (yu2024skinimmunemesenchymalinterplay pages 3-5, yu2024skinimmunemesenchymalinterplay pages 9-11).

### 2.4 Stromal/mesenchymal programming and fibrosis/tunnels
- Fibroblasts participate in tissue destruction and tunnel formation via chemokine production and MMP-associated remodeling (d’onghia2024evidenceonhidradenitis pages 2-4, ackerman2023irak4degraderin pages 6-7).
- In severe disease, stromal programs include fibroblast subsets that support TLS formation and B cell recruitment (e.g., **CXCL13+ fibroblasts**) (straalen2024hidradenitissuppurativakey pages 1-2, yu2024skinimmunemesenchymalinterplay pages 8-9).

### 2.5 Keratinocyte-intrinsic epigenetic switching (2023 PNAS)
Jin et al. provide strong mechanistic evidence that HS epidermis is not just reactive but intrinsically reprogrammed:
- **ATAC-seq** in basal cells showed HS **gained 1,434 and lost 3,722** accessible peaks (|log2FC|>0.5; FDR<0.1) and RNA-seq identified **1,287 DEGs** (|log2FC|>1; P<0.05) (jin2023epigeneticswitchreshapes pages 7-8).
- Single-cell profiling quantified large datasets (**12,942 healthy vs 24,867 HS** epidermal single-cell transcriptomes) and showed expansion of basal progenitor states and an HS-specific inflammatory keratinocyte subcluster (S100A7/A8/A9) (jin2023epigeneticswitchreshapes pages 2-3).
- The work links epidermal remodeling to disrupted adhesion/differentiation programs and inflammatory signaling networks including **IL-1, IL-10, IL-17, and complement signaling** (jin2023epigeneticswitchreshapes pages 7-8, jin2023epigeneticswitchreshapes pages 1-2).

---

## 3. Key molecular players (genes/proteins), chemical entities, cell types, and anatomic locations

| Mechanistic Module | Key Mediators (Genes/Proteins) | Key Cell Types | Key Tissues / Sites | Representative Quantitative Findings | Key Citations |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Follicular Occlusion & Genetic Initiation** | *NCSTN*, *PSENEN*, *PSEN1* ($\gamma$-secretase components), Notch signaling pathway | Keratinocytes, Follicular stem cells | Hair follicle infundibulum, Interfollicular epidermis | ~35-40% of patients have a family history; Notch/NCSTN blockade linked to abnormal keratinocyte differentiation and cysts. | (d’onghia2024evidenceonhidradenitis pages 2-4, saxena2024anemiainhidradenitis pages 9-14, chu2024hidradenitissuppurativaan pages 4-5) |
| **Epithelial Epigenetic Reprogramming** | *S100A7*, *S100A8*, *S100A9*, *IRF3*, *KLF*, *SOX9* (downregulated), *IL1B*, *CCL2* | Basal progenitors (CD49f+), S100A+ inflammatory keratinocytes | Epidermis (basal layer), Psoriasiform hyperplasia | HS basal cells show 1,434 gained chromatin peaks; *S100A8* occupancy enriched $\pm$2.5 kb at TSS; *IRF3* inhibition reduces inflammatory output by ~50%. | (jin2023epigeneticswitchreshapes pages 7-8, jin2023epigeneticswitchreshapes pages 9-10, jin2023epigeneticswitchreshapes pages 2-3, jin2023epigeneticswitchreshapes pages 5-6, jin2023epigeneticswitchreshapes pages 1-2) |
| **Innate Sensing & Inflammasome** | NLRP3, Caspase-1, IL-1$\beta$, IL-18, IL-36$\alpha$/$\beta$/$\gamma$, TLR2 | Macrophages, Neutrophils, Keratinocytes | Ruptured follicular wall, Dermis | NLRP3 inhibition (MCC950) lowers IL-1$\beta$/IL-17A; IL-36 family cytokines significantly elevated in lesional skin. | (d’onghia2024evidenceonhidradenitis pages 2-4, d’onghia2024evidenceonhidradenitis pages 4-5, lamiaux2023imohsetudede pages 177-180, ackerman2023irak4degraderin pages 6-7) |
| **TLR / IL-1R / IRAK4 Axis** | IRAK4, MyD88, NF-$\kappa$B, IL-6, IL-8, CRP | Monocytes, Lymphocytes (B/T), Dendritic cells | Peripheral blood (PBMC), Lesional skin | KT-474 (IRAK4 degrader) achieved >95% degradation in blood; 48-63% reduction in HS inflammatory biomarkers (IL-6, CRP); 955 upregulated genes in HS lesions. | (ackerman2023irak4degraderin pages 6-7, ackerman2023irak4degraderin pages 5-6, ackerman2023irak4degraderin pages 3-4, ackerman2023irak4degraderin pages 1-2, ackerman2023irak4degraderin pages 15-17) |
| **Dysregulated Cytokine Axes (TNF/Th17)** | TNF-$\alpha$, IL-17A, IL-17F, IL-23, IL-12, CCL20, IFN$\gamma$ | Th17 cells, Th1 cells, Neutrophils, Macrophages | Immune infiltrates, Dermis | Anti-TNF response ~40-60% in phase III; IL-17/TNF-$\alpha$ elevated in sera/tissue; specific T-cell clones express IL-17A/IFN$\gamma$. | (straalen2024hidradenitissuppurativakey pages 1-2, chu2024hidradenitissuppurativaan pages 2-4, chu2024hidradenitissuppurativaan pages 4-5, yu2024skinimmunemesenchymalinterplay pages 5-6) |
| **Adaptive Immunity & TLS Formation** | CXCL13, CCL19, TNF-$\alpha$, IL-21, BCR, TCR, SYK, BTK | B cells (CD19+), Plasma cells (CD38+), Tfh cells, CXCL13+ Fibroblasts | Tertiary Lymphoid Structures (TLS) near tunnels | ~40.1% of BCR clonotypes in lesions are expanded (vs <10% perilesional); BTK/SYK inhibitors show ~72-85% clinical response rates. | (straalen2024hidradenitissuppurativakey pages 1-2, yu2024skinimmunemesenchymalinterplay pages 3-5, yu2024skinimmunemesenchymalinterplay pages 1-3, yu2024skinimmunemesenchymalinterplay pages 5-6, yu2024skinimmunemesenchymalinterplay pages 8-9, yu2024skinimmunemesenchymalinterplay pages 30-36) |
| **Fibroblast, ECM & Tunnels** | MMPs (MMP12), CXCL13, CCL19, TNF receptors (TNFR1/2) | Pathogenic Fibroblasts (CXCL13+/CCL19+ subsets) | Sinus tracts / Epithelialized tunnels, Reticular dermis | Fibroblasts drive B/T aggregate formation in vitro via TNF-$\alpha$ loop; CXCL13hi fibroblasts localize to immune aggregates. | (d’onghia2024evidenceonhidradenitis pages 2-4, straalen2024hidradenitissuppurativakey pages 1-2, yu2024skinimmunemesenchymalinterplay pages 8-9, yu2024skinimmunemesenchymalinterplay pages 30-36) |
| **Autoimmunity & Complement** | Autoantibodies (IgG), Complement components | Plasma cells, Keratinocytes (as targets) | Lesional skin layers | Plasma cells produce antibodies reacting to keratinocyte layers; intracellular IgG and complement deposition observed. | (straalen2024hidradenitissuppurativakey pages 1-2, yu2024skinimmunemesenchymalinterplay pages 3-5, yu2024skinimmunemesenchymalinterplay pages 9-11) |


*Table: A summary of key mechanistic modules driving HS pathogenesis, identifying central mediators, cell types, tissues, and quantitative evidence from recent literature.*

### 3.1 Genes/Proteins (HGNC symbols; mechanistic notes)
**Genetic predisposition / follicular biology**
- **NCSTN, PSENEN, PSEN1 (γ-secretase complex / Notch processing):** Heterozygous loss-of-function mutations reported in HS; Notch pathway disruption is linked to abnormal follicular keratinization and cystic phenotypes (d’onghia2024evidenceonhidradenitis pages 2-4, chu2024hidradenitissuppurativaan pages 4-5).
- A 2024 genetics/treatment review notes “a total of **20 reported mutations in NCSTN** thus far” (chu2024hidradenitissuppurativaan pages 2-4).

**Innate immune sensors and IL-1 family**
- **TLR2** (increased expression in resident macrophages/lesions), **NLRP3**, **CASP1**, **IL1B**, **IL36A/IL36B/IL36G** (d’onghia2024evidenceonhidradenitis pages 2-4, d’onghia2024evidenceonhidradenitis pages 4-5).

**Cytokine axes**
- **TNF**, **IL17A/IL17F**, **IL23A/IL12B conceptual axis**, **IL6** (matusiak2024polishguidelinesfor pages 1-2, yu2024skinimmunemesenchymalinterplay pages 5-6, d’onghia2024evidenceonhidradenitis pages 2-4).

**TLS/stromal chemokines**
- **CXCL13**, **CCL19** (pathogenic fibroblast subsets; chemoattraction and feedback with TNF) (yu2024skinimmunemesenchymalinterplay pages 8-9, yu2024skinimmunemesenchymalinterplay pages 9-11).

**Tissue remodeling**
- **MMP12** highlighted among HS-upregulated inflammatory/tissue remodeling transcripts in lesional RNA-seq in an interventional setting (ackerman2023irak4degraderin pages 6-7).

**Keratinocyte inflammatory programs**
- **S100A7/S100A8/S100A9**, chromatin remodeling genes (HDAC1/2 etc.), and immune-response TF motifs (ATF3/FOSL2) are central in HS epidermal reprogramming (jin2023epigeneticswitchreshapes pages 2-3, jin2023epigeneticswitchreshapes pages 7-8).

### 3.2 Chemical entities / drugs (mechanistic relevance)
- **KT-474 (SAR444656)**: oral **IRAK4 degrader** targeting TLR/IL-1R signaling; provides in-human pathway validation (ackerman2023irak4degraderin pages 1-2, ackerman2023irak4degraderin pages 3-4).
- **MCC950**: small-molecule **NLRP3 inhibitor**, used mechanistically to demonstrate inflammasome contribution (d’onghia2024evidenceonhidradenitis pages 4-5).
- **Biologics targeting TNF and IL-17A** are mechanistically aligned with dominant cytokine axes; severe disease may involve additional circuits (B cells, complement, NETs) (straalen2024hidradenitissuppurativakey pages 1-2).

### 3.3 Cell types (CL) and roles
- **Keratinocytes** (CL:0000312): primary initiators/amplifiers (IL-1/IL-36), epigenetically reprogrammed inflammatory states (d’onghia2024evidenceonhidradenitis pages 4-5, jin2023epigeneticswitchreshapes pages 7-8).
- **Neutrophils** (CL:0000775): abscess formation; NETs emphasized as late-stage hallmark (straalen2024hidradenitissuppurativakey pages 1-2, matusiak2024polishguidelinesfor pages 1-2).
- **Monocytes/macrophages** (CL:0000576/CL:0000235): TLR2-high innate cytokine production (TNF/IL-1β/IL-6) (d’onghia2024evidenceonhidradenitis pages 2-4).
- **Th17 cells** (often annotated as CD4+ IL-17A+ T cells): enriched and clonally expanded in TLS (yu2024skinimmunemesenchymalinterplay pages 5-6).
- **B cells / plasma cells** (CL:0000236; CL:0000786): dominant late-stage infiltrates and autoantibody production (straalen2024hidradenitissuppurativakey pages 1-2, yu2024skinimmunemesenchymalinterplay pages 9-11).
- **Fibroblasts** (CL:0000057): CXCL13hi/CCL19hi inflammatory stromal subsets that organize TLS (yu2024skinimmunemesenchymalinterplay pages 8-9).

### 3.4 Anatomical locations (UBERON)
- **Hair follicle / infundibulum** (UBERON:0001037): follicular occlusion/rupture origin (d’onghia2024evidenceonhidradenitis pages 2-4, matusiak2024polishguidelinesfor pages 1-2).
- **Interfollicular epidermis**: keratinocyte epigenetic switch and hyperproliferation (jin2023epigeneticswitchreshapes pages 7-8).
- **Dermis (papillary/reticular)**: spatial segregation of CCL19hi (upper dermis) vs CXCL13hi (lower dermis) fibroblasts (yu2024skinimmunemesenchymalinterplay pages 8-9).
- **Epithelialized tunnels/sinus tracts**: chronic inflammatory niche adjacent to TLS (yu2024skinimmunemesenchymalinterplay pages 20-26).

---

## 4. Biological processes disrupted (GO: Biological Process candidates)
The following process-level disruptions are directly supported by recent mechanistic studies and suitable for GO annotation:
- **Keratinization / cornification** (initiation and chronic epithelial remodeling) (matusiak2024polishguidelinesfor pages 1-2, jin2023epigeneticswitchreshapes pages 3-5).
- **Innate immune response** and **pattern recognition receptor signaling** (TLR2; DAMP/PAMP-driven) (d’onghia2024evidenceonhidradenitis pages 2-4).
- **Inflammasome complex activation** and **interleukin-1 production** (NLRP3/CASP1 → IL-1β) (d’onghia2024evidenceonhidradenitis pages 2-4, d’onghia2024evidenceonhidradenitis pages 4-5).
- **Chemokine-mediated leukocyte migration** (e.g., CXCL1/6/8; CCL2/20; CXCL13/CCL19 in TLS context) (d’onghia2024evidenceonhidradenitis pages 2-4, yu2024skinimmunemesenchymalinterplay pages 8-9).
- **Adaptive immune response**, **B cell activation/differentiation**, and **tertiary lymphoid structure organization** (clonal expansion; chemokine loops) (yu2024skinimmunemesenchymalinterplay pages 5-6, yu2024skinimmunemesenchymalinterplay pages 9-11).
- **Extracellular matrix disassembly / tissue remodeling** contributing to tunnel formation (MMPs, fibroblast involvement) (d’onghia2024evidenceonhidradenitis pages 2-4, ackerman2023irak4degraderin pages 6-7).

---

## 5. Cellular components (GO: Cellular Component candidates)
- **Inflammasome complex** (site of pro–IL-1β processing) (d’onghia2024evidenceonhidradenitis pages 2-4).
- **Nucleus/chromatin** (keratinocyte epigenetic rewiring; ATAC/CUT&RUN evidence) (jin2023epigeneticswitchreshapes pages 7-8, jin2023epigeneticswitchreshapes pages 9-10).
- **Extracellular space** (cytokines/chemokines; autoantibodies; complement deposition) (yu2024skinimmunemesenchymalinterplay pages 9-11).
- **Tertiary lymphoid structure** (immune aggregate compartmentalization adjacent to tunnels) (yu2024skinimmunemesenchymalinterplay pages 1-3, yu2024skinimmunemesenchymalinterplay pages 20-26).

---

## 6. Disease progression: sequence of events (integrated model)

### 6.1 Proposed sequence (from trigger to clinical lesions)
1) **Follicular hyperkeratosis** with keratin plug → follicular distension (d’onghia2024evidenceonhidradenitis pages 2-4, matusiak2024polishguidelinesfor pages 1-2)
2) **Follicular rupture** and microbial biofilm context → DAMP/PAMP release (d’onghia2024evidenceonhidradenitis pages 2-4)
3) **Innate hyperactivation**: TLR2 upregulation; inflammasome-driven IL-1β; IL-36 from keratinocytes (d’onghia2024evidenceonhidradenitis pages 2-4, d’onghia2024evidenceonhidradenitis pages 4-5)
4) **Chemokine recruitment** of neutrophils/monocytes/T cells/B cells; Th17:Treg imbalance (d’onghia2024evidenceonhidradenitis pages 2-4, matusiak2024polishguidelinesfor pages 1-2)
5) **Chronic remodeling**: fibroblast activation, MMP-mediated tissue destruction, **tunnel formation** (d’onghia2024evidenceonhidradenitis pages 2-4)
6) **Late-stage immune reprogramming**: **TLS near tunnels**, clonal B/T responses, autoantibodies, complement activation and NETs (yu2024skinimmunemesenchymalinterplay pages 9-11, straalen2024hidradenitissuppurativakey pages 1-2)

### 6.2 New 2023–2024 addition: epithelium and stroma as active disease drivers
- Keratinocyte programs are epigenetically primed toward inflammatory signaling (ATAC-seq peak rewiring; inflammatory keratinocyte S100A state) (jin2023epigeneticswitchreshapes pages 7-8, jin2023epigeneticswitchreshapes pages 2-3).
- Fibroblast subsets act as organizers of adaptive immunity (CXCL13/CCL19), generating a self-sustaining immune–mesenchymal feedback loop (yu2024skinimmunemesenchymalinterplay pages 8-9, yu2024skinimmunemesenchymalinterplay pages 9-11).

**Central mechanistic model figure:** fibroblast–lymphocyte circuits driving TLS initiation/maintenance are summarized in Yu et al. (Immunity 2024) (yu2024skinimmunemesenchymalinterplay media 3233e121, yu2024skinimmunemesenchymalinterplay media 0432ca6a).

---

## 7. Phenotypic manifestations (HP terms; mechanism links)
Mechanistically linked phenotypes include:
- **Painful inflammatory nodules/abscesses** (neutrophil-rich acute lesions driven by IL-1/TNF/chemokines) (matusiak2024polishguidelinesfor pages 1-2, d’onghia2024evidenceonhidradenitis pages 2-4).
- **Draining fistulae / epithelialized sinus tracts (tunnels)** (ECM remodeling, chronic inflammation) (d’onghia2024evidenceonhidradenitis pages 2-4, yu2024skinimmunemesenchymalinterplay pages 20-26).
- **Scarring/fibrosis** (recurrent injury and remodeling) (saxena2024anemiainhidradenitis pages 9-14, matusiak2024polishguidelinesfor pages 1-2).

(HP codes are not explicitly enumerated in the retrieved texts; the above are ontology-ready phenotype statements supported by mechanistic sources.)

---

## 8. Recent developments & latest research (prioritizing 2023–2024)

### 8.1 2024 Immunity: TLS and immune–mesenchymal feedback loops
Key 2024 findings:
- BCR repertoires show that “**most expanded BCR clonotypes were found in HS lesional skin, with an average of 40.1% belonging to expanded clones**” (yu2024skinimmunemesenchymalinterplay pages 5-6).
- Two fibroblast states **CXCL13hi** and **CCL19hi** are expanded, respond to TNFα/IL1β, and drive lymphocyte aggregation; **TNFα blockade prevents aggregate initiation early** (yu2024skinimmunemesenchymalinterplay pages 9-11, yu2024skinimmunemesenchymalinterplay pages 8-9).
- The images retrieved from this paper summarize ligand–receptor networks and the TNFα–CXCL13/CCL19 positive feedback loops (yu2024skinimmunemesenchymalinterplay media 3233e121, yu2024skinimmunemesenchymalinterplay media 0432ca6a).

### 8.2 2024 JCI (expert synthesis): B cells, complement, NETs as late-stage hallmarks
- Van Straalen et al. (2024) describe B cells as “a central driver” and “dominant infiltrating leukocytes in late-stage HS lesions,” with “increased immunoglobulin production and complement activation” and NET formation as “a hallmark of late-stage disease” (straalen2024hidradenitissuppurativakey pages 1-2).

### 8.3 2023 PNAS: epigenetic switch in basal progenitors
- Quantitative epigenomic rewiring: **1,434 gained / 3,722 lost** ATAC peaks; **1,287 DEGs** (jin2023epigeneticswitchreshapes pages 7-8).
- Large single-cell profiling: **12,942 healthy vs 24,867 HS** epidermal transcriptomes (jin2023epigeneticswitchreshapes pages 2-3).

### 8.4 2023 Nature Medicine: in-human validation of TLR/IL-1R → IRAK4 dependency
- KT-474 achieved “**48–63% reductions across the three analytes**” (IL-6, IL-1β, CRP) in HS and reduced IRAK4 in skin lesions “**by more than 50%**” with normalization (P<0.05) (ackerman2023irak4degraderin pages 3-4).
- Lesional transcriptomics: **955 genes upregulated and 1,309 downregulated** in HS versus healthy volunteer skin (ackerman2023irak4degraderin pages 3-4).

---

## 9. Current applications & real-world implementations

### 9.1 Mechanism-guided therapies (current practice and near-term)
- **Anti-TNF therapy**: clinically effective in a subset; expert synthesis notes phase III response around **40%–60%** and proposes TNF impacts B cell activation in late-stage lesions (straalen2024hidradenitissuppurativakey pages 1-2).
- **IL-17 axis therapies** (secukinumab; investigational IL-17A inhibitors): supported by Th17/TLS evidence and ongoing large trials/extension studies (yu2024skinimmunemesenchymalinterplay pages 5-6, NCT04179175 chunk 1).
- **IRAK4 degradation** (KT-474): early clinical proof-of-mechanism for TLR/IL-1R-driven inflammation and systemic biomarkers (ackerman2023irak4degraderin pages 3-4).

### 9.2 Clinical trial implementations (ClinicalTrials.gov)
- **Secukinumab extension study** (NCT04179175): randomized withdrawal design assessing maintenance of HiSCR response through Week 104 and long-term follow-up through Week 260 (posting and results timeline included in registry) (NCT04179175 chunk 1).
- **Izokibep phase 3** (NCT05905783): IL-17A inhibitor trial; terminated for strategic reasons not due to safety; primary endpoint HiSCR75 at Week 12 (NCT05905783 chunk 1).
- **Izokibep phase 2b** (NCT05355805): IL-17A inhibitor; completed; endpoints include HiSCR75 (Week 12/16) and HiSCR90/100 (NCT05355805 chunk 1).

---

## 10. Relevant statistics and quantitative data (recent studies)

### 10.1 Epidemiology and heritability (guidelines)
- Prevalence estimates vary by population: global ~**0.4%**, USA ~**0.05%**, Denmark **4.1%**, Poland **1.6%**; pediatric prevalence **0.028%** (<18 years; nearly 55 million) (matusiak2024polishguidelinesfor pages 1-2).
- Sex ratio: **female-to-male 3.6:1** (French cohort n=618) (matusiak2024polishguidelinesfor pages 1-2).
- Familial risk: **34.3% of first-degree relatives** affected; heritability up to **80%** (matusiak2024polishguidelinesfor pages 1-2).

### 10.2 TLS and clonal expansion (2024 Immunity)
- Lesional BCR clonotypes: mean **40.1% expanded clones** in lesions; >90% single-cell clonotypes in perilesional skin/blood (yu2024skinimmunemesenchymalinterplay pages 5-6).
- Study cohort sizes in scRNA-seq analysis: normal **N=4**, perilesional **N=7**, lesional **N=8** (yu2024skinimmunemesenchymalinterplay pages 20-26).

### 10.3 Epigenomics and single-cell (2023 PNAS)
- **1,287 DEGs**, **1,434 gained / 3,722 lost** chromatin peaks (jin2023epigeneticswitchreshapes pages 7-8).
- Single-cell epidermis: **12,942 healthy vs 24,867 HS** transcriptomes (jin2023epigeneticswitchreshapes pages 2-3).

### 10.4 Interventional biomarker modulation (2023 Nature Medicine)
- KT-474: **48–63%** reductions across **IL-6, IL-1β, CRP**; IRAK4 in skin reduced by >50% with normalization (ackerman2023irak4degraderin pages 3-4).

---

## 11. Evidence items with PMIDs (from retrieved sources)
The retrieved evidence set contains explicit PMIDs mainly via Open Targets for genetic associations (older foundational genetics), while the 2023–2024 papers in this run are cited by DOI/URL in the excerpts. The PMIDs directly surfaced in the retrieved context are:
- **NCSTN (nicastrin) association evidence:** PMIDs **21495993, 26663538, 22759192, 22622421, 26463457, 22834455, 26224166, 20929727, 21412258, 32086639, 32048120** (Open Targets evidence list; supports γ-secretase genetics) (d’onghia2024evidenceonhidradenitis pages 2-4).
- **PSENEN association evidence:** PMIDs **28922471, 23439959, 28601418, 28287404, 23020871, 27900998, 21412258, 32086639, 32048120, 20929727** (Open Targets evidence list; supports γ-secretase genetics) (d’onghia2024evidenceonhidradenitis pages 2-4).

(Within the provided excerpts for 2023–2024 primary/review articles, PMIDs were not printed; therefore, this report provides URLs/DOIs and publication dates for those sources as required.)

---

## 12. Knowledge-base–ready annotations (condensed)

| Category | Ontology Term / Entity | Role & Quantitative Findings in HS | Evidence |
| :--- | :--- | :--- | :--- |
| **Gene/Protein** | *NCSTN, PSENEN, PSEN1* | Gamma-secretase subunits; heterozygous mutations found in ~35-40% of familial HS cases (or specific cohorts like 6 Han Chinese families); causal in Notch pathway dysfunction. | (saxena2024anemiainhidradenitis pages 9-14, d’onghia2024evidenceonhidradenitis pages 2-4, chu2024hidradenitissuppurativaan pages 2-4) |
| **Gene/Protein** | *TNF* (TNF-$\alpha$) | Key pro-inflammatory cytokine; anti-TNF response rates ~40-60% in phase III; upregulated in monocytes and B-cells. | (straalen2024hidradenitissuppurativakey pages 1-2, chu2024hidradenitissuppurativaan pages 2-4, matusiak2024polishguidelinesfor pages 1-2, liao2024cellularindexingof pages 14-16) |
| **Gene/Protein** | *IL17A / IL17F* | Th17 axis mediators; elevated in serum/lesions; specific T-cell clones in TLS express *IL17A*; targeted by phase 3 biologic trials. | (straalen2024hidradenitissuppurativakey pages 1-2, yu2024skinimmunemesenchymalinterplay pages 5-6, matusiak2024polishguidelinesfor pages 1-2, liao2024cellularindexingof pages 14-16) |
| **Gene/Protein** | *IL1B* (IL-1$\beta$) | Inflammasome product; significantly elevated in lesions; IRAK4 degrader KT-474 reduced IL-1$\beta$ by 48-63% in phase 1 trial. | (d’onghia2024evidenceonhidradenitis pages 4-5, matusiak2024polishguidelinesfor pages 1-2, ackerman2023irak4degraderin pages 3-4) |
| **Gene/Protein** | *CXCL13 / CCL19* | Lymphoid chemokines; upregulated in pathogenic fibroblasts (CXCL13hi/CCL19hi subsets); drive B/T cell recruitment to Tertiary Lymphoid Structures. | (straalen2024hidradenitissuppurativakey pages 1-2, yu2024skinimmunemesenchymalinterplay pages 8-9, yu2024skinimmunemesenchymalinterplay pages 30-36) |
| **Gene/Protein** | *S100A8 / S100A9* | Calprotectin subunits; *S100A8* chromatin occupancy enriched $\pm$2.5 kb at TSS in HS basal cells; marker of epigenetic inflammatory switch. | (jin2023epigeneticswitchreshapes pages 7-8, jin2023epigeneticswitchreshapes pages 5-6) |
| **Gene/Protein** | *IRAK4* | Kinase/scaffold in TLR/IL-1R signaling; overexpression in HS skin normalized by degrader KT-474 (>50% reduction). | (ackerman2023irak4degraderin pages 1-2, ackerman2023irak4degraderin pages 3-4) |
| **Gene/Protein** | *NLRP3* | Inflammasome sensor; pharmacological inhibition (MCC950) lowers IL-1$\beta$ and IL-17A; upregulated in myeloid clusters. | (d’onghia2024evidenceonhidradenitis pages 4-5) |
| **GO: Bio Process** | Keratinization | Follicular occlusion by keratin is the initiating event; altered in HS genetic forms (e.g., *KRT* mutations). | (d’onghia2024evidenceonhidradenitis pages 2-4, matusiak2024polishguidelinesfor pages 1-2) |
| **GO: Bio Process** | Adaptive immune response | Clonal expansion of B cells (40.1% expanded BCR clonotypes in lesions vs <10% perilesional) and T cells in TLS. | (yu2024skinimmunemesenchymalinterplay pages 5-6) |
| **GO: Bio Process** | Inflammatory response | Broad upregulation of immune pathways; 1,287 differentially expressed genes between healthy and HS epidermis. | (d’onghia2024evidenceonhidradenitis pages 2-4, jin2023epigeneticswitchreshapes pages 7-8) |
| **GO: Cell Component** | Tertiary lymphoid structure | Organized immune aggregates near epithelial tunnels; site of local B cell/plasma cell expansion and autoantibody production. | (yu2024skinimmunemesenchymalinterplay pages 3-5, yu2024skinimmunemesenchymalinterplay pages 1-3) |
| **Cell Type** | Keratinocytes (CL:0000312) | Initiate inflammation via IL-1/IL-36; undergo epigenetic reprogramming (S100A+ state) driving cytokine loops. | (d’onghia2024evidenceonhidradenitis pages 4-5, jin2023epigeneticswitchreshapes pages 7-8) |
| **Cell Type** | Plasma cells (CL:0000786) | Produce anti-keratinocyte autoantibodies; enriched in TLS periphery; correlate with disease severity. | (yu2024skinimmunemesenchymalinterplay pages 9-11, yu2024skinimmunemesenchymalinterplay pages 5-6) |
| **Cell Type** | Fibroblasts (CL:0000057) | Pathogenic subsets (CXCL13+); drive inflammation and TLS formation via TNF-chemokine feed-forward loops. | (yu2024skinimmunemesenchymalinterplay pages 8-9, yu2024skinimmunemesenchymalinterplay pages 30-36) |
| **Anatomical Site** | Hair follicle (UBERON:0001037) | Primary site of pathology (infundibular occlusion, rupture); stem cell niche disruption. | (d’onghia2024evidenceonhidradenitis pages 2-4, matusiak2024polishguidelinesfor pages 1-2) |
| **Chemical/Drug** | KT-474 | Small molecule IRAK4 degrader; reduced inflammatory biomarkers (IL-6, CRP) and improved skin lesions in Phase 1. | (ackerman2023irak4degraderin pages 5-6, ackerman2023irak4degraderin pages 3-4) |
| **Chemical/Drug** | MCC950 | Small molecule NLRP3 inhibitor; reduces IL-1$\beta$, TNF, IL-17A, and CXCL1 in HS models. | (d’onghia2024evidenceonhidradenitis pages 4-5) |


*Table: This table categorizes key genes, proteins, biological processes, cell types, and chemical entities involved in Hidradenitis Suppurativa, mapping them to standard ontologies (HGNC, GO, CL, UBERON) and providing quantitative evidence from 2023-2024 research.*

---

## 13. Authoritative expert opinions & analysis (interpretation)
- **Late-stage disease architecture matters:** JCI 2024 frames HS treatment failure/success through the lens of stage-specific biology, emphasizing B cell/plasma cell dominance, complement activation, and NETs in late-stage lesions—implying that cytokine-only blockade may be insufficient once TLS and autoreactivity are established (straalen2024hidradenitissuppurativakey pages 1-2).
- **Temporal therapeutic windows:** Immunity 2024 provides functional evidence (microfluidic TLS model) that **TNFα is required for TLS initiation but less so for maintenance**, supporting early intervention and/or combination approaches aimed at stromal–immune organizing circuits (yu2024skinimmunemesenchymalinterplay pages 9-11, yu2024skinimmunemesenchymalinterplay pages 8-9).
- **Epithelial priming suggests upstream targets:** PNAS 2023 indicates basal progenitor chromatin is rewired toward inflammatory readiness (IL-1/IL-17/complement networks), suggesting epigenetic or epithelial differentiation therapies may complement immune blockade (jin2023epigeneticswitchreshapes pages 7-8, jin2023epigeneticswitchreshapes pages 1-2).

---

## Key URLs and publication dates (2023–2024 priority)
- Yu et al., **Immunity**, **Dec 2024**. https://doi.org/10.1016/j.immuni.2024.11.010 (yu2024skinimmunemesenchymalinterplay pages 20-26)
- van Straalen et al., **J Clin Invest**, **Nov 2024**. https://doi.org/10.1172/jci186744 (straalen2024hidradenitissuppurativakey pages 1-2)
- D’Onghia et al., **J Clin Med**, **Sep 2024**. https://doi.org/10.3390/jcm13175211 (d’onghia2024evidenceonhidradenitis pages 2-4)
- Matusiak et al., **Dermatology Review**, **Jan 2024**. https://doi.org/10.5114/dr.2024.140820 (matusiak2024polishguidelinesfor pages 1-2)
- Chu & Yu, **Biomedicines**, **Feb 2024**. https://doi.org/10.3390/biomedicines12020338 (chu2024hidradenitissuppurativaan pages 2-4)
- Jin et al., **PNAS**, **Nov 2023**. https://doi.org/10.1073/pnas.2315096120 (jin2023epigeneticswitchreshapes pages 7-8)
- Ackerman et al., **Nature Medicine**, **Nov 2023**. https://doi.org/10.1038/s41591-023-02635-7 (ackerman2023irak4degraderin pages 3-4)
- ClinicalTrials.gov: **NCT05905783** (Phase 3 izokibep; posted Jun 15, 2023; terminated; results posted Oct 15, 2025). https://clinicaltrials.gov/study/NCT05905783 (NCT05905783 chunk 1)
- ClinicalTrials.gov: **NCT04179175** (secukinumab extension; results posted Jun 21, 2024). https://clinicaltrials.gov/study/NCT04179175 (NCT04179175 chunk 1)

---

## Figure evidence
Mechanistic model of TLS-driving fibroblast–lymphocyte circuits (Yu et al. 2024) (yu2024skinimmunemesenchymalinterplay media 3233e121, yu2024skinimmunemesenchymalinterplay media 0432ca6a).


References

1. (NCT04179175 chunk 1):  Extension Study to Assess Effects of Non-interrupted Versus Interrupted and Long Term Treatment of Two Dose Regimes of Secukinumab in Subjects With Hidradenitis Suppurativa. Novartis Pharmaceuticals. 2020. ClinicalTrials.gov Identifier: NCT04179175

2. (d’onghia2024evidenceonhidradenitis pages 2-4): Martina D’Onghia, Dalma Malvaso, Giulia Galluccio, Flaminia Antonelli, Giulia Coscarella, Pietro Rubegni, Ketty Peris, and Laura Calabrese. Evidence on hidradenitis suppurativa as an autoinflammatory skin disease. Journal of Clinical Medicine, 13(17):5211, Sep 2024. URL: https://doi.org/10.3390/jcm13175211, doi:10.3390/jcm13175211. This article has 11 citations.

3. (matusiak2024polishguidelinesfor pages 1-2): Łukasz Matusiak, Irena Walecka, Adam Reich, Andrzej Bieniek, Dorota Krasowska, Wioletta Barańska-Rybak, Beata Bergler-Czop, Aleksandra Lesiak, Joanna Narbutt, Agnieszka Owczarczyk-Saczonek, Witold Owczarek, and Jacek Szepietowski. Polish guidelines for the diagnosis and treatment of hidradenitis suppurativa. Dermatology Review, 111:1-19, Jan 2024. URL: https://doi.org/10.5114/dr.2024.140820, doi:10.5114/dr.2024.140820. This article has 4 citations.

4. (jin2023epigeneticswitchreshapes pages 7-8): Lin Jin, Yunjia Chen, Suhail Muzaffar, Chao Li, Carlos A. Mier-Aguilar, Jasim Khan, Mahendra P. Kashyap, Shanrun Liu, Ritesh Srivastava, Jessy S. Deshane, Tim M. Townes, Boni E. Elewski, Craig A. Elmets, David K. Crossman, Chander Raman, and Mohammad Athar. Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. Proceedings of the National Academy of Sciences of the United States of America, Nov 2023. URL: https://doi.org/10.1073/pnas.2315096120, doi:10.1073/pnas.2315096120. This article has 31 citations and is from a highest quality peer-reviewed journal.

5. (d’onghia2024evidenceonhidradenitis pages 4-5): Martina D’Onghia, Dalma Malvaso, Giulia Galluccio, Flaminia Antonelli, Giulia Coscarella, Pietro Rubegni, Ketty Peris, and Laura Calabrese. Evidence on hidradenitis suppurativa as an autoinflammatory skin disease. Journal of Clinical Medicine, 13(17):5211, Sep 2024. URL: https://doi.org/10.3390/jcm13175211, doi:10.3390/jcm13175211. This article has 11 citations.

6. (yu2024skinimmunemesenchymalinterplay pages 5-6): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

7. (chu2024hidradenitissuppurativaan pages 2-4): Yi-Lun Chu and Sebastian Yu. Hidradenitis suppurativa: an understanding of genetic factors and treatment. Biomedicines, 12:338, Feb 2024. URL: https://doi.org/10.3390/biomedicines12020338, doi:10.3390/biomedicines12020338. This article has 17 citations.

8. (yu2024skinimmunemesenchymalinterplay pages 1-3): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

9. (yu2024skinimmunemesenchymalinterplay pages 20-26): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

10. (yu2024skinimmunemesenchymalinterplay pages 3-5): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

11. (yu2024skinimmunemesenchymalinterplay pages 9-11): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

12. (ackerman2023irak4degraderin pages 6-7): Lindsay Ackerman, Gerard Acloque, Sandro Bacchelli, Howard Schwartz, Brian J. Feinstein, Phillip La Stella, Afsaneh Alavi, Ashwin Gollerkeri, Jeffrey Davis, Veronica Campbell, Alice McDonald, Sagar Agarwal, Rahul Karnik, Kelvin Shi, Aimee Mishkin, Jennifer Culbertson, Christine Klaus, Bradley Enerson, Virginia Massa, Eric Kuhn, Kirti Sharma, Erin Keaney, Randy Barnes, Dapeng Chen, Xiaozhang Zheng, Haojing Rong, Vijay Sabesan, Chris Ho, Nello Mainolfi, Anthony Slavin, and Jared A. Gollob. Irak4 degrader in hidradenitis suppurativa and atopic dermatitis: a phase 1 trial. Nature Medicine, 29:3127-3136, Nov 2023. URL: https://doi.org/10.1038/s41591-023-02635-7, doi:10.1038/s41591-023-02635-7. This article has 104 citations and is from a highest quality peer-reviewed journal.

13. (straalen2024hidradenitissuppurativakey pages 1-2): Kelsey R. van Straalen, Vincent Piguet, and Johann E. Gudjonsson. Hidradenitis suppurativa: key insights into treatment success and failure. Journal of Clinical Investigation, Nov 2024. URL: https://doi.org/10.1172/jci186744, doi:10.1172/jci186744. This article has 11 citations and is from a highest quality peer-reviewed journal.

14. (yu2024skinimmunemesenchymalinterplay pages 8-9): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

15. (jin2023epigeneticswitchreshapes pages 2-3): Lin Jin, Yunjia Chen, Suhail Muzaffar, Chao Li, Carlos A. Mier-Aguilar, Jasim Khan, Mahendra P. Kashyap, Shanrun Liu, Ritesh Srivastava, Jessy S. Deshane, Tim M. Townes, Boni E. Elewski, Craig A. Elmets, David K. Crossman, Chander Raman, and Mohammad Athar. Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. Proceedings of the National Academy of Sciences of the United States of America, Nov 2023. URL: https://doi.org/10.1073/pnas.2315096120, doi:10.1073/pnas.2315096120. This article has 31 citations and is from a highest quality peer-reviewed journal.

16. (jin2023epigeneticswitchreshapes pages 1-2): Lin Jin, Yunjia Chen, Suhail Muzaffar, Chao Li, Carlos A. Mier-Aguilar, Jasim Khan, Mahendra P. Kashyap, Shanrun Liu, Ritesh Srivastava, Jessy S. Deshane, Tim M. Townes, Boni E. Elewski, Craig A. Elmets, David K. Crossman, Chander Raman, and Mohammad Athar. Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. Proceedings of the National Academy of Sciences of the United States of America, Nov 2023. URL: https://doi.org/10.1073/pnas.2315096120, doi:10.1073/pnas.2315096120. This article has 31 citations and is from a highest quality peer-reviewed journal.

17. (saxena2024anemiainhidradenitis pages 9-14): A Saxena. Anemia in hidradenitis suppurativa: a retrospective cohort study. Unknown journal, 2024.

18. (chu2024hidradenitissuppurativaan pages 4-5): Yi-Lun Chu and Sebastian Yu. Hidradenitis suppurativa: an understanding of genetic factors and treatment. Biomedicines, 12:338, Feb 2024. URL: https://doi.org/10.3390/biomedicines12020338, doi:10.3390/biomedicines12020338. This article has 17 citations.

19. (jin2023epigeneticswitchreshapes pages 9-10): Lin Jin, Yunjia Chen, Suhail Muzaffar, Chao Li, Carlos A. Mier-Aguilar, Jasim Khan, Mahendra P. Kashyap, Shanrun Liu, Ritesh Srivastava, Jessy S. Deshane, Tim M. Townes, Boni E. Elewski, Craig A. Elmets, David K. Crossman, Chander Raman, and Mohammad Athar. Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. Proceedings of the National Academy of Sciences of the United States of America, Nov 2023. URL: https://doi.org/10.1073/pnas.2315096120, doi:10.1073/pnas.2315096120. This article has 31 citations and is from a highest quality peer-reviewed journal.

20. (jin2023epigeneticswitchreshapes pages 5-6): Lin Jin, Yunjia Chen, Suhail Muzaffar, Chao Li, Carlos A. Mier-Aguilar, Jasim Khan, Mahendra P. Kashyap, Shanrun Liu, Ritesh Srivastava, Jessy S. Deshane, Tim M. Townes, Boni E. Elewski, Craig A. Elmets, David K. Crossman, Chander Raman, and Mohammad Athar. Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. Proceedings of the National Academy of Sciences of the United States of America, Nov 2023. URL: https://doi.org/10.1073/pnas.2315096120, doi:10.1073/pnas.2315096120. This article has 31 citations and is from a highest quality peer-reviewed journal.

21. (lamiaux2023imohsetudede pages 177-180): M Lamiaux. Imohs: etude de l'immunomodulation de la réponse immunitaire dans l'hidradénite suppurée et evaluation in vitro et ex vivo d'une nouvelle stratégie thérapeutique. Unknown journal, 2023.

22. (ackerman2023irak4degraderin pages 5-6): Lindsay Ackerman, Gerard Acloque, Sandro Bacchelli, Howard Schwartz, Brian J. Feinstein, Phillip La Stella, Afsaneh Alavi, Ashwin Gollerkeri, Jeffrey Davis, Veronica Campbell, Alice McDonald, Sagar Agarwal, Rahul Karnik, Kelvin Shi, Aimee Mishkin, Jennifer Culbertson, Christine Klaus, Bradley Enerson, Virginia Massa, Eric Kuhn, Kirti Sharma, Erin Keaney, Randy Barnes, Dapeng Chen, Xiaozhang Zheng, Haojing Rong, Vijay Sabesan, Chris Ho, Nello Mainolfi, Anthony Slavin, and Jared A. Gollob. Irak4 degrader in hidradenitis suppurativa and atopic dermatitis: a phase 1 trial. Nature Medicine, 29:3127-3136, Nov 2023. URL: https://doi.org/10.1038/s41591-023-02635-7, doi:10.1038/s41591-023-02635-7. This article has 104 citations and is from a highest quality peer-reviewed journal.

23. (ackerman2023irak4degraderin pages 3-4): Lindsay Ackerman, Gerard Acloque, Sandro Bacchelli, Howard Schwartz, Brian J. Feinstein, Phillip La Stella, Afsaneh Alavi, Ashwin Gollerkeri, Jeffrey Davis, Veronica Campbell, Alice McDonald, Sagar Agarwal, Rahul Karnik, Kelvin Shi, Aimee Mishkin, Jennifer Culbertson, Christine Klaus, Bradley Enerson, Virginia Massa, Eric Kuhn, Kirti Sharma, Erin Keaney, Randy Barnes, Dapeng Chen, Xiaozhang Zheng, Haojing Rong, Vijay Sabesan, Chris Ho, Nello Mainolfi, Anthony Slavin, and Jared A. Gollob. Irak4 degrader in hidradenitis suppurativa and atopic dermatitis: a phase 1 trial. Nature Medicine, 29:3127-3136, Nov 2023. URL: https://doi.org/10.1038/s41591-023-02635-7, doi:10.1038/s41591-023-02635-7. This article has 104 citations and is from a highest quality peer-reviewed journal.

24. (ackerman2023irak4degraderin pages 1-2): Lindsay Ackerman, Gerard Acloque, Sandro Bacchelli, Howard Schwartz, Brian J. Feinstein, Phillip La Stella, Afsaneh Alavi, Ashwin Gollerkeri, Jeffrey Davis, Veronica Campbell, Alice McDonald, Sagar Agarwal, Rahul Karnik, Kelvin Shi, Aimee Mishkin, Jennifer Culbertson, Christine Klaus, Bradley Enerson, Virginia Massa, Eric Kuhn, Kirti Sharma, Erin Keaney, Randy Barnes, Dapeng Chen, Xiaozhang Zheng, Haojing Rong, Vijay Sabesan, Chris Ho, Nello Mainolfi, Anthony Slavin, and Jared A. Gollob. Irak4 degrader in hidradenitis suppurativa and atopic dermatitis: a phase 1 trial. Nature Medicine, 29:3127-3136, Nov 2023. URL: https://doi.org/10.1038/s41591-023-02635-7, doi:10.1038/s41591-023-02635-7. This article has 104 citations and is from a highest quality peer-reviewed journal.

25. (ackerman2023irak4degraderin pages 15-17): Lindsay Ackerman, Gerard Acloque, Sandro Bacchelli, Howard Schwartz, Brian J. Feinstein, Phillip La Stella, Afsaneh Alavi, Ashwin Gollerkeri, Jeffrey Davis, Veronica Campbell, Alice McDonald, Sagar Agarwal, Rahul Karnik, Kelvin Shi, Aimee Mishkin, Jennifer Culbertson, Christine Klaus, Bradley Enerson, Virginia Massa, Eric Kuhn, Kirti Sharma, Erin Keaney, Randy Barnes, Dapeng Chen, Xiaozhang Zheng, Haojing Rong, Vijay Sabesan, Chris Ho, Nello Mainolfi, Anthony Slavin, and Jared A. Gollob. Irak4 degrader in hidradenitis suppurativa and atopic dermatitis: a phase 1 trial. Nature Medicine, 29:3127-3136, Nov 2023. URL: https://doi.org/10.1038/s41591-023-02635-7, doi:10.1038/s41591-023-02635-7. This article has 104 citations and is from a highest quality peer-reviewed journal.

26. (yu2024skinimmunemesenchymalinterplay pages 30-36): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

27. (jin2023epigeneticswitchreshapes pages 3-5): Lin Jin, Yunjia Chen, Suhail Muzaffar, Chao Li, Carlos A. Mier-Aguilar, Jasim Khan, Mahendra P. Kashyap, Shanrun Liu, Ritesh Srivastava, Jessy S. Deshane, Tim M. Townes, Boni E. Elewski, Craig A. Elmets, David K. Crossman, Chander Raman, and Mohammad Athar. Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. Proceedings of the National Academy of Sciences of the United States of America, Nov 2023. URL: https://doi.org/10.1073/pnas.2315096120, doi:10.1073/pnas.2315096120. This article has 31 citations and is from a highest quality peer-reviewed journal.

28. (yu2024skinimmunemesenchymalinterplay media 3233e121): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

29. (yu2024skinimmunemesenchymalinterplay media 0432ca6a): Wei-Wen Yu, Joy N.P. Barrett, Jie Tong, Meng-Ju Lin, Meaghan Marohn, Joseph C. Devlin, Alberto Herrera, Juliana Remark, Jamie Levine, Pei-Kang Liu, Victoria Fang, Abigail M. Zellmer, Derek A. Oldridge, E. John Wherry, Jia-Ren Lin, Jia-Yun Chen, Peter Sorger, Sandro Santagata, James G. Krueger, Kelly V. Ruggles, Fei Wang, Chang Su, Sergei B. Koralov, Jun Wang, Ernest S. Chiu, and Catherine P. Lu. Skin immune-mesenchymal interplay within tertiarylymphoid structures promotes autoimmunepathogenesis in hidradenitis suppurativa. Immunity, 57 12:2827-2842.e5, Dec 2024. URL: https://doi.org/10.1016/j.immuni.2024.11.010, doi:10.1016/j.immuni.2024.11.010. This article has 30 citations and is from a highest quality peer-reviewed journal.

30. (NCT05905783 chunk 1):  Hidradenitis Suppurativa Study of Izokibep. ACELYRIN Inc.. 2023. ClinicalTrials.gov Identifier: NCT05905783

31. (NCT05355805 chunk 1):  Hidradenitis Suppurativa Phase 2b Study of Izokibep. ACELYRIN Inc.. 2022. ClinicalTrials.gov Identifier: NCT05355805

32. (liao2024cellularindexingof pages 14-16): Wilson Liao, Sugandh Kumar, Faye Orcales, Bobby Shih, Xiaohui Fang, Congcong Yin, Ashley Yates, Peter Dimitrion, Isaac Neuhaus, Chandler Johnson, Indra Adrianto, Antonia Wiala, Iltefat H. Hamzavi, Li Zhou, Haley Naik, Christian Posch, and Qing-Sheng Mi. Cellular indexing of transcriptomes and epitopes (cite-seq) in hidradenitis suppurativa identifies dysregulated cell types in peripheral blood and facilitates diagnosis via machine learning. Unknown journal, Sep 2024. URL: https://doi.org/10.21203/rs.3.rs-4791069/v1, doi:10.21203/rs.3.rs-4791069/v1.