---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:47:02.116641'
end_time: '2025-12-18T09:55:23.467538'
duration_seconds: 501.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autoimmune Hemolytic Anemia
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Autoimmune Hemolytic Anemia
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Autoimmune Hemolytic Anemia**.
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
- **Disease Name:** Autoimmune Hemolytic Anemia
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Autoimmune Hemolytic Anemia**.
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


Disease Pathophysiology Research Report – Autoimmune Hemolytic Anemia (AIHA)

Target Disease
- Disease Name: Autoimmune Hemolytic Anemia (AIHA)
- MONDO ID: MONDO:0007995 (autoimmune hemolytic anemia; cross-check recommended for downstream KB ingestion)
- Category: Autoimmune

Pathophysiology overview (current understanding)
AIHA comprises immune-mediated destruction of red blood cells (RBCs) driven by autoantibodies with or without complement, with contributions from Fcγ receptor-mediated effector pathways, dysregulated complement activation, and inadequate bone-marrow compensation. The direct antiglobulin test (DAT/Coombs) distinguishes subtypes by RBC-bound IgG and/or complement (C3d). Warm AIHA (wAIHA) is usually IgG-mediated and dominated by splenic extravascular hemolysis through Fcγ receptor-dependent erythrophagocytosis; cold agglutinin disease (CAD) is typically driven by monoclonal IgM that agglutinates RBCs and potently activates the classical complement pathway, favoring C3b opsonization and hepatic clearance (with variable intravascular hemolysis). Mixed AIHA exhibits both warm IgG and clinically significant cold IgM; paroxysmal cold hemoglobinuria (PCH) features a biphasic cold-reactive IgG (Donath–Landsteiner antibody) that binds in the cold, fixes complement, and lyses RBCs on rewarming via complement. These immune effector cascades are orchestrated by a broader breakdown of immune tolerance, including altered CD4+ T-cell compartments (Tfh/Treg imbalance) and B-cell dysregulation (e.g., BAFF support), which sustain autoantibody production and diversify effector mechanisms (ADCP, ADCC, CDC) (URLs and dates: Barcellini & Fattizzo, Aug 2024, https://doi.org/10.1159/000540475; Loriamini et al., Apr 2024, https://doi.org/10.3390/ijms25084296; Costa et al., Jul 2025, https://doi.org/10.3389/fimmu.2025.1624667; Kostić et al., Mar 2024, https://doi.org/10.5633/amm.2024.0108) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, costa2025beneaththesurface pages 1-2, kostic2024cd4+tcell pages 1-2).

1) Core Pathophysiology
- Primary mechanisms: RBC autoantibodies bind antigens (commonly band 3/SLC4A1 and Rh complex) and trigger either FcγR-mediated macrophage phagocytosis (extravascular hemolysis; spleen predominance) or classical complement activation (C1q→C1s→C4/C2→C3b deposition; hepatic Kupffer cell clearance) with terminal cascade activation variably producing MAC-mediated intravascular hemolysis. “Warm” IgG (IgG1/IgG3) favors FcγR pathways; cold IgM more strongly activates complement, with C3d-only DAT findings in CAD. Mixed AIHA shows both IgG and C3d on DAT; PCH shows C3d-only DAT and Donath–Landsteiner positivity (URLs/dates: 2024–2025 sources above) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, costa2025beneaththesurface pages 2-3, costa2025beneaththesurface pages 1-2, kostic2024cd4+tcell pages 1-2).
- Dysregulated pathways: FcγR signaling on splenic macrophages (FcγRIIA/IIIa), classical complement pathway (C1q/C1s → C4/C2 → C3b; sometimes C5b-9), ADCC via NK cells, and inefficient erythropoietic compensation in marrow, producing variability in reticulocytosis and severity (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Cellular processes affected: erythrophagocytosis, complement opsonization and lysis, RBC agglutination (cold), ADCC, and marrow erythropoietic response; clinically, extravascular hemolysis yields unconjugated hyperbilirubinemia; intravascular hemolysis yields higher LDH and hemoglobinemia/haptoglobin depletion (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5).

2) Key Molecular Players
- Genes/Proteins (HGNC): Fcγ receptors (FCGR2A/FCGR3A) mediate IgG-opsonized RBC clearance; complement initiators and effectors (C1Q, C1S, C3, C5) mediate opsonization and MAC; RBC antigens commonly targeted include SLC4A1 (band 3) and Rh antigens (RHD/RHCE) (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 1-2, barcellini2020newinsightsin pages 1-3, kostic2024cd4+tcell pages 1-2).
- Chemical entities (CHEBI/drugs): pathogenic immunoglobulins (IgG, IgM); hemolysis metabolites (heme, bilirubin). Targeted therapeutics include rituximab (anti‑CD20), sutimlimab (anti‑C1s), riliprubart (anti‑C1s, early), eculizumab (anti‑C5), fostamatinib (SYK inhibitor), ibrutinib (BTK inhibitor), FcRn blockers (e.g., nipocalimab), daratumumab (anti‑CD38). Real-world implementation includes FDA/EMA‑approved sutimlimab for CAD with long-term efficacy shown in 2024, and growing observational evidence for daratumumab in refractory AIHA (URLs/dates: RÖth et al., eClinicalMedicine, Aug 2024, https://doi.org/10.1016/j.eclinm.2024.102733; JADPRO review Sep 2024, https://doi.org/10.6004/jadpro.2024.15.6.4; Barcellini & Fattizzo Aug 2024; Jalink et al., Blood Advances, May 2024, https://doi.org/10.1182/bloodadvances.2024012585) (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 2-3, costa2025beneaththesurface pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Cell types (CL): splenic red pulp macrophages (FcγR+), hepatic Kupffer cells (complement receptor-mediated clearance), autoreactive B cells/plasma cells (autoantibody production), Tfh (germinal center help), Treg (tolerance), NK cells (ADCC) (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, kostic2024cd4+tcell pages 1-2).
- Anatomical locations (UBERON): spleen (extravascular FcγR-mediated hemolysis), liver (Kupffer cell-mediated clearance of C3-opsonized RBCs), bone marrow (compensation/reticulocytosis), peripheral blood (site of agglutination; hemolysis biomarkers) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 7-8).

