---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-02T22:40:26.395002'
end_time: '2026-04-02T22:48:35.269690'
duration_seconds: 488.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Opsismodysplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Opsismodysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Opsismodysplasia**.
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
- **Disease Name:** Opsismodysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Opsismodysplasia**.
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


## Comprehensive Research Report: Opsismodysplasia (OPSMD)

### 0. Disease identifiers and overview
**Opsismodysplasia** is a rare Mendelian skeletal dysplasia characterized by delayed skeletal maturation and severe abnormalities of endochondral bone growth. An authoritative recent review describes opsismodysplasia as a skeletal dysplasia “**primarily characterized by the delayed ossification of maturing bones**.” (muller2024thefunctionalroles pages 14-15)

- **MONDO disease ID:** **MONDO:0009785** (Open Targets disease entity; retrieved via Open Targets association for OPSMD–INPPL1). (below2013wholegenomeanalysisreveals pages 5-7)
- **Inheritance:** Autosomal recessive (biallelic pathogenic variants). (below2013wholegenomeanalysisreveals pages 5-7, celine2013exomesequencingidentifies pages 1-2)
- **Primary causal gene:** **INPPL1** (HGNC:6091), encoding **SHIP2** (Src homology 2 domain-containing inositol 5-phosphatase 2). (below2013wholegenomeanalysisreveals pages 5-7, celine2013exomesequencingidentifies pages 1-2)

### 1. Key concepts and definitions (current understanding)

#### 1.1 Core molecular definition
INPPL1/SHIP2 is a **phosphoinositide 5-phosphatase** that acts within the PI3K signaling network by turning over phosphatidylinositol lipids. One report summarizes SHIP2 as dephosphorylating the “lipid second messenger phosphoinositol (3,4,5)P3,” consistent with its canonical role in terminating or reshaping PI3K signaling outputs. (feist2016novelcompoundheterozygous pages 3-4)

In the discovery-era clinical genetics literature, INPPL1 is placed in the PI3K lipid-signaling axis: PI3K produces **PtdIns(3,4,5)P3**, which can be converted by 5-phosphatases (including SHIP2) to **PtdIns(3,4)P2**. (celine2013exomesequencingidentifies pages 4-4)

#### 1.2 Pathophysiologic definition at the tissue level
Opsismodysplasia is best conceptualized as a disorder of **growth plate architecture and endochondral ossification**.

Growth plate histopathology in opsismodysplasia demonstrates:
- Loss of normal proliferative-zone organization (columnar arrangement)
- Reduction of the hypertrophic zone and fewer hypertrophic chondrocytes

These features were explicitly reported in the initial AJHG cohort, indicating that the molecular defect produces a characteristic **cellular disorganization of the growth plate** that plausibly explains delayed epiphyseal ossification and skeletal shortening. (celine2013exomesequencingidentifies pages 1-2)

### 2. Core pathophysiology

#### 2.1 Primary mechanisms
**Primary pathophysiological mechanism:** biallelic INPPL1 loss-of-function (or destabilizing) variants lead to dysregulated phosphoinositide metabolism and signaling, producing **growth plate disorganization**, impaired chondrocyte maturation, and delayed endochondral ossification.

Evidence supporting a loss-of-function mechanism includes mutation spectrum and protein loss:
- In one AJHG series, most variants were truncating or splice-site, with missense variants clustering in the **catalytic 5-phosphatase domain**, consistent with disrupted enzymatic function. (celine2013exomesequencingidentifies pages 4-4, celine2013exomesequencingidentifies pages 1-2)
- A fetal opsismodysplasia family showed **no detectable SHIP2 protein** in affected amniocytes, providing direct protein-level support for functional loss. (feist2016novelcompoundheterozygous pages 3-4, feist2016novelcompoundheterozygous media 56a554cb)

#### 2.2 Dysregulated pathways
**(a) Phosphoinositide metabolism / PI3K signaling**
- INPPL1/SHIP2 regulates PIP species (e.g., turnover of PtdIns(3,4,5)P3 and production of PtdIns(3,4)P2), which are second messengers organizing signaling and membrane–cytoskeleton processes. (celine2013exomesequencingidentifies pages 4-4, feist2016novelcompoundheterozygous pages 3-4)
- A 2024 review provides functional context: SHIP2 activation reduces plasma membrane PtdIns(3,4,5)P3 and thereby **inhibits AKT signaling**, supporting a mechanistic link to PI3K–AKT output modulation. (muller2024thefunctionalroles pages 14-15)

**(b) PI(3,4)P2-centered signaling as a mechanistic emphasis**
A mechanistic review highlighted that phenotypes in catalytically inactive SHIP2 models were attributed more to the lack of **PI(3,4)P2** than to simplistic “hyperactive PI3K–Akt signaling,” suggesting that loss of specific phosphoinositide species (and their binding partners) may be central to developmental phenotypes. (edimo2014ship2signalingin pages 3-5)

