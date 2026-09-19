---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-07-30T15:36:06.188374'
end_time: '2026-07-30T15:54:43.995167'
duration_seconds: 1117.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inclusion Body Myositis
  mondo_id: ''
  category: Autoimmune
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
  - claude-opus-5
  web_search_requests: 12
  num_turns: 41
  total_cost_usd: 4.353998
  session_id: 3e71a3c2-e1c7-459e-92ef-00b88b9f9332
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inclusion Body Myositis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Inclusion Body Myositis** covering all of the
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

# Comprehensive Research Report: Inclusion Body Myositis (IBM)

**Prepared:** 2026-07-30 · **Target KB entry:** `kb/disorders/Inclusion_Body_Myositis.yaml` · **MONDO:0007827**

> ### ⚠️ Evidence-verification notice (read before curating)
> Ontology identifiers in this report (MONDO, HP, GO, CL, UBERON, MAXO, HGNC) were **verified locally with OAK** against the repo's configured adapters and can be used as-is. PMIDs marked ✅ were **confirmed by direct NCBI E-utilities lookup** during this research (title/journal/year checked). Quoted abstract text was retrieved through a summarizing fetch layer, so **quotes in this report are candidate snippets, not validated ones** — every one must be re-fetched with `just fetch-reference PMID:XXXX` and confirmed as an exact substring via `just validate-references` before it enters a YAML `snippet:` field, per the repo SOP. Passages I could not confirm as verbatim are marked *(paraphrase — needs exact quote)*.
>
> ### ⚠️ Named Entity Confusion (NEC) hazard for this disease
> **"Inclusion body myositis" (IBM, MONDO:0007827) must not be conflated with "inclusion body myopathy"** — a different, genetically defined family of rimmed-vacuolar myopathies (GNE myopathy/hIBM2/DMRV, OMIM 605820, gene `GNE` = `hgnc:23657`; and VCP-related inclusion body myopathy with Paget disease and frontotemporal dementia / multisystem proteinopathy, gene `VCP` = `hgnc:12666`). Deep-research tools routinely blend these literatures because of the shared "IBM" acronym and shared rimmed-vacuole histology. This disease falls squarely in the **shared-acronym / shared-histology NEC risk class** described in `research/nec_risk_disease_classes.md`. Run the MONDO gene/OMIM/synonym preflight before importing any DR content.

---

## 1. Disease Information

### 1.1 Overview

Inclusion body myositis (IBM; sporadic IBM, sIBM) is a slowly progressive, acquired, late-onset skeletal muscle disease and **the most common acquired myopathy in people over 50 years of age**. It is unique among the idiopathic inflammatory myopathies (IIMs) in combining two co-existing pathological programs in the same myofibres:

1. an **autoimmune/inflammatory arm** — endomysial infiltration by highly differentiated cytotoxic CD8⁺ T cells that invade non-necrotic, MHC class I–overexpressing muscle fibres; and
2. a **myodegenerative arm** — rimmed vacuoles, protein aggregation (p62/SQSTM1, TDP-43, amyloid-β, ubiquitin), autophagy–lysosome dysfunction, and mitochondrial abnormalities (COX-negative fibres, mtDNA deletions).

Whether these arms are causally sequential (inflammation → degeneration), independent, or reciprocally reinforcing is **the central unresolved question of IBM pathogenesis** — an ideal candidate for a `mechanistic_hypotheses` block with competing `hypothesis_group_id` values in the KB entry.

MONDO definition (verified with OAK, `sqlite:obo:mondo`):

> "A slowly progressive degenerative inflammatory disorder of skeletal muscles characterized by late onset weakness of specific muscles and distinctive histopathological features." — MONDO:0007827 `def:` (source Orphanet:611)

The clinical signature is a **highly stereotyped, asymmetric, selective weakness pattern**: quadriceps femoris (knee extension) and deep finger flexors (flexor digitorum profundus), with early dysphagia and ankle dorsiflexor involvement. This pattern is so characteristic that it forms the backbone of every published diagnostic criteria set.

IBM is **refractory to all conventional immunosuppression** — a defining and clinically important negative feature that distinguishes it from dermatomyositis, immune-mediated necrotizing myopathy, and polymyositis, and that motivates the "degeneration-primary" hypothesis.

### 1.2 Key identifiers (all verified from the MONDO:0007827 record via OAK)

| Resource | Identifier |
|---|---|
| **Mondo** | `MONDO:0007827` — inclusion body myositis |
| OMIM | `OMIM:147421` (⚠️ note: this is a *phenotype/HLA-association* entry, not a Mendelian gene entry) |
| Orphanet | `ORPHA:611` |
| ICD-10-CM | `G72.41` |
| ICD-9-CM | `359.71` (also cross-referenced `729.1`) |
| MeSH | `D018979` (Myositis, Inclusion Body) |
| SNOMED CT | `72315009` |
| UMLS | `C0238190` |
| NCIT | `NCIT:C84786` |
| DOID | `DOID:3429` |
| EFO | `EFO:0007323` |
| MedGen | `68659` |
| MedDRA | `10066407` |
| GARD | `0003896` |
| NORD | `1734` |
| NANDO | `1200032`, `1200218` |
| MONDO parent | `is_a: MONDO:0021167` (myositis disease) |
| ICD-11 | Not carried as a MONDO xref — believed to be under `4A41` (idiopathic inflammatory myopathies). **Verify against the ICD-11 browser before asserting a specific code.** |

MONDO `subset:` flags include `rare`, `orphanet_rare`, `nord_rare`, `gard_rare` — IBM is formally a rare disease despite being the commonest myopathy of the elderly.

### 1.3 Synonyms (verified `synonym:` lines from MONDO)

- **IBM** (EXACT; OMIM:147421, Orphanet:611)
- **Sporadic Inclusion Body Myositis** (EXACT; NORD:1734, Orphanet:611)
- **sIBM** (EXACT; Orphanet:611)
- **sporadic inclusion body myositis** (EXACT; Orphanet:611)
- "inflammatory myopathy" (RELATED; GARD — **too broad; do not use as an exact synonym**)

Historic/literature synonyms not in MONDO: *inclusion body myositis, sporadic type*; *sIBM*. Historic misnomer to avoid: *"polymyositis with inclusion bodies."*

### 1.4 Information provenance

Information for this entry is predominantly **aggregated disease-level** (Orphanet, OMIM, ENMC consensus workshops, systematic reviews, registry/cohort studies). Two important **individual-patient / EHR-derived** sources exist and should be tagged as such:

- **Rochester Epidemiology Project (REP)** medical-records-linkage system, Olmsted County and 27 Minnesota/Wisconsin counties — the source of both the 2008 and 2021 US population-based epidemiology figures. This is genuine EHR-linkage data.
- **Swedish national cohort** (Lindgren et al., Ann Neurol 2022 ✅ PMID:35596584) — national registry/biopsy-registry derived.
- **MYOGEN / MYOVISION consortia** — patient-level genotype data underpinning the HLA association work.

---

## 2. Etiology

### 2.1 Overall causal model

**IBM has no single established cause.** It is best modeled in the KB as a **multifactorial, age-dependent disease** in which a permissive genetic background (dominantly HLA class II) plus profound age-associated immune remodeling (immunosenescence) permits a chronic, oligoclonal, cytotoxic T-cell attack on skeletal muscle, superimposed on (or triggering) a cell-autonomous proteostatic/mitochondrial failure in aging myofibres.

Two competing high-level hypotheses should be curated explicitly as `mechanistic_hypotheses` with `status: EMERGING` / `ALTERNATIVE`:

| Hypothesis id (suggested) | Claim | Principal supporting evidence |
|---|---|---|
| `autoimmune_primary` | IBM is fundamentally an autoimmune T-cell disease; degeneration is a downstream consequence of chronic cytotoxic attack and MHC-I–driven ER stress. | Oligoclonal, persistent, highly differentiated KLRG1⁺/CD57⁺ CD8⁺ T cells; HLA-DRB1*03:01 as the single strongest genetic risk factor; anti-cN1A autoantibodies; T-LGL leukaemia overlap. Greenberg SA, Nat Rev Rheumatol 2019 ✅ PMID:30837708 |
| `degeneration_primary` | A cell-autonomous myodegenerative process (proteostasis/autophagy/mitochondrial failure with TDP-43 loss-of-function) drives disease; inflammation is secondary/amplifying. | In the IBM xenograft model, **rimmed vacuoles and TDP-43 loss-of-function persisted after T-cell depletion**; complete failure of every immunosuppressive therapy tried. Britson KA et al., Sci Transl Med 2022 ✅ PMID:35044790 |

The Britson xenograft result is the single most probative experiment currently available and should be curated as an explicit edge-level qualifier: T-cell depletion in the model did **not** rescue the degenerative arm.

### 2.2 Genetic risk factors

**IBM is not a Mendelian disease and has no established causal gene.** Risk is conferred by common-variant susceptibility loci, overwhelmingly in the MHC.

| Locus / allele | Effect | Citation |
|---|---|---|
| **`HLA-DRB1*03:01`** (`hgnc:4948`) on the **8.1 ancestral haplotype** (HLA-A*01:01–B*08:01–C*07:01–DRB1*03:01–DRB3*01:01–DQA1*05:01–DQB1*02:01) | **The single strongest genetic risk factor for IBM.** High-resolution typing refines the signal to `DRB1*03:01:01`; reported ~**14-fold** increased risk in carriers, with onset ~**5 years earlier**. | Rothwell S et al., Arthritis Rheumatol 2017 ✅ PMID:28086002; high-resolution refinement, J Autoimmun 2024 ✅ PMID:38043487 |
| **DRβ1 position 74** | **Arginine-74 confers the allelic risk; glutamine-74 is protective** — an amino-acid-level, peptide-binding-groove mechanism (a genuine *protective* genetic factor for IBM). | ✅ PMID:38043487 |
| `HLA-DRB1*01:01`, `HLA-DRB1*13:01` | Additional independent HLA-DRB1 associations identified by imputation from GWAS SNP data in the MYOGEN Caucasian cohort. | ✅ PMID:28086002 |
| **Complement `C4A` (`hgnc:1323`) low copy number / C4A deficiency** | Low `C4` and `C4A` copy number are risk factors for myositis and its subgroups — the 8.1 AH itself carries a C4A-null allele, so this may be haplotype-linked rather than independent. | Zhou D et al., Ann Rheum Dis 2023 ✅ PMID:36171069 |
| Non-MHC loci | No robustly replicated genome-wide-significant non-MHC locus has been established for IBM. Candidate reports (e.g. `FYCO1`, `hgnc:14673`, an autophagy adaptor) are **not confirmed** and should be curated, if at all, with `supports: PARTIAL` and an explicit knowledge-gap discussion. | — |

**A note for curation:** `NT5C1A` (`hgnc:17819`, encoding cN1A / Mup44) is the **autoantigen**, not a risk gene. Do not model it as a causal gene; model it as an antigen target with `relationship_type` reflecting autoantigen status, and curate the antibody as a biomarker.

**Familial clustering:** Rare familial aggregation of *sporadic-type* IBM has been reported ("familial inflammatory IBM"), but this is distinct from the hereditary inclusion body *myopathies*. There is no established inheritance pattern.

### 2.3 Environmental / acquired risk factors

