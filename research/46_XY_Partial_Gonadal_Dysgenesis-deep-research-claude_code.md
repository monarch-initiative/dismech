---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T02:00:05.275203'
end_time: '2026-08-01T02:21:12.205702'
duration_seconds: 1266.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 46,XY partial gonadal dysgenesis
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
  - claude-opus-5[1m]
  web_search_requests: 20
  num_turns: 58
  total_cost_usd: 5.567871500000001
  session_id: 6c296ed2-cad5-4ae0-9db7-99e1f80070ae
  stop_reason: end_turn
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 46,XY partial gonadal dysgenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **46,XY partial gonadal dysgenesis** covering all of the
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

# Comprehensive Research Report: 46,XY Partial Gonadal Dysgenesis

**Report date:** 2026-08-01
**Target entity:** 46,XY partial gonadal dysgenesis (46,XY PGD)
**Primary identifier:** MONDO:0016674

---

## Scope note and evidence-quality caveat (read first)

46,XY PGD sits on a **continuum** with 46,XY complete gonadal dysgenesis (CGD/Swyer syndrome) and 46,XY testicular regression syndrome (TRS), and is adjacent to — but karyotypically distinct from — **mixed gonadal dysgenesis (MGD)**, which requires 45,X/46,XY (or variant) mosaicism. Much of the published literature pools these entities under "46,XY gonadal dysgenesis" or "46,XY DSD." **Throughout this report I mark whether a figure is PGD-specific or derived from a pooled cohort**, because conflating them is the single largest source of error in curating this entry.

A second caution relevant to this KB: 46,XY PGD is a **high-NEC-risk (named-entity-confusion) disease class** — it belongs to a numbered OMIM series (SRXY1–SRXY12+), shares eponyms and synonyms with CGD/Swyer, and has near-neighbours (MGD, TRS, ovotesticular DSD, partial androgen insensitivity) that generate coherent-but-wrong literature. Any deep-research output for this disease should be preflighted against the MONDO/OMIM gene anchors given in §4.

---

## 1. Disease Information

### 1.1 Definition

**Orphanet/MONDO definition (verbatim, the source of the MONDO `def:`):**

> "46,XY partial gonadal dysgenesis (46,XY PGD) is a disorder of sex development (DSD) associated with anomalies in gonadal development that results in genital ambiguity of variable degree ranging from almost female phenotype to almost male phenotype in a patient carrying a male 46,XY karyotype."
> — Orphanet:251510 (source of MONDO:0016674 definition)

**Operational clinical definition.** 46,XY PGD is defined by *incomplete* (rather than absent) testis determination in a person with a non-mosaic 46,XY karyotype and no syndromic features. Gonads are **bilaterally dysgenetic testes**, or a **dysgenetic testis on one side with a streak gonad on the other**, and produce enough fetal testosterone and anti-Müllerian hormone (AMH) to partially virilize the external genitalia and partially regress the Müllerian ducts — hence the hallmark combination of **ambiguous genitalia plus variably retained Müllerian structures**.

GeneReviews frames the diagnostic boundary as: *"normal general physical examination AND absence of clinical findings involving other organ systems"* — i.e., 46,XY PGD in the strict sense is a **nonsyndromic** disorder of testicular development. Syndromic gonadal dysgenesis (WT1-related Denys–Drash/Frasier, campomelic dysplasia/SOX9, 9p deletion, ATRX, DHH with minifascicular neuropathy) are curated as distinct entities, though they overlap mechanistically. (GeneReviews, *Nonsyndromic Disorders of Testicular Development Overview*, NCBI Bookshelf NBK1547)

The distinction from CGD is **quantitative, not qualitative**: PGD retains partial testis-determining function, CGD retains essentially none. The 2025 I-DSD registry study makes this explicit — *"46,XY gonadal dysgenesis is classified as complete (CGD) or partial (PGD) subtypes. The phenotype of PGD and the long-term outcome is not clearly defined."* (Tadokoro-Cuccaro et al., *J Clin Endocrinol Metab* 2025; **PMID:40208111**)

### 1.2 Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0016674` | `is_a` MONDO:0020040 (46,XY disorder of sex development) |
| **Orphanet** | `ORPHA:251510` | Definition source; subset `ordo_malformation_syndrome`, `ordo_disorder` |
| **UMLS** | `C4510744` | |
| **MedGen** | `1388250` | |
| **SNOMED CT** | `725045004` | |
| **GARD** | `GARD:0017211` | rarediseases.info.nih.gov/diseases/17211 |
| **MeSH** | `D023961` (Gonadal Dysgenesis, 46,XY) | Nearest MeSH; **no PGD-specific descriptor** |
| **ICD-10** | `Q56.3` (Pseudohermaphroditism, unspecified) / `Q99.1` (46,XX true hermaphrodite… — not applicable); most registries use **Q56.3** or **Q99.8** | ICD-10 has **no specific PGD code**; Orphanet maps the DSD group loosely |
| **ICD-11** | `LD2A.Y` / `LD2A.0` — "Sex chromosome structure variations… / 46,XY disorders of sex development" | ICD-11 foundation covers "46,XY DSD"; **no PGD-specific stem code** |
| **OMIM** | **No single OMIM number.** Gene-specific SRXY series applies — see §4.1 | This is important: OMIM models PGD *by gene*, not as one entity |

**MONDO structural note (verified locally via OAK):**
```
[Term]
id: MONDO:0016674
name: 46,XY partial gonadal dysgenesis
def: "46,XY partial gonadal dysgenesis (46,XY PGD) is a disorder of sex development (DSD)
      associated with anomalies in gonadal development that results in genital ambiguity of
      variable degree ranging from almost female phenotype to almost male phenotype in a
      patient carrying a male 46,XY karyotype." [Orphanet:251510]
synonym: "46,XY PGD" EXACT
synonym: "46,XY partial testicular dysgenesis" EXACT
is_a: MONDO:0020040 ! 46,XY disorder of sex development
```

### 1.3 Synonyms and alternative names

**Current/preferred:** 46,XY partial gonadal dysgenesis; 46,XY PGD; 46,XY partial testicular dysgenesis; partial testicular dysgenesis; partial XY gonadal dysgenesis.

**Historical/deprecated (do NOT use as preferred terms — explicitly retired by the 2006 Chicago Consensus):** male pseudohermaphroditism; partial XY sex reversal; dysgenetic male pseudohermaphroditism; intersex. The Chicago Consensus (Hughes IA, Houk C, Ahmed SF, Lee PA; LWPES/ESPE Consensus Groups. *Arch Dis Child* 2006;91(7):554-63; **PMID:16624884**) replaced *"intersex, pseudohermaphroditism, hermaphroditism, sex reversal, and gender-based diagnostic labels"* with the DSD nomenclature. Note HPO still carries the legacy term **HP:0000037 "Male pseudohermaphroditism"** — flag it, don't use it.

**Terminology sensitivity.** Many affected adults and advocacy organisations prefer "**differences** of sex development" or "**variations** of sex characteristics" over "disorders." Curated `description` and `notes` text should use neutral phrasing; the D/DSD abbreviation is broadly accepted.

### 1.4 Data provenance character

Information for this entity is **overwhelmingly aggregated disease-level and case-series derived**, not EHR/individual-patient derived:

- **Registry-derived (highest quality):** the **I-DSD Registry** (international, 34 centres) supplied the only large PGD-specific outcome cohort (n=310 across CGD/PGDf/PGDm; PMID:40208111).
- **National population registry:** Danish nationwide cytogenetic/health registry linkage gives the only true population-based prevalence (PMID:27603905).
- **Single-centre case series:** Brazilian (São Paulo/Campinas), French (Institut Pasteur), UK, Chinese cohorts — the bulk of the genotype literature.
- **Ontology aggregation:** HPO annotations for ORPHA:251510 are curator-derived from Orphanet text, **not** frequency-counted from patients — treat the "Very frequent"/"Frequent" bands as editorial, not empirical (see §3.1 caveat).
- **No claims-based/OMOP phenotype algorithm** exists for 46,XY PGD; ICD coding is too coarse (Q56.3) to support EHR case-finding without chart review or karyotype linkage.

---

## 2. Etiology

### 2.1 Primary causal factors

46,XY PGD is a **monogenic (or oligogenic) developmental disorder of testis determination**. The proximate cause is a germline (occasionally mosaic) variant that reduces — but does not abolish — the output of the testis-determining gene regulatory network during the narrow window of gonadal fate commitment (human ~gestational weeks 6–8; mouse E10.5–E12.5).

The unifying model, stated by the definitive genetics review:

> "In 46,XY men, testis is determined by a genetic network(s) that both promotes testis formation and represses ovarian development. Disruption of this process results in a lack of testis-determination and affected individuals present with 46,XY gonadal dysgenesis (GD), a part of the spectrum of Disorders/Differences of Sex Development/Determination (DSD). A minority of all cases of GD are associated with pathogenic variants in key players of testis-determination, SRY, SOX9, MAP3K1 and NR5A1. However, most of the cases remain unexplained."
> — Elzaiat M, McElreavey K, Bashamboo A. *Genetics of 46,XY gonadal dysgenesis.* Best Pract Res Clin Endocrinol Metab 2022;36(1):101633. **PMID:35249806**

Key etiological points:

1. **Dosage/threshold biology, not simple loss of function.** Testis determination is a bistable switch with a steep dose–response. PGD arises when the pro-testis signal falls into an intermediate band — enough to build some seminiferous tubules and Leydig cells, not enough to build a normal testis. This is why the *same variant* can produce CGD in one family member and PGD (or even isolated hypospadias/infertility) in another.
2. **Both loss-of-function of pro-testis genes and gain-of-function of pro-ovary signalling** cause the same phenotype. MAP3K1 is the canonical gain-of-function example (§6.2).
3. **A large diagnostic gap remains.** Approximately **50–60% of 46,XY GD cases are genetically unexplained** even after exome sequencing (PMID:35249806; Frontiers in Genetics 2024, DOI:10.3389/fgene.2024.1387598). In the largest PGD-specific cohort, *"A genetic cause was identified in 42% overall"* (PMID:40208111).
4. **Karyotype must be non-mosaic 46,XY.** Hidden low-level 45,X/46,XY mosaicism (peripheral blood may be negative while gonadal tissue is mosaic) is a recognised misclassification route into this entity.

### 2.2 Genetic risk/causal factors

**Causal (high-penetrance) loci** — see §4 for full detail. Summary of PGD-relevant genes and approximate contribution (GeneReviews NBK1547; PMID:35249806):

| Gene | Locus | Share of nonsyndromic 46,XY testicular DSD | Inheritance | Direction of effect |
|---|---|---|---|---|
| **NR5A1** (SF-1) | 9q33.3 | 10–15% (up to 42% of PGDf in I-DSD) | Sex-limited AD (also de novo; rare AR) | LoF / haploinsufficiency |
| **MAP3K1** | 5q11.2 | 10–18% (≥4% of PGD+CGD) | Sex-limited AD, near-complete penetrance in 46,XY | **Gain of function** |
| **DHX37** | 12q24.31 | ~10–20% (enriched in TRS/PGD) | Sex-limited AD | Missense, domain-clustered; likely hypomorph |
| **SRY** | Yp11.2 | 10–15% (predominantly CGD; PGD when mosaic/partial-function) | Y-linked, usually de novo | LoF |
| **DHH** | 12q13.12 | Rare | **AR** (sex-limited) | LoF |
| **DMRT1** / 9p24 del | 9p24.3 | Rare | AD / contiguous deletion | Haploinsufficiency |
| **SOX9 / SOX8** | 17q24.3 / 16p13.3 | Rare (incl. enhancer/RevSex CNVs) | AD | LoF or regulatory |
| **NR0B1 (DAX1)** dup | Xp21.2 | Rare | X-linked dosage | **Duplication** (anti-testis) |
| **WT1** | 11p13 | Rare in *nonsyndromic* PGD | AD | LoF / KTS-isoform imbalance |
| **ZFPM2 (FOG2), GATA4** | 8q23.1 / 8p23.1 | Rare | AD | LoF |
| **WNT4 / RSPO1** dup | 1p36 | Very rare | Dosage | Pro-ovary gain |
| **PPP2R3C, PBX1, HHAT, LHX9, SOS1, MYRF, PPP1R12A, WWOX, TSPYL1, CBX2, ESR2, SART3, AKR1C2/4, ARX, ATRX, MAMLD1** | various | Individually rare; collectively meaningful | mixed | mixed |

*(Gene list compiled from GeneReviews NBK1547; Idris et al., Andrology 2025, **PMID:39081229**; PMID:35249806)*

**Y-chromosome microdeletions are NOT a cause of non-mosaic 46,XY PGD.** This is a useful negative result: in a Brazilian series of 13 PGD patients, *"All STS showed positive amplifications in the PGD group"* — no AZF deletions — whereas 6/15 (40%) of the 45,X/46,XY MGD group carried Yq microdeletions (PMC3827999). Curate this as a **REFUTE/negative** evidence item distinguishing PGD from MGD.

**Modifier genes and oligogenicity.** A clear genotype–phenotype correlation is absent for NR5A1, which has led to the hypothesis that *"genetic modifiers, such as pathogenic variants in other testis/ovarian-determining genes, may contribute to the phenotypic expression."* Direct evidence exists: in a 25-patient 46,XY DSD cohort, **two patients carried pathogenic variants in both DHX37 and NR5A1**, with *"the most severe phenotype occurring in the digenic case"* — DHX37 p.(Leu467Val) + NR5A1 frameshift, and DHX37 p.(Val999Met) + de novo NR5A1 nonsense (PMC10222664, *DHX37 and NR5A1 Variants Identified in Patients with 46,XY Partial Gonadal Dysgenesis*).

> **Curation flag for this KB:** This is a genuine **digenic inheritance** finding. Per the CLAUDE.md digenic/oligogenic SOP, it warrants an `Inheritance` block bound to **HP:0010984 (Digenic inheritance)** with the DHX37+NR5A1 double-heterozygote citation as its own evidence item, and `relationship_type: COOPERATING`/`MODIFIER` on the second locus in the `genetic:` section.

### 2.3 Environmental risk factors

**For 46,XY PGD specifically: essentially none established.** This is a genetically determined developmental disorder; no environmental exposure has been shown to cause bona fide 46,XY partial gonadal dysgenesis with dysgenetic/streak gonads.

**Adjacent but distinct — the testicular dysgenesis syndrome (TDS) hypothesis.** Skakkebæk and colleagues proposed that *cryptorchidism, hypospadias, impaired spermatogenesis and testicular cancer* share a common origin in disturbed prenatal testicular development, possibly driven by endocrine-disrupting chemicals (EDCs) — anti-androgenic phthalates in particular (Skakkebaek et al., *Best Pract Res Clin Endocrinol Metab* 2006; **PMID:16522521**; see also **PMID:29183799**, "Is testicular dysgenesis syndrome a genetic, endocrine, or environmental disease…?"). Mechanistically, EDCs *"may interfere with the control of testicular descent, which is regulated by two Leydig cell hormones, testosterone, and insulin like peptide 3 (INSL3),"* and in utero phthalate exposure in rats suppresses fetal-testis steroidogenic gene expression, inducing multinucleated germ cells, hypospadias and cryptorchidism.

**How to curate this:** TDS is a **mechanistically convergent but etiologically separate** entity. It shares the downstream node "fetal Leydig cell dysfunction → androgen insufficiency → undervirilization" with PGD, but the trigger is exogenous and the gonad is not dysgenetic in the PGD sense. Record it as a **discussion/`KNOWLEDGE_GAP` or a mechanistic note**, not as a risk factor for MONDO:0016674. Most TDS evidence is `MODEL_ORGANISM` (rat) or ecological-epidemiological; human fetal testis xenografts were notably **resistant** to phthalate-induced endocrine disruption (PMC3440087) — a genuine human/model mismatch worth recording as `HUMAN_MODEL_MISMATCH`.

**Other environmental factors:** no established role for maternal age, parity, radiation, infection, diet, smoking, or alcohol in 46,XY PGD. **Advanced paternal age** is a plausible but unquantified contributor to the de novo missense burden (MAP3K1, DHX37, NR5A1) — no PGD-specific study exists. GARD's generic statement that *"Environmental factors and viruses may also contribute"* is boilerplate text and should **not** be curated as evidence.

### 2.4 Protective factors

**No genetic or environmental protective factors are established for 46,XY PGD.** Two observations that superficially resemble protection but are not:

1. **46,XX carriers of MAP3K1 and MAP3K1/DHX37 variants are unaffected.** *"46,XX carriers appear to have normal fertility and no developmental abnormalities."* (Ostrer H. *Sex Dev* 2022; **PMID:35290982**) This is **sex-limited expression**, not protection — the same allele is fully penetrant in a 46,XY background.
2. **DHH heterozygotes are asymptomatic** (autosomal recessive; GeneReviews NBK1547) — standard recessive carrier status.

