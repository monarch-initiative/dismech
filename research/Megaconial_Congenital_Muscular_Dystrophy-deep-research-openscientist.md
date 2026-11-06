---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T22:35:05.796602'
end_time: '2026-10-28T22:49:24.457946'
duration_seconds: 858.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Megaconial Congenital Muscular Dystrophy
  mondo_id: MONDO:0011246
  category: Mendelian
  causal_genes: CHKB
  omim_id: not recorded
  synonyms: not recorded
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
  quotes_checked: 9
  quotes_valid: 9
  relevance_assessed: 25
  on_topic: 23
  validator_version: 0.4.0
term_validation:
  total_terms: 36
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 2
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0011246
    reported_labels:
    - MONDO
    ontology_label: megaconial type congenital muscular dystrophy
  - term_id: HP:0001263
    reported_labels:
    - Static/slowly progressive
    ontology_label: Global developmental delay
  - term_id: HP:0010864
    reported_labels:
    - Static
    ontology_label: Severe intellectual disability
  - term_id: HP:0003701
    reported_labels:
    - Slowly progressive/variable
    ontology_label: Proximal muscle weakness
  - term_id: HP:0003202
    reported_labels:
    - Progressive
    ontology_label: Skeletal muscle atrophy
  - term_id: HP:0000252
    reported_labels:
    - Static
    ontology_label: Microcephaly
  - term_id: HP:0001999
    reported_labels:
    - Static
    ontology_label: Abnormal facial shape
  - term_id: HP:0001644
    reported_labels:
    - Progressive
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0003201
    reported_labels:
    - Episodic
    ontology_label: Rhabdomyolysis
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Megaconial_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Megaconial_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Megaconial Congenital Muscular Dystrophy
- **MONDO ID:** MONDO:0011246 (if available)
- **Causal gene(s):** CHKB
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Megaconial Congenital Muscular Dystrophy** covering all of the
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

# Megaconial Congenital Muscular Dystrophy (CHKB): Comprehensive Disease Characterization Report

**MONDO ID:** MONDO:0011246 · **OMIM:** 602541 · **Causal gene:** *CHKB* (choline kinase beta, HGNC:1938, chromosome 22q13.33) · **Category:** Mendelian, autosomal recessive

---

## Summary

**Megaconial Congenital Muscular Dystrophy (MDCMC / MCMD)** is an ultra-rare autosomal-recessive multisystem disorder caused by **biallelic loss-of-function variants in *CHKB*, the gene encoding choline kinase beta**. CHKB catalyzes the first, rate-limiting step of the Kennedy (CDP-choline) pathway for *de novo* biosynthesis of **phosphatidylcholine (PC)** — the most abundant phospholipid in eukaryotic membranes. Loss of CHKB activity disrupts PC-dependent mitochondrial membrane homeostasis and produces the disease's pathognomonic feature: **peripherally enlarged "megaconial" (giant) mitochondria with central mitochondrial depletion** on muscle biopsy. The causal gene was identified by Mitsuhashi et al. in 2011 ([PMID: 21665002](https://pubmed.ncbi.nlm.nih.gov/21665002/)), building on the 1998 morphological description of a novel congenital muscular dystrophy with mitochondrial structural abnormalities ([PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/)).

Clinically, the core phenotype comprises **congenital-to-early-childhood muscular dystrophy** (hypotonia, proximal weakness, muscle wasting, mildly elevated creatine kinase), **global developmental delay with severe intellectual disability and/or autistic features**, **ichthyosis-like skin changes**, and **dilated cardiomyopathy in approximately half of patients** — the leading cause of death. The phenotypic spectrum is broad and allelic, ranging from severe congenital dystrophy with profound intellectual disability to an adult-onset, non-progressive proximal myopathy with normal cognition ("Proximal Myopathy with Focal Depletion of Mitochondria"). Mechanistically, the PC-synthetic defect leads to mitochondrial membrane dysfunction, reduced mitochondrial fission (DRP1/MFF/FIS1), impaired fatty-acid β-oxidation, increased mitophagy, and bioenergetic failure (reduced Krebs-cycle intermediates and ATP).

No disease-modifying therapy is yet approved; management is **supportive** — physiotherapy, developmental/educational support, cardiac surveillance and treatment of dilated cardiomyopathy up to heart transplantation, and targeted dermatologic therapy (ustekinumab responded in one patient). The *Chkb*-deficient **rostrocaudal muscular dystrophy (rmd) mouse** faithfully recapitulates the disease and has enabled proof-of-concept **AAV6-*CHKB* gene-replacement therapy** and **CHKA (paralog) upregulation**, both of which rescue the dystrophic phenotype and now constitute the most promising preclinical therapeutic routes.

---

## Section 1 — Disease Information

