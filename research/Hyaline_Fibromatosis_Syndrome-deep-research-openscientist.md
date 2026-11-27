---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T08:50:22.108814'
end_time: '2026-11-13T09:05:37.751481'
duration_seconds: 915.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hyaline Fibromatosis Syndrome
  mondo_id: MONDO:0009229
  category: Mendelian
  causal_genes: ANTXR2
  omim_id: OMIM:228600
  synonyms: not recorded
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 2f14b36a-c1a8-499a-8b5f-ad9e93bb9852
citation_count: 19
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 25
  quotes_valid: 25
  relevance_assessed: 23
  on_topic: 21
  validator_version: 0.5.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 9
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0009229
    reported_labels:
    - MONDO
    ontology_label: hyaline fibromatosis syndrome
  - term_id: HP:0000704
    reported_labels:
    - gingival overgrowth
    ontology_label: Periodontitis
  - term_id: HP:0000979
    reported_labels:
    - "purpura/skin papules \u2014 approximate"
    ontology_label: Purpura
  - term_id: HP:0100242
    reported_labels:
    - subcutaneous nodules
    ontology_label: Sarcoma
  - term_id: CL:0002254
    reported_labels:
    - intestinal stem cell
    ontology_label: epithelial cell of small intestine
  labels_variant: 7
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
  path: Hyaline_Fibromatosis_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hyaline_Fibromatosis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hyaline Fibromatosis Syndrome
- **MONDO ID:** MONDO:0009229 (if available)
- **Causal gene(s):** ANTXR2
- **OMIM:** OMIM:228600
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hyaline Fibromatosis Syndrome** covering all of the
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

# Hyaline Fibromatosis Syndrome (ANTXR2): Comprehensive Disease Characterization

**Disease:** Hyaline Fibromatosis Syndrome (HFS)
**MONDO:** MONDO:0009229 | **OMIM:** 228600 | **Orphanet:** ORPHA:2176
**Causal gene:** **ANTXR2** (a.k.a. **CMG2**, capillary morphogenesis gene/protein 2), HGNC:21732, chromosome 4q21.21, UniProt P58335
**Category:** Mendelian, autosomal recessive

---

## Summary

**Hyaline Fibromatosis Syndrome (HFS) is an ultra-rare autosomal recessive connective-tissue disorder caused by biallelic loss-of-function mutations in the gene ANTXR2 (also called CMG2, capillary morphogenesis gene 2).** The disease is defined by progressive deposition of amorphous, PAS-positive, diastase-resistant "hyaline" extracellular matrix (ECM) in skin, gingiva, joints, bone, and—in its severe form—internal viscera. HFS is a unifying term that merges two conditions historically described separately: the milder **Juvenile Hyaline Fibromatosis (JHF)** and the severe, frequently lethal **Infantile Systemic Hyalinosis (ISH)**. These were proven allelic in 2003 when mutations in CMG2/ANTXR2 were identified across families with both presentations.

Mechanistically, ANTXR2 is a type I transmembrane protein that functions as a **collagen VI turnover receptor**. In the healthy state it binds collagen VI (and laminin / collagen IV via its von Willebrand factor A domain) and internalizes it for intracellular degradation through a ligand-triggered "talin-to-RhoA switch." When ANTXR2 is lost, this receptor-mediated endocytic clearance fails, collagen VI accumulates in the extracellular matrix, and the hallmark hyaline material builds up. This model is now firmly supported in patient tissue and in `Antxr2`-null mice, in which the phenotype is rescued by concurrent deletion of `Col6a1`, proving it is collagen-VI-dependent.

Clinically, HFS presents from birth or early infancy with painful joint contractures, generalized skin stiffening with pearly papules and subcutaneous nodules, gingival hypertrophy, osteolytic bone lesions, and—in severe ISH—protein-losing enteropathy, recurrent infections, failure to thrive, and death before age two. Genotype predicts severity: truncating mutations and missense variants in the ectodomain-encoding exons produce severe disease, whereas C-terminal missense variants produce the milder form. No curative therapy exists; management is symptomatic and multidisciplinary, and prevention is limited to genetic counseling and DNA-based prenatal/pre-implantation testing in at-risk (often consanguineous) families.

---

## Key Findings

### Finding 1 — HFS is an autosomal recessive connective-tissue disorder caused by biallelic loss-of-function ANTXR2 (CMG2) mutations

