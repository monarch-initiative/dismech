---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T16:12:25.483453'
end_time: '2026-08-29T16:28:15.310364'
duration_seconds: 949.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Recessive Intermediate D
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
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:23001492
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 36
  not_found: 0
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 32
  labels_matching: 17
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: DOID:0110203
    reported_labels:
    - DOID
    ontology_label: Charcot-Marie-Tooth disease recessive intermediate D
  - term_id: HP:0002936
    reported_labels:
    - Distal sensory impairment
    - Symptom/sign
    ontology_label: Distal sensory impairment
  - term_id: HP:0003400
    reported_labels:
    - Onion bulb formation** (demyelination/remyelination hallmark)
    - Lab/electrophysiology + pathology
    ontology_label: Basal lamina onion bulb formation
  - term_id: HP:0003376
    reported_labels:
    - Steppage gait (foot drop)
    - Symptom
    ontology_label: Steppage gait
  - term_id: HP:0001761
    reported_labels:
    - Pes cavus
    - Physical manifestation
    ontology_label: Pes cavus
  - term_id: HP:0002151
    reported_labels:
    - Lab abnormality
    ontology_label: Increased circulating lactate concentration
  - term_id: HP:0003202
    reported_labels:
    - Pathology
    ontology_label: Skeletal muscle atrophy
  - term_id: UBERON:0002470
    reported_labels:
    - pelvic limb
    ontology_label: autopod region
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0005751
    ontology_label: obsolete mitochondrial respiratory chain complex IV
    replaced_by: GO:0045277
  unresolvable_prefixes:
  - ORPHA
  - GARD
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Charcot-Marie-Tooth_Disease_Recessive_Intermediate_D-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Charcot-Marie-Tooth_Disease_Recessive_Intermediate_D-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Recessive Intermediate D
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Recessive Intermediate D** covering all of the
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

# Charcot-Marie-Tooth Disease Recessive Intermediate D (CMTRID)
### A Comprehensive Disease Characterization Report

**Prepared:** 2026-08-29 | **Evidence base:** Primary literature (PubMed), OMIM/Orphanet/HGNC identifiers, and general CMT clinical literature.

> **Scope note:** CMTRID is an **ultra-rare Mendelian mitochondrial peripheral neuropathy** caused by biallelic *COX6A1* variants. Fewer than ~10 families/individuals are described in the literature worldwide. Consequently, many quantitative epidemiologic, prognostic, and treatment-trial parameters are **not established specifically for CMTRID**; where this is the case it is stated explicitly, and general CMT knowledge is used as the best available proxy and labeled as such.

---

## 1. Disease Information

**Overview.** Charcot-Marie-Tooth disease Recessive Intermediate D (CMTRID) is a rare autosomal-recessive form of inherited peripheral neuropathy (hereditary motor and sensory neuropathy, HMSN). Clinically it presents as a length-dependent, slowly progressive distal sensorimotor neuropathy with the electrophysiological features of an **"intermediate"** neuropathy — i.e., motor nerve conduction velocities (NCV) that fall between the demyelinating (CMT1, <38 m/s) and purely axonal (CMT2, >38 m/s) ranges, or a mixed axonal-and-demyelinating picture. The disease is caused by loss-of-function variants in ***COX6A1***, a nuclear-encoded structural subunit of mitochondrial respiratory **complex IV (cytochrome *c* oxidase, COX)** (PMID: 25152455).

**Key identifiers.**
| Resource | Identifier |
|---|---|
| OMIM (phenotype) | **#616039** — Charcot-Marie-Tooth disease, recessive intermediate D (CMTRID) |
| OMIM (gene) | ***602072*** — COX6A1 |
| MONDO | **MONDO:0014467** (Charcot-Marie-Tooth disease recessive intermediate D) — *verified via EBI OLS4* |
| Orphanet | **ORPHA:435998** — *verified via MONDO xref* |
| DOID | **DOID:0110203** |
| GARD | **GARD:0017723** |
| UMLS | **C5569027** |
| MedGen | **1800450** (C5569027) |
| ICD-10 | **G60.0** (Hereditary motor and sensory neuropathy) |
| ICD-11 | **8C20** (Hereditary motor and sensory neuropathy) |
| MeSH | **D002607** (Charcot-Marie-Tooth Disease) |
| HGNC (gene) | **HGNC:2277** (COX6A1) |
| NCBI Gene | **1337** (COX6A1) |
| Ensembl | **ENSG00000111775** |
| UniProt | **P12074** (COX6A1_HUMAN) |

*MONDO definition (verified): "Any Charcot-Marie-Tooth disease in which the cause of the disease is a mutation in the COX6A1 gene."*

