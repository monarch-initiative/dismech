---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-13T21:23:40.788389'
end_time: '2026-08-13T21:43:09.533274'
duration_seconds: 1168.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CHILD Syndrome
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 6
  num_turns: 59
  total_cost_usd: 7.603193000000002
  session_id: d51727a0-7c52-4bd3-ac43-e9a14ceb4803
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 2
citation_count: 38
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 33
  quotes_valid: 27
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CHILD Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CHILD Syndrome** covering all of the
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

I'll research this now.

# CHILD Syndrome — Comprehensive Research Report

**Congenital Hemidysplasia with Ichthyosiform erythroderma/nevus and Limb Defects**

*Prepared 13 August 2026. Evidence sources labeled as HUMAN_CLINICAL / MODEL_ORGANISM / IN_VITRO / COMPUTATIONAL throughout. Quoted text marked with quotation marks is verbatim from the cited abstract or resource; unquoted text is synthesis.*

---

## 1. Disease Information

### Overview

CHILD syndrome is a rare X-linked dominant, male-lethal inborn error of the **distal (post-squalene) cholesterol biosynthesis pathway**, caused by loss-of-function variants in *NSDHL* at Xq28. Its defining feature is not simply a skin disease but a **strikingly lateralized developmental field defect**: an inflammatory ichthyosiform nevus with sharp midline demarcation on one side of the body, accompanied by ipsilateral hypoplasia of limbs, skeleton, and viscera. The lateralization is a direct visible readout of **random X-chromosome inactivation** combined with **negative selection against mutant-expressing cells** — a rare instance where a mosaic pattern is essentially the disease definition.

The original clinical delineation (HUMAN_CLINICAL):

> "The term CHILD syndrome is proposed as an acronym for congenital hemidysplasia with ichthyosiform erythroderma and limb defects. The syndrome is characterized by unilateral erythema and scaling, with a distinct demarcation in the middle of the trunk. The dermatosis is either present at birth or develops during the first weeks of life. Ipsilateral limb defects may vary from hypoplasia of some fingers to complete absence of an extremity."
> — Happle R, Koch H, Lenz W. *Eur J Pediatr.* 1980;134(1):27-33. **PMID:7408908**

Orphanet's definition (aggregated disease-level resource):

