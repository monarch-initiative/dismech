---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-04T10:16:19.448966'
end_time: '2026-03-04T10:30:39.854521'
duration_seconds: 860.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cough Variant Asthma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Cough Variant Asthma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cough Variant Asthma**.
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
- **Disease Name:** Cough Variant Asthma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cough Variant Asthma**.
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


## Comprehensive Research Report: Pathophysiology of Cough Variant Asthma (CVA)

### Target disease
- **Disease name:** Cough Variant Asthma (CVA)
- **MONDO ID:** Not identified from the retrieved sources in this run (not available in current context).
- **Category:** Complex (chronic inflammatory airway disease phenotype)

---

## 1) Key concepts and definitions (current understanding)

### Definition / clinical concept
Cough variant asthma is commonly conceptualized as an asthma phenotype in which **chronic cough is the predominant (sometimes sole) symptom**, in contrast to classic asthma where wheeze and dyspnea are typical. In contemporary chronic cough phenotyping work, “asthmatic cough” is often defined to include **CVA and eosinophilic bronchitis**, operationalized with objective evidence of asthma biology/physiology and confirmed treatment response. In a 2024 prospective registry study, asthmatic cough required objective evidence of bronchodilator reversibility, airway hyperresponsiveness, and/or type 2 inflammation, and then **confirmation by response to anti-asthmatic treatment**. (kim2024couldcoughhypersensitivity pages 2-3)

**Operational diagnostic thresholds used (2024 registry):**
- Bronchodilator response (BDR+): ≥12% and ≥200 mL increase in FEV1
- Methacholine AHR: PC20 <16 mg/mL
- Type 2 inflammation: FeNO ≥25 ppb and/or sputum eosinophils ≥3% and/or blood eosinophils ≥300/µL (kim2024couldcoughhypersensitivity pages 2-3)

### CVA as an “atypical asthma” phenotype and potential “pre-asthmatic” state
A 2024 review focused on atypical asthma phenotypes frames CVA as part of “atypical asthma” and notes the hypothesis that **small airway inflammation → small airway dysfunction** may underlie atypical presentations, while also acknowledging that peripheral/small-airway inflammation is **less characterized** in CVA than in classic asthma. (han2024smallairwayinflammation pages 1-2)

---

## 2) Core pathophysiology (molecular and cellular mechanisms)

CVA pathophysiology is best understood as an overlap of (i) asthma biology (airway inflammation and AHR) and (ii) chronic cough biology (cough reflex hypersensitivity), with phenotype-specific differences in the **intensity and distribution** of inflammation and physiologic dysfunction.

### 2.1 Type 2 (T2) airway inflammation: present but often quantitatively lower than classic asthma
A large multicenter cohort comparing newly diagnosed adults with CVA (n=328) versus mild–moderate classic asthma (n=206) found that CVA had **lower canonical T2 biomarkers** despite more severe cough symptoms:
- **FeNO:** 38.5 vs 53 (median; P=0.0019)
- **Blood eosinophils:** 0.2 vs 0.3 (median; P=0.0014)
- **Sputum eosinophils:** 2.3% vs 12.2% (median; P<0.0001)
- **AHR severity:** milder in CVA (higher methacholine PD20-FEV1: 4.2 vs 0.8; P<0.0001) (lai2022clinicalandinflammatory pages 1-2)

A key clinical interpretation from this cohort is mechanistically important: **cough burden did not correlate with eosinophilic markers, spirometry, or PD20** (“No correlation was found…”), suggesting that cough generation in CVA is not a simple linear function of eosinophil load or AHR severity. (lai2022clinicalandinflammatory pages 1-2)

### 2.2 Airway hyperresponsiveness (AHR) as a core physiologic trait
CVA is frequently identified by **positive bronchial provocation**, and AHR is a central concept in contemporary registry phenotyping (PC20 <16 mg/mL). (kim2024couldcoughhypersensitivity pages 2-3)

Bibliometric synthesis of the field (2024) emphasizes airway inflammation and AHR as leading research foci and notes literature linking AHR to later wheeze/classic asthma features. (zhu2024bibliometricanalysisof pages 16-18)

### 2.3 Cough reflex hypersensitivity (CRH): neuronal dysregulation as a “treatable trait”
Modern cough pathophysiology increasingly highlights cough reflex hypersensitivity. A 2023 state-of-the-art review reported that **heightened cough reflex sensitivity** occurs in asthma and can be quantified by capsaicin challenge; one cited comparison showed markedly lower capsaicin C5 thresholds in asthma versus controls (62.5 vs >500 μM; P<0.001). (hirons2023coughinchronic pages 2-4)