| Factor | Direction | Confidence |
|---|---|---|
| **Age > 50 years** (peak onset 60s–70s) | Strong risk | Established — the dominant risk factor |
| **Male sex** | Risk (M:F ≈ 2:1 to 3:1 in most cohorts) | Established |
| **Northern European / Caucasian ancestry** | Higher reported prevalence — but confounded by ascertainment and by 8.1 AH frequency, which itself tracks northern European ancestry | Moderate |
| **HIV-1 infection** | HIV-associated IBM-like myopathy is described; whether it is true IBM or a phenocopy is unsettled | Weak/uncertain |
| **HTLV-1 infection** | HTLV-1–associated inflammatory myopathy with IBM-like features reported in endemic regions | Weak/uncertain |
| **Hepatitis C virus** | Association reported in some case series | Weak |
| **Statin exposure** | Repeatedly raised as a possible unmasking/triggering factor; **not established**; a statin-associated IBM-like presentation is a recognized diagnostic confounder | Weak — curate as a `KNOWLEDGE_GAP` discussion rather than an asserted risk factor |
| Prior malignancy | Notably, **cancer incidence in sIBM did not differ from the general population** *(paraphrase — needs exact quote)* — unlike dermatomyositis, IBM is **not** a paraneoplastic disease. | ✅ PMID:33879596 |

There is **no established occupational, dietary, toxic, or radiation exposure** for IBM. This is an honest "not available" for the entry.

### 2.4 Protective factors

- **Genetic:** DRβ1 **glutamine at position 74** is reported protective (✅ PMID:38043487). This is a rare, well-specified genetic protective factor and is worth curating explicitly.
- **Environmental:** No validated environmental protective factor. Exercise (see §12) improves function but there is no evidence it prevents disease onset.

### 2.5 Gene–environment interactions

The most plausible G×E model — and one that should be curated as a hypothesis, not a fact — is that **HLA-DRB1*03:01-restricted presentation of a self- or pathogen-derived peptide to CD8⁺ T cells, in the setting of age-related immunosenescence and possible chronic viral (CMV/EBV/HIV) antigenic pressure, drives the clonal expansion of terminally differentiated cytotoxic effectors** that characterize IBM. Chronic CMV infection is a canonical driver of the CD28⁻/CD57⁺/KLRG1⁺ effector-memory phenotype seen in IBM blood and muscle, making CMV serostatus a natural G×E investigation target. No confirmatory human study establishes this chain — curate as `KNOWLEDGE_GAP` with `proposed_experiments`.

---

## 3. Phenotypes

### 3.1 Cardinal motor phenotypes

All HP identifiers below were verified with OAK (`sqlite:obo:hp`).

| Phenotype | HPO term | Typical frequency | Notes |
|---|---|---|---|
| **Quadriceps muscle weakness** | `HP:0003731` Quadriceps muscle weakness | Near-universal (~90–100%) | The defining proximal feature; knee-extension weakness disproportionate to hip flexion. Causes buckling and falls. |
| **Finger flexor weakness** (flexor digitorum profundus) | `HP:0031177` Finger flexor weakness | ~65–90% | The single most specific clinical sign; grip weakness with relative preservation of finger extension. Often asymmetric. |
| **Distal muscle weakness** | `HP:0002460` Distal muscle weakness; consider `HP:0009063` Progressive distal muscle weakness | Common | Distinctive: IBM has combined proximal *and* distal weakness, unlike most myopathies. |
| **Ankle dorsiflexor weakness / foot drop** | `HP:0003376` Steppage gait | ~30–50% | Tibialis anterior involvement (`UBERON:0001385`). |
| **Frequent falls** | `HP:0002359` Frequent falls (or `HP:0002527` Falls) | Very frequent | Direct consequence of quadriceps weakness; a major driver of morbidity and of fracture/head-injury complications. |
| **Quadriceps muscle atrophy** | `HP:0009050` Quadriceps muscle atrophy | Frequent | Visible thigh and forearm (volar) wasting. |
| **Asymmetry of weakness** | No single ideal HP term; describe in prose | Characteristic | Left–right asymmetry is a positive diagnostic feature and is unusual among myopathies. |

**Suggested descriptor qualifiers** (per repo conventions): use `clinical_course: PROGRESSIVE` and `temporality: CHRONIC` on the weakness descriptors, and `onset` with `onset_category` reflecting late-adult onset.

### 3.2 Bulbar phenotypes

| Phenotype | HPO term | Frequency | Notes |
|---|---|---|---|
| **Dysphagia** | `HP:0002015` Dysphagia; more specifically `HP:0200136` Oral-pharyngeal dysphagia or `HP:0002068` Neuromuscular dysphagia | **~40–80%; ~64% in a Mayo/REP cohort; ~2/3 in the 40-year population study** | Cricopharyngeal dysfunction with failure of upper-oesophageal-sphincter relaxation. **The dominant driver of mortality** via aspiration. Anti-cN1A positivity is associated with *more severe* dysphagia. |
| Feeding-tube dependence | consider `HP:0011968` Feeding difficulties + prose | Substantial minority (reported ~half in the REP cohort — *verify this figure carefully*, it is unusually high vs other series) | Gastrostomy (`MAXO:0001346`) |
| Facial weakness (mild) | `HP:0000317`-family / `HP:0030319` Weakness of facial musculature | Mild, in a minority | Severe facial weakness argues against IBM. |

Citations: ✅ PMID:33879596 (natural history/REP); Lindgren U et al. ✅ PMID:35596584; anti-cN1A/dysphagia association (PMC8151681 — resolve to a PMID before citing).

### 3.3 Laboratory phenotypes

| Phenotype | HPO term | Detail |
|---|---|---|
| **Elevated serum creatine kinase** | `HP:0003236` Elevated circulating creatine kinase concentration; often better captured by `HP:0008180` Mildly elevated creatine kinase | CK is **normal to modestly elevated**, typically <10–12× ULN and often <1000 U/L. A CK >2000 U/L should prompt reconsideration of the diagnosis. LOINC: 2157-6 (Creatine kinase [Enzymatic activity/volume] in Serum or Plasma). |
| **Anti-cN1A (anti-NT5C1A) autoantibody positivity** | `HP:0030057` Autoimmune antibody positivity (generic; no IBM-specific HP term exists — a genuine HPO gap worth noting) | See §10.2 for performance characteristics. |
| **Autoimmunity** (co-occurring) | `HP:0002960` Autoimmunity | Sjögren syndrome, sarcoidosis, autoimmune thyroid disease, and **T-cell large granular lymphocytic leukaemia** co-occur at elevated rates. |

### 3.4 Electrophysiological phenotypes

| Phenotype | HPO term | Detail |
|---|---|---|
| **Myopathic EMG** | `HP:0003458` EMG: myopathic abnormalities | Short-duration, low-amplitude, polyphasic motor unit potentials. **Short MUP duration correlated with all clinical measures** in a 50-patient series ✅ PMID:34617994. |
| Mixed myopathic/"neurogenic-appearing" units | prose | Long-duration, high-amplitude units co-exist in IBM (chronic myopathy with fibre splitting/regeneration) and are a classic pitfall leading to misdiagnosis as motor neuron disease. |
| Fibrillations/positive sharp waves | `HP:0030007`-family; consider prose | Common — reflects active fibre necrosis and denervation of split fibres. |

### 3.5 Histopathological phenotypes (biopsy-defined)

| Phenotype | HPO term | Detail |
|---|---|---|
| **Rimmed vacuoles** | `HP:0003805` Rimmed vacuoles | Basophilic-rimmed autophagic vacuoles on modified Gomori trichrome. Specific but **not sensitive** — absent in a substantial fraction of clinically definite IBM biopsies, especially early. |
| **Cytochrome c oxidase–negative muscle fibres** | `HP:0003688` Cytochrome C oxidase-negative muscle fibers | Reported as the **second most common histopathological finding** in IBM; in inflammatory myopathy *without* rimmed vacuoles, COX-deficient fibres were reported **100% sensitive and 73% specific** for IBM *(paraphrase — needs exact quote and primary-source PMID)*. Associated with **somatic mtDNA deletions**. |
| **Ragged-red fibres** | `HP:0003200` Ragged-red muscle fibers | Mitochondrial pathology marker. |
| **Increased endomysial connective tissue** | `HP:0100297` Increased endomysial connective tissue | Endomysial fibrosis with disease progression. |
| Endomysial CD8⁺ T-cell infiltration invading non-necrotic MHC-I⁺ fibres | No HP term; curate as pathophysiology + `histopathology` | **The defining immunopathological lesion.** |
| p62/SQSTM1⁺, TDP-43⁺, ubiquitin⁺, amyloid-β⁺ cytoplasmic inclusions | No HP term; curate as pathophysiology | See §6. Note Greenberg's caution that aggregates are present in **<1% of myofibres** — a quantitative argument against aggregate-primacy. |

### 3.6 Phenotype characteristics summary

- **Age of onset:** adult/late-onset; mean onset ~60–70 years; onset before 45 is rare and should trigger reconsideration. HPO onset term: `HP:0003584` Late onset (verify) or `HP:0003581` Adult onset.
- **Severity:** moderate → severe over decades; universally disabling if survival is long enough.
- **Progression:** **relentlessly progressive**; never episodic, never relapsing-remitting, spontaneous remission essentially unreported.
- **Frequency among affected individuals:** quadriceps and finger-flexor weakness near-universal by the time of diagnosis; dysphagia in the majority eventually.

### 3.7 Quality-of-life impact (per phenotype)

- **Quadriceps weakness →** loss of stair climbing, rising from a chair, and independent ambulation; falls and fall-related fractures; median **time to wheelchair dependence ≈ 10.5 years (range 1–29)** ✅ PMID:33879596. Other series quote wheelchair dependence "on average, 12–20 years after onset" ✅ PMID:25215417.
- **Finger flexor weakness →** loss of grip: buttons, keys, jar opening, writing, holding utensils; disproportionate impact on independence relative to strength loss.
- **Dysphagia →** aspiration fear, meal-time anxiety, social withdrawal from eating, weight loss, PEG dependence; the phenotype most strongly linked to mortality.
- No IBM-specific QoL instrument is standard. Instruments used: **IBMFRS (IBM Functional Rating Scale)** — the field's primary functional outcome and the primary endpoint in the ulviprubart and sirolimus trials; **SF-36**; **HAQ**; **6-minute walk distance (6MWD)** — primary endpoint of RESILIENT. See ✅ PMID:22588740 (Arthritis Care Res 2011 myositis outcome-measures compendium) for the catalogue.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

**None.** IBM has **no causal gene** and no established Mendelian inheritance. This should be stated affirmatively in the entry — it is the key discriminator from the hereditary inclusion body myopathies. `OMIM:147421` exists but describes an HLA-associated susceptibility phenotype, not a gene–disease relationship. There is **no ClinGen Gene-Disease Validity assertion** establishing a definitive gene for sporadic IBM (a `CGGV:` query is worth running to confirm and to cite the absence).

### 4.2 Susceptibility / risk genes (curate with `relationship_type: SUSCEPTIBILITY`)

