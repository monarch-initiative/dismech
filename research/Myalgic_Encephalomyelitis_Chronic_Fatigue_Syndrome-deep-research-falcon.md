---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-17T18:36:36.769363'
end_time: '2026-03-17T18:47:43.481902'
duration_seconds: 666.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Myalgic Encephalomyelitis/Chronic Fatigue Syndrome**.
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
- **Disease Name:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Myalgic Encephalomyelitis/Chronic Fatigue Syndrome**.
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


## Research report: Pathophysiology of Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS)

### Disease entity and scope
**Disease:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS).  
**Category:** Complex, multisystem disorder characterized clinically by post-exertional symptom exacerbation (often termed post-exertional malaise; PEM) and heterogeneous neurological, autonomic, immune, and metabolic manifestations. Recent syntheses emphasize a *multifactorial, network-like* pathophysiology arising from genetic vulnerability plus environmental triggers (commonly infections) that converge on persistent immune dysregulation, autonomic dysfunction, metabolic disturbances, and (in some cohorts) vascular/endothelial and coagulation abnormalities. (arron2024myalgicencephalomyelitischronicfatigue pages 1-2, walitt2024deepphenotypingof pages 1-2)

**MONDO ID:** Not retrieved in the current evidence set.

---

## 1) Core pathophysiology (current understanding)

### 1.1 Immune dysregulation and chronic antigenic stimulation
A consistent theme across recent high-quality studies is chronic immune perturbation compatible with persistent antigenic stimulation.

* **B-cell compartment shifts (post-infectious ME/CFS):** Deep phenotyping of a rigorously adjudicated post-infectious cohort reported an “increase in naïve and decrease in switched memory B-cells,” interpreted as evidence consistent with chronic antigenic stimulation. (walitt2024deepphenotypingof pages 1-2)
* **Natural killer (NK) cell dysfunction (most reproducible immune phenotype):** A 2024 registered meta-analysis of NK cytotoxicity across 28 papers (55 effector:target datapoints) found NK cytotoxicity in ME/CFS was reduced to about half of healthy control levels, with an overall effect size **Hedges’ g = 0.96 (95% CI 0.75–1.18)**. (baraniuk2024metaanalysisofnatural pages 1-2)
* **T-cell exhaustion programs (emerging 2024 theme):** Multi-omic analyses of CD8+ T cells support epigenetic/transcriptional priming toward exhaustion, with exhaustion markers reportedly upregulated after exercise provocation, consistent with chronic antigen exposure models (e.g., persistent/latent viral drivers as one plausible upstream contributor). (iu2024transcriptionalreprogrammingprimes pages 1-2)

**Interpretation:** Immune phenotypes span innate cytotoxic impairment (NK), adaptive exhaustion-like programs (CD8), and altered memory differentiation (B-cells). Together, these can plausibly reduce pathogen control (or promote antigen persistence), while also sustaining inflammatory signaling that couples to autonomic and metabolic dysfunction. (baraniuk2024metaanalysisofnatural pages 1-2, walitt2024deepphenotypingof pages 1-2, iu2024transcriptionalreprogrammingprimes pages 1-2)

### 1.2 Autonomic nervous system (ANS) dysregulation and neurovascular consequences
Autonomic abnormalities are prominent in recent physiologic profiling.

* In post-infectious ME/CFS deep phenotyping, autonomic testing supported altered sympathetic/parasympathetic features, including prolonged blood pressure recovery after Valsalva (**4.1 ± 0.4 s vs 3.0 ± 0.2 s in controls; p = 0.014**). (walitt2024deepphenotypingof pages 1-2)
* Orthostatic intolerance and cerebral blood flow (CBF) abnormalities are described as common, with one synthesis reporting that **90% (384/429) exceeded a 13% CBF reduction cutoff**, with **mean CBF reduction 26% vs 7%** in controls, and substantial rates of orthostatic symptoms (e.g., **72% [32/39] light-headedness on standing**). (nunes2024assessingthecoagulation pages 33-36)
* In a 2024 prospective pilot cohort that compared ME/CFS, long COVID, and controls, **POTS** was identified during a 10-min NASA lean test in **13% (4/31)** of ME/CFS participants. (graves2024chronicfatiguesyndrome pages 5-7)

**Interpretation:** ANS dysregulation provides a mechanistic bridge from immune/inflammatory signaling to impaired perfusion regulation, symptom flares with orthostatic or exertional stress, and downstream energy limitation. (walitt2024deepphenotypingof pages 1-2, nunes2024assessingthecoagulation pages 33-36, graves2024chronicfatiguesyndrome pages 5-7)

### 1.3 Endothelial dysfunction, coagulation pathway disturbance, and complement downregulation
Multiple recent datasets implicate vascular/endothelial and coagulation biology.

* **Endothelial biomarkers and inflammation:** ME/CFS and long COVID groups showed higher ET-1 and VCAM-1 and lower nitrite/nitrate (NOx) than controls; ME/CFS additionally showed higher PAI-1 and E-selectin than both long COVID and controls (p-values reported in the study abstract). (graves2024chronicfatiguesyndrome pages 5-7)
* **Plasma proteomics (DIA LC-MS/MS):** In platelet-poor plasma from **15 ME/CFS vs 10 controls**, 45 proteins were differentially expressed (**24 up, 21 down; p < 0.05**). Large-magnitude examples include **lactotransferrin up to 8.38-fold (p = 0.00009)**, **thrombospondin-1 ~3.48–3.75-fold (p ≤ 0.0002)**, **platelet factor 4 3.11-fold (p = 0.00009)**, **protein S 0.48-fold (p = 0.0006)**, and **complement C9 0.17-fold (p = 0.0001)**. (nunes2024dataindependentlcmsmsanalysis pages 5-7)

