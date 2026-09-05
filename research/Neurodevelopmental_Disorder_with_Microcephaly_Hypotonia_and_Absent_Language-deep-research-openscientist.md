---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-18T15:07:40.513135'
end_time: '2026-08-18T15:24:36.135302'
duration_seconds: 1015.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent
    Language
  mondo_id: ''
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
citation_count: 1
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_with_Microcephaly_Hypotonia_and_Absent_Language-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_with_Microcephaly_Hypotonia_and_Absent_Language-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent Language
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent Language** covering all of the
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

# Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent Language (NEDMHAL)
### A Comprehensive Disease Characterization Report

**Disease:** Neurodevelopmental disorder with microcephaly, hypotonia, and absent language (NEDMHAL)
**Causal gene:** *PSMB1* (proteasome 20S subunit beta 1)
**MONDO:** MONDO:0859287 · **OMIM (phenotype):** #620038 · **Category:** Mendelian, autosomal recessive

> **Evidence-base note:** This is an ultra-rare, recently delineated Mendelian disorder. The primary human evidence rests on a small number of individuals (index family: Ansar et al., 2020, PMID 32129449) plus disease-level ontology curation (OMIM/MONDO/HPO) and mechanistic work on the broader "primary proteasomopathy" gene family. Where information is not established for NEDMHAL specifically, this is stated explicitly and, where reasonable, inferred from the shared proteasomopathy mechanism. Evidence source types are flagged as **[human clinical]**, **[in vitro]**, **[model organism]**, or **[computational]**.

---

## Executive Summary

