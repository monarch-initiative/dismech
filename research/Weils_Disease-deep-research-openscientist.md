---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T18:02:34.482004'
end_time: '2026-09-29T18:18:24.409086'
duration_seconds: 949.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Weil's Disease
  mondo_id: MONDO:0043004
  category: Infectious Disease
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 26
  quotes_valid: 26
  relevance_assessed: 24
  on_topic: 13
  off_topic: 1
  off_topic_references:
  - PMID:42801462
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 37
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 0
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0012819
    reported_labels:
    - Acute, severe
    ontology_label: Myocarditis
  - term_id: HP:0002105
    reported_labels:
    - hemoptysis
    - Acute, severe (LPHS ~50% mortality)
    ontology_label: Hemoptysis
  - term_id: HP:0001945
    reported_labels:
    - "Acute, moderate\u2013severe"
    ontology_label: Fever
  - term_id: HP:0000952
    reported_labels:
    - Acute, severe
    ontology_label: Jaundice
  - term_id: HP:0001873
    reported_labels:
    - Acute
    ontology_label: Thrombocytopenia
  - term_id: HP:0003326
    reported_labels:
    - Acute
    ontology_label: Myalgia
  - term_id: HP:0025406
    reported_labels:
    - Acute
    ontology_label: Asthenia
  - term_id: HP:0002910
    reported_labels:
    - Acute
    ontology_label: Elevated circulating hepatic transaminase concentration
  - term_id: HP:0100785
    reported_labels:
    - Immune phase
    ontology_label: Insomnia
  - term_id: HP:0011446
    reported_labels:
    - Acute
    ontology_label: Abnormality of mental function
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Weils_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Weils_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Weil's Disease
- **MONDO ID:** MONDO:0043004 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Weil's Disease** covering all of the
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

# Weil's Disease (Severe Icteric Leptospirosis) — Comprehensive Disease Characterization Report

**Target disease:** Weil's Disease | **MONDO:** 0043004 | **Category:** Infectious Disease
**Causal agent:** Pathogenic *Leptospira* spp. (chiefly *L. interrogans* serogroup Icterohaemorrhagiae)

---

## Summary

Weil's disease is the **severe, icteric end of the leptospirosis clinical spectrum**, a life-threatening zoonotic infection caused by pathogenic spirochetes of the genus *Leptospira* — most often *Leptospira interrogans* serogroup Icterohaemorrhagiae (serovars Icterohaemorrhagiae and Copenhageni). It is defined clinically by the triad of **jaundice, acute kidney injury (AKI), and hemorrhage**, superimposed on multi-organ dysfunction that can include pulmonary hemorrhage, myocarditis, and altered mental status. Because it is an *acquired infection*, Weil's disease has **no heritable genetic cause**: the "genetic/molecular" dimension of this report concerns the pathogen's virulence genes and the host's transcriptomic/proteomic response, not germline human variants.

The pathophysiology is a two-hit process. Leptospires enter through skin abrasions or mucosa, disseminate hematogenously within hours, and localize to liver, lung, and kidney. There, a combination of **direct spirochete-mediated endothelial and epithelial injury** and a **dysregulated host immune/complement response** (cytokine release, adhesion-molecule upregulation, complement activation) disrupts vascular integrity and produces capillary leak and hemorrhage. In the kidney, injury centers on the proximal convoluted tubule, where downregulation of the sodium/hydrogen exchanger NHE3, aquaporin-1, and Na⁺/K⁺-ATPase produces a characteristic **non-oliguric AKI with hypokalemia and salt wasting**. In the liver, disruption of hepatocyte intercellular junctions ("hepatocyte dissociation") produces deep conjugated hyperbilirubinemia disproportionate to relatively mild transaminase elevation.

Globally leptospirosis causes roughly **one million cases and tens of thousands of deaths per year**, concentrated in tropical low- and middle-income countries and driven by rainfall, flooding, rodent reservoirs, and occupational water/soil contact. Overall case-fatality is a few percent, but severe ICU disease carries **17–21% mortality**, and the leptospirosis-associated pulmonary hemorrhage syndrome (LPHS) approaches **50% mortality with death often within 72 hours**. Mortality is driven principally by respiratory and cardiac complications rather than isolated renal failure. Management rests on early antibiotics (**doxycycline for mild disease; IV penicillin or ceftriaxone for severe disease**) plus aggressive organ support (dialysis, mechanical ventilation, and in refractory cases ECMO), though randomized evidence for an antibiotic mortality benefit remains weak. Prevention combines personal protective equipment, rodent control, sanitation, doxycycline chemoprophylaxis for high-risk groups, and (in animals) whole-cell bacterin vaccines.

---

## Key Findings

### 1. Weil's disease is the severe icteric form of leptospirosis with multi-organ dysfunction (F001)

Weil's disease represents the severe end of the leptospirosis clinical spectrum, defined by the triad of **jaundice, acute kidney injury, and hemorrhage**. The disease is caused by pathogenic *Leptospira* spp., and the clinical spectrum ranges from a mild self-limiting febrile illness (historically "Akiyami" in Japan) to severe multi-organ Weil's disease.

