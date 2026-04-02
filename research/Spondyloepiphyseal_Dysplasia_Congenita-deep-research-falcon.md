---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-02T15:45:56.747920'
end_time: '2026-04-02T16:07:21.422422'
duration_seconds: 1284.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spondyloepiphyseal Dysplasia Congenita
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Spondyloepiphyseal Dysplasia Congenita
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Spondyloepiphyseal Dysplasia Congenita**.
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
- **Disease Name:** Spondyloepiphyseal Dysplasia Congenita
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Spondyloepiphyseal Dysplasia Congenita**.
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


## Comprehensive Research Report: Pathophysiology of Spondyloepiphyseal Dysplasia Congenita (SEDC)

### Disease overview and key definitions
**Spondyloepiphyseal dysplasia congenita (SEDC)** is a Mendelian (typically autosomal dominant) skeletal dysplasia within the **type II collagenopathy** spectrum caused by pathogenic variants in **COL2A1** (collagen type II alpha 1 chain). It is characterized by disproportionate short-trunk short stature with **platyspondyly** and epiphyseal dysplasia and has frequent extraskeletal manifestations due to type II collagen expression in the **vitreous** and **inner ear** (ocular and hearing involvement). (zhan2025clinicalfeaturesof pages 2-2, marchionni2023clinicalandfunctional pages 1-2)

**Epidemiology/statistics (selected):**
* A review focused on COL2A1/SEDC reports **SEDC prevalence ~3.4 per 1,000,000**. (nenna2019col2a1genemutations pages 2-3)
* In a published SEDC cohort summary cited by a 2022 SEDC series: **86%** short stature, **>50%** underwent orthopedic surgery, **45%** myopia, **37%** hearing loss. (akahiraazuma2022novelcol2a1variants pages 2-3)
* Additional complication rates reported in the COL2A1/SEDC review include **retinal detachment ~12%** and **sensorineural hearing loss ~25–30% of adults**. (nenna2019col2a1genemutations pages 2-3)

### 1) Core pathophysiology (current understanding)
SEDC is primarily a disorder of **type II collagen biosynthesis, folding/quality control, secretion, and extracellular matrix (ECM) assembly** in cartilage. The unifying mechanistic theme across model systems is that many COL2A1 variants (especially **glycine substitutions** in the triple helix, or certain C-propeptide variants) produce **misfolded procollagen-II**, which then:
1. **Folds slowly / aberrantly and becomes hypermodified**,
2. **Accumulates intracellularly (often in the rough ER)** causing ER dilation,
3. Leads to either:
   * **canonical ER stress / UPR activation with apoptosis** in some settings (strongly supported in a Col2a1 p.Gly1170Ser knock-in mouse), or
   * **ER storage with minimal transcriptional UPR activation** in other settings (supported in a 2024 human iPSC-derived cartilage model).
4. Results in **decreased secretion and defective extracellular collagen fibril network**, producing a sparse/disorganized cartilage ECM.
5. Disrupts **growth plate architecture and chondrocyte differentiation (including hypertrophy)**, impairing endochondral ossification and leading to short-trunk dwarfism and epiphyseal/spinal malformations. (liang2014endoplasmicreticulumstressunfolding pages 1-3, esapa2012amousemodel pages 1-2, yammine2023erprocollagenstorage pages 9-12)

**Direct mechanistic quote-level evidence:** In a Col2a1 p.Gly1170Ser knock-in mouse model, mutant procollagen “was largely synthesized and retained in dilated endoplasmic reticulum” and this retention could “activate a signaling network of the unfolded protein response (UPR)” and, if unresolved, “apoptosis was initiated”; importantly, apoptosis “occurred prior to hypertrophy,” preventing formation of a hypertrophic zone and causing chondrodysplasia. (liang2014endoplasmicreticulumstressunfolding pages 1-3)

### 2) Dysregulated molecular pathways

#### A. Collagen folding/processing and ER proteostasis
A 2024 human iPSC-derived cartilage model of COL2A1 **p.Gly1170Ser** provides quantitative evidence of ER retention and hypermodification:
* **Intracellular retention** by blinded IHC scoring: **64%** of heterozygous cells retained procollagen-II vs **34%** WT; **>80%** retention in homozygotes. (yammine2023erprocollagenstorage pages 9-12)
* **Triple-helix assembly burden:** in heterozygotes, **>85% of trimers** contained at least one mutant chain. (yammine2023erprocollagenstorage pages 9-12)
* ER localization supported by **co-localization with calreticulin** and ER dilation by TEM. (yammine2023erprocollagenstorage pages 9-12)