**gnomAD-based inference:** because the causal variants are individually ultra-rare and largely de novo or sex-limited, gnomAD constraint metrics (pLI, missense z) support intolerance rather than identifying protective alleles. No protective haplotype has been reported.

### 2.5 Gene–environment interaction

**No validated GxE interaction for 46,XY PGD.** The plausible-but-unproven hypothesis is that sub-threshold germline variants in testis-determining genes (a "genetic first hit" producing borderline SOX9/SF-1 output) may be **unmasked by in-utero anti-androgenic exposure**, pushing the bistable switch across threshold. This is a specific, testable, currently-unsupported claim — appropriate for a `discussions` entry with `kind: KNOWLEDGE_GAP` and `proposed_experiments` (e.g., exposure-stratified genotype analysis in a hypospadias/DSD registry; human fetal-testis organoid dose–response on a sensitized NR5A1<sup>+/−</sup> background).

---

## 3. Phenotypes

### 3.1 HPO annotation set (ORPHA:251510, retrieved from JAX HPO API; all IDs and labels **verified against `sqlite:obo:hp` via OAK**)

> **Frequency caveat — important for this KB.** These frequency bands are Orphanet **curator-assigned editorial bands**, not counts from a genotyped cohort. Per `docs/frequency-evidence-guidelines.md`, most of these should be curated **without** a `frequency:` value unless a quantitative source is cited. Where a real cohort number exists (I-DSD 2025), I give it separately in §3.2 and that is what should carry the frequency band. The annotation set also clearly **pools syndromic causes** (nephroblastoma/nephrotic syndrome → WT1; adrenal insufficiency → NR5A1), so the tail annotations describe the *gene-defined subgroups*, not the core entity.

**Genital / genitourinary — core phenotype**

| HPO ID | Label | Orphanet band | Comment |
|---|---|---|---|
| HP:0000062 | Ambiguous genitalia | Very frequent | **Cardinal sign** |
| HP:0000133 | Gonadal dysgenesis | Very frequent | **Cardinal sign** |
| HP:0012244 | Abnormal sex determination | Very frequent | Mechanistic-level term |
| HP:0000047 | Hypospadias | Very frequent | Penoscrotal/perineal at severe end |
| HP:0000054 | Micropenis | Very frequent | |
| HP:0008736 | Hypoplasia of penis | Very frequent | |
| HP:0008734 | Decreased testicular size | Very frequent | |
| HP:0000812 | Abnormal internal genitalia | Very frequent | Müllerian remnants ± Wolffian hypoplasia |
| HP:0008665 | Clitoral hypertrophy | Very frequent | Female-assigned presentation |
| HP:0000058 | Abnormal labia morphology | Very frequent | Labioscrotal fusion |
| HP:0000045 | Abnormal scrotum morphology | Very frequent | Bifid scrotum |
| HP:0100779 | Urogenital sinus anomaly | Very frequent | |
| HP:0000142 | Abnormal vagina morphology | Very frequent | |
| HP:0008726 | Hypoplasia of the vagina | Very frequent | |
| HP:0008730 | Female external genitalia in individual with 46,XY karyotype | Very frequent | The near-female end of the spectrum |
| HP:0010464 | Streak ovary | Very frequent | Streak gonad (asymmetric in PGD) |
| HP:0012870 | Vanishing testis | Very frequent | TRS overlap |
| HP:0000028 | Cryptorchidism | Frequent | |
| HP:0000027 | Azoospermia | Very frequent | |
| HP:0003251 | Male infertility | Very frequent | |
| HP:0000868 | Decreased fertility in females | Very frequent | |
| HP:0000786 | Primary amenorrhea | Very frequent | Female-assigned, later presentation |

**Endocrine / laboratory**

| HPO ID | Label | Band |
|---|---|---|
| HP:0000815 | Hypergonadotropic hypogonadism | Very frequent |
| HP:0000837 | Increased circulating gonadotropin level | Very frequent |
| HP:0008232 | Elevated circulating follicle stimulating hormone level | Very frequent |
| HP:0011969 | Elevated circulating luteinizing hormone level | Very frequent |
| HP:0040171 | Decreased serum testosterone concentration | Very frequent |
| HP:0008214 | Decreased serum estradiol | Very frequent |
| HP:0008193 | Primary gonadal insufficiency | Occasional |
| HP:0000823 | Delayed puberty | Frequent |
| HP:0008187 | Absence of secondary sex characteristics | Occasional |
| HP:0000846 | Adrenal insufficiency | Occasional | ← **NR5A1 subgroup** |

Two additional lab terms not in the Orphanet set but clinically central, verified in HPO and worth curating:
- **HP:0031103** — Decreased circulating antimullerian hormone circulation *(sic — that is the canonical HPO label; do not "correct" it)*
- **HP:0031100** — Decreased circulating inhibin B concentration

**Neoplasia**

| HPO ID | Label | Band |
|---|---|---|
| HP:0000150 | Gonadoblastoma | Frequent |
| HP:0000030 | Testicular gonadoblastoma | Occasional |
| HP:0000149 | Ovarian gonadoblastoma | Occasional |
| HP:0002667 | Nephroblastoma | Very rare | ← **WT1 subgroup** |

**Other / secondary**

| HPO ID | Label | Band | Comment |
|---|---|---|---|
| HP:0000771 | Gynecomastia | Very frequent | |
| HP:0000939 | Osteoporosis | Very frequent | Secondary to untreated hypogonadism — **downstream complication, not primary** |
| HP:0002225 | Sparse pubic hair | Very frequent | |
| HP:0002215 | Sparse axillary hair | Very frequent | |
| HP:0002750 | Delayed skeletal maturation | Occasional | |
| HP:0000100 | Nephrotic syndrome | Very rare | ← **WT1 subgroup (Denys–Drash/Frasier)** |
| HP:0030680 | Abnormal cardiovascular system morphology | Very rare | Likely contiguous-deletion cases |

### 3.2 PGD-specific quantitative phenotype data — I-DSD Registry 2025 (the best available)

Tadokoro-Cuccaro R, et al. *Phenotypic Variation and Pubertal Outcomes in Males and Females With 46,XY Partial Gonadal Dysgenesis.* J Clin Endocrinol Metab 2025. **PMID:40208111**; DOI:10.1210/clinem/dgaf223. 310 patients, 34 international centres: CGD n=100, PGD assigned female (PGDf) n=107, PGD assigned male (PGDm) n=103.

**These are the numbers that should carry `frequency:` values in the KB.**

| Measure | PGDf | PGDm | CGD |
|---|---|---|---|
| External genital score (median) | 4.0 | 7.0 | — |
| Uterus present | 51% | 31.3% | — |
| Presented with atypical genitalia in infancy | 62.1% | ~100% | — |
| Presented with **delayed puberty** | 17.9% (abstract: "18%") | — | — |
| Presented with **virilization** | 8% | — | — |
| Genetic cause identified | 42.3% overall cohort | | |
| NR5A1 the most frequent gene | 42.2% of solved PGDf | 25.6% of solved PGDm | |
| Low AMH | 48% | 58.1% | |
| Testosterone ≥2× after hCG stimulation | — | 66.0% (31/47) | |
| **Spontaneous puberty onset** (≥13 y, gonads in situ) | — | **80.0% (36/45)** | |
| **Reached Tanner G5 without hormone treatment** | — | **59.3% (16/27)** | |
| **Spontaneous virilization at puberty** (clitoromegaly/hirsutism) | **42.3% (11/26)** | — | |
| **Gonadal pre-/malignancy** | **19.7%** | **8.8%** | **33.8%** |
| Sex reassignment after initial assignment | **16.1% (15/93)** to male | **5.3% (5/94)** to female | |

Direct quotation from the abstract: *"18% of PGDf presented with delayed puberty and 8% with virilization."*

**Second PGD-specific longitudinal series** — Long-term follow-up of 10 patients with 46,XY PGD reared as males, 13.5–19.7 years follow-up (*Int J Endocrinol* 2014; **PMID:25580123**):
- *"All had spontaneous puberty; only one needed androgen therapy"*; 9/10 reached Tanner ≥4.
- *"There was no case of testicular neoplasia"* (small n; does not contradict the 8.8% figure above).
- All three semen analyses: **severe oligozoospermia**.
- Final height −1.57 to +0.80 SDS (9 patients) — **growth is not primarily affected**.
- 30% had learning disabilities (mild ×2, moderate ×1); 50% had other conditions (VUR, hypothyroidism, hearing loss, psychiatric). **Interpret cautiously** — n=10, single centre, ascertainment-biased; this is *not* evidence that 46,XY PGD is a neurodevelopmental disorder.

### 3.3 Phenotype characteristics

**Age of onset.** Congenital / **neonatal** for the great majority. HPO onset: `HP:0003577` Congenital onset / `HP:0003623` Neonatal onset. The I-DSD data show a bimodal ascertainment: ~100% of PGDm and 62% of PGDf detected in infancy via atypical genitalia; a minority of PGDf present at **adolescence** with delayed puberty (18%) or virilization (8%). The Danish national data give **median age at diagnosis of 17.0 years for gonadal dysgenesis presenting as phenotypic female** (vs 7.5 y for AIS) — a striking diagnostic delay (PMID:27603905).

**Severity.** **Variable by definition** — the entity is defined by its spectrum (external genital score 0–12; median 4.0 female-assigned, 7.0 male-assigned). Use `severity: variable` phrasing rather than an enum band at the disease level.

**Progression.** The *gonadal lesion* is **non-progressive in its determination defect** (a fixed developmental event) but the **gonadal function declines progressively** — and there is a distinct **progressive neoplastic risk** with age. Curate two separate progression claims:
- Endocrine: `clinical_course: PROGRESSIVE` on gonadal insufficiency (rising FSH/LH, falling testosterone/inhibin B/AMH across childhood into adulthood).
- Oncological: cumulative, age-dependent germ cell neoplasia risk (§11.3).
- **Countervailing:** the retained dysgenetic testis in PGDm often functions well enough for **spontaneous puberty (80%)**, so "progressive gonadal failure" must not be over-stated for the male-assigned end of the spectrum.

**Frequency among affected individuals.** See §3.2. For the core signs (ambiguous genitalia, gonadal dysgenesis) treat as obligate/near-obligate; for everything else use the I-DSD numbers or omit.

### 3.4 Quality-of-life impact (per phenotype where possible)

**No disease-specific validated QoL instrument exists for 46,XY PGD.** The main data source is the European **dsd-LIFE** cross-sectional study (n=1,040 DSD patients, includes SF-36/WHOQOL and sexual-function measures; the same cohort as PMID:32905884). Per-phenotype impacts, ordered by weight of evidence:

| Phenotype | QoL domain affected | Note |
|---|---|---|
| Atypical genitalia + genital surgery | Sexual function, body image, genital sensation | The most consequential and most contested domain; adult dissatisfaction with early surgery is well documented |
| Gender assignment uncertainty / reassignment (16.1% PGDf, 5.3% PGDm) | Psychological, identity, family | The single most distinctive QoL burden of PGD vs CGD |
| Infertility / severe oligozoospermia | Family planning, partnership, psychological | Near-universal |
| Unanticipated pubertal virilization in female-assigned (42.3%) | Acute distress, body image, need for urgent intervention | PGD-specific; does not occur in CGD |
| Cancer risk surveillance / gonadectomy decision | Anxiety, iatrogenic hypogonadism if gonads removed | See §11.3 |
| Lifelong hormone replacement | Adherence, bone health, metabolic | |
| Diagnostic delay (median 17 y in female-presenting GD) | Trust in care, missed intervention windows | PMID:27603905 |
| Osteoporosis (HP:0000939) | Fracture risk, mobility | Secondary/preventable |

The 2016 Global DSD Update is explicit that *"the goal of patient care is focused upon the best possible quality of life (QoL)"* and that *"it is still impossible to predict gender development in an individual case with certainty."* (Lee PA, Nordenström A, Houk CP, Ahmed SF, Auchus R, et al. *Horm Res Paediatr* 2016; **PMID:26820577**)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes with OMIM allelic-series mapping

**Critical for NEC preflight — the OMIM identity anchors:**

| Gene | HGNC | Locus | Gene OMIM | Phenotype OMIM | Phenotype name |
|---|---|---|---|---|---|
| **SRY** | hgnc:11311 | Yp11.2 | 480000 | **400044** | 46,XY SEX REVERSAL 1 (SRXY1) |
| **NR5A1** | hgnc:7983 | 9q33.3 | 184757 | **612965** | 46,XY SEX REVERSAL 3 (SRXY3) |
| **MAP3K1** | hgnc:6848 | 5q11.2 | 600982 | **613762** | 46,XY SEX REVERSAL 6 (SRXY6) |
| **DHH** | hgnc:2865 | 12q13.12 | 605423 | **233420** | 46,XY SEX REVERSAL 7 (SRXY7) — AR |
| **DHH** | hgnc:2865 | 12q13.12 | 605423 | **607080** | 46,XY GONADAL DYSGENESIS WITH MINIFASCICULAR NEUROPATHY (GDMN) |
| **DHX37** | hgnc:17210 | 12q24.31 | 617362 | **273250** | 46,XY SEX REVERSAL 11 (SRXY11) |
| **SOX9** | hgnc:11204 | 17q24.3 | 608160 | 114290 / 278850 | Campomelic dysplasia w/ sex reversal; RevSex |
| **WT1** | hgnc:12796 | 11p13 | 607102 | 194080 / 136680 | Denys–Drash; Frasier |
| **DMRT1** | hgnc:2934 | 9p24.3 | 602424 | 154230 (9p del) | |
| **NR0B1** (DAX1) | hgnc:7960 | Xp21.2 | 300473 | 300018 | 46,XY sex reversal, dosage-sensitive (duplication) |
| **ZFPM2** (FOG2) | hgnc:16700 | 8q23.1 | 603693 | 616067 | SRXY9 |
| **GATA4** | hgnc:4173 | 8p23.1 | 600576 | — | |
| **SOX8** | hgnc:11203 | 16p13.3 | 605923 | — | |
| **PPP2R3C** | hgnc:9306 | 14q13.2 | 615902 | 618419 | Myopathy + 46,XY GD (MEGD) |
| **HHAT** | hgnc:18021 | 1q32.2 | 605743 | 614270 | Nivelon–Nivelon–Mabille (46,XY GD + skeletal) |

*(Compiled from OMIM entries 400044, 612965, 613762, 233420, 607080, 273250, 605423; GeneReviews NBK1547)*

**Note the OMIM modelling choice:** OMIM does **not** have a "46,XY partial gonadal dysgenesis" entry. It distributes PGD across the SRXY allelic series by gene, with each SRXY entry spanning CGD↔PGD↔TRS. MONDO:0016674, in contrast, is a *phenotype-level* grouping. **This mismatch is the main NEC hazard for this entity** — a deep-research tool asked for "46,XY partial gonadal dysgenesis" may return a report anchored on SRXY1 (SRY/Swyer, i.e., *complete* GD) or on MGD. Preflight by checking that the report's dominant gene is one of NR5A1/MAP3K1/DHX37 and that the described gonads are *dysgenetic testes ± one streak*, not *bilateral streaks*.

### 4.2 NR5A1 (SF-1) — the most frequent single cause

**Function.** NR5A1 encodes steroidogenic factor 1 (SF-1/Ad4BP), an orphan nuclear receptor and master transcriptional regulator of the hypothalamic–pituitary–gonadal–adrenal axis. It directly regulates *SOX9* (via the TESCO/Enh13 enhancers), *AMH*, *CYP17A1*, *STAR*, *INSL3*, *LHB*, and *CYP11A1*.

**Frequency.** *"NR5A1 mutations have been detected in about 10–20% of 46,XY DSD cases as major causes of gonadal dysgenesis in males."* Approximately **8–15%** across pooled 46,XY DSD cohorts; **5/27 (18.5%)** in a German 46,XY DSD cohort (Köhler et al.); **6.70%–22.22%** across 14 international cohorts 2013–2023 (DOI:10.3389/fgene.2024.1387598). **In the PGD-specific I-DSD cohort, NR5A1 was the single most frequent gene: 42.2% of genetically-solved PGDf and 25.6% of solved PGDm** (PMID:40208111).

**Variant classes.** Missense (DNA-binding zinc fingers, ligand-binding domain, Ftz-F1 box), frameshift, nonsense, splice-site, whole-gene deletion. Predominantly **heterozygous** with **haploinsufficiency/dominant-negative** effect; rare biallelic cases cause severe adrenal + gonadal failure.

**Recurrent variant of special note:** **p.Arg92Trp (R92W)** — causes 46,**XX** testicular/ovotesticular DSD in humans (a gain-of-pro-testis effect in the XX background), demonstrating the exquisite dosage sensitivity of SF-1. Critically, this is a **documented human/mouse mismatch**: *"The p.R92W variant of NR5A1/Nr5a1 induces testicular development of 46,XX gonads in humans, but not in mice"* (PMC5101639) — curate as `HUMAN_MODEL_MISMATCH`.

