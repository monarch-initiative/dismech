---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-07T05:20:00.740079'
end_time: '2026-03-07T05:30:53.936527'
duration_seconds: 653.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Coccidioidomycosis
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Coccidioidomycosis
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Coccidioidomycosis**.
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
- **Disease Name:** Coccidioidomycosis
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Coccidioidomycosis**.
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


## Disease Pathophysiology Research Report: Coccidioidomycosis (Valley fever)

### Target disease metadata
- **Disease name:** Coccidioidomycosis (Valley fever)
- **Etiologic agents:** *Coccidioides immitis* and *Coccidioides posadasii* (lim2024clinicalcharacteristicsand pages 1-2, fayed2024overviewofthea pages 1-2)
- **MONDO ID:** Not verified from retrieved sources in this run.
- **Category:** Endemic dimorphic fungal infection (primary pulmonary infection with potential for extrapulmonary dissemination) (lim2024clinicalcharacteristicsand pages 1-2, fayed2024overviewofthea pages 1-2)

---

## 1) Key concepts & definitions (current understanding)

### 1.1 Core definition and clinical spectrum
Coccidioidomycosis is acquired by inhalation of airborne *Coccidioides* arthroconidia and ranges from asymptomatic infection to severe pulmonary disease and disseminated infection (hsu2024theknownand pages 2-4, fayed2024overviewofthea pages 1-2). In a 2024 ICU cohort paper, the authors summarize that “about two-thirds of cases are asymptomatic or have mild respiratory symptoms” and that “1% to 3% present as disseminated infection” (lim2024clinicalcharacteristicsand pages 1-2).

### 1.2 Central pathophysiology concept: host–pathogen interaction shaped by fungal morphogenesis and immune polarization
A key unifying concept across recent reviews is that disease outcome depends on (i) in-host fungal morphogenesis (arthroconidia → spherules → endospores) and (ii) whether host immunity develops protective Th1/Th17 responses and organized containment (e.g., granulomas), versus immune evasion, Th2 skewing, or immunosuppression leading to persistence/dissemination (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, jackson2024fromsoilto pages 8-9, kirkland2024thehostresponse pages 14-16, fayed2024overviewofthea pages 2-6).

---

## 2) Core pathophysiology (molecular & cellular mechanisms)

### 2.1 Initiation: inhalation and morphogenesis in the lung
**Trigger:** inhalation of arthroconidia; incubation is reported as “one-to-three weeks” (Fayed et al., 2024; DOI:10.3390/jof10100724; published Oct 2024) (fayed2024overviewofthea pages 2-6).

**Morphogenetic switch:** Hsu (2024; DOI:10.3390/jof10040256; published Mar 2024) notes that inhaled “2–5 µm arthroconidia” can reach terminal bronchioles and “swell into spherules” that undergo endospore formation; developing spherules can secrete a metalloproteinase that contributes to immune masking, and “rupture of mature spherules triggers a rapid influx of immune cells” (hsu2024theknownand pages 1-2).

**Phagocytosis constraint:** spherules are largely extracellular, while “small round cells and endospores” are phagocytosed by neutrophils, dendritic cells, and macrophages (kirkland2024thehostresponsea pages 9-10).

### 2.2 Innate sensing and early immune programming
**Pattern recognition:** A 2024 clinical review summarizes that initial recognition involves PRRs including “Toll-like receptors (TLRs) and c-type lectin receptors (CLRs)” (fayed2024overviewofthea pages 2-6). 

**β-glucan sensing axis (Dectin-1/2 → CARD9):** In the 2024 host-response review (Kirkland et al., 2024; DOI:10.3390/jof10030173; published Feb 2024), Dectin-1 (CLEC7A) is highlighted as required for pro-inflammatory cytokine responses to spherules and for controlling fungal burden and Th1/Th17 cytokines in murine infection models (kirkland2024thehostresponsea pages 4-5). The granuloma-focused 2023 review states that β-1,3-glucan and SOWgp are detected by Dectin-1 signaling via MyD88 and CARD9, activating NFAT/NF-κB and pro-inflammatory cytokine production (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).

**Innate hyporesponsiveness to arthroconidia:** Kirkland et al. (2024) report that arthroconidia can bias macrophage differentiation toward noninflammatory “M0” macrophages and induce little dendritic cell activation, suggesting early immune programming may be suboptimal before spherule exposure (kirkland2024thehostresponsea pages 4-5).

**Oxidant biology beyond classical NADPH oxidase:** Whole-exome sequencing (WES) of disseminated cases in Kirkland et al. (2024) identified β-glucan sensing pathway defects (including CLEC7A and PLCG2) and enrichment of DUOX1/DUOXA1 mutations associated with reduced epithelial H2O2 responses to Dectin-1 agonists (kirkland2024thehostresponsea pages 9-10).

### 2.3 Adaptive immunity: Th1/Th17 dominance and cytokine axes
Multiple 2023–2024 sources converge on Th1/Th17 dominance as the protective response.

