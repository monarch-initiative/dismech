---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-03T00:39:20.695505'
end_time: '2026-08-03T00:44:15.499481'
duration_seconds: 294.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CDH2-Related ACOG Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 19
  total_cost_usd: 1.5509829000000002
  session_id: ccfe4e45-02a4-514e-bba5-3af1e8db647b
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CDH2-Related ACOG Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CDH2-Related ACOG Syndrome** covering all of the
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

# CDH2-Related ACOG Syndrome: Comprehensive Research Report

## Executive Summary

CDH2-related ACOG syndrome (Agenesis of Corpus Callosum, Ocular, Cardiac, and Genital syndrome; also referred to in OMIM as ACOGS) is an ultra-rare, autosomal dominant, multisystem neurodevelopmental disorder caused by de novo heterozygous pathogenic variants in **CDH2**, the gene encoding **N-cadherin (neuronal cadherin)**. It was first delineated as a distinct Mendelian syndrome in 2019 by Accogli, Srour, Charron, and colleagues (PMID:31585109), who proposed the name "ACOG syndrome" for the pentad of axon-pathfinding defects, corpus callosum anomalies, and ocular, cardiac, and genital malformations. As of the most recent case series (2022), only ~15 individuals have been reported worldwide (PMID:35708058), making this one of the rarest entries in the cadherinopathy spectrum.

---

## 1. Disease Information

**Overview:** CDH2-related ACOG syndrome is a syndromic neurodevelopmental disorder resulting from de novo heterozygous loss-of-function or dominant-negative missense variants in CDH2. The disorder was defined by Accogli et al. (2019), who identified nine individuals with de novo CDH2 variants (seven missense, two frameshift) presenting with "global developmental delay and/or intellectual disability, variable axon pathfinding defects (corpus callosum agenesis or hypoplasia, mirror movements, Duane anomaly), and ocular, cardiac, and genital anomalies" (PMID:31585109). The authors coined the acronym "ACOG syndrome" — Agenesis of corpus callosum, axon pathfinding, Cardiac, Ocular, and Genital defects.

A related, overlapping presentation with a prominent anterior-segment eye phenotype was independently reported as "a new syndrome including Peters anomaly" caused by CDH2 variants (Peters Anomaly Spectrum group, PMID:31650526, *Clinical Genetics* 2020;97(3):502-508), describing four individuals with de novo CDH2 variants (splicing + missense) and Peters anomaly, three of whom had syndromic features overlapping ACOG syndrome (agenesis of the corpus callosum, cerebellar vermis hypoplasia, left-sided cardiac lesions, dysmorphic facies). These two reports are now generally regarded as describing the same CDH2-related disorder spectrum.

**Key identifiers:**
- **OMIM (phenotype):** #618929 — "Agenesis of Corpus Callosum, Cardiac, Ocular, and Genital Syndrome; ACOGS"
- **OMIM (gene):** *114020 — CADHERIN 2; CDH2
- **MONDO:** MONDO:0030065
- **Disease Ontology:** DOID:0080948
- **NCBI GTR condition:** C5394523
- **Gene identifiers:** HGNC:1759; NCBI Gene ID: 1000; chromosome 18q12.1
- **ICD-10/11:** No dedicated ICD code exists; typically coded under Q04.0 (agenesis of corpus callosum) or Q89.7 (multiple congenital malformations, not elsewhere classified) in practice — no CDH2-specific ICD-11 entry was identified.
- **MeSH:** No dedicated MeSH heading; indexed under "Agenesis of Corpus Callosum" (D019112) and "Cadherins" (D029464).

**Synonyms:** ACOGS; ACOG syndrome; CDH2-related neurodevelopmental disorder; "N-cadherinopathy"; the Peters-anomaly-predominant presentation is sometimes referenced separately as "CDH2-related Peters anomaly syndrome."

**Evidence base:** All currently published information derives from aggregated case series/case reports (human clinical, aggregated across ~15 patients total in the two founding cohorts plus subsequent single case reports) rather than large-scale EHR data, reflecting the extreme rarity of the condition.

---

## 2. Etiology

**Disease causal factors:** ACOG syndrome is caused exclusively by **de novo heterozygous pathogenic variants in CDH2** (autosomal dominant, essentially 100% de novo in reported cases). No environmental, infectious, or multifactorial causes have been implicated; this is a purely monogenic disorder.

**Genetic risk factors:**
- All reported pathogenic variants are heterozygous and arose de novo — no inherited/familial transmission has been documented, consistent with a severe, likely-reproductively-limiting phenotype.
- Variant spectrum from the founding cohort: seven missense variants and two frameshift variants (PMID:31585109). "Six of the seven missense variants localize to extracellular cadherin domains 4–5 (EC4–EC5), with four affecting calcium-binding sites" — functional studies showed these EC4–EC5 variants impair cell-cell adhesion.
- The Peters-anomaly cohort (PMID:31650526) added a de novo splicing variant and additional missense variants in the extracellular cadherin domains.
- ClinVar-documented variants associated with ACOGS include NM_001792.5(CDH2):c.1057G>A (p.Asp353Asn), c.1808C>G (p.Pro603Arg), and c.2027A>G (p.Tyr676Cys), among others.
- The Kanjee et al. (2022) case (PMID:35708058) reported a novel de novo **nonsense** variant, expanding the mutational mechanism beyond missense/frameshift to include premature-stop-codon variants.

