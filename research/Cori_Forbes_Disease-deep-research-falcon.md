---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-08T18:24:43.342797'
end_time: '2026-03-08T18:52:21.406272'
duration_seconds: 1658.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cori Forbes Disease
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
- **Disease Name:** Cori Forbes Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cori Forbes Disease**.
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
- **Disease Name:** Cori Forbes Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cori Forbes Disease**.
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


## Research Report: Cori–Forbes Disease (Glycogen Storage Disease Type III, GSD III)

### 1) Key concepts, definitions, and current understanding (pathophysiology core)

**Disease definition / genetics.** Cori–Forbes disease is **glycogen storage disease type III (GSD III)**, an autosomal recessive Mendelian disorder caused by biallelic pathogenic variants in **AGL** (HGNC:317), which encodes the **glycogen debranching enzyme (GDE; amylo-α-1,6-glucosidase / 4-α-glucanotransferase)**. Clinical guidelines describe the consequence as “**structurally abnormal glycogen**” with “**defective glucose release from glycogen in the liver and sometimes in the muscles, whereas gluconeogenesis is normal**.” (wicker2023frenchrecommendationsfor pages 1-2)

**Biochemical lesion in glycogenolysis.** GDE is required to complete glycogen breakdown because glycogen phosphorylase cannot remove glucose residues close to branch points. A recent mechanistic study summarizes that GDE deficiency causes accumulation of **phosphorylase-limit dextrin (PLD)**, i.e., the abnormal, incompletely degraded glycogen species: “**Phosphorylase-limit dextrin (PLD)… [is] the type of glycogen which accumulates in GSDIII**.” (mishra2024theautophagicactivator pages 2-3)

**Primary tissue distribution and why multiple organs are affected.** Glycogen stores are most abundant in liver and muscle; accordingly, GSD III affects these tissues, and (for IIIa) also heart, producing a multisystem metabolic myopathy/hepatopathy (mishra2024theautophagicactivator pages 1-2, hannah2023glycogenstoragediseases pages 1-3).

### 2) Molecular pathways and cellular processes dysregulated

**A. Glycogen metabolism dysregulation (core pathway).**
- **Blocked glycogen debranching step** → persistence of branched limit dextrins (PLD) in cytosol → cellular glycogen overload (mishra2024theautophagicactivator pages 2-3, wicker2023frenchrecommendationsfor pages 1-2).

**B. Autophagy–lysosome system involvement (glycogen clearance / organelle stress).**
- In a GSD III mouse model and patient fibroblasts, an autophagy-activating small molecule (GHF-201) improved key cellular phenotypes, including lysosomal abnormalities: in patient fibroblasts “**GHF-201 restored mitochondrial membrane polarization and corrected lysosomal swelling**.” (mishra2024theautophagicactivator pages 1-2)
- These data support a model in which impaired or insufficient glycogen handling intersects with lysosomal/autophagic pathways and cellular stress responses (mishra2024theautophagicactivator pages 1-2).

**C. Mitochondrial dysfunction and oxidative stress.**
- A 2024 review focused on GSDs notes that in GSD III patients there are mitochondrial abnormalities including “**reduced activities of mitochondrial respiratory chain complexes, increased oxidative stress, and altered mitochondrial morphology**,” which may contribute to “**muscle weakness, cardiomyopathy, and hepatic dysfunction**.” (mishra2024mitochondrialdysfunctionin pages 2-4)
- The GHF-201 study’s rescue of mitochondrial membrane polarization provides experimental support that mitochondrial dysfunction is a modifiable component of cellular pathology in GSD III (mishra2024theautophagicactivator pages 1-2).

**D. Fibrosis and structural remodeling (liver and heart).**
- The 2023 Nature Reviews Disease Primers paper and French PNDS guidance both highlight fibrosis/cirrhosis risk (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 1-2). The French recommendations include surveillance for fibrosis/cirrhosis using imaging, and note that MR elastography “may be better to detect fibrosis” though data are limited (wicker2023frenchrecommendationsfor pages 6-8).
- Cardiac remodeling in GSD IIIa includes hypertrophic cardiomyopathy and fibrosis detectable by CMR (late enhancement, T1 mapping/ECV) per PNDS recommendations (wicker2023frenchrecommendationsfor pages 5-6).

### 3) Key molecular players and entities

#### Genes/Proteins
- **AGL / GDE (amylo-α-1,6-glucosidase/4-α-glucanotransferase)**: causal gene/protein; deficiency leads to PLD accumulation (wicker2023frenchrecommendationsfor pages 1-2, mishra2024theautophagicactivator pages 2-3).

