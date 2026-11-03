---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T20:38:59.533377'
end_time: '2026-09-29T20:54:30.310057'
duration_seconds: 930.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Meningeal tuberculosis
  mondo_id: MONDO:0006042
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
citation_count: 34
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 27
  quotes_valid: 25
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:41629635
  - PMID:39752122
  relevance_assessed: 35
  on_topic: 15
  off_topic: 1
  off_topic_references:
  - PMID:35673608
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0006042
    reported_labels:
    - MONDO
    ontology_label: meningeal tuberculosis
  - term_id: HP:0002013
    reported_labels:
    - "~52\u201392% (children higher)"
    ontology_label: Vomiting
  - term_id: HP:0001250
    reported_labels:
    - ~72% (children)
    ontology_label: Seizure
  - term_id: HP:0001269
    reported_labels:
    - ~30% (stroke)
    ontology_label: Hemiparesis
  - term_id: HP:0000238
    reported_labels:
    - "26\u201363% imaging"
    ontology_label: Hydrocephalus
  - term_id: HP:0100543
    reported_labels:
    - "12\u2013>90% survivors"
    ontology_label: Cognitive impairment
  - term_id: HP:0012229
    reported_labels:
    - abnormal CSF
    ontology_label: CSF pleocytosis
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Meningeal_Tuberculosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Meningeal_Tuberculosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Meningeal tuberculosis
- **MONDO ID:** MONDO:0006042 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Meningeal tuberculosis** covering all of the
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

# Meningeal Tuberculosis (Tuberculous Meningitis) — Comprehensive Disease Characterization Report

**Target Disease:** Meningeal tuberculosis / Tuberculous meningitis (TBM)
**MONDO ID:** MONDO:0006042
**Category:** Infectious Disease
**Report basis:** 15 confirmed findings, 68 papers reviewed across 5 investigation iterations

---

## Summary

Meningeal tuberculosis (tuberculous meningitis, TBM) is the most lethal and disabling form of tuberculosis, arising when *Mycobacterium tuberculosis* infects the meninges and subarachnoid space of the central nervous system. It is fundamentally an **infectious disease with a strong immunopathological component**: the initiating lesion is a subpial or subependymal caseous granuloma (the **Rich focus**) that ruptures into the subarachnoid space, seeding a dense basal meningeal exudate. This exudate drives the three cardinal complications that define the disease's morbidity and mortality — **vasculitis with cerebral infarction, hydrocephalus, and cranial neuropathy** — together with blood-brain-barrier (BBB) breakdown mediated by matrix metalloproteinase-9 (MMP-9) ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/); [PMID: 19789647](https://pubmed.ncbi.nlm.nih.gov/19789647/)).