A 2024 ERJ Open Research registry analysis found that cough hypersensitivity symptom profiles (triggers and laryngeal sensations) were **similar between asthmatic cough (CVA/EB)** and refractory chronic cough, supporting shared neuronal mechanisms across chronic cough phenotypes even when treatable traits differ. (kim2024couldcoughhypersensitivity pages 2-3)

**Putative molecular sensors:** Although CVA-specific mechanistic human omics were not available in 2023–2024 full text in this run, cough neurobiology commonly implicates **TRP channels** (e.g., TRPV1/TRPA1) as cough sensory transducers; this is consistent with the mechanistic framing of cough reflex hypersensitivity in asthma broadly. (hirons2023coughinchronic pages 2-4)

### 2.4 Small airway dysfunction (SAD): high prevalence and persistence
Small airway involvement is increasingly emphasized in atypical asthma. In a CVA cohort (n=120 corticosteroid-naïve), **SAD was common (60.8%)** and persisted in **54.3%** after 2 months of anti-asthma treatment despite improvement in symptoms and inflammatory measures. (yi2022smallairwaydysfunction pages 1-2)

This supports a model in which CVA symptoms may be driven by a combination of AHR and cough hypersensitivity with **peripheral airway functional impairment** that may be relatively treatment-resistant over short horizons. (han2024smallairwayinflammation pages 1-2, yi2022smallairwaydysfunction pages 1-2)

---

## 3) Key molecular players, cell types, and anatomical locations

### 3.1 Genes/proteins (HGNC)
The most consistently implicated (and clinically actioned) molecular axes in the retrieved evidence include:
- **T2 cytokine axis:** **IL5, IL4, IL13** (as canonical T2 mediators; CVA frequently assessed via eosinophils/FeNO as proxies). (zhu2024bibliometricanalysisof pages 16-18, kim2024couldcoughhypersensitivity pages 2-3)
- **Eosinophilic biomarkers:** eosinophil-related mediators (e.g., ECP as reported in literature summarized by the 2024 bibliometric review). (zhu2024bibliometricanalysisof pages 16-18)
- **Inflammatory/remodeling-associated factors measured clinically:** **IL6, IL8, TNF, TGFB1, IgE**—all decreased during inhaled budesonide therapy in a 2024 retrospective cohort. (niu2024theeffectsof pages 2-4)
- **Sensory transduction channels (cough hypersensitivity concept):** **TRPV1, TRPA1** (implicated in cough reflex sensitivity concepts in asthma/chronic cough literature). (hirons2023coughinchronic pages 2-4)

### 3.2 Cell types (Cell Ontology, CL)
- **Eosinophils (CL:0000542):** elevated in subsets; used for defining T2 inflammation (blood eos ≥300/µL; sputum eos ≥3%). (kim2024couldcoughhypersensitivity pages 2-3)
- **Th2 cells (CL:0000910)** and other type 2 immune networks (inferred through T2 inflammation definitions and Th2 framing). (zhu2024bibliometricanalysisof pages 16-18)
- **Airway epithelial cells (CL:0002328):** central to airway inflammation and to sensory nerve–epithelium crosstalk in cough hypersensitivity paradigms. (hirons2023coughinchronic pages 2-4)
- **Airway smooth muscle cells (CL:0000297):** key effector of AHR.
- **Airway sensory neurons (CL:0000107; vagal afferents/C-fibers conceptually):** drivers of cough reflex hypersensitivity. (hirons2023coughinchronic pages 2-4)

### 3.3 Anatomical locations (UBERON)
- **Lower airway/lung (UBERON:0002048)** and **bronchial tree**: site of AHR and inflammation.
- **Small airways/bronchioles (UBERON:0002186; small airway compartment)**: implicated by SAD prevalence and the “small airway inflammation” framing for atypical asthma. (han2024smallairwayinflammation pages 1-2, yi2022smallairwaydysfunction pages 1-2)
- **Airway epithelium (UBERON:0000065)**: interface for inflammatory signaling and cough sensory activation.

---

## 4) Biological processes disrupted (GO-style mapping)

