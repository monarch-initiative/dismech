---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-08-23T00:51:24.510468'
end_time: '2026-08-23T00:55:16.465293'
duration_seconds: 231.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tyrosinemia Type III
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8[1m]
  web_search_requests: 4
  num_turns: 10
  total_cost_usd: 1.6971217499999998
  session_id: 7db51bf0-0bc7-43a1-90d8-354abcfd99e6
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 13
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tyrosinemia Type III
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tyrosinemia Type III** covering all of the
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

I'll research Tyrosinemia Type III comprehensively. Let me start by loading web tools and examining the existing work already in progress on this branch.

The existing entry is thorough. Let me read the remainder and run targeted searches to verify and fill gaps.

Let me gather a few more details on enzyme/pathway biochemistry and comparative biology.

I now have sufficient material — the existing curated entry plus verification searches — to produce the comprehensive report.

---

# Comprehensive Research Report: Tyrosinemia Type III

**Disease:** Tyrosinemia Type III (HPD deficiency)
**MONDO ID:** MONDO:0010162 · **OMIM:** #276710 (disease), *609695 (HPD gene) · **Orphanet:** ORPHA:69723 · **Category:** Mendelian (autosomal recessive inborn error of metabolism)
**Report date:** 2026-08-23

> **Scope note.** Tyrosinemia type III (HT III) is genuinely ultra-rare: as of the 2022 literature summary only **19 biallelic-HPD patients** had been reported worldwide, and a 2025 count places it at ~23 definitively diagnosed cases. Consequently, essentially all clinical knowledge derives from **individual case reports and small case series**, not population-based or EHR-aggregated data. Frequencies, survival statistics, and dose-response relationships are largely undefined, and the report flags this throughout rather than manufacturing numbers.

---

## 1. Disease Information

**Overview.** Tyrosinemia type III is the rarest of the three genetic tyrosinemias — an autosomal recessive inborn error caused by biallelic loss-of-function variants in **HPD**, encoding **4-hydroxyphenylpyruvate dioxygenase (HPD/HPPD)**, the *second* enzyme of the tyrosine catabolic pathway. Loss of HPD activity blocks conversion of 4-hydroxyphenylpyruvate to homogentisate, producing **hypertyrosinemia** and massive urinary excretion of 4-hydroxyphenyl organic acids. Critically, because the block sits *upstream* of the maleylacetoacetate/fumarylacetoacetate steps, **no succinylacetone or other hepatotoxic intermediate is generated** — reported patients have normal liver and renal function and no eye or skin disease. This is the mechanistic feature that separates HT III from tyrosinemia type I (FAH; liver failure, hepatocellular carcinoma) and type II (TAT; oculocutaneous disease). The clinical picture is dominated by variable **neurodevelopmental** manifestations, but the causal route from tyrosine elevation to neurological injury is unresolved (PMID:16602095; PMID:11916315; PMID:10942115).

**Key identifiers:**
- MONDO:0010162 (tyrosinemia type III)
- OMIM #276710 (TYRSN3, disease); OMIM *609695 (HPD, gene)
- Orphanet ORPHA:69723
- ICD-10: **E70.2** (Disorders of tyrosine metabolism); ICD-11: **5C50.0** (Disorders of tyrosine metabolism)
- MeSH: Tyrosinemias (D020176)
- Enzyme: EC 1.13.11.27; UniProt **P32754** (human HPD)

**Synonyms / alternative names:** Hereditary tyrosinemia type III; HT III; 4-hydroxyphenylpyruvate dioxygenase deficiency; HPD deficiency; tyrosinemia due to 4-hydroxyphenylpyruvate dioxygenase deficiency; TYRSN3.

**Data provenance:** Aggregated disease-level resources (OMIM, Orphanet, HPO, MONDO) plus individual patient case reports. No EHR-cohort data exist owing to rarity.