This study frames the defect as an **“ER storage disorder”**: mutant procollagen-II “accumulates intracellularly, consistent with an endoplasmic reticulum (ER) storage disorder,” and is “notably slow to fold and secrete.” (yammine2023erprocollagenstorage pages 1-5)

#### B. Unfolded Protein Response (UPR) branches (PERK/ATF4/CHOP, IRE1/XBP1, ATF6)
**Model-dependent UPR engagement is a key nuance in current understanding.**

*In vivo mouse (UPR+apoptosis phenotype):* The Col2a1 p.Gly1170Ser knock-in mouse directly assayed canonical UPR components by qRT-PCR (**Chop, Total-Xbp1, Spliced-Xbp1, Grp78/BiP, ATF4, ATF6**), consistent with engagement of PERK/ATF4/CHOP, IRE1/XBP1, and ATF6 branches. (liang2014endoplasmicreticulumstressunfolding pages 5-9)

*Human iPSC cartilage model (limited transcriptional UPR):* In the 2024 iPSC cartilage model, despite prominent ER retention and ER dilation, transcriptome/GSEA analyses showed **no detectable UPR induction in clinically relevant heterozygotes** (and only modest changes in homozygotes at an early time point). (yammine2023erprocollagenstorage pages 9-12)

This group explicitly states that ER accumulation was not accompanied by “any substantive UPR” and noted an “absence of the type of chronic activation of the PERK arm of the UPR that can induce apoptosis over time.” (yammine2023erprocollagenstorage pages 15-18)

**Interpretation:** The field is converging on the idea that **misfolded collagen retention is necessary but not sufficient** for a canonical UPR signature; the collagen triple helix may be unusually “UPR-evasive” compared with globular misfolded proteins, leading to substantial ER retention with muted UPR depending on allele dosage, cell state, and model system. (yammine2023erprocollagenstorage pages 9-12, yammine2023erprocollagenstorage pages 15-18)

#### C. Apoptosis and growth plate disruption
In the Col2a1 p.Gly1170Ser knock-in mouse, chondrocyte apoptosis is a central causal event and occurs before hypertrophic differentiation, thereby collapsing the hypertrophic zone and impairing endochondral ossification. (liang2014endoplasmicreticulumstressunfolding pages 1-3)

**Image-based evidence from the same study** shows:
* **Dilated rough ER on TEM** in mutant proliferating-zone chondrocytes.
* **Intracellular retention of mutant procollagen-II co-localizing with GRP78** (ER marker).
* Upregulation of UPR/ER-stress genes.
* Increased apoptosis by **cleaved caspase-3** staining and **TUNEL** positivity. (liang2014endoplasmicreticulumstressunfolding media a802b0c3, liang2014endoplasmicreticulumstressunfolding media 7e048216, liang2014endoplasmicreticulumstressunfolding media 4409704f, liang2014endoplasmicreticulumstressunfolding media 919d3da4)

In contrast, the 2024 iPSC cartilage model did **not** detect increased apoptosis (TUNEL) in either heterozygous or homozygous chondronoids, despite ER retention—again emphasizing context dependence. (yammine2023erprocollagenstorage pages 12-15)

#### D. Extracellular matrix (ECM) fibrillogenesis defects
Multiple sources support defective extracellular collagen network formation:
* The 2024 iPSC cartilage model described collagen fibrils as “generally shorter, yielding a very sparse network,” with “intracellular retention of collagen-II,” and “dilated ER.” (yammine2024erprocollagenstoragea pages 83-88)
* A Col2a1 C-propeptide (Ser1386Pro) mouse model showed reduced cartilage type II collagen staining and EM evidence of fewer/less elaborate collagen fibrils plus enlarged ER vacuoles containing inclusions—supporting defective fibrillogenesis coupled to intracellular trafficking/processing defects. (esapa2012amousemodel pages 1-2)

### 3) Key molecular players

#### Genes / proteins
**Causal gene**
* **COL2A1 (HGNC:2200)** — encodes the α1(II) chain of type II procollagen (a homotrimer), the major fibrillar collagen of hyaline cartilage; produced by proliferating chondrocytes. (marchionni2023clinicalandfunctional pages 1-2)