**Phenotypic spectrum (extremely wide — the defining feature of NR5A1).** GeneReviews: NR5A1 variants are *"associated with a wide range of phenotypes including isolated 46,XY partial and complete gonadal dysgenesis, 46,XY undervirilization, vanishing testes, and male infertility."* In 46,XX carriers: **primary ovarian insufficiency**. Adrenal insufficiency is present in only a **minority** — the classic teaching that SF-1 defects always cause adrenal failure is wrong. *"Heterozygous mutations in SF1 may be found in patients with 46,XY partial gonadal dysgenesis and underandrogenization but normal adrenal function."*

**Genotype–phenotype:** *"A clear genotype-phenotype correlation is not seen in patients bearing NR5A1 mutations, suggesting that genetic modifiers... may contribute to the phenotypic expression."* Intrafamilial variability is marked — the same variant may produce CGD in the proband and only infertility in the father.

**Illustrative case (NR5A1-related PGD, PMID:38206718 / PMC10754607):** 12-year-old raised female presenting with hirsutism, deep voice, clitoromegaly (1.5 × 1.0 cm), Tanner II breast, no menarche; FSH 53.31 mIU/mL (ref 1.78–11.60), testosterone 2.58 ng/mL (ref 0–1.23); dysplastic testes in bilateral groin, absent uterus and ovaries. Bilateral orchiectomy + feminizing hormone therapy → regression of hirsutism and clitoromegaly. **This case is a perfect illustration of the 42.3% pubertal-virilization phenomenon in PGDf.**

**Allele frequency.** Pathogenic NR5A1 variants are absent or singleton in gnomAD. NR5A1 is missense- and LoF-constrained. Many reported variants are **de novo**; inherited variants typically come from a mildly affected or unaffected parent (sex-limited/incomplete penetrance).

### 4.3 MAP3K1 — the canonical gain-of-function cause

**The definitive mechanistic statement (Ostrer H. *Sex Dev* 2022;16(2-3):137-142; PMID:35290982), verbatim:**

> "Pathogenic variants in the MAP3K1 gene are an important cause of 46,XY non-syndromic partial and complete gonadal dysgenesis, accounting for at least 4% of cases. Inheritance occurs in a sex-limited, autosomal dominant fashion with virtually complete penetrance in 46,XY individuals. 46,XX carriers appear to have normal fertility and no developmental abnormalities. Pathogenic variants occur almost exclusively within known domains of the MAP3K1 protein, facilitating annotation when identified. Where studied, these variants have been modeled to alter the local MAP3K1 folding and surface domains and have been shown to alter interactions with known binding partners. The net effect of these variants is to increase phosphorylation of downstream targets ERK1, ERK2, and p38, resulting in multiple gain-of-function effects interfering with testis determination and enabling ovarian determination."

**Discovery (Pearlman A, Loke J, Le Caignec C, et al. *Am J Hum Genet* 2010;87(6):898-904; PMID:21129722):**
> "Here, the locus for an autosomal sex-determining gene was mapped via linkage analysis in two families with 46,XY DSD to the long arm of chromosome 5 with a combined, multipoint parametric LOD score of 6.21."

The same paper showed the mutations alter phosphorylation of downstream signalling molecules, **enhance binding to RHOA**, and that mouse *Map3k1* is expressed in the embryonic gonad during the sex-determination window.

**Clinical series (Granados A, Alaniz VI, Mohnach L, et al. *Am J Med Genet C* 2017;175(2):253-259; PMID:28504475), verbatim abstract excerpt:**
> "MAP3K1 encodes a signal transduction regulator in the sex determination pathway and is emerging as one of the more common genes responsible for 46,XY DSD presenting as complete or partial gonadal dysgenesis. Clinical assessment, endocrine evaluation, and genetic analysis were performed in six individuals from four unrelated families with 46,XY DSD. All six individuals were found to have likely pathogenic MAP3K1 variants. Three of these individuals presented with complete gonadal dysgenesis, characterized by bilateral streak gonads with typical internal and external female genitalia, while the other three presented with **partial gonadal dysgenesis, characterized by incomplete testicular development, resulting in clitoral hypertrophy with otherwise typical female external genitalia**. Testing for MAP3K1 variants should be considered in patients with 46,XY complete or partial gonadal dysgenesis, particularly in families with multiple members affected with 46,XY DSD. Identification of a MAP3K1 variant should prompt an evaluation for DSD in female siblings of the proband."

**Detailed functional dissection of one variant — p.R186G (PMC8927045, *MAP3K1 Variant Causes Hyperactivation of Wnt4/β-Catenin/FOXL2 Signaling…*):**
- Variant c.556A>G / p.R186G in two affected siblings.
- *"significantly decreased affinity to ubiquitin (43–49%) and increased affinity to RhoA, which was 3.19 ± 0.18 fold"* vs wild type → reduced degradation → **increased MAP3K1 protein stability**.
- *"led to hyperphosphorylation of p38 and GSK3β, and promoted hyperactivation of the Wnt4/β-catenin signaling"* — phospho-GSK3β is inactive, permitting β-catenin accumulation and nuclear translocation.
- In NT2/D1 testicular cells the variant *"upregulated the expression of genes associated with ovarian development (including WNT4, CTNNB1, and FOXL2) and downregulated the expression of testicular development-related genes (FGFR2 and DMRT1)."*
- Models: NT2/D1 (testicular teratoma), KGN (ovarian granulosa), HEK-293T (reporter). All `IN_VITRO`.

**Variant type/class:** almost exclusively **missense**, clustered in defined MAP3K1 domains (the SWIM/RHOA-binding and kinase-adjacent regions). Frameshift/nonsense variants are conspicuously **not** a cause — consistent with gain-of-function rather than haploinsufficiency. This is a strong, curatable ACMG-relevant statement: *"Pathogenic variants occur almost exclusively within known domains of the MAP3K1 protein, facilitating annotation when identified."*

### 4.4 DHX37 — the newest major gene (and a candidate ribosomopathy)

**Discovery (McElreavey K, Jorgensen A, Eozenou C, et al. *Genet Med* 2020;22(1):150-159; PMID:31337883; PMC6944638):**
> "XY individuals with disorders/differences of sex development (DSD) are characterized by reduced androgenization caused, in some children, by gonadal dysgenesis or testis regression during fetal development. The genetic etiology for most patients with 46,XY gonadal dysgenesis and for all patients with testicular regression syndrome (TRS) is unknown."

Findings: 145 individuals with 46,XY DSD of unknown cause sequenced; **13 children carried heterozygous missense pathogenic variants in DHX37**, an RNA helicase essential for **ribosome biogenesis**. Enrichment of rare/novel DHX37 missense variants vs controls was **P = 5.8 × 10⁻¹⁰**. Five variants were **de novo**; **twelve clustered in two highly conserved functional domains** and were *"specifically associated with gonadal dysgenesis and testicular regression syndrome."* DHX37 expression was confirmed in developing testis **somatic** cells. Conclusion: *"DHX37 pathogenic variants are a new cause of an autosomal dominant form of 46,XY DSD,"* with GD and TRS representing a **clinical spectrum** and potentially a **ribosomopathy**.

**PGD-specific replication (PMC10222664):** in 25 individuals with 46,XY DSD (16 PGD, 6 TRS, 3 CGD), **4/25 (16%)** carried pathogenic DHX37 variants:
- **p.(Arg308Gln)** — the recurrent hotspot, previously reported in 17 individuals
- **p.(Leu467Val)** — novel in DSD
- **p.(Val999Met)** — 2 unrelated patients, in the **OB-fold domain**

Plus the two **digenic DHX37+NR5A1** cases described in §2.2.

**Domain clustering:** variants concentrate in the **RecA2** and **OB-fold** domains (see also PMID:37717579, "Two Novel Heterozygous Variants in RecA2 Domain of DHX37 Cause 46,XY Gonadal Dysgenesis and Testicular Regression Syndrome"). Consistent with hypomorphic/specific-function-altering rather than null alleles.

**Mechanistic hypothesis (EMERGING status):** DHX37 is required for 18S rRNA processing/small-subunit biogenesis. The proposal is that the fetal testis somatic lineage has an unusually high ribosome-biogenesis demand during the narrow determination window, making it selectively vulnerable to partial DHX37 loss — a **tissue-selective ribosomopathy** (see *"DHX37 and 46,XY DSD: A New Ribosomopathy?"*, Sexual Development 2022;16(2-3):194-206). Curate as a `mechanistic_hypotheses` entry with `status: EMERGING`; the alternative (a non-ribosomal moonlighting function of DHX37 in gonadal somatic cells) is not excluded.

### 4.5 SRY

Hemizygous SRY variants *"primarily cause a 46,XY CGD phenotype,"* though **rare mosaicism cases present with milder 46,XY DSD** — i.e., **somatic SRY mosaicism is a recognised route to PGD rather than CGD** (GeneReviews NBK1547). Variants concentrate in the **HMG box** (DNA-binding/bending domain), impairing DNA binding, nuclear import, or DNA bend angle. Mostly **de novo**; paternal transmission is rare and implies gonadal mosaicism or reduced penetrance. 10–15% of nonsyndromic 46,XY testicular DSD overall.

### 4.6 DHH — the autosomal recessive cause with a neurological tell

- **Umehara et al. 2000** (PMID:11017805) reported the first human DHH mutation: a **homozygous missense at the initiation codon (ATG→ACG) in exon 1**, predicting translational failure, in a 27-year-old 46,XY woman with **partial gonadal dysgenesis + polyneuropathy** — female external genitalia with blind vagina and immature uterus, **a testis on one side and a streak gonad on the other** (the textbook PGD gonadal configuration).
- **Werner et al. 2015** (PMID:25927242) found homozygous **p.Arg124Gln (R124Q)** in two Syrian sisters with 46,XY GD and polyneuropathy, via exome sequencing.
- **OMIM 607080** = 46,XY gonadal dysgenesis with minifascicular neuropathy (GDMN); **OMIM 233420** = SRXY7 (gonadal phenotype without overt neuropathy).
- GeneReviews: *"DHH biallelic pathogenic variants cause 46,XY DSD; individuals may develop peripheral neuropathy between ages 20-30 years."*

**Curation implication:** DHH-related PGD carries a **latent, adult-onset neurological phenotype** that is easily missed if the entry is scoped purely to the gonad. This is a legitimate `has_subtypes` candidate, and a rationale for long-term neurological surveillance in DHH-positive patients.

### 4.7 Other loci

- **DMRT1 / 9p24.3 deletion** — haploinsufficiency; monosomy 9p syndrome includes 46,XY GD with intellectual disability and trigonocephaly (syndromic; distinct entity).
- **SOX9** — coding LoF → campomelic dysplasia with sex reversal; **non-coding enhancer CNVs (RevSex/Enh13 region, ~600 kb upstream)** cause **isolated** 46,XY GD. These are invisible to exome sequencing — a specific argument for WGS/CMA (see §10.2).
- **SOX8** — 16p13.3; rare, phenotypically milder; partially redundant with SOX9.
- **NR0B1 (DAX1) duplication, Xp21.2** — dosage-sensitive sex reversal; X-linked, inherited from carrier mother in most cases; 50% transmission risk per pregnancy.
- **WNT4 / RSPO1 duplication (1p36)** — pro-ovary gain of dosage.
- **ZFPM2 (FOG2) and GATA4** — GATA4–FOG2 complex is required for *Sry* upregulation; LoF variants cause 46,XY GD (ZFPM2 = SRXY9) and, for GATA4, often co-segregating congenital heart disease.
- **WT1** — in *nonsyndromic* PGD, rare; the +KTS/−KTS isoform ratio (Frasier, intron 9 splice donor) and missense zinc-finger variants (Denys–Drash) define syndromic entities with **Wilms tumour (HP:0002667)** and **nephrotic syndrome (HP:0000100)** — explaining those two "Very rare" HPO annotations. A reported case combines *"a novel SRY missense mutation combined with a WT1 KTS splice-site mutation"* in a 46,XY female with bilateral gonadoblastoma (PMID:22815844) — another digenic data point.
- **PPP2R3C, PBX1, HHAT, LHX9, SOS1, OTX2, PROP1, MYRF, PPP1R12A** — reported in GD/PGD; evidence strength varies from strong (HHAT, PPP2R3C, PBX1) to provisional. The Elzaiat review explicitly cautions: *"We critically evaluate the evidence to support causality of these factors… we propose several recommendations to help interpret the data and establish causality."* Curate weak-evidence genes with `supports: PARTIAL` and an explicit `explanation` noting limited replication.

### 4.8 Somatic vs germline, mosaicism, and epigenetics

- **Germline is the rule.** Somatic variants are not a described cause; germline **mosaicism** (parental gonadal mosaicism for SRY, NR5A1, MAP3K1) is documented and underlies apparently de novo recurrence in sibships.
- **Somatic mosaicism in the patient** — notably for SRY — is a route to PGD (partial testis determination in a mosaic gonad) and is a reason to consider **gonadal-tissue** rather than blood-only genotyping. Idris et al. recommend transcriptomics/Hi-C/multi-tissue analysis *"to resolve pathogenicity in ambiguous cases and detect mosaicism across multiple tissues"* (PMID:39081229).
- **Epigenetics.** There is **no established primary epigenetic etiology** for 46,XY PGD. The mechanistically relevant epigenetics is *developmental*: the SOX9 TESCO/Enh13 enhancer landscape and CBX2 (Polycomb) — CBX2 LoF causes 46,XY GD, placing chromatin-mediated repression of the ovarian program in the causal chain. `HP:0071514`-type imprinting mechanisms are **not** implicated. This is a genuine gap: no methylome study of dysgenetic gonad tissue in PGD has been published.
- **Chromosomal abnormalities.** By definition the karyotype is **46,XY non-mosaic**. The relevant "chromosomal" lesions are **submicroscopic CNVs**: 9p24 deletion (DMRT1), Xp21.2 duplication (NR0B1), 1p36 duplication (WNT4/RSPO1), 17q24.3 SOX9 enhancer CNVs, 22q, and 10q26 deletions. **CMA is therefore not optional.** Any *detected* 45,X/46,XY mosaicism reclassifies the patient to MGD.

---

## 5. Environmental Information

**Environmental factors:** none established as causal for 46,XY PGD (see §2.3). The EDC/phthalate literature applies to the TDS spectrum (cryptorchidism, hypospadias, subfertility, testicular germ cell cancer), which is mechanistically adjacent but a different entity. Curate any EDC content as `evidence_source: MODEL_ORGANISM` (rat in-utero phthalate) or `OTHER` (ecological epidemiology), never as `HUMAN_CLINICAL` support for MONDO:0016674.

**Lifestyle factors:** none. No smoking/diet/alcohol/exercise association is established. Post-diagnosis, lifestyle matters only for **secondary** outcomes (bone health under hormone replacement — weight-bearing exercise, calcium/vitamin D).

**Infectious agents:** **Not applicable.** No pathogen has any established role in the etiology of 46,XY PGD.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (upstream → downstream)

The pathophysiology is best modelled as a **five-node chain with a bifurcating output**, plus a distinct late-onset neoplastic arm.

```
[MOLECULAR]  Testis-determining network lesion
             (NR5A1 haploinsufficiency | MAP3K1 GoF | DHX37 hypomorph |
              SRY LoF | DHH LoF | SOX9 dosage | NR0B1 dup)
                        ↓
[CELLULAR]   Failure to reach the SOX9 threshold in bipotential
             supporting-cell precursors → incomplete Sertoli cell
             fate commitment; unopposed WNT4/RSPO1/β-catenin/FOXL2
             pro-ovarian signalling in a subset of cells
                        ↓
[TISSUE]     Partial testis differentiation → dysgenetic testis
             (± contralateral streak gonad): reduced seminiferous
             tubule number/size, peritubular fibrosis, germ cell
             depletion, Leydig cell hyperplasia
                        ↓ ↓ (two parallel hormone deficits)
[ORGANISM]  (a) Sertoli cell AMH deficiency → incomplete Müllerian
                duct regression → retained uterus/tubes/upper vagina
            (b) Fetal Leydig cell testosterone + INSL3 deficiency →
                incomplete Wolffian development, incomplete genital
                tubercle/urethral masculinization, cryptorchidism
                        ↓
[ORGANISM]   Ambiguous external genitalia at birth;
             hypergonadotropic hypogonadism; variable pubertal course
                        ↓ (age-dependent, parallel arm)
[TISSUE]     Germ cells arrested in an immature (OCT3/4+) state in a
             dysgenetic niche, with TSPY expression from the Y →
             germ cell neoplasia in situ / gonadoblastoma →
             invasive dysgerminoma/seminoma
```

