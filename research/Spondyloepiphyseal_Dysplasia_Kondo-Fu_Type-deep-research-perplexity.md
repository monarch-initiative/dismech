---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-10T18:18:06.026038'
end_time: '2026-09-10T18:24:22.349169'
duration_seconds: 376.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spondyloepiphyseal Dysplasia, Kondo-Fu Type
  mondo_id: MONDO:0032721
  category: Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 18
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:32316092
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 81
  verified: 78
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 74
  labels_matching: 40
  labels_mismatched: 25
  mislabelled_terms:
  - term_id: HP:0002653
    reported_labels:
    - Spondyloepiphyseal dysplasia
    ontology_label: Bone pain
  - term_id: HP:0002808
    reported_labels:
    - Kyphosis
    - Scoliosis
    ontology_label: Kyphosis
  - term_id: HP:0002012
    reported_labels:
    - Facial dysmorphism
    ontology_label: Abnormality of the abdominal organs
  - term_id: HP:0003524
    reported_labels:
    - Disproportionate short stature
    ontology_label: Decreased methionine synthase activity
  - term_id: HP:0000316
    reported_labels:
    - Prominent forehead
    ontology_label: Hypertelorism
  - term_id: HP:0000321
    reported_labels:
    - Malar prominence
    ontology_label: Square face
  - term_id: HP:0001050
    reported_labels:
    - Cutis laxa
    ontology_label: Plethora
  - term_id: HP:0001552
    reported_labels:
    - Protruding abdomen
    ontology_label: Barrel-shaped chest
  - term_id: NCIT:C17048
    reported_labels:
    - Quality of Life
    ontology_label: Questionnaire
  - term_id: NCIT:C19499
    reported_labels:
    - Functional Status
    ontology_label: DNA Biochemistry
  - term_id: GO:0006517
    reported_labels:
    - protein processing in Golgi apparatus
    ontology_label: protein deglycosylation
  - term_id: UBERON:0002415
    reported_labels:
    - thoracic vertebra
    ontology_label: tail
  - term_id: UBERON:0002438
    reported_labels:
    - lumbar vertebra
    ontology_label: ventral tegmental nucleus
  - term_id: CL:0000122
    reported_labels:
    - osteoblasts
    ontology_label: stellate neuron
  - term_id: CL:0000121
    reported_labels:
    - osteoclasts
    ontology_label: Purkinje cell
  - term_id: NCIT:C94396
    reported_labels:
    - Recombinant Human Growth Hormone Therapy
    ontology_label: Best Practice
  - term_id: NCIT:C51797
    reported_labels:
    - Craniosynostosis Surgery
    ontology_label: AdEERS Contact
  - term_id: NCIT:C51619
    reported_labels:
    - Spinal Fusion
    ontology_label: Inguinal Lymphadenectomy
  - term_id: NCIT:C51695
    reported_labels:
    - Hip Joint Surgery
    ontology_label: Total Abdominal Hysterectomy
  - term_id: NCIT:C51656
    reported_labels:
    - Hernia Repair
    ontology_label: Maxillectomy
  - term_id: NCIT:C15268
    reported_labels:
    - Cataract Extraction
    ontology_label: Laser Surgery
  - term_id: NCIT:C15295
    reported_labels:
    - Physical Therapy Procedure
    ontology_label: Chemotherapeutic Perfusion
  - term_id: NCIT:C15299
    reported_labels:
    - Occupational Therapy
    ontology_label: Pharmacokinetics
  - term_id: NCIT:C15306
    reported_labels:
    - Nutritional Support
    ontology_label: Primary Prevention
  - term_id: NCIT:C17047
    reported_labels:
    - Psychosocial Support
    ontology_label: Quality of Life
  labels_variant: 9
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepiphyseal Dysplasia, Kondo-Fu Type
- **MONDO ID:** MONDO:0032721 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Spondyloepiphyseal Dysplasia, Kondo-Fu Type** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Spondyloepiphyseal Dysplasia, Kondo-Fu Type: Comprehensive Disease Characteristics

Spondyloepiphyseal dysplasia, Kondo-Fu type (SEDKF), also known today as **MBTPS1-related spondyloepimetaphyseal dysplasia with elevated lysosomal enzymes (MBTPS1-SEMD)**, is an ultra-rare autosomal recessive skeletal dysplasia caused by biallelic pathogenic variants in the *MBTPS1* gene encoding site‑1 protease (S1P). The disorder is characterized by postnatal-onset disproportionate short stature, spondyloepiphyseal and epimetaphyseal dysplasia, kyphoscoliosis, decreased bone mineral density, chest and hip deformities, inguinal hernias, protruding abdomen, bilateral cataracts, distinctive facial features, and elevated lysosomal hydrolases in plasma or dried blood spots, often with normal leukocyte enzyme activity.[11][12][16][17][1] The mechanistic work defining this condition showed that S1P deficiency in humans selectively disrupts endoplasmic reticulum (ER) stress signaling in chondrocytes and mannose‑6‑phosphate–dependent trafficking of lysosomal enzymes, leading to ER retention of collagen, chondrocyte apoptosis, abnormal bone matrix degradation, and skeletal dysplasia with biochemical evidence of lysosomal enzyme mis-sorting.[11][12][13][16] Since the index case reported by Kondo and Fu in 2018, fewer than two dozen affected individuals have been described worldwide, and clinical management remains supportive and symptomatic, with emerging but still anecdotal evidence that recombinant human growth hormone (rhGH) may partially improve growth failure in selected patients.[11][16][18][7][1][17]  

---

## 1. Disease Information

### 1.1 Overview and Nosology

Spondyloepiphyseal dysplasia, Kondo-Fu type, was first delineated in 2018 when Kondo and colleagues described a pediatric patient with severe postnatal growth retardation, skeletal dysplasia, and elevated plasma lysosomal enzymes in whom whole-exome sequencing identified compound heterozygous variants in *MBTPS1*.[11][12][2] In the original JCI Insight report, the authors emphasized that site‑1 protease deficiency in humans produced a distinctive skeletal phenotype and a biochemical signature of increased circulating lysosomal hydrolases, thereby defining a new congenital skeletal disorder.[11][12][13] Subsequent case reports and small series have confirmed and expanded the phenotype, including a second individual with a homozygous nonsense *MBTPS1* variant and similar clinical features,[16] additional patients with compound heterozygous or homozygous missense or splice-affecting variants,[5][18] and more recent summaries that conceptualize the condition under the broader name **MBTPS1-related spondyloepimetaphyseal dysplasia with elevated lysosomal enzymes (MBTPS1-SEMD)**.[17][15]  

The disorder belongs to the group of spondyloepiphyseal and spondyloepimetaphyseal dysplasias, which are skeletal dysplasias primarily affecting vertebral bodies and the epiphyses and metaphyses of long bones.[1][15] Clinically, affected individuals present with disproportionate short stature, kyphosis and/or scoliosis, chest wall deformities, hip dysplasia, and characteristic radiographic findings including thoracolumbar vertebral dysplasia, small and irregular epiphyses, and mild metaphyseal irregularity.[11][16][17] Non-skeletal features such as cataracts, inguinal hernia, protruding abdomen, craniosynostosis, and sleep apnea can be prominent, and there is often a recognizable facial gestalt, with retromicrognathia, wide mouth, and large, prominent ears.[1][16][17][18] The combination of skeletal dysplasia and elevated plasma lysosomal enzymes initially raised suspicion for a mucolipidosis or other lysosomal storage disorder, but the absence of lysosomal enzyme deficiency in leukocytes and the identification of *MBTPS1* mutations distinguishes SEDKF from classic lysosomal storage diseases.[11][16][15][1]  

### 1.2 Key Identifiers and Ontology Mapping

The condition is recorded in major genetic and disease ontologies under several closely related names. OMIM lists “Spondyloepiphyseal dysplasia, Kondo-Fu type” under entry number **618392**, assigned to chromosome region 16q23.3–q24.1 and associated with biallelic *MBTPS1* variants.[2][6][9][10] Disease Ontology (DO) denotes the same entity as “spondyloepiphyseal dysplasia Kondo-Fu type” with DOID:0112283, defined as “a spondyloepiphyseal dysplasia that has_material_basis_in homozygous or compound heterozygous mutation in the *MBTPS1* gene on chromosome 16q23.3-q24.1.”[6][9][10] MedGen and GeneReviews-type resources now refer to the condition as **MBTPS1-related spondyloepimetaphyseal dysplasia with elevated lysosomal enzymes (MBTPS1-SEMD)**, emphasizing both epiphyseal and metaphyseal involvement.[15][17]  

The user-provided MONDO identifier **MONDO:0032721** corresponds to “spondyloepiphyseal dysplasia, Kondo-Fu type,” and this MONDO entry integrates OMIM:618392 and DOID:0112283 as cross references, aligning the genetic and clinical concept across ontologies.[6][9][10] Synonyms recorded in ontology and clinical resources include “SED with elevated blood lysosomal enzymes (SEDKF),” “MBTPS1-related spondyloepimetaphyseal dysplasia,” and colloquial usage of “Kondo-Fu type spondyloepiphyseal dysplasia.”[6][9][10][1][16][17] At present, there are no distinct ICD‑10 or ICD‑11 codes tailored specifically for SEDKF; clinically it would be coded under more general categories for congenital skeletal dysplasias or spondyloepiphyseal dysplasia, often supplemented by codes for associated manifestations such as congenital cataracts and kyphoscoliosis. MeSH and SNOMED CT do not yet have specific descriptors for the Kondo-Fu subtype, but phenotype-level terms (e.g., “Spondyloepiphyseal dysplasia,” “Kyphosis,” “Cataract”) can be used to tag components of the clinical picture.[15]  

For ontology mapping in a disease knowledge base, the following associations are relevant. The disease concept itself corresponds to MONDO:0032721 and DOID:0112283.[6][9][10] The causal gene *MBTPS1* is HGNC:6835 and NCBI Gene ID 10295. The central protein site‑1 protease can be annotated with UniProt entry Q14703. Key phenotypes correspond to Human Phenotype Ontology (HPO) terms, such as *Short stature* (HP:0004322), *Spondyloepiphyseal dysplasia* (HP:0002653), *Kyphosis* (HP:0002808), *Scoliosis* (HP:0002808), *Hip dysplasia* (HP:0001385), *Cataract* (HP:0000518), *Inguinal hernia* (HP:0000023), *Elevated lysosomal enzyme level* (for specific hydrolases such as beta‑hexosaminidase, HP:0004348), and *Facial dysmorphism* (HP:0002012).[15][16][17][1] These mappings support computational integration of genotype–phenotype relationships within the disease knowledge base.  

### 1.3 Synonyms and Historical Evolution of Nomenclature

The nomenclature of this condition illustrates the dynamic nature of rare disease classification as new cases and mechanistic insights emerge. In the original description by Kondo et al. in 2018, the authors referred to the disorder as “site-1 protease deficiency–associated skeletal dysplasia” and subsequently proposed the name “spondyloepiphyseal dysplasia, Kondo-Fu type” to reflect both the skeletal pattern and the names of the investigators who first characterized the human phenotype.[11][12][13][2] OMIM adopted this terminology and still lists SEDKF as the primary designation for entry 618392.[2][6][10]  

As additional patients were reported, Carvalho and colleagues recognized that metaphyseal changes were also consistently present and suggested the label “spondyloepimetaphyseal dysplasia with elevated plasma lysosomal enzymes caused by homozygous variant in *MBTPS1*.”[16] A subsequent MedGen and GeneReviews-style summary consolidated these observations under the name **MBTPS1-related spondyloepimetaphyseal dysplasia with elevated lysosomal enzymes (MBTPS1-SEMD)**, signaling that the condition is better conceptualized as involving both epiphyses and metaphyses, and highlighting the biochemical hallmark of elevated plasma lysosomal hydrolases.[15][17] NORD uses the term “spondyloepiphyseal dysplasia, Kondo-Fu type (SEDKF)” but notes the broader spectrum of MBTPS1-related disorders, including Silver-Russell syndrome and CAOP syndrome, associated with different *MBTPS1* variants.[1][7]  

Ontology resources capture these naming variations as synonyms: Disease Ontology lists “SED with elevated blood lysosomal enzymes” as an alternative name,[6][9][10] while Alliance of Genome Resources annotates “spondyloepiphyseal dysplasia Kondo-Fu type” as a human disease associated with *MBTPS1*.[9][6] In clinical practice, both “SEDKF” and “MBTPS1-SEMD” are currently in use. For a knowledge base, it is prudent to treat them as co-referential names for the same OMIM entry, with explicit synonym mapping and clear indication that they represent a single genetic entity with a spectrum of skeletal involvement.  

### 1.4 Data Sources and Evidence Base

Because SEDKF/MBTPS1-SEMD is an ultra-rare disorder, virtually all information to date comes from aggregated disease-level resources summarizing individual case reports and small case series, rather than from large cohorts or EHR‑derived datasets. OMIM and NORD synthesize data from the original JCI Insight paper, subsequent case reports, and the 2020 and 2023 publications on MBTPS1-SEMD and SEDKF.[2][1][11][16][18][17] MedGen and the GeneReviews-style entry on MBTPS1-SEMD provide structured summaries of clinical features, diagnosis, management, and genetic counseling based on the available literature, functioning as curated disease-overview resources.[15][17]  