**Modifier/susceptibility factors:** No modifier genes have been identified; given the extremely small number of reported cases, genotype-phenotype correlation is preliminary. Variants clustering in EC4–EC5 appear to correlate with the more classic ACOG presentation (CNS/axon-pathfinding-predominant), while some variants correlate more with the Peters-anomaly/anterior-segment ocular phenotype, but sample sizes are too small for robust correlation.

**Protective factors:** None identified — no protective genetic or environmental factors have been reported for this ultra-rare monogenic disorder.

**Gene-environment interactions:** None reported; the disorder behaves as a fully penetrant (or near-fully penetrant), single-gene Mendelian condition with no documented environmental modifiers.

---

## 3. Phenotypes

Phenotype frequencies below are drawn from the aggregated cohort of the two founding reports (approximately 9–13 evaluable individuals per feature; PMID:31585109, PMID:31650526) plus subsequent case reports (PMID:35708058).

### Neurodevelopmental / Neurological
- **Global developmental delay / intellectual disability** — reported in ~10/12 evaluable patients; variable severity (mild–moderate most common). *Suggested HPO:* HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability)
- **Agenesis or hypoplasia of the corpus callosum** — reported in ~11/13; the defining CNS feature, reflecting failure of interhemispheric axon pathfinding. *Suggested HPO:* HP:0001274 (Agenesis of corpus callosum), HP:0002079 (Hypoplasia of the corpus callosum)
- **Cerebellar vermis hypoplasia** — described in both cohorts. *Suggested HPO:* HP:0001320 (Cerebellar vermis hypoplasia)
- **Incomplete hippocampal rotation** — noted as an additional brain malformation. *Suggested HPO:* HP:0030050 (Abnormal hippocampus morphology, most specific available term)
- **Absent septum pellucidum** — reported in a subset. *Suggested HPO:* HP:0030754 (Absent septum pellucidum, if available) or HP:0001300 (Cavum septum pellucidum, note as related structural anomaly)
- **Mirror movements** — an axon-pathfinding/corticospinal-miswiring sign consistent with N-cadherin's role in axon guidance. *Suggested HPO:* HP:0007301 (Mirror movements of the hand) or HP:0002378 (Mirror movements)
- **Hypotonia (axial) with hypertonic extremities** — mixed tone abnormality. *Suggested HPO:* HP:0001252 (Hypotonia), HP:0001276 (Hypertonia)
- **Cognitive/behavioral delay** — variable severity, described qualitatively as "cognitive delays."

### Ocular
- **Duane anomaly / Duane retraction syndrome** — a specific ocular motility axon-pathfinding defect (cranial nerve VI miswiring), directly reflecting N-cadherin's axon-guidance role. *Suggested HPO:* HP:0009921 (Duane anomaly)
- **Peters anomaly** — anterior-segment dysgenesis with corneal opacity/iridocorneal-lenticular adhesions, prominent in the PMID:31650526 cohort. *Suggested HPO:* HP:0007756 (Peters anomaly)
- Other ocular anomalies collectively reported in ~11/13 evaluable individuals (exact sub-phenotypes not fully itemized in available abstracts beyond Duane anomaly and Peters anomaly).

### Cardiac
- **Congenital cardiac anomalies** — reported in ~9/13; left-sided cardiac lesions specifically noted in the Peters-anomaly cohort. *Suggested HPO:* HP:0001631 (Atrial septal defect), HP:0001629 (Ventricular septal defect) — specific lesion types not uniformly itemized across all published cases; "left-sided cardiac lesions" suggests possible left ventricular outflow tract anomalies. *Broader term:* HP:0001627 (Abnormal heart morphology)

### Genital / Genitourinary
- **Cryptorchidism** (males) — a recurring genital anomaly. *Suggested HPO:* HP:0000028 (Cryptorchidism)
- **Micropenis** (males) — reported ("micropesis" in one source is a likely OCR error for "micropenis"). *Suggested HPO:* HP:0000054 (Micropenis)
- **Renal anomaly (ureteropelvic junction obstruction, UPJO)** — reported in the first female patient (Kanjee et al. 2022, PMID:35708058), noted as the first genitourinary/renal finding described in a female with ACOGS, since prior reports documented only male-specific genital malformations. *Suggested HPO:* HP:0000072 (Hydronephrosis) / HP:0100957 (Ureteropelvic junction obstruction, if using UPJO-specific term)

### Craniofacial dysmorphism
- Hypertelorism (HP:0000316), flat nasal bridge (HP:0005280), low-set or posteriorly rotated ears (HP:0000369 / HP:0000368), upturned earlobes, thin upper lip (HP:0000219), small mouth with downturned corners (HP:0000175 / HP:0002714), low anterior hairline (HP:0000294).

**Onset/severity/progression:** All reported phenotypes are congenital/present from birth or early infancy (structural brain, cardiac, ocular, and genital malformations). Developmental delay becomes apparent in infancy/early childhood. The disorder does not appear to be progressive in the neurodegenerative sense — it is a static structural/developmental malformation syndrome, though longitudinal follow-up data are sparse given the small number of reported patients.

