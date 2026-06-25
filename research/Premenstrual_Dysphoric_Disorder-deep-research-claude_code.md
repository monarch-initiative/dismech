---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-24T17:41:12.406020'
end_time: '2026-06-24T17:45:03.025441'
duration_seconds: 230.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Premenstrual Dysphoric Disorder
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
  - claude-opus-4-8[1m]
  web_search_requests: 10
  num_turns: 12
  total_cost_usd: 1.8559045
  session_id: 74f5368d-3ca7-494e-b3e6-28eacadb9b19
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Premenstrual Dysphoric Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Premenstrual Dysphoric Disorder** covering all of the
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

# Comprehensive Research Report: Premenstrual Dysphoric Disorder (PMDD)

> **Curation note (per dismech anti-hallucination SOP):** This report is a research *lead document*, not a finished KB entry. PMIDs marked **[verified via search]** were confirmed during this session against PubMed/PMC. PMIDs marked **[verify before use]** are from my training knowledge and *must* be confirmed with `just fetch-reference PMID:XXXX` and snippet-checked before they enter any YAML. PMDD is a hormone-sensitive *mood* disorder — watch for **Named Entity Confusion** with plain "PMS" (premenstrual syndrome), which is a distinct, broader, milder entity.

---

## 1. Disease Information

**Overview.** Premenstrual dysphoric disorder (PMDD) is a severe, cyclical mood disorder defined by clinically significant affective and somatic symptoms that emerge in the **luteal phase** (roughly the week before menses), remit within a few days of bleeding onset, and are essentially absent in the follicular phase. It is best understood not as a hormone *excess* or *deficiency* state but as an **abnormal central nervous system sensitivity to normal cyclical ovarian-steroid fluctuation** — the symptoms are triggered by physiological progesterone/estradiol changes that are well tolerated by unaffected women. Think of it less like a thermostat set too high and more like a smoke detector wired to go off at the ordinary warmth of cooking dinner: the stimulus is normal, the alarm is not.

**Key identifiers:**
| Resource | ID |
|---|---|
| MONDO | **MONDO:0005905** (premenstrual dysphoric disorder) *[verify exact ID in local MONDO cache]* |
| DSM-5-TR | 625.4 (under Depressive Disorders) |
| ICD-11 | **GA34.41** (genitourinary chapter, cross-listed under depressive disorders **6E40** in some mappings) |
| ICD-10 | **N94.3** (premenstrual tension syndrome) / **F32.81** (US clinical PMDD code) |
| DOID | DOID:9881 *[verify]* |
| MeSH | D065446 "Premenstrual Dysphoric Disorder" |
| OMIM | None — not a Mendelian disorder (no single-gene OMIM entry) |
| Orphanet | Not a rare disease; not an ORPHA leaf |

**Synonyms / alternative names:** Late luteal phase dysphoric disorder (LLPDD — the DSM-III-R/DSM-IV appendix name); severe premenstrual syndrome; premenstrual dysphoria. **Distinguish from** premenstrual syndrome (PMS), a milder and more prevalent condition, and from premenstrual exacerbation (PME) of an underlying disorder.

**Data derivation:** Disease-level. PMDD is defined by **prospective daily symptom ratings** (DSM-5 requires ≥2 symptomatic cycles documented in real time), not by EHR diagnosis codes or biomarkers. Aggregated knowledge comes from cohort studies, RCTs, and the NIMH intramural hormone-manipulation program (Schmidt/Rubinow/Goldman).

