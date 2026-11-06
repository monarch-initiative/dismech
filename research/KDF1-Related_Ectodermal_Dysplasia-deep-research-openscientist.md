---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T17:21:47.856032'
end_time: '2026-10-27T17:41:40.041772'
duration_seconds: 1192.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: KDF1-Related Ectodermal Dysplasia
  mondo_id: MONDO:0015024
  category: Mendelian
  causal_genes: KDF1
  omim_id: not recorded
  synonyms: ECTD12; ectodermal dysplasia 12, hypohidrotic/hair/tooth/nail type; KDF1
    ectodermal dysplasia syndrome; ectodermal dysplasia syndrome caused by mutation
    in KDF1
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
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 57
  verified: 52
  not_found: 1
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.019
  labels_checked: 12
  labels_matching: 8
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0001003
    reported_labels:
    - skin/epidermis
    - "Organ/system level:** **integumentary system** is primary \u2014 **skin/epidermis"
    ontology_label: skin epidermis
  - term_id: UBERON:0001091
    reported_labels:
    - teeth / dentition
    ontology_label: calcareous tooth
  labels_variant: 2
  unresolved_terms:
  - HP:0100680
  obsolete_terms:
  - term_id: HP:0001006
    ontology_label: obsolete Hypotrichosis
    replaced_by: HP:0008070
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: KDF1-Related_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KDF1-Related_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KDF1-Related Ectodermal Dysplasia
- **MONDO ID:** MONDO:0015024 (if available)
- **Causal gene(s):** KDF1
- **OMIM:** not recorded
- **Synonyms:** ECTD12; ectodermal dysplasia 12, hypohidrotic/hair/tooth/nail type; KDF1 ectodermal dysplasia syndrome; ectodermal dysplasia syndrome caused by mutation in KDF1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **KDF1-Related Ectodermal Dysplasia** covering all of the
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

# KDF1-Related Ectodermal Dysplasia (Ectodermal Dysplasia 12, ECTD12)
### A Comprehensive Disease Characterization Report

