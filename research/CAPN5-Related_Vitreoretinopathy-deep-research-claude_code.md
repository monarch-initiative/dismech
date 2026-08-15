---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-17T11:54:07.012570'
end_time: '2026-07-17T11:59:11.108756'
duration_seconds: 304.1
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: CAPN5-related vitreoretinopathy
  mondo_id: MONDO:0100450
  category: Inherited
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
  web_search_requests: 16
  num_turns: 33
  total_cost_usd: 1.3032450000000004
  session_id: 49e16942-32e1-47b7-bff9-e0aa71a17f82
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CAPN5-related vitreoretinopathy
- **MONDO ID:** MONDO:0100450 (if available)
- **Category:** Inherited

## Research Objectives

Please provide a comprehensive research report on **CAPN5-related vitreoretinopathy** covering all of the
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

# CAPN5-Related Vitreoretinopathy: Comprehensive Disease Characteristics Report

## 1. Disease Information

**Overview:** CAPN5-related vitreoretinopathy — most commonly termed **Autosomal Dominant Neovascular Inflammatory Vitreoretinopathy (ADNIV)**, and listed in OMIM as **Vitreoretinopathy, Neovascular Inflammatory (VRNI)** — is a rare, progressive, autosomal dominant autoinflammatory/autoimmune eye disease caused by gain-of-function missense variants in *CAPN5* (calpain-5). It is a hereditary intraocular disease that sequentially mimics three common causes of blindness: **it presents first as posterior uveitis, then evolves to resemble retinitis pigmentosa, and finally proliferative diabetic retinopathy**, ultimately progressing to phthisis bulbi and complete blindness ([EyeWiki](https://eyewiki.org/Autosomal_Dominant_Neovascular_Inflammatory_Vitreoretinopathy_(ADNIV); [Mahajan et al. 2012, PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)).

**Key identifiers:**
- **OMIM (phenotype):** #193235 — VITREORETINOPATHY, NEOVASCULAR INFLAMMATORY; VRNI
- **OMIM (gene):** *602537 — CALPAIN 5; CAPN5
- **Gene:** CAPN5, HGNC:1482, NCBI Gene ID 726, chromosome 11q13.5 (GRCh38: 11:77,066,971–77,126,155)
- **MONDO ID:** MONDO:0100450 (CAPN5-related vitreoretinopathy) — confirmed in NORD/GARD listings
- **GTR/MedGen:** C4721549 (Autosomal dominant neovascular inflammatory vitreoretinopathy)
- **Orphanet:** listed under CAPN5-associated conditions (Orphanet gene page for CAPN5)
- **ICD-10/11:** No disease-specific code; typically coded under hereditary retinal dystrophy/uveitis codes (H35.5, H30.9)

**Synonyms:** Autosomal Dominant Neovascular Inflammatory Vitreoretinopathy (ADNIV); Neovascular Inflammatory Vitreoretinopathy (NIV); CAPN5-Neovascular Inflammatory Vitreoretinopathy (CAPN5-NIV); Calpain-5 retinopathy/retinal degeneration.

**Data source type:** Information is derived almost entirely from **aggregated disease-level resources** — primarily case series and extended-pedigree studies from a small number of research groups (notably the Mahajan/Stanford and Bassuk/Iowa laboratories), OMIM, GeneReviews-adjacent literature reviews, and mouse/zebrafish model studies — rather than large-scale EHR-derived cohorts, reflecting the disease's rarity (only a handful of kindreds and fewer than 10 distinct pathogenic variants reported worldwide as of the most recent literature).

---

## 2. Etiology

**Disease causal factors:** ADNIV/VRNI is a purely **monogenic** disorder. It is caused by heterozygous, autosomal dominant, gain-of-function missense variants in *CAPN5*, which encodes the calcium-activated cysteine protease calpain-5. There is no known environmental, infectious, or multifactorial contribution to disease initiation — onset and course are governed by the causal variant itself ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)).

