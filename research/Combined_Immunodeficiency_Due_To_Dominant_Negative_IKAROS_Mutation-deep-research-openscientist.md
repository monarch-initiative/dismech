---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T19:17:46.088749'
end_time: '2026-10-20T20:15:58.805980'
duration_seconds: 3492.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Immunodeficiency Due To Dominant Negative IKAROS Mutation
  mondo_id: MONDO:0979316
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
citation_count: 16
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 13
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 35
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 10
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0002718
    reported_labels:
    - Common
    ontology_label: Recurrent bacterial infections
  - term_id: HP:0004429
    reported_labels:
    - Common
    ontology_label: Recurrent viral infections
  - term_id: HP:0004313
    reported_labels:
    - High
    ontology_label: Decreased circulating immunoglobulin concentration
  - term_id: HP:0001875
    reported_labels:
    - Present
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0001877
    reported_labels:
    - Present
    ontology_label: Abnormal erythrocyte morphology
  - term_id: HP:0012335
    reported_labels:
    - Present
    ontology_label: obsolete Abnormality of folate metabolism
  - term_id: HP:0006721
    reported_labels:
    - ~1/7 (T-ALL in index cohort)
    ontology_label: Acute lymphoblastic leukemia
  - term_id: UBERON:0002371
    reported_labels:
    - bone marrow
    - "Organ/system level:** Immune/hematopoietic system \u2014 **bone marrow"
    ontology_label: bone marrow
  - term_id: NCIT:C309
    reported_labels:
    - Sulfamethoxazole/Trimethoprim
    ontology_label: Biotin
  - term_id: NCIT:C564
    reported_labels:
    - Immunoglobulin Therapy
    ontology_label: Ifosfamide
  labels_variant: 4
  obsolete_terms:
  - term_id: HP:0012335
    ontology_label: obsolete Abnormality of folate metabolism
    replaced_by: HP:0040087
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Immunodeficiency_Due_To_Dominant_Negative_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Immunodeficiency_Due_To_Dominant_Negative_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Immunodeficiency Due To Dominant Negative IKAROS Mutation
- **MONDO ID:** MONDO:0979316 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Immunodeficiency Due To Dominant Negative IKAROS Mutation** covering all of the
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

# Combined Immunodeficiency Due to Dominant-Negative IKAROS Mutation — Comprehensive Disease Report

**Target disease:** Combined Immunodeficiency Due To Dominant Negative IKAROS Mutation
**MONDO ID:** MONDO:0979316
**Gene:** *IKZF1* (IKAROS), HGNC:13176, chromosome 7p12.2
**Category:** Mendelian inborn error of immunity (IEI); autosomal dominant

---

## Summary

Combined Immunodeficiency Due to Dominant-Negative IKAROS Mutation is a rare, early-onset, autosomal-dominant inborn error of immunity caused by heterozygous (usually *de novo*) germline missense variants in the **DNA-binding zinc-finger domain of *IKZF1*/IKAROS**, prototypically affecting residue **asparagine 159 (N159S, N159T)**. Unlike the milder haploinsufficiency form of IKZF1 disease, these variants act through a **dominant-negative mechanism**: the mutant protein retains its dimerization capacity but loses DNA binding and pericentromeric heterochromatin targeting, so it sequesters wild-type IKAROS into non-functional complexes and cripples IKAROS's role as a master hematopoietic transcription factor and tumor suppressor.

The clinical consequence is a **combined (T, B, and myeloid) immunodeficiency**. Patients present in early childhood with B lymphopenia and hypogammaglobulinemia, a predominance of naive T cells that cannot mature into effector/memory cells, neutropenia and eosinopenia, and reduced myeloid dendritic cells and monocyte dysfunction. The hallmark infectious complication is **near-universal *Pneumocystis jirovecii* pneumonia (PJP)**, alongside other bacterial and viral infections, and there is a predisposition to **acute lymphoblastic leukemia (ALL)**. In the landmark cohort of 7 unrelated patients (Boutboul et al., JCI 2018), all 7 had PJP and one developed T-cell ALL.

The disease sits within a broader, mechanism-based *IKZF1* disease spectrum: loss-of-function by haploinsufficiency (CVID-like antibody deficiency), loss-of-function dominant-negative (this combined immunodeficiency), and gain-of-function variants (immune dysregulation, hypergammaglobulinemia/IgG4-RD, malignancy). Management combines **co-trimoxazole PJP prophylaxis** and **immunoglobulin replacement** as supportive care, with **allogeneic hematopoietic stem-cell transplantation (HSCT)** as the only curative therapy. Paralogous diseases caused by dominant-negative variants in the related IKAROS-family genes *IKZF3* (AIOLOS) and *IKZF2* (HELIOS) strongly corroborate the heterodimeric-interference mechanism.

---

## Key Findings

### Finding 1 — Dominant-negative N159 IKZF1 variants cause early-onset T, B, and myeloid combined immunodeficiency with universal PJP