The evidence supports disruption in the following GO-relevant biological processes (representative terms):
- **Type 2 immune response / eosinophil-mediated inflammation** (proxied by blood/sputum eosinophilia and FeNO; operationalized diagnostically). (kim2024couldcoughhypersensitivity pages 2-3, lai2022clinicalandinflammatory pages 1-2)
- **Inflammatory response / cytokine-mediated signaling** (IL-6, IL-8, TNF, TGF-β1 changes with ICS treatment). (niu2024theeffectsof pages 2-4)
- **Airway smooth muscle contraction / response to bronchoconstrictor stimulus** (AHR defined by methacholine PC20/PD20). (kim2024couldcoughhypersensitivity pages 2-3, lai2022clinicalandinflammatory pages 1-2)
- **Sensory perception of chemical stimulus / cough reflex signaling (neuro-immune interaction)** (cough reflex hypersensitivity; capsaicin sensitivity). (hirons2023coughinchronic pages 2-4)
- **Airway remodeling and small-airway functional impairment** (SAD persistence; atypical asthma small-airway hypothesis). (han2024smallairwayinflammation pages 1-2, yi2022smallairwaydysfunction pages 1-2)

---

## 5) Cellular components (where key processes occur)

Based on the mechanisms above, key cellular compartments include:
- **Extracellular space and airway lumen** (cytokines, eosinophil mediators measured in blood/sputum).
- **Plasma membrane ion channels** on sensory neurons/epithelial cells (TRP channels conceptually implicated in cough reflex sensitivity). (hirons2023coughinchronic pages 2-4)
- **Airway smooth muscle contractile apparatus** (AHR physiology).

---

## 6) Disease progression model (sequence of events)

### Proposed sequence (evidence-supported skeleton)
1. **Triggers/irritants/allergen-associated airway inflammation** occurs with measurable T2 traits in a subset (FeNO/eosinophils), though often lower than classic asthma. (lai2022clinicalandinflammatory pages 1-2, kim2024couldcoughhypersensitivity pages 2-3)
2. **Development of airway hyperresponsiveness** demonstrable via methacholine challenge (PC20/PD20 thresholds). (kim2024couldcoughhypersensitivity pages 2-3, lai2022clinicalandinflammatory pages 1-2)
3. **Cough reflex hypersensitivity** becomes clinically manifest (triggers, laryngeal sensations; capsaicin sensitivity in asthma), contributing to cough disproportionate to measured eosinophilia or AHR severity. (hirons2023coughinchronic pages 2-4, kim2024couldcoughhypersensitivity pages 2-3, lai2022clinicalandinflammatory pages 1-2)
4. **Small airway dysfunction** is common and may persist despite short-term anti-inflammatory therapy, potentially contributing to chronicity and incomplete resolution. (yi2022smallairwaydysfunction pages 1-2, han2024smallairwayinflammation pages 1-2)
5. In a subset, **progression to wheeze/classic asthma** is reported in the broader literature; an older synthesis suggests ~30% may progress without treatment over ~3–5 years, with risk reduction by early ICS. (vujnovic2018coughvariantasthma pages 1-3)

**Note:** High-quality, recent (2023–2024) prospective mechanistic progression estimates were not available in full text within this tool run; the progression statistic above is from older synthesis. (vujnovic2018coughvariantasthma pages 1-3)

---

## 7) Phenotypic manifestations (HP terms) and mechanistic links

### Key clinical phenotypes
- **Chronic cough** (HP:0012735) is the defining manifestation. (kim2024couldcoughhypersensitivity pages 2-3)
- **Airway hyperresponsiveness** (physiologic trait reflected by methacholine PC20/PD20). (kim2024couldcoughhypersensitivity pages 2-3, lai2022clinicalandinflammatory pages 1-2)
- **Abnormal laryngopharyngeal sensations** (cough hypersensitivity-associated phenotype; reported 71% in CVA vs 51% in classic asthma). (lai2022clinicalandinflammatory pages 1-2)

### Mechanistic linkages
- Disproportionate cough severity with lower eosinophilic markers supports a **dual-track model**: treatable T2 inflammation (in some patients) plus **neuronal cough hypersensitivity**. (lai2022clinicalandinflammatory pages 1-2, kim2024couldcoughhypersensitivity pages 2-3, hirons2023coughinchronic pages 2-4)

---

## 8) Recent developments (prioritizing 2023–2024)