**Upstream vs downstream assignment for KB curation:**
- *Upstream (MOLECULAR):* the specific gene lesion; SOX9 threshold failure.
- *Midstream (CELLULAR/TISSUE):* Sertoli-cell fate failure; dysgenetic gonad histology.
- *Downstream (ORGANISM):* AMH deficiency → Müllerian retention; androgen deficiency → undervirilization; hypergonadotropic hypogonadism; infertility; osteoporosis.
- *Parallel late arm:* germ cell neoplasia.

### 6.2 Molecular pathways

**The bistable testis-vs-ovary switch.** The gonadal primordium is bipotential; two mutually antagonistic gene-regulatory networks compete, and the outcome is a switch, not a gradient. Reviews synthesising this (Frontiers in Endocrinology 2024, *Unveiling the roles of Sertoli cells lineage differentiation in reproductive development and disorders*, PMC11063913):

**Pro-testis arm (must win):**
- **SRY** (transient, ~E10.5–E12.0 mouse; wk 6–7 human) + **NR5A1** cooperatively bind the **TESCO/Enh13** enhancer of *SOX9* → **SOX9** upregulation.
- SOX9 *"enhances the expression of testicular development-related factors, such as prostaglandin D2 synthase (PTGDS), anti-Müllerian hormone (AMH), WT1, GATA4, and SOX8, while concurrently inhibiting the expression of ovarian determinants, including WNT4, RSPO1, and β-catenin."*
- SOX9 *"can further enhance its own expression by activating the PGD2 and FGF9 signaling pathways, thereby forming a positive feedback loop."* In the XY gonad, *"a positive feedback loop between Sox9 and Fgf9 (as well as PGD2) is established to suppress Wnt4/Rspo1 expression in a paracrine manner, thereby promoting Sertoli cell differentiation."*
- **DHH** is secreted by Sertoli cells and signals via PTCH1/GLI to induce **fetal Leydig cell** differentiation and to organise the peritubular myoid/basal-lamina compartment — hence DHH loss → Leydig deficiency + testicular dysgenesis + (in Schwann cells) minifascicular neuropathy.

**Pro-ovary arm (must be repressed):**
- **RSPO1 → WNT4 → canonical β-catenin (CTNNB1) → FOXL2**. *"Rspo1, Wnt4, and β-catenin inhibit testicular cord formation."* FOXL2 and the RSPO1/WNT4/β-catenin axis *"work in a complementary manner to promote ovarian growth and inhibit testicular development."*

**The MAP3K1 route into this switch — the single best-characterised PGD mechanism:**

MAP3K1 (MEKK1) is a MAP kinase kinase kinase. PGD-causing variants act by **stabilising the protein and rewiring its interactome**, not by abolishing kinase activity:

1. Variant reduces ubiquitin affinity (to 43–49% of WT) → less proteasomal degradation → **MAP3K1 accumulates**.
2. Variant increases **RHOA** binding (3.19-fold) → altered upstream regulation.
3. → **Hyperphosphorylation of ERK1/ERK2, p38, and GSK3β**.
4. Phospho-GSK3β is **inactivated** → the β-catenin destruction complex fails → **β-catenin accumulates and enters the nucleus**.
5. → **WNT4/CTNNB1/FOXL2 upregulated; FGFR2 and DMRT1 downregulated**.
6. Net effect (Ostrer, verbatim): *"multiple gain-of-function effects interfering with testis determination and enabling ovarian determination."*

This is a beautiful, curatable causal chain and a strong candidate for the pathophysiology graph backbone of the MAP3K1 subtype.

**The DHX37 route:** DHX37 is a DEAH-box RNA helicase required for **ribosome biogenesis** (18S rRNA/SSU processome). Expressed in developing testis **somatic** cells. Domain-clustered missense variants (RecA2, OB-fold) are hypothesised to impair ribosome assembly selectively in the high-demand fetal gonadal somatic lineage → insufficient synthesis of the short-lived, dosage-critical determination factors (SRY, SOX9) during the window → partial determination and/or subsequent testicular regression. **Status: EMERGING hypothesis**, explicitly framed as a question in the literature (*"A New Ribosomopathy?"*).

**The NR5A1 route:** SF-1 haploinsufficiency reduces transactivation at *SOX9* enhancers (determination failure) *and* at *STAR/CYP11A1/CYP17A1* (steroidogenic failure) *and* at *AMH* — a single lesion hitting three limbs. This dual determination+steroidogenesis hit explains why NR5A1 PGD can present with both undervirilization and, occasionally, adrenal insufficiency, and why the phenotype is so variable.

### 6.3 Cellular processes

| Process | GO term (verified) | Role |
|---|---|---|
| Sex determination | **GO:0007530** | Top-level |
| Male sex determination | **GO:0030238** | The defective process |
| Male gonad development | **GO:0008584** | |
| Gonad development | **GO:0008406** | |
| Sertoli cell differentiation | **GO:0060008** | The pivotal cell-fate decision |
| Sertoli cell proliferation | **GO:0060011** | |
| Male sex differentiation | **GO:0046661** | Downstream of determination |
| Female gonad development | **GO:0008585** | Aberrantly de-repressed |
| Wnt signaling pathway | **GO:0016055** | Pro-ovarian arm |
| Canonical Wnt signaling pathway | **GO:0060070** | β-catenin arm; `modifier: INCREASED` in MAP3K1 |
| MAPK cascade | **GO:0000165** | `modifier: INCREASED` in MAP3K1 |
| Intracellular signal transduction | **GO:0035556** | |
| Ribosome biogenesis | **GO:0042254** | DHX37 arm; `modifier: DECREASED` |
| Regulation of transcription by RNA polymerase II | **GO:0006357** | NR5A1/SOX9/SRY arm |
| Adrenal gland development | **GO:0030325** | NR5A1 subgroup only |

Additional relevant (not individually verified here, verify before use): hedgehog signaling (DHH arm), apoptotic process (germ cell loss), cell fate commitment.

### 6.4 Protein dysfunction

| Protein | UniProt | Dysfunction class |
|---|---|---|
| SF-1 / NR5A1 | Q13285 | Loss of function / haploinsufficiency; impaired DNA binding (zinc fingers) or coactivator recruitment (LBD/AF-2) |
| MAP3K1 | Q13233 | **Gain of function**: increased stability (reduced ubiquitination), increased RHOA binding, increased downstream phosphorylation |
| DHX37 | Q8IY37 | Hypomorph in RecA2/OB-fold; impaired RNA helicase/SSU processome function |
| SRY | Q05066 | Loss of DNA binding/bending (HMG box); impaired nuclear import |
| SOX9 | P48436 | Haploinsufficiency, or enhancer-mediated dosage loss |
| DHH | O43323 | Loss of function; the Umehara initiation-codon variant abolishes translation entirely |

**No protein aggregation, misfolding-with-inclusion, or proteinopathy mechanism is involved.** MAP3K1 variants alter *local folding and surface topology* (per Ostrer), which changes binding partners — not a misfolding/aggregation disease.

### 6.5 Metabolic changes

The relevant "metabolism" is **steroidogenesis**, not intermediary metabolism:
- **Reduced fetal and postnatal testosterone** (CHEBI:17347) biosynthesis due to reduced Leydig cell mass and, for NR5A1, reduced transcription of *STAR*, *CYP11A1*, *CYP17A1*, *HSD17B3*.
- Reduced **dihydrotestosterone** (CHEBI:16330; canonical label `17beta-hydroxy-5alpha-androstan-3-one`) from reduced substrate.
- Reduced **AMH** (a TGF-β family glycoprotein, not a CHEBI entity — use the HPO lab term).
- Reduced **inhibin B** (Sertoli cell product).
- Reduced **INSL3** → cryptorchidism.
- In female-assigned patients post-gonadectomy: **decreased 17β-estradiol** (CHEBI:16469) requiring replacement.
- **No energy, lipid, or amino-acid metabolic derangement.** This is not an inborn error of metabolism and must not be modelled as one.

### 6.6 Immune system involvement

**None.** 46,XY PGD is not autoimmune, not an immunodeficiency, and not inflammatory. The only tangential immune consideration is immune surveillance of germ cell neoplasia in situ, which is not disease-specific. Do not curate an immune arm.

### 6.7 Tissue damage mechanisms

The gonad is **maldeveloped, not damaged** — this is a critical modelling distinction. There is no ischemia, oxidative-stress injury, or necrosis. The observed histological features are developmental and secondary:
- **Peritubular fibrosis** — a hallmark of dysgenetic testis (GeneReviews: dysgenetic testes show *"decreased size and number of seminiferous tubules, reduced number or absence of germ cells, peritubular fibrosis, and hyperplasia of Leydig cells"*). This is aberrant matrix deposition in a maldeveloped gonad, **not** a conserved fibrotic response to injury — **do not `conforms_to: fibrotic_response`**.
- **Streak gonad** — ovarian-type stroma without follicles or tubules; the end-state of complete determination failure on one side.
- **Progressive germ cell loss** — apoptotic attrition of germ cells in an unsupportive niche.
- **Leydig cell hyperplasia** — a *compensatory* response to LH drive, not damage.

### 6.8 Biochemical abnormalities

- Sertoli cell: ↓AMH (HP:0031103), ↓inhibin B (HP:0031100)
- Leydig cell: ↓testosterone (HP:0040171), ↓INSL3, blunted hCG response (only 66% of PGDm double testosterone on hCG stimulation, PMID:40208111)
- Pituitary feedback: ↑FSH (HP:0008232), ↑LH (HP:0011969) → hypergonadotropic hypogonadism (HP:0000815)
- NR5A1 subgroup only: ↓cortisol/↑ACTH if adrenal involvement (HP:0000846)
- **No enzyme deficiency, no ion channel defect, no receptor defect** — this distinguishes PGD from the two main differential diagnoses: androgen biosynthesis defects (17β-HSD3, 5α-reductase-2 — true enzymopathies) and androgen insensitivity (AR receptor defect).

### 6.9 Epigenetic changes

No primary epigenetic lesion. The mechanistically relevant chromatin biology is **CBX2/Polycomb-mediated repression of the ovarian program** and **enhancer-dependent SOX9 dosage** (see §4.8). **Genuine gap:** no methylome or ATAC-seq study of human dysgenetic gonadal tissue from PGD patients has been published.

### 6.10 Molecular profiling

**Transcriptomics.** No PGD-patient gonadal transcriptome dataset exists. The available data are (a) **human fetal gonad scRNA-seq atlases** (Human Cell Atlas; Guo et al.; Garcia-Alonso et al. *Nature* 2022 human gonadal development atlas) defining the supporting/Sertoli, Leydig, germ, and coelomic epithelial lineages against which dysgenesis can be interpreted; and (b) **in vitro** cell-line transcriptional readouts from variant-function studies (NT2/D1, KGN — PMC8927045). GEO/ArrayExpress hold no PGD-labelled series.

**Proteomics / metabolomics / lipidomics.** **None available.** No PRIDE, MetaboLights, or Metabolomics Workbench dataset for 46,XY PGD. Explicitly a gap.

**Genomic structural features.** The clinically important ones are the SOX9 upstream regulatory region (RevSex/Enh13, ~600 kb 5′ of SOX9, chr17q24.3), the NR0B1 Xp21.2 dosage-sensitive region, 9p24.3 (DMRT1), and 1p36 (WNT4/RSPO1). These are **non-coding/CNV lesions requiring CMA or WGS**, and are the strongest single argument against exome-only testing.

**Single-cell / spatial.** No PGD-specific single-cell or spatial transcriptomic study. The Idris 2025 review recommends multi-omic escalation (transcriptomics, Hi-C) for VUS resolution — aspirational, not yet standard.

**Functional genomics screens.** No published CRISPR/RNAi screen for testis-determination modifiers in a human gonadal-somatic system. DepMap does not model this tissue. A clear, high-value experimental gap.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary (directly affected by the causal lesion):**
- **Gonad** — UBERON:0000991 (the primary lesion site)
- **Testis** — UBERON:0000473 (dysgenetic)
- **Ovary** — UBERON:0000992 (as ontological reference for the streak gonad; a streak is ovarian-type stroma)

**Secondary (affected by the hormone deficits, i.e., downstream):**
- **Müllerian duct** — UBERON:0003890 → incomplete regression
- **Uterus** — UBERON:0000995 (present in 51% of PGDf, 31.3% of PGDm — PMID:40208111)
- **Vagina** — UBERON:0000996 (upper vagina Müllerian-derived; hypoplasia HP:0008726)
- **Mesonephric (Wolffian) duct** — UBERON:0003074 → incomplete development
- **Epididymis** — UBERON:0001301, **prostate gland** — UBERON:0002367 (hypoplastic)
- **Undifferentiated genital tubercle** — UBERON:0005876 → hypospadias, micropenis, clitoromegaly
- **Internal genitalia** — UBERON:0004175
- **Male reproductive system** — UBERON:0000079
- **Adrenal gland** — UBERON:0002369 (**NR5A1 subgroup only**)
- **Kidney** (Wilms tumour, nephrotic syndrome) — **WT1 subgroup only**
- **Peripheral nerve** — **DHH subgroup only** (minifascicular neuropathy)
- **Bone** — secondary osteoporosis from hypogonadism

**Body systems:** reproductive (primary), endocrine (primary), urinary (via urogenital sinus/hypospadias), skeletal (secondary), nervous (DHH subgroup only), cardiovascular (very rare, contiguous-deletion cases).

### 7.2 Tissue and cell level

| Cell type | CL term (verified) | Involvement |
|---|---|---|
| **Sertoli cell** | **CL:0000216** | **The pivotal cell** — fate commitment fails; ↓AMH, ↓inhibin B |
| **Leydig cell** | **CL:0000178** | Fetal Leydig deficiency → ↓T, ↓INSL3; postnatal hyperplasia under LH drive |
| **Germ cell** | **CL:0000586** | Depleted; when retained, arrested immature → neoplastic precursor |
| **Male germ cell** | **CL:0000015** | |
| **Primordial germ cell** | **CL:0000670** | The migratory population entering a defective niche |
| **Granulosa cell** | **CL:0000501** | Ontological counterpart of the mis-specified supporting lineage |
| **Peritubular myoid cell** | **CL:0002481** | Contributes to cord formation; abnormal → peritubular fibrosis |
| **Sperm** | **CL:0000019** | Absent/severely reduced (azoospermia, severe oligozoospermia) |

Note: `CL:0000630 supporting cell` exists but is the generic (non-gonadal) class — CL currently lacks a clean "bipotential gonadal supporting cell precursor" term. This is a **real ontology gap** worth recording; the honest curation is CL:0000216 (Sertoli cell) with a `preferred_term` of "bipotential gonadal supporting cell precursor" per the `preferred_term` > `term.label` specificity convention in CLAUDE.md.

**Tissue types:** gonadal somatic (mesenchymal/epithelial-derived supporting lineage) — primary; germinal epithelium — secondary; connective tissue (peritubular fibrosis); the streak gonad's ovarian-type stroma.

### 7.3 Subcellular level (GO Cellular Component)

- **Nucleus** (GO:0005634) — SF-1, SOX9, SRY, WT1, DMRT1 are all nuclear transcription factors; β-catenin nuclear translocation is the MAP3K1 effector step.
- **Cytosol** (GO:0005829) — MAP3K1 signalling complex, β-catenin destruction complex (GSK3β/APC/AXIN).
- **Nucleolus** (GO:0005730) — DHX37/ribosome biogenesis.
- **Extracellular region / extracellular space** (GO:0005576/GO:0005615) — DHH, AMH, FGF9, WNT4, RSPO1 (all secreted).
- **Plasma membrane** (GO:0005886) — PTCH1/SMO (hedgehog), FZD/LRP (Wnt), FGFR2.

*Verify these CC IDs with OAK before committing; I verified only the BP terms above.*

### 7.4 Localization and lateralization

