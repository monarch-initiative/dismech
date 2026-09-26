---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T02:03:08.912841'
end_time: '2026-09-25T02:22:55.632418'
duration_seconds: 1186.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Relapsing Fever
  mondo_id: MONDO:0019633
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
citation_count: 30
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 30
  on_topic: 27
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 38
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 2
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0001903
    reported_labels:
    - 74.7% (severe cohort)
    ontology_label: Anemia
  - term_id: HP:0001873
    reported_labels:
    - most suggestive lab finding
    ontology_label: Thrombocytopenia
  - term_id: HP:0033677
    reported_labels:
    - "54.6\u201369.7% (severe cohort)"
    ontology_label: Acute respiratory distress syndrome
  - term_id: HP:0031273
    reported_labels:
    - 60.5% (severe cohort)
    ontology_label: Shock
  - term_id: HP:0002315
    reported_labels:
    - common
    ontology_label: Headache
  - term_id: HP:0001433
    reported_labels:
    - common
    ontology_label: Hepatosplenomegaly
  - term_id: HP:0011446
    reported_labels:
    - 46.2% severe cohort; meningoencephalitis in immunocompromised
    ontology_label: Abnormality of mental function
  - term_id: HP:0000979
    reported_labels:
    - common in LBRF
    ontology_label: Purpura
  - term_id: NCIT:C299
    reported_labels:
    - "tetracyclines \u2014 doxycycline"
    - "First-line pharmacotherapy:** **tetracyclines \u2014 doxycycline"
    ontology_label: Beclomethasone Dipropionate
  - term_id: NCIT:C716
    reported_labels:
    - penicillin
    ontology_label: Omeprazole
  - term_id: NCIT:C1638
    reported_labels:
    - ceftriaxone
    ontology_label: Carbon C-14
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Relapsing_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Relapsing_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Relapsing Fever
- **MONDO ID:** MONDO:0019633 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Relapsing Fever** covering all of the
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

# Relapsing Fever (MONDO:0019633): Comprehensive Disease Characteristics Report

**Disease:** Relapsing Fever · **MONDO:** MONDO:0019633 · **Category:** Infectious Disease (vector-borne bacterial zoonosis / epidemic infection)

> **Evidence-source note:** Relapsing fever (RF) is an **infectious, non-heritable** disease. Template sections that assume a Mendelian/genetic etiology (causal human genes, pathogenic variants, inheritance pattern, penetrance, karyotype/FISH, carrier screening, genetic counseling) are **Not Applicable to the human host**; the relevant "genetics" is that of the *pathogen* (Borrelia antigenic-variation loci) and of *host susceptibility/immune-control genes* studied in mice. Evidence below is drawn from aggregated disease-level resources plus primary human-clinical, model-organism, and in-vitro literature (49 papers reviewed; PMIDs cited throughout).

## Summary

**Relapsing fever (RF)** is an acute, arthropod-borne bacterial infection caused by spirochetes of the genus *Borrelia*, characterized by recurring waves of high fever separated by afebrile intervals. It is an **infectious, non-heritable disease**; the human genome does not "cause" it. The genetics that matter are those of the **pathogen's antigenic-variation loci** and of **murine host-susceptibility genes** used in experimental models. RF exists in two principal epidemiological forms: **louse-borne relapsing fever (LBRF)**, caused by *Borrelia recurrentis* and transmitted by the human body louse (*Pediculus humanus humanus*), and **tick-borne relapsing fever (TBRF)**, caused by numerous species (*B. hermsii*, *B. duttonii*, *B. crocidurae*, *B. hispanica*, *B. persica*, *B. turicatae*, and the emerging hard-tick species *B. miyamotoi*) transmitted by soft ticks (*Ornithodoros* spp.) or *Ixodes* hard ticks.

The **defining mechanistic feature** of the disease — the relapse phenomenon — is driven by **multiphasic antigenic variation of the variable major proteins (Vmps)** on the spirochete outer surface. Through nonreciprocal gene conversion, one of roughly 60 silent *vmp* gene archives is placed downstream of a single active promoter, allowing the population to serially switch its dominant surface antigen and repeatedly evade the host antibody response. Each bacteremic wave is cleared by a **T-independent, B1b-lymphocyte-derived IgM** response, but escape variants seed the next relapse. This produces the pathognomonic sawtooth fever curve.

Clinically, RF causes high fever, chills, headache, myalgia, hepatosplenomegaly, thrombocytopenia and anemia, and — in severe/untreated cases — ARDS, shock, myocarditis, hemorrhage, and death (up to ~70% untreated in LBRF). Diagnosis rests on **direct visualization of spirochetes on stained (Giemsa/Wright) blood films** during febrile peaks, supplemented by 16S rRNA PCR and GlpQ serology. Treatment is with **tetracyclines (doxycycline), penicillin, or ceftriaxone**, and frequently triggers a **Jarisch-Herxheimer reaction (JHR)** — a TNF-α/IL-6/IL-8-driven cytokine storm coincident with antibiotic-induced spirochete lysis. Prevention relies on vector avoidance, delousing (LBRF), and doxycycline post-exposure prophylaxis (TBRF); no vaccine exists.

---

## Key Findings

### Finding 1 — Antigenic variation of variable major proteins (Vmps) drives the relapse phenomenon