- Jackson et al. (2024; Microbiology and Molecular Biology Reviews; DOI:10.1128/mmbr.00161-23; published Dec 2024) notes that “a protective immune response is dominated by Th1/Th17 cells” and that loss of granuloma structure in immunocompromise can lead to fatal infection in mice (jackson2024fromsoilto pages 8-9).
- Fayed et al. (2024; DOI:10.3390/jof10100724) states that “Th1 and Th17 subtypes is particularly critical,” and specifically that “TNF-α… is essential for granuloma formation,” while IL-6/IL-21/TGF-β drive Th17 differentiation and IL-17 production (fayed2024overviewofthea pages 2-6).

**Human genetic evidence of Th1 axis importance:** In Kirkland et al. (2024), a dominant-negative STAT4 E626G mutation is described as reducing IFN-γ responses to IL-12/IL-18 (kirkland2024thehostresponsea pages 9-10). IL12RB1 deficiency is described in the same review with impaired IL-12 signaling and clinical improvement after IFN-γ treatment and subsequent IL-4/IL-13 blockade (dupilumab), supporting pathogenic relevance of Th1:Th2 imbalance in severe disseminated disease (kirkland2024thehostresponse pages 14-16).

### 2.4 Granuloma biology: containment versus breakdown
Granulomas are repeatedly emphasized as a major containment strategy.

- The 2023 granuloma review reports that granulomas form in “roughly 5% of infections” and can be necrotizing and cellularly complex, including neutrophils, macrophages, and lymphocytes (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).
- Spatial immune architecture in patient granulomas is described with CD14+ macrophages localized to granuloma cores and CD206+ macrophages present inside and around granulomas; CD14/CD206/IL-10/TNF-α enriched within granulomas (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).
- Jackson et al. (2024) highlights that immunocompromise can disrupt granuloma structure and lead to mortality in mice (jackson2024fromsoilto pages 8-9).

### 2.5 Immune evasion and immunopathology drivers
**SOWgp and protease-mediated immune masking:** Hsu (2024) reports a metalloproteinase secreted by developing spherules contributes to immune masking (hsu2024theknownand pages 1-2). The granuloma review emphasizes surface antigens such as SOWgp and their role in host recognition (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).

**Urease-mediated microenvironmental modulation:** The granuloma review describes urease/urea release competing with iNOS for L-arginine and promoting an alkalinized microenvironment, with downstream skewing toward anti-inflammatory cytokines (IL-10, IL-4, IL-13) and M2-like responses (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).

---

## 3) Key molecular players (host + fungal), cell types, tissues, chemicals

| Entity | Type | Ontology/ID | Role in Coccidioidomycosis Pathophysiology | Evidence/Citation Context IDs |
| :--- | :--- | :--- | :--- | :--- |
| **Dectin-1** (CLEC7A) | Host Gene/Protein | HGNC:14536 | Primary C-type lectin receptor for fungal $\beta$-1,3-glucan; deficiency leads to dissemination; critical for Th17/Th1 responses. | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponsea pages 9-10, kirkland2024thehostresponse pages 4-5, kirkland2024thehostresponsea pages 4-5) |
| **CARD9** | Host Gene/Protein | HGNC:16391 | Adaptor protein downstream of Dectin-1/2; essential for vaccine-induced protection and Th17 immunity. | (kirkland2024thehostresponse pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 4-5) |
| **STAT1** | Host Gene/Protein | HGNC:11362 | Transcription factor for IFN-$\gamma$ signaling; gain-of-function mutations modulate susceptibility. | (kirkland2024thehostresponse pages 9-10, hsu2024theknownand pages 18-20) |
| **STAT3** | Host Gene/Protein | HGNC:11364 | Transcription factor involved in Th17 differentiation; mutations linked to disseminated disease (Hyper-IgE). | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponseb pages 9-10, jackson2024fromsoilto pages 8-9, hsu2024theknownand pages 18-20) |
| **STAT4** | Host Gene/Protein | HGNC:11365 | Transcription factor for IL-12 signaling; E626G mutation reduces IFN-$\gamma$ response and increases susceptibility. | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponseb pages 9-10, jackson2024fromsoilto pages 8-9) |
| **IL12RB1** | Host Gene/Protein | HGNC:5970 | Receptor for IL-12; deficiency impairs IFN-$\gamma$ production, leading to severe disseminated infection. | (kirkland2024thehostresponse pages 14-16, hsu2024theknownand pages 18-20) |
| **IFN-$\gamma$** (IFNG) | Host Gene/Protein | HGNC:5438 | Cytokine driving Th1 responses and macrophage activation; critical for fungal clearance. | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponseb pages 9-10, kirkland2024thehostresponse pages 14-16, hsu2024theknownand pages 18-20) |
| **TNF-$\alpha$** (TNF) | Host Gene/Protein | HGNC:11892 | Pro-inflammatory cytokine essential for granuloma formation and maintenance. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 4-5, fayed2024overviewofthe pages 2-6) |
| **IL-17** (IL17A) | Host Gene/Protein | HGNC:5981 | Cytokine produced by Th17 cells; crucial for mucosal immunity and vaccine efficacy. | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponseb pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 4-5, fayed2024overviewofthe pages 2-6) |
| **SOWgp** | Fungal Factor | - | Spherule Outer Wall Glycoprotein; major surface antigen recognized by host; can be degraded by fungal metalloproteinase (Mep1) to evade detection. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10) |
| **Urease** | Fungal Factor | - | Enzyme producing ammonia/urea; alkalizes microenvironment to inhibit phagolysosome fusion. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10) |
| **Macrophage** | Cell Type | CL:0000235 | Phagocytes forming the core of granulomas; phenotype (M1 vs M2) influences clearance vs persistence. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 4-5) |
| **Th1 Cell** | Cell Type | CL:0000545 | CD4+ T cells producing IFN-$\gamma$; associated with effective disease resolution. | (kirkland2024thehostresponse pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 14-16) |
| **Th17 Cell** | Cell Type | CL:0000899 | CD4+ T cells producing IL-17; associated with vaccine protection and fungal control. | (kirkland2024thehostresponse pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 4-5, jackson2024fromsoilto pages 8-9) |
| **Lung** | Tissue | UBERON:0002048 | Primary site of infection (pulmonary coccidioidomycosis); site of spherule development and granuloma formation. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 4-5, lim2024clinicalcharacteristicsand pages 1-2) |
| **Meninges** | Tissue | UBERON:0002360 | Major site of extrapulmonary dissemination (coccidioidal meningitis); high mortality. | (lim2024clinicalcharacteristicsand pages 1-2) |
| **Meningitis** | Phenotype | HP:0001287 | Severe complication of disseminated infection; requires lifelong therapy. | (lim2024clinicalcharacteristicsand pages 1-2) |
| **Granuloma** | Phenotype | HP:0002955 | Organized immune structure to contain fungus; failure leads to dissemination. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, jackson2024fromsoilto pages 8-9, fayed2024overviewofthe pages 2-6) |
| **Beta-1,3-glucan** | Chemical | CHEBI:37671 | Fungal cell wall component recognized by Dectin-1; PAMP triggering innate immune response. | (kirkland2024thehostresponse pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10) |