Neurodevelopmental disorder with microcephaly, hypotonia, and absent language (**NEDMHAL**; [OMIM #620038](https://www.omim.org/entry/620038); MONDO:0859287) is an **ultra-rare, severe autosomal recessive Mendelian disorder** caused by **biallelic hypomorphic missense variants in *PSMB1***, the gene encoding the non-catalytic β6 subunit of the 20S proteasome core. It was defined by Ansar et al., 2020 ([PMID: 32129449](https://pubmed.ncbi.nlm.nih.gov/32129449/)), who found a homozygous *PSMB1* c.307T>C, p.(Tyr103His) variant segregating with disease in two siblings of a consanguineous Pakistani family and validated causality in human SH-SY5Y cells and zebrafish.

The **core phenotype** is congenital/early-onset microcephaly, neonatal hypotonia, severe-to-profound intellectual disability, and absent expressive language, with global developmental delay, motor disability (often inability to walk), hearing impairment, and behavioral features (aggression, ADHD). **Mechanistically**, p.(Tyr103His) weakens the β6(PSMB1)–α5(PSMA5) subunit interface, destabilizing the 20S proteasome and reducing proteolytic capacity; the resulting proteostatic stress activates the integrated stress response and a **type I interferon signature** shared across "primary proteasomopathies" (*PSMB1/PSMC1/PSMC3/PSMD12/PSMD11*), derailing prenatal brain development.

There is **no disease-modifying therapy** — management is supportive and multidisciplinary — and **prevention rests on genetic counseling and carrier/prenatal/preimplantation testing**. A key nuance: the causal SNV is **not yet classified pathogenic in ClinVar** (same-codon changes are VUS), so the gene–disease relationship rests on strong functional/segregation evidence rather than accumulated clinical classifications; ClinVar "pathogenic" entries in the region are large 6q-terminal CNVs of a distinct contiguous-gene syndrome.

---

## 1. Disease Information

**Overview.** NEDMHAL is a rare autosomal recessive neurodevelopmental disorder caused by biallelic hypomorphic variants in *PSMB1*, a gene encoding a β-type subunit of the 20S proteasome core. It is a **congenital "primary proteasomopathy"**: impaired proteasome assembly/function during brain development produces a static encephalopathy dominated by microcephaly, muscular hypotonia, severe global developmental delay/intellectual disability, and absent expressive language, frequently with motor disability (inability to walk), hearing impairment, and behavioral disturbance. **[human clinical; computational]**

- *"PSMB1 encodes a β-type proteasome subunit (i.e. β6)… PSMB1/β6 pathogenic variants are the cause of a recessive disease with ID, microcephaly and developmental delay due to abnormal proteasome assembly."* — Ansar et al., 2020 (PMID 32129449).
- Authoritative concept definition (NCBI MedGen CUI C5774216 / UID 1823989): *"Neurodevelopmental disorder with microcephaly, hypotonia, and absent language (NEDMHAL) is a severe autosomal recessive disorder characterized by the constellation of these features. Behavioral problems and hearing loss are also present (Ansar et al., 2020)."* — confirms severity, autosomal recessive inheritance, and the additional behavioral/hearing features, and that OMIM #620038 is anchored to Ansar et al., 2020.

**Key identifiers.**
| Resource | ID |
|---|---|
| MONDO | MONDO:0859287 |
| OMIM (phenotype) | 620038 |
| OMIM (gene, *PSMB1*) | 602017 |
| UMLS / MedGen | C5774216 / CUI 1823989 (MedGen 1823989) |
| HGNC (gene) | HGNC:9537 |
| NCBI Gene | 5689 |
| Ensembl | ENSG00000008018 |
| UniProt (protein) | P20618 |

- **Orphanet:** No NEDMHAL-specific ORPHAcode was identified; the condition falls within Orphanet's broad "rare genetic intellectual disability / rare developmental defect" groupings. *(Not established — flagged as unavailable.)*
- **ICD-11:** No disease-specific code; maps to the neurodevelopmental block (e.g., LD90.Y "Other specified developmental anomalies" / 6A00 "Disorders of intellectual development") plus 5C51-range for proteostasis defects. *(No dedicated code.)*
- **ICD-10:** No specific code (would be coded via Q02 microcephaly / F79 unspecified intellectual disability / R62.0 developmental delay). *(No dedicated code.)*
- **MeSH:** No dedicated descriptor; nearest concepts are "Neurodevelopmental Disorders," "Microcephaly," "Muscle Hypotonia," "Intellectual Disability."

**Synonyms / alternative names:** NEDMHAL; PSMB1-related neurodevelopmental disorder; PSMB1-associated primary proteasomopathy; "microcephaly, intellectual disability, developmental delay and short stature due to PSMB1 deficiency" (descriptive, per Ansar et al. 2020).

**Data provenance:** Disease-level aggregated resources (OMIM, MONDO, HPO/Monarch) combined with individual-patient case reports (EHR/clinical exome workup). Not derived from large EHR cohorts; it is a case-report/case-series–level entity.

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound-heterozygous) pathogenic variants in *PSMB1*. The index report identified a **homozygous missense variant p.(Tyr103His)** (NM_002793) segregating with disease under an autosomal recessive model in a consanguineous Pakistani family. **[human clinical]**

- *"we have identified homozygosity for p(Tyr103His) in the PSMB1 gene (Genbank NM_002793) that segregated with the disease phenotype."* — PMID 32129449.

**Genetic risk factors.**
- **Causal variant:** *PSMB1* p.(Tyr103His) (hypomorphic missense) — necessary and sufficient in the biallelic state.
- **Susceptibility/predisposing factor:** parental **consanguinity** and regional founder homozygosity dramatically increase the risk of this recessive disorder. **[human clinical]**
- **Modifier genes:** none formally identified for NEDMHAL. By analogy to the proteasomopathy family, the residual output of the ubiquitin–proteasome system and stress-response gene background (e.g., ISR/PKR, interferon-pathway genes) are plausible modifiers. *(Not established for PSMB1.)*

**Environmental risk factors:** None known. This is a monogenic disorder with no established toxic, infectious, occupational, dietary, or lifestyle contribution. Age and sex are not established risk factors; family history/consanguinity is the key non-molecular risk indicator.

**Protective factors:** No genetic or environmental protective factors identified. In principle, a normal (wild-type) *PSMB1* allele is fully protective (recessive inheritance → heterozygous carriers are clinically unaffected).

**Gene–environment interactions:** None documented. *(Not applicable/none established.)*

---

## 3. Phenotypes

Curated HPO annotations (MONDO:0859287 / OMIM:620038, via Monarch) plus the primary case series. Onset is **congenital/neonatal-to-infantile**; severity is **severe**; course is **static (non-progressive)**. Frequencies are qualitative given the very small number of reported patients (exact percentages **not established**).

| Phenotype | HPO term | Type | Onset | Severity | Notes |
|---|---|---|---|---|---|
| Microcephaly | HP:0000252 | Physical/clinical sign | Congenital/infantile | Severe (can be primary) | Core feature; recapitulated in zebrafish |
| Absent speech / absent language | HP:0001344 | Clinical sign (communication) | Childhood (fails to emerge) | Severe | Defining feature of the name |
| Global developmental delay | HP:0001263 | Clinical sign | Infantile | Severe | Motor + cognitive |
| Intellectual disability, severe | HP:0010864 | Behavioral/cognitive | Childhood | Severe | |
| Motor delay | HP:0001270 | Clinical sign | Infantile | Severe | |
| Inability to walk | HP:0002540 | Physical manifestation | Childhood | Severe | Non-ambulatory in affected |
| Hypotonia (muscular) | HP:0001252 | Clinical sign | Neonatal | Moderate–severe | "Hypotonia" in disease name |
| Hearing impairment | HP:0000365 | Sensory/lab-audiology | Childhood | Variable | Sensory involvement |
| Aggressive behavior | HP:0000718 | Behavioral | Childhood | Variable | |
| Attention deficit hyperactivity disorder | HP:0007018 | Behavioral | Childhood | Variable | |
| Short stature | HP:0004322 | Physical | Postnatal | Variable | Reported by Ansar et al. 2020 |
| Microphthalmia (model) | HP:0000568 | Physical | Congenital | — | Seen in zebrafish; human ocular involvement not firmly established |

- *"…two siblings with phenotypic signs, including intellectual disability (ID), developmental delay and microcephaly… a recessive disease with ID, microcephaly and developmental delay."* — PMID 32129449.

**Quality-of-life impact:** Profound. Absent language, severe intellectual disability, and non-ambulation imply lifelong dependence for all activities of daily living; behavioral features (aggression, ADHD) add caregiver burden. Formal QoL instruments (EQ-5D, PROMIS, disease-specific tools) have **not** been applied to this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PSMB1* — "proteasome 20S subunit beta 1"; HGNC:9537; NCBI Gene 5689; Ensembl ENSG00000008018; gene OMIM 602017; locus **6q27** (GRCh38 chr6:170,535,120–170,553,307). Protein: UniProt **P20618**, "Proteasome subunit beta type-1," 241 aa (systematic proteasome subunit name **β6**). **[computational]**

**Pathogenic variants.**
- **Reported variant:** NM_002793.4:c.307T>C, **p.(Tyr103His)** — missense, homozygous, autosomal recessive (Ansar et al. 2020). ACMG classification consistent with pathogenic/likely pathogenic given segregation + functional evidence (in vitro proteasome-assembly defect + zebrafish model). **[human clinical; in vitro; model organism]**
- **Variant type/class:** missense (hypomorphic). Frameshift/nonsense biallelic (complete null) genotypes have **not** been reported in this disorder, consistent with predicted non-viability of complete PSMB1 loss.
- **ClinVar reality-check (this iteration):** As of query, ClinVar contains **no classified pathogenic single-nucleotide PSMB1 variant** for NEDMHAL — all PSMB1 SNVs are Uncertain significance or Likely benign (e.g., p.Met7Val, p.Arg66Gln, p.Arg128Cys, and notably **p.Tyr103Cys (c.308A>G)** as VUS at the *same codon* as the disease allele). Every ClinVar record labelled "Pathogenic/Likely pathogenic" in the PSMB1 region is a **large 6q25–q27 terminal deletion/duplication CNV** (contiguous-gene 6q-terminal deletion syndrome), **not** isolated PSMB1 disease. The gene–disease relationship therefore currently rests on the **primary functional study** (segregation + in-vitro proteasome-assembly defect + zebrafish), i.e., strong PS3-type functional evidence rather than accumulated clinical classifications. The occurrence of two independent nucleotide changes at **Tyr103** (His via c.307T>C; Cys via c.308A>G) suggests this residue, near the β6–α5 interface, is a functionally sensitive/possible hotspot. **[computational; human clinical]**
- **Allele frequency:** p.(Tyr103His) is ultra-rare/absent-to-singleton in gnomAD (population frequency not enriched); precise gnomAD count **not established here** but consistent with a private/founder recessive allele.
- **Somatic vs germline:** **germline** (constitutional, inherited from carrier parents).
- **Functional consequence:** **loss of function at the pathway level** — the variant impairs β6 processing and its incorporation into the proteasome, destabilizing the 20S core and reducing proteasome activity (i.e., partial loss of proteolytic capacity), rather than a gain-of-function or dominant-negative mechanism. **[in vitro]**

- *"this variant weakens the interactions between PSMB1/β6 and PSMA5/α5 proteasome subunits and thus destabilizes the 20S proteasome complex… affects both the processing of PSMB1/β6 and its incorporation into proteasome, thus impairing proteasome activity."* — PMID 32129449.

**Population constraint (gnomAD, GRCh38).** *PSMB1* is **loss-of-function intolerant**: pLI = 0.968, LOEUF (oe_lof upper) = 0.52, observed/expected LoF = 0.28, lof_z = 3.09; missense is unconstrained (mis_z = 0.45, oe_mis = 0.94). **Interpretation:** complete biallelic loss is likely embryonic-lethal; the recessive disease arises from **hypomorphic missense** alleles that reduce but do not abolish proteasome function. **[computational]**

**Modifier genes:** none established. **Epigenetic information:** no disease-specific DNA-methylation/histone signature reported for PSMB1-NEDMHAL (episignatures have not been defined). *(Not established.)* **Chromosomal abnormalities:** none; this is a single-gene point-mutation disorder (no recurrent CNV at 6q27 implicated for NEDMHAL). Note the distinct proteasome-CNV disorder at 3q27.1 involves *PSMD2* (PMID 41804662) — a different entity.

Suggested annotations: **HGNC:9537 (PSMB1)**; GO molecular/complex terms below.

---

## 5. Environmental Information

- **Environmental factors:** None known to cause or trigger NEDMHAL (no toxin, radiation, pollution, or occupational association). *(Not applicable — monogenic disorder.)*
- **Lifestyle factors:** None. *(Not applicable.)*
- **Infectious agents:** None causal. *Note the mechanistic irony:* the disorder features a **type I interferon (antiviral-type) signature** driven intrinsically by proteostatic stress, **not** by any infection (see Section 6). *(No infectious etiology.)*

---

## 6. Mechanism / Pathophysiology

**Core defect (upstream).** Hypomorphic PSMB1/β6 → impaired β6 maturation and incorporation into the nascent 20S core → **destabilized 20S proteasome** and reduced assembly of functional 26S proteasomes → **reduced ubiquitin-dependent proteolytic capacity**. **[in vitro; computational]**

**Downstream cascade.**
1. Accumulation of ubiquitinated/misfolded/damaged proteins → disturbed **proteostasis** and protein aggregation.
2. Activation of **stress responses**, including the **integrated stress response (ISR)** via the kinase **PKR**, and a **persistent type I interferon (IFN) gene signature** — a shared hallmark across primary proteasomopathies. **[in vitro; human clinical]**
3. Impaired protein turnover in **neural progenitors and neurons** during a period of intense proliferation and differentiation → reduced brain growth (**microcephaly**, reduced brain size) and disrupted neuronal maturation/connectivity → severe NDD and absent language.

- *"both syndromes show molecular similarities with protein aggregation, activated stress responses, metabolic imbalance and dysregulated type I interferon signalling."* — Wolfgramm et al., 2026 review (PMID 42370079).
- *"PSMD11 loss of function resulted in impaired 26S proteasome assembly and the acquisition of a persistent type I interferon (IFN) gene signature, mediated by the integrated stress response (ISR) protein kinase R (PKR)."* — Deb et al., 2024 (PMID 38866022) [family-level mechanism].

**Molecular pathways / cellular processes.** Ubiquitin–proteasome system (UPS); proteasome assembly; proteasome-mediated ubiquitin-dependent protein catabolism; cellular response to unfolded/misfolded protein; type I IFN response; ISR/eIF2α signaling. Metabolic imbalance is described at the family level. **Protein dysfunction:** structural destabilization of the 20S core via weakened β6(PSMB1)–α5(PSMA5) subunit interface (loss of proteolytic function; secondary aggregation of substrates). **Immune involvement:** sterile, cell-intrinsic **type I interferon activation** (autoinflammatory-adjacent), distinguishing proteasomopathies from classical infections/immunodeficiencies. **Tissue-damage mechanism:** proteotoxic/oxidative-type stress in developing neural tissue rather than ischemia/fibrosis. **Molecular profiling:** transcriptomic type I IFN signatures are documented in the proteasomopathy family; NEDMHAL-specific omics (proteomics/metabolomics/single-cell/spatial) are **not yet published**.

**Causal chain summary:**
`PSMB1 p.(Tyr103His) → β6 misincorporation → 20S destabilization → ↓26S proteasome activity → ubiquitinated-protein accumulation/aggregation → ISR (PKR) + type I IFN → impaired neural proliferation/homeostasis → microcephaly + severe NDD + absent language.`

**Suggested ontology terms.**
- **GO biological process:** proteasome assembly (GO:0043248); proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161); response to type I interferon (GO:0034340); integrated stress response signaling (GO:0140467); cellular response to unfolded protein (GO:0034620).
- **GO cellular component:** proteasome core complex (GO:0005839); proteasome complex (GO:0000502); cytosol (GO:0005829); nucleoplasm (GO:0005654).
- **GO molecular function:** threonine-type endopeptidase activity (GO:0004298) [complex-level].
- **CL cell types:** neural progenitor/radial glial cell (CL:0011020), neuron (CL:0000540), glutamatergic neuron (CL:0000679).
- **CHEBI:** ubiquitin-tagged substrates; bortezomib (CHEBI:52717) and other proteasome inhibitors (research tools, not therapeutics here).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Brain** (UBERON:0000955) — reduced size/microcephaly; cerebrum/cerebral cortex (UBERON:0000956) and overall brain growth. Nervous system (UBERON:0001016) is the primary system. **[human clinical; model organism]**
- **Secondary/associated:** **Ear/auditory system** (hearing impairment; UBERON:0001690 ear); **musculoskeletal/skeletal growth** (short stature; hypotonia affecting skeletal muscle UBERON:0001134); **eye** (UBERON:0000970) — microphthalmia documented in the zebrafish model (human ocular involvement not firmly established).
- **Body systems:** predominantly **central nervous system**; secondarily sensory (auditory), musculoskeletal, and growth/endocrine (short stature).
- **Tissue/cell level:** nervous tissue; neural progenitor cells and neurons of the developing cortex are the presumptive vulnerable populations (high proteostatic demand). CL terms: CL:0011020 (radial glial/neural progenitor), CL:0000540 (neuron).
- **Subcellular level:** the **proteasome core complex (GO:0005839)** within the **cytoplasm (GO:0005737/GO:0005829)** and **nucleus (GO:0005634)** — PSMB1/P20618 localizes to both compartments.
- **Localization/lateralization:** brain involvement is **bilateral/symmetric** (global reduction in brain volume), not focal or lateralized.

