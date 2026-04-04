---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-02T15:45:46.071164'
end_time: '2026-04-02T16:07:40.304577'
duration_seconds: 1314.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Diastrophic Dysplasia
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Diastrophic Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Diastrophic Dysplasia**.
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
- **Disease Name:** Diastrophic Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Diastrophic Dysplasia**.
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


## Disease Pathophysiology Research Report: Diastrophic Dysplasia (DTD)

### Target disease summary
Diastrophic dysplasia (DTD) is a rare **autosomal recessive** chondrodysplasia affecting cartilage and bone development, classically assigned **MIM/OMIM #222600** and caused by biallelic pathogenic variants in **SLC26A2** (also known as DTDST; **OMIM #606718**). (paganini2023identificationofpotential pages 1-3, silveira2022slc26a2dtdstspectruma pages 1-2)

**MONDO mapping (available from Open Targets evidence in this run):** **MONDO_0009107 (diastrophic dysplasia)**. (gramegnatota2023chondrodysplasiascausedby pages 42-46)

---

## 1) Key concepts and definitions (current understanding)

### Core molecular definition
**SLC26A2 encodes a transmembrane sulfate/chloride antiporter** that is critical for **inorganic sulfate uptake** into chondrocytes; intracellular sulfate is required to generate activated sulfate donors (e.g., PAPS) that drive **glycosaminoglycan (GAG)/proteoglycan sulfation**. Reduced sulfate transport results in **undersulfated cartilage proteoglycans**, which disrupt cartilage extracellular matrix (ECM) structure and endochondral ossification, producing the skeletal phenotype. (paganini2023identificationofpotential pages 1-3, gramegnatota2023chondrodysplasiascausedbya pages 42-46)

A key disease principle is the **residual-activity model**: across SLC26A2-related conditions (including lethal and non-lethal phenotypes), **clinical severity correlates with residual sulfate transport capacity and degree of proteoglycan undersulfation**. (paganini2023identificationofpotential pages 1-3)

---

## 2) Primary pathophysiological mechanisms (molecular and cellular)

### 2.1 Initiating lesion: sulfate transport defect → reduced proteoglycan sulfation
DTD pathophysiology begins with impaired sulfate uptake via SLC26A2, lowering the sulfate available for proteoglycan/GAG sulfation in cartilage. This results in **cartilage proteoglycan undersulfation** detectable biochemically and histochemically in mouse models and consistent with patient observations. (forlino2005adiastrophicdysplasia pages 8-9, paganini2023identificationofpotential pages 1-3)

**Quantitative example (mouse dtd A386V model):** chondroitin sulfation at birth was reported as approximately **~0.7 sulfate/disaccharide in dtd vs ~0.9 in wild type**, with strong regional variation across cartilage zones. (mertz2012matrixdisruptionsgrowth pages 1-1)

### 2.2 ECM-level consequences: altered hydration/mechanics and collagen organization
Undersulfated proteoglycans alter cartilage ECM composition, architecture, and mechanics (reduced water retention and collagen “unmasking”), providing a mechanistic bridge from a transport defect to tissue fragility and abnormal morphogenesis. (gramegnatota2023chondrodysplasiascausedbya pages 42-46)

In the dtd mouse, reduced chondroitin sulfation **correlated with reduced collagen orientation**, including in the protective collagen layer of articular cartilage; this was proposed to contribute to progressive cartilage degeneration despite partial normalization of sulfation with age. (mertz2012matrixdisruptionsgrowth pages 1-1, mertz2012matrixdisruptionsgrowth media e64dc09b)

### 2.3 Growth plate dysfunction: impaired proliferation and delayed ossification
Mouse models show developmental consequences consistent with impaired endochondral ossification:
- progressive changes in proteoglycan sulfation with age (P1–P60) (forlino2005adiastrophicdysplasia pages 8-9)
- delayed secondary ossification center formation (forlino2005adiastrophicdysplasia pages 1-2)
- growth-plate disorganization at later time points (P60) (forlino2005adiastrophicdysplasia pages 8-9)

Mechanistically, reduced proliferation has been linked to altered **Indian hedgehog (Ihh)** signaling and cell-cycle control via reduced **p130 phosphorylation** affecting E2F transcription factors, causing a **G1 block** (reported in a synthesis of model data). (gramegnatota2023chondrodysplasiascausedbyc pages 127-129)

### 2.4 Severe/“lethal-end” mechanism: collagen secretion defect → ER stress/UPR → FGFR3 overactivation
Beyond undersulfation, severe Slc26a2 deficiency models demonstrate a second major mechanism: impaired secretion of major cartilage collagens.

In **slc26a2−/−** chondrocytes, **ColII and ColIX** show **strong intracellular retention** with reduced extracellular deposition; ultrastructural data include ER distension and intracellular matrix-containing vesicles. (zheng2019suppressinguprdependentoveractivation pages 6-8)

This intracellular retention triggers **ER stress** and the **unfolded protein response (UPR)**, with **preferential activation/nuclear localization of ATF6**, and **increased ATF6 and FGFR3 protein levels**. (zheng2019suppressinguprdependentoveractivation pages 6-8)

The same work links ATF6 to **FGFR3 transcriptional upregulation** and demonstrates **overactivation of FGFR3 signaling** (increased p-ERK1/2 and p-STAT1; hypersensitivity to FGF2). (zheng2019suppressinguprdependentoveractivation pages 6-8)

**Interpretation (expert mechanistic synthesis):** DTD pathophysiology is not solely “undersulfation,” but can include a UPR-driven signaling pathology (ATF6→FGFR3) that is targetable pharmacologically in preclinical models; this provides a mechanistic rationale for pathway-directed therapy. (zheng2019suppressinguprdependentoveractivation pages 1-2, li2024targetingfgfr3signaling pages 11-13)

---

## 3) Key molecular players (genes/proteins, chemicals, cells, tissues)

