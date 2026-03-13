---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-10T20:33:20.396095'
end_time: '2026-03-10T20:50:42.171217'
duration_seconds: 1041.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Hypercholesterolemia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Familial Hypercholesterolemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Familial Hypercholesterolemia**.
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
- **Disease Name:** Familial Hypercholesterolemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Familial Hypercholesterolemia**.
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


# Familial Hypercholesterolemia (FH) Pathophysiology Research Report (Mendelian)

**Target disease:** Familial hypercholesterolemia (FH)

**Disease identifiers:** MONDO:0007750 / “hypercholesterolemia, familial, 1” and related clinical entity “familial hypercholesterolemia” (EFO_0004911). Homozygous FH: MONDO:0018328. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)

## 1) Key concepts and definitions (current understanding)

Familial hypercholesterolemia is a mostly autosomal-dominant disorder of LDL-cholesterol (LDL-C) metabolism caused by pathogenic variants that reduce hepatic LDL clearance (primarily via LDL receptor–mediated uptake), leading to high LDL-C from early life and markedly increased atherosclerotic cardiovascular disease (ASCVD) risk. (abifadel2023geneticandmolecular pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4)

**HeFH vs HoFH:** FH severity broadly reflects gene dosage and residual LDL receptor pathway activity: heterozygous FH (HeFH) results from one pathogenic allele, while homozygous/bi-allelic FH (HoFH) results from two pathogenic alleles (true homozygotes or compound heterozygotes; or bi-allelic variants across loci). HoFH is characterized by “markedly elevated levels of low-density lipoprotein cholesterol (LDL-C) from conception” with accelerated ASCVD and early mortality if untreated. (cuchel20232023updateon pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4)

**Diagnostic concepts (DLCN):** The Dutch Lipid Clinic Network criteria assign points using family history, clinical signs, and LDL-C strata (e.g., LDL-C >8.5 mmol/L / ≥325 mg/dL gives the highest LDL-C score), plus molecular confirmation (8 points for a functional mutation in LDLR/APOB/PCSK9). (fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2)

## 2) Core pathophysiology (molecular and cellular mechanisms)

### 2.1 Primary pathophysiological mechanism: impaired LDL particle clearance

The unifying mechanism is reduced clearance of apoB-containing LDL particles, resulting in chronic elevation of circulating LDL-C. The principal molecular defect is disruption of **LDLR pathway function**—including receptor synthesis/trafficking, LDL binding, clathrin-mediated endocytosis, and receptor recycling. (taranto2023geneticheterogeneityof pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)

**LDLR functional classes:** LDLR variants are commonly conceptualized as five mechanistic classes: absence of receptor, maturation/transport defects, impaired LDL binding, impaired endocytosis, and defective recycling. (taranto2023geneticheterogeneityof pages 2-4, suryawanshi2023familialhypercholesterolemiaa pages 2-4)

### 2.2 Dysregulated pathways

**(a) Receptor-mediated endocytosis & endosomal sorting/lysosomal degradation:**
- PCSK9 is a secreted factor that binds LDLR and shifts LDLR fate away from recycling toward intracellular degradation. In a primary mechanistic study, the PCSK9–LDLR complex is described as “internalized via clathrin-mediated endocytosis and then routed to lysosomes.” (wang2012molecularcharacterizationof pages 1-2)
- Qian et al. showed that “Secreted PCSK9 mediated cell surface LDLR degradation” and that PCSK9 endocytosis shows endosomal–lysosomal localization; knockdown of ARH/LDLRAP1 reduced PCSK9 endocytosis, supporting LDLR–ARH-mediated internalization as a route to receptor loss. (qian2007secretedpcsk9downregulates pages 1-2)

**(b) LDL retention, modification, and inflammatory atherogenesis:**
Chronic LDL exposure increases deposition of LDL in the subendothelial arterial intima (especially at disturbed-flow sites), where LDL is oxidatively modified to oxLDL and triggers endothelial activation, monocyte recruitment, foam cell formation, and plaque progression. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, thangasparan2024unravellingthemechanisms pages 3-5)

### 2.3 Cellular processes affected

1. **Endothelial activation/dysfunction** → chemokine release and leukocyte adhesion/migration. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, thangasparan2024unravellingthemechanisms pages 3-5)
2. **Monocyte-to-macrophage differentiation** in intima and uptake of modified lipoproteins → foam cell formation. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, thangasparan2024unravellingthemechanisms pages 3-5)
3. **Smooth muscle cell (SMC) migration/phenotypic switching** and lipid uptake; SMCs contribute substantially to foam cell populations. (jin2024mechanismsmodulatingfoam pages 1-2, francis2023thegreatlyunderrepresented pages 1-2)
4. **Sustained inflammation** with cytokine secretion, necrotic core formation, fibrous cap remodeling, and potential plaque rupture. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, galindo2023lipidladenfoamcells pages 1-3)

## 3) Key molecular players (genes/proteins, cells, anatomy, chemicals)