### 8.1 Operationalization of “asthmatic cough” with objective treatable traits (2024)
The Korean chronic cough registry work provides an explicit, reproducible framework to classify CVA within chronic cough phenotypes using objective AHR and T2 thresholds plus treatment response confirmation. This supports real-world phenotype stratification and trial enrollment. (kim2024couldcoughhypersensitivity pages 2-3)

### 8.2 Renewed emphasis on small airway inflammation in atypical asthma (2024)
A 2024 review highlights small-airway inflammation as a likely substrate for atypical asthma manifestations (including CVA), encouraging adoption of approaches that partition central vs peripheral airway inflammation and focus on small airway dysfunction. (han2024smallairwayinflammation pages 1-2)

### 8.3 Updated synthesis of cough biology in asthma (2023)
A 2023 state-of-the-art review emphasizes cough reflex hypersensitivity as a cross-cutting mechanism in asthma and other chronic lung diseases, with objective measures (capsaicin cough challenge) and emerging cough-targeted therapeutics (e.g., P2X3 antagonism) discussed as part of the evolving framework for chronic cough management. (hirons2023coughinchronic pages 2-4)

---

## 9) Current applications and real-world implementations

### 9.1 Diagnostics / phenotyping in clinical settings
- **Bronchial provocation testing (methacholine PC20/PD20)** and **FeNO/blood/sputum eosinophils** are actively used as objective criteria for asthmatic cough/CVA phenotyping in contemporary registries, reflecting real-world implementation. (kim2024couldcoughhypersensitivity pages 2-3)
- Comparative biomarker profiling (FeNO, eosinophils, PD20) differentiates CVA from classic asthma in large cohorts and can guide expectations regarding inflammation intensity and AHR. (lai2022clinicalandinflammatory pages 1-2, lai2022clinicalandinflammatory media 8cf72c80)

### 9.2 Therapeutics
- **Inhaled corticosteroids (ICS)** remain foundational anti-inflammatory therapy. A 2024 retrospective study of budesonide reported 56% complete remission and 36% partial remission at 8 weeks, with parallel decreases in systemic inflammatory markers (IL-6, TGF-β1, IgE and others). (niu2024theeffectsof pages 2-4)
- **Treatable traits paradigm**: the convergence of cough hypersensitivity features across asthmatic cough and refractory chronic cough suggests that, beyond ICS and bronchodilators, cough-directed approaches may be relevant for selected patients. (kim2024couldcoughhypersensitivity pages 2-3, hirons2023coughinchronic pages 2-4)

---

## 10) Relevant statistics and data (recent studies)

| Metric | Population/study design | Numeric result | Interpretation | Source (year, DOI/URL) |
|---|---|---|---|---|
| Chronic cough prevalence in asthma | State-of-the-art review across cohorts | 8–58% | Large variability across studies; cough is common in asthma cohorts | 2023, 10.21037/jtd-22-1776 (hirons2023coughinchronic pages 1-2) |
| Small airway dysfunction (SAD) prevalence in CVA | Retrospective CVA cohort (n=120), pre-treatment | 60.8% | SAD is common at baseline in CVA | 2022, 10.3389/fphys.2021.761622 (yi2022smallairwaydysfunction pages 1-2) |
| SAD persistence after 2 months | Same CVA cohort, post-treatment (n=105) | 54.3% | Over half persist with SAD despite clinical improvement | 2022, 10.3389/fphys.2021.761622 (yi2022smallairwaydysfunction pages 1-2) |
| FeNO (ppb), CVA vs classic asthma | APAC multicenter baseline cohort | 38.5 vs 53 (medians) | CVA shows lower T2 inflammation than classic asthma | 2022, 10.3389/fmed.2021.807385 (lai2022clinicalandinflammatory pages 1-2) |
| Blood eosinophils (10^9/L), CVA vs classic asthma | APAC multicenter baseline cohort | 0.2 vs 0.3 (medians) | Lower systemic eosinophilia in CVA | 2022, 10.3389/fmed.2021.807385 (lai2022clinicalandinflammatory pages 1-2) |
| Sputum eosinophils (%), CVA vs classic asthma | APAC multicenter baseline cohort | 2.3% vs 12.2% (medians) | Milder airway eosinophilia in CVA | 2022, 10.3389/fmed.2021.807385 (lai2022clinicalandinflammatory pages 1-2) |
| Methacholine PD20-FEV1 (mg), CVA vs classic asthma | APAC multicenter baseline cohort | 4.2 vs 0.8 (medians) | CVA has milder AHR (higher PD20) | 2022, 10.3389/fmed.2021.807385 (lai2022clinicalandinflammatory pages 1-2) |
| Budesonide response rates in CVA | Retrospective CVA cohort (n=200), 8 weeks | 56% complete, 36% partial, 8% no remission | Majority improve with ICS; early biomarker shifts (IL-6/TGF-β1) track response | 2024, 10.2147/ijgm.s455872 (niu2024theeffectsof pages 2-4) |
| Operational thresholds (2024 registry): FeNO, sputum eos, blood eos, PC20 | Prospective chronic cough registry (asthmatic cough incl. CVA/EB) | FeNO ≥25 ppb; sputum eos ≥3%; blood eos ≥300/μL; PC20 <16 mg/mL | Pragmatic, objective criteria to define asthmatic cough/CVA and verify treatment response | 2024, 10.1183/23120541.00260-2024 (kim2024couldcoughhypersensitivity pages 2-3) |