**Core ER stress/UPR markers and regulators observed/assayed in SEDC models**
* **HSPA5/GRP78/BiP** (ER chaperone; used as ER marker and UPR readout). (liang2014endoplasmicreticulumstressunfolding pages 5-9, liang2014endoplasmicreticulumstressunfolding media a802b0c3)
* **XBP1 (spliced Xbp1)** (IRE1 branch output). (liang2014endoplasmicreticulumstressunfolding pages 5-9)
* **ATF4** (PERK branch output). (liang2014endoplasmicreticulumstressunfolding pages 5-9)
* **ATF6** (ATF6 branch). (liang2014endoplasmicreticulumstressunfolding pages 5-9)
* **DDIT3/CHOP** (pro-apoptotic UPR mediator). (liang2014endoplasmicreticulumstressunfolding pages 5-9)

**Proteostasis/collagen-modifying factors enriched for interaction with slow-folding mutant procollagen-II (human iPSC model)**
* **PLOD2, P4HB, P3H1, FKBP10, PPIB**, plus chaperones **CALR** (calreticulin) and **SERPINH1** (HSP47) consistent with slow folding/hypermodification and ER retention. (yammine2023erprocollagenstorage pages 12-15)

**Apoptosis readouts (mouse model evidence)**
* **Cleaved caspase-3** and **TUNEL positivity** in growth plate chondrocytes. (liang2014endoplasmicreticulumstressunfolding media a802b0c3, liang2014endoplasmicreticulumstressunfolding media 7e048216)

#### Chemical entities (metabolites/drugs/small molecules)
No disease-modifying pharmacologic therapy is established for SEDC in the provided mechanistic evidence set. However, the iPSC cartilage model explicitly positions itself as enabling “rapid testing of therapeutic strategies to restore proteostasis in the collagenopathies,” implying chemical chaperones/proteostasis modulators as plausible candidates for future work. (yammine2023erprocollagenstorage pages 1-5)

#### Cell types (primary)
* **Chondrocytes** (including growth plate chondrocytes; proliferative and hypertrophic zones). (nenna2019col2a1genemutations pages 2-3, esapa2012amousemodel pages 1-2)

#### Anatomical locations / tissues
* **Hyaline cartilage** and **growth plate cartilage** (primary lesion site). (morales2025theuseof pages 38-42, esapa2012amousemodel pages 1-2)
* **Vertebrae** (platyspondyly) and **epiphyses/proximal long bones** (epiphyseal dysplasia). (zhan2025clinicalfeaturesof pages 2-2, akahiraazuma2022novelcol2a1variants pages 2-3)
* **Vitreous/retina** (myopia/retinal detachment risk) and **inner ear** (hearing impairment). (nenna2019col2a1genemutations pages 2-3, zhan2025clinicalfeaturesof pages 2-2)

### 4) Biological processes disrupted (GO-oriented)
Based on mechanistic evidence in mouse and human cartilage models, disrupted processes include:
* **Protein folding and quality control in the endoplasmic reticulum** (misfolded procollagen retention; ER dilation). (liang2014endoplasmicreticulumstressunfolding pages 1-3, yammine2023erprocollagenstorage pages 9-12)
* **Unfolded protein response (UPR)** (PERK/ATF4/CHOP; IRE1/XBP1; ATF6) — robust in some in vivo settings, minimal in others. (liang2014endoplasmicreticulumstressunfolding pages 5-9, yammine2023erprocollagenstorage pages 9-12)
* **ER-associated stress response / ER lumen homeostasis** (evidenced by GRP78 localization and ER dilation). (liang2014endoplasmicreticulumstressunfolding media a802b0c3, yammine2023erprocollagenstorage pages 9-12)
* **Apoptotic process** (cleaved caspase-3/TUNEL positivity in growth plate). (liang2014endoplasmicreticulumstressunfolding media a802b0c3, liang2014endoplasmicreticulumstressunfolding media 7e048216)
* **Collagen fibril organization / extracellular matrix organization** (sparse, abnormal collagen fibrillar network; reduced secretion). (yammine2024erprocollagenstoragea pages 83-88, esapa2012amousemodel pages 1-2)
* **Chondrocyte proliferation and differentiation (including hypertrophic differentiation)** (reduced proliferation; hypertrophic zone failure in mouse). (liang2014endoplasmicreticulumstressunfolding pages 5-9, liang2014endoplasmicreticulumstressunfolding pages 1-3)

