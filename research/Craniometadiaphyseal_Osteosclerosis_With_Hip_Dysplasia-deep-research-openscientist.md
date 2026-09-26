---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T13:56:41.627537'
end_time: '2026-09-25T14:12:32.606190'
duration_seconds: 950.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Craniometadiaphyseal Osteosclerosis with Hip Dysplasia
  mondo_id: MONDO:0957832
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
citation_count: 8
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 36
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 7
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0957832
    reported_labels:
    - MONDO
    ontology_label: craniometadiaphyseal osteosclerosis with hip dysplasia
  - term_id: HP:0000256
    reported_labels:
    - Core / very frequent
    ontology_label: Macrocephaly
  - term_id: HP:0004437
    reported_labels:
    - Core / very frequent
    ontology_label: Cranial hyperostosis
  - term_id: HP:0004618
    reported_labels:
    - Core / frequent
    ontology_label: Sandwich appearance of vertebral bodies
  - term_id: HP:0003015
    reported_labels:
    - Frequent
    ontology_label: Flared metaphysis
  - term_id: HP:0001385
    reported_labels:
    - Frequent
    ontology_label: Hip dysplasia
  - term_id: HP:0001627
    reported_labels:
    - Frequent
    ontology_label: Abnormal heart morphology
  - term_id: HP:0001263
    reported_labels:
    - Variable
    ontology_label: Global developmental delay
  - term_id: HP:0001871
    reported_labels:
    - Frequent
    ontology_label: Abnormality of blood and blood-forming tissues
  - term_id: HP:0000316
    reported_labels:
    - Frequent
    ontology_label: Hypertelorism
  - term_id: HP:0005280
    reported_labels:
    - Frequent
    ontology_label: Depressed nasal bridge
  - term_id: HP:0004322
    reported_labels:
    - Subset
    ontology_label: Short stature
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Craniometadiaphyseal_Osteosclerosis_With_Hip_Dysplasia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Craniometadiaphyseal_Osteosclerosis_With_Hip_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniometadiaphyseal Osteosclerosis with Hip Dysplasia
- **MONDO ID:** MONDO:0957832 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Craniometadiaphyseal Osteosclerosis with Hip Dysplasia** covering all of the
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

# Craniometadiaphyseal Osteosclerosis with Hip Dysplasia (CMDOH): A Comprehensive Disease Characterization

**Disease:** Craniometadiaphyseal Osteosclerosis with Hip Dysplasia (CMDOH)
**MONDO ID:** MONDO:0957832 · **OMIM:** #620558 · **Gene:** *AXIN1* (OMIM *603816; HGNC:903; chr16p13.3)
**Category:** Mendelian (autosomal recessive)

---

## Summary

Craniometadiaphyseal osteosclerosis with hip dysplasia (CMDOH) is an ultra-rare, autosomal recessive **sclerosing skeletal dysplasia** caused by biallelic (homozygous, in the reported consanguineous families) **C-terminally truncating variants in *AXIN1***. AXIN1 is the scaffold protein of the β-catenin destruction complex, the negative regulator of canonical Wnt signaling. The disease-causing variants truncate the **C-terminal DIX domain**, which mediates AXIN1 self-polymerization, thereby lowering AXIN1 protein levels and impairing destruction-complex assembly. The net functional consequence is **enhanced basal canonical Wnt/β-catenin signaling** — a "Wnt-gain" state — that shifts the balance of bone remodeling toward increased osteoblastic bone formation and reduced osteoclastic resorption, producing generalized osteosclerosis and hyperostosis.

The condition was defined in 2023 by Terhal et al. ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)), who described **seven individuals from four families** carrying **three distinct homozygous truncating *AXIN1* variants**. The core phenotype comprises congenital/progressive **macrocephaly**, **cranial hyperostosis** (calvarial and skull-base sclerosis), and **vertebral endplate sclerosis** ("sandwich vertebrae"), together with frequent **hip dysplasia**, **heart malformations**, **variable developmental delay**, **hematological anomalies**, metaphyseal flaring, and dysmorphic facies. Bone biopsy demonstrated increased osteoblast activity and reduced osteoclast function at the growth-plate resorption zone, consistent with the Wnt-gain mechanism.

Mechanistically, CMDOH sits at the "hypomorphic" end of an *AXIN1* dysfunction spectrum: germline biallelic DIX-domain truncations are partial loss-of-function (protein is reduced and polymerization is impaired but some Wnt-inhibitory function is retained), yielding a viable skeletal phenotype, whereas **complete somatic loss of AXIN1** drives cancer (notably hepatocellular carcinoma) through full canonical Wnt activation. Crucially, the same study showed that a **tankyrase inhibitor (XAV939)** — which stabilizes AXIN1/AXIN2 — attenuates the Wnt overactivity in patient-derived and genome-edited cells, nominating a mechanistically rational (though not yet clinically tested) targeted therapy. Mouse *Axin1* models corroborate the β-catenin–dependent, osteoblast-lineage mechanism. No disease-specific therapy currently exists; management is supportive and multidisciplinary.

---

## Section 1 — Disease Information