The central molecular mechanism of relapsing fever is the multiphasic antigenic variation of surface-exposed **variable major proteins (Vmps)**, which comprise **variable large proteins (Vlp)** and **variable small proteins (Vsp)**. In *B. hermsii*, antigenic variation occurs through a **nonreciprocal gene conversion event** that places one of approximately 60 silent *vmp* genes downstream of a single, transcriptionally active promoter (the "expression site") ([PMID: 29250931](https://pubmed.ncbi.nlm.nih.gov/29250931/)). Silent *vmp* gene archives reside on linear plasmids — for example, the 44-kb linear plasmid of *B. duttonii* strain Ly preserves ~21 *vmp* homologues, most rendered non-functional by frameshifts or missing promoters, serving as an archive for serotype switching ([PMID: 12008924](https://pubmed.ncbi.nlm.nih.gov/12008924/)). Expression is also controlled by switching between expression sites at the transcriptional level ([PMID: 11083837](https://pubmed.ncbi.nlm.nih.gov/11083837/)).

The functional necessity of this system is demonstrated by loss-of-function experiments: **deletion of the expression site or mutation of the flanking cis-acting UHS/DHS inverted repeats renders spirochetes unable to relapse in immunocompetent mice** ([PMID: 29250931](https://pubmed.ncbi.nlm.nih.gov/29250931/)), and a **Vmp-null mutant could not relapse and had lower blood densities** ([PMID: 24699793](https://pubmed.ncbi.nlm.nih.gov/24699793/)). As the abstract states: *"the spirochetes repeatedly evade the host's acquired immune response by undergoing antigenic variation of the variable major proteins (Vmps) produced on their outer surface. This mechanism prolongs spirochete circulation in blood"* ([PMID: 24699793](https://pubmed.ncbi.nlm.nih.gov/24699793/)). The primary defining quote from the mechanism paper: *"In Borrelia hermsii, antigenic variation occurs as a result of a nonreciprocal gene conversion event that places one of ~60 silent variable major protein genes downstream of a single, transcriptionally active promoter"* ([PMID: 29250931](https://pubmed.ncbi.nlm.nih.gov/29250931/)).

### Finding 2 — Relapsing fever causes high untreated mortality with anemia, ARDS, shock, and JHR as leading complications

A retrospective study of 119 blood-film-confirmed RF patients in a resource-limited Ethiopian setting (mean age 24.1 years, mostly daily laborers and homeless persons) quantified the clinical burden. Leading symptoms were fever (85.5%), chills (67.2%), respiratory distress (54.6%), and altered mental status (46.2%). **Complications occurred in 88.2% of cases** — anemia (74.7%), acute respiratory distress syndrome (69.7%), shock (60.5%), and Jarisch-Herxheimer reaction (36.1%) — with an **in-hospital mortality of 45.4%** ([PMID: 41418926](https://pubmed.ncbi.nlm.nih.gov/41418926/)). Untreated mortality may reach **70%** ([PMID: 41418926](https://pubmed.ncbi.nlm.nih.gov/41418926/)).

| Clinical feature | Frequency (%) |
|---|---|
| Fever | 85.5 |
| Chills | 67.2 |
| Respiratory distress | 54.6 |
| Altered mental status | 46.2 |
| **Any complication** | **88.2** |
| Anemia | 74.7 |
| ARDS | 69.7 |
| Shock | 60.5 |
| Jarisch-Herxheimer reaction | 36.1 |
| **In-hospital mortality** | **45.4** |

Direct quotes: *"Complications were observed in 88.2% of cases, most commonly anemia (74.7%), acute respiratory distress syndrome (69.7%), shock (60.5%), and Jarisch-Herxheimer reaction (36.1%). Mortality was 45.4%"* and *"Mortality may reach 70% without treatment"* ([PMID: 41418926](https://pubmed.ncbi.nlm.nih.gov/41418926/)). The Jarisch-Herxheimer reaction is *"a transient response that occurs within 24 hours of antibiotic treatment for spirochete infections, such as syphilis, leptospirosis, Lyme disease, and relapsing fever, and can present with nausea, fever, chills, rigors, vomiting, hypotension, and skin lesions"* ([PMID: 40624823](https://pubmed.ncbi.nlm.nih.gov/40624823/)).

**HPO term suggestions:** Fever (HP:0001945), Recurrent fever (HP:0001954), Anemia (HP:0001903), Thrombocytopenia (HP:0001873), Splenomegaly (HP:0001744), Hepatomegaly (HP:0002240), Acute respiratory distress syndrome (HP:0033677), Shock (HP:0031273).

### Finding 3 — Anemia and thrombocytopenia arise from spirochete–erythrocyte interaction and macrophage-mediated clearance

In inbred mouse models of *B. hermsii* infection, susceptibility is genetically controlled, and disease progression is associated with **thrombocytopenia and anemia mirroring human infection**. Histological and fluorescence in situ hybridization (FISH) analyses showed that **red blood cells are removed by tissue-resident macrophages in spleen and liver**, and spirochetes were frequently visualized associated with RBCs, supporting a direct spirochete–RBC interaction that leads to bacterial clearance and anemia ([PMID: 19995898](https://pubmed.ncbi.nlm.nih.gov/19995898/)). The study found: *"the progression of the disease in mice was associated with thrombocytopenia and anemia. Histological and fluorescence in situ hybridization (FISH) analysis of infected tissues indicated that red blood cells (RBCs) were removed by tissue-resident macrophages, a process that could lead to anemia. Spirochetes in the spleen and liver were often visualized associated with RBCs."* Both innate and adaptive immunity contribute to reducing bacterial burden: *"we found that innate immunity contributes significantly to the reduction of bacterial burden"* ([PMID: 19995898](https://pubmed.ncbi.nlm.nih.gov/19995898/)).

**Cell types (CL) / anatomy (UBERON):** macrophage (CL:0000235), erythrocyte (CL:0000232), spleen (UBERON:0002106), liver (UBERON:0002107).

### Finding 4 — *Borrelia miyamotoi* is an emerging hard-tick relapsing fever spirochete

*B. miyamotoi* represents a paradigm shift: unlike classic soft-tick/louse RF, it is transmitted by *Ixodes ricinus*-complex **hard ticks**, with rodents as reservoirs. It is *"an emerging tick-borne pathogen phylogenetically belonging to spirochaetes causing relapsing fever. It is primarily transmitted by ticks from the Ixodes ricinus complex"* ([PMID: 34412488](https://pubmed.ncbi.nlm.nih.gov/34412488/)). More than 200 human cases have been described: *"To date more than 200 human cases have been described including five cases of meningoencephalitis in immunocompromised patients"* ([PMID: 34412488](https://pubmed.ncbi.nlm.nih.gov/34412488/)). Presentation is nonspecific (fever, fatigue, chills, headache, myalgia, arthralgia), and infection is treatable with antibiotics. A Minnesota meningoencephalitis case was diagnosed by CSF Gram stain plus sequencing ([PMID: 38916722](https://pubmed.ncbi.nlm.nih.gov/38916722/)). Diagnosis relies on *"direct (PCR) and indirect diagnosis (glycerophosphoryldiester-phosphodiesterase (GlpQ) serology)"*, and *B. miyamotoi* was found in 2.2% of *I. ricinus* ticks in Alsace, France ([PMID: 32303256](https://pubmed.ncbi.nlm.nih.gov/32303256/)).

### Finding 5 — TBRF in pregnancy causes very high perinatal mortality

A case-control study in rural Tanzania (137 pregnant vs 120 non-pregnant women with TBRF, 1985–1995) documented severe pregnancy outcomes: *"Risk of birth during the attack of TBRF was 58.0%, with an extremely high perinatal mortality of 436 per 1000 births. The total loss of pregnancies including abortions was 475"* per 1000 ([PMID: 9351408](https://pubmed.ncbi.nlm.nih.gov/9351408/)). Maternal case-fatality was low and similar between groups (1.5% pregnant vs 1.7% non-pregnant), but **pregnant women showed significantly higher spirochete densities**: *"Pregnant women with TBRF show higher densities of spirochetes than non-pregnant women (p < 0.001)"* ([PMID: 9351408](https://pubmed.ncbi.nlm.nih.gov/9351408/)). Delivery during an attack correlated with spirochetemia density (p<0.001) and gestational age (p<0.001); perinatal death was related to low birthweight and low gestational age rather than the degree of spirochetemia. The mechanistic driver of perinatal loss is therefore **preterm delivery precipitated by the febrile attack**.

### Finding 6 — LBRF re-emerged in Europe among East African migrants (2015)

Louse-borne relapsing fever (*B. recurrentis*, transmitted by the *Pediculus humanus humanus* body louse — *"Borrelia recurrentis, transmitted by Pediculus humanus humanus, is the etiological agent of louse-borne relapsing fever (LBRF)"* [PMID: 26938933](https://pubmed.ncbi.nlm.nih.gov/26938933/)) is endemic to the Horn of Africa (Ethiopia, Somalia, Sudan, Eritrea). In 2015, approximately 26–45 imported cases were diagnosed in migrants across Italy, Switzerland, the Netherlands, and Germany — a marked re-emergence after nearly a decade with essentially no imported European cases. A systematic search *"identified 26 cases of LBRF between July and October 2015 in migrants recently arrived in Europe"* ([PMID: 27340042](https://pubmed.ncbi.nlm.nih.gov/27340042/)). Diagnosis was made by microscopy: *"Multiple spirochetes were visualized on stained blood films which were identified as Borrelia recurrentis by 16S rRNA gene sequencing. All patients recovered after antibiotic treatment with ceftriaxone and/or doxycycline"* ([PMID: 27188655](https://pubmed.ncbi.nlm.nih.gov/27188655/)). Meningeal involvement with neck stiffness, CSF pleocytosis and thrombocytopenia was documented and treated with doxycycline plus ceftriaxone ([PMID: 26938933](https://pubmed.ncbi.nlm.nih.gov/26938933/)). Concurrent malaria and tuberculosis co-infections occurred in half of a Swiss case series ([PMID: 27188655](https://pubmed.ncbi.nlm.nih.gov/27188655/)).

### Finding 7 — TBRF is a zoonosis maintained in *Ornithodoros* soft-tick/small-mammal enzootic cycles

Tick-borne relapsing fever spirochetes *"of genus Borrelia thrive in enzootic cycles involving Ornithodoros spp. (Argasidae) mainly, and rodents"* ([PMID: 38321309](https://pubmed.ncbi.nlm.nih.gov/38321309/)). The disease is highly region-specific in its species/vector pairings:

| Region | *Borrelia* species | Vector (*Ornithodoros*) | Reservoir / evidence |
|---|---|---|---|
| West Africa | *B. crocidurae* | *O. sonrai* (rodent-burrow) | 9.2% (287/3109) small mammals infected where vector present vs 0/1004 where absent; *Gerbillus* spp. reservoirs ([PMID: 26327444](https://pubmed.ncbi.nlm.nih.gov/26327444/)) |
| Iberian Peninsula | *B. hispanica* | *O. erraticus* (pigpen) | Blood-meal analysis 46.8% pig, 35.4% human ([PMID: 23808979](https://pubmed.ncbi.nlm.nih.gov/23808979/)) |
| Western North America | *B. hermsii* | *O. hermsi* | Wild rodents; RF spirochetes in 7.7% Nevada mule deer ([PMID: 21995265](https://pubmed.ncbi.nlm.nih.gov/21995265/)) |
| Middle East | *B. persica* | *O. tholozani* | Wildlife reservoirs; mainly transstadial transfer ([PMID: 33741637](https://pubmed.ncbi.nlm.nih.gov/33741637/)) |

The West African data are especially clear: *"In areas with O. sonrai, Borrelia infection was demonstrated in 287 of 3109 (9.2%) small mammals tested, and none was documented in 1004 animals tested from other areas"* ([PMID: 26327444](https://pubmed.ncbi.nlm.nih.gov/26327444/)). The Iberian vector pairing: *"this tick serves as the vector of human tick-borne relapsing fever caused by the spirochete Borrelia hispanica"* ([PMID: 23808979](https://pubmed.ncbi.nlm.nih.gov/23808979/)).

### Finding 8 — The Jarisch-Herxheimer reaction is a TNF-α/IL-6/IL-8 cytokine storm suppressible by anti-TNF-α antibody

In LBRF (*B. recurrentis*), penicillin treatment triggers the JHR with fever, rigors, and hypotension, coincident with **7-, 6-, and 4-fold transient rises in plasma TNF, IL-6, and IL-8**, respectively; these cytokine elevations were absent in the 3/17 patients without JHR, and spirochetes cleared from blood ~5 hours after penicillin ([PMID: 1569394](https://pubmed.ncbi.nlm.nih.gov/1569394/)). The abstract reports *"a seven-, six-, and fourfold elevation of these plasma cytokine concentrations over admission levels was detected, respectively, occurring in transient form coincidental with observed pathophysiological changes of J-HR."*

Causality was established by a randomized double-blind placebo-controlled trial (n=49): sheep **anti-TNF-α Fab given before penicillin reduced JHR with rigors** from 26/29 (controls) to 10/20 (P=0.006), and blunted the rises in temperature (0.8 vs 1.5°C, P<0.001), pulse, blood pressure, and peak IL-6 (17 vs 50 µg/L) and IL-8 (205 vs 2000 ng/L) ([PMID: 8663853](https://pubmed.ncbi.nlm.nih.gov/8663853/)). As stated: *"Ten of the 20 patients given anti-TNF-alpha Fab had Jarisch-Herxheimer reactions with rigors, as compared with 26 of the 29 control patients (P = 0.006)."* This provides direct interventional evidence that TNF-α is the proximal mediator of the JHR.

### Finding 9 — Contemporary epidemiology: *B. miyamotoi* surveillance in the US and RF burden in West Africa

US surveillance across 9 Northeast/Midwest states (2013–2019) identified **300 *B. miyamotoi* cases** (166 confirmed, 134 possible): *"During 2013-2019, a total of 300 cases were identified through surveillance; 166 (55%) were classified as confirmed and 134 (45%) as possible. Median age of case-patients was 52 years (range 1-86 years); 52% were male. Most cases (70%) occurred during June-September"* ([PMID: 37610298](https://pubmed.ncbi.nlm.nih.gov/37610298/)). Fever and headache were common, 28% reported recurring fevers, 55% arthralgia, 16% rash, 13% were hospitalized, and there were no deaths. *B. miyamotoi* is present in questing *Ixodes scapularis* across all 67 Pennsylvania counties (positive pools in 38 counties) ([PMID: 38686844](https://pubmed.ncbi.nlm.nih.gov/38686844/)). In Senegal, metagenomic sequencing of non-malarial febrile illness detected relapsing fever *Borrelia* in **15.5% of cases — the single most common pathogen**: *"Bacteria were the most common, with relapsing fever Borrelia and spotted fever Rickettsia found in 15.5% and 3.8% of cases, respectively"* ([PMID: 38272885](https://pubmed.ncbi.nlm.nih.gov/38272885/)).

### Finding 10 — Resolution of each bacteremic episode requires T-independent IgM produced by B1b lymphocytes

The immune clearance of each relapse wave is a T-independent process. SCID or Rag−/− mice cannot resolve *B. hermsii* infection (they require T/B cells). However, T-cell-deficient TCR−/− and IL-7−/− mice (which lack T cells and follicular B cells but retain B1 and marginal-zone B cells) efficiently cleared the bacterium, and splenectomized mice still cleared it (ruling out a primary marginal-zone B-cell role). *xid* mice (B1-cell deficient) suffered more severe bacteremia, and a selective expansion of the **B1b subset (IgM-high, IgD−/low, Mac1+, CD23−, CD5−)** coincided with resolution: *"a selective expansion of the B1b (i.e., IgM(high), IgD(-/low), Mac1(+) CD23(-), and CD5(-)) cell subset in infected xid mice, which coincided with the eventual resolution of infection"*. Critically, *"mice selectively incapable of secreting IgM, the dominant isotype produced by B1 cells, were completely unable to clear B. hermsii"* ([PMID: 12646649](https://pubmed.ncbi.nlm.nih.gov/12646649/)).

**Cell type (CL):** B-1b B cell (CL:0000821); GO: immunoglobulin production (GO:0002377), humoral immune response (GO:0006959).

### Finding 11 — Dissemination via hijacked plasminogen/plasmin and adhesins; TLR signaling required for protective antibody

RF spirochetes disseminate through host tissues by exploiting the host fibrinolytic system. *B. hermsii* and *B. recurrentis* bind host **plasminogen (Plg)** on their surface and generate **plasmin (Pla)**; spirochetes with Pla activity *"have been shown to degrade extracellular matrix (ECM) components, in addition to digesting fibrin, facilitating bacterial invasion and dissemination"* ([PMID: 25914944](https://pubmed.ncbi.nlm.nih.gov/25914944/)). Borrelia adhesins mediate attachment to cell-surface molecules and to soluble proteins/ECM, cloaking the surface from immune recognition and facilitating tissue colonization ([PMID: 21557056](https://pubmed.ncbi.nlm.nih.gov/21557056/)). On the host side, controlling infection relies on a rapid humoral response, and beyond B-cell receptor signaling, *"growing evidence suggests that additional signaling by innate immune receptors such as Toll-like receptors is necessary for optimal T cell-dependent and T cell-independent antibody responses"* to Borreliae ([PMID: 22202086](https://pubmed.ncbi.nlm.nih.gov/22202086/)).

**GO terms:** plasminogen activation (GO:0031639), proteolysis (GO:0006508), Toll-like receptor signaling pathway (GO:0002224).

### Finding 12 — Natural rodent reservoirs tolerate RF *Borrelia*; laboratory mice are the principal disease model

North American deer mice *Peromyscus leucopus* and *P. maniculatus* are important natural reservoirs for hard-tick relapsing fever (and several other zoonoses); despite high prevalence of persistent infection they display little pathology, exhibiting both **partial resistance** (limiting pathogen burden) and **infection tolerance** (reducing damage): *"they appear to have partial resistance, which limits the burden of the pathogen. In addition, they display traits of infection tolerance, which reduces the damage of the infection"* ([PMID: 27381345](https://pubmed.ncbi.nlm.nih.gov/27381345/)). *Peromyscus* are identified as *"important natural reservoirs for several zoonotic diseases of humans: Lyme disease, human granulocytic anaplasmosis, babesiosis, erhlichiosis, hard tickborne relapsing fever"* ([PMID: 27381345](https://pubmed.ncbi.nlm.nih.gov/27381345/)). In West Africa, *Gerbillus* spp. serve as reservoirs for *B. crocidurae* ([PMID: 26327444](https://pubmed.ncbi.nlm.nih.gov/26327444/)). **Inbred laboratory mice** (both immunocompetent and immunodeficient strains) are the standard experimental model, recapitulating relapsing bacteremia, antigenic variation, thrombocytopenia and anemia ([PMID: 19995898](https://pubmed.ncbi.nlm.nih.gov/19995898/); [PMID: 12646649](https://pubmed.ncbi.nlm.nih.gov/12646649/); [PMID: 24699793](https://pubmed.ncbi.nlm.nih.gov/24699793/)); guinea pigs are used for tick-transmission competence studies ([PMID: 38321309](https://pubmed.ncbi.nlm.nih.gov/38321309/)).

**NCBI Taxonomy:** *Peromyscus leucopus* (txid10041), *Gerbillus* (txid10045), *Mus musculus* (txid10090).

### Finding 13 — Prevention rests on vector avoidance/surveillance and doxycycline post-exposure prophylaxis; no vaccine

In TBRF-endemic Israel, prevention among at-risk military personnel is based on *"heightened awareness and risk stratification by active surveillance of tick bites and selective postexposure prophylaxis (PEP) with doxycycline for tick-bitten individuals"* ([PMID: 24107216](https://pubmed.ncbi.nlm.nih.gov/24107216/)). Across three outbreaks (35 exposed), tick-bite recognition was only ~50% and the attack rate 25–50%; 20% of TBRF cases had no recognized tick bite. After a revised cohort-based policy, *"24 soldiers (including eight with recognized and 16 with unrecognized tick bites) received antimicrobials following the diagnosis of TBRF among their cohorts, and none of these individuals subsequently developed TBRF"* ([PMID: 24107216](https://pubmed.ncbi.nlm.nih.gov/24107216/)). **No licensed vaccine exists** for relapsing fever; primary prevention is environmental and behavioral (delousing/hygiene for LBRF; tick avoidance and rodent-proofing of dwellings for TBRF).

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Relapsing fever is an acute febrile spirochetal zoonosis/anthroponosis characterized by recurring episodes of fever separated by afebrile intervals, caused by *Borrelia* species. It presents as an undifferentiated febrile illness that is frequently confused with malaria, typhoid, dengue, and leptospirosis.

**Key identifiers:**
- **MONDO:** MONDO:0019633 (relapsing fever)
- **MeSH:** Relapsing Fever (D012061)
- **ICD-10:** A68 (A68.0 louse-borne; A68.1 tick-borne; A68.9 unspecified)
- **ICD-11:** 1C1B
- **Not applicable:** OMIM and Orphanet Mendelian-disease identifiers — RF is an infectious, non-heritable disease, so it is not a classic OMIM/Orphanet genetic entry.

**Synonyms/alternative names:** recurrent fever, famine fever, tick fever, spirochetal fever; louse-borne relapsing fever (LBRF; epidemic relapsing fever); tick-borne relapsing fever (TBRF; endemic relapsing fever); *Borrelia miyamotoi* disease (hard-tick relapsing fever).

**Information source.** Evidence is drawn from **aggregated disease-level resources** — clinical case series, hospital cohorts, systematic reviews, and experimental animal studies — rather than a single EHR-derived individual-patient dataset.

### 2. Etiology

**Causal factor: infectious.** RF is caused entirely by *Borrelia* spirochetes; there is **no genetic (human heritable) etiology**. The primary agents are *B. recurrentis* (LBRF) and multiple TBRF species (*B. hermsii*, *B. duttonii*, *B. crocidurae*, *B. hispanica*, *B. persica*, *B. turicatae*, *B. miyamotoi*, and others).

**Environmental / risk factors.** Poverty, overcrowding, homelessness, war, famine, and refugee movements favor body-louse infestation and LBRF ([PMID: 27340042](https://pubmed.ncbi.nlm.nih.gov/27340042/)). Occupational/recreational exposure to *Ornithodoros*-infested rodent burrows, caves, and rustic cabins drives TBRF. **Pregnancy** is a major risk factor for severe outcomes (higher spirochetemia, high perinatal mortality) ([PMID: 9351408](https://pubmed.ncbi.nlm.nih.gov/9351408/)). **Immunocompromise** (e.g., rituximab therapy) predisposes to *B. miyamotoi* meningoencephalitis ([PMID: 34412488](https://pubmed.ncbi.nlm.nih.gov/34412488/)).

**Genetic risk / protective factors.** *Human* — Not established; no validated human susceptibility or protective variants. *Model organism* — susceptibility to *B. hermsii* is genetically controlled across inbred mouse strains via innate-immune genes ([PMID: 19995898](https://pubmed.ncbi.nlm.nih.gov/19995898/)). Natural reservoir *Peromyscus* mice carry resistance/tolerance traits that limit pathology ([PMID: 27381345](https://pubmed.ncbi.nlm.nih.gov/27381345/)).

**Gene–environment interaction.** Not applicable in the human-heritable sense. The operative interaction is **pathogen antigenic-variation genetics × host adaptive immunity**: host antibody pressure selects for Vmp switch variants, producing the relapse cycle.

### 3. Phenotypes

The cardinal phenotype is **relapsing fever** — recurring high-fever episodes (present in ~100% of confirmed cases), each lasting ~3 days with afebrile intervals of ~5–7 days, driven by antigenic variation. Additional phenotypes and their characteristics:

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Recurring fever | symptom | ~100% (defining) | HP:0001954 (recurrent fever) |
| Chills/rigors | symptom | ~67% | HP:0025143 |
| Headache | symptom | common | HP:0002315 |
| Myalgia/arthralgia | symptom | 55% arthralgia (B. miyamotoi) | HP:0003326 / HP:0002829 |
| Thrombocytopenia | lab abnormality | most suggestive lab finding | HP:0001873 |
| Anemia | lab abnormality | 74.7% (severe cohort) | HP:0001903 |
| Hepatosplenomegaly | clinical sign | common | HP:0001433 |
| Altered mental status / neurologic | clinical sign | 46.2% severe cohort; meningoencephalitis in immunocompromised | HP:0011446 |
| ARDS / respiratory distress | complication | 54.6–69.7% (severe cohort) | HP:0033677 |
| Shock | complication | 60.5% (severe cohort) | HP:0031273 |
| Petechial rash / hemorrhage | physical manifestation | common in LBRF | HP:0000979 |

**Onset:** acute, 2–18 days after exposure. **Severity:** variable — mild self-limiting in *B. miyamotoi* to severe/fatal in untreated LBRF. **Progression:** episodic/relapsing-remitting by definition. **Quality of life:** acute and self-limited if treated; severe morbidity (anemia, ARDS, perinatal loss) and death in untreated/severe cases.

### 4. Genetic/Molecular Information

**Not applicable to human heritable genetics.** No human causal genes, pathogenic variants, modifier genes, or chromosomal abnormalities are associated with relapsing fever.

**Pathogen molecular genetics (the operative "genetics"):**
- **Variable major protein (*vmp*) gene families** — *vlp* (variable large protein) and *vsp* (variable small protein) — provide ~60 silent archival genes on **linear plasmids** ([PMID: 12008924](https://pubmed.ncbi.nlm.nih.gov/12008924/); [PMID: 11083837](https://pubmed.ncbi.nlm.nih.gov/11083837/)).
- **Single active expression site** with flanking **cis-acting UHS/DHS inverted repeats**; gene conversion into this site produces serotype switching. Deletion/mutation abolishes relapse ([PMID: 29250931](https://pubmed.ncbi.nlm.nih.gov/29250931/)).
- ***glpQ*** (glycerophosphoryldiester phosphodiesterase) — a conserved gene absent in Lyme *Borrelia*, used as a **serological diagnostic antigen** ([PMID: 32303256](https://pubmed.ncbi.nlm.nih.gov/32303256/)).
- **Vtp** (variable tick protein) — expressed in the tick vector, invariable at its locus but diverse between strains, and also elicits host antibody.

### 5. Environmental Information

**Infectious agents (taxonomy):** *Borrelia recurrentis*, *B. hermsii*, *B. duttonii*, *B. crocidurae*, *B. hispanica*, *B. persica*, *B. turicatae*, *B. miyamotoi* (genus *Borrelia*, family Borreliaceae/Spirochaetaceae). **Vectors:** body louse *Pediculus humanus humanus* (LBRF); soft ticks *Ornithodoros* spp. and hard ticks *Ixodes* spp. (TBRF). **Environmental/lifestyle factors:** poverty, crowding, homelessness, poor hygiene, cold climates promoting layered clothing (lice); exposure to rodent-infested dwellings, caves, and burrows (ticks). No chemical toxin or radiation etiology.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. Arthropod bite (Ornithodoros soft tick, Ixodes hard tick, or body louse)
   inoculates Borrelia spirochetes into skin/blood
        │  leads to
        ▼
2. Spirochetes bind host PLASMINOGEN and generate PLASMIN on their surface
   [F011], and use ADHESINS to attach to ECM/host cells
        │  results in
        ▼
3. Plasmin-mediated degradation of ECM and fibrin → tissue invasion and
   DISSEMINATION into bloodstream and organs (spleen, liver, CNS)
        │  leads to
        ▼
4. High-density BACTEREMIA → first febrile wave; spirochete-RBC interaction
        │  leads to
        ▼
5. Host mounts a rapid T-INDEPENDENT IgM response from B1b lymphocytes
   (requires TLR innate signaling for optimal antibody) [F010, F011]
        │  results in
        ▼
6. IgM-mediated clearance of the dominant serotype → afebrile interval;
   RBCs cleared by tissue-resident MACROPHAGES → ANEMIA/THROMBOCYTOPENIA [F003]
        │
        ├── branch A (relapse): rare Vmp SWITCH VARIANTS (gene conversion at the
        │   single expression site) [F001] escape IgM → new bacteremic wave →
        │   RETURN TO STEP 4 (repeats until variant repertoire/immunity exhausts)
        │
        └── branch B (treatment): ANTIBIOTIC (doxycycline/penicillin/ceftriaxone)
            → rapid spirochete lysis → release of bacterial products →
            TNF-α/IL-6/IL-8 surge → JARISCH-HERXHEIMER REACTION [F008]
        │  in severe/untreated disease leads to
        ▼
7. Systemic inflammation, myocarditis, ARDS, shock, hemorrhage, hepatic failure
   → DEATH (up to ~70% untreated LBRF) [F002]
```

**Upstream vs downstream.** The **initiating lesion** is vector inoculation (step 1); the **upstream driver of chronicity** is Vmp antigenic variation (step 6, branch A); **downstream effectors** are macrophage-mediated cytopenias, plasmin-driven dissemination, and — during therapy — the TNF-α cytokine cascade of the JHR. Note that branch A is *demonstrated* (loss-of-function mutants cannot relapse); the precise trigger of JHR immunopathology in branch B is *inferred* to be lysis-released bacterial products acting via innate receptors, with TNF-α causality established by the anti-TNF-α RCT.

**Molecular pathways / processes:** plasminogen activation and proteolysis (GO:0031639, GO:0006508); Toll-like receptor signaling (GO:0002224); humoral immune response / immunoglobulin production (GO:0006959, GO:0002377); cytokine-mediated inflammatory response (TNF-α, IL-6, IL-8; GO:0071356). **Protein dysfunction:** this is a pathogen-driven disease; the key protein events are surface antigen switching (Vmp) and host immune evasion, not host protein misfolding. **Immune involvement:** dominant — antigenic variation for evasion, B1b IgM for control, TNF-α for JHR immunopathology.

**Cell types (CL):** B-1b B cell (CL:0000821), macrophage (CL:0000235), erythrocyte (CL:0000232), platelet (CL:0000233). **GO biological processes:** antigenic variation / evasion of host immune response, inflammatory response (GO:0006954).

### 7. Anatomical Structures Affected

- **Primary organs:** blood/bloodstream (site of bacteremia; UBERON:0000178), spleen (UBERON:0002106), liver (UBERON:0002107).
- **Secondary involvement:** central nervous system / meninges (meningoencephalitis, especially *B. miyamotoi* in immunocompromised; UBERON:0001016, UBERON:0002360); lungs (ARDS; UBERON:0002048); heart (myocarditis; UBERON:0000948); placenta and fetus (UBERON:0001987) in pregnancy.
- **Body systems:** hematologic/immune, cardiovascular, respiratory, nervous, hepatobiliary, reproductive.
- **Tissue/cell level:** erythrocytes and platelets (cleared by macrophages), reticuloendothelial macrophages of spleen/liver, B1b lymphocytes.
- **Subcellular:** spirochete surface (outer membrane); no specific host organelle target.
- **Localization:** systemic/bilateral (disseminated bloodborne infection); no lateralization.

### 8. Temporal Development

- **Onset:** acute, incubation 2–18 days after exposure.
- **Course:** episodic / relapsing-remitting — the defining pattern. In LBRF typically 1 relapse (sometimes more); in TBRF multiple relapses (often 3–10) are characteristic. Each febrile episode lasts ~3 days; afebrile intervals ~5–7 days.
- **Duration:** self-limited over weeks if untreated survivors clear the infection; curative with antibiotics.
- **Critical period:** febrile attacks in pregnancy precipitate preterm delivery — a key window for intervention ([PMID: 9351408](https://pubmed.ncbi.nlm.nih.gov/9351408/)). Antibiotic timing determines JHR risk.

### 9. Inheritance and Population

**Inheritance:** Not applicable — infectious, not heritable.

**Epidemiology / geographic distribution:**
- **LBRF:** endemic focus in the Horn of Africa (Ethiopia, Somalia, Sudan, Eritrea); epidemic potential in war/famine/refugee settings; 26–45 imported European cases in 2015 ([PMID: 27340042](https://pubmed.ncbi.nlm.nih.gov/27340042/); [PMID: 27188655](https://pubmed.ncbi.nlm.nih.gov/27188655/)).
- **TBRF:** globally distributed enzootic foci (West Africa, Iberia, Middle East, western North America) with region-specific species/vectors ([PMID: 38321309](https://pubmed.ncbi.nlm.nih.gov/38321309/); [PMID: 26327444](https://pubmed.ncbi.nlm.nih.gov/26327444/)).
- **Burden:** relapsing fever *Borrelia* was the most common pathogen (15.5%) in non-malarial febrile illness in Senegal ([PMID: 38272885](https://pubmed.ncbi.nlm.nih.gov/38272885/)).
- **B. miyamotoi (US):** 300 surveillance cases (2013–2019), median age 52, 52% male, 70% June–September ([PMID: 37610298](https://pubmed.ncbi.nlm.nih.gov/37610298/)).

**Demographics:** all ages affected; severe outcomes in pregnant women, the malnourished, and immunocompromised. Sex ratio roughly balanced (52% male in US *B. miyamotoi* series).

### 10. Diagnostics

- **Gold standard:** direct microscopy — spirochetes visualized on **Giemsa/Wright-stained thick and thin blood films** drawn during febrile peaks ([PMID: 27188655](https://pubmed.ncbi.nlm.nih.gov/27188655/)); thrombocytopenia is the most suggestive laboratory finding.
- **Molecular:** **16S rRNA gene PCR/sequencing** for species identification ([PMID: 27188655](https://pubmed.ncbi.nlm.nih.gov/27188655/)); qPCR for *B. miyamotoi* ([PMID: 38686844](https://pubmed.ncbi.nlm.nih.gov/38686844/)); metagenomic sequencing ([PMID: 38272885](https://pubmed.ncbi.nlm.nih.gov/38272885/)).
- **Serology:** **GlpQ (glycerophosphoryldiester-phosphodiesterase) serology** distinguishes RF from Lyme *Borrelia* ([PMID: 32303256](https://pubmed.ncbi.nlm.nih.gov/32303256/)).
- **CSF:** Gram stain + sequencing for meningoencephalitis ([PMID: 38916722](https://pubmed.ncbi.nlm.nih.gov/38916722/)); pleocytosis in meningeal involvement ([PMID: 26938933](https://pubmed.ncbi.nlm.nih.gov/26938933/)).
- **Differential diagnosis:** malaria (co-infection common), typhoid, dengue, leptospirosis, spotted-fever rickettsiosis.
- **Genetic testing / newborn screening / omics diagnostics:** Not applicable (infectious disease).

### 11. Outcome/Prognosis

- **Mortality:** untreated LBRF up to ~70%; severe hospitalized cohort 45.4% in-hospital mortality ([PMID: 41418926](https://pubmed.ncbi.nlm.nih.gov/41418926/)); with antibiotic treatment, case-fatality falls to <5%. No deaths in the milder US *B. miyamotoi* series ([PMID: 37610298](https://pubmed.ncbi.nlm.nih.gov/37610298/)).
- **Complications:** anemia, ARDS, shock, JHR, myocarditis, hemorrhage, hepatic failure, meningoencephalitis, and — in pregnancy — abortion/preterm birth with perinatal mortality of 436/1000 ([PMID: 9351408](https://pubmed.ncbi.nlm.nih.gov/9351408/)).
- **Prognostic factors:** promptness of antibiotic therapy, pregnancy, high spirochetemia density, immunocompromise, malnutrition, and co-infection.
- **Recovery:** complete recovery is expected with timely treatment; the disease is self-limited/curable rather than chronic.

### 12. Treatment

- **First-line pharmacotherapy:** **tetracyclines — doxycycline** (NCIT:C299); **penicillin** (NCIT:C716); **ceftriaxone** (NCIT:C1638) for severe/CNS disease. Erythromycin/macrolides are alternatives (e.g., in children, pregnancy). Patients recovered after ceftriaxone and/or doxycycline ([PMID: 27188655](https://pubmed.ncbi.nlm.nih.gov/27188655/)); doxycycline + ceftriaxone for meningeal involvement ([PMID: 26938933](https://pubmed.ncbi.nlm.nih.gov/26938933/)).
- **Jarisch-Herxheimer management:** anticipate JHR within 24 h of first dose; supportive care (fluids, antipyretics, hemodynamic monitoring). **Pre-treatment anti-TNF-α antibody reduces JHR severity** in trials ([PMID: 8663853](https://pubmed.ncbi.nlm.nih.gov/8663853/)) — a mechanistic proof of concept, not yet standard care.
- **Supportive care:** transfusion for anemia, oxygen/ventilation for ARDS, vasopressors for shock.
- **Advanced/targeted/gene/cell/RNA therapies; pharmacogenomics:** Not applicable.

### 13. Prevention

- **Primary prevention:** LBRF — **delousing**, sterilizing/laundering clothing, pediculicides, improved personal hygiene; TBRF — avoidance of rodent-infested/tick-infested dwellings, rodent-proofing, acaricides, permethrin-treated clothing.
- **Secondary prevention:** active surveillance of tick bites and early diagnosis in endemic settings.
- **Post-exposure prophylaxis:** **doxycycline PEP** effective for TBRF; cohort-based PEP prevented all subsequent cases in an Israeli military study ([PMID: 24107216](https://pubmed.ncbi.nlm.nih.gov/24107216/)).
- **Immunization:** **no vaccine exists** (antigenic variation is a fundamental barrier to vaccine development).
- **Public health:** outbreak control through delousing campaigns, sanitation, health education, and vector control.

### 14. Other Species / Natural Disease

- **Taxonomy of hosts:** *Peromyscus leucopus* / *P. maniculatus* (NCBI txid10041/10042), *Gerbillus* spp. (txid10045), *Mus musculus* (txid10090), *Odocoileus hemionus* (mule deer). Reservoir competence with minimal pathology in *Peromyscus* ([PMID: 27381345](https://pubmed.ncbi.nlm.nih.gov/27381345/)).
- **Zoonotic potential:** TBRF is a **true zoonosis** maintained in *Ornithodoros*/rodent enzootic cycles ([PMID: 38321309](https://pubmed.ncbi.nlm.nih.gov/38321309/)); LBRF (*B. recurrentis*) is essentially an **anthroponosis** (human–louse–human cycle).
- **Comparative biology:** RF spirochetes infect wild rodents, deer (7.7% Nevada mule deer; [PMID: 21995265](https://pubmed.ncbi.nlm.nih.gov/21995265/)), and — for related species such as *B. anserina* and *B. theileri* — birds and cattle. Reservoirs tolerate infection via resistance + tolerance mechanisms ([PMID: 27381345](https://pubmed.ncbi.nlm.nih.gov/27381345/)).

### 15. Model Organisms

- **Principal model:** **inbred laboratory mice** (*Mus musculus*), both immunocompetent and immunodeficient (SCID, Rag−/−, TCR−/−, IL-7−/−, *xid*), which recapitulate relapsing bacteremia, antigenic variation, thrombocytopenia, and anemia and have been used to dissect the B1b/IgM clearance mechanism and genetic susceptibility ([PMID: 12646649](https://pubmed.ncbi.nlm.nih.gov/12646649/); [PMID: 19995898](https://pubmed.ncbi.nlm.nih.gov/19995898/)).
- **Genetic models:** *Borrelia* mutants — Vmp-null, expression-site deletions, UHS/DHS repeat mutants — used to prove antigenic-variation necessity ([PMID: 29250931](https://pubmed.ncbi.nlm.nih.gov/29250931/); [PMID: 24699793](https://pubmed.ncbi.nlm.nih.gov/24699793/)).
- **Other models:** guinea pigs for tick-transmission competence ([PMID: 38321309](https://pubmed.ncbi.nlm.nih.gov/38321309/)); *Peromyscus* reservoir studies for resistance/tolerance biology ([PMID: 27381345](https://pubmed.ncbi.nlm.nih.gov/27381345/)).
- **Recapitulation/limitations:** mouse models faithfully reproduce the relapse cycle and immune control but do not fully capture human severe complications (ARDS, JHR severity, pregnancy loss).

---

## Mechanistic Model / Interpretation

The unifying concept of relapsing fever is an **evolutionary arms race between pathogen antigenic variation and host antibody immunity**, played out in cycles measured in days:

```
        Vmp switch (gene conversion)            IgM from B1b cells
   ┌──────────────────────────────────┐   ┌──────────────────────────┐
   │  silent vmp archive (~60 genes)  │   │  T-independent humoral    │
   │  on linear plasmids              │   │  response (TLR-assisted)  │
   └──────────────┬───────────────────┘   └────────────┬─────────────┘
                  │ places 1 gene at                    │ clears dominant
                  │ single expression site              │ serotype
                  ▼                                      ▼
        NEW SEROTYPE → bacteremic wave ──────► FEVER ──► clearance ──► afebrile
                  ▲                                                        │
                  └──────────── rare escape variant ◄──────────────────────┘
                                (drives the next RELAPSE)
```

Every febrile peak corresponds to a high-density bacteremic wave of a single dominant Vmp serotype; every trough corresponds to IgM-mediated clearance of that serotype. Because gene conversion continually generates rare escape variants, the process repeats until the variant repertoire and cumulative immunity exhaust it. Superimposed on this cycle are (i) **plasmin/adhesin-mediated dissemination** enabling organ invasion, (ii) **macrophage-mediated erythrocyte/platelet clearance** producing the characteristic cytopenias, and (iii) the **TNF-α/IL-6/IL-8 Jarisch-Herxheimer cascade** unleashed when antibiotics lyse the spirochetes. This model explains the clinical hallmarks (sawtooth fever, anemia, thrombocytopenia, treatment-associated crises) as direct consequences of a single organizing principle — antigenic variation under antibody selection.

---

## Evidence Base

| Finding | Key PMIDs | Contribution |
|---|---|---|
| Antigenic variation mechanism | [29250931](https://pubmed.ncbi.nlm.nih.gov/29250931/), [24699793](https://pubmed.ncbi.nlm.nih.gov/24699793/), [12008924](https://pubmed.ncbi.nlm.nih.gov/12008924/), [11083837](https://pubmed.ncbi.nlm.nih.gov/11083837/) | Define gene conversion, expression site, cis-elements; loss-of-function proves relapse dependence |
| Clinical burden/mortality | [41418926](https://pubmed.ncbi.nlm.nih.gov/41418926/), [40624823](https://pubmed.ncbi.nlm.nih.gov/40624823/) | Quantify complications, 45.4% mortality, define JHR |
| Anemia/macrophage clearance | [19995898](https://pubmed.ncbi.nlm.nih.gov/19995898/) | FISH evidence of macrophage RBC clearance; innate + adaptive control |
| *B. miyamotoi* emergence | [34412488](https://pubmed.ncbi.nlm.nih.gov/34412488/), [38916722](https://pubmed.ncbi.nlm.nih.gov/38916722/), [32303256](https://pubmed.ncbi.nlm.nih.gov/32303256/) | Hard-tick RF, CNS disease, PCR/GlpQ diagnosis |
| Pregnancy outcomes | [9351408](https://pubmed.ncbi.nlm.nih.gov/9351408/) | Perinatal mortality 436/1000; higher spirochetemia |
| LBRF re-emergence | [27340042](https://pubmed.ncbi.nlm.nih.gov/27340042/), [27188655](https://pubmed.ncbi.nlm.nih.gov/27188655/), [26938933](https://pubmed.ncbi.nlm.nih.gov/26938933/) | 2015 European migrant cases, diagnosis, treatment |
| Enzootic cycle | [38321309](https://pubmed.ncbi.nlm.nih.gov/38321309/), [26327444](https://pubmed.ncbi.nlm.nih.gov/26327444/), [23808979](https://pubmed.ncbi.nlm.nih.gov/23808979/), [21995265](https://pubmed.ncbi.nlm.nih.gov/21995265/), [33741637](https://pubmed.ncbi.nlm.nih.gov/33741637/) | Region-specific *Ornithodoros*/rodent cycles |
| JHR cytokine mechanism | [8663853](https://pubmed.ncbi.nlm.nih.gov/8663853/), [1569394](https://pubmed.ncbi.nlm.nih.gov/1569394/) | RCT anti-TNF-α suppresses JHR; TNF/IL-6/IL-8 surge |
| Epidemiology | [37610298](https://pubmed.ncbi.nlm.nih.gov/37610298/), [38686844](https://pubmed.ncbi.nlm.nih.gov/38686844/), [38272885](https://pubmed.ncbi.nlm.nih.gov/38272885/) | US surveillance; West African burden |
| B1b/IgM clearance | [12646649](https://pubmed.ncbi.nlm.nih.gov/12646649/) | IgM essential; B1b expansion resolves bacteremia |
| Dissemination/TLR | [25914944](https://pubmed.ncbi.nlm.nih.gov/25914944/), [21557056](https://pubmed.ncbi.nlm.nih.gov/21557056/), [22202086](https://pubmed.ncbi.nlm.nih.gov/22202086/) | Plasmin/adhesins; TLR required for antibody |
| Reservoirs/models | [27381345](https://pubmed.ncbi.nlm.nih.gov/27381345/) | *Peromyscus* resistance + tolerance |
| Prevention/PEP | [24107216](https://pubmed.ncbi.nlm.nih.gov/24107216/) | Doxycycline PEP; no vaccine |

**Evidence source types:** human clinical (case series, cohorts, RCT of anti-TNF-α, surveillance); model organism (mouse genetics, *Borrelia* mutants, *Peromyscus*, guinea pigs); molecular/in vitro (plasmin binding, gene-conversion genetics).

---

## Limitations and Knowledge Gaps

1. **No primary dataset was analyzed** — this report synthesizes published literature; no de novo statistical testing of raw data was performed. Effect sizes are those reported by source studies.
2. **Severe-cohort mortality (45.4%) is not generalizable** — it derives from a single resource-limited hospital cohort of the sickest, blood-film-positive patients and overestimates population case-fatality where treatment is available.
3. **Species heterogeneity** — RF spans many *Borrelia* species with differing virulence (e.g., mild *B. miyamotoi* vs lethal *B. recurrentis*); pooling clinical features across species obscures species-specific behavior.
4. **Human host genetics unexplored** — no GWAS or candidate-gene studies define human susceptibility/protective loci; all host genetic evidence is murine.
5. **Anti-TNF-α for JHR** remains a proof-of-concept from one RCT and is not standard practice; optimal clinical JHR mitigation is unresolved.
6. **Global burden is underestimated** — RF is frequently misdiagnosed as malaria; true incidence/prevalence figures are lacking for most endemic regions.
7. **Vaccine development** is fundamentally hampered by antigenic variation; no candidate has advanced.

---

## Proposed Follow-up Experiments / Actions

1. **Species-stratified clinical meta-analysis** — pool case series by *Borrelia* species to derive species-specific complication rates, JHR risk, and case-fatality with confidence intervals.
2. **Human immunogenetic study** — investigate whether human variants in innate-immunity genes (TLRs, complement) or hemoglobinopathies modulate RF severity, mirroring the murine susceptibility findings ([PMID: 19995898](https://pubmed.ncbi.nlm.nih.gov/19995898/)).
3. **Prospective anti-cytokine JHR trial** — evaluate targeted TNF-α (or IL-6) blockade at antibiotic initiation in LBRF, building on [PMID: 8663853](https://pubmed.ncbi.nlm.nih.gov/8663853/), with hemodynamic and cytokine endpoints.
4. **Conserved-antigen vaccine screen** — target invariant surface molecules (e.g., GlpQ, Vtp-conserved regions, factor-H-binding proteins) to circumvent Vmp antigenic variation.
5. **Enhanced surveillance & rapid diagnostics** — deploy multiplex PCR/metagenomic panels and GlpQ point-of-care serology in malaria-endemic Africa to correctly attribute non-malarial febrile illness ([PMID: 38272885](https://pubmed.ncbi.nlm.nih.gov/38272885/)).
6. **Pregnancy-focused management protocol** — study fetal monitoring and prophylactic strategies to reduce attack-triggered preterm delivery ([PMID: 9351408](https://pubmed.ncbi.nlm.nih.gov/9351408/)).
7. **One Health reservoir mapping** — characterize *Ornithodoros*/rodent enzootic foci and *B. miyamotoi* hard-tick range expansion to predict emergence risk.

---

## Conclusion

Relapsing fever is an infectious, non-heritable, arthropod-borne spirochetosis whose defining relapse phenomenon is produced by multiphasic **Vmp antigenic variation via gene conversion**, which repeatedly evades a **T-independent, B1b-cell IgM** response that clears each bacteremic wave. It is diagnosed by blood-smear microscopy (with PCR and GlpQ serology) and cured with doxycycline, penicillin, or ceftriaxone — treatment that frequently provokes a **TNF-α-driven Jarisch-Herxheimer reaction**. Untreated louse-borne disease can be highly lethal (up to ~70%). All human-heritable genetics sections are Not Applicable; the operative genetics are those of the pathogen's antigenic-variation loci and of murine host-susceptibility genes.


## Artifacts

- [OpenScientist final report](Relapsing_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Relapsing_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 30 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001903` (2 mentions) - the report calls it "74.7% (severe cohort)"; HP calls it **Anemia**
- `HP:0001873` (2 mentions) - the report calls it "most suggestive lab finding"; HP calls it **Thrombocytopenia**
- `HP:0033677` (2 mentions) - the report calls it "54.6–69.7% (severe cohort)"; HP calls it **Acute respiratory distress syndrome**
- `HP:0031273` (2 mentions) - the report calls it "60.5% (severe cohort)"; HP calls it **Shock**
- `HP:0002315` (1 mention) - the report calls it "common"; HP calls it **Headache**
- `HP:0001433` (1 mention) - the report calls it "common"; HP calls it **Hepatosplenomegaly**
- `HP:0011446` (1 mention) - the report calls it "46.2% severe cohort; meningoencephalitis in immunocompromised"; HP calls it **Abnormality of mental function**
- `HP:0000979` (1 mention) - the report calls it "common in LBRF"; HP calls it **Purpura**
- `NCIT:C299` (1 mention) - the report calls it "tetracyclines — doxycycline", "First-line pharmacotherapy:** **tetracyclines — doxycycline"; NCIT calls it **Beclomethasone Dipropionate**
- `NCIT:C716` (1 mention) - the report calls it "penicillin"; NCIT calls it **Omeprazole**
- `NCIT:C1638` (1 mention) - the report calls it "ceftriaxone"; NCIT calls it **Carbon C-14**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C299` - called "tetracyclines — doxycycline", "First-line pharmacotherapy:** **tetracyclines — doxycycline"