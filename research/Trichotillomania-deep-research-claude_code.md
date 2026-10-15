---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-21T18:27:44.553830'
end_time: '2026-08-21T18:31:46.436288'
duration_seconds: 241.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Trichotillomania
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 23
  num_turns: 25
  total_cost_usd: 1.8946384
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 36
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Trichotillomania
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Trichotillomania** covering all of the
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

I now have comprehensive data across all major sections. Let me compile the full research report.

# Trichotillomania (Hair-Pulling Disorder): Comprehensive Research Report

## 1. Disease Information

**Overview.** Trichotillomania (TTM), also termed hair-pulling disorder or trichotillosis, is a psychiatric condition classified in DSM-5 under "Obsessive-Compulsive and Related Disorders" and characterized by recurrent pulling out of one's own hair, resulting in noticeable hair loss, repeated attempts to decrease or stop the behavior, and clinically significant distress or impairment not better explained by another medical or mental disorder. The HPO clinical definition captures the phenomenology precisely: "repetitive pulling out of one's hair resulting in noticeable hair loss," with "a rising subjective sense of tension before pulling out the hair and a sense of gratification or relief when pulling out the hair" (HPO term below).

**Key identifiers:**
- **OMIM:** #613229 (TRICHOTILLOMANIA; TTM) — [OMIM entry](https://www.omim.org/entry/613229)
- **MONDO:** MONDO:0013189
- **ICD-11:** 6B25.0 (grouped under Obsessive-Compulsive or Related Disorders)
- **ICD-10-CM:** F63.3 (Trichotillomania), historically also coded under impulse-control disorders
- **HPO:** HP:0012167 (Trichotillomania)
- **MeSH:** D014307 (Trichotillomania)
- **DSM-5 code:** 312.39 (F63.3)

**Synonyms:** hair-pulling disorder, trichotillosis, trichomania, hair pulling disorder, alopecia due to trichotillomania (as a phenotypic consequence).

**Data provenance note:** Most of the literature base for TTM is aggregated disease-level (clinical trials, cross-sectional cohort/epidemiological studies, twin registries, structural neuroimaging case-control series) rather than large-scale EHR-derived data — nationwide epidemiological studies specifically targeting TTM prevalence are notably lacking, with most estimates drawn from smaller convenience or college-based samples plus a handful of population-based twin registries (e.g., TwinsUK).

---

## 2. Etiology

**Disease causal model.** TTM is understood as a multifactorial neuropsychiatric condition arising from an interaction of polygenic genetic vulnerability, altered cortico-striatal habit/reward circuitry, and environmental/psychological stressors, situated on the obsessive-compulsive/body-focused repetitive behavior (BFRB) spectrum alongside skin-picking (excoriation) disorder.