| Gene | HGNC (OAK-verified) | Role |
|---|---|---|
| `HLA-DRB1` | `hgnc:4948` | `*03:01:01` risk allele; DRβ1 Arg74 risk / Gln74 protective |
| `C4A` | `hgnc:1323` | Low copy number / null allele — myositis risk (8.1-AH-linked) |
| `NT5C1A` | `hgnc:17819` | **Autoantigen (cN1A/Mup44)**, not a risk gene — curate as antigen |
| `TARDBP` | `hgnc:11571` | Encodes TDP-43; **not mutated in sIBM** — the pathology is mislocalization/loss-of-function, not a coding variant |
| `SQSTM1` | `hgnc:11280` | Encodes p62; aggregate constituent, not mutated in sIBM |
| `APP` | `hgnc:620` | Amyloid-β precursor; aggregate constituent, not mutated in sIBM |
| `KLRG1` | `hgnc:6380` | Marker of the pathogenic T-cell population and the therapeutic target of ulviprubart |
| `MSTN` | `hgnc:4223` | Myostatin — therapeutic target (ActRII/bimagrumab axis), not a risk gene |
| `STAT3` | `hgnc:11364` | Somatic gain-of-function mutations in the clonally expanded LGL population (see §4.5) |

**Genes to explicitly exclude** (NEC guard, curate as `notes` or a `discussions` entry): `GNE` (`hgnc:23657`) and `VCP` (`hgnc:12666`) cause *hereditary inclusion body myopathies*, **not** IBM.

### 4.3 Pathogenic variants

Not applicable in the ACMG/AMP sense — there are no pathogenic germline variants for IBM. The relevant genetic architecture is **common HLA haplotype variation** with population allele frequencies available in the Allele Frequency Net Database and gnomAD (HLA imputation). `HLA-DRB1*03:01` carrier frequency in northern European populations is roughly 20–25%, consistent with a common susceptibility allele of moderate-to-large effect rather than a rare pathogenic variant.

### 4.4 Somatic genetic changes

- **Mitochondrial DNA deletions** — clonally expanded, large-scale mtDNA deletions accumulate in COX-negative myofibre segments. These are **somatic, muscle-restricted, and clonally expanded within individual fibre segments**, closely resembling the mtDNA pathology of normal aging muscle but present in far greater abundance. This is a genuine somatic-mutation mechanism worth its own pathophysiology node.
- **`STAT3` gain-of-function somatic mutations** in circulating clonal large granular lymphocytes (see §4.5).

### 4.5 The IBM / T-LGL leukaemia overlap (a major, under-appreciated finding)

Greenberg SA et al., *Brain* 2016 ✅ PMID:26920676 reported that:

> "Most (22 of 38; 58%) patients with inclusion body myositis had aberrant populations of large granular lymphocytes in their blood meeting standard diagnostic criteria for T cell large granular lymphocytic leukaemia, and these T cell populations were clonal in 20 of 20 patients and stably present on follow-up testing." *(candidate quote — verify verbatim)*

`STAT3` gain-of-function mutations, the molecular hallmark of T-LGL leukaemia, are present in ~21–75% of T-LGL cohorts and drive constitutive STAT3 activation → enhanced survival and **defective activation-induced cell death** of the cytotoxic clone. This provides a mechanistically satisfying explanation for why the IBM T-cell attack is *persistent and immunosuppression-resistant*: the effector cells are a long-lived, apoptosis-resistant clone, not a conventional activated T-cell response. This deserves an explicit pathophysiology node and should be linked to a comorbidity entry for T-LGL leukaemia.

### 4.6 Modifier genes

- `HLA-DRB1*03:01:01` acts as an **age-of-onset modifier** (~5 years earlier onset in carriers) ✅ PMID:38043487 — a clean `MODIFIER` relationship.
- Anti-cN1A antibody status behaves as a **severity modifier** (more severe dysphagia, possibly worse survival) but is serological, not genetic.

### 4.7 Epigenetics

No robust, replicated DNA-methylation or histone-modification signature is established for IBM. Muscle transcriptomic studies consistently show a **type II interferon (IFN-γ) signature** rather than the type I IFN signature of dermatomyositis — this is transcriptional, not confirmed epigenetic. Honest gap: **not available**; curate as `KNOWLEDGE_GAP`.

### 4.8 Chromosomal abnormalities

None associated with IBM. CMA/karyotype/FISH have **no diagnostic role**. Explicitly "not applicable."

---

## 5. Environmental Information

- **Environmental toxins / occupational exposure / radiation:** No established association. CTD/TOXNET yield no validated IBM-toxicant links. **Not available.**
- **Lifestyle factors:** No established dietary, smoking, or alcohol association. Physical inactivity worsens deconditioning but is not aetiological.
- **Drugs:** Statins are the recurrently discussed but unproven exposure (see §2.3). Statin-associated autoimmune myopathy (anti-HMGCR) is a distinct entity and a key differential.
- **Infectious agents (all speculative/associative, none causal):**
  - **HIV-1** (`NCBITaxon:11676`) — HIV-associated IBM-like myopathy
  - **HTLV-1** (`NCBITaxon:11908`) — HTLV-1–associated inflammatory myopathy with IBM features
  - **HCV** (`NCBITaxon:11103`) — reported association
  - **Human cytomegalovirus** (`NCBITaxon:10359`) — not causal, but the canonical driver of the terminally differentiated CD8⁺CD28⁻CD57⁺KLRG1⁺ T-cell compartment that IBM's effector cells resemble; mechanistically the most interesting candidate for a G×E study.

  Curate these with `supports: PARTIAL` or as `discussions` — **none meets a causal-agent bar.**

---

## 6. Mechanism / Pathophysiology

### 6.1 Proposed causal chain (upstream → downstream)

Below is a node chain suitable for direct translation into `pathophysiology:` entries, with `biological_scale:` tags per the repo's single-value discipline.

**Node 1 — Permissive genetic background and immunosenescence** (`biological_scale: ORGANISM`)
HLA-DRB1*03:01:01 (Arg74 in the DRβ1 peptide-binding groove) + age-associated contraction of the naïve T-cell repertoire and expansion of terminally differentiated effectors.
→ *downstream:* Node 2

**Node 2 — Clonal expansion of highly differentiated cytotoxic CD8⁺ T cells** (`biological_scale: CELLULAR`)
CD8⁺CD57⁺CD28⁻**KLRG1⁺** effector-memory/TEMRA cells with NK-like features; oligoclonal by TCR sequencing; persistent over years; frequently meeting T-LGL leukaemia criteria; `STAT3`-GOF-driven resistance to activation-induced cell death.
- Cell type: `CL:0000794` CD8-positive, alpha-beta cytotoxic T cell
- GO: `GO:0001913` T cell mediated cytotoxicity; `GO:0043316` cytotoxic T cell degranulation
- Gene: `KLRG1` (`hgnc:6380`), `STAT3` (`hgnc:11364`)
→ *downstream:* Node 4

**Node 3 — Myofibre MHC class I overexpression** (`biological_scale: CELLULAR`)
IFN-γ–driven, widespread sarcolemmal and sarcoplasmic MHC-I upregulation on non-necrotic fibres — both the antigen-presentation substrate and, independently, a cell-intrinsic ER stressor.
- Cell type: `CL:0008002` skeletal muscle fiber
- GO: `GO:0002484` antigen processing and presentation of endogenous peptide antigen via MHC class I via ER pathway
→ *downstream:* Nodes 4 and 5

**Node 4 — Cytotoxic invasion of non-necrotic myofibres** (`biological_scale: CELLULAR`)
Perforin/granzyme-mediated attack; the pathognomonic "partial invasion" lesion. Accompanied by endomysial macrophages (`CL:0000235`) and plasma cells (`CL:0000786`; local Ig production supports a B-cell/plasma-cell arm and the origin of anti-cN1A).
- GO: `GO:0001913` T cell mediated cytotoxicity
→ *downstream:* Node 8

**Node 5 — ER stress / unfolded protein response** (`biological_scale: MOLECULAR`)
MHC-I overload and misfolded-protein burden activate the UPR (PERK/ATF6/IRE1), amplifying NF-κB signalling and further MHC-I expression — a **feed-forward loop**.
- GO: `GO:0034976` response to endoplasmic reticulum stress
→ *downstream:* Nodes 6 and 3 (feedback edge)

**Node 6 — Autophagy–lysosome pathway failure and protein aggregation** (`biological_scale: CELLULAR`)
Impaired autophagic flux and chaperone-mediated autophagy; accumulation of p62/SQSTM1, ubiquitin, LC3, amyloid-β/APP-derived species, and phosphorylated tau in aggregates; formation of rimmed vacuoles (autophagic vacuoles with myeloid debris).
- GO: `GO:0006914` autophagy; `GO:0061684` chaperone-mediated autophagy; `GO:0070841` inclusion body assembly; `GO:0043161` proteasome-mediated ubiquitin-dependent protein catabolic process; `GO:0042026` protein refolding (the arimoclomol/HSP rationale)
- Genes/proteins: `SQSTM1` (`hgnc:11280`), `APP` (`hgnc:620`)
- Phenotype: `HP:0003805` Rimmed vacuoles
→ *downstream:* Node 8
> **Greenberg's caveat to curate honestly:** aggregates are present in **"<1% of myofibres in patients with IBM"** ✅ PMID:30837708 *(candidate quote — verify)*, which is a strong quantitative argument that aggregates are a marker rather than the primary driver.

**Node 7 — TDP-43 nuclear clearance, cytoplasmic aggregation, and loss of splicing repression** (`biological_scale: MOLECULAR`)
Nuclear loss + cytoplasmic mislocalization of TDP-43 (`TARDBP`, `hgnc:11571`) with **cryptic exon inclusion** in TDP-43 target transcripts — a molecular convergence with ALS/FTD. This is now the most mechanistically specific molecular lesion in IBM and a candidate biomarker (cryptic-exon-derived peptides/transcripts).
- Critically: in the xenograft model, **"Loss of TDP-43 function and rimmed vacuoles persist after T cell depletion"** ✅ PMID:35044790 — i.e., this arm is at least partly T-cell–independent.
→ *downstream:* Node 8

**Node 8 — Mitochondrial dysfunction** (`biological_scale: CELLULAR`)
COX-negative fibres, ragged-red fibres, clonally expanded somatic mtDNA deletions, impaired oxidative phosphorylation, ROS generation. Mechanistically linked to TDP-43 (TDP-43 associates with mitochondria and its dysfunction impairs mitochondrial function) and plausibly to chronic inflammatory/nitrosative stress.
- Phenotypes: `HP:0003688` Cytochrome C oxidase-negative muscle fibers; `HP:0003200` Ragged-red muscle fibers
- GO: `GO:0000422` autophagy of mitochondrion (mitophagy)
→ *downstream:* Node 9

**Node 9 — Myofibre degeneration, atrophy, and failed regeneration** (`biological_scale: TISSUE`)
Fibre necrosis, atrophy, splitting, endomysial fibrosis (`HP:0100297`), and exhaustion/impaired activation of satellite cells (`CL:0000594` skeletal muscle satellite cell; `CL:0008016` activated skeletal muscle satellite cell). Fatty and fibrous replacement visible on MRI.
- GO: `GO:0043403` skeletal muscle tissue regeneration
→ *downstream:* Node 10

**Node 10 — Selective, asymmetric muscle weakness and dysphagia** (`biological_scale: ORGANISM`)
Clinical phenotype (§3). Why quadriceps and FDP are selectively vulnerable remains **unexplained** — an excellent, well-defined `KNOWLEDGE_GAP` for the entry.

