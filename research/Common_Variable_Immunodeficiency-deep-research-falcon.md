---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T03:50:16.780532'
end_time: '2026-03-06T04:06:20.239384'
duration_seconds: 963.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Common Variable Immunodeficiency
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Common Variable Immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Common Variable Immunodeficiency**.
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
- **Disease Name:** Common Variable Immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Common Variable Immunodeficiency**.
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


# Comprehensive Research Report: Common Variable Immunodeficiency (CVID) Pathophysiology (Molecular/Cellular)

## Disease identifiers and classification
- **Disease name:** Common variable immunodeficiency (CVID)
- **MONDO ID:** **MONDO:0015517** (“common variable immunodeficiency”) as represented in Open Targets disease mapping.
- **Category:** Complex/heterogeneous inborn error of immunity (IEI) syndrome; increasingly partitioned into (i) polygenic/multifactorial “CVID” and (ii) monogenic “CVID-like” disorders (alhakim2024thescopeand pages 2-4).

## 1. Key concepts and definitions (current understanding)

### Definition (clinical-immunologic)
CVID is defined by **hypogammaglobulinemia** (IgG ≥2 SD below age-adjusted mean, with low IgA and/or IgM), **poor vaccine responses**, and exclusion of secondary causes, reflecting failure to generate effective humoral immunity (sircana2023commonvariableimmunodeficiency pages 3-4). Mechanistically, it is centered on **failure of B-cell terminal differentiation in germinal centers**, leading to reduced plasma cells and memory B cells and inadequate antibody production (sircana2023commonvariableimmunodeficiency pages 3-4).

### Epidemiology and baseline quantitative features
- **Estimated prevalence/incidence:** commonly reported as ~**1:25,000–1:50,000** (sircana2023commonvariableimmunodeficiency pages 3-4, barbati2024monogeniccommonvariable pages 1-5) and also described as **~1 in 20,000–50,000** (cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).
- **Hypogammaglobulinemia depth:** in two large cohorts, **85–94%** of cases had **IgG <4.5 g/L** (alhakim2024thescopeand pages 2-4).
- **Familial aggregation:** familial inheritance of CVID/IgA deficiency is reported at **~20%** (alhakim2024thescopeand pages 2-4), with familial clustering estimates **~5–25%** in other summaries (sircana2023commonvariableimmunodeficiency pages 3-4).

### “CVID+” immune dysregulation endotype
Beyond infection susceptibility, a major conceptual advance is routine recognition of an “immune dysregulation” phenotype (often termed **CVID+**) with inflammatory/autoimmune complications:
- **>50%** of patients have inflammatory and/or autoimmune complications (“CVID+”) and **~25%** have autoimmunity (alhakim2024thescopeand pages 2-4).
- In a cohort of **408** CVID patients, **122 (30%)** had **hematologic autoimmune manifestations** (ITP, AIHA, Evans syndrome, neutropenia) (cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).

## 2. Core pathophysiology (molecular and cellular mechanisms)

CVID is best understood as a **syndrome of convergent failures in germinal-center (GC)–dependent humoral immunity** and peripheral tolerance, arising from diverse genetic and non-genetic perturbations.

### 2.1 B-cell developmental/GC output failure (central axis)
A core feature is defective generation of **class-switched memory B cells and plasma cells**, reflecting impaired GC maturation and/or post-GC survival.
- Reviews emphasize **impaired differentiation into class-switched memory B cells and plasma cells**, with reductions in mucosal sites and bone marrow noted in CVID cohorts (alhakim2024thescopeand pages 2-4).
- A foundational mechanistic framing is “**failure of B-cell terminal differentiation in germinal centers**” with reduced plasma cells/memory B cells (sircana2023commonvariableimmunodeficiency pages 3-4).

### 2.2 BAFF/APRIL–TACI axis and NF-κB signaling (B-cell survival and plasma cell differentiation)
The BAFF/APRIL system is repeatedly implicated in CVID pathophysiology, connecting survival signaling with plasma cell generation and tolerance.
- BAFF/APRIL bind overlapping receptors, and **TACI activation triggers NFAT, NF-κB, and AP‑1** to promote antibody production and plasma cell differentiation (peng2023commonvariableimmunodeficiency pages 7-9).
- **TNFRSF13B (TACI) variants** are associated with CVID/sIgAD; heterozygous variants can promote **autoimmunity** by preserving autoreactive B cells responsive to Tfh stimulation (peng2023commonvariableimmunodeficiency pages 7-9).
- Population genetics highlight incomplete penetrance: common TNFRSF13B alleles (e.g., C104R, A181E) can abrogate signaling yet have substantial asymptomatic carriage (∼**25% asymptomatic carriers** in some family-based observations; allele frequency **~0.5–0.7%** in Europeans) (peng2023commonvariableimmunodeficiency pages 7-9).
- NF-κB pathway lesions are central; both canonical and non-canonical NF-κB pathways are key to B-cell development/function (peng2023commonvariableimmunodeficiency pages 9-10). **NFKB1** loss-of-function/haploinsufficiency is linked to CVID and described as “**the most common monogenic cause**” in Europeans (peng2023commonvariableimmunodeficiency pages 22-23).

