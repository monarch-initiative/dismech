---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-15T19:10:33.622777'
end_time: '2026-08-15T19:16:37.028156'
duration_seconds: 363.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chromosome 3q29 Microdeletion Syndrome
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
  web_search_requests: 22
  num_turns: 31
  total_cost_usd: 2.31747
  session_id: 8ebdbdea-f16d-5e75-8ed9-a88b56851407
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 23
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromosome 3q29 Microdeletion Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chromosome 3q29 Microdeletion Syndrome** covering all of the
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

I'll research this now using web search to gather accurate, citable information on Chromosome 3q29 Microdeletion Syndrome.

# Chromosome 3q29 Microdeletion Syndrome: Comprehensive Research Report

## 1. Disease Information

### Overview
Chromosome 3q29 microdeletion syndrome (3q29Del) is a recurrent genomic disorder caused by a heterozygous, typically de novo, ~1.6 Mb deletion at cytoband 3q29 (chr3:195,998,129–197,623,129, GRCh38), mediated by nonallelic homologous recombination (NAHR) between flanking low-copy repeats (LCRs) [Willatt et al., *Am J Hum Genet*, 2005, PMID:15918153]. It was first delineated as a distinct clinical entity in 2005 in a report of six unrelated patients: "3q29 microdeletion syndrome: clinical and molecular characterization of a new syndrome" — the deletion was shown to be a recurrent, LCR-flanked rearrangement distinguishable from earlier, non-recurrent 3q29 deletions reported since 2001. The syndrome is now recognized as one of the strongest-effect genetic risk factors for schizophrenia identified to date (odds ratio >40), alongside a broad, highly variable neurodevelopmental, psychiatric, and multisystem medical phenotype.

### Key Identifiers
| Resource | Identifier |
|---|---|
| OMIM (deletion) | #609425 — Chromosome 3q29 deletion syndrome |
| OMIM (reciprocal duplication) | #611936 — Chromosome 3q29 duplication syndrome |
| Orphanet | ORPHA:65286 |
| MONDO | MONDO:0012269 (chromosome 3q29 microdeletion syndrome) |
| MedGen | C2674949 |
| GeneReviews | NBK385289 ("3q29 Recurrent Deletion") |
| ICD-10 | Q93.5 (other deletions of part of a chromosome) — no dedicated ICD-10/11 code; captured under chromosomal microdeletion syndromes NEC |
| Suggested MONDO cross-term | MONDO:0012269 |

### Synonyms / Alternative Names
- 3q29 deletion syndrome
- 3q29 microdeletion syndrome
- Del(3)(q29)
- Monosomy 3q29
- DEL3q29 (registry/lay shorthand)

### Data Source Character
Knowledge of this syndrome derives almost entirely from **aggregated, deeply-phenotyped disease-level cohort resources**, not incidental EHR mining — chiefly the **Emory 3q29 Registry / 3q29 Project** (3q29deletion.org; >100 enrolled families as of the mid-2020s; study protocol PMID:29884173), which recruits via self-referral and performs direct, in-person, gold-standard psychiatric/cognitive/medical assessment (e.g., the "Deep phenotyping" cohort of 32 individuals, PMID:33564151). This is supplemented by population-ascertainment studies (Icelandic deCODE cohort, UK Biobank) that establish prevalence and baseline penetrance independent of clinical ascertainment bias, and by case-control CNV burden studies in schizophrenia cohorts (PGC, GAIN, Ashkenazi Jewish cohort) that established the psychiatric risk association.

---

## 2. Etiology

### Disease Causal Factor
3q29Del is caused entirely by **genomic structural variation** — a hemizygous deletion of ~21–22 protein-coding genes at 3q29 — not by infectious, purely environmental, or classical single-gene point-mutation mechanisms. It is a genomic disorder in the same mechanistic class as 22q11.2, 16p11.2, and 1q21.1 deletion syndromes.