**(c) Developmental growth-factor signaling (FGF) connections (model-organism evidence)**
Zebrafish Ship2 knockdown perturbs outputs of **FGF signaling** (reported as dorsal fate expansion in early embryogenesis), supporting the plausibility that SHIP2-dependent phosphoinositide changes can rewire growth-factor pathway responses during development. (celine2013exomesequencingidentifies pages 4-6, edimo2014ship2signalingin pages 3-5)

#### 2.3 Cellular processes affected
Key cellular processes implicated by human pathology and SHIP2 biology include:
- **Chondrocyte proliferation/organization** (loss of columnar organization in proliferative zone) (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2)
- **Chondrocyte hypertrophy/differentiation** (reduced hypertrophic zone, fewer hypertrophic chondrocytes) (celine2013exomesequencingidentifies pages 1-2)
- **Cell expansion/size regulation and tissue mechanics** (recent zebrafish evidence—see below) (voigt2024aconservedregulation pages 1-3)

### 3. Key molecular players

#### 3.1 Genes/proteins
- **INPPL1 (SHIP2)** is the established causal gene/protein. (below2013wholegenomeanalysisreveals pages 5-7, celine2013exomesequencingidentifies pages 1-2)
- Reported disease-associated SHIP2 variants listed in a 2024 review include **R401W, P659S, W688C, F722I** (illustrating variant distribution beyond truncations). (muller2024thefunctionalroles pages 14-15)

**Statistics (genetic contribution):** In a cohort analyzed by whole-genome methods, INPPL1 mutations explained **7/12 kindreds (58%)** and **5/10 simplex cases (50%)**, supporting genetic heterogeneity but also highlighting INPPL1 as a major contributor among clinically diagnosed cases. (below2013wholegenomeanalysisreveals pages 5-7)

#### 3.2 Chemical entities (metabolites and small molecules)
**Endogenous phosphoinositides**
- **Phosphatidylinositol 3,4,5-trisphosphate (PtdIns(3,4,5)P3)**—substrate/regulated lipid messenger in SHIP2 pathway context. (celine2013exomesequencingidentifies pages 4-4, feist2016novelcompoundheterozygous pages 3-4)
- **Phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4)P2)**—product emphasized as mechanistically important in SHIP2-deficiency phenotypes. (edimo2014ship2signalingin pages 3-5)

**Research/therapeutic probes (not established OPSMD therapies)**
A 2024 review describes **SHIP2-selective inhibition (AS1949490)** as increasing insulin-induced AKT phosphorylation and improving glycemic phenotypes in diabetic mouse models, reflecting active translational pharmacology around SHIP2. These compounds are best viewed as **mechanistic tools** and potential future repurposing leads rather than current opsismodysplasia therapies. (muller2024thefunctionalroles pages 14-15)

#### 3.3 Cell types
The disease-relevant cell types are growth plate chondrocytes:
- **Proliferative chondrocytes** (loss of columnar arrangement) (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2)
- **Hypertrophic chondrocytes** (reduced hypertrophic zone) (celine2013exomesequencingidentifies pages 1-2)

#### 3.4 Anatomical locations / tissues
Primary tissues involved:
- **Growth plate cartilage** (histologic disorganization) (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2)
- **Epiphyses (delayed ossification), vertebrae (platyspondyly), pelvis/acetabulum, long bones** (radiographic manifestations) (below2013wholegenomeanalysisreveals pages 5-7, li2014opsismodysplasiaresultingfrom pages 1-3)

### 4. Biological processes disrupted (GO-oriented)
Evidence-supported GO-relevant processes include:
- **Endochondral ossification** (delayed epiphyseal ossification; growth plate disruption) (celine2013exomesequencingidentifies pages 1-2, muller2024thefunctionalroles pages 14-15)
- **Chondrocyte differentiation and hypertrophy** (reduced hypertrophic zone) (celine2013exomesequencingidentifies pages 1-2)
- **Chondrocyte proliferation/organization** (disorganized proliferative zone; absent columnar organization) (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2)
- **Phosphoinositide metabolic process / phosphatidylinositol dephosphorylation** (SHIP2 enzymatic function; mutation localization to catalytic domain) (celine2013exomesequencingidentifies pages 4-4, edimo2014ship2signalingin pages 3-5)
- **Regulation of AKT signaling** (SHIP2 reduces membrane PIP3 and inhibits AKT signaling in reviewed contexts) (muller2024thefunctionalroles pages 14-15)
- **FGF signaling modulation** (zebrafish knockdown evidence) (edimo2014ship2signalingin pages 3-5)

### 5. Cellular components (where key processes occur)
Opsismodysplasia mechanisms localize to compartments where SHIP2 acts on phosphoinositides:
- **Plasma membrane**: phosphoinositide substrates and PI3K signaling lipids (PIP3/PIP2) are membrane-associated; SHIP2 activity affects membrane PIP3 and AKT signaling output. (muller2024thefunctionalroles pages 14-15)
- **Cytosolic signaling complexes / docking interactions**: INPPL1 has described non-catalytic scaffold/docking roles interacting with cytoskeletal and receptor-associated proteins, potentially relevant to organized growth plate column formation. (celine2013exomesequencingidentifies pages 4-6)

