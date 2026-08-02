---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T21:03:53.808360'
end_time: '2026-08-01T21:15:02.874464'
duration_seconds: 669.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 9
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 13
  num_turns: 40
  total_cost_usd: 3.47850125
  session_id: 61bb04ee-ef9f-4517-9e5f-ba003eba19f9
  stop_reason: end_turn
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 9
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 9** covering all of the
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

# Comprehensive Research Report: Hypertrophic Cardiomyopathy 9 (CMH9; TTN‑related hypertrophic cardiomyopathy)

**Prepared:** 2026‑08‑01 · **Target entity:** MONDO:0013412 / OMIM #613765 · **Category:** Genetic (nominal Mendelian subtype)

> **Headline finding that governs this entire report.** CMH9 is a *nominal* OMIM/MONDO disease-series entity, not an established mechanistic disease. It rests on a single 1999 proband plus two variants from one later 96‑patient screen. ClinGen's Hereditary Cardiovascular Disease Gene Curation Expert Panel classifies **TTN–hypertrophic cardiomyopathy as Limited** (reaffirmed in the 2024/2025 reappraisal; a current ClinGen assertion dated 2025‑10‑28 carries the same call), and multiple case‑control datasets show **no enrichment of TTN variation in HCM versus controls**. The very large, well-validated **TTN–dilated cardiomyopathy** literature (ClinGen **Definitive**) is a *different* gene–disease relationship and must not be imported into this entry. Almost every section below therefore has two layers: (a) what is genuinely specific to CMH9 (very little), and (b) what is inherited from the HCM parent phenotype (most of it). I flag which is which throughout.

---

## 1. Disease Information

### 1.1 Overview

Hypertrophic cardiomyopathy 9 (CMH9) is the OMIM disease-series designation for hypertrophic cardiomyopathy (HCM) attributed to heterozygous variants in **TTN** (titin) on chromosome 2q31.2. MONDO defines it purely by gene attribution, not by any distinguishing clinical or mechanistic feature:

> "Any hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the TTN gene." — MONDO:0013412 definition (`MONDO:patterns/disease_series_by_gene`)

The entity originates from Satoh et al. (1999), who screened *TTN* in 82 HCM probands negative for the then-known sarcomere genes and found one heterozygous **c.2219G>T, p.Arg740Leu** substitution (PMID:10462489, *Biochem Biophys Res Commun* 262:411‑7):

