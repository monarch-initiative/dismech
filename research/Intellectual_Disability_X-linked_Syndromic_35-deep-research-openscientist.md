---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T02:51:10.540251'
end_time: '2026-09-07T03:07:31.470112'
duration_seconds: 980.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability X-linked Syndromic 35
  mondo_id: MONDO:0030908
  category: Genetic
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:30482776
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 5
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001999
    reported_labels:
    - Very frequent
    ontology_label: Abnormal facial shape
  - term_id: HP:0001250
    reported_labels:
    - Frequent
    ontology_label: Seizure
  - term_id: HP:0000717
    reported_labels:
    - Frequent
    ontology_label: Autism
  - term_id: HP:0001561
    reported_labels:
    - Frequent (3/4)
    ontology_label: Polyhydramnios
  - term_id: HP:0004322
    reported_labels:
    - Frequent
    ontology_label: Short stature
  - term_id: HP:0000546
    reported_labels:
    - Subset
    ontology_label: Retinal degeneration
  - term_id: HP:0000365
    reported_labels:
    - Subset
    ontology_label: Hearing impairment
  - term_id: HP:0001627
    reported_labels:
    - Subset
    ontology_label: Abnormal heart morphology
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Disability_X-linked_Syndromic_35-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Disability_X-linked_Syndromic_35-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability X-linked Syndromic 35
- **MONDO ID:** MONDO:0030908 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability X-linked Syndromic 35** covering all of the
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

# Intellectual Disability, X-linked Syndromic 35 (MRXS35): A Comprehensive Disease Characterization

**Disease:** Intellectual Disability, X-linked Syndromic 35 (MRXS35)
**MONDO ID:** MONDO:0030908 · **OMIM:** #300998 · **Gene:** *RPL10* (uL16/QM), Xq28
**Category:** Genetic (X-linked recessive ribosomopathy)
**Report type:** Aggregated disease-level synthesis from primary literature and reference databases

---

## Summary