---

## 8. Temporal Development

- **Onset:** **Congenital / neonatal-to-early-infantile.** Hypotonia is often neonatal; microcephaly may be congenital (primary) or evolve postnatally; developmental delay becomes apparent in infancy; language fails to emerge in childhood. Onset pattern is **insidious/chronic** (a fixed developmental abnormality rather than an acute event). **[human clinical]**
- **Progression:** **Static (non-progressive) encephalopathy.** No evidence of neurodegeneration or regression is reported; deficits are stable and lifelong. Disease duration is **chronic/lifelong**. Progression rate is therefore not applicable in a degenerative sense.
- **Disease stages:** not staged (non-neoplastic, non-progressive). Functionally: neonatal hypotonia → infantile developmental delay/microcephaly recognition → childhood confirmation of absent language, severe ID, non-ambulation, behavioral features.
- **Patterns:** No remission (developmental deficits are fixed). **Critical period:** prenatal-to-early-postnatal **neurodevelopmental window**, when proteasome demand in proliferating neural tissue is highest — the presumptive window of vulnerability and, theoretically, the window in which any future intervention would need to act.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic *PSMB1*). Heterozygous carriers are unaffected. **[human clinical]**
- **Penetrance:** presumed **complete** in the biallelic state (based on the single informative family, both affected siblings homozygous). Formal penetrance estimates unavailable.
- **Expressivity:** likely variable (as in other proteasomopathies), but insufficient patients to quantify.
- **Genetic anticipation:** **Not applicable** (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported.
- **Founder effects / consanguinity:** the reported allele arose in a **consanguineous** Pakistani family via homozygosity-by-descent; **consanguinity is the principal risk context.** Population-specific founder status not formally established.
- **Carrier frequency:** not established; expected very low given *PSMB1* LoF-intolerance and rarity of hypomorphic alleles.
- **Epidemiology:** **Ultra-rare.** Prevalence and incidence are **not established** (only a handful of reported individuals worldwide; too few for rate estimates). Likely far below 1/1,000,000.
- **Population demographics:** first described in a South Asian (Pakistani) consanguineous family; no established ethnic predilection beyond the elevated recessive-disease risk in consanguineous populations. **Sex ratio:** no sex bias expected for an autosomal recessive gene (reported index siblings; formal ratio unavailable). **Age distribution:** presents in infancy/childhood; affected individuals are children/young people at description.

---

## 10. Diagnostics

**Genetic testing is the diagnostic cornerstone** (there is no biochemical newborn-screening marker).
- **Recommended approach:** **Whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**, ideally **trio-based**, is the highest-yield strategy for this genetically nonspecific NDD phenotype; homozygosity mapping is a useful adjunct in consanguineous families (as used in the index discovery). **[human clinical]**
- **Gene panels:** *PSMB1* is included on comprehensive intellectual-disability/NDD and (increasingly) proteasomopathy panels; single-gene testing is appropriate only when the phenotype is highly specific.
- **CMA / karyotype / FISH:** used to exclude copy-number and cytogenetic causes of microcephaly + NDD; will **not** detect the *PSMB1* point mutation. **Interpretation caveat:** ClinVar's "pathogenic" calls overlapping *PSMB1* are all **large 6q25–q27 terminal deletions/duplications** — a distinct contiguous-gene (6q-terminal deletion) syndrome in which *PSMB1* is only one of many affected genes; these must not be conflated with biallelic point-variant NEDMHAL. A separate 3q27.1 microdeletion (involving *PSMD2*) is another distinct proteasome-related CNV disorder (PMID 41804662).
- **Mitochondrial DNA / repeat-expansion testing:** not indicated (not a mitochondrial or repeat-expansion disease).
- **Variant interpretation aids:** ClinVar, ClinGen, gnomAD (allele frequency), and functional confirmation (proteasome-assembly/activity assays in patient cells).

**Supportive clinical tests.**
- **Imaging:** **Brain MRI** to document microcephaly and any structural anomaly (the index/model data emphasize reduced brain size; cerebral/cerebellar atrophy has been described in an overlapping severe UPS phenotype). **[human clinical]**
- **Audiology:** hearing assessment (BAER/audiometry) given hearing impairment.
- **EEG:** if seizures are suspected (seizures are prominent in some related proteasomopathies/UPS disorders; not a defining NEDMHAL feature).
- **Auxology:** growth monitoring (short stature), head-circumference tracking.
- **Research/omics biomarkers:** a **type I interferon signature** (ISG transcript score in blood) and reduced proteasome chymotrypsin-like activity / accumulated ubiquitin–protein conjugates in patient cells are promising **research biomarkers** for proteasomopathies, not yet validated diagnostics for NEDMHAL. **[in vitro; human clinical]**

**Clinical criteria / differential diagnosis.** No formal diagnostic criteria; diagnosis = compatible phenotype + biallelic pathogenic *PSMB1* variants. **Differential diagnosis** includes:
- Other **primary proteasomopathies**: *PSMC1, PSMC3* (PMID 37256937), *PSMD11* (PMID 38866022), *PSMD12* (Stankiewicz–Isidor syndrome), *POMP*; and CNV/*PSMD2* (PMID 41804662).
- Other **UPS/ubiquitin disorders** with overlapping microcephaly/absent-speech/hypotonia: *OTUD6B* (PMID 28343629), *FBXO11* (PMID 30057029).
- Broad microcephaly-with-ID differentials (e.g., primary microcephaly genes) and syndromic ID (e.g., Cohen, Angelman when absent speech + behavior predominate) — distinguished by gene-specific testing.

**Screening:** No population newborn screening (no metabolite). Relevant screening is **carrier/cascade testing** in families and **prenatal/preimplantation** genetic testing once the familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Not established.** No survival, life-expectancy, or mortality-rate data exist for this ultra-rare disorder. Prognosis for **neurodevelopmental function** is poor (severe fixed disability).
- **Morbidity/disability:** **Severe, lifelong.** Absent language, severe intellectual disability, and frequent non-ambulation predict full dependence for daily care; hearing impairment and behavioral difficulties (aggression, ADHD) add morbidity. ICF-level: profound limitations in communication, mobility, and self-care.
- **Disease course:** Static; complications are those of severe neurodisability (e.g., feeding difficulty/aspiration, orthopedic sequelae of hypotonia/immobility, communication and behavioral challenges). **Recovery potential:** none for the core developmental deficits; supportive/rehabilitative care can improve function and comfort.
- **Prognostic factors:** presumably genotype-related residual proteasome activity (hypomorphic vs more severe alleles) and severity of microcephaly; formal prognostic models/biomarkers are **not established.** A high type I IFN signature is a candidate severity/activity biomarker at the family level.
- **QoL measures:** none applied specifically. *(Not available.)*

---

## 12. Treatment

**There is no disease-specific or curative therapy.** Management is **supportive, multidisciplinary, and symptom-directed.** **[human clinical — standard of care for severe NDD]**

- **Supportive/rehabilitative (mainstay):**
  - Physical therapy (NCIT:C15367) and occupational therapy (NCIT:C15220) for hypotonia, motor delay, contracture prevention.
  - Speech and language therapy / AAC (augmentative-alternative communication) for absent language.
  - Special education and developmental/early-intervention services.
  - Nutritional support/feeding management; monitoring for aspiration.
  - Hearing aids / audiologic management for hearing impairment (NCIT:C50075 hearing aid).
- **Pharmacotherapy (symptomatic only):**
  - Antiseizure medications **if** seizures occur (none disease-specific).
  - Behavioral/ADHD and aggression management per standard pediatric neurodevelopmental guidelines (behavioral therapy first-line; pharmacologic agents as indicated).
  - No pharmacogenomic guidance specific to *PSMB1*.
- **Advanced/targeted/experimental therapeutics:** None approved or in trials for NEDMHAL. **Gene therapy, cell therapy, RNA-based therapy, and small-molecule proteostasis modulators are conceptual only.** At the **mechanistic/family level**, the type I IFN/ISR axis (e.g., JAK inhibition for IFN-driven proteasome-associated autoinflammatory syndromes; ISR modulators) is a rational research direction, but **not validated** for the neurodevelopmental proteasomopathies and not applicable to already-completed brain development. *(Experimental — no NCT identifiers for NEDMHAL.)*
- **Treatment outcomes / adverse events:** Not applicable (no disease-specific therapy).
- **Treatment strategy:** Individualized supportive care coordinated by pediatric neurology, clinical genetics, rehabilitation medicine, audiology, and developmental pediatrics; genetic counseling for the family.

Suggested NCIT intervention terms: **Physical Therapy (C15367), Occupational Therapy (C15220), Speech Therapy (C15311), Supportive Care (C15277), Genetic Counseling (C15687).**

---

## 13. Prevention

- **Primary prevention:** Not achievable at the individual biological level (constitutional genetic disease). Population-level risk reduction relates to **consanguinity awareness/education** and **genetic counseling** in high-risk communities.
- **Secondary prevention / early detection:** **Early developmental surveillance** (head circumference, tone, milestones) enables earlier diagnosis and initiation of supportive interventions; no biochemical newborn screen exists.
- **Tertiary prevention:** Preventing complications of severe neurodisability (aspiration precautions, orthopedic surveillance, seizure and behavioral management, hearing optimization).
- **Genetic screening/counseling (most relevant):**
  - **Carrier and cascade testing** for at-risk relatives once the familial *PSMB1* variant is known.
  - **Prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** available for couples with a prior affected child (25% recurrence risk per pregnancy for two carriers).
  - Genetic counseling to convey recurrence risk, consanguinity implications, and reproductive options (NSGC/ACMG frameworks).
- **Immunization / public-health / environmental / prophylaxis measures:** Not applicable to a monogenic disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy / conservation:** *PSMB1* is **deeply conserved** with a single ortholog from yeast to human, reflecting an essential proteostasis role. Orthologs (NCBI GeneID): **mouse** *Psmb1* (19170; *Mus musculus*, NCBITaxon:10090), **rat** *Psmb1* (94198; NCBITaxon:10116), **zebrafish** *psmb1* (445413; *Danio rerio*, NCBITaxon:7955), **Drosophila melanogaster** (39855; NCBITaxon:7227), ***Caenorhabditis elegans*** (176161; NCBITaxon:6239), ***S. cerevisiae*** *PRE3* (852239; NCBITaxon:4932), **Xenopus** (394589), **chicken** (421551), plus dog, cow, macaque, and chimpanzee orthologs. **[computational]**
- **Natural disease in other species:** No naturally occurring *PSMB1* Mendelian disease is catalogued in companion animals or wildlife (no OMIA entry identified). *(Not established.)*
- **Comparative biology:** Because the gene and the 20S proteasome architecture are conserved, the disease mechanism (proteasome-assembly deficiency → proteostatic stress) is expected to be evolutionarily conserved; this underpins cross-species modeling. **Zoonotic/cross-species transmission:** not applicable (non-transmissible genetic disorder).

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*), single ortholog *psmb1* (GeneID 445413) — the published disease model.** CRISPR/Cas9 knockout and morpholino knockdown produced **microcephaly, microphthalmia, and reduced brain size**, recapitulating the core human microcephaly/brain-growth phenotype and providing in-vivo causal support. **[model organism]**
  - *"CRISPR/Cas9 mutagenesis or morpholino knock-down of the single psmb1 zebrafish orthologue resulted in microcephaly, microphthalmia and reduced brain size."* — PMID 32129449.
- **In-vitro/cellular models:** Human **SH-SY5Y neuroblastoma cells** expressing p.(Tyr103His) demonstrated impaired β6 processing/incorporation and reduced proteasome activity; **patient-derived cells** (fibroblasts/PBMCs) are the standard substrate for proteasome-activity assays and IFN-signature profiling across proteasomopathies. **[in vitro; human clinical]**
- **Mammalian (mouse/rat) models:** A *PSMB1*-specific NEDMHAL mouse model is **not reported**; constitutive *Psmb1* null is predicted to be **embryonic-lethal** (consistent with high LoF-intolerance), so conditional/hypomorphic or knock-in (p.Tyr103His-equivalent) strategies would be required. Orthologs available at MGI (mouse 19170) and RGD (rat 94198).
- **Invertebrate models (family-level):** Proteasome-NDD mechanisms have been modeled in *Drosophila* (e.g., depletion of the *PSMD11* ortholog *Rpn6* compromised reversal learning; PMID 38866022) — illustrating cognitive-relevant readouts transferable to *PSMB1* study.
- **iPSC/organoid models:** Not yet published for *PSMB1*; cerebral organoids are a logical future platform to model microcephaly and the neurodevelopmental IFN/ISR response.
- **Model characteristics/limitations:** Zebrafish captures **microcephaly/brain-size and eye** phenotypes but not higher cognition/language; cell models capture the **biochemical proteasome defect** but not tissue-level neurodevelopment. Resources: ZFIN (zebrafish), MGI, RGD, FlyBase, WormBase, SGD.

---

## Evidence Summary (key PMIDs)

| PMID | Type | Contribution |
|---|---|---|
| 32129449 (Ansar et al., 2020) | human clinical + in vitro + model organism | **Primary gene–disease discovery**: biallelic *PSMB1* p.(Tyr103His); 20S destabilization; zebrafish microcephaly |
| 38866022 (Deb et al., 2024) | human clinical + model organism | Defines **primary proteasomopathy** class (PSMB1/PSMC1/PSMC3/PSMD12; +PSMD11); 26S-assembly defect → ISR(PKR) → type I IFN |
| 37256937 (Ebstein et al., 2023) | human clinical + in vitro | *PSMC3* NDD with **type I interferon production** (shared mechanism) |
| 42370079 (Wolfgramm et al., 2026) | review | Proteasomopathy framework; shared aggregation/stress/IFN biology; structural modeling for diagnosis |
| 28343629 (OTUD6B, 2017) | human clinical + model organism | Overlapping UPS phenotype (microcephaly, absent speech, hypotonia) — differential |
| 30057029 (FBXO11, 2018) | human clinical | UPS-related NDD — differential |
| 41804662 (PSMD2/3q27.1, 2026) | human clinical | Distinct proteasome CNV disorder — differential/CMA note |

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient cohort** via GeneMatcher/Matchmaker Exchange and consanguineous-population NDD sequencing to identify additional biallelic *PSMB1* families, define the full allelic spectrum, and quantify phenotype frequencies, penetrance, and expressivity.
2. **Formally classify p.(Tyr103His) in ClinVar/ClinGen** by assembling ACMG/AMP evidence — functional (PS3), segregation (PP1), and constraint (PM2) — to close the current interpretation gap for diagnostic laboratories.
3. **Measure the type I interferon / ISG signature** in patient PBMCs and fibroblasts to test whether NEDMHAL shares the IFN-I biomarker of *PSMC3*/*PSMD11* proteasomopathies and to provide a candidate diagnostic/severity biomarker.
4. **Build iPSC-derived neurons and cerebral organoids** from patients to model human microcephaly and the neurodevelopmental ISR/IFN response, and to screen proteostasis-enhancing or IFN-modulating candidate agents.
5. **Generate a hypomorphic knock-in mouse** (p.Tyr103His-equivalent, given predicted null lethality) to study brain growth, behavior/cognition, and candidate therapeutics in vivo.
6. **Conduct a brain-imaging and audiology natural-history study** across identified cases to characterize the structural brain phenotype, hearing-loss trajectory, and prognostic factors.
7. **Explore mechanism-based therapeutics** (proteostasis enhancers; JAK/IFN pathway modulation) in cellular and animal models, with explicit attention to the prenatal critical window in which the neurodevelopmental damage occurs.

---

## Limitations

- **Very small human evidence base** (primarily one consanguineous family); phenotype frequencies, penetrance/expressivity, epidemiology, natural history, and prognosis are qualitative or unavailable.
- Some features (e.g., microphthalmia, precise MRI spectrum) derive from the **model organism** or from **related** proteasomopathies, and may not generalize to every *PSMB1* patient.
- No NEDMHAL-specific omics, biomarker validation, therapeutic trials, mammalian genetic model, or Orphanet/ICD code currently exists.
- Additional patients and functional studies are needed to define the allelic and phenotypic spectrum and to test whether ISR/IFN-targeting strategies have any translational value.


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_with_Microcephaly_Hypotonia_and_Absent_Language-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_with_Microcephaly_Hypotonia_and_Absent_Language-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.