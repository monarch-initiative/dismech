---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-27T22:35:06.502285'
end_time: '2026-07-27T22:49:03.202100'
duration_seconds: 836.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mabry Syndrome
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
  web_search_requests: 15
  num_turns: 58
  total_cost_usd: 4.891132999999999
  session_id: 1c7dc8a2-35d3-4864-a01a-4c89592a6e23
  stop_reason: end_turn
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mabry Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mabry Syndrome** covering all of the
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

sup Harry — dug through this one properly. Here's the report.

---

# Mabry Syndrome (Hyperphosphatasia with Impaired Intellectual Development Syndrome, HPMRS)
### A comprehensive research report for dismech curation
**Compiled 2026-07-27 · evidence types flagged per claim**

---

## 0. Executive framing (read this before curating)

Mabry syndrome is one of those diseases where the *name* and the *entity* have drifted apart, and you have to pick a lane before you write a single YAML line.

- **"Mabry syndrome"** is the eponym for the clinical triad first described in 1970: elevated tissue-nonspecific alkaline phosphatase + seizures + profound developmental disability. In MONDO that eponym is an **exact synonym of the grouping term `MONDO:0016596` "hyperphosphatasia-intellectual disability syndrome"** (= `OMIMPS:239300`, `Orphanet:247262`), *not* of the PIGV-specific child term.
- **`MONDO:0009398`** — which the current stub file uses — is **HPMRS1 specifically, defined by PIGV**. MONDO's own definition: *"Any hyperphosphatasia-intellectual disability syndrome in which the cause of the disease is a mutation in the PIGV gene."*
- Six genetically distinct HPMRS subtypes exist (PIGV, PIGO, PGAP2, PGAP3, PIGW, PIGY), and they all sit inside a much larger family — **inherited GPI deficiencies (IGDs) / GPI biosynthesis defects (GPIBDs)** — spanning ~24 of ~31–33 pathway genes.

**Curation recommendation:** model the entry at the **grouping level (`MONDO:0016596`, "Mabry syndrome")** with `has_subtypes` for HPMRS1–6, since the eponym maps there. If you want a PIGV-only entry, rename the file/entry to match `MONDO:0009398`. Mixing them will cause a MONDO-label mismatch flag in review. (This is exactly the naming-precision trap from the NEC preflight guidance — the eponym and the gene-series term are not the same entity.)

---

## 1. Disease Information

### 1.1 Overview

Mabry syndrome / HPMRS is an **autosomal recessive, multisystem neurodevelopmental disorder caused by defective biosynthesis or remodeling of the glycosylphosphatidylinositol (GPI) anchor** — the little lipid grommet that tacks >150 different human proteins onto the outer face of the plasma membrane. When the grommet is built wrong, some of those proteins never make it to the surface, and one of them — tissue-nonspecific alkaline phosphatase — gets snipped loose and dumped into the blood. Hence the paradoxical signature: a *neurodevelopmental* disease whose calling card is a *bone enzyme* on a routine chemistry panel.

The cardinal triad, per the 2024 index-case review ([Genes 2024, PMC11121671](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11121671/), PMID:38790248):
1. **Hyperphosphatasia** (persistently elevated tissue-nonspecific alkaline phosphatase)
2. **Seizures**
3. **Developmental disability / intellectual disability**

with hypotonia, distinctive facial dysmorphism, and brachytelephalangy (short terminal phalanges) as the near-constant supporting cast.

### 1.2 Identifiers

| Resource | ID | Label |
|---|---|---|
| **MONDO (grouping — "Mabry syndrome")** | `MONDO:0016596` | hyperphosphatasia-intellectual disability syndrome |
| MONDO (HPMRS1, PIGV) | `MONDO:0009398` | hyperphosphatasia with intellectual disability syndrome 1 |
| MONDO (HPMRS2, PIGO) | `MONDO:0013882` | hyperphosphatasia with intellectual disability syndrome 2 |
| MONDO (HPMRS3, PGAP2) | `MONDO:0013628` | hyperphosphatasia with intellectual disability syndrome 3 |
| MONDO (HPMRS4, PGAP3) | `MONDO:0014318` | hyperphosphatasia with intellectual disability syndrome 4 |
| MONDO (HPMRS5, PIGW) | `MONDO:0014457` | hyperphosphatasia with intellectual disability syndrome 5 |
| MONDO (HPMRS6, PIGY) | `MONDO:0014780` | hyperphosphatasia with intellectual disability syndrome 6 |
| OMIM phenotype series | `OMIMPS:239300` | — |
| OMIM (HPMRS1–6) | 239300, 614749, 614207, 615716, 616025, 616809 | — |
| Orphanet | `ORPHA:247262` | Hyperphosphatasia-intellectual disability syndrome |
| DOID | `DOID:0070431` (grouping), `DOID:0070433` (HPMRS1) | — |
| UMLS | C1855923 (grouping), C4551502 (HPMRS1) | — |
| MedGen | 383800 (grouping), 1647044 (HPMRS1) | — |
| SNOMED CT | 33982008 | — |
| GARD | 0017188 / 0018349 | — |
| ICD-10 | **Q87.8** (per Orphanet) | Other specified congenital malformation syndromes |
| ICD-11 | No dedicated stem code identified; falls under congenital-malformation-syndrome / inborn-error-of-metabolism chapters — **flag as unverified** |
| MeSH | No dedicated descriptor; indexed via *Intellectual Disability* + *Alkaline Phosphatase/blood*. **Flag as unverified.** |

MONDO parentage for the grouping term (useful for `classifications`): `is_a` **developmental anomaly of metabolic origin** (`MONDO:0015327`), **syndromic dyslipidemia** (`MONDO:0015905`), **inborn disorder of glycosphingolipid and glycosylphosphatidylinositol anchor glycosylation** (`MONDO:0017748`), **congenital limb malformation** (`MONDO:0019054`).

### 1.3 Synonyms

Mabry syndrome · HPMR · HPMRS · hyperphosphatasia with mental retardation syndrome (historical; "mental retardation" is deprecated language, retained here only where it appears verbatim in titles) · hyperphosphatasia with impaired intellectual development syndrome · hyperphosphatasia-intellectual disability syndrome · GPI biosynthesis defect (GPIBD) subtype · inherited GPI deficiency (IGD).

### 1.4 Data provenance

