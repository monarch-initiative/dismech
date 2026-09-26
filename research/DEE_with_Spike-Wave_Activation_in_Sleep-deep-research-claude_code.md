---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-05T13:42:01.321324'
end_time: '2026-08-05T13:56:11.237445'
duration_seconds: 849.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Developmental and Epileptic Encephalopathy with Spike-Wave Activation
    in Sleep
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
  - claude-opus-5[1m]
  web_search_requests: 17
  num_turns: 52
  total_cost_usd: 4.685067999999999
  session_id: 0a44c86d-6e30-445f-80f2-bbc2a1bd47e3
  stop_reason: end_turn
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental and Epileptic Encephalopathy with Spike-Wave Activation in Sleep
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy with Spike-Wave Activation in Sleep** covering all of the
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

sup Harry — dug through the ILAE nosology, the 2024 Ann Neurol etiology cohort, the RESCUE ESES trial, and a pile of mechanism papers. Report's below. One housekeeping note up front: quotes marked **[verbatim-verified]** were read out of full cached abstract text (or `references_cache/`), so they're safe to drop into an evidence `snippet:`. Quotes marked **[reported]** came back through a page-fetch summarizer and should be re-fetched with `just fetch-reference` before you commit them — the repo's whole anti-hallucination stance says don't trust a middleman for an exact string.

---

# Developmental and/or Epileptic Encephalopathy with Spike-Wave Activation in Sleep (D/EE-SWAS)

**Research report for dismech KB entry** · compiled 2026-08-05

---

## 1. Disease Information

### What it is

DEE-SWAS is one of those syndromes that's really a *state* the brain slides into rather than a single disease. A kid — usually somewhere between 2 and 12, peaking around 4–5 — starts having seizures, and then, a year or two later, starts *losing ground*: language, attention, behavior, sometimes motor skills. The tell is on the overnight EEG: during non-REM sleep, spike-and-wave discharges bloom until they occupy most of the tracing. Wakefulness looks comparatively tame. Sleep is where the damage happens.

The ILAE's 2022 nosology (Specchio et al., PMID:35503717) folded a whole graveyard of older names into this single umbrella. The formal definition: *"a spectrum of conditions with varied degree of cognitive, language, behavioral, and motor regression associated with marked spike-wave activation in sleep"* **[reported — epilepsydiagnosis.org syndrome page]**.

The split between the two halves is purely developmental history:
- **EE-SWAS** — development was **normal** before the regression. The epileptic activity is doing all the harm.
- **DEE-SWAS** — there was **pre-existing** developmental impairment, and then regression on top. Two encephalopathies stacked.

Think of it like a fever in a healthy adult versus a fever in someone already immunosuppressed — same insult, very different baseline, very different ending.

**Landau-Kleffner syndrome (LKS)** was retained as a clinically distinct EE-SWAS subtype: the variant where the regression is essentially *all* language — acquired auditory verbal agnosia in a previously normal child, ages ~3–9.

### Identifiers

| Resource | ID | Notes |
|---|---|---|
| **MONDO** | **MONDO:0800501** | `developmental and/or epileptic encephalopathy with spike-wave activation in sleep` — **verified via local `sqlite:obo:mondo`**. Parents: `MONDO:0002254` (syndromic disease), `MONDO:0800500` (childhood-onset epilepsy syndrome with DEE) |
| Orphanet | **ORPHA:725** | "Developmental and epileptic encephalopathy with spike-wave activation in sleep" |
| GARD | GARD:0027304 | from MONDO xref |
| MedGen | MEDGEN:1790601 | from MONDO xref |
| UMLS | UMLS:C5552731 | from MONDO xref |
| ICD-11 | **8A62.Y** | "Other specified epileptic encephalopathies" (per Orphanet mapping) — *no dedicated ICD-11 stem code exists* |
| ICD-10 | G40.8 (likely) | ⚠️ not independently verified; check Orphanet before curating |
| MeSH | **D018887** | Landau-Kleffner Syndrome (MeSH UID 68018887, verified via E-utilities). **No dedicated MeSH descriptor exists for CSWS/DEE-SWAS itself** |
| OMIM | **#245570** | `EPILEPSY, FOCAL, WITH SPEECH DISORDER AND WITH OR WITHOUT IMPAIRED INTELLECTUAL DEVELOPMENT (FESD)` — the *GRIN2A* phenotype entry, which explicitly encompasses LKS, ECSWS/CSWSS, ADRESD and BECTS. **There is no OMIM entry for the syndrome as an etiologically agnostic entity** |
| OMIM (gene) | *GRIN2A* = 138253 | |

### Synonyms (all from the MONDO synonym block, verified)

CSWS · CSWSS syndrome · DEE-SWAS · EE-SWAS · EESWAS · ESES · electrical status epilepticus of sleep · electrographic status epilepticus in sleep · continuous spike-wave in sleep · continuous spikes and waves during sleep · continuous spikes and waves during slow-wave sleep · continuous slow spike and wave of sleep · epileptic encephalopathy with continuous spike-and-wave during slow sleep (EE-CSWS) · epileptic encephalopathy with spike-and-wave activation in sleep · ESES with language regression · epileptic aphasia · Landau-Kleffner syndrome / LKS / LK syndrome. Also retired but still in the literature: **atypical benign partial epilepsy (ABPE)**, **pseudo-Lennox syndrome**, **Penelope syndrome**.

### Data provenance

Everything below is **disease-level aggregated** — case series, tertiary-center cohorts, systematic reviews, one small RCT. There is no EHR-derived phenotype library for this syndrome, and the OMOP/ICD coding is so coarse (8A62.Y "other specified") that EHR case-finding would be near-useless without EEG-report NLP. Worth flagging as a `KNOWLEDGE_GAP` if you're curating `definitions`.

---

## 2. Etiology

### The big picture: heterogeneous as hell, and half of it stays unsolved

The best-powered modern etiology study is **Viswanathan et al., Ann Neurol 2024 (PMID:39096015)** — 91-patient Core cohort, all meeting ILAE D/EE-SWAS criteria.

> "We identified the etiology in 42/91 (46%) patients in our Core cohort, including 29/44 (66%) with DEE-SWAS and 13/47 (28%) with EE-SWAS. A genetic etiology was identified in 31/91 (34%)." **[verbatim-verified from `references_cache/PMID_39096015.md`]**

> "D/EE-SWAS genes were highly co-expressed in brain, highlighting the importance of channelopathies and transcriptional regulators. Structural etiologies were found in 12/91 (13%) individuals." **[verbatim-verified]**

That 66% vs 28% gap is the single most curation-relevant number in the whole literature: **DEE-SWAS (pre-existing impairment) is more than twice as likely to have a findable cause as EE-SWAS.** Makes intuitive sense — an already-abnormal brain usually got that way for a reason you can find.

Breakdown from the same cohort:
- **Genetic:** 31/91 (34%) — 23 single-gene variants, 6 CNVs, 1 chromosomal abnormality **[reported]**
- **Structural:** 12/91 (13%) — polymicrogyria ×5, thalamic lesions ×5, post-hemorrhagic hydrocephalus ×2 **[reported]**
- **Unsolved:** 49/91 (54%)

Older tertiary-center series put the structural fraction much higher (~45–59%, with perinatal vascular lesions 21–78% and cortical malformations ~25%) **[reported, PMC3929187]** — the discrepancy is almost certainly ascertainment: an epilepsy-genetics research program enriches for undiagnosed kids, a general pediatric neurology clinic enriches for kids with obvious perinatal brain injury.

### Causal factor classes

**(a) Structural — early thalamic injury is the standout.**

This one is mechanistically load-bearing, not just a bucket. From **Sánchez Fernández / Leal et al., Epilepsy Behav 2018 (PMID:29133062)**:

> "Early neonatal thalamic lesions account for about 14% of continuous spike-wave of sleep (CSWS) syndrome, representing the most common etiology in this epileptic encephalopathy in children, and promise useful insights into the pathophysiology of the disease." **[verbatim-verified from cache]**

Other structural causes: polymicrogyria (especially unilateral perisylvian), periventricular leukomalacia and other perinatal vascular insults, post-hemorrhagic hydrocephalus, porencephaly, hemimegalencephaly, cortical dysplasia, and — importantly — **shunted hydrocephalus**.

**(b) Genetic.** See §4 for the gene-by-gene detail. Headline: *GRIN2A* is the single most frequent gene; the two functional classes that dominate are **ion channels/receptors** and **transcriptional regulators**.

**(c) Iatrogenic / drug-provoked — an under-appreciated and *modifiable* cause.**

Sodium-channel-blocking and GABAergic ASMs can *precipitate* SWAS in a child with self-limited focal epilepsy who would otherwise have coasted to remission. Carbamazepine, oxcarbazepine, phenytoin and phenobarbital are all implicated (e.g. **PMID:26415787**, oxcarbazepine-induced ESES in idiopathic childhood focal epilepsy). Practically: *"Carbamazepine is relatively contraindicated in ESES and should be discontinued"* **[reported, StatPearls NBK553167]**. This deserves its own pathophysiology node — it's one of the few genuinely preventable routes into the syndrome.

**(d) Unknown / presumed developmental.** Over half. Age-dependency (onset window 2–12, remission around puberty) strongly implies the causal factor isn't the lesion or variant alone but its *interaction with a developmental window* — the same lesion in an adult brain doesn't do this.

### Risk factors

