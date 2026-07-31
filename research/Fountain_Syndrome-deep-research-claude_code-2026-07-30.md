---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T23:42:14.415122'
end_time: '2026-07-30T23:45:51.806509'
duration_seconds: 217.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fountain Syndrome
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
  web_search_requests: 12
  num_turns: 25
  total_cost_usd: 1.5855094999999997
  session_id: e722e065-5a7d-5394-8cd4-4642dbac948f
  stop_reason: end_turn
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fountain Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fountain Syndrome** covering all of the
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

# Fountain Syndrome — Comprehensive Disease Research Report

## ⚠️ Critical Disambiguation (read first)

The name "Fountain syndrome" is genetically **ambiguous** and this report addresses the classic (1974) entity, distinguishing it from two other conditions that share the name/eponym or overlapping phenotype:

| Entity | OMIM | MONDO | Gene | Inheritance |
|---|---|---|---|---|
| **Fountain syndrome** (this report) | **229120** | **MONDO:0009241** | **Unknown / unmapped** | Autosomal recessive |
| Hao–Fountain syndrome (HAFOUS) | 616863 | MONDO:0014777 | *USP7* | Autosomal dominant (de novo) |
| Dominant deafness–onychodystrophy (DDOD) / DOORS syndrome / Zimmermann-Laband syndrome | 124480 / 220500 / 135500 | — | *ATP6V1B2* (DDOD, ZLS dominant; DOORS also has *TBC1D24* biallelic form) | AD (DDOD, ZLS) / AR (DOORS) |

Hao–Fountain syndrome is named for a different discoverer group (Hao et al., 2015) and Dr. Christian Schaaf's Baylor group, and is unrelated genetically to the classic Fountain syndrome described by R.B. Fountain in 1974 — the shared surname is coincidental (Hao–Fountain syndrome is also called "USP7-related neurodevelopmental disorder"). Likewise, ATP6V1B2-related DDOD/DOORS/Zimmermann-Laband syndromes share a deafness + skeletal/nail phenotype but are molecularly and nosologically distinct — MalaCards and some AI-generated summaries conflate these because of overlapping keyword profiles ("deafness," "skeletal," "intellectual disability"), which is exactly the kind of Named-Entity-Confusion risk to guard against when curating this disease. All findings below pertain specifically to **OMIM #229120 / MONDO:0009241 / Orphanet ORPHA3219**.

---

## 1. Disease Information

**Overview:** Fountain syndrome is an extremely rare, autosomal recessive, congenital multisystem disorder first described by R.B. Fountain in 1974 in a sibship of three brothers and a sister with intellectual disability, congenital sensorineural deafness, skeletal abnormalities, and a coarse facial appearance with progressive, non-inflammatory swelling ("granulomatous"-appearing) of the lips and cheeks (Fountain RB, *Proc R Soc Med.* 1974;67(9):878-9, PMID:4431800). The condition was clinically re-characterized and confirmed as a distinct autosomal recessive entity by Fryns and colleagues in two subsequent reports describing overlapping/additional cases (Fryns JP et al., *Am J Med Genet.* 1987;26(3):551-5, PMID:3565469; Fryns JP, *J Med Genet.* 1989;26(11):722-4, PMID:2585470 — this paper coined the eponym "Fountain's syndrome").

**Key identifiers:**
- **OMIM:** #229120 ("FOUNTAIN SYNDROME")
- **MONDO:** MONDO:0009241
- **Orphanet:** ORPHA3219
- **MedGen:** C0795944 (UID 208650)
- **MeSH indexing (from Fryns 1989):** covers "Abnormalities, Multiple," "Intellectual Disability," "Deafness," "Face/abnormalities," "Skull/abnormalities"

**Synonyms (per MedGen/OMIM):**
- Mental retardation, sensorineural deafness, skeletal abnormalities, and coarse face with full lips
- Deafness with skeletal dysplasia and lip granuloma syndrome
- Deafness, skeletal dysplasia, coarse face with full lips syndrome
- Fountain's syndrome

