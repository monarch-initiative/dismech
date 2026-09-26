---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T21:40:29.494913'
end_time: '2026-08-09T21:48:06.332957'
duration_seconds: 456.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Endomyocardial Fibrosis
  mondo_id: ''
  category: Complex
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
  web_search_requests: 22
  num_turns: 43
  total_cost_usd: 2.7077648000000005
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Endomyocardial Fibrosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Endomyocardial Fibrosis** covering all of the
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

# Endomyocardial Fibrosis (EMF): Comprehensive Disease Research Report

## 1. Disease Information

**Overview.** Endomyocardial fibrosis (EMF) is a rare, insidious restrictive cardiomyopathy characterized by dense fibrous scarring of the ventricular endocardium — predominantly the inflow tracts and apices of the right and/or left ventricle — that obliterates ventricular cavity volume, tethers the atrioventricular (AV) valve subvalvular apparatus (papillary muscles and chordae tendineae) causing regurgitation, and produces severe diastolic dysfunction with markedly preserved systolic function. It is the most common cause of restrictive cardiomyopathy worldwide and is endemic to poor tropical and subtropical regions within roughly 15° of the equator (StatPearls, NBK513293; PMC4239813).

> "Subendocardial fibrosis of the apices and inflow tracts of the right ventricle, left ventricle, or both defines the disease... This restrictive scarring prevents ventricular filling, and tethering of the papillary muscles leads to valvular regurgitation." — Bukhman, Ziegler & Parry, PLoS Negl Trop Dis 2008 (PMID: 18301727)

**Key identifiers:**

| System | Identifier | Notes |
|---|---|---|
| MONDO | MONDO:0006746 | "endomyocardial fibrosis" |
| Orphanet | ORPHA:75565 | "Tropical endomyocardial fibrosis" |
| Disease Ontology | DOID:12932 | |
| ICD-10-CM | I42.3 | "Endomyocardial (eosinophilic) disease" — the ICD bucket also covers Löffler endocarditis/eosinophilic endomyocardial disease |
| MedGen | C0553980 | |
| OMIM | *No dedicated single-gene OMIM entry* | **Important disambiguation:** OMIM 226000 ("Endocardial fibroelastosis; EFE") is a **distinct disease** — a congenital/infantile endocardial thickening syndrome (often linked to ciliopathy genes, mitochondrial/carnitine defects, viral myocarditis, or as a secondary finding in obstructed left heart lesions), not to be conflated with acquired tropical/idiopathic EMF. Do not curate OMIM:226000 against MONDO:0006746. |
| HPO (phenotype) | HP:0006685 | "Endocardial fibrosis" (verify label via OAK before use) |

**Synonyms:** Davies' disease/Davies disease, tropical endomyocardial fibrosis, African endomyocardial fibrosis, endomyocardial sclerosis, obscure African cardiomyopathy, eosinophilic endomyocardial disease (when linked to Löffler/hypereosinophilic pathophysiology) (GARD; StatPearls NBK513293).

**Evidence base:** Information is derived almost entirely from **aggregated disease-level resources** — hospital case series, autopsy series, and a small number of population-based echocardiographic screening studies (notably the 2008 Mozambique study) — rather than large-scale EHR/biobank data, reflecting both the rarity of formal cohorts and the resource-limited settings where EMF is endemic.