Everything below is **disease-level aggregated knowledge** from case reports, case series, and multinational retrospective cohorts. There is no EHR-derived or registry-derived individual-patient dataset for Mabry syndrome specifically. The single largest structured cohort is the multinational IGD study of 83 individuals from 75 families ([Sidpra et al., *Brain* 2024;147:2775–2790](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11292905/)), and the largest PIGV-specific series is 16 families ([Horn et al., *Eur J Hum Genet* 2014, PMID:24129430](https://pubmed.ncbi.nlm.nih.gov/24129430/)).

---

## 2. Etiology

### 2.1 Primary cause

**Biallelic hypomorphic (partial loss-of-function) germline variants in genes of the GPI-anchor biosynthesis/remodeling pathway.** The word *hypomorphic* is load-bearing: complete GPI loss is embryonic-lethal, so every viable patient retains partial pathway function. This is why the phenotype is a graded spectrum rather than an on/off switch.

Six genes give the HPMRS/Mabry phenotype specifically ([Genes 2024, PMC11121671](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11121671/)):

| Subtype | Gene | HGNC | Compartment | Pathway role |
|---|---|---|---|---|
| HPMRS1 | **PIGV** | `hgnc:26031` | ER | GPI α-1,6-mannosyltransferase II (adds 2nd mannose) |
| HPMRS2 | **PIGO** | `hgnc:23215` | ER | Phosphoethanolamine transferase (3rd mannose EtNP) |
| HPMRS3 | **PGAP2** | `hgnc:17893` | Golgi | Fatty-acid remodeling (stearate reacylation) |
| HPMRS4 | **PGAP3** | `hgnc:23719` | Golgi | GPI-anchor maturation (deacylation) |
| HPMRS5 | **PIGW** | `hgnc:23213` | ER | Inositol acyltransferase (early step 3) |
| HPMRS6 | **PIGY** | `hgnc:28213` | ER | GPI-GlcNAc transferase complex subunit |

> "HPMRS1 [MIM: 239300] is the phenotype resulting from inheritance of biallelic PIGV variants. HPMRS2 (MIM 614749), HPMRS5 (MIM 616025) and HPMRS6 (MIM 616809) result from disruption of the PIGO, PIGW and PIGY genes expressed in the endoplasmic reticulum. HPMRS3 (MIM 614207) and HPMRS4 (MIM 615716) result from disruption of post attachment to proteins PGAP2 (HPMRS3) and PGAP3 (HPMRS4)." — [Genes 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11121671/)

**PIGV and PIGO are the two most frequently implicated genes** in Mabry syndrome.

### 2.2 Genetic risk factors

- **Causal**: biallelic pathogenic variants as above. No susceptibility loci or GWAS signals — this is a straight Mendelian recessive disease.
- **Founder/recurrent allele**: `PIGV` **c.1022C>A (p.Ala341Glu)**, rs139073416. Horn et al. found it *"in about 80% of affected families,"* both homozygous and compound heterozygous. gnomAD reports it at ~0.02% (30/126,708) of European chromosomes; ESP European-American MAF 0.00035 — consistent with a European founder allele of modest frequency. First reported in three siblings of unrelated German parents ([Krawitz et al., *Nat Genet* 2010, PMID:20802478](https://pubmed.ncbi.nlm.nih.gov/20802478/)).
- **Consanguinity** is a major contributor for the rarer subtypes — PGAP3 was mapped in a consanguineous Pakistani family via autozygosity mapping ([Howard et al., *Am J Hum Genet* 2014, PMID:24439110](https://pubmed.ncbi.nlm.nih.gov/24439110/)); PIGY in a consanguineous family via a 7.7 Mb autozygous region ([Ilkovski et al., *Hum Mol Genet* 2015, PMID:26293662](https://pubmed.ncbi.nlm.nih.gov/26293662/)).
- **Modifier genes**: none established. Digenic inheritance across two GPI genes has been *specifically tested and excluded* in at least one index case — the paper title says it plainly: ["Excluding Digenic Inheritance of PGAP2 and PGAP3 Variants in Mabry Syndrome (OMIM 239300) Patient"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9957281/). **Do not curate a digenic inheritance block for this disease.**

### 2.3 Environmental risk factors

**None known.** No toxin, exposure, infection, diet, occupational, or lifestyle factor has been associated with disease occurrence. Parental age, sex, and geography carry no reported risk signal beyond consanguinity/founder effects.

### 2.4 Protective factors

**None known genetically.** Environmentally the only "protective" thing in the literature is downstream and therapeutic, not preventive: **pyridoxine (vitamin B6) supplementation** appears to protect against seizure burden in a subset (see §12). No evidence for dietary or lifestyle primary prevention.

### 2.5 Gene–environment interactions

The one credible G×E axis is **nutrient-level**, and it is elegant: elevated ALP in the circulation degrades **pyridoxal 5′-phosphate (PLP)**, the active B6 vitamer, reducing its availability across the blood-brain barrier. Less PLP → less GABA synthesis (PLP is the cofactor for glutamate decarboxylase) → seizures. So a *genetic* enzyme-trafficking defect creates an *acquired, nutritionally correctable* cofactor deficiency in the CNS. Documented directly in CSF: an HPMRS3 patient had **CSF PLP 8 nmol/L (ref 10–37)** and **CSF 5-MTHF 66 nmol/L (ref 72–172)**, both normalizing on pyridoxine 100 mg BD + folinic acid 15 mg daily ([Messina et al., *JIMD Rep* 2023, PMID:36636587](https://pmc.ncbi.nlm.nih.gov/articles/PMC9830023/)).

---

## 3. Phenotypes

### 3.1 Core phenotypes — PIGV/HPMRS1 (HPO annotations for OMIM:239300, with n/N frequencies)

| Phenotype | HPO term | Frequency (HPO/OMIM) |
|---|---|---|
| Elevated circulating alkaline phosphatase | `HP:0003155` | **7/7 (100%)** |
| Intellectual disability | `HP:0001249` | **7/7** |
| Global developmental delay | `HP:0001263` | **7/7** |
| Short distal phalanx of finger (brachytelephalangy) | `HP:0009882` | **7/7** |
| Absent speech | `HP:0001344` | **6/6** |
| Hypotonia | `HP:0001252` | **5/5** |
| Hypertelorism | `HP:0000316` | 6/7 |
| Wide nasal bridge | `HP:0000431` | 6/7 |
| Broad nasal tip | `HP:0000455` | 6/7 |
| Downturned corners of mouth | `HP:0002714` | 6/7 |
| Seizure | `HP:0001250` | 3/5 |
| Abnormal rectum morphology | `HP:0002034` | 4/7 |
| Sensorineural hearing impairment | `HP:0000407` | 2/3 |
| Delayed ossification of carpal bones | `HP:0001216` | 2/3 |
| Constipation | `HP:0002019` | 2/5 |
| Anteriorly placed anus | `HP:0001545` | 2/5 |
| Aganglionic megacolon (Hirschsprung) | `HP:0002251` | 1/7 |
| Cleft palate | `HP:0000175` | 1/7 |
| Cleft upper lip | `HP:0000204` | 1/7 |
| Hydrocephalus | `HP:0000238` | 1/3 |

Additional HPO-annotated features without hard counts: severe intellectual disability `HP:0010864`, tented upper lip vermilion `HP:0010804`, thin upper lip vermilion `HP:0000219`, midface retrusion `HP:0011800`, short philtrum `HP:0000322`, short nose `HP:0003196`, long palpebral fissure `HP:0000637`, upslanted palpebral fissure `HP:0000582`, highly arched eyebrow `HP:0002553`, posteriorly rotated ears `HP:0000358`, malar flattening `HP:0000272`, mandibular prognathia `HP:0000303`, plagiocephaly `HP:0001357`, small nail `HP:0001792`, hyperconvex nail `HP:0001795`, tapered finger `HP:0001182`, short toe `HP:0001831`, delayed myelination `HP:0012448`, cerebral cortical atrophy `HP:0002120`, athetosis `HP:0002305`, abnormal renal morphology `HP:0012210`, abnormal heart morphology `HP:0001627`, abnormally large globe `HP:0001090`, feeding difficulties `HP:0011968`.

### 3.2 Pan-IGD cohort frequencies (n=83, Sidpra 2024 *Brain*)

This is the highest-quality frequency dataset available, though it spans all GPI genes, not Mabry-only. Curate it with an explicit note that the denominator is the broader IGD population.

> "Core clinical features were developmental delay or intellectual disability (DD/ID, 90%), seizures (83%), hypotonia (72%) and motor symptoms (64%)."

| Domain | Feature | Freq | HPO |
|---|---|---|---|
| Neuro | Delayed/absent speech | **95%** | `HP:0000750` / `HP:0001344` |
| Neuro | DD/ID | **90%** | `HP:0001263` / `HP:0001249` |
| Neuro | Seizures | **83%** | `HP:0001250` |
| Neuro | Hypotonia | **72%** | `HP:0001252` |
| Neuro | Motor symptoms | 64% | `HP:0002194` |
| Neuro | Non-ambulant | 64% | — |
| Neuro | Severe-to-profound DD/ID | 59% | `HP:0011344` |
| Neuro | Developmental epileptic encephalopathy | 51% (35/69 with seizures) | — |
| Neuro | Intractable/drug-resistant epilepsy | 57% (40/70) | — |
| Imaging | Cerebral atrophy | **75%** | `HP:0002059` |
| Imaging | Cerebellar atrophy | **60%** | `HP:0001272` |
| Imaging | Symmetric restricted diffusion, central tegmental tracts | 60% (31/52 DWI) | — |
| Imaging | Callosal anomalies | 57% | `HP:0002079` |
| Imaging | Hippocampal atrophy | 19% | — |
| Imaging | Diffuse leukodystrophy | 16% | — |
| Imaging | Craniosynostosis | 16% | `HP:0001363` (verify) |
| Imaging | Delayed myelination | 12% | `HP:0012448` |
| Systemic | Any multisystem involvement | 72% | — |
| GI | Any GI involvement | **66%** | — |
| GI | Aspiration risk | 47% | — |
| GI | GERD | 43% | — |
| GI | Constipation | 23% | `HP:0012450` |
| MSK | Musculoskeletal anomalies | 37% | — |
| MSK | Scoliosis | 27% | — |
| MSK | Osteopenia | 19% (11/59) | `HP:0000938` |
| Cardiac | Cardiac disease | 19% | — |
| Cardiac | Septal defects | 16% | `HP:0001631` / `HP:0001629` |
| Renal | Renal involvement | 17% | — |
| Renal | Hydronephrosis | 15% | `HP:0000126` |
| Renal | Renal cysts | 5% | `HP:0000107` |
| Renal | Renal dysplasia | 4% | `HP:0000110` |
| Dysmorphism | Any dysmorphic feature | 83% | — |
| **Biochem** | **Elevated ALP** | **25% (17/68)** | `HP:0003155` |

**Critical curation caveat on that last row.** In the broad IGD cohort only 25% had elevated ALP; 66% were normal and 9% were *low*. This is the single most important nuance in the disease: **hyperphosphatasia is definitional for HPMRS/Mabry but is not universal across GPI defects, and — importantly — is not even fully reliable within HPMRS.** A South African report describes two PGAP3-related Mabry patients with *unusually low* ALP. Curate hyperphosphatasia as a **defining feature of the HPMRS subgroup** with `frequency: VERY_FREQUENT` at the Mabry level, not as an obligate finding across GPI disease.

Seizure semiology in the cohort (of 69 with seizures): focal motor 23%, epileptic spasms 23% (`HP:0011097`), generalized tonic-clonic 20% (`HP:0002069`), generalized myoclonic 20% (`HP:0032794`), status epilepticus 10%.

### 3.3 Phenotype characteristics

- **Onset**: neonatal to infantile. **Median age at seizure onset 5.9 months** (IQR 2.0–10.0). Developmental delay is apparent in the first year. Hyperphosphatasia is present from infancy and persists.
- **Severity**: variable-to-severe; 59% severe-to-profound DD/ID. Horn et al.: *"the severe end of the clinical spectrum presents as a multiple congenital malformation syndrome with a high frequency of Hirschsprung disease, vesicoureteral, and renal anomalies as well as anorectal malformations."*
- **Progression**: this is the sleeper finding. The disease was long framed as static-encephalopathy-plus-epilepsy, but serial imaging says otherwise — **progressive cerebral volume loss in 87.5% and progressive cerebellar atrophy in 70.8%, "indicating a neurodegenerative process."** Cognitive/motor phenotype is largely static-to-slowly-declining; epilepsy is chronic and often refractory.
- **Course pattern**: chronic, lifelong. Seizures episodic on a chronic substrate. Interestingly, the 1970 index patients **stopped having spontaneous seizures in adulthood and came off anticonvulsants** — evidence that the epilepsy phenotype can attenuate with age in milder genotypes.

### 3.4 Quality of life

No EQ-5D / SF-36 / PROMIS data exist for Mabry syndrome. Functional proxies from the Sidpra cohort: non-ambulance 64%, absent/delayed speech 95%, ongoing enteral feeding and cortical visual impairment both significantly more likely in the DEE group (P<0.001 and P=0.007). Behavioral: ASD 4.8%, ADHD 2.4%. Practical burden is dominated by intractable epilepsy, feeding/aspiration, and total care dependence.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

**PIGV** (`hgnc:26031`, OMIM *610274, chromosome **1p36.11**) — encodes **GPI mannosyltransferase 2 / GPI-MT-II**, an ER membrane enzyme adding the **second mannose** to the GPI glycan backbone. Aliases: GPI-MT-II, PIG-V, dol-P-Man dependent GPI mannosyltransferase II. This is the flagship gene.

Others as tabled in §2.1. `ALPL` (`hgnc:438`, tissue-nonspecific alkaline phosphatase) is not causal but is the **biomarker substrate** — it's the GPI-anchored protein whose mis-release produces the hyperphosphatasia.

### 4.2 Pathogenic variants

**PIGV c.1022C>A, p.(Ala341Glu)** — NM_017837.4, rs139073416, ClinVar VCV000001284, classified **Pathogenic**. Missense. Present in ~80% of PIGV-positive families. Functionally: *"Expression of the p.Ala341Glu variant protein was drastically reduced as compared to wild type"* — so it behaves as a **hypomorph via reduced protein abundance/stability**, not catalytic-site abolition.

Other PIGV variants from Horn et al. (all novel at time of report): **c.176T>G, c.53G>A, c.905T>C, c.1405C>T**.

**PIGO** — compound heterozygous variants; mechanistically heterogeneous: *"The mutant transcripts are aberrantly spliced, decrease the membrane stability of the protein, or impair enzyme function such that GPI-anchor synthesis is affected and the level of GPI-anchored substrates localized at the cell surface is reduced"* ([Krawitz et al., *AJHG* 2012, PMID:22683086](https://pubmed.ncbi.nlm.nih.gov/22683086/)).

**PGAP2** — c.46C>T p.(Arg16Trp), c.380T>C p.(Leu127Ser), c.479C>T p.(Thr160Ile) in the original report; transfection into PGAP2-null cells *"showed only partial restoration of GPI-anchored marker proteins, CD55 and CD59, on the cell surface"* — direct in vitro demonstration of the hypomorph model. The 1970 index family carries **c.881C>T p.(Thr294Met)**. Also c.103del p.(Leu35Serfs*90) and c.134A>G p.(His45Arg).

**PGAP3** — c.275G>A p.(Gly92Asp) homozygous; c.439dupC p.(Leu147Profs*16) (frameshift → nonsense-mediated decay); c.914A>G p.(Asp305Gly); c.314C>G p.(Pro105Arg). PGAP3 also has **rare noncoding (intronic and 3′UTR) pathogenic variants**, which panel-based testing routinely misses ([Knaus et al., *Hum Mutat* 2016, PMC5084765](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5084765/)).

**PIGW** — compound heterozygous NM_178517: c.211A>C, c.499A>G ([Chiyonobu et al., *J Med Genet* 2014, PMID:24367057](https://pubmed.ncbi.nlm.nih.gov/24367057/)).

**PIGY** — c.137T>C p.(Leu46Pro) homozygous (severe: dysmorphism, seizures, severe DD, cataracts, early death); and a **promoter variant c.-540G>A** predicted to disrupt an SP1 consensus binding site and shown to reduce gene expression (milder: moderate DD + microcephaly). Ilkovski et al. explicitly flag the lesson: *"the potential importance of analysing variants detected in 5′-UTR regions despite their typically low coverage in exome data."*

**Origin**: exclusively **germline**, biallelic. No somatic contribution. No chromosomal abnormalities, aneuploidy, or CNV mechanism reported as a primary cause (though CMA remains part of a broad DD workup).

**Functional consequence class**: **partial loss of function (hypomorphic)** across the board. Complete null alleles are not compatible with life in this pathway — every reported patient retains residual GPI synthesis.

### 4.3 Modifier genes / epigenetics

No modifier genes established. No DNA-methylation or histone-modification signature has been reported for HPMRS (unlike, say, the well-characterized episignatures for some other ID syndromes). **This is a genuine knowledge gap worth curating as `kind: KNOWLEDGE_GAP`.**

---

## 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents contribute to causation. The disease is fully genetically determined. The only environmental variable of consequence is **B6 vitamer availability**, which is a *therapeutic* lever rather than an etiologic one (§2.5, §12).

---

## 6. Mechanism / Pathophysiology

Here is where it gets genuinely lovely. Think of the GPI anchor as a lipid anchor-bolt built stepwise on the ER membrane, then handed off to a rivet gun (the GPI transamidase) that swaps a protein's C-terminal signal peptide for the anchor. Two ways to break it: build a bad bolt (PIGV/PIGO/PIGW/PIGY, ER), or fumble the finishing work after riveting (PGAP2/PGAP3, Golgi). Both routes end with alkaline phosphatase floating free in the blood — but for *different reasons*.

### 6.1 The causal chain — biosynthesis arm (PIGV, PIGO, PIGW, PIGY)

**Node 1 — Hypomorphic GPI-pathway enzyme deficiency** (`biological_scale: MOLECULAR`)
Reduced enzyme abundance/activity in the ER. GO: **GPI anchor biosynthetic process `GO:0006506`**; **GPI mannosyltransferase activity `GO:0004376`**; **mannosyltransferase activity `GO:0000030`**; located in **endoplasmic reticulum membrane `GO:0005789`**.
↓
**Node 2 — Accumulation of incomplete, mannose-bearing GPI intermediates** (`MOLECULAR`)
The pathway stalls mid-assembly. This is the mechanistically decisive step.
↓
**Node 3a — Transamidase-mediated release of soluble alkaline phosphatase** (`MOLECULAR`)
The killer insight from [Murakami et al., *J Biol Chem* 2012;287:6318–25, PMID:22228761](https://pmc.ncbi.nlm.nih.gov/articles/PMC3307314/): the GPI transamidase doesn't just refuse to work — it works *badly*. It recognizes the truncated mannose-bearing intermediate, cleaves the C-terminal hydrophobic signal peptide off ALP anyway, and releases the enzyme as a **soluble, unanchored protein into the medium/serum**. GO: **alkaline phosphatase activity `GO:0004035`**.

The 2024 review states the model concretely: *"the proximity of the nascent peptide to an incomplete GPI anchor with at least one mannose may result in the recruitment of a portion of the transamidase, PIGU, that directs the catalytic subunit, PIGK, to cleave the GPI recognition sequence and liberate the non-GPI-anchored, soluble AP."*

**The elegant control experiment**: in **PIGM** deficiency, only *non-mannosylated* intermediates (GlcN-acyl-PI) accumulate, the transamidase is not efficiently engaged, ALP is degraded intracellularly — **and there is no hyperphosphatasia**. That's why some GPI defects have high ALP and others don't. It's a mannose-dependent switch. **This belongs in the pathophysiology graph as an explicit branch condition.**
↓
**Node 3b — Reduced cell-surface display of GPI-anchored proteins** (`CELLULAR`)
CD55, CD59, CD16, FLAER-binding GPI core all reduced on granulocytes and fibroblasts. Ilkovski measured *"significantly reduced levels of GPI-anchored proteins (CD55 and CD59) on the surface of patient-derived skin fibroblasts (~20–50% compared with controls)."* This is the arm that actually causes the *disease*; the ALP release is mostly the arm that causes the *lab abnormality*.
↓
**Node 4 — Impaired neuronal GPI-AP-dependent signaling and synaptic function** (`CELLULAR`)
GPI-APs include ephrin-A ligands, contactins, NCAM-120, Thy-1, glypicans, RECK, prion protein — a whole guild of axon-guidance, synapse-organizing and cell-adhesion molecules. GO: **chemical synaptic transmission `GO:0007268`**; **synapse `GO:0045202`**. Mouse data (§15) show reduced hippocampal synaptophysin, decreased excitatory synaptic transmission, elevated paired-pulse ratio, and downregulated *Abl1* across cell types — *Abl1* interacts with multiple EphrinA receptors, tying the transcriptomic hit back to GPI-anchored ephrin signaling.
↓
**Node 5a — Abnormal brain development and progressive neurodegeneration** (`TISSUE`)
Cerebral atrophy 75%, cerebellar atrophy 60%, callosal anomalies 57%, delayed myelination; serial imaging shows **progression** in 87.5%/70.8%. UBERON: **brain `UBERON:0000955`**, **cerebellum `UBERON:0002037`**, **hippocampal formation `UBERON:0002421`**, **corpus callosum `UBERON:0002336`**.
↓
**Node 5b — Circulating pyridoxal-5′-phosphate depletion** (`ORGANISM`)
Free serum/tissue ALP degrades PLP; CSF PLP falls; GABA synthesis falls. Direct human evidence: CSF PLP 8 nmol/L (ref 10–37), CSF 5-MTHF 66 (ref 72–172), both correcting on supplementation.
↓
**Node 6 — Seizures and developmental epileptic encephalopathy** (`ORGANISM`)
Two converging inputs: the structural/synaptic substrate (Node 5a) and the cofactor-deficiency substrate (Node 5b). The second is the treatable one — which is exactly why pyridoxine helps *some* patients partially and never achieves seizure freedom in most: you can top up the cofactor, but you can't rebuild the synapse.

### 6.2 The causal chain — remodeling arm (PGAP2, PGAP3)

Divergent from Node 2 onward, and mechanistically distinct even though the endpoint looks the same:

- **PGAP3 deficiency**: failure to deacylate the sn-2 unsaturated fatty acid. The unremodeled anchor is a substrate for **GPI-specific phospholipase C**, which releases the protein.
- **PGAP2 deficiency**: failure to reacylate with **stearic acid**. **Phospholipase D** then *"cleaves the lyso-GPI intermediate, resulting in transport of the unstable anchor and its attached protein, alkaline phosphatase, to the extracellular compartment."*

Either way the anchor fails to partition into **lipid rafts** — PGAP2/3 remodeling *"is required for stable association between GPI-anchored proteins and the cell-surface membrane rafts."* GO: **Golgi membrane `GO:0000139`**.

**Curation note**: the biosynthesis arm and remodeling arm should be **two distinct pathophysiology sub-branches converging on a shared downstream node** ("soluble ALP release" + "GPI-AP surface deficiency"). This is a textbook case for a mechanism module if dismech ever factors out *GPI anchor biosynthesis defect* as a conserved module — the same trigger→consequence chain recurs across ~24 genes and ~20 named disorders.

### 6.3 Phenotype-stage correlation (mechanistically meaningful)

Sidpra 2024 found **synthesis-stage gene variants → significantly shorter time to seizure onset** (median 5.6 mo) than transamidase/remodeling-stage variants (median 7.0 mo), log-rank **P = 0.046**. And the 2024 Genes HPO analysis across 152 patients / 22 genes found **biosynthesis defects → 33% abnormal digit morphology vs remodeling defects → 6.7%**, with biosynthesis defects showing greater muscle/tendon/joint involvement. So the *step in the pathway* is itself a phenotype-modifying variable. Worth an explicit `mechanistic_hypotheses` group.

### 6.4 Cell types, compartments, immune, metabolic

- **Cell types (CL)**: neuron `CL:0000540` (primary target), microglial cell `CL:0000129` (transcriptomically most-perturbed cluster in the Pigv mouse — 306 genes downregulated in one microglial subgroup, enriched for small-GTPase-mediated signal transduction), neutrophil/granulocyte `CL:0000775` (diagnostic readout tissue), fibroblast `CL:0000057` (diagnostic readout), osteoblast `CL:0000062` (ALPL source).
- **Subcellular (GO CC)**: **endoplasmic reticulum membrane `GO:0005789`** (PIGV/PIGO/PIGW/PIGY), **Golgi membrane `GO:0000139`** (PGAP2/PGAP3), plasma membrane / lipid raft microdomains. *(Note: `GO:0031225` "anchored component of membrane" and `GO:0016254` "preassembly of GPI anchor in ER membrane" are both **obsolete** in current GO — do not use them.)*
- **Immune involvement**: mechanistically present but clinically quiet. CD55 and CD59 are complement regulators; their loss is what causes paroxysmal nocturnal hemoglobinuria in *somatic* PIGA mutation. In inherited GPI deficiency the loss is partial and the hemolytic phenotype does **not** occur — a nice negative result to record. The Pgap3-knockout mouse does show *"altered T cell proliferation response and increased susceptibility to EAE."*
- **Metabolic**: no classical intermediary-metabolism block. Serum transferrin and transferrin isoelectric focusing are **normal** (22 and 19 individuals tested) — so despite being classified as a CDG, **HPMRS does not produce the N-glycosylation transferrin abnormality**. Clinically important: a normal CDG transferrin screen does not exclude this disease.
- **Tissue damage mechanism**: not oxidative/ischemic/fibrotic. It is **developmental mis-wiring plus progressive volume loss** — a neurodevelopmental-then-neurodegenerative dual process.
- **Molecular profiling available**: single-cell RNA-seq of Pigv341E mouse hippocampus (see §15) is the only omics dataset. No human transcriptomic, proteomic, metabolomic, lipidomic, spatial, or CRISPR-screen data specific to Mabry syndrome. Substantial gap.

---

## 7. Anatomical Structures Affected

**Primary organ**: brain (`UBERON:0000955`) — cerebral cortex, cerebellum (`UBERON:0002037`), hippocampal formation (`UBERON:0002421`), corpus callosum (`UBERON:0002336`), central tegmental tracts (brainstem; symmetric restricted diffusion in 60% is a notably specific radiologic sign).

**Body systems** (with cohort frequencies): nervous (≈100%), gastrointestinal (66%; colon `UBERON:0001155` — Hirschsprung, anorectal malformation, constipation, GERD, aspiration), musculoskeletal (37%; bone element `UBERON:0001474` — brachytelephalangy, scoliosis, osteopenia, delayed carpal ossification), cardiovascular (19%; heart `UBERON:0000948` — septal defects), renal/urinary (17%; kidney `UBERON:0002113` — hydronephrosis, cysts, dysplasia, vesicoureteral anomalies), auditory (sensorineural hearing loss), visual (cortical visual impairment; cataracts in severe PIGY), craniofacial (dysmorphism in 82–83%).

**Lateralization**: bilateral and symmetric throughout. The central-tegmental-tract diffusion restriction is explicitly described as **symmetric**.

**Tissue types**: neural tissue (neurons, glia) primary; enteric nervous system (neural crest derivative — the Hirschsprung link is a neurocristopathy signal worth flagging); bone and connective tissue secondary.

---

## 8. Temporal Development

- **Onset**: congenital/neonatal-to-infantile. Hypotonia and dysmorphism at birth; developmental delay within the first year; **median seizure onset 5.9 months (IQR 2.0–10.0)**. Orphanet lists age of onset as infancy/neonatal.
- **Onset pattern**: chronic/insidious for the developmental phenotype; seizures may present acutely, sometimes as **West syndrome with hypsarrhythmia** (the PIGW index case).
- **Stages**: no formal staging system exists. A pragmatic natural-history framing: (1) neonatal hypotonia + dysmorphism + incidental hyperphosphatasia; (2) infantile seizure onset ± developmental epileptic encephalopathy; (3) childhood plateau with intractable epilepsy, feeding difficulty, non-ambulance; (4) progressive volume loss on serial imaging; (5) in milder genotypes, possible adult seizure remission.
- **Progression rate**: variable, generally slow. Severe end = death in early childhood; mild end = survival to adulthood with stable disability.
- **Course**: chronic and lifelong; epilepsy is relapsing/refractory in 57%.
- **Remission**: spontaneous seizure remission in adulthood is documented in the 1970 index patients — *"During adulthood, however, 1-VI-4 and 1-VI-16 no longer experienced spontaneous seizures and were no longer administered anticonvulsants."* Treatment-induced complete seizure control on pyridoxine occurred in 4/22 trialed individuals.
- **Critical periods**: the first year — seizure onset window and the period of maximal synaptogenesis. The AAV gene-therapy mouse work delivered vector on **postnatal day 1**, implying a narrow neonatal therapeutic window for any future disease-modifying approach.

---

## 9. Inheritance and Population

- **Prevalence**: **<1 / 1,000,000** (Orphanet ORPHA:247262). In `PrevalenceClassEnum` terms → `BELOW_1_IN_1000000`, `rate_per_100000` ≈ 0.1 or lower, `measure_type: POINT_PREVALENCE`. Fewer than ~100 HPMRS patients reported for the common subtypes; some subtypes (PIGY, PIGW) have single-digit case counts. The broader review counts 1–85 reported cases per gene across all 24 IGD genes and states plainly: *"there are currently no established diagnostic guidelines for this rare disease."*
- **Denominator context**: the Deciphering Developmental Disorders study suggests **GPI biosynthesis disorders collectively account for ~0.15% of individuals with developmental disability** — a useful `CASES_IN_LITERATURE`-adjacent figure, but note it's the whole GPIBD family, not Mabry alone.
- **Incidence**: not established.
- **Inheritance**: **autosomal recessive** (`HP:0000007`) for all six subtypes. Recurrence risk 25% per pregnancy.
- **Penetrance**: complete in biallelic carriers, as far as reported. No non-penetrant homozygotes described.
- **Expressivity**: **highly variable**, both between and within genes. Horn: *"PIGV mutations are the major cause of HPMRS, which displays a broad clinical variability regarding associated malformations and growth patterns."* PIGY is the extreme case — the same gene gives lethal multisystem disease (p.Leu46Pro) and moderate DD + microcephaly (promoter variant), tracking residual expression level.
- **Anticipation**: none — no repeat expansion mechanism.
- **Germline mosaicism**: not reported.
- **Founder effect**: PIGV c.1022C>A in Europeans (German/Northern European), ~0.02% European allele frequency in gnomAD.
- **Carrier frequency**: not systematically established. Back-of-envelope from the PIGV A341E European AF of ~2.4×10⁻⁴ → carrier frequency ~1/2,100 for that allele alone. **Treat as an estimate, not a sourced figure.**
- **Consanguinity**: a major factor for PGAP3, PIGY, PGAP2 — several index families were consanguineous (Pakistani, Saudi, South African cohorts).
- **Population/geography**: reported worldwide — Germany, Netherlands, Canada, USA, Japan, Pakistan, Saudi Arabia, Italy, South Africa, UK. PIGV skews European; PGAP3 is over-represented in South Asian and Middle Eastern consanguineous populations.
- **Sex ratio**: 1:1, as expected for autosomal recessive. No sex bias reported.
- **Age distribution**: overwhelmingly pediatric in published series (median follow-up 2.9 years). The oldest individual in the Sidpra cohort was **20 years** (compound heterozygous PIGT). The 1970 index patients born 1952 and 1958 survived into their 60s — so long survival is achievable at the mild end.

---

## 10. Diagnostics

### 10.1 Laboratory / biomarkers

- **Serum alkaline phosphatase** (LOINC 6768-6, *Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma*). Persistently elevated, typically the entry point to diagnosis. **Caveat, restated because it matters: elevated in only 25% of the broad IGD cohort; normal or even low ALP does not exclude Mabry, particularly PGAP3.** Isoenzyme fractionation confirms it is **tissue-nonspecific ALP** (ALPL), not the intestinal or placental isoform, and it is *not* accompanied by bone disease.
- **Flow cytometry for GPI-anchored proteins** — the functional confirmatory assay. Panel: **CD16 and CD24 on granulocytes; CD14 on monocytes; CD55 and CD59 on granulocytes/erythrocytes/fibroblasts; FLAER** (fluorescently-labeled aerolysin), which *"pan-specifically recognize[s] the core GPI structure."* Chiyonobu: *"flow cytometric analysis of blood cells is effective in screening IGD."* One important limitation from Knaus 2018: *"Flow cytometric markers"* showed **no gene-specific patterns and no correlation with phenotypic severity** — flow tells you *whether*, not *which* or *how bad*.
- **CSF neurotransmitter/vitamer panel** — CSF pyridoxal 5′-phosphate, 5-methyltetrahydrofolate, homovanillic acid. Underused and directly actionable, since low PLP/5-MTHF predicts response to pyridoxine + folinic acid.
- **Serum transferrin isoelectric focusing** — **normal**. Do not use to screen for this CDG.

### 10.2 Imaging

Brain MRI including DWI. Look for: cerebral atrophy, cerebellar atrophy, callosal anomalies, and the relatively distinctive **symmetric restricted diffusion of the central tegmental tracts** (60%). Serial MRI is warranted given documented progression. Hand radiographs for brachytelephalangy and delayed carpal ossification. Renal ultrasound, echocardiography. Contrast enema / rectal suction biopsy if Hirschsprung is suspected.

### 10.3 Electrophysiology

EEG — may show **hypsarrhythmia** (West syndrome presentation, documented with PIGW). Otherwise variable epileptiform patterns matching the mixed semiology.

### 10.4 Genetic testing

Recommended tiering:
1. **Whole exome or whole genome sequencing** as first-line for undiagnosed DD/ID + seizures ± high ALP. The 2024 review argues explicitly for **WGS combined with RNA sequencing as "a first line diagnostic method,"** because *"traditional panel-based approaches may miss intronic and 3′UTR variants"* — a warning earned the hard way by the noncoding PGAP3 and promoter PIGY variants.
2. **Targeted GPI-pathway gene panel** — historically productive: Hansen/Krawitz *"developed a diagnostic gene panel for targeting all known genes encoding proteins in the GPI-anchor-synthesis pathway."* Must cover all ~31 pathway genes plus UTRs/promoters to be adequate.
3. **Single-gene PIGV testing** — reasonable only in a classic phenotype with the c.1022C>A founder allele suspected.
4. **CMA/karyotype/FISH** — part of a generic DD workup; will not diagnose this disease.
5. **mtDNA / repeat expansion testing** — not applicable.

**Automated facial phenotyping is a genuinely useful diagnostic adjunct here.** Knaus 2018 found *"facial recognition software achieved the highest accuracy in predicting the disease-causing gene"* — beating flow cytometry and clinical features. The 2024 review adds: *"automated facial analysis, for example by GestaltMatcher, enables more accurate gene assignment in GPI patients compared to experienced clinicians."* Patients with PIGV and PGAP3 variants have the most distinctive facial gestalts.

### 10.5 Clinical criteria and differential

No formal consensus diagnostic criteria exist. Horn's working criteria: **intellectual disability + elevated serum alkaline phosphatase** as minimal criteria.

**Differential diagnosis** (all should be curated as `differentials`):
- **Transient hyperphosphatasemia of infancy** — benign, self-resolving in weeks-to-months, no neurologic features. The single most common thing to rule out.
- **Hypophosphatasia** (`MONDO` ALPL) — the exact mirror image: *low* ALP. Conceptually satisfying to hold both in mind.
- **Vitamin D deficiency rickets, healing fractures, Paget disease, hepatobiliary disease, bone tumors** — non-genetic causes of raised ALP.
- **Other GPI biosynthesis defects without hyperphosphatasia** — MCAHS (multiple congenital anomalies-hypotonia-seizures syndrome; PIGN, PIGT, PIGA), PIGA-related DEE, PGAP1-related ID. Knaus 2018 argues for collapsing these labels: *"The authors recommend unified classification as GPIBDs given overlapping clinical presentations and biochemical findings across both syndrome categories."*
- **Other CDGs** — distinguishable by abnormal transferrin IEF (abnormal in classical CDG, **normal** in HPMRS).
- **Pyridoxine-dependent epilepsy (ALDH7A1)** and **PNPO deficiency** — both B6-responsive, both in the seizure differential; distinguished by α-AASA/pipecolic acid and by genotype.
- Kabuki syndrome, Coffin-Siris, and other dysmorphic ID syndromes on gestalt alone.

### 10.6 Screening

- **Newborn screening**: not included in any national NBS panel. No validated screening assay.
- **Carrier screening**: PIGV/PIGO/PGAP2/PGAP3 appear on some expanded carrier screening panels; no population program.
- **Cascade testing**: standard for at-risk siblings and for reproductive planning in known families.

---

## 11. Outcome / Prognosis

- **Mortality**: **15/83 (18%) deceased** at time of writing in the Sidpra cohort, with **median survival 1.5 years (IQR 1.4–2.8)** among those who died. Causes: respiratory failure secondary to recurrent infection (5/15), seizure-related death (5/15 — 3 post-ictal cardiorespiratory failure, 2 intractable status epilepticus), **SUDEP (4/15)**, GI complications (1/15). Note the SUDEP signal is echoed in the Mabry index family, where two members *"died of sudden unexpected nocturnal frontal lobe epilepsy (SUDEP) despite anticonvulsant medication."* **SUDEP risk counseling is warranted.**
- **Survival at the mild end**: the 1970 index patients (born 1952 and 1958, PGAP2 p.Thr294Met) survived into their 60s with relative phenotypic stability. Oldest in the modern cohort: 20 years. So the survival distribution is genuinely bimodal — severe genotypes die in infancy/early childhood; mild ones reach adulthood.
- **No 5-/10-year survival statistics exist.** Do not fabricate them.
- **Morbidity**: severe. Non-ambulant 64%, absent/delayed speech 95%, severe-to-profound DD/ID 59%, intractable epilepsy 57%, ongoing enteral feeding in the DEE group, cortical visual impairment, osteopenia 19%.
- **Recovery potential**: none for the neurodevelopmental phenotype. Seizure burden is partially modifiable.
- **Prognostic factors** (all statistically supported in Sidpra 2024):
  - **Developmental epileptic encephalopathy (51%)** is the dominant adverse prognostic marker → intractable epilepsy (P=0.003), non-ambulance (P=0.035), ongoing enteral feeds (P<0.001), cortical visual impairment (P=0.007).
  - Conversely, developmental encephalopathy *without* DEE → significantly more likely to achieve seizure control (P=0.003) and to achieve it on **monotherapy** (P=0.010).
  - **Pathway stage**: synthesis-stage genes → earlier seizure onset (P=0.046).
  - **Neuroimaging** features are described as *"prognostic and biologically significant"* — cerebral atrophy, cerebellar atrophy, callosal anomalies, central tegmental tract restricted diffusion.
- **Prognostic biomarkers**: none validated. ALP level does **not** correlate with severity, and neither do flow-cytometry GPI-AP levels (Knaus 2018: no correlation with phenotypic severity). Genotype (specific variant + pathway stage) is currently the best predictor. Sidpra used **unsupervised hierarchical clustering** to identify *"novel genotypic predictors of clinical phenotype and long-term outcome with meaningful implications for management."*

---

## 12. Treatment

There is **no disease-modifying therapy in clinical use**. Management is supportive plus one intriguing partially-effective cofactor intervention.

### 12.1 Pyridoxine / pyridoxal-5′-phosphate — the signature intervention

**MAXO: `MAXO:0001131` pyridoxine supplementation** (also `MAXO:0001129` vitamin supplementation, `MAXO:0000761` B vitamin supplementation). **CHEBI: `CHEBI:16709` pyridoxine**, `CHEBI:18405` pyridoxal 5′-phosphate. Modality: `SMALL_MOLECULE`.

**Rationale**: soluble ALP degrades PLP → CNS PLP deficiency → reduced glutamate decarboxylase activity → reduced GABA → seizures. Supplementation restores the cofactor pool.

**Evidence, in order of rigor:**
- **Prospective open-label multicenter pilot, n=9, Japan** — oral pyridoxine **20–30 mg/kg/day for 1 year**: *"One year of daily high-dose pyridoxine treatment was effective in the treatment of seizures in more than half of our patients with IGDs and modestly improved development in the majority of them."*
- **Prospective cohort, n=7, ages 5–23, 3 months, pyridoxine 20–30 mg/kg/day ± switch to P5P** ([Bayat et al., *Dev Med Child Neurol* 2022;64:789–798, PMID:35080266](https://pubmed.ncbi.nlm.nih.gov/35080266/)): *"more than 50% seizure frequency reduction in 2 out of 7 and less than 50% reduction in another 3 out of 7 participants."* Critically: *"no participants reached seizure freedom"* and electrophysiological improvement was minimal. Conclusion: *"pyridoxine may reduce seizure frequency or burden in inherited GPI deficiency."*
- **Retrospective cohort, n=22 trialed of 83** (Sidpra 2024): complete seizure control in 4, partial in 3. **One individual had a paradoxical increase in seizure frequency.** *"No association was found between pyridoxine dose and seizure control."*
- **Case-level, HPMRS3, with biochemical target engagement** (Messina 2023): pyridoxine **100 mg twice daily** + folinic acid 15 mg daily → complete normalization of CSF PLP, 5-MTHF, and HVA, *"with concurrent improvements in speech and fine motor skills."*
- **Case series, HPMRS3 + HPMRS4** ([*Mol Syndromol* 2025/2026, PMID:41064048](https://pmc.ncbi.nlm.nih.gov/articles/PMC12503530/)): high-dose pyridoxine, patient 1 *"no seizures...during follow-up,"* patient 2 *"no seizures...during the 8-month follow-up."*

**Honest summary for the KB**: response rate roughly 30–55% for meaningful seizure reduction, seizure freedom uncommon, no dose-response relationship established, occasional paradoxical worsening, and **PGAP2/HPMRS3 appears the most responsive subtype**. The 2024 review calls for standardizing dosing and defining the *"dose, route of administration and vitamer species that produces seizure suppression in 50% of patients."* Also worth noting: high-dose pyridoxine carries a real risk of **sensory peripheral neuropathy** at chronic high exposure — a monitoring requirement that the primary literature underplays.

**Folinic acid** (`CHEBI:15640` 5-formyltetrahydrofolic acid) — co-administered where CSF 5-MTHF is low; 15 mg daily in the reported case.

### 12.2 Antiseizure medication

**MAXO: `MAXO:0000167` anticonvulsant agent therapy.** No agent is specifically indicated. **Levetiracetam** (`CHEBI:6437`) was the most-used, appearing in *"38.5% of individuals (15/39) as part of a polytherapeutic regimen."* 57% have drug-resistant epilepsy. **No individuals underwent epilepsy surgery** in the 83-person cohort — surgical candidacy is essentially absent given the diffuse/genetic substrate. Ketogenic diet (`MAXO:0030010`) has not been systematically evaluated — a gap.

### 12.3 Supportive and rehabilitative

- Physical therapy `MAXO:0000011`, occupational therapy `MAXO:0001351`, speech therapy `MAXO:0000930`
- Gastrostomy `MAXO:0001346` for aspiration risk (47%) and feeding difficulty
- Supportive care `MAXO:0000950`
- Surgical: Hirschsprung pull-through, anorectal malformation repair, cardiac septal defect repair, cleft palate repair, scoliosis management
- Bone health monitoring given 19% osteopenia
- Genetic counseling `MAXO:0000079`

### 12.4 Experimental / advanced therapeutics

- **AAV gene therapy** — preclinical only. AAV-PHP.eB carrying human *PIGA* under a CAG promoter, delivered on postnatal day 1 into Nestin-*Piga* conditional knockout mice: improved neurologic function and survival, enhanced myelination, **elimination of spontaneous seizures in female mice**, hPIGA expression reaching endogenous levels by day 25 ([*Mol Ther Methods Clin Dev* 2024, PMID:38572066](https://pmc.ncbi.nlm.nih.gov/articles/PMC10988122/)). **Safety flag**: treated females surviving to 1 year developed **liver tumors associated with *Rian* overexpression** — the known AAV integration risk in neonatal delivery. Targets PIGA, not any HPMRS gene, so it's a proof-of-concept for the pathway rather than for Mabry specifically. Modality: `GENE_THERAPY`.
- **Synthetic GPI fragment supplementation** — in vitro efficacy shown only.
- **No registered clinical trials specific to Mabry syndrome / HPMRS were identified on ClinicalTrials.gov.** The CDG natural-history study at the Frontiers in CDG Consortium (FCDGC) enrolls PGAP3-CDG patients and is the most relevant ongoing study; verify its NCT before curating.
- **Pharmacogenomics**: none established. No genotype-guided drug selection beyond the (weak) signal that PGAP2/HPMRS3 may be more pyridoxine-responsive.

---

## 13. Prevention

- **Primary prevention**: not possible — the disease is fully determined at conception. The only lever is reproductive: **genetic counseling** (`MAXO:0000079`), carrier testing of relatives, and, for couples with a prior affected child, **preimplantation genetic testing (PGT-M)** or **prenatal diagnosis** by CVS/amniocentesis with targeted variant testing. 25% recurrence risk per pregnancy.
- **Secondary prevention (early detection)**: no newborn or population screening program. The practical secondary-prevention move is diagnostic-pathway design — **checking serum ALP in any infant with unexplained developmental delay and seizures**, and not dismissing a normal ALP. Earlier molecular diagnosis enables earlier pyridoxine trial and accurate counseling.
- **Tertiary prevention (complication avoidance)**: this is where most of the actionable work lives — aggressive seizure management to reduce status epilepticus and SUDEP risk; aspiration precautions and gastrostomy given 47% aspiration risk and 5/15 deaths from respiratory failure; bone density surveillance; scoliosis monitoring; renal and cardiac imaging at diagnosis; hearing and vision assessment.
- **Immunization**: standard childhood schedule. No contraindication, no special vaccine strategy. Given respiratory-infection mortality, **influenza, RSV, and pneumococcal immunization deserve emphasis** as a rational (if unstudied) intervention.
- **Public health / environmental interventions**: not applicable.
- **Prophylaxis**: no established prophylactic medication. Rescue benzodiazepine protocols for prolonged seizures are standard practice.

---

## 14. Other Species / Natural Disease

- **Taxonomy**: GPI anchoring is one of the deepest-conserved post-translational modifications in eukaryotes — present in yeast (*Saccharomyces cerevisiae*, NCBITaxon:4932), trypanosomes, *Plasmodium*, and all metazoa. The pathway genes have clear orthologs in *Mus musculus* (NCBITaxon:10090), *Rattus norvegicus* (10116), *Danio rerio* (7955), *Drosophila melanogaster* (7227), *C. elegans* (6239).
- **Orthologs**: mouse *Pigv* (MGI:2442480), mouse *Pgap3* (MGI:2444461), rat *Pigv* (RGD:1349310), plus orthologs of all six HPMRS genes.
- **Naturally occurring disease in other species**: **none reported.** No OMIA entry for a spontaneous animal HPMRS phenotype; no companion-animal or wildlife equivalent. Every animal model is engineered.
- **Breed associations (VBO)**: not applicable.
- **Comparative pathology**: yeast GPI mannosyltransferase mutants are lethal and can be complemented by trypanosomal/plasmodial PigB proteins — good evidence of deep functional conservation of the mannosyltransferase step. The mouse *Pigv* A341E knock-in recapitulates the human phenotype well (§15), supporting cross-species conservation of the neurodevelopmental consequence.
- **Zoonotic potential / cross-species transmission**: not applicable — this is a germline Mendelian disorder.
- **Veterinary relevance**: none.

---

## 15. Model Organisms

### 15.1 The flagship: *Pigv*<sup>341E</sup> knock-in mouse

[Rodríguez de los Santos et al., *PNAS* 2021;118:e2014481118, PMID:33402532](https://pmc.ncbi.nlm.nih.gov/articles/PMC7812744/) — CRISPR-Cas9 knock-in of the exact human founder allele at the conserved mouse residue: *"we used CRISPR-Cas9 to introduce the most prevalent hypomorphic missense mutation in European patients, Pigv:c.1022C > A (p.A341E), at a site that is conserved in mice."* Model type: **mammalian, germline knock-in, humanized point mutation** — about as faithful as a rodent model gets.

**Phenotype recapitulation:**

| Domain | Finding | Human counterpart |
|---|---|---|
| Motor | Reduced rotarod latency, elevated beam-traversal latency, abnormal fore-/hindpaw gait, hindlimb clasping | Motor delay 64%, hypotonia 72% |
| Growth | Reduced weight from early postnatal life | Growth abnormalities reported in HPMRS |
| Cognition | Delayed spatial learning; *"impaired long-term spatial memory at day 12"* (Barnes maze); short-term working memory intact | DD/ID 90% |
| Species-typical behavior | Fewer marbles buried, lower-quality nests | — |
| Social | *"enhanced social approach behavior"* — increased nose-to-anogenital contacts, decreased rearing | Divergent from human; see limitations |
| Sleep | Reduced total sleep, more active during light phase | Circadian/sleep disturbance under-characterized in humans |
| Seizures | PTZ kindling: *"significantly lower seizure threshold"*; first seizure at 63.3 min vs 93.3 min in WT; **all** mutants seized vs 4 WT never seizing after 10 injections | Seizures 83%, DEE 51% |
| Synaptic | *"decreased immunoreactivity for synaptophysin in cornu ammonis 1–stratum radiatum"*; reduced EPSP amplitude; elevated paired-pulse ratio; elevated post-tetanic potentiation | Mechanistic — no direct human counterpart |
| Transcriptomic | scRNA-seq: *Abl1* downregulated across all hippocampal cell clusters (links to GPI-anchored ephrin-A signaling); *Hdc* (histidine decarboxylase) elevated (candidate for sleep/circadian phenotype); 306 genes down in a microglial subgroup | Mechanistic |

**Limitations**: mice show **enhanced** rather than reduced sociability — opposite in valence to human phenotypes, and a caution against over-reading the social domain. Seizures required PTZ provocation; the model is seizure-*susceptible*, not spontaneously epileptic. **Alkaline phosphatase was not quantified**, so the model does not directly validate the hyperphosphatasia biomarker. Facial dysmorphism, brachytelephalangy, Hirschsprung, and renal/cardiac anomalies are not reported. Progressive cerebral/cerebellar atrophy is not demonstrated.

**Curation note**: this pattern — a well-validated mouse recapitulating the neurologic core while diverging on sociability and leaving the defining biomarker unmeasured — is a good candidate for a `kind: HUMAN_MODEL_MISMATCH` discussion entry rather than a plain knowledge gap, per the dismech convention. Evidence source: `MODEL_ORGANISM`.

### 15.2 Other models

- ***Pgap3* knockout mouse** (MGI:2444461): *"abnormal head and tail morphology, growth retardation, limb grasping, altered T cell proliferation response and increased susceptibility to EAE."* Original purpose was immunological — probing fatty-acid remodeling of GPI-APs; in the KO, *"GPI-APs are expressed on the cell surface without fatty acid remodeling, and fail to associate with lipid rafts."* Note the phenotype includes the same limb-grasping/growth-retardation neurologic signature.
- **PGAP3 developmental studies**: a dedicated paper on PGAP3's *"novel role in brain morphogenesis and neuronal wiring at early development"* ([PMC7569840](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7569840/)) — relevant to the developmental arm of the mechanism.
- **Nestin-*Piga* conditional knockout mouse** — CNS-specific *Piga* deletion from E11.5; used as the gene-therapy testbed. Severe: untreated survival ~3 weeks (males) to ~3 months (females). Models a different gene but the same pathway.
- **CHO cell mutant lines** defective at defined GPI biosynthesis steps — the workhorse in vitro system. Murakami used these to demonstrate the transamidase-dependent ALP-release mechanism; Howard used CHO complementation to validate PGAP3 missense pathogenicity; Krawitz/Hansen used PGAP2-null cells for CD55/CD59 rescue assays. Evidence source: `IN_VITRO`.
- **Patient-derived skin fibroblasts** — used for CD55/CD59 flow cytometry (20–50% of control levels in PIGY patients). `IN_VITRO`.
- **Yeast complementation assays** for GPI mannosyltransferase function. `IN_VITRO`.
- **Not available**: no zebrafish, *Drosophila*, *C. elegans*, iPSC-derived neuron, organoid, or MorPhiC model of any HPMRS gene was identified. Given that PIGV/PGAP3 are strong candidates for iPSC-derived neuronal phenotyping, this is a real and citable gap.

**Databases**: MGI (Pigv MGI:2442480, Pgap3 MGI:2444461), RGD (Pigv RGD:1349310), IMPC/KOMP for pathway-gene knockouts, Alliance of Genome Resources for orthology.

---

## 16. Curation summary — suggested dismech structure

| dismech section | Recommended content |
|---|---|
| `disease_term` | `MONDO:0016596` if entry is "Mabry syndrome"; `MONDO:0009398` only if renamed to HPMRS1 |
| `has_subtypes` | HPMRS1–6, names `HPMRS1`…`HPMRS6`, `display_name` with gene |
| `inheritance` | Autosomal recessive, `HP:0000007` |
| `genetic` | 6 genes with HGNC terms as tabled; `case_fractions` for PIGV (~80% of PIGV-positive families carry c.1022C>A) |
| `pathophysiology` | Two-arm chain per §6: biosynthesis (MOLECULAR→CELLULAR) and remodeling (MOLECULAR), converging on soluble-ALP-release + GPI-AP surface deficiency, → synaptic dysfunction (CELLULAR) → brain atrophy (TISSUE) → seizures/DD (ORGANISM); plus the PLP-depletion side branch |
| `phenotypes` | §3.1 for HPMRS1 with n/N frequencies; §3.2 pan-IGD frequencies with explicit denominator note |
| `biochemical` | Serum ALP with `reference_ranges`; CSF PLP (ref 10–37 nmol/L) and CSF 5-MTHF (ref 72–172 nmol/L) with `interpretation_bands` |
| `prevalence` | `BELOW_1_IN_1000000`, `POINT_PREVALENCE`, source `ORPHA:247262` |
| `treatments` | Pyridoxine (`MAXO:0001131` + `CHEBI:16709`), folinic acid, anticonvulsant therapy (`MAXO:0000167`), gastrostomy, PT/OT/speech, genetic counseling |
| `discussions` | `KNOWLEDGE_GAP`: no episignature, no human omics, no ketogenic-diet data, no NCT-registered interventional trial. `HUMAN_MODEL_MISMATCH`: Pigv341E sociability inversion + unmeasured ALP |
| `mechanistic_hypotheses` | (a) mannose-dependent transamidase switch explains why some GPI defects have hyperphosphatasia and others don't — `status: ESTABLISHED`; (b) ALP-mediated PLP depletion as the treatable seizure mechanism — `status: EMERGING`; (c) pathway-stage-determines-phenotype — `status: EMERGING` |

**Two things to double-check before you commit**: the ICD-11 code and the MeSH descriptor are both unverified above — I'd leave them out rather than guess. And run `just fetch-reference` on every PMID here before quoting; the abstracts above came from PubMed/PMC directly, but the dismech snippet validator wants its own cache, and a couple of the quotes are stitched from PMC full text rather than the abstract proper, which will fail substring matching.

---

## Sources

- [Krawitz PM et al. *Nat Genet* 2010;42:827–9 — PIGV (PMID:20802478)](https://pubmed.ncbi.nlm.nih.gov/20802478/)
- [Krawitz PM et al. *Am J Hum Genet* 2012 — PIGO (PMID:22683086)](https://pubmed.ncbi.nlm.nih.gov/22683086/)
- [Murakami Y et al. *J Biol Chem* 2012;287:6318–25 — ALP release mechanism (PMID:22228761)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3307314/)
- [Hansen L / Krawitz P et al. *Am J Hum Genet* 2013 — PGAP2 (PMID:23561847)](https://pubmed.ncbi.nlm.nih.gov/23561847/)
- [Horn D et al. *Eur J Hum Genet* 2014 — PIGV mutation spectrum (PMID:24129430)](https://pubmed.ncbi.nlm.nih.gov/24129430/)
- [Howard MF et al. *Am J Hum Genet* 2014 — PGAP3 (PMID:24439110)](https://pubmed.ncbi.nlm.nih.gov/24439110/)
- [Chiyonobu T et al. *J Med Genet* 2014 — PIGW / West syndrome (PMID:24367057)](https://pubmed.ncbi.nlm.nih.gov/24367057/)
- [Ilkovski B et al. *Hum Mol Genet* 2015 — PIGY (PMID:26293662)](https://pubmed.ncbi.nlm.nih.gov/26293662/)
- [Knaus A et al. *Hum Mutat* 2016 — noncoding PGAP3 variants (PMC5084765)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5084765/)
- [Knaus A et al. *Genome Med* 2018 — flow cytometry + facial image analysis (PMID:29310717)](https://pubmed.ncbi.nlm.nih.gov/29310717/)
- [Rodríguez de los Santos M et al. *PNAS* 2021 — Pigv341E mouse (PMID:33402532)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7812744/)
- [Bayat A et al. *Dev Med Child Neurol* 2022;64:789–798 — pyridoxine/P5P cohort (PMID:35080266)](https://pubmed.ncbi.nlm.nih.gov/35080266/)
- [Messina M et al. *JIMD Rep* 2023 — HPMRS3 CSF abnormalities (PMID:36636587)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9830023/)
- [Thompson MD et al. *Genes* 2023 — excluding digenic PGAP2/PGAP3 (PMC9957281)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9957281/)
- [PGAP3-CDG: 65 cases. *Mol Genet Metab* 2023 (PMID:37647829)](https://pubmed.ncbi.nlm.nih.gov/37647829/)
- [Sidpra J et al. *Brain* 2024;147:2775–2790 — 83-individual IGD cohort (PMC11292905)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11292905/)
- [Thompson MD et al. *Genes* 2024 — Mabry index cases + GPI disorders (PMID:38790248)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11121671/)
- [Inherited GPI deficiency review. *Acta Biochim Biophys Sin* 2024 (PMID:39081219)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11466713/)
- [AAV gene therapy for GPI deficiency. *Mol Ther Methods Clin Dev* 2024 (PMID:38572066)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10988122/)
- [HPMRS3/HPMRS4 pyridoxine case series. *Mol Syndromol* 2025 (PMID:41064048)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12503530/)
- [Thompson MD et al. *Am J Med Genet A* 2012 — phenotypic variability (PMID:22315194)](https://pubmed.ncbi.nlm.nih.gov/22315194/)
- [Mabry CC et al. *J Pediatr* 1970;77:74–85 — original description](https://www.jpeds.com/article/S0022-3476(70)80047-6/abstract)
- [OMIM #239300 HPMRS1](https://omim.org/entry/239300)
- [Orphanet ORPHA:247262](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=247262)
- [ClinVar VCV000001284 — PIGV p.Ala341Glu](https://www.ncbi.nlm.nih.gov/clinvar/variation/1284/)