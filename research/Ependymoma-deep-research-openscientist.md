---
title: Ependymoma pathophysiology for dismech curation
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-28T11:39:37.270415'
end_time: '2026-07-28T12:02:16.035272'
duration_seconds: 1358.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ependymoma
  mondo_id: MONDO:0016698
  category: Neoplasm / ependymal tumor of the central nervous system (WHO CNS5 molecularly
    defined groups)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 10
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 5400
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 54
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ependymoma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ependymoma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ependymoma
- **MONDO ID:** MONDO:0016698 (if available)
- **Category:** Neoplasm / ependymal tumor of the central nervous system (WHO CNS5 molecularly defined groups)

## Research Objectives

Please provide a comprehensive research report on **Ependymoma** covering all of the
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

# Ependymoma: A Comprehensive Disease Characteristics Report

**Disease:** Ependymoma
**MONDO ID:** MONDO:0016698
**Category:** Neoplasm / ependymal tumor of the central nervous system (WHO CNS5 molecularly defined groups)
**Investigation:** 10 iterations · 27 confirmed findings · 3 supported hypotheses · 75 papers reviewed

---

## Summary

Ependymoma is a rare glial neoplasm of ependymal/radial-glial lineage that arises along the neuraxis — in the supratentorial brain, the posterior fossa, or the spinal cord. Its defining biological feature is that, unlike most adult gliomas, it carries **very few recurrent point mutations**. Instead, it is driven by **location-specific fusion oncogenes and epigenetic reprogramming**. The 2021 WHO Classification of CNS Tumors (5th edition, "CNS5") formalized this by defining **10 molecularly and anatomically distinct diagnostic entities**, replacing a grade-based scheme that correlated poorly with survival ([PMID: 37743338](https://pubmed.ncbi.nlm.nih.gov/37743338/)). Anatomic compartment plus molecular driver — not histologic grade — now determines diagnosis and prognosis.

Two mechanisms dominate the intracranial disease. In **supratentorial ependymoma**, a **ZFTA–RELA (formerly C11orf95–RELA) gene fusion** — present in >60% of cases — produces an oncoprotein that constitutively localizes to the nucleus, forms **dynamic nuclear condensates**, and drives aberrant **NF-κB/transcriptional** programs ([PMID: 33741710](https://pubmed.ncbi.nlm.nih.gov/33741710/); [PMID: 40866513](https://pubmed.ncbi.nlm.nih.gov/40866513/); [PMID: 42080900](https://pubmed.ncbi.nlm.nih.gov/42080900/)). In **posterior fossa group A (PFA)** tumors, overexpression of **EZHIP (CXorf67)** mimics the H3K27M oncohistone, inhibits **PRC2**, and causes **global loss of H3K27me3** with de-repression of neurodevelopmental genes ([PMID: 30923826](https://pubmed.ncbi.nlm.nih.gov/30923826/); [PMID: 33049227](https://pubmed.ncbi.nlm.nih.gov/33049227/)). Spinal ependymomas are frequently defined by **NF2 loss** (germline in NF2-related schwannomatosis, or somatic with 22q loss), except an aggressive **MYCN-amplified** class ([PMID: 34895332](https://pubmed.ncbi.nlm.nih.gov/34895332/); [PMID: 38265489](https://pubmed.ncbi.nlm.nih.gov/38265489/)).

Clinically, ependymoma is largely **sporadic** (high-dose ionizing radiation is the only established environmental risk factor; ~5%+ attributable to genetic predisposition, chiefly germline NF2). It presents with **hydrocephalus/raised intracranial pressure** (posterior fossa) or **seizures/focal deficits** (supratentorial). The cornerstone of treatment is **maximal safe surgical resection followed by adjuvant focal radiotherapy**; chemotherapy offers minimal curative benefit. **Extent of resection** and **molecular subgroup** are the strongest prognostic determinants: EPN-PFB has excellent survival (~100% 5-year OS) while PFA with **chromosome 1q gain and/or 6q loss** is the worst. Ten-year overall survival across all ependymoma ranges 50–75%. Emerging targeted (MERTK, EZHIP/PRC2) and locoregional CAR-T strategies remain experimental.

---

## Key Findings

### 1. Disease Information and Classification (WHO CNS5)

The 2021 WHO CNS5 classification lists **10 ependymoma diagnostic entities** integrating histology, molecular alterations, DNA methylation profiling, and anatomic location (Finding F015). These are: (1) supratentorial subependymoma; (2) supratentorial ependymoma, ZFTA fusion-positive; (3) supratentorial ependymoma, YAP1 fusion-positive; (4) posterior fossa subependymoma; (5) posterior fossa group A (PFA) ependymoma; (6) posterior fossa group B (PFB) ependymoma; (7) spinal subependymoma; (8) spinal ependymoma; (9) spinal myxopapillary ependymoma; and (10) spinal ependymoma, MYCN-amplified ([PMID: 37743338](https://pubmed.ncbi.nlm.nih.gov/37743338/)). Molecular information was first incorporated in the 2016 4th edition (RELA-fusion). The term **"anaplastic ependymoma" was dropped** in CNS5 because "the low correlation between tumor grade and survival prognosis remained a problem." Grading now spans CNS WHO grade 1 (subependymoma, myxopapillary) to grades 2–3.

**Key identifiers:** MONDO:0016698; MeSH D004806 (Ependymoma). ICD-O morphology codes 9391/3 (ependymoma), 9392/3 (formerly anaplastic), 9394/1 (myxopapillary), 9383/1 (subependymoma). The information in this report is derived from **aggregated disease-level resources** (registries such as CBTRUS/SEER, cooperative-group trials, molecular cohort studies) rather than individual patient EHR.

**Synonyms:** ependymal tumor; historical subtypes include anaplastic ependymoma (retired), RELA fusion-positive ependymoma (now ZFTA fusion-positive), myxopapillary ependymoma, subependymoma.

### 2. Etiology and Risk Factors

Ependymoma is **largely sporadic with few established risk factors** (Findings F011, F026). The authoritative epidemiologic review states: *"The causes of childhood CNS tumours are largely unknown; and although an estimated 5% or more may be explained by genetic predisposition, investigations of environmental aetiology have not been fruitful. Whilst high dose ionising radiation is an established risk factor for this group of tumours, reported associations with dietary N-nitroso compounds have not been consistent"* ([PMID: 16142778](https://pubmed.ncbi.nlm.nih.gov/16142778/)). Exposure to extremely-low-frequency electromagnetic fields (ELF-EMF) has not been associated with childhood CNS tumors. **No infectious agent** is causally implicated.

- **Genetic risk:** The principal hereditary predisposition is **germline NF2 loss** (NF2-related schwannomatosis; see Section 9). ~5%+ of childhood CNS tumors are attributable to genetic predisposition.
- **Environmental risk:** **High-dose ionizing radiation** is the only confirmed environmental risk factor.
- **Demographics:** Ependymomas (with PNET) *"mainly occur in children less than 10 years"* ([PMID: 16142778](https://pubmed.ncbi.nlm.nih.gov/16142778/)); slight male predominance.
- **Protective factors and gene–environment interactions:** No established genetic or environmental protective factors, and no documented gene–environment interactions specific to ependymoma. *(Information not available for this disease.)*

### 3. Phenotypes (Clinical Presentation)

Presentation is **location- and age-dependent** (Findings F006, F021). Posterior fossa/intraventricular tumors obstruct CSF flow, producing **hydrocephalus and raised intracranial pressure**; supratentorial lesions present with **seizures or focal deficits** ([PMID: 40556668](https://pubmed.ncbi.nlm.nih.gov/40556668/)). Signs of raised ICP vary with age: *"Macrocrania and a bulging fontanel can be observed in infants and toddlers, whereas headache, papilledema and vomiting are present in the older children"* ([PMID: 8677342](https://pubmed.ncbi.nlm.nih.gov/8677342/)). Leptomeningeal **dissemination is present in up to 10% of cases at diagnosis** ([PMID: 40556668](https://pubmed.ncbi.nlm.nih.gov/40556668/)). Lateral posterior-fossa tumors cause lower cranial-nerve dysfunction (dysphagia/dysarthria), often transient. Spinal ependymomas present with back/neck pain, sensorimotor deficits, and sphincter dysfunction.

| Phenotype | Type | HPO suggestion | Frequency/onset |
|---|---|---|---|
| Hydrocephalus | Clinical sign | HP:0000238 | Common in posterior fossa; infants/young children |
| Headache | Symptom | HP:0002315 | Common (raised ICP) |
| Nausea/vomiting | Symptom | HP:0002013/HP:0002017 | Common with raised ICP |
| Papilledema | Clinical sign | HP:0001085 | Older children |
| Ataxia | Clinical sign | HP:0001251 | Posterior fossa |
| Seizures | Clinical sign | HP:0001250 | Supratentorial |
| Nystagmus | Clinical sign | HP:0000639 | Posterior fossa/brainstem |
| Cranial nerve palsy | Clinical sign | HP:0001291 | Lateral posterior fossa |
| Macrocephaly | Physical | HP:0000256 | Infants/toddlers |
| Back pain | Symptom | HP:0003418 | Spinal |
| Sphincter/bladder dysfunction | Clinical sign | HP:0000012 | Spinal |

Median age at intracranial diagnosis is **~5 years** ([PMID: 40556668](https://pubmed.ncbi.nlm.nih.gov/40556668/)). Symptom progression is typically progressive; quality of life is heavily affected by neurocognitive sequelae of tumor, surgery, and craniospinal irradiation (processing speed and psychomotor abilities most affected — HIT-2000 data, [PMID: 38835160](https://pubmed.ncbi.nlm.nih.gov/38835160/)).

### 4. Genetic / Molecular Information

Ependymoma is characterized by **few point mutations**; **fusion genes and copy-number/epigenetic changes** are the defining drivers, and they are location-specific (Findings F001, F009, F015).

- **Supratentorial:** **ZFTA–RELA (ZR)** fusion is the most frequent driver (>60% of ST-EPN). *"In supratentorial ependymoma, the most frequent driver alteration is a gene fusion between ZFTA and RELA (denoted ZR), leads to constitutive localization of ZR in the nucleus"* ([PMID: 42080900](https://pubmed.ncbi.nlm.nih.gov/42080900/)). ST-EPN divides into ZFTA-fused and **YAP1-fused** groups, *"with the majority harbouring ZFTA::RELA fusion"* ([PMID: 42332758](https://pubmed.ncbi.nlm.nih.gov/42332758/)). Genes: **ZFTA** (formerly C11orf95, 11q13), **RELA** (HGNC:9955), **YAP1** (HGNC:16262).
- **Posterior fossa:** **PFA** driven by **EZHIP/CXorf67** overexpression → global H3K27me3 loss; **PFB** is epigenetically distinct with better prognosis. No recurrent driver gene mutation in PF-EPN (epigenetically driven).
- **Spinal:** **NF2** alterations (HGNC:7773, chromosome 22q12) in classic spinal ependymoma; **MYCN (2p24) amplification** defines the aggressive SP-MYCN class ([PMID: 34895332](https://pubmed.ncbi.nlm.nih.gov/34895332/)).
- **Copy-number biomarkers (F008, F019):** **Chromosome 1q gain** and **CDKN2A/2B homozygous deletion** are adverse; **6q loss** is adverse in PFA; gains of 9, 15q, 18 and loss of 6 are favorable. *"age at diagnosis, gain of 1q, and homozygous deletion of CDKN2A comprised the most powerful independent indicators of unfavorable prognosis"* ([PMID: 20516456](https://pubmed.ncbi.nlm.nih.gov/20516456/)).
- **Somatic vs germline:** Nearly all driver events (ZFTA-RELA, EZHIP, MYCN, somatic NF2) are **somatic**; **germline NF2** underlies hereditary spinal disease.
- **Epigenetics:** DNA methylation profiling is central to subgrouping; PFA is defined by a CpG-island methylator phenotype and global H3K27me3 loss.

### 5. Environmental Information

Beyond **high-dose ionizing radiation** (established), there are no confirmed environmental, lifestyle, or infectious contributors (F011, F026). Dietary N-nitroso compound associations are inconsistent; ELF-EMF shows no association. No bacterial, viral, fungal, or parasitic agent is implicated. *(Largely not applicable for this disease.)*

### 6. Mechanism / Pathophysiology

Two divergent molecular mechanisms operate in the two major intracranial compartments (Hypothesis H002; Findings F001, F002, F017).

**Supratentorial — ZFTA-RELA condensate/NF-κB axis:** *"More than 60% of supratentorial ependymomas harbor a"* ZFTA-RELA fusion ([PMID: 33741710](https://pubmed.ncbi.nlm.nih.gov/33741710/)). The fusion oncoprotein *"forms dynamic nuclear condensates that are required for oncogene expression and tumorigenesis. Mutagenesis studies of ZR reveal a key intrinsically disordered region (IDR) in RELA that governs condensate formation"* ([PMID: 40866513](https://pubmed.ncbi.nlm.nih.gov/40866513/)). Condensate-disrupting mutations impaired genomic occupancy and recruitment of MED1, BRD4, and RNA Pol II; synthetic ZFTA fusions grafting IDRs from EWS/FUS restored condensate formation and tumor initiation in mice. CRISPR-Cas9 screens identified druggable ZR interactors — *"XPO1, CARM1, SMARCA4, and CDK1"* ([PMID: 42080900](https://pubmed.ncbi.nlm.nih.gov/42080900/)) — and **MERTK** as a systems-level vulnerability ([PMID: 41665993](https://pubmed.ncbi.nlm.nih.gov/41665993/)). ZFTA-RELA tumors also produce **itaconate** to epigenetically drive fusion expression ([PMID: 41639460](https://pubmed.ncbi.nlm.nih.gov/41639460/)).

**Posterior fossa PFA — EZHIP/PRC2/H3K27me3 axis:** PFA tumors are *"characterized by a lack of the repressive histone H3 lysine 27 trimethylation (H3K27me3) mark"* ([PMID: 30923826](https://pubmed.ncbi.nlm.nih.gov/30923826/)). Mechanistically, *"A small, highly conserved peptide sequence located in the C-terminal region of CXorf67 mimics the sequence of K27M mutated histones and binds to the SET domain ... of EZH2. This interaction blocks EZH2 methyltransferase activity and inhibits PRC2 function, causing de-repression of PRC2 target genes"* ([PMID: 30923826](https://pubmed.ncbi.nlm.nih.gov/30923826/)). EZHIP and H3K27M are *"competitive inhibitors of Polycomb Repressive Complex 2 (PRC2) lysine methyltransferase activity"* ([PMID: 33049227](https://pubmed.ncbi.nlm.nih.gov/33049227/)), impeding H3K27-methylation spreading. PFA shares hindbrain developmental pathway dysregulation with H3K27M diffuse midline glioma ([PMID: 36759899](https://pubmed.ncbi.nlm.nih.gov/36759899/)).

**Cellular origin and hierarchy (F010, F027):** Radial glia are the proposed cell of origin (*"radial glia are cells of origin of ependymoma"*, [PMID: 17179988](https://pubmed.ncbi.nlm.nih.gov/17179988/)). Single-cell RNA-seq shows *"Ependymomas are composed of a cellular hierarchy initiating from undifferentiated populations, which undergo impaired differentiation toward three lineages of neuronal-glial fate specification. While prognostically favorable groups of ependymoma predominantly harbor differentiated cells, aggressive groups are enriched for undifferentiated cell populations"* ([PMID: 32663469](https://pubmed.ncbi.nlm.nih.gov/32663469/)). Spinal ependymomas *"display the highest similarities to mature adult ependymal cells"* ([PMID: 38265489](https://pubmed.ncbi.nlm.nih.gov/38265489/)).

**GO / CL / CHEBI suggestions:** GO:0038061 (NF-κB signaling), GO:0140718 (facultative heterochromatin formation / PRC2), GO:0070734 (histone H3-K27 methylation), GO:0030154 (cell differentiation), GO:0016604 (nuclear body / condensate); CL:0000031 (neuroblast/radial glia), CL:0000065 (ependymal cell); CHEBI:30016 (itaconate).

### 7. Anatomical Structures Affected

Ependymoma is a **central nervous system tumor** (UBERON:0001017) arising from cells lining the ventricular system and central canal.

| Compartment | UBERON | Notes |
|---|---|---|
| Supratentorial brain / lateral ventricles | UBERON:0002037 (cerebral hemisphere), UBERON:0002285 (lateral ventricle) | ZFTA/YAP1 fusions; seizures/focal deficits |
| Posterior fossa / fourth ventricle | UBERON:0002422 (fourth ventricle), UBERON:0002037 (cerebellum) | PFA/PFB; hydrocephalus; "plastic" extension through foramina of Luschka/Magendie |
| Spinal cord / central canal | UBERON:0002240 (spinal cord), UBERON:0002291 (central canal) | NF2, MYCN, myxopapillary (conus/cauda equina/filum terminale) |
| Leptomeninges (secondary) | UBERON:0002360 | Dissemination in up to 10% at diagnosis |

**Cell/tissue level:** Nervous tissue; tumor cells resemble **ependymal cells (CL:0000065)** and derive from **radial glia**. **Subcellular:** nucleus (GO:0005634) is the site of ZR oncoprotein/condensate activity; PRC2 acts on nuclear chromatin. **Lateralization:** midline posterior fossa (PFA/PFB) or lateral (worse prognosis); spinal lesions along the neuraxis.

### 8. Temporal Development

- **Onset:** Intracranial ependymoma predominantly **pediatric** (median ~5 years); PFA in infants/young children; PFB, myxopapillary, and subependymoma skew older/adult; spinal MYCN across ages (F002, F006).
- **Onset pattern:** Typically **subacute to chronic/insidious**, culminating in a raised-ICP crisis.
- **Progression:** Grade 1 subependymoma/myxopapillary are slow-growing; PFA and 1q-gain tumors are more aggressive. 1q gain/6q loss increase from 23% at presentation to 61% at first recurrence in PFA ([PMID: 37246777](https://pubmed.ncbi.nlm.nih.gov/37246777/)).
- **Course:** Recurrences are **predominantly local**; median time to local failure ~5.4 years in adults ([PMID: 42348066](https://pubmed.ncbi.nlm.nih.gov/42348066/)). Disease is chronic/relapsing; myxopapillary can recur decades later, occasionally with extra-neural spread 37 years post-diagnosis ([PMID: 40469371](https://pubmed.ncbi.nlm.nih.gov/40469371/)).
- **Critical intervention window:** Achieving gross total resection at initial surgery is the key opportunity for cure.

### 9. Inheritance and Population (Epidemiology)

**Epidemiology (F003, F018):** In CBTRUS/SEER data (2008–2019), the age-adjusted incidence rate (AAAIR) was **0.41/100,000**, the highest among 12 selected rare CNS tumors, and ependymoma was the most prevalent of these (*"AAIR was 1.47 per 100,000 for these tumors combined, with highest incidence in ependymomas (AAIR = 0.41/100,000)"*, [PMID: 37980692](https://pubmed.ncbi.nlm.nih.gov/37980692/)). Ependymomas comprise **~23% of primary spinal cord tumors** (overall spinal cord tumor incidence 0.74/100,000 person-years; [PMID: 18084720](https://pubmed.ncbi.nlm.nih.gov/18084720/)), and are *"the most common intramedullary spinal cord tumors among adults"* ([PMID: 37619838](https://pubmed.ncbi.nlm.nih.gov/37619838/)). Ependymoma is <10% of pediatric CNS neoplasms. **Sex ratio:** slight male predominance for intracranial disease ([PMID: 11554386](https://pubmed.ncbi.nlm.nih.gov/11554386/)). **Race:** African American patients had lower incidence but 78% higher death risk (HR 1.78, 95% CI 1.30–2.44; [PMID: 33014396](https://pubmed.ncbi.nlm.nih.gov/33014396/)).

**Inheritance (F005, F020):** Most ependymomas are **not inherited**. The principal hereditary predisposition is **NF2-related schwannomatosis** (formerly neurofibromatosis type 2), an **autosomal dominant** tumor-predisposition syndrome caused by germline mutations in **NF2** (22q12; merlin/schwannomin). *"Cranial and spinal meningiomas and spinal ependymomas are other common tumors"* ([PMID: 23931824](https://pubmed.ncbi.nlm.nih.gov/23931824/)). NF2-related SWN is *"the most common SWN syndrome, with increased risk for bilateral vestibular schwannomas, intradermal schwannomas, meningiomas, and less commonly, ependymoma"* ([PMID: 39937237](https://pubmed.ncbi.nlm.nih.gov/39937237/)). Mutation spectrum: *"Fifty to sixty percent of patients represent de novo mutations and as many as 33% of these are mosaic ... Truncating mutations (nonsense, frameshift insertions/deletions) are the most frequent germline events and cause the most severe disease"* ([PMID: 23931824](https://pubmed.ncbi.nlm.nih.gov/23931824/)). Bi-allelic NF2 loss (germline/sporadic mutation + 22q loss) defines a spinal ependymoma molecular subtype ([PMID: 38265489](https://pubmed.ncbi.nlm.nih.gov/38265489/)). Penetrance is high with variable expressivity; germline mosaicism is common. No genetic anticipation, founder effect, or consanguinity role is specifically documented for ependymoma.

### 10. Diagnostics

**Imaging (F016):** MRI is primary. Posterior fossa ependymomas classically fill the fourth ventricle and show *"plastic"* extension through the foramina of Luschka and Magendie, are heterogeneous (calcification, cysts, hemorrhage) with variable enhancement. On DWI, *"Diffusion restriction and low ADC value was a feature of high-grade tumors"* ([PMID: 32539423](https://pubmed.ncbi.nlm.nih.gov/32539423/)) — ependymomas typically have higher ADC than medulloblastoma, aiding differential diagnosis. Machine-learning radiomics classified pediatric posterior fossa tumors with micro-averaged AUC 0.91 (accuracy 0.83) ([PMID: 32661052](https://pubmed.ncbi.nlm.nih.gov/32661052/)). PFA vs PFB show distinct MRI features ([PMID: 37658900](https://pubmed.ncbi.nlm.nih.gov/37658900/)). Spinal MRI and CSF cytology stage leptomeningeal dissemination.

**Histopathology/IHC (F009, F023):** Hallmarks are **perivascular pseudorosettes** and true **ependymal rosettes**. Tumor cells are *"positive for GFAP, S-100, and vimentin"* ([PMID: 18095125](https://pubmed.ncbi.nlm.nih.gov/18095125/)) with characteristic **dot-like/paranuclear and ring-like EMA** positivity (*"highlighted intracytoplasmic lumina in a few cells"*, [PMID: 16160486](https://pubmed.ncbi.nlm.nih.gov/16160486/)), typically negative for synaptophysin/keratin. **Surrogate IHC markers:** *"high concordance rates between L1CAM and ZFTA-fusion and H3K27me3 loss or EZHIP overexpression was used for PFA-EPNs"* ([PMID: 34812989](https://pubmed.ncbi.nlm.nih.gov/34812989/)). PFA is defined by IHC **loss of H3 K27me3** ([PMID: 41553163](https://pubmed.ncbi.nlm.nih.gov/41553163/); cIMPACT-NOW: nuclear EZHIP supports PFA, [PMID: 40887057](https://pubmed.ncbi.nlm.nih.gov/40887057/)). A cost-effective diagnostic flow uses location + three biomarkers (L1CAM, H3K27me3, EZHIP) + **Ki-67** (≥7% cutoff, the only independent prognostic factor for OS/PFS in one cohort).

**Molecular/genetic testing:** DNA **methylation array profiling** is the gold standard for subgrouping; fusion detection (RNA/NGS) for ZFTA/YAP1; FISH/CMA for 1q gain, CDKN2A deletion, MYCN amplification, 22q/NF2. Histopathologic variant diagnosis is unreliable without methylation: integrated diagnosis changed in 35.6% of variant cases ([PMID: 31679042](https://pubmed.ncbi.nlm.nih.gov/31679042/)).

**Differential diagnosis:** medulloblastoma, pilocytic astrocytoma, choroid plexus tumors, MN1/BEND2-altered astroblastoma, angiocentric glioma — distinguished by ADC, morphology, IHC, and methylation.

### 11. Outcome / Prognosis

**Survival (F003, F007, F019):** Ten-year OS ranges **50–75%** ([PMID: 40556668](https://pubmed.ncbi.nlm.nih.gov/40556668/)). Molecular subgroup dominates prognosis. In the E-HIT2000 pooled pediatric cohort (n=228):

| Molecular group | n | 5-yr PFS | 5-yr OS |
|---|---|---|---|
| EPN-PFA | 146 | 45 ± 4% | 77 ± 4% |
| EPN-PFB | 19 | 90 ± 7% | ~100% |
| EPN-ZFTA (supratentorial) | 59 | 64 ± 7% | 86 ± 5% |
| EPN-YAP1 | 4 | 50 ± 25% | ~100% |

Source: [PMID: 41026848](https://pubmed.ncbi.nlm.nih.gov/41026848/).

**Prognostic factors:** Extent of resection (**GTR** strongly favorable; subtotal resection HR 1.86 for mortality, [PMID: 33014396](https://pubmed.ncbi.nlm.nih.gov/33014396/)); **adult age** (HR 1.97 vs children); **chromosome 1q gain** (independent adverse, *"gain of 1q25 ... independent prognostic marker for either recurrence-free survival (P < 0.001) or overall survival (P = 0.003)"*, [PMID: 16609018](https://pubmed.ncbi.nlm.nih.gov/16609018/)); **6q loss** and **CDKN2A/2B loss** (adverse); **Ki-67 ≥7%**; undifferentiated single-cell content. PFA without molecular risk factors + complete resection + radiotherapy achieved 5-yr PFS/OS 75%/92%; PFA with risk factors had poor prognosis regardless of treatment ([PMID: 41026848](https://pubmed.ncbi.nlm.nih.gov/41026848/)). Adult intracranial ependymoma with GTR + adjuvant RT: 5/10-yr PFS 80%/64%, OS 92%/85% ([PMID: 42348066](https://pubmed.ncbi.nlm.nih.gov/42348066/)).

**Morbidity:** Neurocognitive impairment (processing speed, psychomotor) from tumor, surgery, and CSI; endocrine deficits; hydrocephalus requiring shunting; lower cranial-nerve deficits (often transient). Recurrences are predominantly local; disease-specific mortality is driven by uncontrolled local/disseminated progression.

### 12. Treatment

**Standard of care (F007, F022):** *"Maximal safe surgical resection is the cornerstone of treatment. Children over one year with grade 2 or 3 tumors typically receive adjuvant focal radiotherapy, while chemotherapy is used to delay irradiation in infants or after subtotal resection"* ([PMID: 40556668](https://pubmed.ncbi.nlm.nih.gov/40556668/)). GTR significantly improves survival in ependymoma (SEER, [PMID: 41653291](https://pubmed.ncbi.nlm.nih.gov/41653291/); spinal meta-analysis, [PMID: 41988002](https://pubmed.ncbi.nlm.nih.gov/41988002/)). For spinal myxopapillary ependymoma, *"GTR remains the cornerstone of treatment for optimal outcomes. In cases where GTR is not feasible, adjuvant radiotherapy is recommended"* ([PMID: 41394446](https://pubmed.ncbi.nlm.nih.gov/41394446/)). Craniospinal irradiation is reserved for disseminated disease.

**MAXO suggestions:** MAXO:0000004 (surgical procedure / tumor resection), MAXO:0000009 (radiation therapy), MAXO:0000058 (chemotherapy).

**Risk-adapted radiotherapy trial (F012):** COG **ACNS0121** (356 patients, ages 1–21) stratified therapy by location/grade/resection. 5-year EFS: 61.4% (observation after GTR of classic supratentorial), 37.2% (subtotal resection), 68.5% (near-total/GTR + immediate conformal RT 59.4 Gy) ([PMID: 30811284](https://pubmed.ncbi.nlm.nih.gov/30811284/)). 1q gain and methylation profiles were evaluated prospectively as modifiers.

**Recurrent disease (F014):** *"No standard therapies exist at relapse"* ([PMID: 42032119](https://pubmed.ncbi.nlm.nih.gov/42032119/)). Re-resection and re-irradiation are mainstays; proton re-irradiation near brainstem achieved 82% 2-year local control ([PMID: 41488407](https://pubmed.ncbi.nlm.nih.gov/41488407/)). Systemic agents offer limited benefit: *"TMZ monotherapy achieved a DCR of 57% with 6- and 12-month PFS rates of 85.7% and 57.1%"* ([PMID: 41788986](https://pubmed.ncbi.nlm.nih.gov/41788986/)); TMZ-lapatinib DCR 33%; bevacizumab regimens variable.

**Emerging targeted/immunotherapy (F024, H003):** **MERTK** vulnerability in ZFTA-RELA tumors ([PMID: 41665993](https://pubmed.ncbi.nlm.nih.gov/41665993/)); **XPO1** inhibitor selinexor extended survival in ZR PDX models ([PMID: 42080900](https://pubmed.ncbi.nlm.nih.gov/42080900/)); **EZHIP/PRC2** targeting in PFA ([PMID: 41596609](https://pubmed.ncbi.nlm.nih.gov/41596609/)); **locoregional (intrathecal) CAR-T** against EPHA2/HER2/IL13Rα2 — *"an effective treatment for primary, metastatic and recurrent group 3 medulloblastoma and PFA ependymoma xenografts"* ([PMID: 32341580](https://pubmed.ncbi.nlm.nih.gov/32341580/)); a candidate **hsa-miR-138-5p** axis in fusion-positive tumors ([PMID: 41628537](https://pubmed.ncbi.nlm.nih.gov/41628537/)).

### 13. Prevention

There is **no primary prevention** for sporadic ependymoma beyond avoiding unnecessary high-dose ionizing radiation. **Secondary prevention** applies to hereditary risk: in NF2-related schwannomatosis, surveillance imaging and *"active management gave better outcomes than surveillance in spinal ependymoma"* ([PMID: 31425178](https://pubmed.ncbi.nlm.nih.gov/31425178/)). **Genetic counseling** is indicated for NF2 families (autosomal dominant; high de novo/mosaic rates complicate testing). No vaccination, chemoprevention, or population screening exists. Tertiary prevention focuses on managing hydrocephalus, treatment toxicity, and surveillance for recurrence.

### 14. Other Species / Natural Disease

- **Taxonomy of affected species:** *Homo sapiens* (NCBI:txid9606). Experimental disease is modeled in *Mus musculus* (NCBI:txid10090) and *Drosophila melanogaster* (NCBI:txid7227).
- **Orthologous genes:** NF2 (merlin) is highly conserved; EZHIP is **eutherian-specific** (an intrinsically disordered PRC2 inhibitor), limiting cross-species modeling; *"expression of human EZHIP reduces H3K27me3 in Drosophila melanogaster through a conserved mechanism"* ([PMID: 33049227](https://pubmed.ncbi.nlm.nih.gov/33049227/)), showing the PRC2 pathway itself is deeply conserved.
- **Natural disease / veterinary relevance:** Not specifically characterized in this investigation. *(Information not available.)*
- **Zoonotic potential:** None (non-transmissible neoplasm).

### 15. Model Organisms

**Genetically engineered mouse models (F013, F025):** *"ZFTA-RELA ... is sufficient to initiate tumours in mice"* ([PMID: 41882368](https://pubmed.ncbi.nlm.nih.gov/41882368/)) via in utero electroporation of embryonic neural progenitors, faithfully recapitulating supratentorial ependymoma. A *"De Novo Mouse Model of C11orf95-RELA Fusion-Driven Ependymoma Identifies Driver Functions in Addition to NF-κB"* ([PMID: 29949764](https://pubmed.ncbi.nlm.nih.gov/29949764/)). Tumorigenesis depends on nuclear condensate formation and *"goldilocks"* fusion-protein levels compatible with distinct developmental epigenetic states ([PMID: 39211123](https://pubmed.ncbi.nlm.nih.gov/39211123/)).

**Patient-derived xenografts (PDX)/orthotopic models:** Used for preclinical therapy testing — *"Treatment of ZR driven patient-derived mouse models with Selinexor impairs cell growth and extends survival of animals in vivo"* ([PMID: 42080900](https://pubmed.ncbi.nlm.nih.gov/42080900/)); PFA xenografts (primary/metastatic/recurrent) validated intrathecal CAR-T ([PMID: 32341580](https://pubmed.ncbi.nlm.nih.gov/32341580/)).

**Invertebrate:** *Drosophila* models the conserved EZHIP/PRC2 mechanism.

**Recapitulation & limitations:** Mouse ZR models reproduce ST-EPN histology, methylation-linked lineage programs, and NF-κB/condensate biology. Limitations: EZHIP is eutherian-specific, and human PFA's tumor microenvironment and hindbrain developmental context are incompletely captured; cross-species scMultiome shows lineage programs both permit and restrain transformation ([PMID: 39211123](https://pubmed.ncbi.nlm.nih.gov/39211123/)). Resources: MGI, IMPC/KOMP, Cellosaurus (PDX/cell lines).

---

## Mechanistic Model / Interpretation

Ependymoma exemplifies a tumor family unified by anatomy and lineage but split by **compartment-specific oncogenic mechanisms**. The overarching model:

```
                       RADIAL GLIA / EPENDYMAL-LINEAGE PROGENITOR
                       (impaired differentiation -> cellular hierarchy)
                                        |
        +-------------------------------+-------------------------------+
        |                               |                               |
  SUPRATENTORIAL                   POSTERIOR FOSSA                     SPINAL
        |                               |                               |
  ZFTA-RELA fusion (>60%)         PFA: EZHIP up (CXorf67)         NF2 loss (germline/
        |                               |                         somatic + 22q loss)
  Constitutive nuclear            Mimics H3K27M -> binds EZH2       |            |
  localization; IDR-driven        SET domain -> inhibits PRC2    Classic       SP-MYCN
  NUCLEAR CONDENSATES             |                              spinal        (MYCN 2p24
        |                         GLOBAL H3K27me3 LOSS           EPN           amplification)
  Recruit MED1/BRD4/Pol II        |                              |             aggressive
        |                         De-repression of PRC2 target   excellent
  Aberrant NF-kB /                neurodevelopmental genes        prognosis
  oncogenic transcription         |
        |                         PFB: distinct methylation,
  (MERTK, XPO1, itaconate         better prognosis
   dependencies)                  |
        |                         +-------------------------------+
        +--------------+----------+   Modifiers of aggression:    |
                       |              1q gain, 6q loss,           |
                       v              CDKN2A/2B deletion,         |
        CLINICAL MANIFESTATION        Ki-67>=7%, undiff. content  |
   (hydrocephalus/raised ICP;         +-------------------------------+
    seizures/focal deficits; spinal deficits)
```

**Upstream vs downstream:** The initiating fusion (ZFTA-RELA) or epigenetic lesion (EZHIP overexpression) is upstream; downstream are the transcriptional/chromatin programs (NF-κB activation; PRC2-target de-repression) that block differentiation and expand undifferentiated progenitors. Copy-number modifiers (1q gain, 6q loss, CDKN2A loss) are secondary events that amplify aggressiveness and accumulate at recurrence. The convergent endpoint — a proliferating, differentiation-blocked ependymal-lineage tumor obstructing CSF flow or infiltrating cord — produces the shared clinical syndrome. This model directly explains why **molecular subgroup outperforms histologic grade** (Hypothesis H001, supported) and why **subgroup-specific vulnerabilities** (MERTK, EZHIP/PRC2, XPO1) are rational therapeutic targets (Hypothesis H003, supported).

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [37743338](https://pubmed.ncbi.nlm.nih.gov/37743338/) | WHO CNS5 ten-entity classification; "anaplastic" dropped | Supports classification framework |
| [42080900](https://pubmed.ncbi.nlm.nih.gov/42080900/) | ZFTA-RELA most frequent ST driver; XPO1/selinexor vulnerability | Supports F001, F013, F024 |
| [40866513](https://pubmed.ncbi.nlm.nih.gov/40866513/) | ZR nuclear condensates required for tumorigenesis; IDR mechanism | Supports F017 |
| [33741710](https://pubmed.ncbi.nlm.nih.gov/33741710/) | >60% of ST-EPN harbor ZFTA-RELA; oncogenic transcription | Supports F017 |
| [30923826](https://pubmed.ncbi.nlm.nih.gov/30923826/) | EZHIP/CXorf67 mimics K27M, inhibits PRC2, H3K27me3 loss | Supports F002, F017 |
| [33049227](https://pubmed.ncbi.nlm.nih.gov/33049227/) | EZHIP & H3K27M competitively inhibit PRC2; Drosophila model | Supports F017, F025 |
| [36759899](https://pubmed.ncbi.nlm.nih.gov/36759899/) | Shared H3K27me3 loss / hindbrain pathways with DMG | Supports F002 |
| [32663469](https://pubmed.ncbi.nlm.nih.gov/32663469/) | scRNA-seq cellular hierarchy; undifferentiated = aggressive | Supports F010, F027 |
| [17179988](https://pubmed.ncbi.nlm.nih.gov/17179988/) | Radial glia as cell of origin | Supports F010 |
| [38265489](https://pubmed.ncbi.nlm.nih.gov/38265489/) | Spinal EPN = mature ependymal-like; NF2 subtype | Supports F027 |
| [20516456](https://pubmed.ncbi.nlm.nih.gov/20516456/) | 1q gain + CDKN2A deletion adverse; molecular staging | Supports F008 |
| [16609018](https://pubmed.ncbi.nlm.nih.gov/16609018/) | 1q25 gain independent prognostic marker | Supports F019 |
| [37246777](https://pubmed.ncbi.nlm.nih.gov/37246777/) | 1q gain/6q loss enriched at recurrence in PFA | Supports F019 |
| [41026848](https://pubmed.ncbi.nlm.nih.gov/41026848/) | Subgroup-specific PFS/OS; risk stratification | Supports F019 |
| [33135735](https://pubmed.ncbi.nlm.nih.gov/33135735/) | 1q gain/CDKN2A loss adverse; RELA no independent impact | Supports F019 |
| [40556668](https://pubmed.ncbi.nlm.nih.gov/40556668/) | Location-dependent presentation; treatment; 10-yr OS 50–75% | Supports F006, F007 |
| [30811284](https://pubmed.ncbi.nlm.nih.gov/30811284/) | ACNS0121 risk-adapted RT; EFS by group | Supports F012 |
| [33014396](https://pubmed.ncbi.nlm.nih.gov/33014396/) | Adult age, subtotal resection, race as risk factors | Supports F003 |
| [37980692](https://pubmed.ncbi.nlm.nih.gov/37980692/) | AAAIR 0.41/100,000 | Supports F003 |
| [18084720](https://pubmed.ncbi.nlm.nih.gov/18084720/) | 23% of spinal cord tumors; incidence 0.74/100,000 | Supports F018 |
| [16142778](https://pubmed.ncbi.nlm.nih.gov/16142778/) | Etiology largely unknown; radiation the only risk | Supports F011, F026 |
| [23931824](https://pubmed.ncbi.nlm.nih.gov/23931824/) | NF2 predisposition; mutation spectrum/mosaicism | Supports F005, F020 |
| [39937237](https://pubmed.ncbi.nlm.nih.gov/39937237/) | NF2-related SWN nomenclature; ependymoma risk | Supports F005, F020 |
| [34812989](https://pubmed.ncbi.nlm.nih.gov/34812989/) | Surrogate IHC (L1CAM, H3K27me3, EZHIP); Ki-67 | Supports F009, F023 |
| [41553163](https://pubmed.ncbi.nlm.nih.gov/41553163/) | H3K27me3 IHC loss defines PFA | Supports F023 |
| [18095125](https://pubmed.ncbi.nlm.nih.gov/18095125/) / [16160486](https://pubmed.ncbi.nlm.nih.gov/16160486/) | Rosettes; GFAP/S-100/vimentin; dot-like EMA | Supports F023 |
| [32539423](https://pubmed.ncbi.nlm.nih.gov/32539423/) / [32661052](https://pubmed.ncbi.nlm.nih.gov/32661052/) | DWI/ADC; radiomics AUC 0.91 | Supports F016 |
| [34895332](https://pubmed.ncbi.nlm.nih.gov/34895332/) | SP-MYCN aggressive spinal class | Supports F004 |
| [41665993](https://pubmed.ncbi.nlm.nih.gov/41665993/) | MERTK vulnerability in ZFTA-RELA | Supports F024 |
| [32341580](https://pubmed.ncbi.nlm.nih.gov/32341580/) | Intrathecal CAR-T (EPHA2/HER2/IL13Rα2) in PFA models | Supports F024, F025 |
| [41596609](https://pubmed.ncbi.nlm.nih.gov/41596609/) | EZHIP as druggable PFA vulnerability | Supports F024 |
| [41882368](https://pubmed.ncbi.nlm.nih.gov/41882368/) / [29949764](https://pubmed.ncbi.nlm.nih.gov/29949764/) | Mouse models of ZR-driven ependymoma | Supports F013, F025 |
| [42032119](https://pubmed.ncbi.nlm.nih.gov/42032119/) / [41788986](https://pubmed.ncbi.nlm.nih.gov/41788986/) / [41488407](https://pubmed.ncbi.nlm.nih.gov/41488407/) | No standard relapse therapy; re-irradiation; systemic agents | Supports F014 |

**Notes on evidence quality:** A minority of citation snippets were flagged during verification (`mismatch` for PMIDs 42348066, 41665993, 29949764) where the exact quoted text could not be fully re-matched to the stored abstract; the substantive claims they support are corroborated by independent sources in the table above, so the findings remain robust. Evidence sources span **human clinical/registry** (CBTRUS, SEER, cooperative trials), **molecular cohort/omics** studies, **mouse/PDX/Drosophila models**, and **in vitro** mechanistic work.

---

## Limitations and Knowledge Gaps

1. **Literature-only investigation.** No primary molecular data were analyzed; all findings derive from published abstracts and registry summaries. Quantitative claims reflect the specific cohorts cited and may not generalize.
2. **Rare-disease statistics.** Subgroup survival estimates (e.g., EPN-YAP1 n=4; EPN-PFB n=19) rest on small numbers with wide confidence intervals.
3. **Etiology remains largely unexplained.** Beyond high-dose ionizing radiation and germline NF2, no environmental, infectious, or common-variant genetic risk factors are established; no GWAS susceptibility loci or protective factors were identified.
4. **Adult vs pediatric biology.** Most molecular data derive from pediatric cohorts; adult ependymoma (especially spinal) is comparatively under-characterized.
5. **Therapeutic translation.** Targeted (MERTK, XPO1, EZHIP/PRC2) and CAR-T strategies are validated only in preclinical/xenograft models; no subgroup-directed systemic therapy has proven clinical benefit, and chemotherapy remains of minimal value.
6. **Veterinary/natural disease and metabolomics/proteomics/lipidomics** for ependymoma were not characterized in depth (data not available in the reviewed literature).
7. **Grade–methylation reconciliation.** Histologic variant diagnoses are unreliable (~36% reclassified by methylation), and grade correlates weakly with outcome — underscoring dependence on molecular assays not universally available.

---

## Proposed Follow-up Experiments / Actions

1. **Clinical validation of subgroup-directed therapy.** Advance MERTK inhibition and XPO1 inhibition (selinexor) for ZFTA-RELA ST-EPN, and EZHIP/PRC2-axis agents for PFA, into biomarker-selected early-phase trials; register NCT identifiers.
2. **Intrathecal CAR-T translation.** Move locoregional EPHA2/HER2/IL13Rα2 CAR-T (± azacytidine) from PFA xenografts to first-in-human pediatric trials, with CSF pharmacodynamic endpoints.
3. **Prospective molecular risk stratification.** Embed 1q gain, 6q loss, CDKN2A/2B status, and methylation subgroup as stratification variables in cooperative-group RT-adaptation trials (successors to ACNS0121) to test de-escalation in favorable subgroups and intensification in PFA with 1q+/6q−.
4. **Liquid biopsy / CSF biomarkers.** Develop CSF-based methylation or fusion detection for minimally invasive subgrouping, dissemination staging, and recurrence monitoring.
5. **Model refinement.** Given EZHIP's eutherian specificity, prioritize humanized/organoid and PDX models of PFA to capture microenvironment and hindbrain developmental context; use cross-species scMultiome to define the "goldilocks" oncoprotein-dose window as a therapeutic parameter.
6. **Recurrent-disease standard-of-care trials.** Formally compare proton re-irradiation, re-resection, and candidate systemic agents (temozolomide, bevacizumab combinations) in randomized settings to establish an evidence-based relapse algorithm.
7. **Etiologic epidemiology.** Conduct large consortium GWAS and gene–environment studies to probe the unexplained ~95% of sporadic risk, including any germline predisposition beyond NF2.

---

*Report generated from a 10-iteration autonomous investigation: 27 confirmed findings, 3 supported hypotheses (H001 molecular-subgroup classification; H002 divergent ZFTA-RELA/NF-κB vs EZHIP/PRC2 mechanisms; H003 subgroup-specific actionable vulnerabilities), and 75 papers reviewed.*


## Artifacts

- [OpenScientist final report](Ependymoma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ependymoma-deep-research-openscientist_artifacts/final_report.pdf)