**Causal gene: _KDF1_ (Keratinocyte Differentiation Factor 1).** This report concerns the Mendelian ectodermal dysplasia caused by variants in **_KDF1_** (MONDO:0015024; OMIM phenotype #617337, "Ectodermal dysplasia 12, hypohidrotic/hair/tooth/nail type"). _KDF1_ encodes keratinocyte differentiation factor 1, a cytoplasmic adaptor protein that governs the proliferation-versus-differentiation decision in epidermal/ectodermal progenitor cells. Because many ectodermal dysplasias are numbered serially and caused by different genes (e.g., ECTD1/EDA, ECTD10A/B/EDAR, ECTD11/EDARADD, ECTD2 & many others), this entry follows the identifiers above and specifically addresses the **_KDF1_** disorder, not the more common EDA/EDAR hypohidrotic ectodermal dysplasias.

> **Evidence base note.** This is an ultra-rare disorder described in a handful of families worldwide (first reported 2017). The report is compiled from primary human genetics case reports and from mouse/cell-model mechanistic studies. Evidence source types are flagged throughout as *[human clinical]*, *[mouse]*, *[in vitro/iPSC]*, or *[computational]*. Where disease-level data (epidemiology, survival, formal diagnostic criteria, trials) do not exist, this is stated explicitly.

---

## 1. Disease Information

**Overview.** KDF1-related ectodermal dysplasia is a rare, predominantly **autosomal dominant** form of ectodermal dysplasia affecting derivatives of the embryonic ectoderm — **teeth, hair, nails, sweat glands, and skin**. The reported phenotype is a **hypohidrotic (hypohidrotic/hair/tooth/nail-type) ectodermal dysplasia** with tooth agenesis (hypodontia to anodontia), occasionally natal teeth, sparse hair, nail dystrophy, reduced sweating, and variable skin involvement (palmoplantar keratoderma, atopic dermatitis). An allelic, mechanistically distinct **gain-of-function** phenotype combines ectodermal dysplasia with **hidradenitis suppurativa (HS)**.

**Key identifiers.**
- **Gene:** KDF1 — HGNC:26624; **NCBI Gene ID 126695**; Ensembl **ENSG00000175707**; chromosome **1p36.11**; RefSeq transcript **NM_152365.3**; UniProt **Q8NAX2** (KDF1_HUMAN, 398 aa). Gene OMIM ***616758** (database-verified via mygene/UniProt/ClinVar, Iteration 2).
- **Disease OMIM:** #617337 — *Ectodermal dysplasia 12, hypohidrotic/hair/tooth/nail type (ECTD12)*.
- **MONDO:** MONDO:0015024.
- **Orphanet:** **ORPHA:1810** ("Autosomal dominant hypohidrotic ectodermal dysplasia", MONDO:0015884) is the Orphanet grouping to which KDF1/ECTD12 is annotated (HPO/Monarch, verified Iteration 3); there is no separate ORPHA code specific to the KDF1 subtype.
- **ICD-11:** EC20.0 / LD27.0 range (ectodermal dysplasia, anhidrotic/hypohidrotic); **ICD-10:** Q82.4 (Ectodermal dysplasia, anhidrotic). MeSH: "Ectodermal Dysplasia" (D004476); "Ectodermal Dysplasia 1, Anhidrotic" is a separate descriptor.
- **MeSH gene concept:** KDF1.

**Synonyms:** ECTD12; ectodermal dysplasia 12, hypohidrotic/hair/tooth/nail type; ED-12; KDF1 ectodermal dysplasia syndrome; ectodermal dysplasia syndrome caused by mutation in KDF1.

**Data source type:** Disease-level knowledge is derived from **individual-patient case reports / family pedigrees** (not EHR or aggregated registries). No population-level or EHR-derived datasets exist for this disorder.

---

## 2. Etiology

**Disease causal factor — genetic (monogenic, Mendelian).** The disease is caused by **heterozygous pathogenic variants in _KDF1_**. The founding study mapped and exome-sequenced a multigenerational Saudi family and found the KDF1 variant **c.753C>G (p.Phe251Leu)** that fully co-segregated with autosomal dominant hypohidrotic ectodermal dysplasia *[human clinical]* (Shamseldin et al., 2017, PMID 27838789; variant–paper link confirmed via ClinVar VCV003655049):
> "We describe a multigenerational Saudi family with an autosomal dominant form of hypohidrotic ectodermal dysplasia in which positional mapping and exome sequencing identified a novel variant in KDF1 that fully segregates with the phenotype."

**Genetic risk factors.**
- **Causal variants:** heterozygous missense variants in KDF1 (see §4). Both inherited (autosomal dominant) and **de novo** variants are reported (Manaspon et al., 2019, PMID 30977908; Pan et al., 2022, PMID 35641834 — de novo p.I304N).
- **Modifier genes/susceptibility loci:** KDF1 sits in a TP63-centered regulatory network with IRF6, IKKα (CHUK), RIPK4, and stratifin (SFN); these are candidate genetic modifiers because they share the ectodermal knockout phenotype (Shamseldin 2017, PMID 27838789). No formal GWAS/modifier study exists (ultra-rare disease).

**Environmental risk factors.** None established. As a congenital Mendelian disorder, disease occurrence is determined by the germline variant, not by toxins, lifestyle, or exposures. Sex is not a determinant (autosomal, not X-linked, unlike the common EDA form). Family history is the principal non-molecular risk indicator.

**Protective factors.** No genetic or environmental protective factors are described. (By mechanism, a wild-type/corrected allele is "protective": CRISPR correction of the KDF1 mutation partially rescued cellular phenotypes in iPSC models — Peng 2026, PMID 42267391 *[in vitro]*.)

**Gene–environment interactions.** None documented. The disorder is essentially fully genetically determined; environmental contributions are limited to secondary care issues (e.g., hyperthermia risk from reduced sweating in hot environments).

---

## 3. Phenotypes

All phenotypes are **congenital / developmental** in origin, derived from ectodermal structures. Frequencies below are qualitative given the very small number of reported patients.

| Phenotype | Type | Onset / course | Frequency (reported cohorts) | Suggested HPO term |
|---|---|---|---|---|
| **Tooth agenesis** — hypodontia, oligodontia, up to **anodontia** | Clinical sign / physical | Congenital (tooth development); apparent in childhood | Core, near-universal | HP:0000668 (Hypodontia); HP:0000677 (Oligodontia); HP:0009804 (Anodontia) |
| **Natal / neonatal teeth** | Clinical sign | Present at birth | Recurrent; Keramida 2025 is "third documented case of natal teeth" | HP:0000695 (Natal tooth) |
| **Sparse hair / hypotrichosis** | Physical manifestation | Congenital/infancy | Common | HP:0001006 (Hypotrichosis); HP:0008070 (Sparse hair) |
| **Hypohidrosis / reduced sweating** | Clinical sign (lab-testable by sweat test) | Congenital; lifelong | Characteristic ("hypohidrotic" type) | HP:0000966 (Hypohidrosis) |
| **Nail dystrophy** (e.g., dystrophic toenails) | Physical manifestation | Childhood | Common | HP:0008404 (Nail dystrophy); HP:0008388 (abnormal toenail morphology) |
| **Palmoplantar keratoderma / skin hyperkeratosis** | Physical manifestation | Childhood | Reported | HP:0000982 (Palmoplantar keratoderma) |
| **Atopic dermatitis / eczematous skin** | Clinical sign | Childhood | Reported (Keramida 2025) | HP:0001047 (Atopic dermatitis) |
| **Hidradenitis suppurativa / acne inversa** (esp. gain-of-function allele) | Clinical sign | Adolescence/adulthood | Specific to GoF KDF1 variants | **HP:0040154 (Acne inversa)** / HP:0100680 (Hidradenitis suppurativa) |

**Authoritative HPO annotation set (HPO/Monarch for KDF1 / ECTD12, retrieved Iteration 3).** Beyond the core features above, the curated HPO profile adds craniofacial, skin-appendage, and thermoregulatory terms. Full term list:
- **Dentition:** Hypodontia **HP:0000668**; Natal tooth **HP:0000695**; Premature loss of primary teeth **HP:0006323**; Abnormal dental morphology **HP:0006482**; Abnormality of the dentition **HP:0000164**.
- **Hair:** Sparse hair **HP:0008070**; Sparse lateral eyebrow **HP:0005338**; Sparse body hair **HP:0002231**; Scarring alopecia of scalp **HP:0004552**; Trichorrhexis nodosa **HP:0009886**.
- **Sweat glands / thermoregulation:** Hypohidrosis **HP:0000966**; Hypoplastic sweat glands **HP:0007387**; **Malignant hyperthermia HP:0002047** (thermoregulatory vulnerability).
- **Nails:** Nail dystrophy **HP:0008404**; Abnormal fingernail morphology **HP:0001231**; Subungual hyperkeratosis **HP:0008392**.
- **Skin:** Eczematoid dermatitis **HP:0000964**; Keratosis pilaris **HP:0032152**; Orthokeratosis **HP:0040162**; Thin skin **HP:0000963**; Abnormal skin pigmentation **HP:0001000**; Palmar hyperlinearity **HP:0033252**; Knuckle pad **HP:0032541**.
- **Craniofacial:** Prominent forehead **HP:0011220**; Depressed/Concave nasal ridge **HP:0000457 / HP:0011120**; Short philtrum **HP:0000322**; Thick vermilion border **HP:0012471**; **Cleft palate HP:0000175**.
- **Inheritance:** Autosomal dominant inheritance **HP:0000006**.

Note: *Malignant hyperthermia* (HP:0002047) in the HPO profile likely reflects heat-intolerance/hyperthermia risk secondary to defective sweating rather than classic anesthetic malignant hyperthermia; this distinction should be clarified clinically. *Cleft palate* and the craniofacial dysmorphism broaden the syndrome beyond the simple hair/tooth/nail/sweat tetrad.

Keramida et al. 2025 (PMID 40463401) summarize the carrier-family manifestations *[human clinical]*:
> "Clinical manifestations of the carrier family members included natal teeth at birth, hypodontia, atopic dermatitis and dystrophic toenails."

**Severity & progression.** Variable expressivity even within a family; the dental phenotype ranges from mild hypodontia to severe non-syndromic anodontia (Pan 2022, PMID 35641834). Structural ectodermal defects are **congenital and stable** (non-progressive), though sequelae (dental, thermoregulatory) are lifelong. Hidradenitis suppurativa in GoF cases is a chronic, relapsing inflammatory course.

**Quality-of-life impact.** No formal EQ-5D/SF-36 data for this specific disorder. Expected impacts (by analogy to ectodermal dysplasias): impaired mastication/nutrition and speech and psychosocial burden from tooth agenesis; heat intolerance from hypohidrosis; cosmetic/psychosocial impact of sparse hair and nail dystrophy; substantial morbidity and pain where hidradenitis suppurativa is present.

---

## 4. Genetic / Molecular Information

**Causal gene.** _KDF1_ (Keratinocyte Differentiation Factor 1), 1p36.11; HGNC:26624; NCBI Gene ID **126695**; Ensembl ENSG00000175707; transcript NM_152365.3; protein **UniProt Q8NAX2** (398 aa, cytoplasmic/cell-junction). Mouse ortholog *Kdf1* (NCBI Gene **69073**; MGI:1916323; historically "1810019J16Rik"; Lee 2013, PMID 24075906).

**Pathogenic variants (human).** Reported variants are **heterozygous missense** substitutions that cluster in a **C-terminal functional hotspot (~residues 251–304)** of the 398-aa protein:
- **c.753C>G, p.Phe251Leu** — ClinVar **Pathogenic**; this is the **original index Saudi autosomal-dominant HED family variant** (ClinVar VCV cites Shamseldin 2017, PMID 27838789).
- **c.760C>T, p.His254Tyr** — ClinVar **Likely pathogenic**; ClinVar VCV cites the **gain-of-function hidradenitis-suppurativa report** (Ziegler 2023, PMID 37144643) — an IKKα-stabilizing GoF allele.
- **c.795C>A, p.Asp265Glu** — ClinVar **Likely pathogenic**, Ectodermal dysplasia 12.
- **c.812A>C, p.Lys271Thr (p.K271T)** — autosomal dominant ED-12, 3-generation Greek family (Keramida 2025, PMID 40463401).
- **c.908G>C (reported c.G908C), p.Arg303Pro (p.R303P)** — co-segregating in non-syndromic tooth agenesis (Zeng 2019, PMID 30384154).
- **c.911T>A, p.Ile304Asn (p.I304N)** — **de novo**, severe non-syndromic anodontia (Pan 2022, PMID 35641834).
- Additional variants in the index AD family (Shamseldin 2017, PMID 27838789) and a de novo variant (Manaspon 2019, PMID 30977908) substantiating KDF1 causality.
- **Gain-of-function variants** that stabilize IKKα cause HS + ectodermal dysplasia (Ziegler et al., 2023, PMID 37144643).

**Variant classification (ACMG/AMP) — ClinVar landscape (verified Iteration 2, ~60 KDF1 records).** The gene is **VUS-predominant**: ~47 Uncertain significance, 8 Likely benign, 2 Likely pathogenic, 1 Pathogenic. Confirmed P/LP variants are assigned to **"Ectodermal dysplasia 12, hypohidrotic/hair/tooth/nail type."** Classification relies heavily on co-segregation, de novo occurrence, and functional assays because population data are sparse. This VUS-heavy distribution reflects the gene's recent discovery (2017) and rarity.

**Variant type/class.** Predominantly **missense**. (No large structural/CNV mechanism is established for this disorder.)

**Allele frequency.** Causal variants are **absent or ultra-rare** in gnomAD/1000 Genomes/ExAC, consistent with pathogenicity; no common susceptibility allele is known.

**Somatic vs germline.** **Germline** (constitutional) — inherited or de novo. No somatic/cancer role established for this disease.

**Functional consequences.** Two mechanistically opposite classes converge on the same pathway:
- **Loss-of-function-type / hypomorphic** missense variants impair KDF1's pro-differentiation function → ectodermal dysplasia and tooth agenesis. In vitro, mutant KDF1 shows altered mRNA/protein expression (Pan 2022, PMID 35641834): "In vitro functional studies showed altered mRNA and protein expression levels of the mutant KDF1."
- **Gain-of-function** variants **stabilize IκB kinase α (IKKα)** causing HS + ED (Ziegler 2023, PMID 37144643).

**Population constraint & mechanism inference (gnomAD, verified Iteration 3).** KDF1 is **moderately loss-of-function constrained**: pLI = 0.83, **LOEUF = 0.58**, observed/expected LoF = 0.35 (11 observed vs 31.6 expected; lof_z = 3.11). Missense constraint is only mild (oe_mis = 0.87, mis_z = 1.33). Because (i) heterozygous LoF alleles do occur in population controls, (ii) **all reported pathogenic alleles are missense** clustered at aa ~251–304, and (iii) a defined gain-of-function (IKKα-stabilizing) class exists, the dominant disease mechanism most likely reflects a **dominant-negative or gain-of-function missense effect rather than simple haploinsufficiency** *[computational/population-genetics inference]*. This is consistent with the recessive (homozygous-null) Kdf1 mouse, implying human heterozygous null may be largely subclinical.

**Allele frequency.** Pathogenic alleles are absent/ultra-rare in gnomAD; the gene tolerates some common missense variation (476 observed missense), so classification of novel missense variants requires segregation/functional support.

**Modifier genes.** Candidate modifiers are network partners TP63, CHUK/IKKα, IRF6, RIPK4, SFN (stratifin) (Shamseldin 2017). No quantitative modifier data.

**Epigenetic information / chromosomal abnormalities.** None described for this disorder; no methylation signature or cytogenetic abnormality is implicated. Disease is caused by point variants in a single gene.

---

## 5. Environmental Information

- **Environmental factors / toxins / radiation / occupational exposures:** none implicated — this is a monogenic congenital disorder.
- **Lifestyle factors:** none causal. Relevant only to management (heat avoidance due to hypohidrosis; smoking/obesity are known aggravators of hidradenitis suppurativa in general and would be reasonable to address in GoF-variant patients, though not studied specifically here).
- **Infectious agents:** none. Secondary skin infection can complicate hidradenitis suppurativa lesions but is not a cause of the disorder.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous germline _KDF1_ missense variant** (inherited AD or de novo) alters KDF1 protein function in ectodermal progenitor/keratinocyte lineages. *[human clinical + in vitro]*
2. **Loss-of-function branch:** reduced/altered KDF1 activity **leads to** failure to restrain progenitor proliferation (loss of KDF1-mediated **inhibition of p63**) **and** failure to deliver the pro-differentiation signal. *[mouse]* (Lee 2013)
3. Mechanistically, impaired KDF1 **results in** failure to recruit USP7 and **deubiquitinate/stabilize IKKα**, so IKKα-dependent terminal differentiation signaling is not sustained. *[mouse + in vitro]* (Li 2020)
4. The disturbed **proliferation⇄differentiation balance** in epidermal/ectodermal appendage placodes **leads to** defective morphogenesis of teeth, hair follicles, nails, and eccrine sweat glands. *[mouse, inferred for human]*
5. This **results in** the clinical phenotype: tooth agenesis/natal teeth, hypotrichosis, nail dystrophy, hypohidrosis, and skin keratinization abnormalities. *[human clinical]*

   **Gain-of-function branch (parallel):** IKKα-**stabilizing** _KDF1_ variants **lead to** excess/dysregulated IKKα→NF-κB-pathway activity in follicular/apocrine-gland epithelium, **resulting in** hidradenitis suppurativa combined with ectodermal dysplasia. *[human clinical]* (Ziegler 2023)

6. A newly proposed upstream/parallel contributor (from iPSC modeling): the _KDF1_ mutation **disrupts synaptic structure/signaling and raises excitatory neurotransmitter (NMDA-type) tone**, which may **impede ectodermal organogenesis**; NMDA-receptor antagonism (MK-801) and CRISPR correction partially rescue the defect. *[in vitro/iPSC — inferred, not yet demonstrated in vivo human]* (Peng 2026)

### Supporting detail by category

- **Molecular pathways:** **p63 regulatory network** (KDF1 inhibits p63-driven proliferation); **IKKα / NF-κB (IκB-kinase) signaling** via KDF1–USP7-mediated deubiquitination; the TP63–IRF6–IKKα–RIPK4–stratifin ectodermal-differentiation module. Suggested pathway terms: NF-κB signaling (KEGG/Reactome), keratinization (Reactome R-HSA-6805567).
- **Cellular processes:** regulation of cell proliferation (GO:0042127), keratinocyte/epidermal cell differentiation (GO:0030216), protein deubiquitination (GO:0016579), ectoderm/epidermis development (GO:0007398, GO:0008544), epithelial placode morphogenesis.
- **Protein dysfunction:** KDF1 (398 aa) is a cytoplasmic/cell-junction adaptor-scaffold; pathogenic missense variants cluster in a **C-terminal hotspot (~aa 251–304)** near functional interaction surfaces, impairing or distorting partner binding (USP7, IKKα). Population constraint data (gnomAD: LoF-depleted but missense-tolerant; §4) plus exclusively-missense pathogenic alleles indicate a **dominant-negative** mechanism for the ED phenotype and a **gain-of-function** mechanism (abnormal IKKα stabilization) for the HS phenotype — i.e., altered protein function/interaction rather than mere loss of dosage. Suggested structural resources: UniProt Q8NAX2; AlphaFold model AF-Q8NAX2-F1. UniProt annotates KDF1 as cytoplasmic and cell-junction-localized, "Required both as an inhibitor of basal cell proliferation and a promoter of differentiation of basal progenitor cell progeny."
- **Immune-system involvement:** via **IKKα/NF-κB**, dysregulation produces sterile/chronic inflammatory skin disease (hidradenitis suppurativa) in GoF cases.
- **Tissue damage mechanism:** primarily **developmental (hypoplasia/agenesis)** rather than degenerative — appendages fail to form normally; in HS, chronic follicular occlusion/inflammation drives tissue damage.
- **Biochemical abnormality:** aberrant ubiquitin–proteasome handling of IKKα (loss of USP7-dependent stabilization, or pathological over-stabilization).
- **Molecular profiling:** single-cell RNA-seq of patient iPSC-derived embryoid bodies showed a **shortage of specific cell populations related to synapse structure/signaling** (Peng 2026, PMID 42267391) *[in vitro]*.
- **Functional genomics:** KDF1 was discovered by an **unbiased forward-genetic (ENU) screen** in mouse (Lee 2013); CRISPR correction rescues iPSC phenotypes (Peng 2026).

**Upstream vs downstream:** the KDF1 variant is upstream; p63 de-repression and IKKα destabilization are proximal downstream nodes; appendage dysmorphogenesis and the clinical phenotype are terminal. **Cell types:** keratinocytes (CL:0000312), epidermal basal/progenitor cells (CL:0002187). **GO biological processes:** GO:0030216, GO:0008544, GO:0042127, GO:0016579.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** **integumentary system** is primary — **skin/epidermis** (UBERON:0001003), **hair follicles** (UBERON:0002073), **nails** (UBERON:0001705), **eccrine sweat glands** (UBERON:0002031 / sweat gland UBERON:0001820); **teeth / dentition** (UBERON:0001091). Secondary: apocrine-gland–bearing skin (axillae, groin) in HS. Thermoregulation is impaired secondary to sweat-gland hypoplasia.
- **Tissue/cell level:** **stratified squamous epithelium (epidermis)** and ectodermal-appendage epithelia; affected cells are **keratinocytes** (CL:0000312) and **epidermal progenitor/basal cells** (CL:0002187). Dental epithelium (enamel organ) is affected during odontogenesis.
- **Subcellular level:** **cytoplasm** (KDF1 is cytoplasmic; GO:0005737), with functional impact on **ubiquitin–proteasome machinery** and signaling to the **nucleus** (NF-κB). No mitochondrial/lysosomal involvement implicated.
- **Localization / lateralization:** manifestations are **bilateral and generally symmetric** (congenital developmental distribution); HS affects intertriginous (apocrine) sites bilaterally.

---

## 8. Temporal Development

- **Onset:** **congenital / developmental.** Dental and appendage defects originate during embryonic ectodermal development; natal teeth are present at birth; hypotrichosis, hypohidrosis, and nail changes manifest in infancy/early childhood. HS (GoF allele) typically emerges in adolescence/adulthood.
- **Onset pattern:** insidious/congenital (structural features), with HS following a chronic relapsing course.
- **Progression:** the **ectodermal structural defects are non-progressive/stable** (fixed developmental deficits), lifelong. No "staging" system applies. HS is chronic, relapsing–remitting, and can progress through Hurley stages where present.
- **Disease duration:** chronic, lifelong.
- **Remission:** structural features do not remit; they are managed symptomatically. **Critical window:** the key opportunity for intervention is developmental/early childhood for dental and functional management; the iPSC model raises a speculative prenatal/early neuro-developmental window (NMDA signaling) *[in vitro, unproven clinically]*.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant** (OMIM #617337), with documented **de novo** occurrence. Gene is autosomal (1p36.11) — contrasting with the common X-linked EDA hypohidrotic ED.
- **Penetrance / expressivity:** co-segregation in multigenerational families indicates high penetrance; **expressivity is variable** (ranging from isolated/non-syndromic tooth agenesis to full syndromic ED, even within the same gene/region).
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity:** not specifically established; the index family was consanguineous Saudi (Shamseldin 2017) but AD transmission is the rule. No founder variant reported.
- **Carrier frequency:** not applicable in the recessive sense (dominant disorder); causal alleles are ultra-rare in gnomAD.
- **Epidemiology:** **No prevalence/incidence estimates exist** — the disorder is known from only a few families (Saudi Arabia, China, Greece, and others). It is **ultra-rare**. Ectodermal dysplasias collectively affect ~1 in 10,000–100,000, but KDF1 accounts for a very small fraction.
- **Population demographics / geography:** reported across multiple ethnicities (Middle Eastern, East Asian, European); no demonstrated ethnic predilection or endemic region. **Sex ratio:** expected ~1:1 (autosomal). Age distribution: present from birth, recognized across all ages.

---

## 10. Diagnostics

- **Clinical recognition:** diagnosis is suspected on the clinical triad/tetrad of **tooth agenesis (± natal teeth), sparse hair, nail dystrophy, and hypohidrosis**, with or without skin keratoderma; HS + ED should prompt KDF1 testing for the GoF allele.
- **Genetic testing (confirmatory, the diagnostic gold standard):**
  - **Whole-exome sequencing (WES)** — the method by which KDF1 was discovered and by which most cases are diagnosed (Shamseldin 2017; Keramida 2025; Pan 2022).
  - **Multigene ectodermal-dysplasia / tooth-agenesis panels** including KDF1.
  - **Single-gene (KDF1) sequencing** and **Sanger confirmation/segregation** testing of relatives.
  - **Whole-genome sequencing** useful when panels/WES are negative. CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not indicated** (point-variant, nuclear, autosomal disease).
- **Supporting tests:** dental **panoramic radiography (orthopantomogram)** to document agenesis; **sweat/pilocarpine or starch-iodine sweat test** for hypohidrosis; **skin/dental biopsy** can show the differentiation defect but is not routine. Immunohistochemistry of KDF1 in developing tooth germs supports biological plausibility (Zeng 2019).
- **Omics-based diagnostics:** research-level only (scRNA-seq, functional expression assays). Not used clinically.
- **Biomarkers:** no circulating biomarker; the molecular variant is the biomarker.
- **Clinical criteria:** no disorder-specific standardized diagnostic criteria; diagnosis = compatible phenotype + pathogenic KDF1 variant.
- **Differential diagnosis:** other hypohidrotic ectodermal dysplasias — **EDA (X-linked), EDAR, EDARADD** (XLHED/HED); **WNT10A**-related ED/tooth agenesis; **TP63**-related syndromes (EEC, AEC, Hay–Wells); **IRF6** (Van der Woude/popliteal pterygium); isolated non-syndromic **tooth agenesis** genes (PAX9, MSX1, AXIN2, LRP6). KDF1 is distinguished by autosomal dominant inheritance plus the specific KDF1 variant and the natal-teeth/HS associations.
- **Screening:** **cascade genetic testing** of at-risk relatives once a familial variant is identified; prenatal/preimplantation testing is technically possible for known familial variants.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **normal life expectancy**; this is **not a life-limiting disorder**. No disease-specific mortality. (Caveat: untreated severe hypohidrosis carries a theoretical risk of hyperthermia, well-managed by environmental measures.)
- **Morbidity/function:** morbidity is driven by **dental disability** (mastication, nutrition, speech, aesthetics), **heat intolerance**, **cosmetic/psychosocial** impact (hair, nails), and — in GoF cases — **significant pain, scarring, and disability from hidradenitis suppurativa**.
- **Disease course:** structural defects are stable/lifelong; HS is chronic-relapsing. **Recovery:** structural deficits do not spontaneously resolve but are highly amenable to prosthetic/surgical rehabilitation.
- **Quality-of-life measures:** no disorder-specific instruments reported; generic tools (EQ-5D, SF-36, PROMIS, Oral Health Impact Profile, and DLQI/HS-specific indices for HS) would be applicable.
- **Prognostic factors:** severity of tooth agenesis (hypodontia vs anodontia) and presence/absence of HS are the main determinants of functional burden; genotype (LoF-type vs IKKα-stabilizing GoF) predicts the clinical picture.

---

## 12. Treatment

**There is no disease-modifying or gene-specific therapy; management is supportive, symptomatic, and multidisciplinary.** No approved drug or trial (ClinicalTrials.gov) is specific to KDF1-ED.

- **Dental / oral rehabilitation (central):** pediatric dentures, overdentures, **dental implants** and prosthodontics, orthodontics; management of natal teeth (monitoring vs extraction if aspiration/feeding risk). *NCIT suggestions:* Dental Prosthesis (C50111), Dental Implant (C62701), Orthodontic procedures.
- **Thermoregulation/hypohidrosis:** behavioral cooling, hydration, avoidance of heat/exertion; environmental control.
- **Skin/hair/nails:** emollients and keratolytics for keratoderma; topical care for atopic dermatitis; cosmetic measures/wigs for hypotrichosis; nail care.
- **Hidradenitis suppurativa (GoF cases):** standard HS management — topical/systemic antibiotics, anti-inflammatory therapy, **TNF-α inhibitors (e.g., adalimumab)** and other biologics, and surgical excision of chronic lesions. *NCIT:* Adalimumab (C1876). Given the IKKα/NF-κB mechanism, NF-κB-pathway-directed anti-inflammatory strategies are mechanistically rational (research-level).
- **Pharmacogenomics:** none specific.
- **Advanced/experimental therapeutics:** no gene, cell, or RNA therapy in clinical use. **Proof-of-concept** rescue by **CRISPR correction of the KDF1 variant** and by **NMDA-receptor antagonist MK-801** in patient iPSC models (Peng 2026, PMID 42267391) *[in vitro only; not a clinical therapy]*.
- **Supportive/rehabilitative:** speech therapy, nutritional support, psychological support.
- **Treatment strategy:** individualized, lifelong multidisciplinary care (dentistry/prosthodontics, dermatology, genetics, and — for HS — dermatologic surgery).

---

## 13. Prevention

- **Primary prevention:** not possible for a germline Mendelian disorder; **genetic counseling** and **reproductive options** (prenatal diagnosis, preimplantation genetic testing for a known familial variant) are the principal preventive measures (autosomal dominant → 50% transmission risk from an affected parent).
- **Secondary prevention / early detection:** **cascade genetic testing** of relatives; early dental assessment and intervention; early recognition of natal teeth. Newborn screening does not include KDF1.
- **Tertiary prevention:** prevent complications — maintain hydration/cooling to avoid hyperthermia; early prosthodontic rehabilitation to preserve nutrition/oral function; early HS management to limit scarring/disability.
- **Counseling:** genetic counseling regarding autosomal dominant inheritance, variable expressivity, and de novo occurrence is central (per ACMG/NSGC practice).
- **Immunization / public-health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** mouse *Kdf1* (originally **1810019J16Rik**; NCBI Gene **69073**; MGI:1916323; chromosome 4), highly conserved with human KDF1 (ENSG00000175707). *[mouse]*
- **Natural disease in other species:** no naturally occurring companion-animal or wildlife KDF1 disease is catalogued (OMIA); the disorder is defined in humans and modeled experimentally in mice. Veterinary relevance is limited to experimental models.
- **Comparative biology:** the **Kdf1-/- mouse recapitulates the human ectodermal phenotype**, indicating strong evolutionary conservation of KDF1's role in the proliferation–differentiation balance (Shamseldin 2017; Lee 2013). Comparative pathology shows epidermal hyperproliferation with failed terminal differentiation in mouse mirroring human ectodermal appendage defects.
- **Transmission:** not applicable (non-communicable; no zoonotic potential).

---

## 15. Model Organisms

- **Mouse (primary model):** **Kdf1 knockout / ENU-induced loss-of-function mutant** (Lee, Kong, Weatherbee 2013, PMID 24075906) — discovered KDF1 via forward genetics *[mouse]*:
  > "we identified an essential regulator of the proliferation-differentiation balance in epidermal progenitor cells, the Keratinocyte differentiation factor 1 (Kdf1 … ) gene … Kdf1 mutants display both uncontrolled cell proliferation in the epidermis and failure to develop terminal fates."
  - **Model type:** mammalian germline KO/point mutant; conditional/knock-in models feasible.
  - **Phenotype recapitulation:** **high** — the Kdf1-/- mouse reproduces the human ectodermal phenotype (basis for human causality inference; Shamseldin 2017). Also used to dissect the KDF1–USP7–IKKα mechanism (Li et al. 2020, PMID 32239614).
  - **Limitations:** rodent skin/appendage biology differs from human dentition; dominant human missense (incl. GoF) effects are not fully captured by simple knockouts.
- **Human iPSC / organoid models (in vitro):** patient-derived iPSCs, embryoid bodies, epidermal-progenitor and neuronal differentiation; scRNA-seq; **CRISPR-corrected isogenic controls** (Peng et al. 2026, PMID 42267391) *[in vitro]*. Applications: mechanism (synaptic/NMDA signaling in ectodermal organogenesis), drug testing (MK-801), and genotype–phenotype dissection. Limitation: in-vitro system; organogenesis only partially modeled.
- **In vitro cell assays:** HEK/keratinocyte overexpression assays comparing wild-type vs mutant KDF1 mRNA/protein levels and interactions (Pan 2022; Li 2020).
- **Resources:** MGI (mouse Kdf1), IMPC/KOMP (knockout resources), Cellosaurus/ATCC (iPSC lines in cited studies).

---

## Evidence Summary (key PMIDs)

| PMID | Year | Contribution | Evidence type |
|---|---|---|---|
| 27838789 | 2017 | KDF1 identified as cause of AD hypohidrotic ED (index Saudi family, variant c.753C>G/p.Phe251Leu); mouse recapitulation | Human + mouse |
| 24075906 | 2013 | Kdf1 forward-genetic discovery; proliferation–differentiation balance; p63 inhibition | Mouse |
| 32239614 | 2020 | KDF1–USP7 deubiquitinates/stabilizes IKKα to drive epidermal differentiation | Mouse + in vitro |
| 30384154 | 2019 | KDF1 c.G908C p.R303P in non-syndromic tooth agenesis (phenotypic heterogeneity) | Human |
| 35641834 | 2022 | De novo c.911T>A p.I304N causing non-syndromic anodontia; functional assays | Human + in vitro |
| 30977908 | 2019 | De novo KDF1 variant substantiating ED causality | Human |
| 37144643 | 2023 | Gain-of-function KDF1 variants → hidradenitis suppurativa + ED via IKKα stabilization | Human |
| 40463401 | 2025 | Novel c.812A>C p.K271T in 3-generation ED-12 family; natal teeth, hypodontia, dystrophic nails, atopic dermatitis | Human |
| 42267391 | 2026 | iPSC model: synaptic/NMDA dysregulation impairs ectodermal organogenesis; CRISPR/MK-801 rescue | In vitro/iPSC |

---

## Supported vs Refuted / Open Hypotheses

- **Supported:** (1) KDF1 heterozygous variants cause autosomal dominant ectodermal dysplasia (ECTD12). (2) KDF1 controls the epidermal proliferation–differentiation decision via p63 inhibition and USP7-mediated IKKα stabilization. (3) A gain-of-function, IKKα-stabilizing allele produces an HS + ED phenotype. (4) The phenotypic spectrum extends to non-syndromic tooth agenesis/anodontia (variable expressivity).
- **Open / not established:** precise penetrance estimates; whether the iPSC-derived "neuronal/NMDA" mechanism operates in vivo in humans; existence of modifier alleles; any natural-disease counterpart in other species; disorder-specific epidemiology, QoL, and prognostic datasets.

## Limitations
Evidence rests on a small number of families and model systems; no population-level epidemiology, controlled trials, or formal natural-history studies exist. Core identifiers (Gene 126695, HGNC:26624, UniProt Q8NAX2, Ensembl ENSG00000175707, NM_152365.3, gene OMIM *616758) and ClinVar P/LP variants were database-verified (Iteration 2); the disease phenotype MIM (#617337) and the index Saudi-family variant (c.753C>G/p.Phe251Leu) were both resolved via HPO/Monarch and ClinVar–PMID cross-linking (Iterations 3–4). Frequencies remain qualitative owing to the very small patient numbers; per-phenotype penetrance percentages cannot be reliably derived from the few reported families.

## Future directions
Expand genotype–phenotype correlation (LoF vs GoF); structural characterization of KDF1 (UniProt Q8NAX2 / AlphaFold AF-Q8NAX2-F1) to map variant effects on USP7/IKKα binding; registry building for epidemiology and natural history; test NF-κB/IKKα-directed therapy in GoF HS cases; validate the iPSC-derived synaptic-signaling mechanism in vivo.


## Artifacts

- [OpenScientist final report](KDF1-Related_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KDF1-Related_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 57 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 12 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001003` (1 mention) - the report calls it "skin/epidermis", "Organ/system level:** **integumentary system** is primary — **skin/epidermis"; UBERON calls it **skin epidermis**
- `UBERON:0001091` (1 mention) - the report calls it "teeth / dentition"; UBERON calls it **calcareous tooth**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0100680` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001006` (obsolete Hypotrichosis) (1 mention) - replaced by `HP:0008070`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0042127` (2 mentions) - the report calls it "Cellular processes:** regulation of cell proliferation"; GO calls it **regulation of cell population proliferation**, and lists "regulation of cell proliferation" among its other names
- `CL:0002187` (2 mentions) - the report calls it "epidermal progenitor/basal cells"; CL calls it **basal cell of epidermis**, and lists "epidermal basal cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001003` - called "skin/epidermis", "Organ/system level:** **integumentary system** is primary — **skin/epidermis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.