### 2.3 PI3Kδ–AKT–mTOR pathway dysregulation (APDS and GC disruption)
Hyperactive PI3K signaling provides a clear mechanistic bridge between signaling gain-of-function, GC collapse, and CVID-like antibody deficiency.
- In APDS1 (PIK3CD GOF), disease includes “**uncontrolled lymphocyte proliferation, accelerated T cell maturation and senescence, and impaired B cell maturation**” (direct quote) (peng2023commonvariableimmunodeficiency pages 9-10).
- Hyperactive PI3K signaling can disrupt GC structure and interfere with CSR (class-switch recombination), yielding a hyper-IgM–like phenotype (peng2023commonvariableimmunodeficiency pages 9-10).

### 2.4 T-cell help and tolerance checkpoints (Tfh/Treg/CTLA-4–LRBA)
Although classified as an antibody deficiency, a substantial subset involves impaired or dysregulated T-cell help and tolerance.
- T-cell defects are reported in **~one-third** of CVID cases (alhakim2024thescopeand pages 2-4).
- Defects in central and peripheral tolerance pathways and dysregulated Tfh responses can impair CSR/memory B-cell generation (peng2023commonvariableimmunodeficiency pages 12-13).
- **CTLA4 haploinsufficiency** and **LRBA deficiency** exemplify a mechanism where defective inhibitory costimulation and altered CTLA-4 trafficking produce hypogammaglobulinemia with autoimmunity/organ infiltration (enteropathy, interstitial lung disease) (peng2023commonvariableimmunodeficiency pages 13-15, tessarin2023monogenicformsof pages 4-5). LRBA mutations (identified in ~140 patients) can cause functional CTLA-4 loss, autophagy-related abnormalities (reduced LC3 localization), and failure of B cells to form plasmablasts; marked clinical responses to CTLA-4–Ig (abatacept) are reported (peng2023commonvariableimmunodeficiency pages 13-15).

### 2.5 Additional mechanistic routes (DNA repair, transcriptional regulation, organelle/trafficking)
CVID encompasses many routes beyond classical BCR signaling.
- CSR/SHM defects can occur via AID trafficking perturbations (e.g., CTNNBL1 effect on AID nuclear translocation) leading to impaired SHM and inefficient GC reactions, with risk of autoreactive clones and autoimmunity (peng2023commonvariableimmunodeficiency pages 12-13).
- Transcriptional regulators (e.g., BACH2 haploinsufficiency) disrupt T/B specification and CSR/plasmablast differentiation (peng2023commonvariableimmunodeficiency pages 13-15).
- Broader “organelle/trafficking” mechanisms (e.g., SEC61A1, SH3KBP1, DEF6, SAMD9) affect ER homeostasis, calcium flux, mitochondrial health and receptor signaling and can produce CVID-like phenotypes with autoimmunity/autoinflammation (peng2023commonvariableimmunodeficiency pages 13-15).

## 3. Key molecular players (genes/proteins, cells, tissues, chemicals)

### 3.1 Genes/Proteins (HGNC symbols)
CVID and CVID-like disorders have substantial genetic heterogeneity spanning B-cell intrinsic and immune regulatory genes.

**High-confidence/commonly implicated (examples):**
- **NF-κB signaling:** *NFKB1*, *NFKB2* (peng2023commonvariableimmunodeficiency pages 22-23, peng2023commonvariableimmunodeficiency pages 9-10).
- **BAFF/APRIL/TACI axis:** *TNFRSF13B* (TACI), *TNFRSF13C* (BAFF-R) (peng2023commonvariableimmunodeficiency pages 7-9, sircana2023commonvariableimmunodeficiency pages 3-4, sircana2023commonvariableimmunodeficiency pages 4-6).
- **BCR co-receptors:** *CD19*, *CD81*, *MS4A1* (CD20), *CR2* (CD21) (alhakim2024thescopeand pages 2-4, sircana2023commonvariableimmunodeficiency pages 3-4).
- **PI3K pathway:** *PIK3CD*, *PIK3R1*, *PTEN* (peng2023commonvariableimmunodeficiency pages 9-10, tessarin2023monogenicformsof pages 1-2).
- **Immune regulation:** *CTLA4*, *LRBA* (peng2023commonvariableimmunodeficiency pages 13-15, tessarin2023monogenicformsof pages 4-5).
- **Transcription/regulatory:** *IKZF1*, *BACH2*, *STAT3*, *STAT1*, *SOCS1* (peng2023commonvariableimmunodeficiency pages 12-13, peng2023commonvariableimmunodeficiency pages 9-10).

**Recent (2024) pediatric cohort genetic yield and gene list:** In a pediatric CVID cohort (n=32), variants were identified in **17 (53%)**, including *SLC39A7, PRKCD, STAT3, NFKB1, PIK3R1, PLCG2, RFXANK, PRKDC, TNFRSF13B*, and novel *SPI1* and *NFKB1* variants (barbati2024monogeniccommonvariable pages 1-5).

**Open Targets disease–gene associations:** Open Targets lists top CVID-associated targets including *TNFRSF13B, LRBA, IKZF1, NFKB2, ICOS,* and *CD19*. (Note: Open Targets is an evidence integration resource; mechanistic interpretation still relies on primary/review literature.)

