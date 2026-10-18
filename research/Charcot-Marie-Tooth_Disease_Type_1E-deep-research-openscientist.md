---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T13:02:56.748468'
end_time: '2026-09-22T13:16:46.299244'
duration_seconds: 829.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Type 1E
  mondo_id: MONDO:0007311
  category: Disease
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 16
  off_topic: 2
  off_topic_references:
  - PMID:40270660
  - PMID:19588347
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 0
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0002936
    reported_labels:
    - Symptom/sign
    ontology_label: Distal sensory impairment
  - term_id: HP:0001761
    reported_labels:
    - Physical manifestation
    ontology_label: Pes cavus
  - term_id: HP:0001765
    reported_labels:
    - Physical manifestation
    ontology_label: Hammertoe
  - term_id: HP:0001315
    reported_labels:
    - Clinical sign
    ontology_label: Diminished deep tendon reflex
  - term_id: HP:0009830
    reported_labels:
    - Clinical sign
    ontology_label: Peripheral neuropathy
  - term_id: HP:0000407
    reported_labels:
    - Sign / lab (audiometry)
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0003431
    reported_labels:
    - Lab / electrophysiology
    ontology_label: Decreased motor nerve conduction velocity
  - term_id: HP:0002093
    reported_labels:
    - Sign
    ontology_label: Respiratory insufficiency
  - term_id: HP:0002015
    reported_labels:
    - Symptom
    ontology_label: Dysphagia
  - term_id: HP:0001268
    reported_labels:
    - Sign
    ontology_label: Mental deterioration
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Charcot-Marie-Tooth_Disease_Type_1E-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Charcot-Marie-Tooth_Disease_Type_1E-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Type 1E
- **MONDO ID:** MONDO:0007311 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Type 1E** covering all of the
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

# Charcot-Marie-Tooth Disease Type 1E (CMT1E): Comprehensive Disease Characterization Report

**Target Disease:** Charcot-Marie-Tooth Disease Type 1E
**MONDO ID:** MONDO:0007311 | **OMIM:** #118300 | **Gene:** *PMP22* (HGNC:9118, 17p12)
**Category:** Rare inherited demyelinating peripheral neuropathy

---

## Summary

Charcot-Marie-Tooth disease type 1E (CMT1E) is a rare, autosomal dominant demyelinating hereditary motor and sensory neuropathy caused by coding **point mutations and small insertions/deletions (indels) in the *PMP22* gene** on chromosome 17p12. It is molecularly distinct from its two more common allelic disorders that arise from copy-number changes at the same locus: **CMT1A** (1.4-Mb *PMP22* duplication) and **hereditary neuropathy with liability to pressure palsies / HNPP** (*PMP22* deletion). Clinically, CMT1E is frequently **more severe than CMT1A** and is distinguished by a high frequency of **sensorineural hearing loss** (>40% of patients in a large Korean cohort), with a phenotypic spectrum that extends into the severe, early-onset Dejerine-Sottas syndrome (DSS) range. Point mutations in *PMP22* account for **less than 5% of all CMT1 cases**, making CMT1E a genuinely rare subtype within an already uncommon disease group (overall CMT prevalence ~1 in 2,500).

Mechanistically, CMT1E is a **protein-misfolding / toxic gain-of-function (and dominant-negative) disorder**. Most pathogenic substitutions fall within the conserved transmembrane domains of the tetraspan membrane protein PMP22. Mutant PMP22 misfolds, fails to traffic to the plasma membrane, and is **retained in the endoplasmic reticulum (ER) and Golgi apparatus**, where it forms **aggresome-like structures** surrounded by molecular chaperones and lysosomes. These aggregates are cleared by **autophagy**, and their accumulation drives **Schwann-cell proteostatic stress, apoptosis, and mis-trafficking of cholesterol** (retained with mutant PMP22 in the Golgi, reducing plasma-membrane cholesterol needed for myelin). The downstream consequence is **dysmyelination/demyelination of peripheral nerves** with secondary length-dependent axonal loss — producing the classic distal, symmetric, progressive sensorimotor phenotype.

There is **no approved disease-modifying therapy** for CMT1E (or any CMT). Management is entirely supportive — rehabilitation, orthotics, corrective surgery, symptom control, and genetic counseling. Because CMT1E is a point-mutation/proteostasis disease, therapies developed for the *gene-dosage* disorder CMT1A (e.g., ascorbic acid, *PMP22* silencers) are not directly applicable; instead, **proteostasis-directed strategies** — exemplified preclinically by curcumin, which partially rescues the Trembler-J mouse — are the mechanism-matched experimental leads. The faithful natural mouse models **Trembler (Tr)** and **Trembler-J (TrJ)** carry *Pmp22* point mutations (TrJ carries the human CMT1E Leu16Pro substitution) and recapitulate the dysmyelinating pathology, providing a strong platform for mechanistic and therapeutic study.

---

## Key Findings

### Finding 1 — CMT1E is defined by *PMP22* point mutations and is more severe than CMT1A, often with deafness

