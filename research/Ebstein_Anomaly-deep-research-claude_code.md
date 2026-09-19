---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T03:34:18.029001'
end_time: '2026-08-09T03:38:14.762322'
duration_seconds: 236.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ebstein Anomaly
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
  web_search_requests: 10
  num_turns: 12
  total_cost_usd: 1.4722792
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ebstein Anomaly
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ebstein Anomaly** covering all of the
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

# Ebstein Anomaly — Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Ebstein anomaly (EA) is a rare, congenital malformation of the tricuspid valve and right ventricle. The defining lesion is apical (downward) displacement of the functional tricuspid annulus into the right ventricle, caused by failure of delamination of the septal and posterior (inferior) leaflets from the underlying myocardium during valvulogenesis. This produces "atrialization" of the inlet portion of the right ventricle (the RV segment proximal to the displaced valve becomes thin-walled and functions as an extension of the right atrium), a redundant and often abnormally attached anterior/anterosuperior leaflet, a functionally smaller (distal) true right ventricle, tricuspid regurgitation, and right atrial enlargement. Severity ranges from mild (incidental, adult-diagnosed) to severe forms presenting with massive cardiomegaly and circulatory failure in the fetus/neonate ("Ebstein's anomaly-like" fetal hydrops).

**Key identifiers:**
- **OMIM:** 224700 (EBSTEIN ANOMALY) — https://omim.org/entry/224700
- **Orphanet:** ORPHA:1880 (Ebstein malformation of the tricuspid valve)
- **MONDO:** MONDO:0009144
- **ICD-10:** Q22.5 (Ebstein's anomaly)
- **ICD-11:** LA61.0 (or equivalent congenital tricuspid malformation code)
- **MeSH:** D004437 (Ebstein Anomaly)
- **HPO (as a phenotype/malformation term):** HP:0010316 (Ebstein anomaly)

**Synonyms/alternative names:** Ebstein's anomaly; Ebstein malformation of the tricuspid valve; Ebstein's disease; tricuspid valve atrialization; downward displacement of the tricuspid valve.

**Evidence base character:** Much of the mechanistic and epidemiologic literature is aggregated disease-level data — population birth-defect registries (e.g., National Birth Defects Prevention Study, Danish/Swedish national registries), multicenter surgical/echocardiographic case series, and candidate-gene/exome cohorts — rather than individual-patient EHR mining, though single-center EHR-derived case series (e.g., fetal echocardiographic cohorts, CICU admission cohorts) also contribute.

---

## 2. Etiology

### Disease Causal Factors
EA is etiologically heterogeneous: the majority of cases are **sporadic**, with a minority attributable to identifiable monogenic causes (sarcomeric gene mutations), chromosomal microdeletions, or **teratogenic exposure** (notably lithium). The unifying developmental mechanism is failure of normal delamination/apoptotic remodeling of the septal and inferior tricuspid leaflets from the ventricular myocardium during valvulogenesis (roughly weeks 9–16 of human gestation), leaving the leaflets tethered directly to endocardium/myocardium rather than forming discrete mobile leaflets tethered by chordae to papillary muscles.

### Genetic Risk Factors
- **MYH7** (β-myosin heavy chain, sarcomere gene; 14q11.2): Heterozygous MYH7 mutations were identified in 8/141 (6%) unrelated EA probands in a next-generation/Sanger sequencing cohort, with 7 distinct mutations (5 novel, 2 previously known HCM-causing variants). This defines an autosomal-dominant subtype of EA associated with **left ventricular noncompaction (LVNC)**. (PMID:21604106 — "Ebstein's anomaly may be caused by mutations in the sarcomere protein gene MYH7"; PMID:23794396 — familial EA + LVNC autosomal dominant, MYH7; PMID:25444217 — familial EA, LVNC, and VSD with MYH7 mutation.)
- **NKX2-5** and **GATA4**: Candidate transcription-factor genes implicated in isolated and familial EA and broader congenital heart disease (CHD); GATA4 also implicated via **8p23.1 microdeletion** (PMID:21815254 — "Ebstein anomaly: Genetic heterogeneity and association with microdeletions 1p36 and 8p23.1"). NKX2-5/GATA4/TBX5 act combinatorially in cardiac septation/valvulogenesis gene regulatory networks.
- **Chromosomal microdeletions**: 1p36 deletion syndrome and 8p23.1 deletion syndrome are recurrently associated with EA or EA-like tricuspid valve malformation.
- **Exome/targeted-panel studies**: A 47-case EA cohort sequenced for 50 candidate genes (including NKX2-5, GATA4, MYH7) implicated myocardial-development pathway genes (PLOS ONE, PMID not directly captured — "Genetic Variants in Isolated Ebstein Anomaly Implicated in Myocardial Development Pathways").
- Most sporadic EA is **not** explained by a single identified gene; recurrence risk in siblings of an isolated case is low (empirically ~1%), consistent with predominantly sporadic/multifactorial causation, with monogenic causes concentrated in familial or syndromic clusters (especially the MYH7/LVNC subtype).

### Environmental Risk Factors
- **Lithium** (maternal first-trimester exposure): Historically implicated with a very high relative risk (~400) based on voluntary case-registry data from the 1970s, now understood to be a substantial overestimate. Contemporary controlled studies (case-control and cohort, including the large NEJM cohort, PMID:28591541 — Lithium Use in Pregnancy and the Risk of Cardiac Malformations) show a **modest** increase in cardiac-malformation risk with first-trimester lithium exposure, disproportionately affecting right-ventricular-outflow/tricuspid lesions (most likely EA); absolute risk of EA specifically is estimated at roughly 1–2 per 1000 (0.1–0.2%) with exposure, versus ~1 in 20,000 baseline. Risk appears dose-dependent, increasing above ~900 mg/day lithium.
- Other implicated teratogens/exposures (less strongly supported, from the National Birth Defects Prevention Study, PMID: PMC6711372 — "Potential risk factors for Ebstein anomaly"): benzodiazepine use, certain maternal illnesses/exposures during the periconceptional period; findings are exploratory given the rarity of the defect and generally require replication.
- Maternal diabetes and other general CHD risk factors have been examined but are not specifically or strongly linked to EA the way lithium is.

### Protective Factors
No well-established genetic or environmental protective factors are documented in the literature; folic acid periconceptional supplementation is a general CHD-risk-reduction measure but is not specifically validated for EA.

### Gene–Environment Interactions
No specific validated gene–environment interaction has been characterized for EA (e.g., no data indicating lithium risk is modified by a specific genotype). This remains an evidence gap.

**Suggested ontology terms:** HGNC:MYH7 (HGNC:7577), HGNC:NKX2-5 (HGNC:2488), HGNC:GATA4 (HGNC:4237); CHEBI term for lithium (CHEBI:30145, lithium(1+)); GENO terms for LOSS_OF_FUNCTION/dominant-negative variant classes.

---

## 3. Phenotypes

### Cardiac structural phenotypes
- **Apical displacement of the septal/inferior tricuspid leaflet** — HP:0031653 (if available) or best-fit HP:0001702/HP:0025269-class terms; more precisely the defining structural anomaly maps to **HP:0010316 Ebstein anomaly** itself, and component features:
  - Tricuspid valve regurgitation — **HP:0005180** (Tricuspid regurgitation)
  - Tricuspid stenosis (less common) — **HP:0031653** / related term
  - Right atrial enlargement / cardiomegaly — **HP:0004268** (Atrial septal defect, if concurrent), **HP:0001680** cardiomegaly-related term, **HP:0025168** (Right atrial enlargement, if present in HPO)
  - Atrialized right ventricle / functionally diminished RV
  - Right ventricular outflow tract obstruction (in severe fetal forms) — HP:0031090-class term
  - Patent foramen ovale / atrial septal defect (common concurrent lesion, right-to-left shunting causing cyanosis) — **HP:0001631** (Atrial septal defect)
  - Pulmonary atresia/stenosis (severe neonatal presentations) — **HP:0002637**/HP:0001640-class terms

### Functional/clinical phenotypes
- **Cyanosis** (from right-to-left interatrial shunting) — HP:0000961
- **Heart failure/right ventricular failure** — HP:0001635 (Congestive heart failure)
- **Arrhythmia**, particularly supraventricular tachyarrhythmias and **Wolff-Parkinson-White (WPW) pre-excitation**:
  - 5–25% of EA patients have WPW syndrome, making EA the CHD most strongly associated with accessory AV pathways; ~10–25% have one or more accessory pathways, up to 50% of whom have multiple pathways.
  - Atrial fibrillation occurs in roughly one-third of adult EA patients.
  - Pediatric rhythm-disturbance prevalence ~17% (lower than adults), predominantly supraventricular.
  - HP terms: **HP:0001680** (Arrhythmia — non-specific term), **HP:0004757** (Ventricular preexcitation), **HP:0001671** (Atrial fibrillation), **HP:0004308** (Ventricular arrhythmia)
- **Right bundle branch block** — HP:0011711
- **Sudden cardiac death risk** — increased due to arrhythmia substrate

### Fetal/neonatal-specific phenotypes
- Fetal hydrops in severe forms
- Massive cardiomegaly (cardiothoracic ratio) in utero
- Pulmonary hypoplasia secondary to cardiomegaly compressing developing lungs — HP:0002089

### Phenotype characteristics
- **Age of onset**: Spans a continuum from severe prenatal presentation (detectable by mid-gestation fetal echocardiography, often associated with poor outcome) to incidental adult diagnosis of mild anatomic variants. Neonatal presentation with cyanosis and heart failure occurs in more severe anatomic forms; milder cases may be asymptomatic until childhood or adulthood, when arrhythmia or exertional symptoms prompt evaluation.
- **Severity**: Highly variable — graded clinically/echocardiographically (e.g., Carpentier classification types A–D of leaflet tethering, and the echocardiographic Great Ormond Street Echo, "GOSE," score in the fetal/neonatal setting).
- **Progression**: Can be progressive over decades due to worsening tricuspid regurgitation, right heart dilation, and arrhythmia burden; some patients remain stable for long periods with mild disease.
- **Frequency of specific features**: Tricuspid regurgitation is nearly universal; WPW/accessory pathways occur in a substantial minority (5–25%); atrial septal communication (ASD/PFO) is very common; cyanosis frequency depends on shunt direction and pulmonary flow.

### Quality of life impact
Impact on functional capacity correlates with disease severity: patients with severe RV dysfunction and heart failure have significant exercise limitation (reduced NYHA functional class); arrhythmia burden (recurrent SVT/AF) independently reduces quality of life and increases healthcare utilization; patients undergoing successful cone reconstruction generally show improved functional status and exercise tolerance postoperatively. Detailed disease-specific EQ-5D/SF-36 data for EA specifically is sparse in the literature relative to more common CHD lesions — this is a data gap.

---

## 4. Genetic/Molecular Information

### Causal genes (monogenic subsets)
| Gene | HGNC | OMIM gene | Role in EA |
|---|---|---|---|
| MYH7 | HGNC:7577 | 160760 | Autosomal-dominant EA + LVNC subtype; ~6% of EA probands in one cohort (PMID:21604106) |
| NKX2-5 | HGNC:2488 | 600584 | Candidate gene; broader CHD transcription factor, implicated in isolated/familial EA |
| GATA4 | HGNC:4237 | 600576 | Candidate gene; implicated via 8p23.1 microdeletion (PMID:21815254) and direct sequence variants |

### Pathogenic variant characteristics
- **Variant type**: Predominantly missense variants in MYH7 (consistent with sarcomeric dominant-negative/gain-of-function mechanisms as in hypertrophic/dilated cardiomyopathy); some MYH7 variants identified in EA cohorts were previously known HCM-causing alleles, suggesting pleiotropy of specific MYH7 residues across cardiomyopathy and valvulopathy phenotypes.
- **Classification**: Variant pathogenicity in these small EA cohorts is largely based on segregation with LVNC/EA phenotype in families, absence from population databases, and known cardiomyopathy association (per ACMG/AMP-style reasoning); formal ClinVar-level classification varies by variant.
- **Allele frequency**: EA-associated MYH7 variants are rare/private, consistent with rarity in gnomAD population databases (specific frequencies not systematically reported in the identified literature — check ClinVar/gnomAD directly for individual variants).
- **Origin**: Predominantly germline; familial cases show autosomal dominant transmission with variable expressivity (EA, isolated LVNC, or both, and VSD in some kindreds — PMID:25444217).
- **Functional consequence**: Sarcomeric dysfunction (myosin motor domain or lever-arm alterations) is hypothesized to disrupt normal myocardial mechanics during the valvulogenic remodeling window, secondarily impairing tricuspid leaflet delamination — a proposed but not fully mechanistically resolved link between a sarcomere-protein defect and a valve-morphogenesis phenotype.

### Modifier genes
Not well characterized for EA specifically; TBX5 is a co-regulator with NKX2-5/GATA4 in cardiac septation networks and is a plausible modifier/candidate but lacks EA-specific validation in the retrieved literature.

### Chromosomal abnormalities
- **1p36 deletion syndrome** — associated with EA/EA-like tricuspid malformation (PMID:21815254)
- **8p23.1 microdeletion** (encompassing GATA4) — associated with EA (PMID:21815254)

### Epigenetic information
No EA-specific epigenetic (DNA methylation/chromatin) studies were identified in this search; this is an evidence gap relative to more common CHD lesions.

**Suggested ontology terms:** GO:0060420 (regulation of heart growth), GO:0003158 (endothelium development), GO:0003170 (heart valve development), GO:0055008 (cardiac muscle tissue morphogenesis); CL terms for cardiac valve interstitial cells and endocardial cells involved in valvulogenesis.

---

## 5. Environmental Information

### Environmental factors
- **Lithium** (see Etiology above) — the single best-characterized environmental/pharmacologic risk factor, historically over-estimated but confirmed at a modest, dose-related elevated risk in modern cohort studies (PMID:28591541, NEJM 2017; PMID:8031346 — "A reevaluation of risk of in utero exposure to lithium").
- Possible associations with other maternal medication exposures examined in the National Birth Defects Prevention Study (benzodiazepines and others) are preliminary/hypothesis-generating (PMC6711372).

### Lifestyle factors
No robust, EA-specific lifestyle risk factor (smoking, alcohol, diet) has been established in the literature reviewed; general CHD teratogen avoidance guidance applies but is not EA-specific.

### Infectious agents
No infectious etiology is established for EA; it is a structural/developmental cardiac malformation, not known to be triggered by a specific pathogen.

---

## 6. Mechanism / Pathophysiology

### Developmental mechanism (causal chain)
1. **Trigger**: Genetic lesion (e.g., MYH7 sarcomeric variant, NKX2-5/GATA4 dysregulation) or teratogenic exposure (lithium) perturbs normal atrioventricular valvulogenesis during fetal cardiac development.
2. **Failure of leaflet delamination**: Normally, the septal and inferior (posterior) tricuspid leaflets separate ("delaminate") from the underlying ventricular myocardium via a program of localized apoptosis/extracellular matrix remodeling, becoming free, mobile, chordally-tethered structures. In EA, this delamination process is incomplete, leaving the septal and inferior leaflets adherent to (or "plastered" against) the myocardium.
3. **Apical (downward) displacement of the functional tricuspid annulus**: Because the leaflets remain attached to myocardium rather than forming a discrete annular hinge point, the effective/functional tricuspid orifice is displaced apically into the right ventricle, well below the true anatomic tricuspid annulus.
4. **Atrialization of the right ventricle**: The portion of right ventricular myocardium between the true (anatomic) tricuspid annulus and the displaced functional valve becomes thin-walled, dyskinetic, and functionally continuous with the right atrium — the "atrialized RV."
5. **Anterosuperior leaflet abnormality**: The anterosuperior leaflet, while typically not displaced, is frequently enlarged, redundant, fenestrated, and tethered by abnormal chordal/muscular attachments to the RV free wall, further impairing coaptation.
6. **Tricuspid regurgitation / functional right ventricular dysfunction**: Failure of leaflet coaptation causes tricuspid regurgitation; a functionally small, distal "true" right ventricle plus a large, thin atrialized segment reduces effective RV pump function.
7. **Downstream hemodynamic consequences**: Right atrial dilation, elevated right atrial pressure, right-to-left shunting across an associated ASD/PFO (causing cyanosis when present), reduced pulmonary blood flow in severe cases, and — in the most severe fetal presentations — massive cardiomegaly, pulmonary hypoplasia (via mechanical lung compression), and hydrops.
8. **Arrhythmogenic substrate**: The abnormal atrioventricular junction anatomy predisposes to accessory atrioventricular conduction pathways (WPW), and atrial dilation predisposes to atrial fibrillation/flutter and other supraventricular arrhythmias, creating risk for sudden cardiac death.

### Molecular pathways
- Cardiac transcription factor network: NKX2-5–GATA4–TBX5 complex regulating genes required for cardiac septation and AV valve/junction formation (PMC3370385, PMC6503026).
- Sarcomere gene pathway: MYH7-encoded β-myosin heavy chain — primarily characterized in the context of hypertrophic/dilated cardiomyopathy and LVNC signaling, with EA representing a less common but reported phenotypic manifestation, presumably via altered myocardial mechanical signaling during the valvulogenic remodeling window (mechanism incompletely resolved — see Springer Nature chapter "Molecular Pathways and Animal Models of Ebstein's Anomaly," 2023).
- Second heart field (SHF)–derived AV canal signaling: In zebrafish, the transcription factor **foxn4** acts with **tbx5** to direct AV boundary formation by regulating **tbx2b** expression, establishing the developmental logic of AV valve delamination that is disrupted in EA-like phenotypes (relevant developmental biology parallel, not EA-specific human data).

### Cellular processes
- Endocardial cushion formation and epithelial-to-mesenchymal transition (EMT) at the AV canal.
- Localized programmed cell death (apoptosis) in myocardium underlying the developing septal/inferior leaflets, a step required for normal delamination — presumed disrupted in EA.
- Extracellular matrix remodeling of the developing valve leaflets.

### Tissue damage / remodeling mechanisms
Chronic tricuspid regurgitation and RV volume overload drive progressive right atrial and (atrialized) right ventricular dilation, myocardial wall thinning, and fibrosis over time; longstanding RV dysfunction can secondarily affect left ventricular function via ventricular interdependence (documented in the Da Silva cone-repair outcome literature, where LV function improves after cone repair — PMC12295748).

### Biochemical/functional abnormalities
Primary defect is structural/mechanical (valve-myocardial adhesion and displacement) rather than a discrete enzymatic or receptor-level biochemical lesion, distinguishing EA mechanistically from metabolic or channelopathic cardiac disease.

### Molecular profiling
Systematic transcriptomic, proteomic, or metabolomic profiling specific to EA valve/myocardial tissue was not identified in this search — this is a notable data/methods gap; most molecular data derive from candidate-gene sequencing rather than unbiased -omics of affected tissue.

**Suggested GO terms:** GO:0003171 (atrioventricular valve development), GO:0003190 (atrioventricular valve formation), GO:0055010 (ventricular cardiac muscle tissue morphogenesis), GO:0060412 (ventricular septum morphogenesis), GO:0097084 (vascular associated smooth muscle cell development — if relevant to valve interstitial lineage), GO:0006915 (apoptotic process, for leaflet delamination).

**Suggested CL terms:** CL:0002138 (endocardial cell), CL:0000670 (primary heart field cardiomyocyte / cardiac muscle cell — as best fit), valve interstitial cell (if a CL term exists), cardiac neural crest-derived cell (where relevant to AV cushion mesenchyme).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary**: Heart — specifically the tricuspid valve (UBERON:0002102) and right ventricle (UBERON:0002080)/right atrium (UBERON:0002078).
- **Secondary/complication-related**: Lungs (pulmonary hypoplasia in severe fetal cases, UBERON:0002048), liver/systemic venous system (secondary to right heart failure and systemic venous congestion).
- **Body systems**: Cardiovascular system primarily; secondary respiratory involvement in severe fetal/neonatal disease.

### Tissue/cell level
- Valve leaflet fibrous/connective tissue (septal, inferior/posterior, and anterosuperior tricuspid leaflets) — UBERON:0002145 (heart valve) as parent term.
- Ventricular myocardium of the atrialized right ventricle.
- Endocardium/endocardial cushion-derived tissue.
- Conduction system tissue (relevant to accessory pathway formation) — UBERON structures for the AV node/His bundle region.

### Subcellular level
Not specifically characterized beyond generic cardiomyocyte sarcomeric structures (relevant to the MYH7 subtype) — GO Cellular Component: GO:0030017 (sarcomere), GO:0030016 (myofibril).

### Localization
- Right-heart-restricted anatomic defect (left heart structures are typically anatomically normal except in LVNC-overlap MYH7-associated cases, where left ventricular noncompaction co-occurs).
- Not laterality-relevant in the classic sense (it is inherently a right-sided cardiac malformation, not a bilateral/asymmetric process).

---

## 8. Temporal Development

### Onset
- **Congenital**: EA originates in utero during atrioventricular valve morphogenesis (roughly the first trimester through mid-gestation).
- **Clinical presentation spans**: prenatal detection via fetal echocardiography (severe forms, sometimes with poor prognosis), neonatal presentation with cyanosis/heart failure (moderate-severe forms), or delayed diagnosis in childhood through adulthood — sometimes incidentally — in mild anatomic variants.

### Progression
- **Disease course pattern**: Can be stable for extended periods (especially milder anatomic forms) or progressive, with worsening tricuspid regurgitation, right heart enlargement, and increasing arrhythmia burden over years to decades.
- **Progression drivers**: Chronic volume overload from tricuspid regurgitation, progressive RV/RA dilation, development or worsening of arrhythmia substrate.
- Fetal cases with severe cardiomegaly and hydrops carry high risk of in utero or neonatal demise; a cited case series found in-utero mortality of 37.5% and neonatal mortality of 50% in a high-risk fetal cohort, with ~30% one-year mortality overall in prenatally/neonatally diagnosed severe disease.
- Long-term registry data (Danish/Swedish nationwide cohorts, PMID/JACC 2023 — "Mortality in Patients With Ebstein Anomaly") found 35-year cumulative mortality of 11% even among patients with anticipated *mild* EA, with higher mortality in those with associated cardiac lesions; mortality has decreased in patients diagnosed in the modern era compared with earlier eras.

### Patterns
- **Critical period**: The valvulogenic window (delamination of AV valve leaflets) is the developmental critical period during which the causal insult (genetic or teratogenic) acts.
- **Remission**: Not applicable in the classic sense (structural malformation), but successful surgical (cone) reconstruction can produce durable, near-normalization of valve competence and functional status for many years.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence at birth**: Estimates vary by source/methodology — approximately 1 in 20,000 to 1 in 100,000 live births (Orphanet); other studies report 3–5, 4.4, or up to 7 per 100,000 live births (Texas birth-defects registry, PMID:21465650 — "Epidemiology of Ebstein anomaly: prevalence and patterns in Texas, 1999–2005"); broader estimates place incidence at 1.2–5 per 100,000 live births, or as high as 50–100 per million live births in some critical-CHD classifications.
- EA comprises **<1%** of all congenital heart defects.
- No strong sex predilection is generally reported (roughly equal male:female distribution), though some individual series show slight variation.

### Inheritance pattern (for genetically resolved subsets)
- **Autosomal dominant** inheritance is documented for the MYH7-associated EA/LVNC subtype, with variable expressivity across kindred members (isolated LVNC, isolated EA, or both, plus VSD in some families) (PMID:23794396, PMID:25444217).
- The majority of EA cases are **sporadic**, without a clearly Mendelian inheritance pattern, consistent with multifactorial or de novo genetic causation, or non-genetic (e.g., lithium) etiology.
- **Chromosomal microdeletion** cases (1p36, 8p23.1) typically arise de novo but can rarely be inherited from a similarly affected/carrier parent.

### Penetrance / expressivity
- Variable expressivity is documented within MYH7-mutation-positive families (different family members manifesting EA, LVNC, or both) (PMID:23794396).
- Penetrance estimates for specific MYH7 variants in the EA context are not precisely quantified in the retrieved literature.

### Population demographics
- No strong evidence for a specific ethnic/geographic founder effect in EA (unlike many monogenic disorders); it is broadly distributed geographically.
- Sibling recurrence risk for isolated/sporadic EA is empirically low (~1%), consistent with predominantly sporadic causation.

---

## 10. Diagnostics

### Clinical/imaging tests
- **Transthoracic and fetal echocardiography** are the primary diagnostic modalities — demonstrating apical displacement of septal/inferior tricuspid leaflets (displacement index typically defined as >8 mm/m² BSA in adults, or specific fetal apical displacement thresholds), atrialized RV, and tricuspid regurgitation severity.
- **Cardiac MRI**: Used for RV volumetric assessment, atrialized RV quantification, and risk stratification (e.g., RV end-diastolic volume index, RVEF) — cardiovascular magnetic resonance-based risk prediction models for major adverse events and atrial tachyarrhythmia have been published (PMC5749347).
- **Electrocardiography (ECG)**: Right bundle branch block pattern, evidence of pre-excitation (WPW pattern — short PR interval, delta wave) when accessory pathways are present.
- **Electrophysiology study**: For mapping and characterizing accessory pathways prior to ablation, given the high (~25%) prevalence of accessory pathways and frequent multiplicity of pathways in EA.
- **Chest radiography**: Classic "wall-to-wall heart" cardiomegaly appearance in severe cases.

### Fetal-specific diagnostics and scoring
- **Fetal echocardiography** allows in-utero diagnosis and prognostication; key prognostic sonographic features include cardiothoracic index >0.55, relative foramen ovale/atrial septal ratio <0.3, right ventricular outflow tract obstruction, tricuspid valve displacement index >2.5, absence of reverse flow in the ductus arteriosus, and RV:LV ratio >2 (PMID:23819422 and related fetal Ebstein prognosis literature).
- **Great Ormond Street Echo (GOSE) score**: A validated ratio-based echocardiographic prognostic index; e.g., a GOSE score ratio of 1.1–1.49 corresponds to ~10% early mortality in acyanotic patients but up to 100% mortality in cyanotic patients, illustrating the strong prognostic interaction between anatomic severity and physiologic (cyanosis) status.

### Genetic testing
- Not part of routine diagnostic workup for isolated/sporadic EA given its predominantly non-Mendelian nature, but **recommended** when EA is accompanied by left ventricular noncompaction, a family history suggestive of autosomal dominant transmission, or additional syndromic features — targeted sequencing/panel testing for **MYH7** (and consideration of **NKX2-5**, **GATA4**) is reasonable in these contexts.
- **Chromosomal microarray (CMA)**: Indicated when EA occurs with additional dysmorphic features or extracardiac anomalies, to detect 1p36 or 8p23.1 microdeletions.
- **Whole exome/genome sequencing**: Used in research cohorts (e.g., 47-case, 50-gene candidate panel study) to identify novel variants in myocardial-development pathway genes; not yet standard clinical practice for isolated EA.

### Clinical criteria / differential diagnosis
- Diagnosis is primarily echocardiographic/anatomic rather than criteria-based (no DSM/consensus clinical scoring system analogous to other diseases).
- **Differential diagnosis** includes other causes of severe tricuspid regurgitation and right heart enlargement: tricuspid valve dysplasia (a distinct entity without the same degree of leaflet delamination failure/annular displacement), pulmonary atresia with intact ventricular septum, uhl anomaly (parchment right ventricle), and other causes of fetal cardiomegaly/hydrops.

### Screening
No population-based newborn or prenatal screening program specifically targets EA (given its rarity); detection occurs opportunistically via routine obstetric anomaly ultrasound or, postnatally, via clinical evaluation of murmur/cyanosis/arrhythmia.

---

## 11. Outcome/Prognosis

### Survival and mortality
- **Population-level cohort data** (Danish/Swedish national registries, patients born 1970–2017, 530 EA patients vs. 5,300 matched controls, median follow-up 11 years; JACC 2023, PMID for "Mortality in Patients With Ebstein Anomaly"): 35-year cumulative mortality of **11%**, even in patients with anticipated *mild* disease; patients with associated cardiac lesions had higher mortality than isolated EA; mortality has declined in the modern diagnostic/treatment era relative to earlier decades; most common cause of late death was cardiac-related.
- **Fetal/neonatal cohorts**: Substantially worse — one high-risk case series reported in-utero mortality of 37.5% and neonatal mortality of 50%; broader estimates place 1-year mortality at ~30% for prenatally/neonatally diagnosed cases, heavily dependent on anatomic severity and cyanosis status (per GOSE score stratification above).
- **Postoperative mortality risk factors** (surgical cohorts): RV end-diastolic volume index >200 mL/m², RV ejection fraction <40%, and age >50 years at time of operation.

### Morbidity and functional outcomes
- Progressive tricuspid regurgitation and right heart failure are the principal drivers of morbidity in unrepaired or inadequately repaired disease.
- Arrhythmia-related morbidity (recurrent SVT, atrial fibrillation, WPW-mediated tachyarrhythmia) is common and can itself precipitate heart failure or, rarely, sudden cardiac death.
- Post cone-repair, RV size decreases and antegrade stroke volume increases as early as 6 months postoperatively (PMID:25535206 — Da Silva cone repair effect on RV size/function); mid-term studies (2025) additionally document recovery of RV function *and* improvement of LV function after cone repair (PMC12295748), supporting a ventricular-interdependence mechanism for the pre-repair LV dysfunction sometimes observed.

### Prognostic factors
- Anatomic severity (degree of leaflet displacement/tethering, Carpentier type), presence/degree of cyanosis, RV size and function (echocardiographic and MRI-derived indices), presence of associated lesions (pulmonary stenosis/atresia, ASD), and arrhythmia burden are the principal prognostic determinants identified across the fetal, pediatric, and adult literature.
- A 2025 review specifically synthesizes "poor prognostic factors" in EA (PMC12859563 — "Complex Considerations for a Complex Disease: Identifying Poor Prognostic Factors in Ebstein's Anomaly").

---

## 12. Treatment

### Pharmacotherapy
- **Antiarrhythmic medications** (e.g., beta-blockers, class III agents) for rate/rhythm control of atrial fibrillation/flutter and supraventricular tachyarrhythmias.
- **Heart failure pharmacotherapy** (diuretics, and standard heart-failure agents as adapted for right-heart-predominant failure) in patients with RV dysfunction.
- **Prostaglandin E1** in neonates with ductal-dependent pulmonary blood flow (severe forms with functional pulmonary atresia) to maintain ductal patency pending intervention.
- NCIT term: NCIT:C15986 (Pharmacotherapy) as the generic action term, with specific agents captured via `therapeutic_agent` (e.g., CHEBI terms for individual antiarrhythmics).

### Interventional electrophysiology
- **Catheter ablation** of accessory pathways (for WPW) and arrhythmia substrates — though EA-associated ablation carries a notably higher recurrence rate (30–40%) compared with the general population (5–10%), reflecting the complex, often multiple accessory-pathway anatomy in EA.
- NCIT term: consider NCIT:C15329 (Surgical Procedure) parent or a more specific interventional cardiology procedure term if available; `therapeutic_modality: DEVICE` may apply for catheter-based ablation technology.

### Surgical treatment
- **Cone reconstruction (Da Silva cone repair)**: The current preferred definitive surgical technique — extensive mobilization of the (dysplastic but present) leaflet tissue, longitudinal plication of the atrialized right ventricle, and reconstruction of a cone-shaped, leaflet-to-leaflet coapting neo-tricuspid valve using the patient's own (mobilized ± patch-augmented) leaflet tissue. Reported to produce excellent valve competence in the large majority of patients, with RV size normalization and improved antegrade stroke volume by 6 months, and documented mid-term (multi-year) recovery of both RV and LV function (PMID:25535206; PMC12295748). Variants include septal leaflet augmentation with autologous pericardial patch when native septal leaflet tissue is severely deficient (2025 comparative outcomes literature).
- **Staged single-ventricle palliation (Starnes procedure)**: Reserved for the most severe, unrepairable neonatal forms (severe RV hypoplasia/dysfunction) — tricuspid valve exclusion with fenestrated patch, atrial septectomy, and a modified BT shunt or similar systemic-to-pulmonary shunt, as a bridge toward staged single-ventricle (Fontan-pathway) palliation. A cone operation can subsequently be performed after a prior Starnes procedure in select cases (biventricular "conversion") with reported favorable initial outcomes.
- **Cardiac transplantation**: Considered in end-stage cases with severe, irreparable ventricular dysfunction.
- NCIT terms: NCIT:C15329 (Surgical Procedure), and more specific valve-repair/reconstruction terms if available in NCIT; `therapeutic_modality: SURGERY`.

### Supportive/rehabilitative care
- Standard heart-failure supportive management, activity guidance, and longitudinal cardiology follow-up (arrhythmia surveillance, RV function monitoring).
- NCIT:C15747 (Supportive Care).

### Experimental / emerging approaches
- No gene therapy, RNA-based therapy, or targeted molecular therapy is currently established or in active clinical trials specific to EA (the disease is structural/surgical rather than a target for molecular correction), consistent with its developmental/anatomic (rather than progressive metabolic or degenerative) pathophysiology. Ongoing research is concentrated in surgical technique refinement (e.g., septal leaflet augmentation approaches, 2025) and risk-stratification/outcomes modeling (fetal echocardiographic prognostic markers, CMR-based risk prediction) rather than pharmacologic/molecular intervention.

### Treatment outcomes
- Cone repair: high rates of excellent postoperative valve competence, with RV remodeling (size reduction, functional improvement) documented from 6 months through multi-year follow-up.
- Ablation for WPW/accessory pathways in EA: elevated recurrence (30–40%) relative to structurally normal hearts, reflecting anatomic complexity.
- Population-level surgical outcome studies (PMC6852467 — "Early and Long-Term Outcomes of Surgical Treatment of Ebstein's Anomaly") document continued improvement in both early and late surgical outcomes over time as technique (particularly cone reconstruction) has matured.

### Treatment strategy
- Management is stratified by anatomic severity, degree of cyanosis, RV function, and presence of arrhythmia: mild, asymptomatic cases may be managed with surveillance alone; moderate-severe symptomatic disease with significant TR/RV dilation is generally directed toward cone reconstruction; the most severe neonatal forms with minimal functional RV may require staged single-ventricle palliation (Starnes-first strategy) rather than primary biventricular repair.

---

## 13. Prevention

- **Primary prevention**: Avoidance/minimization of first-trimester lithium exposure in women who are or may become pregnant is the principal identified, modifiable primary-prevention strategy; when lithium is clinically necessary for maternal bipolar disorder management, guidance emphasizes using the lowest effective dose, therapeutic drug monitoring, and consideration of dose-related risk (>900 mg/day associated with higher malformation risk) (see PMC10596010 — "Lithium management in pregnant patients with bipolar disorder").
- **Secondary prevention**: Fetal anomaly ultrasound/echocardiography enables early detection, allowing for informed counseling, planned delivery at a center with cardiac surgical/ECMO capability, and early postnatal intervention planning — this does not prevent the malformation but mitigates downstream morbidity/mortality via optimized perinatal management.
- **Genetic counseling**: Recommended for families with a known MYH7 variant or other identified monogenic cause, given autosomal dominant inheritance and variable expressivity in that subset; recurrence-risk counseling for sporadic/isolated EA is generally reassuring (low empiric recurrence risk) absent an identified familial genetic cause.
- **Prenatal genetic testing/counseling**: Consideration of targeted variant testing in subsequent pregnancies when a causal familial variant has been identified.
- No vaccine, public health, or population-level environmental intervention is applicable given the rarity and largely sporadic/idiosyncratic (lithium-exposure-driven or de novo genetic) nature of EA.

---

## 14. Other Species / Natural Disease

- **Naturally occurring EA-like disease in companion/domestic animals**: Not well documented as a recognized naturally occurring veterinary clinical entity analogous to human EA; tricuspid valve dysplasia is described in dogs (e.g., Labrador Retrievers) as a distinct congenital tricuspid malformation, but it is generally classified separately from "Ebstein-like" apical displacement with leaflet-myocardial adhesion, and formal cross-species nosological equivalence to human EA is not firmly established in the retrieved literature — recommend checking OMIA directly for any curated veterinary entries.
- **Comparative/orthologous developmental biology**: Zebrafish (*Danio rerio*) atrioventricular canal development studies (foxn4/tbx5/tbx2b pathway) provide the closest comparative developmental-biology parallel for the delamination/AV-boundary-formation process disrupted in human EA, though these are developmental models of the normal AV valve program rather than models reproducing an EA disease phenotype per se.

---

## 15. Model Organisms

- **Mouse models**: Both mouse and zebrafish genes have been catalogued as associated with EA via cross-species phenotype-matching approaches (linking model-organism cardiac phenotype ontology annotations to candidate human EA genes); specific validated mouse knockout models fully recapitulating the EA leaflet-delamination-failure phenotype were not identified with a specific citation in this search — this appears to be an area with limited dedicated animal-model literature relative to more common structural CHD lesions (see the 2023 review chapter "Molecular Pathways and Animal Models of Ebstein's Anomaly," Springer, for the most current synthesis).
- **Zebrafish models**: Zebrafish AV canal/valve development work (foxn4–tbx5–tbx2b transcriptional pathway) establishes the relevant normal developmental program; loss-of-function perturbation of these genes disrupts AV boundary formation in a manner mechanistically analogous to (but not an established formal model of) human EA.
- **Model characteristics/limitations**: No single animal model is described in the retrieved literature as fully recapitulating the specific combination of septal/inferior leaflet myocardial adhesion, functional annular displacement, and atrialized RV segment characteristic of human EA; existing models primarily inform the normal AV valvulogenesis program whose disruption is inferred (rather than directly demonstrated) to underlie EA.
- **Applications**: Zebrafish AV-canal models are useful for dissecting the transcriptional regulatory logic of valve leaflet delamination and could in principle be used to test candidate EA genes (e.g., MYH7 orthologs, NKX2-5/GATA4 pathway members) for AV valve phenotypes, but this specific application to EA candidate genes was not documented with a citation in the retrieved search results.
- **Resources**: MGI (Mouse Genome Informatics) and ZFIN (Zebrafish Information Network) are the appropriate primary databases to query directly for any curated EA-relevant knockout/mutant phenotype records (not exhaustively queried in this search pass).

---

## Summary of Key Data Gaps (for curation flagging)

1. **Molecular profiling** (transcriptomic/proteomic) of EA-affected valve/myocardial tissue is essentially absent from the literature reviewed.
2. **Dedicated animal models** that recapitulate the specific EA leaflet-delamination-failure phenotype (as opposed to general AV valve developmental biology) are not well established.
3. **Quantitative penetrance** estimates for specific MYH7 (or other) pathogenic variants in the EA context are not precisely defined.
4. **Disease-specific quality-of-life instrument data** (EQ-5D/SF-36) specific to EA populations is sparse.
5. **Gene–environment interaction** data (e.g., whether lithium risk is modified by genotype) is absent.
6. Veterinary/natural-disease cross-species correlates are not well substantiated in this pass and should be checked directly against OMIA before curation.

---

## Suggested Ontology Term Summary Table

| Category | Suggested term(s) |
|---|---|
| Disease | MONDO:0009144; OMIM:224700; ORPHA:1880; ICD-10 Q22.5 |
| Phenotype (HPO) | HP:0010316 (Ebstein anomaly), HP:0005180 (Tricuspid regurgitation), HP:0004757 (Ventricular preexcitation), HP:0001671 (Atrial fibrillation), HP:0011711 (RBBB), HP:0000961 (Cyanosis), HP:0001635 (Congestive heart failure), HP:0001631 (Atrial septal defect), HP:0002089 (Pulmonary hypoplasia) |
| Genes | HGNC:7577 (MYH7), HGNC:2488 (NKX2-5), HGNC:4237 (GATA4) |
| GO — biological process | GO:0003171/GO:0003190 (AV valve development/formation), GO:0055010 (ventricular cardiac muscle tissue morphogenesis), GO:0006915 (apoptotic process) |
| CL | CL:0002138 (endocardial cell) |
| UBERON | UBERON:0002102 (tricuspid valve), UBERON:0002080 (right cardiac ventricle), UBERON:0002078 (right cardiac atrium) |
| CHEBI | CHEBI:30145 (lithium(1+)) |
| NCIT (treatment) | NCIT:C15329 (Surgical Procedure — cone reconstruction), NCIT:C15986 (Pharmacotherapy), NCIT:C15747 (Supportive Care) |

---

## Sources

- [Entry - 224700 - EBSTEIN ANOMALY (OMIM)](https://omim.org/entry/224700)
- [Orphanet: Ebstein malformation of the tricuspid valve](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=1880)
- [Ebstein anomaly | Monarch Initiative](https://monarchinitiative.org/MONDO:0009144)
- [Ebstein Anomaly and Malformation - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK534824/)
- [Congenital Heart Surgery Nomenclature and Database Project: Ebstein's anomaly and tricuspid valve disease - PubMed](https://pubmed.ncbi.nlm.nih.gov/10798422/)
- [Ebstein's anomaly may be caused by mutations in the sarcomere protein gene MYH7 - PMC/PubMed](https://pmc.ncbi.nlm.nih.gov/articles/PMC3578524/) / [PubMed 21604106](https://pubmed.ncbi.nlm.nih.gov/21604106/)
- [Ebstein anomaly associated with left ventricular noncompaction: an autosomal dominant condition that can be caused by mutations in MYH7 - PubMed 23794396](https://pubmed.ncbi.nlm.nih.gov/23794396/)
- [Familial Ebstein's anomaly, left ventricular noncompaction, and ventricular septal defect associated with an MYH7 mutation - PubMed 25444217](https://pubmed.ncbi.nlm.nih.gov/25444217/)
- [Ebstein anomaly: Genetic heterogeneity and association with microdeletions 1p36 and 8p23.1 - PubMed 21815254](https://pubmed.ncbi.nlm.nih.gov/21815254/)
- [Genetic Variants in Isolated Ebstein Anomaly Implicated in Myocardial Development Pathways | PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0165174)
- [Combined Mutation Screening of NKX2-5, GATA4, and TBX5 in Congenital Heart Disease - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3370385/)
- [Association of NKX2-5, GATA4, and TBX5 polymorphisms with congenital heart disease in Egyptian children - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6503026/)
- [Lithium Use in Pregnancy and the Risk of Cardiac Malformations - NEJM / PubMed 28591541](https://pubmed.ncbi.nlm.nih.gov/28591541/)
- [A reevaluation of risk of in utero exposure to lithium - PubMed 8031346](https://pubmed.ncbi.nlm.nih.gov/8031346/)
- [Lithium management in pregnant patients with bipolar disorder - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10596010/)
- [Potential risk factors for Ebstein anomaly, National Birth Defects Prevention Study, 1997–2011 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6711372/)
- [Epidemiology of Ebstein anomaly: prevalence and patterns in Texas, 1999-2005 - PubMed 21465650](https://pubmed.ncbi.nlm.nih.gov/21465650/)
- [Mortality in Patients With Ebstein Anomaly | JACC](https://www.jacc.org/doi/10.1016/j.jacc.2023.04.037)
- [Ebstein Anomaly: We Should Do Better | JACC](https://www.jacc.org/doi/10.1016/j.jacc.2023.05.009)
- [Complex Considerations for a Complex Disease: Identifying Poor Prognostic Factors in Ebstein's Anomaly - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12859563/)
- [A Twenty-Year Follow-Up of Adults with Ebstein Anomaly - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11012800/)
- [Major adverse events and atrial tachycardia in Ebstein's anomaly predicted by cardiovascular magnetic resonance - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5749347/)
- [Risk Factors for Atrial Arrhythmias in Adults With Ebstein Anomaly - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11198643/)
- [A multicenter, long-term study on arrhythmias in children with Ebstein anomaly - PubMed 19937010](https://pubmed.ncbi.nlm.nih.gov/19937010/)
- [Effect of Ebstein's anomaly on short- and long-term outcome of surgically treated patients with WPW syndrome - PubMed 1394922](https://pubmed.ncbi.nlm.nih.gov/1394922/)
- [Da Silva's cone repair for Ebstein's anomaly: effect on right ventricular size and function - PubMed 25535206](https://pubmed.ncbi.nlm.nih.gov/25535206/)
- [Mid-Term Recovery of Right Ventricular Function and Improvement of Left Ventricular Function After Da Silva Cone Procedure for Ebstein Anomaly - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12295748/)
- [The Da Silva cone operation after the Starnes procedure for Ebstein's anomaly](https://www.researchgate.net/publication/341450720)
- [Septal leaflet augmentation during Da Silva cone repair - PubMed 41819162](https://pubmed.ncbi.nlm.nih.gov/41819162/)
- [Early and Long-Term Outcomes of Surgical Treatment of Ebstein's Anomaly - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6852467/)
- [Long-Term Outcomes of Modified Cone Reconstruction for Ebstein's Anomaly in Pediatric Patients](https://e-kcj.org/DOIx.php?id=10.4070%2Fkcj.2023.0200)
- [Fetal diagnosis and prognosis of Ebstein's anomaly - PubMed 23819422](https://pubmed.ncbi.nlm.nih.gov/23819422/)
- [Prenatal Cardiac Ultrasound Markers of Outcomes in Ebstein's Anomaly - Pediatric Cardiology (Springer)](https://link.springer.com/article/10.1007/s00246-024-03530-9)
- [Ebstein's Anomaly, Left Ventricular Noncompaction and Gerbode-Like Defect Triad - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8601841/)
- [Molecular Pathways and Animal Models of Ebstein's Anomaly - Springer Nature Link](https://link.springer.com/chapter/10.1007/978-3-031-44087-8_58)
- [Zebrafish arterial valve development occurs through direct differentiation of second heart field progenitors - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11998914/)