---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T04:59:26.961672'
end_time: '2026-10-20T05:11:45.498941'
duration_seconds: 738.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PLPBP-Related Pyridoxine-Dependent Epilepsy
  mondo_id: MONDO:0015005
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openai
  succeeded: false
  error_type: ProviderAuthError
  status_code: 401
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 6
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:27912044
  relevance_assessed: 19
  on_topic: 9
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 39
  verified: 36
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 2
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0015005
    reported_labels:
    - pyridoxine-dependent epilepsy, umbrella
    - umbrella, pyridoxine-dependent epilepsy
    ontology_label: epilepsy, early-onset, vitamin B6-dependent
  - term_id: HP:0000252
    reported_labels:
    - Frequent
    ontology_label: Microcephaly
  - term_id: HP:0001298
    reported_labels:
    - Common
    ontology_label: Encephalopathy
  - term_id: HP:0012469
    reported_labels:
    - Subset
    ontology_label: Infantile spasms
  - term_id: HP:0003128
    reported_labels:
    - Subset
    ontology_label: Lactic acidosis
  - term_id: CL:0000540
    reported_labels:
    - Cell types / GO-CC:** neurons
    ontology_label: neuron
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0042136
    ontology_label: obsolete neurotransmitter biosynthetic process
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
  path: PLPBP-Related_Pyridoxine-Dependent_Epilepsy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PLPBP-Related_Pyridoxine-Dependent_Epilepsy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PLPBP-Related Pyridoxine-Dependent Epilepsy
- **MONDO ID:** MONDO:0015005 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PLPBP-Related Pyridoxine-Dependent Epilepsy** covering all of the
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

# PLPBP-Related Pyridoxine-Dependent Epilepsy (PLPHP Deficiency): Comprehensive Disease Characterization

**Target disease:** PLPBP-Related Pyridoxine-Dependent Epilepsy (Developmental and Epileptic Encephalopathy 2024; vitamin B6-dependent epilepsy due to PLPHP deficiency)
**MONDO:** MONDO:0015005 (pyridoxine-dependent epilepsy, umbrella). **Category:** Mendelian, autosomal recessive.
**Evidence base:** 27 literature sources reviewed; 11 confirmed findings recorded. This is a literature-based synthesis (no primary patient dataset provided). Evidence types are flagged as *human clinical*, *model organism*, *in vitro/biochemical*, or *computational/structural*.

> **Important caveat on rarity:** As of 2026 only ~54 patients have been reported worldwide (Alsini et al. 2026, PMID 41671913). Many disease parameters (precise prevalence, penetrance, QoL metrics, survival curves) are therefore **not formally established** and are noted as such.

---

## 1. Disease Information