### 3.2 Chemical entities / therapeutics (CHEBI-relevant entities)
While CVID is not typically “metabolic,” small molecules and biologics are directly relevant via pathway-targeted therapy:
- **Abatacept (CTLA-4–Ig fusion protein):** used as targeted immunomodulation in CTLA-4 haploinsufficiency / LRBA deficiency, with reported high efficacy for chronic enteropathy and lymphoproliferation and variable results for cytopenias/neurologic features; for GLILD, full/partial resolution reported in up to ~70% (tessarin2023monogenicformsof pages 4-5). A case report in a CVID patient with CTLA4/LRBA variants described rapid regression of clinical/lab findings and weight gain after abatacept initiation.
- **PI3K inhibitors (APDS):** direct PI3K inhibitor approval and clinical improvement in APDS is highlighted in recent reviews (tessarin2023monogenicformsof pages 1-2, tessarin2023monogenicformsof pages 4-5).
- **Sirolimus (mTOR inhibitor):** reported benefit in some immune dysregulation settings to enhance Treg responses (tessarin2023monogenicformsof pages 4-5).
- **Immunoglobulin replacement therapy (IgRT; IVIG/SCIG):** mainstay therapy that reduces infectious episode rate/severity (tessarin2023monogenicformsof pages 1-2, cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).

### 3.3 Cell types (Cell Ontology; CL terms suggested)
Key affected or mechanistically implicated immune cell types include:
- **B cell** (CL:0000236) and differentiation states: naïve B cell, memory B cell, class-switched memory B cell, plasmablast, plasma cell (central in terminal differentiation failure) (sircana2023commonvariableimmunodeficiency pages 3-4, alhakim2024thescopeand pages 2-4).
- **T follicular helper (Tfh) cell** (CL:0002057) and **regulatory T cell** (Treg; CL:0000815): dysregulated help/tolerance links to failed CSR and autoimmunity (peng2023commonvariableimmunodeficiency pages 12-13, peng2023commonvariableimmunodeficiency pages 13-15, alhakim2024thescopeand pages 2-4).
- **Natural killer cell** (CL:0000623): NK defects are discussed in CVID-like phenotypes such as NFKB2-mutated disease (peng2023commonvariableimmunodeficiency pages 22-23) and broader CVID heterogeneity includes NK involvement (alhakim2024thescopeand pages 2-4).

### 3.4 Anatomical locations (UBERON suggested)
Key sites where the pathophysiology manifests:
- **Secondary lymphoid organs** (UBERON:0002106): lymph nodes (UBERON:0000029), spleen (UBERON:0002106) as germinal center sites supporting CSR and GC output (sircana2023commonvariableimmunodeficiency pages 3-4).
- **Bone marrow** (UBERON:0002371): plasma cell survival/maintenance; reductions in plasma cells noted (alhakim2024thescopeand pages 2-4).
- **Gastrointestinal tract** (e.g., small intestine UBERON:0002108; colon UBERON:0001155; stomach UBERON:0000945): CVID enteropathy is associated with plasma-cell paucity across much of the GI tract (except esophagus) (marsden2024paucityofgastrointestinal pages 1-2).
- **Lung** (UBERON:0002048): granulomatous-lymphocytic interstitial lung disease (GLILD) is part of immune dysregulation phenotypes responsive in some cases to abatacept (tessarin2023monogenicformsof pages 4-5).

## 4. Biological processes and pathways (GO-oriented annotation candidates)
Below are GO-aligned biological processes strongly supported by the cited literature as disrupted in CVID/CVID-like disease:
- **B cell differentiation / plasma cell differentiation** (GO:0030183; GO:0002314) (sircana2023commonvariableimmunodeficiency pages 3-4, alhakim2024thescopeand pages 2-4).
- **Immunoglobulin production** (GO:0002377) and **humoral immune response** (GO:0006959) (sircana2023commonvariableimmunodeficiency pages 3-4, alhakim2024thescopeand pages 2-4).
- **Immunoglobulin class switch recombination** (GO:0042167) and **somatic hypermutation of immunoglobulin genes** (GO:0016446) (peng2023commonvariableimmunodeficiency pages 12-13, peng2023commonvariableimmunodeficiency pages 9-10).
- **NF-κB signaling** (GO:0043122) (peng2023commonvariableimmunodeficiency pages 22-23, peng2023commonvariableimmunodeficiency pages 9-10).
- **Phosphatidylinositol 3-kinase signaling / AKT-mTOR signaling** (GO:0014065; GO:0032008) (peng2023commonvariableimmunodeficiency pages 9-10, tessarin2023monogenicformsof pages 1-2).
- **T cell co-stimulation / negative regulation of T cell activation** (GO:0050863; GO:0050868) (CTLA-4/LRBA axis) (peng2023commonvariableimmunodeficiency pages 13-15, tessarin2023monogenicformsof pages 4-5).
- **Immune tolerance / regulation of autoimmunity** (broadly supported conceptually by tolerance gene involvement and autoimmune enrichment) (peng2023commonvariableimmunodeficiency pages 12-13, alhakim2024thescopeand pages 2-4, cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).

## 5. Cellular components (GO-CC candidates)
Literature-supported cellular compartments where key pathogenic processes occur include:
- **Germinal center microenvironment** (anatomical/functional compartment; mechanistically central to CSR/SHM and selection) (sircana2023commonvariableimmunodeficiency pages 3-4, peng2023commonvariableimmunodeficiency pages 12-13).
- **Plasma cell niches** in bone marrow and mucosa (alhakim2024thescopeand pages 2-4).
- **Cell surface receptor complexes** (BCR co-receptors CD19/CD81; costimulatory CTLA-4) (alhakim2024thescopeand pages 2-4, peng2023commonvariableimmunodeficiency pages 13-15).
- **Endomembrane trafficking compartments** relevant to CTLA-4/LRBA trafficking and organelle/ER homeostasis in some monogenic forms (peng2023commonvariableimmunodeficiency pages 13-15).

