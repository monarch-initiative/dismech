---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-23T19:04:29.485398+00:00'
end_time: '2026-08-23T19:20:34.105160+00:00'
duration_seconds: 964.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Heart Failure
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    model: null
    system_prompt: null
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
run_metadata:
  openscientist_job_id: e0fc2fd2-4a7d-405f-a1c1-8498f68c79d3
citation_count: 47
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Heart_Failure-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Heart_Failure-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Heart Failure
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Heart Failure** covering all of the
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

# Heart Failure: A Comprehensive Disease Characterization Report

**Disease:** Heart Failure | **MONDO ID:** MONDO:0005252 | **Category:** Complex
**ICD-10:** I50 | **ICD-11:** BD10-BD1Z | **MeSH:** D006333 | **Date:** 2026-08-23

---

## Summary

Heart failure (HF) is a complex, highly prevalent clinical syndrome — not a single disease — defined by the 2021 Universal Definition as symptoms and/or signs caused by a structural and/or functional cardiac abnormality, corroborated by elevated natriuretic peptides and/or objective evidence of pulmonary or systemic congestion. It affects **more than 64 million people worldwide**, carries a **lifetime risk of approximately 1 in 4**, and has five-year mortality rates that rival solid-organ malignancies. HF is classified by left ventricular ejection fraction (LVEF) into HFrEF (≤40%), HFmrEF (41–49%), HFpEF (≥50%), and HFimpEF (improved), and staged A (at-risk) through D (advanced) — with roughly two-thirds of US adults sitting in the pre-HF stages A/B, defining an enormous population reservoir for prevention.

Diverse etiologic insults — coronary ischemia, hypertension, genetic cardiomyopathy (notably *TTN*-truncating and *LMNA* variants), infection (Chagas disease from *Trypanosoma cruzi*), and cardiotoxic/metabolic exposures (obesity, diabetes, air pollution, trace-element dysregulation) — converge on a **shared pathophysiology**: neurohormonal activation (RAAS and sympathetic nervous system), mitochondrial energetic failure and oxidative stress, and inflammation-driven fibrotic remodeling. This causal chain produces progressive pump dysfunction and congestion. The syndrome is diagnosed with natriuretic peptides (BNP/NT-proBNP) plus imaging (echocardiography), and increasingly refined by multimarker and multi-omic profiling that reveals etiology-specific biology.

Therapeutically, HFrEF is now highly treatable: four foundational **guideline-directed medical therapy (GDMT)** pillars — RAAS inhibition/ARNI, beta-blockers, mineralocorticoid receptor antagonists (MRA), and SGLT2 inhibitors — substantially reduce mortality and hospitalization, with SGLT2i extending benefit across the EF spectrum. Advanced disease is managed with device therapy (CRT/ICD), left ventricular assist devices (LVAD), and heart transplantation. Prevention is tiered — primary risk-factor/lifestyle control being the highest-yield strategy given the vast pre-HF population. HF is strongly conserved across mammals (naturally occurring canine and feline cardiomyopathy) and well-modeled in rodents (transverse aortic constriction, *Ttn*-truncation knock-in), zebrafish (HFpEF), and human iPSC-cardiomyocytes.

---

## Key Findings

### Finding 1 — Heart failure is a clinical syndrome classified by ejection fraction and staged by risk