**Overview.** Megaconial Congenital Muscular Dystrophy is a form of congenital muscular dystrophy defined morphologically by giant ("megaconial") mitochondria at the periphery of muscle fibers with central sarcoplasmic mitochondrial depletion, and genetically by biallelic *CHKB* mutations. It was first delineated as a distinct clinical-pathological entity by Nishino et al. in 1998 in four patients from three unrelated families who had merosin-positive congenital muscular dystrophy with marked mental retardation ([PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/)). The genetic cause (*CHKB*) was established in 2011 ([PMID: 21665002](https://pubmed.ncbi.nlm.nih.gov/21665002/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0011246 |
| OMIM | 602541 (Muscular dystrophy, congenital, megaconial type / MDCMC) |
| Gene | *CHKB* (HGNC:1938; gene OMIM 612395; Ensembl ENSG00000100288) |
| Chromosomal locus | 22q13.33 (head-to-head with *CPT1B*) |
| Orphanet | Megaconial congenital muscular dystrophy |
| ICD-10 | G71.0 (muscular dystrophy, approximate) |
| MeSH | Muscular Dystrophies (no disease-specific term) |

**Synonyms / alternative names:** Megaconial type congenital muscular dystrophy; Muscular dystrophy, congenital, megaconial type (MDCMC); CHKB-related congenital muscular dystrophy; Congenital muscular dystrophy, megaconial type; and the allelic **Proximal Myopathy with Focal Depletion of Mitochondria** (milder adult-onset form) ([PMID: 26782016](https://pubmed.ncbi.nlm.nih.gov/26782016/)).

**Data source type.** The knowledge here is derived from **aggregated disease-level resources and published individual-patient case series/reports** (OMIM, Orphanet, and PubMed primary literature), not from electronic health records. Reported cohorts are small (largest series n=15; Iranian series n=13).

---

## Section 2 — Etiology

**Primary cause — genetic.** The disease is caused exclusively by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *CHKB***. Mitsuhashi et al. identified such mutations in 15 individuals with the characteristic clinical and morphological phenotype; in three individuals with nonsense mutations, choline kinase enzyme activity was undetectable and phosphatidylcholine levels were decreased ([PMID: 21665002](https://pubmed.ncbi.nlm.nih.gov/21665002/)):

> "we have identified homozygous or compound heterozygous mutations in the gene encoding choline kinase beta (CHKB)... In muscle of three affected individuals with nonsense mutations, choline kinase activities were undetectable, and phosphatidylcholine levels were decreased."

**Genetic risk factors.** The causal variants are the sole genetic risk factor; there are no established susceptibility loci or proven human modifier genes. **Consanguinity** is a major contributing circumstance: most reported patients are homozygous (40 of 49 reported by 2023), consistent with autosomal-recessive inheritance and founder/consanguinity effects in populations with high rates of consanguineous marriage (Turkey, Iran, India, Japan, China) ([PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/); [PMID: 37393748](https://pubmed.ncbi.nlm.nih.gov/37393748/)).

**Environmental risk factors / protective factors / gene-environment interactions.** None are established. As a monogenic Mendelian disorder, environmental exposures, lifestyle, toxins, and infectious agents are **not applicable** as causes. No protective genetic alleles or environmental protective factors are documented. One molecularly relevant note: the paralogous gene **CHKA** can partially substitute for CHKB function (basis of a therapeutic strategy), which is a molecular redundancy rather than a gene-environment interaction.

---

## Section 3 — Phenotypes

The best-characterized phenotype data come from the 15-patient series of Haliloglu et al. ([PMID: 26067811](https://pubmed.ncbi.nlm.nih.gov/26067811/)); additional features come from other series and case reports.

> "Core clinical phenotype included global developmental delay prominent in gross-motor and language domains, severe intellectual disability (ID), and/or muscle weakness in all cases" ([PMID: 26067811](https://pubmed.ncbi.nlm.nih.gov/26067811/)).

| Phenotype | Type | Frequency (where reported) | Onset | Course | Suggested HPO |
|---|---|---|---|---|---|
| Global developmental delay | Clinical sign | 15/15 (100%) | Neonatal–infancy | Static/slowly progressive | HP:0001263 |
| Severe intellectual disability | Clinical sign | Majority (core feature) | Childhood | Static | HP:0010864 |
| Muscle weakness (proximal) | Clinical sign | All cases (core) | Congenital–childhood | Slowly progressive/variable | HP:0003701 |
| Muscle wasting / atrophy | Physical manifestation | Frequent | Childhood | Progressive | HP:0003202 |
| Hypotonia | Clinical sign | Frequent | Neonatal | — | HP:0001252 |
| Elevated serum creatine kinase (mild) | Laboratory abnormality | 12/15 (80%) | — | — | HP:0003236 |
| Ichthyosis-like / dry skin changes | Physical manifestation | 11/15 (73%) | Childhood | Chronic | HP:0008064 / HP:0000958 |
| Microcephaly | Physical manifestation | 6/15 (40%) | Congenital | Static | HP:0000252 |
| Dysmorphic features | Physical manifestation | 7/15 (47%) | Congenital | Static | HP:0001999 |
| Dilated cardiomyopathy | Clinical sign | ~50% overall; 2/15 in series | Variable (childhood–adult) | Progressive | HP:0001644 |
| Congenital heart defect | Clinical sign | 3/15 (20%) | Congenital | — | HP:0001627 |
| Autistic behavior / ASD features | Behavioral | Subset | Childhood | — | HP:0000729 |
| Rhabdomyolysis susceptibility | Clinical sign | Mild (allelic) form | Adult | Episodic | HP:0003201 |

**Severity and progression.** Highly variable, including intrafamilial variability ([PMID: 26067811](https://pubmed.ncbi.nlm.nih.gov/26067811/)). The dilated cardiomyopathy is the most clinically severe feature: "Clinical characteristics are delayed motor development, intellectual disability and dilated cardiomyopathy in half of reported cases" ([PMID: 26855408](https://pubmed.ncbi.nlm.nih.gov/26855408/)).

**Neurobehavioral overlap.** CHKB disease can mimic **atypical Rett syndrome** (developmental regression, hand stereotypies) ([PMID: 33712684](https://pubmed.ncbi.nlm.nih.gov/33712684/)) and present as **autism spectrum disorder** ([PMID: 33623274](https://pubmed.ncbi.nlm.nih.gov/33623274/)) — important differential-diagnosis considerations.

**Quality of life.** No formal EQ-5D/SF-36/PROMIS studies exist. Qualitatively, the combination of severe intellectual disability, motor disability, and cardiac disease produces major impairment of daily functioning and lifelong dependency in the severe-end majority; the mild allelic form permits near-normal function.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *CHKB* (choline kinase beta), gene OMIM 612395; disease OMIM 602541. CHKB catalyzes **ATP + choline → ADP + phosphocholine** (EC 2.7.1.32), the first committed step of PC synthesis via the Kennedy pathway, and also phosphorylates ethanolamine. The protein functions as a homodimer/heterodimer with CHKA. Relevant CHEBI entities: choline, phosphocholine, phosphatidylcholine, ATP.

**Pathogenic variants.** All classes of loss-of-function variants are reported:

| Variant type | Example(s) | Reference |
|---|---|---|
| Nonsense | Nonsense mutations with undetectable choline kinase activity | [PMID: 21665002](https://pubmed.ncbi.nlm.nih.gov/21665002/) |
| Frameshift | c.598delC (p.Q200Rfs*11) | [PMID: 39465137](https://pubmed.ncbi.nlm.nih.gov/39465137/) |
| Missense | c.1031G>A (p.R344Q); c.1060G>C (p.Gly354Arg); c.263C>T; c.950T>A | [PMID: 27123443](https://pubmed.ncbi.nlm.nih.gov/27123443/); [PMID: 36175989](https://pubmed.ncbi.nlm.nih.gov/36175989/); [PMID: 26782016](https://pubmed.ncbi.nlm.nih.gov/26782016/) |
| Splice-site | c.1031+3G>C; c.818+1G>A; c.1031+1G>A; c.225-2A>T; c.448-56_29del (intronic) | [PMID: 25740612](https://pubmed.ncbi.nlm.nih.gov/25740612/); [PMID: 33623274](https://pubmed.ncbi.nlm.nih.gov/33623274/); [PMID: 35707590](https://pubmed.ncbi.nlm.nih.gov/35707590/); [PMID: 36175989](https://pubmed.ncbi.nlm.nih.gov/36175989/) |
| Synonymous→splicing | c.843T>C (p.Phe281=) causing exon 8 skipping; c.581G>A causing exon 4 deletion | [PMID: 41026188](https://pubmed.ncbi.nlm.nih.gov/41026188/) |
| Structural / UPD | Large heterozygous deletion with uniparental disomy masquerading as homozygosity | [PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/) |

**Important molecular lesson:** Several pathogenic *CHKB* variants act through **aberrant splicing**, including intronic and synonymous changes that escape standard coding-sequence analysis; RNA studies (RT-PCR from muscle or lymphocytes) are often needed to prove pathogenicity ([PMID: 41026188](https://pubmed.ncbi.nlm.nih.gov/41026188/); [PMID: 25740612](https://pubmed.ncbi.nlm.nih.gov/25740612/); [PMID: 36175989](https://pubmed.ncbi.nlm.nih.gov/36175989/)). Truncated proteins are frequently degraded by nonsense-mediated decay.

**Variant classification (ACMG/AMP):** Reported variants are predominantly **pathogenic / likely pathogenic** with functional evidence (loss of enzyme activity, reduced DRP1, splicing assays). **Functional consequence:** uniform **loss of function** (no gain-of-function or dominant-negative mechanism).

**Allele frequency.** Causal alleles are ultra-rare / private in gnomAD, consistent with the disorder's rarity and recessive inheritance; many are population- or family-specific.

**Somatic vs germline.** Exclusively **germline**, biallelic.

**Modifier genes / epigenetics / chromosomal abnormalities.** No human modifier genes are confirmed. Of note, *CHKB* lies in a shared epigenetic regulatory domain head-to-head with *CPT1B* (carnitine palmitoyltransferase 1B), a key fatty-acid-oxidation gene; their coordinated regulation is relevant to the FAO defect ([PMID: 33058877](https://pubmed.ncbi.nlm.nih.gov/33058877/)). No recurrent large chromosomal abnormalities beyond the single UPD/deletion case ([PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/)).

---

## Section 5 — Environmental Information

**Not applicable as cause.** Megaconial CMD is a monogenic disorder with no established environmental, lifestyle, toxic, or infectious contributors. No dietary, occupational, or exposure risk or protective factors are documented. Phosphatidylcholine/choline nutritional supplementation has been considered conceptually (given the biochemical defect) but is **not established** to modify disease, because the defect is in the enzymatic kinase step rather than in choline availability.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function *CHKB* mutation** → **leads to** loss of choline kinase beta enzyme activity in skeletal and cardiac muscle (demonstrated: choline kinase activity undetectable in nonsense-mutation muscle) ([PMID: 21665002](https://pubmed.ncbi.nlm.nih.gov/21665002/)).
2. Loss of CHKB activity → **results in** a block at the first step of the Kennedy pathway (choline → phosphocholine) → **decreased de novo phosphatidylcholine (PC) synthesis** in muscle (demonstrated in patient muscle) ([PMID: 21665002](https://pubmed.ncbi.nlm.nih.gov/21665002/)).
3. Reduced PC supply → **leads to** disturbed **mitochondrial membrane phospholipid homeostasis** (PC is a predominant mitochondrial membrane phospholipid) ([PMID: 26855408](https://pubmed.ncbi.nlm.nih.gov/26855408/); [PMID: 22024749](https://pubmed.ncbi.nlm.nih.gov/22024749/)).
4. Membrane dysfunction → **results in** abnormal mitochondrial morphology: **peripheral giant ("megaconial") mitochondria with central sarcoplasmic depletion** — the pathognomonic lesion ([PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/)).
   - **Branch 4a (fission defect):** reduced mitochondrial fission proteins **DRP1, MFF, FIS1** → impaired mitochondrial fission → enlarged mitochondria (demonstrated in patient skeletal muscle cells and tissue) ([PMID: 34518586](https://pubmed.ncbi.nlm.nih.gov/34518586/); [PMID: 36175989](https://pubmed.ncbi.nlm.nih.gov/36175989/)).
   - **Branch 4b (mitophagy):** PC-synthetic defect → **increased mitophagy / mitochondrial dysfunction** ([PMID: 22024749](https://pubmed.ncbi.nlm.nih.gov/22024749/)).
5. Mitochondrial dysfunction → **leads to** **impaired fatty-acid β-oxidation**, with shunting of fatty acids into triacylglycerol and decreased PPAR/target-gene expression (demonstrated in *Chkb* mouse; notably PC level is not significantly altered in that model, implicating a temporal metabolic mechanism) ([PMID: 35322809](https://pubmed.ncbi.nlm.nih.gov/35322809/)).
6. Impaired β-oxidation + reduced OXPHOS (mild complex decreases, incomplete complex V assembly) → **results in** **bioenergetic failure**: decreased phosphonucleotides, Krebs-cycle intermediates, and ATP ([PMID: 34518586](https://pubmed.ncbi.nlm.nih.gov/34518586/); [PMID: 26855408](https://pubmed.ncbi.nlm.nih.gov/26855408/)).
7. Energy failure + membrane instability → **leads to** myofiber degeneration/necrosis and regeneration (dystrophic pathology), plus **downregulation of cytoskeletal and contractile proteins** (proteomics: 218 differentially abundant proteins, mostly reduced) ([PMID: 42449274](https://pubmed.ncbi.nlm.nih.gov/42449274/); [PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/)).
8. → **results in** the clinical manifestations: **skeletal muscle weakness/dystrophy**, **dilated cardiomyopathy** (cardiac hypertrophy and arrhythmia predisposition in mouse), **CNS dysfunction** (intellectual disability, developmental delay — mechanism inferred, less well demonstrated), and **ichthyosis-like skin** (inferred from PC's role in epidermal barrier lipids).

### Supporting mechanistic detail

- **Molecular pathways:** Kennedy / CDP-choline pathway for PC biosynthesis (KEGG hsa00564 glycerophospholipid metabolism); mitochondrial fatty-acid β-oxidation; PPAR signaling.
- **Cellular processes (GO):** mitochondrial fission (GO:0000266), mitophagy (GO:0000423), fatty-acid beta-oxidation (GO:0006635), phosphatidylcholine biosynthetic process (GO:0006656), myofiber apoptosis/necrosis.
- **Protein dysfunction:** loss of CHKB catalytic function (choline kinase activity GO:0004103); secondary reduction of fission GTPase DRP1.
- **Metabolic changes:** reduced PC (patient muscle); impaired FAO with triacylglycerol accumulation; reduced ATP and Krebs-cycle intermediates — an energy-metabolism signature.
- **Tissue damage mechanisms:** bioenergetic insufficiency and membrane instability drive myonecrosis and fibrosis/connective-tissue increase.
- **Immune involvement:** none intrinsic; the skin phenotype may involve the IL-12/IL-23 axis (basis for ustekinumab efficacy) ([PMID: 39143029](https://pubmed.ncbi.nlm.nih.gov/39143029/)).

### ASCII causal diagram

```
 CHKB biallelic LOF
        |
        v
 down choline kinase activity ──► down phosphatidylcholine (Kennedy pathway block)
        |
        v
 mitochondrial membrane dysfunction
   |                 |                      |
   v                 v                      v
 down DRP1/MFF/FIS1  up mitophagy    impaired beta-oxidation (down PPAR, up TAG)
 (down fission)                             |
   |                                        v
   +──────► GIANT peripheral mitochondria + ATP/Krebs failure
                        |
                        v
          myofiber degeneration + down cytoskeletal/contractile proteins
                        |
        ┌───────────────┼───────────────┬────────────────┐
        v               v               v                v
  muscular dystrophy  dilated CM   intellectual     ichthyosis-like
  (weakness, up CK)                disability        skin
```

**Molecular profiling evidence:** Proteomics of patient myoblasts (cytoskeletal/contractile downregulation; [PMID: 42449274](https://pubmed.ncbi.nlm.nih.gov/42449274/)); metabolomics/fluxomics of patient muscle cells (bioenergetic signature; [PMID: 34518586](https://pubmed.ncbi.nlm.nih.gov/34518586/)); transcriptomic/lipid data from the *Chkb* mouse ([PMID: 35322809](https://pubmed.ncbi.nlm.nih.gov/35322809/)).

---

## Section 7 — Anatomical Structures Affected

**Organ level.**
- **Primary:** skeletal muscle (UBERON:0001134) — the principal affected organ.
- **Secondary:** heart / myocardium (UBERON:0000948, UBERON:0002349) — dilated cardiomyopathy in ~50%; brain (UBERON:0000955) — intellectual disability/developmental delay; skin / epidermis (UBERON:0002097, UBERON:0001003) — ichthyosis-like changes.
- **Body systems:** musculoskeletal, cardiovascular, nervous (CNS), integumentary.

**Tissue and cell level.**
- Muscle tissue (UBERON:0002385); **skeletal muscle fiber / myocyte** (CL:0000188 skeletal muscle cell; CL:0008002 skeletal muscle fiber); cardiomyocyte (CL:0000746); epidermal keratinocyte (CL:0000312). Organelle disruption was shown to be **specific to skeletal muscle cells grown in culture** ([PMID: 34518586](https://pubmed.ncbi.nlm.nih.gov/34518586/)).

**Subcellular level.**
- **Mitochondrion (GO:0005739)** — the central affected compartment: peripherally enlarged mitochondria with complicated cristae and central depletion ([PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/)). Mitochondrial inner/outer membranes (GO:0005743 / GO:0005741). Secondary involvement of the endoplasmic reticulum (site of Kennedy-pathway PC synthesis, GO:0005789) is inferred.

**Localization / lateralization.** Generalized, **bilateral and symmetric** muscle involvement with proximal predominance; no lateralization.

---

## Section 8 — Temporal Development

**Onset.** Typically **congenital to early childhood** — neonatal hypotonia, infantile developmental delay; "a newly defined rare autosomal recessive disorder, with multisystem involvement presenting from the neonatal period to adolescence" ([PMID: 37393748](https://pubmed.ncbi.nlm.nih.gov/37393748/)). Onset pattern is **insidious/chronic**. The milder allelic form (Proximal Myopathy with Focal Depletion of Mitochondria) has **adult onset** ([PMID: 26782016](https://pubmed.ncbi.nlm.nih.gov/26782016/)).

**Progression.** Slowly progressive muscle weakness/wasting; intellectual disability is largely static. Dilated cardiomyopathy may develop or progress over childhood–adolescence and can cause heart failure and death. Disease duration is **chronic/lifelong**.

**Course pattern.** Predominantly **slowly progressive**; the mild allelic form is **non-progressive** but with **episodic rhabdomyolysis** susceptibility ([PMID: 26782016](https://pubmed.ncbi.nlm.nih.gov/26782016/)).

**Patterns / critical periods.** No spontaneous remission. The chief window for intervention is before onset of significant cardiac disease (cardiac surveillance) and, for emerging gene therapy, potentially after disease onset — AAV6-*Chkb* rescued the mouse even when given **post-disease onset** ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)).

---

## Section 9 — Inheritance and Population

**Inheritance.** **Autosomal recessive** (biallelic *CHKB* loss of function). Penetrance appears **complete** for biallelic LOF; **expressivity is variable**, including intrafamilial variability ([PMID: 26067811](https://pubmed.ncbi.nlm.nih.gov/26067811/)). No genetic anticipation. One documented case of apparent homozygosity resulted from a large heterozygous deletion plus **uniparental disomy** ([PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/)).

**Epidemiology.** Ultra-rare; precise prevalence/incidence unknown. **~35 confirmed patients** recorded by 2021 ([PMID: 33712684](https://pubmed.ncbi.nlm.nih.gov/33712684/)); ***CHKB* mutations described in 49 patients by 2023, of whom 40 were homozygous** ([PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/)):

> "CHKB mutations have been described in 49 patients with megaconial congenital muscular dystrophy, which is a rare autosomal recessive disorder, of which 40 patients showed homozygosity" ([PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/)).

**Population / geography.** Cases are reported across **Turkey, Japan, Iran (13-patient series), India, China, and Europe (Italy, Spain, Portugal)**, frequently in **consanguineous families** ([PMID: 37393748](https://pubmed.ncbi.nlm.nih.gov/37393748/); [PMID: 26067811](https://pubmed.ncbi.nlm.nih.gov/26067811/)). High homozygosity indicates **founder/consanguinity effects**. No strong sex bias is established (autosomal). Carrier frequency is not formally estimated but is presumed very low outside consanguineous populations.

> "a newly defined rare autosomal recessive disorder, with multisystem involvement presenting from the neonatal period to adolescence" ([PMID: 37393748](https://pubmed.ncbi.nlm.nih.gov/37393748/)).

---

## Section 10 — Diagnostics

**Diagnostic hallmark — muscle biopsy.** Myopathic/dystrophic changes with the **pathognomonic peripheral enlarged ("megaconial") mitochondria and central sarcoplasmic mitochondrial depletion**, best shown on **modified Gomori trichrome stain**, oxidative enzyme histochemistry, and **electron microscopy** ([PMID: 33712684](https://pubmed.ncbi.nlm.nih.gov/33712684/); [PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/); [PMID: 37393748](https://pubmed.ncbi.nlm.nih.gov/37393748/)):

> "Muscle biopsy in two patients showed a myopathic pattern with characteristic peripherally placed enlarged mitochondria on modified Gomori trichrome stain and electron microscopy" ([PMID: 33712684](https://pubmed.ncbi.nlm.nih.gov/33712684/)).

**Laboratory.** Serum creatine kinase is **mildly elevated** (e.g., up to ~500 U/L; 12/15 patients) — a useful but non-specific clue ([PMID: 26067811](https://pubmed.ncbi.nlm.nih.gov/26067811/); [PMID: 27123443](https://pubmed.ncbi.nlm.nih.gov/27123443/)). LOINC: CK [Creatine kinase, serum].

**Imaging / electrophysiology.** Brain MRI is typically **normal** ([PMID: 36175989](https://pubmed.ncbi.nlm.nih.gov/36175989/)); EMG may be normal or myopathic. Echocardiography/ECG are essential for cardiac surveillance (dilated cardiomyopathy, conduction defects — e.g., fascicular/bundle-branch block) ([PMID: 39465137](https://pubmed.ncbi.nlm.nih.gov/39465137/)).

**Genetic testing (confirmatory).** **Whole-exome sequencing** or targeted **CHKB single-gene testing / congenital-muscular-dystrophy gene panels** confirm the diagnosis ([PMID: 25740612](https://pubmed.ncbi.nlm.nih.gov/25740612/); [PMID: 33712684](https://pubmed.ncbi.nlm.nih.gov/33712684/)). Because several pathogenic variants are **intronic/synonymous splice-altering**, **RNA studies (RT-PCR) and careful reanalysis** are sometimes required ([PMID: 41026188](https://pubmed.ncbi.nlm.nih.gov/41026188/); [PMID: 25740612](https://pubmed.ncbi.nlm.nih.gov/25740612/)). Chromosomal microarray can detect large deletions/UPD ([PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/)). Mitochondrial DNA is normal (normal mtDNA content by in situ hybridization) ([PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/)).

**Alternative cell source.** Giant mitochondria can be detected in **lymphocytes/other cells when muscle is unavailable** ([PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/)):

> "We provide a possibility to detect giant mitochondria in other cells when muscle was not available."

**Clinical clue — skin.** Ichthyosis-like/psoriasiform skin changes with pruritus and nummular eczema may point to the diagnosis among congenital muscular dystrophies ([PMID: 27123443](https://pubmed.ncbi.nlm.nih.gov/27123443/); [PMID: 37907281](https://pubmed.ncbi.nlm.nih.gov/37907281/)).

**Differential diagnosis.** Other congenital/merosin-positive muscular dystrophies, mitochondrial myopathies, atypical Rett syndrome, autism spectrum disorder, and hypotonia-cystinuria syndrome (a case co-occurred/mimicked) ([PMID: 33712684](https://pubmed.ncbi.nlm.nih.gov/33712684/); [PMID: 33623274](https://pubmed.ncbi.nlm.nih.gov/33623274/); [PMID: 35707590](https://pubmed.ncbi.nlm.nih.gov/35707590/)).

**Screening.** No newborn screening exists. **Carrier and cascade testing** within affected consanguineous families, and prenatal/preimplantation testing, are feasible once the familial variants are known.

---

## Section 11 — Outcome / Prognosis

**Mortality.** The principal cause of death is **dilated cardiomyopathy / heart failure**; a patient in the original 1998 series died of dilated cardiomyopathy at age 13 ([PMID: 9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/)). Cardiac disease can require **heart transplantation** ([PMID: 26855408](https://pubmed.ncbi.nlm.nih.gov/26855408/)). Formal survival/life-expectancy statistics are not available given rarity.

**Morbidity / disability.** In the severe-end majority: lifelong **severe intellectual disability**, motor disability, and dependency; variable cardiac and dermatologic morbidity. The mild allelic form permits near-normal lifespan and function with episodic rhabdomyolysis risk ([PMID: 26782016](https://pubmed.ncbi.nlm.nih.gov/26782016/)).

**Complications.** Progressive weakness/contractures, cardiac failure/arrhythmia, respiratory compromise (inferred in severe cases), feeding/growth difficulties, and skin complications.

**Prognostic factors.** The **molecular defect (genotype) influences clinical outcome** — e.g., nonsense/complete-LOF alleles associate with severe disease, whereas some missense/hypomorphic or partial-splicing alleles yield milder phenotypes; the clinical outcome "seems to be influenced by CHKB molecular defects" ([PMID: 36175989](https://pubmed.ncbi.nlm.nih.gov/36175989/)). The presence and severity of dilated cardiomyopathy is the dominant prognostic determinant.

---

## Section 12 — Treatment

**No approved disease-modifying therapy exists; management is supportive and multidisciplinary.**

**Supportive / rehabilitative (NCIT: Supportive Care; Physical Therapy; Occupational Therapy):**
- Physiotherapy, occupational and speech therapy; management of contractures; developmental and educational support ([PMID: 26855408](https://pubmed.ncbi.nlm.nih.gov/26855408/)).
- **Cardiac surveillance and heart-failure management**, up to **heart transplantation** for severe dilated cardiomyopathy ([PMID: 26855408](https://pubmed.ncbi.nlm.nih.gov/26855408/)): "who was treated by heart transplantation." (NCIT: Heart Transplantation.)

**Dermatologic (targeted).** The IL-12/IL-23 inhibitor **ustekinumab** produced a successful response in a patient with diffuse ichthyosis-like scaling ([PMID: 39143029](https://pubmed.ncbi.nlm.nih.gov/39143029/)):

> "We report a patient with MCMD who had diffuse ichthyosis-like scaling, and successfully responded to ustekinumab" ([PMID: 39143029](https://pubmed.ncbi.nlm.nih.gov/39143029/)). (NCIT: Ustekinumab.)

**Advanced / experimental (preclinical).**
- **AAV-mediated CHKB gene replacement:** Intramuscular **AAV6-*Chkb*** given **after disease onset** rescued the dystrophic phenotype in the *rmd* mouse; a muscle-specific *Chkb* transgene completely rescued motor/behavioral function ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)):

> "Intramuscular gene therapy post-disease onset using an adeno-associated viral 6 (AAV6) vector carrying a functional copy of Chkb is also capable of rescuing the dystrophy phenotype" ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)).
- **CHKA (paralog) upregulation:** AAV6-driven upregulation of the paralog **Chka** also improved phenotypes — an alternative genetic-rescue strategy ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)).
- Continued **preclinical gene-therapy development** ([PMID: 42292914](https://pubmed.ncbi.nlm.nih.gov/42292914/)) and mechanism-based therapeutic routes targeting the lipid-metabolism defect ([PMID: 35322809](https://pubmed.ncbi.nlm.nih.gov/35322809/)).

**Pharmacogenomics / combination / personalized medicine.** None established. **Genotype-guided prognosis** is informative (see Section 11). No approved small-molecule or RNA therapy.

---

## Section 13 — Prevention

**Primary prevention is genetic**, given the Mendelian recessive etiology:
- **Genetic counseling** for consanguineous families and families with an affected child (recurrence risk 25%).
- **Carrier/cascade screening** once the familial variant is identified; **prenatal diagnosis** and **preimplantation genetic testing** are feasible.
- **Secondary prevention / early detection:** early echocardiographic cardiac surveillance to detect and manage dilated cardiomyopathy before heart failure; early developmental intervention.
- **Tertiary prevention:** physiotherapy to prevent contractures; heart-failure therapy; dermatologic management.

No vaccination, environmental, or public-health interventions are applicable. There is no population newborn screening for this disorder.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *CHKB* (NCBI Gene 1120) has a mouse ortholog *Chkb* (*Mus musculus*, NCBI Taxon 10090).
- **Natural animal disease:** The **rostrocaudal muscular dystrophy (rmd) mouse** carries a naturally occurring *Chkb* deletion and develops an MDCMC-like dystrophy — the key natural/model disease ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)). No well-characterized companion-animal natural disease is documented in the reviewed literature.
- **Comparative biology / conservation:** The CHKB–PC–mitochondrial mechanism is conserved; *Chkb*-null mice reproduce muscle and cardiac disease, supporting evolutionary conservation. The *CHKB–CPT1B* syntenic/regulatory linkage is a eutherian-mammal feature relevant to muscle fatty-acid oxidation and brown-adipose-tissue evolution ([PMID: 33058877](https://pubmed.ncbi.nlm.nih.gov/33058877/)).
- **Transmission / zoonosis:** Not applicable (genetic disease).

---

## Section 15 — Model Organisms

**Primary model — mouse.** The ***Chkb*-deficient rostrocaudal muscular dystrophy (rmd) mouse** is the central model.

| Model aspect | Detail | Reference |
|---|---|---|
| Model type | Mammalian (mouse), naturally occurring *Chkb* deletion | [PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/) |
| Phenotype recapitulation | MDCMC-like muscular dystrophy; motor/behavioral deficits; cardiac hypertrophy and arrhythmia predisposition | [PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/); [PMID: 35151687](https://pubmed.ncbi.nlm.nih.gov/35151687/) |
| Metabolic phenotype | Temporal failure of mitochondrial β-oxidation; shunting into triacylglycerol; reduced PPAR targets (PC level not significantly altered — a model nuance) | [PMID: 35322809](https://pubmed.ncbi.nlm.nih.gov/35322809/) |
| Therapeutic validation | Muscle-specific *Chkb* transgene = complete rescue; AAV6-*Chkb* post-onset = rescue; AAV6-*Chka* upregulation = improvement | [PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/) |

**Cellular / in vitro models.** **Patient-derived primary skeletal myoblasts/muscle cells** recapitulate reduced mitochondrial fission (↓DRP1/MFF/FIS1), impaired energy metabolism, and cytoskeletal/contractile proteomic alterations ([PMID: 34518586](https://pubmed.ncbi.nlm.nih.gov/34518586/); [PMID: 42449274](https://pubmed.ncbi.nlm.nih.gov/42449274/)); notably, organelle disruption was **specific to skeletal muscle cells in culture**.

**Model limitations.** The mouse does not fully model the human CNS/intellectual-disability phenotype; and the discrepancy that **PC levels are not significantly reduced in the *Chkb* mouse** (whereas human nonsense-mutation muscle shows decreased PC) indicates the mouse may capture downstream metabolic consequences better than the primary PC-deficiency readout — relevant when interpreting mechanism and therapeutic endpoints.

**Resources:** MGI (*Chkb*), IMPC/IMSR for mouse lines; patient-derived myoblast cultures.

---

## Mechanistic Model / Interpretation

Megaconial CMD is best understood as a **phospholipid-biosynthesis disorder with a downstream mitochondrial/bioenergetic phenotype**. The single necessary and sufficient lesion is **biallelic CHKB loss of function**, which removes the first enzymatic step of the Kennedy pathway and depletes phosphatidylcholine supply to muscle mitochondrial membranes. The disease's signature — **giant peripheral mitochondria with central depletion** — arises from two converging consequences: (i) **impaired mitochondrial fission** due to reduced DRP1/MFF/FIS1, and (ii) **increased mitophagy** with abnormal membrane dynamics. The functional cost is an **energy crisis**: impaired fatty-acid β-oxidation (with lipid shunting into triacylglycerol), mild OXPHOS/complex-V deficits, and reduced ATP and Krebs-cycle intermediates. The muscle then undergoes dystrophic degeneration with secondary loss of cytoskeletal/contractile proteins, producing weakness and elevated CK. The same mechanism injures cardiomyocytes (dilated cardiomyopathy — the principal lethal complication) and, via less-well-demonstrated routes, the brain (intellectual disability) and skin (ichthyosis). Genotype grades the outcome: complete-LOF alleles → severe congenital disease; hypomorphic/partial-splicing alleles → milder, even adult-onset, phenotypes.

The therapeutic logic follows directly: restoring CHKB function (AAV gene replacement) or boosting the redundant paralog CHKA re-establishes PC synthesis and rescues the mouse, making **gene-directed therapy the leading translational path**, while current care remains supportive with genotype-informed prognosis and cardiac surveillance as the highest-yield clinical interventions.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [21665002](https://pubmed.ncbi.nlm.nih.gov/21665002/) | *CMD caused by defective de novo PC biosynthesis* | **Landmark:** identifies *CHKB* cause; absent choline kinase activity, reduced PC |
| [9427222](https://pubmed.ncbi.nlm.nih.gov/9427222/) | *New CMD with mitochondrial structural abnormalities* | First morphological description of megaconial mitochondria; normal mtDNA |
| [26067811](https://pubmed.ncbi.nlm.nih.gov/26067811/) | *Clinical characteristics, 15 patients* | Core phenotype frequencies; intrafamilial variability |
| [26855408](https://pubmed.ncbi.nlm.nih.gov/26855408/) | *Mitochondrial membrane homeostasis defect* | DCM in half of cases; OXPHOS/complex-V findings; heart transplant |
| [34518586](https://pubmed.ncbi.nlm.nih.gov/34518586/) | *Reduced fission & impaired energy metabolism* | ↓DRP1/MFF/FIS1; bioenergetic signature in patient cells |
| [35322809](https://pubmed.ncbi.nlm.nih.gov/35322809/) | *Mechanism & therapeutic route (lipid metabolism)* | FAO failure, TAG shunting; PC not altered in mouse |
| [22024749](https://pubmed.ncbi.nlm.nih.gov/22024749/) | *Phospholipid synthetic defect & mitophagy* | Links PC defect to mitochondrial dysfunction + mitophagy |
| [31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/) | *Functional rescue in mouse model* | AAV6-*Chkb* and *Chka* rescue; transgene rescue |
| [35151687](https://pubmed.ncbi.nlm.nih.gov/35151687/) | *Mouse cardiac abnormalities / arrhythmia* | Cardiac hypertrophy and arrhythmia predisposition |
| [26782016](https://pubmed.ncbi.nlm.nih.gov/26782016/) | *Proximal myopathy with focal mito depletion* | Mild allelic adult-onset end of spectrum |
| [33712684](https://pubmed.ncbi.nlm.nih.gov/33712684/) | *Resemble atypical Rett syndrome* | Biopsy hallmark; Rett-like presentation; ~35 patients |
| [33623274](https://pubmed.ncbi.nlm.nih.gov/33623274/) | *Rare cause of ASD* | Autism spectrum presentation; splice variants |
| [36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/) | *Large deletion + UPD* | 49 patients/40 homozygous; lymphocyte detection |
| [37393748](https://pubmed.ncbi.nlm.nih.gov/37393748/) | *13 Iranian patients* | AR, multisystem, neonatal–adolescent onset |
| [42449274](https://pubmed.ncbi.nlm.nih.gov/42449274/) | *Proteomic analysis of myoblasts* | Cytoskeletal/contractile downregulation (218 proteins) |
| [39143029](https://pubmed.ncbi.nlm.nih.gov/39143029/) | *Ustekinumab response* | Targeted therapy for cutaneous phenotype |
| [27123443](https://pubmed.ncbi.nlm.nih.gov/27123443/) | *Skin changes in differential diagnosis* | p.R344Q; ichthyosis as diagnostic clue |
| [36175989](https://pubmed.ncbi.nlm.nih.gov/36175989/) | *Novel CHKB variants, review* | Intronic splice variant; ↓DRP1; genotype–outcome link |
| [25740612](https://pubmed.ncbi.nlm.nih.gov/25740612/) | *Splicing mutation by WES* | c.1031+3G>C splice variant; WES utility |
| [41026188](https://pubmed.ncbi.nlm.nih.gov/41026188/) | *Alternative splicing of 3 rare variants* | Synonymous/intronic variants alter splicing |
| [39465137](https://pubmed.ncbi.nlm.nih.gov/39465137/) | *Rare homozygous variant* | c.598delC frameshift; severe cardiac/conduction disease |
| [33058877](https://pubmed.ncbi.nlm.nih.gov/33058877/) | *CHKB-CPT1B coordination* | Shared regulatory domain; FAO/muscle relevance |
| [42292914](https://pubmed.ncbi.nlm.nih.gov/42292914/) | *Preclinical gene therapy* | Ongoing AAV-CHKB gene-therapy development |

---

## Limitations and Knowledge Gaps

1. **Small evidence base:** Fewer than ~50 genetically confirmed patients worldwide; most data are case reports/small series, limiting frequency and natural-history estimates.
2. **No formal epidemiology:** Prevalence/incidence, carrier frequency, sex ratio, and survival statistics are not rigorously established.
3. **CNS mechanism unclear:** The pathway from CHKB/PC deficiency to intellectual disability and autistic/Rett-like features is inferred, not mechanistically demonstrated.
4. **Human vs mouse discrepancy:** PC is reduced in human nonsense-mutation muscle but *not* significantly altered in the *Chkb* mouse, complicating biomarker selection and mechanistic interpretation.
5. **No approved therapy and no human trials yet:** Gene-therapy evidence is entirely preclinical; ustekinumab benefit rests on a single case.
6. **Genotype–phenotype correlations** are suggested but not systematically quantified across variant classes.
7. **Variant detection pitfalls:** Deep-intronic, synonymous, and structural (deletion/UPD) variants can be missed without RNA studies and CMA.
8. **No disease-specific QoL instruments** validated for this disorder.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry & natural-history study** to quantify prevalence, cardiac penetrance/age-of-onset, survival, and genotype–phenotype correlations.
2. **IND-enabling AAV-*CHKB* gene-therapy program:** optimize vector/serotype, dose, route (systemic vs intramuscular), and timing; define regulatory endpoints given the mouse PC-biomarker nuance ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/); [PMID: 42292914](https://pubmed.ncbi.nlm.nih.gov/42292914/)).
3. **Test CHKA-upregulation / small-molecule approaches** as a non-vector-limited alternative ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)).
4. **CNS-focused modeling** (patient iPSC-derived neurons/organoids; brain-targeted mouse studies) to define the intellectual-disability mechanism.
5. **Biomarker development:** validate muscle PC, lipidomic FAO/TAG signatures, DRP1/fission markers, and circulating/imaging markers for diagnosis and trial endpoints ([PMID: 34518586](https://pubmed.ncbi.nlm.nih.gov/34518586/); [PMID: 42449274](https://pubmed.ncbi.nlm.nih.gov/42449274/)).
6. **Prospective cardiac surveillance protocol** (serial echo/ECG/MRI) to guide early heart-failure intervention and transplant timing.
7. **Systematic splicing/RNA diagnostic workflow** and CMA to capture intronic/synonymous/structural variants that escape standard panels ([PMID: 41026188](https://pubmed.ncbi.nlm.nih.gov/41026188/); [PMID: 36896673](https://pubmed.ncbi.nlm.nih.gov/36896673/)).
8. **Controlled evaluation of ustekinumab / IL-23-axis therapy** for the cutaneous phenotype beyond the single reported case ([PMID: 39143029](https://pubmed.ncbi.nlm.nih.gov/39143029/)).

---

*Report compiled from 27 reviewed publications and 9 confirmed findings. Evidence types span human clinical case series/reports, mouse-model studies, patient-derived in vitro work, and molecular/biochemical assays, as indicated per claim.*


## Artifacts

- [OpenScientist final report](Megaconial_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Megaconial_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011246` (2 mentions) - the report calls it "MONDO"; MONDO calls it **megaconial type congenital muscular dystrophy**
- `HP:0001263` (1 mention) - the report calls it "Static/slowly progressive"; HP calls it **Global developmental delay**
- `HP:0010864` (1 mention) - the report calls it "Static"; HP calls it **Severe intellectual disability**
- `HP:0003701` (1 mention) - the report calls it "Slowly progressive/variable"; HP calls it **Proximal muscle weakness**
- `HP:0003202` (1 mention) - the report calls it "Progressive"; HP calls it **Skeletal muscle atrophy**
- `HP:0000252` (1 mention) - the report calls it "Static"; HP calls it **Microcephaly**
- `HP:0001999` (1 mention) - the report calls it "Static"; HP calls it **Abnormal facial shape**
- `HP:0001644` (1 mention) - the report calls it "Progressive"; HP calls it **Dilated cardiomyopathy**
- `HP:0003201` (1 mention) - the report calls it "Episodic"; HP calls it **Rhabdomyolysis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001134` (1 mention) - the report calls it "Primary:** skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names