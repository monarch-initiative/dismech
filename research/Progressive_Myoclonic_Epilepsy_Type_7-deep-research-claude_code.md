---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T20:12:30.043406'
end_time: '2026-08-10T20:18:37.323783'
duration_seconds: 367.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Progressive Myoclonic Epilepsy Type 7
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 15
  num_turns: 29
  total_cost_usd: 2.2164701
  session_id: 991c042b-67a3-550d-b3e7-f2f9959e7354
  stop_reason: end_turn
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Myoclonic Epilepsy Type 7
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Progressive Myoclonic Epilepsy Type 7** covering all of the
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

# Progressive Myoclonic Epilepsy Type 7 (EPM7 / KCNC1-Related Disorders / MEAK)
## Comprehensive Research Report

---

## 1. Disease Information

**Overview.** Progressive Myoclonic Epilepsy Type 7 (EPM7) is a rare autosomal dominant neurologic channelopathy caused by heterozygous variants in *KCNC1*, the gene encoding the voltage-gated potassium channel subunit Kv3.1. The classic, most extensively characterized phenotype is **Myoclonus Epilepsy and Ataxia due to Potassium (K⁺) channel mutation (MEAK)**, defined by childhood/adolescent-onset progressive action myoclonus that becomes severely disabling, infrequent generalized tonic-clonic seizures, and progressive ataxia. *KCNC1* variants are now recognized to cause a broader phenotypic spectrum, collectively termed **KCNC1-related disorders**, ranging from MEAK/EPM7 at the severe-progressive end, through infantile-onset drug-resistant developmental and epileptic encephalopathy (DEE), to isolated non-progressive myoclonus or intellectual disability without seizures at the mild end (GeneReviews, NBK619809).

