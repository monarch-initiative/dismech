---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-17T16:17:01.108044'
end_time: '2026-02-17T16:42:02.886834'
duration_seconds: 1501.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Long COVID
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Long COVID
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Long COVID**.
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
- **Disease Name:** Long COVID
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Long COVID**.
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


# Research Report: Pathophysiology of Long COVID (Post-acute sequelae of SARS‑CoV‑2 infection; PASC)

## Target disease and ontology
- **Disease name:** Long COVID (PASC; post‑COVID condition)
- **MONDO ID:** **Not found in retrieved full texts** (no explicit MONDO identifier present in the evidence corpus used for this report).
- **Category:** Complex, multisystem, post‑infectious syndrome.

## 1) Key concepts and definitions (current understanding)

**Definition / case concept.** Long COVID (PASC) is a heterogeneous syndrome of persistent or new symptoms after acute SARS‑CoV‑2 infection. The Collegium Internationale Allergologicum update notes a clinical definition consistent with WHO framing (symptoms beginning within ~3 months and persisting ≥2 months) and emphasizes multi-organ involvement and immune mechanisms (e.g., persistent reservoir, metabolic reprogramming, virus reactivation, autoimmunity, microbiome dysbiosis). (untersmayr2024immunemechanismsunderpinning pages 2-2, untersmayr2024immunemechanismsunderpinning pages 1-2)

**Scale of the problem.** A conservative estimate of ~10% of infections developing long COVID is summarized in a 2024 immune review, translating to ≥65 million people worldwide. (untersmayr2024immunemechanismsunderpinning pages 1-2)

**Heterogeneity / endotypes.** A major current concept is that PASC is not a single entity but comprises biological subtypes. Serum proteomics identifies an **“inflammatory” subcategory** characterized by **type II interferon (IFN‑γ) and TNF/NF‑κB pathway activity** and a second inflammatory pattern involving neutrophil activation and type I IFN–associated proteins. (talla2023persistentserumprotein pages 6-7, talla2023persistentserumprotein pages 1-2)

## 2) Core pathophysiology: primary mechanisms and dysregulated pathways

Long COVID pathophysiology is best supported by converging evidence for **(A) viral persistence/antigenemia**, **(B) chronic immune activation/dysregulation and autoimmunity**, **(C) endothelial dysfunction/barrier injury with thromboinflammation**, and **(D) metabolic/mitochondrial dysfunction** with organ-specific manifestations (notably skeletal muscle in post‑exertional malaise).

### A. Viral persistence and persistent antigenemia
**Tissue reservoirs and prolonged antigen.** A high-impact 2023 Nature Immunology review synthesizes evidence that SARS‑CoV‑2 RNA/protein can persist in multiple tissues for months after acute infection and that persistence can occur despite negative nasopharyngeal testing. It highlights detection windows such as **31–230 days**, including **subgenomic RNA (marker of recent replication) at day 99**, and reports of viral RNA in **80% of lung samples up to 174 days** in one study. (proal2023sarscov2reservoirin pages 4-6)

**Upper airway and GI persistence durations.** A 2024 review summarizes that SARS‑CoV‑2 RNA has been isolated **up to 3 months in the upper respiratory tract**, **2 months in serum**, and **126 days in stool**. (gusev2024exploringthepathophysiology pages 2-4)

**Prospective evidence for persistent nucleocapsid antigenemia in PASC.** In a prospective cohort (Aug 2022–Jul 2023), **29/57 (51%)** met a questionnaire-based PASC definition; nucleocapsid protein (NP) antigen was **higher in PASC at 3 months** (median **5.49 ng/mL** vs **0.59 ng/mL**; **P=0.022**) despite being lower during acute illness (median **1.58 ng/mL** vs **12.42 ng/mL**; **P=0.045**). (ra2024viralimmunologicand pages 2-4)

**Mechanistic implications.** Peluso & Deeks (Cell 2024) emphasize that higher acute viral burden, RNAemia, and prolonged clearance correlate with long COVID risk and that interventions limiting early viral replication (vaccines; antivirals) provide indirect evidence that reducing acute viral burden may reduce long-term sequelae. (peluso2024mechanismsoflong pages 6-8)

### B. Immune dysregulation: inflammatory endotypes and cytokine/chemokine pathways

**Proteomic inflammatory endotype: IFN‑γ and TNF/NF‑κB.** A 2023 Nature Communications longitudinal serum proteomics study identifies an inflammatory PASC subgroup with dominant enrichment of **“Type II interferon signaling and canonical NF‑κB signaling (particularly associated with TNF)”**. (talla2023persistentserumprotein pages 1-2)

- IFN‑γ–dominant cluster shows elevated IFN‑γ–driven chemokines **CXCL9/CXCL10/CXCL11**, and cytokine axis markers (e.g., IL‑27; IL‑12 p40/heterodimer), with concurrent TNF/NF‑κB enrichment and increased TNF-driven cytokines including **IL‑6**. (talla2023persistentserumprotein pages 6-7)
- Another cluster shows a **type I IFN–associated protein signature** including **SAMD9L, DDX58, MNDA, LAMP3** that **“remained elevated for approximately 180 days post infection”**. (talla2023persistentserumprotein pages 6-7)

**A simple biomarker panel for inflammatory PASC stratification.** The same study proposes a 3‑protein panel (**CCL7, CD40LG, S100A12**) with **AUROC 0.865 (95% CI 0.765–0.966)** training and **0.788 (95% CI 0.590–0.985)** test. (talla2023persistentserumprotein pages 10-11)

**Prospective cytokine differences accompanying antigenemia.** In the JKMS 2024 cohort, among 33 cytokines measured, **IL‑2, IL‑17A, VEGF, RANTES (CCL5), sCD40L, IP‑10 (CXCL10), I‑TAC (CXCL11), and granzyme A** were reported as significantly elevated in the PASC group at 1 and/or 3 months. (ra2024viralimmunologicand pages 5-6, ra2024viralimmunologicand pages 1-2)

