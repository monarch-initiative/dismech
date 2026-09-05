---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-08T17:58:08.355602'
end_time: '2026-08-08T18:12:35.785564'
duration_seconds: 867.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Isolated Sedoheptulokinase Deficiency
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
  - claude-opus-5
  web_search_requests: 9
  num_turns: 65
  total_cost_usd: 5.109532000000001
  session_id: bac4a9b1-540e-436e-96a1-291f477439ec
  stop_reason: end_turn
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isolated Sedoheptulokinase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Isolated Sedoheptulokinase Deficiency** covering all of the
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

# Isolated Sedoheptulokinase Deficiency (SHPK Deficiency) — Comprehensive Research Report

**Prepared:** 2026-08-08 · **Target:** Isolated sedoheptulokinase deficiency · **MONDO:0014969** · Category: Mendelian (autosomal recessive inborn error of metabolism)

---

## ⚠️ Framing note for knowledge-base curation (read first)

This is an unusual entry: **the existence of a clinical disease is explicitly disputed in the defining primary literature.** The only paper reporting isolated (non-contiguous-gene) SHPK deficiency is titled *"First two unrelated cases of isolated sedoheptulokinase deficiency: **A benign disorder?**"* and states verbatim:

> "It is questionable whether SHPK deficiency is a causal factor for the clinical phenotypes of our patients. This study illustrates the necessity of extensive functional and clinical workup for interpreting a novel variant, including nonsense variants."
> — Wamelink et al., *J Inherit Metab Dis* 2015 ([PMID:25647543](https://pubmed.ncbi.nlm.nih.gov/25647543/))

Three independent lines of evidence support the "benign biochemical phenotype" reading: (i) the two reported patients had **discordant, non-overlapping** clinical presentations; (ii) `SHPK` loss-of-function alleles are present in population databases at frequencies **higher than expected for a pathogenic recessive allele**; (iii) `Shpk^-/-` mice reproduce the *biochemical* abnormality with **no clinical or histological phenotype**. Every clinical phenotype below should be curated with that caveat attached, and any `supports:` field should reflect the uncertainty rather than asserting causation.

Also flagged for curators: **no ontology term ID in this report has been passed through `just validate-terms`.** IDs marked ✅ were retrieved directly from the authoritative source (OLS4/ChEBI, HPO API, UniProt, NCBI); IDs marked ⚠️ are suggestions requiring OAK verification before commit.

---

## 1. Disease Information

### 1.1 Overview

Isolated sedoheptulokinase deficiency is an autosomal recessive inborn error of the **non-oxidative branch of the pentose phosphate pathway (PPP)** caused by biallelic loss-of-function variants in `SHPK` (formerly `CARKL`). The enzyme sedoheptulokinase (EC 2.7.1.14) phosphorylates free sedoheptulose to sedoheptulose-7-phosphate; its loss produces a characteristic urinary metabolite signature — **elevated sedoheptulose and elevated erythritol, with low-to-normal sedoheptulose-7-phosphate**.

Orphanet definition (verbatim, ORPHA:440713):

> "A rare, hereditary disorder of pentose phosphate metabolism characterized by increased urine levels of sedoheptulose and erythritol, and low-to-normal excretion of sedoheptulose-7P."

The term **"isolated"** is load-bearing. Sedoheptulokinase deficiency occurs far more often as part of a **contiguous gene deletion**: the common 57-kb founder deletion causing nephropathic cystinosis removes `CTNS` *and* the adjacent `SHPK`, plus the 5′ non-coding exons of `TRPV1` ([PMID:18186520](https://pubmed.ncbi.nlm.nih.gov/18186520/), [PMID:21546516](https://pubmed.ncbi.nlm.nih.gov/21546516/)). "Isolated" SHPK deficiency = SHPK loss **without** concurrent CTNS loss, and has been reported in only **two patients worldwide**.

### 1.2 Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| OMIM (phenotype) | **#617213** | SEDOHEPTULOKINASE DEFICIENCY; SHPKD |
| OMIM (gene) | ***605060** | SEDOHEPTULOKINASE; SHPK |
| Orphanet | **ORPHA:440713** | "Isolated sedoheptulokinase deficiency" |
| MONDO | **MONDO:0014969** ✅ | Exact match to both OMIM:617213 and ORPHA:440713 |
| UMLS / MedGen | **C1291373** ✅ | |
| ICD-10 | **E74.8** | Orphanet mapping type NTBT (disease is *narrower than* the code) |
| ICD-11 | **5C51.0** | NTBT |
| GARD | 18652 | |
| MeSH | *none* | No dedicated MeSH descriptor; no MedDRA or GARD cross-reference in the Orphanet cross-referencing record |
| GeneReviews | *none* | No chapter exists |

Source for the cross-reference set: Orphadata `rd-cross-referencing` API for ORPHA:440713 (CC-BY-4.0).

### 1.3 Synonyms

- Isolated SHPK deficiency
- Sedoheptulokinase deficiency (SHPKD)
- Deficiency of sedoheptulokinase / deficiency of heptulokinase
- CARKL deficiency (historic gene name: *carbohydrate kinase-like*)
- SHK deficiency

### 1.4 Nature of the evidence base

**Individual case reports only** — there is no registry, no cohort, and no EHR-derived dataset. A targeted PubMed query (`SHPK[TIAB] OR sedoheptulokinase[TIAB]` AND `deficiency/patient[TIAB]`) returns exactly **5 records**, of which only one (PMID:25647543) reports isolated human disease. Aggregated resources (Orphanet, OMIM, GARD, MedGen) all trace back to that single 2015 paper. The much larger body of human data comes from **cystinosis patients homozygous for the 57-kb deletion**, in whom SHPK deficiency is a secondary, co-deleted trait.

---

## 2. Etiology

### 2.1 Causal factors

**Genetic, monogenic, autosomal recessive.** Two mechanisms produce SHPK deficiency:

**(a) Isolated SHPK deficiency** — biallelic intragenic loss-of-function variants in `SHPK` (17p13.2). Both reported patients were **homozygous for a nonsense variant**, and both came from families with consanguinity:

> "Both patients had elevated excretion of erythritol and sedoheptulose, and each had a homozygous nonsense mutation in SHPK." ([PMID:25647543](https://pubmed.ncbi.nlm.nih.gov/25647543/))

**(b) Contiguous-gene ("non-isolated") SHPK deficiency** — homozygous 57-kb deletion at 17p13.2 removing `CTNS` + `SHPK` (± `TRPV1` 5′ exons). This is *cystinosis with secondary SHPK deficiency*, not this disease entity, and should be curated on the cystinosis entry with a cross-reference:

> "Cystinosis patients with the common 57-kb deletion had strongly elevated urinary concentrations of sedoheptulose (28-451 mmol/mol creatinine; controls and other cystinosis patients <9) and erythritol (234-1110 mmol/mol creatinine; controls and other cystinosis patients <148)." ([PMID:18186520](https://pubmed.ncbi.nlm.nih.gov/18186520/))

### 2.2 Genetic risk factors

- **Causal variants:** `NM_013276.4:c.355C>T` (p.Arg119Ter) and `NM_013276.4:c.211G>T` (p.Glu71Ter) — see §4.
- **Consanguinity** is the dominant risk factor in both reported families (see §9).
- **No susceptibility loci, GWAS signals, or modifier genes are known.** No GWAS Catalog association exists for `SHPK` with this phenotype.
- Note the inverse relationship: `SHPK` has itself been *proposed as a modifier of the cystinosis phenotype* (NCBI Gene summary for GeneID 23729: "The gene resides in a chromosomal region frequently deleted in cystinosis patients, potentially serving as a disease modifier"). That hypothesis has now been **tested and not supported** for the HSPC/macrophage axis (§15).

### 2.3 Environmental risk factors

**None identified.** No toxin, occupational, infectious, or lifestyle exposure has been associated. Age, sex, and family history other than consanguinity carry no reported effect.

One mechanistically plausible (but unstudied in humans) modifier: **dietary sedoheptulose intake**, since the accumulating substrate is partly diet-derived:

> "Testing plant extracts revealed sedoheptulose presence in carrots and fruits." ([PMID:18775706](https://pubmed.ncbi.nlm.nih.gov/18775706/))

### 2.4 Protective factors

**None documented.** No protective allele, dietary factor, or lifestyle exposure is described. gnomAD-frequency reasoning (§9.3) suggests the *deficiency itself* is largely non-deleterious, which makes "protective factor" an ill-posed question here.

### 2.5 Gene–environment interactions

No demonstrated GxE. A **mechanistically predicted** interaction, worth curating as a hypothesis rather than a fact: erythritol production in SHPK deficiency depends on a bypass route through **ketohexokinase/fructokinase (`KHK`)** and **aldolase B (`ALDOB`)** (§6.2). Dietary sedoheptulose load, and in principle `KHK`/`ALDOB` genotype (e.g., hereditary fructose intolerance alleles), would therefore modulate the erythritol biomarker. This is an inference from [PMID:18775706](https://pubmed.ncbi.nlm.nih.gov/18775706/), **not** an observed interaction — do not curate it as evidence-backed.

---

## 3. Phenotypes

### 3.1 The two index patients (the entire clinical evidence base)

| | Patient 1 | Patient 2 |
|---|---|---|
| Presentation | **Neonatal cholestasis, hypoglycemia, anemia** | **Congenital arthrogryposis multiplex, multiple contractures, dysmorphisms** |
| Age at report | 3 years (boy) | 2 years (girl) |
| Ancestry / consanguinity | Caucasian, suspected consanguinity | Turkish, consanguineous parents |
| `SHPK` genotype | homozygous c.355C>T (p.Arg119Ter) | homozygous c.211G>T (p.Glu71Ter) |
| Biochemistry | ↑ urinary erythritol + sedoheptulose | ↑ urinary erythritol + sedoheptulose |

Verbatim ([PMID:25647543](https://pubmed.ncbi.nlm.nih.gov/25647543/)):

> "The first patient presented with neonatal cholestasis, hypoglycemia, and anemia, while the second patient presented with congenital arthrogryposis multiplex, multiple contractures, and dysmorphisms."

Patient-level demographics are as abstracted by OMIM into ClinVar; for VCV000372203 (p.Glu71Ter) the ClinVar record states the variant was found in **"a 2-year-old girl, born of consanguineous Turkish parents."** Patient 1's age/ancestry come from the same OMIM abstraction chain and should be re-verified against the paywalled full text before being asserted in a KB entry.

**The two presentations share no clinical feature.** That absence of a recurrent phenotype is the single most important observation about this disease and is why the authors questioned causality.

### 3.2 HPO annotation set

Two annotation sources exist and they disagree in scope. Curators must know which they are using.

**(a) HPOA / OMIM:617213 — the conservative set (2 terms, frequency `2/2`):**

| HPO ID | Term | Frequency |
|---|---|---|
| **HP:0025157** ✅ | Increased urinary sedoheptulose | 2/2 |
| **HP:0000007** ✅ | Autosomal recessive inheritance | 2/2 |

This is the defensible core: the *only* feature present in both patients is the biochemical one.

**(b) HPOA / ORPHA:440713 — the expansive set (28 terms):**

| HPO ID | Term | Orphanet frequency | System |
|---|---|---|---|
| HP:0002804 | Arthrogryposis multiplex congenita | Obligate | Connective tissue |
| HP:0001371 | Flexion contracture | Obligate | Connective tissue |
| HP:0012768 | Neonatal asphyxia | Obligate | Respiratory |
| HP:0001396 | Cholestasis | Frequent | Digestive |
| HP:0002611 | Cholestatic liver disease | Frequent | Digestive |
| HP:0012115 | Hepatitis | Frequent | Digestive |
| HP:0001409 | Portal hypertension | Frequent | Cardiovascular |
| HP:0002570 | Steatorrhea | Frequent | Digestive |
| HP:0001540 | Diastasis recti | Frequent | Digestive |
| HP:0001903 | Anemia | Frequent | Blood |
| HP:0004840 | Hypochromic microcytic anemia | Frequent | Blood |
| HP:0011998 | Postprandial hyperglycemia | Frequent | Metabolism/Lab |
| HP:0000083 | Renal insufficiency | Frequent | Genitourinary |
| HP:0000091 | Abnormal renal tubule morphology | Frequent | Genitourinary |
| HP:0011400 | Abnormal CNS myelination | Frequent | Nervous |
| HP:0012157 | Subcortical cerebral atrophy | Frequent | Nervous |
| HP:0002119 | Ventriculomegaly | Frequent | Nervous |
| HP:0000256 | Macrocephaly | Frequent | Head/neck |
| HP:0000348 | High forehead | Frequent | Head/neck |
| HP:0000239 | Large fontanelles | Frequent | Head/neck |
| HP:0000586 | Shallow orbits | Frequent | Head/neck |
| HP:0000601 | Hypotelorism | Frequent | Eye |
| HP:0100886 | Abnormality of globe location | Frequent | Eye |
| HP:0001385 | Hip dysplasia | Frequent | Skeletal |
| HP:0000023 | Inguinal hernia | Frequent | Connective tissue |
| HP:0001623 | Breech presentation | Frequent | Prenatal/birth |
| HP:0008850 | Severe postnatal growth retardation | Frequent | Growth |
| HP:0004322 | Short stature | Frequent | Growth |

> **Curation warning — the "Frequent"/"Obligate" labels here are artifacts.** Each term derives from **one** of the two patients (the arthrogryposis cluster from Patient 2; the cholestasis/anemia cluster from Patient 1). "Obligate" applied to arthrogryposis is literally contradicted by Patient 1, who did not have it. Per the dismech frequency SOP (`docs/frequency-evidence-guidelines.md`), **omit `frequency:` on these phenotypes rather than importing the Orphanet band.** If frequency must be recorded, the honest statement is `1/2` for every clinical feature and `2/2` for the biochemical ones.

Two additional laboratory HPO terms belong on the entry but are absent from both annotation sets:

| HPO ID | Term | Basis |
|---|---|---|
| **HP:0034613** ✅ | Elevated urine erythritol level | Present in both patients (PMID:25647543) and in 57-kb-deletion cystinosis (PMID:18186520) |
| HP:0001943 ⚠️ | Hypoglycemia | Patient 1 only |

Note the internal inconsistency: the Orphanet set carries *postprandial hyperglycemia* (HP:0011998) while the source abstract reports *hypoglycemia* in Patient 1. Resolve against full text before curating either.

### 3.3 Phenotype characteristics

- **Age of onset:** congenital / neonatal in both patients (Orphanet onset category: antenatal and neonatal). The *biochemical* phenotype is present from birth and lifelong.
- **Severity:** not gradeable; n=2 with discordant features.
- **Progression:** unknown. No follow-up beyond ages 2–3 years has been published in the 11 years since.
- **Frequency among affected individuals:** see the §3.2 warning — effectively unmeasurable.

### 3.4 Quality of life

**No data.** No EQ-5D, SF-36, PROMIS, or disease-specific instrument has been applied. Given the likely benign nature of the isolated biochemical defect, the QoL burden in the two index patients is more plausibly attributable to their (unexplained) clinical syndromes than to SHPK loss.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

| Field | Value |
|---|---|
| Symbol | **SHPK** (previous: `CARKL`; alias `SHK`) |
| Name | sedoheptulokinase |
| HGNC | **hgnc:1492** ✅ (note dismech lowercase-prefix convention) |
| NCBI Gene | **23729** ✅ |
| Ensembl | **ENSG00000197417** ✅ (GRCh38, chr17:3,607,433–3,636,637, minus strand) |
| UniProt | **Q9UHJ6** ✅ (SHPK_HUMAN; secondary B2R640, Q8WUH3) |
| OMIM gene | *605060 |
| Cytoband | 17p13.2 |
| Genomic span (NCBI, GRCh38.p14) | NC_000017.11:3,608,240–3,636,250, complement |
| Structure | **7 exons** |
| RefSeq | mRNA **NM_013276.4**; protein **NP_037408.2**; CCDS11030.1; genomic ref NG_052852.1 |
| Protein | **478 aa**, FGGY carbohydrate kinase family |
| EC | **2.7.1.14** |

Genomic context is central to this gene's story: `SHPK` sits immediately adjacent to `CTNS`, sharing a bidirectional promoter region, inside a segment dense in Alu repeats that mediate the recurrent 57-kb deletion.

> "The CTNS promoter region shares 41 nucleotides with the promoter region [of the adjacent CARKL gene], though patient mutations did not affect CARKL activity." ([PMID:11505338](https://pubmed.ncbi.nlm.nih.gov/11505338/))

> "sequence analysis detected the presence of a novel gene (CARKL) residing within the most common cystinosis-causing deletion." ([PMID:10673275](https://pubmed.ncbi.nlm.nih.gov/10673275/), Genome Res 2000;10:165-73 — the gene's discovery paper)

### 4.2 Pathogenic variants — and their contested classification

**Variant 1 — p.Arg119Ter (Patient 1)**

| Field | Value |
|---|---|
| cDNA | NM_013276.4:**c.355C>T** |
| Protein | NP_037408.2:**p.Arg119Ter** (R119*) |
| Genomic | NC_000017.11:g.3624187G>A (GRCh38); NC_000017.10:g.3527481G>A (GRCh37) |
| dbSNP | **rs144071313** |
| ClinVar | **VCV000372202** |
| Type | Nonsense (stop-gained), germline |
| **ClinVar aggregate classification** | **Uncertain significance** |
| Submissions | Labcorp Genetics (formerly Invitae) — *Uncertain significance*, evaluated 2025-12-24, Sherloc criteria · OMIM — ***Affects***, 2016-11-22, no assertion criteria |
| Allele frequency | gnomAD 0.00057–0.00058; ExAC 0.00051; TOPMed 0.00070; 1000G 0.00060; ESP 0.00062 |

The submitter's interpretation is the most consequential text in this whole report for curation purposes:

> "The current clinical and genetic evidence is not sufficient to establish whether loss-of-function variants in SHPK cause disease… This variant is present in population databases (rs144071313, gnomAD 0.09%), and has an allele count higher than expected for a pathogenic variant… The available evidence is currently insufficient to determine the role of this variant in disease." (Labcorp Genetics, SCV002219788.4)

Population distribution (dbSNP): highest in **European and Latin American** populations; minimal or absent in East Asian, South Asian, and African populations.

**Variant 2 — p.Glu71Ter (Patient 2)**

| Field | Value |
|---|---|
| cDNA | NM_013276.4:**c.211G>T** |
| Protein | NP_037408.2:**p.Glu71Ter** (E71*) |
| Genomic | NC_000017.11:g.3630304C>A (GRCh38); NC_000017.10:g.3533598C>A (GRCh37) |
| dbSNP | **rs748544120** |
| ClinVar | **VCV000372203** |
| **ClinVar classification** | ***Affects*** (single OMIM submission, no assertion criteria, 2016-11-22) |
| Allele frequency | TOPMed 0.00000; no GMAF |

> **Neither causal variant is classified "Pathogenic" or "Likely pathogenic" in ClinVar.** One is a VUS; the other carries only OMIM's "Affects" label — the ClinVar term reserved for variants that alter a measurable trait without established disease causation. Under ACMG/AMP rules, PM2 (absent from controls) actively *fails* for R119*, and PS3 (functional evidence) is satisfied only for the enzymatic phenotype, not a clinical one. Curating either as `PATHOGENIC` would misrepresent the primary sources.

### 4.3 Copy-number variants

ClinVar contains **363 variant records touching `SHPK`**, of which 67 carry a pathogenic classification. Inspection of the top-ranked pathogenic records shows **every one is a multi-gene copy-number loss involving `CTNS` (± `TRPV1`, ± dozens of 17p13 genes)** — i.e., cystinosis deletions and larger 17p13.3–13.2 deletions. Representative records: VCV004851017, VCV004279276, VCV004075905 (all `chr17:~3.50–3.56 Mb ×1`, genes `CTNS, SHPK, TRPV1`), and VCV003243030 (`NC_000017.10:g.(?_3520391)_(3558524_?)del`, conditions: ocular cystinosis / juvenile nephropathic cystinosis).

**There is no ClinVar pathogenic CNV restricted to `SHPK` alone.** Isolated SHPK deficiency has never been reported from a CNV.

### 4.4 Functional consequence

Both variants are **loss of function via premature termination**, truncating the 478-aa protein at residue 71 or 119 — before the FGGY kinase catalytic core is complete. Both are predicted NMD substrates. Labcorp's assessment: the variant "creates a premature translational stop signal… expected to result in an absent or disrupted protein product," and functional studies in PMID:25647543 confirmed impact on SHPK activity. No gain-of-function or dominant-negative mechanism is described.

For dismech schema purposes: `GeneticContext.functional_impact_category: LOSS_OF_FUNCTION`, `allele_type` nonsense, `zygosity` homozygous, `variant_origin` germline.

### 4.5 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none identified for SHPK deficiency itself.
- **Epigenetics:** no methylation or chromatin study of `SHPK` in disease. The shared bidirectional `CTNS`/`CARKL` promoter (PMID:11505338) is a *cis*-regulatory, not epigenetic, finding — and importantly, cystinosis-causing `CTNS` promoter mutations were shown **not** to affect CARKL promoter activity.
- **Chromosomal abnormalities:** the Alu-mediated recurrent **57-kb deletion** (see §9.4); larger 17p13.3–13.2 deletions encompassing `PAFAH1B1`/`YWHAE` (Miller–Dieker region) also remove `SHPK` incidentally.
- **Transcriptional consequence of the deletion beyond SHPK:** the deletion extends into `TRPV1`, producing measurable downstream dysfunction — relevant when attributing phenotypes in deletion patients:
  > "72% reduction in PBMC TRPV1 mRNA levels in cystinosis individuals homozygous for the 57 kb deletion (n=6) compared to unaffected individuals without the deletion (n=6) (p=0.002)." ([PMID:21546516](https://pubmed.ncbi.nlm.nih.gov/21546516/))
  > "cystinosis patients homozygous for the 57-kb deletion exhibit a strong reduction of TRPV1 function" — 60% reduction in capsaicin-evoked vasodilation and pain, increased heat detection threshold ([PMID:27734949](https://pubmed.ncbi.nlm.nih.gov/27734949/), *Sci Rep* 2016;6:35395)

---

## 5. Environmental Information

- **Environmental factors:** none. No CTD/TOXNET/EPA association. Not a toxicant-, radiation-, or pollution-related condition.
- **Lifestyle factors:** none established. The only dietary consideration is the exogenous supply of the accumulating substrate — sedoheptulose is present in **carrots and fruits** ([PMID:18775706](https://pubmed.ncbi.nlm.nih.gov/18775706/)). No dietary intervention has been trialled and none is indicated.
- **Infectious agents:** not applicable.

*(Adjacent but distinct: sedoheptulose has been proposed as an anti-inflammatory agent based on the CARKL immunometabolism work — US patent 9,694,026, "Use of sedoheptulose for prevention or treatment of inflammation." This is a therapeutic-development thread about the *substrate*, not an environmental risk factor for the disease.)*

---

## 6. Mechanism / Pathophysiology

### 6.1 The primary enzymatic lesion (upstream)

Sedoheptulokinase catalyses a single, well-defined reaction:

**sedoheptulose + ATP → D-sedoheptulose 7-phosphate + ADP + H⁺**

| Property | Value | Source |
|---|---|---|
| EC | 2.7.1.14 | UniProt Q9UHJ6 |
| Rhea | **RHEA:23844** | UniProt |
| GO molecular function | **GO:0050277** ✅ "sedoheptulokinase activity" — *"Catalysis of the reaction: ATP + sedoheptulose = ADP + 2 H+ + sedoheptulose 7-phosphate."* | OLS4/GO |
| Km (sedoheptulose) | **0.06 mM** | UniProt |
| pH optimum | 8.5 | UniProt |
| Subcellular location | **Cytoplasm** (GO:0005829 cytosol ⚠️) | UniProt |
| Protein family | FGGY carbohydrate kinase family | UniProt |
| Tissue specificity | *"Strongly expressed in liver, kidney and pancreas. Expressed at lower levels in placenta and heart."* | UniProt |
| Substrate specificity | *"Mouse recombinant sedoheptulokinase was found to be virtually specific for sedoheptulose"* | [PMID:18775706](https://pubmed.ncbi.nlm.nih.gov/18775706/) |

The product, **sedoheptulose-7-phosphate (CHEBI:15721 ✅)**, is a core intermediate of the **non-oxidative branch of the pentose phosphate pathway (GO:0009052 ✅)**, feeding transketolase and transaldolase reactions. SHPK thus provides an entry point for *free* sedoheptulose — dietary or from intracellular hydrolysis — into central carbohydrate metabolism.

> "The identification of sedoheptulose kinase demonstrates that free sedoheptulose serves as 'a relevant and accessible carbon source in humans.'" ([PMID:23514175](https://pubmed.ncbi.nlm.nih.gov/23514175/), *Biochem Soc Trans* 2013;41:674-80)

### 6.2 The causal chain to the biomarker phenotype (the well-established part)

This is the one mechanistic chain in this disease that is fully worked out, and it is the chain a dismech pathophysiology graph should encode:

```
SHPK biallelic LOF (MOLECULAR)
  → loss of sedoheptulokinase activity (GO:0050277 ↓)  [MOLECULAR]
    → ① reduced hepatic sedoheptulose-7-phosphate  [MOLECULAR/CELLULAR]
    → ② accumulation of free sedoheptulose (CHEBI:16802)  [ORGANISM]
         → renal excretion → increased urinary sedoheptulose (HP:0025157)
         → ③ bypass: fructokinase (KHK) phosphorylates sedoheptulose
              → sedoheptulose 1-phosphate (CHEBI:9082)
              → aldolase B (ALDOB) cleavage
                   → dihydroxyacetone phosphate + erythrose
                        → reduction of erythrose
                             → erythritol (CHEBI:17113) accumulation
                                  → increased urinary erythritol (HP:0034613)
```

Verbatim support for the erythritol arm:

> "Sedoheptulose 1-phosphate is shown to be a substrate for aldolase B… the findings suggest that in sedoheptulose-7-kinase-deficient patients, fructokinase phosphorylates sedoheptulose to sedoheptulose 1-phosphate, which aldolase B cleaves, leading to erythrose reduction to erythritol." ([PMID:18775706](https://pubmed.ncbi.nlm.nih.gov/18775706/), *FEBS Lett* 2008;582:3330-4)

Enzymatic confirmation in human cells:

> "Enzyme studies performed on fibroblast homogenates derived from patients carrying the 57-kb deletion revealed 80% reduction in their sedoheptulose phosphorylating activity compared to cystinosis patients with other mutations and controls." ([PMID:18186520](https://pubmed.ncbi.nlm.nih.gov/18186520/))

And in the mouse knockout: "Analysis of pentose phosphate pathway intermediates in livers demonstrated a reduction in sedoheptulose-7-phosphate and an increase in sedoheptulose and erythritol in the urine" ([PMID:34823997](https://pubmed.ncbi.nlm.nih.gov/34823997/)).

**Where the chain stops.** There is no demonstrated causal link from this biochemical chain to *any* clinical manifestation. Neither sedoheptulose nor erythritol has documented toxicity at the concentrations observed, and the PPP-flux consequences appear compensated *in vivo*. A dismech pathograph should terminate the causal chain at the laboratory phenotypes and represent the clinical features as **unexplained co-occurrence**, not downstream consequences.

### 6.3 The immunometabolic arm (CARKL as a metabolic rheostat)

The richest mechanistic literature on this protein concerns **not** the inborn error but CARKL's role as a regulator of immune-cell metabolism. This matters for the disease entry because it is the strongest *a priori* reason to expect a phenotype — and its absence in patients and mice is informative.

Founding observation ([PMID:22682222](https://pubmed.ncbi.nlm.nih.gov/22682222/), Haschemi et al., *Cell Metab* 2012;15:813-26):

> "We find that one of these, the carbohydrate kinase-like protein CARKL, is rapidly downregulated in vitro and in vivo upon LPS stimulation in both mice and humans. Interestingly, CARKL catalyzes an orphan reaction in the pentose phosphate pathway, refocusing cellular metabolism to a high-redox state upon physiological or artificial downregulation. We find that CARKL-dependent metabolic reprogramming is required for proper M1- and M2-like macrophage polarization and uncover a rate-limiting requirement for appropriate glucose flux in macrophage polarization."

Downstream and corroborating literature:

| Finding | Cell/system | Citation |
|---|---|---|
| "in M2 cells, sedoheptulose kinase carbohydrate kinase-like protein is critical for regulating the pentose phosphate pathway" | Macrophages (review) | [PMID:25228902](https://pubmed.ncbi.nlm.nih.gov/25228902/) |
| PPP supplies "nucleotide precursors and redox-equivalents"; demand-driven regulation over time | Macrophage activation (review) | [PMID:25904920](https://pubmed.ncbi.nlm.nih.gov/25904920/) |
| CARKL overexpression "significantly attenuated the intracellular ROS production and sensitized the M2 phenotype macrophage polarization"; CARKL is "a rheostat for cellular metabolism" | Sea cucumber coelomocytes + mouse macrophages | [PMID:32283109](https://pubmed.ncbi.nlm.nih.gov/32283109/) |
| Se-dependent proresolving reprogramming implicates sedoheptulokinase alongside SDH and pyruvate kinase | Murine BMDM | [PMID:33581115](https://pubmed.ncbi.nlm.nih.gov/33581115/) |
| "IRAK4i counteracted TLR7-induced CARKL reduction in line with HIF1i" | RA macrophages and fibroblast-like synoviocytes | [PMID:34732329](https://pubmed.ncbi.nlm.nih.gov/34732329/) |
| "CARKL overexpression leads to significant metabolic shifts in T cells, affecting mitochondrial respiration, ATP production, and inflammatory cytokine profiles… compromising CXCR3 expression and impairing T-cell migration" | Human/mouse T cells | [PMID:39669692](https://pubmed.ncbi.nlm.nih.gov/39669692/), *Discov Immunol* 2024 |
| "crosstalk between the HIF-1α and NF-κB pathways modulated by metabolic sensors like CARKL underpins persistent inflammatory responses" | Microglia (review) | [PMID:42031319](https://pubmed.ncbi.nlm.nih.gov/42031319/) |

**Cancer:** SHPK is implicated in glioblastoma proliferation —

> "SHPK expression in GBM shows a significant correlation with histology, prognosis, and survival. In particular, its increased expression is associated with a worse prognosis. Furthermore, its overexpression in GBM cells confirms an increase in cell proliferation." ([PMID:35682658](https://pubmed.ncbi.nlm.nih.gov/35682658/), *Int J Mol Sci* 2022;23:5978)

⚠️ **This paper carries a published Correction** ([PMID:39941164](https://pubmed.ncbi.nlm.nih.gov/39941164/), *Int J Mol Sci* 2025;26:1044). Cite the correction alongside the original.

Note the direction of these findings: they concern **overexpression or acute downregulation** of CARKL as a *regulatory* event in immune/tumour cells, not constitutional germline deficiency. The clean mouse-knockout phenotype (§15) shows the two do not straightforwardly translate.

### 6.4 Suggested ontology terms for the mechanism graph

| Concept | Term | Confidence |
|---|---|---|
| Sedoheptulokinase activity | **GO:0050277** | ✅ verified via OLS4 |
| Pentose-phosphate shunt | **GO:0006098** | ✅ verified |
| Pentose-phosphate shunt, non-oxidative branch | **GO:0009052** | ✅ verified |
| Regulation of pentose-phosphate shunt | GO:0043456 | ✅ verified |
| Negative regulation of pentose-phosphate shunt | GO:1905856 | ✅ verified |
| sedoheptulose | **CHEBI:16802** | ✅ verified |
| sedoheptulose 7-phosphate | **CHEBI:15721** | ✅ verified |
| sedoheptulose 1-phosphate | **CHEBI:9082** | ✅ verified |
| erythritol | **CHEBI:17113** | ✅ verified |
| macrophage | CL:0000235 | ⚠️ verify |
| T cell | CL:0000084 | ⚠️ verify |
| hepatocyte | CL:0000182 | ⚠️ verify |
| microglial cell | CL:0000129 | ⚠️ verify |
| liver / kidney / pancreas | UBERON:0002107 / UBERON:0002113 / UBERON:0001264 | ⚠️ verify |

No dismech **mechanism module** currently fits this disease well. `metabolic_intoxication_decompensation` does **not** apply — there is no toxic-metabolite crisis, no catabolic-stress decompensation, and no encephalopathy. Do not force a `conforms_to`.

---

## 7. Anatomical Structures Affected

### 7.1 Where the enzyme is expressed (the biologically grounded answer)

- **Liver, kidney, pancreas** — strong expression; **placenta, heart** — lower (UniProt Q9UHJ6).
- NCBI Gene expression profile: ubiquitous, with notable **kidney (RPKM 7.3)** and **duodenum (RPKM 6.9)** across 27 tissues.
- Subcellular: **cytoplasm/cytosol**. Not mitochondrial, lysosomal, or nuclear.

### 7.2 Organs implicated in the reported patients (attribution uncertain)

| System | Findings | UBERON ⚠️ |
|---|---|---|
| Hepatobiliary | cholestasis, hepatitis, portal hypertension | UBERON:0002107 liver |
| Haematopoietic | anemia, hypochromic microcytic anemia | UBERON:0000178 blood |
| Musculoskeletal | arthrogryposis, contractures, hip dysplasia | UBERON:0002204 musculoskeletal system |
| CNS | abnormal myelination, ventriculomegaly, subcortical atrophy | UBERON:0000955 brain |
| Renal | renal insufficiency, abnormal tubule morphology | UBERON:0002113 kidney |
| Craniofacial/ocular | macrocephaly, high forehead, large fontanelles, shallow orbits, hypotelorism | UBERON:0000033 head |

**Lateralization:** bilateral/symmetric where relevant (contractures, orbits). No asymmetric involvement described.

**Important negative:** In `Shpk^-/-` mice there were "no histologic anomalies in kidney and liver" — the two organs with highest SHPK expression ([PMID:34823997](https://pubmed.ncbi.nlm.nih.gov/34823997/)). This is direct evidence against liver/kidney being target organs of the enzyme defect.

### 7.3 Cell types

No cell-type-specific pathology has been demonstrated in patients. The mechanistic literature implicates **macrophages** (M1/M2 polarization), **T cells**, and **microglia** as cells where CARKL levels matter functionally — but as regulatory biology, not as sites of disease lesion.

---

## 8. Temporal Development

- **Onset:** congenital. Orphanet records onset as **antenatal and neonatal**; GARD states symptoms "may appear during pregnancy and as a newborn." Patient 2 had congenital arthrogryposis (prenatal onset, with breech presentation and neonatal asphyxia); Patient 1 presented in the neonatal period with cholestasis.
- **Onset pattern:** the metabolic derangement is **chronic and constitutive** from birth. The clinical presentations in the two cases were acute-on-congenital.
- **Stages:** none defined. No staging system exists.
- **Progression rate / course:** **unknown.** Both patients were reported at ages 2–3 years with no published follow-up. There is no natural-history study, no registry, and no longitudinal cohort.
- **Duration:** the biochemical phenotype is lifelong and non-remitting (it is an enzyme absence).
- **Remission:** not applicable to the biochemical phenotype. No treatment-induced remission is possible or has been attempted.
- **Critical periods:** none identified. If the disorder is benign, the concept does not apply; if the neonatal presentations were causally related, the neonatal period would be the window — but that causality is precisely what is unestablished.

---

## 9. Inheritance and Population

### 9.1 Inheritance

**Autosomal recessive** (HP:0000007, HPOA frequency 2/2; Orphanet; GARD). Both index patients were **homozygous** for a nonsense variant, both from families with consanguinity. No compound heterozygote has been reported. No X-linked, mitochondrial, or digenic contribution.

- **Penetrance:** cannot be estimated, and the population-genetic data (§9.3) argue for **markedly reduced or zero clinical penetrance**. Biochemical penetrance (urinary metabolite elevation) appears complete.
- **Expressivity:** the two cases are maximally discordant — which is more parsimoniously read as *coincidence* than as variable expressivity.
- **Anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not reported.

### 9.2 Epidemiology

- **Prevalence: not documented.** Orphanet assigns no epidemiological class to ORPHA:440713. Only **2 cases have ever been reported** (`CASES_IN_LITERATURE` = 2 is the honest structured value for a dismech `Prevalence` record; `prevalence_class: NOT_YET_DOCUMENTED`).
- **Incidence:** unknown.
- **Sex ratio:** 1 male : 1 female among reported cases — uninformative at n=2.
- **Age distribution:** both reported patients ascertained in infancy/early childhood; no adult cases reported (which does not mean none exist — untargeted urine metabolite screening in adults is rare).

### 9.3 Carrier frequency and the under-ascertainment argument

This calculation is worth recording explicitly in the KB because it is the strongest quantitative argument about the disorder's nature:

- `p.Arg119Ter` (rs144071313) gnomAD allele frequency ≈ **0.00057** (0.057%; Labcorp cites 0.09% for a subpopulation-inclusive figure).
- Predicted heterozygous carrier frequency for this single allele: **≈1 in 880**.
- Predicted homozygote frequency for this single allele alone: p² ≈ 3.2 × 10⁻⁷ ≈ **1 in ~3.1 million** — i.e. roughly **2,500 living homozygotes worldwide** for R119* alone, before counting any other `SHPK` LoF allele.
- **Observed reported cases: 2.**

*(This is my arithmetic from the cited gnomAD frequencies, presented as a derived estimate, not a published figure.)* The gap of three-plus orders of magnitude is exactly the reasoning Labcorp applied — "an allele count higher than expected for a pathogenic variant" — and it supports either (a) the condition is clinically silent, or (b) it is severely under-ascertained because nobody measures urinary sedoheptulose. Both readings are compatible with the primary paper's own question mark.

⚠️ *Not retrieved:* gnomAD gene-level constraint metrics for `SHPK` (pLI, LOEUF, observed/expected pLoF, homozygous pLoF count). The gnomAD browser is a client-rendered application and its GraphQL API requires POST, neither of which was accessible from this session. These should be pulled manually — the LOEUF value and the presence/absence of homozygous pLoF individuals would materially strengthen or weaken the benign-disorder argument.

### 9.4 Founder effects, geography, and the far more common contiguous-gene form

**Isolated form:** `p.Arg119Ter` is enriched in **European and Latin American** populations and near-absent in East Asian, South Asian, and African populations (dbSNP/ALFA). `p.Glu71Ter` was found in a **Turkish** consanguineous family and is absent from TOPMed — consistent with a private or very rare regional allele. Neither constitutes an established founder mutation.

**Contiguous-gene form (secondary SHPK deficiency):** the 57-kb `CTNS`/`SHPK` deletion is a genuine **northern European founder allele**, thought to have originated in Germany, and:
- occurs in ~**60%** of cystinosis patients in the US and northern Europe ([PMID:15365816](https://pubmed.ncbi.nlm.nih.gov/15365816/): *"The most prevalent CTNS mutation, a 57-kb deletion, occurs in approximately 60% of patients"*);
- accounts for **50–70%** of pathogenic CTNS alleles in those regions, and is **homozygous in ~50%** of northern-European cystinosis patients (GeneReviews, *Cystinosis*);
- has **not** been reported in individuals from the Middle East, Asia, or Africa.

Cystinosis birth prevalence is **1:100,000 to 1:200,000** (1:26,000 in Brittany, France). Combining these figures gives an order-of-magnitude estimate that roughly **1 in 200,000–400,000 births in northern European populations carries biallelic SHPK loss as part of a cystinosis deletion** — a population perhaps a thousand-fold larger than the reported isolated cases. *(Derived estimate; label as such.)* These individuals are, by definition, clinically dominated by cystinosis.

**Consanguinity** is the operative population factor for the isolated form: both reported families were consanguineous or suspected consanguineous.

---

## 10. Diagnostics

### 10.1 Biochemical (the diagnostic entry point)

**Urinary sugar/polyol profiling by GC-MS or LC-MS/MS** is the discriminating test. The characteristic pattern:

| Analyte | Direction | Reference data |
|---|---|---|
| **Sedoheptulose (urine)** | ↑↑ | Controls and non-deleted cystinosis patients **<9 mmol/mol creatinine**; 57-kb-deletion patients **28–451** ([PMID:18186520](https://pubmed.ncbi.nlm.nih.gov/18186520/)) |
| **Erythritol (urine)** | ↑↑ | Controls **<148 mmol/mol creatinine**; deletion patients **234–1110** (same source) |
| **Sedoheptulose-7-phosphate** | low-to-normal | Orphanet definition; consistent with mouse hepatic S7P reduction (PMID:34823997) |

⚠️ Note these interval values were established in the **cystinosis 57-kb-deletion cohort**, not the two isolated-deficiency patients (whose exact values are in the paywalled full text of PMID:25647543 and should be extracted before curating a `reference_ranges` block). No LOINC code exists for urinary sedoheptulose.

**Dried blood spot sedoheptulose (LC-MS/MS)** — developed for cystinosis screening but directly applicable:

> "Sedoheptulose concentrations in the deleted patients were 6 to 23 times above the upper limit for controls. No overlap existed between sedoheptulose levels in patients homozygous for the deletion versus those without it." ([PMID:21195649](https://pubmed.ncbi.nlm.nih.gov/21195649/), *Mol Genet Metab* 2011;102:339-42)

**Untargeted metabolomics** is an increasingly used unbiased route into non-oxidative PPP disorders:

> "Targeted polyol testing and untargeted metabolomic testing methods were both able to identify specific biochemical patterns indicative of TKT and TALDO deficiency… untargeted analysis revealed novel biomarkers including ribonate, ribose, erythronate, and sedoheptulose 7-phosphate." ([PMID:32828637](https://pubmed.ncbi.nlm.nih.gov/32828637/), *Mol Genet Metab* 2020;131:147-154)

**Enzyme assay:** sedoheptulose-phosphorylating activity in cultured skin fibroblast homogenates — 80% reduction demonstrated in 57-kb-deletion patients vs controls (PMID:18186520). This is a research assay, not a routine clinical service.

### 10.2 Genetic testing

| Modality | Utility |
|---|---|
| **WES / WGS** | High — this is realistically how a new case would be found today (and how the original two were resolved after biochemical suspicion). |
| **Single-gene `SHPK` sequencing** | Available; GTR lists testing for "Isolated sedoheptulokinase deficiency" (MedGen C1291373, OMIM 617213). |
| **Gene panels** | `SHPK` appears on some inborn-errors-of-metabolism / PPP panels; no dedicated panel. |
| **MLPA / CMA** | Required to detect the 57-kb deletion (the far commoner cause of SHPK loss) — CMA will call it as a `CTNS/SHPK/TRPV1` copy-number loss. |
| **FISH** | A validated FISH assay for the common 57-kb deletion exists: *"The FISH probes… made the correct diagnosis in every case"* ([PMID:15365816](https://pubmed.ncbi.nlm.nih.gov/15365816/)) — historically the first FISH-based diagnostic for any lysosomal storage disorder. |
| Karyotyping, mtDNA testing, repeat-expansion testing | Not applicable. |

**Critical interpretation caveat:** because both known causal variants are ClinVar VUS/"Affects" and `SHPK` LoF alleles are relatively common in gnomAD, **a homozygous `SHPK` nonsense finding on exome should not be reported as the explanation for a complex neonatal phenotype without biochemical confirmation and, crucially, without continuing the diagnostic search.** This is the operational lesson of PMID:25647543.

### 10.3 Other modalities

- **Imaging:** no disease-specific findings. Brain MRI abnormalities (myelination, ventriculomegaly, subcortical atrophy) were recorded in one patient; liver imaging for cholestasis in the other. Both are workup of the presenting syndrome, not of SHPK deficiency.
- **Biopsy/histopathology:** no characteristic finding. Mouse KO liver and kidney are histologically normal.
- **Electrophysiology, functional tests:** no role.

### 10.4 Clinical criteria and differential diagnosis

**No standardized diagnostic criteria exist.** A working definition is: biallelic `SHPK` LoF + elevated urinary sedoheptulose and erythritol + normal cystine (excluding cystinosis).

**Differential diagnosis — causes of elevated urinary sedoheptulose/polyols:**

| Condition | Gene | Distinguishing features |
|---|---|---|
| **Cystinosis with 57-kb deletion** | `CTNS` (+`SHPK`) | Elevated leukocyte cystine, corneal crystals, renal Fanconi syndrome; identical sedoheptulose/erythritol signature. **Must be excluded first.** |
| **Transaldolase deficiency** | `TALDO1` | Neonatal liver disease, hepatosplenomegaly, anaemia, thrombocytopenia, cardiac and skin abnormalities; elevated sedoheptulose *and* polyols (erythritol, arabitol, ribitol). **The closest phenotypic mimic of Patient 1.** |
| **Ribose-5-phosphate isomerase deficiency** | `RPIA` | Slowly progressive leukoencephalopathy + peripheral neuropathy; markedly elevated **ribitol and D-arabitol** on brain MRS and in body fluids |
| **Transketolase deficiency** | `TKT` | Non-oxidative PPP; short stature, developmental delay; detectable by polyol/untargeted metabolomics |
| Hereditary fructose intolerance / essential pentosuria | `ALDOB`, `DCXR` | Distinct sugar profile |

*(TALDO/RPI background: [Disorders of the Pentose Phosphate Pathway and Polyol Metabolism](https://link.springer.com/chapter/10.1007/978-3-030-67727-5_40); RPI deficiency original description in *Am J Hum Genet*.)*

### 10.5 Screening

- **Newborn screening: not performed and not indicated** for isolated SHPK deficiency (no treatment, uncertain pathogenicity — fails Wilson–Jungner criteria on both counts).
- However, **DBS sedoheptulose is a proposed NBS marker for cystinosis** homozygous for the 57-kb deletion, where presymptomatic detection *does* change management (cysteamine): "The method enables fast pre-symptomatic detection of cystinosis patients homozygous for the 57-kb deletion, facilitating early treatment initiation" ([PMID:21195649](https://pubmed.ncbi.nlm.nih.gov/21195649/)). Any such programme would incidentally detect isolated SHPK deficiency — an incidental-findings issue worth flagging.
- **Carrier screening:** not on any expanded carrier screening panel; not recommended.
- **Cascade screening:** reasonable within a family for genetic-counselling completeness, but the counselling message is one of uncertainty.

---

## 11. Outcome / Prognosis

**No prognostic data exist.** Both index patients were alive at ages 2 and 3 at publication; no follow-up has been published in the subsequent 11 years.

- **Survival / life expectancy / mortality:** unknown; no deaths attributed to SHPK deficiency. There is no SEER/registry/GBD entry.
- **Disease-specific mortality:** none reported.
- **Morbidity / disability:** the disabilities present in the two index patients (arthrogryposis-related motor impairment; neonatal liver disease) are substantial but of **unestablished attribution**.
- **Complications:** none attributable to the enzyme defect.
- **Recovery potential:** the enzyme deficiency is permanent; the biochemical phenotype does not remit.
- **Prognostic factors / biomarkers:** none. Urinary sedoheptulose and erythritol are **diagnostic** markers with no demonstrated prognostic value.

**The best available prognostic evidence is indirect and reassuring:** `Shpk^-/-` mice show "no obvious phenotypic abnormalities, including the absence of histologic anomalies in kidney and liver" ([PMID:34823997](https://pubmed.ncbi.nlm.nih.gov/34823997/)), and IMPC phenotyping of the `Shpk` line reports **0 significant phenotypes across 20 of 24 physiological systems tested**.

---

## 12. Treatment

**There is no specific treatment, and none is currently indicated.** No pharmacological, dietary, enzyme-replacement, gene-therapy, or cell-therapy approach targets SHPK deficiency.

**Clinical trials: zero.** A ClinicalTrials.gov API query for `sedoheptulokinase OR SHPK` returned **0 studies**.

### 12.1 Management as actually practised

| Intervention | Rationale | NCIT (from the dismech-approved list) |
|---|---|---|
| **Genetic counselling** | AR recurrence risk; and — equally important — counselling about *uncertain pathogenicity* | **NCIT:C15240** Genetic Counseling |
| **Supportive / symptomatic care** | Directed at the individual patient's presenting features (cholestasis, anaemia, contractures), not at the metabolic defect | **NCIT:C15747** Supportive Care |
| Physical therapy / rehabilitation (Patient 2 pattern) | Standard arthrogryposis management | **NCIT:C15302** Physical Therapy; NCIT:C15315 Rehabilitation |
| Continued diagnostic search | The presenting syndromes remain unexplained | — |

Dietary sedoheptulose restriction (`NCIT:C15447` Dietary Intervention) is **theoretically capable of lowering the biomarker** but has never been trialled, has no rationale in the absence of demonstrated toxicity, and should not be curated as a treatment.

### 12.2 Pharmacogenomics, advanced therapeutics, surgery

- **Pharmacogenomics:** no PharmGKB/CPIC entry for `SHPK`.
- **Gene therapy, cell therapy, RNA-based therapy, targeted therapy, immunotherapy:** none developed or proposed for this indication.
- **Surgery:** no role for the metabolic disease.

### 12.3 The one therapeutically consequential finding — cystinosis gene therapy

The most clinically actionable result in this entire literature concerns whether **secondary** SHPK deficiency compromises HSPC gene therapy for cystinosis. It does not:

> "Transplantation of Shpk-/- HSPCs into Ctns-/- mice resulted in significant reduction in tissue cystine load and restoration of Ctns expression, as well as improved kidney architecture comparable to WT-HSPC recipients. Altogether, these data demonstrate that absence of SHPK does not alter the ability of HSPCs to rescue cystinosis, and then patients homozygous for the 57-kb deletion should benefit from ex vivo gene therapy and can be enrolled in the ongoing clinical trial. However, because of the limits inherent to animal models, outcomes of this patient population will be carefully compared to the other enrolled subjects." ([PMID:34823997](https://pubmed.ncbi.nlm.nih.gov/34823997/), *Mol Genet Metab* 2021;134:309-316)

The concern was specific and well-founded — CARKL "influences macrophage polarization," and the therapy's mechanism of action depends on transplanted HSPCs differentiating into tissue macrophages that transfer cystinosin-bearing lysosomes via tunneling nanotubes.

Relevant registered trials (for the cystinosis cross-reference, **not** for this disease):
- **NCT03897361** — Stem Cell Gene Therapy for Cystinosis (CTNS-RD-04; autologous CD34+ HSPC, lentiviral CTNS; Phase 1/2; **Completed**; UC San Diego)
- **NCT05146830** — Long-Term Follow-Up of CTNS-RD-04 Recipients (observational, enrolling by invitation)
- **NCT06910813** — DFT383 in Pediatric Participants With Nephropathic Cystinosis (Phase I/II, recruiting; Novartis)

### 12.4 Treatment outcomes, adverse events, algorithms

Not applicable — no disease-directed treatment exists, therefore no response rates, no FAERS signal, no algorithm, no combination or genotype-guided strategy.

---

## 13. Prevention

- **Primary prevention:** not applicable to a constitutional genetic disorder. The only lever is reproductive: **genetic counselling** for consanguineous couples with an affected child. Given that both causal variants are ClinVar VUS/"Affects" and the disorder may be benign, counselling should explicitly frame recurrence risk as *risk of the biochemical trait*, with clinical consequences unknown. **Offering prenatal diagnosis or PGT for a possibly benign biochemical trait raises a real ethical question** and should not be presented as routine.
- **Secondary prevention:** no screening programme; no evidence that presymptomatic detection changes any outcome. Contrast with cystinosis, where DBS sedoheptulose screening *would* enable early cysteamine (PMID:21195649).
- **Tertiary prevention:** no complications are known to be preventable, because none are established as disease-related.
- **Immunization, behavioural intervention, prophylaxis, public health/environmental intervention:** all not applicable.
- **Risk stratification:** the only actionable stratifier is consanguinity + an affected proband.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologs

| Species | NCBI Taxon | Gene | Identifier |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | `SHPK` | GeneID **23729**; ENSG00000197417; hgnc:1492 |
| *Mus musculus* | NCBITaxon:10090 | `Shpk` (syn. `Carkl`, `4930431K22Rik`) | GeneID **74637**; **MGI:1921887**; Chr11:73,090,286–73,115,337 (+), GRCm39; 45.25 cM |
| *Apostichopus japonicus* (sea cucumber) | NCBITaxon:307972 ⚠️ | `AjCARKL` | Cloned and characterised — [PMID:32283109](https://pubmed.ncbi.nlm.nih.gov/32283109/) |

The enzyme belongs to the **FGGY carbohydrate kinase family**, which is deeply conserved across bacteria, plants, and animals — and the substrate sedoheptulose is a Calvin-cycle-adjacent plant metabolite (sedoheptulose-1,7-bisphosphatase), which is why plants are a dietary source.

### 14.2 Natural disease in other species

**None known.** An OMIA search for `SHPK` returns **no phene records in any species** — there is no naturally occurring animal model, no companion-animal or livestock disease, and no wildlife counterpart. No veterinary relevance.

### 14.3 Comparative biology and transmission

- **Comparative pathology:** the mouse knockout replicates the human **biochemical** phenotype exactly (urinary sedoheptulose ↑, erythritol ↑, hepatic S7P ↓) and shows **no** clinical or histological phenotype — the strongest available cross-species evidence that the metabolite abnormality is not intrinsically pathogenic.
- **Evolutionary conservation:** the CARKL-as-metabolic-rheostat function is conserved from echinoderms to mammals — sea cucumber `AjCARKL` overexpression suppressed G6PD, ROS production, and phagocytosis in coelomocytes and drove M2-like polarization in mouse macrophages ([PMID:32283109](https://pubmed.ncbi.nlm.nih.gov/32283109/)). This makes the *absence* of an immune phenotype in human/mouse deficiency more striking, not less.
- **Zoonotic potential / cross-species susceptibility:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

### 15.1 Mouse — `Shpk` knockout (the key model)

**Origin:** Goodman et al. 2021 (Cherqui lab, UC San Diego), created specifically to test whether SHPK loss compromises cystinosis HSPC gene therapy ([PMID:34823997](https://pubmed.ncbi.nlm.nih.gov/34823997/)).

| Attribute | Detail |
|---|---|
| Model type | Mammalian, constitutive germline knockout |
| Method | **CRISPR-Cas9** |
| Alleles | **Two independent lines**: (i) a **168-bp deletion** centred on the start codon; (ii) a **675-bp deletion** removing all of exon 2 |
| IMPC allele | `Shpk^em1(IMPC)Mbp` — constitutive deletion of exon 2 + flanking splice regions, CRISPR-Cas9, made at the **Mouse Biology Program, UC Davis** |
| Repository | **MMRRC:043666-UCD** |
| MGI record | MGI:1921887 — 10 mutations total (4 targeted, 5 endonuclease-mediated, 1 chemically induced); "4 phenotypes from 2 alleles in 2 genetic backgrounds" |
| Protein validation | **Shpk protein absent in liver and kidney** in both lines |

**Phenotype recapitulation:**

| Human feature | Mouse | Recapitulated? |
|---|---|---|
| ↑ urinary sedoheptulose | ✔ | **Yes** |
| ↑ urinary erythritol | ✔ | **Yes** |
| ↓ sedoheptulose-7-phosphate | ✔ (hepatic PPP intermediates) | **Yes** |
| Neonatal cholestasis / hepatitis | ✘ (no histologic anomaly in liver) | **No** |
| Anemia | ✘ | **No** |
| Arthrogryposis / contractures | ✘ | **No** |
| Renal insufficiency | ✘ (no histologic anomaly in kidney) | **No** |

> "Shpk-/- mice also recapitulated the urinary excretion of sedoheptulose and erythritol found in cystinosis patients homozygous for the 57-kb deletion." ([PMID:34823997](https://pubmed.ncbi.nlm.nih.gov/34823997/))

**IMPC broad phenotyping:** 20 of 24 physiological systems tested; **0 significant phenotypes**; 4 systems not yet evaluated (IMPC Data Release 24.0).

**Model limitations:** (a) it does not reproduce any human clinical feature — which may reflect genuine benignity rather than model failure; (b) mouse diet differs in sedoheptulose content from human diet, potentially altering substrate load; (c) IMPC coverage is incomplete (4 systems untested), and no aged cohort, immune-challenge, or metabolic-stress paradigm has been reported. A **`HUMAN_MODEL_MISMATCH`** discussion is arguably warranted here in the inverse of the usual direction: the model is *healthier* than the patients, and the open question is whether the patients' illness had anything to do with the gene.

**Research applications:** PPP flux in vivo; macrophage/HSPC biology in a CARKL-null background; the cystinosis gene-therapy eligibility question (already answered).

### 15.2 Cellular and in vitro models

| System | Manipulation | Use | Citation |
|---|---|---|---|
| Mouse BMDM / RAW-type macrophages, human monocytes | CARKL knockdown and overexpression | M1/M2 polarization, PPP flux, redox state — the founding immunometabolism work | [PMID:22682222](https://pubmed.ncbi.nlm.nih.gov/22682222/) |
| Human/mouse **T cells** | CARKL overexpression | Mitochondrial respiration, ATP, cytokine profile, CXCR3-dependent migration | [PMID:39669692](https://pubmed.ncbi.nlm.nih.gov/39669692/) |
| **Glioblastoma cell lines** | SHPK overexpression | Proliferation; non-oxidative PPP as a therapeutic target | [PMID:35682658](https://pubmed.ncbi.nlm.nih.gov/35682658/) + correction [PMID:39941164](https://pubmed.ncbi.nlm.nih.gov/39941164/) |
| **Patient skin fibroblasts** | native | Sedoheptulose-phosphorylating enzyme assay (80% reduction in deletion patients) | [PMID:18186520](https://pubmed.ncbi.nlm.nih.gov/18186520/) |
| **Recombinant mouse SHPK** | purified enzyme | Substrate specificity, kinetics | [PMID:18775706](https://pubmed.ncbi.nlm.nih.gov/18775706/) |
| RA macrophages + fibroblast-like synoviocytes | TLR7 stimulation ± IRAK4i | CARKL as a node in inflammatory metabolic rewiring | [PMID:34732329](https://pubmed.ncbi.nlm.nih.gov/34732329/) |
| Sea cucumber coelomocytes | AjCARKL overexpression | Conserved PPP-rheostat function | [PMID:32283109](https://pubmed.ncbi.nlm.nih.gov/32283109/) |

**No iPSC, organoid, zebrafish, *Drosophila*, *C. elegans*, or yeast model of SHPK deficiency has been reported.**

### 15.3 Model databases

MGI (MGI:1921887) · IMPC (mousephenotype.org, `Shpk`) · MMRRC (043666-UCD) · Alliance of Genome Resources · Cellosaurus (for the GBM lines).

---

## Summary of what could not be retrieved

Stated explicitly so gaps are not mistaken for negatives:

1. **OMIM full-text entries** (#617213 and *605060) — omim.org returned HTTP 403 to automated fetch. The OMIM clinical-synopsis content is indirectly captured via HPOA (2 terms) and the ClinVar OMIM submissions; the OMIM narrative "Clinical Features"/"Molecular Genetics" prose was not read.
2. **gnomAD gene-level constraint for `SHPK`** (pLI, LOEUF, obs/exp pLoF, homozygous pLoF count) — browser is client-rendered; API requires POST. Variant-level frequencies *were* obtained via ClinVar and dbSNP.
3. **Full text of Wamelink et al. 2015** (paywalled, not in PMC) — so the index patients' exact metabolite concentrations, fibroblast enzyme activities, imaging details, and the reasoning behind "extensive functional and clinical workup" were not read directly. **This is the single highest-value document to obtain before finalising a KB entry**, since it contains the per-patient quantitative data.
4. **Human Protein Atlas SHPK page** — the fetched URL resolved to a different gene (RIDA); tissue expression here is sourced from UniProt and NCBI Gene instead.

---

## Suggested dismech curation posture

- Curate as a **Disease** entry with a deliberately thin pathophysiology graph terminating at the two laboratory phenotypes; do **not** draw causal edges to the clinical features.
- Record a **`KNOWLEDGE_GAP`** discussion attached to the disease: *"Is isolated SHPK deficiency a disease at all, or a benign biochemical trait? Two discordant cases, LoF alleles at population frequencies exceeding recessive-disease expectation, and a phenotypically normal knockout mouse."* With `proposed_experiments`: systematic urine-metabolite screening of gnomAD-identified `SHPK` LoF homozygotes; deep phenotyping of the two index families' unresolved syndromes.
- Prefer `supports: PARTIAL` over `SUPPORT` for any evidence item linking a clinical phenotype to the genotype.
- Omit `frequency:` on all clinical phenotypes (see §3.2).
- Cross-reference the cystinosis entry for the contiguous-gene form, and note the `TRPV1` co-deletion as a competing explanation for phenotypes in deletion patients.
- No `conforms_to` module fits; do not force one.

---

## Sources

- [First two unrelated cases of isolated sedoheptulokinase deficiency: A benign disorder? — PubMed (PMID:25647543)](https://pubmed.ncbi.nlm.nih.gov/25647543/)
- [Springer Nature Link — J Inherit Metab Dis 2015, 10.1007/s10545-014-9809-1](https://link.springer.com/article/10.1007/s10545-014-9809-1)
- [Sedoheptulokinase deficiency due to a 57-kb deletion in cystinosis patients… elucidation of the CARKL gene (PMID:18186520)](https://pubmed.ncbi.nlm.nih.gov/18186520/)
- [Characterization of mammalian sedoheptulokinase and mechanism of formation of erythritol (PMID:18775706)](https://pubmed.ncbi.nlm.nih.gov/18775706/)
- [Elevated concentrations of sedoheptulose in bloodspots of patients with cystinosis (PMID:21195649)](https://pubmed.ncbi.nlm.nih.gov/21195649/)
- [The 57 kb deletion in cystinosis patients extends into TRPV1 (PMID:21546516)](https://pubmed.ncbi.nlm.nih.gov/21546516/)
- [TRPV1 dysfunction in cystinosis patients harboring the homozygous 57 kb deletion (PMID:27734949)](https://www.nature.com/articles/srep35395)
- [The genomic region encompassing CTNS… discovery of a novel gene within the common cystinosis-causing deletion (PMID:10673275)](https://pubmed.ncbi.nlm.nih.gov/10673275/)
- [The promoter of CTNS… shares sequences with the promoter of an adjacent gene, CARKL (PMID:11505338)](https://pubmed.ncbi.nlm.nih.gov/11505338/)
- [FISH diagnosis of the common 57-kb deletion in CTNS causing cystinosis (PMID:15365816)](https://pubmed.ncbi.nlm.nih.gov/15365816/)
- [The sedoheptulose kinase CARKL directs macrophage polarization through control of glucose metabolism (PMID:22682222)](https://pubmed.ncbi.nlm.nih.gov/22682222/)
- [Sedoheptulose kinase regulates cellular carbohydrate metabolism by sedoheptulose 7-phosphate supply (PMID:23514175)](https://pubmed.ncbi.nlm.nih.gov/23514175/)
- [Metabolic reprograming in macrophage polarization (PMID:25228902)](https://pubmed.ncbi.nlm.nih.gov/25228902/)
- [Time and Demand are Two Critical Dimensions of Immunometabolism (PMID:25904920)](https://pubmed.ncbi.nlm.nih.gov/25904920/)
- [Sedoheptulose kinase bridges the pentose phosphate pathway and immune responses in sea cucumber (PMID:32283109)](https://pubmed.ncbi.nlm.nih.gov/32283109/)
- [Selenium-dependent metabolic reprogramming during inflammation and resolution (PMID:33581115)](https://pubmed.ncbi.nlm.nih.gov/33581115/)
- [IRAK4 inhibitor mitigates joint inflammation by rebalancing metabolism malfunction in RA (PMID:34732329)](https://pubmed.ncbi.nlm.nih.gov/34732329/)
- [Deficiency of the sedoheptulose kinase (Shpk) does not alter the ability of hematopoietic stem cells to rescue cystinosis (PMID:34823997)](https://pubmed.ncbi.nlm.nih.gov/34823997/)
- [Sedoheptulose Kinase SHPK Expression in Glioblastoma (PMID:35682658)](https://pubmed.ncbi.nlm.nih.gov/35682658/) and its [Correction (PMID:39941164)](https://pubmed.ncbi.nlm.nih.gov/39941164/)
- [The sedoheptulose kinase CARKL controls T-cell cytokine outputs and migration (PMID:39669692)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11635167/)
- [Metabolic reprogramming and signalling networks in microglial activation (PMID:42031319)](https://pubmed.ncbi.nlm.nih.gov/42031319/)
- [Untargeted metabolomics… non-oxidative branch of the pentose phosphate pathway (PMID:32828637)](https://pubmed.ncbi.nlm.nih.gov/32828637/)
- [OMIM #617213 — Sedoheptulokinase deficiency](https://www.omim.org/entry/617213) (403 to automated retrieval)
- [OMIM *605060 — Sedoheptulokinase; SHPK](https://omim.org/entry/605060) (403 to automated retrieval)
- [Orphanet: Isolated sedoheptulokinase deficiency (ORPHA:440713)](https://www.orpha.net/en/disease/gene/SHPK) / [Orphadata cross-referencing API](https://api.orphadata.com/rd-cross-referencing/orphacodes/440713?lang=en)
- [GARD — Isolated sedoheptulokinase deficiency](https://rarediseases.info.nih.gov/diseases/18652/isolated-sedoheptulokinase-deficiency)
- [NORD/MONDO — isolated sedoheptulokinase deficiency](https://rarediseases.org/mondo-disease/isolated-sedoheptulokinase-deficiency/)
- [HPO / ontology.jax.org annotations for OMIM:617213 and ORPHA:440713](https://ontology.jax.org/api/network/annotation/ORPHA:440713)
- [NCBI Gene — SHPK (GeneID 23729)](https://www.ncbi.nlm.nih.gov/gene/23729) · [GTR — SHPK](https://www.ncbi.nlm.nih.gov/gtr/genes/23729/)
- [UniProt Q9UHJ6 — SHPK_HUMAN](https://rest.uniprot.org/uniprotkb/Q9UHJ6.txt)
- [ClinVar VCV000372202 — SHPK c.355C>T (p.Arg119Ter)](https://www.ncbi.nlm.nih.gov/clinvar/variation/372202/) · [ClinVar VCV000372203 — SHPK c.211G>T (p.Glu71Ter)](https://www.ncbi.nlm.nih.gov/clinvar/variation/372203/)
- [dbSNP rs144071313](https://www.ncbi.nlm.nih.gov/snp/rs144071313)
- [MGI:1921887 — mouse Shpk](https://www.informatics.jax.org/marker/MGI:1921887) · [IMPC — Shpk](https://www.mousephenotype.org/data/genes/MGI:1921887) · [MMRRC:043666-UCD](https://www.mmrrc.org/catalog/sds.php?mmrrc_id=43666)
- [GeneReviews — Cystinosis](https://www.ncbi.nlm.nih.gov/books/NBK1400/)
- [Disorders of the Pentose Phosphate Pathway and Polyol Metabolism (Springer)](https://link.springer.com/chapter/10.1007/978-3-030-67727-5_40)
- [ClinicalTrials.gov API v2](https://clinicaltrials.gov/api/v2/studies) — NCT03897361, NCT05146830, NCT06910813
- [EBI OLS4 (ChEBI, GO term verification)](https://www.ebi.ac.uk/ols4/api/search)
- [OMIA — Online Mendelian Inheritance in Animals](https://www.omia.org/) (no SHPK phene)