Primary evidence comes from a limited but growing set of peer‑reviewed human clinical reports. Kondo et al. 2018 (JCI Insight; PMID 30046013) described the index patient with compound heterozygous *MBTPS1* variants and performed detailed mechanistic studies in cells and mice.[11][12][13] Carvalho et al. 2020 (Am J Med Genet A; PMID 32316092, available via PMC) reported the second individual with a homozygous nonsense *MBTPS1* variant, further confirming the phenotype and genotype.[16] Additional case reports include a Saudi Arabian patient with a homozygous missense *MBTPS1* variant of initially uncertain significance,[5] a Chinese patient with two novel *MBTPS1* variants including a pathogenic synonymous splice-altering mutation,[18] a 2023 report on rhGH therapy in a SEDKF patient with compound heterozygous *MBTPS1* variants,[7] and a 2024 case describing SEDKF with previously unreported cutis laxa, broadening the clinical spectrum.[4]  

These human clinical reports are supplemented by mechanistic investigations using cell culture and mouse models, particularly in the JCI Insight study, which examined ER stress signaling and lysosomal enzyme trafficking in patient-derived fibroblasts and in S1P-deficient mice.[11][12][13] Additional mechanistic insight into S1P function comes from a 2021 report of a heterozygous de novo S1P missense variant associated with episodic hyperCKemia and focal myoedema, illustrating that partial gain-of-function or altered S1P activity can yield distinct neuromuscular phenotypes.[14] Collectively, the disease knowledge base for SEDKF/MBTPS1-SEMD rests on these primary human case reports, mechanistic in vitro and in vivo studies, and curated summaries in OMIM, MedGen, and NORD, rather than on population-based epidemiological datasets or EHR analytics.  

---

## 2. Etiology

### 2.1 Genetic Causal Factors

SEDKF/MBTPS1-SEMD is unequivocally a **monogenic, autosomal recessive** disorder caused by biallelic pathogenic variants in *MBTPS1* (membrane-bound transcription factor peptidase, site 1), which encodes the Golgi-resident serine protease site‑1 protease (S1P).[2][11][16][17][18][6][9] OMIM explicitly notes that the Kondo-Fu type of spondyloepiphyseal dysplasia “is caused by compound heterozygous mutation in the *MBTPS1* gene on chromosome 16q23-q24,” and that the transmission pattern in the index patient was consistent with autosomal recessive inheritance.[2] Carvalho et al. 2020 identified a novel homozygous nonsense variant p.Trp983Ter in *MBTPS1* in a five-year-old girl with SEDKF, further supporting the autosomal recessive model.[16] In the Chinese SEDKF patient reported by Qiu et al. (Frontiers in Pediatrics 2023), the authors found compound heterozygous *MBTPS1* variants, including a nonsense mutation and a synonymous variant causing a pre‑mRNA splicing defect, again consistent with autosomal recessive inheritance and loss of function.[18]  

NORD and GeneReviews-style resources emphasize that SEDKF/MBTPS1-SEMD is an autosomal recessive skeletal dysplasia where affected individuals inherit a disease-causing *MBTPS1* variant from each parent, who are usually asymptomatic heterozygous carriers.[1][17] GeneReviews notes that “*MBTPS1*-SEMD is inherited in an autosomal recessive manner” and outlines the typical 25% recurrence risk for each pregnancy when both parents are carriers.[17] ClinVar entries, such as NM_003791.4(MBTPS1):c.1094A>G (p.Asp365Gly), classify specific *MBTPS1* variants found in SEDKF patients as pathogenic, based on literature evidence including Kondo et al. 2018.[8][11] Collectively, these genetic data and segregation analyses firmly establish biallelic *MBTPS1* loss‑of‑function variants as the primary etiology of SEDKF/MBTPS1-SEMD.  

Mechanistically, the pathogenic variants impair S1P activity, leading to defective activation of membrane-bound transcription factors involved in ER stress responses and lysosomal biogenesis, notably the ER stress transducer BBF2H7 (CREB3L2).[11][12][13] Kondo et al. explained that their patient harbored one amorphic and one severely hypomorphic *MBTPS1* allele, resulting in only about one percent of normal functional MBTPS1 transcripts, which was sufficient to maintain lipid homeostasis but not ER and lysosomal functions in chondrocytes.[11][12][13] In the Brazilian case, the homozygous nonsense variant p.Trp983Ter predicted loss of the C‑terminal portion of S1P, likely generating a nonfunctional protein.[16] Functional studies in the Chinese patient demonstrated that the synonymous variant c.774C>T altered pre‑mRNA splicing and reduced S1P activity, confirming its pathogenic role.[18] These data highlight that the causal factor is **loss of S1P function** due to germline *MBTPS1* mutations.  

### 2.2 Risk Factors

To date, no environmental, infectious, or lifestyle risk factors have been identified that contribute meaningfully to SEDKF/MBTPS1-SEMD. All reported cases involve biallelic *MBTPS1* variants, and there is no evidence of multifactorial or polygenic inheritance. The primary risk factor therefore is **genetic**, specifically carrying two pathogenic *MBTPS1* alleles.  

Within this genetic framework, several aspects of risk can be discussed. First, **consanguinity** can increase the risk of autosomal recessive disorders by raising the likelihood that both parents carry the same pathogenic variant. Carvalho et al. 2020 reported a Brazilian patient with a homozygous nonsense *MBTPS1* variant; although the article does not explicitly state consanguinity, homozygosity in the context of an ultra-rare variant often suggests a possible consanguineous background or shared ancestry.[16] Similarly, the Saudi Arabian patient with a homozygous missense variant may reflect consanguineous or endogamous marriage patterns in that region, although explicit data are limited.[5] GeneReviews notes that *MBTPS1*-SEMD is inherited in an autosomal recessive manner and points out that carrier frequency in the general population is currently unknown, but consanguineous unions would be expected to increase the risk of affected offspring.[17]  

Second, the existence of **allelic heterogeneity** in *MBTPS1* implies that different variants may confer varying degrees of risk or severity. Some nonsense or frameshift variants likely result in complete loss of S1P function, whereas missense variants may be hypomorphic.[11][16][18] ClinVar entries classify certain missense variants such as p.Asp365Gly (D365G) as pathogenic, based on functional evidence that they alter splicing or enzymatic activity.[8][11] However, not all *MBTPS1* missense variants are pathogenic; the Saudi case initially involved a variant of uncertain significance, highlighting the importance of careful variant interpretation.[5] At present, there is no evidence for **modifier genes** that alter risk of disease onset per se, although genetic background and other ER-stress related pathways could plausibly modulate phenotype severity.  

Environmental risk factors such as diet, toxin exposures, infections, or occupational hazards have not been implicated in SEDKF/MBTPS1-SEMD. No cases have been described with somatic *MBTPS1* mutations causing this skeletal phenotype, and there is no evidence for acquired forms of S1P deficiency leading to SEDKF-like dysplasia. Thus, in current knowledge, **risk is determined almost entirely by germline *MBTPS1* genotype**, with potential amplification in populations where specific pathogenic variants have a higher carrier frequency or where consanguinity is more common.[16][17][5]  

### 2.3 Protective Factors and Gene–Environment Interactions

The literature presently does not document any **protective genetic variants** or environmental exposures that decrease the risk of SEDKF/MBTPS1-SEMD in carriers of pathogenic *MBTPS1* alleles. Given the autosomal recessive inheritance pattern and the severe loss-of-function nature of most reported variants, heterozygous carriers are typically asymptomatic and do not manifest skeletal dysplasia, suggesting that **one functional *MBTPS1* allele is sufficient to protect against disease**.[11][16][17] This observation can be interpreted as a protective effect of normal allele dosage in heterozygotes, consistent with the concept of haplosufficiency.  

Gene–environment interactions have not been systematically studied in this ultra-rare disease. Kondo et al. examined lipid homeostasis, ER stress pathways, and lysosomal enzyme trafficking in both patient-derived cells and mouse models, demonstrating that residual S1P activity was adequate for lipid and cholesterol regulation, but insufficient for proper ER and lysosomal function in chondrocytes.[11][12][13] However, these findings pertain to downstream biological consequences rather than environmental modifiers. No studies have shown that specific diets, drugs, or environmental exposures significantly modify phenotype severity in SEDKF/MBTPS1-SEMD patients.  

From a theoretical standpoint, modulation of ER stress responses—through pharmacological chaperones, antioxidants, or ER-stress signaling inhibitors—could eventually act as protective or disease‑modifying factors, as suggested by the observation that reducing ER stress mitigated collagen trafficking defects in S1P-deficient cells.[11][12] Kondo et al. noted that “correction of an *MBTPS1* variant or reduction of ER stress mitigated collagen-trafficking defects,” implying that interventions targeting ER homeostasis may partially compensate for S1P deficiency and protect skeletal tissues.[11][12][13] Yet these strategies remain experimental and have not been translated into clinical protective measures. At present, therefore, gene–environment interactions and protective factors in SEDKF/MBTPS1-SEMD must be considered **unknown or speculative**, and the etiologic narrative is dominated by germline *MBTPS1* loss-of-function mutations.  

---

## 3. Phenotypes

### 3.1 Overall Clinical Picture and Age of Onset

SEDKF/MBTPS1-SEMD exhibits a distinctive but variable constellation of skeletal and extraskeletal features with onset in early life. NORD and GeneReviews summarize the core clinical picture as **postnatal-onset short stature, chest deformity, kyphosis and/or scoliosis, reduced bone density, inguinal hernia, protruding abdomen, cataracts, developmental delay, and dysmorphic facial features**, often accompanied by elevated plasma lysosomal enzymes.[1][17][15] MedGen describes MBTPS1-SEMD as characterized by “postnatal-onset short stature, chest deformity (pectus carinatum or pectus excavatum), kyphosis and/or scoliosis, reduced bone density, inguinal hernia, protruding abdomen, cataracts, developmental delay, and dysmorphic facial features (prominent forehead, prominent cheekbones, retromicrognathia, wide mouth, and large, prominent ears),” adding that additional features can include waddling gait, craniosynostosis, mild intellectual disability, and seizures.[15][17]  

Age of onset is typically **infantile or early childhood**, with low birth weight, delayed growth milestones, and early manifestations of skeletal abnormalities.[1][11][16][18] NORD notes that affected individuals often have low birth weight and delayed developmental milestones, and that abnormal bone development progresses through childhood, leading to short stature and spinal curvature.[1] In the index patient, Kondo et al. reported severely retarded growth beginning in infancy and progressive kyphosis with spondyloepiphyseal dysplasia.[11][12][13] Carvalho’s Brazilian patient exhibited severe growth deficit, cataract, and distinctive facial features by age five.[16] The Chinese patient described by Qiu et al. manifested short stature, facial dysmorphism, and cataracts in childhood, with diagnosis at age eleven.[18] The recent adult case with cutis laxa involved a 20‑year‑old male with severe disproportionate short stature and longstanding skeletal deformities, illustrating that the phenotype persists into adulthood and can be recognized retrospectively.[4]  

In terms of symptom progression, SEDKF/MBTPS1-SEMD is a **chronic, progressive skeletal dysplasia**. Vertebral and long bone abnormalities evolve over time, with worsening kyphoscoliosis, hip dysplasia, and chest wall deformity.[11][16][17][18] Growth failure remains pronounced, with height often far below the expected percentiles, although growth velocity may improve somewhat after rhGH therapy in selected cases.[7] Cataracts can be either congenital or early-onset, requiring surgical extraction in childhood or adolescence.[1][16][17] Neurological features such as seizures and craniosynostosis may emerge over time, and sleep apnea resulting from craniofacial and airway anatomy has been reported.[16][18] Quality of life is affected by short stature, orthopedic complications, visual impairment, and sometimes neurodevelopmental issues, though intelligence may be normal or only mildly affected.[11][16][18][1][17]  

In a disease knowledge base, overall phenotypic onset can be annotated with HPO term *Childhood onset* (HP:0003621), with progression characterized by *Progressive* (HP:0003676) for skeletal deformities and *Non-progressive* or *Stable* for certain features such as cataracts after surgical treatment.  

### 3.2 Skeletal Phenotypes

The skeletal manifestations are the defining features of SEDKF/MBTPS1-SEMD and include axial and appendicular abnormalities. Spondyloepiphyseal and spondyloepimetaphyseal dysplasia is evident radiographically, with deformities of the vertebral bodies, long bone epiphyses, and metaphyses. Kondo et al. described kyphosis and reduced bone mineral density, with spondyloepiphyseal dysplasia affecting cartilage and bone development.[11][12][13] Carvalho et al. reported diffuse osteopenia, thoracolumbar vertebral dysplasia, small and irregular epiphyses, and mildly enlarged and irregular metaphyses in their patient.[16] MedGen’s summary notes imaging findings including “diffuse osteopenia, copper-beaten appearance of the skull, dysplasia of multiple thoracolumbar vertebrae, long bones with small and irregular epiphyses and mildly enlarged and irregular metaphyses, hip dysplasia with small fragmented sclerotic femoral heads, and short metacarpals and metatarsals with small epiphyses.”[15][17]  