**Sources:**
- [Endomyocardial Fibrosis - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK513293/)
- [Endomyocardial Fibrosis: Still a Mystery after 60 Years - PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0000097) (PMID: 18301727)
- [Endomyocardial fibrosis: A form of endemic restrictive cardiomyopathy - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4239813/)
- [Orphanet: Tropical endomyocardial fibrosis](https://www.orpha.net/en/disease/detail/75565)
- [GARD - Endomyocardial fibrosis](https://rarediseases.info.nih.gov/diseases/6340/endomyocardial-fibrosis)
- [OMIM 226000 - Endocardial Fibroelastosis](https://omim.org/entry/226000)

---

## 2. Etiology

EMF has **no single confirmed cause**; the current model is multifactorial, requiring convergence of infectious/immune stimuli, malnutrition, environmental exposures, and host genetic susceptibility in the context of poverty.

> "No single proposed factor can explain the occurrence of EMF worldwide." — cdt.amegroups.org review (Cardiovasc Diagn Ther)

### Disease causal factors — historically proposed hypotheses
1. **Helminth/parasite–eosinophilia hypothesis:** Filariasis, schistosomiasis, and other chronic helminthic infections drive sustained hypereosinophilia; eosinophil granule protein-mediated cardiotoxicity (see Mechanism section) is the leading mechanistic model. Ive & Brockington (Nigeria) found filariasis in **~100% of 42 angiographic EMF cases vs. 44% of 115 controls** (cited in PMID: 18301727), though the hypothesis fails to explain the absence of EMF in other high-helminth-burden regions (e.g., parts of Southeast Asia).
2. **Löffler endocarditis / hypereosinophilic syndrome (HES) equivalence:** Histological and echocardiographic comparisons (Brockington & Olsen 1975; Davies 1983) found the **fibrotic end-stage of Löffler endocarditis indistinguishable from EMF**, suggesting a shared final common pathway of eosinophil-mediated endomyocardial injury regardless of the trigger for eosinophilia (idiopathic, parasitic, or clonal/neoplastic).
3. **Nutritional/toxic hypotheses:** Cassava-based diets combined with severe protein deprivation were causally tested — feeding uncooked cassava to *Cercopithecus aethiops* (African green monkeys) produced EMF-like cardiac lesions (vs. no lesions on a banana-diet control), supporting a cassava/protein-deficiency mechanism (linked to cyanogenic glycoside/cerium toxicity). The competing "serotonin–plantain" hypothesis was tested by feeding plantains to guinea pigs, rats, and Patas monkeys but **failed to reproduce EMF lesions** and was abandoned by the 1970s (PMID: 18301727).
4. **Geochemical/toxin exposure:** Cerium and thorium in monazite-rich soils (e.g., coastal Kerala, India) have been speculatively linked to regional clustering, without confirmatory studies.
5. **Autoimmunity:** Elevated immunoglobulins and circulating **anti-myosin antibodies** (against actin, tropomyosin, and HSP-70) found in 53.6% of EMF patients vs. 10% of controls (see Genetic/Molecular section) support an autoimmune amplification loop, possibly triggered by molecular mimicry after infection (PMID: 20422043).
6. **Malaria/immune dysregulation:** Migration-associated changes in anti-malarial and anti-heart antibody titers were noted among Rwanda–Burundi migrant populations developing EMF in Uganda, though *Plasmodium* species distribution does not match EMF geography.

### Risk factors

**Genetic risk factors:**
- Familial clustering and ethnic-group concentration strongly suggest heritable susceptibility (PMID: 757895, familial EMF in Zambia).
- The only formal genetic association study to date found **HLA-B\*58** associated with EMF in Mozambique (p=0.03) and **HLA-A\*02:02** in Uganda (p=0.005) (Beaton et al., *Glob Cardiol Sci Pract* 2014, PMID: 25780800). No genome-wide association study has yet been performed or validated these findings.
- In the eosinophilic (Löffler-variant) end of the spectrum, the **FIP1L1-PDGFRA fusion gene** (constitutively active tyrosine kinase from an interstitial 4q12 deletion) drives clonal hypereosinophilia with cardiac (Löffler endocarditis/EMF-pattern) involvement in a subset of chronic eosinophilic leukemia patients — a somatic, acquired lesion rather than germline (PMC12082641, PMC10484160, PMC10217393).

**Environmental risk factors:**
- Extreme poverty, rural residence, subsistence farming, going barefoot, and cassava-based diets (Uganda case-control data cited in PMC12701864/PMID: 41399600 and PMID: 18301727).
- Chronic helminthic (filarial, schistosomal) and malarial infection burden.
- Magnesium and protein-calorie malnutrition.
- Geography: equatorial low-lying humid tropical zones — coastal Tanzania/Mozambique, southern Nigeria, Uganda, Kerala (India), Guangxi Province (China), Bahia/Colombia (South America).

**Protective factors:** No specific genetic or environmental protective factors have been formally identified in the literature; declining incidence in some hospital series has been attributed non-specifically to "improving healthcare and living standards" (PMC4239813) — i.e., socioeconomic/nutritional/parasite-control improvement rather than a defined protective exposure or allele.

**Gene–environment interactions:** The prevailing model is that HLA-conferred immune-response variability modulates the intensity/character of the host response (Th2-skewed, eosinophil/mast-cell-driven inflammation) to a chronic antigenic trigger (helminth, malarial, or nutritional/toxic) that is itself environmentally determined by poverty and geography — i.e., genetic susceptibility determines *who among the exposed* develops fibrotic disease (PMID: 25780800).

**Sources:**
- [Endomyocardial Fibrosis: Still a Mystery after 60 Years (PMID: 18301727)](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0000097)
- [Genetic susceptibility to endomyocardial fibrosis (PMID: 25780800)](https://pubmed.ncbi.nlm.nih.gov/25780800/)
- [Endomyocardial fibrosis: familial and other cases from northern Zambia (PMID: 757895)](https://pubmed.ncbi.nlm.nih.gov/757895/)
- [A Narrative Review on Endomyocardial Fibrosis (PMC12701864 / PMID: 41399600)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701864/)
- [Loeffler endocarditis revealing chronic eosinophilic leukaemia with FIP1L1-PDGFRA rearrangement (PMC12082641)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12082641/)

---

## 3. Phenotypes

EMF phenotypes span cardiac structural/functional signs, systemic congestive symptoms, hematologic/laboratory abnormalities, and constitutional findings from chronic malnutrition. Frequencies below are drawn from hospital case series (Iroegbu et al., *Cardiovasc Diagn Ther*; Mozambique population study PMID: 18596273) and should be treated as approximate/series-specific.

### Cardiac signs and symptoms
| Phenotype | Description | Suggested HPO term* |
|---|---|---|
| Restrictive diastolic dysfunction | Impaired ventricular filling despite preserved ejection fraction | HP:0001723 (restrictive cardiomyopathy) — verify |
| Endocardial fibrosis | Dense fibrous endocardial thickening at apex/inflow tract | HP:0006685 |
| Dyspnea / exertional dyspnea | Left-sided disease | HP:0002094 |
| Orthopnea | Left-sided disease | HP:0012765 — verify |
| Ascites (often disproportionate to peripheral edema) | Right-sided/biventricular disease; exudative, lymphocyte-predominant | HP:0001541 |
| Hepatomegaly / hepatosplenomegaly | Right-sided disease | HP:0002240 |
| Elevated jugular venous pressure / giant "v" waves | Tricuspid regurgitation | — |
| Mitral regurgitation | Chordal/papillary muscle tethering | HP:0001653 |
| Tricuspid regurgitation | Chordal/papillary muscle tethering | HP:0005177 |
| Atrial enlargement (biatrial) | Compensatory to restrictive ventricles | HP:0005120 — verify |
| Atrial fibrillation | Reported in ~30–40% of cases | HP:0005110 |
| Cardiac thrombus (ventricular apex, atrial) | Mural thrombus formation | — |
| Pericardial/pleural effusion | Advanced disease | HP:0002202 (pleural effusion) |
| Cardiomegaly | On CXR | HP:0001640 |
| Sudden cardiac death | Reported in pediatric series (4/55 cases, ages 1–11) | HP:0001645 — verify |

### Systemic/constitutional signs
- Exophthalmos, central cyanosis, lip/gum hyperpigmentation (distinctive but non-specific findings reported in African case series)
- Cachexia, growth stunting, malnutrition (chronic disease)
- Clubbing
- Testicular atrophy and sexual dysfunction in males (advanced chronic disease)

### Laboratory abnormalities
- Eosinophilia during the acute/inflammatory phase (variable; not present once fibrotic stage is reached)
- Hypoalbuminemia in chronic phase
- Elevated NT-proBNP/BNP and high-sensitivity troponin (disease-progression/prognostic markers, not diagnostic)
- Elevated plasma cytokines (see Mechanism section): TNF-α, IL-4, IL-10
- Circulating anti-myosin (anti-actin, anti-tropomyosin, anti-HSP70) IgG/IgM autoantibodies in a disease-activity-correlated subset (PMID: 20422043)

### Phenotype characteristics
- **Age of onset:** Bimodal — childhood peak (~first decade of life; "more than half of reported EMF cases originating in sub-Saharan Africa," per PMC12701864) and a secondary adult peak in women of childbearing age.
- **Severity/progression:** Ranges from asymptomatic/subclinical (in the Mozambique population screen, **only 22.7% of 211 EMF-positive subjects were symptomatic**, PMID: 18596273) to end-stage NYHA class III/IV heart failure. In symptomatic hospital cohorts, **62–98% present in NYHA class III/IV** (cdt.amegroups.org review; Iroegbu et al.).
- **Course:** Chronic and progressive once fibrotic; historically an acute febrile/eosinophilic myocarditic phase (Davies stage 1, up to ~5 months) precedes a subacute thrombotic stage (Davies stage 2, starting ~10 months) and finally the irreversible fibrotic stage (Davies stage 3, over years).
- **Ventricular distribution:** Biventricular ~50–55%, isolated LV ~28–40%, isolated RV ~10–28% (varies by series; NEJM Mozambique study: biventricular 55.5%, right-sided 28.0%, presumably left-sided the remainder) (PMID: 18596273).

### Quality of life impact
Formal disease-specific quality-of-life instruments (EQ-5D, SF-36) have not been reported for EMF specifically. Functional impact is inferred from NYHA class distributions — the majority of clinically ascertained (hospital-based) patients present in NYHA III/IV, i.e., marked-to-severe limitation of ordinary activity — and from the socioeconomic/constitutional burden (growth failure, cachexia, sexual dysfunction) documented in pediatric and adult case series.

*HPO term suggestions are provisional and should be verified against the ontology (label match) before curation, per standard practice.

**Sources:**
- [A population study of endomyocardial fibrosis in a rural area of Mozambique (PMID: 18596273)](https://www.nejm.org/doi/full/10.1056/NEJMoa0708629)
- [Endomyocardial fibrosis - Iroegbu (Cardiovasc Diagn Ther)](https://cdt.amegroups.org/article/view/39479/html)
- [Endomyocardial Fibrosis - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK513293/)

---

## 4. Genetic/Molecular Information

**Causal genes:** EMF (the idiopathic/tropical form) is **not a single-gene Mendelian disorder** — no causal gene has been established, and there is no dedicated OMIM phenotype entry for it (distinguishing it from OMIM:226000 endocardial fibroelastosis, a different, largely infantile/congenital disease with heterogeneous — sometimes monogenic ciliopathy-related — causes).

**Associated genetic/genomic findings:**
- **HLA-B\*58** (Mozambique) and **HLA-A\*02:02** (Uganda) — population-specific susceptibility alleles, PMID: 25780800. These require replication and are not diagnostic markers.
- **FIP1L1-PDGFRA fusion** (interstitial 4q12 deletion producing a constitutively active PDGFRA tyrosine kinase) — a somatic driver of clonal hypereosinophilic syndrome/chronic eosinophilic leukemia, a recognized cause of the Löffler-endocarditis/EMF phenotype in a subset of patients, and clinically actionable because these patients respond to **imatinib** (tyrosine kinase inhibitor) (PMC12082641, PMC10484160). This is a **somatic**, not germline, genetic lesion, relevant to a specific EMF-associated etiologic subset rather than tropical/idiopathic EMF as a whole.
- No pathogenic germline variant, chromosomal abnormality, or copy-number variant has been established as causal for classic tropical/nutritional EMF.

**Autoantibody/molecular immune findings:**
- IgG antibodies against myocardial proteins of **35 kDa (actin), 42 kDa (tropomyosin), and 70 kDa (HSP-70)** detected in 53.6% of 56 Mozambican EMF patients vs. 10% of 10 controls (p<0.05); IgM antibodies in 19.6% vs. 0%. Antibody reactivity correlated with disease activity (mean 19.6±3.7 antibodies in active disease vs. 7.1±3.3 in remission) (PMID: 20422043).

**Cytokine/molecular profiling (plasma, n=27 EMF patients vs. 38 controls, Bossa et al. 2014, PLoS ONE, DOI: 10.1371/journal.pone.0108984, PMCID: PMC4193862):**
| Cytokine | EMF patients | Controls | p-value | % positive in EMF |
|---|---|---|---|---|
| TNF-α | 2.77 ± 4.64 pg/mL | 0.94 ± 0.24 pg/mL | 0.006 | 77.7% |
| IL-4 | 4.51 ± 7.79 pg/mL | 1.22 ± 0.87 pg/mL | 0.001 | 88.8% |
| IL-10 | 4.11 ± 5.27 pg/mL | 0.99 ± 0.89 pg/mL | 0.0001 | 92.6% |
| IL-6, IFN-γ, IL-2 | Not significantly different | — | — | — |

> Interpretation: "a mixed pro- and anti-inflammatory/Th2 circulating cytokine profile" consistent with a persistent inflammatory stimulus with compensatory anti-inflammatory (Th2/IL-10) upregulation, possibly residual from prior helminthic infection.

**Epigenetic information:** No EMF-specific DNA methylation, histone modification, or chromatin studies were identified in the literature search — this is an open gap.

**Functional consequences:** Because no causal germline gene/variant is established, LOSS_OF_FUNCTION/GAIN_OF_FUNCTION functional-impact categorization does not apply to a variant in the way it would for a monogenic disease; the FIP1L1-PDGFRA subset is the clearest example of a **gain-of-function** somatic lesion (constitutive kinase activation) driving eosinophil-mediated cardiotoxicity in a specific EMF-associated etiology.

**Suggested HGNC/gene annotations (for the eosinophilic/Löffler-variant subtype only):** PDGFRA (hgnc:8803), FIP1L1 (hgnc:26845) — verify via HGNC before curation.

**Sources:**
- [Genetic susceptibility to endomyocardial fibrosis (PMID: 25780800)](https://pubmed.ncbi.nlm.nih.gov/25780800/)
- [Presence of Circulating Anti-Myosin Antibodies in Endomyocardial Fibrosis (PMID: 20422043)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2857887/)
- [Plasma Cytokine Profile in Tropical Endomyocardial Fibrosis (PMC4193862)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4193862/)
- [Loeffler endocarditis revealing chronic eosinophilic leukaemia with FIP1L1-PDGFRA rearrangement (PMC12082641)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12082641/)

---

## 5. Environmental Information

**Environmental factors:**
- Cassava (manioc) consumption combined with severe protein deprivation — experimentally reproduced EMF-like cardiac lesions in African green monkeys (*Cercopithecus aethiops*) fed uncooked cassava vs. banana-fed controls.
- Cerium/thorium exposure from monazite-rich soils (speculative, regional correlation only, e.g., coastal Kerala).
- Magnesium deficiency.

**Lifestyle/socioeconomic factors:**
- Extreme poverty; subsistence farming; going barefoot (a marker of poverty and of soil-transmitted helminth exposure) — Ugandan case-control study found associations between EMF and "markers of poverty such as farming, lack of shoes, and cassava-based diets" (PMID: 18301727).
- Rural residence in low-lying, humid, equatorial regions.
- Chronic malnutrition/protein-calorie deficiency.

**Infectious agents implicated (none proven definitively causal):**
- Helminths: filaria, *Schistosoma* spp.
- *Plasmodium* spp. (malaria) — via immune dysregulation/antibody cross-reactivity hypothesis rather than direct cardiac invasion.
- Coxsackievirus (proposed as a possible triggering acute myocarditic insult in some hypotheses).

Suggested ECTO exposure terms (to verify via OAK before curation): exposure to cassava/cyanogenic glycosides, exposure to helminth antigens, exposure to *Plasmodium falciparum* antigens, dietary protein deficiency exposure.

**Sources:** As cited in Sections 2 and 3 above (PMID: 18301727; PMC12701864/PMID: 41399600).

---

## 6. Mechanism / Pathophysiology

### Causal chain overview (from trigger to clinical manifestation)

```
Chronic antigenic/toxic stimulus (helminth infection, malaria, cassava/protein malnutrition)
   → (in genetically susceptible hosts, e.g., HLA-B*58/HLA-A*02:02)
Sustained eosinophilia / Th2-skewed immune activation (elevated IL-4, IL-10, TNF-α)
   → Eosinophil degranulation in endocardium: release of eosinophil cationic protein (ECP),
     major basic protein (MBP), eosinophil-derived neurotoxin, reactive oxygen species
   → Endothelial and myocyte injury (necrosis) — Davies Stage 1: acute eosinophilic
     (necrotic) myocarditis/endocarditis (up to ~5 months)
   → ECP-mediated activation of coagulation factors + MBP-mediated platelet activation
     → Mural thrombus formation at ventricular apex and beneath posterior mitral leaflet
       — Davies Stage 2: thrombotic stage (from ~10 months, over several years)
   → Organization of thrombus + fibroblast activation/excess collagen and ECM deposition
     → Dense acellular fibrocollagenous endocardial scar — Davies Stage 3: fibrotic
       (healed) stage
   → Endocardial fibrosis obliterates ventricular apex/inflow tract, tethers papillary
     muscles/chordae to the ventricular wall
   → Restrictive diastolic physiology + AV valve regurgitation (mitral and/or tricuspid)
   → Atrial dilation (compensatory) → atrial fibrillation, further thromboembolic risk
   → Congestive heart failure, pulmonary hypertension (left-sided disease),
     systemic venous hypertension/ascites/hepatomegaly (right-sided disease)
```

Autoimmune amplification (anti-myosin/actin/tropomyosin/HSP-70 antibodies) may perpetuate myocardial injury independent of ongoing eosinophilic infiltration, particularly in chronic/relapsing disease.

### Molecular pathways
- **Th2/eosinophil-driven inflammatory pathway:** IL-4/IL-10-skewed cytokine milieu with TNF-α co-elevation (PMC4193862).
- **PDGFRA/tyrosine kinase signaling:** constitutively activated in the FIP1L1-PDGFRA somatic-fusion subset, driving eosinophil clonal proliferation (relevant to Löffler-variant/EMF overlap).
- **Coagulation cascade activation:** eosinophil cationic protein directly activates coagulation factors, and MBP stimulates platelet activation — a distinctive eosinophil-to-thrombosis mechanistic link (JIR review, DOI: 10.2147/JIR.S458692, PMCID: PMC10984210).
- **Fibrotic/ECM pathway:** excessive fibroblast activation and collagen/extracellular-matrix deposition in the endocardial subendothelial layer (mechanistically convergent with the dismech `fibrotic_response` module pattern: tissue injury → inflammation → mesenchymal/fibroblast activation → excessive ECM → organ dysfunction).

### Cellular processes
- Eosinophil degranulation and cytotoxicity
- Endothelial injury
- Myocyte necrosis (subendocardial)
- Platelet activation and thrombus organization
- Fibroblast activation and excessive collagen synthesis (myofibroblast-like phenotype implied but not explicitly characterized at single-cell resolution in the literature reviewed)
- Chronic lymphocytic/mononuclear inflammatory infiltration (persists into the fibrotic stage in some series)
- Neovascularization within subendocardial fibrotic tissue

### Protein dysfunction / biochemical abnormalities
- Eosinophil cationic protein (ECP) and major basic protein (MBP) act as direct mediators of endothelial and myocardial cytotoxicity and of pathological coagulation activation.
- No structural protein misfolding/aggregation mechanism (distinguishing EMF from, e.g., amyloidosis, another restrictive-cardiomyopathy differential).

### Immune system involvement
Central and defining: eosinophil-mediated tissue injury (whether from reactive/secondary eosinophilia due to parasitic infection, idiopathic hypereosinophilia, or clonal/neoplastic hypereosinophilic syndrome with FIP1L1-PDGFRA), compounded by autoimmune anti-myocardial antibody production in a subset.

### Tissue damage mechanisms
Eosinophil-granule-protein cytotoxicity → necrosis → thrombosis → fibrotic scarring (a distinctive three-stage, immune-cell-initiated fibrogenesis mechanism, mechanistically related to — but histologically and etiologically distinct from — classic tissue-injury-driven fibrotic_response chains seen in organ fibrosis elsewhere in the KB).

### Molecular profiling
- **Transcriptomics/proteomics/metabolomics/lipidomics/single-cell/spatial data:** No dedicated omics datasets for human EMF cardiac tissue were identified in this search (a notable knowledge gap — EMF is markedly under-studied by modern molecular methods relative to its disease burden, largely due to being endemic in resource-limited settings without omics infrastructure).
- **Histopathology (traditional, most detailed available "molecular profiling" surrogate):**
  - Gross: atrial dilation, apical mural thrombus, reduced ventricular cavity size, AV annular dilation.
  - Microscopic: dense acellular fibrocollagenous endocardial thickening; lymphocyte-predominant infiltrate; minimal myocardial (as opposed to endocardial) tissue loss; subendocardial neovascularization; coronary vessel changes (medial sclerosis, intimal proliferation, plexiform lesions) reported in one pediatric surgical/histopathology series (mean endocardial thickness 3,000 ± 1,519 µm, maximum 5,591 µm) (cdt.amegroups.org).

### Suggested ontology terms (verify before curation)
- **GO (biological process):** GO:0030198 extracellular matrix organization; GO:0006954 inflammatory response; GO:0043534 blood vessel endothelial cell migration (angiogenesis-adjacent); collagen biosynthesis/fibril organization terms.
- **CL (cell type):** CL:0000771 eosinophil; CL:0000057 fibroblast; CL:0000097 mast cell; CL:0000236 (B cell, for autoantibody production context).
- **UBERON:** UBERON:0002348 endocardium; UBERON:0002080 right ventricle; UBERON:0002084 left ventricle; cardiac papillary muscle and chordae tendineae terms.
- **CHEBI:** eosinophil cationic protein / RNase 3 and major basic protein are proteins rather than small molecules — represent via UniProt/gene rather than CHEBI.

**Sources:**
- [In-Depth Review of Loeffler Endocarditis: What Have We Learned? (PMC10984210)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10984210/)
- [Endomyocardial fibrosis - Iroegbu (Cardiovasc Diagn Ther)](https://cdt.amegroups.org/article/view/39479/html)
- [The cardiotoxicity of eosinophils (PMC2417450)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2417450/)
- [Plasma Cytokine Profile in Tropical Endomyocardial Fibrosis (PMC4193862)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4193862/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart — right ventricle, left ventricle (either alone or, most commonly, biventricular), atrioventricular valves (mitral, tricuspid), atria (secondary dilation).
- **Secondary/complication-driven:** Liver (congestive hepatomegaly), spleen (splenomegaly), lungs (pulmonary hypertension, pleural effusion, pulmonary congestion in left-sided disease), peritoneum (ascites — notably exudative/lymphocytic, suggesting a degree of peritoneal inflammatory involvement rather than pure transudative congestion), coronary vasculature (secondary sclerotic/proliferative changes reported in some histopathologic series).
- **Body systems:** Cardiovascular (primary); hepatic, pulmonary, and hematologic (thromboembolic) systems secondarily.

**Tissue/cell level:**
- Endocardium (subendothelial layer) — primary site of fibrous deposition.
- Myocardium — subendocardial injury; relatively spared compared to endocardium.
- Cell populations: eosinophils (infiltrating), fibroblasts (activated, ECM-producing), lymphocytes/mononuclear cells (chronic infiltrate), endothelial cells (injured), platelets (thrombus formation).

**Subcellular level:** No specific organelle-level pathology (e.g., mitochondrial, ER) has been characterized as central to EMF pathogenesis in the literature reviewed; this contrasts with some other cardiomyopathies (e.g., storage/metabolic cardiomyopathies) and represents a gap.

**Localization:**
- Apex and inflow tract predominate (both ventricles can be affected).
- **Right ventricle:** trabecular cavity obliteration, apical retraction, tricuspid valve tethering.
- **Left ventricle:** apical obliteration (rounded "obliterated apex" morphology on echo), posterior mitral leaflet/chordal involvement (fibrosis characteristically engulfs the posterior mitral leaflet).
- **Laterality:** Right-sided, left-sided, or biventricular — biventricular is the most common pattern (~50–55% in major series).

**Sources:** As cited above (StatPearls NBK513293; PMC4239813; PMID: 18596273).

---

## 8. Temporal Development

**Onset:**
- Typically pediatric/adolescent onset (more than half of reported cases arise in the first decade of life), with a secondary adult-onset peak in women of childbearing age. Onset pattern is classically an insidious acute febrile illness (facial swelling, pruritus, eosinophilia) that may be mistaken for viral myocarditis or acute rheumatic fever, though many cases are only detected later in the fibrotic/chronic stage, or incidentally via echocardiographic screening (subclinical disease).

**Progression — Davies three-stage model:**
1. **Acute (necrotic) stage** — up to ~5 months; eosinophilic myocarditis with subendocardial necrosis; may present as fulminant heart failure/cardiogenic shock or be entirely asymptomatic/missed.
2. **Thrombotic (intermediate/subacute) stage** — beginning ~10 months post-onset, lasting several years; mural thrombus formation at the apex and behind the posterior mitral leaflet.
3. **Fibrotic (chronic/healed) stage** — the stage at which most patients present clinically; endocardium replaced by dense collagenous scar; restrictive physiology and valvular regurgitation dominate the clinical picture. This stage is essentially irreversible.

**Rate/course:** Variable — can be relatively indolent (subclinical disease detected on population screening, as in 77% of the Mozambique EMF-positive cohort) or rapidly progressive to severe heart failure and death. Once in the fibrotic stage, the disease course is chronic and progressive, without spontaneous remission; medical therapy does not appreciably alter the underlying fibrotic process (StatPearls NBK513293; a randomized placebo-controlled trial of prednisolone in Uganda found no significant benefit in preventing ascites reaccumulation, PMCID: PMC4678569 — see Treatment section).

**Critical periods:** The acute eosinophilic/necrotic stage represents the theoretical intervention window before irreversible fibrosis sets in (rationale for anti-eosinophilic/immunosuppressive therapy trials), but this stage is rarely captured clinically because of its nonspecific presentation and the resource constraints of endemic settings.

**Sources:**
- [Endomyocardial Fibrosis: Diagnosis and Management (Dove Press / JVD)](https://www.dovepress.com/endomyocardial-fibrosis-diagnosis-and-management-peer-reviewed-fulltext-article-JVD)
- [A population study of endomyocardial fibrosis in a rural area of Mozambique (PMID: 18596273)](https://www.nejm.org/doi/full/10.1056/NEJMoa0708629)
- [The safety and efficacy of prednisolone... (PMC4678569)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4678569/)

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** The only rigorous population-based echocardiographic screening study (rural Mozambique, n=1,063, all ages, PMID: 18596273) found an **overall prevalence of 19.8%** (211/1,063; 95% CI 17.4–22.2), highest in ages 10–19 (28.1%), and higher in males than females (23.0% vs. 17.5%, p=0.03) — a strikingly high figure reflecting substantial subclinical/mild disease burden not captured by hospital-based series. Note this is markedly higher than clinically ascertained hospital prevalence figures and reflects a broad echocardiographic case definition including mild disease.
- Hospital-based series report EMF as accounting for **up to ~20% of heart-failure/echocardiography referrals** in endemic African centers (e.g., Kampala) and as the **4th most common cause of adult cardiac disease** in some equatorial African nations.
- One review cites a global burden estimate of **~12 million affected persons**, predominantly in sub-Saharan Africa (cdt.amegroups.org) — this figure should be treated cautiously given the absence of large-scale multinational surveillance; it likely derives from extrapolation of regional prevalence data (such as the Mozambique 19.8% figure) rather than direct enumeration.
- Historical literature documents **>2,400 published cases worldwide**, ~50% from sub-Saharan Africa and ~25% from Uganda alone (PMID: 18301727) — though this reflects publication/ascertainment bias rather than true incidence.
- Hospital-series incidence appears to be **declining** over recent decades, plausibly linked to improved nutrition, parasite control, and healthcare access, though this has not been rigorously quantified prospectively.

**Inheritance pattern:** Not Mendelian — EMF is a complex/multifactorial disease. No autosomal dominant/recessive/X-linked/mitochondrial pattern has been established. Familial clustering (PMID: 757895) and HLA associations (PMID: 25780800) support polygenic/complex susceptibility rather than single-gene inheritance. Penetrance, expressivity, anticipation, germline mosaicism, and founder-effect concepts are therefore not directly applicable in the Mendelian sense; however, the HLA-B\*58 and HLA-A\*02:02 associations function analogously to susceptibility-locus "carrier frequency" concepts and would require population-specific allele-frequency data (not identified in this search) to quantify.

**Population demographics:**
- **Geographic distribution:** Endemic — sub-Saharan Africa (Uganda, Mozambique, Nigeria, Cameroon, Congo, Malawi, Zambia most represented), South Asia (Kerala, India), East Asia (Guangxi Province, China), South America (Bahia, Brazil; Colombia). Rare sporadic cases reported in non-endemic/Western populations (e.g., a Western European case report, PMC7319822).
- **Sex ratio:** Roughly equal in childhood-onset disease; adult-onset disease reported to affect women roughly twice as often as men in some series (though the Mozambique population screen found higher male prevalence overall — sex-ratio findings are series-dependent and possibly stage/age-dependent).
- **Age distribution:** Bimodal — childhood/adolescent peak and adult (childbearing-age women) peak.
- **Socioeconomic gradient:** Strongly associated with poverty; a recognized "neglected disease of poverty."

**Sources:**
- [A population study of endomyocardial fibrosis in a rural area of Mozambique (PMID: 18596273)](https://www.nejm.org/doi/full/10.1056/NEJMoa0708629)
- [Endomyocardial Fibrosis: Still a Mystery after 60 Years (PMID: 18301727)](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0000097)
- [Endomyocardial fibrosis - Iroegbu (Cardiovasc Diagn Ther)](https://cdt.amegroups.org/article/view/39479/html)
- [Idiopathic endomyocardial fibrosis in a Western European: a case report (PMC7319822)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7319822/)

---

## 10. Diagnostics

**Clinical laboratory tests:** No definitive/diagnostic blood test exists. Eosinophilia may be present in the acute inflammatory phase but is often absent by the fibrotic stage. Hypoalbuminemia is common in chronic disease. Elevated NT-proBNP/BNP and high-sensitivity troponin correlate with disease severity/progression and prognosis but are non-specific.

**Electrocardiography:** Low-voltage QRS, nonspecific ST-/T-wave abnormalities, AV block, bundle branch block, left/biatrial enlargement patterns.

**Chest radiography:** Cardiomegaly, atrial enlargement, pulmonary vascular congestion, occasional endomyocardial calcification, pleural/pericardial effusion.

**Echocardiography — the primary diagnostic modality.** Key structural findings: apical cavity obliteration (right and/or left ventricle), "mushroom sign" apical distortion, dense endocardial echogenicity, mural thrombus/spontaneous contrast, AV valve tethering with regurgitation, biatrial enlargement, restrictive (dip-and-plateau) diastolic filling pattern (short deceleration time, shortened isovolumic relaxation time). Left-ventriculography analog: apical obliteration; M-mode may show a distinctive "M-shaped" septal motion pattern.

**Diagnostic scoring systems (Mocumbi criteria):**
- **Definite diagnosis** requires **2 major criteria, or 1 major + 2 minor criteria.**
- *Major criteria:* obliteration of the RV or LV apex; thrombi or spontaneous contrast without severe global ventricular dysfunction; retraction of the RV apex; AV valve dysfunction from adhesion of the valve apparatus to the ventricular wall.
- *Minor criteria:* restrictive mitral/tricuspid inflow pattern; pulmonary valve diastolic opening; enlarged atrium with normal-sized ventricle.
- A quantitative **severity score** (weighted per criterion) stratifies disease as **mild (<8), moderate (8–15), severe (>15)** in the original Mocumbi formulation; a related pediatric grading (4–6 mild, 7–9 moderate, 10–12 severe) has also been reported in a separate series (cdt.amegroups.org), indicating some variation in scoring implementations across studies — the exact cut-points should be verified against the primary source before formal curation.

**Cardiac MRI:** More sensitive than echocardiography for detecting intracardiac thrombus and for early/subclinical disease; late gadolinium enhancement (LGE) shows continuous subendocardial enhancement from subvalvular regions to the apex ("double V" / "three-layered" sign), correlating with histopathologic fibrosis. LGE-quantified fibrosis volume has been reported as an **independent predictor of mortality** (PMC12701864/PMID: 41399600). MRI is valuable for preoperative planning and treatment-response monitoring.

**Myocardial contrast echocardiography (MCE):** Adjunctive tool for apical obliteration/thrombus detection when conventional imaging is limited.

**Cardiac catheterization:** Rarely required now; shows a classic restrictive "dip-and-plateau" ventricular pressure pattern; angiography demonstrates apical cavity obliteration.

**Endomyocardial biopsy:** Can demonstrate subendocardial fibrosis and thrombus, but limited utility due to patchy distribution of fibrosis and procedural risk (risk of thrombus dislodgement/embolization in a fibrotic, thrombus-laden ventricle).

**Genetic testing:** Not part of the standard diagnostic pathway for classic tropical/idiopathic EMF (no established causal gene). For suspected hypereosinophilic-syndrome-driven (Löffler/eosinophilic) EMF, **FIP1L1-PDGFRA fusion testing** (FISH or RT-PCR) is clinically actionable, as fusion-positive patients respond to imatinib.

**Clinical criteria / differential diagnosis:** Key differentials include viral myocarditis (acute stage), cardiac amyloidosis, cardiac sarcoidosis, dilated cardiomyopathy, left ventricular noncompaction, carcinoid heart disease, anthracycline cardiotoxicity, constrictive pericarditis, and radiation-induced cardiomyopathy — all part of the broader restrictive-cardiomyopathy/heart-failure-with-preserved-EF differential.

**Screening:** No formal national/international newborn or population screening program exists. The single major population-based echocardiographic prevalence survey (Mozambique, PMID: 18596273) demonstrates the feasibility and yield of community echocardiographic screening in endemic areas but has not been scaled into a routine screening program.

**Sources:**
- [Endomyocardial Fibrosis - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK513293/)
- [A Narrative Review on Endomyocardial Fibrosis (PMC12701864 / PMID: 41399600)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701864/)
- [Endomyocardial fibrosis - Iroegbu (Cardiovasc Diagn Ther)](https://cdt.amegroups.org/article/view/39479/html)
- [Left ventricle endomyocardial fibrosis: a case report (PMC10422788)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10422788/)

---

## 11. Outcome/Prognosis

**Survival/mortality (untreated/medically managed):**
- Historical Ugandan autopsy series (1959–1969): **average survival ~2 years after symptom onset.**
- Broadly cited figure: **"75% mortality within 2 years" / "one-third to one-half of patients with advanced disease dying within 2 years"** with medical management alone (figures vary by series and disease-stage-at-presentation).
- Atrial fibrillation is associated with worse prognosis.

**Surgical outcomes:**
- **Operative (30-day) mortality: ~15–21.7%** across major surgical series; one series reported 21.7% 30-day mortality plus 13% late mortality within the first 2 postoperative years.
- **Life-table survival including operative mortality:** ~67% at 2 years, ~55–68% at up to 17 years in selected surgical cohorts; a more recent Mozambican surgical series reported ~76.5% 5-year survival with 70.9% of operated patients showing functional improvement.
- **Recurrence:** Fibrosis recurrence requiring reoperation in ~4–18.8% of surgical patients across series; EMF appearing in the previously unaffected contralateral ventricle in ~8.8% in one series.
- Surgery is explicitly regarded as **palliative** — it corrects structural/valvular consequences but does not alter the underlying fibrotic disease process, and recurrence is well documented.

**Morbidity/functional outcomes:**
- The majority of clinically ascertained (hospital-referred) patients present in **NYHA class III/IV** (62–98% across cited series).
- Postoperative functional improvement is achievable in a substantial subset (e.g., 70.9% improved in one series; younger/less advanced patients achieving NYHA I–II postoperatively in a pediatric series), but a meaningful minority show no improvement or clinical deterioration.
- Complications: heart failure, atrial fibrillation, AV block, thromboembolism (stroke, pulmonary embolism), progressive valvular dysfunction, pulmonary hypertension, infective endocarditis susceptibility, pericardial effusion, sudden cardiac death.

**Prognostic factors/biomarkers:** Advanced diastolic dysfunction, severe atrial enlargement, biventricular involvement, extensive fibrosis/thrombus burden on cardiac MRI, elevated NT-proBNP, and pulmonary hypertension are cited as predictors of poor outcome; **LGE-quantified fibrosis volume on cardiac MRI independently predicts mortality** (PMC12701864/PMID: 41399600).

**Sources:**
- [Endomyocardial fibrosis: Early and late results of surgery in 20 patients](https://www.sciencedirect.com/science/article/pii/S0022522319373246)
- [Surgery for endomyocardial fibrosis revisited (Eur J Cardiothorac Surg)](https://academic.oup.com/ejcts/article/15/3/309/455350)
- [Endomyocardial fibrosis - Iroegbu (Cardiovasc Diagn Ther)](https://cdt.amegroups.org/article/view/39479/html)
- [A Narrative Review on Endomyocardial Fibrosis (PMC12701864 / PMID: 41399600)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701864/)

---

## 12. Treatment

**Pharmacotherapy (symptomatic/supportive; no disease-modifying drug established):**
- **Diuretics** (loop diuretics — furosemide, torasemide) for congestive symptoms (NCIT candidate: Pharmacotherapy NCIT:C15986; specific class terms to be verified).
- **ACE inhibitors and beta-blockers** — standard heart-failure adjuncts, though restrictive physiology limits their hemodynamic benefit relative to dilated cardiomyopathy.
- **Anticoagulation** (warfarin; direct oral anticoagulants limited by cost/access in endemic settings) for documented intracardiac thrombus/atrial fibrillation.
- **Corticosteroids (prednisolone):** Tested in a double-blind, randomized, placebo-controlled trial in Uganda (n=35; 1 mg/kg/day, max 60 mg) for prevention of ascites reaccumulation in EMF: **primary outcome (progression to grade 3 ascites) occurred in 60% of prednisolone-treated vs. 86% of placebo-treated patients (RR 0.70, 95% CI 0.43–1.11, p=0.12) — not statistically significant**, though the drug was safe (PMCID: PMC4678569). This is the only identified randomized controlled trial of a disease-directed medical therapy in EMF and represents a key piece of negative-evidence for immunosuppressive intervention at the (typically late) disease stage studied.
- **Rate/rhythm control** (beta-blockers, digoxin) for atrial fibrillation.

**Advanced/targeted therapeutics (for the eosinophilic/Löffler-variant subset specifically):**
- **Imatinib** (tyrosine kinase inhibitor) — first-line for FIP1L1-PDGFRA-fusion-positive hypereosinophilic syndrome/Löffler endocarditis; achieves eosinophil normalization and echocardiographic improvement.
- **Mepolizumab** (anti-IL-5 monoclonal antibody) — used as an eosinophil-targeting immunomodulator in HES/Löffler endocarditis, though evidence specific to established fibrotic EMF is limited (most benefit expected in the pre-fibrotic/acute eosinophilic stage).
- **Interferon-alfa** — reported for corticosteroid/imatinib-resistant HES-associated cardiac disease.

**Surgical/interventional:**
- **Endocardiectomy (endocardial decortication)** ± mitral and/or tricuspid valve repair or replacement, typically via median sternotomy with cardiopulmonary bypass — the mainstay definitive intervention for NYHA III/IV disease. NCIT candidates: Surgical Procedure (NCIT:C15329), Orthopedic Surgical Procedure not applicable; a cardiac-surgery-specific NCIT term should be verified.
- **Cavopulmonary connection (Fontan-type)** procedures have been proposed as beneficial adjuncts for severe right-ventricular EMF in some case reports.
- **Heart transplantation:** Not an established/first-line therapy (StatPearls notes "no established benefit"), but case reports document successful outcomes — e.g., a patient with FIP1L1-PDGFRA-associated EMF alive and asymptomatic 5 years post-transplant, and a case report describing 2-year good graft function with vigilance for possible disease recurrence in the allograft (PMCID: PMC12046388) — an important, still poorly characterized risk given EMF's presumed ongoing systemic (immune/eosinophilic) driver.

**Experimental/investigational:** No disease-specific investigational agents in active clinical trials for classic tropical EMF were identified; research priorities (per PMID: 18301727) include measuring inflammatory markers (CRP, TNF-α), studying FIP1L1-PDGFRA prevalence in broader EMF cohorts, examining serotonin receptor polymorphisms, and conducting further population-based echocardiographic surveys.

**Treatment outcomes:** See Prognosis section — surgical endocardiectomy is the most effective available intervention but carries substantial operative mortality (~15–22%) and disease recurrence risk (~4–19%); medical therapy alone does not appear to alter the natural history of established fibrotic disease (per the negative prednisolone RCT).

**Treatment strategy/algorithm:** Stage-dependent — acute eosinophilic myocarditis phase (if captured) may warrant corticosteroids ± eosinophil-targeted therapy (imatinib if FIP1L1-PDGFRA+, mepolizumab); established fibrotic-stage disease is managed with heart-failure pharmacotherapy and anticoagulation, escalating to endocardiectomy ± valve surgery for NYHA III/IV symptoms refractory to medical therapy; heart transplantation is reserved for exceptional cases.

**Sources:**
- [The safety and efficacy of prednisolone in preventing reaccumulation of ascites among EMF patients in Uganda (PMC4678569)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4678569/)
- [In-Depth Review of Loeffler Endocarditis (PMC10984210)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10984210/)
- [Case report on heart transplantation in endomyocardial fibrosis (PMC12046388)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12046388/)
- [Successful Heart Transplantation for Unreversible EMF Related to FIP1L1-PDGFRA CEL](https://journals.lww.com/transplantjournal/fulltext/10.1097/tp.0000000000000939~successful-heart-transplantation-for-unreversible)
- [Endomyocardial Fibrosis Treatment & Management (Medscape)](https://emedicine.medscape.com/article/154931-treatment)

---

## 13. Prevention

**Primary prevention:** No disease-specific primary prevention strategy is established. Given the etiologic hypotheses, plausible (but not formally trial-proven for EMF-incidence reduction) primary-prevention levers include:
- Population deworming and helminth/schistosomiasis control programs in endemic regions.
- Nutritional interventions addressing protein-calorie and micronutrient (magnesium) deficiency and reducing dependence on inadequately processed cassava.
- Malaria control.
- Poverty alleviation (the strongest and most consistently identified structural risk factor).

Notably, no clinical trial has directly tested whether these interventions reduce EMF incidence; the rationale is inferential from the epidemiologic/mechanistic associations discussed above.

**Secondary prevention (early detection):** Community echocardiographic screening, as piloted in the Mozambique population study, could theoretically identify subclinical/mild disease (the ~77% of prevalent cases who were asymptomatic in that study) for closer monitoring, though no screening program has been operationalized at scale, and there is no proven early intervention that alters the natural history once fibrosis is detected.

**Tertiary prevention:** Standard heart-failure medical management, anticoagulation to prevent thromboembolic complications, and timely surgical referral (endocardiectomy ± valve surgery) before end-stage/refractory heart failure develops.

**Immunization:** Not applicable — no vaccine-preventable causal agent has been established.

**Genetic counseling:** Not applicable in the conventional Mendelian sense given the complex/multifactorial and non-Mendelian inheritance pattern; family history (given documented familial clustering) may still warrant clinical/echocardiographic surveillance of relatives in high-risk families, though this is not a formalized guideline recommendation identified in the literature.

**Public health interventions:** Improved sanitation and vector/parasite control (reducing helminth and malarial burden), nutritional support programs, and expanded access to echocardiography in endemic primary-care settings are the most plausible public-health levers, consistent with the observed decline in hospital-based EMF incidence attributed generally to "improving healthcare and living standards."

**Sources:** As cited above (PMID: 18301727; PMC12701864/PMID: 41399600; PMC4239813).

---

## 14. Other Species / Natural Disease

**Taxonomy:** Naturally occurring EMF as described here is a **human disease**; there is no well-established veterinary/naturally occurring analog reported in companion animals or wildlife in the literature reviewed.

**Experimental (induced, non-natural) models:**
- ***Cercopithecus aethiops*** (African green monkey; NCBI Taxon ID needed/verify) fed a cassava-based, severe-protein-deficient diet developed cardiac lesions resembling human EMF, while banana-fed controls did not — supporting the cassava/protein-deficiency causal hypothesis (cited in PMID: 18301727).
- Plantain-feeding experiments in **guinea pigs, rats, and Patas monkeys** (testing the serotonin hypothesis) **failed to reproduce EMF lesions**, effectively refuting that hypothesis (PMID: 18301727).

**Comparative biology:** No dedicated comparative pathology or evolutionary-conservation literature on EMF mechanisms across species was identified. The eosinophil-mediated cardiotoxicity mechanism (ECP/MBP-driven endothelial injury and coagulation activation) is presumed broadly conserved across mammals based on general eosinophil biology, but this has not been formally studied in the specific context of EMF model development.

**Zoonotic potential / transmission:** Not applicable — EMF is not an infectious/transmissible disease itself, though proposed infectious co-factors (helminths, *Plasmodium*) are separately zoonotic/vector-borne in their own right.

**Note on a distinct but nomenclature-adjacent condition:** Endocardial fibroelastosis (EFE, OMIM:226000) — a different, largely pediatric/congenital disease — has documented animal models (e.g., distention of the immature left ventricle inducing EFE-like lesions, PMC4433646) and, in some human cases, a ciliopathy-gene basis (e.g., in Alström syndrome, PMC8541947). These EFE-specific models and genetic findings should **not** be conflated with tropical/idiopathic EMF model organism data.

**Sources:**
- [Endomyocardial Fibrosis: Still a Mystery after 60 Years (PMID: 18301727)](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0000097)
- [Distention of the Immature Left Ventricle Triggers Development of Endocardial Fibroelastosis (PMC4433646)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4433646/) (EFE model — distinct disease, included for disambiguation only)

---

## 15. Model Organisms

**Summary:** Model-organism research specific to tropical/idiopathic EMF is **sparse and largely historical**, reflecting both the disease's endemic-region concentration (limiting research infrastructure) and the field's general stagnation after the 1980s (publication volume "declined dramatically post-1980s," peaking "prior to the diffusion of echocardiography in much of the tropics," per PMID: 18301727).

**Genetic/induced models identified:**
- **Cassava/protein-deprivation model (non-human primate):** *Cercopithecus aethiops* fed uncooked cassava under severe protein restriction — produced cardiac histopathology resembling human EMF, plus hepatic changes resembling tropical splenomegaly syndrome, supporting a shared cassava/malnutrition etiology for both conditions. This model **did** partially recapitulate the human phenotype but has not been followed up with modern molecular characterization.
- **Serotonin/plantain hypothesis models (guinea pig, rat, Patas monkey):** Failed to reproduce EMF lesions — a **negative** model result that helped rule out the serotonin-metabolite hypothesis.
- **No genetically engineered (knockout/knock-in/transgenic/conditional/humanized) mouse or other rodent model of EMF** was identified in this search — a clear gap, likely attributable to the absence of an established causal gene to target.
- **FIP1L1-PDGFRA / hypereosinophilic syndrome models:** General HES/eosinophilic-cardiotoxicity models (e.g., IL-5 transgenic or eosinophil-adoptive-transfer mouse models used in broader eosinophilic-disease research) exist in the eosinophil biology literature but were not specifically identified as validated EMF models in this search; they represent the most plausible near-term modeling avenue given the shared mechanism with Löffler endocarditis.

**Model limitations:** No model captures the full multifactorial human EMF phenotype (chronic malnutrition + parasitic/immune exposure + genetic susceptibility + years-long fibrotic evolution); the primate cassava model is the closest histopathologic recapitulation identified but is decades old, ethically and logistically difficult to repeat with modern techniques, and was not molecularly characterized by contemporary standards (no transcriptomic/proteomic follow-up reported).

**Applications:** Existing models have been used primarily to test/refute specific etiologic hypotheses (cassava/protein deficiency: supported; serotonin/plantain: refuted) rather than to dissect molecular pathogenesis or screen therapeutics — an important direction the 2025 Nature Reviews Cardiology review (Mocumbi et al., DOI: 10.1038/s41569-025-01138-x) explicitly flags as a priority for identifying preclinical biomarkers and novel therapeutic targets, though full-text access to that review's specific model-organism recommendations could not be retrieved in this session (paywalled).

**Resources:** No dedicated EMF model-organism database or repository was identified (unlike diseases with established genetic models catalogued in MGI/IMPC/ZFIN); this itself is a notable research-infrastructure gap for EMF.

**Sources:**
- [Endomyocardial Fibrosis: Still a Mystery after 60 Years (PMID: 18301727)](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0000097)
- [Endomyocardial fibrosis: recent advances and future therapeutic targets (Nat Rev Cardiol 2025)](https://www.nature.com/articles/s41569-025-01138-x) — abstract/metadata only accessible (paywalled); Mocumbi et al., *Nat Rev Cardiol* 2025;22(8):564–576.

---

## Summary of Key Knowledge Gaps (for curation planning)

1. **No established causal gene** — EMF is genetically complex, not monogenic; avoid asserting a causal gene/OMIM entry (OMIM:226000 belongs to the distinct disease EFE, not EMF).
2. **HLA associations (HLA-B\*58, HLA-A\*02:02) are single-study, population-specific, and unreplicated** — should be curated as SUSCEPTIBILITY-level evidence with appropriately guarded confidence, not as established risk alleles.
3. **The etiologic model remains a multifactorial hypothesis, not a proven causal chain** — the eosinophil/Löffler-equivalence mechanism has the strongest histopathologic support, but "no single proposed factor can explain the occurrence of EMF worldwide" per the primary review literature.
4. **No RCT-proven disease-modifying medical therapy exists** — the one identified RCT (prednisolone for ascites) was negative; this is important, citable negative evidence.
5. **FIP1L1-PDGFRA/imatinib pathway is a distinct, actionable, but etiologically separate subset** (clonal hypereosinophilic syndrome/Löffler-variant EMF) — should likely be modeled as a related but distinct causal branch/subtype rather than conflated with classic nutritional/parasitic tropical EMF.
6. **Modern omics data (transcriptomic, proteomic, single-cell) for human EMF cardiac tissue are essentially absent** from the literature surveyed — a genuine research and knowledge-base gap.
7. **Global prevalence/burden estimates (e.g., "~12 million") are poorly sourced/extrapolated** and should be cited cautiously with the underlying Mozambique 19.8% population-prevalence study (PMID: 18596273) as the strongest primary anchor.
8. Full text of the most current comprehensive review (Mocumbi et al., *Nat Rev Cardiol* 2025) was **paywalled and not fully accessible** in this session — recommend independent retrieval for the most up-to-date synthesis before finalizing a knowledge-base entry.