*Table: Quantitative findings for cough variant asthma (CVA) and asthmatic cough from recent cohorts and reviews, including prevalence, small-airway dysfunction, biomarker differences versus classic asthma, treatment response, and diagnostic thresholds. These data support evidence-based characterization and operationalization of CVA in research and practice.*

Key comparative biomarker table image (CVA vs classic asthma) is also available from the APAC cohort (Table 4). (lai2022clinicalandinflammatory media 8cf72c80)

---

## 11) Mechanism-to-entity mapping for knowledge base (genes, GO, CL, UBERON, CHEBI)

| Mechanistic theme | Key genes/proteins (HGNC) | Key cell types (CL) | Key tissues/anatomy (UBERON) | Biomarkers/assays | Evidence summary with key numeric data | Key source (DOI/URL, year) |
|---|---|---|---|---|---|---|
| Type 2 (T2) eosinophilic inflammation and cytokine milieu | IL5 (HGNC:6025); IL4 (HGNC:6014); IL13 (HGNC:5973); IGHE (HGNC:5463) | Eosinophil (CL:0000542); Th2 cell (CL:0000910); ILC2 (CL:0001065) | Lower airway/lung (UBERON:0002048) | FeNO; blood/sputum eosinophils; total IgE; serum cytokines (ELISA) | Budesonide therapy in CVA reduced serum IL‑6, IL‑8, TNF‑α, TGF‑β1, IL‑5 and IgE across 2–8 weeks (complete/partial responders showed significantly lower IL‑6/TGF‑β1 at early time points, P<0.05). CVA shows T2-linked mechanisms but often with lower eosinophilic indices than classic asthma (median FeNO 38.5 vs 53 ppb; sputum eos 2.3% vs 12.2%) (niu2024theeffectsof pages 2-4, lai2022clinicalandinflammatory pages 1-2, zhu2024bibliometricanalysisof pages 16-18) | 10.2147/ijgm.s455872 (2024); 10.3389/fmed.2021.807385 (2022); 10.2147/jaa.s452097 (2024) |
| Airway hyperresponsiveness (AHR) and bronchial reactivity | — (physiologic trait) | Airway smooth muscle cell (CL:0000297); epithelial cells (CL:0002328) | Bronchus/bronchioles (UBERON:0002185/0002186) | Methacholine PC20/PD20; bronchodilator response | AHR central to CVA; registry criteria used PC20 <16 mg/mL and/or objective response to anti-asthma therapy. CVA cohorts show milder AHR than classic asthma (higher PD20), yet AHR associates with wheeze risk (bibliometric synthesis) (kim2024couldcoughhypersensitivity pages 2-3, zhu2024bibliometricanalysisof pages 16-18) | 10.1183/23120541.00260-2024 (2024); 10.2147/jaa.s452097 (2024) |
| Cough reflex hypersensitivity (neuro‑sensory pathway) | TRPV1 (HGNC:11320); TRPA1 (HGNC:18012) | Sensory neuron (airway/vagal C‑fiber; CL:0000107); airway epithelial cell (CL:0002328) | Airway epithelium (UBERON:0000065); lower respiratory tract (UBERON:0001004) | Capsaicin cough challenge (C2/C5 thresholds); CHQ (symptom triggers) | Asthma/CVA exhibit heightened cough reflex sensitivity: markedly lower capsaicin C5 thresholds vs controls (e.g., ~62.5 vs >500 μM; P<0.001). Symptom profiles of cough hypersensitivity in asthmatic cough (CVA/EB) similar to refractory chronic cough, underscoring shared neuronal treatable trait (hirons2023coughinchronic pages 2-4, hirons2023coughinchronic pages 1-2, kim2024couldcoughhypersensitivity pages 2-3) | 10.21037/jtd-22-1776 (2023); 10.1183/23120541.00260-2024 (2024) |
| Small airway dysfunction (SAD) and peripheral involvement | — (structural/functional) | Airway epithelial cell (CL:0002328); club cell (CL:0000134) | Small airways (UBERON:0005409) | Spirometric small‑airway indices (MMEF%pred; FEF50/75%pred) | SAD present in 60.8% of corticosteroid‑naïve CVA; persisted in 54.3% after 2 months despite symptom/FeNO/sputum eos improvements; baseline SAD linked to older age, female sex; no baseline FeNO or sputum eos differences vs non‑SAD (yi2022smallairwaydysfunction pages 1-2) | 10.3389/fphys.2021.761622 (2022) |
| Biomarker-defined asthmatic cough/CVA criteria in practice | — (panel) | Eosinophil (CL:0000542); airway cells | Lower airway (UBERON:0002048) | FeNO ≥25 ppb; sputum eos ≥3%; blood eos ≥300/μL; PC20 <16 mg/mL | Prospective registry operationalized “asthmatic cough” (CVA/EB) with objective T2/AHR thresholds and validated response to anti-asthma therapy at 6 months; provides pragmatic, quantifiable CVA identification framework (kim2024couldcoughhypersensitivity pages 2-3) | 10.1183/23120541.00260-2024 (2024) |
| CVA vs classic asthma inflammatory intensity | ECP (PRG2; HGNC:9441, proxy), histamine (HDC; HGNC:4861, proxy) | Eosinophil (CL:0000542); mast cell (CL:0000097) | Bronchial mucosa (UBERON:0001600) | Sputum eosinophils/ECP; FeNO | CVA typically shows lower FeNO/blood & sputum eosinophils than classic asthma despite comparable cough burden; APAC cohort: FeNO 38.5 vs 53 ppb; sputum eos 2.3% vs 12.2%; blood eos 0.2 vs 0.3 (10^9/L), all P≤0.002 (lai2022clinicalandinflammatory pages 1-2) | 10.3389/fmed.2021.807385 (2022) |
| Progression risk to classic asthma (wheeze) | — (risk construct) | — | Lower airway (UBERON:0002048) | Longitudinal natural history; treatment effect (ICS) | Historical/clinical synthesis: without treatment, ~30% of CVA patients may progress to classic asthma with wheeze over ~3–5 years; early ICS associated with reduced progression risk (vujnovic2018coughvariantasthma pages 1-3) | 10.5772/intechopen.75152 (2018) |
| Field consensus on core CVA mechanisms | — | — | Airways/lungs | Bibliometric synthesis of focus areas | CVA research emphases: airway inflammation (eosinophils/T2), airway hyperresponsiveness, cough hypersensitivity; diagnostic cutoffs reported: FeNO ~48.5 ppb; small airway FEF25–75 ~74.6% aiding identification (zhu2024bibliometricanalysisof pages 16-18) | 10.2147/jaa.s452097 (2024) |


