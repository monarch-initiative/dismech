---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T01:36:07.645031'
end_time: '2026-08-01T01:49:10.868008'
duration_seconds: 783.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Non-Syndromic Intellectual Disability
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
  web_search_requests: 15
  num_turns: 56
  total_cost_usd: 3.71910675
  session_id: f7a1b538-78d0-4ea4-a724-4770ed9ba44e
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Non-Syndromic Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Non-Syndromic Intellectual Disability** covering all of the
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

# Comprehensive Research Report
## Autosomal Recessive Non-Syndromic Intellectual Disability (AR‑NSID / NS‑ARID)

**Prepared:** 1 August 2026 · **Target MONDO:** `MONDO:0019502` · **Category:** Genetic

> **Curation caveat up front (dismech SOP §2a/§2b).** This report is a *lead document*. Several abstracts below were retrieved through a summarizing fetch layer that returned quoted fragments rather than complete verbatim text; those are marked **[fragment — re-verify]**. Before any snippet here is committed to a `kb/disorders/` YAML file, run `just fetch-reference PMID:XXXX` and `just validate-references`. Fully verbatim-retrieved abstracts are marked **[verbatim]**.
>
> **A second, structural caveat specific to this entry.** AR‑NSID is not a disease in the usual dismech sense — it is a *nosological class* (an OMIM phenotypic series and a MONDO grouping node with 72 descendants and ~56 causal genes). Section 16 at the end discusses what this implies for how the dismech entry should be shaped (strong candidate for a `kb/groupings/` entity plus/instead of a `Disease`).

---

## 1. Disease Information

### 1.1 Overview

Autosomal recessive non-syndromic intellectual disability is the class of intellectual disability (ID) in which (a) biallelic (homozygous or compound heterozygous) variants in an autosomal gene are the cause, and (b) impaired intellectual functioning and adaptive behaviour occur **without** a consistent, recognizable pattern of associated dysmorphic, malformative, metabolic, or neuroimaging features. It corresponds to the OMIM "intellectual developmental disorder, autosomal recessive" (MRT) numbered series.

Two features define its epistemic character:

1. **Extreme genetic heterogeneity.** Ropers/Jamra estimate "**2500–3000 ARID genes**," of which "less than 700 confirmed genes and less than 400 candidate genes have been identified" (PMID:30459488) **[fragment — re-verify]**. Harripaul et al. write **[verbatim]**: *"Previous studies have indicated high levels of genetic heterogeneity, with estimates of more than 2500 autosomal ID genes, the majority of which are autosomal recessive (AR)."* (PMID:28397838)

2. **An unstable syndromic/non-syndromic boundary.** The "non-syndromic" label is frequently provisional. Jamra states **[fragment — re-verify]**: *"many of the cases were rather unspecific and several ID forms that were reported initially to be nonsyndromic turned out to be syndromic, as other cases with overlapping phenotypes have been identified"* (PMID:30459488). This is the single most important curation caveat for this entry — see §3.4 and §16.

