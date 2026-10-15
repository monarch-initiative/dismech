---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T15:09:43.056421'
end_time: '2026-09-01T15:27:03.690229'
duration_seconds: 1040.63
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: SHORT Syndrome
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 19
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 35
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 0
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0009159
    reported_labels:
    - MONDO
    ontology_label: Ehlers-Danlos syndrome, cardiac valvular type
  - term_id: HP:0001511
    reported_labels:
    - Very common
    ontology_label: Intrauterine growth retardation
  - term_id: HP:0004322
    reported_labels:
    - Common
    ontology_label: Short stature
  - term_id: HP:0000490
    reported_labels:
    - Common
    ontology_label: Deeply set eye
  - term_id: HP:0000347
    reported_labels:
    - Common
    ontology_label: Micrognathia
  - term_id: HP:0000430
    reported_labels:
    - Common
    ontology_label: Underdeveloped nasal alae
  - term_id: HP:0005104
    reported_labels:
    - Common
    ontology_label: Hypoplastic nasal septum
  - term_id: HP:0009125
    reported_labels:
    - Common
    ontology_label: Lipodystrophy
  - term_id: HP:0000855
    reported_labels:
    - Common (metabolic hallmark)
    ontology_label: Insulin resistance
  - term_id: HP:0000684
    reported_labels:
    - Common (eponymous)
    ontology_label: Delayed eruption of teeth
  - term_id: HP:0001382
    reported_labels:
    - Common (eponymous)
    ontology_label: Joint hypermobility
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0000368
    ontology_label: obsolete Low-set, posteriorly rotated ears
    replaced_by: HP:0000358
  - term_id: GO:0014065
    ontology_label: obsolete phosphatidylinositol 3-kinase signaling
    replaced_by: GO:0043491
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
  path: SHORT_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SHORT_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SHORT Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SHORT Syndrome** covering all of the
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

# SHORT Syndrome — Comprehensive Disease Characteristics Report

**Disease:** SHORT Syndrome
**Category:** Mendelian (monogenic)
**Key identifiers:** OMIM #269880 · Orphanet ORPHA:3163 · MONDO:0009159 · ICD-10 Q87.1 · MeSH — indexed under lipodystrophy/insulin-resistance syndromes (no dedicated descriptor)
**Causal gene:** *PIK3R1* (HGNC:8979; OMIM *171833), encoding the p85α regulatory subunit of class IA phosphatidylinositol 3-kinase (PI3K)

---

## Summary