> "A rare developmental defect during embryogenesis characterized by unilateral inflammatory and scaling skin lesions with ipsilateral visceral and limb anomalies."
> — Orphanet ORPHA:139, definition retrieved 2026-07-02 via the Orphanet API (https://api.orphacode.org)

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | **MONDO:0010621** | label "CHILD syndrome"; verified via EBI OLS4 |
| **OMIM** | **308050** | CONGENITAL HEMIDYSPLASIA WITH ICHTHYOSIFORM ERYTHRODERMA AND LIMB DEFECTS |
| **Orphanet** | **ORPHA:139** | |
| **MeSH** | **C562515** | supplementary concept record |
| **UMLS** | C0265267 | |
| **MedGen** | 82697 | |
| **SNOMED CT** | 17608003 | |
| **DOID** | DOID:0111822 | |
| **GARD** | 0006039 | |
| **NORD** | 1284 | |
| **ICD-9-CM** | 759.89 | MONDO `relatedTo` mapping |
| **ICD-10** | Commonly coded **Q82.8** ("other specified congenital malformations of skin") | ⚠️ Not verifiable from an authoritative API in this session — **verify before curation** |
| **ICD-11** | Not confirmed | ⚠️ **No authoritative mapping retrieved** — do not curate an ICD-11 code without checking the WHO browser |
| **Gene: HGNC** | **HGNC:13398** (`hgnc:13398` in dismech lowercase convention) | Symbol NSDHL; "NAD(P) dependent 3-beta-hydroxysteroid dehydrogenase NSDHL" |
| **Gene: OMIM** | **300275** | *NSDHL* |
| **Gene: NCBI Gene** | 50814 | |
| **Gene: Ensembl** | ENSG00000147383 | |
| **Protein: UniProt** | **Q15738** | "Sterol-4-alpha-carboxylate 3-dehydrogenase, decarboxylating"; EC **1.1.1.170** |
| **RefSeq transcript** | NM_015922 | |

*Source for MONDO xrefs, HGNC record, and UniProt fields: EBI OLS4 API, genenames.org REST API, UniProt REST API (all queried 2026-08-13).*

### Synonyms and alternative names

- CHILD syndrome (the standard clinical name)
- Congenital hemidysplasia with **ichthyosiform nevus** and limb defects — this is the **preferred modern expansion**; GeneReviews and much of the recent literature has moved away from "erythroderma," since the lesion is a nevus rather than a true erythroderma
- Congenital hemidysplasia with ichthyosiform erythroderma and limb defects (the original 1980 expansion, retained by OMIM)
- CHILD syndrome, X-linked dominant
- CHILD nevus (referring to the cutaneous lesion specifically)
- Ichthyosis, CHILD syndrome
- Unilateral ichthyosiform erythroderma with ipsilateral malformations (historical descriptive term)

*Synonym list from MONDO:0010621 (OLS4).*

**Nomenclature caveat worth curating:** a 2026 report explicitly argues the name is misleading, describing "CHILD Syndrome without Limb Defects in a 1-year-old: revised nomenclature and successful treatment with Topical 2% Simvastatin/2% Cholesterol" (Wyer J, Moss C, Poudel P, Ibbs S. *Clin Exp Dermatol.* 2026 May 4:llag193. **PMID:42082353**). Limb defects are common but not obligate.

### Data provenance

Essentially **all** knowledge of CHILD syndrome derives from **aggregated case reports and small case series**, not from EHR cohorts or registries. GeneReviews states plainly: **"More than 60 individuals have been reported to date."** (Kurban M, El Feghaly J, Hamie L. *NSDHL-Related Disorders.* GeneReviews®, initially published 1 Feb 2011, last update 5 Sep 2024, Bookshelf NBK51754, **PMID:21290788**). There is no natural-history study, no patient registry with published outcomes, and no population-based prevalence estimate that I could verify. Every frequency figure below should be treated as **case-report-derived and subject to ascertainment bias** — the severe end of the spectrum is over-represented, and the recent discovery of mild adult phenotypes presenting only as gastrointestinal xanthomas (**PMID:39466221**, **PMID:40517742**) suggests substantial under-ascertainment of mild disease.

---

## 2. Etiology

### Primary causal factor

**Germline (or, rarely, post-zygotic somatic) loss-of-function variants in *NSDHL*** (Xq28), encoding decarboxylating sterol-4-alpha-carboxylate 3-dehydrogenase, an enzyme of the C4-demethylation complex in post-squalene cholesterol biosynthesis.

The landmark gene-identification study (HUMAN_CLINICAL):

> "We report for the first time that CHILD syndrome (MIM 308050), an X-linked dominant, male-lethal trait characterized by an inflammatory nevus with striking lateralization and strict midline demarcation, as well as ipsilateral hypoplasia of the body is caused by mutations in the gene NSDHL located at Xq28 (NAD(P)H steroid dehydrogenase-like protein) encoding a 3beta-hydroxysteroid dehydrogenase functioning in the cholesterol biosynthetic pathway."
> — König A, Happle R, Bornholdt D, Engel H, Grzeschik KH. *Am J Med Genet.* 2000;90(4):339-46. **PMID:10710235**

GeneReviews specifies the mechanism as **loss of enzyme function**: the diagnosis rests on "a heterozygous *NSDHL* pathogenic variant identified by molecular genetic testing that results in loss of functional decarboxylating sterol-4-alpha-carboxylate 3-dehydrogenase" (**PMID:21290788**).

### A genetically distinct minority: *EBP*-related CHILD-like phenotype

A small subset of clinically diagnosed CHILD syndrome is **not** *NSDHL*-related but caused by deficiency of the downstream enzyme 3β-hydroxysteroid-Δ8,Δ7-isomerase (EBP, the CDPX2 gene) (HUMAN_CLINICAL):

> "Because CDPX2 patients have abnormal 8-dehydrosterol metabolism caused by mutations in 3beta-hydroxysteroid-delta8,delta7-isomerase, we measured plasma sterols in a patient with CHILD syndrome and found levels of 8-dehydrocholesterol and 8(9)-cholestenol increased to the same degree as in CDPX2 patients. Subsequently, we identified a nonsense mutation in exon 3 of the patient's 3beta-hydroxysteroid-delta8,delta7-isomerase gene. We speculate that at least some cases of CHILD syndrome are allelic with CDPX2 caused by 3beta-hydroxysteroid-delta8,delta7-isomerase deficiency."
> — Grange DK, Kratz LE, Braverman NE, Kelley RI. *Am J Med Genet.* 2000;90(4):328-35. **PMID:10710233**

This is a genuine **locus heterogeneity** finding and should be curated as such (the HPO annotation set for OMIM:308050 includes `HP:0003462` Elevated 8-dehydrocholesterol and `HP:0003465` Elevated 8(9)-cholestenol, which are the *EBP* biochemical signature rather than the *NSDHL* one — a subtlety worth noting when curating biomarker blocks).

### Risk factors

**Genetic risk factors**
- The causal *NSDHL* variant is essentially the whole risk story. There are **no reported susceptibility loci, modifier genes, or polygenic contributions** to CHILD syndrome. This is a fully penetrant Mendelian disorder in heterozygous females (see §9).
- **De novo occurrence is the norm.** Most cases are sporadic; GeneReviews notes familial transmission is documented (König 2000 reported a mother–daughter pair, **PMID:10710235**) but is uncommon.
- **Maternal carriage** is the one true "family-history" risk factor: a heterozygous mother has a 50% transmission risk per pregnancy, with recurrent male miscarriage as a family-history clue (see §9 and **PMID:36504312**).
- **The degree/pattern of X-inactivation** is the closest thing to a modifier — it determines laterality, extent, and (in the exceptional bilateral cases) symmetry. König et al. 2002 concluded: "Apparently, the effect of random X-inactivation is responsible for different patterns of cutaneous involvement in female carriers of NSDHL mutations." (**PMID:11907515**)

**Environmental risk factors**
- **None identified.** No toxin, drug, infection, maternal exposure, occupational hazard, or lifestyle factor has been reported as contributing to CHILD syndrome onset. Age, sex (see §9 — sex is a determinant of *viability*, not of risk), and family history are the only relevant demographic variables.
- ⚠️ Do not curate any environmental factor for disease *causation*. There is, however, an interesting **temperature** angle under gene–environment interaction, below.

### Protective factors

- **No protective variants or alleles have been reported.**
- The one biologically meaningful "protective" phenomenon is **cell-intrinsic selection**: in the mosaic heterozygote, wild-type-expressing cells progressively outcompete and replace mutant-expressing cells in many tissues, effectively protecting the contralateral side and improving the skin over time (see §6 and **PMID:19631568**, **PMID:21753784**).
- No dietary, nutritional, or lifestyle protective factor has been demonstrated. Notably, **dietary cholesterol supplementation is not effective for the skin** — the defect is in *local* cutaneous synthesis behind the epidermal permeability barrier, and serum cholesterol is typically normal.

### Gene–environment interactions

Two are worth curating, both from the mechanistic literature rather than epidemiology:

1. **Temperature sensitivity of mutant NSDHL protein (IN_VITRO).** Several disease-causing missense variants are conformationally unstable and their expression is temperature-dependent:
   > "Here we show that protein expression levels were low for all mutants, but some could be rescued by a lower temperature (30°C vs. 37°C) and/or the chemical chaperone glycerol. Additionally, heat shock proteins 70 and 90 are needed for optimal NSDHL protein expression suggesting that disease mutations in NSDHL may interfere with this interaction, perhaps during translation resulting in lower protein synthesis."
   > — Fenton NM, Sharpe LJ, Fitzsimmons DM, Capell-Hattam IM, Brown AJ. *J Steroid Biochem Mol Biol.* 2025;251:106758. **PMID:40222685**

   The allelic CK syndrome variants were likewise shown to "alter protein folding, show temperature-sensitive protein stability" (**PMID:21129721**). This creates a genuine, if speculative, gene–environment axis (febrile illness, skin surface temperature) and — more importantly — a **pharmacological chaperone therapeutic hypothesis**.

2. **Drug–pathway interaction as therapy.** Topical HMG-CoA reductase inhibitors (statins) and topical ketoconazole (a CYP51A1/lanosterol 14α-demethylase inhibitor) deliberately manipulate the pathway upstream of the block — a *therapeutic* gene–environment interaction (see §12).

---

## 3. Phenotypes

**Frequency caveat (important for KB curation):** CHILD syndrome has **no published cohort with denominators**. Frequency estimates below come from StatPearls' synthesis of the case literature, HPO's curated annotation set for OMIM:308050 (which carries **no frequency modifiers**), and GeneReviews' qualitative language ("common," "usually," "can occur"). Per the dismech frequency-evidence SOP, **most of these should be curated without a `frequency:` value**, or with only the coarse qualitative bands the source actually supports.

### 3.1 Cutaneous phenotypes (the defining domain)

| Feature | HPO suggestion | Onset | Course | Frequency evidence |
|---|---|---|---|---|
| Congenital ichthyosiform erythroderma (the CHILD nevus) | **HP:0007431** Congenital ichthyosiform erythroderma | Birth to first weeks–months of life | Erythema decreases and hyperkeratosis increases through infancy; often improves with age; **new lesions can arise in puberty/adulthood** | Essentially obligate (definitional) |
| Epidermal nevus / nevus | **HP:0010816** Epidermal nevus; **HP:0003764** Nevus | Congenital | Persistent | Definitional |
| Hyperkeratosis | **HP:0000962** Hyperkeratosis | Congenital/infancy | Increases relative to erythema over infancy | "Hyperkeratosis is seen in 30% to 79% of patients" (StatPearls, NBK507813) |
| Parakeratosis | **HP:0001036** Parakeratosis | — | — | Histologic, characteristic |
| Orthokeratosis (alternating with parakeratosis) | **HP:0040162** Orthokeratosis | — | — | Histologic |
| Epidermal acanthosis | **HP:0025092** Epidermal acanthosis | — | — | Histologic |
| Erythema | **HP:0010783** Erythema | Congenital | Wanes with age | Common |
| Nail dystrophy / onychodystrophy, onychorrhexis, periungual hyperkeratosis | **HP:0008404** Nail dystrophy; **HP:0001792** Small nail | Congenital/infancy | Persistent | GeneReviews: "Onychodystrophy, onychorrhexis, and periungual hyperkeratosis are common" (**PMID:21290788**) |
| Scarring alopecia (ipsilateral scalp) | **HP:0001596** Alopecia | Congenital | Persistent, non-regrowing | Reported, frequency unknown |

**Distinctive morphological features of the CHILD nevus** (these are *diagnostically* the most useful and worth curating as descriptors rather than as separate HP terms):

- **Strict midline demarcation** with **unilateral (lateralized) distribution** — "diffuse" lateralization rather than Blaschko-linear
- **Ptychotropism** — a striking predilection for **body folds and creases** (axillary, inguinal, intergluteal, popliteal). Happle coined the term:
  > "The associated CHILD nevus shows unique features such as a diffuse form of lateralization, ptychotropism, and microscopic changes of verruciform xanthoma."
  > — Happle R. *Semin Dermatol.* 1995;14(2):111-21. **PMID:7640190** (HUMAN_CLINICAL / expert review)
- **Waxy, yellowish adherent scale** (the yellow color reflects lipid/foam-cell content)
- **Face is usually spared** but can be involved (GeneReviews, **PMID:21290788**)
- **Right side affected roughly twice as often as left** (StatPearls, NBK507813) — an unexplained and epidemiologically odd finding that would be worth flagging as a knowledge gap

**Bilateral/symmetric exception.** Rare but genuine:
> "As an exception to this rule, in some cases the CHILD nevus may occur in a more or less bilateral distribution... A symmetric distribution of this nevus can exceptionally be seen in patients with CHILD syndrome, and this bilateral involvement should not mislead the clinician to any other diagnosis."
> — König A et al. *J Am Acad Dermatol.* 2002;46(4):594-6. **PMID:11907515** (HUMAN_CLINICAL)

Confirmed again in 2026 with a novel variant: a 7-year-old female "with bilateral involvement and a novel c.449 T>C (p.Phe150Ser) mutation in the NSDHL gene whose lesions cleared completely with topical cholesterol-lovastatin cream" (Zeyrek M, Balan K, Ersoy-Evans S. *Pediatr Dermatol.* 2026 May 5. **PMID:42083494**).

**Quality-of-life impact (cutaneous):** pruritus, malodor and maceration in intertriginous lesions (ptychotropism means the worst lesions sit in flexures), visible disfigurement with attendant psychosocial burden, and secondary bacterial/fungal infection risk. ⚠️ **No formal QoL instrument (EQ-5D, SF-36, DLQI, CDLQI, PROMIS) has been applied to a CHILD syndrome cohort** — this is a genuine, citable knowledge gap.

### 3.2 Musculoskeletal / limb phenotypes

| Feature | HPO suggestion | Notes |
|---|---|---|
| Ipsilateral limb reduction defect — spectrum from digit shortening to complete amelia | **HP:0009827** Amelia (severe end); **HP:0009812** / **HP:0009818** (upper/lower limb amelia) | GeneReviews: limb defects "range from shortening of the metacarpals and phalanges to absence of the entire limb" (**PMID:21290788**) |
| Aplasia of distal phalanges (2nd, 3rd fingers) | **HP:0009565**, **HP:0009429** | HPO-annotated for OMIM:308050 |
| Absent middle phalanx (2nd, 3rd fingers) | **HP:0009576**, **HP:0009438** | |
| Absent toe | **HP:0010760** | |
| Syndactyly (finger, toe, cutaneous 2-5, 4-5 toe) | **HP:0001159**, **HP:0006101**, **HP:0005650**, **HP:0004692** | A 2020 case report specifically links a novel *NSDHL* variant with syndactyly (BMC Med Genet, PMC7439548) |
| **Epiphyseal stippling (chondrodysplasia punctata)** | **HP:0010655** Epiphyseal stippling | "Radiographic epiphyseal stippling is a common diagnostic feature of CHILD syndrome, reported in 80% to 99% of cases" and "typically resolves by late childhood" (StatPearls, NBK507813). GeneReviews: "usually seen in the affected limb or body part" |
| Flexion contracture | **HP:0001371** | Progressive; a target for orthopedic management |
| Scoliosis | **HP:0002650** | Progressive; braces/surgery |
| Hemiatrophy / ipsilateral body hypoplasia | **HP:0100556** Hemiatrophy (+ **HP:0100558**, **HP:0100557** for limb-specific) | The "hemidysplasia" of the acronym |
| Vertebral hypoplasia | **HP:0008417** | Ipsilateral |
| Hypoplastic scapulae | **HP:0000882** | |
| Short clavicles | **HP:0000894** | |
| Short ribs | **HP:0000773** | |
| Hypoplastic pelvis | **HP:0008839** | |
| Congenital hip dislocation | **HP:0001374** | |
| Single transverse palmar crease | **HP:0000954** | |
| Short stature | **HP:0004322** | |

**Course:** limb defects are **congenital, static, and non-progressive** in their structural form; the *functional* consequences (contracture, scoliosis, gait) are **progressive** without intervention. Epiphyseal stippling is the exception — it **resolves spontaneously** in late childhood, making it a **time-limited diagnostic window** (a critical practical point: a normal skeletal survey in a teenager does not exclude CHILD syndrome).

**Quality-of-life impact:** severe. Limb hypoplasia/amelia drives lifelong mobility and dexterity limitation, prosthetic dependence, and educational/occupational impact. StatPearls notes complications of "contractures, immobility, poor dexterity in severe limb hypoplasia."

### 3.3 Visceral phenotypes (all characteristically **ipsilateral**)

| System | Feature | HPO suggestion |
|---|---|---|
| Cardiovascular | Abnormal cardiac septum morphology (ASD/VSD) | **HP:0001671** |
| Cardiovascular | Single ventricle | **HP:0001750** |
| Cardiovascular | Single coronary artery, unilateral ventricle (StatPearls) | — |
| Respiratory | Pulmonary hypoplasia (unilateral) | **HP:0002089** |
| Renal | Unilateral renal agenesis | **HP:0000122** |
| Renal | Hydronephrosis | **HP:0000126** |
| CNS | Aplasia/hypoplasia involving the CNS; ipsilateral brain, cranial nerve, and spinal cord hypoplasia; meningomyelocele | **HP:0002977** |
| CNS | Mild intellectual disability (**minority**) | **HP:0001256** |
| Endocrine | Thyroid hypoplasia | **HP:0005990** |
| Endocrine | Adrenal hypoplasia | **HP:0000835** |
| Reproductive | Ovarian and fallopian tube agenesis (StatPearls) | — |
| Craniofacial | Micrognathia; depressed nasal bridge; cleft upper lip | **HP:0000347**, **HP:0005280**, **HP:0000204** |
| Sensory | Hearing impairment | **HP:0000365** |
| Connective tissue | Umbilical hernia | **HP:0001537** |
| Growth | Mild intrauterine growth retardation | **HP:0008883** |
| GI (newly recognized) | Gastrointestinal/colonic xanthomas | ⚠️ No precise HP term identified — consider curating descriptively; see **PMID:39466221**, **PMID:40517742** |

*Source: HPO disease-annotation set for OMIM:308050, retrieved via https://ontology.jax.org/api/network/annotation/OMIM:308050 (2026-08-13); supplemented by StatPearls NBK507813 and GeneReviews PMID:21290788.*

**Cognition is a key negative finding.** GeneReviews states: **"Intellect is usually normal."** (**PMID:21290788**). Intellectual disability is the exception, not the rule, and this cleanly separates CHILD syndrome from the allelic CK syndrome.

**Left-sided disease appears worse.** StatPearls: "Left-sided involvement carries poorer prognosis due to higher visceral abnormality prevalence" (NBK507813) — plausibly because the heart is a left-sided structure. ⚠️ This is a synthesis claim in a review; it should be curated with appropriate epistemic hedging.

### 3.4 Laboratory abnormalities

| Finding | HPO / LOINC | Comment |
|---|---|---|
| Elevated 4α-methyl and 4α-carboxy sterol intermediates in plasma and skin scales | — (no precise HP term found) | The direct biochemical signature of NSDHL deficiency |
| Elevated 8-dehydrocholesterol | **HP:0003462** | The *EBP*-related subset (**PMID:10710233**) |
| Elevated 8(9)-cholestenol | **HP:0003465** | Ditto |
| **Serum total cholesterol: normal** | — | Critical negative finding — do not expect hypocholesterolemia |
| Dyslipidemia (reported in an adult with haploinsufficiency) | — | **PMID:40517742** |

Sterol profiling in a real patient (HUMAN_CLINICAL):
> "Sterol analysis from skin flakes revealed increased levels of a mono 4-alpha methyl sterol also seen in plasma as well as the presence of 4-alpha-carboxy-4-methyl-cholest-8(9)-en-3beta-ol and several keto-sterols, which are usually below the limit of detection. This sterol pattern is consistent with abnormal function of the 4-alpha-methylsterol-4-demethylase complex."
> — Maceda EBG, Kratz LE, Ramos VME, Abacan MAR. *BMJ Case Rep.* 2020;13(11):e236859. **PMID:33139364**

### 3.5 Clinical course descriptors

- **HP:0003577** Congenital onset
- **HP:0003826** Stillbirth (reflecting male in-utero lethality)
- **HP:0001423** X-linked dominant inheritance

---

## 4. Genetic / Molecular Information

### Causal gene

**NSDHL** — NAD(P) dependent 3-beta-hydroxysteroid dehydrogenase, `hgnc:13398`, OMIM **300275**, Xq28, NCBI Gene 50814, Ensembl ENSG00000147383, RefSeq NM_015922, UniProt **Q15738** (373 aa). Aliases: XAP104, H105e3, SDR31E1.

**Enzyme:** decarboxylating sterol-4-alpha-carboxylate 3-dehydrogenase, **EC 1.1.1.170**.

**UniProt-annotated function** (Q15738):
> "Catalyzes the NAD(P)(+)-dependent oxidative decarboxylation of the C4 methyl groups of 4-alpha-carboxysterols in post-squalene cholesterol biosynthesis (By similarity). Also plays a role in the regulation of the endocytic trafficking of EGFR (By similarity)"

**Representative catalytic reactions** (UniProt/Rhea): 4α-carboxyzymosterol + NADP⁺ → zymosterone + CO₂ + NADPH (RHEA:33455); 4β-methylzymosterol-4α-carboxylate + NADP⁺ → 3-dehydro-4-methylzymosterol + CO₂ + NADPH (RHEA:33447).

**Subcellular localization:** endoplasmic reticulum membrane (single-pass), evidence **ECO:0000269 PubMed:21129721**; also **lipid droplet**. UniProt note: "Trafficking through the Golgi is necessary for ER membrane localization."

GeneReviews frames the enzyme's role compactly: it "functions as a C4 demethylase in post-squalene cholesterol biosynthesis" (**PMID:21290788**).

### Pathogenic variants

**Variant classes and detection yield** (GeneReviews, NBK51754 / **PMID:21290788**):
- **~90% detected by sequence analysis**
- **~10% detected by gene-targeted deletion/duplication analysis**

This ~10% CNV fraction is clinically important. It has been demonstrated repeatedly:
> "The gene mutation is a large deletion of exon 3 and 4 of the NSDHL gene, which was discovered and reported for the first time in CHILD syndrome... Multiple exons deletions or microdeletion was not rare in CHILD syndrome. Classical Sanger sequencing may not be useful enough to find all kinds of mutations. Next-generation sequencing may be more effective."
> — Yu X et al. *J Eur Acad Dermatol Venereol.* 2018;32(7):1209-1213. **PMID:29341259** (HUMAN_CLINICAL)

And, most recently, via optical genome mapping (HUMAN_CLINICAL):
> "This study examines 3 pediatric patients exhibiting a compatible phenotype with inconclusive genetic studies, aiming to evaluate the diagnostic utility of optical genome mapping (OGM)... The identified structural variants consisted of deletions of varying sizes in the Xq28 cytoband, encompassing regions that contain exons."
> — Vergara A et al. *Mol Syndromol.* 2025 Dec 19. **PMID:41625319**

**Variant types reported:** missense, nonsense, frameshift (small indels), splice-site, and multi-exon deletions. The foundational spectrum survey is **Bornholdt D et al., "Mutational spectrum of NSDHL in CHILD syndrome," *J Med Genet.* 2005;42(2):e17, PMID:15689440** (⚠️ *this paper has no PubMed abstract; I could not retrieve its full text in this session. Do not curate specific variant counts from it without reading the PDF — PMC1735983*).

**Specific variants with published support** (all HUMAN_CLINICAL unless noted):

| Variant | Consequence | Context | Source |
|---|---|---|---|
| c.262C>T (p.Arg88Ter) | Nonsense | **Somatic mosaicism in a surviving male** with CHILD syndrome | GeneReviews **PMID:21290788** |
| c.130G>A (p.Gly44Ser) | Missense; initially VUS, reclassified **likely pathogenic** after de novo confirmation; absent from ExAC | Female with classic CHILD + confirmatory sterol profile | **PMID:33139364** |
| c.123delA (p.Val42Ter) | Frameshift/nonsense | 14-year-old Chinese girl, CHILD without limb defects, co-occurring linear porokeratosis | **PMID:40464756** |
| c.449T>C (p.Phe150Ser) | Missense, novel | 7-year-old female with **bilateral** involvement | **PMID:42083494** |
| Deletion of exons 3 and 4 | Multi-exon deletion | Chinese patient mimicking verrucous nevus | **PMID:29341259** |
| c.790-6C>T | Intronic/splice-region, novel | **Male fetus**, recurrent miscarriage; maternally inherited | **PMID:36504312** |
| Xq28 deletions (variable size, exon-containing) | Structural | Detected only by OGM after inconclusive standard testing | **PMID:41625319** |
| c.455G>A; c.696_698delGAA (p.Lys232del); c.1098dupT (p.Arg367SerfsTer33) | **Hypomorphic** — cause **CK syndrome, not CHILD** | Only three CK-causing variants known | GeneReviews **PMID:21290788**; **PMID:21129721** |

**ACMG/AMP classification landscape.** ClinVar holds **545 variant records for *NSDHL***, of which **203 carry a pathogenic clinical-significance property** (NCBI E-utilities esearch against ClinVar, queried 2026-08-13). ⚠️ These counts include CK syndrome and non-disease submissions; treat as an order-of-magnitude figure, not a curated CHILD-specific count.

**Allele frequency.** Pathogenic *NSDHL* alleles are **absent from population databases** — expected for an X-linked male-lethal condition under strong purifying selection. The Maceda variant is explicitly noted as "not included in population databases (ExAC no frequency)" (**PMID:33139364**). ⚠️ I did not query gnomAD directly in this session; a curator should pull gnomAD v4 constraint metrics (pLI / LOEUF) for *NSDHL* before making a constraint claim.

**Somatic vs germline.** Predominantly **germline** (de novo or maternally inherited). **Post-zygotic somatic mosaicism** is the accepted explanation for rare surviving affected males (GeneReviews, **PMID:21290788**). COSMIC/TCGA somatic *NSDHL* mutation in cancer is a separate topic — see the EGFR/oncology link in §6.

### Functional consequences of variants

- **CHILD syndrome:** **complete or near-complete loss of function** → "loss of functional decarboxylating sterol-4-alpha-carboxylate 3-dehydrogenase" (GeneReviews).
- **CK syndrome (allelic, X-linked, affects males):** **partial loss of function** via hypomorphic, conformationally unstable alleles. This dosage relationship is the cleanest genotype–phenotype axis in the *NSDHL* literature: near-null → female-limited CHILD with male lethality; hypomorphic → male-viable CK syndrome with neurodevelopmental rather than dermatologic dominance.
  > "These two mutations, which alter protein folding, show temperature-sensitive protein stability and complementation in Erg26-deficient yeast."
  > — McLarren KW et al. *Am J Hum Genet.* 2010;87(6):905-14. **PMID:21129721** (HUMAN_CLINICAL + IN_VITRO)

- **Missense variants act largely by destabilizing the protein** (IN_VITRO): "protein expression levels were low for all mutants" across 13 missense and one deletion variant (**PMID:40222685**).

**⚠️ Curation note on the GOF/LOF slot:** for *variant* consequence use `GeneticContext.functional_impact_category: LOSS_OF_FUNCTION` (CHILD) / `PARTIAL_LOSS_OF_FUNCTION` (CK). For the *pathway state* node ("cholesterol biosynthesis"), use `Descriptor.modifier: DECREASED` — this is a quantitative reduction in a normally-regulated pathway, not escape from regulatory control.

### Modifier genes

**None established.** The principal phenotype modifier is **stochastic X-inactivation ratio**, not a second locus. A single case reported co-occurring compound heterozygous *PMVK* variants (c.88C>T, p.Gln30Ter) alongside the *NSDHL* variant, in a patient with both CHILD syndrome and linear porokeratosis (**PMID:40464756**) — but this is a **coincidental second mendelian disorder (porokeratosis is *PMVK*-related), not a modifier**, and should be curated as such.

### Epigenetic information

**X-chromosome inactivation is the central epigenetic mechanism of this disease** — arguably CHILD syndrome is the textbook dermatologic demonstration of functional X mosaicism. GO term suggestion for the mechanism: consider curating XCI descriptively; no disease-specific DNA-methylation or histone-modification study of CHILD syndrome tissue exists in ENCODE/Roadmap/DiseaseMeth as far as I could determine. ⚠️ **No CHILD-specific methylome or epigenome dataset identified.**

### Chromosomal abnormalities

No aneuploidy, translocation, or inversion is characteristic. The relevant structural lesions are **submicroscopic Xq28 deletions** encompassing *NSDHL* exons — below karyotype resolution, at or below chromosomal-microarray resolution in some cases, and detectable by NGS-based CNV calling or optical genome mapping (**PMID:41625319**, **PMID:29341259**).

---

## 5. Environmental Information

- **Environmental factors:** none causally implicated. No CTD/TOXNET/EPA-relevant exposure has been associated with CHILD syndrome.
- **Lifestyle factors:** none implicated in causation. Relevant only to symptom management (emollient use, avoidance of skin trauma/maceration in flexures).
- **Infectious agents:** none causal. Secondary bacterial and fungal infection of the eroded, macerated ptychotropic lesions is a recognized **complication** (StatPearls, NBK507813) — curate as a downstream consequence, not an etiology.

⚠️ For a dismech entry, the `environmental:` block should be **absent or empty** for etiology. If curated at all, restrict it to therapeutic/topical exposures with `influences_mechanisms` targeting the cutaneous nodes.

---

## 6. Mechanism / Pathophysiology

### The causal chain, from lesion to clinic

```
NSDHL loss-of-function variant (Xq28, heterozygous female)
  │
  ├─► random X-chromosome inactivation
  │     └─► mosaic patches of NSDHL-null vs NSDHL-competent cells
  │
  ▼
Loss of decarboxylating sterol-4α-carboxylate 3-dehydrogenase (EC 1.1.1.170)
  │
  ├─► BLOCK in C4-demethylation step of post-squalene cholesterol biosynthesis
  │
  ├──────────────► (A) DEFICIENCY of end-product cholesterol in situ
  │                      │
  │                      ├─► impaired lamellar-body lipid processing
  │                      ├─► defective epidermal permeability barrier
  │                      ├─► compensatory keratinocyte hyperproliferation
  │                      │      → psoriasiform acanthosis, hyperkeratosis,
  │                      │        parakeratosis  → the CHILD nevus
  │                      └─► impaired SHH signaling (cholesterol is required
  │                             both for SHH autoprocessing/lipid modification
  │                             and for Smoothened function)
  │                             → disrupted limb/organ patterning
  │
  └──────────────► (B) ACCUMULATION of toxic 4α-methyl / 4α-carboxy sterol
                          intermediates
                          │
                          ├─► direct cytotoxicity → cell death
                          ├─► foam-cell formation in papillary dermis
                          │      (lipid-laden macrophages, CD68+/CD163+)
                          │      → verruciform-xanthoma-like histology
                          ├─► deranged EGFR/ERBB endocytic trafficking
                          │      and growth-factor-receptor signaling
                          └─► NEGATIVE SELECTION of mutant-expressing cells
                                 │
                                 ▼
                       Progressive clearance of NSDHL-null keratinocytes and
                       fibroblasts from the unaffected side
                                 │
                                 ▼
                       STRICT LATERALIZATION with midline demarcation
```

### The two-hit metabolic logic (deficiency **and** toxicity)

This is the single most important mechanistic concept for CHILD syndrome, because it directly dictates therapy. Paller et al. established both arms and used them to design treatment (HUMAN_CLINICAL + ultrastructure):

> "On the basis of the putative pathogenic role of both pathway-product deficiency of cholesterol and accumulation of toxic metabolic intermediates, we assessed the efficacy of combined therapy with lovastatin and cholesterol... Ultrastructural analysis of affected skin showed evidence of both cholesterol depletion and toxic metabolic accumulation. Topical treatment with lovastatin/cholesterol (but not cholesterol alone) virtually cleared skin lesions by 3 months, accompanied by histological and ultrastructural normalization of epidermal structure and lipid secretion."
> — Paller AS, van Steensel MA, Rodriguez-Martín M, Sorrell J, Heath C, Crumrine D, van Geel M, Cabrera AN, Elias PM. *J Invest Dermatol.* 2011;131(11):2242-8. **PMID:21753784**

The **"but not cholesterol alone"** clause is the decisive experimental evidence that toxic intermediate accumulation, not cholesterol deficiency alone, drives the cutaneous phenotype. This is a rare instance of a therapeutic result functioning as a mechanistic proof.

The same principle was independently argued for the allelic disorder: "We hypothesize that methyl sterol accumulation, not only cholesterol deficiency, causes CKS, given that cerebrospinal fluid cholesterol, plasma cholesterol, and plasma 24S-hydroxycholesterol levels are normal in males with CKS." (**PMID:21129721**)

### The lateralization mechanism — cell-autonomous negative selection

Paller et al. resolved a 30-year mystery:
> "The unusual lateralization of abnormalities in CHILD syndrome reflects selective clearance of keratinocytes and fibroblasts that express the mutant allele from the unaffected side."
> — **PMID:21753784**

The mouse work supports the same logic and adds a striking temporal dimension (MODEL_ORGANISM):
> "Clonal populations of mutant cells were visible in the brain, skin and liver of Bpa(1H) pups. In the liver, the proportion of NSDHL negative cells dropped from approximately 50% at postnatal day 6 to approximately 20% at one year of age. In the brain... the proportion of NSDHL negative cells also dropped dramatically over the first year of life. Our results suggest that while NSDHL-deficient cells in the mosaic Bpa(1H) female are able to survive and differentiate during embryonic development, they are subject to negative selection over the life of the animal."
> — Cunningham D, Spychala K, McLarren KW, Garza LA, Boerkoel CF, Herman GE. *Mol Genet Metab.* 2009;98(4):356-66. **PMID:19631568**

**This directly explains the natural history**: skin lesions improve with age because mutant clones are progressively outcompeted. It also explains why the disease is a *developmental* one — the damage is done during the window when mutant cells are still abundant.

### Sonic hedgehog signaling — the link to malformation

Cholesterol is mechanistically required for Hedgehog signaling at two levels: SHH undergoes autocatalytic cleavage with covalent cholesterol modification of its N-terminal signaling domain, and Smoothened activity is sterol-regulated. The most direct experimental demonstration in an *Nsdhl* model (MODEL_ORGANISM + IN_VITRO):

> "Histological abnormalities include progressive loss of cortical and hippocampal neurons, as well as deficits in the proliferation and migration of cerebellar granule precursors and subsequent massive apoptosis of the cerebellar cortex. We replicated the granule cell precursor proliferation defect in vitro and demonstrate that it results from defective signaling by SHH. Furthermore, this defect is almost completely rescued by supplementation of the culture media with exogenous cholesterol, while methylsterol accumulation above the enzymatic block appears to be associated with increased cell death."
> — Cunningham D, DeBarber AE, Bir N, Binkley L, Merkens LS, Steiner RD, Herman GE. *Hum Mol Genet.* 2015;24(10):2808-25. **PMID:25652406**

Note the elegance: **both arms of the two-hit model are separately demonstrated in one experiment** — cholesterol rescue fixes the SHH proliferation defect, while methylsterol accumulation independently causes cell death.

StatPearls summarizes the developmental consequence: deficient enzyme activity "disrupts sonic hedgehog (SHH) protein signaling during embryonic limb development and organogenesis, explaining the characteristic unilateral presentation" (NBK507813).

**GO suggestion:** `GO:0007224` smoothened signaling pathway (`modifier: DECREASED`).

### Protein dysfunction

Mutant NSDHL is predominantly a **protein-stability** problem rather than a catalytic-site problem, and it is chaperone-dependent (IN_VITRO, **PMID:40222685**): all 13 missense mutants surveyed showed low expression; some were rescued by 30°C or by glycerol; HSP70 and HSP90 are needed for optimal wild-type expression. Combined with the temperature-sensitive CK alleles (**PMID:21129721**), this establishes **misfolding/instability** as the dominant molecular mechanism for missense alleles — and opens a **pharmacological chaperone** therapeutic direction.

**GO/CC suggestions:** `GO:0005789` endoplasmic reticulum membrane; `GO:0005811` lipid droplet (⚠️ verify this ID against OLS before curating — I verified `GO:0042599` lamellar body but did not verify lipid droplet).
**GO/MF suggestion:** `GO:0000252` — 3-beta-hydroxysteroid dehydrogenase [NAD(P)+]/C4-decarboxylase activity (verified via OLS4), `modifier: LOSS_OF_FUNCTION`.
**GO/BP suggestions:** `GO:0006695` cholesterol biosynthetic process (`modifier: DECREASED`); `GO:0007224` smoothened signaling pathway (`DECREASED`); `GO:0061436` establishment of skin barrier (`DECREASED`); `GO:0042599` lamellar body (CC, abnormal).

### Metabolic changes

- Block at the **C4-demethylation** step of post-squalene cholesterol synthesis (lanosterol → zymosterol segment).
- Accumulation of 4α-methyl and 4α-carboxy sterols, plus keto-sterols normally below detection (**PMID:33139364**).
- **Systemic cholesterol is preserved** — dietary uptake and hepatic synthesis in wild-type-expressing cells compensate. The lesion is **compartmental**: skin (behind the permeability barrier) and brain (behind the blood-brain barrier) cannot import cholesterol and therefore bear the phenotype. Cunningham et al. make this argument explicitly: "These data support the absolute requirement for cholesterol synthesis in situ once the blood-brain-barrier forms and cholesterol transport to the fetus is abolished." (**PMID:25652406**)

**CHEBI suggestions:** `CHEBI:16113` cholesterol; `CHEBI:16521` lanosterol (all verified via OLS4).

### Tissue damage mechanisms

- **Epidermal barrier failure** from abnormal lamellar-granule (lamellar body) content and secretion (IN_VITRO/ultrastructural, HUMAN_CLINICAL tissue):
  > "Electron microscopy revealed vesicular structures in the intercellular spaces of the stratum corneum and vacuoles or vesicular structures in upper prickle cell layer. Some of them can be recognized as abnormal lamellar granules. Within the foamy cells in the papillary dermis, large vacuoles were found... These findings suggested that abnormal lipid metabolism involving lamellar granules may be responsible to the skin lesion of CHILD syndrome."
  > — Ishibashi M, Matsuda F, Oka H, Ishiko A. *J Cutan Pathol.* 2006;33(6):447-53. **PMID:16776722**
- **Foam-cell (xanthomatous) infiltration** of the papillary dermis — lipid-laden macrophages accumulating undegradable sterol intermediates. StatPearls: "Dermal foam cells express macrophage markers (CD68, CD163) but lack epithelial markers (AE1/AE3, S100)."
- **Apoptotic cell death** driven by methylsterol accumulation (**PMID:25652406**).
- No evidence for oxidative-stress-, ischemia-, or fibrosis-driven damage as a primary mechanism. Note, however, that the 2026 review of post-lanosterol disorders lists "oxidative stress" among the shared pathogenic themes for this disease class (**PMID:42589509**) — curate that as class-level, not CHILD-specific.

### Immune system involvement

**Not an immune-mediated disease.** The lesion is called "inflammatory" descriptively (erythema, psoriasiform histology), and macrophage-derived foam cells are prominent, but there is **no autoimmunity, no immunodeficiency, and no evidence of a primary immune driver**. The inflammation is secondary to barrier failure and lipid accumulation. ⚠️ Do not curate autoimmune or immunodeficiency mechanisms.

### The unexpected oncology connection (NSDHL–EGFR trafficking)

A mechanistically important finding that also explains why ketoconazole works (IN_VITRO + MODEL_ORGANISM):

> "We established that inactivation of 2 sterol biosynthesis pathway genes, SC4MOL (sterol C4-methyl oxidase-like) and its partner, NSDHL (NADP-dependent steroid dehydrogenase-like), sensitized tumor cells to EGFR inhibitors... an unexpected role for SC4MOL and NSDHL in controlling the signaling, vesicular trafficking, and degradation of EGFR and its dimerization partners, ERBB2 and ERBB3. Metabolic block upstream of SC4MOL with ketoconazole or CYP51A1 siRNA rescued cancer cell viability and EGFR degradation... Analysis of Nsdhl-deficient Bpa(1H/+) mice confirmed dramatic and selective loss of internalized platelet-derived growth factor receptor in fibroblasts, and reduced activation of EGFR and its effectors in regions of skin lacking NSDHL."
> — Sukhanova A et al. *Cancer Discov.* 2013;3(1):96-111. **PMID:23125191**

Two things fall out of this for CHILD syndrome specifically: (i) reduced EGFR signaling in NSDHL-null skin is a plausible contributor to the abnormal keratinocyte phenotype; and (ii) **ketoconazole's therapeutic benefit has a mechanistic rationale** — blocking CYP51A1 upstream prevents accumulation of the toxic C4-methylsterols and restores receptor trafficking.

### Molecular profiling

- **Transcriptomics:** Paller et al. analyzed "gene activation in abnormal and unaffected skin" (**PMID:21753784**) — the only such analysis I identified. ⚠️ No GEO/ArrayExpress accession verified in this session.
- **Proteomics / metabolomics / lipidomics:** ⚠️ No dedicated CHILD syndrome dataset identified in PRIDE, MetaboLights, or Metabolomics Workbench. Clinical sterol profiling by GC-MS (Kennedy Krieger Biochemical Genetics Laboratory is the reference lab in published cases) serves the metabolomic function in practice.
- **Single-cell / spatial transcriptomics:** ⚠️ None published. This is a conspicuous gap: a mosaic disease with a sharp midline boundary is close to an ideal spatial-transcriptomics subject, and the "which cells are cleared, and when" question is directly addressable by single-cell work.
- **Functional genomics screens:** the *SC4MOL*/*NSDHL* EGFR-sensitization work (**PMID:23125191**) used siRNA-based approaches; DepMap contains *NSDHL* dependency data for cancer lines (⚠️ not queried in this session).

### Cell types and biological processes for KB curation

| Cell type | CL term (verified via OLS4) | Role |
|---|---|---|
| Keratinocyte | **CL:0000312** | Primary affected cell; site of the barrier defect and of clonal clearance |
| Foam cell | **CL:0000891** | Dermal lipid-laden cells; verruciform-xanthoma histology |
| Macrophage-derived foam cell | **CL:0000517** | CD68⁺/CD163⁺ per StatPearls |
| Fibroblast | **CL:0000057** | Second cell type shown to undergo selective clearance (**PMID:21753784**) |
| Macrophage | ⚠️ verify `CL:0000235` before use | |
| Chondrocyte | **CL:0000138** | Epiphyseal stippling / chondrodysplasia punctata |

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
- **Skin** — `UBERON:0002097` skin of body; `UBERON:0001003` skin epidermis (verified via OLS4). Stratum corneum `UBERON:0002027`, stratum spinosum `UBERON:0002026`, stratum granulosum `UBERON:0002069`, stratum basale `UBERON:0002025`.
- **Papillary dermis** — `UBERON:0001992` papillary layer of dermis (foam-cell infiltrate).
- **Limbs** — `UBERON:0002101` limb.
- **Epiphyses / cartilaginous structures** — `UBERON:0001437` epiphysis (stippling).
- **Nails** — nail unit (onychodystrophy, periungual hyperkeratosis).

**Secondary / variable ipsilateral involvement:**
- Heart (septa, coronary artery, ventricle) — cardiovascular system
- Lung (unilateral hypoplasia) — respiratory system
- Kidney (agenesis, hydronephrosis) — genitourinary system
- Brain, cranial nerves, spinal cord (ipsilateral hypoplasia, meningomyelocele) — nervous system
- Thyroid and adrenal glands — endocrine system
- Ovary, fallopian tube — reproductive system
- Vertebrae, ribs, scapula, clavicle, pelvis — skeletal system
- Colon/GI tract (xanthomas — newly recognized, **PMID:39466221**, **PMID:40517742**) — digestive system

### Tissue and cell level

- **Epithelial tissue** — epidermal keratinocytes (`CL:0000312`), the dominant affected population
- **Connective tissue** — dermal fibroblasts (`CL:0000057`); cartilage chondrocytes (`CL:0000138`)
- **Immune/myeloid** — dermal foam cells (`CL:0000891`), macrophage-derived (`CL:0000517`)

### Subcellular level

- **Endoplasmic reticulum membrane** — `GO:0005789` — NSDHL's site of action (UniProt evidence ECO:0000269 PubMed:21129721)
- **Lipid droplet** — secondary NSDHL localization
- **Lamellar body (lamellar granule)** — `GO:0042599` (verified via OLS4) — structurally abnormal in CHILD skin (**PMID:16776722**); the proximate cause of barrier failure
- **Stratum corneum intercellular lipid lamellae** — abnormal vesicular structures on EM (**PMID:16776722**)

### Localization and lateralization

**This is the single most distinctive anatomical fact about CHILD syndrome and deserves explicit structured curation:**
- **Strictly unilateral** in the overwhelming majority, with **sharp midline demarcation** on the trunk
- **Right side ≈ 2× more often than left** (StatPearls, NBK507813)
- **Ipsilateral** concordance across skin, skeleton, and viscera — the skin lesion predicts which side the visceral anomalies will be on
- **Bilateral/near-symmetric distribution is a rare but real exception** (**PMID:11907515**, **PMID:42083494**) and must not redirect the diagnosis
- **Face usually spared**
- **Ptychotropic** — preferentially in flexural creases
- **Not Blaschko-linear in the classic narrow-banded sense** — the lateralization is "diffuse" (**PMID:7640190**), which distinguishes the CHILD nevus from ILVEN and most epidermal nevi

---

## 8. Temporal Development

### Onset

- **Congenital** (`HP:0003577`). Limb and visceral malformations are established in embryogenesis.
- **Skin:** "The ichthyosiform skin lesions are usually present at birth or in the first weeks of life" (GeneReviews, **PMID:21290788**); Happle 1980: "The dermatosis is either present at birth or develops during the first weeks of life" (**PMID:7408908**). GeneReviews extends the window to "the first weeks to few months of life."
- **Late-onset presentation exists:** StatPearls notes symptoms "may appear as late as age 9 years" (NBK507813).
- **Onset pattern:** congenital/insidious for the skin; the malformations are simply present from birth.

### Progression

- **No formal disease staging system exists.** CHILD syndrome is not staged.
- **Skeletal malformations:** static/non-progressive in structure.
- **Skin:** dynamic and, on balance, **improving**. Erythema decreases while hyperkeratosis increases during infancy; overall "Dermatologic symptoms improve with age" (StatPearls). The mechanistic basis is progressive negative selection against mutant clones (**PMID:19631568**, **PMID:21753784**).
- **Important counter-current:** **"new lesions can develop in later life"** and GeneReviews' surveillance guidance specifically warns that "new lesions may occur in puberty or early adulthood" (**PMID:21290788**). So the course is best described as **improving with episodic new lesion formation**, not monotonically remitting.
- **Epiphyseal stippling resolves by late childhood** (StatPearls) — a genuinely time-limited sign.
- **Secondary progressive complications:** joint contractures and scoliosis worsen without orthopedic management.
- **Duration:** **chronic and lifelong**.

### Patterns

- **Remission:** partial spontaneous improvement of skin with age (natural, clone-selection-driven). **Treatment-induced near-complete remission** of skin lesions is achievable with topical statin/cholesterol — "virtually cleared skin lesions by 3 months" (**PMID:21753784**); "cleared completely" (**PMID:42083494**); improvement within 4 weeks (**PMID:40464756**).
- **Critical periods:**
  - **Embryogenesis** — the only window in which the limb/visceral malformations could theoretically be prevented; no intervention exists.
  - **First weeks to months of life** — optimal window to initiate skin therapy and to complete imaging/organ evaluation. StatPearls: imaging "detect[s] skeletal and visceral anomalies, enabling early intervention," and "Early detection and timely management improve patient outcomes substantially."
  - **Early childhood** — the diagnostic window during which epiphyseal stippling is still radiographically visible.
  - **Puberty/early adulthood** — surveillance window for new cutaneous lesions.
  - **Neonatal period** — highest mortality risk if severe cardiac or pulmonary anomalies are present.

---

## 9. Inheritance and Population

### Epidemiology

- **Reported cases:** GeneReviews (2024 update): **"More than 60 individuals have been reported to date."** (**PMID:21290788**). StatPearls: "fewer than 100 CHILD syndrome cases have been reported in the literature."
- **Incidence:** StatPearls cites "approximately 1 in 100,000 live births" (NBK507813). ⚠️ **This figure is internally inconsistent with "fewer than 100 reported cases"** — at 1/100,000 live births, world annual births alone would generate ~1,300 cases per year. Treat the 1/100,000 figure as **unreliable/unsourced**. Orphanet does not publish a numeric prevalence for ORPHA:139 that I could retrieve (the Orphanet API endpoints for epidemiological data returned 404 in this session).
- **Recommended dismech `prevalence` curation:** `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`, with `notes` recording the ">60 reported individuals" figure and its GeneReviews source. **Do not curate `rate_per_100000: 1.0` on the strength of the StatPearls sentence.**
- **Prevalence/incidence by geography:** no registry data. Cases are reported worldwide (Germany, Japan, China, Philippines, Turkey, USA, Saudi Arabia, Brazil, Spain, UK) with no evident geographic clustering.

### Genetic epidemiology

- **Inheritance pattern:** **X-linked dominant, male-lethal** (`HP:0001423`). Happle's original inference from the sex ratio: "Arguments are presented in favor of the hypothesis that the conditions is due to an X-linked dominant gene lethal in hemizygous males." (**PMID:7408908**)
- **Sex ratio:** Happle 1980, from 20 cases: **"The ratio of females to males is 19 : 1."** (**PMID:7408908**) That single male is now understood to reflect somatic mosaicism.
- **Recurrence risk (GeneReviews, **PMID:21290788**):**
  > "If the mother of a proband has an NSDHL pathogenic variant, the chance of transmitting it in each pregnancy is 50%. However, since studies suggest that male conceptuses with an NSDHL pathogenic variant generally abort or resorb spontaneously, the expected live-born distribution is: 33% heterozygous (typically) affected females; 33% unaffected females; and 33% unaffected males."
- **Male lethality — direct molecular evidence** (HUMAN_CLINICAL):
  > "A 33-year-old pregnant woman with recurrent spontaneous abortion was experiencing her third pregnancy with a male embryo. In this pregnancy, a miscarriage occurred at a gestational age of 10+6 weeks with no copy number variants. However, a novel mutation c.790-6C>T in the NSDHL gene was observed in the fetus through whole-exome sequencing (WES). Parental verification indicated that the NSDHL gene variant was inherited from the mother."
  > — Zhuang J et al. *Mol Genet Genomic Med.* 2023;11(3):e2121. **PMID:36504312**

  This makes **recurrent male miscarriage a recognizable presenting feature of a maternal *NSDHL* variant** — clinically actionable and worth curating explicitly.
- **Surviving affected males:** explained by **post-zygotic somatic mosaicism**; the documented example is a male "mosaic for NSDHL pathogenic variant c.262C>T (p.Arg88Ter)" (GeneReviews, **PMID:21290788**). König et al. also reported "one boy" among their six patients (**PMID:10710235**).
- **Penetrance:** effectively **complete** in heterozygous females. No unaffected obligate female carriers are described.
- **Expressivity:** **highly variable** — from complete amelia with multi-organ malformation to a mild adult presenting with GI xanthomas and ichthyosis only (**PMID:39466221**). The variability is driven principally by X-inactivation pattern, not by allele.
- **Genetic anticipation:** **not applicable** (no repeat expansion).
- **Germline mosaicism:** not specifically documented for *NSDHL*, but somatic mosaicism is established; germline mosaicism cannot be excluded and should be mentioned in counseling.
- **Founder effects:** **none reported.**
- **Consanguinity:** **not relevant** — this is an X-linked dominant, not a recessive, disorder.
- **Carrier frequency:** **not applicable in the usual sense.** Heterozygous females *are* affected; there is no asymptomatic carrier state.

### Population demographics

- **Sex:** overwhelmingly **female** (~95%+). Affected males are exceptional and mosaic.
- **Ethnicity/ancestry:** no predilection reported; cases published across East Asian, South Asian, European, Middle Eastern, Southeast Asian, and Latin American populations.
- **Age distribution:** diagnosis is typically neonatal/infantile; a growing tail of adult diagnoses is emerging as mild phenotypes are recognized (**PMID:39565229** — adult treated with ketoconazole; **PMID:39466221**, **PMID:40517742** — adults presenting through gastroenterology).
- **Geographic distribution of variants:** none — variants are private/de novo. No recurrent hotspot has been established beyond the three known CK-syndrome alleles.

### The allelic disorder, for contrast

**CK syndrome** (OMIM 300831), caused by hypomorphic *NSDHL* alleles, is **X-linked recessive and affects males**. GeneReviews: "To date, 25 affected males from three unrelated families have been reported." Features: "mild-to-severe intellectual disability," seizures in infancy in all affected males, cortical malformations (most consistent with polymicrogyria), microcephaly "greater than 2-3 standard deviations below the mean," thin habitus with long thin digits, strabismus, optic atrophy, scoliosis/kyphosis, and behavioral problems (aggression, ADHD, irritability). Heterozygous females "may have a range of behavioral problems including irritability and aggression" but have "normal physical features, intellect, and brain imaging."

---

## 10. Diagnostics

### Clinical tests

**Laboratory / biochemical**
- **Plasma and skin-scale sterol profiling by GC-MS** — the disease-specific biochemical test. Elevated **C4-methylated and C4-carboxylated sterol intermediates**; see the verbatim sterol pattern in **PMID:33139364**. Reference laboratory in published cases: Kennedy Krieger Institute Biochemical Genetics Laboratory.
- **Serum total cholesterol** — **typically normal**; a normal value does *not* exclude the diagnosis. ⚠️ This is a common source of diagnostic error.
- For the *EBP*-related subset: elevated **8-dehydrocholesterol** (`HP:0003462`) and **8(9)-cholestenol** (`HP:0003465`) (**PMID:10710233**).
- LOINC: standard cholesterol panels (e.g., LOINC:2093-3 total cholesterol) ⚠️ *not verified in this session*. There is **no standard LOINC code for the diagnostic methylsterol panel** — it is a specialized send-out.

**Imaging**
- **Radiographs / skeletal survey** — for limb reduction defects and **epiphyseal stippling** (`HP:0010655`). Must be done in early childhood before stippling resolves.
- **Echocardiography** — septal defects, single ventricle, coronary anomalies.
- **Renal ultrasound** — agenesis, hydronephrosis.
- **Chest imaging** — pulmonary hypoplasia.
- **Brain MRI** — ipsilateral cerebral hypoplasia, cranial nerve/spinal cord anomalies, meningomyelocele.
- **Colonoscopy** — newly relevant for xanthomas in mild adult phenotypes (**PMID:40517742**).

**Biopsy / histopathology** — a strong diagnostic anchor:
- **Psoriasiform epidermal hyperplasia** with hyperkeratosis, alternating orthokeratosis and parakeratosis, acanthosis, papillomatosis (StatPearls, NBK507813)
- **Foam cells in the papillary dermis**, CD68⁺/CD163⁺, negative for AE1/AE3 and S100 (StatPearls)
- **Verruciform xanthoma-like features** — "The histology shared many features with verruciform xanthoma" (**PMID:16776722**); Happle described "microscopic changes of verruciform xanthoma" as a defining feature of the CHILD nevus (**PMID:7640190**)
- **Electron microscopy:** abnormal lamellar granules; intercellular vesicular structures in stratum corneum; large vacuoles in dermal foam cells (**PMID:16776722**)

**Functional tests / electrophysiology** — not disease-specific; ordered according to organ involvement (echo, ECG if cardiac; audiometry given `HP:0000365`; ophthalmology assessment).

### Genetic testing

**Recommended approach:**
1. **Single-gene *NSDHL* sequencing** (or targeted gene panel including *NSDHL* and *EBP*) — first-line given the highly recognizable phenotype. Yield **~90%** by sequence analysis (GeneReviews).
2. **Gene-targeted deletion/duplication analysis** — **mandatory second step**; **~10%** of pathogenic variants are CNVs (GeneReviews). Sanger-only testing is explicitly inadequate: "Classical Sanger sequencing may not be useful enough to find all kinds of mutations" (**PMID:29341259**).
3. **Whole-exome sequencing (WES)** — useful when the phenotype is atypical, or in the prenatal/recurrent-miscarriage setting (**PMID:36504312**).
4. **Whole-genome sequencing (WGS)** — used in at least one report to resolve both *NSDHL* and a second locus (**PMID:40464756**).
5. **Optical genome mapping (OGM)** — a genuinely new option for cases with compatible phenotype but inconclusive standard testing (**PMID:41625319**).
6. **Chromosomal microarray (CMA)** — can detect larger Xq28 deletions but was negative in the fetal case where WES found a splice variant (**PMID:36504312**).
7. **Karyotyping / FISH** — **not useful**; the lesions are submicroscopic.
8. **Mitochondrial DNA testing / repeat expansion testing** — **not applicable.**
9. **Ichthyosis gene panels** typically include *NSDHL* — a practical route when the presenting specialty is dermatology.

**GTR:** "NSDHL-Related Disorders" clinical genetic test, GTR test ID 317493.

**Biochemical testing as an adjunct to VUS resolution:** in **PMID:33139364**, a sterol profile consistent with 4α-methylsterol-4-demethylase dysfunction plus de novo status upgraded a VUS (c.130G>A) to likely pathogenic. This is a **model workflow** worth curating: biochemistry supplies the functional evidence line (PS3-adjacent) that variant-level data alone cannot.

### Omics-based diagnostics

- **RNA sequencing:** could clarify splice-region variants such as c.790-6C>T (**PMID:36504312**) — no published diagnostic RNA-seq series for *NSDHL*.
- **Proteomics / epigenomics / liquid biopsy:** ⚠️ **not established, not applicable.**
- **Targeted metabolomics (sterol GC-MS)** is, in practice, the operative "omics" diagnostic.

### Clinical criteria

**No formal consensus diagnostic criteria (no DSM/ICD-style checklist, no society guideline) exist.** GeneReviews frames it as suggestive findings + molecular confirmation:

*Suggestive findings for CHILD syndrome* (GeneReviews, **PMID:21290788**):
- Unilateral ichthyosiform nevus
- Ipsilateral limb defects
- Punctate cartilage calcifications
- CNS and visceral anomalies

*Diagnosis established* in a female proband with a **heterozygous *NSDHL* pathogenic (or likely pathogenic) variant** identified by molecular genetic testing.

Happle's point (**PMID:11907515**) that "a diagnosis of CHILD syndrome can be based on clinical features such as the highly characteristic morphology of the CHILD nevus" remains the practical clinical reality.

### Differential diagnosis

| Condition | Gene / MONDO | Distinguishing features |
|---|---|---|
| **X-linked dominant chondrodysplasia punctata (CDPX2 / Conradi-Hünermann-Happle)** | *EBP* | GeneReviews: "Absence of strict midline demarcation & lack of unilaterality seen in CHILD syndrome"; "Skin findings fade over time"; "Ocular anomalies are prominent" (cataracts). Grange 2000 notes "the skeletal defects and skin lesions in CDPX2 are bilateral and asymmetric" (**PMID:10710233**). ⚠️ **But some CHILD phenotypes are *EBP*-caused** — the boundary is genuinely blurred |
| **Inflammatory linear verrucous epidermal nevus (ILVEN)** | Mosaic, various | Blaschko-linear narrow bands rather than diffuse lateralization; no ptychotropism; no limb reduction defect; no xanthomatous foam cells. A 2022 paper argues ILVEN "encompasses a spectrum of inflammatory mosaic disorders" (**PMID:35853659**), and a 2025 case reports unilateral ILVEN with ipsilateral limb contracture (**PMID:39953436**) — so this differential is harder than it looks |
| **Epidermal nevus / epidermal nevus syndromes** | *FGFR3*, *PIK3CA*, *HRAS*, *KRAS* mosaic | No xanthomatous histology, no cholesterol pathway abnormality, no ipsilateral hemidysplasia |
| **Nevus sebaceus / Schimmelpenning syndrome** | *HRAS*/*KRAS* mosaic | Sebaceous differentiation; cerebral anomalies, coloboma, conjunctival lipodermoid (**PMID:7640190**) |
| **Phacomatosis pigmentokeratotica** | *HRAS* mosaic | Combined organoid nevus + speckled lentiginous nevus |
| **Incontinentia pigmenti** | *IKBKG* | GeneReviews: "Cutaneous lesions evolve through multiple stages" — vesicular → verrucous → hyperpigmented → hypopigmented, along Blaschko lines |
| **Congenital ichthyosiform erythroderma (non-syndromic)** | *TGM1*, *ALOX12B*, *ALOXE3*, etc. | Generalized and bilateral; no lateralization, no limb defects |
| **Linear porokeratosis** | *MVK*, *PMVK*, *MVD*, *FDPS* (mevalonate pathway) | Cornoid lamella on histology. Note the reported **co-occurrence** of both diseases in one patient (**PMID:40464756**) |
| **Hailey-Hailey disease** | *ATP2C1* | A 2026 report documents CHILD syndrome mimicking Hailey-Hailey — a flexural-distribution trap (Wu/Cheng et al., *J Am Acad Dermatol.* 2026 Aug 10, **PMID:42575321**) |
| **Verrucous nevus / verrucous carcinoma** | — | **PMID:29341259** describes CHILD syndrome mimicking verrucous nevus; a 2024 German article is titled "[Only a wart?—Characteristic skin changes in CHILD syndrome]" (**PMID:39278872**) |
| **CK syndrome** | *NSDHL* (allelic!) | Males, ID + seizures + microcephaly + polymicrogyria, no lateralized nevus |
| **Greenberg dysplasia / dappled diaphyseal dysplasia** | *LBR* | Another sterol-pathway skeletal dysplasia (**PMID:32304187**) |

### Screening

- **Newborn screening:** **CHILD syndrome is not on any newborn screening panel.** The diagnosis is made clinically at birth from the skin lesion.
- **Carrier screening:** not applicable in the classical sense (heterozygous females are affected). Testing of a proband's mother is **cascade testing for affected-status determination**, not carrier screening.
- **Cascade testing:** appropriate for at-risk female relatives once a familial variant is known.
- **Prenatal testing:** "Once the NSDHL pathogenic variant has been identified in a family member with an NSDHL-related disorder, prenatal and preimplantation genetic testing are possible." (GeneReviews, **PMID:21290788**). Prenatal ultrasound may detect limb reduction defects.
- **Consider *NSDHL* testing in recurrent male pregnancy loss** — the actionable insight from **PMID:36504312**.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **Affected females:** normal or near-normal life expectancy when severe visceral malformations are absent. Multiple adult patients are reported at ages 14, 32, 33, and older (**PMID:40464756**, **PMID:16776722**, StatPearls, **PMID:39466221**).
- **Affected males:** **prenatal lethality is the rule** — "male conceptuses with an NSDHL pathogenic variant generally abort or resorb spontaneously" (GeneReviews, **PMID:21290788**); documented at 10+6 weeks' gestation (**PMID:36504312**). Surviving males are somatic mosaics.
- **Early mortality** in affected females occurs with severe cardiac or pulmonary malformation. StatPearls: cardiac disease is "potentially fatal in early weeks if severe."
- ⚠️ **No 5-year or 10-year survival figures, no mortality rate, and no disease-specific mortality data exist.** There is no registry, no SEER-equivalent, no GBD entry. Do not curate numeric survival statistics.

### Morbidity and function

- **Dermatologic:** chronic pruritus, scaling, malodor, secondary infection, disfigurement. Substantially modifiable with modern topical therapy.
- **Musculoskeletal:** the dominant long-term disability driver — contractures, immobility, poor dexterity, scoliosis. StatPearls lists these explicitly.
- **Neurologic:** hearing loss, visual impairment, and cognitive impairment in the minority with CNS involvement — StatPearls lists "hearing loss, blindness, cognitive impairment" among complications. But recall: "Intellect is usually normal."
- **Quality of life:** ⚠️ **No EQ-5D, SF-36, PROMIS, DLQI, or disease-specific instrument has been applied.** This is a real gap for a visibly disfiguring lifelong condition and is worth curating as a `KNOWLEDGE_GAP`.

### Disease course and complications

- **Squamous cell carcinoma** arising in a CHILD nevus — documented in a 33-year-old female (StatPearls, NBK507813). ⚠️ A **single case**; do not curate as an established cancer risk, but do note it as a surveillance rationale.
- **Secondary skin infection** from the eroded/macerated lesions.
- **Cardiac failure / reduced exercise tolerance** depending on severity.
- **Progressive scoliosis and contracture** without orthopedic management.
- **Gastrointestinal xanthomas** — a newly appreciated late/adult manifestation (**PMID:39466221**, **PMID:40517742**).

**Recovery potential:** skeletal malformations are permanent. **Skin lesions are now largely reversible with pathogenesis-based therapy** — the most important prognostic change of the last 15 years.

### Prognostic factors

- **Extent and severity of visceral (especially cardiac and pulmonary) involvement** — the dominant determinant of early survival.
- **Laterality:** "Left-sided involvement carries poorer prognosis due to higher visceral abnormality prevalence" (StatPearls). ⚠️ Review-level synthesis, no cohort backing.
- **Severity of limb reduction** — determines lifelong function.
- **CNS involvement** — determines cognitive/neurological outcome.
- **Age** — skin improves with time.
- **Access to pathogenesis-based topical therapy.**
- **Prognostic biomarkers:** ⚠️ **none identified.** Sterol levels are diagnostic, not prognostic. No molecular marker predicts disease course.

---

## 12. Treatment

### The headline: CHILD syndrome is a flagship success story for pathogenesis-based topical therapy

The core logic — supply the missing end product, and simultaneously shut down flux into the toxic intermediates — is what makes this treatment work, and it is why cholesterol alone fails.

> "Topical treatment with lovastatin/cholesterol (but not cholesterol alone) virtually cleared skin lesions by 3 months, accompanied by histological and ultrastructural normalization of epidermal structure and lipid secretion... These findings validate pathogenesis-based therapy that provides the deficient end product and prevents accumulation of toxic metabolites, an approach of potential utility for other syndromic lipid metabolic disorders."
> — Paller AS et al. *J Invest Dermatol.* 2011;131(11):2242-8. **PMID:21753784** (HUMAN_CLINICAL, n=2)

### Pharmacotherapy — topical (skin-directed)

| Therapy | Reported effect | Evidence |
|---|---|---|
| **Topical lovastatin 2% + cholesterol 2%** | "Complete healing in a few persons" (GeneReviews); "virtually cleared skin lesions by 3 months"; complete clearance in bilateral disease | **PMID:21753784** (n=2); **PMID:42083494** (n=1, bilateral); **PMID:40464756** (n=1, 4 weeks, no adverse events) |
| **Topical simvastatin 2% + cholesterol 2%** | "Remarkable improvement"; verruciform and VX-like lesions "improved obviously" | **PMID:29341259** (n=1); **PMID:42082353** (n=1) |
| **Topical simvastatin monotherapy** | "Pathogenesis-based therapy: Cutaneous abnormalities of CHILD syndrome successfully treated with topical simvastatin monotherapy" | Bajawi SM et al. *JAAD Case Rep.* 2018;4(3):232-234. **PMID:29687057** ⚠️ *title only — no abstract in PubMed* |
| **Topical simvastatin 5% ointment** | Reported effective in a 4-year-old | Acta Med Philipp 2024. **PMID:39431262** |
| **Topical ketoconazole 2%** | GeneReviews: "90% reduction of lesions after 10 days" (oral/topical ketoconazole) | GeneReviews **PMID:21290788**; "Improvement of Skin Lesions in an Adult with CHILD Syndrome Treated with 2% Ketoconazole Cream," Omi M et al. *Acta Derm Venereol.* 2024;104:adv41929. **PMID:39565229** ⚠️ *title only* |
| **Glycolic acid (added to statin/cholesterol)** | "Improved penetrance into thick skin scales" (GeneReviews) | **PMID:21290788** |
| **Topical tretinoin** | Localized benefit | StatPearls NBK507813 |
| **Lactic acid 12%** | "can reduce itching" | GeneReviews **PMID:21290788** |
| **Urea creams** | "can reduce dryness" | GeneReviews **PMID:21290788** |
| **Topical corticosteroids, emollients** | Adjunctive; "limited evidence" | StatPearls NBK507813 |

**Mechanism of each agent (for KB `target_mechanisms` curation):**
- **Cholesterol (topical)** — `ACTIVATES`/restores the deficient end product node ("Cholesterol Deficiency in Epidermis"). CHEBI:16113.
- **Lovastatin / simvastatin (topical)** — `INHIBITS` HMG-CoA reductase, cutting flux into the pathway and thereby the node "Toxic Methylsterol Intermediate Accumulation." CHEBI:40303 (lovastatin), CHEBI:9150 (simvastatin).
- **Ketoconazole** — `INHIBITS` CYP51A1 (lanosterol 14α-demethylase), blocking the pathway *upstream* of the NSDHL step and thus also reducing accumulation of C4-methylsterols. Mechanistic support: "Metabolic block upstream of SC4MOL with ketoconazole or CYP51A1 siRNA rescued cancer cell viability and EGFR degradation" (**PMID:23125191**). CHEBI:47519.

**⚠️ Critical curation note:** statin monotherapy and statin+cholesterol combination target *different* nodes and are not interchangeable. Paller's negative result — cholesterol alone was ineffective — is a `REFUTE`/`PARTIAL` evidence item worth curating explicitly, because it is what establishes the toxicity arm of the mechanism.

### Systemic pharmacotherapy

- **Systemic retinoids** — for widespread involvement (StatPearls). Long-term skeletal toxicity is a concern in a population that already has skeletal disease.
- **Oral ketoconazole** — GeneReviews mentions oral or topical; hepatotoxicity and drug-interaction burden argue against routine oral use now that topical works.
- **Oral/dietary cholesterol supplementation** — **not effective for skin** (barrier-compartment problem). Do not curate as a skin therapy.

### Pharmacogenomics

⚠️ **No pharmacogenomic data for CHILD syndrome.** No PharmGKB/CPIC guidance. Standard *CYP3A4*/*SLCO1B1* considerations for systemic statins are irrelevant at topical doses; ketoconazole is itself a potent CYP3A4 inhibitor, which is a **drug-interaction** consideration for oral use.

### Advanced therapeutics

- **Gene therapy:** ⚠️ none in development. Skin is theoretically an attractive gene-therapy target (cf. beremagene geperpavec for dystrophic EB), and the mosaic nature means only mutant clones need correction — but nothing is published.
- **Cell therapy:** the closest published analogue is **skin grafting**: "Treatment of an inflammatory nevus by grafting skin obtained from a contralateral unaffected region has been successful" (GeneReviews) — "Successful in 1 person." This is an elegant exploitation of the mosaicism: the contralateral side carries wild-type-expressing cells.
- **RNA-based therapies:** ⚠️ none. Splice-modulating ASOs could conceivably address splice-region variants like c.790-6C>T, but nothing exists.
- **Pharmacological chaperones — the most promising emerging direction.** The Fenton 2025 finding that glycerol and lower temperature rescue mutant NSDHL expression (**PMID:40222685**) is an explicit therapeutic lead: the authors state their findings "can help inform future treatments for CHILD and CK syndrome." IN_VITRO only.
- **Targeted therapies / immunotherapies:** not applicable.

### Surgical and interventional

- **Orthopedic surgery** — corrective surgery for limb deformity, contracture release, scoliosis correction. NCIT:C16186 Orthopedic Surgical Procedure.
- **Cardiac surgery** — for septal defects and complex cardiac anomalies. NCIT:C15329 Surgical Procedure.
- **Dermatologic surgery / skin grafting** — from contralateral unaffected skin (GeneReviews).
- **Bracing** — "Scoliosis and joint contractures are treated with braces and/or corrective surgery" (GeneReviews).

### Supportive and rehabilitative

- Emollients, keratolytics, itch control.
- Physical therapy (NCIT:C15302), occupational therapy, prosthetics/orthotics for limb deficiency.
- Rehabilitation (NCIT:C15315), supportive care (NCIT:C15747).
- Genetic counseling (NCIT:C15240) — essential given the 33/33/33 live-born recurrence distribution.
- **Multidisciplinary team** — StatPearls: "orthopedic surgeons for limb defects, pediatric cardiologists for cardiac abnormalities, neurologists for neurologic symptoms, dermatologists for skin disease."

### Experimental treatments / clinical trials

⚠️ **No clinical trials of any intervention for CHILD syndrome were identified.** All therapeutic evidence is from case reports and small series (n = 1–2). There is **no NCT identifier** to curate. This is expected for a disorder with fewer than 100 reported patients, but it means every treatment claim in this section rests on uncontrolled, unblinded, single-patient evidence with obvious publication bias toward successes.

### Treatment outcomes and adverse events

- **Response rates:** uniformly reported as good-to-complete for topical statin/cholesterol — but from a published-cases denominator that is certainly biased. GeneReviews' honest framing: **"In CHILD syndrome, no one therapy described to date appears to ameliorate the cutaneous findings for every reported individual."** (**PMID:21290788**)
- **Adverse events:** minimal reported. **PMID:40464756**: "we didn't observe any adverse events." Systemic absorption of topical statins over large body-surface areas in infants is a theoretical concern that has not been systematically studied. ⚠️ **No FAERS signal or systematic safety data exists for compounded topical statin/cholesterol in this population.**

### Treatment strategy / algorithm

There is no published guideline. The de facto algorithm from the literature:

1. **Confirm diagnosis** (clinical morphology → *NSDHL* sequencing + del/dup → sterol profiling if variant is a VUS).
2. **Comprehensive organ evaluation at diagnosis** — echo, renal US, chest imaging, skeletal survey (early, while stippling is visible), brain MRI, audiology, ophthalmology.
3. **Initiate topical pathogenesis-based therapy** — compounded 2% statin (lovastatin or simvastatin) + 2% cholesterol, twice daily; add glycolic acid for thick scale. Ketoconazole 2% cream is a reasonable alternative or adjunct.
4. **Symptomatic skin care** — 12% lactic acid for pruritus, urea for xerosis, emollients.
5. **Organ-specific management** by the relevant subspecialty.
6. **Orthopedic management** of contracture and scoliosis, with prosthetics/rehabilitation.
7. **Genetic counseling** for the family, including discussion of recurrent male miscarriage risk and prenatal/PGT options.
8. **Lifelong surveillance** (see below).

**Surveillance** (GeneReviews, **PMID:21290788**), annually or as needed:
- "Examine for new cutaneous manifestations; new lesions may occur in puberty or early adulthood"
- Clinical assessment for joint contractures and scoliosis
- Assessment for neurologic, cardiac, or kidney manifestations with imaging

**Personalized medicine:** the only genotype-guided consideration is *EBP*- vs *NSDHL*-related disease, and even that does not currently change therapy (both are downstream cholesterol-pathway blocks amenable to the same topical strategy). ⚠️ Note that a statin would *also* be mechanistically rational for *EBP*-related disease, but this has not been tested.

### NCIT term suggestions

| Treatment | `treatment_term` (NCIT) | `therapeutic_agent` (CHEBI, verified) |
|---|---|---|
| Topical lovastatin/cholesterol | NCIT:C15986 Pharmacotherapy | CHEBI:40303 lovastatin + CHEBI:16113 cholesterol |
| Topical simvastatin/cholesterol | NCIT:C15986 Pharmacotherapy | CHEBI:9150 simvastatin + CHEBI:16113 cholesterol |
| Topical ketoconazole | NCIT:C15986 Pharmacotherapy | CHEBI:47519 ketoconazole |
| Skin grafting from contralateral side | NCIT:C15329 Surgical Procedure | — |
| Orthopedic correction | NCIT:C16186 Orthopedic Surgical Procedure | — |
| Physical therapy | NCIT:C15302 Physical Therapy | — |
| Rehabilitation | NCIT:C15315 Rehabilitation | — |
| Supportive care / emollients | NCIT:C15747 Supportive Care | — |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — |

`therapeutic_modality` suggestions: `SMALL_MOLECULE` for all pharmacotherapy; `SURGERY` for grafting/orthopedic; `BEHAVIORAL` for physical/occupational therapy.

---

## 13. Prevention

### Prevention levels

- **Primary prevention:** **not possible.** The disease is a de novo or inherited germline event. There is no modifiable exposure, no vaccination, no behavioral intervention that reduces incidence. The only "primary prevention" available is **reproductive**: prenatal diagnosis or preimplantation genetic testing in families with a known *NSDHL* variant.
- **Secondary prevention (early detection + early treatment):** highly relevant and effective. The distinctive neonatal skin lesion makes early recognition realistic; StatPearls emphasizes that imaging "detect[s] skeletal and visceral anomalies, enabling early intervention," and that "Early detection and timely management improve patient outcomes substantially." Early initiation of topical pathogenesis-based therapy prevents years of morbidity.
- **Tertiary prevention (preventing complications):** the core of long-term care — orthopedic bracing/surgery to prevent fixed contracture and progressive scoliosis; emollients and prompt antimicrobial treatment to prevent secondary skin infection; annual surveillance for new lesions and for evolving cardiac/renal/neurologic manifestations (GeneReviews surveillance table, **PMID:21290788**).

### Immunization

**Not applicable** — no infectious etiology, no vaccine strategy. Routine childhood immunizations should proceed normally.

### Screening and early detection

- **Population/newborn screening:** **not performed and not recommended** — no biochemical marker suitable for dried-blood-spot screening (serum cholesterol is normal), and the phenotype is visible at birth anyway.
- **Genetic screening:**
  - **Cascade testing** of at-risk female relatives once a familial variant is identified.
  - **Prenatal testing** (CVS/amniocentesis) and **preimplantation genetic testing (PGT-M)** — both explicitly available per GeneReviews: "Once the NSDHL pathogenic variant has been identified in a family member with an NSDHL-related disorder, prenatal and preimplantation genetic testing are possible."
  - **Prenatal ultrasound** for limb reduction defects in at-risk pregnancies.
  - **Consider *NSDHL* testing in couples with recurrent male pregnancy loss** (**PMID:36504312**) — a genuinely new, actionable screening indication.
- **Risk stratification:** the only stratifier is maternal carrier status. Within an affected individual, the presence of cardiac/pulmonary anomalies stratifies early-mortality risk.

### Behavioral interventions

Not preventive of disease. Relevant only to symptom management: gentle skin care, avoidance of flexural maceration and friction, sun protection over affected skin (given the single reported SCC), and consistent emollient use.

### Counseling

**Genetic counseling is a core, non-optional component of care.** Key content:
- X-linked dominant, male-lethal inheritance.
- The 33% / 33% / 33% expected live-born distribution for a heterozygous mother.
- Male conceptuses with the variant "generally abort or resorb spontaneously" — so recurrent male miscarriage is expected and should be anticipated rather than treated as an unexplained obstetric problem.
- Possibility of somatic (and, theoretically, germline) mosaicism.
- Availability of prenatal testing and PGT-M.
- Highly variable expressivity means an affected daughter's severity cannot be predicted from the mother's.

*Source: GeneReviews NSDHL-Related Disorders, **PMID:21290788**.*

### Public health and environmental interventions

**Not applicable.** No sanitation, vector-control, health-education, or environmental-remediation measure is relevant.

### Prophylaxis

No preventive medication or procedure exists. The nearest analogue is **continuous maintenance topical therapy** to prevent lesion recurrence — but this is maintenance treatment, not prophylaxis.

---

## 14. Other Species / Natural Disease

### Taxonomy

- ***Mus musculus*** — **NCBITaxon:10090** — the only species with a well-characterized *Nsdhl* disease phenotype.
- ***Homo sapiens*** — NCBITaxon:9606.
- ***Saccharomyces cerevisiae*** — NCBITaxon:4932 — the *ERG26* ortholog, used for complementation assays (**PMID:21129721**).
- ***Arabidopsis thaliana*** — NCBITaxon:3702 — 3β-hydroxysteroid dehydrogenase/C4-decarboxylase orthologs are "essential for the pollen and embryonic development" (*Int J Mol Sci.* 2023 Oct 25. **PMID:37958553**), a striking demonstration of how deeply conserved the requirement for C4-demethylation is.

### Breed

**Not applicable** — no VBO-codable breed predisposition; no naturally occurring companion-animal or livestock form of this disease has been reported.

### Orthologous genes

- **Mouse *Nsdhl*** — UniProt Q9R1J0 (the ortholog UniProt uses as the evidence source for most human NSDHL functional annotations, `ECO:0000250` "by similarity"). NCBI Gene ID: ⚠️ not verified in this session.
- **Yeast *ERG26*** — functionally complements human NSDHL, established experimentally (**PMID:21129721**).
- **Arabidopsis 3βHSD/C4-decarboxylases** (**PMID:37958553**).

### Natural disease in other species

**The mouse mutants *bare patches* (Bpa) and *striated* (Str) are naturally arising (X-irradiation-induced) X-linked dominant male-lethal mutations that turned out to be allelic *Nsdhl* mutations** — and they were characterized *before* the human gene was found, then used to find it. This is one of the cleanest cases of a mouse mutant leading to a human disease gene.

> "The bare patches (Bpa) and striated (Str) mouse mutations were originally identified in female offspring of X-irradiated males... Here we report mutations in one of these genes, Nsdhl, encoding an NAD(P)H steroid dehydrogenase-like protein, in two independent Bpa and three independent Str alleles. Quantitative analysis of sterols from tissues of affected Bpa mice support a role for Nsdhl in cholesterol biosynthesis. Our results demonstrate that Bpa and Str are allelic mutations and identify the first mammalian locus associated with an X-linked dominant, male-lethal phenotype."
> — Liu XY, Dangel AW, Kelley RI, Zhao W, Denny P, Botcherby M, Cattanach B, Peters J, Hunsicker PR, Mallon AM, Strivens MA, Bate R, Miller W, Rhodes M, Brown SD, Herman GE. *Nat Genet.* 1999;22(2):182-7. **PMID:10369263** (MODEL_ORGANISM)

König et al. explicitly recognized their value: "Two mouse X-linked dominant male-lethal traits, bare patches (Bpa) and striated (Str) had previously been associated with mutations in Nsdhl. They provide animal models for the study of CHILD syndrome" (**PMID:10710235**).

**Veterinary relevance:** none. There is no naturally occurring *NSDHL* disease of veterinary importance; these are laboratory mutants.

### Comparative biology

- **Comparative pathology:** *Bpa/Str* heterozygous females recapitulate the core human features — patchy/striped skin lesions along Blaschko-equivalent lines from X-inactivation mosaicism, skeletal abnormalities, and male hemizygous lethality. Human CHILD's *diffuse* lateralization vs mouse *striping* likely reflects differences in the geometry of clonal expansion in the two species' skin.
- **Evolutionary conservation:** the C4-demethylation step is conserved from yeast (*ERG26*) through plants (Arabidopsis) to mammals, and the human enzyme functionally complements the yeast mutant (**PMID:21129721**) — strong evidence of deep conservation of both structure and function.

### Transmission

**Not applicable** — no zoonotic potential, no cross-species susceptibility. This is a heritable metabolic disorder.

---

## 15. Model Organisms

### Mouse — the workhorse

**Spontaneous/induced X-linked dominant male-lethal alleles:**

| Model | Type | Key features | Reference |
|---|---|---|---|
| ***bare patches* (Bpa)** — multiple independent alleles including **Bpa^1H^** | X-irradiation-induced point/structural mutations in *Nsdhl* | X-linked dominant, male-lethal; heterozygous females show patchy skin lesions, skeletal abnormalities, and mosaic NSDHL expression. Hemizygous males "die by midgestation" | **PMID:10369263**; **PMID:19631568**; **PMID:25652406** |
| ***striated* (Str)** — three independent alleles | Allelic to Bpa | Striped coat/skin phenotype from X-inactivation mosaicism | **PMID:10369263** |
| ***Nsdhl^tm1.1Hrm^*** — **conditional (floxed) allele** | Engineered, Cre-conditional | Built precisely because "hemizygous male mice with Nsdhl mutations die by midgestation"; crossed to *GFAP-cre* to ablate *Nsdhl* in radial glia | **PMID:25652406** |

**Phenotype recapitulation:**

*Strengths* —
- **Male lethality is faithfully reproduced** ("hemizygous male mice with Nsdhl mutations die by midgestation," **PMID:25652406**).
- **Mosaic skin phenotype from X-inactivation** is reproduced.
- **The negative-selection mechanism is reproduced and quantifiable** — Bpa^1H^/+ liver dropped from ~50% NSDHL-negative cells at P6 to ~20% at one year (**PMID:19631568**). This mouse result *predicted* and explains the human lateralization finding.
- **Sterol biochemistry is reproduced** — "Quantitative analysis of sterols from tissues of affected Bpa mice support a role for Nsdhl in cholesterol biosynthesis" (**PMID:10369263**).
- **Growth-factor-receptor trafficking defect is reproduced in vivo** — "Analysis of Nsdhl-deficient Bpa(1H/+) mice confirmed dramatic and selective loss of internalized platelet-derived growth factor receptor in fibroblasts, and reduced activation of EGFR and its effectors in regions of skin lacking NSDHL" (**PMID:23125191**).
- **Developmental expression mapping** — highest embryonic *Nsdhl* expression in "liver, dorsal root ganglia, central nervous system, retina, adrenal gland and testis" (**PMID:19631568**), which usefully predicts which human organs are at risk.

*Limitations* —
- **Skin lesion morphology differs**: mouse shows *striping/patches*; human shows *diffuse lateralization with strict midline demarcation* and *ptychotropism*. The most diagnostically characteristic human features are not reproduced.
- **The limb reduction defects** central to the human acronym are not the mouse model's dominant feature.
- **Hemizygous male embryonic lethality prevents study of the null state in vivo** without conditional alleles — the reason *Nsdhl^tm1.1Hrm^* was made.
- **The conditional CNS model is a CK-syndrome/neurodevelopmental model, not a CHILD model**: *GFAP-cre; Nsdhl^fl^* males "develop overt ataxia by postnatal day 8-10 and die shortly thereafter" (**PMID:25652406**) — informative about cholesterol in brain development, but not about the lateralized cutaneous disease.
- ⚠️ **Curate CNS phenotypes from this model with a `HUMAN_MODEL_MISMATCH` discussion**, since human CHILD syndrome usually has normal intellect.

### Yeast

***Saccharomyces cerevisiae* Erg26-deficient complementation assay** (IN_VITRO) — used as a functional readout for human *NSDHL* variants: the CK-syndrome alleles "show temperature-sensitive protein stability and complementation in Erg26-deficient yeast" (**PMID:21129721**). This is a validated functional assay for VUS resolution and is directly relevant to ACMG PS3-level evidence.

### Cell-based and in vitro systems

- **Patient-derived fibroblasts** — the standard system for sterol profiling and functional confirmation.
- **Heterologous expression systems for mutant NSDHL stability** — the 13-missense-variant survey with temperature and chemical-chaperone rescue (**PMID:40222685**).
- **Cerebellar granule cell precursor cultures** — used to demonstrate the SHH signaling defect and cholesterol rescue (**PMID:25652406**).
- **Cancer cell lines + A431 xenografts** — for the NSDHL/SC4MOL–EGFR trafficking work (**PMID:23125191**).
- **iPSC-derived and CRISPR-edited systems** — an area of **active development but limited CHILD-specific progress**. The 2026 review is the authoritative survey:
  > "This review provides a comprehensive overview of currently available experimental models used to investigate inherited cholesterol biosynthesis disorders, including genetically engineered animal models, patient-derived fibroblasts, immortalized and CRISPR/Cas9-edited cell lines, and induced pluripotent stem cell-based systems. Particular emphasis is placed on Smith-Lemli-Opitz syndrome, the most extensively studied disorder within this group, while recent advances in modeling desmosterolosis, lathosterolosis, and congenital hemidysplasia with ichthyosiform nevus and limb defects syndrome are also critically discussed."
  > — Akhmetzyanova E, Nasybullina E, Rizvanov A, Mukhamedshina Y. *Int J Mol Sci.* 2026;27(15):6853. **PMID:42589509**

  Note the framing: CHILD syndrome is explicitly the *less* well-modeled member of its disease class. **This is the single best citation for a knowledge-gap statement about CHILD syndrome modeling.**

### Not available

- **Zebrafish, Drosophila, C. elegans, rat** — ⚠️ no published *NSDHL*/CHILD model identified in any of these.
- **Organoids / organ-on-chip** — ⚠️ no skin organoid or epidermal-equivalent CHILD model published. Given that this is fundamentally an epidermal barrier disease with a topical therapy, a 3D human epidermal equivalent carrying an *NSDHL* knockout would be an obvious and currently missing tool.

### Model databases

- **MGI** (Mouse Genome Informatics) — *Nsdhl* alleles: `Bpa` series, `Str` series, `Nsdhl^tm1.1Hrm^`. ⚠️ Specific MGI allele accessions not retrieved in this session; look them up before curating identifiers.
- **IMPC / KOMP / IMSR / MMRRC / EMMA** — ⚠️ availability of *Nsdhl* lines not verified.
- **Alliance of Genome Resources** — for ortholog and phenotype integration.
- **SGD** — *ERG26*.

**Research applications the models support:** sterol biochemistry of the C4-demethylation block; X-inactivation mosaicism and clonal selection dynamics; SHH signaling dependence on cholesterol; EGFR/ERBB and PDGFR endocytic trafficking; testing of pharmacological chaperones; preclinical testing of topical pathogenesis-based formulations.

---

## Summary of Key Knowledge Gaps (for `discussions` / `KNOWLEDGE_GAP` curation)

1. **No reliable prevalence estimate.** The widely-repeated "1 in 100,000" figure is inconsistent with the ">60 reported individuals" case count and should not be curated as a rate.
2. **No natural-history study, registry, or longitudinal cohort.** All frequency figures are case-report-derived.
3. **No quality-of-life measurement of any kind** in a visibly disfiguring, lifelong condition.
4. **No clinical trial of any therapy.** All treatment evidence is n = 1–2 uncontrolled case reports with obvious positive-publication bias, and GeneReviews' own caveat stands: no therapy works for everyone.
5. **The right > left laterality bias (~2:1)** is reported but entirely unexplained mechanistically.
6. **The claim that left-sided disease has worse prognosis** is review-level synthesis without cohort support.
7. **No single-cell or spatial transcriptomics** — despite the disease being an almost ideal subject (sharp mosaic boundary, cell-autonomous selection).
8. **No skin organoid / epidermal-equivalent model**, despite the disease being an epidermal barrier disorder with a topical therapy.
9. **Systemic absorption and long-term safety of compounded topical statins** in neonates and infants over large body-surface areas is unstudied.
10. **The *EBP*- vs *NSDHL*-caused boundary of "CHILD syndrome"** remains nosologically unresolved (**PMID:10710233**) — a genuine lump/split question for the KB.
11. **Mild adult phenotypes (GI xanthomas, ichthyosis without limb defects)** are only just being recognized (**PMID:39466221**, **PMID:40517742**, **PMID:42082353**), implying substantial historical under-ascertainment and probable under-estimation of prevalence.
12. **ICD-10 and ICD-11 mappings could not be authoritatively verified** in this session.

---

## Sources

**Primary literature (PubMed):**
- [Happle R, Koch H, Lenz W. The CHILD syndrome. *Eur J Pediatr.* 1980. PMID:7408908](https://pubmed.ncbi.nlm.nih.gov/7408908/)
- [Happle R. Epidermal nevus syndromes. *Semin Dermatol.* 1995. PMID:7640190](https://pubmed.ncbi.nlm.nih.gov/7640190/)
- [Liu XY et al. The gene mutated in bare patches and striated mice encodes a novel 3beta-hydroxysteroid dehydrogenase. *Nat Genet.* 1999. PMID:10369263](https://pubmed.ncbi.nlm.nih.gov/10369263/)
- [König A et al. Mutations in the NSDHL gene... cause CHILD syndrome. *Am J Med Genet.* 2000. PMID:10710235](https://pubmed.ncbi.nlm.nih.gov/10710235/)
- [Grange DK et al. CHILD syndrome caused by deficiency of 3beta-hydroxysteroid-delta8,delta7-isomerase. *Am J Med Genet.* 2000. PMID:10710233](https://pubmed.ncbi.nlm.nih.gov/10710233/)
- [König A et al. A novel missense mutation of NSDHL in an unusual case of CHILD syndrome showing bilateral, almost symmetric involvement. *J Am Acad Dermatol.* 2002. PMID:11907515](https://pubmed.ncbi.nlm.nih.gov/11907515/)
- [Bornholdt D et al. Mutational spectrum of NSDHL in CHILD syndrome. *J Med Genet.* 2005. PMID:15689440](https://pubmed.ncbi.nlm.nih.gov/15689440/)
- [Ishibashi M et al. Abnormal lamellar granules in a case of CHILD syndrome. *J Cutan Pathol.* 2006. PMID:16776722](https://pubmed.ncbi.nlm.nih.gov/16776722/)
- [Cunningham D et al. Developmental expression pattern of the cholesterogenic enzyme NSDHL and negative selection of NSDHL-deficient cells in the heterozygous Bpa(1H)/+ mouse. *Mol Genet Metab.* 2009. PMID:19631568](https://pubmed.ncbi.nlm.nih.gov/19631568/)
- [McLarren KW et al. Hypomorphic temperature-sensitive alleles of NSDHL cause CK syndrome. *Am J Hum Genet.* 2010. PMID:21129721](https://pubmed.ncbi.nlm.nih.gov/21129721/)
- [Paller AS et al. Pathogenesis-based therapy reverses cutaneous abnormalities in an inherited disorder of distal cholesterol metabolism. *J Invest Dermatol.* 2011. PMID:21753784](https://pubmed.ncbi.nlm.nih.gov/21753784/)
- [Sukhanova A et al. Targeting C4-demethylating genes in the cholesterol pathway sensitizes cancer cells to EGF receptor inhibitors. *Cancer Discov.* 2013. PMID:23125191](https://pubmed.ncbi.nlm.nih.gov/23125191/)
- [Cunningham D et al. Analysis of hedgehog signaling in cerebellar granule cell precursors in a conditional Nsdhl allele. *Hum Mol Genet.* 2015. PMID:25652406](https://pubmed.ncbi.nlm.nih.gov/25652406/)
- [Yu X et al. CHILD syndrome mimicking verrucous nevus... simvastatin and cholesterol. *J Eur Acad Dermatol Venereol.* 2018. PMID:29341259](https://pubmed.ncbi.nlm.nih.gov/29341259/)
- [Bajawi SM et al. Pathogenesis-based therapy: ...topical simvastatin monotherapy. *JAAD Case Rep.* 2018. PMID:29687057](https://pubmed.ncbi.nlm.nih.gov/29687057/)
- [Maceda EBG et al. Novel NSDHL gene variant for CHILD syndrome. *BMJ Case Rep.* 2020. PMID:33139364](https://pubmed.ncbi.nlm.nih.gov/33139364/)
- [Zhuang J et al. Etiological identification of recurrent male fatality due to a novel NSDHL gene mutation. *Mol Genet Genomic Med.* 2023. PMID:36504312](https://pubmed.ncbi.nlm.nih.gov/36504312/)
- [Omi M et al. Improvement of Skin Lesions in an Adult with CHILD Syndrome Treated with 2% Ketoconazole Cream. *Acta Derm Venereol.* 2024. PMID:39565229](https://pubmed.ncbi.nlm.nih.gov/39565229/)
- [Kim DH et al. Gastrointestinal Xanthomas and Ichthyosis: A Mild Phenotype of CHILD Syndrome. *Am J Gastroenterol.* 2025. PMID:39466221](https://pubmed.ncbi.nlm.nih.gov/39466221/)
- [Fenton NM et al. Comprehensive survey of disease-causing missense mutations of NSDHL. *J Steroid Biochem Mol Biol.* 2025. PMID:40222685](https://pubmed.ncbi.nlm.nih.gov/40222685/)
- [Chen K et al. CHILD syndrome combined linear porokeratosis... topical lovastatin/cholesterol ointment. *J Dermatolog Treat.* 2025. PMID:40464756](https://pubmed.ncbi.nlm.nih.gov/40464756/)
- [Olarewaju BA et al. Colonic xanthomas in an adult... NSDHL haploinsufficiency. *Mol Genet Metab.* 2025. PMID:40517742](https://pubmed.ncbi.nlm.nih.gov/40517742/)
- [Vergara A et al. Diagnostic Utility of Optical Genome Mapping in X-Linked Dominant Genodermatoses. *Mol Syndromol.* 2025. PMID:41625319](https://pubmed.ncbi.nlm.nih.gov/41625319/)
- [Wyer J et al. CHILD Syndrome without Limb Defects in a 1-year-old: revised nomenclature. *Clin Exp Dermatol.* 2026. PMID:42082353](https://pubmed.ncbi.nlm.nih.gov/42082353/)
- [Zeyrek M et al. Bilateral Involvement in CHILD Syndrome Successfully Treated With Cholesterol-Lovastatin Combination. *Pediatr Dermatol.* 2026. PMID:42083494](https://pubmed.ncbi.nlm.nih.gov/42083494/)
- [Akhmetzyanova E et al. Modeling Inherited Disorders of Post-Lanosterol Cholesterol Biosynthesis. *Int J Mol Sci.* 2026. PMID:42589509](https://pubmed.ncbi.nlm.nih.gov/42589509/)

**Reference resources:**
- [GeneReviews®: NSDHL-Related Disorders (NBK51754), last update 5 Sep 2024. PMID:21290788](https://www.ncbi.nlm.nih.gov/books/NBK51754/)
- [StatPearls: CHILD Syndrome (NBK507813)](https://www.ncbi.nlm.nih.gov/books/NBK507813/)
- [OMIM #308050 — CHILD syndrome](https://omim.org/entry/308050) (⚠️ returned HTTP 403 to automated fetch; identifiers taken from MONDO/HPO cross-references)
- [HPO disease annotations for OMIM:308050](https://ontology.jax.org/api/network/annotation/OMIM:308050)
- [MONDO:0010621 via EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0010621)
- [Orphanet ORPHA:139](https://www.orpha.net/en/disease/detail/139) (definition via https://api.orphacode.org)
- [UniProt Q15738 — NSDHL / sterol-4-alpha-carboxylate 3-dehydrogenase](https://www.uniprot.org/uniprotkb/Q15738/entry)
- [HGNC:13398 — NSDHL](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13398)
- [ClinVar — NSDHL variants](https://www.ncbi.nlm.nih.gov/clinvar/?term=NSDHL%5Bgene%5D)
- [GTR test 317493 — NSDHL-Related Disorders](https://www.ncbi.nlm.nih.gov/gtr/tests/317493/)
- [FIRST — Foundation for Ichthyosis & Related Skin Types: CHILD Syndrome](https://www.firstskinfoundation.org/types-of-ichthyosis/child-syndrome)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 33 |
| Quoted claims found in source | 27 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:21290788`: "Onychodystrophy, onychorrhexis, and periungual hyperkeratosis are common"
  - closest text in source: "Onychodystrophy and periungual hyperkeratosis are common"
- `PMID:21290788`: "functions as a C4 demethylase in post-squalene cholesterol biosynthesis"
  - closest text in source: "Topical statin treatment alone or combined with cholesterol and/or glycolic acid can be beneficial"
- `PMID:21290788`: "new lesions may occur in puberty or early adulthood"
  - closest text in source: "The ichthyosiform skin lesions are usually present at birth or in the first weeks of life; new lesions can develop in later life"
- `PMID:21290788`: "mosaic for NSDHL pathogenic variant c.262C>T (p.Arg88Ter)"
  - closest text in source: "CK syndrome: If the mother of a proband is heterozygous for an NSDHL pathogenic variant, the expected chance of transmitting it in each pregnancy is 50%: males who inherit the pathogenic variant will be affected; females who inherit the pathogenic variant will be heterozygous and may have a range of behavioral problems"
- `PMID:35853659`: "encompasses a spectrum of inflammatory mosaic disorders"
  - closest text in source: "CONCLUSION: ILVEN is a clinical descriptor for a heterogenous group of mosaic inflammatory disorders"
- `PMID:37958553`: "essential for the pollen and embryonic development"
  - closest text in source: "Pollen-specific expression of HSD2 in the heterozygous hsd1 hsd2/+ mutant not only rescued the pollen lethality but also revealed the critical roles of the two HSD genes in embryogenesis"