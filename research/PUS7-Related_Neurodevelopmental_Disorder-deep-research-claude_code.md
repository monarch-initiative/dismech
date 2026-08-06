---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T07:13:50.761403'
end_time: '2026-08-01T07:31:22.309598'
duration_seconds: 1051.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PUS7-Related Neurodevelopmental Disorder
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
  web_search_requests: 12
  num_turns: 95
  total_cost_usd: 5.970193249999998
  session_id: 9b8a580e-554c-404e-bdc4-5a88906fa11d
  stop_reason: end_turn
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PUS7-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PUS7-Related Neurodevelopmental Disorder** covering all of the
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

# PUS7-Related Neurodevelopmental Disorder (IDDABS) — Comprehensive Research Report

**Prepared:** 2026-08-01 · **Target:** PUS7-Related Neurodevelopmental Disorder · **MONDO:0032687** · Category: Mendelian (autosomal recessive)

> **Scope and evidence note.** This report is assembled from primary literature (PubMed/PMC), OMIM, HPO, ClinVar, HGNC, UniProt, GTEx, Human Protein Atlas, G2P, Alliance of Genome Resources, MGI/IMPC, and ClinicalTrials.gov. Eight primary references were verified against fetched abstracts/full text already cached in `references_cache/` (PMID:30526862, 30778726, 31583274, 33100873, 35144859, 37067188, 42226002, 42249560). Ontology term IDs below are **suggestions** and must be confirmed with `just validate-terms` / OAK before committing to a KB entry. Sections where no data exist are stated explicitly rather than inferred.

---

## 1. Disease Information

### Overview

PUS7-related neurodevelopmental disorder is an ultra-rare autosomal recessive syndrome caused by biallelic loss-of-function variants in *PUS7*, which encodes the RNA-independent pseudouridine synthase 7. The core phenotype is **moderate-to-severe intellectual disability with delayed or absent speech, progressive (postnatal-onset) microcephaly, short stature/growth retardation, and prominent early-onset behavioral disturbance — most characteristically aggression, with self-injurious behavior in a subset.** It belongs to the growing family of **tRNA-modification disorders** (alongside *PUS1*, *PUS3*, *ADAT3*, *WDR4*, *NSUN2*, *TRMT10A*), in which perturbed translational fidelity disproportionately injures the developing CNS.