**Bilateral but characteristically ASYMMETRIC** — this is a defining and under-appreciated feature. *"Partial GD is defined by bilateral dysgenetic gonads. The histology of dysgenetic testes may vary from gonads with a few tubular structures and predominance of fibrous tissue to those with mild abnormalities, and they may be found bilaterally or associated with streak gonads."* The classic PGD configuration is **a dysgenetic testis on one side and a streak gonad on the other** (as in Umehara's index DHH case).

**Gonadal position is variable along the descent path:** *"depending on the percentage of testicular tissue, dysgenetic testes can be found anywhere along the line of testis descent, from the abdomen, and in cases of normal testes, in the scrotum."* Intra-abdominal position independently raises tumour risk.

Consequently the **internal duct derivatives are often asymmetric too**: a hemi-uterus/fallopian tube on the side with poorer AMH output and a vas/epididymis on the better side. Curate lateralization as **bilateral, asymmetric**.

---

## 8. Temporal Development

### 8.1 Onset

- **Biological onset: embryonic**, gestational weeks ~6–8 (the human testis-determination window; mouse E10.5–E12.5). The determination event is over before the second trimester.
- **Clinical onset: congenital** (`HP:0003577`), recognised **neonatally** in most (`HP:0003623`) via atypical genitalia.
- **Onset pattern: insidious/static developmental** — not acute, not subacute. The genital phenotype is fully formed at birth.
- **Bimodal ascertainment.** Infancy (atypical genitalia) for ~100% of PGDm and 62.1% of PGDf; **adolescence** for a substantial PGDf minority (17.9% delayed puberty, 8% virilization). Danish population data: median age at diagnosis **17.0 years** for female-presenting gonadal dysgenesis (PMID:27603905).

### 8.2 Progression

**There are no formal disease stages.** A pragmatic natural-history framework:

| Period | Events |
|---|---|
| **Fetal (wk 6–20)** | Determination failure → dysgenetic gonad → partial AMH/androgen deficiency → genital and ductal phenotype fixed |
| **Neonatal (0–6 mo)** | "Mini-puberty" — the diagnostic window when gonadotropins/testosterone/AMH/inhibin B are physiologically elevated and most informative. **Missing it forces reliance on hCG stimulation later.** |
| **Childhood** | Hormonally quiescent; risk of missed diagnosis; gonadal position/surveillance decisions |
| **Puberty (~11–16 y)** | **The critical branch point.** PGDm: 80% enter puberty spontaneously, 59% reach G5 unaided. PGDf with retained gonads: **42.3% virilize** — clitoromegaly, hirsutism, voice change. This is often the trigger for reassignment (16.1% of PGDf reassigned to male). |
| **Young adulthood** | Infertility recognised; hormone replacement stabilised; peak diagnostic yield for germ cell neoplasia |
| **Adulthood** | Cumulative neoplasia risk; osteoporosis if under-replaced; DHH subgroup: peripheral neuropathy onset **ages 20–30** |

**Progression rate:** slow and variable. **Course pattern:** static developmental lesion with **progressive** endocrine decline in a subset, and **progressive** (cumulative) oncological risk. **Duration:** chronic, lifelong.

### 8.3 Patterns

- **Remission:** not applicable — no spontaneous or treatment-induced remission. Hormone replacement and surgery are palliative/reconstructive, not curative.
- **Critical windows:**
  1. **Fetal wk 6–8** — the only window in which the primary defect could theoretically be prevented; currently inaccessible.
  2. **Mini-puberty (0–6 months)** — the highest-yield endocrine diagnostic window.
  3. **Peri-pubertal (~10–13 y)** — the decision point for gonadal retention vs removal in PGDf (retention permits spontaneous puberty and preserves the small chance of gonadal function, but risks unwanted virilization *and* is when neoplasia risk begins to accrue). This trade-off is now quantified by PMID:40208111 and is the most clinically actionable temporal finding for this entity.
  4. **Adolescence–young adulthood** — bone mass accrual window; adequate sex-steroid replacement here determines lifetime fracture risk.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**PGD-specific prevalence is not directly published.** The best anchor is the Danish nationwide registry study (Berglund A, Johannsen TH, Stochholm K, Viuff MH, Fedder J, Main KM, Gravholt CH. *J Clin Endocrinol Metab* 2016;101(12):4532-4540; **PMID:27603905**):

> "The prevalence of 46,XY females was 6.4 per 100 000 live born females."

with **gonadal dysgenesis at 1.5 per 100,000** (vs AIS 4.1 per 100,000). Note this counts **phenotypic females only** — it therefore **undercounts PGD substantially**, since roughly half of PGD patients are assigned male (I-DSD: PGDf 107 vs PGDm 103). A defensible estimate for all 46,XY gonadal dysgenesis (CGD+PGD, both sexes of rearing) is therefore on the order of **~3 per 100,000 births**, with PGD perhaps **1–2 per 100,000** — but flag this as an **inference, not a published figure**.

Other anchors:
- Incidence of gonadal dysgenesis reported as **~1 per 80,000 births**; AIS 1–5 per 100,000.
- Newborns with ambiguous genitalia: **1/4,500 to 1/5,000** — the broader denominator from which PGD is drawn.
- Orphanet classifies ORPHA:251510 under `rare`; the specific Orphanet prevalence class for this entity is **not documented** (`NOT_YET_DOCUMENTED` is the honest `prevalence_class`).

**Suggested KB `prevalence` records:**
```yaml
prevalence:
- population: Denmark (phenotypic females, nationwide registry)
  measure_type: POINT_PREVALENCE
  prevalence_class: BAND_1_9_PER_1000000
  rate_per_100000: 1.5
  notes: >-
    46,XY gonadal dysgenesis (complete + partial pooled) among live-born
    phenotypic females. Undercounts 46,XY PGD because ~half of PGD patients
    are assigned male at birth.
  evidence:
  - reference: PMID:27603905
    supports: PARTIAL
    evidence_source: HUMAN_CLINICAL
    snippet: "The prevalence of 46,XY females was 6.4 per 100 000 live born females"
    explanation: >-
      Nationwide Danish prevalence; the paper reports gonadal dysgenesis at
      1.5 per 100,000 within this 6.4 per 100,000 total.
```
*(Verify the exact snippet against the cached abstract with `just fetch-reference PMID:27603905` before committing.)*

### 9.2 Inheritance

**46,XY PGD is genetically heterogeneous with four distinct inheritance modes** — this should be modelled as multiple `Inheritance` blocks, each with a bound HPO term:

| Mode | HPO term | Genes | Notes |
|---|---|---|---|
| **Sex-limited autosomal dominant** | **HP:0000006** (Autosomal dominant inheritance) | NR5A1, MAP3K1, DHX37, DMRT1, SOX9, SOX8, ZFPM2, GATA4 | 50% transmission to 46,XY offspring; 46,XX sibs generally unaffected. Frequently de novo, or inherited from a mildly affected father or an unaffected mother |
| **Sex-limited autosomal recessive** | **HP:0000007** (Autosomal recessive inheritance) | DHH | 25% risk to 46,XY sibs; heterozygotes asymptomatic |
| **Y-linked** | **HP:0001450** (Y-linked inheritance) | SRY | Usually de novo; paternal transmission rare (mosaicism/reduced penetrance) |
| **X-linked** | **HP:0001417** (X-linked inheritance) | NR0B1 (DAX1) duplication, Xp21.2 | Inherited from carrier mother in most cases; 50% per pregnancy |
| **Digenic** | **HP:0010984** (Digenic inheritance) | DHX37 + NR5A1 | Documented double-heterozygotes with the most severe phenotype (PMC10222664) |

*Verify HP:0000006/0000007/0001450/0001417/0010984 with OAK before committing — I verified HP:0010984's role in the CLAUDE.md convention but did not run OAK on the four standard MOI terms in this session.*

**Penetrance.** Gene-dependent and one of the most important curatable facts:
- **MAP3K1: "virtually complete penetrance in 46,XY individuals"** (PMID:35290982) — unusually high.
- **NR5A1: markedly incomplete and variable**; unaffected/mildly affected transmitting parents are common; the same allele produces CGD, PGD, hypospadias, or isolated infertility within one family.
- **DHX37:** high but with a de novo excess (5/13 de novo in the discovery cohort).
- **All of these are sex-limited**: penetrance in a 46,XX background is ~0 for the gonadal phenotype (with the NR5A1 exception of primary ovarian insufficiency).

**Expressivity: highly variable** — this *is* the disease. The CGD↔PGD↔TRS↔hypospadias↔infertility spectrum arises from single alleles.

**Genetic anticipation:** **Not applicable.** No repeat-expansion mechanism.

**Germline mosaicism:** documented (particularly SRY and NR5A1), and is the standard counselling explanation for recurrence in a sibship with clinically negative parents. Empiric recurrence risk after an apparently de novo variant should be quoted as low-but-not-zero (~1%).

**Founder effects:** none established for 46,XY PGD. The DHH R124Q variant in two Syrian sisters (PMID:25927242) reflects **consanguinity**, not a founder haplotype.

**Consanguinity:** relevant only for the **autosomal recessive** DHH route (and other rare AR causes). Consanguineous populations will show enrichment of the recessive fraction; outbred populations are dominated by de novo AD variants.

**Carrier frequency:** not established for any gene. Pathogenic variants are individually private/ultra-rare; population carrier screening is **not indicated**.

### 9.3 Population demographics

- **Affected populations:** no ethnic predominance. The worldwide cohort analysis (14 cohorts, 2013–2023, six continents) found *"no mutations with a clear geographic or ethnic predominance,"* though *MAP3K1* variant frequencies differed between US, Australian, and Korean cohorts (DOI:10.3389/fgene.2024.1387598). Molecular diagnostic yield varied **24.3% (Korea) to 64.3% (China)**, most cohorts **35–50%** — this variation likely reflects ascertainment and sequencing strategy more than true biology.
- **Geographic distribution:** worldwide; no endemic regions. The recessive DHH fraction will be over-represented where consanguinity is common (Middle East, North Africa, South Asia).
- **Sex ratio:** **Not meaningfully applicable and must be handled carefully in the KB.** All affected individuals are **46,XY by definition** (chromosomal sex ratio ∞:0 male). Sex *of rearing* is roughly balanced: I-DSD PGDf 107 vs PGDm 103 (~1:1). Record chromosomal sex as an inclusion criterion, and sex of rearing as an outcome variable — never as "sex ratio."
- **Age distribution:** bimodal at diagnosis (neonatal peak; adolescent second peak in female-presenting cases). Prevalence is lifelong once diagnosed; no excess mortality shifts the age structure.

---

## 10. Diagnostics

### 10.1 Clinical and laboratory tests

**Karyotype is the entry point and the definitional test.** Standard peripheral-blood karyotype with **≥30 cells counted** (to exclude low-level 45,X mosaicism), **plus FISH for SRY**, or chromosomal microarray. GeneReviews: *"Karyotype with FISH for SRY or chromosomal microarray to determine sex chromosome complement and SRY presence/absence."* A 46,XY non-mosaic result is required; detected mosaicism reclassifies to MGD.

**Hormonal panel** (GeneReviews recommended set):
| Analyte | LOINC (representative) | Interpretation in PGD |
|---|---|---|
| Anti-Müllerian hormone (AMH) | LOINC:38476-0 | **Low** (48% PGDf, 58.1% PGDm) — the best single marker of Sertoli cell mass |
| Inhibin B | LOINC:32079-8 | Low — Sertoli function |
| Testosterone, basal | LOINC:2986-8 | Low or low-normal; **similar between PGDf and PGDm at age ≥13** |
| Testosterone, hCG-stimulated | — | **Only 66.0% (31/47) of PGDm doubled testosterone** — a blunted response is characteristic |
| FSH | LOINC:15067-2 | **Elevated** |
| LH | LOINC:10501-5 | **Elevated** |
| Electrolytes, 17-OHP, ACTH, cortisol | — | To exclude CAH and detect NR5A1-associated adrenal insufficiency |

**Key interpretive rules from GeneReviews:**
> "A greatly elevated follicle-stimulating hormone and/or luteinizing hormone in infancy is usually associated with nonfunctional gonads."

> "Hormonal evaluation cannot distinguish between one versus two functioning gonads."

That second statement is important and under-appreciated: because PGD is characteristically **asymmetric**, biochemistry describes total gonadal output and cannot localise it — **imaging and, ultimately, surgical/histological assessment are required to characterise each gonad separately.**

**Imaging:**
- **Pelvic/abdominal/inguinal ultrasound** (first line) — presence of uterus (51% PGDf, 31.3% PGDm), gonadal position and size.
- **MRI** — better for intra-abdominal gonads and Müllerian anatomy.
- **Genitography / retrograde urethrography** — urogenital sinus anatomy.
- **Bone age radiograph** — HP:0002750 delayed skeletal maturation; puberty tracking.
- **DXA** — bone density surveillance under hormone replacement (HP:0000939 osteoporosis).

**Functional/other:** external masculinization score (EMS) or **external genital score (EGS)** — the I-DSD standard, reported as median **4.0 (PGDf) vs 7.0 (PGDm)**; this is the quantitative phenotype backbone of the field and should be recorded as a measurement in the KB where available. **Electrophysiology (NCS/EMG)** is indicated only in the **DHH subgroup** to detect minifascicular neuropathy.

**Biopsy / histopathology — the definitive gonadal test.**
Dysgenetic testis: *"decreased size and number of seminiferous tubules, reduced number or absence of germ cells, peritubular fibrosis, and hyperplasia of Leydig cells."* Streak gonad: ovarian-type stroma without follicles.

**Immunohistochemistry for neoplastic risk (essential, and easy to omit):**
- **OCT3/4 (POU5F1)** and **PLAP**, **AP-2γ (TFAP2C)** — mark germ cells arrested in an immature pluripotent state = germ cell neoplasia in situ (GCNIS)/pre-gonadoblastoma.
- **TSPY** — the Y-encoded risk factor; *"The testes-specific protein Y 1 (TSPY1) gene, located on the Y chromosome, is considered the most significant gene responsible for a high risk of tumorigenesis. This protein… functions as a protooncogenic factor when expressed in an incompatible niche with immature germ cells."*
- **SOX9/AMH** — Sertoli cell identity; **FOXL2** — inappropriate granulosa-type differentiation.
- **SALL4, D2-40/podoplanin, KIT/CD117** — germ cell tumour panel.

Note the diagnostic-sequencing paradox: *"Because the risk of gonadoblastoma in these patients is so high, precise diagnosis of the type of GD is usually determined after prophylactic or therapeutic gonadectomy"* — definitive gonadal classification often follows, rather than precedes, the surgical decision.

### 10.2 Genetic testing

**Recommended approach (GeneReviews + Idris et al. 2025, PMID:39081229):**

1. **Karyotype ± FISH SRY** (mandatory first step; defines the entity).
2. **Chromosomal microarray (CMA)** — detects 9p24 deletion, Xp21.2/NR0B1 duplication, 1p36 duplication, and SOX9 regulatory CNVs. **Do not skip in favour of exome.**
3. **DSD multigene panel (MPS)** — *"Start with targeted MPS panels (cost-effective, manageable data)"*; yield **30%–60%**.
4. **Whole exome sequencing** if panel negative; yield **30%–66.7%**.
5. **Whole genome sequencing** for suspected structural/non-coding lesions, *"e.g., SOX9 enhancers"*; limited comparative data but superior for structural variants.
6. **Sanger single-gene testing** — largely obsolete standalone (*"~15%"* yield); reserve for targeted familial variant testing.

**Overall real-world yield:** *"Genomic technologies, such as massively parallel sequencing (MPS), have proven to be a valuable diagnostic tool for individuals or families with DSD"* delivering **30%–45%**. PGD-specific: **42.3%** (I-DSD 2025).

**Panel gene content (minimum for PGD):** SRY, NR5A1, MAP3K1, DHX37, SOX9 (+ regulatory region), SOX8, DHH, DMRT1, WT1, NR0B1, ZFPM2, GATA4, WNT4, RSPO1, CBX2, PPP2R3C, PBX1, HHAT, LHX9, MYRF, PPP1R12A, plus the androgen-pathway differential genes (AR, SRD5A2, HSD17B3, LHCGR, StAR, CYP17A1) — because the clinical differential cannot be resolved without them.

**Not indicated:** mitochondrial DNA testing; repeat-expansion testing. **Y-chromosome microdeletion (AZF) testing is NOT indicated in non-mosaic 46,XY PGD** — the Brazilian series found zero deletions in 13 PGD patients (PMC3827999). It *is* informative in 45,X/46,XY MGD (40% positive).

**Emerging:** *"Integrate transcriptomics, proteomics, and Hi-C analysis to resolve pathogenicity in ambiguous cases and detect mosaicism across multiple tissues"* — research-grade, not standard of care.

### 10.3 Omics-based diagnostics

RNA-seq (for splice-variant resolution), proteomics, metabolomics, epigenomics, liquid biopsy: **none are established diagnostics for 46,XY PGD.** RNA-seq on gonadal tissue or fibroblasts is the most plausible near-term addition for VUS resolution.

### 10.4 Clinical criteria and differential diagnosis

**Diagnostic criteria** derive from the 2006 Chicago Consensus (PMID:16624884) and the 2016 Global DSD Update (PMID:26820577), which established the DSD classification (46,XY DSD → disorders of gonadal/testicular development → partial gonadal dysgenesis). There is no formal scored criteria set; diagnosis is the conjunction of:
1. Non-mosaic 46,XY karyotype
2. Ambiguous/undervirilized external genitalia
3. Evidence of partial testicular dysgenesis (biochemical: low AMH/inhibin B, elevated gonadotropins, blunted hCG response; and/or histological: dysgenetic testis ± streak)
4. Variable Müllerian retention
5. Absence of syndromic features (for the nonsyndromic entity)

**Differential diagnosis — with the discriminating feature:**

| Condition | Key discriminator from 46,XY PGD |
|---|---|
| **46,XY complete gonadal dysgenesis (Swyer)** | Bilateral **streak** gonads, fully female external genitalia, **fully developed** uterus; presents with primary amenorrhoea, not ambiguity |
| **Mixed gonadal dysgenesis (MGD)** | **45,X/46,XY mosaic karyotype** (+ Turner stigmata, short stature, Yq microdeletions in 40%) |
| **Partial androgen insensitivity (PAIS)** | **Normal/high** testosterone, **normal AMH**, **no Müllerian structures**, normal testis histology; AR variant |
| **17β-HSD3 deficiency** | Elevated **androstenedione/testosterone ratio**; no Müllerian structures |
| **5α-reductase-2 deficiency** | Elevated **testosterone/DHT ratio**; normal testes; marked pubertal virilization |
| **StAR / CYP17A1 / CYP11A1 defects** | Adrenal insufficiency + salt-wasting; low all androgens |
| **LHCGR inactivating (Leydig cell hypoplasia)** | Low testosterone, **high LH**, absent hCG response, **absent Müllerian structures** (AMH intact) |
| **Ovotesticular DSD** | Both ovarian **follicles** and testicular tubules in the same or contralateral gonad (histological) |
| **Persistent Müllerian duct syndrome (AMH/AMHR2)** | Müllerian structures with **normal male external genitalia** and normal androgenization |
| **Testicular regression syndrome (TRS)** | Absent gonads with a vascular/vestigial remnant; overlaps DHX37 genetically — a spectrum boundary, not a clean separation |
| **Isolated severe hypospadias** | The mild extreme of PGD; the boundary is genuinely arbitrary |
| **Syndromic GD** (Denys–Drash/Frasier, campomelic dysplasia, 9p deletion, ATRX, SLO/DHCR7) | Extra-gonadal features |

### 10.5 Screening

- **Newborn screening: not performed and not proposed.** 46,XY PGD is not on any RUSP/newborn-screening panel; there is no analyte-based screen. The de facto "screen" is **newborn physical examination of the genitalia** — ambiguity should trigger urgent DSD-team referral before hospital discharge (a Chicago Consensus recommendation).
- **Carrier screening: not indicated.** Variants are private; no founder alleles.
- **Cascade screening: indicated and specifically recommended.** Granados et al. are explicit: *"Identification of a MAP3K1 variant should prompt an evaluation for DSD in female siblings of the proband"* (PMID:28504475) — because a phenotypically female sibling may be an unrecognised 46,XY CGD/PGD patient with an unmanaged gonadal tumour risk. This is the single highest-value screening action in this disease.
- **Prenatal:** discordance between **NIPT/cfDNA-predicted male sex** (or an XY karyotype on CVS/amnio) and **female-appearing genitalia on ultrasound** is an increasingly common route to prenatal suspicion. Confirmation requires postnatal evaluation.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

**Life expectancy is normal.** 46,XY PGD is not a life-limiting condition. No PGD-specific survival, mortality, or disease-specific-mortality data exist because there is no measurable excess mortality. Two qualifiers:
- **Malignancy is the one potentially fatal complication** — an untreated invasive dysgerminoma/seminoma. With surveillance and gonadectomy, germ cell tumours arising in dysgenetic gonads are highly curable (dysgerminoma/seminoma are exquisitely chemo- and radiosensitive).
- **The WT1 subgroup** has renal-failure and Wilms-tumour mortality — but that is a different (syndromic) entity.

`survival_rate`, `life_expectancy`, `mortality_rate`: **not applicable / no excess** — record explicitly rather than leaving blank.

### 11.2 Morbidity and function

- **Infertility: near-universal.** *"Most individuals with a nonsyndromic DSD are infertile due to dysgenetic or streak gonads."* All three semen analyses in the long-term male-reared PGD series showed **severe oligozoospermia** (PMID:25580123). Exceptions: *"some pathogenic variants in NR5A1 are associated with normal testicular development in individuals with a 46,XY chromosome complement, which may allow for fertility, although assisted reproductive technology may be required."* 46,XY individuals with Müllerian structures may achieve pregnancy via **oocyte donation**.
- **Lifelong hormone dependence** in those who undergo gonadectomy or have insufficient endogenous function.
- **Osteoporosis (HP:0000939)** — preventable with adequate replacement; a marker of care quality.
- **Growth is normal** — final heights −1.57 to +0.80 SDS (PMID:25580123).
- **No cognitive/neurological impairment intrinsic to the disease** (the 30% learning-disability figure in a 10-patient series is not generalisable). The DHH subgroup develops peripheral neuropathy at **20–30 years**.
- **QoL:** dominated by sexual function, body image, fertility loss, gender-identity concordance, and the burden of surgical decisions made in infancy. No disease-specific PROM; dsd-LIFE used generic instruments.

### 11.3 Gonadal neoplasia — the defining prognostic issue

**The authoritative multicentre figure** (Slowikowska-Hilczer J, Szarras-Czapnik M, Duranteau L, et al.; dsd-LIFE group. *Risk of gonadal neoplasia in patients with disorders/differences of sex development.* Cancer Epidemiol 2020;69:101800; **PMID:32905884**; n=1,040):

> "germ-cell neoplasia was present in 12 % of patients with DSD and in 14 % of those with XY DSD"

with the risk gradient:

| Group | Germ cell neoplasia risk |
|---|---|
| **46,XY gonadal dysgenesis (all)** | **36%** |
| — complete GD | **33%** |
| — **partial GD** | **23%** |
| Mixed GD | 8% |
| Complete AIS | 6% |
| Partial AIS, XX male, CAH, androgen biosynthesis defects | **0%** |

Also: *"benign sex cord-stromal tumours (Sertoli- and Leydig-cell tumours) were noted only in patients with complete AIS (3.1 %) and Klinefelter syndrome (14.3 %)."* Conclusion: **adult patients with gonadal dysgenesis and a Y chromosome require intensive medical surveillance.**

**The PGD-specific, sex-of-rearing-stratified figure** (I-DSD 2025, PMID:40208111) — **this is the most actionable number in the entry**:

| Group | Gonadal pre-/malignancy |
|---|---|
| CGD | **33.8%** |
| **PGD assigned female (PGDf)** | **19.7%** |
| **PGD assigned male (PGDm)** | **8.8%** |

The four-fold PGDf:PGDm gradient is consistent with the mechanistic model: **more severe dysgenesis → more immature/arrested germ cells in an inhospitable niche → more TSPY-driven neoplastic transformation**, and **intra-abdominal position** (more common in the less virilized) further raises risk. Note that these are *cross-sectional* prevalences at variable follow-up, not lifetime cumulative incidence — the true lifetime risk is higher.

Countervailing small-series data: *"There was no case of testicular neoplasia"* in 10 male-reared PGD patients followed 13.5–19.7 years (PMID:25580123) — consistent with the low 8.8% PGDm figure and with scrotal-position gonads being lower risk.

**Risk markers:** presence of Y chromosome material (obligate here); **TSPY1** expression; **OCT3/4-positive immature germ cells**; intra-abdominal gonadal position; degree of dysgenesis; older age.

### 11.4 Disease course, complications, recovery

**Complications:** gonadoblastoma → dysgerminoma/seminoma; hypogonadism and osteoporosis; infertility; urological complications of hypospadias repair (fistula, stricture, need for reoperation — common); vaginal stenosis after vaginoplasty; psychological distress and gender dysphoria; surgical loss of genital sensation.

**Recovery potential:** the gonadal lesion is **irreversible**. Hormone replacement fully restores secondary sexual characteristics and bone health. Fertility is generally unrecoverable.

### 11.5 Prognostic factors

| Factor | Prognostic for |
|---|---|
| **External genital score at presentation** | Sex assignment, surgical burden, likely spontaneous puberty |
| **Degree of dysgenesis / gonadal histology** | Puberty, tumour risk |
| **AMH and inhibin B levels** | Sertoli cell reserve → spontaneous puberty likelihood (low AMH in 48% PGDf / 58.1% PGDm) |
| **hCG-stimulated testosterone response** | Leydig reserve; 66% of PGDm doubled T |
| **Gonadal position (scrotal vs intra-abdominal)** | Tumour risk (lower if scrotal), feasibility of surveillance |
| **Causative gene** | NR5A1 → possible adrenal involvement + rarely preserved fertility; MAP3K1 → near-complete penetrance, recurrence counselling; DHH → neuropathy at 20–30 y; WT1 → renal/Wilms surveillance |
| **Sex of rearing** | Tumour risk (PGDf 19.7% vs PGDm 8.8%); reassignment likelihood (16.1% vs 5.3%) |
| **Presence of a uterus** | Fertility option via oocyte donation |

**Prognostic biomarkers:** AMH and inhibin B (gonadal reserve); OCT3/4 and TSPY immunohistochemistry (neoplastic risk); serum tumour markers (AFP, β-hCG, LDH) for surveillance of established germ cell tumours — though these are insensitive for gonadoblastoma/GCNIS.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**. Management is multidisciplinary, lifelong, and increasingly shared-decision-making driven. The framing authority is the Chicago Consensus (PMID:16624884) and the 2016 Global DSD Update (PMID:26820577); the ESPU–SPU 2020 consensus covers the surgical dimension.

### 12.1 Sex assignment (precedes everything else)

GeneReviews: *"All individuals should receive a sex of rearing"* determined by *"underlying diagnosis, expert opinion, and parental beliefs,"* ideally by an **interdisciplinary team before newborn discharge**. The Global DSD Update's honest caveat: *"it is still impossible to predict gender development in an individual case with certainty."*

The empirical outcome data (I-DSD 2025) should inform this conversation directly: **16.1% of PGDf and 5.3% of PGDm later underwent sex reassignment** — the highest reassignment rate in the DSD spectrum, and a strong argument for conservative, reversible early management.

### 12.2 Hormone therapy

| Treatment | NCIT (verified) | Therapeutic agent (CHEBI/NCIT) | Indication |
|---|---|---|---|
| **Testosterone replacement / induction** | NCIT:C15599 Hormone Replacement Therapy | CHEBI:17347 testosterone; NCIT:C1247 Testosterone Enanthate; NCIT:C1246 Testosterone Cypionate; NCIT:C1249 Testosterone Undecanoate | Male-assigned: short infant course for micropenis (*"stretched penile length >2.5 SD below mean"*); pubertal induction and maintenance |
| **Estrogen replacement** | NCIT:C15599 Hormone Replacement Therapy | CHEBI:16469 17beta-estradiol | Female-assigned: breast development, pubertal induction, bone health |
| **Progestogen** | NCIT:C15599 | progesterone (verify CHEBI) | Added once pubertal progression is advanced, **if a uterus is present** (endometrial protection) |
| **Adrenal replacement** | NCIT:C15986 Pharmacotherapy | hydrocortisone (verify CHEBI) | **NR5A1 subgroup with adrenal insufficiency only** |
| Bone protection | NCIT:C15747 Supportive Care | calcium, cholecalciferol | Adjunct to sex-steroid replacement |

`therapeutic_modality: SMALL_MOLECULE` for the steroid hormones.

### 12.3 Surgical and interventional

**The governing principle (GeneReviews), verbatim:**
> "Surgical decisions should be made after detailed discussion with the family about risks, benefits, and limitations."

and

> "Many surgeries are not medically necessary; consideration should be given to delaying surgery in order to allow the affected individual to participate in the decision-making process."

This is the most contested area in DSD care and should be curated with the caveat prominent, not buried.

| Procedure | NCIT (verified) | Notes |
|---|---|---|
| **Gonadectomy / orchiectomy** | **NCIT:C15288 Orchiectomy** (+ NCIT:C94458 Prophylactic Surgery) | The central oncological intervention. See decision rule below |
| **Orchiopexy** | **NCIT:C111066 Orchiopexy** | Places a functional dysgenetic testis in the scrotum, enabling palpation-based surveillance |
| Hypospadias repair | NCIT:C15329 Surgical Procedure | Male-assigned |
| Scrotoplasty, phalloplasty | NCIT:C15329 | Male-assigned |
| Clitoroplasty | NCIT:C15329 | Female-assigned; **highly contested**, increasingly deferred |
| Vaginoplasty / urogenital sinus mobilization | NCIT:C15329 | Female-assigned; **vaginal dilation is the non-surgical alternative and is often first-line** |
| Müllerian remnant excision | NCIT:C15329 | If symptomatic (haematometra, recurrent infection) |

`therapeutic_modality: SURGERY` for all of the above.

**The gonadectomy decision rule (GeneReviews):**
- Streak and **nonfunctional** dysgenetic gonads carry *"increased risk for the development of gonadoblastoma and should be surgically removed if nonfunctional."*
- Indicators of nonfunctionality in 46,XY individuals: *"absence of virilization and presence of müllerian structures"* — i.e., the gonads failed to make testosterone and AMH in fetal life and will not do better later.
- **Functional dysgenetic gonads may be retained:** *"If located in the inguinal canal with evidence of testicular function, placement in the scrotum may be considered, though this gonad will need to undergo surveillance for gonadoblastoma. There are no current guidelines on surveillance; one option would be yearly ultrasound."*

**Note the explicit guideline gap:** *"There are no current guidelines on surveillance."* Curate this as a `discussions` entry with `kind: KNOWLEDGE_GAP` — the absence of an evidence-based surveillance protocol for retained dysgenetic gonads is a real, named deficiency in the field, and the I-DSD authors reach the same conclusion (*"gonadal tumor risk requires further investigation"*).

**Germ cell tumour treatment** (if malignancy develops): gonadectomy ± platinum-based chemotherapy (BEP: bleomycin/etoposide/cisplatin) — NCIT:C15632 Chemotherapy; and/or radiotherapy for seminoma/dysgerminoma (NCIT:C15313 Radiation Therapy). Cure rates are high.

### 12.4 Supportive, rehabilitative, and counselling

| Intervention | NCIT (verified) |
|---|---|
| **Psychosocial care / mental health support** | **NCIT:C126880 Psychosocial Care**; NCIT:C15514 Psychosocial Assessment and Care |
| **Genetic counselling** | **NCIT:C15240 Genetic Counseling** |
| **Genetic testing** | **NCIT:C15709 Genetic Testing** |
| Peer/family support, DSD support groups | NCIT:C15747 Supportive Care |
| Transition to adult multidisciplinary care | NCIT:C15747 Supportive Care |
| Fertility counselling / gamete or gonadal tissue considerations | NCIT:C15240 / NCIT:C15747 |

`therapeutic_modality: BEHAVIORAL` for psychosocial and counselling interventions.

GeneReviews on psychosocial care: *"Open communication with affected individuals and families, including their active participation in the decision-making process, is critical."* Providers must address concerns *"respectfully and in strict confidence,"* recognizing that *"assigned sex of rearing may not be congruent with gender identity, which is determined by the individual over time."*

### 12.5 Advanced therapeutics

- **Gene therapy, gene editing, cell therapy, RNA therapies, targeted therapy, immunotherapy: none exist, none in trial.** The therapeutic window (fetal weeks 6–8) closes before any current intervention could be delivered, making this a genuinely intractable target for molecular therapy as currently conceived.
- **In vitro gametogenesis (IVG)** from patient iPSCs is the only plausible future fertility route; entirely preclinical.

### 12.6 Pharmacogenomics

No PharmGKB/CPIC guideline applies to 46,XY PGD. Standard testosterone/estradiol pharmacogenomics (CYP3A4/CYP19A1 variation) is not disease-specific and should not be curated here.

### 12.7 Clinical trials

**No interventional trial specific to 46,XY partial gonadal dysgenesis** is registered on ClinicalTrials.gov (searched as of this report). The relevant registered activity is **observational**: the **I-DSD/I-CAH Registry** (the source of PMID:40208111) and **dsd-LIFE** (the source of PMID:32905884). If the KB entry includes a `clinical_trials` block, it should record the registry studies (verify current NCT identifiers before curating; several I-DSD outputs are registry-based rather than NCT-registered) rather than fabricating an interventional trial.

### 12.8 Treatment outcomes and adverse events

- **Spontaneous puberty in PGDm: 80% onset, 59.3% reach Tanner G5 without treatment** — the strongest argument for gonadal retention in well-virilized male-assigned patients.
- **Feminizing therapy after gonadectomy in PGDf works**: in the NR5A1 case, *"Following bilateral orchiectomy and feminizing hormone therapy, hirsutism and clitoromegaly regressed"* (PMID:38206718).
- **Gonadectomy adverse effects:** immediate surgical iatrogenic hypogonadism, lifelong hormone dependence, loss of any residual fertility, and — importantly — **irreversibility of a decision often made before the patient can consent**.
- **Hypospadias repair:** high reoperation rate; fistula and stricture are common.
- **Testosterone:** erythrocytosis, acne, mood effects, accelerated bone-age advancement if over-dosed pre-pubertally.
- **Estrogen:** VTE risk; endometrial hyperplasia if unopposed with a uterus present.

### 12.9 Treatment algorithm (synthesis)

```
Newborn with atypical genitalia
  → Urgent multidisciplinary DSD team referral (before discharge); DO NOT assign sex prematurely
  → Karyotype + FISH SRY + CMA;  exclude CAH (17-OHP, electrolytes)
  → 46,XY non-mosaic + ambiguous genitalia + Müllerian structures + ↑FSH/LH, ↓AMH/inhibin B
       → suspect 46,XY PGD
  → Imaging (US ± MRI): uterus? gonadal position?
  → hCG stimulation (if outside mini-puberty) → Leydig reserve
  → DSD panel → WES → WGS/CMA   (42% yield)
  → Sex-of-rearing discussion: diagnosis + EGS + imaging + parental values + explicit
       counselling that 16.1% of PGDf and 5.3% of PGDm are later reassigned
  ├── Male assignment → assess each gonad:
  │      functional + inguinal/scrotal-placeable → ORCHIOPEXY + lifelong surveillance
  │      nonfunctional / intra-abdominal / streak → GONADECTOMY
  │      → observe for spontaneous puberty (80%); supplement testosterone if needed
  │      → hypospadias repair timing = shared decision, consider deferral
  └── Female assignment → gonads are the key decision:
         retain → permits spontaneous puberty BUT 42.3% virilize AND 19.7% pre-/malignancy
         remove → prevents both, mandates lifelong estrogen ± progesterone
         → vaginal dilation before/instead of vaginoplasty; defer clitoroplasty
  → Both: bone health monitoring (DXA), psychosocial care throughout,
          fertility counselling, structured transition to adult care,
          cascade evaluation of at-risk siblings (esp. phenotypically female sibs)
  → Gene-specific add-ons:
       NR5A1 → adrenal function testing; POI counselling for 46,XX relatives
       DHH   → neurological surveillance from age ~20
       WT1   → renal function + Wilms tumour surveillance (reclassify as syndromic)
       MAP3K1→ near-complete penetrance: 50% recurrence counselling; test female sibs
```

---

## 13. Prevention

### 13.1 Primary prevention

**Not possible.** 46,XY PGD results from a germline variant acting in a fetal developmental window. There is no modifiable exposure, no vaccine, no risk-factor modification. Record explicitly as *not applicable* rather than leaving the field empty.

The only theoretical primary-prevention levers are **reproductive**: preimplantation genetic testing for monogenic disease (PGT-M) or prenatal diagnosis in a family with a known pathogenic variant. Both are:
- Available in principle for any of the identified genes,
- Ethically contested for this indication in particular — 46,XY PGD is compatible with a normal lifespan and good quality of life, and DSD advocacy communities have argued strongly against framing it as a condition to be prevented. Curate this with the ethical caveat explicit.

### 13.2 Secondary prevention (early detection)

This is where the real prevention opportunity lies:
1. **Newborn genital examination** → same-admission DSD team referral. The single most effective secondary-prevention action.
2. **Cascade evaluation of siblings**, especially **phenotypically female siblings** of a proband with an AD variant — *"Identification of a MAP3K1 variant should prompt an evaluation for DSD in female siblings of the proband"* (PMID:28504475). This can identify an unrecognised 46,XY CGD/PGD patient carrying a 20–34% gonadal neoplasia risk.
3. **Closing the adolescent diagnostic gap.** Median age at diagnosis for female-presenting 46,XY gonadal dysgenesis is **17.0 years** (PMID:27603905). Karyotyping every adolescent with primary amenorrhoea and absent/discordant pubertal development would substantially shorten this.
4. **Investigating unexplained pubertal virilization** in a girl — 42.3% of PGDf with retained gonads virilize; this is a red flag, not a benign PCOS variant.

### 13.3 Tertiary prevention (preventing complications in diagnosed patients)

| Complication | Preventive action |
|---|---|
| **Gonadoblastoma / germ cell tumour** | Gonadectomy of nonfunctional/streak gonads; scrotal placement + surveillance for retained functional gonads (annual ultrasound is one suggested option — **but note the acknowledged absence of guidelines**) |
| **Osteoporosis (HP:0000939)** | Timely, adequate, uninterrupted sex-steroid replacement; DXA monitoring; calcium/vitamin D; weight-bearing exercise |
| **Endometrial hyperplasia** | Add progestogen to estrogen when a uterus is present |
| **Psychological distress / gender dysphoria** | Embedded psychology from diagnosis; deferring irreversible surgery; honest age-appropriate disclosure |
| **Unwanted pubertal virilization (PGDf)** | Anticipatory counselling; pre-pubertal decision on gonadal retention; GnRH analogue or gonadectomy if it occurs |
| **DHH-related neuropathy** | Neurological surveillance from ~age 20 in confirmed DHH biallelic cases |
| **Loss to follow-up at transition** | Structured paediatric→adult transition; adult multidisciplinary DSD clinic |

### 13.4 Immunization, behavioural, public health, prophylaxis

- **Immunization:** not applicable (routine schedule only).
- **Behavioural interventions:** no risk-reducing behaviour exists. Post-diagnosis lifestyle advice targets bone health only.
- **Public health / environmental interventions:** not applicable to 46,XY PGD. (EDC reduction policy relates to TDS, a different entity — see §2.3.)
- **Prophylaxis:** **prophylactic gonadectomy** (NCIT:C94458 Prophylactic Surgery + NCIT:C15288 Orchiectomy) is the only prophylactic procedure, and its indication is narrower than historically taught — restricted to nonfunctional/streak/non-surveillable gonads, and increasingly deferred with the patient's participation where the gonad is functional and accessible.

### 13.5 Genetic counselling

Essential and specific. Content per §9.2: mode of inheritance by gene; sex-limited expression (a 46,XX daughter carrying the same MAP3K1 allele is unaffected but a 50% transmitter); the 42% chance that no genetic cause will be found; germline mosaicism and the ~1% recurrence risk after an apparently de novo variant; NR5A1's variable expressivity and **primary ovarian insufficiency risk in 46,XX relatives**; DHH recessive risk in consanguineous families; and reproductive options (PGT-M, prenatal diagnosis, donor gametes, adoption) presented non-directively.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and natural disease

XY disorders of sex development occur naturally across mammals. Per OMIA and the veterinary literature, *"in domestic animals, sex reversal disorders have been described in pig, goat, sheep, roe deer, llama, cattle, buffaloes, horse, cat, dog and ferret."*

| Species | NCBI Taxon | OMIA entry | Notes |
|---|---|---|---|
| **Domestic horse** | NCBITaxon:9796 | **OMIA:001601-9796** — XY difference of sexual development, generic; **OMIA:001230-9796** — XY sex reversal, SRY-related | *"In horses, the most common type is 64XY SRY negative."* In at least one XY mare, *"the DNA-binding domain of the SRY gene was deleted from the Y chromosome."* Clinically important in breeding (the "XY mare" presenting with infertility/abnormal genitalia) |
| **Domestic dog** | NCBITaxon:9615 | OMIA XX/XY DSD entries | The best-studied veterinary DSD; **most published canine work is XX SRY-negative** (SOX9 duplications on CFA9 — PMC4091935/PLOS ONE 2014), which is the *converse* of human 46,XY PGD |
| **Domestic pig** | NCBITaxon:9823 | OMIA XX DSD | SRY-negative XX DSD with ovotestis documented (PMC11945758) |
| **Goat** | NCBITaxon:9925 | OMIA polled intersex (PIS) | **FOXL2 regulatory deletion** — XX sex reversal; a landmark natural model of the pro-ovary arm |
| Cattle, sheep, cat, llama, ferret, roe deer | various | OMIA | Sporadic reports |

**Honest assessment for this KB:** the veterinary literature is dominated by **XX** (SRY-negative) sex reversal, not by XY partial gonadal dysgenesis. Equine XY DSD (OMIA:001601, OMIA:001230) is the closest natural counterpart. There is **no reported naturally occurring animal disorder with a confirmed NR5A1, MAP3K1, or DHX37 lesion producing partial gonadal dysgenesis**. Curate the veterinary section as "related conditions in other species," not as "the same disease in animals."

### 14.2 Orthologous genes

| Human gene | Mouse ortholog | Notes |
|---|---|---|
| SRY | *Sry* | Y-linked in both; **poorly conserved in sequence** (only the HMG box) — a major comparative caveat |
| NR5A1 | *Nr5a1* (Sf1, Ftz-F1) | Highly conserved |
| MAP3K1 | *Map3k1* (Mekk1) | Highly conserved |
| DHX37 | *Dhx37* | Highly conserved (ribosome biogenesis is deeply conserved) |
| SOX9 | *Sox9* | Highly conserved, incl. enhancer architecture (TESCO/Enh13) |
| DHH | *Dhh* | Highly conserved |
| DMRT1 | *Dmrt1* | **DM-domain conserved from Drosophila (dsx) to vertebrates** — the deepest-conserved sex-determination gene |
| WT1, GATA4, ZFPM2, FOXL2, WNT4, RSPO1 | *Wt1, Gata4, Zfpm2, Foxl2, Wnt4, Rspo1* | Conserved |

*(Obtain exact NCBI Gene IDs from NCBI Gene / Alliance of Genome Resources before curating.)*

### 14.3 Comparative biology and evolutionary conservation

The **downstream** testis-determination network (SOX9/FGF9/PTGDS vs WNT4/RSPO1/FOXL2 antagonism; DMRT1) is **deeply conserved across vertebrates**, which is why mouse, and to a lesser extent zebrafish and medaka, are informative. The **upstream trigger is not**: SRY is eutherian-specific and rapidly evolving; birds use ZZ/ZW with DMRT1 dosage; many fish and reptiles use temperature or other master switches. Zebrafish lack a fixed sex-determining locus in domesticated strains and lack SRY entirely.

**Practical consequence:** models are strong for the *conserved core* (SOX9 threshold, Wnt/β-catenin antagonism, Sertoli fate) and weak for the *human-specific trigger layer*.

### 14.4 Transmission

**No zoonotic potential; no cross-species transmission.** Not an infectious or transmissible condition.

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*, NCBITaxon:10090) — the primary model

