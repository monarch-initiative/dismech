---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T15:04:02.579660'
end_time: '2026-10-23T15:32:24.030264'
duration_seconds: 1701.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autoinflammation With Episodic Fever and Immune Dysregulation
  mondo_id: MONDO:0968982
  category: Mendelian
  causal_genes: SHARPIN
  omim_id: OMIM:620795
  synonyms: SHARPIN deficiency; AIFID
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
citation_count: 8
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 13
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0968982
    reported_labels:
    - MONDO
    ontology_label: autoinflammation with episodic fever and immune dysregulation
  - term_id: HP:0040286
    reported_labels:
    - Parotitis
    ontology_label: Abnormal axial muscle morphology
  - term_id: HP:0006568
    reported_labels:
    - Abnormal glycogen storage, liver
    ontology_label: Increased hepatic glycogen content
  - term_id: UBERON:0001484
    reported_labels:
    - parotid gland
    ontology_label: articular capsule
  labels_variant: 7
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
  path: Autoinflammation_With_Episodic_Fever_And_Immune_Dysregulation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autoinflammation_With_Episodic_Fever_And_Immune_Dysregulation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoinflammation With Episodic Fever and Immune Dysregulation
- **MONDO ID:** MONDO:0968982 (if available)
- **Causal gene(s):** SHARPIN
- **OMIM:** OMIM:620795
- **Synonyms:** SHARPIN deficiency; AIFID
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autoinflammation With Episodic Fever and Immune Dysregulation** covering all of the
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

# Autoinflammation With Episodic Fever and Immune Dysregulation (AIFID): SHARPIN Deficiency

**Disease:** Autoinflammation With Episodic Fever and Immune Dysregulation (AIFID) · **MONDO:** 0968982 · **OMIM:** 620795 · **Causal gene:** **SHARPIN** (HGNC:25321) · **Category:** Mendelian, autosomal recessive

---

## Summary

**Autoinflammation With Episodic Fever and Immune Dysregulation (AIFID), also called SHARPIN deficiency or "sharpenia," is an ultra-rare autosomal-recessive inborn error of immunity caused by biallelic loss-of-function variants in SHARPIN**, the gene encoding the accessory/regulatory subunit of the Linear Ubiquitin chain Assembly Complex (LUBAC). The disease was defined in 2024 by Oda and colleagues, who reported two unrelated individuals with homozygous frameshift SHARPIN variants and undetectable SHARPIN protein ([PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)). SHARPIN is one of three LUBAC subunits (together with the catalytic subunit HOIP/RNF31 and the accessory subunit HOIL-1L/RBCK1). LUBAC is the sole cellular machine that builds Met1 (M1)-linked "linear" polyubiquitin chains, which are deposited on NEMO (IKBKG) and RIPK1 to activate canonical NF-κB signaling and to restrain TNF-superfamily-driven cell death.

Mechanistically, loss of SHARPIN destabilizes LUBAC and reduces M1-linear ubiquitination, which **attenuates canonical NF-κB responses** and **shifts cells from an NF-κB-driven survival program toward TNF-superfamily-mediated apoptosis and necroptosis**. The clinical consequence is a paradoxical combination of **autoinflammation** (recurrent/episodic fever, sterile arthritis, parotitis, colitis, hepatic glycogenosis) and **immunodeficiency** (reduced germinal-center B-cell development due to increased B-cell death). Strikingly, and unlike the Sharpin-null *cpdm* mouse that has long served as the disease model, affected humans have **no dermatitis** and their monocytes show **no cytokine hyperresponsiveness**. The autoinflammatory component responds dramatically to **TNF inhibition** — one patient achieved complete clinical and transcriptomic resolution on anti-TNF therapy (etanercept) and has remained symptom-free for roughly seven years.