The disorder was defined in 2018 by two independent groups. Muda et al. (2026) summarize the current state: *"Pathogenic variants in PUS7, encoding pseudouridine synthase 7, cause a rare neurodevelopmental disorder marked by intellectual disability, microcephaly, short stature, and behavioral disturbances."* (PMID:42226002)

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0032687` | "intellectual developmental disorder with abnormal behavior, microcephaly, and short stature"; synonym IDDABS |
| **OMIM (phenotype)** | **618342** | INTELLECTUAL DEVELOPMENTAL DISORDER WITH ABNORMAL BEHAVIOR, MICROCEPHALY, AND SHORT STATURE (IDDABS) |
| **OMIM (gene)** | **616261** | PSEUDOURIDYLATE SYNTHASE 7; PUS7 |
| **HGNC** | `hgnc:26033` | approved symbol PUS7, "pseudouridine synthase 7" |
| **MedGen** | C5193039 / CUI 1675423 | |
| **UMLS** | C5193039 | |
| **DOID** | `DOID:0081265` | |
| **GARD** | 0018516 | |
| **Orphanet** | **No dedicated ORPHA code identified.** Queries against ORDO via OLS and Orphanet search returned no PUS7-specific entity; the disorder is presumably subsumed under broad ID groupings (e.g., ORPHA:87277 "Rare intellectual disability"). *Report this as a data gap.* |
| **ICD-10** | No specific code. Best available: **F70–F79** (intellectual disabilities), with **Q02** (microcephaly) as an additional code |
| **ICD-11** | No specific code. Nearest: **6A00** (disorders of intellectual development); **LD24.0** microcephaly |
| **MeSH** | No disease-specific descriptor. Indexed via *Intellectual Disability* (D008607), *Microcephaly* (D008831), *Aggression* (D000374), *Intramolecular Transferases* (D019764) |
| **Ensembl / Entrez / UniProt** | ENSG00000091127 / 54517 / Q96PZ0 | |
| **RefSeq transcript** | NM_019042.3 / NM_019042.5 (current) | Used for all published HGVS |
| **G2P (DD panel)** | G2P02633, **confidence: Strong**; biallelic autosomal; loss of function | |
| **ClinGen** | **No curation** — 0 gene-disease validity, 0 dosage, 0 actionability assertions | |

### Synonyms / alternative names

- Intellectual developmental disorder with abnormal behavior, microcephaly, and short stature (**IDDABS**) — OMIM-preferred
- PUS7 deficiency
- PUS7-related neurodevelopmental disorder(s)
- PUS7-related syndrome / PUS7-related intellectual disability
- PUS7-related intellectual disability with speech delay, microcephaly, short stature and aggressive behavior (G2P label)
- Intellectual disability with growth retardation, PUS7-related

### Provenance of the information

Essentially **all** knowledge derives from **aggregated disease-level resources built from individual case reports and small multiplex-family cohorts** — not from EHR-derived or registry-scale populations. The evidence base is:

| Study | PMID | n patients | Origin |
|---|---|---|---|
| de Brouwer et al., *Am J Hum Genet* 2018 | 30526862 | 6 (3 families) | Pakistani, Syrian, Moroccan |
| Shaheen et al., *Hum Genet* 2019 | 30778726 | 3 (2 families) | Saudi, Egyptian |
| Darvish et al., *Neurol Genet* 2019 | 31583274 | 2 (1 family) | Afghan |
| Naseer et al., *Saudi J Biol Sci* 2020 | 33100873 | 2 (1 family) | Saudi (dual diagnosis with *AASS*) |
| Han et al., *Mol Genet Metab* 2022 | 35144859 | 2 (siblings) | USA (NIH UDP) |
| Muda et al., *Am J Med Genet A* 2023 | 37067188 | 1 | Italy |
| Muda et al., *Am J Med Genet A* 2026 | 42226002 | 1 new + review of 17 | Italy |
| Bergès et al., *Clin Genet* 2026 | 42249560 | **13 new (15 new variants)** | Multinational GeneMatcher cohort |

**Total published: ~30 individuals worldwide.** There is no patient registry, no natural-history study, and no HPO-annotated cohort beyond n=9 (the current HPO frequency data for OMIM:618342 derive from the 2018–2019 reports).

---

## 2. Etiology

### Primary causal factor

**Biallelic (homozygous or compound heterozygous) loss-of-function variants in *PUS7* (7q22.3).** This is a monogenic, fully genetic etiology with no known environmental, infectious, or multifactorial contribution. Causality is established by:

1. **Segregation in multiple independent multiplex families** with autozygosity mapping and a combined **LOD score of 3.4** for chr7:96,488,196–109,035,887 (hg19) across two families (PMID:30778726).
2. **Direct biochemical demonstration of the molecular defect.** de Brouwer et al.: *"We show that the disease-related variants lead to abolishment of PUS7 activity on both tRNA and mRNA substrates."* (PMID:30526862). Shaheen et al.: *"Functional characterization of the two mutations confirmed that both result in decreased levels of Ψ13 in tRNAs."* (PMID:30778726)
3. **Model-organism recapitulation of the behavioral phenotype.** *"pus7 knockout in Drosophila melanogaster results in a number of behavioral defects, including increased activity, disorientation, and aggressiveness supporting that neurological defects are caused by PUS7 variants."* (PMID:30526862)
4. **Cross-species complementation failure**, establishing the missense allele as null: *"expression of the yeast pus7-D478Y variant failed to detectably rescue the growth defect of the pus7Δ trm8Δ strain… This result indicates that the yeast Pus7-D478Y variant is a complete loss of function mutation."* (PMID:30778726)
5. **G2P confidence: Strong**; biallelic; loss-of-function mechanism.

### Risk factors

**Genetic (causal):** biallelic *PUS7* LoF is necessary and sufficient. **No susceptibility loci, polygenic risk, or GWAS signals for the Mendelian phenotype.** (Note: the GWAS Catalog contains several variants at 7q22.3 for which PUS7 is merely the *nearest* gene — rs2392747, rs13310815, rs13307225, rs62484733, rs142226001. These are positional annotations, **not** established PUS7 trait associations, and should not be curated as susceptibility evidence.)

**Consanguinity is the dominant epidemiological risk factor.** Nearly all reported families are consanguineous (first-cousin unions in Pakistani, Syrian, Moroccan, Saudi, Egyptian, and Afghan pedigrees). Shaheen et al. mapped disease via *"regions of homozygosity >2Mb as surrogates of autozygosity given the parental consanguinity."* The two US siblings (PMID:35144859) are the notable exception — **nonconsanguineous, compound heterozygous** — showing that the disorder is not restricted to inbred populations.

**Environmental risk factors: none identified.** No toxin, exposure, maternal, perinatal, occupational, dietary, or lifestyle risk factor has been reported or plausibly implicated. Pregnancies and deliveries were repeatedly described as uneventful (e.g., PMID:30778726: *"Her pregnancy, delivery and neonatal history was unremarkable"*).

**Sex:** No sex bias. Both sexes affected in roughly equal numbers across cohorts (autosomal recessive).

### Protective factors

- **Genetic:** None known. Heterozygous carriers (parents, unaffected sibs) are consistently unaffected across all published pedigrees — establishing that a single functional *PUS7* allele is fully sufficient, i.e., the gene is **not haploinsufficient**. This is the only "protective" genetic statement supportable.
- **Hypomorphic-allele effect (genotype-dependent attenuation, not "protection"):** Darvish et al. argue that a missense allele spares the growth phenotype — *"The absence of highly extreme phenotypes such as short stature or microcephaly in this family might reflect genotype–phenotype correlation, since this family presented with a PUS7 missense mutation that may be hypomorphic, while previously reported families carried nonsense or frameshift mutations that may cause loss of function."* (PMID:31583274). Note this is **contradicted** by Shaheen et al., whose p.Asp503Tyr missense patients had *severe* microcephaly and whose yeast complementation showed complete LoF — so the correlation is not robust.
- **Environmental:** No dietary, nutritional, or lifestyle protective factor identified. Avoiding consanguineous union reduces population risk but is a public-health/genetic-counseling consideration, not a biological protective factor.

### Gene–environment interactions

**None documented for the human disorder.** However, two mechanistically relevant GxE-adjacent findings deserve curation as *emerging/hypothesis-level* mechanism, not as disease risk:

- **Stress-inducible cytoplasmic relocalization of PUS7.** *"one of the principal mRNA pseudouridylating enzymes, pseudouridine synthase 7 (PUS7), exhibits a stress-induced accumulation in the cytoplasm of yeast and human epithelial lung cells… engineered PUS7 cytoplasmic localization increases cellular fitness under reactive oxygen species (ROS) and divalent metal ion stress."* (PMID:41997936, *Nat Commun* 2026). Notably, *"the modification status of tRNA sites targeted by PUS7 (Ψ13 and Ψ35) is unperturbed"* under this stress relocalization.
- **Heat-shock-inducible mRNA pseudouridylation by Pus7** in yeast (Schwartz et al., PMID:25219674), i.e., PUS7 activity is condition-dependent.

Whether cellular stress modulates *phenotypic severity* in PUS7-deficient patients is **entirely untested** — a good candidate `KNOWLEDGE_GAP` discussion.

---

## 3. Phenotypes

### 3a. Complete HPO annotation set (OMIM:618342, HPO/ontology.jax.org, n=9 evidence base)

| HPO ID | Term | Reported frequency | Category | Notes |
|---|---|---|---|---|
| **HP:0001249** | Intellectual disability | **9/9 (100%)** | Neurologic / cognitive | Moderate–severe; universal |
| **HP:0000750** | Delayed speech and language development | **9/9 (100%)** | Neurologic / speech | Often absent or <30 words |
| **HP:0001263** | Global developmental delay | **3/3** | Neurologic | |
| **HP:0000718** | Aggressive behavior | **7/8 (~88%)** | Behavioral | **Most discriminating feature; very early onset** |
| **HP:0000252** | Microcephaly | **7/8 (~88%)** | Head/neck | **Progressive/postnatal**; −2.5 to −6.7 SD |
| **HP:0004322** | Short stature | **6/8 (75%)** | Growth | −2.2 to −6.6 SD |
| **HP:0000319** | Smooth philtrum | **6/8** | Facial | |
| **HP:0000232** | Everted lower lip vermilion | **5/8** | Facial | |
| **HP:0004325** | Decreased body weight | **4/6** | Growth | −3 to −3.7 SD |
| **HP:0001270** | Motor delay | **3/6** | Neurologic | Variable — some normal motor milestones |
| **HP:0012471** | Thick vermilion border | 3/5 | Facial | |
| **HP:0000490** | Deeply set eye | 2/3 | Eye | |
| **HP:0100876** | Infra-orbital crease | 2/3 | Facial | |
| **HP:0000463** | Anteverted nares | 2/3 | Facial | |
| **HP:0000407** | Sensorineural hearing impairment | **2/3** | Ear | Progressive in ≥1 case; "less common but more peculiar" |
| **HP:0000668** | Hypodontia | 2/5 | Dental | |
| **HP:0007018** | Attention deficit hyperactivity disorder | 1/3 | Behavioral | |
| **HP:0000752** | Hyperactivity | 1/3 | Behavioral | |
| **HP:0000736** | Short attention span | 1/3 | Behavioral | |
| **HP:0000733** | Motor stereotypy | 1/3 | Behavioral | |
| **HP:0003763** | Bruxism | 1/3 | Behavioral/dental | |
| **HP:0001337** | Tremor | 1/3 | Neurologic | "fine tremors" |
| **HP:0003394** | Muscle spasm | 1/3 | Musculature | "frequent muscle spasms" |
| **HP:0012444** | Brain atrophy | **1/6** | Neuroimaging | Most MRIs normal |
| **HP:0002119** | Ventriculomegaly | 1/2 | Neuroimaging | |
| **HP:0001290** | Generalized hypotonia | "Very rare" | Musculature | Reported in PMID:33100873 |
| **HP:0002240** | Hepatomegaly | 1/6 | Digestive | Unexplained; single report |
| **HP:0000411** | Protruding ear | 1/3 | Ear | |
| **HP:0000369** | Low-set ears | 1/3 | Ear | |
| **HP:0006335** | Persistence of primary teeth | 1/3 | Dental | |
| **HP:0000678** | Dental crowding | 1/3 | Dental | |
| **HP:0011095** | Overjet | 1/3 | Dental | Also "deep overbite" |
| **HP:0000307** | Pointed chin | 1/3 | Facial | |
| **HP:0000347** | Micrognathia | 1/3 | Facial | |
| **HP:0000278** | Retrognathia | reported | Facial | Mandibular retrognathia |
| **HP:0000322** | Short philtrum | 1/3 | Facial | |
| **HP:0002057** | Prominent glabella | 1/3 | Facial | |
| **HP:0000218** | High palate | 1/3 | Facial | "high arched palate with narrow vault" |
| **HP:0002553** | Highly arched eyebrow | 1/3 | Facial | |
| **HP:0000179** | Thick lower lip vermilion | 1/3 | Facial | |
| **HP:0000325** | Triangular face | 1/3 | Facial | |
| **HP:0000431** | Wide nasal bridge | reported | Facial | "broad nasal root" |
| **HP:0000286** | Epicanthus | reported | Eye | |
| **HP:0000494** | Downslanted palpebral fissures | reported | Eye | |
| **HP:0020045** | Esodeviation | 1/3 | Eye | "convergent squint" |
| **HP:0000194** | Open mouth | reported | Facial | |
| **HP:0031936** | Delayed ability to walk | reported | Neurologic | Walked 20–24 months, up to 6 years |
| **HP:0003593** | Infantile onset | 2/3 | Onset modifier | |
| **HP:0011463** | Childhood onset | 1/3 | Onset modifier | |
| **HP:0000007** | Autosomal recessive inheritance | — | Inheritance | |

### 3b. Phenotypes reported in the literature but NOT yet in the HPO annotation set

These should be curated with their own evidence and are the substance of the 2022–2026 phenotypic expansion:

| Suggested HPO | Phenotype | Source | Detail |
|---|---|---|---|
| **HP:0000717** | Autism / Autistic behavior | PMID:31583274, PMID:35144859, PMID:42226002 | *"a neurodevelopmental phenotype including autism spectrum disorder in the proband"*; *"autistic and aggressive behaviors"* |
| **HP:0000742** | Self-injurious behavior | PMID:35144859, PMID:37067188, PMID:42226002, PMID:42249560 | *"face pulling, hair pulling, arm scratching, and finger biting"* |
| **HP:0002360** | Sleep disturbance | PMID:37067188 | *"displays self-injurious behavior, sleep disturbances and motor stereotypies"* |
| **HP:0002149** | Hyperuricemia | PMID:35144859 | Uric acid peaks **8.7** and **6.5 mg/dL** (normal 2.3–5.5); required allopurinol |
| **HP:0001943** | Hypoglycemia | PMID:35144859 | |
| **HP:0002015** | Dysphagia | PMID:33100873 | *"difficulties in swallowing"* |
| **HP:0001250** | Seizure | PMID:33100873 | **Discordant** — "nonspecific seizure" in 1 patient with a dual *AASS* diagnosis; **absent in all others** (see below) |
| **HP:0000091** *(verify)* | Lesch-Nyhan-like phenotype | PMID:35144859 | HPRT1-negative LNS phenocopy: hyperuricemia + self-injury *without* pathogenic *HPRT1* variants |
| — | Craniocervical stenosis | PMID:30778726 | Incidental MRI finding, 1 patient; likely coincidental |

### 3c. Notable NEGATIVE findings (important for differential diagnosis)

- **Epilepsy is characteristically ABSENT.** de Brouwer: seizures marked absent (−) in **all six** patients. Shaheen: *"her behavior is described as aggressive… She has good general health otherwise and has no history of admissions or epilepsy"*; *"No epilepsy was reported. EEG recording was normal"*; *"He never developed epilepsy."* Shaheen explicitly frames this: *"the phenotype we present in the three study patients supports the consistent involvement of cognition and postnatal brain growth and **lack of epilepsy** in PUS7 deficiency."* The one reported seizure case (PMID:33100873) carried a **second pathogenic splice variant in *AASS*** (hyperlysinemia type I, in which seizures are a recognized feature) — that patient is a confounded observation and should be curated with an explicit caveat.
- **Brain MRI is usually normal.** *"Brain MRI showed normal brain architecture"* (×2 timepoints, PMID:30778726); normal in 5/6 of de Brouwer's patients. Structural malformation is *not* part of this disorder despite the severe microcephaly.
- **No mitochondrial disease.** Unlike *PUS1* (MLASA1), PUS7 *"does not modify mitochondrial tRNAs"* (PMID:30526862) — no lactic acidosis, myopathy, or sideroblastic anemia.
- **Normal puberty and secondary sexual characteristics** despite growth failure (PMID:30778726).
- **Normal muscle tone and reflexes** on neurological examination in several patients, despite hypotonia in others.
- **Bone age matched chronological age** (PMID:30778726) — the short stature is not a bone-maturation disorder.

### 3d. Phenotype characteristics

| Dimension | Assessment |
|---|---|
| **Age of onset** | Infantile (2/3) to early childhood (1/3). Developmental delay recognized in the first 1–2 years; speech delay typically flagged at failure to acquire words by age 2. Microcephaly is usually **postnatal/acquired**, though the 2 US siblings had OFC at the 1st and 13th centiles **at birth** with subsequent deceleration (PMID:35144859). Aggression is strikingly early: Muda et al. emphasize *"aggressiveness that manifests at a very early age."* |
| **Severity** | Intellectual disability **moderate to severe**. Documented IQ values: **44** and **48** (Stanford-Binet, PMID:30778726); one patient's *"Formal IQ assessment failed on multiple occasions due to aggressive behavior but is believed to be in the severe intellectual disability range."* At the severe end, the NIH siblings had *"profound developmental delay"* — one walked at 6 years, the other *"remained nonverbal and non-ambulatory at age 9."* |
| **Progression** | **Microcephaly: progressive.** Shaheen documents OFC drifting from −5.7 SD at 4y7m to **−6 SD at 16y**, and −5.2 SD at 2y7m to **−6.7 SD at 14y** — this is the clearest longitudinal signal in the literature and justifies `clinical_course: PROGRESSIVE` on the microcephaly descriptor. **Hearing loss: progressive** (initially attributed to middle-ear effusion, later confirmed sensorineural; *"he developed severe sensorineural hearing loss"* at re-evaluation). **Cognitive impairment: static/non-degenerative** — no reported regression or neurodegeneration; brain atrophy is a rare single observation. **Behavior: worsens through childhood into adolescence**, with several patients requiring pharmacological intervention only at re-evaluation in the teens. |
| **Episodic features** | Self-injurious behavior occurs in **episodes** (PMID:35144859: *"episodes of self-injurious behavior"*) — supports `temporality: RECURRENT`. |
| **Frequency among affected** | See table 3a. Muda et al. (2026) synthesis of 17 cases: *"the most frequent features were moderate/severe intellectual disability, delayed/absent speech, aggressive behavior, microcephaly, mild facial dysmorphisms, motor delay, and short stature."* |
| **Discriminating vs. non-discriminating** | Critically, Muda et al. state: *"These features are common but non-specific, with the exception of aggressiveness that manifests at a very early age. Less common but more peculiar findings included sensorineural hearing loss, autistic traits, self-injurious behavior, and motor stereotypies. The combination of core features with these more specific symptoms should prompt suspicion of a PUS7-related disorder."* This is the key clinical-gestalt statement for the entry. |

### 3e. Quality-of-life impact

**No formal QoL instrument (EQ-5D, SF-36, PROMIS, PedsQL, or disease-specific measure) has been applied to this disorder.** No published QoL data exist. Functional impact must be inferred from clinical narrative and should be curated as descriptive text, not as QoL scores:

| Phenotype | Functional / QoL impact (narrative evidence) |
|---|---|
| Intellectual disability + absent speech | Lifelong dependency; all reported school-age patients required special education (*"He was admitted in a school for special education"*, *"admitted in a special education school with his sib"*); illiteracy (*"He was not able to read or write"*) |
| Aggressive behavior | Disrupts clinical assessment itself (*"She was disruptive throughout the clinical examination"*; formal IQ testing failed repeatedly); necessitates antipsychotic pharmacotherapy; major caregiver burden |
| Self-injurious behavior | Physical injury (facial/hair pulling, arm scratching, finger biting); high-risk behavior requiring protective management |
| Sleep disturbance | Family-wide sleep disruption; recognized amplifier of daytime behavioral dysregulation |
| Sensorineural hearing loss | Compounds an already severe communication deficit; hearing aid required |
| Motor delay / non-ambulation | Mobility dependence in the most severely affected |
| Short stature / low weight | Growth monitoring, feeding/nutrition support |

---

## 4. Genetic / Molecular Information

### Causal gene

***PUS7*** — pseudouridine synthase 7 (RNA-independent pseudouridylate synthase 7)
- **HGNC:** `hgnc:26033` · **OMIM gene:** 616261 · **Entrez:** 54517 · **Ensembl:** ENSG00000091127
- **Locus:** **7q22.3** (GRCh37 chr7:~104.9 Mb)
- **Previous symbol/alias:** FLJ20485; "pseudouridylate synthase 7 homolog (S. cerevisiae)"
- **Transcript for HGVS:** NM_019042.3 (older reports) / NM_019042.5 (current ClinVar)
- **Protein:** UniProt **Q96PZ0**, "Pseudouridylate synthase 7 homolog", **661 aa**
- **Domains:** N-terminal **R3H** domain (predicted ssDNA/RNA binding) + **TRUD** catalytic domain, **residues 370–580** (UniProt)
- **Active site:** **Asp-294** (catalytic nucleophile, UniProt). *Note the apparent inconsistency:* Shaheen et al. place p.Asp503 "within the TRUD domain (370–580)" — Asp503 is a conserved salt-bridge residue in the *E. coli* TruD homolog (Kaya et al. 2004), distinct from the Asp294 nucleophile. Both are catalytically required; do not conflate them.
- **Paralog:** *PUS7L* (pseudouridine synthase 7-like), a separate gene also implicated in severe GDD/epilepsy (noted as "manuscript under review" in PMID:30778726)
- **Chromosomal abnormalities:** *PUS7* is contained within larger 7q22 deletions and ring chromosome 7 in ClinVar (e.g., 7q22.3-31.1 chr7:104536649-109624996 x1; several `NC_000007.13:g.(?_104456677)_(...)del` records). These are **large CNVs with broader phenotypes** and are not IDDABS *per se*; no isolated *PUS7* single-gene deletion causing dominant disease has been reported (consistent with the recessive mechanism).

### Constraint / population genetics

- **gnomAD constraint metrics (pLI, LOEUF, o/e) could not be retrieved** — the gnomAD browser and GraphQL endpoint are JS-rendered and were not fetchable, and GeneCards returned HTTP 403. **Do not cite numeric constraint values without direct verification.** What *can* be asserted: heterozygous carriers are consistently unaffected across every published pedigree, so *PUS7* is **not haploinsufficient**, which predicts a permissive (high) LOEUF and low pLI.
- **Causal variants are absent from population databases.** Repeatedly documented: *"none of them were present in public databases, including the Iranome browser, the Greater Middle-East variome, and the Genome Aggregation database (gnomAD), and disease databases such as ClinVar and the Human Gene Mutation Database"* (PMID:31583274); *"These variant are absent in gnomAD and dbSNP database"* (PMID:33100873).
- **Carrier frequency:** Not established. No population carrier-screening data; no founder allele identified. All variants to date are private/family-specific — including the one **recurrent** variant, **c.329_332delCTGA (p.Thr110Argfs\*4)**, which appears independently in a Saudi family (PMID:30778726) and an Italian patient (PMID:37067188) — recurrence more likely reflects a mutational hotspot than a founder effect.

### Reported pathogenic variants

**From the primary literature (verified):**

| Variant (cDNA) | Protein | Type | Consequence | Family origin | PMID |
|---|---|---|---|---|---|
| c.89_90del | p.Thr30Lysfs\*20 | Frameshift | NMD — *"resulted in nonsense-mediated mRNA decay"* | Pakistani | 30526862 |
| c.1348C>T | p.Arg450\* | Nonsense | NMD | Syrian | 30526862 |
| Deletion of penultimate exon 15 (92 bp) | — | Exonic deletion | **Escapes NMD**; *"results in a frameshift removing the C terminus of PUS7 including 56 amino acid residues of the TruD catalytic domain"* | Moroccan | 30526862 |
| c.1507G>T | p.Asp503Tyr | **Missense** | Complete LoF (yeast complementation failure); within TRUD domain; PolyPhen-2 1.0, SIFT 0, CADD 29.4 | Egyptian | 30778726 |
| c.329_332delCTGA | p.Thr110Argfs\*4 | Frameshift | *"predicted to remove 551 amino acids… leading to complete absence of the TRUD domain (370–580)"* | Saudi; Italian (recurrent) | 30778726; 37067188 |
| c.382G>A | p.Gly128Arg | **Missense** | Conserved Gly (to yeast); within pseudouridine synthase domain; **?hypomorphic** — milder phenotype without microcephaly/short stature | Afghan | 31583274 |
| c.606_607delGA | p.Ser282CysfsTer9 | Frameshift | LoF; **co-occurring *AASS* c.1767-1G>A** (dual diagnosis) | Saudi | 33100873 |
| c.398+1G>T | — | **Splice donor** | *"41 bp or 55 bp deletions into the PUS7 mRNA… introducing frameshift and premature termination"*; ~50% reduction in total PUS7 mRNA | USA (maternal allele) | 35144859 |
| c.1160C>T | p.Thr387Met | **Missense** | Compound het with the above (paternal allele) | USA | 35144859 |
| **15 additional novel variants** | — | — | Not yet individually extractable (paywalled, ahead-of-print) | Multinational | **42249560** |

**From ClinVar (`PUS7[gene]`, retrieved 2026-08-01):** **225 total records; 44 with pathogenic clinical significance.** Representative pathogenic small variants annotated to *Intellectual developmental disorder with abnormal behavior, microcephaly, and short stature*:

`c.1275G>A (p.Trp425Ter)` · `c.998del (p.Asn333fs)` · `c.1918C>T (p.Arg640Ter)` · `c.156_159del (p.Ile54fs)` · `c.1270G>T (p.Glu424Ter)` · `c.424del` · `c.1507del (p.Asp503fs)` · `c.920+4_920+7del` (splice donor) · `c.155_161delinsAAC (p.Leu52fs)` · `c.1399-1G>C` (splice acceptor, **Pathogenic/Likely pathogenic**) · `c.532C>T (p.Arg178Ter)` · `c.393_397del (p.Glu132fs)` · `c.1097_1098del (p.Leu366fs)` · `c.(1757+1_1758-1)_(1848+1_1849-1)del` (multi-exon deletion)

**Variant spectrum summary:** The mutational spectrum is dominated by **truncating alleles** (frameshift, nonsense, splice-disrupting, single/multi-exon deletions), with a minority of **missense variants clustered in or adjacent to the TRUD catalytic domain** (p.Gly128Arg, p.Thr387Met, p.Asp503Tyr). All are **germline**; **no somatic *PUS7* driver mutations** are established in cancer (PUS7's oncologic role is via *overexpression*, not mutation — see §6).

**Functional consequence:** Uniformly **loss of function** (G2P: "loss of function"). No gain-of-function or dominant-negative allele has been described. Importantly, the missense alleles behave as **complete** LoF in orthogonal assays, not partial — arguing against a simple truncating-vs-missense severity gradient.

**ACMG/AMP classification support:** Truncating alleles typically reach Pathogenic via PVS1 + PM2 + PP1 (segregation) ± PS3 (functional). Shaheen et al. explicitly propose the biochemical assay as an ACMG PS3 tool: *"this may also serve as a very helpful assay for the proper classification of variants of unknown significance that will inevitably be encountered in this gene."*

### Modifier genes

**None identified.** Phenotypic variability (presence/absence of short stature, hearing loss, autistic features, self-injury) is unexplained and is a stated open question: *"it also suggests that other aspects are more variable… it remains to be seen how common this, and indeed other, clinical features are in PUS7-related syndrome"* (PMID:30778726). Bergès et al. (PMID:42249560) explicitly frame their 13-patient cohort as *"allowing for improved genotype-phenotype correlations."*

**Caution — dual diagnosis, not modification:** the *AASS* splice variant co-segregating in the Saudi family (PMID:33100873) is a **second independent Mendelian diagnosis** (hyperlysinemia type I), a classic consanguinity artifact. Do not curate it as a *PUS7* modifier.

### Epigenetic information

- **Classical epigenetics (DNA methylation, histone marks):** **no data.** No methylation episignature has been developed for PUS7 deficiency (in contrast to many Mendelian NDDs). No ENCODE/Roadmap/DiseaseMeth findings specific to this disorder. This is a notable, tractable gap — an EpiSign-style episignature would be a high-value diagnostic addition.
- **Epi*transcriptomics* is the disease mechanism itself.** PUS7 is an **RNA-modification "writer."** Pseudouridine (Ψ) is *"the most abundant and widespread type of RNA epigenetic modification in living organisms"* (PMID:29628141) and *"the most abundant post-transcriptional modification in RNA, which is primarily thought to stabilize secondary structures of RNA"* (PMID:30526862). This disorder is therefore best classified as an **epitranscriptomic disorder** — the pathological "epigenetic change" is loss of Ψ marks on tRNA, tRFs, mRNA, and snRNA. See §6.

---

## 5. Environmental Information

- **Environmental factors:** **None.** No toxin, radiation, pollutant, occupational, or teratogenic exposure is implicated. CTD/TOXNET searches return no PUS7-disorder environmental associations. (CTD does contain cadmium–*circPUS7* chemical-transformation data — PMID:34232319, a cancer/in-vitro finding entirely unrelated to the NDD.)
- **Lifestyle factors:** **Not applicable.** No dietary, smoking, alcohol, or activity factor influences onset or course. Note the **absence of a dietary treatment** distinguishes this from other tRNA/metabolic NDDs.
- **Infectious agents:** **Not applicable** — this is not an infectious or infection-triggered disorder. (Two tangential findings must **not** be conflated with etiology: PUS7-mediated Ψ in SARS-CoV-2 RNA–host interactions, PMID:38028201; and Ψ prevalence in KSHV, PMID:40961145. These concern PUS7's role in *viral* RNA biology, not IDDABS causation.)
- **Perinatal/obstetric factors:** consistently unremarkable. One report of transient neonatal respiratory difficulty requiring oxygen and physiological jaundice — coincidental.

---

## 6. Mechanism / Pathophysiology

### 6.1 Normal PUS7 biology

**PUS7 is a stand-alone, RNA-independent (snoRNA-independent) pseudouridine synthase** of the **TruD family** — one of 13 human PUS enzymes, and one of only two (*PUS7*, *TRUB1*) that are principal **mRNA** Ψ writers. It isomerizes uridine to 5-ribosyluracil (pseudouridine, Ψ; **CHEBI:17802** *verify*), which *"permits additional hydrogen bonding"* and increases base stacking, historically framed as an RNA-stabilizing mark.

**Substrate repertoire (each substrate class defines a distinct downstream mechanism):**

| Substrate | Site | Function | Evidence |
|---|---|---|---|
| **Cytosolic tRNAs** | **Ψ13** (≥10–17 tRNA species) | Canonical target; tRNA stability/decoding | PMID:30526862, 30778726, 41136621 |
| **pre-tRNA-Tyr(GUA)** | **Ψ35** (anticodon) | Pre-tRNA processing | PMID:30778726 (yeast Behm-Ansmant 2003) |
| **Cytosolic tRNAs** | **Ψ50** (13 sites, 8 tRNA types) | Codon-biased translational control | PMID:35121864 |
| **tRNA-derived fragments (mTOG/5′TOG tRFs)** | **Ψ8** within the mTOG sequence | **Translation repression** via PABPC1 binding | PMID:29628141, 35292784 |
| **mRNAs (dozens–hundreds)** | **UGΨAG / UNUAR / USUAG** motif | Stability, translation, splicing near alternative splice sites | PMID:25219674, 28073919, 42532042, UniProt |
| **U2 snRNA** | **Ψ35** (branch-site recognition region) | Pre-mRNA splicing fidelity | PMID:21131909, 15611063 |
| **7SK snRNA** | Ψ | **Pol II transcription elongation** control via P-TEFb release | PMID:41168165 |
| **Mitochondrial tRNAs** | — | **NOT a substrate.** *"PUS7, which does not modify mitochondrial tRNAs"* | PMID:30526862 |

**Substrate recognition** requires more than the linear motif. Human PUS7 has *"two additional subdomains"* absent in the bacterial homolog that *"contribute to tRNA recognition through increased interactions along the tRNA substrate,"* and *"all structural elements of tRNA are required for productive interaction with PUS7 as the consensus sequence of target RNA alone is not sufficient"* (PMID:34718722). Yeast Pus7 is *"a promiscuous enzyme"* / *"an opportunistic enzyme that binds and modifies substrates with diverse sequences and structures"*, with *"factors beyond inherent enzyme properties—such as enzyme localization, RNA structure, and competition with other RNA-binding proteins"* setting substrate choice (PMID:35058356). Most recently, *"USUAG, target uridine accessibility, and RNA architecture govern mRNA alteration by PUS7"* and *"PUS7 function varies among cell types separate from expression amounts"* (PMID:42532042) — a cell-type-specific determinant that may explain neural selectivity.

**Localization:** **nucleus** (UniProt; HPA: *"Mainly nuclear expression in all tissues"*, nucleoplasm), with **stress-inducible cytoplasmic relocalization** that expands mRNA (but not tRNA) targets (PMID:41997936).

**Expression:** Broad/housekeeping — HPA **"Low tissue specificity" (Tau 0.28)**, "Non-specific — Basic cellular processes." GTEx median TPM: highest in EBV-transformed lymphocytes (21.1), fibroblasts (18.2), adipose (12.1), thyroid (11.9). **Within brain there is a striking regional gradient: cerebellar hemisphere 11.2 and cerebellum 10.0 TPM vs. 2.0–4.8 TPM in cortex, hippocampus, amygdala, and basal ganglia** — i.e., cerebellar expression is 3–5× cortical. de Brouwer et al. leverage exactly this: *"The relatively high PUS7 expression levels in cerebellum and tibial nerve support a more specific role for PUS7 in neurodevelopment."*

### 6.2 The causal chain (upstream → downstream)

```
[MOLECULAR / genetic]
Biallelic PUS7 loss-of-function variant (frameshift/nonsense/splice → NMD;
exon-15 deletion → NMD-escaping TruD-truncated protein; missense → catalytically dead)
        │
        ▼