*Table: This table maps key genes, proteins, fungal factors, cell types, tissues, and phenotypes involved in *Coccidioides* infection to standard ontology identifiers (HGNC, CL, UBERON, HP, CHEBI) where available, summarizing their pathophysiological roles and supporting evidence.*

### 3.1 Host genes/proteins implicated in susceptibility and protection (HGNC)
Evidence from WES and clinical immunogenetics in 2024 reviews implicates:
- **β-glucan sensing and CLR signaling:** **CLEC7A (Dectin-1)** and downstream signaling intermediates (e.g., PLCG2), with disseminated disease enrichment for CLEC7A mutations (kirkland2024thehostresponsea pages 9-10).
- **CARD9** (CLR adaptor) as critical for vaccine-induced Th17/IFN-γ responses and protection (kirkland2024thehostresponsea pages 4-5).
- **STAT4, STAT3, STAT1** as key transcriptional nodes in Th polarization and IFN-γ signaling; STAT4 mutation linked to impaired IFN-γ response; STAT3 mutations observed in disseminated disease cohorts (kirkland2024thehostresponsea pages 9-10).
- **IL12RB1** as a causal susceptibility locus in severe disseminated disease with impaired IL-12 signaling (kirkland2024thehostresponse pages 14-16).
- **DUOX1/DUOXA1** variants associated with reduced epithelial H2O2 responses to Dectin-1 agonists in disseminated disease cohorts (kirkland2024thehostresponsea pages 9-10).

### 3.2 Fungal determinants
Recent reviews highlight fungal attributes that shape immune recognition and persistence:
- **SOWgp (spherule outer wall glycoprotein):** a prominent surface antigen implicated in host recognition (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).
- **Metalloproteinase-mediated masking:** developing spherules secrete a metalloproteinase associated with immune masking (hsu2024theknownand pages 1-2).
- **Urease:** linked to altered local pH and macrophage polarization effects (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).
- **CPS1:** Jackson et al. (2024) describes CPS1 as a virulence-associated gene; Δcps1 is avirulent and can protect mice as a live attenuated vaccine strain (jackson2024fromsoilto pages 8-9).

### 3.3 Key cell types (CL) and anatomical sites (UBERON)
Primary infection occurs in the **lung (UBERON:0002048)** with early involvement of **alveolar macrophages, neutrophils, and dendritic cells**, followed by adaptive **Th1** and **Th17** responses (kirkland2024thehostresponsea pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10, fayed2024overviewofthea pages 2-6). Extrapulmonary dissemination targets include the **meninges (UBERON:0002360)** (coccidioidal meningitis) and musculoskeletal and other tissues (lim2024clinicalcharacteristicsand pages 1-2).

### 3.4 Chemical entities (CHEBI) and relevant small molecules/drugs
- **β-1,3-glucan (CHEBI:37671)** is a key fungal PAMP sensed via Dectin-1 pathways (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).
- **TNF-α inhibitors** and other immunosuppressive agents are repeatedly cited as increasing risk of severe/disseminated disease by suppressing critical antifungal defense mechanisms (fayed2024overviewofthea pages 2-6, hsu2024theknownand pages 18-20).
- **Dupilumab (IL-4/IL-13 blockade)** is described in an IL12RB1-deficiency case as normalizing Th1:Th2 balance with “dramatic clinical improvement” (kirkland2024thehostresponse pages 14-16).

