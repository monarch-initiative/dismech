---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T15:32:11.225801'
end_time: '2026-10-30T15:56:09.940431'
duration_seconds: 1438.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pseudohypoaldosteronism Type 2E
  mondo_id: MONDO:0013782
  category: Mendelian
  causal_genes: CUL3
  omim_id: OMIM:614496
  synonyms: pseudohypoaldosteronism type 2 caused by mutation in CUL3; CUL3 pseudohypoaldosteronism
    type 2; PHA2E
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
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 18
  validator_version: 0.4.0
term_validation:
  total_terms: 23
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 9
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0013782
    reported_labels:
    - MONDO
    - PHA2E
    ontology_label: pseudohypoaldosteronism type 2E
  - term_id: HP:0002153
    reported_labels:
    - Laboratory abnormality
    - Elevated (hyperkalemia)
    - Hyperkalemia
    ontology_label: Hyperkalemia
  - term_id: HP:0004879
    reported_labels:
    - "Hyperchloremia, low HCO\u2083 (metabolic acidosis)"
    ontology_label: Intermittent hyperventilation
  - term_id: HP:0002150
    reported_labels:
    - Laboratory abnormality
    - Elevated (hypercalciuria)
    - Hypercalciuria
    ontology_label: Hypercalciuria
  - term_id: HP:0004322
    reported_labels:
    - Physical manifestation
    ontology_label: Short stature
  labels_variant: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pseudohypoaldosteronism_Type_2E-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pseudohypoaldosteronism_Type_2E-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pseudohypoaldosteronism Type 2E
- **MONDO ID:** MONDO:0013782 (if available)
- **Causal gene(s):** CUL3
- **OMIM:** OMIM:614496
- **Synonyms:** pseudohypoaldosteronism type 2 caused by mutation in CUL3; CUL3 pseudohypoaldosteronism type 2; PHA2E
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pseudohypoaldosteronism Type 2E** covering all of the
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

# Pseudohypoaldosteronism Type 2E (PHA2E): A Comprehensive Disease Characterization

**Disease:** Pseudohypoaldosteronism Type 2E (PHA2E)
**MONDO ID:** MONDO:0013782 · **OMIM:** 614496
**Causal gene:** **CUL3** (cullin-3, HGNC:2553, NCBI Gene 8452, chromosome 2q36.2)
**Category:** Mendelian, monogenic hypertension

---

## Summary

**Pseudohypoaldosteronism type 2E (PHA2E) is the CUL3 (cullin-3)-caused subtype of familial hyperkalemic hypertension (FHHt)**, also known as Gordon syndrome or pseudohypoaldosteronism type II (PHAII). It is a rare, autosomal-dominant, predominantly *de novo* Mendelian disorder in which mutations cause skipping of CUL3 exon 9, producing an in-frame deletion of 57 amino acids (CUL3Δ403-459, "CUL3-Δ9"). PHA2E is distinguished among the four FHHt genes (WNK1, WNK4, KLHL3, CUL3) as the **most severe subtype**, typically presenting in childhood with hypertension, hyperkalemia, hyperchloremic metabolic acidosis, hypercalciuria, suppressed renin, and normal or high aldosterone — all with a normal glomerular filtration rate ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/); [PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/)).

Mechanistically, CUL3 is the scaffold of a cullin-RING E3 ubiquitin ligase that, together with the BTB-Kelch adaptor KLHL3, ubiquitinates WNK1/WNK4 kinases for proteasomal degradation. The PHA2E mutant ligase fails to degrade WNK kinases normally; the accumulated WNKs hyperactivate the downstream kinases SPAK (STE20/SPS1-related proline/alanine-rich kinase) and OSR1 (oxidative stress-responsive kinase 1), which phosphorylate and activate the thiazide-sensitive Na-Cl cotransporter (NCC) in the renal distal convoluted tubule (DCT). This drives excessive NaCl reabsorption (→ hypertension) and impaired potassium secretion (→ hyperkalemia) ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/); [PMID: 39699086](https://pubmed.ncbi.nlm.nih.gov/39699086/)).

Beyond the renal lesion, a faithful knock-in mouse model (CUL3^WT/Δ403-459^) reveals a **vascular component** to the hypertension, consistent with the WNK-SPAK/OSR1 pathway's role in vascular smooth muscle arterial tone ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/); [PMID: 26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/)). The prognosis is excellent with treatment: thiazide diuretics (which directly inhibit the hyperactivated NCC) plus dietary salt restriction produce dramatic normalization of blood pressure and electrolytes. Untreated or late-diagnosed disease carries morbidity including growth and developmental impairment in children and risk of life-threatening hyperkalemic arrhythmia.

---

## 1. Disease Information

PHA2E is a rare inherited monogenic form of low-renin hypertension within the FHHt/Gordon syndrome/PHAII spectrum. It is defined molecularly by its causal gene, **CUL3 (cullin-3)**, which distinguishes it from the other PHAII subtypes caused by WNK1 (PHA2C), WNK4 (PHA2B), and KLHL3 (PHA2D).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013782 |
| OMIM | 614496 (PSEUDOHYPOALDOSTERONISM, TYPE IIE; PHA2E) |
| Causal gene | CUL3 (HGNC:2553; NCBI Gene 8452; chromosome 2q36.2) |
| Disease family | Familial hyperkalemic hypertension (FHHt) / Gordon syndrome / PHAII |

**Synonyms and alternative names:** pseudohypoaldosteronism type 2 caused by mutation in CUL3; CUL3 pseudohypoaldosteronism type 2; PHA2E; Gordon syndrome (CUL3-related); familial hyperkalemic hypertension, CUL3 type.

**Information source:** The disease-level characterization here derives principally from aggregated disease-level resources (OMIM, published case series, and mechanistic studies) combined with individual patient case reports. PHA2E is sufficiently rare that no large patient-level EHR registries exist specifically for the CUL3 subtype; evidence comes from case reports, small pedigree studies, and mechanistic mouse/cell models.

---

## 2. Etiology

**Primary cause — genetic.** PHA2E is caused by heterozygous, dominant, predominantly *de novo* mutations in **CUL3**. Boyden et al. (2012) used exome sequencing across 41 unrelated PHAII families to identify CUL3 (and KLHL3) as causal genes: *"KLHL3 mutations are either recessive or dominant, whereas CUL3 mutations are dominant and predominantly de novo"* ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). A key convergent feature is that diverse CUL3 mutations — spanning splice-donor and splice-acceptor sites flanking exon 9 — all produce the same outcome: *"Diverse CUL3 mutations all result in skipping of exon 9, producing an in-frame deletion"* ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)).

