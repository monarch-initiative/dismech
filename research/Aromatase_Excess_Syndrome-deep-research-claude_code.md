---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-13T23:35:11.481377'
end_time: '2026-08-13T23:40:07.826397'
duration_seconds: 296.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aromatase Excess Syndrome
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
  - claude-sonnet-5
  web_search_requests: 15
  num_turns: 20
  total_cost_usd: 1.9593497000000002
  session_id: 9a8e6f80-f221-5449-bf06-75dbe1a3352c
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 2
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aromatase Excess Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Aromatase Excess Syndrome** covering all of the
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

I'll research Aromatase Excess Syndrome (AEXS) using web searches to gather accurate, citable information before compiling the report.

# Aromatase Excess Syndrome (AEXS): Comprehensive Research Report

## 1. Disease Information

**Overview.** Aromatase excess syndrome (AEXS) is a rare, autosomal dominant endocrine genomic disorder caused by heterozygous structural rearrangements (duplications, deletions, or inversions) in and around the *CYP19A1* gene on chromosome 15q21.2, which encodes aromatase — the enzyme that converts C19 androgens (androstenedione, testosterone) into C18 estrogens (estrone, estradiol). Gain-of-function overexpression of aromatase produces peripheral (extraglandular) estrogen excess, presenting classically as pre‑ or peripubertal-onset **gynecomastia** in males, with accelerated bone maturation, short adult stature, and variable hypogonadotropic hypogonadism; affected females may have macromastia, precocious puberty, and irregular menses, or may be asymptomatic. AEXS is also historically called "familial gynecomastia" or "hereditary gynecomastia."

**Key identifiers:**
- **OMIM:** #139300 (AROMATASE EXCESS SYNDROME; AEXS) — [omim.org/entry/139300](https://omim.org/entry/139300)
- **Orphanet:** ORPHA:178345 — [orpha.net](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=EN&Expert=178345)
- **MONDO:** MONDO:0007690
- **Gene:** *CYP19A1* (HGNC:2594), chromosome 15q21.2
- **MeSH/GARD:** GARD 12494

**Synonyms:** Familial gynecomastia; hereditary gynecomastia; familial hyperestrogenism; gain-of-function *CYP19A1*-related aromatase excess.

**Source of information:** This entry is built almost entirely from **aggregated disease-level resources** — case series and molecular-genetic studies pooling small numbers of families (fewer than ~30 families/40 individuals reported worldwide as of the most recent reviews) rather than large EHR cohorts, reflecting the syndrome's extreme rarity (Orphanet estimates prevalence <1/1,000,000) (Fukami et al., 2012, PMC3272822).

---

## 2. Etiology

**Disease causal factors — genetic, and exclusively so.** AEXS is caused by heterozygous genomic rearrangements involving the *CYP19A1* locus that place the aromatase coding exons under the control of additional or ectopic (cryptic) promoters, causing constitutive gain-of-function overexpression. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause; every confirmed case has a demonstrable structural rearrangement.

**Genetic risk factors.**
- **Causal rearrangement classes** (Fukami et al., 2011, *J Clin Endocrinol Metab* 96:E1035, PMID:21470988; Demura et al., 2007; Fukami et al., 2013, *J Clin Endocrinol Metab* 98:E2013, PMID:24064691):
  - **Duplications** — e.g., a **79,156-bp tandem duplication** encompassing 7 of the 11 noncoding exons 1 of *CYP19A1*, increasing the physiological promoter copy number and boosting expression in native aromatase-expressing tissues (gonad, adipose, skin, bone).
  - **Deletions** — e.g., a **211,631-bp deletion** spanning exons 2–43 of the neighboring gene *DMXL2* and exons 5–10 of *GLDN*; and a **165,901-bp deletion** spanning exons 2–43 of *DMXL2*. These generate a chimeric *DMXL2*/*CYP19A1* transcript, driving ectopic aromatase expression under the *DMXL2* promoter (widely active in many tissues).
  - **Inversions** — heterozygous chromosomal inversions that juxtapose *CYP19A1* coding exons downstream of constitutively active cryptic promoters normally driving neighboring genes **CGNL1, TMOD3, MAPK6, and TLN2**, producing chimeric transcripts with the broadest and highest-level ectopic expression and the most severe phenotypes (Shozu et al., 2003, *N Engl J Med* 348:1855–1865, PMID:12736278; Fukami et al., 2013, PMID:24064691).
  - This three-way mechanistic taxonomy (duplication/deletion/inversion) was consolidated as "recombination- and replication-mediated rearrangements" (Fukami et al., 2013, PMID:24064691), and more recently a further mechanism — **local aromatase excess from recruitment of unusual *CYP19A1* promoters** in prepubertal gynecomastia without classic genomic rearrangement — has been described (PMID:35667691).
- **Modifier factor: which start codon dominates the chimeric mRNA.** Whether the chimeric transcript retains a translation start codon from the fused neighboring gene determines whether nonsense-mediated decay limits expression: e.g., in deletion-type AEXS the chimeric *DMXL2*/*CYP19A1* mRNA constitutes only ~2–5% of total *CYP19A1*-containing transcripts in skin fibroblasts (subject to NMD), whereas inversion-type chimeric transcripts can comprise **89–100%** of transcripts — directly explaining why inversions cause the most severe disease (Fukami et al., 2012, PMC3272822).
- **Zygosity/inheritance:** heterozygous, autosomal dominant, 50% transmission risk per child regardless of parental sex (Orphanet ORPHA:178345).

**Risk factors — environmental/lifestyle.** None specifically documented; the disease is monogenic/structural and fully penetrant with respect to the biochemical phenotype (elevated estrogen), though clinical phenotypic severity is influenced by rearrangement type, not by exposures. Obesity/adiposity is a plausible severity modifier by analogy with other estrogen-excess states (peripheral aromatization occurs substantially in adipose tissue), but this has not been specifically studied in AEXS cohorts.

**Protective factors.** No genetic or environmental protective factors have been reported. Female carriers are frequently minimally symptomatic or asymptomatic, which may reflect a baseline higher physiological estrogen tone masking the biochemical excess, rather than a true protective mechanism (Fukami et al., 2012, PMC3272822).