### 6.2 Molecular pathways

- **IFN-γ / JAK-STAT1** — the dominant muscle transcriptomic signature (type II IFN, distinguishing IBM from the type I IFN signature of dermatomyositis). KEGG hsa04630, Reactome "Interferon gamma signaling."
- **NF-κB** — downstream of ER stress and inflammatory cytokines; drives MHC-I and cytokine expression.
- **mTOR / autophagy** — the rationale for sirolimus; mTORC1 inhibition promotes autophagic clearance *and* preferentially spares/expands regulatory T cells while depleting effector-memory T cells.
- **Heat-shock response / proteostasis** — the rationale for arimoclomol (HSP co-inducer).
- **Myostatin–ActRII–SMAD2/3** — the rationale for bimagrumab (anti-ActRII antibody), aimed at the atrophy arm rather than causation.
- **TDP-43 splicing repression / cryptic exon inclusion** — shared with ALS/FTD.
- **STAT3** — clonal LGL survival.

### 6.3 Cell types involved (CL terms, OAK-verified)

| Cell type | CL term | Role |
|---|---|---|
| CD8⁺ αβ cytotoxic T cell | `CL:0000794` | Primary effector; KLRG1⁺CD57⁺CD28⁻ terminally differentiated subset |
| Skeletal muscle fibre | `CL:0008002` | Target cell; MHC-I⁺, aggregate-bearing, vacuolated |
| Macrophage | `CL:0000235` | Endomysial infiltrate component |
| Plasma cell | `CL:0000786` | Local Ig/autoantibody production in muscle |
| Skeletal muscle satellite cell | `CL:0000594` (also `CL:0008016` activated) | Failed/exhausted regeneration |

### 6.4 Anatomical and subcellular localization

- Tissue: `UBERON:0001134` skeletal muscle tissue (verify exact ID before use — OAK returned `UBERON:0014892` skeletal muscle organ, vertebrate for the organ-level query); `UBERON:0004498` skeletal muscle tissue of quadriceps femoris; `UBERON:0004499` skeletal muscle tissue of tibialis anterior; `UBERON:0001523` flexor digitorum profundus; `UBERON:0000933` chordate pharyngeal muscle.
- Subcellular (GO CC): sarcoplasm/cytoplasm, `GO:0005634` nucleus (TDP-43 clearance), `GO:0005739` mitochondrion, `GO:0005764` lysosome / `GO:0005776` autophagosome, `GO:0005783` endoplasmic reticulum, `GO:0016235` aggresome (verify), `GO:0042612` MHC class I protein complex (verify).

### 6.5 Molecular profiling

- **Transcriptomics:** Muscle RNA-seq consistently shows a **type II interferon-dominant** signature with strong upregulation of MHC-I/II, immunoproteasome subunits, chemokines (CXCL9/10), and Ig genes; plus downregulation of oxidative-phosphorylation and mitochondrial transcripts. Search GEO for `sporadic inclusion body myositis` muscle series to populate a `datasets:` block.
- **Cryptic exon transcriptomics:** TDP-43 loss-of-function–dependent cryptic exons are detectable in IBM muscle (✅ PMID:35044790) — the most disease-specific transcriptomic readout available.
- **Proteomics:** Aggregate-enriched proteomics identifies p62, TDP-43, ubiquitin, amyloid-β, phosphorylated tau, myotilin, αB-crystallin, and cN1A. PRIDE/ProteomeXchange hold relevant datasets.
- **Single-cell / TCR-seq:** scRNA-seq + TCR-seq of muscle-infiltrating and blood T cells is the most active current frontier and directly underpins the KLRG1-targeting therapeutic strategy. Frontiers Immunol 2023 study of expanded CD8⁺ LGLs in IBM correlates T-cell phenotype with disease severity (PMC10098158 — resolve to PMID before citing).
- **Metabolomics/lipidomics:** **Not available** — no established IBM signature.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ:** skeletal muscle (`UBERON:0014892` skeletal muscle organ, vertebrate). Body system: musculoskeletal.
- **Secondary/complication organs:** lung (aspiration pneumonia, respiratory failure — the leading cause of death); pharynx/upper oesophagus (cricopharyngeus); rarely heart (cardiac involvement is **not** a feature of IBM — an important negative); peripheral nerve is **spared** (nerve conduction studies are normal).

### Selective muscle involvement — the diagnostic signature
| Muscle | UBERON | Involvement |
|---|---|---|
| Quadriceps femoris | `UBERON:0001377` (tissue: `UBERON:0004498`) | Severe, early. On MRI, **vastus lateralis and vastus intermedius are affected earliest and most severely while rectus femoris is relatively spared** — an MRI signature of high diagnostic value. |
| Flexor digitorum profundus | `UBERON:0001523` | Severe, early; **highly specific** |
| Tibialis anterior | `UBERON:0001385` (tissue: `UBERON:0004499`) | Frequent (foot drop) |
| Pharyngeal / cricopharyngeal muscle | `UBERON:0000933` chordate pharyngeal muscle | Dysphagia |
| **Relatively spared:** deltoid, finger extensors, facial muscles (mild at most), ocular muscles (**never** — ophthalmoparesis excludes IBM), cardiac muscle | — | Negative discriminators |

### Lateralization
**Asymmetric** — a positive diagnostic feature. Weakness is characteristically worse on one side, unusual for a myopathy and a reason IBM is frequently misdiagnosed as motor neuron disease or a radiculopathy.

### Tissue/cell level
Striated skeletal muscle tissue; myofibres (`CL:0008002`) as targets; endomysial compartment as the site of the inflammatory infiltrate (endomysial, **not** perimysial or perivascular — the latter patterns indicate dermatomyositis). Satellite cells (`CL:0000594`) show impaired regenerative capacity.

### Subcellular
Nucleus (TDP-43 clearance), cytoplasm/sarcoplasm (aggregates), lysosome/autophagosome (rimmed vacuoles), mitochondria (COX-negative segments, mtDNA deletions), ER (UPR), sarcolemma (MHC-I).

---

## 8. Temporal Development

### Onset
- **Typical age:** adult/late — most series report mean onset **~60–70 years**; onset before age 45 is distinctly unusual.
- **Onset pattern:** **insidious**, over months to years. Patients typically report a long prodrome of falls, difficulty rising from chairs, or dropping objects.
- **Diagnostic delay:** notoriously long — commonly **5+ years** from symptom onset to diagnosis, because early asymmetric weakness is misattributed to orthopaedic causes, radiculopathy, or motor neuron disease.

### Progression
- **Course:** **relentlessly, slowly progressive**; never relapsing-remitting; spontaneous remission not described.
- **Rate:** IBMFRS declines ~1–2 points/year in natural-history and placebo-arm data; quantitative strength declines ~3–5%/year. Slow enough that trials require 12–20+ months and large N to detect an effect — the central trial-design problem in IBM.
- **Milestones:** median **time to wheelchair dependence 10.5 years (range 1–29)** ✅ PMID:33879596; other cohorts report 12–20 years ✅ PMID:25215417. Assistive-device use typically precedes this by several years.
- **Duration:** chronic, lifelong.
- **Staging:** No formal consensus staging system. The 272nd ENMC workshop (✅ PMID:38522330) explicitly addressed **clinical trial readiness** and outcome measures; the working stratification used in trials is **mild/moderate vs advanced disease**, and the ulviprubart MUSCLE result (§12) makes this stratification clinically consequential.

### Patterns
- **Remission:** none, spontaneous or treatment-induced. This is a defining negative.
- **Critical window:** The strongest current signal for a therapeutic window is the **MUSCLE trial's mild-to-moderate subgroup**, where ulviprubart showed favourable trends absent in the full population — supporting a "treat early, before irreversible fibro-fatty replacement" model. **Curate this as an emerging hypothesis, not an established fact.**

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Estimate | Source |
|---|---|---|
| **Prevalence, ≥50 years (US, Olmsted/REP, 2010)** | **18.20 per 100,000 people ≥50 years old** | ✅ PMID:33879596 *(candidate quote — verify)* |
| Prevalence, all-ages (US, REP, age/sex-adjusted) | **7.06 per 100,000** (95% CI 0.87–13.24) | ✅ PMID:18203321 / REP series |
| Incidence, all-ages (US, REP, age/sex-adjusted) | **0.79 per 100,000/year** (95% CI 0.24–1.35) | ✅ PMID:18203321 |
| Older/lower literature estimates | incidence ~0.22/100,000; prevalence 0.49–1.07/100,000 | Historical — **underestimates due to under-ascertainment**; do not present as current |
| IIM group context | Incidence of inflammatory myopathies 1.16–19 per million/year; prevalence 2.4–33.8 per 100,000 | Meyer A et al., Rheumatology 2015 ✅ PMID:25065005 |
| Sweden, national cohort | Epidemiology, survival, and clinical characteristics reported nationally | Lindgren U et al., Ann Neurol 2022 ✅ PMID:35596584 |

**Curation guidance:** use the structured `Prevalence` slots. For the 18.20/100,000 figure: `population: "United States (Olmsted County/REP), adults ≥50 years"`, `measure_type: POINT_PREVALENCE`, `prevalence_class: BAND_1_5_PER_10000` (18.2/100,000 = 1.82/10,000 → falls in the 1–5/10,000 band), `rate_per_100000: 18.2`. For the all-ages figure: `rate_per_100000: 7.06`, `rate_low: 0.87`, `rate_high: 13.24`, `prevalence_class: BAND_1_9_PER_100000`. **Never compare the ≥50 figure to the all-ages figure** — different denominators.

Notably, prevalence of sIBM **correlated with the population frequency of HLA-DR3** across studies (✅ PMID:25065005) — an elegant ecological confirmation of the 8.1-AH association and worth curating.

### 9.2 Inheritance

- **Inheritance pattern:** **Not Mendelian.** Multifactorial/complex, with a dominant common-variant HLA contribution. Do **not** assign an HPO mode-of-inheritance term implying Mendelian transmission. If any inheritance block is used, `HP:0010982` Polygenic inheritance with `relationship_type: SUSCEPTIBILITY` gene typing is the most defensible, and even that overstates the evidence — consider omitting the `inheritance:` block entirely and stating the absence in `notes`.
- **Penetrance / expressivity / anticipation / mosaicism / consanguinity / carrier frequency:** **Not applicable.** Explicitly state this; these are the fields DR tools most often hallucinate for IBM by importing GNE-myopathy content.
- **Founder effects:** None for IBM. (Founder effects *do* exist for GNE myopathy — e.g. the Persian-Jewish M712T founder allele — and this is a classic NEC contamination vector. **Do not import it.**)

### 9.3 Population demographics

- **Sex ratio:** **male predominance, ~2:1 to 3:1 (M:F)** — the only IIM with male predominance (dermatomyositis, ASyS, and IMNM are female-predominant). A useful discriminating epidemiological feature.
- **Ethnicity:** Highest reported prevalence in populations of **northern European ancestry**, tracking 8.1-AH frequency; IBM is reported but less frequently ascertained in East Asian, African, and Latin American populations. Ascertainment bias is a real confounder — flag it.
- **Geography:** Reported worldwide; highest measured rates from Scandinavia, the Netherlands, the UK, Australia, and the US Midwest — regions with both high 8.1-AH frequency **and** good neuromuscular ascertainment.
- **Age distribution:** Sharply skewed to ≥50 years, peaking in the 7th–8th decades.