#### Chemical entities / metabolites / relevant small molecules
- **Glycogen (PLD/limit dextrin)**: primary accumulated substrate form in GSD III (mishra2024theautophagicactivator pages 2-3).
- **GHF-201**: experimental “autophagic activator” that improved metabolic, structural, lysosomal, and mitochondrial phenotypes in preclinical models (mishra2024theautophagicactivator pages 1-2, mishra2024theautophagicactivator pages 2-3).
- **UX053**: investigational **AGL mRNA** therapeutic (“**1,6-glucosidase 4-alpha-glucanotransferase Messenger Ribonucleic Acid (AGL mRNA)**”) tested in a Phase 1/2 study (terminated) (NCT04990388 chunk 2, NCT04990388 chunk 1).

#### Cell types (CL-aligned)
- **Hepatocytes (CL:0000182)**: hepatic glycogen overload → hepatomegaly, transaminase elevation; fibrosis risk (wicker2023frenchrecommendationsfor pages 1-2, hannah2023glycogenstoragediseases pages 1-3).
- **Skeletal muscle cells / myofibers (e.g., CL:0000515 skeletal muscle cell)**: “massive glycogen accumulation” in muscle biopsy with PAS-positive vacuoles (wicker2023frenchrecommendationsfor pages 6-8).
- **Cardiomyocytes (CL:0000746)** and **cardiac conduction system cells**: hypertrophic cardiomyopathy, arrhythmia risk; conduction system involvement described in recent cardiac review (wicker2023frenchrecommendationsfor pages 5-6, pinos2026cardiovascularinvolvementin pages 17-21).

#### Anatomical locations (UBERON-aligned)
- **Liver (UBERON:0002107)**: hepatomegaly → fibrosis/cirrhosis/HCC risk (wicker2023frenchrecommendationsfor pages 1-2, hannah2023glycogenstoragediseases pages 1-3).
- **Skeletal muscle tissue (UBERON:0001134)**: progressive myopathy, weakness (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 5-6).
- **Heart (UBERON:0000948)** including myocardium and conduction system: LVH/HCM, fibrosis, arrhythmias (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 5-6, pinos2026cardiovascularinvolvementin pages 17-21).

### 4) Disease progression: sequence of events

A commonly described sequence is:
1. **Inherited AGL deficiency** → impaired debranching step of glycogenolysis → **PLD accumulation** (mishra2024theautophagicactivator pages 2-3, wicker2023frenchrecommendationsfor pages 1-2).
2. **Early hepatic/metabolic presentation**: GSDIII “usually starts as a liver disorder characterized by hepatomegaly, hypoglycemia, hyperlipidemia, and hyperketonemia” (mishra2024theautophagicactivator pages 2-3).
3. Over time, **extrahepatic progression**: “**leading to liver disorder followed by fatal myopathy**” in model-organism framing (mishra2024theautophagicactivator pages 1-2), with clinical recognition that muscle involvement can progress with age (wicker2023frenchrecommendationsfor pages 5-6).
4. **Long-term complications**: hepatic fibrosis/cirrhosis and tumors can occur (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 1-2), and cardiac disease (LVH/HCM, arrhythmias) may emerge or progress, requiring structured surveillance (wicker2023frenchrecommendationsfor pages 5-6).

### 5) Phenotypic manifestations (clinical phenotypes) linked to mechanism

From guideline and review sources:
- **Hypoglycemia (ketotic)**: “short fasting hypoglycaemia (less than 4 to 5 h) with no hyperlactataemia” (wicker2023frenchrecommendationsfor pages 1-2).
- **Hepatomegaly, elevated transaminases** (wicker2023frenchrecommendationsfor pages 1-2, hannah2023glycogenstoragediseases media 16fd5731).
- **Myopathy / weakness**: GSD IIIa includes myopathy and weakness; muscle biopsy shows “massive glycogen accumulation… with large vacuoles of muscle fibres” (wicker2023frenchrecommendationsfor pages 6-8, hannah2023glycogenstoragediseases media 16fd5731).
- **Cardiac manifestations**: “Hypertrophic cardiomyopathy can occur in the first years of life” (wicker2023frenchrecommendationsfor pages 1-2) and later LVH/HCM with arrhythmias risk (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 5-6).

### 6) Recent developments and latest research (prioritize 2023–2024)

**A. Autophagy-targeting small molecule therapy (preclinical, 2024).**
- In Agl−/− mice and patient fibroblasts, the autophagy activator **GHF-201** improved locomotor function and metabolic biomarkers and corrected key cellular defects. Importantly, in patient fibroblasts “**GHF-201 restored mitochondrial membrane polarization and corrected lysosomal swelling**,” supporting a mechanistic link between glycogen overload and organelle stress that may be therapeutically targetable (mishra2024theautophagicactivator pages 1-2).
- The same work reiterates epidemiology and natural history framing and notes that currently “patients are only managed by dietary restrictions” (mishra2024theautophagicactivator pages 2-3).