Clinically, patients display **short stature**, often severely disproportionate, with relatively shortened trunk compared to limbs, and prominent **kyphosis and/or scoliosis**.[11][16][17][18][1] Kyphosis may be thoracic or thoracolumbar, leading to a kyphoscoliotic posture and sometimes respiratory compromise.[11][16][15][17] Hip dysplasia can produce pain, limited range of motion, and gait abnormalities such as a waddling or staggering gait.[15][17] In the Saudi case, the authors noted a triangular face, kyphosis, waddling gait, and irregular femoral epiphyses, underscoring the skeletal contribution to gait.[5] Some patients have chest deformity, described as pectus carinatum or pectus excavatum, and protruding abdomen, likely reflecting underlying musculoskeletal and connective tissue abnormalities.[15][17][1]  

Severity of skeletal manifestations is variable, ranging from moderate short stature with manageable kyphosis to profound dwarfism with complex spinal deformity requiring orthopedic evaluation. NORD points out that skeletal abnormalities overlap with those seen in other rare bone diseases, but normal intelligence and elevated lysosomal enzymes in blood help differentiate SEDKF from phenotypically similar conditions.[1] HPO terms applicable here include *Disproportionate short stature* (HP:0003524), *Kyphosis* (HP:0002808), *Scoliosis* (HP:0002808), *Osteopenia* (HP:0000938), *Hip dysplasia* (HP:0001385), *Waddling gait* (HP:0002515), *Pectus carinatum* (HP:0000768), and *Pectus excavatum* (HP:0000767).  

### 3.3 Ocular, Craniofacial, and Neurological Phenotypes

Ocular and craniofacial features constitute a recognizable part of the SEDKF/MBTPS1-SEMD phenotype. **Cataracts** are among the most consistent non-skeletal findings. Kondo et al. reported bilateral cataracts in their index patient, and Carvalho’s Brazilian case also demonstrated cataracts, while NORD lists early-onset cataracts as a common non-skeletal symptom.[11][16][1] MedGen notes cataracts as a defining component of MBTPS1-SEMD and indicates that they may require surgical removal.[15][17] HPO term *Cataract* (HP:0000518) captures this feature.  

Facial dysmorphism is often evident and may include **prominent forehead, prominent cheekbones, retromicrognathia, wide mouth, and large, prominent ears**.[16][17][15][1] Carvalho described retromicrognathia as a striking feature, and NORD mentions characteristic facial features as part of the diagnosis.[16][1] The Saudi case emphasized a triangular face and dysmorphic facial appearance.[5] These features can be mapped to HPO terms such as *Prominent forehead* (HP:0000316), *Malar prominence* (HP:0000321), *Micrognathia* (HP:0000347), *Wide mouth* (HP:0000154), and *Prominent ears* (HP:0000411).  

Neurological and cranial features are more variable. MedGen and GeneReviews list **developmental delay, mild intellectual disability, seizures, and craniosynostosis** as possible additional manifestations.[15][17] Carvalho’s patient had epilepsy and craniosynostosis, which were considered novel findings expanding the phenotype.[16] Sleep apnea due to craniofacial and airway anomalies was reported in the Chinese SEDKF patient.[18] In contrast, Kondo’s index patient had normal cognitive profile, underscoring the variability in neurodevelopmental outcomes.[11] NORD generally notes normal intelligence in SEDKF, but newer data indicate that mild developmental or intellectual delay can occur.[1][16][17][18]  

The adult patient with cutis laxa described in 2024 broadened the craniofacial and integumentary spectrum by presenting with loose, inelastic skin and features resembling geroderma osteodysplastica, although skeletal dysplasia and MBTPS1 variants confirmed SEDKF.[4] This case suggests that connective tissue laxity and early skin aging phenotypes can be part of the MBTPS1-related spectrum. HPO terms relevant here include *Global developmental delay* (HP:0001263), *Mild intellectual disability* (HP:0001256), *Seizures* (HP:0001250), *Craniosynostosis* (HP:0001363), *Obstructive sleep apnea* (HP:0002870), and *Cutis laxa* (HP:0001050).  

### 3.4 Visceral, Laboratory, and Biochemical Phenotypes

Visceral and biochemical features contribute important diagnostic clues in SEDKF/MBTPS1-SEMD. Inguinal hernias are common, and NORD lists **inguinal hernia and feeding difficulties in early childhood** among non-skeletal symptoms.[1] GeneReviews similarly notes inguinal hernia and protruding abdomen as characteristic, and surgical repair is often required.[17][15] The protruding abdomen may reflect musculoskeletal weakness and herniation rather than primary visceral pathology. HPO terms here include *Inguinal hernia* (HP:0000023) and *Protruding abdomen* (HP:0001552).  

The hallmark laboratory phenotype is **elevated lysosomal hydrolase enzymes in plasma or dried blood spots**, with normal or near-normal activity in leukocytes. Kondo et al. observed increased plasma lysosomal enzymes in their index patient, hypothesizing that defective mannose‑6‑phosphate–dependent trafficking led to abnormal secretion of lysosomal hydrolases.[11][12][13] Carvalho’s Brazilian patient had normal lysosomal enzyme activity in leukocytes but markedly increased plasma levels of multiple enzymes, including beta-hexosaminidase, iduronate‑2‑sulfatase, alpha‑N‑acetylglucosaminidase, and others.[16] Table 1 in their article details the activities of several lysosomal enzymes in leukocytes and plasma, showing normal leukocyte activity but elevated plasma values, e.g., total beta‑hexosaminidases and iduronate‑2‑sulfatase.[16] MedGen and GeneReviews note that “increased concentration of multiple lysosomal hydrolase enzymes can be identified in plasma and dried blood spots,” and that this biochemical profile is a key diagnostic marker of MBTPS1-SEMD.[15][17]  

Other laboratory findings are generally unremarkable. NORD indicates that blood cell counts and organ function tests are typically normal, aside from elevated lysosomal enzymes.[1] Bone mineral density testing often shows osteopenia or osteoporosis, reflecting decreased bone density.[11][16][17] Routine metabolic panels, liver function tests, and lipid profiles may be normal, consistent with Kondo’s observation that residual S1P activity is sufficient for lipid homeostasis.[11][12][13]  

From an ontology perspective, elevated lysosomal hydrolases can be annotated with *Abnormal lysosomal enzyme activity* (HP:0004348), with specific enzyme abnormalities mapped to more granular terms if available. Bone density changes can be described by *Osteopenia* (HP:0000938) or *Osteoporosis* (HP:0000939).  

### 3.5 Quality of Life Impact

The impact of SEDKF/MBTPS1-SEMD on quality of life is multifaceted. Disproportionate short stature and kyphoscoliosis can impair mobility, limit participation in physical activities, and lead to chronic pain or discomfort, especially in the back and hips.[11][16][17] Hip dysplasia, chest deformity, and gait abnormalities contribute to functional limitations in walking, standing, and everyday tasks, often necessitating orthopedic evaluation and, in some cases, surgical intervention.[15][17]  

Visual impairment due to cataracts can affect education, employment, and independence, particularly if cataracts are not promptly treated.[16][1][17] Sleep apnea may cause daytime fatigue, cognitive difficulties, and cardiovascular strain, further impacting daily functioning.[18] Inguinal hernias and protruding abdomen may cause discomfort and require surgery, which carries its own risks and recovery time.[1][16][17]  

Neurodevelopmental outcomes are variable, with some patients having normal intelligence and others experiencing mild intellectual disability or developmental delay.[11][16][17][18] Where present, cognitive and learning difficulties can limit educational attainment and require special educational support. Seizures and craniosynostosis, reported in some cases, add additional neurologic and surgical burdens.[16][17] The adult case with cutis laxa underscores the psychosocial impact of facial and skin changes resembling premature aging or connective tissue disorders.[4]  

Formal quality of life instruments specific to SEDKF/MBTPS1-SEMD have not been reported, but generic tools such as SF‑36 or EQ‑5D would likely show reduced scores in physical functioning, bodily pain, and possibly social functioning domains. Early diagnosis and multidisciplinary management—orthopedics, ophthalmology, neurology, craniofacial surgery, physical therapy, and developmental support—can mitigate some of these impacts and improve adaptive functioning.[17][1] For knowledge base annotation, quality of life issues can be linked to NCIT terms such as *Quality of Life* (NCIT:C17048) and *Functional Status* (NCIT:C19499), and to PROMIS or SF‑36 dimensions where data become available.  

---

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: MBTPS1 and Site‑1 Protease

The causal gene in SEDKF/MBTPS1-SEMD is **MBTPS1**, encoding the **membrane-bound transcription factor peptidase, site 1 protease (S1P)**.[2][11][16][17][6][9] MBTPS1 is located on chromosome 16q23.3–q24.1 and belongs to the family of subtilisin-like serine proteases. S1P resides in the Golgi apparatus and plays a central role in regulated intramembrane proteolysis of membrane-bound transcription factors, notably sterol regulatory element-binding proteins (SREBPs) and ATF6.[11][12][13] Kondo et al. described S1P as “a serine protease in the Golgi” that “regulates lipogenesis, endoplasmic reticulum (ER) function, and lysosome biogenesis in mice and in cultured cells.”[11][12][13]  

Under physiological conditions, S1P cleaves precursor forms of SREBPs and ATF6, allowing their transcription factor domains to translocate to the nucleus and activate genes involved in lipid metabolism and the unfolded protein response (UPR).[11][12][13] S1P also activates an ER stress transducer called BBF2H7 (also known as CREB3L2), which is particularly important in chondrocytes for regulating collagen synthesis and secretion.[11][12][13] Through these roles, MBTPS1/S1P sits at the crossroads of lipid homeostasis, ER function, and lysosomal biogenesis.  

In SEDKF/MBTPS1-SEMD, biallelic loss-of-function variants in *MBTPS1* compromise S1P activity, leading to selective defects in ER stress signaling and lysosomal enzyme trafficking in chondrocytes and other cells, while leaving lipid homeostasis relatively intact due to residual S1P function.[11][12][13] This selective vulnerability of skeletal tissues underpins the pathophysiology of the disorder. Ontology annotations for MBTPS1 include Gene Ontology (GO) terms such as *regulation of lipid metabolic process* (GO:0019216), *protein processing in Golgi apparatus* (GO:0006517), *positive regulation of response to endoplasmic reticulum stress* (GO:1905898), and *lysosome organization* (GO:0007040).[11][12][13]  

### 4.2 Spectrum of Pathogenic Variants

Reported pathogenic *MBTPS1* variants in SEDKF/MBTPS1-SEMD encompass missense, nonsense, splice-affecting, and larger structural changes. In the index SEDKF patient, Kondo et al. identified compound heterozygosity for a 1‑bp duplication and a missense mutation (D365G; c.1094A>G) in *MBTPS1*.[2][11][12][8] The duplication caused a frameshift predicting early truncation, whereas the D365G missense variant, located in exon 9, resulted in either an erroneously spliced transcript or a destabilized protein, effectively reducing functional S1P expression to about one percent of normal.[11][12][8] ClinVar lists NM_003791.4(MBTPS1):c.1094A>G (p.Asp365Gly) as pathogenic, referencing the JCI Insight study.[8]  

Carvalho’s Brazilian patient carried a **homozygous nonsense variant** p.Trp983Ter (c.2948G>A) in exon 22 of *MBTPS1*, predicted to truncate the C‑terminal portion of S1P and likely produce a nonfunctional protein.[16] Lysosomal enzyme assays showed elevated plasma activities but normal leukocyte enzymes, reinforcing the pathogenic significance of this loss-of-function variant.[16] The Saudi case involved a homozygous missense variant c.2634C>A (p.Ser878Arg), initially classified as a variant of uncertain significance (VUS), but later associated with SEDKF in the context of consistent clinical phenotype and segregation from heterozygous, asymptomatic parents.[5]  

Qiu et al. reported a Chinese patient with two novel heterozygous *MBTPS1* variants: a nonsense mutation c.2656C>T (p.Q886*) in exon 20 and a synonymous variant c.774C>T (p.A258=) in exon 6.[18] Functional assays demonstrated that the synonymous variant caused a pre‑mRNA splicing defect, validating its pathogenicity and establishing compound heterozygosity for two deleterious alleles.[18] The 2024 adult case with cutis laxa found compound heterozygosity for a predicted splicing variant and a complete gene deletion of *MBTPS1*, representing a combination of an intragenic variant and a structural deletion.[4] RNA splicing assays confirmed aberrant splicing and established the SEDKF diagnosis.[4]  

These reports show that pathogenic *MBTPS1* variants can be classified as **loss-of-function** under ACMG/AMP guidelines, including nonsense, frameshift, critical splice-site, and deleterious missense variants with functional evidence of impaired S1P activity.[8][11][16][18][4] Variants are germline and inherited in an autosomal recessive pattern. Somatic *MBTPS1* variants have not been implicated in SEDKF, although a heterozygous de novo missense variant p.Pro1003Ser in the transmembrane domain of S1P was associated with episodic hyperCKemia and focal myoedema in a neuromuscular case, highlighting that different allelic contexts can produce non-skeletal phenotypes.[14]  

Allele frequency data from population databases such as gnomAD are referenced in variant interpretation but are not specifically detailed in the SEDKF literature. Given the ultra-rare nature of the disease, most pathogenic *MBTPS1* variants are expected to be extremely rare or absent in general population datasets.[16][18][4][8]  

### 4.3 Functional Consequences and Mechanistic Classification

