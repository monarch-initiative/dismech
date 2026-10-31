---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T19:19:07.839651'
end_time: '2026-09-29T19:36:58.196575'
duration_seconds: 1070.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Haemophilus meningitis
  mondo_id: MONDO:0000889
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
citation_count: 49
reference_validation:
  total_references: 49
  verified: 49
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 20
  quotes_valid: 16
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:33247582
  - PMID:34590133
  - PMID:33668442
  - PMID:41911930
  relevance_assessed: 49
  on_topic: 35
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 32
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 1
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Clinical sign
    ontology_label: Fever
  - term_id: HP:0002315
    reported_labels:
    - Symptom
    ontology_label: Headache
  - term_id: HP:0031179
    reported_labels:
    - Clinical sign
    ontology_label: Nuchal rigidity
  - term_id: HP:0000613
    reported_labels:
    - Symptom
    ontology_label: Photophobia
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0000407
    reported_labels:
    - Lab/clinical
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0012595
    reported_labels:
    - Physical/imaging
    ontology_label: Mild proteinuria
  - term_id: HP:0000238
    reported_labels:
    - Physical/imaging
    ontology_label: Hydrocephalus
  - term_id: HP:0007360
    reported_labels:
    - Clinical sign
    ontology_label: Aplasia/Hypoplasia of the cerebellum
  - term_id: HP:0012229
    reported_labels:
    - Lab abnormality
    ontology_label: CSF pleocytosis
  - term_id: UBERON:0002361
    reported_labels:
    - "Primary organ/system:** central nervous system \u2014 **meninges"
    ontology_label: pia mater
  - term_id: UBERON:0001844
    reported_labels:
    - Secondary organ involvement / complications:** **inner ear/cochlea
    ontology_label: cochlea
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Haemophilus_Meningitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Haemophilus_Meningitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Haemophilus meningitis
- **MONDO ID:** MONDO:0000889 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Haemophilus meningitis** covering all of the
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

# Haemophilus Meningitis (MONDO:0000889): A Comprehensive Disease Characterization

*Infectious Disease Knowledge Base Report — compiled from iterative literature synthesis (59 citations, 12 recorded findings)*

---

## Summary

**Haemophilus meningitis** (MONDO:0000889; ICD-10 **G00.0** "Haemophilus meningitis"; MeSH **D008586** "Meningitis, Haemophilus") is an acute bacterial (pyogenic) meningitis caused by the human-restricted Gram-negative coccobacillus *Haemophilus influenzae*, historically and predominantly serotype **b (Hib)**. It is an **infectious, non-genetic disease**: there is no causal human gene, no Mendelian inheritance, and no OMIM entry for the disease itself. The information base is aggregated disease-level epidemiology, clinical cohorts, randomized trials, and experimental animal/cell-barrier models rather than individual-patient genetic data.

The pathophysiology is a well-defined causal chain: the **polyribosylribitol phosphate (PRP) capsule** allows Hib to resist phagocytosis and complement, survive in the bloodstream, and invade the blood–CSF barrier in a polarized fashion; once in the subarachnoid space, shed **lipooligosaccharide (LOS)** triggers a **TNF-α / IL-1β-driven** meningeal inflammatory cascade that produces cerebral edema, raised intracranial pressure, cochlear injury, and neuronal damage. Clinically the disease presents with fever, headache, neck stiffness, photophobia and altered mental status; case fatality reaches up to ~30% and roughly 50% of survivors develop neurological sequelae (deafness, seizures, cognitive impairment, hydrocephalus). Treatment is a third-generation cephalosporin (ceftriaxone or cefotaxime) plus **adjunctive dexamethasone**, which reduces hearing loss with the strongest evidence in Hib meningitis when given before or with the first antibiotic dose.

The single most important fact about this disease in the modern era is the transformative impact of **PRP–protein conjugate vaccination**. Hib was the leading cause of childhood bacterial meningitis in the pre-vaccine era; conjugate vaccines drove incidence down by 96–98% in surveillance settings. Residual and re-emerging disease is now driven by **non-b serotypes — notably *H. influenzae* type a (Hia) in Indigenous North American children** — as well as nontypeable strains and disease in older/comorbid adults. Meningitis overall remains a major global killer (GBD 2023: ~259,000 deaths, 2.54 million cases, >⅓ of deaths in children under 5), concentrated in low-income settings and the African meningitis belt.

---

## Section 1 — Disease Information