**Genetic risk factors:**
- Causal variants cluster in two structural regions of calpain-5: (1) the **catalytic protease core**, near the calcium-sensitive "gating loop" adjacent to the catalytic histidine (variants p.Arg243Leu, p.Leu244Pro, p.Lys250Asn, p.Gly267Ser, p.Arg289Trp), and (2) the **C2/regulatory domain** (p.Gly376Ser) ([PMID 25856303](https://pmc.ncbi.nlm.nih.gov/articles/PMC4391918/); [PMID 29040051](https://pmc.ncbi.nlm.nih.gov/articles/PMC6711405/)).
- Variant location and resultant degree of protease hyperactivation correlate with severity — catalytic-domain variants generally produce more severe, earlier-onset disease than the single reported regulatory (C2)-domain variant ([PMID 29040051](https://pmc.ncbi.nlm.nih.gov/articles/PMC6711405/); [PMID 32274441](https://pubmed.ncbi.nlm.nih.gov/32274441/)).
- Family history/inheritance from an affected parent is the dominant risk factor given autosomal dominant transmission with reported complete penetrance in classic pedigrees, though incomplete/age-dependent penetrance has since been documented (see Section 9).

**Environmental risk factors:** None established. No toxin, occupational, dietary, or infectious exposure has been linked to onset or severity.

**Protective factors:** No genetic modifier or protective variant has been identified. No environmental/lifestyle factor has been shown to reduce risk or delay onset. Absence of the pathogenic *CAPN5* allele is the only known "protective" factor; wild-type calpain-5 shows tightly calcium-regulated, membrane-localized activity that is lost in mutant alleles.

**Gene-environment interactions:** Not established. Disease expression appears driven by the retina's naturally high local calcium flux (from phototransduction), which interacts with the calcium-hypersensitized mutant enzyme to trigger pathology — this is a tissue-intrinsic biochemical interaction rather than a classic gene-environment (exogenous exposure) interaction ([PMID 25994508](https://pubmed.ncbi.nlm.nih.gov/25994508/)).

---

## 3. Phenotypes

ADNIV progresses through canonical, roughly decade-long stages, each with characteristic clinical signs (Mahajan et al., [PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/); EyeWiki).

| Stage | Approx. duration | Key phenotype | Suggested HPO term(s) |
|---|---|---|---|
| I | ~1st decade of disease | Non-infectious posterior uveitis, vitreous cells, abnormal ERG (reduced b-wave) | Uveitis (HP:0000554), Vitritis, Abnormal electroretinogram (HP:0000512) |
| II | ~2nd decade | Retinitis-pigmentosa-like pigmentary photoreceptor degeneration, night blindness | Retinal pigment epithelial mottling (HP:0007737), Nyctalopia (HP:0000662), Retinal degeneration (HP:0000546) |
| III | ~3rd decade | Retinal/iris neovascularization resembling proliferative diabetic retinopathy, vascular dropout | Retinal neovascularization (HP:0007843), Iris neovascularization |
| IV | ~4th decade | Intraocular fibrosis, epiretinal/proliferative vitreoretinopathy, tractional retinal detachment | Vitreoretinal degeneration, Retinal detachment (HP:0000541), Vitreous hemorrhage (HP:0007843/HP:0011505) |
| V | Terminal | Phthisis bulbi, complete blindness | Phthisis bulbi (HP:0025438), Blindness (HP:0000618) |

**Additional/shared phenotypic features across stages:**
- Cystoid macular edema (HP:0011505 area — Macular edema)
- Cataract (HP:0000518), often nuclear sclerotic
- Neovascular glaucoma (HP:0007843-adjacent; Glaucoma HP:0000501)
- Chronic vitreous hemorrhage
- CD3+ T-lymphocyte infiltration of iris, choroid, ciliary body, vitreous, and retina (largely T-cell predominant, occasional minor B-cell component <15% of infiltrate) ([PMID 23861576](https://pmc.ncbi.nlm.nih.gov/articles/PMC3704602/))
- Pigment clumping distinguishable from the bone-spicule pattern of typical retinitis pigmentosa

**Syndromic/extraocular phenotype (severe end of spectrum — p.Arg289Trp):** progressive sensorineural hearing loss (unresponsive to immunosuppression), developmental delay (language, social, quantitative reasoning), mild truncal hypotonia, nonspecific temporal lobe EEG abnormality, chronic diarrhea/constipation, band keratopathy, optic neuritis, and complete vision loss by age 5 ([Velez et al., Mol Case Stud, PMC5983175](https://pmc.ncbi.nlm.nih.gov/articles/PMC5983175/)). Suggested HPO terms: Sensorineural hearing impairment (HP:0000407), Global developmental delay (HP:0001263), Hypotonia (HP:0001252), Band keratopathy (HP:0007750).

**Onset, severity, progression, frequency:**
- **Onset:** Classically second–third decade of life; documented range from age 3 (infancy/childhood) to as late as the 5th–7th decade for mild presentations ([PMID 32274441](https://pubmed.ncbi.nlm.nih.gov/32274441/)).
- **Severity:** Highly variable — from mild, incidentally-discovered peripheral pigmentary degeneration with preserved 6/6 vision (p.Gly376Ser) to catastrophic childhood-onset syndromic blindness with hearing loss (p.Arg289Trp).
- **Progression:** Classically **relentlessly progressive** over ~40+ years through five stages to blindness, but a subset of patients (notably milder catalytic and the regulatory-domain variant) show slow, non-progressive or minimally progressive courses even into their 60s–70s.
- **Frequency:** Because of extreme rarity, percentage-based phenotype frequencies across a large cohort are not established; findings are drawn from fewer than a dozen published kindreds/cases.

**Quality of life impact:** Progressive, bilateral, irreversible vision loss culminating in legal/complete blindness has profound impact on independence, employment, and mental health; chronic recurrent intraocular inflammation and repeated surgeries (vitrectomy, implant placement/exchange) add significant treatment burden. No disease-specific EQ-5D/SF-36 data were identified in the literature; QOL burden is inferred from the severity of visual and (in syndromic cases) auditory/neurodevelopmental impairment.

---

## 4. Genetic/Molecular Information

**Causal gene:** *CAPN5* (calpain-5), HGNC:1482, NCBI Gene 726, OMIM *602537, chromosome 11q13.5. Encodes a 640-amino-acid calcium-activated cysteine protease.

**Pathogenic variants identified to date (all heterozygous, germline, missense, gain-of-function):**

| Variant (protein) | Nucleotide (CAPN5 mRNA) | Domain | Reported phenotype | PMID |
|---|---|---|---|---|
| p.Arg243Leu (R243L) | c.728G>T | Catalytic core, gating loop | Classic ADNIV, onset ~20s; mild variants also reported at 45/69 | 23055945 |
| p.Leu244Pro (L244P) | c.731T>C | Catalytic core, gating loop | Classic ADNIV | 23055945; family cohort 37782277 |
| p.Lys250Asn (K250N) | c.750G>T | Catalytic core, gating loop | Severe uveitis, retinal neovascularization/detachment | 25856303 |
| p.Gly267Ser (G267S) | c.799G>A | Catalytic domain (exon 6) | Severe, congenital nystagmus, early vitreoretinopathy | 29040051 |
| p.Gly376Ser (G376S) | c.1126G>A | C2/regulatory domain | Mild, incidental, near-normal vision at 19 | 29040051 |
| p.Arg289Trp (R289W) | c.865C>T | Catalytic domain | Most severe/syndromic: childhood blindness, hearing loss, developmental delay | Velez et al., PMC5983175 |

- **Variant classification (ACMG/AMP):** All are classified pathogenic/likely pathogenic in ClinVar (e.g., R243L: ClinVar RCV000033027, RCV001383042, RCV001535499), based on segregation in multigenerational pedigrees, absence from population databases, and functional (biochemical/animal model) validation.
- **Allele frequency:** R243L was **absent from 272 ethnically matched controls and from dbSNP/1000 Genomes** at time of discovery ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)); no specific gnomAD frequency data were retrievable in this search, consistent with these being ultra-rare/private disease alleles essentially absent from population reference databases.
- **Somatic vs. germline:** All reported variants are germline; the R289W case was confirmed **de novo** (absent in both parents).
- **Functional consequences:** **Gain-of-function**, not haploinsufficiency. Mutations (1) increase calcium sensitivity of the protease (R243L is reported "300% more sensitive to calcium"), (2) cause mislocalization of the protein from the plasma membrane ("ruffled" pattern) to a diffuse cytosolic distribution, and (3) increase proteolytic/autolytic activity, with R289W showing the greatest hyperactivation and most proteolytic fragments among tested variants ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/); [PMID 25994508](https://pubmed.ncbi.nlm.nih.gov/25994508/); [PMC5983175](https://pmc.ncbi.nlm.nih.gov/articles/PMC5983175/)). *Capn5* knockout mice show no retinal phenotype, supporting that loss-of-function is not the mechanism ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)).

**Modifier genes:** None formally established; a case report describes co-segregating *TYR* (albinism) variants in one family without altering core ADNIV phenotype, but this is not a validated modifier.

**Epigenetic information:** Not reported for this disease.

**Chromosomal abnormalities:** None reported — disease is caused by point mutations, not structural chromosomal rearrangements. Original linkage mapping localized the locus to an ~22 Mb interval on 11q13, later refined to a 6 Mb interval between rs879380 and D11S1789 ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)).

**Suggested ontology terms:** MONDO:0100450 (CAPN5-related vitreoretinopathy); HGNC:1482 (CAPN5); GO:0004198 (calcium-dependent cysteine-type endopeptidase activity); GO:0005509 (calcium ion binding).

---

## 5. Environmental Information

- **Environmental factors/toxins:** None identified or implicated; disease is fully genetically determined.
- **Lifestyle factors:** None established as risk or protective factors.
- **Infectious agents:** None. Although the early clinical presentation mimics infectious/idiopathic posterior uveitis, no infectious trigger or pathogen has been implicated — pathology is autoimmune/autoinflammatory and driven by the intrinsic mutant enzyme.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Molecular trigger:** Heterozygous gain-of-function missense mutation in *CAPN5* increases calcium sensitivity and catalytic activity of calpain-5 and causes its mislocalization from the photoreceptor cell membrane to the cytosol ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)).
2. **Cell-intrinsic effect:** In the retina's naturally high-calcium synaptic environment (phototransduction), hyperactive mutant calpain-5 undergoes aberrant, promiscuous proteolysis of normal substrates at photoreceptor synapses, disrupting synaptic signaling — proteomic studies show early loss of synaptic proteins including **neurexin-2 (NRXN2), glutamate receptor 4 (GluR4), neurofascin, and calsyntenin-1**, correlating with the earliest clinical/electrophysiological finding, reduced ERG b-wave amplitude ([PMID 31110225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)).
3. **Innate immune activation:** Mouse retina expressing mutant hCAPN5-R243L shows upregulation of **Toll-like receptor pathway genes, chemokines, and cytokines**, consistent with local innate immune activation ([PMID 25994508](https://pubmed.ncbi.nlm.nih.gov/25994508/)). Human vitreous proteomics shows marked elevation of **acute-phase/complement proteins (C1R, C6, C7, C8, C9)**, implicating complement-mediated innate immunity ([PMID 31110225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)).
4. **Adaptive autoimmune response:** Dense **CD3+ T-lymphocyte infiltration** of the uvea, vitreous, and retina (with minor B-cell component) drives chronic autoimmune uveitis, likely via exposure of neo-epitopes generated by aberrant calpain proteolysis ([PMID 23861576](https://pmc.ncbi.nlm.nih.gov/articles/PMC3704602/); [PMID 31110225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)).
5. **Oxidative stress and neurodegeneration:** Loss of antioxidant defenses in vitreous (reduced SOD1, SOD3, peroxiredoxins, catalase, clusterin) contributes to progressive photoreceptor degeneration mimicking retinitis pigmentosa ([PMID 31110225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)).
6. **Angiogenesis:** Downregulation of the anti-angiogenic protein **opticin**, alongside upregulated crystallins (CRYAA, CRYAB, CRYBB1) correlating with elevated VEGF, promotes pathologic retinal/iris neovascularization mimicking proliferative diabetic retinopathy ([PMID 31110225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)).
7. **Fibrosis/end-stage:** Downregulation of the extracellular matrix proteoglycan **versican (VCAN)** disrupts normal vitreous structure, contributing to proliferative vitreoretinopathy, tractional retinal detachment, and eventual phthisis bulbi.

**Molecular pathways:** Calpain/cysteine protease proteolysis; Toll-like receptor signaling; complement activation (classical/terminal pathway); VEGF/angiogenesis signaling; oxidative stress response.
- Suggested GO Biological Process terms: GO:0006508 (proteolysis), GO:0002250 (adaptive immune response), GO:0045087 (innate immune response), GO:0001525 (angiogenesis), GO:0006979 (response to oxidative stress), GO:0007268 (chemical synaptic transmission).

**Protein dysfunction:** Gain-of-function/dysregulation rather than misfolding — hyperactive, mislocalized protease (see Section 4). CAPN5 protein structure comprises a protease core (PC, domains I–II; crystal structure PDB 6P3Q, 2.8 Å) and a C-terminal C2 domain (loss of the classical calpain penta-EF-hand domain IV) that contributes to membrane localization and calcium-dependent activation ([PMID 33811937](https://pmc.ncbi.nlm.nih.gov/articles/PMC8588747/)).

**Cell types involved:** Photoreceptor cells (rods/cones) — primary site of CAPN5 expression (strong immunostaining in photoreceptor inner segments/nuclei; minimal in other retinal layers; CAPN5 transcript detected at 4.63 FPKM in human retina); infiltrating CD3+ T lymphocytes; retinal/iris vascular endothelial cells (neovascularization); retinal pigment epithelium and Müller glia (regeneration/stress response, per zebrafish data). Suggested CL terms: CL:0000210 (photoreceptor cell), CL:0000084 (T cell), CL:0002586 (retinal blood vessel endothelial cell), CL:0000636 (Müller cell).

**Tissue damage mechanisms:** Chronic inflammation-driven bystander photoreceptor degeneration, oxidative stress, aberrant angiogenesis with vascular leakage/hemorrhage, and progressive fibrotic scarring/traction leading to retinal detachment.

**Molecular profiling data available:** Vitreous **proteomics** (mass spectrometry) is the principal omics dataset published for this disease ([PMID 31110225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)). No transcriptomic, metabolomic, lipidomic, single-cell, or spatial transcriptomic human datasets were identified. Mouse retinal transcriptome changes (Toll-like receptor pathway, chemokine/cytokine upregulation) are reported in the R243L transgenic model ([PMID 25994508](https://pubmed.ncbi.nlm.nih.gov/25994508/)).

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary organ: **Eye** (retina, vitreous, uvea/iris, choroid, ciliary body, lens, optic nerve).
- Secondary/syndromic involvement (severe R289W variant only): inner ear (sensorineural hearing loss), central nervous system (developmental delay, EEG abnormalities), gastrointestinal tract (chronic diarrhea/constipation).
- Body systems: primarily **sensory/visual system**; syndromic cases also involve **auditory system** and **nervous system**.

**Tissue/cell level:**
- Neural retina — photoreceptor layer (rods and cones) is the principal site of CAPN5 expression and initial pathology.
- Uveal tract (iris, ciliary body, choroid) — site of lymphocytic infiltration and neovascularization.
- Vitreous — site of inflammatory cell infiltration, hemorrhage, and fibrotic membrane formation.
- Retinal vasculature — site of neovascularization and vascular dropout.
- Suggested CL terms: CL:0000210 (photoreceptor cell), CL:0000573 (retinal cone cell), CL:0000604 (retinal rod cell), CL:0000084 (T cell), CL:0000232 (erythrocyte, vitreous hemorrhage context).

**Subcellular level:** Plasma membrane (site of normal calpain-5 localization, lost in mutants); cytosol (site of mutant mislocalization); photoreceptor synaptic terminals (site of synaptic protein proteolysis). Suggested GO Cellular Component terms: GO:0005886 (plasma membrane), GO:0005829 (cytosol), GO:0098992 (photoreceptor ribbon synapse).

**Localization:** Bilateral in essentially all reported cases (autosomal dominant, systemically expressed gene); disease is generally symmetric, though stage/severity can vary somewhat between the two eyes of an individual.
- Suggested UBERON terms: UBERON:0000966 (retina), UBERON:0003893 (vitreous body), UBERON:0001769 (choroid), UBERON:0001769/UBERON:0001770 (iris/uvea), UBERON:0000970 (eye).

---

## 8. Temporal Development

- **Onset:** Classically insidious, in the **second to third decade of life**, but ranges from early childhood (age 3, especially severe variants) to late adulthood (mild variants presenting incidentally at 45–69 years) ([PMID 32274441](https://pubmed.ncbi.nlm.nih.gov/32274441/)).
- **Onset pattern:** Insidious/chronic rather than acute; earliest sign is often asymptomatic ERG b-wave reduction or mild vitreous cell before overt visual symptoms.
- **Disease stages:** Five clinically defined stages (uveitis → RP-like degeneration → neovascularization → fibrosis/detachment → phthisis bulbi), each lasting roughly a decade in classic pedigrees (see Section 3 table).
- **Progression rate:** Variable — classic catalytic-domain mutations (R243L, L244P) show relentless progression over ~40 years to blindness; the regulatory-domain variant (G376S) and some late-onset R243L cases show much slower or apparently arrested progression.
- **Disease course pattern:** Chronic, progressive; not classically relapsing-remitting, though inflammatory activity can wax and wane with treatment.
- **Disease duration:** Chronic, lifelong, ultimately blinding in the classic/severe forms; some mild cases may remain stable for decades without progressing to advanced stages.
- **Remission:** No spontaneous remission described. Inflammation can be temporarily suppressed by corticosteroid/immunosuppressive therapy, but degenerative and fibrotic components generally continue despite treatment ("persistent retinal degeneration and vision loss" despite steroid control of inflammation) ([PMID 23861576](https://pmc.ncbi.nlm.nih.gov/articles/PMC3704602/)).
- **Critical periods:** Earlier disease stages (I–II, before fibrosis/detachment) represent the presumptive window for therapeutic intervention (anti-inflammatory, anti-VEGF, or future gene therapy) before irreversible structural damage occurs.

---

## 9. Inheritance and Population

**Epidemiology:** Extremely rare; one source estimates prevalence of NIV at **~1 in 1,000,000** (Sequencing.com educational summary, citing rare-disease estimates). Formal incidence/prevalence figures from Orphanet/GBD were not retrievable in this search — the disease is not separately tracked in most national registries given its rarity and historically limited number of characterized kindreds (fewer than 10 published families worldwide).

**Inheritance pattern:** Autosomal dominant, with the founding pedigrees showing **complete penetrance** ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)). However, subsequent case reports of mild, late-onset presentations (age 45, 69) in R243L carriers suggest **age-dependent and possibly incomplete penetrance/expressivity** is more accurate for the broader mutation spectrum ([PMID 32274441](https://pubmed.ncbi.nlm.nih.gov/32274441/)).

**Penetrance:** High/complete in classically studied large pedigrees; increasingly recognized as variable/age-dependent as more (mild) cases are identified.

**Expressivity:** Markedly **variable**, correlating with variant location and degree of protease hyperactivation — ranging from asymptomatic incidental peripheral pigmentary change to catastrophic syndromic childhood blindness with hearing loss and developmental delay (see Section 3/4). Six distinct pathogenic mutations reported to date, "each resulting in varying levels of protease hyperactivity with a direct correlation to clinical severity" ([PMC7132063](https://pmc.ncbi.nlm.nih.gov/articles/PMC7132063/)).

**Genetic anticipation:** Not reported/established for this disorder (not a repeat-expansion disease).

**Germline mosaicism:** Not specifically reported; one case (R289W) was confirmed de novo.

**Founder effects:** The large original ADNIV kindred is a well-characterized multigenerational American family; whether R243L represents a founder allele in that lineage specifically (rather than recurrent mutation) is consistent with dominant private-variant inheritance, though this is not formally established as a population founder effect.

**Consanguinity:** Not a relevant risk factor given the dominant (not recessive) inheritance pattern.

**Carrier frequency:** Not applicable in the traditional (recessive-carrier) sense; pathogenic alleles are essentially private/family-specific and absent from population databases (gnomAD/1000 Genomes/dbSNP), consistent with an ultra-rare, highly penetrant dominant disease allele.

**Population demographics:** No specific ethnic or geographic predilection has been established; reported kindreds are from the United States and United Kingdom. No sex predilection is reported (autosomal, both sexes affected, e.g., two affected sisters in the K250N pedigree). Age distribution spans childhood through the 7th decade depending on variant.

---

## 10. Diagnostics

**Clinical/ophthalmic tests:**
- Dilated fundus examination — vitreous cells, pigmentary changes, neovascularization, fibrosis, detachment.
- **Electroretinography (ERG)** — early, characteristic finding of reduced/lost b-wave amplitude, often the earliest objective abnormality, later progressing to non-recordable cone/rod responses.
- **Fluorescein angiography (FA)** — used serially (every 6–12 months in stable/low-leakage patients) to assess vascular leakage/non-perfusion, guiding treatment (laser, anti-VEGF).
- Optical coherence tomography (OCT) — macular edema, epiretinal membrane, structural retinal changes.
- Slit-lamp exam — cataract, band keratopathy, anterior chamber inflammation.

**Biomarkers:** Vitreous proteomic signature (elevated complement/acute-phase proteins C1R/C6/C7/C8/C9; reduced antioxidants SOD1/SOD3/catalase/peroxiredoxins/clusterin; altered crystallins and opticin) is a research-level biomarker panel, not yet a validated clinical diagnostic biomarker ([PMID 31110225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)).

**Histopathology:** Immunohistochemistry of enucleated/explanted eyes shows dense CD3+ T-cell infiltration of uvea/vitreous/retina with minimal neutrophils/eosinophils/macrophages ([PMID 23861576](https://pmc.ncbi.nlm.nih.gov/articles/PMC3704602/)).

**Genetic testing:**
- **Single-gene *CAPN5* sequencing (Sanger or targeted NGS)** is the recommended diagnostic approach in patients with a phenotype suggestive of ADNIV, especially those with atypical/unexplained uveitis, atypical retinitis pigmentosa, or a family history of progressive vitreoretinopathy.
- *CAPN5* should be included in **inherited retinal dystrophy gene panels**, particularly for patients without a clear family history or classic combination of inflammation + vitreoretinopathy, since phenotype can mimic isolated uveitis or isolated RP.
- Whole-exome sequencing (WES) has been the discovery method for all novel variants reported to date (linkage mapping + WES in the original family; WES/targeted panels in subsequent case reports), underscoring its utility when single-gene testing is uninformative or the phenotype is atypical/syndromic.
- No specific CMA, karyotype, FISH, mitochondrial, or repeat-expansion testing is indicated, as this is a single-gene missense disorder.
- The NIH Genetic Testing Registry (GTR) lists this condition under MedGen C4721549, though specific commercial test/lab listings were not retrievable in this search.

**Differential diagnosis:**
- Idiopathic (non-infectious) posterior uveitis / panuveitis — mimicked in Stage I.
- Autosomal dominant retinitis pigmentosa — mimicked in Stage II (distinguishing feature: ADNIV shows pigment **clumps** rather than classic bone-spicule pigmentation).
- Proliferative diabetic retinopathy — mimicked in Stage III (absence of diabetes, family history, and early inflammatory history help distinguish).
- Idiopathic vitreomacular traction, ischemic neovascular retinopathy — noted as common misdiagnoses in the absence of recognized family history.
- Familial exudative vitreoretinopathy (FEVR) — differs by lacking prominent chronic autoimmune uveitis and by different causal genes (*FZD4, LRP5, TSPAN12, NDP*).

**Screening:** No population or newborn screening program exists given rarity; **cascade genetic testing of at-risk relatives** in known kindreds (with baseline ERG/FA) is the recommended approach, and early genetic diagnosis has been reported to expedite intervention before advanced fibrotic/detachment stages (Ophthalmology Advisor).

---

## 11. Outcome/Prognosis

**Survival/mortality:** ADNIV/VRNI is a strictly ocular (or, rarely, oculo-syndromic) disease with **no established impact on overall life expectancy** in the classic (non-syndromic) form; mortality data are not applicable/reported.

**Morbidity/function:**
- Classic natural history: progression through five stages over ~40 years culminating in **complete blindness/phthisis bulbi**.
- Severe syndromic form (R289W): complete vision loss by age 5, plus profound sensorineural hearing loss and developmental delay — substantial multi-domain disability.
- Mild forms (G376S, late-onset R243L): may retain good visual acuity (e.g., 6/6, 6/5) for years to decades with only peripheral, non-progressive or slowly progressive findings.

**Disease course/complications:** Cystoid macular edema, cataract, neovascular glaucoma, recurrent vitreous hemorrhage, tractional/rhegmatogenous retinal detachment, proliferative vitreoretinopathy, and fibrotic encapsulation of implanted steroid devices requiring repeat surgery ([PMID 23785231](https://pmc.ncbi.nlm.nih.gov/articles/PMC3682853/)).

**Recovery potential:** Structural damage (fibrosis, detachment, photoreceptor loss) is generally **irreversible**; treatment aims to slow progression and control inflammation/neovascularization rather than reverse damage. Even with steroid control of inflammation, degeneration and vision loss can persist ([PMID 23861576](https://pmc.ncbi.nlm.nih.gov/articles/PMC3704602/)).

**Prognostic factors:** Causal variant identity/domain location is the principal known prognostic factor (catalytic-domain variants → more severe; regulatory-domain variant → milder); age of onset also correlates inversely with severity in the limited case data available.

---

## 12. Treatment

**Pharmacotherapy:**
- **Corticosteroids** (topical, periocular, intravitreal, or oral) — mainstay for controlling active intraocular inflammation, but disease often shows incomplete/transient response, especially against the degenerative component.
- **Steroid-sparing systemic immunosuppression** — used for patients with substantial vascular leakage/inflammation; however, "**patients with CAPN5 fail conventional immunosuppressive therapy, such as oral corticosteroids and infliximab (anti-TNF-α)**," indicating a treatment-resistant, non-classic-autoimmune biology (search synthesis of case literature).
- **Intravitreal corticosteroid implants** (e.g., fluocinolone acetonide/Retisert) — used for sustained local anti-inflammatory delivery; recurrent implant placement reported in managed cohorts ([PMID 23785231](https://pmc.ncbi.nlm.nih.gov/articles/PMC3682853/); c.731T>C family cohort, [PMID 37782277](https://pubmed.ncbi.nlm.nih.gov/37782277/)).
- **Anti-VEGF intravitreal injections** — used for retinal/iris neovascularization (Stage III).

**Surgical/interventional:**
- **Panretinal/focal laser photocoagulation** for peripheral non-perfusion.
- **Pars plana vitrectomy** for vitreous hemorrhage, epiretinal membrane, and tractional retinal detachment.
- **Surgical excision of fibrotic capsules** around steroid implants to re-establish drug delivery in advanced proliferative disease ([PMID 23785231](https://pmc.ncbi.nlm.nih.gov/articles/PMC3682853/)).
- Cataract extraction and glaucoma drainage device implantation (e.g., for rubeotic/neovascular glaucoma) as needed in advanced disease ([PMID 29040051](https://pmc.ncbi.nlm.nih.gov/articles/PMC6711405/)).

**Supportive/monitoring:** Regular follow-up with fundus exam and fluorescein angiography every 6–12 months for patients with minimal leakage; low-vision rehabilitation services for advanced disease.

**Experimental/advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or disease-specific clinical trial (ClinicalTrials.gov) was identified for CAPN5-NIV in this search. Given the gain-of-function mechanism, rational future strategies discussed in the literature include **calpain-selective small-molecule inhibitors** and, longer-term, **allele-selective gene silencing (e.g., siRNA/ASO)** approaches, but none are in reported clinical development for this indication.

**Treatment outcomes:** Overall reported as **poor/limited** — the condition is characterized in the literature as "poorly understood," with "limited therapeutic options" and frequent treatment resistance; the fibrotic/proliferative late-stage response is often refractory to local immunosuppression.

**Treatment strategy/algorithm:** Stage-based — anti-inflammatory therapy (topical/systemic/implant) in early inflammatory stages; anti-VEGF/laser for neovascular stage; surgical (vitrectomy, membrane peel, implant revision) for fibrotic/detachment stage; genetic diagnosis is advocated to be obtained early to guide monitoring intensity and family counseling/cascade testing (Ophthalmology Advisor).

**Suggested MAXO terms:** MAXO:0000275-class "corticosteroid therapy," "immunosuppressive therapy," "anti-VEGF therapy," "vitrectomy," "laser photocoagulation," "intravitreal drug delivery implant" (exact MAXO IDs should be confirmed against the current MAXO release).

---

## 13. Prevention

- **Primary prevention:** None possible — this is a fully penetrant/high-penetrance monogenic disorder; no risk-factor modification, vaccination, or environmental intervention prevents onset.
- **Secondary prevention (early detection):** Cascade genetic testing and baseline ERG/ophthalmic exam of at-risk relatives in known *CAPN5* kindreds, enabling detection at the pre-symptomatic or early-Stage-I phase, when intervention may have the greatest chance of altering the course before fibrosis/detachment.
- **Tertiary prevention:** Aggressive, stage-appropriate management (anti-inflammatory, anti-VEGF, laser, timely vitrectomy) aims to delay progression to detachment/phthisis bulbi and to preserve residual vision as long as possible.
- **Genetic counseling:** Essential given autosomal dominant inheritance — a 50% transmission risk to offspring of an affected parent; counseling should also address the observed variable expressivity/penetrance (some carriers remain mildly affected into their 60s), and, for the R289W-type syndromic variant, the possibility of extraocular (hearing, developmental) involvement.
- **Reproductive options:** Prenatal diagnosis or preimplantation genetic testing could theoretically be offered to known carrier families given a validated familial pathogenic variant, though no report of this being performed for CAPN5-NIV was identified.
- **Public health/behavioral/immunization/prophylaxis:** Not applicable — no known modifiable environmental component.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease in other species:** No naturally occurring CAPN5-associated vitreoretinopathy has been reported in companion animals or wildlife (no OMIA entry identified in this search). This distinguishes CAPN5-NIV from human-only disease-modeling contexts.
- **Orthologous gene:** *Capn5* is conserved in mouse (MGI:1100859, Mus musculus) and zebrafish (*capn5*, Danio rerio); NCBI Gene IDs for orthologs can be retrieved from MGI/ZFIN.
- **Comparative biology:** The retinal photoreceptor expression pattern of Capn5 is conserved between human, mouse, and zebrafish, supporting cross-species mechanistic relevance despite the absence of documented spontaneous animal disease.
- **Zoonotic potential/transmission:** Not applicable — this is a non-infectious, purely genetic disease.

---

## 15. Model Organisms

**Mouse models:**
- ***Capn5* germline knockout mice:** Two independently generated null lines gave **conflicting results** — one reported viable, fertile null mice (some runted, dying ~2 months postnatally), while another reported the null allele as **pre-implantation embryonic lethal**. Critically, in the viable line, **no retinal phenotype was observed**, supporting that ADNIV pathology requires gain-of-function mutant protein rather than loss of wild-type function ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)).
- **Transgenic hCAPN5-R243L retina-targeted mice:** Lentiviral/transgenic expression of human mutant CAPN5(R243L) in mouse retina reproduces core disease features — **loss of ERG b-wave, photoreceptor degeneration, protein extravasation, vitreous inflammation, retinal fibrosis, and CD3+ T-cell/immune gene upregulation (Toll-like receptor pathway, chemokines, cytokines)** — validating this as the primary in vivo functional model of ADNIV ([PMID 25994508](https://pubmed.ncbi.nlm.nih.gov/25994508/); [PMID 24381307](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990166/)).
- **MGI resource:** Capn5, MGI:1100859.

**Zebrafish models:**
- Zebrafish *capn5* is expressed in the developing optic vesicle/embryonic brain and in newly differentiated photoreceptors, colocalizing with cone markers in the adult retina.
- *capn5* expression **increases in models of chronic rod photoreceptor degeneration/regeneration** and after **acute light damage**, localizing to surviving cones and a subset of Müller glia — leveraging zebrafish's unique capacity for retinal neuronal regeneration to study Capn5's role in degeneration/regeneration biology, a feature not available in mammalian models ([Noel et al., PMC6054427](https://pmc.ncbi.nlm.nih.gov/articles/PMC6054427/)).

**In vitro/cellular models:**
- Heterologous expression (cultured cell lines) of wild-type vs. mutant CAPN5 constructs used to demonstrate membrane-to-cytosol mislocalization and altered calcium-dependent protease activity of disease variants (R243L, L244P, K250N, R289W) ([PMID 23055945](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/); [PMID 25856303](https://pmc.ncbi.nlm.nih.gov/articles/PMC4391918/); [PMC5983175](https://pmc.ncbi.nlm.nih.gov/articles/PMC5983175/)).
- Structural/biochemical studies of the recombinant CAPN5 protease core (crystal structure, PDB 6P3Q) and C2 domain, informing mechanistic modeling of how disease mutations alter the calcium-sensing gating loop ([PMID 33811937](https://pmc.ncbi.nlm.nih.gov/articles/PMC8588747/)).

**Model limitations:** No mouse or zebrafish model fully recapitulates the chronic, multi-decade, five-stage human disease course, nor the syndromic extraocular (hearing loss/developmental delay) features of the most severe human variant (R289W); most models focus on early inflammatory/degenerative endpoints rather than the full natural history including fibrosis and phthisis bulbi.

**Research applications:** These models have been used to establish the gain-of-function/mislocalization mechanism, to characterize innate/adaptive immune activation, and represent the platform on which future therapeutic testing (e.g., calpain inhibitors, gene-silencing approaches) would likely be evaluated preclinically.

---

## Summary of Key Data Gaps

- No large-scale epidemiological registry data (formal prevalence/incidence beyond a rough ~1:1,000,000 estimate).
- No gnomAD-specific allele frequency figures were retrievable (consistent with variants being essentially private/absent from population databases).
- No published clinical trials or approved advanced therapeutics (gene therapy, targeted molecular therapy) specific to CAPN5-NIV.
- No validated disease-specific QOL instrument data (EQ-5D/SF-36).
- No documented naturally occurring veterinary/animal disease analog.
- Epigenetic and transcriptomic/metabolomic/lipidomic human data are absent from the literature; vitreous proteomics is the only human omics dataset published.

**Sources:**
- [Calpain-5 Mutations Cause Autoimmune Uveitis, Retinal Neovascularization, and Photoreceptor Degeneration (PMID 23055945)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3464205/)
- [Lymphocyte infiltration in CAPN5 ADNIV (PMID 23861576)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3704602/)
- [Structural modeling of a novel CAPN5 mutation (PMID 25856303)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4391918/)
- [CAPN5 R243L mouse model (PMID 25994508)](https://pubmed.ncbi.nlm.nih.gov/25994508/)
- [Two novel CAPN5 variants (PMID 29040051)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6711405/)
- [Proteomic insight into CAPN5-vitreoretinopathy (PMID 31110225)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527583/)
- [A novel de novo CAPN5 mutation with hearing loss/developmental delay (PMC5983175)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5983175/)
- [Phenotypic variance in Calpain-5 retinal degeneration (PMID 32274441)](https://pubmed.ncbi.nlm.nih.gov/32274441/)
- [The C2 domain of calpain 5 (PMID 33811937)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8588747/)
- [Surgical management of fibrotic encapsulation of fluocinolone implant (PMID 23785231)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3682853/)
- [ADNIV c.731T>C family cohort and literature review (PMID 37782277)](https://pubmed.ncbi.nlm.nih.gov/37782277/)
- [Functional validation of CAPN5 exome variant via lentiviral transduction (PMID 24381307)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990166/)
- [Capn5 expression in healthy/regenerating zebrafish retina (PMC6054427)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6054427/)
- [OMIM #193235 — VRNI](https://www.omim.org/entry/193235)
- [OMIM *602537 — CAPN5](https://omim.org/entry/602537)
- [EyeWiki — ADNIV](https://eyewiki.org/Autosomal_Dominant_Neovascular_Inflammatory_Vitreoretinopathy_(ADNIV))
- [NORD/GARD — CAPN5-related vitreoretinopathy](https://rarediseases.org/mondo-disease/capn5-related-vitreoretinopathy/)
- [NCBI GTR — C4721549](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4721549/)
- [CAPN5 Gene — GeneCards](https://www.genecards.org/card/CAPN5)