*Table: Key molecular and cellular mechanisms implicated in cough variant asthma, mapped to genes/proteins, cell types, and anatomical sites, with representative biomarkers and quantitative evidence from recent cohorts/reviews. Citations indicate sources for each row and include URLs/DOIs with publication years.*

**Chemical entities (CHEBI; examples relevant to assays/biology in this evidence set):**
- **Methacholine** (CHEBI:???; used in bronchial provocation testing; CHEBI ID not available in current context) (kim2024couldcoughhypersensitivity pages 2-3, lai2022clinicalandinflammatory pages 1-2)
- **Nitric oxide (NO)** (CHEBI:16480; inferred from FeNO measurement context) (kim2024couldcoughhypersensitivity pages 2-3, lai2022clinicalandinflammatory pages 1-2)
- **Budesonide** (CHEBI:??; ICS used in 2024 cohort; CHEBI ID not available in current context) (niu2024theeffectsof pages 2-4)

---

## 12) Expert opinion / analysis (authoritative synthesis)

The aggregate evidence supports an expert-level interpretation that CVA is not merely “mild asthma with cough,” but rather a phenotype characterized by:
1. **Milder average T2 biomarker elevation and AHR severity** than classic asthma, yet severe cough burden and frequent laryngopharyngeal sensations (suggesting additional mechanisms beyond eosinophilia/AHR magnitude). (lai2022clinicalandinflammatory pages 1-2)
2. **Cough reflex hypersensitivity** as a shared mechanistic substrate across chronic cough phenotypes, including asthmatic cough, motivating treatable-traits frameworks. (kim2024couldcoughhypersensitivity pages 2-3, hirons2023coughinchronic pages 2-4)
3. **High prevalence of small airway dysfunction**, which can persist despite short-term anti-asthma therapy and may represent an under-addressed contributor to persistent symptoms and relapse risk. (yi2022smallairwaydysfunction pages 1-2, han2024smallairwayinflammation pages 1-2)

