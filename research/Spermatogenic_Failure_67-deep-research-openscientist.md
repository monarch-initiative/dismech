---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T04:18:38.639466'
end_time: '2026-10-23T04:36:36.350682'
duration_seconds: 1077.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spermatogenic Failure 67
  mondo_id: MONDO:0030718
  category: Mendelian
  causal_genes: CCDC62
  omim_id: OMIM:619803
  synonyms: SPGF67
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 7
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 21
  verified: 18
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 8
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0030718
    reported_labels:
    - MONDO
    ontology_label: spermatogenic failure 67
  - term_id: CL:0000018
    reported_labels:
    - spermatid
    - spermatids
    - 'Target cell population: **spermatids'
    ontology_label: spermatid
  - term_id: UBERON:0000473
    reported_labels:
    - testis
    - 'Primary organ: **testis'
    ontology_label: testis
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0030374
    ontology_label: obsolete nuclear receptor coactivator activity
    replaced_by: GO:0003713
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spermatogenic_Failure_67-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spermatogenic_Failure_67-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 67
- **MONDO ID:** MONDO:0030718 (if available)
- **Causal gene(s):** CCDC62
- **OMIM:** OMIM:619803
- **Synonyms:** SPGF67
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 67** covering all of the
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

# Spermatogenic Failure 67 (SPGF67): A Comprehensive Disease Characterization

**Disease:** Spermatogenic Failure 67 (SPGF67)
**Causal gene:** **CCDC62** (coiled-coil domain containing 62)
**OMIM:** 619803 | **MONDO:** MONDO:0030718 | **MedGen:** C5676947
**Category:** Mendelian, autosomal recessive, male-limited

---

## Summary

**Spermatogenic Failure 67 (SPGF67) is an autosomal-recessive, male-limited primary infertility disorder caused by biallelic loss-of-function variants in the gene *CCDC62* (coiled-coil domain containing 62).** The disorder sits within the globozoospermia/acrosomal-hypoplasia spectrum of teratozoospermic male infertility: affected men produce spermatozoa that lack a normal acrosome, exhibit abnormal head morphology, and show impaired motility, resulting in a failure to fertilize oocytes naturally. Importantly, affected individuals are otherwise healthy with a normal lifespan — the phenotype is confined to the male reproductive system.

CCDC62 is a testis-enriched protein (Human Protein Atlas testis nTPM 65.5) with a dual molecular identity. It is annotated in UniProt (Q6P9F0) as a nuclear-receptor coactivator — historically named **ERAP75** (estrogen-receptor-associated protein 75) — that enhances the transactivation of estrogen receptors ESR1/ESR2 and modulates progesterone, glucocorticoid, and androgen receptors. In the testis, however, its critical role is in **spermiogenesis and acrosome biogenesis**: CCDC62 localizes to the developing acrosome of spermatids and the acrosome of mature sperm, where it colocalizes and physically interacts with GOPC (Golgi-associated PDZ and coiled-coil motif-containing protein) to drive the Golgi-derived vesicular trafficking that builds the acrosome. When CCDC62 function is lost, acrosome formation fails, producing the malformed, acrosome-deficient sperm that define the disease.

Evidence for the gene–disease relationship is triangulated across (1) a validated mouse model (the repro29 ENU line and CRISPR *Ccdc62⁻/⁻* mice) in which a nonsense mutation causes spermiogenesis defects and male infertility; (2) human globozoospermia exome-sequencing cohorts and systematic reviews that list CCDC62 among core globozoospermia genes; and (3) a ClinVar germline **likely-pathogenic frameshift variant, NM_201435.5(CCDC62):c.132_133insG (p.Asn45fs)**, explicitly linked to the SPGF67 condition. There is no curative therapy; management is assisted reproduction via intracytoplasmic sperm injection (ICSI), frequently combined with calcium-ionophore artificial oocyte activation (AOA) to overcome the fertilization failure intrinsic to acrosome-deficient sperm.

---

## Section 1 — Disease Information