PLPBP-related pyridoxine-dependent epilepsy is a rare autosomal-recessive inborn error of **vitamin B6 (pyridoxal 5'-phosphate, PLP) homeostasis** that presents as a **neonatal-onset developmental and epileptic encephalopathy**. Seizures are typically refractory to conventional antiepileptic drugs (AEDs) but respond to vitamin B6 (pyridoxine or PLP). It was first defined molecularly in 2016 when biallelic *PROSC* (now *PLPBP*) mutations were shown to "disrupt cellular pyridoxal phosphate homeostasis and cause vitamin-B6-dependent epilepsy" (Darin et al., PMID 27912044). *Information source:* aggregated individual case reports and small cohorts/systematic reviews (not population EHR).

**Key identifiers**
- **Gene:** *PLPBP* (formerly *PROSC*); HGNC:30042; NCBI Gene 65015; Ensembl ENSG00000147471; UniProt O94903 (PLPHP_HUMAN). Locus **8p11.23**.
- **Protein:** PLPHP / PLP-BP (pyridoxal 5'-phosphate homeostasis protein).
- **OMIM:** gene *PLPBP* #604436; phenotype **#617290** (Developmental and epileptic encephalopathy 2024, formerly EIEE/pyridoxine-dependent).
- **Orphanet:** within "Pyridoxine-dependent epilepsy" (ORPHA:3006 umbrella; PLPHP deficiency as a molecular subtype).
- **ICD-11:** 8A61 (developmental and epileptic encephalopathies) / 5C50.A (disorders of vitamin B6 metabolism). **ICD-10:** G40.4 + E53.1 (vitamin B6 deficiency) as proxies.
- **MeSH:** "Seizures" / "Epilepsy" + "Vitamin B 6"; no dedicated MeSH heading for PLPHP deficiency.
- **MONDO:** MONDO:0015005 (umbrella, pyridoxine-dependent epilepsy).

**Synonyms / alternative names:** PLPHP deficiency; PLPBP deficiency; PROSC-related/PROSC deficiency epilepsy; Vitamin B6-dependent epilepsy (PLPBP type); Pyridoxine-dependent epilepsy type 2/PLPBP; Developmental and epileptic encephalopathy 2024.

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound heterozygous) pathogenic variants in *PLPBP*. "*Biallelic pathogenic variants in PLPBP (formerly called PROSC) have recently been shown to cause a novel form of vitamin B6-dependent epilepsy*" (Johnstone et al. 2019, PMID 30668673). No environmental or infectious primary cause; the disease is monogenic.

**Genetic risk factors.** The disease-causing variants themselves are the risk factor. **Consanguinity** strongly elevates risk (many reported families are consanguineous; e.g., a first-cousin Pakistani family, Ahmed et al. 2020, PMID 33425341). A recurrent/founder deletion **c.370_373del (p.Asp124fs)** is the single most frequent variant (18.5% of alleles; Alsini 2026, PMID 41671913; also a founder allele reported by Pal et al. 2021, PMID 33977028).

**Environmental risk factors.** None established as causal. However, **intercurrent viral illness/fever can trigger breakthrough seizures or metabolic crises** (Takle et al. 2025, PMID 42563912) — a gene–environment interaction where physiological stress increases demand on an already-compromised PLP-homeostasis system. **Age:** risk window is prenatal/neonatal (congenital metabolic demand). **Sex:** no predilection (AR).

**Protective factors.** No validated genetic protective alleles or modifier genes are published. The principal *modifiable* protective factor is **early vitamin B6 supplementation**, which is treatment rather than a constitutional protective factor. Residual protein function (hypomorphic missense vs. null) is inferred to be protective against the most severe phenotype (genotype–severity correlation, Finding 10).

**Gene–environment interaction.** Illness-provoked crises (above) are the clearest example; otherwise GxE data are *not available* for this ultra-rare disease.

---

## 3. Phenotypes

Core phenotype = **neonatal developmental and epileptic encephalopathy**. Data below are from case series and the 54-patient systematic review (Alsini 2026, PMID 41671913; Johnstone 2019, PMID 30668673).

| Phenotype | Type | Onset | Severity | Frequency | HPO |
|---|---|---|---|---|---|
| Neonatal seizures (multifocal, clonic, tonic, myoclonic, status epilepticus) | Clinical sign | Neonatal (55.5% <24 h; 76% <1 week) | Severe | ~100% | HP:0032807 (Neonatal seizure), HP:0002133 (Status epilepticus), HP:0032794 (Clonic seizure) |
| AED-resistant, B6-responsive seizures | Clinical sign | Neonatal | Severe | ~100% | HP:0011097 (Epileptic spasm), HP:0001250 (Seizure) |
| Global developmental delay / intellectual disability | Clinical sign | Infancy onward | Moderate–severe (>2/3 patients) | Majority | HP:0001263, HP:0001249 |
| Microcephaly (often congenital) | Physical manifestation | Congenital/early | Variable | Frequent | HP:0000252 |
| Encephalopathy | Clinical sign | Neonatal | Severe (untreated) | Common | HP:0001298 |
| Movement disorder: myoclonus, tremor, abnormal eye movements (OMAS-like) | Clinical sign | Infancy/childhood | Variable, episodic | Subset | HP:0001336 (Myoclonus), HP:0002072, HP:0000496 |
| Infantile spasms (± hypsarrhythmia) | Clinical sign | Infancy | Variable | Subset | HP:0012469 |
| Prematurity, fetal distress, antenatal anomalies | Perinatal | Prenatal/birth | — | Common | HP:0001622, HP:0001623 |
| Lactic acidemia (nonspecific) | Lab abnormality | Neonatal | — | Subset | HP:0003128 |
| Hyperglycinemia / elevated glycine & glutamine | Lab abnormality | Neonatal | — | Subset | HP:0002154 (Hyperglycinemia) |

**Progression:** Seizures are **episodic/fluctuating** acutely and become **treatment-controlled** on B6; the underlying encephalopathy is largely **static** but with persistent developmental impairment. **Quality of life:** no formal EQ-5D/PROMIS data exist; QoL is reduced in proportion to intellectual disability, epilepsy burden, and microcephaly (*not formally quantified*).

---

## 4. Genetic / Molecular Information

- **Causal gene:** *PLPBP* (HGNC:30042; OMIM 604436; 8p11.23). Encodes PLPHP (296 aa; UniProt O94903).
- **Variant spectrum (Alsini 2026, PMID 41671913; Johnstone 2019, PMID 30668673):** **missense ≈48%** (most common class), plus frameshift, nonsense, splice-site, and small indels. Representative variants: **c.370_373del (p.Asp124fs)** — most frequent/founder (18.5%); **c.46_47insCA (p.Leu17Hisfs)** (Ahmed 2020, PMID 33425341); **c.695C>T (p.Ala232Val)** missense (İpek 2022, PMID 36308585).
- **Classification (ACMG/AMP):** reported variants are Pathogenic/Likely pathogenic in ClinVar; biallelic requirement.
- **Allele frequency:** individually ultra-rare in gnomAD (consistent with AR disease; carrier frequency not precisely established, inferred very low outside founder contexts).
- **Origin:** **germline** (constitutional). No somatic involvement.
- **Functional consequence:** predominantly **loss of function** — null alleles or missense that reduce protein **stability and/or PLP-binding**. "The most severe phenotypes were associated with variants leading to loss of function of PLPBP or significantly affecting protein stability/PLP-binding" (Johnstone 2019, PMID 30668673).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none established; no reported CNVs, methylation signatures, or cytogenetic lesions. *Not applicable / not available.*

---

## 5. Environmental Information

- **Environmental factors / toxins / occupational exposures:** none causal (*not applicable*).
- **Lifestyle factors:** not relevant to a neonatal monogenic disorder; however **dietary vitamin B6 status** modulates the biochemical state, and B6 supplementation is therapeutic.
- **Infectious agents:** none cause the disease, but **viral illnesses act as triggers** for seizure/metabolic decompensation (Takle 2025, PMID 42563912). NCBI Taxonomy not applicable to etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)
1. **Biallelic loss-of-function *PLPBP* variants** → reduced amount or stability/activity of **PLPHP** protein (*demonstrated*: protein-stability/PLP-binding modeling, Johnstone 2019 PMID 30668673).
2. Loss of PLPHP → **failure of intracellular PLP homeostasis/chaperoning** — the cell can no longer safely buffer and deliver the reactive aldehyde PLP to apo-enzymes (*demonstrated in vitro/structurally*: He 2022 PMID 35897955; "mediates PLP homeostasis by delivering PLP to target enzymes or by performing a protective function").
3. This **leads to** two branches:
   - **Branch A (substrate starvation):** many **PLP-dependent enzymes** receive insufficient correctly-delivered PLP → **reduced holoenzyme activity**.
   - **Branch B (toxic vitamer accumulation):** aberrant accumulation of **pyridoxine 5'-phosphate (PNP)** (*demonstrated in bacteria/in vitro*: Ito 2020 PMID 31677193; Ito 2022 PMID 34978460), which **directly inhibits** PLP-dependent enzymes (e.g., the **glycine cleavage system**).