---

## 13) Evidence items (PMIDs)

**Limitation:** The retrieved tool evidence in this run provided DOIs/URLs and detailed numeric results, but **PMIDs were not present in the extracted snippets** for most items. Therefore, I cannot reliably attach PMID identifiers without risking citation error. Key evidence items are therefore listed with DOI/URL and publication date:
- Kim et al., ERJ Open Research, Jun 2024. https://doi.org/10.1183/23120541.00260-2024 (kim2024couldcoughhypersensitivity pages 2-3)
- Han et al., Heliyon, Sep 2024. https://doi.org/10.1016/j.heliyon.2024.e36124 (han2024smallairwayinflammation pages 1-2)
- Hirons et al., Journal of Thoracic Disease, Oct 2023. https://doi.org/10.21037/jtd-22-1776 (hirons2023coughinchronic pages 1-2, hirons2023coughinchronic pages 2-4)
- Zhu et al., Journal of Asthma and Allergy, Jun 2024. https://doi.org/10.2147/JAA.S452097 (zhu2024bibliometricanalysisof pages 16-18)
- Niu et al., International Journal of General Medicine, Mar 2024. https://doi.org/10.2147/IJGM.S455872 (niu2024theeffectsof pages 2-4)
- Lai et al., Frontiers in Medicine, Jan 2022. https://doi.org/10.3389/fmed.2021.807385 (lai2022clinicalandinflammatory pages 1-2, lai2022clinicalandinflammatory media 8cf72c80)
- Yi et al., Frontiers in Physiology, Jan 2022. https://doi.org/10.3389/fphys.2021.761622 (yi2022smallairwaydysfunction pages 1-2)

---

## Appendix: Visual evidence
- Comparative CVA vs classic asthma biomarker and lung function table (FeNO, blood/sputum eosinophils, PD20-FEV1): (lai2022clinicalandinflammatory media 8cf72c80)


References

1. (kim2024couldcoughhypersensitivity pages 2-3): Mi-Yeong Kim, Ha-Kyeong Won, Ji-Yoon Oh, Ji-Hyang Lee, Eun-Jung Jo, Sung-Yoon Kang, Ji-Ho Lee, Seung-Eun Lee, Noeul Kang, Young-Chan Kim, Hwa Young Lee, Jin An, Youngsang Yoo, Ji-Su Shim, So-Young Park, Han-Ki Park, Min-Hye Kim, Sae-Hoon Kim, Sang-Heon Kim, Yoon-Seok Chang, Sang-Hoon Kim, Byung-Jae Lee, Surinder S. Birring, and Woo-Jung Song. Could cough hypersensitivity symptom profile differentiate phenotypes of chronic cough? ERJ Open Research, 10:00260-2024, Jun 2024. URL: https://doi.org/10.1183/23120541.00260-2024, doi:10.1183/23120541.00260-2024. This article has 14 citations and is from a peer-reviewed journal.

2. (han2024smallairwayinflammation pages 1-2): Junjie Han, Li Li, Ying Gong, Juan Song, Yichun Zhu, Cuicui Chen, Lin Shi, Jian Wang, Yuanlin Song, and Jun She. Small airway inflammation in atypical asthma. Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e36124, doi:10.1016/j.heliyon.2024.e36124. This article has 3 citations.