**B. AAV gene therapy engineering breakthrough (JCI, 2024).**
- A major technical barrier for single-vector rAAV gene therapy in GSD III is the ~4.6 kb GDE cDNA size. A 2024 JCI study reports a truncated “mini-GDE” (ΔNter2-GDE) enabling single rAAV delivery; the vector “**allowed significant glycogen reduction in heart and muscle… as well as normalization of histology features and restoration of muscle strength**” in Agl−/− mice and also corrected pathology in a rat model and human cellular models (gardin2024afunctionalminigde pages 1-2).

**C. Gene therapy landscape synthesis (JIMD review, 2024).**
- A 2024 review summarizes multiple strategies for GSD III, including dual-AAV split vectors and heterologous bacterial debranching enzymes, emphasizing immune/toxicity challenges and organ targeting. It notes that liver-targeted strategies can reverse hepatic fibrosis in models, while muscle/cardiac correction requires different delivery considerations (koeberl2024genetherapyfor pages 11-13).

**D. Updated clinical management recommendations (PNDS France, 2023).**
- The 2023 French recommendations provide detailed surveillance frameworks for liver and heart, including the role of cardiac MRI for fibrosis detection (late enhancement, T1 mapping/ECV) and Holter monitoring cadence in patients with HCM (wicker2023frenchrecommendationsfor pages 5-6).

### 7) Current applications and real-world implementations

**Standard-of-care dietary management.** PNDS guidance states: “**The treatment mainly relies on dietary measures**” and specifically that “**preserving gluconeogenesis requires an increased protein intake**.” (wicker2023frenchrecommendationsfor pages 1-2)

**Cardiac-focused dietary strategy (expert analysis).** A recent Nature Reviews Cardiology synthesis (2026) argues that traditional frequent feeding/cornstarch to prevent hypoglycemia may worsen cardiac glycogen burden, and highlights expert-consensus macronutrient guidance and reported improvements in case series with high-protein/low-complex-carbohydrate regimens (pinos2026cardiovascularinvolvementin pages 17-21). (Note: This is authoritative but outside 2023–2024.)

**Surveillance implementations.**
- **Cardiac surveillance:** LVH prevalence reported as **27–86%**, ECG abnormalities in **>80%** of children/adults, and CMR is recommended to assess fibrosis (wicker2023frenchrecommendationsfor pages 5-6).
- **Hepatic surveillance:** abdominal ultrasound and contrast-enhanced MRI are used to monitor hepatomegaly, adenomas, fibrosis/cirrhosis (wicker2023frenchrecommendationsfor pages 5-6, wicker2023frenchrecommendationsfor pages 6-8).

**Real-world research infrastructure.** The French national registry (NCT06616545) is designed to define natural history and sensitive outcomes over ~10 years, capturing metabolic, neurological, cardiac, and biological data in ~150 patients (NCT06616545 chunk 1).

### 8) Expert opinions / authoritative sources (selected)

- **Nature Reviews Disease Primers (2023)** provides authoritative synthesis of GSDs including GSD III and highlights phenotypic variability and risks of hepatic fibrosis/cirrhosis, arrhythmias, and cardiomyopathy (hannah2023glycogenstoragediseases pages 1-3) with a tabulated clinical summary for GSD III (hannah2023glycogenstoragediseases media 16fd5731).
- **French PNDS recommendations (2023)** provide an expert-consensus clinical pathway emphasizing structured monitoring of cardiac and hepatic complications and functional assessments for neuromuscular disease (wicker2023frenchrecommendationsfor pages 5-6, wicker2023frenchrecommendationsfor pages 6-8).

### 9) Relevant statistics and data from recent sources

- **Incidence:** 2023 PNDS reports incidence ~“**1 in 100 000**” (wicker2023frenchrecommendationsfor pages 1-2). A 2024 mechanistic study similarly states incidence “(incidence of **1:100,000**)” (mishra2024theautophagicactivator pages 2-3).
- **Cardiac involvement metrics:** PNDS reports **LVH prevalence 27–86%** and **ECG abnormalities >80%** (wicker2023frenchrecommendationsfor pages 5-6). A 2024 gene-therapy paper notes that “most adult patients display left-ventricle hypertrophy though only ~15% have overt cardiomyopathy” (gardin2024afunctionalminigde pages 1-2).

### 10) Clinical trials and translational pipeline (selected, with URLs/dates)