SHORT syndrome is a rare autosomal dominant multisystem disorder whose name is an acronym for its cardinal features: **S**hort stature, **H**yperextensibility of joints, **O**cular depression (deep-set eyes), **R**ieger anomaly (anterior-segment dysgenesis), and **T**eething (delayed dental eruption). It is caused by heterozygous **loss-of-function / dominant-negative mutations in *PIK3R1***, the gene encoding the p85α regulatory subunit of class IA PI3K. Three concurrent 2013 exome-sequencing studies established causality, and the recurrent C-terminal hotspot missense variant **c.1945C>T (p.Arg649Trp)** accounts for the majority of cases ([PMID: 24886349](https://pubmed.ncbi.nlm.nih.gov/24886349/), [PMID: 23980586](https://pubmed.ncbi.nlm.nih.gov/23980586/), [PMID: 24033310](https://pubmed.ncbi.nlm.nih.gov/24033310/)).

The unifying mechanism is **impaired proximal insulin/growth-factor PI3K–AKT signaling**. Mutations cluster in the C-terminal SH2 (cSH2)/inter-SH2 (iSH2) substrate-recognition region of p85α; the mutant subunit fails to relieve p110 catalytic inhibition and fails to transmit receptor-generated phosphotyrosine signals. The downstream consequences—intrauterine growth restriction (IUGR) and postnatal short stature, partial (facial/limb) lipodystrophy, a distinctive severe insulin resistance, progeroid craniofacial dysmorphism, and Rieger anomaly—map onto tissues that depend on PI3K signaling. A **Pik3r1 Arg649Trp knock-in mouse recapitulates the human disease** and directly demonstrates reduced PI3K activation as the mechanism ([PMID: 26974159](https://pubmed.ncbi.nlm.nih.gov/26974159/)).

A distinctive metabolic signature separates SHORT syndrome from common obesity-related insulin resistance: the insulin resistance is **uncoupled from dyslipidemia and hepatic steatosis**, biochemically resembling primary insulin-receptor dysfunction and localizing the lesion to a proximal receptor→PI3K node ([PMID: 27766312](https://pubmed.ncbi.nlm.nih.gov/27766312/)). Diabetes typically becomes overt around puberty ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)). Management is supportive—insulin-sensitizing and glucose-lowering drugs (metformin, SGLT2 inhibitors), with growth hormone used cautiously. Notably, *PIK3R1* is a **dual-disorder gene**: loss-of-function C-terminal variants cause SHORT syndrome, while splice variants that hyperactivate p110δ cause the gain-of-function immunodeficiency **APDS2**, with occasional phenotypic overlap ([PMID: 32778990](https://pubmed.ncbi.nlm.nih.gov/32778990/)).

---

## Section 1 — Disease Information

**Overview.** SHORT syndrome is a rare, congenital, autosomal dominant multisystem disorder characterized by pre- and post-natal growth failure, a recognizable progeroid facial gestalt, partial lipodystrophy, anterior-segment eye dysgenesis (Rieger anomaly), delayed dental eruption, joint hyperextensibility, and a highly characteristic insulin-resistant diabetes that emerges around puberty. The SHORT acronym only partially captures the phenotype; systematic review has shown that **facial dysmorphism is actually the most consistent feature**, ahead of the eponymous ocular and dental signs ([PMID: 34212753](https://pubmed.ncbi.nlm.nih.gov/34212753/)).

**Key identifiers.**
| Resource | Identifier |
|---|---|
| OMIM | #269880 (SHORT syndrome) |
| Orphanet | ORPHA:3163 |
| MONDO | MONDO:0009159 |
| ICD-10 | Q87.1 |
| Gene (HGNC) | *PIK3R1*, HGNC:8979 |
| Gene (OMIM) | *171833 |

**Synonyms / alternative names.** SHORT syndrome; Short stature–hyperextensibility–ocular depression–Rieger anomaly–teething delay syndrome; Rieger anomaly–partial lipodystrophy syndrome; Aarskog-Ose-Pande syndrome; lipodystrophy–Rieger anomaly–diabetes syndrome.

**Evidence source.** Information is derived from **aggregated disease-level resources** (OMIM, Orphanet), **individual case reports and small case series**, and one **systematic review** of 19 individuals from 11 families ([PMID: 34212753](https://pubmed.ncbi.nlm.nih.gov/34212753/)). There is no large EHR-derived cohort; the total reported literature comprises on the order of tens of families.

---

## Section 2 — Etiology

**Primary cause — genetic.** SHORT syndrome is a **monogenic disorder** caused by heterozygous pathogenic variants in *PIK3R1*. It is not infectious or primarily environmental. Inheritance is **autosomal dominant**; both inherited (parent-to-child) and *de novo* mutations are reported, with several case reports documenting confirmed *de novo* origin (parents and siblings unaffected and mutation-negative) — e.g., [PMID: 33129256](https://pubmed.ncbi.nlm.nih.gov/33129256/), [PMID: 32602265](https://pubmed.ncbi.nlm.nih.gov/32602265/).

**Genetic risk factors.** The causal variants are the *PIK3R1* C-terminal cSH2/iSH2 mutations (see Section 4). The recurrent **c.1945C>T (p.Arg649Trp)** is the single largest contributor. No independent susceptibility loci or common modifier alleles have been established; because the disorder is highly penetrant and monogenic, the "risk factor" is essentially carriage of the pathogenic allele.

**Environmental risk factors.** None established as causal. **Age/puberty acts as a temporal modifier** of the metabolic phenotype—insulin-resistant diabetes appears around/after puberty rather than in early childhood ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)). Sex does not appear to strongly modify prevalence, though several prominent case reports are female.

**Protective factors.** No genetic or environmental protective variants are described. In mouse models, the mutation itself confers apparent "protection" from obesity and hepatic steatosis (a consequence of reduced lipogenesis), but this is a manifestation of the disease mechanism rather than a protective factor for the patient ([PMID: 29724723](https://pubmed.ncbi.nlm.nih.gov/29724723/)).

**Gene–environment interactions.** The principal documented interaction is **genotype × pubertal/hormonal milieu**: the diabetogenic insulin resistance is latent in childhood and unmasked around puberty. Growth hormone (an iatrogenic/therapeutic exposure) is diabetogenic and can aggravate the metabolic phenotype ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)).

---

## Section 3 — Phenotypes

SHORT syndrome is a multisystem disorder. Phenotype frequencies below draw on the systematic review of 19 individuals ([PMID: 34212753](https://pubmed.ncbi.nlm.nih.gov/34212753/)) and multiple case reports.

| Phenotype | Type | Onset | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Intrauterine growth restriction | Physical manifestation | Prenatal/congenital | Very common | HP:0001511 |
| Short stature / postnatal growth failure | Clinical sign | Congenital–childhood | Common | HP:0004322 |
| Facial dysmorphism (triangular face, frontal bossing) | Physical manifestation | Congenital | **Most consistent** | HP:0000271 / HP:0000268 |
| Deep-set eyes / ocular depression | Physical manifestation | Congenital | Common | HP:0000490 |
| Large, low-set ears | Physical manifestation | Congenital | Common | HP:0000369 / HP:0000368 |
| Micrognathia / mandibular retrognathia | Physical manifestation | Congenital | Common | HP:0000347 |
| Thin/hypoplastic alae nasi | Physical manifestation | Congenital | Common | HP:0000430 |
| Progeroid / aged appearance | Physical manifestation | Childhood | Common | HP:0005104 |
| Partial lipodystrophy (facial/limb lipoatrophy) | Physical manifestation | Childhood | Common | HP:0009125 |
| Insulin resistance | Laboratory abnormality | Childhood–puberty | Common (metabolic hallmark) | HP:0000855 |
| Insulin-resistant diabetes mellitus | Laboratory/clinical | ~Puberty onward | ~10/15 untreated ≥12 y | HP:0000831 / HP:0000857 |
| Acanthosis nigricans | Clinical sign | Childhood | Reported | HP:0000956 |
| Rieger anomaly / anterior-segment dysgenesis | Clinical sign | Congenital | Common (eponymous) | HP:0000554 / HP:0000539 |
| Glaucoma | Clinical sign | Childhood–adult | Reported | HP:0000501 |
| Delayed tooth eruption | Clinical sign | Childhood | Common (eponymous) | HP:0000684 |
| Joint hyperextensibility | Clinical sign | Congenital–childhood | Common (eponymous) | HP:0001382 |
| Inguinal hernia | Clinical sign | Childhood | Reported | HP:0000023 |
| Sensorineural hearing loss | Clinical sign | Variable | Reported | HP:0000407 |

**Characteristics.** Craniofacial features are congenital, stable, and the most penetrant. Metabolic features are **progressive and age-dependent**: insulin resistance is often subclinical in early childhood, then diabetes develops around puberty ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)). Severity is **variable** even within the recurrent hotspot genotype, indicating variable expressivity. Intelligence is typically normal.

**Quality-of-life impact.** No formal EQ-5D/SF-36 studies exist. Practically, QoL is affected by (i) chronic metabolic disease requiring lifelong glucose management, (ii) visual morbidity from glaucoma/anterior-segment disease (risk of vision loss), (iii) short stature and dysmorphism with psychosocial impact, and (iv) dental complications. Cognition and lifespan appear largely preserved.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *PIK3R1* (HGNC:8979; OMIM *171833), chromosome 5q13.1, encoding the **p85α regulatory subunit** of class IA PI3K.

**Pathogenic variants.** Most mutations cluster in the region encoding the **C-terminal SH2 (cSH2) / inter-SH2 (iSH2) substrate-recognition domain**. Documented variants:

| Variant (cDNA) | Protein | Type | Note |
|---|---|---|---|
| c.1945C>T | p.Arg649Trp | Missense | **Recurrent hotspot** — majority of cases (8/14 families in one series) |
| c.1929_1933delTGGCA | p.Asp643Aspfs*8 | Frameshift | Novel truncating variant |
| c.1960C>T | p.Gln654* | Nonsense | *De novo*; first Chinese case with thyroid disease |
| c.2008delT | — | Frameshift | Truncating |
| c.1615_1617del | in-frame del | Small deletion | Chinese case series |

**Classification (ACMG/AMP).** The recurrent c.1945C>T (p.Arg649Trp) and the reported truncating variants are classified **pathogenic/likely pathogenic** in ClinVar. Truncating and dominant-negative missense variants converge on the same C-terminal region.

**Allele frequency.** These are private/ultra-rare disease variants essentially **absent from gnomAD** control populations, consistent with severe monogenic disease.

**Origin.** **Germline** (constitutional). Both inherited and *de novo* germline events occur. No somatic contribution to SHORT syndrome.

**Functional consequence.** **Loss of function with a dominant-negative component.** The mutant p85α fails to relieve inhibition of the p110 catalytic subunit and fails to couple to receptor phosphotyrosines, reducing PI3K activation. Because p85α is a shared regulatory subunit, the mutant subunit dominantly interferes with signaling (heterozygous, autosomal dominant) — [PMID: 26974159](https://pubmed.ncbi.nlm.nih.gov/26974159/).

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes, epigenetic signatures, or large chromosomal rearrangements are established for SHORT syndrome. It is a single-nucleotide/small-indel monogenic disorder; chromosomal microarray is typically normal.

---

## Section 5 — Environmental Information

SHORT syndrome is a **genetic disorder with no established environmental etiology**. There are no causal toxins, radiation exposures, occupational factors, dietary triggers, or infectious agents. The only clinically relevant "environmental"/exogenous modifier is **growth hormone therapy**, which—being diabetogenic—can worsen the metabolic phenotype and is regarded with caution ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)). Pubertal hormonal changes act as an endogenous temporal modifier of diabetes onset.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous *PIK3R1* mutation** (most often c.1945C>T, p.Arg649Trp) in the C-terminal cSH2/iSH2 region **produces a defective p85α regulatory subunit**.
2. The mutant p85α **fails to relieve inhibition of the p110 catalytic subunit and fails to engage activated receptor phosphotyrosines** → *results in* reduced recruitment/activation of class IA PI3K at the insulin/IGF-1/growth-factor receptor complex.
3. Because p85α is heterozygously mutated and dominant-negative, **PI3K activation is reduced across insulin-responsive tissues** (liver, muscle, adipose) → *leads to* diminished generation of PIP₃ and blunted downstream **AKT (PKB) signaling** (demonstrated in the knock-in mouse: reduced capacity of insulin and other growth factors to activate PI3K in liver, muscle, and fat — [PMID: 26974159](https://pubmed.ncbi.nlm.nih.gov/26974159/)).
4. Reduced PI3K–AKT signaling **branches** into the disease phenotypes:
   - **Metabolic branch:** impaired insulin action → *systemic insulin resistance* → compensatory hyperinsulinemia → (around puberty) *insulin-resistant diabetes mellitus* ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)). Because the lesion is proximal (receptor→PI3K), the insulin resistance is **uncoupled from hepatic lipogenesis** → *no fatty liver, no dyslipidemia, preserved/high adiponectin* ([PMID: 27766312](https://pubmed.ncbi.nlm.nih.gov/27766312/)).
   - **Adipose branch:** impaired PI3K-dependent adipocyte development/maintenance → *partial lipodystrophy* → reduced lipid buffering, further aggravating insulin resistance (inferred).
   - **Growth branch:** reduced PI3K/IGF-1 signaling (possible IGF-1 resistance) → *IUGR and postnatal short stature* (inferred from clinical + IGF resistance data; [PMID: 36401775](https://pubmed.ncbi.nlm.nih.gov/36401775/)).
   - **Ocular/developmental branch:** reduced PI3K signaling during anterior-segment development → *iris hypoplasia and anterior-segment dysgenesis* → **Rieger anomaly** — a demonstrated developmental iris defect, independent of diabetes ([PMID: 28632845](https://pubmed.ncbi.nlm.nih.gov/28632845/)).
   - **Craniofacial/dental branch:** reduced PI3K signaling in craniofacial/dental development → *progeroid dysmorphism and delayed tooth eruption* (inferred).

### Molecular / cellular detail

- **Molecular pathway:** class IA **PI3K–AKT–mTOR** signaling downstream of insulin/IGF-1 and other growth-factor receptor tyrosine kinases (KEGG hsa04151 PI3K-Akt; KEGG hsa04910 insulin signaling). SHORT syndrome represents **haploinsufficient/dominant-negative attenuation** of this axis—the mirror image of gain-of-function PI3K activation.
- **Protein dysfunction:** p85α cSH2/iSH2 substrate-recognition domain defect → failure of the regulatory subunit to bind phosphotyrosine motifs and to properly regulate p110 (loss-of-function with dominant-negative behavior).
- **Metabolic changes:** decreased lipogenesis, increased energy expenditure, insulin resistance, and possible IGF-1 resistance ([PMID: 36401775](https://pubmed.ncbi.nlm.nih.gov/36401775/)).
- **Classification:** formally a **genetic (monogenic) insulin resistance syndrome** within the PI3K signaling axis, grouped with INSR (type A/Donohue/Rabson–Mendenhall) and AKT2/TBC1D4/PRKCE disorders ([PMID: 35110500](https://pubmed.ncbi.nlm.nih.gov/35110500/)).

### Suggested ontology terms
- **GO biological process:** phosphatidylinositol 3-kinase signaling (GO:0014065); insulin receptor signaling pathway (GO:0008286); regulation of glucose import (GO:0046324); positive regulation of cell growth (GO:0030307).
- **GO cellular component / molecular function:** phosphatidylinositol 3-kinase complex (GO:0005942); 1-phosphatidylinositol-3-kinase regulator activity (GO:0046935).
- **Cell types (CL):** adipocyte (CL:0000136); hepatocyte (CL:0000182); skeletal muscle cell (CL:0000188); iris pigment/stromal cells and neural-crest-derived anterior-segment cells.

---

## Section 7 — Anatomical Structures Affected

**Organ / system level.**
- **Endocrine/metabolic:** pancreas (islet dysfunction/insulin secretion defect in mouse), adipose tissue, liver, skeletal muscle — insulin target tissues (UBERON:0002107 liver; UBERON:0001013 adipose tissue; UBERON:0001134 skeletal muscle; UBERON:0000006 islet of Langerhans).
- **Eye:** anterior segment — iris (UBERON:0001769), cornea/angle structures; Rieger anomaly with goniosynechiae, prominent ring of Schwalbe, glaucoma, early cataract.
- **Craniofacial skeleton and teeth:** face, mandible, dental structures (delayed eruption).
- **Musculoskeletal:** joints (hyperextensibility); overall stature/growth.
- **Skin:** acanthosis nigricans (secondary to insulin resistance).

**Tissue/cell level.** Adipocytes (lipodystrophy), hepatocytes and myocytes (insulin resistance), pancreatic β-cells (insulin secretion), and neural-crest-derived anterior-segment cells (iris hypoplasia). The mouse model localizes the ocular defect specifically to a **decrease in iris thickness and width with increased pupil area/irregularity**, cornea/lens/retina otherwise normal ([PMID: 28632845](https://pubmed.ncbi.nlm.nih.gov/28632845/)).

**Subcellular level.** Signaling defect at the **plasma membrane / cytoplasmic receptor-signaling complex** (PI3K complex; GO:0005942); PIP₃ generation at the inner leaflet of the plasma membrane.

**Localization / lateralization.** Systemic and generally **bilateral/symmetric**; ocular involvement is bilateral.

---

## Section 8 — Temporal Development

- **Onset:** **Congenital.** IUGR is prenatal; dysmorphism, ocular, and dental features are present from birth/early childhood.
- **Progression:** Craniofacial features are stable. The **metabolic phenotype is progressive and age-dependent**: insulin resistance is often subclinical in early childhood, with insulin-resistant diabetes typically emerging **around puberty** — diabetes in 10/15 untreated patients aged ≥12 y versus none aged ≤10 y ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)).
- **Course:** Chronic, lifelong. No spontaneous remission of the underlying disorder; metabolic parameters can be improved with treatment.
- **Critical period / intervention window:** Peripubertal transition is the key window for metabolic surveillance and early intervention; anterior-segment/glaucoma monitoring is lifelong to preserve vision.

---

## Section 9 — Inheritance and Population

- **Epidemiology:** Ultra-rare. Prevalence is not precisely established; Orphanet lists it as <1/1,000,000, with only tens of families reported worldwide. No reliable incidence figure exists.
- **Inheritance:** **Autosomal dominant** ([PMID: 23980586](https://pubmed.ncbi.nlm.nih.gov/23980586/), [PMID: 24033310](https://pubmed.ncbi.nlm.nih.gov/24033310/)).
- **Penetrance:** High for the overall syndrome; **age-dependent penetrance** for the diabetes component (largely post-pubertal).
- **Expressivity:** **Variable**, even among carriers of the recurrent p.Arg649Trp allele.
- **De novo vs inherited:** Both occur; multiple confirmed *de novo* cases (parents/siblings unaffected and mutation-negative).
- **Anticipation / mosaicism / founder effects:** No genetic anticipation (not a repeat-expansion disorder). No established founder effect; the recurrence of c.1945C>T reflects a **mutational hotspot** rather than a founder haplotype. Germline mosaicism not specifically documented.
- **Consanguinity:** Not relevant (dominant disorder).
- **Population demographics:** Reported across multiple ethnicities (European, Chinese, Filipino, etc.); no strong ethnic predilection. Sex ratio not clearly skewed. Age distribution spans childhood to adulthood.

---

## Section 10 — Diagnostics

**Genetic testing (definitive).** Diagnosis is confirmed by identifying a heterozygous pathogenic *PIK3R1* variant. Recommended approaches:
- **Single-gene testing / targeted variant analysis** for *PIK3R1* (especially the c.1945C>T hotspot) when the phenotype is classic.
- **Whole-exome sequencing (WES)** is the most common route to diagnosis in the reported literature and is high-yield when the phenotype is atypical or overlaps with Silver–Russell syndrome ([PMID: 32546215](https://pubmed.ncbi.nlm.nih.gov/32546215/)).
- **Gene panels** for lipodystrophy/insulin-resistance/growth-failure that include *PIK3R1*.
- **Whole-genome sequencing (WGS)** is useful for splice/structural variants (relevant given the allelic APDS2 splice variants). Chromosomal microarray/karyotype are typically normal and not diagnostic.

**Clinical/laboratory tests.**
- **Metabolic:** fasting glucose, HbA1c, fasting insulin/C-peptide, OGTT with insulin — reveal severe insulin resistance and hyperinsulinemia; adiponectin is characteristically **preserved/high** ([PMID: 27766312](https://pubmed.ncbi.nlm.nih.gov/27766312/)). Lipid panel and liver imaging are characteristically **normal** (no dyslipidemia/steatosis), a distinguishing feature.
- **Ophthalmologic:** slit-lamp/gonioscopy and OCT identify Rieger anomaly, iris thinning, goniosynechiae, prominent ring of Schwalbe, cataract, and glaucoma ([PMID: 28632845](https://pubmed.ncbi.nlm.nih.gov/28632845/)).
- **Auxological/imaging:** growth charts documenting IUGR/short stature; dental radiographs for eruption delay.

**Clinical criteria / differential diagnosis.** No formal consensus criteria; diagnosis is based on the recognizable gestalt plus molecular confirmation. Key differentials:
- **Silver–Russell syndrome** (shared IUGR, triangular face, growth failure) — distinguished by 11p15 LOM/upd(7)mat and by SHORT’s lipodystrophy/insulin resistance ([PMID: 32546215](https://pubmed.ncbi.nlm.nih.gov/32546215/)).
- **Other congenital/partial lipodystrophies** (e.g., FPLD) — distinguished by the SHORT gestalt, Rieger anomaly, and the dyslipidemia-uncoupled insulin resistance.
- **APDS2** (allelic; immunodeficiency phenotype) — distinguished by recurrent sinopulmonary infection and hypogammaglobulinemia and by the splice-site GOF variant ([PMID: 32778990](https://pubmed.ncbi.nlm.nih.gov/32778990/)).

**Screening.** Cascade genetic testing of at-risk relatives once a familial variant is known. No population newborn screening.

---

## Section 11 — Outcome / Prognosis

- **Survival / life expectancy:** No evidence of substantially reduced lifespan; the disorder is compatible with adult life. There is no reported disease-specific mortality figure.
- **Morbidity:** Driven by (i) chronic insulin-resistant diabetes and its long-term complications, (ii) ophthalmologic morbidity (glaucoma → potential vision loss), and (iii) growth/dysmorphism-related psychosocial impact. Notably, two patients with >30 years of diabetes had **no diabetic retinopathy**, suggesting the ocular phenotype is developmental rather than microvascular ([PMID: 28632845](https://pubmed.ncbi.nlm.nih.gov/28632845/)).
- **Disease course:** Chronic, lifelong, non-remitting at the genetic level; metabolic control is achievable pharmacologically.
- **Prognostic factors:** Age/puberty (diabetes onset), adequacy of glycemic management, and intraocular pressure control (vision). Preserved adiponectin and absent dyslipidemia may confer relative protection from atherogenic complications compared with obesity-related insulin resistance.
- **Data gaps:** Long-term natural-history and outcome data are sparse ([PMID: 36401775](https://pubmed.ncbi.nlm.nih.gov/36401775/)).

---

## Section 12 — Treatment

**No formal treatment guidelines exist**; management is supportive and organ-directed, drawn from case reports.

**Pharmacotherapy for insulin resistance / diabetes (NCIT: metformin C61793; SGLT2 inhibitors; thiazolidinediones):**
- **Metformin** (± **pioglitazone**) improved insulin resistance and hyperinsulinemia ([PMID: 33742773](https://pubmed.ncbi.nlm.nih.gov/33742773/)); metformin effective in early treatment of two Chinese girls ([PMID: 32602265](https://pubmed.ncbi.nlm.nih.gov/32602265/)).
- **SGLT2 inhibitor (canagliflozin)** ameliorated overt diurnal hyperglycemia and mild nocturnal hypoglycemia ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)).
- **Multi-agent oral therapy** (metformin + voglibose/DPP-4/SGLT2 combinations) improved glucose and insulin resistance over months ([PMID: 39735640](https://pubmed.ncbi.nlm.nih.gov/39735640/), [PMID: 41459015](https://pubmed.ncbi.nlm.nih.gov/41459015/)).
- **Lifestyle intervention** (diet, exercise) is a consistent adjunct.

**Growth hormone — relatively contraindicated.** GH gives a poor statural response and, being diabetogenic, can worsen glucose metabolism; it has been regarded as contraindicated. However, Masunaga et al. concluded that pubertal development/age—not GH per se—drives diabetes onset, nuancing this caution ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)).

**Ophthalmologic / surgical:** glaucoma management (IOP-lowering therapy, surgery as needed), cataract surgery, and anterior-segment care. Dental management for eruption delay/anomalies.

**Advanced/experimental therapeutics:** No approved gene, cell, RNA-based, or targeted molecular therapy exists for SHORT syndrome. Because the defect is loss-of-PI3K-signaling, PI3K/AKT-pathway inhibitors (used in the opposite, gain-of-function conditions) are inappropriate; conceptually, pathway-restorative strategies would be required. No registered SHORT-syndrome-specific interventional trials identified.

**Pharmacogenomics / personalized approach:** Genotype-guided care is essentially "diagnosis-guided"—confirming *PIK3R1* etiology reframes the insulin resistance as a proximal signaling defect, supporting insulin-sensitizer-based strategies and cautious GH use.

---

## Section 13 — Prevention

SHORT syndrome cannot be prevented (congenital monogenic disorder). Preventive strategy focuses on **secondary and tertiary prevention**:
- **Genetic counseling:** autosomal dominant 50% transmission risk; discussion of *de novo* occurrence and variable expressivity. **Prenatal / preimplantation genetic testing** is feasible when the familial variant is known.
- **Cascade genetic screening** of at-risk relatives.
- **Secondary prevention (early detection):** peripubertal metabolic surveillance (glucose/insulin/HbA1c) to detect and treat diabetes early; regular ophthalmologic monitoring (IOP, gonioscopy) to detect glaucoma before vision loss.
- **Tertiary prevention:** optimize glycemic control to limit diabetic complications; manage IOP to preserve vision; dental follow-up. **Avoid/limit diabetogenic exposures** (e.g., cautious GH use).
- No immunization or public-health/environmental interventions are applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** No naturally occurring SHORT syndrome is described in companion animals or wildlife; OMIA has no established entry. SHORT syndrome is essentially a human-defined disorder studied via engineered animal models.
- **Orthologous gene:** *Pik3r1* is highly conserved (mouse *Pik3r1*, NCBI Gene ID 18708; human *PIK3R1*, NCBI Gene ID 5295). The Arg649 residue and the C-terminal SH2/iSH2 region are conserved between human and mouse, enabling faithful knock-in modeling.
- **Comparative biology:** The conserved PI3K–AKT insulin-signaling axis means the mouse model reproduces core human features, supporting strong evolutionary conservation of the disease mechanism.
- **Zoonotic potential:** Not applicable (non-infectious genetic disorder).

---

## Section 15 — Model Organisms

**Mouse models (mammalian) are the principal system.**

| Model | Genotype | Key phenotype | Reference |
|---|---|---|---|
| *Pik3r1* Arg649Trp knock-in | Heterozygous KI (homolog of human hotspot) | Reduced body weight/length, partial lipodystrophy, systemic insulin resistance; reduced PI3K activation in liver/muscle/fat; defective insulin secretion; impaired GLP-1 action on islets | [PMID: 26974159](https://pubmed.ncbi.nlm.nih.gov/26974159/) |
| Dominant-negative human PI3K (R649W) mouse | Knock-in | Protected from obesity and hepatic steatosis but not diabetes | [PMID: 29724723](https://pubmed.ncbi.nlm.nih.gov/29724723/) |
| R649W knock-in (ocular) | Knock-in | Decreased iris thickness/width, increased pupil area/irregularity; cornea/lens/retina normal — recapitulates Rieger anomaly | [PMID: 28632845](https://pubmed.ncbi.nlm.nih.gov/28632845/) |

**Phenotype recapitulation.** The knock-in mice reproduce the core human phenotype—growth restriction, partial lipodystrophy, insulin resistance, and (independently) the iris/anterior-segment defect—and provide direct mechanistic proof that **reduced PI3K activation** underlies the disease.

**Model limitations.** Some human features (full craniofacial gestalt, dental eruption delay, joint hyperextensibility) are not comprehensively modeled; the obesity-protection phenotype reflects species/dietary context. No invertebrate, zebrafish, or organoid/iPSC SHORT-syndrome models are prominent in the reviewed literature.

**Resources:** MGI (*Pik3r1*), IMPC/KOMP for engineered alleles.

---

## Key Findings (with statistical evidence)

### F1. *PIK3R1* loss-of-function/dominant-negative mutations cause SHORT syndrome
Three concurrent 2013 exome studies (Thauvin-Robinet, Chudasama, Dyment; AJHG 93:141–166) established heterozygous *PIK3R1* mutations as causal, with the recurrent hotspot **c.1945C>T (p.Arg649Trp)** in 8 of 14 families and additional frameshift/nonsense variants clustering in the C-terminal cSH2/iSH2 domain. *"We report the finding of a novel mutation in PIK3R1 (c.1929_1933delTGGCA; p.Asp643Aspfs\*8), as well as a recurrent mutation c.1945C > T (p.Arg649Trp) in this gene"* ([PMID: 24886349](https://pubmed.ncbi.nlm.nih.gov/24886349/)); *"Eight of these families had a recurrent missense mutation (c.1945C>T; p.Arg649Trp)"* ([PMID: 23980586](https://pubmed.ncbi.nlm.nih.gov/23980586/)); [PMID: 24033310](https://pubmed.ncbi.nlm.nih.gov/24033310/).

### F2. A knock-in mouse confirms reduced PI3K activation as the mechanism
*"mutant mice exhibited a reduction in body weight and length, partial lipodystrophy, and systemic insulin resistance... associated with a reduced capacity of insulin and other growth factors to activate PI3K in liver, muscle, and fat"* ([PMID: 26974159](https://pubmed.ncbi.nlm.nih.gov/26974159/)). A second model was *"Protected From Obesity and Hepatic Steatosis but Not Diabetes"* ([PMID: 29724723](https://pubmed.ncbi.nlm.nih.gov/29724723/)).

### F3. Craniofacial dysmorphism is the most consistent feature; diabetes is puberty-onset
Systematic review of 19 individuals: *"Facial dysmorphism including ocular depression, triangular shaped face, frontal bossing, large low-set ears, and micrognathia were the most consistent features followed by lipodystrophy, insulin resistance, and intrauterine growth restriction"* ([PMID: 34212753](https://pubmed.ncbi.nlm.nih.gov/34212753/)). Diabetes is age-dependent: *"IRDM in 10 of 15 GH-untreated patients aged ≥12 years but in none of three GH-treated and six GH-untreated patients aged ≤10 years"* ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)).

### F4. Management: insulin sensitizers/SGLT2 inhibitors; GH relatively contraindicated
Metformin ± pioglitazone reduced insulin resistance ([PMID: 33742773](https://pubmed.ncbi.nlm.nih.gov/33742773/)); canagliflozin *"ameliorated overt diurnal hyperglycemia and mild nocturnal hypoglycemia"* ([PMID: 32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/)).

### F5. Rieger anomaly is a PI3K-dependent developmental iris defect
*"OCT images of the knock-in mouse eyes revealed a significant decrease in thickness and width of the iris... Both human subjects had Rieger anomaly with similar defects including thin irides and irregular pupils, as well as a prominent ring of Schwalbe, goniosynechiae, early cataract formation, and glaucoma"* ([PMID: 28632845](https://pubmed.ncbi.nlm.nih.gov/28632845/)).

### F6. *PIK3R1* is a dual-disorder gene (SHORT LOF vs APDS2 GOF)
*"APDS type 2 is caused by mutations in the PIK3R1 gene affecting the p85α regulatory subunit... The primary causes of SHORT syndrome are heterozygous loss-of-function mutations in the PIK3R1 gene."* A splice variant *"c.1425 + 1G > C... previously associated with APDS2"* was found in a patient with SHORT features ([PMID: 32778990](https://pubmed.ncbi.nlm.nih.gov/32778990/)); overlap also reported by [PMID: 35789397](https://pubmed.ncbi.nlm.nih.gov/35789397/).

### F7. Insulin resistance uncoupled from dyslipidemia (distinctive signature)
*"Insulin resistance due to insulin receptor (INSR) dysfunction is associated with none of these, but when due to dysfunction of the downstream kinase AKT2 phenocopies obesity-related insulin resistance. We report 5 patients with SHORT syndrome and C-terminal mutations"* — placing the p85α defect at a proximal receptor→PI3K node, resembling INSR dysfunction (no fatty liver, no dyslipidemia, high adiponectin) ([PMID: 27766312](https://pubmed.ncbi.nlm.nih.gov/27766312/)).

### F8. Formally classified as a genetic insulin resistance syndrome
The Japan Diabetes Society working group classifies *"SHORT syndrome caused by abnormalities of PIK3R1... conditions caused by abnormalities of AKT2, TBC1D4, or PRKCE"* within genetic insulin resistance syndromes ([PMID: 35110500](https://pubmed.ncbi.nlm.nih.gov/35110500/)).

---

## Mechanistic Model / Interpretation

```
   PIK3R1 mutation (C-terminal cSH2/iSH2; e.g. p.Arg649Trp)
                    │
        defective p85α regulatory subunit
                    │  (fails to relieve p110 inhibition;
                    │   fails to engage receptor phosphotyrosines)
                    ▼
        ↓ class IA PI3K activation  →  ↓ PIP3  →  ↓ AKT signaling
                    │
   ┌────────────┬───┴─────────┬──────────────┬───────────────┐
   ▼            ▼             ▼              ▼               ▼
 Metabolic    Adipose      Growth        Ocular          Craniofacial/
 branch       branch       branch        (development)   dental branch
   │            │             │              │               │
 insulin      partial      IUGR /         iris          progeroid
 resistance   lipodys-     short          hypoplasia →  dysmorphism;
   │          trophy       stature        Rieger        delayed
 (proximal →                (± IGF-1      anomaly       tooth eruption
 no dyslipid-  ─────────►   resistance)   (NOT diabetic
 emia/NAFLD;               ◄──────────    retinopathy)
 high adipo-   aggravates IR
 nectin)
   │
 peri-pubertal → insulin-resistant diabetes mellitus
```

The model’s central insight is that a **single proximal signaling lesion** (attenuated PI3K activation) produces a pleiotropic phenotype by acting in multiple PI3K-dependent developmental and metabolic programs. The **proximal location** of the defect (receptor→PI3K, upstream of the branch controlling hepatic lipogenesis) explains the syndrome’s most discriminating laboratory signature—**severe insulin resistance without dyslipidemia or fatty liver**—which mirrors INSR dysfunction rather than downstream AKT2 dysfunction. This positions SHORT syndrome as a "clean" human experiment of nature isolating proximal PI3K signaling, and it is the **loss-of-function mirror image** of APDS2/gain-of-function PI3K disease at the same gene.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [24886349](https://pubmed.ncbi.nlm.nih.gov/24886349/) | Exome identifies novel *PIK3R1* mutation | Hotspot + frameshift variants; causality |
| [23980586](https://pubmed.ncbi.nlm.nih.gov/23980586/) | *PIK3R1* mutations in SHORT | AD inheritance; Arg649Trp in 8/14 families |
| [24033310](https://pubmed.ncbi.nlm.nih.gov/24033310/) | Autosomal dominant *PIK3R1* cause | Landmark 2013 discovery |
| [26974159](https://pubmed.ncbi.nlm.nih.gov/26974159/) | PI3K mutation → insulin/GF resistance in vivo | Knock-in mouse; mechanism |
| [29724723](https://pubmed.ncbi.nlm.nih.gov/29724723/) | Dominant-negative PI3K mouse | Protected from obesity/steatosis, not diabetes |
| [34212753](https://pubmed.ncbi.nlm.nih.gov/34212753/) | Systematic medical/dental phenotype | Frequency ranking; facial dysmorphism most consistent |
| [32879144](https://pubmed.ncbi.nlm.nih.gov/32879144/) | IRDM in SHORT syndrome | Pubertal onset of diabetes; SGLT2i; GH caution |
| [28632845](https://pubmed.ncbi.nlm.nih.gov/28632845/) | Iris malformation/anterior-segment dysgenesis | Rieger anomaly as developmental iris defect |
| [32778990](https://pubmed.ncbi.nlm.nih.gov/32778990/) | APDS2 + SHORT in a teenager | Dual-disorder gene; phenotypic overlap |
| [27766312](https://pubmed.ncbi.nlm.nih.gov/27766312/) | IR uncoupled from dyslipidemia | Distinctive proximal metabolic signature |
| [35110500](https://pubmed.ncbi.nlm.nih.gov/35110500/) | New IR-syndrome classification | Formal classification of SHORT syndrome |
| [33742773](https://pubmed.ncbi.nlm.nih.gov/33742773/) | Novel variant, 6-mo follow-up | Metformin/pioglitazone efficacy |
| [32602265](https://pubmed.ncbi.nlm.nih.gov/32602265/) | Two Chinese girls | Metformin early efficacy; de novo variants |
| [33129256](https://pubmed.ncbi.nlm.nih.gov/33129256/) | Chinese female + thyroid disease | Novel p.Gln654* nonsense; expanding spectrum |
| [36401775](https://pubmed.ncbi.nlm.nih.gov/36401775/) | Pathogenesis/clinical-spectrum update | Decreased lipogenesis, energy expenditure, IGF1 resistance |
| [32546215](https://pubmed.ncbi.nlm.nih.gov/32546215/) | SRS multigene analysis | SHORT syndrome as SRS differential |
| [39735640](https://pubmed.ncbi.nlm.nih.gov/39735640/) | Atypical diabetes in SHORT | Multi-agent oral therapy |
| [35789397](https://pubmed.ncbi.nlm.nih.gov/35789397/) | APDS2 with SHORT features | Overlap; novel mutation |

Evidence-type mix: **human clinical** (case reports, series, systematic review), **model organism** (knock-in mice), and **in vitro/mechanistic** (PI3K activation assays). Most clinical evidence is Level IV (case reports/series); the mechanistic conclusions are strengthened by convergent mouse-model data.

---

## Limitations and Knowledge Gaps

1. **Small evidence base:** Only tens of families reported; no large cohorts, no natural-history registry, and no formal QoL (EQ-5D/SF-36) or long-term outcome/mortality data.
2. **No treatment guidelines:** Therapy is extrapolated from individual case reports; comparative efficacy of metformin vs SGLT2 inhibitors vs thiazolidinediones is untested in trials.
3. **Genotype–phenotype correlation incomplete:** Variable expressivity even within the p.Arg649Trp genotype is unexplained; modifier genes are unidentified.
4. **Mechanistic gaps:** Precise contributions of PI3K attenuation to craniofacial and dental phenotypes are inferred, not experimentally demonstrated; the degree of IGF-1 resistance is not fully quantified.
5. **Model gaps:** No non-mammalian, organoid, or iPSC models; some human features not recapitulated in mice.
6. **APDS2 overlap:** The mechanistic basis by which certain *PIK3R1* variants produce both loss- and gain-of-function features requires further study.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for SHORT syndrome to define prevalence, natural history, long-term outcomes, and standardized QoL measures.
2. **Prospective metabolic trial** comparing insulin-sensitizing regimens (metformin, SGLT2 inhibitors, TZDs) with peripubertal surveillance protocols to build an evidence-based treatment algorithm.
3. **Deep phenotype–genotype study** across all reported *PIK3R1* variants (missense vs truncating vs splice) to map variant class to LOF/GOF behavior and clinical severity, and to search for modifier loci.
4. **Mechanistic dissection** of craniofacial/dental and IGF-1-resistance branches using conditional/tissue-specific *Pik3r1* knock-in mice and patient iPSC-derived tissues (adipocytes, β-cells, anterior-segment/neural-crest models).
5. **Pathway-restorative therapeutic exploration:** evaluate whether partial, tissue-selective potentiation of PI3K/AKT signaling can safely correct the metabolic phenotype without recapitulating APDS2-like overactivation.
6. **Cross-screening protocol:** systematically test SHORT-syndrome patients for immunologic features (and vice-versa for APDS2) given the shared gene, to detect overlap cases early.

---

*Report compiled from an autonomous, literature-grounded investigation (5 iterations, 8 confirmed findings, 22 papers reviewed). All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](SHORT_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SHORT_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009159` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Ehlers-Danlos syndrome, cardiac valvular type**
- `HP:0001511` (1 mention) - the report calls it "Very common"; HP calls it **Intrauterine growth retardation**
- `HP:0004322` (1 mention) - the report calls it "Common"; HP calls it **Short stature**
- `HP:0000490` (1 mention) - the report calls it "Common"; HP calls it **Deeply set eye**
- `HP:0000347` (1 mention) - the report calls it "Common"; HP calls it **Micrognathia**
- `HP:0000430` (1 mention) - the report calls it "Common"; HP calls it **Underdeveloped nasal alae**
- `HP:0005104` (1 mention) - the report calls it "Common"; HP calls it **Hypoplastic nasal septum**
- `HP:0009125` (1 mention) - the report calls it "Common"; HP calls it **Lipodystrophy**
- `HP:0000855` (1 mention) - the report calls it "Common (metabolic hallmark)"; HP calls it **Insulin resistance**
- `HP:0000684` (1 mention) - the report calls it "Common (eponymous)"; HP calls it **Delayed eruption of teeth**
- `HP:0001382` (1 mention) - the report calls it "Common (eponymous)"; HP calls it **Joint hypermobility**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0000368` (obsolete Low-set, posteriorly rotated ears) (1 mention) - replaced by `HP:0000358`
- `GO:0014065` (obsolete phosphatidylinositol 3-kinase signaling) (1 mention) - replaced by `GO:0043491`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0014065` (1 mention) - the report calls it "GO biological process:** phosphatidylinositol 3-kinase signaling"; GO calls it **obsolete phosphatidylinositol 3-kinase signaling**
- `UBERON:0001769` (1 mention) - the report calls it "Eye:** anterior segment — iris"; UBERON calls it **iris**, and lists "anterior uvea" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