**Interpretation:** These patterns support a model in which endothelial activation/dysfunction and platelet/coagulation signaling contribute to impaired oxygen/nutrient delivery under stress and may interact with inflammatory tone and autonomic dysregulation. Complement downregulation (e.g., C9) may reflect altered innate effector pathways or chronic immune modulation. (nunes2024dataindependentlcmsmsanalysis pages 5-7, graves2024chronicfatiguesyndrome pages 5-7)

### 1.4 Neurological dysfunction and neuroaxonal injury signals
Neurological impairment is core to patient experience (“brain fog,” cognitive dysfunction) and is increasingly probed using blood biomarkers.

* **Plasma neurofilament light chain (NfL):** In **67 ME/CFS vs 43 controls**, NfL was higher in ME/CFS (**F = 4.30, p < 0.05**) and correlated with worse cognition (visuospatial perception **r = −0.42, p ≤ 0.001**; verbal memory **r = −0.35, p ≤ 0.005**; visual memory **r = −0.26, p < 0.05**). NfL explained up to **17.2%** of variance in cognitive tests and associated with parasympathetic dysfunction (**F = 9.48, p ≤ 0.003**). (azcue2024plasmaneurofilamentlight pages 1-2)
* **Central catechol pathway dysregulation hypothesis (deep phenotyping):** Behavioral findings (altered effort preference) were linked to dysfunction of integrative brain regions and “central catechol pathway dysregulation,” consistent with a brain–autonomic–immune interface model. (walitt2024deepphenotypingof pages 1-2)

**Interpretation:** NfL provides convergent evidence for measurable neuroaxonal injury/stress in a subset and supports integrating central nervous system involvement into mechanistic models alongside ANS and immune alterations. (azcue2024plasmaneurofilamentlight pages 1-2, walitt2024deepphenotypingof pages 1-2)

### 1.5 Metabolic/mitochondrial dysfunction and the “energy limitation” phenotype
Recent reviews and multi-omic studies consistently emphasize metabolic disturbance as a contributor to exertion intolerance.

* A 2024 synthesis frames ME/CFS as involving metabolic disturbances alongside immune dysregulation, inflammation, and gut dysbiosis, supporting an integrated “systems” model rather than single-pathway causation. (arron2024myalgicencephalomyelitischronicfatigue pages 1-2)
* Deep phenotyping reported alterations in PBMC gene expression and metabolic pathways (with sex-specific differences), consistent with immune–metabolic coupling. (walitt2024deepphenotypingof pages 1-2)

**Interpretation:** While the mechanistic target is not yet unified, metabolic reprogramming appears to be a downstream integrator of immune and neurovascular stressors—particularly relevant to PEM. (walitt2024deepphenotypingof pages 1-2, arron2024myalgicencephalomyelitischronicfatigue pages 1-2)

### 1.6 Microbiome and gut–immune interactions
Several contemporary reviews highlight gut dysbiosis and reduced short-chain fatty acid (SCFA) production as plausible amplifiers of systemic inflammation and metabolic dysfunction, though cohort-specific causality remains unresolved in the evidence excerpts available here. (graves2024chronicfatiguesyndrome pages 4-5, graves2024chronicfatiguesyndrome pages 5-7)

---

## 2) Recent developments (prioritizing 2023–2024)

### 2.1 Deep phenotyping defines candidate mechanistic axes (2024)
A major 2024 advance is the use of rigorous case adjudication plus broad deep phenotyping to link clinical signatures (including effort preference/behavioral changes) to autonomic function, immune profiles, and multi-omic differences in post-infectious ME/CFS. Key quantitative signals include Valsalva recovery differences (p = 0.014) and an effort-choice odds ratio (OR 1.65, p = 0.04). (walitt2024deepphenotypingof pages 1-2)

### 2.2 Endothelium–inflammation biomarker panels differentiate ME/CFS from long COVID (2024)
The prospective pilot cohort approach combining endothelial and inflammatory markers with symptom severity measures provides a step toward stratification and differential diagnosis, including a measurable POTS proportion under standardized orthostatic testing (13% in ME/CFS). (graves2024chronicfatiguesyndrome pages 5-7)

### 2.3 Plasma proteomics strengthens coagulation/endothelial/complement hypotheses (2024)
The 2024 DIA LC-MS/MS study provides explicit protein-level effect sizes supporting platelet activation (PF4), endothelial/coagulation regulation (THBS1, PROS1), and complement attenuation (C9), generating tractable biomarkers for replication and mechanistic follow-up. (nunes2024dataindependentlcmsmsanalysis pages 5-7)

