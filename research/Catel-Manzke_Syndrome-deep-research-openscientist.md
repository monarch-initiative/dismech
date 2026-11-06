---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-06T19:36:54.963790'
end_time: '2026-11-06T20:29:19.625671'
duration_seconds: 3144.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Catel-Manzke Syndrome
  mondo_id: MONDO:0014507
  category: Mendelian
  causal_genes: TGDS
  omim_id: OMIM:302380, OMIM:616145
  synonyms: Catel Manzke Syndrome; Palatodigital syndrome, Catel-Manzke type; Pierre
    Robin sequence-hyperphalangy-clinodactyly syndrome; Pierre Robin syndrome-hyperphalangy-clinodactyly
    syndrome; hyperphalangy-clinodactyly of index finger with Pierre Robin syndrome;
    index finger anomaly-Pierre Robin syndrome; micrognathia digital syndrome
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 10
  validator_version: 0.5.1
term_validation:
  total_terms: 42
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 0
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0014507
    reported_labels:
    - MONDO
    ontology_label: Catel-Manzke syndrome
  - term_id: HP:0000347
    reported_labels:
    - Physical/skeletal
    ontology_label: Micrognathia
  - term_id: HP:0000162
    reported_labels:
    - Physical
    ontology_label: Glossoptosis
  - term_id: HP:0000175
    reported_labels:
    - Physical
    ontology_label: Cleft palate
  - term_id: HP:0000201
    reported_labels:
    - Composite
    ontology_label: Pierre-Robin sequence
  - term_id: HP:0001382
    reported_labels:
    - Connective tissue
    ontology_label: Joint hypermobility
  - term_id: HP:0001999
    reported_labels:
    - Craniofacial
    ontology_label: Abnormal facial shape
  - term_id: HP:0000767
    reported_labels:
    - Skeletal
    ontology_label: Pectus excavatum
  - term_id: NCIT:C15329
    reported_labels:
    - Surgery
    - Medical/surgical correction of congenital heart defects
    ontology_label: Surgical Procedure
  - term_id: NCIT:C15300
    reported_labels:
    - Nutritional Support
    ontology_label: Photodynamic Therapy
  - term_id: NCIT:C15317
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Second-Look Surgery
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Catel-Manzke_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Catel-Manzke_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Catel-Manzke Syndrome
- **MONDO ID:** MONDO:0014507 (if available)
- **Causal gene(s):** TGDS
- **OMIM:** OMIM:302380, OMIM:616145
- **Synonyms:** Catel Manzke Syndrome; Palatodigital syndrome, Catel-Manzke type; Pierre Robin sequence-hyperphalangy-clinodactyly syndrome; Pierre Robin syndrome-hyperphalangy-clinodactyly syndrome; hyperphalangy-clinodactyly of index finger with Pierre Robin syndrome; index finger anomaly-Pierre Robin syndrome; micrognathia digital syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Catel-Manzke Syndrome** covering all of the
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

# Catel-Manzke Syndrome (MONDO:0014507): A Comprehensive Disease Characteristics Report

## Summary

**Catel-Manzke syndrome (CMS)** is a rare autosomal-recessive skeletal dysplasia caused by **biallelic loss-of-function variants in *TGDS*** (TDP-glucose 4,6-dehydratase; HGNC:20324; chromosome 13q32.1, minus strand; UniProt O95455). The disease is defined by the combination of two cardinal features: **Pierre Robin sequence** (micrognathia, glossoptosis, and cleft palate) and a **pathognomonic bilateral hyperphalangy of the index fingers** produced by an accessory ossification center/bone between the second metacarpal and proximal phalanx — a malformation historically termed **Manzke dysostosis**, which causes radial deviation at the metacarpophalangeal joint and ulnar clinodactyly. Approximately 40 patients have been reported. Additional recurrent features include congenital heart defects, joint hyperextensibility/laxity, characteristic facial features, and, in a subset, short stature. Key identifiers are OMIM:616145 (TGDS-related, autosomal recessive; the historical OMIM:302380 entry predates gene discovery), Orphanet ORPHA:1388, and MONDO:0014507.

The molecular mechanism was substantially clarified in 2025. TGDS is an **endoplasmic-reticulum–localized, NAD-dependent UDP-D-glucose 4,6-dehydratase (EC 4.2.1.76)** of the short-chain dehydrogenase/reductase (SDR) family. Rather than acting as a classical biosynthetic workhorse, TGDS produces **UDP-4-keto-6-deoxyglucose**, an "enzyme-rescue metabolite" that mimics the reaction intermediate of the enzyme **UXS1** (UDP-xylose synthase / UDP-glucuronate decarboxylase) and regenerates the essential cofactor **NAD⁺** within the UXS1 catalytic pocket, completing UXS1's catalytic cycle. Loss of TGDS deprives UXS1 of this rescue metabolite, inactivating UXS1, reducing UDP-xylose and the downstream synthesis of **sulfated glycosaminoglycans/proteoglycans** that are crucial for cartilage and skeletal development. This causal chain is supported in vitro and in vivo, including a zebrafish *tgds* knockout that reproduces craniofacial cartilage defects with decreased sulfated glycosaminoglycan content.

Management is entirely **supportive and multidisciplinary** — there is no disease-modifying or gene-directed therapy. Priorities are neonatal airway and feeding management for the Robin sequence, surgical cleft-palate repair, cardiac evaluation and intervention, and selective hand surgery for the hyperphalangy. Prognosis depends largely on the severity of airway compromise and cardiac defects; survivors who pass the neonatal period generally have a favorable long-term outlook, though a severe end of the spectrum with respiratory failure and failure to thrive exists.