| Gene (HGNC) | Role / Inheritance | Molecular Defect / Mechanism | Key Mechanistic Quote | Citation |
| :--- | :--- | :--- | :--- | :--- |
| **LDLR** | Main causative gene; Autosomal Dominant (AD) | Dysfunction classified into 5 classes: defects in synthesis, ER-to-Golgi transport, LDL ligand binding, internalization, or recycling. | "LDLR defects occur at multiple steps: post-translational transport... impaired LDL binding... reduced clathrin-coated pit–mediated endocytosis, and abnormal LDLR recycling" | Fularski et al., 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5) |
| **APOB** | Ligand for LDLR; Autosomal Dominant (AD) | Missense mutations (e.g., R3500Q) reduce the affinity of the ApoB protein on LDL particles for the LDLR, preventing uptake. | "pathogenic variants that impair ApoB binding to LDLR, notably in exons 26 and 29" | Taranto & Fortunato, 2023 (taranto2023geneticheterogeneityof pages 2-4) |
| **PCSK9** | Regulator of LDLR stability; Autosomal Dominant (AD) | Gain-of-function variants increase LDLR degradation. PCSK9 binds cell-surface LDLR and directs the complex to lysosomes instead of recycling. | "[PCSK9] binds the extracellular domain of the LDLR... internalized via clathrin-mediated endocytosis and then routed to lysosomes via a mechanism that does not require ubiquitination" | Wang et al., 2012 (wang2012molecularcharacterizationof pages 1-2) |
| **LDLRAP1** (ARH) | Endocytic adaptor; Autosomal Recessive (AR) | Loss of function prevents the LDLR-LDL complex from clustering in clathrin-coated pits for internalization. | "ARH is required for endocytosis of the LDLR–LDL complex via its interaction with clathrin" | Maxwell et al., 2005 (maxwell2005overexpressionofpcsk9 pages 1-2) |
| **APOE** | Ligand (rare cause); Autosomal Dominant (AD) | Rare variants (e.g., p.Leu167del) result in an FH-like phenotype (FH phenocopy) via impaired clearance. | "a specific APOE variant was described as causative of FH, contributing to increase FH genetic heterogeneity" | Taranto & Fortunato, 2023 (taranto2023geneticheterogeneityof pages 2-4) |


*Table: This table summarizes the primary genes associated with Familial Hypercholesterolemia, their inheritance patterns, specific molecular defects, and direct mechanistic evidence from primary literature.*

### 3.1 High-confidence causal genes/proteins

- **LDLR (HGNC:6547)**: impaired LDL binding/endocytosis/recycling, reducing LDL uptake. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, taranto2023geneticheterogeneityof pages 2-4)
- **APOB (HGNC:603)**: LDL ligand; variants reduce LDLR binding. (taranto2023geneticheterogeneityof pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)
- **PCSK9 (HGNC:20001)**: binds LDLR and promotes lysosomal routing/degradation. (wang2012molecularcharacterizationof pages 1-2, qian2007secretedpcsk9downregulates pages 1-2)
- **LDLRAP1/ARH (HGNC:18640)**: adaptor for clathrin-mediated internalization of LDLR–LDL complexes; its deficiency causes autosomal recessive hypercholesterolemia. (maxwell2005overexpressionofpcsk9 pages 1-2, canuel2013proproteinconvertasesubtilisinkexin pages 1-2)
- **APOE (HGNC:613)**: rare causative variants/heterogeneity contributor. (taranto2023geneticheterogeneityof pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4)

### 3.2 Key cell types (mechanistic involvement)

- **Hepatocytes**: site of LDLR-mediated LDL clearance and key therapeutic target for LDLR upregulation and PCSK9 inhibition. (qian2007secretedpcsk9downregulates pages 1-2, suryawanshi2023familialhypercholesterolemiaa pages 2-4)
- **Endothelial cells**: barrier/transcytosis and inflammatory activation. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, thangasparan2024unravellingthemechanisms pages 3-5)
- **Monocyte-derived macrophages**: major foam cell source via scavenger receptor uptake of oxLDL. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, thangasparan2024unravellingthemechanisms pages 3-5)
- **Vascular smooth muscle cells (VSMCs/SMCs)**: major contributor to intimal thickening and foam cell pool; recent syntheses note “more than half of the foam cells present in atherosclerotic lesions are of SMC origin.” (jin2024mechanismsmodulatingfoam pages 1-2, francis2023thegreatlyunderrepresented pages 1-2)

### 3.3 Anatomical locations

- **Liver** (LDLR-mediated clearance). (suryawanshi2023familialhypercholesterolemiaa pages 2-4)
- **Arterial intima / subendothelial space** (LDL deposition/oxLDL formation/foam cells). (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, jin2024mechanismsmodulatingfoam pages 1-2)
- **Aortic valve/aorta** (notably in HoFH: aortic disease/stenosis). (cuchel20232023updateon pages 1-2)
- **Tendons/skin/cornea** (xanthomas, corneal arcus). (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, cuchel20232023updateon pages 1-2)

### 3.4 Chemical entities / therapeutically relevant molecules