**Inflammasome and persistent immune activation.** A 2024 review emphasizes chronic low‑grade inflammation and notes **NLRP3 inflammasome activation** among implicated mechanisms. (gusev2024exploringthepathophysiology pages 2-4)

### C. Endothelial dysfunction, barrier injury, and thromboinflammation (microvascular disease)

**Endothelial barrier injury as a central organizing mechanism.** An Angiogenesis 2024 review states that endothelial injury is observed in acute and convalescent COVID and that endothelial dysfunction contributes to long COVID; it reports persistent elevation of **D‑dimer, factor VIII, thrombin, vWF, ICAM‑1 and IL‑6** detectable even one year after recovery, alongside persistent glycocalyx shedding and circulating endothelial cells. (wu2024damagetoendothelial pages 1-2)

**Mechanistic drivers of endothelial pathology.** The same review links endothelial dysfunction to inflammatory cytokines (**IL‑6, IL‑1, TNF**), activated platelets, increased thrombin, NETs, and complement, producing a prothrombotic endothelial phenotype; spike can damage endothelial cells via ACE2 downregulation. (wu2024damagetoendothelial pages 1-2)

**Severe post‑COVID ARDS: persistent endotheliitis markers and in vitro endothelial effects.** A BMC Medicine 2024 study assessed **88** ICU survivors at **6 months** post‑ICU discharge; patients with impaired gas exchange showed elevated plasma markers of endothelial inflammation (ICAM‑1, IL‑8, CCL‑2, ET‑1) and systemic inflammation (NLRP3 overexpression; IL‑6, sCD40‑L, CRP), with persistent IFN‑β and T cell activation markers. (alfaro2024endothelialdysfunctionand pages 1-2)

In vitro, post‑COVID patient plasma increased endothelial activation in HUVECs (e.g., “augmented ICAM‑1 expression,” increased active caspase‑1, increased ET‑1), and IFN‑β inhibition reduced ET‑1 release. (alfaro2024endothelialdysfunctionand pages 8-10)

### D. Coagulation abnormalities, microclots, and platelet activation

**Thrombotic endothelialitis biomarker panel.** A 2024 Seminars in Thrombosis and Hemostasis study reports increased soluble concentrations of **VWF, PF4, SAA, α‑2 antiplasmin (α‑2AP), E‑selectin, and PECAM‑1** in long COVID. The mean **α‑2AP exceeded the upper reference limit**, and the authors interpret microclotting plus these biomarkers as evidence that **thrombotic endothelialitis** is a key pathological process. (turner2024increasedlevelsof pages 1-2)

**Microclots as partial explanation and heterogeneity.** A review on microthrombosis emphasizes that microclots may contribute to PASC but cannot explain all symptoms, and anticoagulation/antiplatelet evidence is inconsistent, supporting symptom/biomarker-based stratification. (turner2024increasedlevelsof pages 1-2)

### E. Mitochondrial, metabolic, and skeletal muscle mechanisms (notably PEM)

**Muscle pathology and post-exertional malaise (PEM).** A Nature Communications 2024 longitudinal case-control study induced PEM with maximal exercise and performed paired biopsies. Long COVID patients had reduced exercise capacity (lower V̇O2max/peak power) and lower peripheral O2 extraction by NIRS, alongside structural abnormalities and inflammation in muscle. (appelman2024muscleabnormalitiesworsen pages 3-4, appelman2024muscleabnormalitiesworsen pages 2-3)

**Direct mitochondrial/metabolic findings in muscle.** The study reports:
- “**Oxidative phosphorylation (OXPHOS) capacity was significantly lower** in patients with long COVID … and remained lower one day after induction of post-exertional malaise.” (appelman2024muscleabnormalitiesworsen pages 5-6)
- Muscle metabolomics showed key TCA metabolites (e.g., **glutamate, FAD+, α‑ketoglutarate, citric acid**) and a lower **citric acid:lactate** ratio in patients, consistent with reduced oxidative metabolism; venous blood showed higher glycolytic metabolites and lower pyruvate/TCA metabolites. (appelman2024muscleabnormalitiesworsen pages 3-4)

**Amyloid-containing deposits in muscle.** The same study reports “**an increased accumulation of amyloid-containing deposits in skeletal muscle**” in long COVID, higher at baseline and increasing after exercise; deposits were extracellular/adjacent to endothelium rather than within endothelial cells. (appelman2024muscleabnormalitiesworsen pages 6-7)

## 3) Key molecular players (genes/proteins), chemicals, cell types, and anatomical locations

### 3.1 Genes/proteins (HGNC-style symbols where applicable)
Below are key molecules supported by the evidence corpus, grouped by mechanism.

**Viral entry/tropism / tissue injury**
- **ACE2** (viral entry receptor; endothelial and GI expression; spike effects on ACE2). (wu2024damagetoendothelial pages 1-2, bohmwald2024pathophysiologicalimmunologicaland pages 12-12)

**Cytokines/chemokines and immune signaling**
- **IFNG (IFN‑γ)** and type II IFN signaling endotype. (talla2023persistentserumprotein pages 6-7, talla2023persistentserumprotein pages 1-2)
- **TNF** and canonical **NF‑κB** signaling enrichment. (talla2023persistentserumprotein pages 6-7, talla2023persistentserumprotein pages 1-2)
- **IL6**, **IL1B** (inflammatory mediators linked to endotheliopathy/inflammation). (wu2024damagetoendothelial pages 1-2, talla2023persistentserumprotein pages 6-7)
- **CXCL9/CXCL10 (IP‑10)/CXCL11 (I‑TAC)** in IFN‑γ endotype and JKMS cytokines. (talla2023persistentserumprotein pages 6-7, ra2024viralimmunologicand pages 5-6)
- **IL17A**, **IL2**, **VEGFA/VEGF**, **CCL5 (RANTES)**, **CD40LG (sCD40L)**, **GZMA** elevated in PASC cohort. (ra2024viralimmunologicand pages 5-6, ra2024viralimmunologicand pages 1-2)