**Gene–environment interactions.** Not established for AEXS specifically; extrapolating from general aromatase biology, adiposity would be expected to amplify peripheral (fat-tissue) aromatization on top of the genetically driven overexpression, but no dedicated AEXS study has quantified this interaction.

---

## 3. Phenotypes

### Males (the predominant/most severe presentation)

| Phenotype | Type | Onset | Notes / Suggested HPO term |
|---|---|---|---|
| Pre-/peripubertal gynecomastia | Clinical sign | 7–13 years (peripubertal) in most reported cases; can be prepubertal | **HP:0100295** (Gynecomastia) |
| Premature/accelerated growth spurt | Clinical sign | Childhood | **HP:0005616** (Increased body height); relative tall stature in childhood |
| Advanced bone age / accelerated bone maturation | Clinical sign (imaging) | Childhood through puberty | **HP:0005616** related — **HP:0005923** (Delayed skeletal maturation) is the inverse; use **"Advanced bone age"** — closest term **HP:0005616** or **HP:0100775** (Advanced ossification of carpal bones) |
| Short adult stature (early epiphyseal fusion) | Clinical sign | Adult outcome | **HP:0004322** (Short stature) |
| Mild hypogonadotropic hypogonadism (FSH-dominant suppression) | Laboratory abnormality | Puberty–adulthood | **HP:0000044** (Hypogonadotropic hypogonadism) |
| Small testes with preserved masculinization | Physical sign | Puberty | **HP:0008734** (Testicular atrophy) / **HP:0000028** (Cryptorchidism, not typical — small testes preferred: **HP:0000797** small testis-related term) |
| Elevated estrone (E1), elevated E2/testosterone ratio | Lab abnormality | Any age | Biochemical/biomarker, not a core HPO term — map to **HP:0025091** (Abnormal circulating estrogen level) if used |
| Sparse/absent facial and body hair (severe cases) | Clinical sign | Adolescence–adult | **HP:0002215** (Sparse body hair) |
| Fertility | Generally preserved | Adulthood | Not a phenotype per se |

Fukami et al. (2012, PMC3272822) report, across 23 confirmed male cases, that gynecomastia severity correlated with rearrangement class: **mild in duplication type, moderate in deletion type, and severe in inversion type**, with the most severe (inversion) cases requiring surgical mastectomy.

### Females

| Phenotype | Notes |
|---|---|
| Macromastia | Six of eight reported women had ≥1 symptom, including macromastia (Stratakis et al., 1998, *J Clin Endocrinol Metab*, PMID:9543166) |
| Premature thelarche / isosexual precocious puberty | **HP:0000389** (Premature thelarche) / **HP:0000826** (Precocious puberty) |
| Early menarche | **HP:0410282** or general early puberty terms |
| Irregular menses / irregular uterine bleeding | **HP:0000858** (Menorrhagia) or **HP:0000141** (Abnormal menstruation cycle) |
| Enlarged uterus | **HP:0008684** (Uterine anomaly) family |
| Short adult stature | **HP:0004322** |
| Asymptomatic carrier state | ~25% of reported female carriers show no clinical manifestations (PMC3272822) |

**Severity/progression:** Gynecomastia is progressive without treatment and can require repeat surgical intervention (mastectomy performed twice in one reported case before diagnosis; PMC11614628). Untreated hyperestrogenemia is hypothesized to increase long-term breast cancer risk, motivating durable aromatase-inhibitor therapy.

**Frequency:** Because AEXS is described only in isolated case reports/small pedigrees (no large cohort denominator), exact phenotype-frequency percentages (e.g., "80% of cases") are not established the way they are for common Mendelian diseases; frequencies above are qualitative (from small case series), not population-derived (Fukami et al., 2014, *Expert Rev Endocrinol Metab*, PMID:25264451).

**Quality of life impact:** Gynecomastia in adolescent males carries substantial documented psychosocial burden (embarrassment, social withdrawal, need for repeated breast surgery); this is inferred from the general gynecomastia literature and directly evidenced in AEXS case reports by the need for repeated mastectomy in a young patient (age of onset in childhood, two surgeries before pharmacologic diagnosis and treatment) (PMC11614628, Frontiers 2024).

---

## 4. Genetic/Molecular Information

**Causal gene:** *CYP19A1* (aromatase; **HGNC:2594**; chr15:51,208,057–51,338,596, GRCh38), OMIM *107910. The gene spans **~123 kb**, has **≥11 noncoding exon-1 variants** driving tissue-specific promoters and **9 coding exons (exons 2–10, historically numbered II–X)** (Fukami et al., 2012, PMC3272822).

**Pathogenic variant classes (all structural, not point mutations):**
1. **Tandem duplication** (e.g., 79,156 bp spanning 7 of 11 noncoding exons 1) — increases native-promoter copy number.
2. **Deletion with chimeric transcript formation** (e.g., 211,631 bp deleting *DMXL2* exons 2–43 + *GLDN* exons 5–10; or 165,901 bp deleting *DMXL2* exons 2–43) — creates a fusion mRNA between an upstream gene's noncoding exon and *CYP19A1* coding exons, driving ectopic, broader-tissue expression.
3. **Inversion** — places *CYP19A1* coding exons adjacent to and under control of constitutively active cryptic promoters of neighboring genes *CGNL1*, *TMOD3*, *MAPK6*, or *TLN2*, forming novel chimeric transcripts — described by the discoverers as "a truly original mechanism of a gain-of-function mutation" (Fukami et al., 2013, PMID:24064691; Shozu et al., 2003, PMID:12736278).