**Overview.** CMDOH is a rare Mendelian sclerosing bone dysplasia combining features of two classic radiographic categories: osteopetrosis-like changes (sandwich vertebrae, metaphyseal flaring) and endosteal-hyperostosis-like changes (calvarial and cortical thickening). It is characterized by macrocephaly, cranial hyperostosis, vertebral endplate sclerosis, hip dysplasia, and additional extraskeletal involvement (cardiac, developmental, hematological). "Sclerosing skeletal dysplasias result from an imbalance between bone formation and resorption" ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)) — CMDOH exemplifies this, with the imbalance tilted toward net bone accrual.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0957832 |
| OMIM (phenotype) | #620558 (Craniometadiaphyseal osteosclerosis with hip dysplasia) |
| Gene | *AXIN1*, OMIM *603816, HGNC:903, chromosome 16p13.3 |
| Orphanet | No dedicated ORPHA code clearly assigned at time of investigation (ultra-rare, delineated 2023) |
| ICD-10 / ICD-11 | No specific code; maps under sclerosing/osteosclerotic bone dysplasia (e.g., ICD-10 Q78.-, "Other osteochondrodysplasias") |
| MeSH | No specific descriptor; related: "Osteosclerosis", "Osteochondrodysplasias" |

**Synonyms / alternative names.** Craniometadiaphyseal osteosclerosis with hip dysplasia; CMDOH; AXIN1-related sclerosing skeletal dysplasia. The name captures the anatomic distribution (**cranio-** = skull; **meta-/diaphyseal** = metaphysis/diaphysis of long bones) plus the associated hip dysplasia.

**Information source.** Knowledge is derived from an **aggregated case series** — deep clinical, radiographic, and functional characterization of individual patients (7 individuals / 4 families) reported in a single landmark paper, plus mechanistic corroboration from cellular models and model organisms. It is **not** derived from large EHR/registry datasets, reflecting the disorder's extreme rarity.

---

## Section 2 — Etiology

**Primary cause (genetic).** CMDOH is a **monogenic autosomal recessive** disorder caused by **biallelic C-terminally truncating variants in *AXIN1***. In the reported families, affected individuals were homozygous, consistent with parental consanguinity. There is no known environmental, infectious, or acquired cause.

**Genetic risk factors.** The disease is fully genetically determined by the *AXIN1* genotype. **Consanguinity** is the principal contextual risk factor, increasing the probability of homozygosity for a rare recessive allele. No modifier loci have been formally mapped; the paralog **AXIN2** is a plausible biological modifier because it can partially compensate for AXIN1 (see Mechanism).

**Environmental risk factors.** None identified. Sex does not appear to influence occurrence (recessive Mendelian trait). Family history / consanguinity is the relevant contextual factor.

**Protective factors.** No genetic or environmental protective factors are established. Biologically, retained partial AXIN1 function and AXIN2 compensation are inferred to make the phenotype viable (compared with the lethality of complete Axin1 loss in mice), but this is a feature of the hypomorphic allele class rather than a modifiable protective factor.

**Gene–environment interactions.** None demonstrated. The disorder is essentially environment-independent.

---

## Section 3 — Phenotypes

The phenotype spectrum below is drawn from the 7 patients / 4 families in Terhal et al. 2023 ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)). Frequencies are qualitative given the tiny cohort.

| Phenotype | Type | Onset | Severity / progression | Frequency | Suggested HPO term |
|---|---|---|---|---|---|
| Macrocephaly (+2.2 to +6.1 SD) | Physical/clinical sign | Congenital, progressive | Moderate–severe, progressive | Core / very frequent | HP:0000256 |
| Cranial hyperostosis (calvarial + skull-base sclerosis) | Imaging/clinical sign | From first year, progressive | Progressive | Core / very frequent | HP:0004437 |
| Vertebral endplate sclerosis ("sandwich vertebrae") | Imaging sign | Childhood | Progressive | Core / frequent | HP:0004618 |
| Metaphyseal flaring / widening | Imaging sign | Childhood | Progressive | Frequent | HP:0003015 |
| Hip dysplasia | Clinical/imaging sign | Congenital/childhood | Variable | Frequent | HP:0001385 |
| Heart malformations | Structural anomaly | Congenital | Variable | Frequent | HP:0001627 |
| Developmental delay | Neurobehavioral | Childhood | Variable/mild-moderate | Variable | HP:0001263 |
| Hematological anomalies | Laboratory abnormality | Variable | Variable | Frequent | HP:0001871 |
| Hypertelorism | Dysmorphic sign | Congenital | Stable | Frequent | HP:0000316 |
| Depressed/low nasal bridge | Dysmorphic sign | Congenital | Stable | Frequent | HP:0005280 |
| Short stature (subset) | Growth | Childhood | Variable | Subset | HP:0004322 |

**Onset and severity.** Reported ages span **3 months to 15.5 years**. Macrocephaly is congenital and progressive; cranial hyperostosis emerges and progresses from the **first year of life**. Severity is variable across families.

