---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-15T21:50:23.296270'
end_time: '2026-02-15T22:01:54.835374'
duration_seconds: 691.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Spherocytosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hereditary Spherocytosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hereditary Spherocytosis**.
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
- **Disease Name:** Hereditary Spherocytosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hereditary Spherocytosis**.
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


## Comprehensive research report: Hereditary spherocytosis (HS) pathophysiology (Mendelian)

### Disease identifiers
Hereditary spherocytosis is represented in Open Targets as **MONDO:0019350** (“hereditary spherocytosis”). (boesveld2023genotypetophenotypecorrelationsin pages 6-9)

---

## 1) Key concepts and definitions (current understanding)

### Definition
HS is an inherited red blood cell (RBC) membrane disorder characterized by decreased RBC deformability and formation of spherocytes that are preferentially cleared in the spleen, producing chronic extravascular hemolysis. HS is described as “a disorder of reduced RBC deformability” due to pathogenic variants in membrane-skeleton and anchoring-complex genes. (boesveld2023genotypetophenotypecorrelationsin pages 6-9)

### Core mechanical concept: surface area loss → spherical shape → splenic clearance
Multiple contemporary sources converge on a “vertical linkage” failure model in which weakened connections between the lipid bilayer and cytoskeleton cause **microvesiculation** and **loss of membrane surface area**, reducing the surface-area-to-volume ratio, creating rigid spherocytes that cannot traverse splenic microcirculation efficiently. HS membrane instability is described as producing “a decreased surface/volume ratio, a decreased deformability and in fine in RBC sequestration in the splenic cords of the red pulp.” (evrard2024intragenicdeletionsin pages 1-3)

Panarach et al. similarly describe that deficiency/dysfunction of cytoskeleton proteins “disrupt[s] the linkage between the phospholipid bilayer and cytoskeleton, altering the red blood cells’ surface area-to-volume ratio,” yielding “decreased membrane mechanical stability and cellular deformability,” with selective trapping and destruction “by splenic macrophages.” (panarach2024identificationandfunctional pages 1-2)

### Extravascular hemolysis and macrophage-mediated clearance
A recent genotype–phenotype review describes the downstream mechanism as “extravascular haemolysis due to entrapment in the spleen and phagocytosis by resident macrophages.” (boesveld2023genotypetophenotypecorrelationsin pages 6-9)

---

## 2) Core pathophysiology (molecular pathways, cellular processes)

### 2.1 Primary pathophysiological mechanisms
**(A) Membrane–cytoskeleton uncoupling and instability**
HS is predominantly caused by mutations affecting RBC cytoskeleton proteins and anchoring complexes, destabilizing vertical linkages and leading to progressive membrane surface loss and reduced deformability. (boesveld2023genotypetophenotypecorrelationsin pages 6-9, panarach2024identificationandfunctional pages 1-2, evrard2024intragenicdeletionsin pages 1-3)

**(B) Microparticle (microvesicle) release**
Weakened vertical linkages “may contribute to the release of microparticles (MPs)” in HS, consistent with vesiculation-mediated surface loss. (panarach2024identificationandfunctional pages 1-2)

**(C) Splenic filtration as a central amplifier of disease**
Splenic cords and macrophages create a mechanical/immune clearance bottleneck; poorly deformable spherocytes undergo trapping and phagocytosis, driving anemia and hyperbilirubinemia. (boesveld2023genotypetophenotypecorrelationsin pages 6-9, evrard2024intragenicdeletionsin pages 1-3)

### 2.2 Ion transport and hydration as contributors/modifiers
While the canonical model is structural, modern work emphasizes additional ion-homeostasis perturbations in many HS patients. A recent mechanistic synthesis reports HS RBCs show “increased passive Na+ and K+ permeability” with compensatory Na+/K+ ATPase activity, but still “undergo net Na+ gain and K+ loss, leading to cellular dehydration and the characteristically elevated MCHC,” contributing to reduced deformability and hemolysis; abnormal permeability is estimated in **~40–70%** of patients in cited literature. (vivescorrons2026hereditaryspherocytosislinking pages 3-4)