### 3.1 Genes/proteins
- **SLC26A2/DTDST**: causal gene and core sulfate transporter. (paganini2023identificationofpotential pages 1-3, silveira2022slc26a2dtdstspectruma pages 1-2)
- **FGFR3**: overactivated in severe Slc26a2 deficiency; pharmacologic/genetic suppression ameliorates phenotype in models. (zheng2019suppressinguprdependentoveractivation pages 6-8, li2024targetingfgfr3signaling pages 11-13)
- **ATF6 (UPR arm)**: preferentially activated in severe deficiency; implicated in FGFR3 upregulation. (zheng2019suppressinguprdependentoveractivation pages 6-8)
- **COL2A1/COL9A1/2/3 (collagen II/IX)**: extracellular deposition reduced with intracellular retention in severe models, implicating secretory pathway stress. (zheng2019suppressinguprdependentoveractivation pages 6-8)
- **Ihh pathway components** and **p130/E2F** cell-cycle control are implicated in reduced chondrocyte proliferation in model-based syntheses. (gramegnatota2023chondrodysplasiascausedbyc pages 127-129)

### 3.2 Chemical entities (relevant metabolites/drugs)
- **Inorganic sulfate** (substrate for sulfation; limiting due to impaired uptake). (forlino2005adiastrophicdysplasia pages 8-9, gramegnatota2023chondrodysplasiascausedbya pages 42-46)
- **PAPS** (universal sulfate donor; reported to become limiting when intracellular sulfate is reduced). (gramegnatota2023chondrodysplasiascausedbya pages 42-46)
- **N-acetylcysteine (NAC)**: proposed as an intracellular sulfate surrogate/thiol donor; reported to increase proteoglycan sulfation and improve phenotype in dtd mice (referenced in clinical review). (harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2)
- **NVP-BGJ398 (infigratinib)**: pan-FGFR inhibitor used in repurposing studies; prolonged treatment increased body size in Slc26a2 cKO mice. (li2024targetingfgfr3signaling pages 11-13)

### 3.3 Cell types primarily affected
- **Chondrocytes** (growth plate and articular cartilage): central cell type for sulfate uptake, ECM synthesis, and stress responses. (forlino2005adiastrophicdysplasia pages 8-9, zheng2019suppressinguprdependentoveractivation pages 6-8)
- **Osteoblasts and fibroblasts** can show impaired sulfate uptake, but strong proteoglycan undersulfation is emphasized as most evident in cartilage. (forlino2005adiastrophicdysplasia pages 1-2, gramegnatota2023chondrodysplasiascausedbyc pages 127-129)

### 3.4 Anatomical locations
- **Cartilage ECM**, especially **growth plate** and **articular cartilage** regions with high matrix synthesis rates show critical susceptibility and regional undersulfation. (mertz2012matrixdisruptionsgrowth pages 1-1, mertz2012matrixdisruptionsgrowth media e64dc09b)

---

## 4) Biological processes disrupted (GO-style descriptions)

From the mechanistic evidence in this corpus, disrupted processes include:
- **Sulfate transmembrane transport** (SLC26A2-dependent). (paganini2023identificationofpotential pages 1-3, forlino2005adiastrophicdysplasia pages 8-9)
- **Proteoglycan/GAG sulfation** and cartilage matrix assembly. (paganini2023identificationofpotential pages 1-3, gramegnatota2023chondrodysplasiascausedbya pages 42-46)
- **Extracellular matrix organization** (collagen orientation/architecture and proteoglycan-dependent hydration). (mertz2012matrixdisruptionsgrowth pages 1-1, gramegnatota2023chondrodysplasiascausedbya pages 42-46)
- **Endochondral ossification / growth plate development** (delayed ossification, reduced proliferation/differentiation). (forlino2005adiastrophicdysplasia pages 1-2, gramegnatota2023chondrodysplasiascausedbyc pages 127-129)
- **ER stress / unfolded protein response (ATF6 arm)** and downstream **FGFR3 signaling** (in severe deficiency). (zheng2019suppressinguprdependentoveractivation pages 6-8)

(Exact GO identifiers were not retrievable from the provided text excerpts; mapping would require ontology lookup beyond the retrieved text.)

---

## 5) Cellular components implicated
- **Plasma membrane**: SLC26A2 localization/function as transmembrane sulfate transporter. (paganini2023identificationofpotential pages 1-3, paganini2020skeletaldysplasiascaused pages 9-10)
- **Endoplasmic reticulum**: collagen retention/ER distension and UPR activation in severe deficiency. (zheng2019suppressinguprdependentoveractivation pages 6-8)
- **Extracellular matrix**: site of undersulfated proteoglycans and altered collagen organization. (mertz2012matrixdisruptionsgrowth pages 1-1, gramegnatota2023chondrodysplasiascausedbya pages 42-46)

---

## 6) Disease progression model (sequence of events)

1. **Biallelic SLC26A2 variants** reduce sulfate transport into chondrocytes. (paganini2023identificationofpotential pages 1-3, forlino2005adiastrophicdysplasia pages 8-9)
2. **Lower intracellular sulfate** limits activated sulfate donor availability and drives **undersulfated proteoglycans** in cartilage. (gramegnatota2023chondrodysplasiascausedbya pages 42-46, forlino2005adiastrophicdysplasia pages 8-9)
3. **Cartilage ECM abnormalities** emerge (reduced sulfated matrix staining; altered collagen orientation), affecting mechanical properties and signaling. (forlino2005adiastrophicdysplasia pages 8-9, mertz2012matrixdisruptionsgrowth pages 1-1)
4. **Growth plate dysfunction** with reduced proliferation/delayed maturation (and altered Ihh/p130/E2F control as reported) leads to impaired longitudinal bone growth and delayed ossification centers. (forlino2005adiastrophicdysplasia pages 8-9, gramegnatota2023chondrodysplasiascausedbyc pages 127-129, forlino2005adiastrophicdysplasia pages 1-2)
5. In more severe contexts, **collagen secretion defects** cause **ER stress/UPR**, inducing **ATF6-driven FGFR3 overactivation**, further impairing cartilage growth and survival balance. (zheng2019suppressinguprdependentoveractivation pages 6-8)
6. Clinically, these processes manifest as congenital skeletal dysplasia with progressive orthopedic complications and joint degeneration. (bondarenko2023slc26a2relateddiastrophic pages 1-2, harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)

---

## 7) Phenotypic manifestations (mechanism-linked)