**Variant classification (ACMG/AMP framing):** These are large structural/genomic rearrangements rather than SNVs, so classic ACMG missense/nonsense classification does not directly apply; they are functionally classified as **gain-of-function (regulatory, not coding) variants**. No frameshift/missense/nonsense point mutations in the *CYP19A1* coding sequence itself have been reported to cause AEXS (contrast with *CYP19A1* loss-of-function point mutations, which cause the opposite disease, aromatase **deficiency**, OMIM #613546 / MONDO:0013301).

**Allele frequency:** Not present in population databases (gnomAD, 1000 Genomes) as recurrent variants — each family's rearrangement is essentially private/de novo or familially inherited; AEXS causal rearrangements are not polymorphisms.

**Somatic vs. germline:** All reported AEXS rearrangements are **germline**, heterozygous, and dominantly inherited (or de novo).

**Functional consequence:** **Gain-of-function** via transcriptional dysregulation (ectopic/overexpressed promoter usage) — not altered enzyme catalytic activity per se; the aromatase protein itself is structurally normal, but its expression is pathologically increased and/or mistargeted to additional tissues.

**Modifier genes:** None specifically identified; phenotypic severity is explained by the rearrangement class itself (duplication < deletion < inversion) and by the relative dominance of the chimeric transcript over native transcripts (nonsense-mediated decay susceptibility) rather than by trans-acting modifier loci (Fukami et al., 2012, PMC3272822).

**Epigenetic information:** Not specifically studied in AEXS; the disease mechanism is structural/promoter-recruitment based rather than a documented methylation or histone-modification defect.

**Chromosomal abnormalities:** The pathogenic events (duplications, deletions, inversions at 15q21.2) are themselves submicroscopic structural/genomic rearrangements detected by targeted long-range PCR, Southern blotting, array-CGH, or genome sequencing — not visible on standard karyotype.

---

## 5. Environmental Information

- **Environmental factors:** No environmental toxin, radiation, or pollutant exposure has been implicated as causal; AEXS is a purely genetic/structural disorder.
- **Lifestyle factors:** Not established as causal. As above, adiposity is biologically plausible as a modifier of peripheral aromatization (extraglandular aromatase activity, including that from the pathologic *CYP19A1* rearrangement, occurs substantially in adipose tissue), but no AEXS-specific study has quantified obesity as a severity modifier.
- **Infectious agents:** Not applicable — AEXS has no infectious component.

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Molecular trigger:** Heterozygous genomic rearrangement (duplication/deletion/inversion) at 15q21.2 places *CYP19A1* coding exons under control of additional native promoters (duplication) or ectopic constitutively active promoters from neighboring genes *DMXL2*, *CGNL1*, *TMOD3*, *MAPK6*, or *TLN2* (deletion/inversion) (Shozu et al., 2003, PMID:12736278; Fukami et al., 2013, PMID:24064691).
2. **Transcriptional/molecular consequence:** Aromatase (CYP19A1) mRNA and protein are overexpressed, either in native aromatase-expressing tissues at higher levels (duplication) or ectopically across a broader range of tissues that normally do not express aromatase, because the neighboring "donor" genes are widely expressed (deletion/inversion).
3. **Enzymatic/biochemical consequence:** Excess aromatase enzyme (a microsomal cytochrome P450 located in the endoplasmic reticulum) drives excess peripheral conversion of C19 androgens (androstenedione, testosterone) to C18 estrogens (estrone, estradiol) via three sequential NADPH-cytochrome-P450-reductase-dependent hydroxylation/aromatization reactions, using molecular oxygen and NADPH (GeneCards/general aromatase biology).
4. **Systemic hormonal consequence:** Markedly elevated serum estrone (E1) and elevated estrogen-to-androgen (E2/T) ratios, with the magnitude scaling with rearrangement severity — E2/T ratios reported as ~10.0–10.4×10³ for duplication type, ~14.8–27.1×10³ for deletion type, and ~69.6–170.4×10³ for inversion type (Fukami et al., 2012, PMC3272822).
5. **Neuroendocrine feedback:** Chronic estrogen excess exerts **negative feedback on the hypothalamic–pituitary axis**, suppressing GnRH pulsatility and consequently LH/FSH secretion — producing **FSH-dominant hypogonadotropic hypogonadism**; FSH values are described as "low at baseline and poorly responsive to GnRH stimulation even after GnRH priming" in confirmed cases, while LH values remain grossly normal (Fukami et al., 2012, PMC3272822; Frontiers 2024, PMC11614628).
6. **Downstream tissue/organ effects:**
   - **Breast tissue:** Estrogen-driven ductal/stromal proliferation → gynecomastia in males, macromastia in females.
   - **Growth plate/skeleton:** Estrogen accelerates epiphyseal maturation and premature growth-plate fusion → early rapid growth followed by premature cessation → net **short adult stature** despite childhood tall stature.
   - **Gonad:** Suppressed gonadotropin drive → small testes, variable impairment of virilization, though testosterone responses to exogenous hCG are typically preserved (suggesting the testicular steroidogenic machinery itself is intact and the defect is predominantly central/feedback-driven, plus local intratesticular aromatization).
   - **Uterus/menstrual cycle (females):** Estrogen excess drives premature thelarche, early menarche, and irregular/heavy uterine bleeding via disrupted hypothalamic-pituitary-ovarian cyclicity.

**Cell types involved:** Adipocytes, gonadal (Leydig/Sertoli, granulosa/theca) cells, osteoblasts/chondrocytes (growth plate), skin fibroblasts (used diagnostically to assay aromatase activity/chimeric transcripts), mammary epithelial and stromal cells, hypothalamic GnRH neurons and pituitary gonadotrope cells (feedback target). Suggested **CL terms**: CL:0000136 (fat cell/adipocyte), CL:0000473 (Sertoli cell), CL:0000625/appropriate (Leydig cell), CL:0000138 (chondrocyte).

**Biological processes:** Suggested **GO terms**: GO:0006703 (estrogen biosynthetic process), GO:0030520 (intracellular estrogen receptor signaling pathway), GO:0060009 (Sertoli cell development, contextual), GO:0060348 (bone development), GO:0032355 (response to estradiol).

**Molecular function:** Suggested **GO term**: GO:0101020 (estrogen 16-alpha-hydroxylase activity) is not exact; the core catalytic activity is **GO:0070330** (aromatase activity).

**Protein dysfunction:** Not a structural/misfolding defect — the aromatase protein sequence and 3D structure (PDB entries exist for human aromatase, e.g., 3EQM) are normal; the defect is purely one of **transcriptional dosage and tissue-expression pattern**.

**Metabolic changes:** Shift in the systemic androgen:estrogen balance toward estrogen dominance; secondary suppression of endogenous testosterone production via central hypogonadotropism.

**Immune system involvement:** None described.

**Advanced/omics profiling:** No transcriptomic, proteomic, or single-cell datasets specific to AEXS patient tissue have been published (extreme rarity limits such studies); molecular diagnosis instead relies on targeted RT-PCR of chimeric transcripts in skin fibroblasts/lymphocytes and long-range genomic PCR/Southern blot/array-CGH or genome sequencing to map the breakpoints (Fukami et al., 2012/2013).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Breast/mammary gland (both sexes — gynecomastia/macromastia), gonads (testis in males; ovary/uterus in females), skeletal system (growth plate/epiphyses, bone age).
- **Secondary/systemic:** Hypothalamic–pituitary axis (functional suppression, not structural), stature/growth overall.
- **Body systems involved:** Endocrine system (primary), reproductive system, skeletal system.

Suggested **UBERON terms:** UBERON:0000310 (breast), UBERON:0000473 (testis), UBERON:0000992 (ovary), UBERON:0000995 (uterus), UBERON:0002481 (bone tissue growth plate — use UBERON:0002516 epiphysis), UBERON:0007200 (hypothalamus).

**Tissue/cell level:** Mammary ductal epithelium and stroma; testicular Leydig/Sertoli cells; skin fibroblasts (diagnostic surrogate tissue for aromatase activity assay); adipose tissue (major extraglandular aromatization site); chondrocytes of the epiphyseal growth plate.

**Subcellular level:** Aromatase is a **microsomal (endoplasmic reticulum)** cytochrome P450 enzyme. Suggested **GO Cellular Component**: GO:0005789 (endoplasmic reticulum membrane).

**Localization:** Systemic/multi-tissue effect (not confined to a single anatomical site) because the enzyme defect is expressed wherever the fused/duplicated promoter is active — ranging from restricted native tissues (duplication type) to essentially ubiquitous tissue expression (inversion type, following the very widely expressed donor genes *CGNL1/TMOD3/MAPK6/TLN2*). No lateralization pattern (bilateral gynecomastia typical).

---

## 8. Temporal Development

- **Onset:** Pre- to peripubertal in males (commonly ages 7–13 for gynecomastia onset); in females, onset spans premature thelarche/early menarche during childhood/puberty, though some female carriers remain lifelong asymptomatic.
- **Onset pattern:** Insidious/gradual (progressive estrogen-driven tissue changes), not acute.
- **Progression:** Untreated, gynecomastia is **progressive**, sometimes requiring repeated surgical mastectomy (one reported patient underwent mastectomy twice before pharmacologic diagnosis/treatment; PMC11614628). Bone maturation advances progressively through childhood, culminating in premature epiphyseal fusion and **halted linear growth**, yielding short adult stature despite early tall stature.
- **Disease course pattern:** Chronic, non-remitting without treatment (there is no spontaneous resolution because the causal genomic rearrangement is permanent); pharmacologic (aromatase-inhibitor) treatment can arrest/reverse gynecomastia and normalize growth trajectory if started early.
- **Critical period:** Early-childhood to peripubertal initiation of aromatase-inhibitor therapy is critical — case data show that starting letrozole around ages 6–7 achieves near-target adult height and can **prevent** gynecomastia from developing at all, versus later-diagnosed patients who require surgery (Frontiers 2024, PMC11614628: "Long term effects of aromatase inhibitor treatment in patients with aromatase excess syndrome").

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Orphanet lists AEXS as **<1 per 1,000,000** — among the rarest recognized Mendelian endocrine disorders; total reported cases in the literature number only in the dozens of individuals across a limited number of families since the first molecular description in 2003.

**Inheritance pattern:** **Autosomal dominant** (Orphanet ORPHA:178345). Males and females are affected with equal genetic transmission risk (50% per child of an affected parent, of either sex), although clinical **expressivity is markedly sex-biased** — males show florid, medically significant phenotypes (gynecomastia, growth abnormalities) while female carriers are frequently mildly affected or entirely asymptomatic, reflecting the fact that the baseline estrogen milieu in females partially masks the pathologic excess.

**Penetrance/expressivity:** Biochemically, all carriers appear to have elevated E1/E2-to-androgen ratios; clinically, penetrance for overt gynecomastia in males is high, while in females symptomatic penetrance is incomplete (~6 of 8 reported women had ≥1 symptom in one series; 2 were phenotypically normal — Stratakis et al., 1998, PMID:9543166).

**Genetic anticipation:** Not described/reported for AEXS.

**Germline mosaicism:** Not specifically reported, though de novo cases have occurred (implying either true de novo events or unrecognized parental mosaicism).

**Founder effects:** Each reported family/pedigree carries a distinct, private rearrangement (no shared recurrent founder allele identified across the literature) — consistent with the disease arising from independent recombination/replication errors at a rearrangement-prone genomic region rather than a single ancestral mutation.

**Consanguinity role:** Not relevant — autosomal dominant disorder, unrelated to consanguinity (which is classically associated with autosomal recessive disease).

**Carrier frequency:** Not applicable in the traditional AR sense (this is dominant), and no population carrier-frequency estimate exists given extreme rarity.

**Population demographics:**
- **Affected populations:** Cases reported across diverse ancestries (Japanese, European, and other cohorts in the literature — Fukami/Ogata groups in Japan have described the largest number of molecularly confirmed families); no clear ethnic predilection established.
- **Geographic distribution:** No endemic clustering; case reports are globally distributed but concentrated in centers with pediatric endocrine/molecular genetics expertise (notably Japan, given the Fukami/Shozu/Ogata research program).
- **Sex ratio:** Reporting bias strongly favors male ascertainment because males present with the more obvious, medically actionable phenotype (gynecomastia); true underlying sex ratio of the genetic trait itself is 1:1 given autosomal dominant inheritance.
- **Age distribution:** Diagnosis typically occurs in childhood/adolescence (peripubertal gynecomastia is usually the presenting complaint that triggers genetic workup), though some cases (e.g., the letrozole case in PMC11614628) were diagnosed and treated as late as young adulthood (age 19) after years of undiagnosed, progressively worsening gynecomastia.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Endocrine panel:** Serum estrone (E1), estradiol (E2), testosterone (T), androstenedione (Δ4), LH, FSH. Key diagnostic pattern: **markedly elevated E1 and elevated E2/T (or E1/androgen) ratio**, with **low/normal androgens** and **suppressed, poorly GnRH-responsive FSH** (FSH-dominant hypogonadotropic hypogonadism) with grossly normal baseline LH (Fukami et al., 2012, PMC3272822). Note serum estradiol is reportedly elevated in only ~48% of affected males, so a normal E2 does **not** exclude AEXS — E1 and the E1/E2-to-androgen ratio are more sensitive.
- **hCG stimulation test:** Generally shows preserved testicular testosterone responsiveness, supporting that the primary lesion is aromatase overexpression/central feedback rather than primary gonadal failure.
- **Imaging:** Bone-age radiograph (hand/wrist) shows advancement relative to chronological age; breast ultrasound/mammography to characterize gynecomastia/macromastia and exclude tumor.
- **Tissue-based aromatase activity assay:** Increased aromatase activity demonstrable in cultured skin fibroblasts and lymphocytes — a classic functional confirmatory test predating routine genomic sequencing.
- **Biopsy/histopathology:** Breast tissue in surgical mastectomy specimens shows typical gynecomastia histology (ductal hyperplasia, periductal fibrosis/stroma) — nonspecific to AEXS but supports the estrogen-excess mechanism.

**Genetic testing (definitive/mandatory for diagnosis):**
- Molecular confirmation of a *CYP19A1* structural rearrangement is **mandatory** to confirm the AEXS diagnosis (Fukami et al., 2012; MalaCards/OMIM). Approach:
  - **RT-PCR** of RNA from skin fibroblasts or lymphocytes to detect **aberrant/chimeric *CYP19A1* transcripts** (e.g., *DMXL2*-*CYP19A1* fusion transcripts, or transcripts driven by *CGNL1/TMOD3/MAPK6/TLN2* exon 1).
  - **Long-range genomic PCR and Southern blotting** to map duplication/deletion breakpoints.
  - **Array-CGH / chromosomal microarray** can detect the larger deletions/duplications (tens to hundreds of kb) but may miss balanced inversions.
  - **Genome sequencing (WGS)** is increasingly the most efficient way to detect and precisely map all three rearrangement classes (duplication, deletion, inversion) in a single test, since standard exome sequencing (WES) and gene panels targeting only coding exons can **miss** these predominantly noncoding/regulatory structural events.
  - **Karyotype/FISH:** Standard karyotyping is insufficient (rearrangements are submicroscopic); FISH with targeted BAC probes spanning 15q21.2 could in principle detect larger events but is not the standard approach.
  - **Mitochondrial DNA/repeat expansion testing:** Not applicable.

**Clinical diagnostic criteria:** No formal consensus diagnostic criteria society statement exists (given rarity); diagnosis rests on the combination of (1) characteristic phenotype (peripubertal gynecomastia/macromastia, advanced bone age, short predicted adult height), (2) biochemical estrogen excess with suppressed FSH, and (3) molecular confirmation of a *CYP19A1* rearrangement.

**Differential diagnosis:**
- **Aromatase-producing tumors** (e.g., estrogen-secreting Sertoli-cell testicular tumors, as seen in **Peutz–Jeghers syndrome**, or adrenal/gonadal tumors) — an important differential because tumoral aromatase excess can mimic AEXS biochemically but is somatic/localized rather than germline (Berkovitz et al., 1991, *N Engl J Med*, "An Aromatase-Producing Sex-Cord Tumor Resulting in Prepubertal Gynecomastia").
- **McCune–Albright syndrome** (GNAS activating mutations) — can present with precocious puberty and gonadal hyperfunction including estrogen excess via a different (G-protein/cAMP) mechanism.
- **Testotoxicosis** (familial male-limited precocious puberty, LHCGR mutations) — precocious puberty but driven by androgen rather than estrogen excess.
- **Exogenous estrogen exposure** (dietary, topical, environmental xenoestrogens) — must be excluded by history.
- **Klinefelter syndrome and other causes of pubertal gynecomastia** — excluded by karyotype/clinical context.
- **Idiopathic pubertal gynecomastia** (common, usually self-limited) — the much more prevalent "look-alike," distinguished from AEXS by persistence, severity, family history, and biochemical/genetic confirmation.

**Screening:** No population-based or newborn screening program exists (extreme rarity); case-finding relies on clinical recognition of familial or severe peripubertal gynecomastia followed by targeted biochemical and molecular workup. Cascade testing of at-risk first-degree relatives is appropriate once a proband's rearrangement is identified, given autosomal dominant transmission with 50% risk.

---

## 11. Outcome/Prognosis

**Survival/mortality:** AEXS is **not associated with increased mortality**; it is a chronic endocrine disorder without a known lethal complication pathway. No survival/mortality statistics are reported in the literature (consistent with the condition not being life-limiting).

**Morbidity and function:**
- **Growth:** Untreated, the classic outcome is childhood tall/accelerated stature followed by **premature epiphyseal fusion and short adult stature** — a key long-term morbidity.
- **Gynecomastia/macromastia:** Progressive without treatment; may necessitate repeated surgical mastectomy, with associated surgical morbidity and psychosocial impact.
- **Gonadal function:** Hypogonadotropic hypogonadism can persist into adulthood, though **fertility has been reported to remain largely unaffected** in treated and some untreated male patients (general AEXS reviews).
- **Bone health beyond growth plates:** Long-term aromatase-inhibitor follow-up data show **no adverse effect on calcium metabolism markers or vertebral bone structure**, with "all markers of calcium metabolism ... within normal range" and no vertebral abnormalities on annual spine imaging during extended letrozole therapy (Frontiers 2024, PMC11614628).
- **Theoretical breast cancer risk:** Chronic untreated hyperestrogenemia is hypothesized in the literature to increase long-term breast cancer risk (by analogy with other chronic-estrogen-excess states and with the established chemopreventive role of aromatase inhibitors in breast cancer), motivating durable AI therapy, though AEXS-specific breast cancer incidence data are not available given the tiny total patient population.

**Complications:** Surgical complications from mastectomy in severe/inversion-type cases; psychosocial burden of gynecomastia in adolescents.

**Recovery potential:** With **early diagnosis and aromatase-inhibitor treatment**, gynecomastia can be **prevented entirely** or substantially reversed, adult height can be brought close to genetic target, testicular volume and virilization can improve, and libido/physical strength can improve even when treatment is started in adulthood (case report: letrozole initiated at age 19 improved testicular volume, virilization, physical strength, and libido) (Frontiers 2024, PMC11614628).

**Prognostic factors:** Rearrangement type (duplication < deletion < inversion in severity) and **age at treatment initiation** are the two dominant prognostic determinants identified in the literature — early (childhood) initiation of aromatase inhibitors is associated with the best height and gynecomastia-prevention outcomes.

---

## 12. Treatment

**Pharmacotherapy — mainstay of treatment: third-generation non-steroidal aromatase inhibitors.**
- **Letrozole:** the most extensively reported agent in long-term AEXS management. Reported dosing: initial doses of **1.25–2.5 mg/day**, subsequently titrated down to maintenance doses as low as **0.015–0.3 mg/day** based on hormone monitoring (Frontiers 2024, PMC11614628). Letrozole and anastrozole both suppress estrogen production by **97–99%** and are highly selective; letrozole has a longer half-life (2–4 days) than anastrozole, associated with higher achieved plasma testosterone concentrations.
- **Anastrozole:** used at reported doses of **1 mg/day** in duplication/deletion-type AEXS and **2–4 mg/day** in more severe inversion-type AEXS, with gynecomastia amelioration reported at these doses (Fukami et al., 2012, PMC3272822).
- **Exemestane:** also mentioned among agents used (steroidal, irreversible AI), though with less AEXS-specific outcome data than letrozole/anastrozole.
- **Important regulatory note:** Aromatase inhibitors are **not FDA-approved for any pediatric indication** and are used entirely **off-label** in children with AEXS (as they are also used off-label in Peutz-Jeghers syndrome, McCune-Albright syndrome, functional follicular ovarian cysts, and testotoxicosis) (Frontiers 2024, PMC11614628).

**Suggested NCIT terms for treatment annotation:**
- Pharmacotherapy: **NCIT:C15986**
- Specific agents (therapeutic_agent slot, CHEBI where available): letrozole (CHEBI:6413), anastrozole (CHEBI:2704), exemestane (CHEBI:135890) — verify via OAK before curation.
- Aromatase-inhibitor drug class: consider **NCIT:C1591** (Aromatase Inhibitor) if reachable from the treatment-term root, else use therapeutic_agent with the specific CHEBI compound.

**Surgical/interventional:**
- **Mastectomy (subcutaneous/simple):** performed for established, severe, or refractory gynecomastia, particularly in inversion-type (most severe) cases; one case report documents **mastectomy performed twice** prior to pharmacologic diagnosis, with **no recurrence over 10-year follow-up** after subsequent letrozole therapy (Frontiers 2024, PMC11614628). Suggested **NCIT:C51571** (Mastectomy) or the general surgical-procedure term **NCIT:C15329**.

**Supportive/monitoring:**
- Regular endocrinological follow-up with hormone panel monitoring (E1/E2, T, LH, FSH) to titrate AI dosing and avoid supraphysiologic testosterone (a documented dose-limiting effect requiring adjustment).
- Annual bone-density/calcium-metabolism monitoring and spinal imaging during long-term AI therapy — reassuring safety data reported to date (no adverse vertebral or calcium-metabolism findings).
- Bone-age monitoring to assess growth-plate status and guide predicted adult height counseling.

**Genetic counseling:** Recommended for affected families given autosomal dominant inheritance and 50% transmission risk; cascade testing of at-risk relatives once the familial rearrangement is characterized. Suggested **NCIT:C15240** (Genetic Counseling).

**Experimental/investigational:** No AEXS-specific clinical trials are registered (extreme rarity precludes conventional trial design); management is derived entirely from case-report/case-series experience and extrapolation from the breast-cancer aromatase-inhibitor literature.

**Treatment outcomes (letrozole, long-term follow-up, PMC11614628 / Frontiers 2024, and the related JCEM report "Long-term Effect of Aromatase Inhibition in Aromatase Excess Syndrome"):**
- Height: a male patient started on letrozole at age 6–7 achieved **178.8 cm** adult height, within/exceeding target range, an improvement of roughly **+8.4 cm** versus pretreatment height prediction; a female patient started at age 11 reached **158 cm**, within target range.
- Gynecomastia: early initiation **prevented** gynecomastia development entirely in one patient; no recurrence after mastectomy plus subsequent AI therapy over 10 years in another.
- Testicular volume: progressive increase from prepubertal (~1 mL) to adult (up to 8 mL) volumes with treatment.
- Safety: **no observed treatment-related side effects** in the reported long-term follow-up cohort; the main managed adverse finding was iatrogenic **supraphysiologic testosterone**, corrected by dose titration.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense — AEXS is a germline monogenic (structural) disorder; there is no modifiable primary-prevention strategy to prevent the genetic rearrangement itself. The only "primary prevention" avenue is reproductive: genetic counseling and, where desired, prenatal diagnosis or preimplantation genetic testing (PGT) for known familial rearrangements, given the well-characterized autosomal dominant, 50%-risk inheritance pattern.

**Secondary prevention (early detection/treatment to prevent morbidity):** This is where AEXS management is most impactful — **early pharmacologic intervention (aromatase inhibitors) started in early-to-mid childhood, before or at the earliest signs of gynecomastia/accelerated bone age, can prevent the major downstream morbidities** (established gynecomastia requiring surgery, and short adult stature from premature epiphyseal fusion). This is supported directly by the long-term follow-up data showing height outcomes near genetic target and gynecomastia prevention with early letrozole initiation (Frontiers 2024, PMC11614628).

**Tertiary prevention:** Once gynecomastia or macromastia is established, aromatase-inhibitor therapy plus, if needed, mastectomy prevents progression/recurrence and can improve associated hypogonadal features (virilization, testicular volume, libido) even when started in adulthood.

**Screening/genetic counseling:** Cascade family screening (biochemical ± molecular) of first-degree relatives of a confirmed proband is the principal "screening" strategy, enabling presymptomatic identification of at-risk children so that AI therapy can be started as early as possible — the single largest lever on long-term outcome identified in the literature. Suggested **NCIT:C15240** (Genetic Counseling).

**Public health/environmental interventions:** Not applicable (no environmental causal factor).

**Prophylaxis:** Early/prophylactic aromatase-inhibitor initiation in genetically confirmed, pre-symptomatic at-risk children functions as disease-modifying prophylaxis against the two major morbidities (gynecomastia, growth-plate-driven short stature), per the case evidence above.

---

## 14. Other Species / Natural Disease

**Naturally occurring AEXS in other species:** No naturally occurring veterinary/companion-animal cases of an AEXS-equivalent genetic disorder have been reported in the literature reviewed; this is consistent with AEXS being an extremely rare human structural-rearrangement disorder with no described veterinary correlate in OMIA or similar databases.

**Orthologous gene:** *Cyp19a1* is well conserved across mammals (mouse *Cyp19a1*, NCBI Gene ID 11594), and aromatase biology (androgen-to-estrogen conversion) is broadly conserved, but no spontaneous *Cyp19a1* gain-of-function structural rearrangement disease has been documented in any non-human species.

**Comparative biology:** The evolutionary conservation of aromatase's catalytic mechanism (cytochrome P450 aromatization chemistry) underlies the utility of rodent aromatase-overexpression **transgenic** models (see Section 15) for studying the human syndrome's downstream consequences, even though the transgenic models are engineered rather than naturally occurring.

**Zoonotic potential/transmission:** Not applicable — AEXS is a non-communicable, purely genetic disorder.

---

## 15. Model Organisms

**Genetic (transgenic) mouse models of aromatase overexpression** are the principal experimental system recapitulating AEXS pathophysiology, though they are engineered rather than naturally arising with the human-specific chimeric-transcript mechanism:

- **Aromatase-overexpression transgenic mice ("AROM+ mice" and related lines):**
  - "Overexpression of aromatase in transgenic male mice results in the induction of gynecomastia and other biochemical changes in mammary glands" (PMID:11358670) — male transgenic mice overexpressing aromatase develop **mammary gland changes histologically resembling human gynecomastia**, with increased estrogen and progesterone receptor expression, increased proliferative/cell-cycle gene expression, and elevated growth factors (bFGF, TGF-β) in mammary tissue — directly recapitulating the breast phenotype of human AEXS.
  - **Testicular phenotype:** Aromatase-overexpressing transgenic male mice also develop **Leydig cell tumors**, described as "An in Vivo Model for Hormone-Mediated Testicular Cancer" (*Am J Pathol*) — a gonadal consequence not prominently reported in human AEXS but relevant to understanding chronic intratesticular estrogen-excess signaling.
  - **Female phenotype:** Aromatase overexpression in these models also produces mammary hyperplastic/dysplastic lesions in female transgenic mice, paralleling the macromastia seen in human female AEXS carriers.
  - **Pharmacologic validation/chemoprevention utility:** The aromatase-overexpression transgenic mouse model has been used to validate **letrozole** as a chemopreventive/therapeutic agent — "aromatase overexpression transgenic mice model: cell type specific expression and use of letrozole to abrogate mammary hyperplasia without affecting normal physiology" (PMID:11850204) — low-dose letrozole reversed the mammary hyperplastic phenotype **without significantly altering circulating estradiol or FSH levels**, supporting the translational rationale for low-dose letrozole titration used in human AEXS patients.

**Model characteristics — fidelity and limitations:**
- **Recapitulation:** The transgenic mouse model faithfully reproduces the core estrogen-excess mammary phenotype (gynecomastia-like histology in males, hyperplasia in females) and demonstrates aromatase-inhibitor responsiveness, directly supporting the mechanistic and therapeutic logic applied in human AEXS.
- **Limitations:** These models use a **generic transgenic overexpression construct**, not the human-specific chimeric-promoter/rearrangement mechanisms (duplication/deletion/inversion with donor genes *DMXL2, CGNL1, TMOD3, MAPK6, TLN2*) that define human AEXS — so tissue-specificity and expression-level nuances captured by the human rearrangement classification (duplication vs. deletion vs. inversion severity gradient) are **not modeled**. Additionally, the murine testicular Leydig cell tumor phenotype has no clear human AEXS counterpart in the reported case literature, illustrating a species-specific divergence.
- **Complementary model — aromatase-deficient mouse (ArKO):** The reciprocal loss-of-function *Cyp19a1* knockout mouse (aromatase-deficient) is well established as a model of the opposite human disease (aromatase deficiency) and, by contrast, helps define the estrogen-dependent processes (bone maturation, feedback suppression of gonadotropins) whose gain-of-function analogs are disrupted in AEXS.

**Research applications:** These transgenic models are primarily used to (1) study estrogen-driven mammary tumorigenesis/hyperplasia mechanisms, (2) validate aromatase-inhibitor pharmacology and dosing strategies later applied clinically, and (3) probe the hypothalamic–pituitary feedback consequences of chronic peripheral estrogen excess.

**Resources:** Mouse Genome Informatics (MGI) carries the relevant *Cyp19a1* transgenic and knockout allele records; no zebrafish, *Drosophila*, or *C. elegans* AEXS-specific models were identified in this search (aromatase/estrogen signaling is not conserved in most invertebrate model systems in a way that would recapitulate this vertebrate-specific endocrine disease).

---

## Summary Table: Key Ontology Term Suggestions

| Domain | Term | ID |
|---|---|---|
| Disease | Aromatase excess syndrome | MONDO:0007690 / OMIM:139300 / ORPHA:178345 |
| Gene | CYP19A1 | HGNC:2594 |
| Phenotype | Gynecomastia | HP:0100295 |
| Phenotype | Hypogonadotropic hypogonadism | HP:0000044 |
| Phenotype | Short stature | HP:0004322 |
| Phenotype | Precocious puberty | HP:0000826 |
| Biological process | Estrogen biosynthetic process | GO:0006703 |
| Molecular function | Aromatase activity | GO:0070330 |
| Cellular component | Endoplasmic reticulum membrane | GO:0005789 |
| Anatomy | Breast | UBERON:0000310 |
| Anatomy | Testis | UBERON:0000473 |
| Treatment | Pharmacotherapy | NCIT:C15986 |
| Treatment | Mastectomy | NCIT:C51571 |
| Treatment | Genetic Counseling | NCIT:C15240 |

*(Ontology term IDs above should be verified against the local OAK adapters — sqlite:obo:hp, sqlite:obo:go, ols:ncit, etc. — per dismech curation SOP before insertion into KB YAML; some (e.g., exact NCIT drug/class codes, precise HPO term for "advanced bone age") were not independently OAK-verified in this research pass and require confirmation.)*

---

## Key Primary Citations

1. Shozu M, Sebastian S, Takayama K, Hsu WT, Schultz RA, Neely K, Bryant M, Bulun SE. "Estrogen excess associated with novel gain-of-function mutations affecting the aromatase gene." *N Engl J Med*. 2003;348(19):1855–1865. PMID:12736278. [nejm.org](https://www.nejm.org/doi/full/10.1056/NEJMoa021559)
2. Stratakis CA, et al. "The aromatase excess syndrome is associated with feminization of both sexes and autosomal dominant transmission of aberrant P450 aromatase gene transcription." *J Clin Endocrinol Metab*. 1998. PMID:9543166. [pubmed](https://pubmed.ncbi.nlm.nih.gov/9543166/)
3. Fukami M, et al. "Aromatase excess syndrome: identification of cryptic duplications and deletions leading to gain of function of CYP19A1 and assessment of phenotypic determinants." *J Clin Endocrinol Metab*. 2011;96(6):E1035–E1043. PMID:21470988. [academic.oup.com](https://academic.oup.com/jcem/article/96/6/E1035/2833840)
4. Fukami M, Miyado M, Ogata T. "Molecular Bases and Phenotypic Determinants of Aromatase Excess Syndrome." *Int J Endocrinol*. 2012;2012:584807. PMC3272822. [ncbi.nlm.nih.gov/pmc/articles/PMC3272822](https://pmc.ncbi.nlm.nih.gov/articles/PMC3272822/)
5. Fukami M, et al. "Genomic Basis of Aromatase Excess Syndrome: Recombination- and Replication-Mediated Rearrangements Leading to CYP19A1 Overexpression." *J Clin Endocrinol Metab*. 2013;98(12):E2013–E2021. PMID:24064691. [academic.oup.com](https://academic.oup.com/jcem/article/98/12/E2013/2833609)
6. Fukami M, Miyado M, Nagasaki K, Shozu M, Ogata T. "Understanding the pathological manifestations of aromatase excess syndrome: lessons for clinical diagnosis." *Expert Rev Endocrinol Metab*. 2014. PMID:25264451. [tandfonline.com](https://www.tandfonline.com/doi/full/10.1586/17446651.2014.926810)
7. Local aromatase excess with recruitment of unusual promoters of CYP19A1 gene in prepubertal patients with gynecomastia. PMID:35667691.
8. "Long term effects of aromatase inhibitor treatment in patients with aromatase excess syndrome." *Front Endocrinol*. 2024. PMC11614628. [pmc.ncbi.nlm.nih.gov/articles/PMC11614628](https://pmc.ncbi.nlm.nih.gov/articles/PMC11614628/)
9. "Long-term Effect of Aromatase Inhibition in Aromatase Excess Syndrome." *J Clin Endocrinol Metab*. 2021;106(5):1491. [academic.oup.com](https://academic.oup.com/jcem/article-abstract/106/5/1491/6123853)
10. Berkovitz GD, et al. "An Aromatase-Producing Sex-Cord Tumor Resulting in Prepubertal Gynecomastia." *N Engl J Med*. 1991;324:1701–1705. [nejm.org](https://www.nejm.org/doi/full/10.1056/NEJM199101313240507) (differential diagnosis reference)
11. Overexpression of aromatase in transgenic male mice results in the induction of gynecomastia and other biochemical changes in mammary glands. PMID:11358670.
12. Aromatase overexpression transgenic mice model: cell type specific expression and use of letrozole to abrogate mammary hyperplasia without affecting normal physiology. PMID:11850204.
13. OMIM #139300 — AROMATASE EXCESS SYNDROME; AEXS. [omim.org/entry/139300](https://omim.org/entry/139300)
14. Orphanet ORPHA:178345 — Aromatase excess syndrome. [orpha.net](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=EN&Expert=178345)
15. MedlinePlus Genetics — Aromatase excess syndrome. [medlineplus.gov](https://medlineplus.gov/download/genetics/condition/aromatase-excess-syndrome.pdf)

**Note on evidence gaps:** This report is compiled from a search-engine/web-fetch research pass, not from directly opened PubMed abstract pages for every citation. Per dismech SOP, **every PMID and every quoted snippet above must be independently re-verified against the cached PubMed abstract** (`just fetch-reference PMID:XXXX` + `just count-verified-snippets`) before any text is copied into a `kb/disorders/Aromatase_Excess_Syndrome.yaml` evidence block — several quotes here are paraphrased summaries from secondary web sources (e.g., PMC full-text summarized via WebFetch) rather than confirmed verbatim abstract substrings, and NEC preflight (`just preflight-dr`, causal gene = *CYP19A1*, MONDO:0007690) should be run as an extra safeguard given this report was not produced by the standard dismech deep-research pipeline.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:24064691`: "recombination- and replication-mediated rearrangements"
  - Text part not found as substring: 'recombination- and replication-mediated rearrangements' (note: only abstract available for PMID:24064691, full text may contain this excerpt)
- `PMID:24064691`: "a truly original mechanism of a gain-of-function mutation"
  - closest text in source: "However, mutation spectrum, clinical consequences, and underlying mechanisms of these rearrangements remain to be elucidated"
- `PMID:12736278`: "a truly original mechanism of a gain-of-function mutation"
  - Text part not found as substring: 'a truly original mechanism of a gain-of-function mutation' (note: only abstract available for PMID:12736278, full text may contain this excerpt)