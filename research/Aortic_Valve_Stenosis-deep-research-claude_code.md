---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T14:07:03.906542'
end_time: '2026-08-10T14:13:17.393740'
duration_seconds: 373.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aortic Valve Stenosis
  mondo_id: ''
  category: Acquired
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
  num_turns: 21
  total_cost_usd: 1.6844580999999996
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aortic Valve Stenosis
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Aortic Valve Stenosis** covering all of the
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

# Aortic Valve Stenosis: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Aortic valve stenosis (AS) is the narrowing of the aortic valve orifice that obstructs left ventricular outflow during systole. In adults in industrialized nations it is overwhelmingly an **acquired, degenerative/calcific** disease — often termed calcific aortic valve disease (CAVD) or calcific aortic valve stenosis (CAVS) — arising from an active, cell-mediated process of lipid deposition, chronic inflammation, fibrosis, and dystrophic calcification of the valve leaflets that is mechanistically distinct from, but shares risk factors with, atherosclerosis (PMID:31912380; PMID:32160774). It is the most common valvular heart disease in high-income countries and the most frequent indication for valve intervention in the elderly. Globally, however, **rheumatic heart disease** remains an important cause of aortic (and mitral) valve stenosis in low- and middle-income countries, and **congenital bicuspid aortic valve (BAV)** is the leading cause of AS presenting before age 65.

**Key identifiers** (verify exact codes at time of KB curation via OAK/authoritative sources before use):
- **ICD-10-CM:** I35.0 (Nonrheumatic aortic (valve) stenosis); I06.0/I06.2 (Rheumatic aortic stenosis, with/without insufficiency); Q23.0 (Congenital stenosis of aortic valve)
- **ICD-11:** BC71.0 (aortic valve stenosis, non-rheumatic) / BC63 rheumatic aortic valve diseases (foundation-layer codes; confirm exact ICD-11 MMS entry)
- **MeSH:** D001024 (Aortic Valve Stenosis); D001022 (Aortic Valve Insufficiency, related)
- **OMIM:** 109730 (Aortic Valve Disease 1; AOVD1 — NOTCH1-related congenital/BAV form); related syndromic entries include 185500 (Williams-Beuren syndrome, associated with supravalvular AS via *ELN*) and 300363 (Filamin A-related valvulopathy)
- **Orphanet:** rare/syndromic subtypes are separately coded (e.g., isolated supravalvular aortic stenosis, Williams syndrome); degenerative calcific AS in the elderly is a common, non-rare disease and is not itself an Orphanet entry
- **MONDO:** search "aortic valve stenosis" for the current MONDO ID; congenital and syndromic subtypes are separately coded (e.g., NOTCH1-related bicuspid aortic valve)
- **HPO:** phenotype term "Aortic valve stenosis" (confirm exact HP ID via OAK) and "Bicuspid aortic valve" (HP:0004936, confirm)

**Common synonyms/alternative names:** Calcific aortic stenosis; senile/degenerative aortic stenosis; calcific aortic valve disease (CAVD); aortic sclerosis (the earliest, hemodynamically insignificant stage); valvular aortic stenosis; rheumatic aortic stenosis (etiology-specific); congenital aortic stenosis; bicuspid aortic valve stenosis; aortic valve calcification (AVC, when referring to the imaging/pathologic substrate rather than the hemodynamic lesion).

**Data provenance for this report:** Findings below are drawn from aggregated disease-level literature (systematic reviews, GWAS meta-analyses, randomized trials, registries such as PARTNER and the Global Burden of Disease study) rather than individual patient-level EHR data, consistent with standard knowledge-base curation sourcing.

---

## 2. Etiology

### 2a. Disease Causal Factors

Three broad etiologic categories converge on the same end-organ lesion (a stenotic, often calcified, aortic valve):

1. **Degenerative/calcific (most common in adults >65):** an active biological process — not passive "wear and tear" — involving endothelial injury, lipoprotein infiltration (notably Lp(a) and oxidized LDL), macrophage/T-cell-driven chronic inflammation, valve interstitial cell (VIC) osteoblastic transdifferentiation, and progressive nodular calcification, closely paralleling early atherogenesis but diverging mechanistically in later stages (PMID:31912380; PMID:32160774).
2. **Congenital (bicuspid or, rarely, unicuspid/quadricuspid) valve:** an abnormal two- (or one-) cusp valve morphology arising from developmental defects in endocardial cushion/valvulogenesis (notably via NOTCH1 signaling), which is hemodynamically stressed from birth and undergoes accelerated calcific degeneration, typically presenting 1–2 decades earlier than tricuspid degenerative AS.
3. **Rheumatic:** post-infectious autoimmune valvulitis following group A *Streptococcus* pharyngitis (acute rheumatic fever), causing commissural fusion, leaflet fibrosis/retraction and, over years to decades, stenosis — almost always accompanied by mitral valve involvement and typically with mixed stenosis/regurgitation.

Less common causes: radiation-induced valvulopathy (mediastinal radiotherapy, e.g., for Hodgkin lymphoma or breast cancer, years after exposure), chronic kidney disease/dialysis-associated valvular calcification, familial hypercholesterolemia (homozygous, causing severe premature supra/valvular aortic disease), and inborn errors such as Fabry disease (glycosphingolipid deposition in valve tissue).

### 2b. Risk Factors

**Genetic risk factors:**
- ***LPA* locus / elevated lipoprotein(a) [Lp(a)]** — the single strongest and most replicated genetic risk factor. GWAS identified rs10455872 and rs3798220 at the *LPA* locus, and Kringle IV type-2 copy-number variation, as determinants of plasma Lp(a) and of aortic valve calcium/AS risk (PMID cluster reviewed in PMC6787733, PMC9182826). A large Danish cohort/Mendelian-randomization study found a 10-fold increase in Lp(a) associated with an age/sex-adjusted hazard ratio of ~1.4 for AS, with an instrumental-variable (causal) estimate of ~1.6 — Mendelian randomization supports a **causal** role, not mere association (JACC 2013, PMID:24291273/doi 10.1016/j.jacc.2013.09.038).
- ***PALMD* (1p21)** and ***TEX41* (2q22)** loci — identified in the first large AS GWAS (Icelandic discovery cohort, 2,457 cases/349,342 controls, replicated in ~4,850 cases); rs7543130 (PALMD) OR≈1.20, P=1.2×10⁻²²; rs1830321 (TEX41) OR≈1.15, P=1.8×10⁻¹³. Both loci also associate with bicuspid aortic valve; TEX41 additionally associates with coronary artery disease (Nature Communications 2018, PMID:29511194).
- ***NOTCH1* (9q34.3)** — the gene with the strongest evidence for Mendelian/familial congenital aortic valve disease (OMIM 109730, Aortic Valve Disease 1/AOVD1, autosomal dominant). NOTCH1 loss-of-function mutations were first described by Garg et al. (2005) causing BAV with severe calcification, and account for an estimated 5–10% of non-syndromic BAV cases (PMC5573733; PMID:32720365). NOTCH1 haploinsufficiency both disrupts valvulogenesis and de-represses osteogenic gene programs (RUNX2, osteopontin) in adult VICs, linking developmental and degenerative calcification mechanisms; associations with osteoprotegerin/RANK/RANKL pathway dysregulation have also been reported (PMC5299165).
- **Multi-ancestry GWAS expansion** — the Million Veteran Program multi-ancestry GWAS and subsequent integrative genomic analyses replicated *ALPL*, *PALMD*, *TEX41*, *LPA*, *IL6*, and *FADS1*, and identified additional novel loci, plus candidate causal genes implicated via tissue-specific regulatory analysis (Circulation 2023; Nature Communications 2024, doi:10.1038/s41467-024-46639-4). *IL6*, *ALPL* (tissue-nonspecific alkaline phosphatase, directly relevant to mineralization biochemistry), and *NAV1* were highlighted as novel susceptibility genes in an earlier meta-analysis (bioRxiv 515494/subsequently published).
- **Other Mendelian/syndromic genetic causes:** *ELN* (elastin) haploinsufficiency in Williams-Beuren syndrome (supravalvular AS, OMIM 185500); *FLNA* (filamin A) in X-linked myxomatous/dysplastic valvulopathy; homozygous familial hypercholesterolemia (*LDLR*, *APOB*, *PCSK9*) causing premature valvular and supravalvular calcific disease.