**Quality of life impact:** Not formally studied (no EQ-5D/SF-36 data identified); qualitatively, impact stems from intellectual disability, visual impairment (Duane anomaly, Peters anomaly with corneal opacity), and, when present, cardiac and renal complications requiring surgical/medical management.

---

## 4. Genetic / Molecular Information

**Causal gene:** CDH2 (cadherin 2, HGNC:1759, NCBI Gene 1000, OMIM *114020, chromosome 18q12.1), encoding **N-cadherin (neuronal cadherin, cadherin-2)**, a classical type I transmembrane cadherin.

**Variant classification and type:**
- Missense variants (majority; six of seven in the founding cohort cluster in EC4–EC5), frameshift variants, a splicing variant, and at least one nonsense variant (PMID:35708058) have been reported — spanning a broader range of variant classes than initially described.
- ACMG/AMP classification: reported variants are generally classified pathogenic/likely pathogenic in ClinVar given de novo occurrence, absence from population databases, and functional evidence of impaired adhesion.
- **Allele frequency:** Given all reported variants are de novo and disease-causing, they are essentially absent from gnomAD/population databases (consistent with severe, non-transmitted Mendelian disease); specific gnomAD allele counts were not available in the sources reviewed.
- **Origin:** Exclusively germline, de novo (no somatic CDH2-ACOGS association reported).

**Functional consequences:** Rutherford/Accogli et al. demonstrated that "cells expressing these variants in the EC4-EC5 domains have a defect in cell-cell adhesion" (PMID:31585109) — i.e., the mechanism is loss of N-cadherin-mediated homophilic adhesion, acting in a dominant-negative and/or haploinsufficient manner. A separate report on ACOGS variants found that "de novo mutations in the CDH2 gene impair the cell adhesion function of N-cadherin by affecting self-binding as well as trans-binding with wildtype N-cadherin" — indicating a **dominant-negative mechanism** in which mutant protein interferes with wild-type N-cadherin function in trans, in addition to any haploinsufficiency.

**Protein structure context:** N-cadherin is composed of five extracellular cadherin (EC1–EC5) repeat domains (each ~110 amino acids), a transmembrane domain, and a cytoplasmic tail that binds β-catenin/p120-catenin linking to the actin cytoskeleton. Calcium ions bind at interdomain linker regions between EC repeats and rigidify the ectodomain into an extended rod required for trans-adhesion between apposing cell surfaces; EC1–EC2 mediate the primary trans-dimer "strand-swap" interaction, while EC4–EC5 (where most ACOG-syndrome variants cluster) contribute to maintaining the correct ectodomain length/rigidity required for productive trans-dimerization, and calcium-binding-site disruption at EC4–EC5 destabilizes this trans-adhesive interface.

**Epigenetic information:** No CDH2-ACOGS-specific epigenetic (DNA methylation/histone) data were identified in the literature reviewed.

**Chromosomal abnormalities:** ACOG syndrome is caused by point mutations/small indels, not by large chromosomal rearrangements; no recurrent CNV/deletion mechanism has been reported (distinguishing it from contiguous-gene 18q12 deletion syndromes, which are a different, unrelated entity).

**Related but genetically/mechanistically distinct CDH2 disease associations** (important for differential diagnosis and module design — these are separate CDH2 phenotypes, not part of ACOG syndrome per se):
- **Arrhythmogenic right ventricular cardiomyopathy (ARVC):** CDH2 mutations were identified as a novel non-desmosomal genetic cause of ARVC (first reported in a South African family, 2017; PMID:28280076, *Circ Cardiovasc Genet*). This is an adult-onset, isolated cardiac arrhythmia/cardiomyopathy phenotype, mechanistically and clinically distinct from ACOG syndrome's developmental malformation presentation, though both stem from N-cadherin dysfunction (ARVC-associated variants are hypothesized to act primarily through desmosome/intercalated-disc destabilization in cardiomyocytes rather than broad developmental adhesion failure).
- **Dilated cardiomyopathy (DCM):** A novel CDH2 variant has also been associated with DCM (PMC9468813, *Front Med* 2022).
- **Attention-Deficit/Hyperactivity Disorder 8:** GeneCards lists CDH2 as associated with an ADHD susceptibility phenotype, distinct from full-syndrome ACOGS.

---

## 5. Environmental Information

No environmental factors, toxin exposures, lifestyle factors, or infectious agents have been implicated in CDH2-related ACOG syndrome — it is a purely genetic (de novo monogenic) disorder. No gene-environment interaction data exist.

---

## 6. Mechanism / Pathophysiology

**Causal chain (from molecular lesion to clinical phenotype):**