---

## Key Findings

### Finding 1 — Biallelic loss-of-function *TGDS* variants cause Catel-Manzke syndrome (autosomal recessive)

The causal gene for Catel-Manzke syndrome is ***TGDS***. In the landmark gene-discovery study, Ehmke et al. (2014) identified homozygous and compound-heterozygous *TGDS* mutations in **seven unrelated individuals with typical CMS** by exome sequencing: *"We describe the identification of homozygous and compound heterozygous mutations in TGDS in seven unrelated individuals with typical Catel-Manzke syndrome by exome sequencing"* [PMID: 25480037]. Six distinct variants were reported — c.892A>G (p.Asn298Asp), c.270_271del (p.Lys91Asnfs\*22), c.298G>T (p.Ala100Ser), c.294T>G (p.Phe98Leu), c.269A>G (p.Glu90Gly), and c.700T>C (p.Tyr234His). The breadth of amino-acid changes (missense, frameshift) led the authors to conclude a **loss-of-function mechanism**: *"Due to the spectrum of the amino acid changes, we suggest that loss of function in TGDS is the underlying mechanism of Catel-Manzke syndrome"* [PMID: 25480037]. Earlier clinical reports had already suggested autosomal-recessive inheritance based on consanguinity and affected sibs [PMID: 21834032].

**Evidence source type:** Human clinical / genetic (exome sequencing cohort).

### Finding 2 — Mechanism: TGDS produces an enzyme-rescue metabolite that sustains UXS1 activity and skeletal glycan synthesis

The 2025 study by Jacobs, Bommer et al. (*Nature* 646:218–226) resolved the long-standing puzzle of why loss of an apparently minor nucleotide-sugar enzyme causes a skeletal dysplasia. TGDS produces **UDP-4-keto-6-deoxyglucose**, described as *"a mimic of the reaction intermediate of the enzyme UXS1, which regenerates the essential cofactor NAD⁺ within the catalytic pocket of UXS1 by completing its catalytic cycle"* [PMID: 40836090]. The consequence of TGDS deficiency is that *"the inability to produce sufficient amounts of this enzyme-rescue metabolite leads to the inactivation of UXS1, impairing the synthesis of specific glycans that are crucial for skeletal development"* [PMID: 40836090]. This establishes a novel, non-canonical "enzyme-rescue metabolite" paradigm: TGDS does not feed a linear biosynthetic pathway directly, but instead keeps a second enzyme (UXS1) catalytically competent by maintaining its NAD⁺ redox state.

**Evidence source type:** In vitro + in vivo mechanistic study.

### Finding 3 — Core clinical phenotype: Pierre Robin sequence plus pathognomonic bilateral index-finger hyperphalangy (Manzke dysostosis)

CMS is clinically defined by *"Pierre Robin sequence and a unique form of bilateral hyperphalangy causing a clinodactyly of the index finger"* [PMID: 25480037]. The broader phenotypic spectrum includes *"hand anomalies, Robin sequence, cardiac defects, joint hyperextensibility, and characteristic facial features"* [PMID: 31833187]. The hallmark hand malformation is an accessory bone: patients present *"with the pathognomonic bilateral or unilateral hyperphalangy caused by an accessory bone between the second metacarpal and proximal phalanx known as Manzke dysostosis"* [PMID: 31833187]. Phenotypic variability is well documented — patients have been reported **without radiologic hyperphalangy** (while retaining mild radial deviation and ulnar clinodactyly) [PMID: 31769200] and **without Manzke dysostosis** [PMID: 31833187], and disproportionate short stature — not classically part of CMS — has been described in TGDS-confirmed patients [PMID: 31769200].

**Evidence source type:** Human clinical (case series and cohort reports).

### Finding 4 — Genetic heterogeneity and differential diagnosis of the Catel-Manzke / hyperphalangy phenotype

*TGDS* is **not** causative in every clinically diagnosed CMS patient: *"Mutations in TGDS have been identified as one cause of Catel-Manzke syndrome, but cannot be found as causative in every patient with the clinical diagnosis"* [PMID: 31923704]. Several genes produce Catel-Manzke–like phenotypes and constitute the molecular differential diagnosis:

- **IMPAD1** (gPAPP-type chondrodysplasia): *"We identified two homozygous loss-of-function IMPAD1 mutations in the two Catel-Manzke like patients (p.Arg187X and p.Ser108ArgfsX48)"* [PMID: 22887726].
- **KYNU** (kynureninase deficiency / NAD-deficiency syndrome with hand hyperphalangism): *"we present unrelated patients identified with biallelic variants in KYNU leading to kynureninase deficiency and xanthurenic aciduria"* [PMID: 31923704].
- **CANT1** (Desbuquois dysplasia type 1) and **Temtamy preaxial brachydactyly** overlap clinically.
- **DNAH10** was proposed as a candidate in one Catel-Manzke–like patient, though with caution given divergent gene function [PMID: 26420031].

Notably, both the KYNU-related disorder (NAD metabolism) and the TGDS mechanism (NAD⁺ regeneration in UXS1) converge on **NAD(H) cofactor biology**, an intriguing mechanistic thread across the differential.

**Evidence source type:** Human clinical / genetic.

