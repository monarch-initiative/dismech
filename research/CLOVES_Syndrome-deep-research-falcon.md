---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-07T04:59:45.872188'
end_time: '2026-03-07T05:15:54.228174'
duration_seconds: 968.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CLOVES Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** CLOVES Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CLOVES Syndrome**.
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
- **Disease Name:** CLOVES Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CLOVES Syndrome**.
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


## Comprehensive Research Report: CLOVES Syndrome Pathophysiology (PROS)

### Disease identifiers
- **Disease name:** CLOVES syndrome
- **MONDO ID:** **MONDO:0013038** (Open Targets disease entry; association evidence not reproduced here)
- **Category:** Mendelian/segmental mosaic (post-zygotic somatic)

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Definition and disease class
CLOVES syndrome (Congenital Lipomatous Overgrowth, Vascular malformations, Epidermal nevi, and Skeletal/Spinal anomalies) is a severe phenotype within the **PIK3CA-related overgrowth spectrum (PROS)** caused by **post-zygotic (somatic) mosaic activating variants in PIK3CA**, leading to segmental/asymmetric overgrowth and combined vascular malformations. (henuzet2025…lipomatousovergrowth pages 2-6, seront2024molecularlandscapeand pages 3-5, podolec2025clovessyndromea pages 5-8)

### 1.2 Mosaicism as a pathophysiology-defining concept
A central concept for CLOVES is **somatic mosaicism**: the pathogenic variant is enriched in affected tissue and may be absent/undetectable in blood, which determines both phenotype distribution and diagnostic strategy. Large-scale PROS sequencing supports that strongly activating variants are rarely detectable in blood and are most reliably found in affected tissue. (mussa2023genotypesandphenotypes pages 4-4, mussa2023genotypesandphenotypes pages 1-2)

---

## 2) Core pathophysiology (molecular and cellular mechanisms)

### 2.1 Primary driver: PIK3CA gain-of-function → PI3K pathway hyperactivation
PIK3CA encodes the catalytic subunit p110α of phosphatidylinositol-3-kinase (PI3Kα). Activating hotspot variants (e.g., **p.Glu542Lys**) can “disrupt autoinhibitory interactions and result in constitutive kinase activation,” producing sustained downstream signaling through the PI3K axis. (lakhmawar¹2025bilateralrenalanomaliesa pages 2-4)

In vascular anomalies and PROS, this is described as **direct activation of PI3K–AKT–mTOR**, resulting in abnormal growth and vascular malformations. (seront2024molecularlandscapeand pages 3-5)

### 2.2 Endothelial-cell–centric mechanism for vascular malformations
A 2024 mechanistic study developed an **endothelial-restricted PIK3CA GOF mouse model (PIK3CA^Tie2-CreER)** that recapitulates capillary–venous malformations (a common vascular component in PROS/CLOVES-like disease). Endothelial PIK3CA activation increased AKT/mTOR signaling, caused endothelial hypertrophy, increased proliferation (KI67+), and produced 3D vascular disorganization and thrombosis-like pathology consistent with slow-flow malformations. (zerbib2024targetedtherapyfor pages 1-3, zerbib2024targetedtherapyfor pages 3-5)

### 2.3 Partial AKT dependence and AKT-independent PI3K outputs
A notable refinement from 2024 mechanistic data is that PIK3CA-driven malformations may **only partially signal through AKT proteins**; in the endothelial model, disease depended **partially on AKT1 (not AKT2)**, and genetic deletion of AKT1 delayed but did not prevent lesions—supporting important **AKT-independent PI3K outputs** (e.g., direct mTOR-dependent and/or metabolic/cytoskeletal programs). (zerbib2024targetedtherapyfor pages 1-3, zerbib2024targetedtherapyfor pages 3-5)

### 2.4 Metabolic reprogramming and systemic coagulopathy signals in severe vascular disease
In the same 2024 endothelial PIK3CA model, systemic consequences included regenerative anemia, thrombocytopenia, elevated D-dimers, and broad metabolic changes (e.g., amino-acid accumulation, mitochondrial respiration intermediates, and urea-cycle activation). These observations support a model in which PI3Kα hyperactivation in vascular endothelium is sufficient to drive local lesion biology and systemic secondary effects (coagulation and metabolism). (zerbib2024targetedtherapyfor pages 3-5)

### 2.5 Dysregulated cellular processes (summary)
Across mechanistic and clinical sources, key affected processes include:
- **Cell growth/proliferation and survival** (PI3K-driven tissue overgrowth; endothelial hypertrophy and proliferation). (lakhmawar¹2025bilateralrenalanomaliesa pages 2-4, zerbib2024targetedtherapyfor pages 3-5)
- **Angiogenesis and vascular morphogenesis** with malformed thin-walled channels and thrombosis risk. (zerbib2024targetedtherapyfor pages 1-3, podolec2025clovessyndromea pages 5-8)
- **Lymphangiogenesis/lymphatic malformation biology**, supported by therapeutic sensitivity to mTOR inhibition and model evidence that sirolimus inhibits lymphangiogenesis. (kane2024targetedtherapiesfor pages 1-2, podolec2025clovessyndromea pages 5-8)
- **Extracellular matrix and cell morphology dysregulation**, with PI3Kα inhibition reported to normalize abnormal AKT phosphorylation, morphology, and extracellular fibronectin in patient-derived cellular contexts. (gu2024pik3cagenemutation pages 5-6)

---

## 3) Key molecular players, cell types, and anatomical locations

### 3.1 Genes/proteins
- **PIK3CA (PI3Kα/p110α)**: causal; somatic GOF mosaic variants. (gu2024pik3cagenemutation pages 3-5, seront2024molecularlandscapeand pages 3-5)
- **AKT (especially AKT1 in endothelium)**: partially mediates lesion signaling in vivo. (zerbib2024targetedtherapyfor pages 3-5, zerbib2024targetedtherapyfor pages 1-3)
- **mTOR pathway effectors** (e.g., p-S6RP readouts in lesion tissue) are downstream functional mediators and therapeutic targets. (zerbib2024targetedtherapyfor media 80420135)
- **TEK/TIE2**: upstream activator converging on PI3Kα signaling in related vascular malformations; contributes to phenotypic overlap and shared therapeutic logic (PI3Kα inhibition). (zerbib2024targetedtherapyfor pages 1-3, seront2024molecularlandscapeand pages 3-5)