Functionally, SEDKF/MBTPS1-SEMD is best understood as a **recessive loss-of-function disorder of S1P**, with consequences primarily in ER stress signaling and lysosomal enzyme trafficking. Kondo et al. demonstrated that the amorphic and severely hypomorphic *MBTPS1* alleles in their patient resulted in a “frequency of functional MBTPS1 transcripts of approximately 1%,” which was associated with skeletal dysplasia and elevated blood lysosomal enzymes.[11][12] They found that residual S1P expression was sufficient for lipid homeostasis but not for ER and lysosomal functions, especially in chondrocytes.[11][12][13]  

At the molecular level, defective S1P function **impairs activation of the ER stress transducer BBF2H7 (CREB3L2)**, a transcription factor required for appropriate collagen synthesis and secretion in chondrocytes.[11][12][13] As a result, collagen is retained in the ER, leading to ER stress, altered extracellular matrix composition, and eventual chondrocyte apoptosis.[11][12][13] In addition, S1P deficiency **disrupts mannose‑6‑phosphate–dependent delivery of lysosomal enzymes to lysosomes**, causing partial mis-sorting and increased secretion of lysosomal hydrolases into extracellular fluids and blood.[11][12][16][13] These secreted lysosomal enzymes contribute to **degradation of the bone matrix**, further aggravating skeletal dysplasia.[11][12][13][16]  

Thus, the functional consequence of *MBTPS1* mutations in SEDKF/MBTPS1-SEMD is a combined defect in ER stress adaptation and lysosomal enzyme trafficking, with cell-type specificity for chondrocytes. In ACMG/AMP mechanistic terms, the variants lead to **loss of normal protein function**, rather than gain of function or dominant negative effects. The disease mechanism is **haploinsufficiency at the cellular level** in homozygous or compound heterozygous individuals, while heterozygous carriers maintain enough S1P activity to avoid disease.  

### 4.4 Modifier Genes and Epigenetic Information

To date, no **modifier genes** have been conclusively identified that alter severity or expression of SEDKF/MBTPS1-SEMD. Differences in clinical features among reported patients—such as presence or absence of intellectual disability, seizures, or craniosynostosis—may reflect genetic background or other ER stress-related pathways, but specific loci have not been mapped.[16][17][18][11] Model organism studies in mice suggest that other components of the UPR and ER stress networks (e.g., IRE1, PERK, ATF6) can modulate cellular responses to ER stress, but these have not been directly linked to phenotypic variability in MBTPS1-deficient humans.[11][12][13]  

No epigenetic signatures (DNA methylation patterns, histone modifications, chromatin changes) specific to SEDKF/MBTPS1-SEMD have been reported in the literature. Since the disease is driven by coding-region mutations in *MBTPS1*, epigenetic dysregulation is not considered a primary etiologic factor. Nonetheless, epigenetic mechanisms could influence expression of other ER-stress and lysosomal genes, potentially modifying disease severity. As high-throughput epigenomic profiling of rare skeletal dysplasias has not yet been performed, epigenetic data for SEDKF/MBTPS1-SEMD remain unavailable.  

### 4.5 Chromosomal Abnormalities

The causal genetic lesions in SEDKF/MBTPS1-SEMD are typically **single‑gene variants** in *MBTPS1*, rather than large-scale chromosomal abnormalities. However, the 2024 cutis laxa case reported a **complete gene deletion** of *MBTPS1* in compound heterozygosity with a splice-affecting variant, representing a structural variant affecting the gene locus.[4] This deletion is submicroscopic rather than a cytogenetically visible chromosomal aberration and would be classified as a gene-level structural variant detectable by techniques such as chromosomal microarray or targeted copy number analysis.  

No aneuploidies, translocations, or large inversions have been associated with SEDKF/MBTPS1-SEMD. The chromosomal location 16q23.3–q24.1 is noted, but the surrounding region has not been implicated in syndromic chromosomal disorders related to the SEDKF phenotype.[2][6][9][10] For a disease knowledge base, structural variants involving the *MBTPS1* locus should be cataloged as part of the spectrum of pathogenic variants, but **chromosomal-level disorders** are not etiologically central in this condition.  

---

## 5. Environmental Information

### 5.1 Environmental and Lifestyle Factors

Current evidence indicates that **environmental and lifestyle factors do not play a primary causal role** in SEDKF/MBTPS1-SEMD. All reported patients have biallelic pathogenic *MBTPS1* variants, and there is no documentation of environmental exposures (toxins, radiation, pollution, occupational hazards) triggering similar skeletal dysplasia in the absence of genetic mutations.[11][16][18][4][1][17] Environmental factors may still influence general health and comorbidities—for example, nutrition can affect bone health, and physical activity may modulate musculoskeletal strength—but these influences are nonspecific and do not alter the fundamental pathogenesis of SEDKF.  

Lifestyle factors such as smoking, alcohol consumption, and exercise have not been systematically studied in this ultra-rare disease, largely because reported cases involve children or young adults and the primary focus has been on genetic and mechanistic characterization.[11][16][18][4][7] It is plausible that heavy weight-bearing exercises or activities stressing the spine could exacerbate kyphoscoliosis or spinal pain in affected individuals; GeneReviews suggests avoiding sports that place significant stress on the spine (e.g., heavy lifting, weight-bearing exercises) in children with significant kyphoscoliosis.[17] This recommendation aims to prevent secondary complications rather than modulate disease risk.  

### 5.2 Infectious Agents

No infectious agents have been implicated in the etiology or exacerbation of SEDKF/MBTPS1-SEMD. The skeletal and biochemical phenotype is tightly linked to germline *MBTPS1* mutations, and there is no evidence of postinfectious or autoimmune mechanisms driving the disorder.[11][16][17][18] While infections can complicate the clinical course (e.g., respiratory infections in patients with chest deformity or sleep apnea), they are not part of the disease mechanism.  

In a disease knowledge base, environmental and infectious sections for SEDKF/MBTPS1-SEMD can be annotated as **no known specific environmental or infectious etiologic factors**, with emphasis on genetic causation and the absence of documented gene–environment interaction effects.  

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

The mechanistic pathway from *MBTPS1* mutations to the clinical manifestations of SEDKF/MBTPS1-SEMD can be expressed as a sequential causal chain, integrating molecular, cellular, tissue, and clinical levels.  

Step 1: Biallelic germline loss-of-function variants in *MBTPS1* reduce or abolish site‑1 protease (S1P) activity in the Golgi apparatus, leading to markedly decreased functional MBTPS1 transcripts and protein.[11][12][16][18][4]  

Step 2: Loss of S1P activity leads to impaired proteolytic activation of specific membrane-bound transcription factors, particularly the ER stress transducer BBF2H7 (CREB3L2), while residual S1P activity may suffice for activation of SREBPs and lipid homeostasis.[11][12][13]  

Step 3: Impaired BBF2H7 activation results in defective transcriptional responses to ER stress in chondrocytes, causing reduced capacity for collagen synthesis and secretion and prolonged retention of collagen within the ER.[11][12][13]  

Step 4: Persistent ER retention of collagen and unresolved ER stress leads to activation of apoptotic pathways in chondrocytes, resulting in increased chondrocyte apoptosis and decreased numbers of functional cartilage cells in growth plates and articular cartilage.[11][12][13]  

Step 5: In parallel, S1P deficiency causes partial impairment of mannose‑6‑phosphate–dependent Golgi-to-lysosome transport of lysosomal enzymes, leading to abnormal secretion of lysosomal hydrolases into the extracellular space and circulation.[11][12][16][13]  

Step 6: Increased extracellular and plasma lysosomal enzyme activity contributes to degradation of bone matrix and cartilage extracellular matrix, exacerbating skeletal dysplasia and reducing bone mineral density.[11][12][13][16]  

Step 7: The combined effects of chondrocyte apoptosis, altered collagen trafficking, and bone matrix degradation result in spondyloepiphyseal and epimetaphyseal dysplasia, vertebral and long bone malformations, osteopenia, and disproportionate short stature.[11][16][17][18]  

Step 8: Secondary effects on connective tissue and other organs lead to chest deformity, hip dysplasia, inguinal hernia, protruding abdomen, craniosynostosis, cataracts, and facial dysmorphism, reflecting broader consequences of matrix and connective tissue abnormalities; some of these steps are inferred rather than fully demonstrated.[16][17][1][4][18]  

Step 9: Elevated plasma lysosomal enzymes, skeletal deformities, and associated features such as cataracts and inguinal hernias manifest clinically as SEDKF/MBTPS1-SEMD, influencing growth, mobility, vision, and overall quality of life.[11][16][17][1][18][4]  

### 6.2 Molecular Pathways: ER Stress, UPR, and Lysosomal Biogenesis

At the molecular level, SEDKF/MBTPS1-SEMD involves dysregulation of ER stress pathways and lysosomal biogenesis. S1P is a key protease in the **unfolded protein response (UPR)**, particularly via activation of ATF6 and BBF2H7/CREB3L2.[11][12][13] When misfolded proteins accumulate in the ER, ATF6 translocates to the Golgi, where S1P cleaves its luminal domain, releasing a transcription factor that upregulates chaperones and components of the ER quality control machinery.[11][12][13] Similarly, BBF2H7/CREB3L2 undergoes regulated intramembrane proteolysis by S1P and participates in ER stress responses, especially in chondrocytes where it governs collagens such as type II and type IX.[11][12][13]  

Kondo et al. showed that in S1P-deficient cells, activation of BBF2H7 is specifically impaired, leading to failure of appropriate ER stress responses in chondrocytes.[11][12] They stated that “the defective S1P function specifically impairs activation of the ER stress transducer BBF2H7, leading to ER retention of collagen in chondrocytes.”[11][12] This defect in UPR signaling underlies the retention of collagen in the ER and subsequent ER stress and apoptosis. Gene Ontology terms applicable here include *response to endoplasmic reticulum stress* (GO:0034976), *unfolded protein response* (GO:0030968), and *regulation of collagen biosynthetic process* (GO:0032964).  

S1P also contributes to **lysosomal biogenesis** by regulating transcription factors that control genes involved in lysosome formation and function. Kondo et al. demonstrated that S1P deficiency causes partial impairment of mannose‑6‑phosphate–dependent delivery of lysosomal enzymes to lysosomes.[11][12][13] In the Golgi, lysosomal hydrolases are tagged with mannose‑6‑phosphate, which directs them to lysosomes via mannose‑6‑phosphate receptors; S1P deficiency disrupts this trafficking, leading to mis-sorting and secretion of lysosomal enzymes into the extracellular space and plasma.[11][12][16][13] This process can be annotated with GO terms such as *lysosome organization* (GO:0007040), *protein glycosylation* (GO:0006486), and *intracellular protein transport* (GO:0006886).  

These molecular pathway disruptions—impaired ER stress signaling and lysosomal enzyme trafficking—are upstream mechanisms that cascade into cellular and tissue-level pathology in SEDKF/MBTPS1-SEMD.  

### 6.3 Cellular Processes: Chondrocyte Apoptosis and Matrix Degradation

At the cellular level, the primary affected cell type is the **chondrocyte**, the cartilage-forming cell in growth plates and articular cartilage.[11][12][13][16] Kondo et al. emphasized that “S1P deficiency also causes abnormal secretion of lysosomal enzymes due to partial impairment of mannose-6-phosphate-dependent delivery to lysosomes” and that “collectively, these abnormalities lead to apoptosis of chondrocytes and lysosomal enzyme–mediated degradation of the bone matrix.”[11][12][13]  

Chondrocytes in S1P-deficient conditions experience ER stress due to retained collagen and compromised UPR signaling, leading to an imbalance between survival and apoptosis pathways.[11][12][13] Increased apoptosis decreases the number of chondrocytes available to produce cartilage matrix, thereby impairing growth plate function and long bone elongation, which translates clinically into short stature and skeletal deformities.[11][16][17][18] The relevant GO biological processes include *chondrocyte differentiation* (GO:0002062), *cartilage development* (GO:0051216), *apoptotic process* (GO:0006915), and *endochondral ossification* (GO:0001958). The primary cell type can be annotated using Cell Ontology term *chondrocyte* (CL:0000138).  

Simultaneously, mis-sorted lysosomal enzymes secreted into the extracellular environment exert **matrix-degrading effects** on bone and cartilage. These hydrolases can cleave proteoglycans, glycosaminoglycans, and other components of the extracellular matrix, weakening the structural integrity of bone and cartilage.[11][12][13][16] Carvalho’s patient showed elevated plasma activities of enzymes such as beta-hexosaminidase, iduronate‑2‑sulfatase, and alpha‑N‑acetylglucosaminidase, all of which are implicated in breakdown of glycosaminoglycans and other matrix components.[16] This contributes to osteopenia and fragmented femoral heads, as observed radiographically.[16][15]  

Thus, at the cellular level, SEDKF/MBTPS1-SEMD is characterized by **chondrocyte ER stress and apoptosis, coupled with extracellular matrix degradation** due to secreted lysosomal hydrolases. These processes are downstream consequences of defective S1P function and lie at the center of the pathophysiology.  

### 6.4 Protein Dysfunction and Structural Considerations

