---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T17:15:51.864524'
end_time: '2026-08-19T17:20:08.788487'
duration_seconds: 256.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vitamin D-Dependent Rickets Type 2A
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
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 14
  total_cost_usd: 1.7344912999999997
  session_id: 75ec52a1-0e70-502f-850e-ec2680b017b0
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 48
reference_validation:
  total_references: 28
  verified: 27
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.036
  relevance_assessed: 27
  on_topic: 24
  unresolved_references:
  - DOI:10.1159/000546444/927170/Persistent-Hyperparathyroidism-in-Vitamin-D
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vitamin D-Dependent Rickets Type 2A
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Vitamin D-Dependent Rickets Type 2A** covering all of the
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

I'll research Vitamin D-Dependent Rickets Type 2A using web search to gather current, well-cited information.

I now have comprehensive, well-sourced data. Compiling the full research report.

# Vitamin D-Dependent Rickets Type 2A (VDDR2A) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Vitamin D-dependent rickets type 2A (VDDR2A), also widely known as **hereditary 1,25-dihydroxyvitamin D-resistant rickets (HVDRR)** or hereditary vitamin D-resistant rickets, is a rare autosomal recessive Mendelian disorder caused by biallelic loss-of-function mutations in the **vitamin D receptor gene (VDR)**, producing end-organ resistance to the active vitamin D hormone, 1,25-dihydroxyvitamin D₃ (calcitriol), rather than a defect in vitamin D synthesis itself. Unlike nutritional rickets or VDDR type 1 (a biosynthetic enzyme defect), VDDR2A patients have normal or elevated circulating 1,25(OH)₂D levels but the target tissues cannot respond to it ([OMIM #277440](https://www.omim.org/entry/277440); [NORD](https://rarediseases.org/mondo-disease/vitamin-d-dependent-rickets-type-2a/)).

**Key identifiers:**
- **OMIM:** #277440 (VDDR2A); causal gene VDR, OMIM *601769 ([OMIM 277440](https://www.omim.org/entry/277440); [OMIM 601769](https://omim.org/entry/601769))
- **Gene:** VDR, chromosome **12q13.11**
- **GTR/MedGen concept:** "Vitamin D-dependent rickets, type II" and "…type II with alopecia" are indexed as related concepts ([NIH GTR C3536983](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3536983/); [NIH GTR C0342646](https://www.ncbi.nlm.nih.gov/gtr/conditions/C0342646/))
- **Orphanet:** grouped under "Hypocalcemic vitamin D-dependent rickets" ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=289157&lng=EN))
- Suggested **MONDO** term: hereditary vitamin D-resistant rickets (VDDR2A subtype) — confirm exact MONDO CURIE against the local MONDO adapter before curation.

**Synonyms/alternative names:** Hereditary 1,25-dihydroxyvitamin D-resistant rickets (HVDRR); vitamin D receptor deficiency rickets; hereditary hypocalcemic vitamin D-resistant rickets; pseudo-vitamin D deficiency rickets type II; hereditary vitamin D-resistant rickets with alopecia (when alopecia present).

**Evidence base:** Almost all published knowledge derives from **individual patient case reports and small case series** (often single kindreds), supplemented by two published retrospective single-center cohorts (a Saudi Arabian series and Chinese/Egyptian family series), rather than large aggregated disease-level registries — reflecting the disorder's extreme rarity. Suggested-evidence sources: HUMAN_CLINICAL (predominant), supplemented by MODEL_ORGANISM (VDR-null mouse/rat) and IN_VITRO (transfection/reporter assays of mutant VDR function).

---

## 2. Etiology

**Disease causal factor:** VDDR2A is caused by **biallelic (typically homozygous or compound heterozygous) loss-of-function mutations in VDR** on chromosome 12q13.11, encoding the nuclear vitamin D receptor. This is a purely **genetic/Mendelian** etiology — no environmental or infectious trigger is causal, though vitamin D intake/sunlight exposure modulates severity of the biochemical phenotype.