**Quality-of-life impact.** No formal QoL instruments (EQ-5D, SF-36, PROMIS) have been applied. Anticipated impacts, by analogy with other cranial hyperostoses, include potential cranial-nerve compression (from skull-base sclerosis), orthopedic morbidity from hip dysplasia (pain, mobility limitation), and developmental/educational impact where developmental delay is present. These are inferred rather than measured.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** ***AXIN1*** (axis inhibitor 1) — OMIM *603816, HGNC:903, chromosome **16p13.3**. AXIN1 is the central scaffold of the β-catenin destruction complex (with APC, GSK3β, CK1), which phosphorylates β-catenin to target it for degradation.

**Pathogenic variants (Terhal et al. 2023).** Three distinct **C-terminal truncating** variants across four families:

| Family | Variant | Type | Consequence |
|---|---|---|---|
| Family 1 (two sisters) | 1-bp duplication (frameshift, e.g., p.Asp796Glufs*6-type) | Frameshift | Premature truncation, DIX domain lost |
| Families 2 & 4 | **p.Arg723*** (R723X) — recurrent nonsense | Nonsense | Truncation removing DIX domain |
| Family 3 | **p.Arg805*** (R805X) | Nonsense | C-terminal truncation, DIX domain disrupted |

All variants disrupt the **C-terminal DIX domain**, which mediates AXIN1 homo-polymerization and destruction-complex assembly.

**Variant classification.** Per ACMG/AMP criteria these are **pathogenic** (loss-of-function truncating variants in a gene with an established gene–disease relationship, segregating with disease in multiple consanguineous families, supported by functional evidence).

**Allele frequency.** These are private/ultra-rare variants; not present at appreciable frequency in gnomAD. The recurrent p.Arg723* appearing in two families likely reflects an arginine CpG mutational hotspot rather than a broad founder effect.

**Somatic vs germline.** In CMDOH the variants are **germline**. By contrast, *AXIN1* is recurrently altered **somatically** in cancer (see F003).

**Functional consequence.** **Hypomorphic loss of function.** The truncations reduce AXIN1 protein levels and impair DIX-domain–mediated polymerization, but overexpression studies showed partially **retained** Wnt-inhibitory function — explaining why the phenotype is a viable skeletal dysplasia rather than the embryonic lethality seen with complete Axin1 loss. Net pathway effect: **enhanced basal canonical Wnt/β-catenin signaling** (gain of Wnt output via loss of a negative regulator).

**Modifier genes.** **AXIN2** (the paralog) is the strongest candidate modifier: XAV939 rescue of AXIN1-knockout cells implicates AXIN2 stabilization as a compensatory route (see F006).

**Epigenetic / chromosomal.** No disease-specific epigenetic signature or large-scale chromosomal abnormality has been reported for CMDOH.

---

## Section 5 — Environmental Information

No environmental, lifestyle, or infectious contributors are implicated. CMDOH is a purely genetic, autosomal recessive Mendelian disorder. **Not applicable:** toxins/radiation/pollution; smoking/diet/exercise/alcohol; infectious agents.

---

## Section 6 — Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic C-terminal truncating variant in *AXIN1*** (e.g., p.Arg723*, p.Arg805*, or a frameshift) → **removes/disrupts the DIX domain**.
2. Loss of the DIX domain **impairs AXIN1 self-polymerization** and **lowers AXIN1 protein levels** → *results in* a weakened, less abundant scaffold.
3. Reduced functional AXIN1 → **destabilizes the β-catenin destruction complex** (AXIN1–APC–GSK3β–CK1) → *leads to* reduced phosphorylation/degradation of β-catenin.
4. → **Cytoplasmic β-catenin accumulates and translocates to the nucleus** → *results in* **enhanced basal canonical Wnt/β-catenin transcriptional output** (demonstrated directly in patient and genome-edited cells).
5. In the **osteoblast lineage**, elevated β-catenin → *increases* **OPG (osteoprotegerin)** and the **OPG:RANKL ratio** (inferred from mouse *Axin1^Osx^* model) → *leads to* **suppressed osteoclastogenesis** (fewer TRAP+/MMP9+/cathepsin-K+ osteoclasts).
6. Branch A — **increased osteoblastic bone formation**; Branch B — **decreased osteoclastic bone resorption**. Both branches converge to → **net increase in bone mass / osteosclerosis and hyperostosis**.
7. Anatomically distributed → **cranial hyperostosis + macrocephaly**, **vertebral endplate ("sandwich") sclerosis**, **metaphyseal flaring**; with associated developmental effects producing **hip dysplasia, cardiac malformation, developmental delay, hematological anomalies** (the extraskeletal links are consistent with the broad developmental role of Wnt signaling but are *inferred*, not individually demonstrated).
8. **Therapeutic branch:** **Tankyrase inhibition (XAV939)** raises AXIN1/AXIN2 levels → *restores* destruction-complex activity → *attenuates* Wnt overactivity in mutant cells (in vitro proof of concept).

Steps 1–4 and step 8 are **experimentally demonstrated in the human/cell system**; step 5 is **inferred from mouse osteoblast-lineage models**; step 7's extraskeletal links are **inferred** from Wnt biology.

### Detail by category