### 5) Cellular components (where processes occur)
* **Rough endoplasmic reticulum / ER lumen** — site of procollagen synthesis, folding, retention, ER dilation, and UPR sensing. (liang2014endoplasmicreticulumstressunfolding media a802b0c3, yammine2023erprocollagenstorage pages 9-12)
* **Golgi apparatus / secretory pathway vesicles** — implicated in abnormal trafficking/processing of mutant collagen. (marchionni2023clinicalandfunctional pages 1-2)
* **Extracellular space / cartilage extracellular matrix** — deficient/sparse collagen network and abnormal fibrils. (yammine2024erprocollagenstoragea pages 83-88, esapa2012amousemodel pages 1-2)

### 6) Disease progression model (sequence of events)
A mechanistically supported sequence integrating mouse and human iPSC evidence is:
1. **Primary trigger:** pathogenic COL2A1 variant (commonly glycine substitution in triple helix; or C-propeptide variant). (marchionni2023clinicalandfunctional pages 1-2, esapa2012amousemodel pages 1-2)
2. **Molecular defect:** slow folding/misfolding of procollagen-II → hypermodification, impaired trimer maturation. (yammine2023erprocollagenstorage pages 9-12)
3. **Cellular defect:** ER retention/accumulation → ER dilation; variable engagement of canonical UPR transcription depending on context/dose. (yammine2023erprocollagenstorage pages 9-12, liang2014endoplasmicreticulumstressunfolding pages 5-9)
4. **Downstream cellular outcome (context-dependent):**
   * In severe settings: UPR activation (CHOP/XBP1/ATF4/ATF6) → apoptosis (cleaved caspase-3, TUNEL) → loss of hypertrophic zone and disrupted growth plate. (liang2014endoplasmicreticulumstressunfolding pages 1-3, liang2014endoplasmicreticulumstressunfolding media a802b0c3)
   * In other settings: ER storage disorder with adaptive remodeling and minimal UPR signature, but persistent matrix deficiency. (yammine2023erprocollagenstorage pages 9-12, yammine2023erprocollagenstorage pages 15-18)
5. **Tissue outcome:** sparse/abnormal cartilage ECM, growth plate disorganization → abnormal endochondral ossification. (esapa2012amousemodel pages 1-2, yammine2024erprocollagenstoragea pages 83-88)
6. **Clinical outcome:** disproportionate short-trunk short stature, vertebral flattening, epiphyseal dysplasia; progressive joint disease/early osteoarthritis; ocular and hearing complications. (akahiraazuma2022novelcol2a1variants pages 2-3, nenna2019col2a1genemutations pages 2-3)

### 7) Phenotypic manifestations (HP-oriented)
Key phenotypes and mechanistic links:
* **Disproportionate short stature / short trunk** arises from growth plate dysfunction and impaired endochondral ossification due to deficient collagen II ECM and (in some models) growth plate chondrocyte apoptosis. (liang2014endoplasmicreticulumstressunfolding pages 1-3, zhan2025clinicalfeaturesof pages 2-2)
* **Platyspondyly and epiphyseal dysplasia** reflect abnormal cartilage template formation in vertebrae and proximal epiphyses. (zhan2025clinicalfeaturesof pages 2-2, akahiraazuma2022novelcol2a1variants pages 2-3)
* **Early degenerative joint disease / osteoarthritis** plausibly reflects both developmental cartilage defects and ongoing matrix fragility; supported by mouse models with secondary OA. (esapa2012amousemodel pages 1-2)
* **Myopia/retinal detachment** and **hearing impairment** track with type II collagen roles in vitreous and inner ear structures; frequencies reported above. (akahiraazuma2022novelcol2a1variants pages 2-3, nenna2019col2a1genemutations pages 2-3)

### 8) Recent developments and latest research (prioritizing 2023–2024)
**2024 (preprint): Human iPSC-derived cartilage model reframing ER stress expectations.**
A 2024 iPSC-derived cartilage study of COL2A1 p.Gly1170Ser provides a quantitatively supported concept that type II collagen misfolding can create an **ER procollagen storage defect without a coupled canonical UPR**, challenging a simplistic “misfolding always → UPR → apoptosis” model. The study quantifies intracellular retention (64% vs 34% WT) and shows ER dilation and a sparse collagen network but minimal UPR transcriptional induction in heterozygotes and no increased apoptosis by TUNEL. (yammine2023erprocollagenstorage pages 9-12, yammine2023erprocollagenstorage pages 12-15)