**Intellectual Disability, X-linked Syndromic 35 (MRXS35; OMIM #300998, MONDO:0030908) is an ultra-rare X-linked recessive ribosomopathy caused by hemizygous hypomorphic missense variants in *RPL10*, the gene encoding the 60S large-subunit ribosomal protein uL16 (also known as QM) at Xq28.** The protein is essential for joining of the 40S and 60S ribosomal subunits during translation initiation, and it sits in close proximity to the peptidyl transferase center of the ribosome. Pathogenic variants reduce functional RPL10, lowering bulk protein synthesis and increasing neuronal apoptosis during brain development — the mechanistic basis for microcephaly and intellectual disability.

Affected males present with a syndromic constellation dominated by intellectual disability/developmental delay (near-universal), and a variable, partly genotype-dependent combination of autism spectrum disorder, epilepsy, microcephaly (~50% of cases, frequently progressive/postnatal), cerebellar signs, facial dysmorphism, short stature, hypotonia, and congenital anomalies affecting the eyes (retinal degeneration), ears (hearing loss), heart, and genitourinary and gastrointestinal systems. Reported pathogenic alleles include p.K78E (c.232A>G), p.R32L (c.95G>T), p.R116Q (c.347G>A), and the original autism-associated C-terminal substitutions p.L206M and p.H213Q. Inheritance is typically from unaffected carrier mothers who exhibit skewed (nonrandom) X-inactivation, consistent with X-linked recessive transmission; de novo occurrence is also documented.

There is no gene-specific or disease-modifying therapy. Management is supportive and multidisciplinary — antiepileptic drugs for seizures, developmental/rehabilitative therapies, and surveillance for ophthalmologic, audiologic, cardiac, and genitourinary complications — coupled with molecular diagnosis by exome/genome or gene-panel sequencing and genetic counseling for at-risk families. Notably, the *same* gene harbors a mechanistically distinct recurrent **somatic** mutation, p.R98S, in ~8% of pediatric T-cell acute lymphoblastic leukemia, which activates JAK-STAT signaling — a clean illustration that germline hypomorphic and somatic oncogenic *RPL10* lesions produce entirely different diseases.

---

## Key Findings

### Finding 1 — MRXS35 is caused by hemizygous missense variants in *RPL10* (uL16), an X-linked ribosomopathy

MRXS35 (OMIM #300998) is caused by hemizygous missense variants in **RPL10** (HGNC:10298; Entrez Gene 6134; Ensembl ENSG00000147403; gene-MIM 312173; cytoband Xq28; aliases QM, uL16, AUTSX5, L10, DXS648, NOV). The gene was first implicated in neurodevelopmental disease through autism families, where two C-terminal missense substitutions (p.L206M and p.H213Q) were identified: *"We have identified two missense mutations in the ribosomal protein gene RPL10 located in Xq28 in two independent families with autism"* ([PMID: 16940977](https://pubmed.ncbi.nlm.nih.gov/16940977/)). The syndromic microcephaly/ID phenotype was subsequently defined by the identification of *"a novel missense mutation in the gene encoding 60S ribosomal protein L10 (RPL10)"* — the p.K78E allele ([PMID: 25316788](https://pubmed.ncbi.nlm.nih.gov/25316788/)).

The recurrent pathogenic missense alleles map to functionally critical regions of the protein. The N-terminal variants (p.R32L, p.K78E) fall within the 28S/25S rRNA-binding region near the peptidyl transferase center, while p.L206M and p.H213Q lie in the C-terminal region. Inheritance follows an X-linked recessive paradigm: *"the p.K78E change segregated with disease under an X-linked recessive paradigm while, consistent with causality, carrier females exhibited skewed X inactivation"* ([PMID: 25316788](https://pubmed.ncbi.nlm.nih.gov/25316788/)). The normal molecular role of the protein — it is *"required for the joining of the 40S and 60S subunits"* ([PMID: 9443083](https://pubmed.ncbi.nlm.nih.gov/9443083/)) — anchors the ribosomopathy mechanism. Zebrafish complementation established that p.K78E is a loss-of-function allele.

**Ontology anchors:** Gene HGNC:10298 (*RPL10*); disease MONDO:0030908; GO:0022618 (ribonucleoprotein complex assembly), GO:0042254 (ribosome biogenesis), GO:0006412 (translation).

### Finding 2 — *RPL10* is highly intolerant to loss-of-function and missense variation

Population constraint metrics from gnomAD confirm that *RPL10* is under strong purifying selection, consistent with an essential housekeeping gene. gnomAD v2 constraint values for ENSG00000147403 are: **pLI = 0.997** (loss-of-function intolerant), **observed/expected LoF = 0.064** (1 observed vs. 15.7 expected; LOEUF/oe_lof_upper = 0.30), **LoF-Z = 3.15**, and **missense-Z = 4.08** (oe_mis = 0.29), while the synonymous-Z of 0.37 confirms the model is well-calibrated (neutral for silent variation). The gene spans chrX:154,389,955–154,409,168 (GRCh38), Xq28.

The practical consequence is that pathogenic *RPL10* missense variants are essentially absent from population reference databases: for one reported pathogenic allele, the *"variant, not reported in gnomAD"* ([PMID: 35876338](https://pubmed.ncbi.nlm.nih.gov/35876338/)). This strong constraint supports ACMG criterion PM2 (absent/rare in population databases) for candidate variants and explains why only hypomorphic (partial loss-of-function) missense alleles — rather than complete null alleles — are compatible with viability and thus observed in patients.

| Constraint metric (gnomAD v2) | Value | Interpretation |
|---|---|---|
| pLI | 0.997 | LoF-intolerant |
| oe LoF (LOEUF) | 0.064 (0.30) | Strong LoF depletion |
| LoF-Z | 3.15 | Significant constraint |
| Missense-Z | 4.08 | Strong missense constraint |
| Synonymous-Z | 0.37 | Neutral (calibrated) |

### Finding 3 — Clinical spectrum: syndromic ID with epilepsy, ASD, microcephaly, dysmorphism, and congenital anomalies

Across ~15–19 reported affected males, the core phenotype comprises **intellectual disability/developmental delay** (near-universal; 4/4 in the Thevenon 2015 family), **autism spectrum disorder**, **epilepsy** (often early-onset, refractory seizures), and **facial dysmorphism**. MRXS35 is defined as *"an X-linked syndrome presenting with intellectual disability (ID), autism spectrum disorder, epilepsy, dysmorphic features, and multiple congenital anomalies"* ([PMID: 35876338](https://pubmed.ncbi.nlm.nih.gov/35876338/)).

**Microcephaly** occurs in approximately half of cases and is often progressive/postnatal: *"microcephaly was observed in approximately half of the cases"* ([PMID: 35876338](https://pubmed.ncbi.nlm.nih.gov/35876338/)). A family segregating an *RPL10* variant showed a characteristic combination of *"syndromic features including amniotic fluid excess (3/4), microcephaly (2/4), urogenital anomalies (3/4), cerebellar syndrome (2/4), and facial dysmorphism"* ([PMID: 25846674](https://pubmed.ncbi.nlm.nih.gov/25846674/)), documenting per-feature frequencies. The severe end of the spectrum, associated with p.K78E, includes *"severe microcephaly, seizures, hearing loss, growth retardation, cardiac defects, and dysmorphic facial features"* ([PMID: 29066376](https://pubmed.ncbi.nlm.nih.gov/29066376/)).

Certain features are variant-associated: retinal degeneration/retinitis pigmentosa is notable with p.R32L, while severe multisystem involvement (hearing loss, cardiac defects) clusters with p.K78E. Onset spans the prenatal/neonatal period (polyhydramnios) to early childhood, and both microcephaly and retinopathy can be **progressive**.

| Phenotype | Approx. frequency | Suggested HPO term |
|---|---|---|
| Intellectual disability / developmental delay | Near-universal | HP:0001249 / HP:0001263 |
| Facial dysmorphism | Very frequent | HP:0001999 |
| Microcephaly (often progressive/postnatal) | ~50% | HP:0000252 / HP:0005484 |
| Epilepsy / seizures | Frequent | HP:0001250 |
| Autism spectrum disorder | Frequent | HP:0000717 |
| Cerebellar signs / ataxia | ~50% (2/4) | HP:0001251 |
| Urogenital/genital anomalies (incl. cryptorchidism) | Frequent (3/4) | HP:0000078 / HP:0000028 |
| Polyhydramnios (antenatal) | Frequent (3/4) | HP:0001561 |
| Short stature / growth retardation | Frequent | HP:0004322 |
| Hypotonia | Reported | HP:0001252 |
| Retinal degeneration (variant-associated, p.R32L) | Subset | HP:0000546 |
| Hearing loss (variant-associated, p.K78E) | Subset | HP:0000365 |
| Cardiac defects (variant-associated, p.K78E) | Subset | HP:0001627 |

### Finding 4 — Mechanism: germline hypomorphic variants impair translation and increase apoptosis; distinct somatic R98S drives leukemia

The germline (MRXS35) mechanism is a partial loss of ribosomal function. In a zebrafish model, *rpl10* suppression *"decreases head size in developing morphant embryos, concomitant with reduced bulk translation and increased apoptosis in the brain"* ([PMID: 25316788](https://pubmed.ncbi.nlm.nih.gov/25316788/)); this phenotype is rescued by wild-type but not mutant human RPL10, establishing p.K78E as loss-of-function. Because uL16 *"is required for the joining of the 40S and 60S subunits"* ([PMID: 9443083](https://pubmed.ncbi.nlm.nih.gov/9443083/)) and is added late during cytoplasmic 60S maturation, reduced functional protein throttles the supply of translation-competent ribosomes precisely when developing neurons demand high protein synthesis — leading to reduced neuronal output, apoptosis, and microcephaly.

Critically, the same gene harbors a **mechanistically distinct somatic** lesion in cancer. The recurrent p.R98S mutation occurs in ~8% of pediatric T-cell acute lymphoblastic leukemia (T-ALL): *"the recurrent RPL10-R98S mutation in T-cell acute lymphoblastic leukemia (T-ALL)"* ([PMID: 30482776](https://pubmed.ncbi.nlm.nih.gov/30482776/)). Rather than simple loss of function, R98S produces a gain of oncogenic activity — *"we describe modulation of the JAK-STAT cascade as a novel cancer-promoting activity of a ribosomal mutation"* ([PMID: 28744013](https://pubmed.ncbi.nlm.nih.gov/28744013/)) — via reduced JAK1 degradation and altered programmed ribosomal frameshifting. R98S also induces oxidative stress (an early proliferation defect), upregulates serine biosynthesis (PSPH) and glycine ([PMID: 31186416](https://pubmed.ncbi.nlm.nih.gov/31186416/)), and promotes secondary oncogenic mutagenesis including NOTCH1-activating lesions ([PMID: 30482776](https://pubmed.ncbi.nlm.nih.gov/30482776/)). This germline-vs-somatic contrast underscores that *RPL10* genotype–phenotype relationships are allele-specific and mechanism-specific.

### Finding 5 — RPL10/uL16 protein: 214-aa cytoplasmic large-subunit ribosomal protein with resolved structures

The protein product is UniProt **P27635** (human RPL10/uL16): 214 amino acids, cytoplasmic. UniProt annotation states it is a *"Component of the large ribosomal subunit… Plays a role in the formation of actively translating ribosomes… May play a role in the embryonic brain development."* At least 37 experimental PDB entries resolve uL16 within the human 80S ribosome (e.g., 5AJ0, 6OLE, 6OLF, 6OLG, 6OLI, 6OLZ), providing structural context for pathogenic residues. The MRXS35 residues Arg32, Lys78, Leu206, and His213 localize to rRNA-binding/N-terminal and C-terminal regions of the protein, and the protein sits in *"close proximity to the peptidyl transferase active site of the 60S ribosomal subunit"* ([PMID: 25316788](https://pubmed.ncbi.nlm.nih.gov/25316788/)). This structural proximity to the catalytic center provides a plausible structural rationale for how single missense substitutions perturb translation.

**Subcellular localization (GO Cellular Component):** GO:0022625 (cytosolic large ribosomal subunit), GO:0005737 (cytoplasm), GO:0005840 (ribosome).

### Finding 6 — ClinVar landscape and cross-species orthologs

ClinVar (RefSeq NM_006013.5) holds ~404 *RPL10* records. At the single-nucleotide level, most missense variants are classified as **variants of uncertain significance (VUS)** (e.g., p.Leu36Gln, p.Asp44Tyr, p.Arg32Cys, p.Ile167Val), with a smaller set of Pathogenic/Likely-pathogenic SNVs corresponding to the known MRXS35 alleles. Importantly, many ClinVar entries labeled "Pathogenic" as copy-number gains/losses are large **multigenic Xq deletions/duplications** that span *RPL10* rather than *RPL10*-specific point mutations — a distinction that matters for interpretation. The disease-relevant residues are *"affecting an evolutionary conserved residue"* ([PMID: 35876338](https://pubmed.ncbi.nlm.nih.gov/35876338/)), consistent with strong cross-species conservation.

Validated orthologs supporting model-organism work: mouse *Rpl10* (NCBI Gene 110954; MGI:105943; ENSMUSG00000008682); zebrafish *rpl10* (NCBI Gene 336712); *S. cerevisiae* RPL10. Human *RPL10* = NCBI Gene 6134, UniProt P27635 (214 aa).

### Finding 7 — Novel p.Arg116Gln allele expands genotype, phenotype, and functional evidence

A 2025 report identified a novel recurrent hemizygous missense variant, **NM_006013.5:c.347G>A, p.Arg116Gln**, in two unrelated Chinese male patients, each maternally inherited: *"the same hemizygous missense RPL10 gene variant (NM_006013.5:c.347G>A, p.Arg116Gln) in each patient, inherited from their respective mothers"* ([PMID: 40861044](https://pubmed.ncbi.nlm.nih.gov/40861044/)). In vitro functional analysis provided independent loss-of-function evidence: the variant *"reduced the mRNA expression of the RPL10 gene, thereby decreasing synthesis of the RPL10 protein"* ([PMID: 40861044](https://pubmed.ncbi.nlm.nih.gov/40861044/)).

This report also expanded the neonatal/early phenotype to include *"congenital laryngeal stridor, feeding difficulties, neonatal pneumonia, neonatal hypoglycemia, dysmorphic features, and bilateral cryptorchidism"* ([PMID: 40861044](https://pubmed.ncbi.nlm.nih.gov/40861044/)), along with short stature, hypotonia, gastrointestinal problems, and craniofacial anomalies. The summarized full MRXS35 spectrum from this paper — ID, psychomotor/speech delay, short stature, craniofacial anomalies, hypotonia, seizures, GI problems, genitourinary anomalies, cardiac anomalies, eye defects, and hearing loss — reinforces the multisystem, prenatal-to-childhood nature of the disorder.

---

## Section-by-Section Report

### 1. Disease Information

MRXS35 is an ultra-rare, X-linked recessive syndromic intellectual disability disorder — a **ribosomopathy** — caused by variants in *RPL10*. Key identifiers: **OMIM #300998**; **MONDO:0030908**; gene-MIM **312173** (*RPL10*). ICD-11 would fall under 6A00 (Disorders of intellectual development) with a genetic modifier; a specific Orphanet number is not firmly assigned in the retrieved data (the disorder overlaps the "RPL10-related disorder" concept). Common synonyms/alternative names: **MRXS35**; **RPL10-related disorder**; **X-linked intellectual disability, syndromic, 35**; historically linked to **AUTSX5** (autism, X-linked 5) via the same gene. The information in this report is derived from **aggregated disease-level resources** (OMIM, ClinVar, gnomAD, UniProt, PDB) and **individual patient case reports/series** in primary literature, not from EHR-scale patient data.

### 2. Etiology

**Causal factor:** monogenic — hemizygous hypomorphic missense variants in *RPL10* (Xq28). **Genetic risk factors:** the causal variants themselves (p.K78E, p.R32L, p.R116Q, p.L206M, p.H213Q); being male (hemizygous) is the principal determinant of clinical expression. **Environmental risk factors:** none established — this is a Mendelian disorder without a recognized environmental contribution. **Protective factors:** in carrier females, skewed X-inactivation favoring the wild-type allele is effectively protective, explaining why carrier mothers are typically unaffected. No dietary/lifestyle protective factors are known. **Gene–environment interactions:** none documented; disease liability is essentially determined by genotype and X-inactivation status.

### 3. Phenotypes

See Finding 3 table for phenotype types, frequencies, and HPO terms. Phenotype **characteristics**: onset is prenatal/neonatal (polyhydramnios, feeding difficulties, laryngeal stridor, neonatal hypoglycemia) to early childhood (developmental delay, seizures); severity is **variable** and partly genotype-dependent (p.K78E severe; C-terminal autism alleles milder/behavioral); progression is largely **stable** for ID but **progressive** for postnatal microcephaly and retinopathy. **Quality-of-life impact** is substantial where ID is moderate-to-severe, with lifelong dependency, communication impairment, and comorbid epilepsy and behavioral (ASD) burden; formal EQ-5D/SF-36 data are not available for this ultra-rare disorder.

### 4. Genetic/Molecular Information

**Causal gene:** *RPL10* (HGNC:10298; NCBI 6134; gene-MIM 312173; Xq28). **Pathogenic variants (germline):** p.K78E (c.232A>G), p.R32L (c.95G>T), p.R116Q (c.347G>A), p.L206M, p.H213Q — all **missense**, all in the RefSeq NM_006013.5 transcript. **Classification:** the recurrent disease alleles are Pathogenic/Likely-pathogenic; the broader ClinVar landscape is VUS-dominant (Finding 6). **Allele frequency:** absent/ultra-rare in gnomAD (Finding 2). **Origin:** germline; typically maternally inherited from carriers with skewed X-inactivation, with de novo cases reported. **Functional consequence:** loss/reduction of function (hypomorphic), demonstrated in zebrafish (p.K78E) and by reduced mRNA/protein for p.R116Q. **Modifier factors:** X-inactivation pattern is the principal modifier in carrier females. **Chromosomal abnormalities:** large Xq28 copy-number gains/losses spanning *RPL10* exist (e.g., MidXq28-duplication syndrome involving FLNA, RPL10, GDI1; and dosage-dependent Xq28 gains where *GDI1* is the likelier driver — [PMID: 31090057](https://pubmed.ncbi.nlm.nih.gov/31090057/), [PMID: 20004760](https://pubmed.ncbi.nlm.nih.gov/20004760/)), but these multigenic CNVs are distinct from *RPL10* point-mutation MRXS35. **Epigenetics:** no disease-specific methylation signature established.

### 5. Environmental Information

Not applicable. MRXS35 is a monogenic disorder; no environmental toxins, lifestyle factors, or infectious agents are implicated in causation or triggering.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (germline MRXS35):**

1. A hemizygous hypomorphic missense variant in *RPL10* (e.g., p.K78E, p.R116Q) **results in** a structurally/functionally impaired uL16 protein (or reduced protein level, as shown for p.R116Q).
2. Reduced functional uL16 **leads to** impaired late cytoplasmic 60S maturation and defective 40S–60S subunit joining (uL16 is *"required for the joining of the 40S and 60S subunits"*).
3. Defective subunit joining **results in** a reduced pool of actively translating 80S ribosomes and **decreased bulk protein synthesis** (demonstrated in zebrafish morphants).
4. Reduced translation in the developing brain **leads to** increased neuronal **apoptosis** and reduced neuronal output (demonstrated).
5. Neuronal loss/reduced proliferation **results in** reduced brain growth → **microcephaly** (often postnatal/progressive) and disrupted neurodevelopment → **intellectual disability, autism, epilepsy** (mechanism inferred from the translation-apoptosis link; clinical correlation strong).
6. **Branch:** tissue-specific translational vulnerability **leads to** variant-associated congenital anomalies — retinal degeneration (p.R32L), hearing loss/cardiac defects (p.K78E), and genitourinary/GI anomalies (inferred).

**Pathways/processes:** cytoplasmic translation (GO:0006412), ribosomal large subunit assembly/biogenesis (GO:0000027, GO:0042273), apoptotic process (GO:0006915), embryonic brain development. **Protein dysfunction:** partial loss of function of a ribosomal structural protein near the peptidyl transferase center. **Cell types (CL):** neurons (CL:0000540), neural progenitor/neuroblast (CL:0000031), and photoreceptor/cochlear/cardiac cells in variant-specific branches. This contrasts with the **somatic** T-ALL mechanism (p.R98S → JAK-STAT gain-of-function, serine/glycine metabolic rewiring, oncogenic mutagenesis; Finding 4).

### 7. Anatomical Structures Affected

**Primary organ:** brain (UBERON:0000955), especially cerebrum and cerebellum (UBERON:0002037; cerebellar signs). **Body system:** central nervous system (UBERON:0001017). **Secondary/variant-associated:** eye/retina (UBERON:0000970 / UBERON:0000966; retinal degeneration), ear/cochlea (hearing loss), heart (UBERON:0000948; cardiac defects), genitourinary tract (cryptorchidism), gastrointestinal tract, and larynx (congenital stridor). **Tissue/cell level:** nervous tissue; neurons and neural progenitors. **Subcellular:** cytoplasm/cytosolic ribosome (GO:0022625). **Lateralization:** bilateral/symmetric involvement (microcephaly, retinopathy, cryptorchidism when bilateral).

### 8. Temporal Development

**Onset:** congenital to early childhood; antenatal signs (polyhydramnios) and neonatal features (feeding difficulty, stridor, hypoglycemia) can precede developmental delay. **Onset pattern:** chronic/insidious for neurodevelopment; microcephaly frequently **postnatal and progressive**. **Progression:** intellectual disability is generally stable (non-degenerative), but head circumference and retinal findings can worsen over time. **Course:** chronic, lifelong. **Critical period:** the fetal/early-postnatal window of maximal neurogenesis and neuronal protein-synthesis demand is the period of greatest vulnerability and the theoretical window for intervention.

### 9. Inheritance and Population

**Inheritance:** X-linked recessive; affected males, unaffected carrier mothers with skewed X-inactivation; de novo cases reported. **Penetrance:** high/complete in hemizygous males; carrier females usually unaffected due to favorable X-inactivation (rare manifesting carriers possible). **Expressivity:** variable, partly genotype-dependent. **Epidemiology:** ultra-rare; fewer than ~20 well-characterized males reported worldwide; precise prevalence/incidence are not established. **Sex ratio:** strongly male-predominant. **Founder effects/consanguinity:** none established; the p.R116Q allele recurred in two unrelated Chinese families (recurrent mutation, not proven founder). **Carrier frequency:** not defined (variants absent from gnomAD).

### 10. Diagnostics

Diagnosis is **molecular**. Recommended approach: **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**, or a targeted **intellectual disability/XLID gene panel** including *RPL10*; single-gene testing is appropriate when a familial variant is known. **Chromosomal microarray (CMA)** is indicated to detect Xq28 CNVs in the differential (MidXq28-duplication syndrome). Variant interpretation follows **ACMG/AMP** guidelines: absence from gnomAD (PM2), evolutionary conservation, and functional/segregation evidence support pathogenicity; many *RPL10* missense variants remain **VUS**. Supportive workup: brain MRI (microcephaly, cerebellar/structural findings), EEG (epilepsy), ophthalmologic exam (retinopathy), audiology, echocardiography, and growth/endocrine and metabolic evaluation (neonatal hypoglycemia). No specific biochemical biomarker exists. **Differential diagnosis:** other X-linked syndromic IDs (e.g., MECP2-related, KDM5C/Claes-Jensen, USP9X-related, MSL3/Basilicata-Akhtar) and other ribosomopathies. **Screening:** cascade carrier testing in families once the variant is identified; prenatal/preimplantation testing possible for known familial variants. No newborn-screening program exists.

### 11. Outcome/Prognosis

**Survival:** the disorder is chronic and non-malignant; life expectancy depends on severity of epilepsy and congenital anomalies (severe p.K78E cases with cardiac defects carry higher risk). No formal survival statistics are available. **Morbidity:** dominated by lifelong intellectual disability, communication impairment, epilepsy, and behavioral (ASD) burden, with additional disability from sensory (visual, auditory) and motor (hypotonia, cerebellar) involvement. **Complications:** refractory seizures, feeding difficulties/aspiration, growth failure, and organ-specific issues. **Recovery:** no reversal; management is supportive. **Prognostic factors:** specific genotype (p.K78E severe end), presence of epilepsy, degree of microcephaly, and multi-organ involvement.

### 12. Treatment

There is **no disease-modifying or gene-specific therapy**. Management is **supportive and multidisciplinary** (suggested NCIT: Supportive Care Intervention):
- **Antiepileptic pharmacotherapy** for seizures (agent selection by seizure type; NCIT: Anticonvulsant Agent).
- **Developmental and rehabilitative therapies** — physical, occupational, and speech therapy; special education.
- **Surveillance and management** of ophthalmologic (retinopathy), audiologic (hearing loss, hearing aids), cardiac (congenital defect management), genitourinary (cryptorchidism — orchidopexy), and gastrointestinal/feeding complications.
- **Nutritional support** for feeding difficulties and growth failure.

No pharmacogenomic guidance, gene therapy, cell therapy, RNA-based therapy, or targeted/immunotherapy is currently available or in trials for MRXS35 (no NCT identifiers retrieved). Personalized/precision approaches remain theoretical.

### 13. Prevention

Primary prevention is not possible for a spontaneous/inherited Mendelian variant. **Secondary/tertiary prevention** centers on early molecular diagnosis, early developmental intervention, and surveillance to prevent complications (e.g., seizure control, visual/hearing rehabilitation). **Genetic counseling** is central: for carrier mothers, recurrence risk is 50% for sons (affected) and 50% for daughters (carriers). **Reproductive options** include prenatal diagnosis and preimplantation genetic testing for known familial variants, and cascade testing of at-risk female relatives. No immunization, public-health, or environmental interventions apply.

### 14. Other Species / Natural Disease

*RPL10* is **highly evolutionarily conserved.** Orthologs: mouse *Rpl10* (NCBI 110954; MGI:105943; ENSMUSG00000008682); zebrafish *rpl10* (NCBI 336712); *S. cerevisiae* RPL10. No naturally occurring companion-animal or wildlife disease equivalent to MRXS35 is documented in the retrieved data (no OMIA entry established here). Conservation of uL16's role in subunit joining across yeast, fish, and mammals underpins the validity of cross-species functional modeling. No zoonotic or cross-species transmission is relevant (non-infectious genetic disorder).

### 15. Model Organisms

The principal disease model is the **zebrafish** (*Danio rerio*): morpholino knockdown of *rpl10* reproduces reduced head size, decreased bulk translation, and increased brain apoptosis; complementation (rescue) assays with wild-type vs. mutant human *RPL10* established loss-of-function for p.K78E ([PMID: 25316788](https://pubmed.ncbi.nlm.nih.gov/25316788/)). This model recapitulates the core microcephaly phenotype and directly demonstrates the translation–apoptosis mechanism. **Yeast** (*S. cerevisiae*) provided foundational evidence that QM/uL16 assembles onto the 60S subunit in the cytoplasm and is required for subunit joining ([PMID: 9443083](https://pubmed.ncbi.nlm.nih.gov/9443083/)). A validated **mouse** ortholog exists (MGI:105943) and would be the natural system for a conditional/knock-in model, though a published MRXS35-specific mouse model was not identified. **Limitations:** morphant models capture microcephaly/translation defects but not the full multisystem, behavioral (ASD/epilepsy), or progressive retinal spectrum; humanized knock-in mammalian models are a key gap.

---

## Mechanistic Model / Interpretation

```
   RPL10 hypomorphic missense variant (e.g., p.K78E, p.R116Q, p.R32L)
                          │
                          ▼
   Impaired / reduced uL16 protein (loss-of-function; near PTC)
                          │
                          ▼
   Defective late 60S maturation → impaired 40S–60S subunit joining
                          │
                          ▼
   Fewer actively translating 80S ribosomes → ↓ bulk protein synthesis
                          │
             ┌────────────┴─────────────┐
             ▼                          ▼
   ↑ neuronal apoptosis          reduced neuronal output/proliferation
             │                          │
             └────────────┬─────────────┘
                          ▼
         Reduced brain growth  →  MICROCEPHALY (progressive)
         Disrupted neurodevelopment → ID, ASD, EPILEPSY, cerebellar signs
                          │
                          ▼ (tissue-specific translational vulnerability — branch)
   Retinal degeneration (p.R32L) · Hearing loss + cardiac defects (p.K78E)
   Genitourinary / GI / laryngeal anomalies · Growth failure

   ─────────────────────────────────────────────────────────────
   CONTRAST — same gene, different disease:
   SOMATIC RPL10 p.R98S (T-ALL, ~8%) → JAK-STAT gain-of-function,
   ↑ serine/glycine biosynthesis (PSPH), oncogenic mutagenesis (NOTCH1)
```

The unifying principle is **dosage-sensitive translational insufficiency in a highly constrained ribosomal protein**: because *RPL10* is LoF-intolerant (pLI 0.997), only partial (hypomorphic) missense alleles are compatible with survival, and their effect manifests most severely in the high-translation-demand developing brain. The germline (hypomorphic, developmental) and somatic (R98S, oncogenic gain-of-function) diseases are cleanly dissociable — a valuable illustration of allele- and context-specific pathobiology.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [25316788](https://pubmed.ncbi.nlm.nih.gov/25316788/) | *Novel ribosomopathy caused by dysfunction of RPL10… X-linked microcephaly* | Defines gene, XLR inheritance, LoF mechanism (zebrafish) | Human + model organism |
| [16940977](https://pubmed.ncbi.nlm.nih.gov/16940977/) | *Mutations in RPL10 suggest a novel disease mechanism for autism* | Original RPL10 identification (L206M, H213Q) | Human clinical |
| [9443083](https://pubmed.ncbi.nlm.nih.gov/9443083/) | *Assembly of the QM protein onto the 60S subunit… cytoplasm* | Normal uL16 function (subunit joining) | In vitro / yeast |
| [35876338](https://pubmed.ncbi.nlm.nih.gov/35876338/) | *Postnatal microcephaly and retinal involvement expand phenotype* | Phenotype spectrum, ~50% microcephaly, conservation, gnomAD-absent | Human clinical |
| [25846674](https://pubmed.ncbi.nlm.nih.gov/25846674/) | *RPL10 mutation segregating in family with XLID* | Per-feature frequencies in affected family | Human clinical |
| [29066376](https://pubmed.ncbi.nlm.nih.gov/29066376/) | *De novo RPL10 mutation… syndromic ID and epilepsy* | Severe end (p.K78E) phenotype; review | Human clinical |
| [40861044](https://pubmed.ncbi.nlm.nih.gov/40861044/) | *Novel hemizygous missense RPL10 (p.R116Q)* | New allele, maternal inheritance, in vitro LoF, expanded neonatal features | Human + in vitro |
| [28744013](https://pubmed.ncbi.nlm.nih.gov/28744013/) | *RPL10 R98S enhances JAK-STAT signaling* | Distinct somatic oncogenic mechanism | Model / in vitro |
| [30482776](https://pubmed.ncbi.nlm.nih.gov/30482776/) | *Ribosomal lesions promote oncogenic mutagenesis* | R98S recurrent in T-ALL; secondary mutagenesis | Model / in vitro |
| [31186416](https://pubmed.ncbi.nlm.nih.gov/31186416/) | *Altered serine and glycine metabolism in T-ALL* | R98S metabolic rewiring (PSPH) | Model / in vitro |
| [31090057](https://pubmed.ncbi.nlm.nih.gov/31090057/) | *MidXq28-duplication syndrome* | Multigenic Xq28 CNV context (FLNA, RPL10, GDI1) | Human clinical |
| [20004760](https://pubmed.ncbi.nlm.nih.gov/20004760/) | *Dosage-dependent Xq28 copy-number gain* | GDI1 dosage as likelier CNV driver; skewed XCI | Human clinical |

Reference databases used: OMIM (#300998, gene-MIM 312173), gnomAD v2 (constraint), UniProt P27635, PDB (≥37 human 80S ribosome structures), ClinVar (~404 records, NM_006013.5), NCBI Gene / Ensembl / HGNC, and MGI/ZFIN (orthologs).

---

## Limitations and Knowledge Gaps

1. **Small N.** Fewer than ~20 molecularly confirmed males limit precise frequency estimates, genotype–phenotype correlation, and epidemiology (no reliable prevalence/incidence).
2. **VUS-dominant variant landscape.** Most *RPL10* missense variants in ClinVar are VUS; functional assays exist for only a few alleles (p.K78E, p.R116Q), so many candidate variants cannot be confidently classified.
3. **Mechanistic gaps.** The steps from reduced translation to specific clinical features (epilepsy, ASD, retinopathy, cardiac/GU anomalies) are largely inferred, not directly demonstrated in human neurons or organoids; the basis for tissue- and allele-specific involvement is unresolved.
4. **No mammalian disease model.** Published evidence rests on zebrafish morphants and yeast; a humanized knock-in mouse recapitulating the full syndrome is absent.
5. **No natural-history or quality-of-life data**, no biomarkers, and no therapeutic development specific to MRXS35.
6. **CNV vs point-mutation ambiguity.** Xq28 CNVs spanning *RPL10* involve multiple candidate genes (GDI1, FLNA), complicating attribution to *RPL10* itself.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a humanized knock-in mouse or human iPSC-derived neuron/organoid model** carrying p.K78E and p.R116Q to directly test the translation→apoptosis→microcephaly chain and dissect cell-type-specific vulnerability (neurons, photoreceptors, cardiomyocytes).
2. **Systematic functional assays** (subunit-joining, polysome profiling, ribosome footprinting) across all reported and VUS alleles to reclassify VUS and build a genotype–severity map — strengthening ACMG PS3 evidence.
3. **International patient registry / natural-history study** to quantify per-phenotype frequencies, onset, progression (especially microcephaly and retinopathy), survival, and quality of life.
4. **Translatome/single-cell profiling** of patient-derived neurons to identify the specific mRNAs whose translation is most sensitive to uL16 loss — candidate downstream effectors and biomarkers.
5. **Structural analysis** (cryo-EM/AlphaFold) mapping Arg32, Lys78, Arg116, Leu206, His213 onto the human 80S ribosome to model how each substitution perturbs rRNA binding and subunit joining.
6. **Explore translation-modulating or apoptosis-limiting therapeutic strategies** in the zebrafish/organoid models as proof-of-concept, given the absence of any disease-modifying therapy.

---

*Report compiled from 5 completed investigation iterations, 7 confirmed findings, and 19 reviewed papers. Evidence types are distinguished as human clinical, model organism, in vitro, and computational throughout.*


## Artifacts

- [OpenScientist final report](Intellectual_Disability_X-linked_Syndromic_35-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Disability_X-linked_Syndromic_35-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:30482776` (6 mentions) - Ribosomal Lesions Promote Oncogenic Mutagenesis.
  - shared terms: protein, disorder

Weighed against this report's own most characteristic terms: `rpl10`, `variant`, `mrxs35`, `gene`, `microcephaly`, `k78e`, `missense`, `allele`, `disease`, `loss`, `ul16`, `protein`, `zebrafish`, `subunit`, `disorder`, `epilepsy`, `xq28`, `functional`, `x-linked`, `disability`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001999` (1 mention) - the report calls it "Very frequent"; HP calls it **Abnormal facial shape**
- `HP:0001250` (1 mention) - the report calls it "Frequent"; HP calls it **Seizure**
- `HP:0000717` (1 mention) - the report calls it "Frequent"; HP calls it **Autism**
- `HP:0001561` (1 mention) - the report calls it "Frequent (3/4)"; HP calls it **Polyhydramnios**
- `HP:0004322` (1 mention) - the report calls it "Frequent"; HP calls it **Short stature**
- `HP:0000546` (1 mention) - the report calls it "Subset"; HP calls it **Retinal degeneration**
- `HP:0000365` (1 mention) - the report calls it "Subset"; HP calls it **Hearing impairment**
- `HP:0001627` (1 mention) - the report calls it "Subset"; HP calls it **Abnormal heart morphology**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0022618` (1 mention) - the report calls it "ribonucleoprotein complex assembly"; GO calls it **protein-RNA complex assembly**, and lists "ribonucleoprotein complex assembly" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.