3) Biological Processes (GO, disrupted in AIHA)
- Classical complement activation; complement-dependent cytotoxicity (CDC); C3b opsonization and C3d deposition (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2).
- FcγR-mediated phagocytosis/antibody-dependent cellular phagocytosis (ADCP) in spleen; antibody-dependent cellular cytotoxicity (ADCC) (costa2025beneaththesurface pages 2-3, kostic2024cd4+tcell pages 1-2).
- Erythrophagocytosis and RBC agglutination; marrow erythropoietic compensation (often inadequate in severe disease) (costa2025beneaththesurface pages 2-3, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Immune tolerance breakdown: Tfh/Treg imbalance; B-cell survival signaling (BAFF) promoting autoreactive clones and class-switched antibodies (kostic2024cd4+tcell pages 1-2, barcellini2020newinsightsin pages 1-3).

4) Cellular Components (GO, key sites)
- RBC plasma membrane (autoantigen display; complement deposition); membrane attack complex on RBCs in intravascular hemolysis (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 2-3).
- Splenic macrophage phagolysosomes (RBC degradation after FcγR-mediated uptake) (costa2025beneaththesurface pages 2-3).
- Hepatic Kupffer cell surface and phagosomes (complement receptor-mediated uptake of C3‑opsonized RBCs) (loriamini2024autoimmunehemolyticanemiasa pages 4-5, barcellini2024autoimmunehemolyticanemias pages 1-2).

5) Disease Progression Model (sequence of events)
- Trigger and tolerance loss: infection, autoimmune milieu, or lymphoproliferative disease prompts dysregulated Tfh/Treg axes and BAFF-driven B-cell survival; clonal monoclonal IgM arises in CAD (a distinct B-cell lymphoproliferative disorder) (costa2025beneaththesurface pages 2-3, kostic2024cd4+tcell pages 1-2).
- Autoantibody generation: warm IgG (wAIHA) versus cold IgM (CAD); in PCH, biphasic IgG binds cold then fixes complement on rewarming (Donath–Landsteiner) (loriamini2024autoimmunehemolyticanemiasa pages 4-5, kostic2024cd4+tcell pages 1-2).
- Effector triggering: FcγR-mediated erythrophagocytosis (extravascular, spleen) vs classical complement activation (C1q/C1s→C3b) leading to hepatic (Kupffer) extravascular clearance and possibly terminal pathway (C5b-9) intravascular hemolysis (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2).
- Clinical manifestation: anemia, jaundice (unconjugated bilirubin), elevated LDH, low haptoglobin; cold-induced acrocyanosis/Raynaud-like circulatory symptoms in CAD; hemoglobinuria in intravascular hemolysis (often PCH, some CAD/mixed) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5).
- Modifiers: bone-marrow compensation (reticulocytosis) may be inadequate in severe/relapsing disease and portends worse outcomes (loriamini2024autoimmunehemolyticanemiasa pages 7-8).

6) Phenotypic Manifestations (HPO links)
- Anemia with reticulocytosis or reticulocytopenia; jaundice (unconjugated hyperbilirubinemia); splenomegaly; acrocyanosis and cold-induced circulatory symptoms in CAD; hemoglobinuria in intravascular hemolysis; fatigue, dyspnea on exertion, pallor. Laboratory triad: elevated LDH, low haptoglobin, indirect hyperbilirubinemia, with DAT pattern defining subtype (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, costa2025beneaththesurface pages 2-3).

