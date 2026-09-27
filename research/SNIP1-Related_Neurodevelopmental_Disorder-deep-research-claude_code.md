---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T00:35:14.279415'
end_time: '2026-08-01T00:52:22.826091'
duration_seconds: 1028.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SNIP1-Related Neurodevelopmental Disorder
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
  web_search_requests: 13
  num_turns: 68
  total_cost_usd: 5.778741749999999
  session_id: 6a374a05-1268-40bc-b2e9-301bc84abacf
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SNIP1-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SNIP1-Related Neurodevelopmental Disorder** covering all of the
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

# Comprehensive Research Report: SNIP1‑Related Neurodevelopmental Disorder

**Prepared:** 2026‑08‑01  |  **Intended use:** dismech knowledge‑base entry population
**Primary MONDO term:** `MONDO:0013787` — *Psychomotor retardation, epilepsy, and craniofacial dysmorphism*

> **⚠️ Curation guardrail (read first).** Only a subset of the quotations below come from PubMed **abstracts** (the only text `linkml-reference-validator` caches). Quotes drawn from article **body text / tables** (marked **[BODY]**) will **not** validate with `just validate-references` and must not be used as evidence `snippet:` values without substitution. Quotes marked **[ABSTRACT]** are from PubMed abstract text and are the safe candidates — but every one must still be re-verified with `just fetch-reference PMID:XXXX` before commit, per the dismech SOP. This report is a **lead document**, not ground truth.
>
> **NEC preflight note.** This disease has moderate Named‑Entity‑Confusion risk: it carries **two different official names** (OMIM has renamed it) and is easily conflated with the unrelated **B‑SNIP** psychosis consortium literature (PubMed keyword "SNIP" collisions are frequent — three of my initial PMID hits were B‑SNIP psychiatry papers). Anchor all curation on **gene = SNIP1 (HGNC:30587)** and **OMIM:614501**.

---

## 1. Disease Information

### Overview

SNIP1‑related neurodevelopmental disorder is an **autosomal recessive, congenital‑onset, multisystem neurodevelopmental syndrome** caused by biallelic variants in *SNIP1* (Smad nuclear interacting protein 1) at 1p34.3. To date the disorder is known essentially exclusively from a **single founder missense variant, `NM_024700.4:c.1097A>G, p.(Glu366Gly)`, segregating in Old Order Amish communities** in Pennsylvania, Ohio, Indiana and Wisconsin.

The cardinal presentation is neonatal hypotonia and poor feeding, followed by severe (typically non‑verbal) global developmental delay, universally penetrant and frequently drug‑resistant epilepsy, and a recognizable craniofacial gestalt with abnormal skull shape (including multi‑suture craniosynostosis in a subset). Congenital heart defects, upper‑airway abnormalities, and hypothyroidism are common comorbidities, and early childhood mortality is substantial.

**[ABSTRACT] PMID:34570759** — "*Here, we describe extensive genetic studies and clinical findings of a complex inherited neurodevelopmental disorder in 35 individuals associated with a SNIP1 NM_024700.4:c.1097A>G, p.(Glu366Gly) variant, present at high frequency in the Amish community. The cardinal clinical features of the condition include hypotonia, global developmental delay, intellectual disability, seizures, and a characteristic craniofacial appearance.*" (Ammous Z, Rawlins LE, Jones H, et al. *PLoS Genet* 2021;17(9):e1009803. doi:10.1371/journal.pgen.1009803)

### Key identifiers

| Resource | Identifier | Label / note |
|---|---|---|
| **MONDO** | `MONDO:0013787` | Psychomotor retardation, epilepsy, and craniofacial dysmorphism (**recommended `disease_term`**) |
| **OMIM (phenotype)** | `OMIM:614501` | NEURODEVELOPMENTAL DISORDER WITH HYPOTONIA, CRANIOFACIAL ABNORMALITIES, AND SEIZURES; **NEDHCS** (renamed from PMRED) |
| **OMIM (gene)** | `OMIM:608241` | SMAD NUCLEAR INTERACTING PROTEIN 1; SNIP1 |
| **MedGen** | `C3281055` / concept 482685 | Psychomotor retardation, epilepsy, and craniofacial dysmorphism |
| **UMLS** | `C3281055` | equivalent |
| **HGNC** | `hgnc:30587` | SNIP1 (note dismech lowercase‑prefix convention) |
| **NCBI Gene** | `79753` | SNIP1, human |
| **Ensembl** | `ENSG00000163877` | |
| **UniProt** | `Q8TAD8` | Smad nuclear‑interacting protein 1 |
| **RefSeq** | `NM_024700.4` / `NP_078976.2` | canonical transcript used for all HGVS |
| **dbSNP** | `rs387906986` | founder variant |
| **ClinVar** | Variation ID `30717`; RCV000023695 | |
| **Orphanet** | **No ORDO entry found** | OLS4 ORDO search for "SNIP1" returned 0 hits; MONDO:0013787 carries no Orphanet xref. **Curation gap — flag as `NOT_YET_DOCUMENTED`.** |
| **ICD‑10 / ICD‑11** | **No dedicated code** | Would be coded under a generic congenital‑malformation‑syndrome / epilepsy code; do not invent a specific code. |
| **MeSH** | **No specific descriptor** | |

### Synonyms and alternative names

- Psychomotor retardation, epilepsy, and craniofacial dysmorphism (**PMRED**) — original OMIM title, still the MONDO label
- Neurodevelopmental disorder with hypotonia, craniofacial abnormalities, and seizures (**NEDHCS**) — current OMIM title
- SNIP1‑related neurodevelopmental disorder
- **"Symptomatic epilepsy and skull dysplasia"** — the clinical/laboratory name used by DDC Clinic Medical Center (Ohio Amish) for its targeted test
- Amish SNIP1 syndrome / SNIP1 Amish founder disorder (informal)

### Nature of the evidence base

Information is derived almost entirely from **aggregated deep‑phenotyping of individual patients in a community‑genetics setting** — the Clinic for Special Children (Strasburg, PA), DDC Clinic (Middlefield, OH), and collaborating centres — rather than from EHR/claims resources. There are effectively **two primary clinical publications**:

1. **PMID:22279524** — Puffenberger EG, Jinks RN, Sougnez C, et al. "Genetic mapping and exome sequencing identify variants associated with five novel diseases." *PLoS One* 2012;7(1):e28936. doi:10.1371/journal.pone.0028936 — original gene discovery (3 patients / 2 sibships).
2. **PMID:34570759** — Ammous Z, Rawlins LE, Jones H, et al. *PLoS Genet* 2021 — definitive natural‑history cohort (51 identified, 35 deeply phenotyped).

No population registry, EHR‑based cohort, or ICEES/COHD‑style comorbidity data exist for this disorder.

---

## 2. Etiology

### Primary causal factor

**Genetic, monogenic, autosomal recessive.** Homozygosity for `SNIP1 c.1097A>G, p.(Glu366Gly)` is the sole established cause.

**[ABSTRACT] PMID:22279524** — "*Using between 1 and 5 patient samples per disorder, we identified sequence variants in the known disease-causing genes SLC6A3 and FLVCR1, and present evidence to strongly support the pathogenicity of variants identified in TUBGCP6, BRAT1, SNIP1, CRADD, and HARS.*"

**[BODY] PMID:22279524** — the disease locus mapped to a region containing 34 homozygous variants shared among affected individuals, of which only one — the *SNIP1* change — was novel. Glu366 is highly conserved and lies in the C‑terminus, the region through which SNIP1 engages c‑Myc.

### Genetic risk factors

- **Causal variant:** `NM_024700.4:c.1097A>G` (`NC_000001.11:g.37537842T>C`, GRCh38), p.(Glu366Gly), missense, exon 4, biallelic/homozygous. rs387906986.
- **Variant classification:** ClinVar germline classification **"Likely pathogenic"**, review status **1 star** (criteria provided, single submitter), last evaluated 2022‑03‑22. The 2021 *PLoS Genetics* authors independently assessed it as **"pathogenic"** under ACMG/AMP criteria. *(This discrepancy should be recorded verbatim in the entry rather than resolved silently.)*
- **Founder effect / ancestry:** essentially the only genetic "risk factor" is **Old Order Amish ancestry**, plus consanguinity/endogamy.
- **Modifier genes:** **none identified.** No modifier or susceptibility loci have been reported.
- **Heterozygote status:** carriers are unaffected; "*no unaffected individuals being homozygous for this variant*" **[BODY, PMID:34570759]** — i.e., complete penetrance in homozygotes within the studied cohort.

### A second, distinct genetic mechanism (heterozygous deletion)

**PMID:29726122** — Jacher JE, Innis JW. "Interstitial microdeletion of the 1p34.3p34.2 region." *Mol Genet Genomic Med* 2018;6(4):649–654. doi:10.1002/mgg3.409. A 2.3 Mb contiguous‑gene deletion **including *SNIP1*** (but not *AGO1*, *AGO3*, *GRIK3*, *SLC2A1*, *RIMS3*) in a patient with global developmental delay, mild intellectual disability, delayed bone age, bilateral vesicoureteral reflux, vocal cord paralysis, right aberrant subclavian artery, kyphoscoliosis, bilateral metatarsus adductus, and valgus knee deformity. The authors attribute the phenotype to haploinsufficiency of the region "*including the SNIP1 gene*."

> **Curation guidance:** this is a *contiguous‑gene deletion syndrome*, **not** the recessive SNIP1 disorder. Do **not** merge. It is at most a supporting datum that *SNIP1* dosage matters, and the vocal‑cord paralysis is an intriguing partial echo of the airway phenotype. Consider a `discussions` entry with `kind: KNOWLEDGE_GAP`.

### Environmental risk factors

**None identified.** No toxin, infectious, nutritional, occupational, parental‑age, or seasonal risk factor has been reported. Sex is not a risk factor (cohort was 19 M : 16 F).

### Protective factors

**None identified.** No protective allele, dietary, or lifestyle factor is known. gnomAD contains **no homozygotes** for the variant, providing no evidence for a compensated/protected genotype.

### Gene–environment interactions

**Not documented for the human disorder.** The nearest mechanistic analogue comes from cell biology: SNIP1's chromatin occupancy in neural progenitors is *signal‑dependent* — **[ABSTRACT‑adjacent, BODY PMID:37553330]** "*TGFβ and NFκB signaling pathways control SNIP1 binding to specific gene loci in NPCs.*" This raises a testable (unproven) hypothesis that maternal/fetal inflammatory or TGF‑β‑modulating exposures could modify expressivity. **Flag as hypothesis, not established.**

---

## 3. Phenotypes