**2023: Cellular functional characterization in patients/variants.**
A 2023 functional case-based analysis of a COL2A1 glycine substitution links glycine replacements to disrupted triple helix integrity and reports intracellular accumulation/secretory pathway alterations and ECM disorganization (e.g., fibronectin network disruption) consistent with defective matrix assembly in type II collagenopathies. (marchionni2023clinicalandfunctional pages 1-2)

### 9) Current applications and real-world implementations
* **Molecular diagnosis in clinical practice:** NGS panels/WES plus confirmatory Sanger sequencing are routinely used for COL2A1 variant identification; accurate diagnosis is emphasized for early monitoring of extraskeletal complications (ocular/hearing/cervical instability). (akahiraazuma2022novelcol2a1variants pages 1-2)
* **Model systems for therapeutic development:** iPSC-derived cartilage/chondronoid platforms are positioned as translational tools for mechanistic study and therapeutic screening of proteostasis-restoring interventions in collagenopathies. (yammine2023erprocollagenstorage pages 1-5)

### 10) Expert opinion / analysis (authoritative synthesis)
Across mechanistic sources, there is consensus that **cartilage ECM deficiency driven by mutant collagen II proteostasis and assembly defects** is central to SEDC. The key expert-level nuance from recent iPSC work is that the **presence/absence of canonical UPR signatures** may vary by genotype dosage and model, and thus **UPR readouts are not universally reliable proxies** for collagen II misfolding burden; nonetheless, ER retention and ECM deficiency remain consistent cellular pathologies. (yammine2023erprocollagenstorage pages 9-12, liang2014endoplasmicreticulumstressunfolding pages 1-3)

---

## Knowledge-base-ready structured annotations

### MONDO / disease identifiers
* MONDO ID was not available in the retrieved evidence set.

### Gene / protein annotations (HGNC)
* **COL2A1 (HGNC:2200)** — causal gene for SEDC. (akahiraazuma2022novelcol2a1variants pages 1-2)

### Key pathways / processes (GO candidates; evidence-linked)
* **Protein folding in endoplasmic reticulum** (misfolded procollagen retained in dilated ER). (liang2014endoplasmicreticulumstressunfolding pages 1-3, yammine2023erprocollagenstorage pages 9-12)
* **Unfolded protein response** (Chop/Xbp1/Grp78/ATF4/ATF6 assayed and upregulated in mouse). (liang2014endoplasmicreticulumstressunfolding pages 5-9)
* **Apoptotic process** (cleaved caspase-3/TUNEL in mouse growth plate). (liang2014endoplasmicreticulumstressunfolding media a802b0c3, liang2014endoplasmicreticulumstressunfolding media 7e048216)
* **Collagen fibril organization / extracellular matrix organization** (sparse network, abnormal fibrils, reduced secretion). (yammine2024erprocollagenstoragea pages 83-88, esapa2012amousemodel pages 1-2)
* **Chondrocyte proliferation and hypertrophic differentiation** (reduced proliferation; loss of hypertrophic zone in severe mouse model). (liang2014endoplasmicreticulumstressunfolding pages 5-9, liang2014endoplasmicreticulumstressunfolding pages 1-3)

### Cellular components (GO-CC candidates)
* **Rough endoplasmic reticulum / ER lumen** (dilated ER with retained procollagen). (liang2014endoplasmicreticulumstressunfolding media a802b0c3, yammine2023erprocollagenstorage pages 9-12)
* **Golgi apparatus / secretory vesicles** (trafficking/processing changes for mutant collagen). (marchionni2023clinicalandfunctional pages 1-2)
* **Extracellular matrix / extracellular space** (deficient collagen network). (yammine2024erprocollagenstoragea pages 83-88)

### Cell type involvement (CL candidates)
* **Chondrocyte** (including growth plate chondrocytes). (esapa2012amousemodel pages 1-2, nenna2019col2a1genemutations pages 2-3)

### Anatomical locations (UBERON candidates)
* **Hyaline cartilage** and **growth plate cartilage**. (morales2025theuseof pages 38-42, esapa2012amousemodel pages 1-2)
* **Vertebrae** and **epiphyses of long bones**. (akahiraazuma2022novelcol2a1variants pages 2-3, zhan2025clinicalfeaturesof pages 2-2)
* **Vitreous body/retina** and **inner ear**. (nenna2019col2a1genemutations pages 2-3, zhan2025clinicalfeaturesof pages 2-2)