The defining clinical description comes from Boutboul et al. (JCI 2018), who reported **7 unrelated patients** with a novel early-onset combined immunodeficiency associated with *de novo* germline heterozygous *IKZF1* mutations affecting **amino acid N159 in the DNA-binding domain**. As the authors state: *"we report 7 unrelated patients with a novel early-onset combined immunodeficiency associated with de novo germline IKZF1 heterozygous mutations affecting amino acid N159 located in the DNA-binding domain of IKZF1. Different bacterial and viral infections were diagnosed, but Pneumocystis jirovecii pneumonia was reported in all patients. One patient developed a T cell ALL."* ([PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/))

The immunophenotype is multilineage. The same study found: *"This immunodeficiency was characterized by innate and adaptive immune defects, including low numbers of B cells, neutrophils, eosinophils, and myeloid dendritic cells, as well as T cell and monocyte dysfunctions. Notably, most T cells exhibited a naive phenotype and were unable to evolve into effector memory cells."* ([PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/))

This distinguishes the dominant-negative combined immunodeficiency from the B-cell-restricted phenotype of IKZF1 haploinsufficiency: the defect spans **adaptive (T and B)** and **innate/myeloid (neutrophils, eosinophils, dendritic cells, monocytes)** compartments simultaneously.

### Finding 2 — IKZF1 variants cause distinct diseases depending on molecular mechanism

Two loss-of-function mechanisms of germline *IKZF1* variants yield two clinically distinct entities. Nunes-Santos, Kuehn & Rosenzweig (2020) state: *"Mutations acting by haploinsufficiency present with a common variable immune deficiency-like phenotype mainly characterized by increased susceptibility to infections. Mutations acting in a dominant negative fashion present with a combined immunodeficiency phenotype with high prevalence of Pneumocystis jirovecii pneumonia."* ([PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/))