### 2.4 Immune exhaustion and cytotoxic impairment are converging mechanistic themes (2024)
The NK cytotoxicity meta-analysis quantifies a robust innate defect across decades of literature (Hedges’ g 0.96), while multi-omic T-cell work is converging on exhaustion-like programs, especially in relation to symptom provocation (exercise). (baraniuk2024metaanalysisofnatural pages 1-2, iu2024transcriptionalreprogrammingprimes pages 1-2)

### 2.5 Neurological biomarker development: NfL as a candidate (2024)
NfL elevations and correlations with cognition and parasympathetic dysfunction nominate a measurable neurological axis and a potential stratification biomarker for clinical studies. (azcue2024plasmaneurofilamentlight pages 1-2)

---

## 3) Current applications and real-world implementations

### 3.1 Biomarker candidates under active investigation
* **Neuroaxonal injury marker:** plasma **NfL** for neurological dysfunction and cognitive/autonomic correlation. (azcue2024plasmaneurofilamentlight pages 1-2)
* **Endothelial and inflammatory panels:** ET-1, VCAM-1, NOx, cytokines/chemokines (e.g., TNF-α, IL-1β, IL-6) to support subtype differentiation and severity associations. (graves2024chronicfatiguesyndrome pages 5-7)
* **Proteomic biomarker set:** THBS1, PF4, PROS1, C9, FCN3, LTF, S100A9 and others as candidate signatures of coagulation/endothelial/complement dysregulation. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **Functional immune assay:** NK cytotoxicity (and related degranulation pathways) remains a reproducible immune functional abnormality, useful as a mechanistic readout in trials. (baraniuk2024metaanalysisofnatural pages 1-2)

### 3.2 Mechanistically motivated interventions being tested
A randomized, placebo-controlled trial of intranasal mechanical stimulation (targeting a proposed brainstem neuro-immune interface) reported an approximately **30% reduction in overall symptom scores after 8 weeks**, with immunologic correlates suggestive of reduced inflammation and increased disease tolerance programs. (rodriguez2023achievingsymptomrelief pages 1-2)

**Caution:** This intervention represents an experimental approach; the evidence excerpt does not establish long-term efficacy or generalizability. (rodriguez2023achievingsymptomrelief pages 1-2)

---

## 4) Expert synthesis and analysis (authoritative perspectives in the retrieved evidence)

### 4.1 “Multifactorial network” model
A 2024 immunology review argues for moving beyond fragmented single-mechanism explanations toward a cohesive model in which genetic predisposition plus environmental triggers (notably infections) lead to interconnected immune dysregulation, chronic inflammation, gut dysbiosis, and metabolic disturbance. (arron2024myalgicencephalomyelitischronicfatigue pages 1-2)

### 4.2 Disease burden and heterogeneity as a pathophysiology constraint
The same review compiles prevalence and socioeconomic burden estimates (e.g., global prevalence 0.1–0.8%; women affected 2–3×; up to 75% unable to work), reinforcing that heterogeneous phenotypes likely reflect multiple biological subtypes and/or phases—an important premise for interpreting inconsistent biomarker literature and for designing stratified studies. (arron2024myalgicencephalomyelitischronicfatigue pages 1-2)

### 4.3 Autoimmunity and post-transcriptional regulation: plausible but not definitive
Recent syntheses highlight potential roles for autoantibodies and miRNA dysregulation, but the evidence base remains heterogeneous and requires careful replication and phenotype definition; miRNAs repeatedly implicated across studies include miR-29c, miR-99b, miR-128, miR-374b, miR-766, and others linked to immune and mitochondrial/oxidative pathways. (tsamou2024identifyingmicrornaspossibly pages 1-2)

---

## 5) Key statistics and quantitative data points from recent studies

* **Deep phenotyping recruitment yield:** 484 inquiries → 27 in-person evaluation → **17** adjudicated PI-ME/CFS cases. (walitt2024deepphenotypingof pages 1-2)
* **Autonomic physiology:** Valsalva BP recovery **4.1 ± 0.4 s vs 3.0 ± 0.2 s**, **p = 0.014**. (walitt2024deepphenotypingof pages 1-2)
* **Orthostatic cerebral blood flow synthesis:** **90% (384/429)** exceeded a 13% CBF reduction cutoff; mean reduction **26% vs 7%** in controls (as reported in synthesis). (nunes2024assessingthecoagulation pages 33-36)
* **POTS rate under standardized test:** ME/CFS **13% (4/31)**. (graves2024chronicfatiguesyndrome pages 5-7)
* **Proteomics:** **45 proteins** differential (24 up/21 down, p < 0.05); examples include THBS1 ~3.5–3.8× up; PF4 3.11× up; LTF 8.38× up; PROS1 0.48×; C9 0.17×. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **NfL biomarker:** higher in ME/CFS (F = 4.30, p < 0.05); cognitive correlations up to |r| = 0.42; variance explained up to **17.2%**; autonomic parasympathetic association F = 9.48, p ≤ 0.003. (azcue2024plasmaneurofilamentlight pages 1-2)
* **NK cytotoxicity meta-analysis:** Hedges’ g **0.96 (0.75–1.18)**; ~50% of control cytotoxicity level. (baraniuk2024metaanalysisofnatural pages 1-2)
* **INMEST trial:** **~30% symptom reduction after 8 weeks** (N = 31). (rodriguez2023achievingsymptomrelief pages 1-2)

---

