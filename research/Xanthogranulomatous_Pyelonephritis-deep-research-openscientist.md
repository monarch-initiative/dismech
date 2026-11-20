---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T02:54:23.628013'
end_time: '2026-09-30T03:22:49.649759'
duration_seconds: 1706.02
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Xanthogranulomatous Pyelonephritis
  mondo_id: MONDO:0007022
  category: Infectious Disease
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
citation_count: 29
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 11
  relevance_assessed: 33
  on_topic: 28
  validator_version: 0.5.1
term_validation:
  total_terms: 30
  verified: 29
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.033
  labels_checked: 17
  labels_matching: 8
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0007022
    reported_labels:
    - if available
    ontology_label: xanthogranulomatous pyelonephritis
  - term_id: HP:0025427
    reported_labels:
    - Bacteriuria
    ontology_label: Abnormal bronchus physiology
  - term_id: GO:0042116
    reported_labels:
    - Cellular processes:** chronic granulomatous inflammation, macrophage activation
    ontology_label: macrophage activation
  - term_id: CL:0000891
    reported_labels:
    - CD68+ lipid-laden macrophages/foam cells
    ontology_label: foam cell
  - term_id: UBERON:0001096
    reported_labels:
    - Secondary / adjacent involvement:** perinephric fat, psoas muscle
    ontology_label: wall of esophagus
  labels_variant: 4
  unresolved_terms:
  - HP:0031183
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Xanthogranulomatous_Pyelonephritis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Xanthogranulomatous_Pyelonephritis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Xanthogranulomatous Pyelonephritis
- **MONDO ID:** MONDO:0007022 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Xanthogranulomatous Pyelonephritis** covering all of the
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

# Xanthogranulomatous Pyelonephritis (XGP): Comprehensive Disease Characterization

**MONDO ID:** MONDO:0007022 · **Category:** Infectious / Chronic Inflammatory Renal Disease
**ICD-10:** N11.8 / N10 (chronic pyelonephritis) · **MeSH:** Pyelonephritis, Xanthogranulomatous (D058365)
**Evidence base:** 11 confirmed findings across 42 reviewed papers (multicenter series, pooled analyses, case series, and case reports)

---

## Summary

Xanthogranulomatous pyelonephritis (XGP) is a rare, acquired (non-genetic) chronic destructive granulomatous form of pyelonephritis. It arises from a characteristic triad—**chronic urinary tract obstruction** (usually by staghorn/struvite calculi), **recurrent bacterial infection** (chiefly *Escherichia coli* and urease-producing *Proteus mirabilis*), and an **incomplete/aberrant host immune response**—that together drive the progressive replacement of renal parenchyma by **lipid-laden CD68+ foamy macrophages**, granulomatous inflammation, and fibrosis. The end result is an enlarged, usually unilateral, non-functioning kidney. The disease predominantly affects middle-aged women and spans all ages from neonate to elderly.

XGP is clinically and radiologically a "great imitator," most notably mimicking renal cell carcinoma (RCC). The classic CT sign is the **"bear paw"** appearance with a central staghorn calculus. Because imaging and even gross pathology overlap with malignancy, **definitive diagnosis is histopathologic**, and **immunohistochemistry (CD68)** is frequently decisive in distinguishing XGP foam cells from the clear cells of RCC. Patients typically present with flank pain, fever, and recurrent urinary tract infections, accompanied by anemia, leukocytosis, pyuria, and hematuria, often after a long diagnostic delay (median ~1 year in one series).

Management is stratified by disease extent and patient age: **nephrectomy remains the definitive treatment for adult diffuse XGP**, whereas **conservative antibiotic-based (kidney-sparing) management** succeeds in a majority of pediatric and focal cases. The condition is curable but carries substantial perioperative morbidity (postoperative complication rates up to 73%, with half being Clavien-Dindo grade ≥3 in one series) and risks of local invasion—psoas abscess, perinephric abscess, and fistulae to skin, colon, or even lung. Rare coexistence with renal malignancy (squamous cell carcinoma, urothelial carcinoma, RCC) is documented, driven by the shared background of chronic stone disease and inflammation. XGP has also now been documented as a naturally occurring disease in at least one non-human species (dog).

---

## 1. Disease Information

**Overview.** XGP is an uncommon chronic destructive granulomatous process of the renal parenchyma occurring in association with long-term urinary tract obstruction and infection. It affects females more often than males across a wide age range, from newborn to elderly [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/). It is regarded as a rare variant of chronic pyelonephritis that produces an enlarged, non-functioning kidney with diffuse parenchymal damage.

**Key identifiers.**
- **MONDO:** MONDO:0007022
- **MeSH:** Pyelonephritis, Xanthogranulomatous
- **ICD-10:** grouped under chronic pyelonephritis (N11.x)
- **OMIM / Orphanet:** No Mendelian OMIM entry (XGP is acquired, not a monogenic disease). No distinct genetic locus.

**Synonyms / alternative names:** Xanthogranulomatous pyelonephritis (XGP, XGPN, XPN); xanthogranulomatous pyelonephritis of the kidney. In older literature sometimes described under "foam-cell" or "lipogranulomatous" pyelonephritis.

**Source of information.** Evidence is derived predominantly from **aggregated disease-level resources**: retrospective multicenter series (e.g., 365 patients across 10 centers/5 countries; [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/)), pooled quantitative analyses of published cases (251 patients; [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/)), single-institution case series, and individual case reports. There is no dedicated genetic or population registry; there are no EHR-derived individual-patient omics datasets specific to XGP.

---