**Innate sensing / type I IFN-associated proteins (proteomics)**
- **DDX58 (RIG‑I)**, **SAMD9L**, **LAMP3**, **MNDA** in persistent type I IFN–associated signature. (talla2023persistentserumprotein pages 6-7)

**Inflammasome / endothelial activation**
- **NLRP3** (inflammasome activation; monocyte overexpression; endothelial transcript changes). (alfaro2024endothelialdysfunctionand pages 5-8, gusev2024exploringthepathophysiology pages 2-4)
- **IFI16** (endothelial inflammatory response marker in HUVEC model). (alfaro2024endothelialdysfunctionand pages 5-8)
- **ICAM1**, **PECAM1 (CD31)**, **SELE (E‑selectin)** endothelial activation markers. (wu2024damagetoendothelial pages 1-2, turner2024increasedlevelsof pages 1-2)
- **EDN1 (ET‑1)** vasoconstrictor; elevated in severe post‑COVID with impaired gas exchange; IFN‑β linked in vitro. (alfaro2024endothelialdysfunctionand pages 1-2, alfaro2024endothelialdysfunctionand pages 8-10)

**Coagulation/fibrinolysis and platelet activation**
- **VWF**, **PF4**, **SERPINF2 (α‑2AP)**, **SAA1/2 (serum amyloid A)**. (turner2024increasedlevelsof pages 1-2)

### 3.2 Chemical entities / metabolites (CHEBI-style where possible)
Evidence-supported metabolites altered in long COVID muscle/blood:
- **FAD+**, **α‑ketoglutarate**, **citric acid**, **lactate**, **glutamate**, **creatine**, **S‑adenosylmethionine (SAM)**. (appelman2024muscleabnormalitiesworsen pages 3-4)

Therapeutically relevant small molecules/drugs with mechanistic rationale:
- **Nirmatrelvir/ritonavir (Paxlovid)** (antiviral; trials and observational signals discussed as modifying long COVID risk). (peluso2024mechanismsoflong pages 6-8)
- **Metformin** (trial evidence for reduced later long COVID diagnoses is discussed in Cell 2024 review). (peluso2024mechanismsoflong pages 6-8)

### 3.3 Cell types (CL terms; key examples)
- **Endothelial cells**: barrier injury, glycocalyx shedding, ICAM‑1/PECAM‑1/E‑selectin signatures, thromboinflammation. (wu2024damagetoendothelial pages 1-2, turner2024increasedlevelsof pages 1-2)
- **CD14+ monocytes**: NLRP3 readouts in post‑COVID ARDS cohort. (alfaro2024endothelialdysfunctionand pages 5-8)
- **T cells (CD3+; activated/exhausted phenotypes)**: persistent antigen-driven activation; muscle CD3+ infiltration; PASC T cell activation/exhaustion markers summarized in reservoir review. (proal2023sarscov2reservoirin pages 8-10, appelman2024muscleabnormalitiesworsen pages 8-9)
- **Macrophages (CD68+)**: increased muscle infiltration. (appelman2024muscleabnormalitiesworsen pages 8-9, appelman2024muscleabnormalitiesworsen pages 5-6)
- **Neutrophils / NETosis**: inflammatory PASC clusters show neutrophil degranulation/NETosis signatures. (talla2023persistentserumprotein pages 11-12)

### 3.4 Anatomical locations (UBERON-style; key examples)
- **Gastrointestinal tract / intestinal mucosa**: viral persistence, permeability (“gut leakage”), zonulin-linked barrier dysfunction discussed in reservoir model; intestinal biopsies show viral RNA/protein in subsets. (proal2023sarscov2reservoirin pages 10-12, wu2024damagetoendothelial pages 1-2)
- **Lymphoid tissues (tonsil/adenoid)**: nucleocapsid RNA detected long after nasopharyngeal negativity. (proal2023sarscov2reservoirin pages 8-10)
- **Vascular system (microvasculature)**: endothelial dysfunction and thrombotic endothelialitis. (turner2024increasedlevelsof pages 1-2, wu2024damagetoendothelial pages 1-2)
- **Skeletal muscle (vastus lateralis)**: OXPHOS impairment, fiber-type shift, amyloid deposits, immune infiltration, PEM-associated worsening. (appelman2024muscleabnormalitiesworsen pages 5-6, appelman2024muscleabnormalitiesworsen pages 6-7)
- **Lung / gas exchange interface**: low DLCO phenotype with endothelial inflammation biomarkers. (alfaro2024endothelialdysfunctionand pages 1-2)

## 4) Biological processes disrupted (GO-oriented)

The following GO-style process categories are supported by the evidence corpus:

1. **Type II interferon signaling (IFN‑γ–mediated signaling)**: dominant inflammatory PASC proteomic cluster with CXCL9/10/11 elevation. (talla2023persistentserumprotein pages 6-7, talla2023persistentserumprotein pages 1-2)
2. **TNF signaling and canonical NF‑κB signaling**: enriched in inflammatory PASC clusters; linked to IL‑6 elevation. (talla2023persistentserumprotein pages 6-7, talla2023persistentserumprotein pages 1-2)
3. **Chemokine-mediated leukocyte migration** (e.g., CXCL10/CXCL11; CCL5): elevated in PASC cohort. (ra2024viralimmunologicand pages 5-6)
4. **Neutrophil degranulation and NETosis / thromboinflammation**: highlighted in inflammatory PASC subgroup; linked to microclots. (talla2023persistentserumprotein pages 11-12, turner2024increasedlevelsof pages 1-2)
5. **Inflammasome activation (NLRP3-related)**: noted in reviews and severe post‑COVID ARDS cohort markers; endothelial model shows inflammatory transcript induction. (alfaro2024endothelialdysfunctionand pages 5-8, gusev2024exploringthepathophysiology pages 2-4)
6. **Endothelial barrier maintenance / vascular permeability and leukocyte adhesion**: endothelial injury and persistent endotheliopathy described; biomarkers ICAM‑1/PECAM‑1/E‑selectin. (wu2024damagetoendothelial pages 1-2, turner2024increasedlevelsof pages 1-2)
7. **Blood coagulation and fibrinolysis / hypofibrinolysis**: microclots and α‑2 antiplasmin elevations; thrombotic endothelialitis model. (turner2024increasedlevelsof pages 1-2)
8. **Oxidative phosphorylation and mitochondrial respiration**: reduced OXPHOS capacity and post‑exercise mitochondrial enzyme activity changes; metabolic shift away from TCA cycle. (appelman2024muscleabnormalitiesworsen pages 5-6, appelman2024muscleabnormalitiesworsen pages 3-4)