**Synonyms / alternative names.**
- CMTRID; CMT Recessive Intermediate type D
- Autosomal recessive intermediate Charcot-Marie-Tooth disease, COX6A1-related
- COX6A1-related axonal/mixed Charcot-Marie-Tooth disease
- Cytochrome c oxidase subunit VIa polypeptide 1-related neuropathy

**Source type.** Information is derived almost entirely from **aggregated, disease-level resources** (OMIM/Orphanet) and a small number of **individual case reports / small consanguineous-family studies** in the primary literature (PMID: 25152455; 41044399). No EHR-scale cohort exists for this specific subtype.

**HPO (disease-level suggestions):** HP:0007141 (Peripheral axonal neuropathy), HP:0003477 (Peripheral sensory neuropathy), HP:0003693 (Distal amyotrophy), HP:0009830 (Peripheral neuropathy).

---

## 2. Etiology

**Primary cause — genetic.** CMTRID is a **monogenic autosomal-recessive** disorder caused by **biallelic (homozygous or compound-heterozygous) pathogenic variants in *COX6A1***. The founding study mapped the locus to a 4.3 Mb region on **chromosome 12q24** (maximum multipoint LOD 4.23) in two consanguineous families and identified a homozygous 5-bp splice-region deletion **c.247-10_247-6delCACTC** in intron 2 of *COX6A1* (PMID: 25152455).

> *"a disease-specific 5 bp deletion (c.247-10_247-6delCACTC) in a splicing element (pyrimidine tract) of intron 2 adjacent to the third exon of cytochrome c oxidase subunit VIa polypeptide 1 (COX6A1), which is a component of mitochondrial respiratory complex IV"* — Tamiya et al., 2014 (PMID: 25152455)

**Risk factors.**
- **Genetic:** The only established risk factor is inheritance of two pathogenic *COX6A1* alleles. **Consanguinity** is a strong contributing factor — the originally described families were consanguineous (PMID: 25152455) — increasing the chance of homozygosity for a rare recessive allele.
- **Environmental / lifestyle:** No environmental risk factors are established as *causal*. However, given the mitochondrial (oxidative-phosphorylation) basis, **metabolic stressors — especially febrile illness — can precipitate acute decompensation** in severe cases; a child with a *COX6A1* stop-loss variant died after a febrile illness at age 3.5 y (PMID: 41044399). General CMT-relevant modifiers (potentially neurotoxic drugs such as vincristine, cisplatin; alcohol; vitamin B6 excess) are prudent to avoid but are not CMTRID-specific.
- **Age / sex / family history:** Autosomal recessive; both sexes affected equally; positive family history and/or consanguinity increase risk.

**Protective factors.** None specifically established. Heterozygous carriers are clinically unaffected (recessive inheritance). No protective modifier alleles have been reported.

**Gene–environment interactions.** The most plausible interaction is between the **complex IV deficiency genotype and metabolic/energetic demand** (fever, catabolic stress, exercise), where increased ATP demand or mitochondrial stress may unmask or worsen the phenotype (inferred from PMID: 41044399). This is not yet formally quantified.

---

## 3. Phenotypes

**Authoritative HPO clinical synopsis (HPO/Jax annotation network for OMIM:616039; verified iteration 3):**

| Phenotype | HPO term | Category |
|---|---|---|
| Peripheral neuropathy | **HP:0009830** | Nervous system |
| Distal sensory impairment | **HP:0002936** | Nervous system |
| **Onion bulb formation** (demyelination/remyelination hallmark) | **HP:0003400** | Nervous system |
| Hyporeflexia | **HP:0001265** | Nervous system |
| Areflexia | **HP:0001284** | Nervous system |
| Steppage gait (foot drop) | **HP:0003376** | Nervous system |
| Foot dorsiflexor weakness | **HP:0009027** | Limbs |
| Pes cavus | **HP:0001761** | Limbs |
| Childhood onset | **HP:0011463** | Clinical course |
| Slowly progressive | **HP:0003677** | Clinical course |
| Autosomal recessive inheritance | **HP:0000007** | Inheritance |

> The co-annotation of **onion-bulb formation** (a demyelinating/remyelinating feature) with axonal signs provides the pathological basis for the **"intermediate/mixed"** electrophysiological classification.

**Additional phenotype detail (from defining families and case reports; PMID: 25152455, 41044399):**