**Environmental / clinical risk factors** (largely overlapping with atherosclerotic risk factors, reflecting shared early pathobiology):
- Advanced age (strongest non-genetic risk factor; prevalence rises steeply after age 65)
- Male sex
- Hypertension
- Diabetes mellitus / metabolic syndrome
- Smoking
- Elevated LDL-cholesterol and elevated Lp(a) (also environmentally/dietarily modulated on top of genetic baseline)
- Chronic kidney disease and CKD-mineral bone disorder (disordered calcium-phosphate handling promotes ectopic valvular/vascular calcification)
- Prior mediastinal radiation therapy
- Rheumatic fever history (for rheumatic AS specifically — itself driven by GAS pharyngitis exposure, crowding, and limited access to antibiotics/penicillin prophylaxis)
- Bicuspid aortic valve (a structural risk factor rather than classic "environmental" one, but non-Mendelian in most sporadic cases)

**Gene-environment interactions:** Elevated Lp(a) and LDL act as substrates for the same oxidative and inflammatory processes that also respond to metabolic-syndrome/diabetogenic dietary exposures — demonstrated experimentally in LDLr⁻/⁻ApoB100/100 mice, where a diabetogenic/procalcific diet markedly accelerated valvular calcification beyond genotype alone (PMID:29539583). This models a genotype (LDL/Lp(a) handling) × environment (diet, metabolic syndrome) interaction analogous to atherosclerosis. CKD represents another gene-environment convergence point: uremic mineral dysregulation accelerates calcification in individuals already genetically predisposed via LPA/PALMD/ALPL risk alleles, though large-scale interaction studies specific to AS are less mature than for the general Lp(a)-CVD relationship.

### 2c. Protective Factors

No robust genetic *protective* variant is established (in contrast to LDL/PCSK9 loss-of-function protective alleles for coronary disease). Statins/aggressive LDL-lowering, despite strong observational and mechanistic rationale (parallel to atherosclerosis biology), **failed** to slow AS progression in randomized trials:
- **SALTIRE** (atorvastatin vs placebo, n=155, up to 3 years): no reduction in aortic-jet velocity progression or valvular calcification.
- **SEAS** (simvastatin/ezetimibe vs placebo; NEJM 2008, doi:10.1056/NEJMoa0804602): no significant effect on AS progression; possible signal of increased cancer incidence noted as a trial-specific finding.
- **ASTRONOMER** (intensive rosuvastatin in mild-moderate AS; PMID:20080097): atorvastatin not associated with slowed hemodynamic progression.
- Meta-analyses of ~2,344 patients across randomized placebo-controlled lipid-lowering trials concluded current data do not support statins as a disease-modifying therapy for established AS, in contrast to their clear benefit for atherosclerotic events — implying that once calcific remodeling is established, lipid lowering alone cannot reverse the fibro-calcific process, and/or that the intervention window (before overt stenosis) had already closed in enrolled cohorts.

This "statin paradox" is itself a key mechanistic finding: it argues that early lipid-driven initiation and later self-sustaining osteogenic/fibrotic progression are at least partly biologically distinct phases, motivating newer targeted approaches (Lp(a)-lowering agents such as pelacarsen and lepodisiran are in trials for atherosclerotic CVD, with dedicated Lp(a)-AS progression trials also underway; specific trial identifiers should be confirmed against ClinicalTrials.gov at curation time).

---

## 3. Phenotypes

Aortic stenosis is characteristically **asymptomatic for years to decades** (long latent/compensated phase) before symptoms emerge once the valve area falls below a critical threshold (~1 cm²) and left ventricular hypertrophy can no longer compensate.

**Cardinal triad of symptoms (classically taught, sign of decompensation and adverse prognosis):**
- **Exertional dyspnea/heart failure symptoms** — most common; reflects diastolic dysfunction from concentric LV hypertrophy progressing to systolic dysfunction. HPO: consider "Dyspnea" (HP:0002094), "Exertional dyspnea" (verify HP ID), "Heart failure" (HP:0001635).
- **Angina** — even without epicardial coronary disease, due to increased myocardial oxygen demand (hypertrophy) outstripping supply (reduced coronary flow reserve, shortened diastolic filling time). HPO: "Angina pectoris" (verify ID).
- **Syncope/presyncope**, typically exertional — due to a fixed cardiac output unable to augment with exertion-induced peripheral vasodilation, and/or transient arrhythmia. HPO: "Syncope" (HP:0001279).

**Additional clinical signs:**
- Harsh crescendo-decrescendo systolic ejection murmur, loudest at the right second intercostal space, radiating to the carotids
- Diminished and delayed carotid upstroke (pulsus parvus et tardus)
- Soft/absent S2 (calcified, immobile leaflets)
- S4 gallop (atrial contraction against a stiff, hypertrophied ventricle)
- Sustained/heaving apical impulse
- Late complications: atrial fibrillation, heart failure with reduced or preserved EF, sudden cardiac death (particularly once symptomatic and untreated), acquired von Willebrand syndrome/Heyde syndrome (GI angiodysplasia bleeding due to shear-induced degradation of high-molecular-weight vWF multimers across the stenotic valve)

**Laboratory abnormalities:** elevated BNP/NT-proBNP (correlates with symptom onset and prognosis, used to trigger intervention in select asymptomatic patients per guidelines); acquired reduction of high-molecular-weight von Willebrand multimers (Heyde syndrome); no disease-specific routine chemistry abnormality otherwise.

**Phenotype characteristics:**
- **Age of onset:** congenital (unicuspid, severe neonatal AS) presents in infancy; BAV-related AS typically presents in the 4th–6th decades; degenerative tricuspid calcific AS typically presents ≥65–70 years; rheumatic AS presents variably depending on access to acute rheumatic fever treatment/prophylaxis, often 3rd–5th decade in endemic regions.
- **Severity:** graded echocardiographically as mild, moderate, severe (see Diagnostics), with "very severe" (peak velocity ≥5 m/s) increasingly recognized as an especially high-risk substage.
- **Progression:** typically slow and progressive over years (mean jet-velocity progression roughly 0.1–0.3 m/s/year, mean gradient progression ~7 mmHg/year in some series), but rate is highly variable between individuals and can accelerate with worsening calcification burden, CKD, or in bicuspid valves.
- **Frequency of individual signs/symptoms among affected individuals:** the systolic murmur is present in nearly all clinically significant cases; classic triad symptoms occur in a minority of the (large) asymptomatic population at any given time but portend a roughly 1–2%/year sudden-death risk once truly asymptomatic-but-severe, rising sharply once symptoms appear (~25% one-year mortality untreated, see Outcome/Prognosis).

**Quality of life impact:** Symptomatic AS substantially reduces functional capacity (NYHA class progression), exercise tolerance, and overall quality of life; validated general instruments (SF-36, EQ-5D) and disease-specific tools (Kansas City Cardiomyopathy Questionnaire, adapted for valve disease) show marked QoL improvement after successful valve replacement (TAVR or SAVR), a major endpoint in the PARTNER trial family.

**Suggested HPO terms** (verify exact IDs/labels via OAK before KB use): Aortic valve stenosis; Bicuspid aortic valve; Dyspnea; Exertional dyspnea; Syncope; Angina pectoris; Left ventricular hypertrophy; Heart failure; Atrial fibrillation; Sudden cardiac death; Systolic ejection murmur (or "Heart murmur").

---

## 4. Genetic/Molecular Information

**Causal/high-risk genes (congenital/Mendelian forms):**
- ***NOTCH1*** (HGNC:7881; OMIM 190198 gene / 109730 phenotype AOVD1) — autosomal dominant BAV and calcific AS; loss-of-function (haploinsufficient) variants; ~5–10% of non-syndromic familial/sporadic BAV (PMC5573733, PMID:32720365).
- ***ELN*** (elastin) — Williams-Beuren syndrome (contiguous gene deletion, 7q11.23), causing supravalvular aortic stenosis as part of a multisystem elastin-arteriopathy syndrome (OMIM 185500).
- ***FLNA*** (filamin A) — X-linked valvulo-septal defects with myxomatous, sometimes stenotic valve disease.
- ***GATA4, GATA5, SMAD6, ROBO4, MAT2A, NOS3*** and others — additional candidate/lower-penetrance genes reported in BAV cohorts via targeted and exome sequencing (systematic review: MDPI Genes 2024, doi:10.3390/genes15101309).