## 5) Cellular components (where key processes occur)

Supported cellular component categories include:
- **Plasma/serum** (antigenemia; cytokines; proteomics signatures). (ra2024viralimmunologicand pages 2-4, talla2023persistentserumprotein pages 10-11)
- **Extracellular vesicles** (review-level evidence of viral/mitochondrial proteins in exosomes in long COVID synthesis). (peluso2024mechanismsoflong pages 38-40)
- **Endothelial glycocalyx** (shedding; barrier dysfunction). (wu2024damagetoendothelial pages 1-2)
- **Extracellular matrix** (muscle nucleocapsid localization and amyloid deposits were extracellular/adjacent to endothelium). (appelman2024muscleabnormalitiesworsen pages 5-6, appelman2024muscleabnormalitiesworsen pages 6-7)
- **Mitochondrion** (OXPHOS capacity; SDH activity). (appelman2024muscleabnormalitiesworsen pages 5-6)
- **Inflammasome complex (NLRP3-associated)** (monocyte MFI readouts; endothelial pyroptosis markers). (alfaro2024endothelialdysfunctionand pages 5-8)
- **Blood–brain barrier and other endothelial barriers** (review synthesis of multi-organ endothelial barriers: blood–air, blood–brain, glomerular filtration, intestinal–blood). (wu2024damagetoendothelial pages 1-2)

## 6) Disease progression model (sequence of events)

A synthesis consistent across recent authoritative sources supports the following progression:

1. **Acute infection determinants**: high viral burden, RNAemia, and prolonged clearance correlate with later long COVID risk; Omicron may reduce risk via lower acute burden; vaccines and early antivirals are indirect evidence for this stage. (peluso2024mechanismsoflong pages 6-8)
2. **Post-acute persistence/antigenemia**: viral RNA/protein persists in tissue reservoirs (GI, lymphoid, lung) and can lead to ongoing antigenemia (e.g., NP antigen at 3 months) that may sustain immune activation. (proal2023sarscov2reservoirin pages 4-6, ra2024viralimmunologicand pages 2-4)
3. **Chronic immune activation and endotypes**: some patients exhibit persistent IFN‑γ/TNF/NF‑κB inflammatory signatures; others show neutrophil/NETosis/type I IFN–associated patterns; cytokines/chemokines (IL‑2, IL‑17A, CXCL10/11) remain elevated beyond 1 month in PASC. (talla2023persistentserumprotein pages 6-7, ra2024viralimmunologicand pages 5-6)
4. **Endothelial dysfunction and thromboinflammation**: persistent endothelial activation (ICAM‑1, vWF, thrombin, FVIII), glycocalyx shedding, microclots/hypofibrinolysis (α‑2AP; PF4; VWF; SAA) drive microvascular hypoperfusion and organ dysfunction. (wu2024damagetoendothelial pages 1-2, turner2024increasedlevelsof pages 1-2)
5. **Downstream organ phenotypes**: impaired gas exchange post‑ARDS with endotheliitis markers; skeletal muscle metabolic failure with reduced OXPHOS, TCA depletion, amyloid deposits and immune infiltration, manifesting as PEM/exercise intolerance. (alfaro2024endothelialdysfunctionand pages 1-2, appelman2024muscleabnormalitiesworsen pages 5-6)

## 7) Phenotypic manifestations and links to mechanisms (HP-style mapping)

Below are key phenotypes supported by the evidence corpus and their mechanistic anchors.

- **Fatigue (HP:0001254)** and **post‑exertional malaise (HP:0030974)**: supported by muscle OXPHOS impairment and metabolomic shift toward glycolysis with TCA depletion; structural myopathy and immune infiltration worsen after exertion. (appelman2024muscleabnormalitiesworsen pages 5-6, appelman2024muscleabnormalitiesworsen pages 8-9)
- **Exercise intolerance (HP:0003546)**: reduced V̇O2max/peak power; reduced peripheral O2 extraction and impaired mitochondrial activity after exercise. (appelman2024muscleabnormalitiesworsen pages 3-4)
- **Dyspnea / impaired gas exchange (HP:0002094 / HP:0011949)**: 6‑month post‑ICU ARDS survivors with low DLCO show persistent endothelial inflammation and systemic inflammation; multivariable marker panel discriminated DLCO status (AUC 0.854). (alfaro2024endothelialdysfunctionand pages 5-8)
- **Cognitive dysfunction/“brain fog” (HP:0100543)**: frequently reported in definitions/reviews as a core symptom cluster; mechanistic linkage is typically proposed via neuroinflammation/vascular dysfunction rather than proven in the specific evidence snippets extracted here. (untersmayr2024immunemechanismsunderpinning pages 2-2)

## 8) Current applications and real-world implementations

### 8.1 Biomarker translation and patient stratification
- **Inflammatory PASC stratification panel:** 3‑protein panel (CCL7, CD40LG, S100A12) with AUROC values reported for classifying inflammatory PASC. (talla2023persistentserumprotein pages 10-11)
- **Persistent antigenemia monitoring:** NP antigenemia trajectories and ROC performance (AUC 0.687) suggest a candidate biomarker for a subset of patients and mechanistic trial enrichment. (ra2024viralimmunologicand pages 2-4)
- **Endotheliopathy panel candidates:** soluble VWF, PF4, SAA, α‑2AP, E‑selectin, PECAM‑1 are proposed as clinically testable markers of thrombotic endothelialitis. (turner2024increasedlevelsof pages 1-2)

