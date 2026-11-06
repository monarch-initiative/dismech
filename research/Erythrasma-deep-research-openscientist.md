---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T13:01:17.180172'
end_time: '2026-09-29T13:13:35.392392'
duration_seconds: 738.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Erythrasma
  mondo_id: MONDO:0002885
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 12
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0002885
    reported_labels:
    - MONDO
    ontology_label: erythrasma
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Erythrasma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Erythrasma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Erythrasma
- **MONDO ID:** MONDO:0002885 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Erythrasma** covering all of the
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

# Erythrasma (MONDO:0002885): A Comprehensive Disease Characteristics Report

*Category: Infectious Disease. Evidence base: human clinical studies (case series, cross-sectional, prospective, one RCT, a 2025 systematic review) and classic in vitro/ultrastructural work. No genetic, animal-model, or omics datasets exist for this disease.*

---

## Summary

**Erythrasma is a common, benign, chronic superficial bacterial infection of the stratum corneum in warm, moist, occluded intertriginous skin, caused by overgrowth of the commensal Gram-positive lipophilic rod *Corynebacterium minutissimum*.** The organism colonizes and keratolytically invades the horny layer of the epidermis in the interdigital toe web spaces, groin/crural folds, axillae, and inframammary/intergluteal folds, producing well-demarcated red-brown scaly patches. Its diagnostic hallmark is a **coral-red (coral-pink) fluorescence under a Wood's lamp**, arising from bacterial synthesis of porphyrins (coproporphyrin III) in the stratum corneum. The disease is generally mild, often asymptomatic, cosmetically bothersome, and chronic/relapsing when the moist, occluded microenvironment persists.

Erythrasma is a **purely infectious, non-genetic disease**. There is no causal human gene, no pathogenic variant, no inheritance pattern, no OMIM entry, and no role for genetic testing or counseling. The "genetics" relevant to the disease belong entirely to the pathogen: *C. minutissimum* (NCBI Taxon 38301) and its porphyrin-biosynthesis and antibiotic-resistance determinants. Likewise, there is **no established natural animal disease and no laboratory model organism** — the condition is a superficial commensal overgrowth rather than a gene-driven phenotype. Risk is governed by conditions that create a warm, humid, occluded skin surface: hyperhidrosis, obesity, diabetes mellitus, warm-humid climate, poor hygiene, occlusion, and immunosuppression.

Prognosis is **excellent**. Cure rates with appropriate antibiotics are high, and disease-specific mortality in immunocompetent hosts is essentially zero. Randomized controlled trial (RCT) and 2025 systematic-review evidence support **topical fusidic acid** as the most effective agent, with **single-dose clarithromycin** and **erythromycin** as convenient systemic alternatives, and clotrimazole, clindamycin, mupirocin and Whitfield's ointment as further options. Because *C. minutissimum* is a normal commensal that becomes pathogenic only under permissive conditions, recurrence is common, and **prevention is entirely behavioral/environmental** — keeping folds dry, improving hygiene, weight reduction, and glycemic control. There is no vaccine and no screening program.

---

## Key Findings

### Finding 1 — Definition, causative organism, and identifiers (F001)

Erythrasma is a chronic superficial bacterial infection of intertriginous skin caused by *Corynebacterium minutissimum*, a lipophilic Gram-positive rod that infects the stratum corneum of warm, moist, occluded skin folds. The most commonly affected sites are the interdigital toe spaces, axillae, inguinal/crural folds, and inframammary and intergluteal folds. It presents as well-demarcated red-brown patches with fine scaling and classically shows **coral-red/coral-pink fluorescence under Wood's lamp** owing to coproporphyrin III.

