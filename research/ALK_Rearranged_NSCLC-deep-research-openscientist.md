---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-06T01:23:42.019631'
end_time: '2026-05-06T02:08:06.407062'
duration_seconds: 2664.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALK-Rearranged Non-Small Cell Lung Cancer
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
citation_count: 69
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALK-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **ALK-Rearranged Non-Small Cell Lung Cancer** covering all of the
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

# Comprehensive Disease Characterization: ALK-Rearranged Non-Small Cell Lung Cancer

## Summary

ALK-rearranged non-small cell lung cancer (ALK+ NSCLC) is a molecularly defined subset of lung adenocarcinoma driven by somatic chromosomal rearrangements involving the anaplastic lymphoma kinase (ALK) gene on chromosome 2p23, most commonly fused with the echinoderm microtubule-associated protein-like 4 (EML4) gene via a small paracentric inversion inv(2)(p21p23). Representing 3–7% of all NSCLC cases, this disease preferentially affects younger patients (median age 55–60 years), never-smokers (60–70%), and those with adenocarcinoma histology. The constitutively active EML4-ALK fusion kinase drives oncogenesis through RAS-MAPK, PI3K-AKT, JAK-STAT, and PLCgamma signaling pathways, orchestrated within phase-separated cytoplasmic signaling foci, while simultaneously fostering an immune-cold tumor microenvironment characterized by low tumor mutational burden (TMB) and CD73/adenosine-mediated immune evasion.

The therapeutic landscape has been transformed by three generations of ALK tyrosine kinase inhibitors (TKIs). First-generation crizotinib (approved 2011) has been superseded by second-generation agents (alectinib, brigatinib, ceritinib, ensartinib) and the third-generation lorlatinib, which achieved an unprecedented 5-year progression-free survival (PFS) of 60%+ in the CROWN trial with a 96% probability of preventing brain metastases. Median overall survival now exceeds 6 years (81 months in sequential TKI-treated cohorts). However, resistance remains inevitable through secondary ALK mutations (G1202R, compound mutations), bypass signaling (EGFR, AXL, SRC, YAP), and tumor microenvironment adaptation. Key prognostic modifiers include EML4-ALK variant type (variant 3 worse than variant 1; HR=1.53), TP53 co-mutation status, and intra-tumoral fusion isoform heterogeneity.

This report synthesizes 22 confirmed findings from 129 reviewed papers across all 15 disease characterization domains, providing comprehensive ontology annotations (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO), clinical evidence with PMIDs, and actionable insights for clinical practice and future research.

---

## 1. Disease Information

### Overview