**Key identifiers:**
- **OMIM phenotype:** #616187 — "EPILEPSY, PROGRESSIVE MYOCLONIC 7; EPM7" ([OMIM](https://www.omim.org/entry/616187))
- **OMIM gene:** *176258 — "POTASSIUM CHANNEL, VOLTAGE-GATED, SHAW-RELATED SUBFAMILY, MEMBER 1; KCNC1" ([OMIM](https://omim.org/entry/176258))
- **Orphanet:** ORPHA:435438 — "Progressive myoclonic epilepsy type 7" ([Orphanet](https://www.orpha.net/en/disease/detail/435438))
- **MONDO:** MONDO:0014521
- **Gene:** HGNC:6233 (*KCNC1*), chromosome **11p15.1** (per GeneCards/OMIM; some sources list 11p15)
- **MedGen:** C4015420

**Synonyms:** EPM7; Myoclonic epilepsy and ataxia due to potassium (K⁺) channel mutation (MEAK); Myoclonus epilepsy and ataxia due to KCNC1 mutation; KCNC1-related progressive myoclonus epilepsy; KCNC1-related developmental and epileptic encephalopathy (for the infantile-onset end of the spectrum). Gene aliases: KV3.1, KV4, NGK2.

**Evidence basis.** Knowledge of this disease derives almost entirely from **aggregated case series and case reports** in the medical literature (exome-sequencing cohorts of progressive myoclonus epilepsy of unknown cause, GeneReviews summaries, individual/familial case reports), supplemented by **functional/electrophysiological studies** (heterologous expression in *Xenopus* oocytes and mammalian cell lines) and **mouse models**. There is no large population-based EHR resource for this ultra-rare disease; GeneReviews estimates "approximately 60 individuals with a KCNC1-related disorder have been reported in the literature to date."

---

## 2. Etiology

**Disease causal factor — purely genetic.** EPM7/MEAK is caused by **heterozygous, almost always de novo, pathogenic variants in *KCNC1*** (OMIM 616187; GeneReviews NBK619809). There is no known infectious, autoimmune, or acquired cause; this is a monogenic channelopathy.

**Genetic risk factors:**
- The **recurrent missense variant c.959G>A (p.Arg320His)** in the S4 voltage-sensor segment of Kv3.1 is by far the most common cause of MEAK. It was identified in 13/84 (≈13% of the exome-sequenced cohort, plus additional cases from a secondary cohort) individuals with progressive myoclonus epilepsy of unknown etiology in the landmark discovery study (Muona et al., *Nat Genet* 2015; PMID: [25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/)). Functional studies in *Xenopus* oocytes showed the mutant channel produced "significantly smaller potassium currents" than wild type, and when co-expressed with wild-type subunits produced a **dominant-negative loss-of-function effect**, with current amplitude reduced roughly fourfold — consistent with Kv3 channels' obligate tetrameric assembly (one mutant subunit poisons the whole channel).
- Additional pathogenic/likely pathogenic variants causing the broader spectrum: **p.Ala421Val** (recurrent, DEE), **p.Cys208Tyr**, **p.Thr399Met**, **p.Arg317His**, **p.Arg339*** (nonsense), **p.Gln492*** (Oliver et al. *Ann Neurol* 2017, PMID: [31353855](https://pubmed.ncbi.nlm.nih.gov/31353855/) [note: this PMID corresponds to the "Encephalopathies with KCNC1 variants" genotype-phenotype-functional-correlation paper]; Muona et al., PMID: [31353862](https://pubmed.ncbi.nlm.nih.gov/31353862/)).
- **No population allele frequency** — the R320H variant and other pathogenic *KCNC1* variants are essentially absent from population reference databases (gnomAD), consistent with de novo occurrence and severe phenotype.
- **Parental (germline/somatic) mosaicism** has been documented as a rare but clinically important risk modifier: a case report describes two affected brothers with classic MEAK (near-normal early development, myoclonus onset ~age 10, infrequent generalized seizures, mild cognitive decline) born to an **asymptomatic mother carrying the p.Arg320His variant in mosaic form** (Yano et al., *Brain Dev* 2018; PMID: [29428275](https://pubmed.ncbi.nlm.nih.gov/29428275/)). This raises recurrence risk in future pregnancies above the background de novo rate despite an unaffected parent.

**Environmental risk factors:** None established. This is a pure Mendelian channelopathy; there is no evidence for toxin, infectious, or lifestyle contribution to disease initiation.

**Protective factors:** None specifically described for *KCNC1*/EPM7 in the literature reviewed.

**Gene-environment interactions:** Not applicable/not reported — no GxE data exist for this monogenic disorder. (Photic stimulation is a seizure/myoclonus *trigger* via EEG photosensitivity, discussed under Phenotypes, but this is a symptom-provocation phenomenon rather than a disease-causing environmental factor.)

---

## 3. Phenotypes

### Classic MEAK/EPM7 phenotype (the "progressive" severe form)

| Phenotype | Frequency (from GeneReviews KCNC1-Related Disorders summary) | Suggested HPO term |
|---|---|---|
| Progressive action myoclonus | ~100% | HP:0001336 (Myoclonus) |
| Generalized tonic-clonic seizures (infrequent) | ~97% | HP:0002069 (Bilateral tonic-clonic seizure) |
| Progressive ataxia | ~97% | HP:0001251 (Ataxia) / HP:0002066 (Gait ataxia) |
| Mild cognitive decline (post-seizure-onset) | ~57% | HP:0007288 (Cognitive decline, suggested — verify) |
| Cerebellar atrophy (MRI) | 32.6% (15/46 in a pooled literature analysis) | HP:0001272 (Cerebellar atrophy) |
| Abnormal/epileptiform EEG | ~87% | HP:0002353 (EEG abnormality, suggested) |
| EEG photosensitivity | Documented in most reported cases | (photoparoxysmal response — verify exact HPO code) |
| Dysmetria, gaze-evoked nystagmus, truncal ataxia | Common exam findings | HP:0000640 (Dysmetria, suggested); HP:0000639 (Nystagmus) |
| Tremor | Reported (e.g., intention tremor from age 4–5 in the DBS case report) | HP:0001337 (Tremor) |
| Learning disability preceding seizure onset | Reported by Orphanet | HP:0001328 (Specific learning disability, suggested) |

**Onset and course:** Myoclonus typically begins **age 6–14 years (mean ~10 years)**; generalized seizures usually emerge in adolescence and can continue into the third or fourth decade; ataxia is progressive and, per Orphanet, "generally becomes disabling in adolescence, with most patients becoming wheelchair-bound." GeneReviews states approximately half of affected individuals require a walking aid or wheelchair by late adolescence/early adulthood. Cognitive impairment is not a prominent early feature — early development is typically near-normal — but mild decline can occur after seizure onset in roughly half of patients. Dementia has not been reported.

### Developmental and Epileptic Encephalopathy (DEE) phenotype (the infantile-onset severe end)

Associated recurrently with **p.Ala421Val**: infantile-onset (typically <10 months of age), **drug-resistant epilepsy with multiple seizure types** (myoclonic, absence, generalized tonic-clonic), **moderate-to-severe global developmental delay/intellectual disability (100%)** without regression, **non-progressive ataxia (~75%)**, myoclonus in about a third of cases, and feeding difficulties/failure to thrive. Suggested HPO: HP:0200134 (Infantile spasm, if applicable), HP:0011097 (Epileptic spasm), HP:0001263 (Global developmental delay), HP:0001508 (Failure to thrive), HP:0011968 (Feeding difficulties).

### Milder end of spectrum

- **Isolated non-progressive myoclonus** (p.Cys208Tyr)
- **Intellectual disability without seizures or epilepsy**, associated with the nonsense variant **p.Arg339***, which acts via nonsense-mediated decay/haploinsufficiency rather than dominant-negative mechanism. Affected individuals across three generations of one family showed delayed motor milestones, speech delay, ID with attention difficulties, hypotonia, and dysmorphic features (epicanthal folds, ptosis, short philtrum, prognathism), with **notable absence of seizures** (Muona/Oliver group, PMC5437909). Suggested HPO: HP:0001256 (Intellectual disability, mild), HP:0001252 (Hypotonia).
- **Developmental encephalopathy without seizures** (p.Arg317His, p.Gln492*)
- Autism spectrum features reported in some individuals.

**Quality-of-life impact:** No disease-specific EQ-5D/SF-36 data were identified in this search, but the natural-history literature (GeneReviews, case reports) documents major functional impact from progressive ataxia/wheelchair dependence and disabling myoclonus interfering with voluntary movement, feeding, and independence, particularly in adolescence/early adulthood for MEAK and from infancy for DEE.

---

## 4. Genetic/Molecular Information

**Causal gene:** ***KCNC1*** (HGNC:6233; OMIM *176258), encoding **Kv3.1**, a member of the Shaw-related (Kv3) subfamily of voltage-gated, tetrameric potassium channels. Chromosome 11p15.1.

**Variant classes and functional consequences:**

| Variant (protein) | cDNA | Domain | Mechanism | Associated phenotype |
|---|---|---|---|---|
| p.Arg320His | c.959G>A | S4 voltage-sensor | Dominant-negative loss of function (~4-fold current reduction in heteromeric channels) | MEAK/EPM7 (classic, recurrent) |
| p.Ala421Val | c.1262C>T | S6/pore-adjacent | Near-complete loss of function; dominant-negative reported in some studies, absent in others (mechanistic nuance still debated) | DEE (recurrent, 6 unrelated patients in one series) |
| p.Cys208Tyr | — | — | Loss of function (no measurable current) | Isolated non-progressive myoclonus |
| p.Thr399Met | — | — | Loss of function with dominant-negative activity | Intellectual disability |
| p.Arg339* | c.1015C>T | Premature stop | **Haploinsufficiency** via nonsense-mediated mRNA decay (>50% transcript reduction in patient fibroblasts) — mechanistically distinct from the dominant-negative missense variants | ID without seizures/epilepsy |
| p.Arg317His, p.Gln492* | — | — | Dominant-negative / loss of function | Developmental encephalopathy without seizures |
| p.Ala513Val | c.1538C>T | — | Variant of uncertain significance | — |

Functional analyses in the KCNC1-related-disorders discovery papers concluded broadly: *"Functional analyses demonstrated no measurable currents for all identified variants"* in heterologous expression, with dominant-negative activity specifically demonstrated for p.Thr399Met and p.Ala421Val in at least one study, predicting **neuronal disinhibition** as the shared downstream mechanism (PMID: 31353862).

**Zygosity/inheritance:** Heterozygous, autosomal dominant. **Predominantly de novo** (>95% of tested probands per GeneReviews); rare instances of **inheritance from a mosaic or subtly-affected parent** are documented (PMID: 29428275).

**Population frequency:** Not present in gnomAD/population databases (consistent with de novo severe disease). GeneReviews estimates the MEAK-causing c.959G>A allele arises at a rate corresponding to roughly **1 per 5,700,000 conceptions**.

**Epigenetics/chromosomal abnormalities:** No epigenetic mechanism (DNA methylation, histone modification) or large chromosomal rearrangement has been reported as causal for EPM7; this is a single-gene, sequence-level channelopathy.

**Modifier genes:** None specifically established; phenotypic variability is attributed primarily to which *KCNC1* variant is present (genotype-phenotype correlation) rather than to a distinct modifier locus.

**Suggested ontology terms:** HGNC:6233 (*KCNC1*); GO:0005249 (voltage-gated potassium channel activity, suggested — verify); GO:0071805 (potassium ion transmembrane transport, suggested — verify); GO:0001508 (regulation of action potential, suggested — verify).

---

## 5. Environmental Information

No environmental factors (toxins, radiation, occupational exposures), lifestyle factors, or infectious agents have been implicated in causing EPM7/KCNC1-related disorders — this is consistent with its status as a highly penetrant monogenic de novo channelopathy. The one environmentally-modulated clinical phenomenon is **photosensitivity**: EEG in KCNC1-related PME frequently shows a photoparoxysmal response, i.e., photic stimulation can provoke epileptiform discharges/myoclonus in susceptible patients, which is a clinical trigger relevant to seizure/myoclonus precipitation rather than a cause of the underlying disease.

---

## 6. Mechanism / Pathophysiology

**Molecular pathway / protein function.** Kv3.1 is a member of the Kv3 (Shaw-related) subfamily of voltage-gated K⁺ channels (KCNC1–4, giving Kv3.1–3.4), distinguished biophysically by **depolarized voltage-dependence of activation and very rapid activation/deactivation kinetics**. This biophysical profile is what permits **high-frequency, sustained action potential firing** in specific neuron populations. Kv3.1/Kv3.2 are the dominant Kv3 subunits in **parvalbumin-positive (PV+) fast-spiking GABAergic interneurons** of the cerebral cortex, and Kv3.1/Kv3.3 are highly expressed in **cerebellar granule cells and Purkinje cells**, where they support rapid repolarization needed for high-frequency spiking and reliable, rapid GABAergic inhibitory neurotransmission.

**Causal chain (loss-of-function variants, e.g., p.Arg320His):**
1. **Trigger:** heterozygous de novo missense variant in the *KCNC1* S4 voltage sensor (or pore-adjacent regions for other variants).
2. **Molecular consequence:** because Kv3 channels are obligate homo/heterotetramers, one mutant subunit poisons the channel complex, producing a **dominant-negative loss of potassium current** far in excess of the 50% predicted by simple haploinsufficiency — up to ~4-fold reduction for R320H.
3. **Cellular consequence:** PV+ fast-spiking interneurons and Kv3.1-dependent cerebellar granule/Purkinje neurons lose their capacity to sustain high-frequency firing ("cells expressing R320H were unable to support high-frequency firing," Carpenter et al., *Epilepsia* 2021; PMID: [33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/)).
4. **Developmental/structural consequence — "developmental dendritopathy":** In primary mouse cortical interneuron culture, expressing R320H Kv3.1 "severely impair[ed] neurite development and interneuron viability" — 85.7% of mutant-expressing neurons had undetectable neuronal processes by 7 days in vitro (vs. ~28–31% in controls), with reduced total dendritic length, impaired dendritic arborization, and increased markers of apoptotic cell death (TUNEL-positivity by 72h, proapoptotic nuclear changes by 48h). Notably, this dendritic/viability phenotype occurred **independent of ion-conduction blockade** ("no gating pore currents detected"), i.e., a non-conducting, structural/developmental toxicity of the mutant protein compounds the electrophysiological loss of function. The authors conclude *"MEAK may be described as a developmental dendritopathy."*
5. **Network/circuit consequence:** loss of fast-spiking PV+ interneuron function and cerebellar Kv3.1-dependent output produces **network disinhibition** — reduced GABAergic inhibitory tone in cortex, and disrupted cerebellar Purkinje/deep cerebellar nuclei output governing motor coordination.
6. **Clinical manifestation:** cortical disinhibition and impaired high-frequency interneuron firing manifest as **cortical myoclonus and generalized epilepsy**; cerebellar circuit dysfunction manifests as **progressive ataxia** and cerebellar atrophy on imaging.

**Mouse model confirmation (in vivo):** A knock-in **Kcnc1-p.Arg320His/+** heterozygous mouse recapitulates core EPM7 features — progressive ataxia and increased seizure susceptibility. Studies in adult heterozygous mice showed loss of Kv3.1 function "alters excitability and synaptic neurotransmission" in both cerebral cortex PV+ interneurons and cerebellar granule cells. A parallel **Kcnc1-p.Ala421Val** transgenic mouse model shows even more severe loss of Kv3.1 function, with decreased PV-interneuron surface channel expression, decreased voltage-gated K⁺ current density, profound impairment of PV-interneuron intrinsic excitability, cognitive impairment, epilepsy, and premature lethality — mechanistically consistent with its more severe, earlier-onset DEE phenotype in humans (eLife 2024/2025 preprint/PMC12916103; bioRxiv 10.1101/2024.09.27.615463).

**Nonsense/haploinsufficiency mechanism (p.Arg339\*):** distinct from the dominant-negative missense mechanism — the premature stop codon triggers nonsense-mediated decay, reducing *KCNC1* transcript by >50% in patient fibroblasts without producing a dominant-negative truncated protein. This **simple haploinsufficiency** is proposed to explain the milder, seizure-free ID phenotype, potentially via disrupted non-canonical roles of Kv3.1 in cell proliferation, migration, and neuronal growth-cone dynamics during brain development, rather than through mature-neuron hyperexcitability defects.

**Cell types involved (suggested CL terms — verify before curation):** fast-spiking parvalbumin-positive GABAergic interneuron (cerebral cortex); cerebellar granule cell (CL:0001031, suggested); Purkinje cell (CL:0000121, suggested); deep cerebellar nuclei neurons.

**Biological processes (suggested GO terms — verify before curation):** GO:0006813 (potassium ion transport); GO:0005249 (voltage-gated potassium channel activity); regulation of neuronal action potential/high-frequency firing; GABAergic synaptic transmission; neurite/dendrite development; apoptotic process (developmental interneuron death).

**Molecular profiling / advanced technologies:** No transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to human KCNC1-related PME were identified in this search; the mechanistic data derive from heterologous electrophysiology (*Xenopus* oocytes, mammalian cell lines), primary neuronal culture, and knock-in/transgenic mouse models rather than -omics profiling.

---

## 7. Anatomical Structures Affected

**Organ level:** Central nervous system exclusively — **cerebellum** (ataxia, cerebellar atrophy) and **cerebral cortex** (myoclonus, seizures). No consistent extra-neurological organ involvement is described for classic MEAK; DEE cases can show secondary feeding/growth problems (failure to thrive) as a consequence of severe encephalopathy rather than primary organ pathology.

**Body systems:** Nervous system (primary); secondary musculoskeletal effects of progressive ataxia (gait impairment, wheelchair dependence).

**Tissue/cell level:**
- Cerebellar cortex: Purkinje cells and granule cells (high Kv3.1/Kv3.3 expression, critical for cerebellar output and motor coordination)
- Cerebral cortex: parvalbumin-positive (PV+) fast-spiking GABAergic interneurons (high Kv3.1/Kv3.2 expression, critical for cortical inhibitory tone and network synchrony)
- Deep cerebellar nuclei (relay of Purkinje output)

**Subcellular level (suggested GO Cellular Component terms — verify):** plasma membrane (voltage-gated channel localization); dendrites/neurites (site of the developmental dendritopathy phenotype); growth cone (proposed site of non-canonical Kv3.1 function relevant to the haploinsufficiency ID phenotype).

**Anatomical localization (suggested UBERON terms — verify):** UBERON:0002037 (cerebellum); UBERON:0002771 (cerebellar cortex); UBERON:0000956 (cerebral cortex); UBERON:0000955 (brain).

**Lateralization:** Bilateral/symmetric — myoclonus, ataxia, and cerebellar atrophy are described as generalized/bilateral, consistent with a diffuse channelopathy rather than a focal lesion.

---

## 8. Temporal Development

**Onset:**
- **MEAK/EPM7 (classic form):** Insidious, childhood-to-adolescent onset. Myoclonus typically begins age 6–14 years (mean ~10); one detailed case documented intention tremor from age 4–5 progressing to myoclonic jerks and ataxia, with first generalized tonic-clonic seizure at age 22.
- **DEE form:** Acute/early — infantile onset, typically before 10 months of age, with drug-resistant epilepsy as the presenting feature alongside global developmental delay.
- **Milder ID/isolated-myoclonus phenotypes:** Developmental delay apparent in infancy/early childhood; myoclonus can be present from an early age but non-progressive.

**Progression:**
- MEAK is explicitly **progressive**: myoclonus becomes increasingly severe and disabling through adolescence, ataxia worsens, and roughly half of patients become dependent on a walking aid or wheelchair by late adolescence/early adulthood. Mild cognitive decline can occur after seizure onset in about half of patients, but frank dementia is not reported.
- DEE is a **static-to-progressive encephalopathy** — epilepsy is drug-resistant from infancy, and ataxia/myoclonus in this group are generally **non-progressive**, distinguishing it mechanistically and prognostically from MEAK despite both arising from *KCNC1* loss of function.
- Milder ID phenotypes (e.g., p.Arg339*) are **non-progressive**; no developmental regression reported.

**Disease course pattern:** Chronic, lifelong, and (in MEAK) progressive; not relapsing-remitting. Rare reports of partial symptomatic improvement with targeted treatment (e.g., DBS reducing myoclonus by 30–100% per prior case-series data cited in the MEAK DBS report) represent treatment response rather than spontaneous remission.

**Critical periods:** The "developmental dendritopathy" mechanism suggests a developmental window during interneuron maturation (dendritic outgrowth, viability) is specifically vulnerable to R320H toxicity — a potential mechanistic explanation for why the phenotype, though genetically present from conception, manifests progressively over childhood/adolescence as circuit maturation proceeds and interneuron networks are increasingly stressed.

---

## 9. Inheritance and Population

**Epidemiology:** EPM7 is an ultra-rare disease. GeneReviews states approximately **60 individuals with a KCNC1-related disorder** have been reported in the literature to date (across the full phenotypic spectrum — MEAK, DEE, and milder ID/myoclonus phenotypes). GeneReviews further estimates the specific MEAK-causing c.959G>A allele arises at a rate of roughly **1 per 5,700,000 conceptions**. No formal point-prevalence or incidence figure (e.g., Orphanet prevalence class) was located in this search; the disease should likely be classified in the "not yet documented" / ultra-rare Orphanet prevalence band pending a dedicated epidemiological study.

**Inheritance pattern:** Autosomal dominant (AD). The overwhelming majority of cases are **de novo**. Rare instances of transmission from a parent are attributable to **germline/somatic mosaicism** in an otherwise unaffected or subtly-affected parent (documented for p.Arg320His; PMID: 29428275) rather than to reduced penetrance in a fully heterozygous parent — i.e., true inherited transmission from a fully affected, non-mosaic parent has not been well documented, consistent with the severity of the phenotype limiting reproductive fitness.

**Penetrance:** The recurrent p.Arg320His variant is described as producing a "highly penetrant and specific" MEAK phenotype (PMID: 25401298) — i.e., essentially full penetrance for the classic syndrome when present in non-mosaic heterozygous form.

**Expressivity:** Variable across the *KCNC1* allelic series — the same gene produces phenotypes ranging from isolated non-progressive myoclonus to severe infantile DEE to progressive MEAK to ID without seizures, depending on the specific variant and its precise functional consequence (simple loss of function vs. dominant-negative vs. haploinsufficiency). Within the MEAK/R320H group specifically, expressivity is comparatively consistent (a defined triad of myoclonus–seizures–ataxia).

**Genetic anticipation:** Not reported/not applicable — this is not a repeat-expansion disorder.

**Germline/somatic mosaicism:** Documented and clinically important (see Etiology and Genetics sections) — critical for accurate genetic counseling, since an apparently sporadic de novo case in a family can recur in a subsequent pregnancy if a parent carries low-level mosaicism.

**Founder effects / consanguinity / carrier frequency:** No founder populations or consanguinity association reported — consistent with a dominant, essentially always de novo disorder rather than a recessive trait with population-specific carrier frequency. There is no meaningful "carrier frequency" concept for this AD, near-fully-penetrant, mostly de novo disease.

**Population demographics:** No specific ethnic, geographic, or sex-ratio predilection was identified in the literature reviewed; cases have been reported from multiple exome-sequencing cohorts internationally (the original Muona et al. 2015 discovery cohort drew from an international collection of 84 unrelated PME cases of unknown etiology). No age-distribution skew beyond the expected childhood/adolescent (MEAK) vs. infantile (DEE) onset windows described above.

---

## 10. Diagnostics

**Establishing the diagnosis:** Per GeneReviews, "the diagnosis of KCNC1-related disorders is established in a proband with suggestive findings and a heterozygous pathogenic variant in *KCNC1* identified by molecular genetic testing."

**Genetic testing approach:**
- **Preferred first-tier test:** a multigene epilepsy/PME panel (including *KCNC1* along with other PME genes) or comprehensive **exome/genome sequencing**, given the phenotypic overlap with other PME etiologies.
- **Single-gene *KCNC1* testing is not recommended** as a first step given genetic heterogeneity of PME.
- Variants of uncertain significance (e.g., p.Ala513Val) do not, by themselves, establish the diagnosis.
- **Parental testing** (including assessment for low-level mosaicism where feasible) is recommended for accurate recurrence-risk counseling once a proband variant is identified.

**Clinical/electrophysiological tests:**
- **EEG:** abnormal/epileptiform in ~87% of reported KCNC1-PME cases; generalized spike-and-polyspike-wave discharges; documented **photosensitivity** (photoparoxysmal response) in most cases; some individual case reports document a normal EEG despite a molecularly confirmed diagnosis, so a normal EEG does not exclude the disease.
- **Neurological examination:** mild cognitive decline, dysmetria, horizontal gaze-evoked nystagmus, truncal ataxia, bilateral upper-limb myoclonic jerks are typical exam findings.

**Neuroimaging:** Brain **MRI shows cerebellar atrophy in about a third of cases (32.6%, 15/46 in a pooled case series)** — a supportive but not obligatory finding; a normal MRI does not exclude EPM7.

**Differential diagnosis** (per GeneReviews, for the PME/MEAK presentation):
- Progressive myoclonic epilepsy type 1 (EPM1, Unverricht-Lundborg disease; *CSTB*)
- Lafora disease (EPM2A/EPM2B; *NHLRC1*)
- Neuronal ceroid lipofuscinoses (NCLs)
- MERRF (mitochondrial, m.8344A>G and related)
- *POLG*-related disorders
- Sialidosis
- Dentatorubral-pallidoluysian atrophy (DRPLA)
- *PRICKLE1*-related progressive myoclonic epilepsy
- *KCTD7*-related progressive myoclonic epilepsy (a molecularly and clinically distinct PME gene, per PME literature — not to be confused with KCNC1 despite superficial acronym similarity)
- For the DEE and milder ID/DD phenotypes, the differential is broad and nonspecific, requiring genomic-first diagnostic approaches (per the OMIM phenotypic-series framework for developmental encephalopathies).

**Omics-based diagnostics:** No routine transcriptomic/proteomic/metabolomic/epigenomic diagnostic assay is used clinically for KCNC1-related disorders; diagnosis is DNA-sequencing based.

**Screening:** No population or newborn screening program exists for this ultra-rare, typically de novo disorder; screening is not applicable outside of diagnostic testing in a symptomatic proband and subsequent targeted parental/reproductive counseling.

---

## 11. Outcome / Prognosis

**Survival/mortality:** GeneReviews states MEAK "does not appear to impact life span" — i.e., despite major morbidity, life expectancy in the classic MEAK phenotype is not reported to be shortened. This contrasts with the DEE phenotype, where severe infantile-onset drug-resistant epilepsy and profound developmental impairment carry greater overall morbidity, though specific mortality/life-expectancy statistics for the DEE subgroup were not identified in this search (the A421V transgenic mouse model does show premature lethality, but this has not been explicitly quantified in human DEE cohorts in the sources reviewed).

**Morbidity/function:** Major functional morbidity in MEAK arises from **progressive ataxia** (approximately half of patients require a walking aid or wheelchair by late adolescence/early adulthood) and from **disabling action myoclonus** that impairs voluntary movement, self-care, and mobility. No dementia has been reported, distinguishing the cognitive trajectory from many other PMEs (e.g., Lafora disease, which is far more rapidly and severely cognitively devastating).

**Disease course/complications:** Recurrent generalized tonic-clonic seizures (infrequent but present in ~97%) carry standard epilepsy-associated risks (injury, and — as with any epilepsy — a background SUDEP consideration, though this was not specifically quantified for KCNC1-PME in the sources reviewed). In DEE, feeding difficulties and failure to thrive are a recognized complication requiring supportive intervention (feeding therapy, gastrostomy).

**Recovery potential:** The disease is not self-limited; there is no spontaneous recovery. Targeted interventions (deep brain stimulation, investigational Kv3 modulator therapy — see Treatment) show partial symptomatic benefit in reported cases/trials but are not curative.

**Prognostic factors:** The single most important prognostic determinant identified in this literature is **genotype** — which specific *KCNC1* variant, and its precise functional mechanism (classic dominant-negative R320H → MEAK; more severe near-complete loss-of-function A421V → infantile DEE; haploinsufficiency nonsense variants → milder ID without seizures) — rather than any independently measured biomarker.

---

## 12. Treatment

**Pharmacotherapy (symptomatic anti-seizure/anti-myoclonic management):** There is **no *KCNC1*-specific approved anti-seizure medication**; management uses conventional PME-appropriate agents:
- **Valproic acid** and **clonazepam** are traditionally considered first-line for PME-associated myoclonus and seizures.
- **Levetiracetam, piracetam, and topiramate** are also reported as effective adjuncts for myoclonus in the broader PME literature and are used in KCNC1-related disorders.
- **Perampanel** has shown benefit for cortical myoclonus in progressive myoclonic epilepsies generally (including case series/systematic review data in PME broadly, e.g., PMID: 25667843 for Lafora disease and a broader PME case series/review, PMC8024635), though **psychiatric/behavioral side effects can limit its use**.
- **Primidone** is also listed among conventional ASMs considered for myoclonus in KCNC1-related disorders per GeneReviews.
- **Contraindicated/to-avoid agents:** consistent with general PME pharmacology, **sodium-channel blockers and GABAergic-potentiating drugs that can worsen myoclonus/PME phenotypes should be avoided** — phenytoin, carbamazepine, gabapentin, and vigabatrin are specifically flagged as agents to avoid in progressive myoclonic epilepsies.
- Suggested NCIT term: NCIT:C15986 (Pharmacotherapy), with `therapeutic_agent` bindable to CHEBI terms for valproic acid, clonazepam, levetiracetam, perampanel, topiramate (exact CHEBI IDs should be independently verified via OAK before KB entry, per dismech SOP).

**Genotype-informed / emerging pharmacotherapy:**
- **Fluoxetine** showed clinical benefit (improved seizures, balance, motor skills) in one reported DEE patient with a gain-of-function-adjacent *KCNC1* variant (c.1273G>A) — a preliminary, single-case observation rather than an established treatment.
- **AUT00201**, a novel **Kv3 modulator** developed by Autifony Therapeutics, directly targets the disease mechanism: preclinical data show it can **restore Kv3.1 channel function in cell lines expressing mutant channels, improve firing of neurons in mouse-model brains, and "completely reverse the seizure sensitivity and ataxia" of KCNC1 mouse models in vivo**. A US **Phase Ib randomized, double-blind, placebo-controlled crossover study** in adults (≥18 years) with genetically confirmed MEAK commenced in 2023 at the University of Pennsylvania (ClinicalTrials.gov NCT05873062), assessing both clinical endpoints (ataxia, myoclonus) and Kv3.1-dysfunction biomarkers; the study is reported complete with data analysis ongoing as of the sources reviewed. This represents the first disease-mechanism-targeted (rather than purely symptomatic) therapeutic approach in clinical development for EPM7.

**Neuromodulation/surgical:**
- **Deep brain stimulation (DBS)** of the subthalamic nucleus/substantia nigra (STN/SNr) has been reported in a genetically confirmed MEAK patient with pharmacoresistant myoclonus and drug-resistant epilepsy, with SNr/STN stimulation reported to reduce myoclonic seizures by 30–100% based on prior case-series data cited in that report (PMID/PMC: 10624572). This is an individualized, refractory-case intervention rather than standard of care.

**Supportive/rehabilitative care:**
- Physical and occupational therapy for progressive ataxia and motor dysfunction.
- Feeding therapy/gastrostomy for infants with DEE-associated feeding difficulties and failure to thrive.
- Standard epilepsy monitoring and safety counseling; educational and developmental support services, particularly for the DEE and ID phenotypes.
- Genetic counseling for families (NCIT:C15240, suggested).

**Experimental/clinical trials:** AUT00201 Phase Ib (NCT05873062) is the principal disease-specific interventional trial identified.

**Treatment strategy:** Progressive myoclonic epilepsies in general (including KCNC1-related PME) are "best treated by polytherapy" rather than monotherapy, combining conventional ASMs targeted at both the seizure and myoclonus components of the phenotype, with emerging genotype/mechanism-targeted approaches (Kv3 modulation, and case-specific SSRI or DBS trials) reserved for refractory cases.

---

## 13. Prevention

Because EPM7/KCNC1-related disorders arise almost exclusively from **de novo dominant mutation**, there is no primary population-level prevention strategy (no modifiable risk-factor reduction, immunization, or public-health intervention applies to a de novo monogenic channelopathy).

- **Secondary prevention / risk stratification:** the main actionable prevention lever is **genetic counseling informed by parental mosaicism testing**. Because low-level parental germline/somatic mosaicism has been documented to cause recurrence in siblings despite an apparently unaffected parent (PMID: 29428275), families should be counseled that recurrence risk is **not simply the general de novo background rate** once a variant is identified in a proband — targeted, sensitive mosaicism testing in parents (where technically available) refines recurrence-risk estimates for future pregnancies.
- **Prenatal/preimplantation genetic testing:** once a familial pathogenic variant is known (including in a mosaic parent), prenatal diagnosis or preimplantation genetic testing for monogenic disease (PGT-M) would be a standard reproductive option discussed in genetic counseling, though no disease-specific PGT program was identified in this search.
- **Tertiary prevention:** early diagnosis (via genomic-first testing given the nonspecific/overlapping PME phenotype) allows earlier initiation of appropriate anti-myoclonic/anti-seizure therapy and avoidance of contraindicated ASMs (phenytoin, carbamazepine, gabapentin, vigabatrin), which is the most concrete disease-specific "prevention of harm" measure identifiable in the current literature.
- No vaccine, prophylactic medication, or environmental-exposure-avoidance strategy applies, consistent with the absence of any identified environmental or infectious contributory factor.

---

## 14. Other Species / Natural Disease

No literature identified in this search describes a **naturally occurring** (spontaneous, non-engineered) KCNC1-associated disease in a non-human species (companion animal, livestock, or wildlife) analogous to OMIA-catalogued veterinary orthologs of human Mendelian disease. All non-human *Kcnc1* disease models identified are **laboratory-engineered** (see Model Organisms, below), not naturally occurring veterinary conditions. The gene is broadly conserved across mammals (mouse *Kcnc1* ortholog is the model used in essentially all functional/in vivo work reviewed here), consistent with deep evolutionary conservation of Kv3-family channel biology across vertebrates, but no comparative/zoonotic transmission relevance applies, since this is a non-communicable monogenic channelopathy.

- **Taxonomy:** Human, NCBITaxon:9606. Mouse ortholog *Kcnc1* used throughout functional/model studies (Mus musculus, NCBITaxon:10090).
- **Breed-specific veterinary disease:** none identified.
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious monogenic disease).

---

## 15. Model Organisms

**Genetic mouse models (the dominant model system for this disease):**

1. **Kcnc1-p.Arg320His/+ knock-in mouse (heterozygous)** — recapitulates the **core features of EPM7/MEAK**: progressive ataxia and increased seizure susceptibility. Electrophysiological studies in adult heterozygous mice demonstrate that loss of Kv3.1 function alters excitability and synaptic neurotransmission in **cerebral cortex PV+ interneurons and cerebellar granule cells**, mirroring the proposed human disease mechanism. This model was used to demonstrate that the investigational Kv3 modulator AUT00201 can "completely reverse the seizure sensitivity and ataxia" in vivo, supporting its translation to the human Phase Ib trial (NCT05873062).

2. **Kcnc1-p.Ala421Val transgenic mouse (global heterozygous expression)** — models the **DEE end of the spectrum**. Shows cognitive impairment, epilepsy, and **premature lethality**, with decreased PV-interneuron surface Kv3.1 expression, decreased voltage-gated K⁺ current density, and profound impairment of PV-interneuron intrinsic excitability — a more severe cellular/electrophysiological phenotype than the R320H model, consistent with A421V's more severe human clinical phenotype (earlier-onset, treatment-resistant epilepsy). Described in "Impaired excitability of fast-spiking neurons in a novel mouse model of *KCNC1* epileptic encephalopathy" (eLife, 2024/2025; PMC12916103, PMC11463657, and the bioRxiv preprint 10.1101/2024.09.27.615463).

3. **Kcnc1/Kcnc3 compound-null mice** (an earlier, mechanistically informative but not disease-variant-specific model): mice lacking *Kcnc1* alleles on a *Kcnc3*-null background show progressively worsening gait ataxia, spike broadening, and deceleration in deep cerebellar nuclei (DCN) neurons as *Kcnc1* alleles are lost; Purkinje-cell-targeted restoration of Kv3.3 (Kcnc3) does **not** rescue motor coordination in the absence of Kcnc1, underscoring the essential, non-redundant contribution of Kv3.1 to cerebellar output pathways governing motor coordination (Purkinje cell → deep cerebellar nuclei → downstream motor circuits) (Espinosa et al., *J Neurosci* 2009; PMID: [20016089](https://pubmed.ncbi.nlm.nih.gov/20016089/)). This model validates the general biological logic (loss of Kv3.1-dependent high-frequency firing in cerebellar circuits → ataxia) rather than directly modeling a specific human pathogenic allele.

**In vitro/cellular models:**
- **Primary mouse cortical interneuron culture** (postnatal day 0–1, C57BL/6J) with lentiviral/plasmid expression of mutant Kv3.1bR320H — used to establish the "developmental dendritopathy" mechanism (impaired neurite outgrowth, reduced high-frequency firing capacity, increased apoptosis) (Carpenter et al., *Epilepsia* 2021; PMID: 33735526).
- ***Xenopus laevis* oocyte heterologous expression system** — used across multiple studies (Muona 2015, Oliver 2017/Ann Neurol, Muona/Oliver 2019 series) for direct biophysical characterization of mutant Kv3.1 channel currents, dominant-negative behavior in co-expression with wild-type subunit, and comparison across the allelic series (R320H, A421V, C208Y, T399M, R339*, etc.).
- **Patient fibroblast qPCR** — used to demonstrate nonsense-mediated decay and haploinsufficiency for the p.Arg339* variant.

**Model characteristics/limitations:** The R320H knock-in mouse is considered a **high-fidelity model of MEAK**, recapitulating both the ataxia and seizure-susceptibility phenotypes and validated as a translational platform for the AUT00201 Kv3-modulator program. The A421V model appropriately captures the more severe DEE phenotype including premature lethality. No invertebrate (Drosophila, *C. elegans*) or zebrafish *kcnc1* disease models were identified in this search (zebrafish *kcna1a* models exist for a related but distinct potassium-channel epilepsy, episodic ataxia type 1, and should not be conflated with *KCNC1*/EPM7).

**Applications:** These models have been directly used for (a) confirming causal genotype-phenotype-mechanism relationships, (b) dissecting cell-type-specific (cortical PV-interneuron vs. cerebellar granule/Purkinje) contributions to the myoclonus-ataxia phenotype, and (c) preclinical validation and translational bridging for the Kv3-modulator (AUT00201) therapeutic program now in human Phase Ib testing.

---

## Summary Table: Key Ontology Term Suggestions for KB Curation

*(All IDs below are provided as starting-point suggestions from research-report synthesis and should be independently verified via OAK/authoritative ontology browsers before use in curation, per standard anti-hallucination practice — several, particularly the CL, GO, and HPO codes, are recalled with lower confidence than the disease/gene identifiers.)*

| Category | Suggested term | ID (verify before use) |
|---|---|---|
| Disease | Progressive myoclonic epilepsy type 7 | MONDO:0014521; OMIM:616187; ORPHA:435438 |
| Gene | KCNC1 | HGNC:6233; OMIM:176258 |
| Phenotype | Myoclonus | HP:0001336 |
| Phenotype | Ataxia | HP:0001251 |
| Phenotype | Gait ataxia | HP:0002066 |
| Phenotype | Bilateral tonic-clonic seizure | HP:0002069 |
| Phenotype | Cerebellar atrophy | HP:0001272 |
| Phenotype | Nystagmus | HP:0000639 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Intellectual disability, mild | HP:0001256 |
| Phenotype | Hypotonia | HP:0001252 |
| Phenotype | Failure to thrive | HP:0001508 |
| Anatomy | Cerebellum | UBERON:0002037 |
| Anatomy | Cerebral cortex | UBERON:0000956 |
| Treatment | Pharmacotherapy | NCIT:C15986 |

---

## Sources

- [Entry - #616187 - EPILEPSY, PROGRESSIVE MYOCLONIC 7; EPM7 - OMIM](https://www.omim.org/entry/616187)
- [Entry - *176258 - POTASSIUM CHANNEL, VOLTAGE-GATED, SHAW-RELATED SUBFAMILY, MEMBER 1; KCNC1 - OMIM](https://omim.org/entry/176258)
- [Orphanet: Progressive myoclonic epilepsy type 7](https://www.orpha.net/en/disease/detail/435438)
- [KCNC1-Related Disorders - GeneReviews® - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK619809/)
- [A recurrent de novo mutation in KCNC1 causes progressive myoclonus epilepsy - PubMed (Muona et al., Nat Genet 2015; PMID 25401298)](https://pubmed.ncbi.nlm.nih.gov/25401298/)
- [Familial cases of progressive myoclonic epilepsy caused by maternal somatic mosaicism of a recurrent KCNC1 p.Arg320His mutation - PubMed (PMID 29428275)](https://pubmed.ncbi.nlm.nih.gov/29428275/)
- [Progressive myoclonus epilepsy KCNC1 variant causes a developmental dendritopathy - PMC (Carpenter et al., Epilepsia 2021; PMID 33735526)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8436768/)
- [Loss of Function of KCNC1 is associated with intellectual disability without seizures - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5437909/)
- [KCNC1-related disorders: new de novo variants expand the phenotypic spectrum - PubMed (PMID 31353862)](https://pubmed.ncbi.nlm.nih.gov/31353862/)
- [Encephalopathies with KCNC1 variants: genotype-phenotype-functional correlations - PubMed (PMID 31353855)](https://pubmed.ncbi.nlm.nih.gov/31353855/)
- [Impaired excitability of fast-spiking neurons in a novel mouse model of KCNC1 epileptic encephalopathy - eLife/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916103/)
- [Targeted therapy improves cellular dysfunction, ataxia, and seizure susceptibility in a model of a progressive myoclonus epilepsy - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666379123006183)
- [Rescue of Motor Coordination by Purkinje Cell-Targeted Restoration of Kv3.3 Channels in Kcnc3-Null Mice Requires Kcnc1 - PubMed (PMID 20016089)](https://pubmed.ncbi.nlm.nih.gov/20016089/)
- [Autifony Therapeutics announces commencement of a US Phase Ib study of AUT00201, a novel Kv3 modulator, in Progressive Myoclonic Epilepsy-7 (EPM7)](https://autifony.com/autifony-therapeutics-announces-commencement-of-a-us-phase-ib-study-of-aut00201-a-novel-kv3-modulator-in-progressive-myoclonic-epilepsy-7-epm7/)
- [Safety, Blood Levels and Effects of AUT00201 in Patients With MEAK - ClinicalTrials.gov protocol (NCT05873062)](https://cdn.clinicaltrials.gov/large-docs/62/NCT05873062/Prot_000.pdf)
- [Deep brain stimulation in a patient with progressive myoclonic epilepsy and ataxia due to potassium channel mutation (MEAK). A case report and review of the literature - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624572/)
- [Myoclonus epilepsy and ataxia due to potassium channel mutation (MEAK) is caused by heterozygous KCNC1 mutations - Epileptic Disorders (Nascimento et al., 2016)](https://onlinelibrary.wiley.com/doi/10.1684/epd.2016.0859)
- [KCNC1 ‐Related Progressive Myoclonus Epilepsy: A Case Report - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12321598/)
- [Kv3 Channels: Enablers of Rapid Firing, Neurotransmitter Release, and Neuronal Endurance - Physiological Reviews](https://journals.physiology.org/doi/full/10.1152/physrev.00002.2017)
- [Perampanel Improves Cortical Myoclonus and Disability in Progressive Myoclonic Epilepsies: A Case Series and a Systematic Review of the Literature - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8024635/)
- [KCNC1 gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=KCNC1)