- **LDL-C**: dominant causal exposure in FH atherogenesis. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7)
- **Oxidized LDL (oxLDL)**: key modified particle driving inflammation and foam cell formation. (thangasparan2024unravellingthemechanisms pages 3-5, duan2023attenuatinglipidmetabolism pages 1-2)
- **Therapies:** statins, ezetimibe, PCSK9 inhibitors, inclisiran, bempedoic acid, evinacumab, lomitapide, LDL apheresis. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9, dingman2024evinacumabmechanismof pages 2-4, suryawanshi2023familialhypercholesterolemiaa pages 8-9)

## 4) Biological processes and cellular components (GO-oriented)

A knowledge-base oriented mapping is provided below.

| Category | Entity / Term | Ontology ID | Context / Source |
| :--- | :--- | :--- | :--- |
| **Disease Identifiers** | Familial Hypercholesterolemia | MONDO:0007750 | (taranto2023geneticheterogeneityof pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5) |
| | Homozygous Familial Hypercholesterolemia | MONDO:0018328 | (cuchel20232023updateon pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4) |
| **Key Genes** | LDLR (Low Density Lipoprotein Receptor) | HGNC:6547 | (taranto2023geneticheterogeneityof pages 2-4, wang2012molecularcharacterizationof pages 1-2) |
| | APOB (Apolipoprotein B) | HGNC:603 | (taranto2023geneticheterogeneityof pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5) |
| | PCSK9 (Proprotein Convertase Subtilisin/Kexin Type 9) | HGNC:20001 | (taranto2023geneticheterogeneityof pages 2-4, qian2007secretedpcsk9downregulates pages 1-2) |
| | LDLRAP1 (LDLR Adaptor Protein 1) | HGNC:18640 | (taranto2023geneticheterogeneityof pages 2-4, canuel2013proproteinconvertasesubtilisinkexin pages 1-2) |
| | APOE (Apolipoprotein E) | HGNC:613 | (taranto2023geneticheterogeneityof pages 2-4, abifadel2023geneticandmolecular pages 1-2) |
| **Biological Processes** | Receptor-mediated endocytosis | GO:0006898 | (qian2007secretedpcsk9downregulates pages 1-2, wang2012molecularcharacterizationof pages 1-2) |
| | Low-density lipoprotein particle clearance | GO:0034383 | (taranto2023geneticheterogeneityof pages 2-4, suryawanshi2023familialhypercholesterolemiaa pages 2-4) |
| | Cholesterol homeostasis | GO:0042632 | (srivastava2023areviewof pages 1-2) |
| **Cellular Components** | Clathrin-coated pit | GO:0005905 | (canuel2013proproteinconvertasesubtilisinkexin pages 1-2, wang2012molecularcharacterizationof pages 1-2) |
| | Plasma membrane | GO:0005886 | (wang2012molecularcharacterizationof pages 1-2) |
| | Lysosome | GO:0005764 | (jang2020cyclaseassociatedprotein1 pages 14-15, wang2012molecularcharacterizationof pages 1-2) |
| **Phenotypes** | Hypercholesterolemia | HP:0003124 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, abifadel2023geneticandmolecular pages 1-2) |
| | Tendon xanthoma | HP:0001388 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, abifadel2023geneticandmolecular pages 1-2) |
| | Corneal arcus | HP:0001023 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, abifadel2023geneticandmolecular pages 1-2) |
| | Premature coronary artery atherosclerosis | HP:0004416 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, cuchel20232023updateon pages 1-2) |
| **Cell Types** | Hepatocyte | CL:0000182 | (suryawanshi2023familialhypercholesterolemiaa pages 2-4, qian2007secretedpcsk9downregulates pages 1-2) |
| | Macrophage (Foam cell precursor) | CL:0000235 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, thangasparan2024unravellingthemechanisms pages 3-5) |
| | Smooth muscle cell (Foam cell source) | CL:0000192 | (jin2024mechanismsmodulatingfoam pages 1-2, francis2023thegreatlyunderrepresented pages 1-2) |
| | Endothelial cell | CL:0000115 | (thangasparan2024unravellingthemechanisms pages 3-5, galindo2023lipidladenfoamcells pages 1-3) |
| **Anatomy** | Liver | UBERON:0002107 | (suryawanshi2023familialhypercholesterolemiaa pages 2-4) |
| | Tunica intima (Arterial intima) | UBERON:0002523 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, jin2024mechanismsmodulatingfoam pages 1-2) |
| | Tendon | UBERON:0000043 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5) |
| **Chemicals / Drugs** | Low-density lipoprotein cholesterol | CHEBI:47774 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, suryawanshi2023familialhypercholesterolemiaa pages 2-4) |
| | Statins (HMG-CoA reductase inhibitors) | CHEBI:87631 | (srivastava2023areviewof pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9) |
| | Ezetimibe | CHEBI:63553 | (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9) |
| | Evinacumab | [monoclonal antibody] | (dingman2024evinacumabmechanismof pages 2-4, beliard2024evinacumabandcardiovascular pages 1-3) |
| | Inclisiran | [siRNA] | (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9) |


*Table: This table maps key concepts in Familial Hypercholesterolemia (FH) to standard biomedical ontologies (MONDO, HGNC, GO, HP, CL, UBERON, CHEBI) to support knowledge graph integration.*