## 6. Disease progression: mechanistic sequence (model)
A practical progression model consistent with current reviews is:
1. **Predisposition/initiating defects**: inherited or de novo variants affecting B-cell activation/survival (NF-κB; BAFF/APRIL/TACI), GC help and regulation (ICOS, Tfh/Treg axis; CTLA4/LRBA), or signaling/metabolic checkpoints (PI3Kδ/AKT/mTOR) (peng2023commonvariableimmunodeficiency pages 7-9, peng2023commonvariableimmunodeficiency pages 9-10, peng2023commonvariableimmunodeficiency pages 13-15).
2. **Germinal center failure or mis-selection**: impaired CSR/SHM, altered selection thresholds, and reduced generation of long-lived plasma cells/switched memory B cells (peng2023commonvariableimmunodeficiency pages 12-13, sircana2023commonvariableimmunodeficiency pages 3-4, peng2023commonvariableimmunodeficiency pages 9-10).
3. **Hypogammaglobulinemia and impaired vaccine responses**: reduced effective antibody titers, recurrent infections, and persistent antigenic stimulation (alhakim2024thescopeand pages 2-4, sircana2023commonvariableimmunodeficiency pages 3-4).
4. **Immune dysregulation amplification (“CVID+”)**: chronic inflammation, breakdown of tolerance, autoimmunity, lymphoproliferation, organ infiltration (enteropathy, lung disease), and increased morbidity/mortality in severe subsets (alhakim2024thescopeand pages 2-4, cunninghamrundles2024commonvariableimmunodeficiency pages 1-2, tessarin2023monogenicformsof pages 4-5).

## 7. Phenotypic manifestations and mechanism links (HP-oriented)
Selected phenotype associations (HP terms suggested) grounded in the evidence:
- **Hypogammaglobulinemia** (HP:0004313) and **recurrent infections** (HP:0002719) arise from impaired plasma cell/memory B-cell output and reduced Ig levels (alhakim2024thescopeand pages 2-4, sircana2023commonvariableimmunodeficiency pages 3-4).
- **Autoimmune cytopenias** (e.g., immune thrombocytopenia HP:0001891; autoimmune hemolytic anemia HP:0001890): observed in **30%** (122/408) in one cohort, reflecting immune dysregulation/tolerance loss (cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).
- **Enteropathy / chronic diarrhea** (HP:0002028): immune-mediated enteropathy is a hallmark of CTLA4/LRBA dysregulation subsets and broader CVID-E; GI biopsies frequently show plasma-cell paucity (tessarin2023monogenicformsof pages 4-5, marsden2024paucityofgastrointestinal pages 1-2).
- **Interstitial lung disease / GLILD** (HP:0006530): part of immune dysregulation; abatacept responses reported in some cohorts (tessarin2023monogenicformsof pages 4-5).

## 8. Recent developments (prioritizing 2023–2024)

### 8.1 Genetics: increasing recognition of monogenic drivers and stratification tools
- Recent summaries emphasize that while earlier estimates suggested **2–10%** monogenic causes, newer genomic analyses identify monogenic causes in **~20–50%** of CVID/CVID-like cases, and monogenic CVID-like entities are increasingly separated from “true CVID” (alhakim2024thescopeand pages 2-4).
- In hematology-focused CVID cohorts, monogenic etiologies are now estimated at **~25–30%**, with **43%** of patients with hematologic autoimmunity (53/122) having one or more genetic mutations considered related to the immune defect (cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).
- A 2024 pediatric cohort (n=32) achieved **53%** gene-variant identification and proposed a clinical/immunologic scoring system (Mo-CVID score) to prioritize genetic work-up, highlighting higher yield in early onset, positive family history, autoimmunity, lymphoproliferation, and specific immunologic alterations (barbati2024monogeniccommonvariable pages 1-5).

### 8.2 Diagnostic yield of sequencing in PID (generalizable implementation evidence)
A 2024 meta-analysis in suspected PIDs (not CVID-specific) provides implementable expectations for NGS:
- Across 29 studies and 5,847 patients, pooled NGS diagnostic detection rate was **42%** (95% CI 0.29–0.54) (chen2024diagnosticyieldof pages 1-3).
- Yield was higher with a family history (**58%**) vs none (**33%**) (chen2024diagnosticyieldof pages 1-3).
This supports real-world adoption of NGS/WES/WGS in antibody deficiency evaluation pathways, especially in familial/early-onset/complex phenotypes (chen2024diagnosticyieldof pages 1-3, barbati2024monogeniccommonvariable pages 1-5).

### 8.3 Targeted therapies: pathway-directed treatment for CVID-like immune dysregulation
- 2023–2024 reviews highlight increasing implementation of **abatacept** for CTLA4/LRBA-associated immune dysregulation and **PI3K inhibitors** for APDS (tessarin2023monogenicformsof pages 1-2, tessarin2023monogenicformsof pages 4-5).
- A 2023 case report describes abatacept benefit in a patient with severe immune-mediated enteropathy and CTLA4/LRBA variants after a prior CVID diagnosis.