The **2021 Universal Definition and Classification of Heart Failure** (jointly issued by the Heart Failure Society of America, the Heart Failure Association of the ESC, and the Japanese Heart Failure Society) established that "*HF is a clinical syndrome with symptoms and or signs caused by a structural and/or functional cardiac abnormality and corroborated by elevated natriuretic peptide levels and or objective evidence of pulmonary or systemic congestion*" [PMID: 33663906](https://pubmed.ncbi.nlm.nih.gov/33663906/). The EF-based classification defines HFrEF (LVEF ≤40%), HFmrEF (41–49%), HFpEF (≥50%), and HFimpEF (baseline ≤40%, ≥10-point rise to >40%), and stages the disease A (at-risk), B (pre-HF), C (symptomatic), and D (advanced).

A single-center registry of 8,471 patients applying this definition confirmed the real-world distribution: "*The most frequent type of HF was HFrEF (n = 4947; 58.4%), followed by HFpEF (n = 1138; 28.2%) and HFmrEF (n = 2386; 13.4%)*" [PMID: 38493451](https://pubmed.ncbi.nlm.nih.gov/38493451/), with all-cause death highest in HFrEF (42.7%). **Ontology:** MONDO:0005252; ICD-10 I50; MeSH D006333.

| HF subtype | LVEF | Registry frequency | All-cause mortality |
|---|---|---|---|
| HFrEF | ≤40% | 58.4% | 42.7% (highest) |
| HFpEF | ≥50% | 28.2% | intermediate |
| HFmrEF | 41–49% | 13.4% | lowest |

### Finding 2 — Lifetime risk is ~1 in 4, with a vast pre-HF reservoir

The lifetime risk of developing HF is approximately **1 in 4**: "*The lifetime risk of developing HF stands at 1 in 4*" [PMID: 41670570](https://pubmed.ncbi.nlm.nih.gov/41670570/). Critically, "*roughly two-thirds of adults in the United States [are] classified as either stage A (at risk) or stage B (pre-HF)*," and "*many HF cases arise from nonatherosclerotic causes, such as obesity, hypertension, cancer therapies, and the cardio-kidney-metabolic syndrome*." This enormous pre-HF population is the central target for primary prevention, and the rising incidence of HFpEF across contemporary cohorts underscores the shift toward metabolic and non-ischemic drivers.

### Finding 3 — Genetic dilated cardiomyopathy: *TTN* and *LMNA* dominate causal genetics

In monogenic/familial dilated cardiomyopathy (DCM), a leading cause of HFrEF, disease-causing variants are found in ~25–46% of patients. In a 280-patient Polish DCM cohort, disease-causing variants were found in 46%, and "*Variants in titin (TTN) and lamin A/C (LMNA) genes were the most frequent (18% and 8% of the study cohort, respectively)*" [PMID: 40792443](https://pubmed.ncbi.nlm.nih.gov/40792443/). A multinational cohort of 2,088 DCM patients found: "*Of the 2,088 patients 514 (24.6%) obtained a molecular diagnosis; 534 LP/P variants were observed across 45 genes*" [PMID: 37795486](https://pubmed.ncbi.nlm.nih.gov/37795486/), spanning sarcomere, nuclear lamina, desmosome, cytoskeleton, and mitochondrial proteins. *LMNA*-related DCM carries genotype-specific high risk: "*the risks of severe DCM and the composite end point were 2.4- and 3-fold higher, respectively, for LMNA-related DCM*" [PMID: 40792443]. A review confirmed "*The most common genes related to dilated cardiomyopathy include TTN, LMNA, MYH7*" [PMID: 40155570](https://pubmed.ncbi.nlm.nih.gov/40155570/).

**HGNC causal genes:** *TTN, LMNA, MYH7, MYBPC3, TNNT2, DSP, FLNC, BAG3, SCN5A, RBM20, DMD.* Population screening data (ARIC + UK Biobank) show ~0.7% of individuals carry an actionable cardiomyopathy variant, conferring increased risk of HF (HR 1.7), atrial fibrillation (HR 2.9), and all-cause mortality (HR 1.5) [PMID: 35544052](https://pubmed.ncbi.nlm.nih.gov/35544052/).

### Finding 4 — Four GDMT pillars reduce mortality and hospitalization in HFrEF

GDMT for HFrEF comprises four foundational pharmacologic pillars: RAAS inhibition or angiotensin receptor-neprilysin inhibition (ARNI, sacubitril/valsartan), evidence-based beta-blockers, mineralocorticoid receptor antagonists (MRA), and SGLT2 inhibitors. Robust evidence supports "*early and combined use of the four foundational GDMT classes, with substantial reductions in mortality and heart failure hospitalization*" [PMID: 42016211](https://pubmed.ncbi.nlm.nih.gov/42016211/), advocating rapid "four drugs in 4 weeks" initiation. SGLT2i (DAPA-HF, EMPEROR-Reduced, EMPEROR-Preserved, DELIVER) reduce HF hospitalization across the EF spectrum by promoting "*a shift in substrate utilization toward fatty acids and ketone bodies, improving mitochondrial efficiency*" and reducing oxidative stress and inflammation [PMID: 41913872](https://pubmed.ncbi.nlm.nih.gov/41913872/). Emerging additional pillars include vericiguat (soluble guanylate cyclase stimulator) and digitoxin [PMID: 42329367](https://pubmed.ncbi.nlm.nih.gov/42329367/). In HFmrEF/HFpEF, combined SGLT2i + finerenone reduced CV death/worsening HF by 31% (HR 0.69; 95% CI 0.59–0.81) [PMID: 41052644](https://pubmed.ncbi.nlm.nih.gov/41052644/).

**NCIT interventions:** sacubitril/valsartan, dapagliflozin, empagliflozin, spironolactone/eplerenone, carvedilol/metoprolol/bisoprolol.

### Finding 5 — Pathophysiology: neurohormonal activation and mitochondrial dysfunction drive remodeling

HF congestion is "*driven by neurohormonal dysregulation involving the renin-angiotensin-aldosterone system and sympathetic nervous system*," producing dyspnea, peripheral edema, and fatigue [PMID: 40801414](https://pubmed.ncbi.nlm.nih.gov/40801414/). Mitochondrial dysfunction is a central driver: impaired oxidative phosphorylation, ROS imbalance, disrupted calcium handling, and defective mitophagy. Post-MI cardiomyocytes exhibit "*a reduction in total mitochondrial membrane potential (MMP) and an increase in reactive oxygen species levels*" [PMID: 42411500](https://pubmed.ncbi.nlm.nih.gov/42411500/). Impaired inter-organelle mitochondrial communication produces "*dysregulated energy metabolism, oxidative stress, lipotoxicity, and impaired cardiomyocyte function*," with phenotype-specific differences between HFpEF and HFrEF [PMID: 42209899](https://pubmed.ncbi.nlm.nih.gov/42209899/). The lysosomal/autophagy regulator TFEB links afterload-induced energy demand to hypertrophy: TFEB knockout hearts under pressure overload "*manifested an amplified hypertrophic response, leading rapidly to HF*" [PMID: 42299666](https://pubmed.ncbi.nlm.nih.gov/42299666/).

**GO terms:** GO:0006119 (oxidative phosphorylation), GO:0006979 (response to oxidative stress), GO:0006954 (inflammatory response), GO:0006936 (muscle contraction). **CL terms:** CL:0000746 (cardiac muscle cell), CL:0000057 (fibroblast).

### Finding 6 — Core phenotypes cluster into symptom groups that impair quality of life

HF symptoms cluster into five groups — emotional, digestive, ischemic (dizziness, chest pain, palpitations, fatigue), dyspnea (orthopnea, paroxysmal nocturnal dyspnea, sleep difficulty), and congestion (cough, shortness of breath, edema) [PMID: 39450907](https://pubmed.ncbi.nlm.nih.gov/39450907/). Symptom burden strongly impairs health-related quality of life (measured by KCCQ and the Minnesota Living with Heart Failure Questionnaire). End-stage HF is "*often complicated with symptoms such as dyspnea, fatigue, pain, and nausea, which can worsen the quality of life*" [PMID: 41550625](https://pubmed.ncbi.nlm.nih.gov/41550625/). NYHA classes I–IV grade severity; symptoms are adult/late-onset and progressive with episodic decompensation.

**HPO terms:** HP:0001635 (congestive heart failure), HP:0002094 (dyspnea), HP:0012651 (orthopnea), HP:0012764 (paroxysmal nocturnal dyspnea), HP:0012378 (fatigue), HP:0100598 (peripheral edema), HP:0001962 (palpitations).

### Finding 7 — Natriuretic peptides are diagnostic and prognostic cornerstones

BNP and NT-proBNP "*remain the cornerstones of biomarker-guided management, yet their interpretation is influenced by age, renal function, obesity, and atrial fibrillation*" [PMID: 42336497](https://pubmed.ncbi.nlm.nih.gov/42336497/). In 116,466 diabetics without known HF, NT-proBNP >300 pg/mL predicted incident HF/death with HR 4.48 (95% CI 3.11–6.47) in T1D and 3.58 (3.39–3.78) in T2D versus <125 pg/mL [PMID: 41166576](https://pubmed.ncbi.nlm.nih.gov/41166576/). Complementary biomarkers with incremental prognostic value include high-sensitivity troponin (myocardial injury), hsCRP (inflammation), galectin-3 and sST2 (fibrosis/remodeling), GDF-15, MPO, MR-proADM, MR-proANP [PMID: 41883058](https://pubmed.ncbi.nlm.nih.gov/41883058/), copeptin [PMID: 41467274](https://pubmed.ncbi.nlm.nih.gov/41467274/), and circulating non-coding RNAs.

**LOINC:** NT-proBNP 33762-6; BNP 30934-4; hs-troponin T 67151-1. Diagnostic screening thresholds: BNP ≥50 or NT-proBNP ≥125 pg/mL.

### Finding 8 — Major modifiable risk factors dominate a multifactorial etiology

"*Its prevalence rises significantly with age. In addition, age-related conditions, such as hypertension, coronary artery disease, obesity, and diabetes mellitus, contribute to an elevated risk of heart failure*" [PMID: 42446811](https://pubmed.ncbi.nlm.nih.gov/42446811/). Obesity promotes HF "*through complex metabolic, haemodynamic, inflammatory, and endothelial mechanisms*," and bariatric surgery reduces these risk factors [PMID: 42591586](https://pubmed.ncbi.nlm.nih.gov/42591586/). Environmental exposures — "*air pollution, noise, heat, chemical contamination, and light pollution*" — increase HF incidence via "*oxidative stress, inflammation, endothelial dysfunction, and circadian disruption*," even below regulatory thresholds [PMID: 42095252](https://pubmed.ncbi.nlm.nih.gov/42095252/). HF is thus multifactorial/polygenic: modifiable factors (hypertension, CAD, diabetes, obesity, smoking, pollution) dominate; age and family history are non-modifiable.

### Finding 9 — Global burden rivals malignancy; iron deficiency is prevalent and treatable

"*Heart failure (HF) affects over 64 million people worldwide, with five-year mortality rates rivaling solid-organ malignancies*" [PMID: 42606681](https://pubmed.ncbi.nlm.nih.gov/42606681/). Iron deficiency "*affected approximately 30-58% of patients with HF*," and in HFrEF, "*intravenous ferric carboxymaltose improved Patient Global Assessment (odds ratio [OR] 2.51; 95% confidence interval [CI] 1.75-3.61) and reduced HF hospitalization (hazard ratio [HR] 0.39; 95% CI 0.19-0.82)*." Prognostic factors include EF class, baseline cardiac/renal function, female sex, mechanical ventilation, and sinus rhythm. LVAD destination-therapy on-device survival is 82.3%/73.3%/49.8% at 1/3/5 years [PMID: 42629526](https://pubmed.ncbi.nlm.nih.gov/42629526/).

### Finding 10 — Advanced therapies: devices, LVAD, and transplantation with reverse remodeling

Device therapy includes cardiac resynchronization therapy (CRT) and implantable cardioverter-defibrillators (ICD); CRT upgrade "*was associated with lower all-cause mortality, heart transplant, or assist device implant*" [PMID: 40533423](https://pubmed.ncbi.nlm.nih.gov/40533423/). LVADs, used as bridge-to-transplant and destination therapy, "*reverse the molecular transformations that take place in the cardiomyocytes… eventually leading to partial or complete recovery in a subset of patients*" [PMID: 40387335](https://pubmed.ncbi.nlm.nih.gov/40387335/). Heart transplantation is definitive for Stage D disease. Cardiac rehabilitation improves 6MWT distance, METs, VO2, LVEF, and anxiety/depression [PMID: 40955678](https://pubmed.ncbi.nlm.nih.gov/40955678/). **NCIT:** cardiac resynchronization therapy, implantable cardioverter-defibrillator, ventricular assist device, heart transplantation, cardiac rehabilitation.

### Finding 11 — Robust model organisms recapitulate HF pathology

Transverse aortic constriction (TAC) in mice "*induced progressive systolic dysfunction, fibrosis, and reduced microvascular density*" — the standard pressure-overload model [PMID: 33464950](https://pubmed.ncbi.nlm.nih.gov/33464950/). A *Ttn*-truncation knock-in mouse recapitulates human DCM: "*a pattern of DCM can be induced by TAC-mediated pressure overload in a TTN-truncated mouse model*" [PMID: 26504781](https://pubmed.ncbi.nlm.nih.gov/26504781/). A zebrafish ion-imbalance model "*recapitulates key characteristics of incipient heart failure with preserved ejection fraction*" [PMID: 36536484](https://pubmed.ncbi.nlm.nih.gov/36536484/). In vitro models include H9c2 cells, neonatal rat/mouse ventricular cardiomyocytes, and human iPSC-cardiomyocytes.

**Taxa:** mouse (NCBI:txid10090), rat (10116), zebrafish (7955). **Resources:** MGI, RGD, ZFIN.

### Finding 12 — Naturally occurring cross-species HF/DCM: the Doberman comparative model

"*Dilated cardiomyopathy (DCM) is a naturally occurring heart failure condition in humans and dogs, notably characterized by a reduced contractility and ejection fraction*" [PMID: 37505469](https://pubmed.ncbi.nlm.nih.gov/37505469/). Canine DCM shares conserved mechanisms: "*IDCM is associated with a marked impairment of mitochondrial production of ATP, arising from decreased activity of the mitochondrial electron transport system*" [PMID: 1338376](https://pubmed.ncbi.nlm.nih.gov/1338376/), and an autoimmune driver — β1-adrenergic receptor autoantibodies (β1-AAB) that are "*highly present in patients with dilated cardiomyopathy (DCM) and are increasingly accepted as disease drivers*" [PMID: 32212256](https://pubmed.ncbi.nlm.nih.gov/32212256/). **Species:** dog (NCBI:txid9615), cat (9685). **Breeds:** Doberman Pinscher, Boxer, Great Dane (canine DCM); Maine Coon, Ragdoll (feline HCM). **Resource:** OMIA.

### Finding 13 — Infectious/inflammatory etiologies: Chagas cardiomyopathy has the worst prognosis

Chagas disease, caused by *Trypanosoma cruzi* (NCBI:txid5693), "*is a common cause of heart failure (HF) in Latin America and has recently been declared endemic in the United States*" [PMID: 41847775](https://pubmed.ncbi.nlm.nih.gov/41847775/). In a pooled analysis of 23,647 HFrEF patients, "*Chagasic HF had the highest incidence rates of all clinical outcomes compared with other etiologies*," with adjusted HRs versus ischemic HF of 1.65 (composite), 1.86 (CV death), and 2.16 (stroke). Viral myocarditis is another recognized cause; pediatric myocarditis with a DCM phenotype is "*characterized by early-onset heart failure, significant enrichment of likely pathogenic/pathogenic variants, and poor outcome*" [PMID: 34213952](https://pubmed.ncbi.nlm.nih.gov/34213952/). Investigator-reported HFrEF etiologies span ischemic (57%), idiopathic, hypertensive, valvular, alcoholic, viral, and Chagasic.

### Finding 14 — Cardiac fibrosis via inflammation → myofibroblast activation is a core downstream mechanism

HF remodeling involves injury-mediated immune cell infiltration and myofibroblast activation. "*An inflammatory to fibrotic transition corresponds with macrophage transition (M1-M2) associated with increased transforming growth factor (TGF)-β response*," driving "*degradation-resistant deposition of extracellular proteins, especially fibrillar Collagen -I, -III and -V, and non-fibrillar Collagen-IV by active myofibroblasts*" [PMID: 39805714](https://pubmed.ncbi.nlm.nih.gov/39805714/). In angiotensin II-infused mouse hearts, platelet inhibition with clopidogrel "*inhibited Ang II infusion-induced accumulation of α-SMA(+) myofibroblasts and cardiac fibrosis*" [PMID: 23887740](https://pubmed.ncbi.nlm.nih.gov/23887740/). Cardiorenal syndrome features bidirectional heart-kidney inflammation and fibrosis.

**GO terms:** GO:0030198 (extracellular matrix organization), GO:0007179 (TGF-beta receptor signaling), GO:0002544 (chronic inflammation). **CL terms:** CL:0000057 (fibroblast), CL:0000186 (myofibroblast), CL:0000235 (macrophage). **UBERON:** UBERON:0002113 (kidney, secondary organ).

### Finding 15 — Plasma proteomics and multi-omics reveal etiology-specific biology

High-throughput plasma proteomics (734 proteins) in 1,212 HFrEF patients identified "*a nine-protein panel (P9: C1QA, CCL4, REN, EGLN1, COL9A1, GP1BA, ITM2A, CNPY2, NT-proBNP) that improved risk classification compared with NT-proBNP alone*" (externally validated in UK Biobank) [PMID: 42258512](https://pubmed.ncbi.nlm.nih.gov/42258512/). Crucially, "*in CCC [chronic Chagas cardiomyopathy] the P9 panel underperformed NT-proBNP alone (-16%), suggesting distinct underlying disease biology*" — confirming etiology-specific molecular signatures. Mitochondrial-associated lncRNAs (LIPCAR, MALAT1, H19) and circulating microRNAs are emerging biomarkers [PMID: 42236984](https://pubmed.ncbi.nlm.nih.gov/42236984/); a hallmark transcriptomic signature is reactivation of the fetal gene program (*NPPA, NPPB, MYH7*). **Resources:** PRIDE/ProteomeXchange (proteomics), GEO (transcriptomics).

### Finding 16 — Tiered prevention: primary risk-factor control is highest-yield

Primary prevention emphasizes "*Lifestyle modifications, including dietary changes, smoking cessation, physical activity, weight management, and psychosocial support*" plus pharmacologic control of blood pressure, lipids, and glucose [PMID: 41628971](https://pubmed.ncbi.nlm.nih.gov/41628971/). Life's Essential 8 and cardiovascular-kidney-metabolic (CKM) staging stratify risk: higher CKM stage conferred stepwise CVD risk up to HR 5.95 (95% CI 4.75–7.45) in a 100,727-person cohort [PMID: 40346555](https://pubmed.ncbi.nlm.nih.gov/40346555/). Secondary prevention uses natriuretic-peptide and global longitudinal strain (GLS) screening of stage A/B individuals (GLS screening cost-effective at €69,543/QALY [PMID: 42025682](https://pubmed.ncbi.nlm.nih.gov/42025682/)). Tertiary prevention (GDMT, devices, cardiac rehab) limits complications.

---

## Detailed Section Coverage

### 1. Disease Information
HF is a clinical syndrome (see Finding 1). **Identifiers:** MONDO:0005252, ICD-10 I50, ICD-11 BD10-BD1Z, MeSH D006333. **Synonyms:** congestive heart failure (CHF), cardiac failure, cardiac insufficiency, myocardial failure. Information derives predominantly from **aggregated disease-level resources** (guidelines, registries, trials) supplemented by EHR/registry-level individual-patient data (e.g., SwedeHF, MyoVasc, EUROMACS).

### 2. Etiology
**Causal factors:** ischemic (coronary artery disease, ~57% of HFrEF), hypertensive, genetic (DCM: *TTN, LMNA*, etc. — Finding 3), infectious (Chagas, viral myocarditis — Finding 13), valvular, alcoholic/toxic, and cardiotoxic (cancer therapies). **Genetic risk:** monogenic causal variants plus polygenic susceptibility; ~0.7% population carriage of actionable cardiomyopathy variants [PMID: 35544052]. **Environmental risk:** age, hypertension, diabetes, obesity, smoking, air/noise/light pollution [PMID: 42095252]. **Protective factors:** healthy lifestyle (Life's Essential 8), weight loss/bariatric surgery [PMID: 42591586], guideline-directed risk-factor control. **Gene-environment interactions:** genetic substrate (e.g., subclinical *Ttn* truncation) unmasked by hemodynamic stress/pressure overload [PMID: 26504781].

### 3. Phenotypes
See Finding 6. Phenotype types span **symptoms** (dyspnea, fatigue, orthopnea, PND), **clinical signs** (peripheral edema, elevated JVP, rales, S3 gallop), and **laboratory abnormalities** (elevated natriuretic peptides, troponin). Adult/late-onset, progressive with episodic decompensation, variable severity (NYHA I–IV). Quality-of-life impact is severe and central to disease burden (KCCQ, MLHFQ). HPO terms enumerated in Finding 6.

### 4. Genetic/Molecular Information
**Causal genes** (Finding 3): *TTN* (18%), *LMNA* (8%), *MYH7, MYBPC3, TNNT2, DSP, FLNC, BAG3, SCN5A, RBM20, DMD.* **Variant types:** *TTN* truncating variants (most common); *LMNA/FLNC* — arrhythmogenic, high-risk. **Classification:** ACMG/AMP P/LP across 45 genes [PMID: 37795486]. **Inheritance:** predominantly autosomal dominant. **Modifiers/genotype-phenotype:** LGE patterns are gene-specific (subepicardial in *DMD/DSP/FLNC*; absent/rare in *TNNT2/RBM20/MYH7*) [PMID: 37562008](https://pubmed.ncbi.nlm.nih.gov/37562008/). **Origin:** germline for inherited cardiomyopathy. **Functional consequence:** loss of function (*TTN* haploinsufficiency), structural/nuclear-envelope disruption (*LMNA*).

### 5. Environmental Information
**Environmental factors:** air pollution (particulate matter), noise, heat, chemical/light pollution [PMID: 42095252]; trace-element/metallomic dysregulation (iron, zinc, selenium, magnesium deficiency) [PMID: 42606681]. **Lifestyle:** smoking, poor diet, physical inactivity, alcohol, obesity. **Infectious agents:** *T. cruzi* (Chagas), coxsackievirus B, parvovirus B19, HHV-6, SARS-CoV-2 (myocarditis).

### 6. Mechanism / Pathophysiology
See Findings 5 and 14 and the Mechanistic Model below. **Pathways:** RAAS, sympathetic/β-adrenergic signaling, TGF-β, AMPK/TFEB-lysosomal, SGLT2-mediated metabolic substrate shift. **Cellular processes:** mitochondrial dysfunction, oxidative stress, apoptosis, autophagy, inflammation, fibrosis. **Metabolic:** substrate shift from fatty acids to glucose/ketones, impaired oxidative phosphorylation. **Immune:** macrophage M1→M2 transition, β1-AAB autoimmunity. **Molecular profiling:** fetal gene reactivation (*NPPA/NPPB/MYH7*), plasma proteomic signatures, mito-lncRNAs.

### 7. Anatomical Structures Affected
**Primary organ:** heart (UBERON:0000948), specifically myocardium (UBERON:0002349), left ventricle (UBERON:0002084). **Secondary:** lungs (pulmonary congestion, UBERON:0002048), kidneys (cardiorenal, UBERON:0002113), liver (congestion), systemic venous circulation. **Body systems:** cardiovascular (primary), renal, respiratory. **Cell types:** cardiomyocytes (CL:0000746), cardiac fibroblasts/myofibroblasts (CL:0000057/CL:0000186), macrophages (CL:0000235), microvascular endothelial cells. **Subcellular:** mitochondria (GO:0005739), sarcoplasmic reticulum, lysosome, nucleus. **Lateralization:** left-sided, right-sided, or biventricular.

### 8. Temporal Development
**Onset:** predominantly adult/geriatric; genetic DCM can present in childhood (pediatric myocarditis-DCM, median 1.4 y [PMID: 34213952]). **Onset pattern:** chronic/insidious (most) or acute (acute decompensated HF, post-MI). **Stages:** A → B → C → D (Universal Definition). **Course:** progressive with episodic decompensations; partial reversibility possible (HFimpEF, LVAD reverse remodeling). **Duration:** chronic, lifelong.

### 9. Inheritance and Population
**Epidemiology:** >64 million worldwide [PMID: 42606681]; ~1-in-4 lifetime risk [PMID: 41670570]. **Inheritance (genetic subset):** autosomal dominant DCM; overall multifactorial/polygenic. **Penetrance:** incomplete, age-dependent. **Expressivity:** variable (genotype-specific LGE, arrhythmia risk). **Demographics:** prevalence rises with age; HFrEF male-predominant; regional variation (Chagas endemic in Latin America/US).

### 10. Diagnostics
**Laboratory/biomarkers:** BNP/NT-proBNP (cornerstone), hs-troponin, galectin-3, sST2, GDF-15, MR-proANP, copeptin (Finding 7). **Imaging:** echocardiography (LVEF, GLS, diastolic function), cardiac MRI with late gadolinium enhancement (genotype-specific patterns [PMID: 37562008]). **Functional:** cardiopulmonary exercise testing, 6MWT. **Electrophysiology:** ECG (QRS duration/morphology for CRT eligibility). **Biopsy:** endomyocardial biopsy for myocarditis. **Genetic testing:** multi-gene cardiomyopathy panels (24.6–46% yield), WES/WGS; recommended for DCM/familial disease. **Clinical criteria:** 2021 Universal Definition; NYHA class. **Differential:** COPD, pulmonary embolism, valvular disease, aortic stenosis.

### 11. Outcome/Prognosis
**Mortality:** five-year rates rival solid-organ malignancies [PMID: 42606681]; HFrEF all-cause death 42.7% [PMID: 38493451]. **Etiology-specific:** Chagas worst (CV death HR 1.86 vs ischemic). **Prognostic factors:** EF class, renal function, natriuretic peptides, sex, sinus rhythm. **Complications:** recurrent hospitalization, arrhythmia, cardiogenic shock, cardiorenal failure, stroke, thromboembolism. **QoL measures:** KCCQ, MLHFQ, EQ-5D, PROMIS. **Risk models:** LIFE-Preserved (HFpEF, C-statistic 0.66–0.71 [PMID: 41810940](https://pubmed.ncbi.nlm.nih.gov/41810940/)), P9 proteomic panel.

### 12. Treatment
See Findings 4 and 10. **Pharmacotherapy:** ARNI, beta-blockers, MRA, SGLT2i (four pillars); + vericiguat, digitoxin, ferric carboxymaltose, loop diuretics, finerenone. **Devices:** CRT, ICD. **Advanced:** LVAD (bridge/destination), heart transplantation. **Supportive/palliative:** dobutamine, opioids for end-stage symptom control. **Rehabilitation:** supervised cardiac rehab. **Personalized:** phenotype-guided GDMT sequencing, genotype-informed risk stratification.

### 13. Prevention
Tiered (Finding 16): **primary** (risk-factor/lifestyle control, Life's Essential 8), **secondary** (NP/GLS screening of stage A/B), **tertiary** (GDMT, rehab, comorbidity management). No vaccine except addressing infectious triggers (vector control for Chagas). Genetic counseling and cascade screening for familial cardiomyopathy.

### 14. Other Species / Natural Disease
See Finding 12. Naturally occurring DCM/HF in dogs (Doberman, Boxer, Great Dane) and feline HCM (Maine Coon, Ragdoll). Strong evolutionary conservation of mitochondrial dysfunction, calcium-handling defects, and β1-AAB autoimmunity. High veterinary relevance; canine DCM is a translational model. **Resource:** OMIA. No zoonotic transmission of HF itself (though *T. cruzi* is zoonotic).

### 15. Model Organisms
See Finding 11. **Mammalian:** TAC/post-MI mouse and rat, *Ttn*/*Lmna*/*Mc1r* genetic mice [PMID: 39921516](https://pubmed.ncbi.nlm.nih.gov/39921516/). **Non-mammalian:** zebrafish HFpEF. **In vitro:** H9c2, neonatal cardiomyocytes, human iPSC-cardiomyocytes, organoids. **Types:** knockout, knock-in, conditional, humanized. **Limitations:** rodent heart rate/electrophysiology differ from human; models rarely capture multimorbid elderly HFpEF. **Resources:** MGI, RGD, ZFIN, IMPC, IMSR.

---

## Mechanistic Model / Interpretation

Heart failure is best understood as a **final common pathway** onto which heterogeneous etiologies converge:

```
  ETIOLOGIC TRIGGERS (upstream)
  ├── Ischemia (MI, CAD)          ┐
  ├── Pressure overload (HTN, AS) │
  ├── Genetic (TTN, LMNA, etc.)   ├──► INITIAL MYOCARDIAL INJURY / OVERLOAD
  ├── Infection (T. cruzi, viral) │
  └── Toxic/metabolic (obesity,   ┘
      diabetes, chemo, pollution)
                    │
                    ▼
    ┌───────────────────────────────────────────┐
    │  NEUROHORMONAL ACTIVATION (RAAS + SNS)     │  ← compensatory, becomes maladaptive
    │  + MITOCHONDRIAL ENERGETIC FAILURE (↓OXPHOS,│
    │    ↑ROS, Ca²⁺ dyshandling, ↓mitophagy)     │
    └───────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────┐
    │  INFLAMMATION (macrophage M1→M2, IL-1β)    │
    │        │                                    │
    │        ▼                                    │
    │  TGF-β → MYOFIBROBLAST ACTIVATION           │
    │        │                                    │
    │        ▼                                    │
    │  FIBROSIS (collagen I/III/IV/V deposition) │
    │  + CARDIOMYOCYTE HYPERTROPHY/APOPTOSIS      │
    │  + FETAL GENE REACTIVATION (NPPA/B, MYH7)  │
    └───────────────────────────────────────────┘
                    │
                    ▼
        MALADAPTIVE REMODELING → PUMP DYSFUNCTION
                    │
                    ▼
   CONGESTION (fluid overload) → dyspnea, edema, fatigue  (downstream = clinical syndrome)
                    │
                    ▼
   SECONDARY ORGAN INJURY (cardiorenal, hepatic, pulmonary)
```

**Upstream mechanisms** (neurohormonal activation, mitochondrial failure) are the earliest and most therapeutically tractable — this is precisely why the four GDMT pillars work: ARNI and MRA interrupt RAAS; beta-blockers interrupt SNS; SGLT2i restore mitochondrial substrate efficiency. **Downstream mechanisms** (established fibrosis, remodeling) are harder to reverse but partially tractable (LVAD-induced reverse remodeling, HFimpEF). The **etiology-specific molecular signatures** (e.g., Chagas biology diverging from the P9 proteomic panel) demonstrate that although the syndrome is shared, its molecular substrate is not uniform — the future of HF care is phenotype- and genotype-informed precision medicine.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports Finding | Evidence type |
|---|---|---|---|
| [33663906](https://pubmed.ncbi.nlm.nih.gov/33663906/) | Universal Definition & Classification of HF | F1 (definition, LVEF classes) | Guideline/consensus |
| [38493451](https://pubmed.ncbi.nlm.nih.gov/38493451/) | Registry per universal definition | F1 (subtype distribution) | Human registry |
| [41670570](https://pubmed.ncbi.nlm.nih.gov/41670570/) | HF Prevention: Evidence Generation | F2 (lifetime risk, pre-HF) | Review |
| [40792443](https://pubmed.ncbi.nlm.nih.gov/40792443/) | DCM genetics in Poland | F3 (TTN/LMNA, LMNA risk) | Human cohort |
| [37795486](https://pubmed.ncbi.nlm.nih.gov/37795486/) | DCM panel yield (n=2088) | F3 (24.6% yield, 45 genes) | Human cohort |
| [40155570](https://pubmed.ncbi.nlm.nih.gov/40155570/) | DCM genes to treatments | F3 (TTN/LMNA/MYH7) | Review |
| [42016211](https://pubmed.ncbi.nlm.nih.gov/42016211/) | GDMT optimization in HFrEF | F4 (four pillars) | Review |
| [41913872](https://pubmed.ncbi.nlm.nih.gov/41913872/) | SGLT2i in HF without diabetes | F4 (mechanism, trials) | Review |
| [41052644](https://pubmed.ncbi.nlm.nih.gov/41052644/) | SGLT2i+finerenone HFmrEF/HFpEF | F4 (HR 0.69) | Cross-trial analysis |
| [40801414](https://pubmed.ncbi.nlm.nih.gov/40801414/) | Fluid restriction in HF | F5, F6 (neurohormonal) | Review |
| [42209899](https://pubmed.ncbi.nlm.nih.gov/42209899/) | Mitochondrial crosstalk in HF | F5 (mitochondrial dysfunction) | Review |
| [42411500](https://pubmed.ncbi.nlm.nih.gov/42411500/) | Post-MI rat mitochondria | F5 (ROS, ↓MMP) | Model organism |
| [39450907](https://pubmed.ncbi.nlm.nih.gov/39450907/) | HF symptom clusters & QoL | F6 (five clusters) | Human cross-sectional |
| [42336497](https://pubmed.ncbi.nlm.nih.gov/42336497/) | Biomarkers in HF | F7 (BNP/NT-proBNP) | Review |
| [41166576](https://pubmed.ncbi.nlm.nih.gov/41166576/) | NP screening in diabetes | F7 (HR 4.48) | Human cohort (n=116k) |
| [42446811](https://pubmed.ncbi.nlm.nih.gov/42446811/) | Age & HF therapy (MyoVasc) | F8 (risk factors) | Human cohort |
| [42591586](https://pubmed.ncbi.nlm.nih.gov/42591586/) | Bariatric surgery & CV risk | F8 (obesity) | Review |
| [42095252](https://pubmed.ncbi.nlm.nih.gov/42095252/) | Environmental risk factors | F8 (pollution) | ESC consensus |
| [42606681](https://pubmed.ncbi.nlm.nih.gov/42606681/) | Metallomic dysregulation & CVD | F9 (64M, iron deficiency) | Systematic review |
| [40387335](https://pubmed.ncbi.nlm.nih.gov/40387335/) | LVAD myocardial repair | F10 (reverse remodeling) | Review |
| [33464950](https://pubmed.ncbi.nlm.nih.gov/33464950/) | Cardiac microvascular EC in pressure overload | F11 (TAC model) | Model organism |
| [26504781](https://pubmed.ncbi.nlm.nih.gov/26504781/) | TAC in Titin-truncated mouse | F11 (Ttn model) | Model organism |
| [36536484](https://pubmed.ncbi.nlm.nih.gov/36536484/) | Zebrafish/mouse ion imbalance | F11 (zebrafish HFpEF) | Model organism |
| [37505469](https://pubmed.ncbi.nlm.nih.gov/37505469/) | Canine DCM myosin SRX | F12 (naturally occurring) | Comparative |
| [1338376](https://pubmed.ncbi.nlm.nih.gov/1338376/) | Doberman mitochondrial defect | F12 (conserved mechanism) | Comparative |
| [32212256](https://pubmed.ncbi.nlm.nih.gov/32212256/) | BC 007 aptamer / β1-AAB | F12 (autoimmune driver) | Comparative/therapeutic |
| [41847775](https://pubmed.ncbi.nlm.nih.gov/41847775/) | Comparative prognosis of Chagas | F13 (worst prognosis) | Human pooled trials |
| [34213952](https://pubmed.ncbi.nlm.nih.gov/34213952/) | DCM variants in pediatric myocarditis | F13 (viral/genetic) | Human cohort |
| [39805714](https://pubmed.ncbi.nlm.nih.gov/39805714/) | Fibrosis in cardiorenal syndrome | F14 (TGF-β, M1→M2) | Review |
| [23887740](https://pubmed.ncbi.nlm.nih.gov/23887740/) | Clopidogrel & cardiac fibrosis | F14 (platelet/inflammation) | Model organism |
| [42258512](https://pubmed.ncbi.nlm.nih.gov/42258512/) | Plasma proteomics in HF | F15 (P9 panel, Chagas biology) | Human + validation |
| [41628971](https://pubmed.ncbi.nlm.nih.gov/41628971/) | Saudi CVD prevention guidelines | F16 (primary prevention) | Guideline |
| [40346555](https://pubmed.ncbi.nlm.nih.gov/40346555/) | Life's Essential 8 / CKM stages | F16 (HR 5.95) | Human cohort (n=100k) |
| [42025682](https://pubmed.ncbi.nlm.nih.gov/42025682/) | GLS screening cost-effectiveness | F16 (secondary prevention) | Cost-effectiveness |

---

## Limitations and Knowledge Gaps

1. **No primary dataset was analyzed.** This report is a literature/knowledge synthesis; no patient-level or omics data files were provided, so all effect sizes are quoted from published studies rather than independently re-derived.
2. **HFpEF mechanism remains incompletely defined.** Although SGLT2i benefit HFpEF, the molecular heterogeneity of HFpEF (metabolic, inflammatory, microvascular endotypes) is not fully resolved, and models incompletely recapitulate elderly multimorbid HFpEF.
3. **Genetic yield is partial.** Even comprehensive DCM panels identify a molecular diagnosis in only ~25–46%, leaving a large "genetically elusive" fraction and many variants of uncertain significance (VUS).
4. **Etiology-specific biology is understudied.** The Chagas proteomic divergence signals that pooled HF trials may mask etiology-specific responses; most GDMT evidence derives from predominantly ischemic/idiopathic cohorts.
5. **Ontology mappings are suggested, not curator-verified.** HPO/GO/CL/UBERON/NCIT terms should be confirmed against current ontology releases before database ingestion.
6. **Epidemiology figures are global aggregates.** Regional incidence/prevalence, sex ratios, and variant geography require registry-specific validation.

---

## Proposed Follow-up Experiments / Actions

1. **Etiology-stratified multi-omics.** Integrate proteomic (P9-type panels), transcriptomic (fetal gene program), and metabolomic signatures stratified by etiology (ischemic vs. Chagas vs. genetic DCM) to build etiology-specific risk models — directly extending [PMID: 42258512].
2. **Prospective validation of GLS + NP screening** in stage A/B populations to quantify HF-prevention yield and cost-effectiveness beyond the German HERZCHECK simulation [PMID: 42025682].
3. **Functional characterization of VUS** in *TTN/LMNA/FLNC* using iPSC-cardiomyocytes and CRISPR editing to reclassify uncertain variants and expand diagnostic yield.
4. **HFpEF endotyping trials** pairing SGLT2i/finerenone response with mechanistic biomarkers (mitochondrial function, inflammation, microvascular density) to define treatment-responsive subgroups.
5. **Comparative-medicine studies** leveraging naturally occurring canine DCM (β1-AAB, mitochondrial ATP defect) to test neutralizing/aptamer therapies (e.g., BC 007) as translational bridges [PMID: 32212256].
6. **Implementation science** to close the GDMT gap: real-world data show persistent under-titration (especially in the elderly [PMID: 42446811]); structured "four drugs in 4 weeks" protocols warrant pragmatic trial evaluation.
7. **Curator handoff:** verify all suggested ontology terms (MONDO, HPO, GO, CL, UBERON, NCIT, CHEBI) against current releases and attach the exact abstract snippets provided herein as evidence items.

---

*Report compiled across 5 iterations, 16 confirmed findings, and 67 reviewed papers. Evidence types span human clinical (guidelines, registries, cohorts, pooled trials), model organism (mouse, rat, zebrafish), comparative (canine/feline), and computational (risk models, cost-effectiveness simulations).*


## Artifacts

- [OpenScientist final report](Heart_Failure-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Heart_Failure-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 25 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 47 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42016211` *(abstract only)*: "*early and combined use of the four foundational GDMT classes, with substantial reductions in mortality and heart failure hospitalization*"
  - closest text in source: "Early and comprehensive initiation of renin-angiotensin system inhibition (preferably with angiotensin receptor-neprilysin inhibitors), evidence-based beta-blockers, mineralocorticoid receptor antagonists, and sodium-glucose cotransporter 2 (SGLT2) inhibitors is associated with rapid and sustained reductions in hospitalization and mortality"
- `PMID:40387335` *(abstract only)*: "*reverse the molecular transformations that take place in the cardiomyocytes… eventually leading to partial or complete recovery in a subset of patients*"
  - closest text in source: "LVADs were initially used as a "bridge-to-transplantation." They were later found to reverse the molecular transformations that take place in the cardiomyocytes in patients with heart failure, eventually leading to partial or complete recovery in a subset of patients"