### 8.2 Interventional trials (ClinicalTrials.gov)
Trials retrieved via registry search reflect active translation of mechanistic hypotheses into therapeutics:
- **Nirmatrelvir/ritonavir (Paxlovid)** for prevention or treatment (e.g., decentralized phase 2 long COVID study; platform protocols). Examples include **NCT05668091**, **NCT05576662**, **NCT05965726**, and a large prevention trial **NCT05852873**. (peluso2024mechanismsoflong pages 6-8)
- **Immunoadsorption (autoantibody/immune complex targeting)**: sham-controlled and other designs (e.g., **NCT05954325**, **NCT05841498**, **NCT07316127**). (peluso2024mechanismsoflong pages 6-8)
- **Ivabradine for POTS cohort**: **NCT05481177** reflects autonomic phenotype targeting. (peluso2024mechanismsoflong pages 6-8)

## 9) Expert opinions and authoritative syntheses (2023–2024)

- A Keystone Symposia report summarizes emerging themes: inflammation/immune alterations potentially related to viral persistence and tissue dysfunction (endothelium, nervous system, mitochondria) and emphasizes replication of major findings and mechanism-focused randomized trials. (durstenfeld2024longcovidand pages 16-17)
- A Cell 2024 review frames long COVID as a mechanistically diverse condition with viral persistence, endothelial involvement, gut-derived inflammation, mitochondrial dysfunction and the need for preventive antiviral trial designs. (peluso2024mechanismsoflong pages 6-8, peluso2024mechanismsoflong pages 38-40)

## 10) Evidence items list (PMID/DOI where available)

PMIDs were not consistently present in extracted text; DOIs/URLs are provided for traceability.

- **Proal et al.** *SARS‑CoV‑2 reservoir in post‑acute sequelae of COVID‑19 (PASC)*. **Nature Immunology**. Publication date: **Sep 2023**. DOI/URL: https://doi.org/10.1038/s41590-023-01601-2 (proal2023sarscov2reservoirin pages 4-6)
- **Talla et al.** *Persistent serum protein signatures define an inflammatory subcategory of long COVID*. **Nature Communications**. Publication date: **Jun 2023**. DOI/URL: https://doi.org/10.1038/s41467-023-38682-4 (talla2023persistentserumprotein pages 6-7, talla2023persistentserumprotein pages 10-11)
- **Wu et al.** *Damage to endothelial barriers and its contribution to long COVID*. **Angiogenesis**. Publication date: **Apr 2024**. DOI/URL: https://doi.org/10.1007/s10456-023-09878-5 (wu2024damagetoendothelial pages 1-2)
- **Alfaro et al.** *Endothelial dysfunction and persistent inflammation in severe post‑COVID‑19 patients: implications for gas exchange*. **BMC Medicine**. Publication date: **Jun 2024**. DOI/URL: https://doi.org/10.1186/s12916-024-03461-5 (alfaro2024endothelialdysfunctionand pages 1-2)
- **Ra et al.** *Viral, Immunologic, and Laboratory Parameters in Patients With and Without PASC*. **Journal of Korean Medical Science**. Publication date: **Jul 2024**. DOI/URL: https://doi.org/10.3346/jkms.2024.39.e237 (ra2024viralimmunologicand pages 2-4)
- **Turner et al.** *Increased Levels of Inflammatory and Endothelial Biomarkers in Blood of Long COVID Patients Point to Thrombotic Endothelialitis*. **Seminars in Thrombosis and Hemostasis**. Publication date: **May 2024**. DOI/URL: https://doi.org/10.1055/s-0043-1769014 (turner2024increasedlevelsof pages 1-2)
- **Appelman et al.** *Muscle abnormalities worsen after post‑exertional malaise in long COVID*. **Nature Communications**. Publication date: **Jan 2024**. DOI/URL: https://doi.org/10.1038/s41467-023-44432-3 (appelman2024muscleabnormalitiesworsen pages 5-6, appelman2024muscleabnormalitiesworsen pages 6-7)
- **Untersmayr et al.** *Immune Mechanisms Underpinning Long COVID: Update 2024*. **International Archives of Allergy and Immunology**. Publication date: **Jan 2024**. DOI/URL: https://doi.org/10.1159/000535736 (untersmayr2024immunemechanismsunderpinning pages 1-2)
- **Peluso & Deeks.** *Mechanisms of long COVID and the path toward therapeutics*. **Cell**. Publication date: **Oct 2024**. DOI/URL: https://doi.org/10.1016/j.cell.2024.07.054 (peluso2024mechanismsoflong pages 6-8)

## Limitations of this report
- **MONDO ID not retrieved:** No explicit MONDO identifier was present in the retrieved full-text evidence.
- **Autoantibody specificity:** Several sources note autoimmunity conceptually, but specific mechanistic/quantitative evidence for GPCR/anti‑IFN/anti‑ACE2 autoantibodies was not captured in the extracted snippets used here.
- **PMIDs:** Many extracted sections did not include PMIDs; DOIs were available for key sources.


References

1. (untersmayr2024immunemechanismsunderpinning pages 2-2): Eva Untersmayr, Carina Venter, Peter Smith, Johanna Rohrhofer, Cebile Ndwandwe, Jurgen Schwarze, Emer Shannon, Milena Sokolowska, Corinna Sadlier, and Liam O’Mahony. Immune mechanisms underpinning long covid: collegium internationale allergologicum update 2024. International Archives of Allergy and Immunology, 185:489-502, Jan 2024. URL: https://doi.org/10.1159/000535736, doi:10.1159/000535736. This article has 17 citations and is from a peer-reviewed journal.

2. (untersmayr2024immunemechanismsunderpinning pages 1-2): Eva Untersmayr, Carina Venter, Peter Smith, Johanna Rohrhofer, Cebile Ndwandwe, Jurgen Schwarze, Emer Shannon, Milena Sokolowska, Corinna Sadlier, and Liam O’Mahony. Immune mechanisms underpinning long covid: collegium internationale allergologicum update 2024. International Archives of Allergy and Immunology, 185:489-502, Jan 2024. URL: https://doi.org/10.1159/000535736, doi:10.1159/000535736. This article has 17 citations and is from a peer-reviewed journal.