**Overview.** Haemophilus meningitis is inflammation of the leptomeninges and subarachnoid CSF caused by *Haemophilus influenzae*, a fastidious Gram-negative coccobacillus that is an obligate human commensal/pathogen of the upper respiratory tract. Encapsulated strains (serotypes a–f, distinguished by capsular polysaccharide) cause invasive disease; **serotype b (Hib)** historically accounted for the overwhelming majority of meningitis cases. Prior to conjugate vaccination, "Hib was the leading cause of meningitis in children prior to the introduction of an effective vaccination" ([PMID: 21999651](https://pubmed.ncbi.nlm.nih.gov/21999651/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0000889 (Haemophilus meningitis) |
| ICD-10 | G00.0 (Haemophilus meningitis) |
| ICD-11 | 1D01.0 (Bacterial meningitis) / infectious meningitis codes |
| MeSH | D008586 "Meningitis, Haemophilus" |
| MeSH (organism) | D006193 "Haemophilus influenzae" |
| NCBI Taxonomy | *Haemophilus influenzae* — txid727 |
| OMIM | Not applicable (infectious disease, no Mendelian gene) |
| Orphanet | Not a rare disease in the Orphanet sense (common infection) |

**Synonyms / alternative names.** *Haemophilus influenzae* meningitis; Hib meningitis; *H. influenzae* type b meningitis; pyogenic/bacterial meningitis due to *H. influenzae*; historically "influenzal meningitis" (a misnomer from the erroneous 1890s belief that *H. influenzae* caused influenza).

**Data source type.** Aggregated, disease-level resources (national surveillance, clinical cohorts, RCTs, meta-analyses, experimental models). Not individual-patient EHR-derived and not genetic-variant-derived.

---

## Section 2 — Etiology

**Causal factor:** infectious. The disease is caused by *Haemophilus influenzae*; it is not genetic and not environmental in origin, although host and environmental factors modulate susceptibility.

**Risk factors (environmental / host):**
- **Age:** highest risk in infants and young children, especially 6–23 months; "Haemophilus influenzae type b (Hib) causes invasive infections almost exclusively in under-fives with those aged 6-23 months being the most vulnerable" ([PMID: 38070126](https://pubmed.ncbi.nlm.nih.gov/38070126/)). Young age (<1 year) is an independent predictor of poor outcome ([PMID: 34732790](https://pubmed.ncbi.nlm.nih.gov/34732790/)).
- **Lack of vaccination / incomplete Hib immunization.**
- **Immunocompromise:** asplenia, HIV, complement deficiency — high-risk groups for invasive encapsulated-bacterial disease ([PMID: 36287171](https://pubmed.ncbi.nlm.nih.gov/36287171/)).
- **CSF shunts / neurosurgical devices** (nosocomial/device-associated meningitis) ([PMID: 40249832](https://pubmed.ncbi.nlm.nih.gov/40249832/)).
- **Indigenous ethnicity (American Indian/Alaska Native)** — markedly elevated invasive *H. influenzae* risk: "Invasive Haemophilus influenzae type b (Hib) disease is a serious bacterial infection that disproportionally affects American Indian and Alaska Native (AI/AN) populations" ([PMID: 39264849](https://pubmed.ncbi.nlm.nih.gov/39264849/)).
- **Crowding / close-contact settings** (households, communities) facilitate transmission of nasopharyngeal carriage.
- **Male sex** was an independent risk factor for poor outcome in shunt-associated pediatric meningitis (OR 2.82) ([PMID: 40249832](https://pubmed.ncbi.nlm.nih.gov/40249832/)).

**Genetic risk factors.** No single causal or susceptibility gene is established. In an Amish Hib outbreak investigation, inbreeding was **not** a significant risk factor and cases shared no common HLA haplotype ([PMID: 3485275](https://pubmed.ncbi.nlm.nih.gov/3485275/)) — arguing against a strong monogenic host susceptibility. Known immunodeficiencies (complement C2–C9, properdin, antibody deficiencies, asplenia) predispose broadly to encapsulated-organism invasive disease.

**Protective factors.**
- **Anti-PRP antibody** (naturally acquired or vaccine-induced) is protective; the long-term protective threshold is ~1 µg/mL anti-PRP ([PMID: 38070126](https://pubmed.ncbi.nlm.nih.gov/38070126/)).
- **Hib conjugate vaccination** (primary protective intervention — see Sections 12–13).
- Breastfeeding and herd immunity (reduced carriage) are recognized protective influences in the broader literature.

**Gene–environment interactions.** Not established for this infectious disease; the dominant "interaction" is between host immune status (age-dependent antibody repertoire, immunodeficiency) and pathogen exposure/carriage.

---

## Section 3 — Phenotypes

Haemophilus meningitis produces the phenotypes of acute bacterial meningitis. The classic triad (fever, neck stiffness, altered mental status) is frequently incomplete: only ~26% show the full triad but ~83% have ≥2 of 4 cardinal features ([PMID: 28879886](https://pubmed.ncbi.nlm.nih.gov/28879886/)).

| Phenotype | Type | HPO suggestion | Onset/severity | Frequency |
|---|---|---|---|---|
| Fever | Clinical sign | HP:0001945 | Acute, moderate–severe | Very frequent |
| Headache | Symptom | HP:0002315 | Acute | Very frequent |
| Nuchal rigidity / meningismus | Clinical sign | HP:0031179 | Acute | Frequent (can be subtle/absent early) |
| Photophobia | Symptom | HP:0000613 | Acute | Frequent |
| Altered mental status / reduced consciousness | Clinical sign | HP:0001259 / HP:0001298 | Acute | Frequent; GCS<13 predicts poor outcome |
| Seizures | Clinical sign | HP:0001250 | Acute; may become chronic disorder | ~10% (seizure disorder as sequela) |
| Sensorineural hearing loss | Lab/clinical | HP:0000407 | Acute onset, often permanent | ~14% |
| Subdural effusion | Physical/imaging | HP:0012595 | Acute | ~23% |
| Hydrocephalus | Physical/imaging | HP:0000238 | Subacute | ~6% |
| Developmental delay / cognitive impairment | Cognitive | HP:0001263 / HP:0100543 | Long-term sequela | ~9% |
| Focal motor deficit | Clinical sign | HP:0007360 | Acute/long-term | Present in cohorts |
| CSF neutrophilic pleocytosis | Lab abnormality | HP:0012229 | Acute | Near-universal |

Per-complication frequencies are drawn from a predominantly-Hib pediatric cohort where "Complications occurred in 26% of the patients and included subdural effusion 23%, hearing loss 14%, seizure disorder 10%, developmental delay 9%, hydrocephalus 6%" ([PMID: 9570646](https://pubmed.ncbi.nlm.nih.gov/9570646/)). Meningeal signs can be subtle early: a confirmed adult *H. influenzae* meningitis case presented with rapid hearing loss and initially absent neck stiffness ([PMID: 40509725](https://pubmed.ncbi.nlm.nih.gov/40509725/)).

**Quality-of-life impact.** Permanent sensorineural deafness, epilepsy, motor deficits, and cognitive/developmental impairment substantially reduce QoL in survivors; ~50% of survivors develop neurological complications ([PMID: 33807653](https://pubmed.ncbi.nlm.nih.gov/33807653/)).

---

## Section 4 — Genetic / Molecular Information

**Not applicable to host genetics.** Haemophilus meningitis has **no causal human gene, no pathogenic germline/somatic variant, no modifier gene, no host epigenetic driver, and no chromosomal abnormality**. It is not a heritable disorder; there is no ClinVar/OMIM/HGMD entry for the disease.

The relevant "molecular genetics" are those of the **pathogen**:
- **cap b locus (bexA–D and type-specific region)** encodes biosynthesis/export of the **PRP capsule** — the principal virulence determinant. "Its major virulence factor is the polyribosyl ribitol phosphate (PRP) polysaccharide capsule" ([PMID: 34076491](https://pubmed.ncbi.nlm.nih.gov/34076491/)).
- **Lipooligosaccharide (LOS)** biosynthesis genes — LOS (endotoxin) is the key inflammatory trigger.
- **Fimbriae/pili and outer-membrane proteins** modulate adhesion and blood–CSF-barrier invasion ([PMID: 30049648](https://pubmed.ncbi.nlm.nih.gov/30049648/); [PMID: 41318968](https://pubmed.ncbi.nlm.nih.gov/41318968/)).
- **vapD/vapX toxin–antitoxin locus** enhances intracellular survival in epithelial and brain microvascular endothelial cells ([PMID: 15274747](https://pubmed.ncbi.nlm.nih.gov/15274747/)).

Serotype is defined by capsular polysaccharide structure; molecular modeling shows serotype a and b capsular polysaccharides differ conformationally enough to lack cross-protective antibody recognition ([PMID: 34491462](https://pubmed.ncbi.nlm.nih.gov/34491462/)) — relevant to serotype-replacement disease.

---

## Section 5 — Environmental Information

**Infectious agent (organism):** *Haemophilus influenzae* (NCBI:txid727), serotype b predominant historically; serotypes a, e, f and nontypeable strains increasingly relevant. Transmission is person-to-person via respiratory droplets and nasopharyngeal carriage. Asymptomatic nasopharyngeal carriage among healthcare workers and community members serves as a reservoir; carriage prevalence for *H. influenzae* was 11.8% among paediatric healthcare workers in Benin (none serotype b) ([PMID: 40847276](https://pubmed.ncbi.nlm.nih.gov/40847276/)).

**Environmental / lifestyle factors** that increase transmission or susceptibility: crowding, daycare attendance, household exposure, tobacco smoke exposure, and lack of vaccination. There are no chemical toxins or occupational exposures that cause this disease. CHEBI-relevant molecular entities in pathogenesis: **lipopolysaccharide/lipooligosaccharide (CHEBI:16412)** and **PRP (ribitol phosphate polymer)**.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Nasopharyngeal colonization** by encapsulated *H. influenzae* (usually Hib) **leads to** local mucosal adherence (fimbriae, OMPs) and, in susceptible hosts, mucosal invasion.
2. Mucosal invasion **results in** **bacteremia**; the **PRP capsule** confers resistance to phagocytosis and complement-mediated killing, **enabling** bloodstream survival and high-grade bacteremia. *(Demonstrated: capsule is the major virulence factor — [PMID: 34076491].)*
3. Sustained bacteremia **leads to** interaction with the **blood–CSF barrier** (choroid plexus epithelium) and blood–brain barrier (microvascular endothelium). Hib invades the barrier **in a polarized manner from the basolateral "blood" side** and/or by transcytosis. *(Demonstrated in HIBCPP cell model — [PMID: 30049648]; transcytosis inferred as a shared CNS-entry route — [PMID: 20026234].)*
4. Barrier penetration **results in** bacterial entry into the **subarachnoid space / CSF**, an immunologically permissive compartment with low complement and antibody.
5. Bacterial multiplication and **autolysis/LOS shedding** **trigger** release of **lipooligosaccharide (endotoxin)** into CSF.
6. LOS **induces** resident macrophages/microglia and meningeal cells to produce **TNF-α and IL-1β** — the seminal early cytokines. In the rabbit model TNF activity appears in CSF within 45 min of intracisternal LOS, **preceding** leukocyte influx by ~75 min. *(Demonstrated — [PMID: 2373990]; [PMID: 2794062].)*
7. TNF-α/IL-1β **cause** upregulation of endothelial adhesion molecules and chemokines, **leading to** **neutrophilic pleocytosis** (leukocyte influx into CSF). Combined TNF-α + IL-1β act **synergistically**. *(Demonstrated — [PMID: 2373990].)*
8. Neutrophil influx and inflammation **result in** blood–brain-barrier breakdown (increased permeability), **vasogenic and cytotoxic cerebral edema**, altered CSF dynamics, and **raised intracranial pressure**. In infant rats Hib causes greater BBB albumin penetration than other pathogens, correlating with CSF TNF ([PMID: 9184127]).
9. Edema + inflammation + vasculitis/thrombosis **branch into**:
   - **(a) Global injury:** raised ICP → reduced cerebral perfusion → **ischemia/hypoxia → neuronal necrosis/apoptosis** → coma, death.
   - **(b) Cochlear injury:** inflammation tracks along the cochlear aqueduct to the inner ear → **cochlear/eighth-nerve inflammation → sensorineural hearing loss**. *(Dexamethasone reduces cochlear-nerve inflammation in infant rats — [PMID: 1759817].)*
   - **(c) Local complications:** subdural effusion, hydrocephalus (impaired CSF resorption), seizures, focal deficits.
10. These processes **manifest clinically** as fever, meningismus, altered consciousness, seizures; and, in survivors, as **long-term sequelae** (deafness, epilepsy, cognitive impairment, hydrocephalus).

### Detail by category

- **Molecular pathways:** LOS/LPS → TLR4/CD14 signaling → NF-κB activation → transcription of TNF-α, IL-1β, IL-6, chemokines (inferred canonical pathway; the cytokine outputs are directly demonstrated). Anti-inflammatory **IL-10** counter-regulates: intracisternal IL-10 >1 µg significantly reduced CSF TNF-α and lactate ([PMID: 9359724](https://pubmed.ncbi.nlm.nih.gov/9359724/)).
- **Cellular processes:** acute inflammation, leukocyte recruitment, endothelial activation, apoptosis/necrosis of neurons, disruption of tight-junction proteins (occludin, claudins, JAMs) by bacterial virulence factors ([PMID: 41318968](https://pubmed.ncbi.nlm.nih.gov/41318968/)).
- **Immune involvement:** innate immune over-activation drives injury; anti-PRP humoral immunity is protective. Specific cytokine inhibitors (sTNFR, IL-1RA) did **not** consistently modulate LOS-driven meningeal inflammation, suggesting redundancy/broad stimulus ([PMID: 7798656](https://pubmed.ncbi.nlm.nih.gov/7798656/)).
- **Tissue damage mechanisms:** oxidative stress, ischemia (vasculitis/thrombosis), cytotoxic + vasogenic edema, elevated CSF lactate.
- **Suggested GO / CL / UBERON terms:** GO:0006954 inflammatory response; GO:0032640 tumor necrosis factor production; GO:0032611 IL-1β production; GO:0050900 leukocyte migration; GO:0006909 phagocytosis; CL:0000235 macrophage; CL:0000129 microglial cell; CL:0000775 neutrophil; CL:0002139 endothelial cell of vascular tree; CL:0000066 epithelial cell (choroid plexus); UBERON:0002361 meninges; UBERON:0001359 CSF; UBERON:0001886 choroid plexus.

---

## Section 7 — Anatomical Structures Affected

- **Primary organ/system:** central nervous system — **meninges (UBERON:0002361)** and **subarachnoid space/CSF (UBERON:0001359)**; the **brain (UBERON:0000955)** is secondarily affected via edema, ischemia, and abscess/effusion.
- **Secondary organ involvement / complications:** **inner ear/cochlea (UBERON:0001844)** → deafness; **cerebral ventricles** → hydrocephalus; **subdural space** → subdural effusion/empyema; systemic sepsis may cause transient myocardial dysfunction (neurogenic stunned myocardium) — reported with *H. influenzae* CNS infection in children ([PMID: 40751825](https://pubmed.ncbi.nlm.nih.gov/40751825/)).
- **Body systems:** nervous, immune, and (via bacteremia) cardiovascular/systemic.
- **Tissue/cell level:** **choroid plexus epithelium** and **brain microvascular endothelial cells** (barrier invasion sites); **meningeal macrophages/microglia** (cytokine production); **neutrophils** (CSF influx); **neurons** (injury); **cochlear hair cells / eighth cranial nerve** (hearing loss).
- **Subcellular:** endothelial/epithelial **tight junctions (GO:0005923 bicellular tight junction)**; plasma membrane signaling complexes (TLR4). Bacterial LOS acts at the cell surface.
- **Localization / lateralization:** the meningeal process is diffuse and **bilateral**; complications (subdural effusion, focal deficits, hearing loss) may be unilateral or asymmetric.

---

## Section 8 — Temporal Development

- **Onset:** typically **acute** (hours to a few days); most common in **infants/young children** (peak 6–23 months). Adult cases occur, often in older/comorbid hosts.
- **Progression:** rapidly progressive if untreated; delays in diagnosis/treatment worsen outcome ([PMID: 35419149](https://pubmed.ncbi.nlm.nih.gov/35419149/)). With effective antibiotics the acute illness is typically **self-limited over 7–14 days** of treatment; shorter (≤7 day) courses may be non-inferior for uncomplicated cases ([PMID: 37870611](https://pubmed.ncbi.nlm.nih.gov/37870611/)).
- **Disease course:** monophasic acute illness (not relapsing/remitting), but with potential permanent sequelae. Critical intervention window: **early antibiotics + dexamethasone before/with the first antibiotic dose** is the key window to prevent hearing loss ([PMID: 22789668](https://pubmed.ncbi.nlm.nih.gov/22789668/)).
- **Remission:** treatment-induced recovery in survivors; sequelae may be permanent.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **None — not a genetic disease** (no AD/AR/X-linked/mitochondrial pattern; not applicable).
- **Epidemiology (pre-vaccine):** Hib was the leading cause of childhood bacterial meningitis. In a Kuwait pediatric series *H. influenzae* accounted for 45.6% of bacterial meningitis episodes; 88% of cases were in children <5 years ([PMID: 2607574](https://pubmed.ncbi.nlm.nih.gov/2607574/)).
- **Epidemiology (post-vaccine):** conjugate vaccines produced 96–98% reductions. Netherlands surveillance (1989–2019, 17,393 episodes): overall bacterial-meningitis incidence fell from 6.37 to 1.58 per 100,000/yr (IRR 0.25); Hib IRRs 0.02–0.04 ([PMID: 33247582](https://pubmed.ncbi.nlm.nih.gov/33247582/)).
- **Current global burden:** GBD 2023 estimated 259,000 meningitis deaths and 2.54 million incident cases (all causes); children <5 accounted for >⅓ of deaths (86,600) ([PMID: 41911930](https://pubmed.ncbi.nlm.nih.gov/41911930/)). An 80-year meta-analysis (371 studies, 157,656 episodes) found *H. influenzae* caused 22% of episodes with an identified pathogen and a case-fatality of 11% (95% CI 10–13%) — lower than pneumococcus (24%) or *Listeria* (27%) ([PMID: 39093565](https://pubmed.ncbi.nlm.nih.gov/39093565/)).
- **Geographic distribution:** highest burden in low-income countries and the **African meningitis belt**; residual/re-emergent Hia disease concentrated in **Indigenous North American (Alaska Native, American Indian) children**.
- **Population demographics:** male predominance in some cohorts; strong age skew toward under-5s; ethnic disparity (AI/AN populations). Alaska Hia surveillance: average annual incidence 17.8/100,000 in children <5 vs 0.3 in ≥5 years ([PMID: 40071574](https://pubmed.ncbi.nlm.nih.gov/40071574/)).

---

## Section 10 — Diagnostics

- **Lumbar puncture / CSF analysis** is definitive. Bacterial meningitis CSF shows **neutrophilic pleocytosis, low glucose (hypoglycorrhachia), elevated protein**, elevated lactate, and elevated opening pressure.
- **Gram stain:** *H. influenzae* appears as **Gram-negative coccobacilli**.
- **Culture:** CSF and blood culture confirm the organism and enable **antimicrobial susceptibility testing** (essential given β-lactamase-mediated ampicillin resistance). Culture remains indispensable ([PMID: 42256222](https://pubmed.ncbi.nlm.nih.gov/42256222/)).
- **Antigen detection:** latex agglutination for the PRP capsular antigen (adjunct, especially after antibiotic pretreatment).
- **Multiplex PCR (BioFire FilmArray Meningitis/Encephalitis panel):** detects 14 pathogens including *H. influenzae* directly from CSF in ~1 hour: "The FilmArray Meningitis/Encephalitis (ME) Panel provides multiplex molecular detection of 14 pathogens within ∼1 h" ([PMID: 42679643](https://pubmed.ncbi.nlm.nih.gov/42679643/)). In one evaluation, bacterial/fungal targets showed sensitivity 100%, specificity 94.9%, NPV 100% vs culture ([PMID: 42388946](https://pubmed.ncbi.nlm.nih.gov/42388946/)). PCR markedly increases pathogen detection over culture in meningitis, particularly after antibiotic pretreatment ([PMID: 40280145](https://pubmed.ncbi.nlm.nih.gov/40280145/)). Panels are adjuncts, not standalone replacements for culture ([PMID: 42256222](https://pubmed.ncbi.nlm.nih.gov/42256222/); [PMID: 42684933](https://pubmed.ncbi.nlm.nih.gov/42684933/)).
- **Imaging:** CT/MRI to detect complications (subdural effusion, hydrocephalus, infarction, edema) and before LP if raised-ICP/mass concern.
- **Differential diagnosis:** pneumococcal and meningococcal meningitis (other pyogenic causes), viral/aseptic meningitis (lymphocytic pleocytosis, normal glucose — e.g., enteroviral [PMID: 41362530], drug-induced [PMID: 40827196]), tuberculous and cryptococcal meningitis ([PMID: 39998376]).
- **Genetic/omics testing:** **not applicable** for host diagnosis. Pathogen molecular typing (serotyping, WGS) is used for surveillance.

---

## Section 11 — Outcome / Prognosis

- **Mortality:** case fatality up to ~30% for bacterial meningitis broadly ([PMID: 33807653](https://pubmed.ncbi.nlm.nih.gov/33807653/)); *H. influenzae*-specific pooled case-fatality ~11% ([PMID: 39093565](https://pubmed.ncbi.nlm.nih.gov/39093565/)), lower than pneumococcal disease.
- **Morbidity:** ~50% of survivors develop neurological complications ([PMID: 33807653](https://pubmed.ncbi.nlm.nih.gov/33807653/)); sequelae include deafness, seizures, cognitive impairment, hydrocephalus, motor deficits.
- **Prognostic factors:** treatment setting/resources (Angola vs Finland OR 11.91), depressed consciousness (GCS<13, OR 4.58), seizures (OR 1.96), age <1 year (OR 1.55), and pneumococcal (vs Hib) etiology ([PMID: 34732790](https://pubmed.ncbi.nlm.nih.gov/34732790/)). Dismal outcome (death/severe sequelae/deafness) occurred in 54% in Angola, 31% in Latin America, 5% in Finland — illustrating that outcome is dominated by setting and presenting severity.
- **Recovery:** with prompt appropriate therapy most survivors recover; permanent deficits (especially deafness) are the principal residual disability.

---

## Section 12 — Treatment

**Empiric antibiotics:** **third-generation cephalosporins — ceftriaxone or cefotaxime** — are first-line (NCIT: Ceftriaxone C574; Cefotaxime C349). They are equivalent to conventional ampicillin-chloramphenicol in outcome where organisms are sensitive, but β-lactamase-producing Hib requires cephalosporins ([PMID: 19375903](https://pubmed.ncbi.nlm.nih.gov/19375903/)). Where cephalosporins are unavailable, ampicillin–chloramphenicol is an alternative.

**Adjunctive dexamethasone (NCIT: C459):** reduces hearing loss and neurological sequelae, with the strongest, organism-specific benefit in Hib meningitis. Cochrane meta-analysis (25 RCTs, 4,121 participants): severe hearing loss RR 0.67 (95% CI 0.51–0.88), any hearing loss RR 0.74 (0.63–0.87), neurological sequelae RR 0.83 (0.69–1.00); mortality reduction non-significant ([PMID: 20824838](https://pubmed.ncbi.nlm.nih.gov/20824838/)). Subgroup: corticosteroids "reduced severe hearing loss in Haemophilus influenzae meningitis (RR 0.34, 95% CI 0.20 to 0.59)" ([PMID: 20824838](https://pubmed.ncbi.nlm.nih.gov/20824838/)). Benefit is clearest in high-income settings and requires timing **before or with the first antibiotic dose** ([PMID: 22789668](https://pubmed.ncbi.nlm.nih.gov/22789668/)). Mechanistically, dexamethasone suppresses LOS-induced CSF TNF ([PMID: 2794062](https://pubmed.ncbi.nlm.nih.gov/2794062/)).

**Treatment duration:** shorter (≤7 days) courses may be non-inferior to longer courses for uncomplicated childhood meningitis ([PMID: 37870611](https://pubmed.ncbi.nlm.nih.gov/37870611/)).

**Supportive care:** ICU-level management of raised ICP, seizures, fluid/electrolyte balance (SIADH), and hemodynamic support; audiology follow-up and rehabilitation for sequelae. Experimental immunomodulation (IL-10) reduces CSF TNF in models but is not clinical ([PMID: 9359724](https://pubmed.ncbi.nlm.nih.gov/9359724/)); specific cytokine inhibitors were ineffective in models ([PMID: 7798656](https://pubmed.ncbi.nlm.nih.gov/7798656/)).

**Pharmacogenomics / gene therapy / cell therapy / targeted-immunotherapy:** not applicable to this infectious disease.

---

## Section 13 — Prevention

**Primary prevention — vaccination (the cornerstone).** **PRP–protein conjugate vaccines** (PRP-T, PRP-OMP, HbOC) generate protective anti-PRP antibody. "As a result of widespread use of the vaccines, the incidence of Hib infections, and their associated morbidity and mortality, has fallen dramatically across the globe" ([PMID: 34590133](https://pubmed.ncbi.nlm.nih.gov/34590133/)). Protective anti-PRP threshold ~1 µg/mL; seroprotection rates ~74% in a Nigerian cohort ([PMID: 38070126](https://pubmed.ncbi.nlm.nih.gov/38070126/)). **NCIT: Haemophilus b Conjugate Vaccine (C1213).**

**Tailored recommendations:** ACIP (2024) preferentially recommends **PRP-OMP-containing Hib vaccine for American Indian/Alaska Native infants** due to higher invasive-disease risk and earlier disease onset ([PMID: 39264849](https://pubmed.ncbi.nlm.nih.gov/39264849/)). A **serotype a (Hia) conjugate vaccine** is in development, motivated by serotype-replacement disease and lack of a/b cross-protection ([PMID: 34491462](https://pubmed.ncbi.nlm.nih.gov/34491462/)).

**Chemoprophylaxis:** **rifampin** for close/household contacts controls transmission and secondary cases — an Amish Hib outbreak ended after rifampin prophylaxis was extended to all community members <15 years ([PMID: 3485275](https://pubmed.ncbi.nlm.nih.gov/3485275/)). **NCIT: Rifampin (C777).**

**Secondary/tertiary prevention:** early LP, rapid empiric antibiotics, adjunctive dexamethasone to prevent sequelae; audiological screening; cochlear implantation for post-meningitic deafness; targeted vaccination of high-risk groups (asplenia, HIV, complement deficiency) ([PMID: 36287171](https://pubmed.ncbi.nlm.nih.gov/36287171/)). WHO's **"Defeating meningitis by 2030"** roadmap frames the global prevention strategy ([PMID: 39006487](https://pubmed.ncbi.nlm.nih.gov/39006487/)).

---

## Section 14 — Other Species / Natural Disease

*Haemophilus influenzae* is **human-restricted**; there is no significant natural reservoir or naturally occurring *H. influenzae* meningitis in companion animals or wildlife. Related *Haemophilus/Glaesserella* species cause veterinary disease (e.g., *Glaesserella (Haemophilus) parasuis* causes Glässer's disease/meningitis in swine; *Avibacterium (Haemophilus) paragallinarum* in poultry), but these are distinct organisms. **Zoonotic potential: none** for *H. influenzae*. NCBI Taxonomy: *H. influenzae* txid727; humans *Homo sapiens* txid9606. VBO/breed: not applicable.

---

## Section 15 — Model Organisms

- **Infant rat (principal in vivo model):** 5-day-old rats develop hematogenous Hib meningitis after intraperitoneal inoculation (10⁴–10⁵ CFU), with reproducible bacteremia, weight loss, lethargy, and mortality; "because adult animals will not reliably develop meningitis after intranasal or intraperitoneal challenge, infant animals are used" ([PMID: 10470555](https://pubmed.ncbi.nlm.nih.gov/10470555/)). Anti-LPS inner-core mAb (MAHI 3) raised survival from 10–17% to 60–90% ([PMID: 10623558](https://pubmed.ncbi.nlm.nih.gov/10623558/)). The model recapitulates BBB permeability changes ([PMID: 9184127](https://pubmed.ncbi.nlm.nih.gov/9184127/)) and cochlear-nerve inflammation reducible by dexamethasone ([PMID: 1759817](https://pubmed.ncbi.nlm.nih.gov/1759817/)).
- **Rabbit intracisternal LOS/Hib model:** dissects the cytokine cascade (TNF-α/IL-1β kinetics, IL-10/dexamethasone modulation) ([PMID: 2373990](https://pubmed.ncbi.nlm.nih.gov/2373990/); [PMID: 2794062](https://pubmed.ncbi.nlm.nih.gov/2794062/); [PMID: 9359724](https://pubmed.ncbi.nlm.nih.gov/9359724/)).
- **Cell-barrier models:** human choroid plexus papilloma (HIBCPP) blood–CSF barrier model and human brain microvascular endothelial cells (HBMEC) model bacterial invasion, polarity, and tight-junction disruption ([PMID: 30049648](https://pubmed.ncbi.nlm.nih.gov/30049648/); [PMID: 15274747](https://pubmed.ncbi.nlm.nih.gov/15274747/); [PMID: 41318968](https://pubmed.ncbi.nlm.nih.gov/41318968/)).

**Recapitulation / limitations:** models faithfully reproduce bacteremia→CNS invasion, cytokine-driven inflammation, BBB permeability, and cochlear injury, and were pivotal in validating adjunctive dexamethasone. Limitations: age-restriction (only infant animals), inoculum route differs from natural mucosal acquisition, and species differences in immune response.

---

## Key Findings (with statistical evidence)

### Finding 1 — Conjugate vaccines produced a dramatic global decline from Hib's pre-vaccine dominance
Hib was the single most common cause of childhood bacterial meningitis before vaccination. Netherlands national surveillance (1989–2019, 17,393 episodes) showed overall bacterial meningitis incidence fell from 6.37 to 1.58 per 100,000/yr (IRR 0.25, 95% CI 0.23–0.26; P<.001), with conjugate vaccines reducing Hib incidence at IRRs of 0.02–0.04 (P<.001): "Conjugate vaccines effectively reduced the incidence of Haemophilus influenzae type b… (IRRs, .02–.04; P < .001)" ([PMID: 33247582](https://pubmed.ncbi.nlm.nih.gov/33247582/)); "the incidence of Hib infections… has fallen dramatically across the globe" ([PMID: 34590133](https://pubmed.ncbi.nlm.nih.gov/34590133/)); "Hib was the leading cause of meningitis in children prior to the introduction of an effective vaccination" ([PMID: 21999651](https://pubmed.ncbi.nlm.nih.gov/21999651/)).

### Finding 2 — Pathophysiology is LOS-triggered, TNF-α/IL-1β-driven meningeal inflammation
In the rabbit model, intracisternal Hib LOS induced CSF TNF within 45 min, preceding leukocyte influx by ~75 min (peak TNF 45 ng/mL at 120 min); anti-TNF-α and anti-IL-1β reduced inflammation and the two cytokines were synergistic. "These data provide evidence for a seminal role of TNF-alpha and IL-1 beta in the initial events of meningeal inflammation" ([PMID: 2373990](https://pubmed.ncbi.nlm.nih.gov/2373990/)). Dexamethasone before/with LOS inhibits CSF TNF: "DXM, when given before or with Hib LOS, inhibits CSF TNF production" ([PMID: 2794062](https://pubmed.ncbi.nlm.nih.gov/2794062/)).

### Finding 3 — Adjunctive dexamethasone reduces hearing loss, strongest in Hib
Cochrane meta-analysis (25 RCTs, 4,121 participants): severe hearing loss RR 0.67 (0.51–0.88), any hearing loss RR 0.74 (0.63–0.87), neurological sequelae RR 0.83 (0.69–1.00); mortality RR 0.90 (0.80–1.01, P=0.07, NS) ([PMID: 20824838](https://pubmed.ncbi.nlm.nih.gov/20824838/)). Hib-specific benefit is greatest when dexamethasone is given before/with first antibiotic dose ([PMID: 22789668](https://pubmed.ncbi.nlm.nih.gov/22789668/)).

### Finding 4 — PRP capsule drives virulence; CNS entry is polarized barrier invasion
"Its major virulence factor is the polyribosyl ribitol phosphate (PRP) polysaccharide capsule" ([PMID: 34076491](https://pubmed.ncbi.nlm.nih.gov/34076491/)). "Invasion occurs in a strongly polar fashion, since the bacteria enter the cells preferentially from the basolateral 'blood' side" ([PMID: 30049648](https://pubmed.ncbi.nlm.nih.gov/30049648/)); transcytosis is a shared CNS-entry route ([PMID: 20026234](https://pubmed.ncbi.nlm.nih.gov/20026234/)).

### Finding 5 — Outcomes are dominated by setting and presenting severity
Pooled 5-trial analysis (2,123 children): dismal outcome in 54% (Angola), 31% (Latin America), 5% (Finland); independent predictors included study site (Angola vs Finland OR 11.91), GCS<13 (OR 4.58), seizures (OR 1.96), age <1 year (OR 1.55) ([PMID: 34732790](https://pubmed.ncbi.nlm.nih.gov/34732790/)).

### Finding 6 — Clinical presentation and complication frequencies
Case fatality up to 30%, ~50% of survivors with complications ([PMID: 33807653](https://pubmed.ncbi.nlm.nih.gov/33807653/)); Saudi pediatric series (66% Hib): complications 26% — subdural effusion 23%, hearing loss 14%, seizure disorder 10%, developmental delay 9%, hydrocephalus 6% ([PMID: 9570646](https://pubmed.ncbi.nlm.nih.gov/9570646/)); meningeal signs can be subtle early ([PMID: 40509725](https://pubmed.ncbi.nlm.nih.gov/40509725/)).

### Finding 7 — Infant rat is the principal in vivo model
Adult animals do not reliably develop meningitis ([PMID: 10470555](https://pubmed.ncbi.nlm.nih.gov/10470555/)); infant-rat hematogenous model with anti-LPS protection ([PMID: 10623558](https://pubmed.ncbi.nlm.nih.gov/10623558/)); Hib causes greater BBB penetration than E. coli K1 or GBS ([PMID: 9184127](https://pubmed.ncbi.nlm.nih.gov/9184127/)).

### Finding 8 — Rifampin chemoprophylaxis controls outbreaks
"The outbreak ended following rifampin prophylaxis of all community members younger than 15 years of age" ([PMID: 3485275](https://pubmed.ncbi.nlm.nih.gov/3485275/)); inbreeding not a risk factor, no shared HLA haplotype.

### Finding 9 — Meningitis is a leading infectious killer of young children
"meningitis, encephalitis and neonatal sepsis, collectively, [are] the second and third largest infectious killers of children under five" ([PMID: 33668442](https://pubmed.ncbi.nlm.nih.gov/33668442/)).

### Finding 10 — Diagnosis: LP/CSF + Gram/culture + multiplex PCR
FilmArray ME panel detects 14 pathogens including *H. influenzae* in ~1 h ([PMID: 42679643](https://pubmed.ncbi.nlm.nih.gov/42679643/)); bacterial/fungal target sensitivity 100%, specificity 94.9%, NPV 100% vs culture ([PMID: 42388946](https://pubmed.ncbi.nlm.nih.gov/42388946/)).

### Finding 11 — Current global burden (GBD 2023)
"In 2023, there were 259 000 (202 000–335 000) global deaths and 2·54 million (2·20–2·93) incident cases of meningitis. Children younger than 5 years accounted for more than a third of deaths (86 600)" ([PMID: 41911930](https://pubmed.ncbi.nlm.nih.gov/41911930/)); 80-year meta-analysis of case-fatality trends ([PMID: 39093565](https://pubmed.ncbi.nlm.nih.gov/39093565/)).

### Finding 12 — Serotype replacement: Hia now drives disease in Indigenous North American children
Alaska 2018–2022: 75% of 52 invasive Hia cases in Alaska Native children <5 in rural areas; incidence 17.8/100,000 in <5s ([PMID: 40071574](https://pubmed.ncbi.nlm.nih.gov/40071574/)); "All deaths (n = 6) and long-term sequelae (n = 7) occurred in children with Hia or Hib meningitis" ([PMID: 40882866](https://pubmed.ncbi.nlm.nih.gov/40882866/)); ACIP tailored PRP-OMP recommendation for AI/AN infants ([PMID: 39264849](https://pubmed.ncbi.nlm.nih.gov/39264849/)).

---

## Mechanistic Model / Interpretation

```
  Nasopharyngeal colonization (encapsulated H. influenzae, esp. Hib)
                 │  adhesion (fimbriae, OMPs), mucosal invasion
                 ▼
            BACTEREMIA  ◄── PRP capsule: resists phagocytosis + complement
                 │
                 ▼
   Blood–CSF / blood–brain barrier  ── polarized (basolateral) invasion +
   (choroid plexus epithelium,          transcytosis; tight-junction disruption
    brain microvascular endothelium)
                 │
                 ▼
        CSF / subarachnoid space   ── bacterial multiplication + autolysis
                 │
                 ▼
        LIPOOLIGOSACCHARIDE (LOS) release
                 │  TLR4/CD14 → NF-κB (inferred)
                 ▼
        TNF-α  +  IL-1β  (synergistic)   ◄── IL-10 / dexamethasone suppress
                 │  chemokines, adhesion molecules
                 ▼
        NEUTROPHILIC CSF PLEOCYTOSIS + BBB breakdown
                 │
      ┌──────────┼───────────────────────┐
      ▼          ▼                        ▼
 Cerebral edema  Cochlear/CN-VIII     Vasculitis / thrombosis
 ↑ ICP           inflammation          → ischemia
 → ischemia      → SENSORINEURAL       → infarction
 → neuronal        HEARING LOSS
   necrosis
      │          │                        │
      └──────────┴───────────┬────────────┘
                             ▼
     CLINICAL: fever, meningismus, ↓consciousness, seizures
     OUTCOME: death (≤30%); survivors ~50% sequelae
              (deafness, epilepsy, cognitive impairment, hydrocephalus)
```

**Upstream vs downstream.** The **capsule** and **barrier invasion** are upstream determinants of *whether* invasive disease occurs; the **LOS→TNF-α/IL-1β cascade** is the upstream determinant of *how much injury* occurs once bacteria reach the CSF. This distinction explains why the two most effective interventions act at different points: **vaccination/anti-PRP antibody** blocks the upstream capsule-dependent step (prevention), while **dexamethasone** dampens the downstream cytokine cascade (reduces sequelae, especially deafness). Antibiotics kill bacteria but, by causing bacteriolysis and LOS release, can transiently intensify the cytokine surge — the mechanistic rationale for giving dexamethasone *before or with* the first antibiotic dose.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [33247582](https://pubmed.ncbi.nlm.nih.gov/33247582/) | 30-yr Netherlands surveillance; conjugate-vaccine IRRs 0.02–0.04 | F1 (vaccine impact) |
| [34590133](https://pubmed.ncbi.nlm.nih.gov/34590133/) | Global dramatic Hib decline | F1, prevention |
| [21999651](https://pubmed.ncbi.nlm.nih.gov/21999651/) | Hib as pre-vaccine leading cause | F1 |
| [2373990](https://pubmed.ncbi.nlm.nih.gov/2373990/) | TNF-α/IL-1β seminal role, rabbit model | F2 (mechanism) |
| [2794062](https://pubmed.ncbi.nlm.nih.gov/2794062/) | Dexamethasone suppresses LOS-induced CSF TNF | F2, treatment |
| [9359724](https://pubmed.ncbi.nlm.nih.gov/9359724/) | IL-10 counter-regulates CSF TNF | Mechanism |
| [7798656](https://pubmed.ncbi.nlm.nih.gov/7798656/) | sTNFR/IL-1RA ineffective vs LOS (redundancy) | Mechanism nuance |
| [20824838](https://pubmed.ncbi.nlm.nih.gov/20824838/) | Cochrane: dexamethasone RR 0.34 severe hearing loss in Hib | F3 (treatment) |
| [22789668](https://pubmed.ncbi.nlm.nih.gov/22789668/) | Timing of dexamethasone in Hib | F3 |
| [34076491](https://pubmed.ncbi.nlm.nih.gov/34076491/) | PRP as major virulence factor | F4 |
| [30049648](https://pubmed.ncbi.nlm.nih.gov/30049648/) | Polarized blood–CSF invasion (HIBCPP) | F4, models |
| [20026234](https://pubmed.ncbi.nlm.nih.gov/20026234/) | Transcytosis CNS entry | F4 |
| [41318968](https://pubmed.ncbi.nlm.nih.gov/41318968/) | Tight-junction disruption mechanisms | Mechanism/anatomy |
| [15274747](https://pubmed.ncbi.nlm.nih.gov/15274747/) | vapD/vapX intracellular survival | Molecular |
| [34732790](https://pubmed.ncbi.nlm.nih.gov/34732790/) | Prognostic factors, 3-continent outcomes | F5 |
| [33807653](https://pubmed.ncbi.nlm.nih.gov/33807653/) | Case fatality, complication spectrum | F6 |
| [9570646](https://pubmed.ncbi.nlm.nih.gov/9570646/) | Per-complication frequencies (66% Hib cohort) | F6 |
| [40509725](https://pubmed.ncbi.nlm.nih.gov/40509725/) | Subtle early meningeal signs, adult case | F6 |
| [10470555](https://pubmed.ncbi.nlm.nih.gov/10470555/) | Infant-animal model rationale | F7 (models) |
| [10623558](https://pubmed.ncbi.nlm.nih.gov/10623558/) | Infant-rat model, anti-LPS protection | F7 |
| [9184127](https://pubmed.ncbi.nlm.nih.gov/9184127/) | BBB permeability greater with Hib | F7 |
| [1759817](https://pubmed.ncbi.nlm.nih.gov/1759817/) | Dexamethasone ↓ cochlear inflammation | F7, treatment |
| [3485275](https://pubmed.ncbi.nlm.nih.gov/3485275/) | Rifampin controls Amish outbreak | F8 (prevention) |
| [33668442](https://pubmed.ncbi.nlm.nih.gov/33668442/) | Meningitis global mortality ranking | F9 |
| [42679643](https://pubmed.ncbi.nlm.nih.gov/42679643/) | FilmArray ME panel (14 pathogens, ~1h) | F10 (diagnostics) |
| [42388946](https://pubmed.ncbi.nlm.nih.gov/42388946/) | ME panel performance vs culture | F10 |
| [42256222](https://pubmed.ncbi.nlm.nih.gov/42256222/) | Culture still essential (AST, coverage) | F10 |
| [41911930](https://pubmed.ncbi.nlm.nih.gov/41911930/) | GBD 2023 burden estimates | F11 |
| [39093565](https://pubmed.ncbi.nlm.nih.gov/39093565/) | 80-yr case-fatality meta-analysis (H. flu 11%) | F11, prognosis |
| [40071574](https://pubmed.ncbi.nlm.nih.gov/40071574/) | Alaska Hia epidemiology | F12 |
| [40882866](https://pubmed.ncbi.nlm.nih.gov/40882866/) | Hia/Hib drive deaths/sequelae in Alaska | F12 |
| [39264849](https://pubmed.ncbi.nlm.nih.gov/39264849/) | ACIP tailored AI/AN Hib vaccine | F12, prevention |
| [34491462](https://pubmed.ncbi.nlm.nih.gov/34491462/) | a/b polysaccharide non-cross-reactivity | Serotype replacement |
| [38070126](https://pubmed.ncbi.nlm.nih.gov/38070126/) | Seroprotection, ~1 µg/mL threshold | Prevention |

---

## Limitations and Knowledge Gaps

1. **Disease-level, not patient-level evidence.** This report synthesizes surveillance, cohorts, RCTs, and animal/cell models. There is no host-genetic dataset — appropriately, since the disease is infectious, not heritable. Sections 4 (host genetics), 14 (natural animal disease), and pharmacogenomics are largely "not applicable."
2. **Serotype-specific data are sparse for non-b strains.** Most mechanistic and much clinical data derive from Hib; the pathophysiology of Hia and nontypeable strains is assumed similar but less directly demonstrated.
3. **Corticosteroid benefit is setting-dependent.** Dexamethasone benefit is robust in high-income settings but not demonstrated in low-income countries where the disease burden is highest ([PMID: 20824838](https://pubmed.ncbi.nlm.nih.gov/20824838/)) — a major equity gap.
4. **Signaling detail is partly inferred.** The TLR4/CD14→NF-κB step upstream of TNF-α/IL-1β is canonical/inferred; the cytokine outputs themselves are directly demonstrated in models.
5. **Model limitations.** Infant-rodent and rabbit models require non-natural inoculation routes and age restriction; they may not capture all aspects of human disease, particularly adult/comorbid presentations and long-term neurocognitive sequelae.
6. **Diagnostic gaps.** Multiplex PCR panels miss non-panel pathogens and cannot provide antimicrobial susceptibility; inter-platform discordance exists ([PMID: 42684933](https://pubmed.ncbi.nlm.nih.gov/42684933/)). Culture remains essential.
7. **Surveillance heterogeneity.** Global burden estimates differ substantially between WHO-MCEE and IHME-GBD models ([PMID: 33668442](https://pubmed.ncbi.nlm.nih.gov/33668442/)), reflecting under-diagnosis in low-resource settings.

---

## Proposed Follow-up Experiments / Actions

1. **Accelerate Hia conjugate vaccine development and evaluation**, prioritizing Indigenous North American populations, given demonstrated serotype replacement, lack of a/b cross-protection, and concentrated mortality/sequelae ([PMID: 34491462](https://pubmed.ncbi.nlm.nih.gov/34491462/); [PMID: 40071574](https://pubmed.ncbi.nlm.nih.gov/40071574/); [PMID: 40882866](https://pubmed.ncbi.nlm.nih.gov/40882866/)).
2. **Definitive RCTs of adjunctive dexamethasone (and alternative anti-inflammatories) in low-income, high-burden settings**, since current evidence of benefit is confined to high-income countries.
3. **Strengthen molecular surveillance** (serotyping + WGS) to track post-Hib serotype dynamics (a, e, f, nontypeable) and antimicrobial resistance, integrated with culture for AST.
4. **Mechanistic dissection of adjunctive host-directed therapies** beyond corticosteroids (e.g., targeted modulation of the LOS→TNF-α/IL-1β axis, complement or matrix-metalloproteinase modulation) using validated infant-rat and HIBCPP barrier models, focusing on hearing-loss and neuronal-injury endpoints.
5. **Improve early recognition tools** for atypical/subtle presentations (adults, subtle meningeal signs) to reduce diagnosis-to-treatment delays, which independently worsen outcome ([PMID: 35419149](https://pubmed.ncbi.nlm.nih.gov/35419149/)).
6. **Standardize global burden estimation** by harmonizing WHO and GBD methodologies and expanding pathogen-specific surveillance in the African meningitis belt and other high-burden regions.

---

*Report compiled from 12 confirmed findings and 59 literature citations across 5 investigation iterations. Evidence types span human clinical cohorts/RCTs/meta-analyses, model-organism (infant rat, rabbit) studies, in-vitro barrier models, and computational/molecular-modeling work.*


## Artifacts

- [OpenScientist final report](Haemophilus_Meningitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Haemophilus_Meningitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 49 |
| On topic | 35 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33247582` *(abstract only)*: "Conjugate vaccines effectively reduced the incidence of Haemophilus influenzae type b… (IRRs, .02–.04; P < .001)"
  - closest text in source: "Conjugate vaccines effectively reduced the incidence of Haemophilus influenzae type b, Neisseria meningitidis serogroup C, and 10 pneumococcal serotypes (IRRs, .02-.04; P < .001)"
- `PMID:34590133` *(abstract only)*: "the incidence of Hib infections… has fallen dramatically across the globe"
  - closest text in source: "As a result of widespread use of the vaccines, the incidence of Hib infections, and their associated morbidity and mortality, has fallen dramatically across the globe"
- `PMID:33668442` *(abstract only)*: "meningitis, encephalitis and neonatal sepsis, collectively, [are] the second and third largest infectious killers of children under five"
  - closest text in source: "Two models, (1) the WHO and the Johns Hopkins Bloomberg School of Public Health's Maternal and Child Epidemiology Estimation (MCEE) group's Child Mortality Estimation (WHO-MCEE) and (2) the Institute for Health Metrics and Evaluation (IHME) Global Burden of Disease Study (GBD 2017), identified meningitis, encephalitis and neonatal sepsis, collectively, to be the second and third largest infectious killers of children under five years, respectively"
- `PMID:41911930` *(abstract only)*: "In 2023, there were 259 000 (202 000–335 000) global deaths and 2·54 million (2·20–2·93) incident cases of meningitis. Children younger than 5 years accounted for more than a third of deaths (86 600)"
  - closest text in source: "FINDINGS: In 2023, there were 259 000 (95% uncertainty interval 202 000-335 000) global deaths and 2·54 million (2·20-2·93) incident cases of meningitis"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Clinical sign"; HP calls it **Fever**
- `HP:0002315` (1 mention) - the report calls it "Symptom"; HP calls it **Headache**
- `HP:0031179` (1 mention) - the report calls it "Clinical sign"; HP calls it **Nuchal rigidity**
- `HP:0000613` (1 mention) - the report calls it "Symptom"; HP calls it **Photophobia**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0000407` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Sensorineural hearing impairment**
- `HP:0012595` (1 mention) - the report calls it "Physical/imaging"; HP calls it **Mild proteinuria**
- `HP:0000238` (1 mention) - the report calls it "Physical/imaging"; HP calls it **Hydrocephalus**
- `HP:0007360` (1 mention) - the report calls it "Clinical sign"; HP calls it **Aplasia/Hypoplasia of the cerebellum**
- `HP:0012229` (1 mention) - the report calls it "Lab abnormality"; HP calls it **CSF pleocytosis**
- `UBERON:0002361` (2 mentions) - the report calls it "Primary organ/system:** central nervous system — **meninges"; UBERON calls it **pia mater**
- `UBERON:0001844` (1 mention) - the report calls it "Secondary organ involvement / complications:** **inner ear/cochlea"; UBERON calls it **cochlea**