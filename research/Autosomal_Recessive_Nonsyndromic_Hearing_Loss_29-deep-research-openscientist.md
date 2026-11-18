---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-16T15:08:03.710538'
end_time: '2026-11-16T15:23:31.071431'
duration_seconds: 927.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 29
  mondo_id: MONDO:0013537
  category: Mendelian
  causal_genes: CLDN14
  omim_id: OMIM:614035
  synonyms: DFNB29; CLDN14 autosomal recessive nonsyndromic deafness; autosomal recessive
    nonsyndromic deafness caused by mutation in CLDN14; deafness, autosomal recessive
    29
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
  job_id: 6ac82395-3e0d-42d8-b20f-e516289d4cf3
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMID:42343561
  needs_review: true
  validator_version: 0.6.0
term_validation:
  total_terms: 28
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: UBERON:0001844
    reported_labels:
    - cochlea
    - Organ:** inner ear / **cochlea
    ontology_label: cochlea
  - term_id: NCIT:C16136
    reported_labels:
    - Cochlear Implant
    ontology_label: Natural History and Cofactors Study
  - term_id: NCIT:C50070
    reported_labels:
    - Hearing Aid
    ontology_label: Mirror Device
  - term_id: NCIT:C15296
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Isolated Chemotherapeutic Perfusion
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_29-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_29-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 29
- **MONDO ID:** MONDO:0013537 (if available)
- **Causal gene(s):** CLDN14
- **OMIM:** OMIM:614035
- **Synonyms:** DFNB29; CLDN14 autosomal recessive nonsyndromic deafness; autosomal recessive nonsyndromic deafness caused by mutation in CLDN14; deafness, autosomal recessive 29
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 29** covering all of the
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

# Autosomal Recessive Nonsyndromic Hearing Loss 29 (DFNB29) — Comprehensive Disease Report

**Disease:** Autosomal Recessive Nonsyndromic Hearing Loss 29 (DFNB29)
**MONDO ID:** MONDO:0013537 · **OMIM:** #614035 (phenotype), *605608 (gene)
**Causal gene:** **CLDN14** (claudin-14), HGNC:2035, chromosome 21q22.13
**Category:** Mendelian, autosomal recessive

---

## Summary