---

## 4) Biological processes disrupted (GO-oriented)
The following biological processes are supported by the retrieved evidence as central to pathophysiology (process names provided in a GO-compatible style; specific GO IDs not asserted here because they were not present in the retrieved text):
- **Pattern recognition receptor signaling** (CLR/TLR-linked), including β-glucan sensing and downstream NF-κB-associated inflammatory gene programs (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, fayed2024overviewofthea pages 2-6).
- **Cytokine-mediated signaling** and **T-helper cell differentiation**, particularly Th1 (IFN-γ) and Th17 (IL-17) programs (fayed2024overviewofthea pages 2-6, jackson2024fromsoilto pages 8-9).
- **Granuloma organization / maintenance** and **chronic inflammatory response**, with TNF-α as a key mediator (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, fayed2024overviewofthea pages 2-6).
- **Reactive oxygen species (ROS) production** in epithelial and immune contexts (DUOX-related H2O2) linked to disseminated disease genetics (kirkland2024thehostresponsea pages 9-10).

---

## 5) Cellular components (where key processes occur)
Based on the mechanistic descriptions retrieved:
- **Cell surface / plasma membrane:** PRR engagement (e.g., Dectin-1/CLRs; TLRs) for sensing fungal PAMPs (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, fayed2024overviewofthea pages 2-6).
- **Nuclear compartment:** STAT transcription-factor signaling (STAT1/3/4) downstream of cytokine receptors shaping IFN-γ and Th differentiation programs (kirkland2024thehostresponsea pages 9-10, kirkland2024thehostresponse pages 14-16).
- **Extracellular space / tissue lesions:** extracellular spherules in host tissues and granuloma microenvironments (kirkland2024thehostresponsea pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10).

---

## 6) Disease progression model (sequence of events)

1. **Exposure and deposition in lung:** inhalation of arthroconidia; incubation ~1–3 weeks (fayed2024overviewofthea pages 2-6).
2. **Morphogenesis and immune masking:** arthroconidia swell into spherules, undergo endospore development; developing spherules secrete a metalloproteinase associated with immune masking (hsu2024theknownand pages 1-2).
3. **Innate sensing and early programming:** arthroconidia may elicit weak dendritic cell activation and M0 macrophage bias; later spherule β-glucans and surface antigens are recognized via CLRs (Dectin-1/2) and CARD9-linked signaling, promoting pro-inflammatory cytokines (kirkland2024thehostresponsea pages 4-5, miranda2023coccidioidomycosisgranulomasinformed pages 7-10).
4. **Spherule rupture and inflammatory influx:** mature spherule rupture drives rapid recruitment of immune cells (hsu2024theknownand pages 1-2).
5. **Adaptive immunity and containment:** protective responses dominated by Th1/Th17; TNF-α supports granuloma formation and integrity; granulomas may form in ~5% of infections (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, fayed2024overviewofthea pages 2-6).
6. **Outcomes:**
   - **Resolution** in most immunologically intact hosts (approximately two-thirds asymptomatic) (lim2024clinicalcharacteristicsand pages 1-2, hsu2024theknownand pages 2-4).
   - **Chronic pulmonary disease** in a subset; Hsu (2024) provides a conceptual breakdown (e.g., ~30% uncomplicated primary, ~5% chronic pulmonary, <1% extrapulmonary) (hsu2024theknownand pages 2-4).
   - **Dissemination** (skin/bone/CNS) when key immune axes fail (e.g., impaired CLR signaling, IL-12/IFN-γ axis defects, TNF blockade, low CD4 counts) (kirkland2024thehostresponsea pages 9-10, kirkland2024thehostresponse pages 14-16, hsu2024theknownand pages 18-20).

---

## 7) Phenotypic manifestations (HP-oriented) and mechanistic links

Key phenotypes include:
- **Primary pulmonary coccidioidomycosis** (pneumonia-like illness) (fayed2024overviewofthea pages 1-2).
- **Chronic pulmonary disease** (>12 months despite therapy) and complications such as cavitary disease (hsu2024theknownand pages 1-2, hsu2024theknownand pages 2-4).
- **Disseminated disease** including **meningitis (HP:0001287)** and musculoskeletal disease (lim2024clinicalcharacteristicsand pages 1-2, hsu2024theknownand pages 2-4).
- **Granulomatous inflammation / granuloma (HP:0002955)** as a tissue-level containment phenotype (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).

Mechanistic links:
- **Th1/IFN-γ deficiency or signaling impairment** (e.g., STAT4, IL12RB1-related) is associated with severe/disseminated phenotypes (kirkland2024thehostresponsea pages 9-10, kirkland2024thehostresponse pages 14-16).
- **TNF-α suppression** (biologics) undermines granuloma formation/maintenance and increases risk of severe disease (fayed2024overviewofthea pages 2-6, hsu2024theknownand pages 18-20).

---

## 8) Recent developments and latest research (prioritize 2023–2024)