CMT1E is caused by coding **point mutations or small indels in *PMP22***, in contrast to CMT1A (whole-gene duplication) and HNPP (whole-gene deletion). In a Korean cohort of 850 CMT families that were negative for the 17p12 duplication, whole-exome and targeted sequencing identified **14 pathogenic/likely pathogenic PMP22 point mutations across 21 families**. Most mutations localized to the **conserved transmembrane domains** of the protein. Critically, **>40% of CMT1E patients showed hearing loss**, and both the physical and electrophysiological severity of CMT1E exceeded that of CMT1A, more closely resembling MPZ-related CMT1B ([PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/)). As the authors state: *"point mutations or small insertions and deletions (indels) usually cause CMT type 1E (CMT1E) or HNPP"* and *"more than 40% of the CMT1E patients showed hearing loss. Physical and electrophysiological symptoms of the CMT1E patients were more severely damaged than those of CMT1A."*

The rarity of this mechanism is quantified: *"Point mutations in the Peripheral Myelin Protein 22 (PMP22) gene comprise less than 5% of the Charcot-Marie-Tooth (CMT) type 1 cases"* ([PMID: 34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/)).

**Synonyms / alternative names:** CMT1E; Charcot-Marie-Tooth neuropathy type 1E; CMT1 with deafness; PMP22-related CMT1 (point mutation type); demyelinating CMT1E. The severe end of the *PMP22* point-mutation spectrum overlaps clinically with **Dejerine-Sottas syndrome (DSS)** and congenital hypomyelinating neuropathy. Information is derived from aggregated disease-level resources (OMIM, Orphanet) combined with clinical cohort and family studies rather than EHR-derived individual data.

### Finding 2 — Mechanism: mutant PMP22 misfolds, is retained in the ER/Golgi, forms aggresomes cleared by autophagy, and disrupts Schwann-cell cholesterol trafficking