### Finding 5 — Zebrafish *tgds* model recapitulates CMS craniofacial/cartilage defects via reduced sulfated glycosaminoglycans

Coppola et al. (*FEBS J* 2026, 293:2248–2269) characterized the zebrafish *tgds* ortholog. Recombinant zebrafish Tgds has **UDP-D-glucose 4,6-dehydratase (EC 4.2.1.76)** activity (the first step of L-rhamnose biosynthesis in lower eukaryotes), and the gene shows conserved biphasic developmental expression. Critically, *"CMS-associated mutations in conserved residues significantly impair enzyme activity and stability"* [PMID: 41159851], functionally confirming loss of function at the enzyme level. CRISPR/Cas9 F0 knockout produced developmental defects including *"craniofacial cartilage alterations, associated with a decrease in sulfate glycosaminoglycan content, mirrored some skeletal features observed in humans with CMS"* [PMID: 41159851] — directly linking the molecular lesion to reduced sulfated GAGs and the cartilage phenotype.

**Evidence source type:** Model organism (zebrafish) + in vitro enzymology.

### Finding 6 — p.Ala100Ser (c.298G>T) is a recurrent/founder allele; severity is variable, including a severe end

Pferdehirt et al. (2015) reported a 12-month-old male **homozygous for p.Ala100Ser** with molecularly confirmed CMS, presenting with Pierre Robin sequence (notably **without cleft palate**) and hyperphalangy. This patient lay at the severe end of the spectrum: *"Our patient is on the severe end of the phenotypic spectrum, presenting with respiratory complications and failure to thrive"* [PMID: 26366375]. The recurrence of this allele supports its status as a common CMS mutation: *"our finding of a homozygous p.Ala100Ser pathogenic variant in our patient supports that it is a common mutation in Catel-Manzke syndrome"* [PMID: 26366375], consistent with the founder-allele status established by haplotype reconstruction in the original cohort [PMID: 25480037].

**Evidence source type:** Human clinical.

### Finding 7 — TGDS is an ER-localized NAD-dependent UDP-D-glucose 4,6-dehydratase; disease variants cluster at the active/substrate-binding site

UniProt O95455 gives the official RecName **"UDP-D-glucose 4,6-dehydratase" (EC 4.2.1.76)**, AltName dTDP-D-glucose 4,6-dehydratase, with subcellular localization to the **endoplasmic reticulum** (keywords: Endoplasmic reticulum, Golgi apparatus, Lyase, NAD, Disease variant). Catalytic/active-site residues are annotated at positions 143, 144, and 166, with substrate/cofactor binding residues including 28, 29, 50, 53, 55, 76, 77, 98, 102, 170, and 196. TGDS belongs to the **SDR family**: *"TGDS (dTDP-D-glucose 4,6-dehydrogenase) is a conserved protein belonging to the SDR family and probably plays a role in nucleotide sugar metabolism"* [PMID: 25480037]. Disease missense variants cluster near the catalytic/substrate-binding pocket — p.Phe98Leu and p.Ala100Ser lie adjacent to binding residue 98, and the atypical fetal variant p.Asp299Asn was shown to be *"located in the predicted substrate binding site of TGDS"* [PMID: 28422407]. This spatial clustering provides a structural rationale for loss of enzyme function.

**Evidence source type:** Computational / protein database (UniProt) + human clinical variant mapping.

### Finding 8 — SOX9-regulated mandibular chondrogenesis links the TGDS/glycan defect to the Pierre Robin branch

Al-Qattan & Almohrij (2022) reviewed the pathogenesis of syndromic Pierre Robin sequence through SOX9: *"SOX9 is the main positive regulator in the development of the mandibular cartilage and it also enhances collagen type II (the main collagen type in cartilage) expression in the mandibular cartilage"* [PMID: 35415063]. The review situates CMS within a SOX9-interaction framework for PRS, listing *"interactions with collagen type II (in Strickler syndrome), exon junction complex (in Richier-Costa-Periera syndrome), glucose (in Catel-Manzke syndrome)"* [PMID: 35415063]. This connects the TGDS glycan/nucleotide-sugar defect to SOX9-dependent mandibular cartilage development — the developmental substrate for the micrognathia that initiates the Robin sequence.

**Evidence source type:** Human / review (developmental biology synthesis).

### Finding 9 — gnomAD confirms c.298G>T (p.Ala100Ser) as the dominant founder allele; all CMS variants are rare

Population-frequency analysis (gnomAD v2.1, GRCh37) shows **c.298G>T p.Ala100Ser** at exome AF = 3.34×10⁻⁴ (AC = 69) and genome AF = 4.14×10⁻⁴ — by far the most frequent pathogenic allele, quantitatively corroborating its founder status. Other reported pathogenic variants are ~10–40× rarer: c.700T>C p.Tyr234His AF = 1.19×10⁻⁵ (AC = 3); c.895G>A p.Asp299Asn AF = 8.4×10⁻⁶ (AC = 2); c.270_271del p.Lys91Asnfs\*22 AF = 1.85×10⁻⁵ (AC = 4); c.269A>G p.Glu90Gly AF = 2.32×10⁻⁵ (AC = 5); c.294T>G p.Phe98Leu is absent from gnomAD. No homozygotes for pathogenic alleles are reported in the (healthy) gnomAD population, consistent with a severe recessive disorder. The founder status was originally established by haplotype reconstruction: *"By using haplotype reconstruction we showed that the mutation c.298G>T is probably a founder mutation"* [PMID: 25480037].

