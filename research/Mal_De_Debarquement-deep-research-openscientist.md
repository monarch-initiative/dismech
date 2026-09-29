---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T15:09:30.250295'
end_time: '2026-08-29T15:22:48.402018'
duration_seconds: 798.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mal De Debarquement
  mondo_id: ''
  category: Acquired
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
citation_count: 21
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 13
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0060013
    reported_labels:
    - GO / biological process:** vestibulo-ocular reflex
    ontology_label: righting reflex
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mal_De_Debarquement-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mal_De_Debarquement-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mal De Debarquement
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Mal De Debarquement** covering all of the
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

# Mal de Débarquement Syndrome (MdDS): A Comprehensive Disease Characteristics Report

**Disease Name:** Mal de Débarquement Syndrome (MdDS)
**Category:** Acquired
**MONDO:** "mal de debarquement" (acquired disease term exists in Mondo); **MeSH:** "Mal de Debarquement" (introduced 2018); **ICD-11:** foundation term under vestibular/balance disorders; **ICD-10:** no dedicated code (coded under H81 / R42 "Dizziness and giddiness"); **OMIM:** none (non-Mendelian); **Orphanet:** listed among rare vestibular disorders.

---

## Summary

Mal de Débarquement Syndrome (MdDS) is a rare, **acquired chronic central/functional vestibular disorder** defined by a persistent, non-spinning oscillatory perception of self-motion — described by patients as *rocking, bobbing, or swaying* — that is present continuously or for most of the day. The hallmark that distinguishes it from other chronic dizziness syndromes is its temporal relationship to passive motion: symptoms begin **within 48 hours of ceasing prolonged passive motion** (classically a sea cruise, but also air and road travel) and are **paradoxically relieved by re-exposure to passive motion** (e.g., driving). A non-motion-triggered ("spontaneous") variant also exists, overlapping clinically with persistent postural-perceptual dizziness (PPPD). These features are codified in the 2020 Bárány Society Classification Committee consensus criteria ([PMID: 32986636](https://pubmed.ncbi.nlm.nih.gov/32986636/)).

Mechanistically, converging evidence supports a model of **maladaptive neuroplasticity** rather than any structural inner-ear lesion or gene defect. The leading physiological account holds that MdDS results from maladaptation of the **vestibulo-ocular reflex (VOR)** and the central **velocity-storage mechanism** to roll of the head during rotation — an inappropriate conditioning of a cross-axis coupling within a dynamical velocity-storage system ([PMID: 25076935](https://pubmed.ncbi.nlm.nih.gov/25076935/); [PMID: 41122084](https://pubmed.ncbi.nlm.nih.gov/41122084/)). Neuroimaging shows a self-sustaining cortico-limbic network signature: **hypermetabolism of the left entorhinal cortex and amygdala** with altered functional connectivity to posterior sensory-processing and frontal/temporal regions ([PMID: 23209584](https://pubmed.ncbi.nlm.nih.gov/23209584/); [PMID: 33746890](https://pubmed.ncbi.nlm.nih.gov/33746890/)), and high-density EEG frames the condition as a brain state of **entrainment to oscillating motion** ([PMID: 30099627](https://pubmed.ncbi.nlm.nih.gov/30099627/)).

MdDS predominates in **midlife women** (~3:1 to >4:1 female), is **highly comorbid with migraine**, is diagnosed **clinically by exclusion** (normal vestibular test battery and structural MRI), and is not life-threatening — but it is frequently chronic and disabling. The most disease-specific therapy is **VOR readaptation / optokinetic stimulation** (~70% substantial improvement in the original series), supplemented by neuromodulation (rTMS/tDCS over the dorsolateral prefrontal cortex) and migraine-prophylaxis pharmacotherapy. There is no FDA-approved drug, no causal gene, no animal disease model, and no established primary prevention. This report synthesizes 16 confirmed findings across 30 reviewed papers into a complete disease-characteristics entry.

---

## Key Findings

### 1. Definition and Diagnostic Criteria (F001)

MdDS is a chronic vestibular disorder of persistent oscillatory self-motion. The Bárány Society Classification Committee consensus ([PMID: 32986636](https://pubmed.ncbi.nlm.nih.gov/32986636/)) provides the authoritative case definition. The criteria specify: *"1] Non-spinning vertigo characterized by an oscillatory perception ('rocking,' 'bobbing,' or 'swaying') present continuously or for most of the day; 2] Onset occurs within 48 hours after the end of exposure to passive motion, 3] Symptoms temporarily reduce with exposure to passive motion (e.g. driving), and 4] Symptoms persist for >48 hours."*

Temporal qualifiers structure the diagnosis: **"in evolution"** (<1 month of observation), **"transient"** (resolves within ≤1 month), and **"persistent"** (>1 month). A **non-motion-triggered variant** is recognized, which follows another vestibular disorder, medical illness, psychological stress, or metabolic disturbance and overlaps clinically with PPPD. MdDS is classified within the International Classification of Vestibular Disorders (ICVD) as a chronic functional/central vestibular disorder.

### 2. Pathophysiology — VOR / Velocity-Storage Maladaptation (F002)

The mechanistic cornerstone is the proposal by Dai, Cohen and colleagues that MdDS arises from **maladaptation of the VOR to roll of the head during rotation**, derived from both monkey and human data: *"Results in monkeys and humans suggested that MdDS was caused by maladaptation of the vestibulo-ocular reflex (VOR) to roll of the head during rotation"* ([PMID: 25076935](https://pubmed.ncbi.nlm.nih.gov/25076935/)). In a cohort of 24 subjects, physical findings included **body oscillation at ~0.2 Hz**, **oscillating vertical nystagmus on side-to-side head roll in darkness**, and unilateral rotation on the Fukuda stepping test.

More recent computational modelling formalizes the central **velocity-storage mechanism** as a 3×3 dynamical system: *"A central vestibular neural mechanism known as velocity storage may be inappropriately conditioned in mal de débarquement syndrome (MdDS)"* ([PMID: 41122084](https://pubmed.ncbi.nlm.nih.gov/41122084/)). In this framework, maladapted off-diagonal (cross-axis coupling) elements — a misalignment between the yaw eigenvector and the head-vertical/gravity axis — produce the persistent "pull" / rocking sensation. This is elaborated as *"improperly sustained neuroplasticity in the velocity storage mechanism of the central vestibular system"* ([PMID: 42440785](https://pubmed.ncbi.nlm.nih.gov/42440785/)).

### 3. Neuroimaging — Limbic Hypermetabolism and Altered Connectivity (F003)

Cha et al. studied 20 MdDS subjects (median duration 17.5 months) versus 20 controls using FDG-PET and resting-state fMRI, reporting: *"MdDS subjects showed increased metabolism in the left entorhinal cortex and amygdala (z>3.3)"* ([PMID: 23209584](https://pubmed.ncbi.nlm.nih.gov/23209584/)). The same study found relative hypometabolism in the left superior medial/middle frontal gyri, right amygdala, right insula, and temporal gyri, alongside increased connectivity between the entorhinal/amygdala cluster and posterior visual/vestibular processing areas.

A dedicated review synthesizes these imaging findings ([PMID: 33746890](https://pubmed.ncbi.nlm.nih.gov/33746890/)): *"a limbic focus in the left entorhinal cortex and amygdala may be important in the pathology of MdDS, as these structures are hypermetabolic in MdDS and exhibit increased functional connectivity to posterior sensory processing areas and reduced connectivity to the frontal and temporal cortices."* Voxel-based morphometry additionally shows **decreasing anterior cingulate volume** and **increasing inferior frontal gyri / anterior insula volume** with longer illness duration.

### 4. Mechanism as an Oscillatory-Entrainment Brain State (F014)

High-density resting-state EEG frames MdDS as *"a motion perceptual disorder induced by entrainment to oscillating motion"* ([PMID: 30099627](https://pubmed.ncbi.nlm.nih.gov/30099627/)). In 20 women (mean age 52.9 ± 12.6 y; illness duration 35.2 ± 24.2 mo), rTMS-induced symptom improvement correlated with **increased long-range low-alpha (8–10 Hz) inter-regional phase coherence** and decreased coherence in other bands, mostly between frontal and parietal regions. High baseline high-alpha/beta coherence predicted treatment response. This electrophysiological signature complements the FDG-PET/fMRI evidence and positions the disorder as a network-level dysrhythmia rather than a focal lesion.

### 5. Treatment — VOR Readaptation and Optokinetic Stimulation (F004)

The most disease-specific therapy directly targets the proposed velocity-storage maladaptation. Dai et al. treated 24 MdDS subjects by rolling the head side-to-side while viewing a rotating full-field visual stimulus: *"Seventeen of the 24 subjects had a complete or substantial recovery on average for approximately 1 year"* — approximately **70% response** ([PMID: 25076935](https://pubmed.ncbi.nlm.nih.gov/25076935/)); 6 relapsed and 1 was a non-responder. The authors summarize that *"readaptation of the VOR has led to a cure or substantial improvement in 70% of the subjects with MdDS."*

The approach has been extended to sham-controlled optokinetic stimulation trials ([PMID: 30410464](https://pubmed.ncbi.nlm.nih.gov/30410464/)) and translated to audiology-vestibular clinic settings. A case report of a 48-year-old woman treated with the **"Roll Readaptation"** technique — full-field omnidirectional optokinetic stimulus during rhythmic head roll, three short sessions — produced significant symptom reduction and return to full-time work after nearly 3 months off ([PMID: 36323329](https://pubmed.ncbi.nlm.nih.gov/36323329/)).

### 6. Neuromodulation — rTMS, tDCS, iTBS over DLPFC (F010)

Controlled-trial evidence supports neuromodulation as an adjunctive therapy targeting the cortico-limbic network node:

| Study | Design | N | Intervention | Key result |
|---|---|---|---|---|
| Cha et al. ([PMID: 27176615](https://pubmed.ncbi.nlm.nih.gov/27176615/)) | Double-blind sham-controlled crossover | 8 women | 5 days 10 Hz rTMS, left DLPFC | Improved DHI at post-weeks 1,3,4 (p<0.05); improved HADS anxiety/depression; no change with sham |
| Cha et al. ([PMID: 27117283](https://pubmed.ncbi.nlm.nih.gov/27117283/)) | Single-blind sham RCT, home tDCS after rTMS | 23 | tDCS anode L / cathode R DLPFC | Improved MdDS Balance Rating Scale and anxiety by week 4; safe (0 skin burns / 556 sessions) |
| Browne et al. ([PMID: 38345630](https://pubmed.ncbi.nlm.nih.gov/38345630/)) | RCT, iTBS + VOR rehab vs sham | 20 | iTBS adjunct to VOR rehabilitation | Both groups improved; **no between-group difference** — iTBS added no benefit over VOR rehab alone |
| Scoping review ([PMID: 40228811](https://pubmed.ncbi.nlm.nih.gov/40228811/)) | Review, 7 studies | — | TMS for chronic vestibular disorders | Statistically significant DHI improvement in 3/7; postural control improved in 7/7 |

Cha et al. concluded: *"Our study provides evidence that the dizziness, mood and anxiety symptoms of MdDS can be improved with 10 Hz rTMS over left DLPFC beyond the treatment period in selected individuals"* ([PMID: 27176615](https://pubmed.ncbi.nlm.nih.gov/27176615/)). However, the scoping review found: *"Statistically significant improvements were noted on the Dizziness Handicap Inventory (3/7 studies) but clinically significant improvements were not observed"* ([PMID: 40228811](https://pubmed.ncbi.nlm.nih.gov/40228811/)). rTMS response also has a connectivity correlate: improvement correlated with reduced connectivity between left entorhinal cortex and posterior default-mode nodes, and higher baseline DLPFC–entorhinal connectivity predicted response ([PMID: 28967282](https://pubmed.ncbi.nlm.nih.gov/28967282/)).

### 7. Treatment — Vestibular-Migraine Prophylaxis (F009)

Given the high migraine comorbidity, migraine-prophylactic pharmacotherapy benefits many patients. Ghavami et al. treated 15 MdDS patients (73% female, mean age 50 ± 13 y) with an institutional vestibular-migraine protocol: *"Eleven patients (73%) responded well to management with a vestibular migraine protocol, which included lifestyle changes, as well as pharmacotherapy with verapamil, nortriptyline, topiramate, or a combination thereof"* ([PMID: 27730651](https://pubmed.ncbi.nlm.nih.gov/27730651/)). Nearly all had a personal or family migraine history, and the response rate exceeded that of a retrospective vestibular-rehabilitation control group. Chronic-dizziness management additionally emphasizes serotonergic antidepressants that *"modulate sensory gating and reduce anxiety,"* vestibular rehabilitation, CBT, and trigger avoidance ([PMID: 34351113](https://pubmed.ncbi.nlm.nih.gov/34351113/)). Benzodiazepines (e.g., clonazepam) are used symptomatically. **There is no FDA-approved drug specifically for MdDS.**

### 8. Epidemiology and Demographics (F005, F015)

MdDS shows a **strong female predominance** (21/24 female in the Dai cohort; 73% female in Ghavami's series) with typical **adult onset in the 4th–6th decades** (mean ages across cohorts: 44.5 ± 7.0, 50 ± 13, 52.9 ± 12.6 years). A sex-hormone review notes: *"In females, gonadal hormones and sex-specific synaptic plasticity may play a significant role in the underlying pathophysiology of peripheral and central vestibular disorders"* ([PMID: 34864753](https://pubmed.ncbi.nlm.nih.gov/34864753/)), consistent with frequent perimenopausal onset.

**Migraine comorbidity is high:** in a study of rocking dizziness, *"both groups had a comparable prevalence of migraine headache (41%: MT; 46%: non-MT)"* ([PMID: 23674832](https://pubmed.ncbi.nlm.nih.gov/23674832/)). True population prevalence and incidence are **unknown** — MdDS is considered rare and under-recognized, with no registry-based figures. Information derives from disease-level case series and specialty-clinic cohorts rather than population EHR data. No specific ethnic or geographic clustering is established.

**Synonyms/nomenclature:** Mal de débarquement syndrome; "sickness of disembarkment / disembarkment syndrome"; "debarkment syndrome"; MdDS; historically "landsickness."

### 9. Diagnosis by Exclusion (F006)

MdDS is diagnosed clinically per Bárány criteria; **no confirmatory laboratory test or biomarker exists.** Standard vestibular function testing (VNG/ENG, caloric, rotary chair, VEMP), audiometry, and structural brain MRI are characteristically normal: *"We found normal inner-ear function, non-related abnormalities and normal brain imaging"* ([PMID: 32364688](https://pubmed.ncbi.nlm.nih.gov/32364688/)). FDG-PET limbic hypermetabolism and resting-state fMRI/EEG connectivity changes are **research-only** biomarkers. The one described diagnostic physical sign is oscillating vertical nystagmus on head roll in darkness ([PMID: 25076935](https://pubmed.ncbi.nlm.nih.gov/25076935/)).

Key differential diagnoses include *"persistent postural perceptual dizziness, mal de débarquement syndrome, motion sickness and visually induced motion sickness, bilateral vestibulopathy"* ([PMID: 34351113](https://pubmed.ncbi.nlm.nih.gov/34351113/)), plus vestibular migraine, BPPV, and Ménière's disease. The **distinguishing feature is transient relief with re-exposure to passive motion.**

### 10. Natural History and Prognosis (F007)

MdDS symptoms characteristically persist for months to years (median 17.5 months in the imaging cohort; 19.1 ± 33 months in the treatment cohort). Ghavami et al. note a key prognostic threshold: *"symptoms that persist beyond 6 months have been described as unlikely to remit"* ([PMID: 27730651](https://pubmed.ncbi.nlm.nih.gov/27730651/)). The course is **fluctuating/relapsing**, exacerbated by psychological stress, fatigue, hormonal changes, and busy visual environments; Cha describes these as *"chronic syndromes with fluctuations that are both innate and driven by environmental stressors"* ([PMID: 34351113](https://pubmed.ncbi.nlm.nih.gov/34351113/)). **MdDS is not associated with increased mortality;** morbidity arises from disability, occupational impairment, anxiety/depression, and reduced quality of life ([PMID: 37987715](https://pubmed.ncbi.nlm.nih.gov/37987715/); [PMID: 40296474](https://pubmed.ncbi.nlm.nih.gov/40296474/)).

### 11. Etiology and Environmental Triggers (F011)

The defining environmental cause is **prolonged exposure to passive oscillatory motion** — classically sea travel, also air and road travel — with onset within 48 hours of disembarking: *"Onset occurs within 48 hours after the end of exposure to passive motion"* ([PMID: 32986636](https://pubmed.ncbi.nlm.nih.gov/32986636/)). Occupational exposure is documented in pilots, where *"As flight time and age increased, the severity of the symptoms of MdDS increased for all subfactors"* ([PMID: 40296474](https://pubmed.ncbi.nlm.nih.gov/40296474/)), and in military personnel exposed to transport motion ([PMID: 37987715](https://pubmed.ncbi.nlm.nih.gov/37987715/)). Symptom-exacerbating factors include busy visual environments, fatigue, sleep deprivation, psychological stress, and hormonal fluctuations. **No toxin, radiation, pollutant, drug, or infectious agent** is implicated. Paradoxically, re-exposure to passive motion transiently relieves symptoms.

### 12. Phenotype Spectrum (F012)

The core phenotype (100% by definition) is **continuous non-spinning oscillatory self-motion** (rocking, bobbing, swaying) present most of the day, adult-onset, chronic/fluctuating. Frequently co-occurring symptoms: *"Individuals with MdDS may develop co-existing symptoms of spatial disorientation, visual motion intolerance, fatigue, and exacerbation of headaches or anxiety"* ([PMID: 32986636](https://pubmed.ncbi.nlm.nih.gov/32986636/)). The symptom burden is variable across patients: even *"dizziness, fatigue, and brain fog, were endorsed variably across subjects"* ([PMID: 42440785](https://pubmed.ncbi.nlm.nih.gov/42440785/)). Imbalance is largely subjective, though objective postural sway at ~0.2 Hz and oscillating vertical nystagmus on head roll are described. Quality-of-life impact is significant, including occupational disability.

**Suggested HPO terms:** Vertigo (HP:0002321), Abnormal vestibular function (HP:0410008), Fatigue (HP:0012378), Anxiety (HP:0000739), Depressivity (HP:0000716), Impaired concentration / cognitive impairment (HP:0100543), Nystagmus (HP:0000639).

### 13. Genetic/Molecular Basis — Non-Mendelian (F008)

**No causal gene, pathogenic variant, chromosomal abnormality, or Mendelian inheritance pattern** has been identified. MdDS is not catalogued in OMIM as a gene-associated disorder; it is an **acquired, multifactorial functional/central vestibular disorder** triggered by environmental motion exposure ([PMID: 32986636](https://pubmed.ncbi.nlm.nih.gov/32986636/); [PMID: 33746890](https://pubmed.ncbi.nlm.nih.gov/33746890/)). Proposed molecular-level contributors are **neuromodulatory/hormonal rather than genetic**: gonadal (estrogen) influence on vestibular synaptic plasticity ([PMID: 34864753](https://pubmed.ncbi.nlm.nih.gov/34864753/)) and migraine-related physiology (CGRP, serotonergic/sensory-gating pathways) given high migraine comorbidity. No transcriptomic, proteomic, metabolomic, or epigenetic disease signature has been established. Germline/somatic variants, modifier genes, founder effects, penetrance, and carrier frequencies are **not applicable**.

### 14. Prevention, Other Species, and Model Organisms (F013)

**Prevention:** No vaccine, screening program, or proven primary prevention exists. Practical risk reduction is behavioral — limiting/preparing for prolonged provocative passive motion, and, once symptomatic, avoiding triggers, managing stress/sleep, and initiating early VOR-readaptation therapy (tertiary prevention of chronicity). Persistence >6 months predicts lower remission, arguing for early intervention ([PMID: 27730651](https://pubmed.ncbi.nlm.nih.gov/27730651/); [PMID: 34351113](https://pubmed.ncbi.nlm.nih.gov/34351113/)). Genetic counseling is not applicable.

**Other species / natural disease:** MdDS is a **human-specific clinical entity**; no naturally occurring MdDS is documented in companion animals or wildlife (no OMIA entry).

**Model organisms:** There is **no transgenic/knockout genetic model.** The mechanistic underpinning — velocity storage and roll-while-rotating VOR adaptation — was characterized experimentally in **non-human primates (Macaca; NCBI Taxon 9544)** and modeled computationally, informing the human treatment ([PMID: 25076935](https://pubmed.ncbi.nlm.nih.gov/25076935/); [PMID: 41122084](https://pubmed.ncbi.nlm.nih.gov/41122084/)). Rotating optokinetic/roll paradigms in humans serve as the principal experimental system.

### 15. Integrated Synthesis — A Treatable Maladaptive-Plasticity Network Disorder (F016)

Convergent evidence supports a unified causal model: prolonged passive oscillatory motion entrains the central velocity-storage/VOR mechanism, producing a self-sustaining cortico-limbic network dysrhythmia (left entorhinal/amygdala hypermetabolism; altered default-mode/salience/executive and fronto-parietal coherence), which manifests as chronic internal rocking with fatigue, brain fog, visual-motion intolerance, and anxiety ([PMID: 23209584](https://pubmed.ncbi.nlm.nih.gov/23209584/); [PMID: 33746890](https://pubmed.ncbi.nlm.nih.gov/33746890/); [PMID: 30099627](https://pubmed.ncbi.nlm.nih.gov/30099627/); [PMID: 41122084](https://pubmed.ncbi.nlm.nih.gov/41122084/)). Treatment targets each node — VOR/optokinetic readaptation (velocity storage; ~70% response) and DLPFC/cerebellar neuromodulation (network). Response is **heterogeneous and increasingly personalized**: two velocity-storage strategies (correction vs. attenuation) yield differing outcomes, and visual-motion sensitivity predicts poorer response to attenuation approaches ([PMID: 42440785](https://pubmed.ncbi.nlm.nih.gov/42440785/); [PMID: 41122084](https://pubmed.ncbi.nlm.nih.gov/41122084/)).

---

## Mechanistic Model / Interpretation

```
   TRIGGER (upstream)            CENTRAL MALADAPTATION            NETWORK STATE (downstream)         CLINICAL PHENOTYPE
 +--------------------+      +---------------------------+    +---------------------------+    +-----------------------+
 | Prolonged passive  |      | Velocity-storage / VOR    |    | Cortico-limbic dysrhythmia|    | Continuous rocking/    |
 | oscillatory motion | ---> | maladaptation:            |--> | - L entorhinal cortex +   |--> | bobbing/swaying        |
 | (cruise, flight,   |      | roll-while-rotating       |    |   amygdala HYPERmetabolism|    | + fatigue, brain fog,  |
 | car); onset <48 h  |      | cross-axis coupling       |    | - altered DMN/salience/   |    | visual-motion          |
 | after motion ends  |      | (3x3 dynamical system)    |    |   fronto-parietal coherence|   | intolerance, anxiety   |
 +--------------------+      +---------------------------+    +---------------------------+    +-----------------------+
        |                              ^                                  ^                               |
        |  re-exposure to motion       |  VOR / optokinetic               |  rTMS / tDCS over DLPFC        |  migraine prophylaxis,
        +--- transiently RELIEVES -----+  READAPTATION (~70%)             +- neuromodulation (adjunct)     +- CBT, symptomatic Rx
```

**Modifiers/amplifiers:** female sex and gonadal hormones (perimenopausal onset), migraine physiology (CGRP, serotonergic sensory gating), psychological stress, fatigue, sleep deprivation, and busy visual environments. The paradoxical relief on re-exposure to motion is a defining clue that the disorder reflects a *learned/entrained internal model* that is transiently "matched" when real motion resumes.

**Ontology term suggestions:**
- **UBERON / anatomy:** vestibular system, semicircular canal (UBERON:0001840), brainstem vestibular nuclei, entorhinal cortex (UBERON:0002728), amygdala (UBERON:0001876), dorsolateral prefrontal cortex, cerebellum (UBERON:0002037), insula.
- **CL / cell types:** central vestibular neurons; no specific pathological cell population is identified (no cell death or lesion).
- **GO / biological process:** vestibulo-ocular reflex (GO:0060013), regulation of neuronal synaptic plasticity (GO:0048168), adaptation of signaling pathway, sensory perception of balance.
- **CHEBI / chemicals (therapeutic):** verapamil, nortriptyline, topiramate, clonazepam; estradiol/estrogen (modifier).
- **NCIT / interventions:** vestibular rehabilitation therapy, transcranial magnetic stimulation, transcranial direct current stimulation, cognitive behavioral therapy.
- **HPO:** see Finding 12.

---

## Evidence Base

| PMID | Focus | Contribution |
|---|---|---|
| [32986636](https://pubmed.ncbi.nlm.nih.gov/32986636/) | Bárány Society diagnostic criteria | Authoritative case definition, temporal qualifiers, triggers, ICVD classification |
| [25076935](https://pubmed.ncbi.nlm.nih.gov/25076935/) | VOR readaptation relieves MdDS | Core mechanism (VOR maladaptation) + landmark ~70%-response treatment; NHP + human data |
| [41122084](https://pubmed.ncbi.nlm.nih.gov/41122084/) | Model-based treatment-effect heterogeneity | Velocity-storage 3x3 dynamical model; personalization rationale |
| [42440785](https://pubmed.ncbi.nlm.nih.gov/42440785/) | Toward personalized medicine for MdDS | Maladaptive-plasticity framing; variable symptom burden; correction vs. attenuation strategies |
| [23209584](https://pubmed.ncbi.nlm.nih.gov/23209584/) | Metabolic/connectivity changes | Primary FDG-PET/fMRI evidence of limbic hypermetabolism |
| [33746890](https://pubmed.ncbi.nlm.nih.gov/33746890/) | Neuroimaging markers review | Synthesis of limbic focus + connectivity/VBM changes |
| [30099627](https://pubmed.ncbi.nlm.nih.gov/30099627/) | EEG signatures of rTMS treatment | Entrainment brain-state framing; EEG coherence biomarker; midlife-female demographics |
| [28967282](https://pubmed.ncbi.nlm.nih.gov/28967282/) | RSFC signature of rTMS | Connectivity predictor/biomarker of rTMS response |
| [27176615](https://pubmed.ncbi.nlm.nih.gov/27176615/) | Double-blind sham rTMS crossover | Controlled evidence rTMS improves dizziness/mood/anxiety |
| [27117283](https://pubmed.ncbi.nlm.nih.gov/27117283/) | Home tDCS after rTMS RCT | tDCS extends benefit; home safety (0/556 burns) |
| [38345630](https://pubmed.ncbi.nlm.nih.gov/38345630/) | iTBS + VOR rehab RCT | Negative: iTBS adds no benefit over VOR rehab |
| [40228811](https://pubmed.ncbi.nlm.nih.gov/40228811/) | TMS scoping review | Modest / statistically-but-not-clinically-significant benefit |
| [30410464](https://pubmed.ncbi.nlm.nih.gov/30410464/) | Sham-controlled optokinetic stimuli | Controlled support for optokinetic treatment |
| [36323329](https://pubmed.ncbi.nlm.nih.gov/36323329/) | Roll Readaptation case (audiology) | Translation of readaptation to clinic; functional recovery |
| [27730651](https://pubmed.ncbi.nlm.nih.gov/27730651/) | MdDS as vestibular migraine | 73% response to migraine prophylaxis; >6-month prognosis threshold |
| [23674832](https://pubmed.ncbi.nlm.nih.gov/23674832/) | Rocking dizziness & headache | Quantifies migraine comorbidity (41–46%) |
| [34864753](https://pubmed.ncbi.nlm.nih.gov/34864753/) | Sex hormones & vestibular disorders | Hormonal/plasticity basis; female predominance |
| [34351113](https://pubmed.ncbi.nlm.nih.gov/34351113/) | Chronic Dizziness | Differential diagnosis; fluctuating course; management principles |
| [32364688](https://pubmed.ncbi.nlm.nih.gov/32364688/) | "Sickness of disembarkment" review | Normal testing -> exclusion diagnosis |
| [31580016](https://pubmed.ncbi.nlm.nih.gov/31580016/) | The MdDS (review) | Phenotype, female predominance, QoL, normal work-up |
| [40296474](https://pubmed.ncbi.nlm.nih.gov/40296474/) | MdDS in pilots by flight time | Occupational exposure-response relationship |
| [37987715](https://pubmed.ncbi.nlm.nih.gov/37987715/) | MdDS in military operations | Occupational burden; disability/morbidity |

**Convergence vs. challenge:** The mechanistic (VOR/velocity-storage), imaging (limbic/network), and electrophysiological (entrainment) lines of evidence are mutually reinforcing. The main *challenge* within the treatment literature is the negative iTBS RCT ([PMID: 38345630](https://pubmed.ncbi.nlm.nih.gov/38345630/)) and the scoping-review conclusion that TMS benefits are statistically but not clinically significant ([PMID: 40228811](https://pubmed.ncbi.nlm.nih.gov/40228811/)) — tempering enthusiasm for neuromodulation as a stand-alone therapy and reinforcing VOR readaptation as the primary disease-specific intervention.

---

## Limitations and Knowledge Gaps

1. **No population-based epidemiology.** True prevalence and incidence are unknown; all demographic estimates derive from small specialty-clinic case series (often N < 25), risking referral and sex-ascertainment bias.
2. **Small treatment trials.** The pivotal readaptation and neuromodulation studies enroll tens of patients; several are single-arm, crossover, or case reports. There are no large multicenter RCTs and no head-to-head comparisons of readaptation vs. neuromodulation vs. pharmacotherapy.
3. **No validated clinical biomarker.** FDG-PET, fMRI, and EEG signatures are research-only; diagnosis remains purely clinical and by exclusion, contributing to under-recognition and diagnostic delay.
4. **Mechanism is inferential.** The velocity-storage model is well-motivated by NHP physiology and computational modelling but not directly confirmed in human MdDS tissue or with causal manipulation; the relationship between the peripheral VOR account and the cortico-limbic imaging findings is correlational.
5. **No animal disease model.** Absence of a naturalistic or genetic model limits mechanistic dissection and therapeutic screening.
6. **Heterogeneous outcome measures.** Studies use DHI, MdDS Balance Rating Scale, HADS, and postural sway inconsistently, hindering meta-analysis.
7. **Non-motion-triggered variant is poorly delineated** from PPPD, blurring case boundaries.
8. **Molecular biology is essentially unexplored** — no transcriptomic, proteomic, metabolomic, or epigenetic studies; the hormonal/migraine hypotheses remain associative.

---

## Proposed Follow-up Experiments / Actions

1. **Multicenter registry and prevalence study.** Establish a standardized MdDS registry (with the non-motion-triggered variant flagged) to derive population prevalence/incidence, sex ratio, and natural-history remission curves, formally testing the ">6-month = unlikely to remit" threshold.
2. **Definitive RCT of VOR/optokinetic readaptation** with sham control, standardized DHI/MdDS-BRS endpoints, and 12-month follow-up; pre-register correction vs. attenuation strategy arms stratified by baseline visual-motion sensitivity (the predictor identified in [PMID: 42440785](https://pubmed.ncbi.nlm.nih.gov/42440785/)).
3. **Biomarker validation.** Prospectively test whether baseline DLPFC–entorhinal RSFC ([PMID: 28967282](https://pubmed.ncbi.nlm.nih.gov/28967282/)) or EEG alpha/beta coherence ([PMID: 30099627](https://pubmed.ncbi.nlm.nih.gov/30099627/)) predicts response, moving toward a treatment-selection tool.
4. **Hormonal mechanism study.** Characterize onset/severity relative to menstrual cycle, menopause, and hormone therapy to test the gonadal-hormone hypothesis ([PMID: 34864753](https://pubmed.ncbi.nlm.nih.gov/34864753/)); consider a pilot of hormonal modulation.
5. **Migraine-overlap trial.** Head-to-head RCT of vestibular-migraine prophylaxis (verapamil/nortriptyline/topiramate) vs. readaptation vs. combination, given the 73% response signal ([PMID: 27730651](https://pubmed.ncbi.nlm.nih.gov/27730651/)) and CGRP biology; explore anti-CGRP agents as a mechanistically motivated experimental therapy.
6. **Computational/personalized modelling.** Extend the velocity-storage dynamical model ([PMID: 41122084](https://pubmed.ncbi.nlm.nih.gov/41122084/)) into a patient-specific readaptation-protocol optimizer, validated prospectively.
7. **Molecular pilot.** Exploratory plasma metabolomic/proteomic and, where feasible, blood transcriptomic profiling to seek any peripheral signature, acknowledging the low prior probability given the functional nature of the disorder.

---

## Conclusion

Mal de Débarquement Syndrome is an acquired, non-genetic, chronic central/functional vestibular disorder in which prolonged passive oscillatory motion inappropriately conditions the brain's velocity-storage/VOR machinery, producing a self-sustaining cortico-limbic network state that is experienced as continuous internal rocking, bobbing, or swaying — accompanied by fatigue, brain fog, visual-motion intolerance, and anxiety. It predominates in midlife women, is highly comorbid with migraine, and is diagnosed clinically by exclusion in the presence of normal vestibular testing and MRI. The maladaptive-plasticity model is directly actionable: VOR readaptation / optokinetic therapy achieves ~70% substantial improvement, with adjunctive DLPFC neuromodulation and migraine-prophylaxis pharmacotherapy for selected patients. It is not life-threatening but is often chronic and disabling, and early intervention is favored because symptoms persisting beyond six months are less likely to remit spontaneously.


## Artifacts

- [OpenScientist final report](Mal_De_Debarquement-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mal_De_Debarquement-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0060013` (1 mention) - the report calls it "GO / biological process:** vestibulo-ocular reflex"; GO calls it **righting reflex**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001840` (1 mention) - the report calls it "UBERON / anatomy:** vestibular system, semicircular canal"; UBERON calls it **semicircular canal**