---

## 10. Diagnostics

### 10.1 Clinical diagnostic criteria

| Criteria set | Citation | Notes |
|---|---|---|
| **Griggs criteria (1995)** | Griggs RC et al., Ann Neurol 1995 | The original pathology-anchored criteria; highly specific, poorly sensitive (require all four canonical biopsy features). |
| **ENMC 2011 (published 2013)** | **Rose MR & ENMC IBM Working Group**, *Neuromuscul Disord* 2013;**23**(12):1044–55 — ✅ **PMID:24268584** | Introduced "clinico-pathologically defined IBM," "clinically defined IBM," and "probable IBM"; the most widely used set for a decade. |
| **Lloyd data-derived criteria (2014)** | **Lloyd TE et al.**, *Neurology* 2014 — ✅ **PMID:24975859** | Machine-learning evaluation of **24 published criteria sets against 371 patients**. Reported: ENMC criteria performed best among published sets; **data-derived criteria achieved "90% sensitivity and 96% specificity"** *(candidate quote — verify)*. The best-performing simple rule combines **finger-flexor OR knee-extension weakness** with characteristic biopsy features. |
| **272nd ENMC workshop (2023, published 2024)** | *Neuromuscul Disord* 2024;**37**:36–51 — ✅ **PMID:38522330** | "10 Years of progress — revision of the ENMC 2013 diagnostic criteria for inclusion body myositis and clinical trial readiness." Incorporates **muscle MRI/ultrasound** and **anti-cN1A serology** as novel diagnostic tools, and addresses outcome measures and trial readiness. **This is the current reference standard and should be the entry's primary `definitions:` citation.** |

