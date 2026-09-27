---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-25T04:34:34.707333'
end_time: '2026-08-25T04:38:44.256131'
duration_seconds: 249.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Subacute Delirium
  mondo_id: ''
  category: Neurologic
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 17
  total_cost_usd: 1.1450848000000002
  session_id: 21924873-a28a-5e64-81d5-a552bf3cfbda
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 55
reference_validation:
  total_references: 36
  verified: 35
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.028
  relevance_assessed: 35
  on_topic: 18
  unresolved_references:
  - DOI:10.1056/NEJMoa1808217)(landmark
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Subacute Delirium
- **MONDO ID:**  (if available)
- **Category:** Neurologic

## Research Objectives

Please provide a comprehensive research report on **Subacute Delirium** covering all of the
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

I'll research this topic now using web search across the key areas: definitions/nosology, etiology, phenotypes, mechanisms, and management.

# Subacute Delirium: Comprehensive Research Report

## Note on Nosology

"Subacute Delirium" is not an independently defined disease entity with its own genetic or pathophysiological literature — it is a **temporal-course descriptor** within the single clinical syndrome of delirium. ICD-10-CM code **F05** ("Delirium due to known physiological condition") is explicitly defined to include "acute **or subacute** confusional state," "acute or subacute brain syndrome," and "acute or subacute psycho-organic syndrome," with **F05.1** covering delirium superimposed on dementia [icd10data.com](https://www.icd10data.com/ICD10CM/Codes/F01-F99/F01-F09/F05-). MONDO (`MONDO:0004629`) and UMLS/MedGen (`C0154333`, SNOMED CT `191507002`) carry "Subacute Delirium" as a synonym set ("Delirium, Subacute"; "Subacute confusional state") mapped onto the same underlying concept as delirium generally [MedGen C0154333](https://www.ncbi.nlm.nih.gov/medgen/56340). Consequently, this report treats "subacute delirium" as **delirium with a subacute onset/course** (onset over days rather than hours, and/or a protracted duration of weeks rather than days) and draws on the delirium literature broadly, flagging the subset of studies that specifically address protracted/persistent/subacute courses (Sections 8 and 11 in particular).

---

## 1. Disease Information

**Overview.** Delirium is an acute neuropsychiatric syndrome of disturbed attention, awareness, and cognition that develops over a short period (hours to days — "acute") or, in the subacute variant, over a somewhat longer interval, and represents a direct physiological consequence of an underlying medical condition, substance intoxication/withdrawal, or medication effect, or multiple combined etiologies [MalaCards / MONDO:0004629 description via search]. Core features include a disturbance of attention and awareness, an additional cognitive disturbance (memory, disorientation, language, visuospatial ability, or perception), development over a short period with a tendency to fluctuate in severity during the day, and evidence that the disturbance is not better explained by a pre-existing/evolving dementia.

**Key identifiers:**
| Ontology | Identifier |
|---|---|
| MONDO | MONDO:0004629 ("subacute delirium") |
| UMLS/MedGen | C0154333 |
| SNOMED CT | 191507002 |
| ICD-10-CM | F05 (Delirium due to known physiological condition — "acute or subacute confusional state"); F05.1 (superimposed on dementia) |
| DSM-5 | Delirium, specified as acute (hours–days) or persistent (weeks–months) |

**Synonyms:** Subacute confusional state; acute confusional state; toxic-metabolic encephalopathy; organic brain syndrome (historical term); ICU psychosis (informal, ICU-specific); sundowning (informal, when evening-predominant) [MedGen C0154333](https://www.ncbi.nlm.nih.gov/medgen/56340).

**Data source note:** Most quantitative data below derive from aggregated, cohort-level clinical research (hospital registries, ICU cohorts, meta-analyses) rather than individual EHR mining per se, though several cited studies (e.g., UK Biobank-linked COVID-19 cohort, US World Delirium Awareness Day prevalence study) are EHR/registry-based.

---

## 2. Etiology

**Causal framework.** Delirium arises from an interaction between predisposing (vulnerability) factors and precipitating (insult) factors — a patient with high vulnerability (e.g., advanced age, dementia) can develop delirium from a minor insult, while a resilient patient requires a major insult (multiple simultaneous new medications, major surgery, severe critical illness).

**Direct causal factors:**
- Systemic infection/sepsis and acute critical illness
- Major surgery/anesthesia (postoperative delirium)
- Metabolic derangement (electrolyte disturbance, hypo-/hyperglycemia, hepatic/renal failure)
- Medication effects, polypharmacy, and substance intoxication/withdrawal (including alcohol and benzodiazepine withdrawal)
- Hypoxia/hypoperfusion
- Primary CNS insults (stroke, seizure, traumatic brain injury, CNS infection)

**Genetic risk factors.** The largest multi-ancestry GWAS of delirium to date analyzed **1,059,130 individuals (11,931 cases)** and identified **APOE** as a strong risk locus, with the effect persisting after adjustment for dementia/Alzheimer's disease and within dementia-free cohorts — indicating APOE independently confers delirium vulnerability rather than acting solely through dementia risk [PLOS Medicine GWAS](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1004963). A large UK cohort further found that **APOE ε4 genotypes increased risk of delirium during COVID-19-related hospitalizations** [PMC8344705](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8344705/). Additional postoperative-delirium-associated loci include **APOC1, TOMM40, and PVRL2**, genes previously linked to dementia, cognitive decline, and cerebral imaging phenotypes [Neuroscience News summary]. Notably, earlier candidate-gene associations between the muscarinic cholinergic receptor genes **CHRM2** and **CHRM4** and postoperative delirium were **not replicated** in more recent, better-powered analyses, with all three previously identified variants showing null effects [medRxiv / Nature Aging, Dissecting the genetic and proteomic risk factors for delirium](https://www.nature.com/articles/s43587-025-01018-6).

**Environmental/clinical risk factors** (odds ratios from recent meta-analyses of hospitalized older patients):
- Frailty: OR ≈ 2.05
- Physical restraints: OR ≈ 5.01
- Prior falls: OR ≈ 1.99
- Severe illness: OR ≈ 1.32
- Cognitive impairment/dementia: OR ≈ 2.61
[ScienceDirect, Global incidence and prevalence of delirium, 2024](https://www.sciencedirect.com/science/article/abs/pii/S0020748924002724); [PubMed 39602991](https://pubmed.ncbi.nlm.nih.gov/39602991/)

Other established risk factors include advanced age, polypharmacy (especially anticholinergics, benzodiazepines, opioids), sensory impairment (vision/hearing), immobility, dehydration, sleep deprivation, indwelling catheters/lines, and mechanical ventilation.

**Protective factors.** Multicomponent nonpharmacological prevention programs are the best-evidenced protective intervention (see Section 13); no robust genetic protective variant has been established, though the absence of the APOE ε4 allele is associated with lower risk by extension of the GWAS findings above.

**Gene-environment interaction.** The APOE-delirium association is modulated by acute physiological stressors (e.g., COVID-19 infection, surgery), consistent with a "two-hit" model in which genetic vulnerability (APOE-mediated neuronal/glial resilience) interacts with an environmental/physiological precipitant (infection, surgery, critical illness) to produce clinical delirium [PMC8344705](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8344705/).

---

## 3. Phenotypes

Delirium's phenotype spans cognitive, behavioral, and psychomotor domains, with laboratory/imaging correlates increasingly recognized as biomarker-level abnormalities.

| Phenotype | Suggested HP term | Notes |
|---|---|---|
| Inattention | HP:0032341 (Impaired social cognition) / general "attention deficit" — closest specific term is **HP:0007018** (Attention deficit) | Cardinal feature; assessed via digit span, months-backward |
| Disorientation | HP:0031466 (disorientation) if available, else HP:0000726 (Dementia) subset | Fluctuating; worse with evening ("sundowning") |
| Fluctuating consciousness/awareness | HP:0007360 (Aggressive behavior) not applicable; consider HP:0000726 or HP:0002360 (Sleep disturbance) for circadian component | Hallmark diagnostic feature (DSM-5 Criterion A/B) |
| Memory impairment | HP:0002354 (Memory impairment) | Both encoding and recall affected |
| Perceptual disturbances (hallucinations, illusions) | HP:0000738 (Hallucinations) | More common in hyperactive subtype |
| Psychomotor agitation | HP:0000723 (Restlessness) / HP:0100716 (Self-injurious behavior) in severe cases | Hyperactive subtype |
| Psychomotor retardation / lethargy | HP:0025336 (Psychomotor retardation) | Hypoactive subtype — most common but most underdiagnosed |
| Sleep-wake cycle disturbance | HP:0002360 (Sleep disturbance) | Circadian reversal common |
| Disorganized thinking/speech | HP:0031936 (Delusions) or HP:0000750 (Delayed speech and language development, N/A for adults) — best mapped as thought-disorder qualifier | |
| Emotional lability | HP:0000712 (Emotional lability) | |

**Motor subtypes and frequency.** A subacute-care cohort study of patients ≥65 admitted with delirium found: **hyperactive delirium 40.6%**, **mixed 31%**, **hypoactive 25.9%**, **nonmotor 2.6%** [PubMed search — persistent delirium subtype study]. Hypoactive delirium, though less prevalent in some settings, is disproportionately missed clinically because of its quiet presentation.

**Onset/severity/progression per DSM-5:** Delirium severity is formally specified as **acute** (a few hours to days) or **persistent** (weeks to months) — the "subacute" category sits at the acute-to-persistent transition, typically representing onset over roughly 1–2 weeks with a course of several weeks [DSM-5 criteria search summary].

**Frequency/persistence data:** Combined proportions of patients with *persistent delirium* were **44.7% at discharge, 32.8% at 1 month, 25.6% at 3 months, and 21% at 6 months** in an updated systematic review and meta-analysis [medRxiv persistent delirium meta-analysis](https://www.medrxiv.org/content/10.1101/2022.01.20.22269044.full.pdf); [Delirium Journal version](https://deliriumjournal.com/article/36822-persistent-delirium-in-older-hospital-patients-an-updated-systematic-review-and-meta-analysis). In patients with and without dementia, delirium symptoms persisted up to 12 months post-diagnosis, with **inattention, disorientation, and impaired memory** the most persistent individual symptoms in both groups.

**Quality of life impact:** Persistent/subacute delirium is associated with functional decline, increased nursing-home placement, and worse cognitive trajectory relative to patients whose delirium resolves acutely [PMC5506578, subsyndromal delirium meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5506578/).

---

## 4. Genetic/Molecular Information

Delirium is not a monogenic disorder; there is no single causal gene analogous to a Mendelian disease. Rather, common-variant susceptibility loci modulate risk in the context of an acute precipitant.

- **APOE** (chr19; HGNC:613) — strongest and most replicated genetic risk factor identified in the largest delirium GWAS to date (N=1,059,130, 11,931 cases), independent of dementia status [PLOS Medicine](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1004963).
- **APOC1, TOMM40, PVRL2 (NECTIN2)** — chromosome 19 loci in linkage disequilibrium with APOE, associated with postoperative delirium and broader neurocognitive phenotypes.
- **CHRM2, CHRM4** (muscarinic acetylcholine receptors) — earlier candidate-gene hits, **not replicated** in recent, adequately powered analyses (null effect in the 2024/2025 genetic-proteomic dissection study) [Nature Aging 2025](https://www.nature.com/articles/s43587-025-01018-6).

**Proteomic/functional correlates:** The same 2024–2025 genetic-and-proteomic dissection identified multiple **blood-based proteins predictive of delirium risk years in advance**, including markers of brain injury and inflammation not previously linked to delirium — supporting a model in which chronic subclinical neuronal vulnerability (proteomically detectable) interacts with an acute precipitant [Nature Aging](https://www.nature.com/articles/s43587-025-01018-6); [PMC12823428](https://pmc.ncbi.nlm.nih.gov/articles/PMC12823428/).

**Functional consequence framing:** These findings support a **susceptibility/modifier** model (GENO: `GENO:0000217` susceptibility) rather than a loss/gain-of-function causal mutation model — APOE ε4 carriage confers relative risk via impaired neuronal lipid transport, reduced synaptic resilience, and amplified neuroinflammatory response to systemic insults, rather than through a specific structural variant.

**Epigenetics/chromosomal abnormalities:** No delirium-specific epigenetic signature or chromosomal abnormality has been established in the literature surveyed; delirium is fundamentally a syndromic, precipitant-driven state superimposed on variable genetic vulnerability rather than a primary genetic or chromosomal disorder.

---

## 5. Environmental Information

**Environmental/iatrogenic factors:**
- Polypharmacy — anticholinergics, benzodiazepines, opioids, corticosteroids
- Physical restraints (independently associated risk, OR ≈ 5.01) [ScienceDirect 2024 meta-analysis]
- Indwelling catheters, intravenous lines, mechanical ventilation
- ICU environment: sleep deprivation, sensory overload/deprivation, lack of day-night cues
- Surgery/anesthesia exposure (postoperative delirium)

**Lifestyle/patient-level factors:** Pre-existing frailty, immobility, dehydration, malnutrition, sensory impairment (uncorrected vision/hearing loss), and sleep disruption are all established contributors, consolidated in the "predisposing × precipitating factor" model of delirium.

**Infectious triggers:** Systemic infection/sepsis is one of the most common precipitants; COVID-19 specifically has been shown to precipitate delirium at elevated rates in APOE ε4 carriers [PMC8344705](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8344705/). LPS (bacterial endotoxin)-driven systemic inflammation is the standard experimental proxy for infection-triggered delirium in animal models (see Section 15).

---

## 6. Mechanism / Pathophysiology

Delirium's mechanism is multifactorial and converges on **acute, reversible cortical-subcortical network dysfunction** driven by systemic and neuro-inflammation, neurotransmitter imbalance, and blood-brain barrier compromise.

**Causal chain (systemic trigger → clinical syndrome):**
1. **Systemic insult** (infection, surgery, metabolic derangement) → release of peripheral pro-inflammatory cytokines (IL-6, TNF-α, IL-1β) and cortisol.
2. **Blood-brain barrier (BBB) dysfunction** — increasingly recognized as a key permissive mechanism allowing peripheral inflammatory signals to reach the CNS [PMC11622424, Pathophysiology and Biomarkers of Delirium](https://pmc.ncbi.nlm.nih.gov/articles/PMC11622424/).
3. **Neuroinflammation** — microglial activation, NF-κB pathway activation, and local cytokine release (TNF-α, IL-1β, PGE2, nitric oxide) in the hippocampus and cortex, demonstrated mechanistically in LPS mouse models [Scientific Reports LPS study](https://www.nature.com/articles/s41598-019-42286-8).
4. **Neurotransmitter dysregulation** — dysregulated cholinergic (relative deficiency) and dopaminergic (relative excess) signaling is a long-standing mechanistic hypothesis, though the specific cholinergic receptor gene candidates have not held up genetically (see Section 4).
5. **Synaptic and network dysfunction** — disrupted thalamocortical and frontal-parietal connectivity.
6. **Clinical manifestation** — inattention, disorientation, and fluctuating consciousness.

**Molecular pathways:** NF-κB signaling (pro-inflammatory transcription); cortisol/HPA-axis signaling exacerbating neuroinflammation and impairing synaptic function [Frontiers postoperative delirium biomarkers review](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2025.1632947/full).

**Cellular processes:** Microglial activation and synaptic remodeling/pruning; astrocytic activation (reflected by S100B elevation); neuronal injury (reflected by NfL, tau, pTau elevation) [PMC11622424](https://pmc.ncbi.nlm.nih.gov/articles/PMC11622424/); [PMC10985356, Serum NFL and tau](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10985356/).

**Network/circuit-level findings (neuroimaging):**
- Reduced functional connectivity of the **intralaminar thalamic and caudate nuclei** with other subcortical regions during a delirium episode, which recovers after resolution [AJP, Neural Network Functional Connectivity During and After an Episode of Delirium](https://psychiatryonline.org/doi/10.1176/appi.ajp.2012.11060976).
- Disrupted reciprocal (inverse) coupling between the **dorsolateral prefrontal cortex** and **posterior cingulate cortex** — normally anti-correlated, these regions become abnormally positively correlated during delirium.
- EEG shows **increased delta/theta power, reduced alpha power, and reduced functional connectivity**, and loss of feedback cortical connectivity has been specifically implicated [Alzheimer's & Dementia 2024, Gjini et al.](https://alz-journals.onlinelibrary.wiley.com/doi/full/10.1002/alz.13471); [Frontiers EEG systematic review](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1274837/full).

**Biochemical/biomarker abnormalities:** Elevated **IL-6, CRP, TNF-α** (systemic inflammation, variable specificity); **S100B and NfL** show the most consistent CNS-injury-marker associations with delirium presence and severity, implicating astrocytic and axonal injury respectively [PMC12401822, Serum biomarkers of delirium in critical illness systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12401822/). A 2024/2025 CSF study found **CSF sIL-6R correlated with plasma IL-6/IL-8 and with blood-brain barrier permeability** (CSF:plasma albumin ratio, plasma S100B), directly linking peripheral inflammation to BBB compromise in postoperative delirium [BJA Open](https://www.bjaopen.org/article/S2772-6096(26)00020-1/fulltext).

**GO/CL/UBERON term suggestions:**
- GO:0034612 (response to tumor necrosis factor), GO:0032496 (response to lipopolysaccharide), GO:0007249 (I-kappaB kinase/NF-kappaB signaling), GO:0006954 (inflammatory response)
- CL:0000129 (microglial cell), CL:0000127 (astrocyte)
- UBERON:0001954 (Ammon's horn/hippocampus), UBERON:0002435 (striatum, incl. caudate), UBERON:0002444 (thalamus), UBERON:0009834 (dorsolateral prefrontal cortex)

---

## 7. Anatomical Structures Affected

**Organ level:** Primary organ affected is the **brain** (central nervous system); delirium is by definition a whole-brain functional (not typically focal-structural) disturbance, though it frequently co-occurs with the organ system driving the underlying precipitant (e.g., respiratory failure, sepsis-affected multiple organs, post-surgical state).

**Tissue/regional level:**
- **Thalamus** (intralaminar nuclei) — reduced functional connectivity during delirium
- **Basal ganglia / caudate nucleus** — reduced subcortical connectivity
- **Prefrontal cortex** (dorsolateral) — disrupted reciprocal connectivity with posterior cingulate
- **Posterior cingulate cortex** — abnormal positive coupling with DLPFC during delirium
- **Hippocampus** — site of microglial activation and neuronal injury in animal models (LPS)

**Subcellular level (GO Cellular Component):** Synapse (GO:0045202), microglial process, astrocytic end-foot at the blood-brain barrier (relevant to BBB dysfunction mechanism).

**Localization:** Diffuse/bilateral cortical-subcortical network disturbance rather than a single lateralized lesion; this distinguishes delirium from focal stroke-related confusional states.

---

## 8. Temporal Development

**Onset:**
- **Acute delirium**: onset over hours to a few days (DSM-5).
- **Subacute delirium**: onset over an intermediate timeframe, typically several days to roughly 1–2 weeks, representing an insidious rather than abrupt presentation — often seen with slowly evolving metabolic derangements, indolent infections, or medication accumulation effects, and clinically important because it is more easily mistaken for evolving dementia [MedGen C0154333 clinical research summary](https://www.ncbi.nlm.nih.gov/medgen/56340).
- Delirium can occur at any adult age but disproportionately affects older adults; onset in critical illness or postoperative settings is typically within the first several days of the inciting event.

**Progression / course pattern:**
- **Fluctuating course** is a defining diagnostic feature — symptom severity waxes and wanes over the course of a day, classically worsening in the evening ("sundowning").
- **DSM-5 persistence specifier**: acute (hours–days) vs. **persistent** (weeks–months) — subacute delirium occupies the transition zone and often evolves into persistent delirium if the underlying precipitant is not resolved.
- **Persistent delirium prevalence**: 44.7% at hospital discharge, declining to 32.8% (1 month), 25.6% (3 months), and 21% (6 months) in a pooled meta-analysis of older hospitalized patients [medRxiv](https://www.medrxiv.org/content/10.1101/2022.01.20.22269044.full.pdf).
- Symptoms can persist up to **12 months**, with inattention, disorientation, and memory impairment the most persistent individual features [search summary, persistent delirium 12-month follow-up].

**Remission patterns:** Delirium is classically defined as reversible with treatment of the underlying cause, though full cognitive recovery is not universal — a substantial minority never return to baseline cognition, particularly in patients with pre-existing cognitive impairment.

**Critical periods / intervention windows:** The subacute-to-persistent transition represents a key intervention window — early identification and treatment of the underlying precipitant during the subacute phase is associated with better functional and cognitive outcomes than intervention after the delirium becomes persistent [PMC12404460, Persistent inpatient delirium and increased LOS/mortality](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12404460/).

---

## 9. Inheritance and Population

**Epidemiology:**
- Pooled **prevalence 23.6%** and pooled **incidence 13.5%** among medically hospitalized older patients (recent systematic review/meta-analysis) [ScienceDirect 2024](https://www.sciencedirect.com/science/article/abs/pii/S0020748924002724); [PubMed 39602991](https://pubmed.ncbi.nlm.nih.gov/39602991/).
- US hospitalized-patient prevalence ranges **~16–18%**, rising to **~23.6%** in older adults specifically.
- 2023 US cross-sectional World Delirium Awareness Day study: clinically documented delirium prevalence **16.4% (morning)** and **17.9% (evening)** assessments [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2667296024000673).
- Prevalence reaches **up to 50%** in hospitalized elderly populations broadly, and **~32.5% incidence** among critically ill (ICU) patients, rising further with mechanical ventilation and organ dysfunction; **~47.7% prevalence** among post-surgical ICU patients [search summary].
- Community-dwelling older adults: systematic review of prevalence/incidence/risk factors in home settings (BJGP 2025) [BJGP.org](https://bjgp.org/content/75/760/e786).

**Inheritance pattern:** Not a Mendelian disorder — **complex/multifactorial**, with common-variant (APOE) susceptibility contributing modest, non-deterministic risk in the context of an acute precipitant. No formal penetrance, expressivity, anticipation, mosaicism, or founder-effect data are applicable in the Mendelian sense; APOE ε4 allele frequency itself varies by ancestry (well-characterized in gnomAD/population genetics resources independent of delirium).

**Population demographics:**
- **Age**: strongest independent risk factor — prevalence rises sharply with advancing age, particularly ≥65 years.
- **Sex**: no strong, consistent sex-ratio skew reported across the reviewed epidemiological studies; risk is driven primarily by frailty, comorbidity burden, and acute illness severity rather than sex per se.
- **Setting-specific demographics**: nephrology ward cohorts, pneumonia cohorts (5-decade prevalence/mortality meta-analysis), and emergency-department ambulance-arrival cohorts each show elevated delirium prevalence in older, frailer sub-populations [PMC12565244](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12565244/); [PMC12148281](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12148281/); [PMC11950662](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11950662/).

---

## 10. Diagnostics

**Clinical/bedside diagnostic tools:**
- **Confusion Assessment Method (CAM)** — the most widely used bedside screening/diagnostic algorithm, requiring acute onset/fluctuating course + inattention, plus either disorganized thinking or altered consciousness [search summary, DSM-5/CAM comparison].
- **CAM-ICU** — ICU-adapted version for non-verbal/ventilated patients.
- **DSM-5 criteria** — considered relatively more restrictive than DRS-R98 or CAM in head-to-head comparisons, identifying a somewhat different (often narrower) case set [PMC4207319, DSM-IV vs DSM-5 concordance](https://pmc.ncbi.nlm.nih.gov/articles/PMC4207319/); [PubMed 25601222](https://pubmed.ncbi.nlm.nih.gov/25601222/); [PubMed 28903799](https://pubmed.ncbi.nlm.nih.gov/28903799/).
- **DRS-R98 (Delirium Rating Scale-Revised-98)** — severity-graded instrument, used as a comparator/gold standard in validation studies.
- Level-of-arousal-inclusive DSM-5 interpretation is argued to be "safer" (more sensitive) for capturing genuine delirium cases [PMC4177077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4177077/).

**Laboratory tests:** No delirium-specific diagnostic lab test exists; work-up targets the underlying precipitant — CBC, metabolic panel, liver/renal function, TSH, blood/urine cultures, ammonia, toxicology screen as clinically indicated.

**Emerging biomarkers (research/investigational, not yet routine clinical diagnostics):**
- **S100B** and **neurofilament light chain (NfL)** — most consistent CNS-injury-marker associations with delirium presence/severity across a systematic review of serum biomarkers in critical illness [PMC12401822](https://pmc.ncbi.nlm.nih.gov/articles/PMC12401822/).
- **Serum tau and NfL** correlated with delirium in a 3-year retrospective analysis, while serum UCHL-1, GFAP, and CSF SNAP-25/NPTX2/sTREM2 did not [PMC10985356](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10985356/).
- **CSF IL-6, soluble IL-6 receptor, and IL-6 trans-signalling complex** associated with postoperative delirium in an observational cohort [BJA Open](https://www.bjaopen.org/article/S2772-6096(26)00020-1/fulltext).
- **EEG-based quantitative/functional-connectivity measures** — increased delta/theta power, reduced alpha power, reduced connectivity, and loss of feedback cortical connectivity are being explored as objective, non-invasive diagnostic adjuncts [Frontiers systematic review](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1274837/full); [Alzheimer's & Dementia 2024](https://alz-journals.onlinelibrary.wiley.com/doi/full/10.1002/alz.13471).
- Bispectral EEG has also been used as a discovery platform to identify novel protective agents for infection-related delirium in preclinical models [Translational Psychiatry 2024](https://www.nature.com/articles/s41398-024-03130-4).

**Genetic testing:** Not clinically indicated for delirium diagnosis (it is an acute syndromic diagnosis, not a genetic disease); APOE genotyping is a research risk-stratification tool, not a diagnostic test.

**Differential diagnosis:** Dementia (chronic, typically non-fluctuating, preserved consciousness), depression (particularly in hypoactive delirium), primary psychiatric psychosis, non-convulsive status epilepticus, stroke/focal neurological deficit, and delirium superimposed on dementia (ICD-10 F05.1) — which is common and requires careful distinction of an acute change from the patient's cognitive baseline.

**Screening:** No population-level genetic or newborn screening applies (delirium is an acquired, precipitant-driven acute-care condition); "screening" in practice means routine CAM/CAM-ICU or 4AT bedside screening of at-risk hospitalized patients (elderly, ICU, postoperative) rather than genetic carrier screening.

---

## 11. Outcome/Prognosis

**Mortality:**
- Persistent delirium is associated with **increased 30-day mortality** and **higher 60-, 90-, 180-, and 360-day mortality**, with an **incremental increase in mortality risk for each additional day of delirium** [search summary, persistent delirium outcomes meta-analysis]; [PMC12404460, increased LOS and mortality](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12404460/).
- Outcomes (mortality, nursing-home placement, function, cognition) for patients with **persistent delirium are consistently worse** than for patients who recover from delirium [PMC5506578](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5506578/); [PubMed 19017678, systematic review of frequency and prognosis](https://pubmed.ncbi.nlm.nih.gov/19017678/).

**Long-term cognitive outcomes / dementia risk:**
- A meta-analysis of **23 studies** found delirium significantly associated with long-term cognitive decline (Hedges g = **0.45**, 95% CI 0.34–0.57, P<.001) [JAMA Neurology meta-analysis](https://jamanetwork.com/journals/jamaneurology/fullarticle/2768000); [PubMed 32658246](https://pubmed.ncbi.nlm.nih.gov/32658246/).
- Patients experiencing in-hospital delirium showed markedly increased **dementia risk post-discharge (OR ≈ 5.37, P<.001)** compared with those without delirium [search summary].
- A separate estimation study modeled how many dementia cases might be prevented by preventing delirium, underscoring delirium as a modifiable dementia risk factor rather than a purely bystander phenomenon [PubMed 37031027](https://pubmed.ncbi.nlm.nih.gov/37031027/).
- A recent (2025) systematic review/meta-analysis of long-term clinical outcomes after hospital discharge for delirium further consolidates the adverse-outcome signal [Age and Ageing 2025](https://academic.oup.com/ageing/article/54/7/afaf188/8193852).

**Morbidity/function:** Increased length of stay, functional decline, and nursing-home placement are consistently reported; hyperactive, mixed, hypoactive, and nonmotor delirium subtypes differ in discharge destination and functional trajectory in subacute-care cohorts.

**Prognostic factors:** Duration of delirium (each additional day worsens mortality risk), pre-existing dementia, frailty, and severity of the underlying precipitating illness are the most consistently reported prognostic modifiers.

---

## 12. Treatment

**Pharmacotherapy:**
- **Antipsychotics (haloperidol, ziprasidone)**: The NEJM MIND-USA trial found **no significant difference** between haloperidol, ziprasidone, and placebo for delirium duration or severity in critically ill patients [NEJM 2018, Haloperidol and Ziprasidone for Treatment of Delirium in Critical Illness](https://www.nejm.org/doi/full/10.1056/NEJMoa1808217)(landmark trial; foundational to current guideline skepticism about routine antipsychotic use). A 2024 follow-up analysis of long-term outcomes similarly found **no difference in long-term quality of life** with haloperidol vs. placebo across the identified trials [ScienceDirect 2024, MIND-USA long-term outcomes](https://www.sciencedirect.com/science/article/abs/pii/S2213260024000778).
- **Dexmedetomidine (alpha-2 agonist)**: The **4D trial** (2024/2025) compared haloperidol-first-then-dexmedetomidine strategies for hyperactive delirium in non-intubated ICU patients, finding **improved agitation control, reduced need for additional medications, and reduced ICU length of stay/costs** with the dexmedetomidine-inclusive strategy [Intensive Care Medicine 2025](https://link.springer.com/article/10.1007/s00134-025-08135-1); [PMC12678554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12678554/).
- **Olanzapine vs. low-dose dexmedetomidine**: A 2024 randomized trial in critically ill patients directly compared these agents [AJRCCM 2024](https://academic.oup.com/ajrccm/article/212/8/1845/8676450).
- **Dexmedetomidine + melatonin** for post-CABG delirium: a 2023 RCT (n=80) found delirium occurrence **lower with combined dexmedetomidine+melatonin (15%) vs. dexmedetomidine alone (30%)** [PMC10664157](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10664157/).

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy) for the generic action, with `therapeutic_agent` bindings to CHEBI for haloperidol, ziprasidone, olanzapine, dexmedetomidine, and melatonin individually.

**Non-pharmacological / supportive care:** Reorientation, early mobilization, sleep-hygiene protocols, hearing/vision aid provision, hydration/nutrition support, and minimizing deliriogenic medications and physical restraints — the core components of the **Hospital Elder Life Program (HELP)** (see Section 13), applied both preventively and as first-line management of established delirium.

**Rehabilitation:** Physical and occupational therapy to address functional decline associated with persistent delirium; NCIT:C15302 (Physical Therapy).

**Experimental/investigational:** Bispectral-EEG-guided discovery platforms are being used to screen for novel protective agents against infection-related delirium in preclinical models [Translational Psychiatry 2024](https://www.nature.com/articles/s41398-024-03130-4).

**Treatment strategy summary:** Current evidence favors **treating the underlying precipitant first**, applying non-pharmacological multicomponent strategies as first line, and reserving antipsychotics/dexmedetomidine for severe agitation or patient/staff safety concerns rather than as disease-modifying therapy — reflecting the accumulated null results for antipsychotics on delirium duration/long-term outcomes.

---

## 13. Prevention

**Primary prevention — multicomponent nonpharmacological interventions:**
- The **Hospital Elder Life Program (HELP)**, developed by Sharon K. Inouye's group at Yale (1999), bundles reorientation, early mobilization, therapeutic activities, hydration/nutrition support, sleep-protocol strategies, and hearing/vision adaptation [PMC3724594](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3724594/).
- The original NEJM 1999 trial established multicomponent targeted intervention efficacy for preventing delirium onset and reducing total delirium-days in hospitalized older medical patients [NEJM 1999](https://www.nejm.org/doi/full/10.1056/NEJM199903043400901).
- A 2024 systematic review/meta-analysis of HELP found subgroup effect estimates of **RR ≈ 0.65 (HELP programs)** and **RR ≈ 0.70 (non-HELP multicomponent programs)** for delirium incidence reduction [ScienceDirect 2024](https://www.sciencedirect.com/science/article/abs/pii/S0197457224000314).
- A 2024/2025 umbrella review of RCTs for delirium prevention/treatment interventions further consolidates this evidence base [ScienceDirect umbrella review](https://www.sciencedirect.com/science/article/pii/S1568163724001314).
- Nurse-led multicomponent interventions have separately been shown effective in a 2025 systematic review/meta-analysis [Journal of Advanced Nursing 2025](https://onlinelibrary.wiley.com/doi/abs/10.1111/jan.70706).

**Secondary prevention:** Routine bedside screening (CAM/CAM-ICU/4AT) of at-risk hospitalized, postoperative, and ICU patients for early detection, permitting prompt treatment of an emerging precipitant before delirium becomes persistent/subacute-to-chronic.

**Tertiary prevention:** Once delirium is established, minimizing deliriogenic medications, restraints, and immobility, and aggressively treating the underlying condition, reduces progression to persistent delirium and its associated mortality/cognitive-decline risk.

**Pharmacological prophylaxis:** Evidence for pharmacological delirium prophylaxis (e.g., prophylactic antipsychotics or dexmedetomidine) remains mixed and is not a first-line recommendation given the null long-term outcome data for antipsychotics; nonpharmacological multicomponent prevention remains the standard of care.

**Counseling:** Not applicable in the genetic-counseling sense (delirium is not a heritable single-gene disorder); patient/family education regarding delirium risk, expected fluctuating course, and reorientation strategies is a core component of both prevention and management.

---

## 14. Other Species / Natural Disease

Delirium as classically defined is a human clinical/DSM construct; there is no widely characterized spontaneous veterinary "delirium" literature comparable to human clinical case series. However:
- Veterinary anesthesia/critical-care literature describes **post-anesthetic emergence delirium/dysphoria** and **ICU-associated confusional states** in companion animals (dogs, cats) that are mechanistically analogous (systemic inflammation, anesthesia, critical illness precipitating acute confusional states), though this is not formally captured in OMIA as a discrete inherited disease.
- The **orthologous APOE gene** is broadly conserved across mammals (NCBI Gene), consistent with cross-species use of Apoe-knockout or humanized-APOE mouse lines in delirium-adjacent neuroinflammation research (see below).

---

## 15. Model Organisms

**Primary model: LPS (lipopolysaccharide)-induced systemic inflammation in mice.** This is the dominant experimental proxy for infection-triggered delirium:
- LPS administration produces **acute-onset, fluctuating cognitive impairment** meeting DSM-IV-analogous criteria in mice, with microglial activation and neuronal cell loss in the hippocampus, assessed via Morris water maze and passive avoidance tests [Scientific Reports 2019](https://www.nature.com/articles/s41598-019-42286-8); [PMC6453933](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6453933/).
- LPS increases **TNF-α, IL-1β, PGE2, and nitric oxide**, with **NF-κB pathway activation**, directly modeling the neuroinflammatory mechanism described in Section 6.
- Interventional studies in this model include deferoxamine (iron chelation) attenuating LPS-induced neuroinflammation/memory impairment [PMC4323121](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4323121/), a Banhasasim-Tang (traditional herbal formulation) attenuation study [PMC7400939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7400939/), and hippocampal GPR17 knockdown/inhibition attenuating LPS-induced cognitive impairment [PMC10662506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10662506/).

**Perioperative/subclinical infection combination model:** A novel adult mouse model combining **subclinical infection with surgery** to induce cognitive dysfunction has been developed specifically as a model for perioperative neurocognitive disorder, closer to the clinical postoperative-delirium scenario than LPS alone [PMC12832885](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12832885/).

**Baseline vulnerability models:** Mouse models with pre-existing cognitive impairment/neurodegenerative pathology (e.g., amyloid-pathology models) show **progressively increased "delirium-like" susceptibility** to a superimposed acute inflammatory insult, mechanistically supporting the predisposing-factor × precipitating-factor clinical model [PMC4278840, Worsening Cognitive Impairment and Neurodegenerative Pathology Progressively Increase Risk for Delirium](https://pmc.ncbi.nlm.nih.gov/articles/PMC4278840/).

**Model limitations:** Mouse "sickness behavior" (reduced activity, reduced food intake) following LPS overlaps with but is not identical to human delirium's core attention/awareness disturbance, which is difficult to operationalize behaviorally in rodents; most LPS studies rely on validated cognitive-impairment proxies (water maze, passive avoidance) rather than a direct delirium-equivalent readout, so translational fidelity for the *attentional* component of delirium specifically remains an open limitation.

**Applications:** These models are used to dissect the neuroinflammation → BBB dysfunction → microglial activation → cognitive impairment causal chain, to screen candidate protective/therapeutic agents (e.g., the bispectral-EEG-guided discovery platform noted in Section 12) [Translational Psychiatry 2024](https://www.nature.com/articles/s41398-024-03130-4), and to test genetic-risk-modifying manipulations (e.g., Apoe-genotype mouse lines, though a delirium-specific Apoe-mouse study was not identified in this search and would be a natural translational follow-on to the human GWAS findings in Section 4).

---

## Summary for Knowledge-Base Curation

"Subacute Delirium" should be curated as a **temporal/course variant within the single delirium pathophysiology module** rather than as a structurally distinct disease mechanism — the causal chain (systemic insult → BBB dysfunction → neuroinflammation → thalamocortical/frontal network dysfunction → clinical syndrome) is shared across acute, subacute, and persistent presentations, with course duration and reversibility as the key differentiating `Descriptor` (`temporality: SUBACUTE` / `CHRONIC`, `clinical_course: PROGRESSIVE` for cases evolving toward persistent delirium or dementia). APOE (`hgnc:613`) is the best-supported genetic modifier and should be entered as a `SUSCEPTIBILITY` relationship type rather than a causal gene. S100B and NfL are the most defensible biomarker phenotypes for a `Biochemical`/laboratory-abnormality entry given consistency across recent systematic reviews.

---

### Sources
- [Subacute delirium (MedGen C0154333) — NCBI](https://www.ncbi.nlm.nih.gov/medgen/56340)
- [subacute delirium — Monarch Initiative MONDO:0004629](https://monarchinitiative.org/MONDO:0004629)
- [The Pathophysiology and Biomarkers of Delirium — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11622424/)
- [Serum biomarkers of delirium in critical illness: systematic review — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12401822/)
- [Emerging biomarkers of postoperative delirium — Frontiers](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2025.1632947/full)
- [Serum NFL and tau correlate with delirium — PMC10985356](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10985356/)
- [CSF IL-6/sIL-6R and postoperative delirium — BJA Open](https://www.bjaopen.org/article/S2772-6096(26)00020-1/fulltext)
- [Persistent delirium in older hospital patients: updated systematic review — medRxiv](https://www.medrxiv.org/content/10.1101/2022.01.20.22269044.full.pdf)
- [Persistent delirium in older hospital patients — Delirium Journal](https://deliriumjournal.com/article/36822-persistent-delirium-in-older-hospital-patients-an-updated-systematic-review-and-meta-analysis)
- [Persistent delirium: frequency and prognosis — PubMed 19017678](https://pubmed.ncbi.nlm.nih.gov/19017678/)
- [Persistent inpatient delirium, length of stay, mortality — PMC12404460](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12404460/)
- [Outcomes of subsyndromal delirium in ICU — PMC5506578](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5506578/)
- [Global incidence and prevalence of delirium — ScienceDirect 2024](https://www.sciencedirect.com/science/article/abs/pii/S0020748924002724)
- [Global incidence/prevalence of delirium — PubMed 39602991](https://pubmed.ncbi.nlm.nih.gov/39602991/)
- [Delirium among older adults living at home — BJGP 2025](https://bjgp.org/content/75/760/e786)
- [Delirium in the US: 2023 World Delirium Awareness Day study — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2667296024000673)
- [Prevalence/risk factors of delirium in nephrology ward — PMC12565244](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12565244/)
- [Five-decade prevalence of delirium in pneumonia — PMC12148281](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12148281/)
- [Delirium at ED arrival by ambulance — PMC11950662](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11950662/)
- [DSM-IV vs DSM-5 delirium concordance — PMC4207319](https://pmc.ncbi.nlm.nih.gov/articles/PMC4207319/)
- [Comparison of delirium diagnosis: CAM, DRS-R98, DSM-IV, DSM-5 — PubMed 25601222](https://pubmed.ncbi.nlm.nih.gov/25601222/)
- [Outcomes by diagnostic system for delirium — PubMed 28903799](https://pubmed.ncbi.nlm.nih.gov/28903799/)
- [DSM-5 criteria, arousal, and delirium diagnosis — PMC4177077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4177077/)
- [Genetic architecture of postoperative delirium — PLOS Medicine](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1004963)
- [Dissecting the genetic and proteomic risk factors for delirium — Nature Aging](https://www.nature.com/articles/s43587-025-01018-6)
- [Dissecting the genetic and proteomic risk factors for delirium — PMC12823428](https://pmc.ncbi.nlm.nih.gov/articles/PMC12823428/)
- [Gene Discovery Reveals Hidden Risk Pathway for Delirium — Neuroscience News](https://neurosciencenews.com/genetics-delerium-29975/)
- [APOE ε4 genotypes and delirium risk during COVID-19 — PMC8344705](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8344705/)
- [Association of Delirium With Long-term Cognitive Decline: Meta-analysis — JAMA Neurology](https://jamanetwork.com/journals/jamaneurology/fullarticle/2768000)
- [Association of Delirium With Long-term Cognitive Decline — PubMed 32658246](https://pubmed.ncbi.nlm.nih.gov/32658246/)
- [Preventing dementia by preventing delirium — PubMed 37031027](https://pubmed.ncbi.nlm.nih.gov/37031027/)
- [Long-term clinical outcomes of delirium after discharge — Age and Ageing 2025](https://academic.oup.com/ageing/article/54/7/afaf188/8193852)
- [Neural network functional connectivity during/after delirium — AJP](https://psychiatryonline.org/doi/10.1176/appi.ajp.2012.11060976)
- [EEG functional connectivity for delirium detection — Frontiers 2023](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1274837/full)
- [Delirium and loss of feedback cortical connectivity — Alzheimer's & Dementia 2024](https://alz-journals.onlinelibrary.wiley.com/doi/full/10.1002/alz.13471)
- [ICD-10-CM F05 codes — icd10data.com](https://www.icd10data.com/ICD10CM/Codes/F01-F99/F01-F09/F05-)
- [Haloperidol and Ziprasidone for Delirium in Critical Illness — NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1808217)
- [Long-term outcomes after antipsychotic treatment of delirium (MIND-USA) — ScienceDirect 2024](https://www.sciencedirect.com/science/article/abs/pii/S2213260024000778)
- [4D Trial: Dexmedetomidine for hyperactive delirium — Intensive Care Medicine 2025](https://link.springer.com/article/10.1007/s00134-025-08135-1)
- [4D Trial — PMC12678554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12678554/)
- [Olanzapine vs low-dose dexmedetomidine — AJRCCM 2024](https://academic.oup.com/ajrccm/article/212/8/1845/8676450)
- [Dexmedetomidine + melatonin for post-CABG delirium — PMC10664157](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10664157/)
- [Hospital Elder Life Program design/methods — PMC3724594](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3724594/)
- [Original HELP trial — NEJM 1999](https://www.nejm.org/doi/full/10.1056/NEJM199903043400901)
- [HELP systematic review/meta-analysis — ScienceDirect 2024](https://www.sciencedirect.com/science/article/abs/pii/S0197457224000314)
- [Umbrella review of delirium prevention/treatment RCTs — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1568163724001314)
- [Nurse-led multicomponent interventions — Journal of Advanced Nursing 2025](https://onlinelibrary.wiley.com/doi/abs/10.1111/jan.70706)
- [Neuroinflammation induced by LPS causes cognitive impairment in mice — Scientific Reports](https://www.nature.com/articles/s41598-019-42286-8)
- [LPS-induced cognitive impairment — PMC6453933](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6453933/)
- [Deferoxamine attenuates LPS-induced neuroinflammation — PMC4323121](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4323121/)
- [Banhasasim-Tang attenuates LPS-induced cognitive impairment — PMC7400939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7400939/)
- [Hippocampal GPR17 knockdown attenuates LPS-induced cognitive impairment — PMC10662506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10662506/)
- [Subclinical infection + surgery mouse model — PMC12832885](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12832885/)
- [Cognitive impairment/neurodegeneration and delirium risk — PMC4278840](https://pmc.ncbi.nlm.nih.gov/articles/PMC4278840/)
- [Bispectral EEG discovery of protective agents for infection-related delirium — Translational Psychiatry 2024](https://www.nature.com/articles/s41398-024-03130-4)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 18 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1056/NEJMoa1808217)(landmark` (1 mention) - Identifier did not resolve to a record