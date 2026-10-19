---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T00:37:51.409880'
end_time: '2026-09-30T00:59:43.395298'
duration_seconds: 1311.99
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Vibrio Vulnificus Infectious Disease
  mondo_id: MONDO:0043297
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
citation_count: 34
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:17853628
  relevance_assessed: 34
  on_topic: 18
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 13
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0002615
    reported_labels:
    - Clinical sign
    ontology_label: Hypotension
  - term_id: HP:0100658
    reported_labels:
    - Clinical sign
    ontology_label: Cellulitis
  - term_id: HP:0001882
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased total leukocyte count
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0003259
    reported_labels:
    - Lab abnormality
    ontology_label: Elevated circulating creatinine concentration
  - term_id: HP:0003073
    reported_labels:
    - Lab abnormality
    ontology_label: Hypoalbuminemia
  - term_id: UBERON:0002107
    reported_labels:
    - Secondary organ involvement:** **Liver
    ontology_label: liver
  - term_id: NCIT:C305
    reported_labels:
    - Ceftriaxone
    ontology_label: Bilirubin
  - term_id: NCIT:C1004
    reported_labels:
    - Ceftazidime
    ontology_label: Antineoplaston A10
  - term_id: NCIT:C544
    reported_labels:
    - Doxycycline
    ontology_label: Altretamine
  - term_id: NCIT:C1738
    reported_labels:
    - Minocycline
    ontology_label: Amphotericin B Liposomal
  - term_id: NCIT:C15325
    reported_labels:
    - Debridement
    ontology_label: Skin Transplantation
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  - term_id: NCIT:C1738
    ontology_label: Amphotericin B Liposomal
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Vibrio_Vulnificus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Vibrio_Vulnificus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vibrio Vulnificus Infectious Disease
- **MONDO ID:** MONDO:0043297 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Vibrio Vulnificus Infectious Disease** covering all of the
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

# Vibrio vulnificus Infectious Disease — Comprehensive Disease Characterization Report

**Disease:** Vibrio vulnificus Infectious Disease
**MONDO ID:** MONDO:0043297
**Category:** Infectious Disease (foodborne / wound-associated bacterial infection)
**Causative organism:** *Vibrio vulnificus* (NCBI Taxonomy txid:672), a halophilic, Gram-negative, motile, curved bacillus of family *Vibrionaceae*

---

## Summary