**Evidence source type:** Population genetics (gnomAD) + human clinical.

---

## Comprehensive Section-by-Section Report

### 1. Disease Information

Catel-Manzke syndrome is a rare, congenital, autosomal-recessive dysostosis/skeletal dysplasia first delineated clinically in the 1970s (Catel; Manzke) and molecularly solved in 2014. It couples **Pierre Robin sequence** with **Manzke dysostosis** (bilateral index-finger hyperphalangy). Information is drawn predominantly from **aggregated disease-level resources and small clinical case series/cohorts** (OMIM, Orphanet, HPO, and ~40 published patients) rather than large EHR datasets, reflecting its rarity.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014507 |
| OMIM | 616145 (TGDS, autosomal recessive); 302380 (historical, pre-gene) |
| Orphanet | ORPHA:1388 |
| Gene (HGNC) | TGDS, HGNC:20324 |
| UniProt | O95455 |
| ICD-10 | Q87.0 (congenital malformation syndromes predominantly affecting facial appearance) — closest mapping |
| MeSH | Indexed under congenital/craniofacial anomalies |

**Synonyms:** Catel-Manzke syndrome; Palatodigital syndrome, Catel-Manzke type; Pierre Robin sequence–hyperphalangy–clinodactyly syndrome; hyperphalangy-clinodactyly of index finger with Pierre Robin syndrome; index finger anomaly–Pierre Robin syndrome; micrognathia-digital syndrome.

### 2. Etiology

**Primary cause — genetic.** CMS is a monogenic Mendelian disorder caused by biallelic (homozygous or compound-heterozygous) loss-of-function variants in *TGDS* [PMID: 25480037]. There is no established environmental, infectious, or teratogenic cause.

**Genetic risk factors.** The only established risk factor is **carriage of two pathogenic *TGDS* alleles**. **Consanguinity** increases risk of homozygosity for rare recessive alleles and was noted in early reports [PMID: 21834032]. The recurrent **founder allele c.298G>T (p.Ala100Ser)** elevates population-level risk in carriers [PMID: 25480037; gnomAD AF 3.3×10⁻⁴].

**Environmental risk factors / protective factors / gene–environment interactions.** None identified. As a fully penetrant recessive Mendelian disorder, CMS is not known to be modified by lifestyle, diet, toxins, or other environmental exposures. No protective alleles or modifier genes have been reported. (This content is **not applicable / not available** for CMS.)

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Frequency | Onset / severity |
|---|---|---|---|---|
| Micrognathia | Physical/skeletal | HP:0000347 | Very frequent (core) | Congenital; part of Robin sequence |
| Glossoptosis | Physical | HP:0000162 | Core (Robin seq) | Congenital |
| Cleft palate | Physical | HP:0000175 | Frequent (not obligate; absent in some) | Congenital |
| Pierre Robin sequence | Composite | HP:0000201 | Core | Neonatal |
| Index-finger hyperphalangy (Manzke dysostosis) | Skeletal | HP:0009811-related | Pathognomonic; variable | Congenital |
| Ulnar deviation/clinodactyly of index finger | Skeletal | HP:0040019 / HP:0004209-analogous | Core | Congenital |
| Radial deviation at MCP joint | Skeletal | HP:0009467-related | Core | Congenital |
| Congenital heart defect | Cardiac | HP:0001627 | Frequent | Congenital |
| Joint hyperextensibility/laxity | Connective tissue | HP:0001382 | Frequent | Congenital/early |
| Characteristic facial features | Craniofacial | HP:0001999 | Frequent | Congenital |
| Short / disproportionate short stature | Growth | HP:0004322 / HP:0003510 | Subset (TGDS-confirmed) | Childhood [PMID: 31769200] |
| Respiratory complications / failure to thrive | Systemic | HP:0002098 / HP:0001508 | Severe end of spectrum | Neonatal/infancy [PMID: 26366375] |
| Pectus excavatum | Skeletal | HP:0000767 | Reported | Early-onset [PMID: 37100424] |

**Onset:** congenital/neonatal for all cardinal features. **Severity:** variable — from mild (hyperphalangy without Robin-sequence complications) to severe (respiratory failure, failure to thrive) [PMID: 26366375]. **Progression:** the malformations are structural and **stable** (non-progressive); outcome is dictated by airway/cardiac complications and surgical correction. **Quality-of-life impact:** feeding and breathing difficulty in infancy, speech and dental impact from cleft palate, and hand-function limitation from the digital malformation; no disease-specific QoL instrument exists.

### 4. Genetic/Molecular Information

**Causal gene:** *TGDS* (TDP-glucose 4,6-dehydratase), HGNC:20324, chromosome 13q32.1 (minus strand); disease OMIM 616145. Encodes UniProt O95455, an SDR-family NAD-dependent dehydratase.

**Pathogenic variants (classification, type, frequency):**

| Variant (cDNA) | Protein | Type | gnomAD AF | Notes |
|---|---|---|---|---|
| c.298G>T | p.Ala100Ser | Missense | 3.34×10⁻⁴ (exome) | Founder allele; near binding residue 98 |
| c.294T>G | p.Phe98Leu | Missense | Absent | Binding-site region |
| c.269A>G | p.Glu90Gly | Missense | 2.32×10⁻⁵ | Active-site cluster |
| c.270_271del | p.Lys91Asnfs\*22 | Frameshift | 1.85×10⁻⁵ | LoF |
| c.700T>C | p.Tyr234His | Missense | 1.19×10⁻⁵ | — |
| c.892A>G | p.Asn298Asp | Missense | — | Original cohort |
| c.895G>A | p.Asp299Asn | Missense | 8.4×10⁻⁶ | Atypical fetal case; substrate-binding site [PMID: 28422407] |