| Phenotype | Type | HPO suggestion | Onset | Severity / Course | Frequency (in reported cases) |
|---|---|---|---|---|---|
| Distal muscle weakness & atrophy (legs > arms) | Clinical sign | HP:0007373 / HP:0009027 | Childhood | Progressive | Typical / most |
| Distal sensory loss | Symptom/sign | HP:0002936 | Childhood | Progressive | Common |
| Reduced/absent deep-tendon reflexes | Clinical sign | HP:0001265 / HP:0001284 | Childhood | Stable/progressive | Common |
| Pes cavus / foot deformity | Physical manifestation | HP:0001761 | Childhood | Progressive | Common |
| Steppage/gait disturbance | Symptom | HP:0003376 | Childhood | Progressive | Typical |
| Intermediate/mixed motor NCV + onion bulbs | Lab/electrophysiology + pathology | HP:0003400 | — | — | Defining feature |
| Elevated blood/CSF lactate | Lab abnormality | HP:0002151 | Infancy (severe cases) | — | Severe variant (PMID:41044399) |
| Global developmental delay | Behavioral/developmental | HP:0001263 | Infancy | — | Severe variant only (PMID:41044399) |
| Neurogenic muscular atrophy | Pathology | HP:0003202 | — | Progressive | Model + patients |

**Phenotype characteristics.**
- **Age of onset:** Typically **childhood** for the classic neuropathy; **infantile** (severe multisystem) presentation with the stop-loss variant (PMID: 41044399).
- **Severity:** **Variable** — from a relatively "pure" intermediate CMT to a severe infantile mitochondrial encephalo-neuropathy with fatal metabolic decompensation.
- **Progression:** **Slowly progressive** in classic cases; **rapidly decompensating** in the severe infantile form.
- **Frequency:** Given <10 reported individuals, frequencies are qualitative, not percentages.

**Quality-of-life impact.** No CMTRID-specific QoL data. In CMT and related rare long-term neurological conditions, HRQL is substantially reduced (mean **EQ-5D index 0.2–0.44**), with frequent pain, anxiety/depression, and problems with mobility, self-care, and usual activities (PMID: 23001492).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***COX6A1*** (Cytochrome c Oxidase Subunit 6A1) — HGNC:2277, NCBI Gene 1337, OMIM *602072, Ensembl ENSG00000111775, chromosome **12q24.31**, 3 exons; encodes an 85-aa mature protein (UniProt P12074, 12-aa mitochondrial targeting presequence) — the **ubiquitous/"liver-type" isoform** of COX subunit VIa (the heart/muscle isoform is COX6A2) (PMID: 7687470; 20307258).

**Pathogenic variants (reported).**
| Variant (HGVS) | Type | Zygosity | Consequence | Reference |
|---|---|---|---|---|
| c.247-10_247-6delCACTC (intron 2) | Splice-region deletion (pyrimidine tract) | Homozygous | Aberrant splicing → reduced COX6A1 expression & COX activity | PMID: 25152455 |
| c.329A>T, p.(Ter110Leuext*41) | **Stop-loss** (missense of stop) | Homozygous | Protein +41 aa, markedly reduced protein level | PMID: 41044399 |

- **ACMG/AMP classification:** The reported variants are **pathogenic**, supported by segregation in consanguineous families, functional assays (reduced mRNA/protein/enzyme activity), and absence from population databases (PMID: 25152455, 41044399).
- **Variant types:** splice-region and stop-loss; both act via **loss of function**.
- **Allele frequency:** Reported variants are **absent from gnomAD/population databases** (PMID: 41044399), consistent with private/family-specific pathogenic alleles.
- **ClinVar landscape (queried iteration 4):** Of 50 COX6A1 ClinVar records, the vast majority are **VUS or likely-benign** missense/synonymous variants; the only "Pathogenic/Likely pathogenic" entries are large **12q24 contiguous-gene CNVs** (associated with intellectual disability), **not** COX6A1 point variants causing CMT. This confirms CMTRID alleles are private and documented chiefly in primary literature rather than variant repositories.
- **gnomAD constraint (queried iteration 4):** COX6A1 (ENSG00000111775) shows **pLI = 0.0023** and **LOEUF (oe_lof) = 0.875** (obs LoF 4 vs exp 4.57) — i.e., **heterozygous loss of function is tolerated** in the population, exactly as expected for a **recessive** disorder (carriers unaffected; two hits required).
- **Origin:** **Germline** (inherited recessive). No somatic role.
- **Functional consequence:** **Loss of function** — reduced COX6A1 protein → complex IV assembly/activity deficiency (PMID: 25152455, 20307258).

**Modifier genes.** None established. Mechanistically, **COX6A2** (heart/muscle isoform) can functionally substitute for COX6A1 in cell models (ectopic COX6A2 rescued holoenzyme and activity in COX6A1-knockdown cells; PMID: 20307258), suggesting isoform expression could theoretically modify tissue vulnerability — but this is not demonstrated in patients.

**Epigenetic information.** No CMTRID-specific epigenetic data. *COX6A1* transcription is regulated by mitochondrial-biogenesis factors (e.g., NRF-1) and tissue-specific elements (PMID: 7687470).