### 8.4 GI pathophysiology: standardizing plasma-cell paucity metrics in CVID enteropathy
A 2024 systematic review of GI plasma cells proposes standardized quantification:
- Plasma cell paucity is reported across studies in ~**50–90%** of CVID enteropathy biopsies (marsden2024paucityofgastrointestinal pages 1-2).
- Proposed conservative definitions: **<10 plasma cells/HPF at 40×**, or **1–5%** of mononuclear cells, recorded across **≥3 sections** and **≥2 biopsies** (marsden2024paucityofgastrointestinal pages 1-2, marsden2024paucityofgastrointestinal pages 5-7).
- Colon biopsies show paucity/absence in **~60–85%** in most studies; IgA+ plasma cells are frequently most reduced (marsden2024paucityofgastrointestinal pages 3-5).

## 9. Current applications and real-world implementations

### 9.1 Standard of care
- **Immunoglobulin replacement therapy (IgRT)** (IVIG/SCIG) is the “mainstay,” with evidence that it **reduces infectious episode rates and severity** (tessarin2023monogenicformsof pages 1-2) and is described as standard management when antibody production is insufficient (cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).

### 9.2 Precision medicine in monogenic CVID-like disease
- **Abatacept** (CTLA-4–Ig) is “widely implemented” as bridge therapy in CTLA-4/LRBA defects with good results in key inflammatory manifestations (tessarin2023monogenicformsof pages 1-2, tessarin2023monogenicformsof pages 4-5).
- **Direct PI3K inhibitors** have been approved for APDS and show encouraging clinical/immunological control in that defined subgroup (tessarin2023monogenicformsof pages 1-2, tessarin2023monogenicformsof pages 4-5).
- **Sirolimus** is described as beneficial in some settings to enhance T-reg responses (tessarin2023monogenicformsof pages 4-5).

### 9.3 Diagnostic implementation: integrating immunophenotype + genomics
- The 2024 pediatric Mo-CVID work and 2024 PID sequencing meta-analysis both support structured criteria (clinical and immunologic) to prioritize and interpret NGS/WES in clinical practice (barbati2024monogeniccommonvariable pages 1-5, chen2024diagnosticyieldof pages 1-3).

## 10. Expert opinions / authoritative synthesis (review-derived analysis)

- A central interpretive position is that “CVID” is an umbrella phenotype with “incredible diversity of pathophysiological mechanisms,” where genotyping is increasingly necessary to resolve distinct disease entities and guide targeted therapy (peng2023commonvariableimmunodeficiency pages 12-13, alhakim2024thescopeand pages 2-4).
- Mechanistically, authoritative reviews emphasize convergent failure of GC outputs via disrupted **NF-κB**, **PI3K/AKT/mTOR**, and **BAFF/APRIL/TACI** signaling, plus immune regulatory lesions (CTLA4/LRBA) that produce combined antibody deficiency and organ-specific inflammation (peng2023commonvariableimmunodeficiency pages 7-9, peng2023commonvariableimmunodeficiency pages 9-10, peng2023commonvariableimmunodeficiency pages 13-15, tessarin2023monogenicformsof pages 4-5).

## Structured knowledge-base elements

### Pathophysiology description (knowledge-base ready)
CVID is a heterogeneous IEI syndrome characterized by hypogammaglobulinemia and impaired vaccine responses due to failure of germinal center–dependent B-cell terminal differentiation and reduced production/maintenance of class-switched memory B cells and plasma cells. Pathogenic mechanisms converge on (i) B-cell survival/differentiation signaling (BAFF/APRIL/TACI and NF-κB), (ii) GC organization and CSR/SHM (including PI3Kδ hyperactivation and AID-related mechanisms), and (iii) immune tolerance/checkpoint regulation (CTLA-4/LRBA and related Tfh/Treg dysregulation), leading not only to infections but frequently to immune dysregulation (autoimmunity, lymphoproliferation, enteropathy, and interstitial lung disease) in a substantial fraction of patients (peng2023commonvariableimmunodeficiency pages 7-9, sircana2023commonvariableimmunodeficiency pages 3-4, peng2023commonvariableimmunodeficiency pages 9-10, peng2023commonvariableimmunodeficiency pages 13-15, alhakim2024thescopeand pages 2-4, cunninghamrundles2024commonvariableimmunodeficiency pages 1-2, marsden2024paucityofgastrointestinal pages 1-2).

### Gene/protein annotations (HGNC; representative set)
- *NFKB1, NFKB2* — NF-κB signaling; monogenic CVID-like disease; *NFKB1* described as a common monogenic cause (peng2023commonvariableimmunodeficiency pages 22-23, peng2023commonvariableimmunodeficiency pages 9-10).
- *TNFRSF13B (TACI), TNFRSF13C (BAFF-R)* — BAFF/APRIL signaling; association with CVID/sIgAD and autoimmunity risk in some carriers (peng2023commonvariableimmunodeficiency pages 7-9, sircana2023commonvariableimmunodeficiency pages 4-6).
- *PIK3CD, PIK3R1* — PI3Kδ pathway; APDS with CSR/GC disruption and CVID-like phenotype; PI3K inhibitors approved for APDS (peng2023commonvariableimmunodeficiency pages 9-10, tessarin2023monogenicformsof pages 1-2, tessarin2023monogenicformsof pages 4-5).
- *CTLA4, LRBA* — immune checkpoint/trafficking; immune dysregulation with antibody deficiency; abatacept widely used (peng2023commonvariableimmunodeficiency pages 13-15, tessarin2023monogenicformsof pages 4-5).
- *ICOS* — T-cell costimulation and GC Tfh help; included among key CVID genes (alhakim2024thescopeand pages 2-4).