### 8.1 Human genetics and “experiments of nature”
Kirkland et al. (Feb 2024) reports WES signals in disseminated disease implicating **β-glucan sensing (CLEC7A/Dectin-1; PLCG2)** and epithelial ROS pathways (**DUOX1/DUOXA1**) (kirkland2024thehostresponsea pages 9-10). These findings reinforce the mechanistic importance of early CLR signaling and mucosal oxidant biology in preventing dissemination (kirkland2024thehostresponsea pages 9-10).

### 8.2 Granuloma microenvironment and cellular ecology
The 2023 granuloma review compiles emerging human tissue evidence describing heterogeneous granuloma morphology and macrophage subset localization (CD14+ core; CD206+ internal/peripheral), and mixed cytokine enrichment within granulomas (miranda2023coccidioidomycosisgranulomasinformed pages 7-10). This supports a microenvironment-driven model in which macrophage polarization states and cytokine milieu influence containment versus persistence (miranda2023coccidioidomycosisgranulomasinformed pages 7-10).

### 8.3 Vaccine-relevant advances
Jackson et al. (Dec 2024) highlights virulence-associated genes and vaccine concepts including **Δcps1** live attenuated strains (avirulent yet immunogenic) and emphasizes Th1/Th17 dominance for protective immunity (jackson2024fromsoilto pages 8-9). Kirkland et al. (Feb 2024) summarizes that spherule preparations and live attenuated mutants that form sterile spherules can be protective in animals (kirkland2024thehostresponse pages 14-16).

---

## 9) Current applications and real-world implementations (2024 emphasis)

### 9.1 Diagnostics and testing: current practice and performance
**Serology as first line:** Fayed et al. (Oct 2024) describes EIA IgM/IgG, immunodiffusion, and complement fixation as standard serologic modalities, noting IgM detectability “within roughly 1-to-3 weeks of symptom onset” and emphasizing that EIAs can vary and “should not be used for definitive assessment” (fayed2024overviewofthea pages 13-15, fayed2024overviewofthe pages 13-15).

**Culture and histopathology:** Culture is described as gold standard but with poor sensitivity “around 50%” and BSL-3 handling requirements (fayed2024overviewofthea pages 15-17). Histopathology can show spherules directly (fayed2024overviewofthe pages 15-17).

**PCR and FDA-cleared BAL testing:** Fayed et al. (2024) reports FDA approval of GenStat for detecting *Coccidioides* DNA from BAL/BW and describes a center’s PCR performance with “100% specificity” and sample-type dependent sensitivities (e.g., BAL 91%, sputum 94%, CSF 59%) (fayed2024overviewofthea pages 15-17).

**Large-scale real-world testing statistics (commercial laboratory):** Benedict et al. (Aug 2024; DOI:10.1093/ofid/ofae448) reports 2019–2024 volumes and positivity for *Coccidioides* EIAs: **154,989 IgM results (5% positive)** and **154,968 IgG results (8% positive)** (benedict2024testingforblastomycosis pages 1-2, benedict2024testingforblastomycosis pages 2-3). Turnaround time was median 1 day (IQR 1–3) overall, with regional variation (benedict2024testingforblastomycosis pages 2-3).

### 9.2 Severe disease management context: ICU outcomes
In a multicenter ICU cohort of 145 culture-proven cases (Arizona; 2017–2022), **48% died during hospitalization**; 72% had pulmonary disease and 28% extrapulmonary disease including meningitis (n=17) and fungemia (n=13) (Lim et al., Aug 2024; DOI:10.1093/ofid/ofae454) (lim2024clinicalcharacteristicsand pages 1-2).

---

## 10) Relevant statistics and data (recent sources)

- **Estimated annual infections:** ~150,000 infections/year are cited in Hsu (2024) (hsu2024theknownand pages 1-2).
- **Dissemination frequency (population-level estimate):** Hsu (2024) reports dissemination in ~600–1000 cases/year (0.4–0.6%) (hsu2024theknownand pages 1-2).
- **Reported case burden:** a 2024 clinical review cites CDC estimates of **10,000–20,000 reported U.S. cases yearly**, mostly in Arizona and California (fayed2024overviewofthea pages 1-2).
- **Incidence trends:** Hsu (2024) reports increases in reported incidence (e.g., 5.3/100,000 in 1998 to 42.6/100,000 in 2011; Arizona 84.4/100,000 in 2014 to 144.1/100,000 in 2019) (hsu2024theknownand pages 2-4).
- **Commercial-lab EIA positivity:** IgM 5% positive; IgG 8% positive in 2019–2024 dataset (benedict2024testingforblastomycosis pages 1-2).
- **ICU mortality:** 48% in culture-proven ICU cohort (lim2024clinicalcharacteristicsand pages 1-2).

---

## 11) Expert opinions and authoritative analysis (2023–2024)

- **Consensus immune model:** Recent authoritative reviews emphasize that protective immunity is dominated by Th1/Th17 programs, and that immunosuppression (notably TNF-α blockade) increases risk of severe/disseminated disease by compromising granuloma formation and antifungal T-cell responses (jackson2024fromsoilto pages 8-9, fayed2024overviewofthea pages 2-6, hsu2024theknownand pages 18-20).
- **Genetic susceptibility framing:** Hsu (2024) cautions that some historically repeated risk factors are not strongly supported, while specific genetic variants and TNF-inhibitor–associated immunosuppression have stronger validation in later cohort studies (hsu2024theknownand pages 1-2).