**Data provenance:** All available clinical information derives from **aggregated case-series literature** — specifically a total of essentially one extended kindred plus one additional unrelated patient across the three foundational publications (Fountain 1974: 4 sibs; Fryns 1987: 3 severely affected males, two of them siblings and one unrelated). There is **no EHR-derived, registry, or large-cohort data** for this condition; it is one of the rarest described Mendelian syndromes, with essentially no independent replication literature since 1989 (searches for post-1989 case reports return only results for the molecularly distinct Hao–Fountain syndrome, confirming the profound rarity/possible underrecognition of the classic entity).

---

## 2. Etiology

**Disease causal factors:** Genetic — Mendelian, autosomal recessive. **The causal gene/locus has never been identified or mapped.** No linkage study, homozygosity mapping, or exome/genome sequencing study of the original or subsequent kindreds has been published in the literature indexed to date. OMIM #229120 remains a clinically-defined (phenotypic) entry without a molecular gene entry — this is explicitly reflected in its "manifests" and cross-reference behavior on OMIM/MedGen (no HGNC gene is linked to the phenotype MIM number).

**Genetic risk factors:** None characterized beyond the Mendelian recessive transmission pattern itself. Because the original description was in a sibship (3 of 4 sibs affected, consistent with autosomal recessive segregation) and the unrelated third case in Fryns 1987 was also male with a similarly severe phenotype, consanguinity or a shared founder allele has been hypothesized but not documented in the primary reports as available in search results. No GWAS, ClinVar entries, or GeneMatcher-style gene-candidate data exist for this specific phenotype MIM.

**Environmental risk factors:** None reported; this is described purely as a genetic/congenital disorder with no known environmental, infectious, or teratogenic contribution.

**Protective factors:** Not applicable / not documented — no data exists on genetic or environmental modifiers given the extreme rarity of reported cases.

**Gene-environment interactions:** Not applicable — no gene has been identified, precluding any GxE analysis.

**Suggested action for a knowledge-base entry:** Given the unmapped molecular basis, the `genetic:` section of a dismech-style entry should likely be **omitted or explicitly marked as unknown**, rather than populated with a candidate gene. Do not conflate with *USP7* (Hao–Fountain) or *ATP6V1B2* (DDOD/DOORS/ZLS) — these must not appear as causal genes for MONDO:0009241.

---

## 3. Phenotypes

Phenotype data are drawn from the original case descriptions (Fountain 1974; Fryns 1987, 1989) as aggregated in OMIM, Orphanet, and MedGen. Because only a handful of individuals have ever been reported, **all frequencies below should be treated as qualitative/descriptive ("present in the reported cases") rather than population-level percentages** — there is no denominator large enough to support formal frequency bands (Orphanet itself does not publish a frequency table for this entry given the case-report-only evidence base).

### Neurodevelopmental
- **Intellectual disability / mental retardation** — moderate to severe, present in all reported cases. *Suggested term:* HP:0001249 (Intellectual disability)
- **Early-onset generalized seizures** — reported as an expansion of the phenotype by Fryns et al. 1987 in some but not all cases. *Suggested term:* HP:0002197 (Generalized-onset seizure) or HP:0001250 (Seizure)
- **Remarkable/abnormal behavior** — noted qualitatively in some sources (MONDO summary). *Suggested term:* HP:0000708 (Behavioral abnormality)

### Audiologic
- **Congenital sensorineural hearing loss/deafness** — present in all reported cases; tomography in the original cases showed structural cochlear malformation. *Suggested term:* HP:0000410 (Profound sensorineural hearing impairment) or HP:0008619 (Bilateral sensorineural hearing impairment); underlying malformation: HP:0000375 (Abnormal cochlea morphology)