**Common-variant / polygenic risk loci (degenerative CAVS):**
- ***LPA*** (rs10455872, rs3798220, KIV-2 copy number) — determines Lp(a) level; strongest and causally-supported (Mendelian randomization) common risk locus.
- ***PALMD*** (1p21.2) and ***TEX41*** (2q22.3) — first GWAS-identified non-*LPA* loci (PMID:29511194), both also linked to BAV.
- ***ALPL*** (tissue-nonspecific alkaline phosphatase) — direct biochemical role in phosphate/mineralization biology.
- ***IL6*** — inflammatory pathway.
- ***FADS1*** — lipid/fatty-acid desaturation pathway.
- ***NAV1*** — novel candidate from meta-analysis.
- Additional loci from the Million Veteran Program multi-ancestry GWAS and 2024 integrative genomics study, which nominated tissue-specific candidate causal genes via valve-tissue expression/regulatory data (Nat Commun 2024, doi:10.1038/s41467-024-46639-4).

**Variant classification/frequency resources:** ClinVar and ClinGen classify pathogenicity for NOTCH1/ELN/FLNA variants per ACMG/AMP criteria; gnomAD provides population allele frequencies for common-variant loci (LPA, PALMD, TEX41 alleles are common, MAF often >5–20% depending on ancestry, consistent with polygenic-risk rather than rare fully penetrant Mendelian variance for the bulk of adult degenerative AS).

**Somatic vs. germline:** AS-associated variants are germline; there is no established somatic-mutation driver analogous to clonal hematopoiesis in this disease (though CHIP/clonal hematopoiesis is an active research area for cardiovascular calcification broadly and may be relevant as an emerging modifier — flagged here as an area for further literature confirmation rather than an established causal link specific to AS).

**Functional consequences:** *NOTCH1* variants are predominantly loss-of-function/haploinsufficient, disrupting Notch-mediated repression of osteogenic transcriptional programs in valve interstitial cells (de-repression of RUNX2/osteopontin-driven calcification) as well as impairing endocardial-cushion/valvulogenesis signaling during development — a dual developmental-and-degenerative mechanism (PMC5299165). *LPA*/Lp(a)-raising alleles act through a gain of circulating pro-atherogenic, pro-inflammatory, and oxidized-phospholipid-carrying lipoprotein particle rather than a coding loss/gain of a single protein's enzymatic function.

**Epigenetic information:** DNA methylation differences have been studied in Turner syndrome-associated BAV (PMC9194862) as a candidate modifier explaining incomplete penetrance/phenotypic variability of BAV in monosomy X; broader epigenomic studies of valve tissue (histone marks, chromatin accessibility) in sporadic CAVS are an active but less mature area relative to atherosclerosis epigenomics.

**Chromosomal abnormalities:** Turner syndrome (45,X and mosaic variants) carries markedly elevated BAV prevalence (14–34% across studies, vs. 0.5–2% general population) and consequent elevated AS risk, alongside coarctation of the aorta and aortopathy (meta-analysis, TechScience CHD journal; JACC 2008, PMID:18538181 area). 22q11.2 deletion syndrome and other conotruncal/left-heart developmental syndromes carry increased rates of left-sided obstructive lesions including AS, though BAV/AS is not the dominant cardiac phenotype in 22q11.2DS specifically.

---

## 5. Environmental Information

- **Environmental/toxic factors:** No specific environmental toxin is established as a primary AS cause; chronic low-grade systemic inflammation and oxidative stress (shared with atherosclerosis) are the operative environmental-biological axis. Air-pollution/particulate-matter exposure has been studied as a contributor to vascular calcification broadly and is a plausible but not disease-specific established risk modifier for CAVS.
- **Radiation:** Mediastinal/thoracic radiotherapy (Hodgkin lymphoma, breast, lung cancer treatment) is a well-established, dose- and latency-dependent cause of radiation-associated valvular heart disease, including accelerated aortic valve fibrosis and calcification appearing 10–20+ years post-exposure.
- **Lifestyle factors:** Smoking, sedentary lifestyle contributing to metabolic syndrome/diabetes, and diets promoting dyslipidemia and hyperglycemia (mirroring the diabetogenic/procalcific diet used experimentally in LDLr⁻/⁻ApoB100/100 mice, PMID:29539583) are relevant modifiable contributors, primarily through acceleration of the shared lipid-inflammatory-calcific pathway rather than as independent disease initiators.
- **Infectious agents:** ***Streptococcus pyogenes* (Group A Streptococcus)** is the infectious trigger for acute rheumatic fever, which via post-streptococcal autoimmune cross-reactivity (molecular mimicry between streptococcal M-protein epitopes and cardiac valve tissue) causes rheumatic valvulitis and, over years of recurrent/chronic disease, rheumatic aortic (and mitral) stenosis. This remains the dominant global cause of valvular AS in low-resource settings (RHD affects an estimated ~41 million people worldwide, causing ~1.4 million premature deaths annually, with the highest childhood cardiovascular DALY burden in ages 10–14; PMC7731852). Infective endocarditis can also cause secondary valve destruction/dysfunction but more typically causes regurgitation than pure stenosis.

---

## 6. Mechanism / Pathophysiology

### Causal chain (degenerative calcific AS — the dominant adult mechanism)

