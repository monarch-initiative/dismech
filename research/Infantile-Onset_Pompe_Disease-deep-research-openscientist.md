---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:43:16.701555'
end_time: '2026-09-01T11:24:29.645536'
duration_seconds: 2472.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Infantile-Onset Pompe Disease
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
citation_count: 38
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 38
  on_topic: 36
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 38
  not_found: 1
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.026
  labels_checked: 35
  labels_matching: 18
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0001639
    reported_labels:
    - "Neonatal\u2013infantile, rapidly progressive"
    ontology_label: Hypertrophic cardiomyopathy
  - term_id: HP:0001640
    reported_labels:
    - Infantile, progressive
    ontology_label: Cardiomegaly
  - term_id: HP:0001324
    reported_labels:
    - Infantile, progressive
    ontology_label: Muscle weakness
  - term_id: HP:0001270
    reported_labels:
    - Infantile, progressive
    ontology_label: Motor delay
  - term_id: HP:0002093
    reported_labels:
    - Infantile, progressive
    ontology_label: Respiratory insufficiency
  - term_id: HP:0011968
    reported_labels:
    - Infantile
    ontology_label: Feeding difficulties
  - term_id: HP:0000158
    reported_labels:
    - Infantile
    ontology_label: Macroglossia
  - term_id: HP:0000191
    reported_labels:
    - Infantile
    ontology_label: Accessory oral frenulum
  - term_id: HP:0002240
    reported_labels:
    - Infantile
    ontology_label: Hepatomegaly
  - term_id: HP:0003236
    reported_labels:
    - Infantile
    ontology_label: Elevated circulating creatine kinase activity
  - term_id: HP:0000407
    reported_labels:
    - Emerges with prolonged survival
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0001260
    reported_labels:
    - Emerges with prolonged survival
    ontology_label: Dysarthria
  - term_id: HP:0000508
    reported_labels:
    - Later
    ontology_label: Ptosis
  labels_variant: 4
  unresolved_terms:
  - HP:0001728
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Infantile-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Infantile-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile-Onset Pompe Disease** covering all of the
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

# Infantile-Onset Pompe Disease (IOPD): A Comprehensive Disease-Characterization Report

*A Mendelian lysosomal storage disorder — glycogen storage disease type II, infantile form*

---

## Summary