### 3.2 Chemical entities / drugs and pathway probes
- **Alpelisib (PI3Kα inhibitor)**: directly targets the causal pathway, with regulatory approval for severe PROS. (singh2024fdaapprovalsummary pages 1-3)
- **Sirolimus (mTOR inhibitor)**: downstream pathway blockade used off-label for vascular anomalies and PROS manifestations. (borst2024targetedmedicaltherapies pages 1-3, kane2024targetedtherapiesfor pages 3-5)
- **Miransertib (AKT inhibitor)**: investigational; illustrates the pathway node-specific approach and supports AKT-dependent components in some tissues/cells. (gu2024pik3cagenemutation pages 5-6)

### 3.3 Cell types primarily implicated
- **Endothelial cells**: lesion-resident somatic PIK3CA variants documented; endothelial-restricted PIK3CA activation recapitulates disease biology in mice. (gu2024pik3cagenemutation pages 3-5, zerbib2024targetedtherapyfor pages 3-5)
- **Fibroblast-lineage cells** (context-dependent): in vitro data cited for AKT-inhibitor responsiveness and PI3K-inhibitor normalization of morphology/ECM. (gu2024pik3cagenemutation pages 5-6)

### 3.4 Main tissues/organs involved (with examples)
Clinical synthesis indicates a multi-tissue, mosaic distribution including:
- **Adipose tissue/soft tissue**: congenital, progressive lipomatous overgrowth, commonly truncal/posterolateral. (podolec2025clovessyndromea pages 5-8)
- **Cutaneous/epidermal**: epidermal nevi; capillary malformations. (podolec2025clovessyndromea pages 5-8, faivre2023lowriskof pages 4-4)
- **Vascular/lymphatic**: combined capillary/venous/lymphatic malformations and slow-flow channels. (podolec2025clovessyndromea pages 5-8, zerbib2024targetedtherapyfor pages 1-3)
- **Skeletal/spine**: scoliosis, limb asymmetry; paraspinal/epidural extension and vascular shunts can produce neurologic compromise. (podolec2025clovessyndromea pages 5-8)
- **Kidney**: reported renal anomalies; clinical sources recommend renal surveillance due to renal involvement and Wilms tumor concern. (lakhmawar¹2025bilateralrenalanomaliesa pages 2-4, podolec2025clovessyndromea pages 5-8)
- **Gastrointestinal tract**: rare but clinically significant vascular malformations/venous anomalies causing bleeding (hematochezia), including abnormal mesenteric venous drainage. (stpierre2023gastrointestinalmanifestationsof pages 1-2)

---

## 4) Biological processes (GO-style) and cellular components

### 4.1 Disrupted biological processes (GO-like)
A mechanism-to-process mapping consistent with the evidence includes:
- **PI3K signaling** (upstream driver of abnormal growth and vascular development). (zerbib2024targetedtherapyfor pages 1-3)
- **Angiogenesis / vascular morphogenesis** (endothelial proliferation, disorganized vessel architecture). (zerbib2024targetedtherapyfor pages 3-5)
- **Lymphangiogenesis** (lymphatic malformations; sirolimus inhibits lymphangiogenesis in experimental systems and is clinically used). (kane2024targetedtherapiesfor pages 1-2)
- **Cell proliferation and growth** (endothelial KI67+; segmental soft-tissue overgrowth). (zerbib2024targetedtherapyfor pages 3-5, podolec2025clovessyndromea pages 5-8)
- **Extracellular matrix organization/cell adhesion** (abnormal fibronectin and morphology reported as reversible with PI3Kα inhibition in disease-derived cellular contexts). (gu2024pik3cagenemutation pages 5-6)

### 4.2 Cellular components (GO-like)
Key molecular events occur in:
- **Plasma membrane and phosphoinositide signaling compartments** (PIK3CA-mediated PIP2→PIP3 conversion and recruitment of signaling complexes). (zerbib2024targetedtherapyfor pages 1-3)
- **Cytosol/kinase signaling modules** (AKT phosphorylation and downstream signaling). (zerbib2024targetedtherapyfor pages 1-3)
- **mTOR signaling nodes (mTORC1 readouts such as p-S6RP)** in lesion tissue. (zerbib2024targetedtherapyfor media 80420135)
- **Extracellular space / ECM** (fibronectin changes). (gu2024pik3cagenemutation pages 5-6)

---

## 5) Disease progression: sequence of events from initial trigger to phenotype

1. **Post-zygotic activating mutation in PIK3CA** occurs during embryogenesis, creating a **mosaic clone**. (seront2024molecularlandscapeand pages 3-5)
2. Mutant clone(s) drive **cell-autonomous PI3Kα hyperactivation**, particularly evident in vascular endothelium for malformation components. (gu2024pik3cagenemutation pages 3-5, zerbib2024targetedtherapyfor pages 3-5)
3. **Aberrant growth and vascular/lymphatic development** produce congenital lesions (lipomatous masses, mixed slow-flow malformations, epidermal nevi), typically present at birth and progressively enlarging. (podolec2025clovessyndromea pages 5-8, henuzet2025…lipomatousovergrowth pages 6-7)
4. **Secondary complications** arise from lesion architecture and flow abnormalities: thrombosis/PE risk from venous malformations, neurologic compromise from spinal/paraspinal involvement, organ-specific effects (renal anomalies; GI bleeding from vascular anomalies). (podolec2025clovessyndromea pages 5-8, stpierre2023gastrointestinalmanifestationsof pages 1-2)

---

## 6) Phenotypic manifestations and mechanistic links

### 6.1 Core phenotypes
CLOVES is characterized by congenital lipomatous overgrowth, mixed vascular malformations (capillary/venous/lymphatic/arteriovenous), epidermal nevi, and skeletal/spinal anomalies including scoliosis and limb asymmetry. (podolec2025clovessyndromea pages 5-8)