### Phenotype associations (HP candidates)
* Disproportionate short stature / short trunk, platyspondyly, epiphyseal dysplasia, hip dysplasia/coxa vara, early osteoarthritis, myopia, retinal detachment, sensorineural hearing loss, cleft palate/Pierre Robin sequence. (akahiraazuma2022novelcol2a1variants pages 2-3, nenna2019col2a1genemutations pages 2-3, marchionni2023clinicalandfunctional pages 1-2)

### Chemical entities (CHEBI candidates)
* No specific disease-modifying small molecules were identified in the retrieved mechanistic evidence; proteostasis-targeting strategies are proposed conceptually for testing in iPSC models. (yammine2023erprocollagenstorage pages 1-5)

---

## Evidence items with PMIDs (where available)
* **Liang et al., PLoS ONE (Jan 2014)** “Endoplasmic Reticulum Stress-Unfolding Protein Response-Apoptosis Cascade Causes Chondrodysplasia in a col2a1 p.Gly1170Ser Mutated Mouse Model.” DOI: https://doi.org/10.1371/journal.pone.0086894 (PMID not provided in retrieved text). (liang2014endoplasmicreticulumstressunfolding pages 1-3, liang2014endoplasmicreticulumstressunfolding pages 5-9)
* **Esapa et al., J Bone Miner Res (Feb 2012)** “A mouse model for spondyloepiphyseal dysplasia congenita with secondary osteoarthritis due to a Col2a1 mutation.” DOI: https://doi.org/10.1002/jbmr.547 (PMID not provided in retrieved text). (esapa2012amousemodel pages 1-2)
* **Akahira-Azuma et al., Human Genome Variation (May 2022)** DOI: https://doi.org/10.1038/s41439-022-00193-x (PMID not provided in retrieved text). (akahiraazuma2022novelcol2a1variants pages 2-3)
* **Marchionni et al., Bone Reports (Dec 2023)** DOI: https://doi.org/10.1016/j.bonr.2023.101728 (PMID not provided in retrieved text). (marchionni2023clinicalandfunctional pages 1-2)
* **Yammine et al., bioRxiv (Oct 2024; preprint originally posted 2023-10-19)** “ER procollagen storage defect without coupled unfolded protein response drives precocious arthritis.” DOI: https://doi.org/10.1101/2023.10.19.562780 (preprint; no PMID). (yammine2023erprocollagenstorage pages 9-12, yammine2023erprocollagenstorage pages 12-15)
* **Nenna et al., Application of Clinical Genetics (Dec 2019)** DOI: https://doi.org/10.2147/tacg.s197205 (PMID not provided in retrieved text). (nenna2019col2a1genemutations pages 2-3)

### Notes on PMID availability
PMIDs were not present in the retrieved text snippets for several articles (including key mechanistic mouse studies). The DOIs and publication metadata above provide stable identifiers; PMIDs can be programmatically resolved from DOIs if needed.


References

1. (zhan2025clinicalfeaturesof pages 2-2): Shumin Zhan, Qin He, Jinna Yuan, Xiaoqin Xu, Ke Huang, Guanping Dong, Junfen Fu, Dingwen Wu, and Wei Wu. Clinical features of seven col2a1 variations in chinese children with type ii collagen disorders. Acta Paediatrica (Oslo, Norway : 1992), 114:1720-1730, Feb 2025. URL: https://doi.org/10.1111/apa.70029, doi:10.1111/apa.70029. This article has 5 citations.

2. (marchionni2023clinicalandfunctional pages 1-2): Enrica Marchionni, Maria Rosaria D'Apice, Viviana Lupo, Giovanna Lattanzi, Elisabetta Mattioli, Gina Lisignoli, Elena Gabusi, Gerardo Pepe, Manuela Helmer Citterich, Elena Campione, Anna Maria Nardone, Paola Spitalieri, Noemi Pucci, Dario Cocciadiferro, Eliseo Picchi, Francesco Garaci, Antonio Novelli, and Giuseppe Novelli. Clinical and functional characterization of col2a1 p.gly444ser variant: from a fetal phenotype to a previously undisclosed postnatal phenotype. Bone Reports, 19:101728, Dec 2023. URL: https://doi.org/10.1016/j.bonr.2023.101728, doi:10.1016/j.bonr.2023.101728. This article has 1 citations and is from a peer-reviewed journal.

