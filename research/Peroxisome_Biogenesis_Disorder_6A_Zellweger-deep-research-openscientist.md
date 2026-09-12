---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-10T16:43:01.909612'
end_time: '2026-09-10T17:23:49.380607'
duration_seconds: 2447.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 6A (Zellweger)
  mondo_id: MONDO:0013936
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
citation_count: 42
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 16
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:20959636
  relevance_assessed: 42
  on_topic: 31
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 16
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0000546
    reported_labels:
    - Lab/clinical
    ontology_label: Retinal degeneration
  - term_id: HP:0000407
    reported_labels:
    - Clinical
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0000107
    reported_labels:
    - Imaging/lab
    ontology_label: Renal cyst
  - term_id: HP:0000846
    reported_labels:
    - Lab
    ontology_label: Adrenal insufficiency
  - term_id: HP:0000943
    reported_labels:
    - Imaging
    ontology_label: Dysostosis multiplex
  - term_id: CHEBI:76724
    reported_labels:
    - very-long-chain fatty acid
    ontology_label: 2-hydroxyoctadecanoate
  - term_id: CHEBI:36021
    reported_labels:
    - plasmalogen
    ontology_label: octadec-9-enoic acid
  labels_variant: 6
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
  path: Peroxisome_Biogenesis_Disorder_6A_Zellweger-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Peroxisome_Biogenesis_Disorder_6A_Zellweger-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 6A (Zellweger)
- **MONDO ID:** MONDO:0013936 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 6A (Zellweger)** covering all of the
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

# Peroxisome Biogenesis Disorder 6A (Zellweger) — Comprehensive Disease Characteristics Report

**Disease:** Peroxisome Biogenesis Disorder 6A (Zellweger) — PBD6A
**MONDO ID:** MONDO:0013936 · **OMIM:** #614870 (PBD6A) / #614871 (PBD6B, milder allelic form) · **Gene:** PEX10 (OMIM 602859, 1p36.32)
**Category:** Mendelian, autosomal recessive

---

## Summary