## Evidence map (recent, 2023–2024)
The following table provides a compact evidence map of recent mechanistic work and quantitative results.

| Mechanistic domain | Key finding | Study (first author, year, journal) | Cohort/sample size | Quantitative results (stats) | Molecular/cellular entities (genes/proteins/metabolites/cell types) | URL/DOI | PMID |
|---|---|---|---|---|---|---|---|
| Multisystem deep phenotyping: immune, autonomic, central catechol/neurobehavioral | Post-infectious ME/CFS showed chronic antigenic stimulation with increased naïve and decreased switched-memory B cells, autonomic abnormalities, and altered effort preference consistent with dysfunction of integrative brain regions and central catechol pathway dysregulation | Walitt, 2024, *Nature Communications* | 17 adjudicated PI-ME/CFS; 21 healthy volunteers; recruited from 484 inquiries and 27 in-person evaluations | Valsalva blood-pressure recovery time 4.1 ± 0.4 s vs 3.0 ± 0.2 s in controls, *p* = 0.014; altered effort choice OR 1.65 (95% CI 1.03–2.65), *p* = 0.04 | Naïve B cells, switched memory B cells, catechol pathways, PBMC gene-expression/metabolic pathways | https://doi.org/10.1038/s41467-024-45107-3 |  |
| Endothelial dysfunction + inflammatory signaling | ME/CFS showed a biomarker pattern consistent with endothelial dysfunction and systemic inflammation, distinct from long COVID but overlapping in ET-1/VCAM-1 elevation and NO metabolite reduction | Domingo, 2024, *Journal of Translational Medicine* | 31 ME/CFS; 23 long COVID; 31 sedentary healthy controls | POTS on NASA lean test: 4/31 ME/CFS (13%), 1/23 long COVID (4%), 1/31 controls (3%); ME/CFS and long COVID had higher ET-1 (*p* < 0.05) and VCAM-1 (*p* < 0.001), lower NOx (*p* < 0.01); ME/CFS had higher PAI-1 and E-selectin than both comparison groups (*p* < 0.01); PCA PC1 82.7%, PC2 6.1%; combined biomarker classification ME/CFS vs long COVID 59% | ET-1/EDN1, VCAM1, ICAM1, SELE/E-selectin, SERPINE1/PAI-1, TNF, IL1B, IL4, IL6, IL10, CXCL10/IP-10, leptin | https://doi.org/10.1186/s12967-024-05148-0 |  |
| Coagulation/endothelial/complement proteomics | Plasma proteomics implicated dysregulated coagulation, endothelial dysfunction, and complement downregulation in ME/CFS | Nunes, 2024, *Cardiovascular Diabetology* | 15 ME/CFS; 10 controls | 45 proteins significant at *p* < 0.05: 24 up, 21 down; thrombospondin-1 3.48–3.75-fold up (*p* ≤ 0.0002); PF4 3.11-fold up (*p* = 0.00009); lactotransferrin up to 8.38-fold up (*p* = 0.00009); protein S 0.48-fold (*p* = 0.0006); C9 0.17-fold (*p* = 0.0001); ficolin-3 ~0.45–0.65-fold (*p* = 0.0006–0.0348) | THBS1, PF4, PROS1, C9, FCN3, LTF, S100A9, IGHG1; platelet-poor plasma proteins | https://doi.org/10.1186/s12933-024-02315-x |  |
| Neurological dysfunction / neuroaxonal injury biomarker | Elevated plasma neurofilament light chain suggested neuroaxonal injury associated with cognitive impairment and autonomic dysfunction in ME/CFS | Azcue, 2024, *Biomedicines* | 67 ME/CFS; 43 healthy controls | Higher plasma NfL in ME/CFS: F = 4.30, *p* < 0.05; correlations with visuospatial perception *r* = -0.42, *p* ≤ 0.001; verbal memory *r* = -0.35, *p* ≤ 0.005; visual memory *r* = -0.26, *p* < 0.05; parasympathetic dysfunction F = 9.48, *p* ≤ 0.003; NfL explained up to 17.2% of cognitive-test variance | NfL/NEFL, cognitive domains, parasympathetic/autonomic function | https://doi.org/10.3390/biomedicines12071539 |  |
| Innate immune dysfunction | NK-cell cytotoxicity is one of the most reproducible immune abnormalities in ME/CFS | Baraniuk, 2024, *Frontiers in Immunology* | Meta-analysis of 28 papers; 55 effector:target data points | Overall Hedges’ *g* = 0.96 (95% CI 0.75–1.18); NK cytotoxicity reduced to about half of healthy-control levels; literature search yielded 522 records | NK cells, cytotoxicity assays, K562 target cells, lytic granule pathways | https://doi.org/10.3389/fimmu.2024.1440643 |  |
| Neuro-immune interface / disease tolerance | Targeting the neuro-immune interface via intranasal mechanical stimulation was associated with symptom improvement and immunologic changes consistent with reduced inflammation and increased disease tolerance | Rodriguez, 2023, *Oxford Open Immunology* | 31 ME patients (17 enrolled in 2018; 14 in 2019) | ~30% reduction in overall symptom scores after 8 weeks; randomized, placebo-controlled treatment: 20 min twice weekly for 1 month | Brainstem, vagus nerve, trigeminal-related nasal nerve endings, T-cell subsets, gut-homing immune cells, inflammatory programs | https://doi.org/10.1093/oxfimm/iqad003 |  |
| Integrative pathophysiology review | ME/CFS is framed as a multifactorial disease emerging from genetic vulnerabilities plus environmental triggers, especially infections, producing immune dysregulation, chronic inflammation, gut dysbiosis, autonomic abnormalities, and metabolic disturbance | Arron, 2024, *Frontiers in Immunology* | Review; epidemiologic synthesis | Global prevalence estimated 0.1–0.8%; women affected 2–3× more than men; up to 75% unable to work; estimated annual cost US $18–24B and UK £3.3B | Immune dysregulation, gut microbiome, metabolic pathways, autonomic nervous system, inflammatory networks | https://doi.org/10.3389/fimmu.2024.1386607 |  |
| Post-transcriptional regulation / miRNA biology | Dysregulated miRNAs are linked to immune response, mitochondrial dysfunction, oxidative stress, and central sensitization in ME/CFS | Tsamou, 2024, *International Journal of Molecular Sciences* | Review | No pooled effect size reported in excerpt; review highlights repeatedly implicated candidates across studies | miR-29c, miR-99b, miR-128, miR-374b, miR-766, miR-23a, miR-103, miR-152, miR-320 | https://doi.org/10.3390/ijms25179551 |  |


