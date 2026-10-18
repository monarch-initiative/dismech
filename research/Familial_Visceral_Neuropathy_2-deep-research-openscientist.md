---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:01:14.736889'
end_time: '2026-08-31T21:27:45.234199'
duration_seconds: 1590.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Visceral Neuropathy 2
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
citation_count: 5
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 11
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: MONDO:0030399
    reported_labels:
    - MONDO
    ontology_label: visceral neuropathy, familial, 2, autosomal recessive
  - term_id: HP:0003812
    reported_labels:
    - variable
    - Expressivity:** Variable across the broader NRG1/ERBB series
    ontology_label: Phenotypic variability
  - term_id: HP:0002580
    reported_labels:
    - Clinical sign
    ontology_label: Volvulus
  - term_id: HP:0000407
    reported_labels:
    - Lab/clinical
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001263
    reported_labels:
    - Behavioral/neuro
    ontology_label: Global developmental delay
  - term_id: HP:0001762
    reported_labels:
    - Physical
    ontology_label: Talipes equinovarus
  - term_id: HP:0002650
    reported_labels:
    - Physical
    ontology_label: Scoliosis
  - term_id: HP:0000054
    reported_labels:
    - Physical
    ontology_label: Micropenis
  - term_id: HP:0040171
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased serum testosterone concentration
  - term_id: HP:0002804
    reported_labels:
    - Physical
    ontology_label: Arthrogryposis multiplex congenita
  - term_id: NCIT:C157763
    reported_labels:
    - surgical procedure
    ontology_label: Metastatic Bladder Small Cell Neuroendocrine Carcinoma
  - term_id: NCIT:C15184
    reported_labels:
    - nutritional support
    ontology_label: Behavioral Intervention
  - term_id: NCIT:C1516
    reported_labels:
    - supportive care
    ontology_label: Lisofylline
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Visceral_Neuropathy_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Visceral_Neuropathy_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Visceral Neuropathy 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Visceral Neuropathy 2** covering all of the
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

# Familial Visceral Neuropathy 2 (VSCN2): Comprehensive Disease Characterization Report

**Disease:** Familial Visceral Neuropathy 2 (VSCN2)
**OMIM:** #619465 · **MONDO:** MONDO:0030399 · **Gene:** *ERBB2* (HER2, 17q12; MIM 164870; HGNC:3430)
**Category:** Mendelian (autosomal recessive neurocristopathy)
**Report date:** 2026-08-31

---

## Summary

