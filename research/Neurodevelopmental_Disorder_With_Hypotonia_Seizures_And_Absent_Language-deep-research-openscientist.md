---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T04:40:48.188527'
end_time: '2026-10-23T04:56:36.794442'
duration_seconds: 948.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Hypotonia, Seizures, And Absent Language
  mondo_id: MONDO:0014995
  category: Mendelian
  causal_genes: HECW2
  omim_id: not recorded
  synonyms: NDHSAL; HECW2-related neurodevelopmental disorder; HECW2-related disorder
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 47
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 3
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0014995
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with hypotonia, seizures, and absent
      language
  - term_id: HP:0000486
    reported_labels:
    - Common
    ontology_label: Strabismus
  - term_id: HP:0000639
    reported_labels:
    - Common
    ontology_label: Nystagmus
  - term_id: HP:0001999
    reported_labels:
    - Common
    ontology_label: Abnormal facial shape
  - term_id: HP:0000252
    reported_labels:
    - Subset
    ontology_label: Microcephaly
  - term_id: HP:0001657
    reported_labels:
    - Rare
    ontology_label: Prolonged QT interval
  - term_id: CL:0000540
    reported_labels:
    - Suggested CL cell types:** neuron
    - neurons
    ontology_label: neuron
  - term_id: NCIT:C73043
    reported_labels:
    - Perampanel
    ontology_label: Barmastine
  - term_id: NCIT:C15401
    reported_labels:
    - Speech Therapy
    ontology_label: Retropubic Prostatectomy
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Hypotonia_Seizures_And_Absent_Language-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Hypotonia_Seizures_And_Absent_Language-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Hypotonia, Seizures, And Absent Language
- **MONDO ID:** MONDO:0014995 (if available)
- **Causal gene(s):** HECW2
- **OMIM:** not recorded
- **Synonyms:** NDHSAL; HECW2-related neurodevelopmental disorder; HECW2-related disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Hypotonia, Seizures, And Absent Language** covering all of the
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

# Neurodevelopmental Disorder With Hypotonia, Seizures, and Absent Language (NDHSAL): A Comprehensive Disease Profile

**Disease:** Neurodevelopmental Disorder With Hypotonia, Seizures, And Absent Language (NDHSAL)
**MONDO:** MONDO:0014995 · **OMIM:** #617268 · **Causal gene:** **HECW2** (HGNC:29853; NCBI Gene 57520; OMIM gene 617245)

---

## Summary