*Sources:* [OMIM #276710](https://www.omim.org/entry/276710), [Wikipedia: Tyrosinemia type III](https://en.wikipedia.org/wiki/Tyrosinemia_type_III), [StatPearls: Hypertyrosinemia](https://www.ncbi.nlm.nih.gov/books/NBK578205/).

---

## 2. Etiology

**Primary cause (genetic).** Biallelic (homozygous or compound heterozygous) pathogenic variants in **HPD** (12q24.31) causing deficient 4-hydroxyphenylpyruvate dioxygenase activity. This is a monogenic Mendelian defect; there are no established environmental, infectious, or mechanistic non-genetic causes.

> *"Tyrosinemia type III (OMIM 276710) is an autosomal recessive disorder caused by the deficiency of 4-hydroxyphenylpyruvate dioxygenase (HPD), the second enzyme in the tyrosine catabolic pathway."* — PMID:10942115

**Genetic risk factors.** The only established risk factor is inheritance of two pathogenic HPD alleles. **Consanguinity** raises the risk of homozygosity (several reported families are consanguineous). No susceptibility loci or modifier genes have been mapped (the case count is far too small for association studies).

**Environmental risk factors.** None causal. **Dietary protein/tyrosine intake** modulates the *biochemical* burden (higher intake → higher plasma tyrosine) but does not cause the disease. Note the important differential: **transient tyrosinemia of the newborn** (the most common cause of neonatal hypertyrosinemia, ~1 in 10 newborns) is non-genetic, attributed to hepatic immaturity/prematurity and relative ascorbate (vitamin C) deficiency, and must be distinguished from HT III.

**Protective factors.** No genetic protective variants documented. **Early dietary tyrosine/phenylalanine restriction** is the candidate protective/modifying intervention, though its disease-modifying effect on neurological outcome is unproven (see §12).

**Gene–environment interaction.** The principal G×E axis is **genotype (HPD residual activity) × dietary tyrosine load** determining circulating tyrosine — but strikingly, neither genotype severity nor tyrosine level predicts neurological phenotype (PMID:10942115), so any G×E model for the *clinical* outcome remains speculative.

*Sources:* PMID:10942115, PMID:11916315; [Wadsworth NBS: Tyrosinemia type III](https://www.wadsworth.org/public-health-programs/newborn-screening/newborn-screening-program/tyrosinemia-type-iii); [MedlinePlus Genetics: Tyrosinemia](https://medlineplus.gov/genetics/condition/tyrosinemia/).

---

## 3. Phenotypes

The phenotype is bimodal by ascertainment: **screening-detected** individuals may be asymptomatic with normal development, while **clinically-ascertained** individuals present with neurological disease after the neonatal period. Because published denominators are unreliable, **frequency bands are deliberately omitted** (per curation SOP — omit rather than fabricate).

| Phenotype | Category | HPO term | Onset | Severity/course | Evidence |
|---|---|---|---|---|---|
| **Hypertyrosinemia** | Laboratory/biochemical | **HP:0003231** Hypertyrosinemia | Congenital (constant) | Persistent; diet-modifiable | PMID:11073718, PMID:9343288 |
| **Intellectual disability** | Neurological | **HP:0001249** Intellectual disability | Childhood | Mild → severe; variable | PMID:9343288, PMID:32520295 |
| **Global developmental delay** | Neurological | **HP:0001263** Global developmental delay | Infancy/childhood | Variable; presenting feature | PMID:37817461, PMID:35707594 |
| **Ataxia** (intermittent) | Neurological | **HP:0001251** Ataxia | Childhood | Episodic/intermittent | PMID:16602095 |
| **Seizure** | Neurological | **HP:0001250** Seizure | Infancy | May progress to status epilepticus | PMID:29456978 |
| **ADHD / attention deficit with hyperactivity** | Behavioral | **HP:0007018** Attention deficit hyperactivity disorder | Childhood | May precede metabolic diagnosis | PMID:32520295 |
| **Ventriculomegaly** (single report) | Neuroimaging | **HP:0002119** Ventriculomegaly | — | Novel/unreplicated finding | PMID:35707594 |

**Key characteristics.** Onset of neurological features is typically post-neonatal (infancy–childhood). Severity is **highly variable and does not correlate with plasma tyrosine level or genotype** — a defining and unusual feature of this disorder:

> *"No correlation of the severity of the mutation and enzyme deficiency and mental function has been found; neither do the recorded tyrosine levels correlate with the clinical phenotype."* — PMID:10942115

> *"Presented case may suggest that high tyrosine concentration itself does not participate directly in neuronal damage described in patients with tyrosinemia type 3."* — PMID:28649543 (asymptomatic girl, serum tyrosine 425–535 µmol/L; ref interval 29–86)

**Notable absences (discriminating negatives).** No hepatic disease, no renal tubular dysfunction, no corneal keratopathy/photophobia, no palmoplantar keratoderma — the features that define types I and II respectively:

> *"All have had normal liver and renal function and none has skin or eye abnormalities."* — PMID:11916315

**Quality-of-life impact.** Not formally measured (no EQ-5D/SF-36/PROMIS data). Burden, where present, is confined to the neurodevelopmental/educational domain; screened-and-treated individuals may have normal function.

---

## 4. Genetic / Molecular Information

**Causal gene: HPD** (HGNC:5147; NCBI Gene 3242; Ensembl ENSG00000158104), chromosome **12q24.31**, **14 exons**, encoding 4-hydroxyphenylpyruvate dioxygenase (UniProt P32754; 393 aa; functions as a homodimer in humans).

**Pathogenic variants (from the small reported allele set):**
- **First mutation survey (PMID:10942115):** 4 presumed pathogenic variants — **2 missense + 2 nonsense** — across 3 unrelated families (4 homozygotes, 1 compound heterozygote).
- **Homozygous missense p.Ala268Val (A268V)** in an HT III patient (PMID:11073718).
- **Compound heterozygous c.731C>T (p.Ala244Val / A244V) + c.656C>T (p.Thr219Met / T219M)** in a Chinese girl (PMID:37817461).
- **Homozygous splice-donor IVS11+1G>A** (intron 11) in a newborn-screened boy (PMID:23036342).
- **Novel splice-site variant** in a patient with developmental delay + ventriculomegaly (PMID:35707594).
- ClinVar records include **NM_002150.3(HPD):c.774T>G (p.Tyr258Ter)** associated with HT III.

**Variant classes represented:** missense, nonsense, and splice-site. All are **loss-of-function** in effect. Population allele frequencies (gnomAD) are consistent with individually ultra-rare alleles; no common founder allele is established. All variants are **germline**; somatic origin is not relevant.

> *"We have identified four presumed pathogenic mutations (two missense and two nonsense mutations) in the HPD gene in three unrelated families encompassing four homozygous individuals and one compound heterozygous individual with tyrosinemia type III."* — PMID:10942115

**One gene, two diseases (allelic disorders).** HPD variants cause **two distinct entities**: biallelic LOF → autosomal recessive tyrosinemia type III; the **heterozygous p.Ala33Thr (A33T)** change → autosomal dominant **hawkinsinuria** (MONDO:0007700, OMIM 140350):

> *"These findings support the hypothesis that alterations in the structure and activity of HPD are causally related to two different metabolic disorders, tyrosinemia type III and hawkinsinuria."* — PMID:11073718

**Modifier genes / epigenetics / chromosomal abnormalities.** None established (cohort too small). No epigenetic mechanism or structural/cytogenetic abnormality is implicated.

*Sources:* PMID:10942115, PMID:11073718, PMID:37817461, PMID:23036342, PMID:35707594; [OMIM *609695](https://omim.org/entry/609695); [ClinVar RCV000001640](https://www.ncbi.nlm.nih.gov/clinvar/RCV000001640/); [GTR HPD](https://www.ncbi.nlm.nih.gov/gtr/genes/3242/).

---

## 5. Environmental Information

- **Environmental / occupational toxins:** None causal. Of mechanistic interest, **HPPD-inhibitor herbicides** (triketones, e.g. sulcotrione/mesotrione; the drug **nitisinone/NTBC** is the pharmaceutical analog) chemically phenocopy the enzyme block — relevant to the pharmacology discussion in §12, not to disease etiology.
- **Lifestyle / dietary factors:** Dietary protein (tyrosine + phenylalanine) intake governs the magnitude of hypertyrosinemia and is the target of therapy; it is a modulator, not a cause.
- **Infectious agents:** Not applicable.

---

## 6. Mechanism / Pathophysiology

**Pathway context.** Tyrosine catabolism proceeds: **TAT → HPD → HGD → GSTZ1 → FAH**. The reactions are: tyrosine →(TAT)→ 4-hydroxyphenylpyruvate →(**HPD**)→ homogentisate →(HGD)→ maleylacetoacetate → fumarylacetoacetate →(FAH)→ fumarate + acetoacetate. HT III is the block at the **HPD (second) step** (KEGG map00350, tyrosine metabolism; Reactome R-HSA-8963684 tyrosine catabolism).

**Causal chain (upstream → downstream):**

1. **[Trigger, MOLECULAR] 4-Hydroxyphenylpyruvate dioxygenase deficiency.** Biallelic LOF HPD variants abolish/reduce HPD activity, blocking 4-hydroxyphenylpyruvate → homogentisate. Expression is principally hepatic, with lesser renal expression.
 - Gene: HPD (hgnc:5147). Molecular function: **GO:0003868** 4-hydroxyphenylpyruvate dioxygenase activity (DECREASED). Process: **GO:0006572** L-tyrosine catabolic process (DECREASED). Product **homogentisate (CHEBI:16169)** DECREASED. Locations: **UBERON:0002107** liver, **UBERON:0002113** kidney.
 > *"The enzyme 4-hydroxyphenylpyruvic acid dioxygenase (HPD) catalyzes the reaction of 4-hydroxyphenylpyruvic acid to homogentisic acid in the tyrosine catabolism pathway."* — PMID:11073718

2. **[Central effector, ORGANISM] Hypertyrosinemia + phenolic-metabolite accumulation.** Substrate proximal to the block accumulates: **L-tyrosine (CHEBI:17895) INCREASED**, **4-hydroxyphenylpyruvate (CHEBI:15999) INCREASED**. Because the block is upstream of maleyl-/fumaryl-acetoacetate, **succinylacetone is NOT produced → no hepatorenal toxicity** (the discriminant vs type I).
 > *"...an autosomal recessive disorder characterized by elevated levels of blood tyrosine and massive excretion of tyrosine derivatives into urine."* — PMID:11073718

3. **[Biomarker, ORGANISM] Urinary 4-hydroxyphenyl organic acids** — 4-hydroxyphenylpyruvate, 4-hydroxyphenyllactate, **4-hydroxyphenylacetate (CHEBI:18101)** INCREASED; diagnostic organic-acid signature.

4. **[Consequence, ORGANISM] Neurodevelopmental dysfunction** (intellectual disability, developmental delay, ataxia, seizures, ADHD). This edge is curated **INDIRECT / UNKNOWN INTERMEDIATES**: the mediator is unresolved because tyrosine level, residual enzyme activity, and genotype all fail to predict the phenotype (PMID:10942115, PMID:28649543).

**Enzyme biochemistry / protein dysfunction.** HPD is a **non-heme Fe(II)-dependent α-keto acid dioxygenase** (EC 1.13.11.27). It performs an unusual single-cycle reaction — **oxidative decarboxylation + side-chain 1,2-migration + aromatic hydroxylation** — converting 3-(4-hydroxyphenyl)pyruvate + O₂ → homogentisate + CO₂. The catalytic non-heme iron is coordinated by a 2-His-1-carboxylate facial triad (His/His/Glu). Pathogenic missense variants are predicted to impair catalysis/stability; nonsense and splice variants cause loss of enzyme protein (in the mouse model, exon skipping and undetectable subunit; see §15).

**Cellular processes / tissue-damage mechanism.** The proximate defect is a **hepatic/renal metabolic block**; there is no fibrosis, apoptosis cascade, or inflammatory tissue destruction (unlike type I). The neurological injury mechanism is **unknown** — candidate hypotheses (none discriminated by evidence) include: a downstream **phenolic metabolite** rather than tyrosine itself; a **human-specific critical developmental window**; and **ascertainment bias** inflating the neurological association in a disorder historically found by investigating neurological symptoms.

**Metabolomics / omics.** The disease signature is a targeted **metabolomic** one (plasma amino acids: ↑tyrosine; urine organic acids: ↑4-hydroxyphenyl-lactate/-pyruvate/-acetate, absent succinylacetone). No transcriptomic, proteomic, single-cell, or functional-genomics screen data specific to HT III exist.

**Suggested GO/CL/UBERON/CHEBI terms:** GO:0003868, GO:0006572, GO:0006559 (L-phenylalanine catabolic process, adjacent); CHEBI:17895, CHEBI:15999, CHEBI:16169, CHEBI:18101; UBERON:0002107 (liver), UBERON:0002113 (kidney), UBERON:0000955 (brain, affected downstream); cell types not well-defined (hepatocyte CL:0000182; renal proximal tubule CL:1000838).

*Sources:* PMID:11073718, PMID:10942115, PMID:16602095, PMID:28649543; [BRENDA EC 1.13.11.27](https://www.brenda-enzymes.org/enzyme.php?ecno=1.13.11.27&UniProtAcc=P32754&OrganismID=2681); [Wikipedia: 4-Hydroxyphenylpyruvate dioxygenase](https://en.wikipedia.org/wiki/4-Hydroxyphenylpyruvate_dioxygenase); [P. fluorescens HPD crystal structure](https://www.cell.com/structure/fulltext/S0969-2126(99)80124-5).

---

## 7. Anatomical Structures Affected

- **Organ level (primary, metabolic):** **Liver** (UBERON:0002107) and **kidney** (UBERON:0002113) — sites of HPD expression and of the metabolic block. Notably, these organs are biochemically affected but **not structurally damaged**.
- **Organ level (clinically affected, downstream):** **Brain / central nervous system** (UBERON:0000955; nervous system UBERON:0001016) — the site of the dominant clinical manifestations. Cranial imaging is usually normal; ventriculomegaly reported once (PMID:35707594).
- **Body systems:** Metabolic (amino-acid metabolism) primary; **nervous system** clinically dominant.
- **Tissue/cell level:** hepatocytes (CL:0000182) and renal proximal tubular epithelium (CL:1000838) carry the enzymatic defect; no specific neuronal population is implicated mechanistically.
- **Subcellular level:** HPD is **cytosolic** (GO:0005829 cytosol / GO:0005737 cytoplasm).
- **Lateralization:** Not applicable (systemic metabolic disease; neurological features bilateral/diffuse).

---

## 8. Temporal Development

- **Onset:** Biochemical abnormality is **congenital** (present from birth; detectable on newborn screening). Clinical/neurological onset is typically **post-neonatal (infancy–childhood)**; pattern insidious to subacute (seizures can be acute).
- **Progression:** No defined staging. Course is **variable** — from stable/asymptomatic (screened, early-treated) to progressive neurodevelopmental impairment or acute seizure crises. It is a **chronic, lifelong** metabolic condition.
 > *"The majority of the nine previously reported patients have presented with neurological symptoms after the neonatal period, while others detected by neonatal screening have been asymptomatic."* — PMID:11916315
- **Patterns / critical periods:** A putative **early-infancy window** where treatment may matter most is suspected but unproven:
 > *"It is not clear whether a strict low tyrosine diet alters the natural history of tyrosinaemia type III, although there remains a suspicion that treatment may be important, at least in infancy."* — PMID:11916315
 - Screened example of a benign early course: normal growth and psychomotor development at 30 months on mild protein restriction (PMID:23036342).
 - Severe example: recurrent seizures at 4 months → status epilepticus at 6 months (PMID:29456978).

---

## 9. Inheritance and Population

**Inheritance:** **Autosomal recessive** (HP:0000007). Requires biallelic pathogenic HPD variants; heterozygous carriers are unaffected.
> *"Hereditary tyrosinemia type III (HT III) is an extremely rare form of tyrosinemia, characterized by autosomal recessive inheritance and biallelic mutations in the HPD gene."* — PMID:37817461

- **Penetrance:** For the *biochemical* phenotype (hypertyrosinemia), effectively complete. For the *neurological* phenotype, **incomplete and unpredictable** (asymptomatic biallelic patients exist — PMID:28649543).
- **Expressivity:** Highly **variable** (mild ADHD/intellectual impairment → severe ID + status epilepticus), uncorrelated with genotype or tyrosine level (PMID:10942115).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / carrier frequency:** No established founder allele; carrier frequency undetermined (too rare). Consanguinity contributes in reported families.

**Epidemiology:**
- **Prevalence/incidence:** No robust population rate. Estimated **incidence < 1 in 1,000,000**; the **rarest** genetic tyrosinemia. ~**19 patients** reported worldwide as of 2022 (PMID:35707594); ~**23** by 2025 counts. Curated prevalence class: **BELOW_1_IN_1000000 (ultra-rare)**.
 > *"Tyrosinemia type III is an extremely rare autosomal recessive disease, with only 19 patients yet reported."* — PMID:35707594
- **Geographic/ethnic distribution:** No documented predisposition; cases reported across Europe, the Middle East, and East Asia. Ascertainment depends on whether a region's newborn-screening panel measures tyrosine.
- **Sex ratio:** No established skew (cases in both sexes).
- **Age distribution:** Neonatal (screened) or infancy–childhood (symptomatic).

*Sources:* PMID:35707594, PMID:32520295, PMID:11916315, PMID:37817461, PMID:23036342; [Wadsworth NBS](https://www.wadsworth.org/public-health-programs/newborn-screening/newborn-screening-program/tyrosinemia-type-iii).

---

## 10. Diagnostics

**Biochemical (first-line):**
- **Plasma amino acids** — elevated **tyrosine** (screening + monitoring analyte). LOINC candidates: Tyrosine [Moles/volume] in plasma.
- **Urine organic acids** — elevated **4-hydroxyphenyl** derivatives (4-OH-phenyllactate, -pyruvate, -acetate); **succinylacetone ABSENT** (excludes type I — the key discriminator).
 > *"These disorders are diagnosed by observing elevated tyrosine by plasma amino acid chromatography and characteristic tyrosine metabolites by urine organic acid analysis."* — PMID:16602095
 > *"Urine organic acids show elevated p-hydroxy-phenyl organic acids in each type of tyrosinemia, and the pathognomic succinylacetone in tyrosinemia Type I."* — PMID:16602095

**Newborn screening:** Detection of elevated tyrosine by **tandem mass spectrometry (MS/MS)** on dried blood spot. Note that MS/MS tyrosine is a poor primary marker for type I (succinylacetone is preferred there), but it does flag HT III/II and transient tyrosinemia. Confirmation requires repeat quantitation + urine organic acids + genetics (PMID:23036342).

**Genetic testing:** **HPD single-gene / targeted NGS** sequencing to identify biallelic pathogenic variants confirms diagnosis; HPD is offered on inborn-errors and tyrosinemia gene panels (also covers hawkinsinuria).
> *"A 3-year-old girl, identified through newborn screening, was diagnosed with HT III using targeted next-generation sequencing."* — PMID:37817461

**Enzyme assay:** Direct hepatic HPD activity assay is possible but rarely needed given molecular testing.

**Imaging / electrophysiology:** Cranial MRI usually normal (ventriculomegaly reported once, PMID:35707594); EEG as indicated for seizures. Neither is diagnostic of HT III per se.

**NCIT diagnostic terms:** Laboratory Procedure (NCIT:C25294); Genetic Testing (NCIT:C15709).

**Differential diagnosis:** Transient tyrosinemia of the newborn (most common; resolves, non-genetic); tyrosinemia type I (FAH — succinylacetone+, liver/renal disease); tyrosinemia type II (TAT — oculocutaneous, no organic aciduria of this pattern); hawkinsinuria (HPD, dominant); liver disease causing secondary hypertyrosinemia; scurvy/ascorbate deficiency.

*Sources:* PMID:16602095, PMID:23036342, PMID:37817461; [Oklahoma tyrosine screening fact sheet](https://oklahoma.gov/content/dam/ok/en/health/health2/documents/tyrosine-provider-fact-sheet.pdf).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Not life-limiting** through the metabolic lesion itself — no hepatic, renal, or oncologic risk (contrast type I). No disease-specific mortality data; life expectancy presumed normal.
- **Morbidity/disability:** Confined to the **neurodevelopmental/behavioral** domain. Long-term disability ranges from none (screened, treated) to significant intellectual disability with neurological abnormality (PMID:9343288).
- **Complications:** Seizures/status epilepticus (PMID:29456978); learning/behavioral difficulties.
- **Recovery potential:** Some patients report subjective gains after diet + falling tyrosine (PMID:35707594), but disease-modifying benefit is unproven.
- **Prognostic factors:** None validated. Age at dietary initiation is the leading candidate modifier (within-family sib comparison favored earlier treatment — PMID:32520295), but plasma tyrosine and genotype are **not** prognostic (PMID:10942115).

> *"All have had normal liver and renal function and none has skin or eye abnormalities."* — PMID:11916315 (bounds the burden to the neurological domain)

---

## 12. Treatment

**1. Dietary phenylalanine + tyrosine restriction (mainstay).** Low-protein diet with a **tyrosine-/phenylalanine-free amino-acid substitute** ("anamix"-type formula). Reliably lowers plasma tyrosine; disease-modifying effect on neurology unresolved.
- Modality: BEHAVIORAL/dietary. NCIT: **Dietary Intervention (NCIT:C15447)**.
- Target mechanism: reduces substrate delivery to the blocked step (INHIBITS "Hypertyrosinemia and phenolic metabolite accumulation").
 > *"She was treated with a diet low in tyrosine and phenylalanine and anamix formula that leading to catch-up growth and improvement of her symptoms. Plasma tyrosine level dropped to normal values."* — PMID:29456978
 > *"Therapy consists of a diet low in phenylalanine and tyrosine for each of the tyrosinemias and 2-(2-nitro-4-trifluoromethylbenzoyl)-1,3-cyclohexanedione (NTBC) for tyrosinemia Type I."* — PMID:16602095
 > *"...a better neurological and behavioral evaluation in the patient who started treatment earlier."* — PMID:32520295 (single sib pair; suggestive only)

**2. Developmental/neurological supportive care.** Antiseizure therapy, developmental/educational support, neurodevelopmental follow-up per phenotype. NCIT: **Supportive Care (NCIT:C15747)** (PMID:35707594).

**Nitisinone (NTBC) — contraindicated in concept, not therapeutic here.** Nitisinone is a **pharmacological HPD inhibitor**; it *reproduces* the HT III lesion rather than correcting it, and is confined to type I (and trialed in alkaptonuria). This is a key teaching point: the drug that treats type I would recreate the exact enzymatic block of type III.

**Pharmacogenomics / advanced therapeutics / surgery / experimental trials:** None applicable/reported. No gene, cell, RNA, or targeted therapy; no HT III–specific clinical trials (rarity).

**Treatment outcomes:** Biochemical response (falling tyrosine) is reliable; clinical/neurological response is variable and unproven as disease-modifying.

*Sources:* PMID:16602095, PMID:29456978, PMID:32520295, PMID:11916315, PMID:35707594, PMID:39290064 (NTBC-induced tyrosinemia toxicity in alkaptonuria).

---

## 13. Prevention

- **Primary prevention:** None (Mendelian). **Genetic/reproductive counseling** for at-risk families; carrier testing, prenatal diagnosis, and **PGT-M** are technically feasible where the familial variants are known. Consanguinity counseling relevant.
- **Secondary prevention (early detection):** **Newborn screening** for elevated tyrosine (MS/MS) enables presymptomatic diagnosis and early dietary intervention — the practical prevention lever, though its effect on neurological outcome is unproven.
- **Tertiary prevention:** Dietary control of tyrosine + neurodevelopmental monitoring to mitigate complications.
- **Immunization / public-health / environmental interventions:** Not applicable.

*Sources:* PMID:23036342; [Wadsworth NBS](https://www.wadsworth.org/public-health-programs/newborn-screening/newborn-screening-program/tyrosinemia-type-iii).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Best-characterized non-human counterpart is **mouse (*Mus musculus*, NCBITaxon:10090)** — spontaneous "mouse strain III" with hereditary hypertyrosinemia.
- **Ortholog:** Mouse **Hpd** (NCBI Gene 15445); human **HPD** (NCBI Gene 3242). HPD is deeply conserved across mammals, plants, and bacteria (the enzyme is the target of HPPD-inhibitor herbicides).
- **Natural disease / comparative biology:** The mouse strain reproduces the human **biochemical** phenotype faithfully — absent hepatic HPD activity/protein, persistent hypertyrosinemia, urinary 4-hydroxyphenyl derivatives, **no succinylacetone** — while being "apparently healthy" (no overt neurological/hepatorenal disease). This species divergence (biochemical fidelity without the human neurodevelopmental phenotype) is itself informative for the neurotoxicity question. No prominent naturally occurring companion-animal/wildlife HT III is catalogued in OMIA.
- **Transmission / zoonosis:** Not applicable.

> *"These features are similar to type III tyrosinemia in humans."* — PMID:2014797

---

## 15. Model Organisms

**Mouse strain III (spontaneous Hpd-null mouse)** — the principal and essentially only established model.

- **Type:** mammalian, spontaneous (pre-targeted-mutagenesis) inbred strain; autosomal recessive.
- **Genotype/lesion:** **Hpd exon-7 nonsense substitution**, homozygous, additionally causing **skipping of the constitutive exon 7** in most transcripts → undetectable HPD subunit and virtually absent hepatic activity, with flanking enzymes (fumarylacetoacetase, both TAT isoforms) intact.
 > *"...4-hydroxyphenylpyruvic acid dioxygenase activity was virtually absent, while fumarylacetoacetase and tyrosine aminotransferases (cytosolic and mitochondrial forms) were normal..."* — PMID:2014797
 > *"We report a nucleotide substitution that generates a termination codon in exon 7 of the 4-hydroxyphenylpyruvic acid dioxygenase gene in III mice. This mutation is associated with partial exon skipping..."* — PMID:7774914
- **Phenotype recapitulation:**
 - **HIGH fidelity** for the enzyme block (RECAPITULATES): hepatic HPD activity and protein both null, pathway-specific.
 - **HIGH fidelity** for the biochemical phenotype (RECAPITULATES): persistent hypertyrosinemia + ↑urinary 4-hydroxyphenylpyruvate derivatives + **succinylacetone absent** (the discriminating negative reproduced).
 - **FAILS TO RECAPITULATE** the neurodevelopmental consequence: animals "apparently healthy," no hepatorenal dysfunction. **Caveat:** this is a *negative on gross observation only* — no standardized neurobehavioral/neurocognitive testing, neuropathology, or tyrosine-exposure calibration against the human range was performed. It therefore **cannot** be cited as evidence that hypertyrosinemia is neurologically harmless.
 > *"All the animals were apparently healthy, and there was no evidence of hepatorenal dysfunction."* — PMID:2014797
- **Model limitations:** Murine allele (exon-7 nonsense/skipping), not a human patient allele — models complete LOF, not the hypomorphic missense genotypes common in patients; enzyme measured in liver only (renal HPD not assessed); metabolite panel qualitative, absolute tyrosine not human-calibrated.
- **Applications:** Studying the metabolic block and biochemistry of tyrosine catabolism; complements type I mouse models; **available for (not-yet-done) neurobehavioral phenotyping** to test the tyrosine-neurotoxicity hypothesis.
- **Other systems:** No non-animal experimental model (organoid/iPSC), no computational model, and no public omics dataset with a mechanism link specific to HT III were identified.

*Sources:* PMID:2014797, PMID:7774914.

---

## Cross-cutting open questions (knowledge gaps)

1. **Tyrosine neurotoxicity is unexplained.** Neither HPD-lesion severity, residual enzyme activity, nor plasma tyrosine predicts the neurological phenotype, and biochemically affected patients with normal development exist. Candidate mediators (a downstream phenolic metabolite; a human-specific early developmental window; ascertainment bias) are undiscriminated. *Proposed:* prospective standardized neurocognitive follow-up of screened cohorts stratified by time-integrated tyrosine exposure (PMID:10942115, PMID:28649543).
2. **Genetic vs pharmacological HPD block discrepancy.** Nitisinone-induced (acquired) HPD blockade in type-I/alkaptonuria patients causes tyrosine corneal keratopathy and skin lesions; genetic HT III patients do **not** develop oculocutaneous disease. Possible explanations (higher absolute tyrosine under pharmacological block, residual activity in hypomorphs, tissue-distribution differences, older/longer-exposed nitisinone-treated adults) are unresolved and bear on whether HT III patients need ocular surveillance (PMID:11916315, PMID:39290064).
3. **Mouse-model silence.** The high-biochemical-fidelity Hpd-null mouse shows no overt neuro phenotype — but only gross observation was ever done; this is a HUMAN_MODEL_MISMATCH, not evidence of safety (PMID:2014797 vs PMID:35707594).

---

## Consolidated Evidence Citations (PMIDs)

| PMID | Role in report |
|---|---|
| **10942115** | HPD mutations in HT III; no genotype/tyrosine–phenotype correlation |
| **11073718** | HPD underlies both HT III and hawkinsinuria; A268V; A33T |
| **11916315** | Outcome review; no liver/renal/skin/eye disease; diet-uncertain |
| **9343288** | Diagnosis + 10-yr follow-up; severe ID case; biochemical phenotype |
| **16602095** | "The genetic tyrosinemias" review; diagnosis, therapy, succinylacetone discriminator |
| **23036342** | NBS-detected boy; IVS11+1G>A; benign early course |
| **35707594** | Novel splice-site variant + ventriculomegaly; 19-patient summary |
| **28649543** | Asymptomatic girl (tyrosine 425–535 µmol/L); argues against direct neurotoxicity |
| **37817461** | Compound het p.A244V/p.T219M; genotype–phenotype review; NGS diagnosis |
| **32520295** | Sibling case report/review; ADHD; earlier-treatment advantage |
| **29456978** | Status epilepticus + ID; diet lowers tyrosine |
| **39290064** | NTBC-induced tyrosinemia toxicity (alkaptonuria) — pharmacological phenocopy |
| **2014797** | Mouse strain III characterization (biochemistry, healthy animals) |
| **7774914** | Mouse Hpd exon-7 nonsense/exon-skipping allele |

**Web/database sources:** [OMIM #276710](https://www.omim.org/entry/276710) · [OMIM *609695 (HPD)](https://omim.org/entry/609695) · [MedlinePlus: Tyrosinemia](https://medlineplus.gov/genetics/condition/tyrosinemia/) · [Wikipedia: Tyrosinemia type III](https://en.wikipedia.org/wiki/Tyrosinemia_type_III) · [StatPearls: Hypertyrosinemia](https://www.ncbi.nlm.nih.gov/books/NBK578205/) · [Wadsworth NBS: Tyrosinemia type III](https://www.wadsworth.org/public-health-programs/newborn-screening/newborn-screening-program/tyrosinemia-type-iii) · [ClinVar RCV000001640](https://www.ncbi.nlm.nih.gov/clinvar/RCV000001640/) · [GTR: HPD gene 3242](https://www.ncbi.nlm.nih.gov/gtr/genes/3242/) · [BRENDA EC 1.13.11.27 (human)](https://www.brenda-enzymes.org/enzyme.php?ecno=1.13.11.27&UniProtAcc=P32754&OrganismID=2681) · [Wikipedia: 4-Hydroxyphenylpyruvate dioxygenase](https://en.wikipedia.org/wiki/4-Hydroxyphenylpyruvate_dioxygenase).

---

**Note for KB curation:** This report corresponds closely to the already-curated `kb/disorders/Tyrosinemia_Type_III.yaml` entry on this branch, which independently verifies each snippet against cached abstracts. The report adds contextualizing detail not carried in the YAML (gene locus 12q24.31 / 14 exons, UniProt P32754, EC/enzyme mechanism, ICD/OMIM-gene identifiers, transient-tyrosinemia differential, mouse Hpd Gene ID) that could enrich the entry; note that any such additions to the YAML would require their own verified PMID snippets (the enzyme-mechanism and locus facts above are sourced to BRENDA/OMIM/Wikipedia, not to the cached PMIDs, and should not be added as PMID-attributed evidence without fetching a citable primary source).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.