- **UX053 (AGL mRNA) Phase 1/2 trial (NCT04990388)**, Ultragenyx. Started **2021-10-18**, completed **2023-03-20**, **TERMINATED** (“Sponsor decision not related to safety concerns”). UX053 is an “**mRNA-based biologic**” given by IV infusion; key endpoint includes TEAEs and detailed PK (Cmax, Tmax, AUC). (NCT04990388 chunk 1, NCT04990388 chunk 2) URL: https://clinicaltrials.gov/study/NCT04990388
- **Biomarkers & manifestations study (NCT04574830)** (COMPLETED; completion **2022-06-30**). Primary objective: “**evaluate potential biomarkers of GSD III**”; primary outcome: urine **Hex4 mean and variance**. (NCT04574830 chunk 1) URL: https://clinicaltrials.gov/study/NCT04574830
- **Hypoglycemia incidence & function survey (NCT05196165)** (TERMINATED). Primary objective: “**evaluate the incidence of hypoglycemia**”; outcome: “Number of Hypoglycemic Events During the 26-week Observation Period”; “No investigational product (IP) will be administered.” (NCT05196165 chunk 1) URL: https://clinicaltrials.gov/study/NCT05196165
- **French GSD III Observatory registry (NCT06616545)** (RECRUITING). Captures natural history; primary endpoint includes “Fasting period”; secondary includes “6MWT distance.” (NCT06616545 chunk 1) URL: https://clinicaltrials.gov/study/NCT06616545
- **Pediatric liver fibrosis assessment by elastography (NCT07303140)** (RECRUITING). Primary outcome: “Liver elastography values” with fibrosis staging F0–F4; start **2024-10-18**. (NCT07303140 chunk 1) URL: https://clinicaltrials.gov/study/NCT07303140

---

## Knowledge-base style structured annotations

### Pathophysiology description (narrative)
Cori–Forbes disease (GSD III) is an autosomal recessive disorder caused by AGL/GDE deficiency that blocks complete glycogenolysis at branch points, producing cytosolic accumulation of phosphorylase-limit dextrin (PLD), a structurally abnormal glycogen. The resulting glycogen overload in hepatocytes, skeletal myofibers, and cardiomyocytes leads to fasting intolerance and hepatic injury in early life, with progression to skeletal myopathy and possible cardiac hypertrophy/arrhythmias. Secondary cellular dysfunction includes autophagy–lysosome involvement (lysosomal swelling) and mitochondrial dysfunction (respiratory chain impairment, oxidative stress, impaired membrane polarization), which are being explored as therapeutic targets. Progressive hepatic fibrosis/cirrhosis and cardiac fibrosis may occur, motivating systematic surveillance. (mishra2024theautophagicactivator pages 2-3, wicker2023frenchrecommendationsfor pages 1-2, hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 5-6, mishra2024theautophagicactivator pages 1-2)

### Gene/protein annotations (HGNC) and related processes
- **AGL (HGNC:317)** – causal gene; encodes glycogen debranching enzyme with glucosyltransferase and amylo-1,6-glucosidase activities (wicker2023frenchrecommendationsfor pages 1-2, mishra2024theautophagicactivator pages 2-3).

### GO Biological Processes (examples for annotation)
(These are ontology-aligned labels suitable for curation; evidence is cited for the disrupted biology, not for the GO term IDs themselves.)
- **Glycogen catabolic process** (blocked by GDE deficiency; PLD accumulation) (mishra2024theautophagicactivator pages 2-3, wicker2023frenchrecommendationsfor pages 1-2)
- **Carbohydrate metabolic process / glucose homeostasis** (fasting hypoglycemia; impaired glycogen-derived glucose release with intact gluconeogenesis) (wicker2023frenchrecommendationsfor pages 1-2)
- **Autophagy / lysosome organization** (lysosomal swelling corrected by autophagy activator) (mishra2024theautophagicactivator pages 1-2)
- **Mitochondrial electron transport / oxidative phosphorylation** (reduced respiratory chain activities; oxidative stress) (mishra2024mitochondrialdysfunctionin pages 2-4)
- **Fibrosis / extracellular matrix organization (liver; myocardium)** (clinical fibrosis surveillance and risk) (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 5-6)

### Cellular Components (examples)
- **Cytosol (glycogen/PLD storage; cytosolic accumulation emphasized vs lysosomal storage in other GSDs)** (mishra2024theautophagicactivator pages 2-3)
- **Lysosome (lysosomal swelling; autophagy-lysosome axis)** (mishra2024theautophagicactivator pages 1-2)
- **Mitochondrion (membrane polarization; respiratory chain defects)** (mishra2024theautophagicactivator pages 1-2, mishra2024mitochondrialdysfunctionin pages 2-4)