3. (talla2023persistentserumprotein pages 6-7): Aarthi Talla, Suhas V. Vasaikar, Gregory Lee Szeto, Maria P. Lemos, Julie L. Czartoski, Hugh MacMillan, Zoe Moodie, Kristen W. Cohen, Lamar B. Fleming, Zachary Thomson, Lauren Okada, Lynne A. Becker, Ernest M. Coffey, Stephen C. De Rosa, Evan W. Newell, Peter J. Skene, Xiaojun Li, Thomas F. Bumol, M. Juliana McElrath, and Troy R. Torgerson. Persistent serum protein signatures define an inflammatory subcategory of long covid. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38682-4, doi:10.1038/s41467-023-38682-4. This article has 115 citations and is from a highest quality peer-reviewed journal.

4. (talla2023persistentserumprotein pages 1-2): Aarthi Talla, Suhas V. Vasaikar, Gregory Lee Szeto, Maria P. Lemos, Julie L. Czartoski, Hugh MacMillan, Zoe Moodie, Kristen W. Cohen, Lamar B. Fleming, Zachary Thomson, Lauren Okada, Lynne A. Becker, Ernest M. Coffey, Stephen C. De Rosa, Evan W. Newell, Peter J. Skene, Xiaojun Li, Thomas F. Bumol, M. Juliana McElrath, and Troy R. Torgerson. Persistent serum protein signatures define an inflammatory subcategory of long covid. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38682-4, doi:10.1038/s41467-023-38682-4. This article has 115 citations and is from a highest quality peer-reviewed journal.

5. (proal2023sarscov2reservoirin pages 4-6): Amy D. Proal, Michael B. VanElzakker, Soo Aleman, Katie Bach, Brittany P. Boribong, Marcus Buggert, Sara Cherry, Daniel S. Chertow, Helen E. Davies, Christopher L. Dupont, Steven G. Deeks, William Eimer, E. Wesley Ely, Alessio Fasano, Marcelo Freire, Linda N. Geng, Diane E. Griffin, Timothy J. Henrich, Akiko Iwasaki, David Izquierdo-Garcia, Michela Locci, Saurabh Mehandru, Mark M. Painter, Michael J. Peluso, Etheresia Pretorius, David A. Price, David Putrino, Richard H. Scheuermann, Gene S. Tan, Rudolph E. Tanzi, Henry F. VanBrocklin, Lael M. Yonker, and E. John Wherry. Sars-cov-2 reservoir in post-acute sequelae of covid-19 (pasc). Nature Immunology, 24:1616-1627, Sep 2023. URL: https://doi.org/10.1038/s41590-023-01601-2, doi:10.1038/s41590-023-01601-2. This article has 323 citations and is from a highest quality peer-reviewed journal.

6. (gusev2024exploringthepathophysiology pages 2-4): Evgenii Gusev and Alexey Sarapultsev. Exploring the pathophysiology of long covid: the central role of low-grade inflammation and multisystem involvement. International Journal of Molecular Sciences, 25:6389, Jun 2024. URL: https://doi.org/10.3390/ijms25126389, doi:10.3390/ijms25126389. This article has 37 citations.

7. (ra2024viralimmunologicand pages 2-4): Sang Hyun Ra, Euijin Chang, Ji-Soo Kwon, Ji Yeun Kim, JuYeon Son, Woori Kim, Choi Young Jang, Hyeon Mu Jang, Seongman Bae, Jiwon Jung, Min Jae Kim, Yong Pil Chong, Sang-Oh Lee, Sang-Ho Choi, Yang Soo Kim, Keun Hwa Lee, and Sung-Han Kim. Viral, immunologic, and laboratory parameters in patients with and without post-acute sequelae of sars-cov-2 infection (pasc). Journal of Korean Medical Science, Jul 2024. URL: https://doi.org/10.3346/jkms.2024.39.e237, doi:10.3346/jkms.2024.39.e237. This article has 3 citations and is from a peer-reviewed journal.

8. (peluso2024mechanismsoflong pages 6-8): Michael J. Peluso and Steven G. Deeks. Mechanisms of long covid and the path toward therapeutics. Oct 2024. URL: https://doi.org/10.1016/j.cell.2024.07.054, doi:10.1016/j.cell.2024.07.054. This article has 249 citations and is from a highest quality peer-reviewed journal.

9. (talla2023persistentserumprotein pages 10-11): Aarthi Talla, Suhas V. Vasaikar, Gregory Lee Szeto, Maria P. Lemos, Julie L. Czartoski, Hugh MacMillan, Zoe Moodie, Kristen W. Cohen, Lamar B. Fleming, Zachary Thomson, Lauren Okada, Lynne A. Becker, Ernest M. Coffey, Stephen C. De Rosa, Evan W. Newell, Peter J. Skene, Xiaojun Li, Thomas F. Bumol, M. Juliana McElrath, and Troy R. Torgerson. Persistent serum protein signatures define an inflammatory subcategory of long covid. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38682-4, doi:10.1038/s41467-023-38682-4. This article has 115 citations and is from a highest quality peer-reviewed journal.

10. (ra2024viralimmunologicand pages 5-6): Sang Hyun Ra, Euijin Chang, Ji-Soo Kwon, Ji Yeun Kim, JuYeon Son, Woori Kim, Choi Young Jang, Hyeon Mu Jang, Seongman Bae, Jiwon Jung, Min Jae Kim, Yong Pil Chong, Sang-Oh Lee, Sang-Ho Choi, Yang Soo Kim, Keun Hwa Lee, and Sung-Han Kim. Viral, immunologic, and laboratory parameters in patients with and without post-acute sequelae of sars-cov-2 infection (pasc). Journal of Korean Medical Science, Jul 2024. URL: https://doi.org/10.3346/jkms.2024.39.e237, doi:10.3346/jkms.2024.39.e237. This article has 3 citations and is from a peer-reviewed journal.