Key quotes (recent authoritative sources)
- “Warm AIHA… is mediated by IgG autoantibodies… [and] hemolysis is predominantly extravascular in the spleen via opsonization and phagocytosis by red pulp macrophages through Fcγ receptors.” (Barcellini & Fattizzo 2024, Aug 2024) (barcellini2024autoimmunehemolyticanemias pages 1-2).
- “Cold AIHA/CAD is primarily IgM-mediated: pentameric IgM targets the I antigen, promotes red cell agglutination, and potently activates classical complement… causing predominantly liver-based extravascular and variable intravascular hemolysis.” (Costa et al., Jul 2025) (costa2025beneaththesurface pages 2-3).
- “PCH… [is] driven by a biphasic cold-reactive IgG that recruits complement… with a DAT positive only for C3d.” (Loriamini et al., Apr 2024) (loriamini2024autoimmunehemolyticanemiasa pages 1-2).
- “No validated predictors for severe clinical course… [and] novel complement inhibitors, such as sutimlimab, [are] emerging.” (Mulder et al., Sep 2023) (loriamini2024autoimmunehemolyticanemiasa pages 7-8).

Recent developments and latest research (2023–2024 priority)
- Complement C1s inhibition in CAD: Long-term data from CADENZA Part B show sustained efficacy and safety of sutimlimab, reinforcing the mechanistic role of classical pathway activation in CAD and demonstrating real-world durability of complement blockade (eClinicalMedicine, Aug 2024, https://doi.org/10.1016/j.eclinm.2024.102733) (barcellini2024autoimmunehemolyticanemias pages 1-2).
- Practice-focused summary: 2024 JADPRO review details sutimlimab’s first-in-class C1s mechanism and clinical outcomes in CAD, aligning with guideline adoption and payer coverage evolution (Sep 2024, https://doi.org/10.6004/jadpro.2024.15.6.4) (barcellini2024autoimmunehemolyticanemias pages 1-2).
- Plasma-cell targeting in refractory disease: 2024 multicenter series shows daratumumab monotherapy can improve hemolysis and cold-induced symptoms in more than half of refractory wAIHA/CAD patients, highlighting plasma cells in persistence of autoantibody production (Blood Advances, May 2024, https://doi.org/10.1182/bloodadvances.2024012585) (loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Updated pathogenesis framing: 2024–2025 peer-reviewed reviews emphasize an integrated network of innate/adaptive immune dysregulation (Tfh/Treg imbalance; FcγR biology; complement) and link emerging targets (SYK, BTK, PI3K, FcRn) to clinical strategies (Transfusion Med Hemother 2024; Frontiers Immunol 2025) (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 1-2).

Current applications and real-world implementations
- Sutimlimab (anti‑C1s) for CAD: FDA/EMA-approved; sustained reduction in hemolysis, improved hemoglobin, and reduced transfusions in long-term follow-up (RÖth et al. 2024) (barcellini2024autoimmunehemolyticanemias pages 1-2).
- Rituximab remains the mainstay B-cell–directed therapy for wAIHA/CAD; splenectomy is used selectively in young/fit wAIHA and contraindicated in CAD; complement inhibitors (e.g., eculizumab) may help intravascular components but not C3‑opsonization clearance (Barcellini & Fattizzo 2024; Loriamini 2024) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Daratumumab (anti‑CD38) as a salvage option addresses long‑lived plasma cells, with 2024 evidence for activity in refractory cases (Jalink et al. 2024) (loriamini2024autoimmunehemolyticanemiasa pages 7-8).

Expert opinions and authoritative analyses
- 2024 Transfusion Medicine and Hemotherapy review (Barcellini & Fattizzo) underscores diagnostic and therapeutic heterogeneity, stressing DAT interpretation limits, the clinical importance of extravascular vs intravascular hemolysis, and the rise of mechanism-based therapies (Aug 2024) (barcellini2024autoimmunehemolyticanemias pages 1-2).
- 2025 Frontiers in Immunology review (Costa et al.) frames AIHA as an immune network disease, not merely antibody‑RBC interactions, and explicitly ties FcγR biology and classical complement to targeted therapy choices (Jul 2025) (costa2025beneaththesurface pages 2-3, costa2025beneaththesurface pages 1-2).
- 2023 Frontiers in Immunology review (Mulder et al.) prioritizes inclusion of severe AIHA in trials and development of biomarkers linked to pathophysiological mechanisms for risk prediction (Sep 2023) (loriamini2024autoimmunehemolyticanemiasa pages 7-8).

Relevant statistics and data (recent)
- Incidence and burden: generalized AIHA incidence ~1–3 per 100,000/year; wAIHA comprises ~60–70% of adult AIHA; CAD/CAS ~15–25%; PCH rare. Severe AIHA lacks validated predictors; extravascular hemolysis predominates in wAIHA, whereas complement-positive AIHA has higher transfusion needs and mortality risk in some series (2024–2023 reviews) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- CAD epidemiology and clonal biology: CAD is a clonal B-cell disorder with monoclonal IgM typically anti-I; complement drives hemolysis with C3d positivity on DAT (2024–2025 reviews) (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 2-3).
- Treatment effects: Sutimlimab long-term benefits in CAD (2024 eClinicalMedicine); daratumumab responses in >50% refractory AIHA/CAD (Blood Advances 2024) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8).

Ontology-ready annotations
- Genes/Proteins (HGNC): FCGR2A, FCGR3A, C1QA/B/C (C1q), C1S, C3, C5; RBC antigens: SLC4A1 (Band 3), RHD, RHCE (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 1-2, barcellini2020newinsightsin pages 1-3).
- Biological Processes (GO): classical complement activation; FcγR‑mediated phagocytosis; complement-dependent cytotoxicity; antibody-dependent cellular cytotoxicity; erythrophagocytosis; immune tolerance (B-cell/T-cell tolerance) (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, kostic2024cd4+tcell pages 1-2).
- Cellular Components (GO): RBC plasma membrane; membrane attack complex; splenic macrophage phagolysosome; Kupffer cell surface (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5).
- Cell Types (CL): splenic red pulp macrophage; Kupffer cell; B cell; plasma cell; Tfh; Treg; NK cell (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, kostic2024cd4+tcell pages 1-2).
- Anatomical Locations (UBERON): spleen; liver; bone marrow; peripheral blood (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Chemical Entities (CHEBI/drugs): IgG; IgM; heme; bilirubin; rituximab; sutimlimab; eculizumab; fostamatinib; ibrutinib; FcRn blockers; daratumumab (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 2-3, loriamini2024autoimmunehemolyticanemiasa pages 7-8, loriamini2024autoimmunehemolyticanemiasa pages 4-5).

Evidence artifact (knowledge-base table)
| Category | Entity/Term | Standard ID (where applicable) | Role in AIHA (1–2 sentences) | Evidence |
|---|---|---|---|---|
| Gene/Protein | FCGR2A (FcγRIIA) | HGNC:FCGR2A | Low-affinity IgG receptor on phagocytes that mediates FcγR-dependent recognition and phagocytosis of IgG-opsonized RBCs, driving splenic extravascular hemolysis. | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Gene/Protein | FCGR3A (FcγRIIIA) | HGNC:FCGR3A | Activating Fcγ receptor on NK cells and macrophages contributing to ADCC and clearance of IgG-coated erythrocytes. | (costa2025beneaththesurface pages 2-3, kostic2024cd4+tcell pages 1-2) |
| Gene/Protein | C1Q (C1q complex) | HGNC:C1QA/B/C | Initiator of the classical complement pathway by binding IgM/IgG Fc and enabling C1s activation and downstream C3 opsonization. | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Gene/Protein | C1S | HGNC:C1S | Protease subunit of the C1 complex; C1s cleavage activity is required for C4/C2 cleavage and C3b deposition on RBCs in complement-mediated AIHA (e.g., CAD). | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Gene/Protein | C3 | HGNC:C3 | Central complement component; C3b opsonizes RBCs promoting hepatic/splenic phagocytosis and is detected by DAT (C3d positive) in complement-driven AIHA. | (loriamini2024autoimmunehemolyticanemiasa pages 4-5, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Gene/Protein | C5 | HGNC:C5 | Terminal cascade component leading to MAC (C5b-9); contributes to intravascular hemolysis when terminal pathway activated. | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| RBC antigen | SLC4A1 (Band 3) | HGNC:SLC4A1 | Common RBC membrane antigen targeted by warm autoantibodies; opsonization can lead to spherocyte formation and splenic clearance. | (barcellini2020newinsightsin pages 1-3, loriamini2024autoimmunehemolyticanemiasa pages 1-2) |
| RBC antigen | RHD / RHCE (Rh antigens) | HGNC:RHD, HGNC:RHCE | Frequent warm-AIHA targets; anti-Rh reactivity promotes IgG opsonization and Fc-mediated erythrophagocytosis. | (barcellini2020newinsightsin pages 1-3, kostic2024cd4+tcell pages 1-2) |
| Pathway / Process | Classical complement activation | GO:classical complement activation | Triggered by IgM or IgG binding to RBCs; drives C4/C2 cleavage, C3b deposition and downstream opsonization or membrane attack complex formation. | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Pathway / Process | FcγR-mediated phagocytosis | GO:FcγR-mediated phagocytosis | Engagement of Fcγ receptors on splenic macrophages leads to antibody-dependent cellular phagocytosis (ADCP) and extravascular hemolysis. | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Pathway / Process | Antibody-dependent cellular cytotoxicity (ADCC) | GO:ADCC | NK cells or cytotoxic lymphocytes recognize IgG-coated RBCs via FcγRIIIA and can mediate direct lytic or cytotoxic mechanisms contributing to RBC loss. | (costa2025beneaththesurface pages 2-3, kostic2024cd4+tcell pages 1-2) |
| Pathway / Process | Complement-dependent cytotoxicity (CDC) | GO:CDC | Complement activation culminating in MAC formation causes intravascular hemolysis in severe complement-driven cases (e.g., some CAD/PCH). | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Pathway / Process | Erythrophagocytosis (macrophage uptake) | GO:erythrophagocytosis | Macrophage ingestion of opsonized RBCs in spleen/liver is the principal mechanism of extravascular hemolysis in wAIHA and complement-opsonized CAD. | (costa2025beneaththesurface pages 2-3, loriamini2024autoimmunehemolyticanemiasa pages 7-8) |
| Pathway / Process | Tolerance breakdown (B/T cells; Tfh/Treg imbalance, BAFF) | GO:immune tolerance; B cell tolerance | Dysregulation of Tfh/Treg balance and elevated BAFF support autoreactive B-cell survival and autoantibody production that initiate and sustain AIHA. | (kostic2024cd4+tcell pages 1-2, barcellini2020newinsightsin pages 1-3) |
| Cellular component | RBC membrane | GO:membrane | Location of antigenic targets (band 3, Rh, glycophorins); modifications or bound complement determine recognition by immune effectors. | (loriamini2024autoimmunehemolyticanemiasa pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5) |
| Cellular component | Splenic macrophage phagolysosome | GO:phagolysosome | Site where FcγR-mediated engulfment and degradation of RBCs occurs, generating extravascular hemolysis and spherocyte formation. | (costa2025beneaththesurface pages 2-3, loriamini2024autoimmunehemolyticanemiasa pages 7-8) |
| Cellular component | Liver Kupffer cell surface | GO:cell surface | Kupffer cells recognize C3-opsonized RBCs via complement receptors and mediate hepatic extravascular clearance, especially in complement-positive AIHA. | (loriamini2024autoimmunehemolyticanemiasa pages 4-5, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Cellular component | Membrane attack complex (MAC) on RBC membrane | GO:membrane attack complex | Deposition of C5b-9 on RBCs can cause lysis and hemoglobin release (intravascular hemolysis) in severe complement activation. | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Cell type | Splenic red pulp macrophage | CL:splenic red pulp macrophage | Principal effector of FcγR-mediated erythrophagocytosis in wAIHA, clearing IgG-opsonized RBCs and causing anemia. | (costa2025beneaththesurface pages 2-3, loriamini2024autoimmunehemolyticanemiasa pages 7-8) |
| Cell type | Hepatic Kupffer cell | CL:Kupffer cell | Clears C3-opsonized RBCs from circulation and contributes to extravascular hemolysis in complement-mediated AIHA (CAD). | (loriamini2024autoimmunehemolyticanemiasa pages 4-5, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Cell type | B cell (autoreactive) | HGNC:B-cell (generic) | Source of autoantibody production; clonal B-cell expansions underlie CAD and support persistent autoantibody-mediated hemolysis. | (costa2025beneaththesurface pages 2-3, costa2025beneaththesurface pages 1-2) |
| Cell type | Plasma cell | CL:plasma cell | Long-lived antibody-secreting cells that maintain pathogenic autoantibody titers and can confer treatment resistance. | (loriamini2024autoimmunehemolyticanemiasa pages 7-8, costa2025beneaththesurface pages 1-2) |
| Cell type | T follicular helper cell (Tfh) | CL:Tfh cell | Supports B-cell maturation and autoreactive antibody generation when dysregulated, implicated in AIHA initiation/maintenance. | (kostic2024cd4+tcell pages 1-2, barcellini2020newinsightsin pages 1-3) |
| Cell type | Regulatory T cell (Treg) | CL:Treg cell | Loss or dysfunction of Tregs permits autoreactive responses and autoantibody emergence in AIHA. | (kostic2024cd4+tcell pages 1-2, barcellini2020newinsightsin pages 1-3) |
| Cell type | Natural killer (NK) cell | CL:NK cell | Mediates ADCC against IgG-opsonized RBCs via FcγRIIIA contributing to immune-mediated RBC destruction. | (costa2025beneaththesurface pages 2-3, kostic2024cd4+tcell pages 1-2) |
| Anatomical site | Spleen | UBERON:spleen | Major organ for FcγR-dependent RBC clearance (extravascular hemolysis); target for splenectomy in refractory warm AIHA. | (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Anatomical site | Liver | UBERON:liver | Important site of complement-mediated (C3b) RBC removal via Kupffer cells; more engaged in CAD and complement-opsonized RBC clearance. | (loriamini2024autoimmunehemolyticanemiasa pages 4-5, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Anatomical site | Bone marrow | UBERON:bone marrow | Site of erythropoiesis and compensation; inadequate reticulocytosis/ marrow failure worsens anemia severity and prognosis. | (loriamini2024autoimmunehemolyticanemiasa pages 7-8, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Anatomical site | Peripheral blood | UBERON:blood | Circulating compartment where autoantibodies, hemolysis markers (LDH, low haptoglobin), and cold agglutinins are detected. | (loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 1-2) |
| Chemical / Drug | IgG (autoantibody) | CHEBI:IgG (class) | Predominant isotype in warm AIHA; opsonizes RBCs for FcγR-mediated phagocytosis and can weakly activate complement (IgG1/IgG3). | (barcellini2020newinsightsin pages 1-3, costa2025beneaththesurface pages 2-3) |
| Chemical / Drug | IgM (cold agglutinin) | CHEBI:IgM (class) | Pentameric IgM strongly activates classical complement upon cold binding (CAD), causing C3 deposition and agglutination. | (loriamini2024autoimmunehemolyticanemiasa pages 4-5, costa2025beneaththesurface pages 2-3) |
| Chemical / Drug | Heme / Bilirubin (hemolysis markers) | CHEBI:heme; CHEBI:bilirubin | Heme release and unconjugated bilirubin rise reflect hemolysis; bilirubin elevation and LDH/haptoglobin help distinguish intra- vs extravascular hemolysis. | (loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 1-2) |
| Chemical / Drug | Rituximab (anti-CD20) | Drug:rituximab | B-cell–depleting therapy effective in many wAIHA and CAD cases by reducing autoantibody-producing B cells; standard second-line agent. | (barcellini2020newinsightsin pages 1-3, barcellini2024autoimmunehemolyticanemias pages 1-2) |
| Chemical / Drug | Daratumumab (anti-CD38) | Drug:daratumumab | Targets plasma cells and has activity in refractory AIHA by reducing long-lived autoantibody-secreting plasma cells. | (loriamini2024autoimmunehemolyticanemiasa pages 7-8, loriamini2024autoimmunehemolyticanemiasa pages 1-2) |
| Chemical / Drug | Sutimlimab (anti-C1s) | Drug:sutimlimab | C1s inhibitor that blocks classical-pathway initiation and rapidly reduces complement-mediated hemolysis in CAD. | (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 1-2) |
| Chemical / Drug | Eculizumab (anti-C5) | Drug:eculizumab | Terminal complement inhibitor preventing MAC formation; may reduce intravascular hemolysis but has variable effects on extravascular complement opsonization. | (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8) |
| Chemical / Drug | Fostamatinib (SYK inhibitor) | Drug:fostamatinib | Inhibits spleen tyrosine kinase to reduce FcγR-mediated phagocytosis signaling, used as targeted therapy in refractory immune cytopenias. | (loriamini2024autoimmunehemolyticanemiasa pages 7-8, costa2025beneaththesurface pages 2-3) |
| Chemical / Drug | Ibrutinib (BTK inhibitor) | Drug:ibrutinib | BTK blockade impairs BCR signaling and clonal B-cell survival, used experimentally in some AIHA/CAD settings to reduce autoantibody production. | (costa2025beneaththesurface pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8) |
| Chemical / Drug | FcRn blockers (e.g., nipocalimab) | Drug:FcRn blocker | Reduce IgG half-life by blocking neonatal Fc receptor, lowering circulating pathogenic IgG levels and ameliorating hemolysis. | (loriamini2024autoimmunehemolyticanemiasa pages 7-8, barcellini2020newinsightsin pages 1-3) |


*Table: Compact knowledge‑base table mapping key genes/proteins, pathways, cells, anatomical sites and therapeutics in AIHA with concise roles and evidence citations; useful for ontology annotation and mechanistic summaries.*

Structured subtype-specific mechanisms
- Warm AIHA (wAIHA): IgG autoantibodies (often anti-band 3, Rh antigens) active at 37°C; dominant FcγR-mediated splenic extravascular hemolysis; DAT typically IgG±C3; complement can contribute when IgG1/IgG3 fix C1q. First-line: glucocorticoids; second-line: rituximab; splenectomy in selected cases; emerging: FcRn blockers, SYK/BTK/PI3K inhibitors, anti-CD38 (URLs/dates: 2024 reviews) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, costa2025beneaththesurface pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Cold Agglutinin Disease (CAD): monoclonal IgM (anti‑I/Ii) binds in the cold; strong classical complement activation with C3d DAT positivity; hepatic clearance of C3-opsonized RBCs plus variable intravascular hemolysis; management: keep warm, rituximab/clone-directed therapy, and complement blockade (C1s inhibition) with sutimlimab as a disease-modifying agent (RÖth et al., 2024) (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 2-3).
- Mixed AIHA: concurrent warm IgG and clinically significant cold IgM (thermal amplitude up to 30–37°C); DAT IgG+C3; both FcγR and complement mechanisms active; management often combines wAIHA and CAD approaches (loriamini2024autoimmunehemolyticanemiasa pages 4-5, barcellini2024autoimmunehemolyticanemias pages 1-2).
- Paroxysmal Cold Hemoglobinuria (PCH): biphasic IgG (Donath–Landsteiner) binds P antigen in the cold and lyses RBCs on warming via complement; DAT C3d-only; typically post-infectious in children, often self-limited; in severe cases, complement blockade has a rationale (loriamini2024autoimmunehemolyticanemiasa pages 1-2).

Open questions and research priorities
- Predictors of severe disease and rapid-acting therapies for steroid-refractory crises remain limited; trials should enrich for severe AIHA and incorporate mechanistic biomarkers (e.g., complement deposition, FcγR expression/polymorphisms, marrow compensation signatures) (Mulder et al., 2023) (loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Systems-level profiling (e.g., single-cell marrow/immune phenotyping) is revealing T-cell infiltration, clonal dynamics, and cytokine shifts across disease phases, with implications for targeted intervention sequencing (2025 scRNA-seq study; URL: https://doi.org/10.1038/s41392-025-02348-y) (loriamini2024autoimmunehemolyticanemiasa pages 7-8).

References with URLs and publication dates
- Barcellini W, Fattizzo B. Autoimmune Hemolytic Anemias: Challenges in Diagnosis and Therapy. Transfusion Medicine and Hemotherapy. Aug 2024. https://doi.org/10.1159/000540475 (barcellini2024autoimmunehemolyticanemias pages 1-2).
- Loriamini M, Cserti-Gazdewich C, Branch DR. Autoimmune Hemolytic Anemias: Classifications, Pathophysiology, Diagnoses and Management. Int J Mol Sci. Apr 2024. https://doi.org/10.3390/ijms25084296 (loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Costa A et al. Beneath the surface in autoimmune hemolytic anemia: pathogenetic networks, therapeutic advancements and open questions. Front Immunol. Jul 2025. https://doi.org/10.3389/fimmu.2025.1624667 (costa2025beneaththesurface pages 2-3, costa2025beneaththesurface pages 1-2).
- Röth A et al. Long-term efficacy and safety of continued complement C1s inhibition with sutimlimab in CAD: CADENZA Part B. eClinicalMedicine. Aug 2024. https://doi.org/10.1016/j.eclinm.2024.102733 (barcellini2024autoimmunehemolyticanemias pages 1-2).
- Reid M, Henderson B. Sutimlimab for Cold Agglutinin Disease. J Adv Pract Oncol. Sep 2024. https://doi.org/10.6004/jadpro.2024.15.6.4 (barcellini2024autoimmunehemolyticanemias pages 1-2).
- Jalink M et al. Daratumumab monotherapy in refractory wAIHA and CAD. Blood Advances. May 2024. https://doi.org/10.1182/bloodadvances.2024012585 (loriamini2024autoimmunehemolyticanemiasa pages 7-8).
- Kostić M et al. CD4+ T cell profiles in AIHA. Acta Medica Medianae. Mar 2024. https://doi.org/10.5633/amm.2024.0108 (kostic2024cd4+tcell pages 1-2).

Pathophysiology description (narrative for KB entry)
AIHA results from immune recognition of self-RBC antigens with autoantibodies (IgG or IgM) that initiate FcγR-mediated erythrophagocytosis in the spleen or classical complement activation with C3 opsonization and occasional MAC-mediated lysis. Warm IgG autoantibodies (often anti-band 3/Rh) at 37°C engage FcγR-bearing splenic macrophages (extravascular hemolysis), with complement contributing variably. Cold IgM autoantibodies in CAD agglutinate RBCs and drive C1q/C1s-dependent C3b deposition, favoring hepatic Kupffer cell clearance and sometimes intravascular hemolysis; mixed AIHA combines both mechanisms; PCH features a biphasic IgG (Donath–Landsteiner) that fixes complement on rewarming to cause intravascular hemolysis. A breakdown in immune tolerance involving Tfh/Treg and B-cell survival signals sustains autoantibody production. Clinical severity depends on effector balance (extravascular vs intravascular), degree of complement activation, and marrow compensation. Mechanism-based therapies target B cells (rituximab), plasma cells (daratumumab), FcγR signaling (SYK), BCR signaling (BTK/PI3K), IgG recycling (FcRn), and complement (C1s, C5) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, costa2025beneaththesurface pages 2-3, costa2025beneaththesurface pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8, kostic2024cd4+tcell pages 1-2).

Gene/protein annotations with ontology terms (examples)
- FCGR2A (HGNC) – GO: Fcγ receptor signaling, FcγR-mediated phagocytosis; CL: splenic red pulp macrophage; UBERON: spleen; Evidence: wAIHA extravascular hemolysis (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2).
- C1S (HGNC) – GO: classical complement activation; UBERON: liver (Kupffer cell clearance) and blood (activation); CHEBI: IgM triggers; Evidence: CAD complement dependence; sutimlimab efficacy (barcellini2024autoimmunehemolyticanemias pages 1-2, costa2025beneaththesurface pages 2-3).
- SLC4A1/Band 3 (HGNC) – GO: RBC membrane; target of warm autoantibodies; Evidence: warm panreactive anti-band 3 (barcellini2020newinsightsin pages 1-3, loriamini2024autoimmunehemolyticanemiasa pages 1-2).

Phenotype associations (HPO; examples)
- Autoimmune hemolytic anemia (HP:0001933); Jaundice (HP:0000952); Hemoglobinuria (HP:0002904); Acrocyanosis (HP:0001063) in CAD; Elevated LDH (HP:0032456); Low haptoglobin (HP:0012394); Reticulocytosis (HP:0001923) or Reticulocytopenia (HP:0020059) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, costa2025beneaththesurface pages 2-3).

Cell type involvement (CL; examples)
- Splenic red pulp macrophages (CL:0000898) – ADCP of IgG-opsonized RBCs; Kupffer cells (CL:0000232) – complement-opsonized RBC clearance; Tfh (CL:0002323); Treg (CL:0000815); NK cells (CL:0000623) (costa2025beneaththesurface pages 2-3, barcellini2024autoimmunehemolyticanemias pages 1-2, kostic2024cd4+tcell pages 1-2).

Anatomical locations (UBERON; examples)
- Spleen (UBERON:0002106); Liver (UBERON:0002107); Bone marrow (UBERON:0002371); Blood (UBERON:0000178) (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 4-5, loriamini2024autoimmunehemolyticanemiasa pages 7-8).

Chemical entities (CHEBI; examples)
- IgG (CHEBI:16110); IgM (CHEBI:15996); Heme (CHEBI:17627); Bilirubin (CHEBI:16990). Drugs: rituximab, daratumumab, sutimlimab, eculizumab, fostamatinib, ibrutinib, FcRn blockers (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8, costa2025beneaththesurface pages 2-3).

Notes on limitations
- Some epidemiologic figures vary across datasets and geography; subtyping by DAT requires expert interpretation due to imperfect sensitivity/specificity; several T-cell tolerance and BAFF-centric mechanisms are derived from broader autoimmunity literature and specific AIHA-focused immunophenotyping continues to evolve (barcellini2024autoimmunehemolyticanemias pages 1-2, loriamini2024autoimmunehemolyticanemiasa pages 7-8, kostic2024cd4+tcell pages 1-2).

References

1. (barcellini2024autoimmunehemolyticanemias pages 1-2): Wilma Barcellini and Bruno Fattizzo. Autoimmune hemolytic anemias: challenges in diagnosis and therapy. Transfusion Medicine and Hemotherapy, 51:321-331, Aug 2024. URL: https://doi.org/10.1159/000540475, doi:10.1159/000540475. This article has 18 citations and is from a peer-reviewed journal.

2. (loriamini2024autoimmunehemolyticanemiasa pages 4-5): Melika Loriamini, Christine Cserti-Gazdewich, and Donald R. Branch. Autoimmune hemolytic anemias: classifications, pathophysiology, diagnoses and management. International Journal of Molecular Sciences, 25:4296, Apr 2024. URL: https://doi.org/10.3390/ijms25084296, doi:10.3390/ijms25084296. This article has 40 citations and is from a poor quality or predatory journal.

3. (costa2025beneaththesurface pages 1-2): Alessandro Costa, Olga Mulas, Angela Maria Mereu, Mercede Schintu, Marianna Greco, and Giovanni Caocci. Beneath the surface in autoimmune hemolytic anemia: pathogenetic networks, therapeutic advancements and open questions. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1624667, doi:10.3389/fimmu.2025.1624667. This article has 1 citations and is from a peer-reviewed journal.

4. (kostic2024cd4+tcell pages 1-2): Miloš Kostić, Nikola Živković, and Ana Cvetanović. Cd4+ t cell profiles in autoimmune hemolytic anemia. Acta Medica Medianae, 63:73-82, Mar 2024. URL: https://doi.org/10.5633/amm.2024.0108, doi:10.5633/amm.2024.0108. This article has 0 citations.

5. (costa2025beneaththesurface pages 2-3): Alessandro Costa, Olga Mulas, Angela Maria Mereu, Mercede Schintu, Marianna Greco, and Giovanni Caocci. Beneath the surface in autoimmune hemolytic anemia: pathogenetic networks, therapeutic advancements and open questions. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1624667, doi:10.3389/fimmu.2025.1624667. This article has 1 citations and is from a peer-reviewed journal.

6. (loriamini2024autoimmunehemolyticanemiasa pages 7-8): Melika Loriamini, Christine Cserti-Gazdewich, and Donald R. Branch. Autoimmune hemolytic anemias: classifications, pathophysiology, diagnoses and management. International Journal of Molecular Sciences, 25:4296, Apr 2024. URL: https://doi.org/10.3390/ijms25084296, doi:10.3390/ijms25084296. This article has 40 citations and is from a poor quality or predatory journal.

7. (loriamini2024autoimmunehemolyticanemiasa pages 1-2): Melika Loriamini, Christine Cserti-Gazdewich, and Donald R. Branch. Autoimmune hemolytic anemias: classifications, pathophysiology, diagnoses and management. International Journal of Molecular Sciences, 25:4296, Apr 2024. URL: https://doi.org/10.3390/ijms25084296, doi:10.3390/ijms25084296. This article has 40 citations and is from a poor quality or predatory journal.

8. (barcellini2020newinsightsin pages 1-3): Wilma Barcellini, Anna Zaninoni, Juri Alessandro Giannotta, and Bruno Fattizzo. New insights in autoimmune hemolytic anemia: from pathogenesis to therapy. Journal of Clinical Medicine, 9:3859, Nov 2020. URL: https://doi.org/10.3390/jcm9123859, doi:10.3390/jcm9123859. This article has 139 citations and is from a poor quality or predatory journal.