**Classification:** pathogenic / likely pathogenic per ACMG (recurrent, functionally validated, segregating). **Functional consequence:** loss of function [PMID: 25480037; 41159851]. **Somatic vs germline:** germline. **Modifier genes / epigenetics / chromosomal abnormalities:** none established; CMS is not caused by copy-number or cytogenetic changes (karyotype/microarray normal). ClinVar lists ~240 TGDS variant records.

### 5. Environmental Information

**Not applicable.** No environmental, lifestyle, or infectious contributors have been identified. CMS is a purely genetic Mendelian disorder.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function variants in *TGDS*** (missense clustering at the active/substrate-binding site, or frameshift) **lead to** loss of TGDS enzymatic activity and protein stability [PMID: 25480037; 41159851].
2. Loss of TGDS activity **results in** failure to produce sufficient **UDP-4-keto-6-deoxyglucose**, the enzyme-rescue metabolite [PMID: 40836090].
3. Absence of this rescue metabolite **leads to** failure to regenerate **NAD⁺** within the catalytic pocket of **UXS1**, so UXS1 cannot complete its catalytic cycle and becomes **inactivated** [PMID: 40836090].
4. UXS1 inactivation **results in** reduced production of **UDP-xylose**, the obligatory initiator sugar for glycosaminoglycan (GAG) chain assembly on proteoglycan core proteins (downstream inference supported by the zebrafish GAG data) [PMID: 40836090].
5. Reduced UDP-xylose **leads to** impaired synthesis of **sulfated glycosaminoglycans/proteoglycans** crucial for cartilage extracellular matrix [PMID: 40836090; 41159851].
6. Deficient cartilage proteoglycan matrix **results in** abnormal **chondrogenesis**, which **branches** into:
   - **(a) Mandibular cartilage branch** → micrognathia → glossoptosis → (secondary) cleft palate = **Pierre Robin sequence**; this branch intersects **SOX9**-driven mandibular chondrogenesis [PMID: 35415063].
   - **(b) Appendicular/hand branch** → aberrant ossification producing the accessory bone between the 2nd metacarpal and proximal phalanx = **Manzke dysostosis / index-finger hyperphalangy** (mechanistic link to the GAG deficit inferred from the shared chondrogenesis defect and zebrafish craniofacial cartilage findings) [PMID: 41159851].

**Molecular pathways / biochemistry:** nucleotide-sugar metabolism; NAD⁺/NADH cofactor cycling; UDP-xylose → UDP-glucuronic acid → GAG (chondroitin/heparan sulfate) biosynthesis. **Enzymes:** TGDS (EC 4.2.1.76); UXS1 (UDP-glucuronate decarboxylase). **Subcellular compartments:** endoplasmic reticulum / Golgi (GO:0005783 endoplasmic reticulum; GO:0005794 Golgi apparatus). **Biological processes (GO):** nucleotide-sugar metabolic process (GO:0009225); glycosaminoglycan biosynthetic process (GO:0006024); proteoglycan biosynthetic process (GO:0030166); chondrocyte differentiation (GO:0002062); skeletal system development (GO:0001501); NAD metabolic process (GO:0019674). **Cell types (CL):** chondrocyte (CL:0000138); neural-crest-derived cranial cartilage cells; osteoblast (CL:0000062). **Upstream vs downstream:** TGDS loss is upstream; UXS1 inactivation and GAG deficiency are proximal downstream; cartilage/skeletal malformation is the terminal manifestation.

```
TGDS LoF ──► no UDP-4-keto-6-deoxyglucose ──► UXS1 can't regenerate NAD+ ──► UXS1 inactive
     │                                                                            │
     └──────────────────────────────────────────────► ↓ UDP-xylose ◄────────────┘
                                                        │
                                                        ↓ sulfated GAG / proteoglycan synthesis
                                                        │
                                   ┌────────────────────┴────────────────────┐
                                   ▼ (SOX9 mandibular cartilage)              ▼ (hand cartilage/ossification)
                         Micrognathia→glossoptosis→cleft palate        Manzke dysostosis / hyperphalangy
                              = PIERRE ROBIN SEQUENCE                   = index-finger clinodactyly
```

### 7. Anatomical Structures Affected

- **Organ/system level — primary:** craniofacial skeleton (mandible — UBERON:0001684), hands/digits (manus UBERON:0002398; phalanx UBERON:0001449), secondary palate (UBERON:0001716). **Secondary:** heart (UBERON:0000948; congenital heart defects); airway/pharynx (secondary to micrognathia/glossoptosis). **Body systems:** skeletal, craniofacial, cardiovascular, respiratory (secondary), connective tissue (joint laxity).
- **Tissue/cell level:** cartilage (UBERON:0002418) and its chondrocytes (CL:0000138); connective tissue (ligamentous laxity); bone/ossification centers.
- **Subcellular level:** endoplasmic reticulum (GO:0005783) and Golgi apparatus (GO:0005794) — sites of nucleotide-sugar synthesis and proteoglycan glycosylation.
- **Localization / lateralization:** hand findings are characteristically **bilateral** (occasionally unilateral); craniofacial findings are midline (mandible/palate).