### 1.2 Key identifiers (verified)

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0019502` | Verified locally via OAK. Def: *"Autosomal recessive form of non-syndromic intellectual disability."* `is_a` MONDO:0000509 (non-syndromic ID) and MONDO:0100597 (intellectual disability, autosomal recessive); logical definition `MONDO:0000509 and RO:0000053 some HP:0000007` |
| **OMIM Phenotypic Series** | `OMIMPS:249500` (PS249500) | Anchor entry MIM 249500 = MRT1 (PRSS12) |
| **Orphanet** | `ORPHA:88616` | ORDO subset `ordo_subtype_of_a_disorder` |
| **DOID** | `DOID:0060308` | |
| **MedGen / UMLS** | MedGen UID 1826073 / `UMLS:C5680181` | Verified via MedGen |
| **GARD** | `GARD:0018643` | |
| **ICD-10** | F70–F79 (no AR-NSID-specific code) | Etiology is not coded in ICD-10; use F70 mild / F71 moderate / F72 severe / F73 profound |
| **ICD-11** | 6A00 *Disorders of intellectual development* (6A00.0–6A00.4) | Plus an etiology code from LD2F (monogenic) where applicable |
| **MeSH** | D008607 *Intellectual Disability*; D000015 *Abnormalities, Multiple*; qualifier "Genetic Diseases, Inborn" (D030342) | No AR-NSID-specific MeSH descriptor |
| **HPO inheritance** | `HP:0000007` Autosomal recessive inheritance (verified) | |

**Monarch association counts for MONDO:0019502** (retrieved 2026-08-01, Monarch API v3): 72 descendants; 61 correlated genes (54 direct); **56 causal genes**; 1131 disease→phenotype associations; 5 disease models.

### 1.3 Synonyms (from the MONDO record, verified)

- **Exact:** AR‑NSID; NS‑ARID; autosomal recessive non-syndromic intellectual disability; mental retardation, autosomal recessive; non-syndromic intellectual disability, autosomal recessive
- **Broad:** autosomal recessive intellectual disability (ARID); intellectual disability, autosomal recessive
- **In the literature:** NS‑ARMR (non-syndromic autosomal recessive mental retardation); NSID (used loosely for both AD and AR forms); "MRT" series

### 1.4 Source type

Almost all AR‑NSID knowledge is **aggregated disease-level** and derives from a specific study design: homozygosity/autozygosity mapping plus exome or genome sequencing in **large multiplex consanguineous families**, predominantly Iranian, Pakistani, Turkish, and Arab. There is essentially no EHR-derived phenotyping literature for AR‑NSID as a class, and this ascertainment design systematically biases the phenotype spectrum (see §9.4).

---

## 2. Etiology

### 2.1 Primary causal factor

Biallelic pathogenic variants — usually homozygous by descent, less often compound heterozygous — in any one of a very large number of autosomal genes. There is **no dominant gene and no dominant pathway**. Jamra's conclusion is the key statement **[fragment — re-verify]**: *"there are no prevalent ARID genes, pathways, or protein complexes and the functions of the affected proteins are very diverse and limited not only to neurological aspects"* — and therefore *"there is no justification for a gene-specific or panel diagnostic when ARID is suspected."* (PMID:30459488)

Recurrence across large cohorts is strikingly low. Among **1,131 families** aggregated across the major studies, the most frequently implicated genes were **[fragment — re-verify]**:

| Gene | Families | % of 1,131 | Note |
|---|---|---|---|
| *VPS13B* | 10 | 2.3% | Cohen syndrome — syndromic on full ascertainment |
| *MAN1B1* | 9 | 2.0% | `hgnc:6823` |
| *ADAT3* | 8 | ~0.7% | `hgnc:25151` |
| *AP4M1* | 8 | ~0.7% | AP-4 deficiency — spastic paraplegia, syndromic |

That the top four together account for well under 6% of families is the defining epidemiological fact of AR‑NSID.

### 2.2 Genetic risk factors

**Causal architecture.** Loss-of-function (nonsense, frameshift, canonical splice, homozygous whole-gene or partial deletion) predominates; missense variants at deeply conserved residues are the second class. Harripaul et al. **[verbatim]**: *"The new ARID genes include nine with loss-of-function mutations (ABI2, MAPK8, MPDZ, PIDD1, SLAIN1, TBC1D23, TRAPPC6B, UBA7 and USP44), and missense mutations include the first reports of variants in BDNF or TET1 associated with ID."* (PMID:28397838)

**The dominant modifiable "genetic" risk factor is parental consanguinity** — a population-structure risk factor rather than a locus. Jamra **[fragment — re-verify]**: *"the total risk for ID is about 2–3 times higher in children of consanguineous families,"* with *"the prevalence of diagnosable monogenic ID in the children of first cousins or closer [being] two times higher"* (PMID:30459488). Couples related as second cousins or closer, and their progeny, account for an estimated **10.4% of the global population** (Bittles & Black; PMID:19805052 for the PNAS treatment). Consanguinity rates of **20–50%** are reported across North Africa, Central and West Asia, and much of South Asia; Saudi Arabia is often quoted at ~56% overall.

Hu et al. frame the population burden **[verbatim]**: *"Autosomal recessive (AR) gene defects are the leading genetic cause of intellectual disability (ID) in countries with frequent parental consanguinity, which account for about 1/7th of the world population."* (PMID:29302074)

**Modifier loci / oligogenic burden.** Multi-locus causation is documented and non-trivial. Riazuddin et al. **[verbatim]**: *"In another eight families segregation of multiple pathogenic variants was observed, affecting 19 genes that were either known or are novel candidates for ID."* (PMID:27457812) — i.e. ~6.6% of their 121 families. This is a real, curatable phenomenon and a candidate for the dismech oligogenic-inheritance pattern (`HP:0010983`).

**Genomic imprinting as a dosage modifier.** *TRAPPC9* is expressed with a maternal bias (~70%) in brain, and heterozygotes lacking the *maternal* allele phenocopy homozygous nulls in mouse — see §4.5.

### 2.3 Environmental risk factors

For AR‑NSID *sensu stricto*, environmental exposure is **not causal**. Environmental factors are relevant only as (a) confounders in the differential diagnosis (see §10.5) and (b) potential severity modifiers acting on an established genetic lesion. Note that the class-level ID prevalence literature explicitly attributes part of the *mild* ID burden to environment: *"the prevalence of severe ID and mild ID is variable due to the influence of some environmental stressors"* (PMC9946902). No AR‑NSID-specific gene–environment interaction has been established.

### 2.4 Protective factors

- **Genetic:** None identified. Notably, common variants in NS‑ARID genes are **not** associated with normal-range intelligence — Davies/Deary et al. **[verbatim]**: *"Gene-based tests indicated that genes implicated in NS-ARID were not significantly enriched for quantitative trait loci (QTL) associated with intelligence. These findings suggest that genes in which mutations can have a large and deleterious effect on intelligence are not associated with variation across the range of intelligence differences."* (PMID:26912939). This is an important negative result: AR‑NSID is **not** the low tail of the polygenic intelligence distribution.
- **Environmental/social:** Outbreeding is protective at the population level. Early intervention, enriched education, and family support improve adaptive outcome without altering the molecular lesion.

### 2.5 Gene–environment interactions

Not established for AR‑NSID. The most defensible statement is negative: AR‑NSID is a high-penetrance monogenic class in which environment modulates *adaptive functional outcome* rather than *disease occurrence*.

---

## 3. Phenotypes

### 3.1 The defining phenotype

| Phenotype | HPO term (verified via OAK) | Frequency | Notes |
|---|---|---|---|
| Intellectual disability | `HP:0001249` Intellectual disability | **Obligate (100%)** | Definitional |
| Global developmental delay | `HP:0001263` Global developmental delay | Very frequent | The pre-school presentation |
| Delayed speech and language development | `HP:0000750` Delayed speech and language development | Frequent | Often the presenting complaint |
| Motor delay | `HP:0001270` Delayed gross motor development | Variable | Often *spared* in classic NS forms |

Diagnostic threshold: *"an intelligence quotient (IQ) of 70 or below and a deficit in at least two behaviors associated with adaptive functioning"* (PMC9946902). DSM-5 requires deficits in intellectual functioning **and** adaptive functioning with onset during the developmental period; DSM-5 grades severity by adaptive functioning rather than IQ.

### 3.2 Severity distribution

Consanguineous-cohort ascertainment (multiplex families, often referred to specialist genetics services) is enriched for **moderate-to-severe** ID. Basel-Vanagaite reported *CC2D1A* families with *"severe autosomal recessive NSMR"* (PMID:16033914) **[fragment]**; NSUN2 families showed *"moderate to severe ID"* (PMID:22541559) **[fragment]**.

| Severity | HPO term (verified) | Comment |
|---|---|---|
| Mild ID | `HP:0001256` | Under-ascertained in the AR‑NSID literature |
| Moderate ID | `HP:0002342` | Common |
| Severe ID | `HP:0010864` | Common; enriched in the classic multiplex-family series |
| Profound ID | `HP:0002187` | Present in the Monarch descendant annotations |

**Curation guidance:** frequency bands for severity strata are *not* supportable from the literature at class level (dismech `docs/frequency-evidence-guidelines.md` — omit rather than fabricate). Record severity as **VARIABLE** with a note on ascertainment bias.

### 3.3 The Monarch-propagated annotation set

Terms propagated to `MONDO:0019502` across its 72 descendants (retrieved 2026-08-01; **no frequency qualifiers present in the source**):

`HP:0001263` global developmental delay · `HP:0031936` delayed ability to walk · `HP:0001249` intellectual disability · `HP:0002194` motor delay · `HP:0001270` delayed gross motor development · `HP:0002187` profound intellectual disability · `HP:0001257` spasticity · `HP:0010864` severe intellectual disability · `HP:0100704` cerebral visual impairment · `HP:0000400` macrotia · `HP:0000598` abnormality of the outer ear · `HP:0000377` abnormal pinna morphology · `HP:0000356` abnormality of the external ear

**Read this set critically.** Spasticity, cerebral visual impairment, and the ear-morphology cluster are *inherited from syndromic descendants* of the grouping node — they are precisely the features whose presence would disqualify a case from being called non-syndromic. Do **not** transcribe them into the AR‑NSID entry as class-level phenotypes; they are evidence of the leaky syndromic/non-syndromic boundary, not of the class phenotype.

### 3.4 Features that are *commonly* present despite the "non-syndromic" label

This is the honest clinical picture, and it should be curated explicitly with per-gene attribution:

| Feature | HPO (verified) | Association |
|---|---|---|
| Microcephaly (usually postnatal) | `HP:0000252` | *TRAPPC9* (PMID:20004763 — *"associated with variable postnatal microcephaly"*; PMID:20004765 — *"Microcephaly is present in some but not all affected individuals"*) **[both verbatim]** |
| Seizure | `HP:0001250` | Subset of MRT genes |
| Autism / autistic behaviour | `HP:0000717` | *CC2D1A* strongly (see §6.2) |
| ADHD / short attention span | `HP:0007018` / `HP:0000736` | Frequent behavioural comorbidity |
| Absent speech | `HP:0001344` | Severe forms |
| Obesity | `HP:0001513` | *TRAPPC9* — >50% of cases (see §4.5, §6.3) |
| Facial dysmorphism | `HP:0001999` | *NSUN2* — *"Affected individuals displayed moderate to severe ID and facial dysmorphism"* (PMID:22541559) **[fragment]** — i.e. NSUN2 is arguably mis-classified as non-syndromic |

### 3.5 Neuroimaging

Classic AR‑NSID has an unremarkable or minimally abnormal MRI — this is part of the definition. Documented exceptions with mechanistic value:

- ***TRAPPC9***: *"MRI analysis of affected patients shows defects in axonal connectivity"* (PMID:20004763) **[verbatim]**; *"Brain magnetic resonance imaging of affected individuals indicates the presence of mild cerebral white matter hypoplasia"* (PMID:20004765) **[verbatim]**. HPO: `HP:0012429` cerebral white matter hypoplasia (verify label with OAK before use).
- Mild cerebellar atrophy reported in individual families (PMC9946902).

### 3.6 Temporal characteristics per phenotype

| Dimension | Value | dismech slot |
|---|---|---|
| Onset | Congenital lesion; clinically apparent in infancy–early childhood | `onset_category: INFANTILE` / `CHILDHOOD` |
| Progression | **Static (non-progressive)** encephalopathy | `clinical_course: STABLE` |
| Regression | Absent — `HP:0002376` developmental regression is a *red flag against* AR‑NSID and toward a metabolic/degenerative diagnosis | Curate as a differential-diagnosis discriminator |
| Duration | Lifelong | `CHRONIC` |

### 3.7 Quality of life

No AR‑NSID-specific QoL instrument literature was located. Generic ID QoL evidence applies: adaptive-functioning severity, communication ability, presence of epilepsy, and behavioural comorbidity are the dominant determinants of caregiver burden and individual QoL. Instruments used in the broader ID field: WHOQOL-DIS, Quality of Life Questionnaire (QoL-Q), PedsQL, EQ-5D-Y (proxy-reported). **Flag as a genuine evidence gap** — a candidate `discussions: kind: KNOWLEDGE_GAP` entry.

---

## 4. Genetic / Molecular Information

### 4.1 Scale of the gene set

- OMIM **PS249500** contains on the order of **60–72 numbered MRT entries**; roughly a quarter still have no identified gene. (I was unable to retrieve the OMIM table directly — omim.org returned HTTP 403. **Pull the authoritative list from https://www.omim.org/phenotypicSeries/PS249500 before finalizing the entry.**)
- Monarch reports **56 causal genes** and 61 correlated genes for `MONDO:0019502`.
- SysID (2018 snapshot): *"684 genes that, when mutated, would lead to an ARID form and 378 autosomal recessive candidate genes."* SysID 2021: *"1500 primary ID genes, causing 1797 ID related disorders, and 1248 ID candidate genes"* (all ID, all inheritance modes) — cited in PMID:34930158.
- Upper-bound estimate: **2500–3000 ARID genes** (PMID:30459488). The DDD study's independent estimate: *"903 ARID genes clarify roughly half of the observed excess of damaging biallelic genotypes."*

### 4.2 Landmark and representative genes (HGNC IDs verified locally via OAK, lowercase `hgnc:` per repo convention)

| Gene | HGNC | MRT | Protein / function | Key citation |
|---|---|---|---|---|
| **PRSS12** | `hgnc:9477` | MRT1 | Neurotrypsin — presynaptic serine protease; cleaves agrin | PMID:12459588 |
| **CRBN** | `hgnc:30185` | MRT2 | Cereblon; CUL4-DDB1 E3 ligase substrate receptor | Higgins 2004 |
| **CC2D1A** | `hgnc:30237` | MRT3 | Freud-1/Aki1; NF‑κB and cAMP–PKA–PDE4D regulator | PMID:16033914 |
| **GRIK2** | `hgnc:4580` | MRT6 | Kainate receptor GluK2 | Motazacker 2007 |
| **TUSC3** | `hgnc:30242` | MRT7 | OST complex subunit; N-glycosylation | PMID:18452889; PMID:21513506 |
| **TRAPPC9** | `hgnc:30832` | MRT13 | NIBP; TRAPPII subunit; NIK/IKKβ-binding | PMID:20004763; PMID:20004765 |
| **NSUN2** | `hgnc:25994` | MRT5 | tRNA m⁵C methyltransferase | PMID:22541559; PMID:22541562 |
| **TECR** | `hgnc:4551` | MRT14 | trans-2-enoyl-CoA reductase; VLCFA elongation | Çalışkan 2011 |
| **MAN1B1** | `hgnc:6823` | MRT15 | ER α-1,2-mannosidase; glycoprotein quality control | PMID:21763484 |
| **ST3GAL3** | `hgnc:10866` | MRT12 | Sialyltransferase | Hu 2011 |
| **MED23** | `hgnc:2372` | MRT18 | Mediator complex subunit 23 | Hashimoto 2011 |
| **ELP2** | `hgnc:18248` | MRT58 | Elongator complex subunit 2 | Cohen 2015 |
| **IMPA1** | `hgnc:6050` | MRT59 | Inositol monophosphatase 1 (lithium target) | Figueiredo 2016 |
| **METTL23** | `hgnc:26988` | MRT44 | Methyltransferase-like 23 | Bernkopf/Reiff 2014 |
| **LINS1** | `hgnc:30922` | MRT27 | Wnt-signalling regulator | Akawi 2013 |
| **ZNF526** | `hgnc:29415` | — | Zinc-finger transcription factor | Najmabadi 2011 cohort |
| **CDK5R1** | `hgnc:1775` | — | p35, CDK5 activator (17q11.2 candidate) | PMC9946902 |
| **NDST1** | `hgnc:7680` | MRT46 | Heparan sulfate N-deacetylase/N-sulfotransferase | |
| **TNIK** | `hgnc:30765` | MRT54 | TRAF2/NCK-interacting kinase | |
| **PGAP1** | `hgnc:25712` | MRT42 | GPI-anchor remodelling | |
| **WASHC4** (KIAA1033/SWIP) | `hgnc:29174` | MRT43 | WASH complex — endosomal actin | Ropers 2011 |
| **TRAPPC6B** | `hgnc:23066` | — | TRAPP complex subunit (new in Harripaul 2018) | PMID:28397838 |
| **MAPK8** (JNK1) | `hgnc:6881` | — | Stress-activated MAP kinase | PMID:28397838 |
| **MPDZ** | `hgnc:7208` | — | Multi-PDZ domain scaffold | PMID:28397838 |
| **TBC1D23** | `hgnc:25622` | — | Golgi–endosome tethering | PMID:28397838 |
| **ADAT3** | `hgnc:25151` | MRT36 | tRNA adenosine deaminase | Recurrent in Arab populations |
| **CRADD** | `hgnc:2340` | MRT34 | PIDDosome; lissencephaly (syndromic) | |
| **VPS13B** | `hgnc:2183` | — | Cohen syndrome (syndromic on full workup) | |
| **AP4M1** | `hgnc:574` | — | AP-4 deficiency / SPG50 (syndromic) | |
| **ADK** | `hgnc:257` | — | Adenosine kinase deficiency (metabolic) | |

Additional Harripaul 2018 LoF genes with HGNC to look up if curated: *ABI2*, *PIDD1*, *SLAIN1*, *UBA7*, *USP44*; missense: *BDNF*, *TET1*.

### 4.3 Variant classification, type, and frequency

- **Classification:** ACMG/AMP. For the ultra-heterogeneous AR‑NSID space the practical bottleneck is PS4/PP1 evidence — most novel genes are supported by one or two families, so many variants sit at "likely pathogenic" or VUS pending GeneMatcher-driven case accrual. ClinGen Gene–Disease Validity classifications exist for only a minority of MRT genes; many remain "Limited" or uncurated. **Cite `CGGV:` structured records where available.**
- **Type:** nonsense, frameshift, canonical ±1/2 splice, homozygous intragenic and whole-gene deletions (e.g. *"a homozygous deletion of 170.673 Kb which encompassed the TUSC3 gene"* — PMID:21513506 **[fragment]**), and conserved-residue missense.
- **Allele frequency:** causal alleles are individually ultra-rare; gnomAD homozygote counts of 0 for a given allele are standard supporting evidence. In consanguineous founder populations specific alleles reach appreciable local carrier frequencies with negligible global frequency — a key filtering trap.
- **Origin:** **germline** throughout. Somatic mosaicism is not a recognized mechanism for AR‑NSID.
- **Functional consequence:** **loss of function** predominates, consistent with recessive inheritance. Gain-of-function and dominant-negative mechanisms are not characteristic. Hypomorphic missense alleles explain part of the severity spectrum within a gene.

### 4.4 Support for pathogenicity beyond segregation

Riazuddin et al. give the canonical multi-modal argument **[verbatim]**:

> *"Transcriptome profiles of normal human brain tissues showed that the novel candidate ID genes formed a network significantly enriched for transcriptional co-expression (P<0.0001) in the frontal cortex during fetal development and in the temporal-parietal and sub-cortex during infancy through adulthood. In addition, proteins encoded by 12 novel ID genes directly interact with previously reported ID proteins in six known pathways essential for cognitive function (P<0.0001)."* (PMID:27457812)

Harripaul et al. add **[verbatim]**: *"The genes identified also showed overlap with de novo gene sets for other neuropsychiatric disorders. Transcriptional studies showed prominent expression in the prenatal brain."* (PMID:28397838)

### 4.5 Epigenetics and imprinting

The best-characterized epigenetic dimension is **parent-of-origin allelic bias at *TRAPPC9*** — Wang et al. **[verbatim]**:

> *"In an analysis of brain-specific allele-biased expression, we identified that Trappc9, a cellular trafficking factor, was expressed predominantly (~70%) from the maternally inherited allele. … Strikingly, heterozygous mice lacking the maternal allele (70% reduced expression) had pathology similar to homozygous mutants, whereas mice lacking the paternal allele (30% reduction) were phenotypically normal."* (PMID:32877400)

This has a direct clinical corollary: for an imprinted-bias ARID gene, a *monoallelic* maternally-inherited LoF variant may be pathogenic — a genotype that standard recessive filtering would discard.

Separately, *TET1* (5mC→5hmC dioxygenase) appearing as a novel ARID gene (PMID:28397838) places DNA demethylation machinery inside the causal set, and differential methylation at *TRAPPC9* has been reported in severe childhood obesity.

### 4.6 Chromosomal abnormalities

Not the primary mechanism — but **homozygous CNVs** are a genuine and recurrent cause, which is why CMA remains a first-tier test even in a suspected-recessive workflow. Harripaul et al. explicitly combined *"microarray genotyping, homozygosity-by-descent (HBD) mapping, copy number variation (CNV) analysis, and whole exome sequencing"* and reported *"definite or candidate mutations (or CNVs) in 51% of families"* (PMID:28397838) **[verbatim]**. Anwar et al. found *"copy number variants in 14% (n=54, 15% are novel)"* of their 337-subject ID cohort (PMID:27431290) **[verbatim]**.

---

## 5. Environmental Information

**Not applicable as an etiologic category.** No toxin, occupational exposure, radiation source, lifestyle factor, or infectious agent causes AR‑NSID.

Environmental factors matter in exactly three ways, all of which belong in the differential-diagnosis and prevention sections rather than etiology:

1. **Diagnostic confounding.** Prenatal alcohol exposure, congenital infection (CMV, Zika, rubella, toxoplasmosis), perinatal hypoxic-ischaemic injury, lead and other heavy-metal exposure, and severe early psychosocial deprivation all produce static ID and must be excluded — especially in consanguineous populations where the prior for a genetic cause is high and a coincidental environmental cause can be missed.
2. **Severity modulation.** Iodine deficiency, malnutrition, and educational deprivation act additively on adaptive outcome.
3. **Population risk structure.** Consanguinity is a *sociocultural* variable with a *genetic* consequence — arguably the only "environmental" factor with real effect on AR‑NSID incidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 The class-level causal chain

There is no single AR‑NSID mechanism. The defensible class-level model is a **convergence architecture**:

```
Biallelic LoF in one of ~2500 autosomal genes  [MOLECULAR]
        ↓