| Model | Phenotype | Fidelity to human PGD |
|---|---|---|
| ***Nr5a1* (Sf1) null** | *"Nr5a1-deficient mice lack both gonads and adrenal glands"*; *"Homozygous Nr5a1 knockout mice lack the adrenal gland and gonad and die within 8 days after birth"* | **Poor** — far more severe than human heterozygous PGD; models complete agenesis, not partial dysgenesis. Human disease is heterozygous; mouse *Nr5a1*<sup>+/−</sup> is only mildly affected |
| ***Nr5a1* conditional (Sox9-Cre)** | *"compromises testis differentiation"* (PMC7904858) | **Good for the Sertoli-specific arm** — dissects post-determination requirement |
| ***Nr5a1* post-determination deletion** | *"Steroidogenic Factor 1 (Nr5a1) is Required for Sertoli Cell Survival Post Sex Determination"* (Sci Rep 2019, PMC6418149) | **Good** — establishes a distinct maintenance role, relevant to progressive dysgenesis/regression |
| ***Nr5a1* p.R92W knock-in** | Does **not** produce XX testicular development in mice, unlike humans (PMC5101639) | **Explicit human/model mismatch** — curate as `HUMAN_MODEL_MISMATCH` |
| ***Map3k1* (Mekk1)** | *"Mouse studies demonstrated that Map3k1 expression occurs in embryonic gonads during the critical sex-determination period"* (PMID:21129722). *Map3k1* **loss**-of-function mice have eyelid-closure and (in the *goya* mutant) cochlear hair-cell phenotypes — **not** gonadal dysgenesis | **Poor for the null; the human disease is gain-of-function.** A knock-in of a human GoF allele is the correct model and, to my knowledge, has not been reported as a fully characterised gonadal model |
| ***Dhx37*** | Discovery paper confirmed *"DHX37 expression… in developing testis somatic cells"* (PMID:31337883); a mouse model was part of the study design (Warr/Greenfield co-authorship) | **Under-developed** — no established mouse recapitulating human DHX37 PGD |
| ***Sry* transgenics; B6.Y<sup>TIR</sup> / B6.Y<sup>POS</sup> strains** | Strain-dependent XY sex reversal from *"Inefficient Sox9 upregulation and absence of Rspo1 repression"* (PMC11094394) | **Excellent conceptual model of PGD** — these strains produce **ovotestes and partial dysgenesis** on a permissive genetic background, directly modelling the threshold/bistability biology and the role of genetic modifiers |
| ***Sox9* / *Sox8* conditional** | *"Sox9 and Sox8 protect the adult testis from male-to-female genetic reprogramming and complete degeneration"* (eLife 2016) | **Good** for maintenance biology |
| ***Wnt4* / *Sox9* double** | *"Mouse Gonad Development in the Absence of the Pro-Ovary Factor WNT4 and the Pro-Testis Factor SOX9"* (PMC7291083) | **Excellent** for the antagonism model |
| ***Rspo1*, *Foxl2*, *Fgf9*, *Dhh*, *Dmrt1*, *Wt1*, *Gata4/Zfpm2* knockouts** | Each dissects one arm | **Good**, mechanism-specific |

