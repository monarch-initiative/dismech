---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T18:50:19.937162'
end_time: '2026-09-29T19:07:40.774785'
duration_seconds: 1040.84
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Ehrlichiosis
  mondo_id: MONDO:0016003
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 16
  validator_version: 0.3.0
term_validation:
  total_terms: 40
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 19
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0016003
    reported_labels:
    - if available
    - ehrlichiosis
    ontology_label: ehrlichiosis
  - term_id: HP:0012047
    reported_labels:
    - hemophagocytosis
    ontology_label: Hemeralopia
  labels_variant: 10
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ehrlichiosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ehrlichiosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ehrlichiosis
- **MONDO ID:** MONDO:0016003 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Ehrlichiosis** covering all of the
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

# Ehrlichiosis (MONDO:0016003): A Comprehensive Disease Characteristics Report

**Category:** Infectious Disease (tick-borne zoonosis)
**Investigation:** 5 iterations · 12 confirmed findings · 52 papers reviewed

---

## Summary

**Ehrlichiosis is an acute, tick-borne zoonotic infection caused by obligate intracellular, Gram-negative bacteria of the genus *Ehrlichia*** — most importantly *Ehrlichia chaffeensis*, the agent of human monocytic ehrlichiosis (HME). It is **not a genetic or heritable disease**; it has no causal human gene, no Mendelian inheritance, and no ClinVar/OMIM pathogenic-variant profile. Accordingly, many sections of the standard "disease characteristics" template that presuppose a genetic etiology (causal genes, pathogenic variants, penetrance, founder effects, karyotyping, gene therapy) are **not applicable**, and this report states so explicitly where relevant while redirecting the underlying question (e.g., "genetic risk factors" → host immune determinants; "causal genes" → bacterial virulence genes).

The disease is transmitted chiefly by the lone star tick (*Amblyomma americanum*), with white-tailed deer (*Odocoileus virginianus*) as the principal reservoir, and is concentrated in the south-central and southeastern United States. Clinically it presents as an **undifferentiated febrile illness** with a characteristic laboratory triad of **leukopenia, thrombocytopenia, and elevated hepatic transaminases**. The pathophysiology is a two-act story: first, the bacterium **subverts monocyte/macrophage innate immunity** (via the TRP120 effector activating Notch and Wnt-PI3K-mTOR signaling, and the T4SS effector Etf-1 hijacking autophagy and ferritinophagy for nutrients and iron); second, in severe cases the **host immune response itself becomes pathogenic**, producing a CD8⁺ T-cell/TNF-α–driven, toxic-shock-like syndrome that can culminate in hemophagocytic lymphohistiocytosis (HLH). Immunosuppression, advanced age, and delayed therapy are the dominant severe-disease risk factors.

**Doxycycline is rapidly and highly effective** and should be started empirically on clinical suspicion, because acute-phase serology is insensitive and diagnosis often relies on PCR or blood-smear morulae. **No human vaccine exists**, so prevention rests entirely on personal anti-tick measures. Encouragingly, an attenuated *E. chaffeensis* modified-live vaccine (disrupting the phage head-to-tail connector gene *phtcp*/Ech_0660) confers durable, CD4⁺ Th1–mediated protection in the canine host, pointing toward a veterinary — and potentially zoonosis-reducing — vaccine.

---

## Key Findings

### F001 — Ehrlichiosis is a tick-borne zoonosis caused by obligate intracellular *Ehrlichia* bacteria, chiefly *E. chaffeensis*

Human monocytotropic ehrlichiosis (HME) is caused by *Ehrlichia chaffeensis* and is maintained in a zoonotic enzootic cycle: **white-tailed deer (*Odocoileus virginianus*)** serve as the main vertebrate reservoir and the **lone star tick (*Amblyomma americanum*)** as the principal vector. Related agents cause related syndromes: *E. ewingii* causes human ewingii ehrlichiosis (often in immunocompromised hosts), *E. muris* subsp. *eauclairensis* causes ehrlichiosis in the upper Midwest, and *E. canis* causes canine monocytic ehrlichiosis (with rare human cases). Disease severity ranges from mild/self-limited to fatal.

