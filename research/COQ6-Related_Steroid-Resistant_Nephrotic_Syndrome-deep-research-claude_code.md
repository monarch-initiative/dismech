---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T18:52:26.425700'
end_time: '2026-08-27T18:56:53.518767'
duration_seconds: 267.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: COQ6-Related Steroid-Resistant Nephrotic Syndrome with Sensorineural
    Deafness
  mondo_id: ''
  category: ''
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
  web_search_requests: 12
  num_turns: 25
  total_cost_usd: 1.2081858000000003
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 21
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 8
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COQ6-Related Steroid-Resistant Nephrotic Syndrome with Sensorineural Deafness
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **COQ6-Related Steroid-Resistant Nephrotic Syndrome with Sensorineural Deafness** covering all of the
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

I'll research this rare disorder now, running parallel searches across the key domains.

Let me follow the redirects and fetch additional key sources in parallel.

# COQ6-Related Steroid-Resistant Nephrotic Syndrome with Sensorineural Deafness (Primary Coenzyme Q10 Deficiency-6, COQ10D6): Comprehensive Research Report

## 1. Disease Information

**Overview.** COQ6-related nephrotic syndrome with sensorineural deafness — designated **Primary Coenzyme Q10 Deficiency, Type 6 (COQ10D6)** — is an ultra-rare, autosomal recessive mitochondrial disorder caused by biallelic loss-of-function variants in *COQ6*, a gene required for biosynthesis of coenzyme Q10 (ubiquinone). The disease is defined by the combination of infantile-onset **steroid-resistant nephrotic syndrome (SRNS)** progressing to end-stage renal failure, together with **bilateral sensorineural hearing loss**; a subset of patients also develop optic atrophy and/or neurological involvement. It is one of the few genetic causes of SRNS that is potentially *treatable*, since high-dose CoQ10 (or the analogue idebenone) supplementation can, in a genotype-dependent fashion, halt or reverse disease progression (PMC7358665; GeneReviews NBK410087).