3. (nenna2019col2a1genemutations pages 2-3): Raffaella Nenna, Arianna Turchetti, Gerarda Mastrogiorgio, and Fabio Midulla. Col2a1 gene mutations: mechanisms of spondyloepiphyseal dysplasia congenita. The Application of Clinical Genetics, 12:235-238, Dec 2019. URL: https://doi.org/10.2147/tacg.s197205, doi:10.2147/tacg.s197205. This article has 51 citations.

4. (akahiraazuma2022novelcol2a1variants pages 2-3): Moe Akahira-Azuma, Yumi Enomoto, Naoyuki Nakamura, Takayuki Yokoi, Mari Minatogawa, Noriaki Harada, Yoshinori Tsurusaki, and Kenji Kurosawa. Novel col2a1 variants in japanese patients with spondyloepiphyseal dysplasia congenita. Human Genome Variation, May 2022. URL: https://doi.org/10.1038/s41439-022-00193-x, doi:10.1038/s41439-022-00193-x. This article has 4 citations.

5. (liang2014endoplasmicreticulumstressunfolding pages 1-3): Guo-yan Liang, Chengjie Lian, Di Huang, Wenjie Gao, Anjing Liang, Yan Peng, Wei Ye, Zizhao Wu, Peiqiang Su, and Dongsheng Huang. Endoplasmic reticulum stress-unfolding protein response-apoptosis cascade causes chondrodysplasia in a col2a1 p.gly1170ser mutated mouse model. PLoS ONE, 9:e86894, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0086894, doi:10.1371/journal.pone.0086894. This article has 45 citations and is from a peer-reviewed journal.

6. (esapa2012amousemodel pages 1-2): Christopher T Esapa, Tertius A Hough, Sarah Testori, Rosie A Head, Elizabeth A Crane, Carol PS Chan, Holly Evans, JH Duncan Bassett, Przemko Tylzanowski, Eugene G McNally, Andrew J Carr, Alan Boyde, Peter GT Howell, Anne Clark, Graham R Williams, Matthew A Brown, Peter I Croucher, M Andrew Nesbit, Steve DM Brown, Roger D Cox, Michael T Cheeseman, and Rajesh V Thakker. A mouse model for spondyloepiphyseal dysplasia congenita with secondary osteoarthritis due to a col2a1 mutation. Journal of Bone and Mineral Research, 27:413-428, Feb 2012. URL: https://doi.org/10.1002/jbmr.547, doi:10.1002/jbmr.547. This article has 44 citations and is from a highest quality peer-reviewed journal.

7. (yammine2023erprocollagenstorage pages 9-12): Kathryn M. Yammine, Sophia Mirda Abularach, Seo-yeon Kim, Agata A. Bikovtseva, Jinia Lilianty, Vincent L. Butty, Richard P. Schiavoni, John F. Bateman, Shireen R. Lamandé, and Matthew D. Shoulders. Er procollagen storage defect without coupled unfolded protein response drives precocious arthritis. BioRxiv, Oct 2024. URL: https://doi.org/10.1101/2023.10.19.562780, doi:10.1101/2023.10.19.562780. This article has 5 citations.

8. (yammine2023erprocollagenstorage pages 1-5): Kathryn M. Yammine, Sophia Mirda Abularach, Seo-yeon Kim, Agata A. Bikovtseva, Jinia Lilianty, Vincent L. Butty, Richard P. Schiavoni, John F. Bateman, Shireen R. Lamandé, and Matthew D. Shoulders. Er procollagen storage defect without coupled unfolded protein response drives precocious arthritis. BioRxiv, Oct 2024. URL: https://doi.org/10.1101/2023.10.19.562780, doi:10.1101/2023.10.19.562780. This article has 5 citations.

9. (liang2014endoplasmicreticulumstressunfolding pages 5-9): Guo-yan Liang, Chengjie Lian, Di Huang, Wenjie Gao, Anjing Liang, Yan Peng, Wei Ye, Zizhao Wu, Peiqiang Su, and Dongsheng Huang. Endoplasmic reticulum stress-unfolding protein response-apoptosis cascade causes chondrodysplasia in a col2a1 p.gly1170ser mutated mouse model. PLoS ONE, 9:e86894, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0086894, doi:10.1371/journal.pone.0086894. This article has 45 citations and is from a peer-reviewed journal.