**MGI is the canonical resource** (informatics.jax.org); IMPC/KOMP hold null alleles for most of these genes; IMSR/EMMA/MMRRC for strain distribution.

### 15.2 Other model systems

- **Zebrafish (*Danio rerio*, NCBITaxon:7955; ZFIN).** *"Zebrafish may be a good complementary model to study gene functions when homozygous lethality occurs in knockout mice"* — directly relevant given the *Nr5a1*-null lethality. **Major limitation:** zebrafish lack SRY and a fixed sex-determining locus; sex determination is polygenic/environmental in domesticated strains. Useful for downstream conserved factors (*dmrt1*, *sox9a/b*, *wnt4*, *foxl2*, *amh*), **not** for testis determination *per se*.
- **Medaka (*Oryzias latipes*).** Has *dmy/gsdfY*, a genuine master male-determining gene — the best non-mammalian model of a *bona fide* Y-linked switch.
- **Cell lines (Cellosaurus):** **NT2/D1** (human testicular embryonal carcinoma — the workhorse for testis-determination reporter and ChIP assays), **KGN** (human granulosa — the ovarian counterpart), **HEK-293T** (reporter/co-IP), **TM3/TM4** (mouse Leydig/Sertoli), **Y-1** (adrenocortical). All three of the first cell lines were used in the definitive MAP3K1 mechanistic study (PMC8927045). Evidence from these is `IN_VITRO`.
- **iPSC and organoid systems:** human iPSC-derived gonadal/Sertoli-like and fetal-Leydig-like differentiation protocols exist but are immature; **testicular organoids** and human fetal gonad **xenografts** (PMC3440087) are the emerging platforms. No patient-derived iPSC model of 46,XY PGD has been published — a clear gap and an obvious MorPhiC-style target (NR5A1, SOX9, DHX37 null alleles in iPSC-derived gonadal somatic cells would be directly informative for this entry).
- **Induced/pharmacological models:** in-utero anti-androgen (flutamide) and phthalate (DEHP/DBP) rat models produce a *TDS-like* phenotype (hypospadias, cryptorchidism, multinucleated germ cells, suppressed fetal-testis steroidogenesis) — a model of the **downstream androgen-deficiency arm**, not of the determination defect. Do not conflate.

### 15.3 Phenotype recapitulation and limitations — summary judgment