**Autosomal Recessive Nonsyndromic Hearing Loss 29 (DFNB29)** is a rare, nonsyndromic, sensorineural form of hereditary deafness caused by **biallelic loss-of-function variants in CLDN14**, the gene encoding the tight-junction protein **claudin-14**. The locus was mapped to chromosome 21q22.1 and the gene identified in two large consanguineous Pakistani families ([PMID: 11163249](https://pubmed.ncbi.nlm.nih.gov/11163249/)). This report follows the identifiers provided (MONDO:0013537 / OMIM:614035 / *CLDN14*) and is not the similarly numbered but gene-distinct DFNB loci (e.g., DFNB1/*GJB2*). Claudin-14 is a four-transmembrane-domain protein that polymerizes into tight-junction strands within the sensory epithelium (organ of Corti) of the inner ear, where it forms a **cation-restrictive paracellular barrier** at the apex of the reticular lamina. When this barrier is lost, the ionic environment around cochlear hair cells is disrupted, triggering hair-cell degeneration and deafness.

The core clinical phenotype is **prelingual, bilateral, sensorineural hearing loss of variable severity (moderate to profound)**. Unlike many deafness genes that collapse the endocochlear potential (EP), the hallmark of DFNB29 — demonstrated in the Cldn14-knockout mouse — is that the **EP is preserved**, yet mice are deaf because of rapid degeneration of **outer hair cells** followed by slower loss of **inner hair cells** during the first three postnatal weeks ([PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/)). A later neural phenotype — loss of inner-hair-cell ribbon synapses and auditory-nerve-fiber regression — has also been documented in the mouse, which is relevant to cochlear-implant rehabilitation that depends on spiral-ganglion-neuron survival ([PMID: 32251970](https://pubmed.ncbi.nlm.nih.gov/32251970/)).

DFNB29 is strongly associated with **consanguinity and founder effects**. In Pakistan, CLDN14 accounts for roughly 2.25% of deafness families and is one of ~13 genes explaining >50% of profound autosomal recessive nonsyndromic hearing loss; the missense allele **p.Val85Asp** is the predominant founder mutation. A separate founder allele, **p.Ala163Val**, causes a distinctive precipitous audioprofile in Newfoundland. There is **no gene-specific drug or approved gene therapy**: management is device-based and rehabilitative — universal newborn hearing screening, hearing aids, and **early cochlear implantation** with speech/language (re)habilitation, plus genetic counseling and carrier/cascade screening in at-risk families. This report is compiled from **aggregated disease-level resources** (OMIM, Orphanet, ClinVar/gnomAD, HPO) and **primary literature** (human clinical cohorts, the Cldn14 knockout mouse, and in-vitro tight-junction assays); it is not derived from individual EHR records.

---

## Key Findings

### Finding 1 — CLDN14 loss-of-function causes DFNB29 (causal gene established)

DFNB29 is caused by loss-of-function mutations in **CLDN14**, which encodes **claudin-14**, a tight-junction protein expressed in the sensory epithelium of the inner ear. The disease locus was mapped to chromosome 21q22.1 and the causal gene was identified by Wilcox and colleagues in two large consanguineous Pakistani families.

> *"The essential function of one of these claudins in the inner ear was established by identifying mutations in CLDN14 that cause nonsyndromic recessive deafness DFNB29 in two large consanguineous Pakistani families."* — [PMID: 11163249](https://pubmed.ncbi.nlm.nih.gov/11163249/)

Key identifiers: **MONDO:0013537; OMIM phenotype #614035; OMIM gene *605608; HGNC:2035; Ensembl ENSG00000159261; UniProt O95500**; gene locus chromosome 21q22.13 (GRCh38 chr21:36,460,621–36,576,569). This is a **germline**, Mendelian, disease-level characterization (aggregated from clinical genetics cohorts and model organisms), not EHR-derived.

### Finding 2 — Pathomechanism: a cation-restrictive cochlear tight-junction barrier whose loss kills hair cells

Claudin-14 functions as a **cation-restrictive paracellular barrier** at the tight-junction complex of the reticular lamina in the organ of Corti. In the Cldn14-null mouse, the **endocochlear potential is normal**, yet the animals are deaf because of hair-cell degeneration, establishing that the defect is one of ionic micro-environment homeostasis around hair cells rather than EP generation.

> *"Cldn14-null mice have a normal endocochlear potential but are deaf due to rapid degeneration of cochlear outer hair cells, followed by slower degeneration of the inner hair cells, during the first 3 weeks of life."* — [PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/)

> *"the TJ complex at the apex of the reticular lamina requires claudin 14 as a cation-restrictive barrier to maintain the proper ionic composition of the fluid surrounding the basolateral surface of outer hair cells"* — [PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/)

In vitro, MDCK monolayers expressing claudin-14 show a **~6-fold increase in transepithelial electrical resistance** by decreasing paracellular permeability for cations. The reticular lamina normally separates high-K⁺ endolymph (apical) from the perilymph-like fluid bathing the basolateral hair-cell surface; claudin-14 maintains this segregation. Its loss allows cation leakage into the basolateral compartment, poisoning hair cells.

### Finding 3 — Founder effects and distinct molecular mechanisms of missense variants

CLDN14 deafness is marked by recurrent **founder alleles**. The Newfoundland founder variant **c.488C>T p.(Ala163Val)** was homozygous in all 12 subjects with a distinctive prelingual, precipitous (rapidly deteriorating above 0.5 kHz) audioprofile, and 1% of population controls were heterozygous carriers.

> *"sequencing 175 population controls revealed 1% of the population are heterozygous for CLDN14 p.(Ala163Val), consistent with a major founder effect in Newfoundland"* — [PMID: 27838790](https://pubmed.ncbi.nlm.nih.gov/27838790/)

At the molecular level, different pathogenic missense variants disable claudin-14 by **different mechanisms**: wild-type CLDN14 forms tight junctions in L fibroblasts, whereas p.V85D (Pakistani) and p.G101R (Spanish/Greek) mutants fail to do so and differ in their plasma-membrane localization.

> *"different mutations of CLDN14 impaired by different mechanisms the ability of the protein to form tight junctions"* — [PMID: 15880785](https://pubmed.ncbi.nlm.nih.gov/15880785/)

CLDN14 is one of ~13 genes accounting for >50% of profound ARNSHL in consanguineous Pakistani populations ([PMID: 38534090](https://pubmed.ncbi.nlm.nih.gov/38534090/)).

### Finding 4 — A second, dosage-sensitive renal role (gain of expression causes hypercalciuria), opposite in direction to the deafness mechanism

CLDN14 has a distinct, **dosage-sensitive** role in renal calcium handling. In the thick ascending limb of the nephron, calcium-sensing receptor (CaSR) activation **increases** claudin-14 expression, which **blocks** paracellular calcium reabsorption. A cis-regulatory SNP within the CLDN14 risk haplotype (creating an INSM1 binding site) increases CLDN14 expression and is associated with pediatric-onset hypercalciuria and kidney stones.

> *"children with the INSM1 binding site within the CLDN14 risk haplotype have a higher likelihood of hypercalciuria and kidney stones. Enhanced CLDN14 expression may play a role in the pathophysiology of their hypercalciuria"* — [PMID: 28229505](https://pubmed.ncbi.nlm.nih.gov/28229505/)

This is mechanistically important for interpreting DFNB29: the **deafness phenotype is caused by loss of function** (too little claudin-14 barrier in the cochlea), whereas the **renal stone phenotype is caused by gain of expression** (too much claudin-14 in the kidney). The two phenotypes are opposite in direction and do not co-segregate as a syndrome — DFNB29 remains **nonsyndromic** ([PMID: 33796889](https://pubmed.ncbi.nlm.nih.gov/33796889/)).

### Finding 5 — Clinical phenotype and the Pakistani founder allele p.V85D

> *"Typically, the DFNB29 phenotype is characterized by prelingual, bilateral, sensorineural hearing loss."* — [PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/)

In a cohort of 800 Pakistani deafness families, CLDN14 mutations were found in **18/800 families (2.25%; 95% CI 1.4–3.5%)**. Five pathogenic alleles were identified: novel p.Ser87Ile and p.Ala94Val, plus p.Arg81His, p.Val85Asp, and the frameshift p.Met133ArgfsX23. p.V85D and p.M133RfsX23 behave as founder mutations, and **p.V85D accounts for ~67% of mutant CLDN14 alleles** in that cohort.

> *"The p.Val85Asp accounts for ~67% of the mutant alleles of CLDN14 in our cohort."* — [PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/)

Severity is variable:

> *"Hearing loss in the affected individuals homozygous for CLDN14 mutations varied from moderate to profound. This phenotypic variability may be due to environmental factors (for example drug and noise exposure) and/or genetic modifiers."* — [PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/)

This documents **variable expressivity** with proposed environmental (ototoxic drugs, noise) and genetic modifier contributions.

### Finding 6 — The Cldn14 knockout mouse is a faithful model with later neural/synaptic degeneration

The targeted **Cldn14-null (Cldn14-lacZ) mouse** recapitulates human DFNB29: deafness arising from rapid outer- then slower inner-hair-cell degeneration in the first three postnatal weeks, with a normal endocochlear potential ([PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/)). A later study documented secondary neural pathology — *"Loss of inner hair cell ribbon synapses and auditory nerve fiber regression in Cldn14 knockout mice"* ([PMID: 32251970](https://pubmed.ncbi.nlm.nih.gov/32251970/)) — relevant to cochlear-implant outcomes, which depend on spiral-ganglion-neuron survival.

> *"In Cldn14-lacZ heterozygous mice beta-galactosidase activity was detected in cochlear inner and outer hair cells and supporting cells, in the collecting ducts of the kidney, and around the lobules of the liver."* — [PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/)

The β-galactosidase (Cldn14-promoter) reporter maps native expression to **cochlear hair cells and supporting cells, renal collecting ducts, and liver lobules**, consistent with the gene's dual auditory and renal roles.

### Finding 7 — Management is non-gene-specific: screening, hearing aids, and early cochlear implantation

No disease-specific pharmacotherapy or approved gene therapy exists for CLDN14 deafness; management follows the general pathway for prelingual sensorineural hearing loss. Universal newborn hearing screening (UNHS) enables earlier diagnosis, referral, and implantation ([PMID: 32179204](https://pubmed.ncbi.nlm.nih.gov/32179204/)).

> *"cochlear implantation (CI) prior to 12 months of age offers the opportunity to foster more typical auditory development during late infancy and early childhood"* — [PMID: 34281434](https://pubmed.ncbi.nlm.nih.gov/34281434/)

> *"Universal newborn hearing screening is a cornerstone of early diagnosis and intervention, enabling superior outcomes with cochlear implantation or emerging gene therapies."* — [PMID: 42319402](https://pubmed.ncbi.nlm.nih.gov/42319402/)

Preventive framing emphasizes UNHS, avoidance of ototoxic drugs and noise, and auditory rehabilitation with hearing aids or implants.

### Finding 8 — CLDN14 variant spectrum (ClinVar)

ClinVar (queried through gnomAD, GRCh38) lists **176 CLDN14 variants**, of which **40 are classified Pathogenic/Likely pathogenic**, comprising **10 missense, 9 frameshift, 7 stop-gained (nonsense)**, plus UTR variants. Confirmed pathogenic/likely-pathogenic deafness alleles include c.254T>A p.Val85Asp, c.398del p.Met133ArgfsTer24, c.242G>A p.Arg81His, c.202C>T p.Arg68Ter, c.167G>A p.Trp56Ter, c.285C>A p.Cys95Ter, and c.291C>A p.Cys97Ter. The milder founder missense alleles c.488C>T p.Ala163Val and c.301G>A p.Gly101Arg are listed under "Conflicting classifications," consistent with their milder/variable audiologic effect.

### Finding 9 & 10 — Protein structure: a 239-aa tetraspan; deafness variants cluster in ECL1/TM2

Claudins are four-transmembrane tight-junction proteins that polymerize into strands and *"either seal the paracellular space or assemble into charge and size-selective pathways"* resembling ion channels ([PMID: 42343561](https://pubmed.ncbi.nlm.nih.gov/42343561/)). Claudin-14 behaves as a **sealing/cation-barrier-type** member: its expression raises transepithelial resistance ~6-fold by decreasing paracellular cation permeability ([PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/)).

UniProt **O95500** topology: **239 amino acids; four transmembrane helices (aa 8–28, 82–102, 116–136, 163–183); extracellular loop 1 (ECL1, aa 29–81); extracellular loop 2 (ECL2, aa 137–162); cytoplasmic N-terminus (1–7) and C-terminus (184–239)**. InterPro claudin family (PF00822). Mapping pathogenic alleles onto the topology shows deafness variants concentrate in **ECL1 and TM2** — the regions that govern **charge selectivity** and **cis/trans tight-junction strand assembly**: p.Arg81His (end of ECL1), p.Val85Asp and p.Gly101Arg (TM2), p.Met133* (TM3), p.Ala163Val (start of TM4).

| Allele | Nucleotide | Region | Type | Population / note |
|---|---|---|---|---|
| p.Val85Asp | c.254T>A | TM2 | Missense | Pakistani founder (~67% of mutant alleles); fails TJ formation in vitro |
| p.Met133ArgfsTer24 | c.398del | TM3 | Frameshift | Pakistani founder |
| p.Arg81His | c.242G>A | end of ECL1 | Missense | Pakistani |
| p.Gly101Arg | c.301G>A | TM2 | Missense | Spanish/Greek; conflicting classification |
| p.Ala163Val | c.488C>T | start of TM4 | Missense | Newfoundland founder; precipitous audioprofile; conflicting classification |
| p.Arg68Ter / p.Trp56Ter | c.202C>T / c.167G>A | ECL1 | Nonsense | Pathogenic |
| p.Cys95Ter / p.Cys97Ter | c.285C>A / c.291C>A | TM2 | Nonsense | Pathogenic |

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in CLDN14** (missense in ECL1/TM2, frameshift, or nonsense) **leads to** absent or non-functional claudin-14 protein. *(Demonstrated — human genetics + in-vitro TJ-formation assays, [PMID: 11163249](https://pubmed.ncbi.nlm.nih.gov/11163249/), [PMID: 15880785](https://pubmed.ncbi.nlm.nih.gov/15880785/).)*
2. Loss of claudin-14 **results in** failure to assemble/seal the cation-restrictive tight-junction strands at the apex of the **reticular lamina** in the organ of Corti. *(Demonstrated — in vitro ~6-fold TER increase requires claudin-14; localization at reticular lamina.)*
3. The defective barrier **leads to** abnormal paracellular cation (K⁺) leakage and loss of proper ionic composition of the fluid bathing the **basolateral** surface of hair cells — while the **endocochlear potential remains normal**. *(Demonstrated — Cldn14-KO mouse, [PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/).)*
4. The disturbed basolateral ionic micro-environment **results in** rapid degeneration of **outer hair cells**, then slower degeneration of **inner hair cells**, over the first ~3 postnatal weeks. *(Demonstrated — mouse.)*
5. **Branch:** hair-cell loss **leads to** downstream **inner-hair-cell ribbon-synapse loss and auditory-nerve-fiber regression**. *(Demonstrated in mouse, [PMID: 32251970](https://pubmed.ncbi.nlm.nih.gov/32251970/); inferred to contribute to the human neural substrate relevant for implantation.)*
6. Hair-cell and synaptic loss **results in** **prelingual, bilateral, sensorineural hearing loss** of variable (moderate-to-profound) severity. *(Demonstrated — human, [PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/).)*
7. **Modifier branch:** ototoxic-drug/noise exposure and genetic modifiers **modulate** severity (variable expressivity). *(Inferred/proposed — [PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/).)*

```
CLDN14 biallelic LoF
        │ leads to
        ▼
No functional claudin-14 at reticular-lamina tight junction
        │ results in
        ▼
Cation-restrictive paracellular barrier fails  ──►  EP stays NORMAL
        │ (K+ leaks to basolateral hair-cell compartment)
        ▼
Outer hair cell degeneration ──► Inner hair cell degeneration
        │                                   │ branch
        ▼                                   ▼
Prelingual bilateral SNHL          Ribbon-synapse loss +
(moderate → profound)              auditory-nerve regression
        ▲
        │ modifiers: ototoxic drugs, noise, genetic background
```

**Upstream vs downstream:** the mutation and tight-junction barrier failure are upstream; ionic disturbance is intermediate; hair-cell death, synaptic/neural regression, and audiometric loss are downstream. **Contrast with EP-collapse deafness** (e.g., gap-junction GJB2 or endolymph-related genes): DFNB29 preserves the EP, distinguishing its mechanism from those that impair endolymph K⁺ recycling or stria vascularis function.

### Suggested ontology terms

- **Gene/protein:** CLDN14 (HGNC:2035); GO:0070160 tight junction; GO:0005923 bicellular tight junction; GO:0016324 apical plasma membrane; GO:0034329 cell junction assembly.
- **Biological processes:** GO:0042472 inner ear morphogenesis; GO:0060113 inner ear receptor cell differentiation; GO:0008219 cell death (hair cell); GO:0034220 monoatomic ion transmembrane transport.
- **Cellular component:** GO:0005923 bicellular tight junction; GO:0016324 apical plasma membrane.
- **Cell types (CL):** CL:0000601 cochlear outer hair cell; CL:0000589 cochlear inner hair cell; CL:0000855 sensory hair cell; inner-ear supporting cell; spiral ganglion neuron.
- **Anatomy (UBERON):** UBERON:0002227 organ of Corti; UBERON:0001844 cochlea; UBERON:0001846 internal ear; reticular lamina of the cochlea.
- **Phenotype (HPO):** HP:0000365 Hearing impairment; HP:0000407 Sensorineural hearing impairment; HP:0008527 Congenital sensorineural hearing impairment; HP:0008615 Prelingual sensorineural hearing impairment; HP:0000006 Autosomal recessive inheritance; HP:0012712 Progressive sensorineural hearing impairment (subset).
- **Chemical (CHEBI):** CHEBI:29103 potassium(1+); CHEBI:29108 calcium(2+) (renal branch).
- **Disease:** MONDO:0013537.

---

## Section-by-Section Content

### 1. Disease Information
DFNB29 is a Mendelian, autosomal-recessive, nonsyndromic sensorineural hearing loss. **Identifiers:** MONDO:0013537; OMIM #614035; gene OMIM *605608; MeSH maps to "Deafness, Autosomal Recessive 29." ICD-10 maps broadly to H90.3/H90.5 (sensorineural hearing loss); ICD-11 to AB52 (sensorineural hearing loss). **Synonyms:** DFNB29; CLDN14 autosomal recessive nonsyndromic deafness; deafness, autosomal recessive 29. Information is **disease-level/aggregated** (clinical genetics cohorts, OMIM, model organisms), not EHR/individual-patient-derived.

### 2. Etiology
**Causal factor:** genetic — biallelic loss-of-function CLDN14 variants. **Genetic risk factors:** homozygous/compound-heterozygous CLDN14 pathogenic variants; founder alleles (p.V85D Pakistan, p.A163V Newfoundland); **consanguinity** is the dominant risk amplifier. **Environmental risk/modifier factors:** ototoxic drug exposure and noise may worsen severity (proposed, [PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/)). **Protective factors:** none specific established; avoidance of ototoxins/noise is protective against added damage. **Gene–environment interaction:** variable expressivity attributed partly to drug/noise exposure superimposed on the genetic lesion.

### 3. Phenotypes
- **Hearing loss** (clinical sign / audiometric abnormality): sensorineural, **bilateral**, **prelingual/congenital onset**, severity **variable — moderate to profound**, generally stable-to-progressive. Frequency: ~100% of affected (defining feature). HPO: HP:0000407, HP:0008615, HP:0008527, HP:0000365.
- **Precipitous high-frequency audioprofile** in the Newfoundland p.A163V founder cohort (12/12 subjects). HPO: high-frequency hearing loss; progressive subset HP:0012712.
- **Nonsyndromic:** no consistent vestibular, visual, renal, or other systemic features segregate with deafness. (The renal stone phenotype is a *separate* dosage/gain effect, not part of DFNB29.)
- **Quality-of-life impact:** prelingual deafness impairs speech/language acquisition, education, and social integration if unaddressed; early intervention markedly improves outcomes.

### 4. Genetic / Molecular Information
Causal gene **CLDN14** (HGNC:2035, chr21q22.13, ENSG00000159261). ~40 ClinVar P/LP alleles: missense (ECL1/TM2-clustered), frameshift, nonsense. Functional consequence: **loss of function** (failure of tight-junction strand assembly / barrier). **Allele frequency:** pathogenic alleles are rare globally but locally enriched by founder effects (e.g., p.A163V ~1% carrier in Newfoundland). **Origin:** germline. **Modifier genes:** unidentified but proposed to explain variable severity. **Epigenetic/chromosomal abnormalities:** none characteristic of DFNB29 (a cis-regulatory CLDN14 SNP is relevant to the renal phenotype only, [PMID: 28229505](https://pubmed.ncbi.nlm.nih.gov/28229505/)).

### 5. Environmental Information
No infectious or primary environmental cause. Ototoxic medications (e.g., aminoglycosides, cisplatin) and noise exposure are plausible severity modifiers. No lifestyle factor is causal.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** above for the ordered causal chain, molecular pathway (tight-junction barrier/paracellular ion selectivity), cellular processes (hair-cell degeneration, synaptic/neural regression), protein dysfunction (loss of TJ strand formation), and biochemical abnormality (loss of cation-restrictive paracellular barrier → disturbed basolateral K⁺ homeostasis with preserved EP).

### 7. Anatomical Structures Affected
- **Organ:** inner ear / **cochlea** (UBERON:0001844); primary site **organ of Corti** (UBERON:0002227); body system: auditory/nervous (sensory).
- **Tissue/cell:** cochlear sensory **epithelium**; **outer hair cells** (CL:0000601, affected first) and **inner hair cells** (CL:0000589); **supporting cells**; secondarily **spiral ganglion neurons**.
- **Subcellular:** apical/apicolateral **tight junction** at the **reticular lamina** (GO:0005923; GO:0016324).
- **Localization/laterality:** **bilateral**, symmetric.

### 8. Temporal Development
**Onset:** congenital/prelingual. **Course:** largely stable but can be progressive (precipitous in some founder genotypes); lifelong. **Critical period:** the first years of life are the window for auditory input and language acquisition — hence the premium on early screening and implantation (ideally cochlear implantation before 12 months; [PMID: 34281434](https://pubmed.ncbi.nlm.nih.gov/34281434/)). No spontaneous remission.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (OMIM #614035). **Penetrance:** essentially complete in biallelic carriers. **Expressivity:** variable (moderate–profound). **No anticipation.** **Founder effects:** p.V85D (Pakistan, ~67% of mutant alleles), p.A163V (Newfoundland, ~1% carrier frequency). **Consanguinity:** major contributor; CLDN14 explains ~2.25% of Pakistani deafness families and is among ~13 genes covering >50% of profound ARNSHL there ([PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/), [PMID: 38534090](https://pubmed.ncbi.nlm.nih.gov/38534090/)). CLDN14 is a **minor** contributor in some other populations (e.g., not a major ARNSHL cause in Koreans, [PMID: 24752540](https://pubmed.ncbi.nlm.nih.gov/24752540/)). **Sex ratio:** ~1:1 (recessive). Prevalence of DFNB29 specifically is not precisely tabulated; it is a rare subtype within overall hereditary deafness.

### 10. Diagnostics
Diagnosis rests on **audiometry** (pure-tone/ABR/OAE) confirming bilateral SNHL plus **molecular genetic testing**. Approaches: hearing-loss **gene panels** (CLDN14 included), **whole-exome/whole-genome sequencing**, and **targeted single-gene/founder-variant testing** in appropriate populations (e.g., p.V85D in Pakistani families, p.A163V in Newfoundland). Imaging (CT/MRI) is typically normal (nonsyndromic). **Differential diagnosis:** GJB2/GJB6, SLC26A4 (often with widened vestibular aqueduct), OTOF (auditory neuropathy/temperature-sensitive), and other DFNB genes — distinguished by genetics, EP/OAE pattern, and imaging. **Screening:** universal newborn hearing screening; carrier and cascade screening in consanguineous/founder families.

### 11. Outcome / Prognosis
DFNB29 is **not life-limiting** (normal life expectancy; no excess mortality). Morbidity is confined to **hearing-related disability** and its downstream effects on communication, education, and social participation. With early detection and appropriate amplification or cochlear implantation plus (re)habilitation, functional and language outcomes are generally good; children implanted before 12 months can achieve near-typical auditory development ([PMID: 34281434](https://pubmed.ncbi.nlm.nih.gov/34281434/)). Prognostic factors: age at intervention, device type, residual spiral-ganglion/neural substrate.

### 12. Treatment
No gene-specific pharmacotherapy or approved gene therapy. **Standard of care:** hearing aids for residual-hearing cases; **cochlear implantation** for severe-to-profound prelingual loss, ideally early; speech-language therapy and auditory (re)habilitation. NCIT suggestions: NCIT:C16136 (Cochlear Implant), NCIT:C50070 (Hearing Aid), NCIT:C15296 (Rehabilitation Therapy). Emerging **gene/RNA therapies** for monogenic deafness are an active research frontier but are not CLDN14-specific or approved.

### 13. Prevention
**Primary:** genetic counseling and carrier/cascade screening in consanguineous and founder populations; informed reproductive options (including prenatal/preimplantation testing where chosen). **Secondary:** universal newborn hearing screening for early detection and timely intervention. **Tertiary:** avoidance of ototoxic drugs/noise to prevent added loss; auditory rehabilitation to mitigate secondary social/cognitive consequences ([PMID: 42319402](https://pubmed.ncbi.nlm.nih.gov/42319402/), [PMID: 32179204](https://pubmed.ncbi.nlm.nih.gov/32179204/)).

### 14. Other Species / Natural Disease
Mouse ortholog **Cldn14** (NCBI Gene; MGI). No prominent naturally occurring companion-animal DFNB29 analog is documented here. The mechanism (tight-junction cation barrier in the organ of Corti) is evolutionarily conserved across mammals, supporting translational relevance of the mouse model.

### 15. Model Organisms
**Mouse** is the principal model: targeted **Cldn14-null (Cldn14-lacZ) knockout** ([PMID: 12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/)). **Phenotype recapitulation:** faithful — deafness via outer-then-inner hair-cell degeneration with normal EP, plus later ribbon-synapse loss and auditory-nerve-fiber regression ([PMID: 32251970](https://pubmed.ncbi.nlm.nih.gov/32251970/)). **Reporter** (β-gal) confirms expression in cochlear hair/supporting cells, renal collecting ducts, and liver lobules. **Limitations:** mouse cochlear degeneration timing (first 3 postnatal weeks) and the renal expression context differ from human developmental timelines; in-vitro MDCK/L-fibroblast TJ assays model barrier/strand function but not whole-organ physiology. Resources: MGI, IMPC.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [11163249](https://pubmed.ncbi.nlm.nih.gov/11163249/) | CLDN14 mutations cause DFNB29 | Human genetics | F1 — causal gene |
| [12913076](https://pubmed.ncbi.nlm.nih.gov/12913076/) | Cldn14-KO mouse, hair-cell degeneration | Model organism | F2, F6, F9 — mechanism, EP-normal, model |
| [15880785](https://pubmed.ncbi.nlm.nih.gov/15880785/) | Mutant CLDN14 TJ-formation defects | In vitro | F3 — distinct molecular mechanisms |
| [27838790](https://pubmed.ncbi.nlm.nih.gov/27838790/) | p.A163V founder, precipitous loss | Human genetics | F3 — founder effect, carrier freq |
| [23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/) | Phenotypic variability, Pakistani cohort | Human clinical | F5 — phenotype, p.V85D founder, expressivity |
| [32251970](https://pubmed.ncbi.nlm.nih.gov/32251970/) | Ribbon-synapse/nerve regression | Model organism | F6 — secondary neural pathology |
| [28229505](https://pubmed.ncbi.nlm.nih.gov/28229505/) | cis-regulatory SNP, hypercalciuria | Human genetics | F4 — renal gain-of-expression role |
| [33796889](https://pubmed.ncbi.nlm.nih.gov/33796889/) | Tubular calcium reabsorption | Review | F4 — CaSR/claudin-14 renal pathway |
| [38534090](https://pubmed.ncbi.nlm.nih.gov/38534090/) | Pakistani ARNSHL genes review | Review | F3 — CLDN14 among top genes |
| [34281434](https://pubmed.ncbi.nlm.nih.gov/34281434/) | Cochlear implantation in infants | Clinical | F7 — early CI |
| [32179204](https://pubmed.ncbi.nlm.nih.gov/32179204/) | UNHS impact | Clinical | F7 — newborn screening |
| [42319402](https://pubmed.ncbi.nlm.nih.gov/42319402/) | Prevention in otology | Review | F7 — screening/rehabilitation framework |
| [42343561](https://pubmed.ncbi.nlm.nih.gov/42343561/) | Claudin-15 pores (cryo-ET) | Structural | F9 — claudin family function |
| [24752540](https://pubmed.ncbi.nlm.nih.gov/24752540/) | TJ genes in Korean NSHL | Human genetics | Population variation (minor contributor) |

**Note on citation validation:** the snippet for [PMID: 32251970](https://pubmed.ncbi.nlm.nih.gov/32251970/) was recorded as a title-derived statement ("mismatch" flag against the stored abstract); the finding it supports (secondary synaptic/neural degeneration in the mouse) should be treated accordingly. The [PMID: 42319402](https://pubmed.ncbi.nlm.nih.gov/42319402/) quote was normalized from a parallel-record abstract.

---

## Limitations and Knowledge Gaps

1. **No precise DFNB29 prevalence/incidence.** Figures are population-relative (e.g., 2.25% of Pakistani deafness families); a population-level per-100,000 estimate is not established.
2. **Modifier genes are hypothesized, not identified.** Variable moderate-to-profound severity is attributed to environment and/or genetic modifiers without a mapped modifier locus.
3. **Human cochlear data are indirect.** The EP-normal, hair-cell-degeneration mechanism is established in the mouse; direct human cochlear histopathology is limited for ethical/practical reasons.
4. **Genotype–phenotype correlation is incomplete.** Why some missense alleles (p.A163V, p.G101R) yield milder/variable phenotypes (and "conflicting" ClinVar classifications) versus truncating alleles is only partly resolved.
5. **No CLDN14-specific therapy or trial.** Gene/RNA therapy for monogenic deafness is advancing generally but not for CLDN14 specifically.
6. **The renal (hypercalciuria) role is biologically distinct** and should not be conflated with the nonsyndromic deafness phenotype; its interaction (if any) with DFNB29 carriers is uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype & audiologic natural-history study** across founder cohorts (p.V85D, p.A163V) to quantify progression rates and define severity predictors.
2. **Modifier-gene mapping** (GWAS/WES in families with discordant severity sharing the same CLDN14 genotype) to test the modifier hypothesis from [PMID: 23235333](https://pubmed.ncbi.nlm.nih.gov/23235333/).
3. **Structure–function dissection** of ECL1/TM2 variants (cryo-EM/MD on claudin-14 strand assembly) to explain allele-specific barrier failure mechanisms observed in [PMID: 15880785](https://pubmed.ncbi.nlm.nih.gov/15880785/).
4. **Cochlear-implant outcome study stratified by CLDN14 genotype**, given mouse evidence of secondary neural regression ([PMID: 32251970](https://pubmed.ncbi.nlm.nih.gov/32251970/)) that could affect implant benefit.
5. **Preclinical gene-replacement / base-editing** in Cldn14-null mice with defined therapeutic windows relative to the postnatal degeneration timeline.
6. **Carrier-screening programs** in high-consanguinity/founder populations paired with genetic counseling, as primary prevention.

---

## Consensus Answer

Autosomal Recessive Nonsyndromic Hearing Loss 29 (DFNB29; MONDO:0013537, OMIM #614035) is a rare autosomal-recessive, nonsyndromic sensorineural deafness caused by biallelic loss-of-function variants in **CLDN14** (claudin-14), a four-transmembrane tight-junction protein on chromosome 21q22.13. Loss of claudin-14 abolishes the cation-restrictive paracellular barrier at the reticular lamina of the organ of Corti, disrupting the ionic environment around hair cells (with a preserved endocochlear potential) and causing outer- then inner-hair-cell degeneration, manifesting as prelingual, bilateral, variable moderate-to-profound hearing loss. There is no gene-specific drug or approved gene therapy, so care centers on newborn screening, hearing aids, early cochlear implantation with (re)habilitation, and genetic counseling/carrier screening in consanguineous and founder populations.


## Artifacts

- [OpenScientist final report](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_29-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_29-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42343561` (4 mentions) - Cryo-electron tomography reveals paracellular claudin-15 pores at the tight junction.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `cldn14`, `gene`, `loss`, `deafness`, `dfnb29`, `founder`, `cochlear`, `genetic`, `hearing`, `phenotype`, `claudin-14`, `barrier`, `variable`, `allele`, `prelingual`, `mouse`, `cell`, `degeneration`, `pakistani`, `nonsyndromic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001844` (2 mentions) - the report calls it "cochlea", "Organ:** inner ear / **cochlea"; UBERON calls it **cochlea**
- `NCIT:C16136` (1 mention) - the report calls it "Cochlear Implant"; NCIT calls it **Natural History and Cofactors Study**
- `NCIT:C50070` (1 mention) - the report calls it "Hearing Aid"; NCIT calls it **Mirror Device**
- `NCIT:C15296` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Isolated Chemotherapeutic Perfusion**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000589` (2 mentions) - the report calls it "inner hair cells"; CL calls it **cochlear inner hair cell**, and lists "inner hair cell" among its other names
- `UBERON:0002227` (2 mentions) - the report calls it "organ of Corti"; UBERON calls it **spiral organ of cochlea**, and lists "organ of Corti" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001844` - called "cochlea", "Organ:** inner ear / **cochlea"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.