### 3.1 Frequency table (Ammous et al. 2021, n = 35–37 evaluated individuals)

Frequencies below are **[BODY]** data from the *PLoS Genetics* clinical tables, cross‑checked against the HPO disease annotations for `OMIM:614501` (retrieved from ontology.jax.org, which encodes exact numerators/denominators).

| Phenotype | Suggested HPO term | Frequency (cohort) | HPO annotation fraction | Suggested `FrequencyEnum` |
|---|---|---|---|---|
| Severe global developmental delay (non‑verbal) | `HP:0011344` Severe global developmental delay | 100% | 37/37 | `OBLIGATE`/`VERY_FREQUENT` |
| Hypotonia | `HP:0001252` Hypotonia | 100% | 35/35 | `VERY_FREQUENT` |
| Hyporeflexia | `HP:0001265` Hyporeflexia | 100% | 35/35 | `VERY_FREQUENT` |
| Seizures | `HP:0001250` Seizure | 100% | 37/37 | `VERY_FREQUENT` |
| Feeding difficulties | `HP:0011968` Feeding difficulties | 100% | 35/35 (onset **early infancy**) | `VERY_FREQUENT` |
| Abnormal skull shape (irregular surface, craniosynostosis) | `HP:0002whatever` → use `HP:0001363` Craniosynostosis + `HP:0002684` Thickened calvaria *(verify)* | 100% | — | `VERY_FREQUENT` |
| High arched palate | `HP:0000218` High palate | 100% | 35/35 | `VERY_FREQUENT` |
| Wide mouth | `HP:0000154` Wide mouth | 100% | 37/37 | `VERY_FREQUENT` |
| Exaggerated cupid's bow upper lip | `HP:0002263` Exaggerated cupid's bow | 100% | 35/35 | `VERY_FREQUENT` |
| Laryngomalacia | `HP:0001601` Laryngomalacia | 74% | 26/35 | `FREQUENT` |
| Upper‑airway abnormality (laryngomalacia, apnoea, stridor) | `HP:0002104` Apnea; `HP:0010307` Stridor | 75% | — | `FREQUENT` |
| Behavioural problems (irritability, autistic features, ADHD) | `HP:0000708` Behavioral abnormality; `HP:0000717` Autism; `HP:0007018` ADHD | 75% | — | `FREQUENT` |
| Congenital heart defect (ASD, VSD, aortic coarctation) | `HP:0001631` ASD; `HP:0001629` VSD; `HP:0001680` Coarctation of aorta | 60% | — | `FREQUENT` |
| Small for gestational age | `HP:0001518` Small for gestational age | 54% | 18/35 | `FREQUENT` |
| Tapered fingers | `HP:0001182` Tapered finger | 54% | 20/37 | `FREQUENT` |
| Short palm / short hands | `HP:0004279` Short palm | 51% | 18/35 | `FREQUENT` |
| Abnormal brain MRI | see §3.3 | 50% | — | `FREQUENT` |
| Pulmonary aspiration | `HP:0002835` Aspiration | 46% | — | `FREQUENT` |
| Horizontal nystagmus and/or strabismus | `HP:0000666` Horizontal nystagmus; `HP:0000486` Strabismus | 45% | — | `FREQUENT` |
| Micrognathia | `HP:0000347` Micrognathia | 29% | 10/35 | `OCCASIONAL` |
| Hypothyroidism | `HP:0000821` Hypothyroidism | 25% | — | `OCCASIONAL` |
| Hypoglycaemia | `HP:0001943` Hypoglycemia | 20–21% | 7/35 | `OCCASIONAL` |
| Failed newborn hearing screen (conductive) | `HP:0000405` Conductive hearing impairment | 21% | — | `OCCASIONAL` |
| Umbilical hernia | `HP:0001537` Umbilical hernia | 20% | 7/35 | `OCCASIONAL` |
| Talipes equinovarus | `HP:0001762` Talipes equinovarus | 14% | 5/35 | `OCCASIONAL` |
| Cardiomyopathy (left ventricular non‑compaction) | `HP:0001638` Cardiomyopathy; `HP:0011664` Left ventricular noncompaction | 12% | — | `OCCASIONAL` |

**Additional HPO terms annotated to OMIM:614501 without a cohort fraction** (from the HPO disease annotation file — treat as `frequency:` omitted):
`HP:0000158` Macroglossia · `HP:0000414` Bulbous nose · `HP:0012802` Broad jaw · `HP:0011304` Broad thumb (2/2) · `HP:0002500` Abnormal cerebral white matter morphology · `HP:0003429` CNS hypomyelination (2/2) · `HP:0002079` Hypoplasia of the corpus callosum (2/2) · `HP:0002119` Ventriculomegaly (2/2) · `HP:0002353` EEG abnormality · `HP:0001607` Subglottic stenosis · `HP:0001647` Bicuspid aortic valve · `HP:0001650` Aortic valve stenosis · `HP:0000007` Autosomal recessive inheritance.

> **Frequency‑evidence caution (per `docs/frequency-evidence-guidelines.md`):** the *fractions* above come from the HPO annotation file (which is itself derived from PMID:34570759 tables), not from an abstract sentence. Only the qualitative associations are abstract‑supported. **Prefer omitting `frequency:` for any phenotype whose band you cannot back with a directly quotable abstract sentence.**

### 3.2 Craniofacial gestalt (the "recognizable" feature)

**[BODY] PMID:34570759** — features include "*midface hypoplasia, a wide mouth with downturned corners and thin cupids bow upper lip, large tongue, high arched palate, microretrognathia (Pierre Robin sequence with or without cleft palate in three patients), malocclusion, small upturned bulbous nose, long palpebral fissures and proptosis.*"

Skull: "*Abnormal skull shape (irregular surface, craniosynostosis)*" in 100%, with "*severe multi-suture craniosynostosis with Cloverleaf appearance of the skull in five individuals*" **[BODY]**.

Suggested HPO: `HP:0000308` Microretrognathia · `HP:0000202` Orofacial cleft / `HP:0000175` Cleft palate · `HP:0000463` Anteverted nares *(verify)* · `HP:0000637` Long palpebral fissure · `HP:0000520` Proptosis · `HP:0000316` Hypertelorism *(not reported — do not add)* · `HP:0011800` Midface retrusion · `HP:0000687` Pierre‑Robin sequence → correct term is `HP:0000201` Pierre‑Robin sequence *(verify with OAK)*.

### 3.3 Neuroimaging phenotype

**[BODY] PMID:34570759** — brain MRI abnormalities in ~50%, "*including hydrocephalus, ventriculomegaly, white matter abnormalities, thin corpus callosum, hypomyelination, irregular cortical ribbon, Chiari malformation, absence of the septum pellucidum, hypoplastic optic nerves and septo-optic dysplasia.*"

Suggested HPO: `HP:0000238` Hydrocephalus · `HP:0002119` Ventriculomegaly · `HP:0002500` Abnormal cerebral white matter morphology · `HP:0002079` Hypoplasia of the corpus callosum · `HP:0003429` CNS hypomyelination · `HP:0002510` Chiari malformation *(verify ID)* · `HP:0001331` Absent septum pellucidum · `HP:0000633` Optic nerve hypoplasia *(verify)* · `HP:0100842` Septo‑optic dysplasia *(verify)*.

### 3.4 Epilepsy phenotype (the dominant morbidity)

**[BODY] PMID:34570759** — "*Seizures are a cardinal feature of the disorder with all affected individuals developing epilepsy*"; types include "*focal and generalised intractable seizures (myoclonic, absence, tonic-clonic) of infantile or childhood onset*"; "*There were no antiepileptic medications identified that consistently provide effective seizure control*" and "*several individuals display multiple drug resistant epilepsy.*"

Suggested HPO: `HP:0001250` Seizure · `HP:0011146` Dialeptic seizure / `HP:0002121` Absence seizure · `HP:0002123` Generalized myoclonic seizure · `HP:0002069` Bilateral tonic‑clonic seizure · `HP:0007359` Focal‑onset seizure · `HP:0011171` Complex febrile seizure *(not reported)* · `HP:0002133` Status epilepticus (management target) · `HP:0011097` Epileptic spasms *(not reported — do not add)*.
Qualifiers: `temporality: RECURRENT`, `onset: INFANTILE_ONSET`/`CHILDHOOD_ONSET`, drug resistance is best captured in the description text.

### 3.5 Developmental attainment and function

**[BODY] PMID:34570759** — "*Global developmental delay (severe, non-verbal)*" in 100%; "*Most affected individuals achieved independent ambulation (age range 3–10 years), and some communicate with signs, gestures and sounds.*"

This is an important nuance: **motor milestones are markedly delayed but often eventually achieved**, while expressive language is essentially absent. Suggested HPO: `HP:0011344` Severe global developmental delay · `HP:0001510` Growth delay · `HP:0002187` Profound global developmental delay *(do not use — cohort described as "severe")* · `HP:0001344` Absent speech.

### 3.6 Quality‑of‑life impact

**No formal QoL instrument (EQ‑5D, PROMIS, SF‑36, PedsQL) has been applied to this cohort.** Impact must be inferred qualitatively:

- **Feeding/nutrition:** universal feeding difficulty with 46% pulmonary aspiration drives gastrostomy dependence — a major daily‑care burden and a driver of the recommendation for **elective** (rather than reactive) G‑tube placement.
- **Epilepsy:** drug‑resistant seizures with status‑epilepticus risk dominate family burden and healthcare utilisation.
- **Communication:** non‑verbal status with partial sign/gesture communication.
- **Mobility:** independent ambulation is attainable for most, materially better than many severe DEEs.
- **Behaviour:** irritability/autistic features/ADHD in 75%.

**Curation note:** record this as `notes:`/description text, **not** as evidence‑backed QoL claims.

---

## 4. Genetic / Molecular Information

### Causal gene

**SNIP1** — Smad nuclear interacting protein 1; `hgnc:30587`; `OMIM:608241`; 1p34.3; Entrez 79753; ENSG00000163877; UniProt **Q8TAD8** (396 aa, 45,778 Da). Previous/alias symbol: **PML1** (yeast Pml1p homolog).

**Protein architecture (UniProt Q8TAD8):**
- N‑terminal **nuclear localisation signal**; the N‑terminal region mediates Smad and RelA/p65 binding
- **Forkhead‑associated (FHA) domain, residues 281–344** — a phospho‑threonine‑peptide recognition module
- C‑terminus (containing Glu366) mediates c‑Myc interaction
- PTMs: phosphorylation (Ser35, Ser49, Ser52, Ser54, Thr57, Ser58, Ser202, Ser394); SUMOylation (Lys30, Lys108, Lys223)
- Subcellular localisation: **nucleus / nucleoplasm** (`GO:0005654`)