### Key clinical phenotypes
- **Short-limbed short stature** and disproportionate growth. (bondarenko2023slc26a2relateddiastrophic pages 1-2, harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)
- **Joint dysplasia/contractures** and progressive orthopedic morbidity (frequent knee/patellar issues; multiple surgeries in cohorts). (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)
- **Spinal deformities** including scoliosis/kyphosis. (bondarenko2023slc26a2relateddiastrophic pages 1-2)
- **External ear/pinna abnormalities** (cartilage involvement outside the skeleton). (bondarenko2023slc26a2relateddiastrophic pages 1-2)
- **Cleft palate** is common in the Finnish pediatric cohort (64%). (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)
- **Neonatal respiratory insufficiency** occurs in a subset (36% in Finnish cohort). (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)

### Genotype–phenotype relationships (selected examples)
A major, widely cited principle is that phenotype severity correlates with residual transport activity, but the same genotype can produce variable phenotypes. (paganini2023identificationofpotential pages 1-3, silveira2022slc26a2dtdstspectruma pages 9-10)

Population and allele effects:
- Finland shows a strong founder effect for **c.-26+2T>C**, commonly homozygous in DTD, and the incidence has decreased over decades with increased prenatal diagnostics. (harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2, harkonen2021slc26a2associateddiastrophicdysplasia pages 5-7)
- **p.R279W** is frequent outside Finland and is associated with mild phenotype in homozygosity and can mitigate severity in compound heterozygosity (“rescue”). (silveira2022slc26a2dtdstspectruma pages 7-8)
- Adult DTD example variants include **p.Val341del** and **p.Cys653Ser** in compound heterozygosity. (bondarenko2023slc26a2relateddiastrophic pages 1-2)

---

## 8) Recent developments and latest research (2023–2024 prioritized)

### 8.1 Biomarker development (2023)
A 2023 Bone study evaluated two non-invasive biomarkers for DTD:
- **Urinary GAG sulfation** profiling via chondroitin sulfate disaccharide HPLC after chondroitinase digestion, reporting undersulfation in DTD patients. (paganini2023identificationofpotential pages 1-3)
- **CXM (N-terminal collagen X fragment)** in dried blood spots, a “real-time marker of endochondral ossification and growth velocity,” reported lower-than-normal in most patients, with interpretation limited by strong age/sex/growth-velocity dependence. (paganini2023identificationofpotential pages 1-3)

These assays are positioned as practical tools to support future natural-history studies and clinical trials in DTD. (paganini2023identificationofpotential pages 1-3)

### 8.2 Targeted therapy and drug repurposing (2024)
Preclinical work in 2024 further operationalizes the UPR→FGFR3 model and evaluates FGFR inhibition:
- Genetic reduction of **Fgfr3** reduced pathway activity (p-ERK1/2 and p-STAT1 down) and partially alleviated phenotypes. (li2024targetingfgfr3signaling pages 11-13)
- Pharmacologic inhibition using **NVP-BGJ398** increased body size in Slc26a2 cKO mice at **49 days** with prolonged treatment. (li2024targetingfgfr3signaling pages 11-13)

Authors explicitly caution that dosing for oncologic indications is much higher than dosing considered for pediatric skeletal indications, emphasizing translational constraints. (li2024targetingfgfr3signaling pages 11-13)

### 8.3 Expanded tissue biology: tooth development and Wnt signaling (2024)
A 2024 Disease Models & Mechanisms paper extends SLC26A2 biology beyond cartilage into odontogenesis, reporting:
- significant reduction of sulfated GAG in upper molar tooth germs (**P<0.0001**) (yoshida2024slc26a2mediatedsulfatemetabolism pages 8-11)
- KEGG enrichment identifying **Wnt signaling** as the most significantly enriched among downregulated genes (yoshida2024slc26a2mediatedsulfatemetabolism pages 8-11)

This supports a broader framework in which sulfate transport can modulate developmental signaling programs in multiple tissues. (yoshida2024slc26a2mediatedsulfatemetabolism pages 8-11)

### 8.4 Human cellular mechanism in related SLC26A2 phenotypes (2024)
In 2024, human primary chondrocyte experiments in SLC26A2-related MED-4 showed mutant SLC26A2 mislocalization and altered differentiation markers (e.g., decreased COL10A1/RUNX2/MMP13, increased ACAN), supporting a direct influence of SLC26A2 variants on chondrocyte differentiation programs. (li2024biallelicvariantsin pages 1-2)

---

## 9) Current applications and real-world implementations

### 9.1 Diagnostic pathways
- Diagnosis integrates **clinical + radiographic findings** and is **confirmed with molecular genetic testing targeting SLC26A2**. (harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2, bondarenko2023slc26a2relateddiastrophic pages 1-2)

### 9.2 Prenatal screening/diagnosis
- “Prenatal diagnosis can be performed by ultrasound and genetic testing.” (harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2)
- In the Finnish cohort, **77% (10/13)** were suspected during pregnancy and **2** were confirmed prenatally from **amniotic fluid**. (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)
- Finnish incidence decreased over decades, likely due to increased prenatal diagnostics. (harkonen2021slc26a2associateddiastrophicdysplasia pages 5-7, harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2)

### 9.3 Clinical management
There is no established disease-modifying therapy; management is largely supportive, including physiotherapy and corrective orthopedic surgery. (harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2)

In the Finnish cohort, common surgeries included knee operations (n=9), cleft palate repair (n=8), club foot surgeries (n=7), and Achilles tenotomy (n=6). (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)

### 9.4 Biomarkers for monitoring and trial readiness
Urinary GAG sulfation and dried-blood-spot CXM are proposed as practical non-invasive biomarkers for DTD monitoring and future trials. (paganini2023identificationofpotential pages 1-3)

---

## 10) Relevant statistics and recent data

### Incidence/epidemiology
- Finland historically: DTD incidence reported as **1:22,000**, compared with estimated **1:100,000** in non-Finnish populations. (harkonen2021slc26a2associateddiastrophicdysplasia pages 5-7)
- Finnish registry trend: **10** children with DTD were born in **2000–2010** and **4** in **2010–2020**, attributed to increased prenatal diagnostics. (harkonen2021slc26a2associateddiastrophicdysplasia pages 5-7)

