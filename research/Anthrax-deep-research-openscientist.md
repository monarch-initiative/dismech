---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T20:09:04.938755'
end_time: '2026-09-24T20:18:14.126295'
duration_seconds: 549.19
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Anthrax
  mondo_id: MONDO:0005119
  category: Infectious Disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 8
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 48
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 23
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0005119
    reported_labels:
    - if available
    ontology_label: anthrax infection
  - term_id: HP:0011124
    reported_labels:
    - localized skin lesion
    ontology_label: Abnormal epidermal morphology
  - term_id: HP:0002090
    reported_labels:
    - fever
    ontology_label: Pneumonia
  - term_id: HP:0025267
    reported_labels:
    - nausea
    ontology_label: Snoring
  - term_id: HP:0011098
    reported_labels:
    - seizure
    ontology_label: Speech apraxia
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Anthrax-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Anthrax-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anthrax
- **MONDO ID:** MONDO:0005119 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Anthrax** covering all of the
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

# Anthrax — Comprehensive Disease Characteristics Report

**Disease:** Anthrax
**MONDO ID:** MONDO:0005119
**Category:** Infectious Disease (bacterial zoonosis)
**Causative agent:** *Bacillus anthracis* (NCBI:txid1392)

> **Evidence-source note:** Anthrax is an infectious/environmental disease, not a heritable human genetic disorder. Accordingly, sections framed around germline "causal genes," "pathogenic variants," "inheritance patterns," and "penetrance" of the *human* host are largely **Not applicable**; where genetics matters, it is (a) the pathogen's virulence genes/plasmids and (b) host receptor/immune genes influencing susceptibility. This is flagged throughout. Information is drawn from aggregated disease-level resources (CDC, WHO, OMIM/pathogen genomics, PubMed) rather than individual EHR patient records.

---

## 1. Disease Information

**Overview.** Anthrax is an acute bacterial zoonotic disease caused by the Gram-positive, spore-forming rod *Bacillus anthracis*. It principally affects herbivorous mammals (cattle, sheep, goats, wild ungulates); humans are incidental hosts infected by contact with infected animals, contaminated animal products (hides, wool, bone, meat), contaminated soil, or—rarely—deliberately released spores (bioterrorism). Disease manifests in four forms defined by the portal of entry: **cutaneous, gastrointestinal, inhalational (pulmonary), and injectional**. All forms can progress to systemic infection with bacteremia, toxemia, sepsis, and hemorrhagic meningitis (PMID: 38638828).

**Key identifiers.**
- **MONDO:** 0005119
- **ICD-11:** 1B97 (Anthrax); ICD-10: A22 (A22.0 cutaneous, A22.1 pulmonary, A22.2 gastrointestinal, A22.7 anthrax sepsis, A22.8, A22.9)
- **MeSH:** D000881 (Anthrax); Descriptor for organism *Bacillus anthracis* D001409
- **SNOMED CT:** 409498004 (Anthrax)
- **DOID:** DOID:7427
- **Pathogen taxonomy:** *Bacillus anthracis* NCBI:txid1392
- **OMIM/Orphanet:** No human Mendelian OMIM entry (infectious disease). Orphanet does not list anthrax as a rare genetic disease; related host receptor gene disorder: Hyaline Fibromatosis Syndrome (ANTXR2/CMG2, OMIM 228600) — see §4.

**Synonyms / alternative names.** Malignant pustule / malignant carbuncle (cutaneous form); woolsorters' disease / ragpickers' disease (inhalational, occupational); splenic fever; charbon; milzbrand; Siberian ulcer; injectional anthrax (heroin-associated).

**Data derivation.** Disease-level aggregated resources and published case series/surveillance, not individual-patient EHR.

---

## 2. Etiology

**Primary cause (infectious).** Infection by *Bacillus anthracis*. Environmentally persistent **endospores** are the infectious particle; they germinate to toxin-producing vegetative bacilli once inside a host. Full virulence requires **two plasmids**:
- **pXO1** (~182 kb) — encodes the three toxin components *pagA* (protective antigen, PA), *lef* (lethal factor, LF), *cya* (edema factor, EF) and the master regulator *atxA*.
- **pXO2** (~95 kb) — encodes the poly-γ-D-glutamic acid (PGA) capsule biosynthesis operon *capBCADE*.