**Chromosomal abnormalities.** None; CMTRID is a single-gene point-variant/small-indel disorder, not a copy-number/structural syndrome. (Contrast with CMT1A, which is a 17p12/PMP22 duplication.)

**Gene ontology (molecular):** GO:0004129 (cytochrome-c oxidase activity, as complex), GO:0005751 (mitochondrial respiratory chain complex IV), GO:0009060 (aerobic respiration).

---

## 5. Environmental Information

- **Environmental factors:** No environmental toxins are causal. As a mitochondrial disorder, exposure to **mitochondrial/neurotoxic agents** (e.g., certain chemotherapeutics, aminoglycosides, alcohol) is theoretically deleterious and should be avoided, though not CMTRID-specific.
- **Lifestyle factors:** No established lifestyle causes. Maintaining fitness/physiotherapy is beneficial for CMT generally; avoiding metabolic stress is prudent given OXPHOS deficiency.
- **Infectious agents:** Not causal. **Febrile/infectious illness can trigger metabolic decompensation** in the severe infantile form (PMID: 41044399).

---

## 6. Mechanism / Pathophysiology

**Causal chain.** Biallelic *COX6A1* LoF variants → reduced COX6A1 protein → **impaired assembly and reduced activity of mitochondrial complex IV (cytochrome c oxidase)** → deficient oxidative phosphorylation / ATP production and altered redox state → energetic failure in metabolically demanding, long peripheral axons → **length-dependent axonal degeneration** (with secondary/mixed demyelinating features giving "intermediate" NCVs) → distal sensorimotor neuropathy and neurogenic muscle atrophy.

**Molecular pathways / cellular processes.**
- **Oxidative phosphorylation / electron transport chain** (complex IV is the terminal oxidase transferring electrons to O₂). Loss of COX6A1 reduces CcO activity, lowers the enzyme's O₂ affinity, decreases holoenzyme and dimer levels, and perturbs respiratory **supercomplex** assembly (PMID: 20307258).
- **Complex IV / supercomplex assembly** (COX6A1 is a late-assembling structural subunit) (PMID: 20307258; supercomplex context PMID: 27775717).
- Downstream: bioenergetic deficit, likely increased oxidative stress, and impaired axonal maintenance — the general theme of mitochondrial CMTs (cf. MFN2/CMT2A, GDAP1) in which axonal mitochondrial function/transport failure preferentially injures long peripheral nerves (PMID: 32733278, 20335458, 33582224).

**Protein dysfunction.** Loss-of-function/reduced abundance of a structural subunit → **failure of complex IV holoenzyme assembly** rather than a gain-of-function or aggregation mechanism (PMID: 25152455, 20307258, 41044399).

**Metabolic changes.** Reduced aerobic ATP synthesis; **lactic acidosis** in severe cases (elevated lactate; PMID: 41044399), reflecting a shift to anaerobic metabolism from complex IV deficiency.

**Immune system involvement.** None described (non-inflammatory, non-autoimmune).

**Tissue-damage mechanism.** Energy-deprivation-mediated **axonal (Wallerian-like) degeneration**, most severe distally in long nerves; likely oxidative stress contribution.

**Molecular profiling.** Functional (not omics) evidence: reduced *COX6A1* mRNA in patient leukocytes and reduced COX activity in patient lymphoblastoid lines (PMID: 25152455); reduced mutant protein by functional assay (PMID: 41044399). No transcriptomic/proteomic/metabolomic dataset specific to CMTRID is published.

**Upstream vs downstream.** *Upstream:* COX6A1 loss → complex IV deficiency (primary). *Downstream:* bioenergetic failure → axonal degeneration → muscle denervation/atrophy → weakness, sensory loss, deformity.

**Suggested ontology terms.** GO:0006119 (oxidative phosphorylation), GO:0033617 (mitochondrial cytochrome c oxidase assembly), GO:0009060 (aerobic respiration), GO:0034599 (cellular response to oxidative stress), GO:0031667 (response to nutrient levels). Cell types (CL): CL:0000101 (sensory neuron), CL:0000100 (motor neuron), CL:0002573 (Schwann cell).

---

## 7. Anatomical Structures Affected

