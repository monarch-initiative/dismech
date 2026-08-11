---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T09:43:40.997655'
end_time: '2026-08-01T10:00:11.379626'
duration_seconds: 990.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: VPS4A-Related Neurodevelopmental Syndrome
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
  web_search_requests: 11
  num_turns: 69
  total_cost_usd: 5.310359999999999
  session_id: f11379ef-ad09-42a7-90e6-292e7f5b0983
  stop_reason: end_turn
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** VPS4A-Related Neurodevelopmental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **VPS4A-Related Neurodevelopmental Syndrome** covering all of the
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

# VPS4A-Related Neurodevelopmental Syndrome (CIMDAG Syndrome)
## Comprehensive Disease Research Report

**Prepared:** 2026-08-01 · **Target MONDO:** `MONDO:0035819` · **Category:** Mendelian (monogenic, ultra-rare)

> **Curation caveat for downstream evidence entry:** quotations below were extracted through automated page-fetch tooling. Per the dismech SOP, every PMID must be re-fetched with `just fetch-reference PMID:XXXXXXXX` and every `snippet:` re-verified as an exact substring of the cached abstract before commit. Where I could confirm a passage reads as authentic abstract text I have marked it **[abstract]**; passages marked **[body/derived]** are from full text or secondary sources and are higher-risk for snippet mismatch.

---

## 1. Disease Information

### Overview

VPS4A-related neurodevelopmental syndrome — formally **CIMDAG syndrome** — is an ultra-rare multisystem Mendelian disorder caused by missense variants in *VPS4A*, which encodes the AAA-ATPase that disassembles and recycles the ESCRT-III membrane-remodeling machinery. The clinical core is a severe, congenital-onset neurodevelopmental phenotype (profound global developmental delay, severe primary microcephaly, dystonia, structural brain malformation) combined with a **transfusion-dependent congenital dyserythropoietic/hemolytic anemia**, **congenital cataracts and retinal dystrophy**, and **severe growth retardation**. It is one of the very few human diseases in which a core ESCRT component is the primary genetic lesion, and it is mechanistically distinctive in that pathogenesis is **dominant-negative poisoning of a hexameric enzyme**, not haploinsufficiency.