### 8. Temporal Development

- **Onset:** congenital; cardinal features present at birth. Robin-sequence airway/feeding problems manifest **neonatally**; hyperphalangy becomes radiographically evident in infancy/early childhood.
- **Progression:** malformations are **structural and non-progressive (stable)**. Short stature, when present, becomes apparent across childhood [PMID: 31769200].
- **Course/duration:** lifelong structural condition; natural history is dominated by the early (neonatal/infant) critical window of airway and feeding risk. No remission concept; clinical improvement follows surgical/supportive intervention.
- **Critical period:** the **neonatal–infant period** is the window of greatest vulnerability (airway obstruction, feeding failure) and of greatest intervention opportunity.

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive [PMID: 25480037; 21834032].
- **Penetrance:** high/complete for biallelic LoF (no unaffected biallelic individuals observed; no pathogenic homozygotes in gnomAD).
- **Expressivity:** variable — from absence of hyperphalangy [PMID: 31769200] or Manzke dysostosis [PMID: 31833187] to severe respiratory failure/failure to thrive [PMID: 26366375].
- **Epidemiology:** very rare; ~40 reported patients. Prevalence/incidence not formally established (effectively <1/1,000,000).
- **Founder effect:** c.298G>T (p.Ala100Ser) is a founder allele [PMID: 25480037], the most common pathogenic variant (gnomAD exome AF 3.3×10⁻⁴).
- **Consanguinity:** contributes to homozygous cases [PMID: 21834032].
- **Carrier frequency / sex ratio / geographic distribution:** carrier frequency is low and dominated by the founder allele; no strong sex bias expected (autosomal); no defined endemic geography.

### 10. Diagnostics

- **Clinical recognition:** the combination of Pierre Robin sequence + bilateral index-finger hyperphalangy/clinodactyly is highly suggestive.
- **Imaging:** **hand radiographs** are central — they reveal the accessory ossification center/bone between the 2nd metacarpal and proximal phalanx (Manzke dysostosis) [PMID: 31833187]. Echocardiography for cardiac defects; skeletal survey as indicated.
- **Genetic testing (confirmatory):** **single-gene *TGDS* sequencing** or multigene skeletal-dysplasia/Robin-sequence panels; **whole-exome sequencing (WES)** is how the gene was discovered and remains high-yield, especially for atypical presentations [PMID: 25480037]. WGS and CMA add little for the point-mutation etiology (karyotype/microarray normal). Targeted testing for the founder allele p.Ala100Ser is an efficient first-tier.
- **Differential diagnosis (with distinguishing molecular features):** IMPAD1-related chondrodysplasia (gPAPP) [PMID: 22887726]; KYNU-related NAD-deficiency syndrome with hyperphalangism and xanthurenic aciduria [PMID: 31923704]; CANT1-related Desbuquois dysplasia type 1; Temtamy preaxial brachydactyly; DNAH10-candidate Catel-Manzke–like case [PMID: 26420031]. Urine organic acids (xanthurenic aciduria) help flag KYNU.
- **Screening:** no newborn-screening program; cascade carrier testing within affected families and genetic counseling are appropriate.

### 11. Outcome/Prognosis

- **Survival/mortality:** no disease-specific mortality statistics; outcome hinges on neonatal airway compromise and congenital heart defects. A **severe end of the spectrum** (respiratory complications, failure to thrive) exists [PMID: 26366375]. Children who are managed through the neonatal period generally have a favorable long-term structural prognosis.
- **Morbidity/function:** feeding and respiratory difficulty in infancy; cleft-palate-related speech/dental issues; hand-function limitation from digital malformation; joint laxity. Intellect is typically normal.
- **Complications:** airway obstruction, feeding failure, recurrent otitis/hearing issues (cleft palate), cardiac sequelae.
- **Prognostic factors:** severity of Robin-sequence airway obstruction and cardiac anomaly are the main determinants; genotype–phenotype correlation is incomplete (p.Ala100Ser homozygotes span mild to severe).

### 12. Treatment

**No disease-modifying or gene-directed therapy exists.** Management is supportive and multidisciplinary:

| Domain | Intervention | NCIT suggestion |
|---|---|---|
| Airway (Robin sequence) | Prone positioning, nasopharyngeal airway, mandibular distraction osteogenesis, tongue-lip adhesion, or tracheostomy in severe cases | NCIT:C15329 (Surgery) |
| Feeding | NG/gastrostomy feeding; specialized nutrition | NCIT:C15300 (Nutritional Support) |
| Cleft palate | Surgical palatoplasty | Cleft-palate repair |
| Cardiac | Medical/surgical correction of congenital heart defects | NCIT:C15329 |
| Hand | Selective reconstructive/orthopedic hand surgery for the hyperphalangy | Orthopedic surgery |
| Rehabilitation | Speech therapy, physical/occupational therapy | NCIT:C15317 (Rehabilitation Therapy) |

**Pharmacotherapy / pharmacogenomics / advanced therapeutics (gene, cell, RNA, targeted, immunotherapy):** none applicable. **Experimental trials:** none specific to CMS. **Personalized medicine:** limited to genotype confirmation and genetic counseling.

### 13. Prevention