**Vibrio vulnificus infectious disease is an acute, frequently fulminant bacterial infection caused by the halophilic marine Gram-negative bacterium *V. vulnificus*, presenting as three overlapping clinical syndromes—primary (foodborne) septicemia, necrotizing wound infection, and gastroenteritis.** Infection is acquired by ingesting raw or undercooked shellfish (especially oysters) or by exposing an open wound to warm brackish/marine water. It is the leading cause of seafood-related death in the United States, with case-fatality exceeding 50% for primary septicemia and about 15% for wound infection ([PMID: 17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/); [PMID: 21367733](https://pubmed.ncbi.nlm.nih.gov/21367733/)).

The disease is **not genetic**; it is an environmental/infectious disease whose severity is dictated by host predisposition. The single most important host risk factor is an **iron-overloaded, immunocompromised state**—above all chronic liver disease (cirrhosis) and hereditary hemochromatosis—because elevated circulating iron and reduced transferrin binding capacity permit explosive bacterial growth. Mechanistically, the pathophysiology is a defined causal chain: a permissive iron-rich host environment enables the Fur-regulated vulnibactin/VuuA siderophore system to strip transferrin-bound iron; the capsular polysaccharide (CPS) confers complement/serum resistance; and secreted toxins—the MARTX/RtxA1 toxin, VvhA cytolysin, and VvpE metalloprotease—breach epithelial and endothelial barriers, injure tissue, and trigger a lipopolysaccharide-driven proinflammatory cytokine storm (TNF-α, IL-1β, IL-6) that culminates in septic shock and multi-organ dysfunction.

Survival hinges on **early recognition and prompt combination antimicrobial therapy** (a third-generation cephalosporin such as ceftazidime/cefotaxime plus a tetracycline such as doxycycline/minocycline, which act synergistically) combined with **aggressive surgical debridement/fasciotomy** for necrotizing soft-tissue infection. Treatment delay beyond three days is an independent predictor of death. Prevention rests on public-health measures (oyster post-harvest processing, consumer education) and on advising high-risk individuals to avoid raw shellfish and marine-water wound exposure. This report synthesizes 14 confirmed findings drawn from 37 primary papers across all 15 requested characteristic domains.

---

## 1. Disease Information

*V. vulnificus* infection is an acute infectious disease caused by a free-living, estuarine, halophilic Gram-negative bacterium. Clinically it manifests as **three distinct subtypes**: (1) **primary septicemia**, typically after ingestion of raw oysters/shellfish; (2) **wound (traumatic) infection**, from exposure of broken skin to *V. vulnificus*-inhabited seawater; and (3) **gastroenteritis** ([PMID: 31325061](https://pubmed.ncbi.nlm.nih.gov/31325061/); [PMID: 7488992](https://pubmed.ncbi.nlm.nih.gov/7488992/)). Progression to multiple organ dysfunction syndrome (MODS) can be extremely rapid.

**Key identifiers:**
- **MONDO:** MONDO:0043297
- **NCBI Taxonomy (organism):** txid672
- **MeSH:** *Vibrio vulnificus* (organism); "Vibrio Infections" (disease group, D014733)
- **ICD-10:** A05.5 (foodborne *Vibrio vulnificus* intoxication is grouped under vibriosis); wound/sepsis cases coded under A48.8 / associated sepsis codes; **ICD-11:** vibriosis-region codes (1A00–1A9Z gastrointestinal / 1B7Y bacterial infections of skin)
- **OMIM / Orphanet:** Not applicable — this is an infectious, non-Mendelian disease with no OMIM disease entry

**Synonyms / alternative names:** *Vibrio vulnificus* septicemia; *Vibrio vulnificus* sepsis; *Vibrio vulnificus* wound infection; "lactose-fermenting vibrio" infection (historical); a subtype of **vibriosis**.

**Data provenance:** The information here is derived from aggregated disease-level resources—clinical reviews, surveillance datasets (e.g., Florida 1998–2007), case series, and mechanistic laboratory studies—rather than from individual-patient EHR extraction.

---

## 2. Etiology

**Disease causal factor (primary cause):** Infection by *V. vulnificus*. This is an **infectious/environmental** etiology, not genetic. Acquisition routes are (a) ingestion of contaminated raw/undercooked shellfish and (b) wound contact with warm seawater ([PMID: 7488992](https://pubmed.ncbi.nlm.nih.gov/7488992/)).

**Host risk factors (environmental/clinical):**
- **Iron overload and chronic liver disease** are the principal host risk factors for fatal infection. Ex vivo, *V. vulnificus* is killed by normal human blood but grows rapidly in blood from hemochromatosis patients—or in normal blood when transferrin saturation is raised or iron (hematin) is added ([PMID: 1872665](https://pubmed.ncbi.nlm.nih.gov/1872665/)). Pathogenicity is "generally reserved for the immunocompromised host, and is specifically related to disease states which exhibit high serum iron levels" ([PMID: 7488992](https://pubmed.ncbi.nlm.nih.gov/7488992/)).
- **Cirrhosis / chronic alcoholic liver disease, hemochromatosis, diabetes mellitus, chronic renal disease, immunosuppression, and hematologic disease.** Risk of death rose with the *number* of underlying conditions (P<0.0001) in Florida surveillance ([PMID: 20546636](https://pubmed.ncbi.nlm.nih.gov/20546636/)). Most patients have at least one predisposing immunocompromising condition ([PMID: 17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/)).
- **Demographic:** Older adult males are disproportionately affected (consistent with higher alcoholic-liver-disease burden).

**Genetic host risk factors:** No causal human germline variants define susceptibility. The relevant "genetic" contribution is indirect: **hereditary hemochromatosis (HFE-related iron overload)** raises circulating iron and thereby susceptibility ([PMID: 1872665](https://pubmed.ncbi.nlm.nih.gov/1872665/)). No GWAS susceptibility loci are established.

**Protective factors:** Thorough cooking of shellfish; avoiding raw shellfish and marine-water wound exposure in at-risk hosts; intact iron homeostasis (normal transferrin saturation limits free iron and is bactericidal). No genetic protective alleles are defined.

**Gene–environment interaction:** The dominant interaction is between **host iron status (genetic or acquired) and pathogen iron-acquisition machinery**: iron-rich host serum (from HFE hemochromatosis or cirrhosis) meets the bacterium's Fur-regulated vulnibactin siderophore system, permitting rapid in-host replication ([PMID: 1872665](https://pubmed.ncbi.nlm.nih.gov/1872665/); [PMID: 16553865](https://pubmed.ncbi.nlm.nih.gov/16553865/)).

---

## 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset / severity / frequency |
|---|---|---|---|
| Fever/chills | Symptom | HP:0001945 (Fever) | Acute; near-universal in septicemia |
| Sepsis / septic shock | Clinical sign | HP:0100806 (Sepsis) | Acute, severe; dominant in primary septicemia (>50% fatal) |
| Hypotension | Clinical sign | HP:0002615 | Acute; predicts poor outcome |
| Cellulitis | Clinical sign | HP:0100658 | Rapidly progressive in wound infection |
| Hemorrhagic bullae / ecchymoses | Skin manifestation | HP:0200041 (Bulla); HP:0031364 | Characteristic; rapid onset |
| Necrotizing fasciitis | Clinical sign | HP:0100806-associated | Severe; surgical emergency; 18% mortality |
| Nausea, vomiting, diarrhea, abdominal pain | GI symptoms | HP:0002018, HP:0002013, HP:0002014, HP:0002027 | Gastroenteritis subtype |
| Leukopenia (<10,000/mm³) | Lab abnormality | HP:0001882 | Mortality marker |
| Thrombocytopenia (<100,000/mm³) | Lab abnormality | HP:0001873 | Mortality marker |
| Elevated creatinine (≥1.3 mg/dL) | Lab abnormality | HP:0003259 | Mortality marker |
| Hypoalbuminemia (<2.5 g/dL) | Lab abnormality | HP:0003073 | Mortality marker |

Most patients "develop sepsis and severe cellulitis progressing rapidly to ecchymoses and bullae" ([PMID: 17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/)). Laboratory markers of mortality in necrotizing fasciitis include leukocytes <10,000/mm³, platelets <100,000/mm³, creatinine ≥1.3 mg/dL, albumin <2.5 g/dL, and multiple skin lesions ([PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/)).

**Onset:** Adult-onset (host predisposition required); acute/fulminant course. **Progression:** Rapid, often within 24–48 h. **Quality-of-life impact:** Extreme per-case burden—V. vulnificus causes >5,800 QALYs lost per 1,000 cases, the highest among 14 US foodborne pathogens ([PMID: 24588853](https://pubmed.ncbi.nlm.nih.gov/24588853/)).

---

## 4. Genetic/Molecular Information

**This is not a human genetic disease**; there are no causal human genes, pathogenic germline variants, chromosomal abnormalities, or epigenetic disease mechanisms. Human "modifier" risk derives from iron-overload genotypes (e.g., HFE hemochromatosis) that raise circulating iron ([PMID: 1872665](https://pubmed.ncbi.nlm.nih.gov/1872665/)).

The relevant genetics are **bacterial (pathogen) virulence genes**:

| Bacterial gene(s) | Product / function |
|---|---|
| *vvhA* | Cytolysin/hemolysin (VvhA); diagnostic marker |
| *rtxA1* | MARTX multifunctional autoprocessing toxin |
| *vvpE* | Elastolytic metalloprotease (VvpE) |
| *wza/wzb* + CPS operon (group 1) | Capsular polysaccharide biosynthesis/export |
| *vvsAB*, *vuuA* | Vulnibactin biosynthesis and ferric-vulnibactin receptor |
| *vcg* (C vs E allele) | Virulence-correlated gene; distinguishes clinical vs environmental type |
| *fur*, *smcR*, *crp*, *fadR*, *rfaH* | Global regulators of iron, quorum sensing, cAMP, fatty-acid metabolism, antitermination |

Virulence-correlated molecular markers—*vcg*, 16S rRNA type, and the CPS operon—differentiate virulent (clinical, "C") from nonvirulent (environmental, "E") strains ([PMID: 20586937](https://pubmed.ncbi.nlm.nih.gov/20586937/)). Clinical C-genotype strains outgrow attenuated environmental strains in vivo ([PMID: 16856938](https://pubmed.ncbi.nlm.nih.gov/16856938/)).

---

## 5. Environmental Information

**Infectious agent:** *Vibrio vulnificus* (NCBI txid672), a halophilic Gram-negative bacillus native to warm (>20 °C), low-to-moderate-salinity estuarine and coastal waters; it bioaccumulates in filter-feeding shellfish, especially oysters.

**Environmental determinants:** Water temperature and salinity govern abundance; **rising incidence of vibriosis is linked to changing climatic conditions that enhance pathogen growth** ([PMID: 37222620](https://pubmed.ncbi.nlm.nih.gov/37222620/)). Warmer waters expand both the geographic range and season of risk.

**Lifestyle factors:** Raw-oyster/shellfish consumption is the dominant ingestion exposure; recreational/occupational seawater contact (fishing, handling shellfish, wading with open wounds) drives wound infections. In Florida surveillance, wounds accounted for 42% of exposures; wound infections (45%) and gastroenteritis (42%) were the most common syndromes ([PMID: 20546636](https://pubmed.ncbi.nlm.nih.gov/20546636/)). Alcohol use is a major indirect factor via alcoholic cirrhosis.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. **Exposure** — Ingestion of contaminated shellfish OR seawater contact with an open wound **introduces** *V. vulnificus* to the gut mucosa or subcutaneous tissue.
2. **Permissive host state** — Host iron overload (cirrhosis/hemochromatosis) and immunocompromise **provide** abundant available iron and blunted clearance.
3. **Iron piracy** — The Fur-regulated **vulnibactin siderophore system (vvsAB) and receptor VuuA strip transferrin-bound iron**, which **enables** rapid bacterial replication (doubling times ~15–28 min in iron-loaded hosts) ([PMID: 10639413](https://pubmed.ncbi.nlm.nih.gov/10639413/); [PMID: 16553865](https://pubmed.ncbi.nlm.nih.gov/16553865/); [PMID: 16856938](https://pubmed.ncbi.nlm.nih.gov/16856938/)).
4. **Immune evasion** — **Capsular polysaccharide (CPS) confers serum/complement resistance**, which **allows** survival in blood; phase variation to the encapsulated opaque form **produces** the virulent phenotype ([PMID: 27859050](https://pubmed.ncbi.nlm.nih.gov/27859050/); [PMID: 16936057](https://pubmed.ncbi.nlm.nih.gov/16936057/)).
5. **Barrier breach (branch A — ingestion route)** — The **MARTX/RtxA1 toxin forms membrane pores and translocates effector domains**, which **induces** intestinal epithelial barrier dysfunction and increased paracellular permeability, **enabling** systemic dissemination from the gut ([PMID: 28060924](https://pubmed.ncbi.nlm.nih.gov/28060924/)).
6. **Tissue injury (branch B — wound route)** — VvhA cytolysin and VvpE metalloprotease, together with MARTX, **cause** cell rounding, apoptosis, then necrosis of soft tissue, **producing** cellulitis → hemorrhagic bullae → necrotizing fasciitis.
7. **Cytokine storm** — Bacterial **lipopolysaccharide (LPS) and capsular LPS trigger release of TNF-α, IL-1β, and IL-6** in a dose-dependent, fatality-correlated manner, which **drives** systemic inflammation ([PMID: 17446960](https://pubmed.ncbi.nlm.nih.gov/17446960/); [PMID: 12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/)).
8. **Septic shock / MODS** — The cytokine cascade **results in** hypotension, disseminated intravascular coagulation, multi-organ dysfunction, and death (>50% in primary septicemia) ([PMID: 17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/)).

### Detail by category

- **Molecular pathways:** LPS→TLR4→NF-κB proinflammatory signaling; Fur/iron, quorum-sensing (SmcR), and cAMP-CRP regulatory circuits controlling virulence-gene expression.
- **Cellular processes:** Pore formation, apoptosis then necrosis of epithelial/endothelial cells, macrophage/monocyte cytokine release, complement evasion, neutrophil recruitment.
- **Protein dysfunction (pathogen-driven host effect):** MARTX effector domains are autoproteolytically released by the cysteine protease domain (CPD) upon binding host inositol hexakisphosphate ([PMID: 28060924](https://pubmed.ncbi.nlm.nih.gov/28060924/)).
- **Metabolic changes:** FadR-regulated fatty-acid metabolism is essential for in-host survival ([PMID: 18835990](https://pubmed.ncbi.nlm.nih.gov/18835990/)); iron acquisition is the central metabolic bottleneck.
- **Immune involvement:** The disease is dominated by dysregulated innate immunity (cytokine storm), not autoimmunity or immunodeficiency per se, though host immunocompromise is permissive.
- **Tissue-damage mechanisms:** Direct cytolysis (VvhA), proteolysis (VvpE), pore-forming toxicity (MARTX), microvascular injury, and hemorrhage/necrosis.

**Suggested GO terms:** GO:0006954 (inflammatory response), GO:0051715 (cytolysis in another organism), GO:0044179 (hemolysis in another organism), GO:0006826 (iron ion transport), GO:0006879 (cellular iron ion homeostasis), GO:0009405 (pathogenesis), GO:0071973 (bacterial-type flagellum-dependent cell motility). **Suggested CL terms:** CL:0000066 (epithelial cell), CL:0000115 (endothelial cell), CL:0000235 (macrophage), CL:0000775 (neutrophil), CL:0000182 (hepatocyte).

---

## 7. Anatomical Structures Affected

- **Primary organs / systems:** Skin and subcutaneous soft tissue (UBERON:0002097 skin; UBERON:0002384 connective tissue) in wound infection; gastrointestinal tract (UBERON:0000160 intestine) in gastroenteritis; blood/circulatory system (UBERON:0000178 blood; UBERON:0004535 cardiovascular system) in septicemia.
- **Secondary organ involvement:** **Liver (UBERON:0002107)** is central—murine data show lethality requires progression from severe skin infection to significant liver infection ([PMID: 21199909](https://pubmed.ncbi.nlm.nih.gov/21199909/)). Multi-organ failure affects kidneys, lungs, and cardiovascular system in septic shock.
- **Tissue/cell level:** Epithelial cells (intestinal, CL:0000066), vascular endothelium (CL:0000115), fascia and muscle in necrotizing fasciitis; monocytes/macrophages as cytokine sources.
- **Subcellular:** Host plasma membrane (GO:0005886) is the target of pore-forming toxins; bacterial outer membrane (GO:0009279) hosts the VuuA receptor.
- **Localization/lateralization:** Wound infections are typically unilateral, often on the extremities; lower-extremity manifestations are well described ([PMID: 7488992](https://pubmed.ncbi.nlm.nih.gov/7488992/)).

---

## 8. Temporal Development

- **Onset:** Adult-onset; acute to fulminant. Symptoms of primary septicemia often begin within 24–48 h of raw-shellfish ingestion; wound infections progress over hours to days.
- **Progression:** Rapid. Most septic deaths occur within 48 h ([PMID: 12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/)). Necrotizing fasciitis is a surgical emergency; treatment delay >3 days independently predicts death ([PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/)).
- **Course pattern:** Acute, self-limited if survived and treated; not chronic or relapsing. Gastroenteritis is usually milder and self-limited.
- **Critical intervention window:** The first ~72 h are decisive—early antibiotics plus surgery within this window is the primary determinant of survival.

---

## 9. Inheritance and Population

- **Inheritance:** Not applicable — infectious, non-heritable disease.
- **Epidemiology:** Rare but severe. *V. vulnificus* is the **leading cause of seafood-related deaths in the United States** ([PMID: 21367733](https://pubmed.ncbi.nlm.nih.gov/21367733/)). Incidence of vibriosis is rising globally with climate change ([PMID: 37222620](https://pubmed.ncbi.nlm.nih.gov/37222620/)). In Florida (1998–2007), among 834 infections, wound infections (45%) and gastroenteritis (42%) predominated ([PMID: 20546636](https://pubmed.ncbi.nlm.nih.gov/20546636/)).
- **Demographics:** Predominantly older adult males with underlying liver disease or immunocompromise.
- **Geographic distribution:** Warm coastal/estuarine regions—Gulf of Mexico and US Atlantic/Gulf coasts, East Asia (Korea, Taiwan, Japan), and expanding poleward with warming seas.
- **Sex ratio:** Male-predominant (linked to alcoholic liver disease prevalence).

---

## 10. Diagnostics

- **Culture:** Isolation of *V. vulnificus* from blood, wound/bulla aspirate, or stool on selective media (e.g., TCBS, CPC agar) is the diagnostic standard.
- **Molecular diagnostics:** Nested and multiplex PCR targeting the hemolysin/cytolysin gene (*vvhA*) directly identify *V. vulnificus* in clinical specimens; nested PCR detected 94.4% of culture-positive septicemic specimens and can detect a single CFU / 1 fg DNA ([PMID: 9738039](https://pubmed.ncbi.nlm.nih.gov/9738039/)). Multiplex PCR using *vvhA*, *vcg*, and the CPS operon simultaneously detects and genotypes strains ([PMID: 20586937](https://pubmed.ncbi.nlm.nih.gov/20586937/)).
- **Laboratory abnormalities / prognostic labs:** Leukopenia, thrombocytopenia, elevated creatinine, hypoalbuminemia, and multiple skin lesions predict mortality ([PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/)).
- **Imaging:** CT/MRI/ultrasound to assess depth of soft-tissue involvement and guide surgical debridement in suspected necrotizing fasciitis.
- **Clinical criteria / differential diagnosis:** Consider in any patient with acute sepsis or rapidly progressive cellulitis/bullae plus a compatible exposure (raw shellfish or seawater) and underlying liver disease. Differentials: streptococcal/staphylococcal necrotizing fasciitis, *Aeromonas* infection, gas gangrene, other vibriosis.
- **Omics/genetic testing:** Not applicable for host diagnosis; strain genotyping (*vcg* C vs E) is a research/risk-characterization tool.

---

## 11. Outcome / Prognosis

| Syndrome | Case-fatality | Source |
|---|---|---|
| Primary septicemia | **>50%** | [PMID: 17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/) |
| Wound infection | **~15%** | [PMID: 17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/) |
| Necrotizing fasciitis (surgical series) | **18%** | [PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/) |
| Sepsis (general) | up to 50%, most deaths <48 h | [PMID: 12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/) |

**Prognostic factors:** Treatment delay >3 days is the dominant modifiable predictor of death (OR 10.75, 95% CI 1.02–113.39, p=0.048) ([PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/)); number of underlying comorbidities increases mortality (P<0.0001) ([PMID: 20546636](https://pubmed.ncbi.nlm.nih.gov/20546636/)). Laboratory markers (leukopenia, thrombocytopenia, high creatinine, low albumin) predict poor outcome.

**Morbidity / QALY burden:** Among survivors, amputation and long-term functional impairment can follow necrotizing infection. Per-case burden is the highest among 14 US foodborne pathogens at **>5,800 QALYs lost per 1,000 cases** ([PMID: 24588853](https://pubmed.ncbi.nlm.nih.gov/24588853/)).

---

## 12. Treatment

**Antimicrobial therapy — combination is superior and synergistic:**
- The recommended backbone is a **third-generation cephalosporin (ceftriaxone/ceftazidime/cefotaxime) plus a tetracycline (doxycycline/minocycline)** ([PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/); [PMID: 12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/)).
- In vitro time-kill studies: cefotaxime + minocycline reduced growth by ~6 orders of magnitude vs either drug alone and sustained inhibition >48 h ([PMID: 9333050](https://pubmed.ncbi.nlm.nih.gov/9333050/)); cefotaxime + ciprofloxacin is also synergistic ([PMID: 16048966](https://pubmed.ncbi.nlm.nih.gov/16048966/)).
- In vivo: in neutropenic mice, cefazolin + minocycline gave 62.5% survival vs death with cefazolin alone (P=0.002) ([PMID: 20093756](https://pubmed.ncbi.nlm.nih.gov/20093756/)); combination cefotaxime + minocycline produced the greatest reduction in lethal proinflammatory cytokines ([PMID: 17446960](https://pubmed.ncbi.nlm.nih.gov/17446960/)). Tetracycline was the animal-study drug of choice ([PMID: 12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/)).

**Surgical / interventional:** Emergency **fasciotomy/debridement** and ICU admission are integral to the multidisciplinary protocol for necrotizing fasciitis ([PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/)). Amputation may be required.

**Supportive care:** Fluid resuscitation, vasopressors, organ support for septic shock.

**Experimental / anti-virulence approaches:** Toxoid nanovaccines and biomimetic nanosponges targeting the VvhA cytolysin neutralize pore-forming toxicity in preclinical models—an anti-virulence strategy ([PMID: 40360045](https://pubmed.ncbi.nlm.nih.gov/40360045/); [PMID: 35743264](https://pubmed.ncbi.nlm.nih.gov/35743264/)).

**Suggested NCIT terms:** NCIT:C305 (Ceftriaxone), NCIT:C1004 (Ceftazidime), NCIT:C544 (Doxycycline), NCIT:C1738 (Minocycline), NCIT:C15325 (Debridement), NCIT:C15329 (Surgical procedure).

---

## 13. Prevention

- **Primary prevention:** Avoid raw/undercooked shellfish and marine-water wound exposure in high-risk individuals (liver disease, immunocompromise, iron overload). **Oyster post-harvest processing** works: California's 2003 regulation reduced raw-oyster-associated *V. vulnificus* illnesses/deaths from up to 6 cases/5 deaths per year to 0 during 2003–2010 (p=0.0005) ([PMID: 23876744](https://pubmed.ncbi.nlm.nih.gov/23876744/)).
- **Public-health interventions:** Consumer/clinician education, shellfish-industry post-harvest treatment (rapid cooling, high-pressure processing, irradiation), water-quality and temperature monitoring; adaptation to climate-driven range expansion ([PMID: 37222620](https://pubmed.ncbi.nlm.nih.gov/37222620/)).
- **Secondary prevention:** Rapid clinical recognition and early empiric combination antibiotics + surgery in exposed at-risk patients (see §12).
- **Immunization:** No licensed human vaccine; toxoid nanovaccines are experimental ([PMID: 40360045](https://pubmed.ncbi.nlm.nih.gov/40360045/)).
- **Prophylaxis:** Prompt wound cleaning after seawater exposure; consider early antibiotics for high-risk hosts with contaminated wounds.

---

## 14. Other Species / Natural Disease

- **Taxonomy / biotypes:** *V. vulnificus* (NCBI txid672) comprises biotypes with distinct host ranges. **Biotype 1** causes most human disease. **Biotype 2** is the etiological agent of **warm-water vibriosis in eels and other teleosts**, especially in fish farms; it emerged via acquisition of a transferable virulence plasmid encoding resistance to fish innate immunity ([PMID: 26185080](https://pubmed.ncbi.nlm.nih.gov/26185080/)).
- **Zoonotic potential:** Biotype 2 **serovar E** is a zoonotic clonal complex that has spread worldwide and can infect humans; it carries RtxA13 (lethal for fish, invasion factor for mice) and transferrin-acquisition genes (vep20 for eel transferrin) ([PMID: 26185080](https://pubmed.ncbi.nlm.nih.gov/26185080/)). Serovar E can acquire quinolone resistance via *gyrA* (Ser83Ile) and *parC* (Ser85Lys) mutations while infecting humans ([PMID: 19218407](https://pubmed.ncbi.nlm.nih.gov/19218407/)).
- **Comparative pathology:** In eels, disease is a hemorrhagic septicemia with head-kidney hematopoietic tissue necrosis; pathology is driven by potent toxic extracellular products rather than massive bacterial growth, and the metalloprotease Vvp is *not* an essential lesional factor ([PMID: 18930131](https://pubmed.ncbi.nlm.nih.gov/18930131/)).
- **Environmental reservoir:** The Eastern oyster (*Crassostrea virginica*) is a key reservoir; CPS, pili, and flagella promote oyster colonization ([PMID: 19689704](https://pubmed.ncbi.nlm.nih.gov/19689704/)).

---

## 15. Model Organisms

- **Standard model:** The **subcutaneously inoculated, iron-dextran-treated mouse** recapitulates human wound infection and sepsis. Lethality requires stepwise progression: severe skin infection → significant liver infection → death; profile-2 genotype strains more often caused lethal systemic infection ([PMID: 21199909](https://pubmed.ncbi.nlm.nih.gov/21199909/)).
- **Iron dependence in the model:** Iron-dextran treatment chiefly increases bacterial growth rate; *V. vulnificus* doubled every ~15–28 min in the first hours of infection ([PMID: 16856938](https://pubmed.ncbi.nlm.nih.gov/16856938/)).
- **Genetic-screen applications:** Signature-tagged/insertion mutagenesis identified *fadR*-regulated fatty-acid metabolism as essential for virulence ([PMID: 18835990](https://pubmed.ncbi.nlm.nih.gov/18835990/)); *vuuA* deletion reduced virulence in an infant-mouse model ([PMID: 10639413](https://pubmed.ncbi.nlm.nih.gov/10639413/)); MARTX effector-domain deletion abolished dissemination from the intestine in an intragastric mouse model ([PMID: 28060924](https://pubmed.ncbi.nlm.nih.gov/28060924/)).
- **Fish model:** The eel (*Anguilla* spp.) is the natural model for biotype-2 warm-water vibriosis ([PMID: 18930131](https://pubmed.ncbi.nlm.nih.gov/18930131/)).
- **Ex vivo human systems:** Human blood, serum, and cirrhotic ascites are used to demonstrate iron-dependent growth and serum resistance ([PMID: 1872665](https://pubmed.ncbi.nlm.nih.gov/1872665/); [PMID: 16553865](https://pubmed.ncbi.nlm.nih.gov/16553865/)).
- **Limitations:** Models require artificial iron loading to reproduce human susceptibility, imperfectly mirroring chronic cirrhotic physiology; oyster models capture environmental persistence but not human immunopathology.

---

## Key Findings (Expanded)

### Finding 1 — Three clinical syndromes
*V. vulnificus* produces **primary septicemia, wound infection, and gastroenteritis** with rapid progression to MODS ([PMID: 31325061](https://pubmed.ncbi.nlm.nih.gov/31325061/)). Florida surveillance of 834 infections found wound infections (45%) and gastroenteritis (42%) most common ([PMID: 20546636](https://pubmed.ncbi.nlm.nih.gov/20546636/)); the two acquisition routes are raw-oyster ingestion (→ sepsis) and seawater wound exposure (→ localized infection) ([PMID: 7488992](https://pubmed.ncbi.nlm.nih.gov/7488992/)).

### Finding 2 — Iron overload and liver disease are the principal host risk factors
Normal blood kills *V. vulnificus*, but blood from hemochromatosis patients—or normal blood with raised transferrin saturation/added iron—supports rapid growth ([PMID: 1872665](https://pubmed.ncbi.nlm.nih.gov/1872665/)). Pathogenicity is reserved for immunocompromised hosts with high serum iron ([PMID: 7488992](https://pubmed.ncbi.nlm.nih.gov/7488992/)); mortality rises with comorbidity count (P<0.0001) ([PMID: 20546636](https://pubmed.ncbi.nlm.nih.gov/20546636/)).

### Finding 3 — Multifactorial virulence arsenal
Strains produce cytolysin/hemolysin (VvhA), RTX/MARTX toxin, metalloprotease, siderophores, CPS, type IV pili, and flagella ([PMID: 23351134](https://pubmed.ncbi.nlm.nih.gov/23351134/)); *vcg* and CPS operon distinguish virulent from nonvirulent strains ([PMID: 20586937](https://pubmed.ncbi.nlm.nih.gov/20586937/)).

### Finding 4 — Treatment delay is the dominant modifiable mortality predictor
In 100 necrotizing-fasciitis cases (18% mortality), delay >3 days independently predicted death (OR 10.75; p=0.048); the protocol combined cephalosporin + tetracycline with emergency fasciotomy and ICU care ([PMID: 24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/)).

### Finding 5 — Leading US seafood-related killer; prevention works
Often from raw oysters, it is the leading cause of US seafood-related deaths ([PMID: 21367733](https://pubmed.ncbi.nlm.nih.gov/21367733/)); California's 2003 post-harvest regulation eliminated raw-oyster-associated cases/deaths (p=0.0005) ([PMID: 23876744](https://pubmed.ncbi.nlm.nih.gov/23876744/)); climate change is raising incidence ([PMID: 37222620](https://pubmed.ncbi.nlm.nih.gov/37222620/)).

### Finding 6 — Iron-dextran mouse model: skin→liver→systemic progression
Lethality requires severe skin infection then significant liver infection ([PMID: 21199909](https://pubmed.ncbi.nlm.nih.gov/21199909/)); *fadR*/fatty-acid metabolism is essential ([PMID: 18835990](https://pubmed.ncbi.nlm.nih.gov/18835990/)); clinical strains outgrow environmental strains in vivo ([PMID: 16856938](https://pubmed.ncbi.nlm.nih.gov/16856938/)).

### Finding 7 — Biotypes and zoonotic serovar E
Biotype 1 causes human disease; biotype 2 causes eel warm-water vibriosis via a transferable virulence plasmid; serovar E is zoonotic and can acquire quinolone resistance (*gyrA*/*parC*) ([PMID: 26185080](https://pubmed.ncbi.nlm.nih.gov/26185080/); [PMID: 19218407](https://pubmed.ncbi.nlm.nih.gov/19218407/); [PMID: 18930131](https://pubmed.ncbi.nlm.nih.gov/18930131/)).

### Finding 8 — Case-fatality: >50% septicemia, ~15% wound
Most patients have ≥1 predisposing immunocompromising condition and progress rapidly to ecchymoses/bullae ([PMID: 17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/)).

### Finding 9 — Cephalosporin + tetracycline synergy
In vitro ~6-log kill vs monotherapy ([PMID: 9333050](https://pubmed.ncbi.nlm.nih.gov/9333050/)); 62.5% murine survival for cefazolin+minocycline (P=0.002) ([PMID: 20093756](https://pubmed.ncbi.nlm.nih.gov/20093756/)); tetracycline the animal drug of choice ([PMID: 12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/)); cefotaxime+ciprofloxacin also synergistic ([PMID: 16048966](https://pubmed.ncbi.nlm.nih.gov/16048966/)).

### Finding 10 — Cytokine storm drives lethality; LPS is core
Serum TNF-α, IL-1β, IL-6 are inoculum-dose-dependent and correlate with fatality; combination antibiotics maximally reduce cytokines ([PMID: 17446960](https://pubmed.ncbi.nlm.nih.gov/17446960/)); LPS, capsular LPS, cytolysin, metalloprotease, and siderophore drive pathogenesis; most septic deaths <48 h ([PMID: 12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/)).

### Finding 11 — MARTX toxin breaches the intestinal barrier
MARTX (up to 5,208 aa) forms membrane pores and translocates effector domains (IP6-activated CPD autoprocessing); the effector region is essential for dissemination from the intestine and induces rapid barrier dysfunction before cell lysis ([PMID: 28060924](https://pubmed.ncbi.nlm.nih.gov/28060924/)).

### Finding 12 — Capsular polysaccharide → serum resistance and virulence
Phase variation switches virulent opaque (CPS+) and attenuated translucent (CPS−) forms; an *rfaH* mutant made negligible CPS and was highly serum-sensitive ([PMID: 27859050](https://pubmed.ncbi.nlm.nih.gov/27859050/)); CPS is an essential virulence factor (~50% fatality) ([PMID: 16936057](https://pubmed.ncbi.nlm.nih.gov/16936057/)); *wzb* deletion locks cells acapsular/translucent ([PMID: 16484211](https://pubmed.ncbi.nlm.nih.gov/16484211/)); CPS aids oyster colonization ([PMID: 19689704](https://pubmed.ncbi.nlm.nih.gov/19689704/)).

### Finding 13 — Highest per-case QALY burden among US foodborne pathogens
>5,800 QALYs lost per 1,000 cases, tying *Listeria* and far exceeding *Toxoplasma* (125), *E. coli* O157:H7 (26), *Salmonella*/*Campylobacter* (16) ([PMID: 24588853](https://pubmed.ncbi.nlm.nih.gov/24588853/)).

### Finding 14 — Fur-regulated vulnibactin system enables transferrin-iron growth
*vuuA* deletion abolished transferrin/vulnibactin iron use and reduced virulence ([PMID: 10639413](https://pubmed.ncbi.nlm.nih.gov/10639413/)); a *crp* mutant could not use transferrin iron and grew poorly in cirrhotic ascites ([PMID: 16553865](https://pubmed.ncbi.nlm.nih.gov/16553865/)); Fur represses *vvsAB* under iron-replete conditions ([PMID: 22696215](https://pubmed.ncbi.nlm.nih.gov/22696215/)).

---

## Mechanistic Model / Interpretation

```
                 RAW SHELLFISH INGESTION          SEAWATER WOUND EXPOSURE
                          │                                 │
                          ▼                                 ▼
              Gut lumen colonization              Subcutaneous inoculation
                          │                                 │
        ┌─────────────────┴─────────────────────────────────┴──────────────┐
        │  PERMISSIVE HOST STATE: iron overload (cirrhosis/hemochromatosis) │
        │  + immunocompromise → abundant free/transferrin-bound iron        │
        └─────────────────────────────┬────────────────────────────────────┘
                                       ▼
        Fur-regulated vulnibactin (vvsAB) + VuuA receptor strip transferrin iron
                                       ▼
        Rapid replication (doubling ~15–28 min)  ── CPS confers serum/complement resistance
                                       ▼
        ┌──────────────── BARRIER BREACH & TISSUE INJURY ─────────────────┐
        │ MARTX/RtxA1 pores + effectors → epithelial barrier failure       │
        │ VvhA cytolysin + VvpE protease → soft-tissue necrosis            │
        └──────────────────────────────┬──────────────────────────────────┘
                                       ▼
        Systemic dissemination → LIVER seeding → bacteremia
                                       ▼
        LPS/capsular LPS → TNF-α, IL-1β, IL-6 (dose-dependent, fatality-linked)
                                       ▼
        SEPTIC SHOCK / DIC / MULTI-ORGAN FAILURE  → death (>50% septicemia, <48 h)
```

The unifying theme is **iron as the master switch**: host iron status determines whether the bacterium is cleared or replicates explosively, and the pathogen's Fur-regulated siderophore machinery is the molecular device that exploits it. Everything downstream—capsule-mediated survival, toxin-mediated barrier breach, and cytokine-driven shock—is contingent on the bacterium first achieving high burden through iron piracy. This explains the tight clinical link to cirrhosis and hemochromatosis and identifies **iron acquisition, CPS, and the toxin trio (MARTX/VvhA/VvpE)** as the highest-value therapeutic targets.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [31325061](https://pubmed.ncbi.nlm.nih.gov/31325061/) | Three clinical subtypes, MODS | Human review/case |
| [20546636](https://pubmed.ncbi.nlm.nih.gov/20546636/) | Syndrome frequencies; comorbidity→death | Human surveillance |
| [7488992](https://pubmed.ncbi.nlm.nih.gov/7488992/) | Two acquisition routes; iron/immunocompromise | Human clinical |
| [1872665](https://pubmed.ncbi.nlm.nih.gov/1872665/) | Iron availability drives susceptibility | Ex vivo human blood |
| [23351134](https://pubmed.ncbi.nlm.nih.gov/23351134/) | Virulence-factor arsenal | In vitro |
| [20586937](https://pubmed.ncbi.nlm.nih.gov/20586937/) | vcg/CPS virulence markers, diagnostics | Molecular |
| [24419406](https://pubmed.ncbi.nlm.nih.gov/24419406/) | Treatment delay OR 10.75; protocol | Human retrospective |
| [21367733](https://pubmed.ncbi.nlm.nih.gov/21367733/) | Leading US seafood death | Review |
| [23876744](https://pubmed.ncbi.nlm.nih.gov/23876744/) | Post-harvest regulation efficacy | Policy epidemiology |
| [37222620](https://pubmed.ncbi.nlm.nih.gov/37222620/) | Climate-driven rise | Environmental |
| [17853628](https://pubmed.ncbi.nlm.nih.gov/17853628/) | Case-fatality rates | Human review |
| [12886957](https://pubmed.ncbi.nlm.nih.gov/12886957/) | LPS/virulence, therapy, <48h deaths | Review |
| [9333050](https://pubmed.ncbi.nlm.nih.gov/9333050/) | Cefotaxime+minocycline synergy | In vitro |
| [20093756](https://pubmed.ncbi.nlm.nih.gov/20093756/) | Combination survival benefit | Mouse |
| [16048966](https://pubmed.ncbi.nlm.nih.gov/16048966/) | Cefotaxime+ciprofloxacin synergy | In vitro |
| [17446960](https://pubmed.ncbi.nlm.nih.gov/17446960/) | Cytokine storm & antibiotic effect | Mouse |
| [28060924](https://pubmed.ncbi.nlm.nih.gov/28060924/) | MARTX barrier breach & spread | In vitro + mouse |
| [27859050](https://pubmed.ncbi.nlm.nih.gov/27859050/) | RfaH/CPS serum resistance | In vitro |
| [16936057](https://pubmed.ncbi.nlm.nih.gov/16936057/) | CPS essential; phase variation | In vitro |
| [16484211](https://pubmed.ncbi.nlm.nih.gov/16484211/) | CPS operon genetics | Molecular |
| [19689704](https://pubmed.ncbi.nlm.nih.gov/19689704/) | CPS/pili/flagella oyster uptake | Oyster model |
| [24588853](https://pubmed.ncbi.nlm.nih.gov/24588853/) | QALY burden ranking | Modeling |
| [10639413](https://pubmed.ncbi.nlm.nih.gov/10639413/) | VuuA transferrin-iron & virulence | Mouse/molecular |
| [16553865](https://pubmed.ncbi.nlm.nih.gov/16553865/) | crp, growth in cirrhotic ascites | Ex vivo human fluid |
| [22696215](https://pubmed.ncbi.nlm.nih.gov/22696215/) | Fur/iron/QS regulation of vulnibactin | Molecular |
| [21199909](https://pubmed.ncbi.nlm.nih.gov/21199909/) | Skin→liver→death model | Mouse |
| [18835990](https://pubmed.ncbi.nlm.nih.gov/18835990/) | fadR essential for virulence | Mouse |
| [16856938](https://pubmed.ncbi.nlm.nih.gov/16856938/) | Growth-rate basis of virulence | Mouse |
| [26185080](https://pubmed.ncbi.nlm.nih.gov/26185080/) | Biotype 2 / serovar E zoonosis | Review |
| [19218407](https://pubmed.ncbi.nlm.nih.gov/19218407/) | Quinolone resistance gyrA/parC | Molecular |
| [18930131](https://pubmed.ncbi.nlm.nih.gov/18930131/) | Eel pathology | Fish model |
| [9738039](https://pubmed.ncbi.nlm.nih.gov/9738039/) | Nested PCR diagnostics | Clinical/molecular |
| [40360045](https://pubmed.ncbi.nlm.nih.gov/40360045/) | Anti-VvhA toxoid nanovaccine | Preclinical |
| [35743264](https://pubmed.ncbi.nlm.nih.gov/35743264/) | Nanosponge detoxification | Preclinical |

---

## Limitations and Knowledge Gaps

1. **No randomized controlled trials** of antibiotic regimens exist; therapy recommendations rest on in vitro synergy, murine survival data, and retrospective human series—susceptible to confounding and small samples (the necrotizing-fasciitis OR had a very wide CI, 1.02–113.39).
2. **Human host-genetic susceptibility beyond iron-overload states is uncharacterized**; no GWAS or defined immune-gene modifiers.
3. **Cytokine-storm data are largely murine**; the precise human immunopathology and any role for immunomodulation (e.g., anti-cytokine adjuncts) remain untested clinically.
4. **True incidence is underreported** owing to poor clinical recognition and laboratory detection, limiting epidemiologic precision.
5. **Animal models require artificial iron loading**, imperfectly mirroring chronic cirrhotic physiology.
6. **Anti-virulence therapeutics** (toxoid vaccines, nanosponges) are preclinical only, with no human data.
7. **Climate-attributable range expansion** is documented at the vibriosis level but the future *V. vulnificus*-specific burden is not precisely quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective multicenter cohort/registry** to validate the treatment-delay threshold and mortality predictors (leukopenia, thrombocytopenia, creatinine, albumin) with adequate power and tighter confidence intervals.
2. **Pragmatic RCT or comparative-effectiveness study** of cephalosporin+tetracycline vs cephalosporin+fluoroquinolone combinations, incorporating time-to-antibiotic and time-to-surgery.
3. **Human immunoprofiling** of TNF-α/IL-1β/IL-6 trajectories to test whether early cytokine levels stratify risk and whether targeted immunomodulation adds benefit to antibiotics + surgery.
4. **Host-genetic study** of iron-regulatory genotypes (HFE, TF, TMPRSS6) and outcome, to refine risk stratification beyond clinical comorbidity.
5. **Advance anti-virulence candidates** (VvhA toxoid nanovaccine, iron-uptake/vulnibactin inhibitors, MARTX blockers) from murine into safety-focused translational studies.
6. **Climate-linked forecasting** integrating sea-surface temperature/salinity to guide targeted public-health warnings and shellfish post-harvest policy expansion.
7. **Point-of-care rapid diagnostics** (e.g., vvhA LAMP/PCR) validation to shorten time-to-targeted therapy in emergency settings.

---

*Report compiled from 14 confirmed findings and 37 primary papers across all 15 disease-characteristic domains. Evidence types are distinguished as human clinical, surveillance/epidemiologic, ex vivo human, mouse/fish model, in vitro, molecular, and computational/modeling throughout.*


## Artifacts

- [OpenScientist final report](Vibrio_Vulnificus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Vibrio_Vulnificus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 34 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:17853628` *(abstract only)*: "develop sepsis and severe cellulitis progressing rapidly to ecchymoses and bullae"
  - closest text in source: "Most patients, including those with primary infection, develop sepsis and severe cellulitis with rapid development to ecchymoses and bullae"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 28 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002615` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotension**
- `HP:0100658` (1 mention) - the report calls it "Clinical sign"; HP calls it **Cellulitis**
- `HP:0001882` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total leukocyte count**
- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0003259` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Elevated circulating creatinine concentration**
- `HP:0003073` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypoalbuminemia**
- `UBERON:0002107` (1 mention) - the report calls it "Secondary organ involvement:** **Liver"; UBERON calls it **liver**
- `NCIT:C305` (1 mention) - the report calls it "Ceftriaxone"; NCIT calls it **Bilirubin**
- `NCIT:C1004` (1 mention) - the report calls it "Ceftazidime"; NCIT calls it **Antineoplaston A10**
- `NCIT:C544` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Altretamine**
- `NCIT:C1738` (1 mention) - the report calls it "Minocycline"; NCIT calls it **Amphotericin B Liposomal**
- `NCIT:C15325` (1 mention) - the report calls it "Debridement"; NCIT calls it **Skin Transplantation**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (1 mention)
- `NCIT:C1738` (Amphotericin B Liposomal) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006879` (1 mention) - the report calls it "cellular iron ion homeostasis"; GO calls it **intracellular iron ion homeostasis**, and lists "cellular iron ion homeostasis" among its other names
- `GO:0009405` (1 mention) - the report calls it "pathogenesis"; GO calls it **obsolete pathogenesis**
- `GO:0005886` (1 mention) - the report calls it "Subcellular:** Host plasma membrane"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names