## 2. Etiology

**Primary causal factors.** XGP is a fundamentally **acquired, infectious/mechanistic** disease. It is thought to arise secondary to a combination of **obstruction, recurrent bacterial infection, and an incomplete immune response**, resulting in focal or diffuse renal destruction [PMID: 34522121](https://pubmed.ncbi.nlm.nih.gov/34522121/). Ultrastructural evidence supports a **bacteria-induced process** whose histologic appearance relates to incomplete bacterial degradation and altered host response [PMID: 7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/).

**Risk factors (environmental / clinical).**
- **Nephrolithiasis / staghorn calculi** — the dominant risk factor; multiple stones present in 34.5% of a 365-patient series [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/), and renal stones in 53.8% of a 251-patient pooled cohort [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/).
- **Chronic urinary obstruction** (stones, stricture, rarely tumor).
- **Recurrent urinary tract infection.**
- **Female sex** — 57–72% of patients across series [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/); [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/); [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/).
- **Chronic kidney disease** — most common comorbidity (71%) [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/).
- **Diabetes mellitus / immunocompromise, low socioeconomic status, and limited healthcare access** are reported associations in case literature.

**Genetic risk factors.** None established. XGP is not a heritable Mendelian disorder; there is no OMIM entry, no ClinVar variants, and no GWAS signal specific to XGP. Rare occurrence in patients with polycystic kidney disease is reported but reflects anatomic predisposition to obstruction/infection rather than a defined genetic driver [PMID: 39185472](https://pubmed.ncbi.nlm.nih.gov/39185472/).

**Protective factors.** No genetic protective variants are known. Environmentally, prevention of the causal chain—effective treatment of urolithiasis, relief of obstruction, and prompt treatment of UTIs—is protective by preventing the disease from developing.

**Gene–environment interactions.** Not applicable in a defined molecular sense. The functionally relevant "interaction" is between **host immune competence** (an incomplete/aberrant macrophage response) and the **environmental insult** (obstruction + chronic infection), which together determine whether chronic infection progresses to xanthogranulomatous destruction [PMID: 7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/); [PMID: 34522121](https://pubmed.ncbi.nlm.nih.gov/34522121/).

---

## 3. Phenotypes

XGP presents with a stereotyped constellation of symptoms, signs, and laboratory abnormalities. The best-quantified profiles come from a 57-patient case series [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/) and a 55-case series [PMID: 41250779](https://pubmed.ncbi.nlm.nih.gov/41250779/).

| Phenotype | Type | Frequency | Suggested HPO term |
|---|---|---|---|
| Flank / lumbar pain | Symptom | 89.5% | Flank pain (HP:0030157) |
| Fever | Symptom/sign | 43.9–55.0% | Fever (HP:0001945) |
| Recurrent UTI | Clinical course | 43.9% | Recurrent urinary tract infections (HP:0000010) |
| Anemia | Lab abnormality | 78.9% | Anemia (HP:0001903) |
| Leukocytosis (± left shift) | Lab abnormality | 43.6% (left shift 21.6%) | Leukocytosis (HP:0001974) |
| Hematuria | Lab abnormality | 75.6% | Hematuria (HP:0000790) |
| Pyuria / leukocyturia | Lab abnormality | 93.2% | Pyuria (HP:0012085) |
| Bacteriuria | Lab abnormality | 40.9% | Bacteriuria (HP:0025427) |
| Palpable abdominal / flank mass | Physical sign | variable | Abdominal mass (HP:0031183) |
| Renal calculi | Structural | ~54% to 49/55 (~89%) | Nephrolithiasis (HP:0000787) |
| Hydronephrosis | Structural | common | Hydronephrosis (HP:0000126) |
| Weight loss | Constitutional | variable | Weight loss (HP:0001824) |

**Direct evidence.** "The most common symptoms were flank/lumbar pain (89.5%), fever (43.9%), and recurrent urinary tract infection (43.9%)" and "Blood tests showed anemia (78.9%), leukocytosis (43.6%) with left shift (21.6%). Urinalysis showed hematuria (75.6%), bacteriuria (40.9%), and leukocytes (93.2%)" [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/). Reviews additionally list lower urinary tract symptoms, palpable mass, gross hematuria, and weight loss [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/).

**Phenotype characteristics.**
- **Age of onset:** predominantly adult (mean age 36–49 years across series), but the full range spans neonate to elderly [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/). Pediatric disease occurs and is often focal.
- **Severity:** moderate to severe; can be indolent/asymptomatic until late-stage, then fulminant.
- **Progression:** chronic and progressive with parenchymal destruction; frequently insidious with a long diagnostic delay (median ~365 days in one series) [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/).

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36 data exist for XGP. Impact is inferred from chronic pain, recurrent infection, anemia/fatigue, prolonged diagnostic delay, and the morbidity of eventual nephrectomy (loss of a kidney, perioperative complications).

---

## 4. Genetic / Molecular Information

**Causal genes:** None. XGP is an acquired infectious/inflammatory disease with **no identified causal gene, pathogenic variant, or chromosomal abnormality**. There are no relevant OMIM, ClinVar, HGMD, or COSMIC entries specific to XGP.

**Pathogenic variants / allele frequencies / somatic-vs-germline:** Not applicable.

**Modifier genes:** None established. Host factors modulating macrophage lipid handling and bacterial clearance are mechanistically implicated but not genetically defined [PMID: 7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/).

**Epigenetic information:** No XGP-specific DNA methylation, histone modification, or chromatin studies are available.

**Chromosomal abnormalities:** Not applicable to XGP itself. (Note: coexisting malignancies such as squamous cell or urothelial carcinoma have their own genomic alterations, but these are separate neoplastic entities.)

---

## 5. Environmental Information

**Environmental / mechanical factors.** The dominant non-genetic contributors are **obstructive nephrolithiasis** (especially staghorn/struvite calculi) and **chronic urinary obstruction**, which create stasis and a nidus for persistent infection.

**Lifestyle / clinical factors.** Recurrent/neglected UTIs, low fluid intake, infrequent voiding, diabetes, and limited healthcare access (delaying stone/UTI treatment) contribute in reported cases.

**Infectious agents.** XGP is driven by chronic bacterial super-infection. The predominant organisms are **_Escherichia coli_** and **_Proteus mirabilis_**, with occasional _Pseudomonas_ and _Providencia stuartii_.

| Organism | Evidence | NCBI Taxon |
|---|---|---|
| *Escherichia coli* | 14.8% of a 27-case series; leading organism in reviews [PMID: 33827527](https://pubmed.ncbi.nlm.nih.gov/33827527/); [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/) | 562 |
| *Proteus mirabilis* (urease-producing) | 18.5% of the same series [PMID: 33827527](https://pubmed.ncbi.nlm.nih.gov/33827527/); [PMID: 34715795](https://pubmed.ncbi.nlm.nih.gov/34715795/) | 584 |
| *Pseudomonas* spp. | occasional [PMID: 34715795](https://pubmed.ncbi.nlm.nih.gov/34715795/) | 286 |
| *Providencia stuartii* | rare, case report [PMID: 34715795](https://pubmed.ncbi.nlm.nih.gov/34715795/) | 588 |

**Direct evidence.** "Urine cultures most often reveal Escherichia coli and Proteus mirabilis" [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/); and XGP is "most commonly associated with super-infections by bacteria such as E. coli, Proteus mirabilis, and occasionally Pseudomonas species" [PMID: 34715795](https://pubmed.ncbi.nlm.nih.gov/34715795/). Importantly, **kidney (upper-tract) urine culture is far more often positive (81.9%) than bladder urine culture (53.2%)** in the same patients, underscoring that the infection is compartmentalized in the obstructed kidney [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/).

The urease activity of *Proteus mirabilis* is mechanistically relevant: it alkalinizes urine and promotes struvite (magnesium ammonium phosphate) stone formation, reinforcing the obstruction–infection loop.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Chronic urinary tract obstruction** (usually a staghorn/struvite calculus, less often stricture or tumor) → **leads to** urinary stasis and increased intrarenal pressure.
2. Stasis → **promotes** persistent bacterial colonization/infection, chiefly by *E. coli* and urease-producing *Proteus mirabilis* (which further drives struvite stone growth, reinforcing obstruction — a feed-forward branch).
3. Chronic infection → **triggers** a suppurative then granulomatous inflammatory response with recruitment of neutrophils, lymphocytes, plasma cells, and macrophages.
4. **Incomplete bacterial degradation and an altered/aberrant host immune response** → **results in** persistence of bacterial and lipid debris within macrophages (*inferred from ultrastructural data*: bacteria seen within PMNs and vacuoles, histiocytes laden with lipid droplets and phagolysosomes) [PMID: 7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/).
5. Defective macrophage lipid clearance → **leads to** accumulation of lipid within histiocytes, forming characteristic **CD68+ lipid-laden "foam cells" (xanthoma cells)** [PMID: 7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/); [PMID: 42288880](https://pubmed.ncbi.nlm.nih.gov/42288880/).
6. Progressive foam-cell accumulation with granulomatous inflammation and multinucleated giant cells → **causes** replacement and destruction of renal parenchyma, with fibrosis [PMID: 42110084](https://pubmed.ncbi.nlm.nih.gov/42110084/); [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/).
7. Parenchymal destruction → **produces** an enlarged, non-functioning kidney (clinical XGP).
8. **Branch (local invasion):** transmural inflammation → **extends** into perinephric fat and adjacent structures → psoas abscess, perinephric abscess, and fistulae (nephrocutaneous, renocolic, and rarely transdiaphragmatic to lung) [PMID: 36105829](https://pubmed.ncbi.nlm.nih.gov/36105829/); [PMID: 29480882](https://pubmed.ncbi.nlm.nih.gov/29480882/).

### Ultrastructural / histologic architecture

An ultrastructural study of 5 cases demonstrated **stratified xanthogranulomas**: a central purulent zone containing bacteria within PMNs and vacuoles, surrounded by a layer of lipid-droplet-laden histiocytes (foam cells) with phagolysosomes, then macrophages, lymphocytes, plasma cells, and peripheral fibroblasts [PMID: 7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/). "Our study suggests that xanthogranulomatous pyelonephritis is a bacteria induced process. Its histological appearance may be related to incomplete bacterial degradation and altered host response." The same study documented that "histiocytes predominated, and their cytoplasm contained numerous lipid droplets with and without limiting membranes and phagolysosomes."

### Categories mapped to the chain

- **Cellular processes:** chronic granulomatous inflammation, macrophage activation (GO:0042116), phagocytosis (GO:0006909), foam cell differentiation (GO:0090077), fibrosis.
- **Immune involvement:** an **incomplete/aberrant immune response** is central—chronic inflammation rather than autoimmunity or classical immunodeficiency [PMID: 34522121](https://pubmed.ncbi.nlm.nih.gov/34522121/); [PMID: 39185472](https://pubmed.ncbi.nlm.nih.gov/39185472/).
- **Protein/biochemical:** macrophage lipid handling defect leading to intracellular lipid droplet accumulation (foam-cell formation); *Proteus* urease-driven urinary alkalinization and struvite lithogenesis.
- **Tissue-damage mechanisms:** suppuration/abscess, granulomatous destruction, fibrosis, and progressive loss of functional nephrons.
- **Metabolic:** local lipid accumulation within histiocytes; no systemic metabolic defect.

### Suggested ontology terms
- **GO (biological process):** inflammatory response (GO:0006954), macrophage activation involved in immune response (GO:0002281), foam cell differentiation (GO:0090077), response to bacterium (GO:0009617).
- **Cell types (CL):** macrophage (CL:0000235), foam cell (CL:0000891), neutrophil (CL:0000775), plasma cell (CL:0000786), lymphocyte (CL:0000542), macrophage giant cell.
- **CHEBI:** cholesterol / lipid (CHEBI:16113), struvite (magnesium ammonium phosphate).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary organ:** kidney (UBERON:0002113), specifically the renal parenchyma and pelvicalyceal system. Involvement is **usually unilateral** and produces an enlarged, non-functioning kidney. Both kidneys are affected at roughly equal frequency (right 45.5%, left 54.5% in one series) [PMID: 41250779](https://pubmed.ncbi.nlm.nih.gov/41250779/).
- **Secondary / adjacent involvement:** perinephric fat, psoas muscle (UBERON:0001096), colon (renocolic fistula), skin (nephrocutaneous fistula), and rarely the diaphragm/lung (transdiaphragmatic extension with lung abscess) [PMID: 36105829](https://pubmed.ncbi.nlm.nih.gov/36105829/); [PMID: 34277481](https://pubmed.ncbi.nlm.nih.gov/34277481/); [PMID: 37171318](https://pubmed.ncbi.nlm.nih.gov/37171318/).
- **Body systems:** urinary/renal system primarily; secondary involvement of the musculoskeletal, gastrointestinal, integumentary, and respiratory systems via local extension; systemic (sepsis in ~13% of a large series) [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/).

**Tissue and cell level.** Renal parenchyma (tubulointerstitium) is destroyed and replaced by sheets of foamy histiocytes with granulomatous inflammation. Key cell populations: **CD68+ lipid-laden macrophages/foam cells** (CL:0000891), neutrophils, lymphocytes, plasma cells, and multinucleated giant cells [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/); [PMID: 42288880](https://pubmed.ncbi.nlm.nih.gov/42288880/).

**Subcellular level.** Lipid droplets and **phagolysosomes** within histiocyte cytoplasm are the ultrastructural hallmark; bacteria persist within phagocytic vacuoles [PMID: 7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/). Relevant GO cellular components: lysosome (GO:0005764), phagocytic vesicle (GO:0045335), lipid droplet (GO:0005811).

**Localization / lateralization.** Predominantly **unilateral**; may be **diffuse** (whole kidney) or **focal/segmental** (a portion of the kidney, more common in children). Bilateral or horseshoe-kidney involvement is rare but a strong predictor of adverse outcome [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/).

---

## 8. Temporal Development

**Onset.** Chronic and typically **insidious**; symptoms (flank pain, low-grade fever, recurrent UTI) may be attributed to nephrolithiasis or simple UTI, delaying diagnosis (median diagnostic delay ~365 days) [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/); [PMID: 36473546](https://pubmed.ncbi.nlm.nih.gov/36473546/). Age of onset is most often adult but ranges from neonate to elderly [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/).

**Progression.** The disease is **progressive** with ongoing parenchymal destruction if untreated. Two anatomic patterns are recognized: **focal/segmental** (earlier, more amenable to kidney-sparing therapy) and **diffuse** (advanced, usually requiring nephrectomy). Advanced disease can become fulminant with sepsis, abscess, and fistula formation.

**Duration and course.** Without definitive treatment the course is chronic and typically culminates in a non-functioning kidney and/or invasive complications; with nephrectomy the disease is essentially **cured** (it does not recur in the removed kidney).

**Critical periods / windows for intervention.** Early recognition—prompted by awareness of risk factors (stones, recurrent UTI)—allows nephron-sparing strategies and prevents late-stage complications [PMID: 36473546](https://pubmed.ncbi.nlm.nih.gov/36473546/). Once diffuse destruction or invasive complications occur, nephrectomy becomes both necessary and technically more difficult.

---

## 9. Inheritance and Population

**Inheritance.** None—XGP is **acquired and non-heritable**. There is no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency to report.

**Epidemiology.** XGP is **rare**; no reliable population incidence/prevalence rates exist. It is estimated to account for a small percentage of chronic pyelonephritis/nephrectomy specimens. In surgical series of poorly/non-functioning kidneys, XGP represented ~14% of nephrectomy histopathology in one large audit [PMID: 39558456](https://pubmed.ncbi.nlm.nih.gov/39558456/).

**Demographics.**
- **Sex:** female predominance—62.5% women in a 365-patient multicenter series [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/); 57.4% in a 251-patient pooled analysis [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/); 71.9% in a 57-patient series [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/).
- **Age:** middle-aged adults predominate—mean age 45 ± 14.4 years [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/); 36.1 years in the pooled cohort [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/); range newborn to elderly.
- **Geographic distribution:** worldwide, with substantial case literature from South Asia, the Middle East, and tropical regions where stone disease and delayed presentation are common [PMID: 41250779](https://pubmed.ncbi.nlm.nih.gov/41250779/); [PMID: 42136792](https://pubmed.ncbi.nlm.nih.gov/42136792/).

---

## 10. Diagnostics

**Definitive diagnosis is histopathologic** and often requires immunohistochemistry, because XGP overlaps clinically and radiologically with RCC, renal tuberculosis, and pyonephrosis [PMID: 41250779](https://pubmed.ncbi.nlm.nih.gov/41250779/).

**Laboratory tests.** Anemia (78.9%), leukocytosis with left shift, elevated inflammatory markers; urinalysis shows pyuria/leukocyturia (93.2%), hematuria (75.6%), and bacteriuria (40.9%) [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/). **Urine culture** most often grows *E. coli* or *Proteus mirabilis*; note that **upper-tract (kidney) cultures are positive far more often (81.9%) than bladder cultures (53.2%)** [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/).

**Imaging.** **CT is the mainstay**. Classic features: an enlarged non-functioning kidney with a central **staghorn calculus**, hydronephrosis, and multiple low-attenuation areas (dilated calyces/abscess cavities) producing the **"bear paw" sign** [PMID: 34522121](https://pubmed.ncbi.nlm.nih.gov/34522121/); [PMID: 41323310](https://pubmed.ncbi.nlm.nih.gov/41323310/). CT also stages perinephric/psoas extension and fistulae. Imaging cannot reliably exclude malignancy (RCC/urothelial/squamous carcinoma can mimic the bear-paw appearance) [PMID: 42558360](https://pubmed.ncbi.nlm.nih.gov/42558360/).

**Biopsy / pathology.** Histology reveals **sheets of foamy histiocytes** with multinucleated giant cells, neutrophils, lymphocytes, plasma cells, and fibrosis, replacing parenchyma [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/); [PMID: 41250779](https://pubmed.ncbi.nlm.nih.gov/41250779/); [PMID: 42110084](https://pubmed.ncbi.nlm.nih.gov/42110084/). "The characteristic pathological finding is the presence of foam cells" [PMID: 3750578](https://pubmed.ncbi.nlm.nih.gov/3750578/).

**Immunohistochemistry.** **CD68** confirms the macrophage/histiocyte lineage of the foam cells [PMID: 42288880](https://pubmed.ncbi.nlm.nih.gov/42288880/). IHC is often **decisive** in distinguishing XGP from RCC: "The misinterpretation of 'foam cells' as 'clear cells' consistent with RCC is the most important diagnostic challenge for pathologists," and "The immunohistochemistry was the decisive factor in confirming the diagnosis of XGPN" [PMID: 37113900](https://pubmed.ncbi.nlm.nih.gov/37113900/).

**Genetic / omics diagnostics.** Not applicable—no genetic test, panel, karyotype, or omics assay is used to diagnose XGP.

**Differential diagnosis.** Clear-cell/papillary/sarcomatoid RCC, squamous cell carcinoma and urothelial carcinoma of the renal pelvis, renal tuberculosis, pyonephrosis, malakoplakia, megalocytic interstitial nephritis, and leiomyosarcoma [PMID: 21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/). Red flags favoring malignancy include culture-negative, antibiotic-refractory disease with an irregular enhancing solid component and vascular involvement [PMID: 42558360](https://pubmed.ncbi.nlm.nih.gov/42558360/).

---

## 11. Outcome / Prognosis

**Overall prognosis.** XGP is **curable with nephrectomy** but carries **high perioperative morbidity**. In a pooled analysis of 251 patients, the adverse composite outcome occurred in 15.5% and any complication in 51.0% [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/). A dedicated nephrectomy series reported that "a postoperative complication occurred in 73% (n = 8), with 50% (n = 4) of complications Clavien Dindo grade 3 or higher, including one patient mortality" [PMID: 37610600](https://pubmed.ncbi.nlm.nih.gov/37610600/). Mortality overall is low (three deaths among 365 patients in a multicenter series) but real, driven by sepsis and advanced disease [PMID: 37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/).

**Prognostic factors (adjusted odds ratios, pooled n=251)** [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/):

| Predictor | Outcome | OR (95% CI) | p |
|---|---|---|---|
| Bilateral / horseshoe kidney | Adverse composite | 3.86 (1.01–14.73) | 0.048 |
| Dialysis required | Adverse composite | 8.64 (2.27–32.94) | 0.002 |
| Staged nephrostomy → nephrectomy | Adverse composite | 4.57 (1.58–13.17) | 0.01 |
| Fever | Any complication | 3.04 (1.63–5.67) | <0.001 |
| Renal stones | Any complication | 2.55 (1.35–4.81) | 0.004 |

Additionally, **fever and perinephric inflammatory changes (PIC) on CT predicted poor outcomes** in an independent series [PMID: 36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/).

**Morbidity / complications.** "The most frequent ones are Psoas abscess, perinephric abscess, and sepsis. Nephrocutaneous and renocolic fistulas are less common" [PMID: 36105829](https://pubmed.ncbi.nlm.nih.gov/36105829/). XGP "can lead to fatal complications, including perinephric inflammation, psoas abscess, and cutaneous fistula" [PMID: 29480882](https://pubmed.ncbi.nlm.nih.gov/29480882/). Emphysematous pyelonephritis can co-occur [PMID: 41323310](https://pubmed.ncbi.nlm.nih.gov/41323310/).

**Pediatric / focal disease** has a favorable prognosis: "Conservative management with antibiotics, with or without drainage, succeeded in 64% of cases, and overall outcomes were favorable, with stable renal function and no reported mortality" [PMID: 41341186](https://pubmed.ncbi.nlm.nih.gov/41341186/).

---

## 12. Treatment

**Overarching strategy.** Culture-guided **antibiotics** plus **source control**. Definitive treatment is stratified by disease extent and patient age.

**Nephrectomy (definitive, adult diffuse disease).** "Although some cases in children have been successfully treated with antibiotics alone, nephrectomy remains the most common treatment for XGP in adults" [PMID: 34522121](https://pubmed.ncbi.nlm.nih.gov/34522121/). Laparoscopic nephrectomy is increasingly used and feasible/safe in experienced centers [PMID: 42136792](https://pubmed.ncbi.nlm.nih.gov/42136792/), though XGP raises operative difficulty (adhesions, perinephric inflammation), longer operative times, longer hospital stay, and higher conversion-to-open and complication rates [PMID: 39558456](https://pubmed.ncbi.nlm.nih.gov/39558456/); [PMID: 40063351](https://pubmed.ncbi.nlm.nih.gov/40063351/). *Suggested NCIT:* Nephrectomy (C15288); Laparoscopic Nephrectomy.

**Kidney-sparing / conservative management (pediatric and focal disease).** Antibiotics with or without drainage succeeded in **64%** of pediatric cases with favorable outcomes and no mortality [PMID: 41341186](https://pubmed.ncbi.nlm.nih.gov/41341186/). Partial nephrectomy / heminephrectomy is an option for focal disease [PMID: 42110084](https://pubmed.ncbi.nlm.nih.gov/42110084/); [PMID: 6810046](https://pubmed.ncbi.nlm.nih.gov/6810046/). *Suggested NCIT:* Antibiotic Therapy (C15352); Partial Nephrectomy (C51716).

**Interventional / supportive.** **Percutaneous nephrostomy** for drainage/decompression and staged control of sepsis before definitive surgery [PMID: 34522121](https://pubmed.ncbi.nlm.nih.gov/34522121/); [PMID: 42281681](https://pubmed.ncbi.nlm.nih.gov/42281681/). Note, however, that a staged nephrostomy-then-nephrectomy course is itself associated with worse composite outcomes—likely a marker of more severe disease [PMID: 39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/). Supportive care includes sepsis management, correction of anemia, and treatment of comorbidities. *Suggested NCIT:* Percutaneous Nephrostomy.

**Pharmacogenomics / advanced therapeutics.** Not applicable—no gene, cell, RNA, targeted, or immunotherapy is used. Antibiotic selection is guided by urine culture and local resistance profiles [PMID: 33827527](https://pubmed.ncbi.nlm.nih.gov/33827527/).

**Treatment algorithm (synthesis).**
```
Suspected XGP (flank pain + fever + recurrent UTI + staghorn calculus)
        │
        ├─ Resuscitate; culture-guided antibiotics; CT staging
        │
        ├─ Diffuse disease (adult) ─────────► Nephrectomy (laparoscopic/open)
        │                                     ± preop nephrostomy if septic
        │
        ├─ Focal disease / pediatric ───────► Antibiotics ± drainage
        │                                     (partial nephrectomy if fails)
        │
        └─ Culture-negative, antibiotic-refractory, solid enhancing mass,
           vascular invasion ───────────────► Suspect malignancy → tissue Dx / surgery
```

---

## 13. Prevention

**Primary prevention.** Prevent and treat the upstream causes: effective management of **nephrolithiasis** (stone clearance, metabolic stone prevention), relief of **urinary obstruction**, and prompt, complete treatment of **UTIs**. Improving healthcare access reduces the neglected-stone pathway to advanced XGP [PMID: 41159347](https://pubmed.ncbi.nlm.nih.gov/41159347/).

**Secondary prevention.** Early recognition through awareness of risk factors and early imaging in patients with recurrent UTI plus stones can enable nephron-sparing strategies and prevent late complications [PMID: 36473546](https://pubmed.ncbi.nlm.nih.gov/36473546/).

**Tertiary prevention.** In established disease, timely source control (drainage/nephrectomy) prevents sepsis, abscess, and fistula formation.

**Immunization / genetic screening / counseling.** Not applicable—no vaccine and no heritable component.

---

## 14. Other Species / Natural Disease

XGP occurs naturally in non-human species. The **first documented canine case** was reported in a 6-year-old Pomeranian with an enlarged right kidney and hypoattenuating areas on CT, treated by radical nephrectomy; histology showed parenchymal destruction, abscess, and "infiltration of CD68 + vacuolated macrophages" [PMID: 42288880](https://pubmed.ncbi.nlm.nih.gov/42288880/). "This is the first documented case of XGP in a dog."

- **Taxonomy:** *Homo sapiens* (NCBI:txid9606); *Canis lupus familiaris* (NCBI:txid9615).
- **Comparative pathology:** The canine lesion recapitulates the human disease—parenchymal destruction, abscess formation, and CD68+ foam-cell infiltration—supporting conserved macrophage-driven pathophysiology.
- **Zoonosis:** XGP is **not** transmissible/zoonotic; it is a host response to obstruction+infection, not a communicable disease. The causative bacteria (*E. coli*, *Proteus*) are ubiquitous commensals/uropathogens, not species-jumping agents in this context.

---

## 15. Model Organisms

There is **no established, purpose-built animal or in vitro model** of XGP. Knowledge derives from human clinical/pathologic material and the single naturally occurring canine case [PMID: 42288880](https://pubmed.ncbi.nlm.nih.gov/42288880/). Historically, experimental partial nephrectomy work was performed in dogs for surgical technique development (not to model XGP biology) [PMID: 6810046](https://pubmed.ncbi.nlm.nih.gov/6810046/).

- **Model types:** none validated (no mouse/rat/zebrafish/organoid model of XGP).
- **Phenotype recapitulation:** the naturally occurring canine case reproduces core features (parenchymal destruction, foam cells, CD68 positivity).
- **Limitations / opportunity:** the lack of a tractable model is a significant knowledge gap. A candidate induced model would combine ureteral obstruction with chronic *Proteus mirabilis*/*E. coli* infection in a rodent to test whether foam-cell granulomas form and to dissect the macrophage lipid-handling defect.

---

## Mechanistic Model / Interpretation

XGP is best understood as a **macrophage-centered end-stage response to a self-reinforcing obstruction–infection loop** in a kidney whose immune clearance is incomplete.

```
  Staghorn/struvite calculus ──► OBSTRUCTION ──► stasis + ↑pressure
            ▲                                          │
            │ (Proteus urease → struvite)              ▼
   Urease+ Proteus / E. coli ◄──── CHRONIC INFECTION ──► suppuration
            │                                          │
            ▼                                          ▼
   INCOMPLETE bacterial degradation +        neutrophil→macrophage recruitment
   defective macrophage lipid clearance ────► LIPID-LADEN CD68+ FOAM CELLS
                                                      │
                                                      ▼
                            GRANULOMATOUS PARENCHYMAL DESTRUCTION + fibrosis
                                                      │
                        ┌─────────────────────────────┼─────────────────────────┐
                        ▼                              ▼                         ▼
              Non-functioning kidney        Local invasion (psoas,      Mimics/rarely
              (enlarged, "bear paw")        perinephric, fistulae,      coexists with
                                            lung)                       RCC/SCC/urothelial CA
```

**Upstream vs downstream.** The obstruction–infection loop (with *Proteus* urease closing the loop via struvite lithogenesis) is upstream; the macrophage lipid-handling defect and foam-cell granuloma are the central transducing lesion; parenchymal destruction, non-function, local invasion, and malignancy mimicry are downstream. The **incomplete immune response** is the pivotal host factor that converts ordinary chronic pyelonephritis into the xanthogranulomatous phenotype.

**Clinical corollaries that fall out of the model.** (1) Upper-tract cultures outperform bladder cultures because the infection is sequestered behind obstruction. (2) Fever and perinephric inflammatory change mark more aggressive host–pathogen interaction and predict worse outcomes. (3) Because the lesion is macrophage/foam-cell rather than epithelial, CD68 IHC resolves the RCC differential. (4) Removing the diseased kidney is curative because it excises the entire self-reinforcing loop.

---

## Evidence Base

| PMID | Type | Contribution |
|---|---|---|
| [21526966](https://pubmed.ncbi.nlm.nih.gov/21526966/) | Review | Definition, female predominance, organisms, histologic infiltrate, differential Dx |
| [34522121](https://pubmed.ncbi.nlm.nih.gov/34522121/) | Narrative review | Etiologic triad, "great imitator," imaging, adult nephrectomy vs pediatric antibiotics |
| [7076194](https://pubmed.ncbi.nlm.nih.gov/7076194/) | Ultrastructural study (n=5) | Bacteria-induced process; incomplete degradation; foam-cell/phagolysosome architecture |
| [37242365](https://pubmed.ncbi.nlm.nih.gov/37242365/) | Multicenter series (n=365) | Demographics, CKD comorbidity, kidney vs bladder culture positivity, sepsis, mortality |
| [39254583](https://pubmed.ncbi.nlm.nih.gov/39254583/) | Pooled analysis (n=251) | Symptom frequencies; adjusted ORs for adverse outcomes and complications |
| [36505992](https://pubmed.ncbi.nlm.nih.gov/36505992/) | Case series (n=57) | Quantitative symptom/lab profile; fever+PIC predict poor outcome; diagnostic delay |
| [33827527](https://pubmed.ncbi.nlm.nih.gov/33827527/) | Microbiology series (n=27) | Organism frequencies (Proteus 18.5%, E. coli 14.8%) and resistance |
| [37610600](https://pubmed.ncbi.nlm.nih.gov/37610600/) | Surgical series | 73% postoperative complications, 50% Clavien-Dindo ≥3, one death |
| [41341186](https://pubmed.ncbi.nlm.nih.gov/41341186/) | Pediatric review (n=34) | 53% focal; conservative management success 64%, no mortality |
| [42288880](https://pubmed.ncbi.nlm.nih.gov/42288880/) | Veterinary case report | First canine XGP; CD68+ foam cells confirm macrophage lineage |
| [37113900](https://pubmed.ncbi.nlm.nih.gov/37113900/) | Case report | IHC decisive vs RCC; "foam cells" vs "clear cells" pitfall |
| [42110084](https://pubmed.ncbi.nlm.nih.gov/42110084/) | Pediatric surgical report | Histology: parenchymal loss replaced by lipid-laden macrophages + fibrosis |
| [3750578](https://pubmed.ncbi.nlm.nih.gov/3750578/) | Review + cases | Foam cells as characteristic pathologic finding |
| [36105829](https://pubmed.ncbi.nlm.nih.gov/36105829/) | Case report/review | Complication frequencies; urothelial CA mimicry + renocolic fistula |
| [29480882](https://pubmed.ncbi.nlm.nih.gov/29480882/) | Case report | Range of local invasive complications incl. cutaneous fistula |
| [33521318](https://pubmed.ncbi.nlm.nih.gov/33521318/), [21119270](https://pubmed.ncbi.nlm.nih.gov/21119270/), [26816904](https://pubmed.ncbi.nlm.nih.gov/26816904/), [21915390](https://pubmed.ncbi.nlm.nih.gov/21915390/) | Case reports | Rare coexistence with SCC/collision tumors; urolithiasis–malignancy link |
| [42558360](https://pubmed.ncbi.nlm.nih.gov/42558360/) | Case report | Malignancy red flags distinguishing sarcomatoid RCC from XGP |
| [41250779](https://pubmed.ncbi.nlm.nih.gov/41250779/) | Case series (n=55) | Clinicopathologic spectrum; histology confirms diagnosis post-nephrectomy |

**Consistency / conflict assessment.** Findings are highly consistent across independent series regarding female predominance, the obstruction+infection+immune triad, *E. coli*/*Proteus* dominance, foam-cell histology, and nephrectomy-based management. The main nuance is treatment: adult diffuse disease → nephrectomy; pediatric/focal disease → conservative therapy often succeeds—these are complementary, not conflicting. No source contradicts the core mechanistic model.

---

## Limitations and Knowledge Gaps

1. **Evidence hierarchy.** The literature is dominated by retrospective series and case reports; there are **no randomized trials** and no prospective natural-history cohorts. Effect estimates (e.g., outcome ORs) derive from pooled published cases and may carry publication bias.
2. **No molecular/omics data.** There are no transcriptomic, proteomic, metabolomic, single-cell, or epigenomic studies specific to XGP. The proposed **macrophage lipid-handling defect** is inferred from ultrastructure, not demonstrated mechanistically (e.g., no identified lipid-transport or efferocytosis lesion).
3. **No genetic dimension.** Host-susceptibility factors (why some obstructed/infected kidneys become xanthogranulomatous and others do not) are unknown; no GWAS or immunogenetic studies exist.
4. **No validated experimental model.** Absence of a tractable animal/organoid model limits mechanistic dissection and therapeutic innovation.
5. **Epidemiology is imprecise.** True incidence/prevalence are unknown; frequencies come from surgical/nephrectomy denominators that overrepresent severe disease.
6. **Malignancy coexistence is under-quantified.** The true rate of concurrent carcinoma is unknown; reliance on case reports risks both over- and under-estimation.

---

## Proposed Follow-up Experiments / Actions

1. **Single-cell / spatial transcriptomics of XGP nephrectomy specimens** vs control chronic pyelonephritis and RCC—define the foam-cell macrophage state (CD68+ subpopulations), test for a specific lipid-handling/efferocytosis signature (e.g., ABCA1, TREM2, APOE, SCARB1), and map the stratified granuloma spatially. *(Resolves the inferred "defective lipid clearance" step.)*
2. **Immunophenotyping of the "incomplete immune response"**—multiplex IHC/flow for macrophage polarization (M1/M2), T-cell subsets, and cytokine milieu to characterize why bacterial clearance is incomplete.
3. **Develop an induced rodent model:** unilateral ureteral obstruction + chronic *Proteus mirabilis* or *E. coli* infection, with readouts for foam-cell granuloma formation; use it to test whether modulating macrophage lipid metabolism prevents xanthogranulomatous transformation.
4. **Prospective multicenter registry** with standardized imaging (CT staging including "bear paw" and perinephric inflammatory change) and outcomes to validate the prognostic ORs (bilateral/horseshoe kidney, dialysis, fever, stones) and refine risk stratification.
5. **Diagnostic-accuracy study of a minimal IHC panel (CD68 ± PAX8/CAIX/RCC markers)** on percutaneous renal mass biopsies to reduce nondiagnostic/false-negative biopsies and pre-operatively separate XGP from RCC, potentially avoiding unnecessary radical surgery.
6. **Systematic review/meta-analysis of laparoscopic vs open nephrectomy** in XGP to quantify conversion rates, complications, and predictors, informing surgical planning.
7. **Antimicrobial stewardship substudy** correlating upper-tract vs bladder culture results and resistance profiles with outcomes, to optimize perioperative antibiotic selection.

---

*Report compiled from 11 confirmed findings and 42 reviewed papers. Evidence source types: predominantly human clinical (multicenter/pooled series, case series, case reports), one veterinary (naturally occurring canine case), and one ultrastructural/in-situ pathology study; no computational or purpose-built model-organism data available for XGP.*


## Artifacts

- [OpenScientist final report](Xanthogranulomatous_Pyelonephritis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Xanthogranulomatous_Pyelonephritis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 33 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007022` (3 mentions) - the report calls it "if available"; MONDO calls it **xanthogranulomatous pyelonephritis**
- `HP:0025427` (1 mention) - the report calls it "Bacteriuria"; HP calls it **Abnormal bronchus physiology**
- `GO:0042116` (1 mention) - the report calls it "Cellular processes:** chronic granulomatous inflammation, macrophage activation"; GO calls it **macrophage activation**
- `CL:0000891` (2 mentions) - the report calls it "CD68+ lipid-laden macrophages/foam cells"; CL calls it **foam cell**
- `UBERON:0001096` (1 mention) - the report calls it "Secondary / adjacent involvement:** perinephric fat, psoas muscle"; UBERON calls it **wall of esophagus**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0031183` (1 mention), reported as "Abdominal mass" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `HP:0000787` (1 mention) - the report calls it "Nephrolithiasis"; HP calls it **Kidney stone**, and lists "Nephrolithiasis" among its other names
- `CHEBI:16113` (1 mention) - the report calls it "CHEBI:** cholesterol / lipid"; CHEBI calls it **cholesterol**
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
