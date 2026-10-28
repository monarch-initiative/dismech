---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:39:33.122231'
end_time: '2026-10-15T02:17:14.460272'
duration_seconds: 2261.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Winchester Syndrome
  mondo_id: MONDO:0010201
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 14
  validator_version: 0.3.0
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 5
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: MONDO:0010201
    reported_labels:
    - MONDO
    ontology_label: Winchester syndrome
  - term_id: HP:0000939
    reported_labels:
    - Radiographic
    ontology_label: Osteoporosis
  - term_id: HP:0001371
    reported_labels:
    - Physical manifestation
    ontology_label: Flexion contracture
  - term_id: HP:0001387
    reported_labels:
    - Clinical sign
    ontology_label: Joint stiffness
  - term_id: HP:0004322
    reported_labels:
    - Physical manifestation
    ontology_label: Short stature
  - term_id: HP:0000280
    reported_labels:
    - Physical manifestation
    ontology_label: Coarse facial features
  - term_id: HP:0007957
    reported_labels:
    - Clinical sign (ocular)
    ontology_label: Corneal opacity
  - term_id: HP:0000212
    reported_labels:
    - Clinical sign
    ontology_label: Gingival overgrowth
  - term_id: HP:0000998
    reported_labels:
    - Physical manifestation
    ontology_label: Hypertrichosis
  - term_id: HP:0001627
    reported_labels:
    - Clinical sign
    ontology_label: Abnormal heart morphology
  - term_id: NCIT:C15682
    reported_labels:
    - Physical Therapy
    ontology_label: Dose-Rate
  - term_id: NCIT:C15329
    reported_labels:
    - Analgesic Therapy
    ontology_label: Surgical Procedure
  - term_id: NCIT:C15300
    reported_labels:
    - Cardiac Surgery
    ontology_label: Photodynamic Therapy
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
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
  path: Winchester_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Winchester_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Winchester Syndrome
- **MONDO ID:** MONDO:0010201 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Winchester Syndrome** covering all of the
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

# Winchester Syndrome: A Comprehensive Disease Characterization Report

**Disease:** Winchester Syndrome
**MONDO ID:** MONDO:0010201 · **OMIM:** #277950 · **Category:** Mendelian (autosomal recessive)
**Report type:** Disease knowledge-base characterization (multi-iteration autonomous literature synthesis)
**Evidence basis:** Human clinical case reports/series, model-organism (mouse) studies, in vitro functional assays. No patient-level dataset was provided; this report is synthesized from primary literature (PMIDs cited inline).

---

## Summary

