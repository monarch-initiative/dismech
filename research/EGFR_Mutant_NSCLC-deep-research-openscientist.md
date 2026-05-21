---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-06T08:23:44.569836'
end_time: '2026-05-06T10:07:46.159416'
duration_seconds: 6241.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: EGFR-Mutant Non-Small Cell Lung Cancer
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
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** EGFR-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **EGFR-Mutant Non-Small Cell Lung Cancer** covering all of the
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

# Comprehensive Disease Characterization: EGFR-Mutant Non-Small Cell Lung Cancer

## Summary

EGFR-mutant non-small cell lung cancer (NSCLC) is a molecularly defined cancer subtype driven by somatic gain-of-function mutations in the epidermal growth factor receptor (EGFR) tyrosine kinase domain, predominantly exon 19 deletions (~45%) and the L858R point mutation in exon 21 (~40%). This disease preferentially affects never-smoking women of East Asian descent with adenocarcinoma histology, with EGFR mutation prevalence of approximately 30% in East Asian populations versus ~7% in Caucasians. The constitutive activation of EGFR-RAS/MAPK/PI3K-AKT signaling cascades drives uncontrolled proliferation, survival, and metastasis, while simultaneously creating an immunologically "cold" tumor microenvironment with paradoxical PD-L1 prognostic significance and limited benefit from immune checkpoint inhibitors.

The treatment landscape has been transformed by three generations of EGFR tyrosine kinase inhibitors (TKIs), with osimertinib—a third-generation, mutant-selective TKI—established as the current standard of care across multiple disease stages: first-line metastatic (FLAURA), adjuvant resected (ADAURA), and consolidation after chemoradiotherapy for unresectable stage III (LAURA). However, resistance inevitably develops through diverse mechanisms including on-target mutations (T790M, C797S), bypass pathway activation (MET amplification), histologic transformation, and epigenetic reprogramming mediated by the AP-1 transcription factor complex. Emerging combination strategies (osimertinib + chemotherapy, amivantamab + lazertinib), antibody-drug conjugates (sacituzumab tirumotecan, datopotamab deruxtecan), and fourth-generation TKIs are expanding post-progression options.

A critical unmet need exists in lung cancer screening: never-smokers—who harbor the highest EGFR mutation rates—remain excluded from current low-dose CT (LDCT) guidelines despite evidence that Asian never-smokers have a 2.3-fold higher baseline lung cancer incidence and screening trial detection rates comparable to smoker-based programs. This report synthesizes evidence from 104 publications across 17 confirmed findings to provide a comprehensive disease knowledge base entry spanning etiology, molecular mechanisms, clinical phenotypes, diagnostics, treatment, prognosis, and prevention.

---

## 1. Disease Information

### Overview

EGFR-mutant NSCLC is a molecular subtype of non-small cell lung cancer characterized by activating somatic mutations in the EGFR gene (chromosome 7p11.2), which encodes a transmembrane receptor tyrosine kinase of the ErbB family. These mutations lead to ligand-independent, constitutive activation of downstream proliferative and survival signaling pathways, making the tumor exquisitely sensitive to EGFR tyrosine kinase inhibitors. NSCLC accounts for approximately 85% of all lung cancers, and EGFR mutations represent one of the most prevalent actionable oncogenic driver alterations, found in 10–50% of NSCLC cases depending on ethnicity and histological subtype.

### Key Identifiers

| Identifier | Value |
|---|---|
| **MONDO** | MONDO:0005233 (non-small cell lung carcinoma); MONDO:0008903 (lung adenocarcinoma) |
| **ICD-10** | C34.x (Malignant neoplasm of bronchus and lung) |
| **ICD-11** | 2C25 (Malignant neoplasms of bronchus or lung) |
| **MeSH** | D002289 (Carcinoma, Non-Small-Cell Lung) |
| **OMIM** | 211980 (Lung Cancer); 131550 (EGFR gene) |
| **Orphanet** | ORPHA:70573 (Non-small cell lung cancer) |
| **EGFR Gene** | HGNC:3236; NCBI Gene:1956; UniProt:P00533 |

### Synonyms and Alternative Names

- EGFR-positive NSCLC
- EGFR-mutated lung adenocarcinoma
- EGFRm+ NSCLC
- EGFR-driven lung cancer
- Oncogene-addicted NSCLC (EGFR subtype)
- EGFR-activating mutation-positive lung cancer

### Information Sources

This characterization is derived from aggregated disease-level resources including clinical trials (FLAURA, ADAURA, LAURA, MARIPOSA, PAPILLON), large-scale genomic databases (TCGA, COSMIC, cBioPortal), genome-wide association studies, meta-analyses, real-world cohort studies across multiple countries (South Korea, Taiwan, Portugal, India, Morocco, Bangladesh, Malaysia, China, Japan), single-cell RNA sequencing studies, and CRISPR functional genomics screens.

---

## 2. Etiology

### Disease Causal Factors