3. (lai2022clinicalandinflammatory pages 1-2): Kefang Lai, Wenzhi Zhan, Feng Wu, Yunhui Zhang, Lin Lin, Wen Li, Fang Yi, Ziyu Jiang, Yuanrong Dai, Suyun Li, Jiangtao Lin, Yadong Yuan, Yong Jiang, Chen Qiu, Limin Zhao, Meihua Chen, Zhongmin Qiu, Hu Li, Ruchong Chen, Wei Luo, Jiaxing Xie, Chunxing Guo, Mei Jiang, Xiaohong Yang, Guochao Shi, Dejun Sun, Rongchang Chen, Kian Fan Chung, Huahao Shen, and Nanshan Zhong. Clinical and inflammatory characteristics of the chinese apac cough variant asthma cohort. Frontiers in Medicine, Jan 2022. URL: https://doi.org/10.3389/fmed.2021.807385, doi:10.3389/fmed.2021.807385. This article has 28 citations.

4. (zhu2024bibliometricanalysisof pages 16-18): Ziyu Zhu, Jiabao Wu, Wenjun Chen, Fei Luo, and Xia Zhao. Bibliometric analysis of cough variant asthma from 1993 to 2022. Journal of Asthma and Allergy, 17:517-537, Jun 2024. URL: https://doi.org/10.2147/jaa.s452097, doi:10.2147/jaa.s452097. This article has 6 citations and is from a peer-reviewed journal.

5. (hirons2023coughinchronic pages 2-4): Barnaby Hirons, Katherine Rhatigan, Harini Kesavan, Richard D. Turner, Surinder S. Birring, and Peter S. P. Cho. Cough in chronic lung disease: a state of the art review. Journal of Thoracic Disease, 15:5823-5843, Oct 2023. URL: https://doi.org/10.21037/jtd-22-1776, doi:10.21037/jtd-22-1776. This article has 34 citations and is from a peer-reviewed journal.

6. (yi2022smallairwaydysfunction pages 1-2): Fang Yi, Ziyu Jiang, Hu Li, Chunxing Guo, Hankun Lu, Wei Luo, Qiaoli Chen, and Kefang Lai. Small airway dysfunction in cough variant asthma: prevalence, clinical, and pathophysiological features. Frontiers in Physiology, Jan 2022. URL: https://doi.org/10.3389/fphys.2021.761622, doi:10.3389/fphys.2021.761622. This article has 30 citations.

7. (niu2024theeffectsof pages 2-4): Yueying Niu, Mengqing Cao, Shumin Li, Juanfen Mo, Ziyi Zhu, and Haiqin Wang. The effects of budesonide inhalation treatment on the expression levels of serum il-6, tgf-β1, and ige and pulmonary function in patients with cough variant asthma and an evaluation of treatment efficacy. International Journal of General Medicine, 17:1253-1261, Mar 2024. URL: https://doi.org/10.2147/ijgm.s455872, doi:10.2147/ijgm.s455872. This article has 6 citations.

8. (vujnovic2018coughvariantasthma pages 1-3): Sanela Domuz Vujnović, Adrijana Domuz, and Slobodanka Petrović. Cough variant asthma as a phenotype of classic asthma. Asthma Diagnosis and Management - Approach Based on Phenotype and Endotype, Jul 2018. URL: https://doi.org/10.5772/intechopen.75152, doi:10.5772/intechopen.75152. This article has 3 citations.

9. (lai2022clinicalandinflammatory media 8cf72c80): Kefang Lai, Wenzhi Zhan, Feng Wu, Yunhui Zhang, Lin Lin, Wen Li, Fang Yi, Ziyu Jiang, Yuanrong Dai, Suyun Li, Jiangtao Lin, Yadong Yuan, Yong Jiang, Chen Qiu, Limin Zhao, Meihua Chen, Zhongmin Qiu, Hu Li, Ruchong Chen, Wei Luo, Jiaxing Xie, Chunxing Guo, Mei Jiang, Xiaohong Yang, Guochao Shi, Dejun Sun, Rongchang Chen, Kian Fan Chung, Huahao Shen, and Nanshan Zhong. Clinical and inflammatory characteristics of the chinese apac cough variant asthma cohort. Frontiers in Medicine, Jan 2022. URL: https://doi.org/10.3389/fmed.2021.807385, doi:10.3389/fmed.2021.807385. This article has 28 citations.

10. (hirons2023coughinchronic pages 1-2): Barnaby Hirons, Katherine Rhatigan, Harini Kesavan, Richard D. Turner, Surinder S. Birring, and Peter S. P. Cho. Cough in chronic lung disease: a state of the art review. Journal of Thoracic Disease, 15:5823-5843, Oct 2023. URL: https://doi.org/10.21037/jtd-22-1776, doi:10.21037/jtd-22-1776. This article has 34 citations and is from a peer-reviewed journal.