### Phenotype associations (HP-aligned labels; examples)
- **Hepatomegaly** (wicker2023frenchrecommendationsfor pages 1-2, hannah2023glycogenstoragediseases media 16fd5731)
- **Hypoglycemia (ketotic)** (wicker2023frenchrecommendationsfor pages 1-2)
- **Hyperlipidemia / hyperketonemia** (mishra2024theautophagicactivator pages 2-3)
- **Elevated transaminases** (wicker2023frenchrecommendationsfor pages 1-2)
- **Myopathy / muscle weakness** (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 6-8)
- **Hypertrophic cardiomyopathy / left ventricular hypertrophy** (wicker2023frenchrecommendationsfor pages 1-2, wicker2023frenchrecommendationsfor pages 5-6)
- **Arrhythmia risk** (hannah2023glycogenstoragediseases pages 1-3, wicker2023frenchrecommendationsfor pages 5-6)

### Cell type involvement (CL-aligned; examples)
- Hepatocyte (CL:0000182) (wicker2023frenchrecommendationsfor pages 1-2)
- Skeletal muscle cell / myofiber (CL:0000515) (wicker2023frenchrecommendationsfor pages 6-8)
- Cardiomyocyte (CL:0000746) (wicker2023frenchrecommendationsfor pages 5-6)

### Anatomical locations (UBERON-aligned; examples)
- Liver (UBERON:0002107) (wicker2023frenchrecommendationsfor pages 1-2)
- Skeletal muscle (UBERON:0001134) (wicker2023frenchrecommendationsfor pages 6-8)
- Heart / myocardium (UBERON:0000948) (wicker2023frenchrecommendationsfor pages 5-6)

### Chemical entities (CHEBI-aligned; examples)
- **Glycogen** (accumulated as PLD) (mishra2024theautophagicactivator pages 2-3)

---

## Summary artifacts

| Pathophysiological Domain | Core Defect & Cellular Dysregulation | Affected Tissues & Cell Types | Representative Clinical Phenotypes | Key Evidence & Citations |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Biochemical Defect** | **Enzyme Deficiency:** Biallelic *AGL* variants cause Glycogen Debranching Enzyme (GDE) deficiency.<br>**Accumulation:** Incomplete glycogenolysis leads to cytosolic accumulation of **Phosphorylase-Limit Dextrin (PLD)**, a structurally abnormal glycogen with short outer branches. | **Systemic Expression:**<br>• Liver (Hepatocytes)<br>• Skeletal Muscle (Myofibers)<br>• Heart (Cardiomyocytes) | • **Metabolic:** Fasting hypoglycemia (ketotic), hyperlipidemia, hyperketonemia.<br>• **Growth:** Short stature, failure to thrive in infancy. | *Biomolecules 2024* (mishra2024theautophagicactivator pages 2-3, mishra2024mitochondrialdysfunctionin pages 2-4, mishra2024theautophagicactivator pages 1-2)<br>*J Clin Invest 2024* (gardin2024afunctionalminigde pages 1-2)<br>*Eur J Med Res 2023* (wicker2023frenchrecommendationsfor pages 1-2) |
| **Secondary Cellular Dysfunction** | **Mitochondrial Impairment:** Reduced respiratory chain complex activity, altered morphology, and increased oxidative stress (ROS).<br>**Autophagy Block:** Impaired autophagic flux and lysosomal swelling contribute to cellular toxicity. | • Fibroblasts<br>• Myocytes<br>• Hepatocytes | • **Functional:** Exercise intolerance, muscle fatigue.<br>• **Progression:** Contribution to long-term muscle atrophy and metabolic inflexibility. | *Biomolecules 2024* (mishra2024theautophagicactivator pages 2-3, mishra2024mitochondrialdysfunctionin pages 1-2)<br>*Cell Prolif 2024* (mishra2024theautophagicactivator pages 1-2) |
| **Hepatic Pathophysiology** | **Structural Damage:** Massive glycogen deposition causes hepatocyte ballooning and injury.<br>**Fibrogenesis:** Progression from inflammation to bridging fibrosis, cirrhosis, and potential tumorigenesis (adenoma/HCC). | • Liver Parenchyma | • **Hepatic:** Hepatomegaly (often improves with age), elevated transaminases (AST/ALT), hepatic fibrosis, hepatocellular adenoma/carcinoma risk. | *Nat Rev Dis Primers 2023* (hannah2023glycogenstoragediseases pages 1-3)<br>*Eur J Med Res 2023* (wicker2023frenchrecommendationsfor pages 1-2)<br>*J Clin Invest 2024* (gardin2024afunctionalminigde pages 1-2) |
| **Cardiac & Muscular Pathology** | **Myopathy:** Vacuolar myopathy with myofibrillar disruption.<br>**Cardiomyopathy:** Cytosolic PLD accumulation, cardiomyocyte vacuolation, and **replacement fibrosis** (scarring).<br>**Remodeling:** Massive hypertrophy (LVH) and conduction system deposition. | • Skeletal Muscle<br>• Myocardium<br>• Conduction System (SA/AV nodes) | • **Muscular:** Proximal/distal weakness, muscle wasting, elevated CK.<br>• **Cardiac:** Hypertrophic cardiomyopathy (HCM), left ventricular hypertrophy, arrhythmias, heart failure. | *Nat Rev Cardiol 2026* (pinos2026cardiovascularinvolvementin pages 17-21)<br>*Eur J Med Res 2023* (wicker2023frenchrecommendationsfor pages 5-6, wicker2023frenchrecommendationsfor pages 6-8)<br>*Biomolecules 2024* (mishra2024theautophagicactivator pages 2-3) |