> *"Ehrlichia chaffeensis is the causative agent of human monocytotropic ehrlichiosis (HME), a disease that ranges in severity from mild to fatal infection. Ehrlichia chaffeensis is maintained in a zoonotic cycle involving white-tailed deer (Odocoileus virginianus) as the main vertebrate reservoir and lone star ticks (Amblyomma americanum) as its principal vector."* — [PMID: 35763959](https://pubmed.ncbi.nlm.nih.gov/35763959/)

**Ontology:** MONDO:0016003 (ehrlichiosis); NCBI Taxon 945 (*Ehrlichia chaffeensis*); NCBI Taxon 9874 (*Odocoileus virginianus*); NCBI Taxon 6943 (*Amblyomma americanum*).

### F008 — *Ehrlichia* are Gram-negative obligate intracellular bacteria replicating as morulae with a biphasic developmental cycle

Ehrlichiae are tick-transmitted, Gram-negative, obligately intracellular bacteria that live and replicate inside host-cell **cytoplasmic vacuoles**, where dividing organisms form microcolonies called **morulae**. They exhibit a biphasic developmental cycle with **reticulate** (replicative) and **dense-cored** (infectious) forms. Notably, they **lack lipopolysaccharide (LPS) and peptidoglycan**, which shapes their immune interactions. A genus-conserved 38-kDa ferric ion-binding protein (Fbp) mediates iron acquisition, and iron-acquisition genes show reductive genome evolution consistent with obligate intracellular life. Cell tropism differs by species: *E. chaffeensis* targets **mononuclear phagocytes (monocytes/macrophages)**, whereas *E. ewingii* and *Anaplasma phagocytophilum* target **granulocytes**.

> *"Ehrlichiae are tick-transmitted, gram-negative, obligately intracellular bacteria that live and replicate in cytoplasmic vacuoles, but little is known about iron acquisition mechanisms necessary for their survival."* — [PMID: 15618141](https://pubmed.ncbi.nlm.nih.gov/15618141/)

> *"Morulae were present in monocytes in E. chaffeensis-infected cases and granulocytes in the E. ewingii-infected case."* — [PMID: 14976527](https://pubmed.ncbi.nlm.nih.gov/14976527/)

**Ontology:** CL:0000576 (monocyte); CL:0000235 (macrophage); CL:0000775 (neutrophil/granulocyte); GO:0005776 (autophagosome); GO:0020003 (symbiont-containing vacuole).

### F002 — *E. chaffeensis* subverts innate immunity via the TRP120 effector, activating Notch and Wnt-PI3K-mTOR signaling

The *E. chaffeensis* type-1 secreted **tandem-repeat protein TRP120** interacts with the Notch metalloprotease **ADAM17**, activating **canonical Notch signaling** to downregulate **TLR2/4** expression and thereby dampen innate immune recognition and promote intracellular survival. In parallel, *Ehrlichia* activates **Wnt–PI3K–mTOR signaling** to inhibit autolysosome generation, blocking the autophagic destruction pathway of the mononuclear phagocyte.

> *"we demonstrate E. chaffeensis, via the TRP120 effector, activates the canonical Notch signaling pathway to promote intracellular survival"* — [PMID: 27381289](https://pubmed.ncbi.nlm.nih.gov/27381289/)

> *"Ehrlichia Activation of Wnt-PI3K-mTOR Signaling Inhibits Autolysosome Generation and Autophagic Destruction by the Mononuclear Phagocyte"* — [PMID: 28993455](https://pubmed.ncbi.nlm.nih.gov/28993455/)

**Ontology:** GO:0007219 (Notch signaling pathway); GO:0016055 (Wnt signaling pathway); GO:0031929 (TOR signaling); GO:0002224 (toll-like receptor signaling pathway).

### F003 — *E. chaffeensis* uses T4SS effector Etf-1 to hijack autophagy and ferritinophagy for nutrients and iron

The **type IV secretion system (T4SS) effector Etf-1** induces host **autophagy** to supply the bacterium with nutrients, and drives **bacterial effector-induced ferritinophagy** to liberate and acquire **iron**, which is essential for intracellular proliferation. Host membrane lipids are additionally trafficked to the bacterial inclusion membrane. An intracellular nanobody directed against the T4SS effector inhibits infection — a proof-of-concept therapeutic strategy.

> *"Iron robbery by intracellular pathogen via bacterial effector-induced ferritinophagy"* — [PMID: 34074773](https://pubmed.ncbi.nlm.nih.gov/34074773/)

**Ontology:** GO:0006914 (autophagy); GO:0006879 (intracellular iron ion homeostasis); GO:0140355 (cargo receptor ligand activity, ferritinophagy).

### F004 — HME presents as an undifferentiated febrile illness with the leukopenia–thrombocytopenia–transaminitis triad; doxycycline is highly efficacious

Both HME (*E. chaffeensis*, infecting mononuclear phagocytes) and granulocytic infection cause **undifferentiated fever with leukopenia, thrombocytopenia, and elevated serum aminotransferases**. Rash is infrequent (more common in children) and vasculitis is exceedingly rare. Severe or fatal disease is associated with secondary/opportunistic infections and delayed therapy. In a pediatric HME series, phenotype frequencies were: fever 100%, rash 67%, myalgias 58%; thrombocytopenia 92%, elevated liver function tests 91%, lymphopenia 75%, hyponatremia 67%, leukopenia 58%, and anemia 42%. Diagnosis is confirmed by PCR (acute) or paired serology (convalescent); intracytoplasmic **morulae** in leukocytes are diagnostic but insensitive (seen in ~38% of PCR-positive cases; far more often in immunocompromised than immunocompetent patients). **Doxycycline is highly efficacious.**

> *"Both infections cause undifferentiated fever with leukopenia, thrombocytopenia, and elevations in serum aminotransferase levels. Rash is an infrequent sign, and vasculitis is exceedingly rare. Severe or fatal ehrlichiosis is associated with secondary or opportunistic infections and delayed therapy."* — [PMID: 7619983](https://pubmed.ncbi.nlm.nih.gov/7619983/)

> *"Therapy with doxycycline is highly efficacious."* — [PMID: 7619983](https://pubmed.ncbi.nlm.nih.gov/7619983/)

> *"patients demonstrated thrombocytopenia (92%), elevated liver function tests (91%), lymphopenia (75%), hyponatremia (67%), leukopenia (58%), and anemia (42%)"* — [PMID: 9200384](https://pubmed.ncbi.nlm.nih.gov/9200384/)

**Phenotype table (pediatric HME, [PMID: 9200384](https://pubmed.ncbi.nlm.nih.gov/9200384/)):**

| Phenotype | Frequency | Type | Suggested HPO term |
|---|---|---|---|
| Fever | 100% | Symptom | HP:0001945 (Fever) |
| Rash | 67% | Clinical sign | HP:0000988 (Skin rash) |
| Myalgia | 58% | Symptom | HP:0003326 (Myalgia) |
| Thrombocytopenia | 92% | Lab abnormality | HP:0001873 (Thrombocytopenia) |
| Elevated transaminases | 91% | Lab abnormality | HP:0002910 (Elevated hepatic transaminase) |
| Lymphopenia | 75% | Lab abnormality | HP:0001888 (Lymphopenia) |
| Hyponatremia | 67% | Lab abnormality | HP:0002902 (Hyponatremia) |
| Leukopenia | 58% | Lab abnormality | HP:0001882 (Leukopenia) |
| Anemia | 42% | Lab abnormality | HP:0001903 (Anemia) |
| Headache / meningoencephalitis | common / rare-severe | Symptom/CNS sign | HP:0002315 (Headache); HP:0002383 (Encephalitis) |

### F005 — Fatal ehrlichiosis is an immunopathologic, TNF-α–mediated toxic-shock-like syndrome driven by CD8⁺ T cells

In murine models (*Ixodes ovatus Ehrlichia*/IOE and *E. muris*), lethal monocytotropic ehrlichiosis produces a **toxic-shock-like syndrome** with extensive liver damage, extremely elevated serum **TNF-α**, expansion of **TNF-α–producing CD8⁺ T cells**, a *decreased* number of *Ehrlichia*-specific **CD4⁺ Th1 (IFN-γ)** cells, low IL-12, and systemic **IL-10** overproduction. CD8⁺ T-cell deficiency abrogated TNF-α/IL-10, reduced tissue injury and bacterial burden, and restored CD4⁺ numbers; IL-10 depletion restored CD4⁺ T-cell numbers. Neutrophil depletion *enhanced* bacterial clearance and *reduced* pathology — indicating neutrophils contribute to immunopathology rather than protection. This establishes that **severe disease is host-immune-mediated, not purely a function of bacterial burden**.

> *"Lethal infections caused by high or low doses of IOE were accompanied by extensive liver damage, extremely elevated levels of TNF-alpha in the serum, high frequency of Ehrlichia-specific, TNF-alpha-producing CD8(+) T cells in the spleen"* — [PMID: 14734762](https://pubmed.ncbi.nlm.nih.gov/14734762/)

> *"depletion of neutrophils from lethally infected mice enhanced bacterial elimination, decreased immune-mediated pathology, and prolonged survival"* — [PMID: 23478316](https://pubmed.ncbi.nlm.nih.gov/23478316/)

**Ontology:** GO:0032640 (tumor necrosis factor production); GO:0006925 (inflammatory cell apoptotic process); CL:0000625 (CD8-positive, alpha-beta T cell); CL:0000545 (T-helper 1 cell); UBERON:0002107 (liver).

### F012 — Ehrlichiosis is an increasingly recognized infectious trigger of secondary HLH, especially in immunosuppressed patients

Multiple case series document HME triggering **secondary hemophagocytic lymphohistiocytosis (HLH)** — a hyperinflammatory syndrome of uncontrolled macrophage/lymphocyte activation with hyperferritinemia, cytopenias, and hemophagocytosis. It represents the clinical extreme of the same immunopathologic continuum defined in murine models (F005). Cases occur in immunocompetent adults, the elderly, and immunosuppressed hosts (e.g., a pediatric kidney transplant recipient within the first post-transplant month). Management combines **doxycycline with immunomodulation** (corticosteroids/dexamethasone, IVIG, anakinra); early doxycycline is key, though some cases progress despite it.

> *"Human monocytotropic ehrlichiosis (HME) is a very rare cause of HLH. Failure to consider ehrlichiosis can result in misdiagnosis and an increased length of hospitalization"* — [PMID: 32928497](https://pubmed.ncbi.nlm.nih.gov/32928497/)

> *"We describe a pediatric kidney transplant recipient who experienced secondary HLH due to ehrlichiosis within the initial post-transplant month."* — [PMID: 34595809](https://pubmed.ncbi.nlm.nih.gov/34595809/)

**Ontology:** MONDO:0015540 (hemophagocytic lymphohistiocytosis); HP:0012047 (hemophagocytosis); HP:0011031 (abnormal iron/ferritin); GO:0006954 (inflammatory response).

### F006 — Epidemiology: HME is concentrated in the south-central/southeastern US, median age ~50s, male predominance, rising incidence

National US surveillance (1997–2001) reported average annual incidences of **HME 0.7, HGE 1.6, and other ehrlichiosis 0.2 per million** persons in reporting states, with most HME cases from the south-central/southeastern US. Median ages were HME 53 years and HGE 51 years, and >57% of patients were male. Texas surveillance (2008–2017) recorded 101 cases with geographic clustering and an increasing annual trend from 2009–2017. Overall US ehrlichiosis incidence rose roughly **four-fold from 2000 to 2012**.

> *"The average annual incidences of HME, HGE, and OE per million persons residing in states reporting disease were 0.7, 1.6, and 0.2, respectively. The median ages of HME (53 yr) and HGE cases (51 yr) were consistent with published patient series. Most (> 57%) ehrlichiosis patients were male."* — [PMID: 12860604](https://pubmed.ncbi.nlm.nih.gov/12860604/)

> *"In Texas, 101 cases of ehrlichiosis were reported during 2008-2017. We observed geographic grouping of cases as well as an increasing trend of reported cases occurring annually from 2009 to 2017."* — [PMID: 34325087](https://pubmed.ncbi.nlm.nih.gov/34325087/)

### F009 — Diagnosis: acute-phase serology has limited sensitivity; PCR and blood-smear morulae enable early diagnosis, paired serology confirms

For the closely related granulocytic anaplasmosis (methodologically analogous), only **~55% of PCR- and culture-confirmed cases were seropositive on acute-presentation serum**; all initially seronegative patients seroconverted on convalescent samples 6–45 days later. This demonstrates the insensitivity of acute indirect immunofluorescence assay (IFA) and the need for **paired acute/convalescent sera (≥4-fold titer rise)**. **PCR of whole blood is the most useful acute direct test**; peripheral blood smear morulae are diagnostic but insensitive (~38% of PCR-positive HME). These facts justify **empiric doxycycline** on clinical suspicion rather than waiting for serologic confirmation.

> *"only approximately 55% of the PCR and culture positive cases were also seropositive on blood samples obtained at the same time point, indicating that serologic testing performed at the time of presentation has limited sensitivity"* — [PMID: 39631641](https://pubmed.ncbi.nlm.nih.gov/39631641/)

### F007 — Prevention relies on personal anti-tick measures; no human vaccine exists

Primary prevention is via **personal protection against tick bites**: EPA-registered repellents, permethrin-treated clothing (strong contact irritancy / "hot-foot" effect causing ticks to dislodge; 93–97% repellency in bioassays), untreated protective clothing, and post-exposure tick checks and showering. **No human vaccine exists for ehrlichiosis**; a Lyme disease vaccine under development would not reduce ehrlichiosis. *Amblyomma americanum* and *Dermacentor variabilis* co-occur and transmit multiple pathogens, so integrated tick avoidance is the practical strategy.

> *"This includes using repellents, wearing untreated or permethrin-treated protective clothing, and conducting tick checks after coming inside"* — [PMID: 35364518](https://pubmed.ncbi.nlm.nih.gov/35364518/)

> *"this breakthrough would not reduce cases of other tick-borne diseases, such as anaplasmosis, babesiosis, ehrlichiosis, spotted fever group rickettsiosis, and Powassan encephalitis"* — [PMID: 33549976](https://pubmed.ncbi.nlm.nih.gov/33549976/)

### F010 — Protective immunity is Th1/CD4⁺ IFN-γ–dependent; an attenuated *phtcp*/Ech_0660 mutant confers durable protection in dogs

Protective immunity depends on *Ehrlichia*-specific **IFN-γ–producing CD4⁺ Th1 cells** plus antibodies (adoptive transfer protects mice). An attenuated *E. chaffeensis* mutant disrupting the **phage head-to-tail connector protein gene (*phtcp* / Ech_0660)** grows in an attenuated manner and, as a **modified live attenuated vaccine (MLAV)**, protects dogs against both intravenous and tick-transmitted wild-type challenge, with protection persisting up to **12 months** and robust *E. chaffeensis*-specific IgG, CD4⁺ Th1 (IFN-γ), and IL-17/Th17 responses. Analogous *phtcp* mutagenesis has now been achieved in *E. canis*, broadening the vaccine strategy across Anaplasmataceae.

> *"vaccination with the Ech_0660 mutant protects dogs from physiologic, tick-transmitted, secondary challenge with wild-type E. chaffeensis"* — [PMID: 26841025](https://pubmed.ncbi.nlm.nih.gov/26841025/)

> *"MLAV-immunized dogs rapidly cleared infections and exhibited significantly fewer systemic bacterial infections compared to unvaccinated controls. Robust E. chaffeensis-specific IgG and CD4 T-cell responses persisted throughout the assessment period."* — [PMID: 39826432](https://pubmed.ncbi.nlm.nih.gov/39826432/)

### F011 — Model organisms: murine IOE/*E. muris* toxic-shock model, plus natural hosts dog and white-tailed deer

**Murine models:** C57BL/6 mice infected with IOE or *E. muris* reproduce fatal toxic-shock-like monocytotropic ehrlichiosis (liver injury, TNF-α surge, CD8⁺ T-cell immunopathology) and are the workhorse for dissecting immunity versus immunopathology. **Natural-host models:** dogs (*E. canis* canine monocytic ehrlichiosis; also experimental *E. chaffeensis*) and white-tailed deer (the *E. chaffeensis* reservoir) support tick-transmission and vaccine studies. **In vitro:** *E. chaffeensis* is cultured in the DH82 canine macrophage line; HL-60 cells support granulocytic *Anaplasma*. Targeted mutagenesis of both *E. chaffeensis* and *E. canis* genomes is now feasible.

> *"we compared low and high doses of the highly virulent IOE strain and the less virulent Ehrlichia muris strain that are closely related to E. chaffeensis in C57BL/6 mice"* — [PMID: 14734762](https://pubmed.ncbi.nlm.nih.gov/14734762/)

> *"We have also described using the ticks infected by this method the transmission of both wild-type and transposon mutants of E. chaffeensis to its primary reservoir host, white tailed deer and to another known host, dog."* — [PMID: 27729288](https://pubmed.ncbi.nlm.nih.gov/27729288/)

---

## Section-by-Section Report

### 1. Disease Information

Ehrlichiosis is a group of acute febrile tick-borne bacterial zoonoses caused by obligate intracellular *Ehrlichia* species (F001, F008). The principal human form is **human monocytic (monocytotropic) ehrlichiosis (HME)**, caused by *E. chaffeensis*. Other human agents include *E. ewingii* (ewingii ehrlichiosis) and *E. muris* subsp. *eauclairensis* (upper Midwest). Note that "human granulocytic ehrlichiosis" (HGE) was **reclassified** as human granulocytic **anaplasmosis (HGA)**, caused by *Anaplasma phagocytophilum* — a distinct but frequently co-cited entity.

**Key identifiers:** MONDO:0016003 (ehrlichiosis); MeSH D016873 (Ehrlichiosis); ICD-10 **A77.40–A77.49** (Ehrlichiosis); ICD-11 **1C30.2**. There is **no OMIM entry** because ehrlichiosis is an infectious, not genetic, disease; Orphanet does not list it as a rare genetic disorder. **Synonyms/alternatives:** human monocytic ehrlichiosis (HME), human monocytotropic ehrlichiosis, *Ehrlichia chaffeensis* infection, Sennetsu fever (historically, *Neorickettsia sennetsu*), canine monocytic ehrlichiosis (veterinary).

**Information source:** Evidence is a mixture of **aggregated disease-level resources** (CDC/national surveillance, reviews) and **individual patient reports** (case series, e.g., pediatric HME [PMID: 9200384], HLH case reports).

### 2. Etiology

**Primary cause — infectious:** Ehrlichiosis is caused by infection with *Ehrlichia* bacteria transmitted by tick bite (F001, F008). It is **not genetic**. Therefore:

- **Genetic risk factors:** Not applicable in the Mendelian/GWAS sense — no human causal variant or susceptibility locus is established. The relevant host determinants are **immune status** (see below), not germline variants. *(Not available: causal variants, modifier genes, GWAS loci.)*
- **Environmental / exposure risk factors:** Outdoor activity in endemic regions (hunting, hiking, camping, occupational exposure such as forestry), residence in the south-central/southeastern US, warm-season tick activity, and tick bite by *A. americanum*. Demographic risk: **older age and male sex** (F006). **Immunosuppression** (transplant, HIV, immunomodulatory therapy) and **advanced age** are the dominant risk factors for *severe* disease and for secondary HLH (F012).
- **Protective factors:** Effective tick avoidance (repellents, permethrin-treated clothing, tick checks) reduces incidence (F007). Prior *Ehrlichia*-specific CD4⁺ Th1/antibody immunity is protective in animal models (F010). *(No genetic protective variants established.)*
- **Gene–environment interactions:** Not applicable in the classical sense; the operative interaction is **host immune competence × pathogen exposure** — the same exposure produces mild disease in the immunocompetent and life-threatening HLH in the immunosuppressed (F012).

### 3. Phenotypes

See F004 table above. Core phenotype: acute (typically 1–2 weeks post-bite) **fever, headache, myalgia, malaise**, with laboratory **thrombocytopenia, leukopenia, and elevated transaminases**. Rash is infrequent in adults (~30%) but common in children (~67%). Severe manifestations include **meningoencephalitis, ARDS, acute kidney injury, DIC, septic/toxic shock, and HLH**. Onset is **adult-predominant** (median age ~50s) but occurs at all ages; severity is **variable** (mild self-limited to fatal); course is **acute/monophasic** with rapid resolution on doxycycline. **Quality-of-life impact:** for uncomplicated, promptly treated disease, full recovery is typical with minimal long-term sequelae; severe/HLH cases carry substantial morbidity and mortality. There is **no strong evidence** that *Ehrlichia* seropositivity is associated with chronic musculoskeletal pain or osteoarthritis (per JoCo OA cross-sectional data, [PMID: 38206624]).

### 4. Genetic/Molecular Information

**Not applicable as a human genetic disease.** There are **no human causal genes, pathogenic variants, modifier genes, disease-specific epigenetic signatures, or chromosomal abnormalities**. ClinVar/HGMD/OMIM contain no entries for ehrlichiosis as a heritable condition.

Reframed to the **pathogen's genetics** (the biologically relevant "molecular information"): key *E. chaffeensis* virulence genes include **TRP120** (immune subversion, Notch activation; F002), **Etf-1** (T4SS effector; autophagy/ferritinophagy; F003), **p28/OMP** (major outer membrane protein family, antigenic variation), **Fbp** (38-kDa ferric ion-binding protein; iron acquisition; F008), and **phtcp/Ech_0660** (phage head-to-tail connector; attenuation target for vaccines; F010). *E. canis* homologs include **TRP19, p30, trp36** (serodiagnostic and genotyping markers).

### 5. Environmental Information

**Infectious agents (Taxon):** *E. chaffeensis* (NCBI:txid945), *E. ewingii* (NCBI:txid302), *E. canis* (NCBI:txid943), *E. muris* (NCBI:txid35795). **Vectors:** *Amblyomma americanum* (lone star tick), with *Amblyomma maculatum* and *Dermacentor variabilis* implicated for related agents. **Reservoir:** white-tailed deer. **Environmental/lifestyle factors:** seasonal (spring–summer) outdoor exposure, geographic residence in endemic zones; suburban green spaces now also carry risk, not just rural settings ([PMID: 41338244]). No chemical toxins, pollution, radiation, smoking, diet, or alcohol are established contributors.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating event → clinical manifestation):**

1. An infected *A. americanum* tick bites a human and inoculates *E. chaffeensis* dense-cored infectious forms → **leads to** entry into the bloodstream (F001, F008).
2. The bacterium is internalized by **monocytes/macrophages** into a cytoplasmic vacuole → **results in** an intracellular replicative niche (morula) (F008).
3. The TRP120 effector engages **ADAM17/Notch** and activates **Wnt–PI3K–mTOR** signaling → **leads to** downregulation of TLR2/4 and inhibition of autolysosome formation, i.e., **evasion of innate killing** (F002). *(Demonstrated in vitro/cell models.)*
4. The T4SS effector **Etf-1** induces **autophagy and ferritinophagy** → **results in** delivery of nutrients and **iron** to the bacterium, enabling proliferation (F003). *(Demonstrated in vitro.)*
5. Bacterial replication and host-cell dysfunction across bone marrow and reticuloendothelial tissues → **leads to** **cytopenias (thrombocytopenia, leukopenia) and hepatic injury (transaminitis)** — the clinical/laboratory triad (F004).

   **Branch A (controlled infection):** A balanced **CD4⁺ Th1 / IFN-γ** response plus antibodies → **results in** bacterial clearance and recovery, accelerated by doxycycline (F010, F004).

   **Branch B (dysregulated immunity → severe disease):** In susceptible hosts (immunosuppressed, elderly, high inoculum, delayed therapy), the response skews to **TNF-α–producing CD8⁺ T cells** with **falling CD4⁺ Th1** numbers and **IL-10 overproduction** → **leads to** a **toxic-shock-like syndrome** with extensive liver damage; neutrophils amplify tissue injury (F005). *(Demonstrated in murine IOE/E. muris models; inferred for human severe disease.)*
6. Unchecked macrophage/T-cell activation → **culminates in** **secondary HLH**: hyperferritinemia, hemophagocytosis, multiorgan failure (F012). *(Human case series; mechanistically continuous with Branch B.)*

**Upstream vs downstream:** Bacterial immune subversion (steps 3–4) is upstream and drives bacterial burden; the host CD8⁺/TNF-α immunopathology (steps 5B–6) is downstream and drives *severity independent of burden* — the critical insight that severe ehrlichiosis is **immune-mediated**. **Cell types:** monocytes/macrophages (CL:0000576/CL:0000235, primary host cells), CD8⁺ T cells (CL:0000625, pathogenic effectors), CD4⁺ Th1 (CL:0000545, protective), neutrophils (CL:0000775, pathology-amplifying). **Biological processes:** GO:0007219 (Notch signaling), GO:0006914 (autophagy), GO:0006879 (iron homeostasis), GO:0032640 (TNF production), GO:0006954 (inflammatory response).

### 7. Anatomical Structures Affected

- **Organ level (primary):** blood/hematopoietic system, liver (UBERON:0002107), spleen (UBERON:0002106), bone marrow (UBERON:0002371), lymph nodes. **Secondary:** lungs (ARDS; UBERON:0002048), kidney (UBERON:0002113), central nervous system (meningoencephalitis; UBERON:0000955).
- **Body systems:** hematologic/immune (primary); hepatobiliary, respiratory, renal, and nervous systems in complicated disease.
- **Tissue/cell level:** mononuclear phagocytes (monocytes/macrophages; CL:0000576/CL:0000235) for *E. chaffeensis*; granulocytes (CL:0000775) for *E. ewingii*.
- **Subcellular level:** the **symbiont-containing cytoplasmic vacuole/morula** (GO:0020003); host processes co-opted include the autophagosome/lysosome (GO:0005776) and ferritin/iron pools.
- **Localization/lateralization:** systemic and **bilateral/diffuse** (a disseminated bloodborne infection), not focal or lateralized.

### 8. Temporal Development

- **Onset:** acute, typically **7–14 days after tick bite**; adult-predominant but all ages affected.
- **Course:** acute/monophasic; **self-limited to rapidly progressive**. With doxycycline, defervescence usually occurs within 24–48 hours. Untreated or delayed cases can progress within days to shock, HLH, or death.
- **Stages:** early undifferentiated febrile phase → laboratory-abnormal phase (cytopenias, transaminitis) → (in severe cases) systemic inflammatory/toxic-shock/HLH phase.
- **Critical period:** the **therapeutic window** — early empiric doxycycline is the single most important determinant of outcome (F004, F012). Chronic carriage is characteristic of the *animal* host (dogs), not typically humans.

### 9. Inheritance and Population

**Not heritable** — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency applies. Epidemiology (F006): US HME incidence ~0.7 per million (1997–2001 surveillance), rising ~4-fold by 2012; concentrated in the **south-central and southeastern US**; **median age ~50s**; **male predominance (>57%)**. Geographic risk tracks *A. americanum* distribution and is expanding into suburban areas.

### 10. Diagnostics

- **Laboratory:** CBC (thrombocytopenia, leukopenia/lymphopenia, anemia), liver panel (elevated AST/ALT), sometimes hyponatremia (F004). LOINC-codable routine chemistries/hematology.
- **Direct detection:** **Whole-blood PCR** is the most useful acute test (F009); **peripheral blood smear** for intracytoplasmic **morulae** (diagnostic but ~38% sensitive; higher in immunocompromised) (F004, F008).
- **Serology:** IFA IgG on **paired acute + convalescent sera (≥4-fold rise)**; acute serology is insensitive (~55% seropositive at presentation in the anaplasmosis analog) (F009).
- **Diagnostic criteria:** CDC/CSTE case definitions (clinically compatible illness + laboratory confirmation by PCR, seroconversion, or morulae). **Differential diagnosis:** anaplasmosis, Rocky Mountain spotted fever/other rickettsioses, babesiosis, tularemia, viral syndromes, sepsis, leptospirosis, and other causes of febrile cytopenia. **Diagnostic gap:** provider awareness and PCR utilization remain low even in high-incidence areas ([PMID: 39983688](https://pubmed.ncbi.nlm.nih.gov/39983688/), [PMID: 42628341](https://pubmed.ncbi.nlm.nih.gov/42628341/)).
- **Not applicable:** genetic testing (WGS/WES/panels/karyotype/FISH/CMA/repeat expansion), newborn/carrier screening.

### 11. Outcome/Prognosis

With prompt doxycycline, prognosis is **excellent** and recovery typically complete (F004). Case-fatality for HME is roughly **1–3%** overall but higher in the elderly, immunocompromised, and those with delayed therapy. **Prognostic factors:** age, immunosuppression, time-to-treatment, and progression to shock/HLH. **Complications:** meningoencephalitis, ARDS, acute renal failure, DIC, secondary/opportunistic infections, and **secondary HLH** (a major driver of mortality; F012). Long-term musculoskeletal sequelae are **not** clearly associated with prior *Ehrlichia* infection ([PMID: 38206624]).

### 12. Treatment

- **First-line pharmacotherapy: doxycycline** (a tetracycline-class protein-synthesis inhibitor), highly efficacious and recommended for all ages including children, started empirically on suspicion (F004; NCIT:C299 "Doxycycline"). Typical adult dosing 100 mg BID; duration commonly 7–14 days or ≥3 days after defervescence.
- **Severe disease / HLH:** doxycycline **plus immunomodulation** — corticosteroids/dexamethasone (NCIT:C561), IVIG, and/or the IL-1 antagonist **anakinra** (F012). Supportive ICU care for shock/organ failure.
- **Pharmacogenomics:** not applicable.
- **Advanced/experimental therapeutics:** an **intracellular nanobody** against the T4SS effector inhibits infection in vitro — a proof-of-concept future therapeutic (F003). No gene, cell, RNA, or immune-checkpoint therapies apply.
- **Not applicable:** targeted oncologic therapies, surgery.

### 13. Prevention

- **Primary:** personal anti-tick measures — EPA-registered repellents, permethrin-treated clothing (93–97% repellency; "hot-foot" contact irritancy), protective clothing, and tick checks/showering after exposure (F007). Environmental/host-directed acaricide and deer-management strategies are adjuncts.
- **Secondary:** prompt recognition and empiric doxycycline in symptomatic exposed individuals (F009).
- **Tertiary:** early treatment and immunomodulation to prevent HLH/organ failure (F012).
- **Immunization:** **no human vaccine** (F007). A canine modified-live *phtcp*/Ech_0660 vaccine shows durable protection and could reduce the zoonotic reservoir/veterinary burden (F010).

### 14. Other Species / Natural Disease

Ehrlichiosis is fundamentally a **zoonosis with important natural animal disease** (F001, F011). **Dogs** develop **canine monocytic ehrlichiosis (CME)** from *E. canis* (transmitted by *Rhipicephalus sanguineus*), a globally distributed, sometimes severe illness with acute, subclinical, and chronic phases; *E. ewingii* and *E. chaffeensis* also infect dogs. **White-tailed deer** (*Odocoileus virginianus*, NCBI:txid9874) are the key *E. chaffeensis* reservoir and are largely subclinically infected. Goats and other ruminants host related agents (e.g., Panola Mountain *Ehrlichia*). **Zoonotic potential is central**: the same tick-maintained agents cross to humans. Comparative pathology: monocyte/macrophage tropism and morula formation are conserved across host species; the canine host importantly enables natural-infection vaccine testing.

### 15. Model Organisms

See F011. **Murine:** C57BL/6 mice + IOE or *E. muris* recapitulate fatal toxic-shock/immunopathology (excellent for immunity vs. immunopathology; limitation: uses surrogate *Ehrlichia* species rather than *E. chaffeensis*, which does not cause lethal disease in immunocompetent mice). **Natural-host models:** dog and white-tailed deer (best for tick-transmission and vaccine efficacy; limitation: cost, outbred variability). **In vitro:** DH82 canine macrophages (*E. chaffeensis*), HL-60 (granulocytic *Anaplasma*). **Genetic tools:** targeted mutagenesis now feasible in *E. chaffeensis* and *E. canis*, enabling attenuated-mutant vaccines (F010).

---

## Mechanistic Model / Interpretation

```
 Tick bite (A. americanum)                     [F001, F008]
        │ inoculates E. chaffeensis
        ▼
 Uptake by MONOCYTE/MACROPHAGE  →  cytoplasmic vacuole (MORULA)
        │
        ├─► TRP120 → ADAM17/Notch ┐
        │                          ├─ ↓TLR2/4, ↓autolysosome   [F002]
        ├─► Wnt–PI3K–mTOR ────────┘   = INNATE IMMUNE EVASION
        │
        └─► T4SS Etf-1 → autophagy + FERRITINOPHAGY            [F003]
                          = nutrient + IRON acquisition
        │
        ▼
 Bacterial replication → BONE MARROW / LIVER dysfunction
        │
        ▼
 CLINICAL TRIAD: fever + thrombocytopenia/leukopenia + ↑transaminases  [F004]
        │
        ├──────────────► BRANCH A (host controls infection)
        │                CD4+ Th1 / IFN-γ + antibody → CLEARANCE  [F010]
        │                (accelerated by DOXYCYCLINE)             [F004]
        │
        └──────────────► BRANCH B (dysregulated immunity)         [F005]
                         ↑TNF-α CD8+ T cells, ↓CD4+ Th1, ↑IL-10
                         + neutrophil-amplified injury
                                  │
                                  ▼
                         TOXIC-SHOCK-LIKE SYNDROME → SECONDARY HLH [F012]
                         (immunosuppressed / elderly / delayed Rx)
```

The unifying interpretation is a **two-phase pathogenesis**: an upstream, pathogen-driven phase of monocyte subversion (which sets bacterial burden) and a downstream, host-driven immunopathologic phase (which sets *severity*). This explains three clinical realities: (1) why the disease is an undifferentiated febrile cytopenia; (2) why severe outcomes cluster in the immunocompromised and elderly, in whom the CD4⁺ Th1/CD8⁺ balance is perturbed; and (3) why treatment of severe HLH cases pairs an antibiotic (doxycycline, reduces burden) with immunomodulation (dampens the pathogenic host response).

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [35763959](https://pubmed.ncbi.nlm.nih.gov/35763959/) | Agent, reservoir, vector, severity range (F001) | Genomic/epidemiologic |
| [15618141](https://pubmed.ncbi.nlm.nih.gov/15618141/) | Gram-negative obligate intracellular vacuolar biology; iron (F008) | In vitro/molecular |
| [14976527](https://pubmed.ncbi.nlm.nih.gov/14976527/) | Cell tropism (monocyte vs granulocyte morulae) (F008) | Human clinical |
| [27381289](https://pubmed.ncbi.nlm.nih.gov/27381289/) | TRP120–Notch immune evasion (F002) | In vitro |
| [28993455](https://pubmed.ncbi.nlm.nih.gov/28993455/) | Wnt-PI3K-mTOR autophagy block (F002) | In vitro |
| [34074773](https://pubmed.ncbi.nlm.nih.gov/34074773/) | Etf-1 ferritinophagy/iron robbery (F003) | In vitro |
| [7619983](https://pubmed.ncbi.nlm.nih.gov/7619983/) | Clinical/lab triad; doxycycline efficacy (F004) | Review/human clinical |
| [9200384](https://pubmed.ncbi.nlm.nih.gov/9200384/) | Pediatric HME phenotype frequencies (F004) | Human clinical |
| [14734762](https://pubmed.ncbi.nlm.nih.gov/14734762/) | TNF-α/CD8+ toxic-shock immunopathology; IOE model (F005, F011) | Model organism |
| [23478316](https://pubmed.ncbi.nlm.nih.gov/23478316/) | Neutrophils drive immunopathology (F005) | Model organism |
| [12860604](https://pubmed.ncbi.nlm.nih.gov/12860604/) | National incidence, age, sex (F006) | Surveillance |
| [34325087](https://pubmed.ncbi.nlm.nih.gov/34325087/) | Texas clustering, rising trend (F006) | Surveillance |
| [39631641](https://pubmed.ncbi.nlm.nih.gov/39631641/) | Acute serology insensitivity → PCR/paired sera (F009) | Human clinical |
| [35364518](https://pubmed.ncbi.nlm.nih.gov/35364518/) | Personal anti-tick prevention (F007) | Guideline/review |
| [33549976](https://pubmed.ncbi.nlm.nih.gov/33549976/) | No ehrlichiosis vaccine; Lyme vaccine won't cover (F007) | Review |
| [26841025](https://pubmed.ncbi.nlm.nih.gov/26841025/) | phtcp/Ech_0660 attenuated vaccine protects dogs (F010) | Model organism |
| [39826432](https://pubmed.ncbi.nlm.nih.gov/39826432/) | Durable 1-yr CD4+/antibody MLAV protection (F010) | Model organism |
| [27729288](https://pubmed.ncbi.nlm.nih.gov/27729288/) | Deer/dog natural-host tick-transmission models (F011) | Model organism |
| [32928497](https://pubmed.ncbi.nlm.nih.gov/32928497/) | HME as HLH trigger; misdiagnosis risk (F012) | Human clinical |
| [34595809](https://pubmed.ncbi.nlm.nih.gov/34595809/) | Ehrlichia-HLH in transplant recipient (F012) | Human clinical |

Supporting case literature for HLH management: [PMID: 42017727](https://pubmed.ncbi.nlm.nih.gov/42017727/) (doxycycline + dexamethasone), [PMID: 39790701](https://pubmed.ncbi.nlm.nih.gov/39790701/) (anakinra, IVIG), and [PMID: 37614269](https://pubmed.ncbi.nlm.nih.gov/37614269/) (progression despite doxycycline — illustrating the immunopathologic component). Diagnostic-gap evidence: [PMID: 39983688](https://pubmed.ncbi.nlm.nih.gov/39983688/) and [PMID: 42628341](https://pubmed.ncbi.nlm.nih.gov/42628341/).

---

## Limitations and Knowledge Gaps

1. **Species conflation.** Much "ehrlichiosis" literature (and this report's surveillance figures) intermixes HME, ewingii ehrlichiosis, and anaplasmosis (formerly HGE). Species-specific human incidence, prognosis, and immunology for *E. ewingii* and *E. muris* subsp. *eauclairensis* remain comparatively sparse.
2. **Human immunopathology is inferred.** The CD8⁺/TNF-α toxic-shock mechanism (F005) is robustly demonstrated in **murine surrogate models (IOE/E. muris)**; direct mechanistic confirmation in human severe HME/HLH tissue is limited. The strength of the mouse→human extrapolation is a genuine gap.
3. **No human omics profiling captured.** No patient-derived transcriptomic, proteomic, metabolomic, or single-cell datasets were located; molecular-profiling subsections are effectively "not available" for human disease.
4. **Precise human case-fatality and QoL metrics.** Standardized EQ-5D/SF-36 data are absent (5-/10-year survival metrics are inapplicable to an acute infection).
5. **Vaccine translation.** Protective-immunity and vaccine data (F010) are canine; no human vaccine candidate has entered trials.
6. **Diagnostic underuse.** PCR is underutilized even in endemic areas, so surveillance likely undercounts true incidence (F006, F009).

---

## Proposed Follow-up Experiments / Actions

1. **Human immunophenotyping of severe HME/HLH:** single-cell RNA-seq and cytokine profiling of blood/bone marrow from severe vs. mild human cases to test whether the murine CD8⁺-TNF-α/IL-10 axis (F005) operates in humans and to identify actionable immunomodulatory targets.
2. **Prospective PCR-anchored surveillance** in high-incidence, low-testing regions (e.g., NC, per [PMID: 39983688]) to obtain species-resolved incidence and case-fatality, correcting serology-based undercounting.
3. **Biomarker study for early severity/HLH prediction:** serial ferritin, TNF-α, IL-10, sCD25, and platelet trajectories to derive a bedside rule for when to add immunomodulation to doxycycline (informing F012 management).
4. **Therapeutic development of the anti-T4SS intracellular nanobody (F003):** advance from in-vitro proof-of-concept toward delivery-optimized preclinical testing as an adjunct for doxycycline-refractory disease.
5. **Human vaccine feasibility:** evaluate whether the attenuated *phtcp*/Ech_0660 platform (F010), proven in dogs, can be adapted or whether subunit approaches (TRP120, Etf-1, OMP-1/p28) elicit protective CD4⁺ Th1 responses; concurrently model whether canine vaccination reduces the enzootic reservoir and human spillover.
6. **Provider-education intervention trial** in endemic states to raise empiric-doxycycline uptake and PCR ordering, measuring impact on time-to-treatment and severe outcomes ([PMID: 42628341]).

---

*Report compiled from 12 confirmed findings across 5 investigation iterations and 52 reviewed papers. Ontology suggestions (MONDO, HPO, GO, CL, UBERON, NCIT, NCBI Taxon) are provided throughout for knowledge-base curation. Evidence types are labeled as human clinical, model organism, in vitro, or surveillance/review.*


## Artifacts

- [OpenScientist final report](Ehrlichiosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ehrlichiosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 31 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0016003` (4 mentions) - the report calls it "if available", "ehrlichiosis"; MONDO calls it **ehrlichiosis**
- `HP:0012047` (1 mention) - the report calls it "hemophagocytosis"; HP calls it **Hemeralopia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000775` (3 mentions) - the report calls it "neutrophil/granulocyte"; CL calls it **neutrophil**, and lists "neutrophil leucocyte" among its other names
- `GO:0020003` (2 mentions) - the report calls it "symbiont-containing vacuole", "symbiont-containing cytoplasmic vacuole/morula", "Subcellular level:** the **symbiont-containing cytoplasmic vacuole/morula"; GO calls it **symbiont-containing vacuole**
- `GO:0007219` (2 mentions) - the report calls it "Notch signaling pathway", "Notch signaling"; GO calls it **Notch signaling pathway**
- `GO:0006879` (2 mentions) - the report calls it "intracellular iron ion homeostasis", "iron homeostasis"; GO calls it **intracellular iron ion homeostasis**, and lists "iron homeostasis" among its other names
- `GO:0140355` (1 mention) - the report calls it "cargo receptor ligand activity, ferritinophagy"; GO calls it **cargo receptor ligand activity**
- `HP:0002910` (1 mention) - the report calls it "Elevated hepatic transaminase"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `HP:0001888` (1 mention) - the report calls it "Lymphopenia"; HP calls it **Decreased total lymphocyte count**, and lists "Lymphopenia" among its other names
- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `GO:0032640` (2 mentions) - the report calls it "tumor necrosis factor production", "TNF production"; GO calls it **tumor necrosis factor production**, and lists "TNF production" among its other names
- `HP:0011031` (1 mention) - the report calls it "abnormal iron/ferritin"; HP calls it **Abnormality of iron homeostasis**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0016003` - called "if available", "ehrlichiosis"
- `GO:0020003` - called "symbiont-containing vacuole", "symbiont-containing cytoplasmic vacuole/morula", "Subcellular level:** the **symbiont-containing cytoplasmic vacuole/morula"
- `GO:0007219` - called "Notch signaling pathway", "Notch signaling"
- `GO:0006879` - called "intracellular iron ion homeostasis", "iron homeostasis"
- `GO:0032640` - called "tumor necrosis factor production", "TNF production"