### 6. Disease progression model (sequence from trigger to phenotype)

1. **Initiating trigger:** Biallelic pathogenic variants in INPPL1 (often truncating/splice or catalytic missense) produce SHIP2 loss or dysfunction. (below2013wholegenomeanalysisreveals pages 5-7, celine2013exomesequencingidentifies pages 1-2)
2. **Molecular consequence:** Impaired phosphoinositide turnover (PtdIns(3,4,5)P3 → PtdIns(3,4)P2) and altered downstream signaling outputs (including PI3K–AKT modulation and potentially growth factor pathways such as FGF, per zebrafish data). (celine2013exomesequencingidentifies pages 4-4, edimo2014ship2signalingin pages 3-5)
3. **Cellular consequence in growth plate:** Proliferative chondrocytes lose normal columnar organization; hypertrophic zone is reduced with fewer hypertrophic chondrocytes. (celine2013exomesequencingidentifies pages 1-2)
4. **Tissue consequence:** Impaired endochondral ossification manifests as delayed epiphyseal ossification and poor mineralization with characteristic skeletal radiology (e.g., platyspondyly). (below2013wholegenomeanalysisreveals pages 5-7, li2014opsismodysplasiaresultingfrom pages 1-3)
5. **Organism-level outcomes:** Severe short stature/micromelia; spinal deformity (scoliosis); thoracic restriction can contribute to pulmonary hypoplasia/respiratory insufficiency in severe cases. (celine2013exomesequencingidentifies pages 4-4)

**Recent in vivo reinforcement (2024):** Zebrafish inppl1a mutants are shorter from early larval stages and later develop notochord/spine abnormalities (thoracic scoliosis, vertebral malformations), supporting a conserved role in axial growth and endochondral lengthening. (voigt2024aconservedregulation pages 1-3)

### 7. Phenotypic manifestations (HP-oriented) and mechanistic links
Key clinical/radiographic phenotypes include:
- **Severe short stature and micromelia**—consistent with impaired growth plate function and endochondral bone formation. (celine2013exomesequencingidentifies pages 4-4, celine2013exomesequencingidentifies pages 1-2)
- **Delayed epiphyseal and carpal ossification**—directly matches the disease definition and endochondral ossification defect. (muller2024thefunctionalroles pages 14-15, li2014opsismodysplasiaresultingfrom pages 1-3)
- **Platyspondyly and skeletal undermineralization**—consistent with defective ossification/mineralization. (below2013wholegenomeanalysisreveals pages 5-7, li2014opsismodysplasiaresultingfrom pages 1-3)
- **Scoliosis**—reported clinically and supported by zebrafish model axial curvature. (celine2013exomesequencingidentifies pages 4-4, voigt2024aconservedregulation pages 1-3)
- **Narrow thorax / pulmonary hypoplasia** in severe prenatal/perinatal cases—likely secondary to shortened ribs/vertebral anomalies and restricted thoracic development. (celine2013exomesequencingidentifies pages 4-4)
- **Low bone density and renal phosphate wasting** have been described in an INPPL1-mutant case, suggesting that mineral metabolism abnormalities may modify skeletal outcomes in some patients. (li2014opsismodysplasiaresultingfrom pages 1-3)

### 8. Recent developments and latest research (prioritizing 2023–2024)

#### 8.1 2024 SHIP2 disease-mechanism and pharmacology synthesis
A 2024 review consolidates SHIP2’s roles across human diseases and explicitly includes opsismodysplasia as an INPPL1/SHIP2-mutation disorder defined by delayed ossification. It also connects SHIP2 enzymology to AKT signaling modulation and summarizes pharmacologic tool compounds (e.g., AS1949490) demonstrating that SHIP2 is chemically tractable. (muller2024thefunctionalroles pages 14-15)

#### 8.2 2024 organismal mechanism work relevant to skeletal growth
A 2024 zebrafish preprint provides new in vivo evidence that INPPL1 ortholog activity is required for **cell expansion**, **notochord mechanics**, **spine morphogenesis**, and **endochondral bone lengthening**—directly relevant to how opsismodysplasia could arise from altered cell/tissue growth mechanics in developing skeletal structures. (voigt2024aconservedregulation pages 1-3)

### 9. Current applications and real-world implementations

#### 9.1 Clinical implementation: molecular diagnosis and counseling
Real-world implementation is primarily through **genetic testing (exome/genome sequencing)** for INPPL1 variants in suspected skeletal dysplasia cases. Early discovery work established that biallelic INPPL1 variants can be found across multiple unrelated families, supporting INPPL1 as a key diagnostic target. (celine2013exomesequencingidentifies pages 1-2)