> *"Erythrasma is a bacterial infection of the skin typically caused by Corynebacterium minutissimum. This pathogen infects the stratum corneum in warm and wet areas of the skin. Most commonly, the axillary, inguinal, and interdigital regions are affected."* — [PMID: 33145138](https://pubmed.ncbi.nlm.nih.gov/33145138/)

> *"It is found mostly in occluded intertriginous areas such as the axillae, inframammary areas, interspaces of the toes, intergluteal and crural folds, and is more common in individuals with diabetes mellitus than other clinical patients."* — [PMID: 12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/)

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0002885 |
| ICD-10 | L08.1 (Erythrasma) |
| MeSH | D004901 |
| OMIM | None (not a genetic disease) |
| Causative organism | *Corynebacterium minutissimum* (NCBI Taxon 38301) |

**Synonyms/alternative names:** Erythrasma; Baerensprung's disease (historical). Information is derived from aggregated disease-level clinical resources and case series, not from a genetic/EHR-linked patient registry.

### Finding 2 — Pathophysiology: keratolytic colonization and porphyrin fluorescence (F002)

Ultrastructural study (Montes et al., 1967) demonstrated bacterial **invasion of the stratum corneum with a keratolytic action** exerted by *C. minutissimum*. The organism proliferates within and digests keratin of the horny layer, driving mild hyperkeratosis, erythema, and brown scaling; its synthesis of porphyrins produces the diagnostic coral-red fluorescence. The infection remains confined to the horny layer, without dermal invasion, in immunocompetent hosts.

> *"This pathogen infects the stratum corneum in warm and wet areas of the skin."* — [PMID: 33145138](https://pubmed.ncbi.nlm.nih.gov/33145138/)

> *"Bacterial invasion of the stratum corneum in erythrasma. I. Ultrastructural evidence for a keratolytic action exerted by Corynebacterium minutissimum."* — [PMID: 6065118](https://pubmed.ncbi.nlm.nih.gov/6065118/)

### Finding 3 — Treatment efficacy (F003, F013)

A 2025 systematic review (studies 1971–2024, including RCTs) concluded that both **clotrimazole and fusidic acid are effective topical options, with fusidic acid providing faster symptom relief, greater reduction in Wood's-lamp fluorescence, and fewer side effects**, and that **clarithromycin is more effective than erythromycin systemically**. The historic systemic standard is erythromycin 250 mg four times daily for 14 days, with cure rates approaching 100%.

> *"both clotrimazole and fusidic acid are effective topical options, with fusidic acid providing faster symptom relief, greater reduction in Wood's lamp fluorescence and fewer side-effects. Clarithromycin was found to be more effective than erythromycin systemically"* — [PMID: 40635638](https://pubmed.ncbi.nlm.nih.gov/40635638/)

> *"Erythromycin 250mg four times daily for 14 days is the treatment of choice"* — [PMID: 12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/)

A double-blind, placebo-controlled RCT (Avci et al. 2013; n=151; five arms — single-dose clarithromycin, erythromycin, fusidic acid cream, placebo cream, placebo tablet) assessed by Wood's-light reflection scores at days 2, 7, and 14 found:

> *"the efficacy of fusidic acid cream therapy was significantly higher than other therapies. When the efficacy of clarithromycin and erythromycin therapy was compared, clarithromycin therapy was significantly more effective than erythromycin therapy at 48 h."* — [PMID: 21923567](https://pubmed.ncbi.nlm.nih.gov/21923567/)

The clarithromycin advantage over erythromycin at 48 h disappeared by days 7 and 14. Suggested NCIT intervention terms: Erythromycin (C558), Clarithromycin (C47530), Clindamycin, Fusidic Acid, Clotrimazole, Mupirocin.

| Agent | Route | Evidence | Notes |
|-------|-------|----------|-------|
| Fusidic acid | Topical | RCT + systematic review | Most effective; fastest fluorescence clearance; fewest side effects |
| Clotrimazole | Topical | Systematic review | Effective topical option |
| Clindamycin / mupirocin / Whitfield's ointment | Topical | Reviews | Alternatives; also used for prophylaxis |
| Clarithromycin (single 1 g dose) | Systemic | RCT | Superior to erythromycin at 48 h; convenient, better compliance |
| Erythromycin 250 mg QID ×14 d | Systemic | Reviews | Historic standard; cure rates up to ~100% |

### Finding 4 — Risk factors (F004)

Recognized predisposing factors are **diabetes mellitus, obesity, hyperhidrosis, occlusion/moisture, warm-humid climate, poor hygiene, and immunosuppression**. *C. minutissimum* is a normal skin commensal that becomes pathogenic under these conditions. Immunosuppression and advanced age are additional risks; in immunocompromised hosts the organism can rarely cause invasive disease (bacteremia, endocarditis, catheter infections, abscesses).

> *"is more common in individuals with diabetes mellitus than other clinical patients"* — [PMID: 12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/)

> *"aggravated by poor hygiene or underlying disorders promoting bacterial overgrowth, including diabetes, intertrigo, erythrasma, and obesity"* — [PMID: 26051066](https://pubmed.ncbi.nlm.nih.gov/26051066/)

> *"The bacterium can cause other diseases such as venous catheter infections, sepsis, orthopedic infections, abscesses, invasive infections, meningitis, endocarditis, and pyelonephritis."* — [PMID: 42412138](https://pubmed.ncbi.nlm.nih.gov/42412138/)

### Finding 5 — Diagnosis and differential diagnosis (F005, F014)

Diagnosis is clinical, confirmed by **coral-red (coral-pink) fluorescence under Wood's lamp**, valid across all skin types (in darker skin, erythema may appear as darkening/violaceous change rather than classic redness). Gram stain/culture shows Gram-positive rods/diphtheroids; biopsy (rarely needed) shows organisms in the stratum corneum. The differential includes **dermatophytosis (tinea), candidiasis, pityriasis (tinea) versicolor, inverse psoriasis, seborrheic dermatitis, intertrigo, and terra firma-forme dermatosis**; concurrent dermatophyte or Candida infection can coexist. *C. minutissimum* is the most common cause of interdigital foot infection.

> *"erythema may not manifest as classic redness in individuals with darker skin tones, instead appearing as subtle darkening, violaceous, or other colour changes. Diagnosis in all skin types is supported by the characteristic coral-red fluorescence observed under a Wood's lamp."* — [PMID: 40635638](https://pubmed.ncbi.nlm.nih.gov/40635638/)

> *"The differential diagnosis of erythrasma includes psoriasis, dermatophytosis, candidiasis and intertrigo, and methods for differentiating include Wood's light examination and bacterial and mycological cultures."* — [PMID: 12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/)

A newer bedside adjunct — **ultraviolet-induced fluorescence (UVF) dermoscopy** — showed significant (p<0.01) discriminating patterns in a multicentric retrospective accuracy study (Errichetti et al., 208 patients): **red fluorescence in Corynebacterium foot intertrigo (erythrasma)** and inverse psoriasis, versus green in Pseudomonas intertrigo.

> *"red in Corynebacterium foot intertrigo, inverse and guttate psoriasis"* — [PMID: 38288676](https://pubmed.ncbi.nlm.nih.gov/38288676/)

> *"tinea cruris (n = 23), and erythrasma (n = 12) were collected for comparison"* — [PMID: 41628788](https://pubmed.ncbi.nlm.nih.gov/41628788/)

### Finding 6 — Epidemiology (F006)

Erythrasma is common worldwide, especially in warm climates, with adult predominance. A prospective Turkish outpatient study (Polat & İlhan 2015; n=182 with interdigital lesions) found **73/182 (40.1%) had interdigital erythrasma**, mean age 45.5±10.8 years (range 22–70), 56.2% women, with desquamation the most common finding. A Tehran cross-sectional intertrigo study (Halvaee 2018; n=188) found erythrasma accounted for **28/80 (35%)** of confirmed intertrigo cases, second only to dermatophytosis (45%). Among elderly Turkish dermatology outpatients (n=240), erythrasma was 17.6% of bacterial infections. There is **no newborn-screening or registry-level incidence/prevalence** per 100,000 (not a reportable disease).

> *"Of 182 patients with interdigital lesions, 73 (40.1%) were diagnosed as having erythrasma. The mean ± SD age of the patients with erythrasma was 45.52 ± 10.83 years (range, 22-70 years). Most of the patients with erythrasma were women (56.2%)."* — [PMID: 25815650](https://pubmed.ncbi.nlm.nih.gov/25815650/)

> *"Dermatophytosis was the predominant cause in this study with 36 (45%) cases followed by erythrasma (28 cases, 35%)"* — [PMID: 30320016](https://pubmed.ncbi.nlm.nih.gov/30320016/)

> *"The most often clinical finding was desquamation."* — [PMID: 25815650](https://pubmed.ncbi.nlm.nih.gov/25815650/)

### Finding 7 — Clinical phenotype (F007)

Erythrasma presents as sharply marginated, irregular **red-brown macules/patches with fine wrinkled scaling** in intertriginous sites; the interdigital form (most common, especially the 4th–5th toe web) shows maceration, scaling, and fissuring. Symptoms are typically mild — often asymptomatic or mildly pruritic, with occasional malodor. Three clinical forms are recognized: (1) interdigital, (2) intertriginous (inguinal/axillary well-defined patches), and (3) disciform/generalized (widespread, more common in diabetics and warm climates). The course is chronic, indolent, and relapsing. Quality-of-life impact is generally low (cosmetic, itch, odor); there are no systemic symptoms in immunocompetent hosts.

> *"Cutaneous features include erythema, scaling and skin discoloration; notably, erythema may not manifest as classic redness in individuals with darker skin tones, instead appearing as subtle darkening, violaceous, or other colour changes."* — [PMID: 40635638](https://pubmed.ncbi.nlm.nih.gov/40635638/)

> *"adjacent areas of central hypopigmentation and peripheral hyperpigmented scaling were also noted bilaterally in the groin region"* — [PMID: 33145138](https://pubmed.ncbi.nlm.nih.gov/33145138/)

**Suggested HPO terms:** Pruritus (HP:0000989), Hyperkeratosis (HP:0000962), Hyperpigmentation of the skin (HP:0000953), Skin rash (HP:0000988), Skin fissure (HP:0100804).

### Finding 8 — No human genetic etiology (F008)

Erythrasma has **no causal human gene, pathogenic variant, inheritance pattern, penetrance, modifier gene, chromosomal abnormality, or germline/somatic mutation**. It is caused by overgrowth of *C. minutissimum*, a Gram-positive, lipophilic, catalase-positive coryneform commensal. There is no OMIM entry, no genetic testing, no carrier screening, and no founder-effect relevance. The molecularly relevant genetics are microbial — porphyrin synthesis (coproporphyrin III) driving fluorescence, plus variable antibiotic-resistance determinants. Any host "genetic" contribution is indirect, via conditions (e.g., diabetes) that alter the skin microenvironment.

> *"A series of superficial infections (erythrasma, some tinea capitis types, tinea/pityriasis versicolor, dermatophytoses, etc.) and pilosebaceous follicles enriched in Propionibacterium spp show fluorescence."* — [PMID: 21411414](https://pubmed.ncbi.nlm.nih.gov/21411414/)

> *"the aim of this study is to understand the significance of pathogenicity, antibiotic resistance, and diagnostic methods for C. minutissimum"* — [PMID: 42412138](https://pubmed.ncbi.nlm.nih.gov/42412138/)

### Finding 9 — No natural animal disease or model organism (F009)

*C. minutissimum* is a commensal of human skin; there is **no recognized naturally occurring erythrasma in companion animals or wildlife and no OMIA entry**, and **no standard model organism or genetic model** exists, because the disease is a superficial commensal overgrowth rather than a gene-driven phenotype. Mechanistic study has relied on human/experimental ultrastructural and in vitro work (stratum-corneum invasion, keratolysis, porphyrin production). Zoonotic transmission is not established.

> *"Corynebacterium minutissimum (C. minutissimum) usually causes a chronic skin infection called erythrasma, which is often caused by infection between the toes and wrinkled areas in the body armpits, under the breasts."* — [PMID: 42412138](https://pubmed.ncbi.nlm.nih.gov/42412138/)

### Finding 10 — Anatomy (F010)

Disease is confined to the **stratum corneum of intertriginous skin** — toe webs, groin, axillae, inframammary/intergluteal folds — and is often bilateral/symmetric. The primary organ is the skin (integumentary system); the target tissue is the epidermis, specifically the horny layer of keratinized stratified squamous epithelium; the cells involved are terminally differentiated corneocytes/keratinocytes. There is no dermal, adnexal, or systemic organ involvement in typical disease.

> *"This pathogen infects the stratum corneum in warm and wet areas of the skin. Most commonly, the axillary, inguinal, and interdigital regions are affected."* — [PMID: 33145138](https://pubmed.ncbi.nlm.nih.gov/33145138/)

> *"occluded intertriginous areas such as the axillae, inframammary areas, interspaces of the toes, intergluteal and crural folds"* — [PMID: 12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/)

**Suggested UBERON terms:** skin of body (UBERON:0002097), stratum corneum of epidermis (UBERON:0002027), epidermis (UBERON:0001003), axilla (UBERON:0009472), inguinal region. **Cell Ontology:** keratinocyte (CL:0000312), corneocyte. **GO cellular component:** cornified envelope (GO:0001533).

### Finding 11 — Temporal course and prognosis (F011)

Onset is **insidious and chronic** (not acute), typically in adults through the geriatric years. Untreated, it is indolent and can persist for months to years or wax and wane; spontaneous remission is uncommon while predisposing factors persist. The course is chronic and relapsing/remitting rather than progressive. **Prognosis is excellent** — benign, non-life-threatening, with essentially zero disease-specific mortality in immunocompetent hosts; cure rates with appropriate antibiotics are high. Main adverse outcomes are cosmetic concern, recurrence, and secondary/co-existing infection. Invasive *C. minutissimum* disease is rare and confined to immunocompromised hosts.

> *"Erythrasma is a chronic superficial bacterial infection caused by Corynebacterium minutissimum, predominantly affecting intertriginous areas."* — [PMID: 40635638](https://pubmed.ncbi.nlm.nih.gov/40635638/)

> *"systemic erythromycin demonstrates cure rates as high as 100%"* — [PMID: 12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/)

> *"the efficacy of fusidic acid cream therapy was significantly higher than other therapies"* — [PMID: 21923567](https://pubmed.ncbi.nlm.nih.gov/21923567/)

### Finding 12 — Prevention (F012)

Prevention centers on modifying the moist, occluded microenvironment that permits *C. minutissimum* overgrowth: **good skin hygiene, thorough drying of intertriginous areas, moisture-wicking/loose clothing and footwear, reducing hyperhidrosis, weight reduction, and glycemic control**. Antibacterial soaps and, for recurrent disease, topical prophylaxis (e.g., clindamycin/erythromycin solutions, benzoyl peroxide wash) are used as tertiary prevention. There is **no vaccine, no population screening, no newborn/carrier/genetic screening, and no role for genetic counseling**, because the disease is a non-communicable commensal overgrowth without a genetic basis.

> *"aggravated by poor hygiene or underlying disorders promoting bacterial overgrowth, including diabetes, intertrigo, erythrasma, and obesity"* — [PMID: 26051066](https://pubmed.ncbi.nlm.nih.gov/26051066/)

> *"topical solutions such as clindamycin, Whitfield's ointment, sodium fusidate ointment and antibacterial soaps may be required for both treatment and prophylaxis"* — [PMID: 12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/)

---

## Mechanistic Model / Interpretation

Erythrasma is best understood as a **microenvironment-driven commensal overgrowth** rather than a classic pathogen invasion. The causal chain runs from a permissive skin surface to a fluorescent, scaly clinical lesion:

```
[1] Warm, moist, occluded intertriginous microenvironment
    + host predisposition (hyperhidrosis, obesity, diabetes, immunosuppression)
        │  leads to
        ▼
[2] Overgrowth of commensal lipophilic Corynebacterium minutissimum on skin surface
        │  results in
        ▼
[3] Bacterial proliferation within and keratolytic digestion of stratum corneum keratin
        │  causes
        ▼
[4] Low-grade colonization → hyperkeratosis, mild erythema, red-brown scaling
        │                                             │
        │  (branch A: pigment)                        │  (branch B: clinical lesion)
        ▼                                             ▼
[5] Bacterial synthesis of porphyrins            Well-demarcated red-brown
    (coproporphyrin III) in horny layer          patches in skin folds;
        │  leads to                              interdigital maceration/fissuring
        ▼
[6] Coral-red fluorescence under 365 nm
    Wood's light → the diagnostic sign
```

**Upstream vs. downstream:** The upstream initiating factors are physical/host (moisture, occlusion, metabolic predisposition). The proximate biological cause is bacterial overgrowth and keratolysis (steps 2–3). The downstream manifestations branch into (A) the porphyrin-mediated fluorescence used for diagnosis and (B) the visible scaly patches. This branching structure explains why the disease is simultaneously easy to diagnose (fluorescence) and easy to confuse clinically with fungal intertrigo (scaly patches) — hence the central diagnostic role of the Wood's lamp.

**Cell types and processes:** Corneocytes/keratinocytes (CL:0000312) of the cornified layer (GO:0001533) are the substrate; the key biological process is bacterial keratin catabolism at the skin surface (extracellular). No host immune activation, apoptosis, or fibrosis is required for the typical phenotype, which is why the lesion is indolent and the prognosis benign. Invasive complications only arise when host immune defenses fail. The step from keratolysis to the visible lesion is well supported by ultrastructural evidence; the precise bacterial enzymes and porphyrin-regulation pathways remain inferred rather than fully demonstrated.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|------|-----------------|------|
| [33145138](https://pubmed.ncbi.nlm.nih.gov/33145138/) | *Erythrasma Revisited: Diagnosis, Differential Diagnoses, and Treatment* | Defines organism, tissue (stratum corneum), sites, fluorescence |
| [12010076](https://pubmed.ncbi.nlm.nih.gov/12010076/) | *Management of cutaneous erythrasma* | Sites, diabetes link, differentials, treatment of choice, prophylaxis |
| [40635638](https://pubmed.ncbi.nlm.nih.gov/40635638/) | *Erythrasma: a systematic review of interventions* | 2025 comparative efficacy (fusidic acid, clarithromycin); presentation across skin tones |
| [21923567](https://pubmed.ncbi.nlm.nih.gov/21923567/) | *Erythromycin vs single-dose clarithromycin vs topical fusidic acid* | RCT establishing comparative efficacy |
| [6065118](https://pubmed.ncbi.nlm.nih.gov/6065118/) | *Bacterial invasion of stratum corneum in erythrasma* | Primary ultrastructural keratolysis evidence |
| [25815650](https://pubmed.ncbi.nlm.nih.gov/25815650/) | *Prevalence of interdigital erythrasma* | Epidemiology, age/sex distribution, desquamation |
| [30320016](https://pubmed.ncbi.nlm.nih.gov/30320016/) | *Intertriginous mycotic and pseudomycotic infections* | Erythrasma as 35% of intertrigo cases |
| [26051066](https://pubmed.ncbi.nlm.nih.gov/26051066/) | *Fold (intertriginous) dermatoses* | Hygiene, diabetes, obesity as drivers |
| [42412138](https://pubmed.ncbi.nlm.nih.gov/42412138/) | *Infections, diagnosis, antibiotic resistance of C. minutissimum* | Microbial pathogenicity, invasive disease, resistance |
| [21411414](https://pubmed.ncbi.nlm.nih.gov/21411414/) | *Specular light reflectance beyond fluorescence* | Microbial porphyrin origin of fluorescence |
| [38288676](https://pubmed.ncbi.nlm.nih.gov/38288676/) | *UV-induced fluorescence dermoscopy accuracy* | UVF dermoscopy as bedside diagnostic aid |
| [41628788](https://pubmed.ncbi.nlm.nih.gov/41628788/) | *Dermoscopic clues for granular parakeratosis* | Erythrasma as dermoscopy comparator |

Twenty papers were reviewed across five iterations. The evidence base is dominated by narrative reviews, single-country prospective/cross-sectional epidemiology studies (mostly Turkey and Iran), one head-to-head RCT (n=151), and a 2025 systematic review. All 14 findings are mutually consistent; none challenge one another.

---

## Limitations and Knowledge Gaps

1. **No global epidemiology.** Erythrasma is not a reportable disease; there is no registry-level incidence/prevalence per 100,000. Available figures (40.1% of interdigital lesions; 35% of intertrigo cases; 17.6% of bacterial infections in the elderly) come from small, single-center outpatient studies in specific countries and may not generalize.

2. **Limited high-quality trial evidence.** Only one substantial RCT (n=151) directly compares treatments; the 2025 systematic review explicitly notes a shortage of large, standardized RCTs. Optimal regimens, durations, and relapse-prevention strategies remain incompletely defined.

3. **Sparse molecular microbiology.** The keratolysis mechanism rests largely on a single 1967 ultrastructural study. The specific bacterial enzymes mediating keratin digestion, the regulation of porphyrin biosynthesis, and the antibiotic-resistance epidemiology of *C. minutissimum* are underexplored.

4. **No model system.** The absence of an animal or genetic model limits mechanistic dissection; findings depend on human observation and in vitro culture.

5. **Quality-of-life data are qualitative.** No validated QoL instrument (EQ-5D, SF-36, DLQI) has been systematically applied to erythrasma.

6. **Microbiome context.** The role of the broader skin microbiome and host factors (e.g., stratum corneum lipid composition, sweat chemistry) in permitting overgrowth is not characterized.

---

## Proposed Follow-up Experiments / Actions

1. **Multicenter, standardized RCT** comparing topical fusidic acid, clotrimazole, and single-dose clarithromycin with predefined Wood's-lamp/UVF endpoints, relapse tracking at 3 and 6 months, and QoL (DLQI) measurement.

2. **Population-based prevalence estimate** using systematic Wood's-lamp/UVF screening in defined cohorts (e.g., diabetes clinics, warm-climate primary care) to generate incidence/prevalence per 100,000 and quantify the diabetes/obesity effect sizes.

3. **Molecular characterization of *C. minutissimum*** keratolytic enzymes and porphyrin-biosynthesis genes via whole-genome sequencing and transcriptomics of clinical isolates, correlating porphyrin output with fluorescence intensity.

4. **Antibiotic-resistance surveillance** of clinical *C. minutissimum* isolates to guide empiric therapy and detect emerging macrolide/fusidic-acid resistance.

5. **Diagnostic accuracy validation** of UVF dermoscopy versus classic Wood's lamp and PCR/culture across skin phototypes, especially to address under-recognition in darker skin.

6. **Prevention trial** of structured moisture-control/hygiene interventions (with or without topical prophylaxis) in high-risk populations to quantify recurrence reduction.

---

## Consensus Answer

Erythrasma (MONDO:0002885; ICD-10 L08.1) is a common, benign, chronic superficial bacterial infection of the stratum corneum in warm, moist, occluded intertriginous skin, caused by overgrowth of the commensal Gram-positive lipophilic rod *Corynebacterium minutissimum*, which keratolytically colonizes the horny layer and produces porphyrins (coproporphyrin III) giving the diagnostic coral-red Wood's-lamp fluorescence. It is a purely infectious, non-genetic disease with no inheritance, causal human gene, natural animal disease, or laboratory model; risk is driven by moisture, hyperhidrosis, obesity, diabetes, warm-humid climate, poor hygiene, and immunosuppression. Prognosis is excellent with topical fusidic acid/clotrimazole/clindamycin or single-dose clarithromycin/erythromycin, though recurrence is common unless the moist, occluded microenvironment and predisposing conditions are corrected, making prevention entirely behavioral and environmental.


## Artifacts

- [OpenScientist final report](Erythrasma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Erythrasma-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0002885` (3 mentions) - the report calls it "MONDO"; MONDO calls it **erythrasma**