---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-09T12:44:28.928986'
end_time: '2025-12-09T13:03:13.642272'
duration_seconds: 1124.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HIDEA Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** HIDEA Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **HIDEA Syndrome**.
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
- **Disease Name:** HIDEA Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **HIDEA Syndrome**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: HIDEA Syndrome
- MONDO ID: [not established in sources retrieved]
- Category: Genetic (autosomal recessive)

## Pathophysiology Description (Narrative)
HIDEA syndrome is a severe, autosomal recessive neurodevelopmental disorder caused by biallelic loss-of-function variants in P4HTM, encoding the endoplasmic reticulum (ER) transmembrane prolyl 4-hydroxylase P4H‑TM. Foundational clinical genetics established that “biallelic loss‑of‑function P4HTM gene variants cause hypotonia, hypoventilation, intellectual disability, dysautonomia, epilepsy, and eye abnormalities (HIDEA)” (Genetics in Medicine, Oct 2019; https://doi.org/10.1038/s41436-019-0503-4). Mechanistically, P4H‑TM localizes to the ER membrane with its catalytic domain in the ER lumen and includes a unique EF‑hand domain, suggesting Ca2+ regulation of enzymatic activity and a tight link to ER–calcium signaling. Recent experimental work demonstrated that P4H‑TM is a regulator of astrocyte Ca2+ signaling and gliotransmission via a HIF‑1–dependent mechanism, implicating dysregulated hypoxia signaling in CNS networks that govern respiration and autonomic function (eNeuro, Dec 2021; https://doi.org/10.1523/eneuro.0253-20.2020) (alanisula2024metaboliccharacteristicsof pages 3-6). Complementary in vivo evidence from global P4h‑tm−/− mice shows alterations in whole‑body energy metabolism, neuromuscular weakness, and, critically, a reduced respiratory rate with blunted ventilatory responses to hypoxia and hypercapnia, leading to respiratory acidosis; the authors conclude that these changes “appear to be neurological and controlled by the brain and central nervous system circuits,” recapitulating key human HIDEA features (Pflügers Archiv, Feb 2024; https://doi.org/10.1007/s00424-024-02920-5) (alanisula2024metaboliccharacteristicsof pages 1-2, alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 3-6, alanisula2024metaboliccharacteristicsof pages 9-11).

A subset of HIDEA patients show mitochondrial respiratory chain complex I deficiency in muscle biopsies, suggesting that P4H‑TM loss can intersect with mitochondrial function and integrated stress response pathways (e.g., ATF4), potentially downstream of altered HIF signaling and ER–mitochondria Ca2+ crosstalk (Eur J Hum Genet, Jul 2021; https://doi.org/10.1038/s41431-021-00932-8) (wang2024clinicalcharacteristicsof pages 6-7). Clinically, HIDEA overlaps with ROHHAD-like presentations (rapid-onset obesity, hypoventilation, dysautonomia), leading experts to recommend P4HTM sequencing in ROHHAD-suspected cases that also exhibit abnormal neurodevelopment or eye findings (Front Genet, Mar 2023; https://doi.org/10.3389/fgene.2023.1137767) (harvengt2023hideasyndromea pages 5-6).

| Category | Key finding or quote | Molecular/Cellular process implicated | Species / Context | Source (authors, year) | Journal | URL / DOI | Publication date |
|---|---|---|---|---|---|---|---|
| Foundational description | "Biallelic loss-of-function P4HTM gene variants cause hypotonia, hypoventilation, intellectual disability, dysautonomia, epilepsy, and eye abnormalities (HIDEA)" (diagnostic/phenotypic definition) (harvengt2023hideasyndromea pages 5-6) | Genetic loss-of-function in P4HTM → syndromic neurodevelopmental disorder | Human patients / clinical genetics | Rahikkala et al., 2019 | Genetics in Medicine | https://doi.org/10.1038/s41436-019-0503-4 | Oct 2019 |
| Clinical case / phenotype overlap | Case report: clinical similarity between HIDEA and ROHHAD; recommends testing P4HTM in ROHHAD-like cases (harvengt2023hideasyndromea pages 5-6) | Hypothalamic/dysautonomia features; central hypoventilation | Human clinical case series / diagnostic recommendation | Harvengt et al., 2023 | Frontiers in Genetics | https://doi.org/10.3389/fgene.2023.1137767 | Mar 2023 |
| Cellular mechanism (astrocytes) | "P4H-TM is a novel regulator of calcium dynamics and gliotransmission" (HIF1 mediates effect on calcium signaling) (alanisula2024metaboliccharacteristicsof pages 3-6) | Disrupted receptor-/store-operated Ca2+ entry (ROCE/SOCE), mitochondrial Ca2+ uptake, altered ATP; HIF-1α–dependent pathway | Mouse primary astrocytes / cortex (cellular assays) | Byts et al., 2021 | eNeuro | https://doi.org/10.1523/eneuro.0253-20.2020 | Dec 2021 |
| Mitochondrial involvement | Reports of mitochondrial respiratory chain complex I deficiency in some HIDEA patients; ATF4/ISR proposed link (alanisula2024metaboliccharacteristicsof pages 3-6) | Mitochondrial respiratory chain dysfunction, integrated stress response (ATF4) | Human muscle biopsy / clinical case | Hay et al., 2021 | European Journal of Human Genetics | https://doi.org/10.1038/s41431-021-00932-8 | Jul 2021 |
| Mouse model — systemic phenotypes | P4h-tm−/− mice show altered 24-h energy expenditure, lower respiratory rate, blunted hypoxia/hypercapnia responses, neuromuscular weakness — "recapitulates some symptoms of HIDEA" (alanisula2024metaboliccharacteristicsof pages 12-13, alanisula2024metaboliccharacteristicsof pages 11-12) | Altered whole-body energy metabolism, respiratory control, neuromuscular function; CNS-origin hypothesis | Global knockout mouse (P4h-tm−/−) — physiological, metabolic, respiratory assays | Ala‑Nisula et al., 2024 | Pflugers Archiv | https://doi.org/10.1007/s00424-024-02920-5 | Feb 2024 |
| Therapeutics / clinical management | Seizures in P4HTM-associated patients often start in infancy and are relatively controllable; valproate (a HIF‑1α inhibitor) proposed as promising (wang2024clinicalcharacteristicsof pages 6-7) | Pharmacologic HIF‑1α modulation considered (valproate cited) | Human case report + literature review (epilepsy focus) | Wang et al., 2024 | Frontiers in Neurology | https://doi.org/10.3389/fneur.2024.1428076 | Nov 2024 |
| Subcellular localization | P4H-TM is an endoplasmic reticulum (ER) transmembrane prolyl 4‑hydroxylase with its catalytic domain in the ER lumen (alanisula2024metaboliccharacteristicsof pages 1-2) | ER membrane localization → lumenal catalytic activity; potential ER‑related substrates/processes | Biochemical/structural annotation from mouse/human studies | (Ala‑Nisula summary of prior work), 2024 | (summarized in Pflugers Archiv) | https://doi.org/10.1007/s00424-024-02920-5 | Feb 2024 |
| EF‑hand / Ca2+ regulation | "its catalytic activity may be regulated by Ca2+"; P4H‑TM contains a unique EF‑hand adjacent to the dioxygenase domain (alanisula2024metaboliccharacteristicsof pages 1-2) | EF‑hand calcium‑binding domain → Ca2+ modulation of enzymatic activity; links to calcium signaling defects | Structural/functional inference (protein domain and mouse/cell data) | (Ala‑Nisula summary of structural data), 2024 | (summarized in Pflugers Archiv) | https://doi.org/10.1007/s00424-024-02920-5 | Feb 2024 |


*Table: Concise, citation-linked summary of mechanistic, clinical, model, localization, and therapeutic evidence for HIDEA syndrome (P4HTM/P4H‑TM) from prioritized 2019–2024 literature; useful as an evidence-annotated quick reference for disease knowledge base entries.*

## 1. Core Pathophysiology
- Primary mechanisms:
  - Loss of ER-resident transmembrane prolyl 4-hydroxylase (P4H‑TM) activity with EF‑hand–mediated Ca2+ modulation, disturbing ER–calcium signaling and HIF‑linked pathways in neural cells (astrocytes) (alanisula2024metaboliccharacteristicsof pages 1-2, alanisula2024metaboliccharacteristicsof pages 3-6).
  - HIF‑1–dependent perturbation of receptor‑operated and store‑operated Ca2+ entry (ROCE/SOCE), impaired mitochondrial Ca2+ uptake, reduced ATP, and attenuated gliotransmission in P4h‑tm−/− astrocytes (eNeuro 2021) (alanisula2024metaboliccharacteristicsof pages 3-6).
  - CNS‑origin respiratory control dysfunction, evidenced by reduced respiratory rate, blunted hypoxia/hypercapnia responses, and respiratory acidosis in P4h‑tm−/− mice, mechanistically linking astroglial/neuronal signaling defects to ventilatory control (Pflügers Archiv 2024) (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 9-11).
  - In some patients, mitochondrial complex I deficiency suggests secondary mitochondrial dysfunction and activation of integrated stress response nodes (e.g., ATF4) (EJHG 2021) (wang2024clinicalcharacteristicsof pages 6-7).

- Dysregulated molecular pathways:
  - Hypoxia signaling (HIF‑1 axis) and calcium signaling pathways in glia (astrocytes) (alanisula2024metaboliccharacteristicsof pages 3-6).
  - Potential ER stress/integrated stress response convergence (ATF4) in patient tissues with mitochondrial involvement (wang2024clinicalcharacteristicsof pages 6-7).

- Affected cellular processes:
  - Calcium homeostasis (ROCE, SOCE), mitochondrial Ca2+ uptake, gliotransmission, and cellular energy metabolism (alanisula2024metaboliccharacteristicsof pages 3-6).
  - Central control of respiration and autonomic function; whole‑body energy balance and glycogenolysis (alanisula2024metaboliccharacteristicsof pages 1-2, alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 9-11).

## 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - P4HTM (HGNC:20070): ER transmembrane prolyl 4‑hydroxylase; causal gene for HIDEA (Genet Med 2019; https://doi.org/10.1038/s41436-019-0503-4) (harvengt2023hideasyndromea pages 5-6).
  - HIF1A (HGNC:4910): Effector of hypoxia signaling implicated in P4H‑TM–dependent astrocyte Ca2+ regulation (eNeuro 2021) (alanisula2024metaboliccharacteristicsof pages 3-6).
  - ATF4 (HGNC:785): Integrated stress response factor hypothesized to be involved in patient mitochondrial phenotype (EJHG 2021) (wang2024clinicalcharacteristicsof pages 6-7).

- Chemical entities (CHEBI) and relevant metabolites/drugs:
  - Calcium ion (CHEBI:29108): EF‑hand regulation; Ca2+ signaling defects (alanisula2024metaboliccharacteristicsof pages 3-6).
  - Lactate (CHEBI:24996): Elevated in sedated P4h‑tm−/− mice, consistent with tissue hypoxia and glycolytic shift (Pflügers Archiv 2024) (alanisula2024metaboliccharacteristicsof pages 9-11).
  - Insulin (CHEBI:5931): Altered responses in mice; >50% loss of consciousness after insulin injection under certain conditions (Pflügers Archiv 2024) (alanisula2024metaboliccharacteristicsof pages 9-11).
  - Valproate (CHEBI:39867): Proposed for seizure control; noted HIF‑1α‑inhibiting properties in review context (Front Neurol 2024) (wang2024clinicalcharacteristicsof pages 6-7).

- Cell types (CL):
  - Astrocytes (CL:0000127): Primary cell type with demonstrated P4H‑TM–dependent Ca2+ signaling and gliotransmission defects (alanisula2024metaboliccharacteristicsof pages 3-6).
  - Neurons (CL:0000540): Implicated in central respiratory/autonomic control (inferred from CNS-origin in mouse phenotype) (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 9-11).

- Anatomical locations (UBERON):
  - Endoplasmic reticulum (GO/Cellular Component but anatomical context within cells): ER membrane localization of P4H‑TM (alanisula2024metaboliccharacteristicsof pages 1-2).
  - Brain/central nervous system (UBERON:0000955), including respiratory centers (medulla/pons; UBERON:0001898, UBERON:0000988) (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 9-11).
  - Eye (UBERON:0000970): HIDEA includes eye abnormalities; retinal involvement reported in some patients (harvengt2023hideasyndromea pages 5-6, wang2024clinicalcharacteristicsof pages 6-7).
  - Liver (UBERON:0002107): Altered glycogenolysis in P4h‑tm−/− mice (alanisula2024metaboliccharacteristicsof pages 7-9).

## 3. Biological Processes (GO) Disrupted
- Calcium ion transmembrane transport; receptor‑operated and store‑operated Ca2+ entry (GO:0070588; GO:0007204; GO:0005245 context) (alanisula2024metaboliccharacteristicsof pages 3-6).
- Gliotransmission and regulation of synaptic signaling by glia (GO:0099177; GO:0099154) (alanisula2024metaboliccharacteristicsof pages 3-6).
- Response to hypoxia and HIF‑1 signaling (GO:0001666; GO:0071456) (alanisula2024metaboliccharacteristicsof pages 3-6).
- Regulation of respiratory system process and ventilatory response to hypoxia/hypercapnia (GO:0003016; GO:0061419) (mouse phenotype mapping to GO context) (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 9-11).
- Glycogen catabolic process and glucose homeostasis (GO:0005980; GO:0042593) (alanisula2024metaboliccharacteristicsof pages 7-9).
- Mitochondrial electron transport, NADH to ubiquinone (complex I) (GO:0006120) in subset of patients (wang2024clinicalcharacteristicsof pages 6-7).

## 4. Cellular Components
- Endoplasmic reticulum membrane and lumen (GO:0005789; GO:0005788): P4H‑TM localization; catalytic domain in ER lumen (alanisula2024metaboliccharacteristicsof pages 1-2).
- Mitochondrion (GO:0005739): Altered Ca2+ uptake and complex I deficiency in some patients; astrocyte mitochondrial redistribution in vitro (alanisula2024metaboliccharacteristicsof pages 3-6, wang2024clinicalcharacteristicsof pages 6-7).
- Synapse and astrocyte processes (GO:0045202; GO:0097449): Attenuated calcium agonist–induced gliotransmission (alanisula2024metaboliccharacteristicsof pages 3-6).

## 5. Disease Progression (Proposed Sequence)
- Genetic trigger: biallelic P4HTM loss-of-function variants (harvengt2023hideasyndromea pages 5-6).
- Cellular dysfunction: loss of P4H‑TM activity in ER with EF‑hand Ca2+ regulation → HIF‑1–linked dysregulation of astrocyte ROCE/SOCE, reduced mitochondrial Ca2+ uptake and ATP, attenuated gliotransmission (alanisula2024metaboliccharacteristicsof pages 3-6).
- Network-level impact: impaired astrocyte–neuron signaling within brainstem/hypothalamic circuits → disordered autonomic and ventilatory control (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 9-11).
- Systemic manifestations: hypoventilation with blunted response to hypoxia/hypercapnia and respiratory acidosis; altered energy balance, accelerated hepatic glycogenolysis, shifts toward glycolysis (in mice) (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 9-11).
- Clinical phenotypes: hypotonia, intellectual disability, dysautonomia, epilepsy, eye abnormalities; occasional mitochondrial complex I deficiency consistent with bioenergetic stress (harvengt2023hideasyndromea pages 5-6, wang2024clinicalcharacteristicsof pages 6-7).

## 6. Phenotypic Manifestations (HPO) and Mechanistic Links
- Generalized hypotonia (HP:0001252): neuromuscular weakness in mice and clinical hypotonia in patients (harvengt2023hideasyndromea pages 5-6, alanisula2024metaboliccharacteristicsof pages 3-6, alanisula2024metaboliccharacteristicsof pages 9-11).
- Central hypoventilation (HP:0002875) and sleep-related hypoventilation (HP:0002871): reduced respiratory rate, blunted ventilatory responses, respiratory acidosis in mice; clinical hypoventilation in HIDEA (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 9-11, harvengt2023hideasyndromea pages 5-6).
- Intellectual disability (HP:0001249) (harvengt2023hideasyndromea pages 5-6).
- Dysautonomia (HP:0002279): overlapping ROHHAD-like dysautonomia and rapid weight gain reported in case; hypothalamic features suggested (harvengt2023hideasyndromea pages 5-6).
- Epilepsy (HP:0001250): variable seizures; 2024 review notes early onset and relative treatment responsiveness; valproate proposed (wang2024clinicalcharacteristicsof pages 6-7).
- Eye abnormalities: strabismus (HP:0000486), ocular motor abnormalities, retinal hypopigmentation (HP:0007736) in some cases (harvengt2023hideasyndromea pages 5-6, wang2024clinicalcharacteristicsof pages 6-7).
- Metabolic alterations: increased lactate under sedation, altered glycogenolysis, insulin responses (mouse) (not direct HPO but mechanistically relevant) (alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 9-11).

## Recent Developments and Latest Research (2023–2024 priority)
- 2024 P4h‑tm−/− physiology study provided quantitative evidence for central ventilatory control defects and systemic metabolic changes: conscious male mutants had ~20% lower respiratory rate; under fentanyl–midazolam, further ~25% reduction with lower arterial pO2, higher pCO2, and lower pH; hypercapnic ventilatory response: WT +31% vs mutants +13%; fasting hepatic glycogen decreased to ~18% in mutants vs ~33% WT (male) (Pflügers Archiv, Feb 2024; https://doi.org/10.1007/s00424-024-02920-5) (alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 11-12).
- 2024 clinical epilepsy report and review: seizures often begin in infancy, multiple types, relatively well controlled; “Valproate, which has HIF‑1α inhibiting properties, may be a promising treatment avenue” (Front Neurol, Nov 2024; https://doi.org/10.3389/fneur.2024.1428076) (wang2024clinicalcharacteristicsof pages 6-7).
- 2023 case report highlighted clinical overlap with ROHHAD and suggested P4HTM testing in ROHHAD-like phenotypes with neurodevelopmental or ocular abnormalities (Front Genet, Mar 2023; https://doi.org/10.3389/fgene.2023.1137767) (harvengt2023hideasyndromea pages 5-6).

## Current Applications and Real-World Implementations
- Diagnostics: Gene sequencing of P4HTM in patients with hypotonia–hypoventilation–dysautonomia–eye abnormalities and in ROHHAD-like cases with atypical neurodevelopment/eye findings, as recommended by recent clinical reports (Front Genet 2023; https://doi.org/10.3389/fgene.2023.1137767) (harvengt2023hideasyndromea pages 5-6).
- Model systems: Global P4h‑tm−/− mice as a translational model recapitulating respiratory and neuromuscular features for preclinical evaluation of ventilatory support or pharmacologic modulation of HIF/Ca2+ pathways (Pflügers Archiv 2024; https://doi.org/10.1007/s00424-024-02920-5) (alanisula2024metaboliccharacteristicsof pages 1-2, alanisula2024metaboliccharacteristicsof pages 9-11).
- Therapeutics: Seizure management generally responsive to standard agents; valproate suggested as potentially beneficial through HIF‑1α inhibition, though controlled trials are lacking (Front Neurol 2024; https://doi.org/10.3389/fneur.2024.1428076) (wang2024clinicalcharacteristicsof pages 6-7).

## Expert Opinions and Authoritative Analyses (selected quotes)
- “P4H‑TM is a novel regulator of calcium dynamics and gliotransmission.” (eNeuro, Dec 2021; https://doi.org/10.1523/eneuro.0253-20.2020) (alanisula2024metaboliccharacteristicsof pages 3-6).
- Mouse in vivo conclusion: respiratory/metabolic/neuromuscular changes “appear to be neurological and controlled by the brain and central nervous system circuits.” (Pflügers Archiv, Feb 2024; https://doi.org/10.1007/s00424-024-02920-5) (alanisula2024metaboliccharacteristicsof pages 11-12).
- Clinical genetics definition: “Biallelic loss‑of‑function P4HTM gene variants cause… (HIDEA)” (Genet Med, Oct 2019; https://doi.org/10.1038/s41436-019-0503-4) (harvengt2023hideasyndromea pages 5-6).

## Relevant Statistics and Data (recent studies)
- Respiratory physiology in P4h‑tm−/− mice: ~20% lower respiratory rate in conscious males; further ~25% reduction under sedation; blunted hypercapnia response (+13% vs WT +31%); arterial blood gases consistent with respiratory acidosis (Pflügers Archiv, Feb 2024; https://doi.org/10.1007/s00424-024-02920-5) (alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 11-12).
- Hepatic glycogen during fasting: male mutants ~18% vs WT ~33% remaining (P=0.024) (Pflügers Archiv, Feb 2024) (alanisula2024metaboliccharacteristicsof pages 7-9).
- Metabolic effects under sedation: improved glucose tolerance, lower fasting insulin, higher blood lactate, lower serum FFA in mutants; >50% lost consciousness ~30 min post‑insulin injection (Pflügers Archiv, Feb 2024) (alanisula2024metaboliccharacteristicsof pages 9-11).
- Clinical epilepsy course: early-onset seizures, multiple types, relatively controlled; valproate effectiveness noted in a case report (Front Neurol, Nov 2024) (wang2024clinicalcharacteristicsof pages 6-7).

## Gene/Protein Annotations and Ontology Mappings
- HGNC:
  - P4HTM (HGNC:20070) (harvengt2023hideasyndromea pages 5-6)
  - HIF1A (HGNC:4910) (alanisula2024metaboliccharacteristicsof pages 3-6)
  - ATF4 (HGNC:785) (wang2024clinicalcharacteristicsof pages 6-7)

- GO Biological Processes: calcium ion transmembrane transport; receptor‑operated Ca2+ entry; store‑operated Ca2+ entry; regulation of gliotransmission; response to hypoxia (HIF‑1 signaling); ventilatory response to hypoxia/hypercapnia; glycogen catabolism; mitochondrial electron transport (complex I) (alanisula2024metaboliccharacteristicsof pages 3-6, alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, wang2024clinicalcharacteristicsof pages 6-7).

- GO Cellular Components: ER membrane/lumen; mitochondrion; synapse; astrocyte processes (alanisula2024metaboliccharacteristicsof pages 1-2, alanisula2024metaboliccharacteristicsof pages 3-6).

- CL (Cell types): Astrocytes (CL:0000127); Neurons (CL:0000540) (alanisula2024metaboliccharacteristicsof pages 3-6, alanisula2024metaboliccharacteristicsof pages 11-12).

- UBERON (Anatomy): Brain/CNS (UBERON:0000955); medulla (UBERON:0001898); pons (UBERON:0000988); eye (UBERON:0000970); liver (UBERON:0002107) (alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, harvengt2023hideasyndromea pages 5-6).

- CHEBI (Chemicals): Calcium (CHEBI:29108); Lactate (CHEBI:24996); Insulin (CHEBI:5931); Valproate (CHEBI:39867) (alanisula2024metaboliccharacteristicsof pages 9-11, wang2024clinicalcharacteristicsof pages 6-7, alanisula2024metaboliccharacteristicsof pages 3-6).

- HPO (Phenotypes): Hypotonia (HP:0001252); Central hypoventilation (HP:0002875); Intellectual disability (HP:0001249); Dysautonomia (HP:0002279); Epilepsy (HP:0001250); Strabismus (HP:0000486); Retinal hypopigmentation (HP:0007736) (harvengt2023hideasyndromea pages 5-6, wang2024clinicalcharacteristicsof pages 6-7).

## Evidence Items with PMIDs/DOIs, URLs, Dates
- Rahikkala et al., 2019. Genetics in Medicine. DOI: 10.1038/s41436-019-0503-4. URL: https://doi.org/10.1038/s41436-019-0503-4. Publication date: Oct 2019. (harvengt2023hideasyndromea pages 5-6)
- Harvengt et al., 2023. Frontiers in Genetics. DOI: 10.3389/fgene.2023.1137767. URL: https://doi.org/10.3389/fgene.2023.1137767. Publication date: Mar 2023. (harvengt2023hideasyndromea pages 5-6)
- Byts et al., 2021. eNeuro. DOI: 10.1523/eneuro.0253-20.2020. URL: https://doi.org/10.1523/eneuro.0253-20.2020. Publication date: Dec 2021. (alanisula2024metaboliccharacteristicsof pages 3-6)
- Hay et al., 2021. European Journal of Human Genetics. DOI: 10.1038/s41431-021-00932-8. URL: https://doi.org/10.1038/s41431-021-00932-8. Publication date: Jul 2021. (wang2024clinicalcharacteristicsof pages 6-7)
- Ala‑Nisula et al., 2024. Pflügers Archiv. DOI: 10.1007/s00424-024-02920-5. URL: https://doi.org/10.1007/s00424-024-02920-5. Publication date: Feb 2024. (alanisula2024metaboliccharacteristicsof pages 1-2, alanisula2024metaboliccharacteristicsof pages 11-12, alanisula2024metaboliccharacteristicsof pages 7-9, alanisula2024metaboliccharacteristicsof pages 3-6, alanisula2024metaboliccharacteristicsof pages 9-11)
- Wang et al., 2024. Frontiers in Neurology. DOI: 10.3389/fneur.2024.1428076. URL: https://doi.org/10.3389/fneur.2024.1428076. Publication date: Nov 2024. (wang2024clinicalcharacteristicsof pages 6-7)

## Notes on Open Questions
- The primary physiological substrate(s) of P4H‑TM in vivo remain uncertain; although HIF‑α hydroxylation can be observed in vitro and HIF‑1–dependent effects are demonstrated in astrocytes, multiple studies emphasize that HIFα may not be the primary substrate across all contexts, leaving room for discovery of additional ER‑luminal target(s) relevant to CNS circuits and mitochondria–ER crosstalk (Pflügers Archiv 2024) (alanisula2024metaboliccharacteristicsof pages 1-2).


References

1. (alanisula2024metaboliccharacteristicsof pages 3-6): Tuulia Ala-Nisula, Riikka Halmetoja, Henri Leinonen, Margareta Kurkela, Henna-Riikka Lipponen, Samuli Sakko, Mikko Karpale, Antti M. Salo, Niina Sissala, Tapio Röning, Ghulam S. Raza, Kari A. Mäkelä, Jérôme Thevenot, Karl-Heinz Herzig, Raisa Serpi, Johanna Myllyharju, Heikki Tanila, Peppi Koivunen, and Elitsa Y. Dimova. Metabolic characteristics of transmembrane prolyl 4-hydroxylase (p4h-tm) deficient mice. Pflugers Archiv, 476:1339-1351, Feb 2024. URL: https://doi.org/10.1007/s00424-024-02920-5, doi:10.1007/s00424-024-02920-5. This article has 5 citations.

2. (alanisula2024metaboliccharacteristicsof pages 1-2): Tuulia Ala-Nisula, Riikka Halmetoja, Henri Leinonen, Margareta Kurkela, Henna-Riikka Lipponen, Samuli Sakko, Mikko Karpale, Antti M. Salo, Niina Sissala, Tapio Röning, Ghulam S. Raza, Kari A. Mäkelä, Jérôme Thevenot, Karl-Heinz Herzig, Raisa Serpi, Johanna Myllyharju, Heikki Tanila, Peppi Koivunen, and Elitsa Y. Dimova. Metabolic characteristics of transmembrane prolyl 4-hydroxylase (p4h-tm) deficient mice. Pflugers Archiv, 476:1339-1351, Feb 2024. URL: https://doi.org/10.1007/s00424-024-02920-5, doi:10.1007/s00424-024-02920-5. This article has 5 citations.

3. (alanisula2024metaboliccharacteristicsof pages 11-12): Tuulia Ala-Nisula, Riikka Halmetoja, Henri Leinonen, Margareta Kurkela, Henna-Riikka Lipponen, Samuli Sakko, Mikko Karpale, Antti M. Salo, Niina Sissala, Tapio Röning, Ghulam S. Raza, Kari A. Mäkelä, Jérôme Thevenot, Karl-Heinz Herzig, Raisa Serpi, Johanna Myllyharju, Heikki Tanila, Peppi Koivunen, and Elitsa Y. Dimova. Metabolic characteristics of transmembrane prolyl 4-hydroxylase (p4h-tm) deficient mice. Pflugers Archiv, 476:1339-1351, Feb 2024. URL: https://doi.org/10.1007/s00424-024-02920-5, doi:10.1007/s00424-024-02920-5. This article has 5 citations.

4. (alanisula2024metaboliccharacteristicsof pages 7-9): Tuulia Ala-Nisula, Riikka Halmetoja, Henri Leinonen, Margareta Kurkela, Henna-Riikka Lipponen, Samuli Sakko, Mikko Karpale, Antti M. Salo, Niina Sissala, Tapio Röning, Ghulam S. Raza, Kari A. Mäkelä, Jérôme Thevenot, Karl-Heinz Herzig, Raisa Serpi, Johanna Myllyharju, Heikki Tanila, Peppi Koivunen, and Elitsa Y. Dimova. Metabolic characteristics of transmembrane prolyl 4-hydroxylase (p4h-tm) deficient mice. Pflugers Archiv, 476:1339-1351, Feb 2024. URL: https://doi.org/10.1007/s00424-024-02920-5, doi:10.1007/s00424-024-02920-5. This article has 5 citations.

5. (alanisula2024metaboliccharacteristicsof pages 9-11): Tuulia Ala-Nisula, Riikka Halmetoja, Henri Leinonen, Margareta Kurkela, Henna-Riikka Lipponen, Samuli Sakko, Mikko Karpale, Antti M. Salo, Niina Sissala, Tapio Röning, Ghulam S. Raza, Kari A. Mäkelä, Jérôme Thevenot, Karl-Heinz Herzig, Raisa Serpi, Johanna Myllyharju, Heikki Tanila, Peppi Koivunen, and Elitsa Y. Dimova. Metabolic characteristics of transmembrane prolyl 4-hydroxylase (p4h-tm) deficient mice. Pflugers Archiv, 476:1339-1351, Feb 2024. URL: https://doi.org/10.1007/s00424-024-02920-5, doi:10.1007/s00424-024-02920-5. This article has 5 citations.

6. (wang2024clinicalcharacteristicsof pages 6-7): Yan-Juan Wang, Si-Xiu Li, Wen-Guang Hu, Li-Li Zhao, Mingping Lan, and Jia-Lei Chen. Clinical characteristics of patients with p4htm variant-associated epilepsy and therapeutic exploration: a case report and literature review. Frontiers in Neurology, Nov 2024. URL: https://doi.org/10.3389/fneur.2024.1428076, doi:10.3389/fneur.2024.1428076. This article has 1 citations and is from a peer-reviewed journal.

7. (harvengt2023hideasyndromea pages 5-6): J. Harvengt, A. Lumaka, C. Fasquelle, J. H. Caberg, M. Mastouri, A. Janssen, L. Palmeira, and V. Bours. Hidea syndrome: a new case report highlighting similarities with rohhad syndrome. Frontiers in Genetics, Mar 2023. URL: https://doi.org/10.3389/fgene.2023.1137767, doi:10.3389/fgene.2023.1137767. This article has 5 citations and is from a peer-reviewed journal.

8. (alanisula2024metaboliccharacteristicsof pages 12-13): Tuulia Ala-Nisula, Riikka Halmetoja, Henri Leinonen, Margareta Kurkela, Henna-Riikka Lipponen, Samuli Sakko, Mikko Karpale, Antti M. Salo, Niina Sissala, Tapio Röning, Ghulam S. Raza, Kari A. Mäkelä, Jérôme Thevenot, Karl-Heinz Herzig, Raisa Serpi, Johanna Myllyharju, Heikki Tanila, Peppi Koivunen, and Elitsa Y. Dimova. Metabolic characteristics of transmembrane prolyl 4-hydroxylase (p4h-tm) deficient mice. Pflugers Archiv, 476:1339-1351, Feb 2024. URL: https://doi.org/10.1007/s00424-024-02920-5, doi:10.1007/s00424-024-02920-5. This article has 5 citations.