- **Organ / system level (primary):** **Peripheral nervous system** — peripheral nerves (UBERON:0000010), especially long motor and sensory nerves of the limbs. Body system: nervous (peripheral).
- **Secondary:** Skeletal muscle (neurogenic atrophy; UBERON:0001134), skeleton/feet (pes cavus, deformity; UBERON:0002387 pes). In the severe infantile form, **CNS involvement** (developmental delay) and systemic metabolic derangement occur (PMID: 41044399).
- **Tissue/cell level:** **Peripheral axons** (motor and sensory neurons), with mixed involvement implicating **Schwann cells/myelin** — supported by **onion-bulb formation (HP:0003400)** in the HPO synopsis, a hallmark of demyelination/remyelination that explains the intermediate NCV. Cell Ontology: CL:0000100 (motor neuron), CL:0000101 (sensory neuron), CL:0002573 (Schwann cell).
- **Subcellular level:** **Mitochondrion** (GO:0005739) — specifically the **mitochondrial inner membrane** (GO:0005743) / **respiratory chain complex IV** (GO:0005751), with the protein localized to the mitochondrial inner-membrane face (UniProt P12074). Axonal mitochondria are the key affected compartment.
- **Localization / laterality:** Distal, **length-dependent** and **bilateral/symmetric** (legs affected earlier and more than arms), typical of CMT. UBERON:0002470 (pelvic limb), UBERON:0001021 (nerve).

---

## 8. Temporal Development

- **Onset:** Usually **childhood** for the classic intermediate neuropathy; **infantile/early-childhood** with a severe multisystem phenotype in the stop-loss case (developmental delay from infancy) (PMID: 25152455, 41044399). Pattern: **insidious/chronic** for the neuropathy; **acute decompensation** possible with intercurrent illness.
- **Progression:** **Slowly progressive** neuropathy in classic cases; **rapid decompensation and death** (age 3.5 y) reported in the severe infantile variant (PMID: 41044399). Course is **chronic and lifelong**.
- **Stages:** No formal staging exists; general CMT trajectory = early (subtle distal weakness, foot deformity) → intermediate (functional gait/hand impairment, orthotic need) → advanced (marked distal atrophy, disability).
- **Patterns:** Progressive, not relapsing-remitting; no spontaneous remission. **Critical windows:** intercurrent febrile illness is a period of vulnerability for metabolic crisis in severe cases (PMID: 41044399).

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic *COX6A1* variants) (PMID: 25152455).
- **Penetrance:** Appears **complete** in biallelic individuals reported to date (small numbers). **Expressivity is variable** (mild intermediate CMT to severe infantile mitochondrial disease).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** None established; reported alleles are private/family-specific and absent from population databases (PMID: 41044399).
- **Consanguinity:** **Important** — index families were consanguineous; homozygosity mapping was the discovery approach (PMID: 25152455).
- **Carrier frequency:** Unknown/very low; pathogenic *COX6A1* alleles are essentially absent from gnomAD.

**Epidemiology.**
- **Prevalence/incidence of CMTRID:** **Not established** — ultra-rare (<10 reported individuals). For context, all-CMT prevalence is ~1 in 2,500 (≈17–40/100,000; PMID: 16775366), but CMTRID is a vanishingly small fraction.
- **Populations / geography:** Reported cases include Japanese (original families; PMID: 25152455) and Chinese (PMID: 41044399) individuals; no ethnic predilection can be inferred from such small numbers. Recessive intermediate CMT overall is enriched in consanguineous populations.
- **Sex ratio:** ~1:1 (autosomal recessive).

---

## 10. Diagnostics

**Clinical / electrophysiology.**
- **Nerve conduction studies (NCS)/EMG:** cornerstone — reveal **intermediate motor NCV** (or mixed axonal + demyelinating) with reduced amplitudes; EMG shows chronic neurogenic changes/denervation (PMID: 25152455; classification framework PMID: 16775366, 16775364).
- **Laboratory:** **Elevated lactate** (blood/CSF) supports the mitochondrial/complex IV defect, particularly in severe cases (PMID: 41044399). **Cytochrome c oxidase (COX) activity assay** in accessible tissue (lymphoblasts/fibroblasts/muscle) is reduced (PMID: 25152455).
- **Nerve/muscle biopsy (not routinely required):** neurogenic muscular atrophy; mixed axonal/demyelinating nerve pathology.

**Genetic testing (definitive).**
- **Approach:** Because CMTRID is clinically indistinguishable from other intermediate/axonal CMTs, diagnosis rests on **molecular genetics**. Recommended: **NGS gene panel for CMT/inherited neuropathy** (including *COX6A1*), or **whole-exome/whole-genome sequencing** — the latter identified the founding variant (PMID: 25152455). *COX6A1* is included in AR-CMT gene lists (PMID: 26556829 lists "CMTRID/COX6A1").
- **Single-gene / targeted testing:** appropriate for at-risk relatives once a familial variant is known (cascade testing).
- **CMA/karyotype/FISH/mtDNA/repeat-expansion testing:** generally **not applicable** (point/indel nuclear-gene disorder; *COX6A1* is nuclear, not mtDNA).
- **Functional confirmation:** reduced *COX6A1* mRNA/protein and COX enzyme activity support pathogenicity of novel variants (PMID: 25152455, 41044399).