### Pathogenic variant

| Field | Value |
|---|---|
| HGVS c. | `NM_024700.4:c.1097A>G` |
| HGVS p. | `NP_078976.2:p.(Glu366Gly)` (E366G) |
| Genomic (GRCh38) | `NC_000001.11:g.37537842T>C` |
| dbSNP | rs387906986 |
| Variant type | Missense (single nucleotide variant), exon 4 |
| Zygosity in patients | Homozygous (biallelic) |
| Origin | **Germline**, inherited (founder haplotype); no somatic involvement |
| ClinVar | Variation 30717; **Likely pathogenic**, 1★, last evaluated 2022‑03‑22 |
| ACMG (publication) | assessed as **pathogenic** in PMID:34570759 |

### Allele frequency

- **gnomAD:** **[BODY, PMID:34570759]** "*allele frequency of 0.001% with 11 heterozygotes (10 Amish) and no homozygous individuals listed.*"
- **Old Order Amish (Puffenberger 2012, control chromosomes):** 5/203 = **2.5% carrier frequency** **[BODY]**
- **Old Order Amish (Ammous 2021):** allele frequency **0.5% (Pennsylvania) to 1.4% (Ohio/Indiana/Wisconsin)** **[BODY]**
- **GeneReviews (Wallace SE, Puffenberger EG, Bean LJH; "Genetic Disorders Associated with Founder Variants Common in the Amish Population," last update 2023‑12‑07; NBK558237):** carrier frequency **1/34** in Old Order Amish; this variant accounts for **~100%** of pathogenic *SNIP1* variants identified in this population.

> **Note the internal inconsistency** across sources (2.5% vs 0.5–1.4% vs 1/34 ≈ 2.9%). These are different sampling frames (small control panel vs settlement‑stratified vs GeneReviews summary). Record each with its own `prevalence`/`case_fractions` record, `population` stratifier, and evidence — do not average them.

### Functional consequences of p.Glu366Gly

Three independent lines of evidence, all pointing to **partial (hypomorphic) loss of function**, not a null:

1. **Protein instability and mislocalisation (in vitro, 2012).** **[BODY, PMID:22279524]** The mutant showed abnormal nuclear localisation with "*a more aggregated appearance*" versus wild‑type's punctate pattern; western blot band density was "*84.9±9.6% SD lower than wild-type*" — i.e. ~85% reduction in steady‑state protein.
2. **Conservation and domain proximity.** **[BODY, PMID:34570759]** "*The p.(Glu366Gly) SNIP1 amino acid substitution is located in close proximity to the forkhead association (FHA) domain*," a "*functionally important region of SNIP1*"; the authors caution "*this Amish variant may be unlikely to result in complete loss of function.*" *(Note the UniProt FHA boundary is 281–344, so E366 sits just C‑terminal to the annotated domain; the 2026 Nature Communications paper below treats E366G as an FHA‑domain mutation. Record the discrepancy rather than picking a side.)*
3. **Direct splicing‑machinery defect (2026, definitive).** **[ABSTRACT] PMID:41904131** — "*Mutations in SNIP1 FHA domain, including the neurodevelopmental disorder-associated E366G variant, impair P-SF3B1 binding, pre-mRNA splicing, and cell viability.*" (Gajdušková P, Ruiz de Los Mozos I, Hluchý M, et al. "Phosphorylation of SF3B1 by CDK11 orchestrates spliceosome activation via SNIP1‑dependent RES complex recruitment." *Nat Commun* 2026. doi:10.1038/s41467-026-71119-2)

**Mechanistic classification for the KB:** `LOSS_OF_FUNCTION` (hypomorphic/partial). Complete LoF is presumably embryonic‑lethal — consistent with mouse homozygous null prenatal lethality (§15).

### Modifier genes

**None reported.** The remarkable clinical homogeneity of the Amish cohort (single variant, shared genetic background) both explains the absence of modifier data and makes this disorder a poor discovery substrate for modifiers.

### Epigenetic information

Two distinct senses, both relevant:

1. **SNIP1 as an epigenetic regulator (mechanism, not biomarker).** **[ABSTRACT] PMID:37553330** — "*SNIP1 facilitates the genomic occupancy of Polycomb complex PRC2 and instructs H3K27me3 turnover at target genes.*" SNIP1 also recruits **TET2** to c‑MYC target genes (PMID:30404004, "SNIP1 Recruits TET2 to Regulate c-MYC Target Genes and Cellular DNA Damage Response," *Cell Rep* 2018) — a direct link to DNA 5‑hydroxymethylation.
2. **Episignature / methylation biomarker for diagnosis:** **none published.** SNIP1 is not among the genes with a validated DNA‑methylation episignature (EpiSign). **Curation gap.**

### Chromosomal abnormalities

- No aneuploidy, translocation, or inversion associated with the recessive disorder.
- **1p34.3p34.2 interstitial microdeletion** encompassing *SNIP1* (PMID:29726122) — see §2. Relevant to CMA interpretation.

---

## 5. Environmental Information

- **Environmental factors:** none identified. No CTD entry links an environmental chemical to this disorder.
- **Lifestyle factors:** not applicable — congenital monogenic disorder.
- **Infectious agents:** not causal. **However, infection is a leading proximate cause of death** (see §11) and recurrent aspiration/respiratory infection is a major secondary morbidity — model this as a **downstream consequence node**, not an etiologic node.

---

## 6. Mechanism / Pathophysiology

### 6.1 SNIP1 protein: four functional arms

**[ABSTRACT] PMID:34570759** — "*SNIP1 (Smad nuclear interacting protein 1) is a widely expressed transcriptional suppressor of the TGF-β signal-transduction pathway which plays a key role in human spliceosome function.*"

**[ABSTRACT] PMID:38304835** (Chen Y, Guo W, Guo X, Wanqing Q, Yin Z. "The clinical utilization of SNIP1 and its pathophysiological mechanisms in disease." *Heliyon* 2024;10(2):e24601) — "*Smad intranuclear binding protein 1 (SNIP1), a highly conserved nuclear protein, functions as a transcriptional regulator and exerts a significant influence on disease progression. In addition, the N-terminal domain of SNIP1 facilitates its interaction with Smad4, a signaling protein associated with the TGF-β family, and RelA/p65, a transcription factor connected to NF-κB. This interaction further enhances the transcriptional activation of c-Myc-dependent genes.*"

| Arm | Molecular action | Key references |
|---|---|---|
| **(A) TGF‑β/BMP repression** | Binds Smad1/2/4; suppresses p300‑dependent TGF‑β signal transduction | Kim RH et al. *Genes Dev* 2000 (**PMID:10887155**) |
| **(B) NF‑κB repression** | Competes with RELA/p65 for the C/H1 domain of CBP/p300 | Kim RH et al. *J Biol Chem* 2001 (**PMID:11567019**) |
| **(C) c‑Myc co‑activation / cell cycle** | Modifies c‑Myc transcriptional activity on E‑box genes; regulates cyclin D1 transcription and mRNA stability; regulates ATR‑dependent DNA‑damage signalling; recruits TET2 to c‑MYC targets | Fujii M et al. *Mol Cell* 2006 (**PMID:17157259**); Roche KC et al. *Oncogene* 2004 (**PMID:15378006**); Bracken CP et al. *Cancer Res* 2008 (**PMID:18794151**); Roche KC et al. *Oncogene* 2007 (**PMID:17260016**); Chen L‑L et al. *Cell Rep* 2018 (**PMID:30404004**) |
| **(D) Spliceosome / RES complex** | FHA domain reads phospho‑SF3B1 and recruits the **RES (retention‑and‑splicing) complex** during spliceosome activation; with RNPS1 forms a "molecular brake" pausing the spliceosome at Bact on **detained introns**; also implicated in U12‑type minor‑spliceosome splicing and small‑RNA biogenesis | **PMID:41904131**; **PMID:37027487**; Fernandez JP et al. *PLoS Genet* 2018 (**PMID:29969449**); Liu C et al. *PNAS* 2008 (**PMID:18632581**) |

### 6.2 The splicing arm — the most direct route from E366G to disease

**[ABSTRACT] PMID:41904131** — "*We further demonstrate that P-SF3B1 is recognized by forkhead-associated (FHA) domain of SNIP1, which promotes recruitment of retention and splicing (RES) complex during spliceosome activation. Acute SNIP1 depletion disrupts RES incorporation, causes widespread splicing defects, and promotes hyperphosphorylation of SF3B1 by CDK11.*"

**[ABSTRACT] PMID:37027487** (Meng D, Zheng Q, Zhang X, Piao X, Luo L, Jia Y. "A molecular brake that modulates spliceosome pausing at detained introns contributes to neurodegeneration." *Protein Cell* 2023;14(1):27–53. doi:10.1093/procel/pwac008) — "*Here, we suggest that post-transcriptional DI splicing is paused at the Bact state, an active spliceosome but not catalytically primed, which depends on Smad Nuclear Interacting Protein 1 (SNIP1) and RNPS1 (a serine-rich RNA binding protein) interaction… Snip1 conditional knockout in the cerebellum decreases DI splicing efficiency and causes neurodegeneration.*"

This places SNIP1 alongside other **spliceosomopathy neurodevelopmental genes** (EFTUD2, SF3B4, SNW1, SF3B1, RNU4‑2) — a useful cross‑entry link in dismech, and arguably a candidate future **mechanism module** ("spliceosomopathy neurodevelopment").

### 6.3 The neural‑progenitor survival arm

**[ABSTRACT] PMID:37553330** (Matsui Y, Djekidel MN, Lindsay K, et al. "SNIP1 and PRC2 coordinate cell fates of neural progenitors during brain development." *Nat Commun* 2023;14:4771. doi:10.1038/s41467-023-40487-4) — "*Here, we report that Smad nuclear interacting protein 1 (SNIP1) promotes neural progenitor cell survival and neurogenesis and is, therefore, integral to brain development. The SNIP1-depleted brain exhibits dysplasia with robust induction of caspase 9-dependent apoptosis. Mechanistically, SNIP1 regulates target genes that promote cell survival and neurogenesis, and its activities are influenced by TGFβ and NFκB signaling pathways. Further, SNIP1 facilitates the genomic occupancy of Polycomb complex PRC2 and instructs H3K27me3 turnover at target genes. Depletion of PRC2 is sufficient to reduce apoptosis and brain dysplasia and to partially restore genetic programs in the SNIP1-depleted brain in vivo.*"