### Molecular/Mechanistic Basis
- **NAHR between LCRs**: The deletion arises from unequal crossing-over between misaligned low-copy repeats flanking the 3q29 region during meiosis, producing a highly recurrent ~1.6 Mb deletion with near-identical breakpoints across unrelated patients (GeneReviews, NBK385289).
- The reciprocal NAHR product is the **3q29 microduplication** (OMIM #611936), providing a natural "dosage" comparator.

### Genetic Risk Factors
- **The deletion itself is the causal lesion** — there is no known additional germline variant required for the deletion to arise (it is a de novo structural mutation in most cases).
- **Genetic modifiers of expressivity**: No single gene within the interval is necessary and sufficient for the full phenotype; mouse single-gene knockouts of *Dlg1* or *Pak2* alone fail to recapitulate the syndrome, supporting a **polygenic/oligogenic model within the CNV** in which multiple genes (candidates: *DLG1*, *PAK2*, *NCBP2*, and the ubiquitination/SUMOylation gene cluster *UBXN7*, *FBXO45*, *RNF168*, *SENP5*) act combinatorially [Rump et al./PLOS Genetics 2020, PMID:32053595; *Journal of Neurodevelopmental Disorders* 2026, "Driver or passenger?"].
- **Polygenic background**: Oetjens et al. (*Nat Commun*, 2019;10:4897) quantified a measurable contribution of genome-wide common-variant polygenic burden to variable expressivity across 11 rare CNV/monogenic disorders including 3q29Del, indicating that background common-variant load modulates phenotypic severity on top of the CNV.
- **Parental origin/mosaicism**: A minority (~7% of tested families) of cases are inherited from an unaffected or mildly affected parent; germline/somatic mosaicism has been documented, giving simplex families a low (<1%, but above general-population) recurrence risk.

### Environmental Risk Factors
No specific environmental cause or trigger for the deletion event itself has been identified (as with other NAHR-mediated CNVs, advanced parental age has been hypothesized as a general risk factor for de novo CNVs but is not specifically established for 3q29). No teratogenic, toxin, or infectious contributor is documented.

### Protective Factors
No genetic or environmental protective factor against deletion occurrence or phenotype severity is established. Reduced penetrance is observed (unaffected or mildly-affected transmitting parents exist), but the modifiers of this reduced penetrance (aside from polygenic background, above) are not yet characterized.

### Gene-Environment Interactions
Not established for this syndrome; the literature to date is dominated by CNV-dosage and within-locus gene-gene interaction studies (Drosophila/Xenopus pairwise-interaction screening, PMID:32053595) rather than classical GxE analysis.

---

## 3. Phenotypes

3q29Del produces a highly pleiotropic, variably expressive phenotype spanning neurodevelopmental, neuropsychiatric, gastrointestinal, cardiac, musculoskeletal, craniofacial, ophthalmologic, dental, and neuroradiological domains. The most systematic data come from the Emory "Deep phenotyping" study of 32 directly-assessed individuals (Sanchez Russo et al., *Genet Med*, 2021;23(5):872–880, PMID:33564151) and the companion cognitive/registry studies.

### Neurodevelopmental
| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Developmental delay | 70–90% | HP:0001263 Global developmental delay |
| Intellectual disability (mild–moderate) | 30–40% (34% in deep-phenotyping cohort) | HP:0001256 Intellectual disability, mild |
| Speech/language delay | ~60% | HP:0000750 Delayed speech and language development |
| Motor delay / hypotonia (infancy) | ~34% | HP:0001290 Generalized hypotonia |
| Executive function deficits | 46–47% | HP:0031466 Impairment in personality function (or free-text) |
| Graphomotor weakness | 78% | HP:0011936 (fine motor delay proxy) |
| Distinct cognitive profile: verbal > nonverbal strength (mean FSIQ 73, range 40–99; verbal mean 80 vs. nonverbal mean 75) | n=32 cohort | — |

### Neuropsychiatric (onset typically childhood–young adulthood; can present earlier than population norms)
| Phenotype | Frequency | HPO term |
|---|---|---|
| ADHD | 63% | HP:0007018 Attention deficit hyperactivity disorder |
| Anxiety disorder | 40% | HP:0000739 Anxiety |
| Autism spectrum disorder | 29–38% (registry: 29.0% vs. 1.47% general population, p<2.2×10⁻¹⁶; deep-phenotyping cohort: 37.5%) | HP:0000729 Autistic behavior |
| Psychotic disorder / schizophrenia spectrum | ~19–20% (>40-fold increased risk vs. population) | HP:0000709 Psychosis |
| Prodromal psychosis | 14% | — |
| Bipolar disorder with psychosis | reported | HP:0007302 |

Distinct ASD phenotype: individuals with 3q29Del show a reduced male:female ratio for autism (2:1 vs. typical 4:1) and a distinctive profile of substantially elevated Restricted Interests and Repetitive Behaviors with comparatively milder Social Motivation impairment relative to idiopathic autism [Pollak et al., *Molecular Autism*, 2019;10:30, PMID:31346402].

### Gastrointestinal (most common medical system involved, ~81–84%)
- Feeding difficulty in infancy (latching problems) — often first presenting sign
- Gastroesophageal reflux — ~50%
- Chronic constipation — ~41%
- Failure to thrive — ~44%
- HPO: HP:0011968 Feeding difficulties; HP:0002020 Gastroesophageal reflux; HP:0002019 Constipation; HP:0001508 Failure to thrive

### Cardiac
- Congenital heart defects — 25%, no single predominant lesion; patent ductus arteriosus most frequent, also reported: ventricular septal defect, pulmonary stenosis/atresia, tricuspid stenosis, hypoplastic right heart
- HPO: HP:0001631 Atrial septal defect; HP:0001643 Patent ductus arteriosus; HP:0004415 Hypoplastic right heart

### Musculoskeletal (~84%)
- Joint laxity, chest wall deformity (pectus), long/tapering fingers, scoliosis (screened annually)
- HPO: HP:0001382 Joint hypermobility; HP:0000768 Pectus carinatum; HP:0100807 Long fingers

### Craniofacial (subtle dysmorphism)
- Long/narrow face, short philtrum, high nasal bridge, prominent forehead, wide/prominent nasal tip, thin upper lip vermilion
- HPO: HP:0000343 Long philtrum (or short, per source); HP:0000426 Prominent nasal bridge; HP:0000219 Thin vermilion border

### Ophthalmologic (59%)
- Strabismus (28%), other ocular anomalies
- HPO: HP:0000486 Strabismus

### Dental (41%) and Otologic
- Dental anomalies; recurrent otitis media (~22%)
- HPO: HP:0000164 Abnormality of the dentition; HP:0000388 Otitis media

### Neuroradiological (posterior fossa; ~71% abnormal on MRI, n=24)
- Cerebellar vermis hypoplasia — 33%
- Retrocerebellar arachnoid cyst / mega cisterna magna — 29%
- Reduced cerebellar cortex volume, increased cerebellar white matter volume vs. controls [Sanders et al./*Mol Psychiatry* 2024, PMID:38744992]; cerebellar volumetrics correlate with visuomotor and IQ measures
- HPO: HP:0001321 Cerebellar hypoplasia; HP:0002571 Retrocerebellar cyst

### Other
- Reduced birth weight/postnatal growth deficits; enuresis (~22–25%); sleep disturbance (~31%); seizures (~13%, generally mild/treatment-responsive) — HPO: HP:0001518 Small for gestational age; HP:0000805 Enuresis; HP:0001250 Seizure

### Quality of Life
No syndrome-specific EQ-5D/SF-36 dataset exists; qualitative registry data emphasize substantial functional burden from the combination of GI symptoms, executive dysfunction, and psychiatric comorbidity, with caregiver-reported reduced adaptive behavior even in carriers not meeting formal ID criteria.

---

## 4. Genetic/Molecular Information

### Causal Locus
- **Region**: 3q29, chr3:195,998,129–197,623,129 (GRCh38); ~1.6 Mb (older coordinate sets: chr3:195,756,054–197,344,665, GRCh37)
- **Gene content**: 21–22 protein-coding genes, plus noncoding transcripts. Confirmed gene list within the canonical interval: *TFRC, ZDHHC19, SLC51A, PCYT1A, TCTEX1D2, UBXN7, RNF168, C3orf43 (WDR53-adjacent), WDR53, FBXO45, NRROS, CEP19, PIGX, PAK2, SENP5, NCBP2, NCBP2-AS2, PIGZ, MFI2, MFI2-AS1, DLG1, DLG1-AS1*, plus intervening lincRNAs (e.g., *LINC00885*) and *MIR4797*.
- No single gene has been definitively established as necessary and sufficient (no monogenic "driver" confirmed); current models favor combinatorial/oligogenic haploinsufficiency (HGNC-suggested key genes below).

### Candidate/Leading Genes
| Gene | HGNC | Function | Evidence |
|---|---|---|---|
| **DLG1** (Disks large homolog 1 / SAP97) | hgnc:2905 | MAGUK scaffold; trafficking of AMPA/NMDA glutamate receptors to synaptic membrane; autosomal paralog of X-linked ID gene *DLG3* | Candidate since original 2005 report; PMID:15918153 |
| **PAK2** (p21-activated kinase 2) | hgnc:8591 | Actin cytoskeleton remodeling; neuronal migration, neurite outgrowth, dendritic spine morphogenesis; autosomal paralog of X-linked ID gene *PAK3* | PAK2 haploinsufficiency linked to synaptic cytoskeleton impairment and autism-related behavior in model systems |
| **NCBP2** (Nuclear cap-binding protein subunit 2 / CBP20) | hgnc:7647 | Component of the nuclear cap-binding complex; mRNA processing/export | Acts as a key genetic **modifier/enhancer** of neurodevelopmental phenotypes of other 3q29 gene homologs in Drosophila/Xenopus screens [PMID:32053595] |
| **UBXN7, FBXO45, RNF168, SENP5** | hgnc:29076; hgnc:24129; hgnc:20620; hgnc:20351 | Ubiquitination/SUMOylation pathway components; *RNF168* is causal for RIDDLE syndrome (DNA-damage response) | Compound haploinsufficiency across this 4-gene cluster implicated as a converging pathway in the 2026 "Driver or passenger?" reassessment |
| PIGX, PIGZ | hgnc:23443; hgnc:30288 | GPI-anchor biosynthesis | Included in interval; not individually linked to core phenotype |
| TFRC | hgnc:11763 | Transferrin receptor, cellular iron uptake | Boundary gene, used to define mouse syntenic deletion (*Bdh1–Tfrc* interval) |
| CEP19 | hgnc:29020 | Centrosomal/ciliary protein; implicated in obesity | Candidate for microduplication-associated obesity phenotype |

### Pathogenic Variant Classification
- **Variant class**: Contiguous-gene microdeletion (structural/copy-number variant), not point mutation. ACMG/AMP CNV classification: Pathogenic per ClinGen dosage sensitivity criteria (recurrent LCR-mediated CNV with established gene-dosage disease association).
- **Origin**: Overwhelmingly **de novo** (~93% of tested trios); ~7% inherited from a parent (who may be subclinically affected or mosaic).
- **Allele frequency**: Extremely rare in population reference databases — population-based ascertainment (Iceland: 3/101,655; UK Biobank: 5/152,728) yields a population prevalence estimate of ~1:30,000–1:40,000; the CNV is not expected/observed at appreciable frequency in gnomAD-SV given its severe, penetrant phenotype and largely de novo occurrence.
- **Functional consequence**: Loss-of-function via **hemizygous gene-dosage reduction (haploinsufficiency)** across the ~21-gene interval, not a single-protein structural defect.
- **Somatic vs. germline**: Germline (constitutional) CNV; documented instance of parental germline/somatic mosaicism.

### Modifier Genes
As above — NCBP2 as an enhancer/modifier of other 3q29 homolog phenotypes in Drosophila/Xenopus; genome-wide polygenic background (Oetjens et al. 2019) as a quantitative modifier of expressivity.

### Epigenetic Information
No syndrome-specific DNA methylation or histone-modification signature has yet been reported in the literature to date; this remains an open area (unlike more established "episignature" CNV syndromes such as 22q11.2DS).

### Chromosomal Abnormality Detail
- Recurrent, NAHR-mediated, LCR-flanked microdeletion — not detectable by conventional G-banded karyotype; requires chromosomal microarray (CMA), FISH, MLPA, or qPCR for detection/confirmation.
- Reciprocal **microduplication** (OMIM #611936) at the same locus produces a distinct, generally milder but still variable phenotype (see below).

---

## 5. Environmental Information

No established environmental causal, exacerbating, or infectious factor has been identified for 3q29Del as a genomic disorder — the deletion event itself is a de novo (or rarely inherited) meiotic NAHR event, not environmentally triggered. There is no documented lifestyle, toxin, occupational, or infectious contributor to either deletion occurrence or phenotypic severity in the current literature. This is consistent with other NAHR-mediated recurrent microdeletion syndromes, where the LCR architecture of the locus — not exogenous exposure — is the primary determinant of recurrence.

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Genomic Lesion → Clinical Phenotype)
1. **Meiotic NAHR** between LCRs flanking 3q29 → recurrent ~1.6 Mb hemizygous deletion (biological_scale: MOLECULAR)
2. **Combinatorial/dose-dependent loss of multiple functionally-connected genes** (*DLG1, PAK2, NCBP2*, and the ubiquitination/SUMOylation cluster *UBXN7/FBXO45/RNF168/SENP5*) → convergent disruption of synaptic scaffolding, cytoskeletal dynamics, mRNA processing, and protein quality-control pathways (biological_scale: MOLECULAR/CELLULAR)
3. **Mitochondrial dysregulation and impaired metabolic flexibility**: cross-species transcriptomic analysis (CRISPR-engineered mouse cortex + isogenic human cortical organoids) found 176 concordantly differentially-expressed genes in excitatory neurons across species, converging on mitochondrial function/energy metabolism pathways, with PAK2 implicated as a contributor to the metabolic-flexibility deficit [Purcell/Sefik et al., *Sci Adv*, 2023;9(33):eadh0558, PMID:37585521]
4. **Synaptic and cytoskeletal dysfunction**: DLG1/PAK2 loss impairs AMPA/NMDA receptor trafficking and dendritic spine morphogenesis (CELLULAR)
5. **Cortical excitatory/inhibitory imbalance**: mouse model shows abnormally increased excitatory neural activity concentrated in auditory cortex, elevated immediate-early genes (*Egr2, Fos, Cyr61, Nr4a1, Btg2, Dusp1*), and decreased parvalbumin-positive interneuron density in sensory cortex [Baba et al., *Neuropsychopharmacology*, 2019;44(12):2125–2135, PMID:31216562] (CELLULAR/TISSUE)
6. **Cerebellar/posterior fossa developmental disruption**: reduced cerebellar cortical volume with increased white matter volume, associated with visuomotor/cognitive deficits (TISSUE)
7. **Convergent behavioral/psychiatric output**: impaired prepulse inhibition (schizophrenia-relevant), reduced social interaction (autism-relevant), repetitive grooming, impaired fear learning, elevated startle in mouse models — mapping onto the human ADHD/anxiety/ASD/psychosis spectrum (ORGANISM)

### Molecular Pathways
- Synaptic scaffolding / glutamatergic signaling (DLG1-MAGUK family) — GO:0098794 postsynapse; GO:0007626 locomotory behavior (proxy)
- Rho-family GTPase / PAK2 actin cytoskeleton signaling — GO:0007169; GO:0030036 actin cytoskeleton organization
- mRNA cap-binding complex / nuclear export (NCBP2) — GO:0000339 RNA cap binding
- Ubiquitin-proteasome/SUMOylation pathway (UBXN7, FBXO45, RNF168, SENP5) — GO:0016567 protein ubiquitination; GO:0016925 protein sumoylation
- Mitochondrial oxidative phosphorylation / energy metabolism — GO:0006119 oxidative phosphorylation

### Cellular Processes
- Neuronal migration, neurite outgrowth, dendritic spine morphogenesis (PAK2)
- Synaptic receptor trafficking (DLG1)
- DNA-damage response (RNF168 — also causal for RIDDLE syndrome)
- Cell-cycle and apoptosis regulation (implicated by NCBP2 interaction screens)

### Protein Dysfunction
Not classical misfolding/aggregation — mechanism is **gene-dosage reduction (haploinsufficiency)** across multiple interacting proteins rather than a single mutant protein's structural defect.

### Immune System Involvement
*NRROS* (negative regulator of reactive oxygen species) lies within the deletion interval and has an immune-regulatory role, but no immune/autoinflammatory phenotype has been robustly linked to 3q29Del in human cohorts to date; this remains an underexplored area.

### Molecular Profiling
- **Transcriptomics**: "Convergent and distributed effects of the 3q29 deletion on the human neural transcriptome" (*Transl Psychiatry*, 2021;11:344, PMC8206125) — profiled iPSC-derived neural models; found both convergent (multi-gene) and gene-distributed transcriptomic signatures.
- **Single-cell/cross-species**: single-cell RNA-seq of cortical organoids (2 and 12 months) and mouse isocortex identifying excitatory-neuron-specific, cross-species-concordant mitochondrial/energy-metabolism dysregulation (PMID:37585521).
- **Model-system functional screening**: systematic pairwise interaction screen of 14 3q29 gene homologs (314 pairwise combinations) in *Drosophila* and *Xenopus laevis*, identifying NCBP2 as a broad enhancer/modifier (PMID:32053595), and a follow-on "two-hit" functional model paper (PMC8049494).

### Suggested Ontology Terms
- GO (biological process): GO:0007268 chemical synaptic transmission; GO:0030182 neuron differentiation; GO:0016192 vesicle-mediated transport; GO:0006457 protein folding/quality control (proxy for ubiquitin pathway)
- CL (cell type): CL:0000679 glutamatergic neuron; CL:0000617 GABAergic interneuron (parvalbumin-positive: CL:0000846 parvalbumin GABAergic interneuron); CL:0002605 astrocyte (cortical organoid context)
- UBERON: UBERON:0002037 cerebellum; UBERON:0001950 neocortex

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary**: Central nervous system (cerebral cortex, cerebellum/posterior fossa) — UBERON:0000955 brain
- **Secondary/systemic**: Heart (UBERON:0000948), gastrointestinal tract (UBERON:0005409), eye (UBERON:0000970), skeletal system (UBERON:0001434), craniofacial skeleton (UBERON:0002516), teeth (UBERON:0003688), middle ear (UBERON:0001846)
- **Body systems involved**: Nervous, psychiatric/behavioral, cardiovascular, digestive, musculoskeletal, ophthalmologic, dental/craniofacial, otologic, genitourinary (enuresis)

### Tissue/Cell Level
- Cerebellar cortex (reduced volume) and cerebellar white matter (increased volume) — UBERON:0002129 cerebellar cortex; UBERON:0002978 cerebellar white matter
- Sensory/auditory cortex — hyperexcitability locus in mouse model
- Parvalbumin-positive GABAergic interneurons (CL:0000846) — reduced density in sensory cortex
- Excitatory (glutamatergic) cortical neurons (CL:0000679) — locus of convergent transcriptomic/mitochondrial dysregulation

### Subcellular Level
- Mitochondria (GO:0005739 cellular component) — dysregulated energy metabolism/oxidative phosphorylation
- Postsynaptic density (GO:0014069) — DLG1/MAGUK scaffold disruption
- Nucleus (nuclear cap-binding complex, NCBP2) — GO:0005849 mRNA cleavage/cap-binding complex
- Actin cytoskeleton (PAK2) — GO:0015629

### Localization
- Bilateral, generally symmetric involvement (posterior fossa cystic/hypoplastic findings, cortical volumetric changes) — no strong lateralization reported.

---

## 8. Temporal Development

### Onset
- **Congenital/prenatal**: Reduced birth weight is a recognized early feature; the CNV itself is present from conception (germline/de novo constitutional event).
- **Infancy**: Feeding difficulties, hypotonia, motor delay, failure to thrive typically present first.
- **Childhood**: Developmental delay, speech delay, ASD, ADHD, anxiety diagnoses emerge.
- **Adolescence–young adulthood**: Psychotic disorders/schizophrenia-spectrum illness onset — notably, **age at onset for psychosis/prodrome can be younger than typical population onset**, with case reports of onset in children as young as 5–10 years compared to the typical 20–25-year window (GeneReviews, NBK385289; Frontiers 2026 case report, "Early-onset psychosis as a sentinel manifestation of 3q29 deletion syndrome").

### Progression
- Neurodevelopmental features (ID, ASD, executive dysfunction) are generally **stable/lifelong** rather than progressive.
- Psychiatric features (anxiety, ADHD, psychosis) can be **episodic or progressive**, with psychosis sometimes evolving from a prodromal phase.
- GI and musculoskeletal features are largely **stable, chronic** issues managed symptomatically; scoliosis is monitored for progression.
- No degenerative/regressive natural-history pattern has been described; this is a static structural genomic lesion producing a developmental, largely non-progressive disorder trajectory at the molecular level, with psychiatric-symptom-level fluctuation.

### Patterns
- **Remission**: Psychiatric symptoms may partially remit with treatment (e.g., antipsychotics for psychosis) but treatment resistance is a recognized feature (see Treatment section).
- **Critical periods**: Early childhood is emphasized as a window for early intervention (speech/OT/PT); adolescence is emphasized as a critical surveillance window for psychosis-prodrome monitoring, particularly around stimulant initiation for ADHD.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence**: ~1:30,000 to 1:40,000, derived from two independent population-ascertainment cohorts:
  - Iceland (deCODE, Stefansson et al.): 3 of 101,655 individuals
  - UK Biobank (Kendall et al., 2017): 5 of 152,728 individuals
- No incidence (birth-rate) data separate from prevalence have been specifically published; given the largely de novo, non-lethal nature of the CNV, birth prevalence and population prevalence are expected to be similar.

### Inheritance Pattern
- **Autosomal dominant**, virtually always via a **de novo** structural mutation (~93% of tested trios de novo; ~7% inherited).
- **Penetrance**: Incomplete — apparently unaffected transmitting parents have been documented, though when comprehensively assessed some carry substantial subclinical neuropsychiatric morbidity (e.g., a reported transmitting parent with undiagnosed schizoaffective disorder, ADHD, panic disorder, social anxiety, and executive dysfunction), suggesting **ascertainment-dependent apparent penetrance** rather than true non-penetrance.
- **Expressivity**: Highly **variable**, even within families (multiplex family case report, PMID:32321479), consistent with a polygenic-background modifier model.
- **Genetic anticipation**: Not established/reported (mechanism is CNV, not repeat expansion).
- **Germline mosaicism**: Documented in at least one reported case (paternal).
- **Founder effects**: Not applicable — this is a recurrent NAHR-mediated CNV (mechanistically analogous across populations via shared LCR architecture) rather than a population-specific founder mutation.
- **Consanguinity**: Not a relevant risk factor (dominant CNV mechanism, not recessive).
- **Carrier frequency**: Equivalent to prevalence given the dominant, largely de novo mechanism (~1:30,000–1:40,000); no population-specific carrier screening data.

### Population Demographics
- No strong evidence for ethnic/geographic enrichment; cases reported across European (Icelandic, UK), North American, and other ancestries via registry/case-report literature.
- **Sex ratio**: Roughly equal for the syndrome overall (registry cohort ~58% male, reflecting general ascertainment rather than a skewed disease ratio); notably the ASD sub-phenotype shows an attenuated male excess (2:1 vs. population 4:1).
- **Age distribution**: Registry cohorts span infancy through middle adulthood (deep-phenotyping cohort ages 4.85–39.1 years; ASD-registry cohort ages 0.1–41 years), reflecting the syndrome's lifelong, non-lethal natural history.

---

## 10. Diagnostics

### First-Line Genetic Test
- **Chromosomal microarray analysis (CMA)** (oligonucleotide- or SNP-array-based) — first-tier test, ~100% sensitivity for the canonical deletion in the proband; standard of care per GeneReviews.
- Routine G-banded karyotype **cannot** detect this microdeletion.

### Confirmatory / Family Testing
- FISH (fluorescence in situ hybridization)
- Quantitative PCR (qPCR)
- Multiplex ligation-dependent probe amplification (MLPA)
— used to confirm the deletion in the proband and to test parents/relatives for inheritance status and recurrence-risk counseling.

### Additional Recommended Work-Up After Diagnosis (per GeneReviews management guidelines)
- Developmental/neuropsychological evaluation (cognitive ability, ASD screening, executive function) — gold-standard instruments as used in registry studies (e.g., ADOS-2, cognitive batteries)
- Psychiatric evaluation for ADHD, anxiety, and **prodromal psychosis screening**
- Brain MRI (posterior fossa/cerebellum evaluation)
- Ophthalmology examination (strabismus, refractive error)
- Dental evaluation
- Echocardiography (congenital heart disease screening)
- Audiology/otolaryngology assessment
- Skeletal (scoliosis) screening

### Clinical Criteria / Differential Diagnosis
No syndrome-specific clinical diagnostic criteria exist independent of the molecular deletion — diagnosis is definitionally genetic (CMA-confirmed 1.6 Mb 3q29 deletion). The clinical differential is broad given the nonspecific combination of developmental delay, learning problems, and neuropsychiatric disorders, overlapping with other genomic disorders (22q11.2DS, 16p11.2, 1q21.1, idiopathic ASD/ID) — CMA is diagnostic and discriminating.

### Screening
No population-based newborn or carrier screening program exists for 3q29Del (it is not part of standard NBS panels, being a structural CNV rather than a metabolic/biochemical target). Prenatal detection occurs incidentally via CMA performed for other indications (e.g., abnormal ultrasound, advanced maternal age) or genome-wide NIPT/prenatal microarray.

### Suggested LOINC/Test Concepts
- Chromosomal microarray analysis — LOINC concepts for cytogenomic (SNP) array
- FISH analysis
- Echocardiogram (structural heart evaluation)
- Brain MRI (posterior fossa protocol)

---

## 11. Outcome / Prognosis

### Survival and Mortality
No elevated mortality rate specific to 3q29Del has been reported in the literature; life expectancy is not documented as reduced, and the condition is not associated with a lethal natural history. Serious cardiac malformations (25% of cases) may carry surgical/perioperative risk in the most severe subset, but no syndrome-wide mortality statistics have been published.

### Morbidity and Function
- Substantial cumulative morbidity from the combination of **intellectual disability (34%)**, **ASD (29–38%)**, **ADHD (63%)**, **anxiety (40%)**, and **psychotic disorder (19–20%)**, plus chronic GI symptoms (81%) and musculoskeletal findings (84%).
- **Distinct cognitive profile** (verbal strength relative to nonverbal ability) can mask underlying deficits and complicate school/vocational planning.
- Quality-of-life burden is not yet quantified with standardized instruments (EQ-5D/SF-36) in a syndrome-specific study; qualitative registry/caregiver data emphasize functional impact from executive dysfunction and psychiatric comorbidity.

### Complications
- Psychosis, when it occurs, appears **particularly treatment-resistant** — a recognized clinical vulnerability (see Treatment).
- Feeding/GI complications can necessitate gastrostomy-tube support in severe infantile presentations.
- Scoliosis and other musculoskeletal complications require ongoing orthopedic monitoring.

### Recovery / Disease Course
- Neurodevelopmental impairments are lifelong (non-regressive); developmental/educational interventions can improve functional trajectory but do not "cure" the underlying deficits.
- Psychiatric symptoms are managed but not curatively resolved; some individuals achieve good symptom control with combination pharmacotherapy.

### Prognostic Factors
- Presence/severity of congenital heart disease and degree of intellectual disability are the most clinically apparent prognostic modifiers of early-life morbidity.
- Polygenic background burden is an emerging, quantifiable modifier of overall phenotypic severity (Oetjens et al. 2019) but is not yet a clinical prognostic tool.
- No validated molecular biomarker currently predicts psychosis conversion risk within 3q29Del carriers (an active area of the field, analogous to 22q11.2DS psychosis-risk biomarker research).

---

## 12. Treatment

There is **no disease-modifying or curative treatment** for 3q29Del; management is entirely **symptomatic, multidisciplinary, and surveillance-based**, following the GeneReviews consensus management recommendations.

### Pharmacotherapy
- **ADHD**: Cautious use of stimulants, with explicit monitoring for emerging/exacerbated psychotic symptoms; non-stimulant alternatives (e.g., **bupropion**, **atomoxetine**) are suggested as potentially lower-risk options relative to amphetamines/methylphenidate given the elevated psychosis risk in this population.
  - Suggested NCIT: `NCIT:C15986` Pharmacotherapy; therapeutic_agent candidates — atomoxetine (CHEBI), bupropion (CHEBI)
- **Anxiety**: Standard anxiolytic pharmacotherapy plus cognitive behavioral therapy (see Behavioral, below).
- **Antipsychotics for psychosis**: **Risperidone** has documented use, with variable efficacy and a notable adverse-effect burden (excessive daytime sedation) limiting maintenance dosing; combination therapy (e.g., **lurasidone + olanzapine**) has achieved sustained stabilization in reported cases without escalation to clozapine [Karger *Neuropsychobiology*, 2026, "Response to Treatment in 3q29 Deletion Syndrome-Associated Psychosis: A Mini-Review"]. **Clozapine** is recommended as the treatment of choice when other antipsychotic trials fail, reflecting a described vulnerability to **treatment-resistant psychosis** in this population.
  - Suggested NCIT therapeutic_agent terms: risperidone (`NCIT:C29127`), clozapine, olanzapine, lurasidone
- **Seizures**: Standard antiepileptic management; seizures in 3q29Del are generally described as mild and treatment-responsive.

### Surgical / Interventional
- Cardiac surgical repair as indicated by specific structural lesion (e.g., PDA closure, VSD repair) — `NCIT:C15329` Surgical Procedure
- Gastrostomy tube placement for severe feeding/failure-to-thrive presentations
- Orthopedic surgical intervention for progressive scoliosis when indicated — `NCIT:C16186` Orthopedic Surgical Procedure

### Supportive / Rehabilitative
- Early speech-language therapy — `NCIT:C159273`
- Physical and occupational therapy — `NCIT:C15302`; `NCIT:C121351`
- Individualized Education Programs (IEP) / special education services
- Feeding therapy
- Applied Behavior Analysis (ABA) for ASD-related behaviors
- Cognitive Behavioral Therapy (CBT) for anxiety and social disability — `NCIT:C181743` behavioral counseling (proxy)

### Genetic Counseling
- Recommended for all newly diagnosed families given the largely de novo but non-zero recurrence risk and variable expressivity — `NCIT:C15240` Genetic Counseling

### Experimental / Research-Stage
- No gene therapy, RNA-based therapy, or targeted molecular therapy currently exists or is in clinical trials for 3q29Del specifically. Mechanistic research (mitochondrial dysfunction, E/I imbalance, ubiquitination pathway) is at the preclinical/model-organism stage and has not yet yielded a therapeutic candidate beyond repurposed psychiatric medications.
- The mouse model responsiveness to **risperidone** in normalizing startle/PPI deficits provided early translational rationale for antipsychotic use in this population [Baba et al., *Neuropsychopharmacology*, 2019, PMID:31216562], though clinical response in humans has proven more variable/resistant than the preclinical data alone would predict.

### Treatment Strategy
Care follows a **surveillance-and-symptom-management algorithm**: baseline multidisciplinary evaluation at diagnosis (developmental, psychiatric, cardiac, ophthalmologic, dental, neuroimaging) → tailored early intervention → longitudinal surveillance (annual neuropsychiatric assessment and scoliosis screening; twice-yearly dental exams; annual ophthalmology) with explicit attention to psychosis-prodrome monitoring through adolescence, particularly around any stimulant initiation.

---

## 13. Prevention

### Primary Prevention
No primary prevention exists for the de novo NAHR-mediated deletion event itself; there is no known modifiable risk factor to reduce occurrence.

### Secondary Prevention (Early Detection)
- **Prenatal diagnosis**: possible via chromosomal microarray or genome-wide NIPT if performed for other indications; not part of a standard universal prenatal screening panel.
- **Preimplantation genetic testing (PGT)**: an option for known carrier parents (the ~7% inherited-case subset) pursuing future pregnancies, analogous to other recurrent CNV syndromes.
- **Early postnatal recognition**: prompt CMA testing in infants presenting with feeding difficulty, hypotonia, developmental delay, or congenital heart disease enables earlier initiation of surveillance and intervention.

### Tertiary Prevention (Preventing Complications)
- Structured surveillance protocol (as above) is explicitly designed to catch and mitigate complications early — e.g., early psychosis-prodrome identification to enable earlier intervention, scoliosis screening to catch progressive curvature, and cautious ADHD-medication selection to reduce psychosis-precipitation risk.

### Genetic Counseling / Family Planning
- Central preventive tool for this syndrome: parental testing after a proband diagnosis to establish de novo vs. inherited status, recurrence-risk counseling (50% for a carrier parent; low but non-zero for simplex families due to possible germline mosaicism), and discussion of prenatal/preimplantation testing options for future pregnancies — `NCIT:C15240`.

### Public Health / Behavioral / Screening Programs
Not applicable at a population level — this is a rare, largely non-preventable de novo genomic disorder without an identified environmental trigger, so public-health-level primary prevention strategies (vaccination, exposure reduction) do not apply.

---

## 14. Other Species / Natural Disease

3q29 microdeletion syndrome, as a human-specific recurrent CNV defined by human-specific LCR architecture at a human chromosomal locus, has **no documented naturally-occurring veterinary/companion-animal counterpart** (unlike some single-gene Mendelian disorders with OMIA-catalogued naturally occurring animal analogs). All animal data derive from **engineered models**, not spontaneous disease (see Model Organisms, below).

- **Taxonomy**: Human-specific structural locus; NCBITaxon:9606 (Homo sapiens)
- **Orthologous genes**: Mouse orthologs of the human 3q29 interval map to a syntenic region on mouse chromosome 16, bounded by *Bdh1* and *Tfrc* — the region used to engineer the mouse deletion model.
- No comparative/evolutionary conservation analysis beyond the syntenic mapping used for model construction has been reported.
- **Zoonotic/transmission relevance**: Not applicable (non-infectious, structural genomic disorder).

---

## 15. Model Organisms

3q29Del is one of the more extensively modeled recurrent CNVs across three complementary experimental systems — mouse, *Drosophila*/*Xenopus*, and human iPSC-derived cortical organoids — reflecting active mechanistic research given its status as a top-tier schizophrenia risk locus.

### Mouse Models
1. **Baba et al., *Neuropsychopharmacology*, 2019;44(12):2125–2135 (PMID:31216562)** — heterozygous deletion (Df/+) of the syntenic *Bdh1–Tfrc* interval on mouse chromosome 16 (~1.3 Mb, ~22–24 genes). Recapitulates: impaired prepulse inhibition (schizophrenia-relevant), reduced social interaction (autism-relevant), increased repetitive self-grooming, impaired fear-based learning, elevated acoustic startle. Whole-brain imaging (FAST technology) revealed cortical hyperactivity concentrated in auditory cortex with elevated immediate-early genes and **decreased parvalbumin-positive interneuron density**, implicating excitatory/inhibitory imbalance. **Risperidone rescued** the startle/PPI deficits — evidence for translational (pharmacological) validity.
   - Relationship: RECAPITULATES core psychiatric-relevant behavioral domains; fidelity MODERATE-HIGH for schizophrenia/autism-relevant endophenotypes.
   - Limitation: Mouse deletion spans a slightly larger/non-identical gene set than the canonical human LCR-flanked interval; not all human phenotypes (e.g., GI, cardiac) are modeled.

2. **CRISPR-engineered mouse model** — Rutkowski et al./Molecular Psychiatry, 2019 (PMID:30976085) — independently engineered heterozygous deletion of the syntenic interval via CRISPR/Cas9. Recapitulates **reduced body weight** (paralleling human failure-to-thrive/reduced birth weight), plus behavioral impairments in social interaction, cognition, acoustic startle, and amphetamine sensitivity.
   - Relationship: RECAPITULATES growth-deficit and multi-domain behavioral phenotype; fidelity MODERATE.

### Invertebrate / Amphibian Models
3. **NCBP2 modulates neurodevelopmental defects of the 3q29 deletion in *Drosophila* and *Xenopus laevis* models** — Rump et al./PMC (PLOS Genetics, 2020;16(2):e1008590, PMID:32053595). Systematically tested 14 individual fly/frog homologs of 3q29 genes and 314 pairwise gene-gene interactions for neuronal, cellular, and developmental phenotypes. **NCBP2** emerged as a broad genetic **enhancer/modifier**, exacerbating the developmental phenotypes driven by other 3q29 homologs and disrupting apoptosis and cell-cycle pathways.
   - Relationship: PERTURBS individual and combinatorial gene function; establishes the oligogenic/two-hit model for the locus.
   - Follow-on: "Functional assessment of the 'two-hit' model for neurodevelopmental defects in *Drosophila* and *X. laevis*" (PMC8049494) directly tests combinatorial (two-gene) haploinsufficiency phenotypes.
   - Limitation: Invertebrate/amphibian systems necessarily diverge substantially from human neurodevelopmental and psychiatric circuitry — useful for high-throughput gene-gene interaction screening rather than direct behavioral phenocopy.

### Human Cellular Models
4. **iPSC-derived cortical organoids** — used in "Convergent and distributed effects of the 3q29 deletion on the human neural transcriptome" (*Transl Psychiatry*, 2021;11:344) and the cross-species mitochondrial-dysregulation study (Purcell/Sefik et al., *Sci Adv*, 2023;9(33):eadh0558, PMID:37585521). Single-cell RNA-seq of isogenic cortical organoids (2 and 12 months) alongside mouse isocortex identified **176 concordantly differentially-expressed genes in excitatory neurons** across species, converging on **mitochondrial function and energy metabolism**, with functional assays confirming reduced metabolic flexibility and implicating *PAK2* as a contributor.
   - Relationship: RECAPITULATES transcriptomic/metabolic dysregulation at the cellular level in a genetically human, isogenic system; fidelity HIGH for molecular convergence, though behavioral/circuit-level correlates cannot be assessed in vitro.
   - This is the most human-proximal model system currently available and is central to current mechanistic hypotheses (mitochondrial dysfunction as a convergent node).

### Model Resources
No dedicated 3q29Del strain is yet cataloged in IMPC/KOMP as a validated multi-gene deletion allele (the model lines described above are investigator-generated, not centrally banked); individual single-gene knockout alleles for *Dlg1*, *Pak2*, etc., are available through MGI/IMSR but explicitly **do not** recapitulate the full syndrome, reinforcing the combinatorial/oligogenic model.

---

## Summary of Suggested Ontology Term Bindings for KB Curation

| Category | Suggested term |
|---|---|
| Disease | MONDO:0012269 (chromosome 3q29 microdeletion syndrome); OMIM:609425 |
| Causal genes | hgnc:2905 (DLG1), hgnc:8591 (PAK2), hgnc:7647 (NCBP2), hgnc:20620 (RNF168), hgnc:24129 (FBXO45), hgnc:29076 (UBXN7), hgnc:20351 (SENP5) |
| Key phenotypes (HP) | HP:0001263 (global developmental delay), HP:0001256 (mild ID), HP:0000729 (autistic behavior), HP:0007018 (ADHD), HP:0000739 (anxiety), HP:0000709 (psychosis), HP:0002020 (GERD), HP:0002019 (constipation), HP:0001508 (failure to thrive), HP:0001321 (cerebellar hypoplasia), HP:0002571 (retrocerebellar cyst), HP:0001631/HP:0001643 (cardiac defects), HP:0000486 (strabismus) |
| GO biological processes | GO:0007268 (chemical synaptic transmission), GO:0030036 (actin cytoskeleton organization), GO:0016567 (protein ubiquitination), GO:0006119 (oxidative phosphorylation) |
| CL cell types | CL:0000679 (glutamatergic neuron), CL:0000846 (parvalbumin GABAergic interneuron) |
| UBERON | UBERON:0002037 (cerebellum), UBERON:0001950 (neocortex), UBERON:0000948 (heart) |
| NCIT treatments | NCIT:C15986 (Pharmacotherapy), NCIT:C15302 (Physical Therapy), NCIT:C15240 (Genetic Counseling), NCIT:C15329 (Surgical Procedure) |

---

## Key Primary Citations (PMID-referenced)

1. Willatt L, et al. "3q29 microdeletion syndrome: clinical and molecular characterization of a new syndrome." *Am J Hum Genet*. 2005;77(1):154–160. PMID:15918153
2. Mulle JG, et al. "Microdeletions of 3q29 confer high risk for schizophrenia." *Am J Hum Genet*. 2010;87(2):229–236. PMID:20691406
3. Mulle JG. "The 3q29 deletion confers >40-fold increase in risk for schizophrenia." *Mol Psychiatry*. 2015;20:1028–1029. PMID:26055425
4. Sanchez Russo R, et al. "Deep phenotyping in 3q29 deletion syndrome: recommendations for clinical care." *Genet Med*. 2021;23(5):872–880. PMID:33564151
5. Pollak RM, et al. "Neuropsychiatric phenotypes and a distinct constellation of ASD features in 3q29 deletion syndrome: results from the 3q29 registry." *Mol Autism*. 2019;10:30. PMID:31346402
6. Rump P, et al. "NCBP2 modulates neurodevelopmental defects of the 3q29 deletion in Drosophila and Xenopus laevis models." *PLoS Genet*. 2020;16(2):e1008590. PMID:32053595
7. Baba M, et al. "Psychiatric-disorder-related behavioral phenotypes and cortical hyperactivity in a mouse model of 3q29 deletion syndrome." *Neuropsychopharmacology*. 2019;44(12):2125–2135. PMID:31216562
8. Rutkowski TP, et al. "Behavioral changes and growth deficits in a CRISPR engineered mouse model of the schizophrenia-associated 3q29 deletion." *Mol Psychiatry*. 2019. PMID:30976085
9. Purcell RH, Sefik E, et al. "Cross-species analysis identifies mitochondrial dysregulation as a functional consequence of the schizophrenia-associated 3q29 deletion." *Sci Adv*. 2023;9(33):eadh0558. PMID:37585521
10. Oetjens MT, et al. "Quantifying the polygenic contribution to variable expressivity in eleven rare genetic disorders." *Nat Commun*. 2019;10:4897.
11. Klaiman C, et al. "A distinct cognitive profile in individuals with 3q29 deletion syndrome." *J Intellect Disabil Res*. 2023. PMID:35297118
12. Sanders A, et al. "Structural deviations of the posterior fossa and the cerebellum and their cognitive links in a neurodevelopmental deletion syndrome." *Mol Psychiatry*. 2024. PMID:38744992
13. "Driver or passenger? A new assessment of genes in the schizophrenia-associated 3q29 deletion locus for contribution to neurodevelopmental disorders." *J Neurodevelopmental Disord*. 2026;18. (PMID pending indexing at time of report)
14. "Response to Treatment in 3q29 Deletion Syndrome-Associated Psychosis: A Mini-Review." *Neuropsychobiology*. 2026;82(5):263. (Karger)

---

**Note on data gaps**: No syndrome-specific standardized QoL instrument data, no confirmed epigenetic/methylation signature, no naturally-occurring veterinary analog, and no disease-modifying/targeted therapy currently exist in the published literature — these should be flagged as `NOT_AVAILABLE`/absent rather than inferred in any downstream knowledge base entry.

Sources:
- [chromosome 3q29 microdeletion syndrome - NORD](https://rarediseases.org/mondo-disease/chromosome-3q29-microdeletion-syndrome/)
- [3q29 Recurrent Deletion - GeneReviews®](https://www.ncbi.nlm.nih.gov/books/NBK385289/)
- [OMIM #609425](https://www.omim.org/entry/609425)
- [OMIM #611936](https://omim.org/entry/611936)
- [Monarch Initiative MONDO:0012269](https://monarchinitiative.org/MONDO:0012269)
- [Willatt et al. 2005, PubMed](https://pubmed.ncbi.nlm.nih.gov/15918153/)
- [Mulle et al. 2010, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2917706/)
- [The 3q29 deletion confers >40-fold increase in risk for schizophrenia, Molecular Psychiatry](https://www.nature.com/articles/mp201576)
- [Deep phenotyping in 3q29 deletion syndrome, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8105170/)
- [Neuropsychiatric phenotypes and ASD features, 3q29 registry, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6636128/)
- [Psychiatric-disorder-related behavioral phenotypes and cortical hyperactivity in a mouse model, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6887869/)
- [Behavioral changes and growth deficits in a CRISPR engineered mouse model, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6788962/)
- [NCBP2 modulates neurodevelopmental defects, PLOS Genetics](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1008590)
- [Structural deviations of the posterior fossa and cerebellum, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11541222/)
- [Cross-species analysis identifies mitochondrial dysregulation, Science Advances](https://www.science.org/doi/10.1126/sciadv.adh0558)
- [Driver or passenger? A new assessment of genes in the 3q29 locus, J Neurodevelopmental Disorders](https://link.springer.com/article/10.1186/s11689-026-09696-y)
- [A distinct cognitive profile in individuals with 3q29 deletion syndrome, medRxiv](https://www.medrxiv.org/content/10.1101/2021.03.05.21252967v1.full)
- [Response to Treatment in 3q29 Deletion Syndrome-Associated Psychosis, Karger](https://karger.com/nps/article/82/5/263/861380/Response-to-Treatment-in-3q29-Deletion-Syndrome)
- [Early-onset psychosis as a sentinel manifestation of 3q29 deletion syndrome, Frontiers](https://www.frontiersin.org/journals/child-and-adolescent-psychiatry/articles/10.3389/frcha.2026.1823061/full)
- [3q29 Recurrent Deletion Table B, GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK385289/table/mdel3q29.molgen.TB/)
- [About Us, 3q29 Project, Emory](https://genome.emory.edu/3q29/about-us/)
- [Study protocol for The Emory 3q29 Project, PubMed](https://pubmed.ncbi.nlm.nih.gov/29884173/)
- [Phenotype Heterogeneity in 3q29 Microduplication Syndrome, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7445637/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |

All extracted references resolved successfully.