This report synthesizes nine confirmed findings drawn from 24 reviewed papers. The strongest human evidence rests on a single landmark study of two patients, supported by an extensive body of mouse-genetics and biochemical work on SHARPIN/LUBAC spanning more than a decade (three foundational 2011 *Nature*/*Nature Immunology* papers establishing SHARPIN as the third LUBAC subunit, plus subsequent genetic-epistasis studies dissecting the death pathways). AIFID sits within a tightly related family of monogenic "M1-ubiquitinopathies" — HOIP deficiency, HOIL-1 deficiency, and OTULIN-related autoinflammatory syndrome (ORAS) — against which it must be differentially diagnosed.

---

## Section 1 — Disease Information

**Overview.** AIFID (SHARPIN deficiency) is a Mendelian autoinflammatory disease with concomitant immunodeficiency, caused by complete loss of the SHARPIN protein. The autoinflammation manifests as episodic fever and sterile inflammation of joints, salivary glands, and gut; the immunodeficiency manifests as impaired germinal-center B-cell development and humoral deficiency. It is an inborn error of immunity (included in the IUIS 2024 classification).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0968982 |
| OMIM (phenotype) | 620795 |
| OMIM (gene SHARPIN) | 611885 |
| HGNC | HGNC:25321 |
| NCBI Gene (Entrez) | 81858 |
| UniProt | Q9H0F6 |
| Ensembl | ENSG00000179526 |
| Cytogenetic locus | 8q24.3 |

**Synonyms / alternative names.** SHARPIN deficiency; AIFID; "sharpenia" (informal, by analogy to otulipenia/HOIL-1 deficiency nomenclature).

**Information source.** Disease-level characterization is derived from **individual patient reports** (two probands with detailed clinical, immunophenotyping, cellular, and transcriptomic workup) aggregated against mechanistic data from aggregated disease-level and model-organism resources. This is not an EHR-derived or population-registry disease; it is defined case-by-case.

---

## Section 2 — Etiology

**Primary cause (genetic).** AIFID is caused by **biallelic (homozygous) loss-of-function variants in SHARPIN**. The two reported patients carried homozygous frameshift alleles producing undetectable protein (complete loss of function). There is no environmental or infectious cause of the disease itself, though inflammatory flares are a dysregulated innate-immune response in which TNF-superfamily signaling is the key effector.

**Genetic risk factors.** The disease is monogenic and fully determined by biallelic SHARPIN LoF. **Consanguinity** is a strong contributing factor: Patient 1 was born to consanguineous parents of Indian origin, consistent with autosomal-recessive inheritance of a rare allele. No susceptibility loci or common-variant modifiers have been defined (sample size of two precludes such analysis).

**Environmental risk factors.** None established as causal. As with other TNF-driven autoinflammatory diseases, infection or other inflammatory triggers plausibly precipitate flares, but this is inferred rather than demonstrated for AIFID specifically.

**Protective factors.** No genetic or environmental protective factors are documented for this ultra-rare disease. Mechanistically, anything reducing TNF-superfamily signaling (e.g., anti-TNF therapy) is therapeutically protective against the autoinflammatory phenotype.

**Gene–environment interactions.** Not characterized in humans. In the mouse model, dsRNA present in skin drives TLR3-mediated keratinocyte death contributing to dermatitis ([PMID: 27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/)) — a gene (Sharpin-loss) × environment (dsRNA/TLR3 ligand) interaction, though this branch appears not to operate in humans (no dermatitis).

---

## Section 3 — Phenotypes

Phenotypes are compiled from the two reported patients ([PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)). Frequencies are necessarily qualitative given n=2.

| Phenotype | Type | HPO suggestion | Onset | Course | Notes / frequency |
|---|---|---|---|---|---|
| Recurrent/episodic fever | Symptom | HP:0001954 (Recurrent fever) | Childhood | Episodic | Core feature (disease-naming) |
| Sterile arthritis (ankle, atlanto-axial) | Clinical sign | HP:0001369 (Arthritis) | Childhood | Episodic, progressive disability | P1; sterile synovial fluid; wheelchair-dependent before Rx |
| Parotitis / parotid swelling | Clinical sign | HP:0040286 (Parotitis) | Age 5 (P1) | Recurrent | P1 |
| Colitis / enteropathy | Clinical sign | HP:0002583 (Colitis) | Childhood | Chronic/relapsing | P1 |
| Hepatic glycogenosis (liver) | Lab/pathology | HP:0006568 (Abnormal glycogen storage, liver) | Childhood | — | P1 biopsy suggestive of glycogenosis |
| Germinal-center B-cell deficiency | Lab abnormality | HP:0010976 (B-cell abnormality) | Childhood | — | Hypoplastic adenoidal GCs; humoral immunodeficiency |
| Attenuated NF-κB signaling (cellular) | Lab abnormality | — | Congenital (cellular) | — | Fibroblasts & B cells |
| Febrile episodes with fatal course | Clinical course | — | Childhood | Severe (P2) | P2 died despite anti-TNF |

**Phenotype characteristics (overall).** Age of onset: childhood (parotid swelling from age 5 in P1). Severity: variable — ranging from controllable, anti-TNF-responsive disease (P1) to fatal (P2). Progression: episodic autoinflammation with progressive disability if untreated (P1 was wheelchair-dependent pre-treatment).

**Quality-of-life impact.** Substantial before treatment: P1 was wheelchair-dependent due to arthritis. Anti-TNF therapy restored function and produced sustained remission (~7 years symptom-free). No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease.

**Notable absences (phenotypic discriminators).** **No dermatitis** and **no monocyte cytokine hyperresponsiveness** — both distinguish human SHARPIN deficiency from the *cpdm* mouse and from HOIL-1/HOIP deficiency, respectively.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *SHARPIN* (SHANK-associated RH-domain-interacting protein), HGNC:25321, gene OMIM 611885, chr8q24.3 (GRCh38 chr8:144,098,633–144,108,124, minus strand). MANE transcript NM_030974.4 / NP_112236.3 encodes a 387-aa scaffold protein.

**Pathogenic variants (two reported, both homozygous frameshift LoF):**

| Patient | cDNA | Protein | Consequence | CADD | gnomAD |
|---|---|---|---|---|---|
| P1 | c.220dupC | p.Leu74ProfsX86 | Frameshift, truncation before/within UBL; NZF deleted | 32.5 | Absent |
| P2 | c.613_614delCT | p.Leu205GlufsX21 | Frameshift, truncation within UBL; NZF deleted | 24.2 | Absent |

Both exceed the SHARPIN mutation-significance cutoff (MSC 12.1) and both produce **undetectable SHARPIN protein** (complete loss of function). No homozygous SHARPIN LoF or homozygous CNV loss is reported in **gnomAD**, indicating intolerance to complete loss. ACMG classification: pathogenic (null variant in a gene with established LoF mechanism; absent from population databases; segregating with disease in consanguineous pedigrees).

**Variant type/class.** Frameshift/truncating (null). **Origin:** germline. **Functional consequence:** loss of function (destabilized/absent LUBAC accessory subunit).

**Protein domain architecture (why truncation abolishes function).** SHARPIN (387 aa) has three domains:
- **N-terminal PH (pleckstrin homology)** — integrin/tumor regulation; LUBAC-independent; not ubiquitin-binding.
- **Central UBL (ubiquitin-like)** — binds the HOIP UBA/NZF2 region to assemble and stabilize LUBAC and relieve HOIP autoinhibition.
- **C-terminal NZF (Npl4 zinc finger)** — binds K63-linked and linear ubiquitin; mediates cell-death protection.

Both UBL and NZF are required to stimulate linear ubiquitylation (UBL I272A and NZF T358L/F359V mutants abolish activity). The disease alleles p.Leu74Profs\*86 and p.Leu205Glufs\*21 truncate before/within the UBL and delete the NZF — abolishing LUBAC-supporting function and yielding undetectable protein.

**Modifier genes.** None established in humans. In mouse, death-pathway genes (*Tnfr1/Tnfrsf1a*, *Ripk3*, *Casp8*, *Mlkl*, *Tlr3*) genetically modify the phenotype (see Sections 6 and 15).

**Epigenetic / chromosomal abnormalities.** None implicated; AIFID is a single-gene LoF disease, not a chromosomal disorder.

---

## Section 5 — Environmental Information

No environmental toxins, radiation, pollution, occupational exposures, or lifestyle factors are established as causing or triggering AIFID. No infectious agent causes the disease. The disease is a cell-intrinsic consequence of SHARPIN loss; TNF-superfamily ligands (endogenous) are the proximal drivers of the inflammatory and cell-death phenotype. In the mouse model, **dsRNA in skin acting through TLR3** is an environmental-like trigger for keratinocyte death and dermatitis ([PMID: 27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/)), but this branch is not evident in human disease.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic SHARPIN LoF variants** (frameshift, null) → **absent SHARPIN protein** (demonstrated: undetectable protein).
2. Absent SHARPIN → **destabilization and reduced abundance of LUBAC** (HOIP/HOIL-1L/SHARPIN complex) (demonstrated in mouse MEFs/B cells; inferred in human cells).
3. Reduced LUBAC → **diminished Met1 (M1)-linear polyubiquitination of NEMO (IKBKG) and RIPK1** (demonstrated biochemically for LUBAC generally).
4. Reduced linear ubiquitination of NEMO → **attenuated assembly/activation of the IKK complex → attenuated canonical NF-κB signaling** (demonstrated: patient fibroblasts and B cells show attenuated canonical NF-κB responses).
5. **Branch A (survival → death switch):** Attenuated NF-κB survival program + loss of LUBAC-mediated restraint on the TNFR1 complex → **increased propensity for TNF-superfamily-mediated cell death** via FADD/caspase-8-dependent apoptosis and RIPK3/MLKL-dependent necroptosis (demonstrated: patient cells show death propensity; mouse epistasis defines both death arms).
6. **Branch A → tissue injury:** Excess death of parenchymal/immune cells → **sterile multi-organ autoinflammation** (fever, arthritis, parotitis, colitis, hepatic glycogenosis). TNF is the key effector (demonstrated: anti-TNF produces complete resolution in P1; *Tnf* deletion prevents mouse skin lesions).
7. **Branch B (immunodeficiency):** Increased B-cell death → **reduced germinal-center B-cell development → humoral immunodeficiency** (demonstrated: both SHARPIN- and HOIP-deficient individuals show substantial GC B-cell reduction).
8. **Mouse-specific branch (not seen in humans):** Loss of LUBAC restraint on TLR3 → enhanced dsRNA-triggered keratinocyte death → **dermatitis** (demonstrated in *cpdm* mouse; absent in humans).

### Molecular pathways
- **Canonical NF-κB pathway** (attenuated) — Reactome/KEGG NF-κB signaling; linear ubiquitination of NEMO is the proximal activating event.
- **TNFR1 signaling complex (Complex I/II)** — loss of LUBAC restraint tips the balance toward Complex II (death).
- **Apoptosis (FADD/caspase-8)** and **necroptosis (RIPK1/RIPK3/MLKL)** — the two death arms.

### Cellular processes
Inflammation (GO:0006954), apoptotic process (GO:0006915), necroptotic process (GO:0070266), canonical NF-κB signal transduction (GO:0007249), linear/M1 protein polyubiquitination, B-cell differentiation / germinal-center formation (GO:0002467).

### Protein dysfunction
Complete loss of the SHARPIN scaffold → LUBAC destabilization → loss of linear-ubiquitin E3 ligase activity support (HOIP is catalytic but requires SHARPIN/HOIL-1 for full activity and stability).

### Immune system involvement
A dual lesion: **autoinflammation** (dysregulated innate TNF-driven inflammation and cell death) plus **immunodeficiency** (defective GC B cells, humoral deficiency). Notably, unlike HOIL-1/HOIP deficiency, SHARPIN-deficient monocytes do **not** show cytokine hyperresponsiveness.

### Metabolic changes
**Hepatic glycogenosis** (abnormal glycogen accumulation in liver, by biopsy) — a feature paralleling other LUBAC defects (HOIP/HOIL-1 cause amylopectinosis/glycogen storage), linking M1-ubiquitin dysfunction to a glycogen-metabolism phenotype (mechanism not fully defined).

### GO / CL term suggestions
- Biological process: GO:0007249 (I-κB kinase/NF-κB signaling), GO:0006915 (apoptotic process), GO:0070266 (necroptotic process), GO:0002467 (germinal center formation).
- Cell types: CL:0000236 (B cell), CL:0000844 (germinal center B cell), CL:0000057 (fibroblast), CL:0000235 (macrophage), CL:0000312 (keratinocyte — mouse branch).

---

## Section 7 — Anatomical Structures Affected

**Organ level (primary).** Joints (sterile arthritis — ankle, atlanto-axial), salivary/parotid glands (parotitis), colon/gut (colitis), liver (glycogenosis), secondary lymphoid organs (adenoid/germinal centers). **Body systems:** musculoskeletal, digestive, hepatobiliary, immune/lymphoreticular.

**Tissue/cell level.** Germinal-center B cells (reduced; increased death), B cells and fibroblasts (attenuated NF-κB; propensity to die), macrophages/monocytes (involved but not hyperresponsive). In the mouse: keratinocytes (epidermal death → dermatitis).

**Subcellular level.** Cytoplasmic signaling platforms — the TNFR1 signaling complex and IKK complex at the plasma membrane/cytosol; LUBAC acts on NEMO in the cytosol. GO cellular component: GO:0005829 (cytosol), GO:0098797 (plasma membrane protein complex), LUBAC complex.

**UBERON suggestions.** UBERON:0001484 (parotid gland), UBERON:0000059 (large intestine/colon), UBERON:0002107 (liver), UBERON:0001474 (bone element/joint), UBERON:0001959 (adenoid/lymphoid tissue), UBERON:0002106 (spleen — mouse). **Lateralization:** arthritis can be bilateral; parotid involvement may be bilateral — not systematically described given small n.

---

## Section 8 — Temporal Development

**Onset.** Childhood; parotid swelling noted from **age 5** in P1. Onset pattern is **episodic/recurrent** (fever flares) superimposed on chronic inflammation.

**Progression.** Untreated disease is progressive in disability (P1 wheelchair-dependent before treatment). Course pattern is **episodic/relapsing autoinflammation**. Duration is **chronic/lifelong** (genetic). Severity ranges from treatable (P1) to **fatal** (P2, death attributed to broader LUBAC-deficiency immunodeficiency despite anti-TNF reducing febrile episodes).

**Patterns.** Remission is **treatment-induced** by anti-TNF (sustained ~7-year remission in P1); no spontaneous remission documented. **Critical period for intervention:** early initiation of TNF blockade appears to control the autoinflammatory component, though it does not fully rescue the immunodeficiency.

---

## Section 9 — Inheritance and Population

**Epidemiology.** Ultra-rare: **two patients reported worldwide** ([PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)). No meaningful prevalence/incidence estimate; effectively <1 per 10⁷ (below Orphanet reporting thresholds).

**Inheritance.** **Autosomal recessive** — both patients homozygous, at least one in a consanguineous pedigree (Indian origin). **Penetrance:** presumed complete for biallelic null (both reported biallelic-null individuals are affected). **Expressivity:** variable (controllable vs fatal). **Carrier frequency:** heterozygous SHARPIN LoF is tolerated (heterozygous carriers unaffected); no homozygous LoF in gnomAD. **Founder effect / anticipation / mosaicism:** none described (n too small). **Consanguinity** is relevant to recurrence risk.

**Population demographics.** One patient of **Indian** ancestry; no ethnic predilection can be inferred from n=2. **Sex ratio:** at least P1 was male (a boy) — not interpretable as a sex bias given sample size. **Age distribution:** pediatric onset.

---

## Section 10 — Diagnostics

**Clinical/laboratory tests.**
- Inflammatory markers during febrile flares (elevated acute-phase response — expected for autoinflammation).
- **Sterile synovial fluid** on joint aspiration (arthritis is non-infectious).
- **Liver biopsy** showing glycogenosis-like changes.
- Immunophenotyping: reduced germinal-center B cells (adenoid/lymphoid tissue histology shows hypoplastic GCs); humoral immunodeficiency workup.
- Functional cellular assays: **attenuated canonical NF-κB response** in patient fibroblasts and B cells; **increased TNF-superfamily-induced cell death** in patient cells. Absence of monocyte cytokine hyperresponsiveness helps distinguish from HOIL-1/HOIP deficiency.
- **Western blot:** undetectable SHARPIN protein; reduced LUBAC.

**Genetic testing (definitive).** **WES or WGS** identifies the biallelic SHARPIN frameshift variants; inborn-errors-of-immunity / autoinflammatory **gene panels** that include SHARPIN, RNF31 (HOIP), RBCK1 (HOIL-1), OTULIN, TNFAIP3, and IKBKG are appropriate. Single-gene SHARPIN testing is reasonable when LUBAC disease is strongly suspected. CMA/karyotype/FISH/mtDNA/repeat testing are **not indicated** (point/frameshift LoF disease).

**Omics-based support.** **Transcriptomic profiling** was used to document resolution of the inflammatory signature on anti-TNF therapy and is informative for monitoring.

**Clinical criteria / differential diagnosis.** No formal diagnostic criteria exist (ultra-rare). Differential diagnosis spans the **LUBAC/M1-ubiquitin disease family and related NF-κB disorders** (see Section 15 table): HOIP (RNF31) deficiency, HOIL-1 (RBCK1) deficiency, OTULIN-related autoinflammatory syndrome (ORAS/otulipenia), A20/TNFAIP3 haploinsufficiency (HA20), and NEMO/IKBKG defects. **Discriminating features of AIFID:** autoinflammatory arthritis/parotitis/colitis + hepatic glycogenosis + GC B-cell immunodeficiency, with **no dermatitis** and **no monocyte cytokine hyperresponsiveness**.

**Screening.** Cascade genetic testing of relatives and carrier testing in consanguineous families; no newborn-screening program exists.

---

## Section 11 — Outcome / Prognosis

**Survival/mortality.** Variable and component-dependent: P1 achieved **sustained remission (~7 years symptom-free)** on anti-TNF; P2 had a **fatal outcome** despite anti-TNF (death attributed to the immunodeficiency/broader LUBAC-deficiency features rather than uncontrolled fever). No formal survival statistics (n=2).

**Morbidity/function.** High pre-treatment morbidity (wheelchair dependence from arthritis in P1), reversible with TNF blockade for the autoinflammatory component.

**Disease course/complications.** Autoinflammation (controllable), humoral immunodeficiency (persists; predisposes to infection), and the metabolic (hepatic glycogenosis) feature. The immunodeficiency is the principal residual risk even when inflammation is controlled.

**Prediction.** Response to anti-TNF predicts control of autoinflammation; severity of the immunodeficiency component appears to drive the worst outcomes. **No validated prognostic biomarkers** beyond the inflammatory transcriptomic signature.

---

## Section 12 — Treatment

**Pharmacotherapy — mechanism-based.** **TNF inhibitors (anti-TNF)** are the cornerstone. One patient achieved **complete clinical and transcriptomic resolution of autoinflammation** on anti-TNF; etanercept maintained ~7-year remission in P1. This is directly predicted by the mechanism (TNF-superfamily-driven cell death/inflammation downstream of LUBAC loss) and corroborated by the mouse model, where *Tnf* deletion prevents disease.
- NCIT suggestions: Etanercept (NCIt C1119), TNF inhibitor / Tumor Necrosis Factor Inhibitor therapy, anti-TNF monoclonal antibodies (infliximab, adalimumab) as alternatives.

**Pharmacogenomics.** Not applicable in a conventional sense; treatment selection is driven by the genotype-defined mechanism (genotype-guided use of anti-TNF).

**Advanced therapeutics.** None approved specifically. Conceptually, **hematopoietic stem cell transplantation** could address the immunodeficiency component (as considered for other LUBAC defects), and gene correction is a theoretical future option — neither is established for AIFID. No RNA, targeted, or immunotherapy agents are specific to this disease.

**Surgical/supportive/rehabilitative.** Symptomatic management of arthritis (physical therapy, mobility support pre-treatment); immunoglobulin replacement and infection prophylaxis may be indicated for the humoral immunodeficiency.

**Experimental / trials.** No disease-specific registered trials (ultra-rare). Management is extrapolated from the broader autoinflammatory and inborn-errors-of-immunity fields.

**Treatment strategy.** (1) Confirm genetic diagnosis; (2) initiate **anti-TNF** to control autoinflammation; (3) manage the **immunodeficiency** (infection surveillance, immunoglobulin as needed); (4) monitor hepatic and inflammatory status. Anti-TNF controls inflammation but does **not** correct the underlying immunodeficiency — a key limitation illustrated by P2's fatal course.

---

## Section 13 — Prevention

**Primary prevention.** Not applicable beyond **genetic counseling** in at-risk (consanguineous) families — carrier identification and reproductive options (prenatal/preimplantation genetic testing) can prevent recurrence.

**Secondary/tertiary prevention.** Early genetic diagnosis and prompt anti-TNF initiation prevent progression of disability (tertiary prevention of autoinflammatory complications). Infection prophylaxis mitigates immunodeficiency complications.

**Immunization/public-health/environmental measures.** Standard immunization caution applies to immunodeficient patients (live-vaccine considerations); no vaccine prevents the disease. No environmental interventions are relevant.

**Counseling.** **Genetic counseling** for autosomal-recessive recurrence (25% risk per pregnancy for carrier couples); cascade testing of relatives.

---

## Section 14 — Other Species / Natural Disease

**Taxonomy / orthologs.** Mouse *Sharpin* (MGI:1913331; Entrez 109322; chromosome 15) is the principal ortholog studied (NCBI Taxon 10090, *Mus musculus*). Human *SHARPIN* NCBI Gene 81858 (Taxon 9606, *Homo sapiens*).

**Natural disease in animals.** The spontaneous mouse mutation **cpdm** (chronic proliferative dermatitis) is a naturally occurring *Sharpin*-null disorder — the founding model of SHARPIN biology — rather than a companion-animal/wildlife disease. No naturally occurring SHARPIN disease is documented in dogs, cats, or livestock in the reviewed literature.

**Comparative biology.** The core mechanism (LUBAC → M1-ubiquitin → NF-κB/cell-death control) is **evolutionarily conserved** between mouse and human. Comparative pathology shows **partial recapitulation with a key divergence**: mice develop prominent **dermatitis** (via TLR3/keratinocyte death) that humans lack, while both show multi-organ inflammation and lymphoid/immune defects.

**Transmission.** Not applicable (non-communicable genetic disease; no zoonotic potential).

---

## Section 15 — Model Organisms

**Principal model: the Sharpin-null mouse (cpdm).** The spontaneous *Sharpin^cpdm/cpdm^* mutation causes **chronic proliferative dermatitis**: chronic eosinophilic dermatitis, multi-organ inflammation, splenomegaly, **loss of Peyer's patches / disrupted secondary lymphoid tissue**, and immunodeficiency with increased serum IgM ([PMID: 21455180](https://pubmed.ncbi.nlm.nih.gov/21455180/), [PMID: 21455173](https://pubmed.ncbi.nlm.nih.gov/21455173/)).

**Genetic epistasis defining the death pathways.**

| Genetic manipulation (on Sharpin-null background) | Effect on phenotype | PMID |
|---|---|---|
| *Tnf* deletion | Prevents skin lesions | [21455173](https://pubmed.ncbi.nlm.nih.gov/21455173/) |
| *Tnfr1* (not *Tnfr2*) deficiency | Suppresses multi-organ phenotype | [25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/) |
| *Ripk3* or *Mlkl* deficiency | Partial amelioration (necroptosis arm) | [25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/) |
| *Ripk3* deletion + *Casp8* heterozygosity | Near-complete suppression; restores Peyer's patches | [25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/) |
| *Tlr3* ablation | Ameliorates dermatitis (keratinocyte death arm) | [27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/) |
| Integrin β1 function-blocking antibody | Reduces epidermal hyperproliferation | [29040328](https://pubmed.ncbi.nlm.nih.gov/29040328/) |

**Model characteristics.** The *cpdm* mouse **partially recapitulates** human disease: shared multi-organ inflammation, lymphoid/immune defects, attenuated NF-κB, and TNF-dependence (basis for anti-TNF therapy). **Key limitation:** the mouse's prominent **dermatitis is absent in humans**, driven by a TLR3/keratinocyte-death branch apparently not operative in human disease. The mouse also reveals a LUBAC-independent **integrin-inhibitory** role of SHARPIN contributing to epidermal hyperproliferation, and a LUBAC-independent **caspase-1-inhibitory** role relevant to sepsis ([PMID: 26968342](https://pubmed.ncbi.nlm.nih.gov/26968342/)).

**Available genetic models.** Spontaneous *cpdm* allele; targeted *Sharpin* knockouts; compound crosses (*Tnfr1⁻/⁻*, *Ripk3⁻/⁻*, *Casp8^+/−^*, *Tlr3⁻/⁻*, *Mlkl⁻/⁻*). **Resources:** MGI (MGI:1913331), IMSR.

**Cellular/in vitro models.** Patient-derived fibroblasts and B cells (attenuated NF-κB, death propensity); HOIL-1-deficient patient fibroblasts used in related LUBAC studies; MEFs and B cells from *cpdm* mice.

---

## Mechanistic Model / Interpretation

```
  Biallelic SHARPIN LoF (frameshift, null)
                │  undetectable SHARPIN protein
                ▼
  LUBAC destabilized / reduced (HOIP–HOIL-1L–SHARPIN)
                │  ↓ M1-linear ubiquitination of NEMO & RIPK1
                ▼
  Attenuated IKK / canonical NF-κB activation
                │
     ┌──────────┴───────────────────────────┐
     ▼ (survival→death switch)               ▼ (immune development)
  ↑ TNF-superfamily cell death          ↑ B-cell death
  • FADD/caspase-8 apoptosis            • ↓ germinal-center B cells
  • RIPK3/MLKL necroptosis                     │
     │                                          ▼
     ▼                                   Humoral immunodeficiency
  Sterile multi-organ autoinflammation
  (fever, arthritis, parotitis,
   colitis, hepatic glycogenosis)
     │                                   ── MOUSE-ONLY BRANCH ──
     │ TNF is key effector               Loss of LUBAC restraint on TLR3
     ▼                                   → dsRNA-driven keratinocyte death
  ✔ Resolves with anti-TNF              → DERMATITIS (absent in humans)
```

The unifying concept is that **SHARPIN loss converts a cell's default NF-κB-driven survival response to TNF into a death response**, simultaneously producing autoinflammation (from excess sterile cell death and TNF signaling) and immunodeficiency (from death of developing B cells). The therapeutic corollary — that **removing TNF collapses the pathogenic branch** — is validated both in the mouse (*Tnf* deletion prevents disease) and in the human patient (anti-TNF produces complete resolution). The human–mouse divergence (no human dermatitis) localizes to the TLR3/keratinocyte branch and is a cautionary note about over-extrapolating the *cpdm* model to human skin.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/) | *Biallelic human SHARPIN loss of function induces autoinflammation and immunodeficiency* | **Defining human study** (2 patients): disease definition, phenotype, variants, attenuated NF-κB, death propensity, GC B-cell defect, anti-TNF response, no dermatitis |
| [25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/) | *TNFR1-dependent cell death drives inflammation in Sharpin-deficient mice* | Mouse epistasis: TNFR1-dependence; apoptosis + necroptosis arms |
| [21455173](https://pubmed.ncbi.nlm.nih.gov/21455173/) | *Linear ubiquitination prevents inflammation and regulates immune signalling* | cpdm phenotype; *Tnf* deletion prevents skin lesions |
| [21455181](https://pubmed.ncbi.nlm.nih.gov/21455181/) | *SHARPIN forms a linear ubiquitin ligase complex regulating NF-κB and apoptosis* | SHARPIN as 3rd LUBAC subunit; NEMO linear ubiquitination; FADD/caspase-8 death |
| [21455180](https://pubmed.ncbi.nlm.nih.gov/21455180/) | *SHARPIN is a component of the NF-κB-activating LUBAC* | SHARPIN loss reduces LUBAC; attenuates NF-κB in MEFs/B cells |
| [22863777](https://pubmed.ncbi.nlm.nih.gov/22863777/) | *HOIP specifies linear ubiquitin chain assembly (RBR + LDD)* | HOIP is catalytic; SHARPIN/HOIL-1 accessory |
| [24469399](https://pubmed.ncbi.nlm.nih.gov/24469399/) | *Mechanism of IKK activation by LUBAC* | Linear-ubiquitinated NEMO activates IKK/NF-κB |
| [23969028](https://pubmed.ncbi.nlm.nih.gov/23969028/) | *Linear ubiquitination-mediated NF-κB regulation and disorders* | Counter-regulatory DUBs CYLD, A20, OTULIN |
| [27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/) | *LUBAC deficiency perturbs TLR3 signaling* | Mouse-specific TLR3/keratinocyte-death dermatitis branch |
| [26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/) | *Human HOIP/LUBAC deficiency* | Differential diagnosis: HOIP deficiency |
| [30804083](https://pubmed.ncbi.nlm.nih.gov/30804083/) | *OTULIN deficiency in ORAS* | Differential diagnosis: ORAS (M1-ubiquitin family) |
| [29040328](https://pubmed.ncbi.nlm.nih.gov/29040328/) | *Integrin β1 inhibition alleviates cpdm dermatitis* | LUBAC-independent integrin role of SHARPIN |
| [26968342](https://pubmed.ncbi.nlm.nih.gov/26968342/) | *SHARPIN regulates caspase-1 in sepsis* | LUBAC-independent SHARPIN function (caspase-1 inhibition) |

**Verified direct quotes supporting key claims:**
- Disease definition — [PMID: 38609546]: *"Here, we report two individuals with SHARPIN deficiency who manifest autoinflammatory symptoms but unexpectedly no dermatological problems. Fibroblasts and B cells from these individuals showed attenuated canonical NF-κB responses and a propensity for cell death mediated by TNF superfamily members."*
- Therapy — [PMID: 38609546]: *"Treatment of one SHARPIN-deficient individual with anti-TNF therapies led to complete clinical and transcriptomic resolution of autoinflammation."*
- Immunodeficiency — [PMID: 38609546]: *"Both SHARPIN-deficient and HOIP-deficient individuals showed a substantial reduction of secondary lymphoid germinal center B cell development."*
- Mouse model — [PMID: 25443632]: *"The inactivating mouse Sharpin cpdm mutation causes TNF-dependent multi-organ inflammation, characterized by dermatitis, liver inflammation, splenomegaly, and loss of Peyer's patches."*
- Death pathways — [PMID: 25443632]: *"Ripk3 or Mlkl deficiency partially ameliorated the multi-organ phenotype, and combined Ripk3 deletion and Casp8 heterozygosity almost completely suppressed it, even restoring Peyer's patches."*
- Catalytic subunit — [PMID: 22863777]: *"both LUBAC catalytic activity and LUBAC specificity for linear ubiquitin chain formation are embedded within the RING-IBR-RING (RBR) ubiquitin ligase subunit HOIP."*
- NEMO/IKK — [PMID: 24469399]: *"linearly polyubiquitinated NEMO activates IKK more potently than unanchored linear chains."*
- Mouse NF-κB — [PMID: 21455180]: *"Deletion of SHARPIN drastically reduced the amount of LUBAC, which resulted in attenuated TNF-α- and CD40-mediated activation of NF-κB in mouse embryonic fibroblasts (MEFs) or B cells from cpdm mice."*

---

## Limitations and Knowledge Gaps

1. **Extremely small human evidence base (n=2).** All human-specific conclusions rest on a single 2024 study of two unrelated patients. Prevalence, penetrance, expressivity, sex bias, age distribution, and the full phenotypic spectrum cannot be reliably estimated.
2. **Human–mouse divergence.** The principal model (*cpdm* mouse) displays dermatitis that humans lack, so the mouse overstates skin involvement and the human disease's full organ spectrum may still be incompletely mapped.
3. **Mechanism of hepatic glycogenosis** downstream of LUBAC loss is unexplained (parallels HOIP/HOIL-1 amylopectinosis but mechanistically undefined).
4. **Immunodeficiency not corrected by anti-TNF.** P2's fatal course indicates anti-TNF controls inflammation but not the immunodeficiency; optimal management of the immune-deficiency component (e.g., HSCT) is undefined.
5. **No modifier genes, no validated biomarkers** in humans; prognostic stratification is anecdotal.
6. **No registered clinical trials** or approved disease-specific therapeutics beyond repurposed anti-TNF.

---

## Proposed Follow-up Experiments / Actions

1. **Case ascertainment / international registry.** Use GeneMatcher and inborn-errors-of-immunity networks (IUIS) to find additional SHARPIN-deficient patients and build a natural-history dataset; this is the single highest-value action.
2. **Define the immunodeficiency mechanism.** Deep immunophenotyping of germinal-center reactions and B-cell survival in patient and *Sharpin*-null tissues; test whether B-cell-intrinsic death (caspase-8/RIPK) drives the GC defect, and whether RIPK1 kinase inhibition rescues it.
3. **Dissect the human-vs-mouse dermatitis divergence.** Compare TLR3/dsRNA-induced keratinocyte death in human SHARPIN-deficient vs *cpdm* keratinocytes to explain why humans are spared.
4. **Test next-generation targeted therapies.** Evaluate RIPK1 kinase inhibitors and combined apoptosis/necroptosis blockade in patient cells and mouse models, given epistasis showing both death arms contribute — potentially addressing features not fully controlled by anti-TNF.
5. **Evaluate HSCT** as definitive therapy for the immunodeficiency component in severe cases, informed by experience in HOIP/HOIL-1 deficiency.
6. **Investigate the glycogenosis phenotype** metabolically (liver glycogen structure/quantity) to connect M1-ubiquitin loss to glycogen-storage pathology across the LUBAC disease family.

---

## Consensus Answer

Autoinflammation with episodic fever and immune dysregulation (AIFID; MONDO:0968982, OMIM 620795) is an ultra-rare autosomal-recessive inborn error of immunity caused by biallelic loss-of-function variants in **SHARPIN** (HGNC:25321, 8q24.3), the accessory subunit of the linear ubiquitin chain assembly complex (LUBAC). Loss of SHARPIN destabilizes LUBAC and reduces M1-linear ubiquitination of NEMO/RIPK1, attenuating canonical NF-κB signaling and shifting cells toward TNF-superfamily-driven apoptosis/necroptosis — producing childhood-onset episodic fever, sterile arthritis, parotitis, colitis, hepatic glycogenosis, and germinal-center B-cell immunodeficiency (but, unlike the Sharpin-null *cpdm* mouse, no dermatitis), with the autoinflammation responding dramatically to TNF inhibition. The disease is defined by two patients reported by Oda et al. 2024 ([PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)).


## Artifacts

- [OpenScientist final report](Autoinflammation_With_Episodic_Fever_And_Immune_Dysregulation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autoinflammation_With_Episodic_Fever_And_Immune_Dysregulation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 24 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0968982` (2 mentions) - the report calls it "MONDO"; MONDO calls it **autoinflammation with episodic fever and immune dysregulation**
- `HP:0040286` (1 mention) - the report calls it "Parotitis"; HP calls it **Abnormal axial muscle morphology**
- `HP:0006568` (1 mention) - the report calls it "Abnormal glycogen storage, liver"; HP calls it **Increased hepatic glycogen content**
- `UBERON:0001484` (1 mention) - the report calls it "parotid gland"; UBERON calls it **articular capsule**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010976` (1 mention) - the report calls it "B-cell abnormality"; HP calls it **Decreased total B cell count**, and lists "Low B cell count" among its other names
- `GO:0007249` (2 mentions) - the report calls it "I-κB kinase/NF-κB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names
- `CL:0000312` (1 mention) - the report calls it "keratinocyte — mouse branch"; CL calls it **keratinocyte**
- `UBERON:0000059` (1 mention) - the report calls it "large intestine/colon"; UBERON calls it **large intestine**
- `UBERON:0001474` (1 mention) - the report calls it "bone element/joint"; UBERON calls it **bone element**
- `UBERON:0001959` (1 mention) - the report calls it "adenoid/lymphoid tissue"; UBERON calls it **white pulp of spleen**, and lists "noduli lymphoidei splenici" among its other names
- `UBERON:0002106` (1 mention) - the report calls it "spleen — mouse"; UBERON calls it **spleen**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:25321` - called "SHARPIN", "HGNC"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.