#### 9.2 Supportive management (example of mineral metabolism intervention)
A 2014 clinical report described renal phosphate wasting and very low bone density in an affected individual; **phosphate replacement improved ambulation and dental eruption**, and pamidronate was administered for low bone mineral density. This illustrates that while no disease-modifying therapy for the core signaling defect exists, **targeted supportive interventions** may improve function in selected patients. (li2014opsismodysplasiaresultingfrom pages 1-3)

### 10. Expert opinions and analysis (authoritative synthesis)

- **Primary conceptual model:** opsismodysplasia is a growth-plate/endocondral-ossification disorder caused by disruption of phosphoinositide signaling via SHIP2 loss-of-function. This is supported by the convergence of (i) mutation patterns that abolish catalytic function, (ii) direct protein loss in patient-derived cells, and (iii) consistent growth plate disorganization. (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2, feist2016novelcompoundheterozygous media 56a554cb)
- **Mechanistic nuance:** synthesis work highlights that SHIP2 biology may not reduce to “more AKT signaling”; rather, specific depletion of PI(3,4)P2 (and its effector interactions) may drive developmental phenotypes, which could explain why pathway readouts may differ across tissues and models. (edimo2014ship2signalingin pages 3-5)
- **Translational interpretation:** 2024 reviews show SHIP2 is chemically targetable with inhibitors developed for metabolic/neuroinflammatory indications; however, because opsismodysplasia reflects developmental skeletal patterning and growth plate architecture, any future translation would likely require careful timing and tissue targeting, and is not currently established. (muller2024thefunctionalroles pages 14-15)

### 11. Evidence figure (protein-level evidence)
A key experimental/clinical evidence item is an immunoblot showing **absence of SHIP2 protein** in proband amniocytes (with α-tubulin loading control), supporting a loss-of-protein mechanism in at least some genotypes. (feist2016novelcompoundheterozygous media 56a554cb)

### 12. Evidence tables for knowledge-base population

Below are curated tables intended for direct knowledge-base population.

| Concept/Mechanism | Molecular players (gene/protein/lipid) | Tissue/cell type | Key evidence (brief) | PMID/DOI | Publication year | URL |
|---|---|---|---|---|---|---|
| Causal genetic mechanism and growth-plate disorganization | **INPPL1** / SHIP2; phosphoinositides | Growth plate cartilage; proliferative and hypertrophic chondrocytes | Exome sequencing identified **12 distinct INPPL1 mutations in 10 unrelated families** with opsismodysplasia; histology showed **loss of normal columnar arrangement of proliferative chondrocytes**, **reduced hypertrophic zone**, and **fewer hypertrophic chondrocytes**, supporting a primary defect in endochondral ossification (celine2013exomesequencingidentifies pages 1-2) | DOI: 10.1016/j.ajhg.2012.11.015 | 2013 | https://doi.org/10.1016/j.ajhg.2012.11.015 |
| Proportion of cases explained by INPPL1 and supportive animal phenotype | **INPPL1** / SHIP2 | Human skeleton; mouse axial/appendicular skeleton | Whole-genome analysis found **INPPL1 mutations in 7/12 kindreds (58%)** and **5/10 simplex cases (50%)**; truncating variants predicted loss of function. Mouse **SHIP2-null/catalytic-dead** models showed **diminished growth**, shortened facial profile, and body size reduction, supporting a developmental role for SHIP2 in skeletal growth (below2013wholegenomeanalysisreveals pages 5-7) | DOI: 10.1016/j.ajhg.2012.11.011 | 2013 | https://doi.org/10.1016/j.ajhg.2012.11.011 |
| Dysregulated phosphoinositide signaling and developmental pathway links | SHIP2; **PI(3,4,5)P3**, **PI(3,4)P2**; FGF signaling | Developing embryo; growth-related tissues | Review synthesis: SHIP2 loss reduces **PI(3,4)P2** and perturbs phosphoinositide balance; phenotypes in catalytic-dead mice were attributed more to lack of **PI(3,4)P2** than simple PI3K-AKT hyperactivation. In zebrafish, **Ship2 knockdown perturbed FGF signaling** and expanded dorsal fates, linking SHIP2 to developmental patterning mechanisms relevant to OPS (edimo2014ship2signalingin pages 3-5) | DOI: 10.1016/j.jbior.2013.09.002 | 2014 | https://doi.org/10.1016/j.jbior.2013.09.002 |
| Loss of SHIP2 protein and severe fetal growth-plate histopathology | **INPPL1** / SHIP2; **PIP3** | Fetal growth plate cartilage; amniocytes | Compound-heterozygous **INPPL1** variants were associated with **absence of detectable SHIP2 protein** in fetal cells. Fetal growth plate cartilage showed **disorganized proliferative zones with near absent columnar organization**, correlating with delayed epiphyseal ossification and severe platyspondyly (feist2016novelcompoundheterozygous pages 3-4) | DOI: 10.1097/MCD.0000000000000136 | 2016 | https://doi.org/10.1097/MCD.0000000000000136 |
| Current disease definition and therapeutic context | **INPPL1** / SHIP2; **PtdIns(3,4,5)P3**; AKT; SHIP2 inhibitors **AS1949490**, K118, K149, K161 | Skeletal tissue (disease context); broader cell signaling systems | 2024 review defines opsismodysplasia as a skeletal dysplasia **“primarily characterized by the delayed ossification of maturing bones.”** It places SHIP2 in **PIP3-to-AKT** regulation and notes selective/pan-SHIP inhibitors (e.g., **AS1949490**, **K161**) with experimental activity in other disease settings, highlighting translational relevance even though no OPS-targeted therapy is established (muller2024thefunctionalroles pages 14-15) | DOI: 10.3390/ijms25105254 | 2024 | https://doi.org/10.3390/ijms25105254 |
| Recent in vivo model for cell expansion, spine morphogenesis, and endochondral lengthening | Zebrafish **inppl1a** (ortholog of **INPPL1/SHIP2**) | Notochord vacuolated cells; spine; endochondral bone | 2024 zebrafish preprint shows **inppl1a** is required for **cell expansion**, **normal notochord mechanics**, **spine morphogenesis**, and **endochondral bone lengthening**. Homozygous mutants were **shorter**, had reduced viability, notochord curvatures, adult thoracic scoliosis, and vertebral malformations, providing recent organismal support for INPPL1-related skeletal pathophysiology (voigt2024aconservedregulation pages 1-3) | DOI: 10.1101/2024.08.12.607640 | 2024 | https://doi.org/10.1101/2024.08.12.607640 |