ALK-rearranged NSCLC is a genomically defined subtype of non-small cell lung cancer characterized by somatic rearrangements of the ALK gene that produce constitutively active fusion proteins, most commonly EML4-ALK. First identified in 2007 by Soda et al., the EML4-ALK fusion gene results from "a small inversion within chromosome 2p [that] results in the formation of a fusion gene comprising portions of the echinoderm microtubule-associated protein-like 4 (EML4) gene and the anaplastic lymphoma kinase (ALK) gene in non-small-cell lung cancer (NSCLC) cells" ([PMID: 17625570](https://pubmed.ncbi.nlm.nih.gov/17625570/)). This landmark discovery established EML4-ALK as a transforming oncogene, as mouse 3T3 fibroblasts expressing the fusion generated transformed foci in culture and subcutaneous tumors in nude mice.

ALK-rearranged NSCLC is recognized as an "oncogene-addicted cancer with peculiar clinical characteristics" ([PMID: 39160676](https://pubmed.ncbi.nlm.nih.gov/39160676/)), making it exquisitely sensitive to ALK-targeted therapy but largely resistant to immune checkpoint inhibitors.

### Key Identifiers

| Database | Identifier | Term |
|----------|-----------|------|
| NCIT | C215346 | ALK-Positive Lung Non-Small Cell Carcinoma |
| MONDO | 0005233 | Non-small cell lung carcinoma |
| MONDO | 0005061 | Lung adenocarcinoma |
| SNOMED CT | 254637007 | Non-small cell lung cancer |
| ICD-10 | C34 | Malignant neoplasm of bronchus and lung |
| MeSH | D002289 | Carcinoma, Non-Small-Cell Lung |
| KEGG | hsa05223 | Non-small cell lung cancer pathway |
| OMIM | 164731 | ALK gene |

### Common Synonyms

- ALK-positive NSCLC / ALK+ NSCLC
- ALK-rearranged lung cancer
- EML4-ALK fusion lung cancer
- ALK-translocated NSCLC
- ALK fusion-positive lung adenocarcinoma

### Information Sources

This characterization is derived from aggregated disease-level resources including clinical trial data (CROWN, ALEX, ALINA, ALTA-1L), real-world cohort studies, systematic reviews, and molecular biology research, rather than individual patient EHR data.

---

## 2. Etiology

### Disease Causal Factors

The primary cause is a somatic chromosomal rearrangement — specifically, a paracentric inversion within chromosome 2p — that fuses the N-terminal portion of EML4 (chr2p21) with the kinase domain of ALK (chr2p23). This creates a constitutively active fusion tyrosine kinase. The rearrangement is exclusively somatic (not inherited) and represents a classic oncogenic driver mutation.

**Gene Information:**
- **ALK** (Anaplastic Lymphoma Kinase): HGNC:427, Ensembl:ENSG00000171094, UniProt:Q9UM73, NCBI Gene:238, chr2p23.2-p23.1
- **EML4** (Echinoderm Microtubule Associated Protein Like 4): HGNC:1316, Ensembl:ENSG00000143924, chr2p21

### Risk Factors

#### Genetic Risk Factors

- **Somatic EML4-ALK fusion**: The defining oncogenic event; detected in 5–7% of adenocarcinomas ([PMID: 22129856](https://pubmed.ncbi.nlm.nih.gov/22129856/))
- **TP53 co-mutations**: Present in ~20% of ALK+ cases, associated with dramatically worse outcomes (V3+TP53: HR=9.1 for death, p=0.02) ([PMID: 30255938](https://pubmed.ncbi.nlm.nih.gov/30255938/))
- **EML4-ALK variant type**: V3 confers worse prognosis than V1 (HR=1.53, 95%CI: 1.17–1.99, p=0.002) ([PMID: 41959926](https://pubmed.ncbi.nlm.nih.gov/41959926/))
- **Intra-tumoral fusion isoform heterogeneity**: 47.1% harbor multiple isoforms; associated with worse PFS (HR=2.45) and OS (HR=3.74) ([PMID: 34626839](https://pubmed.ncbi.nlm.nih.gov/34626839/))
- No known germline susceptibility loci specifically for ALK rearrangement

#### Environmental Risk Factors

ALK-rearranged NSCLC predominantly occurs in never-smokers, distinguishing it from smoking-associated NSCLC. Environmental risk factors for lung cancer in never-smokers (LCINS) include:

- **Radon exposure**: OR=1.73 (95%CI: 1.27–2.35) for exposure >=200 Bq/m3 ([PMID: 30903971](https://pubmed.ncbi.nlm.nih.gov/30903971/))
- **Air pollution**: Ambient and indoor air pollution
- **Secondhand smoke**: Passive tobacco smoke exposure
- **Occupational exposures**: Various industrial carcinogens
- **Infectious agents**: Mycobacterium tuberculosis and HPV have been implicated ([PMID: 32062313](https://pubmed.ncbi.nlm.nih.gov/32062313/))
- **Cooking fume exposure**: Particularly in Asian populations without adequate ventilation

LCINS "constitutes a growing global health challenge, accounting for 10%–25% of lung cancer cases and ranking as the fifth leading cause of cancer-related death worldwide" ([PMID: 41591250](https://pubmed.ncbi.nlm.nih.gov/41591250/)).

#### Demographic Enrichment

ALK rearrangement is significantly enriched in:
- Adenocarcinomas (6.8%, p<0.001)
- Younger patients (p<0.0007)
- Women (7.6%, p<0.001)
- Never-smokers (8.9%, p<0.001)

([PMID: 22129856](https://pubmed.ncbi.nlm.nih.gov/22129856/))

### Protective Factors

- No specific genetic protective variants for ALK rearrangement have been identified
- General lung cancer risk reduction through radon mitigation, avoidance of secondhand smoke, and cooking ventilation is relevant given the never-smoker predominance

### Gene-Environment Interactions

Radon exposure has been linked to genetic alterations in ABL2, SMARCA4, PIK3R2, and MAPK1 in never-smoker lung cancers ([PMID: 30008631](https://pubmed.ncbi.nlm.nih.gov/30008631/)). Whether these interact specifically with ALK rearrangement susceptibility remains unknown.

---

## 3. Phenotypes

### Clinical Symptoms and Signs

| Phenotype | HPO Term | Type | Frequency | Severity | Progression |
|-----------|----------|------|-----------|----------|-------------|
| Lung neoplasm | HP:0100526 | Clinical sign | 100% | Variable | Progressive |
| Cough | HP:0012735 | Symptom | 50–75% | Mild to severe | Progressive |
| Dyspnea | HP:0002094 | Symptom | 30–60% | Moderate to severe | Progressive |
| Hemoptysis | HP:0002105 | Symptom | 20–30% | Variable | Episodic |
| Weight loss | HP:0001824 | Symptom | 30–50% | Moderate | Progressive |
| Chest pain | HP:0100749 | Symptom | 20–40% | Variable | Progressive |
| Pleural effusion | HP:0002202 | Clinical sign | 20–35% | Moderate to severe | Progressive |
| Brain metastases | HP:0100634 | Clinical sign | 29% at diagnosis | Severe | Progressive |
| Fatigue | HP:0012378 | Symptom | 40–60% | Moderate | Progressive |

### Age of Onset

- **Typical onset**: Adult, median age 55–60 years
- Young patients (<50 years): 14.2% of ALK+ cases, median age 44 years ([PMID: 31894386](https://pubmed.ncbi.nlm.nih.gov/31894386/))
- Onset pattern: Insidious; many patients diagnosed at advanced stage

### Distinctive Features

ALK+ NSCLC patients are younger than typical NSCLC: "The median age was 55 years (IQR, 45–67); 86% had Eastern Cooperative Oncology Group <=1, 58% were women, and 57% were nonsmokers. Brain metastases were present at diagnosis in 29%" ([PMID: 41043103](https://pubmed.ncbi.nlm.nih.gov/41043103/)).

### Quality of Life Impact

Brain metastases (cumulative incidence >50%) significantly impair quality of life, causing neurological symptoms, cognitive decline, and functional dependence. ALK TKI treatment substantially improves QoL: the Cochrane analysis demonstrated "ALK inhibitors result in a large increase in the HRQoL measure, time to deterioration (HR 0.52, 95% CI: 0.44 to 0.60)" compared to chemotherapy ([PMID: 34994987](https://pubmed.ncbi.nlm.nih.gov/34994987/)).

---

## 4. Genetic/Molecular Information

### Causal Genes

**ALK (Anaplastic Lymphoma Kinase)**
- HGNC: 427
- OMIM: 105590 (gene), 164731 (ALK)
- Ensembl: ENSG00000171094
- UniProt: Q9UM73
- Chromosomal location: chr2:29,192,774–29,921,586 (GRCh38)
- Normal function: Neuronal receptor tyrosine kinase "essentially and transiently expressed in specific regions of the CNS and PNS, playing important roles in genesis and differentiation of the nervous system" ([PMID: 40813394](https://pubmed.ncbi.nlm.nih.gov/40813394/))

**EML4 (Echinoderm Microtubule Associated Protein Like 4)**
- HGNC: 1316
- Ensembl: ENSG00000143924
- Chromosomal location: chr2:42,169,330–42,332,548 (GRCh38)

### Pathogenic Variants

#### Fusion Variants

The EML4-ALK fusion occurs through a paracentric inversion on chromosome 2p with multiple breakpoints in EML4 producing distinct variants:

| Variant | EML4 Exon–ALK Exon | Frequency | Clinical Significance |
|---------|---------------------|-----------|----------------------|
| V1 (E13;A20) | Exon 13–Exon 20 | ~35% | Better prognosis, HSP90-dependent |
| V2 (E20;A20) | Exon 20–Exon 20 | ~10% | Intermediate |
| V3a/b (E6;A20) | Exon 6–Exon 20 | ~35–45% | Worse prognosis, more resistance |

**V3 biological basis**: "The presence of a partial, probably misfolded beta-propeller domain in variant 1 confers solid-like properties to the compartments it forms, greater dependence on Hsp90 for protein stability and higher cell sensitivity to ALK tyrosine kinase inhibitors (TKIs)" ([PMID: 37149843](https://pubmed.ncbi.nlm.nih.gov/37149843/)).

#### Resistance Mutations (Somatic, Acquired)

| Mutation | Type | Resistance Pattern |
|----------|------|-------------------|
| L1196M | Gatekeeper | Crizotinib-resistant |
| G1202R | Solvent front | Pan-resistant to 1st/2nd gen TKIs |
| G1269A | ATP-binding | Crizotinib-resistant |
| I1171T/N/S | Kinase domain | Alectinib-resistant |
| V1180L | Kinase domain | Alectinib-resistant |
| L1256F | Kinase domain | Lorlatinib-resistant |
| Compound mutations | Multiple | Resistant to all single-agent TKIs |

#### Non-EML4 Fusion Partners

Rare ALK fusion partners include KIF5B-ALK, TFG-ALK, TNIP2-ALK ([PMID: 31521978](https://pubmed.ncbi.nlm.nih.gov/31521978/)), CHRNA7-ALK, TACR1-ALK, HIP1-ALK, DYSF-ALK, ITGAV-ALK ([PMID: 31894386](https://pubmed.ncbi.nlm.nih.gov/31894386/)), and CSNK1G3-ALK ([PMID: 40783309](https://pubmed.ncbi.nlm.nih.gov/40783309/)).

### Chromosomal Abnormalities

The defining abnormality is inv(2)(p21p23), a small paracentric inversion on chromosome 2p. This is cytogenetically cryptic (not visible on standard karyotype) and requires FISH, IHC, or NGS for detection. Alternative rearrangement patterns include isolated 5' ALK deletion detected by FISH ([PMID: 26536196](https://pubmed.ncbi.nlm.nih.gov/26536196/)).

### Epigenetic Information

Resistance to ALK TKIs involves epigenetic changes including EMT induction via STAT3/Slug pathway ([PMID: 35085771](https://pubmed.ncbi.nlm.nih.gov/35085771/)), SIRT1 silencing affecting AMPK/mTOR/S6K signaling ([PMID: 39078281](https://pubmed.ncbi.nlm.nih.gov/39078281/)), and gradual, multifactorial adaptation through "acquisition of multiple cooperating genetic and epigenetic adaptive changes" ([PMID: 32409712](https://pubmed.ncbi.nlm.nih.gov/32409712/)).

---

## 5. Environmental Information

### Environmental Factors

Since ALK+ NSCLC predominantly affects never-smokers, relevant environmental factors include:
- **Residential radon**: The most well-established environmental risk factor for LCINS (OR=1.73 for >=200 Bq/m3) ([PMID: 30903971](https://pubmed.ncbi.nlm.nih.gov/30903971/))
- **Air pollution**: Particulate matter (PM2.5) exposure
- **Occupational exposures**: Asbestos, heavy metals, organic solvents
- **Domestic fuel smoke**: Coal and biomass combustion

### Lifestyle Factors

- **Smoking**: Notably, ALK+ NSCLC is enriched in never-smokers (57–69% across cohorts)
- **Cooking exposure**: Cooking without ventilation assessed in TALENT trial as a risk factor ([PMID: 38042167](https://pubmed.ncbi.nlm.nih.gov/38042167/))
- **Diet and exercise**: No specific associations established; exercise intervention shown beneficial for managing lorlatinib-related weight gain ([PMID: 41357598](https://pubmed.ncbi.nlm.nih.gov/41357598/))

### Infectious Agents

- **Mycobacterium tuberculosis**: History of TB associated with increased LCINS risk ([PMID: 32062313](https://pubmed.ncbi.nlm.nih.gov/32062313/))
- **HPV**: Implicated in some LCINS studies, though mechanistic links to ALK rearrangement are unestablished

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The EML4-ALK fusion protein constitutively activates multiple oncogenic signaling cascades:

```
EML4-ALK Fusion Protein (constitutive kinase)
    |
    +---> RAS-MAPK pathway (hsa04010) -> Cell proliferation
    |       +-- ERK -> Jun -> CD73 upregulation -> Immune evasion
    |
    +---> PI3K-AKT pathway (hsa04151) -> Cell survival, anti-apoptosis
    |       +-- mTOR -> Protein synthesis, cell growth
    |
    +---> JAK-STAT pathway (hsa04630) -> Gene transcription
    |       +-- STAT3 -> EMT, invasion (especially G1202R mutants)
    |
    +---> PLCgamma-ERK pathway -> Proliferative signaling
```

**KEGG Pathways**: Non-small cell lung cancer (hsa05223), PI3K-Akt signaling (hsa04151), MAPK signaling (hsa04010), JAK-STAT signaling (hsa04630)

### Phase-Separated Signaling Foci

A critical mechanistic insight is that "EML4-ALK V1 and V3 proteins form cytoplasmic foci that contain components of the MAPK, PLCgamma and PI3K signalling pathways" ([PMID: 34661367](https://pubmed.ncbi.nlm.nih.gov/34661367/)). These phase-separated compartments:
- Concentrate signaling components for efficient pathway activation
- Are dissolved by ALK inhibitors (ceritinib, lorlatinib)
- Show variant-specific behavior: V3 re-localizes to microtubules upon inhibitor treatment
- Are stabilized by constitutively active ALK mutations even in the presence of inhibitors

### HSP90 Chaperone Dependence

"EML4-ALK [was] identified in complex with multiple cellular chaperones including HSP90" ([PMID: 20952506](https://pubmed.ncbi.nlm.nih.gov/20952506/)). V1 shows greater HSP90 dependence than V3 due to its misfolded beta-propeller domain, explaining differential drug sensitivity.

### Immune Evasion Mechanisms

ALK+ NSCLC exhibits an immune-cold phenotype through multiple mechanisms:
- **Low TMB**: "ALK rearrangements were associated with lower TMB and PD-L1+/TMB-H proportions" ([PMID: 33655698](https://pubmed.ncbi.nlm.nih.gov/33655698/))
- **CD73/adenosine pathway**: "Upregulation of CD73/adenosine pathway also contributes to the immune-inert microenvironment" regulated by the ERK-Jun pathway downstream of ALK ([PMID: 35598361](https://pubmed.ncbi.nlm.nih.gov/35598361/))
- **Low CD8+ TILs**: Poor T-cell infiltration
- Multi-omics confirmation: "ALK/RET/ROS1 fusions [are] linked to immune-cold phenotypes with low tumor mutational burden (TMB) and poor T-cell infiltration" ([PMID: 41424613](https://pubmed.ncbi.nlm.nih.gov/41424613/))

**GO Terms**: protein phosphorylation (GO:0006468), MAPK cascade (GO:0000165), cell proliferation (GO:0008283), signal transduction (GO:0007165), apoptotic process (GO:0006915), cell migration (GO:0016477), epithelial-to-mesenchymal transition (GO:0001837)

### Resistance Mechanisms

Resistance evolves through multiple parallel pathways:

1. **Secondary ALK mutations**: G1202R (solvent front), L1196M (gatekeeper), compound mutations
2. **Bypass signaling activation**:
   - EGFR activation ([PMID: 24199682](https://pubmed.ncbi.nlm.nih.gov/24199682/))
   - ERBB3/AKT pathway: "Dual inhibition of ALK and ERBB receptors or AKT disrupts RAS/MAPK and AKT/PI3K signalling" ([PMID: 39695132](https://pubmed.ncbi.nlm.nih.gov/39695132/))
   - SRC kinase upregulation ([PMID: 38521003](https://pubmed.ncbi.nlm.nih.gov/38521003/))
   - AXL/GAS6 axis from macrophages and MMP11+ fibroblasts ([PMID: 39904499](https://pubmed.ncbi.nlm.nih.gov/39904499/))
   - YAP activation driving EGFR, AXL, CYR61, and TGFbetaR2 ([PMID: 31633304](https://pubmed.ncbi.nlm.nih.gov/31633304/))
3. **Phenotypic transformation**: EMT via STAT3/Slug pathway in G1202R mutants — "the expression of EML4-ALK G1202R mutation in A549 cells induced an epithelial-mesenchymal transition (EMT) phenotype and significantly increased the migration and invasion abilities" ([PMID: 35085771](https://pubmed.ncbi.nlm.nih.gov/35085771/))
4. **Microenvironment adaptation**: Cancer-associated fibroblasts (CAFs) conferring resistance ([PMID: 41433419](https://pubmed.ncbi.nlm.nih.gov/41433419/))
5. **Temporal evolution**: "Evidence for a hybrid scenario involving the gradual, multifactorial adaptation to the inhibitors through acquisition of multiple cooperating genetic and epigenetic adaptive changes" with temporally restricted collateral sensitivities ([PMID: 32409712](https://pubmed.ncbi.nlm.nih.gov/32409712/))

### Metabolic Changes

ALK inhibition produces rapid metabolic shutdown: 18F-FDG-PET-CT showed "almost complete inhibition of tumor metabolic activity within 24 hours of ALK inhibitor exposure" ([PMID: 20952506](https://pubmed.ncbi.nlm.nih.gov/20952506/)).

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary organ**: Lung (UBERON:0002048)
- Predominantly affects the upper and middle lobes
- Adenocarcinoma histology in >95% of cases

**Secondary organ involvement** (metastatic sites):
- Brain (UBERON:0000955) — 29% at diagnosis, cumulative incidence >50%
- Liver (UBERON:0002107) — common metastatic site
- Bone (UBERON:0002481) — skeletal metastases
- Pleura (UBERON:0000977) — pleural effusion in 20–35%
- Adrenal glands (UBERON:0002369)
- Leptomeninges — up to 10% of ALK+ NSCLC cases

**Body systems**: Respiratory (primary), nervous (CNS metastases), skeletal, hepatic

### Tissue and Cell Level

- **Epithelial tissue**: Lung adenocarcinoma arising from type II pneumocytes or Clara cells
- **Cell types affected**:
  - Type II alveolar epithelial cells (CL:0002063)
  - Epithelial cells of lung (CL:0000082)
  - Bronchial epithelial cells (CL:0002328)

### Characteristic Histopathology

ALK+ NSCLC shows distinctive histological features: "Acinar, cribriform, and solid growth patterns, extracellular and intracellular mucin production, and presence of signet-ring-cell element, and psammoma body were significantly more often present in ALK-positive cancer" ([PMID: 26095438](https://pubmed.ncbi.nlm.nih.gov/26095438/)). Additional features include goblet cell-like cells and nuclear inclusions/grooves resembling papillary thyroid carcinoma.

In primary pulmonary mucinous adenocarcinoma, ALK rearrangements were found in 34.2% and were significantly increased in the solid tumor with mucin production subtype, including signet ring cells, cribriform, and micropapillary patterns ([PMID: 25813151](https://pubmed.ncbi.nlm.nih.gov/25813151/)).

### Subcellular Level

- **Cytoplasm**: Phase-separated EML4-ALK signaling foci (GO:0005737)
- **Plasma membrane**: ALK receptor signaling (GO:0005886)
- **Microtubules**: V3 re-localizes to microtubules upon inhibitor treatment (GO:0015630)
- **Nucleus**: Downstream transcription factor activation (GO:0005634)

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Adult; median 55–60 years in most cohorts
- **Young-onset cases**: 14.2% diagnosed before age 50 (median 44 years) ([PMID: 31894386](https://pubmed.ncbi.nlm.nih.gov/31894386/))
- **Onset pattern**: Insidious; symptoms develop gradually over weeks to months

### Disease Staging (AJCC 8th Edition)

| Stage | Description | Treatment Approach |
|-------|-------------|-------------------|
| IB–IIIA | Resectable early-stage | Surgery + adjuvant alectinib (ALINA) |
| IIIB–IIIC | Locally advanced | Multimodal therapy |
| IV | Metastatic | First-line ALK TKI (lorlatinib/alectinib) |

### Progression

- **Natural history without treatment**: Rapid progression, median OS ~12 months historically
- **With ALK TKI therapy**: Dramatically prolonged course
  - Median PFS with lorlatinib: >5 years (not reached at 60 months) ([PMID: 39231392](https://pubmed.ncbi.nlm.nih.gov/39231392/))
  - Median OS with sequential TKIs: 81 months (6.8 years) ([PMID: 30599201](https://pubmed.ncbi.nlm.nih.gov/30599201/))
- **Progression pattern**: Typically progressive; oligoprogression amenable to local therapy

### Critical Periods

- **First-line TKI selection**: Critical window determining long-term outcomes
- **Brain metastasis prevention**: Early CNS-penetrant TKI (lorlatinib) prevents brain metastases in 96% of patients
- **Resistance emergence**: Temporally restricted collateral sensitivities exist during adaptation, absent in therapy-naive or fully resistant cells

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence of ALK rearrangement in NSCLC:**
- Overall: 3–7% of NSCLC
- "The overall ALK gene rearrangement rate was 6.7% in 23,689 patients with advanced NSCLC and 8.2% in 17,436 patients with advanced lung adenocarcinoma" ([PMID: 39016057](https://pubmed.ncbi.nlm.nih.gov/39016057/))
- "In a large cohort of 6576 non-small cell lung cancer patients, 343 (5.2%) cases harboring ALK rearrangements were identified" ([PMID: 34271921](https://pubmed.ncbi.nlm.nih.gov/34271921/))

**Estimated incidence**: Given ~2 million new lung cancer cases annually worldwide and ~85% being NSCLC, approximately 50,000–120,000 new ALK+ NSCLC cases occur per year globally.

### Genetic Etiology

- **Inheritance pattern**: Not inherited; exclusively somatic
- **Penetrance**: Not applicable (somatic mutation)
- **Germline mosaicism**: Not applicable

### Population Demographics

| Characteristic | ALK+ NSCLC | General NSCLC |
|----------------|-----------|---------------|
| Median age | 55–60 years | 65–70 years |
| Female proportion | 50–58% | 40–45% |
| Never-smoker | 57–69% | 10–15% |
| Adenocarcinoma | >95% | 40–50% |
| Asian ethnicity | Enriched (43.9% in BC Canada cohort) | Variable |

Real-world data from multiple geographies confirm these demographics:
- **Argentina**: Median age 55, 58% women, 57% nonsmokers ([PMID: 41043103](https://pubmed.ncbi.nlm.nih.gov/41043103/))
- **Canada**: Median age 60, 68.9% never-smokers, 43.9% Asian ([PMID: 40190818](https://pubmed.ncbi.nlm.nih.gov/40190818/))
- **Taiwan**: Median age 60, 49.9% female, 67.6% never-smokers ([PMID: 39392550](https://pubmed.ncbi.nlm.nih.gov/39392550/))

---

## 10. Diagnostics

### Clinical Tests

#### Molecular Testing for ALK Rearrangement

| Method | Sensitivity | Utilization | Advantages |
|--------|------------|------------|------------|
| IHC (Ventana D5F3) | 94–97% | 53.6% (China) | Rapid, inexpensive, reliable screen |
| FISH (break-apart) | Gold standard | 15.9% | FDA-approved reference standard |
| RT-PCR | High | 25.4% | Detects known fusion variants |
| NGS (DNA/RNA) | 97%+ | 18.3% | Comprehensive; detects novel fusions |

"IHC-VENTANA-D5F3 was used in 53.6%, real-time polymerase chain reaction (RT-PCR) in 25.4%, next-generation sequencing (NGS) in 18.3%, and fluorescence in-situ hybridization (FISH) in 15.9%" with intra-hospital consistency of 98.2% for IHC ([PMID: 39016057](https://pubmed.ncbi.nlm.nih.gov/39016057/)).

**Important**: Discordant ALK IHC+/FISH- cases are "infrequent and associated with a worse outcome" on crizotinib, with PFS at 1 year 58% concordant vs 20% discordant ([PMID: 31630043](https://pubmed.ncbi.nlm.nih.gov/31630043/)).

RNA-based NGS was confirmed as "the most efficient technique for gene fusion identification in clinical practice, allowing the simultaneous analysis of a large set of genomic rearrangements" ([PMID: 37190044](https://pubmed.ncbi.nlm.nih.gov/37190044/)).

#### Imaging

- **CT chest**: Standard for disease staging and response assessment
- **Brain MRI**: Essential at diagnosis (29% brain metastases at presentation)
- **PET-CT**: 18F-FDG PET for staging; shows rapid metabolic response to ALK TKIs
- **LDCT screening**: Detects lung cancer at 0.5–1.2% rate in never-smokers; 78–89% early-stage ([PMID: 41816408](https://pubmed.ncbi.nlm.nih.gov/41816408/), [PMID: 39465408](https://pubmed.ncbi.nlm.nih.gov/39465408/))

#### Liquid Biopsy

- ctDNA-based NGS: Useful for molecular profiling when tissue unavailable
- CSF cfDNA: Superior to plasma for detecting CNS-specific alterations in brain metastases
- Concordance: DNA-NGS concordance 97.1% for RNA-NGS, 94.7% for IHC, 97.4% for FISH ([PMID: 35624360](https://pubmed.ncbi.nlm.nih.gov/35624360/))

#### Histopathology

- **Biopsy findings**: Adenocarcinoma with signet ring cells, cribriform/acinar patterns, extracellular mucin, psammoma bodies ([PMID: 26095438](https://pubmed.ncbi.nlm.nih.gov/26095438/))
- **IHC panel**: ALK (D5F3), TTF-1, p40, PD-L1

### Clinical Criteria

- NCCN Guidelines recommend ALK testing for all non-squamous NSCLC and select squamous NSCLC
- Testing should be performed at diagnosis before initiating first-line therapy
- MAXO terms: molecular testing (MAXO:0000630), immunohistochemistry (MAXO:0000548), fluorescence in situ hybridization (MAXO:0000572)

### Differential Diagnosis

- ROS1-rearranged NSCLC (similar demographics, different fusion)
- EGFR-mutant NSCLC (also in never-smokers but mutually exclusive with ALK)
- RET-rearranged NSCLC
- KRAS-mutant NSCLC (smoking-associated)
- MET exon 14 skipping NSCLC

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Stage IV disease (with ALK TKI therapy):**

| Metric | Value | Source |
|--------|-------|--------|
| Median OS (sequential TKIs) | 81 months (6.8 years) | [PMID: 30599201](https://pubmed.ncbi.nlm.nih.gov/30599201/) |
| Median OS (real-world) | 54.0 months | [PMID: 36270866](https://pubmed.ncbi.nlm.nih.gov/36270866/) |
| 5-year PFS (lorlatinib, 1L) | 63% (Asian) | [PMID: 40024442](https://pubmed.ncbi.nlm.nih.gov/40024442/) |
| 2-year DFS (adjuvant alectinib) | 93.8% (stage II–IIIA) | [PMID: 38598794](https://pubmed.ncbi.nlm.nih.gov/38598794/) |
| 2-year death rate | 21% | [PMID: 36270866](https://pubmed.ncbi.nlm.nih.gov/36270866/) |

"With a median follow-up time of 47 months, the median OS time from diagnosis of stage IV disease was 81 months (6.8 years)" ([PMID: 30599201](https://pubmed.ncbi.nlm.nih.gov/30599201/)).

### Prognostic Factors

**Favorable**:
- EML4-ALK V1 (vs V3)
- Wild-type TP53
- Single fusion isoform
- Fewer metastatic organs at diagnosis
- Treatment with next-generation ALK TKIs (vs crizotinib: HR=3.09 for progression/death) ([PMID: 41043103](https://pubmed.ncbi.nlm.nih.gov/41043103/))

**Unfavorable**:
- EML4-ALK V3 (HR=1.53 for PFS vs V1) ([PMID: 41959926](https://pubmed.ncbi.nlm.nih.gov/41959926/))
- TP53 co-mutation (V3+TP53: HR=9.1 for death) ([PMID: 30255938](https://pubmed.ncbi.nlm.nih.gov/30255938/))
- Multiple fusion isoforms (HR=3.74 for OS) ([PMID: 34626839](https://pubmed.ncbi.nlm.nih.gov/34626839/))
- Number of metastatic organs (HR=1.49 per additional organ) ([PMID: 30599201](https://pubmed.ncbi.nlm.nih.gov/30599201/))
- Crizotinib monotherapy as only TKI

### Brain Metastases

Brain metastases present at diagnosis in 29% of patients, with a cumulative incidence exceeding 50%. Lorlatinib provides dramatic CNS control: intracranial ORR 69% vs crizotinib 6% in patients with baseline brain metastases ([PMID: 40024442](https://pubmed.ncbi.nlm.nih.gov/40024442/)). Complete and durable leptomeningeal regression has been documented with lorlatinib ([PMID: 39008537](https://pubmed.ncbi.nlm.nih.gov/39008537/)).

---

## 12. Treatment

### Pharmacotherapy: ALK Tyrosine Kinase Inhibitors

#### Generation Overview

| Generation | Drug | Year Approved | Key Targets | Pivotal Trial |
|-----------|------|---------------|-------------|---------------|
| 1st | Crizotinib | 2011 | ALK/ROS1/MET | PROFILE 1014 |
| 2nd | Ceritinib | 2014 | ALK/IGF-1R/InsR | ASCEND-4 |
| 2nd | Alectinib | 2015 | ALK/RET | ALEX, ALINA |
| 2nd | Brigatinib | 2017 | ALK/ROS1/IGF-1R/FLT3/EGFR | ALTA-1L |
| 2nd | Ensartinib | 2020 | ALK/ROS1/MET | eXalt3 |
| 3rd | Lorlatinib | 2018 | ALK/ROS1 | CROWN |

**KEGG Drug IDs**: Crizotinib (D09731), Alectinib (D10450/D10542), Brigatinib (D10866), Ceritinib (D10551), Ensartinib (D11346/D11356), Lorlatinib (D11012)

#### Key Efficacy Data

**Lorlatinib (CROWN trial, 5-year follow-up)**:
- Median PFS: Not reached (>60 months)
- 5-year PFS: 63% (Asian) vs 7% crizotinib (HR=0.22, 95%CI: 0.13–0.37)
- Intracranial ORR: 69% vs 6% (brain metastases at baseline)
- 96% probability of preventing brain metastases at 5 years
([PMID: 40024442](https://pubmed.ncbi.nlm.nih.gov/40024442/))

**Alectinib (ALEX trial)**:
- Median PFS: 34.8 months vs crizotinib 10.9 months (HR=0.43)
([PMID: 30902613](https://pubmed.ncbi.nlm.nih.gov/30902613/))

**Adjuvant alectinib (ALINA trial)**:
- "The percentage of patients alive and disease-free at 2 years was 93.8% in the alectinib group and 63.0% in the chemotherapy group among patients with stage II or IIIA disease (hazard ratio for disease recurrence or death, 0.24; 95% confidence interval [CI], 0.13 to 0.45; P<0.001)"
([PMID: 38598794](https://pubmed.ncbi.nlm.nih.gov/38598794/))

**Cochrane meta-analysis of ALK TKIs vs chemotherapy (11 RCTs, 2874 patients)**:
- ALK TKIs vs chemo: PFS HR=0.45 (95%CI: 0.40–0.52, high-certainty evidence)
- Next-gen ALK TKIs vs crizotinib: PFS HR=0.39 (95%CI: 0.33–0.46, high-certainty evidence)
- ORR in brain metastases: RR=4.88 vs chemo, RR=2.45 vs crizotinib
([PMID: 34994987](https://pubmed.ncbi.nlm.nih.gov/34994987/))

#### Safety Profiles

"The rates of grade 3–4 AEs were: alectinib (16.2%), crizotinib (46.4%), brigatinib (63.7%), ensartinib (75.6%), ceritinib (78.3%), and lorlatinib (91.6%)" ([PMID: 37597303](https://pubmed.ncbi.nlm.nih.gov/37597303/)). No significant differences were found in fatal AEs or treatment discontinuation rates among the six TKIs.

| Drug | Key Toxicities |
|------|---------------|
| Crizotinib | GI reactions, visual disorders, neutropenia, edema, hepatotoxicity |
| Alectinib | Anemia, constipation (best tolerated overall) |
| Ceritinib | Diarrhea, hepatotoxicity, elevated creatinine |
| Brigatinib | GI reactions, hypertension, cough, headache |
| Ensartinib | Skin disorders, pruritus, rash |
| Lorlatinib | Hyperlipidemia (most frequent), neurocognitive effects (~20%), weight gain |

"About 20% of patients receiving lorlatinib experienced cognitive effects and behavioral alterations in pivotal trials" ([PMID: 35025076](https://pubmed.ncbi.nlm.nih.gov/35025076/)).

**Renal effects**: AKI occurred in 10% within 90 days of ALK TKI initiation; CKD developed in 14% within 1 year; most cases were mild and did not impact OS ([PMID: 40382267](https://pubmed.ncbi.nlm.nih.gov/40382267/)).

**Weight gain management**: Lorlatinib-induced weight gain is manageable with structured exercise intervention including aerobic and resistance training ([PMID: 41357598](https://pubmed.ncbi.nlm.nih.gov/41357598/)).

#### Pharmacogenomics

- **Crizotinib**: CYP3A substrate with substantial interindividual PK variability; "patient survival is lower in the quartile with the lowest steady-state trough plasma concentrations" — pharmacoenhancement with cobicistat possible ([PMID: 33222380](https://pubmed.ncbi.nlm.nih.gov/33222380/))
- **Alectinib**: CYP3A metabolized to active M4 metabolite; "potent CYP3A inhibition or induction resulted in only minor effects on the combined exposure of alectinib and M4" — favorable drug interaction profile ([PMID: 27545757](https://pubmed.ncbi.nlm.nih.gov/27545757/))
- **Lorlatinib**: CYP3A substrate; strong CYP3A inducers significantly reduce exposure; avoid co-administration

### Immunotherapy

ALK+ NSCLC shows limited benefit from immune checkpoint inhibitors due to the immune-cold phenotype. "First-line immunotherapy has limited activity in ALK-rearranged NSCLC; combination of immunotherapy and targeted agents raised safety concerns" ([PMID: 30954906](https://pubmed.ncbi.nlm.nih.gov/30954906/)). Only 5–15% of metastatic NSCLC patients have EGFR/ALK driver mutations, and these are "largely excluded from immunotherapy trials" ([PMID: 30642913](https://pubmed.ncbi.nlm.nih.gov/30642913/)). Rare complete responses to anti-PD1 + chemotherapy have been reported in patients with high PD-L1 expression ([PMID: 39949598](https://pubmed.ncbi.nlm.nih.gov/39949598/)).

### Surgical and Interventional

- **Surgical resection**: Standard for early-stage (I–IIIA) disease with adjuvant alectinib
- **Stereotactic radiosurgery**: For oligoprogressive brain metastases
- **Local ablative therapy**: For oligoprogressive disease allowing continuation of systemic TKI ([PMID: 31010758](https://pubmed.ncbi.nlm.nih.gov/31010758/))

### Experimental Therapies

- **ALK-directed ADC** (CDX0239-PBD): Potent antitumor efficacy in ALK-expressing xenograft models; "ALK RNA, protein, and tumor cell surface expression is elevated in multiple pediatric and adult malignancies with minimal expression in childhood normal tissues" ([PMID: 40813394](https://pubmed.ncbi.nlm.nih.gov/40813394/))
- **Dual ALK + SRC inhibition**: "Co-targeting of ALK and SRC showed remarkable inhibitory effects in both ALK-driven murine and ALK-patient-derived lung tumor cells" ([PMID: 38521003](https://pubmed.ncbi.nlm.nih.gov/38521003/))
- **YAP-targeting strategies**: Cerivastatin (mevalonate pathway inhibitor) shows activity against ALK TKI resistance in vitro, in vivo, in patient-derived xenografts, and in EML4-ALK transgenic mice ([PMID: 31633304](https://pubmed.ncbi.nlm.nih.gov/31633304/))
- **HSP90 inhibitors**: Cause rapid EML4-ALK degradation and transient tumor regression ([PMID: 20952506](https://pubmed.ncbi.nlm.nih.gov/20952506/))
- **ERBB3/AKT dual inhibition**: Enhances apoptosis in EML4-ALK+ NSCLC cells ([PMID: 39695132](https://pubmed.ncbi.nlm.nih.gov/39695132/))
- **Clinical trials**: NCT04318938 (ABP trial, brigatinib with deep phenotyping), NCT03052608 (CROWN), NCT03456076 (ALINA)

### Treatment Strategy

**Current recommended algorithm:**
1. Molecular testing at diagnosis (IHC screen -> FISH/NGS confirmation)
2. Early-stage (resectable): Surgery + adjuvant alectinib x 24 months
3. Advanced/metastatic: First-line lorlatinib or alectinib
4. Progression: Rebiopsy for resistance mechanism -> targeted 2nd-line
5. Oligoprogression: Local ablative therapy + continue TKI

**Sequential TKI treatment**: Taiwan nationwide data demonstrated that treatment sequences including next-generation TKIs were independently associated with longer survival: G2 group median TTD 34.3 months vs G1 alone 7.5 months; G2 group OS HR=0.22 (95%CI: 0.15–0.31) vs crizotinib alone ([PMID: 39392550](https://pubmed.ncbi.nlm.nih.gov/39392550/)).

**MAXO terms**: chemotherapy (MAXO:0000647), radiation therapy (MAXO:0000014), surgical resection (MAXO:0000448), targeted therapy (MAXO:0001525), molecular testing (MAXO:0000630)

---

## 13. Prevention

### Primary Prevention

No specific primary prevention exists for ALK rearrangement as it is a stochastic somatic event. General lung cancer risk reduction includes:
- **Radon mitigation**: Home radon testing and mitigation systems
- **Air pollution reduction**: Environmental regulatory measures
- **Secondhand smoke avoidance**: Smoke-free environments
- **Adequate cooking ventilation**: Particularly in Asian populations

### Secondary Prevention (Screening)

**LDCT screening in never-smokers:**
- Thailand cohort: LC detection 1.2%, 69.8% stage 0–IB, 85% adenocarcinoma ([PMID: 41816408](https://pubmed.ncbi.nlm.nih.gov/41816408/))
- China NCC: LC detection 1.0% in never-smokers vs 0.8% in smokers; 78.8% early-stage ([PMID: 39465408](https://pubmed.ncbi.nlm.nih.gov/39465408/))
- South Korea: LC diagnosed in 0.47% of 17,968 never-smokers ([PMID: 32482786](https://pubmed.ncbi.nlm.nih.gov/32482786/))

"Current screening guidelines and eligibility criteria have limited efficacy in identifying LC cases (50%), as most screening programs primarily target subjects with a smoking history" ([PMID: 38977146](https://pubmed.ncbi.nlm.nih.gov/38977146/)). Expanding LDCT to never-smokers with risk factors (family history, radon exposure) is an important unmet need.

The TALENT trial (Taiwan) specifically screens never-smokers aged 55–75 with risk factors including family history, passive smoke, TB history, and cooking exposure. Among 12,011 participants, lung cancer was diagnosed in 2.6%, with 77.4% at stage I. Family history of lung cancer and age >60 years were independently associated with increased risk ([PMID: 38042167](https://pubmed.ncbi.nlm.nih.gov/38042167/)).

### Tertiary Prevention

- **Adjuvant ALK TKI therapy**: Prevents recurrence after surgery (ALINA trial: 2-year DFS 93.8% vs 63.0% for chemotherapy)
- **Brain metastasis prevention**: CNS-penetrant TKIs (lorlatinib) prevent brain metastases in 96% of patients over 5 years
- **Resistance monitoring**: Serial liquid biopsy for early detection of resistance mutations

---

## 14. Other Species / Natural Disease

### ALK in Other Species

ALK is evolutionarily conserved and plays roles in nervous system development across species:

- **Drosophila melanogaster** (NCBI Taxon: 7227): ALK ortholog (dAlk) regulates neuropeptide precursors; "The Alk receptor tyrosine kinase regulates Sparkly, a novel activity regulating neuropeptide precursor" ([PMID: 38904987](https://pubmed.ncbi.nlm.nih.gov/38904987/))
- **Mus musculus** (NCBI Taxon: 10090): Mouse Alk gene (NCBI Gene: 11682); EML4-ALK transgenic models phenocopy human disease
- **Danio rerio** (zebrafish): ALK ortholog expressed in developing nervous system

### ALK in Other Cancer Types

ALK rearrangements/mutations drive multiple cancers across species:
- **Anaplastic large cell lymphoma (ALCL)**: NPM1-ALK fusion (KEGG: H01601)
- **Neuroblastoma**: ALK point mutations and amplification (KEGG: H00043); NLRR1 acts as extracellular negative regulator of ALK signaling in neuroblastoma ([PMID: 27604320](https://pubmed.ncbi.nlm.nih.gov/27604320/))
- **Inflammatory myofibroblastic tumors (IMTs)**: Various ALK fusions, including novel rearrangements in neonates ([PMID: 24290361](https://pubmed.ncbi.nlm.nih.gov/24290361/))
- **Rhabdomyosarcoma**: ALK overexpression ([PMID: 40813394](https://pubmed.ncbi.nlm.nih.gov/40813394/))
- **Peripheral T-cell lymphoma** (KEGG: H01892)

### Comparative Biology

ALK expression is "restricted to the developing nervous system" in normal tissues, with "minimal expression in childhood normal tissues" making it an attractive therapeutic target across species and cancer types ([PMID: 40813394](https://pubmed.ncbi.nlm.nih.gov/40813394/)). The evolutionary conservation of ALK function from Drosophila to humans supports the use of cross-species models for studying ALK biology.

---

## 15. Model Organisms

### Genetically Engineered Mouse Models

**EML4-ALK transgenic mice**: "We generated a genetically engineered mouse model that phenocopies the human disease where this rearranged gene arises" ([PMID: 20952506](https://pubmed.ncbi.nlm.nih.gov/20952506/)). Key features:
- Develops lung adenocarcinoma
- Responsive to ALK TKIs (tumor regression with TAE684)
- Shows greater tumor regression with ALK inhibitors than carboplatin/paclitaxel
- HSP90 inhibitors cause rapid EML4-ALK degradation
- Variant-specific models (V1, V3) established showing V3 confers worse ALK inhibitor response ([PMID: 38521003](https://pubmed.ncbi.nlm.nih.gov/38521003/))

### Xenograft Models

| Cell Line | Characteristics | Applications |
|-----------|---------------|-------------|
| NCI-H3122 | EML4-ALK V1 (E13;A20) | Drug testing, resistance studies |
| NCI-H2228 | EML4-ALK V3 (E6;A20) | Drug testing, intrapleural models |
| Patient-derived xenografts (PDX) | Variable | Personalized drug testing, resistance |

"ASP3026 also showed potent antitumor activities, including tumor shrinkage to a nondetectable level, in hEML4-ALK transgenic mice and prolonged survival in mice with intrapleural NCI-H2228 xenografts" ([PMID: 24419060](https://pubmed.ncbi.nlm.nih.gov/24419060/)).

YAP targeting was shown effective in both patient-derived xenografts and EML4-ALK transgenic mice for overcoming ALK TKI resistance ([PMID: 31633304](https://pubmed.ncbi.nlm.nih.gov/31633304/)).

### Patient-Derived Models

**Patient-derived organoids (PDOs)**: Used for drug sensitivity testing in refractory ALK+ NSCLC. Case reports demonstrate clinical utility: "PDOs derived from primary and metastatic lesions may help optimize treatment regimens for patients with lung cancer brain metastases, thereby enabling personalized therapy" ([PMID: 41114337](https://pubmed.ncbi.nlm.nih.gov/41114337/)).

In one case, a patient with complex EML4-ALK fusion variant 3 (E6:A20) and a novel NRXN1-ALK fusion who had progressed on multiple therapies showed PDO sensitivity to brigatinib, which subsequently induced a partial response sustained for 5.8 months.

### Cell Line Models

- **NCI-H3122**: Standard V1 model; used extensively for resistance studies including EGFR activation as bypass mechanism ([PMID: 24199682](https://pubmed.ncbi.nlm.nih.gov/24199682/))
- **NCI-H2228**: V3 model; used for intrapleural and intrahepatic xenograft studies
- **EML4-ALK expressing normal human cells**: EML4-ALK expression in mortal normal fibroblasts causes cellular senescence; hTERT co-expression enables transformation, providing isogenic model systems ([PMID: 33761896](https://pubmed.ncbi.nlm.nih.gov/33761896/))

### Model Limitations

- Mouse models do not fully recapitulate the immune microenvironment complexity
- Xenograft models lack the tumor-stroma interactions of native disease
- Species-specific differences in drug metabolism affect pharmacokinetic translation
- Brain metastasis models are technically challenging to establish
- PDO systems do not capture tumor-immune cell interactions

---

## Key Findings: Detailed Evidence Summary

### Finding 1: ALK Prevalence and Demographics
ALK rearrangements occur in 3–7% of NSCLC, predominantly in adenocarcinoma histology. The overall ALK gene rearrangement rate was 6.7% in 23,689 patients with advanced NSCLC ([PMID: 39016057](https://pubmed.ncbi.nlm.nih.gov/39016057/)). The disease preferentially affects younger (median 55), female (50–58%), never-smoking (57–69%) patients ([PMID: 22129856](https://pubmed.ncbi.nlm.nih.gov/22129856/), [PMID: 41043103](https://pubmed.ncbi.nlm.nih.gov/41043103/), [PMID: 40190818](https://pubmed.ncbi.nlm.nih.gov/40190818/)).

### Finding 2: Variant-Specific Prognosis
EML4-ALK V3 confers worse prognosis than V1, with meta-analysis showing HR=1.53 (95%CI: 1.17–1.99, p=0.002) for PFS ([PMID: 41959926](https://pubmed.ncbi.nlm.nih.gov/41959926/)). The combination of V3 + TP53 mutation is particularly lethal (HR=9.1 for death, p=0.02) ([PMID: 30255938](https://pubmed.ncbi.nlm.nih.gov/30255938/)). The biophysical explanation involves differential phase separation properties and HSP90 dependence between variants ([PMID: 37149843](https://pubmed.ncbi.nlm.nih.gov/37149843/)).

### Finding 3: Dramatic TKI Efficacy
Lorlatinib achieved 5-year PFS of 63% in Asian patients (HR=0.22 vs crizotinib) with 96% brain metastasis prevention ([PMID: 40024442](https://pubmed.ncbi.nlm.nih.gov/40024442/)). Adjuvant alectinib showed 2-year DFS of 93.8% vs 63.0% for chemotherapy (HR=0.24, P<0.001) ([PMID: 38598794](https://pubmed.ncbi.nlm.nih.gov/38598794/)). Sequential TKI therapy yields median OS of 81 months ([PMID: 30599201](https://pubmed.ncbi.nlm.nih.gov/30599201/)).

### Finding 4: Multifaceted Resistance
Resistance evolves gradually through multiple cooperating mechanisms ([PMID: 32409712](https://pubmed.ncbi.nlm.nih.gov/32409712/)) including secondary ALK mutations, bypass signaling (EGFR, SRC, AXL, ERBB3), EMT, YAP activation, and microenvironment adaptation via CAFs.

### Finding 5: Immune-Cold Phenotype
Multi-omics studies consistently demonstrate ALK fusions are linked to immune-cold phenotypes with low TMB and poor T-cell infiltration ([PMID: 41424613](https://pubmed.ncbi.nlm.nih.gov/41424613/)). The CD73/adenosine pathway, regulated by the ALK-ERK-Jun axis, contributes to immune evasion ([PMID: 35598361](https://pubmed.ncbi.nlm.nih.gov/35598361/)).

---

## Mechanistic Model: Integrated Pathophysiology

```
INITIATING EVENT
    Somatic inv(2)(p21p23) -> EML4-ALK fusion gene
                |
MOLECULAR MECHANISM
    Constitutive ALK kinase activity
                |
    +-----------+---------------+
    v           v               v
Phase-separated  HSP90 chaperone  Variant-specific
signaling foci   dependence       properties (V1 vs V3)
    |               |               |
    v               v               v
DOWNSTREAM SIGNALING
    +-- RAS-MAPK -> Proliferation + CD73 -> Immune evasion
    +-- PI3K-AKT-mTOR -> Survival + Growth
    +-- JAK-STAT3 -> Transcription + EMT potential
    +-- PLCgamma-ERK -> Proliferation
                |
CELLULAR CONSEQUENCES
    +-- Uncontrolled proliferation
    +-- Anti-apoptotic signaling
    +-- Immune-cold microenvironment (low TMB, CD73/adenosine)
    +-- CNS tropism (brain metastases in >50%)
                |
CLINICAL MANIFESTATION
    Lung adenocarcinoma -> Metastases (brain, bone, liver)
                |
TREATMENT -> ALK TKI (dissolves signaling foci, blocks kinase)
                |
RESISTANCE EVOLUTION (gradual, multifactorial)
    +-- ALK mutations (G1202R, L1196M, compound)
    +-- Bypass signaling (EGFR, SRC, AXL/GAS6, ERBB3)
    +-- Phenotypic: EMT (STAT3/Slug), YAP activation
    +-- Microenvironment: CAF-mediated resistance
```

---

## Evidence Base: Key Literature

| PMID | Year | Key Contribution |
|------|------|-----------------|
| [17625570](https://pubmed.ncbi.nlm.nih.gov/17625570/) | 2007 | Discovery of EML4-ALK fusion in NSCLC |
| [20952506](https://pubmed.ncbi.nlm.nih.gov/20952506/) | 2010 | EML4-ALK transgenic mouse model; HSP90 dependence |
| [22129856](https://pubmed.ncbi.nlm.nih.gov/22129856/) | 2012 | Demographic enrichment of ALK+ NSCLC |
| [24199682](https://pubmed.ncbi.nlm.nih.gov/24199682/) | 2014 | EGFR activation as crizotinib resistance mechanism |
| [26095438](https://pubmed.ncbi.nlm.nih.gov/26095438/) | 2015 | Histologic features of ALK+ adenocarcinoma |
| [30255938](https://pubmed.ncbi.nlm.nih.gov/30255938/) | 2018 | V3+TP53 lethal subgroup identification |
| [30599201](https://pubmed.ncbi.nlm.nih.gov/30599201/) | 2019 | 6.8-year median OS natural history |
| [30902613](https://pubmed.ncbi.nlm.nih.gov/30902613/) | 2019 | ALEX trial: alectinib 34.8-month PFS |
| [31633304](https://pubmed.ncbi.nlm.nih.gov/31633304/) | 2019 | YAP as resistance mechanism and therapeutic target |
| [32409712](https://pubmed.ncbi.nlm.nih.gov/32409712/) | 2020 | Gradual multifactorial resistance evolution |
| [34661367](https://pubmed.ncbi.nlm.nih.gov/34661367/) | 2021 | Phase-separated EML4-ALK signaling foci |
| [34626839](https://pubmed.ncbi.nlm.nih.gov/34626839/) | 2021 | Fusion isoform heterogeneity as prognostic factor |
| [34994987](https://pubmed.ncbi.nlm.nih.gov/34994987/) | 2021 | Cochrane review of ALK TKIs (11 RCTs, 2874 patients) |
| [35598361](https://pubmed.ncbi.nlm.nih.gov/35598361/) | 2022 | CD73/adenosine immune evasion mechanism |
| [37149843](https://pubmed.ncbi.nlm.nih.gov/37149843/) | 2023 | Biophysical basis of V1 vs V3 drug sensitivity |
| [37597303](https://pubmed.ncbi.nlm.nih.gov/37597303/) | 2023 | Network meta-analysis of ALK TKI safety |
| [38598794](https://pubmed.ncbi.nlm.nih.gov/38598794/) | 2024 | ALINA trial: adjuvant alectinib |
| [39016057](https://pubmed.ncbi.nlm.nih.gov/39016057/) | 2024 | Large-scale real-world ALK testing data |
| [40024442](https://pubmed.ncbi.nlm.nih.gov/40024442/) | 2025 | CROWN 5-year data: lorlatinib PFS >60 months |
| [41424613](https://pubmed.ncbi.nlm.nih.gov/41424613/) | 2025 | Multi-omics confirmation of immune-cold phenotype |
| [41959926](https://pubmed.ncbi.nlm.nih.gov/41959926/) | 2025 | Meta-analysis: V3 vs V1 prognosis |

---

## Limitations and Knowledge Gaps

1. **No head-to-head trials** comparing lorlatinib vs alectinib as first-line therapy; current comparisons rely on matching-adjusted indirect comparisons (MAIC)
2. **Optimal TKI sequencing** remains undefined — which TKI should be used first, and what is the best sequence upon progression?
3. **Resistance to lorlatinib**: Limited understanding of compound ALK mutations and strategies to overcome them
4. **Immunotherapy role**: Optimal approaches to enhance immune response in the immune-cold ALK+ tumor microenvironment remain unclear; CD73/adenosine pathway inhibition is an untested clinical strategy
5. **Screening for never-smokers**: No validated risk models for LDCT screening specifically targeting ALK+ NSCLC-prone populations
6. **Long-term outcomes**: True 10-year survival data with modern TKI regimens are not yet mature
7. **Mechanisms of CNS tropism**: Why ALK+ NSCLC shows preferential brain metastasis remains incompletely understood
8. **Epigenetic contributions**: Role of DNA methylation and chromatin remodeling in ALK rearrangement susceptibility and resistance needs further study
9. **Germline susceptibility**: Whether certain germline variants predispose to somatic ALK rearrangements is unknown
10. **Health disparities**: Access to molecular testing and next-generation ALK TKIs varies dramatically globally

---

## Proposed Follow-up Experiments/Actions

### Clinical Priorities

1. **Head-to-head lorlatinib vs alectinib trial**: Definitive comparison of the two leading first-line options, particularly for patients without brain metastases
2. **Fourth-generation ALK inhibitors**: Development of agents active against compound mutations (G1202R + L1196M, etc.)
3. **CD73/adenosine pathway inhibitors + ALK TKI**: Clinical trials combining ALK-targeted therapy with immune microenvironment modulation to overcome intrinsic immunotherapy resistance
4. **Circulating tumor DNA-guided adaptive therapy**: Using serial ctDNA monitoring to detect resistance mutations early and guide therapy changes before radiographic progression
5. **LDCT screening trials for never-smokers**: Expansion with risk models incorporating family history, radon exposure, and cooking fume exposure; integration with reflex molecular testing of detected nodules

### Research Priorities

6. **Single-cell multi-omics of resistance**: Characterizing the evolution of TKI resistance at single-cell resolution to identify therapeutic windows and collateral sensitivities
7. **ALK-directed ADCs**: Clinical translation of antibody-drug conjugates (e.g., CDX0239-PBD) targeting ALK-expressing tumors
8. **Combination strategies for resistance**: SRC+ALK inhibition, ERBB3+ALK inhibition, YAP/mevalonate pathway targeting
9. **Brain metastasis prevention biomarkers**: Identifying patients at highest risk for CNS metastases who would benefit most from early CNS-penetrant therapy
10. **Patient-derived organoid platforms**: Scaling PDO-guided therapy for personalized treatment selection in refractory disease, particularly for patients with complex or novel fusion variants

---

## Ontology Term Summary

### Disease Ontology
- MONDO:0005233 (non-small cell lung carcinoma)
- MONDO:0005061 (lung adenocarcinoma)
- NCIT:C215346 (ALK-Positive Lung Non-Small Cell Carcinoma)

### Phenotype Ontology (HPO)
- HP:0100526 (Neoplasm of the lung)
- HP:0012735 (Cough)
- HP:0002094 (Dyspnea)
- HP:0002105 (Hemoptysis)
- HP:0001824 (Weight loss)
- HP:0100749 (Chest pain)
- HP:0002202 (Pleural effusion)
- HP:0100634 (Brain metastases)
- HP:0012378 (Fatigue)

### Gene Ontology (Biological Process)
- GO:0006468 (protein phosphorylation)
- GO:0000165 (MAPK cascade)
- GO:0008283 (cell proliferation)
- GO:0007165 (signal transduction)
- GO:0006915 (apoptotic process)
- GO:0016477 (cell migration)
- GO:0001837 (epithelial to mesenchymal transition)

### Gene Ontology (Cellular Component)
- GO:0005737 (cytoplasm)
- GO:0005886 (plasma membrane)
- GO:0015630 (microtubule cytoskeleton)
- GO:0005634 (nucleus)

### Cell Ontology (CL)
- CL:0002063 (type II pneumocyte)
- CL:0000082 (epithelial cell of lung)
- CL:0002328 (bronchial epithelial cell)

### Anatomy Ontology (UBERON)
- UBERON:0002048 (lung)
- UBERON:0002185 (bronchus)
- UBERON:0000955 (brain)
- UBERON:0000977 (pleura)
- UBERON:0002107 (liver)
- UBERON:0002481 (bone tissue)
- UBERON:0002369 (adrenal gland)

### Chemical Entities (CHEBI)
- Crizotinib (KEGG: D09731)
- Alectinib (KEGG: D10450)
- Lorlatinib (KEGG: D11012)
- Brigatinib (KEGG: D10866)
- Ceritinib (KEGG: D10551)
- Ensartinib (KEGG: D11346)

### Medical Action Ontology (MAXO)
- MAXO:0000647 (chemotherapy)
- MAXO:0000014 (radiation therapy)
- MAXO:0000448 (surgical resection)
- MAXO:0001525 (targeted therapy)
- MAXO:0000630 (molecular testing)
- MAXO:0000548 (immunohistochemistry)
- MAXO:0000572 (fluorescence in situ hybridization)

---

*Report generated from systematic analysis of 129 papers, 22 confirmed findings, across 5 investigation iterations. All citations verified against original abstracts. Last updated: 2026-05-06.*
