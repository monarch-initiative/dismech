---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T16:49:13.180036'
end_time: '2026-08-28T17:11:38.531189'
duration_seconds: 1345.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spastic Paraplegia 81
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
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spastic_Paraplegia_81-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spastic_Paraplegia_81-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spastic Paraplegia 81
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spastic Paraplegia 81** covering all of the
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

# Spastic Paraplegia 81 (SPG81): A Comprehensive Disease Characteristics Report

**Disease:** Spastic Paraplegia 81 (SPG81)
**OMIM:** #618768 | **MONDO:** 0032905 | **UMLS:** C5394033
**Causal gene:** *SELENOI* (EPT1) | **Inheritance:** Autosomal recessive | **Category:** Mendelian

---

## Summary

Spastic Paraplegia 81 (SPG81) is an ultra-rare, autosomal recessive **complicated hereditary spastic paraplegia (HSP)** caused by **biallelic loss-of-function variants in *SELENOI*** (also known as *EPT1* or *SELI*). *SELENOI* encodes ethanolamine phosphotransferase 1, the enzyme that catalyzes the **final step of the CDP-ethanolamine branch of the Kennedy pathway**, converting CDP-ethanolamine and diacylglycerol (or alkyl-acylglycerol) into **phosphatidylethanolamine (PE)** and its ether-linked form **plasmenyl-PE (a plasmalogen)**. These ethanolamine phospholipids are indispensable membrane constituents, and plasmenyl-PE in particular is critical for **myelination** and serves as a **sacrificial antioxidant** in oligodendrocytes.

Loss of SELENOI activity therefore produces a neurodevelopmental disorder characterized by **infancy-onset, progressive lower-limb spasticity, delayed motor development with subsequent motor regression, impaired intellectual development, and hypomyelination with brain and cerebellar atrophy**. Severely affected individuals additionally develop **sensorineural deafness, cortical/ocular visual loss, seizures, microcephaly, and orofacial anomalies** (bifid uvula/cleft palate). Mechanistically, a nervous-system–restricted *Selenoi*-deficient mouse recapitulates the human phenotype—hypomyelination, reactive gliosis, microcephaly, and motor deficits—driven by **increased lipid peroxidation and impaired maturation of oligodendrocyte-lineage cells**. The disease thus represents a **disorder of ether-lipid/plasmalogen homeostasis** affecting central nervous system myelination.

SPG81 is exceedingly rare: only about **three definitive consanguineous families** (from Oman, Israel, and India) have been reported since 2017, plus a **fourth candidate family** (Korea) carrying a homozygous missense variant of uncertain significance. There is **no disease-specific or disease-modifying therapy**; management is entirely supportive (antispasticity agents, physical/occupational/speech therapy, seizure control, and sensory/orthopedic support). SELENOI also has pleiotropic roles beyond the CNS—in T-cell activation and Th17 differentiation, adipocyte differentiation, tumorigenesis, embryogenesis, and liver physiology—and emerging data link SELENOI/PE dysregulation to motor-neuron degeneration and TDP-43 pathology in ALS, broadening the disease relevance of this pathway.

---

## Key Findings

### Finding 1 — SPG81 is caused by biallelic loss-of-function variants in *SELENOI* (EPT1), disrupting the Kennedy pathway

SPG81 arises from **biallelic (homozygous) loss-of-function variants in *SELENOI***, the gene encoding ethanolamine phosphotransferase 1 (EPT1). The founding report by **Ahmed et al. (2017, *Brain*)** identified a homozygous *SELENOI/EPT1* variant in a consanguineous family with complicated autosomal recessive HSP and demonstrated that the variant **"dramatically reduces the enzymatic activity of EPT1, thereby hindering the final step in phosphatidylethanolamine synthesis."** SELENOI catalyzes the **third and final reaction of the CDP-ethanolamine branch of the Kennedy pathway** (CDP-ethanolamine + diacylglycerol/alkyl-acylglycerol → PE / plasmanyl-PE).

- Disease identifiers: **OMIM #618768**; gene **SELENOI** (HGNC:30396; aliases *EPT1*, *SELI*); locus **chromosome 2p23.3**; NCBI Gene 85465; Ensembl ENSG00000112782; UniProt Q9C0D9.