Suggested `definitions[]` shape: `definition_type: DIAGNOSTIC_CRITERIA` (or the repo's nearest value), `derivation_basis: ESTABLISHED_CRITERIA`, citing PMID:38522330 with PMID:24268584 and PMID:24975859 as predecessors.

### 10.2 Serological biomarker: anti-cN1A / anti-NT5C1A

The only IBM-associated autoantibody. Target: cytosolic 5′-nucleotidase 1A (cN1A / Mup44), encoded by `NT5C1A` (`hgnc:17819`).

- **Discovery:** Larman HB et al., *Ann Neurol* 2013 — ✅ **PMID:23596012** — "Cytosolic 5′-nucleotidase 1A autoimmunity in sporadic inclusion body myositis." Reported: **"Moderate reactivity of anti-cN1A autoantibodies was 70% sensitive and 92% specific"** and **"high reactivity was 34% sensitive and 98% specific"** *(candidate quotes — verify verbatim; these are the numbers most worth getting exactly right)*. Independently and near-simultaneously reported by Pluk H et al. (Ann Neurol 2013).
- **Isotype work:** Herbert MK et al. — ✅ **PMID:24752512** — "Cytoplasmic 5′-nucleotidase autoantibodies in inclusion body myositis: isotypes and diagnostic utility." **Combination assays measuring all three isotypes (IgM, IgA, IgG) improved sensitivity to 76%.**
- **Meta-analytic performance:** sensitivity **33–76%**, specificity **87–100%** across studies; variability driven by assay platform and cut-off. One Italian cohort: sensitivity 37.1%, specificity 96.8%. A single-centre 40-patient series: sensitivity 50% — ✅ **PMID:30001928**.
- **Clinical utility summary:** ✅ **PMID:31024569** — "Anti-NT5c1A autoantibodies as biomarkers in inclusion body myositis."
- **Interpretation for the KB:** **Moderate sensitivity, high specificity, poor PPV in low-prevalence settings** (one study: PPV 0.29, NPV 0.96). Anti-cN1A is **not disease-specific** — it occurs in Sjögren syndrome and SLE — so a positive result outside a compatible clinical phenotype does not establish IBM. Positivity is associated with **more severe dysphagia**.
- **Reference range curation:** anti-cN1A is qualitative/semi-quantitative and assay-dependent; a `reference_ranges` block is **not appropriate** here. Curate as a phenotype/biomarker with prose interpretation instead.

### 10.3 Laboratory tests

- **Serum CK** (LOINC 2157-6): normal to mildly/moderately elevated, usually <10–12× ULN. `HP:0008180` Mildly elevated creatine kinase. A markedly elevated CK argues for IMNM or dystrophy instead.
- Aldolase, AST/ALT (muscle-derived), LDH: mildly elevated.
- **Myositis-specific antibody panel:** should be **negative** for anti-Jo-1/ARS, anti-Mi-2, anti-TIF1-γ, anti-NXP2, anti-MDA5, anti-SRP, anti-HMGCR. A positive MSA points away from IBM.
- **Peripheral blood flow cytometry / TCR clonality:** given the T-LGL overlap (✅ PMID:26920676), flow cytometry for aberrant CD8⁺CD57⁺ LGL populations and TCR-β clonality is an underused, mechanistically informative test.
- HIV, HTLV-1, HCV serology: to exclude infection-associated myopathy.
- TSH, vitamin D: to exclude reversible myopathies.

### 10.4 Imaging

**Muscle MRI** is now formally part of the diagnostic algorithm (✅ PMID:38522330). Characteristic findings:
- Fatty infiltration (T1) and oedema (STIR/T2 fat-sat) in **anterior thigh** with **vastus lateralis and vastus intermedius affected earlier/more severely than rectus femoris**;
- **Medial gastrocnemius** involvement in the lower leg;
- **Forearm deep flexor compartment** (FDP) involvement.
This pattern is sufficiently distinctive that whole-body muscle MRI can support diagnosis in biopsy-negative cases. RadLex/DICOM applicable. **Muscle ultrasound** (increased echo intensity in the same distribution) is a cheaper, bedside alternative endorsed by the 272nd ENMC workshop.

MAXO: consider `MAXO:0035082` barium swallow radiograph procedure for the swallowing evaluation (see below).

### 10.5 Electrophysiology

- **Needle EMG:** myopathic MUPs (`HP:0003458`) with abundant fibrillation potentials; a **mixed myopathic/large-unit pattern** is characteristic and a classic source of misdiagnosis as ALS. **Short MUP duration correlated with all clinical measures** in a 50-patient series ✅ PMID:34617994.
- **Nerve conduction studies:** normal or mild age-related changes — used to **exclude** neuropathy/motor neuron disease.

### 10.6 Muscle biopsy (the historical gold standard)

Site selection matters: biopsy an affected but not end-stage muscle (commonly vastus lateralis or biceps; **avoid** severely atrophic muscle, which yields only fibro-fatty tissue).

Canonical findings:
1. **Endomysial inflammatory infiltrate with CD8⁺ T-cell invasion of non-necrotic fibres** (the immunological hallmark);
2. **Sarcolemmal/sarcoplasmic MHC class I overexpression** (immunohistochemistry) — highly sensitive, present even when infiltrate is sparse;
3. **Rimmed vacuoles** (`HP:0003805`) on modified Gomori trichrome — specific, insensitive;
4. **Mitochondrial pathology**: COX-negative fibres (`HP:0003688`), ragged-red fibres (`HP:0003200`), SDH-positive/COX-negative fibres on dual staining;
5. **Protein aggregates**: p62/SQSTM1 (the most practical and sensitive aggregate stain), TDP-43 (cytoplasmic, with nuclear clearance), ubiquitin, amyloid-β (Congo red/crystal violet — technically demanding, poor reproducibility);
6. **Increased endomysial connective tissue** (`HP:0100297`).

Important: **absence of rimmed vacuoles does not exclude IBM**. COX-deficient fibres and p62/TDP-43 immunostaining rescue many vacuole-negative biopsies. In inflammatory myopathy without rimmed vacuoles, COX-deficient fibres were reported **100% sensitive and 73% specific** for IBM *(paraphrase — locate and verify the primary source)*.

### 10.7 Swallow assessment

Videofluoroscopic swallow study / modified barium swallow (`MAXO:0035082` barium swallow radiograph procedure) and fibreoptic endoscopic evaluation of swallowing (FEES); manometry to document cricopharyngeal non-relaxation. Speech-language pathologist evaluation: `MAXO:0000733`.

### 10.8 Genetic testing

**Genetic testing has no role in diagnosing sporadic IBM**, and this negative should be stated explicitly. Its role is **exclusionary**, to rule out mimics with rimmed vacuoles or late-onset selective weakness:
- `GNE` sequencing (GNE myopathy — spares quadriceps, a key clinical discriminator);
- `VCP` (multisystem proteinopathy/IBMPFD — look for Paget disease, FTD, family history);
- `MYH2`, `DES`, `MATR3`, `SQSTM1`, `HNRNPA1/A2B1`, `TIA1` (rimmed-vacuolar myopathies);
- `DMPK` CTG repeat (myotonic dystrophy type 1 — distal weakness, but with myotonia and multisystem features);
- `GAA` (late-onset Pompe disease — a **treatable** mimic; dried blood spot enzyme assay is the first-line test and should be done in essentially every case);
- `FKRP`, `ANO5`, `CAPN3`, `DYSF` (LGMDs).

Approach: targeted **gene panel** (limb-girdle/distal/rimmed-vacuolar myopathy panel), escalating to **WES/WGS** only in atypical or familial cases. **CMA, karyotype, FISH, mtDNA testing, and repeat-expansion testing have no routine diagnostic role** (with the DMPK exception). GTR/GeneReviews are the relevant resources.

### 10.9 Omics-based diagnostics

- **RNA-seq for TDP-43–dependent cryptic exons** is the most promising emerging molecular diagnostic, arising directly from ✅ PMID:35044790. Not yet clinically deployed.
- Proteomics, metabolomics, epigenomics, liquid biopsy: **research-only; no validated clinical assay.**

### 10.10 Differential diagnosis

| Mimic | Distinguishing features |
|---|---|
| **Polymyositis** | Historically the commonest misdiagnosis; PM is now widely regarded as over-diagnosed and many "steroid-refractory PM" cases are IBM. Symmetric proximal weakness; steroid-responsive. |
| **Immune-mediated necrotizing myopathy (anti-SRP/anti-HMGCR)** | Much higher CK; symmetric proximal; necrosis without endomysial CD8 invasion; treatment-responsive |
| **ALS / motor neuron disease** | Asymmetric weakness overlaps; but ALS has UMN signs, fasciculations, neurogenic EMG, normal/low CK, no rimmed vacuoles |
| **Late-onset Pompe disease** | **Treatable** — always exclude with GAA dried blood spot; axial/respiratory predominance |
| **GNE myopathy (hIBM2)** | **Quadriceps-sparing**, earlier onset, autosomal recessive, no inflammation |
| **VCP multisystem proteinopathy** | Paget disease of bone, FTD, family history |
| **Myotonic dystrophy type 1/2** | Myotonia, cataracts, cardiac conduction disease, multisystem |
| **Sarcoid myopathy / amyloid myopathy** | Systemic features; biopsy distinguishes |
| **Anti-synthetase syndrome** | ILD, mechanic's hands, arthritis, Raynaud, MSA-positive |

### 10.11 Screening

**No population screening exists or is justified** for IBM. No newborn screening, no carrier screening, no cascade screening — there is no Mendelian gene to screen. Explicitly "not applicable."

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

Evidence from the Mayo/REP cohort (*Rheumatology (Oxford)* 2022;61(5):2016, "Survival and associated comorbidities in inclusion body myositis"; 50 IBM patients, 65 IIM controls, 294 population controls):

| Timepoint | IBM | Other IIM | Population controls |
|---|---|---|---|
| 2-year survival | 75% | 86% | 90% |
| 5-year survival | 52% | 76% | 81% |
| 10-year survival | **36%** | 67% | 59% |

*(Note the 10-year IIM > controls inversion — verify these figures against the primary abstract before curating; the pattern is unusual and may reflect a summarization artefact.)*

- **Leading cause of death: respiratory failure or pneumonia (44%)** — i.e., **aspiration secondary to dysphagia is the dominant mortality mechanism**. This is the single most actionable prognostic fact in IBM and should anchor the prognosis section.
- The 40-year population-based study concluded that **"Patients with sIBM have similar risk of cancer, but slightly shorter life expectancy compared to matched patients without sIBM"** ✅ PMID:33879596 *(candidate quote — verify)*.
- Older literature asserting that IBM "does not reduce life expectancy" (e.g. ✅ PMID:25215417) is **now superseded** by population-based data. Curate the older claim, if at all, with `supports: REFUTE` or `PARTIAL` and an explanation — this is exactly the kind of superseded claim the KB should represent explicitly rather than silently drop.

### 11.2 Morbidity and function

- Median time to wheelchair dependence **10.5 years (range 1–29)** ✅ PMID:33879596.
- Progressive loss of ambulation, grip function, and independent feeding.
- Fall-related fractures and head injury.
- Aspiration pneumonia (recurrent), malnutrition, weight loss.
- Respiratory muscle weakness in advanced disease (less prominent than in other myopathies, but present).
- Functional instruments: **IBMFRS** (primary), MMT-8, 6MWD, HAQ, SF-36, quantitative dynamometry. See ✅ PMID:22588740 for the outcome-measure compendium; ✅ PMID:38522330 for the current trial-readiness consensus.

### 11.3 Complications

Aspiration pneumonia; respiratory failure; falls and fractures; deep vein thrombosis from immobility; pressure injury; malnutrition; depression and social isolation. **Not** complications of IBM: cardiomyopathy, interstitial lung disease, malignancy (cancer incidence not increased ✅ PMID:33879596) — important negatives that distinguish IBM from dermatomyositis and the anti-synthetase syndrome.

### 11.4 Recovery potential

**None.** No treatment has been shown to halt or reverse progression. Recovery of lost strength does not occur. This should be stated plainly.

### 11.5 Prognostic factors

| Factor | Direction |
|---|---|
| **Dysphagia presence/severity** | Worse — the dominant mortality driver |
| **Anti-cN1A positivity** | Associated with more severe dysphagia; some series report worse survival — evidence is not conclusive; curate with `supports: PARTIAL` |
| Older age at onset | Worse |
| Greater baseline weakness / lower IBMFRS at presentation | Worse |
| Degree of fatty replacement on MRI | Worse; a candidate imaging prognostic biomarker |
| Endomysial inflammation on biopsy | Correlated with dysphagia severity ✅ PMID:34617994 |

**Prognostic biomarkers:** No validated molecular prognostic biomarker exists. MRI fat fraction and IBMFRS slope are the best current predictors. Honest gap.

---

## 12. Treatment

> **The central fact of IBM therapeutics: there is no disease-modifying therapy and no approved drug.** Every immunosuppressive and immunomodulatory agent trialled has failed. Management is supportive and rehabilitative. This is not a curation gap — it is the state of the field, and the KB entry should say so directly.

### 12.1 Failed / not recommended pharmacotherapy

| Agent | Outcome |
|---|---|
| Corticosteroids (prednisone) | **Ineffective**; may worsen strength via steroid myopathy. Non-response to steroids is a *supportive* diagnostic feature. |
| Methotrexate, azathioprine, mycophenolate, cyclosporine, cyclophosphamide | Ineffective |
| **IVIG** (`MAXO:0001480` immunoglobulin infusion therapy) | No sustained benefit on strength in RCTs. **Retains a limited, non-consensus role for refractory dysphagia**, where uncontrolled series and clinical experience suggest transient benefit. Curate with `supports: PARTIAL` and an explicit caveat. |
| Anti-T-lymphocyte globulin, alemtuzumab, etanercept, anakinra, interferon-β | Ineffective / no confirmed benefit |
| Oxandrolone, arimoclomol, bimagrumab, sirolimus, ulviprubart | See trial table below |

### 12.2 Completed and ongoing clinical trials

| Agent / target | Trial | Result | Citation |
|---|---|---|---|
| **Arimoclomol** — oral heat-shock-response co-inducer (proteostasis) | Multicentre, randomised, double-blind, placebo-controlled, **n = 150**, 20 months | **Negative.** "Arimoclomol did not improve efficacy outcomes, relative to placebo" *(candidate quote — verify)*; acceptable safety; discontinuation-causing AEs 18% vs 5%. | Lancet Neurol 2023 — ✅ **PMID:37739573** |
| **Bimagrumab** — anti-ActRII mAb (myostatin/activin pathway; anabolic, not anti-inflammatory) | **RESILIENT**, randomised double-blind placebo-controlled phase 2b | **Negative on the primary endpoint.** "Bimagrumab showed a good safety profile, relative to placebo" but "did not improve 6MWD" at week 52 *(candidate quotes — verify)*. Increased lean muscle mass without functional benefit. | Lancet Neurol 2019 — ✅ **PMID:31397289** |
| Bimagrumab, long-term extension | RESILIENT LTE, 2 years | "Extended treatment with bimagrumab up to 2 years produced a good safety profile" but "did not provide clinical benefits in terms of improvement in mobility" *(candidate quotes — verify)*. AEs 91.0% vs 89.1% placebo; diarrhoea 14.7%, muscle contractions 9.6%. | Neurology 2021 — ✅ **PMID:33597289** |
| **Sirolimus (rapamycin)** — mTOR inhibitor (autophagy induction + preferential effector-memory T-cell depletion with Treg sparing) | Randomised, double-blind, placebo-controlled, **proof-of-concept phase 2b** | Missed its primary endpoint but produced **encouraging secondary-endpoint signals** (notably 6MWD and thigh-muscle fat fraction on MRI) that motivated a confirmatory trial. | Benveniste O et al., Lancet Rheumatol 2021 — ✅ **PMID:38273639** |
| Sirolimus, confirmatory | **"Optimism in IBM"** — double-blind randomised controlled **phase III**, primary endpoint IBMFRS | Multinational confirmatory trial; protocol/design publication. Completion expected ~2026. | Badrising UA et al., Clin Exp Rheumatol 2025 — ✅ **PMID:40018746** |
| **Ulviprubart (ABC008)** — first-in-class anti-**KLRG1** mAb, selectively depletes highly differentiated cytotoxic KLRG1⁺ T cells while sparing naïve/regulatory T cells | **MUSCLE**, `NCT05721573`, registrational phase 2/3, two doses (0.5 and 2.0 mg/kg Q8W) vs placebo, primary endpoint IBMFRS change at **week 76** | **Topline announced 24 Feb 2026; detailed data presented at GCOM, 26 Mar 2026. The trial did NOT meet its primary endpoint or key secondary endpoints in the full study population.** A prespecified/post-hoc **mild-to-moderate disease subgroup** showed favourable trends on IBMFRS and other measures, which the sponsor states supports continued development in earlier-stage disease. Favourable safety/tolerability; no new safety signals. | Abcuro press releases (24 Feb 2026; 26 Mar 2026) — **company announcements, not yet peer-reviewed.** Curate with `evidence_source: OTHER` and an explicit caveat, or as a `clinical_trials:` entry citing `clinicaltrials:NCT05721573`. |

**Curation note on ulviprubart:** this is the most mechanistically important trial in IBM history — a direct test of the autoimmune-primary hypothesis with a precision T-cell-depleting agent. Its **primary-endpoint failure in the overall population is meaningful negative evidence for the autoimmune-primary model** and should be curated as such (`supports: PARTIAL` or `REFUTE` against the `autoimmune_primary` hypothesis group), while the mild-to-moderate subgroup signal is curated as `EMERGING` with a clear "subgroup analysis, not confirmatory" explanation. Do **not** present the subgroup finding as efficacy.

Other agents in earlier-phase development or of historical interest: follistatin gene therapy (AAV1-FS344, phase I/II), rapamycin analogues, ABC008 follow-ons, and anti-CD8/anti-senescent-T-cell approaches. `clinicaltrials.gov` should be queried for the current pipeline and cached via `just fetch-reference NCT<...>`.

### 12.3 Supportive and rehabilitative management (the actual standard of care)

| Intervention | MAXO term (OAK-verified) | Detail |
|---|---|---|
| **Physical therapy** | `MAXO:0000011` physical therapy | Cornerstone. **Aerobic and resistance exercise are safe and beneficial in IBM** and do not accelerate muscle damage — an important myth-correction. |
| Aerobic exercise therapy | `MAXO:0000065` aerobic exercise therapy | Improves cardiovascular fitness and function |
| Aquatic exercise therapy | `MAXO:0000465` aquatic exercise therapy | Useful when falls risk limits land-based exercise |
| **Occupational therapy** | `MAXO:0001351` occupational therapy | Adaptive grip aids, built-up utensils, home modification |
| **Speech-language pathologist evaluation** | `MAXO:0000733` | Swallow assessment and compensatory strategy training |
| **Speech therapy / swallowing therapy** | `MAXO:0000930` speech therapy | Swallow rehabilitation, diet texture modification |
| **Gastrostomy (PEG)** | `MAXO:0001346` gastrostomy | For severe dysphagia with aspiration or weight loss |
| Barium swallow / VFSS | `MAXO:0035082` barium swallow radiograph procedure | Diagnostic and to guide management |
| Assistive devices, orthoses (AFO for foot drop), wheelchair provision | Use `NCIT:C49236` Therapeutic Procedure or a device-appropriate term; set `therapeutic_modality: DEVICE` | Ankle-foot orthosis for steppage gait |
| Falls-prevention program | `MAXO:0000950` supportive care | Home safety, gait aids |
| Nutritional support | `MAXO:0000088` dietary intervention | Texture modification, calorie support |

### 12.4 Interventional / surgical management of dysphagia

Reserved for cricopharyngeal dysfunction refractory to conservative measures:
- **Cricopharyngeal myotomy** (no specific MAXO term found via OAK — use `MAXO:0000004` surgical procedure or `NCIT:C15329` Surgical Procedure with `therapeutic_modality: SURGERY`);
- **Endoscopic/balloon dilation of the upper oesophageal sphincter**;
- **Botulinum toxin injection into the cricopharyngeus** — `therapeutic_modality: SMALL_MOLECULE`/protein; `therapeutic_agent` bindable to a CHEBI/NCIT botulinum toxin term (verify with OAK).

Evidence for all three is uncontrolled case series with variable and often transient benefit; curate with `supports: PARTIAL`.

### 12.5 Pharmacogenomics

No IBM-specific pharmacogenomic guidance exists (no CPIC guideline, no FDA PGx biomarker for any IBM-relevant agent). If sirolimus enters practice, `CYP3A4`/`CYP3A5` metabolism and therapeutic drug monitoring become relevant, but this is general sirolimus pharmacology, not IBM-specific. **Not available.**

### 12.6 Treatment strategy / algorithm

1. **Establish the diagnosis** (272nd ENMC criteria; exclude Pompe and other treatable mimics).
2. **Do not initiate chronic immunosuppression** — it is ineffective and adds steroid myopathy, infection, and osteoporosis risk. Deprescribe if already started.
3. **Refer immediately to PT/OT** and start a supervised aerobic + resistance program.
4. **Screen for dysphagia at every visit** and refer to SLP at first symptom; escalate to VFSS → dietary modification → myotomy/dilation/botulinum → PEG.
5. **Falls prevention, orthoses, assistive devices** proactively.
6. **Refer to a clinical trial** — this is an explicit standard-of-care recommendation in IBM given the absence of approved therapy.
7. **Advance-care planning** around respiratory and feeding decisions.
8. **Consider peripheral blood flow cytometry** for T-LGL given the ~58% overlap ✅ PMID:26920676.

No personalized/genotype-guided treatment approach exists.

---

## 13. Prevention

- **Primary prevention:** **None available.** Aetiology is unknown; the dominant risk factor (age) and the dominant genetic factor (HLA haplotype) are unmodifiable. No vaccine, no risk-factor modification, no chemoprophylaxis. State this explicitly.
- **Secondary prevention (early detection):** No population screening. The realistic secondary-prevention target is **reducing diagnostic delay** — increasing clinician recognition of the quadriceps + finger-flexor + asymmetry pattern so patients are diagnosed years earlier. Given the MUSCLE-trial mild-to-moderate subgroup signal, earlier diagnosis may become therapeutically consequential.
- **Tertiary prevention (the substantive, evidence-supported arm):**
  - **Dysphagia surveillance and management to prevent aspiration pneumonia** — the highest-value preventive intervention in IBM, given that respiratory failure/pneumonia causes ~44% of deaths.
  - **Falls-prevention** programs, home safety assessment, orthoses, gait aids.
  - **Maintenance exercise** to prevent superimposed disuse atrophy and cardiovascular deconditioning.
  - **Vaccination against influenza, pneumococcus, COVID-19, and RSV** (`MAXO:0001017` vaccination) — indicated to reduce respiratory-infection mortality in a population whose leading cause of death is pneumonia. Note this is generic preventive care applied to a high-risk group, not IBM-specific evidence.
  - Osteoporosis and fracture prevention in patients with reduced mobility.
- **Genetic screening / counselling:** **Not indicated.** IBM is not Mendelian; there is no carrier state, no prenatal testing, no PGD, and no cascade screening. `MAXO:0000079` genetic counseling applies **only** when a hereditary inclusion body *myopathy* is in the differential — and that is a different disease.
- **Public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human — *Homo sapiens*, `NCBITaxon:9606`.
- **Naturally occurring IBM in other species:** **No established naturally occurring animal homologue of sporadic IBM has been described.** An OMIA (Online Mendelian Inheritance in Animals) query should be run to confirm and to cite the absence explicitly.
  - **Do not conflate** IBM with the immune-mediated myopathies that *do* occur naturally in animals — notably **canine masticatory muscle myositis** (autoantibodies to type 2M myofibres) and **equine immune-mediated myositis** — which share the "immune attack on muscle" concept but have no rimmed-vacuole/TDP-43/aggregate pathology and are mechanistically distinct. VBO breed identifiers would apply to those, **not** to IBM.
- **Orthologous genes** (NCBI Gene / Alliance of Genome Resources): mouse *Nt5c1a*, *Tardbp*, *Sqstm1*, *App*, *Klrg1*, *Mstn* all have clear orthologues. Mouse lacks a direct HLA-DRB1 orthologue (H2 class II is the functional analogue), which is a fundamental limitation for modelling IBM's dominant genetic risk factor.
- **Comparative biology:** The *degenerative* arm has strong evolutionary conservation — TDP-43 proteinopathy, autophagy failure, and mtDNA-deletion accumulation are conserved from invertebrates to humans and are extensively modelled in *Drosophila* and *C. elegans*. The *inflammatory* arm — human-specific HLA restriction, human immunosenescence, and the CMV-driven terminally differentiated T-cell compartment — is **poorly conserved**, which is precisely why the human-muscle xenograft model was needed.
- **Zoonotic potential / cross-species transmission:** **Not applicable** — IBM is not transmissible.

---

## 15. Model Organisms

> IBM modelling is a genuine `HUMAN_MODEL_MISMATCH` case rather than a plain knowledge gap: models exist, but **no non-xenograft model reproduces both arms of the disease**, and the field's most important therapeutic inferences depend on which arm a given model captures. Curate a `discussions` entry with `kind: HUMAN_MODEL_MISMATCH`.

### 15.1 The xenograft model (the current best model)

**Britson KA et al., *Science Translational Medicine* 2022 — ✅ PMID:35044790** — "Loss of TDP-43 function and rimmed vacuoles persist after T cell depletion in a xenograft model of sporadic inclusion body myositis."

- **Design:** human IBM muscle transplanted into the hindlimb of immunodeficient mice; human myofibres regenerate in situ.
- **Recapitulation:** "Xenografts from subjects with IBM displayed robust regeneration of human myofibers and recapitulated both inflammatory and degenerative features of the disease" *(candidate quote — verify)*. Specifically: **invasion by human oligoclonal CD8⁺ T cells, MHC-I upregulation, rimmed vacuoles, mitochondrial pathology, p62⁺ inclusions, and nuclear clearance with cytoplasmic aggregation of TDP-43 associated with cryptic exon inclusion.**
- **Significance:** the **first animal model to recapitulate both the degenerative and inflammatory hallmarks** of IBM.
- **Key experimental result:** after T-cell depletion, **TDP-43 loss of function and rimmed vacuoles persisted** — the strongest available evidence that the degenerative arm is not merely downstream of the T-cell attack.
- **Limitations:** requires fresh human IBM muscle (scarce); immunodeficient host lacks a complete immune system; not a genetic model; low throughput; does not model disease initiation.

### 15.2 Transgenic mouse models

| Model | Recapitulates | Fails to recapitulate |
|---|---|---|
| **Conditional MHC class I overexpression** (Nagaraju et al.) | Myofibre degeneration, inflammation, weakness, ER stress | "Transgenic mice that conditionally overexpress MHC-I show myofiber degeneration, but lack other aspects of IBM pathology" *(candidate quote — verify)* — no rimmed vacuoles, no TDP-43 pathology, no selective muscle distribution |
| **MCK-βAPP / APP-overexpressing mouse** (Askanas/Engel lineage) | Intracellular amyloid-β accumulation, some aggregate pathology, weakness | No T-cell infiltration; the aggregate-primacy premise is itself contested |
| **GNE-mutant mice** (M712T knock-in, Gne KO) | Hyposialylation, rimmed vacuoles in some lines | Models **GNE myopathy**, NOT IBM — **do not curate as an IBM model** (NEC hazard) |
| **VCP-mutant mice** (R155H) | Rimmed vacuoles, TDP-43 mislocalization, Paget-like bone disease | Models **VCP multisystem proteinopathy**, not IBM |
| **TDP-43 mouse models** (muscle-specific overexpression/knockdown) | Cytoplasmic TDP-43 aggregation, myopathy with rimmed vacuoles, cryptic exons | No inflammation; no HLA restriction |

### 15.3 Non-mammalian and in vitro models

- ***Drosophila melanogaster*** and ***C. elegans*** TDP-43 and autophagy models — used for the degenerative arm and for genetic modifier screens; no immune arm.
- **Human myoblast / myotube cultures**, including **patient-derived iPSC-derived myotubes** — used to study ER stress, MHC-I induction (IFN-γ stimulation), autophagic flux, and aggregate formation. These are the right substrate for CRISPR/RNAi functional-genomics screens (DepMap/GenomeRNAi have no IBM-specific screens).
- **Co-culture systems** of patient CD8⁺ T cells with autologous myotubes — a promising route to model the cytotoxic synapse in vitro.

### 15.4 Databases and resources

MGI (mouse), IMSR/JAX (strain availability), Alliance of Genome Resources (orthology), Cellosaurus/ATCC (cell lines), DepMap and GenomeRNAi (screens), and **The Myositis Association (TMA)** and **Cure IBM** for funded-project registries and patient-facing trial listings.

### 15.5 Research applications

The xenograft model is the only system currently suitable for **preclinical testing of agents targeting both arms**; MHC-I transgenics remain useful for the inflammation-to-ER-stress axis; TDP-43 models for splicing/cryptic-exon biology; iPSC myotubes for high-throughput proteostasis screening.

---

## Appendix A — Verified identifier quick-reference for KB curation

**Disease:** `MONDO:0007827`

**Genes (HGNC, lowercase prefix per repo convention, all OAK-verified):**
`hgnc:4948` HLA-DRB1 · `hgnc:17819` NT5C1A · `hgnc:11571` TARDBP · `hgnc:11280` SQSTM1 · `hgnc:620` APP · `hgnc:6380` KLRG1 · `hgnc:4223` MSTN · `hgnc:11364` STAT3 · `hgnc:1323` C4A · `hgnc:14673` FYCO1 · *(exclusion guards:* `hgnc:23657` GNE, `hgnc:12666` VCP*)*

**Phenotypes (HP, OAK-verified):**
`HP:0003731` Quadriceps muscle weakness · `HP:0031177` Finger flexor weakness · `HP:0002460` Distal muscle weakness · `HP:0009063` Progressive distal muscle weakness · `HP:0003376` Steppage gait · `HP:0002359` Frequent falls · `HP:0009050` Quadriceps muscle atrophy · `HP:0002015` Dysphagia · `HP:0200136` Oral-pharyngeal dysphagia · `HP:0002068` Neuromuscular dysphagia · `HP:0003236` Elevated circulating creatine kinase concentration · `HP:0008180` Mildly elevated creatine kinase · `HP:0003458` EMG: myopathic abnormalities · `HP:0003805` Rimmed vacuoles · `HP:0003688` Cytochrome C oxidase-negative muscle fibers · `HP:0003200` Ragged-red muscle fibers · `HP:0100297` Increased endomysial connective tissue · `HP:0030057` Autoimmune antibody positivity · `HP:0002960` Autoimmunity

**Cell types (CL, OAK-verified):**
`CL:0000794` CD8-positive, alpha-beta cytotoxic T cell · `CL:0008002` skeletal muscle fiber · `CL:0000235` macrophage · `CL:0000786` plasma cell · `CL:0000594` skeletal muscle satellite cell · `CL:0008016` activated skeletal muscle satellite cell

**Biological processes (GO, OAK-verified):**
`GO:0001913` T cell mediated cytotoxicity · `GO:0043316` cytotoxic T cell degranulation · `GO:0002484` antigen processing and presentation of endogenous peptide antigen via MHC class I via ER pathway · `GO:0034976` response to endoplasmic reticulum stress · `GO:0006914` autophagy · `GO:0061684` chaperone-mediated autophagy · `GO:0000422` autophagy of mitochondrion · `GO:0070841` inclusion body assembly · `GO:0043161` proteasome-mediated ubiquitin-dependent protein catabolic process · `GO:0042026` protein refolding · `GO:0043403` skeletal muscle tissue regeneration

**Anatomy (UBERON, OAK-verified):**
`UBERON:0014892` skeletal muscle organ, vertebrate · `UBERON:0001377` quadriceps femoris · `UBERON:0004498` skeletal muscle tissue of quadriceps femoris · `UBERON:0001523` flexor digitorum profundus · `UBERON:0001385` tibialis anterior · `UBERON:0004499` skeletal muscle tissue of tibialis anterior · `UBERON:0000933` chordate pharyngeal muscle

**Treatments (MAXO, OAK-verified):**
`MAXO:0000011` physical therapy · `MAXO:0000065` aerobic exercise therapy · `MAXO:0000465` aquatic exercise therapy · `MAXO:0001351` occupational therapy · `MAXO:0000733` speech-language pathologist evaluation · `MAXO:0000930` speech therapy · `MAXO:0001346` gastrostomy · `MAXO:0035082` barium swallow radiograph procedure · `MAXO:0001480` immunoglobulin infusion therapy · `MAXO:0000950` supportive care · `MAXO:0000088` dietary intervention · `MAXO:0001017` vaccination

**Clinical trial:** `clinicaltrials:NCT05721573` (MUSCLE / ulviprubart)

---

## Appendix B — PMID verification status

**✅ Confirmed by direct NCBI E-utilities lookup (title/journal/year checked during this research):**

| PMID | Citation |
|---|---|
| 30837708 | Greenberg SA. Inclusion body myositis: clinical features and pathogenesis. *Nat Rev Rheumatol* 2019 |
| 23596012 | Larman HB et al. Cytosolic 5′-nucleotidase 1A autoimmunity in sporadic inclusion body myositis. *Ann Neurol* 2013 |
| 24752512 | Cytoplasmic 5′-nucleotidase autoantibodies in IBM: isotypes and diagnostic utility, 2014 |
| 24975859 | Lloyd TE et al. Evaluation and construction of diagnostic criteria for inclusion body myositis. *Neurology* 2014 |
| 24268584 | Rose MR & ENMC IBM Working Group. 188th ENMC International Workshop. *Neuromuscul Disord* 2013;23(12):1044–55 |
| 38522330 | 272nd ENMC international workshop. *Neuromuscul Disord* 2024;37:36–51 |
| 33879596 | Epidemiology and Natural History of Inclusion Body Myositis: A 40-Year Population-Based Study. *Neurology* 2021 |
| 35596584 | Lindgren U et al. Epidemiology, Survival, and Clinical Characteristics of IBM. *Ann Neurol* 2022 |
| 18203321 | Epidemiology of sporadic IBM and polymyositis in Olmsted County. *J Rheumatol* 2008 |
| 25065005 | Meyer A et al. Incidence and prevalence of inflammatory myopathies: a systematic review. *Rheumatology* 2015 |
| 26920676 | Greenberg SA et al. Association of IBM with T cell large granular lymphocytic leukaemia. *Brain* 2016 |
| 28086002 | Rothwell S et al. Immune-Array Analysis in Sporadic IBM Reveals HLA-DRB1 Amino Acid Heterogeneity. *Arthritis Rheumatol* 2017 |
| 38043487 | High-resolution HLA genotyping in IBM refines 8.1 AH to DRB1*03:01:01 and DRβ1 Arg-74. *J Autoimmun* 2024 |
| 36171069 | Zhou D et al. Low copy numbers of complement C4/C4A deficiency are risk factors for myositis. *Ann Rheum Dis* 2023 |
| 35044790 | Britson KA et al. Loss of TDP-43 function and rimmed vacuoles persist after T cell depletion in a xenograft model of sporadic IBM. *Sci Transl Med* 2022 |
| 37739573 | Safety and efficacy of arimoclomol for inclusion body myositis. *Lancet Neurol* 2023 |
| 31397289 | Hanna MG et al. Bimagrumab in IBM (RESILIENT) phase 2b. *Lancet Neurol* 2019 |
| 33597289 | Bimagrumab long-term extension of RESILIENT. *Neurology* 2021 |
| 38273639 | Benveniste O et al. Sirolimus for IBM: phase 2b proof-of-concept. *Lancet Rheumatol* 2021 |
| 40018746 | Badrising UA et al. "Optimism in IBM" — phase III sirolimus trial. *Clin Exp Rheumatol* 2025 |
| 34617994 | IBM: correlation of clinical outcomes with histopathology, EMG and laboratory findings. *Rheumatology (Oxford)* 2022 |
| 22588740 | Measures of adult and juvenile DM, PM and IBM. *Arthritis Care Res* 2011 |
| 28832349 | IBM: advancements in diagnosis, pathomechanisms, and treatment. *Curr Opin Rheumatol* 2017 |
| 25215417 | Inclusion body myositis: update. *Curr Opin Rheumatol* 2014 |

**⚠️ Cited but NOT verified by direct lookup — resolve and confirm before use:**
30001928 (cN1A sensitivity, 40-patient single-centre series) · 31024569 (Anti-NT5c1A autoantibodies as biomarkers in IBM) · 30136253 (IBM: Update on Pathogenesis and Treatment) · 36237625 (IBM: update on diagnostic and therapeutic landscape) · Pluk H et al. 2013 (independent cN1A discovery, *Ann Neurol*) · Griggs RC et al. 1995 (original criteria) · Mayo "Survival and associated comorbidities in IBM," *Rheumatology (Oxford)* 2022;61(5):2016 · PMC8151681 (anti-cN1A and dysphagia severity) · PMC10098158 (expanded CD8⁺ LGLs in IBM, *Front Immunol* 2023) · Nagaraju et al. MHC-I transgenic mouse

**Non-peer-reviewed sources (curate as `evidence_source: OTHER` with explicit caveats):** Abcuro corporate press releases on the MUSCLE trial (24 Feb 2026 topline; 26 Mar 2026 GCOM presentation).

---

## Appendix C — Recommended `discussions` entries (knowledge gaps and model mismatches)

1. **`KNOWLEDGE_GAP` — Why quadriceps and flexor digitorum profundus?** No mechanism explains IBM's stereotyped, near-pathognomonic muscle selectivity. *Proposed experiments:* comparative single-nucleus transcriptomics/proteomics of affected vs spared muscles from the same patient; fibre-type composition and mitochondrial-load analysis.
2. **`KNOWLEDGE_GAP` — Inflammation-first vs degeneration-first.** Attach to the causal edges between the T-cell-cytotoxicity node and the proteostasis/TDP-43 nodes; link to the two `mechanistic_hypotheses` groups.
3. **`HUMAN_MODEL_MISMATCH` — No genetic animal model reproduces both arms.** MHC-I transgenics give degeneration without vacuoles/TDP-43; TDP-43 and APP models give degeneration without inflammation; mouse lacks an HLA-DRB1 orthologue, so the dominant human genetic risk factor cannot be modelled. The xenograft model is the only dual-arm system and depends on scarce fresh human tissue.
4. **`KNOWLEDGE_GAP` — Is anti-cN1A pathogenic or an epiphenomenon?** No passive-transfer or in vivo pathogenicity evidence exists; cN1A is intracellular, and the antibody is not disease-specific.
5. **`KNOWLEDGE_GAP` — Does the T-LGL clone cause IBM, or does IBM drive clonal expansion?** The 58% overlap with clonal LGL populations and `STAT3` GOF mutations is unexplained directionally.
6. **`KNOWLEDGE_GAP` — Why does IBM not respond to any immunosuppression, if it is autoimmune?** The MUSCLE trial's primary-endpoint failure sharpens rather than resolves this.

**Sources:**
- [Inclusion body myositis: clinical features and pathogenesis — Nature Reviews Rheumatology](https://www.nature.com/articles/s41584-019-0186-x)
- [Safety and efficacy of arimoclomol for inclusion body myositis — Lancet Neurology](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(23)00275-2/fulltext)
- [Safety and efficacy of intravenous bimagrumab in inclusion body myositis (RESILIENT) — PubMed](https://pubmed.ncbi.nlm.nih.gov/31397289/)
- [Epidemiology and Natural History of Inclusion Body Myositis: A 40-Year Population-Based Study — PubMed](https://pubmed.ncbi.nlm.nih.gov/33879596/)
- [Epidemiology, Survival, and Clinical Characteristics of Inclusion Body Myositis — Annals of Neurology](https://onlinelibrary.wiley.com/doi/full/10.1002/ana.26412)
- [Incidence and prevalence of inflammatory myopathies: a systematic review — Rheumatology](https://academic.oup.com/rheumatology/article/54/1/50/1840053)
- [Cytosolic 5'-nucleotidase 1A autoimmunity in sporadic inclusion body myositis — PubMed](https://pubmed.ncbi.nlm.nih.gov/23596012/)
- [Anti-NT5c1A Autoantibodies as Biomarkers in Inclusion Body Myositis — PubMed](https://pubmed.ncbi.nlm.nih.gov/31024569/)
- [High-resolution HLA genotyping in inclusion body myositis refines 8.1 ancestral haplotype association to DRB1*03:01:01 — PubMed](https://pubmed.ncbi.nlm.nih.gov/38043487/)
- [Immune-Array Analysis in Sporadic Inclusion Body Myositis Reveals HLA-DRB1 Amino Acid Heterogeneity — Arthritis & Rheumatology](https://acrjournals.onlinelibrary.wiley.com/doi/10.1002/art.40045)
- [Association of inclusion body myositis with T cell large granular lymphocytic leukaemia — Brain](https://academic.oup.com/brain/article/139/5/1348/2468724)
- [Loss of TDP-43 function and rimmed vacuoles persist after T cell depletion in a xenograft model of sporadic inclusion body myositis — Science Translational Medicine](https://www.science.org/doi/10.1126/scitranslmed.abi9196)
- [272nd ENMC international workshop: revision of the ENMC 2013 diagnostic criteria for inclusion body myositis — Neuromuscular Disorders](https://www.nmd-journal.com/article/S0960-8966(24)00054-3/fulltext)
- [188th ENMC International Workshop: Inclusion Body Myositis — Neuromuscular Disorders](https://www.nmd-journal.com/article/S0960-8966(13)00950-4/fulltext)
- [Abcuro Announces Topline Results from the MUSCLE Study of Ulviprubart in Patients with Inclusion Body Myositis](https://abcuro.com/uncategorized/abcuro-announces-topline-results-from-the-muscle-study-of-ulviprubart-in-patients-with-inclusion-body-myositis/)
- [Abcuro Presents Results from Phase 2/3 MUSCLE Study of Ulviprubart at GCOM 2026 — BioSpace](https://www.biospace.com/press-releases/abcuro-presents-results-from-phase-2-3-muscle-study-of-ulviprubart-in-patients-with-inclusion-body-myositis-at-gcom-2026)
- [Mitochondrial defects in sporadic inclusion body myositis—causes and consequences — Frontiers in Cell and Developmental Biology](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2024.1403463/full)
- [Uncovering the significance of expanded CD8+ large granular lymphocytes in inclusion body myositis — Frontiers in Immunology](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1153789/full)
- [Inclusion body myositis and immunosenescence: current evidence and future perspectives — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11879327/)
- [Sensitivity and clinical utility of the anti-cN1A antibody test in sporadic inclusion body myositis — PubMed](https://pubmed.ncbi.nlm.nih.gov/30001928/)