**Differential diagnosis.** Other intermediate/recessive CMTs — e.g., CMTRIA (*GDAP1*), CMTRIB (*KARS1*), CMTRIC (*PLEKHG5*), dominant-intermediate CMT (*DNM2*, *YARS1*, *INF2*), CMTX (*GJB1*), CMT2 subtypes, and mitochondrial neuropathies (*MFN2*/CMT2A). Distinguishing features: **elevated lactate and reduced COX activity** point toward *COX6A1*; genetics is definitive (PMID: 16775364, 16541790).

**Screening.** No population/newborn screening exists for this ultra-rare disorder. **Cascade carrier testing** of relatives and **prenatal/preimplantation testing** are options once a familial variant is identified.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** In classic CMT, life expectancy is generally near-normal; **however, the severe infantile *COX6A1* form can be fatal** — one child died at 3.5 y after febrile decompensation (PMID: 41044399). No cohort mortality figures exist for CMTRID.
- **Morbidity/function:** Progressive distal weakness, sensory loss, foot deformity, gait impairment, and hand dysfunction cause **chronic disability**; substantial reduction in quality of life is expected (EQ-5D 0.2–0.44 in comparable rare neurological conditions; PMID: 23001492).
- **Complications:** Foot ulcers/injuries from sensory loss, joint deformity, falls; in severe cases, metabolic crisis with intercurrent illness (PMID: 41044399).
- **Recovery:** No spontaneous recovery; management is supportive and does not reverse the neuropathy.
- **Prognostic factors:** **Variant severity/genotype** (stop-loss with residual severe LoF and multisystem features vs milder splice variant), age of onset, presence of lactic acidosis/CNS involvement, and metabolic stability appear prognostically relevant (inferred from PMID: 25152455 vs 41044399).

---

## 12. Treatment

**No disease-modifying/approved therapy exists for CMTRID.** Management is **symptomatic and supportive**, mirroring general CMT care (PMID: 40014417).

- **Pharmacotherapy:** No targeted drug. Symptomatic management of **neuropathic pain** (e.g., gabapentinoids, duloxetine, tricyclics — NCIT clinical-intervention terms apply generically). **Avoid neurotoxic drugs** (vincristine and other CMT-hazardous agents).
- **Mitochondrial/supportive measures (rational, not proven for CMTRID):** aggressive management of intercurrent illness/fever, avoidance of catabolic/metabolic stress; "mitochondrial cocktail" supplements (e.g., riboflavin, coenzyme Q10, L-carnitine) are sometimes used empirically in complex IV deficiency but lack CMTRID-specific evidence.
- **Advanced therapeutics (investigational for CMT generally, none CMTRID-specific):** gene therapy/gene silencing, HDAC6 inhibitors, and metabolic agents are in trials for other CMT subtypes; govorestat (CMT-SORD) may become the first approved CMT drug (PMID: 40014417). None target *COX6A1*.
- **Clinical-trial status (verified iteration 5):** A ClinicalTrials.gov API query returned **0 studies** mentioning *COX6A1*; no interventional or observational trial specifically addresses CMTRID. Patients may be eligible for general CMT natural-history/registry studies.
- **Surgical/interventional:** orthopedic correction of foot deformities (e.g., osteotomy, tendon transfer) as needed.
- **Supportive/rehabilitative (mainstay):** **physical therapy, occupational therapy, ankle-foot orthoses (AFOs), assistive devices, foot care, exercise**, and multidisciplinary support improve function and QoL (PMID: 40014417).
- **Treatment outcomes:** Supportive care improves function/QoL but does not alter the underlying neurodegeneration.

**Suggested NCIT terms:** Physical Therapy (C15327), Occupational Therapy (C15243), Orthotic Device (C50077), Supportive Care (C15417), Genetic Counseling (C15391).

---

## 13. Prevention