Loss of a gene-specific molecular function required by developing neurons
(synaptic proteolysis | vesicle trafficking | glycosylation | tRNA/protein
 modification | transcription/Mediator | signalling | metabolism)  [MOLECULAR]
        ↓
Perturbed neurodevelopmental cellular process
(neurogenesis, neurite outgrowth/branching, synaptogenesis,
 synaptic plasticity, myelination/axonal connectivity)  [CELLULAR]
        ↓
Altered cortical/hippocampal circuit assembly and function  [TISSUE]
        ↓
Impaired learning, memory, and adaptive behaviour = intellectual disability  [ORGANISM]
```

**Suggested GO terms (all verified locally via OAK):**

| GO term | Label |
|---|---|
| `GO:0007399` | nervous system development |
| `GO:0022008` | neurogenesis |
| `GO:0030182` | neuron differentiation |
| `GO:0048666` | neuron development |
| `GO:0021987` | cerebral cortex development |
| `GO:0021895` | cerebral cortex neuron differentiation |
| `GO:0016358` | dendrite development |
| `GO:0030030` | cell projection organization |
| `GO:0050808` | synapse organization |
| `GO:0007268` | chemical synaptic transmission |
| `GO:0050804` | modulation of chemical synaptic transmission |
| `GO:0007611` / `GO:0007612` | learning or memory / learning |
| `GO:0016192` | vesicle-mediated transport |
| `GO:0006487` | protein N-linked glycosylation |
| `GO:0007249` | canonical NF-kappaB signal transduction |
| `GO:0001510` / `GO:0006400` | RNA methylation / tRNA modification |
| `GO:0006417` | regulation of translation |

> ⚠️ `GO:0006486` ("protein glycosylation") is **obsolete** in the current GO release — use `GO:0006487` (protein N-linked glycosylation). Confirmed via OAK.

**Suggested CL terms (verified):** `CL:0000540` neuron · `CL:0000679` glutamatergic neuron · `CL:0000617` GABAergic neuron · `CL:0000047` neural stem cell · `CL:0000127` astrocyte · `CL:0000128` oligodendrocyte · `CL:0002319` neural cell.

**Suggested UBERON terms (verified):** `UBERON:0000955` brain · `UBERON:0000956` cerebral cortex · `UBERON:0002421` hippocampal formation · `UBERON:0001954` Ammon's horn · `UBERON:0002316` white matter · `UBERON:0002037` cerebellum.

### 6.2 Worked mechanism 1 — *PRSS12* / neurotrypsin: synaptic proteolysis

Molinari et al. **[verbatim]**:

> *"A 4-base pair deletion in the neuronal serine protease neurotrypsin gene was associated with autosomal recessive nonsyndromic mental retardation (MR). In situ hybridization experiments on human fetal brains showed that neurotrypsin was highly expressed in brain structures involved in learning and memory. Immuno-electron microscopy on adult human brain sections revealed that neurotrypsin is located in presynaptic nerve endings, particularly over the presynaptic membrane lining the synaptic cleft. These findings suggest that neurotrypsin-mediated proteolysis is required for normal synaptic function and suggest potential insights into the pathophysiological bases of mental retardation."* (PMID:12459588)

Chain: loss of presynaptic neurotrypsin → failure to cleave agrin at the synaptic cleft → loss of the C-terminal agrin-22 fragment that drives dendritic filopodia formation → impaired activity-dependent synaptic remodelling → deficient learning and memory. Scale tags: MOLECULAR → CELLULAR → ORGANISM. Cell type `CL:0000540`; site `UBERON:0002421`.

### 6.3 Worked mechanism 2 — *CC2D1A*: dual NF‑κB and cAMP–PKA–PDE4D dysregulation

Basel-Vanagaite et al. identified *"a protein truncating mutation … in the gene CC2D1A in nine consanguineous families with severe autosomal recessive NSMR,"* encoding *"a putative signal transducer participating in positive regulation of I-kappaB kinase/NFkappaB cascade,"* expressed most highly *"in the cerebral cortex and hippocampus"* (PMID:16033914) **[fragment — re-verify]**.

The better-resolved arm is the cAMP branch. CC2D1A co-localizes with PDE4D and, on cAMP stimulation, escorts it to the cell periphery; the human deletion allele (lacking three of four DM14 domains plus the adjacent C2 domain) abolishes this translocation, causing constitutive PKA phosphorylation of PDE4D at Ser126 and **PDE4D hyperactivity** → excessive cAMP hydrolysis → reduced CREB phosphorylation → memory and social-behaviour deficits. In *Cc2d1a* KO mice, the PDE4 inhibitor **rolipram** (`CHEBI:104872`, verified) rescues spatial memory — **in males only** (PMID:30732858; see §15.3). Structural work on the human CC2D1A fragment associated with NSID was published in *Bioscience Reports* 2026 (BSR20253955).

This is the single best **druggable-mechanism** exemplar in AR‑NSID and the strongest candidate for a `treatments` entry with `target_mechanisms`.

### 6.4 Worked mechanism 3 — *TRAPPC9*: trafficking + NF‑κB + neurite outgrowth

Both 2009 discovery papers converge **[verbatim]**:

> *"Sequence analysis of genes in the candidate interval identified a nonsense nucleotide change in the gene that encodes TRAPPC9 (trafficking protein particle complex 9, also known as NIBP), which has been implicated in NF-kappaB activation and possibly in intracellular protein trafficking. TRAPPC9 is highly expressed in the postmitotic neurons of the cerebral cortex, and MRI analysis of affected patients shows defects in axonal connectivity."* (PMID:20004763)

> *"This gene encodes NIK- and IKK-beta-binding protein (NIBP), which is involved in the NF-kappaB signaling pathway and directly interacts with IKK-beta and MAP3K14."* (PMID:20004765)

Downstream cell biology (from the model literature): TRAPPC9 partners TRAPPC10 to direct TRAPPII toward Rab11 activation, governing recycling-endosome traffic; deficiency impairs **neurite elongation and branching** in both zebrafish and mouse (Int J Biol Sci 2023, PMC10321293), causes disproportionate hippocampal volume loss with **Sox2⁺ neural stem/progenitor cell depletion** and neuronal lipid-droplet accumulation (bioRxiv 2023), and produces a **dopamine D1/D2 neuron imbalance** underlying the learning/memory deficit (PMID:33208359). The obesity arm is discussed in §15.2.

Chain: TRAPPC9 LoF → impaired TRAPPII/Rab11 endosomal recycling **and** reduced NIK/IKKβ-dependent NF‑κB activation → impaired neurite elongation/branching + NSPC depletion → reduced cortical/hippocampal volume, white matter hypoplasia, axonal connectivity defects → ID ± postnatal microcephaly ± obesity.

### 6.5 Recurrent mechanistic themes across the AR‑NSID gene set

| Theme | Genes | GO anchor |
|---|---|---|
| Membrane/vesicle trafficking | TRAPPC9, TRAPPC6B, WASHC4, TBC1D23, PGAP1, AP4M1 | `GO:0016192` |
| Glycosylation & glycoprotein QC | TUSC3, MAN1B1, ST3GAL3, PGAP1, NDST1 | `GO:0006487` |
| RNA/tRNA modification & translation | NSUN2, ADAT3, ELP2, METTL23 | `GO:0001510`, `GO:0006400`, `GO:0006417` |
| Transcriptional regulation | MED23, ZNF526, TET1 | — |
| Synaptic function & proteolysis | PRSS12, GRIK2, MPDZ | `GO:0050808`, `GO:0007268` |
| Intracellular signalling | CC2D1A, TRAPPC9, MAPK8, TNIK, LINS1 (Wnt) | `GO:0007249` |
| Metabolism / lipid | TECR, ADK, IMPA1 | — |
| Cell-cycle / cytoskeleton / neurogenesis | CDK5R1, ABI2, SLAIN1, CRADD | `GO:0022008` |

**Important:** these are *post-hoc groupings*, not a claim of pathway convergence. Jamra's explicit finding is the opposite — no prevalent pathways or complexes. Curate these as organizing themes with that caveat attached.

### 6.6 Immune, metabolic, and tissue-damage mechanisms

- **Immune:** No autoimmunity or immunodeficiency. NF‑κB appears (CC2D1A, TRAPPC9) as a *neurodevelopmental* signalling node, not an inflammatory one. Do not curate as immune-mediated disease.
- **Metabolic:** Only in specific genes (TECR — VLCFA elongation; ADK — adenosine/methionine metabolism; IMPA1 — inositol recycling). No class-level metabolic signature. Absence of a metabolic abnormality is part of the non-syndromic definition.
- **Tissue damage:** **None.** AR‑NSID is a *developmental* disorder, not a degenerative one — no oxidative-stress, ischaemia, fibrosis, or necrosis mechanism. The pathology is a mis-built circuit, not a damaged one. This is a load-bearing distinction for the dismech pathograph.

### 6.7 Molecular profiling

- **Transcriptomics:** the strongest class-level datum is prenatal-brain co-expression enrichment of AR‑NSID genes (PMID:27457812; PMID:28397838). BrainSpan/GTEx/Allen Brain Atlas are the reference resources.
- **Proteomics / metabolomics / lipidomics:** no AR‑NSID class-level signature. Gene-specific exceptions: transferrin isoelectric focusing / glycan mass-spec abnormalities in *MAN1B1* and *TUSC3* (CDG-like); VLCFA profiling in *TECR*.
- **Single-cell / spatial:** no AR‑NSID-specific atlas. Human Cell Atlas and developing-brain scRNA-seq resources are used to establish cell-type expression for candidate genes.
- **Functional genomics:** no AR‑NSID-focused CRISPR screen. DepMap and MorPhiC (see §15.5) are the relevant resources; MorPhiC's iPSC-derived null-allele phenotyping is directly applicable and would license `category: Cellular` phenotypes with `evidence_source: IN_VITRO`.

---

## 7. Anatomical Structures Affected

| Level | Structure | Ontology term (verified) | Involvement |
|---|---|---|---|
| **System** | Nervous system | `UBERON:0001016` (verify) | Primary and, by definition, sole |
| **Organ** | Brain | `UBERON:0000955` | Primary |
| | Cerebral cortex | `UBERON:0000956` | Primary — TRAPPC9 and CC2D1A both show highest expression here |
| | Hippocampal formation / Ammon's horn | `UBERON:0002421` / `UBERON:0001954` | Learning-and-memory substrate; disproportionately reduced in *Trappc9* KO |
| | Cerebral white matter | `UBERON:0002316` | Hypoplasia in *TRAPPC9*; reduced DTI-derived integrity in the KO mouse |
| | Cerebellum | `UBERON:0002037` | Mild atrophy in isolated families only |
| **Tissue** | Nervous tissue; grey and white matter | | |
| **Cell** | Neuron | `CL:0000540` | Principal target |
| | Glutamatergic / GABAergic neuron | `CL:0000679` / `CL:0000617` | E/I balance |
| | Neural stem cell | `CL:0000047` | Sox2⁺ NSPC depletion (*Trappc9*) |
| | Oligodendrocyte | `CL:0000128` | White matter arm |
| | Astrocyte | `CL:0000127` | Supporting |
| **Subcellular** | Synapse / presynapse | `GO:0045202` / `GO:0098793` (verify) | PRSS12, GRIK2, MPDZ |
| | Axon / dendrite | `GO:0030424` / `GO:0030425` (verified) | TRAPPC9 |
| | Endoplasmic reticulum | `GO:0005783` (verify) | TUSC3, MAN1B1, TECR |
| | Golgi / recycling endosome | `GO:0005794` / `GO:0055037` (verify) | TRAPPC9, TBC1D23, WASHC4 |
| | Nucleolus | `GO:0005730` (verify) | NSUN2 mislocalization (PMID:22541562) |

**Lateralization:** bilateral and symmetric throughout — a diffuse developmental process. Focal or asymmetric imaging findings argue against AR‑NSID.

**Secondary organ involvement:** none by definition. Where present (obesity in *TRAPPC9*, retinal disease in *AHI1* WD40 variants) the case is reclassified as syndromic or as an expanded-phenotype allelic disorder.

---

## 8. Temporal Development

- **Onset:** the molecular lesion is present from conception; the clinical phenotype is congenital. Ascertainment typically occurs at 1–4 years for moderate/severe ID (motor and speech milestones) and at school age for mild ID. Onset pattern is **insidious/chronic**, never acute.
- **Progression:** **static (non-progressive) encephalopathy.** The functional gap versus peers widens with age because the developmental trajectory is shallower — this is *apparent* rather than true progression, and the distinction matters clinically and for curation.
- **Stages:** no formal staging system exists. Practical framing: (i) infancy — global developmental delay, `HP:0001263`; (ii) preschool — speech delay dominant; (iii) school age — formal IQ/adaptive testing establishes ID and severity; (iv) adolescence/adulthood — plateau at an adaptive ceiling, with transition-of-care and supported-living needs.
- **Duration:** lifelong.
- **Remission:** none. Spontaneous or treatment-induced remission does not occur.
- **Critical periods:** (a) prenatal/perinatal — the window in which the gene acts, hence the target for hypothetical molecular therapy; (b) birth to ~5 years — the window of maximal neuroplasticity and the evidence-supported window for early intervention; (c) preconception — the only window for effective prevention (§13).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Quantity | Value | Source |
|---|---|---|
| ID overall prevalence | 1–3% of all populations | PMC9946902; PMID:28397838 (*"Approximately 1% of the global population is affected by intellectual disability"*) **[verbatim]**; PMID:20004765 (*"It occurs with a prevalence of approximately 2%"*) **[verbatim]** |
| ARID as fraction of *diagnosable* ID, outbred populations | **~10%** | PMID:30459488 — *"we estimate that ARID makes up about 10% of all diagnosable ID cases in an outbred population"* **[fragment]** |
| ARID in consanguineous populations | **Leading genetic cause** | PMID:29302074 **[verbatim]** |
| Total ID risk, consanguineous vs outbred | **2–3× higher** | PMID:30459488 **[fragment]** |
| Consanguineous share of world population | ~10.4% (second cousins or closer) | Bittles & Black |
| Recessive share of point mutations in a highly consanguineous ID cohort | **81%** | PMID:27431290 — *"The identified point mutations were mostly recessive (n=117, 81%)"* **[verbatim]** |

Derived class-level estimate for dismech `Prevalence`, to be recorded with explicit assumptions: if ID prevalence is ~1–2% and ARID is ~10% of diagnosable ID in outbred settings, class prevalence is on the order of **100–200 per 100,000** in outbred populations (`prevalence_class: ABOVE_1_IN_1000`), and materially higher in highly consanguineous populations. The non-syndromic subset is a fraction of that and cannot be reliably separated with current data. **Record `measure_type: POINT_PREVALENCE`, put the derivation in `notes`, and do not overstate precision.**

### 9.2 Inheritance mechanics

- **Pattern:** autosomal recessive, `HP:0000007` (verified). Recurrence risk 25% per pregnancy for carrier×carrier couples. Hu et al.: *"For autosomal recessive ID (ARID) the recurrence risk is high"* (PMID:24176302) **[verbatim]**.
- **Multi-locus inheritance:** documented in ~6.6% of families (PMID:27457812). Where curated, use `HP:0010983` oligogenic inheritance with the genes named in the block `description` (the `Inheritance` class has no `genes` slot) — see the repo's digenic/oligogenic section and the `PRPH2-Related_Retinopathy` exemplar.
- **Penetrance:** essentially complete for established LoF genotypes in confirmed genes. Reduced penetrance has not been systematically studied and remains a genuine gap.
- **Expressivity:** **highly variable**, both within and between families, and this is arguably the field's central unsolved problem. Jamra **[fragment — re-verify]**: *"there is … accumulating evidence that the spectrum of symptoms due to bi-allelic mutations in established ARID genes may vary enormously"* — with the striking example that *"compound heterozygous pathogenic variants in the WD40 domain of AHI1 … have been reported to lead to an isolated retinitis pigmentosa"* rather than Joubert syndrome (PMID:30459488).
- **Anticipation:** not applicable — no repeat-expansion mechanism.
- **Germline mosaicism:** not a recognized feature; irrelevant to recurrence counselling in the recessive setting.
- **Founder effects:** important and population-specific (Iranian, Pakistani, Arab, Turkish sub-populations). *MAN1B1* is a partial exception to the no-recurrence rule — *"MAN1B1 is one of the few NS-ARID genes with an elevated mutation frequency in patients with NS-ARID from different populations"* (PMID:21763484) **[fragment]**.
- **Carrier frequency:** no class-level figure is meaningful. Per-gene carrier frequencies are ultra-low globally and locally elevated in founder populations.

### 9.3 Population demographics

- **Highest burden:** North Africa, the Middle East, West/Central/South Asia — the consanguinity belt. Study cohorts are overwhelmingly Iranian (Najmabadi/Hu/Kahrizi), Pakistani (Riazuddin, Harripaul, Mir), Saudi/Gulf Arab (Anwar/Alkuraya), and Turkish.
- **Outbred populations:** AR‑NSID is *not* rare there either — this is the central corrective message of Musante & Ropers **[verbatim]**: *"Here we review recent progress in this field, show that ARID is not rare even in outbred Western populations, and discuss the prospects for improving its diagnosis and prevention."* (PMID:24176302). Harripaul et al. concur **[verbatim]**: *"As with other AR disorders, the relevance will also apply to outbred populations."* (PMID:28397838)
- **Sex ratio:** ~1:1 expected for autosomal recessive inheritance. (Contrast X-linked ID, which is male-biased — the male excess in overall ID cohorts is largely XLID plus ascertainment.) **Caveat worth curating:** at least one AR‑NSID gene shows sex-dimorphic biology in the model system — *Cc2d1a* cognitive rescue by PDE4 inhibition is male-specific (§15.3) — and *Trappc9* KO obesity is *"significantly more severe in females than in males."*
- **Age distribution:** all ages; lifelong condition; prevalence in adults reflects the full lifetime cohort.

### 9.4 Ascertainment bias — read every number above with this in mind

The AR‑NSID evidence base is derived almost exclusively from **multiplex consanguineous families with moderate-to-severe ID**. This design systematically over-represents severe phenotypes and LoF alleles, under-represents mild ID and hypomorphic alleles, and under-represents compound heterozygosity (which is the dominant recessive mechanism in outbred populations). Any frequency, severity, or prevalence claim curated from this literature should carry that caveat.

---

## 10. Diagnostics

### 10.1 Genetic testing — the diagnostic backbone

The consensus is unambiguous. Jamra: *"a genetic diagnosis of ID in general, and ARID specifically, is better made using large panels or exome sequencing"* (PMID:30459488) **[fragment]**, and *"there is no justification for a gene-specific or panel diagnostic when ARID is suspected."* Anwar et al. conclude **[verbatim]**: *"Our results expand the morbid genome of ID and support the adoption of genomics as a first-tier test for individuals with ID."*

**Diagnostic yields (all figures verbatim from the cited abstracts unless noted):**

| Setting | Modality | Yield | Source |
|---|---|---|---|
| 337 ID subjects (highly consanguineous) | Genomics-first (CMA + panel + ES) | **58%** — vs 16% suggested / 11% confirmed by standard clinical evaluation | PMID:27431290 |
| Same cohort, ES applied to all CMA-negative cases | ES | **60% (77/129)** | PMID:27431290 |
| 192 multiplex Pakistani/Iranian consanguineous families | Microarray + HBD + CNV + WES | **51%** of families, 72 genes | PMID:28397838 |
| 121 large consanguineous Pakistani families | WES | **60/121 (~50%)** with a single-gene answer (30 known + 30 novel genes) | PMID:27457812 |
| 404 consanguineous families (mostly Iranian) | WES/WGS | **219/404 (54%)** likely causative; 77 known + 77 novel AR‑ID genes, 21 X-linked, 9 previously non-ID genes | PMID:29302074 |
| Mixed ID (non-consanguineous), meta-analysis | ES | 36% overall NDD; **31% isolated (non-syndromic) NDD**; 53% syndromic NDD | cited in PMID:34930158 |
| Genome sequencing, cumulative | GS | 62% (de novo SNV 39%, de novo CNV 21%, **recessive 2%** — outbred cohort) | Gilissen, cited in PMID:34930158 |
| Iran, 2025 | Proband-only ES | **40.4%**, → 45.4% with CNV, → 50.5% with parental testing | Ghalamkari 2025, *AJMG A* |

**Note the isolated-vs-syndromic split (31% vs 53%):** non-syndromic ID has a *lower* ES yield than syndromic ID. This is a curatable, decision-relevant number.

**Recommended workflow:**
1. **Chromosomal microarray** — first-tier; detects homozygous deletions and the 14% CNV fraction. Karyotype only for suspected balanced rearrangement or aneuploidy; FISH only for targeted confirmation.
2. **Fragile X (*FMR1*) repeat testing** — still first-tier in most guidelines; 1% of the Anwar cohort. Not AR, but a mandatory exclusion.
3. **Trio exome sequencing** — the workhorse. Trio design is essential: it distinguishes de novo dominant from recessive, and Kahrizi et al. showed that de novo mutations occur in consanguineous families too, which homozygosity-mapping-only designs systematically miss (*Clin Genet* 2019;95(1):151–159).
4. **Genome sequencing** — reflex for ES-negative cases; adds deep-intronic, structural, and repeat variants.
5. **Homozygosity/autozygosity mapping** — high-value adjunct in consanguineous pedigrees; ROH data come free from CMA or can be derived from ES/GS.
6. **RNA sequencing on an accessible tissue** — reflex for ES/GS-negative cases; resolves splice-altering variants of uncertain significance.
7. **Reanalysis at 18–24 months** — the DDD experience (27% → 40% on reanalysis) makes this the highest-yield, lowest-cost intervention in the whole pathway.

**Gene panels:** large "intellectual disability" / neurodevelopmental panels (e.g. Genomics England PanelApp *Intellectual disability – microarray and sequencing*) are widely used but are explicitly *not* recommended over ES for suspected ARID because the gene set is too large and too incomplete. Mitochondrial DNA testing and repeat-expansion panels are relevant only for specific differentials, not for AR‑NSID.

### 10.2 Laboratory and biochemical testing

There are **no diagnostic biomarkers for AR‑NSID as a class** — the absence of biochemical abnormality is part of the definition. Metabolic testing is performed to *exclude* treatable IEMs (see §10.5): plasma amino acids, urine organic acids, acylcarnitine profile, ammonia, lactate, homocysteine, copper/ceruloplasmin, creatine metabolites, biotinidase, CDG transferrin isoelectric focusing, thyroid function, lead level.

Gene-specific exceptions worth curating: abnormal transferrin glycoforms in *MAN1B1*/*TUSC3*; VLCFA abnormalities in *TECR*.

### 10.3 Imaging and electrophysiology

- **Brain MRI:** normal or near-normal by definition; performed to exclude malformations of cortical development, leukodystrophy, and acquired injury. Positive findings (white-matter hypoplasia, mild cerebellar atrophy) exist for specific genes.
- **EEG:** indicated only if seizures are suspected.
- **Nerve conduction / EMG, ECG:** not indicated absent specific features; their necessity would itself argue against a non-syndromic classification.
- **Biopsy / histopathology:** not indicated. No characteristic histopathology exists.

### 10.4 Clinical diagnostic criteria

**DSM-5-TR, Intellectual Developmental Disorder (317–319 / F70–F73)** — all three required:
- (A) deficits in intellectual functions confirmed by clinical assessment and standardized testing;
- (B) deficits in adaptive functioning across conceptual, social, and practical domains;
- (C) onset during the developmental period.
Severity is specified by **adaptive functioning**, not IQ.

**ICD-11 6A00** grades by both intellectual functioning and adaptive behaviour (~2 SD below mean; 6A00.0 mild → 6A00.3 profound; 6A00.4 provisional).

**"Non-syndromic" designation** is a clinical judgement, not a criterion set: ID without a consistent pattern of dysmorphism, congenital malformation, neurological signs, growth abnormality, metabolic derangement, or characteristic neuroimaging. It should always be recorded as provisional pending deep phenotyping and follow-up.

**Standard instruments:** WISC-V / WPPSI-IV / WAIS-IV / Stanford-Binet-5 (or Bayley-4 / Mullen in infancy); Vineland-3 or ABAS-3 for adaptive behaviour.

### 10.5 Differential diagnosis

| Category | Discriminating feature |
|---|---|
| **De novo autosomal dominant ID** | The dominant cause in outbred/simplex settings; distinguished only by trio sequencing |
| **X-linked ID** | Male-predominant pedigree; maternal transmission; *FMR1* first |
| **Syndromic ARID** | Dysmorphism, malformation, growth or organ involvement — often only apparent on re-examination or with age |
| **Chromosomal / CNV disorders** | CMA-detectable |
| **Treatable inborn errors of metabolism** | PKU, homocystinuria, creatine deficiency syndromes, biotinidase deficiency, CDG. **Highest-priority exclusion — these change management** |
| **Congenital hypothyroidism** | Newborn screening; treatable |
| **Fetal alcohol spectrum disorder** | Exposure history; facial features |
| **Congenital infection (CMV, Zika, rubella, toxoplasma)** | Serology/PCR; imaging calcifications; hearing loss |
| **Perinatal hypoxic-ischaemic encephalopathy** | Birth history; MRI pattern |
| **Cerebral palsy with ID** | Motor signs predominate |
| **Autism spectrum disorder without ID** | Formal cognitive testing separates them |
| **Progressive/degenerative disease** | **Regression (`HP:0002376`) excludes AR‑NSID** — the key discriminator |
| **Severe psychosocial deprivation** | History; partial catch-up with intervention |

### 10.6 Screening

- **Newborn screening:** does **not** detect AR‑NSID (no biochemical marker). It does detect several key differentials (PKU, congenital hypothyroidism, biotinidase deficiency) — an important negative to state.
- **Carrier screening:** the operative modality. Expanded carrier screening panels include a growing but incomplete subset of ARID genes; in consanguineous couples, **couple-based exome/genome carrier screening** outperforms fixed panels because the relevant allele is often population- or family-private.
- **Cascade screening:** offer to at-risk relatives once the family variant is known — high-value in extended consanguineous kindreds.

---

## 11. Outcome / Prognosis

- **Survival:** for AR‑NSID *sensu stricto*, life expectancy is near-normal or modestly reduced. Excess mortality in the ID population generally is driven by epilepsy, aspiration, immobility, and reduced access to healthcare — largely features of *syndromic* ID. No AR‑NSID-specific survival data were located. **Genuine evidence gap.**
- **Mortality:** no disease-specific mortality data at class level. Do not fabricate a figure.
- **Morbidity and disability:** lifelong cognitive and adaptive impairment is the dominant morbidity. GBD captures "idiopathic developmental intellectual disability" as a YLD-generating cause; ICF is the appropriate functional-classification framework.
- **Disease course:** static; no recovery of the underlying deficit. Adaptive function improves with intervention, education, and support — the developmental trajectory is shallower, not descending.
- **Complications:** behavioural and psychiatric comorbidity (ADHD, autism, anxiety, self-injury), epilepsy in a subset, communication-related social isolation, and dependency needs in adulthood.
- **Prognostic factors:** severity of ID at diagnosis; expressive language attainment by age 5 (the strongest practical predictor of adaptive outcome in the broader ID literature); presence of epilepsy; the specific gene and allele; access to early intervention and educational support; family resources.
- **Prognostic biomarkers:** none. The molecular diagnosis itself is the best available prognostic instrument, via gene-specific natural-history data where it exists.

---

## 12. Treatment

**There is no disease-modifying therapy for AR‑NSID.** Management is supportive, habilitative, and educational, plus targeted treatment of comorbidities. State this plainly in the entry.

### 12.1 Supportive and rehabilitative care (the mainstay)

| Intervention | NCIT term (verified via OAK) | `therapeutic_modality` |
|---|---|---|
| Early intervention / developmental therapy | `NCIT:C15315` Rehabilitation | `BEHAVIORAL` |
| Speech and language therapy | `NCIT:C159273` Speech Language Therapy | `BEHAVIORAL` |
| Occupational therapy | `NCIT:C121351` Occupational Therapy | `BEHAVIORAL` |
| Physical therapy | `NCIT:C15302` Physical Therapy | `BEHAVIORAL` |
| Special education / individualized education programme | `NCIT:C181743` Behavioral Counseling (nearest available) | `BEHAVIORAL` |
| Applied behaviour analysis / behavioural intervention | `NCIT:C181743` Behavioral Counseling | `BEHAVIORAL` |
| Genetic counselling | `NCIT:C15240` Genetic Counseling | `OTHER` |
| Supportive / multidisciplinary care | `NCIT:C15747` Supportive Care | `OTHER` |

Per the repo's mechanical-backfill table, `NCIT:C15302`, `NCIT:C159273`, `NCIT:C121351`, and `NCIT:C181743` all map to `therapeutic_modality: BEHAVIORAL`.

### 12.2 Pharmacotherapy — symptomatic only

No drug treats ID itself. Comorbidity-directed agents: stimulants and alpha-2 agonists for ADHD; SSRIs for anxiety/OCD; atypical antipsychotics (risperidone, aripiprazole) for severe irritability/aggression; anti-seizure medication where epilepsy is present; melatonin for sleep. Use `treatment_term: NCIT:C15986` Pharmacotherapy with a specific `therapeutic_agent` (CHEBI for small molecules).

### 12.3 The one mechanism-targeted lead: PDE4 inhibition in *CC2D1A*

**Preclinical (mouse) only — must be curated with `evidence_source: MODEL_ORGANISM` and must not be presented as a human therapy.** In *Cc2d1a*-deficient mice, PDE4D hyperactivity depletes cAMP and impairs CREB signalling; the PDE4 inhibitor **rolipram** (`CHEBI:104872`, verified) rescues spatial-memory deficits — **in males only** (PMID:30732858, *Biol Psychiatry*). This is the closest thing AR‑NSID has to a druggable node and is a strong candidate for a `target_mechanisms` treatment edge pointing at the "PDE4D hyperactivity" pathophysiology node with `INHIBITS`.

A second, weaker lead: chronic pharmacologic manipulation of dopamine transmission ameliorates the *metabolic* disturbance in *Trappc9*-linked syndrome in mice (PMC11383600, 2024) — metabolic, not cognitive, rescue.

### 12.4 Advanced therapeutics

- **Gene therapy / gene editing / ASO / siRNA:** none in development for any AR‑NSID gene, and the barriers are structural, not merely technical — (i) ~2500 candidate genes make per-gene development economically infeasible; (ii) the causal window is prenatal/early-postnatal, before diagnosis; (iii) the pathology is a mis-built circuit, not an ongoing degenerative process, so post-hoc restoration of gene function may not restore function. Recessive LoF biology is, in principle, gene-replacement-friendly — the timing problem is the real obstacle.
- **Cell therapy, immunotherapy, targeted therapy:** not applicable.
- **Surgery:** not applicable to the ID itself.

### 12.5 Clinical trials

No AR‑NSID-specific interventional trial was identified. One observational study of relevance: **NCT06706934** — *Search for Phenotype-modifying Genes in Patients With Intellectual Disabilities* (verify status, phase, and sponsor on ClinicalTrials.gov, and fetch with `just fetch-reference NCT06706934` before curating).

### 12.6 Pharmacogenomics

No AR‑NSID-specific PGx. Standard CPIC guidance applies to the psychotropics used for comorbidities (CYP2D6/CYP2C19 for SSRIs and atomoxetine; HLA-B*15:02 for carbamazepine in relevant ancestries).

---

## 13. Prevention

Prevention is where AR‑NSID has the **most actionable evidence** — and it is entirely preconception/reproductive rather than therapeutic. Musante & Ropers frame the field's ambition as improving *"its diagnosis and prevention"* (PMID:24176302) **[verbatim]**.

- **Primary prevention.** Genetic counselling about consanguinity risk; preconception and premarital carrier screening; population health education. National **Premarital Screening and Genetic Counseling (PMSGC)** programmes operate in Saudi Arabia and several Gulf and Middle Eastern states; community survey data show 84.4% of respondents correctly identify consanguinity as increasing autosomal recessive risk and 89.3% recognize that genetic counselling reduces family recurrence (Front Genet 2026;1866894). Note the ethical framing: the objective is *informed reproductive choice*, not discouragement of consanguineous marriage — this should be stated explicitly in the entry.
- **Secondary prevention.** For a couple with an affected child and a known molecular diagnosis: prenatal diagnosis (CVS/amniocentesis) or preimplantation genetic testing for monogenic disease (PGT-M), with 25% recurrence risk counselling. Cascade carrier testing across the extended kindred. Early developmental screening for at-risk siblings enables intervention at the point of maximal plasticity.
- **Tertiary prevention.** Early intervention services; epilepsy control; treatment of hearing and vision impairment (which compound the cognitive deficit); behavioural support; nutritional management (relevant for *TRAPPC9*-associated obesity); transition planning.
- **Immunization:** no AR‑NSID-specific vaccine. Routine immunization prevents ID-causing congenital infections (rubella) and is a legitimate public-health adjacency.
- **Newborn screening:** does not detect AR‑NSID (§10.6).

---

## 14. Other Species / Natural Disease

- **Taxonomy of relevance:** *Homo sapiens* `NCBITaxon:9606`. Experimental orthologs: *Mus musculus* `NCBITaxon:10090`, *Danio rerio* `NCBITaxon:7955`, *Drosophila melanogaster* `NCBITaxon:7227`, *Caenorhabditis elegans* `NCBITaxon:6239`.
- **Naturally occurring disease in other species:** **None recognized.** AR‑NSID is a human-specific nosological construct. Intellectual disability requires a construct (IQ, adaptive functioning) that has no cross-species equivalent, so no OMIA entry corresponds to AR‑NSID. I found no OMIA entry for canine or other companion-animal inherited cognitive impairment matching this class. **Curate this section as "not applicable" rather than stretching for an analogue.**
- **Breed (VBO):** not applicable.
- **Comparative biology.** Evolutionary conservation of the *molecular* machinery is well demonstrated even though the *disease* is not: the *Drosophila* NSUN2 ortholog deletion produces *"severe short-term-memory (STM) deficits"* rescuable by wild-type re-expression, indicating *"an evolutionarily conserved role of RNA methylation in normal cognitive development"* (PMID:22541559) **[fragment]**. The *PRSS12*/neurotrypsin ortholog *tequila* regulates long-term memory formation in *Drosophila*. *Trappc9* deficiency impairs neurite elongation and branching in **both zebrafish and mice** (PMC10321293).
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious, non-transmissible).

---

## 15. Model Organisms

### 15.1 Overview

There is no model of "AR‑NSID" — only gene-specific models. Recapitulation is judged by learning/memory assays plus brain morphometry, not by a cognitive construct.

### 15.2 *Trappc9* — the best-characterized model

Wang et al., PLoS Genetics 2020 **[verbatim]**:

> *"By studying Trappc9 null mice we discovered that homozygous mutant mice showed a reduction in brain size, exploratory activity and social memory, as well as a marked increase in body weight. A role for Trappc9 in energy balance was further supported by increased ad libitum food intake in a child with TRAPPC9 deficiency. … Taken together, we conclude that Trappc9 deficient mice recapitulate key pathological features of TRAPPC9 mutations in humans and identify a role for Trappc9 and its imprinting in controlling brain development and metabolism."* (PMID:32877400)

Additional findings across the *Trappc9* model literature:
- Cognitive/memory/learning impairment across Morris water maze, Barnes maze, and social learning.
- Disproportionate **hippocampal** volume reduction with loss of **Sox2⁺ neural stem/progenitor cells** and neuronal lipid-droplet accumulation (bioRxiv 2023.11.20.567859 — *preprint, not peer-reviewed; flag as such*).
- **DTI** shows reduced white-matter organization/integrity; high-resolution MRI shows multiple regions of reduced volume (ISMRM 2022 abstract — *conference abstract, low evidence tier*).
- **Dopamine D1/D2 neuron imbalance** as the proximate cause of learning/memory deficits (PMID:33208359).
- Obesity with hyperinsulinemia, glucose intolerance, and raised plasma lipids, **more severe in females**.
- Chronic dopaminergic pharmacologic manipulation ameliorates the metabolic disturbance (PMC11383600, 2024).
- Zebrafish *trappc9* knockdown/knockout: defective neurite elongation and branching (PMC10321293).

**Fidelity:** good for microcephaly, obesity, and learning/memory. **Limitation:** the mouse cannot model ID as a construct; and the parent-of-origin effect adds a layer whose human relevance is only partially established (the increased ad libitum food intake in one child is suggestive but n=1).

### 15.3 *Cc2d1a*

Constitutive *Cc2d1a* KO is perinatally lethal, so **conditional (cortex/hippocampus) deletion** is the workhorse. Phenotype: cognitive and social deficits, hyperactivity, anxiety, and self-injury **in males**. Mechanism: PDE4D hyperactivity → cAMP depletion → reduced CREB signalling. **Rescue: PDE4 inhibition restores spatial memory in males but has no effect in females** (PMID:30732858). A companion study dissected *Cc2d1a* vs its homolog *Cc2d1b*, which *"differentially affect spatial memory, anxiety, and hyperactivity"* (PMC5840150, Front Genet 2018). The sex-specificity is a major translational caveat and should be curated explicitly.

### 15.4 Other gene-specific models

| Gene | Models | Phenotype |
|---|---|---|
| *NSUN2* | *Drosophila* ortholog deletion; mouse KO | Severe short-term-memory deficit, rescuable by WT re-expression (PMID:22541559) |
| *PRSS12* | Mouse KO; *Drosophila tequila* | Impaired agrin cleavage; LTM formation defect in fly |
| *TUSC3* | Mouse KO; yeast OST-complex biology | Hypoglycosylation |
| *GRIK2* | *Grik2*/GluR6 KO mouse | Altered hippocampal synaptic transmission and LTP |

### 15.5 Model types and resources

- **Genetic model types:** knockout, conditional (Cre-lox), knock-in of patient missense alleles, humanized alleles, transgenic rescue.
- **Cellular models:** patient-derived **iPSCs** and iPSC-derived neurons/cortical organoids — the most human-relevant platform, and the one that can address the cell-autonomy and cell-type-specificity questions the mouse cannot. **MorPhiC** (null alleles of human genes in iPSC-derived multicellular systems) is directly applicable; MorPhiC-derived phenotypes should be curated as `category: Cellular` with `evidence_source: IN_VITRO`.
- **Databases:** MGI, IMPC, KOMP, IMSR, EMMA, MMRRC (mouse); ZFIN (zebrafish); FlyBase; WormBase; Alliance of Genome Resources; Cellosaurus (lines).

### 15.6 Shared limitations (candidates for `kind: HUMAN_MODEL_MISMATCH`)

Per the repo's guidance, these are *not* generic `KNOWLEDGE_GAP` items — evidence exists in the model, but translational validity is the open question:

1. **ID is not modellable.** Rodent learning/memory assays are proxies for a construct (IQ + adaptive functioning) with no animal equivalent.
2. **Human-specific cortical biology.** Outer radial glia and OSVZ-driven cortical expansion are absent or minimal in mouse — directly relevant to the microcephaly-adjacent AR‑NSID genes.
3. **Sex-dimorphic rescue.** *Cc2d1a* PDE4-inhibitor rescue works in males only; the human correlate is unknown.
4. **Imprinting divergence.** Parent-of-origin *Trappc9* bias is established in mouse brain; the extent of the same bias in human brain, and its clinical consequence for maternal-allele heterozygotes, is unresolved.
5. **Background and allele-type effects.** Most models are null alleles on inbred backgrounds; most human alleles are missense/hypomorphic on outbred backgrounds.

---

## 16. Curation guidance for the dismech entry

A few structural recommendations, offered because they materially affect how this entry should be built:

1. **Consider a `kb/groupings/` entity, not (only) a `Disease`.** AR‑NSID is a MONDO grouping node with 72 descendants and ~56 causal genes and no shared mechanism. It maps cleanly onto the `Grouping` class: `grouping_basis: [SHARED_PHENOTYPE, OTHER]` (shared phenotype + shared inheritance mode), with a `NECESSARY` `membership_criteria` block combining `HAS_PHENOTYPE HP:0001249`, `HAS_INHERITANCE` (autosomal recessive), and a **negated** leaf for syndromic features. That structure is honest about what the class is: a union defined by a phenotype plus an inheritance mode plus a negation, not a mechanism. The `Digenic_and_Oligogenic_Disorders` grouping is a close precedent for a criteria-defined union with a `HAS_INHERITANCE` criterion.

2. **If a `Disease` entry is retained**, keep the pathophysiology graph at the *architecture* level (§6.1) with two or three fully-evidenced worked mechanisms (*PRSS12*, *CC2D1A*, *TRAPPC9*) as exemplars — do not attempt 56 gene-specific chains. Use `biological_scale` tags per the four-value enum; the chain in §6.1 is already atomized to one scale per node.

3. **Do not transcribe the Monarch-propagated HPO set** (§3.3). Spasticity, cerebral visual impairment, and the ear-morphology cluster are inherited from syndromic descendants and contradict the class definition.

4. **NEC preflight is low-risk here but not zero.** "Non-syndromic intellectual disability" has both AD and AR forms with parallel numbered series (MRD/MRT), and MONDO carries both `MONDO:0019502` (AR) and an AD counterpart. Any deep-research report used for this entry should be checked for AD/AR series confusion — this falls squarely in the "numbered series" high-NEC-risk class.

5. **A curious MONDO artifact worth surfacing rather than propagating:** `MONDO:0019502` asserts `is_a MONDO:0017706` (*disorder of carbohydrate transmembrane transport and absorption*). That parentage looks like an ontology defect — presumably leaked from a glycosylation-related descendant (*TUSC3*, *MAN1B1*, *ST3GAL3*) — and should not be reflected in the dismech classification. Consider filing it upstream with MONDO.

6. **Evidence gaps worth curating as `discussions`:** (a) `KNOWLEDGE_GAP` — no AR‑NSID-specific survival, mortality, or QoL data; (b) `KNOWLEDGE_GAP` — penetrance and expressivity systematically unstudied; (c) `HUMAN_MODEL_MISMATCH` — the five items in §15.6.

7. **Every snippet marked [fragment] above must be re-fetched** with `just fetch-reference` and validated before it enters a YAML file. The fully-verbatim set (PMIDs 21937992, 28397838, 27431290, 24176302, 27457812, 29302074, 12459588, 20004763, 20004765, 32877400, 26912939, 34930158) is the safest starting pool.

---

## Reference list

**Verbatim-retrieved abstracts (safe snippet pool):**

| PMID | Citation |
|---|---|
| 21937992 | Najmabadi H, et al. Deep sequencing reveals 50 novel genes for recessive cognitive disorders. *Nature*. 2011;478(7367):57-63 |
| 28397838 | Harripaul R, et al. Mapping autosomal recessive intellectual disability: combined microarray and exome sequencing identifies 26 novel candidate genes in 192 consanguineous families. *Mol Psychiatry*. 2018;23(4):973-984 |
| 27431290 | Anwar/Alkuraya et al. Clinical genomics expands the morbid genome of intellectual disability and offers a high diagnostic yield. *Mol Psychiatry*. 2017;22(4):615-624 |
| 24176302 | Musante L, Ropers HH. Genetics of recessive cognitive disorders. *Trends Genet*. 2014;30(1):32-9 |
| 27457812 | Riazuddin S, et al. Exome sequencing of Pakistani consanguineous families identifies 30 novel candidate genes for recessive intellectual disability. *Mol Psychiatry*. 2017;22(11):1604-1614 |
| 29302074 | Hu H, et al. Genetics of intellectual disability in consanguineous families. *Mol Psychiatry*. 2019;24(7):1027-1039 |
| 12459588 | Molinari F, et al. Truncating neurotrypsin mutation in autosomal recessive nonsyndromic mental retardation. *Science*. 2002;298(5599):1779-81 |
| 20004763 | Mochida GH, et al. A truncating mutation of TRAPPC9 is associated with autosomal-recessive intellectual disability and postnatal microcephaly. *Am J Hum Genet*. 2009;85(6):897-902 |
| 20004765 | Mir A, et al. Identification of mutations in TRAPPC9, which encodes the NIK- and IKK-beta-binding protein, in nonsyndromic autosomal-recessive mental retardation. *Am J Hum Genet*. 2009;85(6):909-15 |
| 32877400 | Wang H, et al. Trappc9 deficiency causes parent-of-origin dependent microcephaly and obesity. *PLoS Genet*. 2020 |
| 26912939 | Davies G, et al. Examining non-syndromic autosomal recessive intellectual disability (NS-ARID) genes for an enriched association with intelligence differences. *Intelligence*. 2016 |
| 34930158 | Chiurazzi-group review. Intellectual disability genomics: current state, pitfalls and future challenges. *BMC Genomics*. 2021 |

**Fragment-retrieved — re-verify before quoting:** 30459488 (Abou Jamra R. Genetics of autosomal recessive intellectual disability. *Med Genet*. 2018;30(3):323-327) · 18452889 (Garshasbi M, et al. *Am J Hum Genet*. 2008;82(5):1158-64, TUSC3) · 21763484 (Rafiq MA, et al. *Am J Hum Genet*. 2011;89(1):176-82, MAN1B1) · 21513506 (Khan MA, et al. *BMC Med Genet*. 2011;12:56, TUSC3) · 22541559 (Khan MA, et al. *Am J Hum Genet*. 2012, NSUN2) · 22541562 (Abbasi-Moheb L, et al. *Am J Hum Genet*. 2012, NSUN2) · 16033914 (Basel-Vanagaite L, et al. *J Med Genet*. 2006, CC2D1A) · 30732858 (*Biol Psychiatry*, Cc2d1a/PDE4D male-specific rescue) · 33208359 (Trappc9 D1/D2 imbalance) · 19805052 (Bittles & Black, *PNAS*, consanguinity) · Kahrizi K, et al. *Clin Genet*. 2019;95(1):151-159 (trio sequencing in consanguineous families) · Ghalamkari S, et al. *Am J Med Genet A*. 2025 (proband-only ES, Iran).

**Databases consulted:** MONDO (via OAK `sqlite:obo:mondo`), HPO / GO / CL / UBERON / NCIT / CHEBI / HGNC (via OAK, all terms in this report verified), Monarch Initiative API v3, MedGen, OMIM PS249500 (*inaccessible — HTTP 403; retrieve directly*), Orphanet ORPHA:88616 (*inaccessible — bot protection; retrieve directly or via `just structured-rebuild-orphanet --id 88616`*), SysID, ClinicalTrials.gov, PubMed/E-utilities.

**Sources:**
- [Deep sequencing reveals 50 novel genes for recessive cognitive disorders — PubMed](https://pubmed.ncbi.nlm.nih.gov/21937992/)
- [Mapping autosomal recessive intellectual disability: 26 novel candidate genes in 192 consanguineous families — PubMed](https://pubmed.ncbi.nlm.nih.gov/28397838/)
- [Genetics of autosomal recessive intellectual disability — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6223757/)
- [Genetics of intellectual disability in consanguineous families — PubMed](https://pubmed.ncbi.nlm.nih.gov/29302074/)
- [Exome sequencing of Pakistani consanguineous families identifies 30 novel candidate genes — Mol Psychiatry](https://www.nature.com/articles/mp2016109)
- [Trappc9 deficiency causes parent-of-origin dependent microcephaly and obesity — PubMed](https://pubmed.ncbi.nlm.nih.gov/32877400/)
- [Male-Specific cAMP Signaling in the Hippocampus Controls Spatial Memory Deficits — PubMed](https://pubmed.ncbi.nlm.nih.gov/30732858/)
- [Loss of Cc2d1a and Cc2d1b Differentially Affect Spatial Memory, Anxiety, Hyperactivity — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5840150/)
- [Defective neurite elongation and branching in Nibp/Trappc9 deficient zebrafish and mice — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10321293/)
- [Intellectual disability genomics: current state, pitfalls and future challenges — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8686650/)
- [Examining NS-ARID genes for an enriched association with intelligence differences — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4725222/)
- [Non-syndromic Intellectual Disability: An Experimental In-Depth Exploration — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9946902/)
- [Phosphodiesterase activity is regulated by CC2D1A — PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC3704924)
- [Consanguinity, human evolution, and complex diseases — PNAS](https://www.pnas.org/doi/10.1073/pnas.0906079106)
- [Proband-Only Exome Sequencing for Intellectual Disability in Iran — AJMG A 2025](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.63915?af=R)
- [Effect of inbreeding on intellectual disability revisited by trio sequencing — Clin Genet](https://onlinelibrary.wiley.com/doi/abs/10.1111/cge.13463)
- [Chronic pharmacologic manipulation of dopamine transmission in Trappc9-linked syndrome — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11383600/)
- [Community awareness of genetic disorders associated with consanguineous marriage — Frontiers in Genetics](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2026.1866894/full)
- [Monarch Initiative — MONDO:0019502](https://api.monarchinitiative.org/v3/api/entity/MONDO:0019502)
- [OMIM Phenotypic Series PS249500](https://www.omim.org/phenotypicSeries/PS249500)