- **Molecular pathway:** Canonical **Wnt/β-catenin** signaling (KEGG hsa04310; Reactome "Degradation of beta-catenin by the destruction complex," R-HSA-195253). AXIN1 is the rate-limiting scaffold of the destruction complex.
- **Cellular processes:** Osteoblast differentiation/activity (increased); osteoclastogenesis (suppressed via OPG/RANKL). GO:0060070 (canonical Wnt signaling pathway), GO:0001649 (osteoblast differentiation), GO:0030316 (osteoclast differentiation), GO:0045597/0045668 (regulation of osteoblast/osteoclast differentiation).
- **Protein dysfunction:** DIX-domain truncation → **loss of polymerization**, reduced protein stability → hypomorphic LOF of the destruction-complex scaffold.
- **Biochemical abnormality:** Failure to phosphorylate/degrade β-catenin; downstream Wnt target activation (e.g., c-Myc, CCND1 seen in AXIN1-loss cancer models, supporting pathway direction).
- **Tissue remodeling mechanism:** Dysregulated bone remodeling with osteoblast–osteoclast imbalance at the growth-plate resorption zone; coarse trabeculae on biopsy.
- **Cell types (CL):** osteoblast (CL:0000062), osteoclast (CL:0000092), osteoprogenitor/mesenchymal stromal cell (CL:0000134), osteocyte (CL:0000137).

### Molecular profiling
- Direct **functional readouts** (Wnt reporter activity) in patient-derived and CRISPR-edited cells: *enhanced basal canonical Wnt activity* ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)).
- Mouse osteoblast-lineage models: increased β-catenin, increased OPG:RANKL, decreased osteoclast markers.
- No dedicated patient transcriptomic/proteomic/metabolomic/single-cell datasets are available for CMDOH.

---

## Section 7 — Anatomical Structures Affected

**Organ / system level (primary).** Skeletal system — with a distinctive craniospinal and metadiaphyseal distribution:
- **Skull / calvarium & skull base** (UBERON:0000209 cranial skeletal system; UBERON:0004339 calvaria) — hyperostosis, macrocephaly.
- **Vertebral column** (UBERON:0001130) — endplate sclerosis ("sandwich vertebrae").
- **Long bones — metaphysis/diaphysis** (UBERON:0002515 metaphysis; UBERON:0004770 diaphysis) — flaring, sclerosis.
- **Hip joint / pelvis** (UBERON:0001464 hip; UBERON:0001474 bone of the pelvis) — hip dysplasia.

**Secondary organ involvement.** Cardiovascular (heart malformations, UBERON:0000948); hematopoietic system (hematological anomalies, UBERON:0002390); central nervous system (developmental delay; potential cranial-nerve compromise from skull-base sclerosis).

**Tissue / cell level.** Bone (connective) tissue; growth-plate cartilage/resorption zone. Cell populations: **osteoblasts** (increased activity), **osteoclasts** (reduced number/function), osteoprogenitors.

**Subcellular level.** β-catenin destruction complex is **cytoplasmic**; downstream signaling acts in the **nucleus** (β-catenin/TCF transcription). GO cellular components: GO:0030877 (beta-catenin destruction complex), GO:0005737 (cytoplasm), GO:0005634 (nucleus).

**Localization / lateralization.** Skeletal involvement is **generalized and bilateral/symmetric** (calvarium, spine, long bones); hip dysplasia may be uni- or bilateral.

---

## Section 8 — Temporal Development

- **Onset:** **Congenital** (macrocephaly present at/near birth); cranial hyperostosis develops and progresses from the **first year of life**. Onset pattern is **chronic and insidious/progressive**.
- **Progression:** Radiographic sclerosis is **progressive** through childhood (cases documented from 3 months to 15.5 years). Progression rate appears slow-to-moderate and **variable** between families.
- **Disease course:** **Chronic, lifelong.** No episodic or relapsing-remitting pattern.
- **Remission:** None spontaneous; no treatment-induced remission described (no disease-modifying therapy in clinical use).
- **Critical periods:** The **first years of life** (active bone modeling) represent the window in which hyperostosis emerges — mechanistically the most rational period for any future targeted (Wnt-normalizing) intervention.

---

## Section 9 — Inheritance and Population

- **Epidemiology:** **Ultra-rare.** Prevalence/incidence are unknown and unquantified; total literature comprises 7 individuals from 4 families. No registry-based estimate exists.
- **Inheritance:** **Autosomal recessive.** Affected individuals were **homozygous**; parents are obligate heterozygous carriers.
- **Penetrance:** Appears **complete** in biallelic individuals (all reported homozygotes affected), though the sample is too small for precise estimation.
- **Expressivity:** **Variable** — e.g., variable developmental delay, cardiac involvement, and stature across families/individuals.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effect:** No broad founder effect established; the recurrent p.Arg723* likely reflects a CpG mutational hotspot rather than a shared haplotype.
- **Consanguinity:** **Central** — homozygosity arose in consanguineous families.
- **Carrier frequency:** Unknown; expected to be very low given ultra-rarity.
- **Population demographics:** Reported families are consistent with consanguineous backgrounds; no established sex bias (recessive). Distribution is sporadic, not endemic.

---

## Section 10 — Diagnostics