Supporting **[BODY]** detail from the same paper: "*By E15, Snip1_Nes-KO embryos displayed severe thinning of brain tissues and dysplasia with 100% penetrance*"; SOX2⁺ neural progenitor cells, and TBR2⁺ and INSM1⁺ intermediate progenitors "*were markedly reduced*"; "*All ventricles of Snip1_Nes-KO displayed strong induction of cl-caspase 3*"; "*inhibition of caspase 9 robustly reduced apoptosis*" whereas caspase 8 inhibition "*modestly altered apoptosis*"; EED (PRC2) depletion "*reduced apoptosis and rescued NPCs.*"

### 6.4 Patient transcriptome (human, in vivo)

**[BODY] PMID:34570759** — differential expression analysis of patient samples identified "*75 significantly upregulated genes, and 109 significantly downregulated genes*" (FDR <0.05). Reactome analysis: "*the most overrepresented pathway was the TGF-β receptor signalling in epithelial to mesenchyme pathway.*" Five seizure‑associated genes were notably altered: **ROBO1, SOX5, CNTNAP2, PAFAH1B1, TSNARE1** (ROBO1 most upregulated); *SYT1* (synaptic vesicle) also dysregulated; 24 differentially expressed genes had "*a previously established association with neurological disease.*" Additional dysregulated pathways reported in the paper's discussion include **NOTCH3 signalling** and the **MYC pathway**.

### 6.5 Proposed causal chain (for `pathophysiology` nodes)

```
[MOLECULAR] SNIP1 p.Glu366Gly homozygosity
   → reduced SNIP1 protein abundance (~85% ↓) + nuclear aggregation
   → impaired FHA-domain recognition of phospho-SF3B1
        ├─→ [MOLECULAR] failed RES complex recruitment / spliceosome activation defect
        │        → aberrant pre-mRNA splicing, detained-intron mishandling
        └─→ [MOLECULAR] dysregulated SNIP1-dependent transcription
                 (de-repressed TGF-β/SMAD; de-repressed NF-κB/RELA-p300;
                  altered c-MYC target output; mislocalised PRC2 → aberrant H3K27me3)
   → [CELLULAR] neural progenitor cell (SOX2+, TBR2+, INSM1+) apoptosis
        via the intrinsic, caspase-9-dependent pathway; reduced neurogenesis
   → [TISSUE] cortical dysplasia, hypomyelination, corpus callosum hypoplasia,
        ventriculomegaly, midline defects; abnormal cranial suture fusion;
        abnormal pharyngeal/laryngeal and cardiac morphogenesis
   → [ORGANISM] severe global developmental delay, intractable epilepsy,
        craniofacial gestalt, airway compromise, CHD, early mortality
```

**Upstream vs downstream:** the molecular splicing/transcription lesion is upstream; NPC apoptosis is the pivotal cellular hub (the point at which PRC2 depletion rescues, in mouse); tissue malformation and epilepsy are downstream.

### 6.6 Suggested ontology terms

**GO biological process** (all verified against QuickGO):
- `GO:0000398` mRNA splicing, via spliceosome — modifier `DECREASED`/`ABNORMAL`
- `GO:0007179` transforming growth factor beta receptor signaling pathway — `INCREASED` (de‑repression)
- `GO:0043122` regulation of canonical NF-kappaB signal transduction — `INCREASED`
- `GO:0097193` intrinsic apoptotic signaling pathway — `INCREASED`
- `GO:0021895` cerebral cortex neuron differentiation — `DECREASED`
- `GO:0006974` DNA damage response
- Additional candidates to verify with OAK: `GO:0050768` negative regulation of neurogenesis; `GO:0006355` regulation of DNA-templated transcription; `GO:0035914`? (n/a)

**GO cellular component** (verified): `GO:0005681` spliceosomal complex · `GO:0031519` PcG protein complex · `GO:0005654` nucleoplasm *(verify)*.

**Cell Ontology** (verified via OLS):
- `CL:0011020` neural progenitor cell
- `CL:0000681` radial glial cell
- `CL:0013000` forebrain radial glial cell
- `CL:0000047` neuronal stem cell *(verify)*
- `CL:0000540` neuron *(verify)*

**CHEBI:** not applicable — no small‑molecule metabolite is central to the mechanism.

### 6.7 Metabolic, immune, and biochemical dimensions

- **Metabolic changes:** no primary inborn‑error‑of‑metabolism component. **Hypoglycaemia in ~20%** is documented but its mechanism is unexplained (feeding failure? endocrine?) — record as an unexplained finding / knowledge gap, not as a metabolic mechanism.
- **Immune system involvement:** no immunodeficiency or autoimmunity. SNIP1 is an NF‑κB brake and has documented roles in intestinal epithelial barrier/inflammation (PMID:29426045, *Mucosal Immunol* 2018) and osteoarthritis inflammation (PMID:37739115), but **no immune phenotype has been reported in patients.** Do not over‑extrapolate.
- **Tissue damage mechanisms:** developmental (apoptotic loss of progenitors + malformation), not degenerative — with the important caveat that the *Protein Cell* 2023 cerebellar cKO shows SNIP1 loss can also drive **post‑developmental neurodegeneration**, raising an untested question about whether adolescents/adults with the disorder have a degenerative component.
- **Biochemical abnormalities:** hypothyroidism (25%) is the one reproducible laboratory abnormality; hypoglycaemia (~20%). No specific enzyme deficiency, receptor, or ion‑channel defect.

### 6.8 Molecular profiling summary

| Modality | Status |
|---|---|
| Transcriptomics | ✅ Patient RNA‑seq (PMID:34570759); mouse brain RNA‑seq + CUT&RUN (PMID:37553330); zebrafish RNA‑seq (PMID:29969449); human cell iCLIP‑seq (PMID:41904131) |
| Proteomics | ✅ Quantitative proteomics of chromatin‑associated spliceosomes (PMID:41904131) — mechanism, not patient‑derived |
| Metabolomics / Lipidomics | ❌ None |
| Epigenomics | Indirect only (H3K27me3 CUT&RUN in mouse; no patient methylome) |
| Single‑cell / spatial | ❌ No patient scRNA‑seq or spatial data |
| Functional genomics screens | *SNIP1* is broadly **essential** in DepMap‑type screens (consistent with mouse lethality); the 2026 paper shows acute depletion impairs cell viability |

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
- **Brain** `UBERON:0000955` — cerebral cortex `UBERON:0000956`, cerebral white matter `UBERON:0002437`*(verify)*, corpus callosum `UBERON:0002336`, lateral ventricle `UBERON:0002285`, septum pellucidum `UBERON:0002094`*(verify)*, cerebellum `UBERON:0002037` (mouse degeneration data), optic nerve `UBERON:0000941`
- **Cranium / skull** `UBERON:0003128` — cranial suture `UBERON:0006842`*(verify)*
- **Face / craniofacial skeleton** — mandible `UBERON:0001684`, palate `UBERON:0001716`, tongue `UBERON:0001723`, lip `UBERON:0001833`, nose `UBERON:0000004`

**Secondary / systemic:**
- **Heart** `UBERON:0000948` — interatrial septum, interventricular septum, aorta `UBERON:0000947`, aortic valve `UBERON:0002137`, left ventricular myocardium (non‑compaction)
- **Larynx** `UBERON:0001737` (laryngomalacia, subglottic stenosis)
- **Lung / respiratory system** `UBERON:0001004` (aspiration, pneumonia)
- **Thyroid gland** `UBERON:0002046` (hypothyroidism)
- **Ear / middle ear** `UBERON:0001756` (conductive hearing loss)
- **Eye** `UBERON:0000970` (nystagmus, strabismus, optic nerve hypoplasia)
- **Hand / digits** `UBERON:0002398` (short palms, tapered fingers, broad thumbs)
- **Abdominal wall** (umbilical hernia); **foot** (talipes)

**Body systems:** nervous (central and peripheral reflex arc), musculoskeletal/craniofacial, cardiovascular, respiratory/upper airway, endocrine, gastrointestinal (feeding), sensory.

### Tissue and cell level

- **Neuroepithelium / ventricular and subventricular zone** — the primary site of the cellular lesion
- **Neural progenitor cells** `CL:0011020`; **radial glia** `CL:0000681` / `CL:0013000`; **intermediate (basal) progenitors** (TBR2⁺/INSM1⁺ — no precise CL term; use `CL:0011020` with a more specific `preferred_term`)
- **Neurons** — reduced production; **oligodendrocytes/myelin** — hypomyelination
- **Cranial suture osteogenic tissue** — premature fusion
- **Cardiac septal/valvular mesenchyme** — CHD
- **Laryngeal cartilage/connective tissue** — laryngomalacia

### Subcellular level

- **Nucleus / nucleoplasm** `GO:0005654` — primary site of SNIP1 action
- **Spliceosomal complex** `GO:0005681` — the direct molecular machine affected
- **PcG protein complex (PRC2)** `GO:0031519`
- **Mitochondrion** — indirectly, via the intrinsic (caspase‑9/apoptosome) apoptotic pathway `GO:0097193`

### Localization / lateralization

**Bilateral and symmetric** throughout (brain malformations, craniosynostosis, hand anomalies, nystagmus/strabismus). No lateralized or asymmetric pattern reported. Cloverleaf skull reflects **multi‑suture, bilateral** synostosis.

---

## 8. Temporal Development

### Onset

- **Congenital / neonatal.** Hypotonia and poor feeding are apparent in early infancy; the HPO annotation explicitly records **onset = "Early infancy"** for feeding difficulties.
- 54% are **small for gestational age**, indicating prenatal growth effects.
- Onset pattern: **congenital and insidiously evolving** — the craniofacial gestalt is described as evolving over time ("*Dysmorphic features that evolve over time…*" **[BODY, PMID:22279524]**), so the disorder may be less recognisable in the neonatal period than in later childhood.
- Seizure onset: **infantile or childhood**.

Suggested HPO onset terms: `HP:0003577` Congenital onset · `HP:0003623` Neonatal onset · `HP:0003593` Infantile onset.

### Progression

- **Course:** static‑encephalopathy‑like in its developmental substrate, but with **progressive** craniofacial/skull features, **progressive** epilepsy burden in some, and **cumulative** complications (aspiration, airway, cardiomyopathy).
- **Rate:** slow; developmental gains continue (ambulation achieved between ages 3 and 10 years).
- **Duration:** chronic, lifelong; not self‑limited.
- **Stages:** no formal staging system exists. A practical framing: (i) neonatal — hypotonia/feeding/airway; (ii) infancy–early childhood — seizure onset, skull evolution, CHD management; (iii) mid‑childhood — motor gains, behavioural phenotype, drug‑resistant epilepsy; (iv) adolescence/adulthood — poorly characterised (oldest patient in the 2021 cohort was 26 years).