Sources: [ICD-11 recognition – Asarina/Schroll 2022 AOGS](https://obgyn.onlinelibrary.wiley.com/doi/10.1111/aogs.14360); [Diagnostic validity revisited 2023 (PMC10711063)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10711063/)

---

## 2. Etiology

**Primary causal model.** PMDD is a **multifactorial, gene-by-hormone-by-environment** disorder. The unifying mechanistic insight comes from the landmark NIMH ovarian-suppression studies: when ovarian function is shut off with the GnRH agonist **leuprolide**, women with PMDD lose their symptoms; when estradiol or progesterone is then added back, symptoms recur — *while unaffected women show no mood change to identical manipulations*.

> "In women with premenstrual syndrome, the occurrence of symptoms represents an abnormal response to normal hormonal changes." — Schmidt PJ et al., *N Engl J Med* 1998 (**PMID: 9435325** [verified via search]).

A 2025 replication/extension confirmed the differential-sensitivity finding (PubMed 41030005 [verified via search]).

**Genetic risk factors:**
- **Heritability ~30–56%** for the stable trait component of premenstrual symptoms (Virginia/UK twin registries; Kendler et al. estimated ~56% for the stable component). [verified via search]
- **ESR1 (estrogen receptor alpha)** — four intron-4 SNPs differ between PMDD cases and controls; the association was strongest in carriers of the **COMT Val/Val** genotype (Huo L et al., *Biol Psychiatry* 2007, **PMID: 17599809** [verified via search]).
- **ESC/E(Z) (Extra Sex Combs / Enhancer of Zeste) epigenetic complex** — the strongest molecular lead. Lymphoblastoid cell lines from PMDD women show intrinsically dysregulated expression of >half of ESC/E(Z) genes, both untreated and in response to estradiol/progesterone (Dubey N et al., *Mol Psychiatry* 2017, **PMID: 28044059** [verified via search]).
- **BDNF Val66Met** — a humanized Met-knock-in mouse recapitulates PMDD-like anxiety/depression behavior on estradiol add-back (cross-species model, PMC7042769 [verified via search]).

**Environmental / non-genetic risk factors:** history of trauma/childhood adversity and PTSD; high perceived stress; current/past mood or anxiety disorder; smoking; high BMI; younger-to-mid reproductive age. Cyclical hormone exposure itself is the obligate trigger (PMDD does not occur in anovulatory states, pregnancy, or after menopause).

**Protective factors:** Anything that abolishes ovulatory cyclicity is mechanistically protective — pregnancy, lactational amenorrhea, menopause, continuous ovulation suppression (GnRH agonists, some COCs). No validated protective genetic allele is established.

**Gene–environment interaction:** The core model *is* a G×E interaction — heritable CNS steroid sensitivity (ESC/E(Z), ESR1, BDNF) × the normal cyclical hormonal "environment." Stress reactivity is amplified, plausibly via poor allopregnanolone–GABA control of the HPA axis.

---

## 3. Phenotypes (HPO suggestions)

PMDD is largely **behavioral/psychiatric**; HPO coverage is coarse. Core symptoms cluster as affective, then behavioral/cognitive, then somatic. All are **episodic/cyclical (luteal-phase-locked), recurrent, adult-onset, remitting at menses.**

| Phenotype | Category | Suggested HPO | Notes/frequency |
|---|---|---|---|
| Affective lability / mood swings | Behavioral | **HP:0000713 Behavioral abnormality** (no precise term) | Cardinal; required core symptom |
| Irritability / anger | Behavioral | **HP:0000737 Irritability** | Most distinguishing PMDD symptom |
| Depressed mood / hopelessness | Behavioral | **HP:0000716 Depression / Depressivity** | Common |
| Anxiety / tension / "on edge" | Behavioral | **HP:0000739 Anxiety** | Common |
| Anhedonia / decreased interest | Behavioral | **HP:0100750 Apathy / HP:0000716** | Frequent |
| Difficulty concentrating | Cognitive | **HP:0000752 Hyperactivity?** (poor fit) / use HP:0100543 Cognitive impairment cautiously | Frequent |
| Fatigue / lethargy / low energy | Constitutional | **HP:0012378 Fatigue** | Frequent |
| Appetite change / food cravings | Constitutional | **HP:0002591 Polyphagia** / HP:0004396 Poor appetite | Common |
| Hypersomnia or insomnia | Sleep | **HP:0002360 Sleep abnormality** | Common |
| Feeling overwhelmed / loss of control | Behavioral | HP:0000713 (no precise term) | Required-domain symptom |
| Breast tenderness | Somatic | **HP:0100650 Mastodynia?** (verify) | Physical symptom criterion |
| Bloating / weight-gain sensation | Somatic | **HP:0003270 Abdominal distention** | Physical symptom criterion |
| Joint/muscle pain, headache | Somatic | **HP:0002829 Arthralgia / HP:0002315 Headache** | Physical symptom criterion |
| Suicidal ideation (luteal) | Behavioral | **HP:0031589 Suicidal ideation** | Elevated risk; clinically critical |

**Severity:** moderate–severe by definition (must cause marked impairment in work, relationships, or functioning). **Frequency among affected:** ≥5 of 11 symptom domains required per cycle, with ≥1 from the core affective set. **QoL impact:** substantial — comparable functional impairment to major depression during the symptomatic window; elevated absenteeism, interpersonal conflict, and suicidality.

---

## 4. Genetic / Molecular Information

- **No causal Mendelian gene.** PMDD is polygenic/complex.
- **Top molecular lead — ESC/E(Z) epigenetic regulatory complex** (PRC2-related; includes EZH2, EED, SUZ12 and partners). Intrinsic transcriptional dysregulation in PMDD cells, differentially modulated by ovarian steroids (Dubey 2017, **PMID 28044059**). Subgenual cingulate rCBF correlates with ESC/E(Z) gene expression (Transl Psychiatry 2021, s41398-021-01328-4 [verified via search]).
- **ESR1** (estrogen receptor α; **HGNC:3467**) — intronic SNP associations (Huo 2007, **PMID 17599809**).
- **COMT Val158Met** (**HGNC:2228**) — modifies the ESR1 effect (Val/Val carriers).
- **BDNF Val66Met** (**HGNC:1033**) — model-organism epigenetic interaction with estradiol (PMC7042769).
- **GABA-A receptor subunits** — *functional/transcriptional*, not classic risk variants: lower **δ-subunit (GABRD)** mRNA in luteal phase, correlated with amygdala hyperactivity (search 2023/2025; Transl Psychiatry s41398-025-03465-6 [verified via search]).
- **Variant classification / allele frequencies / somatic vs germline:** Not applicable — these are common germline susceptibility polymorphisms, not pathogenic/ACMG-classified variants; no ClinVar pathogenic entries; no somatic/COSMIC component.
- **Epigenetics:** Central — ESC/E(Z) is a histone-methylation (chromatin) regulatory complex; steroid-responsive epigenetic reprogramming is the leading mechanistic frame.
- **Chromosomal abnormalities:** None.

---

## 5. Environmental Information

- **Environmental/toxic factors:** No established chemical toxicant cause. Smoking is associated with higher PMS/PMDD risk.
- **Lifestyle:** Stress, poor sleep, smoking, high BMI, alcohol associate with severity; exercise and some dietary factors (calcium) associate with milder symptoms (evidence modest).
- **Infectious agents:** **Not applicable** — PMDD is not infectious.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Heritable CNS steroid sensitivity** (ESC/E(Z) epigenetic dysregulation; ESR1/COMT/BDNF variants) sets an abnormal substrate. *[upstream trigger]*
2. **Normal luteal-phase rise then fall of progesterone**, and its neuroactive metabolite **allopregnanolone (ALLO; CHEBI:50169 — verify)**, a potent **positive allosteric modulator of the GABA-A receptor** (GO:1902476 chloride transmembrane transport; GABA-A is the major inhibitory ionotropic receptor).
3. **Dysregulated GABA-A receptor plasticity / sensitivity** to ALLO — paradoxical or blunted inhibitory response, partly via altered **δ-subunit (GABRD)** expression. The system fails to "tune" GABA-A as ALLO swings. *[core mechanism]*

   > PMDD reflects "dysregulated sensitivity to GABA-A receptor modulating neuroactive steroids across the menstrual cycle." — Hantsoo/Epperson-lineage reviews; Frontiers Psychiatry 2023 (**PMC10017536**, doi:10.3389/fpsyt.2023.1140796 [verified via search]).

4. **Impaired top-down emotional regulation:** luteal-phase **amygdala and insula hyperreactivity** to emotional/social stimuli with **reduced anterior cingulate / prefrontal control** (Gingnell et al. 2012, **PMID: 22814368** [verified via search]; recent fMRI systematic review, Frontiers 2026). δ-GABRD mRNA inversely tracks amygdala activation.
5. **HPA-axis stress dysregulation** from poor ALLO–GABA control → heightened stress sensitivity.
6. **Serotonergic involvement:** rapid SSRI efficacy (days, not weeks) suggests SSRIs act partly by **increasing ALLO synthesis (3α-HSD modulation)**, linking the serotonin and neurosteroid systems. *[downstream/therapeutic node]*
7. **Output:** luteal affective/cognitive/somatic symptoms → remission at menses as progesterone/ALLO fall.

**GO term suggestions:** GO:0007268 (chemical synaptic transmission), GO:1902711 (positive regulation of GABA-A receptor activity — verify), GO:0051384 (response to glucocorticoid), GO:0030518 (intracellular steroid hormone receptor signaling), GO:0006classnonsense — use GO:0043401 (steroid hormone mediated signaling). **CL terms:** CL:0000540 (neuron), CL:0000598 (pyramidal neuron), CL:0000617 (GABAergic neuron — verify), CL:0000125 (glial cell). **Cell types involved:** amygdalar/cortical pyramidal neurons and GABAergic interneurons; circulating monocytes used as accessible biomarker tissue.

**Molecular profiling:** RNA-seq of LCLs (ESC/E(Z), Dubey 2017); monocyte GABA-A subunit transcription (2025); steroid metabolome under GnRH suppression (Transl Psychiatry tp2017146 [verified via search]). No robust proteomic/metabolomic clinical signature yet beyond neurosteroid ratios (ALLO, isoallopregnanolone/ISO).

---

## 7. Anatomical Structures Affected

- **Organ/system:** Central nervous system (primary) and the hypothalamic-pituitary-ovarian + HPA axes (endocrine). PMDD is a **brain** disorder triggered by **ovarian** output.
- **UBERON terms:** **UBERON:0001876 amygdala**, **UBERON:0001870 frontal cortex** / **UBERON:0002756 cingulate cortex** (subgenual/ACC), **UBERON:0002021 insula** (verify), **UBERON:0001954 hippocampus/parahippocampal**, **UBERON:0001898 hypothalamus**, **UBERON:0000992 ovary** (trigger source).
- **Tissue/cell:** corticolimbic neurons (pyramidal + GABAergic interneurons).
- **Subcellular (GO CC):** GO:0034707 (chloride channel complex — GABA-A receptor), synaptic membrane (GO:0097060); steroid signaling in nucleus/cytoplasm.
- **Lateralization:** functional imaging often emphasizes **right amygdala**, but the disorder is bilateral/non-lateralized clinically.

---

## 8. Temporal Development

- **Onset:** reproductive years; typically **mid-20s to 30s**, often worsening with age toward perimenopause; requires ovulatory cycles.
- **Onset pattern:** chronic-recurrent with sharply **episodic, cycle-locked** flares.
- **Course:** **relapsing-remitting**, tied 1:1 to the menstrual cycle — symptoms in the late luteal phase, remission within a few days of menses, symptom-free follicular phase.
- **Duration:** persists across the reproductive lifespan unless treated or until ovulation ceases (pregnancy, menopause, suppression).
- **Critical periods / windows:** the **luteal phase** is the intervention window — enables *symptom-onset* or *luteal-only* SSRI dosing; **perimenopause** is a vulnerability window (erratic hormone swings); **menopause** is naturally curative.

---

## 9. Inheritance and Population

- **Prevalence:** meta-analytic pooled **~3.2%** for confirmed (prospectively diagnosed) PMDD and **~7.7%** for provisional diagnosis (J Affect Disord 2024, S0165032724000764 [verified via search]); commonly cited range **2–5%** (up to 8% with looser criteria) of reproductive-age women.
- **Incidence:** not well defined (cyclical disorder, not incident-event based).
- **Inheritance pattern:** **multifactorial / polygenic**; heritability ~30–56% for the stable trait (twin studies). No Mendelian pattern, penetrance, anticipation, founder effect, or carrier frequency applies.
- **Sex ratio:** essentially **exclusively in menstruating individuals** (people assigned female with ovulatory cycles); reproductive-age window.
- **Geographic distribution:** worldwide; prevalence estimates vary by criteria strictness (prospective vs retrospective) more than by geography.

---

## 10. Diagnostics

- **Gold standard:** **prospective daily symptom ratings over ≥2 consecutive cycles** — there is no diagnostic blood test, biomarker, or imaging study. The **Daily Record of Severity of Problems (DRSP)** (21 items, 11 domains) is the validated instrument; the **Carolina Premenstrual Assessment Scoring System (C-PASS)** operationalizes DSM-5 scoring (Eisenlohr-Moul TA et al., *Am J Psychiatry* 2017, **PMID: 27523500** [verified via search]).
- **DSM-5-TR criteria:** ≥5 symptoms in the final luteal week, ≥1 from the core set (marked affective lability, irritability/anger, depressed mood/hopelessness, anxiety/tension), with remission after menses, confirmed prospectively, causing significant impairment, not merely an exacerbation of another disorder (Epperson CN et al., *Am J Psychiatry* 2012;169(5):465–475, **PMID: ~22764360** [verify before use]).
- **ICD-11 (GA34.41):** ≥1 affective + ≥1 somatic/cognitive symptom, cyclically luteal, distressing, prospectively patterned.
- **Labs/imaging:** used only to **exclude** mimics (thyroid panel, CBC for anemia; no PMDD-specific value). Research-only: neurosteroid ratios (ALLO, ISO), fMRI amygdala reactivity.
- **Differential diagnosis (rule out via charting):** **premenstrual exacerbation (PME)** of major depression, bipolar disorder, generalized anxiety, or borderline personality (these persist through the follicular phase — the key discriminator); PMS (milder, fewer affective symptoms); thyroid disease; perimenopausal mood disorder.
- **Genetic/omics testing:** **not clinically indicated.**

---

## 11. Outcome / Prognosis

- **Mortality:** PMDD is **not directly lethal**, but luteal-phase **suicidality is markedly elevated** — a critical safety concern. No survival/5-year metrics apply.
- **Morbidity:** substantial functional disability during symptomatic windows — occupational impairment, relationship conflict, reduced QoL; cumulative burden across decades of cycles.
- **Course:** chronic-relapsing until reproductive cessation; tends to **worsen in perimenopause** and **resolve at menopause** or with definitive ovulation suppression.
- **Prognosis with treatment:** good — most patients respond to SSRIs and/or ovulation suppression. **Prognostic factors:** comorbid mood/anxiety disorders and trauma history predict worse course; clear cyclicity predicts good treatment response.

---

## 12. Treatment (MAXO/CHEBI suggestions)

**First-line — SSRIs** (rapid, often within days; can be **continuous, luteal-phase, or symptom-onset** dosing):
- Fluoxetine (**CHEBI:5118**), sertraline (**CHEBI:9123**), paroxetine (**CHEBI:7936** verify), escitalopram (**CHEBI:36791** verify). FDA-approved for PMDD: fluoxetine, sertraline, paroxetine CR.
- MAXO: **MAXO:0000058** (pharmacotherapy — verify; or NCIT:C15986 Pharmacotherapy); therapeutic_modality SMALL_MOLECULE.
- Evidence: intermittent (luteal) SSRIs effective (meta-analysis PMC10074750 [verified via search]); Cochrane SSRI review PMC11323276.

**First-line/second-line — combined oral contraceptives:** **drospirenone + ethinylestradiol 20 µg, 24/4 regimen** (e.g., YAZ) is FDA-approved and the best-evidenced COC, though placebo effect is large (Cochrane, Ma S 2023, CD006586.pub5 [verified via search]). **CHEBI:** drospirenone (CHEBI:50838 verify), ethinylestradiol (CHEBI:4903 verify).

**Adjunct/other:** SNRIs (venlafaxine); calcium supplementation; CBT/dialectical-behavior-informed therapy (MAXO behavioral therapy); lifestyle measures.

**Third-line / severe-refractory — ovulation suppression:** **GnRH agonists (leuprolide) with estradiol/progesterone add-back**; rarely **bilateral oophorectomy ± hysterectomy** as definitive surgical cure for refractory disease (MAXO surgical procedure MAXO:0000004).

**Investigational (mechanism-targeted neurosteroid therapies):**
- **Sepranolone (UC1010 / isoallopregnanolone, GABA-A modulating steroid antagonist)** — luteal-phase Phase IIb in PMDD (**NCT03697265** [verified via search], Asarina Pharma).
- **Ulipristal acetate** (selective progesterone receptor modulator) — studied for PMDD symptom suppression.
- Allopregnanolone/GABA-A–directed agents under translational development (Frontiers 2023, PMC10017536).

---

## 13. Prevention

- **Primary prevention:** none established (no way to prevent the underlying trait). Risk-factor modification (stress reduction, smoking cessation) may lower severity.
- **Secondary prevention:** early recognition via prospective charting; treat before functional/safety impact accrues.
- **Tertiary prevention:** suicidality risk management during luteal windows; ovulation suppression to prevent recurrent flares.
- **Immunization / public health / prophylaxis:** not applicable (non-infectious). **Genetic counseling/screening:** not indicated (polygenic, no actionable variant).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** human disorder (**NCBITaxon:9606**). No naturally occurring PMDD in other species (requires self-reported cyclical mood symptoms).
- **OMIA / veterinary:** not applicable.
- **Comparative biology:** ovarian-cycle neurosteroid–GABA-A signaling is **evolutionarily conserved** in rodents, which underpins the model systems below, but the *syndrome* is human.
- **Zoonotic:** not applicable.

---

## 15. Model Organisms

- **Mouse, induced hormonal models** — the workhorse. **GnRH-suppression + steroid add-back paradigms** and **progesterone-withdrawal models** reproduce ALLO/GABA-A δ-subunit plasticity and anxiety/depression-like behavior (MGI; in vivo).
- **BDNF Val66Met humanized knock-in mouse** — estradiol add-back induces PMDD-like anxiety/depression behavior in Met carriers, with parallel epigenetic changes (cross-species LCL↔mouse model, PMC7042769 [verified via search]). **evidence_source: MODEL_ORGANISM.**
- **Rat "liver-qi invasion" PMDD-irritability model** — used in GABA-A-Rα4 amygdala/hippocampus studies (PMC10008490 [verified via search]).
- **In vitro / human cells:** **lymphoblastoid cell lines (LCLs)** from PMDD patients vs controls — the ESC/E(Z) RNA-seq discovery platform (Dubey 2017, PMID 28044059). **evidence_source: IN_VITRO.** Circulating monocytes as accessible GABA-A-subunit readout.
- **Recapitulation/limitations:** rodent models capture the **neurosteroid–GABA-A** mechanism and behavioral output well but **cannot model the subjective affective/cognitive criteria**; LCLs/monocytes are peripheral surrogates for inaccessible brain tissue — flag as **HUMAN_MODEL_MISMATCH** where translational validity is the open question.

---

## Key Citations (verify all PMIDs with `just fetch-reference` before YAML use)

| Claim | Citation | PMID | Status |
|---|---|---|---|
| Abnormal response to normal hormone changes | Schmidt PJ et al., *NEJM* 1998 | **9435325** | verified via search |
| ESC/E(Z) epigenetic dysregulation | Dubey N et al., *Mol Psychiatry* 2017 | **28044059** | verified via search |
| ESR1 association | Huo L et al., *Biol Psychiatry* 2007 | **17599809** | verified via search |
| C-PASS diagnostic system | Eisenlohr-Moul TA et al., *Am J Psychiatry* 2017 | **27523500** | verified via search |
| Amygdala reactivity across cycle | Gingnell M et al. 2012 | **22814368** | verified via search |
| DSM-5 new category rationale | Epperson CN et al., *Am J Psychiatry* 2012 | ~22764360 | **verify** |
| Differential-sensitivity replication | (2025 NIMH replication) | 41030005 | verified via search |
| Prevalence meta-analysis | *J Affect Disord* 2024 | (PMC via S0165032724000764) | verified via search |
| ALLO–GABA-A pathogenesis review | Frontiers Psychiatry 2023 | PMC10017536 | verified via search |

**Sources:**
- [Schmidt 1998 NEJM – differential behavioral effects](https://www.nejm.org/doi/full/10.1056/NEJM199801223380401)
- [Dubey 2017 ESC/E(Z) – PMC5495630](https://pmc.ncbi.nlm.nih.gov/articles/PMC5495630/) | [NIMH summary](https://www.nimh.nih.gov/news/science-updates/2017/sex-hormone-sensitive-gene-complex-linked-to-premenstrual-mood-disorder)
- [Huo 2007 ESR1 – PubMed 17599809](https://pubmed.ncbi.nlm.nih.gov/17599809/)
- [Eisenlohr-Moul 2017 C-PASS – PubMed 27523500](https://pubmed.ncbi.nlm.nih.gov/27523500/) | [C-PASS PMC5205545](https://pmc.ncbi.nlm.nih.gov/articles/PMC5205545/)
- [Gingnell 2012 amygdala – PubMed 22814368](https://pubmed.ncbi.nlm.nih.gov/22814368/)
- [ALLO–GABA-A review 2023 – PMC10017536](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017536/) | [GABA-A dysregulated sensitivity – ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352289520300035)
- [Prevalence meta-analysis 2024 – ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0165032724000764)
- [Diagnostic validity revisited 2023 – PMC10711063](https://pmc.ncbi.nlm.nih.gov/articles/PMC10711063/)
- [From Genes to GABA review – PMC10176022](https://pmc.ncbi.nlm.nih.gov/articles/PMC10176022/)
- [Cochrane drospirenone 2023 – CD006586.pub5](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD006586.pub5/full)
- [Intermittent SSRI meta-analysis – PMC10074750](https://pmc.ncbi.nlm.nih.gov/articles/PMC10074750/)
- [Sepranolone trial – NCT03697265](https://clinicaltrials.gov/study/NCT03697265)
- [BDNF Val66Met cross-species model – PMC7042769](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7042769/)
- [GABA-A monocyte transcription 2025 – Transl Psychiatry](https://www.nature.com/articles/s41398-025-03465-6)
- [Steroid metabolome under GnRH suppression – tp2017146](https://www.nature.com/articles/tp2017146)
- [ICD-11 recognition – Schroll 2022 AOGS](https://obgyn.onlinelibrary.wiley.com/doi/10.1111/aogs.14360)

---

### Quick orientation for the curator
sup — the one-sentence version of this whole thing: **PMDD isn't "too much hormone," it's a brain that reads a perfectly normal hormone tide as a threat.** The single most important framing for the dismech pathophysiology causal chain is the Schmidt leuprolide experiment (PMID 9435325) → **differential CNS sensitivity** → **ESC/E(Z) epigenetic setpoint** (PMID 28044059) → **ALLO/GABA-A receptor plasticity failure** → **corticolimbic dysregulation (amygdala↑, ACC↓)** → luteal symptoms that vanish at menses. Two big landmines I'd flag before you commit YAML: (1) keep PMDD cleanly separated from plain **PMS** and from **PME** (premenstrual exacerbation) — that's the classic Named-Entity-Confusion trap here; and (2) several of my CHEBI/HPO/GO IDs above are "best guess, verify" — run `just validate-terms-file` on them, because the affective symptoms genuinely don't have crisp HPO homes and it's easy to grab a term that doesn't exist.

I have one PMID I couldn't fully nail down this session — the Epperson 2012 DSM-5 paper (I'm ~confident it's 22764360 but didn't see it printed in results), so `just fetch-reference` that one specifically before it goes in.