---

## 12) Knowledge-base-ready annotations (evidence-linked)

### 12.1 Pathophysiology description (narrative)
Coccidioidomycosis begins when inhaled 2–5 µm arthroconidia reach distal airways and, if not cleared, swell into spherules that form endospores; developing spherules may secrete a metalloproteinase linked to immune masking, while rupture of mature spherules triggers strong inflammatory influx (hsu2024theknownand pages 1-2). Early innate responses can be blunted by arthroconidia (limited DC activation and M0 macrophage bias), but spherules expose β-glucan and antigens sensed by CLRs (notably Dectin-1/2) and CARD9-linked signaling, supporting inflammatory cytokines that prime Th1/Th17 adaptive immunity (kirkland2024thehostresponsea pages 4-5, miranda2023coccidioidomycosisgranulomasinformed pages 7-10). Protective control is associated with Th1 and Th17 programs (IFN-γ, IL-17) and TNF-α-mediated granuloma formation; breakdown of granuloma structure in immunocompromise predisposes to progression and dissemination (jackson2024fromsoilto pages 8-9, fayed2024overviewofthea pages 2-6). Dissemination risk is amplified by immunosuppression and by inborn errors affecting CLR signaling and IL-12/IFN-γ pathways (e.g., CLEC7A, IL12RB1, STAT4), and by epithelial oxidant response defects (DUOX1/DUOXA1) (kirkland2024thehostresponsea pages 9-10, kirkland2024thehostresponse pages 14-16).

### 12.2 Evidence-linked mechanism summary
| Mechanism / Stage | Key Host Pathways (Genes/Proteins) | Key Fungal Factors | Key Cell Types | Key Tissues | Evidence / Description | Key Citations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Innate Recognition** | Dectin-1 (*CLEC7A*), Dectin-2 (*CLEC6A*), CARD9, MyD88, Syk-JNK, NLRP3, IL-1R1 | $\beta$-1,3-glucan (exposed on spherules), SOWgp | Macrophages, Dendritic Cells (DCs), Neutrophils | Lung (Alveoli) | Dectin-1 is the primary receptor for spherule recognition; Dectin-2/CARD9 axis drives Th17 vaccine immunity; Arthroconidia often induce poor activation (M0 bias). | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponsea pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 4-5, kirkland2024thehostresponsea pages 4-5) |
| **Fungal Morphogenesis & Evasion** | iNOS (competed by fungal arginase) | SOWgp, Metalloproteinase (Mep1), Urease, CPS1 | Neutrophils, Macrophages | Lung | Spherules grow too large for phagocytosis; Mep1 digests immunogenic SOWgp; Urease alkalizes local pH to inhibit phagolysosomes; CPS1 required for virulence. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, jackson2024fromsoilto pages 8-9, hsu2024theknownand pages 1-2, fayed2024overviewofthe pages 2-6) |
| **Adaptive Immunity (Control)** | IFN-$\gamma$, IL-17, TNF-$\alpha$, IL-12/IL-23 axis, STAT1, STAT3, STAT4 | Spherule antigens (e.g., Ag2/Prp2) | Th1 Cells, Th17 Cells, B cells | Lung, Lymph Nodes | Robust Th1 (IFN-$\gamma$) and Th17 (IL-17) responses are required for clearance; Th2 skewing or low CD4+ count increases dissemination risk. | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponseb pages 9-10, miranda2023coccidioidomycosisgranulomasinformed pages 7-10, kirkland2024thehostresponse pages 14-16, hsu2024theknownand pages 18-20) |
| **Granuloma Formation** | TNF-$\alpha$, IFN-$\gamma$ | Persistent fungal antigens | Macrophages (CD14+ core, CD206+ mantle), T cells | Lung | Granulomas form in ~5% of infections to contain fungi; TNF-$\alpha$ is essential for maintenance; breakdown leads to reactivation/spread. | (miranda2023coccidioidomycosisgranulomasinformed pages 7-10, jackson2024fromsoilto pages 8-9, fayed2024overviewofthe pages 2-6) |
| **Dissemination & Susceptibility** | *IL12RB1*, *IFNGR1*, *STAT1*, *STAT3*, *STAT4*, *CLEC7A*, *DUOX1/DUOXA1* | Spherules/Endospores | Th1/Th17 Cells, Monocytes | Meninges, Skin, Bone, Liver | Genetic defects in IL-12/IFN-$\gamma$ loop or Dectin-1 increase dissemination; Biologic suppression (TNF blockers) is a major risk; Pregnancy and specific ancestries (Black, Filipino) elevate risk. | (kirkland2024thehostresponse pages 9-10, kirkland2024thehostresponsea pages 9-10, kirkland2024thehostresponsea pages 4-5, lim2024clinicalcharacteristicsand pages 1-2, hsu2024theknownand pages 18-20) |


*Table: Summary of key mechanisms, molecular players, and evidence underlying the host-pathogen interaction in *Coccidioides* infection.*

### 12.3 Visual evidence from a 2024 source
Kirkland et al. (2024) includes a gene-expression network figure highlighting key inflammatory/signaling nodes (e.g., STAT1, TNF-α, IL-6, IRF1) relevant to the immune programs discussed above (kirkland2024thehostresponse media b6399fc9).