**Imaging (cornerstone of diagnosis).** Skeletal survey / radiographs demonstrating:
- Calvarial and skull-base **hyperostosis/sclerosis**; macrocephaly.
- **Vertebral endplate sclerosis** ("sandwich vertebrae").
- **Metaphyseal flaring** and long-bone sclerosis.
- Hip dysplasia on pelvic imaging.
CT is useful to characterize skull-base sclerosis and potential foraminal narrowing.

**Laboratory / biomarkers.** No specific diagnostic biomarker. Bone turnover markers are not established as diagnostic. Hematological anomalies warrant a CBC and hematologic workup. Bone biopsy (research setting) showed **increased osteoblast and reduced osteoclast function** with coarse trabeculae.

**Genetic testing (confirmatory).** The diagnosis is molecularly confirmed by identifying **biallelic C-terminal truncating *AXIN1* variants**.
- **WES/WGS** is the practical first-line approach given phenotypic overlap among sclerosing dysplasias.
- **Targeted *AXIN1* sequencing** or inclusion in a **sclerosing bone dysplasia / skeletal dysplasia gene panel** is appropriate once suspected.
- CMA/karyotype/FISH/mtDNA/repeat testing are **not** indicated (single-gene, SNV/indel etiology).

**Clinical criteria & differential diagnosis.** No formal consensus criteria exist (recently delineated). Key differentials among sclerosing/craniotubular dysplasias:

| Condition | Gene | Pathway | Distinguishing features |
|---|---|---|---|
| **CMDOH** | *AXIN1* (recessive, DIX truncation) | **Wnt gain** | Sandwich vertebrae + metaphyseal flaring + hip dysplasia + macrocephaly |
| Craniotubular dysplasia, Ikegawa type (CTDI, OMIM #619727) | *TMEM53* | **BMP-SMAD** dysregulation | Skull hyperostosis, childhood **blindness** ([PMID: 33824347](https://pubmed.ncbi.nlm.nih.gov/33824347/), [PMID: 39084544](https://pubmed.ncbi.nlm.nih.gov/39084544/), [PMID: 41408477](https://pubmed.ncbi.nlm.nih.gov/41408477/)) |
| Sclerosteosis / Van Buchem | *SOST* / SOST enhancer | Wnt (loss of inhibitor) | High bone mass, syndactyly (sclerosteosis) |
| Osteopetrosis | *CLCN7*, *TCIRG1*, etc. | Osteoclast defect | Fractures, marrow failure, cranial nerve palsies |
| Endosteal hyperostosis | *LRP4/5*, *SOST* | Wnt | Cortical thickening pattern |

**Screening.** In known families, **cascade carrier testing** and, where desired, **prenatal/preimplantation genetic testing** for the familial *AXIN1* variants are options. No population newborn screening exists.

---

## Section 11 — Outcome / Prognosis

- **Survival/mortality:** No systematic survival data. Not reported to be lethal in childhood; the oldest reported individual was 15.5 years. Life expectancy is undefined.
- **Morbidity:** Driven by skeletal complications — potential **cranial-nerve compromise** from skull-base hyperostosis, **orthopedic morbidity** from hip dysplasia, and functional impact of **developmental delay**; cardiac malformations and hematological anomalies contribute variably.
- **Disease course:** **Chronic, progressive** sclerosis. Recovery potential is limited; no disease-modifying therapy is in clinical use.
- **Prognostic factors:** Presumed to include severity of cranial/skull-base involvement (nerve compression risk), cardiac status, and degree of developmental delay. No validated prognostic biomarkers.
- **QoL measures:** Not formally assessed.

Given the small cohort, all prognostic statements carry substantial uncertainty.

---

## Section 12 — Treatment

**No disease-specific, approved therapy exists.** Management is **supportive and multidisciplinary.**

- **Supportive/rehabilitative:** Orthopedic management of **hip dysplasia** (bracing/surgery as indicated); monitoring for and surgical decompression of **skull-base/foraminal narrowing** if cranial-nerve compromise develops; cardiology management of heart malformations; hematology follow-up; developmental/physical/occupational therapy as needed. NCIT concepts: Supportive Care (NCIT:C15277), Orthopedic Surgery (NCIT:C16536), Physical Therapy (NCIT:C15367).
- **Pharmacotherapy:** No established drug therapy. No pharmacogenomic guidance.
- **Advanced/experimental (mechanistically rational, not clinical):** **Tankyrase inhibition (e.g., XAV939)** is an in-vitro-validated concept — it stabilizes AXIN1/AXIN2 and normalizes Wnt overactivity in mutant cells ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)). This has **not** been tested in patients; systemic tankyrase inhibition carries known intestinal/skeletal toxicity concerns and would require careful therapeutic-window definition. No gene/cell/RNA therapies are in development for CMDOH.
- **Treatment strategy:** Individualized, symptom-directed. Any future targeted (Wnt-normalizing) approach would most plausibly target the **early childhood** window of active bone modeling.

---

## Section 13 — Prevention