- **Primary prevention:** No way to prevent occurrence in a conceived biallelic individual; **prevention is reproductive/genetic** — carrier identification, genetic counseling, and reproductive options (prenatal diagnosis, PGT) for at-risk couples (especially consanguineous families) (rationale: recessive inheritance, PMID: 25152455).
- **Secondary prevention:** Early diagnosis (NCS + genetics) enables timely orthotics, physiotherapy, and surveillance; in severe/infantile cases, **early recognition and aggressive management of febrile illness** to prevent metabolic decompensation (PMID: 41044399).
- **Tertiary prevention:** Prevent complications — foot-care programs to avert ulcers, fall-prevention, contracture prevention via therapy, deformity correction.
- **Immunization/public health/prophylaxis:** No vaccine or specific prophylaxis. Standard immunizations to reduce febrile illnesses may be prudent in severe cases (supportive rationale).
- **Counseling:** **Genetic counseling** is central — recurrence risk 25% for siblings of an affected child of carrier parents; carrier testing of relatives.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI Taxon **9606**). Experimental model: *Mus musculus* (NCBI Taxon **10090**).
- **Orthologous genes:** Mouse *Cox6a1* (NCBI Gene **12861**, **MGI:103099**; verified via mygene.info); *COX6A1* is highly conserved across mammals (bovine gene characterized in PMID: 7687470).
- **Natural disease in other species:** **No naturally occurring COX6A1-related CMT is documented in companion animals or wildlife** (OMIA search yields no established entry for this specific gene/phenotype as of this report). Inherited neuropathies do occur in dogs, but a *COX6A1* etiology is not established.
- **Comparative biology:** Complex IV/OXPHOS machinery is evolutionarily conserved from yeast to mammals, so the bioenergetic mechanism is broadly translatable; the *Cox6a1*-null mouse reproduces reduced COX activity and neurogenic muscular atrophy (PMID: 25152455).
- **Zoonotic potential:** None (non-infectious genetic disease).

---

## 15. Model Organisms

- **Primary model — *Cox6a1*-null mouse (mammalian, knockout):** shows **significantly reduced COX activity and neurogenic muscular atrophy leading to difficulty walking**, recapitulating the core neuromuscular phenotype and confirming causality (PMID: 25152455).
  > *"Cox6a1-null mice showed significantly reduced COX activity and neurogenic muscular atrophy leading to a difficulty in walking"* (PMID: 25152455).
- **Cellular / in vitro models:**
  - Patient-derived **EBV-transformed lymphoblastoid cell lines** (reduced COX activity) and **peripheral leukocytes** (reduced *COX6A1* expression) (PMID: 25152455).
  - **HEK-293 RNAi knockdown** of *COX6A1*: reduced CcO activity, decreased holoenzyme/dimer, accumulation of assembly subcomplexes, altered supercomplexes; rescued by COX6A2 (PMID: 20307258).
  - Transfected cell lines demonstrating reduced mutant protein for novel variants (PMID: 41044399).
- **Model characteristics:** The knockout mouse **recapitulates** COX deficiency and neurogenic atrophy/gait impairment. **Limitations:** murine models may not fully capture the human "intermediate" NCV pattern or the severe multisystem/lactic-acidosis infantile phenotype; small patient numbers limit genotype-phenotype modeling.
- **Applications:** Study of complex IV assembly, axonal bioenergetics, and preclinical testing of mitochondrial-supportive or gene-based therapies.
- **Resources:** MGI (mouse *Cox6a1*), IMPC/KOMP for engineered alleles, Cellosaurus for patient lines.

---

## Supported and Refuted Hypotheses

**Supported:**
1. **CMTRID is caused by biallelic loss-of-function *COX6A1* variants** (splice-region deletion; stop-loss) — supported by linkage (LOD 4.23), WGS/WES, segregation, functional assays, and a knockout mouse (PMID: 25152455, 41044399).
2. **The mechanism is mitochondrial complex IV (cytochrome c oxidase) deficiency** impairing OXPHOS and causing length-dependent axonal degeneration (PMID: 25152455, 20307258).
3. **The phenotypic spectrum is variable**, extending from intermediate/axonal CMT to a severe infantile mitochondrial disease with developmental delay and lactic acidosis (PMID: 41044399).

**Refuted / not supported:**
- CMTRID is **not** a demyelinating-only or dominant disorder; **not** a chromosomal/CNV syndrome; **not** infectious/autoimmune. No founder effect or common population allele underlies it.

## Limitations and Future Directions

- **Very small evidence base** (<10 individuals) → epidemiology, penetrance, natural history, and prognosis are poorly quantified.
- **No omics datasets** (transcriptomic/proteomic/metabolomic) specific to CMTRID; mechanistic detail beyond complex IV assembly is inferred.
- **No targeted therapy or clinical trials** for *COX6A1* CMT.
- **Future work:** patient registries; iPSC-derived motor/sensory neuron models; systematic genotype-phenotype correlation; testing of mitochondrial-support and gene-based therapies; clarification of why COX6A2 isoform substitution does not fully protect peripheral nerve in patients.

---