### Clinical severity (Finnish pediatric cohort)
- Median height SDS at last follow-up: girls with DTD **−5.5**, boys with DTD **−4.1**, boys with rMED **−2.9**. (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)
- Respiratory insufficiency after birth: **36% (5/14)**. (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5)

### Quantitative pathophysiology (mouse)
- Chondroitin sulfation at birth: **~0.7 sulfate/disaccharide (dtd)** vs **~0.9 (WT)** in proximal femur cartilage, with regional variation across zones. (mertz2012matrixdisruptionsgrowth pages 1-1)

---

## 11) Evidence-focused knowledge-base table

The following artifact organizes entities, mechanisms, biomarkers, and phenotypes for direct knowledge-base ingestion.

| Entity type | Identifier/ontology mapping | Role in pathophysiology | Key evidence | URL/DOI | Citation context ID(s) |
|---|---|---|---|---|---|
| Gene/Protein | **SLC26A2** (HGNC symbol); MONDO: **MONDO_0009107**; OMIM disease **222600**; gene OMIM **606718** | Plasma-membrane sulfate/chloride antiporter that supplies intracellular sulfate for proteoglycan sulfation; biallelic loss causes DTD spectrum. | Paganini et al., 2023: SLC26A2 “encodes for a transmembrane sulfate transporter”; severity correlates with “residual sulfate transport.” Silveira et al., 2022 identifies DTD OMIM #222600 and SLC26A2/DTDST OMIM #606718. | https://doi.org/10.1016/j.bone.2023.116838 ; https://doi.org/10.1159/000525020 | (paganini2023identificationofpotential pages 1-3, silveira2022slc26a2dtdstspectruma pages 1-2) |
| Pathway | GO ID not retrieved; sulfate transport / proteoglycan sulfation / PAPS-dependent sulfation | Reduced sulfate uptake lowers intracellular sulfate availability for sulfation, causing undersulfated cartilage proteoglycans. | Gramegna-Tota, 2023: impaired SLC26A2 function “producing reduced intracellular sulfate and undersulfation of proteoglycans (PGs).” Forlino et al., 2005: “Chondroitin sulfate proteoglycans were undersulfated.” | https://doi.org/10.1093/hmg/ddi079 | (gramegnatota2023chondrodysplasiascausedbya pages 42-46, forlino2005adiastrophicdysplasia pages 8-9) |
| Pathway | GO ID not retrieved; endochondral ossification | Undersulfated matrix disrupts growth-plate cartilage and endochondral bone formation. | Paganini et al., 2023: PG sulfation is essential for “normal cartilaginous matrix structure and endochondral ossification.” | https://doi.org/10.1016/j.bone.2023.116838 | (paganini2023identificationofpotential pages 1-3) |
| Pathway | GO ID not retrieved; **FGFR3 signaling** | In severe Slc26a2 deficiency, ATF6-dependent UPR increases FGFR3 signaling, suppressing cartilage growth and differentiation. | Zheng et al., 2019: ATF6 induces excessive FGFR3 expression; p-ERK1/2 and p-STAT1 are increased. Li et al., 2024: NVP-BGJ398 caused a “significant increase in body size” in Slc26a2 cKO mice. | https://doi.org/10.1016/j.ebiom.2019.01.010 ; https://doi.org/10.1016/j.jot.2023.09.003 | (zheng2019suppressinguprdependentoveractivation pages 6-8, li2024targetingfgfr3signaling pages 11-13) |
| Pathway | GO ID not retrieved; **UPR / ATF6 ER-stress pathway** | Collagen retention in chondrocytes triggers ER stress, with preferential ATF6 activation in severe disease models. | Zheng et al., 2019: “increased expression of ATF4, BIP, CHOP, ATF6 and XBP1” with preferential ATF6 nuclear localization. | https://doi.org/10.1016/j.ebiom.2019.01.010 | (zheng2019suppressinguprdependentoveractivation pages 6-8, zheng2019suppressinguprdependentoveractivation pages 1-2) |
| Pathway | GO ID not retrieved; **Indian hedgehog (Ihh) signaling** | Altered Ihh signaling contributes to reduced chondrocyte proliferation and growth-plate dysfunction in hypomorphic DTD models. | Gramegna-Tota, 2023: reduced proliferation is associated with “altered Indian hedgehog (Ihh) signaling.” | URL not retrieved | (gramegnatota2023chondrodysplasiascausedbyc pages 127-129) |
| Pathway | GO ID not retrieved; **cell-cycle regulation (p130/E2F)** | Reduced p130 phosphorylation causes G1 block and contributes to impaired proliferation of growth-plate chondrocytes. | Gramegna-Tota, 2023: reduced p130 phosphorylation affects E2F transcription factors and causes a “G1 phase block.” | URL not retrieved | (gramegnatota2023chondrodysplasiascausedbyc pages 127-129) |
| Pathway | GO ID not retrieved; **Wnt signaling** | Recent non-cartilage work suggests Slc26a2-dependent sulfate metabolism can modulate Wnt-linked differentiation programs. | Yoshida et al., 2024: KEGG analysis found Wnt signaling was the “most significantly enriched pathway among downregulated genes”; sulfated GAG reduction in upper molars was **P<0.0001**. | https://doi.org/10.1242/dmm.052107 | (yoshida2024slc26a2mediatedsulfatemetabolism pages 8-11) |
| Cell type | CL: chondrocyte ID not retrieved | Primary disease cell type; defective sulfate uptake alters proliferation, differentiation, matrix secretion, and survival responses. | Forlino et al., 2005: sulfate uptake impaired in chondrocytes; Zheng et al., 2019: intracellular retention of ColII/ColIX in slc26a2−/− chondrocytes. | https://doi.org/10.1093/hmg/ddi079 ; https://doi.org/10.1016/j.ebiom.2019.01.010 | (forlino2005adiastrophicdysplasia pages 1-2, zheng2019suppressinguprdependentoveractivation pages 6-8) |
| Cell type | CL ID not retrieved; hypertrophic chondrocyte | Terminal differentiation is delayed/perturbed, contributing to abnormal ossification and growth-plate maturation. | Forlino et al., 2005: few apoptotic hypertrophic chondrocytes at P21; Li et al., 2024 reports altered Col X and differentiation markers after FGFR3 targeting. | https://doi.org/10.1093/hmg/ddi079 ; https://doi.org/10.1016/j.jot.2023.09.003 | (forlino2005adiastrophicdysplasia pages 8-9, li2024targetingfgfr3signaling pages 11-13) |
| Cell type | CL ID not retrieved; osteoblast | Sulfate uptake is affected in osteoblasts, but major proteoglycan undersulfation is most evident in cartilage; bone remodeling changes are likely secondary to matrix defects. | Forlino et al., 2005: uptake impaired in osteoblasts; Gualeni et al., 2013: high osteoclast resorption/reduced osteoblast activity despite normal cell numbers. | https://doi.org/10.1093/hmg/ddi079 ; https://doi.org/10.1016/j.bone.2013.01.036 | (forlino2005adiastrophicdysplasia pages 1-2, gualeni2013alterationofproteoglycan pages 9-9) |
| Cell type | CL ID not retrieved; fibroblast | Useful diagnostic/functional cell type for demonstrating reduced sulfate uptake, though cartilage is most pathologically affected. | Paganini 2020 summary: “reduced sulfate uptake in fibroblasts”; Forlino et al., 2005 also notes impaired uptake in fibroblasts. | https://doi.org/10.3390/ijms21082710 ; https://doi.org/10.1093/hmg/ddi079 | (paganini2020skeletaldysplasiascaused pages 9-10, forlino2005adiastrophicdysplasia pages 1-2) |
| Tissue/Anatomy | UBERON ID not retrieved; cartilage | Principal affected tissue because cartilage ECM is rich in sulfated proteoglycans and highly dependent on sulfate flux. | Gramegna-Tota, 2023: significant PG undersulfation was detected “only in cartilage.” | URL not retrieved | (gramegnatota2023chondrodysplasiascausedbyc pages 127-129) |
| Tissue/Anatomy | UBERON ID not retrieved; growth plate cartilage | Regional undersulfation disrupts proliferation and matrix architecture in zones crucial for bone elongation. | Mertz et al., 2012: undersulfation was mild overall but strong in “narrow articular and growth plate regions crucial for bone development.” | https://doi.org/10.1074/jbc.m110.116467 | (mertz2012matrixdisruptionsgrowth pages 1-1, mertz2012matrixdisruptionsgrowth media e64dc09b) |
| Tissue/Anatomy | UBERON ID not retrieved; articular cartilage | Matrix abnormalities and collagen disorganization in the articular surface likely drive progressive degeneration with age. | Mertz et al., 2012: collagen orientation was reduced in the protective surface layer; articular cartilage “degrades with age.” | https://doi.org/10.1074/jbc.m110.116467 | (mertz2012matrixdisruptionsgrowth pages 1-1, mertz2012matrixdisruptionsgrowth media e64dc09b) |
| Tissue/Anatomy | UBERON ID not retrieved; bone / secondary ossification center | Delayed ossification and altered bone remodeling emerge downstream of abnormal cartilage matrix and growth-plate biology. | Forlino et al., 2005: “delayed secondary ossification center formation”; Gualeni et al., 2013: alteration of PG sulfation affects bone growth and remodeling. | https://doi.org/10.1093/hmg/ddi079 ; https://doi.org/10.1016/j.bone.2013.01.036 | (forlino2005adiastrophicdysplasia pages 1-2, gualeni2013alterationofproteoglycan pages 9-9) |
| Cellular component | GO ID not retrieved; plasma membrane | SLC26A2 acts at the cell membrane to import sulfate into target cells. | Paganini et al., 2023 and Paganini 2020 describe SLC26A2 as a “transmembrane sulfate transporter” / “Sulfate/chloride antiporter present on cell membrane.” | https://doi.org/10.1016/j.bone.2023.116838 ; https://doi.org/10.3390/ijms21082710 | (paganini2023identificationofpotential pages 1-3, paganini2020skeletaldysplasiascaused pages 9-10) |
| Cellular component | GO ID not retrieved; endoplasmic reticulum | Severe deficiency causes intracellular collagen retention, ER distension, and ER-stress signaling. | Zheng et al., 2019: “massive intracellular accumulation of matrix-containing vesicles, ER distension in chondrocytes.” | https://doi.org/10.1016/j.ebiom.2019.01.010 | (zheng2019suppressinguprdependentoveractivation pages 6-8) |
| Cellular component | GO ID not retrieved; extracellular matrix | Undersulfated PGs alter matrix composition, hydration, collagen organization, and tissue mechanics. | Gramegna-Tota, 2023: undersulfated PGs alter ECM “composition, architecture, signalling and mechanics”; Mertz et al., 2012 links undersulfation to collagen disorientation. | https://doi.org/10.1074/jbc.m110.116467 | (gramegnatota2023chondrodysplasiascausedbya pages 42-46, mertz2012matrixdisruptionsgrowth pages 1-1) |
| Chemical entity | CHEBI ID not retrieved; sulfate / inorganic sulfate | Limiting substrate whose defective uptake is the initiating biochemical lesion. | Gramegna-Tota, 2023 notes intracellular sulfate pool depends on extracellular uptake; Forlino et al., 2005: “sulfate uptake is impaired in dtd animals.” | https://doi.org/10.1093/hmg/ddi079 | (gramegnatota2023chondrodysplasiascausedbya pages 42-46, forlino2005adiastrophicdysplasia pages 8-9) |
| Chemical entity | CHEBI ID not retrieved; PAPS | Universal activated sulfate donor whose supply becomes limiting when intracellular sulfate is reduced. | Gramegna-Tota, 2023: insufficient intracellular sulfate “limits formation of PAPS, the universal sulfate donor.” | URL not retrieved | (gramegnatota2023chondrodysplasiascausedbya pages 42-46) |
| Chemical entity | CHEBI ID not retrieved; chondroitin sulfate / sulfated GAGs | Major matrix component whose undersulfation tracks with structural and biomechanical defects in cartilage. | Mertz et al., 2012: chondroitin sulfation about **~0.7 sulfate/disaccharide in dtd vs ~0.9 in wild type**; region-specific deficits mapped across cartilage. | https://doi.org/10.1074/jbc.m110.116467 | (mertz2012matrixdisruptionsgrowth pages 1-1, mertz2012matrixdisruptionsgrowth media e64dc09b) |
| Chemical entity | CHEBI ID not retrieved; **N-acetylcysteine (NAC)** | Experimental sulfate surrogate/thiol donor proposed to improve intracellular sulfate availability and proteoglycan sulfation. | Härkönen et al., 2021: “Dtd mice treated with NAC showed an increase in cartilage proteoglycan sulfation and improvement of the skeletal phenotype.” Li et al., 2024: NAC selected “as an alternative to intracellular sulfate.” | https://doi.org/10.3390/genes12050714 ; https://doi.org/10.1016/j.jot.2023.09.003 | (harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2, li2024targetingfgfr3signaling pages 11-13) |
| Chemical entity | CHEBI ID not retrieved; **NVP-BGJ398 / infigratinib** | Experimental FGFR inhibitor repurposed to suppress pathogenic FGFR3 overactivation in Slc26a2-deficient models. | Li et al., 2024: prolonged treatment led to a “significant increase in body size in Slc26a2 cKO mice at 49 days postnatally.” | https://doi.org/10.1016/j.jot.2023.09.003 | (li2024targetingfgfr3signaling pages 11-13) |
| Biomarker | ID not retrieved; urinary GAG sulfation / chondroitin sulfate disaccharides | Non-invasive readout of systemic proteoglycan undersulfation. | Paganini et al., 2023: “Undersulfation of urinary GAGs” measured by HPLC after chondroitinase digestion; both biomarkers judged “promising assays.” | https://doi.org/10.1016/j.bone.2023.116838 | (paganini2023identificationofpotential pages 1-3) |
| Biomarker | ID not retrieved; **CXM** (N-terminal collagen X fragment) | Candidate blood-spot biomarker of endochondral ossification and growth velocity in DTD. | Paganini et al., 2023: CXM is “a real-time marker of endochondral ossification and growth velocity”; most patients had “Lower than normal CXM levels.” | https://doi.org/10.1016/j.bone.2023.116838 | (paganini2023identificationofpotential pages 1-3) |
| Phenotype/Clinical | HP ID not retrieved; short-limb short stature / disproportionate short stature | Reflects chronically reduced endochondral growth from growth-plate dysfunction. | Härkönen et al., 2021: median height SDS at last follow-up was **−5.5** for girls and **−4.1** for boys with DTD. | https://doi.org/10.3390/genes12050714 | (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5) |
| Phenotype/Clinical | HP ID not retrieved; joint dysplasia / contractures | Matrix and growth-plate abnormalities alter joint shape and mobility from early development onward. | Bondarenko et al., 2023 describes “defective joint and skeletal development”; Härkönen et al., 2021 reports frequent knee/patellar problems and multiple knee surgeries. | https://doi.org/10.2478/bjmg-2022-0018 ; https://doi.org/10.3390/genes12050714 | (bondarenko2023slc26a2relateddiastrophic pages 1-2, harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5) |
| Phenotype/Clinical | HP ID not retrieved; spinal deformity (scoliosis/kyphosis) | Progressive vertebral and connective-tissue involvement follows abnormal cartilage/bone development. | Bondarenko et al., 2023 notes “progressive spinal deformity (scoliosis/kyphosis).” | https://doi.org/10.2478/bjmg-2022-0018 | (bondarenko2023slc26a2relateddiastrophic pages 1-2) |
| Phenotype/Clinical | HP ID not retrieved; ear swelling / malformed pinnae | Classic external ear phenotype in DTD, likely reflecting abnormal cartilage development outside the appendicular skeleton. | Bondarenko et al., 2023 mentions external ear/pinna abnormalities; DTD is historically characterized by cystic swelling of the external ear. | https://doi.org/10.2478/bjmg-2022-0018 | (bondarenko2023slc26a2relateddiastrophic pages 1-2) |
| Phenotype/Clinical | HP ID not retrieved; cleft palate | Craniofacial/cartilage developmental consequence common in clinical cohorts. | Härkönen et al., 2021: cleft palate in **64%** of cohort; cleft palate repair performed in **n=8**. | https://doi.org/10.3390/genes12050714 | (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5) |
| Phenotype/Clinical | HP ID not retrieved; respiratory insufficiency in neonates | Severe thoracic/airway consequences can complicate neonatal course in DTD. | Härkönen et al., 2021: respiratory insufficiency after birth in **36% (5/14)**, with three requiring intensive care. | https://doi.org/10.3390/genes12050714 | (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5) |
| Phenotype/Clinical | HP ID not retrieved; prenatal short limbs / skeletal abnormality on ultrasound | Real-world prenatal screening often detects DTD before birth. | Härkönen et al., 2021: **77% (10/13)** suspected prenatally; structural ultrasound showed short limbs in all 10 suspected pregnancies. | https://doi.org/10.3390/genes12050714 | (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5) |
| Phenotype/Clinical | HP ID not retrieved; genotype–phenotype continuum | Residual transporter activity modifies severity across ACG1B/AO2, DTD, and rMED. | Paganini et al., 2023: severity ranges from lethal forms to rMED and “correlates with the level of residual sulfate transport.” Silveira et al., 2022: R279W is mild in homozygosity and can rescue more severe alleles. | https://doi.org/10.1016/j.bone.2023.116838 ; https://doi.org/10.1159/000525020 | (paganini2023identificationofpotential pages 1-3, silveira2022slc26a2dtdstspectruma pages 7-8, silveira2022slc26a2dtdstspectruma pages 9-10) |