11. (ra2024viralimmunologicand pages 1-2): Sang Hyun Ra, Euijin Chang, Ji-Soo Kwon, Ji Yeun Kim, JuYeon Son, Woori Kim, Choi Young Jang, Hyeon Mu Jang, Seongman Bae, Jiwon Jung, Min Jae Kim, Yong Pil Chong, Sang-Oh Lee, Sang-Ho Choi, Yang Soo Kim, Keun Hwa Lee, and Sung-Han Kim. Viral, immunologic, and laboratory parameters in patients with and without post-acute sequelae of sars-cov-2 infection (pasc). Journal of Korean Medical Science, Jul 2024. URL: https://doi.org/10.3346/jkms.2024.39.e237, doi:10.3346/jkms.2024.39.e237. This article has 3 citations and is from a peer-reviewed journal.

12. (wu2024damagetoendothelial pages 1-2): Xiaoming Wu, Mengqi Xiang, Haijiao Jing, Chengyue Wang, Valerie A. Novakovic, and Jialan Shi. Damage to endothelial barriers and its contribution to long covid. Angiogenesis, 27:1-18, Apr 2024. URL: https://doi.org/10.1007/s10456-023-09878-5, doi:10.1007/s10456-023-09878-5. This article has 102 citations and is from a domain leading peer-reviewed journal.

13. (alfaro2024endothelialdysfunctionand pages 1-2): Enrique Alfaro, Elena Díaz-García, Sara García-Tovar, Raúl Galera, Raquel Casitas, María Torres-Vargas, Cristina López-Fernández, José M. Añón, Francisco García-Río, and Carolina Cubillos-Zapata. Endothelial dysfunction and persistent inflammation in severe post-covid-19 patients: implications for gas exchange. BMC Medicine, Jun 2024. URL: https://doi.org/10.1186/s12916-024-03461-5, doi:10.1186/s12916-024-03461-5. This article has 29 citations and is from a domain leading peer-reviewed journal.

14. (alfaro2024endothelialdysfunctionand pages 8-10): Enrique Alfaro, Elena Díaz-García, Sara García-Tovar, Raúl Galera, Raquel Casitas, María Torres-Vargas, Cristina López-Fernández, José M. Añón, Francisco García-Río, and Carolina Cubillos-Zapata. Endothelial dysfunction and persistent inflammation in severe post-covid-19 patients: implications for gas exchange. BMC Medicine, Jun 2024. URL: https://doi.org/10.1186/s12916-024-03461-5, doi:10.1186/s12916-024-03461-5. This article has 29 citations and is from a domain leading peer-reviewed journal.

15. (turner2024increasedlevelsof pages 1-2): BSc Simone Turner, BSc Caitlin A. Naidoo, BSc Thomas J. Usher, MD Arneaux Kruger, PhD Chantelle Venter, MD Gert J. Laubscher, Frcp M Asad Khan, PhD Douglas B. Kell, and PhD Etheresia Pretorius. Increased levels of inflammatory and endothelial biomarkers in blood of long covid patients point to thrombotic endothelialitis. Seminars in Thrombosis and Hemostasis, 50:288-294, May 2024. URL: https://doi.org/10.1055/s-0043-1769014, doi:10.1055/s-0043-1769014. This article has 50 citations and is from a peer-reviewed journal.

16. (appelman2024muscleabnormalitiesworsen pages 3-4): Brent Appelman, Braeden T. Charlton, Richie P. Goulding, Tom J. Kerkhoff, Ellen A. Breedveld, Wendy Noort, Carla Offringa, Frank W. Bloemers, Michel van Weeghel, Bauke V. Schomakers, Pedro Coelho, Jelle J. Posthuma, Eleonora Aronica, W. Joost Wiersinga, Michèle van Vugt, and Rob C. I. Wüst. Muscle abnormalities worsen after post-exertional malaise in long covid. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44432-3, doi:10.1038/s41467-023-44432-3. This article has 346 citations and is from a highest quality peer-reviewed journal.

17. (appelman2024muscleabnormalitiesworsen pages 2-3): Brent Appelman, Braeden T. Charlton, Richie P. Goulding, Tom J. Kerkhoff, Ellen A. Breedveld, Wendy Noort, Carla Offringa, Frank W. Bloemers, Michel van Weeghel, Bauke V. Schomakers, Pedro Coelho, Jelle J. Posthuma, Eleonora Aronica, W. Joost Wiersinga, Michèle van Vugt, and Rob C. I. Wüst. Muscle abnormalities worsen after post-exertional malaise in long covid. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44432-3, doi:10.1038/s41467-023-44432-3. This article has 346 citations and is from a highest quality peer-reviewed journal.

18. (appelman2024muscleabnormalitiesworsen pages 5-6): Brent Appelman, Braeden T. Charlton, Richie P. Goulding, Tom J. Kerkhoff, Ellen A. Breedveld, Wendy Noort, Carla Offringa, Frank W. Bloemers, Michel van Weeghel, Bauke V. Schomakers, Pedro Coelho, Jelle J. Posthuma, Eleonora Aronica, W. Joost Wiersinga, Michèle van Vugt, and Rob C. I. Wüst. Muscle abnormalities worsen after post-exertional malaise in long covid. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44432-3, doi:10.1038/s41467-023-44432-3. This article has 346 citations and is from a highest quality peer-reviewed journal.

19. (appelman2024muscleabnormalitiesworsen pages 6-7): Brent Appelman, Braeden T. Charlton, Richie P. Goulding, Tom J. Kerkhoff, Ellen A. Breedveld, Wendy Noort, Carla Offringa, Frank W. Bloemers, Michel van Weeghel, Bauke V. Schomakers, Pedro Coelho, Jelle J. Posthuma, Eleonora Aronica, W. Joost Wiersinga, Michèle van Vugt, and Rob C. I. Wüst. Muscle abnormalities worsen after post-exertional malaise in long covid. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44432-3, doi:10.1038/s41467-023-44432-3. This article has 346 citations and is from a highest quality peer-reviewed journal.

