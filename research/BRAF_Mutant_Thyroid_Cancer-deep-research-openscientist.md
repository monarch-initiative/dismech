---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T19:32:46.808074'
end_time: '2026-05-05T20:23:11.811033'
duration_seconds: 3025.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRAF-Mutant Papillary Thyroid Cancer
  mondo_id: ''
  category: ''
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
citation_count: 80
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRAF-Mutant Papillary Thyroid Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF-Mutant Papillary Thyroid Cancer** covering all of the
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

# Comprehensive Disease Characterization: BRAF-Mutant Papillary Thyroid Cancer

---

## Summary

BRAF-mutant papillary thyroid cancer (PTC) is the most prevalent molecular subtype of thyroid cancer, defined by the somatic BRAF V600E missense mutation (c.1799T>A, p.Val600Glu) that constitutively activates the MAPK/ERK signaling cascade. Present in 40–80% of all PTC cases—with TCGA data showing 48.4% of 496 PTC samples harboring BRAF mutations, 97.9% of which are V600E—this single nucleotide variant serves as both an oncogenic driver and a clinically actionable biomarker. The mutation suppresses thyroid differentiation genes, most critically the sodium-iodide symporter (NIS/SLC5A5), leading to radioactive iodine (RAI) refractoriness in up to 60% of BRAF-mutant PTC. Co-occurrence with TERT promoter mutations synergistically elevates the risk of RAI refractoriness (OR=4.8), lymph node metastasis, and recurrence, and represents a critical step in the dedifferentiation cascade toward anaplastic thyroid carcinoma (ATC).

Despite its association with more aggressive clinicopathological features—including increased lymph node metastasis (meta-analytic OR=1.38, 95% CI 1.17–1.61) and borderline increased recurrence risk (OR=1.56, 95% CI 1.00–2.41)—the overall prognosis of BRAF-mutant PTC remains excellent (10-year disease-specific survival ~97.2%), particularly for localized disease. The treatment landscape has been transformed by precision medicine approaches: BRAF/MEK inhibitor redifferentiation therapy with dabrafenib-trametinib restores RAI uptake from 5% to 95% of lesions in refractory patients; multikinase inhibitors (lenvatinib, sorafenib, cabozantinib) extend progression-free survival in advanced disease; and immunotherapy combined with targeted therapy achieves remarkable response rates in BRAF V600E-mutant ATC. Active surveillance has been validated as safe for low-risk papillary thyroid microcarcinoma (PTMC), with over 30 years of follow-up data showing zero thyroid-cancer-related deaths. The 2025 ATA guidelines have substantially reclassified low-risk patients toward excellent response categories, supporting de-escalation of care where appropriate.

This report synthesizes evidence from 182 publications, 17 confirmed findings, and multi-omic analyses spanning genomics, transcriptomics, proteomics, epigenomics, and single-cell RNA sequencing to provide a comprehensive disease characterization covering all 15 major disease knowledge domains.

---

## 1. Disease Information

### Overview

BRAF-mutant papillary thyroid cancer is a molecular subtype of papillary thyroid carcinoma (PTC) defined by the presence of activating mutations in the BRAF serine/threonine kinase gene, most commonly the V600E hotspot mutation. PTC itself accounts for 85–90% of all thyroid malignancies, making it the most common endocrine cancer worldwide ([PMID: 40980146](https://pubmed.ncbi.nlm.nih.gov/40980146/)). The BRAF V600E mutation occurs as a somatic (acquired) event in thyroid follicular cells and results in constitutive activation of the MAPK signaling pathway independent of upstream receptor tyrosine kinase stimulation.

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **ICD-10** | C73 (Malignant neoplasm of thyroid gland) |
| **ICD-11** | 2D10.0 (Papillary adenocarcinoma of thyroid gland) |
| **ICD-O-3 Morphology** | 8260/3 (Papillary adenocarcinoma, NOS) |
| **MeSH** | D000077273 (Papillary Thyroid Cancer); D020032 (Proto-Oncogene Proteins B-raf) |
| **MONDO** | MONDO:0005031 (Thyroid gland papillary carcinoma) |
| **OMIM** | 164757 (BRAF gene); 188550 (Thyroid carcinoma, papillary) |
| **COSMIC** | COSM476 (BRAF p.V600E) |
| **Orphanet** | ORPHA:146 (Papillary thyroid carcinoma) |

### Synonyms and Alternative Names

- BRAF V600E-positive papillary thyroid carcinoma
- BRAF-like PTC (TCGA molecular classification)
- BRAF-mutated differentiated thyroid cancer (DTC)
- Papillary thyroid cancer, classic variant (most commonly BRAF V600E-driven)
- PTC with BRAF V600E mutation

### Information Sources

This characterization integrates aggregated disease-level resources (TCGA, COSMIC, GBD, SEER) with findings from individual patient cohorts, clinical trials, meta-analyses, and single-cell transcriptomic studies. The evidence base spans human clinical data, model organism studies, in vitro experiments, and computational analyses.

---

## 2. Etiology

### Disease Causal Factors

The primary causal event in BRAF-mutant PTC is the somatic acquisition of the BRAF V600E mutation (chr7:140453136 A>T, GRCh37) in thyroid follicular epithelial cells. This missense mutation substitutes valine with glutamic acid at position 600 in the activation segment of the BRAF kinase domain, mimicking phosphorylation and locking the kinase in a constitutively active conformation. This results in continuous signaling through the RAS-RAF-MEK-ERK pathway, driving uncontrolled cell proliferation and survival ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/)).

The BRAF V600E mutation is classified as a Class I BRAF mutation—a point mutation that activates BRAF as a monomer, independent of RAS signaling or dimerization ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/)). This distinguishes it from Class II (in-frame insertions/deletions) and Class III (gene fusions) BRAF alterations.

### Risk Factors

**Genetic Risk Factors:**

