---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-02T14:29:08.268917'
end_time: '2026-04-02T14:43:18.233186'
duration_seconds: 849.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypochondrogenesis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hypochondrogenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypochondrogenesis**.
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
- **Disease Name:** Hypochondrogenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypochondrogenesis**.
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


# Hypochondrogenesis (COL2A1-related type II collagenopathy): Pathophysiology Research Report

## Disease overview and definitions
Hypochondrogenesis is a severe, usually perinatal-lethal skeletal dysplasia within the **type II collagenopathy** spectrum caused by pathogenic variants in **COL2A1** (type II procollagen). It overlaps clinically and mechanistically with **achondrogenesis type II**, and both are often discussed as a continuum of severity within COL2A1 structural (dominant-negative) disease. (wu2025prenatalimagingof pages 6-7, myllyharju2014extracellularmatrixand pages 1-2)

**Key concept (current understanding):** hypochondrogenesis is best understood as a combined disorder of (i) **intracellular procollagen II proteostasis** (misfolding, delayed folding, intracellular retention, ER stress/UPR signaling and/or proteostasis failure) and (ii) **extracellular matrix (ECM) insufficiency/architectural disruption** of collagen II fibrils, which secondarily derails growth plate organization and endochondral ossification. (okada2015modelingtypeii pages 2-4, lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6)

*Note on MONDO:* A MONDO identifier was not available in the retrieved sources.

## 1) Core pathophysiology

### 1.1 Primary mechanisms

#### A. Collagen II misfolding and intracellular retention
A common pathogenic class in COL2A1 disorders is **glycine substitution** in the triple-helical Gly–X–Y repeats, which disrupts helix stability and/or folding and can cause intracellular accumulation rather than secretion. Patient-derived cellular studies show **marked intracellular collagen II accumulation with absent extracellular collagen II deposition**, consistent with a secretion/trafficking failure driven by mutant procollagen. (marchionni2023clinicalandfunctional pages 3-4)

A major 2023 human stem-cell cartilage model directly demonstrates this mechanism in a hypochondrogenesis mutation context: iPSC-derived chondronoids carrying **COL2A1 p.G1113C** (heterozygous) show **reduced collagen II ECM** with **prominent intracellular collagen II aggregates**. (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6, lamande2023modelinghumanskeletal media 5b868ad2)

#### B. ER stress and unfolded protein response (UPR) engagement (variable across alleles)
Misfolded collagens can elicit ER stress and activate the three canonical UPR sensors **PERK**, **IRE1**, and **ATF6**, which initially attempt proteostatic recovery but can transition to apoptosis under chronic unresolved stress (e.g., via **ATF4→CHOP/DDIT3** and IRE1-linked pro-apoptotic signaling). (bateman2022collagenmisfoldingmutations pages 2-4)