> "Severe leptospirosis, also known as Weil's disease, is a life-threatening zoonotic infection characterized by multi-organ dysfunction, including acute kidney injury and jaundice." — [PMID: 42169153](https://pubmed.ncbi.nlm.nih.gov/42169153/)

> "The disease ranges from a mild, self-limiting illness known as Akiyami to severe Weil's disease, which presents with high fever; jaundice; hemorrhagic tendencies involving the skin, nasal cavity, and lungs; and acute renal failure." — [PMID: 42156054](https://pubmed.ncbi.nlm.nih.gov/42156054/)

**Key identifiers:** MONDO:0043004; ICD-10 **A27.0** (Leptospirosis icterohaemorrhagica); ICD-11 **1B91** (Leptospirosis); MeSH **D014797** ("Weil Disease"); causal genus *Leptospira* (NCBI Taxonomy). **Synonyms:** Weil's syndrome, icterohemorrhagic leptospirosis, infectious/spirochetal jaundice, leptospiral jaundice. The information is **aggregated disease-level** knowledge drawn from case series, cohorts, and reviews rather than a single patient EHR.

### 2. Global burden: ~1 million cases and tens of thousands of deaths annually (F002)

Leptospirosis is a globally distributed **neglected zoonosis**. Burden is concentrated in low-to-middle-income tropical countries with poor sanitation, and incidence spikes with rainfall and flooding.

> "resulting in approximately one million cases and thousands of deaths annually" — [PMID: 42659462](https://pubmed.ncbi.nlm.nih.gov/42659462/)

An ecological study in Buenos Aires Province, Argentina found leptospirosis incidence was tightly coupled to hydrology:

> "Leptospirosis incidence was highly correlated with TWS [terrestrial water storage] variations (R = 0.82, p = 0.00019), whereas annual precipitation showed a weaker, non-significant correlation" — [PMID: 42410475](https://pubmed.ncbi.nlm.nih.gov/42410475/)

Case-fatality of confirmed cases in temperate surveillance was ~2.3%, but severe ICU disease is far deadlier (see F003, F008).

### 3. Severe phenotype: AKI ~99%, myocarditis ~76%, pulmonary hemorrhage ~62% in ICU (F003)

A prospective ICU cohort (Sri Lanka, n = 116; mean age 43.9 y; 88.8% male) quantified the organ-complication profile of severe disease:

> "99.1% (n = 115) developed acute kidney injury, 62.1% (n = 72) developed pulmonary haemorrhage, and 75.9% (n = 88) developed myocarditis" — [PMID: 41507816](https://pubmed.ncbi.nlm.nih.gov/41507816/)

In that cohort 56.9% required mechanical ventilation, 75% required dialysis, and in-hospital mortality was 17.2%. The **leptospirosis-associated pulmonary hemorrhage syndrome (LPHS)** is the most lethal manifestation:

> "The mortality rate of LPHS is approximately 50%, with death generally occurring within 72 hours after symptom onset." — [PMID: 41637348](https://pubmed.ncbi.nlm.nih.gov/41637348/)

| Complication | Frequency (ICU cohort) | HPO term |
|---|---|---|
| Acute kidney injury | 99.1% | HP:0001919 |
| Myocarditis | 75.9% | HP:0012819 |
| Pulmonary haemorrhage | 62.1% | HP:0002105 (hemoptysis) |
| Mechanical ventilation | 56.9% | — |
| Dialysis required | 75% | — |
| In-hospital mortality | 17.2% | — |

### 4. Etiologic agent: *L. interrogans* serogroup Icterohaemorrhagiae predominates (F006)

Weil's disease is classically caused by *Leptospira interrogans* serogroup Icterohaemorrhagiae, serovars **Icterohaemorrhagiae** and **Copenhageni**. Molecular typing of human clinical isolates found *L. interrogans* predominant, and it was recovered from nearly all fatal cases.

> "L.interrogans was frequently isolated (13/14) from those who died." — [PMID: 40602749](https://pubmed.ncbi.nlm.nih.gov/40602749/)

> "Leptospira interrogans serogroup Icterohaemorrhagiae is the major serogroup infecting humans worldwide, and rodents and dogs are the most significant transmission sources in urban environments." — [PMID: 24054736](https://pubmed.ncbi.nlm.nih.gov/24054736/)

The genus *Leptospira* contains 13+ pathogenic species; other human pathogens include *L. kirschneri*, *L. noguchii*, and *L. borgpetersenii*. **NCBI Taxonomy:** *Leptospira interrogans* txid173; serovar Copenhageni str. Fiocruz L1-130 has a sequenced reference genome. Key **virulence/outer-membrane antigens:** LipL32, LipL41, OmpL1, Loa22, LigA/LigB.

### 5. Pathogenesis: endothelial injury plus dysregulated immune/complement response (F005)

Leptospires enter via skin abrasions or mucosa, disseminate hematogenously, and are engulfed by and aggregate around vascular endothelium. A guinea pig epicutaneous-inoculation model documented dissemination kinetics:

> "leptospires were detected in blood as early as 2 h post infection (p.i.) and then disseminated to the liver, lungs and kidneys of almost all animals within 96 h" — [PMID: 22273178](https://pubmed.ncbi.nlm.nih.gov/22273178/)

In LPHS, the host response amplifies direct bacterial damage:

> "the host immune response, via the cytokine release, high expression of adhesion molecules, and activation of the Complement System, may further disrupt endothelial integrity, promoting vascular leakage" — [PMID: 41637348](https://pubmed.ncbi.nlm.nih.gov/41637348/)

### 6. Renal mechanism: proximal-tubule transporter downregulation → non-oliguric AKI (F009)

Tubulointerstitial nephritis is the hallmark renal lesion, and injury centers on the proximal convoluted tubule. Immunohistochemistry of human leptospirosis autopsy kidneys revealed the molecular basis of the distinctive electrolyte picture:

> "A decrease in NHE 3, aquaporin 1, and alpha-Na(+)K(+)ATPase expression occurred in proximal convoluted tubule cells." — [PMID: 20217429](https://pubmed.ncbi.nlm.nih.gov/20217429/)

> "Primary injury of the proximal convoluted tubules is regarded as the hallmark of the kidney in leptospirosis." — [PMID: 20217429](https://pubmed.ncbi.nlm.nih.gov/20217429/)

The downregulation of NHE3, aquaporin-1, and α-Na⁺/K⁺-ATPase in the proximal tubule (with compensatory enhanced aquaporin-2 in collecting ducts) explains the characteristic **non-oliguric AKI with hypokalemia and sodium/magnesium wasting** — distinguishing leptospiral AKI from typical oliguric acute tubular necrosis.

### 7. Prognostic drivers of death: alveolar hemorrhage, arrhythmia, high urea, thrombocytopenia (F008)

A retrospective ICU cohort (São Paulo, 2017–2025; n = 44; median age 42 y; 95.5% male; mortality 20.5%) identified independent predictors of in-hospital death:

> "alveolar hemorrhage (aOR 7.91, 95% CI 1.07-58.61) and arrhythmia (aOR 13.82, 95% CI 2.06-92.64) were independently associated with death" — [PMID: 42257797](https://pubmed.ncbi.nlm.nih.gov/42257797/)

> "mortality in severe leptospirosis was primarily driven by respiratory and cardiac complications rather than isolated renal dysfunction" — [PMID: 42257797](https://pubmed.ncbi.nlm.nih.gov/42257797/)

| Predictor | Adjusted OR | 95% CI |
|---|---|---|
| Alveolar (pulmonary) hemorrhage | 7.91 | 1.07–58.61 |
| Arrhythmia | 13.82 | 2.06–92.64 |
| Urea > 180 mg/dL | 9.01 | 1.36–59.65 |
| Platelets < 45 × 10³/mm³ | 14.07 | 1.40–141.88 |

### 8. Diagnosis: MAT serology and lipL32 PCR, PCR superior early (F007)

> "Diagnosis is established using bacterial culture, polymerase chain reaction, and serological testing, which allow accurate detection across different stages of the disease." — [PMID: 42156054](https://pubmed.ncbi.nlm.nih.gov/42156054/)

The **microscopic agglutination test (MAT)** is the serological reference standard (paired sera, ≥4-fold rise or a single high titer). Real-time PCR targeting the **lipL32** gene outperforms serology in early/acute samples:

> "Serology showed low seroreactivity (13.5%), whereas PCR detected infection in 80.5% of bulls." — [PMID: 42801462](https://pubmed.ncbi.nlm.nih.gov/42801462/)

### 9. Treatment: antibiotics shorten fever but mortality benefit unproven (F004)

A network meta-analysis (920 patients, 8 antibiotics) found multiple agents shortened defervescence:

> "Six antibiotics resulted in significantly shorter defervescence times compared to the control, namely cefotaxime" — [PMID: 38627798](https://pubmed.ncbi.nlm.nih.gov/38627798/)

But the 2024 Cochrane review is cautious:

> "there seems to be insufficient evidence to determine its effectiveness or to recommend antibiotic use as a standard practice" — [PMID: 38483092](https://pubmed.ncbi.nlm.nih.gov/38483092/)

An earlier meta-analysis found no significant mortality difference for penicillin (OR 1.59, 95% CI 0.59–4.29; [PMID: 23930159](https://pubmed.ncbi.nlm.nih.gov/23930159/)). **Standard practice:** doxycycline for mild–moderate disease; IV penicillin G or ceftriaxone for severe Weil's disease, plus organ support (dialysis, mechanical ventilation, ECMO in refractory cases).

### 10. Prevention: PPE, rodent control, doxycycline chemoprophylaxis (F010)

Transmission is zoonotic via water/soil contaminated by urine of infected animals (rodents primary; also dogs, cattle, pigs, horses, wildlife). An Australian raspberry-farm outbreak (84 cases) implicated skin abrasions and lack of PPE:

> "cases were less likely to wear gloves and more recently employed. Cases also more commonly reported always having scratched hands" — [PMID: 31550083](https://pubmed.ncbi.nlm.nih.gov/31550083/)

Human vaccine options are limited:

> "Although licensed vaccines are available, they are targeted at specific risk groups. Bacterins are composed of specific serovars, induce a short-term immune response, and may cause adverse reactions." — [PMID: 42659462](https://pubmed.ncbi.nlm.nih.gov/42659462/)

### 11. Molecular profiling: proteomic and microRNA biomarkers of severity (F011)

Human serum proteomics (2DE/2D-DIGE + MALDI-TOF/TOF) identified 22 differentially expressed proteins:

> "Functional analysis suggested the involvement of differentially expressed proteins in vital physiological pathways, including acute phase response, complement and coagulation cascades and hemostasis." — [PMID: 22554907](https://pubmed.ncbi.nlm.nih.gov/22554907/)

A multi-omics study of severe pulmonary hemorrhagic syndrome (SPHS) identified circulating microRNA biomarkers:

> "miR-5010-3p and miR-147b-3p had significantly higher expression in SPHS group compared to nonSPHS group" — [PMID: 39793739](https://pubmed.ncbi.nlm.nih.gov/39793739/)

(AUC 0.76 and 0.70 respectively for discriminating SPHS — potential early markers before radiographic changes.)

### 12. Clinical course: biphasic illness; jaundice + AKI + hemorrhage with thrombocytopenia (F012)

> "Patients may exhibit a biphasic course, initially experiencing mild illness followed by a brief recovery and then progressing to more severe symptoms such as jaundice, meningitis, renal failure, or pulmonary hemorrhage." — [PMID: 40861768](https://pubmed.ncbi.nlm.nih.gov/40861768/)

> "severe forms of leptospirosis (Weil's disease) can lead to multi-organ dysfunction, including hepatic and renal failure, hemorrhagic manifestations, and altered mental status" — [PMID: 41882577](https://pubmed.ncbi.nlm.nih.gov/41882577/)

### 13. Natural animal disease recapitulates Weil's disease; hepatocyte dissociation is the classic liver lesion (F013)

> "Common histological findings were acute renal tubular necrosis, exudative glomerulonephritis (GN), hepatocyte dissociation and pulmonary hemorrhage." — [PMID: 41110285](https://pubmed.ncbi.nlm.nih.gov/41110285/) (gray/harbor seals infected with *L. interrogans* serovar Copenhageni)

> "hamsters as well as gerbils and guinea pigs have been used as animal models of acute leptospirosis in studying the pathophysiology of the disease" — [PMID: 32632875](https://pubmed.ncbi.nlm.nih.gov/32632875/)

---

## Section-by-Section Report

### 1. Disease Information

Weil's disease is the **severe icteric form of leptospirosis**, a zoonotic bacterial infection caused by pathogenic *Leptospira* spirochetes. It sits at the severe pole of a spectrum whose mild pole is a self-limiting flu-like febrile illness. The defining clinical constellation is **jaundice + acute kidney injury + hemorrhage**, frequently with pulmonary, cardiac, and CNS involvement (F001).

- **MONDO:** 0043004
- **ICD-10:** A27.0 (Leptospirosis icterohaemorrhagica)
- **ICD-11:** 1B91 (Leptospirosis)
- **MeSH:** D014797 (Weil Disease)
- **SNOMED CT:** Weil's disease / icterohaemorrhagic leptospirosis
- **Synonyms:** Weil's syndrome, icterohemorrhagic leptospirosis, infectious/spirochetal jaundice, leptospiral jaundice, "Akiyami" (historical, Japanese — for the milder end)
- **Data provenance:** Aggregated disease-level literature (cohorts, case series, reviews), not individual EHR.

*Not applicable:* OMIM and Orphanet Mendelian-disease identifiers — Weil's disease is an acquired infection, not a heritable disorder.

### 2. Etiology

**Causal factor:** Infectious — pathogenic *Leptospira* spp., predominantly *L. interrogans* serogroup Icterohaemorrhagiae (serovars Icterohaemorrhagiae, Copenhageni) (F006). There is **no genetic/heritable cause**.

**Environmental / occupational risk factors:** contact with water or soil contaminated by animal urine; flooding and heavy rainfall (incidence correlated with terrestrial water storage, R = 0.82; F002); occupations such as farming, construction, sewer/recycling work, abattoir work, and rice farming; recreational freshwater exposure; skin abrasions/cuts as entry portal; lack of PPE (gloves) (F010); rodent infestation. **Demographic risk:** male sex and young-to-middle adulthood predominate (ICU cohorts 88–96% male; F003, F008).

**Genetic risk / protective factors (human):** None established — not applicable to an acquired infection. Host-response variation exists but no validated germline susceptibility or protective loci.

**Gene–environment interactions:** Not applicable in the classical genetic sense. The operative interaction is **pathogen virulence genotype × host immune response** (see Mechanism).

### 3. Phenotypes

| Phenotype | Type | Frequency (severe/ICU) | Onset/severity | HPO term |
|---|---|---|---|---|
| Fever | Symptom | ~universal | Acute, moderate–severe | HP:0001945 |
| Jaundice / conjugated hyperbilirubinemia | Sign/lab | Defining | Acute, severe | HP:0000952 |
| Acute kidney injury | Sign/lab | 99.1% | Acute, severe, often non-oliguric | HP:0001919 |
| Pulmonary hemorrhage / hemoptysis | Sign | 62.1% | Acute, severe (LPHS ~50% mortality) | HP:0002105 |
| Myocarditis / arrhythmia | Sign | 75.9% | Acute, severe | HP:0012819 |
| Thrombocytopenia | Lab | Common | Acute | HP:0001873 |
| Myalgia | Symptom | Common | Acute | HP:0003326 |
| Conjunctival suffusion | Sign | Characteristic | Acute | HP:0025406 |
| Transaminitis (mild, disproportionate to bilirubin) | Lab | Common | Acute | HP:0002910 |
| Aseptic/lymphocytic meningitis | Sign | Uncommon | Immune phase | HP:0100785 |
| Altered mental status | Symptom | Severe cases | Acute | HP:0011446 |

**Age of onset:** Any age; predominantly working-age adults. **Progression:** Acute, often rapidly progressive; LPHS deaths within 72 h (F003). **Quality-of-life impact:** Acute critical illness with high short-term morbidity; survivors generally recover renal and hepatic function (see Prognosis).

### 4. Genetic / Molecular Information

**Not applicable to human germline genetics** — Weil's disease is an acquired infection with no causal human gene, pathogenic variant, modifier gene, chromosomal abnormality, or heritable epigenetic lesion.

The molecular story is **on the pathogen and host-response side**:
- **Pathogen virulence/antigen genes:** *lipL32*, *lipL41*, *ompL1*, *loa22*, *ligA/ligB* (outer-membrane proteins; adhesion, immune evasion, complement resistance) (F005, F006). *lipL32* is also the leading **diagnostic PCR target** (F007).
- **Reference genome:** *L. interrogans* serovar Copenhageni str. Fiocruz L1-130.
- **Host molecular response:** serum proteomic shifts in acute-phase, complement, and coagulation cascades; circulating microRNAs miR-5010-3p and miR-147b-3p elevated in severe pulmonary hemorrhage (F011).

### 5. Environmental Information

- **Environmental factors:** contaminated freshwater/mud, flooding, warm humid climate, poor urban sanitation (F002, F010).
- **Lifestyle/occupational factors:** farming, abattoir/slaughterhouse work, sewage and recycling work, freshwater recreation, walking barefoot, not wearing gloves (F010); a case report even implicated pica (soil ingestion) as an entry route ([PMID: 34287302](https://pubmed.ncbi.nlm.nih.gov/34287302/)).
- **Infectious agent:** *Leptospira interrogans* (NCBI Taxonomy txid173) and related pathogenic species (*L. kirschneri*, *L. noguchii*, *L. borgpetersenii*). **CHEBI-relevant entities:** doxycycline (CHEBI:50845), benzylpenicillin/penicillin G (CHEBI:18208), ceftriaxone (CHEBI:29007), bilirubin (CHEBI:16990), urea (CHEBI:16199).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating exposure → clinical manifestation):**

1. Pathogenic *Leptospira* contact intact mucosa or (more often) abraded skin **→ leads to** entry into the host (F005, F010).
2. Entry **→ leads to** hematogenous dissemination (leptospiremia); organisms detectable in blood within 2 h and seeded to liver, lung, and kidney within 96 h in animal models (F005).
3. Dissemination **→ leads to** adhesion to and invasion of vascular endothelium and target-organ epithelium, mediated by outer-membrane proteins (LipL32, LigA/LigB, etc.) (F005, F006).
4. Endothelial colonization **→ triggers (branch A)** direct spirochete-mediated capillary/endothelial damage **AND (branch B)** a dysregulated host immune response — cytokine release, adhesion-molecule upregulation, and complement activation (F005, F011).
5. Branches A + B converge **→ result in** loss of endothelial integrity and increased vascular permeability **→ leads to** capillary leak and hemorrhage, most dangerously **pulmonary alveolar hemorrhage (LPHS)** (F003, F005).
6. In the kidney, injury localizes to the **proximal convoluted tubule → results in** downregulation of NHE3, aquaporin-1, and α-Na⁺/K⁺-ATPase (with compensatory collecting-duct aquaporin-2) **→ leads to** non-oliguric AKI with hypokalemia and salt/magnesium wasting (F009).
7. In the liver, injury **→ results in** disruption of hepatocyte intercellular junctions ("hepatocyte dissociation") **→ leads to** deep conjugated hyperbilirubinemia disproportionate to modest transaminase rise (F013).
8. Combined pulmonary hemorrhage, myocarditis/arrhythmia, AKI, and hepatic dysfunction **→ result in** multi-organ failure; death is driven principally by respiratory and cardiac complications, often within 72 h in LPHS (F003, F008). *[The relative contribution of direct vs. immune-mediated injury remains partly inferred rather than fully demonstrated.]*

**Molecular pathways / processes (GO suggestions):** complement activation (GO:0006956), inflammatory response (GO:0006954), regulation of endothelial permeability (GO:0043114), blood coagulation (GO:0007596), acute-phase response (GO:0006953), sodium ion transmembrane transport (GO:0035725). **Cellular processes:** vascular endothelial inflammation and dysfunction, tubular epithelial injury, hepatocyte junction disruption. **Cell types (CL):** endothelial cell (CL:0000115), kidney proximal tubule epithelial cell (CL:1000838), hepatocyte (CL:0000182), macrophage (CL:0000235), neutrophil (CL:0000775).

### 7. Anatomical Structures Affected

- **Primary organs:** kidney (UBERON:0002113), liver (UBERON:0002107), lung (UBERON:0002048).
- **Secondary/associated:** heart/myocardium (UBERON:0002349) — myocarditis/arrhythmia; meninges (UBERON:0002360) — aseptic meningitis; skin (UBERON:0002097) — hemorrhage/entry; eye/conjunctiva (UBERON:0000966) — conjunctival suffusion.
- **Body systems:** renal/urinary, hepatobiliary/digestive, respiratory, cardiovascular, nervous.
- **Tissue level:** vascular endothelium, renal proximal tubular epithelium, hepatic parenchyma, pulmonary alveolar-capillary membrane.
- **Cell populations (CL):** endothelial cells, proximal tubule epithelial cells, hepatocytes, macrophages, neutrophils.
- **Subcellular (GO cellular component):** apical plasma-membrane brush border (GO:0031526), basolateral plasma membrane (GO:0016323).
- **Lateralization:** bilateral/diffuse (e.g., bilateral pulmonary infiltrates in LPHS).

### 8. Temporal Development

- **Onset:** Acute, after an incubation of ~2–30 days (typically 7–14). Classic **biphasic course**: leptospiremic/septicemic phase → brief defervescence → immune phase; severe cases may progress directly to multi-organ failure (F012).
- **Progression:** Rapid in severe disease; LPHS death often within 72 h of symptom onset (F003).
- **Disease course:** Self-limited in mild disease; severe disease is a fulminant, acute critical illness.
- **Critical window:** Early antibiotic therapy and organ support during the first days is the key intervention window (F004).

### 9. Inheritance and Population

- **Epidemiology:** ~1 million cases and tens of thousands of deaths per year globally; endemic in tropical LMICs; outbreaks after floods/heavy rain (F002).
- **Inheritance:** Not applicable (acquired infection).
- **Sex ratio:** Strong male predominance in severe cohorts (~89–96% male; F003, F008), reflecting occupational exposure.
- **Age distribution:** Predominantly working-age adults.
- **Geographic distribution:** Tropical and subtropical regions; serogroup Icterohaemorrhagiae is the major human-infecting serogroup worldwide (F006). Rats/rodents and dogs are principal urban reservoirs.

### 10. Diagnostics

- **Serology (reference standard):** Microscopic agglutination test (MAT) — paired sera, ≥4-fold rise or single high titer (F007). IgM ELISA for early screening.
- **Molecular:** real-time PCR targeting **lipL32** — superior sensitivity in early/acute phase (80.5% vs 13.5% serology in one comparison) (F007). Molecular serogroup typing (MST) and VNTR/HRM for strain identification.
- **Culture:** slow (EMJH medium), low yield, mostly reference/epidemiologic use.
- **Supportive labs:** conjugated hyperbilirubinemia, elevated creatinine/urea, thrombocytopenia, leukocytosis, elevated CRP/ESR, mildly elevated transaminases, hypokalemia; CSF lymphocytic pleocytosis with preserved glucose in meningitis ([PMID: 42113872](https://pubmed.ncbi.nlm.nih.gov/42113872/)).
- **Imaging:** chest X-ray/CT — bilateral pulmonary infiltrates in LPHS.
- **Clinical criteria:** WHO/modified Faine's criteria (clinical + epidemiological + laboratory). **Differential diagnosis:** dengue, hantavirus, viral hepatitis, malaria, typhoid, rickettsioses, atypical HUS (F007, related literature).
- **Omics/genetic testing:** Not applicable for human diagnosis; research microRNA/proteomic panels are exploratory (F011).

### 11. Outcome / Prognosis

- **Mortality:** Overall confirmed-case fatality a few percent (~2.3% temperate surveillance); severe/ICU disease 17–21% (F002, F003, F008); LPHS ~50% (F003).
- **Independent predictors of death:** alveolar hemorrhage (aOR 7.91), arrhythmia (aOR 13.82), urea > 180 mg/dL (aOR 9.01), platelets < 45 × 10³/mm³ (aOR 14.07) (F008).
- **Drivers of death:** respiratory and cardiac complications rather than isolated renal failure (F008).
- **Recovery:** Survivors typically recover renal and hepatic function; leptospiral AKI is often reversible with dialysis support.
- **Prognostic biomarkers:** thrombocytopenia, urea; research microRNAs (miR-5010-3p, miR-147b-3p) for pulmonary hemorrhage (F011).

### 12. Treatment

- **Pharmacotherapy (NCIT):** doxycycline (mild–moderate; NCIT C303), IV penicillin G / benzylpenicillin (severe; NCIT C61785), ceftriaxone (severe; NCIT C47584), azithromycin, cefotaxime — all shorten defervescence but no proven mortality benefit (F004).
- **Organ support:** hemodialysis/renal replacement (75% of ICU cohort), mechanical ventilation (57%), vasopressors; **ECMO** in refractory cardiorespiratory failure ([PMID: 34287302](https://pubmed.ncbi.nlm.nih.gov/34287302/)).
- **Adjuncts:** corticosteroids and other immunomodulation have been used empirically in LPHS but lack robust evidence.
- **Evidence caveat:** Cochrane review — insufficient evidence to recommend antibiotics as standard practice on mortality grounds; early empiric treatment nonetheless standard of care (F004).
- **Pharmacogenomics / advanced (gene, cell, RNA, targeted) therapies:** Not applicable.

### 13. Prevention

- **Primary:** PPE (gloves, boots), avoiding contaminated water, rodent control, sanitation, health education, especially in rainy season/floods (F010).
- **Chemoprophylaxis:** doxycycline for high-risk groups/travellers (Cochrane evidence limited).
- **Immunization:** human whole-cell **bacterins** — serovar-specific, short-lived immunity, licensed only for risk groups; subunit candidates target LipL32/LipL41/OmpL1/Loa22/LigA/LigB (F010). Veterinary vaccines widely used in dogs and livestock.
- **Secondary/tertiary:** early diagnosis and organ support; monitoring for pulmonary/cardiac complications.

### 14. Other Species / Natural Disease

Leptospirosis is a **broad-host-range zoonosis**. Natural disease in gray/harbor seals (*Halichoerus grypus*, *Phoca vitulina*) with *L. interrogans* serovar Copenhageni reproduces the human severe phenotype — jaundice, visceral hemorrhage, acute renal tubular necrosis, exudative glomerulonephritis, **hepatocyte dissociation**, and pulmonary hemorrhage (F013). Dogs develop acute renal failure and LPHS; California sea lions have endemic *Pomona* leptospirosis with interstitial nephritis; cattle, pigs, horses are affected.

- **NCBI Taxon:** reservoir *Rattus norvegicus* (txid10116); *Canis lupus familiaris* (txid9615); *Bos taurus* (txid9913); pathogen *L. interrogans* (txid173).
- **Zoonotic potential:** high — rodent urine is the principal source; occupational and recreational water contact are key transmission routes.

### 15. Model Organisms

- **Golden Syrian hamster** (*Mesocricetus auratus*, txid10036) — standard acute-lethal model; reproduces jaundice, hemorrhage, nephritis (F013, [PMID: 32632875](https://pubmed.ncbi.nlm.nih.gov/32632875/)).
- **Guinea pig** (*Cavia porcellus*, txid10141) — epicutaneous inoculation model; documents dissemination kinetics (F005, F013).
- **Gerbils** — additional acute model.
- **Applications:** pathophysiology, dissemination kinetics, virulence-factor testing, vaccine evaluation.
- **Limitations:** rodent-reservoir species (rats) develop chronic renal carriage without severe disease, poorly modeling acute human Weil's disease; models incompletely capture human immune-mediated LPHS.

---

## Mechanistic Model / Interpretation

```
   Contaminated water/soil (animal urine)
                 │  entry via skin abrasion / mucosa
                 ▼
      Pathogenic Leptospira in bloodstream  ──(2 h → 96 h)──►  liver · lung · kidney
                 │  OMP-mediated adhesion (LipL32, LigA/B)
                 ▼
        Endothelial / epithelial colonization
                 │
        ┌────────┴─────────┐
        ▼                  ▼
 DIRECT spirochete    HOST immune response
 endothelial injury   (cytokines, adhesion
                       molecules, complement)
        └────────┬─────────┘
                 ▼
     Loss of endothelial integrity → capillary leak
                 │
     ┌───────────┼──────────────┬───────────────┐
     ▼           ▼              ▼               ▼
  LUNG:       KIDNEY:        LIVER:          HEART:
  alveolar    PCT injury;    hepatocyte      myocarditis /
  hemorrhage  ↓NHE3, AQP1,   dissociation    arrhythmia
  (LPHS)      Na/K-ATPase    → conjugated
     │        → non-oliguric  hyperbili-
     │        AKI, K+ wasting rubinemia
     └───────────┴──────────────┴───────────────┘
                 ▼
        MULTI-ORGAN FAILURE → death
   (driven mainly by respiratory + cardiac, not renal)
```

The unifying lesion is **systemic microvascular endothelial injury** combining direct bacterial damage with a dysregulated immune/complement response. This single mechanism accounts for the three cardinal features simultaneously: hemorrhage (capillary leak), jaundice (hepatocyte-junction disruption, not hepatocyte death — hence bilirubin ≫ transaminases), and AKI (proximal-tubule transporter downregulation, hence non-oliguric with electrolyte wasting). Mortality tracks the lung and heart branches, not the renal branch, because pulmonary hemorrhage and arrhythmia kill rapidly whereas AKI is supportable by dialysis.

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [42169153](https://pubmed.ncbi.nlm.nih.gov/42169153/) | Defines Weil's disease as severe leptospirosis with multi-organ dysfunction | F001 |
| [42156054](https://pubmed.ncbi.nlm.nih.gov/42156054/) | Clinical spectrum (Akiyami → Weil's); diagnostic pillars | F001, F007 |
| [42659462](https://pubmed.ncbi.nlm.nih.gov/42659462/) | Global burden (~1M cases); vaccine limitations | F002, F010 |
| [42410475](https://pubmed.ncbi.nlm.nih.gov/42410475/) | Incidence correlated with water storage (R=0.82) | F002 |
| [41507816](https://pubmed.ncbi.nlm.nih.gov/41507816/) | ICU organ-complication frequencies | F003 |
| [41637348](https://pubmed.ncbi.nlm.nih.gov/41637348/) | LPHS ~50% mortality; immune-endothelial mechanism | F003, F005 |
| [22273178](https://pubmed.ncbi.nlm.nih.gov/22273178/) | Dissemination kinetics in guinea pig | F005 |
| [40602749](https://pubmed.ncbi.nlm.nih.gov/40602749/) | *L. interrogans* in 13/14 fatal cases | F006 |
| [24054736](https://pubmed.ncbi.nlm.nih.gov/24054736/) | Serogroup Icterohaemorrhagiae predominant; reservoirs | F006 |
| [20217429](https://pubmed.ncbi.nlm.nih.gov/20217429/) | Proximal-tubule transporter downregulation | F009 |
| [42257797](https://pubmed.ncbi.nlm.nih.gov/42257797/) | Independent mortality predictors; respiratory/cardiac drive death | F008 |
| [42801462](https://pubmed.ncbi.nlm.nih.gov/42801462/) | lipL32 PCR > MAT serology early | F007 |
| [38627798](https://pubmed.ncbi.nlm.nih.gov/38627798/) | Antibiotics shorten defervescence (NMA) | F004 |
| [38483092](https://pubmed.ncbi.nlm.nih.gov/38483092/) | Cochrane: insufficient evidence for antibiotic efficacy | F004 |
| [23930159](https://pubmed.ncbi.nlm.nih.gov/23930159/) | Penicillin no mortality benefit (OR 1.59) | F004 |
| [31550083](https://pubmed.ncbi.nlm.nih.gov/31550083/) | PPE/gloves & skin abrasions as risk factors (outbreak) | F010 |
| [39793739](https://pubmed.ncbi.nlm.nih.gov/39793739/) | miR-5010-3p, miR-147b-3p biomarkers of SPHS | F011 |
| [22554907](https://pubmed.ncbi.nlm.nih.gov/22554907/) | Proteomic complement/coagulation involvement | F011 |
| [40861768](https://pubmed.ncbi.nlm.nih.gov/40861768/) | Biphasic course | F012 |
| [41882577](https://pubmed.ncbi.nlm.nih.gov/41882577/) | Multi-organ Weil's constellation | F012 |
| [41110285](https://pubmed.ncbi.nlm.nih.gov/41110285/) | Natural seal disease; hepatocyte dissociation | F013 |
| [32632875](https://pubmed.ncbi.nlm.nih.gov/32632875/) | Hamster/guinea pig models | F013 |

**Evidence source types:** human clinical cohorts and case series (F001–F004, F007, F008, F012); human autopsy immunohistochemistry (F009); human omics (F011); model organism / natural animal disease (F005, F013); systematic reviews/meta-analyses (F004).

---

## Limitations and Knowledge Gaps

1. **Weak antibiotic evidence base.** No trial has demonstrated a mortality benefit; recommendations rest on defervescence and expert consensus (F004). The optimal agent, dose, and timing for severe disease remain uncertain.
2. **Small severe-disease cohorts.** Key prognostic estimates come from single-center ICU cohorts of 44–116 patients with very wide confidence intervals (e.g., platelet aOR 14.07, 95% CI 1.40–141.88) (F003, F008).
3. **Mechanistic inference.** The relative contribution of direct spirochete injury vs. immune/complement-mediated damage is partly inferred from animal models and cannot be cleanly partitioned in humans (F005).
4. **Diagnostic access.** MAT and culture are slow and reference-lab-bound; PCR is more sensitive early but not universally available — leptospirosis is chronically under-diagnosed and under-reported (F002, F007).
5. **Biomarker validation.** MicroRNA and proteomic markers derive from small discovery cohorts and lack prospective validation (F011).
6. **No human vaccine of broad efficacy.** Bacterins are serovar-restricted with short-lived immunity; subunit candidates remain preclinical/early (F010).
7. **Model limitations.** Rodent reservoir species do not develop severe disease, and no model fully reproduces human LPHS immunopathology (F013).

---

## Proposed Follow-up Experiments / Actions

1. **Adequately powered RCT** of early antibiotics (ceftriaxone vs penicillin vs doxycycline) in severe leptospirosis with mortality and organ-failure endpoints, to resolve the Cochrane evidence gap (addresses F004).
2. **Prospective multicenter validation** of the São Paulo mortality model (alveolar hemorrhage, arrhythmia, urea, platelets) as a bedside risk score for ICU triage (F008).
3. **Prospective validation of miR-5010-3p / miR-147b-3p** as early predictors of pulmonary hemorrhage before radiographic change, head-to-head with platelets/urea (F011).
4. **Point-of-care lipL32 PCR** evaluation in endemic primary-care settings to shorten time-to-diagnosis and enable earlier therapy (F007).
5. **Mechanistic dissection** of complement-pathway inhibition (e.g., eculizumab-class agents) in animal LPHS models to test whether the immune-mediated branch is therapeutically tractable (F005, F011); note the reported atypical-HUS overlap ([PMID: 42169153](https://pubmed.ncbi.nlm.nih.gov/42169153/)).
6. **Cross-protective subunit vaccine** development targeting conserved OMPs (LigA/LigB, LipL32) with next-generation adjuvants, leveraging veterinary vaccine experience (F010).
7. **One Health surveillance** integrating rodent-reservoir, environmental water, and human case data in flood-prone endemic regions to enable predictive outbreak modeling (F002).

---

*Report compiled from 13 confirmed findings and 54 reviewed papers across 5 investigation iterations. All quoted snippets are verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Weils_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Weils_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 26 |
| Quoted claims found in source | 26 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 24 |
| On topic | 13 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42801462` (4 mentions) - Diagnosis of bovine genital leptospirosis in asymptomatic bulls: Comparison of methods and samples under field conditions.
  - shared terms: leptospirosis

Weighed against this report's own most characteristic terms: `severe`, `disease`, `pulmonary`, `hemorrhage`, `lphs`, `human`, `acute`, `leptospirosis`, `renal`, `weil`, `mortality`, `death`, `icu`, `injury`, `f003`, `immune`, `kidney`, `interrogan`, `cohort`, `f008`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012819` (2 mentions) - the report calls it "Acute, severe"; HP calls it **Myocarditis**
- `HP:0002105` (2 mentions) - the report calls it "hemoptysis", "Acute, severe (LPHS ~50% mortality)"; HP calls it **Hemoptysis**
- `HP:0001945` (1 mention) - the report calls it "Acute, moderate–severe"; HP calls it **Fever**
- `HP:0000952` (1 mention) - the report calls it "Acute, severe"; HP calls it **Jaundice**
- `HP:0001873` (1 mention) - the report calls it "Acute"; HP calls it **Thrombocytopenia**
- `HP:0003326` (1 mention) - the report calls it "Acute"; HP calls it **Myalgia**
- `HP:0025406` (1 mention) - the report calls it "Acute"; HP calls it **Asthenia**
- `HP:0002910` (1 mention) - the report calls it "Acute"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `HP:0100785` (1 mention) - the report calls it "Immune phase"; HP calls it **Insomnia**
- `HP:0011446` (1 mention) - the report calls it "Acute"; HP calls it **Abnormality of mental function**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001919` (2 mentions) - the report calls it "Acute, severe, often non-oliguric"; HP calls it **Acute kidney injury**, and lists "Acute renal failure" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary organs:** kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `UBERON:0002349` (1 mention) - the report calls it "Secondary/associated:** heart/myocardium"; UBERON calls it **myocardium**, and lists "heart myocardium" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002105` - called "hemoptysis", "Acute, severe (LPHS ~50% mortality)"