Peroxisome Biogenesis Disorder 6A (Zellweger) is the **severe, PEX10-caused end of the Zellweger spectrum disorder (ZSD) continuum** — a fatal, autosomal-recessive inborn error of organelle biogenesis. Biallelic loss-of-function mutations in **PEX10**, one of ~13–14 *PEX* genes required for peroxisome assembly, disable the peroxisomal matrix-protein import machinery. PEX10 is a **C3HC4 zinc-RING-finger peroxin** that, together with PEX2 and PEX12, forms the E3-ubiquitin-ligase core of the peroxisomal "importomer." This ligase mono- and poly-ubiquitinates the cycling receptor PEX5 to drive its recycling; when it fails, PEX5-mediated delivery of matrix enzymes collapses and peroxisomes become **functionally empty ghosts**. RING-finger missense substitutions (e.g., p.Cys307Tyr, p.Cys276Phe, p.Arg311Gln) map to this critical domain, and the most severe (Zellweger) phenotypes arise when residual function is minimal ([PMID: 32069232](https://pubmed.ncbi.nlm.nih.gov/32069232/), [PMID: 28320181](https://pubmed.ncbi.nlm.nih.gov/28320181/), [PMID: 20679226](https://pubmed.ncbi.nlm.nih.gov/20679226/)).

The downstream biochemistry is a **multi-pathway metabolic failure**: impaired α- and β-oxidation of very-long-chain fatty acids (VLCFA), defective bile-acid synthesis with accumulation of toxic C27 intermediates (DHCA, THCA), and deficient ether-phospholipid (plasmalogen) and DHA synthesis ([PMID: 34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/)). These lesions converge on **mitochondria-mediated oxidative stress and neuronal death**, producing the hallmark neuronal-migration defects (polymicrogyria, pachygyria, germinolytic cysts) alongside hepatic, renal, retinal, auditory, adrenal and skeletal disease ([PMID: 20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/)). Classic Zellweger neonates present at birth with profound hypotonia, seizures, craniofacial dysmorphism and failure to thrive, and **most die within the first year** ([PMID: 28784167](https://pubmed.ncbi.nlm.nih.gov/28784167/), [PMID: 12069541](https://pubmed.ncbi.nlm.nih.gov/12069541/)).

ZSD is rare (~1 in 50,000–90,000 births, with regional founder effects), diagnosed by **elevated plasma VLCFA (C26:0, C26:0/C22:0) and the dried-blood-spot marker C26:0-lysophosphatidylcholine** confirmed by *PEX*-gene sequencing ([PMID: 28677031](https://pubmed.ncbi.nlm.nih.gov/28677031/), [PMID: 30846882](https://pubmed.ncbi.nlm.nih.gov/30846882/)). Management is **supportive**; oral **cholic acid (Cholbam®)** is the sole FDA-approved therapy, and gene/base-editing approaches show preclinical rescue in mouse models ([PMID: 34521419](https://pubmed.ncbi.nlm.nih.gov/34521419/), [PMID: 41981313](https://pubmed.ncbi.nlm.nih.gov/41981313/)). Prevention is limited to genetic counseling, carrier testing and prenatal diagnosis ([PMID: 23327810](https://pubmed.ncbi.nlm.nih.gov/23327810/)).

---

## 1. Disease Information

**Overview.** Zellweger syndrome (ZS), historically the **"cerebro-hepato-renal syndrome,"** was first described in 1964 as a familial syndrome of multiple congenital defects, and is the **severest** of the peroxisome biogenesis disorders (PBDs) ([PMID: 12069541](https://pubmed.ncbi.nlm.nih.gov/12069541/), [PMID: 23327810](https://pubmed.ncbi.nlm.nih.gov/23327810/)). PBD6A is the specific designation for the **PEX10-caused severe (Zellweger) form**; PBD6B is the milder PEX10 form (neonatal adrenoleukodystrophy / infantile-Refsum-like). The three classic clinical labels — Zellweger syndrome (severe), neonatal adrenoleukodystrophy (moderate), and infantile Refsum disease / ataxic form (mild) — are now recognized as a **continuum, the Zellweger spectrum disorder (ZSD)** ([PMID: 28320181](https://pubmed.ncbi.nlm.nih.gov/28320181/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #614870 (PBD6A) · #614871 (PBD6B) · 602859 (PEX10 gene) |
| MONDO | MONDO:0013936 (PBD6A) |
| Orphanet | ORPHA:912 (Zellweger syndrome) |
| MeSH | D015211 (Zellweger Syndrome) |
| ICD-10 | Q87.8 / E71.5x (peroxisomal disorders) |
| ICD-11 | 5C57.0 |

**Synonyms / alternative names.** Zellweger syndrome; cerebro-hepato-renal syndrome (CHRS); PBD, Zellweger type; peroxisome biogenesis disorder 6A; PEX10-related ZSD ([PMID: 23327810](https://pubmed.ncbi.nlm.nih.gov/23327810/), [PMID: 12069541](https://pubmed.ncbi.nlm.nih.gov/12069541/)).

**Information source.** Content is drawn from **aggregated disease-level resources** (OMIM, Orphanet, natural-history cohorts, scoping reviews) supplemented by **individual patient case reports** and small clinical cohorts; there is no large EHR-derived dataset given rarity.

---

## 2. Etiology

**Primary cause — genetic.** PBD6A is caused by **biallelic (homozygous or compound-heterozygous) pathogenic variants in PEX10** ([PMID: 32069232](https://pubmed.ncbi.nlm.nih.gov/32069232/)). "Mutations of 13 different PEX genes lead to PBDs including Zellweger syndrome (ZS)" and "different types of mutations of PEX1 and PEX10 genes are correlated with broad-range phenotypes of PBDs" ([PMID: 32069232](https://pubmed.ncbi.nlm.nih.gov/32069232/)). There is **no environmental or infectious cause**; the disease is fully genetically determined.

**Genetic risk factors.** The causal factor is the loss-of-function *PEX10* genotype itself. **Genotype–phenotype correlation** is central: RING-domain missense changes and severe truncating alleles yield Zellweger; hypomorphic/milder alleles yield NALD or the ataxic form ([PMID: 28320181](https://pubmed.ncbi.nlm.nih.gov/28320181/), [PMID: 27230853](https://pubmed.ncbi.nlm.nih.gov/27230853/)). **Consanguinity** and membership in **founder populations** (see §9) increase risk.

**Environmental / lifestyle / infectious factors.** None causative. This is not a multifactorial or exposure-driven disease. Infections (e.g., neonatal sepsis) are **complications**, not causes ([PMID: 33213396](https://pubmed.ncbi.nlm.nih.gov/33213396/)).

**Protective factors.** No established genetic or environmental protective factors. Within the spectrum, **residual PEX10 function (hypomorphic alleles)** is the principal modifier that "protects" against the severe Zellweger phenotype, shifting patients toward milder, longer-surviving disease ([PMID: 27230853](https://pubmed.ncbi.nlm.nih.gov/27230853/)).

**Gene–environment interactions.** Not applicable in a conventional sense; phenotype is modulated chiefly by allele severity and, in prolonged-survival cases, likely by unknown modifier factors ([PMID: 15098231](https://pubmed.ncbi.nlm.nih.gov/15098231/)).

---

## 3. Phenotypes

Classic (severe) Zellweger presents in the **neonatal period** with a stereotyped, multisystem, progressive phenotype. A scoping review/meta-analysis (107 studies, 307 patients) and a 136-patient natural-history chart review found clinical findings differing significantly across severity categories ([PMID: 35741019](https://pubmed.ncbi.nlm.nih.gov/35741019/)).

| Phenotype | Type | HPO term | Onset | Frequency / severity |
|---|---|---|---|---|
| Severe hypotonia | Clinical sign | HP:0001319 (neonatal hypotonia) | Neonatal | Near-universal, severe |
| Seizures | Clinical sign | HP:0001250 | Neonatal | Very common |
| Craniofacial dysmorphism (high forehead, large fontanelle, flat face, epicanthus, broad nasal bridge, micrognathia) | Physical | HP:0000280 / HP:0000239 | Congenital | Characteristic |
| Retinal degeneration → blindness | Lab/clinical | HP:0000546 | Infancy | "Almost all" ([PMID: 37541626](https://pubmed.ncbi.nlm.nih.gov/37541626/)); median VA ~0.93 logMAR (~20/320) |
| Sensorineural hearing loss | Clinical | HP:0000407 | Infancy | Moderately-severe to severe, slowly progressive ([PMID: 34534157](https://pubmed.ncbi.nlm.nih.gov/34534157/)) |
| Hepatic dysfunction (hepatomegaly, cholestasis, fibrosis, coagulopathy) | Lab/clinical | HP:0002240 / HP:0001394 | Neonatal | Common |
| Renal cysts, hyperoxaluria/stones | Imaging/lab | HP:0000107 | Congenital | Common |
| Adrenal insufficiency | Lab | HP:0000846 | Variable | Reported |
| Global developmental delay / no milestones | Behavioral/developmental | HP:0001263 | Infancy | Severe form reaches no milestones ([PMID: 28784167](https://pubmed.ncbi.nlm.nih.gov/28784167/)) |
| Feeding difficulties / failure to thrive / GERD | Clinical | HP:0011968 / HP:0001508 | Neonatal | Common |
| Chondrodysplasia punctata / epiphyseal stippling, fractures | Imaging | HP:0000943 | Congenital | Reported |

"Common clinical findings that were significantly different across severity categories included seizures, hypotonia, reduced mobility, feeding difficulties, renal cysts, adrenal insufficiency, hearing and vision loss, and a shortened lifespan" ([PMID: 35741019](https://pubmed.ncbi.nlm.nih.gov/35741019/)).

**Quality-of-life impact.** In severe Zellweger, QoL is profoundly limited: affected infants reach no developmental milestones, are cortically blind and deaf, feed poorly and rarely survive infancy ([PMID: 28784167](https://pubmed.ncbi.nlm.nih.gov/28784167/)). Milder spectrum survivors may achieve supported employment and partly independent living, but face progressive gait disorders and sensory loss ([PMID: 26287655](https://pubmed.ncbi.nlm.nih.gov/26287655/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** **PEX10** (HGNC gene, OMIM 602859), chromosome **1p36.32**, encoding an integral peroxisomal-membrane peroxin. PEX10 is "involved in the import of peroxisomal matrix proteins, and the mutation of this gene causes 3 subtypes of peroxisome biogenesis disorders, namely Zellweger syndrome (severe), neonatal adrenoleukodystrophy (moderate) and an ataxic form (mild)" ([PMID: 28320181](https://pubmed.ncbi.nlm.nih.gov/28320181/)).

**Pathogenic variants.**
- **Variant types:** missense (esp. RING-domain), frameshift, nonsense/truncating, and small deletions. Representative pathogenic changes: **p.Cys307Tyr (p.C307Y)** in the RING finger ([PMID: 28320181](https://pubmed.ncbi.nlm.nih.gov/28320181/)); **p.Cys276Phe** and **p.Arg311Gln** in the ataxic form ([PMID: 27230853](https://pubmed.ncbi.nlm.nih.gov/27230853/)); a **homozygous 2-bp deletion** as a Japanese founder allele ([PMID: 12794690](https://pubmed.ncbi.nlm.nih.gov/12794690/)).
- **Classification (ACMG/AMP):** null/frameshift/nonsense alleles are pathogenic (PVS1); RING-domain missense in a well-established functional domain are typically pathogenic/likely pathogenic. Milder cases may carry one hypomorphic allele.
- **Allele frequency:** individually very rare in gnomAD; carrier frequencies elevated in founder populations (see §9).
- **Origin:** germline; no somatic relevance.
- **Functional consequence:** **loss of function** (impaired E3-ligase/importomer activity). No gain-of-function or dominant-negative mechanism is described ([PMID: 20679226](https://pubmed.ncbi.nlm.nih.gov/20679226/)).

**Modifier genes.** Allele severity is the dominant modifier; unidentified factors influence phenotype even for identical genotypes ("next to the PEX1 genotype other yet unknown factors determine the ultimate phenotype," [PMID: 15098231](https://pubmed.ncbi.nlm.nih.gov/15098231/) — an observation that generalizes across ZSD).

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification signatures have been established for PBD6A.

**Chromosomal abnormalities.** None characteristic; PBD6A is a single-gene disorder, not a copy-number/structural syndrome.

---

## 5. Environmental Information

**Environmental factors:** none causative — PBD6A is a purely genetic disorder. **Lifestyle factors:** not applicable. **Infectious agents:** not causative; however, neonates are vulnerable to **overwhelming Gram-negative sepsis** as a complication, consistent with an emerging role of peroxisomes in immune modulation ([PMID: 33213396](https://pubmed.ncbi.nlm.nih.gov/33213396/)). Dietary considerations (VLCFA restriction, DHA and fat-soluble-vitamin supplementation) are therapeutic/supportive rather than etiologic.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic PEX10 loss-of-function mutation** (esp. C3HC4 RING-finger substitution) **leads to** loss of PEX10's E3-ubiquitin-ligase activity within the peroxisomal importomer ([PMID: 20679226](https://pubmed.ncbi.nlm.nih.gov/20679226/)).
2. This **results in** failure to mono-/poly-ubiquitinate the cycling PTS1 receptor **PEX5** (and PTS2 co-receptor PEX7/PEX20), blocking receptor recycling ([PMID: 23344950](https://pubmed.ncbi.nlm.nih.gov/23344950/)).
3. Blocked recycling **leads to** collapse of **peroxisomal matrix-protein import** — peroxisomes form membrane "ghosts" lacking matrix enzymes ([PMID: 28320181](https://pubmed.ncbi.nlm.nih.gov/28320181/)).
4. Absent matrix enzymes **result in** multi-pathway metabolic failure: (a) impaired α-/β-oxidation → **VLCFA accumulation (C26:0)**; (b) defective bile-acid synthesis → **toxic C27 intermediates (DHCA, THCA)**; (c) deficient ether-lipid synthesis → **plasmalogen deficiency**; (d) reduced DHA; branched-chain (phytanic/pristanic) and pipecolic-acid accumulation ([PMID: 34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/)).
5. These lesions **branch** into tissue injury:
   - **Brain branch:** plasmalogen deficiency + lipotoxicity **leads to** **mitochondria-mediated oxidative stress** (↑ROS, ↑MnSOD/SOD2), neuronal apoptosis, and impaired neuronal migration → polymicrogyria/pachygyria, germinolytic cysts, gliosis ([PMID: 20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/)).
   - **Liver branch:** toxic C27 bile acids + VLCFA **result in** cholestasis, fibrosis/cirrhosis, coagulopathy.
   - **Kidney / eye / ear / adrenal / bone branches:** metabolic injury **results in** renal cysts, retinal degeneration, sensorineural hearing loss, adrenal insufficiency, chondrodysplasia punctata.
6. Combined multisystem failure **leads to** the classic Zellweger clinical picture and **early death, usually within the first year** ([PMID: 12069541](https://pubmed.ncbi.nlm.nih.gov/12069541/)).

*(Steps 1–4 are mechanistically demonstrated in cell/animal models; the oxidative-stress neurodegeneration step is directly demonstrated in a PEX13 brain model and inferred to generalize to PEX10.)*

### Detail by category

- **Molecular pathways:** peroxisomal matrix-protein import (importomer / receptor-recycling); ubiquitin–proteasome-linked receptor cycling. "The integral peroxisomal membrane proteins PEX10, PEX2, and PEX12 contain a zinc RING finger close to the C terminus" and act as E3 ligases for PEX5/Pex20 ubiquitination ([PMID: 20679226](https://pubmed.ncbi.nlm.nih.gov/20679226/), [PMID: 23344950](https://pubmed.ncbi.nlm.nih.gov/23344950/)).
- **Cellular processes:** apoptosis, oxidative-stress response, gliosis (astro-/microgliosis), defective neuronal migration; dysregulated pexophagy (PEX13/PEX5-ubiquitin axis) ([PMID: 20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/), [PMID: 36541703](https://pubmed.ncbi.nlm.nih.gov/36541703/)).
- **Protein dysfunction:** loss of PEX10 RING-finger E3-ligase function; Zn²⁺-coordination disruption abolishes activity (embryo-lethal in *Arabidopsis*) ([PMID: 12883010](https://pubmed.ncbi.nlm.nih.gov/12883010/), [PMID: 20679226](https://pubmed.ncbi.nlm.nih.gov/20679226/)).
- **Metabolic changes:** VLCFA ↑, C27 bile-acid intermediates ↑, plasmalogens ↓, DHA ↓, phytanic/pristanic/pipecolic acid ↑ ([PMID: 34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/)).
- **Tissue damage:** oxidative stress, mitochondrial dysfunction, apoptosis ([PMID: 20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/)).
- **Immune involvement:** peroxisomes modulate immune response/inflammation; deficiency associated with sepsis vulnerability ([PMID: 33213396](https://pubmed.ncbi.nlm.nih.gov/33213396/)).
- **Molecular profiling (models):** Pex11α-KO mice show serum/liver/heart lipidomic, metabolomic and proteomic dysregulation ([PMID: 35083512](https://pubmed.ncbi.nlm.nih.gov/35083512/)); base editing normalizes liver transcriptomes and eliminates VLCFA/BCFA/C27 bile-acid accumulation ([PMID: 41981313](https://pubmed.ncbi.nlm.nih.gov/41981313/)).

**Suggested ontology terms.** GO:0016558 (protein import into peroxisome matrix); GO:0007031 (peroxisome organization); GO:0006635 (fatty-acid β-oxidation); GO:0008203 (cholesterol/bile-acid metabolism); GO:0006979 (response to oxidative stress); GO:0001764 (neuron migration). CL:0000540 (neuron); CL:0000121 (Purkinje cell); CL:0000573 (retinal photoreceptor); CL:0000182 (hepatocyte). CHEBI:76724 (very-long-chain fatty acid); CHEBI:36021 (plasmalogen); CHEBI:3098 (bile acid).

---

## 7. Anatomical Structures Affected

**Organ / body-system level.** Multisystem — the name *cerebro-hepato-renal* enumerates the three primary organs. Primary: **brain/CNS** (nervous system), **liver** (digestive/hepatobiliary), **kidney** (urinary). Secondary/associated: **eyes** (retina, lens, optic nerve), **ears** (cochlea), **adrenal glands** (endocrine), **skeleton**, **GI tract** ([PMID: 37144748](https://pubmed.ncbi.nlm.nih.gov/37144748/), [PMID: 33213396](https://pubmed.ncbi.nlm.nih.gov/33213396/)).

**Tissue / cell level.** Neurons and neuronal-migration units (cortex, cerebellar granule and Purkinje cells), hepatocytes and biliary epithelium, renal tubular/cortical tissue, retinal photoreceptors and RPE, cochlear sensory cells. The PEX13 brain model shows "impaired cerebellar fissure/cortical layer formation, defective granule cell migration and Purkinje cell layer development" ([PMID: 20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/)).

**Subcellular level.** The **peroxisome** (GO:0005777) is absent/reduced (membrane ghosts persist); secondary **mitochondrial** dysfunction (GO:0005739) contributes to oxidative injury.

**Localization / lateralization.** Bilateral, symmetric multisystem involvement; brain malformations (polymicrogyria, pachygyria, germinolytic subependymal cysts) are typically bilateral. Suggested UBERON terms: UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0002107 (liver), UBERON:0002113 (kidney), UBERON:0000966 (retina), UBERON:0001846 (inner ear), UBERON:0002369 (adrenal gland).

---

## 8. Temporal Development

**Onset.** **Congenital / neonatal.** Severe Zellweger presents at or shortly after birth with hypotonia and seizures ([PMID: 28784167](https://pubmed.ncbi.nlm.nih.gov/28784167/)); the pattern is chronic-progressive from birth.

**Progression.** In the severe form the course is **rapidly progressive**, with failure to thrive and early death, usually **before age 1 year**; patients reach no developmental milestones ([PMID: 12069541](https://pubmed.ncbi.nlm.nih.gov/12069541/)). Across the broader spectrum, intermediate/mild patients survive into childhood or adulthood (cohorts to 24–35 years) with variable courses — stable, slowly declining, or with adolescent-onset progressive gait disorder/leukodystrophy ([PMID: 26287655](https://pubmed.ncbi.nlm.nih.gov/26287655/), [PMID: 15098231](https://pubmed.ncbi.nlm.nih.gov/15098231/)).

**Patterns.** No spontaneous remission. **Critical periods:** the neonatal window is the period of greatest vulnerability and the target window for any disease-modifying intervention; leukoencephalopathy accrues with age in longer survivors ([PMID: 18415699](https://pubmed.ncbi.nlm.nih.gov/18415699/), [PMID: 14872027](https://pubmed.ncbi.nlm.nih.gov/14872027/)).

---

## 9. Inheritance and Population

**Epidemiology.** ZSD incidence ~**1 in 50,000–90,000 births**. New-York newborn screening estimated ~1 in 90,000 (from 1.08 million screenings) — "Our results are close to current newborn screening estimates in New York of 1 in 90,000 births, estimated from 1.08 million screenings"; an ExAC-based bioinformatic estimate gave ~1 in 83,841 ([PMID: 30846882](https://pubmed.ncbi.nlm.nih.gov/30846882/)). Japan overall ~1 in 500,000–800,000, but Okinawa 1 in 30,000 ([PMID: 8914632](https://pubmed.ncbi.nlm.nih.gov/8914632/)).

**Inheritance.** **Autosomal recessive**, complete penetrance for the biochemical/genetic phenotype; **variable expressivity** governed by allele severity. No anticipation (not a repeat-expansion disorder). Germline mosaicism not a notable feature.

**Founder effects / consanguinity.** A **PEX6 founder mutation** in Saguenay-Lac-St-Jean, Quebec gives "Incidence of ZS was estimated to 1 in 12,191 live births, with a carrier frequency of 1 in 55" ([PMID: 22894767](https://pubmed.ncbi.nlm.nih.gov/22894767/)). A **homozygous 2-bp PEX10 deletion is a founder allele** among Japanese complementation-group-B patients — "All the 11 ZS patients with group-B PBD had a common mutation, i.e., a homozygous 2-base-pair deletion in PEX10" ([PMID: 12794690](https://pubmed.ncbi.nlm.nih.gov/12794690/)). Consanguinity increases risk.

**Population demographics.** Panethnic; regional clustering where founder alleles exist (French-Canadian Quebec; Okinawa). **Sex ratio ~1:1** (autosomal). Age distribution skews to neonates/infants for the severe form.

---

## 10. Diagnostics

**Biochemical testing (first-line).** Elevated plasma **VLCFA — C26:0, C26:0/C22:0 and C24:0/C22:0 ratios**; elevated pipecolic, phytanic/pristanic acids; abnormal C27 bile-acid intermediates (DHCA/THCA); reduced erythrocyte plasmalogens ([PMID: 34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/)).

**Dried-blood-spot marker.** **C26:0-lysophosphatidylcholine (C26:0-lysoPC)** is sensitive: "Elevated C26:0-lysoPC levels (>72 nmol/L) were found in 86/91 ZSD DBS (n=33/37 patients) corresponding to a sensitivity of 89.2%" (median 567 nmol/L), whereas C26:0-carnitine is less sensitive (55.2%) — "C26:0-lysoPC in DBS is a sensitive and useful marker for VLCFA accumulation in patients with a ZSD" ([PMID: 28677031](https://pubmed.ncbi.nlm.nih.gov/28677031/)). This is the analyte used in tandem-MS newborn screening (implemented primarily for X-ALD/ABCD1), which **incidentally detects ZSD** ([PMID: 36256460](https://pubmed.ncbi.nlm.nih.gov/36256460/)).

**Genetic testing (confirmatory).** Sequencing the ~13 *PEX* genes — whole-exome sequencing or targeted **PBD/peroxisomal gene panels**; **single-gene PEX10 testing** where a founder allele is known. Classic functional confirmation is **complementation analysis in cultured fibroblasts**. Note that milder alleles may yield near-normal fibroblast studies, making **molecular analysis essential** at the mild end ([PMID: 19127411](https://pubmed.ncbi.nlm.nih.gov/19127411/)).

**Imaging.** Brain MRI is highly informative: "cMRI pathology in ZSS consists of abnormal gyration pattern including polymicrogyria and pachygyria, leukencephalopathy, germinolytic cysts and heterotopias" ([PMID: 18415699](https://pubmed.ncbi.nlm.nih.gov/18415699/)); polymicrogyria/pachygyria predominate in severe disease, leukoencephalopathy in longer survivors ([PMID: 14872027](https://pubmed.ncbi.nlm.nih.gov/14872027/)).

**Differential diagnosis.** Other *PEX*-gene ZSDs (PEX1/PEX6/PEX2/PEX12/PEX26); **single peroxisomal enzyme defects that are "Zellweger-like"** — notably **D-bifunctional protein (HSD17B4) deficiency** ("Peroxisomal D-bifunctional protein (DBP) deficiency is an autosomal recessive disorder historically described as a Zellweger-like syndrome comprising neonatal seizures, retinopathy, hearing loss, dysmorphic features," [PMID: 32904102](https://pubmed.ncbi.nlm.nih.gov/32904102/)) and acyl-CoA oxidase deficiency; rhizomelic chondrodysplasia punctata; Heimler syndrome (mild PEX1/PEX6, [PMID: 26387595](https://pubmed.ncbi.nlm.nih.gov/26387595/)); and non-peroxisomal causes of neonatal hypotonia/renal cysts/epiphyseal stippling such as Smith-Lemli-Opitz and warfarin embryopathy ([PMID: 40995270](https://pubmed.ncbi.nlm.nih.gov/40995270/), [PMID: 39359950](https://pubmed.ncbi.nlm.nih.gov/39359950/)).

**Screening.** Cascade carrier testing in families; prenatal diagnosis on CVS/amniocytes (VLCFA/DHAPAT enzyme assay or molecular testing); newborn C26:0-LPC screening detects ZSD as a secondary finding.

---

## 11. Outcome / Prognosis

**Survival.** Severity-dependent. Classic (severe) Zellweger — the cerebro-hepato-renal syndrome — "is characterized by the presence of dysmorphias and polymalformative syndrome, severe neurologic abnormalities including neurosensory defects and hepato-intestinal dysfunction with failure to thrive and usually early death," typically **before 1 year** ([PMID: 12069541](https://pubmed.ncbi.nlm.nih.gov/12069541/)). Intermediate/mild patients survive into childhood or adulthood ([PMID: 26287655](https://pubmed.ncbi.nlm.nih.gov/26287655/)).

**Prognostic biomarker.** Serum VLCFA, particularly **C26:0**, correlates with severity: "The best predictive value for estimating the projected disease severity and survival time is a concentration of C26:0" ([PMID: 32946460](https://pubmed.ncbi.nlm.nih.gov/32946460/)).

**Morbidity / function.** Severe global disability — cortical blindness, deafness, no developmental milestones, seizures, hepatic and renal failure. Complications: coagulopathy, adrenal crisis, fractures, feeding failure, and vulnerability to **overwhelming neonatal sepsis** ([PMID: 33213396](https://pubmed.ncbi.nlm.nih.gov/33213396/)).

**Recovery potential.** None for the severe form; care is palliative/supportive. Milder spectrum patients may stabilize for years ([PMID: 26287655](https://pubmed.ncbi.nlm.nih.gov/26287655/)).

---

## 12. Treatment

**Pharmacotherapy.** **Oral cholic acid (Cholbam®)** — the **only FDA-approved therapy** (March 2015), an adjunctive treatment for ZSDs and single-enzyme bile-acid-synthesis disorders. "Cholbam® (cholic acid), approved by the U.S. Food and Drug Administration in March 2015, is currently the only therapy approved as adjunctive treatment for patients with ZSDs and single enzyme bile acid synthesis disorders" ([PMID: 34521419](https://pubmed.ncbi.nlm.nih.gov/34521419/)). It suppresses endogenous bile-acid synthesis, lowering toxic C27 intermediates and improving liver chemistries. In a Phase-3 continuation study (53 patients, 12 with ZSD), "statistically significant improvements in urinary bile acids (P = 0.003), height (P < 0.001), and body weight (P < 0.001) were observed" ([PMID: 31899729](https://pubmed.ncbi.nlm.nih.gov/31899729/)); extension studies confirm sustained suppression ([PMID: 30793331](https://pubmed.ncbi.nlm.nih.gov/30793331/), [PMID: 30519152](https://pubmed.ncbi.nlm.nih.gov/30519152/)). NCIT: C29076 (cholic acid).

**Adjunct / experimental medical therapies.** DHA, **Lorenzo's oil**, **batyl alcohol**, and fat-soluble-vitamin supplementation have partial/anecdotal support: "There is some support for the pharmacologic therapies of Lorenzo's oil, docosohexanoic acid, and batyl alcohol in altering symptoms; however, systematic long-term studies are lacking" ([PMID: 34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/)).

**Advanced therapeutics (preclinical).** **In vivo adenine base editing** (AAV9-ABE8e) corrected up to 60% of the pathogenic allele in liver of a Pex1-G844D ZSD mouse; "base editing eliminated bulk accumulation of very long-chain and branched-chain fatty acids, and toxic C27-bile acid intermediates," and normalized liver histology/transcriptomes ([PMID: 41981313](https://pubmed.ncbi.nlm.nih.gov/41981313/)). **AAV8 gene therapy** is in development for the retinal phenotype ([PMID: 42182139](https://pubmed.ncbi.nlm.nih.gov/42182139/)). **Hepatocyte transplantation** has been explored in models ([PMID: 33396635](https://pubmed.ncbi.nlm.nih.gov/33396635/)).

**Supportive / rehabilitative.** Anti-epileptic drugs; nutritional support/gastrostomy for feeding failure; hearing amplification (improves outcomes, [PMID: 34534157](https://pubmed.ncbi.nlm.nih.gov/34534157/)); low-vision support; adrenal replacement; management of coagulopathy and liver disease; physical/occupational/speech therapy. Care is multidisciplinary and largely palliative in the severe form.

---

## 13. Prevention

**No primary prevention exists** for this congenital, autosomal-recessive genetic disorder with no environmental/infectious cause. "As it is fatal in early life, genetic counseling and prenatal diagnosis are thus crucial" ([PMID: 23327810](https://pubmed.ncbi.nlm.nih.gov/23327810/)). Preventive mainstays:

- **Genetic counseling** for at-risk couples (25% recurrence risk per pregnancy).
- **Carrier testing / cascade screening** in families and founder populations.
- **Prenatal diagnosis** on CVS/amniocytes (VLCFA / DHAPAT enzyme assay or molecular testing) and **preimplantation genetic diagnosis (PGD)**.
- **Secondary prevention:** newborn C26:0-LPC screening enables early identification and supportive intervention. Note the ethical caveat — "The Dutch Health Council recommended to screen only male newborns for ALD without identifying untreatable conditions associated with elevated C26:0-LPC, like Zellweger spectrum disorders" ([PMID: 36256460](https://pubmed.ncbi.nlm.nih.gov/36256460/)).
- **Tertiary prevention:** cholic acid, nutritional support, sensory-aid provision to limit complications.

No immunization or public-health/environmental interventions are applicable.

---

## 14. Other Species / Natural Disease

**Model species with orthologs.** PEX10 orthologs are conserved across eukaryotes — mouse (*Mus musculus*, NCBI Taxon 10090), zebrafish (*Danio rerio*, 7955), *Arabidopsis thaliana* (3702), and yeasts (*Hansenula/Pichia*, *Saccharomyces*). In *Arabidopsis*, PEX10 dysfunction is **embryo-lethal**: "dysfunction of a homologous gene in Arabidopsis leads to lethality at the heart stage of embryogenesis, impairing the biogenesis of peroxisomes, lipid bodies, and protein bodies" ([PMID: 12883010](https://pubmed.ncbi.nlm.nih.gov/12883010/)), underscoring deep evolutionary conservation of the peroxisome-import machinery.

**Natural disease in companion/wildlife species.** No well-characterized naturally occurring PEX10-Zellweger equivalent is documented in the reviewed literature (OMIA searches were not resolved in this investigation). **Not zoonotic** — this is a Mendelian metabolic disorder, not transmissible.

---

## 15. Model Organisms

| Model | Type | Key features / recapitulation | Reference |
|---|---|---|---|
| **PEX1-p.Gly844Asp (G844D) mouse** | Mammalian knock-in | Models the common human PEX1-p.Gly843Asp allele; reproduces **retinal & RPE degeneration with subretinal inflammation, liver pathology, metabolic dysfunction** | [PMID: 40058592](https://pubmed.ncbi.nlm.nih.gov/40058592/), [PMID: 41981313](https://pubmed.ncbi.nlm.nih.gov/41981313/) |
| **Brain-restricted PEX13-deficient mouse** | Mammalian conditional KO | **Reduced plasmalogens, impaired cerebellar development, defective granule-cell migration, astro-/microgliosis, ↑ROS/MnSOD, neuronal apoptosis** — mechanistic Zellweger brain model | [PMID: 20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/) |
| **Pex11α-KO mouse** | Mammalian KO | Serum/liver/heart lipidomic, metabolomic, proteomic dysregulation | [PMID: 35083512](https://pubmed.ncbi.nlm.nih.gov/35083512/) |
| **Zebrafish pex mutants (e.g., PEX13)** | Vertebrate | Established peroxisome/pexophagy models | [PMID: 36541703](https://pubmed.ncbi.nlm.nih.gov/36541703/) |
| ***Arabidopsis* AthPEX10 T-DNA mutant** | Plant | Embryo-lethal; absent peroxisomes/oil bodies — proves conserved essentiality | [PMID: 12883010](https://pubmed.ncbi.nlm.nih.gov/12883010/) |
| **Yeast (Pichia/Hansenula)** | Fungal | Defined importomer/Pex20 ubiquitination biochemistry | [PMID: 23344950](https://pubmed.ncbi.nlm.nih.gov/23344950/) |

**Applications & limitations.** Models faithfully reproduce the **biochemical lesion** (VLCFA/plasmalogen/bile-acid abnormalities) and organ pathology (retina, liver, cerebellum), and have enabled proof-of-concept **base-editing and AAV gene therapy** ([PMID: 41981313](https://pubmed.ncbi.nlm.nih.gov/41981313/), [PMID: 42182139](https://pubmed.ncbi.nlm.nih.gov/42182139/)). Limitations: most established models use **PEX1**, not PEX10; complete null models are often perinatally lethal, limiting study of later neurodegeneration; and no single model captures the full human multisystem severity spectrum.

---

## Mechanistic Model / Interpretation

```
 PEX10 biallelic LoF (C3HC4 RING-finger mutation)
        │  abolishes E3-ubiquitin-ligase activity
        ▼
 Importomer failure → PEX5 receptor not ubiquitinated/recycled
        │
        ▼
 Collapse of peroxisomal matrix-protein import  → "ghost" peroxisomes
        │
        ├──► ↓ β-/α-oxidation ─────► VLCFA ↑ (C26:0), phytanic/pristanic ↑
        ├──► defective bile-acid synth ─► toxic C27 intermediates (DHCA/THCA) ↑
        ├──► ↓ ether-lipid synth ──────► plasmalogen ↓, DHA ↓
        │
        ▼   (convergence)
 Mitochondria-mediated OXIDATIVE STRESS (↑ROS, ↑SOD2) + lipotoxicity
        │
   ┌────┴───────────────┬──────────────┬───────────────┬─────────────┐
   ▼                    ▼              ▼               ▼             ▼
 BRAIN               LIVER          KIDNEY           EYE/EAR       ADRENAL/BONE
 migration defects   cholestasis    cortical cysts   retinopathy   insufficiency
 (PMG/pachygyria),   fibrosis,      hyperoxaluria    SNHL          chondrodysplasia
 germinolytic cysts, coagulopathy                                  punctata
 apoptosis, gliosis
        │
        ▼
 Classic Zellweger phenotype → death usually < 1 year
```

The unifying interpretation is that **a single upstream molecular lesion (RING-E3 failure) produces a broad metabolic derangement** because peroxisomes host many non-redundant pathways. Severity tracks with **residual PEX10 function**: null/severe alleles → Zellweger; hypomorphic alleles → NALD/ataxic form with survival into adulthood. **C26:0 is both the diagnostic and prognostic readout** of this pathway, and correcting the pathway (base editing) reverses the biochemistry in models — validating the causal chain.

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [32069232](https://pubmed.ncbi.nlm.nih.gov/32069232/) | PEX10 among 13 PEX genes; genotype–phenotype correlation | Supports etiology (F001) |
| [28320181](https://pubmed.ncbi.nlm.nih.gov/28320181/) | PEX10 import function; severity spectrum; RING p.C307Y | Supports gene function/variants (F001) |
| [20679226](https://pubmed.ncbi.nlm.nih.gov/20679226/) | PEX10/PEX2/PEX12 zinc-RING E3 ligases | Supports mechanism (F012) |
| [23344950](https://pubmed.ncbi.nlm.nih.gov/23344950/) | RING peroxins ubiquitinate PTS receptors | Supports mechanism |
| [34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/) | VLCFA/bile-acid metabolic failure; adjunct therapies | Supports mechanism/treatment (F002, F003) |
| [28784167](https://pubmed.ncbi.nlm.nih.gov/28784167/) | Classic Zellweger neonatal phenotype | Supports phenotype (F002) |
| [35741019](https://pubmed.ncbi.nlm.nih.gov/35741019/) | Severity-graded clinical findings (meta-analysis) | Supports phenotypes (F004) |
| [37541626](https://pubmed.ncbi.nlm.nih.gov/37541626/) | Near-universal retinal degeneration | Supports phenotype (F004) |
| [34534157](https://pubmed.ncbi.nlm.nih.gov/34534157/) | Sensorineural hearing-loss characterization | Supports phenotype (F004) |
| [20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/) | Oxidative-stress neurodegeneration (PEX13 brain model) | Supports mechanism (F007) |
| [28677031](https://pubmed.ncbi.nlm.nih.gov/28677031/) | C26:0-lysoPC DBS marker (89.2% sensitivity) | Supports diagnostics (F008) |
| [36256460](https://pubmed.ncbi.nlm.nih.gov/36256460/) | ZSD detected as secondary finding of C26:0-LPC NBS | Supports diagnostics (F008) |
| [32946460](https://pubmed.ncbi.nlm.nih.gov/32946460/) | C26:0 best predictor of severity/survival | Supports prognosis (F009) |
| [18415699](https://pubmed.ncbi.nlm.nih.gov/18415699/) | MRI: polymicrogyria/pachygyria, germinolytic cysts | Supports diagnostics (F009) |
| [12069541](https://pubmed.ncbi.nlm.nih.gov/12069541/) | Historical CHRS synonym; early-death course | Supports identity/prognosis (F009, F010) |
| [23327810](https://pubmed.ncbi.nlm.nih.gov/23327810/) | Fatal AR disorder; counseling/prenatal prevention | Supports identity/prevention (F010) |
| [30846882](https://pubmed.ncbi.nlm.nih.gov/30846882/) | Incidence ~1/90,000 (NBS) | Supports epidemiology (F006) |
| [22894767](https://pubmed.ncbi.nlm.nih.gov/22894767/) | PEX6 founder effect Quebec (1/12,191; carrier 1/55) | Supports epidemiology (F006) |
| [12794690](https://pubmed.ncbi.nlm.nih.gov/12794690/) | PEX10 founder 2-bp deletion, Japan | Supports epidemiology (F006) |
| [34521419](https://pubmed.ncbi.nlm.nih.gov/34521419/) | Cholic acid sole FDA-approved therapy | Supports treatment (F003) |
| [31899729](https://pubmed.ncbi.nlm.nih.gov/31899729/) | Phase-3 cholic-acid efficacy (urinary BA P=0.003) | Supports treatment (F003) |
| [41981313](https://pubmed.ncbi.nlm.nih.gov/41981313/) | In vivo base editing rescues ZSD mouse | Supports treatment/models (F005) |
| [40058592](https://pubmed.ncbi.nlm.nih.gov/40058592/) | PEX1-G844D mouse retinal/RPE phenotype | Supports models (F005) |
| [32904102](https://pubmed.ncbi.nlm.nih.gov/32904102/) | DBP deficiency = Zellweger-like DDx | Supports diagnostics (F012) |
| [26387595](https://pubmed.ncbi.nlm.nih.gov/26387595/) | Heimler = mild PBD (PEX1/PEX6) | Supports DDx/spectrum |
| [33213396](https://pubmed.ncbi.nlm.nih.gov/33213396/) | Peroxisomes in immunity; neonatal sepsis | Supports anatomy/immune (F011) |
| [37144748](https://pubmed.ncbi.nlm.nih.gov/37144748/) | Craniofacial/neonatal presentation (PEX6 severe) | Supports anatomy (F011) |
| [12883010](https://pubmed.ncbi.nlm.nih.gov/12883010/) | Arabidopsis PEX10 embryo-lethal; conservation | Supports models (F012) |
| [39359950](https://pubmed.ncbi.nlm.nih.gov/39359950/) | Lists related PBD phenotypes (differential spectrum) | Supports DDx |

---

## Limitations and Knowledge Gaps

1. **PEX10-specific data are sparse.** Much mechanistic and therapeutic evidence derives from **PEX1** (most common ZSD gene) and **PEX13** models; direct PEX10 mouse models with full multisystem recapitulation are lacking. Genotype–phenotype claims for PEX10 rest on relatively few case reports.
2. **No PEX10-specific epidemiology.** Incidence figures (1/50,000–90,000) are pan-ZSD; the PEX10 fraction and its precise carrier frequency (outside the Japanese founder allele) are not well quantified.
3. **Prognostic quantification is limited.** C26:0 predicts severity, but no validated multivariable survival model exists for PBD6A specifically.
4. **Therapeutics are palliative.** Cholic acid addresses the bile-acid arm only; it does not correct VLCFA/plasmalogen deficits or CNS disease. Base editing/gene therapy remain **preclinical**, tested largely in PEX1 models and in accessible organs (liver, retina), not brain.
5. **Epigenetics, standardized QoL instruments, and veterinary/natural-disease data** were not resolved in this investigation and represent genuine gaps.
6. **Newborn-screening ethics.** C26:0-LPC screening detects untreatable ZSD as a secondary finding — a policy/counseling challenge rather than a clinical benefit.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a PEX10 RING-domain knock-in mouse** (e.g., p.C307Y) to obtain a PEX10-specific severity model and compare with PEX1-G844D.
2. **Establish PEX10 genotype–phenotype curation** across ClinVar/case literature, correlating residual E3-ligase activity (in vitro PEX5-ubiquitination assays) with clinical severity and C26:0.
3. **Extend base-editing/AAV gene therapy to PEX10 and to CNS delivery** (BBB-crossing AAV capsids; intrathecal routes), testing whether early correction prevents neuronal-migration defects (requires prenatal/perinatal timing).
4. **Prospective natural-history registry** capturing standardized QoL (infant-adapted PROMIS), survival, and biomarker trajectories to build a PBD6A-specific prognostic model.
5. **Biomarker refinement:** validate C26:0-lysoPC cutoffs and combine with bile-acid intermediates for higher specificity in newborn screening, and evaluate plasmalogen/DHA as treatment-response markers.
6. **Screen approved drugs / chaperones** that stabilize hypomorphic PEX10 or upregulate residual peroxisome import, potentially converting severe to milder phenotypes.
7. **Search OMIA / veterinary databases** to determine whether naturally occurring peroxisome-biogenesis disease exists in companion animals for comparative study.

---

*Report compiled from a 5-iteration autonomous investigation: 12 confirmed findings, 55 papers reviewed. Evidence sources span human clinical cohorts, model-organism (mouse/zebrafish/plant/yeast) studies, in vitro biochemistry, and computational/population-genetic estimates.*


## Artifacts

- [OpenScientist final report](Peroxisome_Biogenesis_Disorder_6A_Zellweger-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Peroxisome_Biogenesis_Disorder_6A_Zellweger-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 42 |
| On topic | 31 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:20959636` *(abstract only)*: "impaired cerebellar fissure/cortical layer formation, defective granule cell migration and Purkinje cell layer development"
  - closest text in source: "PEX13 brain mutants exhibit defects in reflex and motor development that correlate with impaired cerebellar fissure and cortical layer formation, granule cell migration and Purkinje cell layer development"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 30 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0000546` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Retinal degeneration**
- `HP:0000407` (1 mention) - the report calls it "Clinical"; HP calls it **Sensorineural hearing impairment**
- `HP:0000107` (1 mention) - the report calls it "Imaging/lab"; HP calls it **Renal cyst**
- `HP:0000846` (1 mention) - the report calls it "Lab"; HP calls it **Adrenal insufficiency**
- `HP:0000943` (1 mention) - the report calls it "Imaging"; HP calls it **Dysostosis multiplex**
- `CHEBI:76724` (1 mention) - the report calls it "very-long-chain fatty acid"; CHEBI calls it **2-hydroxyoctadecanoate**
- `CHEBI:36021` (1 mention) - the report calls it "plasmalogen"; CHEBI calls it **octadec-9-enoic acid**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0013936` (2 mentions) - the report calls it "PBD6A"; MONDO calls it **peroxisome biogenesis disorder 6A (Zellweger)**, and lists "PBD6A" among its other names
- `HP:0001263` (1 mention) - the report calls it "Behavioral/developmental"; HP calls it **Global developmental delay**, and lists "Retarded development" among its other names
- `GO:0006635` (1 mention) - the report calls it "fatty-acid β-oxidation"; GO calls it **fatty acid beta-oxidation**
- `GO:0008203` (1 mention) - the report calls it "cholesterol/bile-acid metabolism"; GO calls it **cholesterol metabolic process**, and lists "cholesterol metabolism" among its other names
- `CL:0000573` (1 mention) - the report calls it "retinal photoreceptor"; CL calls it **retinal cone cell**
- `UBERON:0001846` (1 mention) - the report calls it "inner ear"; UBERON calls it **internal ear**, and lists "inner ear" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.