### Key References
- **PMID 25152455** — Tamiya et al. 2014. *A mutation of COX6A1 causes a recessive axonal or mixed form of Charcot-Marie-Tooth disease.* (Founding gene-discovery study + Cox6a1-null mouse.)
- **PMID 41044399** — Cai et al. 2026. *A novel homozygous COX6A1 variant causes axonal CMT, developmental delays and mitochondrial dysfunction.* (First stop-loss variant; phenotype expansion.)
- **PMID 20307258** — Fornuskova et al. 2010. *Assembly and function of human nuclear-encoded COX subunits 4, 5a, 6a, 7a, 7b.* (COX6A1 in complex IV assembly; COX6A2 rescue.)
- **PMID 7687470** — Smith & Lomax 1993. *Structural organization of the COX6A gene.* (Gene structure/regulation.)
- **PMID 26556829** — Montecchiani et al. 2016. (Lists CMTRID/COX6A1 among AR-CMT genes.)
- **PMID 16775366 / 16775364** — Houlden & Reilly 2006; Pareyson et al. 2006. (CMT classification, intermediate CMT concept, prevalence.)
- **PMID 40014417** — De Grado et al. 2025. *CMT clinical developments and management — 2025.* (Management/therapeutic landscape.)
- **PMID 23001492** — Calvert et al. 2013. (QoL/EQ-5D in CMT and rare neurological conditions.)
- **PMID 27775717** — Cogliati et al. 2016. (Complex III–IV supercomplex assembly context.)


## Artifacts

- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Recessive_Intermediate_D-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Recessive_Intermediate_D-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:23001492` (4 mentions) - Health-related quality of life and supportive care in patients with rare long-term neurological conditions.
  - shared terms: disease

Weighed against this report's own most characteristic terms: `cox6a1`, `cmt`, `variant`, `mitochondrial`, `cmtrid`, `severe`, `complex`, `intermediate`, `recessive`, `metabolic`, `infantile`, `axonal`, `gene`, `neuropathy`, `disease`, `primary`, `peripheral`, `cox`, `genetic`, `phenotype`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 32 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0110203` (1 mention) - the report calls it "DOID"; DOID calls it **Charcot-Marie-Tooth disease recessive intermediate D**
- `HP:0002936` (2 mentions) - the report calls it "Distal sensory impairment", "Symptom/sign"; HP calls it **Distal sensory impairment**
- `HP:0003400` (3 mentions) - the report calls it "Onion bulb formation** (demyelination/remyelination hallmark)", "Lab/electrophysiology + pathology"; HP calls it **Basal lamina onion bulb formation**
- `HP:0003376` (2 mentions) - the report calls it "Steppage gait (foot drop)", "Symptom"; HP calls it **Steppage gait**
- `HP:0001761` (2 mentions) - the report calls it "Pes cavus", "Physical manifestation"; HP calls it **Pes cavus**
- `HP:0002151` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased circulating lactate concentration**
- `HP:0003202` (1 mention) - the report calls it "Pathology"; HP calls it **Skeletal muscle atrophy**
- `UBERON:0002470` (1 mention) - the report calls it "pelvic limb"; UBERON calls it **autopod region**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005751` (obsolete mitochondrial respiratory chain complex IV) (2 mentions) - replaced by `GO:0045277`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007141` (1 mention) - the report calls it "Peripheral axonal neuropathy"; HP calls it **Sensorimotor neuropathy**, and lists "Sensorimotor peripheral neuropathy" among its other names
- `HP:0003477` (1 mention) - the report calls it "Peripheral sensory neuropathy"; HP calls it **Peripheral axonal neuropathy**
- `HP:0001263` (1 mention) - the report calls it "Behavioral/developmental"; HP calls it **Global developmental delay**, and lists "Retarded development" among its other names
- `GO:0004129` (1 mention) - the report calls it "cytochrome-c oxidase activity, as complex"; GO calls it **cytochrome-c oxidase activity**
- `GO:0005751` (2 mentions) - the report calls it "mitochondrial respiratory chain complex IV", "respiratory chain complex IV"; GO calls it **obsolete mitochondrial respiratory chain complex IV**
- `GO:0033617` (1 mention) - the report calls it "mitochondrial cytochrome c oxidase assembly"; GO calls it **mitochondrial respiratory chain complex IV assembly**, and lists "mitochondrial cytochrome c oxidase assembly" among its other names
- `GO:0005739` (1 mention) - the report calls it "Mitochondrion", "Subcellular level:** **Mitochondrion"; GO calls it **mitochondrion**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002936` - called "Distal sensory impairment", "Symptom/sign"
- `HP:0003400` - called "Onion bulb formation** (demyelination/remyelination hallmark)", "Lab/electrophysiology + pathology"
- `HP:0003376` - called "Steppage gait (foot drop)", "Symptom"
- `HP:0001761` - called "Pes cavus", "Physical manifestation"
- `GO:0005751` - called "mitochondrial respiratory chain complex IV", "respiratory chain complex IV"
- `GO:0005739` - called "Mitochondrion", "Subcellular level:** **Mitochondrion"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `GARD`, `OMIM`, `MGI`.