Key disrupted processes include **receptor-mediated endocytosis** (LDLR internalization), **LDL particle clearance**, and **cholesterol homeostasis**, while key cellular compartments include **clathrin-coated pits**, **endosomes**, and **lysosomes** that govern receptor/ligand trafficking and degradation. (wang2012molecularcharacterizationof pages 1-2, canuel2013proproteinconvertasesubtilisinkexin pages 1-2)

## 5) Disease progression: sequence of events from trigger to clinical disease

### Stage 1: Genetic lesion → impaired LDL clearance from birth
Pathogenic variants in LDLR/APOB/PCSK9/LDLRAP1 (and rarer loci) reduce LDL uptake or increase receptor degradation, causing lifelong LDL-C elevation (“from conception” in HoFH). (cuchel20232023updateon pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4)

### Stage 2: Cumulative LDL exposure → arterial LDL deposition and oxidation
At disturbed-flow regions (bifurcations/curvatures), endothelial barrier dysfunction facilitates LDL deposition in the subendothelial space; chronic high LDL-C increases intimal LDL accumulation. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7)

### Stage 3: Endothelial activation → immune cell recruitment
Endothelial damage promotes chemoattractant release, monocyte recruitment, and entry into the intima. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, thangasparan2024unravellingthemechanisms pages 3-5)

### Stage 4: Foam cell formation and plaque growth
In the intima, monocytes differentiate into macrophages that generate oxidants, producing oxLDL; “Ox-LDL-C… is then absorbed via macrophages… [leading to] foam cells,” which amplify inflammation and drive lesion growth. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7)

Parallel SMC mechanisms are increasingly recognized: diffuse intimal thickening (pre–fatty streak) is enriched in lipid-loaded SMCs and proteoglycans, and SMCs can constitute the majority of foam cells in advanced plaques. (jin2024mechanismsmodulatingfoam pages 1-2, francis2023thegreatlyunderrepresented pages 1-2)

### Stage 5: Complications
Progressive plaque burden yields premature coronary heart disease, and in HoFH, frequent aortic disease/calcific aortic stenosis and early cardiovascular events. (cuchel20232023updateon pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)

## 6) Phenotypic manifestations (clinical phenotypes and mechanistic links)

Key phenotypes reflect (i) systemic LDL-C excess and (ii) tissue lipid deposition and atherosclerosis:
- **Hypercholesterolemia (HP:0003124)** from impaired clearance. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)
- **Tendon/skin xanthomas** from cholesterol deposition; correlate with severe LDL burden. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, cuchel20232023updateon pages 1-2)
- **Corneal arcus**. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)
- **Premature ASCVD** (coronary, carotid, peripheral), with vascular inflammation and foam cell biology as key mediators. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7, galindo2023lipidladenfoamcells pages 1-3)

## 7) Recent developments and latest research (prioritizing 2023–2024)

### 7.1 Updated disease architecture and genetic heterogeneity
Recent syntheses emphasize expanded genetic heterogeneity (rare APOE causation; LDLRAP1 recessive FH; phenocopies and modifiers) and phenotype variability even for identical genotypes. (taranto2023geneticheterogeneityof pages 2-4, abifadel2023geneticandmolecular pages 1-2)

### 7.2 Increasing emphasis on SMC biology and extracellular matrix in early atherogenesis
2023–2024 reviews highlight that SMCs and their proteoglycans dominate early human intimal thickening and contribute heavily to foam cell pools. This refines purely macrophage-centric models and suggests new mechanisms/targets centered on LDL retention and SMC phenotypic switching. (jin2024mechanismsmodulatingfoam pages 1-2, francis2023thegreatlyunderrepresented pages 1-2)

### 7.3 LDLR-independent LDL-C lowering for HoFH (ANGPTL3 inhibition)
Evinacumab (anti-ANGPTL3) is emphasized as an LDLR-independent therapy that can reduce LDL-C by ~50% at 15 mg/kg IV every 4 weeks across adult/adolescent/pediatric HoFH, addressing the unmet need in patients with minimal LDLR function. (dingman2024evinacumabmechanismof pages 2-4, wiegman2024evinacumabforpediatric pages 1-2)

## 8) Current applications and real-world implementations

### 8.1 Screening and clinical management
Consensus/guideline sources emphasize screening and multi-pronged lipid-lowering therapy initiated at diagnosis for HoFH, ideally via multidisciplinary care. (cuchel20232023updateon pages 1-2, cuchel20232023updateon media 7c520ae7)

### 8.2 Guideline-driven lipid-lowering strategy (implementation)
A practical approach summarized in recent FH review/guideline synthesis: high-intensity statin plus ezetimibe early; then PCSK9 inhibitors for those not reaching LDL-C goals; the ACC (2022) is reported to consider inclisiran or bempedoic acid if further LDL-C reduction is needed; apheresis remains an option for refractory cases under specialist care. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9)

## 9) Statistics and recent data (2023–2024)