> "A G to T transversion in codon 740, from CGC to CTC, replacing Arginine with Leucine was found in a patient. This mutation was not found in more than 500 normal chromosomes and increased the binding affinity of titin to alpha‑actitin [sic] in the yeast two‑hybrid assay. These observations suggest that the titin mutation **may cause HCM in this patient** via altered affinity to alpha‑actinin." *(HUMAN_CLINICAL + IN_VITRO; note the authors' own hedge)*

There is **no CMH9-specific clinical syndrome**. Reported patients present as ordinary nonsyndromic HCM. No TTN-specific hypertrophy pattern, age of onset, arrhythmic profile, or treatment response has ever been described.

### 1.2 Key identifiers

| Resource | Identifier |
|---|---|
| OMIM | **#613765** (CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 9; CMH9) |
| MONDO | **MONDO:0013412** (`hypertrophic cardiomyopathy 9`) |
| DOID | DOID:0110315 |
| MedGen / UMLS | MEDGEN:348780 / UMLS:C1861065 |
| MeSH (supplementary concept) | MESH:C566044 |
| GARD | GARD:0024921 |
| GTR condition | C1861065 ("Hypertrophic cardiomyopathy 9") |
| Gene | **TTN**, HGNC:12403, OMIM \*188840, NCBI Gene 7273, Ensembl ENSG00000155657, UniProt **Q8WZ42** |
| Parent MONDO classes | MONDO:0024573 (familial hypertrophic cardiomyopathy); **MONDO:0100494 (autosomal dominant titinopathy)**; equivalent to MONDO:0005045 ∧ (RO:0004003 *some* HGNC:12403) |
| ICD‑10‑CM | I42.1 (obstructive HCM) / I42.2 (other HCM) — no CMH9-specific code |
| ICD‑11 | BC43 hypertrophic cardiomyopathy block (familial‑genetic and non‑obstructive subcategories BC43.10 / BC43.11) — no CMH9-specific code |
| Orphanet | **No dedicated ORPHA code.** Familial isolated HCM (ORPHA:155) is flagged "NON RARE IN EUROPE" and is outside the Orphanet rare-disease nomenclature; ORPHA:217569 ("rare hypertrophic cardiomyopathy") is a group-of-disorders node with prevalence/inheritance "not specified" |

**Ontology suggestion for the KB `disease_term`:** MONDO:0013412 (exact). Do **not** substitute MONDO:0005045 (hypertrophic cardiomyopathy) — that is the umbrella entity.

### 1.3 Synonyms

CMH9; cardiomyopathy, familial hypertrophic, 9 (or type 9); hypertrophic cardiomyopathy type 9; TTN hypertrophic cardiomyopathy; hypertrophic cardiomyopathy caused by mutation in TTN. (All are EXACT synonyms in MONDO.)

### 1.4 Provenance of information

Disease-level aggregated resources only (OMIM, MONDO, ClinGen, ClinVar, GeneReviews) plus a handful of small primary case series. **No EHR/registry-derived, patient-level CMH9 cohort exists.** Because the entity is defined by gene attribution rather than a distinguishable phenotype, any EHR case-finding for "CMH9" would in practice retrieve generic HCM cases (I42.1/I42.2) plus a *TTN* genotype.

---

## 2. Etiology

### 2.1 Disease causal factors

**Claimed cause:** heterozygous rare missense variation in *TTN* — a **disputed** causal claim.

Three lines of causal claim exist, all thin:

1. **Z‑repeat missense (p.Arg740Leu)** — one proband, 1999 (PMID:10462489). Never replicated, never segregated.
2. **M‑line/A‑band‑transition Ig‑domain missense** — two variants in 96 sarcomere‑negative Japanese familial HCM probands, plus a medaka fish mutant (PMID:31628103).
3. **Titin‑truncating variants (TTNtv)** — the DCM mechanism — **explicitly not supported for HCM** (see §4.4).

**Counter-evidence is stronger than the positive evidence:**

- Herman et al. 2012, *N Engl J Med* 366:619‑28 (PMID:22335739): "the frequency of TTN mutations was significantly higher among subjects with dilated cardiomyopathy (54 of 203 [27%]) than among subjects with hypertrophic cardiomyopathy (3 of 231 [1%], P=3×10⁻¹⁶) or controls (7 of 249 [3%], P=9×10⁻¹⁴)." Note HCM (1%) was *below* controls (3%). Also: "Mutations associated with dilated cardiomyopathy were overrepresented in the titin A‑band but were **absent from the Z‑disk and M‑band regions** of titin" — i.e., precisely the two regions the CMH9 hypotheses invoke. *(HUMAN_CLINICAL)*
- Bos et al. 2006, *Mol Genet Metab* 88:78‑85 (PMID:16352453): 389 unrelated HCM patients, targeted analysis of the HCM‑associated *TTN* exons (2, 3, 4, 14) — "**No TTN mutations were detected.**" *(HUMAN_CLINICAL; negative replication)*
- Wang et al. 2017, *Can J Cardiol* 33:1292‑7 (PMID:28822653): 529 Chinese HCM vs 307 controls — "We identified 13 and 8 TTNtv in patients with HCM (13 of 529 [2.5%]) and controls (8 of 307 [2.6%]) … **The prevalence of TTNtv in patients with HCM and in healthy controls was comparable** (P = 0.895)." *(HUMAN_CLINICAL)*
- ClinGen HCM GCEP reappraisal (Hespe, Waddell, Asatryan et al., *JACC* 2025;85(7):727‑740, doi:10.1016/j.jacc.2024.12.010; preprint PMID:39132495 / PMC11312670): *TTN* scored **1.2 genetic + 5.5 experimental = 6.7 points → Limited**. Panel narrative: "the majority are missense without functional data or located in an exon with low percent spliced in (PSI) cardiac tissue"; "no excess TTN variants were noted in cases compared to controls in 2 studies"; "evidence for *TTN* variants causing HCM remained limited, rather than being reclassified as disputed." *(OTHER / expert-panel curation)*

**Interpretation for the KB:** model *TTN* with `relationship_type: DISPUTED`, and record the mechanism nodes at `mechanism_confidence: HYPOTHETICAL`.

### 2.2 Risk factors

**Genetic.**
- *TTN* rare missense variation — disputed (above).
- **Background rare-variant burden is the confounder.** Titin is the largest human protein (~34,350 aa canonical; up to ~35,991 aa inferred‑complete isoform; ~364 exons in the meta‑transcript NM_001267550). Every genome carries multiple rare *TTN* missense alleles; ~2–3% of unselected individuals carry a truncating allele (3% of controls in PMID:22335739). Any sufficiently large candidate-gene screen will therefore *find* rare *TTN* variants irrespective of causality — the core methodological problem with CMH9.
- **Real HCM risk factors (parent phenotype):** pathogenic variants in the 8 definitive sarcomere genes — MYBPC3 (~50% of genotype‑positive), MYH7 (~33%), TNNI3 (~5%), TNNT2 (~4%), then TPM1, ACTC1, MYL2, MYL3 (<3% each) (GeneReviews, PMID:20301725). The 2025 ClinGen reappraisal recognises 29 genes at moderate/strong/definitive for HCM or isolated LVH (MYBPC3, MYH7, TNNT2, TNNI3, TNNC1, TPM1, ACTC1, MYL2, MYL3, ACTN2, CSRP3, FHOD3, FLNC, PRKAG2, PLN, DES, FHL1, LAMP2, GLA, CACNA1C, TTR, PTPN11, RAF1, RIT1, and others).
- **Polygenic background** modulates penetrance and expressivity in HCM generally; low-penetrance sarcomere variants contribute additive risk (*Circulation* 2025, "Low Penetrance Sarcomere Variants Contribute to Additive Risk in Hypertrophic Cardiomyopathy").
- **Modifier claim specific to TTN:** TTNtv may be an *outcome* modifier rather than a cause — see §4.5.

**Environmental / demographic (parent phenotype; none TTN‑specific).**
- Age (penetrance is age-dependent; typical onset adolescence–early adulthood).
- Male sex (over-represented in HCM cohorts; adverse events occur earlier in male *TTN* carriers in the DCM setting, PMID:22335739).
- Intense competitive athletic training — a *trigger* for arrhythmic events and a differential-diagnosis confounder ("athlete's heart"), not an initiating cause.
- Hypertension and aortic stenosis are **phenocopy** causes of LVH, not CMH9 risk factors.
- No toxin, infectious, occupational, or dietary exposure has ever been linked to CMH9. **Not applicable / no data.**

### 2.3 Protective factors

**No CMH9-specific protective genetic or environmental factor has been reported.** For HCM generally: avoidance of burst/extreme exertion and of dehydration/volume depletion in LVOT-obstructive physiology; blood-pressure control; avoidance of pure vasodilators and high-dose diuretics in obstructive disease. These are *management* rather than validated primary prevention. No protective allele is documented in gnomAD-scale data.

### 2.4 Gene–environment interactions

No CMH9-specific GxE data. In the broader titin field, the best-characterised GxE is in **DCM, not HCM**: TTNtv carriers show a stress- or exposure-dependent phenotype (alcohol, peripartum, chemotherapy, atrial fibrillation, hypertension; e.g. *Nat Cardiovasc Res* 2024, "Titin truncating variants, cardiovascular risk factors and the risk of atrial fibrillation and heart failure"), and heterozygous *Ttn*-truncation mice are normal at baseline but decompensate under angiotensin II/isoproterenol or transverse aortic constriction (PMID:26504781; MODEL_ORGANISM). **Do not transfer this to CMH9** — it is DCM biology.

---

## 3. Phenotypes

No phenotype in this list is TTN-specific; all are inherited from the HCM parent phenotype, with the exception of the diastolic-dysfunction emphasis that comes from the medaka model. Frequencies below are HCM-cohort figures (GeneReviews PMID:20301725; 2024 AHA/ACC guideline PMID:38718139) and should be curated as **parent-phenotype frequencies, not CMH9 frequencies**.

| Phenotype | HPO term | Type | Onset | Course | Frequency (HCM overall) |
|---|---|---|---|---|---|
| Left ventricular hypertrophy (LV wall ≥15 mm adults; z>3 children) | **HP:0001712** Left ventricular hypertrophy | Clinical sign / imaging | Adolescence–early adulthood typical; any age | Progressive then plateau | Obligate (defining) |
| Asymmetric septal hypertrophy | **HP:0001670** Asymmetric septal hypertrophy | Imaging | as above | Stable/progressive | Most |
| Myocardial sarcomeric (myofibrillar) disarray | **HP:0031333** Myocardial sarcomeric disarray | Histologic | — | — | Histological hallmark |
| LV diastolic dysfunction | **HP:0025168** Left ventricular diastolic dysfunction | Functional | Early, often pre-hypertrophic | Progressive | Very frequent |
| LV outflow tract obstruction | **HP:0031573** Left ventricular outflow tract obstruction | Hemodynamic | Adult | Dynamic/provocable | **25–30%** at rest |
| Exertional dyspnea | **HP:0002875** Exertional dyspnea | Symptom | Adult | Progressive | Common (leading symptom) |
| Chest pain / angina | **HP:0100749** Chest pain | Symptom | Adult | Episodic | Common |
| Palpitations | **HP:0001962** Palpitations | Symptom | Adult | Episodic | Common |
| Syncope / presyncope | **HP:0001279** Syncope | Symptom | Adolescent–adult | Episodic | Important SCD risk marker |
| Atrial fibrillation | **HP:0005110** Atrial fibrillation | Arrhythmia | Adult | Recurrent→permanent | **~60% by age 60** if diagnosed by 40 |
| Ventricular tachycardia | **HP:0004756** Ventricular tachycardia | Arrhythmia | Any | Episodic | Substantial minority |
| Sudden cardiac death | **HP:0001645** Sudden cardiac death | Outcome | Adolescent–young adult peak | Catastrophic | ~6% of cohorts experience SCD/aborted arrest/appropriate ICD therapy; HCM = 5–14% of SCD in competitive athletes |
| Systolic dysfunction / "burnt-out" end-stage phase | **HP:0001635** Congestive heart failure; **HP:0012722**? (use HP:0005162 Abnormal left ventricular function) | Clinical | Late | Progressive | LV systolic dysfunction ~8% |
| Myocardial fibrosis (LGE on CMR) | **HP:0001637** Abnormal myocardium morphology (no precise HP term for LGE) | Imaging/histology | Mid | Progressive | Common; prognostic |
| Mitral regurgitation (SAM-mediated) | **HP:0001653** Mitral regurgitation | Clinical | Adult | Dynamic | Common in obstructive HCM |
| Elevated NT‑proBNP / troponin | **HP:0031185** Abnormal circulating creatine kinase?—prefer LOINC (NT‑proBNP LOINC:33762‑6; hs‑cTnT LOINC:67151‑1) | Laboratory | — | — | Common; prognostic |

**Quality-of-life impact.** No CMH9-specific QoL data. In HCM generally, exertional dyspnea, chest pain and fatigue drive impairment; the SEQUOIA‑HCM aficamten trial used the **Kansas City Cardiomyopathy Questionnaire (KCCQ)** and pVO₂ as functional endpoints, with ~60% of aficamten-treated vs 24% of placebo patients improving NYHA class. Additional QoL burdens: exercise restriction counselling, ICD-related anxiety, and cascade-screening implications for relatives. Instruments in use: KCCQ, SF‑36, EQ‑5D, HCM Symptom Questionnaire (HCMSQ).

**Severity/progression descriptors (HCM parent).** Severity: variable, from lifelong asymptomatic to end-stage HF. Progression: slow and progressive with an episodic arrhythmic overlay. Penetrance 50–62% in P/LP heterozygotes, gene-dependent (~32% MYL3 to ~69% ACTC1) (PMID:20301725). **None of these figures has ever been measured for TTN carriers.**

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**TTN** (titin), HGNC:12403, OMIM \*188840, 2q31.2, UniProt Q8WZ42. Encodes the giant sarcomeric filament spanning the half-sarcomere from Z‑disc to M‑band (>1 µm), 3–4.2 MDa depending on splice isoform (N2B, N2BA, novex isoforms). Functional segments: Z‑disc (Z‑repeats binding α‑actinin, telethonin/TCAP anchoring), I‑band (elastic spring: tandem Ig, N2B/N2BA, PEVK), A‑band (super-repeats binding myosin/MyBP‑C), M‑band (titin kinase domain, MURF1/MURF2 binding, obscurin/myomesin interface).

**GO annotations to use:** GO:0008307 structural constituent of muscle; GO:0042805 actinin binding; GO:0031430 M band; GO:0030018 Z disc; GO:0030016 myofibril; GO:0055003 cardiac myofibril assembly; GO:0016567 protein ubiquitination; GO:0014898 cardiac muscle hypertrophy in response to stress.

### 4.2 The reported CMH9 alleles

| Variant | HGVS | Location | Reported | Evidence | ClinVar |
|---|---|---|---|---|---|
| **p.Arg740Leu** | NM_001267550.2:c.2219G>T; NP_001254479.2:p.Arg740Leu; NC_000002.12:g.178785999C>A; rs28933405 | Z‑disc **Z‑repeat** region | Satoh 1999, 1 proband/82 (PMID:10462489) | Absent from >500 normal chromosomes; ↑α‑actinin binding (~40%) in yeast two‑hybrid | **VCV000012649**, "Pathogenic", **review status 0 stars — "no assertion criteria provided"**, single OMIM submission, last evaluated **1999‑08‑27**; no population frequency displayed |
| **p.Ser30186Ala** | exon 301, TCT→GCT | Ig domain near M‑line/A‑band transition | Medaka/human study (PMID:31628103), 96 familial HCM probands | ↑MURF1 binding; ↑ubiquitin-mediated titin degradation (IN_VITRO) | — |
| **p.Asp30994Asn** | exon 306, GAT→AAT | Ig domain **within the MURF1‑binding site** | same | same | — |
| **p.Arg6745Cys** | c.20233C>T, exon 80 | I‑band region | Chinese family, WES, *Int J Gen Med* 2025 (PMID:39895828) | Present in affected relatives, absent in healthy relatives except one young child | Novel; classification not established |

**Critical caveat on the R740L ClinVar record:** its "Pathogenic" label is a **0‑star OMIM-derived assertion from 1999** predating ACMG/AMP criteria. Under ACMG/AMP 2015 rules the variant would today, at best, be a VUS: PS3 is weak (yeast two‑hybrid interaction assay, not a disease-relevant functional readout), PM2 support was "absent from 500 chromosomes" (not gnomAD-scale), and there is **no PP1 segregation and no PS4 case-control enrichment**. gnomAD frequency is not displayed on the ClinVar record and could not be retrieved programmatically for this report — **flag as a gap to fill before curating any allele-frequency claim.**

### 4.3 Variant classes and functional consequences

- **Type:** all CMH9 claims are **missense**. This matters: the disease-validated *TTN* mechanism (DCM) is **truncating** (nonsense/frameshift/canonical splice) with haploinsufficiency/poison-peptide effects in high‑PSI A‑band exons (Roberts et al. 2015, *Sci Transl Med*, PMID:25589632).
- **Proposed functional consequence #1 (gain of function / altered binding):** R740L *increases* titin–α‑actinin affinity (~40%) — an unusual "too‑tight" gain-of-binding, not loss of function.
- **Proposed functional consequence #2 (enhanced degradation):** M‑line‑proximal Ig missense increases MURF1 binding and ubiquitin-mediated titin turnover — effectively a *localised loss of titin protein*.
- These two proposals are **mechanistically incompatible with each other** and implicate opposite ends of the molecule. They should be curated as two separate, non-merged `mechanistic_hypotheses` groups.
- **Germline** in all cases. Somatic *TTN* variation is irrelevant here (TTN is a well-known false-positive "long gene" hit in tumour mutation datasets — do not cite COSMIC/TCGA for this entity).

### 4.4 Why truncating variants are excluded

TTNtv frequencies: DCM 27% vs HCM 1% vs controls 3% (PMID:22335739); HCM 2.5% vs controls 2.6% (PMID:28822653). PSI/exon-usage analysis (PMID:25589632) established that only constitutively expressed (high‑PSI) A‑band TTNtv are DCM-relevant — "the most common genetic cause of DCM in ambulant patients in the community." The ClinGen panel found the only truncating-type HCM case evidence to be *one* A‑band frameshift (PSI 100%) and *one* I‑band termination (PSI 100%) — two isolated observations against a high background rate.

### 4.5 Modifier hypothesis (a separable claim)

Wang et al. 2017 (PMID:28822653): among 529 HCM patients, TTNtv carriers had cardiovascular death in 3/13 (23.1%) vs 39/516 (7.6%) in non-carriers, **adjusted HR 6.88 (95% CI 2.04–23.20; P=0.002)**. Authors: "Our study suggests that TTNtv might be a genetic modifier of HCM and confers increased risk for cardiovascular death." **Single cohort, 3 events, unreplicated.** Curate as `CONTROVERSY`, not as a causal mechanism. Note the logical structure: *TTN* can be simultaneously (a) not an HCM gene and (b) a prognostic modifier within HCM.

### 4.6 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes for CMH9:** none identified. **No data.**
- **Epigenetics:** no CMH9-specific methylation/histone data. Generic HCM myocardium shows DNA methylation and ncRNA remodelling, but nothing titin- or CMH9-specific is published. **No data.**
- **Chromosomal abnormalities:** not a mechanism here. Large *TTN* CNVs are rare; GeneReviews states "large deletions and duplications are not a major cause of nonsyndromic HCM." Chromosomal microarray/karyotype have no role.

---

## 5. Environmental Information

- **Environmental factors:** none established for CMH9. **Not applicable.**
- **Lifestyle factors:** relevant only as symptom/arrhythmia modifiers of the HCM phenotype (exertion, dehydration, alcohol, stimulants). For titin biology generally, mechanical/haemodynamic load is the physiologically meaningful "environment" — titin is a load-sensing molecule — but no CMH9 load-interaction study exists.
- **Infectious agents:** **Not applicable.** No infectious trigger implicated.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain — as claimed, with confidence labels

```
[HYPOTHETICAL, MOLECULAR]
Rare heterozygous TTN missense variant in a sarcomere-negative HCM patient
   │  (ascertainment: residual, gene-elusive HCM — candidate-gene design)
   ├──► HYPOTHESIS A (Z-disc):  ↑ titin Z-repeat binding to α-actinin (~40%, Y2H)
   │        └─► perturbed Z-disc assembly / Z-disc mechanosensing  [UNBRIDGED]
   │                └─► ??? ─────────────────────────┐
   └──► HYPOTHESIS B (M-line):  ↑ titin Ig-domain binding to MURF1  │
            └─► ↑ ubiquitin-mediated titin degradation              │
                 └─► M-line disassembly, fewer myofibrils,          │
                     stiffer (N2B-shifted) titin isoforms  [fish]   │
                          └─► ??? ────────────────────────────────► │
                                                                    ▼
                                          [TISSUE] Hypertrophic remodeling of the LV
                                          (wall thickening + myocyte disarray +
                                           impaired diastolic filling)
                                                    │
                                                    ▼
                                    Generic HCM downstream cascade
                            (see kb/modules/cardiomyopathy_maladaptive_remodeling)
```

**The step marked `???` is entirely unbridged in both hypotheses.** No intermediate signalling has been demonstrated linking either binding perturbation to a hypertrophic transcriptional program in human cardiomyocytes.

### 6.2 Hypothesis A — altered Z‑disc / α‑actinin interaction

Titin's N‑terminus spans the Z‑disc; the central **Z‑repeats** bind the C‑terminal calmodulin-like domain of **α‑actinin‑2 (ACTN2)**, anchoring the filament and creating a mechanosensing hot spot. Arg740 lies in this Z‑repeat region. The 1999 claim is that a ~40% affinity increase alters Z‑disc assembly or mechanotransduction.

Evidence base: **one yeast two-hybrid experiment**. No cardiac cell, tissue, or animal data for this variant. Independent support that Z‑disc/α‑actinin‑2 disruption *can* cause human myocardial mechanical dysfunction exists (e.g., *Circ Heart Fail*/PMC10572656, "Disruption of Z‑Disc Function Promotes Mechanical Dysfunction in Human Myocardium: Evidence for a Dual Myofilament Modulatory Role by Alpha‑Actinin 2"), and **ACTN2** itself is a ClinGen-recognised HCM gene — but that supports the *pathway's plausibility*, not this variant's causality. Notably, Herman 2012 found DCM-associated truncations were *absent* from the Z‑disc region, and Bos 2006 found nothing at all when directly resequencing the Z‑disc-encoding exons in 389 HCM patients.

**GO:** GO:0042805 actinin binding (modifier INCREASED); GO:0030018 Z disc; GO:0055003 cardiac myofibril assembly.

### 6.3 Hypothesis B — titin/MURF1 signalling and enhanced titin turnover

The titin M‑band harbours the **titin kinase** domain, now understood to be a catalytically inactive **pseudokinase scaffold** that recruits the E3 ubiquitin ligases **MURF1 (TRIM63)** and MURF2, coupling sarcomeric mechanics to ubiquitin-dependent turnover and myofibril trophicity (Bogomolovas et al., *Open Biol* 2014;4:140041, doi:10.1098/rsob.140041). *TRIM63* is itself a recognised HCM-associated gene.

The medaka **non‑spring heart (nsh)** mutant carries an Ig-domain missense (D23186V, exon 204) at the M‑line/A‑band transition (PMID:31628103, *Dis Model Mech* 12:dmm041103):

> "The nsh homozygotes had fewer myofibrils, disrupted sarcomeres and expressed pathologically stiffer titin isoforms. In addition, the nsh heterozygotes showed M‑line disassembly that is similar to the pathological changes found in HCM." *(MODEL_ORGANISM)*

> "Screening of mutations in 96 unrelated patients with familial HCM, who had no previously implicated mutations in known sarcomeric gene candidates, identified two mutations in Ig domains close to the M‑line region of titin. In vitro studies revealed that the mutations found both in medaka fish and in familial HCM **increased binding of titin to muscle‑specific ring finger protein 1 (MURF1) and enhanced titin degradation by ubiquitination**. These findings implicate an impaired interaction between titin and MURF1 as a novel mechanism underlying the pathogenesis of HCM." *(IN_VITRO + MODEL_ORGANISM)*

Mechanistic details from the full text: atrial systolic/diastolic velocities fell from ~183 µm/s (WT) to ~64 µm/s (nsh); N2B (stiff) isoform expression increased, i.e., reduced elasticity and increased passive stiffness — a biophysically coherent route to **diastolic dysfunction**; MURF1/MURF2 catalysed multi-ubiquitination of the titin fragment in vitro; mutant constructs showed lower steady-state protein levels. The authors state a key limitation: "since the medaka *TTN* gene is very large, we were unable to clone the full-length cDNA (~15 kb) to perform the rescue experiments" — **the model lacks genetic rescue.** The human arm presents family pedigrees, but ClinGen's independent assessment of the total case-level evidence remained Limited.

**GO:** GO:0016567 protein ubiquitination (INCREASED); GO:0030239 myofibril assembly (DECREASED); GO:0031430 M band; GO:0061077 chaperone-mediated protein folding (n/a); GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process.

### 6.4 Downstream (inherited from the HCM parent phenotype, not TTN-specific)

Increased sarcomeric energetic cost and Ca²⁺ sensitisation → myocyte hypertrophy and disarray → interstitial and replacement fibrosis → microvascular dysfunction/ischemia → impaired relaxation and elevated filling pressures → LVOT obstruction (± SAM of the mitral valve) → arrhythmogenic substrate → AF, VT, SCD, and in a minority the end-stage systolic ("burnt-out") phase. This is exactly the chain captured by the dismech module `cardiomyopathy_maladaptive_remodeling`; **a `conforms_to` link from CMH9 is not warranted** because the disease-specific edges *into* that chain are hypothetical.

### 6.5 Cell types, compartments, metabolism, immunity

- **Cell types:** **CL:0000746** cardiac muscle cell (cardiomyocyte); secondarily **CL:0002548** fibroblast of cardiac tissue (fibrotic remodelling), **CL:0002144** capillary endothelial cell (microvascular dysfunction).
- **Subcellular:** **GO:0030017** sarcomere; **GO:0030018** Z disc; **GO:0031430** M band; **GO:0030016** myofibril; **GO:0005634** nucleus (titin N‑terminus/Z‑disc mechanosignalling relays, e.g., MLP/CSRP3 shuttling); **GO:0005739** mitochondrion (energetic stress, downstream).
- **Metabolic changes:** no CMH9-specific metabolomics. HCM generally shows impaired myocardial energetics (reduced PCr/ATP by ³¹P‑MRS), a shift toward glucose utilisation, and increased ATP cost of tension. **No titin-specific data.**
- **Immune involvement:** none primary. Sterile inflammation accompanies fibrotic remodelling but is not disease-defining. **Not applicable as a mechanism.**
- **Tissue damage mechanisms:** myocyte hypertrophy/disarray, interstitial + replacement fibrosis, microvascular ischemia. Generic.
- **Molecular profiling (transcriptomics/proteomics/metabolomics/lipidomics/single-cell/spatial/CRISPR screens):** **No CMH9-specific dataset exists in GEO, ArrayExpress, PRIDE, MetaboLights, HCA, or DepMap.** Titin exon-usage/PSI resources from the DCM field (PMID:25589632; *Inferring disease course from differential exon usage in the wide titinopathy spectrum*, PMC11514934) are methodologically relevant for interpreting *TTN* variants but are not CMH9 data. This is a genuine and complete gap.

---

## 7. Anatomical Structures Affected

**Organ level**
- Primary: **heart** — UBERON:0000948; specifically **left ventricle** UBERON:0002084 and **interventricular septum** UBERON:0002094 (asymmetric septal hypertrophy).
- Secondary: **left atrium** UBERON:0002079 (dilation, AF substrate); **mitral valve** UBERON:0002135 (SAM, regurgitation); **cardiac conduction system** UBERON:0004146; pulmonary circulation (post-capillary pulmonary hypertension); systemic embolic targets — **brain** UBERON:0000955 (cardioembolic stroke).
- Body systems: **cardiovascular** primary. Note that titin is also expressed in **skeletal muscle** UBERON:0001134 — skeletal myopathy is not a feature of CMH9 as reported, but is central to other titinopathies (HMERF, LGMD R10, Salih myopathy) under the shared MONDO parent `autosomal dominant titinopathy` (MONDO:0100494). **No skeletal-muscle phenotype has been described in CMH9 patients.**

**Tissue / cell level**
- **Cardiac muscle tissue** UBERON:0001133 / myocardium UBERON:0002349.
- **CL:0000746** cardiac muscle cell — the primary affected population; **CL:0002548** cardiac fibroblast; **CL:0002144** capillary endothelial cell.

**Subcellular** — GO:0030017 sarcomere, GO:0030018 Z disc, GO:0031430 M band, GO:0030016 myofibril.

**Localization / lateralization** — Bilateral in the sense of biventricular potential, but the phenotype is characteristically **left-sided and regionally asymmetric** (basal anteroseptal predominance; apical, midventricular, and concentric variants occur). Right ventricular involvement is possible but secondary. Use **HP:0001670** (asymmetric septal hypertrophy) to capture asymmetry.

---

## 8. Temporal Development

**Onset.** No CMH9-specific onset data (n≈4 reported probands). HCM parent phenotype: onset typically **adolescence or early adulthood**, but ranges from infancy to the eighth decade; onset is **insidious**, detected on screening ECG/echo or after a symptomatic/arrhythmic event. HPO onset terms: **HP:0003581** Adult onset / **HP:0011462** Young adult onset / **HP:0003621** Juvenile onset (choose per case; for CMH9 the honest annotation is *variable/unknown*).

**Progression / staging.** Recognised HCM stages: (1) genotype‑positive/phenotype‑negative (subclinical; may show impaired relaxation, ECG changes, crypts before hypertrophy); (2) classic phenotype with preserved EF ± obstruction; (3) adverse remodelling with AF, progressive fibrosis, worsening diastolic failure; (4) end-stage/"burnt-out" with systolic dysfunction (~8% of cohorts) requiring advanced therapies. Rate is **slow and variable over decades**, punctuated by episodic arrhythmic events. Duration: **chronic, lifelong** (HP:0003679 progressive; HP:0003676 progressive disorder).

**Patterns.** No spontaneous remission. Treatment-induced *symptomatic* remission is achievable (myectomy, alcohol septal ablation, cardiac myosin inhibitors) but does not reverse the genotype; regression of hypertrophy with myosin inhibitors is partial and drug-dependent. **Critical periods:** adolescence/young adulthood (peak SCD risk, athletic exposure) and the period around phenotype conversion in genotype-positive relatives — the rationale for serial screening every 1–2 years (see §13).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**CMH9-specific:** unquantifiable. Cumulative published cases ≈ **4 probands worldwide** (1 Japanese in 1999; 2 Japanese in 2019; 1 Chinese family in 2025). Appropriate `prevalence_class`: **`CASES_IN_LITERATURE`** with `measure_type: CASES_IN_LITERATURE` and a note that the entity's validity is disputed. Do **not** assign a numeric rate.

**HCM parent phenotype (for context only):**
- Classic estimate **1 in 500** (~200 per 100,000) from echocardiographic screening (CARDIA).
- Contemporary US administrative-claims estimate (*JACC: Advances* 2025, "Epidemiology of Hypertrophic Cardiomyopathy in the United States From 2016 to 2023"): **1 in 327**, ~832,956 US cases — higher than classic estimates, reflecting ascertainment and awareness.
- Range across literature 1:500–1:3,000 depending on method; genotype-based estimates (P/LP variant carriage) suggest higher latent carriage with incomplete penetrance.

### 9.2 Genetic parameters

- **Inheritance:** **autosomal dominant** — **HP:0000006**. Recorded as such in ClinGen's TTN‑HCM assertion and asserted by OMIM. But note: the index CMH9 observation was a single proband with **no segregation data**; support for dominance in this specific entity is `PARTIAL`, inherited from HCM generally rather than demonstrated for *TTN*.
- **Penetrance:** unknown for CMH9. HCM overall: **50–62%** in P/LP heterozygotes, age-dependent, gene-specific (~32% MYL3 to ~69% ACTC1) (PMID:20301725). Population-based genotype-first studies show substantially *lower* penetrance than clinic-ascertained estimates.
- **Expressivity:** highly variable with marked intrafamilial variability (HCM generally).
- **Anticipation:** **Not applicable** — no repeat expansion mechanism.
- **Germline mosaicism:** possible in principle for HCM (parental gonadal mosaicism reported); **no CMH9 report**.
- **Founder effects:** none for CMH9. (Contrast: founder TTNtv exist for DCM, e.g. TTN:c.12478del in Slovenia — DCM, not HCM.)
- **Consanguinity:** no role established; dominant mechanism.
- **Carrier frequency:** not a meaningful parameter for a dominant, disputed entity. gnomAD frequency of R740L was not retrievable for this report — **explicit gap**.

### 9.3 Population demographics

- **Affected populations:** the three primary reports are **East Asian** (2 Japanese cohorts, 1 Chinese family). This almost certainly reflects **ascertainment by the research groups involved**, not a genuine ancestry effect, and should be curated as such rather than as a population-prevalence claim.
- **Geographic distribution:** none established. No variant shows geographic clustering.
- **Sex ratio:** no CMH9 data. HCM cohorts are male-predominant (~60:40) with women diagnosed later and often more symptomatic.
- **Age distribution:** no CMH9 data; HCM parent as in §8.

---

## 10. Diagnostics

**There is no CMH9-specific diagnostic test or pathway.** Diagnosis is (1) diagnose HCM, then (2) genotype — and the *TTN* finding, if any, is currently **not reportable as causal**.

### 10.1 Clinical tests (HCM parent; 2024 AHA/ACC guideline, PMID:38718139)

| Modality | Findings | Codes |
|---|---|---|
| **Transthoracic echocardiography** (first-line) | LV wall ≥15 mm (adults) or ≥13 mm with family history; z>3 in children; SAM; dynamic LVOT gradient (rest + Valsalva + exercise provocation); diastolic indices | NCIT:C16816 (Echocardiography) |
| **Cardiac MRI with LGE** | Hypertrophy distribution, apical/mid variants, myocardial fibrosis burden (prognostic), phenocopy discrimination (e.g., amyloid, Fabry) | NCIT:C16809 (Magnetic Resonance Imaging) |
| **12-lead ECG** | LVH voltage, repolarisation abnormalities, deep T inversions (apical HCM), pathologic Q waves; often abnormal before hypertrophy | NCIT:C38053 (Electrocardiography) |
| **Ambulatory ECG (24–48 h Holter)** | NSVT (SCD risk marker), AF detection | NCIT:C38050? — use NCIT:C38053 with modifier |
| **Exercise testing / CPET** | Functional capacity, pVO₂, exercise-provocable obstruction, blood-pressure response (SCD risk) | NCIT:C38082 (Exercise Stress Test) |
| **Biomarkers** | NT‑proBNP (LOINC:33762‑6), hs‑troponin T (LOINC:67151‑1) — prognostic, not diagnostic. Rule out phenocopies: **α‑galactosidase A activity/GLA** for Fabry; **serum/urine free light chains + technetium‑pyrophosphate scintigraphy** for ATTR amyloid; creatine kinase for Danon/glycogenoses | LOINC as listed |
| **Endomyocardial biopsy** | Rarely needed; shows myocyte hypertrophy, **myofibrillar disarray (HP:0031333)**, interstitial fibrosis. Used mainly to confirm infiltrative phenocopies | NCIT:C15680 (Biopsy) |

### 10.2 Genetic testing

- **Recommended approach (2024 AHA/ACC):** HCM-focused **multigene panel** in the proband, with evaluation by a genetic counsellor before and after testing; panels should include **phenocopy genes** (GLA, LAMP2, PRKAG2, TTR, PTPN11/RASopathies, FHL1, DES, CACNA1C, ACTN2, FLNC, FHOD3, ALPK3). Diagnostic yield ~30% in unselected HCM, ~60% in familial cases.
- **Cascade testing:** offered to first-degree relatives **only when a P/LP variant is identified in the proband**. Genotype-positive/phenotype-negative relatives get serial imaging; ICDs are **not** indicated for them, and they may participate in competitive sport.
- **WES/WGS:** second-line when panels are negative and a syndromic/phenocopy diagnosis is suspected; WGS adds little for *TTN* interpretation given the background variant burden.
- **Single-gene testing:** appropriate only for a known familial variant.
- **CMA / karyotype / FISH:** **not indicated** — large CNVs are not a significant cause of nonsyndromic HCM.
- **mtDNA testing:** consider for maternally inherited LVH (MT‑TI and other mt‑tRNA variants).
- **Repeat expansion testing:** **not applicable**, except Friedreich ataxia (FXN GAA) in the syndromic differential.
- **The TTN-specific interpretive rule:** a rare *TTN* variant on an HCM panel **should not be reported as an established cause of the patient's hypertrophy.** For any *TTN* variant, evaluate exon **PSI** (percent-spliced-in) and domain location — but note that even high‑PSI TTNtv are DCM-, not HCM-, associated.

### 10.3 Omics-based diagnostics

**RNA-seq** on blood/muscle can resolve splice-impact of candidate *TTN* variants and is the one omics modality with real utility here. Proteomics, metabolomics, epigenomics, liquid biopsy: **no established diagnostic role. Not applicable.**

### 10.4 Clinical criteria and differential diagnosis

**Diagnostic criterion (2024 AHA/ACC):** maximal LV wall thickness **≥15 mm** in any myocardial segment (or **≥13 mm** with a positive family history or positive genotype), by any imaging modality, **not explained solely by abnormal loading conditions**. Pediatric: z-score >3 (or >2 with family history/genotype).

**Differential (all must be excluded):**
- **Hypertensive heart disease**, **aortic stenosis** — loading-condition LVH.
- **Athlete's heart** — concentric mild LVH with *increased* LV cavity size, normal diastolic function, regression with deconditioning.
- **Cardiac amyloidosis** (ATTR/AL) — low voltage with LVH, apical sparing on strain, positive PYP scan.
- **Fabry disease** (GLA) — low α‑Gal A, prominent inferolateral LGE, extracardiac features.
- **Danon disease** (LAMP2), **PRKAG2 glycogen storage** — pre-excitation, conduction disease.
- **RASopathies** (Noonan/PTPN11, RAF1, RIT1; Costello) — dysmorphology, pulmonary valve stenosis.
- **Pompe disease**, **Friedreich ataxia**, **desminopathy**, **mitochondrial cardiomyopathy**, **Timothy syndrome (CACNA1C)**.

### 10.5 Screening

- **Cascade clinical screening** of first-degree relatives with ECG + echo, repeated every **1–2 years** (more often in adolescence), regardless of genotype availability.
- **Newborn screening:** not applicable.
- **Population carrier screening:** not applicable for a dominant, low-penetrance, disputed entity.

---

## 11. Outcome / Prognosis

**No CMH9-specific outcome data exist.** All figures below are for HCM overall and must be curated as parent-phenotype prognosis.

- **Mortality:** contemporary HCM-related mortality in specialist centres is ~0.5–1%/year, far below the 2–4%/year of older referral-bias-era series. HCM remains a leading cause of SCD in young athletes (5–14% of cases).
- **Survival:** with modern management, life expectancy in many HCM patients approaches that of the general population; the end-stage phase (~8% with systolic dysfunction) carries substantially worse survival and may require transplant.
- **Composite burden:** SHaRe registry (Ho et al., *Circulation* 2018;138:1387‑1398, **PMID:30297972**; 4,591 patients, 2,763 genotyped, mean follow-up 5.4±6.9 y) established that **sarcomere-variant-positive** patients have earlier onset and a **higher lifetime burden** of adverse events (arrhythmias, HF, AF, stroke, death) than sarcomere-negative patients. *This is directly relevant framing for CMH9*: the reported CMH9 patients are by definition **sarcomere-negative** on established genes, which is the *lower*-risk SHaRe stratum — another reason not to assume a distinct severe TTN-HCM phenotype.
- **Morbidity/disability:** exercise intolerance, AF (up to ~60% by age 60 in early-diagnosed patients) with elevated stroke risk requiring anticoagulation irrespective of CHA₂DS₂‑VASc, ICD-related morbidity, and activity restriction.
- **QoL instruments:** KCCQ, SF‑36, EQ‑5D, HCMSQ. **No CMH9-specific QoL study.**
- **Complications:** SCD/VT, AF and cardioembolic stroke, progressive HF, infective endocarditis (rare, with SAM/MR), pregnancy-related decompensation (maternal mortality is nonetheless low, **0.2%**, GeneReviews PMID:20301725).
- **Prognostic factors (HCM):** maximal wall thickness, LV apical aneurysm, extensive LGE on CMR, unexplained syncope, NSVT, family history of SCD, abnormal BP response to exercise, LVEF <50%, left atrial size — all integrated in the **ESC HCM Risk‑SCD** calculator and the AHA/ACC risk-marker approach.
- **TTN-specific prognostic claim:** the single unreplicated finding that **TTNtv carriage predicts cardiovascular death within HCM (adjusted HR 6.88)** (PMID:28822653). Treat as hypothesis-generating.

---

## 12. Treatment

**No CMH9-specific, genotype-directed therapy exists.** Management is standard HCM management (2024 AHA/ACC/AMSSM/HRS/PACES/SCMR guideline, PMID:38718139).

### 12.1 Pharmacotherapy

| Therapy | Mechanism | Indication | NCIT suggestion |
|---|---|---|---|
| **Beta-blockers** (metoprolol, bisoprolol, atenolol) | β₁-adrenergic blockade → ↓ contractility, ↓ HR, ↑ diastolic filling | First-line for symptomatic obstructive and non-obstructive HCM | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` NCIT:C2019 Adrenergic beta-Antagonist |
| **Non-dihydropyridine CCBs** (verapamil, diltiazem) | L-type Ca²⁺ channel blockade | Beta-blocker intolerance/failure; avoid in severe obstruction + hypotension | NCIT:C15986 + CHEBI:9948 verapamil |
| **Disopyramide** | Class Ia antiarrhythmic, negative inotrope | Add-on for refractory obstruction (with AV-nodal blocker) | NCIT:C15986 + CHEBI:4657 disopyramide |
| **Mavacamten** | First-in-class **cardiac myosin inhibitor**; reduces actin–myosin cross-bridge formation → ↓ hypercontractility, ↓ LVOT gradient | Symptomatic obstructive HCM (FDA 2022); REMS due to systolic-dysfunction risk | NCIT:C15986 + NCIT term for mavacamten; `therapeutic_modality: SMALL_MOLECULE` |
| **Aficamten (MYQORZO)** | Allosteric, reversible cardiac myosin inhibitor | Symptomatic obstructive HCM — **FDA approved 2025**, EU **February 2026**; based on phase 3 **SEQUOIA‑HCM** (NCT05186818): ~60% vs 24% placebo improved NYHA class; **Boxed Warning** for heart failure; MYQORZO REMS. *(Aficamten: First Approval, PMID:41941083)* | NCIT:C15986 + `therapeutic_modality: SMALL_MOLECULE` |
| **Oral anticoagulation** (DOAC preferred) | Thromboembolism prevention | **Any AF in HCM, regardless of CHA₂DS₂‑VASc** | NCIT:C15986 |
| **Antiarrhythmics** (amiodarone, sotalol) | Rhythm control | AF/VT | NCIT:C15986 |
| **Diuretics** (cautious) | Preload reduction | Congestion in non-obstructive HCM; **caution in obstruction** | NCIT:C15986 |

**Avoid:** pure vasodilators (nitrates, dihydropyridines), high-dose diuretics, digoxin, and positive inotropes in obstructive physiology.

**Pharmacogenomics:** mavacamten is a **CYP2C19** substrate — dosing and titration are CYP2C19-phenotype-informed (poor metabolisers require dose caps); aficamten has a less CYP2C19-dependent profile. No *TTN*-genotype-directed pharmacogenomics exists. `PharmGKB`/`CPIC` have no CMH9 entry.

### 12.2 Advanced therapeutics

- **Gene therapy:** active for **MYBPC3**-related HCM (AAV9 gene replacement, e.g., TN‑201 and related programs). **Nothing for TTN** — and TTN's ~100 kb coding sequence makes conventional AAV gene replacement structurally impossible. Base/prime editing of specific *TTN* alleles is conceivable but entirely preclinical. **Not applicable to CMH9 today.**
- **Cell therapy, RNA therapies (ASO/siRNA), targeted therapy, immunotherapy:** **none for CMH9.** (Note: *TTN* exon-skipping ASO strategies are being explored preclinically for *TTN*-DCM, not HCM.)

### 12.3 Surgical / interventional

- **Septal myectomy** (extended transaortic) — gold standard for drug-refractory obstructive HCM in experienced centres; NCIT:C15329 Surgical Procedure.
- **Alcohol septal ablation** — catheter alternative for selected anatomy/comorbidity; NCIT:C49236 Therapeutic Procedure.
- **ICD implantation** — primary prevention per risk stratification; secondary prevention after arrest/sustained VT; NCIT:C50040? (use NCIT:C49236 with a device descriptor; `therapeutic_modality: DEVICE`).
- **Catheter ablation** for AF; **cardiac transplantation** (NCIT:C15289 Organ Transplantation) for end-stage disease.

### 12.4 Supportive, rehabilitative, and lifestyle

Symptom-directed care; **moderate-intensity exercise is now endorsed** (a change from historical blanket restriction), with shared decision-making for competitive/high-intensity sport; cardiac rehabilitation (NCIT:C15315 Rehabilitation); genetic counselling (NCIT:C15240); pre-conception and prenatal counselling.

### 12.5 Experimental / trials

No trial has ever enrolled by *TTN* genotype in HCM. Relevant HCM trials: SEQUOIA‑HCM (NCT05186818, aficamten, completed), MAPLE‑HCM (aficamten monotherapy vs metoprolol), ACACIA‑HCM (non-obstructive HCM), ODYSSEY‑HCM, VALOR‑HCM (mavacamten vs septal reduction therapy), and the MYBPC3 gene-therapy programs. **Any clinical_trials block for CMH9 must be annotated as parent-phenotype trials, not CMH9-specific.**

### 12.6 Treatment strategy

Algorithm: confirm HCM and exclude phenocopies → risk-stratify for SCD (ICD decision) → if obstructive and symptomatic: beta-blocker → ±verapamil/disopyramide → cardiac myosin inhibitor (mavacamten or aficamten, with echo surveillance and REMS) → septal reduction therapy if refractory. If non-obstructive: symptom-directed HF therapy, AF management, transplant evaluation at end stage. **Genotype currently informs family screening, not drug choice** — and a *TTN* variant informs neither.

---

## 13. Prevention

- **Primary prevention (preventing the disease):** **not possible** — germline, dominant. No modifiable exposure initiates CMH9.
- **Secondary prevention (early detection):** the core intervention. Cascade clinical screening (ECG + echo) of first-degree relatives every **1–2 years**; cascade *genetic* testing only if a P/LP variant is identified in the proband. **A rare *TTN* variant does not meet this bar and should not be used to include or exclude relatives from surveillance** — the practically important consequence of the Limited classification.
- **Tertiary prevention (preventing complications):** ICD for high SCD risk; anticoagulation for any AF; endocarditis awareness; avoidance of dehydration/vasodilators in obstruction; blood-pressure control; individualised exercise prescription; pregnancy planning and monitoring.
- **Immunization:** not disease-specific; standard influenza/COVID/pneumococcal vaccination as for any cardiac patient.
- **Genetic screening:** PGD/PGT‑M and prenatal diagnosis are technically available for a *known P/LP familial variant* — **not appropriate for a Limited-validity *TTN* variant.**
- **Risk stratification:** ESC HCM Risk‑SCD model; AHA/ACC major risk markers; CMR‑LGE burden.
- **Counselling:** genetic counselling before and after testing is a guideline recommendation (NCIT:C15240 Genetic Counseling); counselling for CMH9 specifically must convey **uncertain gene–disease validity**.
- **Public health / environmental interventions:** pre-participation athletic screening programs (contested cost-effectiveness), AED availability at sporting venues. Not CMH9-specific.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** naturally occurring HCM is well described in **domestic cat**, *Felis catus* (**NCBITaxon:9685**) — the single most important spontaneous animal model of HCM — and less commonly in **dog** (*Canis lupus familiaris*, NCBITaxon:9615), pig, and some non-human primates.
- **Breeds (VBO):** Maine Coon and Ragdoll cats are the classic HCM breeds, with **MYBPC3** founder variants (A31P in Maine Coon; R820W in Ragdoll) — see OMIA. **Sphynx and British Shorthair** have breed-associated HCM without a fully defined gene.
- **Critically: feline HCM is a MYBPC3 story, not a TTN story.** There is **no OMIA entry, and no naturally occurring animal disease, attributed to *TTN* in hypertrophic cardiomyopathy.** *TTN* variants in animals are associated with DCM (e.g., reports in Doberman-type DCM genetics remain contested) and with muscular phenotypes.
- **Orthologues:** mouse *Ttn* (NCBI Gene 22138, MGI:98864); rat *Ttn* (NCBI Gene 84005); zebrafish *ttn.1*/*ttn.2*; medaka *ttn*. Titin's Z‑disc α‑actinin interface, A‑band super-repeats, and M‑band kinase/MURF1 module are **deeply conserved across vertebrates** — the premise on which the medaka model rests.
- **Comparative pathology:** the medaka *nsh* mutant reproduces hypertrophic myocardium, diastolic dysfunction, sarcomeric disarray, and M‑line disassembly — a genuine cross-species mechanistic parallel, but in a two-chambered fish heart without the coronary microcirculation, fibrotic remodelling, or LVOT obstruction that dominate human HCM.
- **Zoonotic potential / transmission:** **not applicable.**

---

## 15. Model Organisms

| Model | Type | Construct | Recapitulation | Limitations | Resource |
|---|---|---|---|---|---|
| **Medaka *non‑spring heart* (nsh)** — *Oryzias latipes* | Vertebrate, in vivo | ENU/positional-cloned **missense D23186V**, exon 204, Ig domain at M‑line/A‑band transition | **The only in vivo model of a CMH9-type allele.** Homozygotes: fewer myofibrils, disrupted sarcomeres, stiffer (N2B-shifted) titin isoforms, atrial velocities ↓ from ~183 to ~64 µm/s. Heterozygotes: **M‑line disassembly** "similar to the pathological changes found in HCM" | **No genetic rescue** ("we were unable to clone the full-length cDNA (~15 kb) to perform the rescue experiments"); fish two-chambered heart; homozygous phenotype is largely hypoplastic/dysmorphic rather than hypertrophic in the mammalian sense; the *human* variants tested are different residues from the fish one | PMID:31628103 (*Dis Model Mech* 2019); bioRxiv 680579; PMC6899042 |
| **Ttn knock-in / truncation mice** | Mammalian, in vivo | M‑line/other targeted alleles; heterozygous truncations | Homozygotes die ~E9.0 with severe sarcomere-assembly defects; heterozygotes normal at baseline but develop **DCM** under angiotensin II/isoproterenol, and **maladaptive hypertrophy** under transverse aortic constriction (PMID:26504781) | **Models DCM, not CMH9.** Load-dependent hypertrophy in a TTNtv mouse is not evidence for TTN-HCM | MGI (MGI:98864), IMSR, IMPC |
| **MURF1/*Trim63* knockout mouse** | Mammalian, in vivo | Constitutive KO | Exaggerated cardiac hypertrophy after pressure overload — establishes MURF1 as a brake on hypertrophic growth, supporting the *pathway* invoked by Hypothesis B | Pathway-level plausibility only; not a *TTN*-variant model | MGI |
| **Yeast two-hybrid titin–α‑actinin assay** | In vitro | Z‑repeat fragment + α‑actinin CaM-like domain | The **entire experimental basis of Hypothesis A** (~40% affinity increase for R740L) | Heterologous, non-cardiac, interaction-only; no functional or cellular readout | PMID:10462489 |
| **In vitro MURF1 binding + ubiquitination assays** | In vitro | Recombinant titin Ig fragments + MURF1/MURF2 | Increased MURF1 binding, multi-ubiquitination, reduced mutant protein levels | Fragment-based; does not establish myocardial consequence | PMID:31628103 |
| **Human iPSC-derived cardiomyocytes (isogenic)** | In vitro, human | **Does not yet exist for CMH9 alleles** | — | — | **This is the single highest-value missing experiment** (see below) |

**Overall model-system verdict:** CMH9 has **no mammalian genetic model, no genetic rescue in the one model that exists, and no human-cell model.** In dismech terms, this warrants a `HUMAN_MODEL_MISMATCH` discussion alongside the `KNOWLEDGE_GAP`: evidence *exists* (medaka, yeast two-hybrid), but its translational validity to human HCM is precisely the unresolved question.

---

## 16. Synthesis: Knowledge Gaps and the Experiments That Would Settle Them

**Open question 1 (KNOWLEDGE_GAP):** *Is TTN a hypertrophic cardiomyopathy gene at all, or should CMH9 be retired as a disease entity?*

What is missing is a specific evidence class: **large-cohort, region-stratified case-control burden testing of rare TTN _missense_ variation** (Z‑disc / I‑band / A‑band / M‑band strata) in HCM against gnomAD-scale controls, plus **segregation in multiplex families**. Note that truncating-variant burden has already been tested and is negative — the burden question that remains open is missense-specific, and it has not been properly asked. Proposed experiments:

1. **Region-stratified rare *TTN* missense burden test** in a large sarcomere-negative HCM cohort vs population reference, stratified by domain and PSI. *Supports* CMH9 if a regional excess emerges; *refutes* it if the burden matches population expectation.
2. **Segregation analysis** of p.Arg740Leu, p.Ser30186Ala, p.Asp30994Asn (and now p.Arg6745Cys) in extended pedigrees. This is the evidence class most conspicuously absent from the founding report.
3. **Isogenic human iPSC-cardiomyocyte modelling** of the reported alleles: hypertrophic growth, sarcomere organisation, titin turnover/half-life, passive stiffness, and relaxation kinetics vs isogenic controls — replacing yeast two-hybrid and fish data with human cardiac cell data.

**Open question 2 (CONTROVERSY):** *If TTN does not cause HCM, do TTNtv nonetheless modify outcome within established HCM?* The two claims are logically separable and the evidence points in opposite directions: prevalence data argue against causation, while the same cohort reports adjusted HR 6.88 for cardiovascular death (PMID:28822653; 3 deaths among 13 carriers, unreplicated). Resolution requires **replication in an independent, ancestrally distinct HCM cohort with adequate event numbers** — e.g., within SHaRe or a national registry with linked *TTN* sequencing.

**Curation guard (Named Entity Confusion risk — high).** *TTN*'s dominant, well-validated cardiomyopathy association is with **dilated** cardiomyopathy (MONDO:0005021; ClinGen **Definitive**; TTNtv in ~25% of familial DCM). That literature is an order of magnitude larger than the HCM literature and is trivially easy to import by mistake — including via search engines and deep-research tools that will happily return DCM content for a "TTN cardiomyopathy" query. Every claim in a CMH9 entry must be checked against the question: *does this source's cohort have hypertrophic, or dilated, cardiomyopathy?*

---

## Reference list (with evidence-source classification)

| PMID / ID | Citation | Evidence source | Use |
|---|---|---|---|
| **10462489** | Satoh M, et al. Structural analysis of the titin gene in hypertrophic cardiomyopathy: identification of a novel disease gene. *Biochem Biophys Res Commun* 1999;262:411‑7 | HUMAN_CLINICAL + IN_VITRO | Founding CMH9 report; R740L; α‑actinin binding |
| **31628103** | Perturbation of the titin/MURF1 signaling complex is associated with hypertrophic cardiomyopathy in a fish model and in human patients. *Dis Model Mech* 2019;12:dmm041103 | MODEL_ORGANISM + IN_VITRO + HUMAN_CLINICAL | Medaka nsh; 2 human M‑line Ig variants; MURF1 |
| **22335739** | Herman DS, et al. Truncations of titin causing dilated cardiomyopathy. *N Engl J Med* 2012;366:619‑28 | HUMAN_CLINICAL | TTNtv: DCM 27% vs HCM 1% vs controls 3%; Z‑disk/M‑band absence |
| **28822653** | Titin-truncating variants increase the risk of cardiovascular death in patients with hypertrophic cardiomyopathy. *Can J Cardiol* 2017;33:1292‑7 | HUMAN_CLINICAL | TTNtv 2.5% HCM vs 2.6% controls; modifier HR 6.88 |
| **16352453** | Bos JM, et al. Genotype-phenotype relationships involving HCM-associated mutations in titin, muscle LIM protein, and telethonin. *Mol Genet Metab* 2006;88:78‑85 | HUMAN_CLINICAL | "No TTN mutations were detected" in 389 HCM |
| **30681346** | Ingles J, et al. Evaluating the clinical validity of hypertrophic cardiomyopathy genes. *Circ Genom Precis Med* 2019;12:e002460 | OTHER (expert curation) | 8/33 definitive; 22/33 limited or no evidence |
| **39132495** / doi:10.1016/j.jacc.2024.12.010 | Hespe S, Waddell A, Asatryan B, et al. Genes associated with hypertrophic cardiomyopathy: a reappraisal by the ClinGen HCVD GCEP. *JACC* 2025;85(7):727‑740 (preprint PMC11312670) | OTHER (expert curation) | TTN 1.2+5.5=6.7 → **Limited**; PSI rationale; 29 genes at moderate+ |
| CGGV assertion `c17e22eb-…-2025-10-28` | ClinGen: TTN / hypertrophic cardiomyopathy (MONDO:0005045), AD, **Limited** | OTHER | Authoritative validity call |
| CGGV assertion `1ec53217-…-2025-05-30` | ClinGen: TTN / dilated cardiomyopathy (MONDO:0005021), AD, **Definitive** | OTHER | Anti-conflation contrast |
| **25589632** | Roberts AM, et al. Integrated allelic, transcriptional, and phenomic dissection of the cardiac effects of titin truncations in health and disease. *Sci Transl Med* 2015 | HUMAN_CLINICAL + COMPUTATIONAL | PSI framework for TTNtv interpretation |
| **20301725** | Cirino AL, Channaoui N, Ho C. Nonsyndromic Hypertrophic Cardiomyopathy Overview. *GeneReviews* [updated 2025‑03‑06] | OTHER (review) | HCM clinical characteristics, penetrance, gene table, management. **Note: does not list TTN as an HCM gene** |
| **38718139** | 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of Hypertrophic Cardiomyopathy. *Circulation* 2024 | OTHER (guideline) | Diagnosis, risk stratification, treatment, cascade screening |
| **30297972** | Ho CY, et al. Genotype and lifetime burden of disease in hypertrophic cardiomyopathy: insights from SHaRe. *Circulation* 2018;138:1387‑1398 | HUMAN_CLINICAL | Sarcomere-positive vs -negative outcomes |
| **39895828** | A case study identified a new mutation in the TTN gene for inherited hypertrophic cardiomyopathy. *Int J Gen Med* 2025 | HUMAN_CLINICAL | Chinese family, TTN c.20233C>T p.R6745C, exon 80 |
| **26504781** | Pressure overload by transverse aortic constriction induces maladaptive hypertrophy in a titin-truncated mouse model. 2015 | MODEL_ORGANISM | **DCM/load model — contextual only** |
| **41941083** | Aficamten: First Approval. *Drugs* | OTHER | Aficamten (MYQORZO) FDA 2025 / EU Feb 2026 |
| doi:10.1098/rsob.140041 | Bogomolovas J, et al. Titin kinase is an inactive pseudokinase scaffold that supports MuRF1 recruitment to the sarcomeric M-line. *Open Biol* 2014;4:140041 | IN_VITRO | Titin kinase–MURF1 scaffold biology |
| doi:10.1016/j.jacadv.2025.102552 | Epidemiology of hypertrophic cardiomyopathy in the United States from 2016 to 2023. *JACC: Advances* 2025 | HUMAN_CLINICAL | US HCM prevalence 1 in 327 |
| ClinVar **VCV000012649** | NM_001267550.2(TTN):c.2219G>T (p.Arg740Leu), rs28933405 | OTHER | 0‑star "Pathogenic", OMIM submission, evaluated 1999‑08‑27 |
| MONDO:0013412 | MONDO ontology record | OTHER | Definition, synonyms, xrefs, logical axioms |

**Unresolved retrieval gaps in this report (flagged rather than guessed):** (1) gnomAD v4 allele frequency for TTN p.Arg740Leu could not be retrieved programmatically (gnomAD is a client-rendered app; ClinVar shows no frequency) — verify via the gnomAD GraphQL API or browser before curating any frequency claim; (2) the full-text TTN paragraph of the final *JACC* 2025 reappraisal was accessible only via the medRxiv/PMC preprint — verify wording against the published version before quoting it as an evidence snippet; (3) whether the two 2019 M‑line Ig variants segregated in their families is asserted in that paper's pedigrees but was judged insufficient by ClinGen — read the primary figures before making a segregation claim either way.

**Sources:**
- [OMIM #613765 — CMH9](https://omim.org/entry/613765) · [OMIM \*188840 — TTN](https://omim.org/entry/188840) · [Clinical Synopsis 613765](https://www.omim.org/clinicalSynopsis/613765)
- [GTR: Hypertrophic cardiomyopathy 9 (C1861065)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1861065/) · [ClinVar VCV000012649](https://www.ncbi.nlm.nih.gov/clinvar/variation/12649/) · [ClinVar RCV000013484](https://www.ncbi.nlm.nih.gov/clinvar/RCV000013484/)
- [ClinGen HCM gene reappraisal (JACC 2025)](https://www.jacc.org/doi/10.1016/j.jacc.2024.12.010) · [preprint PMC11312670](https://pmc.ncbi.nlm.nih.gov/articles/PMC11312670/) · [ClinGen summary page](https://clinicalgenome.org/docs/genes-associated-with-hypertrophic-cardiomyopathy-a-reappraisal-by-the-clingen-hereditary-cardiovascular-disease-gene-curation/) · [GenCC TTN–HCM submission](https://thegencc.org/submissions/SGC-105420.2)
- [Evaluating the Clinical Validity of HCM Genes (Circ Genom Precis Med 2019)](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002460) · [SHaRe: Genotype and Lifetime Burden of Disease in HCM](https://www.ahajournals.org/doi/10.1161/circulationaha.117.033200)
- [Titin/MURF1 medaka + human HCM study (PMC6899042)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6899042/) · [PMID 28822653](https://pubmed.ncbi.nlm.nih.gov/28822653/) · [Titin-truncated mouse TAC model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4609346/) · [Titin kinase pseudokinase / MuRF1 scaffold](https://royalsocietypublishing.org/doi/10.1098/rsob.140041) · [α-actinin-2 Z-disc dysfunction in human myocardium](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10572656/)
- [GeneReviews: Nonsyndromic HCM Overview (NBK1768)](https://www.ncbi.nlm.nih.gov/books/NBK1768/) · [2024 AHA/ACC HCM Guideline](https://www.ahajournals.org/doi/10.1161/CIR.0000000000001250) · [ACC Key Points](https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2024/05/06/15/12/2024-hypertrophic-cardiomyopathy-gl)
- [US HCM epidemiology 2016–2023 (JACC Advances)](https://www.jacc.org/doi/10.1016/j.jacadv.2025.102552) · [Orphanet: rare hypertrophic cardiomyopathy (ORPHA:217569)](https://www.orpha.net/en/disease/detail/217569) · [Orphanet: familial isolated HCM (ORPHA:155)](https://www.orpha.net/en/disease/detail/155)
- [Cytokinetics: FDA approval of MYQORZO (aficamten)](https://ir.cytokinetics.com/press-releases/press-release-details/2025/Cytokinetics-Announces-FDA-Approval-of-MYQORZO-aficamten-for-the-Treatment-of-Adults-with-Symptomatic-Obstructive-Hypertrophic-Cardiomyopathy-to-Improve-Functional-Capacity-and-Symptoms/default.aspx) · [TCTMD coverage](https://www.tctmd.com/news/fda-approves-aficamten-obstructive-hcm) · [Aficamten: First Approval (PMID 41941083)](https://pubmed.ncbi.nlm.nih.gov/41941083/)
- [TTN A Case Study, Int J Gen Med 2025 (PMID 39895828)](https://www.tandfonline.com/doi/full/10.2147/IJGM.S505865) · [ICD-10-CM I42.1](https://www.icd10data.com/ICD10CM/Codes/I00-I99/I30-I5A/I42-/I42.1) · [ICD-10-CM I42.2](https://www.icd10data.com/ICD10CM/Codes/I00-I99/I30-I5A/I42-/I42.2) · [ICD-11 HCM block](https://www.findacode.com/icd-11/block-1830681485.html)