**Neurodevelopmental Disorder With Hypotonia, Seizures, and Absent Language (NDHSAL)** is an ultra-rare Mendelian neurodevelopmental disorder caused by variants in **HECW2** — **HECT, C2 and WW domain-containing E3 ubiquitin protein ligase 2** (alias **NEDL2**). HECW2 encodes a HECT-type E3 ubiquitin ligase that ubiquitinates and **stabilizes the transcription factor p73 (TP73)**, a crucial mediator of neurogenesis and brain development. The disorder was first defined by Berko et al. in 2017, who identified de novo deleterious missense variants in HECW2 in probands with intellectual disability, developmental delay, and hypotonia ([PMID: 27389779](https://pubmed.ncbi.nlm.nih.gov/27389779/)).

Clinically, NDHSAL presents with a **completely penetrant core triad** — neonatal/congenital **hypotonia** (with or without spasticity), **global developmental delay/intellectual disability**, and **developmental language disorder/absent language** (each 100% in the largest cohort) — accompanied by frequent **seizures (~61%)**, behavioural problems (88.9%), vision problems (83.9%), motor/coordination problems (75%), and gastrointestinal issues (70%) ([PMID: 34321324](https://pubmed.ncbi.nlm.nih.gov/34321324/)). A subset develop severe **developmental and epileptic encephalopathy (DEE)**, including West syndrome/infantile spasms and burst-suppression patterns, and rare cases show **cardiac long-QT syndrome** ([PMID: 37280227](https://pubmed.ncbi.nlm.nih.gov/37280227/)).

Two genetic mechanisms operate. The **predominant form is autosomal dominant**, driven by **de novo missense variants clustered in or near the C-terminal HECT catalytic domain (88.2%)** acting through a **dominant-negative** mechanism ([PMID: 34047014](https://pubmed.ncbi.nlm.nih.gov/34047014/)). A **rarer autosomal recessive** form arises from **biallelic loss-of-function/hypomorphic variants** in consanguineous families ([PMID: 35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/); [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/); [PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/)). HECW2 is one of the most constraint-intolerant genes in the genome (pLI ≈ 1, missense Z = 4.54). There is **no disease-modifying or gene-targeted therapy**; management is entirely **symptomatic** (antiseizure drugs, ACTH/ketogenic diet, perampanel for refractory DEE, rehabilitation, and cardiac surveillance). **No validated animal model and no biochemical biomarker** currently exist.

> **Evidence-base note:** This report synthesizes primary human clinical literature (case reports and one ~35-patient multicenter cohort) plus authoritative molecular/population databases (UniProt, NCBI Gene, Ensembl, gnomAD, ClinVar, HomoloGene) queried live during the investigation. NDHSAL is ultra-rare; most statements derive from aggregated small-cohort/case data, not large registries. Where a mechanistic step is inferred rather than experimentally demonstrated in the disease context, this is stated explicitly.

---

## Section 1 — Disease Information

NDHSAL is a Mendelian neurodevelopmental disorder characterized by the symptom triad embedded in its name. The information base is largely **individual-patient derived** (case reports and one multicenter cohort of ~35 individuals) aggregated into disease-level resources (OMIM, MONDO).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014995 |
| OMIM (phenotype) | #617268 |
| OMIM (gene) | 617245 (HECW2) |
| HGNC | 29853 |
| NCBI Gene | 57520 |
| Ensembl | ENSG00000138411 |
| UniProt | Q9P2P5 |
| Cytoband | 2q32.3 |

**Synonyms:** NDHSAL; HECW2-related neurodevelopmental disorder; HECW2-related disorder; neurodevelopmental disorder with hypotonia, seizures, and absent language. Gene aliases: **NEDL2**, NDHSAL.

ICD-10/ICD-11, MeSH and Orphanet do not carry a dedicated, disease-specific code for this ultra-rare entity; it is captured under broad neurodevelopmental/ID categories.

---

## Section 2 — Etiology

**Primary cause — genetic.** NDHSAL is monogenic, caused by pathogenic variants in **HECW2**. There is **no known environmental, infectious, toxic, or lifestyle cause**, and no gene–environment interaction has been described. No environmental or genetic **protective factors** are documented; given the de novo dominant mechanism, classical protective-allele epidemiology is not applicable.

**Genetic risk / causal variants.**
- **Autosomal dominant (most common):** heterozygous **de novo missense** variants, predominantly in or near the C-terminal HECT domain; dominant-negative effect ([PMID: 34047014](https://pubmed.ncbi.nlm.nih.gov/34047014/)).
- **Autosomal recessive (rare):** biallelic loss-of-function/hypomorphic variants (nonsense, splice, frameshift) in consanguineous families ([PMID: 35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/); [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/); [PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/)).

**Risk-factor context.** The only established risk factor for the recessive form is **consanguinity**. For the dominant form, **de novo mutation** (sporadic) is the rule, with advanced parental age a general — but unproven-specific — background risk for de novo events. No modifier genes have been identified.

---

## Section 3 — Phenotypes

Phenotype frequencies are drawn principally from the **35-case cohort of Acharya et al. 2022** ([PMID: 34321324](https://pubmed.ncbi.nlm.nih.gov/34321324/)) and the founding series ([PMID: 27389779](https://pubmed.ncbi.nlm.nih.gov/27389779/)).

| Phenotype | Type | Frequency | Suggested HPO term |
|---|---|---|---|
| Hypotonia (± spasticity) | Clinical sign | 100% | HP:0001252 (± HP:0001257) |
| Developmental delay / intellectual disability | Clinical/behavioural | 100% | HP:0001263 / HP:0001249 |
| Developmental language disorder / absent language | Behavioural/clinical | 100% | HP:0000750 / HP:0001344 |
| Behavioural problems | Behavioural | 88.9% | HP:0000708 |
| Vision problems (incl. cortical visual impairment) | Clinical sign | 83.9% | HP:0100704 / HP:0000505 |
| Motor coordination/movement problems | Clinical sign | 75% | HP:0001310 / HP:0002066 |
| Gastrointestinal issues (incl. GERD) | Clinical sign | 70% | HP:0011024 / HP:0002020 |
| Seizures | Clinical sign | 61.3% | HP:0001250 |
| Strabismus | Clinical sign | Common | HP:0000486 |
| Nystagmus | Clinical sign | Common | HP:0000639 |
| Dysmorphic facial features | Physical | Common | HP:0001999 |
| Microcephaly (severe cases) | Physical | Subset | HP:0000252 |
| Cerebral/cerebellar atrophy (severe cases) | Imaging | Subset | HP:0002059 / HP:0001272 |
| Long QT syndrome (rare) | Lab/ECG | Rare | HP:0001657 |

Berko et al. summarize the associated features: *"Other common features include seizures, strabismus, nystagmus, cortical visual impairment and dysmorphic facial features"* ([PMID: 27389779](https://pubmed.ncbi.nlm.nih.gov/27389779/)). Acharya et al. quantify penetrance: *"Clinical characterisation suggests complete penetrance for hypotonia with or without spasticity (100%), developmental delay/intellectual disability (100%) and developmental language disorder (100%). Other common features are behavioural problems (88.9%), vision problems (83.9%), motor coordination/movement (75%) and gastrointestinal issues (70%). Seizures were present in 61.3% of individuals"* ([PMID: 34321324](https://pubmed.ncbi.nlm.nih.gov/34321324/)).

**Characteristics.** Onset is **congenital/neonatal** (hypotonia) to **infancy** (seizures, developmental delay). Severity is **variable but generally moderate-to-severe**; the disease is **chronic and lifelong** rather than classically neurodegenerative, although DEE presentations can show early cerebral/cerebellar atrophy and drug-resistant epilepsy. **Quality-of-life impact** is substantial: absent/severely limited language, frequent non-ambulatory status, and intellectual disability imply lifelong dependence for daily functioning; no formal EQ-5D/SF-36 data exist for this rare disorder.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** **HECW2** (HGNC:29853; NCBI Gene 57520; Ensembl ENSG00000138411; cytoband 2q32.3; UniProt Q9P2P5, 1572 aa).

**Variant spectrum.** In the autosomal dominant form **all reported variants are missense**, and **88.2%** of likely-pathogenic/pathogenic variants lie in or near the C-terminal HECT domain ([PMID: 34321324](https://pubmed.ncbi.nlm.nih.gov/34321324/)). Four **recurrent variants** anchor the hotspot:

| Variant | Note |
|---|---|
| p.(Arg1191Gln) | ~22.9% of cases |
| p.(Arg1330Trp) | ~20% of cases |
| p.(Asn1199Lys) | Recurrent |
| p.(Phe1327Ser) | Recurrent |

Recessive variants include homozygous nonsense **p.Arg246\*** ([PMID: 35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/)), a homozygous **splice-donor** variant eliminating exon 22 (p.Leu1256_Trp1306del; ~60% reduced protein) ([PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/)), and a homozygous **frameshift p.Y1201Lfs\*7** predicted to undergo nonsense-mediated decay ([PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/)).

**Variant classification (ClinVar, live query of HECW2[gene], 732 records):** 4 Pathogenic, 11 Likely pathogenic, 7 Conflicting, 237 Uncertain significance, 122 Likely benign, 2 Benign. The vast majority are single-nucleotide variants; a handful are small deletions/duplications/CNVs.

**Allele frequency / constraint.** Pathogenic alleles are **essentially absent from gnomAD** (private de novo or rare biallelic events). HECW2 is among the most **constraint-intolerant** genes: gnomAD **pLI = 0.99999**, **LOEUF = 0.43**, **missense Z = 4.54**, **LoF Z = 7.32**, observed/expected missense = 0.76.

**Functional consequences.** The dominant missense variants act by a **dominant-negative** mechanism on the HECT catalytic machinery; recessive variants act by **loss of function** (NMD or reduced protein). No modifier genes, no disease-specific epigenetic signature, and no recurrent chromosomal abnormality are established (HECW2 is not detectable by karyotype and rarely implicated by CMA).

---

## Section 5 — Environmental Information

**Not applicable.** NDHSAL is a monogenic disorder. No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents are implicated in its causation or triggering. The only non-genetic contextual factor is **consanguinity**, which raises the probability of the recessive form.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A **HECW2 variant** (de novo heterozygous missense in the HECT domain, or biallelic LoF) **alters the E3 ubiquitin ligase activity** of HECW2/NEDL2.
   - *Dominant branch:* the HECT-domain missense product **results in** a **dominant-negative** enzyme that poisons normal ligase function (inferred from exclusively missense, HECT-clustered variants with no LoF in the AD form; [PMID: 34047014](https://pubmed.ncbi.nlm.nih.gov/34047014/)).
   - *Recessive branch:* biallelic LoF variants **lead to** **absent/reduced HECW2 protein** (NMD or ~60% reduced expression; [PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/); [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/)).
2. Altered HECW2 activity **leads to** **dysregulated ubiquitination and reduced stabilization of p73 (TP73)** (inferred from HECW2's established role as a p73-stabilizing ligase; [PMID: 27389779](https://pubmed.ncbi.nlm.nih.gov/27389779/); [PMID: 35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/)).
3. Reduced p73 stability/transcriptional activity **results in** **impaired p73-dependent programs of neuronal proliferation, apoptosis, and neuronal differentiation** essential for brain development ([PMID: 35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/)).
4. Disrupted neurodevelopment **leads to** **abnormal cortical/cerebellar development and neuronal network dysfunction** (manifest in severe cases as cerebral/cerebellar atrophy and epileptogenic networks).
5. These developmental and network abnormalities **result in** the **clinical phenotype**: hypotonia, developmental delay/ID, absent language, seizures/DEE, visual and GI dysfunction; and, via HECW2's broad substrate roles, occasional **cardiac long-QT** ([PMID: 37280227](https://pubmed.ncbi.nlm.nih.gov/37280227/)).

```
HECW2 variant
   │
   ├─(AD) dominant-negative missense ─┐
   │                                   ├─► dysregulated ubiquitination
   └─(AR) biallelic LoF → ↓protein ───┘        │
                                               ▼
                               ↓ p73 (TP73) stabilization / activity
                                               │
                                               ▼
              impaired neuronal proliferation / apoptosis / differentiation
                                               │
                                               ▼
                 abnormal brain development & network dysfunction
                                               │
                  ┌────────────────────────────┼───────────────────────────┐
                  ▼                             ▼                            ▼
            hypotonia, DD/ID            seizures / DEE              cortical visual,
            absent language        (atrophy in severe cases)      GI, cardiac (LQTS)
```

### Supporting molecular detail

- **Molecular pathways / protein function:** HECW2/NEDL2 is a **NEDD4-family HECT E3 ubiquitin ligase**. UniProt Q9P2P5 (1572 aa) has an N-terminal **C2 domain** (aa 167–301; membrane/Ca²⁺ targeting), two **WW domains** (aa 807–840 and 985–1018; PPxY substrate binding), and a C-terminal **HECT catalytic domain** (aa 1237–1572) with the catalytic cysteine (~C1540) forming the ubiquitin thioester intermediate. A defined **TP73-interaction region** spans aa 737–1068.
- Berko et al.: *"HECW2 is an ubiquitin ligase that stabilises p73, a crucial mediator of neurodevelopment and neurogenesis. This study implicates pathogenic genetic variants in HECW2 as potential causes of neurodevelopmental disorders in humans"* ([PMID: 27389779](https://pubmed.ncbi.nlm.nih.gov/27389779/)).
- A subsequent report: *"HECW2 encodes an E3 ubiquitin-protein ligase that stabilizes and enhances transcriptional activity of p73, a key factor regulating proliferation, apoptosis, and neuronal differentiation, which are together essential for proper brain development"* ([PMID: 35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/)).
- **Cellular processes:** Beyond p73, HECW2 regulates the **mitotic metaphase/anaphase transition**, interacting with FZR1/Cdh1 and being degraded by APC/C-Cdh1 at mitotic exit — consistent with a role in **cell-cycle control** relevant to neurogenesis.
- **Subcellular localization (GO cellular component):** cytoplasm (GO:0005737) and cytoskeleton/**mitotic spindle** (GO:0072686).
- **Suggested GO biological processes:** protein polyubiquitination (GO:0000209), protein stabilization (GO:0050821), nervous system development (GO:0007399), neuron differentiation (GO:0030182), regulation of mitotic cell cycle (GO:0007346).
- **Suggested CL cell types:** neuron (CL:0000540), glutamatergic neuron (CL:0000679), cerebellar Purkinje cell (CL:0000121), neural progenitor cell (CL:0011020).

**No metabolomic, proteomic, lipidomic, single-cell, spatial, or CRISPR-screen data specific to NDHSAL** are available; disease-variant characterization to date is in vitro/in silico.

---

## Section 7 — Anatomical Structures Affected

- **Primary organ / body system:** central nervous system (**brain**, UBERON:0000955; nervous system, UBERON:0001016). Involved regions include cerebral cortex (UBERON:0000956) and cerebellum (UBERON:0002037) — both showing atrophy in severe cases.
- **Secondary involvement:** eye/visual pathway (cortical visual impairment, strabismus, nystagmus; UBERON:0000970), gastrointestinal tract (GERD; UBERON:0001555), and **heart** (UBERON:0000948) in rare long-QT cases.
- **Tissue/cell level:** nervous tissue; affected cell populations include **neurons** (CL:0000540) and **neural progenitors** (CL:0011020); HECW2 is expressed predominantly in adult **brain, lung, and heart**.
- **Subcellular level (GO CC):** cytoplasm (GO:0005737), mitotic spindle (GO:0072686), nucleus-associated transcriptional regulation via p73.
- **Lateralization:** CNS involvement is **bilateral/symmetric**.

---

## Section 8 — Temporal Development

- **Onset:** congenital/neonatal **hypotonia**; infantile-onset **seizures** and **developmental delay**. Pattern is typically **chronic/insidious** developmental, with acute seizure presentations in DEE.
- **Progression:** Overall **static-to-slowly-evolving** encephalopathy — **not classically neurodegenerative**. However, severe DEE presentations evolve rapidly in infancy (e.g., burst-suppression → myoclonic → spasms; [PMID: 40879666](https://pubmed.ncbi.nlm.nih.gov/40879666/)) and may show early cerebral/cerebellar atrophy ([PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/)).
- **Course / duration:** **lifelong, chronic** disability.
- **Critical periods:** infancy/early childhood is the key window for seizure control and developmental intervention (physiotherapy, speech therapy).
- **Remission:** no spontaneous remission of the neurodevelopmental disorder; seizures may be partially controlled but are frequently **drug-resistant**.

---

## Section 9 — Inheritance and Population

- **Epidemiology:** ultra-rare; **no formal prevalence or incidence** estimates exist. The literature comprises case reports plus one multicenter cohort (~35 individuals; [PMID: 34321324](https://pubmed.ncbi.nlm.nih.gov/34321324/)), so **fewer than ~100 patients** are reported worldwide. No Orphanet prevalence class is established.
- **Inheritance:** predominantly **autosomal dominant** from **de novo heterozygous missense** variants (18/22 confirmed de novo in Acharya 2022). Rare **autosomal recessive** forms arise from biallelic LoF/hypomorphic variants in consanguineous families ([PMID: 35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/); [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/); [PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/)).
- **Penetrance:** **complete (100%)** for hypotonia, DD/ID, and language disorder.
- **Expressivity:** **variable**, including marked intrafamilial variability for a transmitted splice variant ([PMID: 40879666](https://pubmed.ncbi.nlm.nih.gov/40879666/)).
- **Anticipation:** none (no repeat-expansion mechanism).
- **Mosaicism:** germline mosaicism is plausible (as for other de novo disorders) but not specifically documented.
- **Founder effects / consanguinity:** no founder allele; **consanguinity** underlies recessive cases.
- **Carrier frequency:** not established; pathogenic alleles are essentially absent from population databases.
- **Sex ratio:** no clear sex predilection. **Geographic distribution:** worldwide, no endemic region.

---

## Section 10 — Diagnostics

**Molecular diagnosis is definitive.** Because variants are private de novo missense (or rare biallelic), **trio whole-exome sequencing (WES)** is the highest-yield test (18/22 de novo in Acharya 2022; trio-WES diagnoses also in [PMID: 40469502](https://pubmed.ncbi.nlm.nih.gov/40469502/)). **Whole-genome sequencing (WGS)** and **multigene epilepsy/ID/DEE NGS panels** are alternatives; **single-gene testing** supports familial/cascade confirmation. HECW2 is **not detectable by karyotype** and is **rarely implicated by chromosomal microarray** (occasional 2q32.3 CNVs in ClinVar).

**Variant interpretation challenge:** ClinVar shows only **4 Pathogenic + 11 Likely pathogenic** against **237 VUS** and 122 Likely benign (732 records), underscoring the burden of uncertain variants and the value of de novo status and HECT-domain localization in ACMG/AMP classification.

**Supportive diagnostics:**
- **EEG** to characterize seizures (burst-suppression, hypsarrhythmia/spasms; [PMID: 40879666](https://pubmed.ncbi.nlm.nih.gov/40879666/), [PMID: 40705299](https://pubmed.ncbi.nlm.nih.gov/40705299/)).
- **Brain MRI** (cerebral/cerebellar atrophy, nonspecific anomalies; [PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/), [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/)).
- **Ophthalmologic assessment** (cortical visual impairment, strabismus, nystagmus).
- **ECG** for QT monitoring ([PMID: 37280227](https://pubmed.ncbi.nlm.nih.gov/37280227/)).

**No specific biochemical/metabolite biomarker** exists; there is no newborn-screening test. **Differential diagnosis** includes other genetic hypotonia–DEE–ID syndromes; distinction is made by gene identification.

---

## Section 11 — Outcome / Prognosis

- **Survival/mortality:** no published survival statistics. The disorder is **not intrinsically lethal**, but severe DEE and **rare cardiac long-QT** ([PMID: 37280227](https://pubmed.ncbi.nlm.nih.gov/37280227/)) can be **life-threatening**.
- **Morbidity/disability:** high and lifelong — **absent/severely limited language**, intellectual disability, and frequently **non-ambulatory** status, implying dependence for activities of daily living.
- **Course:** chronic, largely static-to-slowly-evolving; **drug-resistant epilepsy** worsens prognosis in a subset.
- **Prognostic factors:** HECT-domain variants correlate with cortical visual impairment and GI issues; **seizures were observed only with variants in or near the HECT domain**. Severe/DEE presentations with early atrophy portend worse developmental outcomes.
- **No validated prognostic biomarker** exists.

---

## Section 12 — Treatment

**There is no disease-modifying or gene-targeted therapy. Management is entirely symptomatic and supportive.**

| Domain | Intervention | Evidence | NCIT suggestion |
|---|---|---|---|
| Epilepsy (general) | Antiseizure medications; often drug-resistant | [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/) | NCIT:C264 (Anticonvulsant Agent) |
| West syndrome / spasms | ACTH + modified Atkins (ketogenic-type) diet | [PMID: 40705299](https://pubmed.ncbi.nlm.nih.gov/40705299/) | NCIT:C2366 (ACTH); NCIT:C92948 (Ketogenic Diet) |
| Refractory DEE | Perampanel (AMPA-receptor antagonist), personalized | [PMID: 40879666](https://pubmed.ncbi.nlm.nih.gov/40879666/) | NCIT:C73043 (Perampanel) |
| Hypotonia/motor | Physiotherapy | — | NCIT:C15415 (Physical Therapy) |
| Language | Speech therapy | — | NCIT:C15401 (Speech Therapy) |
| Vision | Ophthalmologic management | — | — |
| GI (GERD) | Reflux management | [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/) | — |
| Cardiac | QT surveillance / LQTS management | [PMID: 37280227](https://pubmed.ncbi.nlm.nih.gov/37280227/) | — |

ACTH plus ketogenic-type diet was reported with benefit in pharmacoresistant HECW2-related West syndrome: *"We describe an infant with a pathogenic HECW2 gene variation who presented with excessive floppiness, global delay, tonic eye deviations, and epileptic spasms treated with a combination of adrenocorticotropic hormone and modified Atkin's diet"* ([PMID: 40705299](https://pubmed.ncbi.nlm.nih.gov/40705299/)). Perampanel exemplifies personalized strategy: *"It also underscores the importance of personalized therapeutic strategies, as demonstrated by the use of perampanel in this patient"* ([PMID: 40879666](https://pubmed.ncbi.nlm.nih.gov/40879666/)).

**No pharmacogenomic, gene, cell, RNA, targeted, or immunotherapy** is established, and **no registered clinical trials** specific to NDHSAL exist.

---

## Section 13 — Prevention

Because NDHSAL is monogenic with no environmental contribution, prevention is **genetic/reproductive**, not public-health.
- **Primary prevention:** none for the dominant de novo form (sporadic, unpredictable).
- **Genetic counseling:** central — recurrence risk is low for de novo AD cases (but germline mosaicism cannot be fully excluded), and **25%** for biallelic recessive families.
- **Prenatal / preimplantation genetic testing** is possible once a familial variant is known (especially in consanguineous/recessive families).
- **Cascade testing** of relatives for known familial variants.
- **Tertiary prevention:** minimizing complications via seizure control, cardiac QT surveillance, nutritional/GI management, and developmental therapies.
- **No immunization, population screening, or behavioural/environmental intervention** is applicable.

---

## Section 14 — Other Species / Natural Disease

HECW2 is **evolutionarily conserved** with one-to-one orthologs across vertebrates (HomoloGene group 66192):

| Species | Gene | NCBI Gene ID |
|---|---|---|
| Mouse (*Mus musculus*) | Hecw2 | 329152 |
| Rat (*Rattus norvegicus*) | Hecw2 | 316395 |
| Zebrafish (*Danio rerio*) | hecw2 | 100331355 |
| Chicken (*Gallus gallus*) | HECW2 | 424050 |

Additional orthologs exist in dog, cow, macaque, and chimpanzee. HECW2/NEDL2 belongs to the **NEDD4/HECT E3 ligase family**. **No naturally occurring NDHSAL-equivalent disease** is documented in companion animals or wildlife (no OMIA entry equivalent to the human disorder), and there is **no zoonotic or transmission dimension** (it is a genetic disorder).

---

## Section 15 — Model Organisms

**No published knockout/knock-in mouse, rat, or zebrafish model specifically recapitulates the human NDHSAL phenotype as of this review.** The founding functional studies defined NEDL2 as a **p73-stabilizing ubiquitin ligase** in cell systems and a regulator of the **APC/C-Cdh1 mitotic transition**, i.e., **in vitro/cell-based** characterization. Disease-variant work to date is in vitro/in silico (e.g., ~60% reduced protein for the recessive splice variant, [PMID: 35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/); NMD prediction for the frameshift, [PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/)).

**Model resources for future work:** MGI/IMPC/KOMP (mouse Hecw2, Gene 329152), RGD (rat), ZFIN (zebrafish hecw2). Conserved orthology makes mouse and zebrafish strong candidate systems. **Limitation:** absence of any validated model means genotype–phenotype mechanisms (dominant-negative vs. LoF) and candidate therapeutics cannot yet be tested in vivo.

---

## Mechanistic Model / Interpretation

The unifying model is **p73 dysregulation downstream of a defective HECT ubiquitin ligase**. HECW2 normally ubiquitinates and **stabilizes p73**, amplifying a transcriptional program (proliferation, apoptosis, neuronal differentiation) that brain development depends upon. Two mutational routes converge on reduced effective p73 activity:

```
                 ┌──────────────── AD (common) ────────────────┐
  De novo missense in HECT domain → dominant-negative ligase ──┐
                                                                ├─► ↓ functional p73 program
  Biallelic LoF (nonsense/splice/frameshift) → ↓/absent HECW2 ─┘
                 └──────────────── AR (rare) ──────────────────┘
                                   │
                                   ▼
                 impaired neurodevelopment → NDHSAL triad
```

The **genotype–phenotype correlation** is informative: variants in/near the HECT domain are associated with cortical visual impairment and GI issues, and **seizures occur only with HECT-region variants**, implying that the catalytic core is the most phenotypically consequential region ([PMID: 34321324](https://pubmed.ncbi.nlm.nih.gov/34321324/)). The extreme population constraint (pLI ≈ 1, missense Z = 4.54) independently corroborates that both dosage reduction and missense perturbation of HECW2 are strongly deleterious — fully consistent with the observed AD (dominant-negative) and AR (LoF) mechanisms. Yanagishita et al. articulate the dominant branch directly: *"All HECW2 variants, including those that were previously reported, are missense, and no loss-of-function variants have been identified. Most of the identified variants are located around the HECT domain. These findings suggest that the dominant negative effects of missense variants around the HECT domain may be the mechanism underlying HECW2-related disorder"* ([PMID: 34047014](https://pubmed.ncbi.nlm.nih.gov/34047014/)). The recessive branch is explicitly distinguished: *"This frameshift variant likely results in nonsense-mediated decay (NMD) of the mRNA, suggesting a loss-of-function mechanism distinct from the mechanism implicated in missense variants that causing the disease with autosomal dominant inheritance"* ([PMID: 40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [27389779](https://pubmed.ncbi.nlm.nih.gov/27389779/) | De novo missense variants in HECW2 (Berko 2017) | Disease-defining paper; names HECW2 as causal; p73-stabilizing ligase; lists core/associated phenotypes |
| [34321324](https://pubmed.ncbi.nlm.nih.gov/34321324/) | Delineating genotype/phenotype spectrum (Acharya 2022) | 35-case cohort; penetrance 100% for triad; HECT hotspot 88.2%; seizures 61.3%; genotype–phenotype correlation |
| [34047014](https://pubmed.ncbi.nlm.nih.gov/34047014/) | HECW2-related disorder in 4 Japanese patients | Dominant-negative, HECT-clustered missense; no LoF in AD form |
| [35487419](https://pubmed.ncbi.nlm.nih.gov/35487419/) | Homozygous nonsense HECW2 variant | Recessive form; p.Arg246\*; p73/brain-development mechanism |
| [35753050](https://pubmed.ncbi.nlm.nih.gov/35753050/) | First splicing variant, AR inheritance | AR splice variant; ~60% reduced protein (partial LoF); drug-resistant epilepsy, GERD, MRI anomalies |
| [40812465](https://pubmed.ncbi.nlm.nih.gov/40812465/) | AR frameshift broadens spectrum | p.Y1201Lfs\*7; NMD/LoF mechanism distinct from AD missense; microcephaly, atrophy |
| [37280227](https://pubmed.ncbi.nlm.nih.gov/37280227/) | Novel variant, congenital long QT | Cardiac LQTS comorbidity (p.Leu1448Ser) |
| [40705299](https://pubmed.ncbi.nlm.nih.gov/40705299/) | HECW2 as a cause of West syndrome | ACTH + modified Atkins diet management |
| [40879666](https://pubmed.ncbi.nlm.nih.gov/40879666/) | Rapid electroclinical evolution in DEE | Perampanel; familial transmission; intrafamilial variability |
| [40469502](https://pubmed.ncbi.nlm.nih.gov/40469502/) | Novel variant, Chinese girl | Trio-WES diagnosis; DLD, hypotonia |

Context papers on HECW2 substrate biology in non-neural settings (e.g., NSCLC via SCNN1A/AKT-mTOR, [PMID: 42537707](https://pubmed.ncbi.nlm.nih.gov/42537707/); ATR degradation after lamin misexpression, [PMID: 22382637](https://pubmed.ncbi.nlm.nih.gov/22382637/); infantile hemangioma glycolysis, [PMID: 40520873](https://pubmed.ncbi.nlm.nih.gov/40520873/)) confirm HECW2 is a broadly acting K48-linked E3 ligase but are **not disease-specific** to NDHSAL.

---

## Limitations and Knowledge Gaps

1. **Small evidence base:** fewer than ~100 reported patients; no prevalence/incidence, survival, or validated QoL data.
2. **No in vivo model:** the dominant-negative vs. LoF mechanisms are inferred from variant distribution and in vitro data, not demonstrated in an animal model.
3. **Direct p73-pathway link unproven in patient neurons:** the p73 mechanism is extrapolated from cell-line biology; patient-derived neuronal/organoid confirmation is lacking.
4. **Variant interpretation burden:** 237 VUS in ClinVar; functional assays for ligase activity are not routine.
5. **No biomarker and no disease-modifying therapy;** management evidence is anecdotal (single cases).
6. **Recessive form rare and under-characterized;** genotype–phenotype rules for biallelic variants are preliminary.

---

## Proposed Follow-up Experiments / Actions

1. **Generate in vivo models:** create *Hecw2* knock-in mice/zebrafish carrying recurrent HECT-domain missense alleles (e.g., p.Arg1191Gln, p.Arg1330Trp) and biallelic LoF alleles to test dominant-negative vs. LoF mechanisms and recapitulate hypotonia/seizures.
2. **Patient-derived iPSC neurons/organoids:** quantify p73 stability and downstream transcriptional targets in mutant vs. control neurons; test whether p73 activity can be pharmacologically restored.
3. **Functional ligase assays:** establish a standardized in vitro ubiquitination/auto-ubiquitination assay to reclassify the 237 VUS and confirm dominant-negative behavior of HECT-domain missenses.
4. **Natural history registry:** build an international registry to estimate prevalence, define developmental trajectories, seizure outcomes, and cardiac risk, and to standardize QoL assessment.
5. **Cardiac phenotyping:** systematic ECG screening across the cohort to determine the true frequency of QT prolongation and inform surveillance guidelines.
6. **Therapeutic screening:** once a model exists, screen antiseizure agents (including perampanel) and p73-pathway modulators for genotype-specific efficacy.

---

*Report compiled from 5 investigation iterations, 11 confirmed findings, and 18 reviewed papers. Evidence source types span human clinical case reports/cohorts, in vitro/cell-based functional studies, and computational/population-genetics analyses (gnomAD, ClinVar, UniProt, HomoloGene).*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Hypotonia_Seizures_And_Absent_Language-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Hypotonia_Seizures_And_Absent_Language-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014995` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with hypotonia, seizures, and absent language**
- `HP:0000486` (1 mention) - the report calls it "Common"; HP calls it **Strabismus**
- `HP:0000639` (1 mention) - the report calls it "Common"; HP calls it **Nystagmus**
- `HP:0001999` (1 mention) - the report calls it "Common"; HP calls it **Abnormal facial shape**
- `HP:0000252` (1 mention) - the report calls it "Subset"; HP calls it **Microcephaly**
- `HP:0001657` (1 mention) - the report calls it "Rare"; HP calls it **Prolonged QT interval**
- `CL:0000540` (2 mentions) - the report calls it "Suggested CL cell types:** neuron", "neurons"; CL calls it **neuron**
- `NCIT:C73043` (1 mention) - the report calls it "Perampanel"; NCIT calls it **Barmastine**
- `NCIT:C15401` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Retropubic Prostatectomy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0000209` (1 mention) - the report calls it "Suggested GO biological processes:** protein polyubiquitination"; GO calls it **protein polyubiquitination**
- `CL:0011020` (2 mentions) - the report calls it "neural progenitors"; CL calls it **neural progenitor cell**
- `NCIT:C15415` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Hyperthermia Treatment**, and lists "Hyperthermia Therapy" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000540` - called "Suggested CL cell types:** neuron", "neurons"