The acronym CIMDAG expands to: **c**erebellar hypoplasia and **c**ataracts, **i**ntellectual disability, congenital **m**icrocephaly, **d**ystonia and dyserythropoietic **a**naemia, **g**rowth retardation ([Unique/Rare Chromosome Disorder Support Group, 2024](https://rarechromo.org/media/singlegeneinfo/Single%20Gene%20Disorder%20Guides/CIMDAG%20syndrome%20FTNW.pdf)).

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | `MONDO:0035819` — "cerebellar hypoplasia-intellectual disability-congenital microcephaly-dystonia-anemia-growth retardation syndrome" |
| **OMIM (phenotype)** | **#619273** — CIMDAG SYNDROME; CIMDAG |
| **OMIM (gene)** | *609982 — VACUOLAR PROTEIN SORTING 4 HOMOLOG A; VPS4A |
| **Orphanet** | ORPHA:603448 |
| **MedGen** | UID 1780242 |
| **UMLS** | C5543287 |
| **GARD** | 0018020 |
| **HGNC** | HGNC:13488 (*VPS4A*) |
| **NCBI Gene** | 27183 |
| **Ensembl** | ENSG00000132612 |
| **UniProt** | Q9UN37 (VPS4A_HUMAN) |
| **RefSeq transcript** | NM_013245.3 |
| **Cytoband** | 16q22.1 |
| **ICD-11** | No specific code; best fit `LD2F.1Y` (other specified syndromes with CNS anomalies as major feature) / `4A00.1` family not applicable. **Not separately coded.** |
| **ICD-10** | No specific code; Q87.8 (other specified congenital malformation syndromes) used pragmatically |
| **MeSH** | No dedicated descriptor as of 2026 |

Cross-references verified via OLS4 (MONDO term record) and HGNC REST.

### Synonyms and alternative names

- CIMDAG syndrome (preferred acronym)
- VPS4A-related neurodevelopmental disorder (VPS4A-ND) — the label used by the Unique family guide
- Cerebellar hypoplasia–intellectual disability–congenital microcephaly–dystonia–anemia–growth retardation syndrome (MONDO/Orphanet long form)
- Syndromic congenital dyserythropoietic anemia due to *VPS4A* (hematology literature framing; Seu et al.)
- Syndromic congenital hemolytic anemia with neurodevelopmental impairment (Lunati et al. framing)
- *Gene aliases relevant to older literature:* SKD1, SKD1A, SKD2, VPS4, VPS4-1, hVPS4

### Nature of the evidence base

**Entirely individual-patient derived, not aggregated.** The whole disease concept rests on ~11 published probands described in four primary reports plus deep single-patient functional workups. There is **no EHR-based cohort, no registry-derived prevalence, and no natural history study**. The only registry involvement is indirect: three of the probands were ascertained through the **Congenital Dyserythropoietic Anemia Registry (CDAR, NCT02964494**, Cincinnati Children's, observational, actively recruiting), which is a CDA-wide registry rather than a VPS4A-specific one. Aggregated resources (OMIM, Orphanet, HPO annotation file) are themselves derived from the same handful of case reports — so HPO frequencies such as "6/6" and "4/5" are literally patient counts from Rodger et al., not epidemiologic estimates.

---

## 2. Etiology

### Primary causal factor

**Monogenic.** Heterozygous *de novo* missense variants in the AAA-ATPase domain of *VPS4A* are the dominant cause (autosomal dominant, dominant-negative mechanism). A minority of cases are **biallelic (homozygous) missense**, arising in consanguineous families and acting through a distinct, milder loss-of-function-like route.

Rodger et al. (PMID:33186545) frame the causal claim as **[abstract]**:

> "Here we describe six unrelated individuals with *de novo* missense variants affecting the ATPase domain of VPS4A, a critical enzyme regulating ESCRT function. Probands had structural brain abnormalities, severe neurodevelopmental delay, cataracts, growth impairment, and anemia."

### Genetic risk factors

- **Causal variants:** see §4. All published pathogenic alleles are missense; no truncating, splice, or structural pathogenic alleles have been reported.
- **Position-specific risk:** the ATP-binding pocket arginine finger **Arg284** is a mutational hotspot (5 of 11 reported probands), and **pore-loop-1 residues Gly203/Glu206** form a second hotspot cluster.
- **Consanguinity** is the relevant risk factor for the recessive form (Seu proband 3, homozygous p.Ala28Val, both parents unaffected heterozygous carriers; Gupta 2026 Nepalese proband, homozygous p.Arg288Gln).
- **Advanced paternal age** — plausible but **not demonstrated** for this gene; no data. Treat as unknown.
- **Modifier genes:** none identified. *VPS4B* is a mechanistically obvious candidate modifier (see §4, §6): Seu et al. observed **[body/derived]** "significantly increased VPS4B expression in proband 3, indicating that VPS4B may partially, but not adequately, compensate for the VPS4A loss of function in the homozygous p.Ala28Val variant." No germline *VPS4B* modifier alleles have been tested.
- **Susceptibility loci / GWAS:** none. No GWAS Catalog signal is relevant to this Mendelian phenotype.

### Environmental risk factors

**None identified.** As a *de novo* germline missense disorder, no toxin, infectious, occupational, nutritional, or lifestyle exposure has been implicated in causation. The Unique guide states explicitly to families: *"This happens naturally and is not due to the parents' diet, environment or lifestyle."* Sex is not a risk factor (see §9). This should be recorded as **NO_EVIDENCE** rather than left blank.

### Protective factors

- **Genetic:** no protective alleles known. The only relevant observation is *paralog buffering* — an intact *VPS4B* is insufficient to prevent disease when *VPS4A* is mutated (see PMID:38687820), which argues against paralog dosage as a protective modifier in the dominant form but leaves it plausible in the recessive form.
- **Environmental:** none. Secondary/tertiary protective interventions (iron chelation, cataract extraction, seizure control) modify morbidity, not disease occurrence — record under §12/§13, not here.

### Gene–environment interactions

**No documented GxE.** One clinically actionable pseudo-interaction deserves note: **iron overload in this disease is disproportionate to transfusion burden** because ineffective erythropoiesis itself drives hyperabsorption — Unique states that *"Defective red blood cell development (dyserythropoiesis) and ineffective red blood cell production (ineffective erythropoiesis) may cause iron overload disproportionate to the number of transfusions."* This is a genotype-driven amplification of a treatment exposure (transfusional iron) rather than a true environmental interaction, but it belongs in the causal graph.

---

## 3. Phenotypes

### 3.1 HPO annotation set (source: HPO annotation file for OMIM:619273, retrieved via `ontology.jax.org` API)

Frequencies are literal **patient-count fractions** from the source publications, not population estimates. Inheritance annotation: `HP:0000006` Autosomal dominant inheritance.

#### Neurodevelopmental / neurological (core)

| HP ID | Term | Frequency | Notes |
|---|---|---|---|
| HP:0011344 | Severe global developmental delay | 6/6 (100%) | Congenital onset; core |
| HP:0010864 | Severe intellectual disability | 6/6 (100%) | Core |
| HP:0000252 | Microcephaly | 6/6 (100%) | "Z scores < −5" universal **[body/derived]** |
| HP:0011451 | Primary microcephaly | 3/6 (50%) | Congenital subset |
| HP:0001332 | Dystonia | 5/6 (83%) | Axial hypotonia + appendicular hypertonia pattern |
| HP:0001252 | Hypotonia | 5/6 (83%) | Neonatal onset; **central** in origin (zebrafish data) |
| HP:0001257 | Spasticity | 4/5 (80%) | Appendicular |
| HP:0001270 | Motor delay | 5/5 (100%) | None achieve independent walking |
| HP:0000750 | Delayed speech and language development | 5/5 (100%) | |
| HP:0001344 | Absent speech | 2/5 (40%) | Many remain non-verbal |
| HP:0001250 | Seizure | 3/6 (50%) | Multiple semiologies |
| HP:0001251 | Ataxia | 2/4 (50%) | |
| HP:0002072 | Chorea | 1/5 (20%) | |
| HP:0002360 | Sleep disturbance | 4/4 (100%) | High QoL impact; often medicated |

#### Brain structural (neuroimaging)

| HP ID | Term | Frequency |
|---|---|---|
| HP:0001321 | Cerebellar hypoplasia | 2/6 (also 5/6 by full-text count, see note) |
| HP:0001320 | Cerebellar vermis hypoplasia | 1/6 |
| HP:0006879 | Pontocerebellar atrophy | 1/6 |
| HP:0033725 | Thin corpus callosum | 2/6 |
| HP:0002059 | Cerebral atrophy | 1/6 |
| HP:0002126 | Polymicrogyria | 1/6 |

*Note the discrepancy:* the HPO annotation file records cerebellar hypoplasia as 2/6, but the Rodger full text states cerebellar hypoplasia in **five of six** probands. Seu et al. independently describe **[body/derived]** *"moderate to marked deficiency of hemispheric white matter with global cerebral volume loss, thin corpus callosum, and atrophy of the cerebellum and the pons, suggestive of a neurodegenerative syndrome."* For a dismech entry, curate cerebellar hypoplasia at the higher (full-text) frequency with the Rodger PMID, and flag the HPOA discrepancy in a `discussions` block.

#### Ophthalmologic

| HP ID | Term | Frequency |
|---|---|---|
| HP:0000505 | Visual impairment | 6/6 (100%) |
| HP:0000519 | Developmental cataract | 4/5 (80%) |
| HP:0000556 | Retinal dystrophy | 3/5 (60%) |
| HP:0025405 | Visual fixation instability | 3/6 (50%) |
| HP:0030854 | Scleral staphyloma | 1/3 |

One proband had **Leber congenital amaurosis** and/or cortical blindness (Seu proband 1) — consider `HP:0000548` (Leber congenital amaurosis is `HP:0000548`? verify; `MONDO:0018998` is the disease-level term) or curate as retinal dystrophy + cortical visual impairment.

#### Hematologic

Underrepresented in HPOA (the annotation file returned **no anemia term**, a genuine gap, because the anemia was characterized primarily in the *companion* paper, Seu et al., which is annotated to the same OMIM entry only partially). Curate from primary literature:

| Suggested HP ID | Term | Evidence |
|---|---|---|
| HP:0001878 | Hemolytic anemia | Lunati 2021 (PMID:33460484) |
| HP:0031688 | Erythroid dysplasia | Seu 2020 — binucleate erythroblasts, internuclear cytoplasmic bridges |
| HP:0005532 | Macrocytic dyserythropoietic anemia | Partial fit (MCV 80–100 fL = normocytic in the Seu probands, so this term over-specifies) |
| HP:0010972 | Anemia of inadequate production | Fits ineffective erythropoiesis |
| HP:0001744 | Splenomegaly | Persistent in 3/3 Seu probands |
| HP:0011031 | Abnormal iron homeostasis / iron overload | Ferritin 470–4093 ng/mL; LIC 6.5–12.1 mg/g dry weight |
| HP:0001081 | Cholelithiasis | 1/5 (HPOA) — consistent with chronic hemolysis |

Rodger et al. report anemia in 3/6, dyserythropoietic in 2 **[body/derived]**: *"Three subjects had anemia, which was characterized as dyserythropoietic in two."* Combining cohorts (Rodger 3/6 + Seu 3/3 + Lunati 1/1), anemia is present in roughly **7/10** published patients — i.e. **FREQUENT** in HPO frequency terms. Note the Lunati case demonstrates the anemia can be **hemolytic without overt dyserythropoiesis**, so the hematologic phenotype should be curated as a spectrum, not a single entity.

#### Growth and gastrointestinal

| HP ID | Term | Frequency / source |
|---|---|---|
| HP:0011968 | Feeding difficulties | 4/6 (assisted feeding in 3/6) |
| HP:0002240 | Hepatomegaly | 4/5 |
| HP:0001433 | Hepatosplenomegaly | 4/6 "hepatosplenomegaly and/or steatosis" (Rodger) |
| HP:0001414 | Microvesicular hepatic steatosis | 1/5 |
| HP:0009125 | Lipodystrophy | 1/5 |
| HP:0001510 | Growth delay | Most probands; "severe growth retardation across most cases" |
| HP:0004322 / HP:0004325 | Short stature / decreased body weight | Derived from growth retardation |
| HP:0002019 | Constipation | Unique guide (families) |
| HP:0002020 | Gastroesophageal reflux | Unique guide (families) |

#### Other systems

| HP ID | Term | Frequency |
|---|---|---|
| HP:0000407 | Sensorineural hearing impairment | 2/5 (40%) |
| HP:0002719 | Recurrent infections | 1/5 |
| HP:0000135 | Hypogonadism | 1/4 |
| HP:0100613 | Death in early adulthood | 2/6 |

Unique additionally reports, from family experience (not peer-reviewed case series, so lower evidence tier): dental abnormalities (late eruption, overcrowding, weak enamel, bruxism, eruption cysts), **talipes/club foot**, scoliosis/kyphosis, peripheral acrocyanosis and cold extremities, neonatal jaundice, and small hands and feet.

One Seu proband had **chronic kidney disease stage II–III** (`HP:0012622`) and one had **macrocephaly** rather than microcephaly (the homozygous p.Ala28Val proband) — an important genotype–phenotype exception.

### 3.2 Phenotype characteristics

- **Age of onset:** congenital / neonatal for essentially all core features. Microcephaly is present at birth (primary microcephaly in half). Hypotonia is "profound neonatal-onset." Cataracts are congenital in the majority. Anemia is "apparent from early infancy."
- **Severity:** uniformly **severe to profound** for the neurodevelopmental domain in the heterozygous dominant-negative genotypes. The **homozygous p.Ala28Val (MIT-domain) genotype is milder** — Seu et al. note **[body/derived]** *"the phenotype is somewhat milder than the clinical picture secondary to de novo heterozygous variants in the large ATPase domain which appear to exert a more detrimental, dominant-negative effect."*
- **Progression:** predominantly **static/developmental** rather than degenerative in most descriptions, but imaging language in Seu et al. is explicitly *"suggestive of a neurodegenerative syndrome"* (progressive cerebral volume loss, pontocerebellar atrophy). This is an unresolved question — curate as a **KNOWLEDGE_GAP** discussion: *is CIMDAG a static malformation syndrome, a progressive neurodegeneration, or both?* Anemia is chronic and lifelong; feeding difficulties often improve after early childhood per Unique.
- **Frequency across individuals:** given above per phenotype.

### 3.3 Quality-of-life impact (per phenotype)

No EQ-5D, PedsQL, SF-36, or PROMIS data exist for this disorder — this is a genuine and complete gap. Qualitative, family-reported impacts from the Unique guide:

- **Motor/dystonia:** dominant driver of disability — independent sitting, standing, or walking "may not be achieved"; requires orthotics, callipers, wheelchair, hydrotherapy; caregiver-dependent for all mobility and transfers.
- **Speech/communication:** profound; many remain non-verbal, requiring AAC (pictograms, gestures, high-tech aided communication). Families describe first successful interaction via auditory/tactile channels: *"Hearing and making funny noises paired with touching was our first possibility to interact and bring a smile and later laughter to our son's face."*
- **Sleep disturbance (4/4):** high family burden; frequently medicated.
- **Feeding:** NGT/PEG in a substantial subset; aspiration risk.
- **Anemia:** transfusion every 2 weeks to 6 months → recurrent hospital contact, venous access burden, and lifelong chelation.
- **Seizures:** *"Seizures can cause a lot of worry for families and can be frightening to observe."*
- **Vision:** cataract + retinal dystrophy compounds developmental deprivation; cataract is surgically correctable ("if a cataract is diagnosed it can be easily removed with a small surgery").
- **Temperament:** counterbalancing positive — *"most have a happy disposition."*

---

## 4. Genetic / Molecular Information

### Causal gene

***VPS4A*** — vacuolar protein sorting 4 homolog A. HGNC:13488 · NCBI Gene 27183 · Ensembl ENSG00000132612 · UniProt **Q9UN37** · OMIM *609982 · RefSeq **NM_013245.3** / NP_037377 · chromosome **16q22.1**.

Protein: **437 aa**, 48,898 Da. Type I AAA+ ATPase (EC 3.6.4.6). Domain architecture (UniProt Q9UN37):
- **MIT domain, aa 2–80** — "Microtubule Interacting and Trafficking" domain; binds ESCRT-III MIM motifs (CHMP1A/B, CHMP2A/B, IST1). Key ESCRT-III contact residues include **Val-13** and **Leu-64**.
- **AAA+ ATPase cassette (central)** — Walker A P-loop **aa 167–174** (ATP binding), catalytic **Lys-173**, Walker B glutamate **Glu-228** (the residue mutated in the canonical experimental dominant negative E228Q), pore loop 1 containing **Trp201/Leu202/Gly203** and **Glu206**, and the **arginine finger Arg284**.
- **β-domain / Vps4_C** — substrate and VTA1 co-factor engagement.

### Pathogenic variants (all reported cases)

| Variant (NM_013245.3) | Protein | Domain / residue role | Zygosity | Origin | n | Reference |
|---|---|---|---|---|---|---|
| c.850A>T | p.Arg284Trp | Arginine finger, ATP pocket | Heterozygous | *De novo* | 4 | PMID:33186545 |
| c.850A>T | p.Arg284Trp | Arginine finger | Heterozygous | *De novo* | 1 (proband 1) | PMID:33186543 |
| c.850A>G | p.Arg284Gly | Arginine finger | Heterozygous | *De novo* | 1 | PMID:33186545 |
| c.616G>A | p.Glu206Lys | Pore loop 1 region | Heterozygous | *De novo* | 1 | PMID:33186545 |
| c.608G>A | p.Gly203Glu | Pore loop 1, central pore | Heterozygous | *De novo* | 1 (proband 2) | PMID:33186543 |
| c.83C>T | p.Ala28Val | **MIT domain** | **Homozygous** | Inherited (unaffected het parents) | 1 (proband 3) | PMID:33186543 |
| c.863G>A | p.Arg288Gln | AAA domain, conserved Arg | **Homozygous** | Consanguineous, Nepal | 1 | PMID:42498620 |
| (not specified in retrieved abstract) | — | — | Heterozygous | *De novo* | 1 | PMID:33460484 |

**Variants of uncertain significance** reported and functionally *excluded* by Rodger et al.: **c.502C>T (p.Pro168Ser)** and **c.1009A>G (p.Ile337Val)** — associated with non-specific intellectual disability, deemed unlikely pathogenic. UniProt additionally flags a variant at position 193 as a VUS with a CIMDAG-like presentation.

**Variant class:** exclusively **missense**. No pathogenic PTVs, splice, CNV, or structural variants have been reported for this phenotype.

**Population allele frequency:** the pathogenic alleles are **absent from gnomAD, ExAC, and TOPMed** and fall "in regions highly constrained for variation in control populations" **[body/derived, Rodger et al.]**. I was unable to retrieve numeric gnomAD constraint metrics (pLI/LOEUF) — the browser is JS-rendered and the GraphQL endpoint requires POST; record this as a data gap rather than inventing a value. The qualitatively decisive constraint statement is the *opposite* of what one might expect and is central to the mechanism (below).

**Somatic vs germline:** all disease-causing variants are **germline**. *VPS4A* does appear in somatic cancer contexts — it is a well-known **synthetic-lethal partner of VPS4B** in 18q-deleted cancers, and recent work implicates it in oxaliplatin resistance in colorectal cancer (PMID:40558556), radioresistance via MYO1C in esophageal squamous carcinoma (PMID:41654990), EPHB2-driven autophagy in oral squamous carcinoma (PMID:40017157), and STING-driven anti-tumor immunity when VPS4 is pharmacologically targeted in rhabdomyosarcoma (PMID:42032367). **None of this is relevant to CIMDAG pathogenesis** and should not be conflated with it in a disease entry — but the VPS4A/VPS4B synthetic-lethal literature is the reason a VPS4 inhibitor chemical toolkit exists at all.

### Functional consequence: dominant negative, explicitly not haploinsufficiency

This is the single most important molecular fact for the entry. Rodger et al. state **[body/derived]**:

> "Multiple heterozygous *VPS4A* loss-of-function mutations are present in general population databases, indicating that a haploinsufficiency mechanism is unlikely."

and

> "Our data and published evidence point to the p.Glu206Lys, p.Arg284Trp, and p.Arg284Gly mutants having a dominant-negative effect."

The structural logic is hexamer poisoning **[body/derived]**:

> "As VPS4A protein stability is unaltered in proband cells, assuming equal expression of wild-type and mutant VPS4A we expect that a large majority of VPS4A hexamers will have impaired function as they will contain at least one mutant subunit."

with the proximate defect being *"incorporation of the ATPase-defective protein into VPS4 hexamers and subsequent failure of disassembly of the ESCRT complexes."*

Residue-level mechanism (Seu et al.) **[body/derived]**:
- **Arg284:** *"one of two arginine fingers functioning in the ATP binding pocket… interaction with the γ-phosphate of ATP, promoting hydrolysis. Therefore, alteration of Arg284 would be expected to compromise ATP hydrolysis and the function of VPS4A as an ATPase."*
- **Gly203:** *"part of the pore loop 1 motif which forms the central pore of the active hexamer… is highly conserved, as it is the only amino acid that permits the packing and conformation required for the adjacent pore loop 1 residues Trp201 and Leu202 to create binding pockets for the sidechains of the ESCRT-III subunits passing through the pore."*
- **Ala28 (MIT):** *"putatively disrupts VPS4A interaction with ESCRT-III proteins due to altered structure of the MIT domain, rather than directly affecting its ATPase activity"* — a **mechanistically distinct, recessive, hypomorphic** route, consistent with its milder phenotype and requirement for biallelic dosage.
- **Arg288 (homozygous, 2026):** *"disruption of a conserved Arginine-288 residue within the ATPases associated with diverse cellular activities domain"* causing loss of protein stability (PMID:42498620).

This yields a clean **two-mechanism model** worth curating as separate pathophysiology branches:
1. **Dominant-negative branch** (heterozygous ATPase-domain missense: R284W/G, E206K, G203E) → severe classic CIMDAG.
2. **Recessive hypomorphic branch** (biallelic A28V MIT-domain, R288Q destabilizing) → milder/atypical presentations, partial VPS4B compensation.

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifiers:** *VPS4B* is the only credible candidate (compensatory upregulation observed; paralog-specific non-redundancy demonstrated in PMID:38687820). Not formally tested as a modifier.
- **Epigenetics:** **no data.** No methylation episignature has been described for *VPS4A*; it is not in the published EpiSign panels. This is a concrete, tractable gap worth flagging — episignatures exist for many chromatin and trafficking NDDs and would be diagnostically useful here.
- **Chromosomal abnormalities:** none causal. 16q22.1 deletions encompassing *VPS4A* would produce haploinsufficiency, which the population data indicate is **tolerated** — so CMA-detectable deletions should not be expected to cause CIMDAG. This is a useful negative for differential-diagnosis reasoning.

---

## 5. Environmental Information

- **Environmental factors:** none implicated. CTD lists chemical–*VPS4A* expression interactions (as for most genes), but none has any established role in this disease.
- **Lifestyle factors:** not applicable to causation. Relevant only downstream (nutrition/feeding, dental hygiene, mobility/physiotherapy).
- **Infectious agents:** not causal. There is an interesting *inverse* biological connection worth noting but **not** curating as etiology: VPS4A is the ATPase hijacked by many enveloped viruses (HIV-1, Ebola) for ESCRT-dependent budding (`GO:0039702` viral budding via host ESCRT complex). Recurrent infections were reported in 1/5 patients, but there is no evidence of a systematic immunodeficiency or of altered viral susceptibility in patients.

---

## 6. Mechanism / Pathophysiology

### 6.1 The core causal chain

```
[MOLECULAR] De novo heterozygous missense in VPS4A ATPase domain (R284W/G, E206K, G203E)
     │  mutant subunit is stably expressed (protein abundance unchanged)
     ▼
[MOLECULAR] Poisoning of the hexameric VPS4A AAA-ATPase
     │  ≥1 mutant subunit per hexamer → loss of ATP hydrolysis / substrate translocation
     ▼
[MOLECULAR] Failure of ESCRT-III filament disassembly and recycling  (GO:1904903)
     │  IST1 (atypical ESCRT-III) accumulates on limiting membranes; core CHMP2B distribution preserved
     ▼
     ├──► [CELLULAR] Enlarged endo-lysosomal compartments (CD63+/LAMP1+/cathepsin D+)
     ├──► [CELLULAR] Cytokinetic abscission failure at the midbody (GO:0061952)
     ├──► [CELLULAR] Centrosome amplification → multipolar spindles → chromosome missegregation
     ├──► [CELLULAR] Nuclear envelope reformation defect (GO:0007084) → irregular nuclei, γH2AX↑
     ├──► [CELLULAR] Primary ciliogenesis failure ("dot cilium", basal body only)
     ├──► [CELLULAR] Impaired autophagosome closure / LC3B engagement; lipid droplet mishandling
     └──► [CELLULAR] Failed exosome release during reticulocyte maturation (CD71 retention)
     ▼
[TISSUE]  Neural progenitor depletion & aberrant corticogenesis │ Ineffective erythropoiesis │ Lens/retina degeneration
     ▼
[ORGANISM] Microcephaly, cerebellar hypoplasia, dystonia, ID │ Transfusion-dependent anemia, iron overload │ Cataract, retinal dystrophy │ Growth failure
```

### 6.2 Molecular pathways

- **ESCRT (endosomal sorting complexes required for transport) pathway** — the sole primary pathway. VPS4A is the terminal, energy-consuming step that disassembles ESCRT-III polymers so they can be reused. Reactome: *Membrane Trafficking → ESCRT-dependent MVB biogenesis*. KEGG: hsa04144 (Endocytosis).
- **Downstream/secondary:** autophagy–lysosome axis (PMID:42498620 — impaired LC3B interaction); cGAS-STING innate immune signaling is engaged when VPS4 is inhibited pharmacologically (PMID:42032367) — mechanistically interesting, unproven in patients; cell-cycle/mitotic checkpoint (Aurora B/ANCHR abscission checkpoint via ZFYVE19/VTA1).
- **Not implicated:** Wnt, MAPK, mTOR, PI3K-AKT as primary drivers. Do not assert these.

### 6.3 Suggested GO biological process terms

| GO ID | Label | Direction |
|---|---|---|
| GO:1904903 | ESCRT III complex disassembly | DECREASED |
| GO:1904896 | ESCRT complex disassembly | DECREASED |
| GO:0071985 | multivesicular body sorting pathway | ABNORMAL |
| GO:0032509 | endosome transport via multivesicular body sorting pathway | DECREASED |
| GO:0061952 | midbody abscission | DECREASED |
| GO:0007084 | mitotic nuclear membrane reassembly | DECREASED |
| GO:0060271 | cilium assembly | DECREASED |
| GO:0007059 | chromosome segregation | ABNORMAL |
| GO:0000226 | microtubule cytoskeleton organization (spindle) | ABNORMAL |
| GO:0006914 | autophagy | DECREASED |
| GO:0070887 / GO:0006979 | response to oxidative stress | INCREASED |
| GO:0070925 | organelle assembly (lipid droplet) | ABNORMAL |
| GO:0006281 | DNA repair / DNA damage response (γH2AX↑) | INCREASED |

Molecular function: `GO:0016887` ATP hydrolysis activity (DECREASED); `GO:0140657` ATP-dependent activity. Cellular component: `GO:0005770` late endosome, `GO:0005769` early endosome, `GO:0005764` lysosome, `GO:0030496` midbody, `GO:0090543` Flemming body, `GO:0005813` centrosome, `GO:0000922` spindle pole, `GO:0005635` nuclear envelope, `GO:0005811` lipid droplet, `GO:0000815` ESCRT III complex.

### 6.4 Cellular processes — the experimental evidence

**Endosomal morphology (patient fibroblasts and heterologous overexpression)** — Rodger et al. **[abstract]**:

> "In cultured cells, overexpression of VPS4A mutants caused enlarged endosomal vacuoles resembling those induced by expression of known dominant-negative ATPase-defective forms of VPS4A. Proband-derived fibroblasts had enlarged endosomal structures with abnormal accumulation of the ESCRT protein IST1 on the limiting membrane."

Critically, the defect is **selective, not a global endosomal collapse** **[body/derived]**: *"Heterozygous expression of mutant VPS4A in proband cells does not affect the cellular distribution of a core ESCRT-III complex member, prevent formation of ILVs, or adversely affect the degradation of EGFR"* — indeed EGFR degradation was *increased* at 180 min. This partial-penetrance-at-the-cell-biology-level is what makes the disease survivable and is worth modeling as a distinct node.

**Mitosis and genome stability** — proband fibroblasts show **[body/derived]** *"an anomalous centrosome number and morphology in interphase"*; *"Multipolar spindles were observed during mitosis, resulting in a high frequency of aberrant chromosome alignment during metaphase"*; *"Aberrant chromosome segregation was documented by the presence of both lagging and bridging chromosomes during anaphase and telophase"*; increased micronuclei; G2/M accumulation on BrdU flow cytometry; *"increased number of γH2AX foci… indicating increased spontaneous DNA damage."*

**Primary cilium** — *"Normal cilia were absent in fibroblasts expressing the VPS4A-p.Arg284Gly mutant, which instead showed a visible basal body (dot cilium)"*; R284W cells show a dot cilium or occasionally an elongated/normal cilium. Seu et al. additionally report altered *"length, number, and Arl13b composition of primary cilia."* **This makes CIMDAG partially a ciliopathy-adjacent disorder** — relevant to the retinal dystrophy, cerebellar hypoplasia, and renal involvement, and a plausible `conforms_to` link to `ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction` in the dismech module set (flag as partial/atypical, since the primary lesion is ESCRT not IFT).

**Neurons (iPSC-derived i³Neurons + CRISPRi knockdown)** — Rodger et al. **[abstract]**: *"VPS4A function was also required for normal endosomal morphology and IST1 localization in iPSC-derived human neurons."* Full text: *"a significant increase in the percentage of neurons that had enlarged structures marked by CD63, LAMP1, or the lysosomal enzyme cathepsin D"*, and — a striking result — *overexpression of mutant VPS4A was "incompatible with neuronal survival."* CRISPRi VPS4A knockdown *"largely recapitulates phenotypes that are observed in proband cells expressing dominant-negative VPS4A at physiological heterozygous levels."*

**Erythroid lineage** — Seu et al. **[abstract]**:

> "Bone marrow studies showed binucleated erythroblasts and erythroblasts with cytoplasmic bridges indicating abnormal cytokinesis and abscission. Circulating red blood cells were found to retain transferrin receptor (CD71) in their membrane, demonstrating that VPS4A is critical for normal reticulocyte maturation. Using proband-derived induced pluripotent stem cells (iPSCs), we have successfully modeled the hematologic aspects of this syndrome in vitro, recapitulating their dyserythropoietic phenotype."

Two mechanistically separable erythroid defects therefore coexist: (i) **abscission failure → binucleate erythroblasts → ineffective erythropoiesis (dyserythropoiesis)**, and (ii) **failure of exosome-mediated CD71/transferrin-receptor shedding → arrested reticulocyte maturation → shortened RBC survival (hemolysis)**. The Lunati case, in which hemolysis dominated without obvious dyserythropoiesis, is the clinical proof that these two arms can dissociate.

**Paralog non-redundancy** — Dvilansky et al., PLoS Biol 2024 (PMID:38687820) **[abstract]**:

> "Mutations in the human AAA-ATPase VPS4 isoform, VPS4A, cause severe neurodevelopmental defects and congenital dyserythropoietic anemia (CDA). VPS4 is a crucial component of the endosomal sorting complex required for transport (ESCRT) system… while most organisms encode for a single VPS4 gene, human cells have 2 VPS4 paralogs, namely VPS4A and VPS4B, but the functional differences between these paralogs is mostly unknown."

Findings: *"VPS4A depletion resulted in a more severe abscission delay than VPS4B and was found to be involved in earlier stages of abscission"*; *"Depletion of VTA1, a co-factor of VPS4, disrupted VPS4A-ANCHR interactions and accelerated abscission"*; STORM imaging showed *"the decrease in IST1 density in late intercellular bridges is driven by the VPS4B isoform."* Disease relevance stated directly: *"Patients who carry normal VPS4B and mutated VPS4A genes develop pathologies due to the disruption of VPS4A-mediated cellular regulation, which is essential for neurodevelopment and cannot be compensated by VPS4B."* **This is the mechanistic answer to "why doesn't the paralog rescue?" and belongs in the entry.**

### 6.5 Metabolic and lipid changes (newest mechanism, 2026)

Gupta et al., *J Clin Lipidol* 2026 (PMID:42498620) add a **lipotoxicity arm** from the homozygous p.Arg288Gln case: loss of protein stability, **impaired LC3B interaction**, **reduced lipid-droplet localization**, and cellular *"increased lipid accumulation, elevated free fatty acids, and higher reactive oxygen species levels."* This provides a candidate unifying explanation for the otherwise puzzling **hepatic steatosis (1/5), hepatomegaly (4/5), and lipodystrophy (1/5)** in the HPO annotation set. Treat as **EMERGING** (`mechanistic_hypotheses` status), single-patient, in-vitro-supported.

### 6.6 Immune involvement

Not a primary feature. Recurrent infections in 1/5. Pharmacological VPS4 inhibition activates cGAS-STING-TBK1-IRF3 (PMID:42032367, rhabdomyosarcoma models) — mechanistically this predicts that ESCRT dysfunction could produce cytosolic-DNA-driven interferon signaling (consistent with the micronuclei observed in patient fibroblasts). **This is an untested hypothesis in patients** and is the single most interesting unexplored mechanism: micronuclei + cGAS-STING is the canonical route to a chronic interferonopathy, and no one has looked for an interferon signature in CIMDAG blood. Worth curating as a `KNOWLEDGE_GAP` with a proposed experiment.

### 6.7 Tissue damage mechanisms

- **CNS:** proliferative failure of neural progenitors (abscission defect → the classic microcephaly mechanism shared with other cytokinesis/centrosome microcephaly genes) plus post-mitotic neuronal endolysosomal dysfunction and reduced neuronal survival. Zebrafish data (below) localize the hypotonia to a **central sensorimotor transformation** defect, not to motor neuron or muscle failure.
- **Erythron:** ineffective erythropoiesis + peripheral hemolysis + secondary iron loading → hepatosplenomegaly, cholelithiasis, liver iron accumulation.
- **Lens/retina:** presumed proteostasis/trafficking failure in lens fiber cells and photoreceptor outer-segment turnover (an ESCRT/exosome-dependent process); mechanism not directly demonstrated.
- **Oxidative stress:** elevated ROS documented in the R288Q model.

### 6.8 Molecular profiling status

| Modality | Status |
|---|---|
| Transcriptomics | No patient RNA-seq published. Zebrafish shows *atf3*/*jun* stress-response upregulation in affected brain regions. |
| Proteomics | None patient-derived. (*VPS4A* appears as a PBMC biomarker candidate in sporadic Ménière disease, PMID:37603046 — unrelated.) |
| Metabolomics | None. |
| Lipidomics | Cell-model lipid quantification only (PMID:42498620). No patient lipidomics. |
| Single-cell / spatial | None. iPSC-derived i³Neurons and iPSC-erythroid cultures are the closest. |
| Functional genomics screens | *VPS4A* is a prominent **DepMap** synthetic-lethal hit paired with *VPS4B*; not exploited for CIMDAG. |
| Epigenomics | None (see §4). |

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
- **Brain / CNS** (`UBERON:0000955`) — cerebrum (`UBERON:0000956` cerebral cortex), **cerebellum** (`UBERON:0002037`), cerebellar vermis (`UBERON:0004720`), **corpus callosum** (`UBERON:0002336`), **pons** (`UBERON:0000988`), basal ganglia (`UBERON:0002420`), cerebral white matter (`UBERON:0002316`)
- **Bone marrow / erythron** (`UBERON:0002371`)
- **Eye** (`UBERON:0000970`) — **lens** (`UBERON:0000965`), **retina** (`UBERON:0000966`), sclera (`UBERON:0001773`)

**Secondary:**
- **Liver** (`UBERON:0002107`) — hepatomegaly, steatosis, iron loading
- **Spleen** (`UBERON:0002106`) — splenomegaly from extravascular hemolysis
- **Kidney** (`UBERON:0002113`) — CKD in 1 proband
- **Gallbladder / biliary** (`UBERON:0002110`) — cholelithiasis
- **Inner ear / cochlea** (`UBERON:0001844`) — sensorineural hearing loss
- **Skeletal muscle** (`UBERON:0001134`) — secondary to central tone abnormality, not primary myopathy
- **Adipose tissue** (`UBERON:0001013`) — lipodystrophy (1/5)
- Skeleton (spine `UBERON:0001130`, foot `UBERON:0002387`) — scoliosis, talipes
- Teeth (`UBERON:0001091`) — enamel/eruption anomalies

**Body systems:** nervous (central, dominant), hematopoietic, visual, hepatobiliary, musculoskeletal, growth/endocrine (hypogonadism 1/4), auditory, renal.

### Tissue and cell level

Suggested Cell Ontology terms:

| CL ID | Cell type | Role |
|---|---|---|
| CL:0000047 | neuronal stem cell / neural progenitor | Abscission failure → depleted progenitor pool → microcephaly |
| CL:0000540 | neuron | Enlarged endolysosomes; mutant overexpression incompatible with survival |
| CL:0000121 | Purkinje cell | Inferred from cerebellar hypoplasia/atrophy (not directly demonstrated) |
| CL:0000765 | erythroblast | Binucleation, cytoplasmic bridges — the primary hematologic cell |
| CL:0000558 | reticulocyte | Failed exosome-mediated CD71 shedding |
| CL:0000232 | erythrocyte | Aberrant CD71-retaining population; shortened survival |
| CL:0002322 | (iPSC — model system) | Patient iPSCs used for both neuronal and erythroid modeling |
| CL:0000148 / lens fiber `CL:0011004` | lens fiber cell | Cataract |
| CL:0000210 | photoreceptor cell | Retinal dystrophy |
| CL:0000057 | fibroblast | Principal patient-derived assay cell |
| CL:0000182 | hepatocyte | Steatosis, lipid droplet handling |
| CL:0000855 | inner ear hair cell | SNHL (note: zebrafish inner ear function was *unaffected*, so the human SNHL locus is unresolved) |

Tissue types: nervous tissue (dominant), hematopoietic tissue, transparent avascular lens epithelium/fiber, hepatic parenchyma.

### Subcellular level (GO Cellular Component)

`GO:0005770` late endosome · `GO:0005769` early endosome · `GO:0005768` endosome · `GO:0005764` lysosome · `GO:0032585` multivesicular body membrane · `GO:0030496` midbody · `GO:0090543` Flemming body · `GO:0005813` centrosome · `GO:0000922` spindle pole · `GO:0005635` nuclear envelope · `GO:0005811` lipid droplet · `GO:0005929` cilium / `GO:0036064` ciliary basal body · `GO:0000815` ESCRT III complex · `GO:0070062` extracellular exosome.

**The subcellular level is where this disease actually "lives"** — a dismech entry should anchor most `MOLECULAR`/`CELLULAR` pathophysiology nodes here rather than at organ level.

### Localization and lateralization

Brain involvement is **bilateral and symmetric** (cerebellar hypoplasia, symmetric white matter loss, bilateral polymicrogyria in one case, bilateral cataracts). Microcephaly is global. No lateralized or asymmetric pattern reported. Cataracts bilateral.

---

## 8. Temporal Development

### Onset

- **Congenital / prenatal.** Primary microcephaly in 3/6 indicates prenatal onset of the brain growth failure; congenital cataracts confirm in-utero lens involvement.
- **Neonatal:** profound hypotonia, feeding difficulties.
- **Early infancy:** anemia becomes apparent; developmental delay evident by failure to establish head control.
- **Onset pattern:** insidious/congenital rather than acute. There is no asymptomatic interval and no "normal then regressed" trajectory reported.

### Progression

- **Stages:** no formal staging system exists. Practically: (1) neonatal hypotonia/feeding/anemia; (2) infancy-early childhood — failure of motor milestones, cataract, seizure onset, transfusion dependence established; (3) later childhood — dystonia/spasticity dominate, iron overload accrues, scoliosis/contractures; (4) adolescence/adult — a minority survive; two deaths in childhood or early adult life.
- **Rate:** the neurodevelopmental phenotype is best described as **severe and largely static with superimposed progressive elements**. Dystonia is described as progressive by families; imaging in the Seu cohort was read as *"suggestive of a neurodegenerative syndrome."* The literature does not resolve this — curate as an explicit open question.
- **Course pattern:** chronic, lifelong; seizures may be episodic/isolated or recurrent; anemia is chronic with transfusion-cycle fluctuation.
- **Duration:** lifelong; not self-limited. Feeding difficulties are the one feature Unique describes as often improving: *"Feeding issues in the newborn period are common in children with CIMDAG syndrome but usually resolve after babyhood or early childhood."*

### Patterns

- **Remission:** none spontaneous. Treatment-induced improvement is limited to specific features (cataract extraction restores optical clarity; transfusion corrects Hb; chelation reverses iron loading).
- **Critical periods:** (i) **prenatal neurogenesis** — the microcephaly window is closed before birth, so no postnatal therapy can address it (Unique: *"a complete cure is unlikely, even in the future, since the brain has already formed by the time a diagnosis is made"*); (ii) **first year of life** — the actionable window for cataract detection/extraction and for establishing hematologic monitoring, both explicitly recommended; (iii) **from ~1 year** — the window to begin annual iron-status monitoring before organ iron accrues.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** unknown; **ultra-rare**. Orphanet has not assigned a prevalence class. Unique (2024): *"CIMDAG syndrome is extremely rare. Currently (2024) only 10 individuals with a VPS4A gene variant have been reported in the medical literature but more are known to have been diagnosed."* With the 2026 Nepalese case, the published total is **~11**. For a structured `prevalence` record, use `prevalence_class: ULTRA_RARE`, `measure_type: CASES_IN_LITERATURE`, count ≈ 11, `population: Worldwide`, with the Unique guide and the primary case series as evidence. **Do not compute a rate_per_100000** — there is no denominator.
- **Incidence:** not estimable.

### Inheritance

- **Predominant: autosomal dominant, *de novo*** (`HP:0000006`; HPOA inheritance annotation for OMIM:619273 is autosomal dominant). Unique: *"In all individuals identified so far (2024), except one, the genetic change was a random (known as 'de novo') change."*
- **Also: autosomal recessive** (`HP:0000007`) in at least two probands — Seu proband 3 (homozygous p.Ala28Val, unaffected heterozygous parents) and the 2026 Nepalese proband (homozygous p.Arg288Gln). **Both inheritance modes should be curated**, with the AR form tied to MIT-domain/destabilizing alleles and a milder phenotype. This dual-mode architecture (dominant-negative missense vs. recessive hypomorph in the same gene) is a genuinely notable feature of the entry.
- **Penetrance:** complete for the reported pathogenic alleles in the genotypes described. Heterozygous carriers of the recessive p.Ala28Val allele are **unaffected**, confirming that this allele is non-dominant. Heterozygous *VPS4A* LoF alleles in population databases are, by inference, also non-penetrant.
- **Expressivity:** variable within genotype. Four probands share p.Arg284Trp yet differ in seizures, hearing loss, anemia severity, and hepatic involvement — so intra-allelic variable expressivity is real and unexplained.
- **Anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not documented, but explicitly retained in counseling as the residual-risk mechanism — Unique: *"One reason why there is some residual chance of recurrence is due to the rare phenomenon called germline mosaicism."*
- **Founder effects:** none identified.
- **Consanguinity:** directly relevant to the recessive form (Nepalese consanguineous family; Seu proband 3's parents both carriers).
- **Carrier frequency:** not established for any pathogenic allele; all are absent from gnomAD.

### Population demographics

- **Affected populations:** no ethnic predilection identified. Reported patients span European, North American, and South Asian (Nepalese) ancestries. With n≈11, no inference is possible.
- **Geographic distribution:** worldwide; reporting is concentrated in the UK/Europe (Rodger, Lunati) and USA (Seu, via CDAR), which is ascertainment bias from where exome sequencing and CDA registries operate — not a true distribution. The one Asian case (Nepal, 2026) suggests underascertainment in low-resource settings.
- **Sex ratio:** no sex bias reported or expected (autosomal). Individual sexes are not consistently extractable from the abstracts; treat as **unknown/1:1**.
- **Age distribution:** all reported patients ascertained in infancy or childhood; two died in childhood or early adult life; the oldest survivors are young adults.

---

## 10. Diagnostics

### Genetic testing — the definitive route

**Recommended approach:** trio **exome (WES)** or **genome (WGS)** sequencing. Unique: *"CIMDAG syndrome is caused by a VPS4A gene sequence variant that can be identified by a type of genetic test called sequencing (e.g. whole exome sequencing (WES) or whole genome sequencing (WGS))… a genetic test is needed to confirm a suspected diagnosis."* All 11 reported cases were identified by exome/genome sequencing, several via GeneMatcher-style matchmaking.

| Modality | Utility for CIMDAG |
|---|---|
| **Trio WES** | **First-line, high yield.** Detects all known pathogenic alleles; trio design establishes *de novo* status, which is essential for interpretation. |
| **WGS** | Equivalent or better; preferred where available. |
| **Gene panels** | *VPS4A* is on **Genomics England PanelApp "Rare anaemia"** panel and on ID/microcephaly panels of some labs. A CDA panel is a reasonable entry point when anemia dominates the presentation. |
| **Single-gene *VPS4A* testing** | Reasonable only for targeted familial testing / cascade testing after a proband variant is known. |
| **Chromosomal microarray** | **Low yield and mechanistically uninformative** — deletions cause haploinsufficiency, which is tolerated. Will be done anyway as first-tier ID/microcephaly workup; expect negative. |
| **Karyotype / FISH** | Not indicated. |
| **mtDNA testing** | Not indicated, but frequently performed because the phenotype (microcephaly, lactate-free encephalopathy, cerebellar/pontine atrophy, hepatopathy) mimics a mitochondrial disorder — worth listing as a common diagnostic detour. |
| **Repeat expansion testing** | Not indicated. |

**Variant interpretation notes for ACMG/AMP application:** pathogenic alleles are absent from gnomAD (PM2), *de novo* with confirmed parentage (PS2), fall in a well-established functional domain and at a mutational hotspot (PM1), have supporting functional studies (PS3 — the endosomal-vacuole and IST1 assays are essentially a validated functional assay for this gene), and R284W recurs in multiple unrelated probands (PS4_moderate). **Critically, PVS1 should never be applied to *VPS4A*** — LoF is not the mechanism. ClinVar holds 52 records classified pathogenic/likely pathogenic under a broad query and ~149 *VPS4A* variants overall; most non-hotspot missense will be VUS.

### Clinical tests

**Hematology (essential; Unique explicitly recommends):** *"It is recommended to check on complete blood count (CBC) and reticulocyte count at the time of the diagnosis and also monitor the iron status regularly (e.g. once a year, starting by 1 year of age)."*

| Test | Expected finding | LOINC (indicative) |
|---|---|---|
| CBC / hemoglobin | Hb **6.1–7.3 g/dL** untransfused (Seu probands) | LOINC:718-7 |
| MCV | **80–100 fL** — normocytic, *not* macrocytic (distinguishes from CDA type I) | LOINC:787-2 |
| Absolute reticulocyte count | 40–500 ×10⁶/µL — **inadequately elevated for the degree of anemia** (ineffective erythropoiesis) | LOINC:26498-6 |
| Ferritin | **470–4093 ng/mL** | LOINC:2276-4 |
| Liver iron concentration (MRI R2*/T2*) | **6.5–12.1 mg/g dry weight** | — |
| Haptoglobin, LDH, bilirubin | Hemolysis pattern; neonatal/persistent jaundice | — |
| **Flow cytometry: CD71 on mature RBCs** | **Abnormal CD71-retaining mature RBC population — a disease-characteristic biomarker** | — |
| Bone marrow aspirate | **Binucleated erythroblasts (3–7%), internuclear cytoplasmic bridges**; erythroid hyperplasia | — |

The **CD71-retention flow assay is the closest thing to a functional biomarker for this disease** and is worth curating as a `biochemical`/diagnostic entity — it directly reads out the exosome/ESCRT defect and distinguishes VPS4A-CDA from other CDAs.

**Imaging:**
- **Brain MRI** (essential): reduced global cerebral volume, thin/hypoplastic corpus callosum, cerebellar and pontine hypoplasia/atrophy, delayed myelination, white matter deficiency, ± polymicrogyria, ± basal ganglia atrophy. Occasional ventriculomegaly ex vacuo.
- **Abdominal ultrasound:** hepatosplenomegaly, gallstones.
- **Hepatic MRI R2\*/FerriScan:** iron quantification.
- **Cardiac T2\* MRI:** if chronically transfused.

**Electrophysiology:** EEG / video-telemetry for seizure characterization (Unique lists atypical absence, epileptic spasms, generalized tonic-clonic, myoclonic, tonic semiologies). ERG/VEP for retinal dystrophy vs cortical visual impairment. **Auditory brainstem response / newborn hearing screen** — note the useful nuance that hearing screens at birth *"often give a clear response"* despite later SNHL in some, so serial audiology is warranted.

**Functional/ophthalmologic:** slit-lamp for cataract (recommended from the first year of life and then per specialist), dilated fundoscopy for retinal dystrophy.

**Biopsy/histopathology:** bone marrow (above) is the only routinely informative biopsy. Skin biopsy for fibroblast culture is valuable for **research-grade functional confirmation** (enlarged endosomes, IST1 mislocalization, centrosome/cilium assays) — genuinely useful for VUS resolution in this gene given the robust cellular assays published.

### Omics-based diagnostics

- **RNA-seq:** no established role (variants are missense, not splice).
- **Proteomics/metabolomics/liquid biopsy:** no role.
- **Epigenomics:** no *VPS4A* episignature exists — a real opportunity, since an episignature would immediately resolve the VUS burden.

### Clinical criteria and differential diagnosis

No consensus diagnostic criteria exist. Diagnosis is **molecular**, prompted by the gestalt of severe primary microcephaly + profound DD/dystonia + cataract + otherwise-unexplained congenital anemia — a combination that should trigger *VPS4A* consideration specifically. **The anemia is the discriminating clue**: severe microcephaly + ID + dystonia has a long differential, but adding transfusion-dependent congenital dyserythropoietic anemia narrows it dramatically.

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| **CDA type I (*CDAN1*, *CDIN1*)** | Macrocytic anemia, spongy "Swiss cheese" heterochromatin on EM, distal limb anomalies; **no severe microcephaly/dystonia** |
| **CDA type II (*SEC23B*)** | Normocytic anemia, double membrane on EM, SDS-PAGE band 3 pattern; **normal neurodevelopment** |
| **CDA type III (*KIF23*)** | Giant multinucleate erythroblasts; also a **cytokinesis** gene — the closest mechanistic analog |
| ***RACGAP1*-related CDA** | Another cytokinesis-defect CDA; recently described |
| **Majeed syndrome (*LPIN2*)** | CDA + CRMO + inflammation |
| **Pontocerebellar hypoplasia (PCH) types, *TSEN54*, *EXOSC3*, *CASK*** | Overlapping imaging; **anemia and cataract absent** |
| **Autosomal recessive primary microcephaly (MCPH; *ASPM*, *WDR62*, *CDK5RAP2*, *CENPJ*)** | Shares the mitotic/centrosome mechanism and microcephaly; **no anemia, no cataract, milder ID** |
| **Cerebrooculofacioskeletal / Cockayne syndrome** | Microcephaly + cataract + growth failure + progressive course — **strong mimic**; distinguish by photosensitivity, DNA repair assay, absence of dyserythropoiesis |
| **Marinesco-Sjögren syndrome (*SIL1*)** | Cataract + cerebellar hypoplasia + ID + myopathy; **myopathy present, anemia absent** |
| **Congenital disorders of glycosylation (PMM2-CDG)** | Cerebellar hypoplasia, multisystem, coagulopathy; distinguish by transferrin isoform analysis |
| **Mitochondrial encephalopathies** | Frequent diagnostic detour; distinguish by lactate, mtDNA/nuclear panel |
| **Congenital infection (CMV/toxoplasma)** | Microcephaly + cataract + hepatosplenomegaly + thrombocytopenia — **must be excluded**; serology/PCR |
| **Peroxisomal (Zellweger spectrum)** | Hypotonia, hepatomegaly, cataract, seizures; VLCFA testing |

### Screening

- **Newborn screening:** not included in any NBS panel; not a candidate (no treatable metabolic marker, no presymptomatic-treatment benefit).
- **Carrier screening:** not on expanded carrier screening panels; would only be relevant for the recessive alleles in consanguineous populations.
- **Cascade screening:** for *de novo* dominant cases, parental testing is for recurrence-risk counseling, not for finding affected relatives. For biallelic families, sibling carrier testing is appropriate.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **Life expectancy: reduced, but not uniformly.** Rodger et al.: *"Two affected individuals died in childhood or early adult life"* — i.e. **2/6 (33%) mortality** within the reported follow-up. HPO records `HP:0100613` Death in early adulthood at 2/6.
- **No 5-/10-year survival estimates, no formal mortality rate, no actuarial life table exists.** Do not manufacture one.
- **Presumed proximate causes of death** (not systematically reported): respiratory infection/aspiration in the context of severe neurodisability, seizure-related events, complications of chronic transfusion and iron overload. Treat as inference, not evidence.

### Morbidity and function

- **Severe lifelong disability is the rule.** Non-ambulatory (no reported patient achieved independent walking), largely non-verbal, fully dependent for activities of daily living, requiring assisted feeding in a substantial fraction.
- **Disability outcome (ICF framing):** profound impairment across mobility, communication, self-care, and learning domains; complete dependence on caregivers.
- **QoL instruments:** **none applied.** No EQ-5D, PedsQL, CPCHILD, or PROMIS data. This is a clean, well-defined evidence gap suitable for a `KNOWLEDGE_GAP` discussion — and one that matters, because caregiver-reported outcome measures are the plausible endpoint for any future trial in this population.

### Complications

Transfusional and disease-related **iron overload** (disproportionate, due to ineffective erythropoiesis) → hepatic, cardiac, endocrine iron toxicity; **cholelithiasis** from chronic hemolysis; **splenomegaly**; recurrent respiratory infection and aspiration; scoliosis and contractures; dental disease; refractory epilepsy in a subset; **visual loss** from cataract (reversible) and retinal dystrophy (not reversible); chronic kidney disease in at least one patient.

### Recovery potential

**None for the neurodevelopmental core** — the microcephaly and brain malformation are established in utero. Unique is blunt about this: *"There is no cure for CIMDAG syndrome since the effects of the genetic change took place during a baby's formation and development… a complete cure is unlikely, even in the future, since the brain has already formed by the time a diagnosis is made."* Individual features are correctable (cataract surgery, transfusion, chelation, seizure control).

### Prognostic factors

Not formally studied. Reasonable, evidence-anchored predictors to record as **hypotheses**:
1. **Genotype class** — the best-supported predictor. Heterozygous ATPase-domain dominant-negative alleles (R284W/G, E206K, G203E) → severe classic phenotype; biallelic MIT-domain/destabilizing hypomorphs (A28V, R288Q) → milder, with preserved head circumference in at least one case (macrocephaly rather than microcephaly).
2. **Degree of microcephaly** (Z-score) — universal severity marker.
3. **Transfusion burden and iron loading** — modifiable determinant of long-term organ morbidity.
4. **Presence and refractoriness of epilepsy**.

**Prognostic biomarkers:** none validated. Ferritin/LIC are established biomarkers of iron-related risk generically, not of this disease's course.

---

## 12. Treatment

**There is no disease-modifying or targeted therapy. Management is entirely supportive, multisystem, and multidisciplinary.** Unique's management recommendation is the closest thing to a guideline that exists:

> "Children with CIMDAG syndrome should be under the care of a multidisciplinary team. The team should include a geneticist and paediatric neurologist who can oversee care so that development and behaviour can be monitored, and the best help given in the form of physiotherapy, occupational therapy, speech therapy and, if needed, behavioural therapy. For signs of anaemia or haemolysis (pallor, jaundice, decreased level of energy, or abnormal CBC/reticulocyte count), evaluation and care by a paediatric haematologist is recommended. Ophthalmology evaluation is also recommended, starting at the first year of life and then as frequently as is recommended by the specialist."

### Pharmacotherapy

| Treatment | Indication | Suggested NCIT | Modality |
|---|---|---|---|
| **Anti-seizure medications** — lamotrigine, oxcarbazepine, levetiracetam, clobazam (Unique names these explicitly); rescue diazepam or midazolam | Epilepsy (3/6) | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` per drug (CHEBI: lamotrigine `CHEBI:6367`, levetiracetam `CHEBI:6437`, clobazam `CHEBI:31413`, diazepam `CHEBI:49575`, midazolam `CHEBI:6931`) | SMALL_MOLECULE |
| **Iron chelation** — deferasirox / deferoxamine / deferiprone | Transfusional + ineffective-erythropoiesis iron overload | `NCIT:C15986`; agents `CHEBI:49005` (deferasirox), `CHEBI:4356` (deferoxamine) | SMALL_MOLECULE |
| **Laxatives / stool softeners; magnesium** | Constipation (family-reported: *"Magnesia helps us a lot due to its beneficial characteristics on muscle soreness and constipation"*) | `NCIT:C15747` Supportive Care | SMALL_MOLECULE |
| **Anti-reflux therapy** | GERD | `NCIT:C15986` | SMALL_MOLECULE |
| **Sleep-directed medication** (unspecified; families report use) | Sleep disturbance (4/4) | `NCIT:C15986` | SMALL_MOLECULE |
| **Dystonia-directed pharmacotherapy** (trihexyphenidyl, baclofen, botulinum toxin) | Dystonia (5/6) — *not specifically documented in CIMDAG literature; extrapolated from standard dystonia care; flag as inferred* | `NCIT:C15986` | SMALL_MOLECULE |
| **Phototherapy / bilirubin management** | Neonatal and prolonged jaundice | `NCIT:C15747` | DEVICE/OTHER |

**Pharmacogenomics:** nothing *VPS4A*-specific. Standard PGx applies (e.g. HLA-B\*15:02 / HLA-A\*31:01 for carbamazepine-family anti-seizure drugs, relevant given oxcarbazepine use; CPIC guideline). Worth recording because this population is disproportionately exposed to aromatic antiepileptics.

### Transfusion support

**Red cell transfusion** is the mainstay for the anemia. Observed intervals in the Seu cohort: **every 4–6 weeks (proband 1), every 4–10 weeks (proband 2), every 2–6 months (proband 3)**. NCIT: `NCIT:C15380` Blood Transfusion (verify with OAK) / `NCIT:C15747` Supportive Care. Modality: `OTHER`.

### Advanced therapeutics

| Approach | Status for CIMDAG |
|---|---|
| **Gene therapy / gene replacement** | Not developed. Conceptually **poorly suited** to the dominant form — adding wild-type *VPS4A* does not remove poisoned hexamers, and the CNS phenotype is prenatal. |
| **Allele-selective silencing (ASO / siRNA / CRISPR base editing)** | **The mechanistically correct strategy** for the dominant-negative alleles: selectively knock down the mutant transcript, since haploinsufficiency is tolerated (LoF alleles are present in gnomAD). This is an unusually favorable therapeutic logic and deserves to be recorded as a hypothesis. **No program exists.** The recurrent c.850A>T hotspot in 5/11 patients is an ideal allele-specific target. |
| **Cell therapy / HSCT** | Not reported. Would be theoretically rational for the *hematologic* component only (the erythroid defect is cell-autonomous in HSPCs), leaving the neurological phenotype untouched — a difficult risk/benefit calculus in a child with profound neurodisability. **Purely speculative; no case reports.** |
| **Targeted small molecules** | None. VPS4 *inhibitors* exist in oncology (PMID:42032367) — the wrong direction pharmacologically for this disease. No VPS4A chaperone/stabilizer program. |
| **Immunotherapy** | Not applicable. |

### Surgical and interventional

- **Cataract extraction** — high-value, low-burden. Unique quotes a family: *"Check the eyes on a regular basis – if a cataract is diagnosed it can be easily removed with a small surgery."* NCIT: `NCIT:C15329` Surgical Procedure (or a specific lens-extraction term if OAK resolves one). Modality: `SURGERY`.
- **Gastrostomy (PEG/G-tube) or nasogastric tube** — for feeding failure/aspiration in the subset with severe difficulty. `NCIT:C15329`. Modality: `SURGERY`/`DEVICE`.
- **Orthopedic surgery** — talipes correction, scoliosis management. `NCIT:C16186` Orthopedic Surgical Procedure. Modality: `SURGERY`.
- **Splenectomy** — **not reported and not recommended** in this disease; note explicitly, since it is a standard consideration in other congenital hemolytic anemias and its role here is unknown.
- **Dental treatment under general anesthesia** — frequently required.

### Supportive and rehabilitative

- **Physiotherapy** (`NCIT:C15302` Physical Therapy, `BEHAVIORAL`) — including hydrotherapy and hippotherapy, both named by families.
- **Occupational therapy** (`NCIT:C121351`, `BEHAVIORAL`).
- **Speech and language therapy + AAC** (`NCIT:C159273`, `BEHAVIORAL`) — Unique emphasizes AAC (pictograms, gestures, simplified sign, high-tech aided communication) given that many remain non-verbal.
- **Orthotics/bracing** — insoles, braces, splints, callipers, spinal bracing; wheelchair and mobility aids (`DEVICE`).
- **Nutritional support** — high-energy formula, positioning for feeds (`NCIT:C15433`; note the CLAUDE.md caution — do **not** auto-tag nutritional support as `BEHAVIORAL`; here the modality is genuinely dietary/behavioral for positioning and formula, so judge per item).
- **Behavioral therapy and sleep hygiene** (`NCIT:C181743`, `BEHAVIORAL`).
- **Genetic counseling** (`NCIT:C15240`).

### Experimental treatments / clinical trials

**No interventional trial for CIMDAG or *VPS4A* exists** — a ClinicalTrials.gov API query for "VPS4A OR CIMDAG" returns **zero studies** (checked 2026-08-01).

The one registered study capturing these patients is observational:
- **NCT02964494 — The Congenital Dyserythropoietic Anemia Registry (CDAR)**; sponsor Cincinnati Children's Hospital Medical Center; observational patient registry; **recruiting**; estimated enrollment 10,000; condition: Congenital Dyserythropoietic Anemia. This registry is how the three Seu et al. probands were ascertained, and it maintains a blood/bone-marrow biorepository. It is the correct `clinical_trials` entry for a dismech CIMDAG page, curated with the caveat that it is CDA-wide rather than VPS4A-specific.

### Treatment outcomes

No response-rate data. Transfusion reliably corrects hemoglobin; chelation reliably lowers ferritin/LIC (generic evidence, not CIMDAG-specific). Cataract surgery outcomes not reported in this cohort. Anti-seizure efficacy anecdotal — Unique: *"there are currently (2024) no specific recommendations for treating CIMDAG syndrome seizures."* Adverse events are those of the generic therapies (chelator nephro/hepatotoxicity and cytopenias; transfusion reactions and alloimmunization; antiepileptic AEs).

### Treatment strategy

No algorithm exists. A defensible, evidence-anchored care schedule assembled from the Unique recommendations:

1. **At diagnosis:** CBC + reticulocyte count; brain MRI; ophthalmology (slit lamp + fundoscopy); audiology; EEG if paroxysmal events; feeding/swallow assessment; genetic counseling.
2. **Annually from age 1:** iron status (ferritin ± LIC by MRI); ophthalmology per specialist; growth and nutrition; audiology; spine and hip surveillance.
3. **Ongoing:** PT/OT/SLT; dental review; sleep review; hematology follow-up with transfusion and chelation as indicated.
4. **As needed:** cataract extraction; gastrostomy; orthopedic intervention; anti-seizure escalation.

**Personalized medicine:** genotype currently informs prognosis (dominant-negative vs. biallelic hypomorph) but not therapy. Genotype-guided therapy would become real only with allele-selective silencing.

---

## 13. Prevention

- **Primary prevention:** **not possible** for *de novo* dominant cases — by definition unpredictable and unpreventable. Unique makes the non-blame point explicitly: *"It is important to recognize that no one should be blamed for variants in their DNA and no parent is at fault when a new DNA change occurs in their child."* For the recessive form, reduction of consanguinity-associated risk at the population level is the only structural lever, and is a public-health rather than clinical intervention.
- **Secondary prevention (early detection):** the actionable tier. Early molecular diagnosis via trio WES/WGS enables the surveillance schedule above. Unique: *"knowing the diagnosis means that appropriate monitoring and interventions can be put in place early to help each child reach their full potential."* Specific high-yield items: first-year ophthalmology to catch surgically remediable cataract; CBC/retic at diagnosis to catch anemia; annual iron monitoring from age 1 to pre-empt organ iron loading.
- **Tertiary prevention:** iron chelation to prevent cardiac/hepatic/endocrine iron toxicity; aspiration precautions and gastrostomy to prevent recurrent pneumonia; postural management, orthotics, and spinal surveillance to prevent contracture and scoliosis progression; dental care to prevent decay and erosion from bruxism; seizure control.
- **Immunization:** no disease-specific vaccine. **Standard schedule plus enhanced respiratory protection** (influenza, pneumococcal, RSV per local policy) is appropriate for a child with severe neurodisability and aspiration risk. Transfusion-dependent patients should be hepatitis B immune.
- **Genetic screening / reproductive options:** prenatal diagnosis and preimplantation genetic testing (PGT-M) are available once the familial variant is known. For *de novo* cases, recurrence risk is *"usually less than 1%"* with germline mosaicism as the residual mechanism; for biallelic families, **25% per pregnancy** with both parents heterozygous carriers.
- **Genetic counseling:** essential and should be offered at diagnosis and again at reproductive planning for parents and, later, for unaffected siblings (carrier status relevant only in the recessive families). NCIT: `NCIT:C15240`.
- **Risk stratification / public health / environmental interventions:** not applicable.
- **Prophylaxis:** no disease-specific prophylactic medication.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBI Taxon | Gene | Identifier |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *VPS4A* | NCBI Gene 27183; HGNC:13488 |
| *Mus musculus* | NCBITaxon:10090 | *Vps4a* | **MGI:1890520**; NCBI Gene 116733; Chr8:107,757,901–107,772,392 (+) |
| *Danio rerio* | NCBITaxon:7955 | *vps4a* | ZFIN (see model below) |
| *Drosophila melanogaster* | NCBITaxon:7227 | *Vps4* | Single ortholog |
| *Caenorhabditis elegans* | NCBITaxon:6239 | *vps-4* | Single ortholog |
| *Saccharomyces cerevisiae* | NCBITaxon:4932 | *VPS4/END13* | Single ortholog |

**Evolutionary conservation is the key comparative fact and it has direct disease relevance:** most organisms encode **one** VPS4; only vertebrates/mammals have the *VPS4A*/*VPS4B* paralog pair. Dvilansky et al. showed the paralogs are **functionally non-redundant** — VPS4A acts earlier in abscission and cannot be substituted by VPS4B — which is precisely why a heterozygous *VPS4A* missense allele causes human disease despite an intact *VPS4B*. Any invertebrate or yeast model necessarily collapses this paralog distinction and therefore cannot model the human genetics faithfully, only the core ESCRT biochemistry. The affected residues (Ala28, Gly203, Glu206, Arg284, Arg288) are deeply conserved across all these orthologs.

### Breed

Not applicable (`VBO`: no entries).

### Natural disease in other species

**None known.** An OMIA search for *VPS4A* returns **no entries** in any species — no naturally occurring *VPS4A* disease has been described in companion animals, livestock, or wildlife. Record this as an explicit negative rather than omitting the section.

### Comparative pathology

Only engineered models exist (§15). The cross-species comparison that has been made — zebrafish *vps4a* T248I vs. human patients — is informative: the fish reproduce the **central** origin of hypotonia (*"Resembling the central form of hypotonia in VPS4A patients, motor neurons and muscle cells are functional in mutant zebrafish"*) and the endosomal/exosome defect, but the fish inner ear is **unaffected**, unlike the SNHL seen in 2/5 human patients.

### Transmission

Not applicable — non-infectious, non-zoonotic, no cross-species susceptibility.

---

## 15. Model Organisms

### 15.1 Zebrafish — the best available whole-organism neurological model

**Shipman et al., *J Neurosci* 2024;44(50):e0680242024. PMID:39455257; PMCID:PMC11638813; DOI:10.1523/JNEUROSCI.0680-24.2024**

Abstract **[abstract]**:
> "Mutations in human VPS4A are associated with neurodevelopmental defects, including motor delays and defective muscle tone. VPS4A encodes a AAA-ATPase required for membrane scission, but how mutations in VPS4A lead to impaired control of motor function is not known. Here we identified a mutation in zebrafish *vps4a*, T248I, that affects sensorimotor transformation."

- **Model type:** forward-genetic missense allele, *vps4a*^T248I^, in the AAA-ATPase domain (mechanistically parallel to the human ATPase-domain alleles).
- **Molecular validation:** the mutation *"reduces the ATPase activity of Vps4a and disassembly of ESCRT filaments, which mediate membrane scission"* — the same primary lesion as in patients.
- **Phenotypes recapitulated:** *"Optomotor responses, vestibulospinal, and acoustic startle reflexes are absent or strongly impaired"*; larvae *"fail to maintain an upright posture"* and *"swim sideways or upside down"*; *"decreased numbers of circulating exosomes in brain ventricles"*; *"enlarged endosomal compartments in the CNS"*; upregulation of *atf3* and *jun* stress-response genes.
- **Key mechanistic dissociation:** *"Resembling the central form of hypotonia in VPS4A patients, motor neurons and muscle cells are functional in mutant zebrafish"* — establishing that the hypotonia/motor phenotype is **central**, arising at the level of sensorimotor transformation, not neuromuscular.
- **Limitations:** *"the function of the inner ear in vps4a^T248I^ larvae is unaffected"* and vestibulo-ocular responses to head rotation are normal — so the model does **not** capture human SNHL. It also does not model microcephaly, cataract, or the anemia, and zebrafish lack the VPS4A/VPS4B paralog split in the mammalian configuration.
- **Applications:** sensorimotor circuit function, exosome biology in vivo, CNS endosomal morphology, small-molecule screening for motor-function rescue.
- **Resource:** ZFIN.

### 15.2 Mouse

**MGI:1890520 (*Vps4a*).** The MGI record lists **19 mutations/alleles** across three classes — **6 endonuclease-mediated, 9 gene-trapped, 4 targeted** — with 19 strains/lines available through **IMSR**. Existing phenotype annotations (8 phenotypes from one allele in one background, plus one multigenic phenotype) span **craniofacial, digestive, embryonic development, growth/size, hematopoietic, integument, immune, and mortality/aging** systems. **MGI records no human disease model association for *Vps4a*** — i.e., **no mouse has yet been designated a CIMDAG model.**

**What exists:**
- **Cardiomyocyte-specific *Vps4a* conditional knockout** (PMC10341959): impaired autophagic flux — *Vps4a* is *"mainly involved in the sealing of autophagosome in cardiomyocytes"* — with cardiac hypertrophy (increased HW/BW and HW/TL), partial LV dilation, reduced ejection fraction, and **partial lethality beginning at 3 months**, some surviving beyond 12 months. Confirms an in vivo autophagy role for Vps4a but models **no** CIMDAG feature (patients have no reported cardiomyopathy).
- **Double *Vps4a*/*Vps4b* heterozygous null MEFs:** increased endo/lysosomal organelles with large multi-membrane structures.

**The critical gap:** **no knock-in mouse carrying a patient allele (e.g. *Vps4a*^R284W/+^) has been reported.** This is the single most valuable missing model. Because the mechanism is dominant-negative and the paralog architecture is mammal-specific, a heterozygous knock-in mouse — not a knockout — is the design that would test whether the human genetics reproduce in vivo, and would be the required platform for any allele-selective silencing preclinical program. Note also that a *Vps4a* **knockout** mouse would likely be uninformative for CIMDAG, since human heterozygous LoF is tolerated.

Register this as a `HUMAN_MODEL_MISMATCH` discussion rather than a plain `KNOWLEDGE_GAP`: model-system evidence exists (zebrafish missense, mouse conditional KO), but its fidelity to the human dominant-negative, paralog-dependent disease is the open question.

### 15.3 Cellular and in vitro models — the workhorses of this field

| Model | Findings | Source |
|---|---|---|
| **Proband-derived dermal fibroblasts** (R284W, R284G) | Enlarged endosomes; IST1 accumulation on limiting membranes; abnormal centrosome number/morphology; multipolar spindles; lagging/bridging chromosomes; micronuclei; irregular nuclei; ↑γH2AX; G2/M accumulation; "dot cilium" | PMID:33186545 |
| **Proband-derived iPSCs → i³Neurons** (NGN2-induced) | *"significant increase in the percentage of neurons that had enlarged structures marked by CD63, LAMP1, or the lysosomal enzyme cathepsin D"*; increased IST1 puncta on early/late endosomes; mutant overexpression *"incompatible with neuronal survival"* | PMID:33186545 |
| **CRISPRi *VPS4A* knockdown in i³Neurons** | *"largely recapitulates phenotypes that are observed in proband cells expressing dominant-negative VPS4A at physiological heterozygous levels"* — an isogenic complement to patient cells | PMID:33186545 |
| **Proband-derived iPSC → erythroid differentiation** (R284W) | Asynchronous, prematurely maturing erythropoiesis; increased binucleated erythroblasts; poor growth (similar to *CDAN1*-mutant cells); *"persistent cytoplasmic bridges between erythroblasts… even after attempted completion of cytokinesis"* — **the hematologic phenotype recapitulated in a dish** | PMID:33186543 |
| **Heterologous overexpression (HeLa/U2OS)** | Mutants phenocopy the canonical ATPase-dead **E228Q** dominant negative: *"Expression of VPS4A-p.Arg284Trp, VPS4A-p.Arg284Gly, or VPS4A-p.Glu206Lys caused the development of vacuolar endosomal structures identical to those generated by VPS4A-p.Glu228Gln expression"* | PMID:33186545 |
| **STORM super-resolution + siRNA paralog depletion** | VPS4A vs VPS4B abscission-stage specificity; VTA1/ANCHR checkpoint interplay | PMID:38687820 |
| **Structural modeling + cell assays (R288Q)** | Loss of stability; impaired LC3B interaction; reduced lipid-droplet localization; ↑lipid accumulation, ↑FFA, ↑ROS | PMID:42498620 |

**Phenotype recapitulation summary:** the cellular models are unusually strong — patient fibroblasts and patient iPSC-derived erythroblasts reproduce the disease-defining cellular lesions faithfully, and iPSC-neurons reproduce the endolysosomal lesion. **This makes the assay set genuinely usable for VUS resolution (PS3-level functional evidence).** What no model yet captures: microcephaly in vivo, cataract, growth failure, and the integrated multisystem phenotype.

### 15.4 Databases

MGI (`informatics.jax.org`) · IMSR (19 *Vps4a* lines) · IMPC · ZFIN · Alliance of Genome Resources · FlyBase · WormBase · SGD · DepMap (VPS4A/VPS4B synthetic lethality) · Cellosaurus (for patient iPSC lines, if deposited).

---

## Appendix A — Consolidated ontology term suggestions for KB entry

**Disease:** `MONDO:0035819`
**Gene:** `hgnc:13488` (*VPS4A*) — note dismech lowercase `hgnc:` convention
**Inheritance:** `HP:0000006` autosomal dominant (primary); `HP:0010985`? no — use `HP:0000007` autosomal recessive for the biallelic branch

**Top HPO terms (with frequency band):**
`HP:0011344` severe global developmental delay (OBLIGATE/VERY_FREQUENT, 6/6) · `HP:0010864` severe intellectual disability (6/6) · `HP:0000252` microcephaly (6/6) · `HP:0000505` visual impairment (6/6) · `HP:0001332` dystonia (5/6) · `HP:0001252` hypotonia (5/6) · `HP:0001270` motor delay (5/5) · `HP:0000750` delayed speech and language development (5/5) · `HP:0000519` developmental cataract (4/5) · `HP:0001257` spasticity (4/5) · `HP:0002360` sleep disturbance (4/4) · `HP:0011968` feeding difficulties (4/6) · `HP:0002240` hepatomegaly (4/5) · `HP:0001250` seizure (3/6) · `HP:0000556` retinal dystrophy (3/5) · `HP:0011451` primary microcephaly (3/6) · `HP:0001321` cerebellar hypoplasia · `HP:0033725` thin corpus callosum · `HP:0000407` sensorineural hearing impairment (2/5) · `HP:0100613` death in early adulthood (2/6) · `HP:0031688` erythroid dysplasia · `HP:0001878` hemolytic anemia · `HP:0001744` splenomegaly · `HP:0001510` growth delay · `HP:0001414` microvesicular hepatic steatosis · `HP:0009125` lipodystrophy · `HP:0001081` cholelithiasis

**GO BP:** `GO:1904903`, `GO:1904896`, `GO:0071985`, `GO:0032509`, `GO:0061952`, `GO:0007084`, `GO:0060271`, `GO:0007059`, `GO:0006914`
**GO CC:** `GO:0000815`, `GO:0005770`, `GO:0005769`, `GO:0005764`, `GO:0030496`, `GO:0090543`, `GO:0005813`, `GO:0000922`, `GO:0005635`, `GO:0005811`, `GO:0070062`
**GO MF:** `GO:0016887` ATP hydrolysis activity
**CL:** `CL:0000047`, `CL:0000540`, `CL:0000765`, `CL:0000558`, `CL:0000232`, `CL:0000057`, `CL:0000121`
**UBERON:** `UBERON:0000955`, `UBERON:0002037`, `UBERON:0002336`, `UBERON:0000988`, `UBERON:0002371`, `UBERON:0000965`, `UBERON:0000966`, `UBERON:0002107`, `UBERON:0002106`
**NCIT (treatment):** `NCIT:C15986`, `NCIT:C15747`, `NCIT:C15302`, `NCIT:C121351`, `NCIT:C159273`, `NCIT:C15329`, `NCIT:C16186`, `NCIT:C15240`, `NCIT:C15433`

**Candidate dismech module conformance:**
- `ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction` — **partial/atypical** (cilium defect is secondary to ESCRT failure, not an IFT/BBSome lesion). Curate with an explicit caveat.
- `hemolytic_anemia_erythrocyte_destruction#Premature Erythrocyte Destruction` — fits the Lunati/hemolytic arm.
- No existing module covers ESCRT-III recycling failure or cytokinetic abscission failure. **A new `escrt_membrane_scission_failure` or `cytokinetic_abscission_failure` module is a well-motivated candidate** — abscission failure is a conserved mechanism shared with *KIF23*-CDA III, *RACGAP1*-CDA, and the centrosomal MCPH microcephaly genes, which is exactly the recurrence profile that justifies a module.

## Appendix B — Primary reference list

| PMID | Citation | Role |
|---|---|---|
| **33186545** | Rodger C, et al. De Novo VPS4A Mutations Cause Multisystem Disease with Abnormal Neurodevelopment. *Am J Hum Genet*. 2020 Dec 3;107(6):1129–1148. DOI:10.1016/j.ajhg.2020.10.012. PMC7820634 | **Landmark — disease definition, 6 probands, cell biology** |
| **33186543** | Seu KG, Trump LR, Emberesh S, Lorsbach RB, Johnson C, Meznarich J, Underhill HR, Chou ST, Sakthivel H, Nassar NN, Seu KJ, Blanc L, Zhang W, Lutzko CM, Kalfa TA. VPS4A Mutations in Humans Cause Syndromic Congenital Dyserythropoietic Anemia due to Cytokinesis and Trafficking Defects. *Am J Hum Genet*. 2020 Dec 3;107(6):1149–1156. DOI:10.1016/j.ajhg.2020.10.013. PMC7820805 | **Landmark companion — hematology, 3 probands incl. the homozygous case** |
| **33460484** | Lunati A, et al. VPS4A mutation in syndromic congenital hemolytic anemia without obvious signs of dyserythropoiesis. *Am J Hematol*. 2021 Apr 1;96(4):E121–E123. DOI:10.1002/ajh.26099 | Phenotype expansion — hemolysis without dyserythropoiesis |
| **42498620** | Gupta A, Mathuria YP, Jain BP, Gupta SK, Ghosh DK. A novel VPS4A variant drives lipotoxicity underlying CIMDAG syndrome. *J Clin Lipidol*. 2026 Jul 9. DOI:10.1016/j.jacl.2026.07.007 | **Newest** — second homozygous case (p.Arg288Gln), lipotoxicity mechanism |
| **38687820** | Dvilansky I, et al. The human AAA-ATPase VPS4A isoform and its co-factor VTA1 have a unique function in regulating mammalian cytokinesis abscission. *PLoS Biol*. 2024 Apr 30;22(4):e3002327. PMC11086821 | Paralog non-redundancy — why VPS4B cannot compensate |
| **39455257** | Shipman A, et al. Defects in Exosome Biogenesis Are Associated with Sensorimotor Defects in Zebrafish vps4a Mutants. *J Neurosci*. 2024 Dec 11;44(50):e0680242024. PMC11638813 | **Best in vivo neurological model** |
| **35441598** | King R, Gallagher PJ, Khoriaty R. The congenital dyserythropoietic anemias: genetics and pathophysiology. *Curr Opin Hematol*. 2022 May 1;29(3):126–136 | Review placing VPS4A among CDA genes |
| — | Unique / Rare Chromosome Disorder Support Group. *CIMDAG syndrome (also known as VPS4A-related neurodevelopmental disorder)*. 2024. Authors: Steidle-Kloc E, Winter T, Kalfa TA, Unique (AP) | **Only management-guidance document in existence**; clinician-authored; source for patient count, natural history, and care recommendations |
| — | OMIM #619273 / *609982; Orphanet ORPHA:603448; HPO annotation for OMIM:619273; UniProt Q9UN37; MGI:1890520; ClinicalTrials.gov NCT02964494 | Reference resources |

---

## Appendix C — Explicit gaps and open questions (candidates for `discussions` blocks)

1. **`KNOWLEDGE_GAP` — static vs progressive.** Is CIMDAG a static congenital malformation syndrome or a progressive neurodegeneration? Imaging language in Seu et al. is explicitly neurodegenerative; no longitudinal imaging series exists. *Proposed experiment:* serial MRI in the ~11 known patients + the diagnosed-but-unpublished cohort known to Unique.
2. **`KNOWLEDGE_GAP` — micronuclei → cGAS-STING interferonopathy.** Patient fibroblasts make micronuclei; VPS4 inhibition activates cGAS-STING in tumor models. No one has measured an interferon signature in patient blood. *Proposed experiment:* IFN-stimulated gene score on patient PBMCs.
3. **`HUMAN_MODEL_MISMATCH` — no knock-in mouse.** All mouse data are knockout/conditional-knockout; the human mechanism is heterozygous dominant-negative in a paralog-redundant-but-non-equivalent system. A *Vps4a*^R284W/+^ knock-in is the required model and does not exist.
4. **`KNOWLEDGE_GAP` — HPOA frequency discrepancy.** HPO annotation records cerebellar hypoplasia at 2/6 while Rodger full text states 5/6; anemia is absent from HPOA entirely despite being present in ~7/10 published patients. The HPOA record for OMIM:619273 under-annotates the hematologic domain.
5. **`KNOWLEDGE_GAP` — no episignature, no QoL instrument, no natural history study, no prevalence estimate.**
6. **Therapeutic hypothesis worth recording:** allele-selective knockdown of the mutant transcript is the mechanistically correct strategy, uniquely supported by the fact that *VPS4A* haploinsufficiency is tolerated in the general population. The recurrent c.850A>T hotspot (5/11 patients) is an ideal ASO/siRNA/base-editing target. No program exists.
7. **Unresolved genotype–phenotype:** four unrelated p.Arg284Trp probands differ markedly in seizures, hearing, anemia, and hepatic involvement — the source of intra-allelic variable expressivity is unknown.

---

**Sources:**
[Rodger et al. 2020, AJHG (PMC7820634)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7820634/) · [Seu et al. 2020, AJHG (PMC7820805)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7820805/) · [Lunati et al. 2021, Am J Hematol](https://onlinelibrary.wiley.com/doi/10.1002/ajh.26099) · [Gupta et al. 2026, J Clin Lipidol (PMID:42498620)](https://pubmed.ncbi.nlm.nih.gov/42498620/) · [Shipman et al. 2024, J Neurosci (PMC11638813)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638813/) · [Dvilansky et al. 2024, PLoS Biol (PMC11086821)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11086821/) · [Unique: CIMDAG syndrome guide (2024)](https://rarechromo.org/media/singlegeneinfo/Single%20Gene%20Disorder%20Guides/CIMDAG%20syndrome%20FTNW.pdf) · [OMIM #619273](https://www.omim.org/entry/619273) · [OMIM *609982](https://omim.org/entry/609982) · [HPO annotations for OMIM:619273](https://ontology.jax.org/api/network/annotation/OMIM:619273) · [MONDO:0035819 via OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0035819) · [UniProt Q9UN37](https://rest.uniprot.org/uniprotkb/Q9UN37.txt) · [HGNC:13488](https://rest.genenames.org/fetch/symbol/VPS4A) · [MGI:1890520 (Vps4a)](https://www.informatics.jax.org/marker/MGI:1890520) · [Vps4a cardiomyocyte KO (PMC10341959)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10341959/) · [CDAR registry NCT02964494](https://clinicaltrials.gov/study/NCT02964494) · [Genomics England PanelApp — VPS4A (Rare anaemia)](https://panelapp.genomicsengland.co.uk/panels/518/gene/VPS4A/) · [ClinVar VPS4A](https://www.ncbi.nlm.nih.gov/clinvar/?term=VPS4A%5Bgene%5D)