### GO biological process candidates (selected)
- Immunoglobulin class switch recombination; somatic hypermutation; B-cell differentiation; plasma cell differentiation; NF-κB signaling; PI3K/AKT/mTOR signaling; regulation of T-cell activation/co-stimulation (peng2023commonvariableimmunodeficiency pages 12-13, peng2023commonvariableimmunodeficiency pages 7-9, peng2023commonvariableimmunodeficiency pages 9-10, peng2023commonvariableimmunodeficiency pages 13-15).

### Cell types (CL candidates)
B cell, plasma cell, T follicular helper cell, regulatory T cell, natural killer cell (alhakim2024thescopeand pages 2-4, peng2023commonvariableimmunodeficiency pages 13-15).

### Anatomical locations (UBERON candidates)
Lymph node/spleen (germinal centers), bone marrow, small intestine/colon/stomach, lung (alhakim2024thescopeand pages 2-4, sircana2023commonvariableimmunodeficiency pages 3-4, marsden2024paucityofgastrointestinal pages 3-5, marsden2024paucityofgastrointestinal pages 1-2).

### Chemical entities (selected)
Abatacept; PI3K inhibitors (APDS); sirolimus; immunoglobulin replacement products (tessarin2023monogenicformsof pages 1-2, tessarin2023monogenicformsof pages 4-5).

## Evidence tables

| Mechanistic Theme | Key Cells / Tissues | Key Pathways / Molecules | Representative Genes | Key Evidence / Statistics |
| :--- | :--- | :--- | :--- | :--- |
| **B-cell Maturation & Survival Defects** | B cells (Bone marrow, Lymph nodes), Plasma cells | BAFF/APRIL/TACI signaling; NF-κB signaling (canonical/non-canonical) | *TNFRSF13B* (TACI), *TNFRSF13C* (BAFF-R), *NFKB1*, *NFKB2*, *CD19*, *CD20*, *CD21*, *CD81* | • 85–94% of cases show IgG <4.5 g/L (alhakim2024thescopeand pages 2-4).<br>• TACI/BAFF-R defects found in 20–30% of patients (sircana2023commonvariableimmunodeficiency pages 4-6).<br>• *NFKB1* LOF variants are a common monogenic cause (peng2023commonvariableimmunodeficiency pages 22-23). |
| **Class-Switch & Plasma Cell Differentiation** | Germinal Center B cells, Plasma cells | CD40/CD40L; ICOS/ICOS-L; Cytokine signaling (IL-21, IL-10); Transcription factors | *ICOS*, *CD40LG*, *AICDA*, *STAT3*, *BACH2*, *PRKCD*, *IKZF1* | • Failure of terminal differentiation into memory B cells and plasma cells is central (alhakim2024thescopeand pages 2-4, sircana2023commonvariableimmunodeficiency pages 3-4).<br>• Gastrointestinal plasma cell paucity observed in 50–90% of CVID enteropathy biopsies (marsden2024paucityofgastrointestinal pages 2-3, marsden2024paucityofgastrointestinal pages 1-2). |
| **Immune Dysregulation & Tolerance Loss** | Regulatory T cells (Tregs), Tfh cells, Autoreactive B cells | CTLA-4 checkpoint; Transendocytosis; Autophagy | *CTLA4*, *LRBA*, *FOXP3*, *AIRE* | • *CTLA4* mutations (1.7–20.8%) and *LRBA* deficiency (0.9–7.2%) are major causes of immune dysregulation (tessarin2023monogenicformsof pages 4-5).<br>• Over 50% of patients have inflammatory/autoimmune complications (alhakim2024thescopeand pages 2-4). |
| **PI3K/AKT/mTOR Signaling** | B cells, T cells | PI3Kδ hyperactivation (APDS); AKT/mTOR signaling | *PIK3CD*, *PIK3R1*, *PTEN*, *TTC7A* | • *PIK3CD* GOF causes APDS with lymphoproliferation and exhausted T cells (peng2023commonvariableimmunodeficiency pages 9-10, tessarin2023monogenicformsof pages 1-2).<br>• Direct PI3K inhibitors approved for APDS (tessarin2023monogenicformsof pages 1-2, tessarin2023monogenicformsof pages 4-5). |
| **T-cell Dysfunction & Help** | CD4+ T cells, Tfh cells | T-cell activation; Cytokine production; Cytoskeletal dynamics | *ICOS*, *MAGT1*, *PLCG2*, *RAC2*, *DOCK8* | • T-cell defects documented in ~1/3 of CVID cases (alhakim2024thescopeand pages 2-4).<br>• *MAGT1* defects link magnesium transport to T-cell activation and EBV control (peng2023commonvariableimmunodeficiency pages 22-23). |
| **Diagnostic Yield & Genetics** | Systemic | NGS (WES/Targeted Panels) | N/A | • Monogenic causes identified in 20–50% of cases (alhakim2024thescopeand pages 2-4, cunninghamrundles2024commonvariableimmunodeficiency pages 1-2).<br>• Diagnostic yield of NGS in PIDs is ~42%, higher with family history (~58%) (chen2024diagnosticyieldof pages 1-3). |


*Table: Summary of core pathophysiological mechanisms in Common Variable Immunodeficiency, including affected cells, pathways, representative genes, and key statistical evidence from recent literature.*