### 6.2 Mechanistic linkage
- **Lipomatous overgrowth** is consistent with PI3K-driven growth programs in mesodermal soft tissues and may recur after surgery due to persistence of mosaic mutant cells. (podolec2025clovessyndromea pages 5-8)
- **Vascular malformations** reflect endothelial PI3Kα pathway hyperactivation causing abnormal vessel structure and thrombosis susceptibility; animal modeling directly supports an endothelial mechanism. (zerbib2024targetedtherapyfor pages 1-3, zerbib2024targetedtherapyfor pages 3-5)
- **Thrombotic complications** are linked to slow-flow venous malformations and coagulopathy markers (elevated D-dimer noted in long-term clinical follow-up). (wang2024combinedsurgeryand pages 2-5, podolec2025clovessyndromea pages 5-8)
- **Neurologic/spinal symptoms** can result from mass infiltration or arteriovenous shunts leading to venous hypertension and cord injury. (podolec2025clovessyndromea pages 5-8)
- **GI bleeding** may reflect congenital absence/dysplasia of deep venous drainage with intramural venous malformations. (stpierre2023gastrointestinalmanifestationsof pages 1-2)

---

## 7) Recent developments and latest research (prioritizing 2023–2024)

### 7.1 2024: Mechanistic in vivo model clarifying signaling topology
Zerbib et al. (June 2024; Signal Transduction and Targeted Therapy; https://doi.org/10.1038/s41392-024-01862-9) provides mechanistic evidence that endothelial PIK3CA GOF drives malformation formation, clarifies that signaling is **partially AKT1-dependent**, and supports direct PI3Kα inhibition as an effective strategy in preclinical and human contexts. (zerbib2024targetedtherapyfor pages 1-3, zerbib2024targetedtherapyfor pages 3-5)

Immunofluorescence evidence of increased p-AKT and p-S6RP in lesion tissue and clinical response graphics/tables are visible in the extracted figure/table region. (zerbib2024targetedtherapyfor media 80420135)

### 7.2 2023: Large cohort/systematic review enabling quantitative genotype–phenotype and testing strategy insights
Mussa et al. (Mar 2023; Journal of Medical Genetics; https://doi.org/10.1136/jmedgenet-2021-108093) provides quantitative tissue testing yields and genotype-strength correlations across PROS:
- In the 150-patient cohort, detection in **skin biopsies** was much higher than in blood. (mussa2023genotypesandphenotypes pages 4-4)
- **Strong hotspot variants** were far more common in non-CNS phenotypes than CNS phenotypes, emphasizing developmental selection and tissue distribution effects. (mussa2023genotypesandphenotypes pages 6-7)
- CLOVES cases in that cohort showed mutation detection in **skin biopsy** but not in blood/swab in those sampled, reinforcing tissue-based testing. (mussa2023genotypesandphenotypes pages 4-4)

### 7.3 2024: Targeted therapy as a precision-medicine paradigm in vascular anomalies
Hematology-focused 2024 reviews emphasize that a growing proportion of vascular anomalies are driven by somatic variants activating PI3K/AKT/mTOR (or Ras/MAPK), making **genotype-driven therapy selection and standardized monitoring** central to practice. (borst2024targetedmedicaltherapies pages 1-3, seront2024molecularlandscapeand pages 3-5)

---

## 8) Current applications and real-world implementations

### 8.1 Molecular diagnosis (implementation)
Because CLOVES is mosaic, recent cohort evidence supports **testing affected tissue** and, when possible, multiple tissues:
- In the Mussa et al. 2023 cohort, positives by sample type were **93/130 skin biopsies**, **15/38 swabs**, and **12/63 blood**, illustrating the superiority of tissue sampling. (mussa2023genotypesandphenotypes pages 4-4)
- Ultra-deep sequencing depth (mean 2500–3000×; minimum >1000× for low VAF detection) was used in this cohort. (mussa2023genotypesandphenotypes pages 3-4)

### 8.2 Targeted systemic therapy: alpelisib (PI3Kα inhibitor)
**Regulatory/real-world milestone:** The FDA granted **accelerated approval** to alpelisib on **April 5, 2022** for adults and pediatric patients (≥2 years) with severe PROS requiring systemic therapy (publication: Aug 2024, Clinical Cancer Research; https://doi.org/10.1158/1078-0432.CCR-23-1270). (singh2024fdaapprovalsummary pages 1-3)

**Quantitative efficacy:** In EPIK-P1 (expanded access/real-world data; NCT04285723), radiologic response at Week 24 was defined as **≥20% reduction** in the sum of volumetric target lesion(s), with no progression/new lesions. In the efficacy population (n=37), response rate was **27% (95% CI 14–44)**; among responders, **60%** had responses lasting **≥12 months**. (singh2024fdaapprovalsummary pages 1-3, singh2024fdaapprovalsummary pages 3-4)

**Safety statistics (EPIK-P1):** Adverse reactions ≥5% included diarrhea (~16%), stomatitis (~16%), hyperglycemia (~12%), eczema/dry skin (~7%), alopecia/headache/cellulitis (~5%); no grade 5 ARs were reported, and the only grade 3–4 AR described in the excerpt was cellulitis. (singh2024fdaapprovalsummary pages 12-13)

### 8.3 Real-world mechanistic translation in vascular malformations
In a 2024 translational study of capillary–venous malformations, alpelisib improved lesions in a treated patient series and reduced lesion volumes over 6 months (summarized visually with per-patient tabulation in the extracted table/figure region). (zerbib2024targetedtherapyfor media 80420135)

### 8.4 mTOR inhibition and procedural care
**Sirolimus** remains widely used off-label as a pathway-targeted option; reviews emphasize it inhibits lymphangiogenesis in experimental systems and has early clinical case-series support in complex vascular anomalies. (kane2024targetedtherapiesfor pages 1-2)

**Procedures** (sclerotherapy and staged debulking surgery) remain important for symptom control and function; a 13-year CLOVES follow-up reported improvement in deformity and scoliosis after serial ethanol sclerotherapy plus resections. (wang2024combinedsurgeryand pages 2-5)

---

## 9) Expert opinions / authoritative analysis (with monitoring and care delivery considerations)

### 9.1 Genotype-driven therapy selection and monitoring
A 2024 Hematology review emphasizes that somatic PI3K/AKT/mTOR-driven vascular anomalies require targeted therapy expertise, and provides practical monitoring recommendations during targeted therapy (e.g., routine labs every 1–3 months including CBC/CMP/electrolytes and HbA1c; and coagulation markers such as D-dimer/fibrinogen when relevant). (borst2024targetedmedicaltherapies pages 1-3)

### 9.2 FDA perspective on evidence standards and long-term uncertainty
The FDA approval summary explicitly frames alpelisib’s approval as supported by **real-world evidence** with blinded central imaging review, but highlights the need for postmarketing requirements to better characterize response in non-CLOVES/less frequent variants and to study long-term safety in children given expected chronic use and nonclinical bone/dental findings. (singh2024fdaapprovalsummary pages 6-8, singh2024fdaapprovalsummary pages 1-3)

### 9.3 Multidisciplinary implementation
Clinical practice articles stress multidisciplinary management involving genetics, vascular anomalies specialists, hematology/oncology, surgery/interventional radiology, orthopedics, and organ-specific specialists (e.g., nephrology) due to risks of thrombosis, neurologic compromise, and renal involvement. (kane2024targetedtherapiesfor pages 1-2, lakhmawar¹2025bilateralrenalanomaliesa pages 2-4)

---

## 10) Relevant recent statistics and data points (selected)

### 10.1 Mosaicism / detection statistics (PROS cohorts)
- **Specimen yield (150-patient PROS cohort):** positive tests were **93/130 skin biopsies**, **15/38 swabs**, and **12/63 blood**. (mussa2023genotypesandphenotypes pages 4-4)
- **CLOVES subset (same cohort):** **5/5** CLOVES cases were positive in skin biopsies; swab and blood were negative in sampled cases (0/2 each). (mussa2023genotypesandphenotypes pages 4-4)
- **Sequencing depth:** mean 2500–3000×; >1000× as minimum to detect ~1% VAF in that workflow. (mussa2023genotypesandphenotypes pages 3-4)

### 10.2 Targeted therapy outcomes (alpelisib)
- **Radiologic response threshold:** ≥20% volumetric reduction in up to 3 lesions at Week 24. (singh2024fdaapprovalsummary pages 1-3, singh2024fdaapprovalsummary pages 3-4)
- **Response rate:** 27% (95% CI 14–44) at Week 24 (n=37). (singh2024fdaapprovalsummary pages 1-3)
- **Durability:** 60% of responders with response ≥12 months. (singh2024fdaapprovalsummary pages 1-3)
- **Adverse reactions:** diarrhea/stomatitis/hyperglycemia are common; detailed AE frequencies provided in FDA summary excerpts. (singh2024fdaapprovalsummary pages 12-13)

### 10.3 Mechanistic quantitative signals (preclinical)
- In endothelial PIK3CA GOF disease modeling, AKT1 deletion produced only modest survival/lesion-delay benefit and did not prevent lesions, supporting partial AKT dependence. (zerbib2024targetedtherapyfor pages 3-5)

---

## Structured knowledge-base elements

| Component | Mechanism & Description | Key Findings & Quantitative Data | Source(s) |
| :--- | :--- | :--- | :--- |
| **Genetic Etiology** | Somatic mosaic gain-of-function (GOF) mutations in *PIK3CA*. Occurs post-zygotically; not usually inherited. | **Hotspots:** p.His1047Arg, p.Glu542Lys, p.Glu545Lys account for severe phenotypes.<br>**Mosaicism:** Variant Allele Fraction (VAF) ranges from <1% to ~46% in affected tissues; typically very low/absent in blood. | (lakhmawar¹2025bilateralrenalanomalies pages 2-4, gu2024pik3cagenemutation pages 3-5, mussa2023genotypesandphenotypes pages 4-4, faivre2023lowriskof pages 4-4, mussa2023genotypesandphenotypes pages 1-2) |
| **Signaling Pathways** | Hyperactivation of the **PI3K-AKT-mTOR** axis. Mutant p110α (PI3K) increases PIP3, recruiting PDK1 and phosphorylating AKT. | **AKT Dependence:** Endothelial lesions signal *partially* through AKT1 (not AKT2); some effects are AKT-independent.<br>**Upstream:** *TEK*/*TIE2* mutations can activate the same axis in related vascular anomalies. | (gu2024pik3cagenemutation pages 3-5, zerbib2024targetedtherapyfor pages 3-5, zerbib2024targetedtherapyfor pages 1-3, seront2024molecularlandscapeand pages 3-5) |
| **Cellular Processes** | Dysregulated cell growth, survival, and metabolism leading to tissue overgrowth and vascular anomalies. | **Endothelial Cells:** Hypertrophy, increased proliferation (KI67+), 3D vascular disorganization.<br>**Metabolism:** Reprogramming observed (e.g., urea cycle activation, increased mitochondrial respiration). | (zerbib2024targetedtherapyfor pages 3-5, zerbib2024targetedtherapyfor pages 1-3, kane2024targetedtherapiesfor pages 1-2) |
| **Affected Tissues** | Multi-system involvement: Adipose, Vascular, Skeletal, Cutaneous, and Renal tissues. | **Adipose:** Congenital lipomatous overgrowth (often truncal).<br>**Vascular:** Capillary, venous, lymphatic malformations (high risk of thrombosis).<br>**Skeletal:** Scoliosis, limb hypertrophy.<br>**Renal:** Anomalies, Wilms tumor risk (~2-3%). | (lakhmawar¹2025bilateralrenalanomalies pages 2-4, henuzet2025…lipomatousovergrowth pages 2-6, podolec2025clovessyndromea pages 5-8) |
| **Diagnostic Yield** | Diagnosis relies on detecting mosaic variants in affected tissue rather than blood. | **Sensitivity:** Skin biopsy over vascular malformation: ~66% yield; over overgrown tissue: ~73% yield.<br>**Seq. Depth:** High depth (~1500x-3000x) often required to detect low VAF. | (mussa2023genotypesandphenotypes pages 4-4, mussa2023genotypesandphenotypes pages 3-4) |


*Table: Summary of the molecular and cellular mechanisms underlying CLOVES syndrome, including genetic drivers, signaling dysregulation, and tissue-specific manifestations.*

| Therapy | Target / Mechanism | Status | Key Efficacy Findings | Key Safety / Adverse Events | Source(s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Alpelisib**<br>(Vijoice) | **PIK3CA (PI3Kα) Inhibitor**<br>Directly inhibits mutant p110α. | **FDA Accelerated Approval (2022)**<br>For severe PROS ≥2 years requiring systemic therapy. | **EPIK-P1 (n=37):** 27% confirmed radiologic response (≥20% volume reduction); 74% clinical benefit rate. 60% of responders durable ≥12 months.<br>**Mouse Model:** Prevented lesions/improved established ones. | **Common:** Diarrhea (16%), stomatitis (16%), hyperglycemia (12%), cellulitis.<br>**Pediatric:** Potential growth plate/dental abnormalities. | Singh 2024 (singh2024fdaapprovalsummary pages 4-6, singh2024fdaapprovalsummary pages 1-3);<br>Lakhmawar 2025 (lakhmawar¹2025bilateralrenalanomaliesa pages 2-4);<br>Zerbib 2024 (zerbib2024targetedtherapyfor pages 1-3) |
| **Sirolimus**<br>(Rapamycin) | **mTOR Inhibitor**<br>Downstream blockade of mTORC1. | **Off-label**<br>Historical standard of care for vascular anomalies. | Modest reduction in lesion volume; improvement in pain, bleeding, and lymphorrhea. Used when PI3K inhibitors unavailable. | Mucositis, immunosuppression, hyperlipidemia, pneumonitis, risk of rebound upon discontinuation. | Borst 2024 (borst2024targetedmedicaltherapies pages 1-3);<br>Kane 2024 (kane2024targetedtherapiesfor pages 3-5);<br>Gu 2024 (gu2024pik3cagenemutation pages 5-6) |
| **Miransertib** | **AKT Inhibitor**<br>Inhibits AKT phosphorylation. | **Investigational**<br>Compassionate use reported. | Case reports of reduced fatty overgrowth; anti-proliferative effects in patient-derived fibroblasts. Inefficacy noted in some PROS cohorts. | Generally well-tolerated in reported cases; requires monitoring for class effects. | Gu 2024 (gu2024pik3cagenemutation pages 3-5, gu2024pik3cagenemutation pages 5-6);<br>Zerbib 2024 (zerbib2024targetedtherapyfor pages 1-3) |
| **Surgery & Sclerotherapy** | **Mechanical / Chemical Ablation**<br>Debulking or vessel sclerosis. | **Standard Adjunctive**<br>Symptom-directed intervention. | Immediate reduction of bulk or cysts. Serial procedures (e.g., over 13 years) can improve deformity/function. | High risk of nerve damage, bleeding, infection, and rapid regrowth (lipomas are invasive/resistant). | Wang 2024 (wang2024combinedsurgeryand pages 2-5);<br>Podolec 2025 (podolec2025clovessyndromea pages 5-8) |


*Table: Overview of pharmacological and procedural management strategies for CLOVES syndrome, detailing molecular targets, regulatory status, efficacy statistics, and safety profiles based on recent (2023-2025) evidence.*

| Entity Type | Term Label (ID) | Rationale & Relationship to CLOVES | Source(s) |
| :--- | :--- | :--- | :--- |
| **Gene** | *PIK3CA* (HGNC:8975) | Causal somatic mosaic gain-of-function mutations driving pathway hyperactivation. | (lakhmawar¹2025bilateralrenalanomalies pages 2-4, gu2024pik3cagenemutation pages 3-5) |
| **GO Biological Process** | Phosphatidylinositol 3-kinase signaling (GO:0014065) | Primary dysregulated pathway; mutant p110α increases PIP3 and downstream signaling. | (gu2024pik3cagenemutation pages 3-5, zerbib2024targetedtherapyfor pages 1-3) |
| **GO Biological Process** | Angiogenesis (GO:0001525) | Aberrant vessel formation leads to high-flow and low-flow vascular malformations. | (zerbib2024targetedtherapyfor pages 3-5, gu2024pik3cagenemutation pages 3-5) |
| **GO Biological Process** | Lymphangiogenesis (GO:0001906) | Pathologic development of lymphatic structures (macrocystic/microcystic lesions). | (gu2024pik3cagenemutation pages 3-5, kane2024targetedtherapiesfor pages 1-2) |
| **Cell Type** | Endothelial cell (CL:0000115) | Primary mutated cell lineage in vascular lesions; shows hypertrophy and proliferation. | (zerbib2024targetedtherapyfor pages 3-5, zerbib2024targetedtherapyfor pages 1-3) |
| **Anatomy** | Adipose tissue (UBERON:0001013) | Site of congenital, progressive lipomatous overgrowth (often truncal). | (henuzet2025…lipomatousovergrowth pages 2-6, podolec2025clovessyndromea pages 5-8) |
| **Anatomy** | Spinal cord (UBERON:0002240) | Involved via arteriovenous shunts or paraspinal mass infiltration causing compression. | (podolec2025clovessyndromea pages 5-8) |
| **Anatomy** | Kidney (UBERON:0002113) | Risk of anomalies (agenesis, cysts) and Wilms tumor (~2-3% risk). | (lakhmawar¹2025bilateralrenalanomalies pages 2-4, lakhmawar¹2025bilateralrenalanomaliesa pages 2-4) |
| **Phenotype** | Hemihypertrophy (HP:0001528) | Asymmetric overgrowth of limbs or body segments. | (henuzet2025…lipomatousovergrowth pages 2-6, henuzet2025…lipomatousovergrowth pages 6-7) |
| **Phenotype** | Vascular malformation (HP:0002561) | Complex mixed lesions (capillary, venous, lymphatic) predisposing to thrombosis. | (gu2024pik3cagenemutation pages 5-6, podolec2025clovessyndromea pages 5-8) |
| **Phenotype** | Epidermal nevus (HP:0001052) | Linear keratinocytic nevi are a cardinal cutaneous feature. | (faivre2023lowriskof pages 4-4, henuzet2025…lipomatousovergrowth pages 6-7) |
| **Phenotype** | Scoliosis (HP:0002650) | Common skeletal deformity secondary to tissue overgrowth and mass effect. | (henuzet2025…lipomatousovergrowth pages 2-6, wang2024combinedsurgeryand pages 2-5) |
| **Chemical/Drug** | Alpelisib (CHEBI:135936) | PI3Kα-specific inhibitor; FDA-approved for severe PROS. | (singh2024fdaapprovalsummary pages 4-6, lakhmawar¹2025bilateralrenalanomaliesa pages 2-4) |
| **Chemical/Drug** | Sirolimus (CHEBI:9168) | mTOR inhibitor; off-label standard for vascular anomalies/overgrowth. | (borst2024targetedmedicaltherapies pages 1-3, kane2024targetedtherapiesfor pages 3-5) |


*Table: A structured mapping of CLOVES syndrome mechanisms and manifestations to standardized ontology terms (HGNC, GO, CL, UBERON, HP, CHEBI), linking molecular drivers to clinical phenotypes.*

---

## Evidence items (PMID-oriented note)
Several of the cited sources are peer-reviewed and provide DOIs/URLs and publication months/years within the evidence above. In the retrieved excerpts available for this report, **PMIDs were not consistently provided in-text**, so this report cites primary sources via DOI/URL and the evidence context identifiers.

## Visual evidence (figures/tables)
- Extracted figure/table regions from the 2024 translational study show pathway activation readouts (p-AKT and p-S6RP staining) and clinical lesion-volume reductions under alpelisib, including per-patient volume change summaries. (zerbib2024targetedtherapyfor media 80420135)

---

### Notes on scope and limitations
This report focuses on mechanistic and translational evidence explicitly present in the retrieved full-text excerpts. Some clinically important domains (e.g., precise epidemiology across populations, comprehensive staging frameworks, and high-resolution single-cell lesion atlases) may exist in additional literature not captured in the current retrieval set.

References

1. (henuzet2025…lipomatousovergrowth pages 2-6): E Henuzet, L Boon, D Dumitriu, and L Peetermans. … lipomatous overgrowth, vascular malformations, epidermal nevi, and skeletal anomalies (cloves) syndrome: a case report and literature review. Unknown journal, 2025.

2. (seront2024molecularlandscapeand pages 3-5): Emmanuel Seront, Angela Queisser, Laurence M. Boon, and Miikka Vikkula. Molecular landscape and classification of vascular anomalies. Hematology, 2024:700-708, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000598, doi:10.1182/hematology.2024000598. This article has 6 citations and is from a peer-reviewed journal.

3. (podolec2025clovessyndromea pages 5-8): Julianna Podolec, Silvia Ciraolo, Joanna Wojda, Adam Sobiński, Zuzanna Kościuszko, Katarzyna Kurza, Agnieszka Kulczycka-Rowicka, Matylda Czerwonka, Katarzyna Lesiczka-Fedoryj, and Anna Walczak. Cloves syndrome: a review of clinical, genetic, and therapeutic aspects. Quality in Sport, 38:58253, Feb 2025. URL: https://doi.org/10.12775/qs.2025.38.58253, doi:10.12775/qs.2025.38.58253. This article has 0 citations.

4. (mussa2023genotypesandphenotypes pages 4-4): Alessandro Mussa, Chiara Leoni, Matteo Iacoviello, Diana Carli, Carlotta Ranieri, Antonino Pantaleo, Paola Sabrina Buonuomo, Rosanna Bagnulo, Giovanni Battista Ferrero, Andrea Bartuli, Daniela Melis, Silvia Maitz, Daria Carmela Loconte, Antonella Turchiano, Marilidia Piglionica, Annunziata De Luisi, Francesco Claudio Susca, Nenad Bukvic, Cinzia Forleo, Angelo Selicorni, Giuseppe Zampino, Roberta Onesimo, Gerarda Cappuccio, Livia Garavelli, Chiara Novelli, Luigi Memo, Carla Morando, Matteo Della Monica, Maria Accadia, Martina Capurso, Carmelo Piscopo, Anna Cereda, Marilena Carmela Di Giacomo, Veronica Saletti, Alessandro Mauro Spinelli, Patrizia Lastella, Romano Tenconi, Veronika Dvorakova, Alan D Irvine, and Nicoletta Resta. Genotypes and phenotypes heterogeneity in pik3ca-related overgrowth spectrum and overlapping conditions: 150 novel patients and systematic review of 1007 patients with pik3ca pathogenetic variants. Journal of Medical Genetics, 60(2):163-173, Mar 2023. URL: https://doi.org/10.1136/jmedgenet-2021-108093, doi:10.1136/jmedgenet-2021-108093. This article has 44 citations and is from a domain leading peer-reviewed journal.

5. (mussa2023genotypesandphenotypes pages 1-2): Alessandro Mussa, Chiara Leoni, Matteo Iacoviello, Diana Carli, Carlotta Ranieri, Antonino Pantaleo, Paola Sabrina Buonuomo, Rosanna Bagnulo, Giovanni Battista Ferrero, Andrea Bartuli, Daniela Melis, Silvia Maitz, Daria Carmela Loconte, Antonella Turchiano, Marilidia Piglionica, Annunziata De Luisi, Francesco Claudio Susca, Nenad Bukvic, Cinzia Forleo, Angelo Selicorni, Giuseppe Zampino, Roberta Onesimo, Gerarda Cappuccio, Livia Garavelli, Chiara Novelli, Luigi Memo, Carla Morando, Matteo Della Monica, Maria Accadia, Martina Capurso, Carmelo Piscopo, Anna Cereda, Marilena Carmela Di Giacomo, Veronica Saletti, Alessandro Mauro Spinelli, Patrizia Lastella, Romano Tenconi, Veronika Dvorakova, Alan D Irvine, and Nicoletta Resta. Genotypes and phenotypes heterogeneity in pik3ca-related overgrowth spectrum and overlapping conditions: 150 novel patients and systematic review of 1007 patients with pik3ca pathogenetic variants. Journal of Medical Genetics, 60(2):163-173, Mar 2023. URL: https://doi.org/10.1136/jmedgenet-2021-108093, doi:10.1136/jmedgenet-2021-108093. This article has 44 citations and is from a domain leading peer-reviewed journal.

6. (lakhmawar¹2025bilateralrenalanomaliesa pages 2-4): NN Lakhmawar¹, N Khadke, A Shinde, and SN Mhaske. Bilateral renal anomalies and macrocephaly in cloves syndrome: a rare case report with pik3ca hotspot mutation. Unknown journal, 2025.

7. (zerbib2024targetedtherapyfor pages 1-3): Lola Zerbib, Sophia Ladraa, Antoine Fraissenon, Charles Bayard, Marina Firpion, Quitterie Venot, Sanela Protic, Clément Hoguin, Amandine Thomas, Sylvie Fraitag, Jean-Paul Duong, Sophie Kaltenbach, Estelle Balducci, Coline Lefevre, Patrick Villarese, Vahid Asnafi, Christine Broissand, Nicolas Goudin, Ivan Nemazanyy, Gwennhael Autret, Bertrand Tavitian, Christophe Legendre, Nadia Arzouk, Veronique Minard-Colin, Caroline Chopinet, Michael Dussiot, Denise M. Adams, Tristan Mirault, Laurent Guibaud, Paul Isenring, and Guillaume Canaud. Targeted therapy for capillary-venous malformations. Signal Transduction and Targeted Therapy, Jun 2024. URL: https://doi.org/10.1038/s41392-024-01862-9, doi:10.1038/s41392-024-01862-9. This article has 27 citations and is from a peer-reviewed journal.

8. (zerbib2024targetedtherapyfor pages 3-5): Lola Zerbib, Sophia Ladraa, Antoine Fraissenon, Charles Bayard, Marina Firpion, Quitterie Venot, Sanela Protic, Clément Hoguin, Amandine Thomas, Sylvie Fraitag, Jean-Paul Duong, Sophie Kaltenbach, Estelle Balducci, Coline Lefevre, Patrick Villarese, Vahid Asnafi, Christine Broissand, Nicolas Goudin, Ivan Nemazanyy, Gwennhael Autret, Bertrand Tavitian, Christophe Legendre, Nadia Arzouk, Veronique Minard-Colin, Caroline Chopinet, Michael Dussiot, Denise M. Adams, Tristan Mirault, Laurent Guibaud, Paul Isenring, and Guillaume Canaud. Targeted therapy for capillary-venous malformations. Signal Transduction and Targeted Therapy, Jun 2024. URL: https://doi.org/10.1038/s41392-024-01862-9, doi:10.1038/s41392-024-01862-9. This article has 27 citations and is from a peer-reviewed journal.

9. (kane2024targetedtherapiesfor pages 1-2): Gavin Kane and Israel Fernandez-Pineda. Targeted therapies for vascular malformations. Frontiers in Medicine, Sep 2024. URL: https://doi.org/10.3389/fmed.2024.1446046, doi:10.3389/fmed.2024.1446046. This article has 3 citations.

10. (gu2024pik3cagenemutation pages 5-6): Meng Gu, Xuanzhe Zhu, and Yi Zhun Zhu. Pik3ca gene mutation induced rare vascular diseases. Journal of Asian Association of Schools of Pharmacy, 13:12-19, Jan 2024. URL: https://doi.org/10.62100/jaasp.2024.13103, doi:10.62100/jaasp.2024.13103. This article has 0 citations.

11. (gu2024pik3cagenemutation pages 3-5): Meng Gu, Xuanzhe Zhu, and Yi Zhun Zhu. Pik3ca gene mutation induced rare vascular diseases. Journal of Asian Association of Schools of Pharmacy, 13:12-19, Jan 2024. URL: https://doi.org/10.62100/jaasp.2024.13103, doi:10.62100/jaasp.2024.13103. This article has 0 citations.

12. (zerbib2024targetedtherapyfor media 80420135): Lola Zerbib, Sophia Ladraa, Antoine Fraissenon, Charles Bayard, Marina Firpion, Quitterie Venot, Sanela Protic, Clément Hoguin, Amandine Thomas, Sylvie Fraitag, Jean-Paul Duong, Sophie Kaltenbach, Estelle Balducci, Coline Lefevre, Patrick Villarese, Vahid Asnafi, Christine Broissand, Nicolas Goudin, Ivan Nemazanyy, Gwennhael Autret, Bertrand Tavitian, Christophe Legendre, Nadia Arzouk, Veronique Minard-Colin, Caroline Chopinet, Michael Dussiot, Denise M. Adams, Tristan Mirault, Laurent Guibaud, Paul Isenring, and Guillaume Canaud. Targeted therapy for capillary-venous malformations. Signal Transduction and Targeted Therapy, Jun 2024. URL: https://doi.org/10.1038/s41392-024-01862-9, doi:10.1038/s41392-024-01862-9. This article has 27 citations and is from a peer-reviewed journal.

13. (singh2024fdaapprovalsummary pages 1-3): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 52 citations.

14. (borst2024targetedmedicaltherapies pages 1-3): Alexandra Borst. Targeted medical therapies for vascular anomalies. Hematology, 2024:709-717, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000599, doi:10.1182/hematology.2024000599. This article has 4 citations and is from a peer-reviewed journal.

15. (kane2024targetedtherapiesfor pages 3-5): Gavin Kane and Israel Fernandez-Pineda. Targeted therapies for vascular malformations. Frontiers in Medicine, Sep 2024. URL: https://doi.org/10.3389/fmed.2024.1446046, doi:10.3389/fmed.2024.1446046. This article has 3 citations.

16. (faivre2023lowriskof pages 4-4): Laurence Faivre, Jean‐Charles Crépin, Manon Réda, Sophie Nambot, Virginie Carmignac, Caroline Abadie, Tristan Mirault, Cécile Faure‐Conter, Juliette Mazereeuw‐Hautier, Aude Maza, Eve Puzenat, Marie‐Agnès Collonge‐Rame, Anne‐Claire Bursztejn, Christophe Philippe, Christel Thauvin‐Robinet, Martin Chevarin, Claire Abasq‐Thomas, Jeanne Amiel, Stéphanie Arpin, Sébastien Barbarot, Geneviève Baujat, Didier Bessis, Emmanuelle Bourrat, Odile Boute, Nicolas Chassaing, Christine Coubes, Bénédicte Demeer, Patrick Edery, Salima El Chehadeh, Alice Goldenberg, Smail Hadj‐Rabia, Damien Haye, Bertrand Isidor, Marie‐Line Jacquemont, Philippe Khau Van Kien, Didier Lacombe, Daphné Lehalle, Laetitia Lambert, Ludovic Martin, Annabel Maruani, Fanny Morice‐Picard, Florence Petit, Alice Phan, Lucile Pinson, Massimiliano Rossi, Renaud Touraine, Clémence Vanlerberghe, Marie Vincent, Catherine Vincent‐Delorme, Sandra Whalen, Marjolaine Willems, Nathalie Marle, Virginie Verkarre, Christine Devalland, Mojgan Devouassoux‐Shisheboran, Marine Abad, Nathalie Rioux‐Leclercq, Bertille Bonniaud, Yannis Duffourd, Jehanne Martel, Christine Binquet, Paul Kuentz, and Pierre Vabres. Low risk of embryonic and other cancers in pik3ca‐related overgrowth spectrum: impact on screening recommendations. Clinical Genetics, 104:554-563, Aug 2023. URL: https://doi.org/10.1111/cge.14410, doi:10.1111/cge.14410. This article has 13 citations and is from a peer-reviewed journal.

17. (stpierre2023gastrointestinalmanifestationsof pages 1-2): Joëlle St-Pierre, Anirudh Mirakhur, and Nauzer Forbes. Gastrointestinal manifestations of cloves syndrome. ACG Case Reports Journal, 10:e01050, May 2023. URL: https://doi.org/10.14309/crj.0000000000001050, doi:10.14309/crj.0000000000001050. This article has 6 citations.

18. (henuzet2025…lipomatousovergrowth pages 6-7): E Henuzet, L Boon, D Dumitriu, and L Peetermans. … lipomatous overgrowth, vascular malformations, epidermal nevi, and skeletal anomalies (cloves) syndrome: a case report and literature review. Unknown journal, 2025.

19. (wang2024combinedsurgeryand pages 2-5): Shi-Qiang Wang and Siming Yuan. Combined surgery and sclerotherapy for 13 years: a case report of a patient with cloves. Frontiers in Pediatrics, Mar 2024. URL: https://doi.org/10.3389/fped.2024.1336358, doi:10.3389/fped.2024.1336358. This article has 1 citations.

20. (mussa2023genotypesandphenotypes pages 6-7): Alessandro Mussa, Chiara Leoni, Matteo Iacoviello, Diana Carli, Carlotta Ranieri, Antonino Pantaleo, Paola Sabrina Buonuomo, Rosanna Bagnulo, Giovanni Battista Ferrero, Andrea Bartuli, Daniela Melis, Silvia Maitz, Daria Carmela Loconte, Antonella Turchiano, Marilidia Piglionica, Annunziata De Luisi, Francesco Claudio Susca, Nenad Bukvic, Cinzia Forleo, Angelo Selicorni, Giuseppe Zampino, Roberta Onesimo, Gerarda Cappuccio, Livia Garavelli, Chiara Novelli, Luigi Memo, Carla Morando, Matteo Della Monica, Maria Accadia, Martina Capurso, Carmelo Piscopo, Anna Cereda, Marilena Carmela Di Giacomo, Veronica Saletti, Alessandro Mauro Spinelli, Patrizia Lastella, Romano Tenconi, Veronika Dvorakova, Alan D Irvine, and Nicoletta Resta. Genotypes and phenotypes heterogeneity in pik3ca-related overgrowth spectrum and overlapping conditions: 150 novel patients and systematic review of 1007 patients with pik3ca pathogenetic variants. Journal of Medical Genetics, 60(2):163-173, Mar 2023. URL: https://doi.org/10.1136/jmedgenet-2021-108093, doi:10.1136/jmedgenet-2021-108093. This article has 44 citations and is from a domain leading peer-reviewed journal.

21. (mussa2023genotypesandphenotypes pages 3-4): Alessandro Mussa, Chiara Leoni, Matteo Iacoviello, Diana Carli, Carlotta Ranieri, Antonino Pantaleo, Paola Sabrina Buonuomo, Rosanna Bagnulo, Giovanni Battista Ferrero, Andrea Bartuli, Daniela Melis, Silvia Maitz, Daria Carmela Loconte, Antonella Turchiano, Marilidia Piglionica, Annunziata De Luisi, Francesco Claudio Susca, Nenad Bukvic, Cinzia Forleo, Angelo Selicorni, Giuseppe Zampino, Roberta Onesimo, Gerarda Cappuccio, Livia Garavelli, Chiara Novelli, Luigi Memo, Carla Morando, Matteo Della Monica, Maria Accadia, Martina Capurso, Carmelo Piscopo, Anna Cereda, Marilena Carmela Di Giacomo, Veronica Saletti, Alessandro Mauro Spinelli, Patrizia Lastella, Romano Tenconi, Veronika Dvorakova, Alan D Irvine, and Nicoletta Resta. Genotypes and phenotypes heterogeneity in pik3ca-related overgrowth spectrum and overlapping conditions: 150 novel patients and systematic review of 1007 patients with pik3ca pathogenetic variants. Journal of Medical Genetics, 60(2):163-173, Mar 2023. URL: https://doi.org/10.1136/jmedgenet-2021-108093, doi:10.1136/jmedgenet-2021-108093. This article has 44 citations and is from a domain leading peer-reviewed journal.

22. (singh2024fdaapprovalsummary pages 3-4): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 52 citations.

23. (singh2024fdaapprovalsummary pages 12-13): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 52 citations.

24. (singh2024fdaapprovalsummary pages 6-8): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 52 citations.

25. (lakhmawar¹2025bilateralrenalanomalies pages 2-4): NN Lakhmawar¹, N Khadke, A Shinde, and SN Mhaske. Bilateral renal anomalies and macrocephaly in cloves syndrome: a rare case report with pik3ca hotspot mutation. Unknown journal, 2025.

26. (singh2024fdaapprovalsummary pages 4-6): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 52 citations.