Loss of either plasmid attenuates virulence; pXO1/*atxA* is required for intracellular macrophage escape and survival, pXO2 capsule for anti-phagocytic immune evasion (PMID: 11207600; PMID: 16334217).

**Risk factors (environmental / occupational — dominant).**
- Occupational contact with livestock and animal products: farmers, herders, veterinarians, butchers/abattoir workers, wool/hide/leather handlers, ("woolsorters"), bone-meal/tannery workers (PMID: 26720232 — cases concentrated in animal-husbandry workers and housewives with animal contact).
- Consumption of undercooked meat from infected animals (gastrointestinal/oropharyngeal form) (PMID: 29912259).
- Injection drug use with contaminated heroin (injectional anthrax — European outbreaks 2009–2010).
- Residence/work in endemic agricultural regions with poor veterinary-public-health infrastructure; contact with historical animal burial sites; warm-season and post-flood/drought soil disturbance.
- Laboratory exposure; intentional aerosol release (bioterrorism — e.g., 2001 U.S. "Amerithrax" letters; 1979 Sverdlovsk accidental release).
- Age/sex: cases skew to working-age adults with occupational exposure; male predominance in many series (e.g., 63% male, mean age ~44 y; PMID: 26720232).

**Host genetic susceptibility factors.** Not a classical genetic disease, but host genetics modulate toxin susceptibility: polymorphisms/expression of the toxin receptors **ANTXR1 (TEM8)** and **ANTXR2 (CMG2)** and downstream immune-signaling genes affect cellular sensitivity. Post-translational regulation (S-acylation cycles) of CMG2 controls receptor maturation and toxin susceptibility in vivo (PMID: 42409807). Inbred mouse strains differ in *Nlrp1b* inflammasome alleles that determine macrophage sensitivity to lethal toxin (model-organism evidence).

**Protective factors.**
- **Environmental/behavioral:** livestock vaccination, safe carcass disposal (no butchering of animals dying suddenly), thorough cooking of meat, PPE in at-risk occupations, decontamination of animal products.
- **Immunological/medical:** prior vaccination (anti-PA antibody), post-exposure prophylaxis (antibiotics ± vaccine).
- **Host genetic:** *Nlrp1b*-mediated inflammasome activation that triggers rapid pyroptosis of infected macrophages can be protective against lethal-toxin lethality in mice (context-dependent; model-organism evidence).

**Gene–environment interaction.** Spore exposure (environment) intersects with host receptor availability and inflammasome genotype (genetics): only germinated bacilli producing toxin cause disease, and the host's ANTXR2/CMG2 receptor density and Nlrp1b allele determine cellular outcome (toxicity vs pyroptotic clearance). Occupational exposure interacts with vaccination status to determine net risk.

---

## 3. Phenotypes

**Cutaneous anthrax (~95% of natural human cases).** *Type: clinical signs / physical manifestation.*
- Painless, pruritic papule → vesicle → **black necrotic eschar** ("malignant pustule") surrounded by non-pitting **gelatinous edema**; regional lymphadenopathy; low-grade fever/malaise. Incubation ~1–7 days (mean ~4.8 d; PMID: 26720232). Lesions most common on exposed hands/fingers/arms/face. Severity mild–moderate if treated; case-fatality ~20% untreated, <1% treated. HPO: HP:0000988 (skin rash), HP:0200041 (skin ulcer), HP:0011124 (localized skin lesion), HP:0000969 (edema), HP:0002090 (fever), HP:0002716 (lymphadenopathy).

**Inhalational anthrax (most lethal).** *Type: clinical signs + laboratory/imaging abnormalities.*
- Biphasic: nonspecific flu-like prodrome (fever, malaise, dry cough, myalgia) → fulminant phase with dyspnea, hypoxemia, **hemorrhagic mediastinitis with widened mediastinum**, pleural effusions, shock, meningitis. Progression subacute→fulminant over days; severity severe; historic mortality ~85–90%, ~45% with modern intensive care/antitoxin. HPO: HP:0002094 (dyspnea), HP:0002878 (respiratory failure), HP:0002090, HP:0100749 (chest pain), HP:0032263 (mediastinal mass/widening — pleural effusion HP:0002202).

**Gastrointestinal / oropharyngeal anthrax.** *Type: clinical signs.*
- Fever, severe abdominal pain, nausea/vomiting, **hematemesis**, bloody diarrhea, ascites, mesenteric adenopathy; oropharyngeal variant: throat pain, dysphagia, neck edema, oral ulcers. Severe; mortality ~25–60%. HPO: HP:0002240 (hepatomegaly/ascites HP:0001541), HP:0002573 (hematochezia), HP:0002013 (vomiting), HP:0002027 (abdominal pain), HP:0025267 (nausea).

**Injectional anthrax.** *Type: clinical signs.* Deep soft-tissue/necrotizing infection at injection site, marked edema without classic eschar, high rate of sepsis; associated with contaminated heroin. HPO: HP:0100806 (sepsis), HP:0000969.

**Systemic complications (any form).** Anthrax **sepsis/toxemia**, **hemorrhagic meningitis/meningoencephalitis** (poor prognosis), shock, coagulopathy. HPO: HP:0100806 (sepsis), HP:0001287 (meningitis), HP:0002315 (headache), HP:0001259 (coma), HP:0011098 (seizure).

**Quality-of-life impact.** Acute, high-acuity illness; survivors of cutaneous form may have scarring/contractures from eschars on hands. Severe systemic disease causes ICU-level morbidity, respiratory failure, neurological sequelae in meningitis survivors. No chronic relapsing phenotype (disease is acute/self-limited if survived).

---

## 4. Genetic / Molecular Information

**Human causal genes:** **Not applicable** — anthrax is not inherited. There are no human germline "causal genes," pathogenic ACMG/AMP variants, allele frequencies, or somatic/germline classifications for the disease itself.

**Pathogen virulence genes (the relevant "genetics"):**
| Gene | Plasmid | Product | Function |
|------|---------|---------|----------|
| *pagA* | pXO1 | Protective antigen (PA83) | Receptor binding + translocon; delivers LF/EF |
| *lef* | pXO1 | Lethal factor (LF) | Zn²⁺-metalloprotease; cleaves MAPKKs (MEK1/2/3/4/6/7), NLRP1 |
| *cya* | pXO1 | Edema factor (EF) | Calmodulin-dependent adenylate cyclase; ↑cAMP |
| *atxA* | pXO1 | AtxA | Master trans-activator of toxin + capsule genes |
| *capBCADE* | pXO2 | PGA capsule machinery | Poly-γ-D-glutamate anti-phagocytic capsule |
| *acpA/acpB* | pXO2 | Capsule regulators | Capsule expression control |

**Host genes relevant to susceptibility (host receptor / modifier genes):**
- **ANTXR2 / CMG2** (HGNC:21036; OMIM 608041) — **primary** anthrax toxin entry receptor; also a Collagen VI receptor for ECM homeostasis. Its loss-of-function mutations cause **Hyaline Fibromatosis Syndrome** (OMIM 228600) — a distinct human genetic disorder, notable because it reveals CMG2's dual physiological role and its regulation by S-acylation cycles that also control toxin susceptibility (PMID: 42409807).
- **ANTXR1 / TEM8** (HGNC:21014; OMIM 606410) — secondary/alternative toxin receptor; LOF causes GAPO syndrome and infantile hemangioma susceptibility (host disorders, not anthrax).
- **NLRP1** (inflammasome; direct LF substrate in rodents) — determines macrophage pyroptosis vs toxicity; a susceptibility modifier (strong in mouse, human NLRP1 also LF-responsive).

**Epigenetic / chromosomal features.** Not applicable to human host disease. Pathogen genome: single circular chromosome (~5.2 Mb) plus pXO1/pXO2; near-clonal population structure; typed by canonical SNPs and MLVA/VNTR (e.g., TaqMan/canSNP assays, PMID: 33371332).

---

## 5. Environmental Information

- **Environmental reservoir:** *B. anthracis* spores persist in soil for **decades**, favored by alkaline, calcium-rich soils and cycles of flooding/drought that concentrate spores; grazing animals ingest/inhale spores. Distribution modeling identifies host abundance, soil composition, climate, and vegetation as key determinants (PMID: 39509442).
- **Occupational exposures:** hides, wool, hair, bone meal, contaminated meat (see §2).
- **Lifestyle factors:** consumption of meat from animals that died suddenly; injection drug use.
- **Infectious agent:** *Bacillus anthracis* (NCBI:txid1392); Family Bacillaceae. Closely related to *B. cereus* group; distinguished by pXO1/pXO2 and phenotype (non-motile, non-hemolytic, penicillin-susceptible, gamma-phage susceptible).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Spore entry** through skin abrasion, ingestion, inhalation, or injection **leads to** deposition of dormant endospores in tissue.
2. Spores are **phagocytosed by local macrophages/dendritic cells** and transported toward regional lymph nodes; germination-triggering signals (amino acids, nucleosides) **result in** germination to vegetative bacilli.
3. Intracellular germinating bacilli, via **pXO1/atxA-dependent** functions, **escape the phagosome and survive/replicate**, then **lyse and exit the macrophage** (PMID: 11207600; PMID: 16334217).
4. Extracellular vegetative bacilli express the **pXO2 poly-γ-D-glutamate capsule**, which **inhibits phagocytosis and complement** → immune evasion → **unchecked bacteremia** (can reach 10⁷–10⁸ CFU/mL).
5. *atxA* activates **toxin gene expression**; PA83 binds host receptors **ANTXR2/CMG2 (primary)** and **ANTXR1/TEM8** (PMID: 42409807).
6. Cell-surface **furin cleaves PA83 → PA63** (releasing PA20); PA63 **oligomerizes into a heptamer/octamer prepore** that binds up to 3–4 molecules of LF and/or EF (PMID: 42600039).
7. Receptor-mediated **endocytosis** and endosomal acidification **convert the prepore to a membrane-spanning pore** (φ-clamp–gated translocase); LF and EF **translocate into the cytosol**.
8. **Branch A — Lethal toxin (PA+LF):** LF (Zn-metalloprotease) **cleaves MAPKKs (MEK1/2/3/4/6/7)** and activates/cleaves **NLRP1** → disrupts ERK/p38/JNK signaling → **impairs dendritic cell & macrophage function, endothelial dysfunction, and (in sensitive cells) pyroptosis/apoptosis** → **immune paralysis, vascular barrier failure, hypotensive shock**.
9. **Branch B — Edema toxin (PA+EF):** EF (Ca²⁺/calmodulin-dependent adenylate cyclase) **massively raises intracellular cAMP** → **fluid/electrolyte efflux and tissue edema**, impaired neutrophil function, further immune suppression.
10. Combined toxemia + bacteremia **result in** systemic inflammatory collapse: **capillary leak, hemorrhage, hypoxia, DIC-like coagulopathy, multi-organ failure**, and frequently **hemorrhagic meningitis** (bacterial/toxin CNS invasion) → **death**.

Upstream drivers = spore germination, plasmid-encoded capsule and toxins; downstream effectors = MAPKK cleavage, cAMP surge, endothelial/immune failure and shock. *(Steps 8–9 branch and converge on step 10.)*

**Molecular pathways:** MAPK/ERK, p38, JNK cascades (disrupted by LF); cAMP–PKA signaling (hyperactivated by EF); NLRP1 inflammasome; furin-mediated proprotein processing; receptor-mediated endocytosis. KEGG: ko05150-type bacterial pathways; Reactome anthrax-toxin entry.
**Cellular processes:** phagocytosis, phagosomal escape, pyroptosis/apoptosis, inflammasome activation, endothelial barrier dysfunction, immune suppression. GO: GO:0006909 (phagocytosis), GO:0070269 (pyroptosis), GO:0006954 (inflammatory response), GO:0000165 (MAPK cascade), GO:0071356 (cellular response to cytokine).
**Protein dysfunction:** host MAPKK proteolysis (loss of function of MEK signaling); pathological gain of adenylate-cyclase activity in cytosol; PA conformational activation/oligomerization is essential and drug-targetable (PMID: 42600039).
**Immune involvement:** capsule-mediated anti-phagocytosis; toxin-mediated suppression of innate and adaptive immunity; cytokine dysregulation; late overwhelming sepsis.
**Tissue-damage mechanisms:** hemorrhage, edema, necrosis, thrombosis, oxidative/ischemic injury from vascular collapse.
**GO/CL suggestions:** biological processes GO:0006954, GO:0000165, GO:0070269; cell types CL:0000235 (macrophage), CL:0000451 (dendritic cell), CL:0000115 (endothelial cell), CL:0000775 (neutrophil).

---

## 7. Anatomical Structures Affected

- **Organ level (primary, by form):** skin/dermis (cutaneous, UBERON:0002097 skin); lungs & **mediastinal lymph nodes** (inhalational — note primary lesion is hemorrhagic mediastinal lymphadenitis, not pneumonia; UBERON:0002048 lung, UBERON:0002509 mesenteric/UBERON:0000029 lymph node); GI tract — stomach/intestine/oropharynx (UBERON:0000160 intestine, UBERON:0000945 stomach).
- **Secondary / systemic:** blood (bacteremia; UBERON:0000178), spleen (UBERON:0002106; "splenic fever"), **meninges/brain** (hemorrhagic meningitis; UBERON:0002360 meninges, UBERON:0000955 brain), liver, adrenal glands, cardiovascular system (shock).
- **Body systems:** integumentary, respiratory, digestive, lymphatic/hematologic, cardiovascular, central nervous.
- **Tissue/cell level:** dermal connective tissue and vascular endothelium; alveolar and lymphatic macrophages; dendritic cells. Cell Ontology: CL:0000235 (macrophage), CL:0000451 (dendritic cell), CL:0000115 (endothelial cell), CL:0000775 (neutrophil).
- **Subcellular:** endosome/endolysosome (toxin translocation), plasma membrane (PA pore), cytosol (LF/EF targets), nucleus-linked MAPK signaling. GO CC: GO:0005768 (endosome), GO:0005886 (plasma membrane), GO:0005829 (cytosol).
- **Lateralization:** cutaneous lesions typically **unilateral/localized** at inoculation site; systemic disease is diffuse/bilateral (e.g., bilateral pleural effusions, symmetric mediastinal widening).

---

## 8. Temporal Development

- **Onset:** Incubation typically **1–7 days** (cutaneous mean ~4.8 d, PMID: 26720232); inhalational usually 1–7 days but can be delayed weeks (spore dormancy — up to ~43 days observed at Sverdlovsk). Any age; occupational cases in working-age adults. Onset pattern: **acute** (cutaneous) to **subacute→fulminant biphasic** (inhalational).
- **Progression / stages:** cutaneous — papule→vesicle→eschar over ~2–6 days, then healing over weeks. Inhalational — prodromal (flu-like) stage → fulminant systemic stage within 2–5 days; rapid deterioration once fulminant. Systemic sepsis/meningitis can kill within 24–72 h.
- **Course pattern:** **acute, self-limited if survived** (no chronic/relapsing course); untreated systemic disease is rapidly progressive.
- **Remission:** treatment-induced recovery with antibiotics ± antitoxin; cutaneous lesions heal with scar. No spontaneous chronic remission-relapse cycles.
- **Critical intervention window:** outcome hinges on **early antibiotic (and antitoxin) initiation before/at the fulminant toxemic phase**; post-exposure prophylaxis is most effective before symptom onset.

---

## 9. Inheritance and Population (Epidemiology)

- **Inheritance:** **Not applicable** (infectious disease; no Mendelian inheritance, penetrance, expressivity, anticipation, founder effect, carrier frequency, or consanguinity relevance for the host).
- **Global distribution:** worldwide but **endemic** in agricultural regions of sub-Saharan Africa, Central & South Asia, the Middle East, southern/eastern Europe (e.g., Türkiye), the Caucasus, and parts of Central/South America; hyperendemic where livestock vaccination is limited. Modeled suitable zones include central/eastern Türkiye, Armenia, Georgia, southern Russia, Bulgaria, Romania, Hungary, Moldova (PMID: 39509442). Rare/sporadic in most high-income countries.
- **Incidence/prevalence:** Human anthrax is rare and under-reported globally; WHO historically estimated on the order of thousands to ~tens of thousands of human cases per year worldwide, concentrated in endemic foci. It is a recognized but poorly quantified **neglected zoonotic disease** — prioritized in 65 countries yet with minimal formal burden estimates (PMID: 37545541). In endemic countries incidence is highly seasonal (warm months / post-rain) and occupational.
- **Demographics:** male predominance and working-age adults in occupational series (e.g., 63% male, mean age ~44 y, cases peaking Aug–Sep; PMID: 26720232). No ethnic genetic predisposition; distribution reflects exposure.
- **Sex ratio:** roughly male-skewed where occupational exposure dominates; broadly ~1:1–2:1 M:F by setting.

---

## 10. Diagnostics

- **Microbiology (gold standard):** Gram stain (large Gram-positive rods in chains, "boxcar" morphology, unencapsulated in culture / encapsulated in tissue with polychrome methylene blue **M'Fadyean** reaction), culture on sheep-blood agar (non-hemolytic, non-motile, catalase-positive, "medusa-head"/ground-glass colonies), gamma-phage lysis and penicillin susceptibility for confirmation. Blood cultures positive in systemic disease.
- **Molecular:** PCR/qPCR targeting plasmid markers (*pagA/lef* on pXO1, *capB* on pXO2) and chromosomal markers; multiplex **TaqMan** assays and canSNP/MLVA genotyping for strain typing (PMID: 33371332). **Metagenomic next-generation sequencing (mNGS)**, including from FFPE tissue, can confirm difficult cases rapidly (PMID: 38638828).
- **Immunoassays / biomarkers:** anti-PA IgG serology and toxin (PA/LF) detection assays (ELISA, mass-spectrometry LF activity assay — CDC); useful retrospectively and epidemiologically.
- **Histopathology:** skin biopsy — necrosis, edema, hemorrhage, vasculitis, PAS-positive/encapsulated bacilli (PMID: 38638828); tissues show hemorrhagic lymphadenitis/mediastinitis.
- **Imaging:** chest X-ray/CT — **widened mediastinum**, pleural effusions, hilar adenopathy (inhalational); abdominal imaging — ascites, bowel-wall edema (GI); CT/MRI + LP for hemorrhagic meningitis (CSF often hemorrhagic).
- **Diagnostic criteria:** clinical + exposure history + laboratory confirmation per CDC/WHO case definitions (confirmed vs probable/suspect).
- **Differential diagnosis:** cutaneous — spider bite, ecthyma gangrenosum, orf, tularemia, plague, staphylococcal/streptococcal cellulitis, rat-bite fever; inhalational — influenza, community-acquired pneumonia, mediastinitis, aortic dissection; GI — other bacterial gastroenteritis, acute abdomen.
- **Screening:** environmental/animal surveillance; no routine human population screening (rare disease). Genetic testing: not applicable.

---

## 11. Outcome / Prognosis

- **Cutaneous:** case-fatality **~20% untreated**, **<1% with antibiotics**; excellent prognosis if treated early (PMID: 26720232 series: 1.2% mortality overall, the single death from meningitis).
- **Gastrointestinal:** ~25–60% mortality depending on care/recognition.
- **Inhalational:** historically **~85–90%** mortality; **~45%** with modern ICU care, combination antibiotics, and antitoxin (2001 U.S. outbreak: 5/11 inhalational cases died despite treatment).
- **Injectional:** high morbidity/mortality (~30%+), often requiring surgical debridement.
- **Anthrax meningitis:** near-uniformly fatal without aggressive therapy; a leading cause of death across forms.
- **Prognostic factors:** clinical form and portal of entry; time to effective antibiotics/antitoxin; presence of meningitis, shock, pleural effusion; bacterial burden/toxemia; comorbidities. Early treatment before the fulminant toxemic phase is the strongest determinant of survival.
- **Morbidity/QoL:** survivors of severe systemic disease may have prolonged ICU recovery, respiratory compromise, and neurological deficits (post-meningitis); cutaneous scarring/contractures.

---

## 12. Treatment

**Antimicrobials (mainstay).**
- **Fluoroquinolones:** ciprofloxacin, levofloxacin (NCIT drug classes); first-line for treatment/PEP.
- **Tetracyclines:** doxycycline (first-line PEP/treatment).
- **Beta-lactams:** penicillin G / amoxicillin for penicillin-susceptible strains (naturally acquired often susceptible — PMID: 38638828 cured with IV penicillin; PMID: 26720232 penicillin group used in 78%); note intrinsic β-lactamase risk, so not for empiric bioterrorism use.
- **Others active:** clindamycin, linezolid (add for toxin/protein-synthesis suppression and CNS penetration), meropenem, rifampin, vancomycin.
- **Systemic/meningitis regimens:** CDC recommends **≥2–3 drug combination IV therapy** including a bactericidal agent (fluoroquinolone) + a protein-synthesis inhibitor (linezolid/clindamycin) + CNS-penetrant agent when meningitis is possible.
- **Duration:** systemic disease treated intravenously then oral; **inhalational/post-exposure prophylaxis requires 60 days** of oral antibiotics because of spore dormancy.

**Antitoxins (adjuncts for systemic disease — target PA).**
- **Raxibacumab** — human anti-PA monoclonal antibody (FDA-approved 2012).
- **Obiltoxaximab (ETI-204)** — anti-PA monoclonal (FDA-approved 2016).
- **Anthrax immune globulin (AIG, Anthrasil)** — polyclonal anti-PA from vaccinated donors.
These neutralize circulating toxin; used **with** antibiotics for systemic/severe anthrax. Next-generation ultrapotent anti-PA antibodies blocking PA63 oligomerization are in development (e.g., 22F1, IC50 = 0.027 nM; PMID: 42600039).

**Supportive / interventional care:** aggressive fluid/vasopressor support for shock, pleural fluid drainage (improves outcome by removing toxin-rich effusion), mechanical ventilation, surgical debridement (injectional/severe cutaneous — avoid excising uncomplicated eschars), corticosteroids for extensive head/neck edema or meningitis.

**Pharmacogenomics:** not a major factor; standard drug-metabolism considerations (e.g., CYP interactions with ciprofloxacin) apply.
**NCIT suggestions:** Ciprofloxacin (C2778), Doxycycline (C459), Penicillin (C739), Raxibacumab (C82675), Obiltoxaximab, Linezolid, Clindamycin, Anthrax Immune Globulin.

---

## 13. Prevention

- **Primary prevention:**
  - **Animal vaccination** (live attenuated **Sterne strain**, pXO1+/pXO2−) — cornerstone of control in livestock; reduces human exposure.
  - **Human vaccination:** **AVA / BioThrax** (Anthrax Vaccine Adsorbed, PA-based, adsorbed to aluminum hydroxide) and **AV7909 (Cyfendus)** (PA + CPG7909 adjuvant, approved for PEP). Recommended for at-risk occupations, certain military personnel, and lab workers. PA-based vaccines neutralize toxin but do **not** block spore germination/bacteremia, motivating multi-antigen and spore-antigen research (PMID: 18166249; PMID: 17005989).
  - **Behavioral/occupational:** PPE, safe handling/decontamination of animal products, proper carcass disposal (deep burial/incineration, no butchering of sudden-death animals), meat inspection, control of injection-drug spore contamination.
- **Secondary prevention:** rapid case detection and **post-exposure prophylaxis** — 60 days antibiotics (ciprofloxacin/doxycycline) **plus** a 3-dose vaccine series after confirmed aerosol exposure; environmental surveillance and decontamination after release.
- **Tertiary prevention:** early combination antibiotics + antitoxin to prevent progression to shock/meningitis; pleural drainage; ICU support.
- **Public health:** One-Health surveillance linking veterinary and human health, outbreak investigation, environmental decontamination (formaldehyde/chlorine dioxide for spores), education of at-risk communities (PMID: 40303149 — KAP gaps in endemic Ethiopia), biosecurity/select-agent regulation to prevent misuse.
- **Genetic counseling:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy of hosts:** primarily **herbivorous mammals** — cattle (*Bos taurus*, NCBI:txid9913), sheep (*Ovis aries*, txid9940), goats (*Capra hircus*, txid9925), horses (*Equus caballus*, txid9796), and wild ungulates (bison, deer, antelope, hippopotamus, elephants). Carnivores and omnivores (including humans, *Homo sapiens* txid9606) are more resistant and usually acquire via ingestion.
- **Natural disease / veterinary importance:** anthrax is a **major cause of sudden death in grazing livestock and wildlife**, with peracute presentation (sudden death, incomplete rigor, dark unclotted blood from orifices, splenomegaly). Devastating wildlife die-offs occur (e.g., savanna herbivores, hippos). It is a **notifiable/reportable** OIE (WOAH) disease of high economic and food-security impact (PMID: 39509442; OMIA resources).
- **Comparative pathology:** herbivores develop rapidly fatal septicemic anthrax; carnivores/humans show more localized/variable disease due to higher innate resistance — reflecting species differences in receptor biology and innate immunity (e.g., *Nlrp1* inflammasome variation across species/strains).
- **Zoonotic transmission:** all human cases derive from animals/animal products or environment; **no significant human-to-human transmission** (except rare cutaneous contact). Cross-species susceptibility is broad among mammals.

---

## 15. Model Organisms

- **Mice (*Mus musculus*, NCBI:txid10090):** the workhorse model for toxin action, vaccine/antitoxin efficacy, and inflammasome biology; inbred strains differ in **Nlrp1b** alleles governing macrophage sensitivity to lethal toxin. Recapitulate toxemia/lethality; used for PA-vaccine protection studies (PMID: 18166249; PMID: 17005989). Limitation: strain-dependent toxin sensitivity; not all reproduce human inhalational mediastinitis.
- **Rats:** classic model for **edema/lethal toxin lethality** (Fischer 344 rats highly sensitive to lethal toxin), useful for antitoxin pharmacology.
- **Rabbits (*Oryctolagus cuniculus*, txid9986) and non-human primates** (rhesus/cynomolgus macaques, *Macaca* spp.): **gold-standard inhalational anthrax models**; closely mimic human disease (mediastinal lymphadenitis, toxemia, meningitis) and are the basis for FDA "Animal Rule" licensure of vaccines/antitoxins.
- **Guinea pigs:** used for vaccine potency testing.
- **Zebrafish (*Danio rerio*, txid7955):** used to study CMG2/anthrax-toxin receptor biology and S-acylation-dependent toxin susceptibility in vivo; APT2 inhibition attenuated toxin toxicity (PMID: 42409807).
- **Cellular / in vitro:** J774A.1 and RAW264.7 macrophage lines for spore germination, intracellular survival, and pyroptosis assays (PMID: 11207600; PMID: 16334217); CHO and other lines for PA-pore translocation and receptor studies; engineered PA nanopores for biophysics (PMID: 42326671; PMID: 41520172).
- **Applications:** toxin mechanism, receptor/translocation biology, vaccine and antitoxin efficacy, inflammasome/host-defense genetics, therapeutic screening.
- **Resources:** MGI (mouse), RGD (rat), ZFIN (zebrafish), Cellosaurus/ATCC (cell lines); Alliance of Genome Resources.

---

## Evidence-Source Legend
- **Human clinical:** PMID 38638828, 26720232, 29912259, 36980364, 33371332, 39509442, 37545541, 40303149.
- **In vitro / molecular / structural:** PMID 42600039, 42409807, 42326671, 41520172, 42124355, 11207600, 16334217.
- **Model organism / vaccine:** PMID 18166249, 17005989, 42409807, 11207600.

## Limitations
- No primary dataset was provided; report synthesizes literature and canonical databases.
- Global human burden is poorly quantified (neglected zoonosis; under-reporting).
- Several therapeutic/mechanistic details (antitoxin approvals, CDC regimens, Animal Rule) rest on regulatory/guideline sources rather than the specific PMIDs retrievable in this session; PMIDs cited support the core mechanistic and clinical claims. Some retrieved records are recent structural/biophysical studies used to anchor the toxin-mechanism narrative.

## Future Directions
- Multi-antigen/spore-targeted vaccines that block germination and bacteremia (not only toxin).
- Next-generation ultrapotent anti-PA antibodies (oligomerization blockers, PMID 42600039) and small-molecule translocation inhibitors.
- Host-directed therapy exploiting receptor S-acylation cycles (PMID 42409807).
- Improved One-Health surveillance and burden quantification in endemic regions.


## Artifacts

- [OpenScientist final report](Anthrax-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Anthrax-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 31 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005119` (2 mentions) - the report calls it "if available"; MONDO calls it **anthrax infection**
- `HP:0011124` (1 mention) - the report calls it "localized skin lesion"; HP calls it **Abnormal epidermal morphology**
- `HP:0002090` (2 mentions) - the report calls it "fever"; HP calls it **Pneumonia**
- `HP:0025267` (1 mention) - the report calls it "nausea"; HP calls it **Snoring**
- `HP:0011098` (1 mention) - the report calls it "seizure"; HP calls it **Speech apraxia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0200041` (1 mention) - the report calls it "skin ulcer"; HP calls it **Skin erosion**
- `GO:0070269` (2 mentions) - the report calls it "pyroptosis"; GO calls it **pyroptotic inflammatory response**, and lists "pyroptosis" among its other names
- `GO:0071356` (1 mention) - the report calls it "cellular response to cytokine"; GO calls it **cellular response to tumor necrosis factor**, and lists "cellular response to TNF" among its other names