### Patterns

- **Remission:** none. No spontaneous or treatment‑induced remission of the core phenotype. Seizures are not reliably remitting.
- **Critical periods / windows of intervention:**
  - **Prenatal/early embryonic** — the true window for the neurodevelopmental lesion (mouse dysplasia is established by E15); realistically unreachable therapeutically.
  - **Neonatal** — airway and feeding intervention; newborn hearing screen; echocardiogram.
  - **Infancy** — early EEG and anticonvulsant optimisation (explicitly recommended to prevent status epilepticus and treat apnoea).
  - **Infancy–early childhood** — craniosynostosis surgical timing.
  - **Ongoing** — thyroid surveillance, cardiomyopathy surveillance.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** **not formally estimated.** No population prevalence figure exists. The disorder is **ultra‑rare worldwide** and effectively **population‑restricted to Old Order Amish**.
- **Cases described:** **51 affected individuals of Old Order Amish descent identified across 21 families / 27 sibships**, of whom **35 were clinically evaluated** (19 M, 16 F), age range 1 month – 26 years **[BODY, PMID:34570759]**; plus 3 individuals from 2 sibships in the original 2012 report (overlapping cohort).
- **Recommended dismech `Prevalence` records:**
  - `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`, `population: Worldwide`, notes: 51 affected individuals identified (Ammous 2021).
  - `measure_type: CARRIER_FREQUENCY`, `population: Old Order Amish`, `rate_per_100000: 2941` (1/34 ≈ 2.94%), source GeneReviews NBK558237.
  - `measure_type: CARRIER_FREQUENCY`, `population: Old Order Amish control chromosomes (Puffenberger 2012)`, 5/203 chromosomes = 2.5% allele‑carrier estimate.
  - Allele‑frequency records for PA Amish (0.5%) vs OH/IN/WI Amish (1.4%).
- **Incidence:** not reported. A rough derivation from a 1/34 carrier frequency under random mating within the community gives an expected affected‑birth rate of ~1/4,600 — **do not curate this as a sourced figure**; it is an inference, and Amish mating is not random.

### Inheritance