> [PMID: 28052917](https://pubmed.ncbi.nlm.nih.gov/28052917/): *"associated with mutation in the ethanolaminephosphotransferase 1 (EPT1) gene (now known as SELENOI), responsible for the final step in Kennedy pathway forming phosphatidylethanolamine from CDP-ethanolamine."*

> [PMID: 28052917](https://pubmed.ncbi.nlm.nih.gov/28052917/): *"the mutation defined dramatically reduces the enzymatic activity of EPT1, thereby hindering the final step in phosphatidylethanolamine synthesis."*

> [PMID: 27645994](https://pubmed.ncbi.nlm.nih.gov/27645994/): *"SELENOI (selenoprotein I, SELI, EPT1)"* — confirming gene nomenclature and synonyms.

This finding establishes the **causal gene, its enzymatic role, and loss-of-function as the molecular disease mechanism**.

### Finding 2 — SELENOI-derived plasmenyl-PE is essential for myelination; deficiency causes hypomyelination, lipid peroxidation, and microcephaly

The central mechanistic insight is that **SELENOI-derived plasmenyl-PE (a plasmalogen) is essential for myelination**, and its deficiency produces the neuropathology of SPG81. **Nunes et al. (2024)** generated a **nervous-system–restricted *Selenoi*-deficient mouse** (necessary because constitutive knockout is embryonic lethal) that faithfully recapitulated HSP features. Brain lipid composition alterations **"coincided with motor deficits and neuropathology including hypomyelination, elevated reactive gliosis, and microcephaly,"** with **"increased lipid peroxidation in oligodendrocyte lineage cells and disrupted oligodendrocyte maturation both in vivo and in vitro."** Plasmenyl-PE contains a **vinyl-ether bond** that "preferentially reacts with oxidants" and thus acts as a **sacrificial antioxidant**, protecting membranes from peroxidative damage.

> [PMID: 38582453](https://pubmed.ncbi.nlm.nih.gov/38582453/): *"motor deficits and neuropathology including hypomyelination, elevated reactive gliosis, and microcephaly."*

> [PMID: 38582453](https://pubmed.ncbi.nlm.nih.gov/38582453/): *"increased lipid peroxidation in oligodendrocyte lineage cells and disrupted oligodendrocyte maturation both in vivo and in vitro."*

> [PMID: 38582453](https://pubmed.ncbi.nlm.nih.gov/38582453/): *"a critical role for SELENOI-derived plasmenyl-PE in myelination that is of paramount importance for neurodevelopment."*

> [PMID: 38582453](https://pubmed.ncbi.nlm.nih.gov/38582453/): *"characterized by a vinyl ether bond that preferentially reacts with oxidants, thus serves as a sacrificial antioxidant."*

Complementary human/in-vitro work by **Horibata et al. (2018)** established that EPT1/SELENOI is critical for neural development and maintenance of plasmalogens. Together these define the **cellular mechanism: oligodendrocyte dysfunction and oxidative membrane damage → hypomyelination → progressive neurodegeneration**.

### Finding 3 — SELENOI is a bifunctional selenoprotein with roles beyond the CNS

SELENOI is one of the **25 human selenoproteins** and is unusual in being a **bifunctional enzyme**. **Li et al. (2023)** describe two distinct biochemical functions—**"PE regulation and antioxidant potential"**—conferred respectively by its N-terminal **CDP-alcohol phosphotransferase domain** and its C-terminal **selenocysteine (Sec) residue**. This dual functionality underlies its involvement in **"neurological diseases (especially hereditary spastic paraplegia), T cell activation, tumorigenesis, and adipocyte differentiation."** The essentiality of the gene is underscored by embryonic lethality of the constitutive knockout, meaning **only partial (hypomorphic) loss of function is compatible with survival**, consistent with SPG81 being caused by residual-activity alleles.

> [PMID: 36963501](https://pubmed.ncbi.nlm.nih.gov/36963501/): *"neurological diseases (especially hereditary spastic paraplegia), T cell activation, tumorigenesis, and adipocyte differentiation."*

> [PMID: 36007576](https://pubmed.ncbi.nlm.nih.gov/36007576/): *"Deletion of SELENOI in mice is embryonic lethal."*

> [PMID: 40107406](https://pubmed.ncbi.nlm.nih.gov/40107406/): *"how Selenoi loss-of-function affects embryogenesis, neurodevelopment, the immune system and liver physiology."*

### Finding 4 — Clinical phenotype: infancy-onset complicated HSP with spasticity, intellectual disability, and sensory/neuroimaging abnormalities

Across the reported families, SPG81 presents as an **infancy-onset complicated HSP**. Per OMIM #618768 / MONDO:0032905, it is an **"autosomal recessive neurologic disorder with onset in infancy... delayed motor development, progressive spasticity... impaired intellectual development and speech delay,"** with additional features in some patients including **bifid uvula, microcephaly, seizures, and variable ocular anomalies.** The most severely affected patient reported had **cortical visual loss, sensorineural deafness, and achievement of almost no developmental milestones.**

**Sarma et al. (2023)** summarize the combined phenotypic spectrum: **"sensorineural deafness, blindness, cleft palate, delayed motor development, regression of motor skills, impaired intellectual development, poor speech and language acquisition, spasticity, hyperreflexia, white matter abnormalities and cerebral and cerebellar atrophy."** **Horibata et al. (2018)** described a patient with **"severe complicated hereditary spastic paraplegia, sensorineural-deafness, blindness, and seizures. Neuroimaging revealed hypomyelination, followed by brain atrophy mainly in the cerebellum and brainstem."**

> [PMID: 29500230](https://pubmed.ncbi.nlm.nih.gov/29500230/): *"severe complicated hereditary spastic paraplegia, sensorineural-deafness, blindness, and seizures. Neuroimaging revealed hypomyelination, followed by brain atrophy mainly in the cerebellum and brainstem."*

> [PMID: 36942482](https://pubmed.ncbi.nlm.nih.gov/36942482/): *"sensorineural deafness, blindness, cleft palate, delayed motor development, regression of motor skills, impaired intellectual development, poor speech and language acquisition, spasticity, hyperreflexia, white matter abnormalities and cerebral and cerebellar atrophy."*

**Suggested HPO terms:** Spastic paraplegia (HP:0001258), Lower limb spasticity (HP:0002061), Hyperreflexia (HP:0001347), Intellectual disability (HP:0001249), Motor delay (HP:0001270), Developmental regression (HP:0002376), Sensorineural hearing impairment (HP:0000407), Cortical visual impairment (HP:0100704), Seizure (HP:0001250), Microcephaly (HP:0000252), Cerebellar atrophy (HP:0001272), Cerebral atrophy (HP:0002059), Cerebral hypomyelination (HP:0006808), Bifid uvula (HP:0000193), Cleft palate (HP:0000175), Speech delay (HP:0000750).

### Finding 5 — Variant spectrum: rare biallelic splice-disrupting/LOF *SELENOI* variants in consanguineous families

All definitive families are **autosomal recessive with homozygous variants**. **Sarma et al. (2023)** noted **"only two families reported to date"** at the time and identified **"a homozygous, synonymous variant in the SELENOI gene (NM_033505.4:c.126G>A:p.(Lys42Lys))"** that was found to **"disrupt normal splicing and lead to skipping of exon 2, causing in-frame deletion of SELENOI N-terminal 23 amino acids [NM_033505.4:c.57_126del:p.(Tyr20_Lys42del)]."** Horibata (2018) identified a novel exon-skipping mutation, and Ahmed (2017) identified a variant that dramatically reduces EPT1 activity. Disease-causing alleles are **private/family-specific**; SELENOI has ~101 ClinVar submissions dominated by VUS/benign population variants.

> [PMID: 36942482](https://pubmed.ncbi.nlm.nih.gov/36942482/): *"homozygous, synonymous variant in the SELENOI gene (NM_033505.4:c.126G>A:p.(Lys42Lys))."*

> [PMID: 36942482](https://pubmed.ncbi.nlm.nih.gov/36942482/): *"disrupt normal splicing and lead to skipping of exon 2, causing in-frame deletion of SELENOI N-terminal 23 amino acids."*

> [PMID: 36942482](https://pubmed.ncbi.nlm.nih.gov/36942482/): *"with only two families reported to date."*

### Finding 6 — Lipidomic biomarker signature: reduced polyunsaturated PE and plasmenyl-PE with compensatory shifts

**Horibata et al. (2018)** quantified phospholipids by LC-MS/MS in patient fibroblasts and EPT1-knockout HeLa cells, finding **markedly reduced in-vitro EPT activity**, decreased biosynthesis of ethanolamine glycerophospholipids, **reduced polyunsaturated PE species (38:6, 38:4, 40:6, 40:5, 40:4)**, and significant decreases in most plasmenyl-PE species, while most plasmanyl-PC species increased (a compensatory shift). **Ahmed et al. (2017)** found in patient blood **"alteration to levels of specific phosphatidylethanolamine fatty acyl species in patients,"** although **"in blood EPT1 inactivity may be compensated for, in part, via alternate biochemical pathways"**—explaining why blood PE is a poor diagnostic biomarker despite the enzymatic defect. A **cellular (fibroblast) EPT activity assay and tissue lipidomics** are the most informative biochemical readouts.

> [PMID: 28052917](https://pubmed.ncbi.nlm.nih.gov/28052917/): *"alteration to levels of specific phosphatidylethanolamine fatty acyl species in patients."*

> [PMID: 28052917](https://pubmed.ncbi.nlm.nih.gov/28052917/): *"in blood EPT1 inactivity may be compensated for, in part, via alternate biochemical pathways."*

### Finding 7 — SELENOI-dependent ethanolamine phospholipid synthesis drives T-cell metabolic reprogramming and Th17 differentiation (immune pleiotropy)

Beyond the CNS, SELENOI has immunologic roles. **Ma et al. (2021)** showed that **SELENOI knockout in mouse T cells led to "reduced de novo synthesis of PE and plasmenyl PE during activation and impaired proliferation,"** with reduced AMPK activation, ATP accumulation, and reduced GPI-anchor synthesis/attachment. **Ma et al. (2022)** demonstrated that SELENOI KO **"skewed differentiation away from pathogenic Th17 cells"** toward tolerogenic phenotypes (Foxp3+/IL-10+), and that T-cell-specific KO mice in the EAE autoimmune model showed **"diminished clinical symptoms, reduced CNS pathology and decreased T cell infiltration."** These immune roles are relevant for understanding the broader biology of the gene, though their contribution to the SPG81 neurologic phenotype is not established.

> [PMID: 33484950](https://pubmed.ncbi.nlm.nih.gov/33484950/): *"reduced de novo synthesis of PE and plasmenyl PE during activation and impaired proliferation."*

> [PMID: 35916034](https://pubmed.ncbi.nlm.nih.gov/35916034/): *"skewed differentiation away from pathogenic Th17 cells."*

> [PMID: 35916034](https://pubmed.ncbi.nlm.nih.gov/35916034/): *"diminished clinical symptoms, reduced CNS pathology and decreased T cell infiltration."*

### Finding 8 — Model organisms: constitutive KO embryonic lethal; nervous-system conditional KO recapitulates HSP; cellular models available

The mouse ortholog is *Selenoi* (Mus musculus, NCBI Taxon 10090). **Constitutive/global knockout is embryonic lethal**, so faithful modeling required **conditional (nervous-system–restricted) knockout**, which recapitulates SPG81 features. Cellular models include **patient-derived skin fibroblasts** and **EPT1-KO HeLa cells**, both reproducing the lipid defect.

> [PMID: 38582453](https://pubmed.ncbi.nlm.nih.gov/38582453/): *"developed a mouse model of nervous system-restricted SELENOI deficiency that circumvents embryonic lethality caused by constitutive deletion and recapitulates phenotypic features of hereditary spastic paraplegia."*

> [PMID: 36007576](https://pubmed.ncbi.nlm.nih.gov/36007576/): *"Deletion of SELENOI in mice is embryonic lethal."*

> [PMID: 40107406](https://pubmed.ncbi.nlm.nih.gov/40107406/): *"global and conditional knockout (KO) of the Selenoi gene in mice."*

### Finding 9 — Epidemiology, prognosis, and management

SPG81 is **ultra-rare**: fewer than ~10 patients from 3 consanguineous families (Oman, Israel, India) have been published since 2017; prevalence/incidence are not formally estimated (Orphanet lists no point prevalence). **Inheritance is autosomal recessive**; both sexes are affected; **consanguinity is the principal risk factor**; there is no known founder allele, and carrier frequency for pathogenic alleles is presumably very low (SELENOI LOF is depleted in gnomAD). **Prognosis** is poor: infancy onset, progressive course with motor regression, and severe neurodevelopmental disability; the severe end of the spectrum features near-absent developmental milestones, blindness, and deafness. **No cure or disease-modifying therapy exists**; management is supportive/symptomatic (antispasticity agents such as baclofen/tizanidine, physical/occupational/speech therapy, antiepileptics, sensory aids, nutritional and orthopedic support). Genetic counseling, carrier testing, and prenatal/preimplantation genetic testing are indicated for at-risk consanguineous families once the familial variant is known.

> [PMID: 36942482](https://pubmed.ncbi.nlm.nih.gov/36942482/): *"recently identified, rare autosomal recessive disease, caused by biallelic pathogenic variants in the SELENOI gene."*

> [PMID: 29500230](https://pubmed.ncbi.nlm.nih.gov/29500230/): *"severe complicated hereditary spastic paraplegia, sensorineural-deafness, blindness, and seizures."*

### Finding 10 — Fourth candidate family expands variant spectrum to a homozygous missense VUS (p.Pro266Leu)

**Lee et al. (2026, Korea)** reported a consanguineous family of six siblings; the index patient and a younger brother carried a **homozygous *SELENOI* c.797C>T (p.Pro266Leu) variant of uncertain significance**, interpreted in the context of an SPG81-like phenotype (significant lower-limb weakness, spasticity, developmental delay). Notably, other siblings' phenotypes were explained by different genes (*LAMA1* p.Gln1527Ter → Poretti-Boltshauser syndrome; a de novo *SATB2* VUS), illustrating **intrafamilial genetic heterogeneity**. This is the **first reported homozygous SELENOI missense candidate variant**, contrasting with the splice-affecting/in-frame-deletion alleles of the three prior definitive families.

> [PMID: 42446524](https://pubmed.ncbi.nlm.nih.gov/42446524/): *"We report a family of six siblings born to asymptomatic consanguineous parents, in which three siblings exhibited overlapping spastic paraplegia phenotypes with developmental delay."*

### Finding 11 — SELENOI/PE dysregulation links to motor-neuron degeneration and TDP-43 pathology in ALS

**Isik et al. (2025)** found that in human ALS brain, **"PE levels were significantly decreased in the disease-affected motor cortex of ALS compared to controls and were inversely associated with disease duration,"** while PE was unaltered in the disease-unaffected cerebellum. **"SELENOI expression was dysregulated only in the motor cortex,"** the SELENOI–TDP-43 correlation was lost, and **"knockdown of SELENOI expression in neuronal cells caused an upregulation of TDP-43 expression."** The authors explicitly note that **"SELENOI is important in motor neuron development and function, as demonstrated in hereditary spastic paraplegia,"** linking the SPG81 pathway to broader motor-neuron disease.

> [PMID: 41002422](https://pubmed.ncbi.nlm.nih.gov/41002422/): *"PE levels were significantly decreased in the disease-affected motor cortex of ALS compared to controls and were inversely associated with disease duration."*

> [PMID: 41002422](https://pubmed.ncbi.nlm.nih.gov/41002422/): *"SELENOI is important in motor neuron development and function, as demonstrated in hereditary spastic paraplegia."*

---

## Mechanistic Model / Interpretation

SPG81 is fundamentally a **disorder of ether-lipid (plasmalogen) homeostasis** affecting CNS myelination. The causal chain runs from a genetic defect in a single enzymatic step to a progressive neurodevelopmental/neurodegenerative phenotype:

```
Biallelic LOF SELENOI (EPT1)  [chr 2p23.3]
          │
          ▼
Reduced ethanolamine phosphotransferase activity
(final step of CDP-ethanolamine / Kennedy pathway)
          │
          ▼
↓ Phosphatidylethanolamine (PE)  &  ↓↓ plasmenyl-PE (plasmalogen)
   (compensatory ↑ plasmanyl-PC in some tissues)
          │
          ├──────────────► Loss of "sacrificial antioxidant" (vinyl-ether bond)
          │                          │
          ▼                          ▼
Impaired oligodendrocyte      ↑ Lipid peroxidation in
maturation                    oligodendrocyte-lineage cells
          │                          │
          └──────────┬───────────────┘
                     ▼
        HYPOMYELINATION + reactive gliosis + microcephaly
                     │
                     ▼
   Progressive spasticity, motor regression, intellectual
   disability, sensorineural deafness, visual loss, seizures,
   cerebral/cerebellar atrophy
```

**Upstream vs downstream:** The upstream trigger is the enzymatic deficiency and consequent depletion of ethanolamine phospholipids (especially plasmenyl-PE). Downstream consequences are oligodendrocyte-lineage lipid peroxidation and maturation failure, producing hypomyelination and, over time, neurodegeneration/atrophy.

**Cell types and processes involved:** Oligodendrocytes/oligodendrocyte precursor cells (CL:0000128 oligodendrocyte; CL:0002453 oligodendrocyte precursor cell) are the key effector cells; upper motor neurons and corticospinal tract axons (long descending tracts) manifest the classic HSP length-dependent "dying-back" degeneration. **Suggested GO terms:** phosphatidylethanolamine biosynthetic process (GO:0006646), CDP-ethanolamine pathway (GO:0006657), ether lipid biosynthetic process (GO:0008611), myelination (GO:0042552), oligodendrocyte differentiation (GO:0048709), response to oxidative stress (GO:0006979), ethanolamine phosphotransferase activity (GO:0004307). **Cellular components:** endoplasmic reticulum membrane (GO:0005789), myelin sheath (GO:0043209).

**Anatomical structures (UBERON):** brain (UBERON:0000955), cerebellum (UBERON:0002037), brainstem (UBERON:0002298), cerebral white matter (UBERON:0002316), corticospinal tract (UBERON:0005425), spinal cord (UBERON:0002240). **Body system:** central nervous system (UBERON:0001017). Lateralization is bilateral and symmetric, as typical of HSP.

**CHEBI entities:** phosphatidylethanolamine (CHEBI:16038), plasmenyl-ethanolamine/plasmalogen (CHEBI:52590), CDP-ethanolamine (CHEBI:57876), selenocysteine (CHEBI:16633).

| Level | Structure/process affected | Ontology suggestion |
|---|---|---|
| Organ | Brain, cerebellum, brainstem | UBERON:0000955, 0002037, 0002298 |
| System | Central nervous system (corticospinal tracts) | UBERON:0001017, 0005425 |
| Tissue | Cerebral/cerebellar white matter (myelin) | UBERON:0002316 |
| Cell | Oligodendrocytes, OPCs; upper motor neurons | CL:0000128, CL:0002453 |
| Subcellular | ER membrane; myelin sheath | GO:0005789, GO:0043209 |
| Molecule | ↓PE, ↓plasmenyl-PE; ↑lipid peroxidation | CHEBI:16038, 52590 |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report | Evidence type |
|---|---|---|---|
| [28052917](https://pubmed.ncbi.nlm.nih.gov/28052917/) | *A mutation of EPT1 (SELENOI) underlies a new disorder of Kennedy pathway phospholipid biosynthesis* | Founding paper: causal gene, LOF mechanism, blood PE alterations | Human clinical + biochemical |
| [29500230](https://pubmed.ncbi.nlm.nih.gov/29500230/) | *EPT1 (selenoprotein I) is critical for neural development and plasmalogen maintenance* | Severe phenotype, neuroimaging, fibroblast/HeLa lipidomics | Human clinical + in vitro |
| [36942482](https://pubmed.ncbi.nlm.nih.gov/36942482/) | *A novel homozygous synonymous splicing variant in SELENOI causes SPG81* | Third family; exact variant nomenclature; splice mechanism; rarity | Human clinical + molecular |
| [38582453](https://pubmed.ncbi.nlm.nih.gov/38582453/) | *Selenoprotein I is indispensable for ether lipid homeostasis and proper myelination* | Conditional-KO mouse recapitulates HSP; plasmenyl-PE/myelination mechanism | Model organism |
| [36007576](https://pubmed.ncbi.nlm.nih.gov/36007576/) | *Selenoprotein I (Selenoi) as a critical enzyme in the CNS* | Embryonic lethality of global KO | Model organism / review |
| [36963501](https://pubmed.ncbi.nlm.nih.gov/36963501/) | *Biology and Roles in Diseases of Selenoprotein I* | Bifunctionality; pleiotropic disease roles | Review |
| [40107406](https://pubmed.ncbi.nlm.nih.gov/40107406/) | *Insights from selenoprotein I mouse models* | Multi-organ roles from KO models | Review |
| [27645994](https://pubmed.ncbi.nlm.nih.gov/27645994/) | *Selenoprotein Gene Nomenclature* | Confirms SELENOI = SELI = EPT1 | Reference |
| [33484950](https://pubmed.ncbi.nlm.nih.gov/33484950/) | *Ethanolamine phospholipid synthesis via SELENOI in T-cell activation* | Immune role; PE/plasmenyl-PE in T cells | Model organism / in vitro |
| [34681834](https://pubmed.ncbi.nlm.nih.gov/34681834/) | *Roles for Selenoprotein I and Ethanolamine Phospholipid Synthesis in T Cell Activation* | Review of immune metabolic reprogramming | Review |
| [35916034](https://pubmed.ncbi.nlm.nih.gov/35916034/) | *SELENOI deficiency in T cells promotes tolerance, decreases Th17 pathology* | Th17/EAE immune findings | Model organism |
| [42446524](https://pubmed.ncbi.nlm.nih.gov/42446524/) | *HSP in three siblings with distinct genetic mutations* | Fourth candidate family; missense VUS; intrafamilial heterogeneity | Human clinical |
| [41002422](https://pubmed.ncbi.nlm.nih.gov/41002422/) | *Dysregulation of SELENOI associated with TDP-43 neuropathology in ALS* | Broader motor-neuron disease relevance | Human + in vitro |
| [32142958](https://pubmed.ncbi.nlm.nih.gov/32142958/) | *Transcriptional status of selenoproteins in skin cancer cell lines* | SELENOI upregulation in BRAF/NRAS-mutant melanoma (tumor pleiotropy) | In vitro / computational |

**Coherence of evidence:** Human genetic/clinical reports (28052917, 29500230, 36942482, 42446524) converge on biallelic *SELENOI* LOF causing complicated HSP. The mouse conditional-KO study (38582453) provides the definitive mechanistic bridge—directly demonstrating that plasmenyl-PE loss causes hypomyelination via oligodendrocyte lipid peroxidation—and no study contradicts this model. The ALS study (41002422) and immune studies (33484950, 35916034) extend the pathway's relevance without challenging the core SPG81 mechanism.

---

## Section-by-Section Data Compilation

### 1. Disease Information
Complicated autosomal recessive HSP with infancy onset. **Identifiers:** OMIM #618768; MONDO:0032905; UMLS C5394033; gene SELENOI (HGNC:30396). **Synonyms:** SPG81; spastic paraplegia 81, autosomal recessive; SELENOI/EPT1-related HSP. **Source type:** aggregated disease-level resources (OMIM, Orphanet) plus individual case reports; no EHR/registry data.

### 2. Etiology
**Causal factor:** genetic (biallelic LOF *SELENOI*). **Genetic risk factor:** homozygous pathogenic *SELENOI* alleles. **Environmental risk factor:** none identified; **consanguinity** is the dominant risk factor (all definitive families are consanguineous). **Protective factors:** none characterized. **Gene–environment interactions:** none documented. It is a monogenic Mendelian disorder.

### 3. Phenotypes
See Finding 4 and HPO term list. Onset: infancy (congenital/pediatric). Severity: variable but generally severe; progression: progressive with motor regression. Core features (spasticity, hyperreflexia, motor delay, intellectual disability) appear consistent across families; sensory (deafness, blindness), seizures, microcephaly, and orofacial anomalies are variable. Quality of life is severely impacted, with loss of ambulation and profound developmental disability at the severe end.

### 4. Genetic/Molecular Information
**Causal gene:** *SELENOI* (EPT1), 2p23.3, NM_033505.4. **Variant types:** splice-disrupting synonymous (c.126G>A → exon 2 skipping → p.Tyr20_Lys42del), exon-skipping, activity-reducing alleles; plus a candidate missense (c.797C>T, p.Pro266Leu, VUS). **Classification:** pathogenic/likely pathogenic in definitive families; VUS for the missense candidate. **Origin:** germline. **Functional consequence:** loss of function (reduced enzyme activity). **Allele frequency:** private/family-specific; LOF depleted in gnomAD. **Modifier/epigenetic/chromosomal:** none reported.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors. Purely genetic.

### 6. Mechanism / Pathophysiology
See Mechanistic Model. Pathway: CDP-ethanolamine branch of the Kennedy pathway (KEGG glycerophospholipid metabolism). Cellular processes: oligodendrocyte maturation failure, lipid peroxidation/oxidative stress, myelination defect. Protein dysfunction: loss of enzyme activity. Metabolic changes: ↓PE, ↓plasmenyl-PE. Immune involvement: pathway-level (T-cell PE synthesis, Th17) but not part of the SPG81 clinical picture. Transcriptomic/proteomic profiling of patient CNS tissue is not available.

### 7. Anatomical Structures Affected
See table in Mechanistic Model. Primary: CNS white matter/myelin, corticospinal tracts, cerebellum, brainstem. Secondary: sensory systems (auditory, visual). Bilateral, symmetric.

### 8. Temporal Development
Onset: infancy, insidious/chronic. Course: progressive with motor regression; chronic lifelong. No remission. Critical period likely the early postnatal myelination window.

### 9. Inheritance and Population
Autosomal recessive; consanguinity-driven; both sexes; ultra-rare (~3 definitive families, <10 patients); no founder effect; carrier frequency very low; penetrance appears complete in reported homozygotes; expressivity variable (severity ranges from moderate to profound).

### 10. Diagnostics
**Genetic testing** is definitive: WES/WGS or HSP gene panels including *SELENOI*; single-gene/familial variant testing once identified. Careful splice-variant interpretation is needed (synonymous variants can be pathogenic via splicing). **Biochemical:** fibroblast EPT activity assay and lipidomics (↓plasmenyl-PE) are supportive; blood PE is unreliable due to compensation. **Imaging:** MRI shows hypomyelination, cerebral/cerebellar atrophy. **Differential diagnosis:** other complicated HSPs, hypomyelinating leukodystrophies, peroxisomal plasmalogen-biosynthesis disorders (rhizomelic chondrodysplasia punctata), and other Kennedy-pathway/phospholipid disorders.

### 11. Outcome/Prognosis
Poor; progressive disability, motor regression, severe neurodevelopmental impairment; severe cases with blindness, deafness, near-absent milestones. No formal survival data. No disease-specific prognostic biomarkers established; earlier/more severe presentation and severe hypomyelination suggest worse outcome.

### 12. Treatment
**No disease-specific/disease-modifying therapy.** Supportive: antispasticity agents (baclofen, tizanidine, botulinum toxin), physical/occupational/speech therapy, antiepileptic drugs, hearing/visual aids, nutritional and orthopedic support. No pharmacogenomic, gene, cell, or RNA therapy exists. Theoretical/experimental directions (plasmalogen replacement, antioxidants) are unproven for SPG81. **Suggested NCIT terms:** Baclofen (C376), Physical Therapy (C15368), Occupational Therapy (C15218), Supportive Care (C15417).

### 13. Prevention
Primary prevention via genetic counseling for consanguineous families, carrier testing, and prenatal/preimplantation genetic testing once the familial variant is known. No population screening (ultra-rare). No immunization or behavioral prevention applicable.

### 14. Other Species / Natural Disease
Mouse ortholog *Selenoi* (NCBI Taxon 10090). No naturally occurring animal disease reported (no OMIA entry). Gene and pathway are evolutionarily conserved. Not zoonotic.

### 15. Model Organisms
**Mouse:** constitutive KO embryonic lethal; nervous-system–restricted conditional KO recapitulates HSP (hypomyelination, gliosis, microcephaly, motor deficits); T-cell-specific conditional KO for immune studies. **Cellular:** patient skin fibroblasts; EPT1-KO HeLa cells reproduce the lipid defect. Phenotype recapitulation of the neural conditional KO is high. Limitation: no model captures the full multi-sensory human phenotype; global-KO lethality prevents whole-organism study.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity:** Only ~3 definitive families (plus one candidate) exist, limiting genotype–phenotype correlation, penetrance/expressivity estimates, and natural-history data. No prevalence/incidence figures exist.
2. **Missense candidate uncertain:** The p.Pro266Leu allele (Lee 2026) remains a VUS; functional validation is lacking, and the family showed genetic heterogeneity, so SPG81 causation is not confirmed for that variant.
3. **Biomarker limitations:** Blood PE is compensated and unreliable; the most sensitive biochemical assays require patient fibroblasts, limiting non-invasive diagnosis.
4. **No human CNS omics:** Transcriptomic/proteomic/metabolomic profiling of patient brain tissue is unavailable; mechanistic detail derives largely from mouse and cell models.
5. **No therapies tested:** No preclinical or clinical therapeutic studies specific to SPG81; whether plasmalogen supplementation or antioxidants could help is untested.
6. **Citation verification caveats:** A few supporting snippets were flagged during curation (e.g., portions of PMID 29500230, 35916034 quotes); the core claims are corroborated across multiple sources, but exact-quote fidelity should be re-verified before database ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Functional validation of p.Pro266Leu:** Express the missense variant in an EPT1-null cell system and measure ethanolamine phosphotransferase activity and plasmenyl-PE synthesis to resolve its VUS status.
2. **International case aggregation:** Use GeneMatcher/Matchmaker Exchange to identify additional families, enabling genotype–phenotype correlation and natural-history characterization.
3. **Non-invasive biomarker development:** Systematic plasma/CSF lipidomics (plasmalogen panels) across patients and carriers to establish a reliable diagnostic/monitoring biomarker.
4. **Therapeutic proof-of-concept in the conditional-KO mouse:** Test **plasmalogen/ether-lipid precursor supplementation** (e.g., alkyl-glycerols) and **lipophilic antioxidants** for rescue of hypomyelination and motor deficits.
5. **iPSC-derived oligodendrocyte/organoid models:** Generate patient iPSC-derived oligodendrocytes and cerebral organoids to study human oligodendrocyte maturation, lipid peroxidation, and candidate therapeutics.
6. **Cross-disease pathway study:** Given the ALS link (PMID 41002422), examine whether modulating SELENOI/PE affects TDP-43 handling in motor neurons—potentially uncovering shared therapeutic targets across SPG81 and motor-neuron disease.

---

*Report compiled from 11 confirmed findings and 14 reviewed papers over a 5-iteration autonomous investigation. Evidence types span human clinical/genetic reports, model-organism (mouse conditional KO) studies, in-vitro/cellular assays, and computational/transcriptomic analyses.*


## Artifacts

- [OpenScientist final report](Spastic_Paraplegia_81-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spastic_Paraplegia_81-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
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
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002316` (2 mentions) - the report calls it "Cerebral/cerebellar white matter (myelin)"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names

39 of 40 terms resolved to a current term; the rest could not be looked up either way.