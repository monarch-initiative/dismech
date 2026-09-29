---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T06:06:56.585789'
end_time: '2026-08-30T06:37:57.618960'
duration_seconds: 1861.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Progressive Pseudorheumatoid Arthropathy of Childhood
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 29
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 25
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 11
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: HP:0002758
    reported_labels:
    - Osteoarthritis
    - Clinical
    ontology_label: Osteoarthritis
  - term_id: HP:0001387
    reported_labels:
    - Joint stiffness
    - Clinical sign
    ontology_label: Joint stiffness
  - term_id: HP:0000944
    reported_labels:
    - Platyspondyly
    - Radiographic
    ontology_label: Abnormal metaphysis morphology
  - term_id: HP:0000939
    reported_labels:
    - Osteoporosis
    - Laboratory/imaging
    ontology_label: Osteoporosis
  - term_id: HP:0002515
    reported_labels:
    - Waddling gait
    - Clinical sign
    ontology_label: Waddling gait
  - term_id: HP:0004322
    reported_labels:
    - Short stature
    - Physical
    ontology_label: Short stature
  - term_id: HP:0100360
    reported_labels:
    - Enlarged interphalangeal joints
    - Physical
    ontology_label: Upper-limb joint contracture
  - term_id: NCIT:C157866
    reported_labels:
    - Total Hip Arthroplasty
    ontology_label: Gluten Free Diet
  - term_id: NCIT:C51765
    reported_labels:
    - Physical Therapy
    ontology_label: Bilateral Salpingectomy with Oophorectomy
  - term_id: NCIT:C1898
    reported_labels:
    - Calcitriol/Vitamin D
    ontology_label: Physical Carcinogens
  - term_id: HP:0002826
    reported_labels:
    - Spinal canal stenosis
    ontology_label: Halberd-shaped pelvis
  - term_id: HP:0002970
    reported_labels:
    - Physical
    ontology_label: Genu varum
  - term_id: UBERON:0002217
    reported_labels:
    - articular cartilage of joint
    ontology_label: synovial joint
  - term_id: UBERON:0003656
    reported_labels:
    - interphalangeal joint
    ontology_label: mesopodium bone
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Progressive_Pseudorheumatoid_Arthropathy_Of_Childhood-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Progressive_Pseudorheumatoid_Arthropathy_Of_Childhood-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Pseudorheumatoid Arthropathy of Childhood
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Pseudorheumatoid Arthropathy of Childhood** covering all of the
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

# Progressive Pseudorheumatoid Arthropathy of Childhood (PPRD): A Comprehensive Disease Characteristics Report

**Disease:** Progressive Pseudorheumatoid Arthropathy of Childhood
(synonyms: Progressive Pseudorheumatoid Dysplasia, PPRD/PPD; Spondyloepiphyseal Dysplasia Tarda with Progressive Arthropathy, SEDT-PA)
**Category:** Mendelian, autosomal recessive
**OMIM:** 208230 · **Causal gene:** *WISP3*/*CCN6* (chr6q22)
**Suggested MONDO:** MONDO:0009215

---

## Summary

Progressive Pseudorheumatoid Arthropathy of Childhood — more commonly termed **progressive pseudorheumatoid dysplasia (PPRD)** — is a rare autosomal recessive skeletal dysplasia caused by **biallelic loss-of-function variants in the *WISP3*/*CCN6* gene on chromosome 6q22**. *CCN6* encodes a secreted, modular matricellular protein of the CCN family that modulates BMP and Wnt signaling and supports articular-chondrocyte homeostasis. When its function is lost, the articular cartilage of multiple joints progressively degenerates in a **noninflammatory** fashion, producing the disease's hallmark presentation: symmetric polyarticular stiffness and enlargement, "knobbly" interphalangeal joints, platyspondyly, short stature, waddling gait, and early secondary osteoarthritis, with onset typically between ages 3 and 8 years.

The single most clinically important feature of PPRD is that it **closely mimics juvenile idiopathic arthritis (JIA)** and is very frequently misdiagnosed as such. Unlike JIA, however, inflammatory markers (ESR, CRP) are normal and serologies (RF, ACPA, ANA, HLA-B27) are negative. This distinction matters therapeutically: because the disease is noninflammatory, immunosuppressants, DMARDs, and biologics are ineffective, and patients are often exposed to years of unnecessary treatment before the correct molecular diagnosis is established by whole-exome sequencing or targeted gene panels. Radiographic clues — platyspondyly with intravertebral herniations, epiphyseal/metaphyseal changes, and enlarged interphalangeal joints — combined with normal inflammatory parameters and a compatible family history should prompt molecular testing.

There is currently **no disease-modifying pharmacotherapy** for PPRD. Management is entirely supportive: analgesia/NSAIDs, physiotherapy, calcium/vitamin D (with calcitriol for documented deficiency), genetic counseling, and, for end-stage large-joint disease, **joint arthroplasty**, which produces durable functional and quality-of-life gains. Lifespan is generally normal, but the disability burden is high — roughly half of patients lose independent ambulation by adolescence. This report synthesizes nine confirmed findings and 36 reviewed papers into a full disease-characteristics profile spanning etiology, phenotype, molecular mechanism, epidemiology, diagnosis, prognosis, treatment, prevention, and model systems.

---

## Key Findings

### Finding 1 — PPRD is caused by biallelic loss-of-function variants in *WISP3*/*CCN6* (chr6q22), inherited autosomal recessively