**Key identifiers:**
- **OMIM Gene:** *614647 — COENZYME Q6, MONOOXYGENASE; COQ6 ([omim.org/entry/614647](https://www.omim.org/entry/614647))
- **OMIM Phenotype:** #614650 — COENZYME Q10 DEFICIENCY, PRIMARY, 6 (COQ10D6) ([omim.org/entry/614650](https://omim.org/entry/614650))
- **Orphanet:** ORPHA:280406 — Familial steroid-resistant nephrotic syndrome with sensorineural deafness caused by COQ6 mutations ([orpha.net](https://www.orpha.net/en/disease/gene/COQ6))
- **Gene location:** Chromosome 14q24.3
- **Broader disease group:** Primary Coenzyme Q10 Deficiency (a mitochondrial respiratory-chain disorder), GeneReviews overview NBK410087
- **HGNC:** COQ6 (gene symbol), NM_182480 (reference transcript)

**Synonyms:** COQ10D6; Primary ubiquinone deficiency-6; COQ6 nephropathy; COQ6 glomerulopathy; SRNS-deafness syndrome (COQ6-related); COQ6-associated Coenzyme Q10 deficiency.

**Evidence base:** This is a disease characterized almost entirely from **aggregated case series and individual case reports** in the literature (originally 11–13 patients in the founding 2011 study, with subsequent single-family and small-cohort reports from Turkey, Lebanon, China, Korea, and other populations) rather than large-scale registries or EHR-derived cohorts — reflecting its rarity (fewer than a few dozen molecularly confirmed families reported to date).

---

## 2. Etiology

**Disease Causal Factor:** Monogenic — biallelic (homozygous or compound heterozygous) pathogenic variants in *COQ6*, disrupting a step of the CoQ10 (ubiquinone) biosynthetic pathway. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause; this is a primary genetic mitochondrial disease.

**Genetic risk factors:**
- Homozygous or compound heterozygous loss-of-function or missense *COQ6* variants are causal.
- The founding study (Heeringa et al., 2011, *J Clin Invest*, PMID 21540551) identified **six different COQ6 mutations in 13 individuals from 7 families** by homozygosity mapping, establishing the SRNS+deafness phenotype.
- Reported pathogenic variants across the literature include: p.Gly255Arg, p.Ala353Asp (c.1058C>A), p.Arg360Trp (c.1078C>T), c.804delC (frameshift), p.Trp14Ter (c.41G>A, nonsense), p.Tyr83Ter (c.249C>G, nonsense), p.Gln461Ter (c.1381C>T), c.189_191delGAA (p.Lys64del), p.Arg162Ter (c.484C>T), p.Gln229Pro (c.686A>C), and p.Pro261Leu (c.782C>T).
- ClinVar currently lists 307 reported *COQ6* variants, of which 32 alleles are classified pathogenic and 12 likely pathogenic (MARRVEL/ClinVar aggregate, accessed via [marrvel.org/human/gene/51004](https://marrvel.org/human/gene/51004)).
- All missense variants identified in disease cohorts are predicted damaging by PolyPhen2/SIFT; all premature-stop, frameshift, or splice variants are predicted high-confidence loss-of-function (*Sci Rep* 2017, DOI 10.1038/s41598-017-17564-y).
- **Possible genetic modifiers:** a 2026 review (Wiley MGG 2026, DOI 10.1002/mgg3.70221) notes that among siblings carrying the same *COQ6* variant, co-inheritance of a *COQ8B* p.(Arg174)/p.(His174) polymorphism was associated with differing severity of renal involvement, suggesting *COQ8B* may act as a phenotypic modifier of *COQ6* disease.
- No environmental risk factors, occupational exposures, or infectious triggers have been identified — this is a purely Mendelian condition.

**Protective factors:** None identified beyond therapeutic CoQ10/idebenone supplementation (see Treatment, §12), which is disease-modifying rather than truly "protective" in a population-genetics sense. No protective alleles have been described.

**Gene-environment interactions:** Not established; the phenotype is driven by the biosynthetic enzyme defect itself, and no environmental modifier of expressivity has been reported.

---

## 3. Phenotypes

### Renal phenotype (defining feature)
- **Steroid-resistant nephrotic syndrome (SRNS)**: proteinuria at a median age of onset **1.2 years** (range 0.2–6.4 years) in the original cohort (PMC7358665, summarizing Heeringa et al. 2011). Median progression to **end-stage renal failure (ESRF) at 1.7 years** (range 0.4–9.3 years).
- **Renal biopsy**: focal segmental glomerulosclerosis (FSGS) is the most common histologic finding; diffuse mesangial sclerosis has also been reported.
- Suggested HP terms: **HP:0000100** (Nephrotic syndrome), **HP:0000097** (Focal segmental glomerulosclerosis), **HP:0000093** (Proteinuria), **HP:0003774** / **HP:0000083** (Stage 5 chronic kidney disease / Renal insufficiency), **HP:0000822** (Hypertension, in some patients).

### Auditory phenotype (defining feature)
- **Bilateral sensorineural hearing loss (SNHL)**, typically diagnosed between ages 4–6 years in reported cases, though age of onset is variable and it can be congenital in more severe genotypes.
- Suggested HP term: **HP:0000407** (Sensorineural hearing impairment).
- A Korean cohort study (PMC9482153) of 12 patients found the response rate to CoQ10 (no further hearing loss or improvement) was **42.9%** among 7 patients with >1 year of serial audiograms; genotype strongly predicted response (see §12).

### Ophthalmologic phenotype (variable)
- **Optic atrophy**, papilledema, and progressive visual loss have been reported in a subset of patients (e.g., visual acuity 20/200 at age 17 in one case, improving to 20/25+ after 3 years of idebenone; PMC7358665).
- Suggested HP terms: **HP:0000648** (Optic atrophy), **HP:0001622** (Premature birth — not typical), **HP:0000587** (Bilateral cataracts — not typical here).

### Neurological/systemic phenotype (severe/lethal cases only)
- In the most severe (lethal infantile) presentations: severe metabolic acidosis (lactate up to 7.8 mmol/L), seizures, muscle hypotonia, growth retardation, delayed white matter myelination, bifrontal subarachnoid space widening, atrial septal defect, and pulmonary hypertension — death occurring before 6 months of age in the reported family (PMC8802230).
- Suggested HP terms: **HP:0001250** (Seizure), **HP:0001943** (Hypoglycemia, not directly reported but common in mitochondrial disease), **HP:0002151** (Increased serum lactate), **HP:0001252** (Hypotonia), **HP:0001510** (Growth delay), **HP:0006530** (Interstitial pulmonary disease — n/a), **HP:0001631** (Atrial septal defect), **HP:0002092** (Pulmonary hypertension).

### Phenotype variability and severity spectrum
Clinical severity ranges widely: from isolated, slowly progressive SRNS+SNHL surviving into adulthood, to a lethal infantile multisystem mitochondrial disease with cardiac, neurological, and metabolic involvement dying within months. Even siblings sharing the identical *COQ6* genotype can show markedly different renal-phenotype severity (ScienceDirect, "Two siblings with variable expressivity of the renal phenotype"), consistent with modifier effects and/or stochastic factors.

### Quality of life impact
No disease-specific QoL instrument data were found in the literature searched; QoL burden is inferable from the combination of ESRD (dialysis/transplant dependency), profound hearing loss (often requiring cochlear implantation), and, in some patients, progressive visual impairment — a multisensory and renal-replacement burden concentrated in early childhood.

---

## 4. Genetic/Molecular Information

**Causal gene:** *COQ6* (OMIM *614647), chromosome 14q24.3.

**Protein:** Coenzyme Q6, monooxygenase — a mitochondrial **FAD-dependent monooxygenase** of the UbiH/COQ6 family. Two isoforms are described: isoform A (468 aa, ~54 kDa, with an N-terminal mitochondrial targeting leader peptide) and isoform B (~51 kDa, lacking the leader peptide). The protein carries three FAD-binding motifs and catalyzes **C5-ring hydroxylation** in ubiquinone biosynthesis — specifically the conversion of 3-polyprenyl-4-hydroxybenzoic acid to 3-polyprenyl-4,5-dihydroxybenzoic acid (GeneCards/Wikipedia COQ6; PMC4726752, "Substrate Access Channel in the FAD-Dependent Monooxygenase Coq6"). Human COQ6 shares 66% sequence identity with zebrafish Coq6 and 33% with the *E. coli* ortholog UbiH, indicating deep evolutionary conservation of this biosynthetic step.

**Variant classification and types:** Reported pathogenic variants span missense (e.g., p.Ala353Asp, p.Arg360Trp, p.Gly255Arg, p.Gln229Pro, p.Pro261Leu), nonsense (p.Trp14Ter, p.Tyr83Ter, p.Gln461Ter, p.Arg162Ter), and small in-frame/frameshift deletions (c.189_191delGAA/p.Lys64del, c.804delC). All are classified via ACMG/AMP criteria on ClinVar (32 pathogenic, 12 likely pathogenic alleles of 307 total reported variants).

**Allele frequency:** Individually rare (gnomAD-derived global allele frequencies for ubiquinone-pathway pathogenic variants collectively range 4.1×10⁻⁶–1.7×10⁻⁴, combined ≈1.76×10⁻³ across all CoQ-biosynthesis genes; *Sci Rep* 2017, DOI 10.1038/s41598-017-17564-y). No *COQ6*-specific founder allele frequency was identified, though clusters of cases have been reported from Turkish, Lebanese, Chinese, and Korean cohorts, suggesting possible regional enrichment of specific alleles without confirmed founder-effect data in the literature reviewed.

**Origin:** Germline, autosomal recessive — no somatic *COQ6* variants are implicated in this disease.

**Functional consequences:** Loss-of-function (nonsense/frameshift alleles) or hypomorphic/damaging missense variants reduce COQ6 monooxygenase activity, impairing CoQ10 biosynthesis (a "loss of function" mechanism rather than dominant-negative or gain-of-function). Functional impact category: `LOSS_OF_FUNCTION` (nonsense/frameshift) or `PARTIAL_LOSS_OF_FUNCTION` (hypomorphic missense with residual, genotype-dependent enzymatic activity — consistent with the graded CoQ10-treatment response by genotype).

**Modifier genes:** *COQ8B* polymorphism (p.Arg174/His174) proposed as a phenotype modifier in siblings sharing an identical *COQ6* genotype (Wiley MGG 2026 review).

**Epigenetic/chromosomal information:** No epigenetic regulation or chromosomal-abnormality mechanism has been reported for this disease; it is driven purely by coding-sequence variants in *COQ6*.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors have been identified in the literature. This is a monogenic mitochondrial biosynthetic disorder; disease expression is not modulated by toxin exposure, diet (beyond therapeutic CoQ10 supplementation, which is a treatment rather than a preventive environmental factor), or infectious agents. This section is therefore not applicable beyond noting the absence of such associations.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular defect:** Biallelic pathogenic *COQ6* variants → loss/reduction of COQ6 FAD-dependent monooxygenase activity → failure of the C5-ring hydroxylation step of ubiquinone (CoQ10) biosynthesis.
2. **Biochemical consequence:** Reduced cellular/tissue CoQ10 levels. GeneReviews (NBK410087) documents "reduced levels of CoQ10 in skeletal muscle" and "reduced activities of complex I+III and II+III of the mitochondrial respiratory chain" in affected patients — since CoQ10 is the mobile electron carrier shuttling electrons from Complexes I and II to Complex III.
3. **Mitochondrial dysfunction:** Impaired electron transport chain flux → decreased oxidative phosphorylation/ATP generation and, critically, loss of CoQ10's antioxidant function in the inner mitochondrial membrane.
4. **Oxidative stress:** In podocyte and zebrafish knockdown models, *Coq6* deficiency significantly increased reactive oxygen species (ROS), demonstrated by MitoSOX staining (PMC6247592).
5. **Cytoskeletal/structural podocyte injury:** ROS-driven damage reduces F-actin expression (with irregular distribution) and decreases nephrin expression, compromising the slit-diaphragm/cytoskeletal integrity essential to the glomerular filtration barrier.
6. **Apoptosis:** Increased active caspase-3 and caspase-9 (intrinsic mitochondrial apoptotic pathway) documented by flow cytometry and western blot in *Coq6*-knockdown mouse podocyte cell lines (PMC6247592; original JCI paper PMID 21540551).
7. **Clinical/histologic outcome — kidney:** Podocyte loss and dysfunction manifest as proteinuria/nephrotic syndrome, progressing histologically to FSGS or diffuse mesangial sclerosis and clinically to ESRF.
8. **Clinical outcome — cochlea/eye/CNS:** Analogous CoQ10-deficiency-driven oxidative/bioenergetic injury is presumed to underlie sensorineural hearing loss (cochlear hair cells are highly energy-dependent) and optic atrophy/neurologic disease in more severe genotypes, though the cochlear and optic mechanisms are less directly modeled experimentally than the podocyte pathway.

**Cell types involved:** Podocytes (kidney glomerular visceral epithelial cells) are the best-characterized cellular site of injury (Cell Ontology: **CL:0000653**, podocyte). Cochlear hair cells and the auditory pathway are presumed targets for SNHL; retinal ganglion cells/optic nerve for optic atrophy.

**Key pathway/process annotations (suggested GO terms):**
- **GO:0006744** — ubiquinone biosynthetic process (upstream defective pathway)
- **GO:0016709** — oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor and incorporation of one atom of oxygen (COQ6 monooxygenase activity)
- **GO:0055114** — oxidation-reduction process
- **GO:0006979** — response to oxidative stress
- **GO:0006915** — apoptotic process
- **GO:0030036** — actin cytoskeleton organization (F-actin/podocyte cytoskeletal injury)
- **GO:0022900** — electron transport chain

**Biochemical abnormalities:** Reduced tissue CoQ10; reduced mitochondrial respiratory chain complex I+III and II+III activity (measurable in muscle biopsy or cultured fibroblasts) — the biochemical diagnostic correlate of the genetic defect.

**Molecular profiling:** No large-scale transcriptomic, proteomic, or single-cell datasets specific to human COQ6-deficient kidney/cochlear tissue were identified in this search; mechanistic data derive principally from candidate-gene knockdown studies (siRNA in mouse podocyte cell lines; morpholino knockdown in zebrafish embryos), not from unbiased omics profiling of patient tissue.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Kidney (glomerulus/podocytes) — nephrotic syndrome, FSGS; Inner ear (cochlea) — sensorineural hearing loss.
- **Secondary:** Eye (optic nerve) — optic atrophy in a subset; in severe infantile cases, heart (atrial septal defect, pulmonary hypertension) and central nervous system (seizures, delayed white matter myelination).
- **Body systems:** Renal/urinary system (primary), auditory system (primary), visual system (secondary), cardiovascular and central nervous systems (secondary, severe cases only).

**Tissue/cell level:**
- Glomerular visceral epithelial cells (podocytes), **CL:0000653**.
- Cochlear hair cells / spiral ganglion neurons (inferred target, not directly demonstrated at single-cell resolution in the literature reviewed).
- Retinal ganglion cells / optic nerve axons (optic atrophy).

**Subcellular level:** Mitochondria — specifically the **inner mitochondrial membrane**, site of CoQ10's electron-shuttling and antioxidant functions (GO Cellular Component: **GO:0005743**, mitochondrial inner membrane; **GO:0005739**, mitochondrion).

**Localization (UBERON terms, suggested):**
- **UBERON:0001225** — renal glomerulus
- **UBERON:0002113** — kidney
- **UBERON:0000959** — cochlea (auditory system)
- **UBERON:0001784** — optic nerve
- **UBERON:0000948** — heart (atrial septal defect in severe cases)

**Laterality:** Renal disease is systemic/bilateral (both kidneys); sensorineural hearing loss and optic atrophy are typically **bilateral**.

---

## 8. Temporal Development

**Onset:** Congenital-to-infantile in most reported cases. Proteinuria/nephrotic syndrome onset at a median age of **1.2 years** (range 0.2–6.4 years); the most severe (lethal) cases present within the first months of life (3–5 months in the reported lethal sibling pair). Sensorineural hearing loss is typically identified in early childhood (age 4–6 years in several reports), though it can be congenital in severe genotypes.

**Onset pattern:** Generally insidious/subacute for the renal and auditory phenotypes; acute and rapidly fulminant in the lethal infantile multisystem presentations (metabolic acidosis, seizures, cardiac involvement within weeks to months).

**Progression:**
- **Renal:** progresses from proteinuria → steroid-resistant nephrotic syndrome → FSGS on biopsy → ESRF, with median time to ESRF of **1.7 years** (range 0.4–9.3 years) in the original cohort. Progression is not universal or inevitable in all genotypes when CoQ10 treatment is initiated promptly (see Treatment).
- **Auditory:** progressive in genotype-dependent fashion; some genotypes show ongoing threshold deterioration despite treatment (mean shift +24.1 dB in "non-responders"), others remain stable or even improve (mean shift −5.4 dB in "responders") (PMC9482153).
- **Ophthalmologic:** progressive optic atrophy/visual loss reported in adolescence in some patients, partially reversible with idebenone.
- **Course pattern:** Predominantly progressive, though CoQ10/idebenone therapy can achieve durable remission of proteinuria (sustained ≥12 months in one well-documented case, PMC6208703) and stabilization or improvement of hearing/vision in a genotype-dependent subset — making this a rare example of a "modifiable progressive" course among genetic SRNS syndromes.
- **Duration:** Chronic, lifelong for survivors (renal replacement therapy/transplant, hearing aids/cochlear implants); the most severe infantile-onset multisystem form is fatal within the first year of life.

**Remission patterns:** Treatment-induced remission of nephrotic-range proteinuria has been documented with CoQ10 supplementation (complete remission within 1 month of initiating 30 mg/kg/day CoQ10 in one case, sustained to at least 12-month follow-up; PMC6208703). No spontaneous remission has been reported.

**Critical periods:** Early diagnosis and prompt initiation of CoQ10/idebenone therapy — ideally before irreversible glomerular scarring, cochlear damage, or optic nerve injury has occurred — is repeatedly emphasized in the literature as the key window for effective intervention ("Early recognition of this genetic SRNS is mandatory since... can be avoided by adequate treatment based on CoQ10 supplement or an analogue," PMC7358665).

---

## 9. Inheritance and Population

**Epidemiology:** COQ10D6 is ultra-rare; only a few dozen molecularly confirmed cases/families have been reported worldwide since the disease was first delineated in 2011. The broader category of primary CoQ10 deficiency (all 10+ causal genes combined) has an estimated overall incidence of **<1:100,000** (GeneReviews NBK410087). No disease-specific prevalence/incidence estimate isolated to *COQ6* was found; it should be regarded as one of the rarer genetic subtypes within this already-rare disease group.

**Inheritance pattern:** **Autosomal recessive.** At-risk siblings of an affected individual have a 25% recurrence risk when both parents are heterozygous carriers; heterozygous carriers are asymptomatic (GeneReviews NBK410087).

**Penetrance:** Appears fully penetrant for the core renal phenotype among individuals carrying two pathogenic alleles, though severity (age of onset, rate of progression, extrarenal involvement) is highly variable — including divergent severity between siblings sharing the identical genotype, implicating modifier loci (e.g., *COQ8B*) and/or environmental/stochastic factors.

**Expressivity:** Markedly **variable** — spanning isolated, slowly progressive SRNS+SNHL to lethal infantile multisystem mitochondrial disease, even within the same family/genotype.

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed for *COQ6*.

**Founder effects/consanguinity:** The original discovery cohort was identified via **homozygosity mapping**, implying at least some families were consanguineous; case series have originated from Turkish, Lebanese, Chinese, and Korean populations, suggesting the disease is not confined to a single ethnic group, though no single well-characterized founder allele with quantified frequency was identified in this search.

**Carrier frequency:** Not specifically reported for *COQ6* alone; aggregate carrier/allele-frequency data for CoQ-biosynthesis-pathway pathogenic variants collectively (441 carriers identified across genes in gnomAD) yield a combined pathogenic allele frequency of ~1.76×10⁻³ (*Sci Rep* 2017).

**Population demographics:** Reported cases span multiple ethnicities (Turkish, Lebanese, Chinese, Korean, and others); no strong sex predilection has been reported (autosomal recessive inheritance predicts equal sex distribution). Age distribution of affected individuals is concentrated in infancy/early childhood at diagnosis, consistent with the disease's early onset.

---

## 10. Diagnostics

**Laboratory/clinical tests:**
- Urinalysis for proteinuria (nephrotic-range), serum albumin, creatinine/eGFR for renal function staging.
- Serum/plasma lactate (elevated in severe multisystem presentations, e.g., 5.4–7.8 mmol/L in the lethal sibling case).
- Renal biopsy with light and electron microscopy: FSGS or diffuse mesangial sclerosis pattern.
- **Biochemical CoQ10 assay:** reduced CoQ10 levels measurable in skeletal muscle biopsy (the gold-standard tissue) or cultured skin fibroblasts; reduced mitochondrial respiratory chain complex I+III and II+III activities support the diagnosis (GeneReviews NBK410087).

**Genetic testing:**
- **Molecular genetic testing is the primary diagnostic approach.** Recommended strategies per GeneReviews: multigene panels targeting steroid-resistant nephrotic syndrome, mitochondrial disorders, or ataxia gene panels; or exome/genome sequencing for comprehensive assessment, using sequence analysis plus deletion/duplication analysis of *COQ6*.
- Historically, homozygosity mapping was used in consanguineous families to localize the causal locus (original 2011 discovery cohort).
- Single-gene *COQ6* Sanger sequencing is an option when the phenotype (SRNS + SNHL) is highly suggestive.

**Audiological testing:** Serial pure-tone audiometry is recommended for surveillance and to monitor treatment response; Categorical Auditory Performance (CAP) scoring is used post-cochlear-implantation.

**Ophthalmologic testing:** Formal ophthalmologic evaluation (visual acuity, fundoscopy for optic atrophy/papilledema) is recommended, especially in patients on long-term follow-up.

**Differential diagnosis:** Other genetic causes of SRNS (e.g., *NPHS1*, *NPHS2*, *WT1*, *COQ2*, **COQ8B** [note: COQ8B nephropathy is a closely related, better-characterized CoQ-pathway SRNS disorder, also CoQ10-responsive, but classically without deafness]), other mitochondrial CoQ10 deficiency subtypes (COQ2, COQ4, COQ7, COQ8A, COQ8B, COQ9, PDSS1, PDSS2, ADCK3/4), and syndromic deafness-nephropathy conditions (e.g., Alport syndrome — differentiated by lack of hematuria/lens abnormalities typical of Alport, and by biochemical/molecular confirmation of the CoQ pathway defect).

**Screening:** No population-based newborn or carrier screening program specific to *COQ6* was identified; given its rarity, targeted carrier screening would typically only be pursued in families with a known proband or in consanguineous unions with a positive family history.

---

## 11. Outcome / Prognosis

**Survival/mortality:** Highly variable by genotype and treatment timing. Without treatment, the disease inexorably progresses to ESRF (median age 1.7 years in the founding cohort), and the most severe genotypes are **lethal in infancy** (reported deaths at 4–6 months of age in a compound-heterozygous nonsense-variant sibling pair, PMC8802230). In the original 11-patient cohort referenced by later reports, "five [were] dying in early childhood (median age: 5.0 years)" — indicating substantial early mortality historically, prior to widespread recognition of CoQ10-treatment responsiveness.

**Morbidity/function:** Survivors face ESRD requiring dialysis and/or renal transplantation, profound bilateral sensorineural hearing loss frequently requiring cochlear implantation, and in some cases progressive visual impairment. No formal QoL instrument data (EQ-5D, SF-36) specific to this condition were found.

**Complications:** ESRD, hypertension, growth retardation, and — in the most severe multisystem cases — cardiac defects (atrial septal defect, pulmonary hypertension), seizures, and CNS white-matter abnormalities.

**Recovery potential with treatment:** This is the most distinctive feature of the prognosis — early, appropriately dosed CoQ10 (or idebenone) treatment can produce complete and sustained remission of proteinuria (documented to ≥12 months follow-up), stabilization or improvement in visual acuity (idebenone), and — in a genotype-dependent subset (~43% response rate for stable/improved hearing in one cohort) — preservation of hearing.

**Prognostic factors:**
- **Genotype is the dominant prognostic variable.** Homozygosity for p.Gly255Arg or p.Ala353Asp was associated with good CoQ10 response (GeneReviews). Conversely, c.686A>C (p.Gln229Pro) was associated with poor audiological response, while c.189_191delGAA and c.782C>T were associated with better audiological outcomes (PMC9482153); a patient homozygous for p.Pro261Leu (c.782C>T) maintained entirely normal hearing throughout follow-up.
- **Timing of diagnosis/treatment initiation** relative to onset of irreversible organ damage is repeatedly cited as critical.
- Compound heterozygous truncating (nonsense) variants appear to correlate with the most severe, multisystem, and lethal presentations.

---

## 12. Treatment

**Pharmacotherapy (targeted, disease-modifying):**
- **Coenzyme Q10 (ubiquinone-10) oral supplementation** is the cornerstone treatment. Doses reported in the literature range from **5–50 mg/kg/day** (GeneReviews range), with **30 mg/kg/day** (in three divided doses) used in several published cohorts/case reports (PMC9482153; PMC6208703; PMC6247592). CHEBI term: **CHEBI:46245** (ubiquinone-10 / coenzyme Q10). NCIT treatment-action term: **NCIT:C15986** (Pharmacotherapy), with `therapeutic_agent` = coenzyme Q10 (CHEBI:46245); modality classification: `SMALL_MOLECULE` (or arguably `PROTEIN_REPLACEMENT`-adjacent "metabolite replacement," though CoQ10 itself is a lipophilic small molecule).
- **Idebenone**, a hydrophilic short-chain synthetic CoQ10 analogue with improved bioavailability/tissue penetration, has been used successfully particularly for the ophthalmologic (optic atrophy) manifestation, at doses of **10–15 mg/kg/day** (PMC7358665). CHEBI term: **CHEBI:81816** (idebenone).
- Prior to CoQ10/idebenone diagnosis, patients are frequently trialed unsuccessfully on standard nephrotic-syndrome immunosuppression — **prednisone/corticosteroids** (ineffective, consistent with the "steroid-resistant" designation), **ACE inhibitors/ARBs** (e.g., ramipril; supportive antiproteinuric effect only), and **calcineurin inhibitors** (e.g., cyclosporine A, achieving only partial remission in one reported case before CoQ10 achieved complete remission) (PMC6208703; PMC7358665).

**Pharmacogenomics:** Treatment response to CoQ10/idebenone is strongly genotype-dependent (see §11), representing an emerging genotype-guided precision-medicine approach within this single-gene disease, though no formal CPIC/PharmGKB guideline exists given the disease's rarity.

**Renal replacement/surgical:**
- **Renal transplantation** (NCIT:C15289, Organ Transplantation) and **dialysis/hemodialysis** for patients progressing to ESRF despite treatment.

**Auditory intervention:**
- **Cochlear implantation** for patients with severe/progressive sensorineural hearing loss unresponsive to CoQ10; a case series of 4 implanted patients showed Categorical Auditory Performance (CAP) scores improving from an average of 3.2 preoperatively to 6.7 at final follow-up, sustained over an average 61.9 months (PMC9482153).
- Hearing aids for milder hearing loss (inferred standard-of-care, not specifically detailed in sources reviewed).

**Supportive care:** Nutritional support/growth monitoring (accelerated growth was noted as a positive secondary outcome of successful CoQ10 treatment in one case report, alongside improved dental health and reduced respiratory infections — PMC6208703), blood pressure management, and general chronic kidney disease supportive management.

**Experimental/investigational:** No *COQ6*-specific registered clinical trials were identified on ClinicalTrials.gov. General CoQ10-in-CKD trials exist (e.g., NCT03579693, NCT05942027) but target broader chronic kidney disease populations, not the COQ6-specific genetic subtype, and used much higher, non-weight-based adult dosing (1,200 mg/day) without disease-specific benefit in short-term endpoints — underscoring that the genetically targeted, weight-based dosing paradigm used in *COQ6* case reports is distinct from generic CoQ10-for-CKD approaches.

**Treatment outcomes/adverse events:** No significant CoQ10-related adverse events were reported in the case series reviewed; the main "failure mode" is incomplete or absent response in genotypes with more severe loss-of-function variants, and interestingly, one report noted that **serum CoQ10 levels remained variable despite consistent dosing and clinical improvement**, suggesting the therapeutic effect may act locally at the tissue level rather than being reliably tracked by serum levels (PMC6208703).

**Treatment strategy summary:** Early genetic diagnosis → immediate high-dose oral CoQ10 (and/or idebenone, particularly if optic involvement) → serial monitoring of proteinuria, audiometry, and visual acuity → escalation to cochlear implantation for non-responsive hearing loss and renal replacement therapy/transplantation for those progressing to ESRF despite treatment.

---

## 13. Prevention

**Primary prevention:** None possible for the genetic defect itself (autosomal recessive Mendelian disease); the only "primary prevention" analog is reproductive genetic counseling and prenatal/preimplantation genetic testing in families with a known proband, given the 25% recurrence risk to future siblings.

**Secondary prevention (early detection):** This is where intervention is most impactful for this disease — early recognition of the SRNS + SNHL phenotype (or a positive family history) and prompt genetic diagnosis enables initiation of CoQ10/idebenone therapy **before irreversible glomerular, cochlear, or optic nerve damage occurs**, which the literature repeatedly frames as the key modifiable determinant of outcome.

**Genetic counseling:** Standard autosomal recessive counseling applies — carrier parents have a 25% risk per pregnancy of an affected child; carrier testing of at-risk relatives and prenatal diagnosis are options once the familial pathogenic variants are known (GeneReviews NBK410087).

**Screening:** No population-level newborn or carrier screening program specific to *COQ6* exists; targeted testing is reserved for families with an identified proband, given the disease's extreme rarity.

**Public health/environmental interventions:** Not applicable — this is not a disease with an environmental or public-health prevention dimension.

**Prophylaxis:** Continuous CoQ10 supplementation functions as ongoing secondary/tertiary prophylaxis against further nephron loss, hearing deterioration, and optic nerve injury once diagnosis is established, rather than as a true "primary preventive" measure.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease caused by *Coq6* mutations has been reported in the literature searched (e.g., no OMIA entries or veterinary case series were identified). The *Coq6* gene is broadly conserved across vertebrates (mouse ortholog: MGI:1924408; zebrafish ortholog: 66% identity to human COQ6). No zoonotic or cross-species transmission relevance applies, as this is a non-infectious, purely genetic disease.

**Comparative biology:** The deep evolutionary conservation of the ubiquinone biosynthesis pathway — from the bacterial *E. coli* ortholog UbiH (33% identity to human COQ6) through zebrafish (66% identity) — underlies why zebrafish and mouse-cell models have proven experimentally tractable despite the absence of documented spontaneous natural disease in non-human species.

---

## 15. Model Organisms

**Cellular/in vitro models:**
- **Mouse podocyte cell line, siRNA knockdown of Coq6:** Decreased cell growth, increased apoptosis (increased caspase-3 and caspase-9 activation), increased ROS (via MitoSOX staining), reduced F-actin expression with cytoskeletal disorganization, and reduced nephrin expression. **CoQ10 treatment partially reversed the apoptotic phenotype** in knockdown podocytes (PMID 21540551; PMC6247592). Notably, exogenously expressed human COQ6 isoform A localized correctly to mitochondria when transfected into mouse podocyte cell lines, functionally validating the mitochondrial targeting/localization predicted from the protein's leader-peptide sequence.

**Zebrafish model:**
- **Morpholino knockdown of zebrafish coq6:** Induced apoptosis preferentially in the head and trunk of embryos, **partially rescued by co-treatment with CoQ10** (original JCI discovery paper, PMID 21540551). This in vivo functional assay was used to validate candidate variant pathogenicity identified by human homozygosity mapping — a standard approach for genes mutated in human renal-disease patients, given the zebrafish's established utility for studying podocyte biology and glomerular filtration barrier development.

**Model characteristics — recapitulation and limitations:**
- Both the mouse-podocyte and zebrafish knockdown models **recapitulate** the core cellular pathology (apoptosis, oxidative stress) and, importantly, **recapitulate CoQ10 treatment responsiveness**, making them directly relevant translational models supporting the clinical use of CoQ10 supplementation.
- Neither model is reported to recapitulate the sensorineural hearing loss or optic atrophy components of the human phenotype — the auditory and ophthalmologic aspects of disease remain modeled only indirectly (by analogy to the shared mitochondrial/oxidative-stress mechanism), which represents a **translational gap**: no cochlear or optic-nerve-specific *Coq6* animal or cellular model was identified in this search. A curator populating a knowledge-base entry may wish to flag this using a `HUMAN_MODEL_MISMATCH`-type discussion, since fidelity of the podocyte models to human renal disease is well-supported (RECAPITULATES) but no equivalent auditory/ophthalmologic model exists to assess fidelity for those organ systems.
- No germline mouse knockout (constitutive *Coq6*-null) model with a full multisystem phenotype (analogous to the human lethal infantile form) was identified in this search; existing genetic-model resources are limited to the MGI gene record (**MGI:1924408**) without a described knockout-phenotype allele series specific to nephrotic/deafness phenotyping.

**Research applications:** These models have been used specifically to (1) establish causality of candidate human *COQ6* variants via functional rescue experiments, (2) dissect the oxidative-stress/apoptosis mechanism of podocyte injury, and (3) provide preclinical justification for CoQ10 supplementation as a targeted, genotype-informed therapy — directly informing the clinical treatment paradigm described in §12.

---

## Ontology Term Summary for KB Curation

| Category | Suggested terms |
|---|---|
| Disease/gene identifiers | OMIM:614650 (phenotype), OMIM:614647 (gene), Orphanet ORPHA:280406, HGNC COQ6 |
| Phenotypes (HP) | HP:0000100 (Nephrotic syndrome), HP:0000097 (FSGS), HP:0000093 (Proteinuria), HP:0000083 (Renal insufficiency), HP:0000407 (Sensorineural hearing impairment), HP:0000648 (Optic atrophy), HP:0001250 (Seizure), HP:0002151 (Increased serum lactate), HP:0001252 (Hypotonia), HP:0001510 (Growth delay), HP:0001631 (Atrial septal defect), HP:0002092 (Pulmonary hypertension), HP:0000822 (Hypertension) |
| Cell types (CL) | CL:0000653 (podocyte) |
| Anatomy (UBERON) | UBERON:0002113 (kidney), UBERON:0001225 (renal glomerulus), UBERON:0000959 (cochlea), UBERON:0001784 (optic nerve), UBERON:0000948 (heart) |
| Biological process (GO) | GO:0006744 (ubiquinone biosynthetic process), GO:0016709 (FAD monooxygenase activity, relevant catalytic class), GO:0055114 (oxidation-reduction process), GO:0006979 (response to oxidative stress), GO:0006915 (apoptotic process), GO:0030036 (actin cytoskeleton organization) |
| Chemicals (CHEBI) | CHEBI:46245 (ubiquinone-10 / coenzyme Q10), CHEBI:81816 (idebenone) |
| Treatments (NCIT) | NCIT:C15986 (Pharmacotherapy), NCIT:C15289 (Organ Transplantation — renal transplant), NCIT:C15305-class hemodialysis term |

---

## Key Citations

- Heeringa SF et al. **COQ6 mutations in human patients produce nephrotic syndrome with sensorineural deafness.** *J Clin Invest.* 2011. PMID: [21540551](https://pubmed.ncbi.nlm.nih.gov/21540551/); [JCI full text](https://www.jci.org/articles/view/45693)
- **COQ6 mutation in patients with nephrotic syndrome, sensorineural deafness, and optic atrophy.** PMID: [32685349](https://pubmed.ncbi.nlm.nih.gov/32685349/); [PMC7358665](https://pmc.ncbi.nlm.nih.gov/articles/PMC7358665/)
- **Effects of CoQ10 Replacement Therapy on the Audiological Characteristics of Pediatric Patients with COQ6 Variants.** [PMC9482153](https://pmc.ncbi.nlm.nih.gov/articles/PMC9482153/)
- **A Family Segregating Lethal Primary Coenzyme Q10 Deficiency Due to Two Novel COQ6 Variants.** [PMC8802230](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8802230/)
- **New Mutation of Coenzyme Q10 Monooxygenase 6 Causing Podocyte Injury in a Focal Segmental Glomerulosclerosis Patient.** [PMC6247592](https://pmc.ncbi.nlm.nih.gov/articles/PMC6247592/); DOI: [10.4103/0366-6999.245158](https://doi.org/10.4103/0366-6999.245158)
- **CoQ10-related sustained remission of proteinuria in a child with COQ6 glomerulopathy—a case report.** [PMC6208703](https://pmc.ncbi.nlm.nih.gov/articles/PMC6208703/)
- **Primary coenzyme Q10 Deficiency-6 (COQ10D6): Two siblings with variable expressivity of the renal phenotype.** [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1769721218303288)
- OMIM: [*614647 — COQ6](https://www.omim.org/entry/614647); [#614650 — COQ10D6](https://omim.org/entry/614650)
- Orphanet: [COQ6 gene page](https://www.orpha.net/en/disease/gene/COQ6) (ORPHA:280406)
- GeneReviews: **Primary Coenzyme Q10 Deficiency Overview.** [NBK410087](https://www.ncbi.nlm.nih.gov/books/NBK410087/)
- MedlinePlus Genetics: [COQ6 gene](https://medlineplus.gov/genetics/gene/coq6/)
- Coenzyme Q Biosynthesis: Evidence for a Substrate Access Channel in the FAD-Dependent Monooxygenase Coq6. [PMC4726752](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4726752/)
- Estimating the occurrence of primary ubiquinone deficiency by analysis of large-scale sequencing data. *Sci Rep.* 2017. DOI: [10.1038/s41598-017-17564-y](https://www.nature.com/articles/s41598-017-17564-y)
- COQ2‐Associated Primary Coenzyme Q10 Deficiency Presenting With Proteinuria: A Case Report and Literature Review (context review discussing COQ6 modifier data). *Mol Genet Genomic Med.* 2026. DOI: [10.1002/mgg3.70221](https://onlinelibrary.wiley.com/doi/10.1002/mgg3.70221)
- MARRVEL COQ6 gene aggregate (ClinVar variant counts): [marrvel.org/human/gene/51004](https://marrvel.org/human/gene/51004)
- GeneCards: [COQ6](https://www.genecards.org/cgi-bin/carddisp.pl?gene=COQ6); MGI: [Coq6 mouse gene](https://www.informatics.jax.org/marker/MGI:1924408)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.