- **Primary prevention:** Not possible for a Mendelian recessive disorder beyond reproductive genetic counseling.
- **Genetic counseling & reproductive options:** **Central preventive measure.** For carrier couples (25% recurrence risk per pregnancy), options include **carrier/cascade testing**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT)** for the familial *AXIN1* variants. Counseling on **consanguinity**-associated recessive risk is relevant.
- **Secondary/tertiary prevention:** Early imaging surveillance to detect and manage skull-base sclerosis (prevent nerve compression), hip surveillance, and cardiac/hematologic monitoring to prevent complications.
- **Immunization / public health / environmental:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthologous gene:** *Axin1* is conserved across vertebrates. Mouse *Axin1* (NCBI Gene ID 12005) was originally identified as the **Fused** locus ([PMID: 9230313](https://pubmed.ncbi.nlm.nih.gov/9230313/)); "Axin is a novel inhibitor of Wnt signaling." Taxonomy: *Mus musculus* (NCBI:txid10090), *Danio rerio*, etc.
- **Naturally occurring disease:** No naturally occurring CMDOH-equivalent has been catalogued in companion animals or wildlife (no OMIA entry identified for this specific disorder).
- **Comparative biology:** The canonical Wnt/β-catenin pathway and AXIN scaffold function are **deeply evolutionarily conserved**, underpinning the validity of mouse models. Classic mouse *Fused/Axin1* mutant alleles cause **axial duplication**, reflecting Wnt's role in body-axis patterning.
- **Zoonotic potential / cross-species transmission:** Not applicable (genetic disorder).

---

## Section 15 — Model Organisms

- **Mouse — constitutive knockout:** *Axin1*-null is **embryonic lethal**, precluding study of the adult skeletal phenotype and underscoring why viable human disease requires **hypomorphic** alleles.
- **Mouse — conditional osteoblast-lineage deletion (*Axin1^Osx^*, Osterix-Cre):** Increased β-catenin, elevated **OPG and OPG:RANKL ratio**, decreased TRAP+/MMP9+/cathepsin-K+ **osteoclasts**, suppressed osteoclastogenesis, and delayed postnatal bone growth — directly **recapitulating the human biopsy finding** of increased osteoblast/reduced osteoclast activity (Bone Research 2020, PMC7424530).
- **Mouse — limb-mesenchyme deletion (Prrx1-Cre):** Elevated β-catenin producing a fibular-hemimelia/tarsal-coalition phenotype, **partially rescued by deleting one β-catenin allele** (bone volume 92%→71%), formally demonstrating **β-catenin dependence** (eLife 2023, PMC9815809).
- **Paralog — *Axin2* knockout:** Craniosynostosis and increased trabecular bone mass, illustrating overlapping AXIN function in skeletal Wnt regulation and supporting AXIN2 as a compensatory modifier.
- **Cellular models:** Patient-derived primary cells and **CRISPR genome-edited cells** carrying p.Arg723* / p.Asp796Glufs*6, plus HEK293T reporter systems, demonstrated enhanced basal Wnt activity and **XAV939 rescue** ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)).
- **Phenotype recapitulation & limitations:** Osteoblast-lineage models faithfully reproduce the **cellular remodeling imbalance** but not the full craniospinal radiographic pattern; constitutive models are lethal. No model reproduces the complete extraskeletal spectrum (cardiac, hematological).
- **Resources:** MGI (mouse), Alliance of Genome Resources, IMPC/IMSR for *Axin1/Axin2* alleles.

---

## Key Findings (with evidence)

### F001 — CMDOH is caused by biallelic C-terminal-truncating *AXIN1* variants (autosomal recessive)
Terhal et al. 2023 identified **three homozygous, C-terminally truncating *AXIN1* variants in seven individuals from four families**. Verbatim: *"We identified three homozygous, C-terminally truncating AXIN1 variants in seven individuals from four families affected by macrocephaly, cranial hyperostosis, and vertebral endplate sclerosis. Other frequent findings included hip dysplasia, heart malformations, variable developmental delay, and hematological anomalies."* ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)). This establishes the gene, variant class, inheritance, cohort size, and the core phenotype.

### F002 — Mechanism: DIX-domain truncation enhances canonical Wnt/β-catenin signaling; tankyrase inhibition rescues
In patient-derived and genome-edited cells, *"analyses of primary and genome-edited cells harboring the truncating variants revealed enhanced basal canonical Wnt pathway activity."* The truncations impair DIX-domain polymerization but partially retain Wnt-inhibitory function on overexpression, and *"addition of a tankyrase inhibitor attenuated Wnt overactivity in the AXIN1-mutant model systems"* ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)) — establishing both the causal Wnt-gain mechanism and a candidate targeted therapy.