*Table: A summary of the molecular defects, downstream cellular dysfunctions, and resulting clinical phenotypes in GSD III, mapping specific mechanisms to affected tissues and recent literature evidence.*

| Modality / Intervention | Mechanism / Rationale | Development Stage / Status | Key Endpoints / Measures | Selected Recent Citations |
|---|---|---|---|---|
| Dietary therapy: high-protein intake, uncooked cornstarch | Maintain euglycemia between feeds; preserve gluconeogenesis; limit hepatic glycogen re-accumulation; high-protein/low-carbohydrate may benefit cardiac hypertrophy | Standard of care (guidelines) | Fasting tolerance, glucose stability, growth; liver enzymes; lipid profile; symptom control | (wicker2023frenchrecommendationsfor pages 1-2, hannah2023glycogenstoragediseases pages 1-3, pinos2026cardiovascularinvolvementin pages 17-21, gardin2024afunctionalminigde pages 1-2) |
| Multimodal monitoring – liver (ultrasound, MRI ± contrast, MR elastography) | Detect hepatomegaly, adenomas, fibrosis progression; non-invasive fibrosis staging | Recommended in guidelines; prospective pediatric elastography study recruiting | Liver stiffness (F0–F4), adenoma detection/size, hepatomegaly trend | (wicker2023frenchrecommendationsfor pages 5-6, wicker2023frenchrecommendationsfor pages 6-8, NCT07303140 chunk 1) |
| Multimodal monitoring – cardiac (ECG, echocardiography, CMR with LGE/T1, Holter; NT-proBNP) | Detect LVH/HCM, fibrosis, conduction disease/arrhythmias; guide surveillance | Recommended in guidelines; case/series and reviews support HCM/fibrosis detection | LV mass, wall thickness, LGE/fibrosis, arrhythmias (Holter), NT-proBNP | (wicker2023frenchrecommendationsfor pages 5-6, pinos2026cardiovascularinvolvementin pages 17-21, hannah2023glycogenstoragediseases pages 1-3) |
| Small-molecule autophagy activation (GHF-201) | Enhance autophagic flux/lysosomal function; reduce cytosolic PLD; improve mitochondrial membrane potential | Preclinical: Agl−/− mice; patient fibroblasts | Locomotion (open field/rotarod), glycogen reduction (muscle/liver), lysosomal swelling, mitochondrial polarization | (mishra2024theautophagicactivator pages 2-3, mishra2024theautophagicactivator pages 1-2) |
| Gene therapy – single AAV mini-GDE (ΔNter2-GDE) | Truncated GDE transgene enables single-vector delivery; restores debranching | Preclinical: Agl−/− mouse/rat; human myotubes | Glycogen reduction (heart/muscle), normalized histology, muscle strength restoration | (gardin2024afunctionalminigde pages 1-2) |
| Gene therapy – AAV pullulanase (heterologous debranching enzyme) | Bacterial pullulanase substitutes GDE activity; liver/muscle targeting | Preclinical (mice), multiple promoters/vectors evaluated | Glycogen reduction (liver/muscle), reversal of hepatic fibrosis, improved muscle function | (koeberl2024genetherapyfor pages 11-13) |
| Gene therapy – dual AAV split hGDE | Overcome AGL cDNA size limits via dual vectors | Preclinical; high-dose requirements and immunogenicity noted | Restoration of hGDE activity in liver/muscle; safety/CTL response considerations | (koeberl2024genetherapyfor pages 11-13) |
| mRNA therapy – UX053 (NCT04990388) | IV AGL mRNA (with ATX95 excipient) to transiently restore GDE | Phase 1/2; TERMINATED (sponsor decision, not safety) | Safety/tolerability (TEAEs), PK (Cmax, Tmax, AUC, t½, CL, Vss) | (NCT04990388 chunk 1, NCT04990388 chunk 2) |
| Biomarker study – Hexose tetrasaccharide (Hex4) (NCT04574830) | Evaluate urinary Hex4 as exploratory biomarker of glycogen burden | Observational; COMPLETED | Urine Hex4 mean/variance over ~35 days | (NCT04574830 chunk 1) |
| Hypoglycemia survey – incidence and function (NCT05196165) | Real-world hypoglycemia rate and functional status under standard care | Observational; TERMINATED | Number of hypoglycemic events (26 weeks); motor/strength batteries (e.g., 6MWT) | (NCT05196165 chunk 1) |
| National registry – French GSD III Observatory (NCT06616545) | Natural history, outcomes, prognostic factors; standard-of-care capture | Registry; RECRUITING (150 target) | Fasting duration, 6MWT distance; metabolic, cardiac, neuromuscular outcomes | (NCT06616545 chunk 1) |
| Pediatric liver elastography – fibrosis assessment (NCT07303140) | Non-invasive staging to reduce need for biopsy in pediatric GSD III | Observational; RECRUITING | Liver elastography stiffness (F0–F4), longitudinal trends | (NCT07303140 chunk 1) |