*Table: This table organizes key entities, mechanisms, biomarkers, and clinical phenotypes relevant to diastrophic dysplasia for a disease knowledge base. It links each item to ontology/identifier information where available, concise mechanistic roles, and directly cited supporting evidence.*

---

## 12) Notes on evidence limitations (PMID requirement)
The user requested PMIDs for mechanistic claims; however, the retrieved full-text excerpts in this run largely provide **DOIs and URLs but not PMIDs**. Mechanistic claims above are therefore cited to the retrieved document context IDs (as required by the toolchain) and can be cross-walked to PMIDs using the DOIs/metadata if needed. (paganini2023identificationofpotential pages 1-3, li2024targetingfgfr3signaling pages 11-13)

References

1. (paganini2023identificationofpotential pages 1-3): Chiara Paganini, Ricki S. Carroll, Chiara Gramegna Tota, Andrea J. Schelhaas, Alessandra Leone, Angela L. Duker, David A. O'Connell, Ryan F. Coghlan, Brian Johnstone, Carlos R. Ferreira, Sabrina Peressini, Riccardo Albertini, Antonella Forlino, Luisa Bonafé, Ana Belinda Campos-Xavier, Andrea Superti-Furga, Andreas Zankl, Antonio Rossi, and Michael B. Bober. Identification of potential non-invasive biomarkers in diastrophic dysplasia. Bone, 175:116838, Oct 2023. URL: https://doi.org/10.1016/j.bone.2023.116838, doi:10.1016/j.bone.2023.116838. This article has 5 citations and is from a domain leading peer-reviewed journal.