Site‑1 protease itself is a type I transmembrane serine protease with luminal catalytic domain and a transmembrane segment anchoring it in the Golgi membrane.[11][12][13] Pathogenic variants in SEDKF/MBTPS1-SEMD often affect critical regions of the protein. For example, the D365G missense variant in Kondo’s index case lies in the luminal domain and affects either splicing or protein folding, leading to severely reduced protein expression.[11][12][8] The nonsense variants p.Trp983Ter and p.Q886* truncate the C‑terminal region, likely destabilizing the protein or abolishing function.[16][18] The p.Ser878Arg missense variant in the Saudi case occurs in a conserved region and may disrupt structural integrity or catalytic activity.[5]  

These variants cause **loss of protease activity**, resulting in failure to cleave target transcription factors. Structural predictions and functional assays confirm that many missense variants reduce protease function, supporting classification as loss-of-function mutations.[11][12][18][4] In contrast, the p.Pro1003Ser variant associated with neuromuscular symptoms appears to cause **altered rather than abolished S1P activity**, with increased activation of UPR and lipid regulatory pathways, demonstrating that different structural alterations can produce distinct phenotypes.[14]  

Protein dysfunction can be annotated with GO molecular function terms such as *serine-type endopeptidase activity* (GO:0004252), *protease activity* (GO:0008233), and *transcription factor binding* (GO:0008134). The structural perturbation of S1P, rather than misfolding of collagen itself, is the primary protein abnormality in SEDKF/MBTPS1-SEMD.  

### 6.5 Metabolic and Biochemical Changes

Metabolically, SEDKF/MBTPS1-SEMD presents an interesting dichotomy: **lipid metabolism remains largely intact**, whereas ER stress and lysosomal enzyme trafficking are severely disrupted. Kondo et al. observed that residual S1P expression in their patient was “sufficient for lipid homeostasis but not for ER and lysosomal functions, especially in chondrocytes.”[11][12][13] This suggests that different thresholds of S1P activity are required for different pathways, with lipid regulation being more resilient.  

Biochemically, the most prominent change is elevated plasma lysosomal hydrolase activity. Carvalho’s Table 1 shows increased plasma activities for multiple enzymes, including total beta-hexosaminidases, iduronate‑2‑sulfatase, and alpha‑N‑acetylgalactosaminidase, while leukocyte activities remained within reference ranges.[16] This pattern implies dysregulated enzyme sorting rather than primary enzyme deficiency. The presence of significant lysosomal enzyme activity in plasma is unusual and differentiates SEDKF from classic lysosomal storage disorders, where enzyme activity is reduced or absent in cells.[16][11][15][17]  

Energy metabolism and systemic metabolic profiles have not been extensively reported, but there is no indication of major disturbances in glucose or lipid metabolism. ER stress and UPR pathways, however, affect protein folding and secretion, particularly of collagen and other matrix proteins. This can influence bone and cartilage metabolism and may indirectly affect mineralization and bone density.[11][12][13][16]  

Chemical entities central to the pathophysiology include collagen (CHEBI:38161), mannose‑6‑phosphate (CHEBI:16182), and various lysosomal hydrolases such as beta‑hexosaminidase and iduronate‑2‑sulfatase, which are enzymes rather than small molecules but could be annotated in enzyme databases.  

### 6.6 Immune System and Tissue Damage Mechanisms

The immune system is not a primary driver of SEDKF/MBTPS1-SEMD, and there is no evidence of autoimmunity or immunodeficiency in reported patients.[11][16][17][18] However, chronic ER stress and lysosomal dysfunction can potentially influence inflammatory signaling pathways, even if this has not yet been documented in this specific disease.  

Tissue damage in SEDKF/MBTPS1-SEMD results primarily from **ER stress-induced apoptosis and lysosomal enzyme-mediated matrix degradation**, rather than from inflammatory infiltration or ischemia.[11][12][13][16] The skeletal tissue, particularly vertebrae and long bones, experiences cumulative damage as chondrocytes die and bone matrix is degraded, leading to deformities and osteopenia.[11][16][17][18] Craniofacial and connective tissues may also be affected, contributing to craniosynostosis and cutis laxa in some patients.[16][4]  

Histopathological data are limited, but mechanistic studies suggest that cartilage tissue would exhibit decreased cellularity, increased apoptosis markers, and altered collagen organization.[11][12][13] Bone tissue might show reduced mineralization and increased resorption, consistent with osteopenia. These tissue damage mechanisms can be annotated with GO terms such as *cell death* (GO:0008219), *negative regulation of bone mineralization* (GO:0030500), and *extracellular matrix disassembly* (GO:0022617).  

### 6.7 Molecular Profiling and Advanced Technologies

Comprehensive transcriptomic, proteomic, metabolomic, or single-cell profiling studies have not yet been published specifically for SEDKF/MBTPS1-SEMD. Kondo et al. performed functional studies in cultured cells and mice, examining collagen trafficking, ER stress markers, and lysosomal enzyme localization, but these were targeted analyses rather than broad omics profiling.[11][12][13] There are no GEO or ArrayExpress datasets listed in the provided search results for MBTPS1-SEMD, and no multi-omics integration efforts have been reported.  

Nevertheless, the mechanistic findings align with broader themes in skeletal dysplasia research, where ER stress and collagen misfolding are common pathophysiologic threads.[11][12][13] Kondo et al. concluded that “our findings may also lead to new therapies for other genetic skeletal diseases, as ER dysfunction is common in these disorders,” underscoring the potential for cross-disease insights.[11][12][13] Future application of single-cell and spatial transcriptomics could elucidate how different chondrocyte subpopulations respond to S1P deficiency and how matrix remodeling occurs within growth plates and articular cartilage.  

For now, molecular profiling in SEDKF/MBTPS1-SEMD is largely inferred from mechanistic experiments and general ER stress biology, and explicit omics datasets are not available.  

---

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

SEDKF/MBTPS1-SEMD primarily affects the **skeletal system**, including the spine, long bones, and cranial bones, but also involves other organs such as the eyes and, variably, the brain and skin. Vertebral bodies in the thoracolumbar spine show dysplasia, contributing to kyphoscoliosis and spinal deformity.[11][16][15][17] Long bones, especially femurs, tibiae, and the bones of the hands and feet, exhibit small and irregular epiphyses, mildly enlarged metaphyses, and in some cases fragmented sclerotic femoral heads.[16][15] Cranial bones may show a copper-beaten appearance and premature fusion of sutures (craniosynostosis).[16][15][17] These structures can be mapped to UBERON terms such as *thoracic vertebra* (UBERON:0002415), *lumbar vertebra* (UBERON:0002438), *femur* (UBERON:0000981), *metacarpal bone* (UBERON:0001448), *metatarsal bone* (UBERON:0001447), and *skull* (UBERON:0003129).  

Ocular involvement is significant, with **bilateral cataracts** affecting the lens of the eye (UBERON:0001791).[11][16][1][17] Chest deformities influence the thoracic cage and ribs, while inguinal hernias involve the lower abdominal wall and inguinal canal (UBERON:0001555).[1][15][17] The abdomen is protruding due to musculoskeletal and connective tissue changes, rather than intrinsic visceral organ disease.[1][16][17]  

Secondary organ involvement includes the **respiratory system**, affected by kyphoscoliosis and chest deformity, and potentially the **central nervous system**, in cases with seizures or craniosynostosis.[16][17] Sleep apnea reflects airway and upper respiratory tract compromise.[18] Overall, the disease engages musculoskeletal, ocular, and occasionally neurologic systems, with skeletal structures being primary.  

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, SEDKF/MBTPS1-SEMD involves **cartilage, bone, and connective tissue**, all of which are forms of connective tissue. Growth plate cartilage, articular cartilage, and trabecular bone are particularly affected. Vertebral and long bone deformities reflect abnormal endochondral ossification and altered cartilage matrix.[11][12][13][16] Bone tissue shows reduced mineral density and osteopenia.[16][15][17] Connective tissues of the abdominal wall and skin may also be involved, as evidenced by inguinal hernias and cutis laxa.[1][4][17]  

The primary cell type is the **chondrocyte** (CL:0000138) in cartilage, along with **osteoblasts** (CL:0000122) and **osteoclasts** (CL:0000121) in bone, which respond to altered matrix quality and bone remodeling signals.[11][12][13][16] Fibroblasts in the dermis and connective tissue may be affected in cases with cutis laxa or hernias.[4] Lens epithelial cells and fiber cells in the eye may be impacted in cataract formation, although the exact mechanism linking MBTPS1 deficiency to lens opacity is not fully elucidated.[11][16][1][17]  

The ER and lysosomal dysfunction observed in S1P-deficient cells suggests that any cell reliant on high-level protein secretion and lysosomal processing could potentially be vulnerable, but chondrocytes appear to be the most sensitive due to their heavy collagen production.[11][12][13]  

### 7.3 Subcellular Compartments

Subcellular compartments central to SEDKF/MBTPS1-SEMD include the **Golgi apparatus**, **endoplasmic reticulum (ER)**, and **lysosomes**. S1P is a Golgi-resident protease, and its deficiency disrupts processing of ER stress transcription factors, linking Golgi function to ER stress signaling.[11][12][13] The ER is the site of collagen synthesis and folding, and in S1P-deficient cells, collagen accumulates in the ER due to impaired trafficking and UPR responses, causing ER stress.[11][12][13] Lysosomes are the terminal destination for many hydrolases, and their mis-sorting in S1P deficiency results in increased secretion of enzymes into the extracellular space.[11][12][16][13]  

These subcellular structures can be annotated with GO Cellular Component terms such as *Golgi apparatus* (GO:0005794), *endoplasmic reticulum* (GO:0005783), and *lysosome* (GO:0005764). Additional relevant compartments include the *secretory vesicle* (GO:0099503) and *extracellular region* (GO:0005576), where mis-sorted lysosomal enzymes accumulate.  

### 7.4 Localization and Lateralization

Anatomically, SEDKF/MBTPS1-SEMD is **generalized rather than focal**, affecting multiple skeletal regions. Vertebral and long bone abnormalities are bilateral and systemic.[11][16][15][17] Hip dysplasia may be bilateral or asymmetric, but reports often describe involvement of both hips.[16][15] Cataracts are typically bilateral.[11][16][1][17] Inguinal hernias may be unilateral or bilateral, depending on individual anatomy, though bilateral hernias can occur.[1][17]  

No specific lateralization patterns (e.g., strictly right-sided involvement) have been reported. The disease affects axial and appendicular skeleton in a diffuse manner, consistent with a systemic genetic disorder of skeletal development and connective tissue integrity.  

---

## 8. Temporal Development

### 8.1 Onset and Early Course

SEDKF/MBTPS1-SEMD is a **congenital, pediatric-onset disorder**, although some features emerge postnatally rather than in utero. NORD reports that affected individuals often have low birth weight and delayed growth milestones.[1] Kondo’s index patient exhibited severely retarded growth from early infancy, with skeletal abnormalities recognized in childhood.[11][12][13] Carvalho’s case presented with severe growth retardation, cataract, and dysmorphic features by age five.[16] The Chinese patient described by Qiu et al. was diagnosed at age eleven after progressive short stature and skeletal deformities became evident.[18] The adult case with cutis laxa suggests that diagnosis can be delayed into adulthood, particularly when skeletal dysplasia is initially misattributed to other conditions such as geroderma osteodysplastica.[4]  

Onset pattern is **insidious but chronic**, with growth failure and skeletal deformities gradually becoming more pronounced over the first decade of life. Cataracts may be congenital or develop in early childhood. Inguinal hernias and protruding abdomen often present in childhood, sometimes requiring early surgical intervention.[1][16][17] Neurological features such as seizures and craniosynostosis may emerge during infancy or early childhood.[16][17]  

### 8.2 Progression and Disease Staging

SEDKF/MBTPS1-SEMD shows **progressive skeletal involvement** but a relatively stable pattern of non-skeletal features once established. There is no formal staging system analogous to cancer staging, but a conceptual framework can distinguish early, intermediate, and advanced phases.  

In the **early phase**, infants and toddlers exhibit delayed growth, early spinal curvature, and subtle facial dysmorphism. Cataracts may be detected by pediatric ophthalmology, and inguinal hernias may be present.[1][11][16][18]  

By the **intermediate phase** (childhood to adolescence), short stature becomes pronounced, kyphosis and scoliosis worsen, chest and hip deformities become more evident, and gait abnormalities such as waddling emerge. Radiographic studies reveal diffuse osteopenia, vertebral dysplasia, irregular epiphyses, and metaphyseal changes.[16][15][17] Cataracts often require surgical removal, and craniosynostosis may necessitate neurosurgical intervention.[16][17]  

In the **advanced phase** (late adolescence to adulthood), skeletal deformities stabilize but remain disabling, and complications such as chronic back pain, hip arthropathy, and limited mobility are prominent. The adult cutis laxa case illustrates that connective tissue changes may become more visible with age.[4] Overall disease duration is lifelong, with no spontaneous remission.  

### 8.3 Rate of Progression and Course Patterns

The rate of skeletal progression varies among individuals but is generally **slow and chronic**, reflecting the long timescale of bone growth and remodeling.[11][16][17][18] Vertebral and long bone deformities progress as growth plates operate under conditions of chondrocyte ER stress and apoptosis. Once skeletal maturity is reached, deformities may stabilize, though degenerative changes can accrue.  