**Overview.** SPGF67 is a Mendelian form of non-syndromic male infertility caused by defective spermatogenesis/spermiogenesis. The clinical presentation is primary male infertility with abnormal semen parameters, specifically a teratozoospermia dominated by acrosomal defects (globozoospermia-spectrum: round-headed, acrosome-deficient spermatozoa) accompanied by asthenozoospermia (poor motility).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 619803 |
| MONDO | MONDO:0030718 |
| MedGen | C5676947 |
| Gene MIM (CCDC62) | 613481 |
| HGNC | HGNC:30723 |
| NCBI Gene | 84660 |
| Ensembl | ENSG00000130783 |
| UniProt | Q6P9F0 (CCD62_HUMAN) |
| Cytoband | 12q24.31 (chr12:122,774,517–122,827,528, GRCh38, + strand) |

**Synonyms / alternative names.** SPGF67; spermatogenic failure 67. Gene-level aliases for CCDC62: CT109, ERAP75 (estrogen-receptor-associated protein 75), TSP-NY.

**Information source type.** Information is derived from **aggregated disease-level resources** (OMIM, ClinVar, UniProt, HPA, gnomAD) and **individual published case/cohort reports** (globozoospermia exome studies), not from large EHR registries. SPGF67 is a rare, recently delineated Mendelian entity; patient-level data are limited to small research cohorts and single-case reports.

---

## Section 2 — Etiology

**Primary cause (genetic).** SPGF67 is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in CCDC62**. The mechanism is loss of function: truncating variants (frameshift, nonsense) that eliminate or severely truncate the protein. This is supported in model organisms by a nonsense mutation in *Ccdc62* exon 6 producing a premature stop codon and a truncated protein, which causes male infertility in mice (Finding F001).

