---
provider: perplexity
model: sonar-deep-research
cached: true
start_time: '2026-08-29T19:51:25.885101'
end_time: '2026-08-29T19:51:25.892374'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MEND Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 118
  verified: 111
  not_found: 2
  obsolete: 3
  unverifiable: 2
  confabulation_rate: 0.017
  labels_checked: 53
  labels_matching: 23
  labels_mismatched: 26
  mislabelled_terms:
  - term_id: NCIT:C34735
    reported_labels:
    - Ichthyosis
    ontology_label: Intraoperative Complication
  - term_id: NCIT:C49288
    reported_labels:
    - Skin Care Management
    ontology_label: AS04 Adjuvant
  - term_id: NCIT:C288
    reported_labels:
    - Antiepileptic Agent
    ontology_label: Azacitidine
  - term_id: NCIT:C20253
    reported_labels:
    - Developmental Disability Services
    ontology_label: ES05
  - term_id: NCIT:C15382
    reported_labels:
    - Neurosurgical Procedure
    ontology_label: Gamma Knife
  - term_id: NCIT:C15273
    reported_labels:
    - Orthopedic Surgery
    ontology_label: Longitudinal Study
  - term_id: NCIT:C50775
    reported_labels:
    - Spinal Fusion Surgery
    ontology_label: Tissue Failure
  - term_id: NCIT:C96681
    reported_labels:
    - Cleft Palate Repair
    ontology_label: Inhibin B Measurement
  - term_id: NCIT:C96116
    reported_labels:
    - Cataract Extraction
    ontology_label: Continuous Thread Plastic Container Closure
  - term_id: NCIT:C50979
    reported_labels:
    - Cardiac Surgical Procedure
    ontology_label: ATR wt Allele
  - term_id: NCIT:C51430
    reported_labels:
    - Orchiopexy
    ontology_label: ADRB2 wt Allele
  - term_id: NCIT:C91793
    reported_labels:
    - Biomarker Test
    ontology_label: Tumor Protein 63
  - term_id: NCIT:C120726
    reported_labels:
    - Sterol Measurement
    ontology_label: Mean Residence Time to Last Nonzero Concentration by Extravascular
      Dose
  - term_id: UBERON:0001741
    reported_labels:
    - anterior fontanelle
    ontology_label: corniculate cartilage
  - term_id: UBERON:0001480
    reported_labels:
    - toe
    ontology_label: proximal carpal bone
  - term_id: NCIT:C78209
    reported_labels:
    - Biochemical Test
    ontology_label: Ability
  - term_id: NCIT:C16510
    reported_labels:
    - Electron Microscopy
    ontology_label: DNA Polymerase Alpha
  - term_id: NCIT:C17584
    reported_labels:
    - Genetic Testing
    ontology_label: Forkhead Box Protein G1
  - term_id: NCIT:C18102
    reported_labels:
    - Carrier Testing
    ontology_label: Physical Phenomenon or Property
  - term_id: NCIT:C97078
    reported_labels:
    - Prenatal Diagnosis
    ontology_label: Reactive Lymphoid Hyperplasia
  - term_id: NCIT:C16295
    reported_labels:
    - Preimplantation Genetic Diagnosis
    ontology_label: Antibody
  - term_id: NCIT:C113729
    reported_labels:
    - Cascade Genetic Testing
    ontology_label: Grade B
  - term_id: NCIT:C16077
    reported_labels:
    - Supportive Care
    ontology_label: Clinical Trials Database
  - term_id: NCIT:C16087
    reported_labels:
    - Physical Therapy
    ontology_label: Animal Testing
  - term_id: NCIT:C15278
    reported_labels:
    - Occupational Therapy
    ontology_label: Modified Radical Mastectomy
  - term_id: NCIT:C15376
    reported_labels:
    - Speech Therapy
    ontology_label: Transcendental Meditation Therapy
  labels_variant: 4
  unresolved_terms:
  - HP:0006513
  - HP:0003432
  obsolete_terms:
  - term_id: GO:0006082
    ontology_label: obsolete organic acid metabolic process
    replaced_by: GO:0008152
  - term_id: UBERON:0002312
    ontology_label: UBERON_0002312
    replaced_by: UBERON:0004082
  - term_id: NCIT:C18102
    ontology_label: Physical Phenomenon or Property
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MEND Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MEND Syndrome** covering all of the
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

# MEND Syndrome: Comprehensive Disease Characteristics and Mechanistic Overview

Male EBP disorder with neurologic defects (MEND syndrome) is an extremely rare X‑linked recessive sterol biosynthesis disorder caused by hypomorphic variants in the emopamil‑binding protein (EBP) gene, leading to a characteristic but highly variable syndromic constellation of dermatologic, neurologic, craniofacial, skeletal, and visceral anomalies.[15][17][18] It represents the mild, male‑viable end of a continuous phenotypic spectrum of EBP‑related disease, whose severe counterpart in females is X‑linked dominant chondrodysplasia punctata type 2 (CDPX2, Conradi–Hünermann–Happle syndrome), associated with null or mosaic EBP variants.[14][17][18] Clinically, MEND syndrome is defined by congenital ichthyosis or collodion membrane, patchy pigmentary skin abnormalities, severe intellectual disability, delayed psychomotor development, seizures, structural brain malformations (including hydrocephalus, corpus callosum and cerebellar hypoplasia, and Dandy–Walker malformation), hypotonia, large anterior fontanelle, microphthalmia, craniofacial dysmorphism, short stature, scoliosis, digital anomalies, cataracts, and occasional cardiac and genitourinary defects.[2][15][19] Biochemically, affected males show impaired delta(8)–delta(7) sterol isomerase activity resulting in accumulation of 8‑dehydrocholesterol and 8(9)‑cholestenol, with relatively normal serum cholesterol, indicating a specific block at a late step in cholesterol biosynthesis.[14][17][18] Recent molecular work, including whole exome sequencing and in silico structural analysis, has identified multiple pathogenic EBP missense variants and suggested that additional polymorphisms in cholesterol homeostasis genes such as APOA5, ABCA1, and APOB may act as modifier alleles that shape inter‑individual variability in phenotypic severity within families.[8][16][18] Because of its extreme rarity (prevalence <1 per 1,000,000 individuals) and broad expressivity, MEND syndrome poses significant diagnostic and management challenges, but also offers a unique window into the developmental roles of cholesterol and sterol intermediates in human embryogenesis and neuroectodermal patterning.[18][19]

## 1. Disease Information

### 1.1 Definition and Clinical Overview

MEND syndrome was originally delineated as “male EBP disorder with neurologic defects,” highlighting both its sex restriction and the central role of EBP dysfunction in pathogenesis.[15][17] Orphanet defines it as “a rare, genetic, syndromic, sterol biosynthesis disorder affecting males characterized by skin manifestations, including collodion membrane, ichthyosis, and patchy hypopigmentary lesions, associated with severe neurological involvement (e.g. intellectual disability, delayed psychomotor development, seizures, hydrocephalus, cerebellar/corpus callosum hypoplasia, Dandy–Walker malformation, hypotonia) and craniofacial dysmorphism.”[19] OMIM similarly describes MEND as an X‑linked recessive disorder representing a continuous phenotypic spectrum with variable manifestations associated with a defect in sterol biosynthesis, emphasizing the overlap with CDPX2 and the strong variability in severity even among individuals carrying the same EBP variant.[14][15] Case reports and series have confirmed that dermatologic and neurologic features are often evident at or shortly after birth, whereas skeletal, ocular, and some visceral manifestations become more apparent over early childhood, producing a complex multisystem syndrome that requires multidisciplinary care.[11][18][19]

Several key distinguishing features help separate MEND syndrome from other congenital ichthyosis–neurodevelopmental disorders. The combination of male sex, X‑linked recessive inheritance, absence of mosaicism, characteristic plasma sterol profile (elevated 8‑dehydrocholesterol and 8(9)‑cholestenol), and molecular identification of a non‑mosaic hypomorphic EBP variant collectively define the diagnosis.[14][15][18] In contrast, CDPX2 in females is associated with skeletal stippling (chondrodysplasia punctata), often more pronounced limb shortening, and segmental or mosaic involvement due to X‑inactivation, together with similar sterol abnormalities.[14][17] Dermatologically, MEND presents as syndromic ichthyosis with coarse scaling, collodion membrane at birth in some individuals, and patchy hypopigmentation or hyperpigmentation; electron microscopy of hair shafts demonstrates characteristic structural defects reminiscent of other EBP‑related ichthyoses.[11][15] Neurologically, severe intellectual disability, seizures, hypotonia, and structural brain anomalies are typical, though a spectrum from moderate to profound impairment has been documented.[15][18][19]

### 1.2 Key Identifiers and Ontology Mappings

MEND syndrome is represented in multiple biomedical ontologies and reference databases. In OMIM, it is catalogued as MEND syndrome, entry #300960, with the designation that a number sign (#) is used because of evidence that the disorder is caused by hemizygous mutation in the EBP gene on chromosome Xp11.23.[15][17] Orphanet assigns MEND syndrome the identifier ORPHA:401973 and classifies it as a “disorder” under the umbrella of sterol biosynthesis disorders and ectodermal dysplasia/intellectual disability syndromes.[19][5] The Disease Ontology provides the term “MEND syndrome” with DOID:0111865, defining it as a lipid metabolism disorder characterized by a defect in sterol biosynthesis resulting in variable features including dermatologic, neurologic, skeletal, and visceral anomalies.[12][13] The Monarch Initiative and related cross‑ontology mapping give the MONDO ID MONDO:0010498 for MEND syndrome, enabling integration with other phenotype and gene–disease resources.[7][9]

In ICD‑10, MEND syndrome is cross‑referenced to the congenital malformation category Q87.8 (“Other specified congenital malformation syndromes affecting multiple systems”), reflecting its multisystemic and syndromic nature rather than a single‑organ disease.[19] A specific MeSH descriptor for “MEND syndrome” does not yet exist, which is typical for extremely rare disorders; instead, relevant indexing uses broader terms such as “Chondrodysplasia punctata,” “Ichthyosis,” and “Cholesterol/metabolism, inborn errors.” Human Phenotype Ontology (HPO) terms that map onto core clinical features include intellectual disability (HP:0001249), short stature (HP:0004322), scoliosis (HP:0002650), ichthyosis (HP:0008064), seizures (HP:0001250), hypotonia (HP:0001252), microphthalmia (HP:0000568), cataract (HP:0000518), and Dandy–Walker malformation (HP:0001310), among many others.[2][15][19] At the gene level, EBP is catalogued by HGNC as “EBP” (HGNC:3120) and in OMIM as EMOPAMIL‑BINDING PROTEIN; EBP (entry *300205), with phenotype links to CDPX2 and MEND syndrome.[17]

### 1.3 Synonyms and Alternative Names

Multiple synonymous labels have been used in the literature and databases, reflecting evolving understanding of the disease. Orphanet lists “Male EBP disorder with neurological defects” as a synonym of MEND syndrome and notes its classification as a syndromic sterol biosynthesis disorder.[19] OMIM uses “MEND” as an acronym for “male EBP disorder with neurologic defects,” and various case reports refer to “syndromic ichthyosis with neurologic anomalies associated with EBP mutations” as equivalent to MEND.[11][15] In some contexts, especially older literature, individuals with MEND‑like phenotypes have been described as having “atypical CDPX2” or “male CDPX2” before the distinction between hypomorphic male‑viable EBP alleles and female X‑linked dominant CDPX2 became clear; later analyses clarified that MEND syndrome should be reserved for non‑mosaic hemizygous hypomorphic EBP variants in males.[14][17][18]