Non-skeletal features like cataracts and craniosynostosis follow their own timelines. Cataracts may form early and, once removed surgically, remain corrected, representing a **treatment-induced stabilization** rather than ongoing progression.[16][17] Craniosynostosis, if present, progresses during infancy and early childhood and then stabilizes due to fused sutures.[16][17]  

There are no documented episodes of acute exacerbations or remissions driven by environmental triggers. The disease course is **steadily progressive for skeletal features** and **relatively stable for treated ocular and cranial manifestations**.  

### 8.4 Critical Periods and Windows for Intervention

Critical periods in SEDKF/MBTPS1-SEMD include **early childhood**, when growth patterns and skeletal deformities begin to diverge from normal, and **infancy to early childhood**, when craniosynostosis and cataracts manifest. Early recognition of short stature and skeletal abnormalities and prompt radiographic and biochemical evaluation can lead to timely diagnosis and genetic confirmation.[11][16][17][18][1]  

Early surgical intervention for craniosynostosis can prevent intracranial pressure elevation and neurodevelopmental complications.[16][17] Timely cataract extraction can preserve vision and optimize developmental outcomes.[16][17] Orthopedic monitoring during childhood can guide interventions to manage kyphoscoliosis and hip dysplasia, potentially reducing long-term disability.[15][17]  

Recombinant human growth hormone therapy, if used, appears to be more effective when initiated during childhood, before epiphyseal closure. A 2023 case report suggested that rhGH can partially repair growth retardation in an SEDKF patient, though more evidence is needed.[7] This underscores childhood as a window of therapeutic opportunity for growth-modifying strategies.  

Thus, the temporal dimension of SEDKF/MBTPS1-SEMD involves early-onset, chronic progression, and critical windows for surgical and growth-related interventions, all of which should be captured in the disease knowledge base.  

---

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

SEDKF/MBTPS1-SEMD is inherited in an **autosomal recessive** manner, as established by multiple case reports and summarized in GeneReviews and NORD.[2][11][16][17][1] In families where both parents are heterozygous for a pathogenic *MBTPS1* variant, each sibling has a 25% chance of being affected, a 50% chance of being an asymptomatic carrier, and a 25% chance of being unaffected and not a carrier.[17][1]  

Penetrance for biallelic loss-of-function *MBTPS1* variants appears to be **complete**, meaning that individuals with two pathogenic alleles invariably manifest some degree of the skeletal and biochemical phenotype, although expressivity is variable.[11][16][18][4] Expressivity ranges from severe short stature and complex skeletal deformities with craniosynostosis and seizures to milder forms with normal intelligence and fewer extraskeletal complications.[11][16][17][18][4][1] The variability may reflect differences in residual S1P activity, genetic background, or nonspecific environmental factors.  

There is no evidence of genetic anticipation, germline mosaicism, or X‑linked or mitochondrial inheritance in SEDKF/MBTPS1-SEMD. All reported family structures fit autosomal recessive inheritance with heterozygous carrier parents.[11][16][18][4][17][1]  

### 9.2 Epidemiology: Prevalence, Incidence, and Demographics

SEDKF/MBTPS1-SEMD is extremely rare. NORD reports that the disease was only recently discovered and that “only thirteen patients have been identified so far” worldwide.[1] Earlier literature cited fewer cases: Carvalho et al. in 2020 noted that “to date, only one affected individual has been found to harbor compound heterozygous pathogenic variants in *MBTPS1* associated with a spondyloepiphyseal dysplasia,” referring to the index case, and that their report represented the second individual.[16] Subsequent publications and case reports have increased the count, with Qiu et al. stating that “to date, only three *MBTPS1*-related SEDKF cases were reported” before their Chinese case.[18] A Frontiers in Pediatrics case report on rhGH therapy in 2023 noted that variants in *MBTPS1* can cause SEDKF, Silver-Russell syndrome, and CAOP syndrome, but emphasized the rarity of SEDKF.[7] The 2024 cutis laxa case reported that only seven SEDKF cases had been described in the literature, and that their case represented the eighth, though this count may have been limited to published SEDKF-specific articles rather than all MBTPS1-SEMD cases.[4]  

Given these numbers, the **prevalence** is likely well below 1 in 1,000,000, and the **incidence** is extremely low, with sporadic cases around the world. There are no population-based registries or epidemiologic estimates for this disease, and the small number of known cases precludes accurate calculation of incidence and prevalence metrics.[1][16][17][18][4][11]  

Demographically, cases have been reported in diverse geographic regions, including Japan (index case), Brazil, Saudi Arabia, China, and an unspecified region for the 2024 cutis laxa case.[11][16][5][18][4] This suggests that SEDKF/MBTPS1-SEMD is **pan-ethnic**, although founder effects or regional variant clusters have not been defined. Sex distribution appears roughly equal; reported patients include both males and females, but the small sample size prevents meaningful conclusions about sex ratios.[11][16][18][4][5][1][17] Age at diagnosis ranges from early childhood to adulthood, reflecting variable recognition and access to genetic testing.[11][16][18][4][1]  

Carrier frequency of pathogenic *MBTPS1* variants is unknown in the general population, but given the extreme rarity of affected individuals, carrier rates are expected to be very low.[16][17][1] However, in populations with consanguinity or specific founder mutations, carrier frequency may be higher, as suggested by homozygous variants in some families.[16][5][18]  

---

## 10. Diagnostics

### 10.1 Clinical Evaluation and Imaging

Diagnosis of SEDKF/MBTPS1-SEMD rests on **characteristic clinical and radiographic findings**, elevated lysosomal hydrolase enzymes in plasma or dried blood spots, and biallelic pathogenic variants in *MBTPS1* identified by molecular genetic testing.[17][15][1][11][16][18] GeneReviews states that “the diagnosis of *MBTPS1*-SEMD is established in a proband with characteristic clinical and radiographic findings, elevated lysosomal hydrolase enzymes in plasma or dried blood spots, and biallelic pathogenic variants in *MBTPS1* identified by molecular genetic testing.”[17]  

Clinically, pediatricians and geneticists should suspect SEDKF/MBTPS1-SEMD in children with disproportionate short stature, kyphosis or scoliosis, chest deformity, hip dysplasia, inguinal hernia, protruding abdomen, cataracts, facial dysmorphism, and possibly developmental delay or craniosynostosis.[1][16][17][18][11] Comprehensive physical examination, growth chart review, and family history are essential initial steps.  

Imaging plays a crucial diagnostic role. Radiographs of the spine and long bones reveal spondyloepiphyseal and epimetaphyseal dysplasia, diffuse osteopenia, and characteristic vertebral and epiphyseal abnormalities.[11][16][15][17] Carvalho’s patient showed “diffuse osteopenia, copper-beaten appearance of the skull, dysplasia of multiple thoracolumbar vertebrae, long bones with small and irregular epiphyses and mildly enlarged and irregular metaphyses, hip dysplasia with small fragmented sclerotic femoral heads, and short metacarpals and metatarsals with small epiphyses.”[16][15] Such findings can suggest a skeletal dysplasia and guide further evaluation.  

Dual-energy X‑ray absorptiometry (DXA) scans can document reduced bone mineral density, supporting the osteopenia component.[11][16][17] CT or MRI of the skull may be used to evaluate craniosynostosis, while echocardiography and pulmonary function tests assess secondary complications of chest deformity and kyphoscoliosis.  

### 10.2 Laboratory Biomarkers

Laboratory diagnostics are pivotal in differentiating SEDKF/MBTPS1-SEMD from lysosomal storage disorders. The **signature biomarker** is elevated activity of multiple lysosomal hydrolase enzymes in plasma or dried blood spots, with normal or near-normal activity in leukocytes. Kondo et al. first reported elevated blood lysosomal enzymes in their SEDKF patient.[11][12][13] Carvalho’s patient had increased plasma activities of several lysosomal enzymes—total beta-hexosaminidases, alpha-N‑acetylglucosaminidase, iduronate-2‑sulfatase, alpha-N‑acetylgalactosaminidase, hexosaminidase A, and others—while enzyme activities in leukocytes remained within reference ranges.[16] Their Table 1 provides specific enzyme activity values compared to normal ranges, highlighting the distinctive pattern of plasma elevation.[16]  

MedGen and GeneReviews emphasize that increased concentrations of multiple lysosomal hydrolases in plasma and dried blood spots are a key diagnostic criterion for MBTPS1-SEMD.[15][17] Laboratories performing lysosomal enzyme panels can detect these elevations, prompting consideration of MBTPS1-related disorders in the differential diagnosis when leukocyte enzyme activity is normal.[16][11][15][17]  

Other laboratory tests, including complete blood counts, liver and kidney function tests, and lipid profiles, are typically normal.[1][11][16] Bone turnover markers may reflect altered bone metabolism but are not specific. Genetic testing (discussed below) ultimately confirms the diagnosis.  

### 10.3 Genetic Testing Strategies

Genetic testing is **essential for definitive diagnosis** of SEDKF/MBTPS1-SEMD. NORD advises that the diagnosis should be based on characteristic symptoms and clinical evaluation and “confirmed by whole-genome sequencing,” with detection of variants in the *MBTPS1* gene via genomic sequencing.[1] In practice, **whole-exome sequencing (WES)** has been the most commonly used approach in reported cases.  

Kondo et al. performed WES in their index patient, who had spondyloepiphyseal dysplasia and elevated plasma lysosomal enzymes but negative testing for mucolipidosis-associated genes; WES identified compound heterozygosity for a 1‑bp duplication and a missense mutation in *MBTPS1*.[2][11][12] Carvalho’s Brazilian patient also underwent WES, which revealed a homozygous nonsense variant p.Trp983Ter.[16] Qiu’s Chinese patient underwent WES, leading to identification of compound heterozygous *MBTPS1* variants including a synonymous splicing variant.[18] The adult cutis laxa case used WES followed by targeted assays to document a gene deletion and a splice-affecting variant.[4]  

Given the rarity of the disease and the potential for novel variants, **WES or whole-genome sequencing (WGS)** is recommended for patients with the characteristic phenotype and biochemical profile, rather than targeted single-gene testing alone. Once *MBTPS1* variants are identified, segregation analysis in parents confirms autosomal recessive inheritance.[11][16][18][4][2]  

ClinVar and OMIM entries for *MBTPS1* list known pathogenic variants associated with SEDKF/MBTPS1-SEMD, which can inform variant interpretation.[2][8][11][16][18] However, the growing spectrum of *MBTPS1* mutations, including synonymous and structural variants, underscores the need for careful evaluation of novel alleles, functional validation, and consideration of splicing effects.[18][4]  

Chromosomal microarray (CMA) can detect large deletions encompassing *MBTPS1*, as in the adult case with complete gene deletion, and may be indicated when WES reveals only a single variant or when clinical suspicion remains high despite negative sequencing.[4] Karyotyping and FISH are not generally useful, as there are no cytogenetically visible chromosomal abnormalities specific to this disorder.  

### 10.4 Omics-Based and Advanced Diagnostics

Omics-based diagnostics, such as RNA sequencing, proteomics, and metabolomics, have not yet entered routine clinical use for SEDKF/MBTPS1-SEMD, but functional assays in research settings have proven valuable. Qiu et al. used RNA splicing assays to confirm that the synonymous variant c.774C>T caused aberrant pre‑mRNA splicing in *MBTPS1*, underpinning its pathogenic classification.[18] The 2024 cutis laxa case used RNA splicing assays and possibly copy number analysis to validate the structural deletion and splicing variant combination.[4]  

Proteomic analyses of lysosomal enzymes in plasma could in theory refine the biomarker profile, but current diagnostics rely on enzyme activity assays. Transcriptomic profiling of patient-derived fibroblasts or chondrocytes could reveal downstream gene expression changes due to S1P deficiency, though this remains a research tool rather than a clinical diagnostic method.[11][12][13]  

Liquid biopsy approaches, such as cell-free DNA or RNA detection, are not relevant for this inherited skeletal dysplasia. The principal “omics” tool in diagnosis is genomic sequencing (WES/WGS), supplemented by targeted functional studies for particular variants.  

### 10.5 Differential Diagnosis and Screening

Differential diagnosis includes **other spondyloepiphyseal and spondyloepimetaphyseal dysplasias** and **lysosomal storage disorders**. Clinically, SEDKF/MBTPS1-SEMD overlaps with conditions such as spondyloepiphyseal dysplasia congenita, spondyloepimetaphyseal dysplasia due to collagen gene mutations, and geroderma osteodysplastica, which present with short stature and skeletal deformities.[1][4][16][17] The adult cutis laxa case was initially suspected to have geroderma osteodysplastica due to cutis laxa and skeletal dysplasia, but genetic testing revealed SEDKF.[4]  

Lysosomal storage disorders such as mucolipidosis II/III, mucopolysaccharidoses, and multiple sulfatase deficiency can produce skeletal dysplasia and elevated lysosomal enzymes, but in those conditions, enzyme activities are typically reduced in leukocytes or fibroblasts, whereas in SEDKF/MBTPS1-SEMD, leukocyte enzyme activity is normal and plasma levels are elevated.[16][11][15][17] Negative testing for mucolipidosis-associated genes and normal leukocyte enzyme assays help exclude these conditions.[2][11][16]  

Screening for SEDKF/MBTPS1-SEMD in asymptomatic individuals is not currently practiced, given its rarity and the absence of specific newborn screening markers. However, **carrier screening and prenatal/preimplantation genetic testing** can be offered to families with known pathogenic *MBTPS1* variants, as noted in GeneReviews.[17]  

