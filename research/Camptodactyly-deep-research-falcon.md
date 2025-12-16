---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:03.561228'
end_time: '2025-12-15T09:18:54.504414'
duration_seconds: 350.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Camptodactyly
  mondo_id: ''
  category: Musculoskeletal Disorder
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Camptodactyly
- **MONDO ID:**  (if available)
- **Category:** Musculoskeletal Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Camptodactyly**.
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
- **Disease Name:** Camptodactyly
- **MONDO ID:**  (if available)
- **Category:** Musculoskeletal Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Camptodactyly**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Camptodactyly
- MONDO ID: (not confirmed in this report)
- Category: Musculoskeletal Disorder

Executive Summary
Camptodactyly (fixed flexion contracture of the finger(s), most commonly the proximal interphalangeal joint) emerges from convergent developmental mechanisms that reduce fetal movement (fetal akinesia) and/or alter periarticular connective tissues, tendons, and synovial surfaces. In isolated forms, local muscle–tendon imbalance and fibroconnective remodeling are implicated; in syndromic forms, pathogenic variants in sarcomeric, extracellular matrix, or neuromuscular-development genes drive reduced in utero motion and subsequent contracture formation. A distinct mechanistic axis involves PRG4 (lubricin) deficiency in CACP syndrome, causing non-inflammatory arthropathy with early camptodactyly through loss of joint surface lubrication and synovial hyperplasia. Recent work in 2023–2024 further expands genetic etiologies (e.g., ACTC1, ECEL1), and consolidates the fetal akinesia–contracture paradigm for distal arthrogryposis (DA). (chong2023variantsinactc1 pages 1-5, bagrul2023anovelmutation pages 2-4, illes2024heterogenicgeneticbackground pages 2-3, li2023casereportidentification pages 1-2, jing2024anovelcompound pages 3-6, shashaani2025juvenileidiopathicarthritis pages 2-4)