**Genetic risk factors.** The causal variants are the CUL3 exon-9 splice-site mutations themselves. There are no known common susceptibility loci or modifier alleles established specifically for PHA2E; the disorder is monogenic with high penetrance.

**Environmental risk factors.** Dietary sodium (salt) load worsens the hypertensive phenotype because the underlying defect is excessive renal NaCl reabsorption; dietary potassium load exacerbates hyperkalemia. These are modifiers of expression rather than causes.

**Protective factors.** Dietary sodium restriction is a protective/ameliorating environmental factor, reducing the substrate for NCC-driven NaCl retention. No genetic protective variants are established.

**Gene-environment interactions.** The core interaction is between the CUL3 genotype (which fixes NCC in a hyperactive state) and dietary salt and potassium intake, which determine the magnitude of hypertension and hyperkalemia. Co-occurrence of a second channelopathy variant can modify phenotype — a notable case reported a girl carrying both SCNN1A (PHAI) and CUL3 (PHAII) mutations, producing a complex mixed salt-handling phenotype ([PMID: 36303414](https://pubmed.ncbi.nlm.nih.gov/36303414/)).

---

## 3. Phenotypes

The core phenotype is a biochemical and hemodynamic constellation. Bruel et al. (2016) summarize the typical picture: *"The typical clinical picture of Gordon syndrome includes, apart from arterial hypertension and dyskaliemia, hyperchloremia metabolic acidosis, hypercalciuria, a low rate of renin, and most frequently, a normal or high rate of aldosterone. Dental abnormalities and growth retardation can also be associated"* ([PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/)).

| Phenotype | Type | HPO term (suggested) | Characteristics |
|---|---|---|---|
| Arterial hypertension | Clinical sign | HP:0000822 (Hypertension) | Childhood-onset possible; severe in CUL3; the defining feature |
| Hyperkalemia | Laboratory abnormality | HP:0002153 | Present despite normal GFR; can be life-threatening |
| Hyperchloremic metabolic acidosis | Laboratory abnormality | HP:0004879 / HP:0001947 | Characteristic of PHAII |
| Hypercalciuria | Laboratory abnormality | HP:0002150 | Associated finding |
| Suppressed plasma renin | Laboratory abnormality | — (low renin) | Low renin is diagnostic |
| Normal/high aldosterone | Laboratory abnormality | — | Distinguishes from true hypoaldosteronism |
| Growth retardation | Physical manifestation | HP:0001510 (Growth delay) | In pediatric cases, linked to persistent acidosis/hypertension |
| Dental abnormalities | Physical manifestation | HP:0000164 (Abnormality of the teeth) | Reported association in Gordon syndrome |
| Short stature | Physical manifestation | HP:0004322 | Reported in some cases |

**Age of onset:** CUL3/PHA2E tends to present earlier and more severely than other FHHt subtypes — often in childhood. A representative CUL3 case was a 7-year-old girl with hypertension, growth retardation, hyperkalemia and metabolic acidosis carrying a *de novo* exon-9 splice mutation ([PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/)).

**Severity:** CUL3 produces the most severe form of FHHt ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/)).

**Progression:** Chronic and lifelong, but highly responsive to treatment. Untreated, persistent metabolic acidosis and hypertension may lead to significant growth and developmental impairments in pediatric patients ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)).

**Frequency / quality of life:** Hypertension and the biochemical triad are present in essentially all affected individuals; growth retardation and dental abnormalities are variable associations. With appropriate thiazide therapy, quality of life is largely preserved; untreated disease impairs growth/development and carries cardiac arrhythmia risk from hyperkalemia.

---

## 4. Genetic / Molecular Information

**Causal gene:** **CUL3** (cullin-3), HGNC:2553, NCBI Gene 8452, located at chromosome 2q36.2. OMIM gene entry 603136; disease entry 614496.