- **Primary prevention:** not applicable (genetic, congenital). **Genetic counseling** for at-risk/consanguineous families is the principal preventive measure, with a **25% recurrence risk** per pregnancy for carrier couples.
- **Reproductive options:** **carrier/cascade testing**, **prenatal diagnosis** (targeted *TGDS* testing when familial variants are known; atypical CMS has been diagnosed in a fetus [PMID: 28422407]), and **preimplantation genetic testing**.
- **Secondary/tertiary prevention:** early neonatal airway/feeding management and cardiac surveillance to prevent complications. **Immunization / public-health / environmental prevention:** not applicable.

### 14. Other Species / Natural Disease

- **Orthologs / comparative biology:** TGDS orthologs are functionally conserved. The **zebrafish** (*Danio rerio*; NCBI Taxon:7955) *tgds* ortholog encodes an active UDP-D-glucose 4,6-dehydratase and models the disease [PMID: 41159851]. A ***Caenorhabditis elegans*** (NCBI Taxon:6239) homolog, **bus-5**, *"is homologous to human dTDP-D-glucose 4,6-dehydratase, which is implicated in Catel-Manzke syndrome,"* and its mutation affects surface glycosylation and cuticle integrity [PMID: 36911920] — underscoring deep evolutionary conservation of the enzyme's role in glycan biology.
- **Natural disease / veterinary relevance:** no naturally occurring companion-animal or wildlife CMS equivalent is documented (OMIA). **Zoonotic/transmission:** not applicable (non-infectious, genetic).

### 15. Model Organisms

- **Zebrafish (*Danio rerio*):** CRISPR/Cas9 F0 *tgds* knockout recapitulates craniofacial cartilage alterations with decreased sulfated GAG content, mirroring human CMS skeletal features; recombinant Tgds assays confirm CMS mutations impair activity/stability [PMID: 41159851]. **Phenotype recapitulation:** good for the cartilage/craniofacial and glycan-deficiency aspects. **Limitations:** zebrafish Tgds functions in L-rhamnose biosynthesis (a lower-eukaryote pathway), so the enzymatic context differs from the human UXS1-rescue mechanism; F0 mosaic knockouts carry inherent variability.
- **C. elegans (bus-5):** invertebrate model informative for the glycosylation/surface-coat role of the enzyme [PMID: 36911920], but not a skeletal-disease model.
- **Mammalian models:** no published mouse-knockout CMS phenotype was identified in this investigation (knowledge gap).
- **Resources:** ZFIN (zebrafish), WormBase (*C. elegans*), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

The central and most novel insight is that **CMS is not caused by loss of a biosynthetic end-product per se, but by loss of a catalytic "rescue" service**. TGDS's physiologically important output is **UDP-4-keto-6-deoxyglucose**, a transition-state/intermediate mimic that **re-primes UXS1's NAD⁺ cofactor**. UXS1 decarboxylates UDP-glucuronic acid to UDP-xylose — the first sugar laid down on proteoglycan core proteins. When TGDS fails, UXS1 stalls in an NADH-bound, catalytically dead state, UDP-xylose falls, and **sulfated proteoglycan synthesis in cartilage collapses**. Because the mandibular condylar cartilage (SOX9-dependent) and the developing hand skeleton both depend on proteoglycan-rich matrix, the defect manifests precisely as the two hallmark features — Pierre Robin sequence and Manzke dysostosis.