### Craniofacial
- **Coarse facial features** — HP:0000280 (Coarse facial features)
- **Thick/full lower lip (vermilion)** — HP:0012471 (Thick vermilion border) / full lips
- **Facial/lip/cheek soft-tissue swelling ("edema"; in one original case, an eroded granulomatous mass on the lower lip)** — HP:0000286 (Epicanthus not applicable); best mapped as HP:0025322 (facial edema) or free-text if no precise HPO match; the granulomatous lip lesion is a distinctive, possibly idiosyncratic finding in one individual rather than a core diagnostic feature
- **Thickened calvaria (skull vault)** — HP:0002684 (Thickened calvaria)
- **Large head circumference / macrocephaly** — HP:0000256 (Macrocephaly), noted as an additional reported sign

### Skeletal
- **Broad, stubby (short) hands and feet with broad terminal/distal phalanges** — HP:0001181 (Broad thumb) / HP:0011304 (Broad palm) / HP:0100258 (Preaxial polydactyly – not applicable) → best: HP:0011844 (Broad phalanx) and HP:0001167 (Abnormality of the hand)
- **Broad, short palms** — HP:0001180 (Short palm) / HP:0011304 (Broad palm)
- **Kyphosis (hyperkyphosis) / scoliosis** — HP:0002808 (Kyphosis), HP:0002650 (Scoliosis)
- **Short stature** — HP:0004322 (Short stature), reported as an additional feature

### Ophthalmologic
- **Visual impairment / myopia** (per GARD symptom aggregation) — HP:0000572 (Visual impairment) / HP:0000545 (Myopia)

### Oral
- **Gingival overgrowth** (per GARD aggregation) — HP:0000212 (Gingival overgrowth)

**Onset:** Congenital/neonatal-infantile — deafness and skeletal features present from birth or early infancy; facial swelling and other coarse features became more apparent over the first years of life in the original description.

**Severity/progression:** Described as a static-to-slowly-progressive congenital syndrome; the lip/cheek swelling in the index cases was noted to be *progressive*, with an eroded granulomatous lesion developing in one case — suggesting a slowly evolving soft-tissue component layered on top of a static skeletal/audiologic phenotype.

**Quality of life impact:** Not formally studied (no QOL instrument data — EQ-5D/SF-36/PROMIS — exists for this ultra-rare condition). Qualitatively, the combination of severe intellectual disability and profound congenital deafness implies major lifelong functional impact requiring multidisciplinary support, per GARD's general management guidance.

---

## 4. Genetic/Molecular Information

**Causal genes:** **None identified.** OMIM #229120 is a clinical (phenotypic-series) entry with no associated gene/locus MIM number, in contrast to Hao–Fountain syndrome (#616863, *USP7*, chr16p13.2) and the ATP6V1B2-related deafness-skeletal syndromes (DDOD #124480, DOORS #220500 [also *TBC1D24*-biallelic], Zimmermann-Laband #135500), all of which have well-defined molecular bases.

**Pathogenic variants:** Not applicable — no gene to report variants in.

**Modifier genes:** Not documented.

**Epigenetic information:** None reported.

**Chromosomal abnormalities:** None reported; standard karyotyping in the original cases (to the extent performed in the 1970s–80s) did not identify a chromosomal cause, consistent with a single-gene recessive model that remains molecularly uncharacterized.

**Implication for curation:** Any dismech-style KB entry for Fountain syndrome should have an **empty or absent `genetic:` block** (or one explicitly noting "molecular basis unknown / gene not yet identified") rather than a placeholder gene. This is a case where the correct curation action is to document absence of a known genetic cause, consistent with the project's evidence discipline (no fabricated gene-disease associations).

---

## 5. Environmental Information

No environmental, occupational, lifestyle, or infectious contributing factors have been reported for Fountain syndrome in any source reviewed. This is consistent with its classification as a Mendelian congenital disorder.

---

## 6. Mechanism / Pathophysiology

**No molecular pathway, cellular mechanism, or biochemical defect has ever been characterized for this condition** — a direct consequence of the causal gene remaining unidentified. The literature (limited to the three foundational case reports) provides only **descriptive/anatomic** pathophysiology:

- **Auditory system:** Deafness attributed to structural (anatomic) malformation of the cochlea, demonstrated by tomography in the original 1974/1987 cases — i.e., a developmental inner-ear dysplasia rather than a documented biochemical or degenerative mechanism. *Suggested terms:* UBERON:0001844 (cochlea), GO:0009786 (regulation of asymmetric cell division – not directly applicable); more appropriately this is a developmental/morphogenetic anomaly (HP:0000375, abnormal cochlea morphology) rather than a GO-annotatable pathway given the absence of molecular data.
- **Skeletal system:** Thickened calvaria and broad/short distal phalanges suggest a generalized skeletal dysplasia affecting bone modeling, but no histopathology, bone biopsy, or radiographic-genotype correlation beyond gross imaging has been published.
- **Soft tissue (lip/cheek):** Progressive facial/lip swelling with, in one case, an eroded "granulomatous" mass — the original authors used descriptive/histologically unconfirmed terminology ("skin granuloma" appears in the 1974 title), but no formal histopathologic mechanism (e.g., true granulomatous inflammation vs. lymphedema vs. connective tissue accumulation) has been established in indexed literature accessible to this search. This should NOT be conflated with orofacial granulomatosis/Melkersson-Rosenthal syndrome (a distinct, unrelated condition with a similar surface description of lip swelling) without primary-source confirmation.

**No transcriptomic, proteomic, metabolomic, single-cell, or other omics data exist** for this condition — unsurprising given only a handful of patients have ever been described and no causal gene is known to enable functional studies.