---

## 13) URLs and publication dates (for key 2023–2024 sources used)
- Kirkland et al. **“The Host Response to Coccidioidomycosis”** (Journal of Fungi), **Feb 2024**, https://doi.org/10.3390/jof10030173 (kirkland2024thehostresponsea pages 9-10)
- Hsu **“The Known and Unknown ‘Knowns’ of Human Susceptibility to Coccidioidomycosis”** (Journal of Fungi), **Mar 2024**, https://doi.org/10.3390/jof10040256 (hsu2024theknownand pages 1-2)
- Jackson et al. **“From soil to clinic: current advances in understanding Coccidioides and coccidioidomycosis”** (Microbiology and Molecular Biology Reviews), **Dec 2024**, https://doi.org/10.1128/mmbr.00161-23 (jackson2024fromsoilto pages 8-9)
- Fayed et al. **“Overview of the Current Challenges in Pulmonary Coccidioidomycosis”** (Journal of Fungi), **Oct 2024**, https://doi.org/10.3390/jof10100724 (fayed2024overviewofthea pages 1-2)
- Lim et al. **“Clinical Characteristics and Mortality Risks… Critically Ill”** (Open Forum Infectious Diseases), **Aug 2024**, https://doi.org/10.1093/ofid/ofae454 (lim2024clinicalcharacteristicsand pages 1-2)
- Benedict et al. **“Testing for Blastomycosis, Coccidioidomycosis, and Histoplasmosis… 2019–2024”** (Open Forum Infectious Diseases), **Aug 2024**, https://doi.org/10.1093/ofid/ofae448 (benedict2024testingforblastomycosis pages 1-2)
- Miranda & Hoyer **“Coccidioidomycosis Granulomas Informed by Other Diseases”** (Journal of Fungi), **Jun 2023**, https://doi.org/10.3390/jof9060650 (miranda2023coccidioidomycosisgranulomasinformed pages 7-10)

---

## Notes on PMIDs
The retrieved full-text excerpts did not expose PubMed identifiers (PMIDs) for most mechanistic claims. Where PMIDs are required for a downstream knowledge base, the DOIs above provide a reliable route to PubMed records; however, I did not extract PMIDs directly from the available evidence snippets in this run.

References

1. (lim2024clinicalcharacteristicsand pages 1-2): James Lim, Ashley M Scott, Rebecca Wig, Rachel V Tan, Emily R Harnois, Tirdad T Zangeneh, and Mohanad M Al-Obaidi. Clinical characteristics and mortality risks among patients with culture-proven coccidioidomycosis who are critically ill: a multicenter study in an endemic region. Open Forum Infectious Diseases, Aug 2024. URL: https://doi.org/10.1093/ofid/ofae454, doi:10.1093/ofid/ofae454. This article has 9 citations and is from a peer-reviewed journal.

2. (fayed2024overviewofthea pages 1-2): Mohamed A. Fayed, Timothy M. Evans, Eyad Almasri, Kathryn L. Bilello, Robert Libke, and Michael W. Peterson. Overview of the current challenges in pulmonary coccidioidomycosis. Journal of Fungi, 10:724, Oct 2024. URL: https://doi.org/10.3390/jof10100724, doi:10.3390/jof10100724. This article has 4 citations.

3. (hsu2024theknownand pages 2-4): Amy P. Hsu. The known and unknown “knowns” of human susceptibility to coccidioidomycosis. Journal of Fungi, 10:256, Mar 2024. URL: https://doi.org/10.3390/jof10040256, doi:10.3390/jof10040256. This article has 4 citations.

4. (miranda2023coccidioidomycosisgranulomasinformed pages 7-10): Nadia Miranda and Katrina K. Hoyer. Coccidioidomycosis granulomas informed by other diseases: advancements, gaps, and challenges. Journal of Fungi, 9:650, Jun 2023. URL: https://doi.org/10.3390/jof9060650, doi:10.3390/jof9060650. This article has 9 citations.

5. (jackson2024fromsoilto pages 8-9): Katrina M. Jackson, Marcus de Melo Teixeira, and Bridget M. Barker. From soil to clinic: current advances in understanding <i>coccidioides</i> and coccidioidomycosis. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00161-23, doi:10.1128/mmbr.00161-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

6. (kirkland2024thehostresponse pages 14-16): TN Kirkland, CY Hung, LF Shubitz, S Beyhan, and J Fierer. The host response to coccidioidomycosis. j. fungi 2024, 10, 173. Unknown journal, 2024.

7. (fayed2024overviewofthea pages 2-6): Mohamed A. Fayed, Timothy M. Evans, Eyad Almasri, Kathryn L. Bilello, Robert Libke, and Michael W. Peterson. Overview of the current challenges in pulmonary coccidioidomycosis. Journal of Fungi, 10:724, Oct 2024. URL: https://doi.org/10.3390/jof10100724, doi:10.3390/jof10100724. This article has 4 citations.

8. (hsu2024theknownand pages 1-2): Amy P. Hsu. The known and unknown “knowns” of human susceptibility to coccidioidomycosis. Journal of Fungi, 10:256, Mar 2024. URL: https://doi.org/10.3390/jof10040256, doi:10.3390/jof10040256. This article has 4 citations.