2. (silveira2022slc26a2dtdstspectruma pages 1-2): Cynthia Silveira, Karina da Costa Silveira, Maria D. Lacarrubba-Flores, Maurício T. Sakata, Silvia N. Carbognani, Juan Llerena Jr., Carolina A. Moreno, and Denise P. Cavalcanti. Slc26a2/dtdst spectrum: a cohort of 12 patients associated with a comprehensive review of the genotype-phenotype correlation. Molecular Syndromology, 13:485-495, Jun 2022. URL: https://doi.org/10.1159/000525020, doi:10.1159/000525020. This article has 10 citations and is from a peer-reviewed journal.

3. (gramegnatota2023chondrodysplasiascausedby pages 42-46): C GRAMEGNA-TOTA. Chondrodysplasias caused by defects in glycosaminoglycan biosynthesis: deep phenotyping and therapeutic approaches using in vitro and in vivo model. Unknown journal, 2023.

4. (gramegnatota2023chondrodysplasiascausedbya pages 42-46): C GRAMEGNA-TOTA. Chondrodysplasias caused by defects in glycosaminoglycan biosynthesis: deep phenotyping and therapeutic approaches using in vitro and in vivo model. Unknown journal, 2023.

5. (forlino2005adiastrophicdysplasia pages 8-9): A. Forlino, R. Piazza, C. Tiveron, S. Della Torre, L. Tatangelo, L. Bonafė, Benedetta Gualeni, A. Romano, Fabio Pecora, A. Superti-Furga, G. Cetta, and A. Rossi. A diastrophic dysplasia sulfate transporter (slc26a2) mutant mouse: morphological and biochemical characterization of the resulting chondrodysplasia phenotype. Human molecular genetics, 14 6:859-71, Mar 2005. URL: https://doi.org/10.1093/hmg/ddi079, doi:10.1093/hmg/ddi079. This article has 166 citations and is from a domain leading peer-reviewed journal.