| Topic | Key Data / Statistics | Notes / Real-World Implications | Source |
| :--- | :--- | :--- | :--- |
| **Prevalence** | HeFH: ~1:250–300<br>HoFH: ~1:250,000–360,000 | HoFH estimates vary by region (e.g., ~1:300,000). Higher prevalence in founder populations. | Fularski et al., 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2); Taranto et al., 2023 (taranto2023geneticheterogeneityof pages 2-4) |
| **Diagnostic Thresholds (DLCN)** | LDL-C >8.5 mmol/L (>325 mg/dL): 8 pts<br>LDL-C 6.5–8.4 mmol/L (251–325 mg/dL): 5 pts | Based on Dutch Lipid Clinic Network criteria. Definite FH score >8. | Fularski et al., 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2) |
| **CAD Risk** | Odds Ratio: 10–20x higher vs non-FH | Highlights the critical need for early diagnosis and aggressive lipid lowering. | Harada-Shiba et al., 2023 (haradashiba2023guidelinesforthe pages 1-2) |
| **Treatment Targets (Adult)** | High Risk: LDL-C <1.8 mmol/L (<70 mg/dL)<br>Very High Risk: LDL-C <1.4 mmol/L (<55 mg/dL) | Both targets also require ≥50% reduction from baseline. Based on ESC/EAS guidelines. | Fularski et al., 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9) |
| **Pediatric Targets** | LDL-C <3.5 mmol/L (<135 mg/dL) | Recommended target for children >10 years old initiating statins. | Fularski et al., 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9) |
| **Evinacumab (Adult HoFH)** | LDL-C reduction: 56% (sustained ~3.5 yrs)<br>CV Events: 0% vs 24% in controls | First long-term real-world data showing sustained efficacy and improved CV event-free survival. | Béliard et al., 2024 (beliard2024evinacumabandcardiovascular pages 1-3) |
| **Evinacumab (Pediatric HoFH)** | LDL-C reduction: -48.3% at week 24 | Efficacy demonstrated in children aged 5–11 years with LDL-C >130 mg/dL despite optimized therapy. | Wiegman et al., 2024 (wiegman2024evinacumabforpediatric pages 1-2) |


*Table: A summary of recent epidemiological data, diagnostic thresholds, guideline targets, and therapeutic outcomes for Familial Hypercholesterolemia from 2023-2024 literature.*

Selected highlights:
- **Prevalence:** HeFH ~1:250–300; HoFH ~1:250,000–360,000. (fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2)
- **FH CAD risk:** odds ratio reported ~10–20× compared with non-FH. (haradashiba2023guidelinesforthe pages 1-2)
- **Evinacumab real-world long-term cohort (HoFH):** LDL-C reduction 56% at 6 months sustained over median 3.5 years; 0 events on evinacumab vs 24% experiencing events in matched controls (4 years). (beliard2024evinacumabandcardiovascular pages 1-3)

## 10) Expert opinions / authoritative analysis

A central expert consensus is that **lifetime LDL-C exposure** drives premature ASCVD in FH and mandates early, intensive, combination therapy. In HoFH, the EAS consensus emphasizes immediate “multi-prong lipid lowering therapy starting at diagnosis,” including apheresis, oral agents, and biologics, and underscores underdiagnosis/undertreatment and inequities across countries. (cuchel20232023updateon pages 1-2, cuchel20232023updateon media 7c520ae7)

## 11) Evidence items (mechanistic statements; PMID where available in retrieved text)

### PCSK9 → LDLR lysosomal degradation (primary mechanistic studies)
- Qian et al., *J Lipid Res* (2007-07). DOI: https://doi.org/10.1194/jlr.M700071-JLR200. Key mechanistic statements include “Secreted PCSK9 mediated cell surface LDLR degradation…” and support for LDLR–ARH-mediated endocytosis and endosomal–lysosomal localization. **PMID not shown in retrieved excerpt**. (qian2007secretedpcsk9downregulates pages 1-2)
- Wang et al., *J Lipid Res* (2012-09). DOI: https://doi.org/10.1194/jlr.M028563. Key mechanistic statement: PCSK9–LDLR complex “internalized via clathrin-mediated endocytosis and then routed to lysosomes.” **PMID not shown in retrieved excerpt**. (wang2012molecularcharacterizationof pages 1-2)
- Canuel et al., *PLoS ONE* (2013-05). DOI: https://doi.org/10.1371/journal.pone.0064145. Summarizes ARH binding to LDLR NPVY motif and clathrin/AP-2 for recruitment into clathrin-coated pits; notes endosomes/lysosomes as the degradation destination. **PMID not shown in retrieved excerpt**. (canuel2013proproteinconvertasesubtilisinkexin pages 1-2)

### LDL oxidation and foam cell biology (recent mechanistic reviews)
- Thangasparan et al., *IJMS* (2024-12). DOI: https://doi.org/10.3390/ijms252413292. Details oxLDL-driven endothelial dysfunction, monocyte recruitment, scavenger receptor uptake, foam cell formation, and inflammatory perpetuation. (thangasparan2024unravellingthemechanisms pages 3-5, thangasparan2024unravellingthemechanisms pages 2-3)
- Duan et al., *Frontiers in Pharmacology* (2023-03). DOI: https://doi.org/10.3389/fphar.2023.1161657. Describes ROS-driven LDL oxidation and oxLDL effects on endothelium and smooth muscle migration/proliferation. (duan2023attenuatinglipidmetabolism pages 1-2)

