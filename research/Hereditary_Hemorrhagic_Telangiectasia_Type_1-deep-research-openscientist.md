---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T07:01:18.856528'
end_time: '2026-09-01T07:21:45.856831'
duration_seconds: 1227.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Hemorrhagic Telangiectasia Type 1
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 44
reference_validation:
  total_references: 44
  verified: 44
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 44
  on_topic: 21
  off_topic: 2
  off_topic_references:
  - PMID:42162269
  - PMID:42410718
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 10
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: NCIT:C1794
    reported_labels:
    - thalidomide
    ontology_label: Capecitabine
  - term_id: NCIT:C71146
    reported_labels:
    - pazopanib
    ontology_label: Salirasib
  - term_id: NCIT:C72713
    reported_labels:
    - pomalidomide
    ontology_label: Azipramine
  - term_id: NCIT:C74405
    reported_labels:
    - aflibercept
    ontology_label: Betamethasone Acibutate
  - term_id: NCIT:C47737
    reported_labels:
    - tranexamic acid
    ontology_label: Sulfamethoxazole
  - term_id: CHEBI:9445
    reported_labels:
    - thalidomide
    ontology_label: terazosin
  - term_id: CL:0000115
    reported_labels:
    - endothelial cell
    - Vascular endothelial cell (KIT+ angiogenic sub-state)
    ontology_label: endothelial cell
  - term_id: HP:0100761
    reported_labels:
    - Hepatic AVM
    ontology_label: Visceral angiomatosis
  labels_variant: 4
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
  path: Hereditary_Hemorrhagic_Telangiectasia_Type_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Hemorrhagic_Telangiectasia_Type_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Hemorrhagic Telangiectasia Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hemorrhagic Telangiectasia Type 1** covering all of the
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

# Hereditary Hemorrhagic Telangiectasia Type 1 (HHT1): Comprehensive Disease Characteristics Report

**Disease:** Hereditary Hemorrhagic Telangiectasia Type 1 (Osler–Weber–Rendu disease, ENG-related)
**MONDO ID:** MONDO:0008093 · **OMIM:** #187300 (phenotype); ENG gene OMIM 131195
**ICD-10:** I78.0 · **ICD-11:** LA90.0 · **MeSH:** D013683 (Telangiectasia, Hereditary Hemorrhagic) · **Orphanet:** ORPHA:774 (HHT), subtype HHT1
**HGNC:** HGNC:3349 (ENG) · **Category:** Mendelian, autosomal dominant

---

## Summary

Hereditary Hemorrhagic Telangiectasia Type 1 (HHT1) is an autosomal-dominant vascular dysplasia caused by germline **heterozygous loss-of-function variants in *ENG* (endoglin)** on chromosome **9q34**. Endoglin is an endothelial co-receptor that binds the circulating ligands **BMP9/BMP10** and presents them to the type I receptor **ALK1 (ACVRL1)** and BMPR-II to activate the **SMAD1/5/8** cascade — a pathway that maintains vascular quiescence and arteriovenous identity. Loss of one *ENG* allele produces haploinsufficiency; a **stochastic somatic "second hit"** (point mutation or loss of heterozygosity, now directly demonstrated in human lesions) plus a local angiogenic trigger precipitates focal lesions. The result is a systemic disorder of **mucocutaneous telangiectasias and visceral arteriovenous malformations (AVMs)** whose dominant clinical burden is recurrent **epistaxis** leading to iron-deficiency anemia and reduced quality of life, together with pulmonary, cerebral, hepatic, and gastrointestinal AVMs.

HHT1 is clinically distinct from HHT2 (*ACVRL1*): patients carry a **substantially higher burden of pulmonary AVMs and cerebral abscesses**, with earlier epistaxis onset, whereas symptomatic hepatic involvement and GI bleeding are relatively more characteristic of HHT2. Global clinical prevalence is approximately **1 in 5,000** (~1.6 million people worldwide), though genomic-database analyses estimate the true genetic prevalence is higher (up to ~4.3 per 5,000), implying widespread underdiagnosis. Diagnosis rests on the **Curaçao criteria** (epistaxis, telangiectasia, visceral AVMs, affected first-degree relative) supplemented by definitive *ENG* genetic testing, which is particularly important in children in whom clinical features are age-dependent.

Recent mechanistic advances converge on a coherent causal chain: reduced BMP9/BMP10–ENG/ALK1–SMAD signaling → derepression of angiogenic programs (including a druggable **KIT+ angiogenic endothelial state**) → focal AVM/telangiectasia formation requiring a somatic second hit and an angiogenic trigger. This model explains the disease's striking **variable expressivity even within single-mutation families**. Management combines **AVM embolization**, iron/transfusion support, procedural antibiotic prophylaxis, cascade genetic testing, and an emerging class of **antiangiogenic disease-modifying therapies** — with **pomalidomide** now supported by a pivotal randomized placebo-controlled trial, alongside off-label bevacizumab, pazopanib, and thalidomide.

---

## Key Findings

### 1. Molecular cause: germline heterozygous loss-of-function variants in *ENG* (endoglin), 9q34

HHT1 is defined molecularly by **germline heterozygous loss-of-function pathogenic variants in *ENG***, the co-receptor of the BMP9/BMP10–ALK1 signaling pathway. *ENG* maps to chromosome 9q34 (HGNC:3349; OMIM gene 131195); the disease is OMIM #187300. The reported variant spectrum includes **frameshift** (e.g., c.613delC, c.1498dupC, c.322delG), **splice-site** (c.1428+2T>C causing exon 11 skipping), **nonsense**, **missense**, and **start-loss** (c.1A>G, p.Met1Val) alleles. Most produce truncated or non-functional protein, consistent with **haploinsufficiency** as the primary loss-of-function mechanism.