> "we identified a nonsense mutation in the exon 6 of coiled-coil domain-containing 62 gene (Ccdc62), which results in a formation of a premature stop codon and a truncated protein" — [PMID: 28339613](https://pubmed.ncbi.nlm.nih.gov/28339613/)

**Genetic risk factors.** The disease is monogenic; the causal variants are themselves the risk factors. **Consanguinity** increases risk of the homozygous state, as for most autosomal-recessive disorders. No common susceptibility loci or modifier genes have been established specifically for SPGF67.

**Environmental risk factors.** None established as causal for this Mendelian entity. General male-infertility environmental contributors (heat, toxins, smoking) are not implicated in the molecular causation of CCDC62-related disease.

**Protective factors.** No genetic or environmental protective factors have been described. Because the phenotype is reproductive and otherwise health-neutral, there is no selective-pressure landscape analogous to protective alleles in systemic diseases.

**Gene–environment interactions.** None documented for SPGF67.

---

## Section 3 — Phenotypes

The phenotype is confined to the male reproductive system and is detected through semen analysis and infertility workup.

| Phenotype | Type | Suggested HPO term | Characteristics |
|---|---|---|---|
| Male infertility | Clinical sign | HP:0003251 (Male infertility) | Adult-onset (recognized at reproductive age); severe; stable/non-progressive; near-complete among affected men |
| Abnormal sperm morphology / teratozoospermia (globozoospermia-spectrum, acrosome-deficient round-headed sperm) | Laboratory abnormality | HP:0012864 (Abnormal sperm morphology); globozoospermia-type presentation | Severe; stable |
| Asthenozoospermia (reduced motility) | Laboratory abnormality | HP:0012207 (Reduced sperm motility) | Variable-to-severe |
| Acrosome absence/hypoplasia | Laboratory/ultrastructural abnormality | Abnormal acrosome morphology | Severe; the defining molecular lesion |

**Age of onset.** Effectively congenital at the cellular level (spermiogenesis is defective from puberty onward), but **clinically recognized in adulthood** when infertility is investigated.

**Severity / progression.** Severe and stable; this is not a progressive disease. Secondary sexual characteristics, testosterone-dependent development, and general health are unaffected.

**Frequency among affected individuals.** Infertility is essentially fully penetrant in biallelic carriers; the specific semen phenotype falls within the globozoospermia/acrosomal-hypoplasia spectrum.

**Quality-of-life impact.** The impact is psychosocial — infertility and its associated distress — rather than physical disability. There is no effect on daily functioning, lifespan, or non-reproductive health.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** CCDC62 (HGNC:30723; NCBI Gene 84660; Ensembl ENSG00000130783; gene MIM 613481), located at 12q24.31 on the plus strand (Finding F001).

**Protein.** UniProt Q6P9F0, 684 amino acids. Annotated function (Finding F006): *"Nuclear receptor coactivator that can enhance preferentially estrogen receptors ESR1 and ESR2 transactivation. Also modulates progesterone/PGR, glucocorticoid/NR3C1 and androgen/AR receptors transactivation… Required for normal spermiogenesis. It probably plays a role in acrosome formation."* The protein contains **coiled-coil domains** (the basis of the gene name) that mediate protein–protein interactions, including the interaction with GOPC.

**Pathogenic variants.**

| Variant (ClinVar) | Protein | Type | Classification | Condition link |
|---|---|---|---|---|
| NM_201435.5(CCDC62):c.132_133insG | p.Asn45fs | Frameshift | **Likely pathogenic** | SPGF67 (RCV006696178; MedGen C5676947) |
| (3 additional LP records) | — | truncating | Likely pathogenic | — |
| c.559C>G | p.Leu187Val | Missense | VUS | — |
| c.655G>A | p.Val219Ile | Missense | Likely benign | — |
| c.773T>C | p.Val258Ala | Missense | Likely benign | — |

The ClinVar landscape for CCDC62 (~50 records) comprises the SPGF67-linked likely-pathogenic frameshift, additional LP/pathogenic truncating entries, ~19 VUS (mostly missense), and a few likely-benign missense variants (Finding F007). The "Pathogenic" entries in ClinVar are large 12q24 copy-number gains spanning many genes, not CCDC62-specific point mutations.

**Variant type/class.** Predominantly **truncating (frameshift/nonsense) loss-of-function** variants are disease-causing.

**Allele frequency / population genetics (Finding F009).** In gnomAD v4, CCDC62 carries 192 LoF variants with a maximum LoF allele frequency of ~1.4×10⁻⁴ (e.g., heterozygous c.979dup, AC=7/152,010). There is **no common homozygous LoF** in the population, consistent with recessive disease and tolerance of the heterozygous LoF state (pLI ≈ 0; observed/expected LoF ≈ 0.89). The SPGF67 frameshift c.132_133insG is ultra-rare/absent from gnomAD.

**Functional consequence.** **Loss of function.** Biallelic truncation removes the CCDC62 protein's capacity to support acrosome biogenesis.

**Somatic vs germline.** **Germline** (constitutional). The ClinVar SPGF67 variant is annotated germline origin.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes or epigenetic mechanisms are established for SPGF67. Large 12q24 copy-number gains encompassing CCDC62 appear in ClinVar but are not SPGF67-specific.

---

## Section 5 — Environmental Information

SPGF67 is a **monogenic disorder with no established environmental, lifestyle, or infectious contribution** to its causation. There are no implicated toxins, occupational exposures, dietary factors, or pathogens. This section is **not applicable** beyond noting that the disease is purely genetic.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in CCDC62** (e.g., p.Asn45fs frameshift, or nonsense truncation) **lead to** absence or severe truncation of the CCDC62 protein in developing spermatids. *(Demonstrated in mouse; inferred for human by variant class and ClinVar classification.)*
2. Loss of CCDC62 **results in** failure of its interaction with **GOPC** at the Golgi/developing acrosome. *(Demonstrated — colocalization and interaction shown in mouse.)*
3. Disrupted CCDC62–GOPC-dependent **Golgi-derived vesicular trafficking leads to** failed proacrosomal vesicle fusion and **defective acrosome biogenesis**. *(Mechanistically inferred from GOPC biology and CCDC62 localization.)*
4. Defective acrosome formation **results in** abnormal sperm-head shaping and **acrosome-deficient, round-headed/malformed spermatozoa** (globozoospermia spectrum), often with **impaired motility** (asthenozoospermia). *(Demonstrated phenotype in mouse; consistent with human globozoospermia.)*
5. Acrosome-deficient sperm **cannot undergo the acrosome reaction / normal zona penetration**, **leading to** fertilization failure and **primary male infertility**. *(Demonstrated clinically — fertilization failure requires ICSI ± AOA.)*

```
CCDC62 biallelic LoF
        │ (loss of protein)
        ▼
Loss of CCDC62–GOPC interaction at Golgi/acrosome
        │
        ▼
Defective Golgi-derived proacrosomal vesicle trafficking/fusion
        │
        ▼
Failed acrosome biogenesis ──► abnormal sperm-head shaping
        │                              │
        ▼                              ▼
Acrosome-deficient sperm         Reduced motility
        │                              │
        └──────────────┬───────────────┘
                       ▼
          Fertilization failure → primary male infertility
```

### Detail

**Molecular pathways / cellular processes.** The core process is **acrosome assembly** (a specialized Golgi-derived secretory-organelle biogenesis during spermiogenesis). CCDC62 acts as a scaffold/adaptor via coiled-coil-mediated protein interactions. In mouse testis, CCDC62 is expressed in the cytoplasm and developing acrosome of spermatids and localizes specifically to the acrosome of mature sperm (Finding F002).

> "CCDC62 was expressed in the cytoplasm and the developing acrosome in the spematids of mouse testis, and was specifically localized at the acrosome in mature sperm" — [PMID: 28339613](https://pubmed.ncbi.nlm.nih.gov/28339613/)

> "intracellular colocalization and interaction of CCDC62 and Golgi-associated PDZ and coiled-coil motif-containing protein may be important for acrosome formation" — [PMID: 28339613](https://pubmed.ncbi.nlm.nih.gov/28339613/)

**Protein-interaction network (Finding F008).** STRING places CCDC62 firmly in the acrosome-biogenesis/globozoospermia module: top functional partners include SPATA16 (0.707), DPY19L2 (0.688), CCIN (0.624), C2CD6 (0.604), SPACA1 (0.593), PICK1 (0.579), C7orf61 (0.728), plus vesicle-trafficking proteins HIP1R (0.87), SYT11 (0.681), SYT12 (0.679), and the estrogen receptor ESR2 (0.782). This recapitulates both CCDC62 functions — the acrosome/globozoospermia module and the nuclear-receptor (ESR2) coactivator role.

**Dual molecular function (Finding F006).** Beyond spermiogenesis, CCDC62/ERAP75 is a nuclear-receptor coactivator for ESR1/ESR2 (and modulates PGR, NR3C1, AR). HPA subcellular immunofluorescence in somatic cell lines shows nucleoplasm + plasma-membrane staining, consistent with the nuclear-coactivator role. The reproductive phenotype, however, derives from the acrosome-biogenesis function in the germline.

**Suggested ontology terms.**
- **GO biological process:** GO:0007340 (acrosome reaction); GO:0001675 (acrosome assembly); GO:0007283 (spermatogenesis); GO:0030154 (cell differentiation); nuclear-receptor coactivator activity GO:0030374.
- **GO cellular component:** GO:0001669 (acrosomal vesicle); GO:0005794 (Golgi apparatus); GO:0005654 (nucleoplasm).
- **CL cell types:** CL:0000018 (spermatid); CL:0000019 (sperm); CL:0000020 (spermatogonium — upstream); CL:0000216 (Sertoli cell — supportive).

**Single-cell context.** Human testis single-cell studies (PMID 40371706) report CCDC62 co-expression with SOX9 (a Sertoli-cell marker) in testis tissue, indicating expression may include a Sertoli-cell (supportive niche) component; the mechanistically validated role remains spermatid acrosome biogenesis.

> "PRAP1, BST2, and CCDC62 were co-expressed with SOX9 (classical marker of Sertoli cell) in testes tissues also confirmed by immunofluorescence" — [PMID: 40371706](https://pubmed.ncbi.nlm.nih.gov/40371706/)

---

## Section 7 — Anatomical Structures Affected

**Organ level.**
- Primary organ: **testis** (UBERON:0000473), specifically the seminiferous tubules (UBERON:0001343).
- Body system: **male reproductive system** (UBERON:0000079).
- No secondary organ involvement — the disease is reproductive-limited.

**Tissue and cell level.**
- Tissue: seminiferous epithelium (germinal epithelium).
- Target cell population: **spermatids** (CL:0000018) and **spermatozoa** (CL:0000019); supportive **Sertoli cells** (CL:0000216) co-express CCDC62.

**Subcellular level.**
- **Acrosome / acrosomal vesicle** (GO:0001669) — the defining compromised compartment.
- **Golgi apparatus** (GO:0005794) — source of proacrosomal vesicles.
- **Nucleus/nucleoplasm** (GO:0005654) — for the ERAP75 coactivator function in somatic contexts.

**Localization / lateralization.** Bilateral (both testes); the defect is intrinsic to germ-cell development, not focal.

---

## Section 8 — Temporal Development

**Onset.** Cellularly congenital/pubertal (spermiogenesis is defective once it begins), but **clinically adult-onset**, recognized during infertility evaluation.

**Progression.** **Stable and non-progressive.** Semen parameters do not deteriorate over time in a disease-specific manner, and there is no systemic disease course.

**Disease course / duration.** Chronic lifelong with respect to the reproductive phenotype; no remission occurs spontaneously, though the fertility barrier can be bypassed with assisted reproduction.

**Critical periods.** The relevant "window" is reproductive age for family planning and assisted-reproduction intervention; there is no developmental critical period for prevention of the molecular defect.

---

## Section 9 — Inheritance and Population

**Inheritance pattern.** **Autosomal recessive**, male-limited expression (the clinical phenotype manifests only in males because the critical function is in spermiogenesis).

**Penetrance / expressivity.** Infertility penetrance in biallelic males appears high/complete; expressivity falls within the globozoospermia/teratozoospermia–asthenozoospermia spectrum.

**Carrier frequency / founder effects.** Heterozygous LoF is tolerated and present in gnomAD at low frequency (max LoF AF ~1.4×10⁻⁴); no founder effect established. The disease-causing homozygous/compound-heterozygous state is very rare.

**Consanguinity.** Elevates risk, as for recessive disorders generally.

**Epidemiology.** SPGF67 is **ultra-rare**; precise prevalence/incidence are not established. It constitutes a small fraction of genetically explained globozoospermia, itself a rare cause of teratozoospermia. CCDC62 is one of several core globozoospermia genes (Findings F003, F005).

> "nine other genes described to be associated with globozoospermia in human (C2CD6, C7orf61, CCDC62, CCIN, DNAH17, GGN, PICK1, SPATA16, and ZPBP1)" — [PMID: 33108537](https://pubmed.ncbi.nlm.nih.gov/33108537/)

> "The main genes involved in the pathogenesis of globozoospermia are DPY19L2, SPATA16, PICK1, GGN, SPACA1, ZPBP, CCDC62, and CCNB3 genes." — [PMID: 36047070](https://pubmed.ncbi.nlm.nih.gov/36047070/)

**Sex ratio.** Clinically male-limited (infertility manifests only in affected males).

---

## Section 10 — Diagnostics

**Clinical/laboratory tests.**
- **Semen analysis** (WHO criteria): identifies teratozoospermia (globozoospermia-type, acrosome-deficient round-headed sperm) and asthenozoospermia. First-line diagnostic test.
- **Sperm morphology/ultrastructure**: light microscopy and transmission electron microscopy confirm absent/hypoplastic acrosome.
- **Hormonal panel** (FSH, LH, testosterone): typically normal, distinguishing from endocrine or obstructive causes.

**Genetic testing (recommended approach).**
- **Whole-exome sequencing (WES)** is the principal diagnostic modality and the method by which CCDC62 was implicated in human globozoospermia (Finding F003).
- **Gene panels** for male infertility/globozoospermia that include CCDC62 alongside DPY19L2, SPATA16, PICK1, ZPBP, SPACA1, GGN, CCNB3.
- **Single-gene / targeted testing** of CCDC62 and **ClinVar** interpretation (the SPGF67 frameshift c.132_133insG is catalogued).
- **Chromosomal microarray / karyotype** to exclude the large 12q24 copy-number gains and other cytogenetic causes.

> "Exome sequencing in 15 cases of unexplained globozoospermia revealed deleterious mutations in seven new genes, of which two have been validated as causing globozoospermia when knocked out in mouse models" — [PMID: 31985809](https://pubmed.ncbi.nlm.nih.gov/31985809/)

**Clinical criteria / differential diagnosis.** Diagnosis integrates semen phenotype + biallelic CCDC62 LoF. Differential diagnosis includes other globozoospermia genes (DPY19L2 is the most common cause), non-obstructive azoospermia, obstructive azoospermia, and endocrine infertility.

**Screening.** Cascade/carrier screening of at-risk relatives in consanguineous families; preconception carrier testing is applicable once a familial variant is known.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality / morbidity.** SPGF67 has **no effect on survival, life expectancy, or systemic morbidity**. The sole consequence is infertility.

**Disease course / recovery.** The reproductive barrier is not self-resolving; however, **biological paternity is achievable via assisted reproduction**. With ICSI (often plus AOA), fertilization and live birth are possible (Findings F004, F005).

**Prognostic factors.** Fertility prognosis depends on residual sperm quality, oocyte-activation competence, and the success of AOA. Globozoospermia is associated with elevated sperm aneuploidy that can affect ART success, but — importantly for counseling — this is **not** associated with increased transmission of genetic abnormalities to offspring (Finding F005).

> "does not appear to be associated with an increased risk of transmission of genetic abnormalities to offspring" — [PMID: 36047070](https://pubmed.ncbi.nlm.nih.gov/36047070/)

---

## Section 12 — Treatment

**There is no curative or disease-modifying therapy.** Management is **assisted reproductive technology (ART)**:

- **Intracytoplasmic sperm injection (ICSI)** — bypasses the acrosome-dependent fertilization steps. NCIT: Intracytoplasmic Sperm Injection.
- **ICSI with artificial oocyte activation (AOA)** using **calcium ionophore / ionomycin** — overcomes the oocyte-activation failure caused by acrosome-deficient sperm (which lack normal PLCζ-mediated calcium signaling). Also **IMSI** (intracytoplasmic morphologically-selected sperm injection) in some protocols.

AOA improves outcomes in severe teratozoospermia/ICSI-failure settings (Finding F004):

> "the fertilization (50.38% versus 33.86%, respectively, P < 0.001), cleavage (59.16% versus 39.04%, respectively, P < 0.001) and transferable embryo rates (43.51% versus 26.69%, respectively, P < 0.001)" — [PMID: 31160240](https://pubmed.ncbi.nlm.nih.gov/31160240/)

A healthy live birth has been reported with calcium-ionophore AOA after round-headed sperm injection, though activation efficiency remains lower than with normal sperm:

> "calcium ionophore treatment can assist oocyte activation in patients with round-headed sperm, but its efficiency to activate oocytes is lower than that induced by a normal sperm injection" — [PMID: 32318024](https://pubmed.ncbi.nlm.nih.gov/32318024/)

An 8-year retrospective study (PMID 41462321) confirms AOA can prevent fertilization failure following ICSI in severe teratozoospermia, while cautioning that cumulative live-birth benefit is limited in some indication subgroups — underscoring the need for informed consent.

> "intracytoplasmic sperm injection with assisted oocyte activation or intracytoplasmic morphologically-selected sperm injection appears to be associated with a higher success rate" — [PMID: 36047070](https://pubmed.ncbi.nlm.nih.gov/36047070/)

**Pharmacotherapy / advanced therapeutics / gene therapy.** None established or applicable. No pharmacogenomic, gene-, cell-, or RNA-based therapy exists for SPGF67.

**Suggested NCIT terms:** Intracytoplasmic Sperm Injection; Assisted Reproductive Technology; In Vitro Fertilization.

---

## Section 13 — Prevention

- **Primary prevention:** not applicable (genetic, non-preventable at the molecular level).
- **Genetic counseling:** central. For a known biallelic/familial CCDC62 variant, counsel on 25% recurrence risk among offspring of two carriers and male-limited expression. Offer **carrier screening** of partners and **cascade testing**.
- **Reproductive options:** **preimplantation genetic testing (PGT)** and prenatal diagnosis are available where a familial variant is defined; donor sperm is an alternative. Despite elevated sperm aneuploidy, globozoospermia does not increase transmission of genetic abnormalities to offspring (reassuring for ART counseling; Finding F005).
- **Immunization / public-health / environmental prevention:** not applicable.

---

## Section 14 — Other Species / Natural Disease

**Model-relevant orthology.** The **mouse ortholog Ccdc62** (MGI:2684996; NCBI Gene 208908; Ensembl ENSMUSG00000061882; chromosome 5) is the key comparative system (Finding F009). A naturally arising ENU mutation (repro29 line) produces the disease phenotype, demonstrating evolutionary conservation of CCDC62's spermiogenesis function.

**Natural disease in other species.** No spontaneous CCDC62-related infertility has been catalogued in companion animals or livestock (no OMIA entry referenced here). The mechanism — acrosome biogenesis — is deeply conserved across mammals, so the pathway is expected to be functionally orthologous.

**Zoonotic / transmission.** Not applicable (non-infectious, non-transmissible).

---

## Section 15 — Model Organisms

**Mouse (*Mus musculus*, NCBI Taxon 10090) is the principal and validating model.**

| Model | Type | Key phenotype | Recapitulation |
|---|---|---|---|
| repro29/repro29 | ENU-induced nonsense (Ccdc62 exon 6 premature stop) | Spermiogenesis defects, deformed sperm, poor motility, male infertility | Strong — recapitulates human acrosome/teratozoospermia infertility |
| Ccdc62⁻/⁻ (CRISPR knockout) | Targeted knockout | Male infertility, acrosome-localization confirmed | Strong — confirms loss-of-function causality |

> "we identified a nonsense mutation in the exon 6 of coiled-coil domain-containing 62 gene (Ccdc62), which results in a formation of a premature stop codon and a truncated protein" — [PMID: 28339613](https://pubmed.ncbi.nlm.nih.gov/28339613/)

**Phenotype recapitulation.** The mouse reproduces the core human features: spermiogenesis/acrosome defect, abnormal sperm morphology, impaired motility, and male infertility — with CCDC62 localized to the developing and mature acrosome and interacting with GOPC.

**Model limitations.** The mouse does not capture the full human allelic/phenotypic spectrum (e.g., variable human teratozoospermia severity), and the human ERAP75/nuclear-receptor-coactivator contribution to any non-reproductive phenotype remains uninvestigated in these infertility-focused models.

**Resources.** MGI (MGI:2684996); IMPC/IMSR for knockout alleles; human globozoospermia research cohorts for validation.

---

## Mechanistic Model / Interpretation

The SPGF67 story is a clean example of a **conserved germ-cell organelle-biogenesis gene** whose loss produces an isolated, health-neutral reproductive phenotype. CCDC62 functions as a coiled-coil scaffold that couples Golgi-derived vesicular trafficking (via GOPC) to acrosome construction in elongating spermatids. The molecular lesion is **loss of function**; because heterozygous LoF is tolerated in the population (no gnomAD homozygotes, oe_lof ≈ 0.89, pLI ≈ 0), disease requires **two hits**, giving autosomal-recessive inheritance. The downstream clinical consequence — acrosome-deficient sperm that cannot fertilize — is bypassable but not curable, which is why ICSI + AOA is the management mainstay.

The protein's second identity as **ERAP75**, a nuclear-receptor coactivator, is intriguing but appears decoupled from the disease phenotype: the reproductive manifestation derives from the germ-cell acrosome function, while the coactivator role is seen in somatic nucleoplasm/plasma-membrane localization. The STRING network cleanly separates these two modules (globozoospermia genes vs. ESR2), supporting a model of **tissue-partitioned function**.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [28339613](https://pubmed.ncbi.nlm.nih.gov/28339613/) | *Nonsense mutation in Ccdc62 → spermiogenesis defects, male infertility (repro29 mice)* | Model organism | F001, F002 — causal LoF, acrosome localization, GOPC interaction |
| [31985809](https://pubmed.ncbi.nlm.nih.gov/31985809/) | *Exome sequencing reveals novel causes/candidate genes for human globozoospermia* | Human clinical | F003 — human discovery context for CCDC62 |
| [33108537](https://pubmed.ncbi.nlm.nih.gov/33108537/) | *Genetic analyses of large globozoospermia cohort (DPY19L2 main actor)* | Human clinical | F003 — CCDC62 among established globozoospermia genes |
| [36047070](https://pubmed.ncbi.nlm.nih.gov/36047070/) | *Globozoospermia: case report & systematic review* | Human review | F005 — core gene list, ART recommendations, offspring risk |
| [31160240](https://pubmed.ncbi.nlm.nih.gov/31160240/) | *AOA improves ICSI fertilization-failure cycles* | Human clinical | F004 — AOA efficacy quantified |
| [32318024](https://pubmed.ncbi.nlm.nih.gov/32318024/) | *Round-headed sperm injection + calcium ionophore vs normal* | Human case | F004 — AOA in acrosome-deficient sperm |
| [41462321](https://pubmed.ncbi.nlm.nih.gov/41462321/) | *8-year retrospective of ionomycin AOA in ICSI* | Human cohort | Treatment — AOA benefit & limits |
| [40371706](https://pubmed.ncbi.nlm.nih.gov/40371706/) | *scRNA/scATAC testis, NOA* | Human single-cell | CCDC62 testis co-expression with SOX9 (Sertoli) |
| [30333325](https://pubmed.ncbi.nlm.nih.gov/30333325/) | *Novel DPY19L2 variants in Chinese globozoospermia* | Human clinical | Globozoospermia differential/context |

---

## Limitations and Knowledge Gaps

1. **Sparse human genetic evidence.** SPGF67 rests on a limited number of human cases plus one ClinVar likely-pathogenic frameshift (c.132_133insG, p.Asn45fs). The full human allelic spectrum, genotype–phenotype correlation, and penetrance estimates are not established.
2. **No formal epidemiology.** Prevalence/incidence and carrier frequency for the disease state are unquantified.
3. **Phenotype boundary.** It is unresolved whether human CCDC62 disease is strictly globozoospermia or a broader teratozoospermia/oligo-astheno-teratozoospermia spectrum; cohort-level semen characterization is lacking.
4. **Dual-function uncertainty.** Whether the ERAP75/nuclear-receptor-coactivator role contributes anything to the human phenotype (or any subclinical endocrine effect) is unknown.
5. **Treatment outcome data are indirect.** AOA/ICSI efficacy data come from general severe-teratozoospermia/globozoospermia populations, not CCDC62-genotyped cohorts.
6. **Variant interpretation.** Most CCDC62 ClinVar variants are VUS; functional assays to reclassify missense variants are needed.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate additional human cases** via GeneMatcher/Matchmaker Exchange to firm up the gene–disease relationship and define penetrance and the semen-phenotype spectrum.
2. **Functional validation of VUS** (minigene/splicing assays; acrosome-biogenesis rescue in cell or organoid systems) to reclassify the ~19 CCDC62 VUS in ClinVar.
3. **Mechanistic dissection of the CCDC62–GOPC axis** — map the coiled-coil interaction interface and test whether patient truncations abolish GOPC binding and proacrosomal vesicle fusion.
4. **Genotype-specific ART outcome study** — track ICSI ± calcium-ionophore AOA fertilization/live-birth rates specifically in CCDC62-biallelic patients.
5. **Single-cell testis profiling** of CCDC62 across spermatogenic stages (and in Sertoli cells, given SOX9 co-expression) to resolve the germ-cell vs. supportive-niche contribution.
6. **Evaluate the ERAP75 function** in germ cells to determine whether nuclear-receptor coactivation has any reproductive relevance, using domain-separation mutants.

---

*Report compiled from 9 confirmed findings and 9 reviewed papers across 5 investigation iterations. Evidence types: model organism (mouse), human clinical/cohort, in vitro/annotation (UniProt, STRING, HPA, ClinVar, gnomAD).*


## Artifacts

- [OpenScientist final report](Spermatogenic_Failure_67-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spermatogenic_Failure_67-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030718` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spermatogenic failure 67**
- `CL:0000018` (2 mentions) - the report calls it "spermatid", "spermatids", "Target cell population: **spermatids"; CL calls it **spermatid**
- `UBERON:0000473` (1 mention) - the report calls it "testis", "Primary organ: **testis"; UBERON calls it **testis**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030374` (obsolete nuclear receptor coactivator activity) (1 mention) - replaced by `GO:0003713`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0001669` (2 mentions) - the report calls it "acrosomal vesicle", "Acrosome / acrosomal vesicle"; GO calls it **acrosomal vesicle**
- `GO:0005654` (2 mentions) - the report calls it "nucleoplasm", "Nucleus/nucleoplasm"; GO calls it **nucleoplasm**
- `CL:0000019` (2 mentions) - the report calls it "sperm", "spermatozoa"; CL calls it **sperm**, and lists "spermatozoid" among its other names
- `CL:0000020` (1 mention) - the report calls it "spermatogonium — upstream"; CL calls it **spermatogonium**
- `CL:0000216` (2 mentions) - the report calls it "Sertoli cell — supportive", "Sertoli cells"; CL calls it **Sertoli cell**
- `UBERON:0000079` (1 mention) - the report calls it "male reproductive system", "Body system: **male reproductive system"; UBERON calls it **male reproductive system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0001669` - called "acrosomal vesicle", "Acrosome / acrosomal vesicle"
- `GO:0005654` - called "nucleoplasm", "Nucleus/nucleoplasm"
- `CL:0000018` - called "spermatid", "spermatids", "Target cell population: **spermatids"
- `CL:0000019` - called "sperm", "spermatozoa"
- `CL:0000216` - called "Sertoli cell — supportive", "Sertoli cells"
- `UBERON:0000473` - called "testis", "Primary organ: **testis"
- `UBERON:0000079` - called "male reproductive system", "Body system: **male reproductive system"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.