---

## 11. Outcome/Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

No systematic data on survival rates, mortality, or life expectancy in SEDKF/MBTPS1-SEMD are available, due to the small number of cases and relatively short follow-up durations. Reported patients have survived into childhood, adolescence, and adulthood, suggesting that the disease is **compatible with long-term survival**, especially with appropriate supportive care.[11][16][18][4][7][1][17]  

There are no reports of early mortality directly attributable to SEDKF/MBTPS1-SEMD, though severe craniosynostosis, respiratory complications from chest deformity and kyphoscoliosis, or untreated sleep apnea could theoretically increase morbidity and mortality risks.[16][17][18] The adult cutis laxa case at age 20 indicates that at least some patients reach adulthood and live with chronic skeletal and connective tissue manifestations.[4]  

Without more extensive longitudinal data, it is reasonable to infer that **life expectancy may be moderately reduced** due to cumulative skeletal complications and potential respiratory or neurologic issues, but many individuals could live into adulthood with proper management.  

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in SEDKF/MBTPS1-SEMD primarily stems from **orthopedic, visual, and functional impairments**. Disproportionate short stature and kyphoscoliosis can limit mobility, produce chronic pain, and restrict physical functioning.[11][16][17] Hip dysplasia may necessitate surgical intervention and can lead to early osteoarthritis.[16][15] Chest deformity can impair respiratory mechanics, and sleep apnea can cause fatigue and cardiovascular strain.[18][17] Cataracts reduce visual acuity and require surgery.[16][1][17]  

Craniosynostosis and seizures, when present, raise the risk of neurodevelopmental complications and require neurosurgical and neurologic management.[16][17] Inguinal hernias and protruding abdomen involve abdominal wall weakness and may necessitate multiple surgeries.[1][17]  

The degree of disability varies. Some individuals may ambulate independently but with a waddling gait and limited stamina; others may require assistive devices or orthopedic braces. Intellectual disability, when present, is usually mild and allows for some level of independent function, though developmental support may be needed.[16][17][18][11]  

Quality of life is impacted by physical limitations, pain, visual impairment, and psychosocial aspects such as short stature and facial differences. NORD emphasizes that management is symptomatic and supportive, aiming to improve daily functioning and quality of life.[1] GeneReviews recommends physical therapy to maximize mobility and reduce late-onset orthopedic complications, as well as developmental and educational support.[17]  

### 11.3 Disease Course and Complications

SEDKF/MBTPS1-SEMD follows a **chronic, lifelong course** with progressive skeletal deformities and relatively stable non-skeletal features once treated. Complications can include chronic back and hip pain, early degenerative joint disease, increased risk of fractures due to osteopenia, and respiratory compromise from chest deformity and kyphoscoliosis.[11][16][17][18] Sleep apnea, if untreated, can lead to cardiovascular and neurocognitive complications.[18][17] Cataracts, if not surgically addressed, cause long-term visual impairment.[16][1][17]  

Neurologic complications such as seizures and raised intracranial pressure from craniosynostosis may occur, as described by Carvalho.[16] Abdominal hernias can recur after surgery or lead to complications such as incarceration if not properly managed.[1][17]  

There is no evidence of spontaneous recovery or complete reversal of skeletal abnormalities. RhGH therapy may improve growth velocity and height in some patients, but long-term impacts on skeletal deformity and functional outcomes remain unclear.[7]  

Prognostic factors likely include severity of skeletal deformity, presence of craniosynostosis and seizures, degree of respiratory involvement, and access to multidisciplinary care. However, explicit prognostic biomarkers have not been identified in this ultra-rare disease.  

---

## 12. Treatment

### 12.1 Pharmacotherapy and Symptomatic Medications

There are currently **no therapies that target the underlying cause** of SEDKF/MBTPS1-SEMD—that is, the defective S1P function due to *MBTPS1* mutations.[1][17][11][16] Management is therefore symptomatic and supportive. NORD explicitly states that “there are currently no therapies that target the cause of SEDKF. Patients can be managed with symptomatic/supportive treatment.”[1] GeneReviews similarly emphasizes management of manifestations rather than disease modification.[17]  

Pharmacologic strategies focus on managing pain, sleep apnea, seizures, and other symptoms. Analgesics, including nonsteroidal anti-inflammatory drugs (NSAIDs), can help alleviate musculoskeletal pain from kyphoscoliosis and hip dysplasia. Antiepileptic drugs are used for seizure control in patients with epilepsy.[16][17] Medications for sleep apnea, such as nasal steroids or CPAP support, may be part of a broader treatment plan, though mechanical interventions (CPAP devices) are more central than drugs.[18][17]  

In some cases, **recombinant human growth hormone (rhGH)** therapy has been attempted to address growth retardation. A 2023 case report documented rhGH therapy in an SEDKF patient with compound heterozygous *MBTPS1* variants.[7] The authors reported that rhGH improved growth velocity and suggested that “growth hormone therapy can repair growth retardation in patients with spondyloepiphyseal dysplasia, Kondo-Fu type; however, more evidence of such patient cases is required to support this hypothesis.”[7] This indicates a potential role for NCIT term *Recombinant Human Growth Hormone Therapy* (NCIT:C94396) as an intervention in the disease knowledge base, with the caveat that evidence remains limited and anecdotal.  

No specific pharmacogenomic data exist for drug metabolism or efficacy in SEDKF/MBTPS1-SEMD patients, and standard dosing regimens apply.  

### 12.2 Advanced Therapeutics: Gene, Cell, and Targeted Therapies

No **gene therapy, cell therapy, or targeted molecular therapies** have yet been developed specifically for SEDKF/MBTPS1-SEMD. However, mechanistic insights from Kondo et al. suggest future directions. The authors demonstrated that correction of an *MBTPS1* variant or reduction of ER stress could mitigate collagen trafficking defects in S1P-deficient cells, implying that **therapies targeting ER function** might have disease-modifying potential.[11][12][13]  

Gene therapy approaches would theoretically aim to restore functional *MBTPS1* expression in affected tissues, particularly chondrocytes. Viral vector-mediated delivery of *MBTPS1* or gene editing (e.g., CRISPR-Cas systems) to correct pathogenic variants could be envisioned, but no preclinical or clinical programs have been reported for this specific condition. Similarly, cell-based therapies, such as mesenchymal stem cell transplantation or chondrocyte replacement, remain theoretical and unstudied in MBTPS1-SEMD.  

Targeted therapies modulating ER stress responses—such as small molecules affecting ATF6, IRE1, PERK pathways, or chaperone upregulators—could be explored in model systems, but translation to clinic for SEDKF is at a conceptual stage. Kondo’s mention that ER dysfunction is common across genetic skeletal diseases highlights a potential shared therapeutic space for chaperone-based or ER-stress modulation strategies.[11][12][13]  

### 12.3 Surgical and Interventional Treatments

Surgical interventions are central to managing SEDKF/MBTPS1-SEMD complications. GeneReviews outlines treatment of specific manifestations: craniosynostosis should be treated by craniofacial specialists, kyphoscoliosis and scoliosis managed by orthopedists, hip dysplasia corrected surgically as needed, hernias repaired by surgeons or gastroenterologists, and cataracts removed by ophthalmologists.[17] NORD similarly emphasizes surgical management of cataracts and hernias.[1]  

Craniosynostosis surgery aims to relieve intracranial pressure and prevent neurodevelopmental compromise.[16][17] Spinal surgery for severe kyphoscoliosis may involve fusion procedures and instrumentation to stabilize the spine and prevent progression of deformity. Hip reconstruction surgery addresses dysplasia and restores joint function.[16][15][17] Hernia repair, often via open or laparoscopic techniques, prevents complications such as incarceration or strangulation.[1][17] Cataract extraction with lens implantation restores visual clarity.[16][17]  

These interventions correspond to NCIT terms such as *Craniosynostosis Surgery* (NCIT:C51797), *Spinal Fusion* (NCIT:C51619), *Hip Joint Surgery* (NCIT:C51695), *Hernia Repair* (NCIT:C51656), and *Cataract Extraction* (NCIT:C15268). Surgical timing and outcomes depend on individual severity and comorbidities, but generally, early intervention improves prognosis.  

### 12.4 Supportive and Rehabilitative Care

Supportive care and rehabilitation are critical components of SEDKF/MBTPS1-SEMD management. GeneReviews recommends **physical therapy** to maximize mobility and reduce the risk of later-onset orthopedic complications, and **developmental and educational support** for children with developmental delays or learning difficulties.[17] Physical therapy helps maintain joint range of motion, strengthen supporting musculature, and optimize gait patterns, reducing pain and disability. Occupational therapy can assist with activities of daily living and adaptive strategies for short stature and skeletal deformity.  

Nutritional support, including adequate calcium and vitamin D supplementation, is advised for individuals with reduced bone density to support bone health and minimize fracture risk.[17][16] Sleep studies and respiratory evaluation inform interventions for sleep apnea and chest deformity-related respiratory impairment.[18][17] Psychological support may be beneficial to address self-esteem, social integration, and coping with chronic disease.  

NCIT terms relevant to these interventions include *Physical Therapy Procedure* (NCIT:C15295), *Occupational Therapy* (NCIT:C15299), *Nutritional Support* (NCIT:C15306), and *Psychosocial Support* (NCIT:C17047).  

### 12.5 Experimental Treatments and Clinical Trials

As of the available literature and resources, there are **no registered clinical trials** specifically targeting MBTPS1-SEMD or SEDKF. NORD points patients and clinicians to general clinical trial registries such as ClinicalTrials.gov and the EU Clinical Trials Register for potential studies, but no MBTPS1-specific programs are listed in the provided search results.[1]  

The JCI Insight mechanistic study hints at potential therapeutic strategies involving ER stress reduction and correction of *MBTPS1* variants.[11][12][13] However, these concepts have not yet translated into formal clinical trials. The rhGH therapy case report can be considered an experimental, off-label use of growth hormone in SEDKF, but it is a single patient experience rather than a controlled trial.[7]  

For knowledge base purposes, experimental treatments may be annotated as **conceptual or case-report-level**, with caution about limited evidence and absence of robust efficacy data.  

---

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

For a rare, autosomal recessive disorder like SEDKF/MBTPS1-SEMD, **primary prevention** focuses on preventing disease occurrence through genetic counseling and reproductive options. Once pathogenic *MBTPS1* variants are identified in an affected proband, carrier testing of at-risk relatives and options such as preimplantation genetic diagnosis (PGD) and prenatal testing can be offered.[17][1] GeneReviews explicitly notes that “once the *MBTPS1* pathogenic variants have been identified in an affected family member, carrier testing for at-risk relatives and prenatal and preimplantation genetic testing are possible.”[17] These interventions allow families to make informed reproductive choices to reduce the likelihood of having another affected child.  

**Secondary prevention** involves early detection and prompt management of disease manifestations to minimize complications. This includes early recognition of short stature and skeletal deformities, early ophthalmologic evaluation for cataracts, surveillance for craniosynostosis and seizures, and timely surgical and rehabilitative interventions.[16][17][1][18] Annual growth assessment, orthopedic evaluation, ophthalmologic examination, and developmental assessment are recommended in GeneReviews.[17]  

**Tertiary prevention** aims to prevent or reduce complications in individuals already living with SEDKF/MBTPS1-SEMD. Measures include physical therapy to prevent contractures, orthopedic interventions to prevent severe deformities, vitamin D and calcium to reduce fracture risk, and sleep apnea management to prevent cardiovascular and neurocognitive sequelae.[17][16][18]  

### 13.2 Screening and Genetic Counseling

Population-based newborn screening for SEDKF/MBTPS1-SEMD is not currently feasible or recommended, given its extreme rarity and lack of a simple, specific biochemical marker that distinguishes it from other conditions. Elevated lysosomal enzymes in dried blood spots might theoretically be detectable, but such findings are nonspecific and more commonly associated with lysosomal storage disorders.[15][16][11][17]  

Genetic counseling is central to preventive strategies. Families with an affected child should receive counseling about autosomal recessive inheritance, carrier risks, recurrence risks, and options for prenatal or preimplantation testing.[17][1] Counselling also addresses psychosocial implications, expectations for disease course, and the importance of early multidisciplinary care. NSGC and ACMG guidelines for counseling in autosomal recessive disorders apply, with disease-specific tailoring for MBTPS1-SEMD.  

### 13.3 Behavioral and Public Health Interventions

Behavioral interventions specific to SEDKF/MBTPS1-SEMD include **avoiding activities that stress the spine**, such as heavy lifting and high-impact sports, in children with significant kyphoscoliosis.[17] This recommendation aims to prevent exaggerated deformity and reduce risk of spinal injury. More generally, maintaining a healthy lifestyle—with balanced diet, regular low-impact exercise, and avoidance of smoking—supports overall health but does not directly prevent disease onset.  

Public health interventions are not disease-specific, as SEDKF/MBTPS1-SEMD is too rare to warrant population-level programs. However, improving access to genetic testing, specialized orthopedic and craniofacial care, and multidisciplinary rare disease clinics indirectly promotes better outcomes and secondary/tertiary prevention.  

---

## 14. Other Species / Natural Disease

### 14.1 Species and Orthologous Genes