*Table: Structured summary of current clinical management, monitoring, and emerging therapeutic strategies for GSD III, alongside active/completed studies and registries. It consolidates modalities, mechanisms, development stages, endpoints, and citations to guide evidence-based practice and research planning.*

---

## Notes on evidence completeness
This report prioritizes 2023–2024 peer-reviewed sources and guidelines for mechanistic and translational claims. Some detailed quantitative natural-history estimates (e.g., precise fibrosis stage distributions by age, genotype–phenotype penetrance across cohorts) were not available in the retrieved text segments and would require additional targeted cohort papers beyond the current evidence set.

References

1. (wicker2023frenchrecommendationsfor pages 1-2): Camille Wicker, Aline Cano, Valérie Decostre, Roseline Froissart, François Maillot, Ariane Perry, François Petit, Catherine Voillot, Karim Wahbi, Joëlle Wenz, Pascal Laforêt, and Philippe Labrune. French recommendations for the management of glycogen storage disease type iii. European Journal of Medical Research, Jul 2023. URL: https://doi.org/10.1186/s40001-023-01212-5, doi:10.1186/s40001-023-01212-5. This article has 14 citations and is from a peer-reviewed journal.

2. (mishra2024theautophagicactivator pages 2-3): Kumudesh Mishra, Sahar Sweetat, Saja Baraghithy, Uri Sprecher, Monzer Marisat, Sultan Bastu, Hava Glickstein, Joseph Tam, Hanna Rosenmann, Miguel Weil, Edoardo Malfatti, and Or Kakhlon. The autophagic activator ghf-201 can alleviate pathology in a mouse model and in patient fibroblasts of type iii glycogenosis. Biomolecules, 14:893, Jul 2024. URL: https://doi.org/10.3390/biom14080893, doi:10.3390/biom14080893. This article has 4 citations.

3. (mishra2024theautophagicactivator pages 1-2): Kumudesh Mishra, Sahar Sweetat, Saja Baraghithy, Uri Sprecher, Monzer Marisat, Sultan Bastu, Hava Glickstein, Joseph Tam, Hanna Rosenmann, Miguel Weil, Edoardo Malfatti, and Or Kakhlon. The autophagic activator ghf-201 can alleviate pathology in a mouse model and in patient fibroblasts of type iii glycogenosis. Biomolecules, 14:893, Jul 2024. URL: https://doi.org/10.3390/biom14080893, doi:10.3390/biom14080893. This article has 4 citations.

4. (hannah2023glycogenstoragediseases pages 1-3): William B. Hannah, Terry G. J. Derks, Mitchell L. Drumm, Sarah C. Grünert, Priya S. Kishnani, and John Vissing. Glycogen storage diseases. Nature Reviews Disease Primers, 9:1-23, Sep 2023. URL: https://doi.org/10.1038/s41572-023-00456-z, doi:10.1038/s41572-023-00456-z. This article has 102 citations.

5. (mishra2024mitochondrialdysfunctionin pages 2-4): Kumudesh Mishra and Or Kakhlon. Mitochondrial dysfunction in glycogen storage disorders (gsds). Biomolecules, 14:1096, Sep 2024. URL: https://doi.org/10.3390/biom14091096, doi:10.3390/biom14091096. This article has 9 citations.

6. (wicker2023frenchrecommendationsfor pages 6-8): Camille Wicker, Aline Cano, Valérie Decostre, Roseline Froissart, François Maillot, Ariane Perry, François Petit, Catherine Voillot, Karim Wahbi, Joëlle Wenz, Pascal Laforêt, and Philippe Labrune. French recommendations for the management of glycogen storage disease type iii. European Journal of Medical Research, Jul 2023. URL: https://doi.org/10.1186/s40001-023-01212-5, doi:10.1186/s40001-023-01212-5. This article has 14 citations and is from a peer-reviewed journal.

