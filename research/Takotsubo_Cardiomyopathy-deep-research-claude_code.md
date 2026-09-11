---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T21:40:08.099700'
end_time: '2026-08-09T21:45:35.269471'
duration_seconds: 327.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Takotsubo Cardiomyopathy
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
  web_search_requests: 24
  num_turns: 29
  total_cost_usd: 2.2405745
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Takotsubo Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Takotsubo Cardiomyopathy** covering all of the
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

# Takotsubo Cardiomyopathy — Comprehensive Research Report

## 1. Disease Information

**Overview.** Takotsubo cardiomyopathy (Takotsubo syndrome, TTS; also "stress cardiomyopathy," "apical ballooning syndrome," "broken heart syndrome") is an acute, reversible form of left ventricular (LV) systolic and diastolic dysfunction characterized by regional wall-motion abnormalities that extend beyond a single epicardial coronary artery territory, occurring in the absence of obstructive coronary artery disease sufficient to explain the degree of dysfunction. It classically follows an acute emotional or physical stressor and produces a clinical picture that mimics acute myocardial infarction (chest pain, ST-segment changes, troponin elevation) but with disproportionately elevated natriuretic peptides relative to troponin, and near-complete recovery of LV function within days to weeks in most patients. The name derives from the Japanese fishing pot ("tako-tsubo," octopus trap), which the classic apical-ballooned left ventricle resembles on ventriculography (Ravindran et al., 2024, *Intern Med J*, https://onlinelibrary.wiley.com/doi/10.1111/imj.16493).

**Key identifiers:**
- **MONDO:** MONDO:0019018
- **Orphanet:** ORPHA:66529 ("Tako-Tsubo cardiomyopathy"; https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=66529&lng=EN)
- **OMIM:** No OMIM phenotype/gene entry exists — TTS is not classified as a monogenic Mendelian disorder
- **ICD-10-CM:** I51.81 (Takotsubo syndrome) — the clinically used code (https://www.icd10data.com/ICD10CM/Codes/I00-I99/I30-I5A/I51-/I51.81); Orphanet cross-references ICD-10 I42.8 (Other cardiomyopathies)
- **ICD-11:** BC43.5
- **MeSH:** D054549 (Takotsubo Cardiomyopathy)

**Synonyms/alternative names:** Takotsubo syndrome, apical ballooning syndrome, stress cardiomyopathy, stress-induced cardiomyopathy, broken heart syndrome, transient LV apical ballooning syndrome, ampulla cardiomyopathy, catecholamine cardiomyopathy, neurogenic stunned myocardium (overlapping construct).

**Evidence basis:** Knowledge of TTS derives overwhelmingly from **aggregated disease-level resources** — large multicenter registries (International Takotsubo [InterTAK] Registry, ~1,750+ patients; German-Italian Stress Cardiomyopathy [GEIST] Registry; Spanish RETAKO Registry), national hospital discharge/administrative databases (e.g., U.S. National Inpatient Sample), and systematic reviews/meta-analyses, supplemented by case reports/series and mechanistic studies in humans and animal models — rather than from individual-patient EHR mining, since there is no dedicated large-scale genomic biobank for this condition.

---

## 2. Etiology

### Disease causal factors
TTS is best conceptualized as a **stress-triggered, catecholamine-mediated, reversible cardiomyopathy** rather than a disease with a single discrete cause. The unifying causal chain is: an acute emotional or physical/medical stressor → massive sympathoadrenal (catecholamine) surge and/or direct sympathetic nerve terminal norepinephrine release in myocardium → catecholamine-induced myocardial toxicity, coronary microvascular dysfunction, and altered β-adrenergic signal trafficking → reversible regional myocardial stunning ("takotsubo" pattern) (Y-Hassan & Tornvall, 2018, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9603071/; Ghadri et al., *Circulation* 2022, https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.121.055854).

### Risk factors

**Genetic risk factors** (susceptibility, not causal in the Mendelian sense):
- No single causal gene has been identified. Candidate-gene association studies have examined variants in **ADRB1** (β1-adrenergic receptor), **ADRB2** (β2-adrenergic receptor), **ADRA2C** (α2C-adrenergic receptor), **GRK5** (G-protein-coupled receptor kinase 5), **BAG3** (Bcl-2-associated athanogene 3), and estrogen receptor genes, with conflicting/non-replicated results (https://pubmed.ncbi.nlm.nih.gov/19167638/; https://pubmed.ncbi.nlm.nih.gov/19944334/; https://pubmed.ncbi.nlm.nih.gov/25132214/).
- A 2018 case-control study found "**lack of genetic susceptibility**" for candidate adrenergic-pathway variants tested individually (https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-018-0544-6, PMC5842616).
- A recent comprehensive review (2025) concludes: "these data support genetic heterogeneity in takotsubo cardiomyopathy susceptibility and a likely **polygenic basis**, conferring a cumulative effect on adrenergic pathway dysregulation" (https://pmc.ncbi.nlm.nih.gov/articles/PMC12292538/, PMID:40723798). Emerging GWAS efforts (Swedish discovery cohorts) implicate loci beyond adrenergic genes — including genes linked to psychiatric disease, lipid metabolism, and cardiac structural integrity — but sample sizes remain small and no locus reaches definitive genome-wide significance replication.
- Rare familial clusters have been reported, suggesting a genetic contribution in a subset, but there is **no defined Mendelian inheritance pattern**; the mechanism is regarded as multifactorial/polygenic gene–environment interaction (https://pubmed.ncbi.nlm.nih.gov/27638020/; https://pmc.ncbi.nlm.nih.gov/articles/PMC8471495/).

**Environmental/demographic risk factors:**
- **Female sex and postmenopausal status** — the dominant risk factor. Women >50 years account for 80–90% of cases (InterTAK Registry: 89.8% postmenopausal women, mean age 66.8 years) (https://pmc.ncbi.nlm.nih.gov/articles/PMC9999670/).
- **Acute emotional stress** (grief, fear, anger, interpersonal conflict, financial distress) and **acute physical stress/medical illness** (surgery, sepsis, exacerbation of asthma/COPD, seizures, subarachnoid/intracerebral hemorrhage, trauma) are the two principal trigger categories; physical triggers are increasingly recognized as **more common** than emotional triggers in contemporary hospitalized cohorts (52.6% physical vs. 21% emotional in one series) (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6714036/).
- **Pheochromocytoma/paraganglioma** — a recognized secondary catecholamine-excess trigger (https://pubmed.ncbi.nlm.nih.gov/21474192/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6717601/); in a comparative series only 28.9% of pheochromocytoma-triggered TTS cases had an *additional* identifiable antecedent stressor, versus 65.7% of TTS overall.
- **Malignancy** — increased TTS incidence in oncology patients (~53/100,000 chemotherapy-related hospitalizations vs. ~20.4/100,000 in the general population), and TTS prevalence among cancer patients (4–29% depending on cohort) exceeds background rates (https://pmc.ncbi.nlm.nih.gov/articles/PMC9666486/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10800806/).
- **Psychiatric comorbidity**: pre-existing anxiety and mood disorders, neuroticism, and Type D personality traits are overrepresented; pooled OR for psychological morbidity/stress exposure ~6.50 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4888627/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5838620/).
- **Neurological disease** (stroke, subarachnoid hemorrhage, seizure disorders, migraine) — reflects the brain-heart axis pathway.
- **COVID-19 and other acute infections/sepsis** have been reported as physical triggers.

### Protective factors
- **Estrogen/premenopausal status** is the principal recognized protective factor, acting through modulation of cardiomyocyte β2-adrenergic receptor Gs/Gi coupling balance (see Mechanism, below) (https://pmc.ncbi.nlm.nih.gov/articles/PMC8977075/). No specific protective genetic variants or dietary/lifestyle protective factors are established in the literature.

### Gene-environment interactions
The dominant conceptual model is that an **acute catecholamine surge (environmental trigger)** acts on a myocardium whose vulnerability is modulated by **estrogen status** (hormonal/environmental) and a **polygenic background** affecting adrenergic receptor density/coupling and stress-response pathways — i.e., genetic susceptibility lowers the threshold at which a given catecholamine surge produces cardiac injury, rather than genetics being causal on its own (https://pmc.ncbi.nlm.nih.gov/articles/PMC12292538/).

---

## 3. Phenotypes

TTS phenotypes span **symptoms**, **clinical signs**, **laboratory abnormalities**, and **imaging-defined structural/functional abnormalities**. Suggested HPO terms are given where a reasonable match exists (the HPO does not have a takotsubo-specific term; general cardiac phenotype terms apply).

| Phenotype | Type | Suggested HPO term | Frequency | Notes |
|---|---|---|---|---|
| Acute chest pain | Symptom | HP:0100749 (Chest pain) | Most common (~75–90%) presenting symptom | Mimics ACS (https://www.ncbi.nlm.nih.gov/books/NBK538160/) |
| Dyspnea | Symptom | HP:0002094 (Dyspnea) | Common (~20%) | May be sole presenting symptom, esp. secondary TTS |
| Syncope | Symptom | HP:0001279 (Syncope) | ~5–10% | Associated with arrhythmia/LVOTO |
| ST-segment elevation | Lab/ECG abnormality | HP:0033539 (ST segment elevation, if present in HPO) / free text | Common at presentation | Diffuse, not localized to one coronary territory |
| T-wave inversion | Lab/ECG abnormality | — | Common, often develops over 24–48h | Deep, diffuse |
| QT interval prolongation | Lab/ECG abnormality | HP:0001657 (Long QT interval) | Common | Predisposes to torsades de pointes |
| Elevated cardiac troponin | Laboratory abnormality | HP:0410174 (Elevated troponin I, if available) / free text | Universal, but modest | Disproportionately low relative to wall-motion abnormality extent |
| Elevated natriuretic peptide (BNP/NT-proBNP) | Laboratory abnormality | free text | Universal, disproportionately high | Key discriminator vs. MI |
| Regional wall motion abnormality (apical ballooning) | Clinical sign/imaging | HP:0001681 (Abnormal cardiac ventricle morphology) / free text | ~80% classic apical pattern | InterTAK Registry data |
| Reduced left ventricular ejection fraction | Clinical sign | HP:0012664 (Abnormal left ventricular function) | Transient, mean nadir LVEF ~30–40% | Recovers over days–weeks |
| Left ventricular outflow tract obstruction | Clinical sign | free text | ~15–25% (up to 18% in largest series) | Dynamic, worsened by inotropes |
| Cardiogenic shock | Clinical sign/complication | HP:0410174 / free text | ~6.6–11.4% | Higher in physical-trigger/secondary TTS |
| Atrial fibrillation | Clinical sign/complication | HP:0005110 (Atrial fibrillation) | ~20.7% | Most common arrhythmic complication after CHF |
| Congestive heart failure | Clinical sign/complication | HP:0001635 (Congestive heart failure) | ~35.9% (most common complication) | |
| Cardiac arrest | Complication | HP:0001695 (Sudden cardiac death, related) | ~3.4% | |
| Stroke | Complication | HP:0001297 (Stroke) | ~5.3% | Embolic from LV thrombus or comorbid |
| Left ventricular thrombus | Clinical sign/complication | free text | ~2–8% | Requires anticoagulation |
| Mitral regurgitation | Clinical sign | HP:0001653 (Mitral regurgitation) | Variable, often with SAM | |
| Anxiety/mood disturbance | Behavioral | HP:0000739 (Anxiety) / HP:0000716 (Depression) | Elevated lifetime prevalence | Precedes and follows event |

**Characteristics:**
- **Age of onset:** Predominantly adult-onset, typically postmenopausal (mean age ~66–68 years); rare pediatric and premenopausal cases exist, usually with an identifiable severe physical trigger.
- **Severity:** Variable — from mild transient dysfunction to fulminant cardiogenic shock; graded partly by ballooning pattern (global pattern carries the worst prognosis).
- **Progression:** Acute onset, typically **fully reversible** over days to weeks (LVEF normalization usually within 1–4 weeks), though speckle-tracking strain studies show **persistent subclinical dysfunction** in a substantial minority even after LVEF normalizes (PMC12786540).
- **Frequency among affected individuals:** Chest pain and dyspnea are the dominant presenting complaints (>90% combined); cardiogenic shock, arrhythmia, and thrombus are complications occurring in a minority (single-digit to ~35% depending on complication type, per National Inpatient Sample data, https://www.ahajournals.org/doi/10.1161/JAHA.124.037219).

**Quality of life impact:** Despite hemodynamic recovery, patients report persistent fatigue, reduced exercise tolerance, dyspnea, and emotional distress; post-discharge psychological morbidity includes **posttraumatic stress symptoms**, sexual distress, and reduced QoL, with anxiety (but not necessarily depression) preceding the event and psychological distress following it (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5838620/).

---

## 4. Genetic/Molecular Information

- **Causal genes:** None established as monogenic-causal; TTS is **not an OMIM-listed Mendelian condition**.
- **Pathogenic variants:** No ACMG/AMP-classified pathogenic variants exist for TTS. Candidate-gene studies (ADRB1, ADRB2, ADRA2C, GRK5, BAG3) report **inconsistent, non-replicated associations** — classified in the field as research-stage susceptibility signals, not clinically actionable variants (https://pmc.ncbi.nlm.nih.gov/articles/PMC8471495/).
- **Variant type/class:** Studies to date are predominantly SNP association studies (missense and regulatory-region polymorphisms in adrenergic pathway genes), not structural or splice-site variants.
- **Allele frequency:** Not systematically characterized in population databases (gnomAD etc.) specific to TTS risk, since no variant has reached consensus significance.
- **Somatic vs. germline:** All studied variants are germline; no somatic mutational component described.
- **Functional consequences:** Proposed functional models involve altered adrenergic receptor density/desensitization kinetics (e.g., GRK5 variants altering β-adrenergic receptor phosphorylation/desensitization) that could plausibly modulate individual susceptibility to catecholamine-induced myocardial injury, but causality is unproven.
- **Modifier genes:** Estrogen receptor gene variants have been proposed as modifiers interacting with menopausal status, but data are limited.
- **Epigenetic information:** A systematic review (2021) on genetic and epigenetic factors in TTS notes an emerging but still preliminary literature on **microRNA dysregulation** and other epigenetic marks as candidate biomarkers/modifiers, without a validated causal epigenetic mechanism (https://pmc.ncbi.nlm.nih.gov/articles/PMC8471495/).
- **Chromosomal abnormalities:** None reported as disease-associated.

**GO/molecular pathway suggestions:** GO:0071875 (adrenergic receptor signaling pathway), GO:0071870 (cellular response to catecholamine stimulus), GO:0007188 (adenylate cyclase-modulating G protein-coupled receptor signaling pathway), GO:0006874 (cellular calcium ion homeostasis).

---

## 5. Environmental Information

- **Environmental/toxin factors:** Direct exogenous catecholamine or catecholamine-like drug exposure (e.g., iatrogenic epinephrine/adrenaline administration, dobutamine stress testing, illicit stimulant use, cocaine) is a recognized precipitant (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9892140/ — iatrogenic adrenaline-induced mid-ventricular TTS).
- **Lifestyle/behavioral factors:** Chronic psychosocial stress, acute severe emotional events (bereavement, "broken heart" scenarios), and acute anxiety states are behavioral/psychological precipitants rather than classical lifestyle exposures (smoking, diet) — no strong literature links smoking/diet/alcohol directly to TTS risk beyond general cardiovascular risk factor overlap.
- **Infectious agents:** Not a primary etiology, but acute infection/sepsis and COVID-19 are recognized **physical-stress triggers** that can precipitate TTS as a secondary/physical-trigger phenotype, rather than TTS being an infectious disease per se.
- **Suggested ECTO/ontology framing:** the acute physical/emotional stressor functions analogously to an "exposure" that TRIGGERS the pathophysiology (relevant `environmental_effect: TRIGGERS` framing per dismech conventions), with pheochromocytoma-derived endogenous catecholamine excess as a special internal/endocrine trigger.

---

## 6. Mechanism / Pathophysiology

TTS pathophysiology is now understood as **multifactorial**, converging on catecholamine-driven myocardial injury, coronary microvascular dysfunction, and disordered brain–heart signaling (Ghadri et al. 2022, *Circulation*, https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.121.055854; PMC12786540, 2025 review).

### Causal chain (upstream → downstream)

1. **Trigger (upstream):** Acute emotional or physical stress → activation of hypothalamic-pituitary-adrenal axis and sympathetic nervous system.
2. **Catecholamine surge:** Massive systemic release of epinephrine, norepinephrine, and dopamine (2–3-fold or greater elevation vs. controls, and higher than levels seen in acute MI) from the adrenal medulla and sympathetic nerve terminals.
3. **β-adrenergic receptor signal trafficking switch (molecular):** At supraphysiologic epinephrine concentrations, the **β2-adrenergic receptor undergoes a conformational/functional switch from Gs-protein to Gi-protein coupling** (particularly pronounced in the LV apex, where β-receptor density is highest), converting what is normally a positive inotropic signal into a **negative inotropic effect** — the leading molecular explanation for the apex-predominant "ballooning" pattern (Nature Reviews Cardiology, https://www.nature.com/articles/ncpcardio1066; PMC6109068).
4. **Direct catecholamine cardiotoxicity (cellular):** Sustained β-adrenergic overstimulation → intracellular calcium overload → generation of reactive oxygen species, mitochondrial dysfunction, and impaired myocardial energetics (reduced phosphocreatine:ATP ratio) → **contraction-band necrosis**, a histologic hallmark shared with pheochromocytoma- and subarachnoid-hemorrhage-associated catecholamine cardiotoxicity, distinct from the coagulative necrosis of classic MI.
5. **Coronary microvascular dysfunction (tissue):** Impaired coronary flow reserve and abnormal microvascular resistance (documented via TIMI frame count, PET, and invasive index of microcirculatory resistance) contribute to regional hypoperfusion and stunning independent of epicardial coronary stenosis; impaired microvascular parameters independently predict worse in-hospital outcomes and delayed recovery (https://pubmed.ncbi.nlm.nih.gov/26080285/; https://pubmed.ncbi.nlm.nih.gov/37170610/).
6. **Myocardial inflammation:** Endomyocardial biopsy and imaging studies demonstrate a **macrophage-predominant inflammatory infiltrate**, shifted circulating monocyte subsets (increased pro-inflammatory CD14++CD16− monocytes), and elevated systemic pro-inflammatory cytokines (IL-6 markedly elevated: 23.1±4.5 pg/mL vs. 6.5±5.8 pg/mL in controls; also IL-8, CXCL1) (JACC Basic Transl Sci, https://www.jacc.org/doi/10.1016/j.jacbts.2018.08.006; PMID:30586731).
7. **Brain-heart axis (organism level, parallel/contributing arm):** Functional and structural neuroimaging shows altered connectivity and volumetric changes in the **amygdala, insular cortex (especially right insula), anterior cingulate cortex, hippocampus, and brainstem autonomic centers**, with hypoconnectivity between limbic and autonomic-regulatory brain networks. Elevated resting amygdalar activity has been prospectively linked to future cardiovascular events including TTS-like presentations, suggesting a pre-existing central autonomic-limbic vulnerability rather than purely reactive brain changes (Templin et al. 2019, *Eur Heart J*, PMID:30831580; Dichtl et al. 2020, PMID:32002630).
8. **Downstream consequence — regional myocardial stunning:** The combination of direct catecholamine toxicity, microvascular dysfunction, and altered β2AR signaling produces **reversible regional wall-motion abnormality** (classically apical ballooning, ~80% of InterTAK cases; less commonly mid-ventricular ~14.6%, basal/"reverse" ~2.2%, focal ~1.5%, or global) extending across multiple coronary territories.
9. **Clinical manifestation:** Acute heart failure/pulmonary edema, LVOT obstruction (dynamic, from hyperkinetic basal segments plus SAM of the mitral valve — occurring in up to 18–25% of cases and predisposing to cardiogenic shock), arrhythmia (QT prolongation, atrial fibrillation, ventricular arrhythmia/torsades), and (rarely) LV thrombus with embolic stroke or free-wall rupture.
10. **Resolution:** Because the injury is predominantly **stunning without fixed necrosis/fibrosis** (unlike infarction), ventricular function typically normalizes over days to weeks — though speckle-tracking strain and cardiac MR energetics studies show that **subclinical dysfunction can persist** despite LVEF normalization, and recurrence (4–10%) often manifests as a different anatomical variant, suggesting an underlying chronic vulnerability state rather than a single fully resolved acute event.

### Estrogen-mediated modulation (protective mechanism)
Estrogen modulates cardiomyocyte **β2-adrenoceptor Gs/Gi balance**, preventing excessive β2AR depletion and preserving a more favorable Gs:Gi signaling ratio under catecholamine stress, which is proposed as the principal explanation for the strong postmenopausal female predominance of TTS (https://pmc.ncbi.nlm.nih.gov/articles/PMC8977075/; https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.737003/full — estrogen also modulates macrophage polarization via β2AR).

### Cell types and biological processes involved
- **Cardiomyocytes** (CL:0000746) — direct catecholamine toxicity, Ca²⁺ overload, contraction band necrosis, β2AR Gs→Gi switch
- **Cardiac microvascular endothelial cells** (CL:0002350 or general endothelial cell CL:0000115) — endothelial dysfunction, impaired coronary microcirculation
- **Cardiac macrophages/monocytes** (CL:0000235 macrophage; CL:0000576 monocyte) — myocardial inflammatory infiltrate, cytokine release
- **Sympathetic postganglionic neurons / adrenal medullary chromaffin cells** (CL:0000166 chromaffin cell) — catecholamine release
- **Amygdalar and insular cortical neurons** — central autonomic-limbic dysregulation

Suggested GO biological process terms: GO:0071873 (response to norepinephrine), GO:0071870 (cellular response to catecholamine stimulus), GO:0002031 (G protein-coupled receptor internalization), GO:0006979 (response to oxidative stress), GO:0055074 (calcium ion homeostasis), GO:0006954 (inflammatory response), GO:0001666 (response to hypoxia, in the context of microvascular ischemia).

### Molecular profiling
- **Transcriptomics/proteomics/metabolomics**: emerging but limited — systematic reviews describe candidate circulating biomarkers (catecholamine metabolites, endothelial dysfunction markers, cytokines, microRNAs, metabolomic signatures) still "inadequately validated" for clinical use (PMC12786540; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8164033/).
- **Advanced technologies**: No large-scale single-cell or spatial transcriptomic human TTS dataset was identified in this search; most mechanistic cellular data derive from animal models and endomyocardial biopsy immunohistochemistry.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Heart (left ventricle predominantly; right ventricular involvement in ~1/3 of cases, associated with worse hemodynamic compromise).
- **Secondary/complication organs:** Brain (embolic stroke from LV thrombus, or as the trigger organ in secondary/neurogenic TTS), lungs (pulmonary edema from acute heart failure).
- **Body systems:** Cardiovascular system (primary); nervous system (central, via brain-heart axis; autonomic nervous system); endocrine system (adrenal medulla/catecholamine axis).

**Tissue/cell level:**
- Myocardium — predominantly apical (classic pattern), mid-ventricular, basal, or focal segments; ventricular myocardium (UBERON:0006566 or cardiac ventricle UBERON:0002082/0002084 for left/right ventricle).
- Coronary microvasculature — arterioles/capillaries (UBERON:0001981 blood vessel; UBERON:0002015 coronary artery for context, though epicardial coronaries are angiographically normal).
- Affected cell populations: cardiomyocytes, cardiac microvascular endothelial cells, infiltrating macrophages/monocytes.

**Subcellular level:** Mitochondria (GO:0005739, oxidative injury/energetic failure), sarcoplasmic reticulum/calcium handling machinery (GO:0016529), plasma-membrane β-adrenergic receptor complexes (GO:0005886).

**Localization:** Apex of the left ventricle is the most frequently and severely affected region (highest β-adrenergic receptor density); classic pattern is bilaterally symmetric within the ventricle (not lateralized) but extends beyond a single coronary artery's supply territory, a key diagnostic distinguishing feature from infarction.

---

## 8. Temporal Development

**Onset:**
- Typical age of onset: adult, postmenopausal (mean ~66–68 years); rare cases in younger/premenopausal women and men, almost always with a severe identifiable physical trigger.
- Onset pattern: **Acute**, occurring within minutes to hours of the triggering stressor.

**Progression:**
- Disease stages: acute phase (hours to days, wall-motion abnormality and biomarker elevation), subacute recovery phase (days to weeks, LVEF normalization), and a **subclinical/chronic phase** in a subset of patients (persistent strain abnormalities, myocardial energetic deficits, symptoms despite normalized LVEF).
- Progression rate: LV function typically normalizes within 1–4 weeks; a minority show delayed recovery, which is itself associated with higher long-term mortality and HF hospitalization.
- Disease course pattern: Classically **monophasic and self-limited**, but **recurrent** in 4–10% of patients, often with a different ballooning pattern on recurrence — supporting a model of enduring physiological vulnerability rather than a single isolated insult.
- Disease duration: Acute episode is self-limited (days–weeks); however, evidence of persistent subclinical dysfunction and comparable long-term mortality to MI survivors challenges the historical view of TTS as a fully benign, self-resolving condition (PMC12786540).

**Patterns:**
- Remission is typically spontaneous with supportive care; no disease-modifying pharmacotherapy is proven in randomized trials.
- Critical period: the acute 24–72-hour window is the period of highest risk for cardiogenic shock, LVOT obstruction, and malignant arrhythmia; the first 3–7 days is also the optimal imaging window for CMR-detected myocardial edema.

---

## 9. Inheritance and Population

**Epidemiology:**
- TTS accounts for **1–3% of all acute coronary syndrome presentations** and 0.5–0.9% of presentations initially thought to be STEMI.
- U.S. hospital discharge data: prevalence 5.2 per 100,000 for females vs. 0.6 per 100,000 for males; overall ~0.02% of hospitalizations. Annual incidence of TTS hospitalizations rose from 5.7/100,000 person-years (2007) to 17.4/100,000 (2012), reflecting rising recognition (https://pmc.ncbi.nlm.nih.gov/articles/PMC9999670/).

**Inheritance pattern:** No Mendelian inheritance pattern; **polygenic/multifactorial** susceptibility superimposed on an acute environmental (stress/catecholamine) trigger. No penetrance, expressivity, anticipation, germline mosaicism, or carrier-frequency data apply in the classical genetic-disease sense, since no causal variant/locus is established. Rare familial case reports exist but do not establish a consistent inheritance model (https://pmc.ncbi.nlm.nih.gov/articles/PMC12292538/).

**Population demographics:**
- **Sex ratio:** Strongly female-predominant — roughly 9:1 female:male in most registries (InterTAK: 89.8% postmenopausal women).
- **Age distribution:** Peak incidence in the 6th–8th decades; mean age ~66.8 years in InterTAK.
- **Geographic/ethnic distribution:** Recognized worldwide; originally described in Japan (Sato et al., 1990s), now diagnosed globally with increasing frequency attributed to greater clinical awareness and imaging availability rather than a true rise in underlying incidence alone. No strong evidence of founder populations or major ethnic-specific prevalence differences was identified in this search, though some registries (e.g., Palestine cohort, https://pmc.ncbi.nlm.nih.gov/articles/PMC10425303/) document regional prevalence among ACS-presenting patients.
- **Triggers cluster in disaster settings:** notable case-series clusters following mass psychosocial stress events (e.g., a consecutive case series following the 2011 Great East Japan Earthquake, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3363604/).

---

## 10. Diagnostics

**Clinical tests:**
- **Laboratory:** Cardiac troponin (mild-to-moderate elevation, disproportionately low relative to the extent of wall-motion abnormality), BNP/NT-proBNP (markedly and disproportionately elevated relative to troponin — the **BNP/troponin or NT-proBNP/troponin ratio** is a key discriminator from ACS; median BNP/troponin T ratio ~1,292 in TTS vs. ~226.9 in MI in one study) (https://pmc.ncbi.nlm.nih.gov/articles/PMC5633535/).
- **ECG:** Diffuse ST-segment elevation (mimicking anterior STEMI), later deep diffuse T-wave inversion, QTc prolongation.
- **Echocardiography:** First-line imaging; identifies transient regional wall-motion abnormality extending beyond a single coronary territory, dynamic LVOT obstruction, systolic anterior motion of the mitral valve, mitral regurgitation; speckle-tracking global longitudinal strain may remain abnormal even after LVEF normalizes.
- **Cardiac MRI:** Gold-standard adjunct — shows regional myocardial edema on T2-weighted/T2-mapping imaging **without** ischemic-pattern late gadolinium enhancement (contrasting with MI, and with a transmural rather than subepicardial/midmyocardial edema pattern distinguishing it from myocarditis); optimal within days 3–7 of presentation (https://pmc.ncbi.nlm.nih.gov/articles/PMC3996242/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10066439/).
- **Invasive coronary angiography:** Required in essentially all suspected cases to exclude obstructive coronary artery disease, given clinical overlap with ACS.
- **Endomyocardial biopsy (selected cases):** reversible focal myocytolysis, mononuclear (macrophage-predominant) infiltrates, contraction band necrosis without coagulative infarct-type necrosis (https://www.revespcardiol.org/en-histological-findings-in-tako-tsubo-syndrome-articulo-S1885585714004423).

**Genetic testing:** Not part of routine clinical diagnostic workup — no validated clinical gene panel exists given the absence of an established causal gene; genetic/GWAS studies remain research-stage only.

**Clinical/diagnostic criteria:**
- The current internationally accepted framework is the **InterTAK Diagnostic Criteria/Score** (Ghadri et al., European Heart Journal, and subsequent validation studies e.g. https://pmc.ncbi.nlm.nih.gov/articles/PMC12608723/), which incorporates: female sex, presence of an emotional or physical trigger, absence of significant coronary stenosis (or presence not fully explaining the wall-motion abnormality), transient regional wall-motion abnormality extending beyond a single coronary distribution, new ECG abnormalities (ST changes, QTc prolongation), significantly elevated NT-proBNP, relatively modest troponin elevation, and absence of myocarditis. The criteria also distinguish **primary TTS** (stress-activated, presenting as the primary reason for hospitalization) from **secondary TTS** (occurring in the context of another acute medical/surgical/neurological illness) — secondary TTS carries a worse prognosis.
- **Differential diagnosis:** Acute MI (obstructive or with spontaneous coronary recanalization), myocarditis (differentiated by CMR LGE pattern), pheochromocytoma crisis, and reverse/atypical variant confusion with other cardiomyopathies.

**Screening:** No population-level or genetic screening programs exist; recognition relies on clinical suspicion at presentation with an ACS-mimicking picture plus a stress trigger.

Suggested LOINC/diagnostic terms: cardiac troponin I/T panels, NT-proBNP, 12-lead ECG, transthoracic echocardiogram, cardiac MRI with T2 mapping and LGE sequences, coronary angiography.

---

## 11. Outcome/Prognosis

**Survival and mortality:**
- **In-hospital mortality:** ~2–6.5%, with some contemporary large registry data showing an **upward trend** (5.63% in 2016 to 8.38% in 2020) rather than the expected improvement, and **more than double mortality in men versus women** (11.2% vs. 5.5%) (https://www.ahajournals.org/doi/10.1161/JAHA.124.037219, PMID:40365782).
- **Long-term mortality:** 5-year mortality rates are reported as **comparable to those after acute myocardial infarction**, challenging the historical characterization of TTS as uniformly benign; much long-term mortality is attributable to non-cardiac comorbidities (cancer, neurologic disease) rather than the cardiac event itself (PMC12786540).

**Morbidity/complications:**
- Congestive heart failure ~35.9% (most common complication), atrial fibrillation ~20.7%, cardiogenic shock ~6.6–11.4%, cardiac arrest ~3.4%, stroke ~5.3%, LV thrombus 2–8%, LVOT obstruction up to 18–25% (https://pmc.ncbi.nlm.nih.gov/articles/PMC5005189/ — 101-case study of serious early complications and 2-year mortality).
- Predictors of cardiogenic shock: male sex, QTc prolongation, lower admission LVEF, physical (vs. emotional) trigger, significant intraventricular pressure gradient.

**Recovery/disease course:**
- Classic teaching: full LVEF recovery within days–weeks in the majority. However, **persistent subclinical dysfunction** (reduced global longitudinal strain, reduced myocardial energetic reserve on MR spectroscopy) is increasingly documented despite normalized LVEF, associated with ongoing fatigue, reduced exercise tolerance, and dyspnea.
- **Recurrence rate:** ~4–10% (commonly cited ~10%), often with a **different anatomical ballooning pattern** on recurrence, and more likely in patients with ongoing physical illness, psychiatric disease, or chronic emotional stress (GEIST Registry, https://www.ahajournals.org/doi/10.1161/JAHA.118.010753).

**Prognostic factors:**
- Male sex, secondary (vs. primary) TTS, physical/neurologic trigger, global (vs. apical) ballooning pattern, cardiogenic shock at presentation, delayed LVEF normalization, and active malignancy are associated with worse prognosis.
- Cardiac biomarker ratios (BNP/troponin) aid diagnosis but are not established prognostic tools per se.

---

## 12. Treatment

**Pharmacotherapy** (empiric/supportive — no agent has RCT-proven disease-modifying efficacy):
- **Beta-blockers** (NCIT:C15986 Pharmacotherapy; therapeutic_agent class NCIT — beta-adrenergic blocking agent): mechanistically attractive given the catecholamine-driven pathophysiology; evidence is **mixed** — a 28% reduction in all-cause mortality has been reported across pooled long-term-use studies (HR ~0.65, benefit more pronounced at 2–5 years than at 1 year), while propensity-matched analyses of **early/acute-phase** use show no significant effect on 30-day mortality or recurrence (https://www.jacc.org/doi/10.1016/j.jchf.2024.11.015 — GEIST Registry; https://www.sciencedirect.com/science/article/pii/S0870255123000458 — RETAKO Registry).
- **ACE inhibitors/ARBs:** associated with improved survival, particularly in patients with severe LV dysfunction (PMC12786540).
- **Diuretics:** for acute pulmonary congestion/fluid overload.
- **Mineralocorticoid receptor antagonists:** considered for pronounced LV dysfunction, analogous to standard HFrEF management.
- **Anticoagulation:** initiated for documented LV thrombus, extensive apical akinesis, or severely reduced EF, given the 2–8% thrombus incidence.
- **Antiarrhythmics/electrolyte management:** magnesium repletion and avoidance of QT-prolonging drugs given torsades risk in the setting of QTc prolongation.
- Notably, in **LVOT-obstruction-positive** patients, standard inotropic/positive-chronotropic heart-failure therapy is **contraindicated/harmful** since it worsens the dynamic obstruction; management instead favors cautious volume loading and afterload augmentation (e.g., phenylephrine-type pure vasoconstrictors) rather than inotropes.

**Surgical/interventional:** Not disease-directed (no surgical cure); catheter-based coronary angiography is diagnostic, not therapeutic, for TTS itself.

**Mechanical circulatory support (for refractory cardiogenic shock):**
- **Impella** (percutaneous LV assist device) is increasingly preferred over **intra-aortic balloon pump (IABP)** and **VA-ECMO** because it directly unloads the LV and is compatible with the LVOTO-prone physiology; IABP use has declined (13.6%→7.4%) while Impella use has risen (29%→59.3%) in recent cohorts. ECMO without concomitant LV unloading carries higher mortality/adverse events and can **paradoxically worsen LVOTO** by increasing afterload and impairing LV filling; device selection should be guided by pre-implantation assessment of LVOTO and LVEDP (https://pmc.ncbi.nlm.nih.gov/articles/PMC12142538/; https://pmc.ncbi.nlm.nih.gov/articles/PMC12197009/).
- VA-ECMO or the combined "ECMELLA" (ECMO + Impella) strategy is reserved for biventricular failure/most severe shock; these are **temporary bridge measures**, as most patients recover ventricular function within the acute phase.

**Supportive/rehabilitative (emerging disease-altering strategies):**
- Structured **cardiac rehabilitation** (guided aerobic + resistance training) has been shown in recent randomized data to improve exercise tolerance, restore autonomic function, and improve quality of life — described as among "the first long-term disease-altering approaches" for TTS.
- **Cognitive behavioral therapy (CBT)** may reduce anxiety, stress-reactivity, and recurrence risk of emotional triggers, particularly in primary or recurrent TTS.

**Experimental:** No approved targeted/disease-modifying pharmacotherapy exists; clinical trials (e.g., ClinicalTrials.gov NCT02307214 studying pathophysiology, NCT05977049 on psychosocial support) are ongoing rather than pivotal therapeutic trials.

**Suggested NCIT treatment terms:**
- NCIT:C15986 Pharmacotherapy (generic, for beta-blockers, ACE inhibitors/ARBs, diuretics)
- NCIT:C15747 Supportive Care
- NCIT:C15302 Physical Therapy / cardiac rehabilitation (closest fit)
- NCIT:C49236 Therapeutic Procedure (for mechanical circulatory support)
- Therapeutic modality tagging: `SMALL_MOLECULE` for beta-blockers/ACEi/ARBs; `DEVICE` for Impella/IABP/ECMO; `BEHAVIORAL` for cardiac rehabilitation and CBT.

**Treatment outcomes:** No standardized treatment algorithm/guideline dedicated to TTS exists (unlike ACS or HFrEF); management is extrapolated from heart-failure principles with modifications for the reversible, catecholamine-driven, LVOTO-prone physiology (acknowledged explicitly in the literature as a diagnosis/management gap: "diagnosis and clinical management lacks standardized guidelines").

---

## 13. Prevention

- **Primary prevention:** No established primary prevention strategy exists at the population level, since triggers are heterogeneous and largely unpredictable (acute emotional/physical stress, iatrogenic catecholamine exposure). Avoidance of unnecessary exogenous catecholamine administration (e.g., cautious dobutamine stress test use, epinephrine dosing in at-risk patients) is a plausible but unproven mitigation.
- **Secondary prevention:** Early recognition via InterTAK criteria and imaging in patients presenting with ACS-mimicking symptoms after a stress trigger; screening for LVOT obstruction before administering inotropes.
- **Tertiary prevention:** Long-term beta-blocker/ACEi therapy (of debated efficacy), structured cardiac rehabilitation, and CBT to reduce recurrence and improve functional/psychological recovery, as detailed above.
- **Behavioral interventions:** Stress-reduction and psychological support programs (targeting the ~50–65% of cases with an identifiable emotional trigger and the high comorbid anxiety/mood-disorder burden) are an active area of clinical investigation (e.g., NCT05977049, "Psychosocial Support for Patients With Takotsubo Syndrome").
- **Counseling:** No genetic counseling role given lack of established heritable causal variant; psychological counseling/psychiatric referral is relevant given the high burden of comorbid mood/anxiety disorders and post-event PTSD symptoms.
- **Public health:** Not applicable in the classical infectious/environmental public-health sense; population-level stress/disaster preparedness (given documented case clustering after mass-stress events such as earthquakes) is a tangential consideration.
- **Prophylaxis:** No established pharmacologic prophylaxis for at-risk individuals (e.g., prior TTS survivors) beyond secondary-prevention beta-blockade/ACEi noted above, and no consensus on its efficacy.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** TTS/stress cardiomyopathy is predominantly documented in **humans** (NCBITaxon:9606). This search did not identify robust peer-reviewed veterinary literature documenting naturally occurring takotsubo-pattern cardiomyopathy in companion animals or wildlife (e.g., no confirmed dolphin or other marine-mammal natural-disease reports were found); anecdotal/lay references to "broken heart syndrome" in animals were not substantiated by primary veterinary literature in this search.
- **Gene:** Orthologous adrenergic receptor genes (Adrb1, Adrb2, Adra2c) are well conserved across mammals and are the genes manipulated/monitored in rodent and primate experimental models (below), but this reflects experimental induction rather than naturally occurring veterinary disease.
- **Comparative biology:** The catecholamine-toxicity/contraction-band-necrosis mechanism is broadly conserved and is well documented in **experimentally induced** animal models (see Section 15) and in naturally occurring human catecholamine-excess states (pheochromocytoma, subarachnoid hemorrhage), supporting cross-context mechanistic conservation even without confirmed spontaneous non-human disease.
- **Transmission:** Not applicable — TTS is not an infectious or zoonotic condition.

---

## 15. Model Organisms

TTS has a well-developed **induced (non-genetic) animal model literature**, since it is fundamentally a stress/catecholamine-response phenotype rather than a Mendelian genetic disease (comprehensive review: "Animal models of Takotsubo syndrome: bridging the gap to the human condition," 2024, https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2024.1351587/full).

- **Rodent immobilization-stress model (rat):** Ueyama et al. (2002/2003) first restrained rats supine for ~30 minutes, producing intense emotional/physical stress, elevated plasma catecholamines, reversible ST-segment elevation, and reversible LV apical ballooning on ventriculography — normalized by combined α- and β-adrenoceptor blockade, establishing causality for the adrenergic mechanism (https://pubmed.ncbi.nlm.nih.gov/15240400/). Subsequent refinements (6 hours/day immobilization for 1–14 days) show local sympathetic cardiac remodeling by day 1, increasing ventricular tachyarrhythmia induction by day 3, and peak TTS-pattern incidence around day 5.
- **Catecholamine-infusion models (rat, primate):** Intraperitoneal or intravenous catecholamine (epinephrine) administration reproduces takotsubo-like apical dysfunction and increased apical myocytolysis; infusion studies in **non-human primates** (monkeys) similarly produce apex-predominant myocytolysis with IV epinephrine infusion.
- **Hyperthermia-trigger rat model:** demonstrates that non-catecholamine physical stressors (heat stress) can also trigger the TTS phenotype, broadening the model beyond pure catecholamine infusion (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9360576/).
- **Receptor-blockade/genetic-pathway dissection:** β1-adrenergic receptor blockade prevents stress-induced cardiac injury in rodent models, and studies of adrenergic/muscarinic receptor roles in stress-induced cardiac injury further dissect the relative contributions of sympathetic vs. parasympathetic signaling (https://link.springer.com/article/10.1007/s00424-021-02602-6).
- **Genetic models (knockout/transgenic):** No widely used TTS-specific knockout/transgenic mouse line was identified in this search; existing models are predominantly pharmacologic/physical-stress induction in wild-type rodents rather than genetically engineered.

**Phenotype recapitulation:** Rodent immobilization and catecholamine-infusion models reproduce the core TTS triad — reversible apical wall-motion abnormality, ECG ST-segment changes, and catecholamine elevation — and the pharmacologic reversibility with combined adrenoceptor blockade strongly supports the catecholamine-toxicity mechanism. **Limitations:** rodent/primate models do not recapitulate the strong human female/postmenopausal sex bias as robustly, nor the human brain-heart axis (limbic/insular) findings, nor long-term human recurrence and subclinical-dysfunction patterns; translational fidelity to human neuro-cardiac circuitry remains an open question (a candidate `HUMAN_MODEL_MISMATCH` framing for a dismech entry, given documented sex-hormone-dependent human epidemiology not fully modeled in most rodent paradigms).

**Model databases/resources:** No dedicated TTS model-organism strain repository was identified; models are custom-induced (immobilization, restraint, catecholamine infusion) rather than sourced from standard repositories like MGI/IMPC/JAX allele catalogs, consistent with the non-genetic, stress-induction paradigm.

---

## Summary Table of Suggested Ontology Terms for KB Curation

| Category | Term ID | Label |
|---|---|---|
| Disease (MONDO) | MONDO:0019018 | Takotsubo cardiomyopathy |
| Disease (Orphanet) | ORPHA:66529 | Tako-Tsubo cardiomyopathy |
| Phenotype (HP) | HP:0100749 | Chest pain |
| Phenotype (HP) | HP:0002094 | Dyspnea |
| Phenotype (HP) | HP:0001657 | Long QT interval |
| Phenotype (HP) | HP:0005110 | Atrial fibrillation |
| Phenotype (HP) | HP:0001635 | Congestive heart failure |
| Phenotype (HP) | HP:0001279 | Syncope |
| Phenotype (HP) | HP:0001653 | Mitral regurgitation |
| Cell type (CL) | CL:0000746 | Cardiac muscle myocyte |
| Cell type (CL) | CL:0000235 | Macrophage |
| Cell type (CL) | CL:0000166 | Chromaffin cell |
| GO Biological Process | GO:0071870 | Cellular response to catecholamine stimulus |
| GO Biological Process | GO:0006979 | Response to oxidative stress |
| GO Biological Process | GO:0055074 | Calcium ion homeostasis |
| GO Biological Process | GO:0006954 | Inflammatory response |
| UBERON | UBERON:0002084 | Heart left ventricle |
| UBERON | UBERON:0002094 | Left cardiac atrium (context) |
| CHEBI | CHEBI:33569 | Epinephrine |
| CHEBI | CHEBI:33569-adjacent | Norepinephrine (CHEBI:18357) |
| NCIT treatment | NCIT:C15986 | Pharmacotherapy |
| NCIT treatment | NCIT:C15747 | Supportive Care |
| NCIT treatment | NCIT:C15302 | Physical Therapy (cardiac rehab proxy) |

---

## Key Source Citations

- Ravindran et al., 2024, *Intern Med J*, "Clinical perspectives: Takotsubo cardiomyopathy," https://onlinelibrary.wiley.com/doi/10.1111/imj.16493
- Ghadri et al., 2022, *Circulation*, "Takotsubo Syndrome: Pathophysiology, Emerging Concepts, and Clinical Implications," https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.121.055854
- McKenzie & Bargout, 2025, *J Clin Med* (PMID:41517446 / PMC12786540), "Takotsubo Syndrome in 2025: Evolving Concepts in Pathophysiology, Diagnosis, and Long-Term Management," https://pmc.ncbi.nlm.nih.gov/articles/PMC12786540/
- Y-Hassan & Falhammar, 2025 (PMID:40723798 / PMC12292538), "The Genetic Puzzle of the Stress-Induced Cardiomyopathy (Takotsubo Syndrome)," https://pmc.ncbi.nlm.nih.gov/articles/PMC12292538/
- Templin et al., 2019, *Eur Heart J* (PMID:30831580), "Altered limbic and autonomic processing supports brain-heart axis in Takotsubo syndrome"
- Dichtl et al., 2020 (PMID:32002630), "Functional neuroimaging in the acute phase of Takotsubo syndrome"
- Scally et al., 2019, *Circulation* (JACC Basic Transl Sci companion; PMID:30586731), "Myocardial and Systemic Inflammation in Acute Stress-Induced (Takotsubo) Cardiomyopathy"
- PMC9999670, "Epidemiology, Pathophysiology, Diagnosis, and Principles of Management of Takotsubo Cardiomyopathy: A Review"
- JAHA 2025 (PMID:40365782), "High Mortality and Complications in Patients Admitted With Takotsubo Cardiomyopathy"
- JACC Heart Failure 2024, GEIST Registry, "Beta-Blockers and Long-Term Mortality in Takotsubo Syndrome," https://www.jacc.org/doi/10.1016/j.jchf.2024.11.015
- Ueyama et al., 2004 (PMID:15240400), "Emotional stress-induced Tako-tsubo cardiomyopathy: animal model and molecular mechanism"
- PMC12142538, "Trends and outcomes of different mechanical circulatory support modalities for refractory cardiogenic shock in Takotsubo cardiomyopathy"
- PMC9666486 / PMC10800806, cancer-TTS association literature
- BMC Med Genet 2018 (PMC5842616), "Lack of genetic susceptibility in takotsubo cardiomyopathy: a case-control study"