The *MBTPS1* gene is conserved across vertebrates, and orthologs exist in multiple species. Alliance of Genome Resources notes that MBTPS1 is implicated in human spondyloepiphyseal dysplasia Kondo-Fu type and lists orthologs in model organisms.[9][6] NCBI Taxonomy identifies *Homo sapiens* (taxon ID 9606) as the species affected by SEDKF/MBTPS1-SEMD, while model organism databases document MBTPS1 orthologs in mice, zebrafish, and other species.  

In zebrafish, ZFIN lists “spondyloepiphyseal dysplasia Kondo-Fu type” (DOID:0112283) as a human disease, and MBTPS1 orthologs are used in disease modeling.[6] In mice, MBTPS1 orthologs have been studied in the context of lipid metabolism and ER stress, and S1P-deficient mice show phenotypes related to ER function and lysosomal biogenesis.[11][12][13]  

### 14.2 Natural Disease in Animals and Comparative Pathology

There are no reports of **naturally occurring MBTPS1-related SEDKF-like disease** in companion animals or livestock. OMIA (Online Mendelian Inheritance in Animals) does not list MBTPS1-related skeletal dysplasia, and veterinary literature has not described an analogous syndrome linked to MBTPS1 mutations in dogs, cats, or other animals.  

Nonetheless, comparative studies of ER stress and lysosomal enzyme trafficking in animal models inform understanding of the human disease. Kondo et al. used mice and cultured cells to analyze S1P function, showing that S1P regulates lipogenesis, ER function, and lysosome biogenesis in mice and cells, and exploring how S1P differentially regulates these diverse functions in humans.[11][12][13] They highlighted that no human disease with S1P deficiency had been identified before their study, underscoring the novelty of SEDKF.[11][12][13]  

Evolutionary conservation of S1P function across species suggests that MBTPS1-related mechanisms are shared, even if clinical phenotypes diverge. This supports translational research in model organisms while recognizing the unique skeletal phenotype in humans.  

### 14.3 Zoonotic Potential and Cross-Species Susceptibility

SEDKF/MBTPS1-SEMD is a **noninfectious, genetic disorder** and has no zoonotic potential. Cross-species susceptibility pertains only to experimental models, where MBTPS1 mutations or knockouts can be induced to study S1P function. There is no natural cross-species transmission or environmental exposure leading to similar disease across humans and animals.  

---

## 15. Model Organisms

### 15.1 Types of Models and Phenotype Recapitulation

Model organisms play an important role in dissecting the mechanistic underpinnings of SEDKF/MBTPS1-SEMD, though explicit disease models labeled as “SEDKF” are not yet extensively cataloged. Kondo et al. performed mechanistic experiments in **mouse models and cell lines** to understand S1P function.[11][12][13] They showed that S1P regulates lipogenesis, ER function, and lysosome biogenesis in mice and cultured cells, and that S1P deficiency specifically impairs BBF2H7 activation, collagen trafficking, and lysosomal enzyme delivery.[11][12][13] These findings recapitulate key aspects of the human disease mechanism at the cellular level.  

The JCI Insight study likely used conditional MBTPS1 knockout mice or S1P-deficient cells to observe skeletal and lysosomal phenotypes, although detailed model descriptions are not fully provided in the snippet.[11][12][13] These models reproduce ER stress and lysosomal mis-sorting but may not fully recapitulate the human skeletal phenotype, as differences in cartilage biology and growth plate structure exist between species.  

Zebrafish models could theoretically be developed by knocking down or editing the MBTPS1 ortholog, given their utility in studying skeletal development and ER stress. ZFIN’s annotation of DOID:0112283 suggests that MBTPS1-related skeletal dysplasia is recognized as a human disease for cross-species modeling.[6]  

### 15.2 Genetic Models and Limitations

Genetic models for MBTPS1-related disorders include **knockout, knock-in, and transgenic mice** and potentially CRISPR-edited zebrafish or cell lines. Knockout models (global MBTPS1 deletion) might be embryonic lethal or have profound systemic effects, limiting their utility for studying postnatal skeletal phenotypes. Conditional knockouts (e.g., cartilage-specific MBTPS1 deletion) would be more informative for SEDKF-like skeletal dysplasia, but detailed descriptions are not available in the current literature snippets.[11][12][13]  

Knock-in models introducing specific human pathogenic variants (e.g., D365G) could mirror the partial loss-of-function phenotype seen in SEDKF patients, allowing study of residual S1P activity and its differential impact on lipid metabolism versus ER/lysosomal functions.[11][12][13] However, such models have not been explicitly reported.  

Limitations of existing models include species differences in growth plate biology, collagen expression patterns, and lifespan. Mouse and zebrafish skeletons differ in architecture and growth dynamics, so phenotypes may not fully reflect human SEDKF manifestations. Additionally, the ultra-rare nature of the human disease means that model development has focused more on generic S1P function than on disease-specific features.  

### 15.3 Applications of Models

Despite limitations, models of S1P deficiency and MBTPS1 mutation support key applications:  

First, they allow **validation of mechanistic hypotheses**, such as the role of BBF2H7/CREB3L2 in chondrocyte ER stress responses and collagen trafficking.[11][12][13] Second, they enable screening of potential **therapeutic agents** targeting ER stress or lysosomal trafficking, such as chaperones, ER-stress modulators, or small molecules affecting mannose‑6‑phosphate receptor function. Third, they provide a platform for **gene therapy feasibility studies**, evaluating viral vector delivery, gene editing efficiency, and safety in vivo.  

These models therefore inform both fundamental biology and translational strategies, even though formal MBTPS1-SEMD disease models and large animal studies are not yet established.  

---

## Conclusion

Spondyloepiphyseal dysplasia, Kondo-Fu type—now more broadly conceptualized as **MBTPS1-related spondyloepimetaphyseal dysplasia with elevated lysosomal enzymes (MBTPS1-SEMD)**—is an ultra-rare, autosomal recessive skeletal dysplasia defined by biallelic loss-of-function variants in *MBTPS1*, the gene encoding site‑1 protease (S1P).[2][11][16][17][1][6][9] Clinically, the disorder manifests as postnatal-onset disproportionate short stature, spondyloepiphyseal and epimetaphyseal dysplasia, kyphoscoliosis, decreased bone mineral density, chest and hip deformity, inguinal hernia, protruding abdomen, cataracts, facial dysmorphism, and frequently elevated lysosomal hydrolases in plasma and dried blood spots.[11][16][17][15][1][18][4]  

Mechanistically, S1P deficiency in humans selectively disrupts ER stress signaling and lysosomal enzyme trafficking in chondrocytes, particularly via impaired activation of BBF2H7/CREB3L2 and partial impairment of mannose‑6‑phosphate–dependent delivery of lysosomal enzymes to lysosomes.[11][12][13][16] These defects lead to ER retention of collagen, chondrocyte apoptosis, and abnormal secretion of lysosomal hydrolases, which in turn degrade bone and cartilage matrix and produce the characteristic skeletal phenotype.[11][12][13][16] The biochemical hallmark of elevated plasma lysosomal enzymes with normal leukocyte activity distinguishes MBTPS1-SEMD from classic lysosomal storage disorders, while the presence of cataracts and connective tissue manifestations differentiates it from other spondyloepiphyseal dysplasias.[11][16][15][17][1]  

Diagnostic workup involves careful clinical and radiographic assessment, lysosomal enzyme assays in plasma and leukocytes, and ultimately genomic sequencing to identify biallelic pathogenic *MBTPS1* variants.[2][11][16][18][4][1][17] Treatment remains supportive, focusing on orthopedic surgery for skeletal deformities, craniofacial surgery for craniosynostosis, cataract extraction, hernia repair, physical therapy, and developmental support.[17][1][16][18] Recombinant human growth hormone therapy has shown promising results in a single case, improving growth velocity, but evidence is insufficient to consider it standard of care.[7] There are currently no therapies that directly restore S1P function or correct ER and lysosomal defects, although mechanistic insights point to potential future strategies involving ER stress modulation and gene correction.[11][12][13]  

Epidemiologically, SEDKF/MBTPS1-SEMD is extremely rare, with only a small number of patients reported worldwide.[1][16][18][4][11][7] This rarity poses challenges for systematic study of natural history, prognosis, and therapeutic outcomes. Nevertheless, the disorder occupies an important place in skeletal dysplasia and lysosomal biology, as it reveals a unique role for S1P in human skeletal development and lysosomal enzyme trafficking, and highlights ER dysfunction as

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:32316092` (1 mention) - Prevention of Intramammary Infections by Prepartum External Application of a Teat Dip Containing Lactic Acid Bacteria with Antimicrobial Properties in Dairy Heifers.
  - shared terms: none

Weighed against this report's own most characteristic terms: `sedkf`, `mbtps1-semd`, `disease`, `skeletal`, `mbtps1`, `lysosomal`, `dysplasia`, `patient`, `variant`, `enzyme`, `s1p`, `genetic`, `function`, `stress`, `kondo`, `phenotype`, `disorder`, `cataract`, `bone`, `craniosynostosis`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 81 |
| Resolved | 78 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 74 |
| Terms named correctly | 40 |
| Terms named as a **different** term | 25 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002653` (1 mention) - the report calls it "Spondyloepiphyseal dysplasia"; HP calls it **Bone pain**
- `HP:0002808` (4 mentions) - the report calls it "Kyphosis", "Scoliosis"; HP calls it **Kyphosis**
- `HP:0002012` (1 mention) - the report calls it "Facial dysmorphism"; HP calls it **Abnormality of the abdominal organs**
- `HP:0003524` (1 mention) - the report calls it "Disproportionate short stature"; HP calls it **Decreased methionine synthase activity**
- `HP:0000316` (1 mention) - the report calls it "Prominent forehead"; HP calls it **Hypertelorism**
- `HP:0000321` (1 mention) - the report calls it "Malar prominence"; HP calls it **Square face**
- `HP:0001050` (1 mention) - the report calls it "Cutis laxa"; HP calls it **Plethora**
- `HP:0001552` (1 mention) - the report calls it "Protruding abdomen"; HP calls it **Barrel-shaped chest**
- `NCIT:C17048` (1 mention) - the report calls it "Quality of Life"; NCIT calls it **Questionnaire**
- `NCIT:C19499` (1 mention) - the report calls it "Functional Status"; NCIT calls it **DNA Biochemistry**
- `GO:0006517` (1 mention) - the report calls it "protein processing in Golgi apparatus"; GO calls it **protein deglycosylation**
- `UBERON:0002415` (1 mention) - the report calls it "thoracic vertebra"; UBERON calls it **tail**
- `UBERON:0002438` (1 mention) - the report calls it "lumbar vertebra"; UBERON calls it **ventral tegmental nucleus**
- `CL:0000122` (1 mention) - the report calls it "osteoblasts"; CL calls it **stellate neuron**
- `CL:0000121` (1 mention) - the report calls it "osteoclasts"; CL calls it **Purkinje cell**
- `NCIT:C94396` (1 mention) - the report calls it "Recombinant Human Growth Hormone Therapy"; NCIT calls it **Best Practice**
- `NCIT:C51797` (1 mention) - the report calls it "Craniosynostosis Surgery"; NCIT calls it **AdEERS Contact**
- `NCIT:C51619` (1 mention) - the report calls it "Spinal Fusion"; NCIT calls it **Inguinal Lymphadenectomy**
- `NCIT:C51695` (1 mention) - the report calls it "Hip Joint Surgery"; NCIT calls it **Total Abdominal Hysterectomy**
- `NCIT:C51656` (1 mention) - the report calls it "Hernia Repair"; NCIT calls it **Maxillectomy**
- `NCIT:C15268` (1 mention) - the report calls it "Cataract Extraction"; NCIT calls it **Laser Surgery**
- `NCIT:C15295` (1 mention) - the report calls it "Physical Therapy Procedure"; NCIT calls it **Chemotherapeutic Perfusion**
- `NCIT:C15299` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Pharmacokinetics**
- `NCIT:C15306` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Primary Prevention**
- `NCIT:C17047` (1 mention) - the report calls it "Psychosocial Support"; NCIT calls it **Quality of Life**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004348` (2 mentions) - the report calls it "Abnormal lysosomal enzyme activity"; HP calls it **Abnormality of bone mineral density**
- `HP:0003621` (1 mention) - the report calls it "Childhood onset"; HP calls it **Juvenile onset**
- `GO:0030968` (1 mention) - the report calls it "unfolded protein response"; GO calls it **endoplasmic reticulum unfolded protein response**, and lists "ER unfolded protein response" among its other names
- `GO:0032964` (1 mention) - the report calls it "regulation of collagen biosynthetic process"; GO calls it **collagen biosynthetic process**
- `GO:0006486` (1 mention) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**
- `GO:0008233` (1 mention) - the report calls it "protease activity"; GO calls it **peptidase activity**, and lists "protease activity" among its other names
- `GO:0030500` (1 mention) - the report calls it "negative regulation of bone mineralization"; GO calls it **regulation of bone mineralization**
- `UBERON:0001448` (1 mention) - the report calls it "metacarpal bone"; UBERON calls it **metatarsal bone**
- `UBERON:0001447` (1 mention) - the report calls it "metatarsal bone"; UBERON calls it **tarsal bone**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002808` - called "Kyphosis", "Scoliosis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.