*Table: This table compiles the main mechanistic and experimental evidence linking INPPL1/SHIP2 dysfunction to opsismodysplasia, spanning discovery genetics, phosphoinositide signaling, growth-plate pathology, and recent model-organism work. It is useful as a concise evidence map for disease knowledge-base curation.*

| Entity type | Preferred label | ID (HGNC/GO/HP/CL/UBERON/CHEBI) | Evidence/notes |
|---|---|---|---|
| Gene | INPPL1 | HGNC:6091 | Causal gene for opsismodysplasia; encodes SHIP2, a phosphoinositide 5-phosphatase. Biallelic variants are predominantly truncating, splice-site, or catalytic-domain missense, consistent with loss of function; one cohort found INPPL1 variants in 7/12 kindreds (58%) and 5/10 simplex cases (below2013wholegenomeanalysisreveals pages 5-7, celine2013exomesequencingidentifies pages 1-2). |
| Gene | SHIP2 protein | UniProt/Q9Y5R2 | Protein product of INPPL1; absent in affected fetal cells/amniocytes in one family, supporting pathogenic protein loss (feist2016novelcompoundheterozygous pages 3-4, feist2016novelcompoundheterozygous media 56a554cb). |
| GO | phosphatidylinositol-3,4,5-trisphosphate 5-phosphatase activity | GO:0046856 | SHIP2 dephosphorylates PtdIns(3,4,5)P3, placing opsismodysplasia in the phosphoinositide signaling disease spectrum (feist2016novelcompoundheterozygous pages 3-4). |
| GO | phosphatidylinositol dephosphorylation | GO:0046854 | Core biochemical mechanism inferred from SHIP2 enzymatic function and disease-causing catalytic-domain variants (celine2013exomesequencingidentifies pages 4-4, edimo2014ship2signalingin pages 3-5). |
| GO | phosphoinositide metabolic process | GO:0046488 | INPPL1 regulates levels of specific phosphoinositides; disease likely reflects disrupted phosphoinositide turnover in skeletal development (celine2013exomesequencingidentifies pages 4-4, celine2013exomesequencingidentifies pages 1-2). |
| GO | phosphatidylinositol 3-kinase signaling | GO:0014065 | SHIP2 functions within the PI3K pathway by turning over PI3K-generated PtdIns(3,4,5)P3; loss is expected to alter PI3K pathway output (celine2013exomesequencingidentifies pages 4-4, feist2016novelcompoundheterozygous pages 3-4). |
| GO | positive regulation of AKT signaling | GO:0051897 | SHIP2 normally reduces PtdIns(3,4,5)P3 and can inhibit AKT signaling; thus disease-causing loss likely perturbs AKT pathway regulation, though cartilage-specific AKT readouts remain limited (muller2024thefunctionalroles pages 14-15). |
| GO | endochondral ossification | GO:0001958 | Most directly implicated developmental process; patient histology and skeletal findings indicate a primary defect in endochondral ossification with delayed epiphyseal ossification (celine2013exomesequencingidentifies pages 1-2, feist2016novelcompoundheterozygous pages 3-4). |
| GO | chondrocyte differentiation | GO:0002063 | Growth plate histology shows reduced hypertrophic zone and fewer hypertrophic chondrocytes, consistent with impaired chondrocyte maturation/differentiation (celine2013exomesequencingidentifies pages 1-2). |
| GO | chondrocyte proliferation | GO:0035988 | Near-absence of normal columnar organization in the proliferative zone supports altered proliferative chondrocyte behavior (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2). |
| GO | fibroblast growth factor receptor signaling pathway | GO:0008543 | Zebrafish Ship2 knockdown perturbs FGF signaling and developmental patterning, suggesting a plausible conserved mechanism relevant to skeletal morphogenesis (celine2013exomesequencingidentifies pages 4-6, edimo2014ship2signalingin pages 3-5). |
| GO | cell growth | GO:0016049 | Recent zebrafish inppl1a data support a role in cell expansion and endochondral bone lengthening, extending the growth-regulatory disease model (voigt2024aconservedregulation pages 1-3). |
| GO | establishment or maintenance of cell polarity | GO:0007163 | SHIP2 has non-catalytic roles in polarity/migration pathways, relevant because growth plate organization is disrupted in disease (celine2013exomesequencingidentifies pages 4-6, edimo2014ship2signalingin pages 3-5). |
| GO | cell migration | GO:0016477 | SHIP2 participates in migration/polarity signaling via phosphoinositides and cytoskeletal interactions; included as a plausible contributing process rather than OPS-specific proven mechanism (celine2013exomesequencingidentifies pages 4-6, edimo2014ship2signalingin pages 3-5). |
| GO | plasma membrane | GO:0005886 | SHIP2 acts on membrane phosphoinositides such as PtdIns(3,4,5)P3 at the plasma membrane (muller2024thefunctionalroles pages 14-15). |
| GO | cytosol | GO:0005829 | SHIP2 also functions in intracellular signaling complexes and docking interactions involving cytoskeletal/scaffold proteins (celine2013exomesequencingidentifies pages 4-6, feist2016novelcompoundheterozygous pages 4-7). |
| HP | Short stature | HP:0004322 | Severe pre- and postnatal growth deficiency is a consistent phenotype in surviving patients (celine2013exomesequencingidentifies pages 4-4, below2013wholegenomeanalysisreveals pages 5-7). |
| HP | Micromelia | HP:0002983 | Pre- and postnatal micromelia/short long bones are characteristic clinical findings (celine2013exomesequencingidentifies pages 4-4, celine2013exomesequencingidentifies pages 1-2). |
| HP | Delayed ossification of epiphyses | HP:0003093 | Delayed epiphyseal ossification is repeatedly described and is central to disease definition (muller2024thefunctionalroles pages 14-15, li2014opsismodysplasiaresultingfrom pages 1-3). |
| HP | Platyspondyly | HP:0000926 | Severe platyspondyly is a hallmark radiographic feature (feist2016novelcompoundheterozygous pages 3-4, li2014opsismodysplasiaresultingfrom pages 1-3). |
| HP | Scoliosis | HP:0002650 | Severe scoliosis has been reported in survivors; zebrafish inppl1a mutants also develop spinal curvature, supporting mechanistic relevance (celine2013exomesequencingidentifies pages 4-4, voigt2024aconservedregulation pages 1-3). |
| HP | Narrow thorax | HP:0000774 | Narrow chest/thorax contributes to respiratory compromise in severe neonatal presentations (celine2013exomesequencingidentifies pages 4-4). |
| HP | Pulmonary hypoplasia | HP:0002089 | Reported in severe prenatal/perinatal cases and likely secondary to restricted thoracic development (celine2013exomesequencingidentifies pages 4-4). |
| HP | Craniofacial abnormality | HP:0001999 | Craniofacial abnormalities/large neurocranium/shortened facial profile are reported in patients and mouse models (feist2016novelcompoundheterozygous pages 3-4, below2013wholegenomeanalysisreveals pages 5-7). |
| HP | Decreased bone mineral density | HP:0004349 | Low bone density/undermineralization has been documented clinically (below2013wholegenomeanalysisreveals pages 5-7, li2014opsismodysplasiaresultingfrom pages 1-3). |
| HP | Renal phosphate wasting | HP:0000117 | Renal phosphate wasting was described in an INPPL1-mutant patient, with phosphate replacement improving some outcomes (li2014opsismodysplasiaresultingfrom pages 1-3). |
| CL | chondrocyte | CL:0000138 | Principal disease-relevant cell type in growth plate cartilage (celine2013exomesequencingidentifies pages 1-2, feist2016novelcompoundheterozygous pages 3-4). |
| CL | hypertrophic chondrocyte | CL:0002333 | Reduced hypertrophic zone/fewer hypertrophic chondrocytes on histology implicate this maturation stage (celine2013exomesequencingidentifies pages 1-2). |
| CL | proliferative chondrocyte | CL:0002334 | Disorganized proliferative zones with near-absent columnar arrangement strongly implicate proliferative chondrocytes (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2). |
| UBERON | growth plate cartilage | UBERON:0003429 | Primary anatomic site of pathology based on fetal histology and endochondral growth defects (feist2016novelcompoundheterozygous pages 3-4, celine2013exomesequencingidentifies pages 1-2). |
| UBERON | epiphysis | UBERON:0004352 | Delayed epiphyseal ossification is a defining radiographic/clinical feature (muller2024thefunctionalroles pages 14-15, li2014opsismodysplasiaresultingfrom pages 1-3). |
| UBERON | vertebral column | UBERON:0001130 | Platyspondyly, vertebral abnormalities, and scoliosis indicate major vertebral involvement (below2013wholegenomeanalysisreveals pages 5-7, voigt2024aconservedregulation pages 1-3). |
| UBERON | long bone | UBERON:0002371 | Short long bones, bowing, and metaphyseal changes are prominent manifestations (celine2013exomesequencingidentifies pages 4-4, li2014opsismodysplasiaresultingfrom pages 1-3). |
| UBERON | pelvis | UBERON:0001270 | Poor ossification of pelvic bones and poorly formed acetabula are recurrent imaging findings (below2013wholegenomeanalysisreveals pages 5-7, feist2016novelcompoundheterozygous pages 4-7). |
| CHEBI | phosphatidylinositol 3,4,5-trisphosphate | CHEBI:16595 | Direct SHIP2 substrate; excess/abnormal handling is central to proposed disease mechanism (feist2016novelcompoundheterozygous pages 3-4, muller2024thefunctionalroles pages 14-15). |
| CHEBI | phosphatidylinositol 3,4-bisphosphate | CHEBI:17289 | Key SHIP2 product; reduced PI(3,4)P2 has been emphasized as mechanistically important in SHIP2-deficient phenotypes (edimo2014ship2signalingin pages 3-5). |
| CHEBI | AS1949490 | not available | SHIP2-selective inhibitor discussed in 2024 review; relevant as a mechanistic chemical probe, not an opsismodysplasia therapy (muller2024thefunctionalroles pages 14-15). |


