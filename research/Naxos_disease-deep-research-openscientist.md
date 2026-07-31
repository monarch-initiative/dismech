---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T01:14:42.274816'
end_time: '2026-07-31T01:35:06.961090'
duration_seconds: 1224.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Naxos disease
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
citation_count: 34
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Naxos_disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Naxos_disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Naxos disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Naxos disease** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Naxos Disease: A Comprehensive Disease Characteristics Report

## Summary

**Naxos disease** is a rare **autosomal recessive cardiocutaneous syndrome** defined by the triad of **arrhythmogenic right ventricular cardiomyopathy (ARVC)**, **woolly hair** (present from birth), and **palmoplantar keratoderma** (developing in the first year of life). It was first described in families from the Greek island of Naxos and is caused by homozygous loss-of-function mutation of **plakoglobin (JUP)** — most classically the founder frameshift deletion **c.2157del2 (p.Ser710fs)** on chromosome **17q21** ([PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)). Plakoglobin (γ-catenin) is a core component of the desmosome and adherens-junction "composite junction" of the cardiomyocyte intercalated disk; its loss destabilizes cell–cell adhesion and, under mechanical/exercise stress, drives progressive myocyte death and fibrofatty myocardial replacement.

The cardiac phenotype is the life-limiting feature: it is **100% penetrant** in adult homozygotes, manifesting by adolescence (the youngest patient fulfilled ARVC criteria by age 13), and carries an **annual disease-related mortality of ~3%** and **sudden-death mortality of ~2.3%** ([PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)). The cutaneous phenotype is congenital/infantile and therefore serves as an early clinical flag that should trigger cardiac surveillance well before arrhythmias appear. Mechanistically, three interlocking processes are established: (1) mutant plakoglobin fails to localize at intercalated disks and causes early **connexin43 (Cx43) gap-junction and NaV1.5 sodium-channel remodeling** — an arrhythmogenic substrate present even before overt structural disease ([PMID: 15851108](https://pubmed.ncbi.nlm.nih.gov/15851108/), [PMID: 23178689](https://pubmed.ncbi.nlm.nih.gov/23178689/)); (2) **nuclear translocation of plakoglobin suppresses canonical Wnt/β-catenin signaling** through Tcf/Lef1, switching on adipogenic and fibrogenic gene programs and producing the characteristic fibrofatty replacement ([PMID: 16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/)); and (3) **"myocarditis-like" hot-phase episodes** and mechanical stress accelerate the transition from a concealed to a symptomatic, fibrofatty end-stage phenotype ([PMID: 34776086](https://pubmed.ncbi.nlm.nih.gov/34776086/)).

There is **no curative therapy**. Management follows ARVC and heart-failure guidelines: exercise restriction, antiarrhythmic drugs, catheter ablation, and **implantable cardioverter-defibrillator (ICD)** placement for sudden-death prevention, with cardiac transplantation reserved for end-stage failure ([PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/), [PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/)). A promising translational lead is **GSK3β inhibition (SB216763)**, which rescues and partly reverses the arrhythmogenic phenotype across zebrafish, neonatal-rat-cardiomyocyte, and iPSC models, and normalizes junctional protein distribution in patient-derived cells ([PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/), [PMID: 26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/)).

---

## 1. Disease Information

**Overview.** Naxos disease is a recessively inherited syndrome combining ARVC with a distinctive cutaneous phenotype (woolly hair + palmoplantar keratoderma). It was originally described in families from the Greek island of Naxos, with additional families identified across the Aegean islands, Turkey, Israel, Saudi Arabia, and beyond. A closely related allelic/phenotypic variant with predominantly **left ventricular** involvement — **Carvajal syndrome** — is caused by desmoplakin (DSP) mutations and described in families from India and Ecuador ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/), [PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | **601214** (Naxos disease) |
| Orphanet | ORPHA:34217 |
| MeSH | Naxos disease / Arrhythmogenic Right Ventricular Dysplasia |
| Gene (Naxos) | **JUP** (plakoglobin), OMIM *173325, 17q21.2 |
| Related (Carvajal) | **DSP** (desmoplakin), OMIM 605676 |
| MONDO | Mendelian cardiocutaneous ARVC syndrome (map to MONDO Naxos/ARVC entry) |

> Note: OMIM/Orphanet numeric IDs above are the standard catalog entries for this disorder; the investigation's primary-literature anchor for the gene and locus is [PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/).

**Synonyms / alternative names:** Naxos disease; cardiocutaneous syndrome; ARVC with palmoplantar keratoderma and woolly hair; plakoglobin-related arrhythmogenic cardiomyopathy. The DSP-associated left-dominant form is **Carvajal syndrome** (Naxos disease variant).

**Source of information:** Predominantly **aggregated disease-level resources** and family-based cohort/natural-history studies (Protonotarios, McKoy, Antoniades cohorts) rather than individual EHR records; complemented by case series (e.g., a 10-patient Saudi pediatric Carvajal-variant cohort, [PMID: 40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/)).

---

## 2. Etiology

**Primary cause — genetic.** Naxos disease is a **Mendelian, autosomal recessive** disorder. The causal event is **homozygous loss of functional plakoglobin** due to a **2-bp deletion in JUP (c.2157del2; p.Ser710fs)** producing a frameshift and premature truncation, confirmed by Western blot ([PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)). The disease is thus fundamentally a **cell-adhesion (desmosomal) cardiomyopathy** rather than an environmental or infectious disorder.

> *"A homozygous 2 base pair deletion in the plakoglobin gene was identified only in the 19 affected individuals. This deletion caused a frameshift and premature termination of the protein, which was shown by western blot analysis."* — McKoy et al., [PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)

**Genetic risk factors.** The homozygous JUP truncation is fully causal (not merely a susceptibility allele). Heterozygous carriers (parents, unaffected relatives) are clinically unaffected for the full syndrome, consistent with recessive inheritance ([PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)). The related recessive syndrome maps to **DSP** (Carvajal); dominant non-syndromic ARVC is caused by heterozygous mutations in **PKP2, DSG2, DSC2, DSP** ([PMID: 16698823](https://pubmed.ncbi.nlm.nih.gov/16698823/)).

**Environmental risk factors / disease modifiers.** No environmental factor *causes* Naxos disease, but **strenuous/endurance exercise and mechanical stress are major disease-accelerating modifiers**: desmosomal junctions fail preferentially "under conditions of increased mechanical stress or stretch, leading to cell death, progressive loss of myocardium and fibro-fatty replacement" ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/)). In transgenic DSP models, **endurance exercise accelerates arrhythmogenic remodeling** via perturbed AKT1/GSK3β signaling ([PMID: 26545710](https://pubmed.ncbi.nlm.nih.gov/26545710/)). Male sex and vigorous exercise are recognized adverse modifiers in ARVC more broadly.

**Protective factors.** No validated genetic protective alleles are established for Naxos disease specifically. The clearest *modifiable protective factor* is **avoidance of competitive/endurance exercise**, which reduces the mechanical stress that drives progression.

**Gene–environment interaction.** The central GxE axis is **desmosomal loss-of-function × mechanical load**: an intrinsically weakened intercalated disk tolerates normal contraction poorly, so exercise-induced wall stress converts a genetically primed but "concealed" myocardium into a symptomatic, fibrofatty, arrhythmic one ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/), [PMID: 26545710](https://pubmed.ncbi.nlm.nih.gov/26545710/)).

---

## 3. Phenotypes

Naxos disease has an obligate **cutaneous** phenotype (congenital/infantile) and an obligate **cardiac** phenotype (adolescent-onset).

| Phenotype | Type | Onset | Severity / course | Frequency | HPO term (suggested) |
|---|---|---|---|---|---|
| Woolly hair | Physical manifestation (hair) | From birth (congenital) | Stable, non-progressive | ~100% | HP:0002216 (Woolly hair) |
| Palmoplantar keratoderma | Physical manifestation (skin) | First year of life | Stable/slowly progressive | ~100% (Naxos); ~50% in some Carvajal cohorts | HP:0000982 (Palmoplantar keratoderma) |
| Arrhythmogenic RV cardiomyopathy | Clinical sign / structural | Adolescence | Progressive | 100% of adult homozygotes | HP:0011663 (Right ventricular cardiomyopathy) |
| Ventricular tachycardia / arrhythmia | Clinical sign (electrophysiologic) | Adolescence–adulthood | Episodic, life-threatening | ~92% | HP:0004756 (Ventricular arrhythmia) |
| ECG abnormalities (T-wave inversion V1–V3) | Laboratory/electrophysiologic | Adolescence | Progressive | ~92% | HP:0012248 (Abnormal ECG) |
| RV structural alteration | Clinical sign (imaging) | Adolescence | Progressive | 100% | HP:0001714 |
| Left ventricular involvement | Clinical sign | Later / variable | Progressive | ~27% (Naxos); dominant in Carvajal | HP:0001644 (Dilated cardiomyopathy) |
| Syncope | Symptom | Adolescence–adult | Episodic | Common | HP:0001279 |
| Sudden cardiac death | Outcome | Young adulthood | Catastrophic | ~2.3%/yr | HP:0001645 (Sudden cardiac death) |
| Heart failure (right, then bi-ventricular) | Clinical sign | End-stage | Progressive | ~27% develop HF | HP:0001635 |

**Detailed characteristics.** In the definitive natural-history cohort (12 families, 26 adult homozygotes), **all adults who were homozygous fulfilled ARVC criteria, the youngest by age 13** ([PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)). Among affected homozygotes: **92% ECG abnormalities, 92% ventricular arrhythmias, 100% RV structural alterations, and 27% LV involvement.** Over ~10 ± 6 years of follow-up, **62% showed structural progression, 46% had arrhythmic events, and 27% developed heart failure**.

> *"All adults who were homozygous (n = 26) fulfilled the diagnostic criteria for ARVC, the youngest by the age of 13 years."* — [PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)

The **temporal sequence is diagnostically important**: *"woolly hair appears from birth, palmoplantar keratoderma develop during the first year of life and cardiomyopathy is clinically manifested by adolescence with 100% penetrance"* ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/)); across 22 affected families *"all patients had the hair and skin phenotype from infancy and developed ARVC by adolescence"* ([PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/)).

**Quality-of-life impact.** The cutaneous features cause modest QoL impact (cosmetic, keratoderma discomfort). The cardiac phenotype dominates: exercise restriction, ICD implantation, arrhythmia burden, and heart-failure symptoms substantially impair daily functioning; sudden-death risk imposes major psychosocial burden on patients and families. No disease-specific validated QoL instrument (EQ-5D/SF-36) data were identified for Naxos disease.

---

## 4. Genetic / Molecular Information

**Causal gene.** **JUP** — junction plakoglobin (γ-catenin); HGNC:6207; OMIM *173325; chromosome **17q21.2**. Loss of functional plakoglobin is the primary lesion in Naxos disease ([PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)).

**Canonical pathogenic variant.**

| Attribute | Detail |
|---|---|
| Variant | **c.2157del2 (TG deletion) / p.Ser710fs** ("2157del2"; also written 2057del2 in some model papers) |
| Type | Frameshift → premature termination (truncating) |
| Classification | **Pathogenic** (ACMG); recessive, biallelic required |
| Zygosity in affected | Homozygous |
| Functional consequence | **Loss of function** — truncated plakoglobin; mislocalization from intercalated disk |
| Origin | Germline |
| Population frequency | Rare; **founder allele** on Naxos/Aegean islands; essentially absent from general population databases (gnomAD) |

The frameshift was found **only** in the 19 affected homozygotes, with 29 unaffected relatives heterozygous and 20 unrelated islanders plus 43 dominant-ARVC probands homozygous wild-type — establishing both causality and a **founder effect** ([PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)).

**Allelic / related genes.** The **Carvajal (Naxos-variant) form** is caused by homozygous truncating **DSP** mutations — e.g., c.4297C>T (p.Gln1433*) ([PMID: 38433550](https://pubmed.ncbi.nlm.nih.gov/38433550/)) and c.8586delC (p.Ser2863Hisfs*20) at the extreme C-terminus ([PMID: 37143080](https://pubmed.ncbi.nlm.nih.gov/37143080/)). In a Saudi pediatric cohort, **8/8 genetically tested Carvajal-variant patients were homozygous for DSP** ([PMID: 40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/)). Recessive cardiocutaneous overlap also arises from **desmocollin-2 (DSC2)** mutations ([PMID: 25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/)). A comprehensive junctional-protein thesaurus catalogs DSC2, DSG2, DSP, JUP, PKP2 and non-desmosomal genes (TMEM43, RYR2, desmin, lamin A/C, TTN, TGFβ3) associated with ARVC/Naxos/Carvajal ([PMID: 22450909](https://pubmed.ncbi.nlm.nih.gov/22450909/)).

**Modifier genes.** No specific modifier locus is validated for Naxos disease; **DSP** and **desmin** variants associate with a more heart-failure-prone ACM phenotype generally ([PMID: 42372975](https://pubmed.ncbi.nlm.nih.gov/42372975/)). Genotype–phenotype work suggests the *site* of the desmosomal defect (outer vs inner dense plaque) shapes RV- vs LV-dominant expression ([PMID: 16698823](https://pubmed.ncbi.nlm.nih.gov/16698823/)).

**Epigenetic / chromosomal information.** No recurrent epigenetic signature or large-scale chromosomal abnormality is described for Naxos disease; it is a single-gene point/indel disorder.

---

## 5. Environmental Information

- **Environmental/toxic factors:** None causal. No toxin, radiation, or occupational exposure is implicated in disease *causation*.
- **Lifestyle factors:** **Strenuous, competitive, and endurance exercise** is the principal deleterious lifestyle exposure — it accelerates myocyte loss and fibrofatty remodeling in genetically susceptible myocardium ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/), [PMID: 26545710](https://pubmed.ncbi.nlm.nih.gov/26545710/)). Exercise restriction is therefore a cornerstone of management/prevention.
- **Infectious agents:** None cause Naxos disease. However, the phenotype can **mimic acute myocarditis** ("myocarditis-like"/"hot-phase" episodes), which are sterile inflammatory manifestations of desmosomal injury rather than true infection ([PMID: 34776086](https://pubmed.ncbi.nlm.nih.gov/34776086/), [PMID: 42406223](https://pubmed.ncbi.nlm.nih.gov/42406223/), [PMID: 38652395](https://pubmed.ncbi.nlm.nih.gov/38652395/)).

---

## 6. Mechanism / Pathophysiology

### Causal chain

```
Homozygous JUP truncation (c.2157del2)
        │
        ▼
Loss of functional plakoglobin at intercalated disk
        │
        ├──► Composite-junction (desmosome + adherens) destabilization
        │        │
        │        ▼
        │   Mechanical-stress–induced myocyte detachment & death
        │
        ├──► Cx43 gap-junction + NaV1.5 remodeling (EARLY, pre-structural)
        │        │
        │        ▼
        │   Slowed conduction → reentry → ventricular arrhythmia / SCD
        │
        └──► Nuclear translocation of plakoglobin
                 │
                 ▼
             Suppression of canonical Wnt/β-catenin (Tcf/Lef1) ↓2-fold
                 │
                 ▼
             ↑ Adipogenic + fibrogenic gene programs
                 │
                 ▼
             Fibrofatty replacement of myocardium (subepicardial/mediomural)
                 │
                 ▼
             RV (± LV) dysfunction, heart failure
```

**Molecular pathways.** The defining pathway is **canonical Wnt/β-catenin signaling suppression by nuclear plakoglobin**. Garcia-Gras et al. showed that suppressing desmoplakin drives plakoglobin into the nucleus, producing a **2-fold reduction in Wnt/β-catenin signaling through Tcf/Lef1**, with resulting up-regulation of adipogenic and fibrogenic genes and fat-droplet accumulation ([PMID: 16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/)).

> *"suppression of DP expression leads to nuclear localization of the desmosomal protein plakoglobin and a 2-fold reduction in canonical Wnt/beta-catenin signaling through Tcf/Lef1 transcription factors. The ensuing phenotype is increased expression of adipogenic and fibrogenic genes and accumulation of fat droplets."* — [PMID: 16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/)

A parallel and druggable node is **GSK3β**: GSK3β inhibition (SB216763) rescues the arrhythmogenic phenotype in a Naxos-specific plakoglobin (2057del2) zebrafish model, in neonatal rat cardiomyocytes, and in PKP2-mutant iPSC-cardiomyocytes ([PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/)), and reverses abnormal plakoglobin/Cx43 distribution in patient buccal cells ([PMID: 26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/)). **RhoA-ROCK** signaling has been modeled as a co-contributor to loss of cardiomyocyte identity ([PMID: 33670616](https://pubmed.ncbi.nlm.nih.gov/33670616/)).

> *"SB21 was able to rescue and partly reverse the ACM phenotype in three different experimental models: (I) a zebrafish model of Naxos disease induced by the overexpression of the 2057del2 mutation in plakoglobin"* — [PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/)

**Cellular processes.** (i) **Loss of cell–cell adhesion** and myocyte death (apoptosis) under mechanical stress; (ii) **gap-junction remodeling** reducing intercellular electrical coupling; (iii) **transdifferentiation/adipogenesis + fibrosis** replacing lost myocytes; (iv) episodic **inflammation** ("myocarditis-like"). Suggested GO terms: GO:0007155 (cell adhesion), GO:0016055 (Wnt signaling pathway), GO:0045444 (fat cell differentiation), GO:0006915 (apoptotic process), GO:0007507 (heart development), GO:0086064 (cell communication by electrical coupling).

**Protein dysfunction.** Truncated plakoglobin is expressed but **fails to localize normally at intercalated disks**, secondarily depleting Cx43 and NaV1.5 immunosignal there ([PMID: 15851108](https://pubmed.ncbi.nlm.nih.gov/15851108/), [PMID: 23178689](https://pubmed.ncbi.nlm.nih.gov/23178689/)). This is a **loss-of-function at the junction combined with a gain-of-function (Wnt-suppressing) role in the nucleus**.

> *"Connexin43 expression at intercellular junctions was reduced significantly in both right and left ventricles in all patients with Naxos disease."* — [PMID: 15851108](https://pubmed.ncbi.nlm.nih.gov/15851108/)

> *"Mutant plakoglobin was expressed but failed to localize normally at intercellular junctions."* — [PMID: 15851108](https://pubmed.ncbi.nlm.nih.gov/15851108/)

**Ion-channel / electrophysiologic defect.** Reduced NaV1.5 (SCN5A product) at intercalated disks in ~65% of ACM patients contributes to conduction slowing and arrhythmia vulnerability ([PMID: 23178689](https://pubmed.ncbi.nlm.nih.gov/23178689/)); Cx43 reduced in ~70% and plakoglobin in ~74%.

**Metabolic / immune changes.** Adipogenic reprogramming produces lipid-droplet accumulation in cardiomyocytes (recapitulated in patient iPSC-CMs, [PMID: 22798562](https://pubmed.ncbi.nlm.nih.gov/22798562/)). Immune involvement is **secondary/sterile** — recurrent "myocarditis-like" injury episodes rather than autoimmune or infectious primary pathology ([PMID: 42406223](https://pubmed.ncbi.nlm.nih.gov/42406223/)).

**Tissue-damage mechanism.** Mechanical-stress-induced myocyte death → replacement fibrosis and adipogenesis, concentrated **subepicardially and mediomurally** ([PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/)). "Myocarditis-like episodes" step up disease evolution and mark the transition from concealed to symptomatic phase ([PMID: 34776086](https://pubmed.ncbi.nlm.nih.gov/34776086/)).

> *"'Myocarditis-like episodes' may step up the disease evolution or mark a transition from concealed to symptomatic cardiomyopathy phase."* — [PMID: 34776086](https://pubmed.ncbi.nlm.nih.gov/34776086/)

> *"progressive fibrotic or fibrofatty myocardial remodeling, eventually developing phenotypic features consistent with arrhythmogenic cardiomyopathy"* — [PMID: 42406223](https://pubmed.ncbi.nlm.nih.gov/42406223/)

**Cell types (CL) & subcellular compartments (GO CC).** Cardiomyocytes (CL:0000746), specifically ventricular cardiomyocytes (CL:0002131); keratinocytes (CL:0000312) for the skin phenotype; hair follicle cells. Subcellular: **intercalated disc / cell–cell junction** (GO:0014704, GO:0005911), **desmosome** (GO:0030057), **gap junction** (GO:0005921), **nucleus** (GO:0005634 — for Wnt/Tcf-Lef signaling).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary organ:** Heart — right ventricle preferentially (Naxos); left/biventricular in Carvajal variant. UBERON:0000948 (heart), UBERON:0002080 (right ventricle), UBERON:0002084 (left ventricle).
- **Skin & appendages:** palms and soles (palmoplantar keratoderma), hair/hair follicles (woolly hair). UBERON:0002097 (skin of body), UBERON:0001456 (skin of palm/sole), UBERON:0002073 (hair follicle).
- **Secondary organ involvement:** systemic congestion / hepatomegaly from right heart failure at end stage ([PMID: 38433550](https://pubmed.ncbi.nlm.nih.gov/38433550/)).
- **Body systems:** Cardiovascular (primary), Integumentary (primary), with secondary systemic/circulatory effects.

**Tissue & cell level.** Myocardial (cardiac muscle) tissue — cardiomyocytes at the intercalated disk; epidermis — keratinocytes; hair follicle. Fibrofatty replacement introduces adipocytes (CL:0000136) and fibroblasts (CL:0000057) into myocardium.

**Subcellular level.** Intercalated disc composite junctions (desmosome + adherens junction + gap junction), and the nucleus (Wnt/Tcf-Lef transcriptional node).

**Localization / lateralization.** Cardiac involvement is **bilateral within the heart** but **regionally predominant in the RV free wall, inflow, apex, and outflow (the "triangle of dysplasia")**; cutaneous involvement is **bilateral and symmetric** (palms/soles, scalp hair).

---

## 8. Temporal Development

| Feature | Timing |
|---|---|
| Woolly hair | Congenital (from birth) |
| Palmoplantar keratoderma | First year of life |
| Cardiac (ARVC) onset | Adolescence (concealed earlier; criteria met as young as 13) |
| Onset pattern (cardiac) | Insidious/chronic, punctuated by acute arrhythmic or "hot-phase" episodes |
| Disease course | Progressive |
| Duration | Chronic, lifelong |

**Progression / stages.** A **concealed phase** (structurally subtle, but with early Cx43/NaV1.5 remodeling already present, even in a child dying before overt ARVC — [PMID: 15851108](https://pubmed.ncbi.nlm.nih.gov/15851108/)) transitions to an **overt electrical phase** (arrhythmias, ECG changes), then a **structural progression phase** (RV then ± LV dysfunction), and finally **end-stage heart failure**. In the natural-history cohort, **62% showed structural progression** and **27% developed heart failure** over ~10 years ([PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)). "Myocarditis-like" episodes can abruptly advance the disease ([PMID: 34776086](https://pubmed.ncbi.nlm.nih.gov/34776086/)).

**Patterns.** Course is **progressive with episodic arrhythmic exacerbations**; no spontaneous remission. **Critical windows for intervention:** the concealed/adolescent phase (where exercise restriction and surveillance are most valuable) and the early symptomatic phase (ICD decision-making).

---

## 9. Inheritance and Population

**Epidemiology.** Naxos disease is **rare**. It shows notable clustering on the Greek island of Naxos and the wider Aegean (founder effect), with additional families in Turkey, Israel, Saudi Arabia, India, and Ecuador (the latter two mainly the Carvajal/DSP variant) ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/), [PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/)). Precise prevalence/incidence figures are not established (Orphanet lists it as a rare/ultra-rare disease); reported cohorts are small (dozens of families).

**Inheritance.** **Autosomal recessive** (biallelic JUP truncation) ([PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)).

**Penetrance / expressivity.** Cardiac penetrance is **complete (100%) in adult homozygotes** ([PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)); expressivity is **variable** in extent/timing of LV involvement and heart-failure development. The recessive JUP phenotype is clinically comparable in arrhythmic risk to dominant PKP2 ARVC ([PMID: 16893920](https://pubmed.ncbi.nlm.nih.gov/16893920/)).

**Founder effect / consanguinity.** Strong **founder effect** for the JUP 2157del2 allele on Naxos ([PMID: 10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/)). **Consanguinity** amplifies recessive expression, particularly relevant in Middle Eastern populations — e.g., Saudi/Arab Carvajal-variant families, where the authors emphasize extended genetic workup of relatives because "consanguineous marriage is common" ([PMID: 40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/)).

**Carrier frequency.** Heterozygous carriers are asymptomatic for the full syndrome; carrier frequency is elevated locally in founder populations but not quantified in general databases.

**Population demographics / sex ratio.** No strong sex bias in the recessive cardiocutaneous phenotype is established, though male sex and exercise are adverse modifiers of arrhythmic outcome in ARVC broadly. Age distribution: cutaneous features from infancy; cardiac disease clinically emerges in adolescence/young adulthood.

---

## 10. Diagnostics

**Clinical recognition.** The pathognomonic clue is **woolly hair + palmoplantar keratoderma in a child**, which should prompt cardiac evaluation. *"The association of woolly hair with palmoplantar keratoderma in a child should lead to a cardiac workup in the search for those at increased risk for sudden cardiac death"* ([PMID: 25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/)).

**Electrophysiology (ECG/Holter).** Most sensitive/specific markers: **T-wave inversion in leads V1–V3, RV wall-motion abnormalities, and frequent ventricular extrasystoles** ([PMID: 16893920](https://pubmed.ncbi.nlm.nih.gov/16893920/)). ~92% of homozygotes have ECG abnormalities and ventricular arrhythmias ([PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)). QRS dispersion ≥40 ms predicts syncope.

**Imaging.** Echocardiography and **cardiac MRI** demonstrate RV dilation, wall-motion abnormalities, and fibrofatty replacement; updated CMR thresholds improve specificity ([PMID: 41317940](https://pubmed.ncbi.nlm.nih.gov/41317940/)). **Left-ventricular late gadolinium enhancement (LGE)** is associated with arrhythmic risk though it did not add incremental value over the ARVC risk calculator in one multicenter study ([PMID: 41608798](https://pubmed.ncbi.nlm.nih.gov/41608798/)). RVOT diameter is a useful diagnostic/prognostic parameter ([PMID: 41342822](https://pubmed.ncbi.nlm.nih.gov/41342822/)).

**Biopsy / histopathology.** Myocardial loss with **fibrofatty/fibrous replacement at subepicardial and mediomural layers** ([PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/)). **Immunohistochemistry for plakoglobin** shows reduced junctional signal (reported sensitivity ~85%, specificity ~57% in one series — a useful but not standalone test) ([PMID: 22036107](https://pubmed.ncbi.nlm.nih.gov/22036107/)). Reduced Cx43, NaV1.5, and plakoglobin immunosignal at intercalated disks is seen in the majority of ACM patients ([PMID: 23178689](https://pubmed.ncbi.nlm.nih.gov/23178689/)). A **buccal-mucosa cell assay** offers a minimally invasive readout of abnormal plakoglobin/Cx43 distribution ([PMID: 26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/)).

**Genetic testing.** Definitive diagnosis is by **molecular confirmation of biallelic JUP (or DSP for Carvajal) mutation**. Approaches: targeted single-gene testing for the JUP founder allele in Aegean families; **ARVC/cardiomyopathy gene panels** (JUP, DSP, PKP2, DSG2, DSC2, plus broader cardiomyopathy genes); **whole-exome sequencing** is effective in consanguineous/atypical presentations ([PMID: 25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/), [PMID: 40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/)). Recent guidance favors **broad cardiomyopathy/arrhythmia gene panels** over restricting to validated ARVC genes ([PMID: 42389803](https://pubmed.ncbi.nlm.nih.gov/42389803/)).

**Clinical criteria.** Cardiac diagnosis uses the **2010 modified Task Force Criteria** for ARVC (and Padua criteria for ACM), integrating ECG, arrhythmia, structural, and tissue features.

**Differential diagnosis.** Carvajal syndrome (DSP, LV-dominant, dilated phenotype); dominant non-syndromic ARVC (PKP2/DSG2/DSC2/DSP); **acute myocarditis** (desmosomal cardiomyopathy can masquerade as myocarditis — [PMID: 38652395](https://pubmed.ncbi.nlm.nih.gov/38652395/)); other palmoplantar keratoderma/woolly-hair syndromes without cardiac disease.

**Screening.** **Cascade family screening** (clinical + genetic) of first-degree relatives is standard. Non-invasive family screening can be based largely on T-wave inversion, RV wall-motion abnormalities, and frequent ventricular extrasystoles ([PMID: 16893920](https://pubmed.ncbi.nlm.nih.gov/16893920/)).

---

## 11. Outcome / Prognosis

**Mortality.** In the definitive cohort, **annual disease-related mortality was 3% and annual sudden-death mortality 2.3%** ([PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)).

> *"The annual disease-related and sudden death mortality was 3% and 2.3%, respectively."* — [PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)

**Morbidity / disease course.** Over ~10 years: **46% arrhythmic events, 62% structural progression, 27% heart failure** ([PMID: 11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/)). The Carvajal variant is more heart-failure-prone: in a 10-patient pediatric cohort, all had severely dilated/depressed LV function, **4 underwent heart transplantation and 3 died suddenly while awaiting a donor** ([PMID: 40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/)). In ACM broadly, DSP variants and reduced biventricular EF predict heart-failure hospitalization ([PMID: 42372975](https://pubmed.ncbi.nlm.nih.gov/42372975/)).

**Prognostic factors.** Adverse: younger age at presentation, extensive RV/LV structural disease, prior sustained VA, reduced biventricular EF, high arrhythmic burden, and DSP genotype (for HF risk). ICD implantation substantially alters natural history by preventing sudden death; with appropriate management, **near-normal life expectancy is achievable** ([PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)).

**Recovery potential.** No spontaneous recovery; the disease is progressive. End-stage disease requires transplantation.

---

## 12. Treatment

Management is **ARVC/heart-failure–guideline-based**, as no Naxos-specific curative therapy exists ([PMID: 32966140](https://pubmed.ncbi.nlm.nih.gov/32966140/), [PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)).

| Modality | Role | MAXO term (suggested) |
|---|---|---|
| **Exercise restriction** | Reduce mechanical-stress-driven progression | MAXO (lifestyle/physical-activity intervention) |
| **Antiarrhythmic drugs** (β-blockers, sotalol, amiodarone) | Reduce number/complexity of arrhythmias (do NOT reduce SCD risk) | MAXO:0000058 (pharmacotherapy) |
| **Catheter ablation** | Control recurrent VT (high recurrence) | MAXO (catheter ablation) |
| **ICD implantation** | Prevent sudden cardiac death (mainstay) | MAXO (implantable cardioverter defibrillator) |
| **Heart-failure therapy** (ACEi/ARB, β-blocker, diuretics; SGLT2i emerging) | Manage HF | MAXO:0000058 |
| **Heart transplantation** | End-stage failure | MAXO (organ transplantation) |

> *"Treatment consists of restriction of physical exercise, antiarrhythmic drugs, catheter ablation and ICD implantation."* — [PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)

> *"Antiarrhythmic drugs play an important role in terms of reduction of both the number and the complexity of arrhythmias, but they do not reduce the risk of SD."* — [PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)

For sudden-death prevention, **ICD implantation is indicated** in Naxos disease, and heart transplantation is considered at end stages ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/)). ICD decisions should follow risk stratification (the ARVC risk calculator; ICDs are indicated in only a minority of screened relatives — [PMID: 22505462](https://pubmed.ncbi.nlm.nih.gov/22505462/)).

**Emerging / experimental therapeutics.**
- **GSK3β inhibition (SB216763):** rescues/partly reverses the arrhythmogenic phenotype in Naxos-specific plakoglobin models and normalizes junctional protein distribution in patient cells — the leading mechanism-targeted candidate ([PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/), [PMID: 26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/)).

> *"Abnormal protein distributions were reversed in cultured cells incubated with SB216763, a small molecule that rescues the disease phenotype in cardiac myocytes."* — [PMID: 26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/)

- **SGLT2 inhibitors (dapagliflozin):** in carriers of cardiomyopathy-associated variants (including ACM), SGLT2 inhibition strongly reduced HF hospitalization (HR 0.18 in carriers vs 0.70 in non-carriers), suggesting a role in HF prevention for genotype-positive individuals ([PMID: 42260102](https://pubmed.ncbi.nlm.nih.gov/42260102/)).
- **Stem-cell/iPSC-based translational approaches** are under active investigation ([PMID: 32966140](https://pubmed.ncbi.nlm.nih.gov/32966140/)).

**Pharmacogenomics.** No Naxos-specific pharmacogenomic guidance established.

---

## 13. Prevention

- **Primary prevention:** Not possible for the genetic disease itself; **genetic counseling and reproductive options** (carrier testing, prenatal/preimplantation genetic diagnosis) prevent affected births, especially important in consanguineous founder populations ([PMID: 40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/)).
- **Secondary prevention:** **Early detection via the cutaneous phenotype** — woolly hair + keratoderma in a child mandates cardiac surveillance ([PMID: 25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/)). Cascade clinical + genetic screening of first-degree relatives ([PMID: 16893920](https://pubmed.ncbi.nlm.nih.gov/16893920/), [PMID: 42389803](https://pubmed.ncbi.nlm.nih.gov/42389803/)).
- **Tertiary prevention:** **Exercise restriction** to slow progression; **ICD** to prevent sudden death; HF therapy to prevent decompensation ([PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/), [PMID: 26545710](https://pubmed.ncbi.nlm.nih.gov/26545710/)).
- **Genetic screening:** Carrier screening in founder/consanguineous populations; PGD/prenatal testing available.
- **Counseling:** Genetic counseling for recessive risk (25% recurrence for carrier couples) is essential ([PMID: 38433550](https://pubmed.ncbi.nlm.nih.gov/38433550/)).
- **Immunization / public-health / prophylaxis:** Not applicable (non-infectious Mendelian disorder).

---

## 14. Other Species / Natural Disease

- **Naturally occurring homolog:** A **lethal autosomal recessive cardiocutaneous syndrome of Poll Hereford calves** (*Bos taurus*, NCBI Taxon:9913) has been reported in Australia, sharing features with human Naxos disease ([PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/)).

> *"A lethal autosomal recessive cardiocutaneous syndrome of Poll Hereford calves has been reported in Australia sharing similarities with the human syndrome"* — [PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/)

- **Spontaneous mouse mutant:** A recessive mutation on **mouse chromosome 13 (aht)** produces abnormal hair texture with cardiomyopathy, a naturally arising rodent counterpart ([PMID: 37702215](https://pubmed.ncbi.nlm.nih.gov/37702215/)).
- **Orthologous genes:** *Jup* (mouse, NCBI Gene 16480), *jup* (zebrafish). Desmosomal biology is evolutionarily conserved across vertebrates, underlying the transferability of zebrafish/mouse models.
- **Zoonotic potential:** None (genetic disease).

---

## 15. Model Organisms

| Model | Type | Genetic manipulation | Recapitulation | Reference |
|---|---|---|---|---|
| **JUP-KO iPSC line (JMUi001-A-4)** | Human cellular | CRISPR/Cas9 knockout of JUP | Models cardiac ACM phenotype on CM differentiation; retains pluripotency | [PMID: 37995437](https://pubmed.ncbi.nlm.nih.gov/37995437/) |
| **Patient-specific iPSC-CMs** | Human cellular | Endogenous desmosomal mutation (PKP2) | Reduced desmosomal protein signal; adipogenic/lipid-droplet phenotype | [PMID: 22798562](https://pubmed.ncbi.nlm.nih.gov/22798562/) |
| **Zebrafish (2057del2 plakoglobin)** | Vertebrate in vivo | Overexpression of Naxos mutation | Reproduces arrhythmogenic phenotype; rescued by SB216763 | [PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/) |
| **Neonatal rat cardiomyocytes (2057del2)** | Mammalian cellular | Overexpression of Naxos mutation | Arrhythmogenic phenotype; SB216763-responsive | [PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/) |
| **Heterozygous DP (Dsp)-deficient mouse** | Mammalian in vivo | Cardiac-restricted Dsp deletion (het) | Excess adipocytes/fibrosis, myocyte apoptosis, cardiac dysfunction, VT — recapitulates ARVC | [PMID: 16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/) |
| **Tg-DSP(R2834H) mouse** | Mammalian in vivo | Desmoplakin mutant transgene | Exercise-accelerated RV remodeling; perturbed AKT1/GSK3β | [PMID: 26545710](https://pubmed.ncbi.nlm.nih.gov/26545710/) |
| **Poll Hereford calf** | Natural (bovine) | Spontaneous recessive | Cardiocutaneous syndrome homolog | [PMID: 15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/) |
| **aht mouse (Chr 13)** | Natural (rodent) | Spontaneous recessive | Abnormal hair + cardiomyopathy | [PMID: 37702215](https://pubmed.ncbi.nlm.nih.gov/37702215/) |

> *"we generated a knock-out (KO) of the junctional protein Plakoglobin (JUP-KO; JMUi001-A-4) using the CRISPR/Cas9 system in healthy control induced pluripotent stem cells"* — [PMID: 37995437](https://pubmed.ncbi.nlm.nih.gov/37995437/)

**Model applications & limitations.** These models enable study of junctional protein trafficking, Wnt/GSK3β signaling, adipogenic transdifferentiation, and drug rescue. Complete cardiac Dsp knockout is embryonic-lethal, so heterozygous or conditional strategies are required ([PMID: 16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/)). iPSC-CMs are relatively immature and lack the tissue-level mechanical stress and three-dimensional architecture central to the human phenotype; zebrafish overexpression models do not fully capture the recessive loss-of-function context. The cutaneous phenotype is generally under-modeled relative to the cardiac phenotype.

---

## Mechanistic Model / Interpretation

Naxos disease is best understood as a **desmosomal adhesion failure with dual downstream consequences — electrical and structural — amplified by mechanical load.**

1. **Upstream trigger (genetic):** biallelic JUP truncation removes functional plakoglobin from the cardiomyocyte intercalated disk.
2. **Early electrical remodeling (upstream of structural disease):** loss of junctional plakoglobin destabilizes Cx43 gap junctions and NaV1.5 channels, producing conduction slowing and an arrhythmic substrate **before** overt structural changes — this explains sudden death in young, minimally remodeled hearts and the finding of remodeling in a child who died pre-ARVC ([PMID: 15851108](https://pubmed.ncbi.nlm.nih.gov/15851108/), [PMID: 23178689](https://pubmed.ncbi.nlm.nih.gov/23178689/)).
3. **Structural remodeling (downstream):** nuclear plakoglobin suppresses Wnt/β-catenin/Tcf-Lef signaling, activating adipogenic and fibrogenic transcription and yielding fibrofatty replacement ([PMID: 16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/)).
4. **Amplifier (environmental):** mechanical/exercise stress and episodic "myocarditis-like" injury accelerate myocyte death and the concealed→symptomatic transition ([PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/), [PMID: 34776086](https://pubmed.ncbi.nlm.nih.gov/34776086/)).
5. **Convergent therapeutic node:** GSK3β sits at the intersection of these pathways; its inhibition restores junctional protein localization and rescues the phenotype in multiple models — the most compelling disease-modifying lead ([PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/), [PMID: 26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/)).

---

## Evidence Base

| PMID | Contribution | Support/Challenge |
|---|---|---|
| [10902626](https://pubmed.ncbi.nlm.nih.gov/10902626/) | Identifies causal homozygous JUP 2-bp deletion; founder effect | Foundational — establishes gene & recessive inheritance |
| [11691526](https://pubmed.ncbi.nlm.nih.gov/11691526/) | Natural history; 100% penetrance; mortality 3%/2.3% | Defines cardiac penetrance, progression, mortality |
| [15851108](https://pubmed.ncbi.nlm.nih.gov/15851108/) | Cx43 remodeling; mutant plakoglobin mislocalizes | Core electrical mechanism |
| [23178689](https://pubmed.ncbi.nlm.nih.gov/23178689/) | Reduced PKG/Cx43/NaV1.5 in ~65–74% of ACM | Extends channel-remodeling mechanism |
| [16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/) | Nuclear plakoglobin suppresses Wnt; DP-KO mouse | Structural/adipogenic mechanism + in vivo model |
| [16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/) | Clinical overview; mechanical-stress mechanism; ICD | Clinical synthesis |
| [15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/) | Cardiocutaneous spectrum; Poll Hereford homolog | Temporal sequence + comparative biology |
| [26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/) | SB216763 rescues Naxos plakoglobin models | Therapeutic mechanism |
| [26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/) | SB216763 normalizes patient buccal cells | Translational drug evidence |
| [25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/) | ARVC treatment modalities and their limits | Treatment framework |
| [16893920](https://pubmed.ncbi.nlm.nih.gov/16893920/) | JUP vs PKP2 phenotype/screening markers | Diagnosis/prognosis |
| [37995437](https://pubmed.ncbi.nlm.nih.gov/37995437/) | JUP-KO iPSC line | Model resource |
| [34776086](https://pubmed.ncbi.nlm.nih.gov/34776086/) | Myocarditis-like hot-phase episodes | Progression mechanism |
| [40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/) | Carvajal (DSP) pediatric cohort; transplant/SCD outcomes | Genotype-outcome, consanguinity |

---

## Limitations and Knowledge Gaps

1. **Epidemiology is imprecise:** true prevalence/incidence and carrier frequencies are not well quantified beyond founder-population clustering; larger registries are needed ([PMID: 32966140](https://pubmed.ncbi.nlm.nih.gov/32966140/)).
2. **Small cohorts:** natural-history and outcome data derive from limited family cohorts; risk-stratification tools (ARVC risk calculator, LGE) are validated largely in broader ARVC populations, not Naxos-specific samples.
3. **No approved disease-modifying therapy:** GSK3β inhibition and SGLT2 inhibition are promising but unproven in Naxos-specific human trials.
4. **Mechanistic gaps:** the precise trafficking route of mutant plakoglobin to the nucleus, the relative timing of electrical vs structural mechanisms in individual patients, and modifiers of variable expressivity remain incompletely defined.
5. **Cutaneous phenotype under-modeled:** most models focus on the heart; the keratoderma/woolly-hair biology is comparatively unstudied.
6. **Nomenclature variance:** the causal allele appears as both "2157del2" and "2057del2" across sources — a numbering discrepancy to reconcile against reference transcripts.
7. **No primary datasets analyzed:** this report is a literature synthesis; all claims are literature-derived and PMID-cited, not derived from a provided experimental dataset.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a Naxos disease registry** to obtain robust prevalence, penetrance-by-age, and outcome data, and to validate the ARVC risk calculator in this genotype ([PMID: 32966140](https://pubmed.ncbi.nlm.nih.gov/32966140/)).
2. **Advance GSK3β-inhibitor translation:** dose-ranging and safety studies of SB216763 analogs in iPSC-CM and mouse Naxos models, then early-phase human evaluation ([PMID: 26015932](https://pubmed.ncbi.nlm.nih.gov/26015932/)).
3. **Test SGLT2 inhibitors prospectively** in genotype-positive cardiomyopathy carriers for HF prevention, extending the DECLARE-TIMI 58 signal ([PMID: 42260102](https://pubmed.ncbi.nlm.nih.gov/42260102/)).
4. **Generate a homozygous/recessive JUP disease model** (patient iPSC-CMs with the native 2157del2 allele in engineered heart tissue under mechanical load) to capture the exercise/GxE axis.
5. **Longitudinal biomarker study** using the buccal-mucosa plakoglobin/Cx43 assay to track concealed-phase disease and treatment response ([PMID: 26850880](https://pubmed.ncbi.nlm.nih.gov/26850880/)).
6. **Standardize variant nomenclature** (c.2157del2 vs 2057del2) against the current reference JUP transcript and deposit in ClinVar with full ACMG classification.
7. **Cutaneous-phenotype mechanistic studies** (keratinocyte/hair-follicle models) to understand plakoglobin's tissue-specific roles.

---

*Report compiled from 5 iterations, 9 confirmed findings, and 39 reviewed papers. Evidence sources span human clinical cohorts, model organisms (mouse, zebrafish, rat, bovine), and in vitro/iPSC systems, as annotated per citation. Category: Mendelian (autosomal recessive).*


## Artifacts

- [OpenScientist final report](Naxos_disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Naxos_disease-deep-research-openscientist_artifacts/final_report.pdf)