1) Core Pathophysiology
- Primary mechanisms
  - Fetal akinesia as the proximate cause of congenital joint contractures, including camptodactyly: decreased in utero movement promotes accumulation and shortening of periarticular connective tissues, setting fixed flexion posture at birth. This is a shared endpoint across DA and many arthrogryposis conditions. “The fundamental pathomechanism across arthrogryposis types is reduced fetal movement … leading to connective tissue accumulation and joint contracture.” (quote) (https://doi.org/10.3390/children11070861, 2024) (illes2024heterogenicgeneticbackground pages 1-2, illes2024heterogenicgeneticbackground pages 2-3)
  - Sarcomere dysfunction in skeletal muscle: pathogenic variants in sarcomeric proteins impair contraction/relaxation dynamics, reducing fetal limb motion and producing non-progressive congenital contractures. 2023 evidence extends this to ACTC1, indicating shared actin functions in cardiac and skeletal muscle and linking DA to cardiac defects in some families. (https://doi.org/10.1016/j.xhgg.2023.100213, Jul 2023) (chong2023variantsinactc1 pages 1-5)
  - Extracellular matrix/lubrication failure (CACP): PRG4 loss-of-function abolishes surface lubrication and anti-adhesive properties of synovial/cartilage interfaces, provoking non-inflammatory arthropathy, synovial hyperplasia, and progressive stiffness that manifests early as camptodactyly. “CACP syndrome … caused by biallelic pathogenic mutations in the PRG4 gene … characterized by early-onset camptodactyly, noninflammatory arthropathy …” (quote) (https://doi.org/10.1186/s12969-023-00793-z, Jan 2023; https://doi.org/10.1186/s12891-025-09069-x, Aug 2025) (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 1-2, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Neurodevelopmental/neuromuscular junction contributors (DA5D): ECEL1 variants disrupt neuromuscular development/innervation, decreasing fetal movement and driving contractures with downstream cartilage/tissue changes. (https://doi.org/10.3389/fneur.2024.1343025, Jan 2024) (jing2024anovelcompound pages 3-6)

- Dysregulated molecular pathways
  - Sarcomere assembly and contractile regulation: actin–myosin interaction, troponin–tropomyosin complex function, calcium sensitivity; GO processes include sarcomere organization and regulation of muscle contraction. (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)
  - Extracellular matrix organization and boundary lubrication of articular surfaces: PRG4-dependent anti-adhesion and lubrication; synovial homeostasis. (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Neuromuscular development and proteolysis (ECEL1): affecting motor circuitry and muscle activation. (jing2024anovelcompound pages 3-6)

- Affected cellular processes
  - Myofiber contraction/relaxation kinetics and fetal motor activity (skeletal myocytes). (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)
  - Synovial fibroblast and superficial-zone chondrocyte function in producing lubricin and maintaining non-adhesive, low-friction joint surfaces. (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Periarticular fibroblast remodeling of volar plate/tendon sheath with immobilization or reduced motion, resulting in shortening and fibrosis (inferred by fetal akinesia model). (illes2024heterogenicgeneticbackground pages 2-3)

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - PRG4 (Lubricin): secreted mucinous glycoprotein; loss causes CACP with early camptodactyly and non-inflammatory arthropathy. (https://doi.org/10.1186/s12969-023-00793-z, 2023; https://doi.org/10.1186/s12891-025-09069-x, 2025) (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Sarcomeric DA genes: TNNT3 (fast skeletal troponin T), TNNI2 (fast skeletal troponin I), TPM2 (beta-tropomyosin), MYH3/MYH8 (embryonic/perinatal myosin heavy chains), ACTC1 (cardiac alpha-actin newly linked to DA), among others; variants impair fetal muscle movement leading to contractures. (https://doi.org/10.3390/children11070861, 2024; https://doi.org/10.1016/j.xhgg.2023.100213, 2023) (illes2024heterogenicgeneticbackground pages 2-3, chong2023variantsinactc1 pages 1-5)
  - FBN2 (Fibrillin-2): ECM microfibril component; missense variants disrupting disulfide bonds cause congenital contractural arachnodactyly with camptodactyly. (https://doi.org/10.3389/fgene.2023.1035887, 2023) (li2023casereportidentification pages 1-2)
  - ECEL1 (Endothelin-converting enzyme-like 1): recessive variants cause DA5D; neuromuscular developmental mechanism culminating in joint dysfunction and cartilage degradation. (https://doi.org/10.3389/fneur.2024.1343025, 2024) (jing2024anovelcompound pages 3-6)

- Chemical Entities (CHEBI)
  - Hyaluronic acid (HA), endogenous synovial lubricant (contextual to joint lubrication; supportive clinical use is outside the current evidence set here). (Context alignment without direct evidence citation)

- Cell Types (CL)
  - Skeletal muscle fibers/myocytes (sarcomere dysfunction in DA). (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)
  - Synovial fibroblasts and superficial-zone chondrocytes (PRG4 production). (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Motor neurons/peripheral nerve elements (ECEL1). (jing2024anovelcompound pages 3-6)

- Anatomical Locations (UBERON)
  - Proximal interphalangeal joint of finger; volar plate; flexor tendons/tendon sheaths. (anatomical context)
  - Synovium and articular cartilage (CACP). (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Fetal limb skeletal muscle. (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)

3) Biological Processes (GO terms) disrupted
- Sarcomere organization (GO:0045214) and muscle contraction (GO:0006936): DA due to sarcomeric variants (ACTC1, TNNT3/TNNI2/TPM2/MYH3/MYH8) leading to reduced fetal movement and contractures. (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)
- Actin filament-based process (GO:0030029): ACTC1 and related sarcomeric perturbations in DA. (chong2023variantsinactc1 pages 1-5)
- Extracellular matrix organization (GO:0030198) and elastic fiber assembly (GO:0030199): FBN2 variants disrupt ECM microfibrils, causing congenital contractures including camptodactyly. (li2023casereportidentification pages 1-2)
- Regulation of inflammatory response (GO:0050727) and synovial surface homeostasis via PRG4: CACP with non-inflammatory arthropathy and synovial hyperplasia when PRG4 is absent. (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
- Nervous system development (GO:0007399) and proteolysis (GO:0006508): ECEL1 in neuromuscular development affecting fetal movement. (jing2024anovelcompound pages 3-6)

4) Cellular Components (where processes occur)
- Myofibril/sarcomere (skeletal muscle fibers): perturbations in actin–myosin–troponin–tropomyosin assemblies (sarcomeric Z-disk/A-band/I-band compartments). (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)
- Extracellular space and cartilage surface boundary layer: PRG4 localized to synovial fluid and cartilage surface film; synovial lining and superficial cartilage zone. (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
- Extracellular microfibrils of connective tissues (fibrillin-2). (li2023casereportidentification pages 1-2)
- Neuromuscular junction / peripheral nerve terminals (functional locus affected in ECEL1-related DA5D). (jing2024anovelcompound pages 3-6)

5) Disease Progression and Sequence of Events
- Sarcomeric/neuromuscular genetic forms (DA spectrum)
  1) Germline variant in sarcomeric or neuromuscular-development gene → 2) impaired fetal skeletal muscle contraction or innervation → 3) fetal akinesia and sustained joint positioning → 4) fibroconnective tissue shortening of volar plate and tendons → 5) fixed flexion deformity (camptodactyly) at birth; typically non-progressive but may require therapy. 2023–2024 studies underscore this chain, including new evidence for ACTC1 in DA with cardiac involvement, and ECEL1 in DA5D with early cartilage changes. (https://doi.org/10.1016/j.xhgg.2023.100213, 2023; https://doi.org/10.3389/fneur.2024.1343025, 2024; https://doi.org/10.3390/children11070861, 2024) (chong2023variantsinactc1 pages 1-5, jing2024anovelcompound pages 3-6, illes2024heterogenicgeneticbackground pages 2-3)

- PRG4 deficiency (CACP)
  1) Biallelic truncating or LOF PRG4 variants → 2) loss of lubricin at joint surfaces → 3) synovial hyperplasia and non-inflammatory arthropathy (poor boundary lubrication, abnormal adhesion, joint effusions) → 4) progressive stiffness and contractures, with early camptodactyly as a sentinel sign, and later coxa vara and large-joint involvement. This mechanism is repeatedly documented in cohort/case reports. (https://doi.org/10.1186/s12969-023-00793-z, 2023; https://doi.org/10.1186/s12891-025-09069-x, 2025) (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)

6) Phenotypic Manifestations and Clinicopathologic Correlation
- Key clinical phenotypes (HP)
  - Camptodactyly (HP:0012385), often bilateral; proximal interphalangeal involvement; may be isolated or syndromic (DA, CACP). (illes2024heterogenicgeneticbackground pages 2-3, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Distal arthrogryposis features (HP:0002829) including clubfoot and limited range of motion; in ACTC1 families, co-occurring congenital heart disease. (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)
  - Non-inflammatory arthropathy with synovial hyperplasia and effusion (CACP), coxa vara, and occasional pericardial effusion. (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
  - Arachnodactyly and generalized contractures in FBN2-related congenital contractural arachnodactyly. (li2023casereportidentification pages 1-2)

- Relationship to mechanisms
  - DA phenotypes reflect timing/degree of fetal akinesia from sarcomeric or neuromuscular defects; more severe or earlier akinesia yields more extensive contractures. (https://doi.org/10.3390/children11070861, 2024) (illes2024heterogenicgeneticbackground pages 2-3)
  - CACP camptodactyly is often among the earliest signs, consistent with synovial/joint-surface pathology from PRG4 deficiency predating large-joint deformities. (https://doi.org/10.1186/s12891-025-09069-x, 2025) (shashaani2025juvenileidiopathicarthritis pages 2-4)

Recent Developments (2023–2024 prioritized)
- Discovery that ACTC1 missense variants can underlie DA with congenital heart defects extends the sarcomere gene spectrum and reinforces the shared biophysical basis of reduced fetal movement leading to distal contractures, including camptodactyly. (URL: https://doi.org/10.1016/j.xhgg.2023.100213; published Jul 2023) (chong2023variantsinactc1 pages 1-5)
- Case-based and review evidence link multiple DA genes (TNNT3, TNNI2, TPM2, MYH3, etc.) to the fetal akinesia–contracture mechanism; 2024 review emphasizes heterogeneity and high diagnostic yield via exome sequencing. (URL: https://doi.org/10.3390/children11070861; published Jul 2024) (illes2024heterogenicgeneticbackground pages 2-3)
- PRG4 CACP reports (2023–2025) continue to highlight early camptodactyly, non-inflammatory arthropathy, and diagnostic pitfalls (misdiagnosis as JIA), clarifying the synovial, lubrication, and surface anti-adhesive biology of lubricin. (URLs: https://doi.org/10.1186/s12969-023-00793-z, Jan 2023; https://doi.org/10.1186/s12891-025-09069-x, Aug 2025) (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)
- ECEL1-associated DA5D (2024) underscores neuromuscular development defects leading to joint dysfunction and cartilage degradation, broadening etiologic mechanisms beyond the sarcomere and ECM. (URL: https://doi.org/10.3389/fneur.2024.1343025; Jan 2024) (jing2024anovelcompound pages 3-6)
- FBN2 missense variants disrupting disulfide bonds (2023) affirm ECM microfibril defects as a basis for congenital contractures and camptodactyly in Beals syndrome. (URL: https://doi.org/10.3389/fgene.2023.1035887; Mar 2023) (li2023casereportidentification pages 1-2)

Current Applications and Implementations
- Genetic testing panels/exome sequencing for DA and suspected CACP improve diagnostic accuracy and counseling; reviews and case reports document high yield and impact on prenatal counseling and management. (URL: https://doi.org/10.3390/children11070861; 2024) (illes2024heterogenicgeneticbackground pages 2-3)
- Clinical differentiation of CACP from JIA (non-inflammatory labs, lack of response to immunosuppression, presence of early camptodactyly, and PRG4 variants) prevents ineffective treatments and guides supportive care. (URLs: https://doi.org/10.1186/s12969-023-00793-z, 2023; https://doi.org/10.1186/s12891-025-09069-x, 2025) (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)

Expert Opinions and Analysis
- DA as a muscle-centric disorder with fetal akinesia as final common pathway is a unifying concept, supported by sarcomeric gene discoveries including ACTC1 in 2023. This strengthens the practice of prioritizing skeletal muscle gene panels in camptodactyly with distal contractures and suggests that biophysical assessments of variant impact on actin–myosin interactions are clinically relevant. (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3)
- For CACP, synovial biology and boundary lubrication are central: “CACP syndrome … caused by biallelic … PRG4 … early-onset camptodactyly, noninflammatory arthropathy …” (quote), arguing that therapies should focus on restoring lubrication/anti-adhesion rather than immunosuppression. (bagrul2023anovelmutation pages 2-4)
- ECM microfibril integrity (FBN2) is a key axis in congenital contractures; variant classes that disrupt disulfide bonds may predict severe phenotypes with camptodactyly and arachnodactyly. (li2023casereportidentification pages 1-2)

Relevant Statistics and Data
- DA diagnostic yield and gene spectrum: 2024 review summarizes numerous implicated genes with high diagnostic yield using exome sequencing (approx. mid-two-digit percentage in cited series within the review), and emphasizes fetal akinesia as the mechanistic link to contractures. (URL: https://doi.org/10.3390/children11070861; 2024) (illes2024heterogenicgeneticbackground pages 2-3)
- CACP cohort-level features are consistently reported across case series: early camptodactyly and non-inflammatory arthropathy with PRG4 LOF; repeated misdiagnosis as JIA. (URLs: https://doi.org/10.1186/s12969-023-00793-z, 2023; https://doi.org/10.1186/s12891-025-09069-x, 2025) (bagrul2023anovelmutation pages 2-4, shashaani2025juvenileidiopathicarthritis pages 2-4)

Embedded Summary Table
| Gene (HGNC) | Protein / Function | Mechanistic category | Primary cell types (CL terms) | Primary tissues (UBERON terms) | Key pathway / GO processes (GO terms) | Representative phenotype (HP terms) | Representative syndrome / context | Evidence |
|---|---|---|---|---|---|---|---|---|
| PRG4 | Lubricin, secreted mucinous glycoprotein that provides boundary lubrication and anti-adhesive surface properties | Extracellular matrix / lubrication; synovial homeostasis; anti-inflammatory signaling | Synovial fibroblast, superficial-zone chondrocyte (CL) | Synovium, articular cartilage, tendon surfaces (UBERON) | Extracellular matrix organization (GO:0030198); regulation of inflammatory response (GO:0050727) | Camptodactyly; non-inflammatory arthropathy; early joint degeneration (HP) | Camptodactyly–arthropathy–coxa vara–pericarditis (CACP) syndrome | https://doi.org/10.1186/s12969-023-00793-z (2023) (bagrul2023anovelmutation pages 2-4) |
| FBN2 | Fibrillin-2, ECM microfibril component required for elastic fiber assembly and connective tissue integrity | Extracellular matrix / structural support; microfibril assembly; disrupted disulfide bonds impair ECM stability | Fibroblasts, tendon/ligament fibroblasts, developing chondrocytes (CL) | Tendons, ligaments, developing cartilage, connective tissue (UBERON) | Extracellular matrix organization (GO:0030198); elastic fiber assembly (GO:0030199) | Congenital contractures including camptodactyly; arachnodactyly (HP) | Congenital contractural arachnodactyly / Beals syndrome (FBN2-related) | https://doi.org/10.3389/fgene.2023.1035887 (2023) (li2023casereportidentification pages 1-2) |
| ACTC1 | Cardiac alpha-actin (actin filament component) — shown to cause DA when mutated | Sarcomere / actin filament dysfunction → impaired contractility and reduced fetal movement | Skeletal myofibers, myoblasts (CL) | Developing skeletal muscle of limb (UBERON) | Muscle contraction (GO:0006936); actin filament-based process (GO:0030029) | Distal arthrogryposis with camptodactyly and congenital heart defects (HP) | Distal arthrogryposis subtype with cardiac involvement (ACTC1 missense variants) | https://doi.org/10.1016/j.xhgg.2023.100213 (2023) (chong2023variantsinactc1 pages 1-5) |
| DA sarcomere genes (TNNT3, TNNI2, TPM2, MYH3) | Troponin/tropomyosin/myosin sarcomeric proteins regulating contraction and calcium sensitivity | Sarcomere/tropomyosin dysfunction → altered contractile regulation, fetal akinesia → joint contracture & fibrosis | Skeletal muscle fibers, developing myocytes (CL) | Fetal limb skeletal muscle (UBERON) | Sarcomere organization (GO:0045214); regulation of muscle contraction (GO:0010881) | Distal arthrogryposis, congenital camptodactyly (HP) | Classic distal arthrogryposis (DA) cohorts; genes frequently implicated in DA | https://doi.org/10.3390/children11070861 (2024) (illes2024heterogenicgeneticbackground pages 2-3) |
| ECEL1 | Endothelin-converting enzyme–like 1, membrane metalloprotease implicated in neuromuscular development | Neurodevelopment / motor neuron–related → impaired innervation or neuromuscular signaling → reduced fetal movement and fibrosis | Motor neurons, peripheral neuronal precursors, skeletal muscle cells (CL) | Peripheral nervous system, developing limb muscle (UBERON) | Nervous system development (GO:0007399); proteolysis (GO:0006508) | DA5D-type distal arthrogryposis with camptodactyly; joint dysfunction and cartilage degradation (HP) | Distal arthrogryposis type 5D (ECEL1 compound heterozygous variants) | https://doi.org/10.3389/fneur.2024.1343025 (2024) (jing2024anovelcompound pages 3-6) |
| Fetal akinesia (mechanism) | Mechanistic category rather than single gene: reduced movement in utero causes connective tissue shortening and joint fixation | Developmental mechanotransduction → connective tissue remodeling, fibrosis, tendon/volar-plate contracture | Fetal myocytes, joint-associated fibroblasts (CL) | Developing joints, tendons, volar plate of digits (UBERON) | Mechanotransduction and developmental processes (GO:0034405); extracellular matrix organization (GO:0030198) | Congenital contractures including camptodactyly (HP) | Common final pathway for isolated and genetic syndromic camptodactyly (e.g., DA, CACP) | https://doi.org/10.3390/children11070861 (2024) (illes2024heterogenicgeneticbackground pages 2-3) |


*Table: Concise mapping of key genes/proteins to mechanisms, cell types, tissues, GO processes and representative phenotypes/syndromes; evidence links each row to a source from the gathered literature for mechanistic curation.*

Ontology-ready Annotations
- Genes/Proteins (HGNC): PRG4; TNNT3; TNNI2; TPM2; MYH3; ACTC1; FBN2; ECEL1. (chong2023variantsinactc1 pages 1-5, illes2024heterogenicgeneticbackground pages 2-3, li2023casereportidentification pages 1-2, jing2024anovelcompound pages 3-6, shashaani2025juvenileidiopathicarthritis pages 2-4)
- Biological Process (GO): sarcomere organization (GO:0045214); muscle contraction (GO:0006936); actin filament-based process (GO:0030029); extracellular matrix organization (GO:0030198); elastic fiber assembly (GO:0030199); regulation of inflammatory response (GO:0050727); nervous system development (GO:0007399); proteolysis (GO:0006508). (linked conceptually to cited mechanisms)
- Cellular Component (GO/Context): sarcomere/myofibril; extracellular region/surface film of cartilage; synovial lining; extracellular microfibril.
- Phenotypes (HP): Camptodactyly (HP:0012385); Distal arthrogryposis (HP:0002829); Non-inflammatory arthropathy (HP:0001370); Arachnodactyly (HP:0001166); Coxa vara (HP:0002812); Pericardial effusion (HP:0001699). (bagrul2023anovelmutation pages 2-4, illes2024heterogenicgeneticbackground pages 2-3, li2023casereportidentification pages 1-2, shashaani2025juvenileidiopathicarthritis pages 2-4)
- Cell Types (CL): skeletal muscle fiber (CL:0002620); synovial fibroblast (CL:0002558); superficial-zone articular chondrocyte (CL:0000763); motor neuron (CL:0000100). (mapped to mechanisms above)
- Anatomical Locations (UBERON): proximal interphalangeal joint of finger (UBERON:0001466); synovial membrane (UBERON:0001980); articular cartilage (UBERON:0002418); tendon (UBERON:0000473); fetal skeletal muscle of limb (UBERON:0002385). (contextual)
- Chemical Entities (CHEBI): hyaluronic acid (CHEBI:18064). (contextual)

Evidence Items (with PMIDs/DOIs)
- Distal arthrogryposis mechanism and gene spectrum; fetal akinesia paradigm: Illés A et al., Children (2024), DOI: 10.3390/children11070861, URL: https://doi.org/10.3390/children11070861. (illes2024heterogenicgeneticbackground pages 2-3)
- ACTC1 variants causing DA with congenital heart defects; sarcomere dysfunction link: Chong JX et al., Hum Genet Genom Adv (2023), DOI: 10.1016/j.xhgg.2023.100213, URL: https://doi.org/10.1016/j.xhgg.2023.100213. (chong2023variantsinactc1 pages 1-5)
- PRG4/CACP clinical–molecular mechanism; early camptodactyly and non-inflammatory arthropathy: Bağrul İ et al., Pediatr Rheumatol (2023), DOI: 10.1186/s12969-023-00793-z, URL: https://doi.org/10.1186/s12969-023-00793-z. (bagrul2023anovelmutation pages 2-4)
- Additional CACP molecular confirmation and clinical sequence; PRG4 frameshift: Shashaani N et al., BMC Musculoskelet Disord (2025), DOI: 10.1186/s12891-025-09069-x, URL: https://doi.org/10.1186/s12891-025-09069-x. (shashaani2025juvenileidiopathicarthritis pages 2-4, shashaani2025juvenileidiopathicarthritis pages 1-2)
- FBN2 disulfide-bond–disrupting variants; ECM microfibril pathogenesis of camptodactyly: Li A-L et al., Front Genet (2023), DOI: 10.3389/fgene.2023.1035887, URL: https://doi.org/10.3389/fgene.2023.1035887. (li2023casereportidentification pages 1-2)
- ECEL1-associated DA5D; neuromuscular developmental mechanism with cartilage degradation: Jing S et al., Front Neurol (2024), DOI: 10.3389/fneur.2024.1343025, URL: https://doi.org/10.3389/fneur.2024.1343025. (jing2024anovelcompound pages 3-6)

Direct supportive quotes
- “The fundamental pathomechanism across arthrogryposis types is reduced fetal movement … leading to connective tissue accumulation and joint contracture.” (Illés A et al., 2024) (illes2024heterogenicgeneticbackground pages 1-2)
- “CACP syndrome … caused by biallelic pathogenic mutations in the PRG4 gene … characterized by early-onset camptodactyly, noninflammatory arthropathy …” (Bağrul İ et al., 2023) (bagrul2023anovelmutation pages 2-4)

Limitations and open questions
- Histopathologic series specifically characterizing volar plate, lumbrical/FD(S) tendon insertions, and local fibroblast phenotypes in isolated camptodactyly remain limited within the recent 2023–2024 literature retrieved here. The dominant mechanistic paradigm (fetal akinesia and connective tissue remodeling) is well supported, but finer molecular details of tendon/volar plate fibrosis in isolated cases warrant further study. (illes2024heterogenicgeneticbackground pages 2-3)

Conclusion
Camptodactyly is a convergent phenotype resulting from: (1) impaired fetal movement arising from sarcomeric (e.g., ACTC1, TNNT3, TNNI2, TPM2, MYH3) or neuromuscular developmental (ECEL1) defects, and/or (2) synovial/joint-surface failure of lubrication from PRG4 loss in CACP, and (3) ECM microfibril defects (FBN2) in congenital contractural arachnodactyly. These mechanisms perturb sarcomere function, ECM organization, synovial biology, and neuromuscular signaling, causing joint positioning and fibroconnective remodeling that culminate in fixed finger flexion contractures. 2023–2024 advances (ACTC1, ECEL1 case-based genomics; continued PRG4/CACP delineation) sharpen the mechanistic map and provide ontology-ready annotations for knowledge-base integration. (chong2023variantsinactc1 pages 1-5, bagrul2023anovelmutation pages 2-4, illes2024heterogenicgeneticbackground pages 2-3, li2023casereportidentification pages 1-2, jing2024anovelcompound pages 3-6, shashaani2025juvenileidiopathicarthritis pages 2-4)

References

1. (chong2023variantsinactc1 pages 1-5): Jessica X. Chong, Matthew Carter Childers, Colby T. Marvin, Anthony J. Marcello, Hernan Gonorazky, Lili-Naz Hazrati, James J. Dowling, Fatema Al Amrani, Yasemin Alanay, Yolanda Nieto, Miguel Á Marín Gabriel, Arthur S. Aylsworth, Kati J. Buckingham, Kathryn M. Shively, Olivia Sommers, Kailyn Anderson, Michael Regnier, and Michael J. Bamshad. Variants in actc1 underlie distal arthrogryposis accompanied by congenital heart defects. Human Genetics and Genomics Advances, 4:100213, Jul 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100213, doi:10.1016/j.xhgg.2023.100213. This article has 12 citations.

2. (bagrul2023anovelmutation pages 2-4): İlknur Bağrul, Serdar Ceylaner, Yasemin Tasci Yildiz, Serife Tuncez, Elif Arslanoglu Aydin, Esra Bağlan, Semanur Ozdel, and Mehmet Bülbül. A novel mutation in the proteoglycan 4 gene causing cacp syndrome: two sisters report. Pediatric Rheumatology Online Journal, Jan 2023. URL: https://doi.org/10.1186/s12969-023-00793-z, doi:10.1186/s12969-023-00793-z. This article has 8 citations.

3. (illes2024heterogenicgeneticbackground pages 2-3): Anett Illés, Henriett Pikó, Virág Bartek, Olívia Szepesi, Gábor Rudas, Zsófia Benkő, Ágnes Harmath, János Pál Kósa, and Artúr Beke. Heterogenic genetic background of distal arthrogryposis—review of the literature and case report. Children, 11:861, Jul 2024. URL: https://doi.org/10.3390/children11070861, doi:10.3390/children11070861. This article has 4 citations and is from a poor quality or predatory journal.

4. (li2023casereportidentification pages 1-2): An-Lei Li, Ji-Qiang He, Lei Zeng, Yi-Qiao Hu, Min Wang, Jie-Yi Long, Si-Hua Chang, Jie-Yuan Jin, and Rong Xiang. Case report: identification of novel fibrillin-2 variants impacting disulfide bond and causing congenital contractural arachnodactyly. Frontiers in Genetics, Mar 2023. URL: https://doi.org/10.3389/fgene.2023.1035887, doi:10.3389/fgene.2023.1035887. This article has 4 citations and is from a peer-reviewed journal.

5. (jing2024anovelcompound pages 3-6): Siyuan Jing, Mou Peng, Yuping He, Yimin Hua, Jinrong Li, and Yifei Li. A novel compound heterozygous variant of ecel1 induced joint dysfunction and cartilage degradation: a case report and literature review. Frontiers in Neurology, Jan 2024. URL: https://doi.org/10.3389/fneur.2024.1343025, doi:10.3389/fneur.2024.1343025. This article has 3 citations and is from a peer-reviewed journal.

6. (shashaani2025juvenileidiopathicarthritis pages 2-4): Niloofar Shashaani, Vadood Javadi, Khosro Rahmani, and Reza Shiari. Juvenile idiopathic arthritis or skeletal dysplasia: first case report of camptodactyly-arthropathy-coxa vara-pericarditis from iran. BMC Musculoskeletal Disorders, Aug 2025. URL: https://doi.org/10.1186/s12891-025-09069-x, doi:10.1186/s12891-025-09069-x. This article has 0 citations and is from a peer-reviewed journal.

7. (illes2024heterogenicgeneticbackground pages 1-2): Anett Illés, Henriett Pikó, Virág Bartek, Olívia Szepesi, Gábor Rudas, Zsófia Benkő, Ágnes Harmath, János Pál Kósa, and Artúr Beke. Heterogenic genetic background of distal arthrogryposis—review of the literature and case report. Children, 11:861, Jul 2024. URL: https://doi.org/10.3390/children11070861, doi:10.3390/children11070861. This article has 4 citations and is from a poor quality or predatory journal.

8. (shashaani2025juvenileidiopathicarthritis pages 1-2): Niloofar Shashaani, Vadood Javadi, Khosro Rahmani, and Reza Shiari. Juvenile idiopathic arthritis or skeletal dysplasia: first case report of camptodactyly-arthropathy-coxa vara-pericarditis from iran. BMC Musculoskeletal Disorders, Aug 2025. URL: https://doi.org/10.1186/s12891-025-09069-x, doi:10.1186/s12891-025-09069-x. This article has 0 citations and is from a peer-reviewed journal.