- **Pattern:** **Autosomal recessive** — HPO `HP:0000007`; suggested GENO/inheritance binding per dismech `Inheritance` class with `inheritance_term` = `HP:0000007` and `term:` populated.
- **Penetrance:** **complete** in homozygotes within the studied cohort — "*no unaffected individuals being homozygous for this variant*" **[BODY, PMID:34570759]**.
- **Expressivity:** **variable but with an invariant core.** Eight features are 100% penetrant (GDD, hypotonia, hyporeflexia, seizures, feeding difficulties, abnormal skull shape, high palate, wide mouth/cupid's bow); the variable features are cardiac, endocrine, airway, ophthalmologic and MRI findings. Cloverleaf skull occurred in only 5 individuals — the most striking intra‑genotype variability.
- **Anticipation:** not applicable (not a repeat‑expansion disorder).
- **Germline mosaicism:** not reported.
- **Founder effect:** **yes — this is the defining epidemiological feature.** A single Amish founder haplotype accounts for ~100% of pathogenic *SNIP1* alleles in this population.
- **Consanguinity:** central. The disorder was mapped by **autozygosity/homozygosity mapping** in an endogamous population; all patients are homozygous by descent.
- **Carrier frequency:** 1/34 Old Order Amish (GeneReviews 2023).

### Population demographics

- **Affected populations:** Old Order Amish (Pennsylvania; Ohio/Indiana/Wisconsin settlements). gnomAD contains 11 heterozygotes, **10 of whom are Amish** — i.e., the variant is essentially absent from non‑Amish populations.
- **Geographic distribution:** Lancaster County PA; Geauga County OH and related Midwest settlements. The **allele frequency differs ~3‑fold between settlements** (0.5% PA vs 1.4% OH/IN/WI), a classic sub‑founder‑effect signal.
- **Sex ratio:** ~1:1 (19 M : 16 F in the evaluated cohort) — consistent with autosomal inheritance.
- **Age distribution:** paediatric‑weighted; 1 month to 26 years in the reported cohort. **Adult natural history is essentially undescribed — a major knowledge gap.**

---

## 10. Diagnostics

### Clinical tests

| Domain | Test | Findings / purpose |
|---|---|---|
| Electrophysiology | **EEG** — LOINC/`HP:0002353` EEG abnormality | Abnormal; the 2021 paper recommends "*EEG should be obtained at an early stage*" **[BODY]** |
| Imaging | **Brain MRI** | 50% abnormal; hydrocephalus, ventriculomegaly, white‑matter change, thin corpus callosum, hypomyelination, irregular cortical ribbon, Chiari malformation, absent septum pellucidum, optic nerve hypoplasia, septo‑optic dysplasia |
| Imaging | **Skull CT / 3D CT** | multi‑suture craniosynostosis, cloverleaf skull, irregular calvarial surface |
| Imaging | **Echocardiogram** | ASD, VSD, coarctation, bicuspid aortic valve, aortic stenosis; LV non‑compaction cardiomyopathy. "*echocardiogram should be undertaken to screen for congenital heart defects*" **[BODY]** |
| Laboratory | **Thyroid function (TSH, free T4)** | hypothyroidism in 25% |
| Laboratory | **Glucose** | hypoglycaemia in ~20% |
| Functional | **Video‑fluoroscopic swallow study / modified barium swallow** | aspiration in 46% |
| Functional | **Direct laryngoscopy / bronchoscopy; sleep study** | laryngomalacia, subglottic stenosis, apnoea |
| Sensory | **Newborn hearing screen / audiology** | 21% failed (conductive) |
| Sensory | **Ophthalmology** | nystagmus, strabismus, optic nerve hypoplasia |
| Biopsy / pathology | **None indicated** | No diagnostic histopathology or IHC exists for this disorder |

**Biomarkers:** none. No circulating protein, metabolite, or imaging biomarker is validated. **Curation gap.**

### Genetic testing

**Recommended approach, tiered:**

1. **Targeted single‑variant testing** for `SNIP1 c.1097A>G` in any Plain‑community child with the phenotype. A dedicated clinical assay exists: **DDC Clinic Laboratory, "Symptomatic Epilepsy and Skull Dysplasia (SNIP1) Targeted Testing."** Amish/Mennonite multi‑variant founder panels (Clinic for Special Children, DDC Clinic) also include it. This is the **highest‑yield, lowest‑cost first‑line test in the at‑risk population**, and the GeneReviews Amish founder‑variant chapter lists it accordingly.
2. **Exome (WES) or genome (WGS) sequencing** for non‑Plain patients or phenotype‑first presentations — this is how the gene was discovered (WES at the Broad Institute, PMID:22279524) and remains the only route to identify hypothetical non‑founder *SNIP1* alleles.
3. **Epilepsy / intellectual‑disability gene panels** — *SNIP1* is included on many commercial NDD and epilepsy panels (see NCBI GTR, "Clinical and research tests for SNIP1").
4. **Chromosomal microarray (CMA)** — relevant for detecting **1p34.3p34.2 deletions** encompassing *SNIP1* (PMID:29726122), a different mechanism/phenotype.
5. **Karyotype, FISH, mtDNA testing, repeat‑expansion testing:** **not indicated.**
6. **SNP‑array autozygosity mapping** — the research method that mapped the locus; still relevant in consanguineous families with unsolved phenotypes.

### Omics‑based diagnostics

- **RNA sequencing:** research‑grade only. Patient transcriptome signatures (TGF‑β EMT pathway, ROBO1/CNTNAP2/PAFAH1B1) are **not** validated as a diagnostic assay. Given the splicing mechanism (§6.2), RNA‑seq for aberrant splicing/detained‑intron signatures is a **plausible but unvalidated** future diagnostic — worth recording as a `discussions` `KNOWLEDGE_GAP` with proposed experiments.
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** none available or applicable.

### Clinical criteria

**No formal consensus diagnostic criteria (no DSM/ICD/society guideline) exist.** Diagnosis is **molecular**, supported by a recognisable gestalt. Practical criteria: Old Order Amish ancestry + neonatal hypotonia/poor feeding + severe non‑verbal GDD + epilepsy + wide mouth/cupid's‑bow/high palate/abnormal skull shape → targeted *SNIP1* testing.

### Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| Other Amish/Plain founder NDDs (e.g. *BRAT1* lethal neonatal rigidity‑multifocal seizure, *TUBGCP6*, *CRADD*, *HARS*, *SLC6A3*, *FLVCR1* — all in the same 2012 discovery paper) | Overlapping community and severe‑NDD phenotype; distinguished molecularly, and by the *SNIP1* skull/craniofacial gestalt |
| **Syndromic craniosynostosis** (FGFR2/FGFR3/TWIST1 — Pfeiffer, Crouzon, Apert; cloverleaf skull) | Cloverleaf skull overlaps strikingly; distinguished by AD inheritance, limb findings, and normal/near‑normal cognition in many |
| **Developmental and epileptic encephalopathies** (STXBP1, CDKL5, SCN2A, etc.) | Lack the distinctive craniofacial/skull gestalt and near‑universal CHD/airway involvement |
| **Pierre Robin sequence** syndromes (*SOX9* regulatory, Stickler, *EFTUD2*/MFDM) | Present in 3 *SNIP1* patients; MFDM (EFTUD2) is another spliceosomopathy with craniofacial disease |
| **Septo‑optic dysplasia** (*HESX1*, etc.) | Overlapping midline MRI findings in a subset |
| **1p34.3p34.2 microdeletion** | Heterozygous CNV, milder ID, distinct feature set |
| **Chromosomal/CNV disorders generally** | Excluded by CMA |

### Screening

- **Newborn screening:** *SNIP1* is **not** on any state NBS panel and the disorder is not NBS‑amenable (no biochemical marker). However, the **failed newborn hearing screen in 21%** is a real incidental ascertainment route.
- **Carrier screening:** highly appropriate and actively practiced — the variant is on Plain‑community founder‑variant carrier panels (Clinic for Special Children; DDC Clinic).
- **Cascade screening:** standard for at‑risk siblings and extended family in an endogamous pedigree structure.

---

## 11. Outcome / Prognosis

### Survival and mortality

**[BODY] PMID:34570759** — "*Six children died between ages 9 months and 11 years as a consequence of infection, sudden cardiopulmonary arrest, or accidental drowning.*"

- **Case fatality in the reported cohort:** 6 deaths among the evaluated individuals — **≈17% mortality in a cohort spanning 1 month to 26 years.** This is a crude, non‑actuarial figure; **no Kaplan–Meier survival curve, 5‑/10‑year survival rate, or life‑expectancy estimate has been published.**
- **Causes of death (all three named):** infection; sudden cardiopulmonary arrest; accidental drowning.
- **Disease‑specific mortality mechanisms:** aspiration/respiratory infection (46% aspiration rate, 75% upper‑airway abnormality), cardiac (CHD in 60%, LVNC cardiomyopathy in 12% — the plausible substrate for "sudden cardiopulmonary arrest"), and seizure‑related risk (status epilepticus; drowning during an unwitnessed seizure is a well‑recognised epilepsy mortality mode). SUDEP is **not** explicitly invoked by the authors — do not assert it.
- Survival to at least **26 years** is documented.

### Morbidity and function

- **Cognitive:** severe intellectual disability, non‑verbal.
- **Motor:** most achieve independent ambulation (ages 3–10 years) — a meaningfully better motor outcome than the cognitive outcome.
- **Communication:** some use signs, gestures, and sounds; no spoken language.
- **Feeding:** universal difficulty; gastrostomy dependence common.
- **Disability outcome:** lifelong, profound dependence for self‑care; ICF‑level severe activity limitation across learning, communication, and self‑care domains.
- **Quality‑of‑life instruments:** **none applied.** No EQ‑5D, PedsQL, PROMIS, or disease‑specific measure has been reported.

### Complications

Recurrent respiratory infection and pneumonia (aspiration‑driven); status epilepticus; apnoea (infancy); airway obstruction (laryngomalacia, subglottic stenosis); congestive heart failure/arrhythmia risk from CHD and LVNC; raised intracranial pressure and secondary visual/neurological compromise from multi‑suture craniosynostosis; hydrocephalus; hypothyroidism; hypoglycaemia; conductive hearing loss; failure to thrive; orthopaedic sequelae (talipes, kyphoscoliosis in the deletion case).

### Recovery potential

**None.** No recovery or reversal of the neurodevelopmental phenotype is possible; management is entirely supportive and complication‑preventive.

### Prognostic factors

Not formally studied. Clinically plausible (and explicitly targeted by the authors' management recommendations) determinants of outcome: **severity/multiplicity of craniosynostosis**, **presence and severity of CHD or cardiomyopathy**, **degree of airway compromise and aspiration**, and **seizure control**. **Prognostic biomarkers: none.** All of the above should be recorded as clinical reasoning, not as evidenced prognostic factors.

---

## 12. Treatment

**There is no disease‑modifying or targeted therapy.** Management is entirely **supportive, anticipatory, and multidisciplinary**. The 2021 *PLoS Genetics* paper is the only source of formal management recommendations.

### Key management recommendations (from PMID:34570759, **[BODY]**)

- "*elective gastrostomy tube placement to support growth and limit pulmonary aspiration*"
- "*careful optimisation of anticonvulsant medications to treat apnea in infancy, maintain seizure control, and prevent status epilepticus*"
- "*EEG should be obtained at an early stage*"
- "*Neuroimaging should be performed at diagnosis, and echocardiogram should be undertaken to screen for congenital heart defects*"

### Treatment table with suggested NCIT annotations

| Treatment | Description | Suggested `treatment_term` (NCIT) | `therapeutic_modality` |
|---|---|---|---|
| **Antiseizure medication** | No agent provides consistently effective control; multi‑drug resistance common; goal is seizure reduction, apnoea control in infancy, and status‑epilepticus prevention | `NCIT:C15986` Pharmacotherapy; `therapeutic_agent` should be **omitted or generic** — no specific agent is endorsed | `SMALL_MOLECULE` |
| **Gastrostomy tube placement (elective)** | Supports growth, limits aspiration | `NCIT:C157864` Gastrostomy Tube Procedure *(verify reachability from NCIT:C25218; fallback `NCIT:C15329` Surgical Procedure)* | `SURGERY` |
| **Craniosynostosis / cranial vault surgery** | For multi‑suture and cloverleaf synostosis, ICP management | `NCIT:C15329` Surgical Procedure *(a more specific cranioplasty term should be sought with OAK)* | `SURGERY` |
| **Airway surgery (supraglottoplasty, tracheostomy)** | For laryngomalacia, subglottic stenosis, obstructive apnoea | `NCIT:C15329` Surgical Procedure | `SURGERY` |
| **Cardiac surgery / catheter intervention** | ASD/VSD repair, coarctation repair | `NCIT:C15329` Surgical Procedure | `SURGERY` |
| **Levothyroxine replacement** | For hypothyroidism (25%) | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` levothyroxine (`CHEBI:81826` *levothyroxine* — **verify with OAK**) | `SMALL_MOLECULE` |
| **Nutritional support** | Growth failure, feeding difficulty | `NCIT:C15433` Nutritional Support | *(do not auto‑tag `BEHAVIORAL` — see CLAUDE.md guidance)* |
| **Physical therapy** | Hypotonia, ambulation training | `NCIT:C15302` Physical Therapy | `BEHAVIORAL` |
| **Occupational therapy** | Self‑care, adaptive function | `NCIT:C121351` Occupational Therapy | `BEHAVIORAL` |
| **Speech and language therapy / AAC** | Non‑verbal communication, sign/gesture support | `NCIT:C159273` Speech Therapy | `BEHAVIORAL` |
| **Hearing amplification / ENT management** | Conductive loss (21%) | *(no reliable NCIT clinical‑action term for device use)* | `DEVICE` |
| **Ophthalmologic management** | Strabismus, nystagmus, optic nerve hypoplasia | `NCIT:C15329` Surgical Procedure (strabismus surgery) / supportive | `SURGERY` |
| **Supportive / palliative care** | Symptom management, family support | `NCIT:C15747` Supportive Care | `OTHER` |
| **Genetic counselling** | AR recurrence risk 25%; carrier testing for relatives | `NCIT:C15240` Genetic Counseling | `BEHAVIORAL` |

### Pharmacogenomics

**None established.** No *SNIP1*‑specific PGx guidance (no CPIC/PharmGKB entry). Standard antiseizure‑drug PGx caveats apply generically (e.g. HLA‑B*15:02 and carbamazepine), but are **not disorder‑specific** — do not curate as SNIP1‑related.

### Advanced therapeutics

- **Gene therapy / gene editing:** none; not in preclinical development for this indication.
- **ASO / RNA therapy:** none. *Note the conceptual tension:* the pathogenic mechanism is a **splicing‑machinery** defect (trans‑acting), not a cis‑acting splice variant, so classical exon‑skipping ASO logic does **not** apply. Do **not** associate this entry with the `antisense_oligonucleotide_therapy` module.
- **Cell therapy, immunotherapy, targeted small molecules:** none.
- **Theoretical target from mouse work:** the *Nat Commun* 2023 finding that **PRC2 (EED) depletion rescues apoptosis and brain dysplasia** in *Snip1*‑null mouse brain identifies **PRC2/EZH2 inhibition** as a mechanistically motivated but entirely unproven therapeutic hypothesis. There is **no** human, in‑vivo‑disease, or translational evidence, and the rescue was in a **null** (not E366G) background during **embryonic** development — a window that is not clinically actionable. **Record as a `mechanistic_hypotheses` entry with `status: EMERGING` and a `HUMAN_MODEL_MISMATCH` discussion, not as a treatment.**

### Clinical trials

**A ClinicalTrials.gov API v2 query for "SNIP1" returned zero studies** (retrieved 2026‑08‑01). No interventional or observational trial is registered for this disorder.

### Treatment outcomes

- **Response rates:** not reported for any intervention. The single explicit efficacy statement is a **negative** one — no antiepileptic provides consistent seizure control.
- **Adverse events:** no disorder‑specific AE data. Standard risks of gastrostomy, craniofacial surgery, and antiseizure polypharmacy apply.

### Treatment strategy

No published algorithm. The de‑facto pathway from the 2021 paper: **molecular diagnosis → baseline EEG + brain MRI + echocardiogram → airway and swallow assessment → early elective gastrostomy → anticonvulsant optimisation → craniofacial surgical assessment → thyroid surveillance → developmental therapies → genetic counselling and family carrier testing.** Personalised‑medicine approaches beyond genotype‑confirmed diagnosis: none.

---

## 13. Prevention

### Primary prevention

Not possible for an affected conceptus. Population‑level primary prevention operates entirely through **reproductive genetics**:
- **Carrier screening** in Plain communities (Clinic for Special Children, DDC Clinic founder‑variant panels) — high yield given a 1/34 carrier frequency.
- **Genetic counselling** with 25% sibling recurrence risk.
- **Reproductive options:** partner carrier testing, prenatal diagnosis (CVS/amniocentesis targeted variant testing), preimplantation genetic testing for monogenic disease (PGT‑M) where culturally acceptable. *(Note: uptake of PGT‑M and pregnancy termination is culturally constrained in Plain communities; counselling in these communities is typically framed around informed reproductive decision‑making and preparedness, not termination.)*

### Secondary prevention (early detection)

- **Cascade/at‑birth targeted testing** in known carrier families, enabling neonatal anticipatory care rather than diagnostic odyssey.
- The 2021 recommendations are essentially a secondary‑prevention program: **early EEG, baseline neuroimaging, screening echocardiogram, hearing screen, thyroid function testing, swallow assessment.**

### Tertiary prevention (complication prevention) — the highest‑value tier here

- **Elective (pre‑emptive) gastrostomy** to prevent aspiration pneumonia and growth failure — this is an explicit prevention‑framed recommendation.
- **Anticonvulsant optimisation** to prevent **status epilepticus** and treat infantile apnoea.
- **Water safety supervision** — accidental drowning was one of three named causes of death in a cohort where every patient has epilepsy. This is an obvious, concrete, family‑level preventive measure, though it is not stated as a formal recommendation in the paper.
- **Cardiac surveillance** for CHD and LVNC cardiomyopathy.
- **Thyroid surveillance** for treatable hypothyroidism.
- **Airway surveillance** and timely ENT intervention.
- **ICP monitoring / timely craniofacial surgery** in multi‑suture synostosis.

### Immunization

No disease‑specific vaccine. **Routine and enhanced immunisation (influenza, pneumococcal, RSV) is clinically important** given aspiration risk and infection as a leading cause of death — but this is general good practice, not a published disorder‑specific recommendation. Suggested NCIT if curated: `NCIT:C15346` Vaccination, `therapeutic_modality: VACCINE`. *Note: vaccination coverage is historically lower in some Plain communities, which is a real public‑health consideration for this population.*

### Public health / environmental interventions

Community‑partnered genetics services (the Clinic for Special Children / DDC Clinic model) are the operative public‑health intervention: low‑cost founder‑variant testing embedded in a trusted community clinic. No environmental intervention applies.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBI Taxon | Gene | NCBI Gene ID | Notes |
|---|---|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | *SNIP1* | 79753 | |
| *Mus musculus* | `NCBITaxon:10090` | *Snip1* | **76793** | MGI:2156003; chromosome 4, 124,960,465–124,967,835 bp (+); 57.99 cM |
| *Rattus norvegicus* | `NCBITaxon:10116` | *Snip1* | **313588** | RGD:1359268 |
| *Danio rerio* | `NCBITaxon:7955` | *snip1* (a.k.a. *pml1*) | **793873** *(verify)* | RES complex component |
| *Saccharomyces cerevisiae* | `NCBITaxon:4932` | *PML1* | — | The yeast RES‑complex subunit; the source of SNIP1's alias "PML1" |
| *Arabidopsis thaliana* | `NCBITaxon:3702` | *DAWDLE (DDL)* | — | Functional analogue: FHA‑domain protein in small‑RNA biogenesis (PMID:18632581) |

### Breed

**Not applicable** — no VBO breed association; no domestic‑animal breed disorder is known.

### Natural disease in other species

**None identified.** Targeted searching found **no OMIA entry** for *SNIP1* in any species — no naturally occurring SNIP1‑related disease is recorded in dogs, cattle, horses, or other domestic animals as of this search. All animal data are **experimentally induced** (§15).

> Caveat: this is a "not found in search" result, not a proof of absence. Curate as "no naturally occurring animal disease reported" rather than as a positive negative.

### Comparative biology and evolutionary conservation

- **SNIP1 is deeply conserved** — described as "*a highly conserved nuclear protein*" **[ABSTRACT, PMID:38304835]**. Glu366 itself is "*highly conserved*" across species **[BODY, PMID:22279524]**, which is the conservation argument underpinning pathogenicity.
- **The RES complex (Bud13p/Pml1p/Snu17p) is conserved from yeast to vertebrates**, and its splicing function is conserved: **[ABSTRACT, PMID:29969449]** "*The retention and splicing (RES) complex is formed by three different proteins (Bud13p, Pml1p and Snu17p) and is involved in splicing in yeast.*"
- **The neurodevelopmental requirement is conserved across vertebrates** — zebrafish *snip1* mutants and mouse *Snip1* conditional knockouts both show excess brain cell death and reduced neurogenesis (see §15), matching the human cortical/midline malformation phenotype. This cross‑species convergence is the single strongest argument that the human disorder is a **neural‑progenitor‑survival disease**.
- **Divergence to note:** mouse *Snip1* null is prenatally lethal, whereas humans homozygous for E366G survive to adulthood — consistent with E366G being **hypomorphic rather than null**. This is a genuine human‑model mismatch to record.

### Transmission

**Not applicable** — non‑infectious, non‑zoonotic, no cross‑species susceptibility.

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*) — the principal model

**MGI:2156003**, *Snip1*, chromosome 4. MGI records **15 mutations/alleles**: 1 ENU chemically induced, 2 other chemically induced, 5 endonuclease‑mediated, 1 gene‑trapped, 1 radiation‑induced, 5 targeted, 4 genomic mutations.

**Constitutive null — IMPC / MGI:**
> "*Mice homozygous for a knock-out allele exhibit prenatal lethality.*" (MGI phenotype summary)

IMPC data for **`Snip1^tm1a(EUCOMM)Wtsi`**:

| MP phenotype | Zygosity | Sex | p‑value |
|---|---|---|---|
| Preweaning lethality, complete penetrance | homozygote | — | 0.0 |
| Abnormal tail movements | heterozygote | — | 7.93E‑6 |
| Decreased circulating total protein level | heterozygote | male | 7.29E‑8 |
| Decreased circulating iron level | heterozygote | male | 2.66E‑5 |
| Abnormal placement of pupils | heterozygote | female | 1.54E‑5 |

*(Note the heterozygous neurological/ocular signals — "abnormal tail movements," "abnormal placement of pupils" — which weakly echo the human nystagmus/strabismus and neurological phenotype and support dosage sensitivity. Treat as suggestive only; IMPC het findings are noisy.)*

**Conditional neural knockout — the disease‑relevant model (PMID:37553330):**
- **Allele/driver:** `Snip1-tm1a` (Infrafrontier/EMMA 04224) → crossed to **Actin‑FLPe** to make `Snip1‑flox` → crossed to **Nestin‑Cre** = **`Snip1_Nes-KO`** (neural‑progenitor‑specific deletion) **[BODY]**
- **Phenotype:** "*By E15, Snip1_Nes-KO embryos displayed severe thinning of brain tissues and dysplasia with 100% penetrance*" **[BODY]**
- **Cellular:** marked reduction of SOX2⁺ NPCs and TBR2⁺ / INSM1⁺ intermediate progenitors; strong cleaved‑caspase‑3 induction in all ventricles; **caspase‑9 inhibition robustly reduced apoptosis** (caspase‑8 only modestly) **[BODY]**
- **Rescue:** **[ABSTRACT]** "*Depletion of PRC2 is sufficient to reduce apoptosis and brain dysplasia and to partially restore genetic programs in the SNIP1-depleted brain in vivo.*"

**Conditional cerebellar knockout — neurodegeneration model (PMID:37027487):**
- **[ABSTRACT]** "*Haploinsufficiency of Snip1 attenuates neurodegeneration and globally rescues IDT accumulation caused by a previously reported mutant U2 snRNA, a basal spliceosomal component. Snip1 conditional knockout in the cerebellum decreases DI splicing efficiency and causes neurodegeneration.*"
- Note the **bidirectional** result: *Snip1* haploinsufficiency is *protective* in a mutant‑U2 neurodegeneration background, while cerebellar *Snip1* cKO is *causative*. This is a genuinely non‑trivial dose/context dependency worth capturing as a `mechanistic_hypotheses` nuance.

### 15.2 Zebrafish (*Danio rerio*)

**PMID:29969449** — Fernandez JP, Moreno‑Mateos MA, Gohr A, et al. "RES complex is associated with intron definition and required for zebrafish early embryogenesis." *PLoS Genet* 2018;14(7):e1007473. doi:10.1371/journal.pgen.1007473

**[ABSTRACT]** "*In this study, we have generated loss-of-function mutants for the three components of the RES complex in zebrafish and showed that they are required during early development. The mutants showed a marked neural phenotype with increased cell death in the brain and a decrease in differentiated neurons. Transcriptomic analysis of bud13, snip1 (pml1) and rbmx2 (snu17) mutants revealed a global defect in intron splicing, with strong mis-splicing of a subset of introns.*"

This is the **most phenotype‑congruent model for the human brain phenotype at the whole‑organism level**: brain‑specific cell death + reduced neuron production + global splicing defect, all in one organism, and it independently corroborates the mouse NPC‑apoptosis result via a completely different route (splicing rather than PRC2).

### 15.3 Cellular / in vitro systems

- **HEK293/HeLa transfection studies of the E366G mutant** (PMID:22279524) — showed nuclear aggregation and ~85% reduced protein abundance.
- **Acute SNIP1 depletion + FHA‑domain mutant rescue in human cells** (PMID:41904131) — quantitative proteomics of chromatin‑associated spliceosomes, iCLIP‑seq; **directly tested the E366G variant** and showed impaired P‑SF3B1 binding, splicing defects, and reduced cell viability. **This is the definitive variant‑specific functional assay available.**
- **iPSC / organoid models:** **none published.** Given the NPC‑apoptosis mechanism, patient‑derived iPSC cortical organoids are the obvious missing model — a strong candidate for a `proposed_experiments` entry in a `KNOWLEDGE_GAP` discussion.
- **MorPhiC:** *SNIP1* is **not** among the named MorPhiC anchor genes (ISL1, EOMES, GCM1, NKX2‑1); no MorPhiC dataset applies.

### 15.4 Phenotype recapitulation and limitations

| Human feature | Mouse (Nes‑cKO) | Zebrafish | Recapitulated? |
|---|---|---|---|
| Brain dysplasia / cortical malformation | ✅ severe, 100% penetrant | ✅ increased brain cell death | **Yes** |
| Reduced neurogenesis | ✅ NPC/IPC loss | ✅ fewer differentiated neurons | **Yes** |
| Seizures | ✗ not assessed (embryonic lethality precludes) | ✗ | **No** |
| Craniofacial gestalt / craniosynostosis | ✗ not reported | ✗ | **No** |
| Congenital heart defects | ✗ not reported | ✗ | **No** |
| Hypotonia / feeding failure | ✗ | ✗ | **No** |
| Survival to adulthood | ✗ (null = lethal) | ✗ (early lethal) | **No — key mismatch** |

**Limitations to record explicitly (candidate `HUMAN_MODEL_MISMATCH` discussion):**
1. **No E366G knock‑in mouse exists.** Every in‑vivo model is a **null or conditional null**, whereas the human allele is a **hypomorph**. Null mice die prenatally; humans live to at least 26 years. Conclusions about the human disorder drawn from null models are therefore **directionally informative but quantitatively wrong**.
2. Nestin‑Cre deletion is **neural‑restricted**, so it cannot model the craniofacial, cardiac, airway, or endocrine components — i.e., the multisystem, "recognisable syndrome" part of the disease is entirely unmodelled.
3. Embryonic lethality precludes modelling **epilepsy**, the single most disabling human feature.
4. The **PRC2‑depletion rescue** was performed in a null background during embryogenesis — it does not establish that PRC2 inhibition would help a living patient with a hypomorphic allele.
5. Zebrafish *snip1* mutants are studied as **RES‑complex** loss, not as a disease model per se.

### 15.5 Model resources

MGI (informatics.jax.org, MGI:2156003) · IMPC (`Snip1^tm1a(EUCOMM)Wtsi`) · **Infrafrontier/EMMA line 04224** (the tm1a allele used in PMID:37553330) · EUCOMM/KOMP repositories · RGD (RGD:1359268) · ZFIN (zebrafish *snip1*/*pml1* mutants from PMID:29969449) · Alliance of Genome Resources.

---

## Appendix A — Consolidated reference list

| PMID | Citation | Role | Evidence source |
|---|---|---|---|
| **34570759** | Ammous Z, Rawlins LE, Jones H, et al. A biallelic SNIP1 Amish founder variant causes a recognizable neurodevelopmental disorder. *PLoS Genet* 2021;17(9):e1009803. doi:10.1371/journal.pgen.1009803 | **Primary clinical cohort (n=35–51); management recommendations; patient transcriptome** | HUMAN_CLINICAL |
| **22279524** | Puffenberger EG, Jinks RN, Sougnez C, et al. Genetic mapping and exome sequencing identify variants associated with five novel diseases. *PLoS One* 2012;7(1):e28936. doi:10.1371/journal.pone.0028936 | **Gene discovery; mapping; carrier frequency; E366G protein instability** | HUMAN_CLINICAL (+ IN_VITRO for the mutant‑protein experiments — **split into two evidence items**) |
| **41904131** | Gajdušková P, Ruiz de Los Mozos I, Hluchý M, et al. Phosphorylation of SF3B1 by CDK11 orchestrates spliceosome activation via SNIP1‑dependent RES complex recruitment. *Nat Commun* 2026. doi:10.1038/s41467-026-71119-2 | **Definitive E366G functional mechanism (splicing)** | IN_VITRO |
| **37553330** | Matsui Y, Djekidel MN, Lindsay K, et al. SNIP1 and PRC2 coordinate cell fates of neural progenitors during brain development. *Nat Commun* 2023;14:4771. doi:10.1038/s41467-023-40487-4 | **NPC apoptosis mechanism; PRC2/H3K27me3; mouse cKO** | MODEL_ORGANISM |
| **37027487** | Meng D, Zheng Q, Zhang X, et al. A molecular brake that modulates spliceosome pausing at detained introns contributes to neurodegeneration. *Protein Cell* 2023;14(1):27–53. doi:10.1093/procel/pwac008 | **SNIP1–RNPS1 spliceosome brake; cerebellar cKO neurodegeneration** | MODEL_ORGANISM |
| **29969449** | Fernandez JP, Moreno‑Mateos MA, Gohr A, et al. RES complex is associated with intron definition and required for zebrafish early embryogenesis. *PLoS Genet* 2018;14(7):e1007473. doi:10.1371/journal.pgen.1007473 | **Zebrafish snip1 mutant; brain cell death; splicing** | MODEL_ORGANISM |
| **38304835** | Chen Y, Guo W, Guo X, Wanqing Q, Yin Z. The clinical utilization of SNIP1 and its pathophysiological mechanisms in disease. *Heliyon* 2024;10(2):e24601. doi:10.1016/j.heliyon.2024.e24601 | **Review of SNIP1 biology (Smad4/RelA/c‑Myc)** | OTHER (review) |
| **10887155** | Kim RH, Wang D, Tsang M, et al. A novel smad nuclear interacting protein, SNIP1, suppresses p300‑dependent TGF‑β signal transduction. *Genes Dev* 2000 | SNIP1 discovery; TGF‑β arm | IN_VITRO |
| **11567019** | Kim RH, Flanders KC, Birkey Reffey S, et al. SNIP1 inhibits NF‑κB signaling by competing for its binding to the C/H1 domain of CBP/p300. *J Biol Chem* 2001 | NF‑κB arm | IN_VITRO |
| **15378006** | Roche KC, Wiechens N, Owen‑Hughes T, Perkins ND. The FHA domain protein SNIP1 is a regulator of the cell cycle and cyclin D1 expression. *Oncogene* 2004 | FHA domain; cell cycle | IN_VITRO |
| **17157259** | Fujii M, Lyakh LA, Bracken CP, et al. SNIP1 is a candidate modifier of the transcriptional activity of c‑Myc on E box‑dependent target genes. *Mol Cell* 2006 | c‑Myc arm | IN_VITRO |
| **17260016** | Roche KC, Rocha S, Bracken CP, Perkins ND. Regulation of ATR‑dependent pathways by the FHA domain containing protein SNIP1. *Oncogene* 2007 | DNA damage response | IN_VITRO |
| **18794151** | Bracken CP, Wall SJ, Barré B, et al. Regulation of cyclin D1 RNA stability by SNIP1. *Cancer Res* 2008 | Cyclin D1 mRNA stability | IN_VITRO |
| **18632581** | Yu B, Bi L, Zhai J, et al. The FHA domain proteins DAWDLE in Arabidopsis and SNIP1 in humans act in small RNA biogenesis. *PNAS* 2008 | miRNA biogenesis; plant ortholog | IN_VITRO |
| **30404004** | Chen LL, Lin HP, Zhou WJ, et al. SNIP1 Recruits TET2 to Regulate c‑MYC Target Genes and Cellular DNA Damage Response. *Cell Rep* 2018 | Epigenetic (TET2) arm | IN_VITRO |
| **29726122** | Jacher JE, Innis JW. Interstitial microdeletion of the 1p34.3p34.2 region. *Mol Genet Genomic Med* 2018;6(4):649–654. doi:10.1002/mgg3.409 | **Heterozygous CNV including SNIP1 — distinct entity** | HUMAN_CLINICAL |
| **29426045** | Ruan H, Zhang Z, Tian L, et al. Smad nuclear interacting protein 1 (SNIP1) inhibits intestinal inflammation through regulation of epithelial barrier function. *Mucosal Immunol* 2018 | Non‑neural SNIP1 biology (context) | MODEL_ORGANISM |

**Non‑PMID resources:** GeneReviews NBK558237 (Wallace SE, Puffenberger EG, Bean LJH, "Genetic Disorders Associated with Founder Variants Common in the Amish Population," last update 2023‑12‑07) · OMIM #614501 and *608241 · ClinVar Variation 30717 / RCV000023695 · dbSNP rs387906986 · UniProt Q8TAD8 · HGNC:30587 · MGI:2156003 · IMPC · HPO disease annotations for OMIM:614501 (ontology.jax.org) · NCBI GTR (SNIP1 tests) · DDC Clinic Laboratory (Symptomatic Epilepsy and Skull Dysplasia targeted test) · Clinic for Special Children.

---

## Appendix B — Curation gaps and open questions (candidate `discussions` entries)

| Gap | Kind | Note |
|---|---|---|
| No Orphanet/ORDO entry exists for this disorder | `KNOWLEDGE_GAP` | Verified absent in OLS4 ORDO; MONDO carries no ORPHA xref. Consider proposing one upstream. |
| No non‑Amish patients reported; entire disease concept rests on one founder allele | `KNOWLEDGE_GAP` | Systematic literature search (2021–2026) found no additional biallelic *SNIP1* families. Whether the phenotype generalises to other *SNIP1* alleles is unknown. |
| No E366G knock‑in animal model | `HUMAN_MODEL_MISMATCH` | All in‑vivo models are nulls; nulls are lethal, humans survive to ≥26 years. Proposed experiment: *Snip1^E366G/E366G* knock‑in mouse with EEG, craniofacial µCT, and echocardiography. |
| PRC2‑depletion rescue is embryonic and null‑background only | `HUMAN_MODEL_MISMATCH` | Cannot support a therapeutic claim. Proposed experiment: EZH2 inhibition in a hypomorphic model or patient iPSC‑derived cortical organoids. |
| Mechanism of hypoglycaemia (~20%) unexplained | `KNOWLEDGE_GAP` | Not attributable to any known SNIP1 function; may be secondary to feeding failure. |
| No adult natural‑history data | `KNOWLEDGE_GAP` | Oldest reported patient 26 years; whether the cerebellar‑cKO neurodegeneration phenotype has a human adult correlate is untested. |
| No patient iPSC/organoid model; no patient splicing (RNA‑seq detained‑intron) analysis | `KNOWLEDGE_GAP` | The 2026 splicing mechanism has never been tested in patient tissue. |
| No QoL, survival‑curve, or formal prognostic data | `KNOWLEDGE_GAP` | Mortality reported only as raw counts (6 deaths, ages 9 months–11 years). |
| FHA‑domain boundary discrepancy for residue 366 | `KNOWLEDGE_GAP` | UniProt FHA = 281–344 (E366 outside); PMID:34570759 says "close proximity to"; PMID:41904131 calls E366G an FHA‑domain mutation. Record both. |
| ClinVar "Likely pathogenic" (1★) vs publication "pathogenic" | — | Record both classifications with their sources; do not silently upgrade. |
| Candidate new mechanism module: **spliceosomopathy neurodevelopmental disorder** | — | *SNIP1* joins *EFTUD2*, *SF3B4*, *SNW1*, *SF3B1*, *RNU4‑2*; the "spliceosome/RES defect → NPC apoptosis → cortical malformation + craniofacial disease" chain is recurrent and modular. Worth proposing. |

---

**Sources:**
[PLOS Genetics — A biallelic SNIP1 Amish founder variant causes a recognizable neurodevelopmental disorder](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1009803) · [PMC8496849](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496849/) · [PLOS One — Genetic mapping and exome sequencing identify variants associated with five novel diseases](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0028936) · [OMIM #614501](https://omim.org/entry/614501) · [OMIM *608241](https://omim.org/entry/608241) · [ClinVar RCV000023695](https://www.ncbi.nlm.nih.gov/clinvar/RCV000023695/) · [HPO annotations for OMIM:614501](https://ontology.jax.org/api/network/annotation/OMIM:614501) · [MONDO:0013787 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0013787) · [HGNC SNIP1](https://rest.genenames.org/fetch/symbol/SNIP1) · [UniProt Q8TAD8](https://www.ebi.ac.uk/proteins/api/proteins/Q8TAD8) · [MGI:2156003 Snip1](https://www.informatics.jax.org/marker/MGI:2156003) · [IMPC Snip1 genotype–phenotype](https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select?q=marker_symbol:Snip1) · [GeneReviews — Genetic Disorders Associated with Founder Variants Common in the Amish Population (NBK558237)](https://www.ncbi.nlm.nih.gov/books/NBK558237/) · [PubMed 37553330](https://pubmed.ncbi.nlm.nih.gov/37553330/) · [PMC10409800](https://pmc.ncbi.nlm.nih.gov/articles/PMC10409800/) · [PubMed 41904131](https://pubmed.ncbi.nlm.nih.gov/41904131/) · [PubMed 37027487](https://pubmed.ncbi.nlm.nih.gov/37027487/) · [PubMed 29969449](https://pubmed.ncbi.nlm.nih.gov/29969449/) · [PubMed 38304835](https://pubmed.ncbi.nlm.nih.gov/38304835/) · [PubMed 29726122](https://pubmed.ncbi.nlm.nih.gov/29726122/) · [NCBI GTR — SNIP1 tests](https://www.ncbi.nlm.nih.gov/gtr/all/tests/?term=SNIP1) · [DDC Clinic Laboratory — Symptomatic Epilepsy and Skull Dysplasia (SNIP1) Targeted Testing](https://www.ddccliniclab.org/test/detail/symptomatic-epilepsy-and-skull-dysplasia-snip1-targeted-testing) · [QuickGO](https://www.ebi.ac.uk/QuickGO/) · [ClinicalTrials.gov API v2](https://clinicaltrials.gov/api/v2/studies?query.term=SNIP1)