4. Both branches **result in** dysregulation of **amino-acid and neurotransmitter metabolism** — notably **GABA synthesis (glutamate decarboxylase, GAD)**, **glycine catabolism**, and **catecholamine/monoamine synthesis (aromatic L-amino-acid decarboxylase, AADC)** (*model-organism evidence*: zebrafish *plpbp*−/− shows "disruptions in amino acid metabolism as well as GABA and catecholamine pathways", Johnstone 2019 PMID 30668673).
5. Imbalanced excitatory/inhibitory neurotransmission (inferred: ↓GABA, altered glycine/glutamate) → **neuronal hyperexcitability** → **refractory neonatal seizures** (*phenotype demonstrated*; precise neurotransmitter stoichiometry *inferred*).
6. Sustained seizures + metabolic derangement during a critical developmental window → **encephalopathy, white-matter injury, impaired brain growth (microcephaly)** → **developmental delay / intellectual disability**; untreated → **status epilepticus and death in infancy** (Johnstone 2019 PMID 30668673).
7. **Therapeutic branch:** exogenous **vitamin B6 (pyridoxine → PLP, or direct PLP)** raises PLP availability, partially restoring enzyme function → **seizure control** (*demonstrated* in humans and rescued in zebrafish, PMID 30668673).

### Supporting detail by category
- **Molecular pathways / metabolic changes:** vitamin B6 (PLP) metabolism and dependent pathways — amino-acid metabolism (glycine cleavage, aspartate/serine), neurotransmitter biosynthesis (GABA via GAD, dopamine/serotonin via AADC), transsulfuration. KEGG: vitamin B6 metabolism (map00750). GO: vitamin B6 metabolic process (GO:0042816), pyridoxal phosphate biosynthetic process (GO:0042823), neurotransmitter biosynthetic process (GO:0042136).
- **Protein dysfunction:** PLPHP has a **type III TIM-barrel fold** (He 2022, PMID 35897955) with a conserved phosphate-coordinating PLP pocket; pathogenic missense destabilize the fold or the PLP site (loss of function; no dominant-negative or gain-of-function reported). PDB homologs exist for bacterial YggS; human structure via AlphaFold (O94903).
- **Biochemical abnormalities:** functional insufficiency of multiple PLP-dependent enzymes; accumulation of PNP; nonspecific hyperglycinemia and lactic acidemia (Jensen 2019, PMID 31741821).
- **Moonlighting / non-canonical functions:** PLPHP is **also an RNA-binding protein** (Graziani 2024, PMID 39604152) and has a **mitochondrial pool** linked to proteostasis (accumulates when mitochondrial peptidase CLPP is lost; Key 2023, PMID 38139332); PLP-independent functions are reported for the cyanobacterial ortholog PipY (Llop 2026, PMID 41820517). These broaden the mechanism beyond cytosolic PLP delivery and may explain **mitochondrial-disease mimicry** and nonspecific lactic acidemia.
- **Cellular processes / tissue damage:** neuronal hyperexcitability and excitotoxic/seizure-related injury (inferred); no primary inflammatory or autoimmune component. **Immune involvement: not applicable.**
- **Cell types / GO-CC:** neurons (CL:0000540), especially **GABAergic neurons** (CL:0000617); glia secondary. Subcellular: **cytosol (GO:0005829)** and **mitochondrion (GO:0005739)**; molecular function **pyridoxal phosphate binding (GO:0030170)**, **RNA binding (GO:0003723)**.
- **CHEBI chemical entities:** pyridoxal 5'-phosphate (CHEBI:18405), pyridoxine (CHEBI:16709), pyridoxine 5'-phosphate (CHEBI:58589), γ-aminobutyric acid (CHEBI:16865), glycine (CHEBI:15428).
- **Molecular profiling (omics):** no human transcriptomic/proteomic/metabolomic disease atlas published; metabolic perturbations characterized in zebrafish and bacterial models (*model-organism evidence*).