9. (kirkland2024thehostresponsea pages 9-10): Theo N. Kirkland, Chiung-Yu Hung, Lisa F. Shubitz, Sinem Beyhan, and Joshua Fierer. The host response to coccidioidomycosis. Journal of Fungi, 10:173, Feb 2024. URL: https://doi.org/10.3390/jof10030173, doi:10.3390/jof10030173. This article has 5 citations.

10. (kirkland2024thehostresponsea pages 4-5): Theo N. Kirkland, Chiung-Yu Hung, Lisa F. Shubitz, Sinem Beyhan, and Joshua Fierer. The host response to coccidioidomycosis. Journal of Fungi, 10:173, Feb 2024. URL: https://doi.org/10.3390/jof10030173, doi:10.3390/jof10030173. This article has 5 citations.

11. (kirkland2024thehostresponse pages 9-10): TN Kirkland, CY Hung, LF Shubitz, S Beyhan, and J Fierer. The host response to coccidioidomycosis. j. fungi 2024, 10, 173. Unknown journal, 2024.

12. (kirkland2024thehostresponse pages 4-5): TN Kirkland, CY Hung, LF Shubitz, S Beyhan, and J Fierer. The host response to coccidioidomycosis. j. fungi 2024, 10, 173. Unknown journal, 2024.

13. (hsu2024theknownand pages 18-20): Amy P. Hsu. The known and unknown “knowns” of human susceptibility to coccidioidomycosis. Journal of Fungi, 10:256, Mar 2024. URL: https://doi.org/10.3390/jof10040256, doi:10.3390/jof10040256. This article has 4 citations.

14. (kirkland2024thehostresponseb pages 9-10): TN Kirkland, CY Hung, LF Shubitz, S Beyhan, and J Fierer. The host response to coccidioidomycosis. j. fungi 2024, 10, 173. Unknown journal, 2024.

15. (fayed2024overviewofthe pages 2-6): MA Fayed, TM Evans, E Almasri, KL Bilello, and R Libke. Overview of the current challenges in pulmonary coccidioidomycosis. j. fungi 2024, 10, 724. Unknown journal, 2024.

16. (fayed2024overviewofthea pages 13-15): Mohamed A. Fayed, Timothy M. Evans, Eyad Almasri, Kathryn L. Bilello, Robert Libke, and Michael W. Peterson. Overview of the current challenges in pulmonary coccidioidomycosis. Journal of Fungi, 10:724, Oct 2024. URL: https://doi.org/10.3390/jof10100724, doi:10.3390/jof10100724. This article has 4 citations.

17. (fayed2024overviewofthe pages 13-15): MA Fayed, TM Evans, E Almasri, KL Bilello, and R Libke. Overview of the current challenges in pulmonary coccidioidomycosis. j. fungi 2024, 10, 724. Unknown journal, 2024.

18. (fayed2024overviewofthea pages 15-17): Mohamed A. Fayed, Timothy M. Evans, Eyad Almasri, Kathryn L. Bilello, Robert Libke, and Michael W. Peterson. Overview of the current challenges in pulmonary coccidioidomycosis. Journal of Fungi, 10:724, Oct 2024. URL: https://doi.org/10.3390/jof10100724, doi:10.3390/jof10100724. This article has 4 citations.

19. (fayed2024overviewofthe pages 15-17): MA Fayed, TM Evans, E Almasri, KL Bilello, and R Libke. Overview of the current challenges in pulmonary coccidioidomycosis. j. fungi 2024, 10, 724. Unknown journal, 2024.

20. (benedict2024testingforblastomycosis pages 1-2): Kaitlin Benedict, Samantha L Williams, Dallas J Smith, Mark D Lindsley, Shawn R Lockhart, and Mitsuru Toda. Testing for blastomycosis, coccidioidomycosis, and histoplasmosis at a major commercial laboratory, united states, 2019-2024. Open forum infectious diseases, 11 8:ofae448, Aug 2024. URL: https://doi.org/10.1093/ofid/ofae448, doi:10.1093/ofid/ofae448. This article has 4 citations and is from a peer-reviewed journal.

21. (benedict2024testingforblastomycosis pages 2-3): Kaitlin Benedict, Samantha L Williams, Dallas J Smith, Mark D Lindsley, Shawn R Lockhart, and Mitsuru Toda. Testing for blastomycosis, coccidioidomycosis, and histoplasmosis at a major commercial laboratory, united states, 2019-2024. Open forum infectious diseases, 11 8:ofae448, Aug 2024. URL: https://doi.org/10.1093/ofid/ofae448, doi:10.1093/ofid/ofae448. This article has 4 citations and is from a peer-reviewed journal.

22. (kirkland2024thehostresponse media b6399fc9): Theo N. Kirkland, Chiung-Yu Hung, Lisa F. Shubitz, Sinem Beyhan, and Joshua Fierer. The host response to coccidioidomycosis. Journal of Fungi, 10:173, Feb 2024. URL: https://doi.org/10.3390/jof10030173, doi:10.3390/jof10030173. This article has 5 citations.