**Infantile-Onset Pompe Disease (IOPD)** is a severe, autosomal-recessive lysosomal storage disorder (glycogen storage disease type II; OMIM #232300; MONDO:0009290; Orphanet ORPHA:79237) caused by biallelic loss-of-function variants in the *GAA* gene (17q25.3; HGNC:4065), which encodes lysosomal acid α-glucosidase (acid maltase; EC 3.2.1.20; UniProt P10253). Complete or near-complete loss of GAA enzyme activity prevents the lysosomal breakdown of glycogen to glucose, driving massive intralysosomal glycogen accumulation in cardiac, skeletal, and smooth muscle, and — as ERT-prolonged survival has unmasked — throughout the central nervous system. Untreated classic IOPD presents in the first months of life with a "floppy infant" picture of profound generalized hypotonia, rapidly progressive hypertrophic cardiomyopathy (with a pathognomonic short-PR/high-voltage-QRS/Wolff-Parkinson-White ECG signature), feeding and respiratory difficulty, and is uniformly fatal — usually by 1–2 years of age from cardiorespiratory failure.

The disease has been transformed by **enzyme replacement therapy (ERT)**. First-generation recombinant human GAA (alglucosidase alfa, FDA-approved 2006) prolongs ventilator-free survival and reverses cardiomyopathy, but its benefit is critically modulated by **CRIM (cross-reactive immunological material) status** and by the **age at which treatment begins**. Approximately 85–87% of IOPD patients are CRIM-positive; CRIM-negative patients cannot make any native GAA, mount high sustained anti-rhGAA antibody titers, and fail treatment unless given immune tolerance induction (rituximab + methotrexate ± IVIG). Newborn screening now enables ERT initiation in the neonatal window (≤4 weeks), improving outcomes, though residual skeletal-muscle disease, CNS involvement, and antibody risk persist. Next-generation ERTs — the bis-mannose-6-phosphate–enhanced **avalglucosidase alfa** and the second-generation **cipaglucosidase alfa plus the oral stabilizer miglustat** — address intrinsic limitations of first-generation rhGAA (blood-pH inactivation, inefficient uptake, incomplete processing). Investigational AAV gene therapy corrects multi-tissue (including CNS) storage preclinically but carries dorsal-root-ganglion toxicity risk in humans.

This report synthesizes **16 evidence-backed findings** drawn from **62 reviewed papers** spanning human clinical cohorts, pivotal ERT trials, natural-history and genotype–phenotype studies, animal models, and mechanistic work. The mechanistic through-line: *GAA null variants → absent enzyme → lysosomal glycogen entrapment → glycogenosome rupture → secondary autophagic/mTORC1–AMPK dysregulation and a metabolic shift to lipid fuel → multisystem (cardiac, skeletal, respiratory, CNS) failure.*

---

## Disease Overview and Identifiers (Section 1)

IOPD is the most severe end of the Pompe disease clinical spectrum. Pompe disease as a whole is defined by deficiency of the lysosomal enzyme acid α-glucosidase and consequent intralysosomal glycogen accumulation. As stated in a 2025 review, *"Pompe disease (PD) is a rare genetic disorder that leads to intralysosomal glycogen accumulation because of a deficiency in the lysosomal enzyme acid α-glucosidase (GAA), which is required to break down glycogen to glucose"* ([PMID: 40237692](https://pubmed.ncbi.nlm.nih.gov/40237692/)). The infantile form is distinguished clinically by *"severe and progressive hypertrophic cardiomyopathy and muscle weakness with death in the first 2 years of life if left untreated"* ([PMID: 39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/)).

| Resource | Identifier |
|----------|-----------|
| OMIM | #232300 (glycogen storage disease II) |
| MONDO | MONDO:0009290 (glycogen storage disease II); IOPD subtype under Pompe disease |
| Orphanet | ORPHA:79237 (infantile-onset) / ORPHA:365 (Pompe) |
| ICD-10 | E74.02 (Pompe disease) |
| ICD-11 | 5C51.3 |
| MeSH | D006009 (Glycogen Storage Disease Type II) |
| Gene | *GAA*, HGNC:4065, NCBI Gene 2548, Ensembl ENSG00000171298 |
| Protein | UniProt P10253 (lysosomal α-glucosidase) |
| Enzyme | EC 3.2.1.20 |

**Synonyms / alternative names:** Pompe disease (infantile form), glycogen storage disease type II (GSD II / GSDII), acid maltase deficiency, acid α-1,4-glucosidase deficiency, classic infantile Pompe disease, cardiomegalia glycogenica.

**Source of information:** The evidence base is largely aggregated disease-level (natural history studies, registries, clinical trials, systematic reviews) supplemented by individual case reports and single-center cohorts; it is not primarily EHR-derived.

---

## Etiology (Section 2)

**Primary cause — genetic.** IOPD is a monogenic, autosomal-recessive disorder caused by **biallelic loss-of-function variants in *GAA***. The disorder is *"caused by a deficiency in acid α-glucosidase (GAA), … a lysosomal storage disorder"* ([PMID: 41742217](https://pubmed.ncbi.nlm.nih.gov/41742217/)). There is no environmental or infectious cause.

**Genetic risk factors.** The disease-causal factors are the two inherited pathogenic *GAA* alleles. IOPD specifically results from **two "severe/null" variants** (nonsense, frameshift, large deletions, canonical splice) producing near-absent enzyme, in contrast to late-onset Pompe disease (LOPD), where the common "leaky" splice variant **c.-32-13T>G (IVS1)** retains residual activity ([PMID: 38958145](https://pubmed.ncbi.nlm.nih.gov/38958145/); [PMID: 34020684](https://pubmed.ncbi.nlm.nih.gov/34020684/)). Genotype determines both phenotype severity and CRIM status.

**Environmental / lifestyle / infectious factors.** None are causal. IOPD is fully penetrant given a severe biallelic genotype; sex is not a risk factor (autosomal). Family history and consanguinity increase recurrence risk in the classic Mendelian sense.

**Protective factors.** No environmental protective factors are established. The principal disease-modifying factor is therapeutic (early ERT + immune tolerance). At the molecular level, any residual GAA activity (as conferred by "leaky" alleles) shifts phenotype toward the milder late-onset spectrum, functioning as an intrinsic genetic modifier of severity.

**Gene–environment interactions.** Not applicable in the classical toxicological sense. The clinically important "interaction" is between the patient's *GAA* genotype (CRIM status) and the therapeutic environment (ERT + immunomodulation): *"Variant pathogenicity correlated with both CRIM status and clinical outcomes"* ([PMID: 40952111](https://pubmed.ncbi.nlm.nih.gov/40952111/)).

---

## Phenotypes (Section 3)

Classic IOPD presents in the first months of life. In a case series of six Chinese infantile GSD II patients (onset birth to 3 months), *"All patients had varying degrees of generalized muscle weakness, hypotonia and development retardation or retrogression. Other common findings were feeding difficulties in two patients, tongue weakness in two patients, respiratory distress in four patients, macroglossia in one patient, and hepatomegaly in two patients. Left ventricular hypertrophy and cardiomegaly were obvious in all the six patients"* ([PMID: 26310554](https://pubmed.ncbi.nlm.nih.gov/26310554/)).

| Phenotype | Type | Frequency | Onset / progression | HPO term |
|-----------|------|-----------|--------------------|----------|
| Hypertrophic cardiomyopathy | Physical/imaging | ~100% (universal) | Neonatal–infantile, rapidly progressive | HP:0001639 |
| Cardiomegaly | Imaging sign | ~100% | Infantile, progressive | HP:0001640 |
| Generalized muscle hypotonia ("floppy infant") | Clinical sign | ~100% | Infantile, progressive | HP:0001290 / HP:0001252 |
| Muscle weakness | Symptom | ~100% | Infantile, progressive | HP:0001324 |
| Motor delay / developmental regression | Sign | High | Infantile, progressive | HP:0001270 |
| Respiratory distress / insufficiency | Sign | ~65% (4/6) | Infantile, progressive | HP:0002093 |
| Feeding difficulties | Symptom | ~30% | Infantile | HP:0011968 |
| Macroglossia | Physical | Variable (~17%) | Infantile | HP:0000158 |
| Tongue weakness | Sign | ~30% | Infantile | HP:0000191 |
| Hepatomegaly | Sign | ~30% | Infantile | HP:0002240 |
| Short PR interval / WPW pre-excitation | Lab/ECG | Common | Infantile, may present | HP:0005165 / HP:0001728 |
| Elevated creatine kinase | Lab abnormality | High | Infantile | HP:0003236 |
| Sensorineural hearing loss (ERT survivors) | Sign | 6/8 in long-term cohort | Emerges with prolonged survival | HP:0000407 |
| Flaccid dysarthria (ERT survivors) | Sign | 8/8 | Emerges with prolonged survival | HP:0001260 |
| Ptosis (ERT survivors) | Sign | ~4/8 | Later | HP:0000508 |

**Severity and progression.** Untreated classic IOPD is uniformly severe and relentlessly progressive, fatal within ~1–2 years. **Quality-of-life impact** is profound: infants lose feeding, motor, and respiratory function; long-term ERT survivors, though alive into adulthood, retain substantial multisystem morbidity — *"Two participants were ambulatory; 6 used wheelchairs. Flaccid dysarthria (8/8), ptosis (4/8), and sensorineural hearing loss (6/8) were common"* ([PMID: 41014101](https://pubmed.ncbi.nlm.nih.gov/41014101/)).

---

## Genetic / Molecular Information (Section 4)

**Causal gene:** *GAA* (acid alpha-glucosidase), 17q25.3, HGNC:4065, OMIM *606800; disease OMIM #232300.

**Pathogenic variant spectrum.** IOPD arises from two severe/null alleles. In a Mexican cohort, *"Among the 23 different variants identified in the GAA gene, 14 were classified as pathogenic, 5 were likely pathogenic, and 1 was a variant of uncertain significance"* per ACMG/AMP, with **c.-32-13T>G** (the LOPD-associated leaky splice allele) most frequent overall ([PMID: 38958145](https://pubmed.ncbi.nlm.nih.gov/38958145/)). Representative IOPD nonsense/frameshift variants include **c.1822C>T (p.R608*)**, **c.2662G>T (p.E888*)**, **c.2560C>T (p.R854*)**, and the frameshift **c.236_246delCCACACAGTGC**, the latter homozygous state being *"associated with early disease and a worse prognosis"* ([PMID: 34020684](https://pubmed.ncbi.nlm.nih.gov/34020684/)).

**Population-specific variants.** In a Vietnamese cohort, *"The most frequent variants were c.1843G > A and c.1933G > C"* ([PMID: 40952111](https://pubmed.ncbi.nlm.nih.gov/40952111/)), with two novel variants (c.2016del, c.1723T>C) reported — illustrating founder/population enrichment.

**Variant classification & type.** Pathogenic/likely-pathogenic per ACMG/AMP; classes span missense, nonsense, frameshift, splice-site, and structural deletions. IOPD genotypes are enriched for null/severe classes; **functional consequence is loss of function** (near-complete enzyme deficiency). All variants are **germline**; somatic origin is not relevant.

**CRIM status.** Genotype predicts whether any GAA protein is made. Most IOPD patients are CRIM-positive (~85–87%): *"CRIM-positive status was identified in 87.0% of IOPD and 33.3% of LOPD patients"* ([PMID: 40952111](https://pubmed.ncbi.nlm.nih.gov/40952111/)). CRIM-negative patients (two truly null alleles) make no cross-reacting protein and are at highest immunogenic risk.

**Modifier genes / epigenetics / chromosomal abnormalities.** No robust modifier genes beyond *GAA* genotype itself are established; the principal modifier of severity is residual enzyme activity conferred by leaky alleles. No specific epigenetic marks or large-scale chromosomal abnormalities characterize IOPD.

**Pseudodeficiency caveat.** East Asian pseudodeficiency alleles complicate screening: the **c.[752C>T;761C>T]** haplotype is *"markedly enriched in East Asian populations (allele frequencies: 0.259% for c.752C > T and 0.263% for c.761C > T)"* and lowers measured enzyme without causing disease ([PMID: 42320386](https://pubmed.ncbi.nlm.nih.gov/42320386/)).

---

## Environmental Information (Section 5)

IOPD is a purely genetic Mendelian disorder. **No environmental toxins, radiation, pollutants, occupational exposures, lifestyle factors, or infectious agents cause or trigger it.** Intercurrent infection can precipitate cardiorespiratory decompensation in an affected infant (e.g., a 5-month-old presenting with fever and heart failure who was found to carry homozygous c.2662G>T; [PMID: 38450370](https://pubmed.ncbi.nlm.nih.gov/38450370/)), but such infections are non-specific stressors, not etiologic agents.

---

## Mechanism / Pathophysiology (Section 6)

### Ordered causal chain

1. **Biallelic severe/null *GAA* variants** → *lead to* absent or near-absent lysosomal acid α-glucosidase (loss of function). *(Demonstrated.)*
2. **Absent GAA** → *results in* failure to hydrolyze lysosomal glycogen to glucose → progressive **intralysosomal glycogen accumulation** in cardiac, skeletal, and smooth muscle. *(Demonstrated — [PMID: 40237692](https://pubmed.ncbi.nlm.nih.gov/40237692/).)*
3. **Glycogen entrapment** → *leads to* segregation of glycogen during autophagy, phagolysosomal accumulation of undigested glycogen, and eventually **rupture of distended glycogenosomes** (confirmed lysosomal by increased acid phosphatase). *(Demonstrated in canine and human GSD II — [PMID: 3921759](https://pubmed.ncbi.nlm.nih.gov/3921759/).)*
4. **Lysosomal dysfunction** → *sets in motion* "extra-lysosomal" events: **defective autophagy** (autophagosome accumulation), **disruption of mTORC1/AMPK signaling**, and a **metabolic/energetic deficit** — decreased glycolytic-pathway metabolites and a **shift to lipids as the energy source** in diseased muscle. *(Demonstrated — [PMID: 32671132](https://pubmed.ncbi.nlm.nih.gov/32671132/); reversal by gene therapy confirms causality — [PMID: 37463048](https://pubmed.ncbi.nlm.nih.gov/37463048/).)*
5. **BRANCH A — Cardiac:** myocardial glycogen storage → *causes* massive **hypertrophic cardiomyopathy** and a conduction signature (short PR, high-voltage QRS, WPW) → *leads to* heart failure/arrhythmia and, untreated, death. *(Demonstrated.)*
6. **BRANCH B — Skeletal/respiratory muscle:** myofiber storage + autophagic buildup → *causes* generalized weakness, hypotonia, diaphragmatic failure → respiratory insufficiency. *(Demonstrated.)*
7. **BRANCH C — CNS (unmasked by ERT-prolonged survival):** neuronal and glial glycogen accumulation (astrocytes, globus pallidus, brainstem motor nuclei, anterior horn cells) → *contributes to* white-matter changes, dysarthria, hearing loss. *(Demonstrated histopathologically — [PMID: 42538472](https://pubmed.ncbi.nlm.nih.gov/42538472/).)*
8. **Mitochondrial dysfunction** is reported to accompany lysosomal storage, potentially amplifying cardiac energetic failure. *(Inferred / emerging — [PMID: 38450370](https://pubmed.ncbi.nlm.nih.gov/38450370/).)*

### ASCII mechanistic model

```
 GAA null/null genotype
        |
        v
 Absent acid α-glucosidase  (loss of function; GO:0004558)
        |
        v
 Lysosomal glycogen NOT hydrolyzed  --> intralysosomal glycogen accumulation
        |                                (lysosome; GO:0005764)
        v
 Glycogenosome distension --> RUPTURE (acid phosphatase +)
        |
        +--> Impaired autophagy (autophagosome buildup; GO:0006914)
        +--> mTORC1 / AMPK signaling dysregulation
        +--> Glycolytic metabolite drop --> shift to LIPID fuel (energy deficit)
        |
  ------+------------------------------+---------------------------+
  |                                    |                           |
  v                                    v                           v
CARDIAC muscle                  SKELETAL/DIAPHRAGM            CNS neurons + glia
(CL:0000746)                    (CL:0000188)                  (astrocytes CL:0000127)
  |                                    |                           |
Hypertrophic CM,                Hypotonia, weakness,          White-matter change,
short-PR/WPW                    respiratory failure           dysarthria, hearing loss
  |                                    |                           |
  +------------------ Untreated: death by 1-2 y ------------------+
```

### Molecular / cellular / metabolic detail

- **Molecular pathways:** lysosomal glycogen catabolism (defective); autophagy; mTORC1/AMPK nutrient-sensing signaling (dysregulated) — [PMID: 37463048](https://pubmed.ncbi.nlm.nih.gov/37463048/).
- **Cellular processes:** macroautophagy failure, autophagic vacuole accumulation, glycogenosome rupture, cellular energy stress — [PMID: 32671132](https://pubmed.ncbi.nlm.nih.gov/32671132/).
- **Protein dysfunction:** loss of function of GAA (misfolding/truncation/absence depending on variant class).
- **Metabolic changes:** decreased glycolytic intermediates, compensatory reliance on lipid oxidation in diseased muscle — [PMID: 32671132](https://pubmed.ncbi.nlm.nih.gov/32671132/).
- **Immune involvement:** not autoimmune, but immunogenicity of ERT (anti-rhGAA IgG) is a central therapeutic problem, especially in CRIM-negative patients — [PMID: 39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/).
- **Tissue damage mechanisms:** mechanical disruption of myofibers by glycogen-laden/ruptured lysosomes, autophagic buildup, energetic failure.

**Suggested GO terms:** GO:0004558 (alpha-1,4-glucosidase activity), GO:0005764 (lysosome), GO:0006914 (autophagy), GO:0005977 (glycogen metabolic process), GO:0005980 (glycogen catabolic process). **CL terms:** CL:0000746 (cardiac muscle cell), CL:0000188 (skeletal muscle cell), CL:0000187 (muscle cell), CL:0000127 (astrocyte), CL:0000540 (neuron).

---

## Anatomical Structures Affected (Section 7)

**Organ level (primary):** heart (myocardium), skeletal muscle, diaphragm, tongue. **Secondary/associated:** liver (hepatomegaly), CNS, and — in canine model — esophagus (dilatation). **Body systems:** cardiovascular, musculoskeletal, respiratory, and (with prolonged survival) nervous system.

**Tissue/cell level:** striated (cardiac and skeletal) muscle is the principal target; smooth muscle also affected. CNS histopathology shows *"The cerebral and cerebellar white matter (WM), globus pallidus, dentate nucleus, motor nuclei of the brainstem, and anterior horn cells were most frequently affected. Glycogen accumulation was severe in astrocytes and in neurons of the globus pallidus"* ([PMID: 42538472](https://pubmed.ncbi.nlm.nih.gov/42538472/)).

**Subcellular level:** the **lysosome** (GO:0005764) is the primary compartment of pathology; secondary involvement of **autophagosomes** (GO:0005776) and **mitochondria** (GO:0005739).

**Localization / lateralization:** involvement is **bilateral and generalized/systemic** rather than focal.

**Suggested UBERON terms:** UBERON:0000948 (heart), UBERON:0001133 (cardiac muscle), UBERON:0001134 (skeletal muscle tissue), UBERON:0001103 (diaphragm), UBERON:0002240 (spinal cord), UBERON:0002037 (cerebellum), UBERON:0001873 (globus pallidus), UBERON:0002107 (liver), UBERON:0001723 (tongue).

---

## Temporal Development (Section 8)

**Onset:** congenital/neonatal to early infancy; symptom onset typically within the first weeks to 3 months of life ([PMID: 26310554](https://pubmed.ncbi.nlm.nih.gov/26310554/)). Onset pattern is **subacute and rapidly progressive**.

**Progression:** untreated classic IOPD is **relentlessly progressive** with no plateau, reaching end-stage cardiorespiratory failure and death within the first 1–2 years ([PMID: 39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/)). With ERT, cardiomyopathy regresses and survival is prolonged, converting an acute-fatal course into a chronic, lifelong disease with residual skeletal-muscle and emerging CNS morbidity.

**Critical period / therapeutic window:** the **neonatal period** is the window of opportunity. Early ERT (≤4 weeks, newborn-screening-enabled) improves outcomes: *"These data highlight the benefits of early ERT initiation and ITI, along with high-dose ERT. Despite early treatment, patients with IOPD remain at risk of developing HSAT"* ([PMID: 41536902](https://pubmed.ncbi.nlm.nih.gov/41536902/)).

**Remission:** no spontaneous remission. Cardiac hypertrophy is treatment-reversible; skeletal and CNS disease are only partially controlled.

---

## Inheritance and Population (Section 9)

**Inheritance:** autosomal recessive.

**Epidemiology.** Birth prevalence of IOPD, from newborn-screening programs, *"ranged from 1 in 297,387 in Japan to 1 in 62,186 in Taiwan"* ([PMID: 40329343](https://pubmed.ncbi.nlm.nih.gov/40329343/)). In a US program, *"Two newborns were diagnosed with Infantile Onset Pompe Disease (IOPD), and 31 newborns were confirmed to have Late Onset Pompe Disease (LOPD). The incidence of IOPD + LOPD was 1:16,095"* ([PMID: 33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/)).

| Population | IOPD birth prevalence | Source |
|-----------|----------------------|--------|
| Japan | 1 : 297,387 | [PMID: 40329343](https://pubmed.ncbi.nlm.nih.gov/40329343/) |
| Taiwan | 1 : 62,186 | [PMID: 40329343](https://pubmed.ncbi.nlm.nih.gov/40329343/) |
| Pennsylvania, USA | IOPD+LOPD combined 1 : 16,095 | [PMID: 33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/) |

**Penetrance / expressivity:** essentially complete penetrance given a severe biallelic genotype; expressivity is relatively consistent within IOPD (uniformly severe), with residual-activity alleles shifting toward LOPD.

**Founder effects / population variants:** population-specific enrichment exists (e.g., c.1843G>A and c.1933G>C in Vietnamese patients — [PMID: 40952111](https://pubmed.ncbi.nlm.nih.gov/40952111/); East Asian pseudodeficiency haplotype — [PMID: 42320386](https://pubmed.ncbi.nlm.nih.gov/42320386/)).

**Consanguinity** increases risk of homozygous severe genotypes. **Sex ratio** ~1:1 (autosomal). **Genetic anticipation and germline mosaicism** are not features. **CRIM distribution:** ~85–87% CRIM-positive ([PMID: 40952111](https://pubmed.ncbi.nlm.nih.gov/40952111/)).

---

## Diagnostics (Section 10)

**Enzyme assay:** decreased/absent GAA activity is the biochemical hallmark; classic IOPD typically shows <1% of normal activity ([PMID: 16860134](https://pubmed.ncbi.nlm.nih.gov/16860134/)). Measured by tandem mass spectrometry on dried blood spots (screening) with confirmatory assay.

**Biomarker — urinary glucose tetrasaccharide (Glc4/Hex4).** The tetraglucose oligomer Glcα1-6Glcα1-4Glcα1-4Glc (Glc4) is diagnostic and treatment-monitoring. Baseline urinary Glc4 and plasma Hex4 are markedly elevated versus controls, and *"Both urinary Glc4 and plasma Hex4 levels decreased after initiation of ERT for all patients. In the four patients with the best overall clinical response in both skeletal and cardiac muscle, levels decreased to within, or near, normal levels during the first year of treatment. In contrast, levels fluctuated and were persistently elevated above the control ranges in those patients with a less favorable clinical response"* ([PMID: 15886040](https://pubmed.ncbi.nlm.nih.gov/15886040/)). Measured by HPLC-UV and stable-isotope-dilution ESI-MS/MS. **Analyte:** urinary hexose tetrasaccharide (LOINC-type).

**Imaging / functional:** echocardiography (LV hypertrophy, cardiomegaly), chest radiograph (increased cardiothoracic ratio), and cardiac evaluation ([PMID: 18661169](https://pubmed.ncbi.nlm.nih.gov/18661169/)).

**Electrophysiology (ECG):** characteristic **short PR interval, giant high-voltage QRS, and WPW/pre-excitation**. *"ECG showed a shortened PR interval, with huge QRS complexes and biventricular hypertrophy"* ([PMID: 18995995](https://pubmed.ncbi.nlm.nih.gov/18995995/)); WPW may be the presenting sign — *"The initial symptoms were hypertrophic cardiomyopathy with Wolf-Parkinson-White syndrome"* ([PMID: 12162158](https://pubmed.ncbi.nlm.nih.gov/12162158/)).

**Genetic testing:** *GAA* sequencing (single-gene, panel, WES, or WGS) confirms diagnosis, defines variant pathogenicity, and — critically — **predicts CRIM status** for treatment planning. There has been a *"major shift from direct CRIM testing using western blotting and mutation analysis to CRIM status prediction based on genetic variant analysis"* ([PMID: 41583481](https://pubmed.ncbi.nlm.nih.gov/41583481/)). Creatine kinase is typically elevated.

**Screening:** newborn screening (tandem-MS GAA activity on dried blood spots with second-tier *GAA* sequencing) detects most cases and enables neonatal ERT ([PMID: 40329343](https://pubmed.ncbi.nlm.nih.gov/40329343/), [PMID: 33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/)). Pseudodeficiency alleles cause false positives requiring confirmatory genotyping ([PMID: 42320386](https://pubmed.ncbi.nlm.nih.gov/42320386/)).

**Differential diagnosis:** other causes of infantile hypertrophic cardiomyopathy and floppy infant (other glycogenoses, mitochondrial cardiomyopathies, congenital myopathies, spinal muscular atrophy, endocardial fibroelastosis). The GAA enzyme assay and *GAA* genotype are distinguishing.

---

## Outcome / Prognosis (Section 11)

**Natural history (untreated):** uniformly fatal in the first 1–2 years from cardiorespiratory failure ([PMID: 39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/)).

**With ERT — survival transformed.** The landmark first multinational IOPD trial (n=8, rhGAA 10 mg/kg weekly) reported that *"the median age at death or treatment withdrawal for all patients was 21.7 months, significantly later than expected for patients who were not treated. … rhGAA improved ventilator-free survival, cardiomyopathy, growth, and motor function in patients with infantile-onset Pompe disease"* ([PMID: 16860134](https://pubmed.ncbi.nlm.nih.gov/16860134/)). The larger phase IV ADVANCE study (113 patients, 87 IOPD) found *"Overall survival was 98.1% overall, 97.6% IOPD, 100% LOPD; 92.4% remained invasive ventilator-free (93.4% IOPD, 88.7% LOPD)"* ([PMID: 29565424](https://pubmed.ncbi.nlm.nih.gov/29565424/)). In a real-life cohort, *"Event incidence was significantly lower in the ERT group (HR = 0.06)"* ([PMID: 41453391](https://pubmed.ncbi.nlm.nih.gov/41453391/)).

**Residual morbidity in long-term survivors.** Two decades of ERT experience show *"Cardiac hypertrophy was resolved in all; 2 developed arrhythmias requiring intervention. None of the participants required invasive ventilation. Two participants were ambulatory; 6 used wheelchairs. Flaccid dysarthria (8/8), ptosis (4/8), and sensorineural hearing loss (6/8) were common"* ([PMID: 41014101](https://pubmed.ncbi.nlm.nih.gov/41014101/)); white-matter hyperintensities are present but stay mild-to-moderate with stable cognition.

**Mortality where access/timing is limited remains high:** in a Vietnamese cohort, *"Despite ERT administration in 52.9% of patients, overall mortality in the infantile group was 60.8%"* ([PMID: 40952111](https://pubmed.ncbi.nlm.nih.gov/40952111/)).

**Prognostic factors:** CRIM status, age at ERT initiation, ERT dose, immune-tolerance induction, and antibody titers. Persistently elevated Glc4/Hex4 predicts poorer skeletal-muscle response ([PMID: 15886040](https://pubmed.ncbi.nlm.nih.gov/15886040/)).

---

## Treatment (Section 12)

### Enzyme replacement therapy (mainstay)

Three ERTs are now approved: *"three agents now approved — alglucosidase alfa, avalglucosidase alfa, and cipaglucosidase alfa plus miglustat"* ([PMID: 42538546](https://pubmed.ncbi.nlm.nih.gov/42538546/)).

| Agent | Class / design | Key evidence | NCIT-type concept |
|-------|---------------|--------------|-------------------|
| **Alglucosidase alfa** (rhGAA; FDA 2006) | First-generation recombinant human GAA, IV 20 mg/kg q2w | Prolongs ventilator-free survival, reverses cardiomyopathy ([PMID: 16860134](https://pubmed.ncbi.nlm.nih.gov/16860134/), [PMID: 29565424](https://pubmed.ncbi.nlm.nih.gov/29565424/)) | Alglucosidase Alfa |
| **Avalglucosidase alfa** | bis-M6P hexasaccharide–enhanced rhGAA (greater M6PR uptake) | Mini-COMET: motor-function trends favor 40 mg/kg q2w; well tolerated ≥97 wk ([PMID: 36542086](https://pubmed.ncbi.nlm.nih.gov/36542086/), [PMID: 40449831](https://pubmed.ncbi.nlm.nih.gov/40449831/)) | Avalglucosidase Alfa |
| **Cipaglucosidase alfa + miglustat** | Second-gen bis-M6P-enriched rhGAA + oral enzyme stabilizer | PROPEL switch: better 6MWD/FVC responses; combined OR 4.05 ([PMID: 41650629](https://pubmed.ncbi.nlm.nih.gov/41650629/), [PMID: 41769220](https://pubmed.ncbi.nlm.nih.gov/41769220/)) | Cipaglucosidase Alfa; Miglustat |

First-generation rhGAA has intrinsic limitations — *"such as enzyme inactivation at the near-neutral pH of blood, inefficient target cell uptake, and a necessity for complete lysosomal processing once inside target cells"* ([PMID: 41769220](https://pubmed.ncbi.nlm.nih.gov/41769220/)) — that the next-generation agents address; in adult trials both *"are at least as efficacious as alglucosidase alfa and possess a comparable safety profile"* ([PMID: 40471681](https://pubmed.ncbi.nlm.nih.gov/40471681/)). Avalglucosidase alfa's design conjugates *"multiple synthetic bis-M6P-containing hexasaccharides to sialic acids present on the enzyme, thus enhancing M6PR targeting, enzyme uptake, glycogen clearance, and therapeutic outcomes"* ([PMID: 40237692](https://pubmed.ncbi.nlm.nih.gov/40237692/)). The switch benefit is quantified in PROPEL: *"Overall, 50.8 % versus 13.3 % of patients experienced improvements in 6MWD (% predicted) and/or FVC with cipa+mig versus alg+pbo"* ([PMID: 41650629](https://pubmed.ncbi.nlm.nih.gov/41650629/)).

### Immune tolerance induction (ITI) — essential for CRIM-negative patients

*"The inability of CRIM-negative IOPD patients to produce native GAA exposes them to a high risk of development of anti-rhGAA IgG antibody titers, leading to treatment failure"* ([PMID: 39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/)). Prophylactic ITI (rituximab + methotrexate ± IVIG) controls anti-drug antibodies and improves outcomes; ITI benefit also extends to some CRIM-positive patients ([PMID: 41583481](https://pubmed.ncbi.nlm.nih.gov/41583481/)). Hypersensitivity reactions can be managed by structured desensitization even in very young infants ([PMID: 41549377](https://pubmed.ncbi.nlm.nih.gov/41549377/)).

### Cardiac effect of ERT

ERT rapidly reverses the cardiac phenotype: *"The QRS voltage (SV1+RV6) decreased from 13 to 2.9 mV after 32 weeks of ERT"* ([PMID: 18995995](https://pubmed.ncbi.nlm.nih.gov/18995995/)); real-world data show *"Hypertrophic cardiomyopathy normalized in all patients, though electrocardiogram abnormalities persisted in 36%"* ([PMID: 41576647](https://pubmed.ncbi.nlm.nih.gov/41576647/)), and *"most of the treated patients had rapid regression of ventricular hypertrophy in response to ERT"* ([PMID: 18661169](https://pubmed.ncbi.nlm.nih.gov/18661169/)).

### Investigational — gene therapy

Systemic AAV gene therapy *"reversed glycogen storage in all key therapeutic targets — skeletal and cardiac muscles, the diaphragm, and the central nervous system — in both young and severely affected old Gaa-knockout mice"* and reversed autophagy/mTORC1–AMPK abnormalities ([PMID: 37463048](https://pubmed.ncbi.nlm.nih.gov/37463048/)). However, a human safety signal exists: *"a 49-year-old woman with Pompe disease who developed a sensory neuronopathy after receiving AT845, an investigational adeno-associated virus (AAV) gene replacement therapy"* ([PMID: 42142433](https://pubmed.ncbi.nlm.nih.gov/42142433/)) — consistent with AAV-associated dorsal-root-ganglion toxicity.

### Supportive / rehabilitative

Respiratory support, nutritional/feeding support, physical/occupational/speech therapy, and cardiology management (including arrhythmia care) are integral. Personalized medicine is **genotype- and CRIM-guided**: variant analysis directs ITI decisions and treatment intensity.

---

## Prevention (Section 13)

- **Primary prevention:** none possible for a Mendelian genetic disease; the relevant intervention is **reproductive genetic counseling** for at-risk families (carrier testing, prenatal diagnosis, preimplantation genetic testing). One CRIM-negative case was prenatally diagnosed enabling immediate management ([PMID: 33013846](https://pubmed.ncbi.nlm.nih.gov/33013846/)).
- **Secondary prevention:** **newborn screening** is the cornerstone — early detection enables pre-symptomatic/neonatal ERT (the critical window) ([PMID: 33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/), [PMID: 41536902](https://pubmed.ncbi.nlm.nih.gov/41536902/)). Cascade/carrier screening in affected families.
- **Tertiary prevention:** ITI to prevent antibody-mediated treatment failure; cardiac surveillance for arrhythmia; respiratory and nutritional management to prevent complications.
- **Immunization / public-health / environmental measures:** not applicable to disease causation (standard infant vaccination remains appropriate given respiratory vulnerability).

---

## Other Species / Natural Disease (Section 14)

Naturally occurring GSD II occurs across species: *"Naturally occurring animal homologs of LSDs have been described in the mouse, rat, dog, cat, guinea pig, emu, quail, goat, cattle, sheep, and pig"* ([PMID: 15133760](https://pubmed.ncbi.nlm.nih.gov/15133760/)). The canine (Lapland dog) natural model is especially faithful: *"Canine GSD II closely parallels the infantile form of the human disease, except for the presence of oesophageal dilatation. Generalized glycogen storage particularly affected muscular tissues (skeletal, oesophageal, cardiac and smooth muscle)"* ([PMID: 3921759](https://pubmed.ncbi.nlm.nih.gov/3921759/)).

- **Taxonomy / breeds:** dog (*Canis familiaris*, NCBI Taxon 9615; Lapland dog), cat (*Felis catus*, 9685), Japanese quail (*Coturnix japonica*, 93934), cattle (*Bos taurus*, 9913; Brahman, Shorthorn), sheep (*Ovis aries*, 9940).
- **Orthologous gene:** *GAA* is conserved (mouse *Gaa*, NCBI Gene 14618).
- **Comparative biology:** disease mechanism (lysosomal glycogen storage from GAA deficiency) is evolutionarily conserved, underpinning the translational value of animal models. Esophageal/megaesophagus involvement is a distinguishing canine feature.
- **Transmission:** none — non-infectious, inherited; no zoonotic potential.

---

## Model Organisms (Section 15)

**Mouse (workhorse model).** *Gaa*-knockout mice are the standard model. A modern CRISPR compound-heterozygous knock-in — *"CRISPR/Cas9-mediated knock-in introduced R608* (exon 14) and K889* (exon 18) mutations into C57BL/6 zygotes"* — recapitulates reduced GAA activity, elevated plasma glycogen, cardiac hypertrophy, and diaphragm/skeletal-muscle pathology, more faithfully modeling patient compound-heterozygous genotypes ([PMID: 41742217](https://pubmed.ncbi.nlm.nih.gov/41742217/)).

| Model | Type | Recapitulation | Key use | Ref |
|-------|------|----------------|---------|-----|
| *Gaa*-KO mouse | Mammalian knockout | Multi-tissue storage incl. CNS; autophagy/mTORC1–AMPK defects | ERT & AAV gene-therapy testing | [PMID: 37463048](https://pubmed.ncbi.nlm.nih.gov/37463048/) |
| *Gaa* R608*/K889* knock-in mouse | Compound-het knock-in | Reduced GAA, ↑plasma glycogen, cardiac hypertrophy, diaphragm pathology | Genotype-faithful modeling | [PMID: 41742217](https://pubmed.ncbi.nlm.nih.gov/41742217/) |
| Lapland dog | Natural mammalian | Closely parallels human infantile disease (+esophageal dilatation) | Comparative pathology, large-animal therapy | [PMID: 3921759](https://pubmed.ncbi.nlm.nih.gov/3921759/) |
| Japanese quail | Natural avian | Generalized glycogen storage | Natural LSD homolog | [PMID: 15133760](https://pubmed.ncbi.nlm.nih.gov/15133760/) |

**Model applications:** dissecting downstream pathogenesis (autophagy, signaling, metabolism), and preclinical testing of ERT and AAV gene therapy — AAV correction of storage and secondary abnormalities in *Gaa*-KO mice ([PMID: 37463048](https://pubmed.ncbi.nlm.nih.gov/37463048/)) supported clinical translation. Adjunctive β2-agonists (clenbuterol, salmeterol) that upregulate CI-MPR enhance muscle enzyme uptake in mouse models ([PMID: 24448824](https://pubmed.ncbi.nlm.nih.gov/24448824/), [PMID: 30803275](https://pubmed.ncbi.nlm.nih.gov/30803275/)).

**Model limitations:** murine models may under-represent the full human CNS phenotype and long-term skeletal-muscle refractoriness; immune responses to human GAA differ between species. **Resources:** MGI, IMSR for mouse lines.

---

## Mechanistic Model / Interpretation

The unifying interpretation is that **a single enzymatic lesion cascades into multisystem disease**. Absent GAA blocks the terminal step of lysosomal glycogen catabolism; the lysosome fills, distends, and ruptures, and — crucially — the pathology is *not* confined to the lysosome. Downstream "extra-lysosomal" consequences (autophagic block, mTORC1/AMPK dysregulation, a glycolysis-to-lipid metabolic shift) explain why simply restoring enzyme (ERT) reverses cardiac storage dramatically yet incompletely rescues skeletal muscle: cardiomyocytes take up mannose-6-phosphate-tagged enzyme efficiently, whereas skeletal muscle has low CI-MPR density and heavy autophagic burden that impede enzyme delivery. This mechanistic asymmetry is mirrored clinically (cardiac hypertrophy resolves in all long-term survivors while many remain wheelchair-dependent) and biochemically (Glc4/Hex4 normalizes with good skeletal response but stays elevated with poor response). The CNS, historically "silent" because patients died before neurological disease manifested, is now an emerging frontier unmasked by ERT-prolonged survival — and because intravenous rhGAA does not cross the blood–brain barrier, it is precisely the compartment that motivates CNS-penetrant AAV gene therapy. Finally, **CRIM status is the genetic switch that couples genotype to immunology to outcome**: null/null patients make no tolerogenic self-protein, mount neutralizing antibodies, and fail therapy unless tolerized — the single most actionable prognostic variable after age-at-treatment.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|------|-------------|---------------|
| [40237692](https://pubmed.ncbi.nlm.nih.gov/40237692/) | Defines GAA-deficiency → lysosomal glycogen chain; avalglucosidase design | Review |
| [39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/) | Untreated natural history; CRIM-negative immunogenicity | Human clinical |
| [41742217](https://pubmed.ncbi.nlm.nih.gov/41742217/) | Compound-het knock-in mouse model | Model organism |
| [26310554](https://pubmed.ncbi.nlm.nih.gov/26310554/) | Cardinal phenotype frequencies (case series) | Human clinical |
| [38958145](https://pubmed.ncbi.nlm.nih.gov/38958145/) / [34020684](https://pubmed.ncbi.nlm.nih.gov/34020684/) | Variant spectrum, ACMG classification, genotype-severity | Human clinical |
| [42538472](https://pubmed.ncbi.nlm.nih.gov/42538472/) | CNS histopathology distribution | Systematic review |
| [32671132](https://pubmed.ncbi.nlm.nih.gov/32671132/) / [37463048](https://pubmed.ncbi.nlm.nih.gov/37463048/) | Extra-lysosomal cascade; AAV reversal | Mechanistic / model |
| [3921759](https://pubmed.ncbi.nlm.nih.gov/3921759/) | Canine model, glycogenosome rupture | Comparative pathology |
| [16860134](https://pubmed.ncbi.nlm.nih.gov/16860134/) / [29565424](https://pubmed.ncbi.nlm.nih.gov/29565424/) | Pivotal ERT survival/ventilator-free data | Human clinical trials |
| [36542086](https://pubmed.ncbi.nlm.nih.gov/36542086/) / [40449831](https://pubmed.ncbi.nlm.nih.gov/40449831/) | Avalglucosidase Mini-COMET efficacy/safety | Clinical trial |
| [41769220](https://pubmed.ncbi.nlm.nih.gov/41769220/) / [41650629](https://pubmed.ncbi.nlm.nih.gov/41650629/) / [40471681](https://pubmed.ncbi.nlm.nih.gov/40471681/) | Next-gen ERT rationale & efficacy | Review / trial |
| [15886040](https://pubmed.ncbi.nlm.nih.gov/15886040/) | Glc4/Hex4 biomarker | Human clinical |
| [40329343](https://pubmed.ncbi.nlm.nih.gov/40329343/) / [33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/) / [42320386](https://pubmed.ncbi.nlm.nih.gov/42320386/) | Epidemiology & pseudodeficiency | NBS / scoping |
| [40952111](https://pubmed.ncbi.nlm.nih.gov/40952111/) | CRIM distribution, genotype-outcome, mortality | Human clinical |
| [18995995](https://pubmed.ncbi.nlm.nih.gov/18995995/) / [18661169](https://pubmed.ncbi.nlm.nih.gov/18661169/) / [41576647](https://pubmed.ncbi.nlm.nih.gov/41576647/) / [12162158](https://pubmed.ncbi.nlm.nih.gov/12162158/) | Cardiac ECG signature & ERT reversal | Human clinical |
| [41536902](https://pubmed.ncbi.nlm.nih.gov/41536902/) / [41453391](https://pubmed.ncbi.nlm.nih.gov/41453391/) / [41014101](https://pubmed.ncbi.nlm.nih.gov/41014101/) | Early ERT, real-life events, 2-decade outcomes | Human clinical |
| [42142433](https://pubmed.ncbi.nlm.nih.gov/42142433/) | AAV gene-therapy DRG toxicity signal | Human clinical |
| [15133760](https://pubmed.ncbi.nlm.nih.gov/15133760/) | Natural LSD animal homologs | Review |

---

## Limitations and Knowledge Gaps

1. **Skeletal muscle remains incompletely treated.** ERT reverses cardiac but not skeletal disease; the mechanistic basis (low CI-MPR, autophagic block) is understood but not therapeutically solved.
2. **CNS involvement is under-characterized in vivo.** Histopathology is documented, but the natural history of neurocognitive/white-matter disease in long-surviving ERT-treated patients is still emerging, and current IV ERT does not reach the CNS.
3. **Small numbers / heterogeneity.** IOPD cohorts are tiny; several key findings rest on case series and single-center studies, and in silico digital-twin modeling has been needed to compensate for underpowered trials.
4. **Long-term next-generation ERT data in IOPD are limited.** Much comparative efficacy data (avalglucosidase, cipaglucosidase+miglustat) come from LOPD; direct head-to-head IOPD evidence is sparse.
5. **Gene-therapy safety.** The AT845 DRG neuronopathy signal underscores that AAV vectors carry real human toxicity risk requiring dose/route optimization.
6. **Ontology precision.** MONDO subtype IDs specific to IOPD (vs. parent GSD II) and complete HPO frequency annotations were assigned from best available mappings and should be curator-verified.

---

## Proposed Follow-up Experiments / Actions

1. **CNS-directed therapy:** develop and test blood–brain-barrier-penetrant delivery (CNS-tropic AAV serotypes, engineered enzyme) in *Gaa*-KO mice with longitudinal MRI/neurobehavioral endpoints, given the documented neuronal/glial storage.
2. **Skeletal-muscle enhancement:** clinically evaluate CI-MPR-upregulating adjuncts (β2-agonists) and autophagy-modulating strategies in combination with next-generation ERT.
3. **Prospective CRIM-stratified natural-history registry** capturing age-at-ERT, ITI regimen, antibody titers, Glc4/Hex4 trajectories, and motor/respiratory/CNS outcomes to define genotype–phenotype–treatment-response rules.
4. **Biomarker qualification:** formally qualify urinary Glc4/plasma Hex4 as a regulatory surrogate endpoint distinguishing cardiac vs. skeletal response.
5. **Universal newborn screening + neonatal treatment protocols** with harmonized second-tier genotyping to manage pseudodeficiency false positives and enable treatment in the critical neonatal window.
6. **Head-to-head IOPD trials** of avalglucosidase alfa vs. cipaglucosidase alfa + miglustat, and prophylactic ITI optimization for CRIM-positive as well as CRIM-negative infants.

---

*Report compiled from 16 evidence-backed findings across 62 reviewed papers. Evidence types span human clinical cohorts and trials, model-organism and comparative-pathology studies, and mechanistic/in-vitro work, as annotated throughout.*


## Artifacts

- [OpenScientist final report](Infantile-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Infantile-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 38 |
| On topic | 36 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 35 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001639` (1 mention) - the report calls it "Neonatal–infantile, rapidly progressive"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0001640` (1 mention) - the report calls it "Infantile, progressive"; HP calls it **Cardiomegaly**
- `HP:0001324` (1 mention) - the report calls it "Infantile, progressive"; HP calls it **Muscle weakness**
- `HP:0001270` (1 mention) - the report calls it "Infantile, progressive"; HP calls it **Motor delay**
- `HP:0002093` (1 mention) - the report calls it "Infantile, progressive"; HP calls it **Respiratory insufficiency**
- `HP:0011968` (1 mention) - the report calls it "Infantile"; HP calls it **Feeding difficulties**
- `HP:0000158` (1 mention) - the report calls it "Infantile"; HP calls it **Macroglossia**
- `HP:0000191` (1 mention) - the report calls it "Infantile"; HP calls it **Accessory oral frenulum**
- `HP:0002240` (1 mention) - the report calls it "Infantile"; HP calls it **Hepatomegaly**
- `HP:0003236` (1 mention) - the report calls it "Infantile"; HP calls it **Elevated circulating creatine kinase activity**
- `HP:0000407` (1 mention) - the report calls it "Emerges with prolonged survival"; HP calls it **Sensorineural hearing impairment**
- `HP:0001260` (1 mention) - the report calls it "Emerges with prolonged survival"; HP calls it **Dysarthria**
- `HP:0000508` (1 mention) - the report calls it "Later"; HP calls it **Ptosis**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001728` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `GO:0005739` (1 mention) - the report calls it "mitochondria"; GO calls it **mitochondrion**, and lists "mitochondria" among its other names
- `UBERON:0001133` (1 mention) - the report calls it "cardiac muscle"; UBERON calls it **cardiac muscle tissue**, and lists "cardiac muscle" among its other names
- `UBERON:0001873` (1 mention) - the report calls it "globus pallidus"; UBERON calls it **caudate nucleus**, and lists "nucleus caudatus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.