*Table: This table maps core opsismodysplasia mechanisms, phenotypes, cells, tissues, and chemicals to ontology-style identifiers suitable for knowledge-base curation. It emphasizes the INPPL1/SHIP2-centered phosphoinositide signaling defect and its links to growth plate disorganization and impaired endochondral ossification.*

### 13. Evidence items with PMIDs (primary literature prioritized)
- **Below et al., AJHG (2013)** Whole-genome analysis; INPPL1 mutations in 58% of kindreds and 50% of simplex cases; links to mouse developmental growth phenotypes. PMID: **23273569**; DOI: 10.1016/j.ajhg.2012.11.011; Published Jan 2013. (below2013wholegenomeanalysisreveals pages 5-7)
- **Huber et al., AJHG (2013)** Exome sequencing; 12 INPPL1 mutations in 10 families; growth plate disorganization and reduced hypertrophic zone. DOI: 10.1016/j.ajhg.2012.11.015; Published Jan 2013. (celine2013exomesequencingidentifies pages 1-2)

### Limitations of the current evidence base
Opsismodysplasia is ultra-rare; as a result, the most direct growth-plate mechanistic evidence remains concentrated in the 2013 discovery literature and a limited number of follow-up reports. Recent (2023–2024) work strengthens general SHIP2 signaling context and provides new model-organism evidence for skeletal growth roles, but **cartilage-specific PI3K–AKT/FGF pathway readouts in human growth plate cells remain sparse** in the accessible literature set. (edimo2014ship2signalingin pages 3-5, muller2024thefunctionalroles pages 14-15, voigt2024aconservedregulation pages 1-3)