Mechanosensitive and Ca2+-activated potassium channels are implicated as phenotype modifiers: PIEZO1 and KCNN4 (Gardos channel) gain-of-function variants can shift patients toward dehydrated phenotypes and complicate differential diagnosis with xerocytosis-like profiles on osmotic gradient ektacytometry. (vivescorrons2026hereditaryspherocytosislinking pages 8-9, vivescorrons2026hereditaryspherocytosislinking pages 11-12)

---

## 3) Key molecular players (genes/proteins, chemicals, cells, anatomy)

### 3.1 Causal genes/proteins (core HS genes)
Recent literature and cohort studies consistently identify five principal HS genes:
- **ANK1** (ankyrin-1) (boesveld2023genotypetophenotypecorrelationsin pages 6-9, panarach2024identificationandfunctional pages 1-2)
- **SPTB** (β-spectrin) (boesveld2023genotypetophenotypecorrelationsin pages 6-9, evrard2024intragenicdeletionsin pages 1-3)
- **SPTA1** (α-spectrin) (boesveld2023genotypetophenotypecorrelationsin pages 6-9)
- **SLC4A1** (band 3 / AE1) (boesveld2023genotypetophenotypecorrelationsin pages 6-9)
- **EPB42** (protein 4.2) (boesveld2023genotypetophenotypecorrelationsin pages 6-9)

These proteins organize the RBC membrane-skeleton and anchoring complexes; disruption destabilizes membrane cohesion and deformability. (boesveld2023genotypetophenotypecorrelationsin pages 6-9, panarach2024identificationandfunctional pages 1-2)

