---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-05T14:36:28.854136'
end_time: '2026-08-05T14:53:05.640833'
duration_seconds: 996.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hemimegalencephaly
  mondo_id: ''
  category: Somatic mosaic
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
  web_search_requests: 16
  num_turns: 69
  total_cost_usd: 5.829088
  session_id: 06ce006c-c244-453c-92ab-5cb38c9d545f
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemimegalencephaly
- **MONDO ID:**  (if available)
- **Category:** Somatic mosaic

## Research Objectives

Please provide a comprehensive research report on **Hemimegalencephaly** covering all of the
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

# Hemimegalencephaly (HME) — Comprehensive Disease Characteristics Research Report

**Prepared:** 2026-08-05 · **Target MONDO:** `MONDO:0020492` · **Category:** somatic mosaic / malformation of cortical development

**A note on evidence provenance before anything else.** Where I quote below, I flag each quote as either **[verbatim-verified]** (I have the full abstract or full text in hand, either from this repo's `references_cache/` or from a raw PubMed E-utilities fetch) or **[secondhand — RE-VERIFY]** (the quoted fragment came back through a summarizing fetch layer and has *not* been checked character-for-character against the real abstract). Anything in the second bucket must be run through `just fetch-reference PMID:X` and `just validate-references` before it is allowed anywhere near an evidence `snippet:`. Treating a summarizer's paraphrase as a quote is exactly the failure mode the dismech SOP exists to catch.

---

## 1. Disease Information

### Overview

Hemimegalencephaly is a congenital, non-progressive-in-substrate but clinically devastating malformation of cortical development in which all or part of **one** cerebral hemisphere overgrows and is simultaneously *mis-built*. Think of it less as "one side got extra fertilizer" and more as a developmental program that lost its stop codon in one clone of progenitor cells: the affected hemisphere is bigger, but its cortex is thick, poorly layered, populated by grotesquely enlarged cells, and profoundly epileptogenic. The overgrowth and the dysplasia are two faces of one lesion, not two lesions.

The clinical triad that follows is near-obligate: **drug-resistant epilepsy beginning in the newborn period or early infancy, contralateral hemiparesis, and global developmental delay.**

> "Hemimegalencephaly (HME) is a rare diffuse malformation of cortical development characterized by unihemispheric hypertrophy, drug-resistant epilepsy (DRE), hemiparesis, and developmental delay." — Goel et al., *Neurosurgery* 2024, **PMID:37975663** **[verbatim-verified]**

> "Hemimegalencephaly (HMG) is a developmental brain disorder characterized by an enlarged, malformed cerebral hemisphere, typically causing epilepsy that requires surgical resection." — Poduri et al., *Neuron* 2012, **PMID:22500628** **[verbatim-verified via raw efetch]**

The MONDO definition (inherited from Orphanet) is the fullest single-sentence statement available:

> "Hemimegalencephaly is a rare cerebral malformation characterized by overgrowth of all or part of a cerebral hemisphere, often with ipsilateral severe cortical dysplasia or dysgenesis, white matter hypertrophy and dilated lateral ventricle, presenting in early infancy with progressive hemiparesis, severe psychomotor retardation and intractable seizures." — MONDO:0020492 `def`, sourced to `Orphanet:99802` **[verbatim-verified from local `sqlite:obo:mondo`]**

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0020492` | label `hemimegalencephaly`; `is_a MONDO:0100283` (overgrowth syndrome and/or cerebral malformations due to abnormalities in MTOR pathway genes) — this parent is a gift for dismech, it encodes the mechanism in the taxonomy |
| **Orphanet** | `ORPHA:99802` | source of the MONDO definition; citable directly as `ORPHA:99802` via the repo's structured-source cache |
| **HPO (as a phenotype)** | `HP:0007206` "Hemimegalencephaly", def. "Enlargement of all or parts of one cerebral hemisphere." `is_a HP:0001355` Megalencephaly **[verbatim-verified from local `sqlite:obo:hp`]** |
| **MeSH** | `D065705` | |
| **ICD-9** | `742.4` | |
| **ICD-11 (foundation)** | `961229160` | no distinct linearization stem code; usually coded under malformations of the brain |
| **SNOMED CT** | `253170008` | |
| **UMLS** | `C0431391` | |
| **MedGen** | `140910` | |
| **GARD** | `0002637` | |
| **NORD** | `1220` | |
| **NCIt** | MONDO xrefs `NCIT:C177779` — **⚠️ this xref appears wrong.** Querying `sqlite:obo:ncit` returns `NCIT:C177779 = "MCAP Syndrome"` (Megalencephaly-Capillary Malformation, `is_a NCIT:C178285 PROS Syndrome`), which is a *different* entity — a PIK3CA-related overgrowth syndrome, not hemimegalencephaly. Do not propagate this xref into a dismech `mappings:` block without re-checking against live NCIt; consider filing upstream. |

### Synonyms and alternative names

- **unilateral megalencephaly** (EXACT, per Orphanet and ICD-11 foundation)
- **macrencephaly** (RELATED, per GARD — imprecise, avoid)
- **HME**, **HMG**, **HMEG** (literature abbreviations; note the older literature uses HMG, which now collides badly with the HMG-CoA gene family — prefer **HME**)
- **hemimegalencephaly variant of epidermal nevus syndrome** (for the syndromic form)
- Historical: "unilateral hemispheric dysplasia"; first described by **Sims in 1835** (per D'Gama & Poduri, PMID:34608615 **[verbatim-verified from full text in cache]**: "Hemimegalencephaly (HME), first reported by Sims in 1835, is a rare MCD characterized by abnormal enlargement of a cerebral hemisphere")

### Nature of the evidence base

Overwhelmingly **aggregated, small-N, surgical-series derived**. There is no HME registry. Nearly everything mechanistic comes from **resected brain tissue obtained at hemispherectomy** — a peculiar and important epistemic fact: HME is one of the very few brain malformations where the diseased organ is routinely removed and handed to a molecular biologist. The 2012 landmark paper says the quiet part out loud:

> "The intractable epilepsy that is associated with HME can be relieved by the surgical treatment hemispherectomy, allowing sampling of diseased tissue." — Lee et al., *Nat Genet* 2012, **PMID:22729223** **[verbatim-verified from cache]**

Consequence for curation: **the entire genetic literature is ascertainment-biased toward severe, surgical HME.** Mild or non-operated HME is essentially unsampled molecularly. Flag this as a knowledge gap.

---

## 2. Etiology

### 2.1 Primary cause — postzygotic somatic activation of PI3K–AKT–mTOR

HME is, in the modern framing, a **mosaic mTORopathy**. A single postzygotic mutation in a dorsal telencephalic progenitor cell, occurring after gastrulation (often after neurulation), constitutively switches on mTORC1 in that cell's entire clonal descent. That clone builds a hemisphere that is too big and wired wrong.

The three landmark 2012 papers established this in the same year:

**(a) Poduri et al., *Neuron* 2012 (PMID:22500628)** — copy-number and point-mutation evidence:
> "We found that two out of eight HMG samples showed trisomy of chromosome 1q, which encompasses many genes, including AKT3, a gene known to regulate brain size. A third case showed a known activating mutation in AKT3 (c.49G→A, creating p.E17K) that was not present in the patient's blood cells." **[verbatim-verified]**
> "Our data suggest that somatic mutations limited to the brain could represent an important cause of complex neurogenetic disease." **[verbatim-verified]**

**(b) Lee et al., *Nat Genet* 2012 (PMID:22729223)** — exome sequencing of paired brain–blood:
> "Exome sequencing and mass spectrometry analysis in paired brain-blood samples from individuals with HME (n = 20 cases) identified de novo somatic mutations in 30% of affected individuals in the PIK3CA, AKT3 and MTOR genes. A recurrent PIK3CA c.1633G>A mutation was found in four separate cases. Identified mutations were present in 8-40% of sequenced alleles in various brain regions and were associated with increased neuronal S6 protein phosphorylation in the brains of affected individuals, indicating aberrant activation of mammalian target of rapamycin (mTOR) signaling. Thus HME is probably a genetically mosaic disease caused by gain of function in phosphatidylinositol 3-kinase (PI3K)-AKT3-mTOR signaling." **[verbatim-verified from cache]**

**(c) Rivière et al., *Nat Genet* 2012 (PMID:22729224)** — the sibling megalencephaly syndromes MCAP and MPPH, establishing `AKT3`/`PIK3R2`/`PIK3CA` as a germline-and-postzygotic continuum. **[secondhand — RE-VERIFY]**

Subsequent cohorts nailed down yield and the two-hit branch:

**D'Gama et al., *Ann Neurol* 2015 (PMID:25599672)** **[verbatim-verified from raw efetch]**:
> "Using targeted and exome sequencing on DNA from resected brain samples and nonbrain samples from 53 patients with FCD or HME, we identified pathogenic germline and mosaic mutations in multiple PI3K/AKT pathway genes in 9 patients, and a likely pathogenic variant in 1 additional patient. Our data confirm the association of DEPDC5 with sporadic FCD but also implicate this gene for the first time in HME."

**D'Gama et al., *Cell Reports* 2017 (PMID:29281825)** — the "continuum" paper, and the single most useful mechanistic citation for a dismech pathograph **[secondhand — RE-VERIFY, though quoted consistently across sources]**:
> "Deep sequencing of these genes in FCD/HME brain tissue identified an etiology in 27 of 66 cases (41%). Radiographically indistinguishable lesions are caused by somatic activating mutations in AKT3, MTOR, and PIK3CA and germline loss-of-function mutations in DEPDC5, NPRL2, and TSC1/2, including TSC2 mutations in isolated HME demonstrating a 'two-hit' model. Mutations in the same gene cause a disease continuum from FCD to HME to bilateral brain overgrowth, reflecting the progenitor cell and developmental time when the mutation occurred."

**Baldassari et al., *Acta Neuropathol* 2019 (PMID:31444548)** — the cleanest yield statistics and the sharpest genotype–histology split **[verbatim-verified from raw efetch]**:
> "We were able to elucidate 29% of mMCD/FCD1 patients and 63% of FCD2/HME patients. Somatic loss-of-function variants in the N-glycosylation pathway-associated SLC35A2 gene were found in mMCD/FCD1 cases. Somatic gain-of-function variants in MTOR and its activators (AKT3, PIK3CA, RHEB), as well as germline, somatic and two-hit loss-of-function variants in its repressors (DEPDC5, TSC1, TSC2) were found exclusively in FCD2/HME cases."
> "Analysis of microdissected cells demonstrated that DNs and BCs carry the pathogenic variants. We further observed a correlation between the density of pathological cells and the variant-detection likelihood."

**Macdonald-Laurs et al., *Brain Commun* 2025 (PMID:39926610)** — most recent large integrated cohort (IESS-with-FMCD, n=59) **[verbatim-verified from raw efetch]**:
> "A genetic diagnosis was achieved in 47 children (80% of cohort)."
> "Somatic mosaicism was a major cause of focal cortical dysplasia type II/hemimegalencephaly (81%) and mild malformation of cortical development with oligodendroglial hyperplasia (100%)."

### 2.2 Risk factors

**Genetic risk factors.**
- *Causal (see §4 for full detail):* somatic gain-of-function in `MTOR`, `PIK3CA`, `AKT3`, `AKT1`, `RHEB`; loss-of-function (germline, somatic, or two-hit) in `TSC1`, `TSC2`, `DEPDC5`, `NPRL2`, `NPRL3`, `PTEN`.
- *Germline predisposition:* a germline `TSC1`/`TSC2` or GATOR1 (`DEPDC5`/`NPRL2`/`NPRL3`) variant creates a **field of vulnerability** — one somatic second hit anywhere in a telencephalic progenitor produces HME. This is the only setting in which HME carries a meaningful familial recurrence risk, and it matters enormously for counselling.
- *Susceptibility loci / GWAS:* **none.** HME is not a complex-trait disease; there is no GWAS Catalog signal, and there should not be.
- *Modifier genes:* not established. The candidate "modifier" is really **variant allele fraction and clone geography**, not a second gene (see §4).

**Environmental risk factors.** **None established.** No toxin, infection, maternal exposure, parity, or socioeconomic factor is reproducibly associated. The mutational events are the spontaneous-replication-error kind, not the exposure-driven kind. Two nuances worth curating as *negative* or *unresolved*:
- Advanced paternal age is a known driver of *germline* de novo mutation but has **not** been shown to drive postzygotic somatic mutation in HME.
- Crino (PMID:26060899, **[verbatim-verified from full text in cache]**) raises a viral hypothesis for FCD II, not HME, and is explicitly agnostic: "Alternatively, human papilloma virus may have no pathogenic role in FCD." Do **not** import this into HME as a risk factor.

**Sex.** No consistent sex bias reported. Laterality: a **left-sided predominance** was reported in the 2025 single-centre Seizure series (n=14) **[secondhand — RE-VERIFY, PMID:41033188]**, but this is not a robust finding across series and should not be curated as a `frequency`-bearing claim.

### 2.3 Protective factors

None known, genetic or environmental — as expected for a somatic-mutation disease of embryogenesis. There is no meaningful "protection" concept here; the closest analogue is **early surgical intervention as secondary prevention of epileptic encephalopathy** (§13).

### 2.4 Gene–environment interactions

**Not applicable / none demonstrated.** The only genuine "interaction" in HME is genetic × developmental-timing: the *same* mutation produces FCD, HME, or bilateral megalencephaly depending on **when** in corticogenesis and **in which progenitor pool** it arises (D'Gama 2017). That is a gene × developmental-clock interaction, not a gene × environment one, and it is the single most important structural insight to encode in the pathograph.

---

## 3. Phenotypes

Frequency bands below follow the HPO `FrequencyEnum` convention. **Caution for curation:** most HME literature is small surgical series; frequency figures reported here that lack a quantitative denominator should be curated **without** a `frequency:` value rather than with a fabricated band (per `docs/frequency-evidence-guidelines.md`).

### 3.1 Core neurological phenotypes

| Phenotype | Suggested HP term | Onset | Severity | Course | Frequency | Evidence |
|---|---|---|---|---|---|---|
| **Hemimegalencephaly (the structural lesion itself)** | `HP:0007206` Hemimegalencephaly | congenital / antenatal | — | static substrate | Obligate (definitional) | MONDO:0020492 def; PMID:37975663 |
| **Drug-resistant epilepsy** | `HP:0001250` Seizure (+ specify drug-resistance) | neonatal to <6 mo, frequently **day 1 of life** | severe | intractable, multiple daily seizures | Very frequent → obligate ("virtually all") | PMID:34608615; PMID:41033188 |
| **Epileptic (infantile) spasms** | `HP:0011097` Epileptic spasm | 3–12 mo | severe | often evolves from focal seizures | Frequent | PMID:39926610 (whole cohort is IESS+FMCD); TAE series PMID:42208165 |
| **Focal impaired-awareness seizures with motor features** | `HP:0002384` Focal impaired awareness seizure | neonatal | severe | | Very frequent (75% in one TAE series) | PMID:42208165 **[secondhand]** |
| **Epilepsia partialis continua** | `HP:0012847` Epilepsia partialis continua | infancy–childhood | severe | continuous | Occasional — and a **negative prognostic marker** | PMID:37873610 |
| **Contralateral hemiparesis / spastic hemiplegia** | `HP:0002301` Hemiplegia (or `HP:0001269` Hemiparesis) | infancy | moderate–severe | non-progressive but functionally worsens with growth | Very frequent | PMID:37975663; MONDO def ("progressive hemiparesis") |
| **Contralateral homonymous hemianopia** | `HP:0000580` Hemianopia (verify subtype term) | infancy (often detected late) | — | static | Frequent | PMID:34608615 ("contralateral hemiparesis and hemianopia are commonly reported") **[verbatim-verified from cache]** |
| **Global developmental delay** | `HP:0001263` Global developmental delay | infancy | severe | plateau or regression | Very frequent | PMID:37975663 |
| **Intellectual disability** | `HP:0001249` Intellectual disability | childhood | typically severe | static/plateau | Very frequent | PMID:28377884 |
| **Developmental regression (epileptic encephalopathy)** | `HP:0002376` Developmental regression | infancy, with seizure onset | severe | | Frequent | PMID:34608615 |
| **Absent or severely limited speech** | `HP:0001344` Absent speech | childhood | severe | | Frequent | Puka 2021, PMID:34608636 |
| **Macrocephaly / cranial asymmetry** | `HP:0000256` Macrocephaly | congenital–infancy | mild–moderate | | Frequent (not universal — a big *hemisphere* does not always give a big *head*) | MONDO def; Orphanet |
| **Ventriculomegaly / colpocephaly (ipsilateral)** | `HP:0002119` Ventriculomegaly | congenital | — | static | Very frequent | MONDO def; imaging literature |
| **Abnormality of neuronal migration** | `HP:0002269` Abnormality of neuronal migration | prenatal | — | static | Very frequent | PMID:36325654 |
| **Corpus callosum dysgenesis** | `HP:0007370` Aplasia/Hypoplasia of the corpus callosum | prenatal | variable | static | Occasional–frequent | imaging literature |

### 3.2 Systemic / syndromic phenotypes (in syndromic HME only)

- **Epidermal nevus / linear sebaceous nevus** (`HP:0001051` or a more specific nevus term) — epidermal nevus syndrome is the classic HME-associated neurocutaneous disorder; one review identified 57 previously reported ENS+HME cases in which "the most frequent associated features were severe epilepsy, in about half of cases with neonatal onset, mental retardation/developmental delay, ocular/visual involvement, and facial abnormalities" **[secondhand — RE-VERIFY]**
- **Hypopigmented streaks along Blaschko lines** (hypomelanosis of Ito) — `HP:0001010`/`HP:0011358`; note MTOR-related hypomelanosis of Ito is now molecularly linked to HME
- **Capillary/vascular malformation, hemihypertrophy** (Klippel-Trénaunay / MCAP overlap) — `HP:0001028`, `HP:0001528` Hemihypertrophy
- **Facial infiltrating lipomatosis with contralateral HME** — a recognized (and mechanistically informative: PIK3CA-driven) association, PMID:39454530
- **TSC stigmata** in TSC-associated HME (cardiac rhabdomyoma, hypomelanotic macules, renal angiomyolipoma) — PMID:33387903, PMID:26231267, PMID:35022853
- **Hemihypertrophy of the ipsilateral body** — reported; note laterality: body hypertrophy is typically **ipsilateral** to the big hemisphere

### 3.3 Electrophysiological phenotype (a phenotype in its own right for HME)

- **Hemihypsarrhythmia** — the near-pathognomonic infantile EEG signature: asymmetric, lateralized hypsarrhythmia
- **Unilateral suppression-burst**, especially in sleep
- **Depressed background voltage over the involved hemisphere with bursts of numerous spikes in wakefulness** **[secondhand — RE-VERIFY]**
- Suggested term: `HP:0011182` Interictal epileptiform activity (HPO lacks a hemihypsarrhythmia term — a genuine ontology gap worth noting)
- **Bilateral ictal EEG abnormality** is the single strongest adverse surgical predictor (§11)

### 3.4 Quality-of-life impact

Per-phenotype QoL data are thin. What exists:
- Post-hemispherectomy QoL "depends not only on seizure outcome but also on developmental and functional outcomes, such as motor and language impairments," and HME as a substrate "is associated with worse motor and language outcomes" **[secondhand — RE-VERIFY]**
- **Caregiver burden did not improve** after surgery in at least one series, attributed to the chronic nature of the condition **[secondhand — RE-VERIFY]** — a striking and curation-worthy dissociation: seizures improve, family burden does not.
- No EQ-5D, SF-36, PROMIS, or HME-specific PRO instrument data exist. **This is a real gap.**

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

All converge on **mTORC1 hyperactivation**. Two arms:

**Arm A — somatic GAIN-of-function in mTOR pathway activators** (the dominant mechanism in HME, "single-hit"):

| Gene | HGNC | Canonical HME variants | Consequence | Key PMIDs |
|---|---|---|---|---|
| `MTOR` | `hgnc:3942` | p.Cys1483Tyr, p.Ser2215Phe/Tyr, p.Leu2427Pro/Gln, p.Ala1459Pro | GOF — constitutive kinase activity | 22729223; 31444548; 30514132 |
| `PIK3CA` | `hgnc:8975` | **c.1633G>A p.Glu545Lys (recurrent, 4/20 in Lee 2012)**; p.His1047Arg/Leu; p.Glu542Lys | GOF — catalytic p110α | 22729223; 25722288; 36325654 |
| `AKT3` | `hgnc:393` | **c.49G>A p.Glu17Lys**; also mosaic **trisomy 1q** encompassing the AKT3 locus | GOF — PH-domain lock to membrane | 22500628; 22729223 |
| `AKT1` | `hgnc:391` | p.Glu17Lys (Proteus-type) | GOF | 36325654 (fetal HME case) |
| `RHEB` | `hgnc:10011` | p.Tyr35Leu/Asn | GOF — constitutive mTORC1 activator | 31444548; 34608615 |
| `PIK3R2` | `hgnc:8980` | p.Gly373Arg | GOF (loss of p85β inhibition of p110) — chiefly MPPH, HME-adjacent | 22729224 |

**Arm B — LOSS-of-function in mTOR repressors** (germline, somatic, or classic two-hit):

| Gene | HGNC | Mechanism in HME | Key PMIDs |
|---|---|---|---|
| `TSC2` | `hgnc:12363` | two-hit (germline + somatic second hit) in *isolated* HME; also TSC-associated HME | 29281825; 31444548; 33387903 |
| `TSC1` | `hgnc:12362` | as above | 31444548; 35022853 |
| `DEPDC5` | `hgnc:18423` | GATOR1 LOF; **first implicated in HME by D'Gama 2015** | 25599672; 31444548 |
| `NPRL2` | `hgnc:24969` | GATOR1 LOF | 29281825 |
| `NPRL3` | `hgnc:20558` | GATOR1 LOF; reported in neonatal HME with intractable seizures | 33749980 |
| `PTEN` | `hgnc:9588` | LOF; a 2026 fetal case showed **biallelic** PTEN alteration in affected tissue, hemisphere-restricted | 25722288; PMID:42024976 |

The 2026 PTEN fetal report is worth quoting for the mechanism it rules *out* **[secondhand — RE-VERIFY, PMID:42024976]**: hemispheric overgrowth caused by "biallelic PTEN alteration in affected brain tissue, while the unaffected hemisphere carried only heterozygous variant," with outer-subventricular-zone nodular heterotopias composed exclusively of "SATB2+ glutamatergic projection neurons," and the conclusion that "the PTEN mutation is not a dominant-negative variant."

### 4.2 Variant characteristics

- **Origin:** predominantly **somatic / postzygotic**, brain-restricted. D'Gama & Poduri (PMID:34608615, **[verbatim-verified from cache]**): "In general, when blood samples are available, the somatic mosaic variants identified in brain tissue are not detected in blood, suggesting that the mutational events that result in these variants arise relatively late in embryonic development, after gastrulation or in some cases after neurulation."
- **Variant allele fraction (VAF):** the defining quantitative feature. Lee 2012: "present in 8-40% of sequenced alleles in various brain regions." D'Gama & Poduri: "The alternate allele frequency (AAF) of detected somatic mutations in FCD and HME ranges from approximately 1 to 30%… The average AAF for variants associated with FCD is lower than the average AAF for variants associated with HME; while there is some overlap, there appears to be a relationship between the allele frequency and the severity of the phenotype." **[verbatim-verified from cache]** — **VAF is effectively the dose-response variable of this disease.**
- **Variant class:** almost entirely **missense** in the activator arm (recurrent hotspot residues, largely shared with the cancer somatic-mutation catalogue); **truncating/frameshift/splice + LOH** in the repressor arm; plus **somatic copy-number gain** (mosaic trisomy 1q → AKT3).
- **Allele frequency in population databases:** **absent from gnomAD** as constitutional variants (they are embryonic-lethal or syndromic in germline form; the PIK3CA and AKT hotspots are COSMIC-catalogued oncogenic drivers instead). For KB purposes: gnomAD frequency is **not applicable** — do not curate a "0.00" as if it were a measured population frequency.
- **ACMG classification:** the recurrent activators (PIK3CA E545K, AKT3 E17K, MTOR S2215F) are Pathogenic; the framework strains at somatic mosaic variants, and ACMG/AMP germline rules apply awkwardly. Note this as a methodological caveat.
- **Cell-of-origin:** dysmorphic neurons and balloon cells **carry** the variant — Baldassari 2019, "Analysis of microdissected cells demonstrated that DNs and BCs carry the pathogenic variants." **[verbatim-verified]**

### 4.3 Modifier genes

None established. The functional "modifier" is **mutation timing + clone size + cell lineage**, per D'Gama 2017.

### 4.4 Epigenetics

No disease-defining methylation or chromatin signature has been established for HME. One methodologically relevant use of epigenomics: **whole-genome bisulfite sequencing of CSF cell-free DNA** was used alongside ddPCR to assign brain origin to mosaic variants (PMID:33738444) — epigenomics as a *tissue-of-origin tracer*, not as a disease mechanism. Curate accordingly.

### 4.5 Chromosomal abnormalities

**Mosaic trisomy 1q** (encompassing `AKT3` at 1q43-q44) in 2/8 HME samples — Poduri 2012, "the estimated copy number for 1q in one patient (HMG-1) was 2.41 (SD 0.12), consistent with mosaic trisomy 1q" **[secondhand — RE-VERIFY]**. This is the reason chromosomal microarray on **brain tissue** (not blood) retains a role. Otherwise: no recurrent karyotypic abnormality; blood karyotype and blood CMA are normal in isolated HME.

---

## 5. Environmental Information

- **Environmental factors:** none established. No CTD-catalogued chemical association. Nothing in TOXNET/EPA that survives scrutiny.
- **Lifestyle factors:** not applicable — a prenatal somatic-mutation disease.
- **Infectious agents:** **not applicable for HME.** Congenital CMV can produce cortical malformation (pachygyria, polymicrogyria) and belongs in the **differential**, not the etiology. The HPV/CMV/HHV-6 literature in FCD II (discussed by Crino, PMID:26060899) has not been extended to HME and remains contested even for FCD.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (proposed dismech pathograph)

This is the spine of the entry. Each arrow is a curatable `downstream` edge.

```
[1] Postzygotic somatic mutation in a dorsal telencephalic progenitor
    (GOF: MTOR/PIK3CA/AKT3/AKT1/RHEB  |  LOF ± 2nd hit: TSC1/TSC2/DEPDC5/NPRL2/NPRL3/PTEN)
    biological_scale: MOLECULAR
        ↓
[2] Constitutive mTORC1 activation in the mutant clone
    (readout: phospho-S6 Ser240/244, phospho-p70S6K, phospho-4E-BP1)
    biological_scale: MOLECULAR
        ↓
[3] Unrestrained cap-dependent translation, ribosome biogenesis, and cell growth;
    suppressed autophagy
    biological_scale: CELLULAR
        ↓  ↓  ↓  (three parallel consequences)
[4a] Progenitor over-proliferation / failed apoptosis → clonal hemispheric overgrowth
[4b] Cytomegaly → dysmorphic (cytomegalic) neurons and balloon cells
[4c] Impaired radial migration and lineage specification → cortical dyslamination,
     polymicrogyria, subcortical/periventricular/subarachnoid heterotopia
    biological_scale: CELLULAR / TISSUE
        ↓
[5] Hemispheric megalencephaly with severe cortical dysplasia, white matter
    hypertrophy with abnormal myelination, and ipsilateral ventriculomegaly
    biological_scale: TISSUE
        ↓
[6] Excitation–inhibition imbalance and intrinsic hyperexcitability of dysmorphic
    neurons (reduced GABA_A subunit expression, fewer GABAergic interneurons,
    altered glutamate receptor composition)
    biological_scale: CELLULAR   ← conforms_to: epilepsy_excitation_inhibition_imbalance
        ↓
[7] Hemispheric ictogenesis and epileptogenesis (hemihypsarrhythmia, suppression-burst,
    epilepsia partialis continua)
    biological_scale: ORGANISM
        ↓
[8] Epileptic encephalopathy: seizure burden + malformed network → arrest and
    regression of development, contralateral hemiparesis/hemianopia from the
    structurally deficient hemisphere
    biological_scale: ORGANISM
        ↓
[9] Secondary contralateral dysfunction ("the good hemisphere is not innocent"):
    contralateral hemimicrencephaly in some cases; uncrossed cerebellar diaschisis
    biological_scale: ORGANISM
```

**Key branch to encode:** step [1] has *two mechanistically opposite* entry routes (activator GOF vs. repressor LOF) that converge on the identical node [2]. This is a textbook convergent-node structure and belongs in the pathograph explicitly.

**Key modulating variable:** the *timing* of [1] determines whether you get FCD (late, small clone), HME (earlier, hemisphere-sized clone), or bilateral megalencephaly (earliest). Curate this as a `mechanistic_hypotheses`/annotation rather than as three separate diseases.

### 6.2 Molecular pathways

- **PI3K–AKT–mTORC1** — the whole story. GO: `GO:0031929` TOR signaling; `GO:0032008` positive regulation of TOR signaling; `GO:0038202` TORC1 signaling; `GO:0032006` regulation of TOR signaling; `GO:0043491` phosphatidylinositol 3-kinase/protein kinase B signal transduction (**note: `GO:0014065` "phosphatidylinositol 3-kinase signaling" is OBSOLETE — do not use**).
- Two upstream sensing arms converge on mTORC1 and are *not* interchangeable — D'Gama & Poduri, **[verbatim-verified from cache]**: "activation of the energy-sensing pathway (PI3K-PTEN-AKT-TSC-RHEB) versus the amino-acid sensing pathway (GATOR-RAG) that converge on mTOR shows some differences in in vitro studies and animal models, suggesting that the effects of a given activating mTOR pathway mutation will depend on both general hyperactivation of the mTOR pathway and potentially specific effects of the mutated protein." This is a genuine, curatable nuance: **DEPDC5-HME and PIK3CA-HME are not the same disease at the molecular level, even though both are "mTOR."**
- KEGG `hsa04150` (mTOR signaling pathway); Reactome R-HSA-165159 (mTOR signalling), R-HSA-1257604 (PIP3 activates AKT signaling).

### 6.3 Cellular processes

- **Cell growth** `GO:0016049` — INCREASED (the cytomegaly node)
- **Cell population proliferation** `GO:0008283` — INCREASED (progenitor over-proliferation)
- **Neuron migration** `GO:0001764` — DECREASED/ABERRANT
- **Cell motility involved in cerebral cortex radial glia guided migration** `GO:0021814` — DECREASED
- **Cerebral cortex development** `GO:0021987` / **brain development** `GO:0007420` — ABNORMAL
- **Translation** `GO:0006412` — INCREASED
- **Autophagy** `GO:0006914` — DECREASED (mTORC1 suppresses it; note Crino's observation of autophagic vacuoles and p62 in FCD IIb/TSC, i.e. *blocked flux*)
- **Regulation of cell differentiation** `GO:0045595` — ABNORMAL (balloon cells express progenitor markers SOX2, nestin, vimentin, c-myc — "suggesting a failure to differentiate before migration into the cortex," Crino PMID:26060899 **[verbatim-verified from cache]**)
- **Neuronal ciliogenesis** — a mechanistically distinct downstream effect of MTOR somatic variants leading to dyslamination (Park et al., *Neuron* 2018); worth an EMERGING hypothesis node.

### 6.4 Protein dysfunction

- **AKT3 p.E17K**: PH-domain charge reversal → pathological plasma-membrane recruitment independent of PIP3 → constitutive activation. Exactly paralogous to the AKT1/AKT2 E17K substitutions in somatic overgrowth syndromes (Poduri 2012).
- **PIK3CA p.E545K** (helical domain): abolishes p85 inhibitory contact → constitutive p110α lipid-kinase activity. **p.H1047R** (kinase domain): membrane-binding/conformational activation. Both are canonical COSMIC oncogenic hotspots — the same lesions, in a different tissue and a different developmental window, that drive carcinoma. HME is, in a real sense, **oncogenic signalling without oncogenesis**: the clone grows and differentiates badly but does not become malignant.
- **MTOR kinase-domain substitutions** (S2215F/Y, L2427P): relieve autoinhibition.
- **TSC1/TSC2/TBC1D7 complex** LOF: loss of GAP activity toward RHEB → RHEB stays GTP-bound → mTORC1 on.
- **GATOR1 (DEPDC5/NPRL2/NPRL3)** LOF: loss of GAP activity toward RAG GTPases → amino-acid-independent mTORC1 activation.
- **PTEN** LOF: PIP3 not dephosphorylated → sustained AKT activation.
- UniProt anchors: `P42345` MTOR, `P42336` PIK3CA, `Q9Y243` AKT3, `P31749` AKT1, `Q92974`→ use `Q15382` RHEB, `Q92574` TSC1, `P49815` TSC2, `O60484` DEPDC5, `P60484` PTEN.

### 6.5 Metabolic changes

mTORC1 is a master anabolic switch, so the mutant clone shows increased glycolytic and lipogenic flux, increased nucleotide and protein synthesis. Direct human HME metabolomics is essentially absent. One indirect clinical observation is mechanistically suggestive: the ketogenic diet reduces phospho-S6 and phospho-Akt in fed rats, "suggesting inhibition of the mTOR pathway, potentially due to an amino acid deprivation-like environment" (Crino/D'Gama & Poduri, PMID:34608615 **[verbatim-verified from cache]**) — i.e. a dietary intervention acting on the *same node* as the targeted drug.

### 6.6 Immune system involvement

Not primary. Innate and adaptive immune activation is described in FCD II tissue and may be reactive/secondary to seizures. Do **not** curate HME as an immune-mediated disease. The clinically relevant immune issue is **iatrogenic**: mTOR inhibitors are immunosuppressants (stomatitis, recurrent URIs, pneumonitis).

### 6.7 Tissue damage mechanisms

There is no primary degeneration or necrosis. The "damage" is **maldevelopment plus seizure-driven network injury**, with two secondary threads worth noting:
- Neurodegeneration-adjacent changes: "abnormal activation of mTOR may contribute to apoptosis signaling pathways and premature activation of neurodegeneration cascades," including hyperphosphorylated tau in pS6-positive dysmorphic neurons (Crino, **[verbatim-verified from cache]**).
- **Uncrossed cerebellar diaschisis** — remote functional deafferentation demonstrated by FDG-PET and DTI tractography (PMID:40344425), a nice illustration that the lesion's footprint exceeds its anatomy.

### 6.8 Biochemical abnormalities

- **The diagnostic biochemical readout is phospho-S6 ribosomal protein (Ser240/244 or Ser235/236) immunoreactivity** in dysmorphic neurons and balloon cells. Itoh 2023, **[secondhand — RE-VERIFY, PMID:36325654]**: "Scattered cell nests immunoreactive for phosphorylated-S6 ribosomal protein (P-RPS6) (Ser240/244) were observed in the polymicrogyria-like cortical plate, intermediate zone, and arachnoid space, suggesting that the PI3K-AKT-MTOR pathway was actually activated in these cells."
- Jansen 2015 (PMID:25722288) found "elevated levels of phosphorylated S6 ribosomal protein were identified in both neurons and astrocytes" **[secondhand — RE-VERIFY]** — note the glial component.
- Baldassari 2019 **[verbatim-verified]**: "panel-negative FCD2 cases display strong pS6-immunostaining, stressing that all FCD2 are mTORopathies." The pathway is on even when sequencing fails to find the culprit.
- Ion channels / receptors: reduced GABA_A receptor subunit expression, fewer GABAergic interneurons, altered glutamate receptor subunit composition; a specific mechanism reported for MTOR-FCD is hyperexcitability "via overactivation of neuronal GluN2C NMDA receptors" (preprint-stage; do not curate as established).

### 6.9 Molecular profiling

- **Single-cell:** D'Gama 2017 — "Single-cell sequencing demonstrated mTOR activation in neurons in all lesions" **[secondhand — RE-VERIFY]**; Baldassari 2019 microdissection assigned variants to DNs and BCs and found "a somatic second-hit loss-of-heterozygosity in a DEPDC5 germline case" **[verbatim-verified]**.
- **Lineage restriction — the sharpest single mechanistic claim in the literature:** D'Gama 2017 — "Conditional Pik3ca activation in the mouse cortex showed that mTOR activation in excitatory neurons and glia, but not interneurons, is sufficient for abnormal cortical overgrowth." **[secondhand — RE-VERIFY, and worth the effort: this is the cell-type-specificity claim.]**
- **Recent contradicting/complicating datum:** Gelot et al., *Epilepsia* 2025 (PMID:39973610) report **cytomegalic parvalbumin neurons in fetal HME** — i.e. inhibitory interneurons *are* morphologically involved in human fetal tissue, even if mouse interneuron-restricted activation isn't sufficient. Curate this as a `HUMAN_MODEL_MISMATCH` discussion: mouse says interneurons don't matter for overgrowth; human fetal pathology says interneurons are visibly affected. (I could not obtain this abstract verbatim — **RE-VERIFY before use**.)
- **Transcriptomics / proteomics / metabolomics / lipidomics:** no dedicated HME datasets of note in GEO/PRIDE/MetaboLights. **This is a genuine, statable gap.**
- **Functional genomics screens:** none HME-specific.

### 6.10 Cell types (CL) and anatomy — mechanism-relevant

| Cell type | CL term | Role |
|---|---|---|
| radial glial cell | `CL:0000681` | the mutated progenitor; clone founder |
| neural progenitor cell | `CL:0011020` | over-proliferating compartment |
| glutamatergic neuron | `CL:0000679` | the lineage in which mTOR activation is necessary/sufficient |
| pyramidal neuron | `CL:0000598` | substrate of the cytomegalic/dysmorphic neuron |
| astrocyte | `CL:0000127` | pS6-positive; contributes to overgrowth |
| oligodendrocyte | `CL:0000128` | white-matter hypertrophy/dysmyelination |
| GABAergic neuron | `CL:0000617` | E/I imbalance; cytomegalic PV neurons in fetal HME |

*Ontology gap to note:* Cell Ontology has **no term for "balloon cell" or "dysmorphic (cytomegalic) neuron"** — the two cells that literally define this disease's histology. Use `preferred_term: balloon cell` over the nearest CL parent and flag the gap.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** one **cerebral hemisphere** — `UBERON:0001869` cerebral hemisphere; **cerebral cortex** `UBERON:0000956`
- **Secondary:** ipsilateral **white matter** `UBERON:0002316` (hypertrophic, abnormally myelinated); ipsilateral **lateral/telencephalic ventricle** `UBERON:0002285` (enlarged, with the characteristic straightened frontal horn pointing antero-superiorly); **corpus callosum** `UBERON:0002336` (dysgenetic); **basal ganglia** `UBERON:0002420` (often enlarged ipsilaterally); **hippocampal formation** `UBERON:0002421`
- **"Total" HME:** ipsilateral **cerebellum** `UBERON:0002037` and **brainstem** `UBERON:0002298` hypertrophy — the Flores-Sarnat "total hemimegalencephaly" variant (Flores-Sarnat L, *J Child Neurol* 2002;17:373–84 Part 1; 2003;18:776–85 Part 2 — **PMIDs not independently verified in this session; verify before citing**)
- **Contralateral hemisphere:** *not* normal in a meaningful fraction — contralateral hemimicrencephaly and abnormalities "occurring outside the involved hemisphere" are described (AJNR 2007), and contralateral EEG abnormality is the dominant negative surgical predictor
- **Body systems:** nervous system, primarily; integumentary/vascular/skeletal in syndromic forms

### Tissue and cell level
Neural tissue: cortical grey matter (dyslaminated, thickened), subcortical and periventricular white matter (heterotopic neurons, gliosis, abnormal myelin), leptomeninges (subarachnoid heterotopia in fetal cases). Cell populations as in §6.10.

### Subcellular level (GO CC)
- `GO:0031931` TORC1 complex — the locus of the lesion
- `GO:0005886` plasma membrane — where AKT3 E17K wrongly parks
- `GO:0005829` cytosol — PI3K/AKT signalling
- `GO:0022626` cytosolic ribosome / `GO:0005840` ribosome — the S6 readout
- `GO:0005764` lysosome — the mTORC1 docking platform (Rag/Ragulator); the GATOR arm acts here
- `GO:0005929` cilium — implicated in the MTOR-ciliogenesis dyslamination mechanism

### Localization and lateralization
- **Unilateral by definition.** `HP:0012837` Unilateral (as a modifier). Left-sided predominance reported in at least one recent series but not robustly established.
- Distribution within the hemisphere may be **complete** (whole hemisphere) or **partial/lobar** — partial forms shade into hemispheric cortical dysplasia and the FCD end of the continuum, which is a boundary curators will have to draw deliberately.

---

## 8. Temporal Development

### Onset
- **The mutation:** prenatal, postzygotic, after gastrulation/neurulation; the lesion is built between roughly **gestational weeks 5–20** (cortical tubers, the closest-studied analogue, are detectable from ~20 weeks; Crino: "indicating that tubers (and by extension, focal cortical dysplasias) form during embryonic brain development, probably between weeks 10 and 20 of human gestation" **[verbatim-verified from cache]**)
- **The lesion:** detectable prenatally on fetal MRI and even transabdominal/transvaginal ultrasound (PMID:38617140); a notable report describes evolution "from an atypical focal early appearance on fetal MRI to more conventional MR findings" — i.e. **the fetal appearance can be misleadingly focal early on**
- **Seizures:** neonatal to <6 months, very often within days of birth. The 2026 Epilepsia infant surgical series reports "Median seizure onset occurred at 3 days of life" **[secondhand — RE-VERIFY, PMID:42132620]**; the 2026 TAE series "Mean seizure onset occurred at 9 days old" **[secondhand — RE-VERIFY, PMID:42208165]**; the 2025 Seizure series reports onset "within the first day of life" **[secondhand — RE-VERIFY, PMID:41033188]**
- **Onset pattern:** congenital structural lesion; **acute-to-catastrophic** epilepsy onset superimposed on it

### Progression
- **The malformation is static.** The *epilepsy* and its consequences are not.
- Typical trajectory: neonatal focal seizures → status-epilepticus-prone, multiple daily seizures → often evolution to **epileptic spasms / IESS** at 3–12 months → hemihypsarrhythmia → developmental arrest or regression → in survivors, a chronic multi-seizure-type drug-resistant epilepsy
- Epileptogenic zone can *expand*: "the epileptogenic area may increase with poor seizure control" **[secondhand — RE-VERIFY]** — the mechanistic justification for early surgery
- **Duration:** chronic, lifelong. No spontaneous remission.
- Adult data are scant and unpromising: "Few patients with HME have been followed into adulthood. Reported adult cases have milder epilepsy or underwent hemispherectomy in childhood. Patients surviving to adulthood have poor outcomes, regardless of treatment method, although seizure burden is improved with hemispherectomy." (PMID:28377884) **[secondhand — RE-VERIFY]**

### Critical periods
Two, and they pull against each other — this is the central clinical tension of HME:
1. **The neurodevelopmental window (first ~6–12 months)**: uncontrolled seizures during peak synaptogenesis cause the encephalopathy. Argues for operating **as early as possible**.
2. **The surgical-safety window**: hemispherectomy in neonates and very small infants carries high blood-loss and mortality risk. "With neonates and young infants, hemispherectomy has a very high mortality and complication rate, resulting in most neurosurgeons deferring treatment until at least 8 weeks" **[secondhand — RE-VERIFY]**. Argues for **waiting for weight gain**.

Everything interesting in current HME therapeutics — mTOR inhibitors as a bridge, staged transarterial embolization — is an attempt to buy time between these two windows.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** genuinely unknown at the population level. NORD states prevalence estimates are not available. The most-cited figure is denominator-shifted: **1–3 per 1,000 children with epilepsy** **[secondhand — RE-VERIFY]** — note carefully that this is *not* a population prevalence and must not be curated as one. For a dismech `Prevalence` record: `measure_type: UNKNOWN` or a qualitative `prevalence_class: ULTRA_RARE`, with the epilepsy-denominator figure in `notes`.
- **Incidence:** no reliable estimate.
- **Surgical-series representation** (the only well-quantified denominators, and heavily biased):
  - HME was **58%** of seizure etiologies among infants undergoing hemispherectomy/hemispherotomy **[secondhand — RE-VERIFY]**
  - HME made up **42.6%** of anatomic hemispherectomy cases vs **14.1%** of functional hemispherectomy cases **[secondhand — RE-VERIFY]**
  - In one 35-year single-institution hemispherectomy series, HME was the third commonest etiology (n=25) after MCD (n=39) and stroke (n=30) **[secondhand — RE-VERIFY]**

### Inheritance
- **Sporadic / non-Mendelian in the overwhelming majority.** The causal event is a **postzygotic somatic mutation**, so HME has no inheritance pattern in the classical sense. HPO: no standard mode-of-inheritance term applies cleanly — the honest annotation is `HP:0001470`? no — use **`HP:0001426` Multifactorial inheritance**? Also no. The correct handling is to **omit** a mode-of-inheritance term for isolated HME and record "somatic mosaicism, non-heritable" in the description, or use `HP:0003745` Genetic anticipation-adjacent terms — **do not** force-fit. HPO's `HP:0001470`-family lacks a "somatic mosaicism" mode; this is a real ontology gap for mosaic diseases and worth flagging.
- **Exception — the two-hit / germline-predisposition subset:** where a germline `TSC1`/`TSC2` or GATOR1 (`DEPDC5`/`NPRL2`/`NPRL3`) LOF variant is the first hit, the *predisposition* is **autosomal dominant** (`HP:0000006`), with the HME lesion itself requiring a somatic second hit. This subset carries a **50% transmission risk for the predisposing allele** — and must be identified, because the counselling is completely different.
- **Penetrance:** the germline predisposing allele is incompletely penetrant for HME specifically (most TSC patients never develop HME — PMID:33387903 calls the association "uncommon and has so far been reported only in a few cases"). The somatic second hit is essentially fully penetrant *locally*.
- **Expressivity:** highly variable, and the variability maps onto **VAF and clone geography** rather than onto a modifier locus.
- **Genetic anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** theoretically possible if the mutation arose very early (pre-primordial-germ-cell segregation), which would produce both somatic and gonadal mosaicism. Not documented in HME. Recurrence risk for isolated HME is generally counselled as **near-baseline but not formally zero**.
- **Founder effects / carrier frequency / consanguinity:** not applicable.

### Population demographics
- **Ethnic/geographic:** no established variation. Cases reported worldwide (US, Europe, Japan, Korea, China, Turkey, India, Latin America). Apparent geographic clustering in the literature reflects **where paediatric epilepsy surgery programmes exist**, not disease biology — an important curation caveat.
- **Sex ratio:** approximately 1:1; no established bias.
- **Age distribution:** overwhelmingly infants and children, because ascertainment is via early catastrophic epilepsy and because unoperated survival into adulthood is uncommon and under-reported.

---

## 10. Diagnostics

### Imaging — the primary diagnostic modality
**Brain MRI** is the diagnostic test. Characteristic features:
- Enlargement of all or part of one hemisphere with **midline shift**
- **Thickened, dysplastic cortex** with abnormal gyration (agyria, pachygyria, polymicrogyria) and blurred grey–white junction
- **Abnormal white matter signal** — T2/FLAIR hyperintensity, hypertrophic white matter, often with a transmantle-like tapering to the ventricle
- **Ipsilateral lateral ventricle enlarged and dysmorphic**, with the classic **straightened frontal horn pointing antero-superiorly** — near-signature
- Grey-matter **heterotopia** (subcortical, periventricular)
- Ipsilateral basal ganglia enlargement, corpus callosum dysgenesis, ± ipsilateral cerebellar hypertrophy (total HME)
- **Fetal MRI and prenatal ultrasound** can make the diagnosis antenatally (PMID:38617140; the "in utero MRI" literature) — with the caveat that the early fetal appearance may be deceptively focal
- **FDG-PET:** regional hypometabolism; also reveals **uncrossed cerebellar diaschisis** (PMID:40344425)
- **RadLex/DICOM:** standard paediatric brain MRI protocol; add DTI for tractography and presurgical mapping

### Electrophysiology
- **EEG / video-EEG** is mandatory and is both diagnostic and **prognostic**. Look for: lateralized background suppression with high-voltage spike bursts; **hemihypsarrhythmia**; **unilateral suppression-burst**, especially in sleep; epilepsia partialis continua.
- **The single most important EEG finding for prognosis is whether the abnormality is confined to the affected hemisphere.** Bilateral ictal EEG abnormality was the only independent predictor of faster seizure recurrence after hemispherectomy (HR = 11.5; P = .002 — PMID:37975663 **[verbatim-verified from cache]**).
- LOINC: standard EEG codes (e.g. 24708-8 EEG study); no HME-specific code.

### Histopathology (on resected tissue)
- Cortical **dyslamination**, **polymicrogyria**, **heterotopia** (subarachnoid, subcortical, subventricular), immature neurons, calcifications
- **Dysmorphic (cytomegalic) neurons** and **balloon cells** — histologically indistinguishable from FCD IIb and from TSC giant cells
- **Immunohistochemistry: phospho-S6 (Ser240/244 or Ser235/236) is the workhorse.** Positive labelling in DNs and BCs establishes mTOR pathway activation even when sequencing is negative.
- Mixed/ambiguous lineage markers on balloon cells (SOX2, nestin, vimentin, c-myc; Pax6, ER81, Otx1) — the "failed to differentiate" signature
- Recent addition: **cytomegalic parvalbumin (inhibitory) neurons** in fetal HME (PMID:39973610)
- Note: **HME is not currently accommodated in the ILAE FCD classification** — Crino, **[verbatim-verified from cache]**: "Other types of focal MCD, such as TSC, hemimegalencephaly, and some of the newer focal cortical dysplasia syndromes have not yet been subsumed into the ILAE classification."

### Genetic testing — the crucial methodological point
**Blood-based testing is expected to be negative in isolated HME.** This is the diagnostic trap. The variant lives in the brain.

Recommended approach:
1. **Deep targeted panel sequencing (≥500×, ideally ≥2000×) of DNA from resected brain tissue**, paired with blood — the reference standard (Baldassari 2019 used "≥ 2000X read depth" on "matched blood-brain samples to search for low-allele frequency variants"). Panel content: `MTOR`, `PIK3CA`, `AKT1`, `AKT3`, `RHEB`, `PIK3R2`, `TSC1`, `TSC2`, `DEPDC5`, `NPRL2`, `NPRL3`, `PTEN`, plus `SLC35A2` (for the mMCD/MOGHE differential).
2. **Germline WES/WGS on blood** — to catch the two-hit predisposition arm (TSC1/TSC2/GATOR1), which *is* blood-detectable and *is* actionable for the family.
3. **Chromosomal microarray on brain tissue** — for mosaic 1q gain (AKT3).
4. **Microdissection / single-cell enrichment of DNs and BCs** raises yield when bulk VAF is low (Baldassari 2019).
5. **Emerging non-surgical routes:**
   - **CSF cell-free DNA liquid biopsy** — PMID:33738444, "cerebrospinal fluid liquid biopsy is valuable in investigating mosaic neurological disorders where brain tissue is unavailable" **[secondhand — RE-VERIFY]**; sensitivity is modest (3/12 known-positive cases in one ddPCR series) so a negative does not exclude.
   - **Trace DNA from stereo-EEG depth electrodes** — a 2024 report identified a mosaic MTOR variant in purified neuronal DNA from depth electrodes (preprint/medRxiv at time of writing — **do not curate as established**).
6. **Karyotype, FISH, mtDNA testing, repeat-expansion testing:** not indicated.

### Laboratory tests / biomarkers
No blood or urine biomarker exists. Routine labs are normal. There is **no validated circulating biomarker** for HME — a real gap, and the reason the CSF/electrode-DNA work matters.

### Clinical criteria and differential diagnosis

No formal consensus diagnostic criteria exist (unlike TSC). Diagnosis = characteristic MRI + compatible clinical picture, with histology confirming after surgery.

**Differential diagnosis:**

| Alternative | Distinguishing feature |
|---|---|
| **Hemispheric / multilobar focal cortical dysplasia** | Hemisphere not enlarged; ventricle normal size — this is the hardest and most important boundary, and it is a **continuum**, not a dichotomy (D'Gama 2017) |
| **Tuberous sclerosis complex** | Multifocal bilateral tubers, subependymal nodules, systemic stigmata — but note TSC and HME **co-occur** (PMID:33387903, PMID:26231267) |
| **Sturge-Weber syndrome** | Leptomeningeal angioma with contrast enhancement, gyriform calcification, hemi**atrophy** rather than hypertrophy |
| **Congenital CMV / congenital infection** | Periventricular calcification, microcephaly, positive serology/PCR |
| **Rasmussen encephalitis** | Later onset, progressive hemi**atrophy**, inflammatory histology |
| **Hemispheric low-grade tumour (DNET, ganglioglioma)** | Discrete mass, contrast behaviour, different histology — though gangliogliomas *also* show mTOR activation |
| **Perinatal arterial ischaemic stroke / porencephaly** | Vascular territory, encephalomalacia, hemiatrophy |
| **MCAP / MPPH (megalencephaly syndromes)** | **Bilateral** brain overgrowth ± polymicrogyria; overlapping genes (PIK3CA, AKT3, PIK3R2) — same pathway, different clone geography |
| **Hemispheric cortical dysplasia (HCD)** | Often grouped with HME in surgical series; increasingly treated as the same continuum |

### Screening
- **No newborn screening, no carrier screening, no population screening.** Not appropriate for a somatic-mutation disease.
- **Cascade screening does apply** in the two-hit subset: once a germline TSC1/TSC2/DEPDC5/NPRL2/NPRL3 variant is identified, first-degree relatives should be offered testing.
- **Prenatal detection** by fetal MRI/ultrasound is real but opportunistic, not a screening programme.

---

## 11. Outcome / Prognosis

### Survival and mortality
- **Untreated:** high early morbidity; deaths from status epilepticus, aspiration, and complications of profound neurological impairment. No reliable population survival curve exists.
- **Surgical mortality** has fallen dramatically. A meta-analysis reports overall procedure mortality **5%** (hemispherectomy 7%, hemispherotomy 3%), with reported mortality falling "over the last 30 years from 32% to 2%" **[secondhand — RE-VERIFY]**. The 2026 infant series (n=15, surgery at median 6.4 months) reported **no deaths** **[secondhand — RE-VERIFY, PMID:42132620]**.
- **Disease-specific mortality:** no registry data.

### Seizure outcomes after hemispheric surgery — the best-quantified prognostic data

**Goel et al., *Neurosurgery* 2024 — IPD meta-analysis, n=145 from 26 studies (PMID:37975663) [verbatim-verified from cache]:**
> "Data from 145 patients were extracted from 26 studies, of which 89 underwent FH (22 vertical, 33 lateral), 47 underwent AH, and 9 received an unspecified hemispherectomy with a median last follow-up of 44.0 months (FH cohort) and 45.0 months (AH cohort). Cohorts were similar in preoperative characteristics and at the last follow-up; 77% (n = 66) of the FH cohort and 81% (n = 38) and of the AH cohort were Engel I."
> "On multivariate analysis, only the presence of bilateral ictal electroencephalography abnormalities (hazard ratio = 11.5; P = .002) was significantly associated with faster time-to-seizure recurrence."
> "A number-needed-to-treat analysis to prevent 1 additional case of posthemispherectomy hydrocephalus reveals that FH, compared with AH, was 3."
> "We show that hemispheric surgery is a highly effective treatment for HME-related DRE."

**Goel et al., *Epilepsia* 2024 — UCLA single-centre, n=56, 1984–2021 (PMID:37873610) [secondhand — RE-VERIFY]:** 24 patients (49%) seizure-free at median 55 months; 17 (30%) required CSF shunting for hydrocephalus; independent favourable predictors were "Younger age at seizure onset (HR = .29, p = .029), lack of epilepsia partialis continua (EPC) (HR = .30, p = .022), and no contralateral seizures on electroencephalography (EEG) (HR = .33, p = .039)."

**Pielas et al., *Epilepsia* 2026 — infants <12 months, n=15 (PMID:42132620) [secondhand — RE-VERIFY]:** Engel I at 12 months in 53.3% overall, 46% in HME specifically; all required transfusion, one-third >1 circulating volume; 26.7% shunted; ~40% ICU stay >5 days; complications included 2 intracerebral haemorrhages and 1 intraoperative cardiac arrest; no deaths.

**Note the apparent tension between the meta-analysis (77–81% Engel I) and the single-centre series (46–53%).** The meta-analysis aggregates published series with publication bias toward good outcomes and heterogeneous follow-up; the single-centre infant series is younger, sicker, and prospectively complete. **Curate both; do not average them.**

### Morbidity, function, and quality of life

**Puka et al., *Epilepsia* 2021 — cognitive/language outcomes after hemispherectomy for HME, n=45 (PMID:34608636) [secondhand — RE-VERIFY]:**
- 68% seizure-free
- Only **43%** demonstrated average or mildly impaired cognition
- Only **26%** could "speak age appropriately"
- Only **21%** achieved satisfactory reading
- "55%, 43%, and 17% of children first babbled, spoke their first words, and started speaking in sentences at an age-appropriate period, respectively"
- Better outcomes with **right**-hemisphere surgery and **later** seizure onset
- Conclusion: children "continue to require significant language and literacy support long-term after cerebral hemispherectomy"

**This is the outcome message that matters most for a knowledge base: seizure freedom and functional recovery are only loosely coupled.** Two-thirds get seizure control; fewer than half get near-typical cognition; a quarter get fluent speech. Curate seizure outcome and developmental outcome as **separate** outcome nodes, not as one "prognosis."

Permanent expected deficits after hemispherectomy: contralateral **hemiparesis** (hand function largely lost, ambulation usually preserved) and **homonymous hemianopia** — these are accepted trade-offs, not complications.

### Complications
- **Post-hemispherectomy hydrocephalus** requiring shunt: **16–30%** across series
- Intraoperative **blood loss** (the dominant infant risk; the malformed hemisphere's vasculature is abnormal and hard to control)
- Aseptic meningitis/fever (~33%), infection (~11%), hematoma requiring evacuation (~8%), subgaleal effusion (~8%) **[secondhand — RE-VERIFY]**
- Late: superficial cerebral hemosiderosis, shunt dependence, contralateral seizure emergence

### Prognostic factors

| Favourable | Unfavourable |
|---|---|
| Unilateral (hemisphere-confined) ictal EEG | **Bilateral ictal EEG abnormality (HR 11.5)** |
| Absence of epilepsia partialis continua | Epilepsia partialis continua |
| No contralateral seizures on EEG | Contralateral EEG seizures |
| Right-hemisphere lesion (for language) | Left-hemisphere lesion |
| Later seizure onset (for cognition) | Very early / day-1 seizure onset (for cognition) |
| Complete disconnection at first surgery | Incomplete disconnection → residual seizures |
| Functional over anatomic hemispherectomy (hydrocephalus risk) | Anatomic hemispherectomy (NNT 3 for hydrocephalus) |

Note the deliberate contradiction to record: **younger age at seizure onset was *favourable* for seizure freedom in the UCLA series** (HR .29) but is *unfavourable* for cognitive outcome. Those are different endpoints, and the field genuinely disagrees on the seizure-onset-age direction. Do not collapse them.

**Prognostic biomarkers:** none molecular. Attempts to correlate specific genotype (MTOR vs PIK3CA vs DEPDC5) with surgical outcome have not produced a validated predictor. **This is a stated knowledge gap.**

---

## 12. Treatment

### 12.1 Definitive treatment — hemispheric surgery

**Hemispherectomy / hemispherotomy is the only definitive treatment for HME-related drug-resistant epilepsy.**

- **Anatomic hemispherectomy (AH):** removal of the hemisphere. Higher seizure-freedom in some series; higher hydrocephalus risk (NNT 3).
- **Functional hemispherectomy / hemispherotomy (FH):** disconnection with minimal resection; vertical (parasagittal) or lateral (peri-insular) approaches — no significant difference between them (HR = 2.59; P = .101).
- NCIT suggestions: `NCIT:C15656` **Neurosurgical Procedure** (verified) or `NCIT:C15329` **Surgical Procedure** (verified). ⚠️ **NCIt has no "Hemispherectomy" term** — I searched both the local `sqlite:obo:ncit` and live OLS and found none (MeSH `D038421` and SNOMED `14247003` do have it). Use `NCIT:C15656` with `preferred_term: cerebral hemispherectomy` and flag the ontology gap. `therapeutic_modality: SURGERY`.

### 12.2 Targeted therapy — mTOR inhibitors

The precision-medicine story, still mostly promissory but with a clear rationale and real case-level evidence.

**Agents:** sirolimus/rapamycin (`CHEBI:9168` **verified**), everolimus (`CHEBI:68478` **verified**). Both inhibit mTORC1 via FKBP12.

**Regulatory status for HME: none. Off-label everywhere.** Everolimus is approved for TSC-associated refractory focal seizures (EXIST-3) — not for HME or FCD.

**Best case-level human evidence (PMID:30514132) [secondhand — RE-VERIFY]:**
> "We report a 6-day-old female with hemimegalencephaly and frequent seizures despite 9 antiseizure medications. At 3 months of age, while awaiting hemispherectomy, an mTOR inhibitor, rapamycin, was initiated by the neurologist. After 1 week of treatment, there was >50% reduction in seizures and total seizure burden, and after 2 weeks, development improved, resulting in deferral of surgery by 2.5 months with an increased body weight. Pathology demonstrated cortical dysplasia with upregulation of the mTOR pathway. Deep-sequencing of brain tissue demonstrated 16% mosaicism for a pathogenic de novo MTOR gene mutation. This case exemplifies how mTOR inhibitors could be considered for seizure reduction in patients with hemimegalencephaly while awaiting surgery."

**The framing that matters: mTOR inhibition in HME is currently a *bridge to surgery*, not a substitute for it.** It buys weight gain and reduces perioperative risk.

**Counter-evidence to curate honestly:** in an NPRL3-associated neonatal HME case, "mTOR inhibitor therapy proved ineffective but functional hemispherectomy at 3 months of age resulted in total abatement of clinical seizures" (PMID:33749980) **[secondhand — RE-VERIFY]**. Genotype may matter — GATOR1 (amino-acid-sensing arm) lesions may not respond like activator-arm lesions.

**Trial status:** D'Gama & Poduri (PMID:34608615, **[verbatim-verified from cache]**) — "Clinical studies of mTOR inhibitors for patients with FCD and HME are just emerging and will be an exciting area in the coming years." Active/registered trials are in **FCD II**, not HME: `NCT02451696` (everolimus, brain mTOR activity in TSC and FCD, US, phase II open-label) and `NCT03198949` (everolimus in FCD II, Korea, randomized double-blind placebo-controlled crossover phase II). Also `NCT03646240` (ABI-009 / nab-rapamycin, RaSuRE, surgically-refractory epilepsy). **No HME-specific registered trial was identified.**

**Cautions from the same review [verbatim-verified from cache]:** "the long-term effects of early and potentially lifelong treatment with such broad inhibitors on immunosuppression, growth, and development, particularly neurodevelopment and sexual maturation, remain unclear and should prompt caution."

**NCIT/CHEBI pattern:**
```yaml
- name: Sirolimus (mTOR inhibitor)
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: Targeted Therapy
    term: {id: NCIT:C93352, label: Targeted Therapy}   # verified
    therapeutic_agent:
    - preferred_term: sirolimus
      term: {id: CHEBI:9168, label: sirolimus}          # verified
  target_mechanisms: ...  # INHIBITS the "Constitutive mTORC1 Activation" node
```

### 12.3 Antiseizure medications

Empiric and largely ineffective as monotherapy — that is the definition of the disease. Agents used: vigabatrin (`CHEBI:63638` **verified**; first-line for spasms, retinal toxicity risk), ACTH/corticosteroids for spasms, levetiracetam (`CHEBI:6437` **verified**), phenobarbital, topiramate, carbamazepine/oxcarbazepine, clobazam, cannabidiol, felbamate. The 2026 TAE series reports patients "required a median of 8 antiseizure medications during hospitalization" **[secondhand — RE-VERIFY]** — a number that speaks for itself.
- NCIT: `NCIT:C15986` Pharmacotherapy (**verified**), `therapeutic_modality: SMALL_MOLECULE`.

### 12.4 Emerging: staged transarterial embolization ("endovascular hemispherectomy")

A genuinely novel 2023–2026 development, worth a dedicated treatment node.
- **Concept:** devascularize the malformed hemisphere endovascularly in stages, in neonates too small or unstable for open surgery.
- PMID:36302639 (*J Neurointerv Surg* 2023): three infants aged 13 days–13 weeks; "all infants" remained "seizure-free to date" at 8–57 months follow-up **[secondhand — RE-VERIFY]**
- PMID:42208165 (*Pediatr Neurol* 2026, n=8): mean seizure onset 9 days, first embolization ~50 days, 3–5 staged procedures; at discharge 75% achieved electrographic seizure freedom from the affected hemisphere; ASM burden fell from median 8 to median 4 **[secondhand — RE-VERIFY]**
- A 2025 comparative study (TAE n=12 vs surgical hemispherectomy n=11) reported 6/8 (75%) seizure-free among TAE-primary patients **[secondhand — RE-VERIFY]**
- PMID:40425282 (2026): complication analysis and evolution of strategy in infants <3 months
- Applied even to TSC-related HME (PMID:41489603)
- NCIT: `NCIT:C15656` Neurosurgical Procedure or an interventional-radiology term; `therapeutic_modality: DEVICE` or `SURGERY`.

**Evidence caveat for curation:** this is single-institution, small-N, non-randomized, and short-follow-up. Curate as EMERGING, not established.

### 12.5 Supportive, dietary, and rehabilitative

- **Ketogenic diet** — `NCIT:C173168` **Ketogenic Diet** (verified); mechanistically attractive given the pS6/pAkt reduction seen in ketogenic-fed rats. `therapeutic_modality: BEHAVIORAL`.
- **Vagus nerve stimulation** — palliative; note NCIt's nearest verified term is `NCIT:C203750` *Transcutaneous Auricular* VNS, which is **not** implanted VNS — do not use it for implanted VNS. Ontology gap.
- **Physical / occupational / speech therapy** — `NCIT:C15302` Physical Therapy (verified), `NCIT:C121351` occupational therapy, `NCIT:C159273` speech therapy. `therapeutic_modality: BEHAVIORAL`.
- **Supportive care** — `NCIT:C15747` Supportive Care (verified).
- **Genetic counseling** — `NCIT:C15240` Genetic Counseling (verified). Essential specifically to distinguish the sporadic-somatic majority from the germline-predisposed minority.

### 12.6 Not applicable / no evidence
Gene therapy, gene editing, cell therapy, RNA therapeutics (ASO/siRNA), immunotherapy, and monoclonal antibodies: **no HME programmes.** Conceptually, an allele-selective approach is nearly impossible here — the lesion is built before birth and the pathological cells are structurally integrated. Correcting the genotype postnatally would not un-build the hemisphere. This is a mechanistically principled therapeutic ceiling worth stating in the entry.

### 12.7 Pharmacogenomics
- **Genotype-guided** in the loosest sense: an identified mTOR-activator variant is the rationale for rapalog use. There is no validated PharmGKB/CPIC pharmacogenomic guidance for HME.
- Practical PGx note: sirolimus/everolimus are **CYP3A4/P-gp** substrates and interact substantially with enzyme-inducing ASMs (carbamazepine, phenytoin, phenobarbital) — a real, curatable drug–drug interaction in exactly this patient population.

### 12.8 Treatment algorithm (synthesized)

1. Neonatal seizures + characteristic MRI → diagnose HME; video-EEG to establish lateralization
2. Trial ASMs (vigabatrin/ACTH if spasms) — expect failure
3. **Refer to a paediatric epilepsy surgery centre early.** Delay costs development.
4. If too small/unstable for open surgery: consider mTOR inhibitor as a **bridge**, and/or staged transarterial embolization at experienced centres
5. **Hemispherotomy (functional) as first surgical management** — the meta-analysis favours it on hydrocephalus grounds at equivalent seizure outcome
6. Send resected tissue for **deep sequencing + pS6 IHC**; send blood for germline testing
7. Lifelong rehabilitation, education support, and — given the caregiver-burden data — family support that does not stop when the seizures do

---

## 13. Prevention

- **Primary prevention: none possible.** A spontaneous postzygotic mutation in embryogenesis is not preventable by any known intervention. Vaccination, diet, exposure avoidance — all not applicable. State this plainly rather than leaving the section empty.
- **Secondary prevention (the real content of this section): early surgical intervention to prevent epileptic encephalopathy.** The whole "buy time, then operate early" strategy — mTOR inhibitor bridging, staged embolization — is secondary prevention of developmental catastrophe. The TSC precedent (EPISTOP, PMID data in D'Gama & Poduri) that pre-emptive vigabatrin on EEG-epileptiform-activity *before clinical seizures* delays seizure onset and reduces refractory epilepsy at 2 years is the model. **It has not been tested in HME**, but prenatally diagnosed HME is precisely the situation where such a design becomes thinkable. Flag as a proposed experiment.
- **Tertiary prevention:** seizure control, aspiration/nutrition management, orthopaedic and spasticity management for the hemiparesis, shunt surveillance post-surgery, developmental and educational support.
- **Immunization:** not applicable to disease causation; standard childhood schedule applies, with the caveat that **live vaccines are contraindicated on mTOR inhibitors**.
- **Screening:** no population or newborn screening. **Cascade genetic screening is indicated only in the germline-predisposition subset** (TSC1/TSC2/DEPDC5/NPRL2/NPRL3).
- **Genetic counselling (`NCIT:C15240`):** the core preventive service. Key messages: (a) for isolated somatic HME, recurrence risk is near-baseline; (b) germline mosaicism cannot be formally excluded; (c) if a germline predisposing allele is found, the counselling flips entirely to autosomal dominant with 50% transmission and the option of prenatal/preimplantation testing for the *predisposition* (not for HME itself, which requires the unpredictable second hit).
- **Prenatal testing:** fetal MRI/ultrasound can detect the lesion; molecular prenatal diagnosis is not feasible for a brain-restricted somatic variant (amniocytes and CVS won't carry it).
- **Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy of naturally affected species:** *Homo sapiens* (`NCBITaxon:9606`) only, as far as the literature shows.
- **Naturally occurring HME in animals: not documented.** I searched specifically for canine/feline/veterinary hemimegalencephaly and found **no case reports**. Veterinary neurology does describe unilateral cerebral abnormalities (porencephaly, hydranencephaly, hydrocephalus) in dogs and cats, but these are **destructive/cavitary lesions, not hemispheric overgrowth**, and are mechanistically unrelated. **OMIA has no HME entry.**
  - *Reason this is unsurprising:* HME requires a somatic mutation in a large-brained, long-corticogenesis species, and would require deliberate imaging of a neonate with seizures — an ascertainment pipeline that barely exists in veterinary practice.
- **Orthologous genes** (for model-organism curation): mouse *Mtor* (NCBI Gene 56717), *Pik3ca* (18706), *Akt3* (23797), *Akt1* (11651), *Rheb* (19744), *Tsc1* (64930), *Tsc2* (22084), *Depdc5* (277854), *Pten* (19211). The PI3K–AKT–mTOR module is deeply conserved from yeast (TOR1/TOR2) onward — one of the most conserved growth-control circuits in eukaryotes.
- **Comparative pathology:** engineered rodent models reproduce cytomegaly, dyslamination, migration failure, and seizures (§15), but *no* rodent model reproduces **hemisphere-scale unilateral overgrowth**, because the lissencephalic mouse cortex lacks the outer subventricular zone and outer radial glia that drive human cortical expansion. **This is a textbook `HUMAN_MODEL_MISMATCH`, and should be curated as one.**
- **Zoonotic potential / cross-species transmission:** not applicable.
- **Breed (VBO):** not applicable.

---

## 15. Model Organisms

### 15.1 Mouse — in utero electroporation (the workhorse)

The dominant paradigm: electroporate a mutant construct into a subset of dorsal telencephalic progenitors at ~E14.5, thereby **manufacturing mosaicism on purpose**. Elegant, because it models the *mechanism of the mechanism* — a clone, not an organism.

From D'Gama & Poduri (PMID:34608615) **[verbatim-verified from cache]**:
> "In utero electroporation of the variant that results in the Akt3 E17K substitution leads to abnormal cortical architecture, cytomegalic neurons, abnormal neuronal migration, and electrographic seizures that are rescued when rapamycin is administered prenatally but not postnatally."
> "Prenatal conditional expression of Pik3ca mutations leads to megalencephaly, abnormal cortical architecture, cytomegalic neurons, and seizures, and acute postnatal treatment with the PI3K inhibitor BKM120 suppressed seizures."
> "In utero electroporation of the variant that results in Mtor L2427P leads to abnormal neuronal migration, cytomegalic neurons, and spontaneous seizures, and postnatal rapamycin suppressed cytomegalic neurons and seizures."
> "In utero electroporation of the variant that results in Rheb Y35L leads to abnormal neuronal migration, cytomegalic neurons, and seizures, and postnatal rapamycin significantly reduced seizure frequency."

**The AKT3 timing result is the single most important preclinical finding in this disease, and it cuts against the therapeutic hope:** prenatal rapamycin rescues the malformation; postnatal rapamycin does not. Reported specifics: rapamycin 3 mg/kg/day E15.5–E18.5 rescued cortical malformation and cytomegaly; P1–P3 dosing did not, with spontaneous seizures at ~P28 **[secondhand — RE-VERIFY]**. Curate this as a `HUMAN_MODEL_MISMATCH` or at minimum as an explicit caveat on the mTOR-inhibitor treatment node: **the structural lesion may have a closed therapeutic window that the seizures do not.**

### 15.2 Mouse — conditional / knockout models of repressors

Also from PMID:34608615 **[verbatim-verified from cache]**:
> "Conditional knockout of Pten in neurons leads to megalencephaly, cytomegalic neurons, and seizures, and rapamycin suppressed seizures, including in older mice with established epilepsy."
> "Depdc5+/− rats have cytomegalic neurons and balloon-like cells (Depdc5−/− models are embryonic lethal), and prenatal rapamycin suppressed the abnormal cells."
> "Focal mosaic knockout of Depdc5 in mouse brain leads to abnormal cortical lamination, balloon-like cells, and spontaneous epilepsy, and prenatal rapamycin rescued neuronal migration defects."
> "Conditional knockout of Depdc5 in neurons leads to megalencephaly, cytomegalic neurons, and seizures, and postnatal chronic rapamycin prolonged survival and decreased brain size and neuronal soma size."

Note the interesting inversion: in **Pten** models, rapamycin works even in **older mice with established epilepsy** — unlike the AKT3 electroporation result. Genotype-dependent therapeutic windows are a live hypothesis.

### 15.3 Mouse — lineage-restricted conditional activation

D'Gama 2017: conditional *Pik3ca* activation showing that mTOR activation "in excitatory neurons and glia, but not interneurons, is sufficient for abnormal cortical overgrowth." **[secondhand — RE-VERIFY]** The key cell-type-attribution experiment.

Also from PMID:34608615 **[verbatim-verified from cache]**: "Single cell studies of human brain tissue resected in the course of clinical treatment and mouse studies have suggested that abnormal hyperactivation of the mTOR pathway in neurons is necessary for disease pathogenesis, and further that such hyperactivation in the excitatory neuron lineage is necessary and in some cases sufficient."

### 15.4 Rat
`Depdc5+/−` rats (see above). Also PI3K/mTOR inhibition preventing ictal activity and cell death in rat hippocampal organotypic post-traumatic epilepsy cultures (Crino, PMID:26060899) — relevant to mechanism, not to HME specifically.

### 15.5 Human cortical organoids (iPSC/ESC) — the model that addresses the mouse's biggest limitation

**Zhang et al., *BBA Mol Basis Dis* 2024 (PMID:38759814) [secondhand — RE-VERIFY]:**
> "Focal malformations of cortical development (FMCDs) are brain disorders mainly caused by hyperactive mTOR signaling due to both inactivating and activating mutations of genes in the PI3K-AKT-mTOR pathway."
> "mosaic and somatic expression of AKT3 activating mutations in cortical organoids mimicking the disease presentation with overproliferation and the formation of dysmorphic neurons"

The study also reports an **allelic-strength gradient**: stronger AKT3 activating mutations → more severe migratory and overgrowth defects. That is the *in vitro* counterpart of the human VAF-severity relationship, from a different direction.

**Why organoids matter here specifically:** they carry human oRG/OSVZ biology that mice lack, which is exactly the biology that scales a human hemisphere. But they lack vasculature, immune cells, a full developmental timeline, and — critically for an epilepsy — mature circuits and behaviour. **Neither model alone can carry a claim about human HME.**

### 15.6 Model characteristics summary

| Model | Recapitulates | Fails to recapitulate |
|---|---|---|
| Mouse IUE (Akt3/Pik3ca/Mtor/Rheb) | mosaicism, cytomegaly, dyslamination, migration failure, spontaneous seizures, rapamycin response | **hemisphere-scale unilateral overgrowth**; gyrification; human oRG/OSVZ expansion; human seizure semiology |
| Mouse conditional KO (Pten/Depdc5/Tsc1/Tsc2) | megalencephaly, cytomegaly, balloon-like cells, epilepsy, drug response | focality/mosaicism (unless focal-mosaic KO used); unilaterality |
| Depdc5+/− rat | cytomegalic neurons, balloon-like cells | homozygotes embryonic lethal; limited epilepsy phenotype |
| Human cortical organoids (AKT3, PIK3CA) | human progenitor biology, over-proliferation, dysmorphic neurons, allelic dose-response | vasculature, immunity, circuits, seizures, full timeline |
| **No model** | — | **the unilateral, hemisphere-restricted geometry that names the disease** |

### 15.7 Resources
MGI (`Mtor`, `Pik3ca`, `Akt3`, `Pten`, `Depdc5`, `Tsc1`, `Tsc2` alleles), IMPC/KOMP, IMSR, RGD (Depdc5 rat), Alliance of Genome Resources, Addgene (AKT3 E17K, MTOR, RHEB constructs), Cellosaurus (engineered hESC/iPSC lines from the organoid work).

---

## Appendix A — Verified ontology terms (checked this session against local OAK adapters)

**Confirmed correct (label matches exactly):**

| CURIE | Label | Adapter |
|---|---|---|
| `MONDO:0020492` | hemimegalencephaly | `sqlite:obo:mondo` |
| `HP:0007206` | Hemimegalencephaly | `sqlite:obo:hp` |
| `HP:0001355` | Megalencephaly | `sqlite:obo:hp` |
| `HP:0001250` | Seizure | `sqlite:obo:hp` |
| `HP:0011097` | Epileptic spasm | `sqlite:obo:hp` |
| `HP:0011182` | Interictal epileptiform activity | `sqlite:obo:hp` |
| `HP:0002376` | Developmental regression | `sqlite:obo:hp` |
| `HP:0001249` | Intellectual disability | `sqlite:obo:hp` |
| `HP:0000256` | Macrocephaly | `sqlite:obo:hp` |
| `HP:0001344` | Absent speech | `sqlite:obo:hp` |
| `HP:0007370` | Aplasia/Hypoplasia of the corpus callosum | `sqlite:obo:hp` |
| `HP:0002269` | Abnormality of neuronal migration | `sqlite:obo:hp` |
| `HP:0002119` | Ventriculomegaly | `sqlite:obo:hp` |
| `GO:0031929` | TOR signaling | `sqlite:obo:go` |
| `GO:0032008` | positive regulation of TOR signaling | `sqlite:obo:go` |
| `GO:0032006` | regulation of TOR signaling | `sqlite:obo:go` |
| `GO:0038202` | TORC1 signaling | `sqlite:obo:go` |
| `GO:0043491` | phosphatidylinositol 3-kinase/protein kinase B signal transduction | `sqlite:obo:go` |
| `GO:0001764` | neuron migration | `sqlite:obo:go` |
| `GO:0021814` | cell motility involved in cerebral cortex radial glia guided migration | `sqlite:obo:go` |
| `GO:0016049` | cell growth | `sqlite:obo:go` |
| `GO:0008283` | cell population proliferation | `sqlite:obo:go` |
| `GO:0021987` | cerebral cortex development | `sqlite:obo:go` |
| `GO:0007420` | brain development | `sqlite:obo:go` |
| `GO:0006412` | translation | `sqlite:obo:go` |
| `GO:0006914` | autophagy | `sqlite:obo:go` |
| `GO:0045595` | regulation of cell differentiation | `sqlite:obo:go` |
| `CL:0000681` | radial glial cell | `sqlite:obo:cl` |
| `CL:0011020` | neural progenitor cell | `sqlite:obo:cl` |
| `CL:0000679` | glutamatergic neuron | `sqlite:obo:cl` |
| `CL:0000598` | pyramidal neuron | `sqlite:obo:cl` |
| `CL:0000127` | astrocyte | `sqlite:obo:cl` |
| `CL:0000128` | oligodendrocyte | `sqlite:obo:cl` |
| `CL:0000617` | GABAergic neuron | `sqlite:obo:cl` |
| `UBERON:0001869` | cerebral hemisphere | `sqlite:obo:uberon` |
| `UBERON:0000956` | cerebral cortex | `sqlite:obo:uberon` |
| `UBERON:0002285` | telencephalic ventricle | `sqlite:obo:uberon` |
| `UBERON:0002316` | white matter | `sqlite:obo:uberon` |
| `UBERON:0002336` | corpus callosum | `sqlite:obo:uberon` |
| `CHEBI:9168` | sirolimus | `sqlite:obo:chebi` |
| `CHEBI:68478` | everolimus | `sqlite:obo:chebi` |
| `CHEBI:63638` | vigabatrin | `sqlite:obo:chebi` |
| `CHEBI:6437` | levetiracetam | `sqlite:obo:chebi` |
| `NCIT:C15986` | Pharmacotherapy | `sqlite:obo:ncit` |
| `NCIT:C93352` | Targeted Therapy | `sqlite:obo:ncit` |
| `NCIT:C15656` | Neurosurgical Procedure | `sqlite:obo:ncit` |
| `NCIT:C15329` | Surgical Procedure | `sqlite:obo:ncit` |
| `NCIT:C173168` | Ketogenic Diet | `sqlite:obo:ncit` |
| `NCIT:C15302` | Physical Therapy | `sqlite:obo:ncit` |
| `NCIT:C15240` | Genetic Counseling | `sqlite:obo:ncit` |
| `NCIT:C15747` | Supportive Care | `sqlite:obo:ncit` |
| `NCIT:C15447` | Dietary Intervention | `sqlite:obo:ncit` |

**Do NOT use:**
- `GO:0014065` — **OBSOLETE** ("obsolete phosphatidylinositol 3-kinase signaling"). Use `GO:0043491`.
- `NCIT:C177779` as a hemimegalencephaly mapping — it resolves to **"MCAP Syndrome"**, a different entity, despite MONDO xref-ing it. Verify against live NCIt and consider an upstream MONDO issue.
- `NCIT:C203750` for implanted vagus nerve stimulation — it is *Transcutaneous Auricular* VNS.

**Ontology gaps identified:**
1. No CL term for **balloon cell** or **dysmorphic/cytomegalic neuron** — the defining cells of this disease.
2. No HP term for **hemihypsarrhythmia**.
3. No NCIt term for **hemispherectomy** (MeSH `D038421` and SNOMED `14247003` have it).
4. No HPO mode-of-inheritance term for **somatic mosaicism / postzygotic non-heritable** — a systematic problem for every mosaic disease in the KB, not just this one.

---

## Appendix B — Citation index

| PMID | Citation | Verification status |
|---|---|---|
| 22500628 | Poduri A et al. Somatic activation of AKT3 causes hemispheric developmental brain malformations. *Neuron* 2012;74:41-8 | abstract verbatim-verified via raw efetch |
| 22729223 | Lee JH et al. De novo somatic mutations in components of the PI3K-AKT3-mTOR pathway cause hemimegalencephaly. *Nat Genet* 2012;44:941-5. doi:10.1038/ng.2329 | **cached in repo**, verbatim-verified |
| 22729224 | Rivière JB et al. De novo germline and postzygotic mutations in AKT3, PIK3R2 and PIK3CA cause a spectrum of related megalencephaly syndromes. *Nat Genet* 2012;44:934-40. doi:10.1038/ng.2331 | secondhand — RE-VERIFY |
| 25599672 | D'Gama AM et al. Mammalian target of rapamycin pathway mutations cause hemimegalencephaly and focal cortical dysplasia. *Ann Neurol* 2015;77:720-5 | abstract verbatim-verified via raw efetch |
| 25722288 | Jansen LA et al. PI3K/AKT pathway mutations cause a spectrum of brain malformations from megalencephaly to focal cortical dysplasia. *Brain* 2015 | secondhand — RE-VERIFY |
| 26060899 | Crino PB. Focal Cortical Dysplasia. *Semin Neurol* 2015;35:201-8 | **cached in repo (full text)**, verbatim-verified |
| 28377884 | Evolution of epilepsy in hemimegalencephaly from infancy to adulthood. *Epilepsy Behav Case Rep* 2017 | secondhand — RE-VERIFY |
| 29281825 | D'Gama AM et al. Somatic Mutations Activating the mTOR Pathway in Dorsal Telencephalic Progenitors Cause a Continuum of Cortical Dysplasias. *Cell Rep* 2017 | secondhand — RE-VERIFY |
| 30514132 | mTOR Inhibitors as a New Therapeutic Strategy in Treatment Resistant Epilepsy in Hemimegalencephaly: A Case Report. *J Child Neurol* 2019 | secondhand — RE-VERIFY |
| 31444548 | Baldassari S et al. Dissecting the genetic basis of focal cortical dysplasia: a large cohort study. *Acta Neuropathol* 2019 | abstract verbatim-verified via raw efetch |
| 33387903 | Hemimegalencephaly and tuberous sclerosis complex: A rare yet challenging association. *Eur J Paediatr Neurol* 2021 | secondhand — RE-VERIFY |
| 33738444 | Cerebrospinal fluid liquid biopsy for detecting somatic mosaicism in brain. *Brain Commun* 2021 | secondhand — RE-VERIFY |
| 33749980 | Hemimegalencephaly and intractable seizures associated with the NPRL3 gene variant in a newborn. *Am J Med Genet A* 2021 | secondhand — RE-VERIFY |
| 34608615 | D'Gama AM, Poduri A. Precision Therapy for Epilepsy Related to Brain Malformations. *Neurotherapeutics* 2021;18:1548-63 | **cached in repo (full text)**, verbatim-verified |
| 34608636 | Puka K et al. Functional cognitive and language outcomes after cerebral hemispherectomy for hemimegalencephaly. *Epilepsia* 2021;62:2932-40 | secondhand — RE-VERIFY |
| 35022853 | Hemispherectomy for hemimegalencephaly in a 6.5-week-old infant with TSC. *Childs Nerv Syst* 2022 | secondhand — RE-VERIFY |
| 36302639 | Definitive treatment of seizures due to hemimegalencephaly … by transarterial embolization. *J Neurointerv Surg* 2023 | secondhand — RE-VERIFY |
| 36325654 | Itoh M et al. Somatic mosaicism of the PI3K-AKT-MTOR pathway is associated with hemimegalencephaly in fetal brains. *Neuropathology* 2023 | secondhand — RE-VERIFY |
| 37149062 | Gerasimenko A, Baldassari S, Baulac S. mTOR pathway: Insights into an established pathway for brain mosaicism in epilepsy. *Neurobiol Dis* 2023;182:106144 | **cached in repo**, verbatim-verified |
| 37873610 | Goel K et al. Hemispheric epilepsy surgery for hemimegalencephaly: The UCLA experience. *Epilepsia* 2024 | secondhand — RE-VERIFY |
| 37975663 | Goel K et al. Hemimegalencephaly: A Systematic Comparison of Functional and Anatomic Hemispherectomy for Drug-Resistant Epilepsy. *Neurosurgery* 2024;94:666-78 | **cached in repo**, verbatim-verified |
| 38617140 | Prenatal diagnosis of hemimegalencephaly via transabdominal and transvaginal ultrasonography. *Quant Imaging Med Surg* 2024 | secondhand — RE-VERIFY |
| 38759814 | A spectrum of AKT3 activating mutations cause focal malformations of cortical development in cortical organoids. *BBA Mol Basis Dis* 2024;1870:167232 | secondhand — RE-VERIFY |
| 39454530 | Facial infiltrating lipomatosis with contralateral hemimegalencephaly. *Seizure* 2024 | secondhand — RE-VERIFY |
| 39641771 | Macdonald-Laurs E et al. ILAE genetic literacy series: Focal cortical dysplasia. *Epileptic Disord* 2025 | secondhand — RE-VERIFY |
| 39926610 | The genetic landscape and classification of infantile epileptic spasms syndrome requiring surgery due to suspected focal brain malformations. *Brain Commun* 2025 | abstract verbatim-verified via raw efetch |
| 39973610 | Gelot A et al. Cytomegalic parvalbumin neurons in fetal cases of hemimegalencephaly. *Epilepsia* 2025 | **no abstract obtained** — RE-VERIFY |
| 40344425 | Uncrossed Cerebellar Diaschisis in Hemimegalencephaly: FDG-PET and DTI. *Int J Dev Neurosci* 2025 | secondhand — RE-VERIFY |
| 40425282 | Transarterial embolization for infants under 3 months … complication analysis. *J Neurointerv Surg* 2026 | secondhand — RE-VERIFY |
| 41033188 | Clinical and radiological evaluation of children with hemimegalencephaly and epilepsy: A single-center study. *Seizure* 2025 | secondhand — RE-VERIFY |
| 41489603 | Hemispheric endovascular embolization in an infant with TSC-related hemimegalencephaly. *Seizure* 2026 | secondhand — RE-VERIFY |
| 42024976 | A novel PTEN variant causing hemimegalencephaly and focal nodular heterotopias in the developing human brain. *Epilepsia* 2026 | secondhand — RE-VERIFY |
| 42132620 | Pielas M et al. Hemispheric surgery for hemimegalencephaly and hemispheric cortical dysplasia in infants below 12 months of age. *Epilepsia* 2026 | secondhand — RE-VERIFY |
| 42208165 | Seizure Burden and Management in Infants With Hemimegalencephaly Prestaged and Poststaged Transarterial Embolization. *Pediatr Neurol* 2026 | secondhand — RE-VERIFY |

**Structured-source references also citable:** `ORPHA:99802` (Orphanet disorder record — definition, epidemiology class, phenotype table).

**Registered trials referenced:** `NCT02451696` (everolimus, TSC & FCD, phase II), `NCT03198949` (everolimus in FCD II, phase II crossover), `NCT03646240` (ABI-009/nab-rapamycin, RaSuRE), `NCT01713946` (EXIST-3, TSC — context only), `NCT02098759` (EPISTOP, TSC — context only). **No HME-specific interventional trial identified.**

---

## Appendix C — Stated knowledge gaps (candidates for `discussions:` blocks)

1. **`KNOWLEDGE_GAP` — no population prevalence or incidence for HME.** The only circulating figure (1–3 per 1,000 children *with epilepsy*) has an epilepsy denominator and cannot be converted to a population rate.
2. **`KNOWLEDGE_GAP` — the genetic literature is ascertained entirely through surgery.** Non-operated and milder HME is molecularly unsampled; the true genotype spectrum and the true "unsolved" fraction are unknown.
3. **`HUMAN_MODEL_MISMATCH` — no animal model reproduces unilateral hemisphere-scale overgrowth.** Rodents lack the outer subventricular zone / outer radial glia biology that scales the human cortex, so every mouse result about *magnitude* of overgrowth is of uncertain human validity. Proposed resolution: human cortical organoid and assembloid models with mosaic mutation induction at defined developmental stages; comparative ferret/primate work.
4. **`HUMAN_MODEL_MISMATCH` — interneuron involvement.** Mouse conditional-activation data say mTOR activation in interneurons is *not* sufficient for overgrowth (D'Gama 2017); human fetal pathology shows cytomegalic parvalbumin interneurons (Gelot 2025). Proposed resolution: single-nucleus multiome of human HME tissue with lineage-resolved variant calling.
5. **`KNOWLEDGE_GAP` — closed therapeutic window for the structural lesion.** Prenatal rapamycin rescues the Akt3-E17K malformation in mice; postnatal does not. Whether postnatal mTOR inhibition in humans can do anything beyond seizure suppression is unresolved, and it determines whether "precision therapy for HME" means disease modification or symptom control.
6. **`KNOWLEDGE_GAP` — no genotype-outcome predictor.** Whether MTOR- vs PIK3CA- vs DEPDC5-associated HME differ in surgical outcome, mTOR-inhibitor responsiveness, or developmental trajectory has not been tested with adequate power. The NPRL3 non-response case (PMID:33749980) hints that the amino-acid-sensing arm may behave differently.
7. **`KNOWLEDGE_GAP` — no HME-specific quality-of-life instrument, and caregiver burden does not improve with seizure freedom.** The seizure-outcome literature and the family-outcome literature barely touch.
8. **`KNOWLEDGE_GAP` — no validated non-invasive molecular diagnostic.** CSF cfDNA sensitivity is low (3/12 in one series); depth-electrode DNA is preprint-stage. Until one works, molecular diagnosis requires removing the hemisphere first, which is diagnostically backwards.