HFS unifies two previously separate clinical entities—JHF (milder) and ISH (severe)—shown to be allelic. The landmark study by Hanks et al. (2003) identified **15 different mutations in the gene encoding capillary morphogenesis protein 2 (CMG2/ANTXR2)** on chromosome 4q21 across 17 families with either JHF or ISH. ANTXR2 encodes a transmembrane von Willebrand factor A (vWA)-domain protein that binds laminin and collagen IV/VI and also serves as the cellular receptor for anthrax toxin.

> "We now report the identification of 15 different mutations in the gene encoding capillary morphogenesis protein 2 (CMG2) in 17 families with JHF or ISH. CMG2 is a transmembrane protein that is induced during capillary morphogenesis and that binds laminin and collagen IV via a von Willebrand factor type A (vWA) domain." — [PMID: 14508707](https://pubmed.ncbi.nlm.nih.gov/14508707/)

> "Hyaline fibromatosis syndrome (HFS) is the unifying term for infantile systemic hyalinosis and juvenile hyaline fibromatosis. HFS is a rare autosomal recessive disorder of the connective tissue caused by mutations in the gene for anthrax toxin receptor-2 (ANTXR2)." — [PMID: 30176098](https://pubmed.ncbi.nlm.nih.gov/30176098/)

### Finding 2 — ANTXR2/CMG2 is a collagen VI turnover receptor; its loss causes ECM accumulation via a blocked talin-to-RhoA endocytic switch

CMG2 binds collagen VI (and laminin/collagen IV via its vWA domain) and mediates its endocytic internalization and degradation. Bürgi et al. (2020) showed that CMG2 binds talin—and thereby the actin cytoskeleton—**only in its ligand-free state**; extracellular ligand binding triggers src-dependent talin release and recruitment of RhoA, and this talin-to-RhoA switch is required for intracellular degradation of collagen VI in human fibroblasts.

> "CMG2 binds talin, and thereby the actin cytoskeleton, only in its ligand-free state. Extracellular ligand binding leads to src-dependent talin release and recruitment of the actin cytoskeleton regulator RhoA and its effectors." — [PMID: 32428455](https://pubmed.ncbi.nlm.nih.gov/32428455/)

The in vivo proof came from Metti et al. (2026), who showed ANTXR2 is expressed predominantly by **fibro-adipogenic progenitors (FAPs)**, and that `Antxr2`-null mice exhibit premature collagen VI accumulation, tissue stiffening, and maladaptive muscle hypertrophy. Crucially, `Antxr2⁻/⁻::Col6a1⁻/⁻` double-knockout mice rescue the phenotype, demonstrating it is collagen-VI-dependent.

> "ANTXR2-null (Antxr2-/-) mice exhibit premature COL6 accumulation within intramuscular connective tissue, leading to tissue stiffening and progressive, maladaptive muscle hypertrophy with impaired locomotion and myopathic features. Using Antxr2-/-::Col6a1-/- double-knockout mice, we demonstrate that these phenotypes are COL6-dependent." — [PMID: 42878719](https://pubmed.ncbi.nlm.nih.gov/42878719/)

At the protein level, HFS-causing missense mutations in the vWA / Ig-like ectodomain cause protein misfolding and ER retention (ERAD). Deuquet et al. (2011) demonstrated that such mutations lead to retention of the mutated protein in the endoplasmic reticulum, and that proteasome inhibitors can partially rescue surface expression.

> "missense mutations that map to the extracellular von Willebrand domain or the here characterized Ig-like domain of CMG2 lead to folding defects and thereby to retention of the mutated protein in the endoplasmic reticulum (ER)." — [PMID: 21328543](https://pubmed.ncbi.nlm.nih.gov/21328543/)

### Finding 3 — Genotype–phenotype correlation: ectodomain/truncating mutations → severe ISH; C-terminal missense → milder JHF

In a review of 84 published cases, Casas-Alba et al. (2018) reinforced that **missense mutations in exons 1–12 and mutations leading to a premature stop codon produce the severe (grade 4, life-limiting) form**, while missense pathogenic variants in exons 13–17 produce the mild form. Grade 4 patients present in the newborn period with extreme pain on minimal handling; causes of death are intractable diarrhea, recurrent infections, and organ failure, with a median age of death of 15.0 months (IQR 9.5–24.0).

> "This review provides evidence to reinforce the previous hypothesis that missense mutations in exons 1-12 and mutations leading to a premature stop codon lead to the severe form of the disease, while missense pathogenic variants in exons 13-17 lead to the mild form of the disease." — [PMID: 30176098](https://pubmed.ncbi.nlm.nih.gov/30176098/)

> "Causes of death are intractable diarrhea, recurrent infections, and organ failure. Median age of death of grade 4 cases is 15.0 months (p25-p75: 9.5-24.0)." — [PMID: 30176098](https://pubmed.ncbi.nlm.nih.gov/30176098/)

Reported pathogenic variants include missense (e.g., c.945T>G p.Cys315Trp; c.652T>C p.Cys218Arg; c.1223T>C p.Leu408Pro), frameshift/truncating (c.1073dup p.Ala359Cysfs*13; c.1074del/c.1074delT), and splice-site (c.697+1G>A) changes, affecting the vWA and Ig-like ectodomain and the cytoplasmic domain. A novel c.1223T>C (p.Leu408Pro) variant appeared to permit a protracted course (PMID 32196989).

### Finding 4 — Core clinical phenotype

Hallmarks across case series are: joint contractures/stiffness (near-universal), generalized skin stiffness/thickening with pearly papules and subcutaneous nodules, hyperpigmented papules over extensor/bony surfaces, fleshy perianal masses, gingival hypertrophy, and severe/persistent diarrhea. Histopathology shows bland fibroblasts embedded in abundant amorphous eosinophilic hyaline matrix that is strongly PAS-positive and diastase-resistant.

> "The hallmarks of the disease are joint contractures, generalized skin stiffness, hyperpigmented papules over extensor surfaces of joints, fleshy perianal masses, severe diarrhea, and gingival hypertrophy." — [PMID: 38814306](https://pubmed.ncbi.nlm.nih.gov/38814306/)

Severe ISH adds hyaline deposits in viscera, **protein-losing enteropathy** driven by enhanced duodenal collagen deposition, recurrent infections, failure to thrive, osteopenia/osteolytic lesions, bone fractures, and hypotonia.

> *"Enhanced Collagen Deposition in the Duodenum of Patients with Hyaline Fibromatosis Syndrome and Protein Losing Enteropathy."* — [PMID: 33147779](https://pubmed.ncbi.nlm.nih.gov/33147779/)

Rare presentations include hypercalcemia (from osteoclast stimulation and immobilization; PMID 37264371) and, uncommonly, isolated gingival enlargement as the only manifestation (PMID 34627224).

**Suggested HPO terms:** HP:0003549 (abnormal connective tissue), HP:0001371 (flexion contracture), HP:0000704 (gingival overgrowth), HP:0000979 (purpura/skin papules — approximate), HP:0002664→HP:0100242 (subcutaneous nodules), HP:0002754 (osteolysis), HP:0002028 (chronic diarrhea), HP:0001824 (weight loss/failure to thrive), HP:0002902 (hyponatremia—secondary), HP:0003072 (hypercalcemia).

### Finding 5 — Epidemiology: ultra-rare, consanguinity-associated, recurrent/founder-type mutations

HFS is ultra-rare. Orphanet lists it as ORPHA:2176 with prevalence **<1/1,000,000** and fewer than ~100–150 reported cases worldwide (Casas-Alba 2018 reviewed 84 cases; Futagawa 2024 noted ~100 cases reported). It is strongly associated with consanguineous backgrounds, and over 40 ANTXR2 mutations are known.

> "Over 40 mutations in the ANTXR2 gene have been associated with cases of HFS." — [PMID: 29801470](https://pubmed.ncbi.nlm.nih.gov/29801470/)

The recurrent c.1073dup (p.Ala359Cysfs*13) mutation appears to arise sporadically/recurrently in different populations rather than from a single ancient founder:

> "Haplotype analysis was performed to determine the origin of this mutation in this consanguineous cohort, which suggested that it may develop sporadically in different populations." — [PMID: 29801470](https://pubmed.ncbi.nlm.nih.gov/29801470/)

> "Thus far, about 100 cases have been reported but few of these were reported from Japan." — [PMID: 39258861](https://pubmed.ncbi.nlm.nih.gov/39258861/)

Inheritance is autosomal recessive (homozygous or compound heterozygous). No sex predilection is established, and intellectual ability is generally normal.

### Finding 6 — Diagnosis: characteristic biopsy + ANTXR2 molecular confirmation; imaging shows osteolytic/intra-articular lesions

Diagnosis is clinical + histopathological + molecular. Skin/nodule biopsy shows bland spindle/epithelioid fibroblasts embedded in abundant amorphous eosinophilic hyaline ground substance that is PAS-positive and diastase-resistant. Confirmation is by ANTXR2 sequencing — single-gene testing, trio whole-exome sequencing, or rapid whole-genome sequencing.

> "rapid whole-genome sequencing (rWGS) was done with Fabric GEM®-assisted artificial intelligence." — [PMID: 38989346](https://pubmed.ncbi.nlm.nih.gov/38989346/)

Radiographic/MRI findings include osteolytic/low-density bone lesions, osteopenia, and multifocal intra-articular hyaline deposition.

> "We describe a case of a 25-year-old patient presenting with bilateral knee pain, limited range of motion in her extremities, and lower extremity weakness with detailed MR imaging demonstrating the first case of multifocal intra-articular deposition of hyaline material within several joints." — [PMID: 33120290](https://pubmed.ncbi.nlm.nih.gov/33120290/)

Differential diagnosis includes juvenile rheumatoid arthritis, Winchester syndrome, lipoid proteinosis, Farber disease, neurofibromatosis, and gingival fibromatosis.

### Finding 7 — No curative therapy; management is symptomatic and multidisciplinary

No specific or curative treatment exists. Management is supportive and multidisciplinary: surgical excision of debilitating/giant nodules (often with recurrence), intralesional/oral corticosteroids (temporary nodule reduction), analgesia for chronic pain, nutritional support for failure to thrive/protein-losing enteropathy, physiotherapy for contractures, and periodontal/dental surgery for gingival hypertrophy (improves mastication, weight gain, and quality of life).

> "No specific treatment is yet available. Most patients with the severe form of the condition pass away before the second year of age." — [PMID: 38814306](https://pubmed.ncbi.nlm.nih.gov/38814306/)

> "Early surgical treatment provided instantaneous and more sustainable results, while corticosteroids can be used as alternative modalities with temporary outcomes." — [PMID: 33173631](https://pubmed.ncbi.nlm.nih.gov/33173631/)

Mechanistically-motivated experimental strategies include proteasome inhibitors to rescue ER-retained misfolded CMG2 mutants in vitro (PMID 21328543) and S-acylation / APT2-pathway modulation (PMID 42409807) — none yet in clinical use.

**Suggested NCIT terms:** Corticosteroid Therapy, Surgical Excision, Physical Therapy, Nutritional Support, Analgesic Therapy.

### Finding 8 — Antxr2/Cmg2 knockout mice model multiple HFS mechanisms

The `Antxr2⁻/⁻` mouse (*Mus musculus*, NCBI Taxon 10090; ortholog Antxr2, NCBI Gene 71914) is the principal model and recapitulates several facets of HFS:

1. **ECM/collagen VI accumulation → muscle hypertrophy**, rescued by `Col6a1` double-KO (PMID 42878719).
2. **Impaired intestinal stem-cell renewal after colitis** via a defective fetal-to-Lgr5⁺ transition and β-catenin nuclear translocation — identifying CMG2 as a context-specific Wnt modulator and offering a mechanism for lethal diarrhea in HFS.

> "CMG2 knockout impairs the transition from fetal-like to Lgr5+ adult stem cells, which is associated with a defect in ß-catenin nuclear translocation. Based on our findings, we propose that CMG2 functions as a context-specific modulator of Wnt signaling, essential for replenishing the pool of intestinal stem cells following injury." — [PMID: 40847216](https://pubmed.ncbi.nlm.nih.gov/40847216/)

3. **Cervical ECM/collagen accumulation → parturition (dystocia) defect** with altered pyridinoline crosslink density.

> "Antxr2-/- females are known to have a parturition defect, in part, due to an excessive accumulation of extracellular matrix proteins in the cervix, particularly collagen." — [PMID: 24390076](https://pubmed.ncbi.nlm.nih.gov/24390076/)

4. **Angiogenesis/chemotaxis role**: CMG2 is required for growth-factor-induced endothelial chemotaxis in a Rho-dependent manner.

> "CMG2 mediates the antiangiogenic effects of PA and is required for growth-factor-induced chemotaxis." — [PMID: 35212873](https://pubmed.ncbi.nlm.nih.gov/35212873/)

5. **Anthrax resistance**: `Antxr2`-knockout mice are resistant to anthrax toxin / *Bacillus anthracis* (reflecting CMG2's dual role as the major anthrax toxin receptor). Zebrafish models additionally show CMG2 controls oriented cell division.

### Finding 9 — Identifiers, nomenclature, and gene/protein annotations

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009229 |
| OMIM | 228600 (Hyaline Fibromatosis Syndrome; formerly Systemic Hyalinosis) |
| Orphanet | ORPHA:2176 |
| MeSH | "Hyalinosis, Systemic" |
| ICD-10 (proxy) | L98.5 (mucinosis/hyalinosis of skin) or M72.x (fibromatoses) |
| Gene | **ANTXR2** (HGNC:21732; NCBI Gene 118429; Ensembl ENSG00000163297), chr 4q21.21; aliases CMG2 |
| Protein | UniProt **P58335** (ANTR2_HUMAN) |

Historical synonyms: Juvenile Hyaline Fibromatosis (JHF), Infantile Systemic Hyalinosis (ISH; formerly OMIM 236490), Murray-Puretic-Drescher syndrome, fibromatosis hyalinica multiplex juvenilis, systemic hyalinosis, molluscum fibrosum. The ANTXR2 protein is a type I single-pass transmembrane protein with an extracellular vWA/I-domain (containing a MIDAS metal-ion-dependent adhesion site), an Ig-like domain, a transmembrane helix, and a cytoplasmic tail.

> "Hyaline fibromatosis syndrome (HFS; MIM 228600) is a rare autosomal recessive disorder." — [PMID: 30152846](https://pubmed.ncbi.nlm.nih.gov/30152846/)

> "we previously mapped the gene for JHF to chromosome 4q21." — [PMID: 14508707](https://pubmed.ncbi.nlm.nih.gov/14508707/)

Information is derived from aggregated disease-level resources (OMIM, Orphanet) combined with individual case reports/series (EHR-type data).

### Finding 10 — Temporal course and prevention

**Onset** ranges from congenital to early infancy. Severe ISH usually presents at or shortly after birth (extreme pain on handling, stiffness) and is progressive, with death typically within the first 1–2 years. Milder JHF presents in infancy/early childhood with subcutaneous nodules that increase in number and size with age and can continue into adulthood (reported age range 5–44 years).

> "The condition usually presents at birth, resulting in death in infancy." — [PMID: 22300424](https://pubmed.ncbi.nlm.nih.gov/22300424/)

> "With increasing age, the number and size of the nodules gradually increased in the patient." — [PMID: 30152846](https://pubmed.ncbi.nlm.nih.gov/30152846/)

The course is chronic, progressive, and non-remitting; no spontaneous remission occurs, and nodules recur after excision. No true primary prevention exists for a monogenic recessive disorder. Reproductive prevention is feasible: identification of the familial ANTXR2 mutation enables carrier testing, cascade screening, presymptomatic diagnosis, DNA-based prenatal diagnosis, and preimplantation genetic testing, with genetic counseling for consanguineous couples (25% recurrence risk per pregnancy).

> "identification of pathogenetic mutations in the ANTXR2 gene makes DNA-based prenatal diagnosis feasible for subsequent pregnancies." — [PMID: 22300424](https://pubmed.ncbi.nlm.nih.gov/22300424/)

### Finding 11 — Collagen VI is the physiological ligand that accumulates in HFS tissue

Bürgi et al. (2017) demonstrated that CMG2/ANTXR2 is a central regulator of collagen VI homeostasis: CMG2 loss of function promotes collagen VI accumulation in patients, driving nodule formation, with massive collagen VI accumulation in `Antxr2`-null mouse uteri. Abrami et al. (2026) states plainly that CMG2/ANTXR2 functions as a collagen VI receptor required for ECM homeostasis.

> "CMG2 loss of function promotes accumulation of collagen VI in patients, leading in particular to nodule formation." — [PMID: 28604699](https://pubmed.ncbi.nlm.nih.gov/28604699/)

> "CMG2/ANTXR2 functions as a Collagen VI receptor required for extracellular matrix homeostasis." — [PMID: 42409807](https://pubmed.ncbi.nlm.nih.gov/42409807/)

This identifies the specific "hyaline" ECM material as collagen VI, bridging the original observation that CMG2 binds laminin/collagen IV (Hanks 2003) with the modern collagen-VI turnover model.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function mutation in *ANTXR2* (CMG2)** — missense (ectodomain), frameshift, nonsense, or splice-site — *leads to* loss of functional cell-surface receptor.
   - *Branch (ectodomain missense):* vWA/Ig-domain misfolding *results in* ER retention and ERAD-mediated degradation, so little/no mature protein reaches the surface (demonstrated in vitro; PMID 21328543).
   - *Branch (truncating/splice):* loss of protein entirely → severe ISH.
2. **Loss of surface ANTXR2 on fibro-adipogenic progenitors and fibroblasts** *results in* failure of the ligand-triggered talin-to-RhoA switch that drives receptor-mediated endocytosis (demonstrated in human fibroblasts; PMID 32428455).
3. **Failed endocytic internalization/degradation of collagen VI** *leads to* progressive extracellular accumulation of collagen VI and associated matrix (demonstrated in patient tissue and mouse; PMIDs 28604699, 42878719).
4. **Accumulated collagen VI / "hyaline" ECM** (PAS-positive, diastase-resistant) *results in* tissue stiffening and deposition in skin, gingiva, perichondrium/joints, bone, and viscera.
5. **Tissue-level deposition** *leads to* the clinical hallmarks:
   - Skin/subcutis → papulonodules, pearly papules, perianal masses.
   - Joints/periarticular → painful contractures, stiffness, limited range of motion.
   - Bone → osteolytic lesions, osteopenia, fractures.
   - Gingiva → hypertrophy.
   - *Branch (severe ISH):* duodenal/intestinal collagen deposition *leads to* protein-losing enteropathy; impaired intestinal stem-cell renewal (Wnt/β-catenin defect, *inferred* from mouse colitis model; PMID 40847216) *contributes to* intractable diarrhea → failure to thrive, infection susceptibility, and early death.

### Schematic

```
ANTXR2 (CMG2) biallelic LoF mutation
        │
        ├── ectodomain missense ─► misfolding ─► ER retention / ERAD ─► no surface receptor
        └── truncating / splice ─────────────────────────────────────► no receptor
        │
        ▼
Loss of surface CMG2 on FAPs / fibroblasts
        │  (normally: ligand binding → talin release → RhoA → endocytosis)
        ▼
Failed collagen VI endocytosis & degradation
        │
        ▼
Extracellular collagen VI ("hyaline") ACCUMULATION  ◄── rescued by Col6a1 KO in mice
        │
   ┌────┼───────┬───────────┬──────────────┬───────────────┐
 Skin  Joints  Bone      Gingiva        Viscera (ISH)
papulo- contrac- osteolysis hypertrophy  PLE + diarrhea
nodules  tures   fractures               infection, FTT, death
```

### Upstream vs downstream; cell types and processes

- **Upstream (initiating):** ANTXR2 loss of function; ER quality-control failure of misfolded mutants.
- **Central node:** defective collagen VI receptor-mediated endocytosis (talin→RhoA switch).
- **Downstream (effector):** extracellular collagen VI accumulation and consequent tissue fibrosis/stiffening.
- **Key cell types:** fibro-adipogenic progenitors (FAPs), dermal and gingival fibroblasts, intestinal stem cells (Lgr5⁺), endothelial cells (angiogenesis role).
- **Suggested GO terms:** GO:0030198 extracellular matrix organization; GO:0006898 receptor-mediated endocytosis; GO:0030574 collagen catabolic process; GO:0016055 Wnt signaling pathway; GO:0001525 angiogenesis; GO:0030968 ER unfolded protein response.
- **Suggested CL terms:** CL:0000057 (fibroblast), CL:0000134 (mesenchymal stem cell), CL:0000115 (endothelial cell), CL:0002254 (intestinal stem cell).
- **Suggested UBERON terms:** UBERON:0002097 (skin), UBERON:0001828 (gingiva), UBERON:0000982 (joint), UBERON:0002481 (bone tissue), UBERON:0002114 (duodenum), UBERON:0000002 (uterine cervix — model).
- **Relevant molecule (CHEBI/complex):** collagen type VI (ECM protein complex); PAS-reactive hyaline glycoprotein material.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [14508707](https://pubmed.ncbi.nlm.nih.gov/14508707/) | CMG2 mutations cause JHF and ISH | Establishes ANTXR2/CMG2 as the causal gene; JHF+ISH allelic; 4q21 locus |
| [30176098](https://pubmed.ncbi.nlm.nih.gov/30176098/) | HFS clinical update & genotype-phenotype | Unifying HFS term; exon-based genotype–phenotype rule; mortality data |
| [32428455](https://pubmed.ncbi.nlm.nih.gov/32428455/) | Collagen VI receptor talin-to-RhoA switch | Defines endocytic molecular switch controlling collagen VI degradation |
| [42878719](https://pubmed.ncbi.nlm.nih.gov/42878719/) | FAPs / ANTXR2 fine-tune collagen VI | In vivo COL6-dependence; `Col6a1` double-KO rescue |
| [21328543](https://pubmed.ncbi.nlm.nih.gov/21328543/) | Ectodomain mutations rescued by proteasome inhibitors | ER retention of misfolded mutants; therapeutic concept |
| [28604699](https://pubmed.ncbi.nlm.nih.gov/28604699/) | CMG2/ANTXR2 regulates extracellular collagen VI | Collagen VI accumulation in patients |
| [42409807](https://pubmed.ncbi.nlm.nih.gov/42409807/) | Dynamic S-acylation controls CMG2 | Confirms CMG2 as collagen VI receptor; S-acylation pathway |
| [38814306](https://pubmed.ncbi.nlm.nih.gov/38814306/) | HFS: a recognizable syndrome | Core hallmarks; no specific treatment; prognosis |
| [33147779](https://pubmed.ncbi.nlm.nih.gov/33147779/) | Duodenal collagen & protein-losing enteropathy | Mechanism of PLE in severe HFS |
| [29801470](https://pubmed.ncbi.nlm.nih.gov/29801470/) | Genetic basis in consanguineous cohort | >40 mutations; recurrent-mutation origin |
| [39258861](https://pubmed.ncbi.nlm.nih.gov/39258861/) | Prognostic factors for wellbeing | ~100 cases reported globally |
| [33120290](https://pubmed.ncbi.nlm.nih.gov/33120290/) | Multifocal intra-articular involvement | MRI hyaline deposition imaging |
| [38989346](https://pubmed.ncbi.nlm.nih.gov/38989346/) | AI-assisted rapid WGS diagnosis | rWGS diagnostic approach |
| [33173631](https://pubmed.ncbi.nlm.nih.gov/33173631/) | JHF treated with excision + corticosteroid | Symptomatic treatment outcomes |
| [40847216](https://pubmed.ncbi.nlm.nih.gov/40847216/) | Injury-induced intestinal stem-cell renewal needs CMG2 | Wnt/β-catenin mechanism for lethal diarrhea |
| [24390076](https://pubmed.ncbi.nlm.nih.gov/24390076/) | Cervical collagen remodeling / parturition defect | Mouse ECM accumulation phenotype |
| [35212873](https://pubmed.ncbi.nlm.nih.gov/35212873/) | CMG2 and growth-factor-induced angiogenesis | Angiogenesis/chemotaxis role |
| [22300424](https://pubmed.ncbi.nlm.nih.gov/22300424/) | ISH with splice-site ANTXR2 mutation | Congenital onset; prenatal diagnosis feasibility |
| [30152846](https://pubmed.ncbi.nlm.nih.gov/30152846/) | Two novel ANTXR2 mutations (Chinese) | MIM 228600; progressive nodule course |
| [37264371](https://pubmed.ncbi.nlm.nih.gov/37264371/) | Hypercalcemia presentation | Rare metabolic complication |
| [34627224](https://pubmed.ncbi.nlm.nih.gov/34627224/) | Gingival enlargement as sole manifestation | Phenotypic variability; diagnostic pitfall |
| [25781883](https://pubmed.ncbi.nlm.nih.gov/25781883/) | N-glycosylation of CMG2/TEM8 | Glycosylation buffers against pathogenic mutations |

The evidence base spans **human clinical case series and reviews** (diagnosis, phenotype, genotype–phenotype, epidemiology, treatment), **in vitro mechanistic studies** in patient/human fibroblasts (endocytic switch, ER retention), and **model-organism studies** (Antxr2 knockout mouse; zebrafish), providing convergent support for the collagen-VI-turnover model. The most decisive single piece of evidence is the `Antxr2⁻/⁻::Col6a1⁻/⁻` genetic rescue (PMID 42878719), which moves collagen VI from a correlative accumulant to a causal effector.

---

## Limitations and Knowledge Gaps

1. **Rarity limits quantitative epidemiology.** With <1/1,000,000 prevalence and ~100 reported cases, there are no robust incidence, survival-curve, or population-stratified data; most figures derive from case reviews (e.g., the 84-case review) rather than registries.
2. **Phenotype frequencies are semi-quantitative.** Precise penetrance of individual HPO features (e.g., exact % with osteolytic lesions vs. contractures) is not established from systematic cohorts.
3. **Mechanistic gaps downstream of collagen VI.** How collagen VI accumulation specifically produces bone osteolysis, hypercalcemia, and the striking pain phenotype is not fully resolved. The Wnt/stem-cell mechanism for diarrhea is demonstrated in a mouse colitis model and remains *inferred* for human PLE.
4. **Therapeutics are preclinical.** Proteasome-inhibitor rescue of ER-retained mutants and APT2/S-acylation modulation are in vitro only; no genotype-tailored (e.g., mutation-class-specific) therapy has reached trials.
5. **No approved biomarker** tracks disease activity; diagnosis still relies on biopsy + sequencing rather than a circulating marker.
6. **Modifier genes and expressivity** within the same genotype are not characterized; why some ectodomain variants permit protracted courses (e.g., p.Leu408Pro) is incompletely understood. N-glycosylation state may buffer tolerance to mutations (PMID 25781883).

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry.** Establish an international HFS registry capturing standardized HPO annotations, genotype, and longitudinal outcomes to produce real penetrance, progression-rate, and survival statistics.
2. **Mutation-class-specific therapeutic testing.** For ectodomain misfolding mutants, test proteasome inhibitors / chemical chaperones / ERAD modulators in patient-derived iPSC fibroblasts and FAP organoids to see whether surface CMG2 and collagen VI clearance are restored; progress toward mutation-stratified trials.
3. **Collagen-VI-lowering strategies.** Given the `Col6a1` genetic rescue, evaluate COL6-targeting approaches (antisense oligonucleotides / siRNA against COL6A1-3) in `Antxr2⁻/⁻` mice as a potential disease-modifying therapy.
4. **Biomarker development.** Measure circulating collagen VI fragments (e.g., C6M/PRO-C6 neoepitopes) in HFS patients vs. controls as candidate diagnostic/monitoring biomarkers.
5. **Dissect the diarrhea/PLE mechanism in humans.** Combine duodenal biopsy transcriptomics/single-cell analysis with Wnt/β-catenin readouts to test whether the mouse intestinal stem-cell-renewal defect operates in human ISH.
6. **Pain and bone mechanisms.** Investigate how periarticular/osseous collagen VI deposition drives nociception and osteolysis (osteoclast assays, immobilization-hypercalcemia models) to identify adjunctive symptomatic targets.
7. **Genotype–modifier studies.** Sequence modifier loci and N-glycosylation determinants across patients with discordant severity for the same primary variant.

---

## Conclusion

Hyaline Fibromatosis Syndrome is a Mendelian, autosomal recessive ECM disorder in which **loss of the collagen VI receptor ANTXR2/CMG2** abolishes receptor-mediated collagen VI endocytosis and degradation, causing progressive hyaline (collagen VI) accumulation across connective tissues. The molecular chain—from biallelic loss-of-function mutation, through failed talin-to-RhoA endocytic switching, to collagen-VI-dependent tissue stiffening—is now supported by patient tissue, human fibroblast biology, and a decisive `Col6a1` double-knockout mouse rescue. Clinical severity tracks mutation type/position, diagnosis combines characteristic PAS-positive hyaline histology with ANTXR2 sequencing, and—absent any curative therapy—care remains symptomatic and multidisciplinary, with prevention resting on genetic counseling and prenatal/pre-implantation testing in at-risk, frequently consanguineous families.


## Artifacts

- [OpenScientist final report](Hyaline_Fibromatosis_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hyaline_Fibromatosis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 25 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 21 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009229` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hyaline fibromatosis syndrome**
- `HP:0000704` (1 mention) - the report calls it "gingival overgrowth"; HP calls it **Periodontitis**
- `HP:0000979` (1 mention) - the report calls it "purpura/skin papules — approximate"; HP calls it **Purpura**
- `HP:0100242` (1 mention) - the report calls it "subcutaneous nodules"; HP calls it **Sarcoma**
- `CL:0002254` (1 mention) - the report calls it "intestinal stem cell"; CL calls it **epithelial cell of small intestine**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003549` (1 mention) - the report calls it "abnormal connective tissue"; HP calls it **Abnormality of connective tissue**
- `HP:0002754` (1 mention) - the report calls it "osteolysis"; HP calls it **Osteomyelitis**
- `HP:0001824` (1 mention) - the report calls it "weight loss/failure to thrive"; HP calls it **Weight loss**
- `HP:0002902` (1 mention) - the report calls it "hyponatremia—secondary"; HP calls it **Hyponatremia**
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0000982` (1 mention) - the report calls it "joint"; UBERON calls it **skeletal joint**, and lists "joints" among its other names
- `UBERON:0000002` (1 mention) - the report calls it "uterine cervix — model"; UBERON calls it **uterine cervix**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.