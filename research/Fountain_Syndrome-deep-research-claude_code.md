---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T05:14:16.750937'
end_time: '2026-07-31T05:18:34.437531'
duration_seconds: 257.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fountain Syndrome
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 23
  total_cost_usd: 1.5464816000000001
  session_id: 4c1993f9-a9f9-5903-a02b-2767d17a8463
  stop_reason: end_turn
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fountain Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fountain Syndrome** covering all of the
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

# Fountain Syndrome — Comprehensive Research Report

## ⚠️ Critical Naming Disambiguation (Read First — High Named-Entity-Confusion Risk)

There are **two distinct, unrelated conditions that share the "Fountain" name**, and literature searches conflate them constantly. This is a textbook Named Entity Confusion (NEC) hazard:

| | **Fountain syndrome** (this report's primary target) | **Hao-Fountain syndrome (HAFOUS)** — a *different* disorder |
|---|---|---|
| OMIM | [#229120](https://omim.org/entry/229120) | [#616863](https://omim.org/entry/616863) |
| Orphanet | [ORPHA:3219](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=3219) | [ORPHA:643549](https://orpha.net/en/disease/detail/643549) |
| Gene | **Unknown** — molecular basis never identified | **USP7** (ubiquitin-specific protease 7), 16p13.2 |
| Inheritance | Autosomal recessive | Autosomal dominant (de novo) |
| First described | Fountain, 1974 (eponym source) | Hao et al. and Fountain (a *different* Fountain — co-author) et al., 2015 |
| Cases in literature | ~7 patients across 2 families total | Growing cohort; 32 novel patients in a 2024 series alone |
| ICD-10-CM (2026) | No dedicated code — falls under generic Q87.8/Q87.89 | **Q87.87** (new dedicated code, effective Oct 2025) |
| Active research/clinical trials | None found | Active (episignature studies, natural history cohorts) |

**These are not variant names for the same disease** — they are two separate eponymous syndromes that happen to both trace to a clinician surnamed Fountain. Because Hao-Fountain syndrome is far better characterized, actively studied, and now has its own ICD-10-CM code, any AI/DR tool or literature search for "Fountain syndrome" is at high risk of silently substituting Hao-Fountain (USP7) content. **All content below pertains to the original OMIM #229120 entry** unless explicitly labeled otherwise. If curating a dismech entry, this distinction should be treated with the same rigor as the project's documented NEC preflight (synonym/gene/OMIM cross-check against MONDO).

Given this is a genuinely ultra-rare, molecularly uncharacterized syndrome (2 published families, no gene identified in over 50 years), most of the 15 requested sections below are honestly sparse — this reflects the true state of the literature, not incomplete research. Where information does not exist, that is stated explicitly rather than inferred or extrapolated from Hao-Fountain syndrome.

---

## 1. Disease Information

**Overview:** Fountain syndrome is an extremely rare autosomal recessive congenital multisystem disorder characterized by intellectual disability, sensorineural deafness, skeletal abnormalities (notably calvarial thickening and short broad hands), and a coarse facial appearance with full/everted lips, in some patients progressing to lip swelling with granulomatous mass formation.

**Key identifiers:**
- **OMIM:** [#229120](https://omim.org/entry/229120) — FOUNTAIN SYNDROME
- **Orphanet:** [ORPHA:3219](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=3219)
- **MONDO:** MONDO:0009241 (identified via Wikidata/GARD cross-reference; **not independently confirmed against the live Monarch MONDO record** during this research pass — verify with `runoak -i sqlite:obo:mondo info MONDO:0009241 -O obo` before curation use)
- **ICD-10/ICD-11:** No dedicated code exists; would be coded under the non-specific ICD-10-CM Q87.8/Q87.89 ("Other specified congenital malformation syndromes, not elsewhere classified")
- **MeSH indexing** (per PubMed record for the original 1974 report): abnormal skeletal features, genetic deafness, intellectual disability, skin granuloma, gingival/lip disease manifestations

**Synonyms:**
- Fountain's syndrome
- Deafness with skeletal dysplasia and lip granuloma syndrome
- Deafness-skeletal dysplasia-coarse face with full lips syndrome
- Hearing loss-skeletal dysplasia-lip granuloma syndrome
- Mental retardation-deafness-skeletal abnormalities-coarse face with full lips syndrome

**Evidence source:** All available information derives from **aggregated, published case-series/case-report literature** (2 families, total of ~7 affected individuals), not from any EHR cohort, registry, or large-scale genomic database — this disease is too rare for population-level resources (gnomAD, GWAS Catalog, disease registries) to contain meaningful entries.

---

## 2. Etiology

- **Disease causal factors:** Genetic; presumed single-gene autosomal recessive etiology based on segregation pattern (affected sibs of unaffected parents, both sexes affected, in both reported families). **The causal gene has never been identified or mapped** — over 50 years since the original description, no molecular/positional cloning study has been published. OMIM classifies this as a phenotype-only entry with no associated gene.
- **Genetic risk factors:** Presumed biallelic loss-of-function at an unknown locus. No candidate gene, linkage interval, or ClinVar/ClinGen assertions exist. Consanguinity was not explicitly reported as a feature of either published family, though autosomal recessive inheritance in isolated sibships is consistent with unrecognized shared ancestry.
- **Environmental risk factors:** None reported or plausible given the presumed monogenic recessive pattern.
- **Protective factors:** Not applicable/not studied — no population-scale variant or outcome data exist to identify protective alleles.
- **Gene-environment interactions:** Not studied; no data.

---

## 3. Phenotypes

Because the disorder is documented in only two published families, phenotype "frequencies" below are counts/impressions from the primary literature rather than statistically robust percentages. All phenotype claims trace to:
- Fountain RB, 1974, *Proc R Soc Med* 67(9):878-9, PMID:[4431800](https://pubmed.ncbi.nlm.nih.gov/4431800/) — original family (3 brothers + 1 sister)
- Fryns JP, Dereymaeker AM, Hoefnagels M, Van den Berghe H, 1987, *Am J Med Genet* 26(3):551-5, PMID:[3565469](https://pubmed.ncbi.nlm.nih.gov/3565469/) — confirmatory second family (3 moderately-to-severely mentally retarded males: 2 brothers and 1 isolated patient)
- Fryns JP, 1989, *J Med Genet* 26(11):722-4 ("Syndrome of the month" review), PMID:[2585470](https://pubmed.ncbi.nlm.nih.gov/2585470/) — synthesis/review of the above

| Phenotype | Type | Suggested HP term | Notes |
|---|---|---|---|
| Intellectual disability | Neurodevelopmental | HP:0001249 (Intellectual disability) | Reported "moderate to severe" in the second family; core feature in all reported patients |
| Sensorineural hearing loss | Clinical sign / lab-imaging | HP:0000407 (Sensorineural hearing impairment) | Attributed to malformation of cochlear structures on tomography in the original family |
| Coarse facial features | Physical/dysmorphic | HP:0000280 (Coarse facial features) | Core diagnostic feature |
| Full/everted lips | Physical/dysmorphic | HP:0012471 (Thick vermilion border) / HP:0000232 (Everted lower lip vermillion) | Progressive lip swelling reported in 2 of the original 4 sibs |
| Lip granuloma / eroded granulomatous mass | Physical sign | Best mapped to a general "abnormal lip morphology" HP term — no precise HP term for granulomatous lip mass identified | Reported in 1 of the original patients; a distinguishing, unusual feature |
| Calvarial thickening | Skeletal/imaging | HP:0002684 (Thickened calvaria) | Marked, described in original family |
| Short, stubby hands with broad terminal phalanges | Skeletal | HP:0009882 (Short distal phalanx of finger) / HP:0001167 (Abnormality of the hand) | Consistent across reports |
| Spina bifida | Skeletal (one patient only) | HP:0002414 (Spina bifida) | Reported in 1 of Fountain's original 4 patients; not a core/obligate feature |

**Age of onset:** Congenital/infantile — features (facial coarsening, deafness, developmental delay) are described as apparent from infancy/early childhood in both reports.

**Severity/progression:** Facial/lip changes were noted as *progressive* (worsening swelling over time) in the original family; intellectual disability was static/non-degenerative (a congenital malformation-type disorder, not a neurodegenerative one).

**Quality of life impact:** Not formally studied (no EQ-5D/SF-36 or disease-specific QOL instrument data exist). Given moderate-severe intellectual disability and hearing loss, substantial lifelong impact on communication, education, and independence would be expected but is not empirically quantified in the literature.

**Behavioral note:** The original description specifically remarked that all 5 examined patients (across both families, per the 1989 review) had "remarkably friendly behavior" — an informal but repeatedly noted behavioral/temperament observation.

---

## 4. Genetic/Molecular Information

- **Causal genes:** **None identified.** No gene has ever been mapped, linked, or sequenced to this phenotype. This is the single most important curation caveat for this entry.
- **Pathogenic variants:** Not applicable — no gene, therefore no variant classification, ACMG/AMP tier, allele frequency, or functional consequence data exist.
- **Modifier genes:** None reported.
- **Epigenetic information:** None reported.
- **Chromosomal abnormalities:** None reported; the two published families show no karyotype/microarray abnormalities described (though molecular cytogenetic evaluation using modern methods, e.g., CMA or exome/genome sequencing, does not appear to have ever been performed or published for either family, to the best of this search).

**Important negative note for curators:** Do NOT attach the **KCTD3** gene (OMIM *613272*, chromosome 1q41) to this entry. KCTD3 appeared in preliminary searches because of general keyword overlap ("Fountain" + intellectual disability–type searches surfaced KCTD3/HCN3 mouse-brain interaction literature), but no publication was found linking KCTD3 to Fountain syndrome (OMIM 229120) specifically — this looks like a search-engine co-occurrence artifact, not an established gene-disease relationship. Likewise, do NOT attach **USP7** (the Hao-Fountain gene) — see Section 0/disambiguation above.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious triggers are implicated or reported. This is presented as a purely genetic congenital malformation syndrome.

---

## 6. Mechanism / Pathophysiology

**This is the section with the largest evidence gap.** Because no causal gene has been identified, there is no molecular pathway, protein dysfunction, or mechanistic literature to cite — mechanism sections describing "molecular pathways," "protein dysfunction," "metabolic changes," "immune involvement," etc. are **not available** for this disease and should not be fabricated or extrapolated from superficially similar syndromes.

What *can* be stated from the phenotypic descriptions (purely observational/anatomic, not mechanistic):
- **Bone abnormality mechanism (descriptive only):** marked calvarial thickening and short/broad distal phalanges suggest a skeletal dysplasia-type process, but no histopathological, radiographic-quantitative, or biochemical (e.g., bone turnover marker) study has characterized this further.
- **Hearing loss mechanism (descriptive only):** tomography in the original family showed "congenital anomalies of the cochlea," consistent with a structural inner-ear malformation (a Cell/GO-term-level cochlear developmental process such as GO:0043588 "skin development" is not relevant; a more fitting anatomic anchor would be UBERON:0002099 [cochlea] with no specific molecular process identified).
- **Lip/facial soft-tissue mechanism (descriptive only):** described as "excessive accumulation of body fluids under the skin" (per NORD/GARD lay summaries) progressing to granulomatous change in one patient — no histopathology report with immunohistochemistry, no identified inflammatory/immune mechanism, and no biopsy-based cellular characterization was located in the primary literature.

No transcriptomic, proteomic, metabolomic, single-cell, or spatial-omics data exist for this condition (unsurprising given it predates the genomics era and has never been revisited with modern sequencing, as far as this search could determine).

---

## 7. Anatomical Structures Affected

- **Organ/system level:**
  - Skeletal system (calvaria, hands/phalanges; one patient with spina bifida — axial skeleton)
  - Auditory system (inner ear/cochlea — sensorineural hearing loss)
  - Craniofacial soft tissue (lips, cheeks — coarse facies, granulomatous lip swelling)
  - Central nervous system (intellectual disability — though no neuroimaging or neuropathology findings were reported)
- **Suggested UBERON terms:** UBERON:0003128 (calvaria), UBERON:0002389 (hand), UBERON:0002099 (cochlea), UBERON:0016482 (lip), UBERON:0001016 (central nervous system) — anatomic anchors only; no cell-type- or subcellular-level data exist to support CL or GO Cellular Component annotation.
- **Tissue/cell level:** Not characterized — no biopsy-based cell population data.
- **Subcellular level:** Not characterized.
- **Lateralization:** Bilateral where described (bilateral sensorineural hearing loss, bilateral hand involvement); not applicable to facial/lip findings.

---

## 8. Temporal Development

- **Onset:** Congenital to infantile; facial coarsening, deafness, and developmental delay were apparent from infancy in reported cases.
- **Progression:** Facial/lip swelling described as *progressive* over time (worsening, culminating in granulomatous mass in one patient). Intellectual disability and hearing loss appear static (congenital, non-degenerative) rather than progressive, based on available descriptions.
- **Disease course pattern:** Chronic, lifelong, non-remitting — consistent with a congenital malformation syndrome rather than an episodic or relapsing-remitting condition.
- **Critical periods:** Not studied; no intervention-timing or developmental-window data exist.

---

## 9. Inheritance and Population

- **Epidemiology:** Orphanet lists prevalence as **<1 per 1,000,000** — among the rarest catalogued Mendelian phenotypes, with only ~7 patients across 2 families ever published.
- **Inheritance pattern:** Autosomal recessive (inferred from sibship recurrence with unaffected parents in both reported families; not molecularly confirmed since no gene/variant has been identified).
- **Penetrance/expressivity:** Not formally assessable — sample size is too small (2 families) for meaningful penetrance or variable-expressivity statistics; core features (ID, deafness, coarse facies) appear consistently present across all reported affected individuals, while some features (spina bifida, granulomatous lip mass) appear to be variable/incomplete.
- **Genetic anticipation, germline mosaicism, founder effects, carrier frequency:** No data — these require either multigenerational molecular data or a known gene, neither of which exists for this condition.
- **Consanguinity:** Not explicitly reported in either published family, though plausible given the recessive pattern and isolated sibship presentation.
- **Population demographics:** Both published families are European (Belgian — the Fryns reports originate from the Centre for Human Genetics, University of Leuven; geographic origin of the original 1974 Fountain report is UK-based per the Royal Society of Medicine venue, though patient ancestry is not specified in available abstracts). No data on other ethnic/geographic groups, no reported geographic clustering beyond these two reports, no sex-ratio data beyond the fact both sexes are affected (3 males + 1 female in the original family; 3 males in the second family — small numbers preclude a reliable sex-ratio estimate).

---

## 10. Diagnostics

- **Clinical tests reported historically:** Audiological/tomographic assessment of the cochlea (showing structural anomaly); skull/hand radiography (showing calvarial thickening and short broad distal phalanges).
- **Biomarkers:** None identified.
- **Genetic testing:** No gene-specific test exists (no known causal gene). Modern diagnosis, if attempted today, would necessarily rely on **clinical/radiographic pattern recognition** plus **exclusion of overlapping/better-characterized conditions** (most importantly, excluding Hao-Fountain syndrome via USP7 sequencing/deletion analysis, and excluding other coarse-facies + deafness + skeletal syndromes) rather than a confirmatory molecular test.
- **Omics-based diagnostics:** None reported/available.
- **Clinical criteria:** No formal consensus diagnostic criteria have been published; diagnosis in the literature is based on the gestalt of the four core features (intellectual disability, sensorineural deafness, skeletal changes, coarse face with full lips) as originally delineated by Fountain (1974) and confirmed by Fryns et al. (1987).
- **Differential diagnosis:** Must include (at minimum) Hao-Fountain syndrome (USP7-related; distinguished by autosomal dominant/de novo inheritance and different facial gestalt/behavioral profile), and other coarse-face + intellectual disability + deafness syndromes more broadly (e.g., mucopolysaccharidoses, which should be excluded via biochemical/enzymatic and GAG-storage testing given phenotypic overlap in coarse facies).
- **Screening:** No newborn, carrier, or population screening program exists or would be feasible without a known gene.

---

## 11. Outcome/Prognosis

No survival, mortality, life-expectancy, or longitudinal outcome data exist in the literature — the original reports are cross-sectional clinical descriptions, not longitudinal natural-history studies. No disability, complication-rate, or quality-of-life outcome data are available. No prognostic biomarkers exist.

---

## 12. Treatment

No disease-specific, gene-targeted, or FDA-approved therapy exists (unsurprising given no causal gene/pathway is known). Management described in secondary/lay sources (NORD/GARD) is entirely **supportive and symptomatic**, generalized from standard care for the component features rather than sourced from disease-specific trials:

- Hearing aids / audiological rehabilitation for sensorineural hearing loss (MAXO term candidate: not a precise match in the standard MAXO list provided in project guidance; general "supportive care," MAXO:0000950, would be the closest fit; a device-based approach would map to `therapeutic_modality: DEVICE`)
- Physical/occupational therapy and orthopedic follow-up for skeletal abnormalities (MAXO:0000011 physical therapy)
- Special-education/developmental support for intellectual disability
- Genetic counseling for recurrence-risk discussion given the recessive pattern (MAXO:0000079 genetic counseling)
- Surgical evaluation of lip granulomatous mass if functionally/cosmetically significant (no specific surgical outcome reported in the primary literature)

**No clinical trials, gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy exist or are in development for this condition** (searches of ClinicalTrials.gov-indexed literature returned no hits for "Fountain syndrome" OMIM:229120; all relevant hits were for Hao-Fountain/USP7).

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies are described beyond standard genetic counseling for at-risk families (relevant given the autosomal recessive pattern, once/if future affected relatives are identified). No immunization, screening program, or prophylaxis literature exists.

---

## 14. Other Species / Natural Disease

No naturally occurring animal model, veterinary case report, or cross-species orthology data were found for Fountain syndrome (OMIM 229120). This is unsurprising given the absence of an identified causal gene — there is no ortholog to search for in OMIA, MGI, or comparative pathology databases.

---

## 15. Model Organisms

**None exist.** No mouse, zebrafish, Drosophila, C. elegans, yeast, cell-line, organoid, or iPSC model has been generated or reported for this condition, again directly attributable to the absence of a known causal gene — model generation (knockout/knock-in/transgenic) is not possible without a target locus.

---

## Summary for Knowledge-Base Curation Purposes

Fountain syndrome (OMIM #229120) is an appropriate but **unusually evidence-sparse** candidate for a dismech entry: it is a genuine, distinct Mendelian phenotype with clear historical primary-literature support (2 independent published families, 3 citable PMIDs), but curators should expect that most schema slots requiring molecular/mechanistic detail (`genetic:`, `pathophysiology` biological-process/GO nodes, `molecular_functions`, gene-treatment `target_mechanisms`) will need to be **left empty or explicitly noted as unknown**, rather than populated — there is no gene to bind, no pathway to model, and no treatment mechanism beyond generic supportive care. The highest-value, best-evidenced content for a dismech entry would be the **phenotype** (`phenotypes:`) and **prevalence/inheritance** (`prevalence:`, `inheritance:`) sections drawn directly from the three PMIDs above, with heavy reliance on `notes:` fields (rather than fabricated `evidence:` snippets) for anything sourced only from secondary compilations (NORD/GARD/MalaCards/OMIM) whose underlying abstracts were not independently retrievable during this research pass (both direct OMIM.org and Orphanet fetches returned HTTP 403 in this environment — their content above is triangulated from search-result summaries and should be re-verified against the primary OMIM/Orphanet pages directly, e.g. via `just fetch-reference`, before being cited as `evidence:` in a KB entry). **Above all, the entry must not be conflated with Hao-Fountain syndrome (USP7, OMIM #616863)** — that is a separate, actively-studied disease that dominates any casual literature search for "Fountain syndrome" today.

### Key Citations
- Fountain RB. Familial bone abnormalities, deaf mutism, mental retardation and skin granuloma. *Proc R Soc Med.* 1974;67(9):878-9. PMID: [4431800](https://pubmed.ncbi.nlm.nih.gov/4431800/) (PMCID: PMC1645940) — original description, 4 sibs.
- Fryns JP, Dereymaeker AM, Hoefnagels M, Van den Berghe H. Mental retardation, deafness, skeletal abnormalities, and coarse face with full lips: confirmation of the Fountain syndrome. *Am J Med Genet.* 1987;26(3):551-5. PMID: [3565469](https://pubmed.ncbi.nlm.nih.gov/3565469/) — confirmatory second family, 3 males.
- Fryns JP. Fountain's syndrome: mental retardation, sensorineural deafness, skeletal abnormalities, and coarse face with full lips. *J Med Genet.* 1989;26(11):722-4. PMID: [2585470](https://pubmed.ncbi.nlm.nih.gov/2585470/) — "Syndrome of the Month" synthesis/review.

### Sources
- [OMIM #229120 — FOUNTAIN SYNDROME](https://omim.org/entry/229120)
- [OMIM #616863 — HAO-FOUNTAIN SYNDROME; HAFOUS](https://omim.org/entry/616863)
- [OMIM *613272 — KCTD3](https://www.omim.org/entry/613272)
- [Orphanet: Fountain syndrome (ORPHA:3219)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=3219)
- [Orphanet: Hao-Fountain syndrome due to USP7 mutation](https://www.orpha.net/en/disease/detail/643538)
- [GARD/NIH: Fountain syndrome](https://rarediseases.info.nih.gov/diseases/64/fountain-syndrome)
- [NORD: Fountain Syndrome](https://rarediseases.org/rare-diseases/fountain-syndrome/)
- [Wikipedia: Fountain syndrome](https://en.wikipedia.org/wiki/Fountain_syndrome)
- [Wikipedia: Hao-Fountain syndrome](https://en.wikipedia.org/wiki/Hao-Fountain_syndrome)
- [MalaCards: Fountain Syndrome](https://www.malacards.org/card/fountain_syndrome)
- [icd10data.com: Q87.87 Hao-Fountain Syndrome](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q80-Q89/Q87-/Q87.87)
- [Wimmer et al. 2024, Hao-Fountain syndrome: 32 novel patients, *Clinical Genetics*](https://onlinelibrary.wiley.com/doi/10.1111/cge.14480)
- PubMed: [4431800](https://pubmed.ncbi.nlm.nih.gov/4431800/), [3565469](https://pubmed.ncbi.nlm.nih.gov/3565469/), [2585470](https://pubmed.ncbi.nlm.nih.gov/2585470/)