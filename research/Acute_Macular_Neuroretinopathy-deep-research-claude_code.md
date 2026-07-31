---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-17T09:41:28.259924'
end_time: '2026-07-17T09:44:46.346424'
duration_seconds: 198.09
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Macular Neuroretinopathy
  mondo_id: ''
  category: ''
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: C:/Users/flaharty/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/bin/claude.exe
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    working_dir: C:/Users/flaharty/AppData/Local/Temp/claude/C--Users-flaharty-Desktop-VSCode/f7c7fd62-c958-42c1-b32e-24e5587d6fa0/scratchpad
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 16
  total_cost_usd: 0.8520285999999999
  session_id: 21cb34c0-8694-411a-ac56-1dc7d0dedd52
  stop_reason: end_turn
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Macular Neuroretinopathy
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Acute Macular Neuroretinopathy** covering all of the
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

# Acute Macular Neuroretinopathy (AMN) — Comprehensive Disease Research Report

## 1. Disease Information

**Overview:** Acute macular neuroretinopathy (AMN) is a rare, acquired retinal disorder characterized by acute-onset paracentral scotomas accompanied by distinctive reddish-brown, wedge-shaped ("petaloid" or teardrop-configured) lesions in the macula, with apices pointing toward the fovea. It was first described by Bos and Deutman in 1975. It is now understood as a disorder of the outer retina caused by ischemia affecting the deep capillary plexus (DCP) and/or choriocapillaris (Orphanet ORPHA:488239; PMID: 26973287).

**Key identifiers:**
- **Orphanet:** ORPHA:488239
- **MONDO:** Indexed in MONDO Disease Ontology (referenced via NORD/MONDO partnership; specific MONDO ID not independently confirmed in available sources — verify against current MONDO release)
- **ICD-10-CM:** H35.89 (Other specified retinal disorders) is the most commonly cited code; some sources list it under H35.3 (Degeneration of macula and posterior pole) — coding conventions vary by institution
- **OMIM:** No dedicated OMIM entry identified; AMN is not classified as a monogenic/Mendelian disorder
- **MeSH:** Retinal Diseases (broader term); no AMN-specific MeSH descriptor identified in search
- **Suggested MONDO/HPO cross-reference terms below**

**Synonyms:** AMN; acute macular neuroretinopathy of Bos and Deutman; "type 2 AMN" is sometimes used loosely for a related but distinct entity (paracentral acute middle maculopathy, PAMM) — see Section 6/8 for the AMN/PAMM spectrum debate.

**Evidence base:** Information is derived predominantly from **aggregated case series, case reports, and one major systematic literature review** (Bhavsar et al., Surv Ophthalmol 2016;61(5):538-65, PMID: 26973287, pooling 156 eyes from 101 published cases), rather than large-scale registries or EHR-based cohort studies. No disease registry or biobank specific to AMN was identified. A retrospective single-center study also reported an increase in visits coded for AMN during the COVID-19 pandemic (0.66/100,000 visits in 2019 to 8.97/100,000 in 2020), suggesting some administrative/EHR-level data exists but is not aggregated into a public registry.