7. (wicker2023frenchrecommendationsfor pages 5-6): Camille Wicker, Aline Cano, Valérie Decostre, Roseline Froissart, François Maillot, Ariane Perry, François Petit, Catherine Voillot, Karim Wahbi, Joëlle Wenz, Pascal Laforêt, and Philippe Labrune. French recommendations for the management of glycogen storage disease type iii. European Journal of Medical Research, Jul 2023. URL: https://doi.org/10.1186/s40001-023-01212-5, doi:10.1186/s40001-023-01212-5. This article has 14 citations and is from a peer-reviewed journal.

8. (NCT04990388 chunk 2):  Safety, Tolerability, and Pharmacokinetics of UX053 in Patients With Glycogen Storage Disease Type III (GSD III). Ultragenyx Pharmaceutical Inc. 2021. ClinicalTrials.gov Identifier: NCT04990388

9. (NCT04990388 chunk 1):  Safety, Tolerability, and Pharmacokinetics of UX053 in Patients With Glycogen Storage Disease Type III (GSD III). Ultragenyx Pharmaceutical Inc. 2021. ClinicalTrials.gov Identifier: NCT04990388

10. (pinos2026cardiovascularinvolvementin pages 17-21): Tomàs Pinós, Richard M. Cubbon, Alfredo Santalla, Carmen Fiuza-Luces, Alejandro Santos-Lozano, Miguel A. Martín, Joaquín Arenas, Joachim Nielsen, Niels Ørtenblad, and Alejandro Lucia. Cardiovascular involvement in glycogen storage diseases. Nature reviews. Cardiology, Jun 2026. URL: https://doi.org/10.1038/s41569-025-01171-w, doi:10.1038/s41569-025-01171-w. This article has 2 citations.

11. (hannah2023glycogenstoragediseases media 16fd5731): William B. Hannah, Terry G. J. Derks, Mitchell L. Drumm, Sarah C. Grünert, Priya S. Kishnani, and John Vissing. Glycogen storage diseases. Nature Reviews Disease Primers, 9:1-23, Sep 2023. URL: https://doi.org/10.1038/s41572-023-00456-z, doi:10.1038/s41572-023-00456-z. This article has 102 citations.

12. (gardin2024afunctionalminigde pages 1-2): Antoine Gardin, Jérémy Rouillon, Valle Montalvo-Romeral, Lucille Rossiaud, Patrice Vidal, Romain Launay, Mallaury Vie, Youssef Krimi Benchekroun, Jérémie Cosette, Bérangère Bertin, Tiziana La Bella, Guillaume Dubreuil, Justine Nozi, Louisa Jauze, Romain Fragnoud, Nathalie Daniele, Laetitia Van Wittenberghe, Jérémy Esque, Isabelle André, Xavier Nissan, Lucile Hoch, and Giuseppe Ronzitti. A functional mini-gde transgene corrects impairment in models of glycogen storage disease type iii. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci172018, doi:10.1172/jci172018. This article has 19 citations and is from a highest quality peer-reviewed journal.

13. (koeberl2024genetherapyfor pages 11-13): Dwight D. Koeberl, Rebecca L. Koch, Jeong‐A. Lim, Elizabeth D. Brooks, Benjamin D. Arnson, Baodong Sun, and Priya S. Kishnani. Gene therapy for glycogen storage diseases. Journal of Inherited Metabolic Disease, 47:93-118, Jul 2024. URL: https://doi.org/10.1002/jimd.12654, doi:10.1002/jimd.12654. This article has 28 citations and is from a peer-reviewed journal.

14. (NCT06616545 chunk 1):  French Observatory for Patients with Type 3 Glycogenosis. Institut de Myologie, France. 2013. ClinicalTrials.gov Identifier: NCT06616545

15. (NCT04574830 chunk 1):  Study to Evaluate Biomarkers and Clinical Manifestations in Individuals With Glycogen Storage Disease Type III (GSD III). Ultragenyx Pharmaceutical Inc. 2020. ClinicalTrials.gov Identifier: NCT04574830

16. (NCT05196165 chunk 1):  Clinical Survey Study to Assess Physical Function and the Incidence of Hypoglycemia in Participants With Glycogen Storage Disease Type III. Ultragenyx Pharmaceutical Inc. 2022. ClinicalTrials.gov Identifier: NCT05196165

17. (NCT07303140 chunk 1):  Non-invasive Assessment of Liver Fibrosis in a French Cohort of Pediatric Patients With Type III Glycogen Storage Disease: Current State and Perspectives. University Hospital, Strasbourg, France. 2024. ClinicalTrials.gov Identifier: NCT07303140

18. (mishra2024mitochondrialdysfunctionin pages 1-2): Kumudesh Mishra and Or Kakhlon. Mitochondrial dysfunction in glycogen storage disorders (gsds). Biomolecules, 14:1096, Sep 2024. URL: https://doi.org/10.3390/biom14091096, doi:10.3390/biom14091096. This article has 9 citations.