Familial Visceral Neuropathy 2 (VSCN2; OMIM #619465) is an **ultra-rare autosomal recessive developmental neurocristopathy** caused by **biallelic loss-of-function variants in *ERBB2*** (HER2), the ligand-orphan but kinase-active partner of the neuregulin-1 (NRG1) receptor system. The disorder was defined in a single consanguineous Turkish family (a sister and brother) reported by Le et al. in 2021, who carried a homozygous kinase-domain missense variant, c.2129C>T; p.Ala710Val (A710V) in *ERBB2* (NM_004448.3). Functional assays showed this variant drastically reduces phosphorylation of both ERBB2 and its heterodimeric partner ERBB3, establishing loss of NRG1/ERBB signaling as the mechanistic root of disease [PMID: 33497358].

Because ERBB3 binds NRG1 with high affinity but is catalytically weak, and ERBB2 is a ligand orphan but a strong kinase, functional NRG1 signaling requires an **ERBB3/ERBB2 heterodimer**. Loss of ERBB2 kinase activity therefore cripples signaling that is essential for the survival, proliferation, and migration of **neural-crest-derived enteric neuronal progenitors and Schwann cell precursors** that colonize the gut. The clinical consequence is a gastrointestinal dysmotility syndrome spanning colonic **aganglionosis/hypoganglionosis** (Hirschsprung disease, HSCR) and **chronic intestinal pseudo-obstruction (CIPO)**, accompanied by **peripheral axonal neuropathy, bilateral facial paresis, sensorineural hearing loss, ptosis**, and additional musculoskeletal and endocrine features. Gut histology in affected individuals revealed aganglionosis, hypoganglionosis, and intestinal smooth-muscle abnormalities [PMID: 33497358].

VSCN2 sits within an **allelic/pathway series** built around the NRG1/ERBB axis: VSCN1 (OMIM #243180, *ERBB3*), VSCN2 (OMIM #619465, *ERBB2*), and the dominant VSCN3 (#609629); *ERBB3* also underlies Lethal Congenital Contractural Syndrome type 2 (LCCS2, #607598). As of 2026, VSCN2 remains a **single-family entity** with a gene–disease validity classification of LIMITED, and there is **no disease-specific therapy** — management is supportive and surgical (pull-through for aganglionosis, nutritional support for dysmotility) with genetic counseling for prevention.

---

## 1. Disease Information

**Overview.** VSCN2 is a congenital disorder of gastrointestinal motility caused by defective development of the enteric nervous system (ENS) and peripheral nervous system, arising from biallelic *ERBB2* dysfunction. It is a **neurocristopathy** — a disease of neural-crest-derived tissues — combining features of Hirschsprung disease, chronic intestinal pseudo-obstruction, and peripheral neuropathy [PMID: 33497358; PMID: 33720042].

**Key identifiers.**

| Resource | Identifier |
|----------|-----------|
| OMIM | #619465 — *Visceral neuropathy, familial, 2, autosomal recessive* |
| MONDO | MONDO:0030399 |
| Gene (OMIM) | *ERBB2* — MIM 164870 |
| HGNC | HGNC:3430 (*ERBB2*) |
| MedGen | Concept present for the disorder |
| Orphanet | No dedicated ORPHA code specific to type 2 (VSCN1 = ORPHA99811) |
| ICD-11 | No type-2-specific code (VSCN1 maps to DA90.2) |

**Synonyms / alternative names.** Visceral neuropathy, familial, 2, autosomal recessive; VSCN2. Gene aliases for *ERBB2*: HER2, NEU, CD340, HER-2, VSCN2.

**Data source type.** Information is derived from **aggregated disease-level resources** (OMIM, MONDO, GenCC, PanelApp) and a **primary case series of individual patients** (Le et al. 2021), not EHR-scale populations. The entire VSCN2 clinical picture derives from **two siblings** in one consanguineous Turkish family.

---

## 2. Etiology

**Disease causal factors.** VSCN2 is a **monogenic, autosomal recessive genetic disorder**. The primary cause is **biallelic loss-of-function of *ERBB2***, disrupting NRG1/ERBB signaling required for ENS and Schwann cell development. There is no infectious or environmental cause; it is a developmental (neurocristopathy) mechanism.

> *"Trio-exome sequencing led to the identification of biallelic variants in ERBB3 and ERBB2 in 8 individuals variably associating HSCR, CIPO, peripheral neuropathy, and arthrogryposis."* [PMID: 33497358]

**Genetic risk factors.** The sole established genetic risk factor is inheritance of **two loss-of-function *ERBB2* alleles**. In the index family, the causal variant is homozygous p.Ala710Val, a kinase-domain missense change absent from gnomAD. **Consanguinity** is a major contributing factor (parents were heterozygous carriers).

**Environmental risk factors.** None established. As a fully penetrant Mendelian developmental disorder in the reported family, environmental exposures are not implicated.

**Protective factors.** None reported. No protective alleles or environmental modifiers are known. (Given a single family, statistical assessment of modifiers is not possible.)

**Gene–environment interactions.** None documented for VSCN2. Mechanistically, the disorder is driven by developmental loss of a receptor tyrosine kinase pathway rather than gene–environment interplay.

---

## 3. Phenotypes

The full phenotype spectrum derives from the two Turkish siblings (Le et al. 2021, family 5) plus the broader ERBB3/ERBB2 case series. Onset is **congenital/pediatric**, and expressivity is **variable** (HP:0003812).

| Phenotype | Type | HPO term | Notes / frequency |
|-----------|------|----------|-------------------|
| Intestinal dysmotility / severe constipation | Clinical sign | HP:0002019 (constipation) | Core feature; irregular bowel evacuation |
| Colonic aganglionosis (Hirschsprung disease) | Pathology | HP:0002251 (aganglionic megacolon) | Rectal aganglionosis with submucosal nerve-fiber hyperplasia |
| Hypoganglionosis (above aganglionic segment) | Pathology | — | Present in gut histology |
| Chronic intestinal pseudo-obstruction (CIPO) | Clinical sign | HP:0002580 | Neurogenic dysmotility |
| Peripheral axonal neuropathy | Clinical sign | HP:0003477 (peripheral neuropathy) | Axonal type |
| Bilateral facial paresis | Clinical sign | HP:0007209 | Cranial nerve involvement |
| Sensorineural hearing loss | Lab/clinical | HP:0000407 | — |
| Ptosis (unilateral) | Physical | HP:0007687 / HP:0000508 | — |
| Hypotonia | Clinical sign | HP:0001252 | — |
| Mild developmental delay | Behavioral/neuro | HP:0001263 | — |
| Clubfeet / talipes | Physical | HP:0001762 | — |
| Scoliosis | Physical | HP:0002650 | — |
| Micropenis | Physical | HP:0000054 | Endocrine involvement |
| Low testosterone | Lab abnormality | HP:0040171 | — |
| Small nose / hypoplastic alae nasi | Physical | HP:0000160 / HP:0000389 | Facial dysmorphism |
| Arthrogryposis (broader series) | Physical | HP:0002804 | Seen in ERBB3 cases; part of NRG1/ERBB spectrum |

> *"biallelic variants in ERBB3 and ERBB2 in 8 individuals variably associating HSCR, CIPO, peripheral neuropathy, and arthrogryposis. Thorough gut histology revealed aganglionosis, hypoganglionosis, and intestinal smooth muscle abnormalities."* [PMID: 33497358]

**Severity/progression.** Severe, congenital-onset, chronic. GI dysmotility is life-limiting and requires lifelong management. **Quality-of-life impact:** major — chronic constipation/pseudo-obstruction, dependence on nutritional support/surgery, hearing and neuromuscular impairment. No formal EQ-5D/SF-36 data exist for this ultra-rare entity.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***ERBB2*** (HER2/NEU; 17q12; MIM 164870; HGNC:3430) — encodes a transmembrane EGF-family receptor tyrosine kinase.

**Pathogenic variant (index family).**

| Feature | Detail |
|---------|--------|
| Variant | c.2129C>T (NM_004448.3), p.Ala710Val (A710V) |
| Zygosity | Homozygous (consanguineous; parents heterozygous) |
| Location | Highly conserved residue within the tyrosine kinase domain |
| Type | Missense |
| Population frequency | Absent from gnomAD |
| Functional consequence | Loss of function — drastic decrease in phosphorylation of both ERBB2 and ERBB3 (Neuro-2a overexpression) |
| Origin | Germline |
| ACMG interpretation | Pathogenic / likely pathogenic in context (segregation + functional + absence from population) |

> *"The consequences of the identified variants were evaluated using quantitative real-time PCR (RT-qPCR) on patient-derived fibroblasts or immunoblot assays on Neuro-2a cells overexpressing WT or mutant proteins, revealing either decreased expression or altered phosphorylation of the mutant receptors."* [PMID: 33497358]

**Functional class.** Loss of function (reduced receptor phosphorylation/kinase output). No gain-of-function or dominant-negative mechanism in VSCN2 (in contrast to oncogenic *ERBB2* amplification/activating mutations in cancer).

**Related disorders / allelic series.**
- **VSCN1** — OMIM #243180, *ERBB3* (MIM 190151), autosomal recessive.
- **VSCN2** — OMIM #619465, *ERBB2*, autosomal recessive.
- **VSCN3** — OMIM #609629, autosomal dominant.
- **LCCS2** (Lethal Congenital Contractural Syndrome 2) — OMIM #607598, *ERBB3*.

**Modifier genes / epigenetics / chromosomal abnormalities.** None specifically established for VSCN2. *SOX10* directly activates *ERBB3* transcription via an intronic neural-crest enhancer (ERBB3_MCS6) — relevant to the shared regulatory network but not a documented VSCN2 modifier. No large-scale chromosomal abnormalities are implicated.

---

## 5. Environmental Information

**Environmental factors:** None known. **Lifestyle factors:** None applicable. **Infectious agents:** None — VSCN2 is a genetic developmental disorder with no infectious trigger. This section is **not applicable** to VSCN2 beyond noting that consanguinity (a demographic, not environmental, factor) increases recessive risk.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *ERBB2* loss-of-function variant (p.A710V, kinase domain)** → **leads to** a catalytically impaired ERBB2 receptor with drastically reduced autophosphorylation/trans-phosphorylation capacity [PMID: 33497358].
2. Because ERBB3 is ligand-binding but kinase-dead and ERBB2 is the kinase-active partner, impaired ERBB2 → **results in** failure of the **NRG1 → ERBB3/ERBB2 heterodimer** to trans-phosphorylate ERBB3 C-terminal tyrosines (Y1054–Y1328) [Reactome R-HSA-1227986].
3. Loss of ERBB3 phosphotyrosine docking sites → **results in** attenuated recruitment/activation of two downstream cascades (branch point):
   - **3a. PI3K → AKT survival arm** → normally phosphorylates/inhibits pro-apoptotic BAD, GSK3, FKHR-L1; its attenuation → **leads to** reduced survival of Schwann cell precursors and enteric progenitors [PMID: 11312610].
   - **3b. RAS → RAF → MEK → ERK (MAPK) proliferation/migration arm** → its attenuation → **leads to** impaired proliferation and migration of progenitors.
4. Reduced survival/proliferation/migration of **neural-crest-derived enteric neuronal progenitors and Schwann cell precursors (SCPs)** → **results in** failure of these cells to fully colonize the gut and populate peripheral nerves [PMID: 33720042].
5. Incomplete ENS colonization → **results in** **colonic aganglionosis (rectum) and hypoganglionosis** above the aganglionic segment, with compensatory submucosal nerve-fiber hyperplasia [PMID: 33497358].
6. Absent/atrophic enteric ganglia and smooth-muscle abnormalities → **lead to** loss of coordinated peristalsis → clinical **Hirschsprung disease / chronic intestinal pseudo-obstruction** (functional obstruction, severe constipation).
7. In parallel (branch), SCP/Schwann-cell deficiency along peripheral and cranial nerves → **leads to** **peripheral axonal neuropathy, bilateral facial paresis, sensorineural hearing loss, and ptosis**; neural-crest contributions to other structures → musculoskeletal/craniofacial and endocrine features (*inferred* from neural-crest biology and the broader ERBB3/ERBB2 series).

### Detail by category

- **Molecular pathways:** NRG1/ERBB receptor tyrosine kinase signaling → PI3K–AKT and RAS–MAPK (KEGG "ErbB signaling pathway"; Reactome "Signaling by ERBB2", R-HSA-1227986). cAMP/PKA potentiates NRG1-induced ERBB2/ERBB3 phosphorylation and both downstream arms.
- **Cellular processes:** Progenitor survival (anti-apoptosis via AKT→BAD), proliferation, and directed migration (via GRB2/SHC, PLCγ/Ca²⁺-calcineurin, FAK, Rac/Cdc42).
- **Protein dysfunction:** Loss of ERBB2 kinase output; the receptor pair is **asymmetric and complementary** — ERBB3 (high-affinity NRG1 binding, weak kinase) + ERBB2 (ligand-orphan, active kinase). A710V abolishes the kinase contribution.
- **Immune involvement:** Not implicated.
- **Tissue damage mechanism:** Developmental failure/hypoplasia of neural-crest derivatives (not oxidative/ischemic injury).
- **Molecular profiling:** Mouse single-cell RNA-seq confirmed *Erbb3*/*Erbb2* expression in **enteric neuronal progenitor cells**; a conditional *ErbB3*-deficient model revealed a primary role for ERBB3 in enteric progenitors [PMID: 33497358; PMID: 33720042].

> *"Experiments using mice revealed that Erbb3 and Erbb2 were expressed in enteric neuronal progenitor cells."* [PMID: 33720042]

> *"The cell type-specific ErbB3 and ErbB2 function was further analyzed in mouse single-cell RNA sequencing data and in a conditional ErbB3-deficient mouse model, revealing a primary role for ERBB3 in enteric progenitors."* [PMID: 33497358]

### ASCII schematic

```
   NRG1
     │ (binds)
     ▼
  ERBB3 ──heterodimer── ERBB2  ◄── p.A710V (kinase-dead) = VSCN2 lesion
  (kinase-weak)         (kinase-active)
     │  trans-phosphorylation of ERBB3 Y1054..Y1328
     ├───────────────┬──────────────────┐
     ▼               ▼
  PI3K→AKT        RAS→MAPK
  (survival)      (proliferation/migration)
     │               │
     └──────┬────────┘
            ▼
  Enteric progenitors + Schwann cell precursors
  (survive, proliferate, migrate, colonize gut/nerves)
            │  FAILS when ERBB2 kinase is lost
            ▼
  Aganglionosis / hypoganglionosis  +  peripheral neuropathy
  → HSCR / CIPO                      → facial paresis, hearing loss, ptosis
```

**GO term suggestions:** GO:0038128 (ERBB2 signaling pathway), GO:0007399 (nervous system development), GO:0048484 (enteric nervous system development), GO:0014010 (Schwann cell proliferation), GO:0043524 (negative regulation of neuron apoptotic process), GO:0016477 (cell migration).
**CL term suggestions:** CL:0011103 (enteric neuron), CL:0002375 (Schwann cell precursor), CL:0000333 (migratory neural crest cell).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Large intestine / colon and rectum (UBERON:0001155 colon; UBERON:0001052 rectum) — site of aganglionosis. Small and large bowel broadly in CIPO.
**Secondary / body systems:** Digestive system (UBERON:0001007), peripheral nervous system (UBERON:0000010), cranial nerves (facial nerve UBERON:0001647), inner ear/cochlea (sensorineural hearing loss; UBERON:0001846), musculoskeletal (spine, feet), and reproductive/endocrine (micropenis, low testosterone).

**Tissue/cell level:** Enteric ganglia within the myenteric (Auerbach; UBERON:0002439) and submucosal (Meissner; UBERON:0013529) plexuses; intestinal smooth muscle (UBERON:0001529); peripheral nerve Schwann cells. Cell populations: **enteric neurons and their progenitors (CL:0011103), Schwann cells / SCPs (CL:0002573 / CL:0002375)**, neural-crest-derived cells.

**Subcellular level:** Plasma membrane receptor tyrosine kinase complex (GO:0005886 plasma membrane; GO:0004714 transmembrane receptor protein tyrosine kinase activity). No mitochondrial/lysosomal defect implicated.

**Localization / lateralization:** GI involvement follows the aganglionic segment (distal colon/rectum). Facial paresis is **bilateral**; ptosis reported **unilateral**; overall a mixed lateralization pattern.

---

## 8. Temporal Development

- **Onset:** Congenital / neonatal–pediatric. GI dysmotility and HSCR features manifest early in life; developmental/craniofacial and neuromuscular features are present from birth.
- **Onset pattern:** Chronic, developmental (insidious progression of dysmotility complications).
- **Progression:** Chronic and lifelong. Enteric aganglionosis is a fixed developmental deficit; secondary complications (pseudo-obstruction, nutritional failure) can be progressive without intervention.
- **Course pattern:** Chronic-progressive with episodic pseudo-obstruction crises; not relapsing-remitting.
- **Remission:** No spontaneous remission; surgical management (pull-through) can relieve the aganglionic obstruction but does not cure the underlying neuropathy.
- **Critical periods:** The developmental window of neural-crest colonization of the gut (embryonic) is the mechanistically critical period — clinically not therapeutically accessible postnatally.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Homozygous causal variant in the consanguineous index family; heterozygous parents unaffected.
- **Penetrance:** Presumed complete in biallelic carriers (based on single family; formal penetrance estimate not possible).
- **Expressivity:** Variable across the broader NRG1/ERBB series (HP:0003812).
- **Consanguinity:** Central — the disorder was identified in a consanguineous Turkish family; consanguinity is the main route to homozygosity.
- **Founder effect / carrier frequency:** Not established; variant absent from gnomAD, so no population carrier frequency is defined.
- **Epidemiology:** **Ultra-rare** — VSCN2 remains a **single-family entity** as of 2026, with no additional ERBB2-specific families reported (2022–2026 literature review). No prevalence/incidence figures exist. Context: Hirschsprung disease overall has an incidence of ~1 in 5,000 live births, but VSCN2 is a vanishingly small molecular subset.
- **Demographics:** Reported in a Turkish family (one affected sister and one affected brother); sex ratio not meaningfully estimable (both sexes affected). Gene–disease validity: **LIMITED** (GenCC/PanelApp).

> *"The patients carried homozygous or heterozygous variants in ERBB3 or ERBB2, which encode transmembrane epidermal growth factor receptors that bind neuroregulin 1 (NRG1)."* [PMID: 33720042]

---

## 10. Diagnostics

**Molecular diagnosis (definitive):**
- **Whole-exome sequencing (WES)** — the method that established the diagnosis (trio/WES in Le et al. 2021). Trio design aids interpretation.
- **Whole-genome sequencing (WGS)** — useful for non-coding/structural variants when WES is negative.
- **Targeted NGS gene panels** for HSCR/CIPO/pediatric intestinal pseudo-obstruction (e.g., **Genomics England PanelApp panel 1217 includes *ERBB2***).
- **Single-gene *ERBB2* sequencing with segregation** (confirm parental heterozygosity).

> *"Trio-exome sequencing led to the identification of biallelic variants in ERBB3 and ERBB2."* [PMID: 33497358]

**Histopathology (cornerstone for the aganglionosis component):**
- **Rectal suction biopsy** — absence of ganglion cells with hypertrophied acetylcholinesterase (AChE)-positive cholinergic nerve trunks.
- **Calretinin immunohistochemistry** — loss of staining is characteristic of Hirschsprung disease (sensitivity ~80–100%, specificity ~99–100%).
- Full-thickness bowel biopsy in selected cases; findings include aganglionosis, hypoganglionosis, submucosal nerve-fiber hyperplasia, and smooth-muscle abnormalities.

**CIPO workup:** Exclude mechanical obstruction (CT/MRI); metabolic panel; endoscopy; GI scintigraphy; **antroduodenal/small-bowel manometry** (neuropathic pattern — abnormal migrating motor complex, non-propagated bursts); **anorectal manometry** (absent recto-anal inhibitory reflex in HSCR).

**Adjunct testing:** Nerve conduction studies/EMG (confirm axonal peripheral neuropathy); audiometry (sensorineural hearing loss); ophthalmologic assessment (ptosis).

**Differential diagnosis:** VSCN1 (*ERBB3*) and VSCN3; syndromic HSCR (e.g., *RET*, *EDNRB*, *SOX10* — Waardenburg–Shah); other causes of CIPO (myogenic vs neurogenic); mitochondrial neurogastrointestinal encephalomyopathy (MNGIE); LCCS2. Molecular testing distinguishes these.

**Screening:** Cascade carrier testing in the family; prenatal/preimplantation testing feasible once the familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** No formal survival statistics for this ultra-rare entity. Prognosis is driven by the severity of intestinal dysmotility; CIPO with intestinal failure carries substantial morbidity/mortality and may require long-term parenteral nutrition.
- **Morbidity / function:** High chronic morbidity — dependence on nutritional support and/or surgery, peripheral neuropathy, hearing impairment, and developmental delay affecting daily functioning.
- **Complications:** Pseudo-obstruction crises, malnutrition/intestinal failure, enterocolitis (HSCR-associated), complications of surgery and long-term nutrition support.
- **Recovery potential:** The developmental enteric deficit is not reversible; surgery relieves the aganglionic segment but underlying dysmotility and extraintestinal features persist.
- **Prognostic factors:** Extent of aganglionosis/dysmotility, presence of intestinal failure, and severity of extraintestinal (neuromuscular, hearing) involvement. No validated molecular prognostic biomarkers.

---

## 12. Treatment

**There is no disease-specific pharmacotherapy, gene therapy, or cell therapy for VSCN2.** Management is **supportive and surgical**, targeting the manifestations.

| Modality | Intervention | NCIT suggestion |
|----------|-------------|-----------------|
| Surgical (HSCR) | Pull-through resection of aganglionic segment (Soave, Duhamel, Swenson) | NCIT:C157763 (surgical procedure) |
| Nutritional | Enteral/parenteral nutrition for dysmotility/intestinal failure | NCIT:C15184 (nutritional support) |
| GI supportive | Prokinetics, laxatives, bowel decompression for CIPO | NCIT:C1516 (supportive care) |
| Neuromuscular | Physical/occupational therapy for neuropathy, hypotonia | NCIT:C15315 (rehabilitation therapy) |
| Sensory | Hearing aids / audiologic support for sensorineural hearing loss | — |
| Endocrine | Testosterone/androgen evaluation for micropenis/low testosterone | — |
| Ophthalmology | Ptosis management | — |

- **Pharmacogenomics:** Not applicable (no targeted drug).
- **Advanced / experimental therapeutics:** No gene, RNA, or cell therapies in trials for VSCN2. (The many *ERBB2*/HER2-targeted oncology agents — e.g., trastuzumab, trastuzumab deruxtecan — are irrelevant here, as VSCN2 is caused by loss, not gain, of ERBB2 function; HER2 antagonism would be counterproductive.)
- **Treatment strategy:** Multidisciplinary care (pediatric surgery, gastroenterology/motility, neurology, audiology, nutrition, genetics). Personalized approach centered on the individual's dysmotility burden.

---

## 13. Prevention

- **Primary prevention:** **Genetic counseling** for consanguineous families and known carriers; awareness of autosomal recessive recurrence risk (25% for carrier couples).
- **Secondary prevention:** **Cascade carrier screening** within the affected family; **prenatal diagnosis or preimplantation genetic testing (PGT)** once the familial *ERBB2* variant is identified. Early recognition of HSCR/CIPO in at-risk newborns enables timely surgical/nutritional intervention.
- **Tertiary prevention:** Prevention of complications — enterocolitis prophylaxis in HSCR, nutritional monitoring to prevent intestinal failure, and rehabilitation to limit neuromuscular disability.
- **Immunization / public-health / environmental interventions:** Not applicable (non-infectious genetic disorder).
- **Counseling:** NSGC/ACMG-guided genetic counseling is the principal preventive tool.

---

## 14. Other Species / Natural Disease

- **Taxonomy / model species:** *Mus musculus* (NCBI:txid10090) and *Danio rerio* (zebrafish, NCBI:txid7955) are the principal experimental species; no naturally occurring companion-animal or wildlife VSCN2 analog is catalogued in OMIA.
- **Orthologous genes:** Mouse *Erbb2* (NCBI Gene 13866), *Erbb3* (NCBI Gene 13867), *Nrg1* (NCBI Gene 211323); strongly conserved.
- **Comparative biology / conservation:** The NRG1/ERBB3/ERBB2 axis is deeply conserved across vertebrates in Schwann cell and neural-crest development. Mouse and zebrafish loss-of-function phenocopy key components (Schwann cell precursor loss; reduced enteric/sympathetic ganglia).
- **Zoonotic potential:** None (genetic disorder).

---

## 15. Model Organisms

Mouse and zebrafish models robustly validate the ERBB2/ERBB3/NRG1 mechanism.

| Model | Phenotype | Recapitulation of VSCN2 | Reference |
|-------|-----------|--------------------------|-----------|
| *Erbb2*-null mouse | Embryonic lethal ~E10.5 (cardiac ventricular trabeculation defect) | Limited by early lethality; ENS not fully assessable | Erickson 1997 [PMID: 9362461] |
| *Nrg1* (heregulin)-null mouse | Embryonic lethal ~E10.5 (cardiac) | Confirms NRG1 as the ligand of the axis | [PMID: 9362461] |
| *Erbb3*-null mouse | Lethal ~E13.5; **absent Schwann cell precursors**; generalized neural-crest defect (reduced cranial ganglia, enteric ganglia, adrenal chromaffin cells) | Strong — recapitulates peripheral neuropathy + reduced enteric ganglia | Riethmacher 1997 [PMID: 9338783] |
| Cardiac-rescued *Erbb2*-null mouse | Survive to birth; **lack Schwann cells**, lose motor/sensory neurons | Strong for peripheral component | Woldeyesus/Morris, Neuron 1999 |
| *Wnt1-Cre;Erbb3* conditional | Depletes cervical sympatho-enteric population (E10); esophageal ganglia reduced ~68% at E13.5; reduced foregut Sox10+ cells at E10.5 | Directly models enteric progenitor failure | [PMID: 33497358] |
| *erbb2/erbb3* mutant zebrafish | Early ENS grossly normal (redundancy/timing; dual vagal SCP + trunk crest origin) | Highlights model limitation/redundancy | (Le et al. discussion) |

> *"Schwann-cell precursors"* — Riethmacher et al. showed *Erbb3*-null mice lack Schwann-cell precursors, recapitulating the peripheral neuropathy component. [PMID: 9338783]

**Model limitations:** Conventional *Erbb2*/*Nrg1* knockouts die too early (cardiac lethality) to assess ENS directly; conditional/rescue models are required. Zebrafish show ENS redundancy, so early enteric formation can appear normal. These caveats reflect pathway redundancy and the dual embryonic origin of enteric neurons rather than absence of a role.

**Applications:** Single-cell RNA-seq and conditional deletion models establish cell-type-specific ERBB function in enteric progenitors and Schwann cell precursors — the core disease mechanism.

---

## Mechanistic Model / Interpretation

VSCN2 is best understood as a **kinase-deficiency neurocristopathy**. The NRG1 receptor system is intrinsically split into a ligand-binding subunit (ERBB3) and a catalytic subunit (ERBB2). Neither works alone: signaling demands the **ERBB3/ERBB2 heterodimer**, in which ERBB2 phosphorylates ERBB3's cytoplasmic tail to create docking sites for PI3K–AKT (survival) and RAS–MAPK (proliferation/migration). The VSCN2 lesion (homozygous p.A710V in the ERBB2 kinase domain) removes the catalytic half of this obligate partnership, functionally silencing NRG1 signaling despite intact ligand and intact ERBB3.

Developmentally, the cells most dependent on this signal are **neural-crest-derived enteric progenitors and Schwann cell precursors**, which must survive, proliferate, and migrate to colonize the gut and peripheral nerves. Their signaling failure produces the disease's dual signature: **enteric aganglionosis/hypoganglionosis** (→ HSCR/CIPO) in the gut and **Schwann-cell/peripheral-nerve deficiency** (→ axonal neuropathy, facial paresis, sensorineural hearing loss, ptosis). Mouse genetics corroborates each branch — *Erbb3*/*Erbb2*/*Nrg1* nulls lose Schwann cell precursors and show reduced enteric ganglia, and conditional *Wnt1-Cre;Erbb3* deletion specifically depletes sympatho-enteric progenitors. The convergence of human genetics, patient-cell functional assays (reduced ERBB2/ERBB3 phosphorylation), single-cell expression data, and conditional mouse models makes this one of the more mechanistically complete rare-disease causal chains.

The disorder anchors a coherent **allelic/pathway series**: recessive *ERBB3* (VSCN1, LCCS2) and recessive *ERBB2* (VSCN2) lesions produce overlapping neurocristopathy phenotypes, consistent with their shared obligate-heterodimer biology.

---

## Evidence Base

| PMID | Title / focus | Role in this report |
|------|---------------|---------------------|
| [33497358](https://pubmed.ncbi.nlm.nih.gov/33497358/) | *Dysregulation of the NRG1/ERBB pathway causes a developmental disorder with gastrointestinal dysmotility in humans* (Le et al., J Clin Invest 2021) | **Primary defining paper.** Identifies biallelic *ERBB2*/*ERBB3* variants in 8 individuals; defines VSCN2 (ERBB2 A710V); functional loss-of-function assays; single-cell + conditional mouse validation. |
| [33720042](https://pubmed.ncbi.nlm.nih.gov/33720042/) | *Hirschsprung disease and more: dysregulation of ERBB2 and ERBB3* (Gershon commentary) | Confirms ERBB2/ERBB3 as NRG1-binding EGF receptors expressed in enteric neuronal progenitors; frames HSCR/CIPO as congenital motility defects. |
| [9338783](https://pubmed.ncbi.nlm.nih.gov/9338783/) | Riethmacher et al. 1997 — *Erbb3*-null mouse | Model evidence: absence of Schwann-cell precursors; neural-crest/enteric ganglia defect. |
| [9362461](https://pubmed.ncbi.nlm.nih.gov/9362461/) | Erickson et al. 1997 — *Erbb2*/*Nrg1* nulls | Model evidence: early cardiac-lethal phenotypes; establishes ligand/receptor pairing. |
| [11312610](https://pubmed.ncbi.nlm.nih.gov/11312610/) | *Neuregulin signaling through a PI3K/Akt/Bad pathway in Schwann cell survival* | Mechanistic: defines the PI3K/AKT/BAD survival arm downstream of NRG1-ERBB. |

**Evidence-source types:** Human clinical/genetic (PMID 33497358; commentary 33720042); model organism (PMID 9338783, 9362461, conditional models); in vitro functional (patient fibroblast RT-qPCR, Neuro-2a immunoblot; PMID 33497358); biochemical/pathway (PMID 11312610; Reactome R-HSA-1227986).

*(Note: The breast-cancer HER2 therapy papers retrieved during investigation — PMIDs 40759100, 32715420, 28366406, 18650157 — pertain to oncologic HER2 gain-of-function targeting and are **not** applicable to VSCN2, a loss-of-function disorder. They are excluded from the mechanistic evidence base.)*

---

## Limitations and Knowledge Gaps

1. **Single-family disease.** All VSCN2-specific clinical data derive from two siblings in one consanguineous Turkish family. Penetrance, expressivity, natural history, prognosis, and prevalence cannot be estimated; gene–disease validity is **LIMITED**.
2. **One variant.** Only p.A710V is documented for *ERBB2* in VSCN2; the full mutational spectrum, genotype–phenotype correlations, and allele frequencies are unknown.
3. **No epidemiologic data.** No prevalence/incidence, sex ratio, or geographic distribution beyond the index Turkish family.
4. **No dedicated Orphanet/ICD-11 code** for type 2, complicating standardized cataloguing.
5. **Model caveats.** Conventional *Erbb2* knockouts are cardiac-lethal before ENS assessment; zebrafish show ENS redundancy — so the enteric role relies on conditional/rescue models and human genetics rather than a direct *Erbb2* enteric knockout phenotype.
6. **No therapeutics.** No disease-specific treatment exists; management is empiric/supportive.
7. **Extraintestinal features under-characterized.** The mechanistic link between ERBB2 loss and craniofacial/endocrine features (micropenis, low testosterone, hypoplastic alae nasi) is *inferred* from neural-crest biology, not directly demonstrated.

---

## Proposed Follow-up Experiments / Actions

1. **Patient ascertainment / matchmaking.** Deposit the *ERBB2* variant in ClinVar and use GeneMatcher/Matchmaker Exchange to find additional VSCN2 families, enabling genotype–phenotype and penetrance analysis.
2. **Allelic-series functional platform.** Establish a standardized ERBB2/ERBB3 phosphorylation and PI3K-AKT/MAPK reporter assay to classify future *ERBB2* variants (VUS resolution per ACMG PS3/BS3).
3. **Conditional *Erbb2* enteric knockout.** Generate a *Wnt1-Cre;Erbb2* (or inducible *Sox10-CreER;Erbb2*) mouse to directly test the enteric requirement for ERBB2 (paralleling the existing *Erbb3* conditional), bypassing cardiac lethality.
4. **Patient iPSC → enteric neural crest / organoid model.** Differentiate patient-derived iPSCs into enteric neural crest and gut organoids to model colonization failure and screen small molecules acting downstream of the receptor block.
5. **Extraintestinal mechanism mapping.** Lineage-tracing in conditional models to test whether craniofacial/endocrine features arise from specific neural-crest sublineages, formalizing the currently inferred steps.
6. **Registry / natural history.** Create an NRG1/ERBB-spectrum (VSCN1/2/3, LCCS2) registry to aggregate ultra-rare cases and define prognosis and management outcomes.
7. **Ontology curation.** Propose a dedicated Orphanet/ICD-11 entry and HPO annotation set for VSCN2 to improve knowledge-base interoperability.

---

*Prepared from a 5-iteration autonomous investigation. Core citations: [PMID 33497358](https://pubmed.ncbi.nlm.nih.gov/33497358/), [PMID 33720042](https://pubmed.ncbi.nlm.nih.gov/33720042/), [PMID 9338783](https://pubmed.ncbi.nlm.nih.gov/9338783/), [PMID 9362461](https://pubmed.ncbi.nlm.nih.gov/9362461/), [PMID 11312610](https://pubmed.ncbi.nlm.nih.gov/11312610/).*


## Artifacts

- [OpenScientist final report](Familial_Visceral_Neuropathy_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Visceral_Neuropathy_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 28 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030399` (2 mentions) - the report calls it "MONDO"; MONDO calls it **visceral neuropathy, familial, 2, autosomal recessive**
- `HP:0003812` (2 mentions) - the report calls it "variable", "Expressivity:** Variable across the broader NRG1/ERBB series"; HP calls it **Phenotypic variability**
- `HP:0002580` (1 mention) - the report calls it "Clinical sign"; HP calls it **Volvulus**
- `HP:0000407` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Sensorineural hearing impairment**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001263` (1 mention) - the report calls it "Behavioral/neuro"; HP calls it **Global developmental delay**
- `HP:0001762` (1 mention) - the report calls it "Physical"; HP calls it **Talipes equinovarus**
- `HP:0002650` (1 mention) - the report calls it "Physical"; HP calls it **Scoliosis**
- `HP:0000054` (1 mention) - the report calls it "Physical"; HP calls it **Micropenis**
- `HP:0040171` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased serum testosterone concentration**
- `HP:0002804` (1 mention) - the report calls it "Physical"; HP calls it **Arthrogryposis multiplex congenita**
- `NCIT:C157763` (1 mention) - the report calls it "surgical procedure"; NCIT calls it **Metastatic Bladder Small Cell Neuroendocrine Carcinoma**
- `NCIT:C15184` (1 mention) - the report calls it "nutritional support"; NCIT calls it **Behavioral Intervention**
- `NCIT:C1516` (1 mention) - the report calls it "supportive care"; NCIT calls it **Lisofylline**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003477` (1 mention) - the report calls it "peripheral neuropathy"; HP calls it **Peripheral axonal neuropathy**
- `HP:0007209` (1 mention) - the report calls it "Clinical sign"; HP calls it **Facial paralysis**, and lists "Facial paresis" among its other names
- `CL:0011103` (2 mentions) - the report calls it "enteric neuron"; CL calls it **sympathetic neuron**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003812` - called "variable", "Expressivity:** Variable across the broader NRG1/ERBB series"