*Table: This table summarizes key 2023-2024 mechanistic studies and reviews on ME/CFS pathophysiology, emphasizing quantitative findings, implicated molecular/cellular entities, and ontology-relevant domains. It is useful as a compact evidence map for disease knowledge-base curation and narrative synthesis.*

---

## Ontology-oriented annotations (knowledge-base ready)
*These mappings reflect the mechanisms supported by the cited evidence above; they are intended as starting points for formal curation.*

### A) Genes/proteins (HGNC symbols; examples with evidence)
* **THBS1** (thrombospondin-1): upregulated in ME/CFS plasma proteomics; implicated in platelet activation/coagulation biology. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **PF4** (platelet factor 4): upregulated in plasma proteomics; platelet/coagulation biology. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **PROS1** (protein S): downregulated; anticoagulant pathway regulation. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **C9** (complement component 9): downregulated; membrane attack complex component. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **FCN3** (ficolin-3): downregulated; lectin pathway innate immunity. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **LTF** (lactotransferrin): strongly upregulated; innate immune signaling/iron-binding protein. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **S100A9**: upregulated; inflammatory/myeloid-associated alarmin. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **NEFL / NfL (protein biomarker):** elevated plasma marker consistent with neuroaxonal injury. (azcue2024plasmaneurofilamentlight pages 1-2)