This model unifies several otherwise disparate observations: (i) the **SDR/NAD-dependent** nature of TGDS and its ER/Golgi localization; (ii) the **reduced sulfated GAGs** in the zebrafish knockout; (iii) the **convergence on NAD biology** shared with the KYNU differential diagnosis; and (iv) the **variant clustering** at the substrate/active site producing loss of function. The branch point at defective chondrogenesis cleanly separates the craniofacial (Robin) and appendicular (hyperphalangy) phenotypes while keeping a single upstream lesion.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [25480037](https://pubmed.ncbi.nlm.nih.gov/25480037/) | *Homozygous/compound-het mutations in TGDS cause CMS* | Gene discovery; LoF mechanism; founder allele; SDR family |
| [40836090](https://pubmed.ncbi.nlm.nih.gov/40836090/) | *A missing enzyme-rescue metabolite as cause of a rare skeletal dysplasia* | Core mechanism: TGDS→UDP-4-keto-6-deoxyglucose→UXS1 NAD⁺ rescue |
| [41159851](https://pubmed.ncbi.nlm.nih.gov/41159851/) | *Zebrafish as a model for CMS* | In vivo recapitulation; reduced sulfated GAGs; enzyme-LoF confirmation |
| [31833187](https://pubmed.ncbi.nlm.nih.gov/31833187/) | *CMS without Manzke dysostosis* | Phenotype spectrum; Manzke dysostosis / accessory bone |
| [31769200](https://pubmed.ncbi.nlm.nih.gov/31769200/) | *TGDS variants cause CMS without hyperphalangy* | Phenotype expansion; short stature |
| [26366375](https://pubmed.ncbi.nlm.nih.gov/26366375/) | *CMS further delineation* | p.Ala100Ser recurrence; severe end (respiratory failure, FTT) |
| [28422407](https://pubmed.ncbi.nlm.nih.gov/28422407/) | *Atypical CMS in a fetus* | p.Asp299Asn at substrate-binding site; prenatal context |
| [31923704](https://pubmed.ncbi.nlm.nih.gov/31923704/) | *Biallelic KYNU variants* | Genetic heterogeneity / differential diagnosis |
| [22887726](https://pubmed.ncbi.nlm.nih.gov/22887726/) | *IMPAD1 mutations in CMS-like patients* | Differential diagnosis |
| [26420031](https://pubmed.ncbi.nlm.nih.gov/26420031/) | *Exome in CMS-like, DNAH10 candidate* | Differential / candidate-gene caution |
| [35415063](https://pubmed.ncbi.nlm.nih.gov/35415063/) | *Pathogenesis of PRS through SOX9* | Links CMS to SOX9 mandibular chondrogenesis |
| [36911920](https://pubmed.ncbi.nlm.nih.gov/36911920/) | *C. elegans surface mutants* | Conserved ortholog (bus-5); glycosylation role |
| [21834032](https://pubmed.ncbi.nlm.nih.gov/21834032/) | *CMS autosomal recessive inheritance* | Early AR evidence; consanguinity |
| [37100424](https://pubmed.ncbi.nlm.nih.gov/37100424/) | *Early-onset pectus excavatum genetics* | CMS among genetic causes of early-onset PE |

---

## Limitations and Knowledge Gaps

1. **Small evidence base:** ~40 reported patients; no formal prevalence/incidence, survival, or validated QoL data. Natural-history data are anecdotal.
2. **Hand-phenotype mechanism is inferred:** the direct molecular link from UDP-xylose/GAG deficiency to the specific accessory ossification center (Manzke dysostosis) is plausible but not experimentally demonstrated at the cellular level.
3. **UXS1 rescue mechanism** is newly described (2025); independent replication and human-tissue confirmation in CMS patients remain limited.
4. **No mammalian (mouse) model** phenotype was identified — a gap for translational/preclinical work.
5. **Incomplete genotype–phenotype correlation:** the same founder allele (p.Ala100Ser) spans mild to severe presentations, implying unidentified modifiers or stochastic developmental factors.
6. **Citation verification flags:** two mechanism snippets (PMID:40836090) and two zebrafish/severity snippets were marked "mismatch" during automated validation; the substantive claims are consistent with the papers, but exact quotes should be re-verified against the published abstracts before database ingestion.
7. **Historical OMIM ambiguity:** OMIM 302380 predates gene discovery; annotations should be anchored to OMIM 616145 / *TGDS*.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional mouse *Tgds* knockout** (cartilage-specific, e.g., *Col2a1-Cre*) to test cartilage proteoglycan deficiency and recapitulate micrognathia/hyperphalangy in a mammal.
2. **Directly measure UXS1 activity, UDP-xylose, and sulfated GAG levels** in patient-derived chondrocytes/iPSC-chondrocytes to confirm the rescue-metabolite mechanism in human cells.
3. **Structural/enzymology studies:** co-crystallize UXS1 with UDP-4-keto-6-deoxyglucose and model each CMS missense variant against TGDS active-site residues 143/144/166 and binding residues 98/102 to refine genotype–activity relationships.
4. **Metabolite-supplementation rescue test:** determine whether supplying UDP-4-keto-6-deoxyglucose or a cell-permeable analog restores UXS1 activity — proof-of-concept for a future therapeutic avenue.
5. **Curate a patient registry** to establish prevalence, natural history, genotype–phenotype correlations, airway/cardiac outcomes, and standardized QoL metrics.
6. **Re-verify citation snippets** flagged as mismatches and finalize HPO/GO/CL/UBERON/NCIT ontology mappings for knowledge-base ingestion.

---

*Report compiled from 9 confirmed findings and 20 reviewed papers over 5 investigation iterations. Evidence types: human clinical/genetic, model organism (zebrafish, C. elegans), in vitro enzymology, and computational/database (UniProt, gnomAD, ClinVar).*


## Artifacts

- [OpenScientist final report](Catel-Manzke_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Catel-Manzke_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 14 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014507` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Catel-Manzke syndrome**
- `HP:0000347` (1 mention) - the report calls it "Physical/skeletal"; HP calls it **Micrognathia**
- `HP:0000162` (1 mention) - the report calls it "Physical"; HP calls it **Glossoptosis**
- `HP:0000175` (1 mention) - the report calls it "Physical"; HP calls it **Cleft palate**
- `HP:0000201` (1 mention) - the report calls it "Composite"; HP calls it **Pierre-Robin sequence**
- `HP:0001382` (1 mention) - the report calls it "Connective tissue"; HP calls it **Joint hypermobility**
- `HP:0001999` (1 mention) - the report calls it "Craniofacial"; HP calls it **Abnormal facial shape**
- `HP:0000767` (1 mention) - the report calls it "Skeletal"; HP calls it **Pectus excavatum**
- `NCIT:C15329` (2 mentions) - the report calls it "Surgery", "Medical/surgical correction of congenital heart defects"; NCIT calls it **Surgical Procedure**
- `NCIT:C15300` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Photodynamic Therapy**
- `NCIT:C15317` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Second-Look Surgery**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001627` (1 mention) - the report calls it "Cardiac"; HP calls it **Abnormal heart morphology**, and lists "Cardiac anomaly" among its other names
- `GO:0005783` (2 mentions) - the report calls it "Subcellular level:** endoplasmic reticulum"; GO calls it **endoplasmic reticulum**
- `UBERON:0002418` (1 mention) - the report calls it "Tissue/cell level:** cartilage"; UBERON calls it **cartilage tissue**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15329` - called "Surgery", "Medical/surgical correction of congenital heart defects"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `Taxon`.