[MOLECULAR] Loss of PUS7 pseudouridine synthase activity
  "the disease-related variants lead to abolishment of PUS7 activity on both
   tRNA and mRNA substrates" (PMID:30526862)
        │
        ├──────────────┬────────────────┬─────────────────┐
        ▼              ▼                ▼                 ▼
[MOLECULAR]      [MOLECULAR]      [MOLECULAR]       [MOLECULAR]
Loss of tRNA     Loss of Ψ8 on    Loss of mRNA Ψ    Loss of snRNA Ψ
Ψ13 (≥10-17      mTOG/5'TOG       at UGΨAG motifs   (U2 Ψ35; 7SK Ψ)
tRNAs) ± Ψ35,    tRFs             (dozens-hundreds  → splicing fidelity /
Ψ50                               of mRNAs)          Pol II elongation
        │              │                │                 │
        ▼              ▼                ▼                 ▼
Reduced tRNA     Failure of tRF-  Altered mRNA      Aberrant pre-mRNA
stability &      mediated         stability &        splicing; altered
decoding         PABPC1 blockade  translation        transcription
fidelity              │                │                 │
        └──────────────┴────────────────┴─────────────────┘
                              │
                              ▼
[CELLULAR — convergent hub] DYSREGULATED / GLOBALLY UPREGULATED PROTEIN SYNTHESIS
  "PUS7 inactivation in embryonic stem cells impairs tRF-mediated translation
   regulation, leading to increased protein biosynthesis" (PMID:29628141)
  Patient fibroblasts: elevated puromycin incorporation (SUnSET, p=2.1e-3),
  elevated MYC protein with normal MYC mRNA (p=4.9e-4) (PMID:35144859)
                              │
        ┌─────────────────────┼──────────────────────┐
        ▼                     ▼                      ▼
[CELLULAR]             [CELLULAR]              [CELLULAR]
Impaired neural        Impaired stem-cell      Mildly decreased HPRT1
progenitor             commitment / germ-      protein (normal mRNA)
proliferation &        layer specification     (p=3.5e-3) → purine
differentiation        "defective germ layer   salvage insufficiency
(inferred)             specification"
        │                     │                      │
        ▼                     ▼                      ▼
[TISSUE]               [TISSUE]                [ORGANISM]
Reduced brain          Reduced somatic         Hyperuricemia
growth; cerebellum     growth                  (8.7, 6.5 mg/dL)
disproportionately            │                      │
vulnerable (highest           │                      │
regional expression)          │                      │
        │                     │                      │
        ▼                     ▼                      ▼
[ORGANISM] Progressive        [ORGANISM]         [ORGANISM] Lesch-Nyhan-like
postnatal microcephaly        Short stature,     self-injurious behavior +
        │                     low weight         hyperuricemia (HPRT1-negative)
        ▼