**Genetic risk factors:**
- **SLITRK1** (chromosome 13q31.1; OMIM 609678): Two rare variants (a frameshift and a 3′UTR SNP, var321) were identified in TTM patients and estimated to account for **~5% of TTM cases** in the original family-based discovery study; mutations have also been reported in Tourette syndrome. Subsequent replication attempts in independent OCD/TTM cohorts have had mixed success. ([Nature Molecular Psychiatry](https://www.nature.com/articles/4001865))
- **SAPAP3 (DLGAP3)**: A SNP (rs11583978) in SAPAP3 was associated with TTM in the OCD Collaborative Genetics Study, supporting SAPAP3 as a shared genetic risk factor across TTM and OCD-spectrum pathological grooming. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10885776/))
- **Polygenic/GWAS evidence:** The first case-control GWAS of TTM (Halvorsen et al. 2025, medRxiv/AJMG-B; 101 European-ancestry TTM cases vs. 488 matched controls) found **no genome-wide-significant loci**, but demonstrated that TTM cases carry a significantly elevated burden of **cross-disorder psychiatric polygenic risk** (using a large trans-diagnostic psychiatric GWAS as reference), plus a trend toward excess large CNV deletions impacting constrained/dosage-sensitive genes. Summary statistics were released publicly to enable future meta-analysis. ([medRxiv](https://www.medrxiv.org/content/10.1101/2025.01.23.25321045v1), [PubMed 40511557](https://pubmed.ncbi.nlm.nih.gov/40511557/))
- **Twin heritability estimates:** Two published twin studies give divergent heritability estimates — Novak et al. (24 MZ, 10 DZ pairs) estimated **h²≈76%**, with MZ:DZ DSM-IV concordance of 38.1% vs. 0%; Monzani et al. (TwinsUK, population-based, 5,409 female twins) estimated **h²≈32%**. Both support a substantial genetic component but with considerable unexplained (largely non-shared environmental) variance. ([PubMed 19199280](https://pubmed.ncbi.nlm.nih.gov/19199280/))

**Environmental/psychosocial risk factors:** Stress and negative affect states are the most consistently reported precipitants/triggers of pulling episodes; boredom and sedentary/passive activities (e.g., reading, watching TV) are common antecedents of "automatic" (low-awareness) pulling, while tension/anxiety precede "focused" pulling. Family history of OCD-spectrum illness is a reported correlate. Age and sex are strong demographic modifiers of course (see Sections 8–9).

**Protective factors:** No genetic protective variants are established. Early treatment engagement and, for very-early-onset (pre-school) pulling, spontaneous natural remission are the best-documented "protective" trajectories (see Section 8).

**Gene-environment interaction:** Not well characterized specifically for TTM; the field draws on the broader OCD-spectrum literature (e.g., stress reactivity interacting with polygenic risk) rather than TTM-specific G×E studies.

---

## 3. Phenotypes

### Core behavioral/psychiatric phenotype
- **Hair-pulling behavior** — recurrent, resulting in noticeable hair loss; may be "focused" (purposeful, preceded by rising tension and followed by relief/gratification) or "automatic" (out-of-awareness, occurring during sedentary/passive activities). Suggested term: **HP:0012167 Trichotillomania**.
- **Rising tension before pulling, relief/gratification after pulling** — the core DSM-5 phenomenological criteria (not required for diagnosis in DSM-5, unlike DSM-IV, but frequently present).
- **Repeated unsuccessful attempts to decrease/stop pulling.**
- **Trichophagia** (hair-eating) — occurs in a substantial minority and is the direct precursor to trichobezoar formation.
- **Trichotemnomania** (compulsive hair-cutting) — a related but distinct BFRB sometimes comorbid.

### Physical/dermatologic manifestations
- **Alopecia** — patchy, irregular, incomplete hair loss with hairs of varying length in affected areas (contrasted with complete, well-demarcated patches in alopecia areata). Suggested term: HP:0001596 (Alopecia) as a parent/associated term, with HP:0012167 as the more specific disease-behavior term.
- **Trichoscopic/dermoscopic findings**: black dots (variable size/shape), coiled/hook hairs, flame hairs, "V-sign," tulip hairs, trichoptilosis (split ends), hair powder, follicular microhemorrhages, upright regrowing hairs; **absence of exclamation-mark hairs and yellow dots** helps distinguish TTM from alopecia areata. ([Acta Derm Venereol](https://www.medicaljournals.se/acta/content/html/10.2340/00015555-1674), [PMC3500069](https://pmc.ncbi.nlm.nih.gov/articles/PMC3500069/))
- **Trichobezoar/Rapunzel syndrome** — in patients with trichophagia, ingested hair accumulates in the stomach (± extension into small bowel = Rapunzel syndrome), producing gastric outlet obstruction, ulceration, perforation, peritonitis, intussusception, pancreatitis, obstructive jaundice, protein-losing enteropathy, and iron-deficiency/megaloblastic anemia. ([PMC10449238](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10449238/), [PMC9637412](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9637412/))
- Sites: scalp (most common), eyebrows, eyelashes, pubic/body hair.

### Psychiatric/functional phenotypes
- Marked distress, shame, guilt, and social avoidance related to visible hair loss.
- Impaired occupational, academic, and social functioning; financial burden (wigs, dermatologic treatment, camouflage).

### Onset, severity, progression
- **Age of onset**: mean overall ~17.7 years in some series; other estimates cite mean onset ~13 years or bimodal childhood peaks around 8 years (boys) / 12 years (girls); onset before age 5 has a distinct, often self-limiting course.
- **Severity**: measured clinically using the **Massachusetts General Hospital Hairpulling Scale (MGH-HPS)** — a 7-item, 0–4 Likert self-report scale (total range 0–28) with a two-factor structure (Severity; Resistance and Control), good internal consistency (α 0.80–0.85). ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022399906005290))
- **Progression**: chronic, waxing-and-waning course typical when onset occurs in later childhood/adolescence; later age of onset is associated with greater severity, more treatment resistance, and higher comorbidity, whereas very-early (pre-school) onset frequently resolves spontaneously ("natural recovery").
- **Frequency in affected individuals**: comorbid psychiatric illness present in ~79% of TTM patients (see Section 9/comorbidity below).

### Quality-of-life impact
Multiple case-control studies (e.g., Diefenbach et al.) show TTM patients report significantly worse psychological distress, self-esteem, and quality of life than non-psychiatric controls, with effects substantially mediated by comorbid depression; shame, embarrassment, social isolation, and avoidance of activities that expose hair loss (swimming, wind, intimacy, hairdressers) are consistently reported. ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0005796704001354))

---

## 4. Genetic/Molecular Information

- **Causal/risk genes**: **SLITRK1** (chr13q31.1, OMIM 609678) — integral membrane protein homologous to TRK neurotrophin receptors, implicated in neurite outgrowth/synaptic connectivity; a frameshift deletion and the noncoding variant var321 were identified in TTM (and Tourette) pedigrees. **SAPAP3/DLGAP3** (chr1p34.3) — postsynaptic scaffolding protein at glutamatergic corticostriatal synapses, interacting with PSD-95/Shank family proteins in the striatum (caudate); rs11583978 associated with TTM/pathological grooming.
- **Variant classification**: Both SLITRK1 and SAPAP3 findings are common/rare-variant *association* findings rather than ClinVar-curated pathogenic/likely-pathogenic single-gene Mendelian variants; TTM is not modeled as a single-gene Mendelian disorder — genetic architecture is best characterized as **polygenic**, overlapping substantially with general psychiatric risk (per the 2025 GWAS).
- **Structural variation**: The 2025 GWAS reported a nominal excess of **large, constrained-gene-impacting copy-number deletions** in TTM cases vs. controls (trend-level, not genome-wide significant given small sample).
- **Functional consequence framing**: SLITRK1 loss-of-function variants are hypothesized to impair neurite/synapse formation ("faulty wiring") producing the urge to pull; SAPAP3 dysfunction is hypothesized to alter glutamatergic corticostriatal synaptic structure/function, consistent with the NAC (glutamate-modulator) treatment rationale (Section 12) and with Sapap3-knockout mouse hyperglutamatergic/hypergrooming phenotypes.
- **Epigenetics/somatic**: No disease-defining epigenetic or somatic-mosaicism findings are established for TTM specifically.
- **Chromosomal abnormalities**: None established as causal.

Suggested annotations: HGNC gene symbols `SLITRK1` (HGNC:20297) and `DLGAP3`/`SAPAP3` (HGNC:19071); GO terms such as GO:0007416 (synapse assembly) and GO:0007268 (chemical synaptic transmission) for mechanistic framing.

---

## 5. Environmental Information

- **Psychosocial stressors**: acute and chronic stress, negative affect, boredom, and sedentary cognitive load (reading, screen time) are the most consistently identified situational triggers/exacerbators, rather than toxin/occupational exposures.
- **No infectious etiology** — TTM is not infection-associated; tinea capitis is a key infectious differential diagnosis to exclude (see Section 10), not a cause.
- **Lifestyle factors**: sedentary/passive activity contexts specifically associated with "automatic" subtype pulling.

---

## 6. Mechanism / Pathophysiology

**Causal chain (proposed):** genetic vulnerability (polygenic risk overlapping general psychiatric risk; candidate SLITRK1/SAPAP3 variants) → **altered cortico-striato-thalamo-cortical (CSTC) circuitry**, particularly striatal (caudate/putamen), orbitofrontal/cingulate, and cerebellar nodes involved in habit formation, motor sequencing, and affect regulation → dysregulated **glutamatergic neurotransmission** in corticostriatal/nucleus accumbens circuits (supported by NAC's mechanism and Sapap3-knockout hyperglutamatergic grooming) → maladaptive habit-learning loop in which hair-pulling becomes negatively reinforced by tension relief (or is captured by an automatic, low-awareness habit circuit) → recurrent pulling behavior, hair-follicle trauma, and (if trichophagia present) secondary GI bezoar pathology.

- **Molecular pathways**: Glutamatergic signaling in nucleus accumbens/striatum implicated via the SAPAP3/Shank–PSD95 postsynaptic density complex and via NAC's efficacy as a cystine-glutamate antiporter modulator restoring extracellular glutamate tone. Serotonergic dysregulation is also implicated (basis for SSRI trials, though evidence is weaker than for OCD proper).
- **Cellular processes**: Aberrant corticostriatal synaptic structure — Sapap3-knockout mice show excess dendritic spine density and pre/postsynaptic structural defects in striatum; Hoxb8-mutant mice show corticostriatal circuit defects (excess dendritic spines, LTP and miniature postsynaptic current abnormalities) on Golgi/ultrastructural/electrophysiological study. ([Nature Molecular Psychiatry](https://www.nature.com/articles/mp2017180))
- **Neuroimmune mechanism (Hoxb8 model)**: Hoxb8 lineage in brain labels **bone-marrow-derived microglia** exclusively; Hoxb8-mutant mice display doubled grooming time leading to hair removal and self-inflicted sores, and this pathological grooming is **rescued by wild-type bone-marrow transplantation**, implicating a hematopoietic/microglial origin for the corticostriatal circuit defect — a striking "neuroimmunological" mechanistic candidate for compulsive grooming disorders. ([PMC2894573](https://pmc.ncbi.nlm.nih.gov/articles/PMC2894573/), [Cell/ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0092867410003740))
- **Structural neuroimaging in humans**: Morphometric MRI shows increased gray-matter density in left striatum, left amygdalo-hippocampal formation, and cingulate/supplementary motor/frontal cortex bilaterally — regions implicated in habit learning, cognition, and affect regulation ([Cambridge/BJP](https://www.cambridge.org/core/journals/the-british-journal-of-psychiatry/article/grey-matter-abnormalities-in-trichotillomania-morphometric-magnetic-resonance-imaging-study/7DE602B3AF7E77C2853898828DF072BE)). A separate parcellation study found **reduced cerebellar volumes** in TTM (n=14) vs. controls (n=12), implicating the cerebellum's role in complex motor sequencing. White-matter volume alterations and structural brain network connectivity differences have also been reported, though the overall imaging literature is described as "limited and inconsistent," and (unlike OCD) TTM-specific CSTC circuit dysfunction has not been as extensively or consistently mapped as in OCD proper.
- **Tissue-level mechanism**: repeated mechanical traction on hair follicles causes anagen hair extraction with variable catagen/telogen involvement (trichogram shows catagen and anagen hairs with ruptured root sheaths, absence of telogen hairs), producing irregular patchy alopecia without epidermal inflammation/scarring — distinguishing TTM histologically/trichoscopically from alopecia areata and cicatricial alopecias.
- **GI pathophysiology (trichobezoar)**: swallowed hair is resistant to digestion and peristaltic transit due to its smooth, slippery surface; it accumulates in the gastric rugae, becomes matted with mucus/food, and can extend through the pylorus into the small bowel (Rapunzel syndrome), producing obstruction, pressure necrosis/ulceration, and perforation via impaired local blood supply.

**Suggested ontology terms**: GO:0035640 (exploration behavior) / behavioral GO terms are limited for this domain — more precise: GO:0007268 (synaptic transmission), GO:0050890 (cognition), GO:0007612 (learning); CL terms for microglia (CL:0000129) and medium spiny neurons (CL:1001474) given the Hoxb8/microglial and striatal-neuron mechanistic threads; UBERON:0002316 (striatum), UBERON:0002037 (cerebellum), UBERON:0001870 (frontal cortex).

---

## 7. Anatomical Structures Affected

- **Organ level (primary)**: Skin/hair follicles of the **scalp** (UBERON:0002385 or more specific scalp term), **eyebrows**, **eyelashes**, and other body hair sites. **Secondary**: gastrointestinal tract (stomach/small intestine) via trichobezoar in patients with trichophagia.
- **Body systems**: primarily the **integumentary system** (behaviorally driven) and **central nervous system** (etiological/mechanistic locus — corticostriatal circuitry); secondary **gastrointestinal system** involvement in trichophagic patients.
- **Tissue/cell level**: hair follicle epithelium and dermal papilla (mechanical trauma); striatal medium spiny neurons and corticostriatal glutamatergic synapses (CNS mechanism); microglia (Hoxb8 mouse model).
- **Subcellular level**: postsynaptic density complex (PSD-95/SAPAP3/Shank) at glutamatergic synapses; dendritic spines (structural remodeling in animal models).
- **Localization/laterality**: Scalp involvement is typically patchy and can be unilateral or bilateral depending on hand dominance and pulling pattern (e.g., "Friar Tuck" pattern on the vertex/crown is a recognized presentation); eyebrow/eyelash involvement can be unilateral if one hand is dominantly used.

Suggested UBERON terms: UBERON:0002481 (skin of scalp region — or closest scalp term), UBERON:0006914 (eyebrow), UBERON:0006414 (eyelash region... check exact ID), UBERON:0000945 (stomach) for trichobezoar site, UBERON:0002108 (small intestine) for Rapunzel-syndrome extension.

---

## 8. Temporal Development

- **Onset**: bimodal/variable — early childhood (mean ~8 y boys / ~12 y girls in one series, sexes roughly equally affected in childhood) versus adolescent onset (mean overall ~17.7 y; males ~19.0 y, females ~14.8 y in another series). Onset pattern is typically **insidious** rather than acute.
- **Progression**: **Childhood-onset (pre-school, <5 years) TTM** frequently shows spontaneous cessation over time and is often considered a transient, self-limited habit requiring little intervention. **Adolescent/later-onset TTM** more often becomes a **chronic, waxing-and-waning condition** persisting into adulthood if untreated, and is associated with greater severity, treatment resistance, and psychiatric comorbidity than early-onset disease.
- **Course pattern**: chronic, relapsing-remitting/fluctuating severity over the lifespan is the modal pattern in clinical (as opposed to community/subclinical) samples; "automatic" pulling in passive/sedentary contexts and "focused," tension-driven pulling can co-occur and fluctuate with stress.
- **Remission**: Natural (untreated) recovery is documented, more common in childhood-onset disease; treatment-induced remission is achievable with behavioral therapy but relapse is common (see Section 12).
- **Critical periods**: Adolescence appears to be a period of both risk (onset) and relative treatment resistance if onset occurs then, versus early childhood onset, where the window is more one of spontaneous resolution.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Lifetime prevalence**: estimates range 0.6–2.2%, with a pooled meta-analytic estimate of **1.14%** (95% CI 0.66–1.96%) across 30 studies/38,526 participants; other single estimates cite ~1.7%.
- **Nationwide/population-representative incidence data are lacking**; most prevalence estimates derive from college/community convenience samples.

**Sex ratio**: Clinical samples classically report a strong female predominance (as high as ~9:1 female:male in adult clinical populations), while population-based/meta-analytic data do **not** consistently confirm female preponderance, with substantial cross-study heterogeneity — sexes are reported as roughly equally affected in **childhood**, with the female skew emerging/persisting more strongly in **adulthood** (possibly reflecting differential treatment-seeking or persistence rather than true incidence difference).

**Inheritance pattern**: TTM is **not Mendelian** — best characterized as **complex/multifactorial (polygenic)** inheritance with candidate contributory rare variants (SLITRK1, SAPAP3) of modest individual effect. No established penetrance/expressivity figures analogous to single-gene disorders; no genetic anticipation, germline mosaicism, or founder-effect data reported. No specific carrier-frequency data (not applicable to a polygenic/complex trait in this framework).

**Population demographics**: No strong evidence for differential prevalence by ethnicity/geography has been robustly established in the literature reviewed; data are concentrated in North American/European clinical and web-recruited cohorts (e.g., the 2025 GWAS cohort was European-ancestry, US-recruited via the Trichotillomania Learning Center).

---

## 10. Diagnostics

**Clinical criteria (DSM-5)**: (A) recurrent pulling out of one's hair resulting in hair loss; (B) repeated attempts to decrease/stop; (C) clinically significant distress or impairment; (D) not attributable to another medical condition (e.g., dermatologic); (E) not better explained by another mental disorder.

**Physical/dermatologic exam and trichoscopy** (key tool):
- Trichoscopic features suggestive of TTM: black dots of variable size/shape, coiled/hook hairs, "flame hairs," "V-sign," "tulip hairs," trichoptilosis (split ends), broken hairs of varying length, hair powder, follicular microhemorrhages, upright regrowing hairs; **absence of exclamation-mark hairs and yellow dots** (the latter two being more typical of alopecia areata). ([Acta Derm Venereol](https://www.medicaljournals.se/acta/content/html/10.2340/00015555-1674), [PMC3500069](https://pmc.ncbi.nlm.nih.gov/articles/PMC3500069/))
- Trichogram: catagen and anagen hairs with ruptured root sheaths; absence of telogen hairs.
- Scalp biopsy (when diagnosis unclear): pigment casts, increased catagen hairs, perifollicular hemorrhage, empty follicles, trichomalacia — without significant inflammation or scarring.

**Differential diagnosis**:
- **Alopecia areata**: complete hair loss within well-demarcated patches, exclamation-mark hairs present, uniform black-dot morphology, autoimmune pathogenesis.
- **Tinea capitis**: scaling, erythema, crusting, broken hairs at the scalp surface, positive fungal culture/KOH.
- **Traction alopecia**: history of chronic mechanical tension (braiding, tight hairstyles) rather than compulsive pulling.
- Androgenetic alopecia, telogen effluvium, and other cicatricial alopecias in atypical presentations.

**Standardized severity/assessment tools**:
- **MGH-HPS (Massachusetts General Hospital Hairpulling Scale)** — 7-item self-report, 0–28 total, two-factor (Severity; Resistance and Control) structure. ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022399906005290))
- Trichotillomania Impact Project scales, Milwaukee Inventory for Subtypes of Trichotillomania (MIST), NIMH-TTM Severity Scale.

**Genetic testing**: No clinically validated single-gene or panel-based genetic test exists for TTM diagnosis (it is a behavioral/clinical diagnosis); research-only genotyping (GWAS arrays) has been used investigationally.

**Imaging**: Not diagnostic/routine; structural MRI (VBM) has been used in research settings to characterize gray-matter and cerebellar volume differences (Section 6) but has no established individual diagnostic utility.

**Screening**: No population screening programs exist; case identification is via clinical interview, often supplemented by trichoscopy for confirmation and to exclude dermatologic mimics. GI imaging (ultrasound/CT) is indicated diagnostically when trichobezoar/Rapunzel syndrome is suspected in patients with a trichophagia history presenting with abdominal mass, obstruction, or GI bleeding.

---

## 11. Outcome / Prognosis

- **Mortality**: TTM itself is not directly life-threatening, but **trichobezoar-related complications** (gastric/intestinal perforation, peritonitis, severe malnutrition) carry real morbidity/mortality risk in trichophagic patients if unrecognized and untreated; case-report literature documents severe outcomes including perforation peritonitis and multi-organ complications (pancreatitis, cholangitis).
- **Morbidity/functional impact**: Significant impairment in psychosocial functioning, self-esteem, and quality of life, substantially mediated by comorbid depression; occupational, academic, and social impairment and financial burden are well documented.
- **Course/complications**: chronic waxing-and-waning course in clinical samples; comorbidity with mood/anxiety disorders is associated with greater severity and poorer prognosis. Up to **50–67% of initial treatment responders relapse** during long-term follow-up after habit reversal-based behavioral therapy, underscoring a high relapse burden even among treatment responders.
- **Prognostic factors**: later age of onset, comorbid OCD/anxiety/depression, and greater experiential avoidance are associated with more severe/treatment-resistant course; very early (pre-school) onset is prognostically favorable (frequent spontaneous remission).
- **Recovery potential**: Natural recovery is well documented, especially in early-onset cases; with behavioral treatment (habit reversal-based therapy), large effect sizes are achievable in the short-to-medium term (see Section 12), though durability is limited without maintenance.

---

## 12. Treatment

### Behavioral/psychotherapeutic (first-line, strongest evidence base)
- **Habit Reversal Training (HRT)** / broader **behavior therapy** — large effect vs. control conditions (SMD ≈ **−1.22**); superior to pharmacotherapy (clomipramine or SSRIs) in comparative meta-analyses. Suggested NCIT: closest fit is a behavioral therapy/counseling term (e.g., NCIT:C15315 Rehabilitation or a psychotherapy-specific term); no MAXO/NCIT-specific "habit reversal training" term is confirmed — use free-text `preferred_term` with `therapeutic_modality: BEHAVIORAL`.
- **Acceptance and Commitment Therapy (ACT)-enhanced HRT**: RCT (Woods et al., 25 adults) found significant reductions in MGH-HPS severity, impairment, experiential avoidance, anxiety, and depression vs. waitlist; **66% response rate** in the ACT/HRT arm vs. **8%** in waitlist control, with gains generally maintained at 3-month follow-up. ("Strong support" designation also given in a more recent evidence review, alongside plain HRT and NAC.) ([PubMed 16039603](https://pubmed.ncbi.nlm.nih.gov/16039603/))
- **Comprehensive Behavioral (ComB) model**, cognitive therapy (targeting self-control cognitions), telehealth/virtual HRT delivery — virtual-delivery real-world data show median 33.3% severity reduction (Hedges' g=1.01).
- **Limitation**: 50–67% of initial responders relapse long-term.

### Pharmacotherapy (adjunctive/second-line; overall low-certainty evidence per Cochrane)
- **N-acetylcysteine (NAC)** — glutamate modulator (restores extracellular glutamate in nucleus accumbens via cystine-glutamate antiporter). **Adult RCT (Grant, Odlaug, Kim 2009, Arch Gen Psychiatry)**: 50 adults, NAC 1200–2400 mg/day × 12 weeks; 56% "much/very much improved" vs. 16% placebo — significant benefit, well tolerated. ([JAMA Network](https://jamanetwork.com/journals/jamapsychiatry/fullarticle/483113)) **Pediatric RCT** (39 children/adolescents 8–17y, 12 weeks, add-on design): **no significant difference** from placebo on MGH-HPS. Suggests efficacy may be age-dependent (adults > children). CHEBI candidate: CHEBI:47704 (N-acetyl-L-cysteine).
- **Clomipramine** (TCA with SRI action, 50→250 mg/day) — low-certainty evidence of benefit from a single small trial. NCIT/CHEBI: clomipramine has an established CHEBI ID.
- **Olanzapine** (atypical antipsychotic, 2.5→10 mg/day) — low-certainty benefit from one small RCT.
- **SSRIs**: commonly used clinically but evidence base for TTM specifically is weaker/inconsistent compared to OCD.
- Overall Cochrane conclusion: evidence is **low-certainty**, from few, small (n often <50), short-duration (5–13 week) trials; treatment decisions should be individualized based on severity and comorbidity. ([Cochrane](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007662.pub3/full))
- **Experimental/investigational**: valbenazine (VMAT2 inhibitor) trial ongoing (NCT05207085); milk thistle pediatric/adult trial (NCT02473913).

### Surgical/interventional
- **Trichobezoar/Rapunzel syndrome**: surgical (open or laparoscopic) gastrotomy/enterotomy for bezoar removal is definitive management for GI complications; endoscopic removal may be attempted for smaller bezoars.

### Supportive care
- Psychoeducation, family therapy (especially pediatric cases), dermatologic camouflage/wig counseling, and treatment of comorbid mood/anxiety disorders as part of a comprehensive plan.

### Treatment algorithm
Behavioral therapy (HRT ± ACT enhancement) is generally first-line given the strongest and most consistent effect sizes; pharmacotherapy (NAC in adults, or SSRIs/clomipramine/olanzapine) is used adjunctively or when behavioral therapy access is limited or comorbidity (e.g., depression, OCD) predominates.

Suggested NCIT terms: NCIT:C15986 (Pharmacotherapy) for drug treatments generally, paired with `therapeutic_agent` CHEBI terms for clomipramine, olanzapine, and NAC; NCIT:C15302 (Physical Therapy) is not appropriate — HRT/ACT are psychological/behavioral interventions best captured with `therapeutic_modality: BEHAVIORAL`.

---

## 13. Prevention

- **No established primary prevention** (no vaccine, no modifiable single risk factor with proven prevention efficacy).
- **Secondary prevention/early detection**: early clinical recognition in childhood-onset cases to differentiate transient (likely self-resolving) pulling from a pattern likely to become chronic, enabling earlier behavioral intervention when indicated.
- **Tertiary prevention**: prevention of trichobezoar/GI complications via early identification and treatment of trichophagia in TTM patients (screening for hair-eating behavior specifically, given the outsized morbidity risk of undetected bezoar formation).
- **Genetic counseling**: not a standard part of TTM management given its complex/polygenic, non-Mendelian architecture; family history of OCD-spectrum illness may be discussed as a risk correlate in counseling contexts but no formal risk-prediction tools exist.
- **Behavioral/public health interventions**: stress-reduction and habit-awareness psychoeducation in at-risk youth (e.g., those with early automatic pulling behaviors or comorbid anxiety) is a plausible but not rigorously trial-validated preventive strategy.

---

## 14. Other Species / Natural Disease

TTM-like body-focused repetitive/compulsive grooming behaviors occur naturally across multiple species, supporting cross-species translational relevance:

- **Avian — feather-picking/feather-damaging behavior in parrots**: proposed as a naturalistic model with phenomenological similarities to TTM (behavior pattern, proposed stress-related etiology, evoking cues, and shared responsiveness to behavioral and SSRI-based pharmacological treatment). ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0005791694900191))
- **Canine — acral lick dermatitis**: dogs lick paws/flank to the point of ulceration/infection, proposed as a compulsive-grooming veterinary analog.
- **Feline and nonhuman primate — psychogenic alopecia**: self-induced hair loss from excessive grooming, described as phenotypically analogous.
- **Swine**: tail/ear biting behaviors described in the same conceptual family of body-focused repetitive disorders.
- **Rodent (naturalistic)**: inbred **C57BL/6J mice** display spontaneous barbering behavior with phenotypic parallels to TTM; **alcohol-preferring (P) rats** selectively bred for alcohol preference show elevated scratching/oral grooming predictive of subsequent dermatitis/skin lesion development, proposed as an additional naturalistic model. ([PMC8875168](https://pmc.ncbi.nlm.nih.gov/articles/PMC8875168/))

These natural/spontaneous animal presentations are distinct from the induced genetic models below but reinforce that compulsive self-grooming with tissue damage is a conserved cross-species behavioral phenotype.

---

## 15. Model Organisms

**Genetic/induced mouse models:**

- **Sapap3 (Dlgap3) knockout mice**: exhibit excessive/compulsive grooming with facial injuries and increased anxiety-like behavior, closely paralleling human TTM/OCD-spectrum pathological grooming. Quantitatively, pre-stressor (pre-spray) grooming was 31 s (KO) vs. 8 s (WT); post-spray, 167 s (KO) vs. 52 s (WT). Underlying mechanism: SAPAP3 (a PSD-95/Shank-interacting postsynaptic scaffolding protein enriched in the striatum/caudate) loss produces corticostriatal glutamatergic synaptic dysfunction. Recent extensions include study of the **nucleus accumbens circuit and oxytocin as a candidate therapeutic** in this model. ([Scientific Reports 2025](https://www.nature.com/articles/s41598-025-14076-y), [bioRxiv](https://www.biorxiv.org/content/10.1101/2020.01.22.915215v1.full))
- **Hoxb8 mutant mice**: spend roughly double the grooming time of wild-type littermates, developing hair removal and self-inflicted open sores highly analogous to human TTM. Mechanistically notable for its **hematopoietic/microglial origin** — Hoxb8 lineage in brain exclusively marks bone-marrow-derived microglia, and pathological grooming is **rescued by wild-type bone-marrow transplantation** (though the associated sensory/nociceptive defect is not rescued), and corticostriatal circuit defects (excess dendritic spines, synaptic/LTP abnormalities) are demonstrable by Golgi, ultrastructural, and electrophysiological study. Disruption of Hoxb8 restricted to the hematopoietic lineage alone recapitulates pathological grooming. ([PMC2894573](https://pmc.ncbi.nlm.nih.gov/articles/PMC2894573/), [Molecular Psychiatry 2018](https://www.nature.com/articles/mp2017180))
- **iNOS (NOS2) knockout mice**: proposed as an additional model of trichotillomania-like behavior (nitric oxide synthase pathway implicated in compulsive grooming; bioRxiv preprint).

**Model characteristics and translational fidelity**: Both Sapap3-KO and Hoxb8-mutant models recapitulate the core surface phenotype (excessive, injurious self-grooming/hair removal) and implicate convergent corticostriatal circuit and glutamatergic synaptic pathology, aligning with human structural imaging (striatal/cingulate gray-matter changes) and the clinical efficacy of the glutamate-modulator NAC. A key **limitation**: these are models of pathological *grooming* generally (shared across TTM and OCD-spectrum compulsive behavior) rather than TTM-specific models, and the Hoxb8 model's microglial/hematopoietic mechanism, while mechanistically striking, has an uncertain degree of translational specificity to human TTM (a candidate `HUMAN_MODEL_MISMATCH` consideration for KB curation, given no direct human confirmation of a hematopoietic/microglial causal contribution to TTM).

**Research applications**: These models are used to probe corticostriatal synaptic and microglial mechanisms of compulsive grooming, to screen candidate pharmacotherapies (e.g., oxytocin, NAC-related glutamate modulators), and to study circuit-level (nucleus accumbens, striatum) intervention targets.

Suggested NCBITaxon terms: NCBITaxon:10090 (Mus musculus), NCBITaxon:10116 (Rattus norvegicus, P rats), NCBITaxon:9615 (Canis lupus familiaris), and relevant Psittaciformes taxa for parrot feather-picking models.

---

## Summary of Suggested Ontology Term Bindings

| Domain | Suggested term |
|---|---|
| Disease | MONDO:0013189; OMIM:613229; ICD-11:6B25.0 |
| Core phenotype | HP:0012167 (Trichotillomania) |
| Associated phenotype | HP:0001596 (Alopecia) |
| Genes | HGNC:20297 (SLITRK1); HGNC:19071 (DLGAP3/SAPAP3) |
| Biological process | GO:0007268 (chemical synaptic transmission); GO:0007612 (learning) |
| Cell types | CL:1001474 (medium spiny neuron); CL:0000129 (microglial cell) |
| Anatomy | UBERON:0002316 (striatum); UBERON:0002037 (cerebellum); UBERON:0000945 (stomach, for trichobezoar) |
| Chemical/drug | CHEBI: N-acetyl-L-cysteine; clomipramine; olanzapine |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy) + `therapeutic_agent`; behavioral therapy via `therapeutic_modality: BEHAVIORAL` (no precise NCIT HRT term identified) |

---

## Sources

- [OMIM #613229 — Trichotillomania](https://www.omim.org/entry/613229)
- [SLITRK1 mutations in Trichotillomania — Molecular Psychiatry](https://www.nature.com/articles/4001865)
- [Sapap3 and pathological grooming in humans — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10885776/)
- [Exploring the nucleus accumbens circuit and oxytocin therapy in a Sapap3 knockout mouse model — Scientific Reports 2025](https://www.nature.com/articles/s41598-025-14076-y)
- [The Sapap3-knockout mouse model manifests a spectrum of repetitive behaviours — bioRxiv](https://www.biorxiv.org/content/10.1101/2020.01.22.915215v1.full)
- [Hematopoietic Origin of Pathological Grooming in Hoxb8 Mutant Mice — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2894573/)
- [Corticostriatal circuit defects in Hoxb8 mutant mice — Molecular Psychiatry](https://www.nature.com/articles/mp2017180)
- [Trichotillomania — American Journal of Psychiatry review](https://psychiatryonline.org/doi/10.1176/appi.ajp.2016.15111432)
- [Trichotillomania — StatPearls/NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK493186/)
- [Pharmacological and behavioral treatment for trichotillomania: updated systematic review with meta-analysis — PubMed](https://pubmed.ncbi.nlm.nih.gov/32390221/)
- [The genetics of trichotillomania and excoriation disorder: A systematic review — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11513794/)
- [A twin concordance study of trichotillomania — PubMed](https://pubmed.ncbi.nlm.nih.gov/19199280/)
- [Comorbidity in trichotillomania: A cluster analytical approach — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6908854/)
- [Grey matter abnormalities in trichotillomania: morphometric MRI study — British Journal of Psychiatry](https://www.cambridge.org/core/journals/the-british-journal-of-psychiatry/article/grey-matter-abnormalities-in-trichotillomania-morphometric-magnetic-resonance-imaging-study/7DE602B3AF7E77C2853898828DF072BE)
- [White matter volume alterations in hair-pulling disorder — Brain Imaging and Behavior](https://link.springer.com/article/10.1007/s11682-019-00170-z)
- [Rapunzel Syndrome: A Case of Trichobezoar with Small Bowel Complications — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9637412/)
- [A Rare Case of Rapunzel Syndrome Presenting with Perforation Peritonitis — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10449238/)
- [Pharmacotherapy for trichotillomania — Cochrane Library](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007662.pub3/full)
- [N-Acetylcysteine, a Glutamate Modulator, in the Treatment of Trichotillomania — JAMA Network (Arch Gen Psychiatry 2009)](https://jamanetwork.com/journals/jamapsychiatry/fullarticle/483113)
- [N-Acetylcysteine in the Treatment of Pediatric Trichotillomania — JAACAP](https://www.jaacap.org/article/S0890-8567(12)01006-4/abstract)
- [New Trichoscopy Findings in Trichotillomania — Acta Dermato-Venereologica](https://www.medicaljournals.se/acta/content/html/10.2340/00015555-1674)
- [Trichoscopy as an aid in the diagnosis of trichotillomania — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3500069/)
- [Trichotillomania Differential Diagnoses — Medscape](https://emedicine.medscape.com/article/1071854-differential)
- [Factor analysis of the Massachusetts General Hospital Hairpulling Scale](https://www.sciencedirect.com/science/article/abs/pii/S0022399906005290)
- [Genomic Analysis of Trichotillomania — medRxiv/PubMed 40511557](https://www.medrxiv.org/content/10.1101/2025.01.23.25321045v1)
- [A controlled evaluation of acceptance and commitment therapy plus habit reversal for trichotillomania — PubMed](https://pubmed.ncbi.nlm.nih.gov/16039603/)
- [Trichotillomania: impact on psychosocial functioning and quality of life — PubMed](https://pubmed.ncbi.nlm.nih.gov/15896284/)
- [Feather picking disorder and trichotillomania: An avian model of human psychopathology — PubMed](https://pubmed.ncbi.nlm.nih.gov/7852601/)
- [Predictive Value of Grooming Behavior for Development of Dermatitis in Selectively Bred P Rats — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8875168/)
- [Age of onset of trichotillomania symptoms: investigating clinical correlates — PubMed](https://pubmed.ncbi.nlm.nih.gov/21135642/)
- [Natural Recovery in Trichotillomania — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7614802/)
- [Prevalence, gender correlates, and co-morbidity of trichotillomania — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0165178120303553)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.