### F003 — AXIN1 is a Wnt-pathway tumor suppressor; complete somatic loss causes cancer, whereas germline hypomorphic truncations cause skeletal dysplasia
AXIN1 is a bona fide tumor suppressor: in hepatocellular carcinoma, *"up to 50% of cases exhibit aberrant activation of the canonical Wnt/β-catenin pathway, driven by CTNNB1 mutations or inactivating alterations in AXIN1, adenomatous polyposis coli, or ZNRF3, which are mutually exclusive"* ([PMID: 42237887](https://pubmed.ncbi.nlm.nih.gov/42237887/)). Functional demonstration: *"the WNT pathway and its target gene c-Myc were activated when AXIN1 was missing"* ([PMID: 39653061](https://pubmed.ncbi.nlm.nih.gov/39653061/)); AXIN1 mutation upregulates CCND1 (p=0.022) with β-catenin–CCND1 correlation r=0.43 ([PMID: 40344393](https://pubmed.ncbi.nlm.nih.gov/40344393/)). The dosage/allele-class contrast explains why germline **hypomorphic** DIX truncations yield a viable Wnt-gain skeletal phenotype rather than malignancy.

### F004 — Clinical spectrum and specific variants (OMIM #620558)
Core radiographic features: macrocephaly (+2.2 to +6.1 SD), progressive calvarial/skull-base sclerosis, vertebral endplate ("sandwich") sclerosis, metaphyseal flaring, hypertelorism with low nasal bridge; plus hip dysplasia, heart malformations, variable developmental delay, hematological anomalies, and short stature in a subset. Bone biopsy showed increased osteoblast and reduced osteoclast activity at the growth-plate resorption zone. *"Sclerosing skeletal dysplasias result from an imbalance between bone formation and resorption"* ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)) frames the underlying remodeling defect.

### F005 — Mouse *Axin1* models support the Wnt-gain, osteoblast-lineage mechanism
*Axin1* was cloned from the mouse *Fused* locus ([PMID: 9230313](https://pubmed.ncbi.nlm.nih.gov/9230313/)); constitutive knockout is embryonic-lethal. Osteoblast-lineage deletion increases β-catenin and OPG:RANKL and suppresses osteoclastogenesis (mirroring the human biopsy); limb-mesenchyme deletion elevates β-catenin and is partially rescued by removing one β-catenin allele, confirming β-catenin dependence.

### F006 — XAV939 dose-dependently rescues Wnt overactivity (partly via AXIN2)
In HEK293T cells engineered with AXIN1 p.Arg723* and p.Asp796Glufs*6, XAV939 at 100 nM and 1 µM produced dose-dependent suppression of Wnt activation; it also rescued AXIN1-knockout cells, implicating **AXIN2 stabilization**. Tankyrases PARylate AXIN1/AXIN2 for degradation, so their inhibition raises AXIN levels and restores destruction-complex activity ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)).

---

## Mechanistic Model (synthesis)

```
  Biallelic AXIN1 C-terminal truncation (p.Arg723*, p.Arg805*, frameshift)
                     │  removes/disrupts DIX domain
                     ▼
  ↓ AXIN1 protein level  +  impaired AXIN1 polymerization
                     │
                     ▼
  Weakened β-catenin destruction complex (AXIN1·APC·GSK3β·CK1)
                     │  ↓ β-catenin phosphorylation/degradation
                     ▼
  ↑ Nuclear β-catenin  →  ENHANCED canonical Wnt/β-catenin output   ◄── XAV939
                     │        (demonstrated in patient/edited cells)      (tankyrase
        ┌────────────┴─────────────┐                                       inhibitor,
        ▼                          ▼                                       stabilizes
  ↑ Osteoblast formation     ↑ OPG : RANKL ratio                           AXIN1/AXIN2
                                   │  (mouse model)                        → rescues)
                                   ▼
                             ↓ Osteoclast resorption
        └────────────┬─────────────┘
                     ▼
     NET ↑ BONE MASS → osteosclerosis / hyperostosis
                     ▼
  Macrocephaly · cranial/skull-base hyperostosis · sandwich vertebrae ·
  metaphyseal flaring · hip dysplasia · (cardiac, developmental, hematologic — inferred)
```

**Allele-dosage spectrum of AXIN1 dysfunction:**