[ORGANISM] Intellectual disability, absent/delayed speech,
aggression, autistic features, stereotypies, sleep disturbance,
sensorineural hearing loss
```

### 6.3 Mechanism detail by module

**(a) tRNA hypomodification → translational infidelity (the canonical arm).**
Patient EBV-LCLs show *"the pseudouridylation signal in EBV-LCLs of affected individuals was essentially abolished at the PUS7 substrates at position 13"* and *"All of these sites were at position 13 of various tRNAs"* (PMID:30526862). CMCT primer-extension and HPLC in an independent cohort: *"tRNAHis(GTG) and tRNAGlu(CTC) from LCLs of patients with the Asp503Tyr mutation lacked Ψ13"*, and purified tRNA-Val(AAC) *"showed a reduction of 0.88 moles of Ψ relative to that from a WT control (1.75 moles/mole compared to 2.63 moles/mole)"* while *"the levels of the other analyzed tRNAVal(AAC) modifications (m5C, m2G) were very similar"* — a clean, site-specific defect (PMID:30778726).

The disease-mechanism framing is explicit: *"We and others have previously emphasized the predilection of Mendelian diseases caused by tRNA modification genes to CNS involvement and how this suggests the vulnerability of the brain to any perturbation of tRNA modification, presumably through its deleterious effect on protein synthesis"* (PMID:30778726).

**(b) tRF (mTOG)–PABPC1 axis → loss of translational braking (the best-resolved arm).**
PUS7 Ψ-modifies **mini-tRFs containing a 5′ terminal oligoguanine (mTOG)** at U8. Ψ-mTOG binds and inhibits **PABPC1**, and *"this hinders the recruitment of translational co-activator PABPC1-interacting protein 1 (PAIP1) and strongly represses the translation of transcripts sharing pyrimidine-enriched sequences (PES) at the 5' untranslated region (UTR), including 5' terminal oligopyrimidine tracts (TOP) that encode protein machinery components"* (PMID:35292784). Loss of PUS7 therefore **releases the brake** on 5′TOP/PES mRNA translation — i.e., derepresses translation of the translational machinery itself, a feed-forward amplification. *"tRNA-derived fragments with five consecutive guanine residues are classified as 5′TOG, and these are significantly depleted in PUS7-knockout cells"* (PMID:29628141).

**(c) Codon-biased translation via tRNA Ψ50.**
In glioblastoma stem cells, *"13 PUS7-dependent pseudouridine sites in 8 tRNA types"* were mapped; *"tRNA-Arg-CCG-2–1 at position 50 exhibited a dramatic decrease in pseudouridine modification upon PUS7 KO"*, and *"PUS7-mediated pseudouridylation in tRNA inhibits codon-specific translation."* Loss of PUS7 raises translation efficiency of the affected tRNA and de-represses CGG-codon-rich transcripts such as TYK2 at the **protein but not mRNA** level (PMID:35121864). This provides a *codon-level* mechanism for how a global "writer" loss produces **selective** proteome changes — the most plausible explanation for tissue-selective phenotypes.

**(d) Purine-salvage secondary hit → Lesch-Nyhan phenocopy.**
The single most clinically actionable mechanistic finding: *"the dysregulation of protein translation also resulted in mildly decreased levels of HPRT1 protein suggesting an association between dysregulated protein translation and the LNS-like phenotypic findings"* (PMID:35144859). Patients had hyperuricemia (peaks 8.7 and 6.5 mg/dL vs normal 2.3–5.5) and self-injurious behavior **without pathogenic *HPRT1* variants**, and were treated with allopurinol. This is a *translationally-mediated* partial HPRT1 deficiency — a genuine secondary metabolic mechanism, and mechanistically the disorder's link to purine metabolism (KEGG hsa00230 purine metabolism).

Critically, the paper distinguishes this from cancer: *"Patient fibroblasts demonstrated upregulation of protein synthesis, including elevated MYC protein, but did not exhibit increased rates of cell proliferation"* — high MYC/high translation **without** proliferation, i.e., neurodevelopmental rather than oncogenic output. The authors frame the paradox in the abstract: *"Upregulated protein translation is a hallmark of cancer and is implicated in autism spectrum disorder, but the risks of developing each disease do not appear to be correlated with one another."*

**(e) Splicing and transcription arms (mechanistically established, disease-relevance untested).**
UniProt: PUS7 *"regulates pre-mRNA splicing near alternative splice sites."* U2 snRNA Ψ35 in the branch-site recognition region is required for efficient splicing (PMID:15611063, 21131909). And 7SK Ψ controls Pol II pausing: *"PUS7 loss leads to hypo-pseudouridylation of 7SK, which promotes dissociation of the positive transcription elongation factor b (P-TEFb) complex from 7SK. The release of P-TEFb from 7SK increases serine 2 phosphorylation (Ser2P) in the RNA Pol II C-terminal domain and enhances transcription elongation"* (PMID:41168165). Whether either arm contributes to IDDABS is **unknown** — curate as a mechanistic hypothesis (`status: EMERGING`) with a `KNOWLEDGE_GAP`.

**(f) Direct neuronal/synaptic mechanism (the most disease-proximal recent evidence).**
Liu et al. 2025 provide the first *in vivo* mammalian link between PUS7 and synaptic plasticity: *"we identified selective Ψ enrichment at exons of synaptic regulatory genes within ILPFC during fear extinction learning. Fear extinction in the ILPFC drives concomitant exonic Ψ deposition and upregulation of synaptogenic transcripts, processes that involve pseudouridine synthase PUS7. Crucially, PUS7 knockdown in the ILPFC selectively impaired fear extinction memory formation without altering baseline fear expression, establishing a causal link between Ψ-dependent RNA processing and activity-dependent synaptic structural remodeling in this microcircuit."* (PMID:41094471). This supplies a plausible mechanism for the *behavioral* phenotype (aggression, autistic features, impaired learning) distinct from the growth phenotype — and is a strong candidate for a dedicated pathophysiology node.

**(g) Neuronal cell-autonomy (Drosophila).**
*"expression of pus7 only in neurons by using the elav-Gal4 driver was sufficient to alter fly behavior, suggesting that Pus7 exerts its activity through a neuronal function"* (PMID:30526862). This is the key evidence that the mechanism is **neuron-intrinsic**, not secondary to systemic growth failure.

### 6.4 Molecular pathways, cell types, and processes

**Pathways (KEGG/Reactome/GO):**
- RNA modification / pseudouridine synthesis (**GO:0001522**, **GO:0031119** tRNA pseudouridine synthesis, **GO:1990481** mRNA pseudouridine synthesis)
- tRNA processing and maturation; **tRNA pseudouridine(13) synthase activity (GO:0160150)**
- Translation initiation control (eIF4F/PABPC1–PAIP1 axis); **negative regulation of translation (GO:0017148)**
- mTOR/5′TOP mRNA translational program (indirect, via PES/TOP derepression)
- Pre-mRNA splicing (**GO:0008380**), mRNA processing (**GO:0006397**)
- Pol II transcription elongation (P-TEFb/7SK)
- **Purine metabolism / purine salvage** (KEGG hsa00230) — via HPRT1 protein reduction
- Stem-cell commitment: **regulation of hematopoietic stem cell differentiation (GO:1902036)**, **regulation of mesoderm development (GO:2000380)**

**Additional suggested GO BP terms for pathophysiology nodes** *(verify with OAK)*: GO:0006412 translation; GO:0045727 positive regulation of translation; GO:0022008 neurogenesis; GO:0021895 cerebral cortex neuron differentiation; GO:0050803 regulation of synapse structure or activity; GO:0007612 learning; GO:0040007 growth; GO:0008285 negative regulation of cell population proliferation.

**Molecular functions:** GO:0009982 pseudouridine synthase activity; GO:0160150 tRNA pseudouridine(13) synthase activity; GO:0003723 RNA binding; GO:0019899 enzyme binding.

**Cellular components:** **GO:0005634 nucleus** (primary); GO:0005654 nucleoplasm (HPA); GO:0005737 cytoplasm (stress-induced, PMID:41997936); GO:0005829 cytosol (site of tRF/PABPC1 action).

**Cell types (CL — suggestions, verify):**
| CL term | Cell type | Basis |
|---|---|---|
| CL:0000540 | neuron | Cell-autonomous requirement (elav-Gal4 rescue); ILPFC knockdown |
| CL:0000047 | neuronal stem cell / CL:0000031 neuroblast | Inferred: progenitor-pool reduction underlying microcephaly (**not directly demonstrated — knowledge gap**) |
| CL:0000121 | Purkinje cell | Speculative: cerebellum has 3–5× higher PUS7 expression than cortex (GTEx). No cerebellar pathology reported — flag as hypothesis. |
| CL:0000037 | hematopoietic stem cell | Directly demonstrated: impaired engraftment of PUS7-depleted HSPCs (PMID:29628141, 35292784) — **no clinical hematologic phenotype in patients**, an important human–model mismatch |
| CL:0002322 | embryonic stem cell | PUS7-KO ESC: increased protein synthesis, defective germ-layer specification |
| CL:0000057 | fibroblast | Patient-derived assay system (SUnSET, MYC, HPRT1) |
| CL:0000542 | lymphocyte (EBV-LCL) | Patient-derived assay system (CMCT, HPLC Ψ13) |
| CL:0000855 | sensory hair cell / CL:0000202 auditory hair cell | Inferred for SNHL — **not demonstrated** |

### 6.5 Protein dysfunction

- **Truncating alleles:** transcript eliminated by **NMD** — *"mRNA transcripts containing the premature stop codons were eliminated through surveillance mechanisms"* (PMID:31583274). Effectively a **null**.
- **Exon 15 deletion:** *"escaped the nonsense-mediated mRNA decay to encode a mutant protein missing the C terminus including the TruD catalytic domain"* — a **stable but catalytically dead protein**, mechanistically distinct (potential for aberrant substrate sequestration; untested).
- **Missense alleles:** catalytic-domain destabilization. p.Asp503Tyr disrupts a residue *"involved in a salt bridge in the E. coli TruD homolog"*; p.Gly128Arg alters *"an evolutionarily conserved glycine down to yeast."*
- **No misfolding/aggregation, no gain of function, no dominant-negative** effect described.
- Structural resources: **X-ray crystal structure of human PUS7 at 2.26 Å** (PMID:34718722); *S. cerevisiae* Pus7 structure (PMID:35058356); *T. thermophilus* TruD (PMID:15135053); AlphaFold model available for Q96PZ0.

### 6.6 Metabolic, immune, and tissue-damage mechanisms

- **Metabolic:** the only established metabolic abnormality is **hyperuricemia via translationally-reduced HPRT1** (purine salvage insufficiency; PMID:35144859) — plus **hypoglycemia** in the same siblings (mechanism unexplained). No amino-acid, organic-acid, lipid, or energy-metabolism defect. **No lactic acidosis** (contrast *PUS1*/MLASA1). No metabolomic/lipidomic study of patients exists.
- **Immune system:** **no immune involvement in the human disorder.** No immunodeficiency, autoimmunity, or inflammation reported. (Adjacent, non-clinical: PUS7 in macrophage phenotype regulation — VUB research portal; *Trub1*-mediated Ψ dispensable for immune development, PMID:41876669. Neither bears on IDDABS.)
- **Tissue damage mechanisms:** **no oxidative stress, ischemia, fibrosis, necrosis, or degeneration.** This is a **developmental/hypoplastic** disorder — failure of brain and somatic *growth* — not a destructive or neurodegenerative one. The single brain-atrophy report (1/6) is an outlier and MRI is normal in most patients.
- **Biochemical abnormalities (patient-detectable):** loss of tRNA Ψ13 (CMCT/HPLC); elevated global protein synthesis; elevated MYC protein; reduced HPRT1 protein; elevated serum uric acid.

### 6.7 Molecular profiling and advanced technologies

| Modality | Status for PUS7 deficiency |
|---|---|
| **Transcriptomics** | No patient-tissue RNA-seq published. PUS7-KO ESC/GSC/HCT116 transcriptomes and Ψ-maps exist in the mechanism literature. |
| **Ψ-mapping (the disease-specific "omics")** | Well developed as a *research* readout: Ψ-seq (PMID:25219674), CMCT primer extension, RBS-seq, **BACS/2-bromoacrylamide-assisted cyclization sequencing** (PMID:41136621), quantitative Ψ profiling (PMID:36997645, 39349603), and **nanopore direct-RNA** approaches incl. **Nano-Mod-Amp** (PMID:42532042, 38766185, 40829803, 41571893). PMID:41698914 reports *"Quantitative analysis of small RNA pseudouridylation reveals interplay of PUS enzymes."* |
| **Proteomics** | Isotope-exchange proteomics defined the mTOG–PABPC1 RRM interaction (PMID:35292784); quantitative proteomics showed *"reshaping of the proteome upon PUS7 relocalization under stress"* (PMID:41997936). Dataset: **PRIDE PXD008676** (Guzzi 2018). No patient proteomics. |
| **Metabolomics / lipidomics** | **None** for this disorder. |
| **Epigenomics** | **None** — no episignature. |
| **Single-cell / spatial** | **None** for PUS7 deficiency. A major gap: single-cell Ψ-mapping in developing human brain would directly test the neural-progenitor hypothesis. |
| **Functional genomics screens** | PUS7 KO/KD across HCT116 (BACS, PMID:41136621), ESCs, GSCs, HeLa (commercial PUS7-KO HeLa line, Abcam ab265407). DepMap dependency data exist for cancer lines but not for neural models. |
| **Suggested datasets for a KB entry** | PRIDE PXD008676; GEO series accompanying PMID:29628141, 35121864, 41136621, 41094471 (accessions not individually verified here — **fetch before curating**) |

---

## 7. Anatomical Structures Affected

### Organ level

| Level | Structure | UBERON *(verify)* | Involvement |
|---|---|---|---|
| **Primary** | Brain | UBERON:0000955 | Reduced growth → progressive microcephaly; architecture normally preserved |
| | Cerebral cortex | UBERON:0000956 | Cognitive/language/behavioral phenotype localizes here |
| | Cerebellum | UBERON:0002037 | **Highest regional PUS7 expression** (GTEx); mechanistically implicated, clinically silent |
| | Prefrontal cortex (infralimbic/ILPFC homolog) | UBERON:0000451 / UBERON:0002743 | PUS7-dependent Ψ required for fear-extinction memory (mouse, PMID:41094471) |
| **Secondary** | Inner ear / cochlea | UBERON:0001846 / UBERON:0001844 | Sensorineural hearing loss (2/3 in one cohort), progressive |
| | Skeleton / long bones | UBERON:0001474 | Short stature (proportionate; **normal bone age**) |
| | Craniofacial skeleton, mandible, maxilla | UBERON:0010363 / UBERON:0001684 | Mild dysmorphism; micrognathia, retrognathia, hypoplastic zygomatic arches |
| | Teeth / dentition | UBERON:0001091 / UBERON:0003672 | Hypodontia, conical teeth, retained deciduous teeth, crowding, overjet/overbite |
| | Skeletal muscle | UBERON:0001134 | Hypotonia (rare), muscle spasms, fine tremor |
| | Kidney (functional, via urate) | UBERON:0002113 | Hyperuricemia — risk of urate nephropathy/stones if untreated |
| | Liver | UBERON:0002107 | Hepatomegaly, 1/6, unexplained |
| | Eye / extraocular muscles | UBERON:0000970 | Convergent squint/esodeviation, deep-set eyes |
| **Body systems** | **Nervous system** (primary), **musculoskeletal/growth**, **auditory/sensory**, **craniofacial/dental**, **metabolic (purine)** | | |
| **NOT involved** | Heart, lungs, GI tract (beyond dysphagia), immune system, hematopoietic system (despite model data), mitochondria | | |

**Lateralization:** All structural findings are **bilateral and symmetric** (microcephaly, hearing loss, dysmorphism, short stature). No lateralized or asymmetric involvement reported. Note the intriguing negative: laterality defects (a feature of motile-ciliopathy) are absent, and PUS7 has no cilia link.

### Tissue and cell level

- **Nervous tissue** (UBERON:0003714) — neurons (CL:0000540) are the cell type with demonstrated cell-autonomous requirement (elav-Gal4 rescue; ILPFC knockdown).
- **Peripheral nerve** — GTEx tibial nerve is among the higher-expressing tissues; de Brouwer cites it as supporting neurodevelopmental specificity. **No clinical peripheral neuropathy has been reported** — an unexploited hypothesis worth flagging (nerve conduction studies have not been systematically performed).
- **Connective/skeletal tissue** — growth failure; **cartilage/growth plate not studied**.
- **Cochlear sensory epithelium** — inferred for SNHL; no histopathology.
- **Assay tissues (not disease sites):** dermal fibroblasts, EBV-LCLs, peripheral blood.

### Subcellular level

| GO CC *(verified via UniProt)* | Compartment | Relevance |
|---|---|---|
| **GO:0005634** | Nucleus | Primary PUS7 localization; site of tRNA/pre-mRNA/snRNA modification |
| GO:0005654 | Nucleoplasm | HPA-annotated subcellular location |
| GO:0005737 / GO:0005829 | Cytoplasm / cytosol | Stress-induced relocalization (PMID:41997936); site of tRF–PABPC1 translational repression and of ribosomal translation |
| GO:0005840 | Ribosome | Downstream effector compartment (dysregulated translation) |
| **NOT GO:0005739** | Mitochondrion | **Explicitly excluded** — PUS7 does not modify mitochondrial tRNAs |

**Histopathology:** **No human neuropathology, biopsy, or autopsy data exist for this disorder.** Report as a gap.

---

## 8. Temporal Development

### Onset

- **Congenital/prenatal:** Head circumference is usually **normal at birth** — the microcephaly is characteristically **acquired/postnatal and progressive**. Shaheen et al.: *"a phenotype comprising intellectual disability and progressive microcephaly."* Exception: the two US siblings had OFC at the 1st and 13th centiles at birth with subsequent deceleration (PMID:35144859), and low birth weight (1500 g, −3 SD; 2500 g, −2 SD) occurs (PMID:30778726) — so prenatal growth restriction is present in a subset.
- **Infantile onset (HP:0003593, 2/3)** — developmental delay evident in year 1–2.
- **Childhood onset (HP:0011463, 1/3)** — milder cases may present at 3–5 years for developmental/speech evaluation.
- **Onset pattern:** **insidious and chronic.** No acute, subacute, or crisis presentation. Notably **no metabolic decompensation** — this disorder does *not* conform to `metabolic_intoxication_decompensation`.
- **Presenting complaint:** most often speech delay ± unexplained ID/microcephaly. Typical ages at first genetics evaluation in the literature: 2y7m, 4y7m, 6y.

### Progression

| Domain | Course |
|---|---|
| **Microcephaly** | **PROGRESSIVE** — best-documented. Serial OFC: −5.7 SD (4y7m) → −6 SD (16y); −5.2 SD (2y7m) → **−6.7 SD (14y)** |
| **Short stature** | **PROGRESSIVE** — height −4.9 SD (4y7m) → −4 SD (16y) in one; −5.5 SD (2y7m) → **−6.6 SD (14y)** in his sib |
| **Hearing loss** | **PROGRESSIVE** — initially attributed to chronic middle-ear effusion, later confirmed sensorineural and "severe" by adolescence |
| **Cognition** | **STATIC (non-degenerative)** — no regression, no loss of acquired skills. Deficits are developmental. |
| **Behavior** | **Worsens through childhood into adolescence** — aggression and self-injury escalate; several patients only required risperidone at teenage re-evaluation |
| **Motor** | **Variable and non-progressive** — some normal motor milestones (*"her motor development was described as normal"*), others walked at 20–24 months or as late as 6 years; one non-ambulatory at 9 years |
| **Overall course pattern** | **Chronic, lifelong, non-relapsing**; growth/head-circumference parameters progressive, neurocognition static, behavior escalating |
| **Disease stages** | **No staging system exists.** No AJCC/WHO classification applies. |
| **Duration** | **Lifelong.** Oldest reported patients are 16–18 years — **no adult natural-history data.** |

### Patterns

- **Remission:** **None** — neither spontaneous nor treatment-induced. No disease-modifying therapy exists.
- **Critical periods:** Mechanistically, the vulnerable window is **early embryogenesis and early postnatal brain growth**. Guzzi et al.: *"a Ψ-driven posttranscriptional program steers translation control to impact stem cell commitment during early embryogenesis"* (PMID:29628141) — implying the primary insult is prenatal/perinatal and largely irreversible by the time of diagnosis. Practical intervention windows are therefore **symptomatic**: early behavioral/speech intervention, early audiological surveillance (hearing loss is progressive and remediable with amplification), and early hyperuricemia detection (allopurinol prevents urate complications).
- **Anticipation:** **Not applicable** — not a repeat-expansion disorder.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: not established. Ultra-rare.** No published prevalence or incidence estimate; no Orphanet epidemiology record (no ORPHA code). The only quantitative anchor is the **cumulative case count: ~30 published patients worldwide as of mid-2026** (16 through 2025 per Muda et al.; +1 Muda 2026; +13 Bergès 2026).
- **Recommended dismech `Prevalence` record:** `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`, `population: Worldwide`, `notes: "~30 patients reported in the literature 2018–2026 (16 through 2025, +1, +13)."` Do **not** invent a `rate_per_100000`.
- **Supporting quotes:** *"Since the first report in 2018, only 16 patients have been described"* (PMID:42226002); *"Since 2018, PUS7 deficiency has been described in 15 patients"* (PMID:37067188); *"papers reported that variants in PUS7 in 16 patients"* (PMID:42249560).
- **Incidence:** unknown.
- **Ascertainment caveat:** The trajectory (6 → 16 → ~30 in 8 years, with 13 arriving in a single GeneMatcher cohort) indicates substantial **under-ascertainment**, not true ultra-rarity of the genotype. Muda et al. explicitly urge broader testing: *"We recommend looking for PUS7 pathological variants when performing whole exome sequencing in children with this constellation of neurodevelopmental and behavioral signs."*

### Genetic etiology parameters

| Parameter | Assessment |
|---|---|
| **Inheritance** | **Autosomal recessive** (HP:0000007). Confirmed across all families; G2P allelic requirement "biallelic autosomal." |
| **Genotype** | Predominantly **homozygous** (consanguineous families); **compound heterozygous** documented in the nonconsanguineous US siblings (PMID:35144859). |
| **Penetrance** | Appears **complete** in biallelic carriers — no unaffected homozygote reported. Sample size (~30) is too small for a formal estimate. Heterozygotes are uniformly unaffected. |
| **Expressivity** | **Variable.** Consistent: ID, speech delay, aggression. Variable: short stature, microcephaly severity, hearing loss, autistic features, self-injury, motor delay. *"Short stature and hearing loss were variable in these patients"* (PMID:30778726). Intrafamilial variability is documented — two brothers with the same variant differed in aggression (*"he did not show aggressiveness like his brother"*). |
| **Genetic anticipation** | Not applicable. |
| **Germline/somatic mosaicism** | **Not reported.** |
| **Founder effects** | **None identified.** All variants are private/family-specific. c.329_332delCTGA recurs in Saudi and Italian patients — more plausibly a **mutational hotspot** than a shared founder. |
| **Consanguinity** | **Central.** First-cousin unions in most reported families; autozygosity mapping (ROH >2 Mb) was the discovery route in several. Recurrence risk 25% per pregnancy for carrier couples. |
| **Carrier frequency** | **Unknown.** No screening data. Given ultra-rarity and private alleles, gene-level (not variant-level) sequencing is required for carrier testing. |

### Population demographics

- **Affected populations:** Reported ancestries — **Pakistani, Syrian, Moroccan, Saudi Arabian, Egyptian, Afghan, Italian, and the multinational Bergès cohort** (contributing centers: France, Belgium, Netherlands, Germany, UK, USA, Pakistan, Saudi Arabia, Australia, Luxembourg). The heavy Middle Eastern/North African/South Asian representation reflects **consanguinity-driven ascertainment**, not population-specific genetic susceptibility.
- **Geographic distribution:** Global; no endemic region. The 2026 European/multinational cohorts confirm the disorder is not geographically restricted.
- **Variant geography:** No variant shows geographic clustering. p.Thr110Argfs\*4 in Saudi and Italian patients argues against geographic partitioning.
- **Sex ratio:** Approximately **1:1**, as expected for AR. de Brouwer: 1 female / 5 males across 3 families; Shaheen: 1 female / 2 males; Darvish: 1 male / 1 female; Naseer: 2 males; Han: 2 siblings. Pooled counts are male-leaning but small-sample and not statistically meaningful — **do not assert a sex bias**.
- **Age distribution of reported patients:** **2–18 years**, per PMID:33100873 (*"nine patients ranged in age from 2 to 18 years old"*). **No adults have been reported** — the natural history beyond adolescence is completely unknown.

---

## 10. Diagnostics

### Clinical tests

**Laboratory tests**
| Test | LOINC *(verify)* | Purpose / finding |
|---|---|---|
| **Serum uric acid** | LOINC:3084-1 | **Hyperuricemia** (peaks 8.7, 6.5 mg/dL; ref 2.3–5.5). *Recommended in all patients* — treatable, and a mechanistic clue |
| Plasma glucose | LOINC:2345-7 | Hypoglycemia reported |
| Plasma amino acids / urine organic acids | — | **Normal** (rule out aminoacidopathy; note the *AASS* dual-diagnosis family had hyperlysinemia — an argument for keeping metabolic workup in the differential) |
| Lactate | LOINC:2524-7 | **Normal** — distinguishes from *PUS1*/MLASA1 |
| CBC | — | **Normal** (no cytopenia despite HSPC model data — human–model mismatch) |
| **tRNA Ψ13 quantification** (research only) | — | CMCT primer extension and HPLC nucleoside analysis on patient LCLs; the definitive functional assay |

**Biomarkers.** There is **no validated clinical biomarker.** The mechanistically specific candidate is **reduced tRNA Ψ13**, which Shaheen et al. propose for variant interpretation: *"this may also serve as a very helpful assay for the proper classification of variants of unknown significance."* Additional research-grade candidates: elevated global protein synthesis (SUnSET/puromycin incorporation), elevated MYC protein, reduced HPRT1 protein, depleted 5′TOG/mTOG tRFs. **None are FDA-listed or clinically available.** Hyperuricemia is the only routinely measurable abnormality and is neither sensitive nor specific.

**Imaging.** **Brain MRI** — recommended, but expect a **normal** study. *"Brain MRI showed normal brain architecture"*; *"both studies revealed normal brain architecture."* Rare findings: generalized atrophy with ventricular enlargement (1/6), brain atrophy (PMID:33100873), incidental craniocervical stenosis (managed conservatively). MRI's role is **exclusionary** (rule out malformation, migration defect, leukodystrophy), not confirmatory. Serial OFC plotting on growth charts is more diagnostically informative than imaging.

**Functional tests.** Not applicable (no pulmonary/cardiac involvement).

**Electrophysiology.**
- **Audiology / ABR / audiometry:** **Essential and under-recognized.** SNHL was initially misattributed to middle-ear effusion in one patient — *"Hearing loss was suspected due to chronic middle ear effusion but her poor response to ventilation tubes prompted re-evaluation and sensorineural hearing loss was confirmed."* Recommend baseline plus **serial** audiology given progression.
- **EEG:** **Normal** where performed (*"EEG recording was normal"*). Useful to document the absence of epilepsy.
- **ECG / EMG / NCS:** No indication established. (Given tibial-nerve PUS7 expression, NCS is an untested question rather than a recommendation.)

**Biopsy / histopathology.** **No role.** No characteristic histopathology exists; no biopsy findings published.

### Genetic testing

**Recommended approach:** *PUS7* is not clinically suspected on gestalt alone — the phenotype is *"common but non-specific"* — so diagnosis is **sequencing-first**.

| Modality | Utility for PUS7 |
|---|---|
| **Whole exome sequencing (WES)** | **First-line and highest-yield.** The discovery modality in nearly every published family. Muda et al.: *"We recommend looking for PUS7 pathological variants when performing whole exome sequencing in children with this constellation."* Coding SNVs/indels are well captured. |
| **Whole genome sequencing (WGS)** | Used by Darvish et al. (found p.Gly128Arg) and appropriate for deep-intronic/regulatory variants and for CNVs missed by WES. Detected the **penultimate exon 15 deletion** class of allele. |
| **ID/NDD gene panels** | *PUS7* is on modern ID/microcephaly/NDD panels and the **DDG2P/G2P DD panel** (G2P02633, Strong). Verify panel content — inclusion is recent (post-2018). |
| **Single-gene *PUS7* testing** | Appropriate only for **targeted familial testing** (carrier testing of relatives, prenatal/PGT once the familial variant is known), not for diagnosis. |
| **Chromosomal microarray (CMA)** | Detects the **multi-exon and whole-gene deletions** in ClinVar and larger 7q22 CNVs. A reasonable parallel first-tier test for unexplained ID/microcephaly, but will miss the majority (SNV/indel) of cases. |
| **Karyotype / FISH** | Low yield; relevant only for the rare **ring chromosome 7** and large 7q22 rearrangements. |
| **Mitochondrial DNA testing** | **Not indicated** — PUS7 does not modify mitochondrial tRNAs; no mitochondrial phenotype. |
| **Repeat expansion testing** | **Not applicable.** |
| **Homozygosity mapping / autozygome analysis** | Highly effective adjunct in consanguineous families (ROH >2 Mb; LOD 3.4 across two families). |
| **Functional confirmation (research)** | CMCT/HPLC tRNA Ψ13 assay on patient LCLs; yeast *pus7Δ trm8Δ* complementation for missense VUS — ACMG PS3-grade evidence. |

**GTR:** *PUS7* clinical testing is registered (NIH GTR gene page 54517). **ClinGen has published no variant-curation expert-panel specifications for *PUS7***, so ACMG/AMP interpretation is lab-specific.

### Omics-based diagnostics

- **RNA sequencing:** Useful for **splice-variant validation** — how the c.398+1G>T allele was characterized (*"41 bp or 55 bp deletions into the PUS7 mRNA"*, ~50% mRNA reduction). Recommend RNA-seq/RT-PCR for any candidate splice variant.
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** **No clinical diagnostic role.** No methylation episignature exists (a genuine, tractable diagnostic gap).

### Clinical criteria and differential diagnosis

**No formal diagnostic criteria** (no DSM/ICD/society guideline). Diagnosis = biallelic pathogenic *PUS7* variants + compatible phenotype. **No GeneReviews chapter exists.**

**Clinical suspicion gestalt (from PMID:42226002):** core features (moderate/severe ID + delayed/absent speech + very-early-onset aggression + progressive microcephaly + short stature + mild facial dysmorphism) **plus** one or more of the "peculiar" features (**sensorineural hearing loss, autistic traits, self-injurious behavior, motor stereotypies**).

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| **Lesch-Nyhan syndrome** (*HPRT1*, X-linked) | **The most important mimic.** Shares hyperuricemia + self-injurious behavior + ID. Distinguished by: X-linked (males), gout/nephrolithiasis, dystonia/choreoathetosis, markedly elevated urate, **absent HPRT enzyme activity**, and **pathogenic *HPRT1* variants**. PMID:35144859 documents PUS7 patients with *"features of Lesch-Nyhan syndrome, including hyperuricemia and self-injurious behavior, but without pathogenic variants in HPRT1"* — **PUS7 should be considered in HPRT1-negative LNS phenocopies.** |
| **Other PUS-gene disorders** | ***PUS1*** → MLASA1 (MIM 600462): myopathy, lactic acidosis, sideroblastic anemia — *absent* in PUS7. ***PUS3*** (MIM 616283) → ID + microcephaly, closest phenocopy; distinguished only by gene. ***PUS7L*** → severe GDD **with epilepsy**. |
| **Other tRNA-modification NDDs** | *ADAT3* (commonest single-gene ID cause in Arabia), *WDR4* (severe encephalopathy + microcephaly), *NSUN2*, *TRMT10A* (ID + microcephaly + short stature ± diabetes). Phenotypically near-indistinguishable → panel/WES resolves. |
| **Autosomal recessive primary microcephaly (MCPH)** | *ASPM*, *WDR62*, *MCPH1* etc.: microcephaly usually **congenital and more severe**, often with cortical malformation on MRI; **aggression is not a hallmark**. |
| **Cornelia de Lange / Rubinstein-Taybi / Coffin-Siris** | Growth failure + ID + dysmorphism, but each has a distinctive facial gestalt and limb/organ features absent in PUS7. |
| **Smith-Magenis syndrome** (*RAI1*/17p11.2del) | Strong overlap: **self-injury, sleep disturbance, aggression, stereotypies, ID, short stature**. Distinguished by inverted circadian melatonin rhythm and characteristic facies; CMA/*RAI1* testing. |
| **Angelman / Rett / MECP2-related** | Consider for stereotypies + absent speech; distinguished by ataxia/EEG (Angelman) or regression + hand stereotypies (Rett — **PUS7 has no regression**). |
| **Nonsyndromic ARID** | Sequencing-resolved. |
| **Hyperlysinemia type I / saccharopinuria** (*AASS*) | Must be considered in consanguineous pedigrees — co-occurred with *PUS7* in one family (PMID:33100873). |
| **Acquired causes** | Congenital infection, perinatal insult, lead/toxic exposure — excluded by history and normal MRI. |

### Screening

- **Newborn screening: not included, and not appropriate** — no biochemical marker, no presymptomatic treatment. No ACMG RUSP inclusion.
- **Carrier screening:** Not on any expanded carrier screening panel. Gene-level sequencing is required (private alleles). **Highest-value use: consanguineous couples with an affected relative.**
- **Cascade/family screening:** Indicated. Test at-risk siblings and offer carrier testing to relatives once the familial variant is known.
- **Prenatal / PGT:** Available once the familial variant is known — the principal current clinical benefit of diagnosis. Shaheen et al.: *"the benefit of discovering these disease-gene links… is currently limited to establishing an accurate molecular diagnosis and prevention through informed reproductive choices."*
- **Risk stratification:** Unexplained ID + progressive microcephaly + very-early aggression, especially with consanguinity or an HPRT1-negative LNS-like presentation → prioritize WES with *PUS7* in the analysis pipeline.

---

## 11. Outcome / Prognosis

> **Important caveat:** All prognostic statements below are **inferences from ~30 cross-sectional case reports of patients aged 2–18 years.** No natural-history study, registry, or survival analysis exists, and **no adult patient has been reported.** Curate prognosis with low confidence and an explicit `KNOWLEDGE_GAP`.

### Survival and mortality

- **Survival rate (5-/10-year/overall): not reported.** No deaths have been reported among published patients.
- **Life expectancy: not established.** No data. The absence of epilepsy, mitochondrial disease, progressive neurodegeneration, cardiac or respiratory involvement, and the observation of patients reaching 16–18 years in apparently stable general health (*"She has good general health otherwise and has no history of admissions"*) are consistent with **survival into adulthood**, but this is inference, not evidence.
- **Mortality rate / disease-specific mortality: not reported.**

### Morbidity and function

- **Morbidity is high and lifelong**, driven by cognitive, communication, and behavioral impairment rather than by organ failure.
- **Disability outcomes:** Lifelong dependency for most. Documented functional endpoints: special education placement (multiple patients), inability to read or write, expressive vocabulary limited to ~30 words at age 16, non-ambulation at age 9 in the most severe case, IQ 44–48 where measurable.
- **Quality of life measures:** **None applied.** No EQ-5D, SF-36, PROMIS, PedsQL, or disease-specific instrument has been used. This is a clear gap for a rare-disease natural-history study.

### Disease course and complications

| Complication | Notes |
|---|---|
| **Behavioral crisis / aggression and self-injury** | The dominant morbidity; physical injury risk; caregiver burden; drives pharmacotherapy |
| **Progressive sensorineural hearing loss** | Compounds communication deficit; requires amplification |
| **Hyperuricemia → urate nephropathy / nephrolithiasis / gout** | **Preventable** with allopurinol; requires monitoring |
| **Failure to thrive / low weight** | Nutritional support may be needed |
| **Dysphagia** | Aspiration risk in the severely affected |
| **Sleep disturbance** | Amplifies daytime behavioral dysregulation |
| **Dental complications** | Hypodontia, retained deciduous teeth, crowding, bruxism → dental care needs |
| **Not observed** | Epilepsy, neurodegeneration/regression, cardiac, respiratory, hepatic failure, hematologic disease, malignancy |
| **Recovery potential** | **None** for the neurodevelopmental core — the deficits are developmental and irreversible. Functional gains come from habilitation. Hearing loss is remediable (amplification). Hyperuricemia is fully treatable. |

### Prediction

- **Prognostic factors:** None validated. Candidate (weak, contested) factor: **variant class** — Darvish et al. suggest missense/hypomorphic alleles spare microcephaly and short stature, but Shaheen's p.Asp503Tyr missense patients had severe microcephaly and complete LoF in yeast, so the correlation does not hold. Bergès et al. (PMID:42249560) explicitly aim to improve genotype–phenotype correlation with 13 new patients and 15 new variants — **this paper is the priority follow-up read** for prognostic factors.
- **Prognostic biomarkers:** **None.** (Note: PUS7-related prognostic biomarkers *do* exist in oncology — high PUS7 predicts worse survival in glioblastoma, and mTOG dysregulation *"is clinically associated with leukaemic transformation and reduced patient survival"* in MDS. These are **entirely separate disease contexts** and must not be curated as prognostic markers for IDDABS.)

---

## 12. Treatment

> **There is no disease-modifying or curative therapy.** Management is entirely **symptomatic, supportive, and multidisciplinary.** Shaheen et al. state the position plainly: *"the benefit of discovering these disease-gene links… is currently limited to establishing an accurate molecular diagnosis and prevention through informed reproductive choices, it is likely that these revelations will inform the development of therapeutics in the future."*

### Pharmacotherapy

| Treatment | Agent | Evidence | Suggested annotation *(verify all terms)* |
|---|---|---|---|
| **Antipsychotic for aggression** | **Risperidone** | **Directly documented:** *"We re-evaluated him at age 16 yrs, he presented with aggressive behavior and Risperidone treatment was introduced."* (PMID:30778726). Outcome not reported. | `treatment_term: NCIT:C15986 Pharmacotherapy`; `therapeutic_agent: CHEBI:8871 risperidone`; `therapeutic_modality: SMALL_MOLECULE`; target: aggressive behavior (HP:0000718) |
| **Xanthine oxidase inhibitor for hyperuricemia** | **Allopurinol** | **Directly documented:** *"Uric acid levels peaked at 8.7 mg/dL and 6.5 mg/dL (normal: 2.3–5.5), requiring allopurinol intervention."* (PMID:35144859) | `NCIT:C15986`; `therapeutic_agent: CHEBI:40279 allopurinol`; `SMALL_MOLECULE`; targets hyperuricemia (HP:0002149) |
| ADHD/hyperactivity pharmacotherapy | stimulants / alpha-2 agonists | **Not documented in PUS7 literature** — extrapolated standard of care. Curate only with a general-practice citation, or omit. | — |
| Melatonin for sleep disturbance | melatonin (CHEBI:16796) | **Not documented in PUS7 literature** — extrapolated. Do not assert. | — |
| **Pharmacogenomics** | — | **No PUS7 pharmacogenomic data.** No PharmGKB/CPIC entry; no FDA PGx biomarker. Standard CYP2D6 guidance applies to risperidone generally, not PUS7-specifically. | — |

### Advanced therapeutics

- **Gene therapy / gene editing:** **None.** No preclinical program. Conceptually challenging: the critical developmental window is prenatal, and correction would require broad CNS delivery.
- **Cell therapy:** **None.**
- **RNA-based therapies:** **None for this disorder.** *But note a mechanistically striking opportunity*: **programmable/site-directed pseudouridylation** (dCas13b-guided Ψ deposition was demonstrated for 7SK, PMID:41168165; reviewed in PMID:40394244, which covers *"therapeutic applications including programmable pseudouridylation"*). Substrate-specific Ψ restoration is a *conceptual* future direction, not a therapy. Similarly, PMID:42532042 shows *"Perturbing structure through mutations or antisense oligos modulates pseudouridine levels"* — an ASO-based lever on Ψ levels. Curate these as `mechanistic_hypotheses` / research directions, **not** as treatments.
- **Targeted therapies:** **None.** Critically, the existing PUS7-directed small molecules (**C4, C17/NSC107512**, IC50 92.15 nM in PBT003 GSCs) are **PUS7 INHIBITORS developed for glioblastoma** — they would be expected to *worsen* PUS7 deficiency and are **contraindicated in concept**. This is an important curation guardrail: do not import cancer PUS7 pharmacology as therapy for IDDABS.
- **Immunotherapies:** Not applicable.

### Surgical and interventional

- No disease-specific surgery. Reported procedures were incidental: ventilation tubes for middle-ear effusion (ineffective — the loss was sensorineural); craniocervical stenosis *"Neurosurgical consultation suggested that conservative management is sufficient."*
- **Hearing aids** — documented: *"he developed severe sensorineural hearing loss and hearing aid was used."* (`therapeutic_modality: DEVICE`)
- Dental/orthodontic intervention for hypodontia, crowding, retained deciduous teeth.

### Supportive and rehabilitative (the mainstay)

| Intervention | NCIT *(verify)* | Modality | Evidence |
|---|---|---|---|
| **Special education** | NCIT:C15302 / NCIT:C181743 | BEHAVIORAL | Documented in ≥3 patients |
| **Speech and language therapy** | NCIT:C159273 | BEHAVIORAL | Standard of care for universal speech delay |
| **Physical therapy** | NCIT:C15302 | BEHAVIORAL | For motor delay, hypotonia |
| **Occupational therapy** | NCIT:C121351 | BEHAVIORAL | ADLs, sensory/stereotypy management |
| **Behavioral intervention / ABA-style behavior management** | NCIT:C181743 | BEHAVIORAL | For aggression, self-injury, stereotypies |
| **Audiological management + serial audiometry** | NCIT:C15747 | DEVICE / SUPPORTIVE | Progressive SNHL |
| **Nutritional support** | NCIT:C15433 | (agent-dependent) | Low weight, dysphagia |
| **Genetic counseling** | NCIT:C15240 | BEHAVIORAL | Recurrence risk 25%; prenatal/PGT options |
| **Supportive/multidisciplinary care** | NCIT:C15747 | SUPPORTIVE | Umbrella node |

### Experimental treatments and trials

**ClinicalTrials.gov query for "PUS7" returns zero studies** (API v2, 2026-08-01). No EU-CTR or WHO ICTRP entries identified. **There are no clinical trials in this disorder.**

### Treatment outcomes, algorithms, strategy

- **Response rates:** **Not reported for any intervention.** Risperidone and allopurinol outcomes were not quantified in the source reports.
- **Adverse events:** No PUS7-specific safety data. Standard risperidone (weight gain, metabolic syndrome, EPS, hyperprolactinemia) and allopurinol (rash, rare SJS/TEN — note **HLA-B\*58:01** risk, relevant to the dismech `drug_hypersensitivity_scar` and `Allopurinol_Induced_SJS_TEN` entries) risks apply.
- **Treatment algorithm:** No published algorithm or guideline. Practical framework: (1) confirm molecular diagnosis; (2) baseline serum uric acid, glucose, audiology, OFC plotting, MRI (exclusionary); (3) early habilitation (speech/PT/OT/special ed); (4) structured behavioral management, escalating to antipsychotic for refractory aggression/self-injury; (5) allopurinol if hyperuricemic; (6) serial audiology and growth monitoring; (7) genetic counseling and cascade testing.
- **Combination therapy / personalized medicine:** No genotype-guided treatment exists.

---

## 13. Prevention

### Prevention levels

- **Primary prevention (preventing disease occurrence):** The only effective lever is **reproductive**, not exposure-based, because the etiology is purely genetic.
  - **Genetic counseling** for consanguineous couples and for families with an affected child (25% recurrence risk per pregnancy).
  - **Prenatal diagnosis** (CVS/amniocentesis with targeted variant testing) and **preimplantation genetic testing (PGT-M)** once the familial variant is known.
  - **Community-level consanguinity counseling / premarital genetic counseling programs**, which are established public-health interventions in several of the high-ascertainment populations. This is the highest-impact population measure.
  - Shaheen et al. name this explicitly as the current benefit of diagnosis: *"prevention through informed reproductive choices."*
- **Secondary prevention (early detection):**
  - **Early WES in unexplained ID + microcephaly** — Muda et al.'s explicit recommendation. Shortens the diagnostic odyssey and enables the interventions below.
  - **Cascade carrier testing** in extended families.
  - **No population newborn or presymptomatic screening** is appropriate (no biochemical marker, no presymptomatic therapy).
- **Tertiary prevention (preventing complications in affected individuals)** — the most actionable domain:
  - **Serum uric acid monitoring → allopurinol** to prevent urate nephropathy, nephrolithiasis, and gout.
  - **Serial audiology** to detect progressive SNHL early and fit amplification — prevents avoidable additional communication loss. *Also prevents misdiagnosis as conductive/effusion-related loss.*
  - **Structured behavioral management** to reduce self-injury-related physical harm.
  - **Nutritional and swallowing assessment** to prevent aspiration and worsening failure to thrive.
  - **Serial OFC and growth plotting** to document progression and trigger review.
  - **Sleep hygiene management** to reduce behavioral escalation.
  - **Dental surveillance.**

### Other prevention modalities

- **Immunization:** No disease-specific vaccine strategy. Routine childhood immunization per schedule; no contraindication.
- **Behavioral interventions to reduce risk:** Not applicable to disease occurrence (genetic etiology). Behavioral intervention is *therapeutic*, not preventive of the disorder.
- **Public health interventions:** Premarital/preconception genetic counseling and consanguinity-awareness programs in high-consanguinity populations; expansion of WES access in low-resource settings where much of the reported patient population resides.
- **Environmental interventions:** **Not applicable** — no environmental contribution.
- **Prophylaxis:** Allopurinol functions as prophylaxis against urate complications in hyperuricemic patients. No other prophylactic medication or procedure.
- **Risk stratification for targeted prevention:** consanguineous families with an affected proband; families with an unexplained ID + progressive microcephaly + early aggression phenotype.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthology (Alliance of Genome Resources, all "high" confidence, best-score across methods)

| Species | NCBI Taxon | Gene ID | Symbol |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | `hgnc:26033` | **PUS7** |
| *Mus musculus* | NCBITaxon:10090 | **MGI:1925947** | **Pus7** (syn. C330017I15Rik), **Chr 5: 23,945,646–23,988,709 (−), GRCm39; 10.42 cM** |
| *Rattus norvegicus* | NCBITaxon:10116 | RGD:1307054 | Pus7 |
| *Danio rerio* | NCBITaxon:7955 | ZFIN:ZDB-GENE-060620-1 | pus7 (Chr 25) |
| *Drosophila melanogaster* | NCBITaxon:7227 | **FBgn0035901** (CG6745) | **Pus7**, Chr 3L |
| *Caenorhabditis elegans* | NCBITaxon:6239 | WBGene00007101 | B0024.11 |
| *Saccharomyces cerevisiae* S288C | NCBITaxon:559292 | SGD:S000005769 | **PUS7** |
| *Xenopus tropicalis* / *X. laevis* | NCBITaxon:8364 / 8355 | XB-GENE-5812368 / XB-GENE-5812471 | pus7 / pus7.L |

*PUS7* is **broadly conserved from yeast to human**, which is central to the disease evidence base.

### Naturally occurring disease in other species

- **None.** No naturally occurring PUS7-related disorder is recorded in **OMIA** for dogs, cats, cattle, horses, or any other species. No wildlife or companion-animal disease.
- **Veterinary relevance: none.** All animal data are experimentally induced.
- One tangential agricultural genomics hit: *PUS7* appeared in a GWAS for body weight in Chinese native ducks (PMID:38909509) — a statistical association in a production trait, **not** a natural disease model, and should not be curated as such.

### Comparative biology

- **Evolutionary conservation of mechanism is strong and load-bearing for the disease argument:**
  - Yeast Pus7 catalyzes Ψ13 in cytoplasmic tRNAs and Ψ35 in pre-tRNA-Tyr(GUA) — the *same* positions as human PUS7.
  - Yeast complementation established human residue Asp503 as functionally essential: *"This result indicates that the yeast Pus7-D478Y variant is a complete loss of function mutation, and thus that the importance of the human Thr503 residue is conserved among eukaryotes."* (PMID:30778726) *(Note the paper's internal typo — "Thr503" for Asp503.)*
  - p.Gly128 is *"an evolutionarily conserved glycine down to yeast."*
  - Substrate motif conserved: *"in yeast and human PUS7 identify a core motif UGΨAG."*
- **Comparative pathology / species differences:**
  - **Human PUS7 has two additional subdomains** absent from the bacterial homolog, which *"contribute to tRNA recognition through increased interactions along the tRNA substrate"* (PMID:34718722) — recognition mechanism, and therefore substrate breadth, is **not** fully conserved; caution when extrapolating from prokaryotic/yeast structural work.
  - Yeast/*T. thermophilus* TruD modifies U13 and U35 (PMID:40138658); the U50 activity was described in human GSCs (PMID:35121864).
  - The *behavioral* phenotype (hyperactivity, disorientation, aggression) is recapitulated in *Drosophila*, but the *growth/microcephaly* phenotype has **no** described animal counterpart — a genuine cross-species gap.
- **Transmission / zoonosis / cross-species susceptibility:** **Not applicable** — non-infectious genetic disorder.

---

## 15. Model Organisms

### 15a. *Drosophila melanogaster* — the flagship behavioral model

**Gene:** *Pus7* / **FBgn0035901** (CG6745), Chr 3L. **Alleles:** *Pus7^fs* (frameshift) and *Pus7^UAS.cBa*; FlyBase annotates these as models of IDDABS.

**Type:** Whole-animal knockout + tissue-specific (neuronal) UAS/GAL4 rescue — the only *in vivo* model demonstrating a **causal, cell-autonomous, neuronal** basis for the behavioral phenotype.

**Phenotype recapitulation (PMID:30526862):**

| Assay | Result | Human counterpart |
|---|---|---|
| Locomotor activity | *"Overall activity of pus7 mutant flies was significantly increased"* | Hyperactivity (HP:0000752), ADHD (HP:0007018) |
| Orientation | *"severe orientation defects were observed"*; *"significantly larger angular deviation"* | Cognitive/motor dysfunction |
| Aggression (dyadic fighting) | *"pus7 flies spent significantly more time fighting"* and *"were most often the winner of the fight"* | **Aggressive behavior (HP:0000718) — the disorder's most discriminating feature** |
| Neuron-restricted rescue | *"expression of pus7 only in neurons by using the elav-Gal4 driver was sufficient to alter fly behavior, suggesting that Pus7 exerts its activity through a neuronal function"* | Establishes neuron-intrinsic mechanism |

**Summary claim:** *"pus7 knockout in Drosophila melanogaster results in a number of behavioral defects, including increased activity, disorientation, and aggressiveness supporting that neurological defects are caused by PUS7 variants."*

**Limitations:** No microcephaly/brain-size, growth, hearing, or speech correlate. Flies cannot model ID, language, or self-injury. Invertebrate translational machinery and tRNA repertoire differ. `evidence_source: MODEL_ORGANISM`.

### 15b. *Saccharomyces cerevisiae* — variant-interpretation model

**Gene:** PUS7 / SGD:S000005769. **Design:** *pus7Δ* in a *trm8Δ* background, which *"grows very poorly at 33°C and higher temperatures, due to rapid tRNA decay of tRNAVal(AAC)"* — a temperature-sensitive growth readout for Pus7 function. Humanized-residue allele *pus7-D478Y* (≡ human D503Y) expressed from a CEN/URA3 plasmid under the native promoter.

**Result:** *"expression of the yeast pus7-D478Y variant failed to detectably rescue the growth defect of the pus7Δ trm8Δ strain."* (PMID:30778726)

**Application:** The **most directly clinically useful model** — a scalable functional assay for classifying *PUS7* missense VUS (ACMG PS3). **Limitations:** cannot model any organismal phenotype; humanized residues only; human PUS7 has eukaryote-specific subdomains yeast Pus7 lacks.

### 15c. *Mus musculus* — available but essentially uncharacterized for this disorder

**Gene:** *Pus7* / **MGI:1925947**, Chr 5.

**Allele resources (MGI, 24 total mutations/alleles):** 9 gene-trapped, 9 endonuclease-mediated (CRISPR), 2 targeted, 2 chemically induced, 1 radiation-induced, 1 spontaneous. **Available from IMPC/KOMP repositories.**

**Phenotype data:** MGI records **3 phenotypes from 1 allele in a single genetic background**. **IMPC (MGI:1925947): 3 significant phenotypes; 18/24 physiological systems tested; significantly impacted systems: Mortality/aging, Homeostasis/metabolism, Embryo.** (Specific MP terms and the viability call did not render in the fetched page — **retrieve these directly from mousephenotype.org before curating any MP term.**)

**Critical assessment:** **No published mouse model of PUS7-related neurodevelopmental disorder exists.** There is no report of a *Pus7*-null mouse with microcephaly, growth retardation, aggression, or cognitive impairment. This is the single largest gap in the field — a `KNOWLEDGE_GAP` and arguably a `HUMAN_MODEL_MISMATCH` candidate (IMPC's "Mortality/aging, Homeostasis/metabolism, Embryo" hits do not obviously map onto the human neurobehavioral phenotype, and the human-relevant systems may be untested or under-powered in the IMPC pipeline).

**The closest mammalian *in vivo* neural evidence is a knockdown, not a germline model:** *"PUS7 knockdown in the ILPFC selectively impaired fear extinction memory formation without altering baseline fear expression"* (PMID:41094471) — region-specific, adult-onset, AAV/shRNA-based. This demonstrates a mammalian PUS7 requirement for activity-dependent synaptic remodeling and learning, but does not model the developmental disorder.

### 15d. Cellular and *in vitro* models

| Model | Findings | PMID |
|---|---|---|
| **Patient-derived EBV-LCLs** | Loss of Ψ13 in tRNA-His(GTG), tRNA-Glu(CTC); tRNA-Val(AAC) Ψ reduced by 0.88 mol/mol (1.75 vs 2.63); m5C and m2G unchanged; reduced Ψ at 9 PUS7 mRNA targets with **no change in TRUB1 targets** (specificity control) | 30526862, 30778726 |
| **Patient-derived fibroblasts** | ↑global protein synthesis (SUnSET, p=2.1e-3); ↑MYC protein with normal mRNA (p=4.9e-4); ↓HPRT1 protein with normal mRNA (p=3.5e-3); **no change in proliferation rate** | 35144859 |
| **PUS7-KO human embryonic stem cells** | *"impairs tRF-mediated translation regulation, leading to increased protein biosynthesis and defective germ layer specification"* | 29628141 |
| **Primary human HSPCs (PUS7-depleted) + xenotransplant** | Multilineage engraftment *"dramatically impaired"*, with loss evident by 4 weeks post-transplant | 29628141 |
| **MDS patient HSPCs** | mTOG-Ψ dysregulation → aberrantly increased 5′PES mRNA translation; associated with leukemic transformation | 35292784 |
| **Glioblastoma stem cells (PUS7 KO)** | 13 PUS7-dependent Ψ sites in 8 tRNA types; loss of Ψ50 in tRNA-Arg-CCG-2-1; ↑translation efficiency; ↑TYK2 protein (not mRNA); C4/C17 inhibitors (C17 IC50 92.15 nM) suppress tumorigenesis and prolong murine survival | 35121864 |
| **HCT116 PUS7 KO/KD (9 stand-alone PUS enzymes)** | Comprehensive human tRNA Ψ map by BACS; PUS enzymes act at distinct pre-tRNA processing stages | 41136621 |
| **PUS7-KO HeLa** | Commercially available (Abcam ab265407) — a ready reagent for functional assays | — |
| **iPSC-derived neural models / brain organoids** | **DO NOT EXIST.** No iPSC neuronal or organoid model of PUS7 deficiency has been reported. Given that the phenotype is CNS-restricted and the mechanism is a translational-control defect in neural progenitors, this is the **highest-priority missing model.** MorPhiC-style null-allele phenotyping in iPSC-derived neural lineages would be directly informative. | — |

### 15e. Model resources

MGI (informatics.jax.org, MGI:1925947) · IMPC (mousephenotype.org/data/genes/MGI:1925947) · IMSR / KOMP / EuMMCR for *Pus7* alleles · FlyBase (FBgn0035901) · SGD (S000005769) · RGD (1307054) · ZFIN (ZDB-GENE-060620-1) · WormBase (WBGene00007101) · Xenbase · Alliance of Genome Resources (HGNC:26033) · Cellosaurus/ATCC for PUS7-KO HeLa · PRIDE PXD008676.

---

## Appendix A — Verified abstract quotes for evidence items

These are exact quotes from fetched abstracts/full text, suitable for `snippet:` fields after `just fetch-reference` and `just validate-references`. **Reference cache files already exist** for PMIDs 29628141, 30526862, 30778726, 31583274, 33100873, 35144859, 37067188, 41094471, 41136621, 42226002, 42249560.

| PMID | Quote | Supports |
|---|---|---|
| 30526862 | "All these individuals have intellectual disability with speech delay, short stature, microcephaly, and aggressive behavior." | Core phenotype |
| 30526862 | "We show that the disease-related variants lead to abolishment of PUS7 activity on both tRNA and mRNA substrates." | Molecular mechanism (LoF) |
| 30526862 | "pus7 knockout in Drosophila melanogaster results in a number of behavioral defects, including increased activity, disorientation, and aggressiveness supporting that neurological defects are caused by PUS7 variants." | MODEL_ORGANISM behavioral recapitulation |
| 30526862 | "Our findings demonstrate that RNA pseudouridylation by PUS7 is essential for proper neuronal development and function." | Neurodevelopmental requirement |
| 30778726 | "We describe two families in which two different homozygous PUS7 mutations (missense and frameshift deletion) segregate with a phenotype comprising intellectual disability and progressive microcephaly." | Progressive microcephaly; AR |
| 30778726 | "Short stature and hearing loss were variable in these patients." | Variable expressivity; SNHL |
| 30778726 | "Functional characterization of the two mutations confirmed that both result in decreased levels of Ψ13 in tRNAs." | tRNA Ψ13 defect |
| 30778726 | "the missense variant of the S. cerevisiae ortholog failed to complement the growth defect of S. cerevisiae pus7Δ trm8Δ mutants" | Yeast model; missense = LoF |
| 31583274 | "We report a novel PUS7 homozygous mutation resulting in p.Gly128Arg amino-acid translation in a consanguineous Afghani family presenting with similar but milder clinical features without microcephaly and short stature" | Milder/hypomorphic phenotype |
| 31583274 | "All identified PUS7 variants resulted in aberrant pseudouridylation of at least 10 cytosolic tRNAs at position 13." | ≥10 tRNA Ψ13 targets |
| 33100873 | "Intellectual developmental disorder with abnormal behavior, microcephaly and short stature (IDDABS), (OMIM# 618342) is an autosomal recessive condition" | Disease identity/inheritance |
| 33100873 | "nine patients ranged in age from 2 to 18 years old" | Age distribution |
| 35144859 | "These patients exhibited a neurodevelopmental phenotype including autism spectrum disorder in the proband." | ASD |
| 35144859 | "Both patients also had features of Lesch-Nyhan syndrome, including hyperuricemia and self-injurious behavior, but without pathogenic variants in HPRT1." | LNS phenocopy; hyperuricemia |
| 35144859 | "Patient fibroblasts demonstrated upregulation of protein synthesis, including elevated MYC protein, but did not exhibit increased rates of cell proliferation." | Translational dysregulation |
| 35144859 | "the dysregulation of protein translation also resulted in mildly decreased levels of HPRT1 protein suggesting an association between dysregulated protein translation and the LNS-like phenotypic findings" | HPRT1 secondary mechanism |
| 37067188 | "results in a neurodevelopmental phenotype characterized by various degrees of psychomotor delay, acquired microcephaly, aggressive behavior, and intellectual disability" | **Acquired** microcephaly |
| 37067188 | "who, in addition to the previously mentioned features, displays self-injurious behavior, sleep disturbances and motor stereotypies" | Self-injury, sleep, stereotypies |
| 42226002 | "Across 17 cases, the most frequent features were moderate/severe intellectual disability, delayed/absent speech, aggressive behavior, microcephaly, mild facial dysmorphisms, motor delay, and short stature." | Frequency ranking |
| 42226002 | "These features are common but non-specific, with the exception of aggressiveness that manifests at a very early age." | Discriminating feature |
| 42226002 | "Less common but more peculiar findings included sensorineural hearing loss, autistic traits, self-injurious behavior, and motor stereotypies." | Expanded phenotype |
| 42249560 | "In total, we report 13 new cases carrying 15 new variants." | Cohort expansion |
| 29628141 | "PUS7 inactivation in embryonic stem cells impairs tRF-mediated translation regulation, leading to increased protein biosynthesis and defective germ layer specification." | IN_VITRO; core mechanism |
| 29628141 | "the Ψ 'writer' PUS7 modifies and activates a novel network of tRNA-derived small fragments (tRFs) targeting the translation initiation complex" | tRF mechanism |
| 35292784 | "pseudouridylation (Ψ) of a stem cell-enriched tRF subtype, mini tRFs containing a 5' terminal oligoguanine (mTOG), selectively inhibits aberrant protein synthesis programmes" | mTOG–PABPC1 axis |
| 35121864 | "pseudouridylation of PUS7-regulated transfer RNA is critical for codon-specific translational control" | Codon-biased translation |
| 34718722 | "The human pseudouridine synthase PUS7 is a versatile RNA modification enzyme targeting many RNAs thereby playing a critical role in development and brain function." | Brain function; substrate breadth |
| 41094471 | "PUS7 knockdown in the ILPFC selectively impaired fear extinction memory formation without altering baseline fear expression, establishing a causal link between Ψ-dependent RNA processing and activity-dependent synaptic structural remodeling in this microcircuit." | MODEL_ORGANISM synaptic/learning mechanism |
| 41997936 | "engineered PUS7 cytoplasmic localization increases cellular fitness under reactive oxygen species (ROS) and divalent metal ion stress" | Stress-responsive localization |

---

## Appendix B — Ontology term suggestions summary

**All IDs below require verification with `just validate-terms` / OAK before use.** Only the GO terms in the "verified" column were confirmed against a UniProt annotation set in this session.

- **MONDO:** `MONDO:0032687` ✅ (verified via OLS, with OMIM/GARD/MedGen/UMLS/DOID xrefs)
- **HGNC:** `hgnc:26033` ✅ (verified via rest.genenames.org)
- **GO (verified via UniProt Q96PZ0):** GO:0009982, GO:0160150, GO:0003723, GO:0019899 (MF); GO:0001522, GO:0031119, GO:1990481, GO:0006397, GO:0008380, GO:0017148, GO:1902036, GO:2000380 (BP); GO:0005634 (CC)
- **GO (additional, unverified suggestions):** GO:0006412, GO:0045727, GO:0022008, GO:0021895, GO:0050803, GO:0007612, GO:0005829, GO:0005737, GO:0005654
- **HPO:** 50 terms enumerated in §3a (all sourced from ontology.jax.org for OMIM:618342) + 9 literature-expansion terms in §3b
- **CL (unverified):** CL:0000540, CL:0000047, CL:0000031, CL:0000121, CL:0000037, CL:0002322, CL:0000057, CL:0000542
- **UBERON (unverified):** UBERON:0000955, UBERON:0000956, UBERON:0002037, UBERON:0002743, UBERON:0001846, UBERON:0001844, UBERON:0001474, UBERON:0001684, UBERON:0001091, UBERON:0001134, UBERON:0002113, UBERON:0002107
- **CHEBI (unverified):** CHEBI:17802 (pseudouridine), CHEBI:8871 (risperidone), CHEBI:40279 (allopurinol), CHEBI:16704 (uric acid — verify)
- **NCIT (unverified):** NCIT:C15986, NCIT:C15302, NCIT:C159273, NCIT:C121351, NCIT:C181743, NCIT:C15240, NCIT:C15747, NCIT:C15433
- **NCBITaxon:** 9606, 10090, 10116, 7955, 7227, 6239, 559292, 8364

---

## Appendix C — Explicit knowledge gaps (candidate `discussions` entries)

| Gap | Kind | Rationale |
|---|---|---|
| No mouse model of the neurodevelopmental phenotype; IMPC hits (mortality/aging, homeostasis/metabolism, embryo) do not map onto human ID/microcephaly/aggression | `HUMAN_MODEL_MISMATCH` | Alleles exist (24 in MGI) but no published *Pus7*-null mouse with brain-size, growth, or behavioral characterization. IMPC's significant systems are discordant with the human phenotype. |
| PUS7-depleted HSPCs show dramatically impaired engraftment and MDS-associated dysregulation, yet **no human patient has a hematologic phenotype** | `HUMAN_MODEL_MISMATCH` | Robust *in vitro*/xenograft hematopoietic requirement vs. normal CBCs in patients — a genuine translational discrepancy needing explanation (redundancy? dosage? cell-autonomy?). |
| Mechanism of microcephaly is inferred, not demonstrated — no evidence for neural progenitor pool depletion, altered cell-cycle exit, or apoptosis in human neural tissue | `KNOWLEDGE_GAP` | The molecular defect (tRNA/tRF/mRNA Ψ loss → ↑translation) and the phenotype (reduced brain growth) are separated by an unbridged causal gap. iPSC-derived neural progenitors / brain organoids would test it directly. |
| Cerebellar expression is 3–5× cortical (GTEx) and cited as supporting neurodevelopmental specificity, but no cerebellar phenotype (ataxia, cerebellar hypoplasia) is reported | `KNOWLEDGE_GAP` | Expression–phenotype mismatch; systematic cerebellar imaging/exam has not been reported. |
| Splicing (U2 snRNA Ψ35) and transcription-elongation (7SK Ψ) arms of PUS7 function have no established role in the human disorder | `KNOWLEDGE_GAP` | Mechanistically established in cell models; disease-relevance untested. Curate as `mechanistic_hypotheses` with `status: EMERGING`. |
| No natural history study; no adult patient reported; life expectancy unknown | `KNOWLEDGE_GAP` | Oldest reported patients are 16–18 years. Prognostic and management guidance for adulthood is absent. |
| No genotype–phenotype correlation established; the missense=milder hypothesis (Darvish) is contradicted by Shaheen | `KNOWLEDGE_GAP` | Bergès et al. (PMID:42249560, 13 patients / 15 variants) is the priority follow-up read; obtain full text when available. |
| No DNA methylation episignature developed | `KNOWLEDGE_GAP` | Tractable diagnostic opportunity; would aid VUS resolution alongside the tRNA Ψ13 assay. |
| Peripheral nerve is among the higher-PUS7-expressing tissues; peripheral neuropathy has never been assessed | `KNOWLEDGE_GAP` | No NCS/EMG data in any patient. |
| Whether cellular stress (ROS, metal ions, heat) modulates phenotypic severity in PUS7-deficient patients | `KNOWLEDGE_GAP` | PUS7 relocalizes to cytoplasm under stress and remodels the proteome (PMID:41997936); GxE relevance untested in patients. |
| No Orphanet code exists for this disorder | Curation/data gap | Consider submitting to Orphanet; note absence in the entry's mappings. |

---

## Appendix D — Curation guardrails (read before building the KB entry)

1. **PUS7 cancer literature is a large trap.** ~40 of ~86 PUS7 PubMed records concern oncology (glioblastoma, colorectal, gastric, pancreatic, HCC, ovarian, bladder, thyroid, osteosarcoma, TNBC, NSCLC, RCC). These describe **PUS7 overexpression** and its **inhibition as therapy** — the mechanistic *opposite* of this recessive LoF disorder. Do not import PUS7 inhibitors (C4, C17/NSC107512) as treatments; do not import PUS7-high prognostic biomarkers. If a `viral_oncogenesis`/hallmark module link is tempting, it belongs on a cancer entry, not here.
2. **The Naseer 2020 family (PMID:33100873) is a dual diagnosis** (*PUS7* + *AASS* splice variant). The seizures, hypotonia, and possibly the brain atrophy in those patients may derive from hyperlysinemia type I, not PUS7. Curate any phenotype from this paper with an explicit caveat, and **do not** let it override the strong "epilepsy absent" signal from every other cohort.
3. **The "PUS7 modifies Ψ50 in mitochondrial tRNA-Met" claim** appearing in a 2025 secondary review conflicts with de Brouwer et al.'s primary statement that *"PUS7… does not modify mitochondrial tRNAs"* and with Cui et al.'s Ψ50 finding in *cytosolic* tRNA-Arg-CCG. **Do not curate a mitochondrial tRNA target** without primary-source verification.
4. **Do not fabricate gnomAD constraint values.** pLI/LOEUF/o-e could not be retrieved in this session (JS-rendered browser; GeneCards 403). Fetch directly before citing.
5. **The Han 2022 (PMID:35144859) growth numbers extracted as "heights of 47.8 cm and 48 cm at ages 9–10"** are almost certainly **occipitofrontal circumference**, not height. Re-read the primary table before curating any numeric growth value from that paper.
6. **Bergès 2026 (PMID:42249560) and Muda 2026 (PMID:42226002) are paywalled, ahead-of-print, and not in EuropePMC/PMC** (`isOpenAccess: N`, `inEPMC: N`). Only their abstracts are quotable today. The 15 new variants and the 17-case frequency table are **not** currently extractable — flag for a follow-up curation pass once full text is accessible.
7. **`evidence_source` assignments:** de Brouwer/Shaheen/Darvish/Naseer/Muda/Bergès clinical descriptions → `HUMAN_CLINICAL`. Patient LCL/fibroblast assays, ESC/GSC/HCT116 experiments, PUS7 crystal structures → `IN_VITRO`. Drosophila and mouse ILPFC knockdown → `MODEL_ORGANISM`. Yeast complementation → `IN_VITRO` (or `MODEL_ORGANISM` if treated as an organismal growth assay — pick one and be consistent). In silico pathogenicity predictions (SIFT/PolyPhen/CADD/MutationTaster) → `COMPUTATIONAL`; split these into separate evidence items from the clinical claims.
8. **Frequency qualifiers:** the HPO n/N values in §3a are legitimate derived-count evidence for `frequency:` bands, but they derive from **n≤9 patients**. Prefer citing the count explicitly in the evidence `explanation` over asserting a confident FrequencyEnum band, and follow `docs/frequency-evidence-guidelines.md`. Where a count is 1/3 or 1/6, consider omitting `frequency:` entirely.
9. **NEC preflight passed.** MONDO:0032687's identity anchors (OMIM:618342, causal gene *PUS7*, synonym IDDABS) are consistent across OMIM, UniProt, HGNC, G2P, ClinVar, and every primary paper. The gene named most frequently in the literature *is* the canonical gene. No named-entity confusion detected. Watch only for *PUS7* vs ***PUS7L*** (a distinct paralog with a distinct, epilepsy-featuring phenotype) and *PUS7* vs *PUS1*/*PUS3*.
10. **Module conformance candidates** (evaluate, don't assume): this disorder does **not** fit `metabolic_intoxication_decompensation` (no decompensation), `lysosomal_substrate_accumulation`, or any mitochondrial pattern. `sensorineural_hair_cell_loss` is a plausible partial conformer for the progressive SNHL node, and `epilepsy_excitation_inhibition_imbalance` should be **explicitly not** applied (epilepsy is characteristically absent). There is no existing dismech module for "translational-control / RNA-modification neurodevelopmental disorder" — the *PUS1/PUS3/PUS7/ADAT3/WDR4/NSUN2/TRMT10A* family would make a coherent new mechanism module and/or a `Grouping` (basis: `SHARED_MECHANISM` + `SHARED_GENE_FAMILY`), which is worth proposing.

---

## Sources

**Primary literature (PubMed/PMC):**
- [de Brouwer et al. 2018, Am J Hum Genet — PMID:30526862](https://pubmed.ncbi.nlm.nih.gov/30526862/) · [full text PMC6288278](https://pmc.ncbi.nlm.nih.gov/articles/PMC6288278/)
- [Shaheen et al. 2019, Hum Genet — PMID:30778726](https://pubmed.ncbi.nlm.nih.gov/30778726/)
- [Darvish et al. 2019, Neurol Genet — PMID:31583274](https://pmc.ncbi.nlm.nih.gov/articles/PMC6745718/)
- [Naseer et al. 2020, Saudi J Biol Sci — PMID:33100873](https://pubmed.ncbi.nlm.nih.gov/33100873/)
- [Han et al. 2022, Mol Genet Metab — PMID:35144859](https://pmc.ncbi.nlm.nih.gov/articles/PMC8958514/)
- [Muda et al. 2023, Am J Med Genet A — PMID:37067188](https://pubmed.ncbi.nlm.nih.gov/37067188/)
- [Muda et al. 2026, Am J Med Genet A — PMID:42226002](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.70220)
- [Bergès et al. 2026, Clin Genet — PMID:42249560](https://pubmed.ncbi.nlm.nih.gov/42249560/)
- [Guzzi et al. 2018, Cell — PMID:29628141](https://www.sciencedirect.com/science/article/pii/S0092867418302885)
- [Guzzi et al. 2022, Nat Cell Biol — PMID:35292784](https://www.nature.com/articles/s41556-022-00852-9)
- [Cui et al. 2021, Nat Cancer — PMID:35121864](https://pmc.ncbi.nlm.nih.gov/articles/PMC8809511/) · [Cancer Discov commentary](https://aacrjournals.org/cancerdiscovery/article/11/10/2367/665576/Glioblastoma-Is-Dependent-on-tRNA) · [Trends Pharmacol Sci commentary](https://www.cell.com/trends/pharmacological-sciences/abstract/S0165-6147(21)00191-7)
- [Purchal et al. 2022, PNAS — PMID:35058356](https://www.pnas.org/doi/10.1073/pnas.2109708119)
- [PUS7 crystal structure, Nucleic Acids Res 2021 — PMID:34718722](https://pubmed.ncbi.nlm.nih.gov/34718722/)
- [Liu et al. 2025, Mol Brain (ILPFC fear extinction) — PMID:41094471](https://pubmed.ncbi.nlm.nih.gov/41094471/)
- [tRNA Ψ map / stand-alone PUS enzymes, Nat Cell Biol 2025 — PMID:41136621](https://www.nature.com/articles/s41556-025-01803-w)
- [7SK pseudouridylation & Pol II elongation, Nat Commun 2025 — PMID:41168165](https://pubmed.ncbi.nlm.nih.gov/41168165/)
- [Cytoplasmic PUS7 & stress tolerance, Nat Commun 2026 — PMID:41997936](https://pubmed.ncbi.nlm.nih.gov/41997936/)
- [Rodell et al. 2026, Cell Genomics (Nano-Mod-Amp) — PMID:42532042](https://pubmed.ncbi.nlm.nih.gov/42532042/)
- [Luo et al. 2025, Nat Rev Mol Cell Biol — PMID:40394244](https://www.nature.com/articles/s41580-025-00852-1)
- [Pseudouridine modification in the nervous system, Int J Neurosci — PMID:38407188](https://pubmed.ncbi.nlm.nih.gov/38407188/)
- [Impact of pseudouridine on human tRNA, Biochem Soc Trans 2026 — PMID:42290177](https://pubmed.ncbi.nlm.nih.gov/42290177/)
- [PUS7 as a context-specific cancer target, JPET 2026 — PMID:42190315](https://pubmed.ncbi.nlm.nih.gov/42190315/)
- [Pseudouridine Synthase 7 in Cancer, Cells 2025 — PMID:40940790](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12428485/)
- [Full PUS7 PubMed result set (86 records)](https://pubmed.ncbi.nlm.nih.gov/?term=PUS7&sort=date&size=100)

**Databases:**
- [OMIM 618342 (IDDABS)](https://www.omim.org/entry/618342) · [OMIM 616261 (PUS7)](https://www.omim.org/entry/616261)
- [HPO annotations, OMIM:618342](https://ontology.jax.org/api/network/annotation/OMIM:618342)
- [MONDO:0032687 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0032687)
- [HGNC:26033](https://rest.genenames.org/fetch/symbol/PUS7) · [UniProt Q96PZ0](https://rest.uniprot.org/uniprotkb/Q96PZ0.txt)
- [ClinVar PUS7](https://www.ncbi.nlm.nih.gov/clinvar/?term=PUS7%5Bgene%5D) (225 records; 44 pathogenic)
- [EBI Gene2Phenotype PUS7 (G2P02633)](https://www.ebi.ac.uk/gene2phenotype/) · [ClinGen PUS7](https://search.clinicalgenome.org/kb/genes/HGNC:26033) (no curation)
- [GTEx PUS7 expression](https://gtexportal.org/home/gene/PUS7) · [Human Protein Atlas PUS7](https://www.proteinatlas.org/ENSG00000091127-PUS7/tissue)
- [Alliance of Genome Resources HGNC:26033 orthologs](https://www.alliancegenome.org/gene/HGNC:26033)
- [MGI:1925947 (mouse Pus7)](https://www.informatics.jax.org/marker/MGI:1925947) · [IMPC Pus7](https://www.mousephenotype.org/data/genes/MGI:1925947)
- [FlyBase Pus7 FBgn0035901](https://flybase.org/reports/FBgn0035901.htm) · [RGD Pus7 1307054](https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=1307054) · [ZFIN pus7](https://zfin.org/ZDB-GENE-060620-1)
- [NIH GTR PUS7](https://www.ncbi.nlm.nih.gov/gtr/genes/54517/) · [ClinicalTrials.gov](https://clinicaltrials.gov/) (0 studies for PUS7)
- [PRIDE PXD008676](https://www.omicsdi.org/dataset/pride/PXD008676)