EGFR-mutant NSCLC is caused by somatic gain-of-function mutations in the EGFR gene that result in constitutive kinase activity independent of ligand binding. Unlike smoking-associated lung cancers driven by KRAS mutations, EGFR-mutant NSCLC arises through distinct mutagenic processes including clock-like mutational signatures and APOBEC-mediated mutagenesis rather than tobacco-associated signatures ([PMID: 39052387](https://pubmed.ncbi.nlm.nih.gov/39052387/)). As one genomic study of the Women's Health Initiative cohort demonstrated, "mutations in both EGFR and KRAS showed unique allelic differences determined by smoking status that are known to alter tumor response to targeted therapy."

### Risk Factors

#### Genetic Risk Factors

- **EGFR somatic mutations** (primary driver): Exon 19 deletions (E746_A750del most common) and L858R point mutation account for ~85% of EGFR mutations
- **Germline susceptibility loci**: A landmark GWAS in 3,173 Japanese EGFR-mutant lung adenocarcinoma patients identified 6 susceptibility loci: 5p15.33 (TERT), 6p21.3 (BTNL2), 3q28 (TP63), 17q24.2 (BPTF), and two novel loci specifically associated with EGFR mutation-positive tumors—**HLA class II at 6p21.32** (rs2179920; P = 5.1 × 10⁻¹⁷, per-allele OR = 1.36) and **FOXP4 at 6p21.1** (rs2495239; P = 3.9 × 10⁻⁹, per-allele OR = 1.19) ([PMID: 27501781](https://pubmed.ncbi.nlm.nih.gov/27501781/))
- **Germline DNA repair gene mutations**: Systematic review identified germline mutations in ATM, BRCA1/2, TP53, PALB2, CHEK2, and EGFR as contributors to NSCLC susceptibility. "Most germline mutations in NSCLC involve genes participating in DNA damage repair and cell cycle control" and "carry important prognostic, predictive, and preventive implications" ([PMID: 41933854](https://pubmed.ncbi.nlm.nih.gov/41933854/))
- **BIM deletion polymorphism**: A 2,903 bp germline deletion in BCL2L11 intron 2, present in ~15.8% of Asian EGFR-mutant NSCLC patients, predicts shorter PFS on EGFR TKIs (HR = 1.35, 95% CI: 1.10–1.64) ([PMID: 34722761](https://pubmed.ncbi.nlm.nih.gov/34722761/))

#### Environmental Risk Factors

- **Smoking**: While EGFR mutations predominantly occur in never-smokers, smoking status modifies allelic differences and treatment response
- **Age**: Median age at diagnosis 60–65 years; young patients (<50) show higher frequency of EGFR mutations ([PMID: 41793321](https://pubmed.ncbi.nlm.nih.gov/41793321/))
- **Sex**: Female predominance (approximately 60–70% of EGFR-mutant cases)
- **Ethnicity**: East Asian descent confers ~4-fold higher EGFR mutation prevalence vs. Caucasians
- **Family history**: Confers 1.7-fold higher lung cancer incidence in never-smokers ([PMID: 41932615](https://pubmed.ncbi.nlm.nih.gov/41932615/))
- **Radon exposure, air pollution, cooking oil fumes**: Environmental risk factors particularly relevant in never-smokers

#### Protective Factors

- Certain HLA alleles may confer reduced susceptibility (further studies needed)
- Environmental protective factors remain poorly defined for this molecular subtype

### Gene-Environment Interactions

The interaction between germline HLA class II variants and EGFR mutation-positive tumors suggests an immune-mediated component to disease susceptibility specific to this molecular subtype. The BIM deletion polymorphism represents a pharmacogenomic gene-environment interaction where a germline variant directly modifies response to targeted therapy.

{{figure:plot_6.png|caption=Comprehensive disease landscape of EGFR-mutant NSCLC integrating epidemiology, molecular mechanisms, treatment strategies, and resistance pathways}}

---

## 3. Phenotypes

### Clinical Symptoms and Signs

| Phenotype | HPO Term | Frequency | Onset | Severity |
|---|---|---|---|---|
| Chronic cough | HP:0012735 | 50–75% | Insidious | Variable |
| Dyspnea | HP:0002094 | 40–60% | Progressive | Moderate-severe |
| Chest pain | HP:0100749 | 25–50% | Variable | Variable |
| Hemoptysis | HP:0002105 | 15–30% | Acute | Variable |
| Weight loss | HP:0001824 | 30–50% | Progressive | Moderate |
| Fatigue | HP:0012378 | 40–60% | Progressive | Moderate |
| Malignant pleural effusion | HP:0002202 | 20–40% | Progressive | Severe |
| Brain metastasis symptoms | HP:0002315, HP:0001250 | 25–40% | Variable | Severe |

### Phenotype Characteristics

- **Age of onset**: Predominantly adult-onset (median 60–65 years); earlier onset in Asian populations and women
- **Symptom progression**: Typically progressive; many patients present with advanced-stage disease
- **CNS involvement**: High propensity for brain metastases (25–40%), including leptomeningeal metastases (3–5%)
- **Quality of life**: Significantly impacted by respiratory symptoms, CNS metastases, and treatment-related adverse events; PROMIS and EORTC QLQ-C30 assessments show maintenance of function with TKI therapy versus chemotherapy. The PAPILLON trial demonstrated that amivantamab plus chemotherapy "significantly delays symptomatic progression without compromising health-related quality of life" ([PMID: 41671629](https://pubmed.ncbi.nlm.nih.gov/41671629/))

### Treatment-Related Phenotypes (EGFR-TKI Adverse Events)

A comprehensive meta-analysis of 34 RCTs (15,887 patients) documented class-specific EGFR-TKI toxicities ([PMID: 38824269](https://pubmed.ncbi.nlm.nih.gov/38824269/)): "EGFR-TKIs were associated with a significantly increased risk of all-grade dermatologic AEs including paronychia, pruritus, rash, skin exfoliation, and skin fissures, gastrointestinal AEs including abdominal pain, diarrhea, dyspepsia, mouth ulceration, and stomatitis, hepatic AEs including elevated alanine aminotransferase and aspartate aminotransferase, and respiratory AEs including epistaxis, interstitial lung disease." Interstitial lung disease (ILD) is rare (~3.7% TKI-induced) but potentially fatal: 9% mortality from osimertinib-related pneumonitis in one cohort, predominantly in male heavy smokers ([PMID: 42049362](https://pubmed.ncbi.nlm.nih.gov/42049362/)).

---

## 4. Genetic/Molecular Information

### Causal Gene: EGFR

- **Gene**: EGFR (Epidermal Growth Factor Receptor)
- **HGNC ID**: HGNC:3236
- **OMIM**: 131550
- **Chromosome**: 7p11.2
- **Protein**: UniProt P00533

### Pathogenic Variants

Analysis of TCGA LUAD Pan-Cancer Atlas (n = 86 EGFR mutations via cBioPortal) confirmed the distribution of EGFR mutations:

{{figure:egfr_mutation_distribution.png|caption=Distribution of EGFR mutation types from TCGA LUAD Pan-Cancer Atlas showing dominance of L858R (26.7%) and exon 19 deletions (23.3%) with diverse uncommon variants}}

| Variant | Clinical Frequency | TCGA Frequency | Exon | Type | Functional Consequence |
|---|---|---|---|---|---|
| **Exon 19 deletions** (E746_A750del) | ~45% | 23.3% | 19 | In-frame deletion | Gain of function |
| **L858R** | ~40% | 26.7% | 21 | Missense | Gain of function |
| **G719X** (G719A, G719S, G719C) | 3–5% | Included in uncommon | 18 | Missense | Gain of function (uncommon sensitizing) |
| **L861Q** | 1–2% | Included in uncommon | 21 | Missense | Gain of function (uncommon sensitizing) |
| **S768I** | 1–2% | Included in uncommon | 20 | Missense | Gain of function (uncommon sensitizing) |
| **Exon 20 insertions** | ~4–12% of EGFR mut | 3.5% (in-frame ins) | 20 | In-frame insertion | Gain of function; generally TKI-resistant |
| **T790M** (resistance) | Acquired ~50–60% on 1st/2nd-gen TKIs | 2.3% | 20 | Missense | Steric hindrance to 1st/2nd-gen TKI binding |
| **C797S** (resistance) | Most common on-target 3rd-gen resistance | Rare in treatment-naïve | 20 | Missense | Loss of covalent binding site for 3rd-gen TKIs |

TCGA mutation types: missense 61.6%, in-frame deletion 30.2%, in-frame insertion 3.5%, nonsense 2.3%. Uncommon sensitizing mutations comprised 11.6% of the TCGA cohort (L861Q, G719A, S768I, E709_T710delinsD).

- **Somatic origin**: All primary driver EGFR mutations are somatic; rare germline EGFR variants (e.g., de novo T790M) exist but are uncommon ([PMID: 38461768](https://pubmed.ncbi.nlm.nih.gov/38461768/))
- **COSMIC**: EGFR is among the most frequently mutated genes in lung adenocarcinoma
- **KEGG**: EGFR mapped to 51 pathways including hsa05223 (NSCLC), hsa04012 (ErbB signaling), hsa01521 (EGFR TKI resistance)

### Modifier Genes

- **TP53**: Co-mutation frequent (~45% in exon 20 insertion tumors; common across subtypes) and associated with adverse prognosis; co-mutation with RB1 predisposes to small-cell transformation
- **BIM (BCL2L11)**: Germline deletion polymorphism modifies TKI response (HR = 1.35 for PFS) — "A germline 2903 bp deletion polymorphism of Bcl-2-like protein 11 (BIM) causes reduced expression of proapoptotic BH3-only BIM protein and blocks TKI-induced apoptosis of tumor cells" ([PMID: 34722761](https://pubmed.ncbi.nlm.nih.gov/34722761/))
- **PIK3CA, CDKN2A**: Co-mutations in exon 20 insertion cases (20% and 10% respectively)
- **STK11**: Mutations affect cancer-associated gene expression broadly in never-smoker lung adenocarcinoma

### Epigenetic Information

- **AP-1/FOSL1/JUN**: CRISPR screen identified AP-1 transcription factor complex as key mediator of osimertinib resistance via epigenetic reprogramming. "Through CRISPR-based functional genomics screen targeting epigenetic regulators and transcription factors, we uncover a critical regulatory network featuring key members of the NuRD and PRC2 complexes that mediate resistance" ([PMID: 40414926](https://pubmed.ncbi.nlm.nih.gov/40414926/))
- **Lineage plasticity**: Transcriptional and epigenetic reprogramming enables histologic transformation — "Lineage plasticity, the ability of cancer cells to alter their differentiated state through transcriptional and epigenetic reprogramming, has emerged as a key mechanism of therapeutic resistance across cancers" ([PMID: 41516316](https://pubmed.ncbi.nlm.nih.gov/41516316/))
- **PP2A-B56α suppression**: Drives EMT in EGFR-mutant NSCLC through posttranslational regulatory mechanisms ([PMID: 41965447](https://pubmed.ncbi.nlm.nih.gov/41965447/))

---

## 5. Environmental Information

### Environmental Factors

- **Radon exposure**: Leading environmental risk factor for lung cancer in never-smokers
- **Air pollution**: Particulate matter (PM2.5) exposure associated with EGFR-mutant lung cancer incidence
- **Cooking oil fumes**: Particularly relevant in Asian female never-smokers
- **Occupational exposures**: Asbestos, heavy metals, radiation

### Lifestyle Factors

EGFR mutations are enriched in never-smokers. "Female gender, nonsmoking status, and adenocarcinoma histology all were independent predictors of response or disease control" to gefitinib in East Asian populations ([PMID: 16989002](https://pubmed.ncbi.nlm.nih.gov/16989002/)). In a Malaysian cohort of resectable NSCLC, "EGFR mutations were detected in 62.3% (n=91) of patients, with 93.4% harbouring single-locus mutations, primarily in exons 19 and 21" with female sex and higher histological grade as independent predictors ([PMID: 41617518](https://pubmed.ncbi.nlm.nih.gov/41617518/)).

### Infectious Agents

- **HPV**: Detected in 31.2% of NSCLC tumors in one Egyptian cohort; relationship to EGFR mutation status requires further study ([PMID: 41327362](https://pubmed.ncbi.nlm.nih.gov/41327362/))
- **Pulmonary microbiota**: Reduced bacterial diversity in lung cancer patients may influence immunotherapy response ([PMID: 41933853](https://pubmed.ncbi.nlm.nih.gov/41933853/))

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

{{figure:egfr_signaling_pathway.png|caption=EGFR signaling pathway architecture showing the RAS-MAPK-ERK and PI3K-AKT-mTOR cascades with therapeutic intervention points across TKI generations}}

The core oncogenic signaling cascade in EGFR-mutant NSCLC:

```
EGFR mutation (constitutive activation)
    │
    ├──→ RAS → RAF → MEK → ERK → Cell proliferation, survival
    │         (KEGG: hsa04010 MAPK signaling)
    │
    ├──→ PI3K → AKT → mTOR → Cell growth, metabolism, anti-apoptosis
    │         (KEGG: hsa04151 PI3K-AKT signaling)
    │
    ├──→ JAK → STAT3 → Transcription of survival genes
    │         (KEGG: hsa04630 JAK-STAT signaling)
    │
    └──→ PLCγ → PKC → Cell motility, invasion
              (KEGG: hsa04012 ErbB signaling)
```

### Cellular Processes

| Process | GO Term | Role in EGFR-mutant NSCLC |
|---|---|---|
| Cell proliferation | GO:0008283 | Constitutive EGFR → uncontrolled division |
| Negative regulation of apoptosis | GO:0043066 | AKT-mediated BCL-2 upregulation |
| Cell migration | GO:0016477 | EMT and metastasis |
| Angiogenesis | GO:0001525 | VEGF pathway activation |
| Epithelial-mesenchymal transition | GO:0001837 | PP2A-B56α suppression drives EMT ([PMID: 41965447](https://pubmed.ncbi.nlm.nih.gov/41965447/)) |

### Protein Dysfunction

Mutant EGFR adopts a constitutively active conformation. Exon 19 deletions remove amino acids near the αC-helix of the kinase domain, stabilizing the active state. L858R substitution in the activation loop similarly favors the active kinase conformation. These mutations increase ATP affinity and basal kinase activity by 10–100-fold. Insertional mutations in the juxtamembrane region can also lead to constitutive receptor dimerization and activation ([PMID: 7478577](https://pubmed.ncbi.nlm.nih.gov/7478577/)).

### Resistance Mechanisms

{{figure:resistance_and_timeline.png|caption=Resistance mechanisms to EGFR TKIs across three generations showing the evolution from T790M-mediated resistance to diverse bypass and transformation pathways}}

Resistance to EGFR TKIs develops through multiple mechanisms ([PMID: 37060646](https://pubmed.ncbi.nlm.nih.gov/37060646/)): "While EGFR-dependent mechanisms consist mainly of the C797S EGFR mutation, EGFR-independent mechanisms include bypass pathways, oncogenic fusions, and phenotypic transformation, among others."

| Mechanism | Category | Frequency | Therapeutic Strategy |
|---|---|---|---|
| **T790M** | On-target | ~50-60% (post-1st/2nd-gen) | Osimertinib (3rd-gen TKI) |
| **C797S** | On-target | Most common (post-3rd-gen) | 4th-gen TKIs (BDTX-1535, JIN-A02, HS-10504) |
| **MET amplification** | Bypass | ~15-20% | MET inhibitors (vabametkib + lazertinib) |
| **SCLC transformation** | Histologic | ~5-15% | Platinum-etoposide chemotherapy |
| **AP-1/epigenetic reprogramming** | Epigenetic | Emerging | MEK/ERK inhibitors, AP-1 targeting |
| **FN1/FAK/YAP1 upregulation** | ECM remodeling | Cross-generational | Combinatorial targeting ([PMID: 42087187](https://pubmed.ncbi.nlm.nih.gov/42087187/)) |
| **BIM deletion polymorphism** | Pharmacogenomic | ~15.8% (Asian) | Bevacizumab addition; HDAC inhibitors |

The CRISPR functional genomics screen finding is particularly significant: "our screen identifies FOSL1 and JUN, two subunits of the AP-1 transcription factor within this network, as the most significant hits" and "genetic depletion or pharmacological inhibition of AP-1 reinstates cellular and molecular sensitivity" ([PMID: 40414926](https://pubmed.ncbi.nlm.nih.gov/40414926/)). This opens a new therapeutic avenue for epigenetic resistance.

Cross-generational resistance mechanisms were identified through proteomics: "extracellular matrix components and signaling proteins (FN1, FAK, YAP1) were found altered and validated as synergistically targetable resistance drivers across all three drug generations" ([PMID: 42087187](https://pubmed.ncbi.nlm.nih.gov/42087187/)).

### Immune System Involvement

EGFR-mutant NSCLC is characterized by an immunologically "cold" tumor microenvironment:
- Low tumor mutational burden (TMB): average 3.3 mutations/megabase
- Attenuated T-cell infiltration with rare CD8+ TILs
- Paradoxical PD-L1 significance: high PD-L1 (≥50%) associated with **worse** outcomes on osimertinib — "PD-L1 ≥50% was associated with over twofold risk of progression" (HR 3.03, 95% CI 1.85–4.96, p < 0.001) and shorter OS ([PMID: 41371099](https://pubmed.ncbi.nlm.nih.gov/41371099/))
- "EGFR-mutant NSCLC with high PD-L1 expression may represent a biologically distinct phenotype" ([PMID: 41977474](https://pubmed.ncbi.nlm.nih.gov/41977474/))
- Limited ICI monotherapy benefit confirmed by meta-analysis of 87 studies ([PMID: 34295687](https://pubmed.ncbi.nlm.nih.gov/34295687/))
- Single-cell sequencing identified RNASE1+ lipid-associated macrophages linked to osimertinib resistance and leptomeningeal metastasis development, "regulated by Midkine (MDK) from malignant epithelial cells." Malignant cells achieved immune evasion through CD47-SIRPA interactions ([PMID: 39116206](https://pubmed.ncbi.nlm.nih.gov/39116206/))

### Molecular Profiling

- **Single-cell analysis**: TraCe-seq identified preexisting transcriptional programs affecting EGFR-TKI response and an essential role of ER protein processing pathway in anti-EGFR therapeutic efficacy ([PMID: 34531539](https://pubmed.ncbi.nlm.nih.gov/34531539/))
- **Proteogenomics**: Never-smoker lung adenocarcinoma without EGFR/ALK shows activated estrogen signaling ([PMID: 38607364](https://pubmed.ncbi.nlm.nih.gov/38607364/))
- **Spatial transcriptomics**: STK24-positive epithelial cells communicate with fibroblasts and endothelial cells via MIF and PDGF pathways ([PMID: 41168822](https://pubmed.ncbi.nlm.nih.gov/41168822/))
- **LINE-1 retrotransposon**: Contributes to genomic evolution in lung adenocarcinoma ([PMID: 41372401](https://pubmed.ncbi.nlm.nih.gov/41372401/))

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organ**: Lung (UBERON:0002048) — predominantly peripheral lung adenocarcinoma
- **Secondary organs** (metastatic sites):
  - Brain (UBERON:0000955) — 25–40% of patients
  - Bone (UBERON:0002481)
  - Liver (UBERON:0002107)
  - Adrenal glands (UBERON:0002369)
  - Pleura (UBERON:0000977) — malignant pleural effusion common
  - Leptomeninges — leptomeningeal metastasis in 3–5%
- **Body systems**: Respiratory system (primary), nervous system, skeletal system, hepatobiliary system

### Tissue and Cell Level

- **Primary tissue**: Pulmonary epithelium (UBERON:0000115)
- **Cell types**:
  - Type II pneumocytes (CL:0002063) — primary cell of origin for adenocarcinoma
  - Club cells (CL:0000158) — alternative cell of origin
  - Cancer-associated fibroblasts
  - Lipid-associated macrophages (RNASE1+ subtype) — drive resistance ([PMID: 39116206](https://pubmed.ncbi.nlm.nih.gov/39116206/))
  - Tumor-infiltrating lymphocytes (sparse in EGFR-mutant tumors)

### Subcellular Level

- **Plasma membrane** (GO:0005886): EGFR receptor localization
- **Cytoplasm** (GO:0005737): RAS-MAPK and PI3K-AKT signaling cascades
- **Nucleus** (GO:0005634): STAT3 and AP-1 transcriptional programs
- **Endoplasmic reticulum** (GO:0005783): ER protein processing pathway involved in TKI efficacy

### Localization

- Peripheral lung fields (most common)
- Upper lobes slightly more common
- Bilateral/multifocal disease possible
- CNS metastases frequently bilateral

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: 55–70 years (median ~62); younger in East Asian populations
- **Onset pattern**: Insidious; often diagnosed at advanced stage (~60% present as stage III/IV)

### Progression and Staging (AJCC 8th Edition)

| Stage | Description | 5-Year DFS (without adj. TKI) | Key Reference |
|---|---|---|---|
| IB | T2a N0 M0 | ~84% | [PMID: 41353641](https://pubmed.ncbi.nlm.nih.gov/41353641/) |
| II | T2b-T3 N0-N1 M0 | ~60-70% | — |
| IIIA | T1-T4 N0-N2 M0 | ~20% | [PMID: 41353641](https://pubmed.ncbi.nlm.nih.gov/41353641/) |
| III (unresectable) | T4 or N3 | Median PFS 12-22 mo with CRT + TKI | — |
| IV | Any T, any N, M1 | Median OS 28-55 mo with TKIs | — |

Real-world Portuguese data showed "the five-year disease-free survival and overall survival rates were 70% and 81%, respectively" for resected EGFR-mutant NSCLC without adjuvant TKI ([PMID: 41353641](https://pubmed.ncbi.nlm.nih.gov/41353641/)).

### Disease Course

- **On first-line osimertinib**: Median PFS ~18.9 months; median OS ~38.6 months (FLAURA)
- **Sequential therapy**: "Sequential afatinib-osimertinib therapy achieved a median OS of 55 months (95% confidence interval [CI] 53.2–66.4) compared to 32.3 months (95% CI 30.3–34.5) with alternative strategies (adjusted hazard ratio 0.43, p < 0.001)" ([PMID: 41862776](https://pubmed.ncbi.nlm.nih.gov/41862776/))
- **Resistance**: Virtually universal; median time to resistance 12–24 months on 3rd-gen TKIs
- **Post-progression**: Median OS 16.38 months with TROP-2 ADCs; median PFS 6.08 months ([PMID: 41443486](https://pubmed.ncbi.nlm.nih.gov/41443486/))

### Critical Periods

- Post-surgical window for adjuvant osimertinib initiation (within 26 weeks)
- T790M testing window at progression on 1st/2nd-gen TKIs
- CNS surveillance throughout disease course given high metastatic propensity

---

## 9. Inheritance and Population

### Epidemiology

EGFR mutation prevalence varies dramatically by ethnicity and geography:

| Population | EGFR Mutation Prevalence | Source |
|---|---|---|
| East Asian | ~30% | [PMID: 21527061](https://pubmed.ncbi.nlm.nih.gov/21527061/) |
| Caucasian | ~7% | [PMID: 21527061](https://pubmed.ncbi.nlm.nih.gov/21527061/) |
| Bangladeshi | 23% | [PMID: 23299280](https://pubmed.ncbi.nlm.nih.gov/23299280/) |
| Moroccan | 14.4% | [PMID: 33079008](https://pubmed.ncbi.nlm.nih.gov/33079008/) |
| Malaysian (resectable) | 62.3% | [PMID: 41617518](https://pubmed.ncbi.nlm.nih.gov/41617518/) |
| French | ~15% | [PMID: 40155080](https://pubmed.ncbi.nlm.nih.gov/40155080/) |
| Egyptian | 20.4% | [PMID: 41327362](https://pubmed.ncbi.nlm.nih.gov/41327362/) |

"Compared with Caucasian patients with NSCLC, East Asian patients have a much higher prevalence of epidermal growth factor receptor (EGFR) mutation (approximately 30% vs. 7%, predominantly among patients with adenocarcinoma and never-smokers)" ([PMID: 21527061](https://pubmed.ncbi.nlm.nih.gov/21527061/)).

### Genetic Etiology Characteristics

- **Inheritance**: Somatic (not inherited); germline susceptibility variants modify risk
- **Penetrance**: Not applicable for somatic driver; germline risk alleles have incomplete penetrance (OR 1.19–1.36)
- **Founder effects**: BIM deletion polymorphism enriched in East Asian populations (~12–18% prevalence vs. <1% in Europeans)

### Population Demographics

- **Sex ratio**: Female predominance (~60–70% of EGFR-mutant cases)
- **Age distribution**: Peak incidence 55–70 years; young patients (<50) have higher frequency of actionable drivers including EGFR, ALK, ROS1, and ERBB2 ([PMID: 41793321](https://pubmed.ncbi.nlm.nih.gov/41793321/))
- **Geographic distribution**: Highest prevalence in East Asia (Japan, China, South Korea, Taiwan); intermediate in South/Southeast Asia; lowest in Northern Europe and North America
- **Never-smoker relevance**: "Asian never smokers have a 2.3-fold higher baseline incidence of lung cancer than non-Asian never smokers, and Asian female never smokers exhibit lung cancer detection rates comparable to Asian male ever smokers" ([PMID: 41932615](https://pubmed.ncbi.nlm.nih.gov/41932615/))

---

## 10. Diagnostics

### Molecular Testing (Standard of Care)

Comprehensive molecular profiling is mandatory for all non-squamous NSCLC at diagnosis:

| Test | Application | Sensitivity | Key Findings |
|---|---|---|---|
| **NGS panel (tissue)** | Gold standard | >95% | Covers exons 18-21; detects co-mutations |
| **PCR-based assays (tissue)** | Targeted EGFR testing | ~95% | Rapid turnaround |
| **Liquid biopsy (ctDNA)** | Tissue unavailable; monitoring | 68-88% | Concordance 82.9% with tissue ([PMID: 35343188](https://pubmed.ncbi.nlm.nih.gov/35343188/)) |
| **Pleural effusion cfDNA** | Enhanced detection with MPE | 88% | Superior to tissue in some settings ([PMID: 39799785](https://pubmed.ncbi.nlm.nih.gov/39799785/)) |

Liquid biopsy concordance: "The concordance between plasma and tissue testing was found to be 82.9% (95% confidence interval [CI]: 77.55, 87.45). The sensitivity and specificity of NGS were 68.4% and 90.1%, respectively" ([PMID: 35343188](https://pubmed.ncbi.nlm.nih.gov/35343188/)).

### Imaging Studies

- **CT chest with contrast**: Primary staging
- **PET-CT**: Systemic staging
- **Brain MRI**: Mandatory at diagnosis and during surveillance
- **LDCT**: Screening (currently limited to smokers; gap for never-smokers)

### Biomarkers

- **Predictive**: EGFR mutation status (TKI response), T790M (osimertinib response), BIM deletion (reduced TKI response), C797S (4th-gen TKI candidates)
- **Prognostic**: TP53 co-mutation (adverse), PD-L1 expression (paradoxically adverse in EGFR-mutant), ctDNA clearance (favorable)
- **MRD detection**: ctDNA-based systems achieving LOD of 0.01% allele fraction ([PMID: 35308511](https://pubmed.ncbi.nlm.nih.gov/35308511/))

### Histopathology

- Predominantly adenocarcinoma (>85%); rarely squamous or adenosquamous
- Immunohistochemistry: TTF-1+, CK7+, Napsin A+
- PD-L1 IHC assessed but paradoxical prognostic significance in EGFR-mutant tumors

### Differential Diagnosis

- KRAS-mutant NSCLC (smoking-associated)
- ALK-rearranged NSCLC (younger never-smokers)
- ROS1-rearranged NSCLC
- HER2-mutant NSCLC (newly targetable with zongertinib; [PMID: 41985129](https://pubmed.ncbi.nlm.nih.gov/41985129/))
- BRAF-mutant NSCLC
- Metastatic adenocarcinoma from other primary sites

---

## 11. Outcome / Prognosis

### Survival

| Setting | Treatment | Median PFS | Median OS | Source |
|---|---|---|---|---|
| Stage IB-IIIA (resected) | Surgery alone | — | 5-yr OS 81% | [PMID: 41353641](https://pubmed.ncbi.nlm.nih.gov/41353641/) |
| Stage IB-IIIA (resected) | Surgery + adj. osimertinib | Significantly improved DFS | Significant OS benefit | ADAURA |
| Stage III (unresectable) | CRT + osimertinib | NR vs 3.7 mo (HR 0.16) | Immature | [PMID: 41785639](https://pubmed.ncbi.nlm.nih.gov/41785639/) |
| Stage IV (1L) | Osimertinib | ~18.9 months | ~38.6 months | FLAURA |
| Stage IV (1L) | Afatinib | ~11.0 months | 28.8 months | [PMID: 41223879](https://pubmed.ncbi.nlm.nih.gov/41223879/) |
| Stage IV (1L) | Gefitinib | — | 25.3 months | [PMID: 41223879](https://pubmed.ncbi.nlm.nih.gov/41223879/) |
| Stage IV (sequential) | Afatinib → osimertinib | — | 55 months | [PMID: 41862776](https://pubmed.ncbi.nlm.nih.gov/41862776/) |
| Post-TKI (2L+) | Sacituzumab tirumotecan | HR 0.49 vs chemo | HR 0.60 vs chemo | [PMID: 41520595](https://pubmed.ncbi.nlm.nih.gov/41520595/) |

### Prognostic Factors

- **Favorable**: Exon 19 deletion (vs L858R), younger age, good PS (ECOG 0-1), absence of CNS metastases, ctDNA clearance, smaller PTV (<450 cc for stage III)
- **Adverse**: TP53 co-mutation, high PD-L1 (≥50%), BIM deletion polymorphism, positive pleural lavage cytology (HR 2.13 for RFS; [PMID: 41145016](https://pubmed.ncbi.nlm.nih.gov/41145016/)), smoking history (for ILD risk)

### Complications

- Brain metastases (25–40%); leptomeningeal metastases (3–5%)
- Malignant pleural effusion
- Treatment-related ILD (3.7% TKI-induced)
- Skeletal-related events from bone metastases
- Treatment-related dermatologic, GI, and hepatic toxicities

---

## 12. Treatment

### Treatment Algorithm

{{figure:treatment_algorithm.png|caption=Treatment algorithm for EGFR-mutant NSCLC across disease stages showing standard of care and emerging combination strategies}}

### First-Line Metastatic Treatment

**Standard of care: Osimertinib** (MAXO:0000058 — pharmacotherapy)

"Osimertinib demonstrates superior efficacy across multiple endpoints in patients with EGFR-mutant" NSCLC — meta-analysis of 16 studies (4,931 patients): ORR RR = 1.59 (95% CI 1.16–2.17) ([PMID: 41907704](https://pubmed.ncbi.nlm.nih.gov/41907704/)).

**Emerging first-line combinations:**

| Regimen | Trial | Key Efficacy | Toxicity Consideration |
|---|---|---|---|
| Osimertinib + platinum-pemetrexed | FLAURA2 | Improved PFS | Higher hematologic toxicity |
| Amivantamab + lazertinib | MARIPOSA | PFS and OS benefit | Cutaneous, edema, infusion reactions |
| EGFR TKI + bevacizumab | BIM-CLICaP | Particularly beneficial in BIM-del patients | Anti-VEGF AEs |

"EGFR-TKIs plus Bev conferred a significantly higher ORR and PFS in advanced NSCLC patients with EGFR mutation and BIMdel" ([PMID: 34994616](https://pubmed.ncbi.nlm.nih.gov/34994616/)).

### Perioperative Treatment

**Adjuvant osimertinib** (ADAURA) is the reference standard: "adjuvant osimertinib now representing the most mature perioperative strategy because it has demonstrated durable disease-free survival, overall survival, and central nervous system (CNS) benefit in ADAURA" ([PMID: 42033967](https://pubmed.ncbi.nlm.nih.gov/42033967/)).

### Unresectable Stage III

**CRT + consolidation osimertinib** (LAURA): In the China cohort, "median BICR-assessed PFS was not reached (17.4–not calculable) versus 3.7 months (1.8–7.7) with osimertinib versus placebo" ([PMID: 41785639](https://pubmed.ncbi.nlm.nih.gov/41785639/)).

### CNS-Directed Therapy

{{figure:plot_5.png|caption=CNS metastasis management algorithm and the critical screening gap for never-smokers with EGFR mutations showing osimertinib CNS response rates and unscreened high-risk populations}}

"Osimertinib penetrates the blood-brain barrier and achieves greater exposure in the brain compared with other EGFR-TKIs" ([PMID: 36652172](https://pubmed.ncbi.nlm.nih.gov/36652172/)). Meta-analysis: "the overall response rate (ORR) and disease control rate (DCR) were 70% and 92%, respectively, in patients with T790M mutations" with CNS metastases; ORR 71% and DCR 93% in untreated advanced EGFR+ NSCLC with CNS metastases; median PFS 12.21 months ([PMID: 32954743](https://pubmed.ncbi.nlm.nih.gov/32954743/)).

### Post-Resistance Strategies

| Agent/Regimen | Mechanism | Key Data |
|---|---|---|
| **Sacituzumab tirumotecan** | TROP-2 ADC | HR 0.49 (PFS), HR 0.60 (OS) vs chemo; "significantly improved OS over chemo-immunotherapy (HR 0.68)" ([PMID: 41520595](https://pubmed.ncbi.nlm.nih.gov/41520595/)) |
| **Amivantamab + chemotherapy** | EGFR-MET bsAb + chemo | HR 0.48 (PFS) vs chemo |
| **Datopotamab deruxtecan** | TROP-2 ADC | Meaningful efficacy; EGFR-mutated subgroup response ratio 1.70 ([PMID: 41443486](https://pubmed.ncbi.nlm.nih.gov/41443486/)) |
| **Vabametkib + lazertinib** | MET TKI + EGFR TKI | Synergistic in MET-amplified PDX models; phase II ongoing (NCT05541822) ([PMID: 41927036](https://pubmed.ncbi.nlm.nih.gov/41927036/)) |
| **4th-gen TKIs** (BDTX-1535, JIN-A02, HS-10504) | Allosteric EGFR inhibitors | Phase I/II for L858R/T790M/C797S ([PMID: 40667612](https://pubmed.ncbi.nlm.nih.gov/40667612/)) |
| **Ivonescimab** | PD-1/VEGFA bispecific | Case reports of benefit in complex resistance ([PMID: 41479892](https://pubmed.ncbi.nlm.nih.gov/41479892/)) |

For C797S-positive patients: "chemotherapy-based therapies demonstrated superior PFS vs non-chemotherapy (5.5 vs 3.4 months, p=0.014)" ([PMID: 41430586](https://pubmed.ncbi.nlm.nih.gov/41430586/)).

### Pharmacogenomics

- **BIM deletion polymorphism**: "BIM deletion polymorphism may confer resistance to EGFR-TKIs and can be used as a biomarker to predict treatment response to EGFR-TKIs in EGFR-mutant NSCLC patients from Asian populations" ([PMID: 34722761](https://pubmed.ncbi.nlm.nih.gov/34722761/)). Resminostat (HDAC inhibitor) can circumvent BIM-del-associated apoptosis resistance in preclinical models ([PMID: 33148913](https://pubmed.ncbi.nlm.nih.gov/33148913/)).
- **Lazertinib**: Potentially cardio-safer alternative to osimertinib with "superior selectivity for mutant EGFR while sparing wild-type EGFR" ([PMID: 40919674](https://pubmed.ncbi.nlm.nih.gov/40919674/))

---

## 13. Prevention

### Primary Prevention

- Smoking avoidance (although EGFR-mutant NSCLC predominantly affects never-smokers)
- Environmental exposure reduction: radon mitigation, air quality improvements, cooking ventilation
- Occupational safety regulations

### Secondary Prevention (Screening)

**Critical unmet need**: "never smokers remain excluded from current screening guidelines despite rising incidence and identifiable high-risk subgroups" ([PMID: 41932615](https://pubmed.ncbi.nlm.nih.gov/41932615/)). Evidence supporting expanded screening:
- Family history confers 1.7-fold higher incidence
- "Asian never smokers have a 2.3-fold higher baseline incidence of lung cancer than non-Asian never smokers"
- "Screening trials in never smokers demonstrated detection rates comparable to smoker-based trials, suggesting certain demographic subgroups may reach risk thresholds where screening could be beneficial"

### Tertiary Prevention

- **Adjuvant osimertinib**: Prevents recurrence in resected stage IB-IIIA
- **Consolidation osimertinib**: Prevents progression after CRT for unresectable stage III
- **ctDNA-based MRD monitoring**: Enables early detection of recurrence
- **Regular brain MRI surveillance**: Detects asymptomatic CNS metastases early

---

## 14. Other Species / Natural Disease

### Comparative Biology

- **EGFR ortholog** (highly conserved): Mouse *Egfr* (NCBI Gene: 13649); Rat *Egfr* (NCBI Gene: 24329); Zebrafish *egfra* (NCBI Gene: 378478); *Drosophila* *Egfr/DER* (FlyBase: FBgn0003731)
- Spontaneous EGFR-mutant lung tumors are not well documented in companion animals
- The EGFR kinase domain is >90% conserved between human and mouse, supporting murine model utility
- Canine pulmonary adenocarcinoma shares histological features with human NSCLC but EGFR mutation status is rarely characterized

---

## 15. Model Organisms

### Mouse Models

| Model | Type | Key Features | Limitations |
|---|---|---|---|
| EGFR L858R transgenic | Conditional knock-in | Develops lung adenocarcinoma; TKI-sensitive | Single mutation; no tumor heterogeneity |
| EGFR exon 19 del | Conditional knock-in | Recapitulates human exon 19 deletion tumors | Limited immune microenvironment modeling |
| EGFR T790M/L858R | Compound knock-in | Models acquired resistance | Does not fully recapitulate all resistance mechanisms |
| PDX models | Patient-derived xenograft | Preserves tumor heterogeneity; used for drug testing (e.g., vabametkib + lazertinib [PMID: 41927036](https://pubmed.ncbi.nlm.nih.gov/41927036/)) | Immunodeficient host |

### Cell Line Models

| Cell Line | EGFR Status | Key Application |
|---|---|---|
| **PC-9** | Exon 19 deletion | TKI sensitivity; BIM-del studies ([PMID: 33148913](https://pubmed.ncbi.nlm.nih.gov/33148913/)) |
| **HCC827** | Exon 19 deletion (amplified) | Resistance modeling; CRISPR screens ([PMID: 40414926](https://pubmed.ncbi.nlm.nih.gov/40414926/)) |
| **NCI-H1975** | L858R/T790M | Third-generation TKI testing |
| **PC-9 BIMi2-/-** | Exon 19 del + BIM-del (engineered) | Pharmacogenomic studies |

### Advanced Model Systems

- **Patient-derived organoids**: Used for drug sensitivity testing
- **CRISPR functional genomics screens**: Identified AP-1/NuRD/PRC2 resistance network ([PMID: 40414926](https://pubmed.ncbi.nlm.nih.gov/40414926/))
- **TraCe-seq**: Tracked clonal differential responses to EGFR inhibitors ([PMID: 34531539](https://pubmed.ncbi.nlm.nih.gov/34531539/))
- **3D collagen spheroid models**: Evaluated invasive phenotypes in TKI-resistant cells ([PMID: 42087187](https://pubmed.ncbi.nlm.nih.gov/42087187/))
- **Single-cell CTC analysis**: Demonstrated inter- and intra-patient heterogeneity in EGFR mutation status and gene expression ([PMID: 32700450](https://pubmed.ncbi.nlm.nih.gov/32700450/))

---

## Key Findings Summary

### F1: Ethnic Variation in EGFR Mutation Prevalence
EGFR mutation prevalence varies dramatically by ethnicity: approximately 30% in East Asians versus ~7% in Caucasians, with intermediate rates in South Asian (23%) and North African (14.4%) populations ([PMID: 21527061](https://pubmed.ncbi.nlm.nih.gov/21527061/); [PMID: 23299280](https://pubmed.ncbi.nlm.nih.gov/23299280/)).

### F2: Osimertinib as Standard First-Line Treatment
Osimertinib demonstrates superior ORR, PFS, and OS versus earlier-generation TKIs. Sequential afatinib → osimertinib achieves median OS of 55 months ([PMID: 41907704](https://pubmed.ncbi.nlm.nih.gov/41907704/); [PMID: 41862776](https://pubmed.ncbi.nlm.nih.gov/41862776/)).

### F3: C797S as Primary On-Target Resistance to Osimertinib
C797S is the most common on-target resistance mechanism, with diverse bypass mechanisms. Fourth-generation TKIs are in clinical development ([PMID: 37060646](https://pubmed.ncbi.nlm.nih.gov/37060646/); [PMID: 41430586](https://pubmed.ncbi.nlm.nih.gov/41430586/)).

### F4: Paradoxical Immune Microenvironment
High PD-L1 (≥50%) paradoxically predicts shorter PFS (HR 3.03) and OS on osimertinib, representing a biologically distinct phenotype ([PMID: 41977474](https://pubmed.ncbi.nlm.nih.gov/41977474/); [PMID: 41371099](https://pubmed.ncbi.nlm.nih.gov/41371099/)).

### F5: Superior CNS Efficacy of Osimertinib
CNS ORR of 70–71% with several-fold higher BBB penetration than other EGFR-TKIs. Adjuvant osimertinib reduces CNS recurrence ([PMID: 32954743](https://pubmed.ncbi.nlm.nih.gov/32954743/); [PMID: 36652172](https://pubmed.ncbi.nlm.nih.gov/36652172/)).

### F6: Lineage Plasticity as Resistance Mechanism
Epigenetic reprogramming enables histologic transformation (adenocarcinoma → SCLC). TP53/RB1 co-mutations predispose to this transformation ([PMID: 41516316](https://pubmed.ncbi.nlm.nih.gov/41516316/)).

### F7: Lipid-Associated Macrophages in CNS Resistance
RNASE1+ lipid-associated macrophages regulated by Midkine drive osimertinib resistance and leptomeningeal metastasis via CD47-SIRPA interactions ([PMID: 39116206](https://pubmed.ncbi.nlm.nih.gov/39116206/)).

### F8: ADAURA Adjuvant Standard
Adjuvant osimertinib provides durable DFS, OS, and CNS recurrence benefit for resected stage IB-IIIA EGFR-mutant NSCLC ([PMID: 42033967](https://pubmed.ncbi.nlm.nih.gov/42033967/); [PMID: 41353641](https://pubmed.ncbi.nlm.nih.gov/41353641/)).

### F9: TCGA Mutation Distribution Confirmed
L858R (26.7%), exon 19 deletions (23.3%), uncommon sensitizing (11.6%), T790M (2.3%) in TCGA LUAD cohort.

### F10: GWAS Susceptibility Loci
Six germline loci identified, with HLA class II (OR 1.36) and FOXP4 (OR 1.19) specifically associated with EGFR mutation-positive tumors ([PMID: 27501781](https://pubmed.ncbi.nlm.nih.gov/27501781/)).

### F11: EGFR TKI Adverse Event Profile
Class-specific toxicities documented across 34 RCTs: dermatologic, GI, hepatic, and respiratory AEs. ILD rare but potentially fatal ([PMID: 38824269](https://pubmed.ncbi.nlm.nih.gov/38824269/)).

### F12: Never-Smoker Genomic Landscape
Distinct mutational signatures (clock-like, APOBEC) with high EGFR mutation prevalence and unique allelic differences by smoking status ([PMID: 39052387](https://pubmed.ncbi.nlm.nih.gov/39052387/); [PMID: 41617518](https://pubmed.ncbi.nlm.nih.gov/41617518/)).

### F13: Never-Smoker Screening Gap
Asian never-smokers have 2.3-fold higher incidence; screening trials show comparable detection rates to smoker-based programs, yet never-smokers remain excluded from guidelines ([PMID: 41932615](https://pubmed.ncbi.nlm.nih.gov/41932615/)).

### F14: Germline DNA Repair Gene Contributions
ATM, BRCA1/2, TP53, PALB2, CHEK2 germline mutations contribute to NSCLC susceptibility with prognostic and predictive implications ([PMID: 41933854](https://pubmed.ncbi.nlm.nih.gov/41933854/)).

### F15: Osimertinib CNS Efficacy Quantified
Pooled ORR 70%, DCR 92% in T790M+ CNS metastases; ORR 71%, DCR 93% in untreated CNS metastases; median PFS 12.21 months ([PMID: 32954743](https://pubmed.ncbi.nlm.nih.gov/32954743/)).

### F16: BIM Deletion as Pharmacogenomic Modifier
Present in 15.8% of Asian EGFR-mutant patients; predicts shorter PFS (HR 1.35); bevacizumab addition overcomes resistance ([PMID: 34722761](https://pubmed.ncbi.nlm.nih.gov/34722761/); [PMID: 34994616](https://pubmed.ncbi.nlm.nih.gov/34994616/)).

### F17: AP-1 as Targetable Resistance Mediator
CRISPR screen identified FOSL1/JUN (AP-1) as top resistance mediators via epigenetic reprogramming; pharmacological inhibition reinstates sensitivity ([PMID: 40414926](https://pubmed.ncbi.nlm.nih.gov/40414926/)).

---

## Mechanistic Model

```
GERMLINE SUSCEPTIBILITY              ENVIRONMENTAL EXPOSURE
(HLA class II, TERT, TP63,          (Radon, air pollution, cooking
 FOXP4, BIM-del polymorphism)         fumes, APOBEC mutagenesis)
           │                                    │
           └──────────────┬─────────────────────┘
                          ▼
              SOMATIC EGFR MUTATION
         (Exon 19 del / L858R / others)
                          │
                          ▼
           CONSTITUTIVE EGFR KINASE ACTIVITY
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
      RAS-MAPK-ERK   PI3K-AKT-mTOR  JAK-STAT3
           │              │              │
           ▼              ▼              ▼
    Proliferation    Anti-apoptosis  Immune evasion
    Cell survival    Metabolism      Low TMB, cold TME
                                    Paradoxical PD-L1
                          │
                          ▼
              LUNG ADENOCARCINOMA
        (Stage I-IV at presentation)
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
      Local growth   CNS metastasis  Systemic mets
                    (25-40%)        (bone, liver,
                                     adrenal, pleura)
                          │
                          ▼
              EGFR TKI TREATMENT
        (1st/2nd/3rd generation)
                          │
                          ▼
              ACQUIRED RESISTANCE
           ┌──────────┬──────────┬──────────┐
           ▼          ▼          ▼          ▼
       On-target   Bypass    Histologic  Epigenetic
       (T790M,     (MET amp, (SCLC      (AP-1/NuRD/
        C797S)      fusions)  transform)  PRC2)
           │
           ▼
    NEXT-LINE THERAPY
    (4th-gen TKIs, ADCs, bsAbs,
     MET inhibitors, combinations)
```

---

## Evidence Base

This report synthesizes 104 publications across multiple evidence types:

| Evidence Type | Count | Key Examples |
|---|---|---|
| Meta-analyses | ~10 | TKI efficacy ([PMID: 41907704](https://pubmed.ncbi.nlm.nih.gov/41907704/)), AE profiles ([PMID: 38824269](https://pubmed.ncbi.nlm.nih.gov/38824269/)), BIM-del ([PMID: 34722761](https://pubmed.ncbi.nlm.nih.gov/34722761/)), CNS ([PMID: 32954743](https://pubmed.ncbi.nlm.nih.gov/32954743/)), post-TKI ([PMID: 41520595](https://pubmed.ncbi.nlm.nih.gov/41520595/)) |
| Landmark clinical trials | ~8 | FLAURA, ADAURA, LAURA, MARIPOSA, PAPILLON, PACIFIC |
| GWAS | 1 | Japanese EGFR-mutant LUAD susceptibility ([PMID: 27501781](https://pubmed.ncbi.nlm.nih.gov/27501781/)) |
| Single-cell/spatial studies | ~5 | Lipid-associated macrophages ([PMID: 39116206](https://pubmed.ncbi.nlm.nih.gov/39116206/)), TraCe-seq ([PMID: 34531539](https://pubmed.ncbi.nlm.nih.gov/34531539/)), STK24 ([PMID: 41168822](https://pubmed.ncbi.nlm.nih.gov/41168822/)) |
| CRISPR screens | 1 | AP-1 resistance network ([PMID: 40414926](https://pubmed.ncbi.nlm.nih.gov/40414926/)) |
| Real-world cohorts | ~15 | South Korea, Taiwan, Portugal, India, Italy, China, Malaysia, Morocco, Bangladesh, Egypt |
| Genomic database analyses | ~5 | TCGA/cBioPortal, KEGG, COSMIC |
| Liquid biopsy studies | ~10 | ctDNA concordance, MRD detection, cfDNA monitoring |
| Review articles | ~25 | Treatment algorithms, resistance mechanisms, screening |

---

## Limitations and Knowledge Gaps

1. **Limited diversity in genomic studies**: Most GWAS data from East Asian populations; susceptibility loci in African and Latin American populations remain undefined
2. **Resistance heterogeneity**: Post-osimertinib resistance mechanisms are diverse and often co-occurring; comprehensive profiling at resistance is not routinely performed
3. **Immunotherapy optimization**: Optimal strategy to overcome the immunologically cold microenvironment remains unclear; clinical trials of ICI + TKI combinations show mixed results with increased toxicity
4. **Never-smoker screening**: No large randomized trial has established LDCT screening benefits specifically in never-smoker populations
5. **Biomarker gaps**: Predictive biomarkers for choosing between first-line strategies (osimertinib monotherapy vs. FLAURA2 vs. MARIPOSA) are lacking
6. **Treatment sequencing**: Optimal post-progression sequencing after front-line combination therapy is undefined
7. **Long-term survivorship**: Data on 10-year outcomes with sequential TKI strategies are limited
8. **Epigenetic resistance translation**: Clinical development of AP-1 targeting and epigenetic therapies remains at early stages
9. **Rare mutations**: Optimal treatment for uncommon EGFR mutations (exon 20 insertions, compound mutations) continues to evolve
10. **Health equity**: Access to molecular testing, novel therapies, and clinical trials varies significantly between high- and low-resource settings

---

## Proposed Follow-up Experiments / Actions

### High Priority

1. **Never-smoker screening trials**: Randomized LDCT screening studies in high-risk never-smoker populations (Asian women, family history positive), incorporating ctDNA and AI-enhanced imaging
2. **Resistance mechanism profiling**: Systematic tissue and liquid biopsy at progression on first-line osimertinib-based combinations to define resistance patterns
3. **AP-1 targeting clinical trials**: Develop and test AP-1 pharmacological inhibitors in combination with osimertinib for epigenetic resistance
4. **BIM-del prospective validation**: Pharmacogenomic trial of BIM deletion-guided therapy selection (standard TKI vs. TKI + bevacizumab vs. TKI + HDAC inhibitor)

### Medium Priority

5. **Biomarker-driven treatment selection**: Develop composite biomarkers (mutation subtype, co-mutations, ctDNA dynamics, BIM-del) to guide first-line intensity
6. **Microenvironment-directed therapy**: Clinical trials targeting MDK/RNASE1+ macrophages combined with osimertinib for CNS disease
7. **Fourth-generation TKI development**: Accelerate BDTX-1535 and JIN-A02 clinical trials for C797S-positive patients
8. **Multi-ethnic GWAS**: Expand to African, Latin American, and Middle Eastern populations

### Lower Priority

9. **Organoid biobanks**: Establish diverse PDO biobanks representing all mutation subtypes and resistance mechanisms
10. **Prevention studies**: Evaluate radon mitigation and air quality interventions in high-risk never-smoker communities

---

## Ontology Summary

| Category | Term | ID |
|---|---|---|
| Disease | Non-small cell lung carcinoma | MONDO:0005233 |
| Disease | Lung adenocarcinoma | MONDO:0008903 |
| Gene | EGFR | HGNC:3236 |
| Gene | TP53 | HGNC:11998 |
| Gene | BCL2L11 (BIM) | HGNC:994 |
| Phenotype | Neoplasm of the lung | HP:0100526 |
| Phenotype | Cough | HP:0012735 |
| Phenotype | Dyspnea | HP:0002094 |
| Cell type | Type II pneumocyte | CL:0002063 |
| Cell type | Macrophage | CL:0000235 |
| Anatomy | Lung | UBERON:0002048 |
| Anatomy | Brain | UBERON:0000955 |
| Pathway | EGFR signaling | GO:0007173 |
| Pathway | MAPK cascade | GO:0000165 |
| Pathway | PI3K-AKT signaling | KEGG:hsa04151 |
| Process | Cell proliferation | GO:0008283 |
| Process | Apoptotic process | GO:0006915 |
| Process | EMT | GO:0001837 |
| Chemical | Osimertinib | CHEBI:90943 |
| Chemical | Gefitinib | CHEBI:49668 |
| Chemical | Erlotinib | CHEBI:114785 |
| Treatment | Pharmacotherapy | MAXO:0000058 |
| Treatment | Surgical resection | MAXO:0000004 |
| Treatment | Radiation therapy | MAXO:0000015 |
| Treatment | Genetic testing | MAXO:0000127 |

---

*Report generated from 5 iterations of autonomous investigation, 17 confirmed findings, and 104 reviewed publications. Last updated: 2026-05-06.*