Sources:
- [Orphanet: Acute macular neuroretinopathy](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=488239&lng=EN)
- [Acute macular neuroretinopathy: A comprehensive review of the literature - PubMed (PMID 26973287)](https://pubmed.ncbi.nlm.nih.gov/26973287/)
- [NORD/MONDO: acute macular neuroretinopathy](https://rarediseases.org/mondo-disease/acute-macular-neuroretinopathy/)
- [ICD10Data H35.89](https://www.icd10data.com/ICD10CM/Codes/H00-H59/H30-H36/H35-/H35.89)

---

## 2. Etiology

**Disease causal factors:** AMN is understood as a **primarily mechanistic/vascular disorder** — microvascular ischemia of the retinal deep capillary plexus and/or inner choroid/choriocapillaris — rather than a genetic or single-infectious-agent disease. It is best conceptualized as a final common pathway triggered by diverse systemic insults that transiently compromise perfusion to the outer retina.

**Risk factors (environmental/clinical — no confirmed genetic risk loci identified in literature searched):**
- Preceding **viral or flu-like illness** (influenza, dengue, SARS-CoV-2, other febrile illnesses)
- **Oral contraceptive pill use**
- **Vaccination** (including COVID-19 mRNA and adenoviral vector vaccines — multiple case reports)
- **Sympathomimetic/vasoactive drug exposure**: intravenous epinephrine, ephedrine
- **Hypovolemia, systemic shock, hypotension**
- **Pregnancy**
- **Excessive caffeine intake**
- **Trauma** (including head injury; associated with Purtscher retinopathy)
- **Intravenous contrast administration**
- **Migraine history**
- **Prothrombotic states**, including antiphospholipid antibodies
- **Demographics as risk modifiers**: young age, female sex, non-Latino white race are overrepresented in case series (see Section 9)

**Protective factors:** No genetic or environmental protective factors have been identified or studied in the literature; this is consistent with AMN's classification as an acquired, trigger-driven microvascular event rather than a disease with defined susceptibility/resistance alleles.

**Gene-environment interactions:** Not established. No GWAS, CTD, or PheGenI data specific to AMN were found. The described "risk factors" are exclusively environmental/physiological triggers layered onto a presumed baseline vascular vulnerability of the deep capillary plexus/choriocapillaris (a watershed, low-flow vascular bed), rather than documented gene × environment interactions.

Sources:
- [Acute macular neuroretinopathy: A comprehensive review — PubMed](https://pubmed.ncbi.nlm.nih.gov/26973287/)
- [Multimodal imaging of type 2 AMN in a young woman — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8668169/)
- [Acute macular neuroretinopathy in dengue virus serotype 1 — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8760433/)
- [Bilateral AMN after Oxford-AstraZeneca COVID-19 vaccine — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8769920/)

---

## 3. Phenotypes

| Phenotype | Type | Onset/Course | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Paracentral scotoma | Symptom/sign | Acute onset, often persists indefinitely (may partially resolve over months) | Common/near-universal presenting feature | HP:0000575 (Scotoma) — consider HP:0000618 (Blindness) as too severe; scotoma is the best fit |
| Sudden decreased visual acuity / blurred vision | Symptom | Acute, days after febrile illness or trigger | Very common | HP:0000572 (Visual impairment) / HP:0007663 (Reduced visual acuity) |
| Reddish-brown wedge-shaped (petaloid) macular lesion | Clinical sign (fundoscopic) | Present at onset, may fade over weeks–months, can become subtle/occult | Characteristic but not always grossly visible (some "occult AMN" cases) | HP:0007689 (Macular degeneration) — no precise HPO term exists for petaloid lesion morphology; consider free-text annotation |
| Hyperreflective band at OPL/ONL junction on OCT | Imaging/laboratory-type finding | Acute; evolves to outer retinal thinning/atrophy | Near-universal on OCT | Not an HPO clinical term — imaging biomarker |
| Ellipsoid zone (IS/OS) disruption | Imaging finding | Acute, may persist as chronic disruption | Common | Imaging biomarker (no direct HPO term) |
| Hyporeflectivity on near-infrared reflectance imaging | Imaging finding | Acute–subacute | Highly sensitive/characteristic | Imaging biomarker |
| Photopsias | Symptom | Prodromal/acute | Reported in subset | HP:0000704 (Photopsia) — verify exact HPO code |
| Metamorphopsia | Symptom | Acute–subacute | Reported in subset | HP:0012029 (approx.; verify) |

**Onset/severity/progression:** Onset is acute (days), typically following a systemic trigger by 1–7 days (e.g., mean 2.8 ± 2.5 days post-COVID-19 PCR positivity in one series). Severity is variable — visual acuity is "often only mildly affected" since lesions are typically paracentral rather than foveal, but permanent paracentral scotomas are common even when acuity recovers well. Course is typically **stable-to-slowly-improving**: lesions and associated OCT/IR changes evolve over weeks to months, with scotomas persisting indefinitely in many patients even as visual acuity improves. Bilateral involvement occurs in ~54% of cases (Bhavsar et al. review of 156 eyes/101 cases).

**Quality of life impact:** Persistent paracentral scotomas can impair reading and fine visual tasks despite preserved central acuity; no formal EQ-5D/SF-36 disease-specific QOL data were identified in the literature searched.

Sources:
- [Acute macular neuroretinopathy: A comprehensive review — PubMed](https://pubmed.ncbi.nlm.nih.gov/26973287/)
- [Occult Acute Macular Neuroretinopathy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762149/)
- [The characteristics of AMN following COVID-19 infection — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10782751/)

---

## 4. Genetic/Molecular Information

**Not applicable / not established.** AMN has **no known causal genes, pathogenic variants, chromosomal abnormalities, or Mendelian inheritance pattern**. No entries were found in OMIM, ClinVar, or HGMD specific to AMN as a genetic disease. It is classified as an **acquired microvascular retinopathy**, not a genetic disorder. The only quasi-genetic association in the literature is an **acquired autoantibody state** (antiphospholipid antibodies) as a prothrombotic risk factor, which is an immunologic/hematologic risk factor rather than a germline genetic cause.

- **Causal genes:** None identified
- **Modifier genes:** None identified
- **Epigenetic information:** No epigenetic studies of AMN were found
- **Chromosomal abnormalities:** None reported

This section should likely be flagged as **"not applicable"** in the disease knowledge base entry, distinguishing AMN clearly from inherited macular dystrophies (e.g., Stargardt disease, macular telangiectasia type 2) with which it is sometimes confused due to imaging overlap.

---

## 5. Environmental Information

**Environmental/infectious/lifestyle factors** (overlapping with Section 2 risk factors, detailed here with supporting evidence):

- **Infectious agents:** Influenza-like illness (classic historical association); **SARS-CoV-2** (multiple case series, including an 11-patient/20-eye series with mean age 33.8 ± 12.6 years, female-predominant, mean interval 2.8 ± 2.5 days from positive PCR to ocular symptom onset); **dengue virus** (serotype 1 documented; described as a major manifestation of "dengue maculopathy" with scotomas persisting ≥6 months despite corticosteroid pulse therapy)
- **Vaccination:** COVID-19 mRNA (Moderna) and adenoviral vector (Oxford-AstraZeneca) vaccines — reported as temporally associated triggers in case reports, though causality is not established (temporal association vs. causation)
- **Lifestyle factors:** Oral contraceptive use, excessive caffeine intake
- **Pharmacologic/iatrogenic exposures:** IV epinephrine, ephedrine, IV contrast administration
- **Physiologic stressors:** Systemic shock, hypovolemia, hypotension, pregnancy, trauma (including Purtscher retinopathy-associated cases)

No occupational, toxin, or pollution exposures were identified in the literature searched.

Sources:
- [COVID-19 Related AMN: A Case Series — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10474860/)
- [Case report: dengue fever associated AMN — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10995331/)
- [AMN in Dengue Fever: Short-term Prospectively Followed Up Case Series — JAMA Ophthalmology](https://jamanetwork.com/journals/jamaophthalmology/fullarticle/2425881)
- [Bilateral AMN after Oxford-AstraZeneca COVID-19 vaccine — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8769920/)

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Trigger event** (viral illness, vasoactive drug, hypovolemia/shock, vaccination, trauma) →
2. **Microvascular compromise** of a watershed, low-flow vascular bed — historically attributed to the **deep capillary plexus (DCP)** of the retina, but more recent OCT-angiography evidence implicates the **inner choroid/choriocapillaris** as the primary site of perfusion deficit →
3. **Ischemia of the outer retina** at the level of the outer plexiform layer (OPL) and outer nuclear layer (ONL), with secondary involvement of the photoreceptor ellipsoid zone (IS/OS junction) →
4. **Photoreceptor and Müller cell injury**, manifesting as hyperreflective bands on structural OCT and hyporeflective lesions on near-infrared reflectance/en face OCT →
5. **Clinical manifestation**: paracentral scotoma corresponding topographically to the area of capillary/choriocapillaris non-perfusion.

**Molecular pathways:** No specific signaling cascade (Wnt, MAPK, mTOR, PI3K-AKT) has been implicated; the mechanism is vascular/ischemic rather than a defined biochemical pathway defect.

**Cellular processes:** Ischemia-driven photoreceptor outer segment disruption; no confirmed apoptosis/autophagy pathway studies in human tissue (no histopathology available given lack of biopsy/autopsy specimens — this is a clinical-imaging diagnosis).

**Imaging-based mechanistic evidence:**
- OCT angiography (Nemiroff et al., 2018, PMID: 29561336) demonstrated **flow voids in the deep capillary plexus** corresponding to AMN lesions, supporting DCP ischemia as (at least one) mechanism.
- More recent work (2024, PMC11271325) found **choriocapillaris vessel area density reduced by 27%** and **choroidal vessel area density reduced by 41%** relative to adjacent control tissue, supporting an alternative/additional **choroidal perfusion deficit** hypothesis.
- En face OCT analysis indicates the pathognomonic infrared hyporeflectivity is caused by **photoreceptor-level alterations rather than inner retinal layer changes** (PMC7885468).
- Structural OCT shows **hyperreflectivity in the outer plexiform and outer nuclear layers nasal to the fovea**, with disruption of the ellipsoid zone.

**Debate/uncertainty:** There is active debate in the literature (as of 2024 sources) whether the DCP or the choriocapillaris/inner choroid is the primary site of vascular insult — this remains an area of ongoing research rather than settled mechanism.

**Suggested GO terms:** GO:0001525 (angiogenesis, as a related/contrasting process), GO:0006915 (apoptotic process, hypothesized downstream of ischemia), GO:0034599 (cellular response to oxidative stress). **Suggested CL terms:** CL:0000573 (retinal cone cell), CL:0000604 (retinal rod cell), CL:0000751 (rod bipolar cell — deep capillary plexus territory), CL:0000636 (Müller cell).

Sources:
- [OCT Angiography of AMN reveals deep capillary ischemia — PubMed (PMID 29561336)](https://pubmed.ncbi.nlm.nih.gov/29561336/)
- [OCTA suggests choriocapillaris perfusion deficit as etiology of AMN — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11271325/)
- [Multimodal imaging for paracentral acute maculopathy; diagnostic role of en face OCT — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7885468/)

---

## 7. Anatomical Structures Affected

**Organ level:** Eye — specifically the **posterior segment/retina** (macula). Systemically, AMN is a manifestation/complication of an inciting systemic illness rather than causing secondary organ damage itself.

**Tissue/cell level:**
- Outer plexiform layer (OPL) and outer nuclear layer (ONL) — primary site of hyperreflective change
- Photoreceptor inner/outer segments (ellipsoid zone) — site of disruption
- Deep capillary plexus (DCP) — implicated vascular bed
- Choriocapillaris / inner choroid — alternative/additional implicated vascular bed
- Cell types: photoreceptors (rods and cones), Müller cells (secondary involvement)

**Subcellular level:** Photoreceptor outer segment disc membranes (structural disruption); no specific organelle-level (mitochondrial, ER) pathology has been documented in humans due to absence of histopathologic specimens.

**Localization (UBERON):** Macula lutea (UBERON:0002583), retina (UBERON:0000966), specifically the **parafoveal/paracentral retina** (lesions characteristically spare or point toward, but do not center on, the fovea). Fovea itself (UBERON:0004791) is typically relatively spared, correlating with preserved central acuity.

**Lateralization:** Bilateral in ~54% of cases; unilateral in the remainder. No consistent left/right predominance reported.

Sources:
- [Acute macular neuroretinopathy: A comprehensive review — PubMed](https://pubmed.ncbi.nlm.nih.gov/26973287/)

---

## 8. Temporal Development

**Onset:** Acute — typically in **young adulthood** (median age ~26 years per Bhavsar et al. review; mean 29.5 years; COVID-associated series mean 33.8 ± 12.6 years). Onset pattern is acute, frequently 1–7 days after a systemic trigger (fever, vaccination, dengue/COVID infection).

**Progression:**
- **Acute phase** (days to weeks): hyperreflective OPL/ONL band, IR hyporeflectivity, visible fundus lesion (reddish-brown/petaloid), scotoma onset
- **Subacute/evolution phase** (weeks to months): lesion fading, evolution of ellipsoid zone disruption, gradual improvement in acuity
- **Chronic/residual phase**: outer retinal thinning/atrophy at lesion site may persist; scotomas often persist indefinitely even after visual acuity substantially recovers

**Disease course pattern:** Predominantly **monophasic/self-limited** with a single acute event and gradual partial-to-good recovery; recurrence is uncommon but has been reported. Not typically relapsing-remitting or chronically progressive in the way of a neurodegenerative disease.

**Duration:** Self-limited acute event; **residual scotomas may be permanent/lifelong** even though the acute inflammatory/ischemic phase resolves.

**Remission patterns:** Spontaneous — no treatment has been shown to alter the natural course; recovery is attributed to natural resolution of the ischemic insult rather than intervention.

**Critical periods:** No defined window of therapeutic opportunity has been established, consistent with lack of proven treatment.

Sources:
- [Acute macular neuroretinopathy: A comprehensive review — PubMed](https://pubmed.ncbi.nlm.nih.gov/26973287/)
- [The characteristics of AMN following COVID-19 infection — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10782751/)

---

## 9. Inheritance and Population

**Epidemiology:** AMN is **rare**; precise population-level prevalence/incidence figures are not established via national registries. One retrospective single-center study found AMN-coded visits rose from **0.66 per 100,000 visits (2019) to 8.97 per 100,000 visits (2020)**, coincident with the COVID-19 pandemic — suggesting substantial under-ascertainment in typical (non-pandemic) years and an environmentally-modulated incidence.

**Inheritance pattern:** **None — AMN is not a genetic/heritable disease.** No penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency data apply.

**Population demographics:**
- **Sex ratio:** Strongly female-predominant — 84% female in the Bhavsar review (156 eyes/101 cases); male:female ratio 0.57:1 in the COVID-19-associated series (i.e., ~64% female)
- **Race/ethnicity:** Preferentially affects **young, non-Latino white women**, per case-series data (selection bias in published literature is a caveat)
- **Age distribution:** Predominantly reproductive-age young adults — median age 26 years, mean 29.5 years across pooled cases; COVID-associated cohort mean 33.8 ± 12.6 years
- **Geographic distribution:** Most published cases originate from the United States (per Bhavsar review), though this likely reflects publication/reporting bias rather than true geographic clustering; dengue-associated cases reported from Taiwan and other dengue-endemic regions.

Sources:
- [Acute macular neuroretinopathy: A comprehensive review — PubMed](https://pubmed.ncbi.nlm.nih.gov/26973287/)
- [The characteristics of AMN following COVID-19 infection — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10782751/)

---

## 10. Diagnostics

**Clinical/imaging tests (diagnosis is primarily clinical-imaging based; no lab biomarker or biopsy is diagnostic):**

- **Fundoscopy:** Reddish-brown, wedge-shaped/petaloid macular lesions with apices pointing toward the fovea; may be subtle, hypopigmented/grayish-white, or entirely absent on exam ("occult AMN," diagnosed by imaging alone) (PMC5762149)
- **Structural OCT (spectral-domain):** Hyperreflective band at the OPL/ONL junction acutely, evolving to outer nuclear layer thinning and ellipsoid zone disruption chronically — the primary diagnostic modality
- **Near-infrared reflectance (IR) imaging:** Characteristic hyporeflective lesion, often more sensitive than color fundus photography for detecting subtle or occult lesions
- **En face OCT:** Localizes the hyporeflective signal to the photoreceptor layer rather than inner retina
- **OCT angiography (OCTA):** Flow voids/reduced vessel density in the deep capillary plexus; more recent data show reduced choriocapillaris (−27%) and choroidal (−41%) vessel area density
- **Fluorescein angiography (FA):** Typically unremarkable or shows only subtle late staining — FA is relatively insensitive in AMN, an important distinguishing feature from other vascular retinopathies
- **Visual field testing:** Confirms paracentral scotoma corresponding to lesion location
- **Multifocal ERG:** Reduced amplitude corresponding to lesion area (reported in some case series)

**Genetic testing:** Not applicable/not indicated — AMN is not a genetic disorder, so gene panels, WES/WGS, CMA, karyotyping, FISH, and mitochondrial DNA testing have no established diagnostic role.

**Omics-based diagnostics:** None established; AMN is not currently diagnosed via transcriptomic, proteomic, metabolomic, or epigenomic assays.

**Clinical diagnostic criteria:** No formal society-endorsed diagnostic criteria (e.g., DSM/ICD operational criteria) exist beyond the characteristic clinical + multimodal imaging picture (fundoscopic lesion morphology + OCT hyperreflective band + IR hyporeflectivity + corresponding scotoma).

**Differential diagnosis:**
- **Paracentral acute middle maculopathy (PAMM)** — key differential/spectrum-overlap condition; PAMM lesions are more superficial (inner nuclear layer/DCP level) versus AMN's outer retinal (OPL/ONL) involvement; PAMM patients tend to be older (>50 years), more often male, with vasculopathic risk factors, versus AMN's younger (often <30 years), female-predominant demographic
- Acute idiopathic maculopathy
- White dot syndromes (multiple evanescent white dot syndrome, MEWDS)
- Macular telangiectasia type 2
- Central serous chorioretinopathy
- Solar/photic retinopathy
- Occult macular dystrophy

**Screening:** No population-based or genetic screening applies (acquired, non-heritable condition).

Sources:
- [Occult Acute Macular Neuroretinopathy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762149/)
- [Paracentral acute middle maculopathy and acute macular neuroretinopathy — PubMed](https://pubmed.ncbi.nlm.nih.gov/24220881/)
- [PAMM — EyeWiki](https://eyewiki.org/Paracentral_Acute_Middle_Maculopathy)
- [Multimodal imaging for paracentral acute maculopathy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7885468/)

---

## 11. Outcome/Prognosis

**Survival/mortality:** Not applicable — AMN is a non-life-threatening, vision-specific condition with no associated mortality.

**Morbidity/function:**
- Visual acuity outcomes are generally **good** — acuity is "often only mildly affected" since foveal center is typically spared
- **Paracentral scotomas frequently persist indefinitely**, even when Snellen acuity recovers to near-normal, representing the main residual morbidity
- No validated disease-specific quality-of-life instrument was identified in the literature searched

**Disease course/complications:** Self-limited in the majority; recurrence is uncommon. Outer retinal atrophy at the lesion site can be seen on long-term OCT follow-up even after subjective symptom resolution ("despite local retinal atrophy, subjective complaints disappear completely" in some patients) — indicating a dissociation between structural and functional/subjective recovery.

**Recovery potential:** Variable — some patients experience a fully self-limiting course with essentially complete retinal/functional recovery; others have persistent, permanent reduction in visual acuity and/or scotomas. No treatment has been shown to alter this natural trajectory.

**Prognostic factors:** No validated prognostic biomarkers or models identified; lesion size/location (foveal-sparing vs. foveal-involving) is the most intuitively relevant clinical factor described in case reports, though not formally validated.

Sources:
- [Acute macular neuroretinopathy — Retina Specialist](https://www.retina-specialist.com/article/acute-macular-neuroretinopathy)
- [Acute macular neuroretinopathy: A comprehensive review — PubMed](https://pubmed.ncbi.nlm.nih.gov/26973287/)

---

## 12. Treatment

**Pharmacotherapy:** **No proven, causative, or standardized treatment exists.** The mainstay of management is **observation**. Isolated case reports describe use of **systemic corticosteroids** with subjective/anatomical improvement in scotomas, but this is not supported by controlled evidence and is not a standard-of-care recommendation. Corticosteroid pulse therapy has also been tried in dengue-associated AMN without preventing persistent visual disturbance.

**Pharmacogenomics:** Not applicable — no established pharmacogenomic considerations for AMN treatment.

**Advanced therapeutics (gene therapy, cell therapy, RNA-based therapies, targeted therapies, immunotherapy):** None applicable or under investigation for AMN specifically.

**Surgical/interventional treatment:** None indicated; AMN is not a surgical disease.

**Supportive care:** Reassurance, monitoring for resolution, low-vision support if permanent scotomas cause functional impairment (e.g., for reading).

**Experimental treatments/clinical trials:** No AMN-specific registered clinical trials were identified in the sources reviewed.

**Treatment outcomes:** Because no treatment has demonstrated efficacy over observation, "response rates" are not meaningfully defined; most published corticosteroid use reflects anecdotal, uncontrolled experience.

**Treatment strategy:** The de facto clinical pathway is: (1) confirm diagnosis via multimodal imaging (OCT, IR, OCTA), (2) rule out/treat any identifiable underlying systemic trigger (e.g., manage the associated viral illness, discontinue oral contraceptives if implicated, address hypotension/shock), and (3) observe with serial OCT/visual field follow-up.

**Suggested MAXO terms:** MAXO term for "watchful waiting"/clinical observation would apply; no MAXO term for a specific pharmacologic or procedural intervention is well-supported given the absence of an evidence-based treatment.

Sources:
- [Acute macular neuroretinopathy — Retina Specialist](https://www.retina-specialist.com/article/acute-macular-neuroretinopathy)
- [AMN in Dengue Fever — JAMA Ophthalmology](https://jamanetwork.com/journals/jamaophthalmology/fullarticle/2425881)

---

## 13. Prevention

**Primary prevention:** No specific primary prevention strategy exists, since AMN is an unpredictable, idiosyncratic response to diverse systemic triggers (infection, vaccination, vasoactive drugs, hypotension). General avoidance/caution regarding known associated triggers (e.g., judicious use of vasoactive sympathomimetics, avoiding hypovolemia) has been suggested anecdotally but is not a validated prevention protocol.

**Secondary prevention:** Early recognition via multimodal imaging in at-risk patients (e.g., those presenting with paracentral scotoma after febrile illness) allows prompt diagnosis, though this does not alter the natural disease course.

**Immunization:** Not applicable in a preventive sense — vaccination is itself a reported (rare) trigger rather than a preventive measure for AMN.

**Screening/genetic screening:** Not applicable — non-heritable condition.

**Behavioral interventions:** Possible modifiable risk factor avoidance (e.g., reducing excessive caffeine intake, considering alternatives to oral contraceptives in a patient with a prior AMN episode) has been informally suggested in case discussions but lacks trial-level evidence.

**Counseling:** Genetic counseling is not applicable. Patients may benefit from counseling regarding the generally favorable but variable visual prognosis and the possibility of persistent scotomas.

**Public health/prophylaxis:** No public health intervention or prophylactic medication regimen has been established.

---

## 14. Other Species / Natural Disease

**Not established.** No literature was identified describing naturally occurring AMN in non-human species, veterinary case reports, or OMIA entries. AMN appears to be a human-specific clinical entity as currently described in the literature (searches for veterinary/animal natural disease returned no relevant AMN-specific results, only unrelated age-related macular degeneration animal model literature).

---

## 15. Model Organisms

**No dedicated animal or in vitro model of AMN was identified** in the literature searched (MGI, ZFIN, RGD, and general model-organism searches did not surface AMN-specific models). This is consistent with AMN's status as an acquired, imaging-defined clinical syndrome without a known genetic driver to model, and with the practical difficulty of modeling transient, spontaneously-resolving deep capillary plexus/choriocapillaris ischemia. Related ischemic retinal models (e.g., rodent retinal vein occlusion or middle cerebral/retinal artery occlusion models used to study deep capillary plexus ischemia and PAMM) may be indirectly relevant analogs but were not confirmed as validated AMN models in the sources reviewed. This section should be flagged as a **research gap** in the disease knowledge base.

---

## Summary of Key Data Gaps for Knowledge Base Curation

1. **No genetic/molecular section applies** — flag explicitly as N/A rather than leaving blank, to distinguish from an incomplete curation.
2. **No animal models or veterinary natural disease** identified — flag as N/A/research gap.
3. **MONDO ID** requires direct confirmation from the current MONDO release (not independently verified in this search).
4. **ICD-10-CM code** shows some inconsistency across sources (H35.89 vs. H35.3) — recommend verifying against current CMS/WHO coding guidance.
5. Mechanism (DCP vs. choriocapillaris as primary ischemic site) is an **active, unresolved scientific debate** — should be represented as competing hypotheses rather than a single settled mechanism.

**Key primary references (PMIDs):**
- Bhavsar KV et al. Acute macular neuroretinopathy: A comprehensive review of the literature. Surv Ophthalmol. 2016;61(5):538-565. **PMID: 26973287**
- Nemiroff J et al. Optical coherence tomography angiography of acute macular neuroretinopathy reveals deep capillary ischemia. **PMID: 29561336**
- Fawzi AA et al. Acute macular neuroretinopathy: long-term insights revealed by multimodal imaging. Retina. 2012;32(8):1500-1513.
- Rahimy E et al. Paracentral acute middle maculopathy and acute macular neuroretinopathy. **PMID: 24220881**

Sources:
- [Orphanet: Acute macular neuroretinopathy](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=488239&lng=EN)
- [Acute macular neuroretinopathy: A comprehensive review of the literature - PubMed](https://pubmed.ncbi.nlm.nih.gov/26973287/)
- [OCT Angiography of AMN reveals deep capillary ischemia - PubMed](https://pubmed.ncbi.nlm.nih.gov/29561336/)
- [OCTA suggests choriocapillaris perfusion deficit - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11271325/)
- [Multimodal imaging for paracentral acute maculopathy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7885468/)
- [The characteristics of AMN following COVID-19 infection — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10782751/)
- [COVID-19 Related AMN: A Case Series — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10474860/)
- [Bilateral AMN after Oxford-AstraZeneca COVID-19 vaccine — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8769920/)
- [Case report: dengue fever associated AMN — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10995331/)
- [AMN in Dengue Fever — JAMA Ophthalmology](https://jamanetwork.com/journals/jamaophthalmology/fullarticle/2425881)
- [Occult Acute Macular Neuroretinopathy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762149/)
- [PAMM and AMN — PubMed](https://pubmed.ncbi.nlm.nih.gov/24220881/)
- [Paracentral Acute Middle Maculopathy — EyeWiki](https://eyewiki.org/Paracentral_Acute_Middle_Maculopathy)
- [Acute macular neuroretinopathy — Retina Specialist](https://www.retina-specialist.com/article/acute-macular-neuroretinopathy)
- [NORD/MONDO: acute macular neuroretinopathy](https://rarediseases.org/mondo-disease/acute-macular-neuroretinopathy/)
- [ICD10Data H35.89](https://www.icd10data.com/ICD10CM/Codes/H00-H59/H30-H36/H35-/H35.89)