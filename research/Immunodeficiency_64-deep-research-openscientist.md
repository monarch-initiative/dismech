---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T18:32:04.295766'
end_time: '2026-08-30T19:01:14.645915'
duration_seconds: 1750.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 64
  mondo_id: ''
  category: Immunodeficiency
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
citation_count: 22
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 16
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0012177
    reported_labels:
    - Decreased proportion of NK cells
    ontology_label: Abnormal natural killer cell physiology
  - term_id: GO:0005768
    reported_labels:
    - endosome; RasGRP1 trafficking
    ontology_label: endosome
  - term_id: NCIT:C15329
    reported_labels:
    - Immunosuppressive Therapy
    ontology_label: Surgical Procedure
  - term_id: NCIT:C579
    reported_labels:
    - Immunoglobulin Therapy
    ontology_label: Inorganic Chemical
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_64-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_64-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 64
- **MONDO ID:**  (if available)
- **Category:** Immunodeficiency

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 64** covering all of the
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

# Immunodeficiency 64 (IMD64 / RASGRP1 Deficiency): Comprehensive Disease Characteristics Report

## Summary

**Immunodeficiency 64 (IMD64; OMIM #618534; MONDO:0030926)** is an ultra-rare autosomal-recessive **combined immunodeficiency with immune dysregulation** caused by biallelic loss-of-function (LOF) mutations in **RASGRP1** (RAS guanyl-releasing protein 1; HGNC:9866; gene locus 15q14). RASGRP1 is a calcium- and diacylglycerol (DAG)-regulated RAS guanine-nucleotide exchange factor (RasGEF) that couples the T-cell receptor (TCR) — and other antigen receptors — to the **RAS–RAF–MEK–ERK/MAPK** signaling cascade. In the resting state the protein is held in an autoinhibited conformation; TCR engagement generates Ca²⁺ and DAG signals that relieve autoinhibition and switch on RAS. When both alleles are non-functional, this switch fails: thymocyte selection, lymphocyte proliferation, activation and motility, and natural-killer (NK)-cell cytotoxicity are all impaired, and — critically — cytotoxic CD8⁺ T cells cannot control Epstein–Barr-virus (EBV)-infected B cells.

Clinically, IMD64 presents in childhood with **recurrent/severe infections (reported in 100% of cases), non-malignant lymphoproliferation (~87%), autoimmunity, and a strong predisposition to EBV-driven B-cell lymphoproliferative disease and lymphoma** (both Hodgkin and non-Hodgkin). Autoimmune manifestations range from cytopenias (notably autoimmune hemolytic anemia) to an **emerging, potentially fatal vasculopathy**. The disease is defined at the disease level from aggregated case reports and small cohorts (~15 reported patients worldwide), not from large EHR datasets. Allogeneic **hematopoietic stem cell transplantation (HSCT) remains the only curative therapy**; conservative management carries high mortality. Mechanism-based experimental options — most notably **lenalidomide**, which restores RhoA activity and reverses migration/activation defects in patient lymphocytes — have been reported.

This report synthesizes six confirmed findings and 28 reviewed papers into a full disease knowledge-base entry, organized by the 15 requested sections. Where information is unavailable or not applicable for this ultra-rare monogenic disorder (e.g., cancer-style survival curves, veterinary natural disease), this is stated explicitly.

---

## Key Findings

### Finding 1 — IMD64 is caused by biallelic loss-of-function RASGRP1 mutations that impair RAS–MAPK/ERK signaling

Homozygosity mapping plus exome sequencing in a consanguineous family identified a **biallelic stop-gain variant in RASGRP1** that segregated perfectly with disease. Functionally, RASGRP1 deficiency reduced **phosphorylation of ERK** in both T and B cells, and this defect was **rescued by re-expression of wild-type RASGRP1**, establishing causality and the molecular mechanism (Salzer et al., 2016). This was independently confirmed by Somekh et al. (2018), who identified **two additional novel LOF mutations** and demonstrated, using immunoblotting and active-RAS pull-down assays, **perturbed ERK1/2 signaling and reduced RAS-GTPase activity** in a Jurkat model.

> *"we used homozygosity mapping and exome sequencing to identify a biallelic stop-gain variant in RASGRP1. This variant segregated perfectly with the disease"* — [PMID: 27776107](https://pubmed.ncbi.nlm.nih.gov/27776107/)

> *"RASGRP1 deficiency was associated in T cells and B cells with decreased phosphorylation of the extracellular-signal-regulated serine kinase ERK, which was restored following expression of wild-type RASGRP1"* — [PMID: 27776107](https://pubmed.ncbi.nlm.nih.gov/27776107/)

> *"Genetic screening identified two novel loss-of-function mutations in RASGRP1. Immunoblotting and active Ras pull-down assays confirmed perturbed ERK1/2 signaling and reduced Ras-GTPase activity"* — [PMID: 30030704](https://pubmed.ncbi.nlm.nih.gov/30030704/)

**Interpretation:** The genetic lesion is a bona-fide autosomal-recessive LOF defect, and the downstream consequence — collapse of TCR→RAS→ERK signaling — is the proximate biochemical cause of the immune phenotype.

### Finding 2 — RASGRP1 deficiency causes EBV-driven lymphoproliferation and lymphoma via defective cytotoxic T-cell control of infected B cells

Patient T cells show **severe activation defects that result in uncontrolled EBV-induced B-cell proliferation** (Mansour et al., 2023). Somekh et al. (2018) described patients with immunodeficiency and **EBV-associated lymphoproliferative disease and susceptibility to EBV-induced B-cell malignancies**. Mechanistically, Latour & Fischer (2019) group RASGRP1 with **MAGT1 and ITK** as genes whose mutation causes **defective expansion of EBV-specific CD8⁺ T cells** and impaired elimination of proliferating EBV-infected B cells.

> *"T cells from the patient showed severe activation defects resulting in uncontrolled Epstein-Bar Virus-induced B cell proliferation"* — [PMID: 37898412](https://pubmed.ncbi.nlm.nih.gov/37898412/)

> *"the defective expansion of EBV-specific CD8 T cells results from mutations in genes involved in T-cell activation (such as RASGRP1, MAGT1, and ITK)"* — [PMID: 31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/)

> *"RASGRP1 deficiency is associated with life-threatening immune dysregulation, severe autoimmune manifestations, and susceptibility to EBV-induced B cell malignancies"* — [PMID: 30030704](https://pubmed.ncbi.nlm.nih.gov/30030704/)

**Interpretation:** EBV susceptibility is not incidental; it is a direct, mechanistically predictable consequence of impaired TCR-driven CD8⁺ effector expansion. This places IMD64 firmly within the family of **inborn errors of immunity predisposing to EBV lymphoproliferation** (alongside XLP1/SH2D1A, XLP2/XIAP, ITK, MAGT1, CD27, CD70, CTPS1, CORO1A).

### Finding 3 — RASGRP1 links TCR signaling to cytoskeletal dynamics via DYNLL1; the NK-cytotoxicity defect is reversible by lenalidomide

Beyond ERK, RASGRP1 deficiency causes **defective proliferation, activation and motility** of T and B cells, and **impaired NK-cell cytotoxicity with defective granule convergence and actin accumulation**. Interaction proteomics identified the **dynein light chain DYNLL1** as a RASGRP1 interactor, linking RASGRP1 to cytoskeletal dynamics. Deficient cells showed **decreased RhoA GTPase activation**, and treatment with **lenalidomide increased RhoA activity and reversed the migration and activation defects** (Salzer et al., 2016).

> *"RASGRP1-deficient natural killer (NK) cells exhibited impaired cytotoxicity with defective granule convergence and actin accumulation. Interaction proteomics identified the dynein light chain DYNLL1 as interacting with RASGRP1, which links RASGRP1 to cytoskeletal dynamics"* — [PMID: 27776107](https://pubmed.ncbi.nlm.nih.gov/27776107/)

> *"Treatment with lenalidomide increased RhoA activity and reversed the migration and activation defects of RASGRP1-deficient lymphocytes"* — [PMID: 27776107](https://pubmed.ncbi.nlm.nih.gov/27776107/)

**Interpretation:** RASGRP1 has a **RAS-ERK–independent, cytoskeletal arm** (via DYNLL1/RhoA) that explains the NK immune-synapse and lymphocyte-motility defects. The lenalidomide rescue provides a rational, mechanism-based bridging therapy.

### Finding 4 — Across ~15 reported patients, infections (100%) and lymphoproliferation (87%) predominate; vasculopathy is an emerging fatal phenotype and HSCT is the only cure

A 2026 review by Ashari et al. compiled **14 previously reported cases plus one new patient** (a 5-year-old male with a novel homozygous splice-donor RASGRP1 mutation). Across this aggregated cohort, **infections occurred in 100% and lymphoproliferation in 87%** of cases; **severe vasculopathy and fatal autoimmune hemolytic anemia** are highlighted as **emerging life-threatening phenotypes**. HSCT remains the only curative therapy.

> *"A review of 14 previously reported cases (plus current case) confirms that while infections (100%) and lymphoproliferation (87%) are common, vascular autoimmunity is an emerging life-threatening phenotype. Hematopoietic stem cell transplantation remains the only curative therapy, as conservative management carries high mortality."* — [PMID: 42253627](https://pubmed.ncbi.nlm.nih.gov/42253627/)

**Interpretation:** This provides the best available disease-level quantification of penetrant phenotypes and prognosis, and flags autoimmune vasculopathy as an underrecognized driver of mortality.

### Finding 5 — RASGRP1 is a calcium- and DAG-regulated RAS exchange factor held in an autoinhibited state; truncating mutations abolish this catalytic machinery

A crystal structure of a RasGRP1 fragment (Iwig et al., 2013) revealed that the **RAS-binding (catalytic REM/CDC25) site is blocked by an interdomain linker** and the **membrane-interaction surface is hidden within a dimerization interface** stabilized by the C-terminal oligomerization domain. NMR showed that **Ca²⁺ binding to the EF-hand regulatory module drives conformational changes incompatible with the inactive assembly**, so RasGRP1 is maintained inactive but "poised for activation by calcium and membrane-localization signals."

> *"We present a crystal structure of a fragment of RasGRP1 in which the Ras-binding site is blocked by an interdomain linker and the membrane-interaction surface of RasGRP1 is hidden within a dimerization interface that may be stabilized by the C-terminal oligomerization domain."* — [PMID: 23908768](https://pubmed.ncbi.nlm.nih.gov/23908768/)

> *"NMR data demonstrate that calcium binding to the regulatory module generates substantial conformational changes that are incompatible with the inactive assembly. These features allow RasGRP1 to be maintained in an inactive state that is poised for activation by calcium and membrane-localization signals."* — [PMID: 23908768](https://pubmed.ncbi.nlm.nih.gov/23908768/)

**Interpretation:** The structure explains why **truncating/LOF mutations are catastrophic**: they remove the catalytic and/or regulatory modules needed to convert the Ca²⁺/DAG signal into RAS-GTP loading, producing complete loss of exchange activity.

### Finding 6 — Common RASGRP1 regulatory variants are autoimmunity susceptibility loci, distinct from the monogenic biallelic-null immunodeficiency

GWAS/immunochip studies associate **common RASGRP1 variants** with multiple autoimmune diseases: **East Asian SLE** (Sun et al., 2016), **rheumatoid arthritis** in Europeans (2016), **Hashimoto's thyroiditis / TPOAb** (rs7171171 near RASGRP1, OR 1.4), and **IgA nephropathy**. These are population-level susceptibility alleles that alter RASGRP1 expression/dosage — mechanistically distinct from the rare **biallelic LOF** alleles that cause IMD64.

> *"followed by DEF6, IL12B, TCF7, TERT, CD226, PCNXL3, RASGRP1, SYNGR1 and SIGLEC6"* — [PMID: 26808113](https://pubmed.ncbi.nlm.nih.gov/26808113/)

> *"IL6R, BACH2, RASGRP1, TLE3, and IKZF3 are replicated for the first time in an independent European population"* — [PMID: 26939566](https://pubmed.ncbi.nlm.nih.gov/26939566/)

> *"rs7171171 near RASGRP1 gene (p = 0.0356, OR = 1.4, CI = 1.02-1.92)"* — [PMID: 27268232](https://pubmed.ncbi.nlm.nih.gov/27268232/)

**Interpretation:** RASGRP1 exhibits an **allelic spectrum**: partial/dosage perturbation → polygenic autoimmunity; complete biallelic loss → monogenic combined immunodeficiency (IMD64). This dosage sensitivity underscores RASGRP1's central role in immune homeostasis.

---

## Detailed Section-by-Section Report

### 1. Disease Information

- **Overview:** IMD64 is an autosomal-recessive combined immunodeficiency with immune dysregulation, characterized by defective TCR→RAS→ERK signaling, recurrent infections, lymphoproliferation, autoimmunity, and EBV-associated lymphoma.
- **Key identifiers:** OMIM **#618534** ("Immunodeficiency 64 with lymphoproliferation"); MONDO:**0030926**; gene RASGRP1 (HGNC:9866; NCBI Gene 10125; OMIM *603962). Orphanet does not have a widely used dedicated ORPHAcode distinct from the RASGRP1-deficiency entry; ICD-11 best maps to **4A00.x** (Primary immunodeficiencies) / immune dysregulation category; MeSH lacks a specific term (falls under "Primary Immunodeficiency Diseases," D000081207; "Lymphoproliferative Disorders," D008232).
- **Synonyms / alternative names:** "Immunodeficiency 64 with lymphoproliferation"; "RASGRP1 deficiency"; "RASGRP1-related combined immunodeficiency."
- **Information source:** Aggregated disease-level knowledge derived from individual **case reports and small case series** (~15 patients), not from large-scale EHR/registry data.

### 2. Etiology

- **Primary cause:** Genetic — **biallelic loss-of-function mutations in RASGRP1** (Finding 1). No environmental or infectious cause initiates the disease, though **EBV acts as a critical downstream trigger** of lymphoproliferation/lymphoma in the setting of the genetic defect (Finding 2).
- **Genetic risk factors:** The causal variants are private/rare biallelic RASGRP1 LOF alleles (stop-gain, splice-site, frameshift). **Consanguinity** is a major risk factor, as most reported families are consanguineous with homozygous variants (Findings 1, 4). Common RASGRP1 regulatory variants are **not** a cause of IMD64 but are independent autoimmunity susceptibility alleles (Finding 6).
- **Environmental risk factors:** EBV exposure (near-universal in humans) is the key environmental cofactor converting the immunodeficiency into life-threatening lymphoproliferation.
- **Protective factors:** None established genetically. Practically, **EBV surveillance and avoidance of unnecessary immunosuppression** may reduce complications; no protective alleles are known.
- **Gene–environment interaction:** The central GxE interaction is **RASGRP1 LOF × EBV infection → uncontrolled B-cell proliferation and lymphoma** (Findings 2, 4).

### 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Frequency | Onset / severity |
|---|---|---|---|---|
| Recurrent/severe infections | Clinical / immunologic | HP:0002719 (Recurrent infections) | 100% | Childhood; moderate–severe |
| Non-malignant lymphoproliferation (lymphadenopathy, splenomegaly) | Clinical sign | HP:0002733 (Generalized lymphadenopathy); HP:0001744 (Splenomegaly) | ~87% | Childhood; variable |
| EBV-driven lymphoproliferative disease / lymphoma (Hodgkin & non-Hodgkin) | Neoplasm | HP:0002665 (Lymphoma); HP:0005523 (Combined immunodeficiency) | High | Childhood/adolescence; severe |
| Autoimmune cytopenias (autoimmune hemolytic anemia) | Lab / clinical | HP:0001890 (Autoimmune hemolytic anemia) | Recurrent | Childhood; can be fatal |
| Vasculopathy / vascular autoimmunity | Clinical | HP:0002597 (Abnormality of the vasculature) | Emerging | Severe, potentially fatal |
| Impaired T/B-cell proliferation & activation; abnormal lymphocyte subsets | Lab abnormality | HP:0005425 (Abnormal T cell count); HP:0010975 (Abnormal B cell morphology) | Common | Congenital defect, childhood-detected |
| Reduced NK cytotoxicity | Lab abnormality | HP:0012177 (Decreased proportion of NK cells) | Common | Congenital |
| Hypogammaglobulinemia / absent B cells (subset) | Lab abnormality | HP:0004313 (Decreased circulating antibody level) | Variable | Childhood |

- **Progression:** Generally **progressive/episodic**, punctuated by infection and autoimmune flares; lymphoma is a life-threatening event.
- **Quality-of-life impact:** Substantial — recurrent hospitalization for infection, immunosuppression, chemotherapy, and transplant; disease-specific QoL instruments (EQ-5D/SF-36) have not been reported for this ultra-rare disorder.

### 4. Genetic / Molecular Information

- **Causal gene:** **RASGRP1** (HGNC:9866; NCBI Gene 10125; OMIM *603962; Ensembl ENSG00000172575; 15q14; UniProt O95267).
- **Pathogenic variants:** Reported variants are **biallelic LOF**: stop-gain/nonsense (Salzer 2016), **splice-donor** (Ashari 2026), frameshift, and other LOF alleles (Somekh 2018). Classification per ACMG/AMP is **pathogenic/likely pathogenic** for these truncating and splice variants (PVS1-supporting, given LOF is the established disease mechanism).
- **Variant type/class:** Nonsense, splice-site, frameshift (loss-of-function); the disease requires **homozygous or compound-heterozygous** LOF.
- **Allele frequency:** Causal alleles are extremely rare/private (absent or ultra-rare in gnomAD), consistent with recessive, often consanguineous inheritance.
- **Somatic vs germline:** **Germline** (constitutional). Secondary lymphomas may acquire somatic changes, but the primary lesion is germline.
- **Functional consequence:** **Loss of function** — abolition of RAS-GEF catalytic activity and Ca²⁺/DAG-regulated activation (Findings 1, 5).
- **Modifier genes:** Not formally defined; disease severity may be modulated by EBV status and other immune genes, but no specific modifiers proven.
- **Epigenetic information:** RASGRP1 expression is transcriptionally regulated (e.g., Nurr1 binds a RasGRP1 intron; [PMID: 32612143](https://pubmed.ncbi.nlm.nih.gov/32612143/)), but disease-specific epigenetic changes in IMD64 are not established.
- **Chromosomal abnormalities:** None characteristic; IMD64 is a single-gene disorder, not a copy-number/aneuploidy syndrome.

### 5. Environmental Information

- **Environmental factors:** No toxic/occupational/radiation exposures cause IMD64.
- **Lifestyle factors:** Not applicable as causal factors.
- **Infectious agents:** **Epstein–Barr virus (EBV; HHV-4; NCBI Taxon 10376)** is the pivotal infectious trigger of lymphoproliferation and lymphoma (Findings 2, 4). Patients are also generally susceptible to recurrent bacterial and other viral infections due to combined immunodeficiency.

### 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
Biallelic RASGRP1 LOF mutation
        │  (loss of Ca2+/DAG-regulated RasGEF; catalytic/regulatory modules abolished — Iwig 2013)
        ▼
Failure to load RAS-GTP after TCR/pre-TCR engagement
        │
        ▼
Collapse of RAS → RAF → MEK → ERK1/2 (MAPK) signaling  (Salzer 2016; Somekh 2018)
        │                                   │
        ▼                                   ▼
Impaired thymocyte positive selection    Defective lymphocyte proliferation/activation
(reduced naive T-cell output)                 + RASGRP1–DYNLL1–RhoA cytoskeletal arm
        │                                   │        (impaired motility; NK granule
        ▼                                   ▼         convergence & actin — Salzer 2016)
Reduced/abnormal T-cell repertoire      Defective CD8+ effector expansion & NK cytotoxicity
        │                                   │
        └───────────────┬───────────────────┘
                        ▼
        Failure to control EBV-infected B cells
                        ▼
   Uncontrolled B-cell proliferation → lymphoproliferative disease → Hodgkin/non-Hodgkin lymphoma
                        ▼
   Concurrent loss of tolerance → autoimmunity (AIHA, cytopenias, vasculopathy)
```

- **Molecular pathways:** **RAS–MAPK/ERK** (KEGG hsa04014; Reactome RAF/MAP kinase cascade R-HSA-5673001); TCR signaling (KEGG hsa04660); DAG/Ca²⁺ second-messenger signaling. RASGRP1 sits upstream, converting DAG/Ca²⁺ to RAS activation; adaptors such as SKAP55 ([PMID: 17658605](https://pubmed.ncbi.nlm.nih.gov/17658605/)) modulate RASGRP1.
- **Cellular processes (GO suggestions):** GO:0007265 (Ras protein signal transduction), GO:0000165 (MAPK cascade), GO:0050852 (T cell receptor signaling pathway), GO:0042110 (T cell activation), GO:0002323 (natural killer cell activation), GO:0030036 (actin cytoskeleton organization), GO:0007204 (positive regulation of cytosolic calcium ion concentration).
- **Protein dysfunction:** Loss of RAS-GEF catalytic function; truncating mutations remove REM/CDC25 catalytic and/or EF-hand/C1 regulatory modules, abolishing Ca²⁺/DAG-triggered relief of autoinhibition (Finding 5).
- **Immune-system involvement:** Combined immunodeficiency (impaired T, B, NK function) **plus** immune dysregulation/autoimmunity — a hallmark "PIRD" (primary immune regulatory disorder).
- **Cell types (CL suggestions):** CL:0000084 (T cell), CL:0000625 (CD8⁺ T cell), CL:0000624 (CD4⁺ T cell), CL:0000236 (B cell), CL:0000623 (natural killer cell), CL:0000813 (memory T cell).
- **Molecular profiling:** Functional immunology (pERK, RAS-GTP pull-down, NK cytotoxicity assays) is the main readout; no large transcriptomic/proteomic/metabolomic disease signatures have been published.

### 7. Anatomical Structures Affected

- **Organ level:** **Immune/lymphoid system** primarily — thymus (UBERON:0002370; impaired selection), spleen (UBERON:0002106; splenomegaly), lymph nodes (UBERON:0000029; lymphadenopathy), bone marrow (UBERON:0002371). Secondary involvement: **blood vessels** (UBERON:0001981; vasculopathy), **kidney** (UBERON:0002113; diffuse mesangial sclerosis/nephrotic syndrome reported — [PMID: 39752212](https://pubmed.ncbi.nlm.nih.gov/39752212/)), and **red-cell compartment** (AIHA).
- **Body systems:** Immune/hematolymphoid (primary); cardiovascular (vasculopathy); renal (secondary).
- **Tissue/cell level:** Hematopoietic/lymphoid tissue; affected populations are T cells, B cells, and NK cells (CL terms above).
- **Subcellular level (GO cellular component):** GO:0005886 (plasma membrane; site of RAS activation), GO:0005856 (cytoskeleton; DYNLL1/RhoA arm), GO:0005768 (endosome; RasGRP1 trafficking).
- **Localization/lateralization:** Systemic and bilateral (lymphadenopathy, cytopenias); no characteristic lateralization.

### 8. Temporal Development

- **Onset:** **Childhood-onset**, typically early (some as young as infancy/toddlerhood; the new Ashari case was 5 years old). Onset pattern is chronic with acute infectious/autoimmune exacerbations.
- **Progression:** Progressive and **episodic**; lymphoproliferation may precede overt lymphoma. Vasculopathy and AIHA can be **rapidly life-threatening**.
- **Disease course:** Chronic, lifelong without curative HSCT.
- **Critical periods / windows for intervention:** Early diagnosis before EBV-driven lymphoma or fatal autoimmune complications; **HSCT before end-organ damage** offers the best outcome.

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare — approximately **15 reported patients worldwide** (Finding 4). No reliable prevalence/incidence figures exist; effectively <1 per 1,000,000.
- **Inheritance:** **Autosomal recessive** (biallelic LOF).
- **Penetrance / expressivity:** Appears **high penetrance** for immunodeficiency/lymphoproliferation in biallelic-null individuals, with **variable expressivity** for autoimmunity, lymphoma type, and vasculopathy.
- **Consanguinity:** Major contributor; most reported families are **consanguineous** with homozygous variants.
- **Founder effects / carrier frequency:** No established founder alleles; carrier frequency not defined but presumed very low (rare private alleles).
- **Population demographics:** Cases reported from consanguineous populations (e.g., Middle Eastern, including Iranian and Turkish cohorts — [PMID: 38644452](https://pubmed.ncbi.nlm.nih.gov/38644452/), [PMID: 38683392](https://pubmed.ncbi.nlm.nih.gov/38683392/)); no strong sex bias established. Common (non-causal) RASGRP1 autoimmunity alleles show population-specific frequencies (East Asian SLE, European RA — Finding 6).

### 10. Diagnostics

- **Laboratory / immunologic tests:** Lymphocyte subset quantification (variable T/B/NK abnormalities; some patients absent B cells/hypogammaglobulinemia — [PMID: 38683392](https://pubmed.ncbi.nlm.nih.gov/38683392/)); **functional assays** — reduced TCR-induced **ERK phosphorylation**, reduced **RAS-GTP** loading, impaired T/B proliferation, and **defective NK cytotoxicity** (Findings 1, 3). EBV viral-load monitoring is essential.
- **Biomarkers:** No specific circulating biomarker; functional signaling defects and EBV load serve as surrogate markers.
- **Imaging:** CT/PET for lymphadenopathy/lymphoma staging; vascular imaging for vasculopathy.
- **Biopsy/pathology:** Lymph-node/tissue biopsy to distinguish reactive lymphoproliferation from lymphoma (Hodgkin/non-Hodgkin); renal biopsy where nephrotic syndrome occurs.
- **Genetic testing (recommended, definitive):** **Whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**, or **targeted IEI/PIRD next-generation-sequencing panels** including RASGRP1 (e.g., Ion AmpliSeq Primary Immune Deficiency panel — [PMID: 38644452](https://pubmed.ncbi.nlm.nih.gov/38644452/)); confirm with Sanger and segregation. Homozygosity mapping is useful in consanguineous families.
- **Clinical criteria / differential diagnosis:** Consider within **ALPS-like / PIRD** and **EBV-susceptibility IEIs**; differentials include XLP1 (SH2D1A), XLP2 (XIAP), ITK, MAGT1, CD27/CD70, CTPS1, CORO1A deficiencies ([PMID: 34447369](https://pubmed.ncbi.nlm.nih.gov/34447369/), [PMID: 36209991](https://pubmed.ncbi.nlm.nih.gov/36209991/)). Genetic testing distinguishes them.
- **Screening:** Cascade genetic testing in families; carrier testing for at-risk relatives; EBV surveillance in known-affected individuals.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival curves exist for this ultra-rare disorder. Prognosis is **guarded**: conservative management carries **high mortality** (Finding 4). Fatal outcomes reported from lymphoma, severe infection, autoimmune hemolytic anemia, and vasculopathy. As broader context, lymphoma arising on a background of primary immunodeficiency has markedly worse survival than in immunocompetent patients (5-yr OS 41% vs 80% in a PID-malignancy cohort — [PMID: 35282762](https://pubmed.ncbi.nlm.nih.gov/35282762/)).
- **Morbidity/function:** High — recurrent infection, chronic immunosuppression, chemotherapy, transplant-related morbidity.
- **Complications:** EBV lymphoma, autoimmune cytopenias, vasculopathy, nephrotic syndrome, infection.
- **Recovery potential:** **HSCT can be curative** (Finding 4); without it, chronic and often fatal.
- **Prognostic factors:** Early diagnosis, EBV control, absence of established lymphoma/vasculopathy at transplant, and successful HSCT engraftment.

### 12. Treatment

| Modality | Intervention | Evidence / rationale | NCIT (suggested) |
|---|---|---|---|
| **Curative** | Allogeneic **HSCT** | Only curative therapy; corrects the hematopoietic-restricted defect (Finding 4) | NCIT:C15431 (Hematopoietic Stem Cell Transplantation) |
| **Mechanism-based experimental** | **Lenalidomide** | Restores RhoA activity, reverses migration/activation defects in patient cells (Finding 3) | NCIT:C1873 (Lenalidomide) |
| Anti-B-cell / lymphoma | **Rituximab**, chemotherapy | Controls EBV-driven B-cell proliferation/lymphoma | NCIT:C1702 (Rituximab) |
| Immune dysregulation | Immunosuppression / immunomodulation | Manages autoimmunity (cytopenias, vasculopathy) | NCIT:C15329 (Immunosuppressive Therapy) |
| Supportive | **IVIG replacement**, antimicrobial prophylaxis | For hypogammaglobulinemia and infection prevention | NCIT:C579 (Immunoglobulin Therapy) |
| Surveillance | EBV viral-load monitoring | Early detection of lymphoproliferation | — |

- **Pharmacogenomics:** Not established for IMD64.
- **Gene/cell/RNA therapies:** No approved gene therapy; RASGRP1 is a rational future gene-correction/HSC gene-therapy target given the hematopoietic-restricted phenotype, but this remains preclinical/theoretical.
- **Treatment strategy:** Genotype-driven — confirm biallelic RASGRP1 LOF, control EBV/lymphoma, manage autoimmunity, and proceed to **HSCT** as definitive therapy.

### 13. Prevention

- **Primary prevention:** Not possible for the genetic defect. **Genetic counseling** and, in consanguineous families, awareness of recessive risk. Prenatal/preimplantation genetic testing for known familial variants.
- **Secondary prevention:** Early molecular diagnosis (WES/panel), **cascade testing**, and **EBV surveillance** to catch lymphoproliferation early.
- **Tertiary prevention:** Infection prophylaxis (antimicrobials, IVIG), vaccination per IEI guidelines (avoid live vaccines where cellular immunity is compromised), and timely HSCT to prevent lethal complications.
- **Counseling:** Autosomal-recessive recurrence risk 25% for future offspring of carrier parents; offer carrier testing and reproductive options.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** RASGRP1 is conserved. **Mouse Rasgrp1** (Mus musculus, NCBI Taxon 10090; NCBI Gene 19419) is the principal ortholog studied.
- **Natural disease in animals:** No well-characterized spontaneous RASGRP1-deficiency disease reported in companion animals or wildlife (no OMIA entry noted).
- **Comparative biology:** The **Ras–ERK requirement for thymocyte positive selection and β-selection is evolutionarily conserved**, validated extensively in mouse (see Section 15). Human and mouse share the core TCR→RASGRP1→ERK developmental mechanism.
- **Zoonotic potential:** Not applicable (non-transmissible genetic disorder).

### 15. Model Organisms

- **Primary model:** **Mouse (Rasgrp1)** knockout and knock-in models, which recapitulate key mechanistic features:
  - **Positive selection defect:** RasGRP1 is the dominant RasGEF required at the TCR checkpoint; its deletion efficiently blocks positive selection ([PMID: 22586275](https://pubmed.ncbi.nlm.nih.gov/22586275/)).
  - **β-selection / DN3 block & CXCR4-ERK link:** RasGRP1-KO thymi show a partial DN3 developmental block and reduced proliferation; RasGRP1 is required for ERK activation downstream of CXCR4 ([PMID: 23308188](https://pubmed.ncbi.nlm.nih.gov/23308188/)).
  - **Tail-domain knock-in:** Deletion of the unique C-terminal tail impairs membrane trafficking and ERK activation and drives CD4⁺ expansion/autoantibodies with age ([PMID: 22719950](https://pubmed.ncbi.nlm.nih.gov/22719950/)) — modeling the autoimmunity axis.
  - **γδ T cells & agonist selection:** RasGRP1 is required for γδ T-cell proliferation/IL-17 and for agonist selection of TCRαβ lineages ([PMID: 22623331](https://pubmed.ncbi.nlm.nih.gov/22623331/), [PMID: 28652304](https://pubmed.ncbi.nlm.nih.gov/28652304/)).
- **Cellular / in vitro models:** **Jurkat T-leukemia cells** used to demonstrate perturbed ERK1/2 and reduced RAS-GTPase activity from patient variants ([PMID: 30030704](https://pubmed.ncbi.nlm.nih.gov/30030704/)); patient-derived primary lymphocytes/NK cells for functional rescue (WT re-expression, lenalidomide) ([PMID: 27776107](https://pubmed.ncbi.nlm.nih.gov/27776107/)).
- **Phenotype recapitulation & limitations:** Mouse models faithfully reproduce the **T-cell developmental and ERK-signaling defects and the autoimmunity predisposition**, but **do not recapitulate EBV-driven lymphoproliferation** (EBV is human-restricted), a central feature of the human disease — the key limitation for modeling IMD64.
- **Resources:** MGI (Rasgrp1), IMPC/KOMP for engineered alleles; Cellosaurus for Jurkat.

---

## Mechanistic Model / Interpretation

RASGRP1 is the **molecular switch that translates antigen-receptor engagement into RAS-ERK activation** in lymphocytes. Structural work (Finding 5) shows it is normally **autoinhibited** — catalytic site occluded, membrane surface buried in a dimer — until **Ca²⁺ and DAG** relieve autoinhibition and recruit it to the membrane to load RAS-GTP. Biallelic LOF mutations (Finding 1) destroy this switch. The consequences fan out along **two arms**: (i) a **RAS-ERK arm** that governs thymocyte selection and lymphocyte proliferation/activation, and (ii) a **cytoskeletal arm** via DYNLL1/RhoA that governs lymphocyte motility and NK immune-synapse/granule dynamics (Finding 3). Failure of both arms yields a **combined immunodeficiency** whose most dangerous manifestation is **loss of CD8⁺/NK control over EBV-infected B cells** (Finding 2), driving lymphoproliferation and lymphoma; concurrently, disrupted tolerance produces **autoimmunity**, including cytopenias and an emerging **fatal vasculopathy** (Finding 4).

The **allelic spectrum** (Finding 6) ties the rare and common ends together: partial perturbation of RASGRP1 dosage predisposes to polygenic autoimmunity (SLE, RA, thyroiditis, IgAN), while complete biallelic loss produces monogenic IMD64. This dosage sensitivity marks RASGRP1 as a **rheostat of immune homeostasis**.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [27776107](https://pubmed.ncbi.nlm.nih.gov/27776107/) | *RASGRP1 deficiency causes immunodeficiency with impaired cytoskeletal dynamics* | Landmark: causal gene, ERK rescue, DYNLL1/RhoA, lenalidomide (Findings 1, 3) |
| [30030704](https://pubmed.ncbi.nlm.nih.gov/30030704/) | *Novel Mutations in RASGRP1... EBV-Induced Lymphoma* | Independent LOF confirmation; EBV malignancy (Findings 1, 2) |
| [37898412](https://pubmed.ncbi.nlm.nih.gov/37898412/) | *Novel homozygous RASGRP1 mutation... EBV-induced B cell proliferation* | Direct EBV-control failure (Finding 2) |
| [31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/) | *Signaling pathways in T-cell immunity against EBV* | Mechanistic placement with MAGT1/ITK (Finding 2) |
| [42253627](https://pubmed.ncbi.nlm.nih.gov/42253627/) | *RASGRP1 Deficiency... Severe Vasculopathy and Fatal AIHA* | Cohort quantification, vasculopathy, HSCT (Finding 4) |
| [23908768](https://pubmed.ncbi.nlm.nih.gov/23908768/) | *Structural analysis of autoinhibition in RasGRP1* | Autoinhibition/activation structure (Finding 5) |
| [26808113](https://pubmed.ncbi.nlm.nih.gov/26808113/) | *SLE risk variants, Asian ancestry* | RASGRP1 as SLE locus (Finding 6) |
| [26939566](https://pubmed.ncbi.nlm.nih.gov/26939566/) | *RA variants, European* | RASGRP1 as RA locus (Finding 6) |
| [27268232](https://pubmed.ncbi.nlm.nih.gov/27268232/) | *TPOAb variants, Hashimoto's* | RASGRP1 autoimmune thyroid locus (Finding 6) |
| [27804980](https://pubmed.ncbi.nlm.nih.gov/27804980/) | *RGS1/RASGRP1 in IgA nephropathy* | RASGRP1 autoimmune renal locus (Finding 6) |
| [22586275](https://pubmed.ncbi.nlm.nih.gov/22586275/), [23308188](https://pubmed.ncbi.nlm.nih.gov/23308188/), [22719950](https://pubmed.ncbi.nlm.nih.gov/22719950/), [22623331](https://pubmed.ncbi.nlm.nih.gov/22623331/), [28652304](https://pubmed.ncbi.nlm.nih.gov/28652304/) | Mouse Rasgrp1 studies | Model-organism validation (Section 15) |
| [34447369](https://pubmed.ncbi.nlm.nih.gov/34447369/), [36209991](https://pubmed.ncbi.nlm.nih.gov/36209991/), [38644452](https://pubmed.ncbi.nlm.nih.gov/38644452/), [38683392](https://pubmed.ncbi.nlm.nih.gov/38683392/), [39752212](https://pubmed.ncbi.nlm.nih.gov/39752212/), [35282762](https://pubmed.ncbi.nlm.nih.gov/35282762/) | PIRD/ALPS-like, panels, phenotypes | Differential diagnosis, diagnostics, prognosis |

---

## Limitations and Knowledge Gaps

- **Very small evidence base (~15 patients):** Frequency estimates (100% infections, 87% lymphoproliferation) come from aggregated case reports and are subject to ascertainment/publication bias.
- **No formal epidemiology:** True prevalence, incidence, penetrance, sex ratio, and survival statistics are unknown.
- **No large omics datasets:** Transcriptomic/proteomic/metabolomic disease signatures and single-cell studies are lacking.
- **EBV cannot be modeled in mouse:** The central lymphoproliferative phenotype is human-restricted; humanized models are needed.
- **Vasculopathy mechanism undefined:** The emerging fatal vasculopathy is described phenomenologically but not mechanistically dissected.
- **Therapeutics largely anecdotal:** Lenalidomide efficacy is based on ex-vivo/limited clinical data; HSCT outcomes lack systematic cohort analysis.
- **Ontology/identifier gaps:** MONDO/OMIM are established, but Orphanet/ICD-11/MeSH mappings are imprecise for this recently defined entity.

## Proposed Follow-up Experiments / Actions

1. **Establish an international IMD64 patient registry** to obtain robust frequency, penetrance, HSCT-outcome, and survival data.
2. **Systematic HSCT outcome analysis** — timing, conditioning, and pre-transplant lymphoma/vasculopathy status as prognostic factors.
3. **Prospective evaluation of lenalidomide** (and other RhoA-restoring agents) as bridging therapy, with standardized functional endpoints (RhoA activity, migration, NK cytotoxicity).
4. **Humanized/EBV-permissive models** (e.g., RASGRP1-null humanized mice, patient-iPSC-derived lymphoid organoids) to model EBV lymphoproliferation and test gene correction.
5. **Mechanistic study of the vasculopathy** — vessel-wall immunopathology, autoantibody characterization, and cytokine profiling.
6. **Autologous HSC gene therapy/gene editing** feasibility studies for RASGRP1 correction, given the hematopoietic-restricted phenotype.
7. **Single-cell multi-omics** of patient lymphoid compartments to map cell-type-specific consequences of RAS-ERK collapse and identify biomarkers of lymphoma risk.
8. **Deep-phenotyping of EBV surveillance protocols** to define optimal viral-load thresholds triggering pre-emptive rituximab.


## Artifacts

- [OpenScientist final report](Immunodeficiency_64-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_64-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 26 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012177` (1 mention) - the report calls it "Decreased proportion of NK cells"; HP calls it **Abnormal natural killer cell physiology**
- `GO:0005768` (1 mention) - the report calls it "endosome; RasGRP1 trafficking"; GO calls it **endosome**
- `NCIT:C15329` (1 mention) - the report calls it "Immunosuppressive Therapy"; NCIT calls it **Surgical Procedure**
- `NCIT:C579` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **Inorganic Chemical**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0002323` (1 mention) - the report calls it "natural killer cell activation"; GO calls it **natural killer cell activation involved in immune response**, and lists "natural killer cell activation during immune response" among its other names
- `CL:0000625` (1 mention) - the report calls it "CD8⁺ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `CL:0000624` (1 mention) - the report calls it "CD4⁺ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `GO:0005886` (1 mention) - the report calls it "plasma membrane; site of RAS activation"; GO calls it **plasma membrane**, and lists "plasma membrane lipid bilayer" among its other names
- `GO:0005856` (1 mention) - the report calls it "cytoskeleton; DYNLL1/RhoA arm"; GO calls it **cytoskeleton**
- `NCIT:C1873` (1 mention) - the report calls it "Lenalidomide"; NCIT calls it **Apomine**