---

## 7. Anatomical Structures Affected

- **Organ/system:** **central nervous system / nervous system (UBERON:0001016)** is the primary target; brain (UBERON:0000955). No consistent extra-CNS organ disease.
- **Regional (imaging, Alsini 2026, PMID 41671913):** abnormalities in **65%** — **white matter (UBERON:0002316) abnormalities 54%**, **periventricular/temporal cysts 27%**, **corpus callosum (UBERON:0002336) anomalies 15.4%**, global brain underdevelopment with broad gyri/shallow sulci; cerebral cortex (UBERON:0000956) involvement.
- **Tissue/cell:** nervous tissue; neurons (CL:0000540), GABAergic neurons (CL:0000617); glia/white-matter tracts secondarily.
- **Subcellular:** cytosol (GO:0005829) and mitochondrion (GO:0005739).
- **Lateralization:** **bilateral**, diffuse/global (consistent with a metabolic encephalopathy); not focal/lateralized.

---

## 8. Temporal Development

- **Onset:** **congenital/neonatal.** Seizures begin very early — 55.5% within the first 24 h and 76% within the first week of life (Alsini 2026, PMID 41671913); rare later-onset (infantile) cases exist. Onset pattern: **acute** seizures on a congenital metabolic background. Some fetal seizure activity/antenatal anomalies reported.
- **Progression:** acute refractory phase → **treatment-induced remission** of seizures on B6 → **chronic, largely static encephalopathy** with persistent developmental impairment. Disease course for seizures is **episodic** (with illness-triggered breakthroughs) superimposed on a stable deficit.
- **Duration:** **chronic, lifelong**; requires lifelong B6 supplementation (withdrawal → seizure recurrence).
- **Remission:** **treatment-induced** (vitamin B6), not spontaneous.
- **Critical period:** the **neonatal/early-infantile window** is the key opportunity for intervention; earlier treatment limits (but does not eliminate) neurodevelopmental damage.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive.** Biallelic variants required; parents are obligate carriers.
- **Epidemiology:** **ultra-rare.** Overall pyridoxine-dependent epilepsy birth incidence ≈ **1:396,000 (definite/probable) to 1:252,000 (incl. possible)** in the Netherlands (Been 2005, PMID 16159904) — figures dominated by ALDH7A1. **PLPBP is a small minority**: ~30 patients by 2020 (Ahmed, PMID 33425341), **54 by 2026** (Alsini, PMID 41671913). Point prevalence: not formally established (<1/1,000,000, inferred).
- **Penetrance:** appears **complete** for biallelic LoF (all reported biallelic patients are affected); formal penetrance estimates unavailable.
- **Expressivity:** **variable** — severity correlates with residual protein function (LoF/unstable = severe).
- **Anticipation:** **not applicable** (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported.
- **Founder effects:** **c.370_373del** acts as a recurrent/founder allele (Pal 2021, PMID 33977028; Alsini 2026).
- **Consanguinity:** major contributor; many homozygous cases in consanguineous families.
- **Carrier frequency:** very low, not precisely quantified.
- **Demographics:** reported worldwide (Europe, Middle East/Saudi Arabia, Pakistan, North America, East Asia); **higher counts in consanguineous populations**. **Sex ratio ≈ 1:1** (AR). **Age distribution:** overwhelmingly neonates/infants at presentation.

---

## 10. Diagnostics

- **No specific diagnostic metabolite** (unlike ALDH7A1 → ↑α-AASA/pipecolic acid, or PNPO). Biochemistry is **nonspecific**: "diagnostic pitfalls, including lactic acidemia as well as hyperglycinemia, highlighting the importance of a pyridoxine trial, and genetic testing" (Jensen 2019, PMID 31741821); elevated glycine/glutamine may occur (Takle 2025, PMID 42563912). LOINC-codable labs: plasma amino acids (glycine), lactate, CSF neurotransmitter metabolites.
- **Clinical/functional tests:** **EEG** (multifocal/burst-suppression or spasms; infantile spasms sometimes without hypsarrhythmia — Kalser 2023, PMID 36577449); **therapeutic trial of pyridoxine (± PLP)** with seizure response is a key diagnostic maneuver.
- **Imaging:** brain **MRI** frequently abnormal (65%) — white-matter changes, periventricular/temporal cysts, callosal anomalies, atrophy (Alsini 2026, PMID 41671913). RadLex: cerebral white matter lesion.
- **Genetic testing (definitive):** **WES or WGS**, or **epilepsy/vitamin-B6 gene panels** including *PLPBP*; single-gene *PLPBP* sequencing when clinically suspected. WES often succeeds after nondiagnostic panels (Takle 2025, PMID 42563912). CMA/karyotype/FISH generally unrevealing (no CNVs reported). Mitochondrial DNA/repeat-expansion testing not indicated (though mitochondrial disease is a common misdiagnosis).
- **Clinical criteria & differential diagnosis:** diagnosis rests on **B6-responsive neonatal epilepsy + biallelic *PLPBP* variants**. Differentials: **ALDH7A1** (classic PDE; ↑α-AASA), **PNPO** deficiency (PLP-responsive), **hypoxic-ischemic encephalopathy**, **mitochondrial encephalopathy**, **folinic-acid-responsive seizures** (allelic with ALDH7A1), **AADC deficiency**, **nonketotic hyperglycinemia**, and **opsoclonus-myoclonus-ataxia syndrome (OMAS)** (Johnstone 2019 PMID 30668673; Takle 2025 PMID 42563912).
- **Screening:** **not on standard newborn screening** (no specific metabolite). **Cascade/carrier testing** in families with a known variant and **prenatal/preimplantation testing** are feasible once the familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Untreated disease is fatal** — "can progress to status epilepticus and death in infancy" (Johnstone 2019, PMID 30668673). With treatment, survival into childhood/adulthood is expected; formal survival rates unpublished.
- **Morbidity/function:** **Guarded** — **>2/3 of patients classified moderate-to-severe** on a combined neurodevelopmental/seizure-control severity score (Alsini 2026, PMID 41671913). Common sequelae: intellectual disability, developmental delay, microcephaly, ongoing epilepsy risk.
- **Disease course/complications:** chronic static encephalopathy; breakthrough seizures during illness; feeding/motor impairment in severe cases.
- **Recovery potential:** seizures are usually controllable with B6, but **neurocognitive recovery is incomplete**; earlier treatment improves but does not normalize outcomes.
- **Prognostic factors:** **variant class (LoF/unstable → worse)**, treatment delay, neonatal seizure burden, degree of MRI abnormality/microcephaly. **Prognostic biomarkers:** none validated; genotype is the best available predictor. QoL: no EQ-5D/SF-36/PROMIS data (*not available*).

---

## 12. Treatment

- **Pharmacotherapy (disease-specific):** **Vitamin B6.** "neonatal onset seizures responsive to treatment with vitamin B6 available as **pyridoxine (PN)** or as the biologically active form **pyridoxal 5-phosphate (PLP)**" (Ahmed 2020, PMID 33425341). Seizures are "generally resistant to traditional antiepileptic drugs and show a dramatic response to high-dose pyridoxine" (İpek 2022, PMID 36308585). Some patients respond to pyridoxine, others require PLP; **lifelong supplementation** is mandatory (withdrawal → recurrence). NCIT: **Pyridoxine (C745)**, **Pyridoxal Phosphate (C84305)**, Pyridoxine Therapy. CHEBI: pyridoxine (CHEBI:16709), PLP (CHEBI:18405). DrugBank: Pyridoxine DB00165; Pyridoxal phosphate DB00114.
- **Pharmacogenomics / personalized:** treatment is **genotype-directed** — confirming *PLPBP* distinguishes it from ALDH7A1/PNPO and dictates B6 (not diet) therapy. PN vs PLP choice is individualized.
- **Supportive AEDs:** conventional AEDs are largely ineffective as monotherapy but may be adjuncts; standard supportive/rehabilitative care (PT/OT/speech), developmental support, nutrition.
- **Therapies that do NOT apply:** **lysine-reduction therapy** (dietary lysine restriction ± arginine), which benefits ALDH7A1 PDE by lowering α-AASA (Coughlin 2022, PMID 36008148), is **mechanistically irrelevant** to PLPBP (no α-AASA accumulation).
- **Advanced therapeutics:** **No approved gene, cell, or RNA therapy.** Gene replacement is conceptually attractive (monogenic LoF) but **not in clinical trials** for *PLPBP* (*not available*). No disease-specific NCT trials identified.
- **Treatment outcomes / adverse events:** B6 generally controls seizures; **high-dose pyridoxine carries a risk of sensory peripheral neuropathy** (a general class effect) — dosing should balance efficacy and toxicity (monitor). FAERS: pyridoxine neuropathy at high chronic doses.

---

## 13. Prevention

- **Primary prevention:** not possible at the individual level (monogenic, congenital). **Genetic counseling** for carrier couples (25% recurrence risk per pregnancy, AR) and **reproductive options** (prenatal diagnosis, PGT-M) where the familial variants are known.
- **Secondary prevention:** **early recognition and prompt B6 trial** in any neonate with unexplained AED-resistant seizures; early molecular diagnosis (WES/WGS) to start targeted therapy within the critical window.
- **Tertiary prevention:** lifelong B6 to prevent seizure recurrence; **supplement during intercurrent illness** to avert illness-triggered crises; developmental/rehabilitative support to mitigate disability.
- **Immunization / public-health / environmental measures:** not applicable (no infectious or environmental cause), though routine childhood vaccination to reduce febrile-illness triggers is prudent supportive advice.
- **Counseling:** AR genetic counseling is the cornerstone of prevention (NSGC/ACMG frameworks); cascade carrier testing for relatives.

---

## 14. Other Species / Natural Disease

- **Evolutionary conservation:** the **YggS/Ybl036c/PLPBP (COG0325) family is "widely conserved across the three domains of life"** (Xu 2026, PMID 42803569) — bacteria, archaea, eukaryotes.
- **Orthologs / NCBI identifiers:** human *PLPBP* (Gene 65015); mouse *Plpbp* (NCBI Taxon 10090); zebrafish *plpbp* (Taxon 7955, ZFIN); *E. coli* **yggS** (Taxon 562); *Salmonella enterica* **yggS** (Taxon 28901); *S. cerevisiae* **YBL036C** (Taxon 4932); cyanobacterial **PipY**.
- **Natural disease in animals:** **no naturally occurring companion-animal/wildlife disease documented (OMIA: none established)** — human disease and engineered models only. **Veterinary relevance: minimal/not applicable.**
- **Comparative biology:** loss of the ortholog disrupts **amino-acid metabolism via PNP** across species (bacteria: Ito 2019/2020 PMIDs 30902856, 31677193; *Salmonella* aspartate metabolism, Vu & Downs 2021 PMID 34498310), indicating deep conservation of the **PLP-homeostasis mechanism**.
- **Transmission / zoonosis:** **not applicable** (genetic disease).

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*, Taxon 7955) — best vertebrate model.** CRISPR/Cas9 **plpbp−/−** larvae: behavioural, biochemical, and electrophysiological **seizures by 10 dpf**, **death by 16 dpf**, with **disrupted amino-acid, GABA and catecholamine metabolism**; **pyridoxine rescues** the phenotype and extends lifespan (Johnstone 2019, PMID 30668673). **Phenotype recapitulation: high** (seizures, early lethality, B6-responsiveness). **Limitation:** does not capture human cortical white-matter/structural changes or long-term cognition. Resource: ZFIN.
- **Bacterial models — mechanistic workhorses.** *E. coli* **yggS** and *Salmonella* **yggS** mutants reveal **PNP accumulation**, glycine-cleavage-system inhibition and amino-acid metabolic disruption (Ito 2019/2020 PMIDs 30902856, 31677193; Vu & Downs 2021 PMID 34498310). **Limitation:** no nervous system; purely biochemical.
- **Yeast (*S. cerevisiae* YBL036C) and cyanobacterial PipY** — structure/function and PLP-independent/moonlighting roles (Llop 2026, PMID 41820517).
- **In vitro / structural:** bacterial YggS crystal structures (TIM-barrel; He 2022 PMID 35897955); human PLPHP biochemistry incl. **RNA-binding** (Graziani 2024 PMID 39604152); AlphaFold model (UniProt O94903).
- **Mammalian (mouse *Plpbp*):** ortholog exists and PLPBP biology probed indirectly (e.g., CLPP-KO mitochondrial study, Key 2023 PMID 38139332); **no widely-reported dedicated *Plpbp* mouse epilepsy model** (*gap / not available*). Resources: MGI, IMPC.