1. **Molecular lesion:** De novo heterozygous CDH2 variant (missense in EC4–EC5 calcium-binding sites, frameshift, nonsense, or splice-altering) →
2. **Protein dysfunction:** Impaired N-cadherin ectodomain rigidity/calcium coordination → defective **homophilic trans-adhesion** between N-cadherin molecules on apposing cell membranes, with evidence of a **dominant-negative effect** on wild-type N-cadherin trans-binding (not pure haploinsufficiency) →
3. **Cellular process disruption:** Failure of N-cadherin-dependent processes across multiple developing tissues — neuroepithelial integrity, radial glial scaffold confinement, growth-cone/axon-guidance receptor complex function, cardiomyocyte adherens-junction/intercalated-disc assembly, and periocular/anterior-segment mesenchymal-neural-crest adhesion →
4. **Tissue-level consequence:** Failure of commissural/callosal axons to cross the midline (agenesis/hypoplasia of the corpus callosum), miswiring of cranial motor axons (Duane anomaly), anterior-segment dysgenesis (Peters anomaly), cardiac septation/outflow anomalies, and disrupted genital tubercle/urogenital tract morphogenesis →
5. **Organism-level phenotype:** The multisystem ACOG syndrome presentation (global developmental delay/ID, callosal agenesis, axon-pathfinding defects, ocular anomalies, cardiac anomalies, genital anomalies, craniofacial dysmorphism).

