---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T20:24:04.049540'
end_time: '2026-07-30T20:29:22.540660'
duration_seconds: 318.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CANVAS (cerebellar ataxia, neuropathy, and vestibular areflexia syndrome;
    RFC1 repeat expansion)
  mondo_id: MONDO:0044720
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
  web_search_requests: 18
  num_turns: 20
  total_cost_usd: 1.8316799999999995
  session_id: 5dd887df-f66e-565b-8209-dadd5bf74d40
  stop_reason: end_turn
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CANVAS (cerebellar ataxia, neuropathy, and vestibular areflexia syndrome; RFC1 repeat expansion)
- **MONDO ID:** MONDO:0044720 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CANVAS (cerebellar ataxia, neuropathy, and vestibular areflexia syndrome; RFC1 repeat expansion)** covering all of the
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

# CANVAS (Cerebellar Ataxia, Neuropathy, and Vestibular Areflexia Syndrome) / RFC1-Related Disease: Comprehensive Research Report

## 1. Disease Information

**Overview:** CANVAS is a late-onset (typically 6th decade), recessively inherited neurodegenerative disorder caused by biallelic intronic pentanucleotide repeat expansions in *RFC1* (Replication Factor C subunit 1). The eponymous acronym reflects its three cardinal domains: **C**erebellar **A**taxia, **N**europathy (sensory neuronopathy), and **V**estibular **A**reflexia **S**yndrome. Since the genetic discovery in 2019, the disease is now understood to represent one pole of a much broader phenotypic continuum, and many authors now prefer the umbrella term "RFC1 CANVAS/spectrum disorder" or simply "RFC1 disease" (NCBI Bookshelf, GeneReviews, https://www.ncbi.nlm.nih.gov/books/NBK564656/).

**Key identifiers:**
- **OMIM (phenotype):** #614575 — Cerebellar Ataxia, Neuropathy, and Vestibular Areflexia Syndrome; CANVAS
- **OMIM (gene):** *102579 — Replication Factor C, Subunit 1; RFC1
- **MONDO:** MONDO:0044720
- **Orphanet:** ORPHA:504476
- **SNOMED CT:** 1236804009
- (GARD/NIH also lists it as "Cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome," https://rarediseases.info.nih.gov/diseases/17937/)

**Synonyms/alternative names:** CANVAS syndrome; RFC1-related ataxia; RFC1 CANVAS/spectrum disorder; RFC1 disease; sensory ataxia with bilateral vestibulopathy and cough. Some limited-phenotype presentations are described in the literature as "CANVAS-minus" (isolated sensory neuronopathy, isolated bilateral vestibulopathy, ataxia with chronic cough, ataxia-neuropathy without vestibular loss).

**Evidence base:** Information is derived predominantly from **aggregated disease-level clinical cohorts** (retrospective and prospective multicenter case series, e.g., the 100-patient GeneReviews-cited cohort, the ARCA registry natural history study), rather than single-patient case reports, supplemented by molecular/genetic population-frequency data (gnomAD-style control cohorts) and increasingly by iPSC-neuron and animal-model mechanistic studies.

---

## 2. Etiology

**Primary cause:** Biallelic (homozygous or compound heterozygous), non-reference intronic pentanucleotide repeat expansions in intron 2 of *RFC1*, most commonly the motif **(AAGGG)n** replacing the reference **(AAAAG)11** allele. This was independently discovered by two groups in 2019:
- Cortese A, et al. "Biallelic expansion of an intronic repeat in RFC1 is a common cause of late-onset ataxia." *Nat Genet.* 2019;51(4):649-658.
- Rafehi H, et al. "Bioinformatics-Based Identification of Expanded Repeats: A Non-reference Intronic Pentanucleotide Repeat in RFC1 Causes CANVAS." *Am J Hum Genet.* 2019;105(1):151-165. PMID: 31178126.

**Genetic risk factors:**
- Biallelic pathogenic repeat configurations at the *RFC1* intron 2 locus (see Section 4 for full motif table).
- High population carrier frequency of the pathogenic (AAGGG)exp allele creates risk of **pseudodominance** — apparent vertical transmission across generations in the absence of consanguinity, due to a carrier partner marrying into the family (Cerebellum, 2024, "Pseudodominance in RFC1-Spectrum Disorder," https://link.springer.com/article/10.1007/s12311-024-01735-5).
- Population/ethnicity-specific founder configurations (see Section 9).

**Environmental risk factors:** No environmental/infectious/toxic causal factor is established. However, several agents are reported to **exacerbate or unmask** the underlying vulnerability rather than cause it:
- Neurotoxic chemotherapy agents and pyridoxine (peripheral nerve toxicity)
- Phenytoin (cerebellar toxicity)
- Aminoglycosides (vestibulotoxicity)
- Chronic alcohol use
(GeneReviews management section explicitly lists these as agents/circumstances to avoid because they may worsen the phenotype.)

**Age/sex:** Onset is typically in mid-to-late adulthood (mean ~52 years, range 19–76); no strong sex skew has been consistently reported across cohorts.

**Protective factors:** None established. Heterozygous carriers of a single pathogenic expansion are, to date, uniformly reported as asymptomatic — i.e., monoallelic carriage itself functions as implicitly "protective" relative to the biallelic state, but no specific protective allele or modifier variant has been validated.

**Gene-environment interaction:** Not established as a primary disease mechanism; the described environmental "risk factors" act at the level of symptomatic exacerbation of an already-genetically-determined neurodegenerative process (multi-hit model: genetically vulnerable dorsal root ganglion/vestibular ganglion/Purkinje neurons made symptomatic sooner by additional neurotoxic insults).

---

## 3. Phenotypes

The clinical picture is a **multisystem, spatiotemporally evolving ganglionopathy/cerebellopathy**. Using GeneReviews-cited retrospective cohort data (n=100) and additional cohort studies:

| Phenotype | Frequency | Onset/Course | Suggested HPO term |
|---|---|---|---|
| Sensory neuropathy/neuronopathy (non-length-dependent, DRG) | 100% | Often earliest manifestation; progressive | HP:0003474 (Peripheral axonal neuropathy) / HP:0007141 (Axonal loss); consider HP:0012394 (sensory neuronopathy context) |
| Bilateral vestibular areflexia/hypofunction | 69% overall (93% of those formally tested) | Mid-course; produces oscillopsia | HP:0007751 (Bilateral sensorineural hearing impairment - N/A) → better: HP:0025406 (Vestibular dysfunction) |
| Chronic dry/spasmodic cough | 64–97% (higher in some cohorts) | Can precede neurologic onset by years-to-decades, sometimes starting in the 2nd–3rd decade | HP:0031246 (Chronic cough) |
| Full CANVAS triad (cerebellar + sensory + vestibular) | ~63% (up to two-thirds); full triad may take >10 yrs to manifest | Progressive, sequential | — |
| Cerebellar syndrome (gait/limb ataxia, dysarthria, oculomotor signs) | 63% | Progressive, later-appearing element | HP:0001251 (Ataxia); HP:0001260 (Dysarthria); HP:0000639 (Nystagmus); HP:0000751 (Gaze-evoked nystagmus); HP:0007766 (Downbeat nystagmus) |
| Oscillopsia | ~33% | Related to bilateral VOR failure | HP:0025430-type visual disturbance (no exact dedicated HPO term; often coded under nystagmus/vestibular categories) |
| Dysautonomia (orthostatic hypotension, erectile dysfunction, constipation, urinary dysfunction, sweating changes) | 32–50% | Usually mild, rarely disabling (contrasts with MSA) | HP:0001278 (Orthostatic hypotension); HP:0000021 (Erectile dysfunction); HP:0002019 (Constipation) |
| Dysphagia | Later-stage | Progressive | HP:0002015 (Dysphagia) |
| Motor neuron involvement (fasciculations, mild weakness/wasting) | ~55% in some cohorts (motor-neuron-focused study) | Can mimic ALS/MND presentations | HP:0002380 (Fasciculations); HP:0007083 (motor neuron degeneration context) |
| Parkinsonism | ~10% | Overlaps with/mimics atypical parkinsonism, MSA-C | HP:0001300 (Parkinsonism) |
| Truncal/appendicular ataxia, saccadic dysmetria | Core cerebellar sign | Progressive | HP:0002078 (Truncal ataxia); HP:0001305 (Dysmetria) |

**Quality of life impact:** Progressive gait imbalance (worse in darkness, due to combined sensory + vestibular + cerebellar deafferentation) is typically the presenting and most disabling complaint. Natural history data (GeneReviews) indicate: ~50% require an assistive mobility device (cane) by 10 years from onset, and ~25% become wheelchair-dependent by ~15 years; **life expectancy is not reduced**. Chronic cough itself can be socially disabling and diagnostically misleading (frequently treated for years as idiopathic/refractory chronic cough before neurologic diagnosis) (European Respiratory Society, "CANVAS: a neurogenic cough prototype," https://publications.ersnet.org/content/erjor/10/4/00024-2024).

**Diagnostic yield caveat:** Even in cohorts selected for the "full" CANVAS phenotype, biallelic RFC1 expansions are found in 82–97% (i.e., some phenocopies without RFC1 expansion exist); in broader "late-onset ataxia" cohorts unselected for the full triad, the yield drops to 14–22% (GeneReviews, https://www.ncbi.nlm.nih.gov/books/NBK564656/).

---

## 4. Genetic/Molecular Information

**Causal gene:** *RFC1* (chromosome 4p14; encodes the large subunit of Replication Factor C, the clamp-loader complex for PCNA). OMIM gene: *102579.

**Locus/repeat details — normal vs. pathogenic motifs (per GeneReviews and Currie et al., *Brain* 2023, "Normal and pathogenic variation of RFC1 repeat expansions: implications for clinical diagnosis," https://academic.oup.com/brain/article/146/12/5060/7224416):**

| Allele class | Motif / structure | Repeat size | Population frequency | Pathogenicity |
|---|---|---|---|---|
| Reference/common normal | (AAAAG)11 | 11 | ~0.75 | Benign |
| Normal, expanded but non-pathogenic | (AAAAG)12–200 | 12–200 | ~0.13 | Benign |
| Normal, expanded but non-pathogenic | (AAAGG)40–1000 | 40–1000 | ~0.08 | Benign |
| Non-pathogenic (heterozygous, found in patients and controls) | AAGAG, AGAGG, interrupted AAAAG | variable | — | Benign |
| **Pathogenic (most common)** | **(AAGGG)exp** | ~400 to >2000 (max reported 2750) | allele frequency 0.01–0.04 | Fully penetrant when biallelic |
| Pathogenic (Asia-Pacific/Japanese) | (ACAGG)exp | ~1000 | rare; carrier freq ~0.26% South Asia, ~0% Europe | Pathogenic, common in East Asians |
| Pathogenic (Māori/Cook Islands founder) | (AAAGG)10–25(AAGGG)exp(AAAGG)4–6 | 990–1940 | Founder population-specific | Pathogenic (Beecroft et al., *Brain* 2020;143(9):2673-2680) |
| Other reported pathogenic motifs | AGGGC, AAGGC (South Asian family) | variable | rare | Pathogenic in trans with AAGGG or homozygous |

The repeat sits within an **AluSx3 transposable-element-derived poly(A) tract** in intron 2 — i.e., the expansion co-opts a retrotransposon-derived sequence, and the pathogenic (AAGGG)n motif is on the antisense strand relative to the reference (AAAAG)n.

**Variant classification/type:** Non-coding (intronic) short tandem repeat/microsatellite expansion — a repeat-expansion disorder mechanistically analogous to other STR diseases (e.g., Friedreich ataxia GAA, myotonic dystrophy CTG), but recessive rather than the more typical dominant repeat-expansion pattern. Rare **truncating point variants/small indels** in *RFC1* have also been reported in trans with an expanded allele or, less commonly, biallelically, broadening the allelic spectrum (Neurology, "Truncating Variants in RFC1 in CANVAS," PMC9931080, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9931080/).

**Allele frequency in population databases:** Carrier (heterozygous) frequency of pathogenic AAGGG expansion estimated at 0.7–6.8% depending on population/method, with more conservative recent estimates around 0.2% (2/1000) in Caucasian cohorts once biallelic segregation was more strictly required; ~2.24% in a Chinese Han population. Predicted homozygous/biallelic population frequency ranges from ~1/625 to ~1/712 in earlier estimates (making RFC1 disease one of the most common causes of inherited ataxia), though the more conservative later estimate implies a substantially lower biallelic frequency (GeneReviews; ResearchGate Māori founder study; Neurology Genetics prevalence study, https://www.neurology.org/doi/10.1212/NXG.0000000000000440).

**Somatic vs. germline:** Germline only; no somatic mosaicism or cancer association reported.

**Functional consequence / mechanism (loss-of-function debate):** Counter-intuitively for a recessive disease, "preliminary studies have not shown reduced expression or overt loss of function of RFC1 protein" in early work (GeneReviews). More recent mechanistic studies refine this:
- The pathogenic (AAGGG)n repeat (DNA and transcribed RNA) forms stable parallel **G-quadruplex (G4)** structures (and can also form triplex structures), which stall DNA replication forks, reduce RFC1 transcript/gene expression in a tissue-specific manner, and increase cellular sensitivity to DNA damage (PMC10563062; PMC10954463; 2025 bioRxiv "CANVAS causing AAGGG repeat expansions cause tissue-specific reduction in RFC1 expression and increase sensitivity to DNA damage," https://www.biorxiv.org/content/10.1101/2025.11.18.688292).
- A 2024 human iPSC-neuron (iNeuron) study (Science Advances, https://www.science.org/doi/10.1126/sciadv.adn2321; PMC11373605) found that CRISPR deletion of a single expanded (AAGGG) allele rescues synaptic/developmental deficits in patient neurons, but simple restoration of RFC1 protein does NOT rescue the phenotype — arguing for a **repeat-dependent but RFC1-protein-independent ("RFC1-independent")** toxic mechanism, i.e., a repeat-RNA or R-loop/G4-mediated gain-of-toxic-function superimposed on a partial expression loss, rather than a pure loss-of-function model.
- Structural work on RFC1 as part of the CTF18-RFC alternative clamp loader (cryo-EM, 2024–2025, eLife/PNAS) clarifies normal RFC1 biology (PCNA loading, replication/repair fidelity) but is not itself CANVAS-specific.

**Modifier genes:** No clinically validated modifier genes; "no clinically relevant genotype-phenotype correlations have been identified" per GeneReviews, though larger repeat size has been loosely associated with earlier age of onset in some series.

**Epigenetics:** Not a major established mechanism for CANVAS specifically (contrast with e.g. Fragile X, where CGG expansion drives promoter methylation/silencing); the dominant proposed nucleic-acid mechanism is G-quadruplex/secondary-structure formation rather than DNA methylation-mediated silencing, though tissue-specific transcript reduction is documented.

**Chromosomal abnormalities:** None; this is a single-locus repeat expansion, not a copy-number/structural chromosomal disorder.

**Suggested ontology terms:** Gene: HGNC RFC1 (hgnc:9969 approx. — verify via HGNC before use); process: GO:0006281 (DNA repair), GO:0006260 (DNA replication), GO:0032201 (telomere maintenance — related clamp-loader biology), GO:0051973 (positive regulation of telomerase activity — tangential).

---

## 5. Environmental Information

- **Environmental factors:** None established as causal. As above, certain iatrogenic exposures (neurotoxic chemotherapeutics, pyridoxine excess, phenytoin, aminoglycosides) and chronic alcohol use are documented as **aggravating/unmasking** factors rather than causal ones.
- **Lifestyle factors:** No specific dietary, occupational, or lifestyle causal association reported in the literature reviewed.
- **Infectious agents:** None implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (proposed, still partially unresolved):**

1. **Trigger:** Biallelic intronic (AAGGG)n (or other pathogenic-motif) expansion in *RFC1* intron 2, embedded in an AluSx3-derived poly(A) tract.
2. **Molecular consequence:** Repeat DNA/RNA folds into G-quadruplex (and triplex) secondary structures → replication fork stalling, tissue-specific reduction of RFC1 transcript, and (per newer iNeuron data) additional RFC1-protein-independent toxic mechanisms affecting neuronal development and synaptic connectivity. Increased sensitivity to DNA damage has also been demonstrated in cellular/Drosophila models.
3. **Cellular process:** Selective, non-length-dependent degeneration of specific neuronal populations with high metabolic/genomic-integrity demands: dorsal root ganglion (DRG) sensory neurons, vestibular ganglion neurons, and cranial nerve ganglia V (trigeminal) and VII (facial), plus cerebellar Purkinje cells and (in a subset) motor neurons.
4. **Tissue-level pathology:** Post-mortem/pathology studies show ganglionic and nerve-root atrophy with neuronal cell loss replaced by **psammoma bodies** and **satellite (glial) cell proliferation** in the DRG/cranial ganglia (a "ganglionopathy"/sensory neuronopathy pattern rather than a classic dying-back axonopathy), plus cerebellar and basal ganglia atrophy with diffuse Purkinje cell loss.
5. **Systemic/clinical output:** Progressive sensory ataxia (proprioceptive loss) + bilateral vestibular failure (loss of VOR, oscillopsia) + cerebellar dysfunction (gait/limb ataxia, dysarthria, oculomotor abnormalities) — a triple-deafferentation syndrome that compounds imbalance beyond any single system's contribution. Chronic cough is hypothesized to reflect a similar sensory neuronopathy affecting vagal/laryngeal afferents (a "neurogenic cough" mechanism), often the earliest and longest-preceding symptom.

**Molecular pathways:** DNA replication/repair pathway (RFC1 as the large subunit of the RFC clamp-loader complex, loading PCNA onto DNA to enable processive DNA polymerase activity — canonical role, GO:0006260, GO:0006281); no classical signaling cascade (Wnt/MAPK/mTOR/PI3K-AKT) has been specifically implicated as primary driver — the mechanism is nucleic-acid structural/genome-integrity based rather than a signal-transduction defect.

**Cellular processes:** Impaired DNA damage response/replication stress in affected neurons; selective neuronal vulnerability of post-mitotic ganglionic neurons (an interesting paradox for a "replication" gene, suggesting a replication-independent, transcription-coupled or R-loop-related toxicity in non-dividing cells); neurodevelopmental impact demonstrated in zebrafish (impaired granule and Purkinje cell progenitor expansion/differentiation) suggesting RFC1 also has a role in normal neurodevelopmental proliferation, distinct from its adult neurodegenerative role.

**Protein dysfunction:** Not a classical misfolding/aggregation disease (unlike polyQ repeat disorders) — mechanism centers on the repeat DNA/RNA nucleic acid structure itself (G-quadruplex, R-loop potential) rather than an aberrant RFC1 protein conformer; early studies found preserved RFC1 protein levels overall, though newer tissue-specific transcript-reduction data complicates this.

**Immune system involvement:** Not a primary autoimmune mechanism; however, satellite glial cell proliferation in ganglia may represent a secondary neuroinflammatory/reactive response to neuronal loss. Note also (separately) that *RFC1* expansions have been found at increased frequency in some cohorts of "immune-mediated neuropathy" patients (Scientific Reports 2023, https://www.nature.com/articles/s41598-023-45011-8), raising the possibility of diagnostic overlap/mimicry rather than a shared immune mechanism.

**Tissue damage mechanisms:** Selective ganglionic/Purkinje neuronal loss (a form of programmed neurodegeneration linked to genomic instability/replication stress) rather than classical oxidative-stress/ischemia/fibrosis mechanisms.

**Advanced/omics findings:**
- **Single-cell/model organism:** Zebrafish *rfc1* loss-of-function model (CRISPR/Cas9) shows a developmental role for rfc1 in expansion/differentiation of cerebellar granule and Purkinje neuronal progenitor pools (*Nat Commun* 2025, https://www.nature.com/articles/s41467-025-60775-5; PMC12217872).
- **iPSC-neuron transcriptomic/functional profiling:** CANVAS patient-derived iNeurons show synaptic connectivity and neurodevelopmental gene-expression deficits rescued by CRISPR correction of the repeat but not by RFC1 re-expression (Science Advances 2024).
- **Structural biology:** Cryo-EM structures of RFC1-containing clamp loader complexes (2024–2025) clarify normal PCNA-loading biology, providing a structural backdrop, though not disease-specific.
- **G-quadruplex structural studies:** NMR/biophysical work (PMC10563062, PMC10954463) directly demonstrates that pathogenic AAGGG (but not benign AAAAG) repeats form G4/triplex structures that stall replication and dysregulate gene expression — proposed as a druggable structural target (small-molecule G4 ligands, helicases).

**Suggested GO terms:** GO:0006260 (DNA replication), GO:0006281 (DNA repair), GO:0000731 (DNA synthesis involved in DNA repair), GO:0051983 (regulation of chromosome segregation - tangential), GO:0002087 (regulation of respiratory gaseous exchange by nervous system control of breathing — for cough mechanism, speculative).
**Suggested CL terms:** CL:0000540 (neuron), CL:0000617 (GABAergic neuron - Purkinje cell subtype context), CL:1001580 (Purkinje cell, if available in CL) — verify via OAK; CL:0000561 (amacrine cell — N/A); sensory ganglion neuron terms should be verified (dorsal root ganglion sensory neuron).
**Suggested UBERON terms:** UBERON:0002037 (cerebellum), UBERON:0000044 (dorsal root ganglion), UBERON:0001846 (vestibular ganglion — verify exact ID), UBERON:0001651 (trigeminal ganglion), UBERON:0001654 (facial nerve/geniculate ganglion — verify).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Cerebellum (vermis, crus I especially), peripheral sensory nervous system (dorsal root ganglia), vestibular end-organs/vestibular ganglion (bilateral), cranial nerve ganglia V and VII.
- **Secondary:** Spinal cord (posterior column degeneration visible on MRI as T2 hyperintensity, with cord atrophy), basal ganglia (atrophy reported at autopsy, correlating with parkinsonism in a subset), lower motor neurons (subset with motor neuron involvement/fasciculations), autonomic nervous system (mild).
- **Body systems:** Nervous system (central + peripheral + autonomic); secondarily respiratory system (chronic cough — likely neurogenic/vagal afferent rather than primary pulmonary pathology); gastrointestinal system (dysphagia, constipation); genitourinary system (erectile dysfunction, bladder dysfunction).

**Tissue/cell level:** Neuronal loss in dorsal root ganglia and cranial sensory ganglia with replacement by **psammoma bodies** and **satellite glial cell proliferation**; diffuse cerebellar Purkinje cell loss; cerebellar granule cell layer involvement (per zebrafish developmental model).

**Subcellular level:** Nuclear/genomic — the core molecular lesion is an intronic DNA repeat forming G-quadruplex secondary structure, implicating nuclear DNA replication/repair machinery (GO Cellular Component: nucleus, replication fork) rather than a specific organelle like mitochondria or lysosome.

**Localization:** Bilateral and symmetric in essentially all core features (bilateral vestibular areflexia by definition, bilateral/symmetric sensory neuropathy, cerebellar vermian atrophy) — no lateralization reported, consistent with a systemic/genetic rather than focal-structural mechanism.

---

## 8. Temporal Development

**Onset:** Adult/late-onset disease. Mean age of neurological symptom onset ~52 years (range 19–76). Chronic cough, when present, frequently precedes neurological onset by years to decades (onset sometimes in the 2nd–3rd decade of life). Onset pattern is **insidious/chronic**, not acute or subacute.

**Progression:** Slowly progressive, with a well-documented **spatiotemporal pattern**: early involvement of sensory (DRG) neurons, followed years later by vestibular dysfunction, followed by cerebellar dysfunction — full triad may take over a decade to manifest, and only ~two-thirds of patients ever develop all three domains. Disease course is chronic and lifelong (non-remitting), without a defined staging system (unlike cancer staging); natural history/longitudinal imaging studies are ongoing (PubMed 40908706, "Longitudinal Evaluation of Ataxia and Brain Structural Changes in RFC1-Related Disorder").

**Progression rate:** Notably slower than its key mimic, multiple system atrophy (MSA) — mean survival from onset to death in MSA is ~9.3 years, whereas RFC1 CANVAS/spectrum disorder progresses very slowly and **does not appear to shorten life expectancy**.

**Patterns:** No spontaneous remission described. No clearly defined "critical period" for intervention, given the current absence of disease-modifying therapy; the main "window" emphasized in the literature is for **early diagnostic recognition** (e.g., of isolated chronic cough or bilateral vestibulopathy) to shorten the diagnostic odyssey.

---

## 9. Inheritance and Population

**Epidemiology:**
- RFC1-associated repeat expansions are one of the **most common identified genetic causes of adult-onset/late-onset ataxia**, found in 14–22% of unselected late-onset ataxia cohorts and up to 82–97% of cohorts selected for the full CANVAS phenotype.
- Predicted biallelic (disease) population frequency estimates range widely: ~1/625–1/712 (early estimates) down to more conservative later estimates (~2/1000 carrier frequency implying a lower biallelic frequency) in Caucasian populations — reflecting evolving methodology (Southern blot/long-read vs. PCR-only screening) (Neurology Genetics, https://www.neurology.org/doi/10.1212/NXG.0000000000000440).
- More than 200 individuals (simplex or familial autosomal recessive pattern) had been reported with biallelic AAGGG expansions as of the GeneReviews review.

**Inheritance pattern:** Autosomal recessive. Because carrier frequency of the pathogenic allele is unusually high for a recessive disease, **pseudodominance** (apparent multi-generational transmission mimicking autosomal dominant inheritance) is well documented and should not be mistaken for AD inheritance.

**Penetrance:** Full penetrance reported for biallelic (AAGGG)exp/(AAGGG)exp and compound heterozygous pathogenic genotypes (age-dependent — the disease is late-onset, so "full penetrance" is realized only with sufficient lifespan/observation).

**Expressivity:** Variable — phenotypic spectrum ranges from full CANVAS triad to isolated/limited system involvement (pure sensory neuronopathy, isolated bilateral vestibulopathy, isolated cough), with no established genotype-phenotype correlation to explain this variability (repeat size shows only a loose association with age of onset).

**Genetic anticipation:** Not a feature of this disorder (in contrast to unstable dominant repeat-expansion diseases like Huntington disease or myotonic dystrophy) — consistent with a recessive, non-anticipating repeat disorder.

**Germline mosaicism:** Not specifically reported/characterized in the literature reviewed.

**Founder effects:** Multiple population-specific founder configurations documented:
- A distinct **(AAAGG)10–25(AAGGG)exp(AAAGG)4–6** configuration is a founder allele in **New Zealand Māori and Cook Island** populations (Beecroft et al., *Brain* 2020;143(9):2673-2680, ResearchGate summary: "A Maori-Specific RFC1 pathogenic repeat configuration in CANVAS, likely due to a founder allele").
- The **(ACAGG)exp** motif is common in **East Asian** populations (identified in Asia-Pacific and Japanese CANVAS families), essentially absent in European cohorts (carrier frequency 0% Europe, 0.03% Africa, 0.26% South Asia).
- The common **(AAGGG)exp** allele is the predominant pathogenic configuration in **European/Caucasian** populations.

**Consanguinity:** Not a major driver given the relatively high population carrier frequency of pathogenic alleles (unlike most rare AR diseases where consanguinity is the dominant risk factor); however, consanguinity would still increase biallelic risk in any given family.

**Carrier frequency:** Heterozygous carrier frequency 0.7–4% in populations of Northern European origin; ~2.24% in Chinese Han; ranges up to 6.5–6.8% reported in some individual control cohorts, with more conservative pooled estimates around 0.2–2/1000 for confirmed biallelic-pathogenic carriers in later, more rigorously validated cohorts.

**Population demographics:** No strong sex-ratio skew reported in the literature surveyed. Geographic/ethnic variation is substantial and motif-specific (see founder effects above) — curators should note that a given population's dominant pathogenic motif differs (AAGGG in Europeans, ACAGG in East Asians, the compound AAAGG/AAGGG/AAAGG configuration in Māori/Cook Islanders), which has direct implications for assay design (repeat-primed PCR designed only for AAGGG will miss ACAGG or Māori-configuration alleles).

---

## 10. Diagnostics

**Clinical suspicion:** Onset after age 35 (though can be younger) with one or more of: sensory neuropathy/neuronopathy, bilateral vestibular dysfunction, cerebellar dysfunction, chronic cough, or dysautonomia. **No formal consensus diagnostic criteria have been established** (per GeneReviews).

**Electrophysiology:**
- Nerve conduction studies: reduced/absent sensory nerve action potentials (SNAPs) with normal motor conduction studies — the electrophysiological signature of a sensory neuronopathy/ganglionopathy (non-length-dependent).
- Abnormal blink reflex; H-reflex often preserved.
- Nerve ultrasound: reduced nerve cross-sectional area (a discriminating feature vs. inflammatory neuropathies), now formally studied as a predictive tool alongside cough and neuronopathy pattern (Brain Communications 2025, "Nerve ultrasound, neuronopathy and cough predict sensory neuropathy patients with RFC1 expansions," PMC12662233).

**Vestibular testing:** Bilaterally abnormal video head impulse test (vHIT); reduced/absent caloric responses; abnormal VOR gain — confirms bilateral vestibular areflexia/hypofunction.

**Imaging:**
- Brain MRI: cerebellar atrophy, particularly vermian and crus I atrophy (can be subtle early in disease).
- Spine MRI: spinal cord atrophy and T2-weighted posterior-column hyperintensity (dorsal column degeneration signature).
- Comprehensive multimodal deep-phenotyping studies integrating electrophysiology + imaging + otoneurological data are an active area of research (PMC12558705).

**Pathology/biopsy:** Not typically required for diagnosis; when performed (autopsy/rare biopsy series), shows ganglionic/nerve-root atrophy, neuronal loss, psammoma bodies, satellite glial cell proliferation, and diffuse Purkinje cell loss with cerebellar/basal ganglia atrophy.

**Genetic testing (central to diagnosis):**
- **Cannot be detected by standard sequence-based multigene panels or exome sequencing** — this is a critical practical point, since the pathogenic repeat is intronic and expanded, invisible to short-read exome capture.
- **Repeat-primed PCR (RP-PCR)** and conventional PCR are first-line targeted assays (must specifically target the pathogenic motif(s) — AAGGG, and regionally ACAGG or the Māori configuration as appropriate).
- **Southern blotting** is used for definitive sizing and confirmation of biallelic status.
- **Long-read sequencing** (e.g., Oxford Nanopore, PacBio) is an emerging/gold-standard technology that can resolve repeat motif, size, and complex/compound configurations in one assay, and is increasingly used to reanalyze existing genome sequencing data to improve diagnostic yield (medRxiv 2024, "RFC1 repeat expansion analysis from whole genome sequencing data simplifies screening and increases diagnostic rates").
- Standard short-read genome sequencing can raise suspicion of an expansion (via specialized repeat-expansion-calling algorithms, e.g., ExpansionHunter) but generally requires orthogonal confirmation (RP-PCR/Southern/long-read).

**Differential diagnosis (detailed in GeneReviews):**
- **Multiple system atrophy (MSA)** — the single most important mimic/misdiagnosis risk, especially the MSA-cerebellar (MSA-C) and parkinsonian subtypes; distinguished by RFC1 disease's slower progression, normal life expectancy, milder dysautonomia, presence of sensory neuronopathy and bilateral vestibular failure, and absence of the "hot cross bun" pontine sign or severe putaminal atrophy on MRI.
- **Spinocerebellar ataxia type 3 (SCA3/Machado-Joseph disease)** — dystonic-rigid extrapyramidal signs, sensorimotor (not pure sensory) neuropathy, ophthalmoplegia.
- **Friedreich ataxia** (late-onset presentations) — typical onset <25 years, cardiomyopathy, diabetes, skeletal deformity, pyramidal signs.
- **Mitochondrial disorders** (NARP, MIDD, Kearns-Sayre, POLG-related) — earlier onset, multisystem involvement, ophthalmoplegia, hearing/vision loss.
- **RNF170-related disease** — sensory ataxia + vestibular areflexia but normal cerebellar function/SNAPs.
- **Usher syndrome types I/II** — vestibular hypofunction plus hearing and visual loss.
- Other causes of bilateral vestibular areflexia (aminoglycoside ototoxicity, Ménière disease, bilateral vestibular neuritis, NF2, infectious/inflammatory vestibulopathy).
- Idiopathic/immune-mediated peripheral neuropathy and idiopathic bilateral vestibulopathy cohorts, in which RFC1 screening is increasingly recommended given non-trivial diagnostic yield (Neurology 2023, "Frequency and Phenotype of RFC1 Repeat Expansions in Bilateral Vestibulopathy," https://www.neurology.org/doi/10.1212/WNL.0000000000207553).
- **Motor neuron disease/ALS phenocopies** — a German cohort study specifically screened MND-phenotype patients for biallelic RFC1 expansions (PMC11377604).
- **Parkinson's disease/atypical parkinsonism** — recent 2025 work frames "Parkinson's disease and MSA [as] gateways to RFC1-related disorders," i.e., RFC1 expansion screening is now advocated within apparent idiopathic PD/MSA cohorts.

**Screening:** No population/newborn screening program (adult-onset, no early intervention available); carrier screening and cascade testing in relatives of an affected proband is appropriate once a family's specific pathogenic motif is known; prenatal and preimplantation genetic testing are technically available once the familial genotype is defined.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Life expectancy does not appear to be reduced by RFC1 CANVAS/spectrum disorder — a key prognostic and counseling point, and a major discriminator from MSA (median survival ~9.3 years from onset in MSA vs. a much longer, non-life-limiting course in RFC1 disease).
- **Morbidity/function:** Progressive disability trajectory — approximately 50% of patients require an assistive ambulatory device (e.g., cane) roughly 10 years after symptom onset; approximately 25% become wheelchair-dependent by ~15 years after onset. Falls risk is significant given combined sensory + vestibular + cerebellar deafferentation.
- **Quality of life:** Substantially affected by chronic imbalance/fall risk, oscillopsia (which impairs reading/visual tasks during head movement), dysarthria/dysphagia in later stages, and the often years-long unexplained chronic cough that precedes diagnosis (with associated diagnostic-odyssey burden).
- **Complications:** Falls and fall-related injury; aspiration risk from dysphagia; social/occupational impact of dysarthria and chronic cough.
- **Prognostic factors:** No validated formal prognostic biomarker; loosely, larger repeat expansion size has been associated with earlier age of onset in some series, but no validated predictor of overall disease trajectory/severity exists. Ongoing natural-history/biomarker studies (e.g., the ARCA-registry-based global multicenter RFC1 natural history study) aim to establish quantitative outcome measures (SARA — Scale for Assessment and Rating of Ataxia; INAS — Inventory of Non-Ataxia Signs; CMTNS — Charcot-Marie-Tooth Neuropathy Score) for future trial readiness.

---

## 12. Treatment

**No disease-modifying or curative treatment currently exists.** Management is entirely multidisciplinary and symptomatic/supportive (per GeneReviews):

- **Ataxia:** Physical and occupational therapy (balance/gait training, strengthening); adaptive mobility devices (canes, walkers, motorized wheelchairs); inpatient rehabilitation; home fall-prevention modification; weight management. (MAXO:0000011 physical therapy)
- **Vestibular dysfunction:** Vestibular rehabilitation therapy — the standard of care for bilateral vestibular hypofunction generally; a CANVAS-specific case report on vestibular rehabilitation exists (ScienceDirect 2023, https://www.sciencedirect.com/science/article/pii/S167229302300048X). (MAXO term for vestibular/physical rehabilitation — verify exact MAXO ID)
- **Sensory neuropathy:** Counseling on injury avoidance (given impaired proprioception/pain sensation); pain management rarely required.
- **Autonomic dysfunction:** Symptomatic treatment of erectile dysfunction, urinary incontinence/retention, constipation/diarrhea, dry eyes/mouth. (MAXO:0000950 supportive care; NCIT:C15986 Pharmacotherapy as generic action term with appropriate `therapeutic_agent`)
- **Dysarthria:** Speech-language therapy; augmentative/alternative communication as needed. (MAXO term for speech therapy — MAXO:0000930)
- **Dysphagia:** Modified food consistency, videofluoroscopic/esophagographic evaluation, aspiration-risk assessment. (MAXO:0001351 occupational therapy / relevant swallowing-therapy term — verify)
- **Chronic cough:** Proton pump inhibitors if reflux contributes; pulmonology/ENT referral for refractory neurogenic cough. (NCIT:C15986 Pharmacotherapy + appropriate therapeutic_agent for PPI, e.g., omeprazole)
- **Agents to avoid (iatrogenic worsening):** Neurotoxic chemotherapy agents, high-dose pyridoxine, phenytoin, aminoglycosides, chronic alcohol use.

**Investigational/experimental therapeutics:**
- **Noisy galvanic vestibular stimulation** and **prosthetic vestibular implants** are cited as promising investigational approaches for the bilateral vestibular hypofunction component (general bilateral vestibular weakness literature, Curr Treat Options Neurol 2026, https://link.springer.com/article/10.1007/s11940-026-00866-w), not yet CANVAS-specific approved therapies.
- **Mechanism-targeted small-molecule/G-quadruplex-ligand strategies:** Structural biology work explicitly proposes that resolved G4 structures formed by pathogenic AAGGG repeats could guide rational design of small-molecule ligands or helicases to resolve the toxic secondary structure — a preclinical concept, not yet in trials (PMC10954463, PMC10563062).
- No published antisense oligonucleotide (ASO), gene-replacement, or gene-editing clinical program was identified in this search for RFC1/CANVAS specifically (searches for ASO/gene therapy approaches returned no CANVAS-specific hits) — this remains an unmet therapeutic gap, consistent with the disease being explicitly described in the primary literature as "currently untreatable" (Science Advances 2024).
- **Natural history/biomarker study:** A prospective global 2-year multicenter natural history study (ARCA registry, 31 centers) is underway to define clinical outcome measures and biomarkers in preparation for future interventional trials (Ataxia Global Initiative, https://ataxia-global-initiative.net/projects/rfc1-a-global-multicenter-multimodal-natural-history-clinical-outcome-and-biomarker-study-based-on-the-arca-registry/). The National Ataxia Foundation's CRC-SCA observational study also now includes RFC1 Ataxia/CANVAS as an eligible cohort.

**Treatment strategy/algorithm:** Sequential, symptom-triggered multidisciplinary referral (neurology, PT/OT, physiatry, speech-language pathology, respiratory/ENT, gastroenterology) with **annual neurologic surveillance** (or more frequently during acute change) using SARA and CMTNS as standardized outcome measures, per GeneReviews management/surveillance recommendations.

---

## 13. Prevention

- **Primary prevention:** None available — this is a genetic, adult-onset disorder with no known modifiable environmental cause to intervene upon prior to disease onset.
- **Secondary prevention/early detection:** Increasing clinical index of suspicion (screening idiopathic bilateral vestibulopathy, idiopathic chronic cough, and idiopathic late-onset ataxia/peripheral neuropathy cohorts for RFC1 expansions) shortens diagnostic delay and enables earlier supportive intervention/fall-prevention counseling, though it does not alter the underlying disease course given the absence of disease-modifying therapy.
- **Genetic/reproductive prevention:** Genetic counseling for affected individuals, carriers, and at-risk relatives regarding autosomal recessive inheritance and pseudodominance; carrier testing of at-risk relatives once the familial pathogenic motif is known; prenatal testing and preimplantation genetic testing are technically available options for reproductive planning; DNA banking is recommended given the rapidly evolving assay landscape (RP-PCR → Southern blot → long-read sequencing).
- **Tertiary prevention:** Avoidance of neurotoxic exposures (aminoglycosides, phenytoin, neurotoxic chemotherapy, high-dose pyridoxine, chronic alcohol) to prevent iatrogenic acceleration of neuropathy/cerebellar/vestibular injury in known or at-risk individuals; fall-prevention home modification; aspiration-risk mitigation for dysphagia.
- **Screening programs:** No population-level or newborn screening program exists (late-onset disease); targeted cascade genetic screening within affected families is the practical current approach.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease in other species:** No naturally occurring veterinary/wildlife CANVAS-like disease attributable to RFC1 was identified in the literature reviewed (no OMIA entry surfaced in this search). This appears to be a human-specific clinical entity as currently documented, likely reflecting both the specific human AluSx3-derived repeat locus (Alu elements are primate-specific transposons) and the recency of genetic characterization.
- **Orthologous gene:** RFC1 is a broadly conserved gene across vertebrates (mouse *Rfc1*, zebrafish *rfc1*, and more distant orthologs in *Drosophila* and yeast, given its fundamental role in DNA replication/PCNA loading) — see NCBI Gene for ortholog records. No repeat-expansion equivalent is expected in these species since the pathogenic locus is a human/primate-specific Alu-derived repeat.
- **Comparative pathology/evolutionary conservation:** The core RFC1 clamp-loader function is deeply conserved (yeast to human), underscoring why complete loss of function is developmentally lethal across species (see Section 15), while the CANVAS-causing repeat-expansion mechanism itself is a human-specific genomic event superimposed on this conserved gene.
- **Transmission/zoonotic potential:** Not applicable — this is a genetic (non-infectious) human disease.

---

## 15. Model Organisms

- **Mouse:** A conventional *Rfc1* knockout allele (Jackson Laboratory Phenotyping Center / IMPC-type resource) is **embryonic and/or pre-weaning lethal in the homozygous state**, precluding straightforward modeling of the human disease (which is caused by a hypomorphic repeat-expansion allele, not complete null) via simple knockout. This lethality itself is informative: it underscores that the human CANVAS-causing repeat allele must be substantially hypomorphic/partial-function (or repeat-toxic-gain-of-function) rather than a complete null, since affected humans are viable into adulthood.
- **Zebrafish:** To circumvent mouse embryonic lethality, a CRISPR/Cas9-generated zebrafish *rfc1* loss-of-function model was developed. *rfc1⁻/⁻* larvae are viable long enough (dying prematurely after ~10 days) to permit functional neurodevelopmental analysis. This model revealed a **key developmental role for rfc1 in the expansion and differentiation of cerebellar granule and Purkinje cell neuronal progenitor pools** (*Nat Commun* 2025, https://www.nature.com/articles/s41467-025-60775-5; PMC12217872) — informative for understanding baseline RFC1 neurodevelopmental biology, though it models complete loss-of-function rather than the repeat-expansion-specific toxic mechanism per se.
- **Drosophila:** A neuronal RFC1 *Drosophila* model expressing the pathogenic AAGGG repeat demonstrated **tissue-specific reduction in RFC1 transcript expression, impaired RFC1 function, and increased sensitivity to DNA damage** — directly modeling the repeat-toxicity mechanism rather than simple gene knockout (per 2025 bioRxiv preprint, https://www.researchgate.net/publication/397733610).
- **Human iPSC-derived neurons (iNeurons):** The most disease-relevant model to date. CANVAS patient fibroblast-derived iPSCs differentiated into neurons recapitulate defects in neuronal development and diminished synaptic connectivity; critically, **CRISPR-mediated deletion of a single expanded (AAGGG) allele rescues these phenotypes**, while simple re-expression of RFC1 protein does **not** rescue them — the key evidence for an RFC1-protein-independent, repeat-dependent toxic mechanism (Science Advances 2024, https://www.science.org/doi/10.1126/sciadv.adn2321; PMC11373605).
- **Model limitations:** No current animal model fully recapitulates the adult-onset, multisystem (cerebellar + sensory ganglionopathy + vestibular + cough) human phenotype with the biallelic repeat expansion genotype in vivo; existing models variably capture (a) complete RFC1 loss-of-function developmental biology (mouse/zebrafish knockouts) or (b) repeat-specific molecular toxicity in a heterologous/reduced system (Drosophila, human iNeurons) — a genuine **human-model-mismatch gap** exists between repeat-toxicity cellular models and an in vivo repeat-expansion "knock-in" animal model reproducing the full adult neurodegenerative phenotype, which had not yet been reported as of the sources reviewed here.
- **Research applications:** These models collectively support study of (1) normal RFC1 developmental neurobiology (granule/Purkinje progenitor expansion), (2) repeat-driven G-quadruplex/replication-stress toxicity, and (3) candidate therapeutic screening (e.g., G4-resolving small molecules, ASO/CRISPR repeat-targeting strategies) in a currently treatment-free disease.
- **Resources:** MGI (mouse *Rfc1* knockout phenotype data, IMPC), ZFIN (zebrafish *rfc1* model), standard Drosophila stock/CRISPR resources, and patient-derived iPSC lines (institution-specific biobanks, not yet indexed in a large public repository per this search).

---

## Summary Ontology Term Suggestions for KB Curation

- **Disease:** MONDO:0044720; Orphanet ORPHA:504476; OMIM #614575
- **Gene:** RFC1 (hgnc: — verify exact HGNC numeric ID before use, e.g. via `uv run runoak -i sqlite:obo:hgnc info RFC1`)
- **Key HP terms:** HP:0001251 (Ataxia), HP:0007141/HP:0003474 (axonal sensory neuropathy features — verify most specific term for "sensory neuronopathy"), HP:0025406/vestibular dysfunction term (verify exact HPO ID), HP:0031246 (Chronic cough), HP:0001278 (Orthostatic hypotension), HP:0000639 (Nystagmus), HP:0007766 (Downbeat nystagmus), HP:0001260 (Dysarthria), HP:0002015 (Dysphagia), HP:0002380 (Fasciculations), HP:0001300 (Parkinsonism)
- **GO terms:** GO:0006260 (DNA replication), GO:0006281 (DNA repair)
- **CL terms:** dorsal root ganglion sensory neuron, Purkinje cell, vestibular ganglion neuron (verify exact CL IDs via OAK before curation)
- **UBERON terms:** UBERON:0002037 (cerebellum), UBERON:0000044 (dorsal root ganglion), plus vestibular/trigeminal/facial ganglion terms (verify exact IDs)
- **MAXO terms:** MAXO:0000011 (physical therapy), MAXO:0000950 (supportive care), MAXO:0000930 (speech therapy), NCIT:C15986 (Pharmacotherapy, for PPI/symptomatic drugs)

**Important curatorial note (NEC risk):** Given that "CANVAS" and "RFC1 disease" nomenclature has evolved rapidly (2019–2025) and overlaps phenotypically with MSA, SCA3, Friedreich ataxia, and idiopathic bilateral vestibulopathy, curators should verify the MONDO:0044720 gene/OMIM anchors (RFC1, OMIM #614575/*102579) against any deep-research output before use, per the project's Named Entity Confusion preflight protocol.

---

### Sources

- [RFC1 CANVAS / Spectrum Disorder – GeneReviews®](https://www.ncbi.nlm.nih.gov/books/NBK564656/)
- [Normal and pathogenic variation of RFC1 repeat expansions: implications for clinical diagnosis (Brain, 2023)](https://academic.oup.com/brain/article/146/12/5060/7224416)
- [AAGGG repeat expansions trigger RFC1-independent synaptic dysregulation in human CANVAS neurons (Science Advances, 2024)](https://www.science.org/doi/10.1126/sciadv.adn2321)
- [AAGGG repeat expansions trigger RFC1-independent synaptic dysregulation in human CANVAS neurons – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11373605/)
- [CANVAS causing AAGGG repeat expansions cause tissue-specific reduction in RFC1 expression and increase sensitivity to DNA damage (bioRxiv, 2025)](https://www.biorxiv.org/content/10.1101/2025.11.18.688292.full.pdf)
- [Structural investigation of pathogenic RFC1 AAGGG pentanucleotide repeats reveals a role of G-quadruplex in dysregulated gene expression in CANVAS – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10954463/)
- [Pathogenic CANVAS-causing but not nonpathogenic RFC1 DNA/RNA repeat motifs form quadruplex or triplex structures – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10563062/)
- [RFC1-Related Disease: Molecular and Clinical Insights (Neurology Genetics)](https://www.neurology.org/doi/10.1212/NXG.0000000000200016)
- [Cerebellar ataxia, neuropathy and vestibular areflexia syndrome (CANVAS): from clinical diagnosis towards genetic testing – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11006361/)
- [CANVAS-related RFC1 mutations in patients with immune-mediated neuropathy – Scientific Reports](https://www.nature.com/articles/s41598-023-45011-8)
- [Truncating Variants in RFC1 in Cerebellar Ataxia, Neuropathy, and Vestibular Areflexia Syndrome – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9931080/)
- [Prevalence of RFC1-mediated spinocerebellar ataxia in a North American ataxia cohort – Neurology Genetics](https://www.neurology.org/doi/10.1212/NXG.0000000000000440)
- [Pseudodominance in RFC1-Spectrum Disorder – The Cerebellum](https://link.springer.com/article/10.1007/s12311-024-01735-5)
- [Cerebellar ataxia, neuropathy and vestibular areflexia syndrome: a neurogenic cough prototype – European Respiratory Society](https://publications.ersnet.org/content/erjor/10/4/00024-2024)
- [Nerve ultrasound, neuronopathy and cough predict sensory neuropathy patients with RFC1 expansions – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12662233/)
- [Motor neuron pathology in CANVAS due to RFC1 expansions – Brain](https://academic.oup.com/brain/article/145/6/2121/6470371)
- [RFC1-related ataxia is a mimic of early multiple system atrophy – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7958109/)
- [Multisystemic RFC1-Related Disorder – Neurology Clinical Practice](https://www.neurology.org/doi/10.1212/CPJ.0000000000200190)
- [Analysis and occurrence of biallelic pathogenic repeat expansions in RFC1 in a German cohort with motor neuron disease phenotype – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11377604/)
- [Frequency and Phenotype of RFC1 Repeat Expansions in Bilateral Vestibulopathy – Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000207553)
- [RFC1 regulates the expansion of neural progenitors in the developing zebrafish cerebellum – Nature Communications](https://www.nature.com/articles/s41467-025-60775-5)
- [RFC1 regulates the expansion of neural progenitors in the developing zebrafish cerebellum – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12217872/)
- [RFC1 in an Australasian neurological disease cohort: extending the genetic heterogeneity and implications for diagnostics – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10445415/)
- [Comprehensive phenotyping of RFC1-related disorder: integrating electrophysiological, brain imaging, and otoneurological data – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12558705/)
- [RFC1: a global multicenter multimodal natural history, clinical outcome and biomarker study, based on the ARCA registry](https://ataxia-global-initiative.net/projects/rfc1-a-global-multicenter-multimodal-natural-history-clinical-outcome-and-biomarker-study-based-on-the-arca-registry/)
- [Clinical Synopsis - #614575 - CANVAS - OMIM](https://omim.org/clinicalSynopsis/614575)
- [CANVAS Syndrome – Vestibular Disorders Association](https://vestibular.org/article/diagnosis-treatment/types-of-vestibular-disorders/canvas-syndrome-2/)
- [Cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome – GARD/NIH](https://rarediseases.info.nih.gov/diseases/17937/cerebellar-ataxia-with-neuropathy-and-bilateral-vestibular-areflexia-syndrome)