---

## Summary of Supported vs. Open Questions

**Supported (high confidence):**
- Monogenic AR disease from biallelic *PLPBP* LoF variants disrupting PLP homeostasis (PMID 27912044, 30668673).
- Neonatal-onset, AED-resistant, **B6-responsive** epileptic encephalopathy (PMID 41671913, 36308585, 33425341).
- Mechanism: PLPHP chaperones/buffers PLP and prevents toxic PNP; loss impairs PLP-dependent amino-acid/neurotransmitter enzymes (PMID 35897955, 31677193, 34978460).
- No specific biomarker → diagnosis by B6 trial + molecular testing (PMID 31741821).
- Guarded prognosis despite treatment; genotype–severity correlation (PMID 41671913, 30668673).
- Deep cross-species conservation; zebrafish/bacterial models; lysine-reduction therapy inapplicable (PMID 42803569, 30668673, 36008148).

**Open / not available:**
- Precise prevalence, penetrance, carrier frequency, survival/QoL metrics.
- Human omics atlases (transcriptomic/proteomic/metabolomic) of affected brain.
- Dedicated mammalian (mouse) epilepsy model; approved advanced therapeutics (gene therapy).
- Full in-vivo clarification of the GABA/glycine/catecholamine contributions and the moonlighting RNA-binding/mitochondrial roles in human pathogenesis.