**Genetic risk:**
- Pathogenic/likely pathogenic variants in the genes in §4 (causal, not merely susceptibility, in solved cases)
- Being a **male** carrier of an X-linked *CNKSR2* variant (hemizygous males affected; most carrier mothers neurologically unremarkable **[reported]**)
- Underlying self-limited epilepsy with centrotemporal spikes (SeLECTS) — sits on the same **epilepsy-aphasia spectrum** as DEE-SWAS; *GRIN2A* detection rate climbs from ~4.9% in BECTS/SeLECTS to ~17.6% in CSWS **[reported, Lemke et al. Nat Genet 2013]**
- Incomplete penetrance and intrafamilial variability documented even for the *same* GRIN2A variant **[reported, OMIM #245570]**

**Environmental / acquired risk:**
- Neonatal thalamic hemorrhage or infarction (often associated with neonatal sinovenous thrombosis)
- Perinatal hypoxic-ischemic injury, prematurity, periventricular leukomalacia
- Intraventricular hemorrhage → post-hemorrhagic hydrocephalus → shunt
- Exposure to carbamazepine/oxcarbazepine/phenytoin/phenobarbital in a child with focal childhood epilepsy
- **Age 2–12** is itself the dominant risk factor — this is a developmental-window disease
- **Sex:** mild male excess (~60:40) **[reported, PMC3929187]**; the Ann Neurol cohort was 53% male **[reported]**. Not a strong signal except in X-linked *CNKSR2* families.

**Protective factors:** Honestly, nothing established. No protective allele, no dietary or lifestyle factor with evidence. The nearest thing to a protective factor is **early recognition and early spike-suppressing treatment** (see §12) plus **avoiding the aggravating ASMs**. Worth curating explicitly as absent rather than leaving the section blank.

**Gene–environment interaction:** The clearest one is *pharmacogenetic-ish* rather than classical GxE: a child with a *GRIN2A* variant and a SeLECTS phenotype who gets started on carbamazepine may be tipped into full SWAS. Also: a genetic background (e.g. channelopathy) plus a structural thalamic hit appears additive in some series. No formal GxE study exists — flag as a gap.

---

## 3. Phenotypes

### The two-act structure

**Act I (age ~2–7):** seizures appear, often nocturnal, often unimpressive. Up to 80% of children present with seizures as the first symptom **[reported]**, and about 80% have only one seizure type at onset **[reported]**. Roughly 20% present the other way round — cognitive/behavioral change first, seizures later or never prominent **[reported]**.

**Act II (~1–2 years later):** SWAS establishes on the sleep EEG, seizure frequency often jumps (up to 70% have multiple daily seizures once ESES appears **[reported]**), and the regression begins. This is the encephalopathy proper.

### Phenotype table with HPO suggestions

All HP IDs below **verified against `sqlite:obo:hp` via OAK**.

| Phenotype | HPO term | Category | Onset | Course | Frequency |
|---|---|---|---|---|---|
| Developmental regression (the defining feature) | **HP:0002376** Developmental regression | Neurologic / behavioral | ~1–2 yr after seizure onset; median 5–6 yr | Subacute then plateau; partial recovery after SWAS remits | Obligate (100% by definition) |
| Seizure | **HP:0001250** Seizure | Neurologic | 2–12 yr, peak 4–5 | Episodic; remits at puberty | ~80–90% (a minority are seizure-free) |
| Focal-onset seizure | **HP:0007359** | Neurologic | as above | episodic | Very frequent |
| Focal motor seizure (often unilateral clonic, nocturnal) | **HP:0011153** | Neurologic | as above | episodic | Frequent |
| Bilateral tonic-clonic seizure | **HP:0002069** | Neurologic | as above | episodic | Frequent |
| Generalized non-motor (absence) seizure — "atypical absence" | **HP:0002121** | Neurologic | after SWAS onset | episodic, often many/day | Frequent |
| Atonic seizure / epileptic negative myoclonus (drop attacks, head nods) | **HP:0010819** | Neurologic | after SWAS onset | episodic | Occasional–frequent |
| Myoclonic seizure | **HP:0032794** | Neurologic | variable | episodic | Occasional |
| Epileptic encephalopathy | **HP:0200134** | Neurologic | — | — | Obligate |
| EEG abnormality | **HP:0002353** | Lab / electrophysiology | at SWAS onset | — | Obligate |
| Interictal epileptiform activity | **HP:0011182** | Lab | — | markedly sleep-activated | Obligate |
| Multifocal epileptiform discharges | **HP:0010841** | Lab | — | — | Frequent |
| Intellectual disability | **HP:0001249** | Cognitive | after regression | often persists | **DEE-SWAS 49% moderate-severe; EE-SWAS 8%** [reported] |
| Global developmental delay | **HP:0001263** | Cognitive | *pre-dates* regression in DEE-SWAS | — | Defining for DEE-SWAS arm |
| Delayed speech and language development | **HP:0000750** | Language | — | — | Very frequent |
| Aphasia (acquired — the LKS core) | **HP:0002381** | Language | 3–9 yr in LKS | subacute or fluctuating | Obligate in LKS subtype |
| Receptive language delay / auditory verbal agnosia | **HP:0010863** | Language | 3–9 yr | — | Obligate in LKS |
| Poor speech / mutism | **HP:0002465** | Language | — | may progress to complete mutism | Frequent in LKS |
| ADHD | **HP:0007018** | Behavioral | with/before regression | often persists | Very frequent |
| Hyperactivity | **HP:0000752** | Behavioral | — | — | Very frequent |
| Autistic behavior | **HP:0000729** | Behavioral | may be the regression phenotype | — | Occasional |
| Autism | **HP:0000717** | Behavioral | — | — | Occasional |
| Specific learning disability | **HP:0001328** | Cognitive | — | persists | Frequent |
| Ataxia | **HP:0001251** | Motor | with SWAS | improves with remission | Occasional |
| Dysarthria | **HP:0001260** | Motor speech | — | — | Occasional |
| Hemiparesis | **HP:0001269** | Motor | pre-existing in structural cases | static | Occasional (structural etiologies) |
| Status epilepticus | **HP:0002133** | Neurologic | — | — | Occasional |
| Polymicrogyria | **HP:0002126** | Structural (imaging) | congenital | static | ~5/91 in solved structural cases |
| Hydrocephalus | **HP:0000238** | Structural | perinatal | static | ~2/91 |

⚠️ **Frequency-band caution (per `docs/frequency-evidence-guidelines.md`):** most of the percentages above are single-cohort tertiary-center figures, not pooled. I would only assign a `frequency:` enum to *Developmental regression* (definitional, obligate) and the EEG features. For the rest, omit the band rather than manufacture support.

### The regression is not one thing

Worth splitting into nodes if you're curating carefully. Per the ILAE description, *"All cognitive domains are affected including language and communication, temporo-spatial orientation, attention and social interaction"* **[reported]**. The domain hit tracks the **anatomy of the spike focus**:
- **Perisylvian/temporal focus → LKS phenotype** (auditory verbal agnosia, aphasia)
- **Frontal focus → CSWS phenotype** (dysexecutive/frontal syndrome, behavioral disinhibition, global cognitive drop)

From **Issa NP, Pediatr Neurol 2014 (PMID:25160535)**:

> "Several pediatric seizure disorders have common electrophysiological features during slow-wave sleep that produce different syndromes based on which part of the developing brain is involved." **[verbatim-verified from cache]**

That sentence is a good anchor for a "topography determines phenotype" pathophysiology node.

### Quality of life

No EQ-5D/PROMIS/SF-36 data specific to D/EE-SWAS that I could find — a genuine gap. Qualitatively: the burden is dominated by (1) permanent language/cognitive deficit rather than seizures, since seizures usually remit; (2) behavioral dysregulation and ADHD, which drive school placement and family stress; (3) in LKS, the profound communication loss — a child who could speak in sentences and now cannot understand speech at all. Caregiver burden is high across the active phase (typically 2–5+ years). **Flag as `KNOWLEDGE_GAP`: no validated disease-specific QoL instrument.**

---

## 4. Genetic / Molecular Information

### Causal genes

**The flagship: *GRIN2A*** (HGNC:4585; OMIM 138253; 16p13.2; GluN2A subunit of the NMDA receptor).

- Lemke et al., Nat Genet 2013: *"Heterozygous mutations in GRIN2A were detected in 27 of 359 affected individuals from independent cohorts with IFE (7.5%), with mutation detection rates ranging from 4.9% in individuals with BECTS to 17.6% in individuals with CSWS."* **[reported]**
- In the Ann Neurol 2024 cohort, *GRIN2A* was the most common single gene (~23% of genetic cases) **[reported]**
- *GRIN2A* accounts for ~9–20% of epilepsy-aphasia syndromes overall **[reported]**

**Functional consequence predicts phenotype** — this is the therapeutically actionable bit. Strehlow et al., Brain 2019 (**PMID:30544257**):

> "Null variants and mis_ATD+LBD_ of GRIN2A share the same clinical spectrum (milder phenotypes), but also result in similar electrophysiological consequences (loss-of-function) opposing those of mis_TMD+Linker_ (severe phenotypes; predominantly gain-of-function)." **[reported]**

> "Individuals with developmental and epileptic encephalopathy due to misTMD+Linker are prone to having an underlying gain of NMDAR function and represent promising candidates for treatment with NMDAR blockers, such as memantine." **[reported]**

So: **null / ATD+LBD missense → loss of function → milder, epilepsy-aphasia-spectrum end; TMD+Linker missense → gain of function → severe DEE end.** Domain-level annotation, not just "pathogenic," is what determines whether memantine (block) or a positive allosteric modulator is the rational move.

**The other established genes.** From the Ann Neurol 2024 cohort (previously known): *CNKSR2, SCN2A, ARID1B, CUL4B, GRIN2B, KCNH5, MECP2, SCN1A* **[reported]**.

**Ten novel D/EE-SWAS genes** from the same study, verbatim from the abstract:

> "We identified 10 novel D/EE-SWAS genes with a range of functions: ATP1A2, CACNA1A, FOXP1, GRIN1, KCNMA1, KCNQ3, PPFIA3, PUF60, SETD1B, and ZBTB18, and 2 novel copy number variants, 17p11.2 duplication and 5q22 deletion." **[verbatim-verified from cache]**

**From the systematic review of genetic ESES etiologies (PMID:29976148)** — 16 studies, 151 cases, 11 monogenic genes: *GRIN2A* (34 cases), *SCN2A* (6), *KCNA2* (5), *KCNB1* (5), *KCNQ2* (2), *CNKSR2* (2), *SLC6A1* (2), *SLC9A6/NHE6* (1), *ATN1/DRPLA* (1), *SRPX2/neuroserpin* (1), *OPA3* (1) **[reported]**. Key conclusion: *"The most common underlying pathway was channelopathy"* (56 cases) **[reported]**.

**From the Seizure 2023 systematic review (PMID:37352690)**, 172 cases: variants in *GRIN2A, ZEB2, CNKSR2*, and 17q21.31 deletions; conclusion that *"presentations occurring before age five warrant genetic investigation"* **[reported]**.

**From the Turkish cohort (PMID:38388889)**, 24 patients, 7 solved (29%): novel variants in *SLC12A5, DLG4, SLC9A6*; also *SCN8A* and Smith-Magenis syndrome **[reported]**.

***CNKSR2*** (Xp22.12; connector enhancer of KSR-2) deserves its own node — it's the X-linked epilepsy-aphasia gene:
> "The disease is characterized by intellectual disability, attention deficit-hyperactivity and abrupt lifelong language loss following a brief early-childhood epilepsy with continuous spike-waves in sleep." **[reported]**

~50% de novo; carrier mothers usually unaffected **[reported]**. Predominance of loss-of-function variants (PMC8281706).

### Consolidated gene table

| Gene | HGNC | Locus | Class | Mechanism | Inheritance |
|---|---|---|---|---|---|
| **GRIN2A** | hgnc:4585 | 16p13.2 | NMDAR subunit | LoF *or* GoF, domain-dependent | AD, incomplete penetrance |
| **CNKSR2** | hgnc:2570 | Xp22.12 | Postsynaptic scaffold | LoF | X-linked |
| GRIN2B | hgnc:4586 | 12p13.1 | NMDAR subunit | LoF/GoF | AD de novo |
| GRIN1 | hgnc:4584 | 9q34.3 | NMDAR subunit | LoF/GoF | AD de novo |
| SCN1A | hgnc:10585 | 2q24.3 | Nav1.1 | LoF | AD de novo |
| SCN2A | hgnc:10588 | 2q24.3 | Nav1.2 | GoF (early) / LoF (late) | AD de novo |
| SCN8A | hgnc:10596 | 12q13.13 | Nav1.6 | GoF | AD de novo |
| KCNQ2 | hgnc:6296 | 20q13.33 | Kv7.2 | LoF / dominant-negative | AD |
| KCNQ3 | hgnc:6297 | 8q24.22 | Kv7.3 | LoF | AD |
| KCNA2 | hgnc:6220 | 1p13.3 | Kv1.2 | LoF/GoF | AD de novo |
| KCNB1 | hgnc:6231 | 20q13.13 | Kv2.1 | LoF/dominant-negative | AD de novo |
| KCNH5 | hgnc:6254 | 14q23.1 | Kv10.2 | GoF | AD de novo |
| KCNMA1 | hgnc:6284 | 10q22.3 | BK channel | LoF/GoF | AD |
| CACNA1A | hgnc:1388 | 19p13.13 | Cav2.1 | LoF/GoF | AD |
| ATP1A2 | hgnc:800 | 1q23.2 | Na/K-ATPase α2 | LoF | AD |
| SLC6A1 | hgnc:11042 | 3p25.3 | GAT-1 GABA transporter | LoF | AD de novo |
| SLC12A5 | hgnc:13818 | 20q13.12 | KCC2 chloride extruder | LoF | AR/AD |
| SLC9A6 | hgnc:11079 | Xq26.3 | NHE6 (Christianson) | LoF | X-linked |
| DLG4 | hgnc:2903 | 17p13.1 | PSD-95 | LoF | AD de novo |
| MECP2 | hgnc:6990 | Xq28 | Transcriptional regulator | LoF | X-linked |
| FOXP1 | hgnc:3823 | 3p13 | TF | LoF/haploinsufficiency | AD de novo |
| ZBTB18 | hgnc:13030 | 1q44 | TF | LoF | AD de novo |
| SETD1B | hgnc:29187 | 12q24.31 | H3K4 methyltransferase | LoF | AD de novo |
| ARID1B | hgnc:18040 | 6q25.3 | BAF chromatin remodeler | Haploinsufficiency | AD de novo |
| PUF60 | hgnc:17042 | 8q24.3 | Splicing factor | LoF | AD de novo |
| CUL4B | hgnc:2555 | Xq24 | E3 ligase | LoF | X-linked |
| ZEB2 | hgnc:14881 | 2q22.3 | TF (Mowat-Wilson) | LoF | AD de novo |
| PPFIA3 | hgnc:9247 | 19q13.33 | Liprin-α3, active zone | LoF | AD |
| SRPX2 | hgnc:30668 | Xq22.1 | Secreted, synaptogenesis | — | X-linked (contested) |
| ATN1 | hgnc:3033 | 12p13.31 | DRPLA repeat expansion | Toxic GoF | AD, anticipation |
| OPA3 | hgnc:8142 | 19q13.32 | Mitochondrial (Costeff) | LoF | AR |

⚠️ **HGNC IDs above are from memory and are NOT OAK-verified.** Run `just validate-terms` before committing any of them — the repo uses lowercase `hgnc:`.

### Copy number variants and chromosomal abnormalities

Recurrent CNVs from the systematic review (89 CNVs total, 9 recurrent) **[reported]**:
- **15q11.2–13.1 duplication** — 15 cases (also relevant to your existing 15q11q13 microduplication entry — likely a comorbidity/grouping link)
- **3q29 duplication** — 11 cases
- **Xp22.12 deletion** (removing *CNKSR2*) — 6 cases
- **16p13 deletion** (removing *GRIN2A*) — 4 cases
- **17q21.31 deletion** (Koolen-de Vries) **[reported, Seizure 2023]**
- **17p11.2 duplication** (Potocki-Lupski) — novel, Ann Neurol 2024
- **5q22 deletion** — novel, Ann Neurol 2024
- **17p11.2 deletion** (Smith-Magenis) **[reported, Turkish cohort]**

### Allele frequency / somatic vs germline

All reported variants are **germline** (constitutional). Somatic mosaicism has not been established as a mechanism in D/EE-SWAS — though it's plausible in cases with focal cortical dysplasia. Pathogenic variants are absent or vanishingly rare in gnomAD; *GRIN2A* is strongly constrained (missense- and LoF-intolerant). ⚠️ Specific gnomAD constraint scores not retrieved — look them up if you want to cite pLI/o/e values.

### Modifier genes

None validated. The obvious candidate class — genes affecting sleep spindle generation and thalamocortical rhythm — is theorized but not demonstrated. The intrafamilial variability of the *same GRIN2A* variant strongly implies modifiers exist. Gap.

### Epigenetics

Indirect but suggestive: *SETD1B* (H3K4 methyltransferase), *ARID1B* (BAF chromatin remodeling), and *MECP2* (methyl-CpG binding) all appear as causal genes, i.e. **chromatin/transcriptional regulation is one of the two major functional clusters**. Per the Ann Neurol brain co-expression analysis, the D/EE-SWAS genes partition into **Cluster 1 (ion channels: GRIN2A, GRIN2B, KCNH5, KCNQ3, CACNA1A, SCN1A, SCN2A)** and **Cluster 2 (transcriptional regulators: FOXP1, PUF60, MECP2, ARID1B, ZBTB18)**, both co-expressed above chance **[reported]**. No DNA-methylation episignature has been published for D/EE-SWAS as a syndrome (though episignatures exist for some individual causal genes, e.g. ARID1B/Coffin-Siris). Gap.

---

## 5. Environmental Information

Thin section, and that's the honest answer.

- **Toxins / pollution / occupational / radiation:** no established role. Nothing in CTD.
- **Lifestyle:** no established role. Sleep deprivation may worsen seizures generically but is not a syndrome-specific factor.
- **Infectious agents:** no causal pathogen. Post-encephalitic and post-meningitic acquired brain injury can be a *structural* substrate in individual cases, but this is generic acquired-lesion territory, not a specific infectious etiology. Notably, LKS was historically *suspected* to be inflammatory/autoimmune (hence steroid responsiveness), but no pathogen or autoantibody has been confirmed.
- **The one real "environmental" exposure is pharmacological** — the carbamazepine/oxcarbazepine/phenytoin/phenobarbital aggravation described in §2. I'd model this as an environmental/iatrogenic trigger node rather than leaving §5 empty.
- **Perinatal events** (hypoxia-ischemia, IVH, sinovenous thrombosis) are the most important non-genetic contributors, acting via structural injury — especially thalamic.

---

## 6. Mechanism / Pathophysiology

This is the interesting part. There are **three distinct, partly complementary mechanistic models**, and I'd curate them as competing/complementary `mechanistic_hypotheses` rather than blending them.

### Model A — Thalamocortical disconnection and the "augmenting response" (CANONICAL for structural cases)

The thalamus is the metronome for non-REM sleep rhythms. Lesion it early and unilaterally, and the cortex on that side loses its normal pacing input — and, critically, *gains* an abnormal form of frequency-dependent synaptic potentiation.

From **PMID:29133062** (nine patients with unilateral neonatal thalamic lesions):

> "Thalamic volume loss ranged from 19% to 94%, predominantly on medial and dorsal nuclei and sparing the ventral thalamus. Lesions produced white matter loss and ventricle enlargement on the same hemisphere, which in four patients was associated with selective loss of thalamic-cortical fibers." **[verbatim-verified from cache]**

> "Impact on EEG rhythms was mild, with a volume-loss-related decrease in alpha power and preservation of sleep spindles. The sleep continuous spiking was lateralized to the hemisphere with the lesion." **[verbatim-verified]**

> "Unilateral selective thalamic-cortical disconnection is a common feature in our patients and is associated with both a focal pattern of CSWS and a pathological type of frequency-dependent excitability (peak: 10-20Hz). We propose that this excitability represents an abnormal synaptic plasticity previously described as the augmenting response. This synaptic plasticity has been described as absent in the corticocortical interactions in healthy experimental animals, emerging after ablation of the thalamus and producing a frequency-dependent potentiation with a peak at 10-20Hz. Because this response is potentiated by sleep states of reduced brainstem activation and by appropriate stimulating rhythms, such as sleep spindles, the simultaneous occurrence of these two factors in nonrapid-eye-movement sleep is proposed as an explanation for CSWS in our patients." **[verbatim-verified — this is the money quote for the whole mechanism section]**

The causal chain, node by node:

```
Early thalamic lesion (medial/dorsal nuclei)
  → selective loss of thalamocortical fibers (unilateral disconnection)
    → emergence of pathological corticocortical "augmenting response"
       (frequency-dependent potentiation peaking 10–20 Hz — absent in healthy cortex)
      → sleep spindles (10–16 Hz) + reduced brainstem arousal tone in NREM
         act as the ideal driving stimulus
        → runaway spike-wave activation confined to NREM sleep
          → [feeds Model B]
```

That's elegant: the spindle, a *normal* sleep rhythm, becomes the trigger pulse for a *pathological* potentiation the healthy brain doesn't have. Like a heart with a re-entrant circuit — the sinus beat isn't the problem, the abnormal pathway is; the normal rhythm just keeps lighting the fuse.

- **UBERON:0001903** thalamic reticular nucleus *(verified)*
- **UBERON:0001897** dorsal plus ventral thalamus *(verified)*
- **UBERON:0000956** cerebral cortex, **UBERON:0001950** neocortex *(verified)*
- **GO:0021794** thalamus development *(verified)*
- **CL:0000617** GABAergic neuron (TRN neurons), **CL:0000598** pyramidal neuron, **CL:0000679** glutamatergic neuron *(all verified)*

### Model B — Disruption of sleep-dependent synaptic homeostasis (CANONICAL for the *encephalopathy*)

Model A explains why the spikes happen in sleep. Model B explains why the spikes make the child *worse*.

Normal picture: you potentiate synapses all day (learning), and slow-wave sleep runs a global **downscaling** program that renormalizes synaptic weight, preserving signal-to-noise and consolidating what matters. It's a nightly pruning shift — like the lymphatic system clearing the interstitium overnight, except for synaptic weight instead of fluid.

In SWAS, that shift doesn't happen. Per the literature summarized around **Bölsterli et al.** (impaired slow-wave downscaling in ESES):

> "The profound spike activation in sleep found in CSWS disrupts synaptic homeostasis—the balanced synaptic potentiation during daytime and synaptic downscaling in sleep—leading to an inefficient cerebral network." **[reported]**

> "Alterations in synaptic strength are shown through changes in sleep slow-wave activity (SWA), but notably during CSWS there are no sleep SWA changes, which occur again after CSWS remission" **[reported]**

That last observation is the strongest causal evidence available in humans: the overnight slope of slow-wave activity — the electrophysiological fingerprint of downscaling — **flattens during the active phase and returns when SWAS remits**. State-dependent, reversible, and time-locked to the clinical course.

And from **PMID:25160535** (Issa 2014):

> "Over the last 20 years, a variety of basic science findings suggest how spike-wave activity during sleep can cause the observed clinical outcomes." **[verbatim-verified]**

> "The role of slow-wave sleep in normal cortical plasticity during developmental critical periods, how disruption of slow-wave sleep by electrographic seizures could affect cortical maps and development, and the organization and functional connectivity of the thalamic structures that when damaged are thought to produce these seizure disorders are reviewed." **[verbatim-verified]**

Chain:

```
Near-continuous NREM spike-wave
  → failure of sleep-dependent synaptic downscaling (flat overnight SWA slope)
    → saturated, non-selective synaptic weights → poor signal-to-noise
      → failed overnight memory consolidation + corrupted cortical map refinement
        → domain-specific regression matching the spike topography
          → (spikes remit at puberty) partial recovery, but the critical-period
             window for that cortical map has closed → residual permanent deficit
```

The **critical-period** framing is what explains the syndrome's cruellest feature: seizures stop, EEG normalizes, and the child still doesn't fully get the language back. The scaffolding came down before the building was finished.

- **GO:0048167** regulation of synaptic plasticity *(verified)*
- **GO:0060291** long-term synaptic potentiation, **GO:0060292** long-term synaptic depression *(verified)*
- **GO:0030431** sleep *(verified)*
- **GO:0050803** regulation of synapse structure or activity *(verified)*
- **GO:0050890** cognition, **GO:0007613** memory *(verified)*

### Model C — Molecular substrate: NMDAR/channel dysfunction and E/I imbalance

For the genetic cases, the proximate lesion is at the synapse.

*GRIN2A* encodes GluN2A, the subunit that dominates NMDA receptors in cortex from late infancy onward — exactly the developmental window of this syndrome. GluN2A-containing NMDARs have fast deactivation kinetics; alter them and you alter the temporal integration window for coincidence detection, i.e. the machinery of plasticity itself. Both directions break things:
- **GoF (TMD/linker missense):** prolonged current, excess Ca²⁺ influx, excitotoxic/hyperexcitable phenotype → severe DEE
- **LoF (null, ATD/LBD missense):** reduced NMDAR signalling — including on GABAergic interneurons, so net *dis*inhibition → milder epilepsy-aphasia spectrum

The other genes converge on the same theme from different angles: Nav/Kv/Cav channelopathies (intrinsic excitability), *SLC6A1*/GAT-1 and *SLC12A5*/KCC2 (GABAergic inhibitory tone and chloride gradient), *DLG4*/PSD-95, *CNKSR2*, *PPFIA3* (postsynaptic scaffolding and active zone). Plus the transcriptional-regulator cluster acting further upstream on the whole developmental program.

- **GO:0004972** NMDA glutamate receptor activity *(verified)*
- **GO:0035249** synaptic transmission, glutamatergic *(verified)*
- **GO:0060079** excitatory postsynaptic potential *(verified)*
- **GO:0098978** glutamatergic synapse *(verified)*
- **GO:0005248** voltage-gated sodium channel activity, **GO:0005249** voltage-gated potassium channel activity *(verified)*
- **GO:0006357** regulation of transcription by RNA polymerase II *(verified — for Cluster 2)*
- **UniProt:** GluN2A = Q12879; PDB structures of NMDAR GluN1/GluN2A heterotetramer available

**Note for the KB:** this maps cleanly onto your existing module `epilepsy_excitation_inhibition_imbalance` — `#Excitation-Inhibition Imbalance` is an obvious `conforms_to` target. Model B (sleep-dependent downscaling failure) is *not* covered by any existing module and might be worth one, since it also touches your `glymphatic_dysfunction` module's territory conceptually (both are "sleep does maintenance work; disease blocks the maintenance") without duplicating it — glymphatic is extracellular clearance, this is synaptic weight renormalization. Different plumbing, same night shift.

### Network-level: functional imaging

FDG-PET and EEG-fMRI (De Tiège et al., Epilepsia 2009) show the syndrome is a *network* disease, not a focal one:

> "Hypermetabolism in perisylvian regions bilaterally and hypometabolism in lateral and mesial prefrontal cortex, precuneus, posterior cingulate cortex and parahippocampal gyri characterized the acute phase of CSWS. Altered functional connectivity was found between hyper- and hypometabolic regions" **[reported]**

The hypometabolic set is essentially the **default mode network** (see "Default mode network hypometabolism in epileptic encephalopathies with CSWS," Epilepsy Res 2014). The mechanism proposed is **remote inhibition** — the hyperactive epileptic focus actively suppresses distant connected cortex. That explains how a perisylvian spike focus produces a *frontal-executive* clinical syndrome: the deficit is downstream of the focus, not at it.

- **UBERON:0000451** prefrontal cortex, **UBERON:0016525** frontal lobe, **UBERON:0001871** temporal lobe *(verified)*

### Not involved

- **Metabolic changes:** no primary metabolic derangement (excepting the rare *OPA3*/Costeff case). Regional cerebral glucose metabolism is altered (above), but that's a consequence.
- **Immune system:** steroid responsiveness has long tempted people toward a neuroinflammatory hypothesis, and microglial (**CL:0000129**) / astrocytic (**CL:0000127**) contributions are plausible, but **no autoantibody, no CSF inflammatory signature, no confirmed immune mechanism**. Steroids may work via non-immune routes (direct effects on neuronal excitability, BBB, or neurosteroid pathways). Curate this as an explicit `KNOWLEDGE_GAP` — it's a real open question and the biggest unexplained therapeutic observation in the syndrome.
- **Tissue damage:** no necrosis, no fibrosis, no gliotic signature attributable to the SWAS itself. The "damage" is functional/synaptic, which is precisely why partial recovery is possible.

### Molecular profiling

Essentially absent for this syndrome specifically. The one systems-level result worth citing is the Ann Neurol **brain-specific gene co-expression analysis** showing the two functional clusters. No GEO dataset, no proteomics, no metabolomics, no single-cell or spatial data specific to D/EE-SWAS. Large gap, and a legitimate one to record.

---

## 7. Anatomical Structures Affected

**Organ level**
- **Primary:** brain (**UBERON:0000955**), specifically cerebral cortex (**UBERON:0000956**) and thalamus (**UBERON:0001897**) *(verified)*
- **Body system:** central nervous system only. No systemic organ involvement — this is a purely neurological syndrome unless the underlying genetic cause is syndromic (e.g. Mowat-Wilson, Smith-Magenis, Christianson, Costeff bring their own multi-organ features)
- **Secondary:** none organ-wise; secondary *consequences* are behavioral/educational/psychosocial

**Regional**
- **Thalamus** — medial and dorsal nuclei preferentially; **ventral thalamus spared** (verified from PMID:29133062). Thalamic reticular nucleus (**UBERON:0001903**) is the spindle generator and is the mechanistic linchpin
- **Perisylvian cortex** — hypermetabolic in the acute phase; the LKS substrate (superior temporal / auditory association cortex)
- **Frontal cortex** (**UBERON:0016525**) and **prefrontal cortex** (**UBERON:0000451**) — hypometabolic; the CSWS/dysexecutive substrate
- **Precuneus, posterior cingulate, parahippocampal gyrus** — hypometabolic (DMN)
- **Centrotemporal / rolandic region** — the SeLECTS-spectrum spike focus
- Ipsilateral **white matter** and **lateral ventricle** — volume loss / enlargement in thalamic-lesion cases

**Lateralization**
Genuinely variable and clinically informative: **unilateral/focal SWAS** in thalamic-lesion and other unilateral structural cases (spiking lateralizes to the lesioned hemisphere — verified in PMID:29133062); **bilateral/diffuse SWAS** in genetic and idiopathic cases. Bilateral secondary synchrony from a unilateral generator is common. Worth curating as a distinguishing feature.

**Cell level**
- **CL:0000598** pyramidal neuron (cortical, layer V — the augmenting-response substrate)
- **CL:0000679** glutamatergic neuron
- **CL:0000617** GABAergic neuron (TRN, cortical interneurons)
- **CL:0000099** interneuron
- **CL:0010012** cerebral cortex neuron
- **CL:0000127** astrocyte, **CL:0000129** microglial cell — speculative, no direct evidence
*(all verified against `sqlite:obo:cl`)*

**Subcellular**
- **GO:0045202** synapse; **GO:0098978** glutamatergic synapse *(verified)*
- Postsynaptic density (GO:0014069), dendritic spine (GO:0043197), plasma membrane, axon initial segment — ⚠️ these four IDs are from memory, verify with OAK
- No mitochondrial, lysosomal, ER, or nuclear-envelope pathology (excepting rare *OPA3*)

---

## 8. Temporal Development

This syndrome has one of the tightest and most reproducible time courses in pediatric neurology, which makes it very curatable.

**Onset**
- **Seizure onset:** 2–12 years, **peak 4–5 years**; medians in cohorts cluster at 3.3 yr (DEE-SWAS) / 4.4 yr (EE-SWAS) **[reported, Ann Neurol 2024]** and 4 years in the Turkish cohort **[reported]**
- **Regression onset:** ~1–2 years after seizures, typically **5–6 years**
- **LKS auditory verbal agnosia onset:** 3–9 years
- **Pattern:** insidious-to-subacute. Regression can be gradual over months or, disconcertingly, abrupt over weeks. Fluctuation (especially in LKS language) is characteristic and often misread as behavioral or psychiatric

**Stages**

| Stage | Age | Features |
|---|---|---|
| **Prodrome** | 2–5 yr | Infrequent nocturnal focal seizures; development normal (EE-SWAS) or already delayed (DEE-SWAS); EEG shows focal spikes without SWAS |
| **Active / encephalopathic** | 5–9 yr | SWAS on sleep EEG; seizure frequency escalates (up to 70% with multiple daily seizures **[reported]**); regression; new seizure types appear (atypical absence, atonic/negative myoclonus) |
| **Remission** | ~9–12 yr, near puberty | SWAS resolves (~age 11 typically **[reported]**); seizures cease; some cognitive recovery |
| **Residual** | adolescence–adult | Persistent deficits in most; degree tracks how long the active phase lasted |

**Progression rate & course:** stepwise/subacute during the active phase, then a **spontaneous, age-dependent remission** — one of the few epileptic encephalopathies that reliably self-terminates. But the neurodevelopmental damage does not fully reverse.

**Duration:** active phase typically 2–5 years. From the Ann Neurol cohort: **DEE-SWAS median epilepsy duration 10.0 years vs EE-SWAS 5.2 years** **[reported]**, and:

> "Although developmental regression patterns were similar in both syndromes, DEE-SWAS was associated with a longer duration of epilepsy and poorer intellectual outcome than EE-SWAS." **[verbatim-verified from cache]**

**Remission patterns:** both **spontaneous** (age-dependent, near-universal for the EEG pattern and seizures) and **treatment-induced** (steroids/benzodiazepines can abolish SWAS in weeks). Relapse after treatment-induced remission is common — the diazepam and steroid literature is full of it — which is why prolonged/pulsed courses are used.

**Critical period — the whole therapeutic rationale:** the vulnerable window *is* the intervention window. Because the deficit accrues from cumulative SWAS exposure during an active cortical-map-refinement period, **duration of ESES is the main predictor of neurocognitive outcome** **[reported, PMC3929187]**. Every month of unsuppressed SWAS is irreversible developmental opportunity cost. This is the argument for early aggressive treatment and for annual sleep EEG surveillance in at-risk children.

---

## 9. Inheritance and Population

**Epidemiology**
- **Prevalence among childhood epilepsies:** *"0.5% to 0.6% of all childhood epilepsy cases"* at tertiary referral epilepsy centers **[reported, PMC3929187]**; other sources give a wider **0.2%–2%** of epilepsies **[reported]**
- **Population prevalence:** ⚠️ Not reliably published. Orphanet classes it as rare (< 1 in 2,000). Back-of-envelope from a childhood epilepsy prevalence of ~0.5–1% and a 0.5% share gives an order of magnitude around **2–5 per 100,000 children**, but that's a derived estimate, not a cited figure — **do not curate it as a sourced prevalence.** Use `prevalence_class: UNKNOWN` or `NOT_YET_DOCUMENTED` with a `notes` field, or cite the ORPHA:725 epidemiology row directly via the structured Orphanet cache
- **Incidence:** no published incidence figure found. Gap.
- **Sex ratio:** ~**60:40 male:female** **[reported, PMC3929187]**; 53% male in the Ann Neurol cohort **[reported]**. ILAE states both sexes equally affected **[reported]**. Treat as "slight male predominance or none" — sources disagree
- **Age distribution:** exclusively pediatric onset (2–12), remitting around puberty. Adults exist only as survivors with residual deficits

**Inheritance (for the genetic subset — ~34% of cases)**
- **Predominantly de novo autosomal dominant.** Most single-gene cases are de novo heterozygous variants
- **X-linked** for *CNKSR2* (~50% de novo; carrier mothers usually unaffected **[reported]**), *MECP2*, *CUL4B*, *SLC9A6*
- **Autosomal recessive** rarely (*OPA3*/Costeff)
- **HPO inheritance terms:** HP:0000006 (AD), HP:0001417 (X-linked), HP:0001423 (X-linked dominant), HP:0001419 (X-linked recessive), HP:0000007 (AR) — ⚠️ verify these IDs with OAK; I did not check them
- **Penetrance:** **incomplete**, explicitly documented for *GRIN2A* — OMIM #245570 notes *"incomplete penetrance and intrafamilial variability, even among family members who carry the same GRIN2A mutation"* **[reported]**. Use `penetrance: INCOMPLETE`
- **Expressivity:** **highly variable** — the same *GRIN2A* variant can produce anything from asymptomatic to severe DEE across one family. This is the single best-documented genotype-phenotype caveat in the syndrome
- **Anticipation:** not a feature, except in the one *ATN1*/DRPLA repeat-expansion case
- **Germline mosaicism:** not documented specifically; theoretically possible for any de novo dominant gene, and standard recurrence-risk counselling (~1%) applies
- **Founder effects:** none reported
- **Consanguinity:** no established role (the recessive fraction is tiny)
- **Carrier frequency:** not applicable at syndrome level; not meaningfully estimable

**Population demographics**
- **Ethnic/geographic:** no established variation. Cohorts published from Australia/NZ, UK, Netherlands, Italy, France, Germany, Spain, Denmark, Turkey, Serbia, Romania, Malaysia, Hong Kong, USA — the syndrome appears globally with no reported prevalence differences. Ascertainment is heavily skewed to high-income countries with routine overnight EEG access, which is itself worth noting: **you cannot diagnose this without a sleep EEG**, so under-diagnosis in low-resource settings is near-certain
- **Variant geography:** no population-specific variants reported

---

## 10. Diagnostics

### The single indispensable test

**Overnight / sleep EEG.** Nothing else diagnoses this. A routine awake EEG can be entirely normal or show only modest focal spikes; the syndrome hides in NREM sleep. If you take one thing from this section: *a child with unexplained developmental regression needs a sleep EEG, not a waking one.*

**EEG features:**
- Bilateral (or, less often, unilateral) **continuous or near-continuous slow spike-wave during NREM sleep**
- Frequency **1.5–3 Hz** (often stated as 1–2 Hz)
- Marked attenuation in REM sleep and wakefulness — the state-dependence *is* the diagnostic signature
- SWI highest in the first sleep cycle, declining across the night
- Localization typically frontotemporal or centrotemporal
- **HP:0011182** Interictal epileptiform activity; **HP:0010841** Multifocal epileptiform discharges; **HP:0002353** EEG abnormality *(verified)*

**Spike-wave index (SWI) — and its controversy.** SWI = (minutes containing spike-wave × 100) / total NREM minutes.

Thresholds are genuinely unsettled, and this matters for any computable phenotype:
- Classic/strict: **≥85%** of NREM ("typical ESES")
- Commonly used pragmatic: **≥50%**
- SWI <85% sometimes labeled "atypical ESES"
- Resolution often defined as SWI **<50%**
- **The ILAE 2022 criteria deliberately do NOT specify a minimum percentage** — they require "marked activation" clinically judged, precisely because the thresholds were never validated against outcome

⚠️ This is a real curation trap. Do **not** write "SWI ≥85% is the ILAE criterion" — it isn't. Model it as an open methodological question (`KNOWLEDGE_GAP`) with the competing thresholds recorded. The systematic review noted ~67.6% of published genetic cases were diagnosed using a >50% threshold **[reported]** — i.e. the literature isn't even internally consistent about who has the disease.

### Imaging
- **Brain MRI is mandatory.** Looking for: thalamic lesion (often small, requires deliberate attention to medial/dorsal nuclei — easy to miss), polymicrogyria, periventricular leukomalacia, porencephaly, hydrocephalus/shunt, cortical dysplasia. Volumetric analysis may be needed for subtle thalamic volume loss (range in the published series: 19%–94%)
- **FDG-PET** (research/selected): perisylvian hypermetabolism + prefrontal/precuneus/posterior cingulate hypometabolism in the active phase
- **SPECT:** focal hyperperfusion with remote hypoperfusion
- **EEG-fMRI:** research tool for mapping the generator and remote effects
- **Polysomnography with spindle quantification:** emerging — sleep spindle density is both a biomarker and, per the rTMS work, a treatment-response correlate

### Genetic testing

Given a 34% genetic yield, this is not optional. Recommended approach:

1. **Chromosomal microarray (CMA)** first or in parallel — CNVs are ~19% of the genetic yield (6/31 in the Ann Neurol cohort), and several recurrent CNVs (15q11.2-13.1 dup, 3q29 dup, Xp22.12 del, 16p13 del, 17q21.31 del, 17p11.2 dup/del) are microarray-detectable
2. **Exome or genome sequencing** — best single-test yield; genome adds CNV/structural resolution and non-coding coverage. The Seizure 2023 review concluded that *"presentations occurring before age five warrant genetic investigation"* **[reported]**
3. **Epilepsy gene panels** — acceptable but will miss the syndromic and novel genes; must include *GRIN2A, GRIN2B, GRIN1, CNKSR2, SCN1A, SCN2A, SCN8A, KCNQ2, KCNQ3, KCNA2, KCNB1, KCNH5, KCNMA1, CACNA1A, ATP1A2, SLC6A1, SLC12A5, SLC9A6, DLG4, MECP2, FOXP1, ZBTB18, SETD1B, ARID1B, PUF60, CUL4B, ZEB2, PPFIA3*
4. **Single-gene *GRIN2A*** — reasonable only when the phenotype is classic epilepsy-aphasia/LKS and cost is limiting
5. **Karyotype/FISH:** low yield; reserve for suspected specific rearrangements
6. **Mitochondrial DNA testing:** not indicated
7. **Repeat expansion testing:** not indicated (except the DRPLA outlier if there's a suggestive family history)
8. **Variant classification** per ACMG/AMP; interpret in ClinVar/ClinGen context. **For *GRIN2A*, push for protein-domain annotation** (ATD/LBD vs TMD/linker) because it changes the therapeutic hypothesis

**Omics diagnostics:** RNA-seq, proteomics, metabolomics, methylation episignature — none established for this syndrome. Metabolic workup is generally low-yield unless the phenotype suggests a specific IEM.

### Clinical criteria

**ILAE 2022 (Specchio et al., PMID:35503717) — DEE-SWAS/EE-SWAS**, in substance:
- Regression or plateauing in development affecting one or more of cognition, language, behavior, motor function
- Marked spike-wave activation in NREM sleep, temporally related to the regression
- Onset 2–12 years (peak 4–5)
- Seizures usually present but **not mandatory**
- EE-SWAS if development was normal before; DEE-SWAS if impaired before
- LKS as a distinct EE-SWAS subtype defined by acquired auditory verbal agnosia

⚠️ I could not retrieve the position paper's formal *mandatory / alerts / exclusionary* tables — Epilepsia and the ILAE site both blocked automated fetch. **Get the actual table from the PDF before curating `definitions` for this entry.** The cached `references_cache/PMID_35503717.md` is abstract-only.

### Differential diagnosis

| Condition | How to distinguish |
|---|---|
| **SeLECTS** (self-limited epilepsy with centrotemporal spikes) | Same spectrum, but no marked sleep activation, no regression. Can *evolve into* DEE-SWAS — hence the surveillance argument |
| **Lennox-Gastaut syndrome** | Slow (1.5–2.5 Hz) spike-wave in *wakefulness*, tonic seizures in sleep, generalized paroxysmal fast activity, no discrete regression event |
| **Autism spectrum disorder with regression** | Regression typically <3 yr, no SWAS on sleep EEG. Overlaps genuinely — a sleep EEG is the discriminator |
| **Acquired aphasia from stroke/tumor/encephalitis** | Focal lesion on MRI, no SWAS |
| **Hearing loss / auditory processing disorder** | Normal audiometry and ABR distinguish LKS's auditory verbal agnosia from deafness — a classic misdiagnosis |
| **Myoclonic-atonic epilepsy (Doose)** | Myoclonic-atonic seizures dominant, generalized 2–3 Hz spike-wave awake |
| **Progressive neurodegenerative / metabolic disease** | Progressive and non-remitting; DEE-SWAS plateaus and improves at puberty |
| **Rett syndrome / MECP2** | Hand stereotypies, deceleration of head growth — but note *MECP2* is also a D/EE-SWAS gene, so these can coexist |
| **Psychiatric / selective mutism** | Sleep EEG |

### Screening

- **No newborn or population screening** exists or is warranted
- **Targeted surveillance is the meaningful intervention:** serial sleep EEG in children with (a) early thalamic lesion, (b) polymicrogyria, (c) shunted hydrocephalus, (d) SeLECTS with new cognitive/behavioral change, (e) known pathogenic variant in a D/EE-SWAS gene. There is no formal guideline endorsing an interval — I'd flag "annual, or on any cognitive change" as expert-practice, not evidence-based
- **Cascade testing** where a familial variant is identified; be explicit about incomplete penetrance in counselling
- **Carrier screening:** not applicable

---

## 11. Outcome / Prognosis

**Mortality:** Not a fatal syndrome. **No excess mortality** established, no survival statistics, no life-expectancy reduction attributable to D/EE-SWAS itself. SUDEP risk is presumably that of the underlying epilepsy generally, but has not been quantified for this syndrome. The RESCUE ESES trial explicitly recorded *"No deaths were reported"* **[verbatim-verified]**. This is a **morbidity disease, not a mortality disease** — curate `disease-specific mortality: none established` rather than leaving it blank.

**Morbidity — the actual endpoint.** Persistent intellectual disability, language impairment, ADHD, and learning disability in most patients. Educational placement and independent adult functioning are the outcomes that matter.

Concrete numbers from the Ann Neurol 2024 cohort **[reported]**:

| | DEE-SWAS | EE-SWAS |
|---|---|---|
| Moderate–severe intellectual disability | **49%** | **8%** |
| Normal / mild ID | 51% | 92% |
| Median epilepsy duration | 10.0 yr | 5.2 yr |

Plus, verbatim: *"Phenotypic analysis highlights valuable clinical differences between DEE-SWAS and EE-SWAS which inform clinical care and prognostic counseling."* **[verbatim-verified]**

**From the older CSWS literature:** *"Most patients continue to demonstrate some degree of impairment"* **[reported]**, and *"Duration of ESES seems to be the main predictor of neurocognitive function"* **[reported]**.

**Recovery potential:** Partial. Seizures and the EEG pattern remit near-universally around puberty. Cognition recovers *partially* — the earlier and more completely SWAS is suppressed, the more is recovered. Full return to premorbid function is uncommon, and in LKS specifically, complete language recovery is the exception; many are left with lasting receptive language impairment into adulthood.

**Prognostic factors (best supported → weakest):**
1. **Duration of SWAS** — the strongest predictor
2. **Etiology** — from the 50-child Serbian cohort: SeLECTS-background patients had *"shorter symptom duration and superior prognosis, whereas those with structural etiologies experienced prolonged manifestations and reduced treatment efficacy"* **[reported, PMID:41076959]**
3. **DEE-SWAS vs EE-SWAS** — pre-existing impairment predicts worse outcome (49% vs 8% moderate-severe ID)
4. **Age at SWAS onset** — earlier onset, worse (more of the critical period consumed)
5. **Spike-wave index magnitude** — higher SWI associated with more severe developmental disturbance **[reported]**, though weaker/less consistent than duration
6. **Time to effective treatment** — the modifiable one

**Prognostic biomarkers:** SWI and its trajectory; **sleep spindle density** (emerging — the rTMS study found spindle increase correlated with IQ improvement, p=0.035 **[reported]**); overnight slow-wave-activity slope (research). No molecular/fluid biomarker exists.

**Complications:** educational failure, behavioral/psychiatric comorbidity, social exclusion; steroid-related complications from prolonged treatment (weight gain, hypertension, immunosuppression, bone effects) — treatment toxicity is a genuine part of the disease burden here.

---

## 12. Treatment

The uncomfortable headline: **treatment for this syndrome rests on a single small, prematurely terminated RCT plus a lot of retrospective case series.** Every decision below is made in an evidence twilight.

### The one randomized trial: RESCUE ESES (PMID:38081201, Lancet Neurol 2024)

Corticosteroids vs clobazam, 8 tertiary centres, 7 European countries, children 2–12 diagnosed within 6 months, steroid- and clobazam-naive.

> "At the 6-month assessment, an improvement of 11·25 IQ points or greater was reported for five (25%) of 20 children assigned corticosteroids versus zero (0%) of 18 assigned clobazam (risk ratio [RR] 10·0, 95% CI 1·2-1310·4; p=0·025)." **[verbatim-verified from cache]**

> "An improvement of 0·75 points or more in the cognitive sum score was recorded for one (5%) of 22 children assigned corticosteroids versus one (5%) of 21 children assigned clobazam (RR 1·0, 95% CI 0·1-11·7, p=0·97)." **[verbatim-verified]**

> "The trial was terminated prematurely, and the target sample size was not met, so our findings must be interpreted with caution. Our data indicated an improvement in IQ outcomes with corticosteroids compared with clobazam treatment, but no difference was seen in cognitive sum score. Our findings strengthen those from previous uncontrolled studies that support the early use of corticosteroids for children with EE-SWAS." **[verbatim-verified]**

Read that carefully before curating: **the two co-primary outcomes disagreed.** IQ favored steroids with a confidence interval you could drive a bus through (1.2 to 1310.4); the cognitive sum score showed literally nothing. 45 children enrolled against a target of 130 over eight years. This is *suggestive* evidence for steroids, not established efficacy — and it should be curated with that caveat intact, not laundered into "steroids are proven effective."

Regimens used: prednisolone 1–2 mg/kg/day oral continuous, **or** methylprednisolone 20 mg/kg/day IV ×3 days every 4 weeks (pulse). Clobazam 0.5–1.2 mg/kg/day.

Safety **[verbatim-verified]**: *"Adverse events occurred in ten (45%) of 22 children who received corticosteroids, most frequently weight gain, and in 11 (52%) of 21 children who received clobazam, most often fatigue and behavioural disturbances."*

### Real-world effectiveness (PMID:41076959, Seizure 2025, n=50)

> "corticosteroids (80.9%), clobazam (55.8%), levetiracetam (54.1%), and sulthiame (52.9%) were the most effective treatments." **[reported]**

### Pooled historical data

A pooled analysis of 575 treated ESES cases found improvement in cognition or EEG most often with **surgery (90%), steroids (81%), or benzodiazepines (68%)**, with standard ASMs least effective (**49%**) **[reported]**. Note the surgery figure is drowning in selection bias — only carefully chosen structural cases get operated.

### Treatment table with NCIT/CHEBI annotations

| Treatment | Modality | NCIT | Agent (CHEBI) | Evidence |
|---|---|---|---|---|
| **Prednisolone / prednisone** (continuous oral) | SMALL_MOLECULE | NCIT:C15986 Pharmacotherapy † | CHEBI:8378 prednisolone ‡ / CHEBI:8382 prednisone ‡ | RESCUE ESES RCT; drug class NCIT:C2322 Corticosteroid † |
| **Methylprednisolone pulse** (20 mg/kg/d ×3d, monthly) | SMALL_MOLECULE | NCIT:C15986 † | CHEBI:6888 6alpha-methylprednisolone ‡ | RESCUE ESES; 47% of European centres use pulse-only **[reported, PMID:40301922]** |
| **ACTH** | PEPTIDE | NCIT:C15986 † | ⚠️ CHEBI unverified | Case series only |
| **Clobazam** | SMALL_MOLECULE | NCIT:C15986 † | CHEBI:31413 clobazam ‡ | RCT comparator; 55.8% effective real-world |
| **High-dose oral/rectal diazepam** (nocturnal) | SMALL_MOLECULE | NCIT:C15986 † | CHEBI:49575 diazepam ‡ | Case series; rapid EEG effect, frequent relapse |
| **Levetiracetam** | SMALL_MOLECULE | NCIT:C15986 † | CHEBI:6437 levetiracetam ‡ | 54.1% effective real-world |
| **Sulthiame** | SMALL_MOLECULE | NCIT:C15986 † | ⚠️ **no CHEBI term found via OAK** — use NCIT drug term or free-text | 52.9% effective; European/Japanese use; case report of GRIN2A-variant EE-SWAS responding (PMC9996194) |
| **Ethosuximide** | SMALL_MOLECULE | NCIT:C15986 † | CHEBI:4887 ethosuximide ‡ | First-line historically; T-type Ca²⁺ block fits the thalamocortical model |
| **Valproate** | SMALL_MOLECULE | NCIT:C15986 † | CHEBI:39867 valproic acid ‡ | First-line historically |
| **Acetazolamide** | SMALL_MOLECULE | NCIT:C15986 † | CHEBI:27690 acetazolamide ‡ | Adjunct, case series |
| **Ketogenic diet** | BEHAVIORAL | NCIT:C15447 Dietary Intervention † | n/a | Weak: one 5-patient series (1 complete, 1 partial, 3 no response) **[reported]** |
| **IVIG** | OTHER | NCIT:C15986 † | ⚠️ unverified | Anecdotal; rests on the unproven immune hypothesis |
| **Epilepsy surgery** (resection, multiple subpial transection, hemispherotomy, corpus callosotomy) | SURGERY | NCIT:C15329 Surgical Procedure † | n/a | 90% improvement in pooled series (selection-biased); *"should be considered in cases of drug-resistant D/EE-SWAS that have an underlying structural abnormality"* **[reported]** |
| **rTMS** | DEVICE | ⚠️ no verified NCIT term | n/a | Open-label, n=9, PMID:40620003 |
| **tDCS** | DEVICE | ⚠️ unverified | n/a | Case-level only |
| **Speech and language therapy** | BEHAVIORAL | NCIT:C159273 speech therapy † | n/a | Supportive; essential, especially LKS |
| **Special education / neuropsych support** | BEHAVIORAL | NCIT:C15747 Supportive Care † | n/a | Universal |
| **Genetic counselling** | — | NCIT:C15240 Genetic Counseling † | n/a | For solved genetic cases |

† NCIT IDs taken from the verified list in `CLAUDE.md`. ‡ CHEBI IDs **verified via `sqlite:obo:chebi`**. Everything marked ⚠️ needs an OAK lookup before curating.

### Contraindicated / to avoid

**Carbamazepine (CHEBI:3387 ‡), oxcarbazepine, phenytoin, phenobarbital** — can induce or worsen SWAS. *"Carbamazepine is relatively contraindicated in ESES and should be discontinued"* **[reported]**. This belongs in the entry as an explicit negative treatment recommendation — it's the cheapest intervention in the whole syndrome.

### Precision medicine — the frontier

The rational-therapy story here is genuinely good, and it's the reason etiologic workup matters:

- ***GRIN2A* gain-of-function (TMD/linker missense) → memantine** (CHEBI:64312 ‡), an NMDAR open-channel blocker. Per Strehlow et al.: these individuals *"represent promising candidates for treatment with NMDAR blockers, such as memantine"* **[reported]**
- ***GRIN2A* loss-of-function (null, ATD/LBD) → NMDAR positive allosteric modulators** (investigational; L-serine has been tried for GRIN LoF)
- **Sodium-channel GoF (*SCN2A* early-onset, *SCN8A*) → high-dose sodium channel blockers** — note this directly conflicts with the general "avoid carbamazepine" rule, which is exactly why genotype matters
- **Sodium-channel LoF (*SCN1A*, *SCN2A* late-onset) → avoid** sodium channel blockers
- ***SLC6A1*/GAT-1 LoF** → GABAergic strategies under investigation

From the Ann Neurol conclusion: *"Our etiological findings pave the way for the development of precision therapies."* **[verbatim-verified]**

### Emerging: rTMS via sleep-spindle restoration

Small (n=9) open-label study, PMID:40620003, and mechanistically the most interesting thing in the treatment literature because it *tests Model B directly*. Low-frequency (0.3–1 Hz) rTMS over the central facial motor area or a PET-identified hypometabolic zone, 10 workdays, 1,000–1,500 pulses/day:
- Sleep spindle density: 55 → 91 (3 mo) → 147 (6 mo), p=0.002 **[reported]**
- Median SWI: 81% → 68% → 57% (p=0.045, p=0.035) **[reported]**
- Median IQ 72 → 83, and *"improvement correlated significantly with sleep spindle increase (p = 0.035)"* **[reported]**
- *"The mean probability of the sleep spindle coupling in the slow wave 'up' state increased from 28% to 55%"* **[reported]**

n=9, open-label, no control — nowhere near practice-changing. But it's the first study to move a *mechanistic* variable (spindle–slow-wave coupling) and show cognition follow it. If Model B is right, this is what right looks like.

### Treatment strategy in practice

1. Diagnose with sleep EEG; get MRI and genetics going in parallel
2. **Stop any carbamazepine/oxcarbazepine/phenytoin/phenobarbital**
3. First-line: corticosteroids (continuous or pulse) and/or high-dose benzodiazepine (clobazam/nocturnal diazepam) — **early**, because duration is the prognostic driver
4. Adjunct/alternative ASMs: levetiracetam, sulthiame, ethosuximide, valproate
5. Genotype-guided adjustment once results return
6. Ketogenic diet or IVIG in refractory cases (weak evidence)
7. Surgery if a resectable structural lesion is driving it
8. Throughout: speech therapy, special education, neuropsychological monitoring, serial sleep EEG to track SWI

**Note the guideline vacuum.** Per the European steroid survey (PMID:40301922), 60 centres in 18 countries, 11 different published steroid regimens, only 7 used as published: *"Steroids are part of the first line therapy of (D)EE-SWAS across Europe, but heterogeneity in formulations, dosages, and regimens persists due to limited guideline availability."* **[reported]**. And per the Seizure 2023 review: *"Uniformity concerning the new definition of EE/DEE-SWAS, guidelines for management and more frequent genetic screening will be needed to guide best practices."* **[reported]**

**Clinical trials:** RESCUE ESES = Dutch Trial Register NL43510.041.13 / **ISRCTN42686094** (note: ISRCTN, not an NCT — your `clinical_trials` block wants NCT IDs, so this one may not fit the standard pattern). No large active NCT-registered interventional trial specific to D/EE-SWAS was identified; GRIN-disorder trials (memantine, L-serine) exist but enroll by gene, not by this syndrome.

---

## 13. Prevention

Short section, honestly assessed.

**Primary prevention:** No means of preventing the syndrome. The genetic cases are overwhelmingly de novo. The one partial lever is **preventing the perinatal brain injuries** (neonatal thalamic hemorrhage/infarction, IVH, HIE) that constitute the commonest structural etiology — i.e. general perinatal and neonatal care quality, not anything syndrome-specific. **No vaccine, no immunization strategy applies.**

**The genuine preventive intervention is avoiding iatrogenic precipitation:** don't put a child with SeLECTS on carbamazepine/oxcarbazepine. Small, cheap, real.

**Secondary prevention (early detection) — this is where the value is:**
- Sleep EEG surveillance in the at-risk groups listed in §10
- Low threshold for sleep EEG in any child with unexplained developmental regression, language loss, or new behavioral deterioration
- Rationale is explicit: because outcome tracks **SWAS duration**, shortening the delay to diagnosis is itself the therapy. Median diagnostic delay is not well quantified — gap.

**Tertiary prevention (limiting damage in diagnosed patients):**
- Early aggressive SWAS suppression
- Serial sleep EEG to confirm suppression and catch relapse
- Serial neuropsychological assessment
- Speech/language therapy and educational support to compensate for what can't be prevented
- Monitor for steroid toxicity during prolonged courses (BP, weight, glucose — 98%/93%/64% of European centres respectively **[reported]**)

**Genetic screening / counselling:**
- No newborn or population screening
- Post-diagnosis genetic counselling for solved cases; recurrence risk usually low (de novo) but **not zero** (germline mosaicism ~1%)
- X-linked *CNKSR2* families need proper carrier counselling — 50% recurrence for sons of carrier mothers
- Prenatal testing / PGT technically available for known familial variants but complicated by **incomplete penetrance and extreme variable expressivity** — a *GRIN2A* variant carrier may be asymptomatic. This is a genuine counselling difficulty and worth recording
- NCIT:C15240 Genetic Counseling

**Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

**Naturally occurring animal disease: none.** There is no reported spontaneous DEE-SWAS analog in companion animals, livestock, or wildlife. I checked OMIA-adjacent literature and found nothing — this is unsurprising, because the diagnosis depends on (a) a sleep EEG and (b) documented loss of *language*, neither of which transfers to veterinary medicine. **Curate as explicitly not applicable rather than leaving blank.**

- **Taxonomy:** NCBITaxon:9606 *Homo sapiens* (only)
- **Breed (VBO):** not applicable
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious)

**Comparative biology / evolutionary conservation:**
- The *molecular* substrate is deeply conserved: NMDA receptor subunits, voltage-gated Na⁺/K⁺/Ca²⁺ channels, and the thalamocortical circuit itself are conserved across mammals. Sleep spindles and slow-wave sleep are present in all mammals studied, and the synaptic homeostasis hypothesis was developed largely in rodents and *Drosophila*
- Orthologs: *Grin2a* (mouse MGI, NCBI Gene 14811), *Cnksr2* (mouse), *Grin2a* (rat, zebrafish *grin2aa/grin2ab*)
- **What does NOT conserve is the phenotype**: the defining clinical feature is *acquired aphasia / language regression*, which has no animal correlate. This is a fundamental **HUMAN_MODEL_MISMATCH** and should be curated as one — models can reproduce the seizures, the sleep-EEG abnormality, and social/vocalization deficits, but never the syndrome's core clinical feature

---

## 15. Model Organisms

### Mouse — the workhorse

***Cnksr2* knockout mouse** (PMID:34580165, J Neurosci 2021):
> "Cnksr2 KO mice have increased seizures, impaired learning and memory, increased levels of anxiety, and loss of ultrasonic vocalizations (USV)." **[reported]**

Follow-up (eNeuro 2025, "The Epilepsy–Aphasia Syndrome Gene, Cnksr2, Plays a Critical Role in the Anterior Cingulate Cortex Mediating Vocal Communication") localized the USV deficit to **excitatory neurons of the anterior cingulate cortex** **[reported]**.

This is the best available model, and the USV loss is the closest thing to a rodent "aphasia" readout that exists. But be careful how you phrase it: mouse ultrasonic vocalization is a social/affective signal, not language. It is *analogous*, not homologous, and that gap is exactly the HUMAN_MODEL_MISMATCH to record.

***Grin2a* mouse models** — heterozygous and null lines exist. The *Grin2a*⁺/⁻ mouse shows changes in prefrontal cortex, insular cortex, superficial cortical layers, and **thalamic reticular nucleus** **[reported]**, which is intriguing given the TRN's role in spindle generation. Caveat: most *Grin2a* mouse work is framed around **schizophrenia**, not epilepsy-aphasia, so the literature is oriented elsewhere and should be read with that in mind.

**Thalamic lesion models:** the "augmenting response" — the pathological frequency-dependent potentiation at the heart of Model A — was originally characterized in cats and rodents after experimental **thalamic ablation** (see PMID:29133062's discussion). These aren't disease models per se, but they're the physiological foundation of the leading mechanistic hypothesis. Worth curating as MODEL_ORGANISM evidence for the mechanism node even though they long predate the syndrome's molecular era.

**Other genetic models available:** *Scn1a*, *Scn2a*, *Scn8a*, *Kcnq2*, *Kcnb1*, *Kcna2*, *Slc6a1*, *Mecp2*, *Arid1b*, *Foxp1*, *Zeb2* mouse lines all exist (MGI, IMPC/KOMP), constitutive and conditional. None were built as DEE-SWAS models; all are DEE models more broadly.

### In vitro

- **Xenopus oocyte and HEK293 two-electrode/patch electrophysiology** — the workhorse for GRIN2A variant functional classification (this is how Strehlow et al. established the LoF/GoF domain split). This is the assay that makes the precision-medicine claim actionable
- **Patient iPSC-derived neurons and cortical organoids** — feasible and being pursued for GRIN and channelopathy genes; nothing published specific to D/EE-SWAS
- **Cellosaurus/ATCC:** no disease-specific cell line

### Model limitations — be explicit

1. **No rodent model reproduces the defining EEG pattern** (near-continuous NREM spike-wave with sleep-state dependence) *together with* regression. This is the single biggest gap
2. **No language phenotype is possible** — the clinical core of the syndrome is untestable in animals
3. **The age-dependent spontaneous remission at puberty** — the syndrome's most distinctive natural-history feature — has no established animal correlate
4. Mouse sleep architecture (polyphasic, much shorter cycles, different spindle characteristics) differs enough that translating slow-wave downscaling findings to a child's overnight EEG requires real caution
5. Most single-gene models were made for a different indication and are studied under different phenotyping batteries

### Research applications the models *do* support

- Variant functional classification → therapeutic stratification (in vitro electrophysiology; strongest translational value)
- Circuit dissection of thalamocortical/TRN contributions
- Sleep-dependent synaptic homeostasis mechanisms
- Preclinical testing of NMDAR blockers/PAMs
- Vocalization/social-communication readouts as a partial language proxy (*Cnksr2*)

### Resources

MGI (`informatics.jax.org`), IMPC, KOMP/EuMMCR, IMSR, RGD, ZFIN, Alliance of Genome Resources, Cellosaurus.

---

## Curation notes for the dismech entry

A few things I'd flag before this goes into `kb/disorders/`:

1. **`disease_term: MONDO:0800501`** is verified and correct. It's a relatively new-ish MONDO term — per the repo's known gotcha, seed **both** `cache/enums/diseaseterm_*.csv` and `cache/mondo/terms.csv` from the local sqlite adapter, in the worktree *and* the primary checkout, or CI will fail with an OLS timeout dressed up as "term not found."

2. **Model this as two subtypes**, not one blob: `DEE-SWAS` and `EE-SWAS`, with `LKS` as a sub-subtype or a distinguishing-feature block under EE-SWAS. The 66%/28% etiologic-yield split and the 49%/8% ID-outcome split are the strongest sub-entity evidence in the literature and they'd be destroyed by lumping.

3. **Existing module conformance candidates:** `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` is a clean fit. The sleep-dependent-downscaling mechanism (Model B) has no existing module and is a plausible future one — it recurs conceptually across DEEs.

4. **Curate the mechanism as competing hypotheses**, not one chain. Model A (thalamocortical disconnection / augmenting response, `status: CANONICAL` for structural cases) and Model B (synaptic homeostasis failure, `CANONICAL` for the encephalopathy) are complementary; the neuroinflammatory/steroid-responsiveness explanation is a genuine `KNOWLEDGE_GAP`.

5. **Three explicit gaps worth `discussions` entries:** (a) the unvalidated SWI threshold (85% vs 50% vs ILAE's deliberate silence); (b) why steroids work, given no confirmed immune mechanism; (c) no disease-specific QoL instrument and no population prevalence/incidence figure.

6. **One `HUMAN_MODEL_MISMATCH`:** the *Cnksr2* USV phenotype as a language proxy. Real, useful, and not the same thing as aphasia.

7. **Evidence discipline:** every `[reported]` quote above needs `just fetch-reference PMID:xxxxx` and a manual substring check before it becomes a `snippet:`. The `[verbatim-verified]` ones came out of full cached text and should survive `validate-references` as-is — and remember the ≥5-word minimum and no square brackets.

---

## Sources

- [ILAE syndrome page: DEE-SWAS / EE-SWAS](https://www.epilepsydiagnosis.org/syndrome/ee-csws-overview.html)
- [Specchio et al., ILAE classification of childhood-onset syndromes, Epilepsia 2022 (PMID:35503717)](https://onlinelibrary.wiley.com/doi/10.1111/epi.17241)
- [Viswanathan et al., Solving the Etiology of D/EE-SWAS, Ann Neurol 2024 (PMID:39096015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11496008/)
- [van Arnhem et al., RESCUE ESES RCT, Lancet Neurol 2024 (PMID:38081201)](https://doi.org/10.1016/S1474-4422(23)00409-X)
- [Leal et al., Anatomical and physiological basis of CSWS after early thalamic lesions, Epilepsy Behav 2018 (PMID:29133062)](https://pubmed.ncbi.nlm.nih.gov/29133062/)
- [Issa NP, Neurobiology of CSWS and Landau-Kleffner syndromes, Pediatr Neurol 2014 (PMID:25160535)](https://pubmed.ncbi.nlm.nih.gov/25160535/)
- [Kravljanac et al., D/EE-SWAS cohort of 50 children, Seizure 2025 (PMID:41076959)](https://www.sciencedirect.com/science/article/abs/pii/S1059131125002651)
- [The genetic landscape of DEE-SWAS, Seizure 2023 (PMID:37352690)](https://www.seizure-journal.com/article/S1059-1311(23)00175-9/fulltext)
- [Expanding the clinical and genetic landscape of (D)EE-SWAS: Turkish cohort, Neurogenetics 2024 (PMID:38388889)](https://pubmed.ncbi.nlm.nih.gov/38388889/)
- [Genetic etiologies of ESES: systematic review (PMID:29976148)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6034250/)
- [Strehlow et al., GRIN2A-related disorders: genotype and functional consequence predict phenotype, Brain 2019 (PMID:30544257)](https://academic.oup.com/brain/article/142/1/80/5240919)
- [Lemke et al., Mutations in GRIN2A cause idiopathic focal epilepsy with rolandic spikes, Nat Genet 2013](https://www.nature.com/articles/ng.2728)
- [CNKSR2-related neurodevelopmental and epilepsy disorder: cohort of 13 families](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281706/)
- [Cnksr2 Loss in Mice Leads to Increased Neural Activity and Behavioral Phenotypes of Epilepsy-Aphasia Syndrome, J Neurosci 2021 (PMID:34580165)](https://www.jneurosci.org/content/41/46/9633)
- [The Epilepsy–Aphasia Syndrome Gene, Cnksr2, Plays a Critical Role in the Anterior Cingulate Cortex, eNeuro 2025](https://www.eneuro.org/content/12/1/ENEURO.0532-24.2024)
- [Singhal & Sullivan, Continuous Spike-Wave during Slow Wave Sleep and Related Conditions, ISRN Neurol 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3929187/)
- [European experience of steroid therapy in (D)EE-SWAS (PMID:40301922)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12039249/)
- [rTMS improves cognition in SeLECTS with ESES via increase of the sleep spindle (PMID:40620003)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12230375/)
- [ESES induced by oxcarbazepine in idiopathic focal epilepsy in childhood (PMID:26415787)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4610762/)
- [Electrical Status Epilepticus in Sleep — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK553167/)
- [De Tiège et al., Insights into psychomotor regression in CSWS from FDG-PET and EEG-fMRI, Epilepsia 2009](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2009.02219.x)
- [Default mode network hypometabolism in epileptic encephalopathies with CSWS, Epilepsy Res 2014](https://www.sciencedirect.com/science/article/abs/pii/S0920121114000886)
- [Successful treatment of a child with EE-SWAS and GRIN2A variant using sulthiame, Cureus 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9996194/)
- [Landau-Kleffner Syndrome: Current Etiopathogenesis and Management](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12135646/)
- [OMIM #245570 — Epilepsy, focal, with speech disorder (FESD)](https://www.omim.org/entry/245570)
- [Treatment of DEE-SWAS — Practical Neurology](https://practicalneurology.com/diseases-diagnoses/epilepsy-seizures/treatment-of-developmentalepileptic-encephalopathy-with-spike-wave-activation-in-sleep/39968/)
- [Orphanet ORPHA:725](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=725&Lng=GB)