6. (mertz2012matrixdisruptionsgrowth pages 1-1): Edward L. Mertz, Marcella Facchini, Anna T. Pham, Benedetta Gualeni, Fabio De Leonardis, Antonio Rossi, and Antonella Forlino. Matrix disruptions, growth, and degradation of cartilage with impaired sulfation. Journal of Biological Chemistry, 287:22030-22042, Jun 2012. URL: https://doi.org/10.1074/jbc.m110.116467, doi:10.1074/jbc.m110.116467. This article has 30 citations and is from a domain leading peer-reviewed journal.

7. (mertz2012matrixdisruptionsgrowth media e64dc09b): Edward L. Mertz, Marcella Facchini, Anna T. Pham, Benedetta Gualeni, Fabio De Leonardis, Antonio Rossi, and Antonella Forlino. Matrix disruptions, growth, and degradation of cartilage with impaired sulfation. Journal of Biological Chemistry, 287:22030-22042, Jun 2012. URL: https://doi.org/10.1074/jbc.m110.116467, doi:10.1074/jbc.m110.116467. This article has 30 citations and is from a domain leading peer-reviewed journal.

8. (forlino2005adiastrophicdysplasia pages 1-2): A. Forlino, R. Piazza, C. Tiveron, S. Della Torre, L. Tatangelo, L. Bonafė, Benedetta Gualeni, A. Romano, Fabio Pecora, A. Superti-Furga, G. Cetta, and A. Rossi. A diastrophic dysplasia sulfate transporter (slc26a2) mutant mouse: morphological and biochemical characterization of the resulting chondrodysplasia phenotype. Human molecular genetics, 14 6:859-71, Mar 2005. URL: https://doi.org/10.1093/hmg/ddi079, doi:10.1093/hmg/ddi079. This article has 166 citations and is from a domain leading peer-reviewed journal.

9. (gramegnatota2023chondrodysplasiascausedbyc pages 127-129): C GRAMEGNA-TOTA. Chondrodysplasias caused by defects in glycosaminoglycan biosynthesis: deep phenotyping and therapeutic approaches using in vitro and in vivo model. Unknown journal, 2023.

10. (zheng2019suppressinguprdependentoveractivation pages 6-8): Chao Zheng, Xisheng Lin, Xiaolong Xu, Cheng Wang, Jinru Zhou, Bo Gao, Jingzhou Fan, Weiguang Lu, Yaqian Hu, Qiang Jie, Zhuojing Luo, and Liu Yang. Suppressing upr-dependent overactivation of fgfr3 signaling ameliorates slc26a2-deficient chondrodysplasias. EBioMedicine, 40:695-709, Feb 2019. URL: https://doi.org/10.1016/j.ebiom.2019.01.010, doi:10.1016/j.ebiom.2019.01.010. This article has 44 citations and is from a peer-reviewed journal.

11. (zheng2019suppressinguprdependentoveractivation pages 1-2): Chao Zheng, Xisheng Lin, Xiaolong Xu, Cheng Wang, Jinru Zhou, Bo Gao, Jingzhou Fan, Weiguang Lu, Yaqian Hu, Qiang Jie, Zhuojing Luo, and Liu Yang. Suppressing upr-dependent overactivation of fgfr3 signaling ameliorates slc26a2-deficient chondrodysplasias. EBioMedicine, 40:695-709, Feb 2019. URL: https://doi.org/10.1016/j.ebiom.2019.01.010, doi:10.1016/j.ebiom.2019.01.010. This article has 44 citations and is from a peer-reviewed journal.