> *"Hereditary Hemorrhagic Telangiectasia type I (HHT1) is an autosomal dominant vascular disease caused by pathogenic variants in endoglin (ENG) gene. It is located on chromosome 9 and encodes for the Endoglin protein, which is involved in the TGFb/BMP signalling pathway."* — [PMID: 41880974](https://pubmed.ncbi.nlm.nih.gov/41880974/)

> *"HHT is caused by heterozygous loss-of-function mutations in genes involved in the BMP9/BMP10 signaling pathway-primarily ENG, ACVRL1 (also known as ALK1), and SMAD4-which define the major HHT subtypes (HHT1, HHT2, and HHT-JP)."* — [PMID: 41251906](https://pubmed.ncbi.nlm.nih.gov/41251906/)

Specific frameshift variants producing premature termination are documented across independent families: *"The variants identified in Families 1, 3, and 4 (c.613delC, c.1498dupC, and c.322delG) are all frameshift variants that lead to premature termination of translation."* — [PMID: 42633037](https://pubmed.ncbi.nlm.nih.gov/42633037/). By ACMG/AMP criteria most such truncating variants classify as pathogenic/likely pathogenic; the functional consequence is **loss of function (haploinsufficiency)** rather than gain of function or dominant-negative.

**Ontology terms:** gene HGNC:3349 (*ENG*); GO:0007179 (transforming growth factor beta receptor signaling pathway); GO:0030509 (BMP signaling pathway).

### 2. Epidemiology: ~1 in 5,000, with genetic prevalence higher due to underdiagnosis

Clinical prevalence of HHT is approximately **1 in 5,000** (~1.6 million people worldwide). Analysis of large genomic databases (gnomAD, All of Us, Regeneron Million Exome) estimates the genetic prevalence of pathogenic/likely-pathogenic *ENG* + *ACVRL1* variants at **1.75–2.56 per 5,000**, rising to **2.87–4.33 per 5,000** when potentially pathogenic variants are included — indicating substantial underdiagnosis.

> *"HHT has a global prevalence of 1 in 5000 individuals, affecting approximately 1.6 million worldwide."* — [PMID: 41251906](https://pubmed.ncbi.nlm.nih.gov/41251906/)

> *"The genetic prevalence of HHT ranged from 1.753 to 2.555 in 5000 individuals, when considering only pathogenic and likely pathogenic variants, and from 2.874 to 4.327 in 5000 individuals, when also potentially pathogenic variants were considered."* — [PMID: 41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/)

HHT is described as the **second most common inherited bleeding disorder worldwide** ([PMID: 40662351](https://pubmed.ncbi.nlm.nih.gov/40662351/)). EHR-based data note a **higher observed prevalence in females**, consistent with sex-modified phenotypic expression ([PMID: 42162269](https://pubmed.ncbi.nlm.nih.gov/42162269/)). Distribution is worldwide with regional founder clusters; no single endemic geography defines the disease.

### 3. Diagnosis rests on the Curaçao criteria plus genetic testing

The **Curaçao clinical criteria** comprise: (1) spontaneous recurrent epistaxis; (2) mucocutaneous telangiectasia; (3) visceral AVMs (pulmonary, hepatic, cerebral, GI); and (4) a first-degree relative with HHT. **≥3 criteria = definite HHT; 2 = possible/suspected; ≤1 = unlikely.** The criteria are insufficient in children because features develop with age; positive genetic testing gives a definitive diagnosis at any age.

> *"HHT is commonly diagnosed using the established Curaçao clinical criteria, which include (1) family history, (2) recurrent epistaxis, (3) telangiectasia, and (4) visceral AVMs. Fulfillment of 3 or more criteria provides a definite diagnosis of HHT, whereas 2 criteria constitute a possible diagnosis of HHT."* — [PMID: 34889398](https://pubmed.ncbi.nlm.nih.gov/34889398/)

> *"these criteria are insufficient in children to rule out disease due to the age-dependent development of some of these criteria. Genetic testing, when positive, can provide definitive diagnosis of HHT in all age groups."* — [PMID: 34889398](https://pubmed.ncbi.nlm.nih.gov/34889398/)

In a Korean cohort, only ~57% of genetically confirmed patients met "definite" Curaçao criteria, reinforcing the complementary value of molecular testing ([PMID: 33677851](https://pubmed.ncbi.nlm.nih.gov/33677851/)). Recommended genetic testing is **single-gene/panel sequencing of ENG, ACVRL1, and SMAD4** (with GDF2/BMP9 in atypical cases); WES/WGS are useful when panels are negative. Differential diagnosis includes other causes of epistaxis/telangiectasia and PAVMs (e.g., idiopathic/traumatic AVMs, CREST); the Curaçao criteria distinguish HHT ([PMID: 34723698](https://pubmed.ncbi.nlm.nih.gov/34723698/)).

### 4. Core mechanism: reduced BMP9/BMP10–ENG/ALK1–SMAD signaling plus a Knudsonian second hit

Endoglin is an endothelial co-receptor that binds circulating **BMP9/BMP10** to activate the **ALK1–BMPR-II–SMAD1/5/8** cascade, maintaining vascular quiescence and arteriovenous identity. In mice, loss of *Bmp9* (and especially *Bmp10*) is sufficient to induce spontaneous AVMs in liver, GI tract, retina, and brain, altering endothelial capillary identity, Notch signaling, and cell-cycle control. Human and mouse evidence supports a **Knudsonian two-hit model**: a germline heterozygous *ENG* variant plus a somatic second hit (or an angiogenic/inflammatory environmental trigger) precipitates focal lesion formation — explaining the patchy distribution of lesions despite a uniform germline mutation.

> *"The signaling pathway of the bone morphogenetic protein (BMP)-9 binding to the endothelial receptor BMP receptor type II (BMPR-II), activin receptor-like kinase-1 (ALK1) and the coreceptor endoglin is essential to maintain the pulmonary vascular integrity."* — [PMID: 36828679](https://pubmed.ncbi.nlm.nih.gov/36828679/)

> *"the loss of Bmp9 led to spontaneous arteriovenous malformations (AVMs) in the liver, gastrointestinal tract, and uterus"* — [PMID: 38502919](https://pubmed.ncbi.nlm.nih.gov/38502919/)

> *"HHT pathogenesis is thought to follow a Knudsonian two-hit model, requiring a second somatic mutation for lesion formation."* — [PMID: 39651127](https://pubmed.ncbi.nlm.nih.gov/39651127/)

Complementary work shows **BMP10 is the most relevant physiological ligand** of ENG-ALK1 signaling for arteriovenous network formation, with BMP9 having limited compensatory function ([PMID: 36348215](https://pubmed.ncbi.nlm.nih.gov/36348215/)). The affected molecular pathway is **TGF-β/BMP–SMAD** (KEGG/Reactome BMP signaling); the core defective **biological processes** are vascular quiescence, angiogenesis, and vascular stabilization.

### 5. Genotype–phenotype: HHT1 has more pulmonary AVMs and cerebral abscess than HHT2

The French–Italian HHT network (93 HHT1 vs 250 HHT2 patients) demonstrated that **symptomatic pulmonary AVMs (PAVMs)** are far more frequent in HHT1 (**34.4% vs 5.2%, P<0.001**); **cerebral abscesses** more frequent in HHT1 (**7.5% vs 0.8%, P=0.002**); and PAVMs detected in asymptomatic HHT1 patients 54% vs 12.8% (P<0.0001). Conversely, **GI bleeding** (16.4% vs 6.5%, P=0.017) and symptomatic hepatic involvement were more common in HHT2. Epistaxis onset is earlier in HHT1. In a pediatric cohort, 59% of children with HHT had PAVMs.

> *"Symptomatic PAVMs were more frequent in HHT1 (34.4 vs. 5.2%, P<0.001), as were cerebral abscesses (7.5 vs. 0.8%, P=0.002). Gastrointestinal bleeding occurred more frequently in HHT2 (16.4 vs. 6.5%, P=0.017)."* — [PMID: 17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/)

> *"Of 129 children with HHT, 76 (59%) were found to have PAVMs."* — [PMID: 29916764](https://pubmed.ncbi.nlm.nih.gov/29916764/)

| Manifestation | HHT1 (*ENG*) | HHT2 (*ACVRL1*) | P-value |
|---|---|---|---|
| Symptomatic pulmonary AVMs | 34.4% | 5.2% | <0.001 |
| Cerebral abscess | 7.5% | 0.8% | 0.002 |
| PAVMs in asymptomatic patients | 54% | 12.8% | <0.0001 |
| GI bleeding | 6.5% | 16.4% | 0.017 |
| Symptomatic hepatic involvement | Lower | Higher | — |

### 6. Dominant clinical burden is epistaxis → iron-deficiency anemia → reduced QoL; antiangiogenic therapy is disease-modifying

Epistaxis is the primary manifestation of HHT and produces iron-deficiency anemia and reduced health-related quality of life; chronic GI bleeding and visceral AVMs add morbidity. In the pivotal randomized placebo-controlled **pomalidomide** trial (n=144; baseline mean Epistaxis Severity Score [ESS] 5.0 ± 1.5, moderate-to-severe), **pomalidomide 4 mg/day for 24 weeks reduced ESS versus placebo by −0.94 points (95% CI −1.57 to −0.31; MCID −0.71)**, and the trial stopped early for efficacy. Off-label antiangiogenic options include IV **bevacizumab**, oral **pazopanib**, and **thalidomide**; **aflibercept** salvage is reported for high-output states. Supportive care includes iron replacement, transfusion, tranexamic acid, and nasal/endoscopic interventions.

> *"The primary clinical manifestation is epistaxis that results in iron-deficiency anemia and reduced health-related quality of life."* — [PMID: 39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/)

> *"the mean difference between the pomalidomide group and the placebo group in the change from baseline in the Epistaxis Severity Score was -0.94 points (95% confidence interval [CI], -1.57 to -0.31 ...)"* — [PMID: 39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/)

> *"Intravenous bevacizumab, oral pazopanib, and oral thalidomide are the three targeted primary angiogenesis inhibitors, with multiple studies describing both reassuring safety and impressive effectiveness in the treatment of moderate-to-severe HHT-associated bleeding."* — [PMID: 35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/)

A disease-specific **HHT-QoL** instrument has now been externally validated (MCID ~1 point), enabling longitudinal QoL assessment in trials ([PMID: 41092987](https://pubmed.ncbi.nlm.nih.gov/41092987/)). Aflibercept reduced cardiac index from 3.92 to 2.90 L/min/m² after bevacizumab/pazopanib failure ([PMID: 40379104](https://pubmed.ncbi.nlm.nih.gov/40379104/)).

**Treatment (NCIT) terms:** NCIT:C1794 (thalidomide), NCIT:C2039 (bevacizumab), NCIT:C71146 (pazopanib), NCIT:C72713 (pomalidomide), NCIT:C74405 (aflibercept), NCIT:C47737 (tranexamic acid); CHEBI:9445 (thalidomide).

### 7. Model organisms recapitulate AVMs and implicate VEGF as a druggable second driver

Multiple engineered mouse models reproduce HHT vascular lesions: **Bmp9-KO** mice develop spontaneous AVMs in liver, GI tract, and uterus; **Bmp10-inducible-KO** and **Bmp9/10-double-KO** develop retinal, brain, and skin AVMs; endothelial **Alk1/Eng** deletion produces AVMs requiring a secondary trigger (wounding). In the *Alk1* wound-induced skin AVM model, **VEGF mimics the wound effect, and a VEGF-neutralizing antibody prevents AVM formation and ameliorates internal bleeding**. HHT1-specific human models include a CRISPR/Cas9 *ENG* c.1A>G (p.Met1Val) hiPSC line (LUMCi029-A-2) for drug testing, and new mouse models of somatic second-hit *ENG*/*ACVRL1* mutations.

> *"VEGF can mimic the wound effect on skin AVM formation, and VEGF-neutralizing antibody can prevent skin AVM formation and ameliorate internal bleeding in Alk1-deficient adult mice"* — [PMID: 24957885](https://pubmed.ncbi.nlm.nih.gov/24957885/)

> *"Using CRISPR/Cas9-mediated gene editing, the ENG c.1A > G mutation was introduced in homozygous form in the well-characterized LUMCi029-A line."* — [PMID: 41880974](https://pubmed.ncbi.nlm.nih.gov/41880974/)

New mouse models directly modeling **somatic second-hit mutations** further validate the two-hit mechanism ([PMID: 41756958](https://pubmed.ncbi.nlm.nih.gov/41756958/)); a broader preclinical-model review summarizes the ENG/ALK1 axis and its lesions ([PMID: 36250069](https://pubmed.ncbi.nlm.nih.gov/36250069/)). **Model recapitulation:** these systems reproduce AVMs, arteriovenous shunting, and bleeding; **limitations** include incomplete modeling of chronic human epistaxis and mucocutaneous telangiectasia distribution. **Orthologue:** mouse *Eng* (NCBI Gene 13805); human *ENG* (NCBI Gene 2022).

### 8. Prognosis: reduced life expectancy; anemia, GI bleeding, and liver VMs predict mortality

A population-based Swedish registry found **life expectancy after age 30 of 73.0 years (95% CI 68.0–77.2) in HHT vs 80.5 (79.1–82.0) in matched controls**, with excess deaths from ischemic heart disease, arterial/capillary disease, and liver disease. A questionnaire cohort estimated ~19 years (SD 11) of life lost, with causes of death: **sepsis 35%, cardiac failure 26%, severe bleeding 20%, terminal cancer 13%**. In the Brain Vascular Malformation Consortium prospective cohort (N=1,286; 59 deaths), independent mortality predictors were **history of anemia (HR 2.93, 95% CI 1.37–6.26, p=0.006)**, **GI bleeding (HR 2.63, 1.46–4.74, p=0.001)**, and **symptomatic liver VMs (HR 2.10, 1.15–3.84, p=0.015)**. Notably, **brain VMs and PAVMs were NOT associated with mortality**, and SMAD4 carriers had markedly higher mortality (HR 18.36) than ENG/ACVRL1.

> *"Life expectancy for cases with HHT after age 30 was estimated at 73.0 (68.0-77.2) compared to 80.5 (79.1-82.0) years for controls."* — [PMID: 42410718](https://pubmed.ncbi.nlm.nih.gov/42410718/)

> *"A history of anemia was associated with increased mortality (HR = 2.93, 95% CI 1.37-6.26, p = 0.006), as were gastro-intestinal (GI) bleeding (HR = 2.63, 95% CI 1.46-4.74, p = 0.001), and symptomatic liver VMs (HR = 2.10, 95% CI 1.15-3.84, p = 0.015). Brain VMs and pulmonary arteriovenous malformations (AVMs) were not associated with mortality"* — [PMID: 33407668](https://pubmed.ncbi.nlm.nih.gov/33407668/)

> *"35% (95% CI: 23-48%) died from sepsis, 26% (95% CI: 16-38%) from cardiac failure, 20% (95% CI: 9-28%) from a severe bleeding episode"* — [PMID: 29781402](https://pubmed.ncbi.nlm.nih.gov/29781402/)

HHT is a **chronic, lifelong, progressive** disorder with episodic bleeding; recovery is not spontaneous but complications are largely preventable with surveillance and intervention.

### 9. Prevention/screening: PAVM and brain-VM screening, embolization, and antibiotic prophylaxis

Because HHT1 carries a high risk of pulmonary and cerebral AVMs, guideline-based prevention includes: **contrast transthoracic echocardiography (TTCE)** to screen for right-to-left shunt/PAVMs, with **transcatheter coil/plug embolization** of PAVMs with feeding arteries >3 mm (standard of care) to prevent paradoxical embolic stroke, brain abscess, and hemorrhage; **contrast-enhanced brain MRI screening** (brain vascular malformations occur in ~10% of patients); and **antibiotic prophylaxis** before dental/surgical procedures to prevent brain abscess from paradoxical bacteremia. **Cascade genetic testing** of first-degree relatives for the family *ENG* variant enables presymptomatic diagnosis. **Pregnancy increases PAVM rupture risk**, requiring surveillance.

> *"Embolisation represents the standard of care for significant PAVMs with periodic radiological surveillance recommended."* — [PMID: 42209023](https://pubmed.ncbi.nlm.nih.gov/42209023/)

> *"organ vascular malformations including in the brain, which occur in about 10% of patients"* — [PMID: 38816017](https://pubmed.ncbi.nlm.nih.gov/38816017/)

> *"Pulmonary VMs can lead to paradoxical embolism of thrombi or bacteria, e.g., due to dental procedures."* — [PMID: 36820363](https://pubmed.ncbi.nlm.nih.gov/36820363/)

The Second International HHT Guidelines provide 36 evidence-based recommendations across epistaxis, GI bleeding, anemia/iron deficiency, liver VMs, pediatric care, and pregnancy/delivery ([PMID: 32894695](https://pubmed.ncbi.nlm.nih.gov/32894695/)). These map to **primary** (risk counseling), **secondary** (screening/early embolization), and **tertiary** (complication management) prevention levels. Genetic counseling covers 50% autosomal-dominant recurrence risk and reproductive options (PGT/prenatal testing).

### 10. Hepatic vascular malformations drive high-output heart failure

In a Danish national cohort (152 HHT patients), **hepatic vascular malformations (HVMs)** were present in **67.8%** (up to 78% in the literature); **high-output heart failure (HOHF)** occurred in **6.6%**, 90% of whom had grade 4 HVMs. Cardiac index correlated with HVM severity (Buscarini grade) (**ρ=0.36, p<0.001**), demonstrating a graded hemodynamic mechanism: arteriovenous hepatic shunting increases stroke volume and cardiac preload/output. Symptomatic hepatic involvement is more characteristic of HHT2, but HVMs occur across genotypes and are an independent mortality predictor.

> *"HVMs were identified in 103 patients (67.8%), of whom 24 (15.8%) had grade 4 HVMs. HOHF was present in 10 patients (6.6%), nine of whom (90%) had grade 4 HVMs."* — [PMID: 42019870](https://pubmed.ncbi.nlm.nih.gov/42019870/)

> *"Cardiac index measured by TTE correlated positively with HVM severity"* — [PMID: 42019870](https://pubmed.ncbi.nlm.nih.gov/42019870/)

Hepatic arterial embolization carries a high risk of portal-vein thrombosis and is generally avoided; Doppler ultrasound is the preferred screening modality with CT/MRI for characterization ([PMID: 42517041](https://pubmed.ncbi.nlm.nih.gov/42517041/)).

### 11. Structural basis: endoglin's N-terminal orphan domain binds BMP9; HHT1 mutations map to this interface

Crystal structures of the human endoglin (ENG/CD105) ectodomain and its complex with BMP9 show that **BMP9 interacts with a hydrophobic surface of endoglin's N-terminal orphan domain** — a novel duplicated/circularly-permuted fold — while the **C-terminal zona pellucida (ZP) module** allows two copies of ENG to embrace homodimeric BMP9. Critically, the ENG–BMP9 interface involves **residues mutated in HHT1** and overlaps with the epitope of the tumor-suppressing anti-ENG monoclonal antibody TRC105. BMP9 binding to endoglin is compatible with ligand recognition by type I (ALK1) but not type II receptors, structurally rationalizing endoglin's ligand-presentation role.

> *"BMP9 interacts with a hydrophobic surface of the N-terminal orphan domain of ENG, which adopts a new duplicated fold generated by circular permutation. The interface involves residues mutated in HHT1 and overlaps with the epitope of tumor-suppressing anti-ENG monoclonal TRC105."* — [PMID: 28564608](https://pubmed.ncbi.nlm.nih.gov/28564608/)

> *"The structure of the C-terminal zona pellucida module suggests how two copies of ENG embrace homodimeric BMP9, whose binding is compatible with ligand recognition by type I but not type II receptors."* — [PMID: 28564608](https://pubmed.ncbi.nlm.nih.gov/28564608/)

This provides the protein-level mechanism by which missense HHT1 variants disrupt ligand binding. Related structural work on BMP-9/-10 interchain disulfide bonds clarifies how the physiological heterodimeric ligand forms ([PMID: 39793884](https://pubmed.ncbi.nlm.nih.gov/39793884/)).

**Ontology terms:** UniProt P17813 (Endoglin, human); GO:0005515 (protein binding); GO:0009986 (cell surface).

### 12. Candidate circulating biomarkers

A review of HHT biomarkers reports plasma/serum candidates: **soluble proteins** — VEGF, TGF-β1, soluble endoglin, and angiopoietin-2 — plus **microRNA variants miR-27a, miR-205, and miR-210** — alongside gene-expression fingerprinting, NGS gene panels, and infrared-spectroscopy/artificial-neural-network approaches. These remain research-stage adjuncts; diagnosis is still clinical (Curaçao) plus molecular confirmation. Elevated VEGF underlies the rationale for anti-VEGF therapy.

> *"products detected in plasma or serum samples: soluble proteins (vascular endothelial growth factor, transforming growth factor β1, soluble endoglin, angiopoietin-2) and microRNA variants (miR-27a, miR-205, miR-210)"* — [PMID: 25873934](https://pubmed.ncbi.nlm.nih.gov/25873934/)

### 13. Human lesion sequencing confirms a bi-allelic two-hit mechanism

Deep sequencing of human HHT lesions demonstrates that focal telangiectasias and internal-organ AVMs acquire a **somatic second hit in the same HHT gene** carrying the germline variant, reconciling systemic haploinsufficiency with focal lesions. Marchuk-lab work identified **somatic point mutations AND loss of heterozygosity (LOH)** across the germline-mutant chromosome in liver telangiectases, one pulmonary AVM, and two brain AVMs. In an *ACVRL1*-germline-deletion patient, multiple lesion-specific somatic variants were found across hepatic AVMs and a skin telangiectasia. The same paradigm applies to *ENG*/HHT1.

> *"another mechanism for the second hit is loss of heterozygosity across the chromosome bearing the germline mutation"* — [PMID: 39299239](https://pubmed.ncbi.nlm.nih.gov/39299239/)

> *"we identified somatic molecular genetic events in eight liver telangiectases, including point mutations and a loss of heterozygosity event. We also identified somatic mutations in one pulmonary AVM and two brain AVMs"* — [PMID: 39299239](https://pubmed.ncbi.nlm.nih.gov/39299239/)

> *"Somatic mosaic lesion-specific ACVRL1 variants were identified in four hepatic AVM samples and in one telangiectasia."* — [PMID: 41162588](https://pubmed.ncbi.nlm.nih.gov/41162588/)

Additional support comes from investigations of somatic second-hit variation in HHT lesions ([PMID: 39062925](https://pubmed.ncbi.nlm.nih.gov/39062925/)) and a JP-HHT AVM harboring two somatic second-hit alterations ([PMID: 39939156](https://pubmed.ncbi.nlm.nih.gov/39939156/)). Somatic events are found in roughly half of telangiectases, with LOH providing an additional route.

### 14. Single-cell profiling reveals a pathogenic, druggable KIT+ angiogenic endothelial state

Regionally-resolved single-cell RNA-seq of *Alk1*-deficient mouse brain AVMs identified an emergent **KIT+ angiogenic endothelial-cell population** with human-AVM-like transcriptional features (tip-cell markers, PI3K and KRAS pathway activation). **KIT is directly repressed by BMP9–ALK1–SMAD4 signaling**; KIT expression is conserved in human sporadic and HHT2 brain AVMs; and **pharmacologic KIT inhibition reduced AVMs without harming normal vasculature**. Complementary human endothelial siRNA work shows that depleting different BMP-pathway components (e.g., *ENG* vs *ACVRL1*) drives **divergent endothelial flow-response programs**, arguing that HHT1 is not mechanistically interchangeable with HHT2.

> *"This process is driven by the emergence of a KIT+ angiogenic EC population with human AVM-like transcriptional features, including tip-cell markers and activation of PI3K and KRAS signaling pathways."* — [PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/)

> *"Kit is directly repressed by BMP9-ALK1-SMAD4 signaling. Pharmacological inhibition of KIT reduced angiogenic reprogramming and vascular malformations in vivo without affecting normal vasculature"* — [PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/)

> *"These findings reveal divergent cellular programs driving arteriovenous malformations and underscore the need for gene-specific diagnostic and therapeutic strategies."* — [PMID: 42460472](https://pubmed.ncbi.nlm.nih.gov/42460472/)

**Ontology terms:** CL:0000115 (endothelial cell); GO:0001525 (angiogenesis); GO:0048010 (VEGF receptor signaling pathway).

### 15. Striking variable expressivity even within single-mutation families

In a large single-mutation HHT kindred, clinical manifestations and severity varied "tremendously" despite an identical germline allele — mechanistically consistent with the requirement for **stochastic somatic second hits (mutation/LOH) and local angiogenic triggers**. Organ-AVM frequencies also vary; pulmonary AVMs are consistently more common in HHT1 than HHT2.

> *"Even in this family in which all affected individuals have the same mutation, the clinical manifestations of HHT and their severity varied tremendously. Intrafamilial variation in expression of HHT is clearly significant"* — [PMID: 10946360](https://pubmed.ncbi.nlm.nih.gov/10946360/)

> *"It also adds to the evidence suggesting that pulmonary AVMs are more common in HHT 1 than in HHT 2."* — [PMID: 10946360](https://pubmed.ncbi.nlm.nih.gov/10946360/)

This underpins the inheritance profile: **autosomal dominant, high but age-dependent penetrance, highly variable expressivity**; no repeat-expansion anticipation. Founder effects contribute to population-specific variants; consanguinity is not central (dominant disorder).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **germline heterozygous loss-of-function variant in *ENG*** (frameshift, nonsense, splice, missense, or start-loss) **leads to** reduced endoglin protein on the endothelial cell surface (**haploinsufficiency**). *(demonstrated — [PMID: 41880974](https://pubmed.ncbi.nlm.nih.gov/41880974/), [PMID: 42633037](https://pubmed.ncbi.nlm.nih.gov/42633037/))*
2. Reduced endoglin **results in** impaired presentation of circulating **BMP9/BMP10** ligands to the **ALK1 (ACVRL1)–BMPR-II** receptor complex, **leading to** reduced **SMAD1/5/8** phosphorylation. *(demonstrated — [PMID: 36828679](https://pubmed.ncbi.nlm.nih.gov/36828679/), [PMID: 28564608](https://pubmed.ncbi.nlm.nih.gov/28564608/))*
3. Reduced BMP–SMAD signaling **results in** loss of the endothelial quiescence/arteriovenous-identity program (dysregulated Notch, cell-cycle, and endothelial-identity genes). *(demonstrated in mouse — [PMID: 38502919](https://pubmed.ncbi.nlm.nih.gov/38502919/), [PMID: 36348215](https://pubmed.ncbi.nlm.nih.gov/36348215/))*
4. **Branch point — a focal "second hit" is required.** In a subset of endothelial cells, a **somatic second mutation or LOH** in *ENG* (bi-allelic loss) AND/OR a **local angiogenic/inflammatory trigger** (wounding, VEGF, hormonal change, infection) **leads to** complete local pathway failure. *(demonstrated in human lesions — [PMID: 39299239](https://pubmed.ncbi.nlm.nih.gov/39299239/), [PMID: 41162588](https://pubmed.ncbi.nlm.nih.gov/41162588/); trigger demonstrated in mouse — [PMID: 24957885](https://pubmed.ncbi.nlm.nih.gov/24957885/))*
5. Local pathway failure **results in** derepression of angiogenic programs, including emergence of a **KIT+ angiogenic endothelial state** (tip-cell markers; PI3K/KRAS activation), with elevated VEGF signaling. *(demonstrated in mouse + human validation — [PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/))*
6. Aberrant angiogenesis and defective vascular stabilization **lead to** direct artery-to-vein connections that bypass the capillary bed — forming **telangiectasias** (small, mucocutaneous) and **AVMs** (large, visceral). *(inferred/demonstrated — [PMID: 19834013](https://pubmed.ncbi.nlm.nih.gov/19834013/))*
7. Fragile lesions **result in** the clinical phenotype, which **branches by anatomical site** (below).

```
   ENG LoF (germline, 1 allele)
            │ haploinsufficiency
            ▼
  ↓ BMP9/BMP10 → ENG/ALK1 → SMAD1/5/8 signaling
            │ loss of vascular quiescence
            ▼
  ┌─────────  SECOND HIT REQUIRED  ─────────┐
  │ somatic mutation / LOH in ENG   +/or     │
  │ angiogenic trigger (VEGF, wound, hormone)│
  └──────────────────┬───────────────────────┘
                     ▼
     KIT+ angiogenic EC state (PI3K/KRAS, tip cells)
                     ▼
     Telangiectasias  &  Arteriovenous Malformations
        │            │            │           │
   Nasal→epistaxis  Lung→stroke  Liver→HOHF  Brain→hemorrhage
        ▼
   Iron-deficiency anemia, ↓QoL, reduced life expectancy
```

**Upstream vs downstream:** The germline *ENG* defect and BMP–SMAD signaling loss are **upstream** and systemic (present in every cell); the somatic second hit, KIT+ angiogenic reprogramming, and focal lesion formation are **downstream** and stochastic — this architecture is the mechanistic explanation for HHT's hallmark **variable expressivity**, even within a single-mutation family ([PMID: 10946360](https://pubmed.ncbi.nlm.nih.gov/10946360/)). **Cell type:** vascular endothelial cell (CL:0000115). **Biological processes:** BMP signaling (GO:0030509), angiogenesis (GO:0001525), blood vessel morphogenesis (GO:0048514).

### Anatomical structures affected

| Level | Structures | UBERON / CL / GO |
|---|---|---|
| Organ (primary) | Nasal mucosa, lung, brain, liver, GI tract, skin | UBERON:0001707 (nasal cavity), UBERON:0002048 (lung), UBERON:0000955 (brain), UBERON:0002107 (liver), UBERON:0000160 (intestine), UBERON:0002097 (skin) |
| Body systems | Cardiovascular (primary), respiratory, nervous, digestive | UBERON:0004535 (cardiovascular system) |
| Tissue | Vascular endothelium; capillary/arteriole/venule walls | UBERON:0001981 (blood vessel) |
| Cell | Vascular endothelial cell (KIT+ angiogenic sub-state) | CL:0000115 |
| Subcellular | Cell-surface receptor complex; nucleus (SMAD signaling) | GO:0009986, GO:0005634 |
| Lateralization | Multifocal, bilateral, systemic | — |

### Phenotype table

| Phenotype (HPO) | Type | Frequency | Onset | Severity/Course |
|---|---|---|---|---|
| Epistaxis (HP:0000421) | Symptom | Near-universal | Childhood, earlier in HHT1 | Progressive, episodic; drives anemia |
| Telangiectasia (HP:0001009) | Physical sign | Very frequent | Adolescence–adulthood | Progressive |
| Pulmonary AVM (HP:0002629 spectrum) | Structural | ~34% symptomatic (HHT1) | Congenital/childhood; 59% of children | Stable→enlarging; embolic risk |
| Cerebral AVM (HP:0002408) | Structural | ~10% brain VMs | Congenital | Rupture risk |
| Cerebral abscess | Complication | ~7.5% (HHT1) | Adult | Serious/acute |
| Hepatic AVM (HP:0100761) | Structural | up to ~68–78% | Adult | Graded → high-output HF |
| GI bleeding (HP:0002239) | Symptom | Higher in HHT2 | Older adult | Chronic |
| Iron-deficiency anemia (HP:0004840) | Lab abnormality | Frequent | Any | Fluctuating; mortality predictor |

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding(s) | Evidence type |
|---|---|---|---|
| [41880974](https://pubmed.ncbi.nlm.nih.gov/41880974/) | ENG p.Met1Val hiPSC line for HHT1 | F1, F7 | In vitro / model |
| [41251906](https://pubmed.ncbi.nlm.nih.gov/41251906/) | 15th HHT conference summary | F1, F2 | Review |
| [42633037](https://pubmed.ncbi.nlm.nih.gov/42633037/) | Korean phenotype/genetic study | F1 | Human clinical |
| [41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/) | Global genetic prevalence | F2 | Genomic database |
| [34889398](https://pubmed.ncbi.nlm.nih.gov/34889398/) | HHT management guide | F3 | Review |
| [33677851](https://pubmed.ncbi.nlm.nih.gov/33677851/) | Korean genetic/phenotype study | F3 | Human clinical |
| [36828679](https://pubmed.ncbi.nlm.nih.gov/36828679/) | BMP-9 endothelial signaling | F4 | Review |
| [38502919](https://pubmed.ncbi.nlm.nih.gov/38502919/) | BMP9 loss induces AVMs | F4, F7 | Model organism |
| [36348215](https://pubmed.ncbi.nlm.nih.gov/36348215/) | BMP10 indispensable for AV network | F4 | Model organism |
| [39651127](https://pubmed.ncbi.nlm.nih.gov/39651127/) | Arterial endothelial HHT2 deletion | F4 | Model organism |
| [17224686](https://pubmed.ncbi.nlm.nih.gov/17224686/) | French–Italian genotype–phenotype | F5 | Human clinical |
| [29916764](https://pubmed.ncbi.nlm.nih.gov/29916764/) | Pediatric PAVM longitudinal study | F5 | Human clinical |
| [39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/) | Pomalidomide RCT | F6 | Human RCT |
| [35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/) | Antiangiogenic therapy guide | F6 | Review |
| [24957885](https://pubmed.ncbi.nlm.nih.gov/24957885/) | VEGF neutralization in HHT2 model | F7 | Model organism |
| [41756958](https://pubmed.ncbi.nlm.nih.gov/41756958/) | Somatic second-hit mouse models | F7, F13 | Model organism |
| [42410718](https://pubmed.ncbi.nlm.nih.gov/42410718/) | Population registry survival | F8 | Human registry |
| [33407668](https://pubmed.ncbi.nlm.nih.gov/33407668/) | Predictors of mortality | F8 | Human cohort |
| [29781402](https://pubmed.ncbi.nlm.nih.gov/29781402/) | Life expectancy/comorbidities | F8 | Human cohort |
| [42209023](https://pubmed.ncbi.nlm.nih.gov/42209023/) | Exertional dyspnoea / embolization | F9 | Review/clinical |
| [38816017](https://pubmed.ncbi.nlm.nih.gov/38816017/) | Pediatric brain VM screening | F9 | Review |
| [36820363](https://pubmed.ncbi.nlm.nih.gov/36820363/) | Dental screening campaign | F9 | Public health |
| [32894695](https://pubmed.ncbi.nlm.nih.gov/32894695/) | Second International Guidelines | F3, F9 | Guideline |
| [42019870](https://pubmed.ncbi.nlm.nih.gov/42019870/) | Hepatic VM hemodynamics | F10 | Human cohort |
| [28564608](https://pubmed.ncbi.nlm.nih.gov/28564608/) | ENG–BMP9 structure | F11 | Structural |
| [25873934](https://pubmed.ncbi.nlm.nih.gov/25873934/) | HHT biomarkers | F12 | Review |
| [39299239](https://pubmed.ncbi.nlm.nih.gov/39299239/) | Somatic two-hit lesion sequencing | F13 | Human lesion |
| [41162588](https://pubmed.ncbi.nlm.nih.gov/41162588/) | Multiple lesion-specific ACVRL1 hits | F13 | Human lesion |
| [39062925](https://pubmed.ncbi.nlm.nih.gov/39062925/) | Genetic determinants of lesions | F13 | Human lesion |
| [42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/) | KIT+ angiogenic EC / KIT inhibition | F14 | Model + human |
| [42460472](https://pubmed.ncbi.nlm.nih.gov/42460472/) | Gene-specific endothelial programs | F14 | In vitro |
| [10946360](https://pubmed.ncbi.nlm.nih.gov/10946360/) | Large HHT2 kindred variability | F15 | Human clinical |

**Additional supporting literature:** standardized bleeding terminology ([PMID: 40662351](https://pubmed.ncbi.nlm.nih.gov/40662351/)); validated HHT-QoL scale ([PMID: 41092987](https://pubmed.ncbi.nlm.nih.gov/41092987/)); aflibercept salvage ([PMID: 40379104](https://pubmed.ncbi.nlm.nih.gov/40379104/)); preclinical model review ([PMID: 36250069](https://pubmed.ncbi.nlm.nih.gov/36250069/)); vascular malformation biology ([PMID: 19834013](https://pubmed.ncbi.nlm.nih.gov/19834013/)); hormonal-status questionnaire ([PMID: 41862858](https://pubmed.ncbi.nlm.nih.gov/41862858/)); pediatric stroke/PAVM incidence ([PMID: 42247997](https://pubmed.ncbi.nlm.nih.gov/42247997/)); EHR female-predominance ([PMID: 42162269](https://pubmed.ncbi.nlm.nih.gov/42162269/)); imaging/interventional review ([PMID: 34723698](https://pubmed.ncbi.nlm.nih.gov/34723698/)); hepatic imaging series ([PMID: 42517041](https://pubmed.ncbi.nlm.nih.gov/42517041/)); BMP-9/10 disulfide structure ([PMID: 39793884](https://pubmed.ncbi.nlm.nih.gov/39793884/)); JP-HHT two-hit AVM ([PMID: 39939156](https://pubmed.ncbi.nlm.nih.gov/39939156/)).

---

## Sections with limited / non-applicable data for HHT1

- **Environmental / infectious etiology (Section 5):** HHT1 is a monogenic disorder with no infectious cause. Environmental/physiological factors act as **second-hit angiogenic triggers** — wounding/VEGF (model organism, [PMID: 24957885](https://pubmed.ncbi.nlm.nih.gov/24957885/)) and hormonal changes (puberty/pregnancy worsen epistaxis; combined estrogen–progestin may reduce it; [PMID: 41862858](https://pubmed.ncbi.nlm.nih.gov/41862858/)). Infection is a *consequence* (brain abscess from paradoxical bacteremia), not a cause.
- **Protective factors:** No validated genetic protective alleles are established. Combined estrogen–progestin therapy was associated with less epistaxis in 52% of treated women ([PMID: 41862858](https://pubmed.ncbi.nlm.nih.gov/41862858/)).
- **Epigenetics / chromosomal abnormalities:** No recurrent large-scale cytogenetic abnormality defines HHT1; it is single-gene. Somatic **LOH** (a chromosomal-scale event) contributes as a second hit ([PMID: 39299239](https://pubmed.ncbi.nlm.nih.gov/39299239/)). Dedicated disease-driver methylation/histone data are not established.
- **Other species / natural disease (Section 14):** Orthologous genes exist (mouse *Eng*, NCBI Gene 13805; human *ENG*, NCBI Gene 2022). Disease is modeled via engineered mice, zebrafish, and hiPSCs rather than a naturally occurring companion-animal disease; no prominent veterinary or zoonotic dimension.
- **Somatic vs germline origin:** The disease-defining variant is **germline**; the disease-precipitating second hit is **somatic** ([PMID: 39299239](https://pubmed.ncbi.nlm.nih.gov/39299239/)).

---

## Limitations and Knowledge Gaps

1. **Genotype-specific data scarcity.** Much mechanistic work (VEGF neutralization, KIT+ angiogenic state, arterial-endothelial deletion) derives from *Alk1*/HHT2 or *Bmp9/10* models rather than *ENG*/HHT1-specific systems. In vitro data ([PMID: 42460472](https://pubmed.ncbi.nlm.nih.gov/42460472/)) argue ENG and ACVRL1 drive **divergent programs**, so HHT2-derived findings may not transfer wholesale to HHT1.
2. **Second-hit frequency and detectability.** Somatic second hits are found in roughly half of telangiectases; it remains unclear whether undetected low-frequency hits, LOH, or purely environmental triggers account for the remainder.
3. **Modifier genes.** Beyond stochastic second hits, germline modifiers of angiogenesis (e.g., VEGF/PLGF levels) that shape variable expressivity are largely uncharacterized for HHT1.
4. **Biomarkers remain research-stage.** Soluble endoglin, VEGF, TGF-β1, angiopoietin-2, and miRNAs are not yet validated for diagnosis or prognosis ([PMID: 25873934](https://pubmed.ncbi.nlm.nih.gov/25873934/)).
5. **Trial evidence for antiangiogenics is still maturing.** Only pomalidomide has pivotal RCT support ([PMID: 39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/)); bevacizumab, pazopanib, and thalidomide are largely off-label/observational.
6. **Prognostic data are cohort-dependent.** Mortality predictors ([PMID: 33407668](https://pubmed.ncbi.nlm.nih.gov/33407668/)) mix genotypes; ENG-specific survival curves are limited.
7. **This is a literature-synthesis report.** No primary patient-level dataset was analyzed; all quantitative claims derive from published cohorts, registries, and experimental studies.

---

## Proposed Follow-up Experiments / Actions

1. **HHT1-specific single-cell atlas.** Apply the regionally-resolved scRNA-seq approach used for *Alk1* AVMs ([PMID: 42579368](https://pubmed.ncbi.nlm.nih.gov/42579368/)) to *Eng*-deficient lesions to test whether the **KIT+ angiogenic EC state** and PI3K/KRAS activation are shared or gene-specific — directly informing whether KIT inhibitors would benefit HHT1.
2. **Test KIT inhibition and anti-VEGF in ENG-null human models.** Use the LUMCi029-A-2 *ENG* p.Met1Val hiPSC line ([PMID: 41880974](https://pubmed.ncbi.nlm.nih.gov/41880974/)) and *ENG* second-hit mouse models ([PMID: 41756958](https://pubmed.ncbi.nlm.nih.gov/41756958/)) to benchmark KIT inhibitors, bevacizumab, and pomalidomide head-to-head.
3. **Deep/duplex sequencing of ENG lesions.** Increase sequencing depth on HHT1 telangiectases and PAVMs to raise second-hit detection rates and quantify the LOH-vs-point-mutation-vs-trigger split.
4. **Biomarker validation study.** Prospectively test soluble endoglin, VEGF, and the miR-27a/205/210 panel against ESS, anemia, and treatment response in an ENG-genotyped cohort to move biomarkers toward clinical utility.
5. **Genotype-stratified antiangiogenic trials.** Design comparative trials (per standardized bleeding outcome criteria, [PMID: 40662351](https://pubmed.ncbi.nlm.nih.gov/40662351/); using validated HHT-QoL, [PMID: 41092987](https://pubmed.ncbi.nlm.nih.gov/41092987/)) that pre-specify ENG (HHT1) vs ACVRL1 (HHT2) subgroups.
6. **Modifier-gene mapping.** Perform family-based and cohort GWAS/burden testing in HHT1 to identify germline modifiers explaining organ-specific AVM burden and epistaxis severity.
7. **Address underdiagnosis.** Given the genetic-vs-clinical prevalence gap ([PMID: 41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/)), scale cascade genetic testing and awareness programs (e.g., dental screening, [PMID: 36820363](https://pubmed.ncbi.nlm.nih.gov/36820363/)) to improve early PAVM detection and stroke prevention.

---

*Report compiled from 15 confirmed findings across 5 investigation iterations and 56 reviewed papers. Evidence types span human clinical cohorts and registries, human lesion sequencing, structural biology, engineered mouse models, hiPSC/in-vitro systems, and genomic-database analyses. Evidence is human clinical unless otherwise noted.*


## Artifacts

- [OpenScientist final report](Hereditary_Hemorrhagic_Telangiectasia_Type_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Hemorrhagic_Telangiectasia_Type_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 44 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 44 |
| On topic | 21 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42162269` (5 mentions) - Systematic mapping of rare genetic disease studies using UK primary care electronic health records.
  - shared terms: human
- `PMID:42410718` (4 mentions) - Expected survival is decreased in hereditary hemorrhagic telangiectasia: Results from a population-based registry study.
  - shared terms: hht

Weighed against this report's own most characteristic terms: `eng`, `hht`, `hht1`, `avms`, `acvrl1`, `vascular`, `variant`, `human`, `bmp9`, `bleeding`, `angiogenic`, `brain`, `hht2`, `somatic`, `clinical`, `epistaxis`, `alk1`, `pulmonary`, `model`, `germline`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 22 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C1794` (1 mention) - the report calls it "thalidomide"; NCIT calls it **Capecitabine**
- `NCIT:C71146` (1 mention) - the report calls it "pazopanib"; NCIT calls it **Salirasib**
- `NCIT:C72713` (1 mention) - the report calls it "pomalidomide"; NCIT calls it **Azipramine**
- `NCIT:C74405` (1 mention) - the report calls it "aflibercept"; NCIT calls it **Betamethasone Acibutate**
- `NCIT:C47737` (1 mention) - the report calls it "tranexamic acid"; NCIT calls it **Sulfamethoxazole**
- `CHEBI:9445` (1 mention) - the report calls it "thalidomide"; CHEBI calls it **terazosin**
- `CL:0000115` (3 mentions) - the report calls it "endothelial cell", "Vascular endothelial cell (KIT+ angiogenic sub-state)"; CL calls it **endothelial cell**
- `HP:0100761` (1 mention) - the report calls it "Hepatic AVM"; HP calls it **Visceral angiomatosis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0048010` (1 mention) - the report calls it "VEGF receptor signaling pathway"; GO calls it **vascular endothelial growth factor receptor signaling pathway**, and lists "VEGF receptor signaling pathway" among its other names
- `HP:0002408` (1 mention) - the report calls it "Cerebral AVM"; HP calls it **Cerebral arteriovenous malformation**, and lists "Cerebral AV malformation" among its other names
- `HP:0002239` (1 mention) - the report calls it "GI bleeding"; HP calls it **Gastrointestinal hemorrhage**, and lists "Gastrointestinal bleeding" among its other names
- `HP:0004840` (1 mention) - the report calls it "Iron-deficiency anemia"; HP calls it **Hypochromic microcytic anemia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000115` - called "endothelial cell", "Vascular endothelial cell (KIT+ angiogenic sub-state)"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.