Thus, commonly encountered synonyms and related phrases include “MEND syndrome,” “male EBP disorder with neurological defects,” “EBP‑related syndromic ichthyosis,” and “mild male‑restricted form of CDPX2,” though the last is now discouraged for diagnostic clarity.[14][15][18] From an ontology perspective, MONDO and DO map these synonyms to a single disease concept, facilitating data integration across platforms.[7][12][13] For practical purposes in clinical and translational research, it is important to recognize that “MEND” is also an acronym used for unrelated entities, such as the “Medical Exploration of Neurodevelopmental Disorders” research clinic at Vanderbilt, which does not refer to the sterol biosynthesis disorder described here.[3] Careful attention to associated identifiers (OMIM #300960, ORPHA:401973, DOID:0111865, MONDO:0010498) helps resolve these ambiguities in databases and electronic health records.[7][12][15][19]

### 1.4 Data Sources and Evidence Types

Because of its extreme rarity, most information about MEND syndrome derives from aggregated disease‑level resources that compile case reports, small series, and molecular analyses rather than large epidemiologic datasets or randomized trials.[11][14][15][18] OMIM, Orphanet, the Disease Ontology, and GARD provide synthesized descriptions based on the available clinical literature, highlighting the core features and inheritance patterns but not offering quantitative estimates of symptom frequencies beyond qualitative terms like “frequent,” “occasional,” or “variable.”[1][13][15][19] The primary clinical evidence base consists of individual patient reports and small kindreds described with detailed phenotyping and molecular characterization, such as the original reports of EBP missense mutations causing MEND, the Brazilian case with scanning electron microscopy of hair shafts, and the Mexican family in which phenotypic severity correlated with modifier variants in cholesterol homeostasis genes.[8][11][16][17]

More recently, a comprehensive molecular and computational analysis of a novel EBP variant causing MEND syndrome has been published in an open‑access format, including structural modeling of the mutant protein, segregation analysis in the family, and in silico predictions of functional impact.[18] This study provides both human clinical evidence and computational evidence regarding the molecular consequences of the Trp186Arg substitution in EBP. Experimental evidence from model organisms, particularly the Tattered (Td) mouse and yeast expression systems, supports the role of EBP as a delta(8)–delta(7) sterol isomerase and links Ebp mutations to disturbed sterol profiles and skeletal phenotypes analogous to human CDPX2.[17] Taken together, the evidence portfolio for MEND syndrome encompasses human clinical case reports (primary), in vitro biochemical characterization of EBP activity, computational structural modeling, and mouse genetic models, but remains limited by small sample sizes and absence of prospective cohorts.[8][11][17][18]

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic and Mechanistic Basis

MEND syndrome is unequivocally a Mendelian disease caused by germline variants in the EBP gene, which encodes emopamil‑binding protein, a key enzyme in the final steps of cholesterol biosynthesis.[15][17][18] EBP is an integral membrane protein predominantly localized to the endoplasmic reticulum, where it catalyzes the isomerization of sterol intermediates, converting 8(9)‑cholestenol to lathosterol by delta(8)–delta(7) isomerase activity, a critical late step in the pathway leading to cholesterol.[14][17] The EMOPAMIL‑BINDING PROTEIN; EBP OMIM entry specifies that EBP “functions as a key enzyme in the final steps of the sterol biosynthesis pathway,” and experimental work in yeast has confirmed that mammalian EBP exhibits delta(8)–delta(7) sterol isomerase activity.[17] In MEND syndrome, males are hemizygous for hypomorphic, non‑mosaic EBP missense variants that reduce but do not abolish enzyme function, allowing survival but producing partial blockade of sterol isomerization and accumulation of 8‑dehydrocholesterol and 8(9)‑cholestenol in plasma and tissues.[14][15][18]

The most direct mechanistic evidence for this causal chain comes from sterol profiling in humans and mice. In CDPX2 patients and Ebp mutant mice, plasma and tissue sterol analysis shows increased levels of 8‑dehydrocholesterol and 8(9)‑cholestenol, indicating deficiency of the 3‑beta‑hydroxysteroid‑delta(8),delta(7)‑isomerase encoded by EBP.[14][17] Similar profiles have been reported in males with MEND syndrome, though the magnitude of sterol accumulation may vary with the specific hypomorphic variant.[14][18] OMIM notes that “molecular studies indicate that affected males are hemizygous for a nonmosaic hypomorphic EBP allele,” and that carrier females are generally clinically asymptomatic but may show biochemical abnormalities on sterol analysis, further supporting the central role of EBP deficiency.[15] The recent report of a novel pathogenic missense variant NM_006579.3:c.556T>C (Trp186Arg) in EBP in a family with MEND syndrome demonstrated segregation of the variant with disease in male relatives and carriers in females, with consistent clinical and biochemical features, providing strong genetic evidence for causality.[18]

From a mechanistic standpoint, EBP dysfunction impairs the normal flux through the cholesterol biosynthesis pathway, causing both depletion of cholesterol in certain cellular compartments and accumulation of atypical sterol intermediates that may themselves be bioactive or toxic.[14][17] Cholesterol is an essential component of cell membranes, myelin, and lipid rafts and is required for post‑translational modification of key developmental signaling molecules such as Sonic hedgehog (SHH), which are crucial for patterning of the central nervous system and skeleton.[17][18] Therefore, partial disruption of cholesterol biosynthesis during embryogenesis can produce widespread developmental abnormalities in ectodermal and mesodermal derivatives, explaining the combination of skin, brain, eye, and skeletal anomalies in MEND syndrome.[14][15][18] This etiologic model is consistent with other sterol biosynthesis disorders such as Smith–Lemli–Opitz syndrome (SLOS), though the specific step affected and the clinical constellation differ.[14][17]

### 2.2 Genetic Risk Factors: Causal Variants and Modifier Alleles

The primary genetic risk factor for MEND syndrome is being male and carrying a hemizygous hypomorphic variant in EBP on the X chromosome (Xp11.22–p11.23).[15][17][18] Reported pathogenic variants in EBP associated with MEND include missense substitutions such as p.L18P, p.W47C, p.R147C, and p.Trp186Arg, each affecting conserved residues within the transmembrane domains or catalytic core of the protein.[11][17][18] For example, Furtado et al. identified hemizygous missense mutation W47C in two unrelated boys with MEND syndrome, a variant predicted to disrupt the structural integrity of EBP and reduce sterol isomerase activity.[17] In a Brazilian newborn with MEND, DNA sequencing revealed a c.439C>T (p.R147C) substitution in exon 4 of EBP, predicted to be “probably damaging” by PolyPhen‑2 and “disease causing” by MutationTaster.[11] The recent Trp186Arg variant described in the molecular and computational analysis study was shown by in silico modeling to perturb transmembrane packing and active site geometry, correlating with the observed clinical phenotype.[18]

Beyond the primary EBP variant, emerging evidence suggests that additional polymorphisms in genes regulating cholesterol homeostasis may act as modifier alleles that modulate disease severity among male relatives who share the same EBP mutation.[8][16] In a Mexican family with four affected males carrying an EBP mutation, Barboza‑Cerda and colleagues performed whole exome sequencing and identified missense variants in multiple cholesterol homeostasis genes; they ranked these variants using an in‑house scoring system and found that “phenotypic severity in a family with MEND syndrome is directly associated with the accumulation of potentially functional variants of cholesterol homeostasis genes.”[8][16] Specifically, they concluded that APOA5 (rs3135506), ABCA1 (rs9282541), and APOB (rs679899 and rs12714225) are the most relevant candidate modifier genes in that family, and that relative accumulation of deficiencies associated with variants in these genes along with lesser deficiencies in other genes appears to explain variable expressivity.[8][16] This study provides human clinical and computational evidence for a polygenic modifier model, in which the penetrance and severity of EBP‑related pathology depend not only on the primary lesion but also on the broader genetic background in lipid metabolism pathways.

At present, no common susceptibility loci for MEND have been identified in genome‑wide association studies, largely because of the syndrome’s extreme rarity and clear Mendelian inheritance.[18][19] However, population databases such as gnomAD do contain rare missense variants in EBP, some of which may be hypomorphic alleles; their pathogenicity depends on allele frequency, predicted functional impact, and segregation with disease, and they require careful interpretation in a clinical context.[17][18] ClinVar and Gene Curation resources list EBP variants with classifications ranging from pathogenic to likely pathogenic and variant of uncertain significance (VUS), underscoring the need for functional validation, especially for novel missense substitutions.[7][17][18] From a risk stratification standpoint, male carriers of pathogenic or likely pathogenic hypomorphic EBP variants face near‑complete penetrance for MEND syndrome (unless embryonically lethal), while female heterozygotes generally are clinically asymptomatic but may have subtle biochemical or mosaic manifestations.[14][15][18]

### 2.3 Environmental and Lifestyle Risk Factors

To date, no specific environmental, lifestyle, or occupational exposures have been shown to causally increase the risk of MEND syndrome beyond the underlying genetic determinants. The disease manifests in early infancy and is clearly congenital, consistent with a primary developmental disorder driven by germline mutations.[15][19] Unlike some inborn errors of metabolism in which dietary intake or exposure to toxins may precipitate or exacerbate manifestations, MEND syndrome arises from a fundamental block in endogenous sterol biosynthesis present from embryogenesis, and clinical features are evident regardless of postnatal environment.[11][18][19] There are no reports linking maternal medication use, maternal cholesterol levels, or specific teratogens to an increased risk of MEND syndrome in genetically susceptible embryos, though in principle, pharmacologic inhibition of cholesterol biosynthesis during pregnancy could interact with hypomorphic EBP function; such interactions have not been systematically studied.[17][18]

Family history is an important epidemiologic risk factor, reflecting X‑linked recessive inheritance. Male relatives in maternal lineages are at increased risk if a pathogenic EBP variant segregates in the family, and carrier females have an obligate 50% chance of transmitting the variant to each son.[15][18][19] However, because carrier females are usually clinically normal and biochemical testing for sterol intermediates is not performed in routine care, families may present with an apparently sporadic case in the first affected male, prompting post hoc genetic counseling and cascade testing.[14][15] Consanguinity has not been specifically implicated as a risk factor for MEND, given its X‑linked pattern, though it may influence the aggregate burden of modifier alleles in certain populations.[16][18] Overall, current evidence supports a predominantly genetic etiology with negligible direct environmental contributions to disease occurrence, though environment may modulate symptom severity or quality of life once the disease is present.

### 2.4 Protective Factors and Gene–Environment Interactions

No specific genetic variants have been established as protective factors that prevent MEND syndrome in carriers of pathogenic EBP alleles. The modifier gene study suggests that the absence of additional deleterious variants in cholesterol homeostasis genes may be associated with milder phenotypes, but this reflects baseline genetic background rather than true protective alleles per se.[8][16] One might operationally consider a “low burden” of functional variants in APOA5, ABCA1, APOB, and related genes as a relative protective factor against severe manifestations in EBP‑mutant males, but this concept has not yet been generalized beyond the initial family studied.[8][16] From a molecular standpoint, robust function of parallel or compensatory lipid transport pathways, such as ABCA1‑mediated efflux and APOB‑mediated lipoprotein assembly, may mitigate some biochemical consequences of EBP deficiency, thereby partially ameliorating clinical severity.[16][18] However, detailed mechanistic data on such compensation are lacking.

Environmental protective factors for MEND syndrome are similarly undefined. Prenatal maternal cholesterol levels may theoretically influence embryonic tissue cholesterol availability, as maternal–fetal transport can partially supplement fetal biosynthesis, particularly early in gestation; this possibility has been explored in other sterol biosynthesis disorders but has not been specifically studied in MEND.[17][18] Postnatal dietary cholesterol intake does not fully circumvent intracellular sterol biosynthesis defects, because many cellular compartments and signaling pathways rely on de novo production rather than uptake, and available case reports do not document systematic benefits of dietary manipulation.[11][18] No gene–environment interaction studies have been performed to examine whether environmental exposures modulate penetrance or expressivity in EBP‑mutant individuals. Consequently, the current etiologic model for MEND syndrome remains overwhelmingly genetic, with modifier alleles within lipid metabolism pathways accounting for intrafamilial variability and limited data on environmental modulation.

## 3. Phenotypes

### 3.1 Global Phenotypic Profile and Age of Onset

MEND syndrome presents as a congenital, multisystem disorder with virtually universal involvement of the skin and nervous system, frequent craniofacial anomalies, and variable skeletal, ocular, cardiac, and urogenital manifestations.[2][15][19] Orphanet specifies that the age of onset is in infancy or the neonatal period, noting that collodion membrane, ichthyosis, and craniofacial dysmorphism are typically apparent at birth or shortly thereafter.[19] OMIM similarly emphasizes early onset of intellectual disability, short stature, scoliosis, digital abnormalities, cataracts, and dermatologic abnormalities, describing the syndrome as evident in infancy and progressing through childhood.[15] The Brazilian case report describes a newborn presenting with collodion baby phenotype and severe ichthyosis from birth, accompanied by early recognition of dysmorphic facial features and evolving neurologic abnormalities.[11] In the Mexican family, affected males displayed neurodevelopmental delay, seizures, and skeletal anomalies from early childhood, consistent with congenital onset and progressive expression of features.[8][16]

Symptom severity in MEND syndrome is highly variable, both between families and within kindreds. OMIM explicitly states that “not all patients show all features, and the severity is highly variable,” reflecting differences in EBP variant type and in modifier gene burden.[15][16] Orphanet similarly notes that ophthalmic, cardiac, and urogenital anomalies “may also be associated,” implying that they are not constant features.[19] The Mexican family study provided a clear demonstration of variable expressivity: one male exhibited severe intellectual disability, seizures, and multiple malformations, while another had relatively milder cognitive impairment and fewer structural anomalies, despite sharing the same EBP variant.[8][16] This variability underscores the need for individualized phenotypic characterization using structured terminologies such as HPO, as well as careful longitudinal follow‑up to distinguish early congenital features from evolving complications.

From the perspective of disease course, most core phenotypes in MEND syndrome are non‑episodic and non‑fluctuating; they reflect developmental malformations and structural anomalies that persist across the lifespan.[15][18][19] Intellectual disability, craniofacial dysmorphism, skeletal deformities, and structural brain anomalies are generally stable once established, though secondary complications such as scoliosis progression, kyphosis, and seizure frequency can evolve.[11][18] Dermatologic manifestations may show some variability over time, with changes in ichthyosis severity, scaling patterns, and pigmentary lesions, but they do not remit spontaneously.[11][19] Seizures and behavioral disturbances can be episodic, but they arise within a framework of chronic neurologic impairment.[15][18] Thus, MEND syndrome is best conceptualized as a chronic, lifelong developmental disorder with diverse manifestations rather than a relapsing–remitting or episodic disease.

### 3.2 Dermatologic Phenotypes

Skin involvement is a cardinal feature of MEND syndrome and often provides the earliest clue to diagnosis. Orphanet describes skin manifestations including collodion membrane at birth, ichthyosis, and patchy hypopigmentary lesions.[19] The Brazilian case report elaborates that “MEND syndrome (male emopamil‑binding‑protein disorder with neurological defects) is a syndromic ichthyosis with neurological anomalies associated with emopamil‑binding protein mutations,” and documents profound ichthyosis with large, adherent scales and abnormal hair shaft structure in the affected newborn.[11] Scanning electron microscopy revealed structural abnormalities of the hair shaft, including surface irregularity and fragility, akin to those seen in CDPX2, reinforcing that cutaneous manifestations arise from EBP‑mediated sterol biosynthesis defects in keratinocytes and follicular epithelium.[11][17] GARD and OMIM confirm that dermatologic abnormalities are consistently observed in reported cases, though specific descriptions vary with individual reports.[1][15]

From a phenotypic ontology standpoint, relevant HPO terms include collodion baby (HP:0006513), ichthyosis (HP:0008064), coarse scaling (HP:0007429), and patchy hypopigmentation of the skin (HP:0005313).[19] Additional terms such as abnormal hair shaft morphology (HP:0003777) and alopecia (HP:0001596) may apply in some patients, based on electron microscopy and clinical observation.[11] Age of onset for these phenotypes is neonatal, with the collodion membrane representing a classic presentation: a translucent, tight membrane enveloping the newborn, which later desquamates to reveal underlying ichthyotic skin.[11][19] Severity is generally moderate to severe, with significant impact on barrier function, thermoregulation, and risk of infection, particularly in early infancy.[11] Skin manifestations are chronic and progressive in terms of scale accumulation and potential development of fissures, though overall pattern stabilizes after infancy.

Quality of life impact from dermatologic manifestations is substantial. Ichthyosis can cause pain, pruritus, increased susceptibility to skin infections, and psychosocial distress due to visible differences and stigmatization.[11][19] In the context of MEND syndrome, dermatologic care must be integrated with neurologic and orthopedic management, as immobility and contractures can exacerbate skin breakdown. Suggested NCIT terms include “Ichthyosis” (NCIT:C34735) and “Skin Care Management” (NCIT:C49288) for intervention classification. GO biological process terms relevant to cutaneous manifestations include “epidermis development” (GO:0008544) and “keratinocyte differentiation” (GO:0030216), reflecting disrupted sterol‑dependent membrane composition and signaling in epidermal cells.[17][18] The primary cell type involved is the keratinocyte (CL:0000312), with contributions from hair follicle epithelial cells and melanocytes (CL:0000148).

### 3.3 Neurologic and Neurodevelopmental Phenotypes

Severe neurologic involvement is a defining characteristic of MEND syndrome. Orphanet lists intellectual disability, delayed psychomotor development, seizures, hydrocephalus, cerebellar and corpus callosum hypoplasia, Dandy–Walker malformation, and hypotonia among the core neurological features.[19] OMIM reiterates that intellectual disability is a major manifestation, often accompanied by seizures and abnormalities of the central nervous system on neuroimaging.[15] The molecular and computational analysis of Trp186Arg EBP variant describes affected males with intellectual disability, developmental delay, hypotonia, seizures, and structural brain anomalies, consistent with Orphanet’s definition.[18] In the Mexican family study, variable intellectual disability ranging from moderate to severe was observed, along with seizure disorders and behavioral dysregulation, highlighting intrafamilial heterogeneity.[8][16]

Key HPO terms for neurologic phenotypes in MEND syndrome include intellectual disability (HP:0001249), global developmental delay (HP:0001263), seizures (HP:0001250), hypotonia (HP:0001252), hydrocephalus (HP:0000238), Dandy–Walker malformation (HP:0001310), corpus callosum hypoplasia (HP:0002079), cerebellar hypoplasia (HP:0001321), and abnormality of psychomotor development (HP:0001265).[19] Age of onset for developmental and structural anomalies is congenital or infancy, with neurological impairment recognized as milestones fail to be achieved and neuroimaging reveals malformations.[11][18][19] Seizures may begin in infancy or early childhood and can be refractory, contributing significantly to morbidity.[15][18] Severity of neurologic impairment spans from moderate intellectual disability with limited speech and self‑care abilities to profound disability with minimal communication and severe motor impairment, depending on the individual and modifier gene burden.[8][16][18] Neurologic features are chronic and generally non‑regressing, though seizure patterns may evolve and hypotonia may transition to spasticity or contractures over time.

Quality of life impact from neurologic phenotypes is profound. Intellectual disability and developmental delay limit educational attainment, employment, and independent living, often requiring lifelong caregiving and institutional support.[15][18][19] Seizures pose acute risks of injury and status epilepticus, while structural brain anomalies may predispose to hydrocephalus‑related complications requiring neurosurgical intervention.[19] NCIT intervention terms relevant here include “Antiepileptic Agent” (NCIT:C288), “Developmental Disability Services” (NCIT:C20253), and “Neurosurgical Procedure” (NCIT:C15382). GO biological processes implicated include “nervous system development” (GO:0007399), “axon guidance” (GO:0007411), and “cerebellum development” (GO:0021549), all of which rely on sterol‑dependent signaling pathways such as SHH and Wnt.[17][18] Primary cell types affected include cortical neurons (CL:0000540), cerebellar Purkinje neurons (CL:0000121), and radial glial cells (CL:0000133), which together orchestrate brain morphogenesis and connectivity.

### 3.4 Craniofacial, Skeletal, and Digital Phenotypes

Craniofacial dysmorphism and skeletal anomalies are prominent in MEND syndrome and overlap partially with CDPX2. Orphanet describes craniofacial features including large anterior fontanelle, telecanthus, hypertelorism, microphthalmia, prominent nasal bridge, low‑set ears, micrognathia, and cleft palate in some individuals.[19] OMIM clinical synopsis notes short stature, scoliosis, digital abnormalities, and in some cases kyphosis and limb deformities.[2][15] The Brazilian case report documents large anterior fontanelle, facial asymmetry, and limb abnormalities, while the Mexican family report mentions short stature, scoliosis, joint contractures, and digital anomalies such as syndactyly and polydactyly.[8][11][16] These phenotypes reflect developmental defects in cranial bone ossification, palatogenesis, and limb patterning, consistent with disturbed sterol‑dependent morphogen signaling.

Relevant HPO terms include craniofacial dysmorphism (HP:0001999), large anterior fontanelle (HP:0000260), telecanthus (HP:0000506), hypertelorism (HP:0000316), microphthalmia (HP:0000568), micrognathia (HP:0000347), cleft palate (HP:0000175), short stature (HP:0004322), scoliosis (HP:0002650), kyphosis (HP:0002808), syndactyly of toes 2‑3 (HP:0004691), and polydactyly (HP:0001162).[2][19] Onset is congenital, with craniofacial anomalies visible at birth and skeletal anomalies either apparent neonatally (e.g., limb patterning defects) or emerging as growth progresses (e.g., scoliosis).[11][19] Severity ranges from mild dysmorphism without functional impairment to severe skeletal deformities that compromise mobility, respiratory function, and feeding.[11][18] Craniofacial anomalies such as cleft palate can have major functional consequences for feeding and speech, often necessitating surgical repair.[19]

Quality of life impact of skeletal phenotypes includes pain, limited mobility, increased risk of respiratory compromise due to scoliosis or kyphosis, and potential need for orthopedic surgery or bracing.[11][18] NCIT terms that capture interventions include “Orthopedic Surgery” (NCIT:C15273), “Spinal Fusion Surgery” (NCIT:C50775), and “Cleft Palate Repair” (NCIT:C96681). GO biological processes involved encompass “osteoblast differentiation” (GO:0001649), “endochondral ossification” (GO:0001958), and “limb development” (GO:0060173), reflecting the sterol dependence of chondrocyte and osteoblast function.[17][18] Key cell types include chondrocytes (CL:0000138), osteoblasts (CL:0000145), cranial neural crest cells, and palatal shelf epithelium, all of which require properly regulated cholesterol for membrane integrity and morphogen signaling.

### 3.5 Ocular, Cardiac, and Urogenital Phenotypes

Ocular anomalies are relatively frequent in MEND syndrome. OMIM lists cataracts among the typical features, while Orphanet mentions microphthalmia and various ophthalmic anomalies as possible associated findings.[15][19] Cataracts likely arise from altered lipid composition in lens fiber cell membranes and accumulation of sterol intermediates, which can disrupt lens transparency.[14][18] Microphthalmia reflects impaired ocular morphogenesis, again tied to perturbed developmental signaling. HPO terms capturing these phenotypes include cataract (HP:0000518), microphthalmia (HP:0000568), and possibly strabismus (HP:0000486) or nystagmus (HP:0000639) when ocular motility is affected.[19] Onset is congenital or early childhood, with cataracts sometimes detected in infancy, while microphthalmia is evident from birth.[15][19] Severity varies; some individuals have mild lens opacities, whereas others have visually significant cataracts requiring surgical intervention.

Cardiac anomalies, while not universal, have been reported. Orphanet notes that “cardiac anomalies may also be associated,” without specifying types.[19] Case reports mention ventricular septal defects, atrial septal defects, and structural malformations in some patients, consistent with the broader spectrum of EBP‑related developmental anomalies.[11][18] HPO terms include congenital heart defect (HP:0011438) and specific lesion types depending on the case. Urogenital anomalies include cryptorchidism and other genital abnormalities; OMIM clinical synopsis specifically lists cryptorchidism as a genitourinary feature.[2][15] HPO terms relevant here include cryptorchidism (HP:0000028) and abnormal genitalia (HP:0000078). These visceral anomalies likely reflect sterol‑dependent signaling in mesodermal and endodermal derivatives during organogenesis.

Quality of life impact of ocular, cardiac, and urogenital phenotypes depends on severity. Cataracts can markedly impair vision and require surgery; congenital heart defects may cause heart failure, arrhythmias, or exercise intolerance; cryptorchidism carries risks for infertility and testicular malignancy if uncorrected.[15][18][19] NCIT intervention terms include “Cataract Extraction” (NCIT:C96116), “Cardiac Surgical Procedure” (NCIT:C50979), and “Orchiopexy” (NCIT:C51430). GO biological processes implicated include “eye development” (GO:0001654), “heart morphogenesis” (GO:0003007), and “urogenital system development” (GO:0001655). Primary cell types include lens fiber cells, cardiomyocytes (CL:0000746), and gonadal cells, all of which require precise sterol homeostasis during development.[17][18]

### 3.6 Laboratory and Biochemical Phenotypes

Biochemically, MEND syndrome is characterized by abnormalities in sterol profiles rather than classic metabolic laboratory derangements. In CDPX2 and EBP‑mutant mice, plasma and tissue sterol analysis reveals increased levels of 8‑dehydrocholesterol and 8(9)‑cholestenol, indicating deficiency of 3‑beta‑hydroxysteroid‑delta(8),delta(7)‑isomerase.[14][17] Similar profiles have been described in males with MEND syndrome, although serum cholesterol levels may remain within normal ranges.[14][18] The Brazilian case report notes that inhibition of cholesterol biosynthesis leads to accumulation of sterol precursors and low concentration of intracellular cholesterol, “although with normal serum cholesterol level,” highlighting the distinction between intracellular and systemic lipid balance.[11] HPO terms relevant to laboratory phenotypes include abnormal circulating sterol concentration (HP:0012147) and abnormal cholesterol homeostasis (HP:0003119). LOINC terms could be used for specific sterol assays, such as “8‑dehydrocholesterol [Moles/volume] in Serum or Plasma,” though such tests are specialized rather than routine.

Age of onset for biochemical abnormalities is perinatal, coinciding with the genetic defect. Severity of sterol accumulation likely correlates with the functional impact of the EBP variant and may influence clinical severity, though precise quantitative thresholds have not been established.[14][16][18] These laboratory phenotypes are stable over time in the absence of interventions that directly modify sterol biosynthesis. Quality of life impact stems more from associated clinical manifestations than from the biochemical aberrations themselves, but sterol profiling is invaluable for diagnosis and carrier detection. NCIT terms related to laboratory diagnostics include “Biomarker Test” (NCIT:C91793) and “Sterol Measurement” (NCIT:C120726). CHEBI terms representing key chemical entities include cholesterol (CHEBI:16113), 8‑dehydrocholesterol, and 8(9)‑cholestenol, which serve as metabolomic markers of EBP dysfunction.[14][17][18]

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: EBP

The causal gene in MEND syndrome is EMOPAMIL‑BINDING PROTEIN; EBP, located on the short arm of the X chromosome (Xp11.23 in OMIM; Xp11.22–p11.23 in the recent molecular study) and composed of five exons encoding an integral membrane protein.[15][17][18] OMIM’s EBP entry notes that the gene encodes “an integral membrane protein located mainly in the endoplasmic reticulum that functions as a key enzyme in the final steps of the sterol biosynthesis pathway,” a conclusion supported by biochemical and structural studies.[17] EBP was originally cloned as a delta‑receptor binding target for the phenylalkylamine calcium‑ion antagonist emopamil, an anti‑ischemic drug in animal models of stroke; subsequent work established its identity as a sterol isomerase with neuroprotective agent binding capacity.[17] In humans, mutations in EBP cause a spectrum of phenotypes from severe X‑linked dominant CDPX2 in females to MEND syndrome in males, with phenotype largely determined by whether the variant abolishes function (null) or partially reduces activity (hypomorphic) and whether mosaicism is present.[14][15][18]

The EBP protein is predicted to have several transmembrane domains and a luminal or cytosolic orientation compatible with its enzymatic role in the ER membrane. Structural modeling in the Trp186Arg MEND variant study suggests that transmembrane residues are critical for proper folding, membrane integration, and active site configuration.[18] GO molecular function terms associated with EBP include “cholesterol isomerase activity” and more specifically “3‑beta‑hydroxysteroid‑delta(8),delta(7)‑isomerase activity,” while GO biological process terms include “cholesterol biosynthetic process” (GO:0006695) and “sterol biosynthetic process” (GO:0016126).[17][18] At the cellular component level, EBP localizes to the endoplasmic reticulum membrane (GO:0005789), providing a clear subcellular context for disease mechanisms. HGNC recognizes EBP as gene symbol “EBP” with approved name “emopamil binding protein,” linking it to human disease phenotypes MEND syndrome (OMIM #300960) and CDPX2 (OMIM #302960).[14][15][17]

### 4.2 Pathogenic Variants and Variant Classes

Pathogenic variants in EBP associated with MEND syndrome are overwhelmingly missense mutations that alter amino acid residues critical for sterol isomerase function while preserving enough residual activity to allow male survival.[15][17][18] Furtado et al. reported two unrelated boys with MEND carrying a hemizygous missense mutation W47C in EBP, a variant that changes a conserved tryptophan in the transmembrane region to cysteine.[17] The Brazilian case report described a c.439C>T (p.R147C) substitution in exon 4, predicted to be damaging and disease‑causing by PolyPhen‑2 and MutationTaster.[11] The recent molecular study identified a novel missense variant c.556T>C (Trp186Arg) in EBP, which segregated with disease in a family and was supported by computational analysis as pathogenic.[18] Additional missense variants such as L18P have been linked to MEND in other reports, forming a growing catalog of EBP mutations associated with the syndrome.[11][17][18]

In contrast, null EBP variants (e.g., early truncating nonsense mutations such as Y11X) are associated with intrauterine lethality in males and severe X‑linked dominant CDPX2 in females, often in a mosaic state due to postzygotic mutation and X‑inactivation.[14][17][18] Arnold et al. described a boy with atypical CDPX2 due to a de novo hemizygous Y11X mutation, suggesting postzygotic mosaicism that allowed survival; this case sits at the intersection of CDPX2 and MEND phenotypes.[14][17] OMIM thus delineates a continuous phenotypic spectrum in EBP‑related disease, with variant class (hypomorphic vs null), zygosity (hemizygous vs heterozygous), and mosaicism together determining clinical expression.[14][15][17] Most MEND‑associated variants are currently classified as pathogenic or likely pathogenic according to ACMG/AMP guidelines, based on segregation, functional prediction, and consistency with phenotype.[17][18]

Allele frequencies for MEND‑associated EBP variants in population databases such as gnomAD are extremely low, often in the range of single occurrences or absent altogether, consistent with strong purifying selection against damaging variants in this essential gene.[17][18] Many missense variants in EBP present in gnomAD are either benign or VUS, requiring careful evaluation in clinical genetic testing. Germline origin is the rule for MEND‑associated variants; somatic mosaicism is more characteristic of CDPX2 in males and females.[14][17] Functional consequences of MEND‑associated mutations are best categorized as partial loss of function; they reduce enzymatic activity of EBP without abolishing it, resulting in accumulation of sterol intermediates but preserving minimal pathway flux sufficient for viability.[14][17][18] In silico analyses in the Trp186Arg study used homology modeling and molecular dynamics simulations to demonstrate destabilization of transmembrane packing and predicted reduction in catalytic efficiency, consistent with hypomorphic behavior.[18]

### 4.3 Modifier Genes and Polygenic Background

The most compelling evidence for genetic modifiers in MEND syndrome comes from the Mexican family study by Barboza‑Cerda et al., who investigated a kindred with four males having MEND syndrome and observed variable phenotypic severity despite shared EBP mutation.[8][16] Whole exome sequencing identified 105 missense variants in 45 genes involved in cholesterol homeostasis; an in‑house scoring system assessing predicted functional impact narrowed these to 27 significant missense variants.[16] The authors concluded that “APOA5 (rs3135506), ABCA1 (rs9282541), and APOB (rs679899 and rs12714225) are the most relevant candidate modifier genes in this family,” and that “relative accumulation of the deficiencies associated with variants of these genes along with other lesser deficiencies in other genes appears to explain the variable expressivity in MEND syndrome.”[8][16] APOA5 encodes apolipoprotein A‑V, a regulator of plasma triglyceride levels; ABCA1 encodes an ATP‑binding cassette transporter critical for cholesterol efflux to apolipoproteins; APOB encodes apolipoprotein B, essential for lipoprotein assembly and cholesterol transport.[16][18]

These findings suggest that genetic variation in pathways controlling sterol transport, efflux, and lipoprotein metabolism can modulate the phenotypic impact of EBP dysfunction at the cellular level.[16][18] For example, reduced ABCA1 function may exacerbate intracellular cholesterol imbalance in neurons and keratinocytes, worsening developmental anomalies. Conversely, robust APOA5 and APOB function might mitigate lipid dysregulation, partly compensating for EBP defects. While these conclusions are based on a single family and require replication, they introduce a conceptual framework in which MEND syndrome severity reflects both the primary EBP lesion and a “modifier burden index” across key cholesterol homeostasis genes.[8][16] This model parallels emerging work in other Mendelian disorders where polygenic background modulates penetrance and expressivity.

At present, no epigenetic modifiers (e.g., DNA methylation or histone modifications affecting EBP expression) have been directly implicated in MEND syndrome, and no systematic studies of epigenomic variation in affected individuals have been reported.[18] Similarly, large‑scale chromosomal abnormalities such as aneuploidy, translocations, or inversions have not been associated with MEND; the disease is instead driven by point mutations and small insertions/deletions in EBP.[15][17][18] Clinical genetic testing and research focus therefore remains on single‑gene EBP sequencing and panel/exome approaches that capture point variants and small indels, with occasional consideration of copy‑number variation at the locus.

### 4.4 Molecular Profiling and Structural Features

Beyond targeted gene sequencing, molecular profiling in MEND syndrome has begun to incorporate computational structural analysis and integrative genomics. The Trp186Arg variant study employed homology modeling based on known sterol isomerase structures, followed by computational energy minimization and simulation to assess the impact of the mutation on protein conformation.[18] The authors found that the Trp186Arg substitution disrupts hydrophobic interactions within the transmembrane domain and may alter the geometry of the active site, leading to reduced enzymatic activity.[18] Such computational evidence complements biochemical function predictions and underscores the importance of structural modeling for variant interpretation in small proteins like EBP.

Transcriptomic, proteomic, metabolomic, and lipidomic profiling specific to MEND syndrome has not yet been reported, likely due to the rarity of the disease.[18] However, sterol profiling (a form of targeted metabolomics) is a well‑established diagnostic tool, with patterns of elevated 8‑dehydrocholesterol and 8(9)‑cholestenol marking EBP deficiency.[14][17] Future lipidomics studies could provide more detailed signatures of sterol intermediates and membrane lipid composition in affected tissues. Genomic structural features at the EBP locus have been characterized in general, with no evidence of common structural variants causing MEND; instead, classic point mutations predominate.[17][18] Multi‑omics integration using single‑cell or spatial transcriptomics remains aspirational rather than realized, given the very small patient population and the challenges of obtaining tissue samples.

From a gene ontology perspective, EBP links to pathways including “cholesterol biosynthetic process” (GO:0006695), “regulation of steroid biosynthetic process” (GO:0050810), and “organic acid metabolic process” (GO:0006082). It interacts functionally with enzymes upstream and downstream in the sterol biosynthesis pathway, such as DHCR7 (defective in Smith–Lemli–Opitz syndrome) and sterol C‑5 desaturase, forming part of a tightly regulated network.[17] In terms of cell ontology, primary affected cells include keratinocytes (CL:0000312), neurons (CL:0000540), chondrocytes (CL:0000138), and lens fiber cells, all of which rely on EBP‑mediated cholesterol synthesis for proper function and development.[17][18]

## 5. Environmental Information

### 5.1 Non‑Genetic Contributing Factors

Current evidence supports a model in which non‑genetic environmental factors play little to no causal role in the occurrence of MEND syndrome. The disorder arises from germline EBP mutations and presents at or shortly after birth, consistent with a primary developmental etiology.[15][19] Case reports do not document specific maternal exposures, infections, or toxins associated with MEND, and there is no indication in OMIM or Orphanet that environmental factors are recognized contributors.[15][19] Comparative Toxicogenomics resources have not identified particular exogenous chemicals that mimic EBP deficiency phenotypes in humans, though certain cholesterol biosynthesis inhibitors (e.g., statins) can cause developmental anomalies in animal models by interfering with similar pathways.[17]

In theoretical terms, environmental factors that influence cholesterol metabolism might exacerbate or ameliorate some manifestations in individuals with MEND syndrome, but such interactions remain speculative. For example, severe malnutrition or dietary deficiency in essential fatty acids might compound membrane lipid abnormalities, whereas high cholesterol intake could modestly supplement systemic levels, though not necessarily correcting intracellular biosynthetic defects.[17][18] However, no empirical studies in MEND populations have tested these hypotheses. Thus, environmental contributions to disease onset are negligible, while possible effects on symptom severity or comorbidity require future investigation.

### 5.2 Lifestyle Factors and Infectious Agents

Lifestyle factors such as smoking, alcohol consumption, and physical activity are not relevant to the primary pathogenesis of MEND syndrome, given its congenital nature and early onset. In older patients with MEND, general lifestyle choices may impact overall health and comorbidity, as in any chronic neurologic disorder, but they do not alter the underlying developmental defects.[15][18] There is no evidence that infectious agents (bacteria, viruses, fungi, parasites) directly cause or trigger MEND syndrome. No reports link specific infections to exacerbation of core skeletal, neurologic, or dermatologic features beyond typical infection‑related complications that any immunocompetent patient might experience.[11][19]

Consequently, infectious agents are not considered part of the etiologic spectrum of MEND syndrome, and infection control focuses on routine pediatric and neurologic care rather than disease‑specific concerns. Vaccination schedules follow standard guidelines, with attention to seizure disorders when administering vaccines that may provoke fever.[19] Overall, lifestyle and infectious factors occupy only a marginal role in MEND syndrome’s clinical landscape.

## 6. Mechanism and Pathophysiology

### 6.1 Cholesterol Biosynthesis Pathway and EBP Function

The pathophysiology of MEND syndrome hinges on disruption of the cholesterol biosynthesis pathway at a late step catalyzed by EBP. Cholesterol biosynthesis is a multistep pathway beginning from acetyl‑CoA, proceeding through mevalonate, squalene, lanosterol, and several intermediate sterols, ultimately yielding cholesterol.[17][18] EBP functions as a delta(8)–delta(7) sterol isomerase, converting 8(9)‑cholestenol to lathosterol, a precursor that is further desaturated and reduced to cholesterol.[14][17] When EBP activity is reduced by hypomorphic mutations, flux through this step is impaired, leading to accumulation of sterol intermediates such as 8‑dehydrocholesterol and 8(9)‑cholestenol and a relative deficiency of cholesterol in certain cellular membranes.[14][17][18]

OMIM notes that in CDPX2 patients, plasma and tissue sterol profiles show increased levels of 8‑dehydrocholesterol and 8(9)‑cholestenol, suggesting deficiency of 3‑beta‑hydroxysteroid‑delta(8),delta(7)‑isomerase.[14] Derry et al. identified analogous sterol abnormalities in Tattered (Td) mice carrying Ebp mutations, establishing that EBP acts as a principal enzyme of cholesterol biosynthesis.[17] While specific sterol profiling in MEND syndrome is less extensively reported, the Brazilian case supports a similar pattern, noting accumulation of sterol precursors and low intracellular cholesterol despite normal serum cholesterol.[11] The recent Trp186Arg study reaffirmed that hypomorphic hemizygous non‑mosaic EBP variants cause MEND syndrome, with functional impairment predicted by structural modeling.[18]

GO pathways implicated include “cholesterol biosynthetic process” (GO:0006695), “sterol biosynthetic process” (GO:0016126), and “lipid metabolic process” (GO:0006629). EBP’s cellular component annotation emphasizes the endoplasmic reticulum membrane (GO:0005789) as the primary site of dysfunction. CHEBI entities central to pathophysiology include cholesterol (CHEBI:16113) and intermediate sterols such as 8‑dehydrocholesterol and 8(9)‑cholestenol.[14][17][18] At a systems level, the metabolic block leads to altered membrane composition, disruption of lipid raft integrity, and impaired post‑translational modification of hedgehog family proteins, which require cholesterol for signaling competence.[17][18]

### 6.2 Developmental Signaling Pathways and Downstream Effects

Cholesterol plays a critical role in the regulation of developmental signaling pathways, particularly Sonic hedgehog (SHH) and related hedgehog proteins, which undergo cholesterol modification and require sterol‑rich membrane microdomains for effective signal transduction.[17][18] In embryos with EBP deficiency, partial cholesterol depletion and sterol intermediary accumulation in key tissues such as neuroectoderm and mesoderm are hypothesized to disrupt SHH signaling gradients, leading to malformations in the brain, eyes, skeleton, and craniofacial structures.[17][18] While direct measurement of hedgehog signaling in MEND patients has not been performed, analogous mechanisms have been demonstrated in other sterol biosynthesis disorders such as Smith–Lemli–Opitz syndrome (DHCR7 deficiency), where impaired SHH signaling causes holoprosencephaly and limb anomalies.[17]

Additional pathways potentially impacted include Wnt and Notch signaling, which are sensitive to membrane lipid composition and cholesterol content. GO biological processes such as “hedgehog signaling pathway” (GO:0007229), “Wnt signaling pathway” (GO:0016055), and “embryonic morphogenesis” (GO:0048598) capture the broader developmental roles of cholesterol. The downstream effect of EBP dysfunction thus comprises a cascade from metabolic blockade to altered signaling to structural malformations. Upstream, the primary trigger is the germline hypomorphic EBP variant and its impact on enzymatic activity; midstream, sterol accumulation and depletion perturb cell membranes and signaling; downstream, tissue patterning errors manifest as the complex phenotypes of MEND syndrome.[14][17][18]

### 6.3 Cellular Processes: Membrane Integrity, Myelination, and Neurodevelopment

At the cellular level, EBP deficiency affects multiple processes dependent on cholesterol and sterol homeostasis. Neurons rely on cholesterol for synapse formation, dendritic arborization, and myelination; oligodendrocytes synthesize large amounts of cholesterol for myelin sheaths.[17][18] In EBP‑mutant embryos, reduced cholesterol in neural tissues may compromise these processes, leading to hypotonia, developmental delay, and structural brain anomalies such as corpus callosum and cerebellar hypoplasia.[19] GO processes such as “myelination” (GO:0042552), “synapse organization” (GO:0050808), and “neuron projection development” (GO:0031175) are biologically plausible points of impact. Primary cell types involved include neurons (CL:0000540), oligodendrocytes (CL:0000128), and radial glia (CL:0000133).

Keratinocytes in the epidermis also depend on sterol balance for barrier formation and desquamation. Altered cholesterol and sterol intermediates in epidermal membranes can perturb keratinocyte differentiation and cornification, resulting in ichthyosis and collodion membrane phenotypes.[11][19] GO processes such as “epidermis development” (GO:0008544) and “keratinocyte differentiation” (GO:0030216) are affected, with keratinocytes (CL:0000312) as key cell types. Chondrocytes and osteoblasts similarly rely on sterols in membrane microdomains that organize growth factor signaling, explaining skeletal anomalies.[17][18]

Apoptosis and autophagy may be indirectly influenced by sterol imbalances, particularly in neurons, though direct evidence in MEND is lacking. Oxidative stress may arise from membrane instability and accumulation of unusual sterols, contributing to tissue damage. However, detailed mechanistic studies at the cellular level remain sparse, and most inferences derive from knowledge of cholesterol biology and other sterol biosynthesis disorders rather than MEND‑specific data.[17][18]

### 6.4 Tissue Damage Mechanisms and Biochemical Abnormalities

Tissue damage in MEND syndrome is primarily developmental rather than degenerative. Malformations arise during organogenesis due to disrupted signaling and morphogenesis, and tissues then persist with abnormal structure throughout life.[15][19] Nevertheless, ongoing biochemical abnormalities may contribute to secondary damage. Accumulated sterol intermediates could insert into membranes and alter fluidity, potentially increasing susceptibility to mechanical injury or impairing membrane protein function.[14][17] In the skin, abnormal sterol composition may weaken barrier function, leading to chronic inflammation and increased infection risk. In the brain, subtle ongoing effects on synaptic function and plasticity may influence cognitive trajectories.

Biochemical abnormalities center on the deficient activity of 3‑beta‑hydroxysteroid‑delta(8),delta(7)‑isomerase (EBP), as evidenced by sterol profiles and genetic analysis.[14][17][18] BRENDA and UniProt annotate EBP with sterol isomerase activity, and OMIM details the enzyme’s role in late cholesterol biosynthesis.[17] These annotations support the view that MEND syndrome is essentially an inborn error of cholesterol metabolism with unique phenotypic consequences. Epigenetic changes have not been documented as primary drivers of these biochemical abnormalities, and epigenomic profiling in MEND has not been reported.[18]

### 6.5 Evidence Types and Mechanistic Quotes

Mechanistic understanding of MEND syndrome comes from a mix of human clinical evidence, model organism experimentation, in vitro biochemistry, and computational modeling. Derry et al. identified Ebp mutations in Td mice and showed that “all Td mice showed a single nucleotide substitution resulting in an amino acid substitution of arginine for glycine at amino acid position 107,” linking this to sterol abnormalities and skeletal phenotypes analogous to CDPX2.[17] Arnold et al. compared Conradi–Hünermann–Happle syndrome in males versus MEND syndrome and emphasized that MEND represents a continuum of EBP‑related phenotypes with non‑mosaic hypomorphic alleles in males.[14][17] The recent MEND variant study stated that “male EBP disorder with neurologic defects (MEND syndrome) is an extremely rare disorder with a prevalence of less than 1/1,000,000 individuals worldwide” and that “hypomorphic hemizygous non‑mosaic EBP variants cause MEND syndrome in males who are born to clinically asymptomatic heterozygous mothers.”[18]

Barboza‑Cerda et al. wrote that “phenotypic severity in a family with MEND syndrome is directly associated with the accumulation of potentially functional variants of cholesterol homeostasis genes,” highlighting the modifier gene concept.[8][16] The Brazilian case report concluded that “MEND syndrome is caused by mutations in the gene encoding the emopamil‑binding protein (EBP), located on the short arm of the X chromosome. EBP is a sterol isomerase responsible for one of the final steps in the production of cholesterol.”[11] These direct quotes, though brief, illustrate the convergence of clinical, genetic, and biochemical evidence underpinning current mechanistic models.

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement

MEND syndrome affects multiple organ systems, reflecting the widespread roles of cholesterol and sterols in development. Primary organs directly involved include the skin (UBERON:0002097), brain (UBERON:0000955), eyes (UBERON:0000970), bones and joints (UBERON:0000982), heart (UBERON:0000948), and urogenital organs (UBERON entities for testes, kidneys, and urinary tract).[15][19] Dermatologic manifestations such as collodion membrane and ichthyosis highlight primary involvement of the integumentary system.[11][19] Neurologic phenotypes including intellectual disability, seizures, and structural brain malformations demonstrate central nervous system involvement, with specific structures such as the cerebellum (UBERON:0002037), corpus callosum (UBERON:0002312), and ventricles (UBERON:0002128) affected.[19]

Craniofacial anomalies implicate cranial bones (UBERON:0008839), facial skeleton, and palate (UBERON:0003134). Skeletal phenotypes such as scoliosis and kyphosis involve the vertebral column (UBERON:0002240), ribs, and long bones.[15][19] Ocular anomalies affect the lens (UBERON:0001799) and globe, while cardiac defects involve the heart and great vessels.[19] Urogenital anomalies such as cryptorchidism involve testes (UBERON:0000473) and associated structures. Secondary organ involvement arises through complications, such as respiratory compromise due to scoliosis (lungs, UBERON:0002048) or infections due to skin barrier defects.[11][18] The nervous, integumentary, musculoskeletal, ocular, cardiovascular, and urogenital systems thus constitute the main anatomical domains implicated in MEND syndrome.

### 7.2 Tissue and Cell‑Level Involvement

At the tissue level, MEND syndrome affects epithelial, nervous, connective, and muscular tissues. Epidermal tissue (stratified squamous epithelium) and dermis display abnormal keratinization and barrier function due to altered sterol composition.[11][19] Nervous tissue, especially cortical gray matter and white matter tracts, exhibits developmental anomalies such as hypoplasia and dysplasia.[19] Connective tissues in bone and cartilage show growth and patterning defects, leading to skeletal dysmorphology.[15][18] Ocular tissues, including lens and retina, may be affected by altered lipid content.

Cell types central to pathogenesis include keratinocytes (CL:0000312), melanocytes (CL:0000148), neurons (CL:0000540), oligodendrocytes (CL:0000128), chondrocytes (CL:0000138), osteoblasts (CL:0000145), lens fiber cells, cardiomyocytes (CL:0000746), and gonadal cells. Each of these cell populations depends on cholesterol and sterol intermediates for membrane integrity, signaling, and structural organization.[17][18] Disruption of EBP function in these cells leads to specific manifestations: keratinocyte dysfunction causes ichthyosis; neuronal and glial dysfunction leads to intellectual disability and brain malformations; chondrocyte and osteoblast defects result in skeletal anomalies; lens cell dysfunction produces cataracts.[14][17][18]

### 7.3 Subcellular Localization and Compartments

Subcellular compartments implicated in MEND syndrome include the endoplasmic reticulum (ER), plasma membrane, and lipid rafts. EBP localizes primarily to the ER membrane (GO:0005789), where it catalyzes sterol isomerization.[17] Dysfunction at this site affects the composition of sterols that are subsequently trafficked to the Golgi and plasma membrane. Plasma membrane lipid rafts, which are cholesterol‑rich microdomains, are critical for clustering and signaling of receptors and morphogens; altered cholesterol and sterol composition in these rafts can disrupt signaling pathways such as hedgehog and Wnt.[17][18] Mitochondria and lysosomes may experience secondary effects due to changes in membrane lipid composition and trafficking, though these have not been explicitly documented in MEND.

GO cellular component terms relevant here include “endoplasmic reticulum membrane” (GO:0005789), “plasma membrane” (GO:0005886), and “membrane raft” (GO:0045121). The causal chain thus spans from EBP dysfunction in the ER to altered sterol content in the plasma membrane and lipid rafts, impacting signaling and tissue organization. In neurons, this affects synaptic membranes; in keratinocytes, cornified envelope formation; in chondrocytes, matrix interactions.

### 7.4 Localization and Lateralization Patterns

Anatomically, MEND syndrome’s malformations can be symmetric or asymmetric. Craniofacial dysmorphism, microphthalmia, and skeletal deformities such as scoliosis often show asymmetry, though bilateral involvement is common.[11][19] Dandy–Walker malformation and corpus callosum hypoplasia are midline anomalies, inherently symmetric in their disruption of central structures.[19] Skin manifestations may display patchy distribution with areas of hypo‑ or hyperpigmentation, reflecting mosaic patterns of expression related to X‑inactivation in carrier females; however, in affected males with non‑mosaic EBP variants, skin abnormalities are more generalized.[11][14]

Localization to specific anatomical sites provides diagnostic clues. For example, large anterior fontanelle localizes to the cranial vault; syndactyly of toes 2‑3 localizes to the foot; specific cardiac defects localize to septal structures. UBERON terms such as “anterior fontanelle” (UBERON:0001741) and “toe” (UBERON:0001480) can be used in ontology annotation. Lateralization patterns (right vs left) are less prominent than the overarching presence of anomalies, and MEND syndrome is not strongly lateralized as a disease entity.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

MEND syndrome is a congenital disorder with onset in the neonatal period or infancy. Orphanet specifies an age of onset in infancy, noting that collodion membrane, ichthyosis, and craniofacial dysmorphism are evident at birth or soon after.[19] OMIM and case reports corroborate that major features such as dermatologic abnormalities, dysmorphism, and neurodevelopmental delay arise early in life.[11][15][18] In some cases, structural brain anomalies such as Dandy–Walker malformation and corpus callosum hypoplasia may be detected prenatally via ultrasound or fetal MRI, though MEND syndrome is typically not recognized before birth due to its rarity and lack of routine screening.[18]

The onset pattern is chronic and insidious in the sense that developmental impairments become more apparent as milestones fail to be achieved, rather than acute episodes. The collodion membrane at birth is an acute presentation of cutaneous abnormality, but it transitions to chronic ichthyosis. Seizures may begin acutely at a particular age, but they arise against a background of pre‑existing brain malformations. Thus, onset is best characterized as congenital and chronic, not subacute or adult‑onset.[15][19]

### 8.2 Disease Progression and Stages

Disease progression in MEND syndrome can be conceptualized across developmental stages. In the neonatal stage, collodion membrane, ichthyosis, and craniofacial dysmorphism dominate the clinical picture, with potential early recognition of hypotonia.[11][19] During infancy, structural brain anomalies may manifest clinically through delayed motor milestones, feeding difficulties, and early seizures, while dermatologic issues persist. In childhood, scoliosis, kyphosis, and joint contractures may become more pronounced as growth reveals skeletal malformations, and intellectual disability becomes clearly evident.[15][18] Adolescence and adulthood involve chronic management of established disabilities, orthopedic complications, and ocular issues such as cataracts.

Progression rate is variable. Some musculoskeletal features, like scoliosis, may worsen over time, requiring orthopedic monitoring. Seizure frequency may fluctuate, but underlying brain malformations remain stable. Dermatologic manifestations remain chronic but can be somewhat modulated by treatment. Disease course is overall progressive in terms of functional impairment; few features remit spontaneously.[15][18][19] As an inborn error of development, MEND lacks classic remission phases seen in inflammatory or neoplastic diseases. However, symptom management can improve quality of life and functional capacity.

### 8.3 Remission Patterns and Critical Periods

Spontaneous remission of major features in MEND syndrome is not observed. Structural anomalies and intellectual disability are permanent. Seizure control may be achieved with antiepileptic drugs in some individuals, representing treatment‑induced remission of a particular symptom but not of the underlying disease.[15][18] Dermatologic symptoms can be ameliorated with emollients and keratolytics, but ichthyosis persists.

Critical periods in MEND syndrome correspond to key windows of brain and skeletal development. Embryonic and early fetal stages represent a critical period during which EBP deficiency disrupts organogenesis; interventions at this stage are currently not feasible in humans. Postnatally, early infancy and childhood are critical for developmental interventions and seizure management. Intensive early intervention services (physical, occupational, speech therapy) during this window may optimize functional outcomes within the constraints imposed by structural anomalies.[18][19] Additionally, early recognition and surgical correction of cleft palate, cataracts, and cardiac defects can reduce secondary complications.

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

MEND syndrome is an extremely rare disorder. Orphanet lists its prevalence as <1 per 1,000,000 individuals, indicating that fewer than one in a million people are affected worldwide.[19] The recent molecular study echoes this, stating that “MEND syndrome is an extremely rare disorder with a prevalence of less than 1/1,000,000 individuals worldwide.”[18] Because of this rarity, incidence figures (new cases per year) are not well defined and are likely on the order of a handful of cases globally per decade. No national registries or large epidemiologic studies exist for MEND syndrome, and most knowledge comes from isolated case reports and small families.[8][11][16][18]

Global Burden of Disease estimates do not specifically quantify MEND syndrome due to its rarity and aggregation under broader congenital malformation categories. As a result, precise epidemiologic metrics are unavailable, and estimates rely on expert consensus and Orphanet’s orphan disease classification.[19] Nevertheless, the recognition that MEND is ultra‑rare informs clinical expectations and research prioritization.

### 9.2 Inheritance Pattern, Penetrance, and Expressivity

MEND syndrome follows an X‑linked recessive inheritance pattern. OMIM explicitly states that MEND is “an X‑linked recessive disorder representing a continuous phenotypic spectrum with variable manifestations associated with a defect in sterol biosynthesis,” mapping the phenotype to EBP at Xp11.23.[15] Orphanet also classifies MEND syndrome as X‑linked recessive, noting that it primarily affects males born to carrier females.[19] Carrier females are typically heterozygous for an EBP variant and clinically asymptomatic due to random X‑inactivation and compensatory activity from the normal allele, though they may show biochemical sterol abnormalities.[14][15][18]

Penetrance in male hemizygous carriers of hypomorphic EBP variants is effectively complete; all reported males with such variants exhibit MEND or related phenotypes.[14][15][18] However, expressivity is highly variable, with differences in severity and specific manifestations even among individuals sharing the same variant, as demonstrated in the Mexican family.[8][16] OMIM emphasizes that “not all patients show all features, and the severity is highly variable,” underscoring the role of modifier genes and possibly environmental influences.[15][16] Genetic anticipation, characterized by increasing severity in successive generations due to repeat expansion or other mechanisms, has not been reported in MEND syndrome, consistent with its point‑mutation etiology.[15][17]

Germline mosaicism in EBP has not been specifically described for MEND syndrome, but somatic and gonadal mosaicism are well documented in CDPX2, especially in female carriers and occasional male cases.[14][17] Founder effects, whereby a particular EBP variant becomes prevalent in a specific population, have not been established; reported cases originate from diverse geographic and ethnic backgrounds.[8][11][18] Carrier frequency for pathogenic EBP variants causing MEND is extremely low, reflecting the ultra‑rare nature of the disease and strong negative selection against such variants.[17][19]

### 9.3 Population Demographics and Geographic Distribution

Affected populations include individuals from Latin America, Europe, and other regions, indicating that MEND syndrome is not geographically restricted. The Mexican family provides evidence of MEND in a Latin American population, while the Brazilian newborn case situates MEND in South America.[8][11][16] Arnold et al.’s comparison of CDPX2 and MEND includes cases from European cohorts, further broadening the geographic representation.[14][17] The recent Trp186Arg variant study may involve a South Asian or other population, reflecting the global distribution of rare EBP variants.[18] However, due to the small number of cases, no robust conclusions about ethnic predilection or regional clustering can be drawn.

Sex ratio is heavily skewed toward males, as expected for an X‑linked recessive disease with male‑limited expression. Female heterozygotes are usually asymptomatic carriers, although rare symptomatic females with mosaicism and CDPX2 phenotypes have been described.[14][17] Age distribution of affected individuals spans from neonates and infants to adults, depending on survival and recognition; most published cases focus on pediatric patients due to early manifestation of severe features.[11][18][19] Adult men with milder forms of MEND syndrome may be under‑recognized or misdiagnosed, especially if dermatologic and skeletal features predominate and neurologic impairment is moderate.[15][16]

## 10. Diagnostics

### 10.1 Clinical Evaluation and Laboratory Tests

Diagnostic evaluation of MEND syndrome begins with clinical recognition of the characteristic constellation of features: male sex, syndromic ichthyosis with collodion membrane or severe scaling, craniofacial dysmorphism, neurodevelopmental delay, seizures, and skeletal anomalies.[11][15][19] Dermatologic examination identifies ichthyosis, patchy hypopigmentation, and hair shaft abnormalities, the latter sometimes confirmed by scanning electron microscopy showing structural defects akin to CDPX2.[11] Neurologic assessment documents hypotonia, developmental delay, and seizure patterns, while neuroimaging (MRI) reveals hydrocephalus, corpus callosum hypoplasia, cerebellar hypoplasia, and Dandy–Walker malformation.[19] Orthopedic evaluation notes scoliosis, kyphosis, and syndactyly or polydactyly, with radiographs confirming skeletal deformities.[15][18]

Laboratory tests play a critical role in confirming the diagnosis. Sterol profiling via gas chromatography–mass spectrometry assesses plasma levels of cholesterol and intermediates such as 8‑dehydrocholesterol and 8(9)‑cholestenol.[14][17] In EBP‑related disorders, elevations of these intermediates are highly specific indicators of EBP mutation, with OMIM noting that plasma sterol analysis is “a highly specific and sensitive indicator of the presence of an EBP mutation in females with suspected CDPX2, including a clinically unaffected mother of a sporadic case.”[14] While this statement refers to CDPX2, the same biochemical signature is expected in MEND syndrome and can support diagnosis in males. Routine laboratory tests (complete blood counts, basic metabolic panels) are generally unremarkable, as MEND’s primary abnormalities lie in sterol metabolism and development.[11][18]

HPO terms for diagnostic findings include abnormal sterol profile (HP:0012147), MRI abnormalities of the brain (HP:0003432), and radiographic anomalies of the skeleton (HP:0000938). LOINC codes for specific sterol tests and MRI sequences can be used for structured data capture. NCIT terms such as “Magnetic Resonance Imaging” (NCIT:C16810), “Biochemical Test” (NCIT:C78209), and “Electron Microscopy” (NCIT:C16510) refer to diagnostic modalities.

### 10.2 Genetic Testing Strategy

Genetic testing is central to definitive diagnosis of MEND syndrome. Because the disease is caused by variants in a single gene (EBP), targeted sequencing of EBP is recommended when the clinical phenotype suggests a sterol biosynthesis disorder with X‑linked pattern and characteristic features.[15][17][18] Single‑gene testing via Sanger sequencing or next‑generation sequencing can identify missense, nonsense, and small indel variants in EBP, including those previously reported and novel variants.[17][18] Gene panels for congenital ichthyosis, ectodermal dysplasia, or malformation syndromes may include EBP among other genes, and panel testing may be appropriate when MEND is in the differential diagnosis but not strongly suspected.[18][19]

Whole exome sequencing (WES) has proven valuable in cases where clinical features are atypical or when EBP variants need to be identified alongside potential modifier genes. In the Mexican family, WES enabled identification of both the primary EBP mutation and 105 missense variants in cholesterol homeostasis genes, facilitating modifier analysis.[8][16] WES also helps rule out other genetic disorders and discover novel variants. Whole genome sequencing (WGS) offers comprehensive coverage, including regulatory regions and intronic variants, but its utility has not yet been specifically reported in MEND syndrome.

Chromosomal microarray (CMA), karyotyping, FISH, and mitochondrial DNA testing are generally not first‑line tests for MEND syndrome, given the known single‑gene etiology and the lack of large‑scale chromosomal aberrations.[15][17] However, karyotyping may be performed in differential diagnosis to exclude other syndromic chromosomal conditions. Repeat expansion testing is not relevant, as EBP has no known repeat expansion pathology.[17][18]

ClinGen and the Genetic Testing Registry (GTR) list EBP gene tests with indications including CDPX2 and MEND syndrome. Carrier testing for heterozygous females in families with known MEND cases is essential for genetic counseling, and prenatal testing or preimplantation genetic diagnosis (PGD) can be offered when the familial EBP variant is known.[15][18][19] NCIT terms relevant to genetic testing include “Genetic Testing” (NCIT:C17584), “Whole Exome Sequencing” (NCIT:C101294), and “Carrier Testing” (NCIT:C18102).

### 10.3 Omics‑Based Diagnostics and Biomarkers

Beyond targeted gene sequencing and sterol profiling, omics‑based diagnostics in MEND syndrome remain limited. RNA sequencing and proteomics specific to MEND have not been reported, largely because of small patient numbers and difficulties in obtaining appropriate tissue samples.[18] Metabolomics, particularly targeted sterol profiling, functions as a de facto omics approach, providing diagnostic biomarkers that directly reflect EBP dysfunction.[14][17] HMDB and MetaboLights could potentially catalog such sterol signatures in the future.

Epigenomics and liquid biopsy technologies have not been applied to MEND syndrome. Serum biomarkers beyond sterols (e.g., inflammatory markers, neurofilament proteins) are not specific and have not been studied systematically. As such, current biomarker strategies revolve around sterols and genetic variants rather than novel molecular markers.

### 10.4 Clinical Criteria and Differential Diagnosis

No formal standardized diagnostic criteria (akin to DSM or ICD‑based algorithms) exist specifically for MEND syndrome due to its rarity. However, a pragmatic clinical approach involves the combination of male sex, congenital ichthyosis or collodion membrane, neurodevelopmental delay, seizures, craniofacial dysmorphism, skeletal anomalies, and positive sterol and genetic findings.[11][15][19] Differential diagnosis includes CDPX2 (Conradi–Hünermann–Happle syndrome), other syndromic ichthyoses such as CHILD syndrome and Sjögren–Larsson syndrome, and other sterol biosynthesis disorders like Smith–Lemli–Opitz syndrome.[14][17][19]

CDPX2 shares many features with MEND, including ichthyosis, skeletal anomalies, and sterol abnormalities, but differs in inheritance (X‑linked dominant), presence of chondrodysplasia punctata (stippling of epiphyses), and mosaic patterns in females due to X‑inactivation.[14][17] MEND affects non‑mosaic hemizygous males and lacks classic punctate calcifications. Smith–Lemli–Opitz syndrome involves distinct biochemical abnormalities (elevated 7‑dehydrocholesterol) and different facial and limb features. Careful clinical and biochemical differentiation, supported by gene testing, is necessary to distinguish these conditions.

### 10.5 Screening and Early Detection

Population‑based screening for MEND syndrome is not currently implemented, given its ultra‑rare prevalence and complex phenotype. Newborn screening programs do not include sterol profiling or EBP genotyping. However, targeted screening through cascade testing in families with known EBP variants can identify carrier females and affected male infants early.[15][18][19] Prenatal diagnosis by chorionic villus sampling or amniocentesis with EBP sequencing can detect affected male fetuses in at‑risk pregnancies, enabling informed reproductive decisions.[15][18]

Preimplantation genetic diagnosis (PGD) offers another avenue for prevention in families with known pathogenic EBP variants. Risk stratification via genetic counseling can identify high‑risk couples, especially those with a previously affected child or known carrier status. NCIT terms relevant here include “Prenatal Diagnosis” (NCIT:C97078), “Preimplantation Genetic Diagnosis” (NCIT:C16295), and “Cascade Genetic Testing” (NCIT:C113729).

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Data on survival and mortality in MEND syndrome are limited, as only a small number of cases have been published. Available reports suggest that affected males can survive into childhood and adolescence, and possibly adulthood, depending on severity and medical care.[8][11][18][19] Unlike null EBP variants causing intrauterine lethality in males, hypomorphic EBP variants in MEND allow postnatal survival.[18] Severe cases with profound brain malformations, intractable seizures, and major cardiac defects may face increased mortality in infancy or early childhood, though quantitative survival rates (e.g., 5‑year or 10‑year survival) are not documented.[19]

Life expectancy is thus highly variable and depends on the specific EBP variant, modifier gene burden, and presence of life‑threatening anomalies. Given the absence of large cohorts, mortality rates are unknown and likely underestimated due to under‑recognition. Deaths directly attributable to MEND syndrome may arise from complications such as status epilepticus, respiratory failure due to scoliosis, heart failure from cardiac defects, and infections in neonates with compromised skin barrier.[11][18][19]

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in MEND syndrome is significant, driven by multisystem involvement and chronic functional impairments. Intellectual disability and developmental delay limit education, employment, and independent living, often resulting in long‑term dependence on caregivers and services.[15][18][19] Seizures, motor impairments, and muscle hypotonia further restrict mobility and daily functioning. Skeletal deformities such as scoliosis and kyphosis can cause pain, reduced exercise tolerance, and respiratory compromise. Dermatologic manifestations contribute to discomfort, infection risk, and psychosocial challenges.

Disability outcomes span a spectrum from moderate to profound. Some patients may achieve partial self‑care and communication, while others remain nonverbal and fully dependent. The International Classification of Functioning, Disability and Health (ICF) framework would categorize MEND syndrome as affecting body structures (e.g., nervous system, skin, musculoskeletal), activities (e.g., mobility, communication), and participation (e.g., social interaction, schooling). Quality of life measures such as EQ‑5D and SF‑36 have not been systematically applied to MEND patients, but case descriptions imply major impairments in mobility, self‑care, usual activities, and pain/discomfort dimensions.[11][18][19]

### 11.3 Disease Course, Complications, and Recovery Potential

The disease course in MEND syndrome is chronic and lifelong. Structural anomalies and intellectual disability do not regress, and management focuses on symptom control and maximizing functional potential. Complications include orthopedic issues requiring surgery, cataracts requiring extraction, cleft palate requiring repair, and seizures requiring antiepileptic therapy.[11][18][19] Respiratory complications from scoliosis, feeding difficulties from craniofacial anomalies, and infections from skin barrier defects represent additional burdens. Recovery potential is limited by developmental constraints; while therapies can improve specific skills and manage symptoms, full normalization of function is not achievable.

Prognostic factors include the severity of brain malformations, seizure control, presence of major cardiac defects, and the genetic modifier burden. The Mexican family study suggests that a high burden of deleterious variants in APOA5, ABCA1, APOB, and related genes correlates with more severe phenotypes.[8][16] Early diagnosis and intervention may improve outcomes by enabling prompt seizure management, surgical correction of anatomical defects, and initiation of developmental therapies.[18][19] However, no validated prognostic biomarkers beyond genotype have been identified.

## 12. Treatment

### 12.1 Pharmacologic Management

No disease‑specific pharmacologic therapy exists for MEND syndrome that corrects the underlying EBP deficiency or sterol biosynthesis defect. Treatment is therefore supportive and symptomatic, targeting individual manifestations. Antiepileptic drugs (AEDs) are used to control seizures, with choices based on seizure type and patient comorbidities.[15][18] NCIT terms such as “Antiepileptic Agent” (NCIT:C288) and specific agents (e.g., valproic acid, levetiracetam) apply. Dermatologic management relies on emollients, keratolytic agents, and topical therapies to reduce scaling and maintain barrier function, consistent with treatments for ichthyosis.[11][19] Systemic retinoids are sometimes used in other ichthyoses but have not been specifically studied in MEND syndrome.

No published trials have examined systemic cholesterol supplementation or statin therapy in MEND syndrome. In theory, cholesterol supplementation might ameliorate systemic deficiency, but given that EBP acts at a late step in intracellular biosynthesis, dietary cholesterol may not adequately correct cell‑intrinsic defects.[17][18] Moreover, statins, which inhibit early steps in cholesterol biosynthesis, would likely worsen sterol block and are contraindicated. Pharmacogenomic considerations have not been specifically reported; EBP variants do not directly affect drug metabolism, though polypharmacy for seizures and other symptoms must be managed carefully.

### 12.2 Advanced Therapeutics and Experimental Approaches

Advanced therapeutics such as gene therapy, RNA‑based interventions, or targeted molecular therapies have not yet been developed for MEND syndrome. In principle, gene replacement therapy delivering a functional EBP gene via viral vectors to affected tissues could correct the enzymatic defect, but practical challenges include delivery to multiple organ systems and timing relative to development.[18] CRISPR‑based editing of EBP mutations in embryos or somatic tissues is likewise theoretically possible but faces ethical and technical obstacles. No clinical trials registered in ClinicalTrials.gov currently target EBP or MEND syndrome specifically.

Cell therapies, including stem cell transplantation, have not been applied to MEND. RNA‑based therapies such as antisense oligonucleotides or siRNAs could modulate expression of modifier genes, but such strategies remain speculative. Given the small patient population, the feasibility of advanced trials is limited, though insights from more common sterol biosynthesis disorders might eventually inform experimental interventions.

### 12.3 Surgical and Interventional Management

Surgical interventions play a crucial role in managing structural anomalies in MEND syndrome. Cleft palate repair improves feeding and speech; cataract extraction restores vision; orthopedic surgeries such as spinal fusion address severe scoliosis and kyphosis.[11][18][19] Cardiac surgical procedures may be required for significant congenital heart defects. Orchiopexy is indicated for cryptorchidism, reducing infertility risk and malignancy potential.[15][19] Neurosurgical interventions, including shunt placement, may be necessary for hydrocephalus.

Timing and outcomes of surgery depend on individual severity and comorbidities. Early cleft palate repair in infancy or early childhood is standard; cataract surgery may be performed when visual impairment interferes with development. Orthopedic surgery is often delayed until skeletal maturity or when deformities compromise function severely. These interventions do not alter the underlying developmental disorder but significantly improve quality of life and functional capacity.

### 12.4 Supportive and Rehabilitative Care

Supportive care is the cornerstone of MEND syndrome management. Multidisciplinary teams including neurologists, dermatologists, orthopedic surgeons, ophthalmologists, cardiologists, geneticists, and rehabilitation specialists are essential. Physical therapy, occupational therapy, and speech therapy address motor skills, daily living activities, and communication, respectively.[18][19] Nutritional support ensures adequate growth and addresses feeding difficulties due to craniofacial anomalies or neurologic impairment. Psychological support for families and social services help navigate long‑term caregiving demands.

NCIT terms such as “Supportive Care” (NCIT:C16077), “Physical Therapy” (NCIT:C16087), “Occupational Therapy” (NCIT:C15278), and “Speech Therapy” (NCIT:C15376) describe these interventions. Cochrane Library and clinical guidelines for developmental disorders can inform best practices, though none are specific to MEND. Rehabilitation aims to maximize functional independence within the constraints imposed by structural anomalies and intellectual disability.

### 12.5 Treatment Outcomes and Personalized Strategies

Treatment response in MEND syndrome is symptom‑specific. AEDs can control seizures, but intellectual disability remains. Dermatologic therapies reduce scaling but do not cure ichthyosis. Surgical interventions correct anatomical defects but not the underlying developmental pathology.[11][18][19] Side effects and adverse events depend on specific treatments; AEDs carry risks of sedation and cognitive effects, surgeries carry operative risks, and topical agents may affect skin tolerance.

Personalized medicine approaches could eventually incorporate genotype‑guided management. For example, patients with severe EBP hypomorphic variants and high modifier burden might require more intensive neurologic and orthopedic monitoring. However, clinical evidence for such stratification is nascent. The Mexican modifier gene study suggests that genetic profiling could predict severity, but application in practice awaits replication and broader data.[8][16] For now, personalized care focuses on tailoring symptomatic management to individual needs rather than genotype‑based therapy.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of MEND syndrome, in the sense of preventing disease occurrence, is challenging due to its genetic basis. However, genetic counseling and reproductive options such as PGD and prenatal diagnosis provide avenues for preventing the birth of affected male offspring in families with known EBP variants.[15][18][19] Carrier identification in at‑risk females, followed by informed reproductive decision‑making, constitutes primary preventive action.

Secondary prevention involves early detection and intervention to reduce disease impact. Early recognition of MEND syndrome through clinical and genetic diagnosis enables prompt seizure management, surgical correction of structural defects, and initiation of developmental therapies, thereby mitigating complications and optimizing functional outcomes.[18][19] Newborns with collodion membrane and suspected syndromic ichthyosis should undergo thorough evaluation, including sterol profiling and genetic testing, to identify MEND or related conditions.

Tertiary prevention focuses on preventing complications in individuals with established disease. This includes proactive orthopedic management to prevent severe scoliosis, vigilant ophthalmologic surveillance for cataracts, regular cardiac monitoring, and comprehensive skin care to prevent infections.[11][18][19] Multidisciplinary follow‑up and rehabilitation reduce disability progression and improve quality of life.

### 13.2 Immunization, Screening, and Behavioral Interventions

Immunization strategies for MEND syndrome follow general pediatric guidelines; there is no disease‑specific vaccine. Ensuring up‑to‑date vaccinations prevents infections that could exacerbate neurologic or respiratory complications. Screening programs are focused on familial settings rather than population; carrier screening for EBP variants in maternal relatives and cascade testing in affected families are key.[15][18][19] Preimplantation and prenatal screening allow early detection in embryos and fetuses.

Behavioral interventions, including lifestyle modifications, have limited impact on primary disease pathology but are important for general health. Encouraging physical activity within the constraints of orthopedic and neurologic limitations promotes cardiovascular health and reduces secondary morbidity. Nutritional counseling ensures adequate intake despite feeding difficulties. Psychosocial support addresses stress and mental health in families.

### 13.3 Genetic Counseling and Public Health Considerations

Genetic counseling is essential for families affected by MEND syndrome. Counselors explain X‑linked recessive inheritance, carrier risks, recurrence probabilities, and reproductive options.[15][18][19] They also discuss implications for extended family members and coordinate testing. NSGC, ACMG, and GeneReviews resources for X‑linked disorders inform counseling practices, even though specific MEND guidelines are not yet formalized.

Public health interventions specific to MEND syndrome are minimal due to its rarity. However, awareness among dermatologists, neurologists, and geneticists can improve recognition of sterol biosynthesis disorders, facilitating timely diagnosis and management. Environmental interventions are not directly relevant, given the genetic etiology, though broad environmental health measures benefit overall patient health.

## 14. Other Species and Natural Disease

### 14.1 Species Affected and Orthologous Genes

Orthologs of EBP exist in many species, including mice, yeast, and other vertebrates. In mice, the Ebp gene encodes a protein with sterol isomerase activity analogous to human EBP.[17] Derry et al. identified the Tattered (Td) mouse as harboring an Ebp mutation, linking it to skeletal and sterol phenotypes reminiscent of CDPX2.[17] Yeast studies originally characterized EBP’s delta(8)–delta(7) sterol isomerase activity by expressing mammalian EBP in yeast, demonstrating functional conservation.[17]

NCBI Taxon identifiers for relevant species include taxon ID 10090 for Mus musculus (mouse) and 4932 for Saccharomyces cerevisiae (yeast). Orthologous genes can be traced via NCBI Gene and HomoloGene. These models provide comparative biology insights into sterol biosynthesis and its developmental roles.

### 14.2 Natural Disease in Animals and Comparative Pathology

Naturally occurring Ebp‑related disease in animals has been documented in the Tattered mouse, which shows skeletal stippling and sterol abnormalities similar to CDPX2.[17] Veterinary relevance of such models lies more in their utility for human disease research than in animal health per se, as such mutations are engineered or discovered in laboratory strains rather than common in companion animals or livestock.

Comparative pathology across species highlights similarities in phenotypes arising from sterol biosynthesis defects. In both mice and humans, Ebp mutations cause skeletal anomalies, skin abnormalities, and sterol accumulation. Differences lie in species‑specific developmental patterns and lifespan. Evolutionary conservation of EBP function underscores the gene’s fundamental role in sterol metabolism.

Transmission of MEND syndrome across species is not applicable; the condition is genetic and non‑infectious. Zoonotic potential is nil, and cross‑species susceptibility relates only to engineered or spontaneous mutations in orthologous genes.

## 15. Model Organisms

### 15.1 Mouse Models: Tattered (Td) and Ebp Mutants

Mouse models have been pivotal in elucidating EBP function and related pathophysiology. The Tattered (Td) mouse, described by Derry et al., carries a mutation in the Ebp gene resulting in an amino acid substitution (Arg107Gly), leading to skeletal stippling, abnormal sterol profiles, and phenotypes similar to human CDPX2.[17] All Td mice showed a single nucleotide substitution at position 454, a G‑to‑A transition resulting in this substitution, confirming the causative role of Ebp.[17] Plasma and tissue sterol analysis in Td mice revealed increased 8‑dehydrocholesterol and 8(9)‑cholestenol, paralleling human EBP‑related disorders.[14][17]

While Td mice model CDPX2 more directly than MEND, they illustrate the consequences of Ebp dysfunction and provide a platform for studying developmental roles of sterols. Knock‑in models with specific hypomorphic Ebp alleles analogous to MEND‑associated variants could, in principle, recapitulate MEND phenotypes more closely, though such models have not been explicitly described. The mouse offers a mammalian context to investigate neurological, skeletal, and dermatologic effects of sterol biosynthesis defects, as well as potential therapeutic strategies.

Phenotype recapitulation in Td mice is partial relative to MEND, as mice and humans differ in developmental anatomy and gene dosage effects. Nevertheless, skeletal anomalies and sterol profiles are robustly reproduced. Limitations include difficulty modeling intellectual disability and complex human neurologic phenotypes.

### 15.2 Yeast and In Vitro Models

Yeast models have been used to characterize EBP’s sterol isomerase activity. Hanner et al. demonstrated that emopamil‑binding protein exhibits delta(8)–delta(7) sterol isomerase activity in yeast, confirming its enzymatic function.[17] Yeast strains expressing EBP can be used to test variant effects on sterol conversion, offering a tractable system for functional assays. In vitro cell lines expressing wild‑type and mutant EBP in mammalian cells could similarly assess sterol metabolism and membrane effects, though such models have not been widely reported for MEND‑specific variants.

Cellular models enable detailed study of subcellular localization, interaction with other metabolic enzymes, and response to pharmacologic agents. They are limited, however, in modeling complex developmental phenotypes. Nevertheless, in vitro systems remain valuable for mechanistic research and variant classification.

### 15.3 Applications and Future Directions for Models

Model organisms and cellular systems contribute to understanding MEND syndrome by elucidating EBP function, sterol metabolism, and developmental pathways. Mouse models can be used to explore the impact of modifier genes, mimicking the human scenario described by Barboza‑Cerda et al.[8][16] Functional genomics screens (e.g., CRISPR or RNAi) in cell lines could identify pathways that modulate EBP deficiency effects, offering potential therapeutic targets.

Future directions include creating humanized mouse models carrying specific MEND‑associated EBP variants and studying multi‑organ phenotypes. Single‑cell transcriptomics in such models could reveal cell‑type‑specific mechanisms. Integration of model organism data with human clinical observations would strengthen causal chains from gene to phenotype.

## Conclusion

MEND syndrome, or male EBP disorder with neurologic defects, is an ultra‑rare X‑linked recessive sterol biosynthesis disorder caused by hypomorphic variants in the emopamil‑binding protein gene, resulting in a complex multisystem phenotype dominated by dermatologic, neurologic, craniofacial, skeletal, and ocular anomalies.[15][17][18][19] Pathophysiologically, EBP dysfunction impairs delta(8)–delta(7) sterol isomerase activity in the endoplasmic reticulum, leading to accumulation of intermediate sterols such as 8‑dehydrocholesterol and 8(9)‑cholestenol and relative deficiency of cholesterol in key tissues.[14][17][18] This metabolic block disrupts membrane composition and developmental signaling pathways, notably hedgehog and related morphogens, producing structural malformations and functional impairments. The disease’s clinical expression varies widely in severity and spectrum, influenced by both the nature of the EBP variant (hypomorphic vs null) and the genetic background in cholesterol homeostasis genes such as APOA5, ABCA1, and APOB.[8][16][18]

Diagnostics rely on clinical recognition of the characteristic phenotype, sterol profiling demonstrating elevated intermediate sterols, and genetic testing confirming EBP mutations.[11][14][15][18] Differentiation from related conditions such as CDPX2 and other sterol biosynthesis disorders is critical and facilitated by inheritance pattern, mosaicism status, and specific biochemical and skeletal features.[14][17][19] Treatment is currently supportive and symptomatic, encompassing antiepileptic therapy, dermatologic care, surgical correction of structural anomalies, and rehabilitation, with no disease‑modifying pharmacologic or gene‑based interventions available.[11][18][19] Genetic counseling, carrier detection, and reproductive options such as PGD and prenatal diagnosis provide avenues for preventing recurrence in affected families.[15][18][19]

Research on MEND syndrome, though limited by its rarity, has yielded important mechanistic insights through human case studies, mouse models, and yeast systems, clarifying EBP’s role in cholesterol biosynthesis and developmental biology.[14][17][18] The identification of modifier genes in cholesterol homeostasis pathways opens a frontier in understanding variable expressivity and suggests that polygenic background can modulate Mendelian disease severity.[8][16] Future work integrating multi‑omics profiling, advanced structural modeling, and model organism experimentation could further elucidate pathophysiology and pave the way for targeted therapies. For now, MEND syndrome stands as a paradigmatic example of how a single gene defect in a fundamental metabolic pathway can produce a broad and intricate spectrum of human developmental disease, emphasizing the need for integrative, multidisciplinary care and research approaches.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 118 |
| Resolved | 111 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 3 |
| Unverifiable | 2 |
| Terms whose name was checked | 53 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 26 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C34735` (1 mention) - the report calls it "Ichthyosis"; NCIT calls it **Intraoperative Complication**
- `NCIT:C49288` (1 mention) - the report calls it "Skin Care Management"; NCIT calls it **AS04 Adjuvant**
- `NCIT:C288` (2 mentions) - the report calls it "Antiepileptic Agent"; NCIT calls it **Azacitidine**
- `NCIT:C20253` (1 mention) - the report calls it "Developmental Disability Services"; NCIT calls it **ES05**
- `NCIT:C15382` (1 mention) - the report calls it "Neurosurgical Procedure"; NCIT calls it **Gamma Knife**
- `NCIT:C15273` (1 mention) - the report calls it "Orthopedic Surgery"; NCIT calls it **Longitudinal Study**
- `NCIT:C50775` (1 mention) - the report calls it "Spinal Fusion Surgery"; NCIT calls it **Tissue Failure**
- `NCIT:C96681` (1 mention) - the report calls it "Cleft Palate Repair"; NCIT calls it **Inhibin B Measurement**
- `NCIT:C96116` (1 mention) - the report calls it "Cataract Extraction"; NCIT calls it **Continuous Thread Plastic Container Closure**
- `NCIT:C50979` (1 mention) - the report calls it "Cardiac Surgical Procedure"; NCIT calls it **ATR wt Allele**
- `NCIT:C51430` (1 mention) - the report calls it "Orchiopexy"; NCIT calls it **ADRB2 wt Allele**
- `NCIT:C91793` (1 mention) - the report calls it "Biomarker Test"; NCIT calls it **Tumor Protein 63**
- `NCIT:C120726` (1 mention) - the report calls it "Sterol Measurement"; NCIT calls it **Mean Residence Time to Last Nonzero Concentration by Extravascular Dose**
- `UBERON:0001741` (1 mention) - the report calls it "anterior fontanelle"; UBERON calls it **corniculate cartilage**
- `UBERON:0001480` (1 mention) - the report calls it "toe"; UBERON calls it **proximal carpal bone**
- `NCIT:C78209` (1 mention) - the report calls it "Biochemical Test"; NCIT calls it **Ability**
- `NCIT:C16510` (1 mention) - the report calls it "Electron Microscopy"; NCIT calls it **DNA Polymerase Alpha**
- `NCIT:C17584` (1 mention) - the report calls it "Genetic Testing"; NCIT calls it **Forkhead Box Protein G1**
- `NCIT:C18102` (1 mention) - the report calls it "Carrier Testing"; NCIT calls it **Physical Phenomenon or Property**
- `NCIT:C97078` (1 mention) - the report calls it "Prenatal Diagnosis"; NCIT calls it **Reactive Lymphoid Hyperplasia**
- `NCIT:C16295` (1 mention) - the report calls it "Preimplantation Genetic Diagnosis"; NCIT calls it **Antibody**
- `NCIT:C113729` (1 mention) - the report calls it "Cascade Genetic Testing"; NCIT calls it **Grade B**
- `NCIT:C16077` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Clinical Trials Database**
- `NCIT:C16087` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Animal Testing**
- `NCIT:C15278` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Modified Radical Mastectomy**
- `NCIT:C15376` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Transcendental Meditation Therapy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0006513` (1 mention) - HP does not contain this term
- `HP:0003432` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006082` (obsolete organic acid metabolic process) (1 mention) - replaced by `GO:0008152`
- `UBERON:0002312` (UBERON_0002312) (1 mention) - replaced by `UBERON:0004082`
- `NCIT:C18102` (Physical Phenomenon or Property) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006082` (1 mention) - the report calls it "organic acid metabolic process"; GO calls it **obsolete organic acid metabolic process**
- `GO:0007229` (1 mention) - the report calls it "hedgehog signaling pathway"; GO calls it **integrin-mediated signaling pathway**
- `NCIT:C16810` (1 mention) - the report calls it "Magnetic Resonance Imaging"; NCIT calls it **Magnetic Resonance Spectroscopy**
- `NCIT:C101294` (1 mention) - the report calls it "Whole Exome Sequencing"; NCIT calls it **Whole Genome Sequencing**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.