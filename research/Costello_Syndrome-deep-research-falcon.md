---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-04T22:32:52.502098'
end_time: '2026-02-04T22:39:26.011659'
duration_seconds: 393.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Costello Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Costello Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Costello Syndrome**.
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
- **Disease Name:** Costello Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Costello Syndrome**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Costello Syndrome
- MONDO ID: MONDO:0009026
- Category: Mendelian

Pathophysiology description
Costello syndrome (CS) is a Rasopathy caused by heterozygous, germline gain-of-function variants in HRAS that dysregulate Ras protein signal transduction and downstream effector pathways. Core signaling derangements include persistent activation of the RAS/MAPK cascade and aberrant PI3K signaling observed in patient-derived cells, which together perturb proliferation, differentiation, growth, and survival programs across multiple tissues (developmental, cardiac, ectodermal, and oncogenic contexts) (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4).

At the cellular level in the heart, HRAS-mutant atrial-like cardiomyocytes (hiPSC-derived) exhibit an increased fraction of pacemaker-like cells, elevated funny current (If), and a hybrid atrial/nodal transcriptional program with upregulation of ISL1, TBX3, and TBX18, along with disrupted intracellular calcium handling. These electrophysiologic and transcriptional changes mechanistically link hyperactive HRAS to multifocal atrial tachycardia (MAT) and arrhythmogenesis in CS. Pharmacologic modulation in vitro shows that ivabradine (HCN/If inhibitor) and flecainide (Nav1.5 blocker) reduce beating rates, while verapamil (L-type Ca2+ channel blocker) attenuates irregularity, providing proof-of-mechanism and candidate antiarrhythmic strategies (publication URL: https://doi.org/10.1161/circep.123.012022; Apr 2024) (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).

Tumor predisposition is characteristic, with a lifetime risk on the order of 10–15% for embryonal rhabdomyosarcoma, neuroblastoma, and transitional cell carcinoma of the bladder, consistent with the role of HRAS pathway hyperactivation in oncogenic transformation. Cardiovascular disease is prominent and includes congenital heart defects (CHD), hypertrophic cardiomyopathy (HCM), and distinctive supraventricular arrhythmias such as MAT, which may occur independently of HCM. MEK inhibition is discussed as a targeted therapeutic approach in severe RASopathy-associated cardiac disease, reflecting the centrality of MAPK hyperactivation in pathogenesis (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33).

Direct supporting quotes
- “CS-associated gain-of-function HRASG12 mutations in induced pluripotent stem cells-derived [atrial-like cardiomyocytes] trigger transcriptional changes associated with enhanced automaticity and arrhythmic activity consistent with multifocal atrial tachycardia.” (URL: https://doi.org/10.1161/circep.123.012022; Apr 2024) (rodriguez2024hrasmutantcardiomyocyte pages 1-3)
- In HRAS-mutant atrial-like cardiomyocytes, “the hyperpolarization activated cyclic nucleotide gated potassium channel inhibitor ivabradine and the Nav1.5 blocker flecainide significantly decreased beating rates… verapamil attenuated their irregularity,” linking If and Ca2+ handling to the arrhythmic phenotype (URL: https://doi.org/10.1161/circep.123.012022; Apr 2024) (rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Prolonged PI3K signaling has been reported in HRAS patient fibroblasts, supporting a role for PI3K/AKT axis dysregulation in CS pathogenesis (gripp2023hrasrelatedcostellosyndrome pages 31-33).

1. Core Pathophysiology
- Primary mechanisms: Germline HRAS activation drives constitutive Ras signal transduction, with downstream RAS/MAPK hyperactivation and evidence for aberrant PI3K signaling, thereby altering lineage programs, growth, and survival. Cardiac-specific effects include ectopic pacemaker-nodal programming in atrial cardiomyocytes and calcium-handling abnormalities that produce MAT. Oncogenic signaling predisposes to embryonal tumors and bladder carcinoma (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Dysregulated molecular pathways: RAS/MAPK cascade (Ras–Raf–MEK–ERK), PI3K/AKT signaling; cardiomyocyte pacemaker pathway (HCN/If) and Ca2+ homeostasis are second-order effectors in arrhythmia pathogenesis (gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4, rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Affected cellular processes: Proliferation and differentiation (developmental anomalies), hypertrophic growth and excitation–contraction coupling (HCM, arrhythmias), and oncogenic transformation (tumor predisposition). In atrial cells, increased pacemaker-like lineage fraction, If augmentation, and Ca2+ dysregulation are central (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).

2. Key Molecular Players
- Genes/Proteins (HGNC): HRAS (HGNC:5173) is causal; RASopathy-relevant nodes that contextualize pathway biology include RAF1, BRAF, KRAS, NRAS, MAP2K1/2, and MAPK1, although non-HRAS genes are not causal in classical CS (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4).
- Chemical Entities (CHEBI) and targeted agents: MEK inhibitor trametinib is discussed for severe RASopathy cardiac disease (targeting MAPK hyperactivation). In arrhythmic ACM models: ivabradine (HCN/If inhibitor), flecainide (Na+ channel blocker), verapamil (L-type Ca2+ channel blocker) modulated HRAS-driven phenotypes (gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 2-4, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Cell Types (CL): Atrial cardiomyocytes with a shift toward pacemaker-nodal programming; increased pacemaker-like cell proportion is a key mechanistic finding in the arrhythmia model (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Anatomical Locations (UBERON): Heart/atrium (CHD, HCM, MAT), skin (papillomata and ectodermal features), urinary bladder (transitional cell carcinoma), cerebellum (postnatal overgrowth/Chiari) (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4).

3. Biological Processes (GO terms)
- Ras protein signal transduction (GO:0007265) and RAS/MAPK cascade (GO:0000165) are centrally dysregulated by HRAS activation (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4).
- PI3K signaling (GO:0014065) shows prolonged activity in patient fibroblasts, implicating AKT/mTOR axis involvement in growth and oncogenesis (gripp2023hrasrelatedcostellosyndrome pages 31-33).
- Cardiac electrical and calcium-handling processes: regulation of heart rate via pacemaker If current and intracellular calcium ion homeostasis (e.g., GO:0070588), underlying MAT in CS models (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).

4. Cellular Components
- Plasma membrane signaling complexes (RAS at inner leaflet membranes; receptor-proximal signaling), cytosol and nucleus for ERK/AKT effectors; in cardiomyocytes, sarcolemma ion channels (HCN, Nav1.5, Cav1.2) and sarcoplasmic reticulum Ca2+ handling machinery represent key locales of dysfunction (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5, faienza2024cardiacphenotypeand pages 2-4).

5. Disease Progression
- Initial trigger: De novo heterozygous HRAS gain-of-function variant.
- Early developmental effects: Abnormal Ras/MAPK and PI3K signaling perturb organogenesis and growth, producing characteristic craniofacial features, feeding difficulty/failure to thrive, short stature, hypotonia, and neurodevelopmental issues; cerebellar overgrowth and Chiari/hydrocephalus may develop postnatally (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33).
- Cardiac phase: High prevalence of CHD and HCM; atrial electrical remodeling with pacemaker-nodal reprogramming and Ca2+ dysregulation yields MAT/ectopic atrial tachycardia in infancy/early childhood (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Oncogenesis: Elevated lifetime risk for embryonal tumors (RMS, NB) and bladder carcinoma emerges from sustained HRAS effector pathway activation (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33).

6. Phenotypic Manifestations and Statistics
- Cardiovascular involvement is frequent. Reported series document cardiovascular abnormalities in the large majority of patients; CHD around 44%; hypertrophic cardiomyopathy approximately 60–61%; supraventricular arrhythmias in roughly half, including MAT that often presents in infancy and can occur independent of HCM (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33). Recent RASopathy-focused cardiology review reports HCM prevalence “~65% in Costello syndrome” and atrial arrhythmias “up to 56%,” underscoring the burden of cardiac disease (URL: https://doi.org/10.3390/genes15081015; Aug 2024) (faienza2024cardiacphenotypeand pages 7-8).
- Tumor predisposition: Lifetime tumor risk on the order of 10–15% with a spectrum including rhabdomyosarcoma, neuroblastoma, and transitional cell carcinoma of the bladder (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4).

Current applications and real-world implementations
- Precision electrophysiology: The HRAS-mutant atrial-like cardiomyocyte model establishes a mechanistic basis for MAT and nominates HCN inhibition (ivabradine), Nav1.5 blockade (flecainide), and L-type Ca2+ channel blockade (verapamil) as rational antiarrhythmic interventions to test clinically in CS-associated tachyarrhythmias (URL: https://doi.org/10.1161/circep.123.012022; Apr 2024) (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Targeted pathway inhibition: MEK inhibition (e.g., trametinib) is discussed/considered for severe RASopathy-associated cardiac disease, aligning treatment with RAS/MAPK pathway hyperactivation in CS (gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 2-4).
- Surveillance protocols: Given tumor predisposition, longitudinal screening (e.g., abdominal/pelvic ultrasound in early childhood; bladder surveillance later) is standard practice in CS management frameworks (gripp2023hrasrelatedcostellosyndrome pages 1-4).

Expert opinions and analysis
- Contemporary expert summaries emphasize CS as a prototypic Rasopathy with multisystem involvement driven by HRAS gain-of-function, with prominent cardiac and oncologic risks. Arrhythmia mechanisms are increasingly understood through hiPSC models showing pacemaker-nodal reprogramming and Ca2+ dysregulation. These insights prioritize HCN, Na+ channel, and L-type Ca2+ channel modulators in addition to MAPK-directed therapy for organ-specific complications (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5, gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 2-4).

Evidence items with PMIDs/URLs/dates
- Rodríguez NA et al. HRAS-mutant cardiomyocyte model of multifocal atrial tachycardia. Circulation: Arrhythmia & Electrophysiology. Apr 2024. URL: https://doi.org/10.1161/circep.123.012022 (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Gripp KW, Weaver KN. HRAS-related Costello syndrome (GeneReviews-like chapter). 2023. Key statistics and clinical correlations, tumor risk and management principles (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33).
- Faienza MF et al. Cardiac phenotype and gene mutations in RASopathies. Genes. Aug 2024;15:1015. URL: https://doi.org/10.3390/genes15081015 (faienza2024cardiacphenotypeand pages 2-4, faienza2024cardiacphenotypeand pages 7-8).

Gene/protein annotations with ontology terms
- HRAS (HGNC:5173): causal gene; pathway: RAS/MAPK (GO:0000165); process: Ras protein signal transduction (GO:0007265); additional effector: PI3K signaling (GO:0014065). Tissues: heart/atrium (UBERON:0000948/0002080), skin (UBERON:0002097), urinary bladder (UBERON:0001255), cerebellum (UBERON:0002037). Phenotypes: HCM (HPO:0001639), multifocal atrial tachycardia (HPO term). Chemicals: trametinib (CHEBI:90698), ivabradine (CHEBI:83587), flecainide (CHEBI:5126), verapamil (CHEBI:9945) (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4, rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).

Phenotype associations (HPO terms)
- Hypertrophic cardiomyopathy (HPO:0001639): high prevalence and major morbidity (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 7-8).
- Multifocal atrial tachycardia (HPO term): frequent, often early-onset supraventricular arrhythmia linked mechanistically to pacemaker-nodal reprogramming and Ca2+ dysregulation (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5, gripp2023hrasrelatedcostellosyndrome pages 1-4).
- Tumor predisposition phenotypes: rhabdomyosarcoma, neuroblastoma, transitional cell carcinoma of the bladder (HPO tumor terms) (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33).

Cell type involvement (CL terms)
- Atrial cardiomyocytes with increased pacemaker-like cell fraction; mechanistic basis for arrhythmia in CS (CL term for atrial cardiomyocyte) (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).

Anatomical locations (UBERON terms)
- Heart/atrium (cardiac structural and electrophysiological disease); skin (ectodermal features); urinary bladder (solid tumor predisposition); cerebellum (postnatal overgrowth/Chiari) (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4).

Chemical entities (CHEBI terms)
- Trametinib (CHEBI:90698), ivabradine (CHEBI:83587), flecainide (CHEBI:5126), verapamil (CHEBI:9945) (gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 2-4, rodriguez2024hrasmutantcardiomyocyte pages 3-5).

Recent developments and latest research (2023–2024)
- 2024 hiPSC-derived atrial cardiomyocyte modeling established a direct mechanistic link from HRAS gain-of-function to MAT via nodal-like reprogramming and If/Ca2+ dysregulation, and nominated ivabradine, flecainide, and verapamil as rational modulators (Apr 2024; URL: https://doi.org/10.1161/circep.123.012022) (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Contemporary reviews consolidate high cardiac burden and provide updated prevalence ranges for HCM and arrhythmias in RASopathies, including CS, underscoring the need for targeted pathway therapies and careful risk stratification (Aug 2024; URL: https://doi.org/10.3390/genes15081015) (faienza2024cardiacphenotypeand pages 2-4, faienza2024cardiacphenotypeand pages 7-8).
- Expert clinical overviews reaffirm the tumor spectrum and surveillance rationale, as well as the potential role of MAPK pathway inhibition in severe cardiac phenotypes (2023) (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33).

Structured artifact
| Category | Entity (standard name) | Ontology ID | Mechanistic/phenotypic role in Costello syndrome | Evidence |
|---|---|---|---|---|
| Gene | HRAS (HRas proto-oncogene) | HGNC:5173 | Germline gain-of-function HRAS variants cause Costello syndrome; drive developmental defects, tumor predisposition, hypertrophic cardiomyopathy and supraventricular arrhythmias via RAS pathway dysregulation and prolonged PI3K signaling. | (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33) |
| Pathway | RAS/MAPK cascade | GO:0000165 | Constitutively activated in CS; mediates abnormal cell proliferation/differentiation contributing to cardiac hypertrophy and developmental phenotypes. | (gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 2-4, gripp2023hrasrelatedcostellosyndrome pages 31-33) |
| Process | Ras protein signal transduction | GO:0007265 | Upstream signaling node altered by HRAS variants; perturbs downstream MAPK and PI3K/AKT effectors affecting multiple tissues. | (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33) |
| Pathway | PI3K signaling | GO:0014065 | Prolonged/aberrant PI3K/AKT activity reported in patient cells; implicated in oncogenesis and cardiac/myocyte hypertrophic responses. | (gripp2023hrasrelatedcostellosyndrome pages 31-33, faienza2024cardiacphenotypeand pages 2-4) |
| Cell program | Atrial cardiomyocyte / pacemaker-like program (cell fate shift) | CL:0002321 (atrial cardiomyocyte) | HRAS-mutant atrial-like cardiomyocytes adopt hybrid atrial/nodal transcriptional program (↑ISL1, TBX3, TBX18) increasing pacemaker-like cells and automaticity. | (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5) |
| Process | Calcium handling in cardiomyocytes | GO:0006816 / GO:0070588 | Disrupted intracellular Ca2+ homeostasis in HRAS-mutant ACMs contributes to arrhythmic activity and abnormal excitation–contraction coupling. | (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5) |
| Anatomy | Heart / atrium | UBERON:0000948 / UBERON:0002080 | Primary organ system affected: congenital heart defects, hypertrophic cardiomyopathy, and atrial arrhythmias (multifocal atrial tachycardia) are common clinical manifestations. | (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 2-4) |
| Anatomy | Skin | UBERON:0002097 | Ectodermal/cutaneous involvement: papillomata, keratoderma and other skin findings commonly observed in CS. | (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33) |
| Anatomy | Urinary bladder | UBERON:0001255 | Predisposition to transitional cell carcinoma of the bladder reported as part of tumor spectrum in CS. | (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33) |
| Anatomy | Cerebellum | UBERON:0002037 | Postnatal cerebellar overgrowth and Chiari I/hydrocephalus reported; neurodevelopmental involvement linked to HRAS signaling effects. | (gripp2023hrasrelatedcostellosyndrome pages 1-4) |
| Phenotype | Hypertrophic cardiomyopathy | HPO:0001639 | High prevalence (~60% in some series); major determinant of morbidity/mortality in CS patients. | (gripp2023hrasrelatedcostellosyndrome pages 6-8, faienza2024cardiacphenotypeand pages 2-4, gripp2023hrasrelatedcostellosyndrome pages 31-33) |
| Phenotype | Multifocal atrial tachycardia (MAT) | HPO:— (multifocal atrial tachycardia) | Frequent, treatment-resistant supraventricular arrhythmia of infancy/early childhood in CS; mechanistic link to increased pacemaker-like cells and ↑If current. | (rodriguez2024hrasmutantcardiomyocyte pages 1-3, gripp2023hrasrelatedcostellosyndrome pages 1-4, rodriguez2024hrasmutantcardiomyocyte pages 3-5) |
| Phenotype cluster | Rhabdomyosarcoma; Neuroblastoma; Transitional cell carcinoma | HPO:— (see individual tumor terms) | Tumor predisposition (lifetime risk ~10–15% reported) with early-onset pediatric tumors (RMS, NB) and bladder carcinoma risk. | (gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33, gripp2023hrasrelatedcostellosyndrome pages 13-14) |
| Drug | Trametinib (MEK inhibitor) | CHEBI:90698 | Used compassionately/considered for severe RASopathy-associated cardiac disease (MEK inhibition targets hyperactive MAPK signaling). | (gripp2023hrasrelatedcostellosyndrome pages 1-4, faienza2024cardiacphenotypeand pages 2-4, rodriguez2024hrasmutantcardiomyocyte pages 3-5) |
| Drug | Ivabradine (HCN/If inhibitor) | CHEBI:83587 | Reduces elevated beating rates in HRAS-mutant atrial-like cardiomyocytes by inhibiting funny current; shown to decrease automaticity in cellular model. | (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5) |
| Drug | Flecainide (Na+ channel blocker) | CHEBI:5126 | Nav1.5 blockade reduced beating rate in HRAS-mutant ACMs in vitro; evaluated as antiarrhythmic in models/patients. | (rodriguez2024hrasmutantcardiomyocyte pages 3-5) |
| Drug | Verapamil (L-type Ca2+ channel blocker) | CHEBI:9945 | Attenuated irregularity of beating in HRAS-mutant ACMs by modulating Ca2+ flux; supports role of Ca2+ handling in arrhythmogenesis. | (rodriguez2024hrasmutantcardiomyocyte pages 3-5) |


*Table: Compact table summarizing core genes, pathways, cell/tissue involvements, phenotypes and drugs relevant to Costello syndrome, with evidence pointers to the gathered sources (pqac IDs). This aids rapid integration into a disease knowledge base with ontology references.*

References (with links where available)
- Rodríguez NA, Patel N, Dariolli R, et al. HRAS-mutant cardiomyocyte model of multifocal atrial tachycardia. Circulation: Arrhythmia & Electrophysiology. Apr 2024. https://doi.org/10.1161/circep.123.012022 (rodriguez2024hrasmutantcardiomyocyte pages 1-3, rodriguez2024hrasmutantcardiomyocyte pages 3-5).
- Gripp KW, Weaver KN. HRAS-related Costello syndrome. 2023. Summary of epidemiology, phenotype, tumor risk, and management (gripp2023hrasrelatedcostellosyndrome pages 6-8, gripp2023hrasrelatedcostellosyndrome pages 1-4, gripp2023hrasrelatedcostellosyndrome pages 31-33).
- Faienza MF, Meliota G, Mentino D, et al. Cardiac phenotype and gene mutations in RASopathies. Genes. Aug 2024;15:1015. https://doi.org/10.3390/genes15081015 (faienza2024cardiacphenotypeand pages 2-4, faienza2024cardiacphenotypeand pages 7-8).

References

1. (gripp2023hrasrelatedcostellosyndrome pages 1-4): KW Gripp and KN Weaver. Hras-related costello syndrome. Unknown journal, 2023.

2. (gripp2023hrasrelatedcostellosyndrome pages 31-33): KW Gripp and KN Weaver. Hras-related costello syndrome. Unknown journal, 2023.

3. (faienza2024cardiacphenotypeand pages 2-4): Maria Felicia Faienza, Giovanni Meliota, Donatella Mentino, Romina Ficarella, Mattia Gentile, Ugo Vairo, and Gabriele D’amato. Cardiac phenotype and gene mutations in rasopathies. Genes, 15:1015, Aug 2024. URL: https://doi.org/10.3390/genes15081015, doi:10.3390/genes15081015. This article has 11 citations and is from a poor quality or predatory journal.

4. (rodriguez2024hrasmutantcardiomyocyte pages 1-3): Nelson A. Rodríguez, Nihir Patel, Rafael Dariolli, Simon Ng, Angelika G. Aleman, Jingqi Q.X. Gong, Hung-Mo Lin, Matthew Rodríguez, Rebecca Josowitz, Katia Sol-Church, Karen W. Gripp, Xianming Lin, Soomin C. Song, Glenn I. Fishman, Eric A. Sobie, and Bruce D. Gelb. <i>hras</i> -mutant cardiomyocyte model of multifocal atrial tachycardia. Circulation: Arrhythmia and Electrophysiology, Apr 2024. URL: https://doi.org/10.1161/circep.123.012022, doi:10.1161/circep.123.012022. This article has 2 citations and is from a peer-reviewed journal.

5. (rodriguez2024hrasmutantcardiomyocyte pages 3-5): Nelson A. Rodríguez, Nihir Patel, Rafael Dariolli, Simon Ng, Angelika G. Aleman, Jingqi Q.X. Gong, Hung-Mo Lin, Matthew Rodríguez, Rebecca Josowitz, Katia Sol-Church, Karen W. Gripp, Xianming Lin, Soomin C. Song, Glenn I. Fishman, Eric A. Sobie, and Bruce D. Gelb. <i>hras</i> -mutant cardiomyocyte model of multifocal atrial tachycardia. Circulation: Arrhythmia and Electrophysiology, Apr 2024. URL: https://doi.org/10.1161/circep.123.012022, doi:10.1161/circep.123.012022. This article has 2 citations and is from a peer-reviewed journal.

6. (gripp2023hrasrelatedcostellosyndrome pages 6-8): KW Gripp and KN Weaver. Hras-related costello syndrome. Unknown journal, 2023.

7. (faienza2024cardiacphenotypeand pages 7-8): Maria Felicia Faienza, Giovanni Meliota, Donatella Mentino, Romina Ficarella, Mattia Gentile, Ugo Vairo, and Gabriele D’amato. Cardiac phenotype and gene mutations in rasopathies. Genes, 15:1015, Aug 2024. URL: https://doi.org/10.3390/genes15081015, doi:10.3390/genes15081015. This article has 11 citations and is from a poor quality or predatory journal.

8. (gripp2023hrasrelatedcostellosyndrome pages 13-14): KW Gripp and KN Weaver. Hras-related costello syndrome. Unknown journal, 2023.