## Key references (with URLs and publication timing)
- Peng XP, Caballero-Oteyza A, Grimbacher B. *Common Variable Immunodeficiency: More Pathways than Roads to Rome.* **Annual Review of Pathology**. **Jan 2023**. https://doi.org/10.1146/annurev-pathmechdis-031521-024229 (peng2023commonvariableimmunodeficiency pages 12-13)
- Sircana MC et al. *Common Variable Immunodeficiency and Selective IgA Deficiency: Focus on Autoimmune Manifestations and Their Pathogenesis.* **Int J Transl Med**. **Oct 2023**. https://doi.org/10.3390/ijtm3040031 (sircana2023commonvariableimmunodeficiency pages 3-4)
- Tessarin G et al. *Monogenic forms of common variable immunodeficiency and implications on target therapeutic approaches.* **Curr Opin Allergy Clin Immunol**. **Sep 2023**. https://doi.org/10.1097/aci.0000000000000947 (tessarin2023monogenicformsof pages 1-2)
- Al‑Hakim A et al. *The Scope and Impact of Viral Infections in CVID and CVID-like Disorders: A Literature Review.* **J Clin Med**. **Mar 2024**. https://doi.org/10.3390/jcm13061717 (alhakim2024thescopeand pages 2-4)
- Chen Y et al. *Diagnostic yield of next-generation sequencing in suspect primary immunodeficiencies diseases: a systematic review and meta-analysis.* **Clin Exp Med**. **Jun 2024**. https://doi.org/10.1007/s10238-024-01392-2 (chen2024diagnosticyieldof pages 1-3)
- Cunningham‑Rundles C et al. *Common variable immunodeficiency: autoimmune cytopenias and advances in molecular diagnosis.* **Hematology (ASH Education)**. **Dec 2024**. https://doi.org/10.1182/hematology.2024000538 (cunninghamrundles2024commonvariableimmunodeficiency pages 1-2)
- Marsden JWN et al. *Paucity of gastrointestinal plasma cells in common variable immunodeficiency.* **Curr Opin Allergy Clin Immunol**. **Oct 2024**. https://doi.org/10.1097/aci.0000000000001040 (marsden2024paucityofgastrointestinal pages 1-2)

## Notes on limitations of this synthesis
- This report is constrained to mechanisms and quantitative statistics present in the retrieved full-text excerpts; some CVID-specific sequencing yield estimates and mechanistic details for particular pathways may require additional primary studies not yet retrieved in this run.
- Some evidence items above (e.g., abatacept response rates) are derived from authoritative reviews summarizing multiple cohorts; interpretation should consider underlying study heterogeneity (tessarin2023monogenicformsof pages 4-5).


References

1. (alhakim2024thescopeand pages 2-4): Adam Al-Hakim, Mark Kacar, and Sinisa Savic. The scope and impact of viral infections in common variable immunodeficiency (cvid) and cvid-like disorders: a literature review. Journal of Clinical Medicine, 13:1717, Mar 2024. URL: https://doi.org/10.3390/jcm13061717, doi:10.3390/jcm13061717. This article has 8 citations.

2. (sircana2023commonvariableimmunodeficiency pages 3-4): Marta Chiara Sircana, Gianpaolo Vidili, Antonio Gidaro, Alessandro Palmerio Delitala, Fabiana Filigheddu, Roberto Castelli, and Roberto Manetti. Common variable immunodeficiency and selective iga deficiency: focus on autoimmune manifestations and their pathogenesis. International Journal of Translational Medicine, 3:432-460, Oct 2023. URL: https://doi.org/10.3390/ijtm3040031, doi:10.3390/ijtm3040031. This article has 7 citations.

3. (barbati2024monogeniccommonvariable pages 1-5): Federica Barbati, Lorenzo Lodi, Silvia Boscia, Martina Cortimiglia, Elisa Calistri, Francesca Quaranta, Laura Maggi, Alessio Mazzoni, Boaz Palterer, Francesco Annunziato, Chiara Azzari, and Silvia Ricci. Monogenic common variable immunodeficiency (mo-cvid) score for optimizing the diagnostic metamorphosis in pediatric cvid cohort. Unknown journal, Jun 2024. URL: https://doi.org/10.21203/rs.3.rs-4438029/v1, doi:10.21203/rs.3.rs-4438029/v1.

4. (cunninghamrundles2024commonvariableimmunodeficiency pages 1-2): Charlotte Cunningham-Rundles, Jean-Laurent Casanova, and Bertrand Boisson. Common variable immunodeficiency: autoimmune cytopenias and advances in molecular diagnosis. Hematology, 2024:137-142, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000538, doi:10.1182/hematology.2024000538. This article has 10 citations and is from a peer-reviewed journal.

5. (peng2023commonvariableimmunodeficiency pages 7-9): Xiao P. Peng, Andrés Caballero-Oteyza, and Bodo Grimbacher. Common variable immunodeficiency: more pathways than roads to rome. Jan 2023. URL: https://doi.org/10.1146/annurev-pathmechdis-031521-024229, doi:10.1146/annurev-pathmechdis-031521-024229. This article has 65 citations and is from a domain leading peer-reviewed journal.