10. (yammine2023erprocollagenstorage pages 15-18): Kathryn M. Yammine, Sophia Mirda Abularach, Seo-yeon Kim, Agata A. Bikovtseva, Jinia Lilianty, Vincent L. Butty, Richard P. Schiavoni, John F. Bateman, Shireen R. Lamandé, and Matthew D. Shoulders. Er procollagen storage defect without coupled unfolded protein response drives precocious arthritis. BioRxiv, Oct 2024. URL: https://doi.org/10.1101/2023.10.19.562780, doi:10.1101/2023.10.19.562780. This article has 5 citations.

11. (liang2014endoplasmicreticulumstressunfolding media a802b0c3): Guo-yan Liang, Chengjie Lian, Di Huang, Wenjie Gao, Anjing Liang, Yan Peng, Wei Ye, Zizhao Wu, Peiqiang Su, and Dongsheng Huang. Endoplasmic reticulum stress-unfolding protein response-apoptosis cascade causes chondrodysplasia in a col2a1 p.gly1170ser mutated mouse model. PLoS ONE, 9:e86894, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0086894, doi:10.1371/journal.pone.0086894. This article has 45 citations and is from a peer-reviewed journal.

12. (liang2014endoplasmicreticulumstressunfolding media 7e048216): Guo-yan Liang, Chengjie Lian, Di Huang, Wenjie Gao, Anjing Liang, Yan Peng, Wei Ye, Zizhao Wu, Peiqiang Su, and Dongsheng Huang. Endoplasmic reticulum stress-unfolding protein response-apoptosis cascade causes chondrodysplasia in a col2a1 p.gly1170ser mutated mouse model. PLoS ONE, 9:e86894, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0086894, doi:10.1371/journal.pone.0086894. This article has 45 citations and is from a peer-reviewed journal.

13. (liang2014endoplasmicreticulumstressunfolding media 4409704f): Guo-yan Liang, Chengjie Lian, Di Huang, Wenjie Gao, Anjing Liang, Yan Peng, Wei Ye, Zizhao Wu, Peiqiang Su, and Dongsheng Huang. Endoplasmic reticulum stress-unfolding protein response-apoptosis cascade causes chondrodysplasia in a col2a1 p.gly1170ser mutated mouse model. PLoS ONE, 9:e86894, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0086894, doi:10.1371/journal.pone.0086894. This article has 45 citations and is from a peer-reviewed journal.

14. (liang2014endoplasmicreticulumstressunfolding media 919d3da4): Guo-yan Liang, Chengjie Lian, Di Huang, Wenjie Gao, Anjing Liang, Yan Peng, Wei Ye, Zizhao Wu, Peiqiang Su, and Dongsheng Huang. Endoplasmic reticulum stress-unfolding protein response-apoptosis cascade causes chondrodysplasia in a col2a1 p.gly1170ser mutated mouse model. PLoS ONE, 9:e86894, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0086894, doi:10.1371/journal.pone.0086894. This article has 45 citations and is from a peer-reviewed journal.

15. (yammine2023erprocollagenstorage pages 12-15): Kathryn M. Yammine, Sophia Mirda Abularach, Seo-yeon Kim, Agata A. Bikovtseva, Jinia Lilianty, Vincent L. Butty, Richard P. Schiavoni, John F. Bateman, Shireen R. Lamandé, and Matthew D. Shoulders. Er procollagen storage defect without coupled unfolded protein response drives precocious arthritis. BioRxiv, Oct 2024. URL: https://doi.org/10.1101/2023.10.19.562780, doi:10.1101/2023.10.19.562780. This article has 5 citations.

16. (yammine2024erprocollagenstoragea pages 83-88): KM Yammine, S Mirda Abularach, and S Kim. Er procollagen storage defect without associated unfolded protein response drives precocious osteoarthritis. Unknown journal, 2024.

17. (morales2025theuseof pages 38-42): LC Vertel Morales. The use of human induced pluripotent stem cells to model type 2 collagenopathies. Unknown journal, 2025.

18. (akahiraazuma2022novelcol2a1variants pages 1-2): Moe Akahira-Azuma, Yumi Enomoto, Naoyuki Nakamura, Takayuki Yokoi, Mari Minatogawa, Noriaki Harada, Yoshinori Tsurusaki, and Kenji Kurosawa. Novel col2a1 variants in japanese patients with spondyloepiphyseal dysplasia congenita. Human Genome Variation, May 2022. URL: https://doi.org/10.1038/s41439-022-00193-x, doi:10.1038/s41439-022-00193-x. This article has 4 citations.