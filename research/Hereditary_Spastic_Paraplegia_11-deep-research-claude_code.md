---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-24T19:03:56.455830'
end_time: '2026-08-24T19:08:29.695886'
duration_seconds: 273.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Spastic Paraplegia 11
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
  num_turns: 16
  total_cost_usd: 0.867356
  session_id: 5f967ed8-4b7d-5ed5-b009-2720effe579b
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 11
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 11** covering all of the
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

I'll research current information on Hereditary Spastic Paraplegia 11 (SPG11) using web search to ensure accurate, well-cited findings.

I now have sufficient primary-literature grounding to compile the full report.

I now have comprehensive, well-sourced material to compile the full research report.

# Hereditary Spastic Paraplegia 11 (SPG11): Comprehensive Research Report

## 1. Disease Information

### Overview

Hereditary Spastic Paraplegia 11 (SPG11) is an autosomal recessive, complex (complicated) form of hereditary spastic paraplegia caused by biallelic loss-of-function variants in the *SPG11* gene, encoding the protein **spatacsin**. It is the most common cause of autosomal recessive HSP overall and the most frequent cause of "HSP with thin corpus callosum" (ARHSP-TCC), accounting for roughly **19–31% of autosomal recessive HSP cases**, up to **30–50% of complex autosomal recessive HSP**, and up to **59–70%** of cases when both intellectual impairment and thin corpus callosum are present, but fewer than 10% of "pure" HSP cases (NCBI GeneReviews, [Spastic Paraplegia 11](https://www.ncbi.nlm.nih.gov/books/NBK1210/)).

Clinically, SPG11 presents with progressive spastic paraparesis of the lower limbs combined with a broad multisystem neurodegenerative syndrome: mild intellectual disability/learning difficulty in childhood and/or progressive cognitive decline, axonal peripheral neuropathy (reported in >80% of cases), pseudobulbar signs (dysarthria, hypomimia), and brisk upper-limb reflexes. Less frequent findings include cerebellar signs (found in over half of patients, per [ScienceDirect topic overview](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/spg11)), retinal/macular degeneration (Kjellin syndrome), pes cavus, scoliosis, tremor and parkinsonism, and, uncommonly, epilepsy. The disease was historically also described under names such as Nakamura-Osame syndrome.

### Key Identifiers

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 604360 — Spastic Paraplegia 11, Autosomal Recessive ([OMIM:604360](https://omim.org/entry/604360)) |
| OMIM (gene) | 610844 — SPG11, Vesicle Trafficking Associated, Spatacsin ([OMIM:610844](https://omim.org/entry/610844)) |
| Gene | *SPG11* (formerly *KIAA1840*), chromosome 15q21.1 |
| Orphanet | ORPHA:2822 — Autosomal recessive spastic paraplegia type 11 ([Orphanet](https://www.orpha.net/en/disease/detail/2822)) |
| MONDO | MONDO term for "hereditary spastic paraplegia 11" (mapped from OMIM 604360; used by GARD/NORD, [GARD entry](https://rarediseases.info.nih.gov/diseases/4919/hereditary-spastic-paraplegia-11), [NORD MONDO page](https://rarediseases.org/mondo-disease/hereditary-spastic-paraplegia-11/)) |
| GeneReviews | Spastic Paraplegia 11 ([NBK1210](https://www.ncbi.nlm.nih.gov/books/NBK1210/)) |
| ICD-10 | G11.4 (Hereditary spastic paraplegia) — generic code; no SPG11-specific ICD-10/11 code exists |

### Synonyms

- Nakamura-Osame syndrome
- Autosomal recessive hereditary spastic paraplegia with thin corpus callosum (ARHSP-TCC)
- Spastic paraplegia-intellectual disability-thin corpus callosum syndrome
- Kjellin syndrome (when central retinal degeneration is prominent)
- ALS5 and CMT2X are allelic disorders (see §4)

### Data Source Type

Information below is aggregated from disease-level resources (OMIM, Orphanet, GeneReviews, MONDO) and case-series/cohort literature (typically tens to low hundreds of patients), rather than large-scale EHR/claims data, reflecting SPG11's rarity.

---

## 2. Etiology

### Disease Causal Factors

SPG11 is a **monogenic, purely genetic** disease. It is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants** in *SPG11*. GeneReviews states that "most pathogenic variants identified to date in SPG11 predict truncation of the protein, demonstrating that pathogenicity results from loss of spatacsin function" ([NBK1210](https://www.ncbi.nlm.nih.gov/books/NBK1210/)). More than 100 distinct mutations have been catalogued across the 15q21.1 locus, including nonsense, frameshift (small insertions/deletions), splice-site, and exon-level or larger deletion/duplication variants; approximately 10–20% of disease alleles are exon-sized or larger structural rearrangements not detectable by sequencing alone ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1210/); [ScienceDirect](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/spg11)).

The founding gene-identification study, Stevanin et al. (2007, *Nature Genetics* 39:366–372, DOI 10.1038/ng1980), analyzed 12 autosomal recessive HSP-with-thin-corpus-callosum families linked to the SPG11 locus on chromosome 15 and identified ten mutations — nonsense or frameshift-causing insertions/deletions — in a previously uncharacterized gene expressed ubiquitously in the nervous system, most prominently in cerebellum, cerebral cortex, hippocampus, and pineal gland ([Nature Genetics](https://www.nature.com/articles/ng1980)).

### Genotype–Phenotype Correlation

Missense and splice-site variants (which may retain partial protein function) are associated with **later onset and milder disease severity**, whereas truncating (nonsense/frameshift) variants — the majority of pathogenic alleles — produce the more typical earlier-onset, severe phenotype ([GeneReviews NBK1210](https://www.ncbi.nlm.nih.gov/books/NBK1210/)).

### Risk Factors

- **Genetic**: Biallelic pathogenic *SPG11* variants are both necessary and sufficient — this is a fully penetrant Mendelian recessive disease, not a susceptibility-locus condition. There is no meaningful "risk allele" concept beyond carrier status.
- **Consanguinity**: Most originally described families derive from populations/regions where consanguinity is common (Mediterranean basin, Middle East, North Africa), though the disease has now been reported worldwide ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1210/)).
- **Founder effects**: Regional recurrent variants have been reported in various populations, consistent with founder mutations, though *SPG11* mutational spectrum is broadly heterogeneous rather than dominated by one global founder allele.
- **De novo occurrence**: Rare; at least one reported case involved one variant inherited from a carrier parent and a second occurring de novo in the proband ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1210/)).
- **Environmental/lifestyle factors**: None established — SPG11 has no known environmental, infectious, dietary, or occupational risk-factor contribution. This distinguishes it from complex/multifactorial neurodegenerative diseases.

### Protective Factors

No genetic or environmental protective factors have been described. There is no evidence of modifier alleles ameliorating disease course in the literature reviewed, though variability in age of onset (1–60 years) and severity even among individuals with the same genotype suggests unidentified modifiers or stochastic factors may exist.

### Gene–Environment Interactions

None established; SPG11 pathogenesis is driven by loss of spatacsin protein function rather than gene–environment interplay.

---

## 3. Phenotypes

SPG11 produces a multisystem, progressive clinical picture. Below, phenotypes are grouped with suggested HPO terms, onset/frequency where reported, and progression pattern.

### Motor/Corticospinal Phenotypes

| Phenotype | HPO term (suggested) | Frequency/Notes |
|---|---|---|
| Progressive spastic paraparesis (lower-limb spasticity and weakness) | HP:0007256 (progressive spasticity), HP:0002061 (spastic paraparesis) | Core feature, essentially 100% |
| Hyperreflexia (upper limb) | HP:0001347 | Common |
| Extensor plantar responses (Babinski sign) | HP:0003487 | Common |
| Pseudobulbar signs — dysarthria, hypomimia | HP:0001260 (dysarthria), HP:0000338 (hypomimia) | Frequent |
| Lower motor neuron/muscle wasting (ALS5-like presentation) | HP:0003202 (muscle wasting) | Reported, especially in later stage/motor-predominant presentations |

Wheelchair dependence typically develops **1–2 decades after disease onset** ("Most affected individuals become wheelchair bound one or two decades after disease onset," per [GeneReviews NBK1210](https://www.ncbi.nlm.nih.gov/books/NBK1210/)).

### Cognitive/Behavioral Phenotypes

- **Cognitive impairment/intellectual disability**, present in **80–100%** of patients according to a recent clinical-genetic-imaging cohort study ([PMC10743703](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743703/)). Presents either as childhood learning difficulty or as progressive cognitive decline/dementia in later life.
- Specific deficits documented: severe short-term memory impairment, emotional lability, childish behavior, reduced verbal fluency, and attention deficits indicative of executive dysfunction ([GeneReviews NBK1210](https://www.ncbi.nlm.nih.gov/books/NBK1210/)).
- HPO suggestions: HP:0001249 (Intellectual disability), HP:0002354 (Memory impairment), HP:0000737 (Irritability/emotional lability), HP:0000708 (Behavioral abnormality), HP:0002088 (Abnormal executive function — via broader cognitive term sets).
- A neuropsychology/MRI correlation study of 16 SPG11 patients found reaction times correlated significantly with disease progression, with long-term follow-up testing in a subset of 7 patients ([PMC9336101](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9336101/)).

### Peripheral Neuropathy

- Axonal sensorimotor peripheral neuropathy reported in **>80%** of individuals (GeneReviews). It commonly emerges **later** in the disease course, distinct from the early cognitive/spastic features, and can progress to a pure motor neuropathy or ALS5-like/CMT2X-like presentation in some patients.
- HPO term: HP:0009830 (Peripheral neuropathy), HP:0007002 (Axonal loss).

### Ophthalmologic/Retinal Phenotype (Kjellin Syndrome)

- Central retinal degeneration with bilateral retinal flecks (resembling Stargardt disease/fundus flavimaculatus) constitutes the eponymous "Kjellin syndrome" subtype ([PMID:19194956](https://pubmed.ncbi.nlm.nih.gov/19194956/); [PMID:21035867](https://pubmed.ncbi.nlm.nih.gov/21035867/)). Notably, retinal changes are typically only observed **once paraplegia has become apparent**, and may be clinically silent, requiring dedicated fundus examination and OCT/electroretinography for detection (case example in late-onset diagnosis: [PMID:38613257](https://pubmed.ncbi.nlm.nih.gov/38613257/)).
- HPO terms: HP:0000546 (Retinal degeneration), HP:0007754 (Macular dystrophy).

### Cerebellar and Movement Disorder Phenotypes

- Cerebellar signs (dysarthria, dysmetria, dysdiadochokinesia, intention tremor, nystagmus, gait ataxia) reported in **over half** of patients ([ScienceDirect overview](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/spg11)).
- A subset present with extrapyramidal features — focal dystonia, tremor, and juvenile/early-onset **parkinsonism** with variable levodopa responsiveness, reported particularly in SPG7 and SPG11 ([PMC10689114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10689114/); case report [SPG11 Presenting with Tremor](https://tremorjournal.org/articles/10.5334/tohm.95)).
- HPO terms: HP:0001251 (Ataxia), HP:0000639 (Nystagmus), HP:0001300 (Parkinsonism), HP:0001337 (Tremor).

### Musculoskeletal

- Pes cavus (HP:0001761) and scoliosis (HP:0002650) reported as less-frequent features.

### Other/Less Frequent

- Seizures/epilepsy: uncommon in SPG11 — a feature that helps distinguish it from some other complex HSP subtypes ([tremorjournal search summary](https://tremorjournal.org/articles/10.5334/tohm.95); [OMIM:618876](https://omim.org/entry/618876) is a distinct, unrelated progressive myoclonic epilepsy entry, not SPG11-specific). HPO: HP:0001250 (Seizure).
- Sphincter/bladder disturbance — urinary urgency, requiring urodynamic evaluation (GeneReviews).

### Age of Onset and Progression Characteristics

- Onset is highly variable: **1–31 years** in most series, rarely as late as **age 60** (GeneReviews). A recent cohort placed mean age of onset at **14.3 years** (range 4–36 years) ([search summary of Orphanet/cohort data](https://www.orpha.net/en/disease/detail/2822)).
- **Progressive** disease course — not episodic or relapsing-remitting. Most patients develop the "complete" complex phenotype within about a decade of first symptoms.
- A recent large case-report/series review compiling **339 SPG11 cases** found: spasticity, hyperreflexia, gait disturbance, cognitive decline, decreased vision, epilepsy, and scoliosis as reported findings, with brain MRI showing thin corpus callosum in 173/190 cases with available imaging data (91%), periventricular white matter changes in 130/158 (82%), and cortical atrophy in 55/107 (51%) ([Frontiers in Neurology, 2023](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2023.1198728/full)).

### Quality of Life

Specific validated QoL instrument data (EQ-5D, SF-36) for SPG11 were not identified in this search; broader HSP QoL literature documents substantial impact on mobility-related and cognitive domains of daily functioning given the combination of progressive lower-limb disability with wheelchair dependence and cognitive decline, but disease-specific quantitative QoL studies for SPG11 were not located and should be flagged as **not established / data-limited** in a KB entry.

---

## 4. Genetic/Molecular Information

### Causal Gene

- **Gene**: *SPG11* (HGNC symbol SPG11; former alias *KIAA1840*)
- **Locus**: chromosome 15q21.1
- **Protein**: spatacsin
- **OMIM gene entry**: 610844 ([OMIM:610844](https://omim.org/entry/610844))
- **OMIM phenotype entry**: 604360, "Spastic Paraplegia 11, Autosomal Recessive" ([OMIM:604360](https://omim.org/entry/604360))

### Pathogenic Variants

- **Variant types**: The mutational spectrum spans nonsense, frameshift (small indels), splice-site, missense, and exon-level/larger genomic deletions or duplications. More than 100 distinct mutations are catalogued.
- **Variant classification (ACMG/AMP)**: The vast majority of disease-causing alleles are classified pathogenic/likely pathogenic in ClinVar on the basis of predicted protein truncation (see ClinVar records, e.g. [RCV000001168](https://www.ncbi.nlm.nih.gov/clinvar/RCV000001168/), c.6100C>T p.Arg2034Ter; [RCV000034200](https://www.ncbi.nlm.nih.gov/clinvar/RCV000034200/), c.2834+1G>T splice variant).
- **Detection rates**: Sequence analysis identifies ~81% of pathogenic alleles; deletion/duplication (copy-number) analysis is needed to identify the remaining ~19% (GeneReviews).
- **Functional consequence**: **Loss of function** — this is the unambiguous, well-established mechanism (truncating variants predominate; missense/splice variants associated with milder, later-onset phenotypes retain partial function).
- **Somatic vs. germline**: Exclusively germline in SPG11-HSP (this is not a cancer-predisposition or somatic-mosaicism-driven disease in its classic presentation).

### Modifier Genes

No validated modifier genes have been established for SPG11 severity or age of onset in the literature surveyed. Genotype (truncating vs. missense/splice) is the main documented modifier of phenotype severity.

### Allelic Disorders (Same Gene, Different Phenotypes)

Biallelic *SPG11* pathogenic variants cause a **spectrum of motor neuron degeneration phenotypes** regardless of variant type, including:
- Pure or complex hereditary spastic paraplegia (classic SPG11)
- Autosomal recessive juvenile-onset **amyotrophic lateral sclerosis type 5 (ALS5)**
- Autosomal recessive **Charcot-Marie-Tooth disease type 2X (CMT2X)**
- An association with multiple sclerosis has also been reported

(Source: [MalaCards/OMIM aggregation](https://www.malacards.org/card/spastic_paraplegia_11_autosomal_recessive); [GeneReviews NBK1210](https://www.ncbi.nlm.nih.gov/books/NBK1210/))

### Epigenetic Information

A 2025 transcriptomic study ("Transcriptomic analysis reinforces the implication of spatacsin in neuroinflammation and neurodevelopment," *Scientific Reports*, [DOI link](https://www.nature.com/articles/s41598-025-86337-9)) reinforces links between spatacsin loss and dysregulated neurodevelopmental and neuroinflammatory transcriptional programs, though this is transcriptomic rather than classical epigenetic (methylation/histone) data specifically.

### Chromosomal Abnormalities

Not typically a large-scale chromosomal disorder; disease-causing lesions are gene-level (point mutations, indels) or exon-level deletions/duplications within *SPG11*, detectable via targeted deletion/duplication (CNV) analysis, exome, or genome sequencing rather than karyotype/FISH.

---

## 5. Environmental Information

- **Environmental factors**: None established as causal or modifying for SPG11 — it is a purely monogenic disease.
- **Lifestyle factors**: No established role; general supportive-care lifestyle measures (physiotherapy, activity maintenance) affect symptom management, not underlying etiology.
- **Infectious agents**: None implicated.

---

## 6. Mechanism / Pathophysiology

### Protein Function and the AP-5 Complex

Spatacsin functions as an accessory protein of **adaptor protein complex 5 (AP-5)**, working together with spastizin (the SPG15 gene product) and the AP-5 core subunit AP5Z1. This AP-5–SPG11–SPG15 complex is implicated in **endosome-to-trans-Golgi-network recycling of the cation-independent mannose-6-phosphate receptor (CI-MPR)**, a receptor essential for delivering lysosomal hydrolases to lysosomes. Loss of SPG11, SPG15, or AP5Z1 causes CI-MPR to accumulate abnormally in early endosomes ([Molecular Biology of the Cell, PMC](https://www.molbiolcell.org/doi/10.1091/mbc.e13-03-0170); [J. Cell Biology, Rag GTPases/PI3P recruitment of AP-5/SPG11/SPG15](https://rupress.org/jcb/article/220/2/e202002075/211690/Rag-GTPases-and-phosphatidylinositol-3-phosphate)).

A 2025 structural biology paper resolved the **structural basis for membrane remodeling by the AP5–SPG11–SPG15 complex** (*Nature Structural & Molecular Biology*, [DOI link](https://www.nature.com/articles/s41594-025-01500-0)), and a 2023 PLOS Biology study showed spatacsin **regulates the directionality of lysosome trafficking by promoting degradation of its partner AP5Z1** — spastizin and AP5Z1 regulate tubular lysosome formation and its anterograde/retrograde trafficking via kinesin KIF13A and dynein/dynactin p150Glued, respectively ([PMID:37871017](https://pubmed.ncbi.nlm.nih.gov/37871017/); [PLOS Biology](https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3002337)).

### Causal Chain: Endolysosomal Dysfunction → Lipid Accumulation → Axonal Degeneration

1. **Trigger**: Biallelic loss-of-function *SPG11* variants → loss of spatacsin protein.
2. **Molecular consequence**: Impaired AP-5-mediated endosomal/lysosomal receptor trafficking; failure of **autophagic lysosome reformation (ALR)** — the process by which lysosomes are recycled from autolysosomes. In *Spg11* knockout mice, autophagic flux studies show diminished lysosome tubulation events in starved knockout MEFs, and lysosome numbers decrease in knockout brain neurons ([PMID:33618608](https://pubmed.ncbi.nlm.nih.gov/33618608/); PLOS Genetics [PMC4540459](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4540459/)).
3. **Cellular consequence**: Lysosomal depletion and impaired autophagic clearance leads to progressive **accumulation of autofluorescent lipofuscin-like material** and lysosomal proteins (LAMP1, p62) within neurons — direct **in vivo evidence for lysosome depletion and impaired autophagic clearance** was demonstrated in *Spg11*-knockout mice ([PLOS Genetics, PMC4540459](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4540459/)).
4. **Lipid handling defect**: Loss of spatacsin function alters **lysosomal lipid clearance**, with accumulation of gangliosides and cholesterol, altering membrane cholesterol levels and disrupting **calcium homeostasis**; this impairs neurite formation and dysregulates **GSK3β signaling** — establishing a mechanistic route from lysosomal dysfunction to structural neuronal damage ([PMID:28237315](https://pubmed.ncbi.nlm.nih.gov/28237315/), "Loss of spatacsin function alters lysosomal lipid clearance leading to upper and lower motor neuron degeneration"; corroborated by GeneReviews mechanistic summary).
5. **Axonal instability**: Independent of lipid/lysosomal pathways, spatacsin loss causes axonal instability via **downregulation of acetylated tubulin** and **reduced anterograde vesicle trafficking**, indicating impaired axonal transport — demonstrated in "Dysfunction of spatacsin leads to axonal pathology in SPG11-linked hereditary spastic paraplegia" ([PMID:24794856](https://pubmed.ncbi.nlm.nih.gov/24794856/); [PMC4140466](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4140466/)).
6. **Mitochondrial involvement**: Axon-specific mitochondrial pathology has been documented in SPG11 alpha motor neurons ("Axon-Specific Mitochondrial Pathology in SPG11 Alpha Motor Neurons," [Frontiers in Neuroscience](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.680572/full)), suggesting a convergent axonal energy-metabolism deficit contributing to distal axonopathy.
7. **Neurodevelopmental component**: A 2020 *Brain* review, "Janus-faced spatacsin (SPG11): involvement in neurodevelopment and multisystem neurodegeneration" ([Oxford Academic](https://academic.oup.com/brain/article/143/8/2369/5827584)), frames spatacsin as having a dual role — contributing to normal neurodevelopment as well as being required to prevent neurodegeneration, potentially explaining the combination of static (cognitive/structural, e.g., thin corpus callosum) and progressive (spasticity, neuropathy) features. A 2025 transcriptomic study reinforces this dual neuroinflammatory/neurodevelopmental signature ([Scientific Reports](https://www.nature.com/articles/s41598-025-86337-9)).
8. **Final common pathway / clinical manifestation**: Progressive degeneration of the **long corticospinal tract axons** (upper motor neuron), together with **lower motor neuron and peripheral axon degeneration**, and **cortical/cerebellar neuron loss** (including Purkinje cell loss, seen in mouse models), produces the combined spastic paraparesis, cognitive decline, cerebellar, and peripheral neuropathy phenotype.

### Suggested Ontology Terms for Pathophysiology Nodes

- **GO Biological Process**: GO:0016240 (autophagosome membrane docking)/GO:0000045 (autophagosome assembly); GO:0007032 (endosome organization); GO:0016082 (synaptic vesicle priming — for anterograde transport); a general "axonal transport" GO term (GO:0008088, axo-dendritic transport); GO:0032418 (lysosome localization).
- **GO Cellular Component**: GO:0005764 (lysosome); GO:0005768 (endosome); GO:0030425 (dendrite)/GO:0030424 (axon).
- **CL (cell type)**: CL:0000030 (glutamatergic upper motor/pyramidal corticospinal neuron), CL:0000100 (motor neuron), CL:0000121 (Purkinje cell — per mouse model loss), CL:0002573 (Schwann cell — peripheral neuropathy arm).
- **CHEBI**: CHEBI:16113 (cholesterol), CHEBI:24404 (ganglioside class) — for the lipid-accumulation arm.

### Molecular Profiling / Omics

- **Transcriptomics**: 2025 *Scientific Reports* transcriptomic analysis in SPG11 models supports neuroinflammatory and neurodevelopmental gene expression signatures ([Scientific Reports](https://www.nature.com/articles/s41598-025-86337-9)).
- **iPSC-based cellular models**: SPG11-patient-derived iPSC cortical neurons (and a CRISPR-Cas9-generated SPG11 knockout line) show **shorter, less complex neurites** than controls, membrane-bound structures within neuronal processes, and impaired organelle transport/lack of synaptic vesicle movement — used as a drug-screening platform ("Tideglusib Rescues Neurite Pathology of SPG11 iPSC Derived Cortical Neurons," [PMC6291617](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6291617/)), where the GSK3β inhibitor **tideglusib** reversed neurite defects — directly connecting the GSK3β-signaling mechanistic node to a candidate small-molecule intervention.

### Single-Cell / Spatial / Multi-omics

Dedicated single-cell or spatial transcriptomic datasets specific to SPG11 patient tissue were not identified in this search — model-system (mouse, zebrafish, iPSC) transcriptomic/proteomic data are the primary molecular-profiling resources currently available.

---

## 7. Anatomical Structures Affected

### Organ/System Level
- **Primary**: Central nervous system — corticospinal tracts (long motor axons), cerebral cortex, corpus callosum, cerebellum, brainstem, basal ganglia, retina.
- **Secondary**: Peripheral nervous system (peripheral nerves — axonal sensorimotor neuropathy); musculoskeletal system (secondary contractures, scoliosis, pes cavus from chronic spasticity); genitourinary system (neurogenic bladder/sphincter disturbance).
- **Body systems involved**: Nervous system (primary), musculoskeletal, sensory (visual), genitourinary.

### Tissue/Cell Level
- Upper motor neurons of the corticospinal tract (long-axon pyramidal neurons)
- Lower motor neurons (in ALS5-like/motor-neuropathy presentations)
- Peripheral (sensory and motor) axons — axonal, not primarily demyelinating, neuropathy
- Cerebellar Purkinje cells (documented loss in mouse models — [PMID:33618608](https://pubmed.ncbi.nlm.nih.gov/33618608/))
- Cortical neurons
- Retinal pigment epithelium/photoreceptors (macular dystrophy in Kjellin syndrome)

Suggested UBERON terms: UBERON:0002240 (spinal cord), UBERON:0002298 (brainstem), UBERON:0002037 (cerebellum), UBERON:0002336 (corpus callosum), UBERON:0000966 (retina), UBERON:0001017 (central nervous system), UBERON:0000010 (peripheral nervous system).

### Subcellular Level
- Lysosomes/autolysosomes (GO:0005764)
- Endosomes (GO:0005768)
- Axonal cytoskeleton (microtubules — acetylated tubulin pool)
- Mitochondria (axon-specific mitochondrial pathology)

### Localization/Lateralization
Bilateral/symmetric involvement; corpus callosum thinning is diffuse but classically most pronounced at the **rostral body/anterior midbody**.

---

## 8. Temporal Development

### Onset
- Typical onset: **infancy through adolescence**, range **1–31 years**, rarely up to age 60 (GeneReviews).
- Mean age of onset reported as **14.3 years** (range 4–36) in one cohort ([search summary, Orphanet/cohort data](https://www.orpha.net/en/disease/detail/2822)).
- Onset pattern: insidious, gradually progressive — not acute or episodic.

### Progression
- Chronic, **progressive** disease course (not relapsing-remitting).
- Most patients develop the "complete" complex phenotype within roughly a decade of first symptoms.
- **Wheelchair dependence** typically develops **1–2 decades after onset** (GeneReviews).
- Cognitive decline and motor neuropathy tend to manifest and progress **later** in the disease course relative to the initial spasticity/cognitive-learning-difficulty presentation.
- Retinal changes (Kjellin phenotype) generally appear **after** paraplegia is established, not as a presenting sign.

### Patterns
- No spontaneous remission is described; this is a monotonically progressive neurodegenerative disorder.
- No clearly defined "critical therapeutic window" has been established in the literature, though earlier diagnosis/intervention with symptomatic and rehabilitative therapy is generally advocated.

---

## 9. Inheritance and Population

### Epidemiology
- **Overall HSP prevalence**: highly variable by geography, ranging from ~1/11,000 to 1/77,000 in Europe; broader estimates of 1–10 per 100,000 depending on region ([Orphanet](https://www.orpha.net/en/disease/detail/2822); GeneReviews).
- **SPG11-specific incidence**: **0.35 per 100,000 people**, accounting for 19–31% of autosomal recessive HSP ([Frontiers in Neurology 2023](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.680572/full) cohort summary).
- **Calculated SPG11 prevalence**: GeneReviews estimates approximately **1.25 per 100,000** by applying the 19–31% AR-HSP fraction to overall AR-HSP prevalence figures ([NBK1210](https://www.ncbi.nlm.nih.gov/books/NBK1210/)).
- A formal integrated epidemiological modeling study specifically estimated global incidence/prevalence for **SPG4, SPG7, SPG11, and SPG15** ([PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)) — useful for cross-referencing model-based prevalence estimates against the simpler fraction-based GeneReviews estimate.

### Inheritance Pattern
- **Autosomal recessive.**
- **Recurrence risk**: each sibling of an affected individual has a 25% chance of being affected, 50% chance of being an unaffected carrier, 25% chance of being unaffected/non-carrier (GeneReviews).
- **Penetrance**: full/complete penetrance is assumed for biallelic loss-of-function genotypes, though expressivity (age of onset, symptom severity/spectrum) is markedly variable.
- **Parental carriers**: typically asymptomatic, although abnormal ocular findings have occasionally been reported in heterozygous carriers (GeneReviews).
- **Genetic anticipation**: not a described feature (this is not a repeat-expansion disorder).
- **Germline mosaicism**: not specifically documented in the literature surveyed, though theoretically possible for recessive disorders generally.
- **Founder effects**: Present in specific populations given the Mediterranean/Middle Eastern consanguinity-associated founding cohorts, though *SPG11* mutations are broadly heterogeneous worldwide.
- **Consanguinity**: A significant contributing factor historically, as most original description families were consanguineous; disease is nonetheless reported in outbred populations globally.
- **Carrier frequency**: Not explicitly reported as a population-wide statistic in the sources surveyed; can be estimated from the calculated disease prevalence (~1.25/100,000) under Hardy-Weinberg assumptions, but no direct gnomAD-based carrier-frequency figure was retrieved in this search.

### Population Demographics
- No strong evidence of ethnic-specific enrichment beyond the historical consanguinity-associated founder families (Mediterranean, Middle Eastern, North African); cases are now documented worldwide.
- Sex ratio: no sex predilection is described; autosomal recessive inheritance implies equal male:female risk.
- Age distribution of affected individuals spans childhood through adulthood given the wide onset range.

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- Routine bloodwork is generally unremarkable; no specific validated circulating biomarker exists.
- **Electrophysiology**: Nerve conduction studies/EMG to document axonal peripheral neuropathy; visual evoked potentials (VEP) and somatosensory evoked potentials (SEP) recommended annually for surveillance (GeneReviews).

### Imaging (Key Diagnostic Modality)
Brain MRI is central to diagnosis and shows a highly characteristic pattern:
- **Thin corpus callosum** — present in >90% of individuals (GeneReviews); confirmed at 173/190 (91%) in a large 339-case review ([Frontiers in Neurology 2023](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2023.1198728/full)).
- **"Ear of the lynx" sign**: hyperintense on FLAIR, hypointense on T1, in the periatrial/periventricular white matter — a highly characteristic (though not fully specific) neuroimaging sign.
- **Periventricular/confluent white matter hyperintensities** — 130/158 (82%) in the same cohort.
- **Cortical atrophy** — 55/107 (51%).
- Brainstem and cerebellar atrophy also documented; basal ganglia abnormalities have also been reported ("SPG11 mutations cause widespread white matter and basal ganglia abnormalities, but restricted cortical damage," [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2213158218301773)).

### Genetic Testing
- **First-tier**: Single-gene sequence analysis of *SPG11*, followed by deletion/duplication (CNV) analysis if only one or zero variants are found (since ~10–20% of pathogenic alleles are structural). Alternatively, a multi-gene HSP panel.
- **Comprehensive**: Exome or genome sequencing when the phenotype does not clearly distinguish SPG11 from other complex AR-HSPs (notably SPG15, which is clinically indistinguishable — "No clinical features discriminate between SPG11 & SPG15," per GeneReviews).
- **Detection sensitivity**: sequence analysis ~81%, deletion/duplication analysis ~19% of remaining pathogenic alleles (GeneReviews).

### Differential Diagnosis
Key alternative/overlapping diagnoses per GeneReviews:
- **SPG15** (clinically indistinguishable from SPG11 without genetic testing)
- **SPG21** (Mast syndrome)
- **SPG46, SPG47–SPG52** and other complex AR-HSPs with thin corpus callosum
- **ALS** — when lower motor neuron/muscle wasting predominates
- Other leukodystrophies/leukoencephalopathies with white matter change and callosal thinning

### Clinical Criteria
No formal consensus diagnostic-criteria scoring system (e.g., DSM/ICD-style) exists specifically for SPG11; diagnosis rests on the combination of clinical phenotype + characteristic MRI + confirmatory biallelic molecular genetic testing, per GeneReviews consensus recommendations.

### Screening
No newborn screening or population carrier-screening program specifically targets *SPG11*; carrier testing and prenatal/preimplantation genetic testing are offered on a family-specific basis once the familial pathogenic variants are identified (GeneReviews).

---

## 11. Outcome/Prognosis

- **Life expectancy**: Specific quantitative life-expectancy/mortality data were not identified in this search; SPG11 is generally understood as a disabling but not directly life-shortening disease in most reported cohorts (unlike ALS5 presentations, where motor neuron disease severity may carry different prognostic implications).
- **Functional outcome**: Most patients become **wheelchair-dependent within 1–2 decades of symptom onset** (GeneReviews) — the single most quantified functional/disability outcome in the literature.
- **Cognitive trajectory**: Progressive decline is typical, with a neuropsychology/MRI correlation study showing reaction-time performance correlating with disease progression on longitudinal follow-up ([PMC9336101](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9336101/)).
- **Complications**: Secondary musculoskeletal complications (contractures, scoliosis) from chronic spasticity if inadequately managed; urinary tract infection risk from neurogenic bladder dysfunction if unmonitored; visual impairment from progressive macular dystrophy in Kjellin-syndrome presentations.
- **Prognostic factors**: Genotype (truncating vs. missense/splice variant) correlates with severity/age of onset — missense/splice variants associate with milder, later-onset disease (GeneReviews).
- A dedicated **natural history / biomarker study** ("Biological course and natural history of hereditary spastic paraplegia type 11 (SPG11)," [MDS Abstracts](https://www.mdsabstracts.org/abstract/biological-course-and-natural-history-of-hereditary-spastic-paraplegia-type-11-spg11/)) is explicitly working to establish quantitative biological markers of disease course as a basis for upcoming therapeutic trials — indicating that robust natural-history/prognostic data are still an active area of development rather than fully established.

---

## 12. Treatment

**No disease-modifying or curative treatment currently exists for SPG11.** Management is entirely symptomatic and supportive (GeneReviews):

### Pharmacotherapy (Symptomatic)
- **Spasticity**: oral antispastic agents — **baclofen**, **tizanidine**; **botulinum toxin** injections and **intrathecal baclofen** for severe, treatment-refractory spasticity.
  - Suggested NCIT term: NCIT:C15986 (Pharmacotherapy), with `therapeutic_agent` bound to CHEBI (e.g., baclofen CHEBI:2854, tizanidine).
- **Bladder dysfunction**: anticholinergic medications for urinary urgency, guided by urodynamic evaluation.
- **Psychiatric manifestations**: standard psychiatric/psychopharmacologic management per presentation.

### Rehabilitative/Supportive Care
- **Physiotherapy** for muscle stretching and contracture prevention (NCIT:C15302, Physical Therapy).
- Multidisciplinary coordination among neurology, clinical genetics, physiotherapy, social work, and psychology (GeneReviews).

### Investigational / Emerging Approaches
- **Venglustat** (a glucosylceramide synthase inhibitor) is being investigated as a candidate to slow SPG11 progression, in a research program launched **March 2025** by Euro-HSP and Life4HSP, based at the Paris Brain Institute under Dr. Frédéric Darios ([life4hsp.com](https://life4hsp.com/en/research-to-treatment-for-spg11-started/)). This targets the lysosomal ganglioside/lipid-accumulation mechanistic arm described in §6.
- **Tideglusib** (a GSK3β inhibitor) rescued neurite pathology in SPG11-patient iPSC-derived cortical neurons in a preclinical study, directly implicating the GSK3β-signaling node as a druggable target ([PMC6291617](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6291617/)).
- No SPG11-specific gene therapy trial (viral-vector gene replacement or gene editing) has yet reached clinical testing as of this search (August 2026); gene therapy for HSP overall is at an early stage, exemplified by an unrelated single-patient AAV gene-therapy trial for **SPG50** (*Nature Medicine*, 2024, [DOI link](https://www.nature.com/articles/s41591-024-03078-4)) — illustrating the platform/precedent but not yet a SPG11-specific program.
- A 2026 review, "Hereditary spastic paraplegia: from decades of therapy to future innovations" ([SAGE Journals](https://journals.sagepub.com/doi/10.1177/17562864251406589)), frames drug repurposing and early gene-based interventions as the field's emerging disease-modifying strategy for ultra-rare HSP subtypes including SPG11.
- Nutritional/dietary intervention: A 2025/2026 scoping review noted **no dietary intervention trials have specifically been conducted for SPG11** to date ("Nutritional Approaches in Neurodegenerative Disorders," [PMC12609518](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12609518/)).

### Treatment Outcomes
No randomized controlled trial efficacy data exist yet for any disease-modifying SPG11 therapy; symptomatic-treatment response data (spasticity agents, botulinum toxin, intrathecal baclofen) follow general HSP/spasticity management evidence rather than SPG11-specific trials.

---

## 13. Prevention

- **Primary prevention**: Not applicable in the traditional sense (no modifiable environmental cause); the relevant "primary prevention" for SPG11 is reproductive — **genetic counseling** for at-risk couples/families, ideally initiated **before pregnancy**, covering recurrence risk (25% per pregnancy for two carrier parents) and reproductive options including prenatal testing and preimplantation genetic testing (GeneReviews).
- **Secondary prevention**: Not a screening-amenable disease at the population level (no newborn or population screening program exists); cascade **carrier testing** within families once a pathogenic variant is identified is standard practice.
- **Tertiary prevention** (preventing complications in affected individuals): regular physiotherapy to prevent contractures; sphincter-function monitoring to prevent urinary tract infections; scheduled surveillance imaging and electrophysiology to track progression and adjust management (GeneReviews surveillance schedule):
  - Specialized clinic evaluation every **6 months**
  - Annual **brain MRI** (corpus callosum, cerebellar/brainstem atrophy, white matter change)
  - Annual **electrophysiologic studies** (EMG, VEP, SEP)
  - Annual **visual acuity assessment** (given the retinal/macular degeneration risk)
- **Genetic counseling** resources: SPATAX Network, EURO HSP, Spastic Paraplegia Foundation, NINDS HSP information page (GeneReviews resource list).

---

## 14. Other Species / Natural Disease

No naturally occurring SPG11 disease has been documented in non-human species (companion animals, livestock, or wildlife) in the literature surveyed — this is a human-specific Mendelian condition without a known veterinary/OMIA counterpart identified in this search. All non-human data derive from **engineered/induced models** (see §15) rather than naturally occurring animal disease.

---

## 15. Model Organisms

### Mouse Models
- **Spg11 knockout mice** are the best-characterized model. They develop:
  - Progressive **motor impairment**, correlating with accumulation of autofluorescent (lipofuscin-like) material in neurons and progressive neuron loss ([PMID:33618608](https://pubmed.ncbi.nlm.nih.gov/33618608/)).
  - **Axonal degeneration of cortical motor neurons** ([source aggregation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4140466/)).
  - **Loss of cortical neurons and Purkinje cells.**
  - **In vivo evidence of lysosome depletion and impaired autophagic clearance** — degenerating neurons accumulate LAMP1+/p62+ autolysosome-derived material over time due to a defect in **autophagic lysosome reformation (ALR)**, i.e., reduced recycling of lysosomes from autolysosomes ([PLOS Genetics, PMC4540459](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4540459/)).
  - Compound *Spg11*/*Zfyve26* (SPG15) knockout mice show even more compromised ALR, underscoring the shared AP-5-complex mechanism ("Mouse models for hereditary spastic paraplegia uncover a role of PI4K2A in autophagic lysosome reformation," [PMID:33618608](https://pubmed.ncbi.nlm.nih.gov/33618608/); [PMC8632344](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8632344/)).
  - Fidelity: **High** for the axonal/lysosomal degeneration mechanism and motor phenotype; the mouse model recapitulates progressive upper-motor-neuron axonal pathology and lysosomal dysfunction well, though it does not fully model the human cognitive/intellectual-disability phenotype or the retinal (Kjellin) phenotype.

### Zebrafish Models
- Depletion of spatacsin in zebrafish **impairs motor neuron development**, supporting a role for spatacsin in motor neuron differentiation/maintenance and offering a tractable in vivo system for mechanistic and (potentially) drug-screening studies of SPG11-related motor neuropathy (search-aggregated summary).

### Cellular / iPSC Models
- **Patient-derived iPSC cortical neurons** (plus a CRISPR-Cas9-engineered *SPG11* knockout isogenic control line) recapitulate **shortened, less-complex neurites**, abnormal membrane-bound structures within neuronal processes, impaired organelle transport, and reduced synaptic vesicle movement — used successfully as a **drug-screening platform**, identifying the GSK3β inhibitor tideglusib as a rescue compound ([PMC6291617](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6291617/)).
- Broader HSP iPSC-neuron literature (including SPG11 lines) documents impaired neurite outgrowth, increased axonal swellings, and reduced axonal transport as shared, recapitulated disease-specific defects across HSP subtypes modeled by iPSC-derived neurons.

### Model Limitations
- Mouse and zebrafish models capture the **axonal/lysosomal degenerative mechanism** and motor phenotype well but do not fully reproduce the **human cognitive impairment**, **thin corpus callosum**, or **retinal degeneration** components of the complex human phenotype — an important **human-model-mismatch** consideration for any KB entry linking these models to specific pathophysiology nodes.
- No SPG11-specific large-animal (canine, feline, non-human primate) model was identified in this search.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested terms |
|---|---|
| Disease | MONDO (hereditary spastic paraplegia 11, mapped OMIM:604360), OMIM:604360, ORPHA:2822 |
| Gene | HGNC SPG11, hgnc: identifier for spatacsin; also note allelic ALS5/CMT2X phenotype links |
| Core phenotypes (HP) | HP:0007256/HP:0002061 (spastic paraparesis), HP:0001249 (intellectual disability), HP:0009830 (peripheral neuropathy), HP:0000546 (retinal degeneration), HP:0001251 (ataxia), HP:0001300 (parkinsonism), HP:0002088/related (thin corpus callosum via imaging term), HP:0002650 (scoliosis), HP:0001761 (pes cavus) |
| Biological process (GO) | Autophagy/autophagosome assembly, endosome organization, lysosome organization, axonal transport |
| Cellular component (GO) | Lysosome, endosome, axon |
| Cell types (CL) | Upper motor (corticospinal/pyramidal) neuron, Purkinje cell, peripheral sensory/motor axon-associated cell types |
| Anatomy (UBERON) | Spinal cord, corpus callosum, cerebellum, retina, peripheral nervous system |
| Chemicals (CHEBI) | Cholesterol, ganglioside class (lipid-accumulation mechanism); baclofen, tizanidine (symptomatic drugs) |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy), NCIT:C15302 (Physical Therapy), NCIT:C15240 (Genetic Counseling) |

---

## Notable Gaps / Data Not Available

- No SPG11-specific validated QoL instrument data (EQ-5D/SF-36) located.
- No formal SPG11-specific mortality/life-expectancy statistics located.
- No naturally occurring veterinary/animal disease counterpart identified.
- No population-level carrier-frequency (gnomAD-derived) figure was retrieved in this search.
- No SPG11-specific gene therapy clinical trial yet registered as of August 2026; venglustat (drug-repurposing, small-molecule) is the most advanced disease-modifying investigational approach identified.

---

## Sources

- [Spastic Paraplegia 11 — GeneReviews®, NCBI Bookshelf (NBK1210)](https://www.ncbi.nlm.nih.gov/books/NBK1210/)
- [OMIM 604360 — Spastic Paraplegia 11, Autosomal Recessive](https://omim.org/entry/604360)
- [OMIM 610844 — SPG11 Vesicle Trafficking Associated, Spatacsin](https://omim.org/entry/610844)
- [Orphanet: Autosomal recessive spastic paraplegia type 11 (ORPHA:2822)](https://www.orpha.net/en/disease/detail/2822)
- [GARD — Hereditary spastic paraplegia 11](https://rarediseases.info.nih.gov/diseases/4919/hereditary-spastic-paraplegia-11)
- [NORD — hereditary spastic paraplegia 11 (MONDO)](https://rarediseases.org/mondo-disease/hereditary-spastic-paraplegia-11/)
- [Stevanin et al. 2007, Nature Genetics — Mutations in SPG11, encoding spatacsin](https://www.nature.com/articles/ng1980)
- [Hereditary spastic paraplegia with thin corpus callosum and SPG11 mutation: neuropathological evaluation, PMC12005084](https://pmc.ncbi.nlm.nih.gov/articles/PMC12005084/) / [PubMed 39391989](https://pubmed.ncbi.nlm.nih.gov/39391989/)
- [Dysfunction of spatacsin leads to axonal pathology (PMID 24794856 / PMC4140466)](https://pubmed.ncbi.nlm.nih.gov/24794856/)
- [Clinical analysis in patients with SPG11 HSP, Frontiers in Neurology 2023](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2023.1198728/full)
- [Hereditary Spastic Paraplegia Type 11 — Clinical, Genetic, and Neuroimaging Characteristics, PMC10743703](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743703/)
- [Neuropsychology and MRI correlates of neurodegeneration in SPG11, PMC9336101](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9336101/)
- [SPG11 mutations cause widespread white matter and basal ganglia abnormalities, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2213158218301773)
- [Biological course and natural history of SPG11, MDS Abstracts](https://www.mdsabstracts.org/abstract/biological-course-and-natural-history-of-hereditary-spastic-paraplegia-type-11-spg11/)
- [Mouse models for HSP uncover PI4K2A role in autophagic lysosome reformation, PMID 33618608 / PMC8632344](https://pubmed.ncbi.nlm.nih.gov/33618608/)
- [In Vivo Evidence for Lysosome Depletion and Impaired Autophagic Clearance in SPG11, PLOS Genetics / PMC4540459](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4540459/)
- [Loss of spatacsin function alters lysosomal lipid clearance, PMID 28237315](https://pubmed.ncbi.nlm.nih.gov/28237315/)
- [SPG11 mutations cause Kjellin syndrome, PMID 19194956](https://pubmed.ncbi.nlm.nih.gov/19194956/)
- [Kjellin syndrome long-term neuro-ophthalmologic follow-up, PMID 21035867](https://pubmed.ncbi.nlm.nih.gov/21035867/)
- [Late-onset Kjellin syndrome diagnosed on fundus exam, PMID 38613257](https://pubmed.ncbi.nlm.nih.gov/38613257/)
- [Janus-faced spatacsin (SPG11): neurodevelopment and multisystem neurodegeneration, Brain 2020](https://academic.oup.com/brain/article/143/8/2369/5827584)
- [Spatacsin regulates directionality of lysosome trafficking via AP5Z1 degradation, PMID 37871017 / PLOS Biology](https://pubmed.ncbi.nlm.nih.gov/37871017/)
- [Interaction between AP-5 and SPG11/SPG15, Molecular Biology of the Cell](https://www.molbiolcell.org/doi/10.1091/mbc.e13-03-0170)
- [Structural basis for membrane remodeling by the AP5–SPG11–SPG15 complex, Nature Structural & Molecular Biology 2025](https://www.nature.com/articles/s41594-025-01500-0)
- [Rag GTPases and PI3P mediate recruitment of AP-5/SPG11/SPG15, J. Cell Biology](https://rupress.org/jcb/article/220/2/e202002075/211690/Rag-GTPases-and-phosphatidylinositol-3-phosphate)
- [Transcriptomic analysis reinforces spatacsin's role in neuroinflammation/neurodevelopment, Scientific Reports 2025](https://www.nature.com/articles/s41598-025-86337-9)
- [Tideglusib Rescues Neurite Pathology of SPG11 iPSC-Derived Cortical Neurons, PMC6291617](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6291617/)
- [Axon-Specific Mitochondrial Pathology in SPG11 Alpha Motor Neurons, Frontiers in Neuroscience](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.680572/full)
- [Movement disorders in hereditary spastic paraplegias, PMC10689114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10689114/)
- [SPG11 Presenting with Tremor, Tremor and Other Hyperkinetic Movements](https://tremorjournal.org/articles/10.5334/tohm.95)
- [Integrated modelling of global incidence/prevalence for SPG4, SPG7, SPG11, SPG15, PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)
- [Hereditary spastic paraplegia: from decades of therapy to future innovations, SAGE 2026](https://journals.sagepub.com/doi/10.1177/17562864251406589)
- [Life4HSP — SPG11 venglustat research project launch](https://life4hsp.com/en/research-to-treatment-for-spg11-started/)
- [AAV gene therapy for HSP type 50: phase 1 single-patient trial, Nature Medicine 2024](https://www.nature.com/articles/s41591-024-03078-4)
- [Nutritional Approaches in Neurodegenerative Disorders — SPG11 scoping review, PMC12609518](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12609518/)
- [SPG11 — an overview, ScienceDirect Topics](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/spg11)
- [ClinVar RCV000001168 — SPG11 c.6100C>T (p.Arg2034Ter)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000001168/)
- [ClinVar RCV000034200 — SPG11 c.2834+1G>T splice variant](https://www.ncbi.nlm.nih.gov/clinvar/RCV000034200/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 16 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 4 |
| References weighed for topical relevance | 8 |
| On topic | 7 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMC:PMC4140466`: "Dysfunction of spatacsin leads to axonal pathology in SPG11-linked hereditary spastic paraplegia"
  - The PMC ID service was unreachable, so the quote was not checked
- `PMC:PMC6291617`: "Tideglusib Rescues Neurite Pathology of SPG11 iPSC Derived Cortical Neurons,"
  - The PMC ID service was unreachable, so the quote was not checked
- `DOI:10.1177/17562864251406589`: "Hereditary spastic paraplegia: from decades of therapy to future innovations"
  - Reference was skipped, so the quote was not checked
- `PMC:PMC12609518`: "Nutritional Approaches in Neurodegenerative Disorders,"
  - The PMC ID service was unreachable, so the quote was not checked

8 of 24 references resolved; the rest could not be looked up either way.