TBM accounts for roughly 1% of all active TB cases (1–5% of TB, ~14% of all meningitis) but carries an in-hospital mortality near 42%, rising toward 70% in HIV co-infection, and left ~78,200 adults dead in 2019 alone ([PMID: 35288778](https://pubmed.ncbi.nlm.nih.gov/35288778/); [PMID: 36795648](https://pubmed.ncbi.nlm.nih.gov/36795648/)). Survivors frequently suffer multidomain cognitive impairment and focal neurological deficits. Diagnosis remains a central challenge because no single test is both sensitive and specific: clinicians rely on a composite of CSF findings (lymphocytic pleocytosis, elevated protein, low glucose, elevated adenosine deaminase), molecular testing (Xpert MTB/RIF Ultra, ~77% sensitive), and the neuroimaging triad of basal meningeal enhancement, hydrocephalus, and basal-ganglia infarction ([PMID: 31924549](https://pubmed.ncbi.nlm.nih.gov/31924549/); [PMID: 28281443](https://pubmed.ncbi.nlm.nih.gov/28281443/)).

Treatment is prolonged multidrug antituberculous therapy — the WHO-standard 12-month HRZE-based regimen (2HRZE/10HR) — because standard 6-month pulmonary regimens penetrate the CNS poorly. Adjunctive corticosteroids are standard, but their survival benefit is now understood to be **host-genotype-dependent**: leukotriene A4 hydrolase (*LTA4H*) promoter genotype defines hyper-, intermediate-, and low-inflammatory phenotypes, and the phase 3 LAST ACT trial found no dexamethasone benefit in the CC/CT (lower-inflammation) genotypes ([PMID: 41540106](https://pubmed.ncbi.nlm.nih.gov/41540106/)). Prevention rests principally on neonatal BCG vaccination, which is ~90% protective against the meningeal and miliary childhood forms ([PMID: 24336911](https://pubmed.ncbi.nlm.nih.gov/24336911/)).

---

## 1. Disease Information

**Overview.** TBM is a subacute-to-chronic granulomatous meningitis caused by *Mycobacterium tuberculosis* reaching the CNS, usually via hematogenous dissemination from a primary (typically pulmonary) focus. It is the most severe manifestation of extrapulmonary TB. Untreated, it "presents as a subacute to chronic meningitis syndrome with a prodrome of malaise, fever, and headache progressing to altered mentation and focal neurologic signs, followed by stupor, coma, and death within five to eight weeks of onset" ([PMID: 28281443](https://pubmed.ncbi.nlm.nih.gov/28281443/)).

**Key identifiers:**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0006042 |
| MeSH | Tuberculosis, Meningeal (D014390) |
| ICD-10 | A17.0 (Tuberculous meningitis) |
| ICD-11 | 1B41 (Tuberculosis of the nervous system) |
| SNOMED CT | Tuberculous meningitis (disorder) |

**Synonyms / alternative names:** tuberculous meningitis, TB meningitis, TBM, meningeal tuberculosis, tuberculosis of the meninges, CNS tuberculosis (broader — includes tuberculoma and spinal arachnoiditis).

**Information source type.** This report aggregates **disease-level** evidence from systematic reviews, meta-analyses, randomized controlled trials, and cohort studies, supplemented by mechanistic model-organism and in-vitro work. It is not derived from individual EHR records.

---

## 2. Etiology

**Primary cause (infectious).** TBM is caused by *Mycobacterium tuberculosis* (NCBI Taxonomy 1773; complex 77643). The mechanistic trigger is the **Rich focus** — a caseating granuloma seeded during bacillemia that lodges subpially/subependymally and later ruptures into the subarachnoid space ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/)).

**Genetic risk factors (host susceptibility).** Susceptibility and severity are shaped by host genetic polymorphisms and by pathogen lineage. "Pathogen lineage (Beijing genotype) and host genetics (polymorphisms in TLR2, TIRAP and LTA4H genes) can influence susceptibility to TBM" ([PMID: 22953709](https://pubmed.ncbi.nlm.nih.gov/22953709/)). The *LTA4H* (leukotriene A4 hydrolase; HGNC:6710) promoter genotype is the best-characterized modifier, defining three intracerebral inflammatory phenotypes: **TT (hyperinflammatory), CT (intermediate), CC (low inflammation)** ([PMID: 41540106](https://pubmed.ncbi.nlm.nih.gov/41540106/)).

**Environmental / demographic risk factors.** HIV co-infection is the dominant risk factor and outcome modifier. Other risks include young age (children <5 years present with more advanced disease), high community TB burden, low Human Development Index, malnutrition, and lack of BCG vaccination ([PMID: 36795648](https://pubmed.ncbi.nlm.nih.gov/36795648/); [PMID: 41639788](https://pubmed.ncbi.nlm.nih.gov/41639788/)).

**Protective factors.** Neonatal BCG vaccination is strongly protective against meningeal/miliary TB (~90%) ([PMID: 24336911](https://pubmed.ncbi.nlm.nih.gov/24336911/)). No robustly validated protective human genetic variant is established for TBM specifically.

**Gene-environment interaction.** The clearest GxE relationship is *LTA4H* genotype × corticosteroid therapy: the anti-inflammatory (steroid) intervention interacts with the host inflammatory set-point, so benefit is expected in the hyperinflammatory TT genotype but is uncertain/absent in CC/CT ([PMID: 41540106](https://pubmed.ncbi.nlm.nih.gov/41540106/); [PMID: 22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/)).

---

## 3. Phenotypes

TBM produces symptoms/signs (clinical), physical manifestations, behavioral/cognitive change, and laboratory abnormalities. Onset is subacute (typically days-to-weeks). Frequencies below are drawn from cohort and review data.

| Phenotype | Type | Frequency / notes | Suggested HPO |
|---|---|---|---|
| Fever | Symptom | ~67–80% | HP:0001945 |
| Headache | Symptom | ~33–63% | HP:0002315 |
| Vomiting / nausea | Symptom | ~52–92% (children higher) | HP:0002013 |
| Altered mental status / consciousness | Sign | ~55–78% | HP:0011446 |
| Meningismus / nuchal rigidity | Sign | ~38% + | HP:0002829 |
| Seizures | Sign | ~72% (children) | HP:0001250 |
| Cranial neuropathy (e.g., optic, oculomotor) | Sign | common (basal exudate entrapment) | HP:0000496 |
| Focal deficit / hemiparesis (stroke) | Sign | ~30% (stroke) | HP:0001269 |
| Hydrocephalus | Manifestation | 26–63% imaging | HP:0000238 |
| Cognitive impairment (memory, attention, executive) | Behavioral/cognitive | 12–>90% survivors | HP:0100543 |
| Lymphocytic CSF pleocytosis | Lab | classic | HP:0012229 (abnormal CSF) |
| Hyponatremia | Lab | ~46–93% | HP:0002902 |

**Characteristics.** Onset spans neonatal through geriatric, with a pediatric predilection for severe meningoencephalitis. Severity is graded by the British Medical Research Council (BMRC) stages I–III. Progression is typically progressive if untreated. Cognitive sequelae "most consistently affected memory, attention, and executive function" ([PMID: 41629635](https://pubmed.ncbi.nlm.nih.gov/41629635/)). Younger children carry a disproportionate burden: "The < 5 years group had a higher proportion of TBM stage III cases (29.5% vs. 2.2%, p <0.001)" ([PMID: 41639788](https://pubmed.ncbi.nlm.nih.gov/41639788/)).

**Quality of life.** Survivors face substantial disability from motor deficits, epilepsy, hydrocephalus-related morbidity, and cognitive dysfunction spanning mild deficits to severe global dysfunction ([PMID: 41629635](https://pubmed.ncbi.nlm.nih.gov/41629635/)).

---

## 4. Genetic / Molecular Information

TBM is **not a Mendelian genetic disease** — there are no causal genes, pathogenic ACMG-classified variants, chromosomal abnormalities, or germline/somatic driver mutations. Host genetics act as **susceptibility/modifier factors**, not as causes:

- ***LTA4H*** (HGNC:6710) — promoter polymorphism defines inflammatory phenotype and modifies corticosteroid response ([PMID: 41540106](https://pubmed.ncbi.nlm.nih.gov/41540106/)).
- ***TLR2*** (Toll-like receptor 2) and ***TIRAP*** (TIR domain adaptor) — susceptibility polymorphisms ([PMID: 22953709](https://pubmed.ncbi.nlm.nih.gov/22953709/)).

**Epigenetic information:** No TBM-specific human epigenomic signature is established in the reviewed literature.

The relevant "molecular" pathology is therefore host-inflammatory rather than genomic. The *LTA4H*-encoded enzyme sits at the eicosanoid branch point governing the balance of pro-inflammatory leukotriene B4 versus anti-inflammatory lipoxins ([PMID: 22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/)).

---

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* (NCBI Taxon 1773); the **Beijing lineage** is associated with increased TBM susceptibility ([PMID: 22953709](https://pubmed.ncbi.nlm.nih.gov/22953709/)). CHEBI-relevant host mediators include leukotriene B4 (CHEBI:15514) and lipoxins.
- **Environmental/lifestyle contributors:** crowding and airborne transmission of TB, malnutrition, immunosuppression (notably HIV), and absence of BCG vaccination. HIV co-infection modifies presentation — persons living with HIV "exhibited lower frequencies of vomiting, nuchal rigidity, signs of meningeal inflammation, and coma, along with lower leukocyte counts in cerebrospinal fluid" ([PMID: 40589807](https://pubmed.ncbi.nlm.nih.gov/40589807/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Inhalation of *M. tuberculosis*** → primary (usually pulmonary) infection → hematogenous dissemination **leads to** seeding of subpial/subependymal caseous granulomas (**Rich foci**). *(Demonstrated — classic neuropathology.)*
2. **Rupture of a Rich focus** into the subarachnoid space **results in** release of bacilli and antigen into CSF ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/)).
3. Antigen release **triggers** a dense **basal meningeal exudate** of mononuclear/epithelioid cells and Langhans giant cells around the basal cisterns ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/)).
4. The exudate **branches** into three parallel injury pathways:
   - **(4a) Vasculitis branch:** exudate encases perforating arteries → arteritis → "arteritic occlusion of larger arteries, such as the middle cerebral" → **infarction**, characteristically in the basal ganglia (lateral striate, MCA, medial striate territory) ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/); [PMID: 36048445](https://pubmed.ncbi.nlm.nih.gov/36048445/)).
   - **(4b) CSF-flow branch:** "Blockage of the basal subarachnoid cisterns ... or narrowing of aqueduct and third ventricle by a small tuberculoma causes consequent **hydrocephalus**" ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/)).
   - **(4c) Cranial-nerve branch:** entrapment of optic nerves and other cranial nerves in the interpeduncular fossa → **cranial neuropathies** ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/)).
5. **In parallel**, neutrophil-driven and macrophage-driven secretion of **MMP-9** (a zinc-dependent gelatinase) **degrades basement membrane/extracellular matrix** → **blood-brain-barrier disruption** and neuroinflammatory injury ([PMID: 19789647](https://pubmed.ncbi.nlm.nih.gov/19789647/); [PMID: 39536643](https://pubmed.ncbi.nlm.nih.gov/39536643/)).
6. Host **inflammatory set-point (LTA4H genotype)** modulates the magnitude of steps 3–5: both inadequate and excessive inflammation converge on **dysregulated TNF**, worsening outcome (*inferred from zebrafish/human correlation*) ([PMID: 22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/)).
7. Combined ischemia, hydrocephalus, BBB breakdown and edema **result in** raised intracranial pressure, coma, and death, or — in survivors — cognitive and focal neurological sequelae ([PMID: 41629635](https://pubmed.ncbi.nlm.nih.gov/41629635/)).

### Detail by category

**Cellular / immune processes.** Granulomatous inflammation (epithelioid macrophages, Langhans giant cells, lymphocytes) is the dominant tissue response ([PMID: 7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/)). Early pathogenesis has a neutrophilic component: "The strong correlation between CSF MMP-9 and neutrophil count suggests that polymorphonuclear leukocytes may play a central role in the early pathogenesis of TBM" ([PMID: 19789647](https://pubmed.ncbi.nlm.nih.gov/19789647/)). Specialized pro-resolving mediators (resolvins, lipoxins) decline with severity, and their CSF concentrations associate with 80-day survival ([PMID: 31500466](https://pubmed.ncbi.nlm.nih.gov/31500466/)).

**Protein dysfunction / biochemical abnormality.** MMP-9 over-activity is central to matrix destruction. In a mouse CNS-TB model, SHH-pathway antagonism "upregulated Matrix Metalloproteinase-9 (MMP-9) secretion, a key contributor to BBB disruption," severe gliosis, and a 99% increase in brain bacillary load ([PMID: 39536643](https://pubmed.ncbi.nlm.nih.gov/39536643/)). Dexamethasone "significantly reduced CSF MMP-9 concentrations in early follow up samples" ([PMID: 19789647](https://pubmed.ncbi.nlm.nih.gov/19789647/)).

**Molecular pathway.** The eicosanoid/LTA4H axis (leukotriene B4 vs lipoxin balance) tunes TNF signaling: "inadequate inflammation caused by excess lipoxins and hyperinflammation driven by excess leukotriene B(4)" both cause susceptibility ([PMID: 22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/)). The sonic hedgehog (SHH) pathway is implicated in BBB integrity ([PMID: 39536643](https://pubmed.ncbi.nlm.nih.gov/39536643/)).

**Suggested ontology terms.** GO: inflammatory response (GO:0006954), extracellular matrix disassembly (GO:0022617), blood-brain barrier maintenance (GO:0035633), leukotriene metabolic process (GO:0006691). CL: macrophage (CL:0000235), epithelioid cell, Langhans giant cell, neutrophil (CL:0000775), T lymphocyte (CL:0000084).

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary organ: **brain and meninges** (nervous system). The basal meninges, subarachnoid cisterns, and CSF pathways are the epicenter. Secondary involvement: cerebral parenchyma (infarcts, tuberculomas, encephalitis), ventricular system (hydrocephalus), cranial nerves, and spinal cord/arachnoid (spinal arachnoiditis). Systemic dissemination (miliary TB) is common in children.

**Vascular territory.** Basal-ganglia perforators are characteristically affected: "The lateral striate, middle cerebral, and medial striate arteries were typically affected" — the perforator "TB zone" encased by exudate ([PMID: 36048445](https://pubmed.ncbi.nlm.nih.gov/36048445/)).

**Tissue / cell level.** Leptomeninges (pia-arachnoid), cerebral arterial walls (arteritis), ependyma, and choroid/aqueductal structures. Cell populations: macrophages, epithelioid and Langhans giant cells, lymphocytes, neutrophils.

**Localization / UBERON:** meninges (UBERON:0002360), leptomeninges/subarachnoid space (UBERON:0002450), basal cistern, brain (UBERON:0000955), cerebrospinal fluid (UBERON:0001359), middle cerebral artery (UBERON:0001627), basal ganglia (UBERON:0002420), cerebral ventricle (UBERON:0002285). Lateralization is typically **bilateral/basal** but infarcts may be focal/asymmetric.

---

## 8. Temporal Development

- **Onset:** any age, with pediatric predilection; onset is **subacute to chronic** (prodrome of days to weeks).
- **Staging:** BMRC grades I (alert, no deficit), II (altered consciousness/focal signs), III (stupor/coma, dense deficit). Advanced stage predicts poor outcome — up to 100% fatality in stage III in one pediatric series ([PMID: 41288109](https://pubmed.ncbi.nlm.nih.gov/41288109/)).
- **Untreated course:** progression from "malaise, fever, and headache progressing to altered mentation and focal neurologic signs, followed by stupor, coma, and death within five to eight weeks of onset" ([PMID: 28281443](https://pubmed.ncbi.nlm.nih.gov/28281443/)).
- **Treated course:** prolonged (≥12 months therapy); paradoxical reactions may occur during treatment in ~21% of CNS-TB ([PMID: 42242389](https://pubmed.ncbi.nlm.nih.gov/42242389/)).
- **Critical period:** early diagnosis and treatment initiation is the key intervention window; delay strongly worsens outcome.

---

## 9. Inheritance and Population (Epidemiology)

- **Proportion of TB:** "Tuberculosis meningitis (TBM) accounts for approximately 1% of all active TB cases" (1–5% of TB) ([PMID: 36795648](https://pubmed.ncbi.nlm.nih.gov/36795648/)).
- **Prevalence:** CNS-TB ~2 per 100,000 inhabitants; represents "13.91% of all cases of meningitis and 4.55% of all cases of TB" ([PMID: 35288778](https://pubmed.ncbi.nlm.nih.gov/35288778/)).
- **Mortality:** in-hospital mortality "rose up to 42.12% in hospitalized patients" ([PMID: 35288778](https://pubmed.ncbi.nlm.nih.gov/35288778/)); ~40% HIV-negative, up to ~70% with HIV. In 2019, "78,200 adults died of TB meningitis" ([PMID: 36795648](https://pubmed.ncbi.nlm.nih.gov/36795648/)). An estimated 24,000 children <15 years developed TBM in 2019, of whom ~16,100 died ([PMID: 39706662](https://pubmed.ncbi.nlm.nih.gov/39706662/)).
- **Inheritance:** Not applicable (infectious disease). Host susceptibility is **multifactorial/polygenic** (TLR2, TIRAP, LTA4H).
- **Geographic distribution:** burden concentrated in high-TB-incidence, low-HDI settings and areas of high HIV prevalence.
- **Demographics:** male predominance in many cohorts; younger children over-represented among severe cases.

---

## 10. Diagnostics

No single test reliably rules TBM in or out; diagnosis is a composite.

**CSF profile.** "Cerebrospinal fluid (CSF) analysis showed lymphocytic pleocytosis, elevated protein, low glucose levels, and cobweb coagulum indicative of TBM" ([PMID: 37915698](https://pubmed.ncbi.nlm.nih.gov/37915698/)).

**Adenosine deaminase (ADA).** A useful adjunct with high specificity but limited sensitivity: "ADA was the best performing parameter. It attained a specificity of 95%, a positive likelihood ratio of 10.7, and an area under the receiver operating characteristics curve of 82.1%, but had a low sensitivity (55%)" ([PMID: 23973430](https://pubmed.ncbi.nlm.nih.gov/23973430/)).

**Molecular tests.** Xpert MTB/RIF Ultra is the WHO first-choice test: "Xpert Ultra had 76·5% sensitivity (95% CI 62·5-87·2 ...) and a negative predictive value of 92·7%," superior to Xpert (~56%) and MGIT culture (~61%) ([PMID: 31924549](https://pubmed.ncbi.nlm.nih.gov/31924549/)). Metagenomic NGS reaches ~84% sensitivity and CSF pyrosequencing higher still, but "mNGS cannot be used as a rule-out test" ([PMID: 35202495](https://pubmed.ncbi.nlm.nih.gov/35202495/)).

**Culture.** Confirmatory but insensitive: "The overall pooled estimates of CSF culture positive TBM was 29.72%" ([PMID: 36795648](https://pubmed.ncbi.nlm.nih.gov/36795648/)).

**Drug-resistance testing.** Targeted NGS on CSF (e.g., Deeplex Myc-TB) enables rapid resistance detection: "Targeted next-generation sequencing (tNGS) produces high read depths, allowing the detection of DR-associated alleles with low frequencies" ([PMID: 38466092](https://pubmed.ncbi.nlm.nih.gov/38466092/)).

**Neuroimaging.** The **TBM triad** — basal meningeal enhancement + hydrocephalus + basal-ganglia infarction — is diagnostically valuable: "the combination of meningeal enhancement and any degree of hydrocephalus is strongly suggestive of TBM" ([PMID: 28281443](https://pubmed.ncbi.nlm.nih.gov/28281443/)). In a 559-case series: tuberculomas 40%, basal meningeal enhancement 41%, infarction 27%, hydrocephalus 26% ([PMID: 31115112](https://pubmed.ncbi.nlm.nih.gov/31115112/)).

| Test | Sensitivity | Specificity/NPV | Source |
|---|---|---|---|
| CSF Xpert Ultra | ~77% | NPV 92.7% | PMID:31924549 |
| CSF Xpert (original) | ~56% | — | PMID:31924549 |
| MGIT culture | ~25–61% | culture-positive ~30% | PMID:36795648 |
| CSF mNGS | ~84% | not rule-out | PMID:35202495 |
| CSF pyrosequencing | ~98% | NPV ~98% | PMID:33421910 |
| CSF ADA | ~55% | ~95% spec | PMID:23973430 |

**Clinical criteria.** The Marais/uniform case definition (definite/probable/possible) and Thwaites score are used to classify cases. **Differential diagnosis** includes cryptococcal meningitis, bacterial/partially-treated bacterial meningitis, viral meningoencephalitis, carcinomatous meningitis, and neurosarcoidosis ([PMID: 41788392](https://pubmed.ncbi.nlm.nih.gov/41788392/)).

---

## 11. Outcome / Prognosis

- **Mortality:** ~40% overall (HIV-negative), up to ~70% with HIV co-infection; in-hospital ~42% ([PMID: 35288778](https://pubmed.ncbi.nlm.nih.gov/35288778/)).
- **Morbidity:** high rates of long-term neurological and cognitive sequelae. "Cognitive impairment ranging from 12% to over 90% was found across studies ... The most consistently affected domains were memory, attention, and executive function" ([PMID: 41629635](https://pubmed.ncbi.nlm.nih.gov/41629635/)).
- **Complications:** stroke/infarction (~30%), hydrocephalus, seizures/epilepsy, cranial neuropathies, hyponatremia, paradoxical reactions, IRIS (in HIV).
- **Prognostic factors:** BMRC stage at presentation (dominant), age (<5 years worse), HIV status, drug resistance, hyponatremia severity/persistence, low albumin/hemoglobin, delayed treatment. "Persistent hyponatraemia and increasing urinary output during treatment associate with worse clinical out[come]" ([PMID: 42167495](https://pubmed.ncbi.nlm.nih.gov/42167495/)).
- **Stroke burden:** "The frequency of stroke in TBM showed an estimate of 0.30 (95% CI, 0.26-0.33)" ([PMID: 36048445](https://pubmed.ncbi.nlm.nih.gov/36048445/)).

---

## 12. Treatment

**Standard antituberculous therapy.** WHO recommends **12 months** of therapy for TBM: "the World Health Organization recommends 12 months of treatment for TBM. The drugs used in the treatment are rifampicin, isoniazid, ethambutol, and pyrazinamide" (regimen 2HRZE/10HR) ([PMID: 39752122](https://pubmed.ncbi.nlm.nih.gov/39752122/)). CNS penetration differs by drug: "pyrazinamide penetrates the brain better than other drugs and kills TB bacteria more effectively. In addition, ethambutol does not get into the brain" ([PMID: 39752122](https://pubmed.ncbi.nlm.nih.gov/39752122/)). Rifampicin CNS penetration is limited, motivating high-dose (25–35 mg/kg) trials ([PMID: 34494572](https://pubmed.ncbi.nlm.nih.gov/34494572/)). Suggested NCIT terms: Isoniazid (C557), Rifampicin/Rifampin (C608), Pyrazinamide (C777), Ethambutol (C486), Dexamethasone (C405).

**Pediatric intensified regimen.** A 6-month intensified regimen (higher-dose H/R, pyrazinamide, ethionamide replacing ethambutol; 6HRZEto) markedly improved outcomes: "death, 5.5% ... vs 23.9% ...; treatment success (survival with or without sequelae), 94.6% ... vs 75.4%" ([PMID: 35673608](https://pubmed.ncbi.nlm.nih.gov/35673608/)).

**Adjunctive corticosteroids (NCIT: dexamethasone, prednisolone).** Standard of care for HIV-negative adults and children — but benefit is host-genotype-dependent. In the phase 3 LAST ACT trial (HIV-negative, CC/CT genotypes), "the primary endpoint of all-cause death or new neurological event over 12 months from randomization occurred in 108/305 (35.4%) given dexamethasone and 110/308 (35.7%) given placebo (hazard ratio of 0.99)" — i.e., no benefit in lower-inflammation genotypes ([PMID: 41540106](https://pubmed.ncbi.nlm.nih.gov/41540106/)). In HIV-positive adults, adjunctive dexamethasone "did not confer a benefit with respect to survival" ([PMID: 37819954](https://pubmed.ncbi.nlm.nih.gov/37819954/)).

**Host-directed / adjunctive therapy.** Aspirin, high-dose rifampicin, and linezolid are under trial (LASER-TBM, INTENSE-TBM, INSHORT, SURE). MMP inhibition (e.g., doxycycline) is a preclinical host-directed strategy ([PMID: 41819159](https://pubmed.ncbi.nlm.nih.gov/41819159/)).

**HIV co-management.** ART improves survival but timing is critical — early ART increases IRIS/adverse events in TBM; prednisone "is effective in both preventing and treating the paradoxical tuberculosis-associated immune reconstitution inflammatory syndrome" ([PMID: 31272663](https://pubmed.ncbi.nlm.nih.gov/31272663/)).

**Supportive / surgical.** Management of hydrocephalus (CSF diversion/shunting), seizure control, hyponatremia correction (distinguishing SIADH from cerebral salt wasting, which require opposite fluid strategies), and rehabilitation.

---

## 13. Prevention

- **Primary — BCG vaccination.** The cornerstone. "Protection against meningeal and miliary tuberculosis was also high in infants (RR, 0.1; 95% CI, .01-.77)" — ~90% efficacy ([PMID: 24336911](https://pubmed.ncbi.nlm.nih.gov/24336911/)). "the neonatal Bacillus Calmette-Guérin (BCG) is the only vaccine against TB and offers significant efficacy against disseminated and meningeal disease in children" ([PMID: 40498907](https://pubmed.ncbi.nlm.nih.gov/40498907/)). Protection against pulmonary TB is weaker and more variable.
- **Secondary.** Early case detection and prompt treatment initiation; TB preventive therapy in high-risk (e.g., HIV) individuals; contact tracing.
- **Tertiary.** Corticosteroids to limit inflammatory injury (genotype-informed), hydrocephalus management, and prevention/treatment of IRIS.
- **Public health.** TB control programs, HIV control, nutrition, and reduction of transmission.

---

## 14. Other Species / Natural Disease

TBM is fundamentally a human disease. *M. tuberculosis* has limited natural host range, though *M. bovis* (zoonotic) can cause CNS TB. Experimental infection with *Mycobacterium marinum* in zebrafish reproduces key inflammatory susceptibility biology ([PMID: 22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/)). Zoonotic potential exists for bovine TB. No dedicated companion-animal natural-TBM literature was identified in this review.

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*) / *M. marinum*.** Establishes the "inverted-U" inflammation model: "susceptibility to Mycobacterium marinum can result from either inadequate or excessive acute inflammation," driven by the LTA4H eicosanoid balance; the human LTA4H polymorphism "is associated with inflammatory cell recruitment, patient survival and response to adjunctive anti-inflammatory therapy" ([PMID: 22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/)). **Strength:** models host-genotype-directed therapy. **Limitation:** does not reproduce full basal-exudate neuropathology.
- **Mouse CNS-TB model.** SHH-modulated rapid CNS-TB model recapitulates MMP-9-driven BBB breakdown, reactive gliosis, and increased brain bacillary load ([PMID: 39536643](https://pubmed.ncbi.nlm.nih.gov/39536643/)). **Application:** BBB pathology and drug/host-directed therapy discovery.

---

## Mechanistic Model / Interpretation

```
 M. tuberculosis (Beijing lineage)
        │  hematogenous spread
        ▼
   RICH FOCUS (subpial/subependymal caseous granuloma)
        │  rupture into subarachnoid space
        ▼
   DENSE BASAL MENINGEAL EXUDATE ──────────────┐
        │              │              │        │
   (4a) arteritis  (4b) CSF-flow  (4c) CN     (5) MMP-9 ↑
        │              block       entrapment  │ (neutrophil/macrophage)
        ▼              ▼              ▼         ▼
   INFARCTION     HYDROCEPHALUS   CRANIAL     BBB DISRUPTION
   (basal ganglia)                NEUROPATHY  + neuroinflammation
        └──────────────┴──────────────┴─────────┘
                        ▼
        RAISED ICP, COMA, DEATH  /  survivor sequelae
        (cognitive impairment, focal deficit, epilepsy)

   HOST MODIFIER: LTA4H genotype (TT hyper- / CT / CC low-inflammation)
   → tunes exudate & MMP-9 magnitude, TNF balance
   → determines corticosteroid benefit
```

The disease is best understood as a **two-hit process**: (1) the mechanical/infectious hit of the Rich focus rupturing and generating a strategically located basal exudate, and (2) the immunopathological hit of dysregulated host inflammation (eicosanoid/TNF imbalance, MMP-9-mediated matrix destruction). The exudate's anatomical location — around the basal cisterns and perforating arteries — explains why the three cardinal complications are stereotyped (basal-ganglia stroke, obstructive hydrocephalus, cranial neuropathy). The host-inflammatory hit explains why anti-inflammatory adjunctive therapy helps some patients (hyperinflammatory TT) but not others (CC/CT), and why both too little and too much inflammation are harmful.

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [7610242](https://pubmed.ncbi.nlm.nih.gov/7610242/) | *Neuropathology* — establishes Rich focus → basal exudate → vasculitis/hydrocephalus/CN entrapment chain |
| [22953709](https://pubmed.ncbi.nlm.nih.gov/22953709/) | Host (TLR2, TIRAP, LTA4H) and pathogen (Beijing) susceptibility factors |
| [41540106](https://pubmed.ncbi.nlm.nih.gov/41540106/) | LAST ACT phase 3 — genotype-stratified dexamethasone; null in CC/CT |
| [22304914](https://pubmed.ncbi.nlm.nih.gov/22304914/) | Zebrafish LTA4H inverted-U inflammation model; links to human steroid response |
| [19789647](https://pubmed.ncbi.nlm.nih.gov/19789647/) | Dexamethasone lowers CSF MMP-9; MMP-9/neutrophil link |
| [39536643](https://pubmed.ncbi.nlm.nih.gov/39536643/) | Mouse model — MMP-9 drives BBB disruption |
| [31924549](https://pubmed.ncbi.nlm.nih.gov/31924549/) | Xpert Ultra diagnostic performance (~77%) |
| [23973430](https://pubmed.ncbi.nlm.nih.gov/23973430/) | CSF ADA performance (spec 95%, sens 55%) |
| [35288778](https://pubmed.ncbi.nlm.nih.gov/35288778/) | Epidemiology & mortality meta-analysis |
| [36795648](https://pubmed.ncbi.nlm.nih.gov/36795648/) | Microbiological diagnosis & mortality; 78,200 adult deaths (2019) |
| [36048445](https://pubmed.ncbi.nlm.nih.gov/36048445/) | Stroke frequency (~30%) and vascular territory |
| [41629635](https://pubmed.ncbi.nlm.nih.gov/41629635/) | Cognitive sequelae meta-analysis |
| [35673608](https://pubmed.ncbi.nlm.nih.gov/35673608/) | Pediatric 6-month intensified regimen outcomes |
| [39752122](https://pubmed.ncbi.nlm.nih.gov/39752122/) | WHO 12-month regimen & CNS drug penetration |
| [42167495](https://pubmed.ncbi.nlm.nih.gov/42167495/) | Hyponatremia prevalence & prognostic value |
| [34510291](https://pubmed.ncbi.nlm.nih.gov/34510291/) | SIADH vs cerebral salt wasting frequencies |
| [24336911](https://pubmed.ncbi.nlm.nih.gov/24336911/) | BCG ~90% protection vs meningeal/miliary TB |
| [28281443](https://pubmed.ncbi.nlm.nih.gov/28281443/) | Untreated temporal course; imaging triad value |
| [31115112](https://pubmed.ncbi.nlm.nih.gov/31115112/) | Imaging finding frequencies (559 cases) |
| [38466092](https://pubmed.ncbi.nlm.nih.gov/38466092/) | tNGS for rapid CSF drug-resistance detection |
| [37819954](https://pubmed.ncbi.nlm.nih.gov/37819954/) | Dexamethasone no benefit in HIV-positive adults |
| [42242389](https://pubmed.ncbi.nlm.nih.gov/42242389/) | Paradoxical reactions (~21%) in CNS-TB |

---

## Limitations and Knowledge Gaps

1. **Diagnostic gap.** No test reliably excludes TBM; culture confirms only ~30%, and even Xpert Ultra misses ~1 in 4 cases. Delayed diagnosis remains a leading cause of death.
2. **Corticosteroid uncertainty.** The genotype-stratified null result in CC/CT and the HIV-positive null challenge decades of blanket steroid use; optimal, genotype-informed anti-inflammatory strategy is unresolved.
3. **Drug penetration.** Standard regimens penetrate the CNS poorly; optimal doses of rifampicin/linezolid and duration are still under trial.
4. **Host-directed therapy.** MMP-9 inhibition, aspirin, and resolvin biology are promising but not yet standard.
5. **Pediatric/HIV evidence.** Much mechanistic and trial data derive from adult, HIV-negative Vietnamese cohorts; generalizability to children and HIV-endemic African settings is incomplete.
6. **No omics disease signature.** TBM-specific transcriptomic/proteomic/metabolomic diagnostic biomarkers are not yet validated for routine use.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-guided steroid trials** extending LAST ACT to pediatric and HIV-positive populations, testing whether the TT (hyperinflammatory) genotype specifically benefits.
2. **Host-directed therapy trials** of MMP-9 inhibitors (doxycycline) and pro-resolving mediators, using CSF MMP-9 and resolvin profiles as pharmacodynamic biomarkers.
3. **Optimized antibiotic PK/PD** — complete high-dose rifampicin + linezolid intensification trials (INTENSE-TBM, INSHORT, SURE) with CSF drug-exposure endpoints.
4. **Rapid molecular diagnostics scale-up** — deploy CSF tNGS/pyrosequencing for simultaneous detection and resistance profiling; develop a rule-out biomarker panel.
5. **CSF biomarker discovery** — multi-omic (proteomic/metabolomic/lipidomic) profiling to build a validated early-diagnosis and prognostic signature.
6. **Improved vaccines** — evaluate next-generation TB vaccines specifically for prevention of childhood meningeal/miliary disease.

---

*Report compiled from 15 confirmed findings and 68 reviewed papers. Evidence sources span human clinical (RCTs, cohorts, meta-analyses), model-organism (zebrafish, mouse), and in-vitro studies, as annotated by PMID throughout.*


## Artifacts

- [OpenScientist final report](Meningeal_Tuberculosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Meningeal_Tuberculosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 35 |
| On topic | 15 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41629635` *(abstract only)*: "most consistently affected memory, attention, and executive function"
  - closest text in source: "The most consistently affected domains were memory, attention, and executive function, followed by language and visuospatial"
- `PMID:39752122` *(abstract only)*: "pyrazinamide penetrates the brain better than other drugs and kills TB bacteria more effectively. In addition, ethambutol does not get into the brain"
  - closest text in source: "However, pyrazinamide, with higher penetration into the central nervous system, is generally overlooked"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35673608` (4 mentions) - Comparative Effectiveness of Regimens for Drug-Susceptible Tuberculous Meningitis in Children and Adolescents: A Systematic Review and Aggregate-Level Data Meta-Analysis.
  - shared terms: children

Weighed against this report's own most characteristic terms: `tbm`, `disease`, `meningeal`, `csf`, `hydrocephalus`, `tuberculosis`, `therapy`, `hiv`, `lta4h`, `host`, `susceptibility`, `inflammatory`, `basal`, `children`, `inflammation`, `human`, `mmp-9`, `exudate`, `cns`, `cranial`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0006042` (2 mentions) - the report calls it "MONDO"; MONDO calls it **meningeal tuberculosis**
- `HP:0002013` (1 mention) - the report calls it "~52–92% (children higher)"; HP calls it **Vomiting**
- `HP:0001250` (1 mention) - the report calls it "~72% (children)"; HP calls it **Seizure**
- `HP:0001269` (1 mention) - the report calls it "~30% (stroke)"; HP calls it **Hemiparesis**
- `HP:0000238` (1 mention) - the report calls it "26–63% imaging"; HP calls it **Hydrocephalus**
- `HP:0100543` (1 mention) - the report calls it "12–>90% survivors"; HP calls it **Cognitive impairment**
- `HP:0012229` (1 mention) - the report calls it "abnormal CSF"; HP calls it **CSF pleocytosis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000496` (1 mention) - the report calls it "common (basal exudate entrapment)"; HP calls it **Abnormality of eye movement**, and lists "Abnormal eye movement" among its other names