References

1. (muller2024thefunctionalroles pages 14-15): Spike Murphy Müller and Manfred Jücker. The functional roles of the src homology 2 domain-containing inositol 5-phosphatases ship1 and ship2 in the pathogenesis of human diseases. International Journal of Molecular Sciences, 25:5254, May 2024. URL: https://doi.org/10.3390/ijms25105254, doi:10.3390/ijms25105254. This article has 16 citations.

2. (below2013wholegenomeanalysisreveals pages 5-7): Jennifer E. Below, Dawn L. Earl, Kathryn M. Shively, Margaret J. McMillin, Joshua D. Smith, Emily H. Turner, Mark J. Stephan, Lihadh I. Al-Gazali, Jozef L. Hertecant, David Chitayat, Sheila Unger, Daniel H. Cohn, Deborah Krakow, James M. Swanson, Elaine M. Faustman, Jay Shendure, Deborah A. Nickerson, and Michael J. Bamshad. Whole-genome analysis reveals that mutations in inositol polyphosphate phosphatase-like 1 cause opsismodysplasia. American journal of human genetics, 92 1:137-43, Jan 2013. URL: https://doi.org/10.1016/j.ajhg.2012.11.011, doi:10.1016/j.ajhg.2012.11.011. This article has 67 citations and is from a highest quality peer-reviewed journal.

3. (celine2013exomesequencingidentifies pages 1-2): Céline Huber, Eissa Ali Faqeih, Deborah Bartholdi, Christine Bole-Feysot, Zvi Borochowitz, Denise P Cavalcanti, Amandine Frigo, Patrick Nitschke, Joelle Roume, Heloísa G Santos, Stavit A Shalev, Andrea Superti-Furga, Anne-Lise Delezoide, Martine Le Merrer, Arnold Munnich, and Valérie Cormier-Daire. Exome sequencing identifies inppl1 mutations as a cause of opsismodysplasia. American journal of human genetics, 92 1:144-9, Jan 2013. URL: https://doi.org/10.1016/j.ajhg.2012.11.015, doi:10.1016/j.ajhg.2012.11.015. This article has 62 citations and is from a highest quality peer-reviewed journal.