**Bottom line for KB curation:** A `pathophysiology:` section for this entry would necessarily be sparse and should be scoped to the **descriptive anatomic findings** (cochlear malformation, calvarial thickening) rather than any causal molecular chain, since none is documented. Any curator should explicitly flag this as a `KNOWLEDGE_GAP` (per the dismech schema's `discussions`/`kind: KNOWLEDGE_GAP` convention) — the disease's fundamental molecular mechanism is unknown.

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Auditory system** — inner ear (cochlea), sensorineural pathway (UBERON:0001846 inner ear cavity / UBERON:0001844 cochlea)
- **Skeletal system** — skull/calvaria (UBERON:0002396 calvaria), hands/feet (UBERON:0002398 manus, UBERON:0002387 pes), spine (UBERON:0001130 vertebral column — for kyphoscoliosis)
- **Craniofacial soft tissue** — lips (UBERON:0002174 lip), cheeks
- **Central nervous system** — implicated by intellectual disability and seizures, though no structural neuroimaging abnormality is specifically documented in the available literature summaries (UBERON:0000955 brain, general)
- **Ocular** — implicated by reported myopia/visual impairment (UBERON:0000970 eye)
- **Oral cavity** — gingiva (UBERON:0001754 gingiva), per gingival overgrowth

**Tissue/cell level:** No cell-type-specific or Cell Ontology (CL)–resolvable data exists; findings are at the gross anatomic/radiographic level only (no biopsy-confirmed cell population implicated in indexed sources).

**Subcellular level:** Not applicable — no molecular/cellular mechanism has been characterized.

**Laterality:** Auditory and skeletal findings are described as bilateral/symmetric (bilateral sensorineural hearing loss, bilateral hand/foot involvement) in the original reports.

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal — hearing loss and skeletal abnormalities are present from birth or earliest infancy (consistent with GARD's classification of onset in the "newborn/infant" period).
- **Onset pattern:** Congenital with some features (facial/lip swelling) noted to be progressive rather than fully present at birth.
- **Progression:** The condition is broadly static in its core skeletal/audiologic phenotype but the soft-tissue lip/cheek swelling was explicitly described as progressive in the original cases (developing into an eroded granulomatous lesion in one individual over time).
- **Disease course:** Chronic, lifelong — no spontaneous remission is described; this is a fixed developmental/congenital disorder rather than a relapsing-remitting one.
- **Critical periods:** None specifically identified; no early-intervention window data exists given the absence of any treatment trials.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Extremely rare — GARD/Orphanet classify it as "<1/1,000,000" worldwide. Only a single kindred (4 siblings, Fountain 1974) plus one additional unrelated case and possible phenotypic overlap in Fryns' subsequent series have been published; the total number of molecularly-undefined "classic" Fountain syndrome cases in the literature is on the order of a handful (fewer than 10) individuals total.
- **Incidence:** Not calculable — no population-based ascertainment exists.

**Inheritance pattern:** Autosomal recessive, based on segregation in the original sibship (affected brothers and sister, unaffected parents) and confirmed by Fryns' independent unrelated case with a similar severe phenotype.

**Penetrance:** Presumed complete within the recessive model as described (all reported homozygous/compound-heterozygous-presumed individuals were symptomatic), though this has never been formally assessed since no causal variant has been identified to correlate with genotype.

**Expressivity:** Some variability noted — e.g., seizures were present in some but not all reported cases (an "additional" feature per Fryns 1987), suggesting variable expressivity within the small reported cohort.

**Genetic anticipation:** Not applicable/not reported.

**Germline mosaicism:** Not documented.

**Founder effects:** Not established — no population-genetic study exists; the original kindred's ethnic/geographic background is not detailed in the abstracts available to this search (original report from the UK, Fryns reports from Belgium — Centre for Human Genetics, University of Leuven — suggesting European ascertainment, but this does not establish a founder allele).

**Consanguinity:** Not explicitly documented as present in the original reports based on available abstracts, though autosomal recessive segregation in a sibship raises this as a reasonable clinical consideration that a full-text review of the primary papers would need to confirm.

**Carrier frequency:** Unknown — cannot be estimated without a known causal gene/variant.

**Population demographics:** All reported cases appear to derive from European (UK and Belgian) case series; no other geographic or ethnic-specific reports were identified. Sex distribution in the reported cases: the original sibship included 3 affected brothers and 1 affected sister (male-predominant numerically but consistent with autosomal, not X-linked, recessive inheritance); Fryns' 1987 series described 3 affected males. This male skew across small case numbers should not be over-interpreted as evidence of X-linkage given the documented father-to-... (irrelevant, since AR) — the original pedigree is consistent with autosomal recessive transmission.

---

## 10. Diagnostics

**Clinical tests reported/used in original case descriptions:**
- **Audiological testing** — to characterize sensorineural hearing loss
- **Tomography (historically) / modern equivalent CT or MRI imaging of the temporal bone/inner ear** — to demonstrate cochlear malformation
- **Skeletal radiographs** — to characterize calvarial thickening, broad/short hand and foot phalanges, kyphoscoliosis
- **Neuroimaging (brain)** — used in modern diagnostic workups per GARD's general recommendation, though no specific finding is reported as diagnostic in the original literature

**Genetic testing:** Because no causal gene is known, there is **no targeted genetic test, gene panel, or diagnostic molecular assay specific to Fountain syndrome**. Diagnosis remains **exclusively clinical**, based on the combination of:
1. Congenital sensorineural deafness with cochlear malformation
2. Intellectual disability (± seizures)
3. Characteristic skeletal findings (thick calvaria, broad/short hands and feet, kyphoscoliosis)
4. Coarse facial features with full/thick lips and progressive facial/lip soft-tissue swelling

Given the phenotypic overlap with other "deafness + skeletal + intellectual disability + coarse face" syndromes, a modern diagnostic workup would reasonably include **exome or genome sequencing to exclude known mimics** (e.g., ATP6V1B2-related DDOD/DOORS/Zimmermann-Laband, USP7-related Hao–Fountain syndrome, mucopolysaccharidoses, and other coarse-facies syndromes), with classic Fountain syndrome remaining a diagnosis of exclusion pending gene discovery.

**Differential diagnosis (inferred from phenotypic overlap, not explicitly stated as a formal differential in the sparse available literature):**
- Hao–Fountain syndrome (*USP7*) — shares the eponym but a distinct, milder-onset neurodevelopmental/behavioral phenotype without the deafness-skeletal-lip triad
- DDOD / DOORS / Zimmermann-Laband syndromes (*ATP6V1B2*, *TBC1D24*) — share deafness + skeletal (nail/phalangeal) findings but center on onychodystrophy (nail aplasia/hypoplasia) rather than coarse facies with lip swelling
- Mucopolysaccharidoses and other coarse-facies/skeletal dysplasia syndromes with hearing loss (general storage-disorder differential, not specifically documented in the primary Fountain syndrome literature reviewed)

**Screening:** No population or newborn screening program exists or is applicable given the absence of a known gene and the extreme rarity of the condition.

---

## 11. Outcome/Prognosis

No formal survival, mortality, or long-term outcome data exist in the literature (case-report-only evidence base with no longitudinal follow-up reported). Qualitatively:

- **Morbidity:** Lifelong severe-to-moderate intellectual disability and profound congenital deafness imply substantial functional impairment and need for lifelong support.
- **Complications:** Progressive facial/lip soft-tissue swelling, with an eroded granulomatous lesion documented in one original case, could represent a source of ongoing morbidity, though its long-term course is not documented beyond the initial reports.
- **Seizures**, when present, add additional morbidity and would be managed per standard anticonvulsant protocols (per GARD's general symptomatic-management guidance).
- **Prognostic biomarkers:** None exist.

---

## 12. Treatment

**No disease-specific or curative treatment exists** — consistent with GARD's statement that "only about 5% of rare diseases have FDA-approved treatments," and Fountain syndrome is not among them. Management is entirely **supportive and symptomatic**, per general rare-disease multidisciplinary care guidance (GARD):

- **Hearing loss management:** Hearing aids; audiological follow-up. *Suggested MAXO term:* MAXO:0009030 (hearing aid usage)
- **Seizure management:** Anticonvulsant medications (specific agents not specified in available sources). *Suggested treatment_term:* NCIT:C15986 (Pharmacotherapy) with therapeutic_agent to be specified per individual regimen if documented
- **Skeletal/orthopedic management:** Bracing and physical therapy for kyphoscoliosis. *Suggested MAXO terms:* MAXO:0000011 (physical therapy); orthopedic bracing (no precise MAXO term identified — may require NCIT:C16186, Orthopedic Surgical Procedure, only if surgery is used; bracing itself may need free-text or a device-classification approach)
- **Developmental/intellectual disability support:** Early intervention, special education, multidisciplinary developmental services (general supportive care pattern; MAXO:0000950, supportive care)
- **Genetic counseling:** Recommended for families given the confirmed autosomal recessive inheritance pattern, despite the unknown causal gene, to convey recurrence risk (~25% for future siblings of an affected proband, per standard AR Mendelian counseling, extrapolated from the established inheritance pattern rather than direct genetic testing). *Suggested MAXO term:* MAXO:0000079 (genetic counseling)
- **Experimental/clinical trials:** None identified — no NCT-registered trials specific to Fountain syndrome were found (searches return only Hao–Fountain syndrome-related content, reinforcing this is a molecularly uncharacterized ultra-rare disorder with no active therapeutic pipeline).

**Treatment outcomes, response rates, personalized medicine approaches:** Not applicable — no data exists.

---

## 13. Prevention

**No primary, secondary, or tertiary prevention strategy exists** beyond generic genetic counseling for at-risk families (given the confirmed but molecularly uncharacterized autosomal recessive inheritance). No prenatal or carrier screening test can be offered since no causal gene has been identified. No immunization, public health, or environmental intervention is applicable, as no environmental contributing factor is implicated.

---

## 14. Other Species / Natural Disease

No naturally occurring animal model, veterinary case report, or cross-species orthologous disease has been identified for Fountain syndrome in any source reviewed — an expected consequence of the causal gene remaining unknown, which precludes any comparative-genomics or veterinary correlation (OMIA, VBO, or NCBI Gene ortholog searches are not meaningfully actionable without a human causal gene to anchor them).

---

## 15. Model Organisms

**None exist.** Because no causal gene has ever been identified for Fountain syndrome (OMIM #229120), there are no knockout mice, zebrafish morphants, Drosophila models, iPSC-derived cellular models, or any other genetically engineered model system representing this specific disease. This stands in sharp contrast to the molecularly-defined Hao–Fountain syndrome (*USP7*) and ATP6V1B2-related syndromes, both of which have documented functional/model-organism literature (e.g., zebrafish and cell-based studies of ATP6V1B2's role in lysosomal acidification and spiral ganglion neuron degeneration, PMC8568048).

---

## Summary Table for Knowledge-Base Curation

| Field | Status |
|---|---|
| Causal gene | **Unknown / unmapped** — do not populate `genetic:` with a candidate gene |
| Pathophysiology | Sparse, descriptive only (cochlear malformation, calvarial thickening); flag as `KNOWLEDGE_GAP` |
| Evidence base | 3 primary papers only: PMID:4431800 (Fountain 1974), PMID:3565469 (Fryns 1987), PMID:2585470 (Fryns 1989) |
| Total reported cases (classic entity) | ~7 individuals across all literature (1 sibship of 4 + up to 3 in Fryns 1987, likely partially overlapping) |
| Key NEC risk | Do not conflate with Hao–Fountain syndrome (USP7, OMIM 616863) or ATP6V1B2-related DDOD/DOORS/Zimmermann-Laband syndromes |
| Treatment | Entirely supportive/symptomatic; no disease-specific therapy or active trials |
| Model organisms | None |

---

### Sources

- [Entry - #229120 - FOUNTAIN SYNDROME - OMIM](https://omim.org/entry/229120)
- [Fountain syndrome | About the Disease | GARD](https://rarediseases.info.nih.gov/diseases/64/fountain-syndrome)
- [Fountain Syndrome - MalaCards](https://www.malacards.org/card/fountain_syndrome)
- [Fountain syndrome - Wikipedia](https://en.wikipedia.org/wiki/Fountain_syndrome)
- [Fountain syndrome (Concept ID: C0795944) - MedGen - NCBI](https://www.ncbi.nlm.nih.gov/medgen/C0795944)
- [fountain syndrome - National Organization for Rare Disorders (NORD)](https://rarediseases.org/mondo-disease/fountain-syndrome/)
- [Fountain's syndrome: mental retardation, sensorineural deafness, skeletal abnormalities, and coarse face with full lips - PubMed (PMID:2585470)](https://pubmed.ncbi.nlm.nih.gov/2585470/)
- [Fountain RB 1974 case report - PubMed (PMID:4431800)](https://pubmed.ncbi.nlm.nih.gov/4431800/) / [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1645940/)
- [Fryns JP et al. 1987 - PubMed (PMID:3565469)](https://pubmed.ncbi.nlm.nih.gov/3565469/)
- [Orphanet: Fountain syndrome (ORPHA3219)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=3219&lng=en)
- Distinguishing entities (for NEC disambiguation):
  - [Entry - #616863 - HAO-FOUNTAIN SYNDROME; HAFOUS - OMIM](https://omim.org/entry/616863)
  - [USP7-Related Hao-Fountain Syndrome - GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK619577/)
  - [Dominant deafness–onychodystrophy syndrome caused by an ATP6V1B2 mutation - PMC (PMID:28396750)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5378843/)
  - [De novo mutation in ATP6V1B2 impairs lysosome acidification and causes dominant deafness-onychodystrophy syndrome - PubMed (PMID:24913193)](https://pubmed.ncbi.nlm.nih.gov/24913193/)
  - [DOORS syndrome and a recurrent truncating ATP6V1B2 variant - PubMed (PMID:32873933)](https://pubmed.ncbi.nlm.nih.gov/32873933/)
  - [Syndromic Deafness Gene ATP6V1B2 Controls Degeneration of Spiral Ganglion Neurons Through Modulating Proton Flux - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8568048/)