---

### Key references (PMID)
27912044 (Darin 2016, discovery) · 30668673 (Johnstone 2019, cohort + zebrafish) · 41671913 (Alsini 2026, systematic review n=54) · 34978460 & 31677193 & 30902856 (Ito, PNP mechanism) · 35897955 (He 2022, structure) · 39604152 (Graziani 2024, RNA-binding) · 38139332 (Key 2023, mitochondrial pool) · 42803569 (Xu 2026, conservation) · 34498310 (Vu & Downs 2021, Salmonella) · 41820517 (Llop 2026, PipY) · 31741821 (Jensen 2019, diagnostic pitfalls) · 33425341 (Ahmed 2020) · 36308585 (İpek 2022) · 36577449 (Kalser 2023, spasms) · 42563912 (Takle 2025, OMAS mimic) · 33977028 (Pal 2021, founder) · 28391250 (Plecko 2017) · 16159904 (Been 2005, epidemiology) · 36008148 (Coughlin 2022, LRT/ALDH7A1) · 40832147 (Coughlin & Gospe 2023, PDE review).


## Artifacts

- [OpenScientist final report](PLPBP-Related_Pyridoxine-Dependent_Epilepsy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PLPBP-Related_Pyridoxine-Dependent_Epilepsy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:27912044`: "disrupt cellular pyridoxal phosphate homeostasis and cause vitamin-B6-dependent epilepsy"
  - closest text in source: "Circulating alkaline phosphatase levels are high (hyperphosphatasia), and in some individuals, seizures respond to treatment with pyridoxine.9 Enzymes and Transporters Involved in Mammalian CNS PLP Synthesis and Homeostasis and Known Human Genetic Vitamin-B6-Dependent Epilepsies Pyridoxal 5′-phosphate (PLP); pyridoxamine 5′-phosphate (PMP); pyridoxal (PL); pyridoxine (PN); pyridoxine 5′-phosphate (PNP); pyridoxine-5′-β-D-glucoside (PNG); intestinal phosphatases (IP); transporter (identity unknown; T1); pyridoxal kinase (PK); pyridox(am)ine 5′-phosphate oxidase (PNPO); tissue non-specific alkaline phosphatase (TNSALP); pyridoxal-phosphatase (PLPase); aldehyde oxidase (Mo cofactor)/β-NAD dehydrogenase (AOX/DH)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 11 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0015005` (2 mentions) - the report calls it "pyridoxine-dependent epilepsy, umbrella", "umbrella, pyridoxine-dependent epilepsy"; MONDO calls it **epilepsy, early-onset, vitamin B6-dependent**
- `HP:0000252` (1 mention) - the report calls it "Frequent"; HP calls it **Microcephaly**
- `HP:0001298` (1 mention) - the report calls it "Common"; HP calls it **Encephalopathy**
- `HP:0012469` (1 mention) - the report calls it "Subset"; HP calls it **Infantile spasms**
- `HP:0003128` (1 mention) - the report calls it "Subset"; HP calls it **Lactic acidosis**
- `CL:0000540` (2 mentions) - the report calls it "Cell types / GO-CC:** neurons"; CL calls it **neuron**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0042136` (obsolete neurotransmitter biosynthetic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005829` (2 mentions) - the report calls it "Subcellular:** cytosol"; GO calls it **cytosol**
- `CHEBI:18405` (2 mentions) - the report calls it "CHEBI chemical entities:** pyridoxal 5'-phosphate"; CHEBI calls it **pyridoxal 5'-phosphate**
- `UBERON:0001016` (1 mention) - the report calls it "Organ/system:** **central nervous system / nervous system"; UBERON calls it **nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0015005` - called "pyridoxine-dependent epilepsy, umbrella", "umbrella, pyridoxine-dependent epilepsy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.