### Note on PMID coverage
Several retrieved primary papers did not display PMIDs in the extracted text chunks; however, some PMIDs are explicitly visible in a secondary mechanistic excerpt list (e.g., Fisher et al. **PMID: 17493938**; Saavedra et al. **PMID: 23105118**), indicating where PubMed identifiers exist even if not consistently shown in all excerpts. (poirier2016traffickingdynamicsof pages 22-23, poirier2016traffickingdynamicsof pages 24-24)

## 12) Visual evidence

The EAS 2023 HoFH consensus graphical abstract summarizes genetics (LDLR/APOB/PCSK9/LDLRAP1), clinical features, and the multi-pronged treatment framework for HoFH, serving as a high-level schematic of disease pathophysiology and management. (cuchel20232023updateon media 7c520ae7)



References

1. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 25 citations.

2. (abifadel2023geneticandmolecular pages 1-2): Marianne Abifadel and Catherine Boileau. Genetic and molecular architecture of familial hypercholesterolemia. Journal of Internal Medicine, 293:144-165, Oct 2023. URL: https://doi.org/10.1111/joim.13577, doi:10.1111/joim.13577. This article has 153 citations and is from a domain leading peer-reviewed journal.

3. (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 25 citations.

4. (cuchel20232023updateon pages 1-2): Marina Cuchel, Frederick J Raal, Robert A Hegele, Khalid Al-Rasadi, Marcello Arca, Maurizio Averna, Eric Bruckert, Tomas Freiberger, Daniel Gaudet, Mariko Harada-Shiba, Lisa C Hudgins, Meral Kayikcioglu, Luis Masana, Klaus G Parhofer, Jeanine E Roeters van Lennep, Raul D Santos, Erik S G Stroes, Gerald F Watts, Albert Wiegman, Jane K Stock, Lale S Tokgözoğlu, Alberico L Catapano, and Kausik K Ray. 2023 update on european atherosclerosis society consensus statement on homozygous familial hypercholesterolaemia: new treatments and clinical guidance. European Heart Journal, 44:2277-2291, May 2023. URL: https://doi.org/10.1093/eurheartj/ehad197, doi:10.1093/eurheartj/ehad197. This article has 345 citations and is from a highest quality peer-reviewed journal.

5. (fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 25 citations.

6. (taranto2023geneticheterogeneityof pages 2-4): Maria Donata Di Taranto and Giuliana Fortunato. Genetic heterogeneity of familial hypercholesterolemia: repercussions for molecular diagnosis. International Journal of Molecular Sciences, 24:3224, Feb 2023. URL: https://doi.org/10.3390/ijms24043224, doi:10.3390/ijms24043224. This article has 47 citations.

7. (suryawanshi2023familialhypercholesterolemiaa pages 2-4): Yasha N Suryawanshi and Rupesh A Warbhe. Familial hypercholesterolemia: a literature review of the pathophysiology and current and novel treatments. Cureus, Nov 2023. URL: https://doi.org/10.7759/cureus.49121, doi:10.7759/cureus.49121. This article has 17 citations.

8. (wang2012molecularcharacterizationof pages 1-2): Yan Wang, Yongcheng Huang, Helen H. Hobbs, and Jonathan C. Cohen. Molecular characterization of proprotein convertase subtilisin/kexin type 9-mediated degradation of the ldlr. Journal of Lipid Research, 53:1932-1943, Sep 2012. URL: https://doi.org/10.1194/jlr.m028563, doi:10.1194/jlr.m028563. This article has 141 citations and is from a peer-reviewed journal.

9. (qian2007secretedpcsk9downregulates pages 1-2): Yue-Wei Qian, Robert J. Schmidt, Youyan Zhang, Shaoyou Chu, Aimin Lin, He Wang, Xiliang Wang, Thomas P. Beyer, William R. Bensch, Weiming Li, Mariam E. Ehsani, Deshun Lu, Robert J. Konrad, Patrick I. Eacho, David E. Moller, Sotirios K. Karathanasis, and Guoqing Cao. Secreted pcsk9 downregulates low density lipoprotein receptor through receptor-mediated endocytosis published, jlr papers in press, april 20, 2007. Journal of Lipid Research, 48:1488-1498, Jul 2007. URL: https://doi.org/10.1194/jlr.m700071-jlr200, doi:10.1194/jlr.m700071-jlr200. This article has 308 citations and is from a peer-reviewed journal.

10. (fularski2024unveilingfamilialhypercholesterolemia—review pages 5-7): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 25 citations.

11. (thangasparan2024unravellingthemechanisms pages 3-5): Sahsikala Thangasparan, Yusof Kamisah, Azizah Ugusman, Nur Najmi Mohamad Anuar, and Nurul ‘Izzah Ibrahim. Unravelling the mechanisms of oxidised low-density lipoprotein in cardiovascular health: current evidence from in vitro and in vivo studies. International Journal of Molecular Sciences, 25:13292, Dec 2024. URL: https://doi.org/10.3390/ijms252413292, doi:10.3390/ijms252413292. This article has 24 citations.

12. (jin2024mechanismsmodulatingfoam pages 1-2): Hong Jin, Robert C. Bauer, La Chica, MT Lhoëst, La Chica Lhoëst, Martinez, Claudi Garcia, Polishchuk Piñero Vilades Guerra Sanz Rotllan Escolà-Gil Benitez-Amaro, Llorente-Cortés. This, M. T. La, Chica Lhoëst, A. Martínez, L. Claudí, E. Garcia, A. Benitez-Amaro, A. Polishchuk, J. Pinero, D. Viladés, J. M. Guerra, F. Sanz, N. Rotllan, J. Escolà-Gil, and V. Llorente-Cortés. Mechanisms modulating foam cell formation in the arterial intima: exploring new therapeutic opportunities in atherosclerosis. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1381520, doi:10.3389/fcvm.2024.1381520. This article has 17 citations and is from a peer-reviewed journal.

13. (francis2023thegreatlyunderrepresented pages 1-2): Gordon A. Francis. The greatly under-represented role of smooth muscle cells in atherosclerosis. Current Atherosclerosis Reports, 25:741-749, Sep 2023. URL: https://doi.org/10.1007/s11883-023-01145-8, doi:10.1007/s11883-023-01145-8. This article has 35 citations and is from a peer-reviewed journal.

14. (galindo2023lipidladenfoamcells pages 1-3): Cristi L Galindo, Saifur R Khan, Xiangyu Zhang, Yu-Sheng Yeh, Ziyang Liu, and Babak Razani. Lipid-laden foam cells in the pathology of atherosclerosis: shedding light on new therapeutic targets. Expert Opinion on Therapeutic Targets, 27:1231-1245, Nov 2023. URL: https://doi.org/10.1080/14728222.2023.2288272, doi:10.1080/14728222.2023.2288272. This article has 47 citations and is from a peer-reviewed journal.

15. (maxwell2005overexpressionofpcsk9 pages 1-2): Kara N. Maxwell, Edward A. Fisher, and Jan L. Breslow. Overexpression of pcsk9 accelerates the degradation of the ldlr in a post-endoplasmic reticulum compartment. Proceedings of the National Academy of Sciences of the United States of America, 102 6:2069-74, Feb 2005. URL: https://doi.org/10.1073/pnas.0409736102, doi:10.1073/pnas.0409736102. This article has 550 citations and is from a highest quality peer-reviewed journal.

16. (canuel2013proproteinconvertasesubtilisinkexin pages 1-2): Maryssa Canuel, Xiaowei Sun, Marie-Claude Asselin, Eustache Paramithiotis, Annik Prat, and Nabil G. Seidah. Proprotein convertase subtilisin/kexin type 9 (pcsk9) can mediate degradation of the low density lipoprotein receptor-related protein 1 (lrp-1). PLoS ONE, 8:e64145, May 2013. URL: https://doi.org/10.1371/journal.pone.0064145, doi:10.1371/journal.pone.0064145. This article has 276 citations and is from a peer-reviewed journal.

17. (duan2023attenuatinglipidmetabolism pages 1-2): Huxinyue Duan, Pan Song, Ruolan Li, Hong-guang Su, and Lisha He. Attenuating lipid metabolism in atherosclerosis: the potential role of anti-oxidative effects on low-density lipoprotein of herbal medicines. Frontiers in Pharmacology, Mar 2023. URL: https://doi.org/10.3389/fphar.2023.1161657, doi:10.3389/fphar.2023.1161657. This article has 34 citations.

18. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 25 citations.

19. (dingman2024evinacumabmechanismof pages 2-4): Robert Dingman, Sébastien Bihorel, Viktoria Gusarova, Jeanne Mendell, and Robert Pordy. Evinacumab: mechanism of action, clinical, and translational science. Clinical and Translational Science, Jun 2024. URL: https://doi.org/10.1111/cts.13836, doi:10.1111/cts.13836. This article has 17 citations.

20. (suryawanshi2023familialhypercholesterolemiaa pages 8-9): Yasha N Suryawanshi and Rupesh A Warbhe. Familial hypercholesterolemia: a literature review of the pathophysiology and current and novel treatments. Cureus, Nov 2023. URL: https://doi.org/10.7759/cureus.49121, doi:10.7759/cureus.49121. This article has 17 citations.

21. (srivastava2023areviewof pages 1-2): Rai Ajit K. Srivastava. A review of progress on targeting ldl receptor-dependent and -independent pathways for the treatment of hypercholesterolemia, a major risk factor of ascvd. Cells, 12:1648, Jun 2023. URL: https://doi.org/10.3390/cells12121648, doi:10.3390/cells12121648. This article has 42 citations.

22. (jang2020cyclaseassociatedprotein1 pages 14-15): Hyun-Duk Jang, Sang Eun Lee, Jimin Yang, Hyun-Chae Lee, Dasom Shin, Hwan Lee, Jaewon Lee, Sooryeonhwa Jin, Soungchan Kim, Seung Ji Lee, Jihye You, Hyun-Woo Park, Ky-Youb Nam, Sang-Hak Lee, Sahng Wook Park, Jin-Soo Kim, Sang-Yeob Kim, Yoo-Wook Kwon, Soo Heon Kwak, Han-Mo Yang, and Hyo-Soo Kim. Cyclase-associated protein 1 is a binding partner of proprotein convertase subtilisin/kexin type-9 and is required for the degradation of low-density lipoprotein receptors by proprotein convertase subtilisin/kexin type-9. European Heart Journal, 41:239-252, Aug 2020. URL: https://doi.org/10.1093/eurheartj/ehz566, doi:10.1093/eurheartj/ehz566. This article has 112 citations and is from a highest quality peer-reviewed journal.

23. (beliard2024evinacumabandcardiovascular pages 1-3): Sophie Béliard, Samir Saheb, Stéphanie Litzler-Renault, Alexandre Vimont, René Valero, Éric Bruckert, Michel Farnier, and Antonio Gallo. Evinacumab and cardiovascular outcome in patients with homozygous familial hypercholesterolemia. Arteriosclerosis, Thrombosis, and Vascular Biology, 44:1447-1454, Jun 2024. URL: https://doi.org/10.1161/atvbaha.123.320609, doi:10.1161/atvbaha.123.320609. This article has 25 citations and is from a domain leading peer-reviewed journal.

24. (wiegman2024evinacumabforpediatric pages 1-2): MD PhD Albert Wiegman, MD PhD Albert Wiegman, MD Susanne Greber-Platzer, PharmD Shazia Ali, MD M. Doortje Reijman, MD Eliot A Brinton, MD Min-Ji Charng, PhD Shubha Srinivasan, PhD Carissa Baker-Smith Md, Mph Seth Baum Md, MD Julie A. Brothers, MD Jacob Hartz, M. P. M. Md, MD Jeanne Mendell, Mph Sébastien Bihorel PhD, P. Banerjee, PhD Richard T. George, MD Boaz Hirshberg, and MD Robert Pordy. Evinacumab for pediatric patients with homozygous familial hypercholesterolemia. Circulation, 149:343-353, Jan 2024. URL: https://doi.org/10.1161/circulationaha.123.065529, doi:10.1161/circulationaha.123.065529. This article has 98 citations and is from a highest quality peer-reviewed journal.

25. (cuchel20232023updateon media 7c520ae7): Marina Cuchel, Frederick J Raal, Robert A Hegele, Khalid Al-Rasadi, Marcello Arca, Maurizio Averna, Eric Bruckert, Tomas Freiberger, Daniel Gaudet, Mariko Harada-Shiba, Lisa C Hudgins, Meral Kayikcioglu, Luis Masana, Klaus G Parhofer, Jeanine E Roeters van Lennep, Raul D Santos, Erik S G Stroes, Gerald F Watts, Albert Wiegman, Jane K Stock, Lale S Tokgözoğlu, Alberico L Catapano, and Kausik K Ray. 2023 update on european atherosclerosis society consensus statement on homozygous familial hypercholesterolaemia: new treatments and clinical guidance. European Heart Journal, 44:2277-2291, May 2023. URL: https://doi.org/10.1093/eurheartj/ehad197, doi:10.1093/eurheartj/ehad197. This article has 345 citations and is from a highest quality peer-reviewed journal.

26. (haradashiba2023guidelinesforthe pages 1-2): Mariko Harada-Shiba, Hidenori Arai, Hirotoshi Ohmura, Hiroaki Okazaki, Daisuke Sugiyama, Hayato Tada, Kazushige Dobashi, Kota Matsuki, Tetsuo Minamino, Shizuya Yamashita, and Koutaro Yokote. Guidelines for the diagnosis and treatment of adult familial hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis, 30:558-586, May 2023. URL: https://doi.org/10.5551/jat.cr005, doi:10.5551/jat.cr005. This article has 100 citations and is from a peer-reviewed journal.

27. (thangasparan2024unravellingthemechanisms pages 2-3): Sahsikala Thangasparan, Yusof Kamisah, Azizah Ugusman, Nur Najmi Mohamad Anuar, and Nurul ‘Izzah Ibrahim. Unravelling the mechanisms of oxidised low-density lipoprotein in cardiovascular health: current evidence from in vitro and in vivo studies. International Journal of Molecular Sciences, 25:13292, Dec 2024. URL: https://doi.org/10.3390/ijms252413292, doi:10.3390/ijms252413292. This article has 24 citations.

28. (poirier2016traffickingdynamicsof pages 22-23): Steve Poirier, Hocine Ait Hamouda, Louis Villeneuve, Annie Demers, and Gaétan Mayer. Trafficking dynamics of pcsk9-induced ldlr degradation: focus on human pcsk9 mutations and c-terminal domain. PLoS ONE, 11:e0157230, Jun 2016. URL: https://doi.org/10.1371/journal.pone.0157230, doi:10.1371/journal.pone.0157230. This article has 51 citations and is from a peer-reviewed journal.

29. (poirier2016traffickingdynamicsof pages 24-24): Steve Poirier, Hocine Ait Hamouda, Louis Villeneuve, Annie Demers, and Gaétan Mayer. Trafficking dynamics of pcsk9-induced ldlr degradation: focus on human pcsk9 mutations and c-terminal domain. PLoS ONE, 11:e0157230, Jun 2016. URL: https://doi.org/10.1371/journal.pone.0157230, doi:10.1371/journal.pone.0157230. This article has 51 citations and is from a peer-reviewed journal.