For COL2A1/collagen II misfolding mutations, reported UPR-related signatures include upregulation of **BiP**/**GRP94**, **CHOP**, **eIF2α phosphorylation** (PERK arm), **ATF6** induction/activation, and **XBP1 splicing** (IRE1 arm), with apoptosis reported in severe contexts; however, the extent of canonical UPR activation can vary by allele and zygosity. (bateman2022collagenmisfoldingmutations pages 11-12)

A complementary review focused on cartilage pathophysiology notes that intracellular retention of misfolded mutant **COL2A1** in a mouse model is associated with distended rough ER and UPR signaling early in life, linking collagen II retention to ER stress mechanisms in chondrocytes. (hughes2017endoplasmicreticulumstress pages 3-5)

#### C. ECM fibril deficiency and disorganization
Even when some mutant collagen is secreted, collagen II can be insufficient or structurally abnormal, leading to **sparse, disorganized fibrils** and compromised cartilage matrix integrity. In the 2023 iPSC hypochondrogenesis model, TEM shows **reduced/disorganized collagen II fibrils** in mutant cartilage. (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6, lamande2023modelinghumanskeletal media 5b868ad2)

Patient-cell functional work similarly indicates broader ECM disruption: collagen II trafficking/assembly defects were accompanied by a **disorganized fibronectin network**, implying downstream ECM architectural consequences beyond collagen itself. (marchionni2023clinicalandfunctional pages 3-4)

### 1.2 Dysregulated molecular pathways and affected cellular processes

Key dysregulated processes supported by the retrieved evidence include:

- **Protein folding/proteostasis** in the secretory pathway (ER quality control, trafficking, degradation), with potential activation of UPR signaling branches. (bateman2022collagenmisfoldingmutations pages 2-4, bateman2022collagenmisfoldingmutations pages 11-12)
- **Collagen biosynthesis, post-translational processing, secretion, and fibril assembly**, leading to reduced functional collagen II in cartilage ECM. (marchionni2023clinicalandfunctional pages 3-4, lamande2023modelinghumanskeletal pages 7-9)
- **Chondrocyte differentiation and survival** (apoptosis in severe models; impaired chondrogenic differentiation in patient-derived cell studies). (okada2015modelingtypeii pages 2-4, marchionni2023clinicalandfunctional pages 3-4)
- **Growth plate cartilage organization and endochondral ossification**, as an emergent tissue-level failure when cartilage ECM is inadequate and/or chondrocytes are stressed/dysfunctional. (myllyharju2014extracellularmatrixand pages 1-2, okada2015modelingtypeii pages 2-4)

## 2) Key molecular players

### 2.1 Genes/proteins
- **COL2A1** (HGNC:2200): causal gene encoding type II procollagen (principal cartilage fibrillar collagen). Functional studies support that glycine substitutions can drive intracellular retention and secretion failure. (marchionni2023clinicalandfunctional pages 1-2, marchionni2023clinicalandfunctional pages 3-4, lamande2023modelinghumanskeletal pages 7-9)

- **UPR mediators (pathway-level):** PERK/EIF2AK3 → eIF2α phosphorylation → ATF4 → CHOP/DDIT3; IRE1/ERN1 → XBP1 splicing; ATF6 activation. These are mechanistically linked to proteostasis outcomes and apoptosis under unresolved ER stress in collagenopathies, including collagen II contexts where UPR markers have been observed. (bateman2022collagenmisfoldingmutations pages 2-4, bateman2022collagenmisfoldingmutations pages 11-12)

### 2.2 Chemical entities (metabolites/drugs/small molecules)
Evidence from COL2A1 disease modeling and ER-stress literature highlights several chemicals relevant to mechanism and experimental intervention:

- **Trimethylamine N-oxide (TMAO)** (chemical chaperone): In a COL2A1/type II collagenopathy iChon model, TMAO **increased extracellular type II collagen** and **partially decreased apoptosis**, consistent with proteostasis improvement; it also reduced an ER-stress marker (BiP) in the model. (okada2015modelingtypeii pages 10-12, okada2015modelingtypeii pages 17-18)

- **4-phenylbutyric acid (4-PBA)** (chemical chaperone/ER-stress modulator): Reported to reduce ER stress in chondrocyte ER-stress contexts and discussed as a potential therapeutic avenue for ER stress diseases involving type II collagen retention, though in vivo efficacy may vary by disease/model. (briggs2020newdevelopmentsin pages 5-6)

- **ISRIB** (integrated stress response inhibitor): Demonstrated to restore bone growth and suppress ATF4/CHOP translation in an ER-stress chondrodysplasia model (not COL2A1-specific), supporting feasibility of targeting translation/ISR pathways relevant to UPR-mediated pathology. (briggs2020newdevelopmentsin pages 5-6)

- **Ascorbic acid (vitamin C)**: In COL2A1 mutant iChon cells, ascorbic acid increased multiple ER-stress markers (BiP/GRP94/CHOP; phospho-eIF2α; cleaved ATF6) and reduced chondrogenic nodules, suggesting that forcing collagen biosynthesis/processing can worsen proteostatic load in some mutant contexts. (okada2015modelingtypeii pages 9-10)

- **Bafilomycin A1** and **MG132**: Used experimentally to probe degradation routes; bafilomycin A1 increased type II collagen levels in the iChon model, implicating lysosomal contribution to collagen clearance, whereas MG132 did not show the same effect in the described assay. (okada2015modelingtypeii pages 10-12)

### 2.3 Cell types
- **Chondrocytes** (CL:0000138) are the primary affected cell type; they are professional secretory cells, making them vulnerable to proteostasis disruption when ECM proteins misfold or accumulate. (briggs2020newdevelopmentsin pages 1-3)

### 2.4 Anatomical locations/tissues
- **Cartilage ECM** and **growth plate cartilage** (UBERON:0002384 cartilage; UBERON:0005868 growth plate cartilage) are principal sites of pathology, consistent with type II collagen’s dominant role in cartilage structure and endochondral ossification. (myllyharju2014extracellularmatrixand pages 1-2, lamande2023modelinghumanskeletal pages 5-6)

## 3) Biological processes (GO-oriented) disrupted (candidate GO annotations)
Based on the evidence, hypochondrogenesis can be annotated to disruption of:

- **Collagen fibril organization** (GO:0030199) and **collagen biosynthetic process** (GO:0032964), reflecting impaired production/assembly of collagen II fibrils. (lamande2023modelinghumanskeletal pages 7-9, marchionni2023clinicalandfunctional pages 3-4)
- **Protein folding** (GO:0006457), **response to ER stress** (GO:0034976), and **response to unfolded protein** (GO:0006986), reflecting intracellular retention/misfolding and UPR involvement. (bateman2022collagenmisfoldingmutations pages 2-4, bateman2022collagenmisfoldingmutations pages 11-12)
- **Apoptotic signaling pathway** (GO:0097190) in severe misfolding/ER stress contexts. (bateman2022collagenmisfoldingmutations pages 2-4, okada2015modelingtypeii pages 2-4)
- **Endochondral ossification** (GO:0001958) and **skeletal system development** (GO:0001501), reflecting downstream growth plate dysfunction. (myllyharju2014extracellularmatrixand pages 1-2, okada2015modelingtypeii pages 2-4)

## 4) Cellular components (GO CC) implicated
Key cellular compartments implicated by mechanistic evidence include:

- **Rough endoplasmic reticulum** (GO:0005791): site of procollagen folding/retention, ER distension, and UPR signaling. (hughes2017endoplasmicreticulumstress pages 3-5, okada2015modelingtypeii pages 2-4)
- **Golgi apparatus** (GO:0005794) / Golgi vesicular structures: patient-derived cellular evidence localizes accumulated collagen II to Golgi-associated vesicles in a COL2A1 glycine-substitution context, consistent with trafficking disruption. (marchionni2023clinicalandfunctional pages 3-4)
- **Collagen-containing extracellular matrix** (GO:0062023) / **extracellular matrix** (GO:0031012): site of collagen II fibril insufficiency and disorganization. (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6)

## 5) Disease progression (sequence of events)
A mechanistically supported disease sequence is:

1. **Initiating trigger:** heterozygous COL2A1 structural variant (often triple-helix glycine substitution) generates mutant procollagen II. (marchionni2023clinicalandfunctional pages 1-2, wu2025prenatalimagingof pages 6-7)
2. **Intracellular proteostasis defect:** delayed folding/misfolding causes intracellular accumulation/retention in the secretory pathway (ER and/or Golgi-associated compartments), with potential activation of ER stress/UPR signaling in some alleles. (marchionni2023clinicalandfunctional pages 3-4, bateman2022collagenmisfoldingmutations pages 11-12)
3. **ECM deficiency:** reduced secretion and/or secretion of dysfunctional collagen II yields a **sparse/disorganized collagen II matrix**. (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal media 5b868ad2)
4. **Cell and tissue dysfunction:** impaired chondrocyte differentiation and/or apoptosis and disorganized cartilage architecture disrupt **growth plate function** and **endochondral ossification**. (okada2015modelingtypeii pages 2-4, myllyharju2014extracellularmatrixand pages 1-2)
5. **Clinical manifestation:** severe skeletal dysplasia phenotype consistent with hypochondrogenesis/achondrogenesis spectrum (short limbs, vertebral and thoracic abnormalities, perinatal lethality in the severe end). (wu2025prenatalimagingof pages 6-7, myllyharju2014extracellularmatrixand pages 1-2)

## 6) Phenotypic manifestations and mechanistic links (HPO-oriented)
Representative phenotypes (illustrative HPO terms) include:

- **Short limbs** (e.g., HP:0002117) and severe short stature due to growth plate failure and impaired endochondral ossification. (myllyharju2014extracellularmatrixand pages 1-2, wu2025prenatalimagingof pages 6-7)
- **Platyspondyly** (HP:0000926) and vertebral anomalies due to abnormal cartilage templates and ECM defects. (wu2025prenatalimagingof pages 6-7)
- **Perinatal lethality** in severe COL2A1 continuum phenotypes (often via thoracic insufficiency/respiratory failure). (wu2025prenatalimagingof pages 6-7, myllyharju2014extracellularmatrixand pages 1-2)

## Recent developments and latest research (prioritizing 2023–2024)

### 2023: Human iPSC-derived developmental skeletal model directly modeling hypochondrogenesis
Lamandé et al. (PNAS, publication date May 2023) present a human iPSC-based platform that recapitulates cartilage maturation and mineralizing transitions and demonstrate disease modeling for hypochondrogenesis using a **COL2A1 p.G1113C** line. A key quantitative finding is a large increase in chondrocytes with intracellular collagen II aggregates (**58% mutant vs 7% control**) alongside reduced collagen II ECM and sparse/disorganized fibrils (Figure 4A–B). This represents a high-value, human genotype-accurate experimental system for mechanistic studies and therapeutic screening. URL: https://doi.org/10.1073/pnas.2211510120 (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6, lamande2023modelinghumanskeletal media 5b868ad2)

### 2023: Functional characterization of COL2A1 variant with cellular ECM readouts
Marchionni et al. (Bone Reports, publication date Dec 2023) provide patient-cell mechanistic evidence for a COL2A1 glycine substitution (p.Gly444Ser), reporting impaired chondrogenic differentiation, intracellular collagen II accumulation, lack of extracellular collagen II deposition, and ECM disorganization (fibronectin network). URL: https://doi.org/10.1016/j.bonr.2023.101728 (marchionni2023clinicalandfunctional pages 3-4)

### 2024: Real-world gene panel implementation and outcomes in skeletal dysplasia
MacCarrick et al. (Am J Med Genet A, publication date May 2024) report the largest cohort to date (n=5,011; Dec 2019–Apr 2022 testing window) evaluating multigene panel testing for skeletal dysplasia. The study’s diagnostic yield was **27.4%**, with care/treatment implications for **84.4%** of positive diagnoses, supporting broad deployment of molecular diagnostics in skeletal dysplasia workflows—including COL2A1 phenotypes that are difficult to resolve clinically given overlap across multiple disorders. URL: https://doi.org/10.1002/ajmg.a.63646 (maccarrick2024clinicalutilityof pages 1-2, maccarrick2024clinicalutilityof pages 2-3)

### 2024: Updated nosology and disease-group scale
A 2024 clinical overview of skeletal dysplasias highlights that the **2023 Nosology** includes **771 entries**, caused by variants in **552 genes**, organized into **41 groups**, emphasizing rapid expansion of genotype–phenotype mapping relevant to cartilage disorders. URL: https://doi.org/10.12956/tchd.1380641 (dasar2024overviewofskeletal pages 1-2)

## Current applications and real-world implementations

### Molecular diagnosis (panels, exome, and assay design)
- **Gene panels**: Large-cohort evidence indicates panels are widely used and yield clinically actionable results for a substantial fraction of suspected skeletal dysplasia cases (27.4% overall yield in 5,011 individuals). (maccarrick2024clinicalutilityof pages 1-2)
- **Handling large, multi-exon collagen genes**: Long-range PCR-based NGS (vLAS) is proposed to streamline analysis of large collagen genes such as **COL2A1 (54 exons; ~31.5 kb)**, covering entire genes with ~20 kb amplicons, supporting practical clinical implementation alternatives to exon-by-exon Sanger sequencing or capture-probe design. URL: https://doi.org/10.7759/cureus.50482 (niida2023streamlininggeneticdiagnosis pages 1-2)

### Prenatal evaluation
Although detailed prenatal-pathway statistics were limited in the retrieved 2023–2024 texts, current practice referenced in skeletal dysplasia genetic testing literature includes prenatal ultrasound suspicion followed by molecular testing (gene panels or exome) to distinguish overlapping lethal/nonlethal skeletal dysplasias. (maccarrick2024clinicalutilityof pages 2-3)

## Expert opinions and analysis (authoritative sources)

- Expert reviews emphasize that **ER stress/UPR is a plausible, druggable mechanism** in genetic cartilage diseases, but that the strength of evidence for canonical, cytotoxic UPR varies between collagen types and mutations; they argue that mechanistic studies must be performed in the relevant target cells (chondrocytes) and allele contexts. (bateman2022collagenmisfoldingmutations pages 2-4, bateman2022collagenmisfoldingmutations pages 11-12)

- Reviews focusing on cartilage ER stress describe chondrocyte ER stress as a **core disease mechanism** in subsets of genetic skeletal diseases and highlight experimental modulation by chemical chaperones and ISR inhibitors as emerging therapeutic strategies. (briggs2020newdevelopmentsin pages 1-3, briggs2020newdevelopmentsin pages 5-6)

## Relevant statistics and data (recent)

- **Skeletal dysplasia birth incidence (collective):** approximately **1 in 5,000 live births**; alternatively **2.4–4.5 per 10,000 live births**, estimated as ~**5% of all birth defects** (review-level epidemiology). (dasar2024overviewofskeletal pages 1-2)
- **Genetic nosology scale:** 2023 revision includes **771 entries**, **552 genes**, **41 groups**. (dasar2024overviewofskeletal pages 1-2)
- **Diagnostic yield (real-world U.S. panel testing):** **27.4% molecular diagnostic yield** among **5,011** individuals; **84.4%** of molecular diagnoses had implications for specific care/treatment decisions. (maccarrick2024clinicalutilityof pages 1-2)
- **Quantitative cellular pathology in a 2023 hypochondrogenesis model:** intracellular collagen II aggregates in **58%** of mutant chondrocytes vs **7%** in isogenic control. (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal media 5b868ad2)

## Evidence-backed mechanistic summary table
The following table consolidates mechanism-to-ontology mappings and key evidence items.

| Mechanistic level | Key elements (ontology IDs where possible) | Evidence summary | Key citations | Year / journal / URL |
|---|---|---|---|---|
| Gene/protein | **COL2A1** (HGNC:2200); collagen type II alpha 1 chain; triple-helical Gly-X-Y domain; HP:0002117 short limb, HP:0002808 platyspondyly | Hypochondrogenesis is a **type II collagenopathy** most commonly caused by heterozygous **COL2A1 glycine substitutions** or other structural variants that disrupt triple-helix folding, causing delayed folding, overmodification, intracellular retention, and dominant-negative loss of functional collagen II. Recent patient-cell work also showed absent extracellular collagen II with intracellular accumulation for a glycine substitution. | (marchionni2023clinicalandfunctional pages 1-2, marchionni2023clinicalandfunctional pages 3-4, okada2015modelingtypeii pages 2-4, aljuid2026col2a1mutationsand pages 8-9, maccarrick2024clinicalutilityof pages 2-3) | 2023, *Bone Reports*, https://doi.org/10.1016/j.bonr.2023.101728; 2015, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddu444 |
| Pathway/process | GO:0032964 collagen biosynthetic process; GO:0030199 collagen fibril organization; GO:0006457 protein folding; GO:0034976 response to endoplasmic reticulum stress; GO:0006986 response to unfolded protein; rough ER (GO:0005791) | Misfolded mutant procollagen II is retained within the **rough ER**, with ER distension/storage defects and impaired secretion. In COL2A1 disease models, retained collagen II shows slow folding and accumulation compatible with proteostasis failure. | (okada2015modelingtypeii pages 2-4, aljuid2026col2a1mutationsand pages 8-9, lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6) | 2015, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddu444; 2023, *PNAS*, https://doi.org/10.1073/pnas.2211510120 |
| Pathway/process | UPR branches: **PERK(EIF2AK3)**, **IRE1(ERN1)-XBP1**, **ATF6**; GO:0036498 IRE1-mediated unfolded protein response; GO:0036499 PERK-mediated unfolded protein response; GO:0036500 ATF6-mediated unfolded protein response; CHOP/**DDIT3**-linked apoptosis GO:0097190 apoptotic signaling pathway | Reviews and model systems indicate that collagen misfolding can activate all three canonical **UPR** arms. In collagen II disorders, reported markers include **BiP/GRP94**, **ATF6**, **eIF2α phosphorylation**, **XBP1 splicing**, **ATF4**, and **CHOP**; chronic unresolved signaling is linked to apoptosis. Evidence is variable across COL2A1 alleles, but severe models support UPR involvement. | (bateman2022collagenmisfoldingmutations pages 2-4, hughes2017endoplasmicreticulumstress pages 3-5, bateman2022collagenmisfoldingmutations pages 11-12, briggs2020newdevelopmentsin pages 1-3, bateman2022collagenmisfoldingmutations pages 1-2) | 2022, *Connective Tissue Research*, https://doi.org/10.1080/03008207.2022.2036735; 2020, *F1000Research*, https://doi.org/10.12688/f1000research.22275.1 |
| Cell type / organelle | Chondrocyte (CL:0000138); proliferating/hypertrophic growth plate chondrocytes; rough endoplasmic reticulum (GO:0005791); Golgi apparatus (GO:0005794) | The principal affected cell is the **chondrocyte**, a professional secretory cell highly sensitive to ER proteostasis disruption. Patient-derived cells with a COL2A1 glycine variant showed intracellular collagen II accumulation with **Golgi-associated vesicular localization** and impaired chondrogenic differentiation. | (marchionni2023clinicalandfunctional pages 3-4, briggs2020newdevelopmentsin pages 1-3) | 2023, *Bone Reports*, https://doi.org/10.1016/j.bonr.2023.101728; 2020, *F1000Research*, https://doi.org/10.12688/f1000research.22275.1 |
| ECM / tissue architecture | Extracellular matrix (GO:0031012); collagen-containing extracellular matrix (GO:0062023); type II collagen fibrils; UBERON:0002384 cartilage; UBERON:0005868 growth plate cartilage | A core downstream lesion is **reduced extracellular collagen II** with a **sparse/disorganized fibrillar network**. Recent human organoid/iPSC modeling of hypochondrogenesis showed reduced ECM collagen II staining, intracellular aggregates, and TEM evidence of reduced/disorganized fibrils, closely matching patient and mouse observations. | (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6, okada2015modelingtypeii pages 2-4, myllyharju2014extracellularmatrixand pages 1-2) | 2023, *PNAS*, https://doi.org/10.1073/pnas.2211510120; 2015, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddu444 |
| Tissue/organ development | GO:0061036 positive regulation of cartilage development; GO:0001501 skeletal system development; GO:0001958 endochondral ossification; UBERON:0005868 growth plate; HP:0002750 abnormal chondrocyte morphology | Defective collagen II secretion and matrix assembly disrupt **growth plate organization** and **endochondral ossification**, producing shortened limbs, vertebral abnormalities, and lethal or near-lethal skeletal dysplasia. Mouse and human stem-cell models link ER retention/matrix deficiency to altered differentiation, sparse cartilage matrix, and failed skeletal maturation. | (okada2015modelingtypeii pages 2-4, myllyharju2014extracellularmatrixand pages 1-2, lamande2023modelinghumanskeletal pages 5-6) | 2015, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddu444; 2014, *Current Osteoporosis Reports*, https://doi.org/10.1007/s11914-014-0232-1; 2023, *PNAS*, https://doi.org/10.1073/pnas.2211510120 |
| Disease progression | Sequence: COL2A1 structural variant → procollagen II misfolding/slow folding → intracellular retention ± UPR/ER stress → reduced secretion/ECM deficiency → altered chondrocyte differentiation/apoptosis → growth plate failure → skeletal phenotype | Across the evidence base, disease progression is best understood as a combined **intracellular proteostasis defect** plus **extracellular matrix insufficiency**. Both mechanisms likely interact: retained mutant collagen burdens the secretory pathway, while deficient/disorganized matrix feeds back on chondrocyte maturation and tissue architecture. | (okada2015modelingtypeii pages 2-4, aljuid2026col2a1mutationsand pages 6-7, aljuid2026col2a1mutationsand pages 8-9, bateman2022collagenmisfoldingmutations pages 2-4) | 2015, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddu444; 2022, *Connective Tissue Research*, https://doi.org/10.1080/03008207.2022.2036735 |
| Experimental model / real-world implementation | iPSC-derived chondrogenic models; organoid/chondronoid systems; prenatal exome sequencing; gene panels | **Okada 2015** established patient iPSC models showing apoptosis, ER stress markers, and partial rescue of collagen II secretion/chondrocyte survival by a chemical chaperone. **Lamandé 2023** modeled hypochondrogenesis with a **COL2A1 p.G1113C** mutant line and quantified intracellular collagen II aggregates in **58% (210/365)** of mutant cells vs **7% (56/860)** of control cells, with reduced ECM collagen II and disorganized fibrils. Clinically, 2023–2024 studies support prenatal exome/gene-panel diagnosis for COL2A1 skeletal dysplasias. | (okada2015modelingtypeii pages 2-4, lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6, maccarrick2024clinicalutilityof pages 1-2) | 2015, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddu444; 2023, *PNAS*, https://doi.org/10.1073/pnas.2211510120; 2024, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.63646 |


*Table: This table maps the main molecular, cellular, and tissue-level mechanisms implicated in hypochondrogenesis, centered on COL2A1 dysfunction. It also highlights recent disease-model evidence, including 2023 iPSC/organoid findings and clinically relevant diagnostic applications.*

## Key evidence item (visual)
Figure evidence from the 2023 iPSC hypochondrogenesis model (COL2A1 p.G1113C) shows reduced collagen II ECM, intracellular collagen II aggregates (with quantification), and TEM evidence of sparse/disorganized fibrils. (lamande2023modelinghumanskeletal media 5b868ad2)

## Evidence items list (PMIDs where available)
The retrieved full-text excerpts did not consistently include PMIDs; therefore, PMIDs cannot be reliably provided without additional database lookups. The following evidence items (with DOI URLs and publication timing) support the mechanistic claims above:

- Lamandé SR et al. *PNAS* (May 2023): https://doi.org/10.1073/pnas.2211510120 (lamande2023modelinghumanskeletal pages 7-9, lamande2023modelinghumanskeletal pages 5-6, lamande2023modelinghumanskeletal media 5b868ad2)
- Marchionni E et al. *Bone Reports* (Dec 2023): https://doi.org/10.1016/j.bonr.2023.101728 (marchionni2023clinicalandfunctional pages 1-2, marchionni2023clinicalandfunctional pages 3-4)
- MacCarrick G et al. *Am J Med Genet A* (May 2024): https://doi.org/10.1002/ajmg.a.63646 (maccarrick2024clinicalutilityof pages 1-2, maccarrick2024clinicalutilityof pages 2-3)
- Niida Y et al. *Cureus* (Dec 2023): https://doi.org/10.7759/cureus.50482 (niida2023streamlininggeneticdiagnosis pages 1-2)
- Bateman JF et al. *Connective Tissue Research* (Feb 2022): https://doi.org/10.1080/03008207.2022.2036735 (bateman2022collagenmisfoldingmutations pages 2-4, bateman2022collagenmisfoldingmutations pages 11-12)
- Briggs MD et al. *F1000Research* (Apr 2020): https://doi.org/10.12688/f1000research.22275.1 (briggs2020newdevelopmentsin pages 1-3, briggs2020newdevelopmentsin pages 5-6)
- Okada M et al. *Human Molecular Genetics* (Jan 2015): https://doi.org/10.1093/hmg/ddu444 (okada2015modelingtypeii pages 2-4, okada2015modelingtypeii pages 10-12)
- Myllyharju J. *Current Osteoporosis Reports* (Sep 2014): https://doi.org/10.1007/s11914-014-0232-1 (myllyharju2014extracellularmatrixand pages 1-2)



References

1. (wu2025prenatalimagingof pages 6-7): Yi-Cheng Wu, Chih-Yao Chen, Guan-Yeu Chen, Ching-Hua Hsiao, Woei-Chyn Chu, and Jack Yu-Jen Huang. Prenatal imaging of micrognathia, micromelia, and fetal hydrops leading to the diagnosis of achondrogenesis type ii with a col2a1 missense mutation. International Journal of Molecular Sciences, 26:11472, Nov 2025. URL: https://doi.org/10.3390/ijms262311472, doi:10.3390/ijms262311472. This article has 0 citations.

2. (myllyharju2014extracellularmatrixand pages 1-2): Johanna Myllyharju. Extracellular matrix and developing growth plate. Current Osteoporosis Reports, 12:439-445, Sep 2014. URL: https://doi.org/10.1007/s11914-014-0232-1, doi:10.1007/s11914-014-0232-1. This article has 59 citations and is from a peer-reviewed journal.

3. (okada2015modelingtypeii pages 2-4): Minoru Okada, Shiro Ikegawa, Miho Morioka, Akihiro Yamashita, Atsushi Saito, Hideaki Sawai, Jun Murotsuki, Hirofumi Ohashi, Toshio Okamoto, Gen Nishimura, Kazunori Imaizumi, and Noriyuki Tsumaki. Modeling type ii collagenopathy skeletal dysplasia by directed conversion and induced pluripotent stem cells. Human molecular genetics, 24 2:299-313, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu444, doi:10.1093/hmg/ddu444. This article has 49 citations and is from a domain leading peer-reviewed journal.

4. (lamande2023modelinghumanskeletal pages 7-9): Shireen R. Lamandé, Elizabeth S. Ng, Trevor L. Cameron, Louise H. W. Kung, Lisa Sampurno, Lynn Rowley, Jinia Lilianty, Yudha Nur Patria, Tayla Stenta, Eric Hanssen, Katrina M. Bell, Ritika Saxena, Kathryn S. Stok, Edouard G. Stanley, Andrew G. Elefanty, and John F. Bateman. Modeling human skeletal development using human pluripotent stem cells. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2211510120, doi:10.1073/pnas.2211510120. This article has 72 citations and is from a highest quality peer-reviewed journal.

5. (lamande2023modelinghumanskeletal pages 5-6): Shireen R. Lamandé, Elizabeth S. Ng, Trevor L. Cameron, Louise H. W. Kung, Lisa Sampurno, Lynn Rowley, Jinia Lilianty, Yudha Nur Patria, Tayla Stenta, Eric Hanssen, Katrina M. Bell, Ritika Saxena, Kathryn S. Stok, Edouard G. Stanley, Andrew G. Elefanty, and John F. Bateman. Modeling human skeletal development using human pluripotent stem cells. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2211510120, doi:10.1073/pnas.2211510120. This article has 72 citations and is from a highest quality peer-reviewed journal.

6. (marchionni2023clinicalandfunctional pages 3-4): Enrica Marchionni, Maria Rosaria D'Apice, Viviana Lupo, Giovanna Lattanzi, Elisabetta Mattioli, Gina Lisignoli, Elena Gabusi, Gerardo Pepe, Manuela Helmer Citterich, Elena Campione, Anna Maria Nardone, Paola Spitalieri, Noemi Pucci, Dario Cocciadiferro, Eliseo Picchi, Francesco Garaci, Antonio Novelli, and Giuseppe Novelli. Clinical and functional characterization of col2a1 p.gly444ser variant: from a fetal phenotype to a previously undisclosed postnatal phenotype. Bone Reports, 19:101728, Dec 2023. URL: https://doi.org/10.1016/j.bonr.2023.101728, doi:10.1016/j.bonr.2023.101728. This article has 1 citations and is from a peer-reviewed journal.

7. (lamande2023modelinghumanskeletal media 5b868ad2): Shireen R. Lamandé, Elizabeth S. Ng, Trevor L. Cameron, Louise H. W. Kung, Lisa Sampurno, Lynn Rowley, Jinia Lilianty, Yudha Nur Patria, Tayla Stenta, Eric Hanssen, Katrina M. Bell, Ritika Saxena, Kathryn S. Stok, Edouard G. Stanley, Andrew G. Elefanty, and John F. Bateman. Modeling human skeletal development using human pluripotent stem cells. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2211510120, doi:10.1073/pnas.2211510120. This article has 72 citations and is from a highest quality peer-reviewed journal.

8. (bateman2022collagenmisfoldingmutations pages 2-4): John F. Bateman, Matthew D. Shoulders, and Shireen R. Lamandé. Collagen misfolding mutations: the contribution of the unfolded protein response to the molecular pathology. Connective Tissue Research, 63:210-227, Feb 2022. URL: https://doi.org/10.1080/03008207.2022.2036735, doi:10.1080/03008207.2022.2036735. This article has 32 citations and is from a peer-reviewed journal.

9. (bateman2022collagenmisfoldingmutations pages 11-12): John F. Bateman, Matthew D. Shoulders, and Shireen R. Lamandé. Collagen misfolding mutations: the contribution of the unfolded protein response to the molecular pathology. Connective Tissue Research, 63:210-227, Feb 2022. URL: https://doi.org/10.1080/03008207.2022.2036735, doi:10.1080/03008207.2022.2036735. This article has 32 citations and is from a peer-reviewed journal.

10. (hughes2017endoplasmicreticulumstress pages 3-5): Alexandria Hughes, Alexandra Oxford, Ken Tawara, Cheryl Jorcyk, and Julia Oxford. Endoplasmic reticulum stress and unfolded protein response in cartilage pathophysiology; contributing factors to apoptosis and osteoarthritis. International Journal of Molecular Sciences, 18:665, Mar 2017. URL: https://doi.org/10.3390/ijms18030665, doi:10.3390/ijms18030665. This article has 118 citations.

11. (marchionni2023clinicalandfunctional pages 1-2): Enrica Marchionni, Maria Rosaria D'Apice, Viviana Lupo, Giovanna Lattanzi, Elisabetta Mattioli, Gina Lisignoli, Elena Gabusi, Gerardo Pepe, Manuela Helmer Citterich, Elena Campione, Anna Maria Nardone, Paola Spitalieri, Noemi Pucci, Dario Cocciadiferro, Eliseo Picchi, Francesco Garaci, Antonio Novelli, and Giuseppe Novelli. Clinical and functional characterization of col2a1 p.gly444ser variant: from a fetal phenotype to a previously undisclosed postnatal phenotype. Bone Reports, 19:101728, Dec 2023. URL: https://doi.org/10.1016/j.bonr.2023.101728, doi:10.1016/j.bonr.2023.101728. This article has 1 citations and is from a peer-reviewed journal.

12. (okada2015modelingtypeii pages 10-12): Minoru Okada, Shiro Ikegawa, Miho Morioka, Akihiro Yamashita, Atsushi Saito, Hideaki Sawai, Jun Murotsuki, Hirofumi Ohashi, Toshio Okamoto, Gen Nishimura, Kazunori Imaizumi, and Noriyuki Tsumaki. Modeling type ii collagenopathy skeletal dysplasia by directed conversion and induced pluripotent stem cells. Human molecular genetics, 24 2:299-313, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu444, doi:10.1093/hmg/ddu444. This article has 49 citations and is from a domain leading peer-reviewed journal.

13. (okada2015modelingtypeii pages 17-18): Minoru Okada, Shiro Ikegawa, Miho Morioka, Akihiro Yamashita, Atsushi Saito, Hideaki Sawai, Jun Murotsuki, Hirofumi Ohashi, Toshio Okamoto, Gen Nishimura, Kazunori Imaizumi, and Noriyuki Tsumaki. Modeling type ii collagenopathy skeletal dysplasia by directed conversion and induced pluripotent stem cells. Human molecular genetics, 24 2:299-313, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu444, doi:10.1093/hmg/ddu444. This article has 49 citations and is from a domain leading peer-reviewed journal.

14. (briggs2020newdevelopmentsin pages 5-6): Michael D. Briggs, Ella P. Dennis, Helen F. Dietmar, and Katarzyna A. Pirog. New developments in chondrocyte er stress and related diseases. F1000Research, 9:290, Apr 2020. URL: https://doi.org/10.12688/f1000research.22275.1, doi:10.12688/f1000research.22275.1. This article has 36 citations and is from a peer-reviewed journal.

15. (okada2015modelingtypeii pages 9-10): Minoru Okada, Shiro Ikegawa, Miho Morioka, Akihiro Yamashita, Atsushi Saito, Hideaki Sawai, Jun Murotsuki, Hirofumi Ohashi, Toshio Okamoto, Gen Nishimura, Kazunori Imaizumi, and Noriyuki Tsumaki. Modeling type ii collagenopathy skeletal dysplasia by directed conversion and induced pluripotent stem cells. Human molecular genetics, 24 2:299-313, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu444, doi:10.1093/hmg/ddu444. This article has 49 citations and is from a domain leading peer-reviewed journal.

16. (briggs2020newdevelopmentsin pages 1-3): Michael D. Briggs, Ella P. Dennis, Helen F. Dietmar, and Katarzyna A. Pirog. New developments in chondrocyte er stress and related diseases. F1000Research, 9:290, Apr 2020. URL: https://doi.org/10.12688/f1000research.22275.1, doi:10.12688/f1000research.22275.1. This article has 36 citations and is from a peer-reviewed journal.

17. (maccarrick2024clinicalutilityof pages 1-2): Gretchen MacCarrick, Swaroop Aradhya, Mitch Bailey, Dorna Chu, Abigail Hunt, Emanuela Izzo, Deborah Krakow, William Mackenzie, Sarah Poll, Cathleen Raggio, Renée Shediac, Klane K. White, Heather M. McLaughlin, and Guillermo Seratti. Clinical utility of comprehensive gene panel testing for common and rare causes of skeletal dysplasia and other skeletal disorders: results from the largest cohort to date. American Journal of Medical Genetics Part A, May 2024. URL: https://doi.org/10.1002/ajmg.a.63646, doi:10.1002/ajmg.a.63646. This article has 3 citations.

18. (maccarrick2024clinicalutilityof pages 2-3): Gretchen MacCarrick, Swaroop Aradhya, Mitch Bailey, Dorna Chu, Abigail Hunt, Emanuela Izzo, Deborah Krakow, William Mackenzie, Sarah Poll, Cathleen Raggio, Renée Shediac, Klane K. White, Heather M. McLaughlin, and Guillermo Seratti. Clinical utility of comprehensive gene panel testing for common and rare causes of skeletal dysplasia and other skeletal disorders: results from the largest cohort to date. American Journal of Medical Genetics Part A, May 2024. URL: https://doi.org/10.1002/ajmg.a.63646, doi:10.1002/ajmg.a.63646. This article has 3 citations.

19. (dasar2024overviewofskeletal pages 1-2): Tuğba DAŞAR and Esra KILIÇ. Overview of skeletal dysplasias. Turkish Journal of Pediatric Disease, pages 1-11, Jan 2024. URL: https://doi.org/10.12956/tchd.1380641, doi:10.12956/tchd.1380641. This article has 1 citations.

20. (niida2023streamlininggeneticdiagnosis pages 1-2): Yo Niida, Sumihito Togi, and Hiroki Ura. Streamlining genetic diagnosis with long-range polymerase chain reaction (pcr)-based next-generation sequencing for type i and type ii collagenopathies. Cureus, Dec 2023. URL: https://doi.org/10.7759/cureus.50482, doi:10.7759/cureus.50482. This article has 3 citations.

21. (aljuid2026col2a1mutationsand pages 8-9): Latifa Mohammed Aljuid, Dareen Alyousfi, Manal Hosawi, and Ayman Z Elsamanoudy. Col2a1 mutations and type ii collagenopathies: molecular mechanisms and ipsc-based modeling of cartilage disorders. Archives of Stem Cell and Therapy, 6:6, Feb 2026. URL: https://doi.org/10.46439/stemcell.6.026, doi:10.46439/stemcell.6.026. This article has 0 citations.

22. (bateman2022collagenmisfoldingmutations pages 1-2): John F. Bateman, Matthew D. Shoulders, and Shireen R. Lamandé. Collagen misfolding mutations: the contribution of the unfolded protein response to the molecular pathology. Connective Tissue Research, 63:210-227, Feb 2022. URL: https://doi.org/10.1080/03008207.2022.2036735, doi:10.1080/03008207.2022.2036735. This article has 32 citations and is from a peer-reviewed journal.

23. (aljuid2026col2a1mutationsand pages 6-7): Latifa Mohammed Aljuid, Dareen Alyousfi, Manal Hosawi, and Ayman Z Elsamanoudy. Col2a1 mutations and type ii collagenopathies: molecular mechanisms and ipsc-based modeling of cartilage disorders. Archives of Stem Cell and Therapy, 6:6, Feb 2026. URL: https://doi.org/10.46439/stemcell.6.026, doi:10.46439/stemcell.6.026. This article has 0 citations.