**Pathogenic variants.** The pathognomonic lesion is **skipping of exon 9**, caused by heterozygous mutations at the intron 8 / exon 9 splice-acceptor site and the exon 9 / intron 9 splice-donor site, as well as some exonic variants. All converge on an in-frame deletion of 57 amino acids (residues 403-459): **CUL3Δ403-459** ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/); [PMID: 27378813](https://pubmed.ncbi.nlm.nih.gov/27378813/)).

- **Variant classification (ACMG/AMP):** Pathogenic (established, recurrent, functionally validated disease-causing variants).
- **Variant type/class:** Predominantly splice-site variants producing an in-frame exon-skip; functionally equivalent to an internal deletion.
- **Allele frequency:** Effectively absent from population databases (gnomAD) — these are private, predominantly *de novo* pathogenic variants, consistent with a severe, early-onset dominant disorder.
- **Somatic vs germline:** Germline; a large fraction arise *de novo* in the proband.
- **Functional consequence:** A combination of **loss of function** (impaired WNK ubiquitylation) and abnormal **gain/altered function** (auto-ubiquitylation, loss of regulatory interactions). Schumacher et al. (2015) showed: *"the PHA2E mutant, CUL3(Δ403-459), is severely compromised in its ability to ubiquitylate WNKs, possibly due to altered structural flexibility. Instead, CUL3(Δ403-459) auto-ubiquitylates and loses interaction with two important Cullin regulators: the COP9-signalosome and CAND1"* ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/)). The dual gain/loss nature is emphasized in [PMID: 29897280](https://pubmed.ncbi.nlm.nih.gov/29897280/).

**Why CUL3 is more severe.** The same study notes: *"These findings may explain the severity of the FHHt phenotype caused by CUL3 mutations compared to those reported in KLHL3 or WNK kinases"* ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/)). Loss of COP9-signalosome (CSN) binding is central — the catalytically active CSN subunit JAB1 fails to associate with the deleted CUL3 4-helix bundle domain ([PMID: 29897280](https://pubmed.ncbi.nlm.nih.gov/29897280/)), and disrupted CSN binding has been confirmed as a major contributor to the FHHt phenotype in a renal CSN-deficient mouse ([PMID: 30301860](https://pubmed.ncbi.nlm.nih.gov/30301860/); see also [PMID: 31813255](https://pubmed.ncbi.nlm.nih.gov/31813255/)).

**Modifier genes:** Within the pathway, the levels/activity of WNK1, WNK4, KLHL3, SPAK, OSR1, and NCC (SLC12A3) modulate the net phenotype. No formal modifier loci are established for PHA2E.

**Epigenetic information:** No disease-specific DNA methylation or histone modification signatures have been established for PHA2E. (CUL3 itself regulates protein stability of many substrates via ubiquitination/neddylation — a post-translational rather than epigenetic mechanism.)

**Chromosomal abnormalities:** None characteristic; PHA2E is a single-gene splice-defect disorder, not a copy-number or structural disorder.

---

## 5. Environmental Information

PHA2E is a genetic disorder; environmental factors modulate expression rather than cause disease.

- **Environmental factors:** No toxic, radiation, or occupational exposures are implicated as causes.
- **Lifestyle factors:** Dietary **sodium (salt)** intake worsens hypertension; dietary **potassium** intake worsens hyperkalemia. Salt restriction is beneficial.
- **Infectious agents:** None. PHA2E is not an infectious or post-infectious disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous *de novo* **CUL3 splice-site mutation** disrupts splicing → **leads to** skipping of exon 9 and an in-frame deletion (CUL3Δ403-459). ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/))
2. CUL3Δ403-459 protein **results in** a structurally altered cullin-RING E3 ligase that loses binding to the COP9 signalosome (CSN) and CAND1, and instead auto-ubiquitylates. ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/); [PMID: 29897280](https://pubmed.ncbi.nlm.nih.gov/29897280/))
3. The defective CUL3-KLHL3 ligase **fails to ubiquitinate WNK1/WNK4 kinases** → proteasomal degradation of WNKs is abrogated → **leads to** cytoplasmic accumulation of WNK kinases. ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/))
4. Accumulated WNK kinases **phosphorylate and activate SPAK and OSR1** (overactivation). ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/))
5. Active SPAK/OSR1 **phosphorylate and activate the thiazide-sensitive Na-Cl cotransporter (NCC)** in the distal convoluted tubule. ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/); [PMID: 39699086](https://pubmed.ncbi.nlm.nih.gov/39699086/))
6a. **Renal branch:** NCC hyperactivation → increased NaCl reabsorption → volume expansion → **hypertension**; reduced distal Na⁺ delivery impairs K⁺ and H⁺ secretion → **hyperkalemia and hyperchloremic metabolic acidosis**. ([PMID: 39699086](https://pubmed.ncbi.nlm.nih.gov/39699086/))
6b. **Vascular branch (demonstrated in mouse, inferred in human):** The same WNK-OSR1/SPAK-SLC12a cascade is active in vascular smooth muscle, where it regulates arterial tone — contributing a vascular component to hypertension evidenced by altered arterial pulse waveform in the CUL3 knock-in mouse. ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/); [PMID: 26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/))

### ASCII mechanistic diagram

```
 CUL3 splice mutation
        │ (exon 9 skipping)
        ▼
 CUL3Δ403-459  ── loses CSN/CAND1 binding, auto-ubiquitylates (gain + loss of function)
        │
        ▼ (ligase fails to ubiquitinate WNKs)
 WNK1 / WNK4 kinases accumulate (degradation abrogated)
        │
        ▼ (phosphorylation)
 SPAK / OSR1  overactivated
        │
    ┌───┴──────────────────────────┐
    ▼ (renal DCT)                   ▼ (vascular smooth muscle)
 NCC hyperactivation           ↑ arterial tone
    │                               │
    ▼                               ▼
 ↑ NaCl reabsorption          vascular contribution
 ↓ distal Na+ delivery             │
    │                               │
    ▼                               │
 Hyperkalemia +  ───► HYPERTENSION ◄┘
 metabolic acidosis
```

### Detail by category

- **Molecular pathways:** The CUL3/KLHL3–WNK–SPAK/OSR1–NCC pathway. Ferdaus & McCormick frame it as a therapeutic target: *"The disease familial hyperkalemic hypertension is caused by mutations in with-no-lysine (WNK) kinases 1 and 4 and in cullin-3 and kelch-like 3, components of an E3 ubiquitin ligase complex that promotes WNK kinase degradation"* ([PMID: 27076645](https://pubmed.ncbi.nlm.nih.gov/27076645/)).
- **Cellular processes:** Protein polyubiquitination (GO:0000209), protein targeting for proteasomal degradation, cullin-RING ligase activity (Cul3-RING ubiquitin ligase complex GO:0031463), protein neddylation (GO:0045116; CUL3 is NEDD8-modified), sodium ion transmembrane transport (GO:0035725), regulation of blood pressure (GO:0008217).
- **Protein dysfunction:** Altered structural flexibility of the mutant cullin scaffold; impaired substrate (WNK) ubiquitylation; aberrant auto-ubiquitylation; loss of CSN/CAND1 regulatory interactions ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/)).
- **Biochemical abnormalities:** Transporter (NCC) hyperactivity; E3 ligase dysfunction; dysregulated NEDD8/CSN deneddylation cycle.
- **Tissue damage mechanisms:** Primarily functional (electrolyte/volume dysregulation) rather than destructive; chronic hypertension can cause downstream end-organ effects, and DCT-specific CSN disruption can cause tubular injury ([PMID: 39205661](https://pubmed.ncbi.nlm.nih.gov/39205661/)).
- **Immune/metabolic/epigenetic:** No primary autoimmune, metabolic-enzyme, or epigenetic mechanism is implicated.

**Upstream vs downstream:** Upstream = CUL3 ligase defect → WNK accumulation. Downstream = SPAK/OSR1 → NCC → NaCl retention → clinical phenotype. **Cell types:** DCT epithelial cell (CL:1000768 kidney distal convoluted tubule epithelial cell), vascular smooth muscle cell (CL:0000359). **GO biological processes:** GO:0000209 (protein polyubiquitination), GO:0035725 (sodium ion transmembrane transport), GO:0008217 (regulation of blood pressure).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Kidney (UBERON:0002113), specifically the **renal distal convoluted tubule (DCT)** (UBERON:0001292). Cornelius et al.: *"In the kidney, these mutations ultimately cause hyperactivation of NCC along the renal distal convoluted tubule. Hypertension results from increased NaCl retention, and hyperkalemia by impaired K[+ secretion]"* ([PMID: 39699086](https://pubmed.ncbi.nlm.nih.gov/39699086/)).
- **Secondary / body systems:** Cardiovascular system (hypertension, vascular smooth muscle involvement; UBERON:0004535), endocrine/renin-angiotensin-aldosterone axis (suppressed renin), skeletal/dental (growth retardation, dental abnormalities).
- **Tissue and cell level:** Renal tubular epithelium — DCT epithelial cells (CL:1000768) where KLHL3, CUL3, WNK kinases, and NCC are co-expressed ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)); vascular smooth muscle cells (CL:0000359) where the WNK-OSR1/SPAK-SLC12a cascade regulates arterial tone ([PMID: 26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/)). Downstream potassium handling involves the connecting tubule/collecting duct (ENaC/ROMK) secondarily — notably ROMK expression remained unaltered in the CUL3Δ403-459 mouse, indicating hyperkalemia arises chiefly from reduced distal Na⁺ delivery rather than ROMK loss ([PMID: 27378813](https://pubmed.ncbi.nlm.nih.gov/27378813/)).
- **Subcellular level:** Cytoplasm (WNK kinase accumulation), plasma/apical membrane (NCC), and the Cul3-RING ubiquitin ligase complex (GO:0031463). GO cellular components: GO:0005737 (cytoplasm), GO:0016020 (membrane), GO:0031463 (Cul3-RING ligase complex).
- **Localization / lateralization:** Bilateral renal involvement; systemic (not lateralized) hypertension.

---

## 8. Temporal Development

- **Onset:** Congenital genetic basis; clinical onset frequently in childhood for CUL3/PHA2E (the most severe subtype), though biochemical abnormalities may be detected at various ages. Onset pattern is insidious/chronic. Representative case: 7-year-old girl ([PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/)); a 9-year follow-up of early-onset PHAII has been reported ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)).
- **Progression:** Chronic, lifelong, non-remitting without treatment, but not typically a destructive/degenerative course. Hypertension shows a positive relationship with age, as in the general population ([PMID: 11903313](https://pubmed.ncbi.nlm.nih.gov/11903313/)).
- **Progression rate / course:** Stable-chronic; electrolyte abnormalities and hypertension persist until treated.
- **Patterns:** No spontaneous remission; treatment-induced normalization is rapid and dramatic with thiazides. **Critical period:** Childhood is a window where untreated acidosis and hypertension impair growth and development — early diagnosis and intervention are key ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)).

---

## 9. Inheritance and Population

- **Epidemiology:** FHHt/Gordon syndrome is a very rare cause of hypertension. Among 5,100 patients referred to a tertiary hypertension unit, 7.3% had hyperkalemia and FHHt was a rare diagnosis within that group ([PMID: 39229746](https://pubmed.ncbi.nlm.nih.gov/39229746/)). More than 90 single cases/families of FHHt have been reported historically, with marked phenotypic heterogeneity ([PMID: 11903313](https://pubmed.ncbi.nlm.nih.gov/11903313/)). CUL3 (PHA2E) is one of the rarer and most severe subtypes. Precise prevalence/incidence figures for the CUL3 subtype specifically are not established.
- **Inheritance pattern:** Autosomal dominant, **predominantly *de novo*** for CUL3 ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). CUL3 and KLHL3 variants segregated in 63% of previously unexplained FHHt pedigrees ([PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)).
- **Penetrance:** High (effectively complete for the biochemical phenotype in reported pedigrees).
- **Expressivity:** Variable — severity of biochemical abnormalities varies among individuals and families ([PMID: 11903313](https://pubmed.ncbi.nlm.nih.gov/11903313/)).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity / carrier frequency:** Given the predominantly *de novo* nature of CUL3 variants, founder effects and consanguinity are not typical features (unlike recessive KLHL3). No meaningful carrier frequency applies to a *de novo* dominant disorder.
- **Population demographics:** No ethnic or geographic predilection established for PHA2E. **Sex ratio:** Autosomal — expected ~1:1 male:female. **Age distribution:** Childhood onset is characteristic of the CUL3 subtype.

---

## 10. Diagnostics

**Biochemical diagnosis.** PHA2E is suspected on the triad of **hyperkalemia, hyperchloremic metabolic acidosis, and hypertension with suppressed plasma renin and normal GFR**, with normal or high aldosterone and hypercalciuria ([PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/); [PMID: 6384650](https://pubmed.ncbi.nlm.nih.gov/6384650/)).

| Test | Finding in PHA2E | Notes |
|---|---|---|
| Serum potassium | Elevated (hyperkalemia) | HP:0002153 |
| Serum chloride / bicarbonate | Hyperchloremia, low HCO₃ (metabolic acidosis) | HP:0004879 |
| Plasma renin activity | Suppressed/low | diagnostic clue |
| Plasma aldosterone | Normal or high | distinguishes from hypoaldosteronism |
| Urinary calcium | Elevated (hypercalciuria) | HP:0002150 |
| eGFR | Normal | rules out renal failure |
| Urinary exosomal NCC | Increased NCC abundance | supportive, research/translational ([PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)) |

**Genetic testing (confirmatory).** Diagnosis is confirmed by molecular testing of the four FHHt genes — WNK1, WNK4, KLHL3, CUL3 — via next-generation sequencing (gene panel or exome), with attention to splice-site variants causing CUL3 exon-9 skipping. Network-medicine-informed diagnostic panels (e.g., PHA-X incorporating CNV detection and ACMG/AMP curation) have been proposed ([PMID: 41569463](https://pubmed.ncbi.nlm.nih.gov/41569463/)). Genetic testing is indispensable for precise subtyping, which directs etiology-specific management and prognostication ([PMID: 41982973](https://pubmed.ncbi.nlm.nih.gov/41982973/)).

**Differential diagnosis.** PHAII must be distinguished from conditions producing *hypotension*: PHA type I (salt-wasting, hypotension, elevated aldosterone), type 4 RTA/hypoaldosteronism (aldosterone deficiency, low BP), and other causes of hyperkalemia (renal failure, drugs). The discriminating feature is the direction of blood pressure: *"Hyperabsorption of chloride in the distal nephron leads to pseudohypoaldosteronism type II, which is linked with hypertension, whereas blood pressure in the other mentioned disorders is decreased"* ([PMID: 6384650](https://pubmed.ncbi.nlm.nih.gov/6384650/)). A **spectacular therapeutic response to thiazide** also serves as a diagnostic pointer ([PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/)).

**Screening.** No newborn or population screening program exists; cascade genetic testing of first-degree relatives is appropriate once a familial variant is identified, though *de novo* status is common in CUL3.

---

## 11. Outcome / Prognosis

PHA2E is a **chronic, lifelong but highly treatable** condition with an **excellent prognosis when diagnosed and treated**. Thiazide diuretics produce dramatic ("spectacular") normalization of blood pressure and kalemia ([PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/)).

- **Survival/mortality:** Not a directly lethal disorder when treated; life expectancy is expected to be near-normal with therapy. Severe untreated hyperkalemia can cause life-threatening cardiac arrhythmia.
- **Morbidity:** Untreated or late-diagnosed disease causes morbidity — *"persistent metabolic acidosis and hypertension may lead to significant growth and developmental impairments in pediatric patients"* ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)). Chronic hypertension carries the usual long-term cardiovascular/renal end-organ risks if uncontrolled.
- **Prognostic factors:** Timeliness of diagnosis and treatment adherence are the dominant determinants. *"A timely diagnosis of FHH is important for effective management of hypertension, electrolyte imbalance correction with tailored treatment, and genetic counseling"* ([PMID: 39229746](https://pubmed.ncbi.nlm.nih.gov/39229746/)).
- **Recovery potential:** The biochemical and hemodynamic abnormalities are fully reversible with thiazide therapy; genotype-specific (NCC-targeted) treatment is highly effective.

---

## 12. Treatment

**First-line pharmacotherapy — thiazide diuretics.** Thiazides directly inhibit the hyperactivated NCC, reversing hypertension, hyperkalemia, and acidosis — often with dramatic effect. Boyden et al.: *"Disease features are reversed by thiazide diuretics, which inhibit the Na-Cl cotransporter in the distal nephron of the kidney; KLHL3 and CUL3 are expressed in this location"* ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). Glover et al. confirm FHHt *"is effectively treated by thiazide diuretics and/or dietary salt restriction"* ([PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)). NCIT: thiazide diuretic (e.g., hydrochlorothiazide, NCIT:C29181); chlorthalidone.

**Dietary / supportive measures.** Sodium (salt) restriction reduces substrate for NaCl retention; potassium restriction and, if needed, potassium-binding resins address hyperkalemia. Klaus: *"sodium restriction and chloruretic diuretics (thiazide) in type II of pseudohypoaldosteronism"* ([PMID: 6384650](https://pubmed.ncbi.nlm.nih.gov/6384650/)).

**Treatment strategy / personalized medicine.** PHA2E is a model of genotype-guided therapy: identifying a CUL3/KLHL3-WNK pathway defect directs clinicians specifically to NCC-blocking thiazides rather than empirical antihypertensives. The CUL3/KLHL3–WNK–SPAK/OSR1 pathway is itself being pursued as a target for novel antihypertensive agents, with the appeal that *"its inhibition may not only reduce renal sodium reabsorption along multiple segments but may also reduce vascular tone"* ([PMID: 27076645](https://pubmed.ncbi.nlm.nih.gov/27076645/)).

**Advanced/experimental therapeutics:** No gene therapy, cell therapy, or RNA-based therapy is clinically available or in trials specifically for PHA2E; the pathway (WNK/SPAK inhibitors) is at the preclinical/translational stage.

**Treatment outcomes and adverse events:** Response is typically excellent and rapid. Thiazide adverse effects to monitor include hypokalemia (useful here, as it counters the hyperkalemia), hyponatremia, hyperuricemia, and volume depletion; doses are titrated to normalize potassium and blood pressure.

---

## 13. Prevention

- **Primary prevention:** Not applicable as a genetic *de novo* disorder — occurrence cannot be prevented. Risk-factor modification (salt restriction) prevents symptomatic worsening.
- **Secondary prevention (early detection):** Measuring blood pressure in children and recognizing the hyperkalemia/acidosis/hypertension triad enables early diagnosis; the title of [PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/) itself stresses "the importance of measuring blood pressure in children." Early thiazide treatment prevents growth/developmental complications.
- **Tertiary prevention:** Ongoing thiazide therapy plus dietary salt/potassium management prevents hypertensive end-organ damage and hyperkalemic arrhythmia.
- **Genetic counseling:** Important for affected families — explaining autosomal-dominant transmission (50% risk to offspring of an affected individual) and the predominantly *de novo* origin in CUL3. Cascade genetic testing and counseling are recommended ([PMID: 39229746](https://pubmed.ncbi.nlm.nih.gov/39229746/)).
- **Immunization / public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** CUL3 is highly conserved. Mouse *Cul3* (NCBI Gene 26554; *Mus musculus*, NCBI Taxon 10090) is the principal experimental ortholog. The WNK-SPAK/OSR1-NCC signaling axis is conserved across mammals.
- **Natural disease in other species:** No well-documented naturally occurring CUL3-exon-9 Gordon syndrome equivalent is established in companion animals or wildlife (no specific OMIA entry identified for this exact condition in the reviewed literature).
- **Comparative biology:** The knock-in mouse (below) recapitulates the human disease closely, demonstrating strong evolutionary conservation of the disease mechanism.
- **Transmission / zoonosis:** Not applicable — PHA2E is a non-transmissible genetic disorder.

---

## 15. Model Organisms

**Primary model — CUL3Δ403-459 knock-in mouse.** A knock-in mouse carrying the PHA2E deletion faithfully recapitulates the disease: *"Deletion of exon 9 from CUL3 (affecting residues 403-459, CUL3(Δ403-459)) causes a severe form of FHHt (PHA2E) that is recapitulated closely in a knock-in mouse model"* ([PMID: 27378813](https://pubmed.ncbi.nlm.nih.gov/27378813/)).

| Model | Type | Key findings | Reference |
|---|---|---|---|
| CUL3^WT/Δ403-459^ knock-in mouse | Mammalian, knock-in (heterozygous) | Recapitulates hyperkalemia/hypertension; reveals arterial pulse-waveform changes = vascular component | [PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/) |
| CUL3Δ403-459 mouse (ROMK study) | Mammalian, knock-in | NCC activation via WNK accumulation; ROMK expression unaltered → hyperkalemia from reduced distal Na⁺ delivery | [PMID: 27378813](https://pubmed.ncbi.nlm.nih.gov/27378813/) |
| Renal CSN (JAB1)-deficient mouse | Mammalian, conditional (Pax8/LC1) | Deficient COP9-signalosome binding contributes importantly to the FHHt phenotype | [PMID: 30301860](https://pubmed.ncbi.nlm.nih.gov/30301860/) |
| DCT-specific CSN disruption mouse | Mammalian, conditional | DCT-specific CSN disruption (not CUL3 itself) causes tubular injury | [PMID: 39205661](https://pubmed.ncbi.nlm.nih.gov/39205661/) |
| Cultured kidney cells expressing Cul3Δ403-459 | In vitro | Dissected dual gain/loss of function; JAB1 fails to bind deleted 4-helix bundle | [PMID: 29897280](https://pubmed.ncbi.nlm.nih.gov/29897280/) |

**Phenotype recapitulation:** Excellent — the knock-in mouse reproduces the renal electrolyte/hypertension phenotype and additionally uncovered the vascular contribution not previously appreciated. **Limitations:** Mouse models of the mutant have been central to resolving the still-debated balance of gain-of-function vs loss-of-function mechanisms ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/)); subtle human features (dental abnormalities, growth retardation) are less emphasized in models. **Applications:** Dissecting the CUL3-CSN-WNK-SPAK-NCC cascade, testing WNK/SPAK inhibitors, and probing renal vs vascular contributions to hypertension.

---

## Key Findings (with evidence)

### F1 — PHA2E is caused by dominant, predominantly *de novo* CUL3 mutations causing exon-9 skipping
Boyden et al. (2012) identified CUL3 and KLHL3 as PHAII genes across 41 families; CUL3 mutations are dominant and predominantly *de novo*, and diverse mutations converge on exon-9 skipping (CUL3Δ403-459). *"KLHL3 mutations are either recessive or dominant, whereas CUL3 mutations are dominant and predominantly de novo"* and *"Diverse CUL3 mutations all result in skipping of exon 9, producing an in-frame deletion"* ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)).

### F2 — Mechanism: CUL3-Δ9 abrogates WNK degradation, hyperactivating SPAK/OSR1-NCC
*"In CUL3-∆9-mediated FHHt, proteasomal degradation of WNKs is abrogated, leading to overactivation of the WNK targets [SPAK] and oxidative stress-response kinase-1, which directly phosphorylate and activate the thiazide-sensitive Na[-Cl cotransporter]"* ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/)); NCC hyperactivation occurs along the DCT, producing hypertension and hyperkalemia ([PMID: 39699086](https://pubmed.ncbi.nlm.nih.gov/39699086/)).

### F3 — CUL3 causes the most severe FHHt; thiazides reverse it
*"Autosomal dominant mutations in cullin-3 (Cul3) cause the most severe form of familial hyperkalemic hypertension (FHHt)"* ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/)); disease features reverse with thiazides ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)).

### F4 — A CUL3Δ403-459 knock-in mouse recapitulates PHA2E
*"Deletion of exon 9 from CUL3 ... causes a severe form of FHHt (PHA2E) that is recapitulated closely in a knock-in mouse model"* ([PMID: 27378813](https://pubmed.ncbi.nlm.nih.gov/27378813/)).

### F5 — The mutant auto-ubiquitylates and loses CSN/CAND1 binding (explains severity)
*"the PHA2E mutant, CUL3(Δ403-459), is severely compromised in its ability to ubiquitylate WNKs ... Instead, CUL3(Δ403-459) auto-ubiquitylates and loses interaction with two important Cullin regulators: the COP9-signalosome and CAND1"*; *"These findings may explain the severity of the FHHt phenotype caused by CUL3 mutations compared to those reported in KLHL3 or WNK kinases"* ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/)); dual gain/loss of function and JAB1/CSN disruption ([PMID: 29897280](https://pubmed.ncbi.nlm.nih.gov/29897280/); [PMID: 30301860](https://pubmed.ncbi.nlm.nih.gov/30301860/)).

### F6 — PHA2E hypertension has a vascular component
*"These mice also show changes in the arterial pulse waveform, suggesting a vascular contribution to their hypertension not reported in previous FHHt models"* ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/)); the WNK-OSR1/SPAK-SLC12a cascade is present in VSMCs and regulates arterial tone ([PMID: 26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/)).

### F7 — Full clinical phenotype
*"The typical clinical picture ... includes ... arterial hypertension and dyskaliemia, hyperchloremia metabolic acidosis, hypercalciuria, a low rate of renin, and most frequently, a normal or high rate of aldosterone. Dental abnormalities and growth retardation can also be associated"* ([PMID: 27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/)); growth/developmental impairment from persistent acidosis/hypertension ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/) | *Mutations in KLHL3 and CUL3 cause hypertension and electrolyte abnormalities* | Landmark: identifies CUL3 cause, exon-9 skipping, *de novo* dominance, thiazide reversal |
| [29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/) | *Mechanisms and controversies in mutant Cul3-mediated FHHt* | Core mechanism; CUL3 = most severe FHHt |
| [39699086](https://pubmed.ncbi.nlm.nih.gov/39699086/) | *Familial Hyperkalemic Hypertension* | NCC/DCT localization of lesion |
| [26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/) | *Characterisation of the Cullin-3 mutation...* | Protein dysfunction; CSN/CAND1 loss; vascular component |
| [29897280](https://pubmed.ncbi.nlm.nih.gov/29897280/) | *Dual gain and loss of cullin 3 function...* | Mechanistic dissection; JAB1/CSN |
| [30301860](https://pubmed.ncbi.nlm.nih.gov/30301860/) | *Renal COP9 Signalosome Deficiency...* | CSN binding deficiency drives FHHt |
| [27378813](https://pubmed.ncbi.nlm.nih.gov/27378813/) | *ROMK expression unaltered in CUL3Δ403-459 mouse* | Knock-in model; hyperkalemia mechanism |
| [26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/) | *KLHL3/CUL3 ubiquitin ligase and WNK signaling...* | Vascular smooth muscle pathway |
| [27076645](https://pubmed.ncbi.nlm.nih.gov/27076645/) | *The CUL3/KLHL3-WNK-SPAK/OSR1 pathway as antihypertensive target* | Pathway definition; drug target |
| [27369102](https://pubmed.ncbi.nlm.nih.gov/27369102/) | *Gordon syndrome: BP measurement in children* | Clinical phenotype; CUL3 pediatric case; thiazide response |
| [41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/) | *Diagnostic pitfalls... 9-year follow-up of early-onset PHAII* | Morbidity; growth/developmental impairment |
| [24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/) | *Detection of mutations in KLHL3 and CUL3 in FHHt families* | Epidemiology; treatment |
| [39229746](https://pubmed.ncbi.nlm.nih.gov/39229746/) | *Prevalence of Hyperkalemia and FHHt in 5100 patients* | Rarity; diagnosis importance |
| [11903313](https://pubmed.ncbi.nlm.nih.gov/11903313/) | *Phenotypic/genetic heterogeneity of FHHt* | Historical epidemiology; AD inheritance; variable expressivity |
| [6384650](https://pubmed.ncbi.nlm.nih.gov/6384650/) | *Primary hypoaldosteronism, pseudo-hypoaldosteronism...* | Differential diagnosis; thiazide treatment |
| [41569463](https://pubmed.ncbi.nlm.nih.gov/41569463/) | *PHA demystification; diagnostic panels* | Diagnostic panel design |
| [41982973](https://pubmed.ncbi.nlm.nih.gov/41982973/) | *Chinese children with PHA case series* | Value of genetic subtyping |

---

## Limitations and Knowledge Gaps

1. **Precise epidemiology unknown:** No reliable prevalence/incidence estimate exists for the CUL3 subtype specifically; it is simply "very rare." Case counts are small.
2. **Mechanistic controversy:** The relative contributions of gain-of-function (auto-ubiquitylation, altered substrate repertoire, KLHL3 degradation) versus loss-of-function (impaired WNK ubiquitylation) remain debated ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/); [PMID: 29897280](https://pubmed.ncbi.nlm.nih.gov/29897280/)).
3. **Vascular contribution not fully quantified in humans:** The vascular component is demonstrated in mice ([PMID: 26286618](https://pubmed.ncbi.nlm.nih.gov/26286618/)); its magnitude in human PHA2E is inferred, not directly measured.
4. **Limited data on non-renal phenotypes:** Dental abnormalities and growth retardation are reported as associations, but their frequency, mechanism, and reversibility are not well quantified.
5. **No omics datasets** (transcriptomic/proteomic/metabolomic) specific to PHA2E patient tissue were available in this investigation; molecular profiling evidence is derived from mechanistic cell/mouse studies.
6. **No formal modifier genes or genotype-phenotype correlation** within CUL3 variants is established beyond the shared exon-9-skipping outcome.

---

## Proposed Follow-up Experiments / Actions

1. **Human vascular phenotyping:** Measure arterial stiffness/pulse-wave velocity in genetically confirmed PHA2E patients to test whether the mouse-observed vascular component is clinically relevant and whether it responds to thiazides.
2. **Natural-history registry:** Establish a CUL3-specific FHHt registry to quantify age of onset, penetrance, growth/dental outcomes, and long-term cardiovascular/renal endpoints with and without early treatment.
3. **CSN/neddylation-targeted studies:** Given that loss of CSN/JAB1 binding is central to CUL3 severity, test whether modulating neddylation (e.g., NEDD8-pathway tools) in the knock-in mouse corrects NCC hyperactivation — a potential precision-therapy avenue.
4. **WNK/SPAK inhibitor translation:** Advance preclinical WNK-SPAK/OSR1 inhibitors in the CUL3Δ403-459 mouse, directly comparing renal and vascular blood-pressure effects against thiazide.
5. **Patient-derived omics:** Perform transcriptomic/proteomic profiling of patient-derived cells or urinary exosomes (NCC abundance) to develop non-invasive biomarkers of disease activity and treatment response ([PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)).
6. **Growth-impairment mechanism:** Investigate whether early acidosis correction fully rescues growth in pediatric PHA2E, clarifying the critical intervention window.

---

### Ontology Term Appendix

- **MONDO:** MONDO:0013782 (PHA2E)
- **Gene (HGNC):** CUL3 (HGNC:2553)
- **HPO:** HP:0000822 (Hypertension), HP:0002153 (Hyperkalemia), HP:0004879/HP:0001947 (Hyperchloremic metabolic acidosis), HP:0002150 (Hypercalciuria), HP:0001510 (Growth delay), HP:0000164 (Dental abnormality)
- **GO (BP):** GO:0000209 (protein polyubiquitination), GO:0045116 (protein neddylation), GO:0035725 (sodium ion transmembrane transport), GO:0008217 (regulation of blood pressure)
- **GO (CC):** GO:0031463 (Cul3-RING ubiquitin ligase complex), GO:0005737 (cytoplasm), GO:0016020 (membrane)
- **CL:** CL:1000768 (kidney distal convoluted tubule epithelial cell), CL:0000359 (vascular associated smooth muscle cell)
- **UBERON:** UBERON:0002113 (kidney), UBERON:0001292 (distal convoluted tubule), UBERON:0004535 (cardiovascular system)
- **CHEBI:** thiazide diuretics (e.g., hydrochlorothiazide), sodium chloride, potassium
- **NCIT:** Thiazide diuretic / hydrochlorothiazide (antihypertensive intervention)

---

*Report compiled from autonomous iterative investigation (5 iterations, 13 confirmed findings, 30 papers reviewed). Evidence source types span human clinical case reports/series, model-organism (mouse knock-in) studies, and in vitro mechanistic studies, as noted throughout.*


## Artifacts

- [OpenScientist final report](Pseudohypoaldosteronism_Type_2E-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pseudohypoaldosteronism_Type_2E-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013782` (3 mentions) - the report calls it "MONDO", "PHA2E"; MONDO calls it **pseudohypoaldosteronism type 2E**
- `HP:0002153` (3 mentions) - the report calls it "Laboratory abnormality", "Elevated (hyperkalemia)", "Hyperkalemia"; HP calls it **Hyperkalemia**
- `HP:0004879` (3 mentions) - the report calls it "Hyperchloremia, low HCO₃ (metabolic acidosis)"; HP calls it **Intermittent hyperventilation**
- `HP:0002150` (3 mentions) - the report calls it "Laboratory abnormality", "Elevated (hypercalciuria)", "Hypercalciuria"; HP calls it **Hypercalciuria**
- `HP:0004322` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Short stature**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001947` (2 mentions) - the report calls it "Hyperchloremic metabolic acidosis"; HP calls it **Renal tubular acidosis**
- `HP:0000164` (2 mentions) - the report calls it "Abnormality of the teeth", "Dental abnormality"; HP calls it **Abnormality of the dentition**, and lists "Abnormality of the teeth" among its other names
- `GO:0000209` (3 mentions) - the report calls it "Cellular processes:** Protein polyubiquitination", "protein polyubiquitination"; GO calls it **protein polyubiquitination**
- `GO:0031463` (4 mentions) - the report calls it "Cul3-RING ligase complex", "Cul3-RING ubiquitin ligase complex"; GO calls it **Cul3-RING ubiquitin ligase complex**
- `CL:1000768` (3 mentions) - the report calls it "kidney distal convoluted tubule epithelial cell"; CL calls it **kidney connecting tubule epithelial cell**
- `UBERON:0002113` (2 mentions) - the report calls it "Primary organ:** Kidney", "kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `UBERON:0001292` (2 mentions) - the report calls it "renal distal convoluted tubule (DCT)", "distal convoluted tubule"; UBERON calls it **distal convoluted tubule**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0013782` - called "MONDO", "PHA2E"
- `HP:0002153` - called "Laboratory abnormality", "Elevated (hyperkalemia)", "Hyperkalemia"
- `HP:0002150` - called "Laboratory abnormality", "Elevated (hypercalciuria)", "Hypercalciuria"
- `HP:0000164` - called "Abnormality of the teeth", "Dental abnormality"
- `GO:0000209` - called "Cellular processes:** Protein polyubiquitination", "protein polyubiquitination"
- `GO:0031463` - called "Cul3-RING ligase complex", "Cul3-RING ubiquitin ligase complex"
- `UBERON:0002113` - called "Primary organ:** Kidney", "kidney"
- `UBERON:0001292` - called "renal distal convoluted tubule (DCT)", "distal convoluted tubule"