The core pathophysiology is a **proteostatic / trafficking defect**. In Trembler-J (TrJ, Leu16Pro PMP22) mouse nerves, PMP22 has an **extended half-life** and forms **aggresome-like structures surrounded by molecular chaperones and lysosomes**; aggresome clearance is **enhanced by autophagy activation and blocked by autophagy inhibition** ([PMID: 14627652](https://pubmed.ncbi.nlm.nih.gov/14627652/)): *"PMP22 has an extended half-life and forms aggresome-like structures that are surrounded by molecular chaperones and lysosomes"* via *"a mechanism that is enhanced when autophagy is activated and is primarily prevented when autophagy is inhibited."*

The trafficking lesion is specific to the transmembrane domains: *"disease-related missense mutations within transmembrane domains of PMP22 disturb intracellular protein trafficking leading to accumulation of the mutant protein in the endoplasmic reticulum/Golgi compartment"* ([PMID: 10625337](https://pubmed.ncbi.nlm.nih.gov/10625337/)).

A key downstream consequence is disrupted lipid handling: in TrJ Schwann cells, **cholesterol is retained with TrJ-PMP22 in the Golgi**, with a corresponding reduction in plasma-membrane cholesterol, and cholesterol supplementation improved myelination in *PMP22*-deficient DRG explants ([PMID: 32511821](https://pubmed.ncbi.nlm.nih.gov/32511821/)): *"cholesterol was retained with TrJ-PMP22 in the Golgi, alongside a corresponding reduction in its plasma membrane level."* Because cholesterol is an essential structural lipid of compact myelin, its sequestration provides a direct biochemical link between the misfolded protein and the failure of myelination.

### Finding 3 — Epidemiology: CMT is the commonest inherited neuropathy (~1/2,500); CMT1E is a rare *PMP22*-point-mutation subtype

Overall CMT population prevalence is **~1 in 2,500** ([PMID: 27584852](https://pubmed.ncbi.nlm.nih.gov/27584852/); [PMID: 38784904](https://pubmed.ncbi.nlm.nih.gov/38784904/)): *"Charcot-Marie-Tooth disease (CMT) is one of the commonest inherited neuromuscular diseases with a population prevalence of 1 in 2500."* Within CMT, demyelinating forms dominate. In the Italian National CMT Registry (n=1,012 registered; 711 genetically diagnosed), *"Demyelinating CMT (65.3%) was more common than axonal CMT2 (24.6%) and intermediate CMT (9.0%). The PMP22 duplication was the most frequent mutation (45.2%)"* ([PMID: 37170966](https://pubmed.ncbi.nlm.nih.gov/37170966/)). The same registry ranked CMT1E among the **most disabling subtypes**: *"CMT4A was the most disabling type, followed by CMT4C and CMT1E."*

CMT1E's rarity is reinforced by cohort data: point mutations comprise <5% of CMT1 ([PMID: 34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/)), and in some populations (e.g., a Chinese Han cohort of 77 CMT1 families) **no point mutations were detected** among duplication/deletion-negative probands ([PMID: 25522693](https://pubmed.ncbi.nlm.nih.gov/25522693/)).

| Disorder | *PMP22* lesion | Frequency in CMT1 | Relative severity |
|---|---|---|---|
| **CMT1A** | 1.4-Mb duplication (gene dosage ↑) | ~45% (most common) | Classic, typically milder |
| **CMT1E** | Point mutation / small indel | <5% | More severe; often with deafness |
| **HNPP** | Deletion (gene dosage ↓) | — | Episodic pressure palsies |

### Finding 4 — Trembler and Trembler-J mice are faithful natural point-mutation models; the human Trembler mutation causes Dejerine-Sottas with deafness

The Trembler-J mouse is a **natural model carrying a genuine human CMT1E mutation**: *"Trembler J (TrJ) mice carry the same Leu16Pro amino acid substitution in the PMP22 protein that is present in families diagnosed with CMT1E"* ([PMID: 42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/)). TrJ mice display demyelination, aggresome formation, extracellular-matrix remodeling with MMP-2/-9-expressing macrophage infiltration ([PMID: 12421361](https://pubmed.ncbi.nlm.nih.gov/12421361/)), and respiratory/phrenic-nerve myelin defects with axonal atrophy (p<0.0001) plus diaphragm remodeling ([PMID: 42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/)).

Comparative profiling shows that point mutations act through a **distinct mechanism from gene-dosage changes**: across *Pmp22*-null, *Pmp22*-overexpressing, and Trembler mice, *"the three Pmp22 mutants exhibited distinct profiles of gene expression, suggesting different disease mechanisms"* ([PMID: 15755691](https://pubmed.ncbi.nlm.nih.gov/15755691/)). This is a central caveat for therapy translation (see Finding 7).

In humans, the classic **Trembler (Gly150Asp)** substitution produces severe disease: *"We report two cases of DSS [Dejerine-Sottas syndrome] in a mother and son with the Trembler mutation, with associated findings of hearing loss and cognitive impairment"* ([PMID: 35974257](https://pubmed.ncbi.nlm.nih.gov/35974257/)), underscoring that *PMP22* point mutations can drive the severe end of the demyelinating spectrum.

### Finding 5 — No disease-modifying therapy exists; management is supportive; curcumin rescues the Trembler-J phenotype preclinically

*"Disease-modifying therapies are not yet available for any form of CMT. Management includes rehabilitative approaches such as muscle strength training and orthotic devices, surgical interventions, symptom relief and anticipatory monitoring of associated complications"* ([PMID: 41571707](https://pubmed.ncbi.nlm.nih.gov/41571707/)).

The mechanism-matched preclinical lead is **curcumin**, which targets the ER-retention/aggregation-induced apoptosis specific to mutant PMP22: *"oral administration of curcumin partially mitigates the severe neuropathy phenotype of the Trembler-J mouse model in a dose-dependent manner. Administration of curcumin significantly decreases the percentage of apoptotic Schwann cells and results in increased number and size of myelinated axons"* ([PMID: 17701891](https://pubmed.ncbi.nlm.nih.gov/17701891/)). Emerging strategies under investigation for the broader CMT field include *PMP22* silencers (for CMT1A), HDAC6 inhibitors, and unfolded-protein-response modulation ([PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)).

### Finding 6 — Clinical picture and diagnosis: length-dependent progressive sensorimotor demyelinating neuropathy; NCS + genetic testing

*"All forms of CMT result in length-dependent, progressive axonal loss that correlates with clinical impairments such as distal upper and lower limb weakness, musculoskeletal deformity, absent deep tendon reflexes and distal sensory deficits"* ([PMID: 41571707](https://pubmed.ncbi.nlm.nih.gov/41571707/)). Characteristic features include **pes cavus, hammertoes, foot drop, distal muscle atrophy, and reduced quality of life** across physical, emotional, and social domains (physical being most disabling).

Diagnosis requires *"a detailed family history, comprehensive clinical evaluation, nerve conduction studies, and relevant genetic testing"* ([PMID: 42563944](https://pubmed.ncbi.nlm.nih.gov/42563944/)). Demyelinating CMT1 shows **uniformly slowed motor nerve conduction velocity (typically <38 m/s)**. CMT1E is confirmed by identifying a *PMP22* point mutation/indel **after the *PMP22* duplication has been excluded** — usually via MLPA (to exclude duplication/deletion) followed by Sanger sequencing or NGS gene panels / WES ([PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/); [PMID: 32506583](https://pubmed.ncbi.nlm.nih.gov/32506583/)). Pediatric CMT prevalence estimates range from **9.7 to 82 per 100,000** ([PMID: 42563944](https://pubmed.ncbi.nlm.nih.gov/42563944/)). CMT can also involve smooth muscle, causing diaphragmatic and gastrointestinal (esophageal) dysmotility ([PMID: 40270660](https://pubmed.ncbi.nlm.nih.gov/40270660/)).

### Finding 7 — Genetics: autosomal dominant with frequent de novo mutations, mutational hotspots, and markedly variable expressivity

CMT1E follows **autosomal dominant** inheritance. In the Korean cohort, *"High frequencies of de novo mutations were observed, and the mutation sites of c.68C>G and c.215C>T were suggested as the mutational hotspots"* ([PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/)). Most mutations lie in conserved transmembrane domains and produce a **bimodal early-onset-severe / late-onset-mild** phenotype.

Expressivity is highly variable, even within a single family: a Portuguese family carrying **p.Trp28Cys** ranged *"from asymptomatic to mild complaints of distal limb numbness and gait difficulties, with the age of onset of symptoms ranging from mid-twenties to late-sixties"* and without disability or hearing loss ([PMID: 34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/)) — in stark contrast to the severe DSS-with-deafness produced by the Trembler mutation ([PMID: 35974257](https://pubmed.ncbi.nlm.nih.gov/35974257/)). This demonstrates that the specific variant, and its position within the protein, is a major determinant of severity.

Importantly, **dosage-model therapies do not translate to point-mutation disease**: ascorbic acid, which benefited CMT1A transgenic mice, *"in three 1-year trials... had no benefit in human beings"* ([PMID: 21393063](https://pubmed.ncbi.nlm.nih.gov/21393063/)), and high-quality evidence confirms no meaningful benefit in CMT1A ([PMID: 26662471](https://pubmed.ncbi.nlm.nih.gov/26662471/)). This negative result cautions strongly against extrapolating CMT1A-directed therapies to CMT1E.

### Finding 8 — Anatomical/cellular targeting: Schwann-cell-autonomous demyelination of peripheral nerves, ER/Golgi as the subcellular site

The primary affected cell is the **myelinating Schwann cell (CL:0002573)**; the structural target is **compact PNS myelin (GO:0043209)**, with mutant PMP22 pathology localized to the **endoplasmic reticulum (GO:0005783)** and **Golgi (GO:0005794)** and cleared via **lysosomes/autophagosomes** ([PMID: 14627652](https://pubmed.ncbi.nlm.nih.gov/14627652/); [PMID: 10625337](https://pubmed.ncbi.nlm.nih.gov/10625337/); [PMID: 32511821](https://pubmed.ncbi.nlm.nih.gov/32511821/)). Affected anatomy is the **peripheral nervous system (UBERON:0000044)** — including the **sciatic (UBERON:0001322)** and **phrenic (UBERON:0002385)** nerves — in a **bilateral, symmetric, length-dependent** distribution, with secondary axonal loss, musculoskeletal deformity, auditory (sensorineural hearing loss) involvement, and uncommon respiratory/GI smooth-muscle involvement ([PMID: 41571707](https://pubmed.ncbi.nlm.nih.gov/41571707/); [PMID: 42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/); [PMID: 40270660](https://pubmed.ncbi.nlm.nih.gov/40270660/)). PMP22 additionally **modulates store-operated calcium channel activity**, implicating altered Schwann-cell Ca²⁺ handling in the mechanism ([PMID: 31213528](https://pubmed.ncbi.nlm.nih.gov/31213528/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **germline (or frequently de novo) heterozygous point mutation / small indel in *PMP22*** (17p12), typically within a conserved transmembrane domain (hotspots c.68C>G, c.215C>T), **leads to** production of a misfolded PMP22 protein. *(demonstrated — PMID: 35886002)*
2. Misfolded PMP22 **fails to traffic** to the Schwann-cell plasma membrane and **is retained in the ER and Golgi** apparatus. *(demonstrated — PMID: 10625337)*
3. ER/Golgi-retained mutant PMP22 has an **extended half-life** and **aggregates into aggresome-like structures** surrounded by chaperones and lysosomes. *(demonstrated in model — PMID: 14627652)*
4. Aggresomes are **cleared by autophagy**; when this proteostatic capacity is overwhelmed, **Schwann-cell stress accumulates**. *(demonstrated in model — PMID: 14627652)*
5. In parallel (branch), mutant PMP22 **sequesters cholesterol in the Golgi**, **reducing plasma-membrane cholesterol** required for compact myelin assembly. *(demonstrated in model — PMID: 32511821)*
6. Proteostatic stress and lipid mis-trafficking **result in Schwann-cell apoptosis** and impaired myelination. *(demonstrated in model; apoptosis reversible by curcumin — PMID: 17701891)*
7. Additional contributing branch: altered PMP22-dependent **store-operated Ca²⁺ handling** and **MMP-2/-9-driven extracellular-matrix remodeling** (macrophage-mediated) **contribute to** nerve pathology. *(inferred / partly demonstrated — PMID: 31213528, PMID: 12421361)*
8. Schwann-cell dysfunction **causes dysmyelination/demyelination** of peripheral nerves (compact myelin, GO:0043209). *(demonstrated)*
9. Demyelination **leads to** uniformly slowed nerve conduction and **secondary, length-dependent axonal degeneration**. *(demonstrated — PMID: 41571707)*
10. Axonal loss **manifests clinically** as distal, symmetric, progressive weakness and sensory loss, pes cavus/hammertoes, areflexia, foot drop — and, in many CMT1E patients, **sensorineural hearing loss** (a distinguishing feature). *(demonstrated — PMID: 35886002, PMID: 41571707)*

```
 PMP22 point mutation (TM domain)
            │  leads to
            ▼
   Misfolded PMP22 protein
            │  retained in
            ▼
      ER / Golgi ──────────────┐
        │  aggregates          │ sequesters
        ▼                      ▼
  Aggresomes            Cholesterol trapped in Golgi
   │ cleared by             │ ↓ plasma-membrane cholesterol
   ▼ autophagy              ▼
 Proteostatic stress ──► Schwann-cell apoptosis ◄── impaired myelin lipids
            │  (+ Ca²⁺ dysregulation, MMP/ECM remodeling)
            ▼
  Dysmyelination / demyelination of peripheral nerves
            │  leads to
            ▼
  Slowed conduction + secondary axonal loss
            │  manifests as
            ▼
  Distal progressive sensorimotor neuropathy ± deafness
```

**Upstream vs downstream:** The mutation and protein misfolding/ER-Golgi retention are the **upstream initiating events**; aggresome formation, cholesterol sequestration, Ca²⁺ dysregulation, and ECM remodeling are **intermediate** Schwann-cell-autonomous processes; demyelination, secondary axonal loss, and the clinical phenotype are **downstream**. The mechanism is best classified as a **toxic gain-of-function / dominant-negative** proteostasis disease — fundamentally different from the **gene-dosage** mechanism of CMT1A and HNPP, which is why CMT1A-directed therapies (ascorbic acid, *PMP22*-lowering) are not expected to help CMT1E.

**Cell types (CL):** myelinating Schwann cell (CL:0002573); infiltrating macrophage (CL:0000235). **Biological processes (GO):** myelination (GO:0042552); ensheathment of neurons / compact myelin (GO:0043209); ER-associated protein catabolic process / ERAD; autophagy (GO:0006914); protein folding (GO:0006457); cholesterol transport (GO:0030301); apoptotic process (GO:0006915). **Cellular components (GO):** ER (GO:0005783); Golgi apparatus (GO:0005794); lysosome (GO:0005764); aggresome (GO:0016235).

---

## Section-by-Section Findings

### 1. Disease Information
CMT1E is an autosomal dominant demyelinating hereditary motor and sensory neuropathy caused by *PMP22* coding point mutations. **Identifiers:** MONDO:0007311; OMIM #118300; gene *PMP22* (HGNC:9118); chromosome 17p12. Orphanet groups it under CMT1/PMP22-related neuropathy. **Synonyms:** Charcot-Marie-Tooth neuropathy type 1E; CMT1 with deafness; PMP22 point-mutation CMT1. Information derives from aggregated disease-level resources plus clinical cohort/family studies, not EHR data.

### 2. Etiology
**Primary cause:** heterozygous germline (frequently de novo) point mutation or small indel in *PMP22*, usually in a transmembrane domain ([PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/)). **Genetic risk factors:** the specific pathogenic *PMP22* variant is causal and largely deterministic; the exact variant is the main modifier of severity (variable expressivity — [PMID: 34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/)). **Environmental risk/protective factors and gene-environment interactions:** none established; this is a monogenic Mendelian disorder. Neurotoxic drugs (e.g., vincristine) are a general precaution in CMT but not specifically characterized for CMT1E. No protective alleles identified.

### 3. Phenotypes
| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Distal muscle weakness/atrophy | Clinical sign | HP:0003693 / HP:0003701 | Childhood–adult; progressive; near-universal |
| Distal sensory loss | Symptom/sign | HP:0002936 | Progressive |
| Pes cavus | Physical manifestation | HP:0001761 | Common |
| Hammertoes / foot deformity | Physical manifestation | HP:0001765 | Common |
| Areflexia / hyporeflexia | Clinical sign | HP:0001315 | Common |
| Foot drop / steppage gait | Clinical sign | HP:0009830 | Common |
| Sensorineural hearing loss | Sign / lab (audiometry) | HP:0000407 | >40% of CMT1E ([PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/)) — distinguishing |
| Slowed motor NCV (<38 m/s) | Lab / electrophysiology | HP:0003431 | Universal in demyelinating CMT1 |
| Respiratory / diaphragmatic involvement | Sign | HP:0002093 | Uncommon ([PMID: 42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/), model) |
| Esophageal / GI dysmotility | Symptom | HP:0002015 | Rare ([PMID: 40270660](https://pubmed.ncbi.nlm.nih.gov/40270660/)) |
| Cognitive impairment (severe/DSS end) | Sign | HP:0001268 | Rare, severe variants ([PMID: 35974257](https://pubmed.ncbi.nlm.nih.gov/35974257/)) |

**Onset:** ranges from congenital/infantile (severe, DSS-like) to late-adult (mild), reflecting bimodal expressivity. **Progression:** slowly progressive, chronic. **QoL:** reduced across physical, emotional, and social domains, with the physical domain most disabling ([PMID: 41571707](https://pubmed.ncbi.nlm.nih.gov/41571707/)).

### 4. Genetic / Molecular Information
**Causal gene:** *PMP22* (OMIM *601097; HGNC:9118), encoding a 22-kDa tetraspan integral membrane protein of compact PNS myelin ([PMID: 11002284](https://pubmed.ncbi.nlm.nih.gov/11002284/)). **Variant types:** missense (predominant, transmembrane domains), plus small indels; classified pathogenic/likely pathogenic per ACMG/AMP. **Representative variants:** hotspots c.68C>G and c.215C>T ([PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/)); p.Trp28Cys (mild, Portuguese family — [PMID: 34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/)); Leu16Pro (TrJ / CMT1E); Gly150Asp (Trembler / DSS — [PMID: 35974257](https://pubmed.ncbi.nlm.nih.gov/35974257/)). **Allele frequency:** pathogenic variants are private/rare (absent or extremely rare in gnomAD). **Origin:** germline; frequent de novo. **Functional consequence:** toxic gain-of-function / dominant-negative via misfolding, not haploinsufficiency. **Modifier genes/epigenetics:** none established; the causal variant itself is the principal severity determinant. **Chromosomal abnormalities:** none (point-mutation disease; distinct from the CNVs underlying CMT1A/HNPP).

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are established. CMT1E is monogenic and Mendelian. General neurotoxin avoidance (e.g., vincristine) applies to CMT broadly.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the ordered causal chain, branch points, and ontology terms. Key steps: transmembrane-domain misfolding → ER/Golgi retention → aggresome formation cleared by autophagy → cholesterol sequestration and Ca²⁺ dysregulation → Schwann-cell apoptosis → dysmyelination → secondary axonal loss → clinical neuropathy with deafness.

### 7. Anatomical Structures Affected
**Primary:** peripheral nerves (UBERON:0000044), especially motor/sensory nerves of distal limbs; sciatic (UBERON:0001322) and phrenic (UBERON:0002385) nerves in models. **Body systems:** peripheral nervous system; secondary musculoskeletal (foot deformity), auditory system (sensorineural hearing loss), and occasionally respiratory/GI smooth muscle. **Cell:** myelinating Schwann cell (CL:0002573). **Subcellular:** ER (GO:0005783), Golgi (GO:0005794), lysosome, aggresome. **Laterality:** bilateral, symmetric, length-dependent.

### 8. Temporal Development
**Onset:** bimodal — early-onset severe (infantile/childhood, DSS-like) vs late-onset mild (adult, up to late-sixties). **Course:** chronic, slowly progressive, lifelong; not episodic or relapsing-remitting (contrast HNPP). **Critical periods:** developmental myelination is when *PMP22* dysfunction is most consequential; early Schwann-cell proteostasis may be a therapeutic window ([PMID: 14627652](https://pubmed.ncbi.nlm.nih.gov/14627652/), [PMID: 17701891](https://pubmed.ncbi.nlm.nih.gov/17701891/)). No spontaneous remission.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant; frequent de novo mutations ([PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/)). **Penetrance:** high but variable expressivity even intrafamilially ([PMID: 34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/)). **Prevalence:** CMT overall ~1/2,500 ([PMID: 27584852](https://pubmed.ncbi.nlm.nih.gov/27584852/)); CMT1E <5% of CMT1 ([PMID: 34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/)); pediatric CMT 9.7–82/100,000 ([PMID: 42563944](https://pubmed.ncbi.nlm.nih.gov/42563944/)). **Anticipation / mosaicism / founder effects:** not established for CMT1E specifically; de novo occurrence is common. **Sex ratio:** no strong sex bias reported. **Consanguinity:** not relevant (dominant).

### 10. Diagnostics
**Electrophysiology:** nerve conduction studies showing uniform motor NCV slowing (<38 m/s) — hallmark of demyelinating CMT1. **Genetic testing algorithm:** exclude *PMP22* duplication/deletion first (MLPA/CMA), then Sanger or NGS panel / WES to detect the point mutation ([PMID: 32506583](https://pubmed.ncbi.nlm.nih.gov/32506583/), [PMID: 35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/)). **Audiometry** for hearing loss. **Nerve biopsy** (rarely needed) shows demyelination and onion-bulb formation. **Differential diagnosis:** CMT1A (duplication), CMT1B (*MPZ*), CMTX1 (*GJB1*), CIDP (acquired), Dejerine-Sottas syndrome. **Screening:** cascade genetic testing of at-risk relatives; prenatal/preimplantation testing available given a known familial variant.

### 11. Outcome / Prognosis
**Survival:** normal or near-normal life expectancy in typical CMT1E; not directly life-limiting, though severe early-onset (DSS) forms carry higher morbidity, and rare respiratory involvement can affect prognosis ([PMID: 42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/)). **Morbidity:** significant, chronic disability from progressive weakness, deformity, and sensory loss; CMT1E ranks among the most disabling CMT subtypes ([PMID: 37170966](https://pubmed.ncbi.nlm.nih.gov/37170966/)). **Prognostic factors:** specific variant / domain location, age of onset, presence of hearing loss. No validated molecular prognostic biomarkers.

### 12. Treatment
**No disease-modifying therapy** ([PMID: 41571707](https://pubmed.ncbi.nlm.nih.gov/41571707/), [PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)). **Supportive/rehabilitative (NCIT-type interventions):** physical therapy / strength training (NCIT: Physical Therapy), orthoses/AFOs (NCIT: Orthotic Device), occupational therapy, corrective foot surgery, pain management, hearing aids. Strength training showed benefit for timed walking in CMT ([PMID: 19588347](https://pubmed.ncbi.nlm.nih.gov/19588347/)). **Not indicated:** ascorbic acid (no benefit in CMT1A; dosage-model therapy — [PMID: 21393063](https://pubmed.ncbi.nlm.nih.gov/21393063/), [PMID: 26662471](https://pubmed.ncbi.nlm.nih.gov/26662471/)). **Experimental / mechanism-matched:** curcumin (proteostasis/anti-apoptotic; preclinical rescue of TrJ — [PMID: 17701891](https://pubmed.ncbi.nlm.nih.gov/17701891/)); autophagy enhancers; HDAC6 inhibitors; UPR modulators ([PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)). *PMP22* silencers target CMT1A dosage and are **not** appropriate for point-mutation CMT1E unless allele-specific.

### 13. Prevention
No primary prevention (monogenic). **Genetic counseling** is central: autosomal dominant inheritance with 50% transmission risk, plus de novo recurrence counseling. **Reproductive options:** prenatal diagnosis and preimplantation genetic testing when the familial variant is known. **Tertiary prevention:** rehabilitation, orthotics, foot care, fall prevention, and anticipatory monitoring for respiratory/auditory complications.

### 14. Other Species / Natural Disease
*Pmp22* is highly conserved; **mouse (NCBI Taxon:10090)** orthologue *Pmp22* underlies the spontaneous **Trembler (Tr)** and **Trembler-J (TrJ)** mutants — naturally occurring dysmyelinating neuropathies that are genuine models of human *PMP22* point-mutation disease ([PMID: 42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/), [PMID: 30685714](https://pubmed.ncbi.nlm.nih.gov/30685714/)). No zoonotic potential. Evolutionary conservation of PMP22 function in myelination makes rodent models informative but imperfect (species differences in lesions — [PMID: 30685714](https://pubmed.ncbi.nlm.nih.gov/30685714/)).

### 15. Model Organisms
**Natural point-mutation mice:** Trembler-J (Leu16Pro, the human CMT1E allele) and Trembler (Gly150Asp) ([PMID: 42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/), [PMID: 15755691](https://pubmed.ncbi.nlm.nih.gov/15755691/)). **Engineered models:** *Pmp22*-null and *Pmp22*-overexpressing lines model HNPP and CMT1A respectively, and comparative studies show **distinct expression profiles / mechanisms** by mutation type ([PMID: 15755691](https://pubmed.ncbi.nlm.nih.gov/15755691/)). **Recapitulation:** TrJ faithfully reproduces dysmyelination, aggresome formation, apoptosis, ECM remodeling, and phrenic-nerve/diaphragm pathology. **Limitations:** rodent lesions differ in some respects from human nerve pathology ([PMID: 30685714](https://pubmed.ncbi.nlm.nih.gov/30685714/)). **In vitro:** DRG/Schwann-cell co-cultures and patient-derived iPSC-Schwann cells are relevant for trafficking/proteostasis assays. **Resources:** MGI, IMSR.

---

## Evidence Base

| PMID | Title (abbreviated) | Evidence type | Role |
|---|---|---|---|
| [35886002](https://pubmed.ncbi.nlm.nih.gov/35886002/) | *PMP22 mutations in CMT1E patients* | Human cohort (Korea) | Defines CMT1E genetics, deafness >40%, severity vs CMT1A, de novo hotspots |
| [34332267](https://pubmed.ncbi.nlm.nih.gov/34332267/) | *Portuguese family, novel PMP22 point mutation* | Human family | Rarity (<5% of CMT1); variable expressivity (p.Trp28Cys) |
| [14627652](https://pubmed.ncbi.nlm.nih.gov/14627652/) | *Autophagy removes aggresomes in Schwann cells* | Model (TrJ) | Aggresome formation; autophagic clearance |
| [10625337](https://pubmed.ncbi.nlm.nih.gov/10625337/) | *PMP22 and demyelinating neuropathies* | In vitro/review | ER/Golgi retention of TM-domain mutants |
| [32511821](https://pubmed.ncbi.nlm.nih.gov/32511821/) | *Subcellular diversion of cholesterol by PMP22* | Model/in vitro | Cholesterol trapped in Golgi; myelination rescue |
| [42105803](https://pubmed.ncbi.nlm.nih.gov/42105803/) | *Diaphragm/phrenic defects in CMT1E mouse* | Model (TrJ) | TrJ = human Leu16Pro; respiratory involvement |
| [15755691](https://pubmed.ncbi.nlm.nih.gov/15755691/) | *Distinct mechanisms by PMP22 dosage vs point mutation* | Model | Point mutation ≠ dosage mechanism |
| [35974257](https://pubmed.ncbi.nlm.nih.gov/35974257/) | *DSS from Trembler mutation* | Human | Severe end: DSS + deafness + cognitive |
| [17701891](https://pubmed.ncbi.nlm.nih.gov/17701891/) | *Oral curcumin mitigates TrJ phenotype* | Model | Mechanism-matched preclinical therapy |
| [41571707](https://pubmed.ncbi.nlm.nih.gov/41571707/) | *CMT and related neuropathies* | Review | No DMT; supportive care; clinical phenotype |
| [40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/) | *CMT management 2025* | Review | Emerging therapies (silencers, HDAC6i, UPR) |
| [42563944](https://pubmed.ncbi.nlm.nih.gov/42563944/) | *CMT in children* | Review | Diagnostic workup; pediatric prevalence |
| [37170966](https://pubmed.ncbi.nlm.nih.gov/37170966/) | *Italian National CMT Registry* | Registry | Demyelinating 65.3%; CMT1E among most disabling |
| [27584852](https://pubmed.ncbi.nlm.nih.gov/27584852/) | *Recent advances in genetic neuropathies* | Review | CMT prevalence 1/2,500 |
| [32506583](https://pubmed.ncbi.nlm.nih.gov/32506583/) | *Diagnostic yield of sequencing strategies* | Human | MLPA→Sanger/NGS diagnostic algorithm |
| [25522693](https://pubmed.ncbi.nlm.nih.gov/25522693/) | *PMP22 neuropathies in Chinese Han* | Human cohort | No point mutations detected — rarity |
| [21393063](https://pubmed.ncbi.nlm.nih.gov/21393063/) / [26662471](https://pubmed.ncbi.nlm.nih.gov/26662471/) | *Ascorbic acid trials* | RCT | Negative: dosage-model therapy fails |
| [31213528](https://pubmed.ncbi.nlm.nih.gov/31213528/) | *PMP22 and store-operated Ca²⁺* | In vitro | Ca²⁺-handling contribution |
| [12421361](https://pubmed.ncbi.nlm.nih.gov/12421361/) | *MMP-mediated ECM degradation in TrJ* | Model | Macrophage/MMP ECM remodeling |
| [11002284](https://pubmed.ncbi.nlm.nih.gov/11002284/) | *Membrane topology of PMP22* | In vitro | Tetraspan protein structure |
| [30685714](https://pubmed.ncbi.nlm.nih.gov/30685714/) | *Rodent PMP22 models* | Review | Model relevance and limitations |

**Consistency of the evidence:** Findings converge across independent human cohorts (Korea, Portugal, Italy, China, Brazil), natural mouse models (Trembler/TrJ), and in vitro trafficking studies. The proteostasis/misfolding mechanism is supported by ≥4 independent model/in vitro lines. The one important *negative* result — ascorbic acid failing in CMT1A RCTs — reinforces (rather than challenges) the conclusion that CMT1E, a distinct proteostasis disorder, requires distinct, mechanism-matched therapy.

---

## Limitations and Knowledge Gaps

1. **CMT1E-specific epidemiology is imprecise.** No dedicated prevalence/incidence estimate exists for CMT1E; it is inferred as <5% of CMT1. Sex ratio, penetrance quantification, and natural-history data are largely extrapolated from broader CMT/CMT1 datasets.
2. **Genotype–phenotype correlation is incomplete.** Although variant position (transmembrane vs extracellular) clearly influences severity, no comprehensive map links specific *PMP22* residues to hearing loss, onset, or progression rate.
3. **Human mechanistic data are limited.** Much of the misfolding/aggresome/cholesterol mechanism derives from Trembler/TrJ mice and in vitro systems; direct confirmation in human CMT1E nerve or iPSC-Schwann cells is sparse.
4. **No CMT1E-specific therapeutic trials.** Curcumin data are preclinical (mouse) only; no human trials in CMT1E. Emerging therapies (HDAC6 inhibitors, UPR modulators, allele-specific silencing) remain unvalidated for point-mutation disease.
5. **Hearing-loss mechanism unexplained.** The >40% frequency of sensorineural hearing loss is well documented but its cellular basis (cochlear vs auditory-nerve myelination) is not established.
6. **Ca²⁺ and ECM contributions** (store-operated calcium, MMP-mediated remodeling) are documented in models but their causal weight in human disease is uncertain.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype registry analysis:** Aggregate ClinVar/HGMD *PMP22* point-mutation variants with clinical severity and hearing-loss status to build a residue-level severity map, distinguishing transmembrane vs loop-domain effects.
2. **Patient-derived iPSC-Schwann-cell models:** Generate CMT1E lines (e.g., Leu16Pro, Trp28Cys, Gly150Asp) to confirm ER/Golgi retention, aggresome burden, cholesterol mis-trafficking, and apoptosis in a human context, and to screen proteostasis modulators.
3. **Mechanism-matched therapeutic screening:** Test autophagy enhancers, chemical chaperones, HDAC6 inhibitors, and UPR modulators against mutant-PMP22 clearance and myelination endpoints in TrJ mice and human iPSC-Schwann cells; advance the most efficacious to CMT1E-specific trial design.
4. **Cholesterol-supplementation study:** Given Golgi cholesterol sequestration, evaluate dietary/pharmacologic cholesterol or statin-pathway modulation on myelination in TrJ models.
5. **Allele-specific silencing:** Develop and test ASO/siRNA approaches that selectively suppress the mutant *PMP22* allele (preserving wild-type dosage) — the rational silencing strategy for a dominant point-mutation disease.
6. **Auditory phenotyping:** Systematically characterize the cochlear/auditory-nerve basis of CMT1E hearing loss (audiometry + ABR in patients; cochlear histology in models) to define an underexplored, distinguishing feature.
7. **Natural-history cohort:** Establish a CMT1E-specific longitudinal cohort (CMTNS, timed walk, QoL, audiometry, respiratory function) to define progression rate and validate outcome measures for future trials.

---

*Report compiled from an autonomous multi-iteration literature investigation (32 papers reviewed; 8 confirmed findings). Evidence types span human clinical/cohort studies, natural and engineered mouse models, and in vitro systems, as annotated throughout.*


## Artifacts

- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Type_1E-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Type_1E-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 16 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:40270660` (7 mentions) - Oesophageal Dysmotility in a Patient with Charcot-Marie-Tooth Disease: Report and Literature Review.
  - shared terms: disease
- `PMID:19588347` (3 mentions) - Rehabilitation interventions for foot drop in neuromuscular disease.
  - shared terms: disease

Weighed against this report's own most characteristic terms: `pmp22`, `cmt1e`, `mutation`, `loss`, `model`, `cmt`, `hearing`, `point-mutation`, `disease`, `cmt1a`, `type`, `trj`, `cmt1`, `severe`, `demyelinating`, `domain`, `nerve`, `mechanism`, `aggresome`, `variant`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002936` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Distal sensory impairment**
- `HP:0001761` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Pes cavus**
- `HP:0001765` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Hammertoe**
- `HP:0001315` (1 mention) - the report calls it "Clinical sign"; HP calls it **Diminished deep tendon reflex**
- `HP:0009830` (1 mention) - the report calls it "Clinical sign"; HP calls it **Peripheral neuropathy**
- `HP:0000407` (1 mention) - the report calls it "Sign / lab (audiometry)"; HP calls it **Sensorineural hearing impairment**
- `HP:0003431` (1 mention) - the report calls it "Lab / electrophysiology"; HP calls it **Decreased motor nerve conduction velocity**
- `HP:0002093` (1 mention) - the report calls it "Sign"; HP calls it **Respiratory insufficiency**
- `HP:0002015` (1 mention) - the report calls it "Symptom"; HP calls it **Dysphagia**
- `HP:0001268` (1 mention) - the report calls it "Sign"; HP calls it **Mental deterioration**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.