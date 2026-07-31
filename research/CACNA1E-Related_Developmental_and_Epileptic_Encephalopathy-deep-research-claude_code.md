---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-25T17:14:19.541949'
end_time: '2026-07-25T17:39:33.434488'
duration_seconds: 1513.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CACNA1E-Related Developmental and Epileptic Encephalopathy
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
  - claude-opus-5[1m]
  web_search_requests: 15
  num_turns: 33
  total_cost_usd: 3.5098155
  session_id: 78134249-0dcd-4de5-96b6-436d93db5713
  stop_reason: end_turn
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CACNA1E-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CACNA1E-Related Developmental and Epileptic Encephalopathy** covering all of the
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

# CACNA1E-Related Developmental and Epileptic Encephalopathy (DEE69)
### A comprehensive research report for knowledge-base curation
**Compiled 2026-07-25 · MONDO:0032657 · OMIM #618285 · gene CACNA1E (HGNC:1392)**

---

## Reading note before we dive in

ok so — a quick honesty pass up front, because it shapes everything below. This disease is *young*. It got its name in October 2018, and the evidence base is basically one landmark cohort of 30 people, one commentary that re-tabulates that cohort with percentages, one 7-person "no-epilepsy" cohort, a handful of case reports, and a beautiful piece of mechanism work that arrived sideways from the CDKL5 field. That's it. There's no natural-history study, no registry, no prevalence number, no clinical trial, no biomarker.

So think of the literature here less like a well-mapped organ system and more like a single core sample pulled out of a cliff face — the layers you can see are crisp and real, but there's a whole lot of rock nobody's drilled yet. Wherever the rock is undrilled, I say so instead of filling it in.

Two of the sources below (PMID:30343943, PMID:31064215) are already cached and snippet-validated in this repository's `references_cache/`, so quotes from those two are verified exact substrings of the real abstracts. Quotes from the others were pulled fresh from PubMed/publisher abstracts during this session and are marked accordingly.

---

## 1. Disease Information

### Overview

CACNA1E-related developmental and epileptic encephalopathy — formally **developmental and epileptic encephalopathy 69 (DEE69)** — is a severe, early-onset neurodevelopmental disorder caused by de novo heterozygous variants in *CACNA1E*, the gene for the pore-forming α1 subunit of the **Ca_V2.3 R-type voltage-gated calcium channel**.

The defining clinical picture, straight from the paper that named it:

> "we identified de novo CACNA1E variants in 30 individuals with DEE, characterized by refractory infantile-onset seizures, severe hypotonia, and profound developmental impairment, often with congenital contractures, macrocephaly, hyperkinetic movement disorders, and early death."
> — Helbig et al., *Am J Hum Genet* 2018 (**PMID:30343943**) *[cached & validated]*

The mechanistic one-liner: most pathogenic variants sit at the cytoplasmic ends of the four S6 helices — the channel's activation gate — and they're **gain-of-function**. The gate gets sloppy about closing. Calcium that should trickle in on a tight schedule instead floods in early and leaves late.

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | `MONDO:0032657` — developmental and epileptic encephalopathy, 69 |
| OMIM (disease) | `#618285` DEE69 |
| OMIM (gene) | `*601013` CACNA1E |
| DOID | `DOID:0112205` |
| MedGen / UMLS | `C4748988` |
| GARD | `GARD:0025714` |
| HGNC | `hgnc:1392` (lowercase prefix per repo convention) |
| NCBI Gene | `777` |
| Ensembl | `ENSG00000198216` |
| UniProt | `Q15878` (CAC1E_HUMAN) |
| Cytoband | 1q25.3 |
| MONDO parent | `MONDO:0100062` genetic developmental and epileptic encephalopathy |

*(MONDO xrefs and synonyms verified locally against `sqlite:obo:mondo` this session.)*

**Orphanet:** I could not confirm a dedicated ORPHA code for the CACNA1E-specific entity. *CACNA1E* appears as a causal gene under Orphanet's broader early-infantile DEE grouping (**ORPHA:1934**), but no `ORPHA_*` cache file for it exists in this repo. **Flag as unresolved** rather than asserting a code.

**ICD:** no disease-specific code. Falls under ICD-10 **G40.4** (other generalized epilepsy and epileptic syndromes) / ICD-11 **8A61** (developmental and epileptic encephalopathies) — these are syndrome-class codes, not entity codes, so don't treat them as identifiers.

### Synonyms

- DEE69 · EIEE69
- Epileptic encephalopathy, early infantile, 69
- CACNA1E-related developmental and epileptic encephalopathy
- Developmental and epileptic encephalopathy with contractures, macrocephaly, and dyskinesias
- CACNA1E encephalopathy · Ca_V2.3 channelopathy (informal)

### Data provenance

All disease-level knowledge here is **aggregated from published individual-patient reports** — GeneMatcher-assembled international cohorts, single case reports, and one video-EEG case study. There is **no EHR-derived cohort, no patient registry, and no natural-history study** for this disease. That's a real gap, not an oversight of my searching.

---

## 2. Etiology

### Primary cause

Monogenic, essentially always **de novo heterozygous missense variants in *CACNA1E***. No environmental, infectious, or multifactorial contribution is described anywhere in the literature I reviewed.

The variant architecture is startlingly tidy — a small mutational hotspot rather than a scatter:

> "Most of the 14, partially recurring, variants cluster within the cytoplasmic ends of all four S6 segments, which form the presumed CaV2.3 channel activation gate."
> — **PMID:30343943** *[cached & validated]*

That S6-distal clustering isn't unique to this gene, either. It's a recurring architectural motif across the calcium-channel epilepsies — a shared soft spot, like how the same vertebra tends to go in several different back conditions:

> "Disease-causing variants predominantly involve gain-of-function mechanisms, with missense variants clustering in the distal S6 segment — a mutational hotspot shared across other voltage-gated calcium channel genes."
> — Lauerer & Lerche, *J Neurochem* 2023 (**PMID:37822150**) *[fetched this session]*

### Genetic risk factors