| AXIN1 state | Wnt output | Outcome |
|---|---|---|
| Wild-type | Normal (destruction complex intact) | Healthy |
| Germline **biallelic hypomorphic** DIX truncation | Moderately ↑ (partial retained function) | **CMDOH** (viable skeletal dysplasia) |
| **Somatic complete inactivation** | Strongly ↑ (full Wnt activation, c-Myc/CCND1) | **Cancer** (e.g., HCC) |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/) | *AXIN1 bi-allelic variants disrupting the C-terminal DIX domain cause CMDOH* | **Primary defining paper** — gene, variants, phenotype, Wnt-gain mechanism, XAV939 rescue |
| [42237887](https://pubmed.ncbi.nlm.nih.gov/42237887/) | *Wnt/β-catenin in HCC* | Establishes AXIN1 as a Wnt tumor suppressor (dosage contrast) |
| [39653061](https://pubmed.ncbi.nlm.nih.gov/39653061/) | *Loss of AXIN1 & lenvatinib response in HCC* | Functional proof loss of AXIN1 activates Wnt/c-Myc |
| [40344393](https://pubmed.ncbi.nlm.nih.gov/40344393/) | *TP53/AXIN1/CTNNB1/KRAS in Mongolian HCC* | AXIN1 mutation ↑CCND1; β-catenin–CCND1 correlation |
| [9230313](https://pubmed.ncbi.nlm.nih.gov/9230313/) | *Axin (Fused locus): a novel Wnt inhibitor* | Foundational mouse genetics; Axin inhibits Wnt |
| [33824347](https://pubmed.ncbi.nlm.nih.gov/33824347/), [39084544](https://pubmed.ncbi.nlm.nih.gov/39084544/), [41408477](https://pubmed.ncbi.nlm.nih.gov/41408477/) | *TMEM53 craniotubular dysplasia (CTDI)* | Key **differential** — BMP-SMAD (not Wnt) sclerosing dysplasia |
| [18981475](https://pubmed.ncbi.nlm.nih.gov/18981475/) | *PTH signaling via LRP6/axin* | Context: axin/Wnt integration in osteoblast bone formation |
| [26763102](https://pubmed.ncbi.nlm.nih.gov/26763102/) | *Osteoblast exosomes inhibit Axin1* | Context: Axin1 suppression → Wnt activation promotes osteogenesis |

**Note on evidence strength:** The human genotype–phenotype and Wnt-gain findings rest on a **single, well-executed 7-patient study** with strong functional validation. The osteoblast/osteoclast step is supported by **model-organism** data. The tumor-suppressor/dosage framing is **inferential context** from cancer literature, not direct CMDOH data.

---

## Limitations and Knowledge Gaps

1. **Tiny cohort (n=7/4 families):** Frequencies, penetrance, expressivity, and prognosis are imprecise; the phenotype spectrum may broaden as more cases are found.
2. **No epidemiology:** Prevalence, incidence, carrier frequency, and geographic/ethnic distribution are unquantified.
3. **Extraskeletal mechanism is inferred:** How Wnt-gain produces the cardiac, hematological, and developmental features is not mechanistically dissected.
4. **No natural-history/QoL/survival data:** Long-term outcomes and QoL are undefined.
5. **Therapy is preclinical only:** XAV939 rescue is in-vitro; efficacy, safety, therapeutic window, and delivery in patients are unknown. Systemic tankyrase inhibition has known toxicity.
6. **No patient omics datasets** (transcriptomic/proteomic/single-cell) exist to refine cell-type-specific mechanisms.
7. **Modifier genetics unproven:** AXIN2 compensation is inferred from cell rescue, not demonstrated as a clinical modifier.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international CMDOH registry** and GeneMatcher-driven case collection to define prevalence, natural history, penetrance, and expressivity.
2. **Generate a knock-in mouse** carrying a patient-equivalent C-terminal *Axin1* truncation (e.g., R723*-analog) to recapitulate the craniospinal radiographic phenotype and test therapeutic windows.
3. **In-vivo XAV939 / next-generation tankyrase-inhibitor studies** in the knock-in model, defining dose, timing (early bone-modeling window), and skeletal/intestinal toxicity — a prerequisite before any human consideration.
4. **Patient-derived iPSC → osteoblast/osteoclast organoid models** to map cell-type-specific Wnt targets (RNA-seq/single-cell) and OPG:RANKL dynamics directly in human cells.
5. **Dissect extraskeletal mechanisms** (cardiac, hematopoietic) via conditional *Axin1*-truncation models in relevant lineages.
6. **Systematic differential-diagnosis workflow:** incorporate *AXIN1* into sclerosing-dysplasia gene panels and publish radiographic criteria distinguishing CMDOH (Wnt) from TMEM53/CTDI (BMP-SMAD) and osteopetroses.
7. **Biomarker development:** evaluate serum bone-turnover markers and Wnt-target readouts as potential monitoring/prognostic biomarkers.

---

*Report compiled from a 5-iteration autonomous investigation; 6 confirmed findings, 12 papers reviewed. Primary source: Terhal et al., 2023 ([PMID: 37582359](https://pubmed.ncbi.nlm.nih.gov/37582359/)).*


## Artifacts

- [OpenScientist final report](Craniometadiaphyseal_Osteosclerosis_With_Hip_Dysplasia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Craniometadiaphyseal_Osteosclerosis_With_Hip_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957832` (2 mentions) - the report calls it "MONDO"; MONDO calls it **craniometadiaphyseal osteosclerosis with hip dysplasia**
- `HP:0000256` (1 mention) - the report calls it "Core / very frequent"; HP calls it **Macrocephaly**
- `HP:0004437` (1 mention) - the report calls it "Core / very frequent"; HP calls it **Cranial hyperostosis**
- `HP:0004618` (1 mention) - the report calls it "Core / frequent"; HP calls it **Sandwich appearance of vertebral bodies**
- `HP:0003015` (1 mention) - the report calls it "Frequent"; HP calls it **Flared metaphysis**
- `HP:0001385` (1 mention) - the report calls it "Frequent"; HP calls it **Hip dysplasia**
- `HP:0001627` (1 mention) - the report calls it "Frequent"; HP calls it **Abnormal heart morphology**
- `HP:0001263` (1 mention) - the report calls it "Variable"; HP calls it **Global developmental delay**
- `HP:0001871` (1 mention) - the report calls it "Frequent"; HP calls it **Abnormality of blood and blood-forming tissues**
- `HP:0000316` (1 mention) - the report calls it "Frequent"; HP calls it **Hypertelorism**
- `HP:0005280` (1 mention) - the report calls it "Frequent"; HP calls it **Depressed nasal bridge**
- `HP:0004322` (1 mention) - the report calls it "Subset"; HP calls it **Short stature**