4. (feist2016novelcompoundheterozygous pages 3-4): Cori Feist, Paul Holden, and Jamie Fitzgerald. Novel compound heterozygous mutations in inositol polyphosphate phosphatase-like 1 in a family with severe opsismodysplasia. Clinical Dysmorphology, 25:152–155, Oct 2016. URL: https://doi.org/10.1097/mcd.0000000000000136, doi:10.1097/mcd.0000000000000136. This article has 10 citations and is from a peer-reviewed journal.

5. (celine2013exomesequencingidentifies pages 4-4): Céline Huber, Eissa Ali Faqeih, Deborah Bartholdi, Christine Bole-Feysot, Zvi Borochowitz, Denise P Cavalcanti, Amandine Frigo, Patrick Nitschke, Joelle Roume, Heloísa G Santos, Stavit A Shalev, Andrea Superti-Furga, Anne-Lise Delezoide, Martine Le Merrer, Arnold Munnich, and Valérie Cormier-Daire. Exome sequencing identifies inppl1 mutations as a cause of opsismodysplasia. American journal of human genetics, 92 1:144-9, Jan 2013. URL: https://doi.org/10.1016/j.ajhg.2012.11.015, doi:10.1016/j.ajhg.2012.11.015. This article has 62 citations and is from a highest quality peer-reviewed journal.

6. (feist2016novelcompoundheterozygous media 56a554cb): Cori Feist, Paul Holden, and Jamie Fitzgerald. Novel compound heterozygous mutations in inositol polyphosphate phosphatase-like 1 in a family with severe opsismodysplasia. Clinical Dysmorphology, 25:152–155, Oct 2016. URL: https://doi.org/10.1097/mcd.0000000000000136, doi:10.1097/mcd.0000000000000136. This article has 10 citations and is from a peer-reviewed journal.

7. (edimo2014ship2signalingin pages 3-5): William's Elong Edimo, Stéphane Schurmans, Pierre P. Roger, and Christophe Erneux. Ship2 signaling in normal and pathological situations: its impact on cell proliferation. Advances in Biological Regulation, 54:142-151, Jan 2014. URL: https://doi.org/10.1016/j.jbior.2013.09.002, doi:10.1016/j.jbior.2013.09.002. This article has 37 citations and is from a peer-reviewed journal.

8. (celine2013exomesequencingidentifies pages 4-6): Céline Huber, Eissa Ali Faqeih, Deborah Bartholdi, Christine Bole-Feysot, Zvi Borochowitz, Denise P Cavalcanti, Amandine Frigo, Patrick Nitschke, Joelle Roume, Heloísa G Santos, Stavit A Shalev, Andrea Superti-Furga, Anne-Lise Delezoide, Martine Le Merrer, Arnold Munnich, and Valérie Cormier-Daire. Exome sequencing identifies inppl1 mutations as a cause of opsismodysplasia. American journal of human genetics, 92 1:144-9, Jan 2013. URL: https://doi.org/10.1016/j.ajhg.2012.11.015, doi:10.1016/j.ajhg.2012.11.015. This article has 62 citations and is from a highest quality peer-reviewed journal.

9. (voigt2024aconservedregulation pages 1-3): Brittney Voigt, Katherine Frazier, Donya Yazdi, Paul Gontarz, Bo Zhang, Diane S. Sepich, Lilianna Solnica-Krezel, and Ryan S. Gray. A conserved regulation of cell expansion underlies notochord mechanics, spine morphogenesis, and endochondral bone lengthening. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.12.607640, doi:10.1101/2024.08.12.607640. This article has 2 citations.

10. (li2014opsismodysplasiaresultingfrom pages 1-3): Bing Li, Deborah Krakow, Deborah A. Nickerson, Michael J. Bamshad, Yong Chang, Ralph S. Lachman, Alev Yilmaz, Hülya Kayserili, and Daniel H. Cohn. Opsismodysplasia resulting from an insertion mutation in the sh2 domain, which destabilizes inppl1. American Journal of Medical Genetics Part A, 164:2407-2411, Jun 2014. URL: https://doi.org/10.1002/ajmg.a.36640, doi:10.1002/ajmg.a.36640. This article has 19 citations.

11. (feist2016novelcompoundheterozygous pages 4-7): Cori Feist, Paul Holden, and Jamie Fitzgerald. Novel compound heterozygous mutations in inositol polyphosphate phosphatase-like 1 in a family with severe opsismodysplasia. Clinical Dysmorphology, 25:152–155, Oct 2016. URL: https://doi.org/10.1097/mcd.0000000000000136, doi:10.1097/mcd.0000000000000136. This article has 10 citations and is from a peer-reviewed journal.