### B) Biological processes (GO-like terms; not exhaustive)
* Immune effector process / cytotoxicity (e.g., NK cytotoxicity). (baraniuk2024metaanalysisofnatural pages 1-2)
* Regulation of T cell activation / T cell exhaustion-like programs. (iu2024transcriptionalreprogrammingprimes pages 1-2)
* Platelet activation and coagulation-related processes. (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* Complement activation (notably terminal complement complex components altered). (nunes2024dataindependentlcmsmsanalysis pages 5-7)
* Regulation of blood pressure and autonomic reflexes (baroreflex/cardiovagal and Valsalva recovery). (walitt2024deepphenotypingof pages 1-2)
* Response to exertion / post-exertional symptom exacerbation as a systems stress response (conceptual, supported by provocation paradigms and symptom-linked biomarker changes). (iu2024transcriptionalreprogrammingprimes pages 1-2, walitt2024deepphenotypingof pages 1-2)

### C) Cellular components (cellular locations where key processes occur)
* **Blood plasma / extracellular space:** proteomic and endothelial biomarker evidence. (nunes2024dataindependentlcmsmsanalysis pages 5-7, graves2024chronicfatiguesyndrome pages 5-7)
* **Peripheral blood mononuclear cells (PBMCs):** multi-omic immune signatures and metabolic pathway alterations. (walitt2024deepphenotypingof pages 1-2, rodriguez2023achievingsymptomrelief pages 1-2)
* **Axonal cytoskeleton (neurofilament):** implicated by elevated NfL. (azcue2024plasmaneurofilamentlight pages 1-2)

### D) Cell types (Cell Ontology-like)
* **Natural killer cell** (CL:0000623) – reduced cytotoxicity. (baraniuk2024metaanalysisofnatural pages 1-2)
* **CD8-positive, alpha-beta T cell** (CL:0000625) – exhaustion-like reprogramming. (iu2024transcriptionalreprogrammingprimes pages 1-2)
* **Naïve B cell** and **class-switched memory B cell** – altered proportions suggesting chronic antigenic stimulation. (walitt2024deepphenotypingof pages 1-2)
* **Endothelial cell** – implicated by ET-1/VCAM-1/E-selectin/PAI-1 patterns and by proteomic signatures interpreted as endotheliopathy. (graves2024chronicfatiguesyndrome pages 5-7, nunes2024dataindependentlcmsmsanalysis pages 5-7)
* **Platelet** – PF4/THBS1 and platelet dysregulation signaling. (nunes2024dataindependentlcmsmsanalysis pages 5-7)

### E) Anatomical locations (UBERON-like)
* **Peripheral blood** (UBERON:0000178) – dominant source of current biomarker evidence. (azcue2024plasmaneurofilamentlight pages 1-2, nunes2024dataindependentlcmsmsanalysis pages 5-7, graves2024chronicfatiguesyndrome pages 5-7)
* **Brain/central nervous system** (UBERON:0000955) – implicated by central catechol pathway dysregulation hypothesis and neuroaxonal injury markers. (walitt2024deepphenotypingof pages 1-2, azcue2024plasmaneurofilamentlight pages 1-2)
* **Autonomic nervous system** (UBERON:0002410) – physiological abnormalities and orthostatic intolerance. (walitt2024deepphenotypingof pages 1-2, nunes2024assessingthecoagulation pages 33-36)

### F) Chemical entities (CHEBI-like; representative)
* **Nitrite/nitrate (NOx)** as nitric oxide metabolites: reduced in ME/CFS and long COVID vs controls in the prospective cohort. (graves2024chronicfatiguesyndrome pages 5-7)

### G) Phenotypes (Human Phenotype Ontology-like)
* **Post-exertional malaise / post-exertional symptom exacerbation** (concept aligns with HP:0025406 “Post-exertional malaise”). (arron2024myalgicencephalomyelitischronicfatigue pages 1-2, rodriguez2023achievingsymptomrelief pages 1-2)
* **Orthostatic intolerance** (HP:0001278-like) and **postural orthostatic tachycardia** (POTS; HP:0012431). (graves2024chronicfatiguesyndrome pages 5-7, nunes2024assessingthecoagulation pages 33-36)
* **Cognitive impairment** (HP:0100543) with correlations to NfL. (azcue2024plasmaneurofilamentlight pages 1-2)

---

## Disease progression model (mechanistic sequence; integrative)
1. **Triggering event (often infection) in genetically/biologically predisposed host** → initiates immune activation and, in some, incomplete immune resolution. (arron2024myalgicencephalomyelitischronicfatigue pages 1-2, walitt2024deepphenotypingof pages 1-2)
2. **Persistent immune remodeling** (e.g., NK cytotoxic impairment; exhaustion-like T-cell programs; B-cell memory shifts) → chronic antigenic stimulation phenotype and immune–metabolic coupling. (baraniuk2024metaanalysisofnatural pages 1-2, iu2024transcriptionalreprogrammingprimes pages 1-2, walitt2024deepphenotypingof pages 1-2)
3. **Coupled vascular/endothelial and autonomic dysfunction** → impaired perfusion regulation, orthostatic intolerance, and susceptibility to symptom exacerbation with orthostatic or exertional stress. (graves2024chronicfatiguesyndrome pages 5-7, nunes2024dataindependentlcmsmsanalysis pages 5-7, nunes2024assessingthecoagulation pages 33-36)
4. **Metabolic limitation state** (downstream integrator) → reduced tolerance to exertional stress and PEM episodes. (arron2024myalgicencephalomyelitischronicfatigue pages 1-2, walitt2024deepphenotypingof pages 1-2)
5. **Neurological impact** (central catechol pathway dysregulation hypothesis; measurable neuroaxonal injury signals in subsets) → cognitive/autonomic symptom coupling and potentially sustained disability. (walitt2024deepphenotypingof pages 1-2, azcue2024plasmaneurofilamentlight pages 1-2)

---

## Figures supporting the report
* Walitt et al. 2024 *Nature Communications* cohort selection and deep-phenotyping schematic (Figure 1a) provides the recruitment and adjudication counts (17 PI-ME/CFS; 21 controls). (walitt2024deepphenotypingof media 4ea86a03)
* Walitt et al. 2024 summary schematic (Figure 10) integrates infection-triggered mechanisms with immune, autonomic, and central catechol pathways as a proposed explanatory framework. (walitt2024deepphenotypingof media c5d66364)

---

## Notes on evidence completeness and PMIDs
PMIDs were not available in the retrieved text excerpts for the key 2023–2024 papers used here; therefore, this report provides DOIs/URLs and publication month/year from the sources as retrieved. (walitt2024deepphenotypingof pages 1-2, nunes2024dataindependentlcmsmsanalysis pages 5-7, azcue2024plasmaneurofilamentlight pages 1-2, baraniuk2024metaanalysisofnatural pages 1-2, graves2024chronicfatiguesyndrome pages 5-7, arron2024myalgicencephalomyelitischronicfatigue pages 1-2, rodriguez2023achievingsymptomrelief pages 1-2, tsamou2024identifyingmicrornaspossibly pages 1-2)

References

1. (arron2024myalgicencephalomyelitischronicfatigue pages 1-2): H. E. Arron, Benjamin D. Marsh, D. Kell, M. A. Khan, Beate R. Jaeger, and E. Pretorius. Myalgic encephalomyelitis/chronic fatigue syndrome: the biology of a neglected disease. Frontiers in Immunology, Jun 2024. URL: https://doi.org/10.3389/fimmu.2024.1386607, doi:10.3389/fimmu.2024.1386607. This article has 83 citations and is from a peer-reviewed journal.

2. (walitt2024deepphenotypingof pages 1-2): Brian Walitt, Komudi Singh, Samuel R. LaMunion, Mark Hallett, Steve Jacobson, Kong Chen, Yoshimi Enose-Akahata, Richard Apps, Jennifer J. Barb, Patrick Bedard, Robert J. Brychta, Ashura Williams Buckley, Peter D. Burbelo, Brice Calco, Brianna Cathay, Li Chen, Snigdha Chigurupati, Jinguo Chen, Foo Cheung, Lisa M. K. Chin, Benjamin W. Coleman, Amber B. Courville, Madeleine S. Deming, Bart Drinkard, Li Rebekah Feng, Luigi Ferrucci, Scott A. Gabel, Angelique Gavin, David S. Goldstein, Shahin Hassanzadeh, Sean C. Horan, Silvina G. Horovitz, Kory R. Johnson, Anita Jones Govan, Kristine M. Knutson, Joy D. Kreskow, Mark Levin, Jonathan J. Lyons, Nicholas Madian, Nasir Malik, Andrew L. Mammen, John A. McCulloch, Patrick M. McGurrin, Joshua D. Milner, Ruin Moaddel, Geoffrey A. Mueller, Amrita Mukherjee, Sandra Muñoz-Braceras, Gina Norato, Katherine Pak, Iago Pinal-Fernandez, Traian Popa, Lauren B. Reoma, Michael N. Sack, Farinaz Safavi, Leorey N. Saligan, Brian A. Sellers, Stephen Sinclair, Bryan Smith, Joseph Snow, Stacey Solin, Barbara J. Stussman, Giorgio Trinchieri, Sara A. Turner, C. Stephenie Vetter, Felipe Vial, Carlotta Vizioli, Ashley Williams, Shanna B. Yang, and Avindra Nath. Deep phenotyping of post-infectious myalgic encephalomyelitis/chronic fatigue syndrome. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45107-3, doi:10.1038/s41467-024-45107-3. This article has 137 citations and is from a highest quality peer-reviewed journal.

3. (baraniuk2024metaanalysisofnatural pages 1-2): James N. Baraniuk, Natalie Eaton-Fitch, and Sonya Marshall-Gradisnik. Meta-analysis of natural killer cell cytotoxicity in myalgic encephalomyelitis/chronic fatigue syndrome. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1440643, doi:10.3389/fimmu.2024.1440643. This article has 9 citations and is from a peer-reviewed journal.

4. (iu2024transcriptionalreprogrammingprimes pages 1-2): David S. Iu, Jessica Maya, Luyen T. Vu, Elizabeth A. Fogarty, Adrian J. McNairn, Faraz Ahmed, Carl J. Franconi, Paul R. Munn, Jennifer K. Grenier, Maureen R. Hanson, and Andrew Grimson. Transcriptional reprogramming primes cd8+ t cells toward exhaustion in myalgic encephalomyelitis/chronic fatigue syndrome. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415119121, doi:10.1073/pnas.2415119121. This article has 21 citations and is from a highest quality peer-reviewed journal.

5. (nunes2024assessingthecoagulation pages 33-36): JM Nunes. Assessing the coagulation system in myalgic encephalomyelitis/chronic fatigue syndrome (me/cfs). Unknown journal, 2024.

6. (graves2024chronicfatiguesyndrome pages 5-7): B. Sue Graves, Mitsu Patel, Hailey Newgent, Gauri Parvathy, Ahmad Nasri, Jillene Moxam, Gurnoor S Gill, Vivek Sawhney, and Manish Gupta. Chronic fatigue syndrome: diagnosis, treatment, and future direction. Cureus, Oct 2024. URL: https://doi.org/10.7759/cureus.70616, doi:10.7759/cureus.70616. This article has 34 citations.

7. (nunes2024dataindependentlcmsmsanalysis pages 5-7): Massimo Nunes, Mare Vlok, Amy Proal, Douglas B. Kell, and Etheresia Pretorius. Data-independent lc-ms/ms analysis of me/cfs plasma reveals a dysregulated coagulation system, endothelial dysfunction, downregulation of complement machinery. Cardiovascular Diabetology, Jul 2024. URL: https://doi.org/10.1186/s12933-024-02315-x, doi:10.1186/s12933-024-02315-x. This article has 25 citations and is from a peer-reviewed journal.

8. (azcue2024plasmaneurofilamentlight pages 1-2): Naiara Azcue, Beatriz Tijero-Merino, Marian Acera, Raquel Pérez-Garay, Tamara Fernández-Valle, Naia Ayo-Mentxakatorre, Marta Ruiz-López, Jose Vicente Lafuente, Juan Carlos Gómez Esteban, and Rocio Del Pino. Plasma neurofilament light chain: a potential biomarker for neurological dysfunction in myalgic encephalomyelitis/chronic fatigue syndrome. Biomedicines, 12:1539, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071539, doi:10.3390/biomedicines12071539. This article has 9 citations.

9. (graves2024chronicfatiguesyndrome pages 4-5): B. Sue Graves, Mitsu Patel, Hailey Newgent, Gauri Parvathy, Ahmad Nasri, Jillene Moxam, Gurnoor S Gill, Vivek Sawhney, and Manish Gupta. Chronic fatigue syndrome: diagnosis, treatment, and future direction. Cureus, Oct 2024. URL: https://doi.org/10.7759/cureus.70616, doi:10.7759/cureus.70616. This article has 34 citations.

10. (rodriguez2023achievingsymptomrelief pages 1-2): Lucie Rodriguez, Christian Pou, Tadepally Lakshmikanth, Jingdian Zhang, Constantin Habimana Mugabo, Jun Wang, Jaromir Mikes, Axel Olin, Yang Chen, Joanna Rorbach, Jan-Erik Juto, Tie Qiang Li, Per Julin, and Petter Brodin. Achieving symptom relief in patients with myalgic encephalomyelitis by targeting the neuro-immune interface and optimizing disease tolerance. Oxford Open Immunology, Apr 2023. URL: https://doi.org/10.1093/oxfimm/iqad003, doi:10.1093/oxfimm/iqad003. This article has 12 citations.

11. (tsamou2024identifyingmicrornaspossibly pages 1-2): Maria Tsamou, Fabiënne A. C. Kremers, Keano A. Samaritakis, and Erwin L. Roggen. Identifying micrornas possibly implicated in myalgic encephalomyelitis/chronic fatigue syndrome and fibromyalgia: a review. International Journal of Molecular Sciences, 25:9551, Sep 2024. URL: https://doi.org/10.3390/ijms25179551, doi:10.3390/ijms25179551. This article has 11 citations.

12. (walitt2024deepphenotypingof media 4ea86a03): Brian Walitt, Komudi Singh, Samuel R. LaMunion, Mark Hallett, Steve Jacobson, Kong Chen, Yoshimi Enose-Akahata, Richard Apps, Jennifer J. Barb, Patrick Bedard, Robert J. Brychta, Ashura Williams Buckley, Peter D. Burbelo, Brice Calco, Brianna Cathay, Li Chen, Snigdha Chigurupati, Jinguo Chen, Foo Cheung, Lisa M. K. Chin, Benjamin W. Coleman, Amber B. Courville, Madeleine S. Deming, Bart Drinkard, Li Rebekah Feng, Luigi Ferrucci, Scott A. Gabel, Angelique Gavin, David S. Goldstein, Shahin Hassanzadeh, Sean C. Horan, Silvina G. Horovitz, Kory R. Johnson, Anita Jones Govan, Kristine M. Knutson, Joy D. Kreskow, Mark Levin, Jonathan J. Lyons, Nicholas Madian, Nasir Malik, Andrew L. Mammen, John A. McCulloch, Patrick M. McGurrin, Joshua D. Milner, Ruin Moaddel, Geoffrey A. Mueller, Amrita Mukherjee, Sandra Muñoz-Braceras, Gina Norato, Katherine Pak, Iago Pinal-Fernandez, Traian Popa, Lauren B. Reoma, Michael N. Sack, Farinaz Safavi, Leorey N. Saligan, Brian A. Sellers, Stephen Sinclair, Bryan Smith, Joseph Snow, Stacey Solin, Barbara J. Stussman, Giorgio Trinchieri, Sara A. Turner, C. Stephenie Vetter, Felipe Vial, Carlotta Vizioli, Ashley Williams, Shanna B. Yang, and Avindra Nath. Deep phenotyping of post-infectious myalgic encephalomyelitis/chronic fatigue syndrome. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45107-3, doi:10.1038/s41467-024-45107-3. This article has 137 citations and is from a highest quality peer-reviewed journal.

13. (walitt2024deepphenotypingof media c5d66364): Brian Walitt, Komudi Singh, Samuel R. LaMunion, Mark Hallett, Steve Jacobson, Kong Chen, Yoshimi Enose-Akahata, Richard Apps, Jennifer J. Barb, Patrick Bedard, Robert J. Brychta, Ashura Williams Buckley, Peter D. Burbelo, Brice Calco, Brianna Cathay, Li Chen, Snigdha Chigurupati, Jinguo Chen, Foo Cheung, Lisa M. K. Chin, Benjamin W. Coleman, Amber B. Courville, Madeleine S. Deming, Bart Drinkard, Li Rebekah Feng, Luigi Ferrucci, Scott A. Gabel, Angelique Gavin, David S. Goldstein, Shahin Hassanzadeh, Sean C. Horan, Silvina G. Horovitz, Kory R. Johnson, Anita Jones Govan, Kristine M. Knutson, Joy D. Kreskow, Mark Levin, Jonathan J. Lyons, Nicholas Madian, Nasir Malik, Andrew L. Mammen, John A. McCulloch, Patrick M. McGurrin, Joshua D. Milner, Ruin Moaddel, Geoffrey A. Mueller, Amrita Mukherjee, Sandra Muñoz-Braceras, Gina Norato, Katherine Pak, Iago Pinal-Fernandez, Traian Popa, Lauren B. Reoma, Michael N. Sack, Farinaz Safavi, Leorey N. Saligan, Brian A. Sellers, Stephen Sinclair, Bryan Smith, Joseph Snow, Stacey Solin, Barbara J. Stussman, Giorgio Trinchieri, Sara A. Turner, C. Stephenie Vetter, Felipe Vial, Carlotta Vizioli, Ashley Williams, Shanna B. Yang, and Avindra Nath. Deep phenotyping of post-infectious myalgic encephalomyelitis/chronic fatigue syndrome. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45107-3, doi:10.1038/s41467-024-45107-3. This article has 137 citations and is from a highest quality peer-reviewed journal.