**Genetic risk factors:**
- **Consanguinity** is a major risk factor given the autosomal recessive inheritance and the disease's concentration in consanguineous kindreds (Chinese, Egyptian, Middle Eastern, and Saudi Arabian case series predominate in the literature) ([PMC4589239](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589239/); [PubMed 24859502](https://pubmed.ncbi.nlm.nih.gov/24859502/)).
- **Uniparental disomy of chromosome 12** has been documented as a distinct mechanism producing apparent homozygosity for a VDR mutation without both parents being carriers — confirmed by SNP array in at least one reported case ([PLOS ONE / PMC4496068](https://pmc.ncbi.nlm.nih.gov/articles/PMC4496068/)).
- A **dominant-negative mechanism** has also been reported: a single mutant VDR allele with a constitutive corepressor (NCoR) interaction and ligand-independent VDRE binding causes dominantly inherited HVDRR, analogous to dominant-negative thyroid hormone receptor mutations ([ScienceDirect / PMC5365159](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5365159/); [PubMed 28377956](https://pubmed.ncbi.nlm.nih.gov/28377956/)). A 2025 case report also described an atypical **heterozygous** VDDR2A presentation (c.146+9dup) presenting with pseudoarthrosis rather than the classic recessive picture ([Goldberg et al. 2025, Case Reports in Endocrinology](https://onlinelibrary.wiley.com/doi/10.1155/crie/2434759); [PMC12003035](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003035/)).

**Environmental risk factors:** None are causal, but low ambient sunlight/dietary vitamin D deficiency can exacerbate the biochemical/clinical phenotype in an already receptor-resistant patient by lowering the (already ineffective) precursor pool further, and can complicate diagnosis by mimicking nutritional rickets.

**Protective factors:** No specific protective genetic variant is described. Adequate dietary calcium intake mitigates (but does not cure) the phenotype, since the downstream defect is receptor unresponsiveness rather than calcium/vitamin D substrate availability — this underlies the calcium-based (rather than vitamin D-based) treatment strategy (see §12).

**Gene-environment interaction:** The core interaction is that the severity of clinical rickets/hypocalcemia is buffered by dietary calcium intake independent of VDR/calcitriol signaling — i.e., sufficiently high oral or IV calcium can partially bypass the VDR defect by driving passive, non-VDR-mediated paracellular intestinal calcium absorption.

---

## 3. Phenotypes

VDDR2A phenotypes fall into rickets/mineral-metabolism findings (present in essentially all patients) and alopecia (present in a majority but not universal, and correlating with mutation severity).

| Phenotype | Type | Suggested HPO term |
|---|---|---|
| Rickets / rachitic bone changes | Sign | HP:0002748 (Rickets) |
| Growth retardation / short stature | Sign | HP:0004322 (Short stature) |
| Muscle weakness / hypotonia | Sign | HP:0001324 / HP:0001252 |
| Bone pain | Symptom | HP:0002653 (Bone pain) |
| Bowing of long bones (genu varum) | Sign | HP:0002979 (Genu varum) |
| Widened wrists/costochondral beading (rachitic rosary) | Sign | HP:0000939 (Osteoporosis)-adjacent / HP:0004464 (Enlarged costochondral junctions) |
| Dental abnormalities / enamel hypoplasia | Sign | HP:0000704 (Dental caries)/HP:0006297 |
| Hypocalcemia | Lab abnormality | HP:0002901 (Hypocalcemia) |
| Hypophosphatemia | Lab abnormality | HP:0002148 (Hypophosphatemia) |
| Secondary hyperparathyroidism | Lab/sign | HP:0000870 (Hyperparathyroidism) |
| Elevated serum alkaline phosphatase | Lab abnormality | HP:0003155 (Elevated alkaline phosphatase) |
| Elevated 1,25-dihydroxyvitamin D (distinguishing lab feature) | Lab abnormality | (no dedicated HPO term commonly used; describe via biochemical marker) |
| Alopecia totalis/partialis | Sign | HP:0007550/ HP:0002293 (Alopecia) |
| Hypocalcemic seizures / tetany | Symptom | HP:0032792 / HP:0001336 |
| Milia/epidermal (cutaneous) cysts | Sign | HP:0001059 |

**Onset and course:** Manifestations typically present in **infancy to early childhood** (rickets is usually evident by the first 1–2 years of life; alopecia, when present, is often noted from birth or shortly thereafter). Severity is variable — even within families with the same genotype — and disease course is generally described as an **early, severe, and treatment-resistant** rachitic picture that improves with high-dose calcium repletion (see §12) but with alopecia typically **not** reversing.

**Alopecia frequency and severity correlation:** Reported figures vary by cohort, from roughly half to the majority of patients: "most patients have total alopecia in addition to rickets" ([OMIM 277440](https://www.omim.org/entry/277440)) and "approximately 80% of patients with HVDRR have early-onset alopecia... the degree of alopecia is associated with the severity of the vitamin D resistance," with an unusual patchy pattern of total baldness adjacent to normal or scant hair ([PMC3196847](https://pmc.ncbi.nlm.nih.gov/articles/PMC3196847/)). Alopecia is a poor prognostic marker for treatment response (see §12).

**Atypical presentations:** VDDR2A can present with **hypophosphatemia in the absence of hypocalcemia**, causing initial misclassification as an FGF23-mediated hypophosphatemic rickets ([JCEM Case Reports, PMC/Oxford](https://academic.oup.com/jcemcr/article/4/8/luag189/8732980); [Karger/PMC12187100](https://pmc.ncbi.nlm.nih.gov/articles/PMC12187100/)) — an important differential-diagnosis pitfall (§10).

**Quality of life impact:** Untreated or delayed-diagnosis disease causes significant motor disability (inability to bear weight/walk due to bone pain and deformity) that reverses substantially with calcium therapy (documented improvement from non-ambulatory to independent walking within weeks of IV calcium in case reports); alopecia carries a persistent psychosocial/cosmetic burden since it is typically treatment-refractory.

---

## 4. Genetic/Molecular Information

**Causal gene:** **VDR** (Vitamin D Receptor), OMIM *601769, chromosome 12q13.11 ([GeneCards](https://www.genecards.org/card/VDR); [OMIM 601769](https://omim.org/entry/601769)).

**Variant spectrum:** VDDR2A is caused by **heterogeneous loss-of-function mutations** distributed across the DNA-binding domain (DBD) and ligand-binding domain (LBD) of VDR, including:
- **Missense mutations** disrupting ligand binding or DNA binding — e.g., **I268T** (LBD, ~5–10-fold reduced 1,25(OH)₂D₃ affinity, ~65-fold higher concentration required for equipotent transactivation) ([PubMed 15308610](https://pubmed.ncbi.nlm.nih.gov/15308610/)); **V26M** (DBD, impairs DNA binding) ([PMC2794978](https://pmc.ncbi.nlm.nih.gov/articles/PMC2794978/)); **R343H** and **R343C** (recently reported, associated with alopecia and with a hypophosphatemia-predominant presentation respectively) ([PMC5681508](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5681508/); [JCEM Case Reports 2024](https://academic.oup.com/jcemcr/article/4/8/luag189/8732980)).
- **Splice-site mutations** — e.g., a novel splice-site mutation successfully managed with oral calcium therapy ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S8756328209016238)); a 2025 case with a heterozygous c.146+9dup splice-region variant with an atypical pseudoarthrosis presentation ([PMC12003035](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003035/)).
- **Compound heterozygous** genotypes are well documented, including in a 2008 report of compound heterozygous VDR mutations with alopecia ([PubMed 19049339](https://pubmed.ncbi.nlm.nih.gov/19049339/)) and a 2025 congress report of a novel compound-heterozygous VDR mutation ([Endocrine Abstracts 2025](https://www.endocrine-abstracts.org/ea/0110/ea0110ep247)).
- **Uniparental disomy of chromosome 12**, producing homozygosity for a maternal-only VDR mutation despite the father not being a carrier ([PMC4496068](https://pmc.ncbi.nlm.nih.gov/articles/PMC4496068/)).
- Rare **dominant-negative heterozygous mutations** producing HVDRR via constitutive corepressor (NCoR) recruitment ([PMC5365159](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5365159/)).

**Variant classification/functional consequence:** The great majority are classified functionally as **loss-of-function** (complete or partial) via in-vitro transactivation/reporter assays; a minority display **dominant-negative** behavior. Standard ACMG/AMP pathogenicity classification should be applied per-variant via ClinVar; no single recurrent "hot-spot" variant dominates worldwide — mutations are largely private/family-specific, consistent with a rare, ethnically dispersed autosomal recessive disorder.

**Allele frequency:** Given the rarity and largely private nature of pathogenic VDR loss-of-function alleles, population database (gnomAD) frequencies for individual pathogenic variants are expected to be near-absent/singleton; no common founder allele with an appreciable population allele frequency has been established in the literature surveyed.

**Somatic vs. germline:** VDDR2A is exclusively a **germline** Mendelian disorder (not somatic/acquired).

**Modifier genes:** None firmly established; phenotypic variability (notably in alopecia severity) is attributed to the specific functional consequence of the causal VDR allele (LBD vs. DBD, partial vs. complete loss of function, dominant-negative vs. simple loss-of-function) rather than a distinct modifier locus.

**Suggested GO terms for the VDR molecular function/pathway:** GO:0004879 (nuclear receptor activity), GO:0070644 (vitamin D response element binding), GO:0008202 (steroid metabolic process), GO:0060348 (bone development).

---

## 5. Environmental Information

Because VDDR2A is a fully penetrant genetic receptor defect, environmental factors do not cause the disease but strongly **modulate symptom severity and diagnostic presentation**:
- **Dietary vitamin D/calcium intake and sunlight exposure** affect substrate availability but cannot correct receptor unresponsiveness; low dietary calcium can precipitate more severe hypocalcemic crises (seizures/tetany) in an affected infant.
- No infectious agent is implicated in VDDR2A pathogenesis.
- No specific toxin/occupational exposure is implicated (this is a congenital, not acquired, receptor defect).

---

## 6. Mechanism / Pathophysiology

**Molecular pathway.** VDR is a member of the nuclear hormone receptor superfamily. Upon binding its ligand, 1,25-dihydroxyvitamin D₃ (calcitriol), the liganded VDR **heterodimerizes with the retinoid X receptor (RXR)**. Helix 12 (H12) of the VDR ligand-binding domain acts as a flexible "lid" whose ligand-induced repositioning creates the activation function-2 (AF-2) hydrophobic cleft required for coactivator recruitment; RXR undergoes an allosteric "phantom ligand effect" shift toward an active conformation even without its own ligand ([Oxford Mol Endocrinol](https://academic.oup.com/mend/article/17/11/2320/2747379); [PMC3087838](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3087838/)). The VDR-RXR heterodimer binds **vitamin D response elements (VDREs)** — direct repeats of the RGKTSA hexameric half-site separated by 3 nucleotides (DR3 motif) — in enhancer regions of target genes, recruiting a multiprotein complex (pioneer factors, chromatin remodelers, coactivators, Mediator complex) that docks onto RNA polymerase II to drive transcription of vitamin D target genes (e.g., intestinal calcium transporters, renal calcium-handling genes, osteoblast genes) (search synthesis of [ScienceDirect VDRE overview](https://www.sciencedirect.com/topics/veterinary-science-and-veterinary-medicine/vdre), [PMC6332450](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6332450/)).

**Causal chain — genetic lesion to clinical phenotype:**
1. **Biallelic (or dominant-negative) VDR mutation** → loss of ligand binding (LBD mutations, e.g. I268T) or loss of DNA binding (DBD mutations, e.g. V26M) → **impaired or absent VDR-RXR-VDRE transcriptional activation** of calcitriol target genes.
2. **End-organ (intestinal, renal, skeletal) resistance to 1,25(OH)₂D₃** → **decreased active intestinal calcium (and secondarily phosphate) absorption** despite normal or compensatorily elevated circulating calcitriol.
3. **Hypocalcemia** → **secondary/compensatory hyperparathyroidism** (elevated PTH) → renal phosphate wasting exacerbating **hypophosphatemia**; PTH-driven bone resorption contributes to elevated **alkaline phosphatase**.
4. Combined hypocalcemia/hypophosphatemia → **defective mineralization of osteoid at growth plates and bone matrix** → **rickets/osteomalacia**, growth retardation, bone pain/deformity, muscle weakness (mineral-dependent neuromuscular function).
5. **Independently (not calcium-pathway mediated): VDR loss in hair-follicle keratinocytes** disrupts a **ligand-independent** VDR function required for postmorphogenic anagen (growth phase) initiation of the hair cycle, causing **alopecia** — this occurs even though the alopecia-causing VDR function does not require 1,25(OH)₂D binding, explaining why alopecic patients are especially treatment-refractory to vitamin D/calcitriol-based therapy while their rickets can still be treated via calcium (see below and §12) ([JCI 11676](https://www.jci.org/articles/view/11676); [Oxford Mol Endocrinol 19(4):855](https://academic.oup.com/mend/article/19/4/855/2741289); [PMC11720424](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11720424/)).

**Cellular processes involved:** Intestinal enterocyte calcium transport (TRPV6/calbindin-mediated active transport, normally VDR-induced); osteoblast/osteoclast coupling and PTH-driven bone remodeling; parathyroid chief cell PTH secretion (normally suppressed by calcitriol-VDR signaling — loss of this suppression contributes to the hyperparathyroidism); hair-follicle keratinocyte stem-cell-driven anagen re-entry (VDR-dependent, ligand-independent, involving cooperative β-catenin/Lef1 canonical Wnt signaling that is abolished in VDR-null keratinocytes) ([PNAS 0702884104](https://www.pnas.org/doi/10.1073/pnas.0702884104)).

**Biochemical abnormalities:** Hypocalcemia, hypophosphatemia (variable — can be absent in some presentations), elevated alkaline phosphatase, elevated PTH, and the biochemically **distinguishing feature of markedly elevated (not low) circulating 1,25(OH)₂D**, which differentiates VDDR2A from VDDR1A (CYP27B1 biosynthetic defect, where 1,25(OH)₂D is low).

**Suggested GO/biological process terms:** GO:0070508 (cholesterol import)-adjacent calcium pathway terms are less relevant; more directly: GO:0006816 (calcium ion transport), GO:0070508 n/a, GO:0060349 (bone morphogenesis), GO:0042633 (hair cycle), GO:0022416 (chaeta development)-adjacent is not applicable to humans — use GO:0042633 (hair cycle) and GO:0030855 (epithelial cell differentiation) for the alopecia arm.

**Suggested CL (cell type) terms:** CL:0000584 (enterocyte), CL:0000062 (osteoblast), CL:0000092 (osteoclast), CL:0000446 (parathyroid chief cell), CL:0000312 (keratinocyte), CL:0002337 (hair follicle stem cell / bulge keratinocyte).

**Model system / omics data:** The literature surveyed is predominantly clinical case reports and targeted functional (reporter-gene transactivation) assays of specific VDR mutants; no large-scale transcriptomic/proteomic/single-cell dataset specific to human VDDR2A patient tissue was identified in this search. Model-organism transcriptomic characterization exists for VDR-null mice (see §15).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skeletal system (long bones, growth plates, ribs — costochondral junctions), skin/hair follicles.
- **Secondary:** Parathyroid glands (secondary hyperparathyroidism), kidney (secondary renal phosphate wasting via PTH), skeletal muscle (hypotonia/weakness), teeth (enamel defects).
- **Body systems:** Musculoskeletal, endocrine, integumentary; less so cardiovascular/neurological (hypocalcemic seizures reflect a neuromuscular/CNS excitability consequence of the mineral disturbance rather than primary CNS pathology).

**Tissue/cell level:** Growth-plate chondrocytes and osteoid-forming osteoblasts (impaired mineralization); intestinal enterocytes (impaired active transcellular calcium absorption); renal tubular epithelium (secondary phosphate handling); hair follicle keratinocytes, specifically the **bulge stem cell niche**, which forms normally in VDR-null models but fails to regenerate the lower hair follicle without VDR ([PNAS 0702884104](https://www.pnas.org/doi/10.1073/pnas.0702884104)).

**Subcellular level:** VDR is a **nuclear receptor**; the defect is localized to nuclear transcriptional machinery (GO Cellular Component: GO:0005634 nucleus; GO:0090575 RNA polymerase II transcription regulator complex) rather than membrane, mitochondrial, or lysosomal compartments.

**Localization/laterality:** Systemic/bilateral, symmetric — skeletal changes affect long bones bilaterally (e.g., bilateral genu varum), and alopecia, when present, is typically diffuse/total rather than a focal or lateralized process.

Suggested **UBERON** terms: UBERON:0002481 (bone tissue), UBERON:0002049 (vasculature)-not primary, UBERON:0000014 (zone of skin), UBERON:0002073 (hair follicle), UBERON:0001103 (diaphragm)-n/a; more precisely UBERON:0002365 (exocrine gland)-n/a — best fits: UBERON:0001474 (bone element), UBERON:0002073 (hair follicle), UBERON:0001737 (parathyroid gland), UBERON:0002113 (kidney), UBERON:0001911 (mammary gland)-n/a.

---

## 8. Temporal Development

**Onset:** Congenital genetic lesion with **clinical onset in infancy to early childhood** — most reported cases present with rachitic signs (bowing, growth failure) and/or alopecia within the first 1–2 years of life; alopecia, when it occurs, is frequently apparent from birth or the first months.

**Onset pattern:** Insidious/progressive for the skeletal phenotype (worsening over months if undiagnosed), occasionally punctuated by **acute hypocalcemic events** (seizures/tetany) that can be the presenting acute event prompting diagnosis.

**Progression:** Without treatment, rachitic bone disease progresses with worsening deformity, growth retardation, and motor disability. With calcium-based treatment (see §12), the skeletal phenotype is generally **reversible/healable** — radiographic and biochemical normalization documented over roughly **8 weeks to 6 months** depending on severity/delay to diagnosis ([Frontiers, Saudi Arabia cohort](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1365714/full); case reports above). Alopecia, in contrast, is typically **stable/persistent** and largely treatment-refractory even when the skeletal disease resolves.

**Disease course pattern:** Chronic but medically manageable — not classically relapsing-remitting, though inadequate treatment adherence can allow biochemical relapse. A 2025 Hormone Research in Paediatrics report specifically notes that **persistent hyperparathyroidism** can remain despite normalization of hypophosphatemia and radiographic healing of rickets, indicating dissociation between different biochemical/clinical axes during treatment response ([Karger 2025](https://karger.com/hrp/article/doi/10.1159/000546444/927170/Persistent-Hyperparathyroidism-in-Vitamin-D); [PMC12187100](https://pmc.ncbi.nlm.nih.gov/articles/PMC12187100/)).

**Critical periods:** Early diagnosis and initiation of high-dose calcium therapy is critical to prevent long-term skeletal deformity and to shorten time-to-healing; delayed diagnosis is explicitly associated with longer treatment courses (up to 6 months of IV calcium in severe/delayed cases per the Saudi cohort).

---

## 9. Inheritance and Population

**Epidemiology:** VDDR2A/HVDRR is an ultra-rare disorder without a well-established global prevalence figure specific to the 2A subtype. The broader category of hypocalcemic vitamin D-dependent rickets (VDDR overall, types 1 and 2) has been estimated in Denmark at approximately **1 in 250,000 children under age 15** ([search synthesis, cf. Springer VDDR review](https://link.springer.com/rwe/10.1007/978-3-319-66816-1_1803-1)); no dedicated Orphanet prevalence class specific to VDDR2A was retrieved in this search (VDDR is grouped under "Hypocalcemic vitamin D-dependent rickets" in Orphanet without a granular 2A-specific number). Given the low observed patient counts in the literature (dominated by single-family/single-case reports across Chinese, Egyptian, Saudi, and other largely consanguineous populations), a `prevalence_class` of `ULTRA_RARE` or the Orphanet numeric band `BELOW_1_IN_1000000` is a reasonable placeholder pending confirmation from an authoritative source.

**Inheritance pattern:** **Autosomal recessive** in the great majority of reported cases (biallelic VDR mutations); rare **dominant-negative heterozygous** cases have been documented via a distinct molecular mechanism (constitutive corepressor recruitment) ([PMC5365159](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5365159/)), and at least one atypical single-heterozygous-variant presentation has been reported clinically ([PMC12003035](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003035/)) — curators should model both an `AR` `Inheritance` block and, where the evidence supports it, a distinct dominant-negative note rather than conflating the two mechanisms.

**Penetrance:** Effectively complete for the biochemical/skeletal phenotype in biallelic loss-of-function carriers; **variable expressivity** for alopecia (ranging from absent to total), correlating with the severity/type of the underlying functional VDR defect (ligand-binding vs. DNA-binding vs. dominant-negative).

**Genetic anticipation:** Not reported/applicable (VDR loss-of-function is not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the sources reviewed, though theoretically possible for any autosomal recessive condition; not a prominent feature of the VDDR2A literature.

**Founder effects / consanguinity:** Strongly relevant — many reported kindreds are from consanguineous populations (Chinese, Egyptian, Middle Eastern/Saudi), and **uniparental disomy** has been documented as an alternative route to apparent homozygosity without biparental transmission ([PMC4496068](https://pmc.ncbi.nlm.nih.gov/articles/PMC4496068/)).

**Carrier frequency:** Not established/reported in the literature surveyed, consistent with the largely private nature of pathogenic VDR alleles.

**Population demographics:** No strong sex predilection is reported (autosomal, not X-linked); case series span pediatric populations globally, with concentration of published cohorts in the Middle East/North Africa and East Asia, likely reflecting both true prevalence (consanguinity rates) and reporting/ascertainment patterns.

---

## 10. Diagnostics

**Core laboratory pattern:** Hypocalcemia, hypophosphatemia (though may be absent — see atypical presentations), elevated alkaline phosphatase, elevated PTH (secondary hyperparathyroidism), and the **key discriminating test: markedly elevated (not low) serum 1,25-dihydroxyvitamin D**, which distinguishes VDDR2A from VDDR1A (CYP27B1 defect, low 1,25(OH)₂D) and from nutritional vitamin D deficiency (low 25-OH-D, low/normal 1,25(OH)₂D).

**Imaging:** Plain radiographs showing classic rachitic changes — metaphyseal widening/fraying/cupping, growth plate widening, long-bone bowing (genu varum), demineralization — used both for diagnosis and to monitor healing response to treatment.

**Genetic testing:** **VDR sequence analysis** (single-gene sequencing or inclusion in a rickets/metabolic bone disease gene panel, or exome sequencing) is the definitive diagnostic step, especially important because hypophosphatemia-predominant presentations can be clinically indistinguishable from FGF23-mediated hypophosphatemic rickets without genetic confirmation ([Karger 2025](https://karger.com/hrp/article/doi/10.1159/000546444/927170/Persistent-Hyperparathyroidism-in-Vitamin-D)). Whole-exome sequencing has been used successfully to identify novel homozygous pathogenic VDR variants (e.g., R343C) in atypical presentations ([JCEM Case Reports 2024](https://academic.oup.com/jcemcr/article/4/8/luag189/8732980)).

**Differential diagnosis:**
- **VDDR1A** (CYP27B1 biosynthetic defect): low 1,25(OH)₂D (vs. elevated in VDDR2A), elevated PTH in both.
- **VDDR1B** (CYP2R1 defect — 25-hydroxylase deficiency).
- **VDDR2B** (normal VDR gene/protein; end-organ resistance instead caused by a nuclear ribonucleoprotein that interferes with VDR-DNA interaction — phenotypically similar to 2A but with an intact receptor gene) ([OMIM 277440](https://www.omim.org/entry/277440)).
- **Nutritional (vitamin D deficiency) rickets** — distinguished by low 25-OH-D.
- **FGF23-mediated hereditary hypophosphatemic rickets** (e.g., XLH/PHEX) — an important pitfall because VDDR2A can present with isolated hypophosphatemia without hypocalcemia, mimicking this category; genetic testing is required to discriminate ([JCEM Case Reports 2024](https://academic.oup.com/jcemcr/article/4/8/luag189/8732980); [PMC12187100](https://pmc.ncbi.nlm.nih.gov/articles/PMC12187100/)).

**Screening:** No population newborn-screening program targets VDDR2A specifically, given its rarity; diagnosis relies on clinical suspicion (rickets ± alopecia with markedly elevated 1,25(OH)₂D) followed by targeted or exome genetic testing. Cascade/carrier testing within affected consanguineous families is appropriate once a familial pathogenic variant is identified.

---

## 11. Outcome/Prognosis

**Mortality:** Not associated with increased mortality when appropriately diagnosed and treated with calcium repletion; severe untreated hypocalcemia can produce life-threatening seizures/tetany acutely, but chronic mortality data specific to VDDR2A were not identified in this literature review — the disorder is generally considered manageable rather than lethal.

**Morbidity/functional outcome:** With prompt, adequately dosed calcium therapy, **rickets is fully radiographically and biochemically reversible** — documented cases show return to normal ambulation within weeks and complete radiographic healing within ~3 months to 6 months depending on delay-to-diagnosis and severity. Persistent secondary hyperparathyroidism can, however, remain elevated even after phosphate/rickets normalization, per a 2025 Hormone Research in Paediatrics report ([Karger 2025](https://karger.com/hrp/article/doi/10.1159/000546444/927170/Persistent-Hyperparathyroidism-in-Vitamin-D)) — an important point for long-term monitoring guidance.

**Alopecia prognosis:** Generally **persistent/refractory to treatment** — patients with alopecia tend to have more severe underlying receptor dysfunction and respond less well to vitamin D metabolite therapy overall, often requiring the more aggressive calcium-infusion regimens ([PMC3196847](https://pmc.ncbi.nlm.nih.gov/articles/PMC3196847/)). Some case reports document partial or full resolution of alopecia with conventional-dose 1α-hydroxycholecalciferol plus oral calcium in milder genotypes ([PubMed 21118628](https://pubmed.ncbi.nlm.nih.gov/21118628/)), indicating genotype-dependent variability rather than a uniformly fixed outcome.

**Prognostic factors:** Presence/severity of alopecia (marker of more severe VDR dysfunction and poorer response to vitamin D-based therapy), timeliness of diagnosis (delayed diagnosis associated with longer treatment courses), and specific mutation type (ligand-binding-domain vs. DNA-binding-domain vs. dominant-negative mutations differ in residual receptor function and thus treatment responsiveness).

---

## 12. Treatment

**First-line strategy — bypass the receptor defect with calcium, not vitamin D metabolites.** Because the fundamental lesion is receptor unresponsiveness rather than ligand deficiency, simply increasing vitamin D or calcitriol dosing is often ineffective; the mainstay of therapy is **high-dose calcium supplementation**, sufficient to drive passive (non-VDR-dependent, paracellular) intestinal calcium absorption:

- **Mild-to-moderate cases:** managed with high-dose **oral calcitriol** plus supplemental **oral calcium** ([case-based review](https://www.ijpediatrics.com/index.php/ijcp/article/view/5217); [PubMed 7833085 — oral calcium treatment in VDDR type II](https://pubmed.ncbi.nlm.nih.gov/7833085/)).
- **Severe/alopecic/treatment-refractory cases:** require **intravenous (IV) calcium infusion**, shown to be more potent/effective than oral therapy for rapid clinical, radiological, and biochemical improvement. Reported protocols include daily calcium gluconate infusion (e.g., 250 mg elemental calcium every 8 hours, several days per week) continued until calcium/phosphate normalize — typically averaging **8 weeks**, up to **6 months** in severe/delayed-diagnosis cases ([Frontiers, Saudi Arabia cohort](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1365714/full)). Documented outcomes include return to independent ambulation within ~2 weeks and complete radiographic healing by ~3 months.
- An adult-onset case documented favorable changes in **bone metabolic parameters following oral calcium supplementation** ([PubMed 28367941](https://pubmed.ncbi.nlm.nih.gov/28367941/)).

**Pharmacotherapy — vitamin D analogs:** High-dose active vitamin D metabolites (calcitriol, 1α-hydroxycholecalciferol/alfacalcidol) are used adjunctively, particularly in milder genotypes, and can improve both rickets and (in some reports) alopecia ([PubMed 21118628](https://pubmed.ncbi.nlm.nih.gov/21118628/)). Suggested NCIT term: `NCIT:C15986` (Pharmacotherapy) with `therapeutic_agent` bound to CHEBI calcitriol (CHEBI:17823) or alfacalcidol.

**Alopecia-directed/experimental approaches:**
- Because alopecia in VDR-null models arises from a **ligand-independent** VDR function in keratinocytes, systemic calcitriol/calcium therapy does not reliably restore hair growth; **topical calcipotriol** (a vitamin D analog with reduced calcemic activity, used for its VDR-binding/epidermal-differentiation effects independent of systemic calcium metabolism) has been explored for alopecia areata and is mechanistically relevant here, though robust VDDR2A-specific efficacy data are limited ([Ann Dermatol / calcipotriol review](https://anndermatol.org/DOIx.php?id=10.5021%2Fad.2012.24.3.341)).
- **Gene-therapy proof-of-concept:** a VDR-expressing adenoviral vector has been used experimentally to treat alopecia in a rat model of type II rickets, restoring hair-follicle VDR expression ([PMC10613246](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10613246/)) — MODEL_ORGANISM evidence, not yet a human therapy.
- Note: **seocalcitol (EB1089)** and related low-calcemic vitamin D analogs are primarily investigated as **anticancer agents** (pancreatic, hepatocellular, CLL) rather than as VDDR2A treatments specifically — relevant mainly as background on structure-activity of VDR ligands, not a direct VDDR2A therapeutic ([BJC EB1089 pancreatic cancer trial](https://www.nature.com/articles/6600162)).

**Surgical/orthopedic:** Corrective orthopedic surgery may be required for severe or fixed long-bone deformity in cases with delayed diagnosis/treatment, though this is supportive rather than disease-modifying (suggested NCIT `C16186`, Orthopedic Surgical Procedure).

**Supportive care:** Physical therapy/rehabilitation (NCIT:C15302) to address motor delay from rachitic myopathy/deformity during and after biochemical treatment.

**Monitoring:** Serial calcium, phosphate, alkaline phosphatase, and PTH; per the 2025 Karger report, **PTH may remain persistently elevated despite normalization of phosphate and radiographic healing**, so PTH cannot be used alone as a marker of complete treatment response ([Karger 2025](https://karger.com/hrp/article/doi/10.1159/000546444/927170/Persistent-Hyperparathyroidism-in-Vitamin-D)).

**Experimental/clinical trials:** No VDDR2A-specific registered interventional trials were identified in this search; management is derived from case-report-level and small single-center retrospective evidence, not randomized trial data.

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (this is a fully penetrant Mendelian genetic disorder) — the relevant "primary prevention" tool is **genetic counseling and carrier/prenatal testing** in consanguineous families or families with a known proband, given the autosomal recessive (occasionally dominant-negative) inheritance.

**Secondary prevention (early detection):** Prompt clinical suspicion (rickets with elevated, not low, 1,25(OH)₂D; ± alopecia) and early genetic confirmation are the practical "secondary prevention" tools that shorten time-to-treatment and reduce the risk of severe/fixed skeletal deformity.

**Tertiary prevention:** Adequate ongoing calcium supplementation and monitoring to prevent recurrence of hypocalcemic crises and to protect against long-term skeletal deformity and growth impairment; monitoring for persistent hyperparathyroidism as a residual complication even after apparent rickets healing.

**Genetic counseling:** Recommended for parents of an affected child (autosomal recessive recurrence risk ~25% per pregnancy for the typical biallelic form) and for extended family members in consanguineous kindreds; prenatal or preimplantation testing is technically feasible once the familial pathogenic VDR variant(s) are known, though this was not specifically documented as routine practice in the sources reviewed.

**Public health/behavioral:** General population-level vitamin D/calcium sufficiency programs (e.g., sunlight exposure guidance, dietary fortification) address nutritional rickets but have no bearing on the genetic VDR-resistance mechanism underlying VDDR2A specifically.

---

## 14. Other Species / Natural Disease

No naturally occurring VDDR2A/HVDRR case in a non-human companion-animal or wildlife species (i.e., a spontaneous VDR-null phenotype analogous to human disease) was identified in this search; the available cross-species data are from **engineered rodent models** (see §15) rather than naturally occurring veterinary disease. Curators should check OMIA (Online Mendelian Inheritance in Animals) directly if a naturally occurring animal correlate is needed for the entry, as this was not surfaced by the searches performed here.

---

## 15. Model Organisms

**VDR knockout (Vdr⁻/⁻) mouse:** The primary and best-characterized animal model. **Targeted ablation of VDR** produces a mouse model that recapitulates the core human VDDR2A phenotype: mice are normal at birth but develop **growth retardation, hypocalcemia, hyperparathyroidism, rickets, osteomalacia, and alopecia** — closely mirroring human VDDR2A with alopecia ([PNAS 94(18):9831](https://www.pnas.org/doi/10.1073/pnas.94.18.9831); [JCI 11676](https://www.jci.org/articles/view/11676); [PubMed 22903507 — physiological insights review](https://pubmed.ncbi.nlm.nih.gov/22903507/)).
- **Fidelity:** High for the skeletal/mineral-metabolism phenotype (RECAPITULATES) and for alopecia (RECAPITULATES) — the mouse model directly established that alopecia results from **defective anagen (hair growth phase) initiation** and demonstrated the **ligand-independent** role of VDR in hair-follicle keratinocytes (a keratinocyte-specific VDR transgene with a ligand-binding-abolishing mutation still restores normal hair cycling in VDR-null mice) ([Oxford Mol Endocrinol 19(4):855](https://academic.oup.com/mend/article/19/4/855/2741289); [PNAS 0702884104](https://www.pnas.org/doi/10.1073/pnas.0702884104)).
- **Limitation:** Because the alopecia-preventing VDR function is ligand-independent, this model demonstrates that vitamin D/calcitriol-based pharmacotherapy is mechanistically unlikely to reverse alopecia — a translational insight directly informing human treatment expectations (§12).

**Humanized VDR mouse models:** A "humanized" mouse model of HVDRR **without alopecia** has been engineered, allowing dissociation of the rachitic/mineral phenotype from the alopecia phenotype and enabling study of genotype-phenotype correlation for specific human VDR mutations ([PubMed 25147982](https://pubmed.ncbi.nlm.nih.gov/25147982/); [Endocrinology 155(11):4137](https://academic.oup.com/endo/article-abstract/155/11/4137/2422423)).

**Rat model:** A rat model of "type II rickets" with alopecia has been used as a preclinical platform for **VDR gene-therapy** proof-of-concept (adenoviral VDR-expressing vector) targeting the alopecia phenotype specifically ([PMC10613246](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10613246/)).

**Applications:** These rodent models have been used to (1) establish the causal relationship between VDR loss and both the mineral/skeletal phenotype and alopecia, (2) dissect ligand-dependent (mineral metabolism) versus ligand-independent (hair cycle) VDR functions, (3) test genotype-specific functional consequences of human VDR mutations via "humanized" knock-in approaches, and (4) pilot gene-replacement therapeutic strategies for the alopecia arm of the disease.

**Suggested NCBITaxon terms:** NCBITaxon:10090 (Mus musculus), NCBITaxon:10116 (Rattus norvegicus).

---

## Summary of Key PMIDs/Sources for Curation

| Topic | Citation |
|---|---|
| OMIM disease/gene entries | OMIM #277440 (VDDR2A); OMIM *601769 (VDR) |
| Core clinical/molecular review | PMID (via PMC4589239) — Chinese HVDRR mutation series |
| Alopecia mechanism/frequency | PMC3196847 |
| I268T ligand-binding mutant functional study | PubMed 15308610 |
| V26M DNA-binding-domain mutant | PMC2794978 |
| Dominant-negative HVDRR mechanism | PubMed 28377956 / PMC5365159 |
| Uniparental disomy mechanism | PMC4496068 |
| Atypical hypophosphatemia-only presentation, R343C | JCEM Case Reports 2024 (academic.oup.com/jcemcr) |
| Persistent hyperparathyroidism despite healing | Karger 2025, PMC12187100 |
| Heterozygous VDDR2A with pseudoarthrosis | PMC12003035 (2025) |
| VDR knockout mouse — original model | PNAS 94(18):9831 (1997) |
| Ligand-independent VDR/alopecia mechanism | JCI 11676; Mol Endocrinol 19(4):855; PNAS 0702884104 |
| Humanized mouse model without alopecia | PubMed 25147982 |
| Gene-therapy rat model | PMC10613246 |
| VDR-RXR-VDRE transcriptional mechanism | Mol Endocrinol 17(11):2320; PMC3087838; PMC6332450 |

**Note on evidence-source classification for curation:** Case reports/series (majority of citations above) = HUMAN_CLINICAL; VDR-null mouse/rat and humanized-mouse studies = MODEL_ORGANISM; in-vitro transactivation/reporter-gene assays of specific VDR mutants = IN_VITRO. No COMPUTATIONAL-only evidence was identified as primary support for any major claim in this report.

Sources:
- [Entry - #277440 - VITAMIN D-DEPENDENT RICKETS, TYPE 2A; VDDR2A - OMIM](https://www.omim.org/entry/277440)
- [Entry - *601769 - VITAMIN D RECEPTOR; VDR - OMIM](https://omim.org/entry/601769)
- [vitamin D-dependent rickets, type 2A - NORD](https://rarediseases.org/mondo-disease/vitamin-d-dependent-rickets-type-2a/)
- [Heterozygous Hereditary Vitamin D-Dependent Rickets Type 2A (VDDR2A) in a Patient Presenting With Pseudoarthrosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003035/)
- [Novel Vitamin D Receptor Mutations in Hereditary Vitamin D Resistant Rickets in Chinese - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589239/)
- [The Role of Vitamin D Receptor Mutations in the Development of Alopecia - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3196847/)
- [Compound heterozygous mutations in the vitamin D receptor in a patient with hereditary 1,25-dihydroxyvitamin D-resistant rickets with alopecia - PubMed](https://pubmed.ncbi.nlm.nih.gov/19049339/)
- [Hereditary 1,25-dihydroxyvitamin D-resistant rickets with alopecia resulting from a novel missense mutation in the DNA-binding domain of the vitamin D receptor - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2794978/)
- [Hereditary vitamin D resistant rickets: novel splice site mutation, oral calcium therapy - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S8756328209016238)
- [Functional Analysis of VDR Gene Mutation R343H - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5681508/)
- [Hereditary 1,25-dihydroxyvitamin D-resistant rickets with alopecia in four Egyptian families - PubMed](https://pubmed.ncbi.nlm.nih.gov/24859502/)
- [Case of vitamin D–dependent rickets type 2A presenting with hypophosphatemia without hypocalcemia - JCEM Case Reports](https://academic.oup.com/jcemcr/article/4/8/luag189/8732980)
- [Persistent Hyperparathyroidism in Vitamin D-Dependent Rickets Type 2A - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12187100/)
- [Persistent Hyperparathyroidism in Vitamin D-Dependent Rickets Type 2A - Karger](https://karger.com/hrp/article/doi/10.1159/000546444/927170/Persistent-Hyperparathyroidism-in-Vitamin-D)
- [Clinical characteristics and long-term management for VDDR type II - Saudi Arabia cohort - Frontiers](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1365714/full)
- [Oral calcium treatment in vitamin D-dependent rickets type II - PubMed](https://pubmed.ncbi.nlm.nih.gov/7833085/)
- [Changes in bone metabolic parameters following oral calcium supplementation - PubMed](https://pubmed.ncbi.nlm.nih.gov/28367941/)
- [Hereditary 1,25-dihydroxyvitamin D-resistant rickets (HVDRR) caused by a VDR mutation: novel mechanism of dominant inheritance - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5365159/)
- [Hereditary 1,25-dihydroxyvitamin D resistant rickets due to a mutation causing multiple defects in VDR function - PubMed](https://pubmed.ncbi.nlm.nih.gov/15308610/)
- [Detection of Hereditary 1,25-Hydroxyvitamin D-Resistant Rickets Caused by Uniparental Disomy of Chromosome 12 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4496068/)
- [VDR gene - GeneCards](https://www.genecards.org/card/VDR)
- [Vitamin D Dependent Rickets 2A With Alopecia: Three Cases With Novel Genetic Variants - PubMed](https://pubmed.ncbi.nlm.nih.gov/39716449/)
- [Heterozygous Hereditary Vitamin D‐Dependent Rickets Type 2A (VDDR2A) in a Patient Presenting With Pseudoarthrosis - Wiley](https://onlinelibrary.wiley.com/doi/10.1155/crie/2434759)
- [Novel VDR gene mutation in a VDDR2A compound heterozygote - Endocrine Abstracts](https://www.endocrine-abstracts.org/ea/0110/ea0110ep247)
- [Vitamin D dependent rickets type 2A in a 1-year-old girl - Endocrine Abstracts](https://www.endocrine-abstracts.org/ea/0110/ea0110p267)
- [JCI - Metabolic and cellular analysis of alopecia in vitamin D receptor knockout mice](https://www.jci.org/articles/view/11676)
- [A humanized mouse model of hereditary 1,25-dihydroxyvitamin D-resistant rickets without alopecia - PubMed](https://pubmed.ncbi.nlm.nih.gov/25147982/)
- [Humanized Mouse Model of HVDRR Without Alopecia - Oxford Academic](https://academic.oup.com/endo/article-abstract/155/11/4137/2422423)
- [Physiological insights from the vitamin D receptor knockout mouse - PubMed](https://pubmed.ncbi.nlm.nih.gov/22903507/)
- [Targeted ablation of the vitamin D receptor: An animal model of VDDR type II with alopecia - PNAS](https://www.pnas.org/doi/10.1073/pnas.94.18.9831)
- [Gene therapy for alopecia in type II rickets model rats using VDR-expressing adenovirus vector - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10613246/)
- [The role of vitamin D receptor signaling in hair follicle health and alopecia - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12747802/)
- [Vitamin D receptor is essential for normal keratinocyte stem cell function - PNAS](https://www.pnas.org/doi/10.1073/pnas.0702884104)
- [Ligand-Independent Actions of the Vitamin D Receptor Maintain Hair Follicle Homeostasis - Oxford Academic](https://academic.oup.com/mend/article/19/4/855/2741289)
- [Ligand-Independent Vitamin D Receptor Actions Essential for Keratinocyte Homeostasis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11720424/)
- [Retinoid X Receptor Is a Nonsilent Major Contributor to VDR-Mediated Transcriptional Activation - Oxford Academic](https://academic.oup.com/mend/article/17/11/2320/2747379)
- [DNA binding alters coactivator interaction surfaces of the intact VDR–RXR complex - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3087838/)
- [Relationship of Structure and Function of DNA-Binding Domain in Vitamin D Receptor - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6332450/)
- [Vitamin D Hydroxylation-Deficient Rickets (VDDR) – Types 1A, 1B, 2A, 2B - Springer](https://link.springer.com/rwe/10.1007/978-3-319-66816-1_1803-1)
- [Orphanet: Hypocalcemic vitamin D-dependent rickets](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=289157&lng=EN)
- [Vitamin D-dependent rickets, type 2 - NIH GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3536983/)
- [Vitamin D-dependent rickets type II with alopecia - NIH GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C0342646/)
- [A phase II trial of seocalcitol (EB1089) in inoperable pancreatic cancer - British Journal of Cancer](https://www.nature.com/articles/6600162)
- [Alopecia in vitamin D-dependent rickets type II responding to 1α-hydroxycholecalciferol - PubMed](https://pubmed.ncbi.nlm.nih.gov/21118628/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 24 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1159/000546444/927170/Persistent-Hyperparathyroidism-in-Vitamin-D` (6 mentions) - Identifier did not resolve to a record