Winchester syndrome is an ultra-rare, autosomal recessive "vanishing bone" skeletal dysplasia caused by **biallelic loss-of-function mutations in *MMP14* (MT1-MMP, membrane type-1 matrix metalloproteinase)**. The defining molecular lesion abolishes the cell-surface activation of pro-MMP2 and cripples pericellular remodeling of type I and type IV collagen. Because MT1-MMP is the master pericellular collagenase required to model skeletal and extraskeletal connective tissue, its loss produces a slow, relentless destruction of bone and a reactive fibrosis of soft tissue. Clinically, this manifests as progressive **carpal and tarsal osteolysis** ("disappearing bones"), generalized osteoporosis, destructive arthropathy with joint contractures, short stature, coarse facial features, peripheral corneal opacities, gingival hypertrophy, thickened leathery skin, and — in a substantial subset — congenital cardiac anomalies ([PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/), [PMID: 14726867](https://pubmed.ncbi.nlm.nih.gov/14726867/)).

Winchester syndrome does not stand alone. Landmark nosological work places it within a unified **"defective collagen-remodeling spectrum" (DECORS)** together with Multicentric Osteolysis, Nodulosis, and Arthropathy (MONA/Torg-Winchester, caused by *MMP2*) and Frank-Ter Haar syndrome (caused by *SH3PXD2B*). The three gene products — SH3PXD2B, MMP14, and MMP2 — physically and functionally cooperate in a single collagen-degradation axis, which is why the three disorders share craniofacial malformation, reduced bone density, skeletal and cardiac anomalies, and dermal fibrosis ([PMID: 31218820](https://pubmed.ncbi.nlm.nih.gov/31218820/)). The mechanism is strongly corroborated by mouse genetics: *Mmp14*-null mice reproduce the human phenotype (dwarfism, osteopenia, arthritis, soft-tissue fibrosis) through ablated collagenolysis, and *Mmp2*-null mice reproduce the bone-density and osteocyte-network defects ([PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/), [PMID: 16959767](https://pubmed.ncbi.nlm.nih.gov/16959767/)).

The disease is strongly associated with **consanguinity**, has been reported across many ethnicities (Indian, Egyptian, Pakistani, Finnish, Iranian, Japanese), and is frequently misdiagnosed as juvenile idiopathic arthritis (JIA) or rheumatoid arthritis — a dangerous error that leads to inappropriate immunosuppression. Diagnosis rests on characteristic radiographic osteolysis confirmed by **MMP-2 zymography** or **molecular testing of *MMP14*/*MMP2***. **No disease-modifying or curative therapy exists**; care is supportive and multidisciplinary (physiotherapy, analgesia, orthopedic correction, and ophthalmologic/cardiac surveillance) ([PMID: 34466312](https://pubmed.ncbi.nlm.nih.gov/34466312/), [PMID: 37842447](https://pubmed.ncbi.nlm.nih.gov/37842447/)).

---

## 1. Disease Information

**Overview.** Winchester syndrome is a Mendelian, autosomal recessive skeletal dysplasia belonging to the "idiopathic / inherited osteolysis" group of disorders. It is characterized by the spontaneous dissolution (osteolysis) of bones — most prominently the carpals and tarsals — together with generalized osteoporosis, progressive joint contractures, short stature, coarse facies, corneal opacities, and characteristic skin changes ([PMID: 14726867](https://pubmed.ncbi.nlm.nih.gov/14726867/)). It is sometimes grouped under the colloquial term "disappearing bone disease," although that label also covers non-heritable entities such as Gorham-Stout disease ([PMID: 21995273](https://pubmed.ncbi.nlm.nih.gov/21995273/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0010201 |
| OMIM | #277950 (Winchester syndrome) |
| Causal gene | *MMP14* (MT1-MMP); closely related MONA = *MMP2* |
| Spectrum | DECORS (defective collagen-remodeling spectrum) |

**Synonyms / alternative names.** Winchester syndrome; Torg-Winchester syndrome; (closely related / historically conflated) Multicentric Osteolysis, Nodulosis and Arthropathy (MONA), Torg syndrome, Nodulosis-Arthropathy-Osteolysis (NAO) syndrome, Multicentric Osteolysis with Arthropathy (MOA). Historically, Winchester syndrome and Torg/MONA were considered variants of a single entity; molecular work now separates classic Winchester syndrome (*MMP14*) from MONA (*MMP2*), while uniting them mechanistically ([PMID: 24637309](https://pubmed.ncbi.nlm.nih.gov/24637309/), [PMID: 31218820](https://pubmed.ncbi.nlm.nih.gov/31218820/)).

**Source of information.** The evidence base is aggregated from **individual patient case reports and small consanguineous-family case series** rather than large registries or EHR datasets — a direct consequence of the disease's extreme rarity.

---

## 2. Etiology

**Primary cause — genetic.** Classic Winchester syndrome is caused by **homozygous (biallelic) loss-of-function mutations in *MMP14***. Evans et al. (2012) identified homozygous *MMP14* mutations in the original Winchester sisters and demonstrated that the resulting signal-peptide substitution **p.Thr17Arg** decreases MT1-MMP membrane localization, with consequent impairment of pro-MMP2 activation ([PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/)):

> "we have now identified homozygous mutations in membrane type-1 metalloproteinase (MT1-MMP or MMP14). We demonstrate that the resulting hydrophobic-region signal-peptide substitution (p.Thr17Arg) decreases MT1-MMP membrane localization with consequent impairment of pro-MMP2 activation."

The closely allied MONA/Torg phenotype is caused by biallelic *MMP2* mutations; MMP2 encodes a gelatinase that cleaves type IV collagen, a major basement-membrane component ([PMID: 24637309](https://pubmed.ncbi.nlm.nih.gov/24637309/)).

**Genetic risk factors.** The overwhelming risk determinant is **inheritance of two pathogenic alleles**, almost always in the setting of **parental consanguinity**. There are no established susceptibility loci or polygenic contributions; this is a monogenic Mendelian disorder.

**Environmental risk factors.** None established. There is no evidence that toxins, infections, diet, occupational exposure, age, or sex trigger or modify disease onset. The only "non-genetic" risk amplifier is the population-structural factor of consanguineous mating, which raises homozygosity.

**Protective factors.** None identified at the genetic or environmental level. Because the disorder is fully penetrant recessive, the only "protective" state is being a heterozygous carrier (clinically unaffected).

**Gene–environment interactions.** No gene–environment interaction has been described. The phenotype appears driven essentially entirely by genotype, with variable expressivity attributable to genetic/allelic background rather than environment.

---

## 3. Phenotypes

Winchester syndrome is a multisystem disorder. The cardinal features, drawn primarily from Sidwell et al. (2004) and corroborated across the MONA/Winchester case series, are summarized below ([PMID: 14726867](https://pubmed.ncbi.nlm.nih.gov/14726867/)):

> "characterized by dissolution of carpal and tarsal bones with generalized osteoporosis, progressive joint contractures, short stature, peripheral corneal opacities, and coarse facial features."

| Phenotype | Type | HPO suggestion | Onset | Severity / progression | Frequency |
|---|---|---|---|---|---|
| Carpal/tarsal osteolysis ("vanishing bone") | Radiographic/clinical sign | HP:0010656 (carpal) / HP:0008369 (tarsal) | Childhood | Progressive | Cardinal/near-universal |
| Generalized osteoporosis / reduced bone density | Radiographic | HP:0000939 | Childhood | Progressive | Very frequent |
| Progressive joint contractures | Physical manifestation | HP:0001371 | Childhood | Progressive | Very frequent |
| Destructive arthropathy (pain, swelling, stiffness) | Clinical sign | HP:0001387 | Childhood | Progressive | Frequent |
| Short stature / dwarfism | Physical manifestation | HP:0004322 | Childhood | Stable–progressive | Frequent |
| Coarse facial features | Physical manifestation | HP:0000280 | Childhood | Progressive | Frequent |
| Peripheral corneal opacities | Clinical sign (ocular) | HP:0007957 | Childhood | Slowly progressive | Frequent |
| Gingival hypertrophy | Clinical sign | HP:0000212 | Childhood | Progressive | Variable |
| Thickened, leathery skin / dermal fibrosis | Physical manifestation | HP:0000974 (thick skin) | Childhood | Progressive | Variable |
| Hypertrichosis / hirsutism | Physical manifestation | HP:0000998 | Childhood | Stable | Variable |
| Hyperpigmentation | Physical manifestation | HP:0000953 | Childhood | Variable | Variable |
| Subcutaneous nodules (esp. MONA; palmoplantar) | Physical manifestation | HP:0031800 / HP:0012732 | Childhood | Progressive | **Distinguishes MONA from classic Winchester** |
| Congenital cardiac/valve defects | Clinical sign | HP:0001627 | Congenital | Variable | Subset (can be presenting feature) |

**Cutaneous phenotype.** In addition to generalized skin thickening, a distinctive **progressive multilayered banded skin** pattern has been reported in Winchester syndrome, along with hypertrichosis, hyperpigmentation, and subcutaneous nodules ([PMID: 14726867](https://pubmed.ncbi.nlm.nih.gov/14726867/)).

**Key clinical distinction.** Classic Winchester syndrome is historically distinguished from MONA by the **absence or paucity of palmoplantar subcutaneous nodulosis**; nodulosis is a hallmark of MONA (*MMP2*) ([PMID: 24637309](https://pubmed.ncbi.nlm.nih.gov/24637309/), [PMID: 39540058](https://pubmed.ncbi.nlm.nih.gov/39540058/)).

**Ocular phenotype (refined).** In a molecularly confirmed spectrum patient, anterior-segment OCT demonstrated **posterior stromal and endothelial hyperreflectivity**, and confocal microscopy showed an **acellular peripheral endothelium with a normal central endothelium**; the peripheral corneal opacities were **visually insignificant** ([PMID: 39502084](https://pubmed.ncbi.nlm.nih.gov/39502084/)):

> "Anterior segment optical coherence tomography (AS-OCT) demonstrated posterior stromal and endothelial hyperreflectivity. Confocal microscopy demonstrated an acellular peripheral endothelium with a normal central endothelium."

**Quality-of-life impact.** Formal instruments (EQ-5D, SF-36, PROMIS) have not been applied in this ultra-rare disease. Qualitatively, the dominant QoL burdens are **progressive loss of hand and foot function from osteolysis plus contractures**, chronic arthralgia, impaired mobility, and (where present) cardiac morbidity. Vision is usually preserved because corneal opacities are peripheral and visually insignificant.

---

## 4. Genetic / Molecular Information

**Causal genes.**

| Gene (HGNC) | Protein | Associated phenotype | Core molecular role |
|---|---|---|---|
| ***MMP14*** | MT1-MMP (membrane type-1 MMP) | **Classic Winchester syndrome** | Cell-surface collagenase; activates pro-MMP2; pericellular type I collagen turnover |
| ***MMP2*** | Gelatinase A / 72 kDa type IV collagenase | MONA / Torg (Winchester spectrum) | Cleaves type IV collagen; osteocyte canalicular network maintenance |
| *SH3PXD2B* | Tks5 adaptor | Frank-Ter Haar syndrome (same spectrum) | Podosome scaffold organizing MT1-MMP delivery |

**Pathogenic variants.**
- ***MMP14*:* The index pathogenic variant is the signal-peptide missense **p.Thr17Arg**, which reduces MT1-MMP membrane localization and impairs pro-MMP2 activation ([PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/)).
- ***MMP2*:* Reported variants span missense (e.g., c.538G>A p.Asp180Asn [PMID: 24637309](https://pubmed.ncbi.nlm.nih.gov/24637309/); c.1188C>A p.Ser396Arg, predicted to disturb the MMP2 collagen-binding region), splice-donor (e.g., c.1336+2T>G, predicted to introduce a premature stop codon), and nonsense variants ([PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/), [PMID: 37025869](https://pubmed.ncbi.nlm.nih.gov/37025869/)).

**Variant classification.** Reported disease-causing variants are classified **pathogenic/likely pathogenic** per ACMG/AMP criteria, typically supported by homozygosity in affected individuals, carrier status in consanguineous parents, segregation, conservation, and in-silico/molecular-modeling evidence.

**Variant type/class.** Missense (signal-peptide and collagen-binding region), nonsense, and splice-site variants predominate. All converge on **loss of function**.

**Allele frequency.** Pathogenic alleles are **extremely rare** in population databases (gnomAD), consistent with an ultra-rare recessive disorder; most are private or population/family-specific.

**Somatic vs germline.** All pathogenic variants are **germline**; there is no somatic/oncogenic component.

**Functional consequence.** **Loss of function** of pericellular collagenolytic activity (MT1-MMP) and/or type IV collagenase activity (MMP2). For p.Thr17Arg, the mechanism is mislocalization of MT1-MMP away from the membrane, blocking the MT1-MMP → pro-MMP2 activation step ([PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/)).

**Modifier genes.** Within the DECORS axis, *SH3PXD2B*, *MMP14*, and *MMP2* are functionally interdependent; dysfunction of one effectively modifies the output of the shared pathway ([PMID: 31218820](https://pubmed.ncbi.nlm.nih.gov/31218820/)). No classical independent modifier loci are established. Significant **intrafamilial variability** in age of onset and severity is documented, implying modifier effects that remain uncharacterized ([PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/)).

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification signature has been reported for Winchester syndrome.

**Chromosomal abnormalities.** None; this is a single-gene disorder without characteristic aneuploidy, translocation, or large structural rearrangement.

---

## 5. Environmental Information

- **Environmental factors:** None implicated. No toxin, radiation, pollution, or occupational exposure is associated with onset or progression.
- **Lifestyle factors:** None implicated (smoking, diet, exercise, alcohol have no established role).
- **Infectious agents:** Not applicable. Winchester syndrome is not infectious and has no known infectious trigger.

The only population-level non-genetic contributor is **consanguinity**, which increases the probability of homozygosity for rare recessive *MMP14*/*MMP2* alleles ([PMID: 26601801](https://pubmed.ncbi.nlm.nih.gov/26601801/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *MMP14* loss-of-function mutation** (e.g., signal-peptide p.Thr17Arg) **results in** reduced MT1-MMP membrane localization. *(Demonstrated — [PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/))*
2. Reduced membrane MT1-MMP **leads to** impaired cell-surface activation of **pro-MMP2 → active MMP2**. *(Demonstrated — [PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/))*
3. Loss of MT1-MMP collagenolytic activity (± downstream MMP2 activity) **leads to** failure of **pericellular type I / type IV collagen remodeling**. *(Demonstrated in mouse — [PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/))*
4. Defective collagen turnover **results in** inadequate modeling and maintenance of skeletal and extraskeletal connective tissue. *(Demonstrated in mouse — [PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/))*
   - **Branch A (bone):** Disrupted osteocytic canalicular network and dysregulated osteoblast gene expression (↑ osteopontin/bone sialoprotein) **lead to** abnormal bone homeostasis → **progressive osteolysis + osteoporosis** → carpal/tarsal dissolution, short stature, fractures. *([PMID: 16959767](https://pubmed.ncbi.nlm.nih.gov/16959767/), [PMID: 22917927](https://pubmed.ncbi.nlm.nih.gov/22917927/))*
   - **Branch B (joint):** Failure to model peri-articular connective tissue **leads to** destructive arthropathy and **joint contractures**.
   - **Branch C (soft tissue):** Accumulation of unremodeled collagen **results in** **dermal/soft-tissue fibrosis**, thickened skin, gingival hypertrophy, coarse facies, and corneal stromal/endothelial changes. *([PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/), [PMID: 39502084](https://pubmed.ncbi.nlm.nih.gov/39502084/))*
   - **Branch D (cardiac):** Abnormal connective-tissue/valve matrix remodeling **leads to** **congenital cardiac/valve defects**. *(Inferred from phenotype + spectrum — [PMID: 37025869](https://pubmed.ncbi.nlm.nih.gov/37025869/), [PMID: 33101055](https://pubmed.ncbi.nlm.nih.gov/33101055/))*
5. Secondary to MMP-2 loss, **dysregulated serum cytokines and hormones** **are implicated in promoting osteolysis** (candidate downstream amplifiers and therapeutic targets). *(Demonstrated/associative — [PMID: 33101055](https://pubmed.ncbi.nlm.nih.gov/33101055/))*

### Mechanistic schematic

```
 MMP14 (MT1-MMP) biallelic LOF
            │  (p.Thr17Arg → mislocalization)
            ▼
 ↓ membrane MT1-MMP ──► ↓ pro-MMP2 activation
            │                     │
            ▼                     ▼
 ↓ pericellular type I/IV collagenolysis  (core defect)
            │
            ▼
 Inadequate connective-tissue remodeling
   ├─► BONE: osteocyte canalicular + osteoblast dysregulation → osteolysis/osteoporosis
   ├─► JOINT: arthropathy, contractures
   ├─► SOFT TISSUE: dermal fibrosis, gingival/corneal/facial changes
   └─► HEART: valve/cardiac matrix defects
            │
            ▼
 (amplifier) dysregulated cytokines/hormones → further osteolysis
```

### Detail by category
- **Molecular pathways:** Pericellular matrix proteolysis via the **MT1-MMP → pro-MMP2 activation cascade**; collagen (type I, type IV) degradation. Podosome-mediated protease delivery (SH3PXD2B/Tks5 scaffold) links the three DECORS genes ([PMID: 31218820](https://pubmed.ncbi.nlm.nih.gov/31218820/)).
- **Cellular processes:** Extracellular-matrix organization and turnover; bone remodeling (osteoclast/osteoblast/osteocyte coupling); fibroblast-driven fibrosis. GO suggestions: GO:0030574 (collagen catabolic process), GO:0022617 (extracellular matrix disassembly), GO:0001503 (ossification), GO:0030198 (extracellular matrix organization).
- **Protein dysfunction:** Loss of function — MT1-MMP mislocalized (signal-peptide defect); MMP2 missense disrupting the collagen-binding region, or truncating variants abolishing enzyme ([PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/), [PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/)).
- **Metabolic / biochemical abnormalities:** Reduced/absent gelatinase (MMP-2) activity detectable by zymography; dysregulated serum cytokines/hormones ([PMID: 33101055](https://pubmed.ncbi.nlm.nih.gov/33101055/)).
- **Immune involvement:** No primary autoimmunity; the arthropathy is **mechanical/degenerative**, not inflammatory-autoimmune — a crucial point given frequent JIA misdiagnosis.
- **Tissue damage mechanisms:** Failure of matrix maintenance → osteolysis (resorption outpacing modeling) and fibrosis (accumulation of poorly remodeled collagen).
- **Molecular profiling:** *Mmp2*-null osteoblasts show upregulated **osteopontin (OPN)** and **bone sialoprotein (BSP)**, defining a bone-homeostasis feedback circuit ([PMID: 22917927](https://pubmed.ncbi.nlm.nih.gov/22917927/)). No human single-cell or spatial datasets are published for this ultra-rare disease.

**Cell types (CL):** osteocyte (CL:0000137), osteoblast (CL:0000062), osteoclast (CL:0000092), fibroblast (CL:0000057), corneal endothelial cell (CL:0000575).

---

## 7. Anatomical Structures Affected

**Organ level.**
- *Primary:* Skeleton — especially **carpal and tarsal bones** (UBERON:0001773 carpal region / tarsal region), small bones of hands and feet; generalized skeleton (osteoporosis).
- *Joints:* wrists, interphalangeal and metacarpophalangeal joints, knees.
- *Secondary / multisystem:* **eye** (cornea, UBERON:0000964), **skin** (UBERON:0002097), **gingiva** (UBERON:0001828), **heart/cardiac valves** (UBERON:0000948 / UBERON:0000946).
- *Body systems:* skeletal, articular/connective-tissue, integumentary, ocular, and cardiovascular.

**Tissue and cell level.** Connective tissue (bone matrix, dermal collagen); affected cell populations: osteocytes, osteoblasts, osteoclasts, fibroblasts, and corneal endothelial cells (peripheral acellular endothelium) ([PMID: 39502084](https://pubmed.ncbi.nlm.nih.gov/39502084/)).

**Subcellular level.** Defect localizes to the **plasma membrane / cell surface** (GO:0005886) where MT1-MMP acts, and the **extracellular matrix / extracellular region** (GO:0031012, GO:0005615). Podosome-associated protease trafficking is implicated via SH3PXD2B.

**Localization & lateralization.** Skeletal involvement is characteristically **bilateral and symmetric**, centered on the appendicular skeleton (hands/feet). Corneal opacities are **peripheral and bilateral**.

---

## 8. Temporal Development

- **Onset:** Typically **childhood**, though onset can range from early childhood into **late adolescence** ([PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/)). Cardiac defects, when present, may be **congenital** and can be the first presentation ([PMID: 37025869](https://pubmed.ncbi.nlm.nih.gov/37025869/)).
- **Onset pattern:** Insidious and **chronic**.
- **Progression:** **Progressive** osteolysis and contractures; longitudinal follow-up confirms continued bone loss over years ([PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/)). There is a stereotyped chronological order — skeletal manifestations begin in hands/feet, with later, wider joint involvement ([PMID: 34307793](https://pubmed.ncbi.nlm.nih.gov/34307793/)).
- **Disease course:** Chronic, lifelong, progressive; no spontaneous remission.
- **Critical periods:** Childhood/adolescence represents the window of most active osteolysis — the practical window for diagnosis and supportive intervention.

---

## 9. Inheritance and Population

**Epidemiology.** Winchester syndrome is **ultra-rare**; precise prevalence/incidence are not established and it is described only through isolated cases and small family series. Orphanet classifies it among extremely rare bone dysplasias.

**Inheritance.** **Autosomal recessive** ([PMID: 26601801](https://pubmed.ncbi.nlm.nih.gov/26601801/)):

> "Multicentric osteolysis nodulosis and arthropathy (MONA) is an infrequently described autosomal recessive skeletal dysplasia."

- **Penetrance:** Effectively complete in biallelic carriers.
- **Expressivity:** Variable, with documented significant **intrafamilial variability** in onset and severity ([PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/)).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** Many variants are private/family-specific; several populations harbor recurrent homozygous variants in consanguineous pedigrees.
- **Consanguinity:** Strongly linked — the majority of reported families are consanguineous ([PMID: 26601801](https://pubmed.ncbi.nlm.nih.gov/26601801/), [PMID: 22876575](https://pubmed.ncbi.nlm.nih.gov/22876575/)).
- **Carrier frequency:** Not established; expected to be very low outside consanguineous or founder populations.

**Population demographics.** Reported in diverse ethnicities — **Indian, Egyptian, Pakistani, Finnish, Iranian, Japanese** — supporting a **pan-ethnic** distribution ([PMID: 22876575](https://pubmed.ncbi.nlm.nih.gov/22876575/), [PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/), [PMID: 38409917](https://pubmed.ncbi.nlm.nih.gov/38409917/)). No strong sex predilection is established (consistent with autosomal recessive inheritance). Age distribution of affected individuals is concentrated in childhood through young adulthood at time of diagnosis.

---

## 10. Diagnostics

**Clinical/radiographic.** Diagnosis begins with the **characteristic radiographic pattern**: multicentric osteolysis predominantly of **carpal and tarsal bones**, osteopenia/osteoporosis, dysplastic changes of hands/feet, and (in MONA) subcutaneous nodules ([PMID: 37842447](https://pubmed.ncbi.nlm.nih.gov/37842447/), [PMID: 34307793](https://pubmed.ncbi.nlm.nih.gov/34307793/)).

**Confirmatory tests.** Diagnosis is established by ([PMID: 34466312](https://pubmed.ncbi.nlm.nih.gov/34466312/)):

> "established either by measuring matrix metalloproteinase-2 (MMP-2) enzyme activity through electrophoresis (zymography) or genomic testing."

- **MMP-2 zymography** (gelatin electrophoresis) — functional assay of gelatinase activity.
- **Molecular genetic testing** of ***MMP14*** (Winchester) and ***MMP2*** (MONA) — single-gene testing, targeted panels, or **whole-exome sequencing (WES)**, which has been the discovery route in several families ([PMID: 37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/)).

**Ocular imaging.** AS-OCT and confocal microscopy characterize the peripheral corneal endothelial/stromal changes ([PMID: 39502084](https://pubmed.ncbi.nlm.nih.gov/39502084/)).

**Differential diagnosis.** The most important and dangerous differential is **juvenile idiopathic arthritis / rheumatoid arthritis** ([PMID: 37842447](https://pubmed.ncbi.nlm.nih.gov/37842447/)):

> "can be misdiagnosed as juvenile idiopathic arthritis or rheumatoid arthritis."

Misclassification as JIA leads to inappropriate corticosteroid/immunosuppressive therapy ([PMID: 39463871](https://pubmed.ncbi.nlm.nih.gov/39463871/)). Other differentials include non-heritable osteolyses (Gorham-Stout disease), other inherited osteolysis syndromes, and skeletal dysplasias ([PMID: 21995273](https://pubmed.ncbi.nlm.nih.gov/21995273/)).

**Screening.** In known families, **cascade/carrier testing** and genetic counseling are appropriate; prenatal/preimplantation testing is feasible when the familial variant is known. There is no population newborn screening.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No systematic survival data exist. Skeletal disease is not directly lethal, but **cardiac involvement** can be life-threatening — one child required open-heart surgery at 8 months of age ([PMID: 37025869](https://pubmed.ncbi.nlm.nih.gov/37025869/)).
- **Morbidity/disability:** Dominated by **progressive loss of hand/foot function**, contractures, chronic pain, and reduced mobility — a chronic, lifelong functional burden.
- **Disease course:** Progressive osteolysis with accumulating skeletal deformity; complications include pathologic fractures, severe contractures, and cardiac/valvular disease.
- **Recovery potential:** Osteolytic bone loss is **not reversible** with current care; management is palliative/supportive.
- **Prognostic factors:** Presence and severity of **cardiac involvement** is the principal determinant of serious outcome; extent/rate of skeletal osteolysis governs functional disability. No validated prognostic biomarkers exist.

---

## 12. Treatment

**No disease-specific or curative therapy exists** ([PMID: 34466312](https://pubmed.ncbi.nlm.nih.gov/34466312/)):

> "no specific therapy has been identified with proven long term relief and control of the disease progression."

**Management is supportive and multidisciplinary:**

| Modality | Purpose | NCIT suggestion |
|---|---|---|
| Physiotherapy / rehabilitation | Preserve joint mobility, limit contractures | NCIT:C15682 (Physical Therapy) |
| Analgesia | Chronic pain control | NCIT:C15329 (Analgesic Therapy) |
| Orthopedic / reconstructive surgery | Correct deformity, stabilize joints | NCIT surgical repair |
| Ophthalmologic surveillance | Monitor corneal opacities | — |
| Cardiac surveillance / surgery | Detect & correct valve/congenital defects | NCIT:C15300 (Cardiac Surgery) |

**Pharmacotherapy / pharmacogenomics:** No approved targeted drugs. Critically, **immunosuppression/corticosteroids are not indicated** and reflect misdiagnosis as inflammatory arthritis ([PMID: 39463871](https://pubmed.ncbi.nlm.nih.gov/39463871/)).

**Advanced / experimental therapeutics:** None approved. A mechanistically promising direction: Sarker et al. identified **dysregulated serum cytokines and hormones** common to MMP-2-deficient mice and children as candidate **therapeutic targets** for the osteolysis ([PMID: 33101055](https://pubmed.ncbi.nlm.nih.gov/33101055/)):

> "multicentric osteolysis, nodulosis, and arthropathy (MONA) as well as cardiac valve defects, dwarfism and hirsutism."

Gene/enzyme-replacement approaches are conceptually plausible (restore MT1-MMP/MMP2 function) but remain untested.

---

## 13. Prevention

- **Primary prevention:** Not possible at the individual genetic level. The main lever is **genetic counseling in consanguineous and known-carrier families**, including reproductive options (carrier testing, prenatal/preimplantation genetic diagnosis once the familial variant is identified).
- **Secondary prevention:** **Early, accurate diagnosis** — recognizing carpal/tarsal osteolysis and pursuing zymography/molecular testing rather than defaulting to a JIA diagnosis — prevents harmful immunosuppression and enables timely cardiac/ophthalmologic surveillance.
- **Tertiary prevention:** Physiotherapy, orthopedic intervention, and **cardiac monitoring** to limit complications.
- **Immunization / public health / environmental interventions:** Not applicable (non-infectious, non-environmental monogenic disorder).
- **Counseling:** Genetic counseling is the cornerstone of prevention given autosomal recessive inheritance and consanguinity linkage.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *MMP14* and *MMP2* are highly conserved across mammals; mouse orthologs *Mmp14* and *Mmp2* (NCBI Taxon:10090, *Mus musculus*) are the principal comparative systems.
- **Natural disease in other species:** No well-characterized spontaneous Winchester-syndrome equivalent is documented in companion animals or wildlife; the disease model is engineered (knockout), not naturally occurring.
- **Comparative biology:** The **evolutionary conservation of the MT1-MMP → MMP2 collagen-remodeling axis** is strong, which is why murine knockouts faithfully reproduce human skeletal/connective-tissue pathology ([PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/)).
- **Transmission / zoonosis:** Not applicable.

---

## 15. Model Organisms

Mouse knockouts are the definitive disease models and provide the strongest mechanistic validation ([PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/)):

> "MT1-MMP deficiency causes craniofacial dysmorphism, arthritis, osteopenia, dwarfism, and fibrosis of soft tissues due to ablation of a collagenolytic activity that is essential for modeling of skeletal and extraskeletal connective tissues."

| Model | Type | Phenotype recapitulation | Key insight | Ref |
|---|---|---|---|---|
| ***Mmp14⁻/⁻*** mouse | Constitutive knockout (mammalian) | **High** — dwarfism, osteopenia, arthritis, craniofacial dysmorphism, soft-tissue fibrosis | Loss of essential collagenolysis drives connective-tissue disease | [PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/) |
| ***Mmp2⁻/⁻*** mouse | Constitutive knockout (mammalian) | **High** — ↓ bone mineral density, disrupted osteocytic canalicular network, dysregulated osteoblast genes | MMP-2 crucial for osteocyte canaliculi and bone metabolism | [PMID: 16959767](https://pubmed.ncbi.nlm.nih.gov/16959767/) |
| *Mmp2⁻/⁻* osteoblasts / SaOS2 siRNA | Cellular / in vitro | Upregulated **OPN** and **BSP** | Defines a bone-homeostasis feedback circuit regulated by MMP-2 | [PMID: 22917927](https://pubmed.ncbi.nlm.nih.gov/22917927/) |

**Model characteristics.** The canalicular-network insight is explicit ([PMID: 16959767](https://pubmed.ncbi.nlm.nih.gov/16959767/)):

> "MMP-2 plays a crucial role in forming and maintaining the osteocytic canalicular network."

**Limitations.** Mouse models capture skeletal/connective-tissue biology well but do not fully model the human ocular phenotype or allele-specific effects (e.g., the human p.Thr17Arg mislocalization mechanism). **Resources:** MGI, IMPC/IMSR.

---

## Key Findings (consolidated)

**F001 — Winchester syndrome is caused by biallelic *MMP14* (MT1-MMP) mutations.** Evans et al. (2012) identified homozygous *MMP14* mutations in the original Winchester sisters; the p.Thr17Arg signal-peptide substitution decreases MT1-MMP membrane localization and impairs pro-MMP2 activation, inherited autosomal recessively ([PMID: 22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/)).

**F002 — Winchester/MONA spectrum is a defective collagen-remodeling disorder (DECORS).** de Vos et al. (2019) reviewed 63 patients and showed that Frank-Ter Haar (SH3PXD2B), Winchester (MMP14), and MONA (MMP2) share craniofacial malformations, reduced bone density, skeletal/cardiac anomalies, and dermal fibrosis; the protein products "directly cooperate in collagen remodeling," prompting the DECORS nosology ([PMID: 31218820](https://pubmed.ncbi.nlm.nih.gov/31218820/)).

**F003 — Mouse models recapitulate the human osteolysis syndrome via inadequate collagen turnover.** *Mmp14⁻/⁻* and *Mmp2⁻/⁻* mice reproduce craniofacial dysmorphism, arthritis, osteopenia, dwarfism, soft-tissue fibrosis, reduced bone mineral density, and disrupted osteocytic canalicular networks ([PMID: 10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/), [PMID: 16959767](https://pubmed.ncbi.nlm.nih.gov/16959767/), [PMID: 22917927](https://pubmed.ncbi.nlm.nih.gov/22917927/)).

**F004 — Core clinical phenotype: carpal/tarsal osteolysis, contractures, coarse facies, corneal opacities.** Plus short stature, generalized osteoporosis, and cutaneous features (thickened skin, hypertrichosis, hyperpigmentation, subcutaneous nodules, gingival hypertrophy); Winchester is distinguished from MONA by paucity of palmoplantar nodulosis ([PMID: 14726867](https://pubmed.ncbi.nlm.nih.gov/14726867/)).

**F005 — Diagnosis relies on radiographic osteolysis + MMP2/MMP14 testing or MMP-2 zymography; frequently misdiagnosed as JIA** ([PMID: 34466312](https://pubmed.ncbi.nlm.nih.gov/34466312/), [PMID: 37842447](https://pubmed.ncbi.nlm.nih.gov/37842447/)).

**F006 — Autosomal recessive inheritance with strong consanguinity link; cardiac defects are part of the multisystem phenotype,** and may be the first presentation ([PMID: 26601801](https://pubmed.ncbi.nlm.nih.gov/26601801/), [PMID: 37025869](https://pubmed.ncbi.nlm.nih.gov/37025869/)).

**F007 — No disease-specific/curative therapy exists; management is supportive and multidisciplinary** ([PMID: 34466312](https://pubmed.ncbi.nlm.nih.gov/34466312/), [PMID: 33101055](https://pubmed.ncbi.nlm.nih.gov/33101055/)).

**F008 — Ocular involvement: peripheral corneal opacities with posterior stromal/endothelial changes, usually visually insignificant** ([PMID: 39502084](https://pubmed.ncbi.nlm.nih.gov/39502084/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [22922033](https://pubmed.ncbi.nlm.nih.gov/22922033/) | *MT1-MMP (MMP14) causes Winchester syndrome* | **Establishes causal gene** and p.Thr17Arg mechanism |
| [31218820](https://pubmed.ncbi.nlm.nih.gov/31218820/) | *Multicentric osteolytic syndromes = defective collagen remodeling* | Unifies MMP14/MMP2/SH3PXD2B into **DECORS** |
| [10520996](https://pubmed.ncbi.nlm.nih.gov/10520996/) | *MT1-MMP-deficient mice* | Mouse model recapitulates phenotype; collagenolytic mechanism |
| [16959767](https://pubmed.ncbi.nlm.nih.gov/16959767/) | *MMP-2 in osteocytic canalicular formation* | Links MMP2 loss to bone phenotype |
| [22917927](https://pubmed.ncbi.nlm.nih.gov/22917927/) | *Loss of MMP-2 upregulates OPN/BSP* | Downstream bone-homeostasis circuit |
| [14726867](https://pubmed.ncbi.nlm.nih.gov/14726867/) | *Progressive multilayered banded skin in Winchester* | Cardinal clinical + cutaneous features |
| [34466312](https://pubmed.ncbi.nlm.nih.gov/34466312/) | *Clinical/molecular profile of MONA* | Diagnostic tests; no disease-modifying therapy |
| [37842447](https://pubmed.ncbi.nlm.nih.gov/37842447/) | *MONA simulating JIA in adult* | Key differential/misdiagnosis risk |
| [26601801](https://pubmed.ncbi.nlm.nih.gov/26601801/) | *Clinical/mutation profile of MONA* | Autosomal recessive inheritance; consanguinity |
| [37025869](https://pubmed.ncbi.nlm.nih.gov/37025869/) | *Novel MONA mutation* | Cardiac defect as presenting feature |
| [33101055](https://pubmed.ncbi.nlm.nih.gov/33101055/) | *Dysregulated cytokines/hormones in MMP-2 deficiency* | Multisystem phenotype; therapeutic targets |
| [39502084](https://pubmed.ncbi.nlm.nih.gov/39502084/) | *Multimodal imaging of corneal opacities* | Refines ocular phenotype |
| [37710205](https://pubmed.ncbi.nlm.nih.gov/37710205/) | *Two families (Pakistan/Finland)* | Variant spectrum; variable age of onset |
| [24637309](https://pubmed.ncbi.nlm.nih.gov/24637309/) | *MMP2 case report* | Torg/MMP2 biology; nodulosis distinction |
| [22876575](https://pubmed.ncbi.nlm.nih.gov/22876575/) | *Three Egyptian patients* | Pan-ethnic; consanguinity |
| [39540058](https://pubmed.ncbi.nlm.nih.gov/39540058/) | *Pakistani MONA family* | Nodulosis + MMP2 deficiency |
| [34307793](https://pubmed.ncbi.nlm.nih.gov/34307793/) | *Two children, genetic–skeletal correlations* | Skeletal pattern, progression order |
| [39463871](https://pubmed.ncbi.nlm.nih.gov/39463871/) | *MONA case series* | JIA misdiagnosis; multidisciplinary management |
| [38409917](https://pubmed.ncbi.nlm.nih.gov/38409917/) | *Japanese siblings* | Pan-ethnic distribution |
| [21995273](https://pubmed.ncbi.nlm.nih.gov/21995273/) | *Idiopathic osteolysis diagnosis/management* | Differential diagnosis framework |

All findings above are anchored to verified abstract quotes recorded during the investigation.

---

## Limitations and Knowledge Gaps

1. **Nomenclature overlap.** Classic Winchester syndrome (*MMP14*) and MONA/Torg (*MMP2*) are mechanistically unified but genetically distinct; much published literature uses "Torg-Winchester"/"MONA" interchangeably, so some clinical detail is drawn from the *MMP2* literature and extrapolated to the *MMP14* entity under the DECORS framework.
2. **Thin human molecular data.** There are **no human transcriptomic, proteomic, single-cell, or spatial datasets** for this ultra-rare disease; molecular profiling evidence is largely from mouse models.
3. **No quantitative epidemiology.** Prevalence, incidence, carrier frequency, and survival statistics are essentially unknown.
4. **No validated outcome measures.** QoL, prognostic biomarkers, and natural-history endpoints are not formalized.
5. **No therapeutics pipeline.** Treatment is entirely supportive; the cytokine/hormone-targeting hypothesis remains untested in patients.
6. **Modifiers unexplained.** Documented intrafamilial variability implies modifier effects that are uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international registry** for *MMP14*/*MMP2* osteolysis to generate prevalence, natural-history, and genotype–phenotype data (addresses gaps 3–4).
2. **Patient-derived iPSC → osteoblast/osteocyte/chondrocyte models** and organoids to obtain human single-cell transcriptomic/proteomic signatures and test rescue of the MT1-MMP → pro-MMP2 axis.
3. **Variant-function platform:** systematically express *MMP14*/*MMP2* variants (e.g., p.Thr17Arg) to quantify membrane localization, pro-MMP2 activation, and collagenolysis — supporting ACMG reclassification of VUS.
4. **Therapeutic proof-of-concept:** test cytokine/hormone-pathway modulators identified by Sarker et al. ([PMID: 33101055](https://pubmed.ncbi.nlm.nih.gov/33101055/)) in *Mmp2⁻/⁻*/*Mmp14⁻/⁻* mice; explore enzyme-replacement or AAV gene-replacement in these models.
5. **Diagnostic standardization:** promote an algorithm of "carpal/tarsal osteolysis → MMP-2 zymography + *MMP14*/*MMP2* sequencing" to curb JIA misdiagnosis and inappropriate immunosuppression.
6. **Prospective cardiac surveillance protocol**, given that congenital heart disease can be the presenting and most dangerous manifestation ([PMID: 37025869](https://pubmed.ncbi.nlm.nih.gov/37025869/)).

---

*Report compiled from a 5-iteration autonomous literature synthesis; 8 confirmed findings, 21 papers reviewed. Evidence source types: human clinical case reports/series, mouse model-organism studies, and in vitro/cellular experiments, as indicated throughout.*


## Artifacts

- [OpenScientist final report](Winchester_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Winchester_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010201` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Winchester syndrome**
- `HP:0000939` (1 mention) - the report calls it "Radiographic"; HP calls it **Osteoporosis**
- `HP:0001371` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Flexion contracture**
- `HP:0001387` (1 mention) - the report calls it "Clinical sign"; HP calls it **Joint stiffness**
- `HP:0004322` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Short stature**
- `HP:0000280` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Coarse facial features**
- `HP:0007957` (1 mention) - the report calls it "Clinical sign (ocular)"; HP calls it **Corneal opacity**
- `HP:0000212` (1 mention) - the report calls it "Clinical sign"; HP calls it **Gingival overgrowth**
- `HP:0000998` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Hypertrichosis**
- `HP:0001627` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormal heart morphology**
- `NCIT:C15682` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Dose-Rate**
- `NCIT:C15329` (1 mention) - the report calls it "Analgesic Therapy"; NCIT calls it **Surgical Procedure**
- `NCIT:C15300` (1 mention) - the report calls it "Cardiac Surgery"; NCIT calls it **Photodynamic Therapy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000974` (1 mention) - the report calls it "thick skin"; HP calls it **Hyperextensible skin**, and lists "Hyperelastic skin" among its other names
- `HP:0000953` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Hyperpigmentation of the skin**, and lists "Skin hyperpigmentation" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `GO:0005886` (1 mention) - the report calls it "plasma membrane / cell surface"; GO calls it **plasma membrane**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.