- **BRAF V600E somatic mutation**: The defining oncogenic driver, present in 40–80% of PTC across studies. A 2025 single-institution study found 78.7% of 301 PTC patients harbored BRAF V600E ([PMID: 40237893](https://pubmed.ncbi.nlm.nih.gov/40237893/)). Among TCGA PTC samples, 48.4% (240/496) had BRAF mutations, with V600E comprising 97.9% (235/240).
- **GWAS susceptibility loci**: Multiple genome-wide association studies have identified DTC risk loci that may modify BRAF-mutant PTC susceptibility:
  - **9q22.33 (FOXE1)**: rs965513, OR=1.7 per A allele (95% CI 1.2–2.3) ([PMID: 25879635](https://pubmed.ncbi.nlm.nih.gov/25879635/))
  - **14q13.3 (NKX2-1)**: rs944289, OR=1.6 per A allele (95% CI 1.2–2.1) ([PMID: 25879635](https://pubmed.ncbi.nlm.nih.gov/25879635/))
  - **2q35 (DIRC3)**: Confirmed across multiple populations ([PMID: 23894154](https://pubmed.ncbi.nlm.nih.gov/23894154/))
  - **8p12 (NRG1)**: rs6996585, P=1.08×10⁻⁸ in Korean GWAS ([PMID: 28703219](https://pubmed.ncbi.nlm.nih.gov/28703219/))
  - **BATF and DHX35**: rs10136427 (OR=1.30) and rs7267944 (OR=1.32) in Italian populations ([PMID: 25029422](https://pubmed.ncbi.nlm.nih.gov/25029422/))
- **TERT promoter co-mutation**: Synergistically worsens prognosis (see Section 4)

**Environmental Risk Factors:**

- **Ionizing radiation exposure**: The most well-established environmental risk factor for DTC. A study of indigenous populations near the former Semipalatinsk Nuclear Test Site found BRAF V600E exclusively in papillary carcinoma samples among radiation-exposed individuals ([PMID: 41370693](https://pubmed.ncbi.nlm.nih.gov/41370693/)).
- **Iodine intake**: Dose-response meta-analysis of 25 studies (54,621 participants) revealed a U-shaped nonlinear relationship between urinary iodine concentration and thyroid nodule risk (P for nonlinearity <0.001), with increased risks at both deficient and excessive iodine levels ([PMID: 41675569](https://pubmed.ncbi.nlm.nih.gov/41675569/)).
- **Volcanic area residence**: Exposure to volcanic emissions (gas, ash, lava) contaminates food chains with toxic compounds ([PMID: 30104523](https://pubmed.ncbi.nlm.nih.gov/30104523/)).
- **Obesity/metabolic dysfunction**: NAFLD (non-alcoholic fatty liver disease) is an independent risk factor for lymph node metastasis in PTC (OR=1.285, 95% CI 1.052–1.570) and is associated with higher incidence of BRAF V600E mutation ([PMID: 36696026](https://pubmed.ncbi.nlm.nih.gov/36696026/)).
- **Sex**: Female predominance (2–4:1 female-to-male ratio), with women accounting for 67% of all thyroid cancer cases globally ([PMID: 41726144](https://pubmed.ncbi.nlm.nih.gov/41726144/)).
- **Age**: Mean age at diagnosis 40–45 years for PTC ([PMID: 23014067](https://pubmed.ncbi.nlm.nih.gov/23014067/)).

### Protective Factors

- **Adequate iodine intake**: More-than-adequate iodine showed a trend toward lower thyroid nodule prevalence ([PMID: 41675569](https://pubmed.ncbi.nlm.nih.gov/41675569/)).
- **Iodine prophylaxis legislation**: Adoption of iodine prophylaxis programs improved thyroid cancer epidemiological outcomes in subsequent generations ([PMID: 41370693](https://pubmed.ncbi.nlm.nih.gov/41370693/)).

### Gene–Environment Interactions

The shift in PTC oncogenic patterns over recent decades—from RET/PTC rearrangements to BRAF V600E dominance—suggests changing environmental exposures interact with genetic susceptibility. Radiation exposure correlates with RET/PTC rearrangements, while the increasing BRAF V600E prevalence may reflect different environmental carcinogens or detection biases ([PMID: 23014067](https://pubmed.ncbi.nlm.nih.gov/23014067/)).

---

## 3. Phenotypes

### Clinical Presentation

| Phenotype | HPO Term | Frequency | Severity | Onset |
|-----------|----------|-----------|----------|-------|
| Thyroid nodule | HP:0002890 | >95% | Variable | Adult |
| Cervical lymphadenopathy | HP:0002716 | 30–80% | Variable | Adult |
| Neck swelling | HP:0025164 | 56% | Mild–Moderate | Adult |
| Palpable neck mass | HP:0100548 | 49% | Variable | Adult |
| Hoarseness/Dysphonia | HP:0001609 | 5–15% | Mild–Severe | Adult |
| Dysphagia | HP:0002015 | 5–10% | Mild–Moderate | Adult |
| Elevated serum thyroglobulin | HP:0031508 | 60–80% | Variable | Adult |
| Microcalcifications on ultrasound | — | 47.7% | — | Adult |
| Hypoechogenicity on ultrasound | — | 39.0% | — | Adult |

**BRAF V600E-specific associations** ([PMID: 40237893](https://pubmed.ncbi.nlm.nih.gov/40237893/)):
- Classic PTC morphology: 88% of classic subtype PTCs express BRAF V600E
- Tall cell variant: 100% express BRAF V600E (most aggressive histological subtype)
- Follicular variant: Only 38% express BRAF V600E
- Association with infiltrative borders, extrathyroidal extension, and intraglandular tumor spread ([PMID: 26271724](https://pubmed.ncbi.nlm.nih.gov/26271724/))

### Quality of Life Impact

HRQOL meta-analysis of PTMC treatments found uncomplicated QALY weights ranging from 0.975 to 0.992, with no significant difference between active surveillance, thermal ablation, and surgery (P=.15) ([PMID: 41452620](https://pubmed.ncbi.nlm.nih.gov/41452620/)). Patient treatment preferences are driven by aversion to treatment complications rather than to the treatments themselves ([PMID: 41006152](https://pubmed.ncbi.nlm.nih.gov/41006152/)). Post-thyroidectomy patients report challenges in sensory function, body satisfaction, eating, speaking, and social interactions ([PMID: 38384638](https://pubmed.ncbi.nlm.nih.gov/38384638/)). Thyroid cancer survivors report significant unmet informational, psychological, emotional, and practical support needs, often influenced by the "good cancer" label ([PMID: 40402541](https://pubmed.ncbi.nlm.nih.gov/40402541/)).

---

## 4. Genetic/Molecular Information

### Causal Gene: BRAF

| Feature | Detail |
|---------|--------|
| **Gene** | BRAF (v-Raf murine sarcoma viral oncogene homolog B) |
| **HGNC ID** | HGNC:1097 |
| **OMIM** | 164757 |
| **Chromosomal location** | 7q34 |
| **UniProt** | P15056 |
| **COSMIC ID** | COSM476 (V600E) |

### Pathogenic Variants

**BRAF V600E (c.1799T>A, p.Val600Glu)**:
- **Variant type**: Missense (Class I BRAF mutation)
- **Somatic origin**: Acquired in thyroid follicular cells; not inherited
- **Frequency in PTC**: 40–80% across studies; TCGA: 48.4% (240/496 samples)
- **Functional consequence**: Gain-of-function; constitutive kinase activation (~500-fold increased activity)
- **ACMG classification**: Pathogenic (somatic oncogenic variant)
- **Population frequency**: Extremely rare as germline variant in gnomAD; functionally exclusive to somatic tumors

**Rare non-V600E BRAF variants in PTC** (TCGA data):
- K601E (n=1), N581_A598dup (n=1), K591_A598dup (n=1), P490_Q494del (n=1), T488_P492del (n=1)
- Mutation types: 236 missense, 2 in-frame insertions, 2 in-frame deletions

### Co-occurring Mutations and Modifier Genes

**TERT promoter mutations** (C228T, C250T):
- Found in 38.2% of DTC patients harboring BRAF V600E ([PMID: 40988283](https://pubmed.ncbi.nlm.nih.gov/40988283/))
- Coexisting BRAF V600E + TERT independently elevates risk of loss of RAI avidity (OR=4.8, P=.009) and accelerates recurrence ([PMID: 40988283](https://pubmed.ncbi.nlm.nih.gov/40988283/))
- TERT is an independent predictor of lateral lymph node metastasis (OR=2.272, 95% CI 1.078–4.786) ([PMID: 40184730](https://pubmed.ncbi.nlm.nih.gov/40184730/))

**TP53 mutations**: Observed in the ATC component during dedifferentiation from PTC; not typically found in well-differentiated PTC ([PMID: 40887557](https://pubmed.ncbi.nlm.nih.gov/40887557/))

**Additional co-occurring alterations**: DICER1 (7%), PTEN (6%), RET (4%) in multifocal PTC ([PMID: 40235071](https://pubmed.ncbi.nlm.nih.gov/40235071/))

### Epigenetic Information

- **Promoter methylation**: BRAF V600E correlates with methylation of TIMP3, CDH13, RASSF1A, and RARB tumor suppressor genes ([PMID: 31006665](https://pubmed.ncbi.nlm.nih.gov/31006665/))
- **miRNA dysregulation**: miR-146b, miR-221/222, and miR-375 are upregulated in BRAF V600E PTC and associated with aggressive behavior ([PMID: 41660935](https://pubmed.ncbi.nlm.nih.gov/41660935/))
- **NOX4-mediated epigenetic mechanism**: NOX4-derived oxidative DNA damage impairs thyroid differentiation through epigenetic reprogramming in BRAF-mutated RAI-refractory cells ([PMID: 41694580](https://pubmed.ncbi.nlm.nih.gov/41694580/))
- **Global hypomethylation**: Associated with chromosomal instability in aggressive PTC ([PMID: 41660935](https://pubmed.ncbi.nlm.nih.gov/41660935/))

---

## 5. Environmental Information

### Environmental Factors

- **Ionizing radiation**: Most established risk factor; includes external radiation exposure, nuclear fallout, and therapeutic radiation ([PMID: 41370693](https://pubmed.ncbi.nlm.nih.gov/41370693/); [PMID: 23132514](https://pubmed.ncbi.nlm.nih.gov/23132514/))
- **Volcanic emissions**: Toxic compounds in gas, ash, and lava contaminate ground water and food chains ([PMID: 30104523](https://pubmed.ncbi.nlm.nih.gov/30104523/))
- **Xenobiotic compounds**: Environmental pollutants (PCBs, nitrates) accumulate and exert carcinogenic effects ([PMID: 30104523](https://pubmed.ncbi.nlm.nih.gov/30104523/))

### Lifestyle Factors

- **Obesity**: BMI associated with altered clinicopathological features; MAFLD/NAFLD associated with higher BRAF V600E incidence and lymph node metastasis ([PMID: 36696026](https://pubmed.ncbi.nlm.nih.gov/36696026/); [PMID: 38787506](https://pubmed.ncbi.nlm.nih.gov/38787506/))
- **Iodine intake**: Both deficiency and excess modify thyroid cancer risk in a U-shaped relationship ([PMID: 41675569](https://pubmed.ncbi.nlm.nih.gov/41675569/))

### Infectious Agents

Not directly applicable. No established infectious etiology for BRAF-mutant PTC, though chronic lymphocytic thyroiditis (Hashimoto's) shows complex immunological relationships with PTC ([PMID: 38940753](https://pubmed.ncbi.nlm.nih.gov/38940753/)).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**Primary pathway — MAPK/ERK cascade:**

```
BRAF V600E (constitutively active)
    |
    v
MEK1/2 phosphorylation (constitutive)
    |
    v
ERK1/2 phosphorylation (constitutive)
    |
    |---> Cell proliferation (Cyclin D1, c-Myc)
    |---> Survival (BCL-2 family)
    |---> NIS suppression --> RAI refractoriness
    |---> Dedifferentiation gene silencing
    |---> PD-L1 upregulation --> Immune evasion
    +---> Tumor invasion/migration (MMP, EMT)
```

The BRAF V600E mutation "activates the MAPK pathway and suppresses genes involved in iodine metabolism and differentiation" ([PMID: 41368991](https://pubmed.ncbi.nlm.nih.gov/41368991/)). This constitutive signaling operates independently of extracellular growth factor stimulation.

**Secondary pathway involvement:**
- **PI3K/AKT/mTOR**: Dysregulated in concert with MAPK; contributes to resistance ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/))
- **WNT/beta-Catenin**: Beta-catenin attenuation inhibits tumor growth and promotes differentiation in BRAF-mutant models ([PMID: 34224366](https://pubmed.ncbi.nlm.nih.gov/34224366/))
- **NF-kB signaling**: Drives organoid maturation; inhibition synergistically enhances therapeutic efficacy ([PMID: 41761289](https://pubmed.ncbi.nlm.nih.gov/41761289/))

### Cellular Processes

- **NIS suppression and RAI refractoriness**: Up to 60% of PTC harbor BRAF V600E and may become RAI-refractory. NOX4-derived oxidative DNA damage impairs thyroid differentiation through an epigenetic mechanism, silencing NIS expression ([PMID: 41694580](https://pubmed.ncbi.nlm.nih.gov/41694580/)). GO: GO:0006882 (cellular zinc ion homeostasis); GO:0055085 (transmembrane transport)
- **Immune evasion**: BRAF V600E positively correlates with PD-L1 and PD-1 expression in PTC tumor microenvironment (Type 1 PD-L1+/PD-1+ in 41% of cases), suggesting immune checkpoint therapies may be effective ([PMID: 29651624](https://pubmed.ncbi.nlm.nih.gov/29651624/))
- **Dedifferentiation cascade**: Progressive accumulation of TERT, TP53 mutations drives transition from PTC to PDTC to ATC, with LINE-1 retrotransposons and endogenous retroviruses reactivated during this process ([PMID: 41462994](https://pubmed.ncbi.nlm.nih.gov/41462994/); [PMID: 41296188](https://pubmed.ncbi.nlm.nih.gov/41296188/))
- **Metabolic reprogramming**: Fatty acid oxidation drives acetyl-CoA-dependent H3K9ac epigenetic reprogramming to promote adaptive resistance to BRAF-targeted therapy ([PMID: 41862440](https://pubmed.ncbi.nlm.nih.gov/41862440/))

### Protein Dysfunction

BRAF V600E results in a constitutively active kinase domain (gain-of-function). The glutamic acid substitution at position 600 mimics the phosphorylated state of the activation segment, resulting in approximately 500-fold increased basal kinase activity. This removes the requirement for upstream RAS activation and RAF dimerization for signaling ([PMID: 39577552](https://pubmed.ncbi.nlm.nih.gov/39577552/)).

### Resistance Mechanisms

Three major resistance pathways to BRAF inhibitors have been identified:

1. **TAZ/Hippo pathway**: CRISPR screens identified TAZ (WWTR1) deficiency as synthetically lethal with BRAF inhibitor in ATC; TAZ loss triggers ferroptosis ([PMID: 42035477](https://pubmed.ncbi.nlm.nih.gov/42035477/))
2. **Fatty acid oxidation (FAO)**: FAO drives acetyl-CoA-dependent H3K9ac epigenetic reprogramming mediating adaptive resistance ([PMID: 41862440](https://pubmed.ncbi.nlm.nih.gov/41862440/))
3. **RAS pathway feedback activation**: BRAF inhibitors induce feedback activation of RAS signaling in thyroid cancer cells ([PMID: 34072194](https://pubmed.ncbi.nlm.nih.gov/34072194/))

### Molecular Profiling

**Transcriptomics (TCGA):**
- BRAF-like vs. RAS-like molecular classification based on gene expression profiles
- BRAF-like tumors characterized by MAPK pathway activation signature
- Transcriptomic classifiers ("BRAF-like" and "RAS-like") more accurately predict iodine avidity, tumor aggressiveness, and treatment response than histology or genotype alone ([PMID: 41685247](https://pubmed.ncbi.nlm.nih.gov/41685247/))

**Single-cell RNA sequencing:**
- scRNA-seq reveals "differentiation-dependent trajectory of tumor immune microenvironment remodeling—from immune activation/suppression coexistence in PTC, to immune exclusion in PDTC, and terminal exhaustion in ATC" ([PMID: 41562080](https://pubmed.ncbi.nlm.nih.gov/41562080/))
- RGS5+ tumor subpopulation identified with prognostic significance; high prognostic immune score linked to genetic instability ([PMID: 40132388](https://pubmed.ncbi.nlm.nih.gov/40132388/))
- Intra-tumoral heterogeneity in BRAF V600E PTC includes differentiation-dependent functional states ([PMID: 41935217](https://pubmed.ncbi.nlm.nih.gov/41935217/))

**Proteomics:**
- Differential activation of MAPK and PI3K pathways critical for enhancing lateral lymph node metastatic potential ([PMID: 39600146](https://pubmed.ncbi.nlm.nih.gov/39600146/))
- Patient-derived organoids (DEOs) achieve 92% driver gene concordance with parental tumors and faithfully recapitulate histopathological architecture and immune microenvironment ([PMID: 41761289](https://pubmed.ncbi.nlm.nih.gov/41761289/))

---

## 7. Anatomical Structures Affected

### Organ Level

| Level | Structure | UBERON Term | Involvement |
|-------|-----------|-------------|-------------|
| **Primary** | Thyroid gland | UBERON:0002046 | Direct malignant transformation |
| **Secondary** | Cervical lymph nodes | UBERON:0002429 | Metastatic (30–80%) |
| **Secondary** | Lung | UBERON:0002048 | Distant metastasis (2–15%) |
| **Secondary** | Bone | UBERON:0002481 | Distant metastasis (rare) |
| **System** | Endocrine system | UBERON:0000949 | TSH/thyroid hormone axis |

### Tissue and Cell Level

- **Thyroid follicular epithelial cells** (CL:0002258): Primary cell of origin for BRAF-mutant PTC
- **Thyroid follicular tissue**: Papillary architecture with fibrovascular cores, psammoma bodies
- **Tumor microenvironment**: CD3+, CD56+, CD68+, alpha-SMA+ cells recapitulated in patient-derived organoids ([PMID: 41761289](https://pubmed.ncbi.nlm.nih.gov/41761289/))

### Subcellular Level

- **Cytoplasm/cytosol** (GO:0005829): BRAF kinase signaling
- **Cell membrane** (GO:0005886): NIS (SLC5A5) expression loss
- **Nucleus** (GO:0005634): ERK-mediated transcriptional changes
- **Endoplasmic reticulum** (GO:0005783): Unfolded protein response under BRAF inhibitor treatment ([PMID: 42035477](https://pubmed.ncbi.nlm.nih.gov/42035477/))

### Localization

Thyroid nodules demonstrate right-side predominance (P=0.0004), and right-sided PTC with lymph node metastasis shows significantly more right-side-affected LNM (P=0.0007) ([PMID: 40050757](https://pubmed.ncbi.nlm.nih.gov/40050757/)). The tumor can be unilateral or bilateral, unifocal or multifocal.

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Adults aged 40–45 years for PTC ([PMID: 23014067](https://pubmed.ncbi.nlm.nih.gov/23014067/)); median age 56 years for tall cell variant ([PMID: 23682579](https://pubmed.ncbi.nlm.nih.gov/23682579/))
- **Pediatric PTC**: BRAF V600E found in 50.8% of pediatric PTC (Chinese cohort, n=124); independently predicts non-excellent ATA outcomes (aOR=3.45, 95% CI 1.37–8.70) ([PMID: 41499172](https://pubmed.ncbi.nlm.nih.gov/41499172/); [PMID: 39982551](https://pubmed.ncbi.nlm.nih.gov/39982551/))
- **Onset pattern**: Insidious; typically discovered incidentally on imaging or as palpable thyroid nodule

### Progression

**AJCC 8th Edition Staging** (age-dependent for DTC):
- **Stage I**: Age <55 with any T, any N, M0; or age >=55 with T1-T2, N0, M0
- **Stage II**: Age <55 with any T, any N, M1; or age >=55 with T1-T2, N1, M0 or T3, N0-N1, M0
- **Stage III-IV**: Age >=55 with advanced T-stage, extensive nodal disease, or distant metastases

**Disease course**: Most patients (79.1%) present with early-stage disease. The 2022 WHO classification introduced "differentiated high-grade thyroid carcinoma" (DHGTC) as an intermediate entity between well-differentiated PTC and ATC ([PMID: 36193717](https://pubmed.ncbi.nlm.nih.gov/36193717/)).

**Dedifferentiation pathway** ([PMID: 41462994](https://pubmed.ncbi.nlm.nih.gov/41462994/)):

```
Well-differentiated PTC (BRAF V600E)
    | + TERT promoter mutation
    v
Poorly differentiated TC (PDTC)
    | + TP53 mutation
    v
Anaplastic thyroid carcinoma (ATC)
```

**Recurrence patterns**: Most recurrences occur within the first year (23.3%) or after 10 years post-thyroidectomy (35.7%). Patients with very early recurrences (<6 months) had TERT/BRAF V600E mutations in 69% of cases ([PMID: 37336036](https://pubmed.ncbi.nlm.nih.gov/37336036/)).

---

## 9. Inheritance and Population

### Epidemiology

- **Global thyroid cancer incidence**: Age-standardized incidence rate increased from 2.06 to 2.91 per 100,000 (1990–2021), EAPC=1.25 ([PMID: 41726144](https://pubmed.ncbi.nlm.nih.gov/41726144/))
- **Global mortality**: Modest decline (EAPC=-0.23), but DALYs remained high (14.57 million in 2021) ([PMID: 41726144](https://pubmed.ncbi.nlm.nih.gov/41726144/))
- **Overdiagnosis**: Estimated at approximately 25% globally; population-based study across 63 countries found 75.6% of 2.3 million thyroid cancer cases attributable to overdiagnosis ([PMID: 39389067](https://pubmed.ncbi.nlm.nih.gov/39389067/); [PMID: 39330046](https://pubmed.ncbi.nlm.nih.gov/39330046/))

### Genetic Inheritance

BRAF V600E in PTC is a **somatic mutation** (not inherited). However:
- **Multifactorial/polygenic susceptibility**: GWAS loci (FOXE1, NKX2-1, DIRC3, NRG1, BATF) confer inherited susceptibility to DTC
- **Familial non-medullary thyroid carcinoma**: ~5% of PTC cases show familial clustering; modifier genes influence susceptibility
- **No Mendelian inheritance pattern** for BRAF-mutant PTC specifically

### Population Demographics

- **Sex ratio**: Female-to-male ~2.5–4:1; women account for 67% of cases globally ([PMID: 41726144](https://pubmed.ncbi.nlm.nih.gov/41726144/))
- **Geographic variation**: Highest incidence in South Korea, Cyprus, Ecuador, China, and Turkiye; high-SDI regions account for 72% of cases due to intensive screening, while low-SDI regions contribute 68% of deaths due to delayed diagnosis ([PMID: 41726144](https://pubmed.ncbi.nlm.nih.gov/41726144/); [PMID: 39389067](https://pubmed.ncbi.nlm.nih.gov/39389067/))
- **BRAF V600E prevalence varies geographically**: From 40% to >78% depending on population and study design

---

## 10. Diagnostics

### Clinical Tests

**Imaging:**
- **Thyroid ultrasound** (primary modality): ACR TI-RADS risk stratification system for thyroid nodules ([PMID: 33112199](https://pubmed.ncbi.nlm.nih.gov/33112199/))
- **CT neck with contrast**: Optional for baseline AS assessment; evaluates extrathyroidal extension
- **I-123/I-131 whole-body scan**: Assesses RAI avidity post-thyroidectomy
- **F-18-FDG PET/CT**: For RAI-refractory disease and ATC

**Laboratory tests:**
- Serum thyroglobulin (Tg): Primary tumor marker; ATA 2025 raised excellent-response threshold to 2.5 ng/mL ([PMID: 41697551](https://pubmed.ncbi.nlm.nih.gov/41697551/))
- Anti-thyroglobulin antibodies (TgAb)
- TSH, free T4

**Biopsy:**
- Fine-needle aspiration biopsy (FNAB) with Bethesda System cytological classification
- BRAF V600E immunohistochemistry (VE1 antibody): 88% concordance with NGS ([PMID: 40614342](https://pubmed.ncbi.nlm.nih.gov/40614342/))

### Genetic/Molecular Testing

- **BRAF V600E testing**: Single-gene PCR, pyrosequencing, or allele-specific PCR from FNA or surgical specimens
- **NGS panels**: Myriapod panel (16 genes), Archer DX VariantPlex (31 genes) + FusionPlex (40 genes) achieve 100% sensitivity, 95.5% specificity ([PMID: 41370117](https://pubmed.ncbi.nlm.nih.gov/41370117/))
- **4-gene NGS panel** (BRAF + 3 others): Cost-effective for predicting PTC in indeterminate cytology ([PMID: 42083301](https://pubmed.ncbi.nlm.nih.gov/42083301/))
- **Liquid biopsy**: ctDNA detection of BRAF V600E in plasma feasible; detected in 79.7% of malignant cases using 8-gene panel ([PMID: 36744987](https://pubmed.ncbi.nlm.nih.gov/36744987/))
- **Transcriptomic classifiers**: Thyroid GuidePx and similar tools classify tumors as "BRAF-like" vs "RAS-like" ([PMID: 41685247](https://pubmed.ncbi.nlm.nih.gov/41685247/))

### Clinical Criteria

- **ATA 2015 / ATA 2025 risk stratification**: Low, intermediate, and high-risk categories based on clinicopathological features
- **ATA 2025 update**: Reclassified 89.1% of low-risk DTC as excellent response at baseline vs. 49.2% under ATA 2015 (P<0.001) ([PMID: 41697551](https://pubmed.ncbi.nlm.nih.gov/41697551/))

### Differential Diagnosis

| Condition | Distinguishing Feature |
|-----------|----------------------|
| Follicular thyroid carcinoma | RAS-driven; encapsulated; no papillary architecture |
| Medullary thyroid carcinoma | C-cell origin; RET mutations; elevated calcitonin |
| NIFTP | Non-invasive; follicular growth; RAS-like molecular profile |
| Hashimoto thyroiditis | Autoimmune; may coexist with PTC |
| Follicular adenoma | Benign; encapsulated without invasion |

---

## 11. Outcome/Prognosis

### Survival and Mortality

| Metric | Value | Source |
|--------|-------|--------|
| 10-year DSS (all DTC) | 97.2% | Population-based cohort, n=3,330 ([PMID: 41817109](https://pubmed.ncbi.nlm.nih.gov/41817109/)) |
| 10-year OS (PTC, Saudi Arabia) | 95.8% | Retrospective cohort, n=293 ([PMID: 41215859](https://pubmed.ncbi.nlm.nih.gov/41215859/)) |
| Recurrence rate | 2.1–30% | Depends on risk stratification |
| 5-year PFS (low-risk pediatric) | 86% | Multi-center, n=216 ([PMID: 39821955](https://pubmed.ncbi.nlm.nih.gov/39821955/)) |
| 5-year PFS (high-risk pediatric) | 43% | Same cohort |
| Disease-specific survival (pediatric) | 100% | Pediatric DTC series |

### Prognostic Factors

**Adverse prognostic factors:**
- BRAF V600E + TERT co-mutation (OR for RAI refractoriness = 4.8)
- Age >=55 years with extrathyroidal extension (26.47-fold higher odds of incomplete response) ([PMID: 41275349](https://pubmed.ncbi.nlm.nih.gov/41275349/))
- Tall cell variant histology (92.6% BRAF V600E positive; 36% present at stage III/IVA) ([PMID: 23682579](https://pubmed.ncbi.nlm.nih.gov/23682579/))
- Hobnail variant (75% BRAF and p53 positivity) ([PMID: 40560352](https://pubmed.ncbi.nlm.nih.gov/40560352/))
- Distant metastasis, incomplete resection, male sex, non-papillary histology

**Favorable prognostic factors:**
- Young age at diagnosis (<55 years)
- Classic PTC without high-grade features
- Absence of TERT co-mutation
- RAS-mutant or DICER1-mutant molecular profile (in pediatric PTC) ([PMID: 41499172](https://pubmed.ncbi.nlm.nih.gov/41499172/))

### Prognostic Biomarkers

- **BRAF V600E + TERT promoter co-mutation**: Strongest molecular predictor of aggressive behavior
- **Serum VEGFA**: Elevated baseline independently associated with poor PFS ([PMID: 31558473](https://pubmed.ncbi.nlm.nih.gov/31558473/))
- **RGS5+ tumor subpopulation**: Outperforms existing models in predicting patient outcomes ([PMID: 40132388](https://pubmed.ncbi.nlm.nih.gov/40132388/))
- **miR-146b, miR-221, miR-375**: Promising predictors of aggressive disease progression ([PMID: 41660935](https://pubmed.ncbi.nlm.nih.gov/41660935/))

---

## 12. Treatment

### Surgical Treatment (MAXO:0000136 — Thyroidectomy)

| Procedure | Indication | Evidence |
|-----------|-----------|----------|
| **Total thyroidectomy** | Standard for PTC >4 cm, bilateral, or high-risk | Decreasing utilization per ATA guidelines |
| **Thyroid lobectomy** | Low-risk PTC 1–4 cm, unilateral, N0 | Increasing use (13.7% to 22.9% after 2015 ATA) ([PMID: 36326739](https://pubmed.ncbi.nlm.nih.gov/36326739/)) |
| **Central compartment dissection** | Clinically apparent N1a disease | Prophylactic role limited |
| **Lateral neck dissection** | N1b disease | Lobectomy non-inferior to TT+RAI for select N1b (5-yr OS 96.9% vs 96.8%) ([PMID: 41411004](https://pubmed.ncbi.nlm.nih.gov/41411004/)) |
| **Thermal ablation (RFA/MWA)** | T1N0M0, select candidates | Comparable long-term DFS to surgery with fewer complications ([PMID: 41350156](https://pubmed.ncbi.nlm.nih.gov/41350156/); [PMID: 40770138](https://pubmed.ncbi.nlm.nih.gov/40770138/)) |

### Radioactive Iodine Therapy (MAXO:0001298)

- Selective use recommended based on risk stratification
- RAI not significantly associated with DSS overall, but associated with >80% risk reduction in metastatic DTC (HR 0.192; CI 0.088–0.417) ([PMID: 41817109](https://pubmed.ncbi.nlm.nih.gov/41817109/))
- Decreasing utilization: adjuvant RAI rates fell from 48.7% to 19.3% after 2015 guidelines ([PMID: 36326739](https://pubmed.ncbi.nlm.nih.gov/36326739/))

### Targeted Therapy (MAXO:0001525 — Targeted molecular therapy)

**BRAF/MEK Inhibitor Redifferentiation:**

Dabrafenib (150 mg BID) + trametinib (2 mg daily) for RAI-refractory BRAF V600E DTC:
- Phase II trial (n=24): Restored abnormal I-131 uptake from 5% at baseline to 95% on post-therapy scan
- At 6 months: PR 38%, SD 52%, PD 10%
- 12-month PFS 82%, 24-month PFS 68% ([PMID: 37074727](https://pubmed.ncbi.nlm.nih.gov/37074727/))

**Multikinase Inhibitors for RAI-Refractory DTC:**

| Trial | Drug | Line | PFS (median) | HR | Key Result |
|-------|------|------|-------------|----|----|
| SELECT | Lenvatinib | 1st | 18.3 vs 3.6 mo | 0.21 | P<0.001 |
| DECISION | Sorafenib | 1st | 10.8 vs 5.8 mo | 0.59 | P<0.001 |
| COSMIC-311 | Cabozantinib | 2nd+ | — | 0.22 | P<0.0001 ([PMID: 34237250](https://pubmed.ncbi.nlm.nih.gov/34237250/)) |

Real-world lenvatinib data: median PFS 36.0 months, OS 76.7 months, ORR 52.3%, DCR 95.5% ([PMID: 41565294](https://pubmed.ncbi.nlm.nih.gov/41565294/)).

### Immunotherapy

- **BRAF V600E ATC**: Kinase inhibitors + anti-PD-1 achieved mOS not reached for BRAF V600E ATC vs. 4.0 months for non-BRAF (P=0.049); ORR 61.1% ([PMID: 39395384](https://pubmed.ncbi.nlm.nih.gov/39395384/))
- **Neoadjuvant mutation-based therapy**: Converted 9/12 unresectable ATC to resectable ([PMID: 40927298](https://pubmed.ncbi.nlm.nih.gov/40927298/))
- **PD-L1/PD-1 correlation**: BRAF V600E positively correlates with PD-L1 expression, suggesting potential immunotherapy targets ([PMID: 29651624](https://pubmed.ncbi.nlm.nih.gov/29651624/))

### Active Surveillance (MAXO:0000950)

For low-risk PTMC (Bethesda V–VI, <=1 cm, no adverse features):
- Initiated 1993 at Kuma Hospital; zero thyroid-cancer-related deaths reported in 30+ years ([PMID: 41196684](https://pubmed.ncbi.nlm.nih.gov/41196684/))
- Argentine cohort (n=104): 5- and 10-year cumulative tumor growth 7% and 8%; LN metastasis 0.9% ([PMID: 40425952](https://pubmed.ncbi.nlm.nih.gov/40425952/))
- 2025 Korean guideline: Recommends AS for adults with confirmed PTMC without adverse features ([PMID: 40598902](https://pubmed.ncbi.nlm.nih.gov/40598902/))
- HRQOL: No significant difference between AS, ablation, and surgery for uncomplicated PTMC (P=.15) ([PMID: 41452620](https://pubmed.ncbi.nlm.nih.gov/41452620/))

### Experimental Therapies

- **Triple therapy (BRAF + MEK + AKT)**: Phase I study showed tolerability and objective responses ([PMID: 38261444](https://pubmed.ncbi.nlm.nih.gov/38261444/))
- **Disulfiram metabolite Cu(DDC)2**: Enhances NIS function via proteostasis modulation for RAI therapy ([PMID: 41679192](https://pubmed.ncbi.nlm.nih.gov/41679192/))
- **Reverse transcriptase inhibitors**: Suppress retroelement activity and may restore RAI uptake ([PMID: 41296188](https://pubmed.ncbi.nlm.nih.gov/41296188/))
- **Patient-derived organoids**: Microfluidic DEOs with 76% success rate enable personalized drug screening ([PMID: 41761289](https://pubmed.ncbi.nlm.nih.gov/41761289/))

---

## 13. Prevention

### Primary Prevention

- **Radiation protection**: Minimize unnecessary radiation exposure; iodine prophylaxis for nuclear emergencies
- **Iodine supplementation**: Maintain adequate iodine intake to prevent both deficiency and excess-related risk
- **Obesity management**: Address metabolic risk factors (MAFLD/NAFLD)

### Secondary Prevention (Screening and Early Detection)

- **Avoiding overdiagnosis**: Global thyroid cancer overdiagnosis estimated at ~25%; "incidence has risen exponentially, mostly driven by overdiagnosis of low-risk tumors; however, a small rise in incidence of higher risk tumors has been noted" ([PMID: 39087407](https://pubmed.ncbi.nlm.nih.gov/39087407/))
- **ACR TI-RADS**: Ultrasound-based risk stratification reduces unnecessary biopsies by 19.9–46.5% compared to other systems ([PMID: 33112199](https://pubmed.ncbi.nlm.nih.gov/33112199/))
- **Molecular testing of indeterminate nodules**: BRAF V600E testing on FNA reduces unnecessary surgery

### Tertiary Prevention

- **Dynamic risk stratification**: ATA 2025 response assessment categories (excellent, indeterminate, biochemical incomplete, structural incomplete)
- **Active surveillance protocols**: Follow-up ultrasound every 6 months for 2 years, then annually ([PMID: 40598902](https://pubmed.ncbi.nlm.nih.gov/40598902/))
- **TSH suppression**: Tailored to risk category
- **Genetic counseling**: For familial non-medullary thyroid cancer families

---

## 14. Other Species / Natural Disease

### Comparative Biology

- **BRAF ortholog**: BRAF is highly conserved across vertebrates
  - Mouse (*Mus musculus*): NCBI Gene ID 109880
  - Zebrafish (*Danio rerio*): NCBI Gene ID 403065
  - Dog (*Canis lupus familiaris*): NCBI Gene ID 475526

- **Canine thyroid carcinoma**: Dogs develop follicular thyroid carcinoma naturally, though BRAF V600E is not a prominent driver in canine thyroid tumors. Canine thyroid cancer shares some histopathological features with human DTC.

- **Evolutionary conservation**: The MAPK/ERK signaling pathway is evolutionarily conserved from invertebrates to humans, with BRAF orthologs present in Drosophila (dRaf) and C. elegans (lin-45). Mutations in these orthologs produce developmental phenotypes relevant to understanding BRAF oncogenesis.

### Zoonotic Potential

Not applicable — BRAF-mutant PTC is not an infectious or transmissible disease.

---

## 15. Model Organisms

### Mouse Models

- **BrafV600E knock-in mice** (thyroid-specific): Thyroid-targeted expression of BrafV600E using Tg-Cre or TPO-Cre drivers produces autochthonous PTC that recapitulates human disease features, including papillary architecture and loss of differentiation markers. scRNA-seq analysis of these models reveals transcriptional heterogeneity and hierarchical trajectories of malignant thyrocytes ([PMID: 41935217](https://pubmed.ncbi.nlm.nih.gov/41935217/)).
- **Beta-catenin attenuation studies**: Demonstrated that WNT pathway inhibition can promote differentiation in BRAF-mutant thyroid tumors ([PMID: 34224366](https://pubmed.ncbi.nlm.nih.gov/34224366/))
- **Limitations**: Mouse models may not fully recapitulate human immune microenvironment or dedifferentiation dynamics

### Cell Lines

- **BCPAP**: Human PTC cell line harboring BRAF V600E; widely used for signaling and drug sensitivity studies
- **8505C**: ATC cell line with BRAF V600E; used for resistance mechanism studies
- **KTC-1**: PTC cell line for BRAF inhibitor studies
- **Patient-derived organoids (PDOs/DEOs)**: Microfluidic-generated organoids achieve 92% driver gene concordance, recapitulate immune microenvironment (CD3+/CD56+/CD68+/alpha-SMA+), and enable personalized drug screening ([PMID: 41761289](https://pubmed.ncbi.nlm.nih.gov/41761289/))

### Zebrafish Models

Zebrafish expressing human BRAF V600E develop thyroid hyperplasia, useful for high-throughput drug screening and studying early oncogenic events.

---

## Key Findings — Statistical Evidence Summary

### Finding 1: BRAF V600E Prevalence and Prognostic Impact
BRAF V600E is the most common oncogenic driver in PTC (40–80% prevalence). Meta-analysis of 46 studies (20,570 patients) confirmed significant association with lymph node metastasis (OR=1.38, 95% CI 1.17–1.61) and borderline recurrence risk (OR=1.56, 95% CI 1.00–2.41) ([PMID: 41419184](https://pubmed.ncbi.nlm.nih.gov/41419184/)). A 2025 study found 78.7% prevalence, with subtype-specific distribution: 88% classic, 38% follicular variant, 100% tall cell ([PMID: 40237893](https://pubmed.ncbi.nlm.nih.gov/40237893/)).

### Finding 2: MAPK Activation and NIS Suppression
BRAF V600E constitutively activates the MAPK pathway and suppresses iodine metabolism genes ([PMID: 41368991](https://pubmed.ncbi.nlm.nih.gov/41368991/)). NOX4-derived oxidative DNA damage impairs differentiation via epigenetic mechanisms ([PMID: 41694580](https://pubmed.ncbi.nlm.nih.gov/41694580/)).

### Finding 3: BRAF + TERT Synergy
Coexisting mutations independently elevated RAI refractoriness risk (OR=4.8, P=.009) ([PMID: 40988283](https://pubmed.ncbi.nlm.nih.gov/40988283/)). TERT alone predicts lateral LN metastasis (OR=2.272) ([PMID: 40184730](https://pubmed.ncbi.nlm.nih.gov/40184730/)).

### Finding 4: Redifferentiation Therapy Success
Dabrafenib-trametinib restored RAI uptake from 5% to 95% in BRAF V600E RAI-refractory DTC, with PR in 38% and 24-month PFS of 68% ([PMID: 37074727](https://pubmed.ncbi.nlm.nih.gov/37074727/)).

### Finding 5: Resistance Mechanisms
Three validated mechanisms: TAZ/Hippo (ferroptosis) ([PMID: 42035477](https://pubmed.ncbi.nlm.nih.gov/42035477/)), FAO-driven epigenetic reprogramming ([PMID: 41862440](https://pubmed.ncbi.nlm.nih.gov/41862440/)), and RAS feedback activation ([PMID: 34072194](https://pubmed.ncbi.nlm.nih.gov/34072194/)).

### Finding 6: Active Surveillance Safety
Over 30 years of AS data with zero thyroid-cancer-related deaths ([PMID: 41196684](https://pubmed.ncbi.nlm.nih.gov/41196684/)). MAeSTro study (n=1,177) and multiple international cohorts validate this approach ([PMID: 39962344](https://pubmed.ncbi.nlm.nih.gov/39962344/)).

### Finding 7: Immunotherapy in BRAF-Mutant ATC
Kinase inhibitors + anti-PD-1 achieved ORR 61.1% and mOS not reached in BRAF V600E ATC vs. 4.0 months for non-BRAF (P=0.049) ([PMID: 39395384](https://pubmed.ncbi.nlm.nih.gov/39395384/)).

### Finding 8: Global Overdiagnosis
Estimated at ~25% of thyroid cancers globally, driven by screening intensity in high-SDI regions ([PMID: 39389067](https://pubmed.ncbi.nlm.nih.gov/39389067/); [PMID: 39330046](https://pubmed.ncbi.nlm.nih.gov/39330046/)).

---

## Mechanistic Model: From Mutation to Clinical Phenotype

```
+----------------------------------------------------------------+
|                    INITIATING EVENT                             |
|         Somatic BRAF V600E mutation (c.1799T>A)                |
|              in thyroid follicular cell                          |
+----------------------------+-----------------------------------+
                             |
                             v
+----------------------------------------------------------------+
|              CONSTITUTIVE MAPK ACTIVATION                       |
|    BRAF V600E --> MEK1/2 --> ERK1/2 (independent of RAS)       |
+------+----------+----------+----------+----------+-------------+
       |          |          |          |          |
       v          v          v          v          v
  Proliferation  NIS loss   PD-L1 up  TSG silenc  EMT/Invasion
  (Cyclin D1)   (RAI-R)   (immune    (RASSF1A,   (MMP, TGFb)
                           evasion)   TIMP3 meth)
       |          |          |          |          |
       +----------+----------+----------+----------+
                             |
          +------------------+------------------+
          v                  v                  v
    Low-risk PTC    Intermediate PTC    High-risk PTC
    (indolent)      (moderate risk)     (aggressive)
          |                  |                  |
          |         + TERT mutation              |
          |                  |                  v
          |                  v             Dedifferentiation
          |          RAI-refractory        + TP53 mutation
          |           disease                   |
          |                  |                  v
          |                  |              ATC (lethal)
          v                  v                  v
    Active            BRAF/MEK inhibitor   Immunotherapy +
    surveillance      redifferentiation    targeted therapy
    (safe)            (RAI restored)       (ORR 61%)
+----------------------------------------------------------------+
```

---

## Evidence Base — Key Literature

| Citation | Key Contribution |
|----------|-----------------|
| [PMID: 41419184](https://pubmed.ncbi.nlm.nih.gov/41419184/) | Largest meta-analysis (46 studies, 20,570 patients) of BRAF V600E prognostic impact |
| [PMID: 41368991](https://pubmed.ncbi.nlm.nih.gov/41368991/) | Mechanistic review of BRAF V600E in PTC: MAPK activation and differentiation loss |
| [PMID: 40988283](https://pubmed.ncbi.nlm.nih.gov/40988283/) | BRAF + TERT co-mutation synergy: OR=4.8 for RAI refractoriness |
| [PMID: 37074727](https://pubmed.ncbi.nlm.nih.gov/37074727/) | Landmark phase II trial: dabrafenib-trametinib redifferentiation therapy |
| [PMID: 34237250](https://pubmed.ncbi.nlm.nih.gov/34237250/) | COSMIC-311: cabozantinib as 2nd-line for RAI-R DTC (HR=0.22) |
| [PMID: 41196684](https://pubmed.ncbi.nlm.nih.gov/41196684/) | 30+ years of active surveillance safety data from Kuma Hospital |
| [PMID: 39395384](https://pubmed.ncbi.nlm.nih.gov/39395384/) | Immunotherapy + kinase inhibitors in BRAF V600E ATC: ORR 61.1% |
| [PMID: 41562080](https://pubmed.ncbi.nlm.nih.gov/41562080/) | scRNA-seq revealing immune trajectory across thyroid cancer differentiation spectrum |
| [PMID: 41726144](https://pubmed.ncbi.nlm.nih.gov/41726144/) | GBD 2021: comprehensive global thyroid cancer epidemiology |
| [PMID: 39389067](https://pubmed.ncbi.nlm.nih.gov/39389067/) | 63-country overdiagnosis estimate (75.6% attributable) |
| [PMID: 41697551](https://pubmed.ncbi.nlm.nih.gov/41697551/) | ATA 2025 vs ATA 2015 reclassification: 89.1% vs 49.2% excellent response |
| [PMID: 41499172](https://pubmed.ncbi.nlm.nih.gov/41499172/) | Pediatric BRAF V600E: aOR=3.45 for non-excellent outcomes |
| [PMID: 42035477](https://pubmed.ncbi.nlm.nih.gov/42035477/) | CRISPR screen identifies TAZ as BRAF inhibitor resistance target |
| [PMID: 41761289](https://pubmed.ncbi.nlm.nih.gov/41761289/) | Patient-derived organoids with 92% driver gene concordance |
| [PMID: 36193717](https://pubmed.ncbi.nlm.nih.gov/36193717/) | WHO 2022 classification update introducing DHGTC |

---

## Limitations and Knowledge Gaps

1. **BRAF V600E prognostic independence**: While meta-analyses show significant associations with aggressive features, the independent prognostic value of BRAF V600E after multivariate adjustment remains debated. The borderline recurrence OR (1.56, 95% CI 1.00–2.41) underscores uncertainty ([PMID: 41419184](https://pubmed.ncbi.nlm.nih.gov/41419184/)).

2. **Overdiagnosis confounding**: The substantial overdiagnosis of thyroid cancer (~25%) confounds epidemiological analyses and may inflate the apparent indolent behavior of BRAF-mutant PTMC in surveillance studies.

3. **Redifferentiation durability**: Phase II redifferentiation data (24-month PFS 68%) require longer follow-up and phase III confirmation. Optimal sequencing of redifferentiation vs. MKI therapy is undefined.

4. **Resistance mechanisms**: While three mechanisms have been identified (TAZ, FAO, RAS feedback), clinical strategies to overcome them remain largely preclinical. The interplay between multiple resistance pathways in individual patients is poorly understood.

5. **Pediatric data gaps**: Pediatric BRAF-mutant PTC has distinct biology (more aggressive despite excellent survival), but dedicated pediatric clinical trials for targeted therapies are lacking.

6. **Single-cell resolution limitations**: scRNA-seq studies have revealed immune trajectory and heterogeneity, but spatial transcriptomics data for BRAF-mutant PTC remain limited. Translating single-cell findings to clinical biomarkers requires validation.

7. **Geographic and ethnic variation**: BRAF V600E prevalence varies widely (40–80%), and GWAS susceptibility loci show population specificity (e.g., NRG1 in Korean, BATF/DHX35 in Italian populations). Cross-ethnic validation of molecular risk models is needed.

8. **Active surveillance expansion**: MAeSTro-EXP is extending AS to tumors up to 1.5 cm, but long-term outcomes for this expanded cohort are not yet available.

---

## Proposed Follow-up Experiments/Actions

### Near-Term (1–2 years)

1. **Phase III redifferentiation trial**: Prospective randomized trial comparing dabrafenib-trametinib redifferentiation + RAI vs. standard MKI therapy in BRAF V600E RAI-refractory DTC.

2. **Combinatorial resistance studies**: Clinical trials testing TAZ inhibitors or FAO inhibitors in combination with BRAF/MEK inhibitors in patients progressing on monotherapy.

3. **ctDNA monitoring validation**: Prospective study validating BRAF V600E ctDNA as a minimal residual disease biomarker after thyroidectomy, with sensitivity analysis against serum thyroglobulin.

4. **Expanded active surveillance cohort**: Long-term outcomes from MAeSTro-EXP (1.0–1.5 cm tumors) to define safe upper size limit for observation.

### Medium-Term (2–5 years)

5. **Immunotherapy biomarker discovery**: Prospective correlation of PD-L1 expression, BRAF V600E status, and tumor immune microenvironment features with immunotherapy response in advanced DTC/ATC.

6. **Multi-ethnic GWAS integration**: Pan-ancestry GWAS combining existing data with African, South Asian, and Latin American cohorts to identify universal and population-specific PTC susceptibility loci.

7. **Spatial multi-omics of dedifferentiation**: Spatial transcriptomics and proteomics profiling of BRAF V600E PTC to PDTC to ATC transition specimens to map the molecular geography of dedifferentiation.

8. **Organoid-guided personalized therapy**: Clinical trial using patient-derived organoid drug sensitivity testing to guide second-line therapy selection in RAI-refractory DTC.

### Long-Term (5+ years)

9. **AI-integrated risk stratification**: Development and validation of machine learning models integrating ultrasound features, molecular profiling, liquid biopsy, and clinical data for precision risk assessment.

10. **Prevention trials**: Interventional studies testing whether metabolic syndrome management (weight loss, NAFLD treatment) reduces PTC incidence or modifies BRAF V600E positivity rates.

---

## Ontology Term Summary

| Domain | Suggested Terms |
|--------|----------------|
| **MONDO** | MONDO:0005031 (Thyroid gland papillary carcinoma) |
| **HPO** | HP:0002890 (Thyroid carcinoma), HP:0002716 (Lymphadenopathy), HP:0001609 (Hoarseness), HP:0002015 (Dysphagia) |
| **GO (Biological Process)** | GO:0000165 (MAPK cascade), GO:0006915 (Apoptotic process), GO:0055085 (Transmembrane transport), GO:0008283 (Cell population proliferation) |
| **GO (Cellular Component)** | GO:0005829 (Cytosol), GO:0005886 (Plasma membrane), GO:0005634 (Nucleus) |
| **CL (Cell Ontology)** | CL:0002258 (Thyroid follicular cell) |
| **UBERON** | UBERON:0002046 (Thyroid gland), UBERON:0002429 (Cervical lymph node) |
| **CHEBI** | CHEBI:24859 (Iodide), CHEBI:68481 (Dabrafenib), CHEBI:75998 (Trametinib), CHEBI:90227 (Lenvatinib), CHEBI:50924 (Sorafenib) |
| **MAXO** | MAXO:0000136 (Thyroidectomy), MAXO:0001298 (Radioiodine therapy), MAXO:0001525 (Targeted molecular therapy), MAXO:0000950 (Active surveillance) |

---

*Report generated from 5 investigation iterations, 17 confirmed findings, 182 papers reviewed. Last updated: 2026-05-05.*
