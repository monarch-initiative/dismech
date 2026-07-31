---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-29T22:12:22.455913'
end_time: '2026-07-29T22:17:20.610025'
duration_seconds: 298.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bulimia Nervosa
  mondo_id: ''
  category: Psychiatric
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
  web_search_requests: 22
  num_turns: 26
  total_cost_usd: 1.7670860000000004
  session_id: 574ce21a-bc93-5c7c-a2f0-f74643218baf
  stop_reason: end_turn
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bulimia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Bulimia Nervosa** covering all of the
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

# Bulimia Nervosa — Comprehensive Research Report

## 1. Disease Information

**Overview.** Bulimia nervosa (BN) is a psychiatric eating disorder characterized by recurrent episodes of binge eating (rapid consumption of an objectively large amount of food accompanied by a subjective sense of loss of control) followed by inappropriate compensatory behaviors intended to prevent weight gain — most commonly self-induced vomiting, but also laxative/diuretic/enema misuse, fasting, or excessive/compulsive exercise. Self-evaluation is disproportionately influenced by body shape and weight. Unlike anorexia nervosa, body weight in BN is typically within or above the normal range, which contributes to underrecognition ([MRCPsych UK, ICD-11 criteria](https://www.mrcpsych.uk/2022/05/icd-11-criteria-for-bulimia-nervosa-6b81.html); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK562178/)).

**Key identifiers:**
- **MONDO:** `MONDO:0005452` (bulimia nervosa) — confirmed via OLS/Monarch query (EBI OLS4 API, 2026-07-29 query)
- **OMIM:** `607499` — "BULIMIA NERVOSA, SUSCEPTIBILITY TO; BULN" (a susceptibility locus entry, not a monogenic disorder) ([OMIM:607499](https://omim.org/entry/607499))
- **DOID:** `DOID:12129`
- **ICD-10-CM:** `F50.2` (Bulimia nervosa); ICD-11: `6B81`
- **ICD-11 diagnostic code:** `6B81`
- **EFO:** `EFO_0005204`
- **HPO:** `HP:0100739` "Bulimia" (synonym: "Binge and purge") — confirmed via OLS4 API query
- **MeSH:** `D002032` (Bulimia Nervosa)

**Synonyms:** Bulimia, binge-purge syndrome, bulimarexia (historical, now discouraged).

**Evidence base:** Predominantly aggregated disease-level literature (case series, clinical cohorts, epidemiological registries, twin/family studies, GWAS meta-analyses, RCTs). Individual-patient EHR-level data exist but are less centralized than for BED/AN; national inpatient databases (e.g., US Nationwide Inpatient Sample) provide some individual-level aggregated statistics ([PMC6034764](https://pmc.ncbi.nlm.nih.gov/articles/PMC6034764/)).

Sources: [ICD-11 Criteria (MRCPsych)](https://www.mrcpsych.uk/2022/05/icd-11-criteria-for-bulimia-nervosa-6b81.html), [StatPearls: Bulimia Nervosa](https://www.ncbi.nlm.nih.gov/books/NBK562178/), [OMIM:607499](https://omim.org/entry/607499)

---

## 2. Etiology

**Disease causal model:** BN is multifactorial/polygenic — no single causal gene; risk arises from an interaction of genetic vulnerability (heritability ~50–60%), neurobiological reward/impulse-control dysregulation, and environmental/psychosocial exposures (sociocultural thin-ideal internalization, dieting, trauma).

### Genetic risk factors
- **Heritability:** Twin studies estimate BN heritability at ~50–60% (one classic study: heritability of liability 55%; a subsequent twin study ~41%; proband-wise concordance 22.9% MZ vs. 8.7% DZ twins) ([PubMed:1842216](https://pubmed.ncbi.nlm.nih.gov/1842216/) — Kendler et al., "The genetic epidemiology of bulimia nervosa").
- **Genetic correlation with anorexia nervosa:** rg 0.46–0.79, indicating substantial shared genetic architecture between AN and BN ([Nature Transl Psychiatry, 2023](https://www.nature.com/articles/s41398-023-02585-1)).
- **GWAS:** The Psychiatric Genomics Consortium – Eating Disorders (PGC-ED) is actively collecting BN samples; a 2025 GWAS of binge-eating behavior and anorexia nervosa found shared and unique genetic architecture across ED phenotypes (medRxiv 2025.01.31.25321397). A dedicated, well-powered BN-specific GWAS with genome-wide-significant loci has not yet been published (as of 2026), in contrast to AN (first genome-wide-significant locus reported in Watson et al. 2019, chr12).
- **Candidate gene studies (largely underpowered/candidate-gene era, mixed replication):**
  - **5-HTTLPR** (serotonin transporter promoter polymorphism, *SLC6A4*/`hgnc:11050`): implicated in reward processing, impulsivity, and eating-disorder susceptibility in meta-analyses; effects reported are inconsistent across studies.
  - **BDNF Val66Met** (rs6265, `hgnc:1033`): studied primarily in AN; not robustly associated in BN-specific analyses.
  - **OPRD1** (delta-opioid receptor) and **HTR1D**: association signals reported with eating-disorder susceptibility (primarily AN datasets, with BN comorbid samples).
  - **ESR1/ESR2** (estrogen receptor genes): implicated given menstrual-cycle-linked binge-eating fluctuations.
- **Note on evidence quality:** Most single-candidate-gene associations in BN come from small case-control samples and have not been replicated in well-powered GWAS; treat as `evidence_source: HUMAN_CLINICAL` with low confidence pending GWAS confirmation.

### Environmental / psychosocial risk factors
- **Sociocultural pressure/thin-ideal internalization** and **dieting behavior** are established proximal risk factors — strict caloric restriction predisposes to disinhibited binge eating ([PMC2907970](https://pmc.ncbi.nlm.nih.gov/articles/PMC2907970/)).
- **Childhood sexual abuse and maltreatment:** Childhood sexual abuse is a replicated non-specific risk factor for BN (elevated risk vs. no-ED controls, though not specific to BN vs. other psychiatric disorders) ([PubMed, Am J Psychiatry 1992](https://psychiatryonline.org/doi/abs/10.1176/ajp.149.4.455); [ScienceDirect 1993](https://www.sciencedirect.com/science/article/abs/pii/014521349390050F)).
- **Adverse childhood experiences (ACEs):** emotional, physical, and sexual abuse and emotional neglect show a dose-dependent relationship with eating-disorder symptom severity, including in BN ([Frontiers 2022](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1063693/full); [PMC8860810](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8860810/)).
- **Perfectionism** (particularly self-oriented perfectionism) and **low self-esteem/body dissatisfaction** are robust psychological risk factors.
- **Sex:** female sex is the strongest demographic risk factor (see §9).
- **Family history** of eating disorders, depression, substance use, or obesity.
- **Weight stigma / weight-based teasing** and **participation in weight-class or appearance-focused activities** (dance, gymnastics, modeling).

### Protective factors
- Limited high-quality literature specifically on protective genetic variants. Environmentally, protective factors include: family meal structure/cohesion, media-literacy interventions, and body-acceptance-based prevention programs (see §13). No confirmed protective allele has reached genome-wide significance specifically for BN.

### Gene-environment interaction
- The interaction of genetic loading (reward/impulsivity circuitry variants) with dieting/restriction as an environmental trigger is the dominant conceptual G×E model — caloric restriction unmasks binge-eating vulnerability in genetically susceptible individuals, consistent with rodent binge-eating-prone (BEP) vs binge-eating-resistant (BER) models responding differentially to identical intermittent palatable-food-access protocols ([PMC3132131](https://pmc.ncbi.nlm.nih.gov/articles/PMC3132131/)).

Sources: [Kendler et al. PMID:1842216](https://pubmed.ncbi.nlm.nih.gov/1842216/), [Nature Transl Psychiatry 2023](https://www.nature.com/articles/s41398-023-02585-1), [PMC2907970](https://pmc.ncbi.nlm.nih.gov/articles/PMC2907970/), [Frontiers 2022 ACEs](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1063693/full)

---

## 3. Phenotypes

| Phenotype | Type | Onset/Course | Frequency | Suggested HP term |
|---|---|---|---|---|
| Recurrent binge-eating episodes | Behavioral | Core criterion; episodic | ~100% (defining) | `HP:0100739` Bulimia |
| Self-induced vomiting (purging) | Behavioral | Chronic/recurrent | Most common compensatory behavior (~80-90% of BN-purging type) | (behavioral; no dedicated HP term — capture via `notes`/definitions) |
| Laxative/diuretic misuse | Behavioral | Recurrent | Subset (~10-60% depending on cohort; nonpurging vs purging subtype) | — |
| Dental erosion (perimyolysis) | Physical/clinical sign | Chronic, progressive with purging duration | Common in chronic purgers | `HP:0006486` Abnormal dental enamel morphology (general fit); tooth erosion has no exact-match HP term |
| Parotid/salivary gland enlargement ("chipmunk facies") | Physical sign | 3–4 days post-vomiting cessation; recurs with purging | ~36% enlargement vs controls | `HP:0100730` Sialadenitis (imperfect fit) / general parotid enlargement |
| Russell's sign (knuckle calluses from self-induced vomiting) | Physical sign | Chronic | Uncommon (many use utensils, not fingers) | — (no specific HP term; document narratively) |
| Hypokalemia | Laboratory abnormality | Acute-on-chronic with purging | ~13.7% of BN samples | `HP:0002900` Hypokalemia |
| Metabolic (hypochloremic) alkalosis | Laboratory abnormality | Recurrent with vomiting | ~27.4% (most common lab abnormality) | `HP:0001941` Metabolic alkalosis; `HP:0003111` Hypochloremia |
| Elevated serum amylase | Laboratory abnormality | Correlates with binge/purge frequency | Common | `HP:0040217` Hyperamylasemia (verify exact term) |
| Esophagitis / Mallory-Weiss tear | Clinical/GI | Acute, recurrent-vomiting-associated | Rare-moderate | `HP:0002037` Gastrointestinal hemorrhage (proxy) |
| Esophageal rupture (Boerhaave syndrome) | Clinical/GI, rare severe | Acute, life-threatening | Rare | — |
| QTc prolongation / cardiac arrhythmia | Clinical sign | Acute, hypokalemia-driven | Present in severe electrolyte disturbance | `HP:0001657` Long QT syndrome (proxy); `HP:0011675` Arrhythmia |
| Amenorrhea/menstrual irregularity | Physical/endocrine | Variable | Reported subset (less universal than in AN) | `HP:0000141` Amenorrhea |
| Depressed mood | Behavioral/psychiatric | Often co-occurring, can precede or follow BN onset | ~50-75% (comorbid MDD) | `HP:0000716` Depressivity |
| Anxiety symptoms | Behavioral/psychiatric | Often precedes BN onset | ~36% any anxiety disorder | `HP:0000739` Anxiety |
| Impulsivity | Behavioral | Trait-like, associated with poorer prognosis | Variable | `HP:0100710` Impulsivity |
| Body image distortion/overvaluation of shape and weight | Behavioral/cognitive | Core, persistent | ~100% (defining) | — (no dedicated HP term; core diagnostic construct) |

**Onset:** Typically late adolescence to early adulthood (median onset ~18–21 years); can follow a period of dietary restriction or, less commonly, transition from anorexia nervosa (AN-restricting → BN crossover reported in a subset of AN patients) ([PMC2275291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2275291/)).

**Severity (DSM-5)** is graded by weekly frequency of inappropriate compensatory behaviors:
- Mild: 1–3 episodes/week
- Moderate: 4–7 episodes/week
- Severe: 8–13 episodes/week
- Extreme: ≥14 episodes/week

**Course:** Episodic/fluctuating with a tendency toward chronicity if untreated; partial and full remission specifiers apply (see §8, §11).

**Quality of life impact:** Significant impairment in psychosocial functioning, social withdrawal (due to secrecy around bingeing/purging), impaired occupational/educational functioning, and elevated suicide risk associated with comorbid depression.

Sources: [Cleveland Clinic J Med](https://www.ccjm.org/content/88/6/333), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK562178/), [ScienceDirect salivary gland](https://www.sciencedirect.com/science/article/abs/pii/S0006322398002212), [PMC2275291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2275291/)

---

## 4. Genetic / Molecular Information

- **Causal genes:** None establish a monogenic cause; BN is polygenic/multifactorial (OMIM `607499` is explicitly a "susceptibility" entry, not a Mendelian disease locus).
- **Pathogenic variants:** Not applicable in the classical Mendelian sense. No ClinVar pathogenic/likely-pathogenic variant classifications exist for BN as a discrete monogenic trait.
- **Susceptibility loci / candidate genes** (see §2 for detail): *SLC6A4* (5-HTTLPR), *BDNF* (Val66Met/rs6265), *OPRD1*, *HTR1D*, *ESR1*/*ESR2* — candidate-gene-era findings, generally not replicated at genome-wide significance.
- **Polygenic architecture:** Significant genetic correlation with anorexia nervosa (rg 0.46–0.79) and likely with major depression, anxiety disorders, OCD, and impulsivity/ADHD traits, consistent with the high psychiatric comorbidity burden (§9 below; [Nature Transl Psychiatry 2023](https://www.nature.com/articles/s41398-023-02585-1)).
- **Epigenetics:** Limited direct BN-specific data; eating-disorder epigenetics literature (largely AN-focused) has examined DNA methylation changes in genes related to appetite regulation (e.g., *POMC*, *AGRP*) but BN-specific methylation studies are sparse and not yet conclusive.
- **Chromosomal abnormalities:** None established as causal for BN.
- **Modifier genes:** Not well characterized specifically for BN; impulsivity- and reward-related gene variants may modify symptom severity/course but data are preliminary.

Suggested gene terms if annotating candidate associations (low-confidence, candidate-gene-era evidence — flag accordingly): `hgnc:11050` (SLC6A4), `hgnc:1033` (BDNF), `hgnc:8156` (OPRD1), `hgnc:3444` (ESR1).

Sources: [OMIM:607499](https://omim.org/entry/607499), [Nature Transl Psychiatry 2023](https://www.nature.com/articles/s41398-023-02585-1), [Frontiers 2024 AN polymorphisms](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1386233/full)

---

## 5. Environmental Information

- **Sociocultural exposures:** Media/thin-ideal internalization, social-media use (a Lebanese university-student study found problematic social media use associated with BN symptoms mediated by anxiety/depression — [PMC10052263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10052263/)), weight stigma, appearance-focused athletic/artistic activities.
- **Lifestyle factors:** Chronic dieting/caloric restriction is the most consistently identified proximal behavioral trigger; alcohol/substance use frequently co-occurs and may share impulsivity-driven risk pathways.
- **Life stress/trauma:** Childhood abuse/neglect (§2), interpersonal stressors, and transitions (e.g., leaving home, athletic competition pressure).
- **Infectious agents:** Not applicable — BN has no known infectious etiology.

Sources: [PMC10052263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10052263/), [NEDA Risk Factors](https://www.nationaleatingdisorders.org/risk-factors/)

---

## 6. Mechanism / Pathophysiology

BN pathophysiology is best modeled as a **reward-circuitry and homeostatic-appetite-signaling dysregulation cascade**, upstream of the behavioral binge-purge cycle, with secondary systemic/metabolic consequences downstream of purging behaviors.

### Causal chain (upstream → downstream)
1. **Trigger:** Caloric restriction/dieting (behavioral) and/or genetic predisposition (reward/impulsivity circuitry variants) → 
2. **Gut-hormone/appetite-signaling dysregulation:** Impaired meal-induced ghrelin suppression, blunted postprandial cholecystokinin (CCK) rise, and lower postprandial leptin — collectively reducing satiety signaling and promoting continued/disinhibited intake ([PMC3782835](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3782835/); ResearchGate ghrelin/leptin study) →
3. **Mesolimbic reward-circuit hyperresponsivity:** Altered dopamine D1/D2 receptor balance and interaction with serotonergic (mood/anxiety) systems in ventral striatum, orbitofrontal cortex; corticostriatal circuitry changes parallel those seen in substance-use disorders ([ScienceDirect reward dysregulation](https://www.sciencedirect.com/science/article/abs/pii/S0028390811004898); [PMC3366171](https://pmc.ncbi.nlm.nih.gov/articles/PMC3366171/)) →
4. **Impaired top-down inhibitory control:** Altered functional connectivity between dorsolateral prefrontal cortex (self-regulation) and striatum (reward), plus insular hyperactivity to food cues driving impulsive/compulsive food approach ([PMC7311647 / Int J Neuropsychopharmacol 2020](https://academic.oup.com/ijnp/article/23/6/356/5811695); [Frontiers 2022 OFC](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.963092/full)) →
5. **Binge-eating episode** (loss-of-control overconsumption) →
6. **Compensatory purging behavior** (self-induced vomiting most common; laxative/diuretic misuse; excessive exercise), driven by shape/weight overvaluation and anxiety-reduction reinforcement (negative reinforcement loop: purging transiently reduces post-binge distress, reinforcing the cycle) →
7. **Systemic/metabolic sequelae:** Recurrent vomiting → gastric acid exposure to oral cavity/esophagus → dental enamel erosion (perimyolysis), esophagitis, rare Mallory-Weiss tears/Boerhaave esophageal rupture; hydrochloric acid and fluid loss → hypochloremic, hypokalemic metabolic alkalosis (pseudo-Bartter physiology via chronic volume depletion → secondary hyperaldosteronism) → risk of QTc prolongation and arrhythmia (torsades de pointes); salivary gland (parotid) hypertrophy with elevated serum amylase.

### Gut-brain axis
Vagal gut-brain signaling governs mesolimbic dopamine dynamics; gut microbial metabolites (short-chain fatty acids, bile acids, tryptophan metabolites) and microbially synthesized neurotransmitters (dopamine, serotonin, GABA) may modulate reward-driven eating behavior, an emerging area of interest connecting the gut microbiome to BN's binge phenotype ([PMC12857734](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12857734/); [Bulimia Nervosa and Depression, gut microbiota](https://www.imrpress.com/journal/FBL/29/8/10.31083/j.fbl2908277)).

### Molecular pathways / GO term suggestions
- Serotonergic signaling: `GO:0007210` serotonin receptor signaling pathway
- Dopaminergic reward signaling: `GO:0007212` dopamine receptor signaling pathway
- Appetite regulation / satiety: `GO:0032100` positive regulation of appetite; `GO:0032099` negative regulation of appetite
- Response to nutrient levels / feeding behavior: `GO:0007631` feeding behavior

### Cell types / anatomical substrates (CL/UBERON suggestions)
- Neurons of ventral striatum/nucleus accumbens (reward): `CL:0000540` neuron (generic; more specific CL terms for medium spiny neurons: `CL:0000842`? verify via OAK)
- Hypothalamic arcuate nucleus neurons (appetite regulation)
- Parotid gland acinar cells (secondary complication): `UBERON:0001830` parotid gland

### Biochemical abnormalities
Hypokalemia (`HP:0002900`), hypochloremia, metabolic alkalosis, hyperamylasemia (salivary isoenzyme predominance) — direct consequences of purging, not primary disease mechanism, but clinically critical downstream nodes.

### Immune involvement
Not a primary feature; no established autoimmune/inflammatory mechanism in BN specifically (contrast with some appetite-neuropeptide-autoantibody findings reported in AN — [PMC3782835](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3782835/) discusses "mixed" orexigenic/anorexigenic autoantibody signals relevant to both AN and BN, an area of ongoing investigation).

### Model-system caveat
Much of the gut-hormone and reward-circuit mechanistic evidence blends human clinical (fMRI, hormone assay) studies with rodent binge-eating-prone (BEP) models; rodent bingeing models capture caloric/palatability-driven overconsumption and associated anxiety-like behavior but do not fully recapitulate purging behavior or the cognitive shape/weight-overvaluation component — a human-model mismatch worth flagging if curated as a `HUMAN_MODEL_MISMATCH` discussion.

Sources: [PMC3782835](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3782835/), [PMC12857734](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12857734/), [ScienceDirect reward dysregulation](https://www.sciencedirect.com/science/article/abs/pii/S0028390811004898), [PMC7311647](https://pmc.ncbi.nlm.nih.gov/articles/PMC7311647/), [Frontiers 2022 OFC VBM/FC](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.963092/full), [PMC6379643](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6379643/)

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Central nervous system (reward/limbic circuitry, hypothalamus) — primary driver; secondary/complication organs: gastrointestinal tract (oral cavity, esophagus, stomach), salivary glands (parotid), cardiovascular system (arrhythmia risk from electrolyte disturbance), renal system (electrolyte/fluid balance), endocrine/reproductive system (menstrual irregularity), dental/oral structures.

**Body systems involved:** Nervous (CNS reward/cognitive control), digestive (esophagus, salivary glands, dental enamel), cardiovascular, renal, endocrine/reproductive, psychiatric/behavioral.

**UBERON suggestions:**
- `UBERON:0001630` muscle organ / `UBERON:0006562` — not directly relevant
- `UBERON:0001043` esophagus
- `UBERON:0001830` parotid gland
- `UBERON:0001723` tooth enamel (or `UBERON:0001754` tooth)
- `UBERON:0002107` liver — not primary but monitored in refeeding/metabolic workups
- `UBERON:0002037` cerebellum / `UBERON:0002420` basal ganglia (striatum) — reward circuitry
- `UBERON:0001876` amygdala

**Tissue/cell level:** Dental enamel (acid erosion), esophageal squamous epithelium (irritation/tears), parotid acinar tissue (hypertrophy), gastric mucosa.

**Subcellular:** Not a primary organelle-level disease; mitochondrial/oxidative changes are not established mechanistic features.

**Lateralization:** Not applicable (systemic/bilateral/symmetric where relevant, e.g., bilateral parotid enlargement).

Sources: [Cleveland Clinic J Med](https://www.ccjm.org/content/88/6/333), [ScienceDirect salivary gland enlargement](https://www.sciencedirect.com/science/article/abs/pii/S0006322398002212)

---

## 8. Temporal Development

- **Onset:** Adolescence to early adulthood; median age of onset typically 18–21 years, though onset can occur earlier (early teens) or later. Onset pattern is typically insidious, often emerging after a period of dietary restriction (subacute/gradual).
- **Progression:** Variable — can remain stable, progress in severity/frequency, or fluctuate episodically; DSM-5 severity specifiers (mild/moderate/severe/extreme) are frequency-based, not stage-based.
- **Disease course pattern:** Predominantly episodic/relapsing-remitting; approximately two-thirds of patients achieve substantial improvement or recovery long-term, with frequent relapses in between, and 15–20% follow a chronic protracted course ([Am J Psychiatry, "Outcome of bulimia nervosa" 2009](https://psychiatryonline.org/doi/10.1176/appi.ajp.2009.09040582); [PubMed:19884225](https://pubmed.ncbi.nlm.nih.gov/19884225/)).
- **Remission patterns:** Both spontaneous and treatment-induced remission occur; risk of relapse declines notably after ~4 years post-presentation. Full and partial remission are formal DSM-5 specifiers.
- **Critical periods:** Adolescence/young adulthood represents the key vulnerability window (developmental identity formation + peak dieting-behavior prevalence); early intervention within the first few years of illness onset is associated with better prognosis.

Sources: [PubMed:9054777](https://pubmed.ncbi.nlm.nih.gov/9054777/), [PubMed:19884225](https://pubmed.ncbi.nlm.nih.gov/19884225/), [PubMed:9892257](https://pubmed.ncbi.nlm.nih.gov/9892257/)

---

## 9. Inheritance and Population

### Epidemiology
- **Lifetime prevalence:** 0.8–2.6% among women; 0.1–0.2% among men (some sources cite up to 3% of females and >1% of males) ([search synthesis of multiple epidemiological reviews](https://pmc.ncbi.nlm.nih.gov/articles/PMC8500372/)).
- **Global burden trend:** Age-standardized prevalence increased ~43% globally from 1990–2021 (EAPC 0.57); burden correlates positively with socioeconomic development; Australia had the highest burden in 2021; fastest growth in East and South Asia; decline in high-income North America ([PMC12164058](https://pmc.ncbi.nlm.nih.gov/articles/PMC12164058/); [J Eating Disorders 2025](https://link.springer.com/article/10.1186/s40337-025-01289-9)).
- **Age distribution:** Most common in adolescents (10–19y) and young adults (20–40y), especially in Western/high-income countries.

### Inheritance pattern
Multifactorial/polygenic — not Mendelian. OMIM designates a "susceptibility" locus construct (`607499`), consistent with complex trait architecture.
- **Heritability:** ~50–60% (twin studies).
- **Penetrance/expressivity:** Not applicable in the Mendelian sense; risk is probabilistic/polygenic, modulated heavily by environmental exposure (dieting, trauma).
- **Genetic anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency:** Not applicable to this polygenic behavioral/psychiatric disorder.

### Population demographics
- **Sex ratio:** Strongly female-predominant (historically cited ~10:1 female:male in clinical samples, though population-based estimates suggest a narrower gap and rising recognition in males).
- **Geographic distribution:** Higher burden in higher-SES/Western countries historically; rapidly rising in East/South Asia; regional variation reflects both true prevalence differences and detection/reporting differences.

Sources: [PMC8500372](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8500372/), [PMC12164058](https://pmc.ncbi.nlm.nih.gov/articles/PMC12164058/), [Oxford Academic Eur J Public Health 2026](https://academic.oup.com/eurpub/article/36/3/ckag069/8671892)

---

## 10. Diagnostics

### Clinical/laboratory tests
- **Electrolytes:** Serum potassium, chloride, bicarbonate — screen for hypokalemic, hypochloremic metabolic alkalosis (most common abnormality, ~27.4% of BN patients show metabolic alkalosis; hypochloremia ~23.8%; hypokalemia ~13.7%) ([search synthesis of medical-complications literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC4392812/)).
- **Serum amylase:** Elevated (salivary isoenzyme) correlating with binge/purge frequency and parotid enlargement — useful non-invasive marker of active purging ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0006322398002212)).
- **ECG:** To assess QTc interval, especially with significant hypokalemia — risk of torsades de pointes.
- **Dental exam:** Perimyolysis (lingual-surface enamel erosion of maxillary teeth) is a sensitive clinical sign of chronic self-induced vomiting ([PMC11986531 dentin hypersensitivity study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11986531/)).
- **Imaging:** Not routinely required for diagnosis; used if complications suspected (e.g., chest/abdominal imaging for suspected esophageal rupture).

### Genetic testing
Not clinically indicated — BN is not a Mendelian/single-gene disorder; no diagnostic genetic test exists.

### Screening tools
- **SCOFF questionnaire:** 5-item screen (Sick, Control, One stone, Fat, Food); cutoff ≥2 "yes" answers; sensitivity 84.6%, specificity 89.6% in primary care, detecting all AN and BN cases and 77% of EDNOS in the validating study ([search synthesis](https://pubmed.ncbi.nlm.nih.gov/18359005/)).
- **EDE-Q (Eating Disorder Examination Questionnaire):** 28-item self-report across 4 subscales (restraint, eating concern, shape concern, weight concern); optimal global-score cutoff ≥2.80 (sensitivity/specificity ~0.80/0.80) ([ScienceDirect EDE-Q vs SCOFF](https://www.sciencedirect.com/science/article/abs/pii/S0005796708000351)).

### Clinical diagnostic criteria
- **DSM-5:** Recurrent binge eating + recurrent inappropriate compensatory behavior, both occurring on average ≥1×/week for 3 months; self-evaluation unduly influenced by shape/weight; not occurring exclusively during AN episodes.
- **ICD-11 (6B81):** Similar core criteria; frequency threshold ≥1×/week for ≥1 month; notably includes "subjective binges" (loss of control even without objectively large intake) — a key ICD-11/DSM-5 divergence. About 98% diagnostic concordance between ICD-11 and DSM-5 in inpatient samples ([PMC6515596](https://pmc.ncbi.nlm.nih.gov/articles/PMC6515596/)).
- **Differential diagnosis:** Anorexia nervosa binge-purge subtype (distinguished by significantly low body weight), binge-eating disorder (no regular compensatory behavior), Kleine-Levin syndrome, atypical depression with hyperphagia, Prader-Willi syndrome (in relevant developmental contexts), medical causes of vomiting.

Sources: [SCOFF validation](https://pubmed.ncbi.nlm.nih.gov/18359005/), [ICD-11 field study PMC6515596](https://pmc.ncbi.nlm.nih.gov/articles/PMC6515596/), [PMC11986531](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11986531/)

---

## 11. Outcome/Prognosis

- **Mortality:** Crude mortality rate ~0.3% across pooled follow-up studies (7 deaths/2,194 subjects, likely an underestimate given short follow-up); more recent cohort analyses indicate a ~50% increased risk of death (all-cause) relative to general population ([PubMed:23771148 — longitudinal mortality study](https://pubmed.ncbi.nlm.nih.gov/23771148/)).
- **Long-term recovery:** At 5–10 years, ~50% fully recover; ~20% continue to meet full BN criteria; ~30% relapse into bulimic symptoms after initial improvement (risk of relapse declines after ~4 years) ([PubMed:9054777](https://pubmed.ncbi.nlm.nih.gov/9054777/)).
- **Quarter-century synthesis:** ~45% full recovery on average, ~27% considerable improvement, ~23% chronic protracted course ([Am J Psychiatry 2009](https://psychiatryonline.org/doi/10.1176/appi.ajp.2009.09040582)).
- **Prognostic factors:** Impulsivity (personality trait) associated with poorer outcome; comorbid depression/substance use predicts persistence ([ScienceDirect comorbid depression/substance use](https://www.sciencedirect.com/science/article/abs/pii/S2589979121000408)); treatment speeds recovery but doesn't strongly alter outcome beyond 5 years post-presentation.
- **Complications driving morbidity:** Electrolyte-disturbance-related cardiac arrhythmia, GI complications (Mallory-Weiss tear, rare Boerhaave esophageal rupture), dental damage, and psychiatric comorbidity burden (depression, anxiety, substance use) are the principal drivers of long-term morbidity.
- **QoL:** Chronic BN is associated with substantial reduction in psychosocial functioning and quality of life, improving with successful treatment.

Sources: [PubMed:23771148](https://pubmed.ncbi.nlm.nih.gov/23771148/), [PubMed:9054777](https://pubmed.ncbi.nlm.nih.gov/9054777/), [Am J Psychiatry 2009](https://psychiatryonline.org/doi/10.1176/appi.ajp.2009.09040582)

---

## 12. Treatment

### Pharmacotherapy
- **Fluoxetine** (SSRI; `CHEBI:5118`): The only FDA-approved medication for BN, at a higher dose (60 mg/day) than typical antidepressant dosing. RCT evidence: fluoxetine reduces core binge/purge symptoms and psychological features in the short term ([PubMed:9299800](https://pubmed.ncbi.nlm.nih.gov/9299800/); [systematic review PubMed:17370288](https://pubmed.ncbi.nlm.nih.gov/17370288/)).
- **Combination fluoxetine + CBT:** All three arms (fluoxetine alone, CBT alone, combination) showed improvement in an RCT; combination was superior to medication alone on some parameters but not significantly superior to CBT alone ([PubMed:9299800](https://pubmed.ncbi.nlm.nih.gov/9299800/)).
- **Topiramate** (anticonvulsant, off-label): Reduces binge urges via effects on appetite/impulse-control-relevant neurotransmission; studied in partial responders ([NCT00988481](https://clinicaltrials.gov/study/NCT00988481)).
- **Lisdexamfetamine** (psychostimulant, FDA-approved for BED, off-label in BN): Emerging open-label feasibility data in BN adults show reductions in binge/purge frequency ([PMC10204259](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204259/)); case-series data on psychostimulants generally show reduced binge/purge days ([PubMed:28111772](https://pubmed.ncbi.nlm.nih.gov/28111772/)).

### Psychotherapy (first-line)
- **Cognitive Behavioral Therapy (CBT), including enhanced CBT (CBT-E):** Leading evidence-based treatment; reduces core behavioral/psychological features in short and long term ([systematic review PubMed:17370288](https://pubmed.ncbi.nlm.nih.gov/17370288/)). MAXO suggestion: cognitive behavioral therapy — closest MAXO/NCIT term should be verified via OAK (`NCIT:C49236` Therapeutic Procedure as a fallback if no specific CBT term exists).
- **Interpersonal psychotherapy (IPT):** An evidence-based alternative, slower onset of effect but comparable longer-term outcomes to CBT in some trials.
- Guided self-help CBT models have been piloted in non-Western settings (e.g., Japan) with promising feasibility ([PMC5918895](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5918895/); [PMC7041176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7041176/)).

### Nutritional/behavioral/supportive
- Nutritional counseling/rehabilitation, regular meal-pattern restoration, and psychoeducation are standard adjunctive components.
- Group therapy formats are under active study (e.g., "Step by Step Group Therapy for Bulimia Nervosa" — [NCT06063278](https://clinicaltrials.gov/study/NCT06063278)).
- Physical exercise and dietary therapy have been compared to CBT in RCT protocols (PED-t trial — [PMC5427572](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5427572/)).

### Medical/supportive management of complications
Electrolyte repletion (aggressive potassium correction to prevent arrhythmia), dental care, and monitoring for esophageal injury in severe purging.

### Experimental / advanced therapeutics
No gene therapy, cell therapy, or immunotherapy approaches are applicable — BN is a behavioral/psychiatric disorder, not amenable to these modalities. Active clinical trial areas include neurobiological/fMRI-guided treatment-response studies (e.g., "Neurobiology of Bulimia Nervosa" — [NCT04225221](https://clinicaltrials.gov/study/NCT04225221)) and self-control/impulsivity-targeted interventions ([NCT04409457](https://clinicaltrials.gov/study/NCT04409457)).

### Treatment algorithm
Guideline-concordant stepped care: CBT-E (or IPT) as first-line psychotherapy; fluoxetine as first-line/adjunctive pharmacotherapy or for partial responders; topiramate/psychostimulants as off-label augmentation in treatment-resistant cases; inpatient/higher level of care for medical instability (severe electrolyte disturbance, cardiac risk).

Suggested MAXO terms: `MAXO:0000950` supportive care (nutritional/medical monitoring), pharmacotherapy generically under `NCIT:C15986`, with `therapeutic_agent` CHEBI binding to fluoxetine (`CHEBI:5118`) and topiramate; psychotherapy modality would need a dedicated MAXO/NCIT lookup (verify via OAK — likely closest is a general "psychotherapy" or "behavioral therapy" NCIT term).

Sources: [PubMed:9299800](https://pubmed.ncbi.nlm.nih.gov/9299800/), [PubMed:17370288](https://pubmed.ncbi.nlm.nih.gov/17370288/), [PMC10204259](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204259/), [PubMed:28111772](https://pubmed.ncbi.nlm.nih.gov/28111772/)

---

## 13. Prevention

- **Primary prevention:** School- and media-literacy-based programs targeting thin-ideal internalization, body dissatisfaction, and dieting behavior; universal and targeted (high-risk) prevention curricula have shown modest efficacy in reducing eating-disorder risk-factor endorsement.
- **Secondary prevention/early detection:** Primary-care screening with SCOFF or EDE-Q in at-risk populations (adolescent girls, athletes in weight-sensitive sports, individuals with early dieting behavior or subthreshold binge/purge symptoms).
- **Tertiary prevention:** Relapse-prevention components within CBT-E; ongoing monitoring of electrolytes/dental health in patients with residual purging behavior to prevent life-threatening complications (arrhythmia, esophageal rupture).
- **Behavioral interventions:** Reducing dieting behavior, promoting normalized eating patterns, media-literacy and body-acceptance interventions.
- **Counseling:** Family-based approaches and psychoeducation for caregivers; no genetic counseling role given the polygenic, non-Mendelian architecture.
- **Public health:** Broader social-media/advertising regulation discussions around thin-ideal content; weight-stigma reduction campaigns.
- **Immunization/prophylaxis:** Not applicable.

Sources: General synthesis from [NEDA risk factors](https://www.nationaleatingdisorders.org/risk-factors/) and prevention literature cited in etiology searches above.

---

## 14. Other Species / Natural Disease

BN as clinically defined (with its cognitive component of shape/weight overvaluation) is a human-specific psychiatric construct; there is **no known naturally occurring veterinary analog** in companion animals or wildlife, and no OMIA entry exists for a bulimia-like natural disease. This is distinct from binge-eating/palatability-driven overconsumption, which is modeled experimentally (see §15).

- **Taxonomy:** Not applicable for natural disease.
- **Zoonotic potential:** Not applicable.

---

## 15. Model Organisms

BN pathophysiology (specifically the binge-eating component) is modeled almost exclusively via **induced rodent models**, since no genetic/knockout model recapitulates the full human syndrome (including purging and cognitive shape/weight overvaluation).

- **Binge-Eating-Prone (BEP) / Binge-Eating-Resistant (BER) rat model:** Rats undergo repeated intermittent exposure to palatable food; individual variation in over- vs under-consumption identifies BEP vs. BER phenotypes, used to study neurobiological risk factors for binge eating ([Springer protocol](https://link.springer.com/protocol/10.1007/978-1-0716-0924-8_2)).
- **Sugar-bingeing / intermittent access model:** Periodic (e.g., 12-hour) food restriction followed by scheduled access to 25% glucose or 10% sucrose solution; over ~3 weeks produces a bingeing pattern (up to 32% of caloric intake from sugar), used as a model of behavioral/neurochemical "sugar addiction" relevant to binge-type eating disorders ([PMC4361030](https://pmc.ncbi.nlm.nih.gov/articles/PMC4361030/)).
- **Neurochemical findings from these models:** Altered dopamine D1/D2 receptor balance, changes in midbrain serotonin neurotransmission — mirroring hypothesized human corticostriatal reward dysregulation ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0028390811004898); [PMC3366171](https://pmc.ncbi.nlm.nih.gov/articles/PMC3366171/)).
- **Behavioral readouts:** Elevated Plus-Maze anxiety-like behavior is increased (small effect size) across pooled rodent binge-eating studies (systematic review/meta-analysis of 18 studies) ([ScienceDirect meta-analysis](https://www.sciencedirect.com/science/article/abs/pii/S0149763421004784)).
- **Model limitations:** Rodent bingeing models do not capture compensatory purging behavior, body-image/shape-weight cognitive overvaluation, or the menstrual-cycle/estrogen-linked symptom fluctuation seen in humans — an important human-model-mismatch caveat for any hypothesis-flagged pathophysiology node built from these data.
- **Applications:** Used to dissect neurochemical/circuit-level contributions to loss-of-control eating, palatability-driven reward, and pharmacological screening (e.g., topiramate, opioid-antagonist, and serotonergic-agent testing) relevant to BN's binge component.

Sources: [PMC3132131](https://pmc.ncbi.nlm.nih.gov/articles/PMC3132131/), [Springer BEP/BER protocol](https://link.springer.com/protocol/10.1007/978-1-0716-0924-8_2), [PMC4361030](https://pmc.ncbi.nlm.nih.gov/articles/PMC4361030/), [MDPI 2023 rodent pharmacotherapy review](https://www.mdpi.com/2218-273X/13/5/742)

---

## Summary of Key Ontology Term Suggestions

| Domain | Term |
|---|---|
| Disease | `MONDO:0005452` bulimia nervosa; `DOID:12129`; `ICD-11:6B81`; `ICD-10-CM:F50.2`; `OMIM:607499` (susceptibility) |
| Core phenotype | `HP:0100739` Bulimia |
| Lab phenotypes | `HP:0002900` Hypokalemia; `HP:0001941` Metabolic alkalosis; `HP:0003111` Hypochloremia |
| Psychiatric comorbid phenotypes | `HP:0000716` Depressivity; `HP:0000739` Anxiety; `HP:0100710` Impulsivity |
| Endocrine | `HP:0000141` Amenorrhea |
| GO biological processes | `GO:0007631` feeding behavior; `GO:0007210` serotonin receptor signaling pathway; `GO:0007212` dopamine receptor signaling pathway; `GO:0032100`/`GO:0032099` regulation of appetite |
| UBERON | `UBERON:0001043` esophagus; `UBERON:0001830` parotid gland; `UBERON:0002420` basal ganglia/striatum |
| CHEBI (drugs) | `CHEBI:5118` fluoxetine; topiramate (verify CHEBI ID via OAK) |
| Genes (candidate, low confidence) | `hgnc:11050` SLC6A4; `hgnc:1033` BDNF; `hgnc:8156` OPRD1; `hgnc:3444` ESR1 |
| MAXO/NCIT (treatment) | `NCIT:C15986` Pharmacotherapy (+ `therapeutic_agent` CHEBI binding); CBT/psychotherapy term — verify specific MAXO/NCIT code via OAK lookup |

---

## Notes on Evidence Gaps for Curation

1. **No BN-specific genome-wide-significant GWAS locus** has been published as of this report (contrast with AN); candidate-gene findings (5-HTTLPR, BDNF, OPRD1, ESR1) should be curated as `evidence_source: HUMAN_CLINICAL` with an explicit caveat about small-sample/candidate-gene-era limitations, or considered for a `KNOWLEDGE_GAP` discussion entry.
2. **No dedicated HP terms** exist for several clinically important signs (Russell's sign, perimyolysis/dental erosion, parotid enlargement specifically) — these will need either a best-fit broader HP term or documentation via `notes`/free text rather than a forced ontology binding.
3. **Rodent binge-eating models** do not recapitulate purging or cognitive shape/weight overvaluation — a strong candidate for a `HUMAN_MODEL_MISMATCH` discussion node if a MODEL_ORGANISM-sourced pathophysiology claim (e.g., dopamine D1/D2 imbalance) is included.
4. All PMIDs/URLs above should be independently re-verified against cached abstracts (`just fetch-reference`) and exact-quote snippets extracted before use in KB YAML, per dismech's evidence SOP — this report is a research lead document, not pre-validated curation content.

**Sources (consolidated):**
- [ICD-11 Criteria for Bulimia Nervosa (MRCPsych UK)](https://www.mrcpsych.uk/2022/05/icd-11-criteria-for-bulimia-nervosa-6b81.html)
- [ICD-11 field study, PMC6515596](https://pmc.ncbi.nlm.nih.gov/articles/PMC6515596/)
- [StatPearls: Bulimia Nervosa](https://www.ncbi.nlm.nih.gov/books/NBK562178/)
- [OMIM:607499](https://omim.org/entry/607499)
- [Kendler et al., PMID:1842216](https://pubmed.ncbi.nlm.nih.gov/1842216/)
- [Nature Translational Psychiatry 2023](https://www.nature.com/articles/s41398-023-02585-1)
- [PMC2907970 — Bulimia nervosa review](https://pmc.ncbi.nlm.nih.gov/articles/PMC2907970/)
- [Frontiers 2022 — ACEs and eating disorders](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1063693/full)
- [PMC8860810 — childhood maltreatment network analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8860810/)
- [PMC3782835 — orexigenic/anorexigenic autoantibodies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3782835/)
- [PMC12857734 — gut-brain vagal axis and dopamine](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12857734/)
- [ScienceDirect — reward system dysregulation animal models](https://www.sciencedirect.com/science/article/abs/pii/S0028390811004898)
- [PMC3366171](https://pmc.ncbi.nlm.nih.gov/articles/PMC3366171/)
- [PMC7311647 / Int J Neuropsychopharmacol 2020](https://academic.oup.com/ijnp/article/23/6/356/5811695)
- [Frontiers 2022 — OFC VBM/FC study](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.963092/full)
- [PMC6379643 — resting-state fMRI BED/BN](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6379643/)
- [Cleveland Clinic Journal of Medicine — medical complications](https://www.ccjm.org/content/88/6/333)
- [ScienceDirect — salivary gland enlargement/amylase](https://www.sciencedirect.com/science/article/abs/pii/S0006322398002212)
- [PMC4392812 — medical complications review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4392812/)
- [PMC11986531 — dentin hypersensitivity in BN](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11986531/)
- [PMC6034764 — hospitalization outcomes/comorbidities](https://pmc.ncbi.nlm.nih.gov/articles/PMC6034764/)
- [PubMed:9299800 — fluoxetine + CBT RCT](https://pubmed.ncbi.nlm.nih.gov/9299800/)
- [PubMed:17370288 — treatment systematic review](https://pubmed.ncbi.nlm.nih.gov/17370288/)
- [PMC10204259 — lisdexamfetamine feasibility trial](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204259/)
- [PubMed:28111772 — psychostimulants case reports](https://pubmed.ncbi.nlm.nih.gov/28111772/)
- [NCT00988481 — topiramate augmentation](https://clinicaltrials.gov/study/NCT00988481)
- [NCT06063278 — group therapy](https://clinicaltrials.gov/study/NCT06063278)
- [NCT04225221 — neurobiology of BN](https://clinicaltrials.gov/study/NCT04225221)
- [PubMed:23771148 — longitudinal mortality study](https://pubmed.ncbi.nlm.nih.gov/23771148/)
- [PubMed:9054777 — outcome in bulimia nervosa](https://pubmed.ncbi.nlm.nih.gov/9054777/)
- [Am J Psychiatry 2009 — quarter-century outcome review](https://psychiatryonline.org/doi/10.1176/appi.ajp.2009.09040582)
- [PMC8500372 — incidence/prevalence/mortality review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8500372/)
- [PMC12164058 — GBD 2021 analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC12164058/)
- [PMC2275291 — AN-restricting to BN transition](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2275291/)
- [PMC3132131 — rat models of binge eating](https://pmc.ncbi.nlm.nih.gov/articles/PMC3132131/)
- [PMC4361030 — sugar addiction rat model](https://pmc.ncbi.nlm.nih.gov/articles/PMC4361030/)
- [Springer protocol — BEP/BER model](https://link.springer.com/protocol/10.1007/978-1-0716-0924-8_2)
- [PubMed:18359005 — EDE-Q vs SCOFF screening](https://pubmed.ncbi.nlm.nih.gov/18359005/)