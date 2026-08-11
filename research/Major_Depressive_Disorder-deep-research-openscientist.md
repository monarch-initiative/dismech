---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T05:33:03.293459'
end_time: '2026-07-26T05:49:16.909248'
duration_seconds: 973.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Major Depressive Disorder
  mondo_id: ''
  category: Complex
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
citation_count: 59
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Major_Depressive_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Major_Depressive_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Major Depressive Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Major Depressive Disorder** covering all of the
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

# Major Depressive Disorder: A Comprehensive Disease-Characteristics Report

## Summary

**Major Depressive Disorder (MDD)** is a common, frequently recurrent, and highly disabling psychiatric syndrome defined clinically by standardized symptom criteria (DSM-5 / ICD-11) requiring persistent depressed mood and/or anhedonia lasting at least two weeks, accompanied by a constellation of neurovegetative, cognitive, and psychomotor symptoms. It affects approximately **5.7% of adults worldwide**, typically first onsets in adolescence or young adulthood, and follows an episodic/recurrent course. MDD is the **second leading cause of global years lived with disability (YLDs)** among all diseases (GBD 2021), making it one of the largest contributors to the worldwide burden of non-fatal health loss.

MDD is a **complex, polygenic, multifactorial disorder**. Twin studies estimate heritability at ~39–41%, and the largest genome-wide meta-analyses have identified **102+ independent risk loci** implicating synaptic biology and prefrontal cortical function. No single gene is causal; instead, thousands of common variants of small effect combine with powerful environmental exposures — most prominently **childhood trauma** (odds ratios ~2–2.8) and **stressful life events** — to produce disease. These gene-by-environment interactions are exemplified by the serotonin transporter (*SLC6A4*) 5-HTTLPR short allele, which amplifies depression risk following stress. Pathophysiology integrates at least four interacting mechanistic systems: **monoaminergic neurotransmission, hypothalamic–pituitary–adrenal (HPA) axis dysregulation, inflammation, and impaired glutamatergic neuroplasticity/neurogenesis**, all converging on fronto-limbic brain circuits (prefrontal cortex, hippocampus, amygdala, cingulate, striatum).

MDD carries substantial excess mortality (all-cause standardized mortality ratio [SMR] ≈ 1.84; suicide-specific SMR ≈ 7.9), with women affected roughly **twice as often** as men. It is, however, a treatable condition. First-line evidence-based treatments include **cognitive behavioural therapy (CBT)**, **antidepressant pharmacotherapy** (with combined CBT + antidepressant most efficacious for severe depression), **neuromodulation** (repetitive transcranial magnetic stimulation [rTMS], electroconvulsive therapy [ECT]), and, for treatment-resistant depression, **rapid-acting glutamatergic agents** such as FDA-approved intranasal esketamine. Pharmacogenomic guidance (CYP2D6, CYP2C19) can optimize antidepressant dosing. This report synthesizes 19 confirmed findings drawn from 83 reviewed papers across all 15 requested disease-characteristic domains.

---

## Key Findings

### Finding 1 — MDD is a leading global cause of disability with rising burden

Global Burden of Disease (GBD) analyses establish MDD as one of the largest single contributors to worldwide disability. In GBD 2021, **depressive and anxiety disorders ranked as the 2nd and 6th leading causes of global YLDs**, respectively, with depressive disorders among the top 25 causes of disability overall. GBD 2023 systematically estimated MDD prevalence and burden across 204 countries as one of 12 mental disorders using Bayesian meta-regression, confirming steadily rising absolute case counts driven by population growth and aging even where age-standardized rates are stable or declining.