**Molecular pathways/cellular processes:** N-cadherin functions at the head of a "cadherin–catenin–actin" adhesion complex: the cytoplasmic tail binds **p120-catenin** and **β-catenin**, which in turn links to **α-catenin** and the actin cytoskeleton, stabilizing adherens junctions and simultaneously modulating **Wnt/β-catenin signaling** availability. In neurons, N-cadherin also interacts with growth-cone guidance-receptor machinery relevant to netrin/DCC and other axon-pathfinding pathways (consistent with senior-author Frédéric Charron's expertise in axon guidance) and is implicated in growth-cone adhesion-dependent turning responses.

The 2022 review "Flying under the radar: CDH2 (N-cadherin), an important hub molecule in neurodevelopmental and neurodegenerative diseases" (Njoo & Charron lab collaborators, PMID:36213737, *Front Neurosci* 2022;16:972059) summarizes that during CNS development CDH2/N-cadherin is required for: "maintenance of neuroepithelial integrity, neural tube closure, confinement of radial glia progenitor cells to the ventricular zone and maintaining their proliferation-differentiation balance, postmitotic neural precursor migration, axon guidance, synaptic development and maintenance."

**Cell types involved (suggested CL terms):**
- Neuroepithelial cells / radial glial cells (CL:0000681, radial glial cell)
- Commissural/callosal projection neurons (CL:0000679, glutamatergic neuron; or CL:0011005, callosal neuron if available)
- Cardiomyocytes (CL:0000746, cardiac muscle cell)
- Cranial neural crest-derived mesenchyme (CL:0000333, migratory neural crest cell) — relevant to anterior-segment (Peters anomaly) and craniofacial dysmorphism
- Growth cones of developing axons (structure rather than cell type; consider GO cellular component GO:0030426, growth cone)

**Suggested GO Biological Process terms:**
- GO:0007156 (homophilic cell adhesion via plasma membrane adhesion molecules)
- GO:0007411 (axon guidance)
- GO:0021801 (cerebral cortex radial glia guided migration) / GO:0021795 (cerebral cortex cell migration)
- GO:0007043 (cell-cell junction assembly)
- GO:0060976 (coronary vasculature development) — less specific; better: GO:0003231 (cardiac ventricle development) or GO:0003179 (heart valve morphogenesis) depending on the specific cardiac lesion
- GO:0021952 (central nervous system projection neuron axonogenesis)
- GO:0060997 (dendritic spine morphogenesis) — for the synaptic maintenance role noted in the review

**Suggested GO Cellular Component / Molecular Function terms:**
- GO:0005913 (cell-cell adherens junction)
- GO:0098641 (cadherin binding involved in cell-cell adhesion)
- GO:0008014 (obsolete/legacy) — prefer GO:0005509 (calcium ion binding) for the EC-domain calcium coordination function

**Protein dysfunction mechanism:** Predominantly **dominant-negative** — mutant N-cadherin monomers interfere with wild-type N-cadherin's ability to form productive trans-dimers at apposing cell surfaces ("affecting self-binding as well as trans-binding with wildtype N-cadherin"), rather than simple haploinsufficiency, though partial loss-of-function contribution cannot be excluded for frameshift/nonsense alleles predicted to trigger nonsense-mediated decay.

**Immune system involvement:** Not implicated; this is a developmental structural disorder, not an immune-mediated one.

**Molecular profiling / omics:** No transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to human CDH2-ACOG-syndrome patient tissue were identified in the literature reviewed; mechanistic data derive from in vitro cell-adhesion assays (e.g., aggregation assays in transfected cell lines) rather than patient-derived omics.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain (corpus callosum, cerebellar vermis, hippocampus, septum pellucidum), eyes (anterior segment/cornea, extraocular muscles/cranial nerve VI), heart, external/internal genitalia, kidneys/urinary tract.
- **Secondary:** Craniofacial skeleton (dysmorphic features).
- **Body systems:** Nervous system, cardiovascular system, ocular/visual system, genitourinary system, musculoskeletal/craniofacial system.

**Suggested UBERON terms:**
- UBERON:0002336 (corpus callosum)
- UBERON:0002037 (cerebellum) / UBERON:0002264 (cerebellar vermis, if available)
- UBERON:0002421 (hippocampal formation)
- UBERON:0000955 (brain)
- UBERON:0000970 (eye)
- UBERON:0000006 (islet of Langerhans — not relevant; disregard) — correct ocular term: UBERON:0000964 (cornea) for Peters anomaly; UBERON:0001776 (extraocular muscle) for Duane anomaly
- UBERON:0000948 (heart)
- UBERON:0000992 (gonad) / UBERON:0000473 (testis) for cryptorchidism; UBERON:0000030 (penis) for micropenis
- UBERON:0002113 (kidney) / UBERON:0001222 (ureteropelvic junction, if available) for UPJO

**Tissue/cell level:** Neuroepithelium and radial glial scaffold of the ventricular zone; commissural axon tracts; cardiac myocardium and intercalated discs; corneal endothelium/anterior-segment mesenchyme (neural-crest derived).

**Subcellular level (GO Cellular Component):** Adherens junctions (GO:0005913), plasma membrane (site of N-cadherin's homophilic adhesive function), growth cone (GO:0030426).

**Lateralization:** No consistent lateralization pattern reported; corpus callosum agenesis is inherently a midline defect, and cardiac lesions described as "left-sided" in the Peters-anomaly cohort suggest some left-sided predilection for cardiac involvement specifically, but this is based on very small numbers.

---

## 8. Temporal Development

**Onset:** Congenital — all core structural anomalies (brain, cardiac, ocular, genital, craniofacial) are present from birth/prenatally, as expected for a developmental malformation syndrome. Developmental delay/intellectual disability becomes clinically apparent during infancy and early childhood as milestones are missed.

**Onset pattern:** Insidious recognition in infancy for the neurodevelopmental component; acute/immediately apparent at birth for structural anomalies (e.g., cardiac defects, genital anomalies, corneal opacity in Peters anomaly).

**Progression:** The disorder is best characterized as a **static structural malformation syndrome** rather than a progressive neurodegenerative one — no reports of regression or progressive deterioration were identified. However, given only ~15 patients have ever been reported and longitudinal follow-up is limited, the full natural history (e.g., adult outcomes, aging-related complications) remains poorly characterized.

**Disease course pattern:** Chronic, lifelong (congenital malformations and associated intellectual disability persist), not relapsing-remitting or episodic.

**Critical periods:** The pathophysiology implicates disruption during early embryonic/fetal development — specifically during neural tube closure, midline commissural axon crossing (corpus callosum formation, ~12–20 weeks gestation in humans), cardiac septation/looping (weeks 3–8 gestation), anterior-segment/ocular morphogenesis, and genital tubercle differentiation — all first-trimester-to-mid-second-trimester embryonic windows.

**Remission:** Not applicable — no remission pattern described for a congenital structural malformation syndrome.

---

## 9. Inheritance and Population

**Epidemiology:** Extremely rare — as of the most recent published case report (2022), "only 14 patients with ACOGS had been reported" prior to the fifteenth patient described by Kanjee et al. (PMID:35708058). No formal prevalence or incidence rate (cases per 100,000) has been established; the disorder is far below the threshold of most registry-based epidemiological reporting, consistent with its very recent (2019) delineation as a distinct syndrome and its de novo, non-transmitted genetic basis.

**Inheritance pattern:** Autosomal dominant, with essentially all reported cases arising from **de novo** variants (no vertical transmission reported to date, consistent with reduced reproductive fitness typical of severe multisystem developmental syndromes).

**Penetrance:** Presumed high/complete for the core neurodevelopmental and structural phenotype, though formal penetrance estimates are not available given the small cohort and absence of inherited (non-de-novo) transmission data.

**Expressivity:** Notably **variable** — patients show a spectrum from ACOG-syndrome-predominant (axon-pathfinding/callosal-predominant) to Peters-anomaly-predominant (anterior-segment ocular-predominant) presentations, and individual features (cardiac, genital, renal) are present in only a subset of patients (e.g., renal/UPJO reported in only one patient to date). This variable expressivity may partly correlate with variant location/type but sample sizes are too small for firm genotype-phenotype rules.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed, though it remains a theoretical possibility relevant to recurrence-risk counseling for parents of an affected child, as with other de novo dominant disorders.

**Founder effects:** None reported; cases have been identified across North America, Europe, and Turkey (Kanjee et al., first reported case from Turkey), consistent with pan-ethnic occurrence and no population-specific founder variant.

**Consanguinity:** Not implicated — consistent with the de novo dominant mechanism (consanguinity is relevant to recessive disease, not de novo dominant disease).

**Carrier frequency:** Not applicable for a de novo dominant, non-carrier-based condition.

**Population demographics:**
- **Sex ratio:** Both males and females affected; genital anomalies (cryptorchidism, micropenis) were initially described only in males, but Kanjee et al. (2022) reported "the first female patient" with ACOGS, presenting instead with a renal anomaly (UPJO), suggesting genitourinary tract involvement in females manifests differently (upper urinary tract rather than external genitalia).
- **Geographic distribution:** Cases reported from North America, Europe, and Turkey; no endemic or regionally clustered pattern identified — consistent with a pan-ethnic de novo disorder.
- **Age distribution:** All reported cases are pediatric at time of publication (diagnosis in infancy/childhood); no adult natural-history cohort has been published.

---

## 10. Diagnostics

**Clinical/laboratory tests:** No CDH2-ACOGS-specific biochemical biomarker exists; diagnosis relies on recognition of the clinical/imaging phenotype plus molecular confirmation.

**Imaging studies:**
- **Brain MRI:** Essential for detecting agenesis/hypoplasia of the corpus callosum, cerebellar vermis hypoplasia, incomplete hippocampal rotation, and absent septum pellucidum.
- **Echocardiography:** For detection of congenital cardiac anomalies (including left-sided lesions).
- **Renal/abdominal ultrasound:** For detection of urinary tract anomalies (e.g., UPJO/hydronephrosis), as illustrated by the female patient reported by Kanjee et al.
- **Ophthalmologic exam (slit-lamp, anterior-segment imaging):** For Duane anomaly and Peters anomaly detection.

**Genetic testing:**
- **Recommended approach:** Given the phenotypic overlap with numerous other syndromic corpus callosum agenesis/neurodevelopmental disorders, **exome sequencing (WES) or genome sequencing (WGS)**, typically as a **trio (proband + both parents)** to establish de novo status, is the diagnostic approach used in all reported cases (the founding cohort was largely ascertained through the NIH Undiagnosed Diseases Network and international WES/WGS collaborations).
- **Gene panels:** CDH2 is increasingly included on clinical "corpus callosum agenesis," "intellectual disability," and "malformations of cortical development" gene panels (e.g., Genomics England PanelApp lists CDH2 under "Malformations of cortical development" and "Paediatric disorders — additional genes" panels).
- **Single-gene testing:** Feasible once a specific familial variant is known, but as a first-tier test is unlikely to be efficient given phenotypic overlap with many other genes.
- **Chromosomal microarray (CMA)/karyotyping:** Not diagnostic for CDH2 point variants but often performed first-line to exclude copy-number/chromosomal causes of corpus callosum agenesis or multiple congenital anomalies before sequencing.

**Clinical/diagnostic criteria:** No formal consensus diagnostic criteria (e.g., DSM/ICD-style) have been published; diagnosis is currently based on the combination of (1) characteristic multisystem phenotype (callosal/axon-pathfinding + ocular + cardiac + genital + craniofacial dysmorphism) and (2) identification of a de novo heterozygous CDH2 variant.

**Differential diagnosis:** Other syndromic corpus callosum agenesis disorders (e.g., Mowat-Wilson syndrome, Acrocallosal syndrome, other Duane-anomaly-associated syndromes such as Okihiro/Duane-radial ray syndrome [SALL4], and other cadherin/catenin-pathway disorders), isolated Peters anomaly (PAX6, PITX2, FOXC1, CYP1B1, COL6A3, B3GLCT, DOP1B and other genes), and other causes of syndromic developmental delay with cardiac and genital anomalies (e.g., CHARGE syndrome, VACTERL association).

**Screening:** No population-based or newborn screening applicable — the disorder is not detectable by standard biochemical newborn screening panels and is far too rare for targeted population screening; diagnosis occurs reactively based on clinical presentation.

---

## 11. Outcome / Prognosis

**Survival/mortality:** No mortality data specific to CDH2-ACOGS were identified; the disorder has not been reported as inherently life-limiting, though outcomes will depend heavily on the severity of associated cardiac and renal anomalies in individual patients, which can independently carry morbidity/mortality risk if uncorrected.

**Morbidity/function:** Long-term functional outcomes are not well characterized given the small number of reported, largely pediatric, cases. Anticipated morbidity domains include: cognitive/intellectual disability (variable, generally mild-to-moderate based on available descriptions), visual impairment (from Peters anomaly's corneal opacity and/or Duane anomaly's motility restriction), and any sequelae of unrepaired/repaired structural cardiac or renal anomalies.

**Complications:** Congenital cardiac lesions and renal/urinary tract anomalies (e.g., UPJO leading to hydronephrosis) may require surgical intervention and carry their own complication profiles independent of the neurodevelopmental features.

**Recovery potential:** Structural malformations (cardiac, renal, ocular) may be amenable to surgical correction with resulting improvement in organ-specific function; the neurodevelopmental/intellectual disability component is not expected to "recover" but may improve functionally with early intervention (standard practice for developmental delay, not disease-specific).

**Prognostic factors:** Not formally established; qualitatively, the presence and severity of cardiac and renal anomalies, and the degree of corpus callosum abnormality/associated brain malformation burden, would be expected to influence overall prognosis, but no quantitative prognostic model exists given the rarity of the condition.

---

## 12. Treatment

There is **no disease-modifying or CDH2-targeted therapy** for ACOG syndrome; management is entirely **symptomatic, supportive, and multidisciplinary**, following standard-of-care approaches for each organ-system manifestation (this mirrors management of other syndromic multiple-congenital-anomaly/intellectual disability disorders where no gene-specific therapy exists).

**Suggested multidisciplinary management approach (NCIT terms in parentheses where applicable):**
- **Neurodevelopmental/rehabilitative:** Early intervention services, physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), speech-language therapy (NCIT:C159273), special education support for intellectual disability.
- **Ophthalmologic:** Surgical management of Peters anomaly (e.g., penetrating keratoplasty for corneal opacity in severe cases) (NCIT:C15329, Surgical Procedure); strabismus/Duane anomaly management may include observation or extraocular muscle surgery depending on severity and functional impact.
- **Cardiac:** Standard congenital heart disease management per lesion type — may range from surveillance to surgical repair (NCIT:C15329, Surgical Procedure; cardiology follow-up).
- **Genitourinary:** Urologic evaluation/management of cryptorchidism (orchiopexy) and UPJO (pyeloplasty if obstructive/symptomatic) (NCIT:C15329, Surgical Procedure).
- **Genetic counseling:** Recommended for all families given the de novo autosomal dominant mechanism, to discuss low (but non-zero, due to theoretical germline mosaicism) recurrence risk for future pregnancies and to facilitate cascade/predictive considerations (NCIT:C15240, Genetic Counseling).
- **Supportive care:** Routine surveillance/supportive care coordinated across specialists (NCIT:C15747, Supportive Care).

**Experimental treatments:** No CDH2-ACOGS-specific clinical trials (ClinicalTrials.gov) were identified — the extreme rarity of the condition (~15 reported patients) makes disease-specific trials unlikely at this stage. No gene therapy, RNA-based therapy, or targeted molecular therapy has been proposed or is in development for this disorder in the literature reviewed.

**Treatment outcomes:** No systematic data on treatment response rates or adverse events specific to this population exist, again reflecting the very small published cohort.

---

## 13. Prevention

**Primary prevention:** Not applicable in a conventional sense — the disorder results from de novo germline mutation with no known modifiable environmental trigger, so there are no primary-prevention (risk-factor-modification) strategies.

**Secondary prevention / screening:** No population or targeted screening program exists or would be practical given the extreme rarity and de novo nature of the disorder. Prenatal detection is theoretically possible via detailed fetal anatomy ultrasound (identifying corpus callosum agenesis, cardiac anomalies, or genital anomalies) followed by diagnostic prenatal exome sequencing if a syndromic picture is suspected, but this is not a formal screening recommendation specific to CDH2.

**Genetic counseling:** The main "preventive" intervention available is **reproductive genetic counseling** for parents of an affected child — given de novo dominant inheritance, recurrence risk for future pregnancies is low but not zero (accounting for theoretical parental germline mosaicism, as is standard counseling practice for de novo dominant conditions); prenatal diagnosis via chorionic villus sampling/amniocentesis with targeted variant testing would be available once the familial pathogenic variant is known.

**Public health interventions:** None specific to this ultra-rare monogenic disorder.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring CDH2-ACOG-syndrome-like disease has been reported in non-human species (e.g., in OMIA, the animal-disease counterpart of OMIM). CDH2/N-cadherin is highly evolutionarily conserved across vertebrates (relevant orthologs exist in mouse, zebrafish, chick, Xenopus), but no spontaneous veterinary case series analogous to human ACOG syndrome was identified.

**Orthologous gene:** Mouse *Cdh2* (MGI:88355), located on a syntenic region; extensively studied in developmental biology (see Model Organisms, below).

**Comparative biology:** N-cadherin's role in neural tube closure, cardiac morphogenesis, and axon guidance is deeply conserved across vertebrate models, supporting strong mechanistic plausibility that mouse/zebrafish CDH2 loss-of-function models recapitulate aspects of the human phenotype, even though a naturally occurring animal ACOG-syndrome phenocopy has not been documented.

**Zoonotic potential:** Not applicable (non-infectious, genetic disorder).

---

## 15. Model Organisms

**Mouse (*Mus musculus*, Cdh2, MGI:88355):**
- **Constitutive knockout:** Global *Cdh2*-null mice are **embryonic lethal around E10**, due to severe cardiac developmental defects. Reported abnormalities include growth retardation, an enlarged/malformed heart, distended pericardial sac, abnormal heart tube looping, a "wavy" (undulated) neural tube, irregular somite shape, and abnormal embryonic turning — precluding assessment of later CNS developmental roles in the constitutive knockout (JAX strain 003179).
- **Conditional/cardiac-specific knockout:** Because global knockout is embryonic lethal via cardiac failure, cardiac-specific conditional deletion strategies have been used. Non-inducible cardiomyocyte-specific deletion (αMHC-Cre) is also embryonic lethal; an **inducible** cardiac-specific Cre was required to bypass the embryonic requirement. Inducible postnatal cardiomyocyte-specific *Cdh2* deletion "disrupts cell-cell adherens contacts and destabilization of gap junctions, resulting in conduction defects, spontaneous ventricular arrhythmias, cardiomyopathy, and premature cardiac death" (relevant to the CDH2-ARVC/DCM cardiac phenotypes specifically, and mechanistically informative for the cardiac component of ACOG syndrome).
- **Neural-specific conditional models:** Conditional CNS deletion approaches (e.g., using neural-lineage Cre drivers) have been used in the broader N-cadherin literature to study neuroepithelial integrity, neural tube closure, radial glial scaffold maintenance, and axon guidance — consistent with, and mechanistically supportive of, the CNS phenotypes (corpus callosum agenesis, axon-pathfinding defects) seen in human ACOG syndrome patients, per the review by PMID:36213737.

**Zebrafish and other model systems:** N-cadherin (*cdh2*) mutant/morphant zebrafish have long been used to study neural tube and heart-tube morphogenesis given the same fundamental conservation of N-cadherin function, though a study specifically modeling the human ACOG-syndrome missense alleles in zebrafish was not identified in the sources reviewed.

**In vitro/cell-based models:** The primary functional validation for human ACOG-syndrome-associated CDH2 variants to date has been **cell-based adhesion/aggregation assays** in transfected cell lines (e.g., L-cells or similar cadherin-null lines classically used for cadherin adhesion assays), which demonstrated that EC4–EC5 domain variants impair both self-binding (cis) and trans-binding to wild-type N-cadherin, supporting a dominant-negative mechanism (PMID:31585109).

**Model limitations:** The constitutive mouse knockout's early embryonic lethality (E10, via cardiac failure) means it cannot recapitulate — or be used to directly study — the later CNS callosal/axon-pathfinding phenotypes central to the human syndrome; conditional/tissue-specific and patient-variant-knock-in mouse models (rather than null alleles) would be needed to more faithfully model the human missense/dominant-negative disease mechanism, and such variant-specific knock-in models were not identified as yet published in the literature reviewed.

---

## Summary Table of Key Ontology Term Suggestions

| Category | Suggested Term | ID |
|---|---|---|
| Disease | Agenesis of corpus callosum, cardiac, ocular, and genital syndrome | OMIM:618929 / MONDO:0030065 |
| Gene | CDH2 | HGNC:1759 / NCBI Gene:1000 |
| Phenotype | Agenesis of corpus callosum | HP:0001274 |
| Phenotype | Duane anomaly | HP:0009921 |
| Phenotype | Peters anomaly | HP:0007756 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Cryptorchidism | HP:0000028 |
| Phenotype | Micropenis | HP:0000054 |
| Phenotype | Cerebellar vermis hypoplasia | HP:0001320 |
| Biological process | Homophilic cell adhesion via plasma membrane adhesion molecules | GO:0007156 |
| Biological process | Axon guidance | GO:0007411 |
| Cellular component | Cell-cell adherens junction | GO:0005913 |
| Cell type | Radial glial cell | CL:0000681 |
| Cell type | Cardiac muscle cell | CL:0000746 |
| Anatomy | Corpus callosum | UBERON:0002336 |
| Anatomy | Heart | UBERON:0000948 |

---

## Notes on Evidence Gaps

- **Prevalence/incidence:** No formal population-level rate is available (only cumulative case counts, ~15 patients as of 2022); any later-reported cases beyond the sources reviewed here should be checked via a fresh PubMed search before curation, given the field is actively expanding one case report at a time.
- **ORPHA number:** A dedicated Orphanet entry number specifically for "ACOG syndrome"/ACOGS was not conclusively located in this search (Orphanet does maintain a CDH2 gene page linking to associated rare diseases); this should be verified directly against Orphanet's live database before finalizing a KB entry.
- **Quantitative phenotype frequencies** beyond the qualitative fractions cited (e.g., "10/12," "11/13," "9/13") should be re-verified against the primary AJHG and Clinical Genetics papers' full tables, as only abstract/secondary-source-level detail was accessible in this research pass.
- **No dedicated GeneReviews chapter** for CDH2-ACOG syndrome was identified as of this search — the primary clinical reference remains the original 2019 AJHG paper and subsequent case reports.

---

### Sources

- [De Novo Pathogenic Variants in N-cadherin Cause a Syndromic Neurodevelopmental Disorder with Corpus Callosum, Axon, Cardiac, Ocular, and Genital Defects (AJHG 2019) — PMID:31585109](https://www.sciencedirect.com/science/article/pii/S0002929719303441)
- [Novel variants in CDH2 are associated with a new syndrome including Peters anomaly (Clin Genet 2020) — PMID:31650526](https://pubmed.ncbi.nlm.nih.gov/31650526/)
- [A Novel nonsense variant in the CDH2 gene associated with ACOGS: A case report (AJMG-A 2022) — PMID:35708058](https://pubmed.ncbi.nlm.nih.gov/35708058/)
- [Flying under the radar: CDH2 (N-cadherin), an important hub molecule in neurodevelopmental and neurodegenerative diseases (Front Neurosci 2022) — PMID:36213737](https://pmc.ncbi.nlm.nih.gov/articles/PMC9539934/)
- [OMIM #618929 — Agenesis of Corpus Callosum, Cardiac, Ocular, and Genital Syndrome](https://omim.org/entry/618929)
- [OMIM *114020 — Cadherin 2; CDH2](https://omim.org/entry/114020)
- [Identification of Cadherin 2 (CDH2) Mutations in Arrhythmogenic Right Ventricular Cardiomyopathy — PMID:28280076](https://pubmed.ncbi.nlm.nih.gov/28280076/)
- [Identification of a novel variant in N-cadherin associated with dilated cardiomyopathy](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468813/)
- [CDH2 Gene - GeneCards](https://www.genecards.org/card/CDH2)
- [Agenesis of Corpus Callosum, Cardiac, Ocular, and Genital Syndrome - MalaCards](https://www.malacards.org/card/agenesis_of_corpus_callosum_cardiac_ocular_and_genital_syndrome)
- [Cdh2 MGI Mouse Gene Detail - MGI:88355](https://www.informatics.jax.org/marker/MGI:88355)
- [003179 - N-cadherin KO Strain Details - JAX](https://www.jax.org/strain/003179)
- [Induced Deletion of the N-Cadherin Gene in the Heart Leads to Dissolution of the Intercalated Disc Structure — Circulation Research](https://www.ahajournals.org/doi/10.1161/01.res.0000156274.72390.2c)