20. (bohmwald2024pathophysiologicalimmunologicaland pages 12-12): Karen Bohmwald, Benjamín Diethelm-Varela, Linmar Rodríguez-Guilarte, Thomas Rivera, Claudia A. Riedel, Pablo A. González, and Alexis M. Kalergis. Pathophysiological, immunological, and inflammatory features of long covid. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1341600, doi:10.3389/fimmu.2024.1341600. This article has 72 citations and is from a peer-reviewed journal.

21. (alfaro2024endothelialdysfunctionand pages 5-8): Enrique Alfaro, Elena Díaz-García, Sara García-Tovar, Raúl Galera, Raquel Casitas, María Torres-Vargas, Cristina López-Fernández, José M. Añón, Francisco García-Río, and Carolina Cubillos-Zapata. Endothelial dysfunction and persistent inflammation in severe post-covid-19 patients: implications for gas exchange. BMC Medicine, Jun 2024. URL: https://doi.org/10.1186/s12916-024-03461-5, doi:10.1186/s12916-024-03461-5. This article has 29 citations and is from a domain leading peer-reviewed journal.

22. (proal2023sarscov2reservoirin pages 8-10): Amy D. Proal, Michael B. VanElzakker, Soo Aleman, Katie Bach, Brittany P. Boribong, Marcus Buggert, Sara Cherry, Daniel S. Chertow, Helen E. Davies, Christopher L. Dupont, Steven G. Deeks, William Eimer, E. Wesley Ely, Alessio Fasano, Marcelo Freire, Linda N. Geng, Diane E. Griffin, Timothy J. Henrich, Akiko Iwasaki, David Izquierdo-Garcia, Michela Locci, Saurabh Mehandru, Mark M. Painter, Michael J. Peluso, Etheresia Pretorius, David A. Price, David Putrino, Richard H. Scheuermann, Gene S. Tan, Rudolph E. Tanzi, Henry F. VanBrocklin, Lael M. Yonker, and E. John Wherry. Sars-cov-2 reservoir in post-acute sequelae of covid-19 (pasc). Nature Immunology, 24:1616-1627, Sep 2023. URL: https://doi.org/10.1038/s41590-023-01601-2, doi:10.1038/s41590-023-01601-2. This article has 323 citations and is from a highest quality peer-reviewed journal.

23. (appelman2024muscleabnormalitiesworsen pages 8-9): Brent Appelman, Braeden T. Charlton, Richie P. Goulding, Tom J. Kerkhoff, Ellen A. Breedveld, Wendy Noort, Carla Offringa, Frank W. Bloemers, Michel van Weeghel, Bauke V. Schomakers, Pedro Coelho, Jelle J. Posthuma, Eleonora Aronica, W. Joost Wiersinga, Michèle van Vugt, and Rob C. I. Wüst. Muscle abnormalities worsen after post-exertional malaise in long covid. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44432-3, doi:10.1038/s41467-023-44432-3. This article has 346 citations and is from a highest quality peer-reviewed journal.

24. (talla2023persistentserumprotein pages 11-12): Aarthi Talla, Suhas V. Vasaikar, Gregory Lee Szeto, Maria P. Lemos, Julie L. Czartoski, Hugh MacMillan, Zoe Moodie, Kristen W. Cohen, Lamar B. Fleming, Zachary Thomson, Lauren Okada, Lynne A. Becker, Ernest M. Coffey, Stephen C. De Rosa, Evan W. Newell, Peter J. Skene, Xiaojun Li, Thomas F. Bumol, M. Juliana McElrath, and Troy R. Torgerson. Persistent serum protein signatures define an inflammatory subcategory of long covid. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38682-4, doi:10.1038/s41467-023-38682-4. This article has 115 citations and is from a highest quality peer-reviewed journal.

25. (proal2023sarscov2reservoirin pages 10-12): Amy D. Proal, Michael B. VanElzakker, Soo Aleman, Katie Bach, Brittany P. Boribong, Marcus Buggert, Sara Cherry, Daniel S. Chertow, Helen E. Davies, Christopher L. Dupont, Steven G. Deeks, William Eimer, E. Wesley Ely, Alessio Fasano, Marcelo Freire, Linda N. Geng, Diane E. Griffin, Timothy J. Henrich, Akiko Iwasaki, David Izquierdo-Garcia, Michela Locci, Saurabh Mehandru, Mark M. Painter, Michael J. Peluso, Etheresia Pretorius, David A. Price, David Putrino, Richard H. Scheuermann, Gene S. Tan, Rudolph E. Tanzi, Henry F. VanBrocklin, Lael M. Yonker, and E. John Wherry. Sars-cov-2 reservoir in post-acute sequelae of covid-19 (pasc). Nature Immunology, 24:1616-1627, Sep 2023. URL: https://doi.org/10.1038/s41590-023-01601-2, doi:10.1038/s41590-023-01601-2. This article has 323 citations and is from a highest quality peer-reviewed journal.

26. (peluso2024mechanismsoflong pages 38-40): Michael J. Peluso and Steven G. Deeks. Mechanisms of long covid and the path toward therapeutics. Oct 2024. URL: https://doi.org/10.1016/j.cell.2024.07.054, doi:10.1016/j.cell.2024.07.054. This article has 249 citations and is from a highest quality peer-reviewed journal.

27. (durstenfeld2024longcovidand pages 16-17): Matthew S. Durstenfeld, Shannon Weiman, Michael Holtzman, Catherine Blish, Resia Pretorius, and Steven G. Deeks. Long covid and post-acute sequelae of sars-cov-2 pathogenesis and treatment: a keystone symposia report. Annals of the New York Academy of Sciences, 1535:31-41, Apr 2024. URL: https://doi.org/10.1111/nyas.15132, doi:10.1111/nyas.15132. This article has 7 citations and is from a peer-reviewed journal.