1. **Initiating endothelial injury/dysfunction** at sites of high mechanical shear/turbulent flow on the aortic (outflow) side of the leaflet — analogous to early atherogenesis (GO: response to fluid shear stress, GO:0034405).
2. **Lipoprotein infiltration and retention** — LDL and especially Lp(a)-carried oxidized phospholipids (OxPL) accumulate in the subendothelial valve matrix; Lp(a) also delivers autotaxin, which generates lysophosphatidic acid, amplifying local inflammatory/pro-osteogenic signaling.
3. **Chronic inflammatory infiltration** — macrophages, T lymphocytes, and mast cells infiltrate the leaflet; pro-inflammatory cytokines (IL-6, TNF-α, IL-1β) and complement activation sustain a self-perpetuating inflammatory microenvironment (GO: inflammatory response, GO:0006954).
4. **Valve interstitial cell (VIC) activation and osteoblastic transdifferentiation** — resident VICs (normally quiescent fibroblast-like cells) activate into myofibroblasts and subsequently trans-differentiate into osteoblast-like cells expressing RUNX2, alkaline phosphatase (ALPL), osteopontin, and osteocalcin — a genuine ectopic bone-formation-like program (GO: osteoblast differentiation, GO:0001649; GO: bone mineralization, GO:0030282), counterbalanced physiologically by inhibitors such as osteoprotegerin (loss of which accelerates calcification in hypercholesterolemic mouse models, PMC3675204).
5. **Nodular calcification and matrix remodeling** — deposition of calcium-phosphate (hydroxyapatite; CHEBI relevant to calcium phosphate mineral) at leaflet bases progressing toward the free edges, extracellular matrix degradation/remodeling by matrix metalloproteinases, and progressive leaflet stiffening.
6. **Neovascularization and intravalvular microhemorrhage** contribute additional inflammatory and calcific stimulus in more advanced lesions.
7. **Mechanical outflow obstruction** — leaflet stiffening and calcific bulk progressively reduce effective orifice area, imposing chronic pressure overload on the left ventricle.
8. **Compensatory concentric LV hypertrophy** — normalizes wall stress initially (Laplace's law) but over time causes myocardial fibrosis, diastolic dysfunction, reduced coronary flow reserve, and eventually systolic dysfunction/heart failure once compensation fails.
9. **Clinical decompensation** — symptom onset (angina, syncope, dyspnea) signals a marked increase in mortality risk absent intervention.

**Upstream vs. downstream:** Endothelial injury/lipid infiltration and the *LPA*/*NOTCH1*/*PALMD* genetic lesions sit upstream (initiating/predisposing); inflammatory amplification and VIC osteogenic transdifferentiation are the central, self-sustaining mid-pathway "engine" (explaining why upstream lipid-lowering with statins fails once this program is established); mechanical stenosis, LV hypertrophy, and heart failure are downstream consequences.

**Cell types involved:** valve interstitial cells (VICs; fibroblast-like, myofibroblast, osteoblast-like states), valve endothelial cells (VECs), infiltrating macrophages, T lymphocytes, mast cells, and — for the downstream cardiac remodeling arm — cardiomyocytes undergoing hypertrophy and interstitial cardiac fibroblasts. Suggested CL terms (verify exact IDs): "cardiac valve interstitial cell," "cardiac endothelial cell" (CL:1000487 candidate), "macrophage" (CL:0000235), "myofibroblast" (CL:0000186), "osteoblast" (CL:0000062, used here in an ectopic/trans-differentiated sense), "T cell" (CL:0000084), "cardiac muscle cell"/cardiomyocyte (CL:0000746).

### Rheumatic mechanism (distinct pathway)
Group A streptococcal pharyngitis triggers an autoimmune cross-reactive (molecular mimicry) response targeting valvular endothelium and matrix proteins; recurrent/chronic inflammatory valvulitis produces commissural fusion, leaflet thickening/retraction and fibrosis, and secondary calcification — mechanistically an immune-mediated fibrotic process rather than the primarily lipid/osteogenic pathway of degenerative CAVS, though the two can converge on calcification as a final common pathway (dismech's `granuloma_formation`- and `atherogenesis`-adjacent, but non-identical, mechanism logic — a rheumatic AS entry would not `conforms_to` `atherogenesis`).

### Molecular profiling / omics evidence
- **Transcriptomics:** valve-tissue RNA-seq/microarray studies (deposited in GEO) have characterized differential expression of osteogenic (RUNX2, BMP2), inflammatory (IL6, TNF), and matrix-remodeling (MMPs) genes between calcified and normal leaflets, and underpin the tissue-specific regulatory analyses used in recent integrative GWAS follow-up (Nat Commun 2024).
- **Proteomics:** valve and serum proteomic studies have identified osteopontin, osteocalcin, and complement components as enriched in calcified leaflets and, for some markers, in circulation.
- **Genomic structural features:** copy-number variation at the *LPA* KIV-2 domain directly determines Lp(a) particle number/plasma level and thus genetic AS risk — a structural-genomic (not just SNP) contributor.
- **Single-cell/spatial approaches:** emerging single-cell RNA-seq of human calcific valve tissue is beginning to resolve VIC subpopulation heterogeneity (quiescent vs. activated vs. osteogenic states) and immune cell diversity within lesions; this is a rapidly developing area as of 2025–2026 and specific dataset citations should be pulled from GEO/Human Cell Atlas at curation time.
- **Functional genomics:** CRISPR/RNAi screens in valve interstitial cell culture systems have been used to interrogate osteogenic transdifferentiation regulators (e.g., RUNX2 pathway components), though this remains a smaller literature than for atherosclerosis-focused functional genomics (DepMap/BioGRID ORCS coverage of this specific phenotype should be checked directly if curating this level of detail).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** the aortic valve (three leaflets/cusps in the normal tricuspid valve; two in BAV) and, immediately downstream, the left ventricle (concentric hypertrophy, later systolic dysfunction).
- **Secondary/complications:** left atrium (pressure/volume overload contributing to atrial fibrillation), pulmonary vasculature and right heart (pulmonary hypertension, right heart failure in advanced disease), coronary circulation (reduced flow reserve despite often-normal epicardial arteries; concurrent atherosclerotic CAD is also common given shared risk factors), ascending aorta (post-stenotic dilation from turbulent jet, and — especially with BAV — an intrinsic aortopathy with aneurysm risk independent of hemodynamics), and (for BAV) association with aortic coarctation.
- **Body systems:** primarily cardiovascular; secondarily hematologic (acquired von Willebrand syndrome/Heyde syndrome with GI bleeding), and — via reduced cardiac output — renal (cardiorenal interactions) and cerebrovascular (embolic stroke risk from calcific debris or associated atrial fibrillation).

**Tissue and cell level:**
- Valve leaflet fibrosa, spongiosa, and ventricularis layers (trilaminar valve extracellular matrix architecture) undergo disorganization, fibrosis, and calcific nodule formation, predominantly on the fibrosa (aortic/outflow) side.
- Cell populations: valve interstitial cells (activated/osteoblast-like), valve endothelial cells (dysfunctional), infiltrating macrophages/T cells/mast cells, and downstream cardiomyocyte hypertrophy plus interstitial myocardial fibroblast activation (fibrosis) in the left ventricle.

**Subcellular level:** mitochondrial oxidative stress in VICs contributes to osteogenic reprogramming; nuclear transcriptional reprogramming (RUNX2 activation) drives the osteoblast-like phenotype switch; extracellular matrix vesicles (a recognized nucleation site for hydroxyapatite deposition, paralleling bone/vascular calcification biology) are implicated in the mineralization step itself.

**Localization/lateralization:** Not applicable in the sense of unilateral/bilateral — the aortic valve is a single, midline structure — but calcification classically begins focally at leaflet bases near the commissures/hinge points and progresses toward the free margins, with the degree and distribution differing characteristically between tricuspid (more circumferential/central) and bicuspid (often raphe-centered, asymmetric) valve calcification, a distinction used clinically (e.g., in CT calcium scoring thresholds, which differ by sex and valve morphology).

**Suggested UBERON terms:** aortic valve (UBERON:0002137, verify); aortic valve leaflet (UBERON candidate, verify exact ID); left ventricle (UBERON:0002082); left ventricular myocardium; ascending aorta (UBERON:0001496, verify); left atrium (UBERON:0002079).

---

## 8. Temporal Development

**Onset:**
- **Congenital forms** (unicuspid valve, severe neonatal critical AS) present at or shortly after birth, sometimes prenatally on fetal echocardiography.
- **BAV-associated AS** most often becomes clinically significant in the 4th–6th decades of life, decades earlier than tricuspid degenerative AS, due to the additional mechanical stress of an abnormal two-cusp geometry.
- **Degenerative tricuspid calcific AS** is an insidious, chronic process typically becoming hemodynamically severe after age 65–70, with prevalence rising steeply with each further decade of life.
- **Rheumatic AS** onset is more variable, often presenting as clinically significant stenosis in the 3rd–5th decade in endemic, resource-limited regions, reflecting years of recurrent/subclinical rheumatic valvulitis following childhood acute rheumatic fever.

**Progression:**
- **Stages** (echocardiographic, per current ACC/AHA staging framework): Stage A (at risk — e.g., BAV or early sclerosis without stenosis), Stage B (progressive, mild-moderate hemodynamic obstruction), Stage C (asymptomatic severe — C1 normal LV function, C2 LV dysfunction), Stage D (symptomatic severe — D1 high-gradient, D2 low-flow/low-gradient with reduced EF, D3 low-flow/low-gradient with preserved EF/paradoxical low-flow).
- **Progression rate:** generally slow (years), quantifiable as annualized increase in peak velocity/mean gradient and decrease in valve area, but with substantial inter-individual variability; BAV, higher baseline calcium burden, CKD, and elevated Lp(a) are associated with faster progression.
- **Course pattern:** typically unidirectional and progressive (no spontaneous regression of established calcific stenosis); asymptomatic patients can remain stable for years before relatively abrupt symptom onset once critical obstruction is reached, at which point the clinical trajectory changes sharply (a recognized "cliff-edge" prognostic transition, discussed further in Outcome/Prognosis).
- **Duration:** chronic and, once truly severe and symptomatic, rapidly lethal without intervention (median survival on the order of ~2 years untreated after symptom onset, per classical natural-history literature, with more contemporary series estimating ~77% one-year survival in unoperated symptomatic patients, PMC3954323 area).

**Patterns:**
- No spontaneous remission is described for calcific AS (unlike some inflammatory valvulopathies).
- The key "critical period" from a management perspective is the transition from asymptomatic-severe to symptomatic disease — a major focus of intervention-timing guidelines and trials (e.g., debate over early intervention in asymptomatic severe AS, addressed by studies such as PMC8026050 and the JAMA Cardiology meta-analysis, doi:10.1001/jamacardio.2021.5528 area) — because outcomes worsen sharply once symptoms (or LV dysfunction/biomarker elevation) develop.

---

## 9. Inheritance and Population

**Epidemiology:**
- Calcific/degenerative AS: prevalence rises steeply with age, generally cited in the range of a few percent of individuals over 65 and up to ~2–4% (severe AS specifically lower, on the order of 1–3%) in octogenarians in population-based echocardiographic screening cohorts (classic sources: Cardiovascular Health Study, Helsinki Aging Study, Framingham-related analyses — confirm exact contemporary percentages against a current source such as the JACC 2025 state-of-the-art review, doi:10.1016/j.jacc.2025.06.049, at curation time).
- Global Burden of Disease-based estimates place non-rheumatic calcific aortic valve disease burden as rising substantially from 1990 to 2021 with further projected increases to 2050, tracking population aging (medRxiv 2025.02.05.25321722; JAHA 2024, doi:10.1161/JAHA.124.037991).
- Aortic valve stenotic disease overall (all etiologies) is estimated to affect on the order of ~9 million people worldwide, with calcific disease dominant in high-sociodemographic-index (high-SDI) regions and rheumatic disease dominant in low-SDI regions (Nature Reviews Cardiology 2021, doi:10.1038/s41569-021-00570-z).
- Bicuspid aortic valve: population prevalence ~0.9–1.36% by autopsy/screening series (up to ~4.6/1000 live births in a newborn screening cohort), making it the most common congenital heart defect.

**Inheritance pattern (genetic forms):**
- NOTCH1-related AOVD1/BAV: autosomal dominant, with variable/incomplete penetrance and expressivity (some carriers have isolated BAV without stenosis; others develop severe calcific AS or thoracic aortic aneurysm).
- Common-variant polygenic risk (LPA, PALMD, TEX41, ALPL, IL6, FADS1, etc.): complex/multifactorial inheritance — no single-gene Mendelian pattern; risk is cumulative and interacts with age and environmental exposures.
- Williams-Beuren syndrome (ELN, supravalvular AS): autosomal dominant, typically due to a de novo 7q11.23 microdeletion (contiguous gene deletion syndrome), so usually not inherited from a parent but is transmissible at 50% risk if a parent is affected.

**Penetrance/expressivity:** Notably incomplete/variable for NOTCH1 and other BAV-associated genes — family members carrying the same variant may show isolated BAV, BAV with AS, BAV with aortopathy, or apparently normal valve morphology, motivating cascade echocardiographic screening in relatives of BAV probands.

**Genetic anticipation:** Not a recognized feature of AS (not a repeat-expansion disorder).

**Founder effects / consanguinity:** Not prominently described for common degenerative AS; may be locally relevant for specific rare Mendelian valvulopathy variants in genetically isolated populations, but this is not a well-characterized area in the mainstream AS literature.

**Population demographics:**
- **Sex ratio:** BAV shows a strong male predominance (commonly cited 2:1 to 4:1 male:female across studies, with a newborn screening cohort reporting 4:1); however, sex differences in valve *phenotype presentation* exist — men with BAV more often present with aortic regurgitation, while women more often present with aortic stenosis (Circ Cardiovasc Imaging, PMID:28251911). Degenerative calcific AS in the elderly still shows a male predominance in incidence, though the gap narrows somewhat with the oldest age groups, and women may show relatively more fibrotic (versus purely calcific) valve remodeling patterns — an active area of sex-specific pathobiology research.
- **Turner syndrome (45,X):** markedly elevated BAV prevalence (14–34% vs. 0.5–2% general population), making it an important syndromic subgroup for population-level AS risk.
- **Geographic distribution:** rheumatic AS is concentrated in low- and middle-income countries (Sub-Saharan Africa, South Asia, Pacific Islander populations, Indigenous populations in some high-income countries) reflecting limited access to primary prevention (penicillin prophylaxis) and treatment of streptococcal pharyngitis/acute rheumatic fever; calcific AS predominates in aging high-income-country populations.
- **Age distribution:** BAV-related AS peaks in middle age (40s–60s); degenerative tricuspid AS peaks in the elderly (>70–80); rheumatic AS varies by region but often presents younger than degenerative AS in endemic settings.

---

## 10. Diagnostics

**Clinical/imaging tests:**
- **Transthoracic echocardiography (TTE) is the primary diagnostic modality.** Key parameters per current (2020 ACC/AHA and analogous ESC) guidelines: peak aortic jet velocity, mean transvalvular pressure gradient (MPG), and aortic valve area (AVA) by the continuity equation. **Severe AS** is defined by peak velocity ≥4 m/s, MPG ≥40 mmHg, and/or AVA ≤1.0 cm² (or indexed AVA ≤0.6 cm²/m²); "very severe" AS is increasingly recognized at peak velocity ≥5 m/s or ≥5.5 m/s, associated with markedly worse event-free survival (44%, 25%, 11%, 4% at 1–4 years in one cohort, AHA Circulation 2010-era study).
- **Four hemodynamic categories** are defined when flow, gradient, and area are discordant: high-gradient severe AS; low-flow low-gradient AS with reduced LVEF (classical low-flow low-gradient); low-flow low-gradient AS with preserved LVEF (paradoxical low-flow, low-gradient); and normal-flow low-gradient AS with preserved LVEF — reflecting the complexity of grading in the presence of ventricular dysfunction or small ventricular cavities.
- **Dobutamine stress echocardiography** helps distinguish truly severe AS with reduced contractile/flow reserve from pseudo-severe AS in low-flow, low-gradient, reduced-EF states.
- **Cardiac CT with aortic valve calcium (AVC) scoring (Agatston units)** is a class-I-recommended adjunct in ACC/AHA/ESC guidelines specifically to resolve discordant/low-gradient grading, with established sex-specific severity thresholds (men and women have different calcium-score cutoffs for "severe" AS given differing valve calcification propensity).
- **Cardiac MRI** for LV volumes/function, myocardial fibrosis (late gadolinium enhancement, T1 mapping) when echo is inconclusive or for research-grade fibrosis quantification.
- **Cardiac catheterization** (invasive hemodynamic gradient measurement) reserved for cases of echo-catheterization discordance or when non-invasive data are inconclusive; coronary angiography (or coronary CTA) is routinely performed pre-intervention to assess concomitant CAD.
- **Biomarkers:** BNP/NT-proBNP elevation supports symptomatic status/prognostic risk stratification and can help trigger earlier intervention in asymptomatic patients per guideline-endorsed thresholds.
- **Electrocardiography:** may show LV hypertrophy pattern, left atrial abnormality, conduction disease (especially relevant peri-TAVR given proximity of the conduction system to the aortic annulus).
- **Histopathology (surgical/explanted valve specimens):** shows fibrosis, dystrophic/nodular calcification predominantly on the aortic surface of the fibrosa layer, chronic inflammatory infiltrate, and neovascularization in advanced disease; rheumatic valves additionally show commissural fusion and characteristic fibrous thickening/retraction distinct from purely nodular calcific deposits.

**Genetic testing:** Not routine for typical sporadic degenerative or BAV-related AS, but recommended in the context of: familial clustering of BAV/thoracic aortic disease (first-degree relative screening echocardiography is guideline-recommended regardless of genetic testing; targeted gene panels including *NOTCH1*, *ACTA2*, *TGFBR1/2*, *FBN1*, *SMAD3* etc. are used when a syndromic thoracic aortic aneurysm/BAV phenotype is suspected); suspected Williams-Beuren syndrome (chromosomal microarray/FISH for 7q11.23 deletion) in supravalvular AS; suspected homozygous familial hypercholesterolemia (LDLR/APOB/PCSK9 sequencing) in children/young adults with premature valvular/supravalvular calcific disease.

**Clinical/differential diagnosis:** Hypertrophic obstructive cardiomyopathy (dynamic subaortic/midcavitary obstruction, distinguished by echo features and provocative maneuvers), subvalvular/supravalvular aortic stenosis (fixed obstruction at a different anatomic level than the valve itself, important to distinguish since management differs — e.g., surgical membrane resection rather than valve replacement for discrete subvalvular membranes), aortic sclerosis (valve thickening/calcification without significant hemodynamic obstruction — the earliest point on the same disease continuum), and flow murmurs of other causes (anemia, hyperthyroidism, physiologic in young/athletic individuals) that can mimic the systolic ejection murmur without true stenosis.

**Screening:** No population-based screening program exists for degenerative AS given its age-related, largely non-preventable natural history; targeted echocardiographic screening is recommended for first-degree relatives of BAV/thoracic aortic aneurysm probands given the substantial heritable component, and for individuals with Turner syndrome given the markedly elevated BAV prevalence in that population.

---

## 11. Outcome/Prognosis

**Survival/mortality:**
- **Asymptomatic severe AS under watchful waiting:** roughly 44% experience death or require valve replacement by 2 years in some cohorts; one comparative analysis found 1-year mortality of 5.2% (watchful waiting) vs. 4.7% (early surgery), and 2-year survival of 83.9% vs. 92.5% respectively, favoring earlier intervention in appropriately selected patients (Annals of Thoracic Surgery, PMID area referenced above).
- **"Very severe" AS** (peak velocity ≥5.5 m/s): event-free survival of only 44%, 25%, 11%, and 4% at 1, 2, 3, and 4 years respectively if managed conservatively — among the strongest natural-history prognostic signals in cardiology (Circulation, PMID:20026779 area).
- **Symptomatic, unoperated severe AS:** classically associated with a median survival around 2–3 years from symptom onset (angina ~5 years, syncope ~3 years, heart failure ~1–2 years, per the long-standing Ross-Braunwald natural-history framework); more recent series report ~77% one-year survival in unoperated symptomatic patients — still a markedly poor prognosis relative to treated disease.
- **Sudden cardiac death** is a recognized risk in truly asymptomatic-but-severe AS (historically estimated around 1%/year), a key argument for evolving early-intervention strategies and biomarker/imaging-based risk stratification (JAMA Cardiology systematic review/meta-analysis on early intervention vs. watchful waiting in asymptomatic severe AS).

**Post-intervention outcomes (TAVR/SAVR):**
- **High surgical risk (PARTNER 1):** 5-year mortality similar between TAVR (67.8%) and SAVR (62.4%), HR 1.04 (95% CI 0.86–1.24), demonstrating durable comparable outcomes in this population (Lancet 2015, PMID:25788234).
- **Intermediate risk (PARTNER 2):** 24-month mortality 16.7% (TAVR) vs. 18.0% (SAVR) — non-inferior/comparable (NEJM 2016, PMID:27040324 area).
- **Low risk (PARTNER 3):** TAVR superior to SAVR for the composite of death/stroke/rehospitalization at 1 year; by 7-year follow-up, TAVR and surgery show similar durability and valve function (NEJM 2025 7-year report, doi:10.1056/NEJMoa2509766) — a major, still-evolving evidence base extending TAVR's applicability across the full surgical-risk spectrum.

**Morbidity/complications:** heart failure, atrial fibrillation, stroke (both disease-related embolism and periprocedural), conduction system disease/need for permanent pacemaker (particularly post-TAVR, given proximity of the conduction system to the valve annulus), acquired von Willebrand syndrome with GI bleeding (Heyde syndrome, which characteristically resolves after valve replacement), and, for rheumatic disease, concomitant mitral valve disease compounding overall morbidity.

**Quality of life:** substantially improved after successful intervention (TAVR/SAVR), a primary endpoint across the PARTNER trial family and reflected in validated instruments (KCCQ, SF-36, EQ-5D).

**Prognostic factors/biomarkers:** symptom status (single strongest classical prognostic determinant), peak jet velocity/mean gradient severity ("very severe" category especially high-risk), LV ejection fraction and presence of low-flow states, degree of valve calcification (AVC score), elevated BNP/NT-proBNP, global longitudinal strain abnormalities (subclinical LV dysfunction), concomitant coronary artery disease, frailty and comorbidity burden (central to surgical/TAVR risk-scoring and candidacy decisions), and elevated Lp(a) (associated with both incident risk and, in some studies, faster hemodynamic progression).

---

## 12. Treatment

**No effective pharmacotherapy modifies the natural history of the valvular lesion itself.** Definitive treatment is mechanical relief of obstruction; medical therapy addresses risk-factor modification, symptom/heart-failure management, and comorbidities.

**Pharmacotherapy (adjunctive/comorbidity management, not disease-modifying for the valve):**
- Standard heart failure and hypertension management (with caution regarding preload/afterload-sensitive agents in severe AS) once symptomatic or LV dysfunction present.
- Statins/lipid-lowering: NOT disease-modifying for AS progression despite benefit for atherosclerotic risk reduction generally (SALTIRE, SEAS, ASTRONOMER — see Etiology/Protective Factors above); still indicated per standard cardiovascular risk criteria, just not "for" the valve disease itself.
- Emerging investigational Lp(a)-lowering agents (e.g., pelacarsen, an antisense oligonucleotide, and lepodisiran, an siRNA) are in active clinical development primarily for atherosclerotic cardiovascular disease, with dedicated hypotheses/trials examining whether Lp(a) lowering can slow AS progression given the strong causal genetic evidence for Lp(a) in AS — specific trial identifiers, phase, and results should be confirmed against ClinicalTrials.gov/recent primary literature at curation time, as this is a fast-moving area.
- Rheumatic AS: secondary antibiotic prophylaxis (penicillin) to prevent recurrent rheumatic fever/valvulitis is a cornerstone of preventing disease progression in that specific etiology (distinct from the calcific-disease pharmacology discussion above).

**Surgical and interventional (definitive therapy):**
- **Surgical aortic valve replacement (SAVR):** long-standing gold-standard, using mechanical or bioprosthetic valves, with established durability data.
- **Transcatheter aortic valve replacement/implantation (TAVR/TAVI):** catheter-based valve replacement, now guideline-supported across the low-to-high surgical risk spectrum based on the PARTNER trial program (PARTNER 1 high-risk PMID:25788234; PARTNER 2 intermediate-risk NEJM 2016; PARTNER 3 low-risk, 1-year superiority and 7-year comparable durability, NEJM 2019/2025) and parallel CoreValve/Evolut trial programs. TAVR has become the dominant intervention modality for symptomatic severe AS given its less invasive nature, with ongoing evidence generation on long-term (>10 year) valve durability, particularly relevant as TAVR is used in younger, lower-risk patients.
- **Balloon aortic valvuloplasty:** a temporizing (not curative) procedure, used as a bridge to definitive TAVR/SAVR in hemodynamically unstable patients or those needing urgent noncardiac surgery, or in the pediatric/young congenital AS population where valve growth potential argues against prosthetic replacement.
- Ross procedure (pulmonary autograft) — an option in select younger patients, particularly in congenital/pediatric AS, avoiding lifelong anticoagulation and allowing growth.

**Rehabilitative/supportive care:** cardiac rehabilitation post-intervention; standard heart-failure supportive management for those not undergoing intervention or awaiting it; endocarditis-prophylaxis counseling for prosthetic valve recipients per current guidelines.

**Experimental/investigational:** Lp(a)-lowering agents as above; osteoprotegerin/RANKL-pathway-targeted approaches remain preclinical (mouse model rationale from PMC3675204) rather than in clinical trials for AS specifically; anti-inflammatory strategies analogous to those tested in atherosclerosis (e.g., canakinumab-class IL-1β inhibition) are of mechanistic interest given the IL6 GWAS signal but are not established AS therapies.

**Treatment outcomes:** As detailed under Prognosis — TAVR and SAVR produce comparable survival across risk strata in randomized trials, with TAVR showing an early advantage in low-risk patients for the composite endpoint at 1 year and comparable long-term valve durability out to 7 years.

**Personalized/precision approaches:** risk-stratified selection between TAVR and SAVR based on surgical risk scores (STS-PROM, EuroSCORE II), frailty assessment, valve/annulus anatomy (including bicuspid-specific anatomic considerations that affect TAVR device selection and outcomes), and access-site/vascular anatomy; genotype-informed risk assessment (e.g., elevated Lp(a) or known familial NOTCH1 BAV) is increasingly used to guide surveillance intensity and cascade family screening rather than to select a specific drug therapy at present.

**Suggested NCIT terms:** Surgical Procedure (NCIT:C15329); Transcatheter Aortic Valve Replacement (confirm exact NCIT ID, candidate NCIT:C80324); Pharmacotherapy (NCIT:C15986); Organ/Valve Transplantation-adjacent procedure codes as applicable; Balloon Valvuloplasty (confirm NCIT ID); Cardiac Rehabilitation (NCIT candidate, confirm).

---

## 13. Prevention

- **Primary prevention:** Modifiable-risk-factor control (blood pressure, LDL-cholesterol per general cardiovascular risk guidelines, smoking cessation, diabetes/metabolic-syndrome management) reduces atherosclerotic cardiovascular risk broadly but has **not** been shown to prevent the specific development of calcific AS, given the negative statin trials described above — this is an important, somewhat counterintuitive point distinguishing AS from coronary disease prevention. For rheumatic AS specifically, **primary prevention of acute rheumatic fever** via prompt antibiotic treatment of streptococcal pharyngitis is genuinely effective and central to reducing global RHD-attributable AS incidence, particularly in low-resource, high-incidence settings.
- **Secondary prevention:** Secondary antibiotic (penicillin) prophylaxis after acute rheumatic fever prevents recurrent valvulitis and thus limits progression to (or worsening of) rheumatic aortic/mitral stenosis — a well-established, guideline-endorsed intervention. For calcific AS, "secondary prevention" in practice means surveillance echocardiography at guideline-recommended intervals (frequency scaled to severity stage) to detect progression to severe/symptomatic disease at the optimal point for intervention, since no medical therapy prevents progression once the process has begun.
- **Tertiary prevention:** Timely valve replacement (TAVR/SAVR) prevents the downstream complications of untreated severe symptomatic AS (heart failure, sudden death); post-intervention care (endocarditis prophylaxis for prosthetic valves, anticoagulation management for mechanical valves, periodic prosthetic valve surveillance) prevents intervention-related complications.
- **Screening/early detection:** targeted (not population-wide) echocardiographic screening of first-degree relatives of BAV/thoracic-aortopathy probands and of individuals with Turner syndrome, given markedly elevated baseline risk in these groups; risk stratification using AVC scoring and biomarkers (BNP/NT-proBNP) to identify asymptomatic patients who may benefit from earlier intervention.
- **Genetic counseling:** relevant for families with NOTCH1-associated autosomal dominant BAV/AOVD1, Williams-Beuren syndrome (recurrence risk essentially that of a de novo microdeletion, low for future pregnancies unless germline mosaicism), and homozygous familial hypercholesterolemia (autosomal codominant, with defined recurrence risk counseling for LDLR/APOB/PCSK9 pathogenic variants).
- **Public health interventions:** for rheumatic AS, public-health-level investment in access to primary care/antibiotics for streptococcal pharyngitis, improved living conditions (reducing overcrowding-driven GAS transmission), and RHD control programs (echocardiographic screening programs for latent RHD in endemic regions, WHO-endorsed) represent the most effective population-level prevention strategy for this etiology globally.
- **Prophylaxis:** infective endocarditis antibiotic prophylaxis is recommended for patients with prosthetic aortic valves (and select other high-risk categories) undergoing specified dental/procedural exposures, per current AHA/ESC guidelines.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** naturally occurring aortic/subaortic valvular stenosis is well described in domestic dogs (NCBITaxon:9615, *Canis lupus familiaris*), particularly as **subvalvular aortic stenosis (SAS)**, a congenital fixed left ventricular outflow tract obstruction with strong breed predisposition.
- **Breed:** Newfoundlands, Golden Retrievers, Rottweilers, Boxers, and German Shepherd Dogs are classically over-represented for canine subvalvular/aortic stenosis (breed-specific Vertebrate Breed Ontology/VBO identifiers should be confirmed at curation time; this is a well-established heritable condition in Newfoundlands specifically, with published pedigree/heritability analyses).
- **Gene:** the specific causal genetic variant(s) for canine SAS are less definitively characterized than the human NOTCH1/LPA loci, though it is recognized as heritable with a complex/polygenic inheritance pattern in most studied breeds; orthology to human developmental valve genes (e.g., NOTCH1 pathway members) is biologically plausible but not established as the confirmed canine mechanism in the literature reviewed here — flag for targeted OMIA/veterinary literature confirmation if curating this comparative angle in detail.
- **Natural disease and veterinary relevance:** canine SAS is one of the most common congenital cardiac defects in dogs and a significant cause of exercise intolerance, syncope, and sudden cardiac death in affected large-breed dogs, giving it substantial veterinary clinical importance and making affected dogs a naturally-occurring (rather than experimentally induced) comparative model.
- **Comparative pathology:** the fixed left ventricular outflow obstruction, compensatory LV hypertrophy, and risk of sudden death parallel human congenital/valvular AS pathophysiology, though the anatomic level (frequently subvalvular fibrous ridge/membrane in dogs) and degenerative-calcific biology differ from adult human calcific AS — better viewed as a comparative model for congenital/subvalvular obstruction than for the lipid-driven calcific pathway.
- **Transmission/zoonotic potential:** not applicable — this is a non-infectious structural cardiac disease in the calcific/congenital forms; note that the *infectious trigger* for rheumatic AS (Group A Streptococcus) is itself a human-adapted pathogen without a natural zoonotic reservoir relevant to this disease pathway.

---

## 15. Model Organisms

**Genetically engineered and diet-induced mouse models** (the dominant experimental system for calcific AS mechanism research):
- ***Ldlr⁻/⁻* mice:** develop aortic/vascular calcification with a distribution paralleling human disease; used with micro-CT quantification as a model for aortic calcification generally (PMID:22051553).
- ***Ldlr⁻/⁻ApoB100/100* mice:** hypercholesterolemic model prone to aortic **valve** calcification and oxidative stress with functional valvular disease mimicking the clinical syndrome; a customized diabetogenic/procalcific diet further accelerates calcification, hyperglycemia, and obesity in this model, directly modeling gene(lipid handling)×diet(metabolic syndrome) interaction (PMID:29539583).
- ***Notch1⁺/⁻* heterozygous mice (on high-cholesterol diet):** an established small-animal model of calcific aortic valve disease reflecting the human NOTCH1-haploinsufficiency mechanism; used, for example, to test genetic ablation of serotonin receptor 2B (Htr2b), which improved aortic valve hemodynamics in this model (PMC7688160), illustrating the model's utility for testing candidate modifier genes/pathways.
- **Aged hypercholesterolemic mice** (without additional genetic valve-specific lesions): develop calcific AS with aging plus hypercholesterolemic diet, supporting age as an independent, non-genetic experimental variable (PMID:17075015).
- **Hypercholesterolemic/hypertensive combined mouse models:** develop a more fibrotic (versus purely calcific) valve stenosis phenotype, useful for modeling the fibrotic component of human CAVD and potentially for sex- or subtype-specific human disease correlates (PMC4767592).
- **Osteoprotegerin (*Opg*) pathway models:** OPG administration/genetic manipulation in hypercholesterolemic mice modulates valve calcification and preserves valve function, supporting OPG/RANK/RANKL as a therapeutic target axis (PMC3675204).

**Model characteristics:**
- **Phenotype recapitulation:** these models reproduce key histopathologic features (lipid deposition, macrophage infiltration, osteogenic marker expression, calcific nodule formation) and, in several models, measurable hemodynamic valve dysfunction (reduced valve area, increased velocity by echocardiography), giving reasonable face validity for the initiation/inflammatory/early-osteogenic phases of human disease.
- **Model limitations:** mice do not naturally develop the degree of leaflet macro-calcification and hemodynamically severe stenosis seen in elderly humans without genetic/dietary manipulation and prolonged time courses; the mouse valve is anatomically smaller and structurally distinct; models largely capture the LDL/cholesterol-driven and Notch-pathway-driven arms but less fully recapitulate the Lp(a)-driven arm (mice do not naturally express an LPA-orthologous gene generating human-like Lp(a) particles, a recognized cross-species translational gap given how central Lp(a) is to human genetic risk — a candidate `HUMAN_MODEL_MISMATCH`-type caveat if this disease were curated into a mechanism module framework); rheumatic-etiology AS has no direct standard rodent model given its human-adapted streptococcal/autoimmune basis.
- **Research applications:** these models are used to dissect the initiating lipid/inflammatory phase, test candidate therapeutic targets (OPG/RANKL, serotonin receptor 2B, and others) before human trials, and to generate mechanistic hypotheses for pathways (e.g., IL6, ALPL) subsequently supported by human GWAS.
- **Resources:** Mouse Genome Informatics (MGI) for strain/allele records (e.g., *Ldlr* and *Notch1* alleles), International Mouse Phenotyping Consortium (IMPC) for systematic knockout phenotyping data potentially relevant to candidate valve-calcification genes, and GEO for deposited transcriptomic datasets from these valve-calcification mouse models.

---

## Summary for Knowledge-Base Curation

This disease is best modeled with **at least two distinct etiologic pathophysiology chains** given its heterogeneous causation: (1) a degenerative/calcific chain (endothelial injury → lipid/Lp(a) infiltration → chronic inflammation → VIC osteoblastic transdifferentiation → nodular calcification → mechanical obstruction → LV hypertrophy/heart failure), strongly analogous to — but mechanistically distinct from — the dismech `atherogenesis` module, and a plausible candidate for its own dedicated "calcific valvulopathy" mechanism module given its recurrence pattern (it would also be a strong candidate to `conforms_to` a future `cardiomyopathy_maladaptive_remodeling` node for the downstream LV-hypertrophy-to-heart-failure arm); and (2) a rheumatic/autoimmune chain (GAS pharyngitis → molecular mimicry autoimmune valvulitis → commissural fusion/fibrosis → stenosis), which is mechanistically distinct and should not be conflated with the calcific pathway in a single pathophysiology chain. Congenital/BAV forms sit partly upstream of the calcific chain (as an "at-risk" structural predisposition, Stage A in the ACC/AHA framework) rather than being a wholly separate mechanism. The strongest, most rigorously evidenced single risk factor for curation priority is the *LPA*/Lp(a) axis (Mendelian-randomization-supported causality); *NOTCH1* is the best-evidenced Mendelian congenital driver; and the negative statin trial evidence (SALTIRE/SEAS/ASTRONOMER) is an important, well-documented "expected but disconfirmed" treatment hypothesis worth explicitly capturing as a `mechanistic_hypotheses`/discussion entry rather than omitting.

---

### Sources

- [Calcific Aortic Valve Stenosis and Atherosclerotic Calcification - PubMed (PMID:31912380)](https://pubmed.ncbi.nlm.nih.gov/31912380/)
- [Aortic Valve Stenosis: From Basic Mechanisms to Novel Therapeutic Targets - PubMed (PMID:32160774)](https://pubmed.ncbi.nlm.nih.gov/32160774/)
- [The Pathophysiologic Basis and Management of Calcific Aortic Valve Stenosis: JACC State-of-the-Art Review](https://www.jacc.org/doi/10.1016/j.jacc.2025.06.049)
- [The Haemodynamic and Pathophysiological Mechanisms of Calcific Aortic Valve Disease (PMC9220142)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9220142/)
- [Calcific Aortic Stenosis—A Review on Acquired Mechanisms of the Disease and Treatments (PMC8486019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8486019/)
- [Lipoprotein(a) Gene Polymorphism Increases a Risk Factor for Aortic Valve Calcification (PMC6787733)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6787733/)
- [Elevated Lipoprotein(a) and Risk of Aortic Valve Stenosis in the General Population - JACC](https://www.jacc.org/doi/10.1016/j.jacc.2013.09.038)
- [Observational and Genetic Associations of Modifiable Risk Factors with Aortic Valve Stenosis (PMC9182826)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9182826/)
- [Lipoprotein(a) as a Causal Risk Factor for Cardiovascular Disease (PMC11836235)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11836235/)
- [Lipoprotein(a) as a Potential Predictive Factor for Earlier Aortic Valve Replacement in Bicuspid Aortic Valve (PMC10376971)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10376971/)
- [Entry - #109730 - AORTIC VALVE DISEASE 1; AOVD1 - OMIM](https://omim.org/entry/109730)
- [Genetic Bases of Bicuspid Aortic Valve (PMC5573733)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5573733/)
- [Novel loss of function mutation in NOTCH1 in a family with BAV, VSD, TAA, and AS - PubMed (PMID:32720365)](https://pubmed.ncbi.nlm.nih.gov/32720365/)
- [NOTCH1 Mutations in Aortic Stenosis: Association with Osteoprotegerin/RANK/RANKL (PMC5299165)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5299165/)
- [5-year outcomes of TAVR or SAVR for high surgical risk patients (PARTNER 1) - PubMed (PMID:25788234)](https://pubmed.ncbi.nlm.nih.gov/25788234/)
- [Surgical or Transcatheter Aortic-Valve Replacement in Intermediate-Risk Patients - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1700456)
- [Transcatheter or Surgical Aortic-Valve Replacement in Low-Risk Patients at 7 Years - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2509766)
- [Transcatheter versus Surgical Aortic-Valve Replacement in High-Risk Patients - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1103510)
- [Confirmation of Aortic Stenosis Severity in Case of Discordance Between AVA and Gradient - JACC Case Reports](https://www.jacc.org/doi/10.1016/j.jaccas.2021.11.009)
- [Aortic valve stenosis: evaluation and management of discordant grading - ESC](https://www.escardio.org/communities/councils/cardiology-practice/scientific-documents-and-publications/ejournal/volume-15/Aortic-valve-stenosis-evaluation-and-management-of-patients-with-discordant-grading/)
- [Sex Differences in Phenotypes of Bicuspid Aortic Valve and Aortopathy - Circ Cardiovasc Imaging (PMID:28251911)](https://pubmed.ncbi.nlm.nih.gov/28251911/)
- [Sex differences in bicuspid aortic valve disease - PubMed (PMID:32599025)](https://pubmed.ncbi.nlm.nih.gov/32599025/)
- [Outcomes in asymptomatic, severe aortic stenosis (PMC8026050)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8026050/)
- [Natural History of Very Severe Aortic Stenosis - Circulation](https://www.ahajournals.org/doi/10.1161/circulationaha.109.894170)
- [Unoperated severe aortic stenosis: decision making in an adult UK-based population (PMC3954323)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3954323/)
- [Natural History of Asymptomatic Severe Aortic Stenosis and Early Intervention - JAMA Cardiology](https://jamanetwork.com/journals/jamacardiology/fullarticle/2768167)
- [A Randomized Trial of Intensive Lipid-Lowering Therapy in Calcific Aortic Stenosis (SEAS) - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa043876)
- [Atorvastatin therapy is not associated with slowing progression of aortic stenosis - PubMed (PMID:23724618)](https://pubmed.ncbi.nlm.nih.gov/23724618/)
- [Global, Regional, and National Burden of Valvular Heart Disease, 1990 to 2021 - JAHA](https://www.ahajournals.org/doi/10.1161/JAHA.124.037991)
- [Global epidemiology of valvular heart disease - Nature Reviews Cardiology](https://www.nature.com/articles/s41569-021-00570-z)
- [The Global Burden of Rheumatic Heart Disease (PMC7731852)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7731852/)
- [The LDLR deficient mouse as a model for aortic calcification - PubMed (PMID:22051553)](https://pubmed.ncbi.nlm.nih.gov/22051553/)
- [Increased Calcific Aortic Valve Disease in response to a diabetogenic, procalcific diet in LDLr-/-ApoB100/100 mice - PubMed (PMID:29539583)](https://pubmed.ncbi.nlm.nih.gov/29539583/)
- [Genetic ablation of serotonin receptor 2B improves aortic valve hemodynamics of Notch1 heterozygous mice (PMC7688160)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7688160/)
- [Calcific aortic valve stenosis in old hypercholesterolemic mice - PubMed (PMID:17075015)](https://pubmed.ncbi.nlm.nih.gov/17075015/)
- [Fibrotic Aortic Valve Stenosis in Hypercholesterolemic/Hypertensive Mice (PMC4767592)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4767592/)
- [Osteoprotegerin Inhibits Aortic Valve Calcification in Hypercholesterolemic Mice (PMC3675204)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3675204/)
- [Genome-wide analysis yields new loci associating with aortic valve stenosis - PubMed (PMID:29511194)](https://pubmed.ncbi.nlm.nih.gov/29511194/)
- [Multiancestry Genome-Wide Association Study of Aortic Stenosis in the Million Veteran Program - Circulation](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.122.061451)
- [Integrative genomic analyses identify candidate causal genes for calcific aortic valve stenosis - Nature Communications](https://www.nature.com/articles/s41467-024-46639-4)
- [Genetics of Calcific Aortic Stenosis: A Systematic Review - MDPI Genes](https://www.mdpi.com/2073-4425/15/10/1309)
- [Prevalence of Bicuspid Aortic Valve in Turner Syndrome Patients Receiving Cardiac MRI and CT: A Meta-Analysis](https://www.techscience.com/chd/v17n2/46678)
- [DNA Methylation Analysis of Turner Syndrome BAV (PMC9194862)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9194862/)
- [Aortic Valve Disease in Turner Syndrome - JACC](https://www.jacc.org/doi/abs/10.1016/j.jacc.2008.02.035)