12. (li2024targetingfgfr3signaling pages 11-13): Pan Li, Dong Wang, Weiguang Lu, Xin He, Jingyan Hu, Haitao Yun, Chengxiang Zhao, Liu Yang, Qiang Jie, and Zhuojing Luo. Targeting fgfr3 signaling and drug repurposing for the treatment of slc26a2-related chondrodysplasia in mouse model. Journal of Orthopaedic Translation, 44:88-101, Jan 2024. URL: https://doi.org/10.1016/j.jot.2023.09.003, doi:10.1016/j.jot.2023.09.003. This article has 4 citations.

13. (harkonen2021slc26a2associateddiastrophicdysplasia pages 1-2): Helmi Härkönen, Petra Loid, and Outi Mäkitie. Slc26a2-associated diastrophic dysplasia and rmed—clinical features in affected finnish children and review of the literature. Genes, 12:714, May 2021. URL: https://doi.org/10.3390/genes12050714, doi:10.3390/genes12050714. This article has 34 citations.

14. (paganini2020skeletaldysplasiascaused pages 9-10): Chiara Paganini, Chiara Gramegna Tota, Andrea Superti-Furga, and Antonio Rossi. Skeletal dysplasias caused by sulfation defects. International Journal of Molecular Sciences, 21:2710, Apr 2020. URL: https://doi.org/10.3390/ijms21082710, doi:10.3390/ijms21082710. This article has 38 citations.

15. (bondarenko2023slc26a2relateddiastrophic pages 1-2): M. Bondarenko, I. Haiboniuk, I. Solovei, Y. Shargorodska, and H. Makukh. Slc26a2 related diastrophic dysplasia in 42-years ukrainian women. Balkan Journal of Medical Genetics : BJMG, 25:83-90, Dec 2023. URL: https://doi.org/10.2478/bjmg-2022-0018, doi:10.2478/bjmg-2022-0018. This article has 3 citations.

16. (harkonen2021slc26a2associateddiastrophicdysplasia pages 4-5): Helmi Härkönen, Petra Loid, and Outi Mäkitie. Slc26a2-associated diastrophic dysplasia and rmed—clinical features in affected finnish children and review of the literature. Genes, 12:714, May 2021. URL: https://doi.org/10.3390/genes12050714, doi:10.3390/genes12050714. This article has 34 citations.

17. (silveira2022slc26a2dtdstspectruma pages 9-10): Cynthia Silveira, Karina da Costa Silveira, Maria D. Lacarrubba-Flores, Maurício T. Sakata, Silvia N. Carbognani, Juan Llerena Jr., Carolina A. Moreno, and Denise P. Cavalcanti. Slc26a2/dtdst spectrum: a cohort of 12 patients associated with a comprehensive review of the genotype-phenotype correlation. Molecular Syndromology, 13:485-495, Jun 2022. URL: https://doi.org/10.1159/000525020, doi:10.1159/000525020. This article has 10 citations and is from a peer-reviewed journal.

18. (harkonen2021slc26a2associateddiastrophicdysplasia pages 5-7): Helmi Härkönen, Petra Loid, and Outi Mäkitie. Slc26a2-associated diastrophic dysplasia and rmed—clinical features in affected finnish children and review of the literature. Genes, 12:714, May 2021. URL: https://doi.org/10.3390/genes12050714, doi:10.3390/genes12050714. This article has 34 citations.

19. (silveira2022slc26a2dtdstspectruma pages 7-8): Cynthia Silveira, Karina da Costa Silveira, Maria D. Lacarrubba-Flores, Maurício T. Sakata, Silvia N. Carbognani, Juan Llerena Jr., Carolina A. Moreno, and Denise P. Cavalcanti. Slc26a2/dtdst spectrum: a cohort of 12 patients associated with a comprehensive review of the genotype-phenotype correlation. Molecular Syndromology, 13:485-495, Jun 2022. URL: https://doi.org/10.1159/000525020, doi:10.1159/000525020. This article has 10 citations and is from a peer-reviewed journal.

20. (yoshida2024slc26a2mediatedsulfatemetabolism pages 8-11): Yuka Yoshida, Toshihiro Inubushi, Mika Yokoyama, Priyanka Nag, Jun-ichi Sasaki, Ayaka Oka, Tomoya Murotani, Renshiro Kani, Yuki Shiraishi, Hiroshi Kurosaka, Yoshifumi Takahata, Riko Nishimura, Satoshi Imazato, Petros Papagerakis, and Takashi Yamashiro. <i>slc26a2</i>-mediated sulfate metabolism is important in tooth development. Disease Models &amp; Mechanisms, Dec 2024. URL: https://doi.org/10.1242/dmm.052107, doi:10.1242/dmm.052107. This article has 1 citations and is from a domain leading peer-reviewed journal.

21. (li2024biallelicvariantsin pages 1-2): Shan Li, Yueyang Sheng, Xinyu Wang, Qianqian Wang, Ying Wang, Yanzhuo Zhang, Chengai Wu, and Xu Jiang. Biallelic variants in slc26a2 cause multiple epiphyseal dysplasia-4 by disturbing chondrocyte homeostasis. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03228-4, doi:10.1186/s13023-024-03228-4. This article has 4 citations and is from a peer-reviewed journal.

22. (gualeni2013alterationofproteoglycan pages 9-9): Benedetta Gualeni, Marie-Christine de Vernejoul, Caroline Marty-Morieux, Fabio De Leonardis, Marco Franchi, Luca Monti, Antonella Forlino, Pascal Houillier, Antonio Rossi, and Valerie Geoffroy. Alteration of proteoglycan sulfation affects bone growth and remodeling. Bone, 54:83-91, May 2013. URL: https://doi.org/10.1016/j.bone.2013.01.036, doi:10.1016/j.bone.2013.01.036. This article has 53 citations and is from a domain leading peer-reviewed journal.