6. (peng2023commonvariableimmunodeficiency pages 9-10): Xiao P. Peng, Andrés Caballero-Oteyza, and Bodo Grimbacher. Common variable immunodeficiency: more pathways than roads to rome. Jan 2023. URL: https://doi.org/10.1146/annurev-pathmechdis-031521-024229, doi:10.1146/annurev-pathmechdis-031521-024229. This article has 65 citations and is from a domain leading peer-reviewed journal.

7. (peng2023commonvariableimmunodeficiency pages 22-23): Xiao P. Peng, Andrés Caballero-Oteyza, and Bodo Grimbacher. Common variable immunodeficiency: more pathways than roads to rome. Jan 2023. URL: https://doi.org/10.1146/annurev-pathmechdis-031521-024229, doi:10.1146/annurev-pathmechdis-031521-024229. This article has 65 citations and is from a domain leading peer-reviewed journal.

8. (peng2023commonvariableimmunodeficiency pages 12-13): Xiao P. Peng, Andrés Caballero-Oteyza, and Bodo Grimbacher. Common variable immunodeficiency: more pathways than roads to rome. Jan 2023. URL: https://doi.org/10.1146/annurev-pathmechdis-031521-024229, doi:10.1146/annurev-pathmechdis-031521-024229. This article has 65 citations and is from a domain leading peer-reviewed journal.

9. (peng2023commonvariableimmunodeficiency pages 13-15): Xiao P. Peng, Andrés Caballero-Oteyza, and Bodo Grimbacher. Common variable immunodeficiency: more pathways than roads to rome. Jan 2023. URL: https://doi.org/10.1146/annurev-pathmechdis-031521-024229, doi:10.1146/annurev-pathmechdis-031521-024229. This article has 65 citations and is from a domain leading peer-reviewed journal.

10. (tessarin2023monogenicformsof pages 4-5): Giulio Tessarin, Manuela Baronio, and Vassilios Lougaris. Monogenic forms of common variable immunodeficiency and implications on target therapeutic approaches. Current Opinion in Allergy and Clinical Immunology, 23:461-466, Sep 2023. URL: https://doi.org/10.1097/aci.0000000000000947, doi:10.1097/aci.0000000000000947. This article has 7 citations and is from a peer-reviewed journal.

11. (sircana2023commonvariableimmunodeficiency pages 4-6): Marta Chiara Sircana, Gianpaolo Vidili, Antonio Gidaro, Alessandro Palmerio Delitala, Fabiana Filigheddu, Roberto Castelli, and Roberto Manetti. Common variable immunodeficiency and selective iga deficiency: focus on autoimmune manifestations and their pathogenesis. International Journal of Translational Medicine, 3:432-460, Oct 2023. URL: https://doi.org/10.3390/ijtm3040031, doi:10.3390/ijtm3040031. This article has 7 citations.

12. (tessarin2023monogenicformsof pages 1-2): Giulio Tessarin, Manuela Baronio, and Vassilios Lougaris. Monogenic forms of common variable immunodeficiency and implications on target therapeutic approaches. Current Opinion in Allergy and Clinical Immunology, 23:461-466, Sep 2023. URL: https://doi.org/10.1097/aci.0000000000000947, doi:10.1097/aci.0000000000000947. This article has 7 citations and is from a peer-reviewed journal.

13. (marsden2024paucityofgastrointestinal pages 1-2): Jan Willem N. Marsden, Miangela M. Laclé, Mirjam Severs, and Helen Louisa Leavis. Paucity of gastrointestinal plasma cells in common variable immunodeficiency. Oct 2024. URL: https://doi.org/10.1097/aci.0000000000001040, doi:10.1097/aci.0000000000001040. This article has 8 citations and is from a peer-reviewed journal.

14. (chen2024diagnosticyieldof pages 1-3): Yingying Chen, Dongrui Li, Jiawen Yin, Jinglin Xiong, Min Xu, Qing Qi, and Wenlin Yang. Diagnostic yield of next-generation sequencing in suspect primary immunodeficiencies diseases: a systematic review and meta-analysis. Clinical and Experimental Medicine, Jun 2024. URL: https://doi.org/10.1007/s10238-024-01392-2, doi:10.1007/s10238-024-01392-2. This article has 8 citations and is from a peer-reviewed journal.

15. (marsden2024paucityofgastrointestinal pages 5-7): Jan Willem N. Marsden, Miangela M. Laclé, Mirjam Severs, and Helen Louisa Leavis. Paucity of gastrointestinal plasma cells in common variable immunodeficiency. Oct 2024. URL: https://doi.org/10.1097/aci.0000000000001040, doi:10.1097/aci.0000000000001040. This article has 8 citations and is from a peer-reviewed journal.

16. (marsden2024paucityofgastrointestinal pages 3-5): Jan Willem N. Marsden, Miangela M. Laclé, Mirjam Severs, and Helen Louisa Leavis. Paucity of gastrointestinal plasma cells in common variable immunodeficiency. Oct 2024. URL: https://doi.org/10.1097/aci.0000000000001040, doi:10.1097/aci.0000000000001040. This article has 8 citations and is from a peer-reviewed journal.

17. (marsden2024paucityofgastrointestinal pages 2-3): Jan Willem N. Marsden, Miangela M. Laclé, Mirjam Severs, and Helen Louisa Leavis. Paucity of gastrointestinal plasma cells in common variable immunodeficiency. Oct 2024. URL: https://doi.org/10.1097/aci.0000000000001040, doi:10.1097/aci.0000000000001040. This article has 8 citations and is from a peer-reviewed journal.