PPRD is a monogenic Mendelian disorder. Multiple independent cohorts have confirmed that biallelic pathogenic variants in *WISP3* (also designated *CCN6*), located on chromosome 6q22, cause the disease through loss of function. As stated directly in the Egyptian cohort report: *"PPRD occurs due to loss of function pathogenic variants in WISP3 (CCN6) gene, located on chromosome 6q22"* ([PMID: 37377052](https://pubmed.ncbi.nlm.nih.gov/37377052/)).

The mutational spectrum is broad and dominated by single-nucleotide variants and small indels, with variants concentrated in exons 2, 4, and 5. Representative cohort data are summarized below:

| Cohort | N patients | Distinct variants | Notable/founder alleles | PMID |
|---|---|---|---|---|
| Egypt | 23 | 11 (5 novel): nonsense (p.L27\*, p.Q126\*), frameshift (p.C54fs\*12), missense (p.Leu246Pro), splice (IVS3-1G>A) | — | [37377052](https://pubmed.ncbi.nlm.nih.gov/37377052/) |
| China | 105 | 33 (79% Chinese-exclusive) | c.624dupA (hotspot; later onset) | [36622578](https://pubmed.ncbi.nlm.nih.gov/36622578/) |
| India | 35 (25 families) | — | c.1010G>A (p.Cys337Tyr) in 10 families | [22987568](https://pubmed.ncbi.nlm.nih.gov/22987568/) |
| Turkey | 44 | — | c.156C>A (p.Cys52\*) in 53.3% of families | [34919662](https://pubmed.ncbi.nlm.nih.gov/34919662/) |

A genotype–phenotype correlation has been documented in the Chinese population: *"Among the five hotspot variants, c.624dupA is associated with later onset of disease, more extensive joint involvement, and a tendency to affect elbow joints"* ([PMID: 36622578](https://pubmed.ncbi.nlm.nih.gov/36622578/)). The Indian founder allele is likewise well established: *"One missense mutation (c.1010G>A; p.Cys337Tyr) appears to be the most common in our population being seen in 10 unrelated families"* ([PMID: 22987568](https://pubmed.ncbi.nlm.nih.gov/22987568/)). Although nearly all reported variants are SNVs or small indels, a copy-number deletion in *trans* with a single-nucleotide variant has also been reported in monozygotic twins, detected only by genome sequencing after a 13-year diagnostic odyssey ([PMID: 38958524](https://pubmed.ncbi.nlm.nih.gov/38958524/)).

**Ontology suggestions:** Gene HGNC *WISP3*/*CCN6*; inheritance HP:0000007 (Autosomal recessive inheritance).

### Finding 2 — PPRD is a noninflammatory progressive arthropathy frequently misdiagnosed as juvenile idiopathic arthritis

Clinically, PPRD presents in childhood with symmetric polyarticular stiffness and enlargement, characteristic "knobbly" interphalangeal joints, gait abnormality, platyspondyly, short stature, and early secondary osteoarthritis with osteoporosis. In the Turkish cohort, median symptom onset was ~4 years but median age at diagnosis was 9.7 years, underscoring diagnostic delay. Gait involvement is nearly universal and disability accrues over time: *"Waddling gait occurred in 97.7% of the patients. A total of 47.7% lost independent walking ability at the median age of 12 years"* ([PMID: 34919662](https://pubmed.ncbi.nlm.nih.gov/34919662/)). Genu varum before age 3 is described as an early sign of the early-onset form.

Crucially, laboratory inflammatory markers are normal (ESR/CRP within range) and serologies are negative (RF, ACPA, ANA, HLA-B27), distinguishing PPRD from true inflammatory arthritides ([PMID: 39539552](https://pubmed.ncbi.nlm.nih.gov/39539552/), [PMID: 34749805](https://pubmed.ncbi.nlm.nih.gov/34749805/)). Despite this, the clinical resemblance to JIA leads to frequent misdiagnosis: *"Clinical features of progressive pseudorheumatoid dysplasia resemble those of juvenile idiopathic arthritis. Patients with progressive pseudorheumatoid dysplasia are usually misdiagnosed as having juvenile idiopathic arthritis"* ([PMID: 34749805](https://pubmed.ncbi.nlm.nih.gov/34749805/)). Consequently, patients are often inappropriately treated with methotrexate and biologics before the correct diagnosis ([PMID: 32894151](https://pubmed.ncbi.nlm.nih.gov/32894151/)).

**Ontology suggestions:** HP:0002758 (Osteoarthritis), HP:0001387 (Joint stiffness), HP:0000944 (Platyspondyly), HP:0000939 (Osteoporosis), HP:0002515 (Waddling gait), HP:0004322 (Short stature), HP:0100360 (Enlarged interphalangeal joints).

### Finding 3 — *WISP3*/*CCN6* modulates BMP and Wnt signaling and supports cartilage homeostasis

The molecular function of *CCN6* has been most clearly defined in zebrafish. Overexpression of zebrafish Wisp3 inhibits both BMP and Wnt signaling by binding BMP ligand and Wnt co-receptors LRP6/Frizzled; disease-causing amino-acid substitutions reduce this inhibitory activity, and morpholino knockdown alters pharyngeal cartilage size and shape ([PMID: 17823661](https://pubmed.ncbi.nlm.nih.gov/17823661/)). As stated: *"Overexpression of zebrafish Wisp3 protein inhibited bone morphogenetic protein (BMP) and Wnt signaling in developing zebrafish."*

In chondrocytes, WISP-3 acts as an autocrine/paracrine ligand and upregulates type II collagen, aggrecan, and superoxide dismutase (SOD) activity, linking it to both matrix maintenance and antioxidant defense: *"WISP-3 may also promote superoxide dismutase expression and activity in chondrocytes"* ([PMID: 16480948](https://pubmed.ncbi.nlm.nih.gov/16480948/)). A mechanistic hypothesis proposes that mutant WISP3 loses its ability to inhibit IGF-1, increasing chondrocyte sensitivity to IGF-1 and driving a shift toward hypertrophic differentiation and apoptosis ([PMID: 17363178](https://pubmed.ncbi.nlm.nih.gov/17363178/)).

Notably, the mouse model does not recapitulate the disease: *"in mice there is no apparent phenotype caused by Wisp3 deficiency or overexpression"* ([PMID: 17823661](https://pubmed.ncbi.nlm.nih.gov/17823661/)) — a critical limitation for translational research (see Model Organisms, Section 15).

**Ontology suggestions:** GO:0030509 (BMP signaling pathway), GO:0016055 (Wnt signaling pathway), GO:0051216 (cartilage development), GO:0005520 (insulin-like growth factor binding); CL:0000138 (chondrocyte).

### Finding 4 — No disease-modifying pharmacotherapy exists; management is supportive, with joint replacement effective for end-stage disease

There is no specific pharmacological treatment for PPRD; care is supportive — analgesia/NSAIDs, physiotherapy, calcium/vitamin D, calcitriol, and genetic counseling ([PMID: 38862149](https://pubmed.ncbi.nlm.nih.gov/38862149/), [PMID: 34674084](https://pubmed.ncbi.nlm.nih.gov/34674084/)). Because the disease is noninflammatory, immunosuppressants and DMARDs are ineffective ([PMID: 37417608](https://pubmed.ncbi.nlm.nih.gov/37417608/)). As stated plainly: *"Its diagnosis is only confirmed by genetic testing, and no specific pharmacological treatment is still available"* ([PMID: 38862149](https://pubmed.ncbi.nlm.nih.gov/38862149/)).

For end-stage hip and knee disease, **total joint arthroplasty** provides durable benefit. In four genetically confirmed PPRD patients undergoing total hip arthroplasty, functional and quality-of-life scores improved substantially: *"Harris Hip Score increased from 39.67 ± 9.73 points preoperatively to 91.67 ± 4.32 points postoperatively (p < 0.05); Short Form 36 increased from 19.67 ± 1.53 points preoperatively to 71.33 ± 3.06 postoperatively (p < 0.05)"* at a mean follow-up of 47.9 months, with no aseptic loosening ([PMID: 31876842](https://pubmed.ncbi.nlm.nih.gov/31876842/)). Multi-joint replacement (bilateral hips, knees, and ankle) has restored function even in young patients ([PMID: 38681928](https://pubmed.ncbi.nlm.nih.gov/38681928/), [PMID: 38862149](https://pubmed.ncbi.nlm.nih.gov/38862149/)). Calcitriol for documented low 25-OH vitamin D stabilized or improved joints in a small series ([PMID: 34674084](https://pubmed.ncbi.nlm.nih.gov/34674084/)).

**Ontology suggestions:** NCIT:C157866 (Total Hip Arthroplasty), NCIT:C51765 (Physical Therapy), NCIT:C1898 (Calcitriol/Vitamin D), NCIT:C1505 (Calcium supplement).

### Finding 5 — PPRD is a rare disease (~1 per million estimated), underdiagnosed, with founder variants in consanguineous populations

The estimated prevalence is approximately **1 per 1,000,000**, but this figure is widely regarded as an underestimate due to frequent misdiagnosis as JIA: *"Prevalence underestimated as one per million and most of the cases remain undiagnosed or treated as Juvenile Idiopathic Arthritis (JIA)"* ([PMID: 36550675](https://pubmed.ncbi.nlm.nih.gov/36550675/)). The largest cohorts derive from consanguineous or endemic populations — India, China, Turkey, and Egypt — each with population-specific hotspot/founder alleles (c.1010G>A in India, c.156C>A in 53.3% of Turkish families, c.624dupA in China). Autosomal recessive inheritance means consanguinity elevates risk.

The radiographic hallmarks that support diagnosis are well documented: *"Radiographic and magnetic resonance imaging of the cases revealed typical features characteristic for PPD-like platyspondyly, multiple intravertebral herniations, changes in metaphyses and epiphysis"* ([PMID: 15877179](https://pubmed.ncbi.nlm.nih.gov/15877179/)).

### Finding 6 — *WISP3*/*CCN6* is a secreted matricellular CCN-family protein with modular IGFBP–VWC–TSP1–CT domains; disease variants disrupt conserved cysteines

CCN6 (WISP3) is one of six CCN matricellular proteins (CCN1–CCN6). Each shares a conserved modular architecture: *"The proteins consist of 4 motifs, a signal peptide (for secretion) followed consecutively by the IGFBP, VWC, TSP1 and CT (C-terminal cysteine knot domain) motifs"* ([PMID: 27517291](https://pubmed.ncbi.nlm.nih.gov/27517291/)). These modules mediate binding to growth factors, extracellular matrix, integrins, and receptors. The N-terminal IGFBP-like module is the structural basis for the proposed IGF-1 sensitization mechanism ([PMID: 17363178](https://pubmed.ncbi.nlm.nih.gov/17363178/)).

Many PPRD-causing variants are nonsense or frameshift changes producing loss of function, while missense variants frequently substitute conserved cysteines that form the disulfide bonds stabilizing these modules (e.g., p.Cys52\*, p.Cys337Tyr, p.C54fs) ([PMID: 22987568](https://pubmed.ncbi.nlm.nih.gov/22987568/), [PMID: 34919662](https://pubmed.ncbi.nlm.nih.gov/34919662/), [PMID: 37377052](https://pubmed.ncbi.nlm.nih.gov/37377052/)).

**Ontology suggestions:** GO:0005576 (extracellular region), GO:0005520 (insulin-like growth factor binding), GO:0031012 (extracellular matrix).

### Finding 7 — PPRD belongs to a group of skeletal-dysplasia "rheumatic mimics" requiring molecular diagnosis to avoid misclassification as JIA

PPRD is one of several genetic skeletal dysplasias whose musculoskeletal presentation mimics rheumatic disease. In a Southeastern Turkey cohort of 47 individuals from 22 families with noninflammatory musculoskeletal complaints, molecular testing identified PPRD in 7 patients alongside other JIA mimics: Camptodactyly–Arthropathy–Coxa Vara–Pericarditis syndrome (n=12, *PRG4*), Hereditary Multiple Exostoses (n=9), Trichorhinophalangeal syndrome (n=5), Spondyloenchondrodysplasia with immune dysregulation (n=6), Pseudoachondroplasia (n=3, *COMP*), MPS VI, and others ([PMID: 40626694](https://pubmed.ncbi.nlm.nih.gov/40626694/)). As the authors note: *"Their musculoskeletal manifestations frequently mimic those of rheumatic diseases, especially Juvenile Idiopathic Arthritis (JIA), complicating accurate diagnosis"*, and *"Progressive Pseudorheumatoid Dysplasia (n = 7)"* was confirmed molecularly.

A PPRD-*like* phenotype can also arise from a heterozygous *COL2A1* variant, producing a type II collagenopathy overlapping with SED Stanescu type — an important differential to consider when *WISP3* testing is negative ([PMID: 26183434](https://pubmed.ncbi.nlm.nih.gov/26183434/)).

### Finding 8 — Wide expressivity from severe early-onset to delayed adult presentation; spinal canal stenosis may require surgery

Although classic onset is between 3 and 8 years — *"characterized by pain, stiffness and enlargement of multiple joints with an age of onset between 3 and 8 years old"* ([PMID: 29246200](https://pubmed.ncbi.nlm.nih.gov/29246200/)) — the phenotype spans a wide clinical spectrum. At the severe end, neglected early-onset cases present with marked muscle wasting and weakness ([PMID: 29258992](https://pubmed.ncbi.nlm.nih.gov/29258992/)); at the mild end, delayed adult presentations occur, such as a 35-year-old man with a ~20-year history diagnosed via compound *WISP3* variants (c.670dupA + c.756C>A/p.Cys252\*) ([PMID: 29246200](https://pubmed.ncbi.nlm.nih.gov/29246200/)) and a 53-year-old affected relative in an Iraqi-Jewish family carrying p.C86F ([PMID: 30922245](https://pubmed.ncbi.nlm.nih.gov/30922245/)).

Spinal involvement can progress to canal stenosis requiring surgery: *"we present a Chinese man with PPD who underwent spinal surgery twice because of canal stenosis and related symptoms caused by the disease"* (homozygous c.395G>A/p.C132Y; [PMID: 30635069](https://pubmed.ncbi.nlm.nih.gov/30635069/)). Severe early scoliosis has also been reported ([PMID: 26991965](https://pubmed.ncbi.nlm.nih.gov/26991965/)). Across the literature, diagnosis is repeatedly established by WES or gene panels once clinical suspicion is high ([PMID: 30922245](https://pubmed.ncbi.nlm.nih.gov/30922245/), [PMID: 29258992](https://pubmed.ncbi.nlm.nih.gov/29258992/), [PMID: 32894151](https://pubmed.ncbi.nlm.nih.gov/32894151/)).

**Ontology suggestions:** HP:0002826 (Spinal canal stenosis), HP:0002650 (Scoliosis), HP:0002751 (Kyphoscoliosis).

### Finding 9 — No disease-modifying drug pipeline, pharmacogenomic markers, or validated omics biomarkers exist (evidence gap)

Targeted literature searches for therapeutic-target/drug-development, chondroprotection, and disease-modifying pharmacotherapy in PPRD return no primary reports; reviews and case series consistently affirm that no specific pharmacological treatment exists ([PMID: 38862149](https://pubmed.ncbi.nlm.nih.gov/38862149/), [PMID: 30327864](https://pubmed.ncbi.nlm.nih.gov/30327864/)). No registered disease-specific interventional trials of disease-modifying agents were identified. There are no established transcriptomic, proteomic, or metabolomic patient biomarkers; the only mechanistic omics-adjacent work is in vitro chondrocyte regulation of collagen II/aggrecan/SOD ([PMID: 16480948](https://pubmed.ncbi.nlm.nih.gov/16480948/)) and a 2025 study of the molecular consequences of *CCN6* variants ([PMID: 41009407](https://pubmed.ncbi.nlm.nih.gov/41009407/)). Pharmacogenomics is not applicable because there is no disease-specific drug therapy.

---

## Section-by-Section Disease Profile

### 1. Disease Information
PPRD is a rare, autosomal recessive, **noninflammatory** skeletal dysplasia characterized by progressive degeneration of articular cartilage across multiple joints, producing pain, stiffness, joint enlargement, platyspondyly, and short stature. **Key identifiers:** OMIM **208230**; suggested **MONDO:0009215**; the gene is *WISP3*/*CCN6*. **Synonyms/alternative names:** Progressive Pseudorheumatoid Dysplasia (PPRD/PPD); Spondyloepiphyseal Dysplasia Tarda with Progressive Arthropathy (SEDT-PA); Arthropathy, Progressive Pseudorheumatoid, of Childhood (APPRC). Information is derived primarily from **aggregated disease-level resources** — cohort studies, case series, and case reports — rather than EHR-derived individual patient records.

### 2. Etiology
The primary cause is **genetic**: biallelic loss-of-function variants in *WISP3*/*CCN6* (Finding 1). No environmental, infectious, or mechanical cause initiates the disease. **Genetic risk factors:** the causal variants themselves; population-specific founder/hotspot alleles increase incidence in certain groups (c.1010G>A India, c.156C>A Turkey, c.624dupA China). **Environmental risk/protective factors:** none established; consanguinity is a demographic risk factor for recessive disease inheritance. Vitamin D deficiency is a modifiable comorbidity that may worsen skeletal outcomes and should be corrected ([PMID: 34674084](https://pubmed.ncbi.nlm.nih.gov/34674084/)). No gene–environment interactions are documented.

### 3. Phenotypes
Core phenotypes (with suggested HPO terms and qualitative frequency):

| Phenotype | Type | HPO suggestion | Onset | Frequency |
|---|---|---|---|---|
| Symmetric polyarticular stiffness/enlargement | Clinical sign | HP:0001387 | Childhood | Very frequent |
| Enlarged ("knobbly") interphalangeal joints | Physical | HP:0100360 | Childhood | Very frequent |
| Waddling gait | Clinical sign | HP:0002515 | Childhood | 97.7% ([PMID: 34919662](https://pubmed.ncbi.nlm.nih.gov/34919662/)) |
| Loss of independent ambulation | Functional | — | Adolescence | 47.7% by median age 12 |
| Platyspondyly / intravertebral herniations | Radiographic | HP:0000944 | Childhood | Frequent |
| Short stature | Physical | HP:0004322 | Childhood | Frequent |
| Early secondary osteoarthritis | Clinical | HP:0002758 | Childhood–adolescence | Frequent |
| Osteoporosis / reduced BMD | Laboratory/imaging | HP:0000939 | Childhood | Frequent |
| Genu varum (early-onset form) | Physical | HP:0002970 | <3 yr | Early sign |
| Spinal canal stenosis / scoliosis | Complication | HP:0002826 / HP:0002650 | Variable | Subset |
| Normal inflammatory markers/serology | Laboratory | — | — | Characteristic |

**Quality of life:** substantial impairment — chronic pain, progressive joint contracture, and loss of ambulation in ~half of patients by adolescence markedly reduce daily functioning; arthroplasty improves SF-36 scores dramatically ([PMID: 31876842](https://pubmed.ncbi.nlm.nih.gov/31876842/)).

### 4. Genetic/Molecular Information
**Causal gene:** *WISP3*/*CCN6* (OMIM 603400), chr6q22. **Variant classification:** the majority are pathogenic/likely pathogenic per ACMG/AMP; >70 variants reported, concentrated in exons 2, 4, and 5 ([PMID: 30327864](https://pubmed.ncbi.nlm.nih.gov/30327864/)). **Variant types:** nonsense, frameshift, missense (frequently conserved-cysteine substitutions), splice-site, and — rarely — copy-number deletions ([PMID: 38958524](https://pubmed.ncbi.nlm.nih.gov/38958524/)). **Allele frequency:** individually very rare in gnomAD; founder alleles enriched regionally. **Origin:** germline. **Functional consequence:** loss of function (Findings 1, 6). Intronic splice variants may require mRNA analysis from cultured skin fibroblasts when genomic-DNA screening is negative ([PMID: 30327864](https://pubmed.ncbi.nlm.nih.gov/30327864/)). **Modifier genes:** none firmly established, though genotype (e.g., c.624dupA) correlates with onset timing. Incidental *MEFV* variants have been co-reported but are not modifiers of PPRD per se ([PMID: 32894151](https://pubmed.ncbi.nlm.nih.gov/32894151/)). **Epigenetics / chromosomal abnormalities:** none characteristic.

### 5. Environmental Information
Not applicable as a cause — PPRD is monogenic. No environmental toxins, lifestyle factors, or infectious agents contribute to onset. Vitamin D status is the only modifiable environmental co-factor relevant to management.

### 6. Mechanism / Pathophysiology
**Molecular pathways:** *CCN6* normally inhibits **BMP** and **Wnt** signaling and supports chondrocyte matrix synthesis (type II collagen, aggrecan) and antioxidant defense (SOD) (Findings 3, 6). **Proposed causal chain:** loss-of-function *CCN6* → dysregulated BMP/Wnt signaling and increased chondrocyte sensitivity to IGF-1 → shift of articular chondrocytes toward hypertrophic/terminal differentiation and apoptosis, with reduced type II/IX collagen → progressive noninflammatory cartilage degeneration → secondary osteoarthritis, joint enlargement, platyspondyly, and disability ([PMID: 17363178](https://pubmed.ncbi.nlm.nih.gov/17363178/), [PMID: 16480948](https://pubmed.ncbi.nlm.nih.gov/16480948/)). **Cellular processes:** chondrocyte apoptosis, hypertrophic differentiation, matrix homeostasis failure, possible oxidative stress (loss of SOD support). **Immune involvement:** none — the disease is noninflammatory. **Metabolic changes:** none characteristic beyond local cartilage matrix metabolism.

```
LOF CCN6/WISP3 (biallelic)
        │
        ▼
Loss of BMP/Wnt inhibition + increased IGF-1 sensitivity
        │
        ▼
Articular chondrocyte hypertrophic shift → apoptosis
        │
        ▼
Progressive NON-inflammatory cartilage degeneration
        │
        ├──► Enlarged interphalangeal joints, joint stiffness
        ├──► Platyspondyly, intravertebral herniation, short stature
        └──► Early secondary osteoarthritis → disability / loss of ambulation
```

**GO/CL suggestions:** GO:0030509 (BMP signaling), GO:0016055 (Wnt signaling), GO:0051216 (cartilage development), GO:0006915 (apoptotic process); CL:0000138 (chondrocyte), CL:0000743 (articular chondrocyte).

### 7. Anatomical Structures Affected
**Primary organ/system:** the **skeletal system**, specifically the **articular cartilage** of multiple synovial joints (interphalangeal joints, hips, knees, elbows, ankles, shoulders, wrists) and the **vertebral column** (platyspondyly, intravertebral herniation, canal stenosis). **Secondary involvement:** secondary osteoarthritis, muscle wasting/weakness in severe cases. **Tissue/cell level:** hyaline articular cartilage; articular chondrocytes (CL:0000743). **Subcellular:** the secreted protein acts extracellularly (GO:0005576, extracellular region/matrix). **Localization:** symmetric and bilateral joint involvement is characteristic. **UBERON suggestions:** UBERON:0002217 (articular cartilage of joint), UBERON:0001474 (bone element), UBERON:0001130 (vertebral column), UBERON:0003656 (interphalangeal joint).

### 8. Temporal Development
**Onset:** typically pediatric, ages 3–8 years, but ranges from severe early-onset (<3 yr, genu varum) to delayed adult presentation ([PMID: 29246200](https://pubmed.ncbi.nlm.nih.gov/29246200/), [PMID: 30922245](https://pubmed.ncbi.nlm.nih.gov/30922245/)). **Onset pattern:** insidious, chronic. **Progression:** slowly progressive over years; ~48% lose independent ambulation by median age 12. **Course:** progressive, lifelong; no spontaneous remission. **Critical periods:** early diagnosis (childhood) is the key window to avoid inappropriate immunosuppressive treatment and to institute supportive care; end-stage large-joint disease is the window for arthroplasty.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** high/complete for biallelic LOF, with **variable expressivity** (Finding 8). **Prevalence:** ~1/1,000,000, likely underestimated ([PMID: 36550675](https://pubmed.ncbi.nlm.nih.gov/36550675/), [PMID: 30200995](https://pubmed.ncbi.nlm.nih.gov/30200995/)). **Founder effects/consanguinity:** documented in India, Turkey, China, Egypt, and an Iraqi-Jewish family; consanguinity increases risk. **Sex ratio:** no strong sex bias reported (autosomal). **Anticipation/mosaicism:** not features of this disorder.

### 10. Diagnostics
**Laboratory:** inflammatory markers (ESR, CRP) normal; RF, ACPA, ANA, HLA-B27 negative — a key discriminator from JIA. **Imaging:** skeletal survey / lateral spine radiograph showing platyspondyly, intravertebral herniations, epiphyseal/metaphyseal changes, and enlarged interphalangeal joints; MRI may show joint changes ([PMID: 15877179](https://pubmed.ncbi.nlm.nih.gov/15877179/)). **Genetic testing (definitive):** single-gene *WISP3* sequencing, skeletal-dysplasia gene panels, or WES/WGS; genome sequencing detects CNVs missed by other methods ([PMID: 38958524](https://pubmed.ncbi.nlm.nih.gov/38958524/)); mRNA analysis from skin-fibroblast culture is needed for intronic splice variants ([PMID: 30327864](https://pubmed.ncbi.nlm.nih.gov/30327864/)). **Clinical criteria:** clinical suspicion from symmetric noninflammatory polyarthropathy + knobbly IP joints + gait abnormality + normal inflammatory markers + characteristic radiographs, confirmed molecularly. **Differential diagnosis:** JIA (primary mimic), Camptodactyly–Arthropathy–Coxa Vara–Pericarditis syndrome (*PRG4*), pseudoachondroplasia (*COMP*), mucopolysaccharidoses, SED Stanescu-type / *COL2A1* type II collagenopathy, and other skeletal dysplasias ([PMID: 40626694](https://pubmed.ncbi.nlm.nih.gov/40626694/), [PMID: 26183434](https://pubmed.ncbi.nlm.nih.gov/26183434/)).

### 11. Outcome/Prognosis
**Survival:** lifespan is generally normal ([PMID: 30200995](https://pubmed.ncbi.nlm.nih.gov/30200995/)). **Morbidity:** high disability — progressive joint contracture, chronic pain, and loss of independent ambulation in ~48% by adolescence. **Complications:** severe secondary osteoarthritis, spinal canal stenosis, scoliosis, muscle wasting. **Quality of life:** markedly reduced; substantially improved after arthroplasty (SF-36 ~20→71) ([PMID: 31876842](https://pubmed.ncbi.nlm.nih.gov/31876842/)). **Prognostic factors:** genotype (e.g., c.624dupA → later onset), age at diagnosis, and access to supportive/surgical care.

### 12. Treatment
**Pharmacotherapy:** none disease-modifying; symptomatic analgesia/NSAIDs, calcium/vitamin D, calcitriol for deficiency ([PMID: 34674084](https://pubmed.ncbi.nlm.nih.gov/34674084/)). Immunosuppressants/DMARDs/biologics are **ineffective and should be avoided** ([PMID: 37417608](https://pubmed.ncbi.nlm.nih.gov/37417608/)). **Surgical/interventional:** total hip/knee arthroplasty and multi-joint replacement for end-stage disease with durable benefit (NCIT:C157866); spinal decompression/correction for canal stenosis or scoliosis ([PMID: 31876842](https://pubmed.ncbi.nlm.nih.gov/31876842/), [PMID: 38681928](https://pubmed.ncbi.nlm.nih.gov/38681928/), [PMID: 30635069](https://pubmed.ncbi.nlm.nih.gov/30635069/)). **Rehabilitative/supportive:** physiotherapy, occupational therapy, mobility aids, pain management. **Pharmacogenomics:** not applicable. **Experimental:** no registered disease-modifying trials identified.

### 13. Prevention
**Primary prevention:** genetic counseling for at-risk (especially consanguineous) families; carrier testing and, where appropriate, prenatal or preimplantation genetic diagnosis once the familial variant is known. **Secondary prevention:** early molecular diagnosis to avoid unnecessary immunosuppression and to initiate timely supportive care. **Tertiary prevention:** physiotherapy, vitamin D optimization, and well-timed arthroplasty to preserve function and prevent complications. No vaccine, behavioral, or population-based public-health intervention applies.

### 14. Other Species / Natural Disease
Orthologs of *WISP3*/*CCN6* exist across vertebrates (human, mouse *Wisp3*, zebrafish *wisp3*). **No naturally occurring animal disease** counterpart is documented (no established OMIA entry in the reviewed literature). Zebrafish require Wisp3 for normal pharyngeal cartilage development, whereas mice show no phenotype — a striking species divergence relevant to evolutionary conservation of the mechanism ([PMID: 17823661](https://pubmed.ncbi.nlm.nih.gov/17823661/)). No zoonotic or cross-species transmission applies (non-infectious disease).

### 15. Model Organisms
| Model | Phenotype recapitulation | Utility | PMID |
|---|---|---|---|
| Mouse *Wisp3* KO / overexpression | **No apparent phenotype** — does not model the disease | Limited; a major translational gap | [17823661](https://pubmed.ncbi.nlm.nih.gov/17823661/) |
| Zebrafish (morpholino knockdown / overexpression) | Alters pharyngeal cartilage size/shape; demonstrates BMP/Wnt modulation | Best available in vivo system for mechanism | [17823661](https://pubmed.ncbi.nlm.nih.gov/17823661/) |
| In vitro chondrocytes | WISP-3 regulates collagen II, aggrecan, SOD; IGF-1 sensitivity | Mechanistic dissection of cartilage biology | [16480948](https://pubmed.ncbi.nlm.nih.gov/16480948/), [17363178](https://pubmed.ncbi.nlm.nih.gov/17363178/) |

The **lack of a phenotypic mouse model** is the principal limitation for preclinical therapeutic development; patient-derived iPSC-chondrocytes or organoids represent a logical next step but were not found in the reviewed literature.

---

## Mechanistic Model / Interpretation

PPRD is best understood as a **cartilage-autonomous, noninflammatory chondrodysplasia** driven by loss of a single secreted regulator of joint-cartilage homeostasis. The unifying model places *CCN6*/WISP3 at a signaling node that restrains BMP, Wnt, and IGF-1 activity in articular chondrocytes and simultaneously supports matrix synthesis (type II collagen, aggrecan) and antioxidant defense (SOD). Biallelic loss of function removes these brakes, tipping chondrocytes toward hypertrophic terminal differentiation and apoptosis — the same fate normally reserved for growth-plate chondrocytes, now occurring inappropriately in permanent articular cartilage. The result is relentless, symmetric cartilage attrition with secondary osteoarthritis, joint enlargement, and vertebral (platyspondyly) changes, but **without immune-mediated inflammation** — which is why serologies and acute-phase reactants remain normal and why anti-inflammatory/immunosuppressive therapy fails.

This mechanistic picture directly explains the disease's dominant clinical problem — misdiagnosis as JIA — and its therapeutic corollary: only supportive and reconstructive (surgical) management alters outcomes, because the primary lesion is structural cartilage loss, not inflammation. The variable expressivity (severe childhood to mild adult forms) likely reflects residual/hypomorphic protein function tied to specific genotypes (e.g., c.624dupA → later onset), a hypothesis supported by cohort genotype–phenotype correlations.

---

## Evidence Base

| PMID | Contribution | Supports finding |
|---|---|---|
| [37377052](https://pubmed.ncbi.nlm.nih.gov/37377052/) | Egyptian cohort; gene, locus, LOF mechanism, 11 variants | F1, F6 |
| [36622578](https://pubmed.ncbi.nlm.nih.gov/36622578/) | Chinese cohort (105); genotype–phenotype (c.624dupA) | F1 |
| [22987568](https://pubmed.ncbi.nlm.nih.gov/22987568/) | Indian cohort; founder allele c.1010G>A | F1, F6 |
| [34919662](https://pubmed.ncbi.nlm.nih.gov/34919662/) | Turkish cohort; gait 97.7%, disability, founder c.156C>A | F2, F5 |
| [34749805](https://pubmed.ncbi.nlm.nih.gov/34749805/) | Documents JIA misdiagnosis pitfall | F2 |
| [17823661](https://pubmed.ncbi.nlm.nih.gov/17823661/) | Zebrafish BMP/Wnt modulation; mouse null phenotype | F3, F15 |
| [16480948](https://pubmed.ncbi.nlm.nih.gov/16480948/) | WISP-3 as ligand; SOD, collagen II, aggrecan | F3, F9 |
| [17363178](https://pubmed.ncbi.nlm.nih.gov/17363178/) | IGF-1 sensitization hypothesis | F3, F6 |
| [31876842](https://pubmed.ncbi.nlm.nih.gov/31876842/) | THA outcomes: HHS 40→92, SF-36 20→71 | F4 |
| [38862149](https://pubmed.ncbi.nlm.nih.gov/38862149/) | No pharmacotherapy; diagnosis genetic only | F4, F9 |
| [27517291](https://pubmed.ncbi.nlm.nih.gov/27517291/) | CCN modular domain architecture | F6 |
| [40626694](https://pubmed.ncbi.nlm.nih.gov/40626694/) | PPRD among genetic rheumatic mimics | F7 |
| [26183434](https://pubmed.ncbi.nlm.nih.gov/26183434/) | *COL2A1* PPRD-like phenocopy | F7 |
| [30635069](https://pubmed.ncbi.nlm.nih.gov/30635069/) | Spinal canal stenosis requiring surgery | F8 |
| [29246200](https://pubmed.ncbi.nlm.nih.gov/29246200/) | Age of onset 3–8 yr; delayed adult case | F8 |
| [36550675](https://pubmed.ncbi.nlm.nih.gov/36550675/) | Prevalence ~1/million, underdiagnosis | F5 |
| [15877179](https://pubmed.ncbi.nlm.nih.gov/15877179/) | Radiographic diagnostic features | F5 |
| [38958524](https://pubmed.ncbi.nlm.nih.gov/38958524/) | CNV in trans; GS + deep phenotyping | F1 |
| [34674084](https://pubmed.ncbi.nlm.nih.gov/34674084/) | Calcitriol for vitamin D deficiency | F4 |
| [30327864](https://pubmed.ncbi.nlm.nih.gov/30327864/) | Review; >70 variants; mRNA testing for splice variants | F9 |

Evidence source types span **human clinical** cohorts and case series (majority), **model organism** (zebrafish, mouse), **in vitro** chondrocyte studies, and **computational/genomic** variant analyses.

---

## Limitations and Knowledge Gaps

1. **No disease-modifying therapy or drug pipeline.** All treatment is supportive/surgical; no targeted agent, RNA therapy, or gene therapy has been trialed (F9).
2. **No phenotypic mouse model.** *Wisp3*-null mice are asymptomatic, hampering preclinical development; zebrafish and in vitro chondrocytes are the only usable systems (F3, F15).
3. **No validated biomarkers.** No transcriptomic, proteomic, or metabolomic patient biomarker exists for diagnosis, staging, or prognosis (F9).
4. **Prevalence uncertainty.** The ~1/million estimate is unreliable due to systematic misdiagnosis; true prevalence is likely higher (F5).
5. **Incomplete genotype–phenotype maps.** Beyond a few hotspot alleles, determinants of severity/onset are poorly resolved; modifier genes are unidentified.
6. **Mechanistic gaps.** The IGF-1 sensitization model remains a hypothesis; the precise postnatal role of CCN6 in cartilage homeostasis is not fully defined.

---

## Proposed Follow-up Experiments / Actions

1. **Develop patient-derived iPSC-chondrocyte and cartilage-organoid models** to overcome the mouse phenotype gap and enable mechanistic dissection and drug screening.
2. **Test rescue of BMP/Wnt/IGF-1 dysregulation** (e.g., pathway modulators) in zebrafish and iPSC-chondrocyte systems as candidate chondroprotective strategies.
3. **Establish an international PPRD registry** with standardized deep phenotyping and genome sequencing to refine prevalence, natural history, and genotype–phenotype correlations.
4. **Discover circulating biomarkers** — measure CCN6 and cartilage-turnover markers (e.g., CTX-II, COMP) longitudinally to enable early diagnosis and progression monitoring.
5. **Systematize early diagnostic pathways** in pediatric rheumatology (normal inflammatory markers + symmetric noninflammatory polyarthropathy + platyspondyly → reflex *WISP3*/panel testing) to shorten diagnostic delay and prevent inappropriate immunosuppression.
6. **Long-term arthroplasty outcome studies** in young PPRD patients to optimize implant selection, timing, and multi-joint strategies.
7. **Evaluate variant-specific effects** (including the newer c.348C>A, c.676G>C, and CNV alleles) on protein secretion/function to inform prognosis and future precision approaches.

---

*Report compiled from 9 confirmed findings and 36 reviewed publications across a multi-iteration autonomous investigation. Ontology suggestions (HPO, GO, CL, UBERON, NCIT, MONDO) are provided throughout to support knowledge-base curation.*


## Artifacts

- [OpenScientist final report](Progressive_Pseudorheumatoid_Arthropathy_Of_Childhood-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Progressive_Pseudorheumatoid_Arthropathy_Of_Childhood-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 29 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002758` (2 mentions) - the report calls it "Osteoarthritis", "Clinical"; HP calls it **Osteoarthritis**
- `HP:0001387` (2 mentions) - the report calls it "Joint stiffness", "Clinical sign"; HP calls it **Joint stiffness**
- `HP:0000944` (2 mentions) - the report calls it "Platyspondyly", "Radiographic"; HP calls it **Abnormal metaphysis morphology**
- `HP:0000939` (2 mentions) - the report calls it "Osteoporosis", "Laboratory/imaging"; HP calls it **Osteoporosis**
- `HP:0002515` (2 mentions) - the report calls it "Waddling gait", "Clinical sign"; HP calls it **Waddling gait**
- `HP:0004322` (2 mentions) - the report calls it "Short stature", "Physical"; HP calls it **Short stature**
- `HP:0100360` (2 mentions) - the report calls it "Enlarged interphalangeal joints", "Physical"; HP calls it **Upper-limb joint contracture**
- `NCIT:C157866` (2 mentions) - the report calls it "Total Hip Arthroplasty"; NCIT calls it **Gluten Free Diet**
- `NCIT:C51765` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Bilateral Salpingectomy with Oophorectomy**
- `NCIT:C1898` (1 mention) - the report calls it "Calcitriol/Vitamin D"; NCIT calls it **Physical Carcinogens**
- `HP:0002826` (2 mentions) - the report calls it "Spinal canal stenosis"; HP calls it **Halberd-shaped pelvis**
- `HP:0002970` (1 mention) - the report calls it "Physical"; HP calls it **Genu varum**
- `UBERON:0002217` (1 mention) - the report calls it "articular cartilage of joint"; UBERON calls it **synovial joint**
- `UBERON:0003656` (1 mention) - the report calls it "interphalangeal joint"; UBERON calls it **mesopodium bone**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030509` (2 mentions) - the report calls it "BMP signaling pathway", "BMP signaling"; GO calls it **BMP signaling pathway**
- `GO:0016055` (2 mentions) - the report calls it "Wnt signaling pathway", "Wnt signaling"; GO calls it **Wnt signaling pathway**
- `NCIT:C1505` (1 mention) - the report calls it "Calcium supplement"; NCIT calls it **Dietary Supplement**, and lists "Supplement" among its other names
- `CL:0000743` (2 mentions) - the report calls it "articular chondrocyte"; CL calls it **hypertrophic chondrocyte**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002758` - called "Osteoarthritis", "Clinical"
- `HP:0001387` - called "Joint stiffness", "Clinical sign"
- `HP:0000944` - called "Platyspondyly", "Radiographic"
- `HP:0000939` - called "Osteoporosis", "Laboratory/imaging"
- `HP:0002515` - called "Waddling gait", "Clinical sign"
- `HP:0004322` - called "Short stature", "Physical"
- `HP:0100360` - called "Enlarged interphalangeal joints", "Physical"
- `GO:0030509` - called "BMP signaling pathway", "BMP signaling"
- `GO:0016055` - called "Wnt signaling pathway", "Wnt signaling"