**Notable recent molecular genetics development (2024):**
Evrard et al. (British Journal of Haematology, **Aug 2024**, https://doi.org/10.1111/bjh.19692) highlight that **intragenic deletions in SPTB** can be a substantial subset of SPTB molecular defects (“up to 20%” in their series), emphasizing the need for CNV-aware molecular pipelines. (evrard2024intragenicdeletionsin pages 1-3)

### 3.2 Modifiers / related channel genes affecting hydration and deformability
- **PIEZO1** (mechanosensitive cation channel; modifier) (vivescorrons2026hereditaryspherocytosislinking pages 8-9, vivescorrons2026hereditaryspherocytosislinking pages 11-12)
- **KCNN4** (Gardos channel; modifier) (vivescorrons2026hereditaryspherocytosislinking pages 8-9, vivescorrons2026hereditaryspherocytosislinking pages 11-12)

### 3.3 Cell types (Cell Ontology, CL)
- Primary affected cell type: **erythrocyte** (RBC) (CL term suggestion: *erythrocyte*) (boesveld2023genotypetophenotypecorrelationsin pages 6-9, panarach2024identificationandfunctional pages 1-2)
- Key effector immune cell: **splenic macrophage** (CL term suggestion: *macrophage*) driving phagocytosis in extravascular hemolysis (boesveld2023genotypetophenotypecorrelationsin pages 6-9, panarach2024identificationandfunctional pages 1-2)

### 3.4 Anatomical locations (UBERON)
- **Spleen red pulp / splenic cords** are central to sequestration and clearance (UBERON term suggestions: *spleen*, *red pulp of spleen*) (evrard2024intragenicdeletionsin pages 1-3)
- **Gallbladder** is involved in pigment gallstone complications in chronic hemolysis (UBERON term suggestion: *gallbladder*) (boaro2023hematologicalcharacteristicsand pages 1-2)

### 3.5 Chemical entities (CHEBI) relevant to diagnosis/management
- **Eosin-5’-maleimide (EMA)** dye used in flow cytometry EMA binding test (CHEBI term suggestion: *eosin-5-maleimide*) (boaro2023hematologicalcharacteristicsand pages 2-3, beltran2024flowcytometryas pages 2-4)
- **Sodium chloride (NaCl)** in osmotic fragility testing and osmotic-gradient protocols (CHEBI: sodium chloride) (hauser2023hereditaryspherocytosiscan pages 5-7)

---

## 4) Biological processes (GO) and cellular components (GO-CC) disrupted

### 4.1 Biological processes (GO) disrupted (ontology-ready suggestions)
Based on the extracted mechanisms, HS disrupts:
- **Erythrocyte morphology and deformability regulation** (spherocyte formation due to reduced S/V ratio) (boesveld2023genotypetophenotypecorrelationsin pages 6-9, evrard2024intragenicdeletionsin pages 1-3)
- **Membrane organization / vesicle-mediated membrane remodeling** (microvesiculation / microparticle release) (panarach2024identificationandfunctional pages 1-2)
- **Macrophage-mediated phagocytosis of erythrocytes** / extravascular hemolysis (boesveld2023genotypetophenotypecorrelationsin pages 6-9)
- **Ion transport / cellular potassium ion homeostasis / sodium ion homeostasis** contributing to dehydration and high MCHC (vivescorrons2026hereditaryspherocytosislinking pages 3-4)

### 4.2 Cellular components (GO-CC) (ontology-ready suggestions)
Key processes occur at:
- **Plasma membrane** and **membrane skeleton (submembranous cytoskeleton)** (vertical linkage between phospholipid bilayer and cytoskeleton) (panarach2024identificationandfunctional pages 1-2)
- **Spectrin-based membrane skeleton** / anchoring complexes involving ankyrin, band 3, spectrins (boesveld2023genotypetophenotypecorrelationsin pages 6-9)

---

## 5) Disease progression (sequence of events)

1. **Germline pathogenic variant** in a membrane-skeleton gene (e.g., ANK1, SPTB, SLC4A1, SPTA1, EPB42) alters abundance/structure of key components. (boesveld2023genotypetophenotypecorrelationsin pages 6-9, panarach2024identificationandfunctional pages 1-2)
2. **Vertical linkage weakening** between lipid bilayer and cytoskeleton reduces membrane mechanical stability. (panarach2024identificationandfunctional pages 1-2)
3. **Microvesiculation / microparticle release** causes membrane surface loss, lowering surface-area-to-volume ratio and producing rigid spherocytes. (panarach2024identificationandfunctional pages 1-2, evrard2024intragenicdeletionsin pages 1-3)
4. **Reduced deformability** leads to poor passage through splenic microarchitecture, causing sequestration in splenic cords/red pulp. (evrard2024intragenicdeletionsin pages 1-3)
5. **Extravascular hemolysis**: spherocytes undergo “phagocytosis by resident macrophages,” producing chronic hemolytic anemia and downstream bilirubin burden. (boesveld2023genotypetophenotypecorrelationsin pages 6-9)
6. **Complications over time**: pigment gallstones and hemolytic/aplastic crises can occur; clinical severity varies widely by genotype and modifiers (including ion-transport effects). (evrard2024intragenicdeletionsin pages 1-3, boaro2023hematologicalcharacteristicsand pages 1-2)

---

## 6) Phenotypic manifestations (HP) and mechanistic links

Ontology-ready phenotype suggestions (Human Phenotype Ontology, HP) consistent with the evidence:
- **Spherocytosis** (HP: *Spherocytosis*) due to reduced S/V ratio and cytoskeletal instability (panarach2024identificationandfunctional pages 1-2, evrard2024intragenicdeletionsin pages 1-3)
- **Hemolytic anemia** (HP: *Hemolytic anemia*) due to splenic trapping and macrophage clearance (boesveld2023genotypetophenotypecorrelationsin pages 6-9, panarach2024identificationandfunctional pages 1-2)
- **Jaundice** (HP: *Jaundice*) and **splenomegaly** (HP: *Splenomegaly*) reported as common clinical features in genetic series (evrard2024intragenicdeletionsin pages 1-3)
- **Cholelithiasis / gallstones** (HP: *Cholelithiasis*) as a common complication in pediatric cohorts (boaro2023hematologicalcharacteristicsand pages 1-2)
- **Aplastic crisis** (HP: *Aplastic crisis*) noted as a complication in molecular diagnostic series and review discussions (hauser2023hereditaryspherocytosiscan pages 5-7)

Mechanistic coupling: decreased deformability and splenic clearance explain anemia/splenomegaly, while chronic hemolysis increases bilirubin turnover, predisposing to pigment gallstones. (boesveld2023genotypetophenotypecorrelationsin pages 6-9, boaro2023hematologicalcharacteristicsand pages 1-2)

---

## 7) Recent developments and latest research (prioritize 2023–2024)

### 7.1 Quantifying hemolysis using RBC lifespan (2023)
Shi et al. (BMC Genomics, **Jun 2023**, https://doi.org/10.1186/s12864-023-09364-8) combined NGS with Levitt’s CO breath test in **23 HS patients**, reporting **median RBC lifespan 14 (8–48) days** and providing gene distribution (8 ANK1, 9 SPTB, 5 SLC4A1, 1 SPTA1). They found no statistically significant correlation between genotype class and RBC lifespan in this small cohort. (shi2023genotypedegreeofhemolysis pages 1-2)

### 7.2 Molecular diagnostics: five-gene NGS panel performance (2023)
Häuser et al. (International Journal of Molecular Sciences, **Nov 2023**, https://doi.org/10.3390/ijms242317021) evaluated whether a 5-gene NGS approach could replace functional testing; among genetically tested suspected HS patients (n=17), they report **100% sensitivity (95% CI 81.5–100.0%)**, and conclude that “the combination of medical history, basic laboratory parameters, and an NGS panel with five genes is sufficient for diagnosis in most cases.” (hauser2023hereditaryspherocytosiscan pages 1-2)

### 7.3 Hepatobiliary complications and care pathways in pediatrics (2023)
Boaro et al. (Frontiers in Pediatrics, **Oct 2023**, https://doi.org/10.3389/fped.2023.1269645) report gallstones in **16/40 (40%)** children undergoing ultrasound surveillance, with higher hemolytic crises and parvovirus infections among those with stones (53.6% vs 26.1% and 63.6% vs 28.6%). (boaro2023hematologicalcharacteristicsand pages 1-2)

### 7.4 CNVs in SPTB as an under-recognized mechanism (2024)
Evrard et al. (British Journal of Haematology, **Aug 2024**, https://doi.org/10.1111/bjh.19692) describe intragenic deletions in **SPTB** associated with HS and report that such deletions represented “up to 20% of molecular defects found in the SPTB gene” in their series, reinforcing the need for CNV-sensitive molecular methods. (evrard2024intragenicdeletionsin pages 1-3)

### 7.5 Expanding access to functional diagnostics (2024)
Beltrán et al. (Biomedicines, **Jul 2024**, https://doi.org/10.3390/biomedicines12071607) address limited access to osmotic gradient ektacytometry by developing a **flow-cytometry-based osmotic method**. In the pediatric group, they report **AUC 1.0 (100% sensitivity, 93.3% specificity)**, and in adults **AUC 0.98 (80% sensitivity, 90.9% specificity)** for discriminating HS patients from controls using an iso-osmolar assessment point. (vivescorrons2026hereditaryspherocytosislinking pages 1-3)

---

## 8) Current applications and real-world implementations

### 8.1 Diagnostic testing in practice
A real-world pediatric center experience shows reliance on confirmatory tests such as **osmotic fragility testing (OFT)** and **EMA binding**. In Boaro et al., OFT was performed in 32 patients (26 positive) and EMA binding in 28 (27 positive). (boaro2023hematologicalcharacteristicsand pages 3-5)

Ektacytometry is described as a “gold standard” deformability test but is often not widely available, motivating alternative implementations such as flow-cytometric osmotic profiling and more NGS-first workflows. (boaro2023hematologicalcharacteristicsand pages 2-3, beltran2024flowcytometryas pages 2-4)

### 8.2 Molecular diagnosis workflows
NGS panels targeting the five main HS genes (ANK1, EPB42, SLC4A1, SPTA1, SPTB) can have high diagnostic sensitivity in selected cohorts and are particularly practical in pediatrics due to low blood volume requirements and sample stability. (hauser2023hereditaryspherocytosiscan pages 1-2)

### 8.3 Management and monitoring implementations
Boaro et al. recommend longitudinal follow-up including labs and ultrasound surveillance, with cholecystectomy for symptomatic gallstones and careful consideration of splenectomy; they note annual ultrasound after age 5 years in their institutional practice. (boaro2023hematologicalcharacteristicsand pages 2-3)

---

## 9) Expert opinion and analysis (authoritative synthesis)

**Conceptual consensus:** Contemporary reviews emphasize HS as primarily a membrane-skeleton disorder with splenic clearance as the proximate cause of anemia, but they increasingly highlight integrated molecular-functional diagnostics (NGS + functional deformability assays) to address heterogeneity and overlap with related membranopathies. (boesveld2023genotypetophenotypecorrelationsin pages 6-9, vivescorrons2026hereditaryspherocytosislinking pages 11-12)

**Precision hematology direction:** The ion-transport synthesis argues HS is multifactorial in many individuals, where ion homeostasis defects (including PIEZO1/KCNN4-driven dehydration) can modulate deformability and may influence management decisions (e.g., avoiding splenectomy in dehydrating channelopathies). (vivescorrons2026hereditaryspherocytosislinking pages 11-12)

---

## 10) Evidence items (mechanistic + numeric), with publication dates and URLs

1. **Boaro et al.** Frontiers in Pediatrics. **2023-10**. “Hematological characteristics and hepatobiliary complications of hereditary spherocytosis…” https://doi.org/10.3389/fped.2023.1269645 — Gallstones 16/40 (40%); OFT/EMA real-world testing uptake and outcomes. (boaro2023hematologicalcharacteristicsand pages 1-2, boaro2023hematologicalcharacteristicsand pages 3-5)
2. **Shi et al.** BMC Genomics. **2023-06**. “Genotype-degree of hemolysis correlation in hereditary spherocytosis.” https://doi.org/10.1186/s12864-023-09364-8 — RBC lifespan median 14 (8–48) days; gene distribution in n=23. (shi2023genotypedegreeofhemolysis pages 1-2)
3. **Häuser et al.** Int J Mol Sci. **2023-11**. “Hereditary Spherocytosis: Can NGS… replace functional investigations?” https://doi.org/10.3390/ijms242317021 — 5-gene NGS sensitivity 100% (95% CI 81.5–100.0%); de novo example. (hauser2023hereditaryspherocytosiscan pages 1-2, hauser2023hereditaryspherocytosiscan pages 5-7)
4. **Panarach et al.** Scientific Reports. **2024-11**. “Identification and functional analysis of novel SPTB and ANK1 mutations…” https://doi.org/10.1038/s41598-024-78622-w — Structural linkage disruption, decreased S/V ratio, splenic macrophage clearance; microparticles. (panarach2024identificationandfunctional pages 1-2)
5. **Evrard et al.** British Journal of Haematology. **2024-08**. “Intragenic deletions in SPTB…” https://doi.org/10.1111/bjh.19692 — Mechanism to splenic sequestration; CNV contribution up to 20% of SPTB molecular defects in series. (evrard2024intragenicdeletionsin pages 1-3)
6. **Beltrán et al.** Biomedicines. **2024-07**. “Flow cytometry as a new accessible method…” https://doi.org/10.3390/biomedicines12071607 — Alternative diagnostic osmotic profiling; sensitivity/specificity/AUC in small cohort. (beltran2024flowcytometryas pages 2-4)

---

## Limitations of this extraction
The provided full-text slices did not include PubMed identifiers (PMIDs) directly. Therefore, evidence is linked using **DOIs and URLs** available in the extracted text, which are sufficient for unambiguous retrieval. (shi2023genotypedegreeofhemolysis pages 1-2, hauser2023hereditaryspherocytosiscan pages 1-2, boaro2023hematologicalcharacteristicsand pages 1-2)


References

1. (boesveld2023genotypetophenotypecorrelationsin pages 6-9): M Boesveld. Genotype-to-phenotype correlations in hereditary spherocytosis. Unknown journal, 2023.

2. (evrard2024intragenicdeletionsin pages 1-3): Ophélie Evrard, Alexis Billes, Catherine Badens, Estelle Cadet, Lamisse Mansour‐Hendili, Kahia Messaoudi, Valérie Li Thiao Te, Philippe Joly, Caroline Favennec, Guillaume Jedraszak, Céline Renoux, and Loïc Garçon. Intragenic deletions in sptb are associated with hereditary spherocytosis: series of 12 cases. British Journal of Haematology, Aug 2024. URL: https://doi.org/10.1111/bjh.19692, doi:10.1111/bjh.19692. This article has 2 citations and is from a domain leading peer-reviewed journal.

3. (panarach2024identificationandfunctional pages 1-2): Charuwan Panarach, Chaiwat Netsawang, Issarang Nuchprayoon, and Kamonlak Leecharoenkiat. Identification and functional analysis of novel sptb and ank1 mutations in hereditary spherocytosis patients. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78622-w, doi:10.1038/s41598-024-78622-w. This article has 5 citations and is from a peer-reviewed journal.

4. (vivescorrons2026hereditaryspherocytosislinking pages 3-4): Joan Lluís Vives-Corrons and Elena Krishnevskaya. Hereditary spherocytosis: linking ion transport defects to osmotic gradient ektacytometry profiles—a review. International Journal of Molecular Sciences, 27:721, Jan 2026. URL: https://doi.org/10.3390/ijms27020721, doi:10.3390/ijms27020721. This article has 0 citations.

5. (vivescorrons2026hereditaryspherocytosislinking pages 8-9): Joan Lluís Vives-Corrons and Elena Krishnevskaya. Hereditary spherocytosis: linking ion transport defects to osmotic gradient ektacytometry profiles—a review. International Journal of Molecular Sciences, 27:721, Jan 2026. URL: https://doi.org/10.3390/ijms27020721, doi:10.3390/ijms27020721. This article has 0 citations.

6. (vivescorrons2026hereditaryspherocytosislinking pages 11-12): Joan Lluís Vives-Corrons and Elena Krishnevskaya. Hereditary spherocytosis: linking ion transport defects to osmotic gradient ektacytometry profiles—a review. International Journal of Molecular Sciences, 27:721, Jan 2026. URL: https://doi.org/10.3390/ijms27020721, doi:10.3390/ijms27020721. This article has 0 citations.

7. (boaro2023hematologicalcharacteristicsand pages 1-2): Maria Paola Boaro, Giulia Reggiani, Mirco D’Agnolo, Vania Munaretto, Francesco Pozzebon, Roberta Trapanese, Maddalena Martella, and Raffaella Colombatti. Hematological characteristics and hepatobiliary complications of hereditary spherocytosis in a tertiary care pediatric center: optimizing diagnosis and care through local and international networks. Frontiers in Pediatrics, Oct 2023. URL: https://doi.org/10.3389/fped.2023.1269645, doi:10.3389/fped.2023.1269645. This article has 3 citations.

8. (boaro2023hematologicalcharacteristicsand pages 2-3): Maria Paola Boaro, Giulia Reggiani, Mirco D’Agnolo, Vania Munaretto, Francesco Pozzebon, Roberta Trapanese, Maddalena Martella, and Raffaella Colombatti. Hematological characteristics and hepatobiliary complications of hereditary spherocytosis in a tertiary care pediatric center: optimizing diagnosis and care through local and international networks. Frontiers in Pediatrics, Oct 2023. URL: https://doi.org/10.3389/fped.2023.1269645, doi:10.3389/fped.2023.1269645. This article has 3 citations.

9. (beltran2024flowcytometryas pages 2-4): Asunción Beltrán, María Sánchez-Villalobos, Eduardo Salido, Carmen Algueró, Eulalia Campos, Ana Belén Pérez-Oliva, Miguel Blanquer, and José M. Moraleda. Flow cytometry as a new accessible method to evaluate diagnostic osmotic changes in patients with red blood cell membrane defects. Biomedicines, 12:1607, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071607, doi:10.3390/biomedicines12071607. This article has 4 citations.

10. (hauser2023hereditaryspherocytosiscan pages 5-7): Friederike Häuser, Heidi Rossmann, Anke Adenaeuer, Annette Shrestha, Dana Marandiuc, Claudia Paret, Jörg Faber, Karl J. Lackner, Bernhard Lämmle, and Olaf Beck. Hereditary spherocytosis: can next-generation sequencing of the five most frequently affected genes replace time-consuming functional investigations? International Journal of Molecular Sciences, 24:17021, Nov 2023. URL: https://doi.org/10.3390/ijms242317021, doi:10.3390/ijms242317021. This article has 10 citations.

11. (shi2023genotypedegreeofhemolysis pages 1-2): Yimeng Shi, Yuan Li, Xiawan Yang, Xiaoxia Li, Guangxin Peng, Xin Zhao, Xu Liu, Yufei Zhao, Jing Hu, Xiangrong Hu, Baohang Zhang, Kang Zhou, Yang Yang, Youzhen Xiong, Jianping Li, Huihui Fan, Wenrui Yang, Lei Ye, Liping Jing, Li Zhang, and Fengkui Zhang. Genotype-degree of hemolysis correlation in hereditary spherocytosis. BMC Genomics, Jun 2023. URL: https://doi.org/10.1186/s12864-023-09364-8, doi:10.1186/s12864-023-09364-8. This article has 7 citations and is from a peer-reviewed journal.

12. (hauser2023hereditaryspherocytosiscan pages 1-2): Friederike Häuser, Heidi Rossmann, Anke Adenaeuer, Annette Shrestha, Dana Marandiuc, Claudia Paret, Jörg Faber, Karl J. Lackner, Bernhard Lämmle, and Olaf Beck. Hereditary spherocytosis: can next-generation sequencing of the five most frequently affected genes replace time-consuming functional investigations? International Journal of Molecular Sciences, 24:17021, Nov 2023. URL: https://doi.org/10.3390/ijms242317021, doi:10.3390/ijms242317021. This article has 10 citations.

13. (vivescorrons2026hereditaryspherocytosislinking pages 1-3): Joan Lluís Vives-Corrons and Elena Krishnevskaya. Hereditary spherocytosis: linking ion transport defects to osmotic gradient ektacytometry profiles—a review. International Journal of Molecular Sciences, 27:721, Jan 2026. URL: https://doi.org/10.3390/ijms27020721, doi:10.3390/ijms27020721. This article has 0 citations.

14. (boaro2023hematologicalcharacteristicsand pages 3-5): Maria Paola Boaro, Giulia Reggiani, Mirco D’Agnolo, Vania Munaretto, Francesco Pozzebon, Roberta Trapanese, Maddalena Martella, and Raffaella Colombatti. Hematological characteristics and hepatobiliary complications of hereditary spherocytosis in a tertiary care pediatric center: optimizing diagnosis and care through local and international networks. Frontiers in Pediatrics, Oct 2023. URL: https://doi.org/10.3389/fped.2023.1269645, doi:10.3389/fped.2023.1269645. This article has 3 citations.