- **Causal:** de novo GOF missense in *CACNA1E*. Recurrent hotspots: **p.Gly352Arg** (DI-S6) and **p.Ala702Thr** (DII-S6).
- **Susceptibility loci / modifier genes:** none identified. No GWAS, no modifier screen exists.
- **Constraint:** *CACNA1E* is a large, highly brain-expressed gene under evident missense constraint; Royer-Bertrand et al. explicitly compared the pathogenic-variant landscape against gnomAD and "identified protein regions intolerant to substitutions" (**PMID:34702355**). I did **not** retrieve the numeric gnomAD pLI/LOEUF/missense-Z values in this session (the browser is a JS app that WebFetch can't render) — **fetch those directly before curating any specific number.**

### Environmental risk factors

**None known.** De novo mutation rate rises modestly with advanced paternal age as a general genomic phenomenon, but no paternal-age effect has been specifically demonstrated for *CACNA1E* — do not assert one.

### Protective factors

None described in humans. The nearest thing is inverse-mechanistic and comes from mice: losing Ca_V2.3 function is *anticonvulsant* (see §15). No protective human allele is known.

### Gene–environment interactions

None reported. Not applicable in any documented sense.

---

## 3. Phenotypes

### The quantitative core

Almost every frequency in this disease traces back to one tabulation of the founding 30-person cohort. Here it is verbatim, because it's the single densest sentence in the whole literature:

> "The 30 patients with pathogenic CACNA1E variants presented with a variable DEE characterized by refractory epilepsy (87% of patients) with median seizure onset at 4.5 months, movement disorders (60%), spastic quadriplegia (53%), congenital joint contractures (43%), macrocephaly (43%), and profound developmental impairments (ie, nonverbal and nonambulatory) (88%)."
> — Carvill, *Epilepsy Curr* 2019 (**PMID:31064215**) *[cached & validated]*

### Phenotype table with HPO suggestions

| Phenotype | HPO term | Freq. | Onset | Course | Type |
|---|---|---|---|---|---|
| Epileptic encephalopathy | `HP:0200134` Epileptic encephalopathy | defining | infantile | — | clinical sign |
| Refractory seizures | `HP:0001250` Seizure (+ temporality RECURRENT) | 87% (VERY_FREQUENT) | median **4.5 months** | drug-resistant, persistent | clinical sign |
| Profound global developmental delay | `HP:0012736` | 88% (VERY_FREQUENT) | infantile | static-to-progressive impairment | clinical sign |
| Severe hypotonia | `HP:0001252` Hypotonia (severity SEVERE) | core feature, % not tabulated | neonatal/infantile | often evolves toward spasticity | physical sign |
| Movement disorder (hyperkinetic) | `HP:0002487` Hyperkinetic movements | 60% (FREQUENT) | infancy–early childhood | episodic/fluctuating | clinical sign |
| — severe dystonia component | `HP:0001332` Dystonia | ~40% | — | — | clinical sign |
| — other dyskinesias | `HP:0002072` Abnormality of extrapyramidal motor function | ~20% | — | — | clinical sign |
| Spastic quadriplegia | `HP:0002510` Spastic tetraplegia | 53% (FREQUENT) | infancy onward | progressive | physical sign |
| Congenital joint contractures | `HP:0002803` Congenital contracture | 43% (FREQUENT) | **congenital** | fixed/progressive | physical sign |
| Macrocephaly | `HP:0000256` Macrocephaly | 43% (FREQUENT) | congenital/infantile | — | physical sign |
| Absent speech | `HP:0001344` Absent speech | most (within the 88%) | — | — | clinical sign |
| Non-ambulatory | `HP:0002540` Inability to walk | most (within the 88%) | — | — | clinical sign |
| Early death | `HP:0001522` Death in infancy *(approximate — timing not precisely specified in abstract)* | subset | — | — | outcome |
| Abundant epileptiform EEG activity | `HP:0011185` EEG with focal epileptiform discharges / `HP:0002353` EEG abnormality | defining | infantile | — | lab/electrophysiology |

**Additional phenotypes from the non-epilepsy cohort (Royer-Bertrand 2021, PMID:34702355):**

| Phenotype | HPO term | Notes |
|---|---|---|
| Intellectual disability | `HP:0001249` Intellectual disability | 7/7 in that cohort |
| Developmental regression | `HP:0002376` Developmental regression | variable presence |
| ASD-like behavioral profile | `HP:0000717` Autism | "social cognition deficit" |
| Severe speech/language delay | `HP:0000750` Delayed speech and language development | "marked" |
| Global developmental delay | `HP:0001263` Global developmental delay | shared feature |
| **Absence** of epilepsy | — | the defining negative of this subgroup |

Verbatim: they found seven unrelated individuals with **"intellectual disability, developmental regression and ASD-like behavioral profile, and notably without epilepsy"** carrying de novo pathogenic *CACNA1E* variants (**PMID:34702355**) *[fetched this session]*.

### The seizure/movement-disorder trap — important for curation

Here's a wrinkle worth its own paragraph, because it undermines the neatness of the 60%-movement-disorder figure. When someone finally put a *CACNA1E* patient (p.Gly352Arg) on long-term video-EEG, some of the "movement disorder" turned out to be seizures wearing a costume:

> long-term video-EEG revealed "tonic asymmetric seizures during wakefulness and mild paroxysmal dyskinesias of the trunk out of sleep which were thought to be a movement disorder and instead turned out to be focal hyperkinetic seizures."
> — Di Micco et al., *Epileptic Disord* 2024 (**PMID:38780451**) *[fetched this session]*

The authors call this **the first documented description of the EEG findings in this disorder** and note "a possible overlap between cortical and subcortical phenomena." So: some fraction of the reported dyskinesia burden is probably ictal, not extrapyramidal. Curate the movement-disorder phenotype with that caveat attached — it's a genuine open question, not a settled observation.

### Quality of life

No EQ-5D, SF-36, PROMIS, or disease-specific QoL instrument has been applied to this population. **Nothing to cite.** Qualitatively, the profile — nonverbal, nonambulatory, refractory seizures, contractures, spastic quadriplegia, movement disorder — implies total dependence for all activities of daily living and a very high caregiver burden, but that inference is mine, not a published measurement. Curate it as description, not evidence.

---

## 4. Genetic / Molecular Information

### The gene and its product

*CACNA1E* (1q25.3) encodes the ~2,251–2,270 aa, ~255–257 kDa α1E subunit — the pore-forming, voltage-sensing core of Ca_V2.3. Canonical four-domain (I–IV) architecture, each domain six transmembrane helices (S1–S6): S4s are the voltage sensors, S5–S6 line the pore, and the **cytoplasmic ends of the four S6 helices form the activation gate** where the disease variants live.

The channel carries the **R-type** current — historically "R for Resistant," since it's the high-voltage-activated current left standing after you block L, N, P, and Q types. From the abstract:

> "CACNA1E is highly expressed in the CNS and is the pore-forming subunit of the voltage-gated calcium channel CaV2.3, which conducts high voltage-activated R-type calcium currents that initiate synaptic transmission."
> — **PMID:30343943** *[cached & validated]*

### Variant classes

**Class 1 — GOF missense at the S6 activation gate (the disease-defining class).** 14 partially recurring variants across 30 individuals in the founding cohort; ACMG classification pathogenic/likely pathogenic; **germline de novo**; absent from gnomAD.

| Domain | n | Hotspot | Phenotype signature |
|---|---|---|---|
| **DI-S6** | 10 | **p.Gly352Arg** (9/10) | *all 10* had hyperkinetic movement disorder, vs only 2/19 with variants elsewhere |
| **DII-S6** | 13 | **p.Ala702Thr** (6/13) | "the majority... presented with all clinical features" — full spectrum |
| **DIII-S6** | — | — | **mildest end**: 2 never developed seizures; one seizure-free 5 years, spoke single words, walked independently |
| DII S4–S5 linker | ≥1 | — | facilitated activation **+ increased current density** |

Verbatim genotype–phenotype quotes (all **PMID:31064215**, *cached & validated*):

> "Ten individuals carried missense variants in the DI-S6 domain, including 9 individuals with the recurrent p.Gly352Arg variant; all 10 individuals presented with hyperkinetic movement disorders, compared with only (2/19) individuals with variants outside this domain."

> "In contrast, patients with missense variants located in the DIII-S6 presented with a milder phenotype, as 2 patients never developed seizures and one has been seizure-free for 5 years, spoke single words, and walked independently."

**Class 2 — truncating variants (rare, milder, mechanistically murky).**

> "an additional 3 individuals with truncating CACNA1E variants were identified, including 1 somatic mosaic (27% of cells), 1 inherited from an unaffected parent, and 1 with unknown inheritance. All 3 individuals presented with a much milder phenotype"
> — **PMID:31064215** *[cached & validated]*

This class matters out of proportion to its size: an unaffected transmitting parent means truncating *CACNA1E* alleles are **not straightforwardly pathogenic**, and it means the disease is not simply "too much or too little Ca_V2.3" on a single dial. Curate these as a distinct, uncertain class.

**Class 3 — the non-epilepsy neurodevelopmental variants.** Seven de novo variants (six missense, one splice-donor **c.3422+1G>A** predicted to disrupt the exon 22 donor site) producing ID/regression/ASD without seizures. Functional validation was explicitly **not** performed — Royer-Bertrand et al. list "lacks functional validation" among their own limitations. So we don't know whether these are GOF, LOF, or something else.

### Functional consequence — the biophysics

Two independent GOF flavors, both documented:

> "Functional analysis of several S6 variants revealed consistent gain-of-function effects comprising facilitated voltage-dependent activation and slowed inactivation."
> — **PMID:30343943** *[cached & validated, IN_VITRO]*

> "Another variant located in the domain II S4-S5 linker results in facilitated activation and increased current density."
> — **PMID:30343943** *[cached & validated, IN_VITRO]*

> "Electrophysiological recordings showed a hyperpolarizing shift in voltage-dependent activation, slowed kinetics of inactivation, and increased current density."
> — **PMID:31064215** *[cached & validated, IN_VITRO]*

Put plainly: the gate opens at voltages where it shouldn't, and then dawdles about shutting. Two independent leaks in the same faucet.

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifiers:** none identified.
- **Epigenetics:** no methylation episignature has been reported for *CACNA1E* (unlike, say, several other NDD genes with published episignatures). **Nothing to curate.**
- **Chromosomal abnormalities:** DEE69 is not a CNV/microdeletion syndrome. ClinGen has a dosage-sensitivity curation page for HGNC:1392 (`search.clinicalgenome.org/kb/gene-dosage/HGNC:1392`), but the site refused connection during this session — **fetch the haploinsufficiency/triplosensitivity scores directly before curating them.**
- **Somatic vs germline:** germline de novo for the missense class; one documented **somatic mosaic** truncating case (27% of cells).

---

## 5. Environmental Information

Short section, honestly stated: **no environmental, lifestyle, toxicological, or infectious contribution is described for this disorder.** It's a de novo monogenic channelopathy. CTD/TOXNET-style exposure associations for *CACNA1E* as a gene exist in the general toxicogenomics literature but have **no established relationship to DEE69** — don't import them.

The only environment-adjacent factor with any mechanistic footing is **fever/illness as a generic seizure precipitant** in DEEs, and I found no *CACNA1E*-specific fever-sensitivity data. (Contrast this with `Timothy_Syndrome` in this KB, where a fever-exacerbation hypothesis *is* explicitly modeled — resist the temptation to copy that pattern here without evidence.)

One genuinely interesting modulator, though, and it's ionic rather than environmental: Ca_V2.3 is the classic **zinc- and copper-sensitive** calcium channel, and trace-metal modulation shapes convulsive seizure behavior in mice (**PMID:32068980**). That's a real biological handle on the channel, but it is model-organism pharmacology, not a human risk factor.

---

## 6. Mechanism / Pathophysiology

### The causal chain

Here's the pathograph as I'd model it — five nodes, molecular → organism:

```
CACNA1E S6-gate GOF variant          [MOLECULAR — trigger]
   ↓ DIRECT
Increased neuronal Ca²⁺ influx        [CELLULAR — central effector]
   ↓ DIRECT
Altered excitability + transmitter release   [CELLULAR — intermediate]
   ├─ DIRECT ──→ Neuronal hyperexcitability / E-I imbalance   [TISSUE — central effector]
   │                 ├─→ Developmental and epileptic encephalopathy
   │                 └─→ Refractory infantile-onset seizures
   └─ INDIRECT ─→ Impaired neurodevelopment                   [ORGANISM — outcome]
                     ├─→ Profound developmental impairment
                     ├─→ Hyperkinetic movement disorder
                     └─→ Spastic quadriplegia
```

**Node 1 — the leaky gate (MOLECULAR).** GOF missense at the S6 activation gate: facilitated (hyperpolarized) activation + slowed inactivation, sometimes plus increased current density. GO: `GO:0005245` voltage-gated calcium channel activity (INCREASED), `GO:0008331` high voltage-gated calcium channel activity (INCREASED).

**Node 2 — calcium overload (CELLULAR).** Ca_V2.3 lives in *both* compartments — presynaptic terminals and the somatodendritic membrane — so a gating defect raises Ca²⁺ at both ends of the neuron simultaneously. GO: `GO:0070588` calcium ion transmembrane transport (INCREASED), `GO:0019722` calcium-mediated signaling. CHEBI: `CHEBI:29108` calcium(2+).

**Node 3 — deranged synaptic signaling (CELLULAR).**

> "CACNA1E encodes Cav2.3, an R-type VGCC implicated in both presynaptic neurotransmitter release and postsynaptic somatodendritic integration and long-term potentiation."
> — **PMID:31064215** *[cached & validated]*

GO: `GO:0007269` neurotransmitter secretion (DYSREGULATED), `GO:0042391` regulation of membrane potential (ABNORMAL), `GO:0060291` long-term synaptic potentiation.

**Node 4 — network hyperexcitability (TISSUE).** This node `conforms_to` the KB's existing `epilepsy_excitation_inhibition_imbalance#Neuronal Hyperexcitability and Hypersynchrony` module — a clean conformance target.

> "We establish pathogenic variants in CACNA1E as a cause of DEEs and suggest facilitated R-type calcium currents as a disease mechanism for human epilepsy and developmental disorders."
> — **PMID:30343943** *[cached & validated]*

The cell-biological gearing was worked out in rodent CA1: Ca_V2.3 "triggers epileptiform activity in specialized neurons via plateau potentials and afterdepolarizations" (**PMID:16686648**). That's the specific machinery — R-type calcium entry sustains a depolarizing plateau after the spike, so instead of one action potential you get a burst, and instead of a burst you get a seizure. A dripping tap that never quite shuts off, and eventually the whole basin overflows in rhythm.

**Node 5 — developmental encephalopathy (ORGANISM).** Critically: the developmental impairment is **not merely post-ictal damage**. Two independent lines say so. (a) DIII-S6 patients who *never seized* still had disease; (b) the entire Royer-Bertrand cohort had ID/regression/ASD **without epilepsy**. Calcium is a developmental signaling currency — activity-dependent transcription, synapse refinement, circuit sculpting — so chronic mis-set calcium during a critical window degrades development independently of seizures. Curate the "developmental" and "epileptic" arms as parallel consequences, not as a cascade.

### The CDKL5 convergence — the best mechanism news in this field

This one is genuinely elegant. Working *from the other end* — trying to figure out what the kinase CDKL5 actually phosphorylates — Sampedro-Castañeda et al. landed squarely on Ca_V2.3:

> "We identified the voltage-gated Ca2+ channel Cav2.3 (encoded by CACNA1E) as a physiological target of CDKL5 in mice and humans. Recombinant channel electrophysiology and interdisciplinary characterization of Cav2.3 phosphomutant mice revealed that loss of Cav2.3 phosphorylation leads to channel gain-of-function via slower inactivation and enhanced cholinergic stimulation, resulting in increased neuronal excitability. Our results thus show that CDD is partly a channelopathy. The properties of unphosphorylated Cav2.3 closely resemble those described for CACNA1E gain-of-function mutations causing DEE69, a disorder sharing clinical features with CDD. We show that these two single-gene diseases are mechanistically related and could be ameliorated with Cav2.3 inhibitors."
> — *Nat Commun* 2023 (**PMID:38081835**) *[fetched this session]*

Read that again, because it's a two-gene convergence onto one channel state. In DEE69 the channel is broken open by a variant in its own gate. In CDKL5 deficiency disorder the channel is *structurally fine* but nobody's phosphorylating it, and unphosphorylated Ca_V2.3 behaves like a DEE69 mutant. Same phenotypic destination, two different roads — like two mutations in different enzymes of one pathway causing the same metabolite to pile up.

For this KB that suggests something concrete: a shared mechanism node ("Ca_V2.3 gain-of-function state") that both `CACNA1E-Related_DEE` and the existing CDKL5 entry could point at. Worth raising as a module candidate.

Additional GO terms for the CDKL5 arm: `GO:0006468` protein phosphorylation, `GO:0004674` protein serine/threonine kinase activity, and note the **enhanced cholinergic stimulation** finding (`GO:0007271` synaptic transmission, cholinergic).

### Protein structure

Two cryo-EM structures now anchor the mechanism in atoms:

- **Human Ca_V2.3 + α2δ-1 + β3, 3.1 Å** — "structural and electrophysiological characterizations showed that the CH2II helix stabilizes the inactivated conformation of the channel by tightening the cytosolic juxtamembrane segments" (**PMID:36446785**, *Nat Commun* 2022; PDB entries deposited with that paper).
- **Human Ca_V2.3 + α2δ1 + β1 gating-mechanism structures** — *Nat Commun* 2023, DOI 10.1038/s41467-023-36260-2.

Both papers frame Ca_V2.3 as a drug target "for pain, seizures, epilepsy, and Parkinson's disease." **These structures were not available when the 2018 disease paper was written**, so nobody has yet published a structure-mapped analysis of the DEE69 variant set onto the resolved gate. That's a very tractable open question and a good `KNOWLEDGE_GAP` candidate.

### Not applicable / no data

- **Metabolic changes:** no metabolomic or energy-metabolism data. Nothing.
- **Immune involvement:** none described. Not an inflammatory disease.
- **Tissue damage mechanisms:** the only relevant thread is excitotoxicity, and it comes from mice — Ca_V2.3-null mice are protected from kainate excitotoxic cell death (**PMID:17376845**). Whether excitotoxic neuronal loss contributes in human DEE69 is **unknown**; no neuropathology series exists.
- **Transcriptomics / proteomics / metabolomics / lipidomics / single-cell / spatial / multi-omics in patients:** **none published.** The only omics that touched this disease is the SILAC phosphoproteomic screen in PMID:38081835 — and that was mouse/human neuronal material studying CDKL5, not patient tissue.
- **Functional genomics screens:** no CRISPR/RNAi screen targeting *CACNA1E* in a disease-relevant readout.

---

## 7. Anatomical Structures Affected

**Primary:** the central nervous system, full stop. *CACNA1E* is "highly expressed in the CNS."

| Level | Structure | Ontology term | Basis |
|---|---|---|---|
| Organ | brain | `UBERON:0000955` | primary site |
| Organ system | central nervous system | `UBERON:0001017` | — |
| Region | cerebral cortex | `UBERON:0000956` | seizure origin; focal hyperkinetic seizures on EEG |
| Region | hippocampal formation | `UBERON:0002421` | CA1 plateau-potential mechanism (rodent) |
| Region | basal ganglia | `UBERON:0002420` | movement-disorder substrate (**inferred**, not imaged) |
| Region | substantia nigra pars compacta | `UBERON:0002965` | high Ca_V2.3 in nigral DA neurons (mouse; PD-relevant, not DEE-demonstrated) |
| Tract | corticospinal / spinal cord | `UBERON:0002240` | spastic quadriplegia implies UMN involvement |
| Secondary | skeletal joint | `UBERON:0000982` | congenital contractures |
| Secondary | skeletal musculature | `UBERON:0001015` | hypotonia → spasticity |
| Head | cranium / head | `UBERON:0000033` | macrocephaly |

**Cell types:**

| Cell | CL term | Note |
|---|---|---|
| neuron (generic) | `CL:0000540` | the safe default; the founding papers don't resolve cell type |
| glutamatergic neuron | `CL:0000679` | inferred from excitatory network mechanism |
| GABAergic neuron | `CL:0000617` | inferred; E-I imbalance implies both sides — **which side dominates is unknown** |
| pyramidal neuron | `CL:0000598` | CA1 plateau-potential mechanism (rodent) |
| dopaminergic neuron | `CL:0000700` | Ca_V2.3-rich in SNc (mouse; relevant to channel biology, not proven in DEE69) |

**Subcellular (GO cellular component):**
- `GO:0005891` voltage-gated calcium channel complex
- `GO:0005886` plasma membrane
- `GO:0043195` terminal bouton (presynaptic pool)
- `GO:0030425` dendrite / `GO:0043197` dendritic spine (somatodendritic pool)
- `GO:0042995` neuron projection

**Lateralization:** bilateral/diffuse for the encephalopathy. Notably, Di Micco et al. recorded **tonic asymmetric seizures** — so ictal semiology can be asymmetric even on a diffuse substrate. No structural brain malformation is a consistent feature; **no systematic neuroimaging series has been published**, which is itself a notable gap given that macrocephaly is in 43% of patients and nobody has characterized what's under those large skulls.

---

## 8. Temporal Development

**Onset.** Congenital for the structural features (contractures are present at birth — `HP:0002803`); infantile for the epilepsy. **Median seizure onset 4.5 months** (PMID:31064215). Hypotonia is a neonatal/early-infantile finding. The onset pattern is best described as congenital-plus-early-infantile rather than acute: the machinery was mis-set before birth, and the seizures are when it becomes audible.

**Progression.** No staging system exists for this disease. What can be said from the cohort:

- Seizures are **refractory from the start** — this is not a disorder with a good honeymoon period.
- Development is profoundly impaired and most patients never acquire speech or ambulation (88%) — so it reads as **severe static-to-slowly-worsening impairment**, not a neurodegenerative course. But **no longitudinal study exists**, so "static vs. progressive" is genuinely unresolved. Curate with `PROGRESSIVE` only if the schema demands a value, and flag it.
- Tone evolves: severe early hypotonia in many patients coexists with or gives way to spastic quadriplegia (53%).
- **Early death occurred in a subset** — "often with congenital contractures, macrocephaly, hyperkinetic movement disorders, and early death" (**PMID:30343943**). The abstract does not give a mortality rate or age distribution. **Do not invent one.**

**Milder trajectories exist and matter.** The DIII-S6 patients — some never seizing, one seizure-free five years with single words and independent walking — plus the entire truncating class ("much milder phenotype") and the whole non-epilepsy cohort together tell you this is a **spectrum**, not a monolith. Prognostic counseling anchored only on the severe DI/DII-S6 picture would be wrong for a meaningful minority.

**Remission.** Spontaneous remission not described. Treatment-induced seizure freedom is documented in five topiramate-treated participants (see §12) — that's the one bright spot in the course data.

**Critical periods.** No intervention-window data exist. Mechanistically, the developmental arm implies an early window (calcium-dependent circuit assembly in infancy), which would argue for early diagnosis and early mechanism-matched treatment — but this is a **hypothesis**, not a demonstrated therapeutic window.

---

## 9. Inheritance and Population

**Inheritance:** autosomal dominant, **essentially always de novo**. `HP:0000006` Autosomal dominant inheritance.

**Penetrance:** for the recurrent GOF missense class, apparently complete — every reported carrier is affected. For the **truncating** class, penetrance is clearly *incomplete*: one such variant was **inherited from an unaffected parent**.

**Expressivity:** highly variable, and — unusually for a rare disease — partly *predictable* from variant location. DI-S6 → movement disorder in 10/10. DIII-S6 → milder, sometimes seizure-free. That domain-level genotype–phenotype correlation is one of the most curation-valuable facts in this entry.

**Germline mosaicism:** not reported. **Somatic mosaicism** is documented once (truncating variant, 27% of cells). Parental mosaicism has not been reported but cannot be excluded — relevant to recurrence-risk counseling.

**Anticipation:** not applicable (not a repeat-expansion disorder).

**Founder effects / carrier frequency / consanguinity:** all **not applicable**. De novo dominant disorders don't have carriers, founders, or a consanguinity signal.

**Epidemiology:**
- **Prevalence: not established.** No population estimate exists.
- The only defensible curation is a `CASES_IN_LITERATURE` measure: 30 individuals in the founding cohort, plus 7 in the non-epilepsy cohort, plus scattered case reports — on the order of **40–50 published individuals** as of mid-2026. Prevalence class: `ULTRA_RARE`.
- **Incidence:** unknown.
- *CACNA1E* is a recognized contributor to the DEE gene pool but a numerically small one; it sits on the **Genomics England PanelApp epileptic-encephalopathy panel** and is reported as **ClinGen "Definitive"** for gene–disease validity with DEE69 *(per ClinGen/GenCC search results this session — the ClinGen site itself refused connection, so **verify the assertion ID and date before citing a CGGV reference**)*.

**Demographics:** the founding cohort was an international GeneMatcher-assembled series with no reported ethnic clustering — expected, since de novo mutation doesn't respect ancestry. **No sex ratio has been reported**, and there's no biological reason to expect skew (autosomal, dominant, de novo). Age distribution of living patients is unstudied.

---

## 10. Diagnostics

### Genetic testing — the whole ballgame

Diagnosis is molecular. There is no biochemical marker, no imaging signature, no functional test that makes this diagnosis.

> "Using next-generation sequencing techniques, we identified de novo CACNA1E variants in 30 individuals with DEE"
> — **PMID:30343943** *[cached & validated]*

Recommended approach, in order of yield:
1. **Epilepsy/DEE gene panel** or **exome (WES)** as first-tier for infantile-onset refractory epilepsy with developmental impairment. *CACNA1E* is on major DEE panels (Genomics England PanelApp panel 67, green).
2. **Genome (WGS)** when panel/exome is negative — better for the splice-region and non-coding space (note the c.3422+1G>A splice-donor variant class).
3. **Trio testing** — parental samples are essentially required, because de novo status is a major ACMG evidence line (PS2) for a gene where most missense is otherwise hard to classify.
4. **Single-gene testing** — only for targeted confirmation/cascade, not for discovery.
5. **CMA / karyotype / FISH:** appropriate as general NDD workup but **not informative for this diagnosis** — DEE69 is not a CNV syndrome.
6. **Mitochondrial DNA testing / repeat-expansion testing:** not applicable.

**Variant interpretation tips specific to this gene:** location is evidence. A missense at the cytoplasmic end of an S6 helix — especially at Gly352 or Ala702 — in a de novo trio configuration is a very different animal from a truncating variant, which may be benign or mildly-acting (an unaffected parent carried one). Royer-Bertrand's substitution-intolerance mapping against gnomAD provides a useful PM1-style regional argument.

MAXO: `MAXO:0000533` molecular genetic testing.

### EEG

> "abundant epileptiform activity on EEG"
> — **PMID:30343943** *[cached & validated]*

And, crucially, **long-term video-EEG is not optional** in this disease. Di Micco et al.'s case is the argument: routine assessment called the trunk paroxysms a movement disorder; video-EEG called them focal hyperkinetic seizures. That changes treatment. Their paper is the **first published EEG characterization** of the disorder — meaning the electroclinical phenotype is, at this point, an n-of-1.

MAXO: `MAXO:0000932` electroencephalography.

### Other modalities — status honestly reported

- **Laboratory / biochemical tests:** no diagnostic lab abnormality. No LOINC-codeable analyte. Routine metabolic workup is normal (and is typically done to exclude mimics).
- **Biomarkers:** **none** — not diagnostic, not prognostic, not pharmacodynamic. This is a real gap; a Ca_V2.3-function biomarker would be transformative for trial design.
- **Imaging (MRI):** no consistent malformation reported; no published imaging series. Given 43% macrocephaly, the absence of a systematic neuroimaging study is conspicuous.
- **Biopsy / histopathology:** no neuropathology series published. Not applicable clinically.
- **Functional/electrophysiology beyond EEG:** patch-clamp of variant channels is a **research** assay (heterologous expression), not a clinical test — though it's how the GOF mechanism was established and how a future variant-function service could work.
- **Omics-based diagnostics** (RNA-seq for the splice variants, proteomics, metabolomics, methylation episignature, liquid biopsy): **none validated.** RNA-seq is the one with a plausible near-term role, for splice-region variants like c.3422+1G>A.

### Clinical criteria and differential diagnosis

No society-issued diagnostic criteria exist for DEE69 specifically. The syndrome is diagnosed as an ILAE-framework DEE plus a *CACNA1E* molecular result.

**Differential diagnosis** — the phenotype (infantile refractory seizures + profound impairment + hypotonia + movement disorder ± contractures ± macrocephaly) overlaps heavily with:

| Differential | Distinguishing feature |
|---|---|
| **CDKL5 deficiency disorder (CDD/DEE2)** | Clinically the closest — and now known to be **mechanistically related** via Ca_V2.3 phosphorylation (PMID:38081835). Distinguished by gene; CDD has classic hypsarrhythmia-adjacent EEG and epileptic spasms |
| **STXBP1 encephalopathy** | Synaptic-vesicle release mechanism rather than channelopathy |
| **CACNA1A spectrum** | Ataxia/hemiplegic migraine features; different Ca_V (2.1) |
| **CACNA1D, CACNA1G GOF encephalopathies** | Other calcium channelopathies with the same S6-hotspot logic — gene-level testing separates them |
| **SCN2A / SCN8A / KCNQ2 DEEs** | Sodium/potassium channelopathies; different ASM responsiveness profiles |
| **Arthrogryposis syndromes** | When contractures dominate the neonatal picture, DEE69 can masquerade as a primary contracture syndrome |
| **Cerebral palsy (dyskinetic/spastic quadriplegic)** | The single most likely *misdiagnosis* — profound impairment + spastic quadriplegia + dyskinesia without a clear acquired cause should trigger genetic testing |

### Screening

**Not applicable.** No newborn screening (de novo, no treatable metabolic marker), no carrier screening (no carriers), no cascade screening (parents are unaffected non-carriers in essentially all cases). Prenatal/preimplantation testing is only relevant for the rare family with proven parental mosaicism.

---

## 11. Outcome / Prognosis

Thin evidence, plainly stated.

**Mortality.** "Early death" is named in the founding abstract as an outcome in a subset (**PMID:30343943**). **No mortality rate, no median survival, no cause-of-death breakdown has been published.** By analogy with other severe DEEs, SUDEP, status epilepticus, and respiratory infection are the expected contributors — but that's inference, not data. **Do not curate a survival percentage.**

**Morbidity.** This is where the picture is unambiguous and severe: 88% nonverbal and nonambulatory. Add 53% spastic quadriplegia, 43% contractures, 60% movement disorder, 87% refractory epilepsy. Functionally that's total dependence for feeding, mobility, communication, and personal care — GMFCS-V-equivalent territory, though nobody has formally scored this cohort.

**Quality of life measures:** none applied. No EQ-5D, PROMIS, or disease-specific instrument. **Genuine gap.**

**Complications** (expected, largely uncurated in the literature): status epilepticus, aspiration and respiratory infection, feeding difficulty/failure to thrive, orthopedic sequelae of contractures and spasticity (hip dislocation, scoliosis), and the medication burden of polytherapy.

**Recovery potential:** none for the developmental impairment. Seizure freedom is achievable in a minority (topiramate, n=5).

**Prognostic factors — the one real signal:** **variant domain.**
- DI-S6 / p.Gly352Arg → predicts hyperkinetic movement disorder (10/10).
- DII-S6 / p.Ala702Thr → predicts the full severe spectrum.
- DIII-S6 → predicts a milder course, potentially seizure-free with speech and ambulation.
- Truncating → "much milder phenotype."

That's an unusually clean structure-to-prognosis map for a disease this young, and it should be the headline prognostic content of the KB entry.

**Prognostic biomarkers:** none.

---

## 12. Treatment

### Topiramate — the mechanism-matched option

This is the therapeutic centerpiece, and it's a lovely bit of pharmacological serendipity: the drug that worked is a drug that blocks the very current the mutation amplifies.

> "Five participants achieved seizure freedom on the anti-epileptic drug topiramate, which blocks R-type calcium channels."
> — **PMID:30343943** *[cached & validated]*

Corroborated independently:

> "Topiramate, an antiseizure drug (ASM) acting on CaV2.3 channels, has been identified as an effective treatment option in some patients."
> — Lauerer & Lerche, **PMID:37822150** *[fetched this session]*

And notably it isn't only a seizure drug here — in the **non-epilepsy** cohort, "one patient demonstrated clinical improvement with topiramate" (**PMID:34702355**), hinting that lowering R-type current might touch the developmental/behavioral arm too.

Curation pattern for this KB:
```yaml
- name: Topiramate
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: Pharmacotherapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}
    therapeutic_agent:
    - preferred_term: topiramate
      term: {id: CHEBI:63631, label: topiramate}
  target_mechanisms:
  - target: Increased Neuronal Calcium Influx
    treatment_effect: INHIBITS
```

**Caveats worth stating in the entry:** n=5, uncontrolled, retrospective, in a cohort where 87% had refractory epilepsy — so this is a promising signal, not an established standard of care. Topiramate is also a dirty drug pharmacologically (sodium channels, GABA-A, AMPA/kainate, carbonic anhydrase, *and* R-type calcium), so the R-type attribution is mechanistically plausible rather than proven.

### The rest of the pharmacological picture

**Nothing else has published efficacy data in this disorder.** Standard DEE polytherapy applies by default (levetiracetam, valproate, benzodiazepines, vigabatrin, ketogenic diet, etc.), but I found **no *CACNA1E*-specific response data for any of them** and won't invent it. Seizures are described as pharmacoresistant as a rule.

**Pharmacogenomics:** none specific to this disease. Standard ASM pharmacogenetics (e.g. HLA-B*15:02 for aromatic ASMs) applies as it does to any epilepsy patient, not as a disease feature.

### Advanced therapeutics — where things could go

- **Selective Ca_V2.3 blockade** is the obvious precision-therapy target, and it now has three independent endorsements: the topiramate signal, the mouse KO anticonvulsant phenotype, and the CDKL5 paper's explicit conclusion that both diseases "could be ameliorated with Cav2.3 inhibitors" (**PMID:38081835**). The two cryo-EM structures (**PMID:36446785** and *Nat Commun* 2023) provide the structural basis for rational design.
  **But:** the only well-characterized selective blocker is **SNX-482**, a tarantula-venom peptide gating modifier (IC₅₀ ~30 nM) — a research tool, not a drug. It's a peptide, it partitions into membranes, it isn't CNS-deliverable. **There is no clinical-stage selective Ca_V2.3 antagonist.**
- **Gene therapy / gene editing:** nothing. And note the design difficulty — this is a *gain-of-function dominant* disorder, so the useful strategy is allele-specific knockdown (ASO or RNAi against the mutant allele), not gene replacement. No program exists.
- **ASO therapy:** no program. Mechanistically it's a reasonable fit for the recurrent hotspot variants (p.Gly352Arg, p.Ala702Thr are shared across many patients — exactly the economics that make an allele-specific ASO feasible). Purely prospective.
- **Cell therapy, immunotherapy, targeted small-molecule oncology-style therapy:** not applicable.

### Surgical, supportive, rehabilitative

No epilepsy-surgery data (the encephalopathy is generalized/diffuse, so resective surgery is unlikely to apply; VNS/palliative approaches unreported). Orthopedic management of contractures and spasticity is expected practice, unreported in the literature.

Multidisciplinary supportive and developmental care is the practical mainstay: physical/occupational/speech therapy, spasticity and dystonia management, feeding support, seizure management, orthopedic surveillance.

**MAXO suggestions:**
- `MAXO:0000533` molecular genetic testing (diagnostic)
- `MAXO:0000932` electroencephalography (diagnostic)
- `MAXO:0000079` genetic counseling
- `MAXO:0000011` physical therapy
- `MAXO:0000950` supportive care
- `MAXO:0000004` surgical procedure (contracture release — *inferred practice, uncited*)
- `MAXO:0000088` dietary intervention (ketogenic diet — *inferred, no CACNA1E-specific data*)
- `NCIT:C15747` Supportive Care, `NCIT:C15986` Pharmacotherapy

### Clinical trials

**Search result: no interventional trial specific to CACNA1E-related DEE or DEE69 was identified.** Patients may be eligible for general DEE natural-history or platform studies, but no NCT identifier can be attached to this disease with confidence. **Verify against ClinicalTrials.gov directly before curating any `clinical_trials` block.**

---

## 13. Prevention

Bluntly: this section is mostly "not applicable," and saying so is more useful than padding it.

- **Primary prevention: not possible.** De novo mutation isn't preventable by any known behavioral, nutritional, or environmental intervention.
- **Secondary prevention (early detection):** the meaningful action is **early genetic diagnosis** — rapid trio exome/genome in an infant with refractory seizures and profound impairment. Earlier diagnosis buys mechanism-matched ASM selection (topiramate), stops the diagnostic odyssey, and enables accurate counseling. Whether early treatment changes the developmental trajectory is **unknown but mechanistically plausible**.
- **Tertiary prevention:** seizure control, aspiration/respiratory-infection prevention, contracture and hip-dislocation surveillance, nutritional support, status-epilepticus rescue planning. Standard severe-DEE management; nothing disease-specific published.
- **Immunization:** routine childhood schedule; no disease-specific vaccine strategy. (Standard practice for severe epilepsy applies — vaccinate, with fever management.)
- **Population screening:** not applicable — no newborn or carrier screening rationale.
- **Genetic counseling:** the real deliverable. Message: de novo dominant, **recurrence risk low but not zero** because parental gonadal mosaicism can't be excluded (and somatic mosaicism is documented in this gene). Prenatal testing available for a known familial variant. Domain-specific prognostic information (DI-S6 → movement disorder; DIII-S6 → milder) belongs in the counseling conversation.
- **Public health / environmental interventions:** not applicable.
- **Prophylaxis:** none established.

---

## 14. Other Species / Natural Disease

**Orthologs:**

| Species | NCBI Taxon | Gene | Identifier |
|---|---|---|---|
| Human | `NCBITaxon:9606` | *CACNA1E* | HGNC:1392, NCBI Gene 777 |
| Mouse | `NCBITaxon:10090` | *Cacna1e* | **MGI:106217** ("calcium channel, voltage-dependent, R type, alpha 1E subunit") |
| Rat | `NCBITaxon:10116` | *Cacna1e* | RGD (ortholog exists; ID not verified this session) |
| Zebrafish | `NCBITaxon:7955` | *cacna1e* paralog(s) | ZFIN carries a human-disease page for DOID:0112205; **paralog naming not verified — check ZFIN before curating** |

**Naturally occurring disease in other species:** I found **no OMIA entry or veterinary case literature** describing a spontaneous *CACNA1E* disorder in companion animals or livestock. Report as "not identified," not as "does not exist" — absence of a search hit in a rare-gene space isn't proof.

**Breed (VBO):** not applicable — no breed-associated natural disease known.

**Comparative biology:** Ca_V2.3 is deeply conserved across vertebrates in both sequence and function; the R-type current, its zinc/copper sensitivity, and its presynaptic/somatodendritic dual localization are conserved features. The knockout mouse's seizure-resistance phenotype (§15) is the mirror image of the human GOF disease — which is about as good a cross-species mechanistic validation as you get without a knock-in.

**Zoonotic potential / cross-species transmission:** not applicable (genetic disorder).

---

## 15. Model Organisms

### Mouse — the workhorse, and the evidence is strong

**Constitutive *Cacna1e* knockout (Ca_V2.3⁻/⁻).** These mice are the inverse-mechanism proof that Ca_V2.3 activity is pro-epileptogenic:

> "PTZ-induced seizure susceptibility was dramatically reduced in Ca(v)2.3-deficient mice, whereas 4-AP sensitivity remained unchanged."
> — Weiergräber et al., *Epilepsia* 2006 (**PMID:16686648**) *[fetched this session]*

> "Administration of kainic acid (30 mg/kg ip) revealed clear alteration in behavioral seizure architecture and dramatic resistance to limbic seizures in Ca(v)2.3(−/−) mice compared with controls." … "excitotoxic effects after kainic acid administration are absent in Ca(v)2.3(−/−) mice, whereas Ca(v)2.3(+/+) animals exhibited clear and typical signs of excitotoxic cell death."
> — Weiergräber et al., *J Neurophysiol* 2007 (**PMID:17376845**) *[fetched this session]*

And as summarized in the disease commentary:

> "Cav2.3 is also known to play a role in epileptogenesis in rodents, and its deletion reduces susceptibility to chemically induced seizures."
> — **PMID:31064215** *[cached & validated, MODEL_ORGANISM]*

Note the convulsant-specific pattern: protection against PTZ and kainate, **not** 4-AP. That's a mechanistic fingerprint, not blanket seizure resistance — Ca_V2.3 matters for particular routes into hypersynchrony.

Knockout mice also show normal brain structure, no spontaneous seizures, and no compensatory shifts in other calcium-channel expression — so the phenotype is attributable to the channel itself.

**Ca_V2.3 phosphomutant mouse (2023) — the most disease-relevant model that exists.** Sampedro-Castañeda et al. made mice in which the CDKL5 phosphorylation sites on Ca_V2.3 are ablated. The result: "loss of Cav2.3 phosphorylation leads to channel gain-of-function via slower inactivation and enhanced cholinergic stimulation, resulting in increased neuronal excitability," with properties that "closely resemble those described for CACNA1E gain-of-function mutations causing DEE69" (**PMID:38081835**). This is currently the **closest available in-vivo model of the DEE69 channel state** — an indirect GOF model rather than a patient-variant knock-in.

**Ca_V2.3 in nigral dopaminergic neurons.** Benkert et al., *Nat Commun* 2019 (**PMID:31704946**): Ca_V2.3 transcripts are the most abundant VGCC in mouse nigral neurons and rise with age; Ca_V2.3 knockout "afforded full protection from degeneration in vivo" in a neurotoxin Parkinson's model. Relevant here for **channel biology and the movement-disorder question**, not as a DEE69 model — but it's the reason people care about Ca_V2.3 selective blockers beyond epilepsy.

**Zinc/copper modulation:** PMID:32068980 — convulsive seizures are modulated in part by zinc ions through the pharmacoresistant Ca_V2.3 channel. Useful mechanistic color; not a disease model.

### The critical gap

**No patient-variant knock-in mouse exists.** Nobody has made a Ca_V2.3-p.Gly352Arg or -p.Ala702Thr animal. Every in-vivo statement about this disease is therefore either (a) inverse — what happens when you *remove* the channel — or (b) indirect, via the phosphomutant. That's the single biggest experimental gap in the field, and it's the natural `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH` to record: a knockout that is *protected* from seizures is not a model of a disease caused by *gain* of the same channel, however satisfying the logic feels.

### Cellular models

- **Heterologous expression (HEK/tsA-201 + α2δ and β subunits) with patch-clamp** — the workhorse for variant functional characterization; this is how the GOF mechanism was established (PMID:30343943).
- **Patient-derived iPSC neurons:** **none published for *CACNA1E*.** The commentary explicitly calls for them: "future studies in patient-derived iPSC are likely to shed light on pathogenic mechanisms and potential therapeutic targets" (PMID:31064215). Still true seven years on.
- **Organoids / MorPhiC:** *CACNA1E* is not among the MorPhiC anchor genes (ISL1, EOMES, GCM1, NKX2-1). No cellular-phenotype data to import.
- **Zebrafish:** ZFIN maintains a human-disease page for DOID:0112205, but I found no published *cacna1e* zebrafish disease model. Verify before asserting.

### Model resources

MGI (`MGI:106217`), IMPC/KOMP (check for *Cacna1e* allele availability), IMSR for strain sourcing, ZFIN, Alliance of Genome Resources for ortholog/phenotype integration.

---

## Curation notes — what I'd flag before this goes in the KB

**Solid, cite-able, already validated in this repo:** the founding cohort's clinical percentages, the S6-gate variant clustering, the GOF biophysics, the domain-level genotype–phenotype correlations, the truncating-variant caveat, and the topiramate signal. All of that has snippet-verified evidence in `references_cache/PMID_30343943.md` and `PMID_31064215.md`.

**New material worth adding to the existing entry** (all fetched this session — **run `just fetch-reference` and re-verify each snippet before committing**):
1. **PMID:34702355** — the non-epilepsy neurodevelopmental phenotype. This meaningfully broadens the entry beyond "DEE" and supports an ASD/ID phenotype block plus a `has_subtypes` or spectrum note.
2. **PMID:38081835** — the CDKL5–Ca_V2.3 convergence. Strong candidate for a cross-disease mechanism link and possibly a shared module node with the CDKL5 entry.
3. **PMID:38780451** — first EEG characterization; forces a caveat on the movement-disorder phenotype (some of it is ictal).
4. **PMID:37822150** — Lauerer & Lerche review; good general-mechanism citation and supports the shared distal-S6 hotspot claim across calcium-channel epilepsies.
5. **PMID:16686648 / PMID:17376845** — the primary mouse KO papers behind the existing `MODEL_ORGANISM` evidence, currently cited only secondhand through the commentary.
6. **PMID:36446785** — cryo-EM structure; enables a structural node and a variant-mapping knowledge gap.

**Things to verify, not assert:** the ClinGen CGGV assertion ID (site was unreachable), gnomAD constraint numbers (browser is JS-only), the Orphanet code, ClinGen dosage scores, zebrafish paralog names, and any ClinicalTrials.gov entry.

**Knowledge gaps worth encoding as `discussions`:**
- No patient-variant knock-in animal exists — everything in vivo is inverse or indirect (`HUMAN_MODEL_MISMATCH` fits better than `KNOWLEDGE_GAP` here, since evidence *exists* but its fidelity to the human GOF disease is the open question).
- No selective, CNS-deliverable Ca_V2.3 antagonist despite three converging lines of rationale (already partly captured in the existing entry's `gap_cacna1e_rtype_blocker_precision_therapy`).
- Truncating variants: benign, hypomorphic, or a distinct milder mechanism? An unaffected transmitting parent says the simple dose model is wrong.
- No structure-mapped analysis of the DEE69 variant set onto the 2022/2023 cryo-EM gate.
- No natural history, no imaging series, no neuropathology, no QoL instrument, no biomarker.

---

**Sources:**
- [De Novo Pathogenic Variants in CACNA1E Cause Developmental and Epileptic Encephalopathy with Contractures, Macrocephaly, and Dyskinesias — PubMed (PMID:30343943)](https://pubmed.ncbi.nlm.nih.gov/30343943/)
- [Calcium Channel Dysfunction in Epilepsy: Gain of CACNA1E — PubMed (PMID:31064215)](https://pubmed.ncbi.nlm.nih.gov/31064215/)
- [De novo variants in CACNA1E found in patients with intellectual disability, developmental regression and social cognition deficit but no seizures — PubMed (PMID:34702355)](https://pubmed.ncbi.nlm.nih.gov/34702355/)
- [Epilepsy-linked kinase CDKL5 phosphorylates voltage-gated calcium channel Cav2.3 — PubMed (PMID:38081835)](https://pubmed.ncbi.nlm.nih.gov/38081835/)
- [Seizure and movement disorder in CACNA1E developmental and epileptic encephalopathy — PubMed (PMID:38780451)](https://pubmed.ncbi.nlm.nih.gov/38780451/)
- [Voltage-gated calcium channels in genetic epilepsies (Lauerer & Lerche) — PMC11591408 (PMID:37822150)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11591408/)
- [Altered seizure susceptibility in mice lacking the Ca(v)2.3 E-type Ca2+ channel — PubMed (PMID:16686648)](https://pubmed.ncbi.nlm.nih.gov/16686648/)
- [Hippocampal seizure resistance and reduced neuronal excitotoxicity in mice lacking Cav2.3 — PubMed (PMID:17376845)](https://pubmed.ncbi.nlm.nih.gov/17376845/)
- [Structures of the R-type human Cav2.3 channel reveal conformational crosstalk — PubMed (PMID:36446785)](https://pubmed.ncbi.nlm.nih.gov/36446785/)
- [Molecular insights into the gating mechanisms of voltage-gated calcium channel CaV2.3 — Nature Communications 2023](https://www.nature.com/articles/s41467-023-36260-2)
- [Cav2.3 channels contribute to dopaminergic neuron loss in a model of Parkinson's disease — PubMed (PMID:31704946)](https://pubmed.ncbi.nlm.nih.gov/31704946/)
- [Experimentally Induced Convulsive Seizures Are Modulated in Part by Zinc Ions through the Pharmacoresistant Cav2.3 Calcium Channel — PubMed (PMID:32068980)](https://pubmed.ncbi.nlm.nih.gov/32068980/)
- [OMIM #618285 — Developmental and Epileptic Encephalopathy 69](https://www.omim.org/entry/618285) *(403 to automated fetch; identifiers cross-verified via MONDO xrefs)*
- [OMIM *601013 — CACNA1E gene](https://www.omim.org/entry/601013)
- [Genomics England PanelApp — CACNA1E (Epileptic encephalopathy panel)](https://panelapp.genomicsengland.co.uk/panels/67/gene/CACNA1E/)
- [GenCC — CACNA1E (HGNC:1392) submissions by classification](https://thegencc.org/genes/HGNC:1392)
- [ClinGen dosage sensitivity — CACNA1E](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:1392) *(connection refused during this session — verify manually)*
- [MGI:106217 — mouse Cacna1e](https://www.informatics.jax.org/marker/MGI:106217)
- [ZFIN human disease page — developmental and epileptic encephalopathy 69 (DOID:0112205)](https://zfin.org/DOID:0112205)
- [GTR — Developmental and epileptic encephalopathy, 69 (C4748988)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4748988/)
- [Orphanet — CACNA1E gene page](https://www.orpha.net/en/disease/gene/CACNA1E)