The 2021 Kuehn review generalizes this genotype–mechanism–phenotype framework: *"These allelic variants, acting by either haploinsufficiency or dominant negative mechanisms affecting particular functions of IKAROS, are associated with common variable immunodeficiency, combined immunodeficiency, or primarily hematologic phenotypes in affected patients."* ([PMID: 33392855](https://pubmed.ncbi.nlm.nih.gov/33392855/))

This is the central organizing principle of the disease: the **dominant-negative class specifically produces the combined immunodeficiency with PJP**, whereas haploinsufficiency produces a milder, more humorally restricted CVID-like disease.

### Finding 3 — Molecular mechanism: loss of DNA binding + retained dimerization = heterodimeric sequestration

IKAROS targets genes for heritable silencing by localizing to pericentromeric heterochromatin, and this localization is a direct functional readout of its activity. Cobb et al. (2000) showed that *"targeting was dependent on the amino-terminal DNA-binding zinc finger domain and carboxy-terminal dimerization domain of Ikaros,"* with a close correlation between DNA binding and pericentromeric localization ([PMID: 10970879](https://pubmed.ncbi.nlm.nih.gov/10970879/)).

Because N159 lies within the DNA-binding zinc fingers, variants there abolish DNA binding while preserving dimerization. A human congenital-pancytopenia case with a DNA-binding zinc-finger substitution demonstrated the lesion directly: Goldman et al. (2012) reported that *"the observed mutation decreased Ikaros DNA-binding affinity, and immunofluorescence microscopy revealed aberrant Ikaros pericentromeric localization."* ([PMID: 21548011](https://pubmed.ncbi.nlm.nih.gov/21548011/))

Since IKAROS homo- and heterodimerizes, a DNA-binding-dead but dimerization-competent mutant **drags wild-type IKAROS off chromatin**, explaining the dominance. This heterodimeric-interference logic was formally proven for the paralog AIOLOS: Yamashita et al. (2021) showed that removing the dimerization capacity of mutant AIOLOS restored normal development, establishing *"Heterodimeric interference is a new mechanism of autosomal dominance that causes inborn errors of immunity by impairing protein function via the mutation of its heterodimeric partner."* ([PMID: 34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/))

### Finding 4 — IKAROS is a master hematopoietic transcription factor and tumor suppressor

IKAROS's broad hematopoietic role explains both the multilineage immunodeficiency and the leukemia risk. The 2021 Kuehn review summarizes: *"IKAROS, encoded by IKZF1, is a zinc finger transcription factor and a critical regulator of hematopoiesis. Mutations in IKZF1 have been implicated in immune deficiency, autoimmunity, and malignancy in humans. Somatic IKZF1 loss-of-function mutations and deletions have been shown to increase predisposition to the development of B cell acute lymphoblastic leukemia (B-ALL)."* ([PMID: 33392855](https://pubmed.ncbi.nlm.nih.gov/33392855/))

IKAROS is not restricted to lymphoid cells. Francis et al. (2011) note that *"Ikaros has been shown to regulate hematopoietic stem cell renewal, as well as the development and function of cells from multiple hematopoietic lineages, including the myeloid lineage"* ([PMID: 21765977](https://pubmed.ncbi.nlm.nih.gov/21765977/)) — accounting for the neutropenia, eosinopenia, and dendritic-cell deficits in the combined immunodeficiency. Its tumor-suppressor function underlies the ALL predisposition seen clinically (one of seven N159 patients developed T-ALL).

### Finding 5 — Mouse knock-in models recapitulate human IKAROS DNA-binding-domain disease

Causality is supported by animal models. Boast et al. (2021) generated mice carrying a point mutation in IKAROS zinc finger 1 (ZF1) and demonstrated it causes a B-cell deficiency, modeling the human DNA-binding-domain phenotype ([PMID: 33658297](https://pubmed.ncbi.nlm.nih.gov/33658297/)). For the paralog AIOLOS, Kuehn et al. (2021) showed that the human p.N160S variant (the direct analog of IKAROS N159S) *"was recapitulated in a murine model carrying the corresponding human mutation,"* with the mutant protein failing DNA binding and pericentromeric targeting and exerting a dominant-negative effect ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)).

The dose-dependence of IKAROS function is illustrated by classic genetics: Schmitt et al. (2002) note that *"inactivation of Ikaros family proteins leads to a complete absence of T, B, NK and dendritic cells, whereas a reduction of Ikaros activity induce hyperproliferation and lymphomas"* ([PMID: 11997672](https://pubmed.ncbi.nlm.nih.gov/11997672/)) — spanning immunodeficiency to lymphoproliferation, mirroring the human spectrum.

### Finding 6 — Management: PJP prophylaxis, immunoglobulin replacement, and allogeneic HSCT

Because the disease is a combined immunodeficiency with near-universal PJP and antibody deficiency, standard supportive care is **trimethoprim-sulfamethoxazole (co-trimoxazole) PJP prophylaxis** plus **immunoglobulin replacement therapy** — the established approach for combined immunodeficiencies with PJP risk and humoral failure (illustrative management: *"clinically stable on immunoglobulin replacement therapy and trimethoprim-sulfamethoxazole prophylaxis"* [PMID: 22982295](https://pubmed.ncbi.nlm.nih.gov/22982295/)).

**Allogeneic HSCT is the only curative therapy.** In the related IKAROS gain-of-function disease, Klangkalya et al. (2024) reported that *"HCT was well-tolerated achieving full engraftment in both patients receiving reduced intensity, matched unrelated donor grafts, with no severe acute or chronic graft-vs-host-disease, and in remission from their diseases 2.5 and 4 years post-HCT, respectively. These results suggest that HCT is a valid and curative option"* ([PMID: 38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/)).

### Finding 7 — The disease sits within a four-class IKZF1 genotype–mechanism–phenotype spectrum

Germline *IKZF1* variants produce at least four functional classes with distinct diseases:

| Class | Mechanism | Representative variant | Phenotype |
|-------|-----------|------------------------|-----------|
| 1 | Loss-of-function, **haploinsufficiency** | N-terminal/various | CVID-like antibody deficiency |
| 2 | Loss-of-function, **dominant-negative** (DNA-binding domain) | **N159S / N159T** | **Combined immunodeficiency + PJP (this disease)** |
| 3 | **Gain-of-function** | R183H | Hypergammaglobulinemia, IgG4-RD, autoimmunity, B-cell malignancy |
| 4 | **Gain-of-function by loss-of-phosphorylation** | (ZF cell-cycle) | Immune dysregulation |

García-Solís et al. (2024) frame the loss- vs gain-of-function contrast: *"Monoallelic loss-of-function IKZF1 (IKAROS) variants cause B-cell deficiency or combined immunodeficiency, whereas monoallelic gain-of-function (GOF) IKZF1 variants have recently been reported to cause hypergammaglobulinemia, abnormal plasma cell differentiation, autoimmune and allergic manifestations, and infections."* ([PMID: 38579942](https://pubmed.ncbi.nlm.nih.gov/38579942/))

A systematic functional study localized impactful variants to the functional domains: Kuehn et al. (2026) provide *"a comprehensive description of the biologic impact of 81 previously unreported and/or untested IKAROS variants, including 33 patient-detected germ line VUS and 48 laboratory-generated mutations in the dimerization domain."* ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/))

---

## Full Disease Characterization by Section

### 1. Disease Information

**Overview:** A Mendelian, autosomal-dominant inborn error of immunity in which a heterozygous germline missense variant in the DNA-binding zinc-finger domain of *IKZF1* acts dominant-negatively to disrupt IKAROS-dependent hematopoiesis, producing an early-onset combined (T, B, myeloid) immunodeficiency with near-universal *Pneumocystis jirovecii* pneumonia and leukemia predisposition.

**Key identifiers:**
- **MONDO:** MONDO:0979316
- **Gene/OMIM:** *IKZF1* gene OMIM 603023. The IKZF1-associated immunodeficiency phenotype series includes OMIM #616873 (Immunodeficiency, common variable, 13 — IKZF1 haploinsufficiency); the dominant-negative combined immunodeficiency is described in the literature as a distinct clinical entity (Boutboul 2018) within the IKZF1 disease spectrum.
- **HGNC:** 13176
- **Orphanet / ICD-11 / MeSH:** No disease-specific dedicated codes; classified under combined immunodeficiencies / primary immunodeficiency (ICD-11 4A00 range; MeSH "Severe Combined Immunodeficiency"/"Immunologic Deficiency Syndromes" are the closest aggregate terms).

**Synonyms / alternative names:** Dominant-negative IKZF1 combined immunodeficiency; IKAROS DNA-binding-domain combined immunodeficiency; IKZF1 N159S/N159T combined immunodeficiency; IKAROS-associated T, B and myeloid combined immunodeficiency.

**Information source:** Derived from aggregated case series and disease-level reviews (Boutboul 2018 cohort of 7 patients; Kuehn/Nunes-Santos reviews), not from large EHR datasets. This is a very rare disease described in small numbers of individual patients.

### 2. Etiology

**Causal factor:** Genetic — heterozygous germline missense variant in the *IKZF1* DNA-binding zinc-finger domain (prototypically N159S/N159T), usually arising *de novo*. No environmental or infectious cause initiates the disease; infections are downstream consequences.

**Genetic risk factors:** The causal variant itself is the sole primary genetic driver. The dominant-negative effect requires an intact dimerization domain (so the mutant can hijack wild-type IKAROS). Modifier genes are not defined, but paralog dosage (AIOLOS, HELIOS, which heterodimerize with IKAROS) is biologically plausible as a modifier.

**Environmental/lifestyle risk factors:** None established as causal. Pathogen exposure (notably *Pneumocystis jirovecii*) determines which infections manifest but does not cause the immunodeficiency.

**Protective factors:** None genetically defined. Early diagnosis, prophylaxis, and transplantation are the practical determinants of outcome.

**Gene–environment interaction:** The genetic lesion sets a permissive state for opportunistic infection; environmental pathogen exposure converts latent immunodeficiency into clinical disease (e.g., PJP). No classical GxE modifier data exist.

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|-----------|------|-------|-----------|---------------|
| *Pneumocystis jirovecii* pneumonia | Clinical/infectious | Early childhood | 7/7 (universal in index cohort) | HP:0002090 (Pneumonia); HP:0032262 (Pneumocystis pneumonia) |
| Recurrent bacterial infections | Clinical/infectious | Childhood | Common | HP:0002718 |
| Recurrent viral infections | Clinical/infectious | Childhood | Common | HP:0004429 |
| B lymphopenia | Lab abnormality | Congenital/childhood | High | HP:0010976 (B lymphocytopenia) |
| Hypogammaglobulinemia | Lab abnormality | Childhood | High | HP:0004313 |
| Naive-skewed T cells / impaired effector-memory differentiation | Lab/cellular | Childhood | High | HP:0005415; HP:0002846 |
| Neutropenia | Lab abnormality | Childhood | Present | HP:0001875 |
| Eosinopenia (decreased eosinophils) | Lab abnormality | Childhood | Present | HP:0001877 |
| Decreased myeloid dendritic cells | Lab/cellular | Childhood | Present | HP:0012177 (abnormal dendritic cell) |
| Monocyte dysfunction | Lab/cellular | Childhood | Present | HP:0012335 |
| Acute lymphoblastic leukemia | Neoplasm | Childhood | ~1/7 (T-ALL in index cohort) | HP:0006721 |

**Severity/progression:** Severe and progressive without treatment, given combined immunodeficiency plus malignancy risk. Severity is variable across patients but uniformly serious.

**Quality-of-life impact:** Major — recurrent/opportunistic infections, hospitalizations, lifelong prophylaxis/immunoglobulin dependence, and transplantation burden substantially impair daily functioning; disease-specific QoL instruments have not been applied to this ultra-rare cohort.

### 4. Genetic / Molecular Information

- **Causal gene:** *IKZF1* (IKAROS), HGNC:13176, OMIM 603023, chromosome 7p12.2.
- **Pathogenic variants:** Missense substitutions in the DNA-binding zinc-finger domain — prototypically **p.N159S (c.476A>G)** and **p.N159T**. Other DNA-binding-domain variants (e.g., R143W) can exert partial dominant-negative effects ([PMID: 33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/)).
- **Classification (ACMG/AMP):** Pathogenic / likely pathogenic (de novo occurrence, functional DNA-binding loss, absence from population databases).
- **Variant type:** Missense (single-nucleotide). Larger *IKZF1* deletions/truncations typically produce haploinsufficiency rather than the dominant-negative phenotype.
- **Allele frequency:** Absent from gnomAD/population databases (private, de novo variants).
- **Origin:** Germline, usually de novo heterozygous.
- **Functional consequence:** Loss of function at the protein-activity level with a **dominant-negative** mode — loss of DNA binding and pericentromeric targeting with retained dimerization, causing sequestration of wild-type IKAROS.
- **Modifier genes:** Not established.
- **Epigenetic dimension:** IKAROS operates within chromatin-remodeling (NuRD) complexes and recruits target loci to pericentromeric heterochromatin for heritable silencing; dominant-negative variants therefore produce downstream epigenetic/transcriptional dysregulation rather than being caused by epigenetic changes.
- **Chromosomal abnormalities:** Not applicable (point mutation); somatic *IKZF1* deletions are relevant to leukemia biology but not the germline disease lesion.

### 5. Environmental Information

- **Environmental/toxic factors:** None causal.
- **Lifestyle factors:** None causal.
- **Infectious agents:** *Pneumocystis jirovecii* (fungus; near-universal PJP; NCBI Taxonomy txid42068) is the signature opportunistic pathogen; various bacteria and viruses cause additional infections. These are consequences of the immunodeficiency, not causes.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A heterozygous germline missense variant arises (usually de novo) in the **DNA-binding zinc-finger domain of *IKZF1*** (e.g., N159S) → **leads to** a mutant IKAROS protein that cannot bind its DNA target motif.
2. Loss of DNA binding **results in** failure of pericentromeric heterochromatin targeting (demonstrated in analogous DNA-binding-domain variants).
3. Because the mutant retains its **C-terminal dimerization domain**, it still dimerizes with wild-type IKAROS (and paralogs) → **leads to** heterodimeric sequestration of wild-type IKAROS off chromatin (dominant-negative interference; directly proven for AIOLOS).
4. Sequestration **results in** global loss of IKAROS transcriptional/epigenetic activity within NuRD chromatin-remodeling complexes across hematopoietic progenitors.
5. Loss of IKAROS function **leads to** failure of normal lymphoid and myeloid differentiation programs → B lymphopenia/hypogammaglobulinemia; naive-skewed T cells unable to become effector/memory; neutropenia, eosinopenia, reduced dendritic cells, monocyte dysfunction.
6. The combined immune defect **results in** susceptibility to opportunistic and conventional infection — most characteristically *Pneumocystis jirovecii* pneumonia (branch: bacterial and viral infections).
7. In parallel, loss of IKAROS **tumor-suppressor** function **leads to** predisposition to acute lymphoblastic leukemia (branch; T-ALL observed clinically).

(*Steps 2–3 are partly inferred from closely analogous DNA-binding-domain variants and the AIOLOS paralog, where DNA-binding loss, mislocalization, and heterodimeric interference were directly demonstrated.*)

**Molecular pathways / processes:** IKAROS-dependent transcriptional regulation within chromatin-remodeling (NuRD) complexes; pericentromeric heterochromatin gene silencing; hematopoietic lineage commitment. Suggested GO terms: GO:0006357 (regulation of transcription by RNA Pol II), GO:0030098 (lymphocyte differentiation), GO:0002521 (leukocyte differentiation), GO:0030099 (myeloid cell differentiation), chromatin organization; cellular component GO:0005721 (pericentric heterochromatin), GO:0000785 (chromatin), GO:0005634 (nucleus).

**Cell types involved (CL):** B cells (CL:0000236), T cells (CL:0000084), hematopoietic stem cells (CL:0000037), myeloid dendritic cells (CL:0000782), neutrophils (CL:0000775), eosinophils (CL:0000771), monocytes (CL:0000576).

**Immune involvement:** Combined (innate + adaptive) immunodeficiency; not primarily autoimmune in the dominant-negative class (autoimmunity is more typical of GOF variants).

### 7. Anatomical Structures Affected

- **Organ/system level:** Immune/hematopoietic system — **bone marrow** (UBERON:0002371), **thymus** (UBERON:0002370), **spleen** (UBERON:0002106), **lymph nodes** (UBERON:0000029). Secondary involvement: **lung** (UBERON:0002048) as the principal site of PJP and other pneumonias.
- **Tissue/cell level:** Lymphoid and myeloid hematopoietic lineages (see CL terms above).
- **Subcellular level:** Nucleus (GO:0005634), pericentromeric heterochromatin (GO:0005721), chromatin / NuRD remodeling complex.
- **Localization/lateralization:** Systemic; pulmonary involvement typically bilateral (as in PJP).

### 8. Temporal Development

- **Onset:** Early childhood (effectively congenital immune defect); infections manifest in infancy/early childhood.
- **Onset pattern:** Insidious underlying immunodeficiency punctuated by acute infectious presentations (often PJP).
- **Progression:** Progressive and life-threatening without intervention; lifelong/chronic.
- **Course:** Recurrent infections; superimposed risk of leukemia.
- **Critical window:** Early diagnosis enables prophylaxis and curative HSCT before severe infections or malignancy supervene.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant, typically de novo (dominant-negative).
- **Penetrance:** High/complete for the prototypical N159 variants (all reported carriers affected).
- **Expressivity:** Variable (range of infection severity; variable leukemia occurrence).
- **Prevalence/incidence:** Ultra-rare; no population estimates — described in small case series worldwide.
- **Carrier frequency / founder effects / consanguinity:** Not applicable (de novo dominant variants, absent from population databases).
- **Sex ratio / ethnicity / geography:** No established skew; reported across unrelated families internationally.

### 10. Diagnostics

- **Immunophenotyping (flow cytometry):** Low B cells, neutropenia, eosinopenia, reduced myeloid dendritic cells; naive-predominant T cells with impaired effector-memory differentiation; monocyte dysfunction.
- **Immunoglobulins:** Hypogammaglobulinemia; impaired specific antibody responses.
- **Functional readouts (research/confirmatory):** Electrophoretic mobility shift assay (loss of DNA binding) and immunofluorescence (aberrant pericentromeric localization), plus dominant-negative cotransfection assays — as used to validate IKZF1 variants ([PMID: 21548011](https://pubmed.ncbi.nlm.nih.gov/21548011/); [PMID: 33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/)).
- **Genetic testing (definitive):** Single-gene *IKZF1* sequencing, IEI/PID gene panels, or whole-exome/whole-genome sequencing (preferred for de novo discovery). Upfront genomic sequencing is increasingly advocated for monogenic IEI ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)). Variant interpretation benefits from functional classification ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)).
- **Imaging:** Chest CT/X-ray for PJP and other pneumonias.
- **Differential diagnosis:** IKZF1 haploinsufficiency (milder CVID-like), IKZF1 GOF disease, other combined immunodeficiencies/SCID-spectrum disorders with PJP, and paralog diseases (IKZF3/AIOLOS, IKZF2/HELIOS) with overlapping phenotypes.
- **Screening:** No specific newborn screen; TREC-based SCID screening may not reliably capture this phenotype. Cascade/familial testing applies if a pathogenic variant is identified (though most are de novo).

### 11. Outcome / Prognosis

- **Natural history:** Serious; untreated combined immunodeficiency carries high morbidity/mortality from opportunistic infection, compounded by leukemia risk.
- **Prognostic factors:** Timeliness of diagnosis, infection control, and access to HSCT; development of malignancy worsens prognosis.
- **With treatment:** Supportive care (prophylaxis + Ig) stabilizes infection risk; allogeneic HSCT offers cure of the immunodeficiency and removal of the hematopoietic-intrinsic malignancy risk.
- **Complications:** PJP and other severe infections; T/B-ALL.

### 12. Treatment

| Modality | Specifics | Suggested NCIT |
|----------|-----------|----------------|
| PJP prophylaxis | Trimethoprim-sulfamethoxazole (co-trimoxazole) | NCIT:C309 (Sulfamethoxazole/Trimethoprim) |
| Antibody replacement | IVIG/SCIG immunoglobulin replacement | NCIT:C564 (Immunoglobulin Therapy) |
| Definitive/curative | Allogeneic hematopoietic stem-cell transplantation (reduced-intensity conditioning, matched unrelated donor shown feasible in IKAROS disease) | NCIT:C15431 (Hematopoietic Stem Cell Transplantation) |
| Infection management | Targeted antimicrobials for bacterial/viral/fungal infections | — |
| Malignancy | Standard ALL chemotherapy if leukemia develops | — |

Supportive management (co-trimoxazole + immunoglobulin) is the established standard for combined immunodeficiency with PJP and humoral failure ([PMID: 22982295](https://pubmed.ncbi.nlm.nih.gov/22982295/)). HSCT is curative and well-tolerated in severe IKAROS-associated disease ([PMID: 38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/)). No approved gene therapy or targeted small-molecule therapy exists for this disease; pharmacogenomic considerations are not specifically defined.

### 13. Prevention

- **Primary prevention:** Not possible (de novo genetic lesion). Genetic counseling for recurrence risk (low, given de novo origin, but germline mosaicism cannot be excluded).
- **Secondary prevention:** Early genetic diagnosis → institution of PJP prophylaxis and Ig replacement; surveillance for leukemia.
- **Tertiary prevention:** Prevent infectious complications and plan HSCT before severe sequelae.
- **Counseling:** Genetic counseling; prenatal/preimplantation testing feasible if a familial variant is known.

### 14. Other Species / Natural Disease

- **Orthologs:** Mouse *Ikzf1* (NCBI Gene ID 22778). Highly conserved zinc-finger structure.
- **Natural disease in animals:** No well-characterized spontaneous companion-animal counterpart documented; disease knowledge is from engineered models.
- **Comparative biology:** Mechanisms are evolutionarily conserved — mouse Ikaros mutations reproduce lineage defects, supporting cross-species conservation of IKAROS-dependent hematopoiesis.

### 15. Model Organisms

- **Mouse knock-in of IKAROS ZF1 point mutation:** Reproduces B-cell deficiency, modeling the human DNA-binding-domain disease ([PMID: 33658297](https://pubmed.ncbi.nlm.nih.gov/33658297/)).
- **Paralog (AIOLOS p.N160S) murine knock-in:** Recapitulates the human immunophenotype with failed DNA binding, pericentromeric mistargeting, and dominant-negative effect — a direct analog of IKAROS N159S ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)).
- **Germline Ikzf1-null and hypomorphic mice:** Absence of T, B, NK, and dendritic cells (null) vs lymphoproliferation/lymphoma (reduced activity), illustrating dose-dependence ([PMID: 11997672](https://pubmed.ncbi.nlm.nih.gov/11997672/)).
- **Applications/limitations:** Models validate causality and mechanism but may not fully capture the human combined phenotype or PJP susceptibility; in vitro cotransfection/EMSA/immunofluorescence assays model the molecular lesion.

---

## Mechanistic Model / Interpretation

```
 De novo germline missense in IKZF1 DNA-binding ZF (e.g., N159S)
                         │
                         ▼
        Mutant IKAROS loses DNA binding ───────┐
                         │                       │ retains dimerization
                         ▼                       ▼
        Fails pericentromeric targeting   Heterodimerizes with WT IKAROS
                         │                       │
                         └───────────┬───────────┘
                                     ▼
            Sequestration of WT IKAROS off chromatin
            (DOMINANT-NEGATIVE interference; NuRD dysfunction)
                                     │
                                     ▼
          Global loss of IKAROS transcription-factor activity
                                     │
        ┌───────────────┬───────────┴───────────┬──────────────┐
        ▼               ▼                        ▼              ▼
   B lymphopenia   Naive-skewed T cells    Myeloid defects   Loss of tumor
   hypogamma-      (no effector/memory)    (neutropenia,     suppression
   globulinemia                            eosinopenia,          │
        │               │                   low mDC, mono-       ▼
        └───────┬───────┘                   cyte dysfnx)      ALL risk
                ▼                                 │          (T-ALL seen)
    Combined immunodeficiency ◄───────────────────┘
                │
                ▼
   Near-universal Pneumocystis jirovecii pneumonia
   + bacterial/viral infections
```

The unifying concept is **heterodimeric interference**: unlike simple haploinsufficiency (50% dose reduction → milder CVID-like disease), the dominant-negative mutant actively poisons the remaining wild-type allele's product, producing a deeper, multilineage functional loss and a qualitatively more severe (combined) immunodeficiency. The requirement for an intact dimerization domain is the mechanistic signature, directly demonstrated in the AIOLOS paralog where deleting dimerization rescued the phenotype.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/) | *Dominant-negative IKZF1 mutations cause a T, B, and myeloid combined immunodeficiency* | Defines the clinical entity: 7 patients, N159, universal PJP, multilineage defect, T-ALL |
| [32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/) | *IKAROS Family Zinc Finger 1-Associated Diseases* | Contrasts haploinsufficiency (CVID-like) vs dominant-negative (CID + PJP) |
| [33392855](https://pubmed.ncbi.nlm.nih.gov/33392855/) | *IKAROS-Associated Diseases in 2020* | Genotype–mechanism–phenotype framework; IKAROS as regulator/tumor suppressor |
| [10970879](https://pubmed.ncbi.nlm.nih.gov/10970879/) | *Targeting of Ikaros to pericentromeric heterochromatin* | DNA binding + dimerization both required for targeting — basis of DN effect |
| [21548011](https://pubmed.ncbi.nlm.nih.gov/21548011/) | *Congenital pancytopenia... Ikaros mutation* | DNA-binding-domain variant → decreased affinity, aberrant localization |
| [34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/) | *A variant in human AIOLOS impairs adaptive immunity by interfering with IKAROS* | Proves heterodimeric-interference mechanism (dimerization required) |
| [34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/) | *AIOLOS defect (p.N160S) in patients* | Paralog analog of N159S; murine recapitulation; DN effect |
| [33658297](https://pubmed.ncbi.nlm.nih.gov/33658297/) | *Point mutation in IKAROS ZF1 causes B cell deficiency in mice* | Mouse DNA-binding-domain knock-in validates causality |
| [11997672](https://pubmed.ncbi.nlm.nih.gov/11997672/) | *Aiolos and Ikaros: regulators of lymphocyte development* | Dose-dependent spectrum: immunodeficiency ↔ lymphoproliferation |
| [21765977](https://pubmed.ncbi.nlm.nih.gov/21765977/) | *Regulator of myeloid differentiation: the secret life of Ikaros* | IKAROS role in HSC renewal and myeloid lineage (explains myeloid defects) |
| [38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/) | *IKAROS GOF disease: allogeneic HCT experience* | HSCT curative and well-tolerated in IKAROS disease |
| [22982295](https://pubmed.ncbi.nlm.nih.gov/22982295/) | *VODI (Sp110)* | Illustrative standard supportive care: Ig + co-trimoxazole in CID with PJP |
| [38579942](https://pubmed.ncbi.nlm.nih.gov/38579942/) | *IgG4-RD and B-cell malignancy due to IKZF1 GOF* | Defines GOF class; situates DN CID in the spectrum |
| [41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/) | *Systematic functional validation of IKAROS variants* | 81 variants; impact maps to DNA-binding/dimerization domains |
| [33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/) | *CVID, AIHA, pancytopenia with IKAROS defect (R143W)* | Partial dominant-negative DNA-binding-domain variant |
| [38438084](https://pubmed.ncbi.nlm.nih.gov/38438084/) | *Loss-of-phosphorylation IKZF1 → GOF* | Fourth functional class (GOF-LOP) |

**Evidence source types:** Human clinical case series (29889099, 33122583, 34694366), disease-level reviews (32654692, 33392855), in vitro functional assays (10970879, 21548011, 41380100), and model-organism studies (33658297, 34155405, 11997672).

---

## Limitations and Knowledge Gaps

1. **Small patient numbers.** The defining cohort comprises only 7 unrelated patients; prevalence, incidence, sex ratio, penetrance estimates, and long-term natural history are therefore imprecise.
2. **No disease-specific HSCT outcome data.** The strongest transplant evidence comes from the related IKAROS *gain-of-function* disease (PMID 38320737) rather than directly from the dominant-negative CID cohort; curative benefit is inferred.
3. **Some mechanistic steps are inferential.** Pericentromeric mistargeting and heterodimeric sequestration for the specific N159 variants are strongly supported by analogous DNA-binding-domain variants and the AIOLOS paralog, but not every step has been demonstrated for N159 itself.
4. **No standardized ontology mappings.** The disease lacks dedicated ICD-11/Orphanet/MeSH codes; HPO frequency annotations are derived from a single small cohort.
5. **No QoL instrument data**, no pharmacogenomics, and no approved targeted/gene therapy.
6. **Modifier genetics undefined** — the influence of paralog (AIOLOS/HELIOS) dosage or other modifiers on severity is unexplored.
7. **A knowledge-state citation mismatch** was flagged for PMID 33658297 (title used as snippet); the supporting claim nonetheless reflects the paper's documented finding of a mouse ZF1 B-cell deficiency model.

---

## Proposed Follow-up Experiments / Actions

1. **International registry/cohort aggregation** (via inborn-errors-of-immunity consortia) to refine prevalence, penetrance, expressivity, natural history, and HSCT outcomes specifically for dominant-negative *IKZF1* CID.
2. **Direct functional validation of N159S/N159T** — EMSA/DNA-binding, immunofluorescence pericentromeric localization, and dominant-negative cotransfection assays, plus dimerization-deletion rescue (as done for AIOLOS) to formally close the mechanistic chain.
3. **Single-cell transcriptomics/epigenomics** of patient hematopoietic progenitors and immune subsets to map IKAROS-dependent regulatory failures across lineages and define the molecular basis of the naive-T-cell block and myeloid deficits.
4. **Dedicated N159 knock-in mouse model** to recapitulate the full combined phenotype (including PJP susceptibility) and test HSCT and candidate therapies.
5. **Prospective HSCT outcome study** in dominant-negative *IKZF1* CID, including conditioning optimization and leukemia-risk reduction.
6. **Ontology/knowledge-base curation** — assign MONDO/HPO/UBERON/CL/NCIT annotations as above and advocate for a dedicated Orphanet/ICD-11 entry.
7. **Functional classification pipeline** to triage *IKZF1* VUS into haploinsufficiency vs dominant-negative vs GOF classes (building on PMID 41380100), enabling genotype-guided management.

---

*Report compiled from 5 investigation iterations, 7 confirmed findings, and 28 reviewed papers. Evidence integrity: claims attributed only to papers with verified abstract snippets or provided citation context.*


## Artifacts

- [OpenScientist final report](Combined_Immunodeficiency_Due_To_Dominant_Negative_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Immunodeficiency_Due_To_Dominant_Negative_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002718` (1 mention) - the report calls it "Common"; HP calls it **Recurrent bacterial infections**
- `HP:0004429` (1 mention) - the report calls it "Common"; HP calls it **Recurrent viral infections**
- `HP:0004313` (1 mention) - the report calls it "High"; HP calls it **Decreased circulating immunoglobulin concentration**
- `HP:0001875` (1 mention) - the report calls it "Present"; HP calls it **Decreased total neutrophil count**
- `HP:0001877` (1 mention) - the report calls it "Present"; HP calls it **Abnormal erythrocyte morphology**
- `HP:0012335` (1 mention) - the report calls it "Present"; HP calls it **obsolete Abnormality of folate metabolism**
- `HP:0006721` (1 mention) - the report calls it "~1/7 (T-ALL in index cohort)"; HP calls it **Acute lymphoblastic leukemia**
- `UBERON:0002371` (1 mention) - the report calls it "bone marrow", "Organ/system level:** Immune/hematopoietic system — **bone marrow"; UBERON calls it **bone marrow**
- `NCIT:C309` (1 mention) - the report calls it "Sulfamethoxazole/Trimethoprim"; NCIT calls it **Biotin**
- `NCIT:C564` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **Ifosfamide**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0012335` (obsolete Abnormality of folate metabolism) (1 mention) - replaced by `HP:0040087`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010976` (1 mention) - the report calls it "B lymphocytopenia"; HP calls it **Decreased total B cell count**, and lists "B lymphocytopenia" among its other names
- `HP:0012177` (1 mention) - the report calls it "abnormal dendritic cell"; HP calls it **Abnormal natural killer cell physiology**, and lists "Abnormal NK cell physiology" among its other names
- `GO:0006357` (1 mention) - the report calls it "regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**
- `GO:0005634` (2 mentions) - the report calls it "nucleus", "Subcellular level:** Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "nucleus", "Subcellular level:** Nucleus"
- `UBERON:0002371` - called "bone marrow", "Organ/system level:** Immune/hematopoietic system — **bone marrow"