> "depressive and anxiety disorders ranked as the 2nd and 6th leading causes of global YLDs" — [PMID: 42269957](https://pubmed.ncbi.nlm.nih.gov/42269957/)

Comparative GBD 2021 analyses show age-standardized incidence, prevalence, and DALY rates rising rapidly among individuals aged 10–24 years both globally and in high-population countries such as China, underscoring the adolescent/young-adult vulnerability window ([PMID: 42416185](https://pubmed.ncbi.nlm.nih.gov/42416185/)).

### Finding 2 — MDD is polygenic; GWAS identifies 102+ loci implicating synaptic/prefrontal biology

A landmark genome-wide meta-analysis of **807,553 individuals (246,363 cases, 561,190 controls)** identified **102 independent variants, 269 genes, and 15 gene-sets**, with strong enrichment for genes governing synaptic structure and neurotransmission, and for prefrontal brain regions. 87 of 102 variants replicated in an independent sample of 1,306,354 individuals. Twin-based heritability of DSM-IV MDD is estimated at **39–41%**.

> "We identified 102 independent variants, 269 genes, and 15 genesets associated with depression, including both genes and gene pathways associated with synaptic structure and neurotransmission" — [PMID: 30718901](https://pubmed.ncbi.nlm.nih.gov/30718901/)

> "An enrichment analysis provided further evidence of the importance of prefrontal brain regions" — [PMID: 30718901](https://pubmed.ncbi.nlm.nih.gov/30718901/)

> "Heritability estimates were higher for STB phenotypes (51-80%) compared to DSM-IV MDD (39-41%)" — [PMID: 40991153](https://pubmed.ncbi.nlm.nih.gov/40991153/)

This polygenic architecture means MDD has **no single causal gene**; risk is distributed across thousands of common variants of small individual effect. Cross-trait genetic analyses further show shared genetic architecture with cardiovascular disease (calcium-signaling loci: *TPCN1, CACNA2D2, CACNA1D, ATP2B1*; [PMID: 42436150](https://pubmed.ncbi.nlm.nih.gov/42436150/)), insulin resistance/metabolic conditions ([PMID: 42435748](https://pubmed.ncbi.nlm.nih.gov/42435748/)), and chronic inflammatory skin disease ([PMID: 42445668](https://pubmed.ncbi.nlm.nih.gov/42445668/)), highlighting pleiotropic neuroimmune and metabolic links.

### Finding 3 — MDD pathophysiology integrates monoamine, HPA-axis, inflammation, and neuroplasticity mechanisms

Integrated neurobiological reviews converge on a multi-system model in which **altered neurotransmission, HPA-axis abnormalities from chronic stress, inflammation, reduced neuroplasticity/neurogenesis, and large-scale network dysfunction** interact to produce depression.

> "Some possible pathophysiological mechanisms of depression include altered neurotransmission, HPA axis abnormalities involved in chronic stress, inflammation, reduced neuroplasticity, and network dysfunction" — [PMID: 28558878](https://pubmed.ncbi.nlm.nih.gov/28558878/)

Inflammation appears causally sufficient to produce depressive phenotypes: experimentally inducing a pro-inflammatory state produces "sickness behavior" resembling depression.

> "the induction of a pro-inflammatory state in healthy or medically ill subjects induces 'sickness behavior' resembling depressive symptomatology" — [PMID: 24468642](https://pubmed.ncbi.nlm.nih.gov/24468642/)

### Finding 4 — Childhood trauma is a major modifiable risk factor

A meta-analysis of early trauma and adult depression found robust dose-dependent associations across all trauma types, with emotional maltreatment strongest:

| Trauma type | Odds ratio for adult depression |
|---|---|
| Emotional abuse | 2.78 |
| Neglect | 2.75 |
| Sexual abuse | 2.42 |
| Domestic violence | 2.06 |
| Physical abuse | 1.98 |

> "Emotional abuse showed the strongest association with depression (OR=2.78) followed by neglect (OR=2.75) and sexual abuse (OR=2.42)" — [PMID: 26078093](https://pubmed.ncbi.nlm.nih.gov/26078093/)

Childhood adversities carry a **population-attributable-risk of 40.7–61.0%** for anxiety/mood disorders ([PMID: 40541041](https://pubmed.ncbi.nlm.nih.gov/40541041/)), and childhood social disadvantage (low SES, family disruption, residential instability) increases onset risk, recurrence, and reduces remission likelihood ([PMID: 14672243](https://pubmed.ncbi.nlm.nih.gov/14672243/)).

### Finding 5 — MDD prevalence is ~2× higher in women

Prevalence of major depression is approximately **twice as high in women as in men**. Proposed mechanisms include 17β-estradiol modulation of reward circuitry and sex differences in immune response; hormonal-transition windows (puberty, postpartum, menopause) mark vulnerability.

> "with depression affecting women at twice the rate of men" — [PMID: 42382579](https://pubmed.ncbi.nlm.nih.gov/42382579/)

> "the prevalence of major depression is approximately twice as high in women compared to men" — [PMID: 42425939](https://pubmed.ncbi.nlm.nih.gov/42425939/)

### Finding 6 — Intranasal esketamine is FDA-approved for treatment-resistant depression

Esketamine (S-enantiomer of ketamine), an NMDA-receptor antagonist, was **FDA-approved in 2019** as adjunctive therapy for treatment-resistant depression (TRD). An individual-patient-data meta-analysis of 7 RCTs (1,505 patients) showed MADRS reduction at 4 weeks (mean difference −2.94, 95% CI −5.39 to −0.48; moderate certainty) and reduced relapse in continuation therapy (HR = 0.38, 0.26–0.57).

> "In 2019, the FDA and EMA approved intranasal esketamine for treatment-resistant depression (TRD)" — [PMID: 41310599](https://pubmed.ncbi.nlm.nih.gov/41310599/)

> "esketamine reduced MADRS scores at 4 weeks (mean difference (MD) = - 2.94, 95% CI [- 5.39 to - 0.48]; GRADE: moderate certainty)" — [PMID: 41310599](https://pubmed.ncbi.nlm.nih.gov/41310599/)

Roughly **one-third of depressed patients develop TRD** ([PMID: 41244961](https://pubmed.ncbi.nlm.nih.gov/41244961/)), the population motivating rapid-acting glutamatergic treatments.

### Finding 7 — MDD causes substantial excess mortality, especially from suicide

A 20-year population cohort of **126,573 depressed individuals** (1,139,073 person-years) quantified excess mortality:

| Mortality category | SMR (95% CI) |
|---|---|
| All-cause | 1.84 (1.82–1.88) |
| Natural-cause | 1.69 (1.66–1.72) |
| Unnatural-cause | 5.24 (4.97–5.51) |
| Suicide-specific | 7.92 (7.47–8.38) |
| Suicide, ages 15–34 | 12.75 (10.87–14.79) |

> "individuals with depression exhibited significantly higher all-cause (SMR=1.84 [95% CI=1.82-1.88]), natural-cause (1.69 [1.66-1.72]), and unnatural-cause (5.24 [4.97-5.51]) mortality rates than the general population" — [PMID: 39536694](https://pubmed.ncbi.nlm.nih.gov/39536694/)

> "Suicide-specific SMR was markedly elevated (7.92 [7.47-8.38]), particularly in the 15-34 year-olds (12.75 [10.87-14.79])" — [PMID: 39536694](https://pubmed.ncbi.nlm.nih.gov/39536694/)

Excess life-years-lost were 5.67 years (men) and 4.06 years (women); cardiovascular disease, respiratory disease, and cancers accounted for most natural-cause deaths.

### Finding 8 — Peripheral inflammation (CRP/IL-6) is elevated in a subset of MDD, with sex specificity and treatment relevance

A sex-stratified meta-analysis (23 studies) found elevated **CRP in depressed females** (Cohen's d = 0.19, p = 0.02) but not males (d = −0.01), and elevated **IL-6 in females** (d = 0.51, p = 0.04). Higher baseline CRP and IL-6 predicted greater symptom reduction after ECT (14 studies, n = 556), supporting inflammatory markers as prognostic/predictive biomarkers.

> "Sex-based analyses revealed elevated levels of CRP among females with depression (Cohen's d = 0.19) relative to their healthy counterparts (p = 0.02), an effect not apparent among males" — [PMID: 39089535](https://pubmed.ncbi.nlm.nih.gov/39089535/)

> "higher baseline CRP and IL-6 levels were significantly associated with greater depressive symptom reduction post-ECT" — [PMID: 39938607](https://pubmed.ncbi.nlm.nih.gov/39938607/)

Sleep disturbance in MDD correlates with pooled inflammatory markers and CRP ([PMID: 41475163](https://pubmed.ncbi.nlm.nih.gov/41475163/)).

### Finding 9 — MDD is diagnosed clinically via DSM-5 nine-symptom criteria (PHQ-9 operationalizes them)

DSM-5 MDD requires **≥5 of nine symptoms** for ≥2 weeks, at least one being depressed mood or anhedonia: (1) depressed mood, (2) anhedonia, (3) appetite/weight change, (4) sleep disturbance, (5) psychomotor agitation/retardation, (6) fatigue, (7) worthlessness/guilt, (8) concentration difficulty, (9) thoughts of death/suicidality. The **PHQ-9** operationalizes these criteria for screening and severity measurement.

> "nine depressive symptoms, including suicidality, comprising the DSM-5 diagnostic criteria for major depressive disorder (assessed using the Patient Health Questionnaire-9)" — [PMID: 37798353](https://pubmed.ncbi.nlm.nih.gov/37798353/)

Symptom presentation is heterogeneous and precipitant-dependent: different adverse life events produce distinct symptom patterns (bereavement → sadness/anhedonia/appetite loss; chronic stress → fatigue/hypersomnia).

> "The patterns of depressive symptoms associated with the nine categories of adverse life events differed significantly" — [PMID: 17898343](https://pubmed.ncbi.nlm.nih.gov/17898343/)

ICD-11 differs slightly, requiring 5 of **ten** symptoms (adding "hopelessness") and retaining separate dysthymia and mixed-episode categories ([PMID: 34964106](https://pubmed.ncbi.nlm.nih.gov/34964106/)).

### Finding 10 — Gene–environment interaction: 5-HTTLPR short allele amplifies stress-induced depression risk

The serotonin transporter (*SLC6A4*) 5-HTTLPR polymorphism moderates the stress–depression relationship: **short (S) allele carriers show a stronger association between stressful life event load and depression** than L/L homozygotes.

> "the association between SLE load and MS depression severity was stronger among those with one or two copies of the short allele of the 5-HTTLPR" — [PMID: 29683385](https://pubmed.ncbi.nlm.nih.gov/29683385/)

> "carriers of either one or two copies of the s allele had increased odds of depressive symptoms associated with stress compared to participants with the l/l genotype not exposed to stressful situations" — [PMID: 37558806](https://pubmed.ncbi.nlm.nih.gov/37558806/)

The effect operates via glucocorticoid reactivity ([PMID: 29940236](https://pubmed.ncbi.nlm.nih.gov/29940236/)) and emotion-regulation network connectivity ([PMID: 29129791](https://pubmed.ncbi.nlm.nih.gov/29129791/)). Twin analyses also show income-inequality exposure moderates genetic variance in depressive symptoms ([PMID: 42253158](https://pubmed.ncbi.nlm.nih.gov/42253158/)).

### Finding 11 — Mediterranean diet and lifestyle are candidate protective/preventive factors

An extra-virgin olive-oil-enriched **Mediterranean diet** is being tested in the PREDI-DEP RCT — the first trial designed to prevent recurrent unipolar depression. Anti-inflammatory dietary patterns (vegetables, fruits, legumes, nuts, whole grains, omega-3/PUFA) associate with lower metabolic-syndrome severity and depressive symptoms.

> "the PREDI-DEP trial is the first ongoing randomized clinical trial designed to assess the role of the Mediterranean diet in the prevention of recurrent depression" — [PMID: 30744589](https://pubmed.ncbi.nlm.nih.gov/30744589/)

Meta-umbrella reviews catalog Mediterranean diet and physical activity as protective factors across neuropsychiatric disorders, and late-life depression as a risk factor for dementia ([PMID: 33435977](https://pubmed.ncbi.nlm.nih.gov/33435977/)).

### Finding 12 — Glutamatergic neuroplasticity (AMPA–BDNF–mTOR) is a convergent mechanism of rapid-acting antidepressants

Ketamine and classical psychedelics converge on a neuroplasticity pathway in prefrontal cortex pyramidal neurons: **increased glutamate release → AMPA receptor activation → BDNF and mTOR signaling → synaptic-protein expression → synaptogenesis**.

> "ketamine and psychedelics [psilocybin, lysergic acid diethylamide (LSD), and N,N-dimethyltryptamine (DMT)] induce synaptic, structural, and functional changes, particularly in pyramidal neurons in the prefrontal cortex. These include increased glutamate release, α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid receptor (AMPAR) activation, brain-derived neurotrophic factor (BDNF) and mammalian target of rapamycin (mTOR)-mediated signaling, expression of synaptic proteins, and synaptogenesis" — [PMID: 34565579](https://pubmed.ncbi.nlm.nih.gov/34565579/)

FDA approvals of S-ketamine and brexanolone (2019) opened non-monoamine (NMDA/GABA-A) therapeutic strategies, contrasting with the slow onset of monoaminergic antidepressants ([PMID: 31991195](https://pubmed.ncbi.nlm.nih.gov/31991195/)).

### Finding 13 — MDD affects fronto-limbic circuits

Structural and functional MRI consistently implicate a distributed fronto-limbic network. In late-life depression:

> "Decreased volumes or cortical thickness in the prefrontal cortex, orbitofrontal cortex, anterior and posterior cingulate cortex, several temporal and parietal regions, hippocampus, amygdala, striatum, thalamus, and the insula were associated with LLD" — [PMID: 32544600](https://pubmed.ncbi.nlm.nih.gov/32544600/)

> "The study highlights the important role of the hippocampus and the prefrontal cortex in EO patients as part of emotion-regulation networks" — [PMID: 35421280](https://pubmed.ncbi.nlm.nih.gov/35421280/)

Late-life depression additionally shows white-matter hyperintensities and reduced integrity in fronto-striatal-limbic tracts (cingulum, corpus callosum, uncinate fasciculus), with altered default-mode-network connectivity. Postpartum depression shows overlapping structural/functional/metabolic alterations ([PMID: 40925498](https://pubmed.ncbi.nlm.nih.gov/40925498/)).

### Finding 14 — Pharmacogenomics: CYP2D6 and CYP2C19 genotypes guide antidepressant dosing (CPIC)

The Clinical Pharmacogenetics Implementation Consortium (CPIC) provides genotype-informed prescribing guidance: variation in **CYP2D6, CYP2C19, and CYP2B6** influences metabolism of SSRIs/SNRIs, affecting dosing, efficacy, and tolerability.

> "Genetic variation in CYP2D6, CYP2C19, and CYP2B6 influences the metabolism of many of these antidepressants, which may potentially affect dosing, efficacy, and tolerability" — [PMID: 37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/)

Pharmacodynamic genes are not yet clinically actionable:

> "the existing data for SLC6A4 and HTR2A, which do not support their clinical use in antidepressant prescribing" — [PMID: 37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/)

Polygenic risk scores for antidepressant response remain insufficiently predictive for routine use ([PMID: 42442668](https://pubmed.ncbi.nlm.nih.gov/42442668/)).

### Finding 15 — Epigenetic dysregulation links stress to depression

Stress-induced DNA methylation changes affect depression-associated genes **NR3C1 (glucocorticoid receptor), NR3C2, CRHR1, SLC6A4, BDNF, and FKBP5**; some changes are lasting and show transgenerational effects.

> "several genes associated with depression (NR3C1, NR3C2, CRHR1, SLC6A4, BDNF, and FKBP5)" — [PMID: 36590248](https://pubmed.ncbi.nlm.nih.gov/36590248/)

In ECT responders, changes in BDNF, ERK1, and NR3C1 mRNA correlated strongly with methylation changes:

> "changes in mRNA expression were highly correlated (R = 0.59 - 0.88) with changes in DNA methylation for multiple CpG sites in the respective genes" — [PMID: 36067540](https://pubmed.ncbi.nlm.nih.gov/36067540/)

### Finding 16 — Rodent stress models recapitulate core MDD features (anhedonia)

**Chronic unpredictable mild stress (CUMS)** is the most widely used, reliable rodent model, robustly producing anhedonia (reduced sucrose preference).

> "the CUMS protocol is a robust animal model of depression and is strongly associated with anhedonic behavior in rodents" — [PMID: 30529362](https://pubmed.ncbi.nlm.nih.gov/30529362/)

> "The prolonged exposure of rodents to unpredictable/uncontrollable mild stressors leads to a reduction in the intake of palatable liquids, behavioral despair, locomotor inhibition, anxiety-like changes, and vegetative (somatic) abnormalities" — [PMID: 35072761](https://pubmed.ncbi.nlm.nih.gov/35072761/)

**Chronic social defeat stress (CSDS)** yields separable susceptible vs resilient populations implicating BDNF/TrkB, MeCP2, and FKBP51/glucocorticoid-receptor signaling ([PMID: 35711008](https://pubmed.ncbi.nlm.nih.gov/35711008/); [PMID: 36104438](https://pubmed.ncbi.nlm.nih.gov/36104438/)). Limitations include cross-lab reproducibility, protocol heterogeneity, and incomplete capture of human cognitive/affective features.

### Finding 17 — Psychotherapy (CBT) and combined CBT + antidepressant are first-line efficacious treatments

A NICE network meta-analysis (**676 RCTs, 105,477 participants, 63 treatment classes**) found, for **more severe depression**, that combined individual CT/CBT + antidepressants was the most efficacious class vs placebo (SMD −1.18), followed by individual CT/CBT (−0.78), mirtazapine (−0.35), and SNRIs (−0.32). For less severe depression, group CT/CBT was efficacious vs treatment-as-usual (SMD −1.01).

> "efficacious classes versus pill placebo (reference treatment for this population) included combined individual CT/CBT with antidepressants [-1.18 (-2.07; -0.44)]" — [PMID: 39246718](https://pubmed.ncbi.nlm.nih.gov/39246718/)

> "group cognitive/cognitive behavioural therapy (CT/CBT) class was efficacious versus treatment as usual [TAU]" — [PMID: 39246718](https://pubmed.ncbi.nlm.nih.gov/39246718/)

Short-term psychodynamic psychotherapy is also superior to unstructured usual treatment (SMD −0.91; [PMID: 36623570](https://pubmed.ncbi.nlm.nih.gov/36623570/)).

### Finding 18 — rTMS is an effective device-based treatment for MDD/TRD

A sham-controlled meta-analysis (30 comparisons, N = 1,850) found active prefrontal rTMS reduced depressive symptoms vs sham (**Hedges' g = −1.056**, 95% CI −1.407 to −0.704, p < 0.001).

> "Active rTMS reduced depressive symptoms versus sham (Hedges' g = -1.056, 95% CI -1.407 to -0.704; p < 0.001)" — [PMID: 41997374](https://pubmed.ncbi.nlm.nih.gov/41997374/)

In youth (16 studies, 1,295 patients aged 10–25): response RR 1.24, remission RR 1.63 (NNT ≈ 10).

> "Pooled RR was 1.24 (95% CI = 1.06-1.45) for response rate and 1.63 (95% CI = 1.11-2.39) for remission rate (with an associated number needed to treat of 10)" — [PMID: 41137879](https://pubmed.ncbi.nlm.nih.gov/41137879/)

A large NMA (141 trials, 10,587 participants) ranked theta-burst stimulation (TBS) most efficacious among modalities ([PMID: 42383744](https://pubmed.ncbi.nlm.nih.gov/42383744/)).

### Finding 19 — MDD is common (~5–6% of adults), first onsets in adolescence/early adulthood, and is recurrent/episodic

Depression affects **approximately 5.7% of adults worldwide**; around one-third develop TRD.

> "Depression affects approximately 5.7% of adults worldwide, and around one-third of these individuals develop treatment-resistant depression (TRD)" — [PMID: 41244961](https://pubmed.ncbi.nlm.nih.gov/41244961/)

WHO World Mental Health surveys (156,331 respondents, 29 countries) show mood disorders commonly first onset in adolescence/young adulthood, with median age of onset of any mental disorder ~19–20 years and MDD among the two most prevalent disorders in both sexes ([PMID: 37531964](https://pubmed.ncbi.nlm.nih.gov/37531964/)). Childhood adversities carry population-attributable-risk of 40.7–61.0% for mood disorders.

> "Population attributable risk proportions of 12-month disorders associated with CAs were in the range of 40.7-61.0 % for anxiety and mood disorders" — [PMID: 40541041](https://pubmed.ncbi.nlm.nih.gov/40541041/)

---

## Report by Requested Domain

### 1. Disease Information

MDD is a common mood disorder characterized by persistent depressed mood and/or loss of interest/pleasure (anhedonia) with associated neurovegetative, cognitive, and psychomotor symptoms lasting ≥2 weeks and causing clinically significant distress or impairment. Key identifiers and synonyms:

| Field | Value |
|---|---|
| **MONDO** | MONDO:0002050 (major depressive disorder); MONDO:0002009 (depressive disorder) |
| **ICD-10** | F32 (single episode), F33 (recurrent) |
| **ICD-11** | 6A70 (single episode depressive disorder), 6A71 (recurrent depressive disorder) |
| **MeSH** | D003865 (Depressive Disorder, Major) |
| **OMIM** | 608516 (MDD susceptibility) |
| **Synonyms** | Major depression, unipolar depression, clinical depression, major depressive episode, unipolar major depression |

Information is derived predominantly from **aggregated disease-level resources** (GWAS consortia, GBD, meta-analyses, national registries) plus individual patient / EHR-derived cohort studies (e.g., Finnish/Swedish registers, [PMID: 41536102](https://pubmed.ncbi.nlm.nih.gov/41536102/)).

### 2. Etiology

**Causal factors:** MDD is multifactorial and polygenic (Findings 2, 3). There is **no infectious cause**, though inflammation contributes mechanistically (Finding 3). **Genetic risk factors:** 102+ common susceptibility loci, heritability 39–41%; no single causal gene. **Environmental risk factors:** childhood trauma (OR 1.98–2.78, Finding 4), stressful life events, female sex (~2× risk, Finding 5), low SES/family disruption, childhood income inequality, sleep disturbance. **Protective factors:** Mediterranean/anti-inflammatory diet, physical activity, education (Finding 11; [PMID: 33435977](https://pubmed.ncbi.nlm.nih.gov/33435977/)); neurobiological resilience factors (greater prefrontal volume/activity, [PMID: 40520971](https://pubmed.ncbi.nlm.nih.gov/40520971/)). **Gene–environment interactions:** 5-HTTLPR × stress (Finding 10); polygenic risk × income inequality (Finding 10).

### 3. Phenotypes

Core phenotypes map to the DSM-5 nine symptoms (Finding 9). Suggested HPO terms:

| Phenotype (type) | HPO term | Frequency/characteristics |
|---|---|---|
| Depressed mood (behavioral) | HP:0000716 (Depressivity) | Core; required |
| Anhedonia (behavioral) | HP:0100754 (Anhedonia) | Core; required |
| Insomnia / sleep disturbance | HP:0100785 (Insomnia) | Very common; links to inflammation |
| Fatigue | HP:0012378 (Fatigue) | Common |
| Appetite/weight change | HP:0004396 (Poor appetite) | Common |
| Poor concentration | HP:0000736 (Short attention span) | Common |
| Suicidal ideation | HP:0031589 (Suicidal ideation) | High-risk; drives mortality |
| Psychomotor retardation/agitation | HP:0025059 / HP:0000733 | Variable |

**Onset:** adolescent/adult (median ~19–20 y). **Severity:** mild to severe, variable. **Progression:** episodic/recurrent/fluctuating. **Quality of life:** even minor depression produces significant functional impairment in daily activities, feelings, pain, and social function ([PMID: 7804493](https://pubmed.ncbi.nlm.nih.gov/7804493/)).

### 4. Genetic/Molecular Information

No monogenic cause; **polygenic** (Finding 2). Implicated genes/pathways: synaptic structure and neurotransmission genes, prefrontal-enriched loci; candidate/mechanistic genes *SLC6A4, BDNF, FKBP5, NR3C1, NR3C2, CRHR1, HTR2A, COMT, MTHFR, SGK1* ([PMID: 32849818](https://pubmed.ncbi.nlm.nih.gov/32849818/)); pleiotropic loci *FADS1-2-3* (PUFA metabolism, [PMID: 42309192](https://pubmed.ncbi.nlm.nih.gov/42309192/)), calcium-channel genes, and MHC/histone genes ([PMID: 42320287](https://pubmed.ncbi.nlm.nih.gov/42320287/)). Variants are **germline**, common, low-effect (not classified pathogenic/likely-pathogenic under ACMG — this is a complex trait, not a Mendelian disorder). **Epigenetics:** methylation of NR3C1/BDNF/FKBP5/SLC6A4 (Finding 15). No characteristic chromosomal abnormalities.

### 5. Environmental Information

Non-genetic contributors: psychosocial stress, childhood maltreatment, low SES, income inequality, sleep disruption. Lifestyle: physical inactivity, poor diet (protective: Mediterranean diet, exercise; Finding 11). No infectious agent causes MDD, though inflammatory/immune activation is mechanistically implicated (Findings 3, 8) and comorbid inflammatory diseases share genetic liability ([PMID: 42445668](https://pubmed.ncbi.nlm.nih.gov/42445668/)).

### 6. Mechanism / Pathophysiology

See Mechanistic Model below. Key pathways: monoaminergic (5-HT/NE/DA); glutamatergic AMPA–BDNF–mTOR neuroplasticity (Finding 12; GO:0048167 regulation of synaptic plasticity, GO:0007268 chemical synaptic transmission); HPA-axis/glucocorticoid signaling (Finding 15; GO:0051384 response to glucocorticoid); neuroinflammation (Finding 8; GO:0006954 inflammatory response); impaired hippocampal neurogenesis (GO:0021766). Cell types: pyramidal neurons (CL:0000598), astrocytes (CL:0000127), microglia (CL:0000129), oligodendrocytes (CL:0000128) — single-cell eQTL work implicates cell-type-specific genes ZSCAN31 (astrocytes/endothelial), BTN3A2 (microglia), YLPM1 (oligodendrocytes) ([PMID: 42372879](https://pubmed.ncbi.nlm.nih.gov/42372879/)). Subcellular: mitochondria (GO:0005739; energy metabolism), synapse (GO:0045202). CHEBI-relevant chemical entities: serotonin (CHEBI:28790), cortisol (CHEBI:17650), glutamate (CHEBI:14321), BDNF signaling.

### 7. Anatomical Structures Affected

Primary organ: **brain** (UBERON:0000955), nervous system. Key regions: prefrontal cortex (UBERON:0000451), orbitofrontal cortex, anterior/posterior cingulate cortex (UBERON:0002715), hippocampus (UBERON:0002421), amygdala (UBERON:0001876), striatum (UBERON:0002435), thalamus (UBERON:0001897), insula (UBERON:0002690) — Finding 13. White-matter tracts: cingulum, corpus callosum, uncinate fasciculus. Involvement is typically **bilateral**. Secondary systems: cardiovascular, endocrine (HPA), immune.

### 8. Temporal Development

Onset typically adolescence/young adulthood (median ~19–20 y), insidious. Course is **episodic/recurrent/relapsing-remitting**; early-onset cases have higher recurrence risk. Remission may be spontaneous or treatment-induced; ~one-third become treatment-resistant. Chronic and lifelong in many. Adolescence (10–24 y) is a critical vulnerability window (Findings 1, 19).

### 9. Inheritance and Population

**Prevalence** ~5.7% of adults (Finding 19). **Inheritance:** multifactorial/polygenic, heritability 39–41% (Finding 2); no Mendelian pattern, penetrance, anticipation, founder effects, or carrier frequency applicable. **Demographics:** female:male ≈ 2:1 (Finding 5); rising burden in youth; higher middle-age/older-adult burden in some regions ([PMID: 42416185](https://pubmed.ncbi.nlm.nih.gov/42416185/)).

### 10. Diagnostics

Diagnosis is **clinical** via DSM-5/ICD-11 criteria (Finding 9), aided by structured tools (PHQ-9, MADRS, CDRS-R in youth). No diagnostic laboratory/genetic test exists. Emerging biomarkers: CRP/IL-6 (prognostic/predictive, Finding 8); neuroimaging (structural/functional MRI, Finding 13) is research-grade. Pharmacogenomic testing (CYP2D6/CYP2C19) informs treatment, not diagnosis (Finding 14). Differential diagnosis: bipolar depression, persistent depressive disorder/dysthymia, adjustment disorder, normal grief, hypothyroidism, substance-induced mood disorder.

### 11. Outcome/Prognosis

Excess mortality: all-cause SMR 1.84, suicide SMR 7.9 (Finding 7); 4–5.7 excess life-years lost. High morbidity/disability (leading YLD cause, Finding 1). Prognostic factors: severity, comorbidity, early onset, treatment response; inflammatory markers predict ECT response (Finding 8). Real-world RCT-ineligible patients (comorbid) have >2× worse outcomes ([PMID: 41536102](https://pubmed.ncbi.nlm.nih.gov/41536102/)). Late-life depression predicts dementia/AD ([PMID: 42134046](https://pubmed.ncbi.nlm.nih.gov/42134046/)).

### 12. Treatment

| Modality | Examples | Evidence | MAXO suggestion |
|---|---|---|---|
| Psychotherapy | CBT, group CBT, STPP | SMD −0.78 to −1.01 (Finding 17) | MAXO:0000804 (psychotherapy) |
| Pharmacotherapy | SSRIs, SNRIs, mirtazapine | SMD −0.32 to −0.35 (Finding 17) | MAXO:0001008 (pharmacotherapy) |
| Combined | CBT + antidepressant | SMD −1.18 (most efficacious, severe) | — |
| Neuromodulation | rTMS, TBS, ECT | rTMS g = −1.06 (Finding 18) | MAXO:0000823 (TMS) |
| Rapid-acting | Intranasal esketamine (TRD) | MADRS MD −2.94 (Finding 6) | MAXO:0000058 (drug therapy) |

**Pharmacogenomics:** CYP2D6/CYP2C19 genotype-guided dosing (Finding 14). In youth, fluoxetine/escitalopram/sertraline preferred; suicidality monitoring essential ([PMID: 34029378](https://pubmed.ncbi.nlm.nih.gov/34029378/)).

### 13. Prevention

**Primary:** risk-factor modification, Mediterranean diet (PREDI-DEP), physical activity, childhood-adversity reduction (Finding 11). **Secondary:** PHQ-9 screening, early intervention. **Tertiary:** relapse prevention (maintenance antidepressants, continuation esketamine HR 0.38). Behavioral: exercise, diet, sleep hygiene. No immunization applicable.

### 14. Other Species / Natural Disease

Depression-like states are studied in rodents (*Mus musculus*, NCBI:txid10090; *Rattus norvegicus*, NCBI:txid10116) via induced models (Finding 16). Orthologous genes conserved: *Bdnf, Slc6a4, Fkbp5, Nr3c1*. Naturally occurring analogues (e.g., separation-related/anhedonic states in companion animals) exist but are not well characterized; no strong zoonotic or breed-specific associations apply.

### 15. Model Organisms

Predominantly **mammalian induced models**: CUMS and CSDS in mice/rats recapitulate anhedonia, behavioral despair, and vegetative changes (Finding 16). Genetic models: BDNF Val66Met knock-in, FKBP5 manipulation, MeCP2 overexpression. **Recapitulation:** strong for anhedonia and stress-susceptibility/resilience; **limitations:** poor capture of human subjective/cognitive symptoms, cross-lab reproducibility, protocol heterogeneity. Resources: MGI, RGD, IMPC.

---

## Mechanistic Model / Interpretation

MDD is best understood as a **diathesis–stress disorder** in which polygenic genetic liability and early-life/ongoing environmental stress converge on shared neurobiological substrates:

```
   GENETIC LIABILITY (polygenic, 102+ loci,        ENVIRONMENTAL STRESS
   heritability ~39-41%; SLC6A4, BDNF, FKBP5,       (childhood trauma OR 1.98-2.78,
   NR3C1, FADS1, synaptic/prefrontal genes)          stressful life events, low SES)
            |                                                 |
            +---------------->  GENE x ENVIRONMENT  <---------+
                          (5-HTTLPR-S x stress; epigenetic
                           methylation of NR3C1/BDNF/FKBP5)
                                       |
              +------------------------+------------------------+
              v                        v                        v
     HPA-AXIS DYSREGULATION     NEUROINFLAMMATION         MONOAMINE DEFICIT
     (^cortisol, v GR function,  (^CRP, ^IL-6;             (v 5-HT/NE/DA
      FKBP5, SGK1)               "sickness behavior";       signaling)
              |                   sex-specific, female)          |
              +------------------------+------------------------+
                                       v
                    IMPAIRED GLUTAMATERGIC NEUROPLASTICITY
                    (v AMPA-BDNF-mTOR signaling, v synaptogenesis,
                     v hippocampal neurogenesis)
                                       |
                                       v
                   FRONTO-LIMBIC CIRCUIT DYSFUNCTION
        (PFC, hippocampus, amygdala, cingulate, striatum; v volume,
         altered connectivity, default-mode-network dysregulation)
                                       |
                                       v
          CLINICAL DEPRESSION (DSM-5: depressed mood/anhedonia +
          >=5 symptoms >=2 weeks) -> disability, excess mortality (suicide)
```

**Upstream** drivers are genetic liability, early-life stress, and their epigenetic embedding. **Midstream** are the four interacting biological systems (HPA, inflammation, monoamines, neuroplasticity). **Downstream** is fronto-limbic circuit dysfunction producing the clinical syndrome. Critically, the **treatment landscape maps onto this model**: SSRIs/SNRIs target monoamines (slow onset); esketamine and psychedelics target the glutamate–AMPA–BDNF–mTOR neuroplasticity node (rapid onset); anti-inflammatory strategies and ECT-response biomarkers target inflammation; and psychotherapy/rTMS act on fronto-limbic circuit function. This explains why combined biological + psychological treatment is most efficacious for severe disease.

---

## Evidence Base

| PMID | Contribution | Supports finding |
|---|---|---|
| [30718901](https://pubmed.ncbi.nlm.nih.gov/30718901/) | 102-loci GWAS meta-analysis; synaptic/prefrontal enrichment | F2 (core genetics) |
| [28558878](https://pubmed.ncbi.nlm.nih.gov/28558878/) | Integrated neurobiology review | F3 (mechanism) |
| [24468642](https://pubmed.ncbi.nlm.nih.gov/24468642/) | Inflammation → sickness behavior | F3, F8 |
| [26078093](https://pubmed.ncbi.nlm.nih.gov/26078093/) | Childhood-trauma meta-analysis (ORs) | F4 |
| [39536694](https://pubmed.ncbi.nlm.nih.gov/39536694/) | 126,573-person mortality cohort | F7 |
| [39089535](https://pubmed.ncbi.nlm.nih.gov/39089535/) | Sex-specific inflammation | F8 |
| [39938607](https://pubmed.ncbi.nlm.nih.gov/39938607/) | CRP/IL-6 predict ECT response | F8 |
| [29683385](https://pubmed.ncbi.nlm.nih.gov/29683385/) / [37558806](https://pubmed.ncbi.nlm.nih.gov/37558806/) | 5-HTTLPR × stress GxE | F10 |
| [34565579](https://pubmed.ncbi.nlm.nih.gov/34565579/) | AMPA-BDNF-mTOR neuroplasticity | F12 |
| [32544600](https://pubmed.ncbi.nlm.nih.gov/32544600/) / [35421280](https://pubmed.ncbi.nlm.nih.gov/35421280/) | Fronto-limbic neuroimaging | F13 |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | CPIC pharmacogenomics | F14 |
| [36590248](https://pubmed.ncbi.nlm.nih.gov/36590248/) / [36067540](https://pubmed.ncbi.nlm.nih.gov/36067540/) | Epigenetic methylation | F15 |
| [30529362](https://pubmed.ncbi.nlm.nih.gov/30529362/) / [35072761](https://pubmed.ncbi.nlm.nih.gov/35072761/) | CUMS rodent model | F16 |
| [39246718](https://pubmed.ncbi.nlm.nih.gov/39246718/) | NICE NMA (676 RCTs) treatment | F17 |
| [41997374](https://pubmed.ncbi.nlm.nih.gov/41997374/) / [41137879](https://pubmed.ncbi.nlm.nih.gov/41137879/) | rTMS efficacy | F18 |
| [41310599](https://pubmed.ncbi.nlm.nih.gov/41310599/) | Esketamine IPD meta-analysis | F6 |
| [42269957](https://pubmed.ncbi.nlm.nih.gov/42269957/) / [42167272](https://pubmed.ncbi.nlm.nih.gov/42167272/) | GBD burden | F1 |
| [41244961](https://pubmed.ncbi.nlm.nih.gov/41244961/) / [37531964](https://pubmed.ncbi.nlm.nih.gov/37531964/) | Prevalence, age-of-onset | F19 |

Evidence types span **human clinical** (GWAS, cohorts, RCTs, meta-analyses — the majority), **model organism** (CUMS/CSDS rodents), and **in vitro/computational** (single-cell eQTL, colocalization). The convergence of independent evidence streams (genetics, imaging, biomarkers, treatment mechanism) on a shared multi-system model strengthens confidence.

---

## Limitations and Knowledge Gaps

1. **Heterogeneity.** MDD is diagnostically heterogeneous; the same DSM-5 label captures biologically distinct subtypes (e.g., inflammatory vs non-inflammatory, melancholic vs atypical). Group-level effect sizes obscure individual variation.
2. **Genetic architecture incompletely resolved.** GWAS explains only a fraction of heritability; effector genes at most loci and their functional mechanisms remain uncertain (e.g., FADS1-2-3 pleiotropy).
3. **Biomarkers not diagnostic.** CRP/IL-6 and neuroimaging findings are group-level and not yet clinically actionable for individual diagnosis or treatment selection.
4. **Pharmacogenomics limited.** Only CYP2D6/CYP2C19 are clinically actionable; polygenic response scores lack predictive performance, especially in non-European ancestries.
5. **Ancestry bias.** Most genetic and biomarker data derive from European-ancestry samples, limiting generalizability.
6. **Model organism validity gap.** Rodent models capture anhedonia/stress-susceptibility well but poorly model human subjective/cognitive symptoms.
7. **RCT generalizability.** ~one-third of real-world MDD patients would be RCT-ineligible and have substantially worse outcomes, so guideline evidence may not reflect typical patients.
8. **Causality.** Much evidence is observational/correlational; directionality (e.g., inflammation ↔ depression, sleep ↔ inflammation) is often bidirectional or unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **Biologically-stratified trials.** Prospectively test anti-inflammatory augmentation in the CRP/IL-6-high, female-predominant inflammatory subtype (Finding 8), using baseline inflammatory markers as inclusion criteria and treatment-response predictors.
2. **Ancestry diversification.** Expand GWAS and pharmacogenomic studies into non-European populations to improve polygenic-risk-score portability and equity.
3. **Effector-gene functional validation.** Use single-cell eQTL/CRISPR screens to resolve causal genes at ambiguous loci (FADS1-2-3, calcium-channel, MHC/histone loci) and their cell-type-specific mechanisms.
4. **Prevention trial readouts.** Complete PREDI-DEP and similar dietary/lifestyle RCTs to establish causal preventive efficacy of the Mediterranean/anti-inflammatory diet.
5. **Neuroplasticity biomarker development.** Validate BDNF/mTOR-pathway and neuroimaging markers as predictors of rapid-acting (esketamine/psychedelic) treatment response.
6. **Comparative-effectiveness of neuromodulation.** Conduct high-quality head-to-head rTMS-modality trials (TBS vs accelerated vs deep TMS) to confirm probabilistic NMA rankings.
7. **Real-world evidence integration.** Combine registry/EHR data with RCT evidence to build treatment guidelines generalizable to comorbid, RCT-ineligible patients.
8. **Deep phenotyping for subtypes.** Integrate multi-omics + longitudinal symptom trajectories to define reproducible, treatment-relevant MDD subtypes.

---

*Report compiled from 19 confirmed findings across 83 reviewed papers over 5 investigation iterations. Evidence prioritizes primary literature with verified abstract quotations; ontology suggestions (MONDO, HPO, GO, CL, UBERON, CHEBI, MAXO) are provided throughout for knowledge-base integration.*


## Artifacts

- [OpenScientist final report](Major_Depressive_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Major_Depressive_Disorder-deep-research-openscientist_artifacts/final_report.pdf)