**What models capture well:**
- The bistable SOX9-vs-WNT4/β-catenin switch and its dosage sensitivity (B6.Y<sup>TIR</sup>/Y<sup>POS</sup> strains; *Wnt4*/*Sox9* doubles).
- Cell-autonomous Sertoli and Leydig requirements (conditional *Nr5a1*, *Sox9/Sox8*).
- Post-determination maintenance and regression biology (*Nr5a1* post-determination deletion; *Sox9/Sox8* adult conditional).
- Biochemical consequences of specific human variants (NT2/D1, KGN, HEK-293T assays).

**What models fail to capture (curate these as `HUMAN_MODEL_MISMATCH`):**
1. **The heterozygous human phenotype.** Human PGD is overwhelmingly a heterozygous, dosage-threshold disease; mouse heterozygotes are usually normal and mouse homozygotes are usually far too severe (agenesis/lethality).
2. **The NR5A1 p.R92W species divergence** — explicitly documented (PMC5101639).
3. **The MAP3K1 gain-of-function mechanism** — mouse *Map3k1* nulls do not have gonadal dysgenesis; the human disease direction of effect is the opposite of what the knockout tests.
4. **SRY sequence divergence** — mouse *Sry* differs so substantially outside the HMG box that human SRY variant modelling is unreliable.
5. **The partial/asymmetric gonadal phenotype itself** — the defining PGD feature (dysgenetic testis on one side, streak on the other) is strain-background- and stochasticity-dependent in mice and is not reliably reproducible.
6. **No model exists for DHX37**, the newest major gene.

### 15.4 Research applications

Determination-window timing and dosage thresholds; Sertoli/Leydig lineage specification; the antagonistic-network topology; variant functional classification (the practical near-term use — resolving VUS in NR5A1/MAP3K1/DHX37); germ cell neoplasia initiation in a dysgenetic niche (poorly modelled — **mice do not develop gonadoblastoma**, a major gap given that neoplasia is the chief clinical risk); hormone-replacement and bone outcomes.

### 15.5 Resources

MGI (informatics.jax.org), IMPC, KOMP/EuMMCR, IMSR, EMMA, MMRRC, ZFIN, RGD, Alliance of Genome Resources, OMIA (omia.org), Cellosaurus, Human Cell Atlas / CELLxGENE (human fetal gonad reference atlases).

---

## Appendix A — Consolidated ontology term suggestions

All HPO, GO, CL, UBERON, CHEBI, and NCIT identifiers below were **verified against the local OAK adapters** (`sqlite:obo:hp`, `sqlite:obo:go`, `sqlite:obo:cl`, `sqlite:obo:uberon`, `sqlite:obo:chebi`, `sqlite:obo:ncit`) in this session, with the exceptions explicitly flagged as unverified. Labels shown are the canonical ontology labels — use them verbatim in `term.label`.

**Disease:** `MONDO:0016674` — 46,XY partial gonadal dysgenesis

**Core phenotypes (HP):** 0000062 Ambiguous genitalia · 0000133 Gonadal dysgenesis · 0012244 Abnormal sex determination · 0000047 Hypospadias · 0000054 Micropenis · 0008736 Hypoplasia of penis · 0008734 Decreased testicular size · 0000028 Cryptorchidism · 0000812 Abnormal internal genitalia · 0008665 Clitoral hypertrophy · 0010464 Streak ovary · 0008730 Female external genitalia in individual with 46,XY karyotype · 0000058 Abnormal labia morphology · 0000045 Abnormal scrotum morphology · 0100779 Urogenital sinus anomaly · 0000142 Abnormal vagina morphology · 0008726 Hypoplasia of the vagina · 0012870 Vanishing testis

**Endocrine/lab (HP):** 0000815 Hypergonadotropic hypogonadism · 0000837 Increased circulating gonadotropin level · 0008232 Elevated circulating follicle stimulating hormone level · 0011969 Elevated circulating luteinizing hormone level · 0040171 Decreased serum testosterone concentration · 0008214 Decreased serum estradiol · 0031103 Decreased circulating antimullerian hormone circulation · 0031100 Decreased circulating inhibin B concentration · 0008193 Primary gonadal insufficiency · 0000823 Delayed puberty · 0008187 Absence of secondary sex characteristics · 0000846 Adrenal insufficiency *(NR5A1 subgroup)*

**Reproductive outcome (HP):** 0000027 Azoospermia · 0003251 Male infertility · 0000144 Decreased fertility · 0000786 Primary amenorrhea

**Neoplasia (HP):** 0000150 Gonadoblastoma · 0000030 Testicular gonadoblastoma · 0000149 Ovarian gonadoblastoma

**Secondary/other (HP):** 0000771 Gynecomastia · 0000939 Osteoporosis · 0002225 Sparse pubic hair · 0002215 Sparse axillary hair · 0002750 Delayed skeletal maturation · 0002667 Nephroblastoma *(WT1)* · 0000100 Nephrotic syndrome *(WT1)*

**Inheritance (HP) — verify these five with OAK before use:** 0000006 AD · 0000007 AR · 0001417 X-linked · 0001450 Y-linked · 0010984 Digenic

**Biological processes (GO):** 0007530 sex determination · 0030238 male sex determination · 0008584 male gonad development · 0008406 gonad development · 0060008 Sertoli cell differentiation · 0060011 Sertoli cell proliferation · 0046661 male sex differentiation · 0008585 female gonad development *(`modifier: INCREASED` — inappropriate de-repression)* · 0016055 Wnt signaling pathway · 0060070 canonical Wnt signaling pathway *(INCREASED in MAP3K1)* · 0000165 MAPK cascade *(INCREASED in MAP3K1)* · 0035556 intracellular signal transduction · 0042254 ribosome biogenesis *(DECREASED in DHX37)* · 0006357 regulation of transcription by RNA polymerase II · 0030325 adrenal gland development *(NR5A1)*

**Cell types (CL):** 0000216 Sertoli cell · 0000178 Leydig cell · 0000586 germ cell · 0000015 male germ cell · 0000670 primordial germ cell · 0000501 granulosa cell · 0002481 peritubular myoid cell · 0000019 sperm

**Anatomy (UBERON):** 0000991 gonad · 0000473 testis · 0000992 ovary · 0003890 Mullerian duct · 0003074 mesonephric duct · 0000995 uterus · 0000996 vagina · 0005876 undifferentiated genital tubercle · 0001301 epididymis · 0002367 prostate gland · 0004175 internal genitalia · 0000079 male reproductive system · 0002369 adrenal gland *(NR5A1)*

**Chemicals (CHEBI):** 17347 testosterone · 16469 17beta-estradiol · 16330 17beta-hydroxy-5alpha-androstan-3-one *(DHT)*

**Treatments (NCIT):** C15288 Orchiectomy · C94458 Prophylactic Surgery · C111066 Orchiopexy · C15599 Hormone Replacement Therapy · C15986 Pharmacotherapy · C15329 Surgical Procedure · C126880 Psychosocial Care · C15514 Psychosocial Assessment and Care · C15240 Genetic Counseling · C15709 Genetic Testing · C15747 Supportive Care · C1247 Testosterone Enanthate · C1246 Testosterone Cypionate · C1249 Testosterone Undecanoate · C15632 Chemotherapy *(germ cell tumour)* · C15313 Radiation Therapy *(dysgerminoma/seminoma)*

**Genes (HGNC, lowercase prefix per repo convention):** hgnc:11311 SRY · hgnc:7983 NR5A1 · hgnc:6848 MAP3K1 · hgnc:17210 DHX37 · hgnc:2865 DHH · hgnc:11204 SOX9 · hgnc:11203 SOX8 · hgnc:2934 DMRT1 · hgnc:12796 WT1 · hgnc:7960 NR0B1 · hgnc:16700 ZFPM2 · hgnc:4173 GATA4 · hgnc:9306 PPP2R3C · hgnc:18021 HHAT — *verify each HGNC numeric ID with `just validate-terms` before committing.*

---

## Appendix B — Curation guidance specific to this KB

1. **Module conformance.** No existing `kb/modules/` module fits this disease well. Candidate anchors: none of the cancer hallmark, fibrosis, senescence, lysosomal, or metabolic-intoxication modules apply. The gonadal-neoplasia arm has partial affinity to `genome_instability_mutation` but the mechanism (TSPY-driven transformation of an arrested germ cell in a dysgenetic niche) is distinct. **Do NOT force `conforms_to: fibrotic_response`** for peritubular fibrosis — it is developmental matrix abnormality, not injury-driven fibrosis. If a module is warranted, the right one to *create* would be a conserved **"bipotential-fate-switch failure"** module capturing the SOX9-threshold/Wnt-antagonism logic, which would also serve 46,XX testicular/ovotesticular DSD and 46,XY CGD.

2. **Grouping candidacy.** 46,XY PGD is a natural member of a **"46,XY Disorders of Testicular Development"** grouping alongside 46,XY CGD, TRS, MGD, and ovotesticular DSD (`grouping_basis: SHARED_MECHANISM`, `NECESSARY` criteria: `HAS_INHERITANCE`/karyotype + `HAS_PHENOTYPE HP:0000133`). It is also a member of `Digenic_and_Oligogenic_Disorders` on the strength of the DHX37+NR5A1 double-heterozygotes.

3. **Subtypes.** Model gene-defined subtypes (`NR5A1-related`, `MAP3K1-related`, `DHX37-related`, `SRY-related`, `DHH-related`) with short slug-friendly names. The DHH subtype carries the distinctive adult neuropathy; the NR5A1 subtype carries adrenal insufficiency and 46,XX POI in relatives; the WT1 route should be excluded as syndromic.

4. **`biological_scale` tags:** gene lesion → `MOLECULAR`; SOX9-threshold/Sertoli fate failure → `CELLULAR`; dysgenetic gonad → `TISSUE`; Müllerian retention, undervirilization, hypergonadotropic hypogonadism → `ORGANISM`.

5. **Frequency discipline.** Use the I-DSD 2025 numbers (PMID:40208111) as the only source of `frequency:` values. Omit `frequency:` for the Orphanet editorial bands.

6. **Evidence-source tagging.** Registry/cohort/case series → `HUMAN_CLINICAL`. NT2/D1, KGN, HEK-293T variant-function assays → `IN_VITRO`. Mouse/rat/zebrafish → `MODEL_ORGANISM`. Structural/docking predictions of MAP3K1 folding → `COMPUTATIONAL`. Guideline consensus statements without primary data → `OTHER`.

7. **Three `discussions` entries are warranted:**
   - `KNOWLEDGE_GAP`: *"There are no current guidelines on surveillance"* for retained functional dysgenetic gonads (GeneReviews, corroborated by PMID:40208111).
   - `KNOWLEDGE_GAP`: 42–58% of cases remain genetically unexplained after exome sequencing.
   - `HUMAN_MODEL_MISMATCH`: NR5A1 p.R92W produces XX testicular development in humans but not mice (PMC5101639); and separately, mouse *Map3k1* nulls do not model the human gain-of-function disease.

8. **Before committing any evidence item, run the full stack:** `just fetch-reference PMID:<id>` for every PMID cited here (I have not populated `references_cache/`), then `just validate`, `just validate-references`, `just validate-terms`. Several snippets in this report are paraphrases produced by page-summarisation and **must be replaced with exact abstract substrings** verified against the cached file. The verbatim-quoted passages (marked with `>` blockquotes and explicit "verbatim" labels) are the safest starting points but still require substring verification.

---

## Sources

**Primary literature (PMID-cited)**
- [Elzaiat M, McElreavey K, Bashamboo A. Genetics of 46,XY gonadal dysgenesis. Best Pract Res Clin Endocrinol Metab 2022;36(1):101633. PMID:35249806](https://pubmed.ncbi.nlm.nih.gov/35249806/)
- [Tadokoro-Cuccaro R, et al. Phenotypic Variation and Pubertal Outcomes in Males and Females With 46,XY Partial Gonadal Dysgenesis. J Clin Endocrinol Metab 2025. PMID:40208111](https://pubmed.ncbi.nlm.nih.gov/40208111/)
- [McElreavey K, et al. Pathogenic variants in the DEAH-box RNA helicase DHX37… Genet Med 2020;22(1):150-159. PMID:31337883](https://pubmed.ncbi.nlm.nih.gov/31337883/)
- [Ostrer H. Pathogenic Variants in MAP3K1 Cause 46,XY Gonadal Dysgenesis: A Review. Sex Dev 2022. PMID:35290982](https://pubmed.ncbi.nlm.nih.gov/35290982/)
- [Pearlman A, et al. Mutations in MAP3K1 cause 46,XY disorders of sex development… Am J Hum Genet 2010;87(6):898-904. PMID:21129722](https://pubmed.ncbi.nlm.nih.gov/21129722/)
- [Granados A, et al. MAP3K1-related gonadal dysgenesis: Six new cases and review of the literature. Am J Med Genet C 2017. PMID:28504475](https://pubmed.ncbi.nlm.nih.gov/28504475/)
- [Slowikowska-Hilczer J, et al. Risk of gonadal neoplasia in patients with disorders/differences of sex development. Cancer Epidemiol 2020;69:101800. PMID:32905884](https://www.sciencedirect.com/science/article/abs/pii/S187778212030134X)
- [Berglund A, et al. Incidence, Prevalence, Diagnostic Delay, and Clinical Presentation of Female 46,XY Disorders of Sex Development. J Clin Endocrinol Metab 2016;101(12):4532-4540. PMID:27603905](https://pubmed.ncbi.nlm.nih.gov/27603905/)
- [Hughes IA, Houk C, Ahmed SF, Lee PA. Consensus statement on management of intersex disorders. Arch Dis Child 2006;91(7):554-63. PMID:16624884](https://pubmed.ncbi.nlm.nih.gov/16624884/)
- [Lee PA, et al. Global Disorders of Sex Development Update since 2006. Horm Res Paediatr 2016. PMID:26820577](https://pubmed.ncbi.nlm.nih.gov/26820577/)
- [Long-Term Follow-Up of Patients with 46,XY Partial Gonadal Dysgenesis Reared as Males. Int J Endocrinol 2014. PMID:25580123](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4279723/)
- [NR5A1-related 46,XY partial gonadal dysgenesis: A case report and literature review. PMID:38206718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10754607/)
- [DHX37 and NR5A1 Variants Identified in Patients with 46,XY Partial Gonadal Dysgenesis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10222664/)
- [MAP3K1 Variant Causes Hyperactivation of Wnt4/β-Catenin/FOXL2 Signaling…](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8927045/)
- [Screening of Y chromosome microdeletions in 46,XY partial gonadal dysgenesis…](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3827999/)
- [Idris et al. Genomic technologies and the diagnosis of 46,XY differences of sex development. Andrology 2025. PMID:39081229](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12183017/)
- [Worldwide cohort study of 46,XY DSD genetic diagnoses. Front Genet 2024. DOI:10.3389/fgene.2024.1387598](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1387598/full)
- [Two Novel Heterozygous Variants in RecA2 Domain of DHX37… PMID:37717579](https://pubmed.ncbi.nlm.nih.gov/37717579/)
- [46,XY Gonadal Dysgenesis due to a Homozygous Mutation in Desert Hedgehog (DHH)… PMID:25927242](https://pubmed.ncbi.nlm.nih.gov/25927242/)
- [Skakkebaek NE, et al. Testicular dysgenesis syndrome: possible role of endocrine disrupters. PMID:16522521](https://pubmed.ncbi.nlm.nih.gov/16522521/)
- [Is testicular dysgenesis syndrome a genetic, endocrine, or environmental disease…? PMID:29183799](https://pubmed.ncbi.nlm.nih.gov/29183799/)
- [The p.R92W variant of NR5A1/Nr5a1 induces testicular development of 46,XX gonads in humans, but not in mice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5101639/)
- [Steroidogenic Factor 1 (Nr5a1) is Required for Sertoli Cell Survival Post Sex Determination](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6418149/)
- [The conditional deletion of Nr5a1 in Sox9-Cre mice compromises testis differentiation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7904858/)
- [Unveiling the roles of Sertoli cells lineage differentiation in reproductive development and disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC11063913/)
- [Inefficient Sox9 upregulation and absence of Rspo1 repression lead to sex reversal in the B6.XYTIR mouse gonad](https://pmc.ncbi.nlm.nih.gov/articles/PMC11094394/)
- [A 46,XY female DSD patient with bilateral gonadoblastoma, a novel SRY missense mutation combined with a WT1 KTS splice-site mutation. PMID:22815844](https://pubmed.ncbi.nlm.nih.gov/22815844/)

**Databases and reference resources**
- [GeneReviews: Nonsyndromic Disorders of Testicular Development Overview (NBK1547)](https://www.ncbi.nlm.nih.gov/books/NBK1547/)
- [MONDO:0016674 — Monarch Initiative](https://monarchinitiative.org/MONDO:0016674)
- [Orphanet: 46,XY partial gonadal dysgenesis (ORPHA:251510)](https://www.orpha.net/en/disease/detail/251510)
- [GARD: 46,XY partial gonadal dysgenesis](https://rarediseases.info.nih.gov/diseases/17211/46xy-partial-gonadal-dysgenesis)
- [HPO annotations — ontology.jax.org](https://ontology.jax.org/api/network/annotation/ORPHA:251510)
- [OMIM 400044 (SRXY1)](https://omim.org/entry/400044) · [612965 (SRXY3/NR5A1)](https://www.omim.org/entry/612965) · [613762 (SRXY6/MAP3K1)](https://omim.org/entry/613762) · [233420 (SRXY7/DHH)](https://omim.org/entry/233420) · [273250 (SRXY11/DHX37)](https://omim.org/entry/273250) · [607080 (GDMN)](https://www.omim.org/entry/607080)
- [OMIA:001601-9796 — XY difference of sexual development, horse](https://omia.org/OMIA001601/9796/) · [OMIA:001230-9796 — XY sex reversal, SRY-related, horse](https://omia.org/OMIA001230/9796/)
- [ESPU–SPU Consensus statement 2020: Management of Differences of Sex Development](https://www.espu.org/members/documents/espu-spu-consensus-statement-2020-management-of-differences-of-sex-development-dsd/)
- [Sox9 Duplications Are a Relevant Cause of Sry-Negative XX Sex Reversal Dogs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4091935/)
- [Human Fetal Testis Xenografts Are Resistant to Phthalate-Induced Endocrine Disruption](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3440087/)