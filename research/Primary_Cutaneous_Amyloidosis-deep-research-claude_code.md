---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T01:40:07.041889'
end_time: '2026-08-01T01:52:41.395332'
duration_seconds: 754.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Cutaneous Amyloidosis
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
  web_search_requests: 18
  num_turns: 54
  total_cost_usd: 3.9914067499999994
  session_id: 2a4934e9-35a5-4360-b8f8-622725a21479
  stop_reason: end_turn
citation_count: 50
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Cutaneous Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Primary Cutaneous Amyloidosis** covering all of the
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

# Primary Cutaneous Amyloidosis — Comprehensive Disease Research Report

**Prepared:** 2026-08-01 · **Target entity:** Primary (localized) cutaneous amyloidosis (PLCA/PCA) · **MONDO:0015301**

**Evidence provenance note.** Citations marked **[cached]** have been verified against abstracts already fetched into `references_cache/` in this worktree — the quoted snippets below are exact substrings of those cached abstracts and are safe to use directly in evidence items. Citations marked **[lead]** were surfaced by literature/database search in this session but have **not** yet been fetched via `just fetch-reference`; per the dismech DR SOP, treat them as leads and verify PMID + snippet + ontology terms before committing them to YAML.

---

## 1. Disease Information

### Overview

Primary localized cutaneous amyloidosis (PLCA, also PCA) is a group of chronic, skin-limited disorders defined by extracellular deposition of amyloid in the papillary dermis **without visceral organ involvement**. In the two dominant keratinocyte-derived forms (lichen and macular amyloidosis) the fibril precursor is **degenerate epidermal keratin**, not a plasma-cell or hepatic-precursor protein — which mechanistically separates PLCA from AL/ATTR/AA systemic amyloidosis. A third clinical form, **nodular amyloidosis**, is mechanistically distinct: it is a localized cutaneous plasma-cell dyscrasia depositing **AL (immunoglobulin light chain)** amyloid, and it carries a real (if modest) risk of representing or evolving into systemic disease.

The canonical mechanistic quote for the keratinocyte-origin claim:

> "Amyloids in lichenoid and macular amyloidoses, and in basal cell epithelioma had an identical antigenicity with epidermal keratin, whereas amyloids in nodular amyloidosis and systemic amyloidosis did not have this identity." — Kobayashi & Hashimoto, *J Invest Dermatol* 1983, **PMID:6184423** [cached]

> "It was concluded that at least some of the amyloid substance in organ-limited cutaneous amyloidosis is derived from degenerated epidermal keratinocytes through filamentous degeneration or apoptosis." — **PMID:6184423** [cached]

Modern proteomic subtyping has refined the precursor identity to specific basal keratins:

> Title: "LC-MS/MS and immuno-electron subtyping combined with genetics show that OSMR mutations cause amyloid deposition of keratins 5/14 in familial primary localized cutaneous amyloidosis" — Bourguiba et al., *JEADV* 2022, **PMID:34459039** [cached] *(title-level evidence only; this is a correspondence piece with no structured abstract in the cache — quote the title, not a fabricated body sentence)*

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0015301` | primary cutaneous amyloidosis (verified via OAK; `is_a` MONDO:0019065 amyloidosis, MONDO:0021154 dermis disorder) |
| MONDO (familial) | `MONDO:0007101` | familial primary localized cutaneous amyloidosis |
| MONDO (nodular) | `MONDO:0015302` | nodular cutaneous amyloidosis |
| **OMIM** | **105250** (PLCA1, *OSMR*, AD, 5p13) | [lead] |
| OMIM | **613955** (PLCA2, *IL31RA*, AD, 5q11) | [lead] |
| OMIM | **617920** (PLCA3 / amyloidosis cutis dyschromica, *GPNMB*, AR, 7p15) | [lead] |
| Orphanet | `ORPHA:137807` (primary cutaneous amyloidosis); `ORPHA:137810` (nodular cutaneous amyloidosis) | xref confirmed in MONDO record |
| ICD-10 | **E85.4** — Organ-limited amyloidosis | [lead] |
| ICD-11 | 5D00.2 / EE60-adjacent organ-limited amyloidosis branch — **not confirmed**; verify in the ICD-11 browser before curating | ⚠️ |
| MeSH | `MESH:C562642` | via MONDO xref |
| Others | DOID:0050639 · GARD:0000132 · MedGen:120635 · MedDRA:10011659 · NCIT:C199391 · SNOMED CT:282834007 · UMLS:C0268397 | via MONDO xrefs |

### Synonyms (from the MONDO record, OAK-verified)

primary localised cutaneous amyloidosis; **PLCA** (narrow); familial primary localized cutaneous amyloidosis (narrow); amyloidosis IX; amyloidosis familial cutaneous lichen; lichen amyloidosis familial. Clinically also: lichen amyloidosus, papular amyloidosis, lichenoid amyloidosis, macular amyloidosis, biphasic amyloidosis, frictional amyloidosis, amyloidosis cutis dyschromica (ACD).

### Information provenance

Predominantly **disease-level aggregated** (OMIM/Orphanet/GeneReviews-style, review syntheses) plus **individual-patient case series and pedigree studies** (Taiwanese, Chinese, Brazilian, Pakistani, Central European cohorts). No large EHR-derived phenotype work identified; there is no registry. This is a good candidate for a `definitions[]` block with `derivation_basis: ESTABLISHED_CRITERIA` but `validation_status: PROPOSED` — no validated computable phenotype exists.

---

## 2. Etiology

### Causal factors — a genuinely multifactorial disease

PLCA is best modeled as a **complex/multifactorial** disorder with a well-characterized Mendelian subset. Three converging causal streams:

1. **Germline cytokine-receptor lesions (Mendelian arm).** Autosomal-dominant missense variants in *OSMR* and *IL31RA*; autosomal-recessive loss-of-function in *GPNMB* (ACD).
2. **Chronic mechanical/frictional epidermal injury (environmental arm).** Long-term rubbing with nylon towels/brushes, and chronic scratching, are established triggers, especially for macular amyloidosis in Asian and Middle Eastern populations [lead: PMID:19207438, PMID:9330050, PMID:3391726].
3. **Chronic pruritus of any cause feeding a scratch–damage–deposition loop.** Atopic dermatitis is the most frequent comorbid itch driver.

The full-text of the Taiwanese genetics paper states the multifactorial framing explicitly:

> "The precise pathogenesis of PCA is unclear, but it is considered to be multifactorial, involving both genetic and environmental contributions. Earlier reports have implicated frictional epidermal damage, apoptosis, viral infection, and other triggers in the disease etiology." — Lin et al., *Eur J Hum Genet* 2010, **PMID:19690585** [cached, full text]

### Genetic risk factors

**Causal / high-effect:**
- ***OSMR*** (HGNC:8507, `hgnc:8507` — verify with OAK before curating), 5p13.1 — heterozygous missense in the extracellular fibronectin type III-like (FNIII) domains. **AD.**
- ***IL31RA*** (5q11.2) — heterozygous missense, also FNIII-domain. **AD.**
- ***GPNMB*** (7p15) — biallelic truncating (and some missense) alleles → amyloidosis cutis dyschromica. **AR.**

**Susceptibility / modifier:**
- ***RET*** codon **634** (and rarely other codons) — cutaneous lichen amyloidosis is a recognized MEN2A variant phenotype. ~⅓ of C634 carriers develop CLA (range 9–50%) [lead: PMID:12864791; PMC11587112].
- **Haplotype background:** the Taiwanese p.P694L allele sits on a shared ancestral haplotype (`25-GAAAA`) in 5/6 families plus 2 sporadic cases — a **founder effect**; the same amino-acid change in a Chilean family arose on a different haplotype, i.e. p.P694L is *both* ancestral and recurrent, favored by a CpG mutational hotspot (CCG>CTG) [cached, PMID:19690585 full text].
- **Locus heterogeneity:** 8/29 Taiwanese pedigrees mapped to chr5 without an *OSMR* coding lesion; two pedigrees gave negative LOD scores at chr5 entirely — so **additional PLCA loci remain undiscovered**.

**Ancestry:** Southern Chinese/Taiwanese, Southeast Asian, South American, Middle Eastern, and South Asian populations are over-represented.

### Environmental risk factors

| Factor | Evidence | Note |
|---|---|---|
| Chronic friction (nylon towel/brush, loofah, back scratchers) | [lead] PMID:19207438, PMID:9330050, PMID:3391726 | Strongest non-genetic factor; "frictional amyloidosis" is a named entity |
| Chronic scratching from any pruritic dermatosis | [cached] PMID:19690585 full text: *"Severe itching is a hallmark of PCA and prolonged scratching might induce apoptosis and lead to PCA."* | Self-amplifying loop |
| Atopic dermatitis / atopic diathesis | [cached] PMID:39975679 case series (most reported dupilumab-treated PCA patients were atopic) | 12.2% atopy in Central European cohort [lead: PMID:38137741] |
| UV radiation | Cited as a keratinocyte-apoptosis trigger in review literature | Weak/indirect |
| EBV and other viral infection | Historically proposed [cached: PMID:19690585 cites "viral infection"] | Not replicated; low confidence |
| Sjögren syndrome (nodular form) | [cached] PMID:18576343 | See §5 |

### Protective factors

**No validated genetic protective variants and no established dietary/lifestyle protective factors are reported.** The only actionable "protective" intervention is **cessation of frictional trauma** (abandoning nylon towel/brush use) and effective itch control to break the scratch–deposition cycle. This should be recorded as expert-consensus-level, not evidence-graded.

### Gene–environment interaction

The most defensible G×E model: a hypomorphic *OSMR*/*IL31RA* allele lowers the threshold at which ordinary frictional/pruritic epidermal stress produces amyloidogenic keratinocyte degeneration. Supporting observations:
- *OSMR* missense variants appear in **34.38% of sporadic** PLCA as well as **63.89% of familial** PLCA, i.e. the same alleles behave as susceptibility factors outside pedigrees [cached, PMID:30734345].
- **Allele dosage shifts onset:** *"Age of onset of PLCA with OSMR homozygous mutation (median age 20 years) was earlier than that of PLCA with OSMR heterozygous mutation (median age 32 years; P < 0.01) or PLCA with wildtype genotype (median age 32 years; P < 0.01)."* [cached, PMID:30734345]
- **Genotype tracks severity:** in a Taiwanese four-affected-member family, *"those who have p.P694L mutation showed greater severity of PCA… larger areas of skin lesion… and a higher density of amyloid papules, as compared with those without the mutation."* [cached, PMID:19690585 full text]

---

## 3. Phenotypes

### Core phenotype set with HPO terms (all OAK-verified against `sqlite:obo:hp`)

| Phenotype | HPO term | Category | Frequency | Onset | Course |
|---|---|---|---|---|---|
| **Pruritus** (often severe, the dominant symptom) | `HP:0000989` Pruritus | Symptom | Very frequent — near-universal in lichen form | Adult, with disease | Chronic, fluctuating |
| **Cutaneous amyloidosis** (umbrella) | `HP:0012309` Cutaneous amyloidosis | Clinical sign / path | Obligate | — | Progressive |
| **Cutaneous lichen amyloidosis** | `HP:0032346` | Subtype sign | ~44% of a Central European cohort | 3rd–5th decade | Progressive |
| **Cutaneous macular amyloidosis** | `HP:0032347` | Subtype sign | ~54% of same cohort | 5th decade | Progressive |
| **Cutaneous nodular amyloidosis** | `HP:0032348` | Subtype sign | Rare (0/41 in Central Europe) | Older adult | Slowly progressive |
| **Hyperpigmented papules** | `HP:0025473` Hyperpigmented papule | Physical | Frequent (lichen form) | Adult | Progressive |
| **Hyperpigmentation of the skin** | `HP:0000953` | Physical | Frequent | Adult | Progressive |
| **Reticulated / rippled skin pigmentation** | `HP:0007427` Reticulated skin pigmentation | Physical | Frequent (macular form) | Adult | Stable–progressive |
| **Hyperkeratosis** | `HP:0000962` | Histologic/physical | Frequent | Adult | Progressive |
| **Lichenification** | `HP:0100725` | Physical | Occasional (scratch-related) | Adult | Chronic |
| **Hypopigmented skin patches** (ACD only) | `HP:0001053` | Physical | Obligate in ACD | Childhood/adolescence | Progressive |
| **Generalized hyperpigmentation** (ACD) | `HP:0007440` | Physical | Obligate in ACD | Childhood | Progressive |

**Cellular/laboratory-level phenotypes** (suitable for `category: Cellular`):
- Reduced intraepidermal nerve fiber (IENF) density — small-fiber neuropathy
- Elevated warm detection threshold on quantitative sensory testing
- Increased epidermal OSMRβ and IL-31RA immunostaining
- Increased basal keratinocyte Ki67 positivity; increased FLG/LOR expression

### Phenotype characteristics

**Age of onset.** Adult-onset is the rule. Median 32 years in *OSMR*-heterozygous and wild-type Chinese patients, 20 years in *OSMR*-homozygotes [cached, PMID:30734345]. Central European mean age at diagnosis 54.6 ± 15.2 years (range 27–87); mean onset MA 53 ± 16.1, LA 46.7 ± 18.2 [lead, PMID:38137741]. Chinese HRQoL cohort: mean age 43.7 (18–91), mean onset 36.5 years [lead, PLOS One 2015, doi:10.1371/journal.pone.0120623]. **ACD is earlier** — childhood to adolescence.

**Severity.** Highly variable; genotype-dependent (see above). Pruritus is the severity driver, not lesion extent.

**Progression.** Chronic and slowly progressive; **essentially never spontaneously remitting**. Lesions persist for decades (reported disease durations 3–30 years in the dupilumab series [cached, PMID:39975679]).

**Frequency among affected individuals.** Pruritus dominates: in the dupilumab series both index patients reported Pruritus NRS 10/10 [cached, PMID:39975679]. Caution: most published frequency statements are qualitative — per `docs/frequency-evidence-guidelines.md`, **omit `frequency:` rather than manufacture a band** for most of these.

### Quality-of-life impact

The best single QoL source is a Chinese cross-sectional study of 104 PCA patients vs 101 controls [lead, PLOS One 2015]:
- Mean **DLQI 9.05 ± 3.88** — moderate impairment
- Highest subdomain: symptoms/feelings (2.29 ± 1.05); lowest: work/school (0.98 ± 0.73)
- *"Younger age, female gender, more pruritus and distribution pattern were independent predictor correlates of the high DLQI scores."*
- Itch severity showed the strongest association with DLQI

Corroborating per-patient data [cached, PMID:39975679]: baseline DLQI 16 and 24 in the two index cases, falling to 1 and 0 on dupilumab. Suggested instruments for a dismech `definitions`/outcome block: **DLQI**, **Peak Pruritus NRS (PP-NRS)**, **IGA**, and the modified EASI (m-EASI) used in that series.

---

## 4. Genetic / Molecular Information

### Causal genes

| Gene | HGNC | Locus | OMIM phenotype | Inheritance | Mechanism |
|---|---|---|---|---|---|
| ***OSMR*** (oncostatin M receptor β) | HGNC:8507 † | 5p13.1 | PLCA1 #105250 | AD (rare homozygotes) | Partial **loss of function**; impaired receptor dimerization/signaling |
| ***IL31RA*** (IL-31 receptor A) | HGNC:18969 † | 5q11.2 | PLCA2 #613955 | AD | Partial LoF, same FNIII-domain logic |
| ***GPNMB*** (glycoprotein NMB) | HGNC:4462 † | 7p15 | PLCA3/ACD #617920 | **AR** | Truncating/destabilizing **complete LoF** |
| ***RET*** (modifier/syndromic) | HGNC:9967 † | 10q11.21 | MEN2A #171400 with CLA | AD | GoF proto-oncogene; CLA is a variant phenotype |

† HGNC IDs are from memory of standard mappings — **verify each with `uv run runoak -i sqlite:obo:hgnc info hgnc:XXXX` before curating**, and use the repo's lowercase `hgnc:` prefix.

### Pathogenic variants — *OSMR*

All reported PLCA1 alleles are **missense substitutions in the extracellular fibronectin type III-like (FNIII) repeats**:

> "The pathogenic amino acid substitutions are located within the extracellular fibronectin type III-like (FNIII) domains, regions critical for receptor dimerization and function." — **PMID:18179886** [cached]

| Variant | cDNA | Population / families | Source |
|---|---|---|---|
| p.G618A | c.1853G>C | UK + South African white families | PMID:18179886 [cached] |
| p.I691T | c.2072T>C | Brazilian family | PMID:18179886 [cached] |
| p.D647V | c.1940A>T | 1 Taiwanese pedigree (exon 14) | PMID:19690585 [cached] |
| **p.P694L** | c.2081C>T | **6 Taiwanese pedigrees + 2 sporadic + 1 Chilean family** — most frequent allele worldwide; CpG hotspot | PMID:19690585 [cached] |
| p.K697T | c.2090A>C | 3 Taiwanese pedigrees (exon 15) | PMID:19690585 [cached] |
| p.G513D | c.1538G>A | Most frequent in mainland Chinese PLCA alongside p.P694L | PMID:33502684 [cached, full text] |

> "we investigated 29 Taiwanese pedigrees with PCA and found that 10 had heterozygous missense mutations in OSMR: p.D647V (one family), p.P694L (six families), and p.K697T (three families)." — **PMID:19690585** [cached]

**Population frequency.** *"None of the 142 control subjects from Taiwan (or over 250 control chromosomes from other populations) showed presence of p.P694L or the other missense mutations."* [cached, PMID:19690585 full text]. p.P694L = **rs387906822**, ClinVar VCV000030221 / RCV000023144, classified in association with "Amyloidosis, primary localized cutaneous, 1" [lead — pull the current ClinVar review status and gnomAD AF directly before asserting a classification].

**Somatic vs germline.** All PLCA1/2/3 variants are **germline**. No somatic driver is described. The *nodular* form involves a clonal **somatic** plasma-cell population producing light chain — a different molecular category entirely.

**Functional consequence — partial loss of function, not dominant negative.** This is a nuance worth curating precisely:
> "p.P694L mutant failed to activate STAT5 and STAT3, and… p.G513D mutant failed to activate STAT5… **No dominant negative effect was observed**, as OSM can activate either STAT5 or STAT3 phosphorylation in both WT/p.G513D and WT/p.P694L co-infected HaCaT cells." — **PMID:33502684** [cached, full text]

Neither variant mislocalizes the receptor; the defect is signaling-competence, and the paper labels them explicitly *"partial loss-of-function mutants."*

### Pathogenic variants — *IL31RA*

- **p.S521F** (c.1562C>T, NM_139017), exon 12 — one Taiwanese FPCA family; absent from 142 controls; codon conserved across mammals; *"also sited within a fibronectin type III-like repeat domain as observed in the OSMR mutations."* [cached, PMID:19690585]

### Pathogenic variants — *GPNMB* (amyloidosis cutis dyschromica)

> "the compound heterozygosity or homozygosity of GPNMB truncating alleles is the cause of autosomal-recessive ACD. Six nonsense or frameshift mutations were identified in nine individuals diagnosed with ACD." — Yang et al., *AJHG* 2018, **PMID:29336782** [cached]

Missense alleles in consanguineous Pakistani families extend the spectrum:
> "We found a novel homozygous mutation, p.Gly363Val (c.1088 G>T), in GPNMB in all affected cases. In a replication study, another homozygous missense mutation in GPNMB, pIle174Met (c.522 C>G), was carried by the affected son. The two mutations were not observed in our in-house data set comprising 217 healthy Pakistani individuals or in The Genome Aggregation Database." — **PMID:33687658** [cached]

Structural modeling (COMPUTATIONAL evidence): *"p.Gly363Val enhanced its stability, whereas p.Ile174Met caused instability."* Additional GPNMB alleles reported in Chinese pedigrees [lead: PMID:31260093]; a semidominant inheritance mode has been proposed [lead].

### Modifier genes

*RET* C634 is the best-established syndromic modifier. Within-family locus heterogeneity is documented (one Taiwanese family had two independent genetic causes segregating simultaneously — mother/son with p.P694L, father/other son without any *OSMR* lesion) [cached, PMID:19690585].

### Epigenetics and chromosomal abnormalities

**No disease-specific DNA methylation, histone-modification, or chromosomal abnormality data identified.** Do not curate speculative epigenetic content. Chromosomal microarray and karyotyping have **no role** in PLCA.

---

## 5. Environmental Information

- **Mechanical/frictional:** nylon towel, nylon brush, loofah, backscratcher; occupational/cultural bathing practices. Named entities: "nylon brush macular amyloidosis," "frictional amyloidosis" [lead: PMID:9330050, PMID:3391726, PMID:19207438]. Prolonged friction produces *hyperkeratosis, keratinocyte damage (filamentous degeneration), and melanocyte stimulation*.
- **Iatrogenic:** long-term subcutaneous injection sites (e.g. insulin) have been implicated in localized amyloid deposition [lead, PMC11587112].
- **Lifestyle:** no smoking/alcohol/diet association established.
- **Infectious agents:** EBV was historically proposed as a trigger [cached, PMID:19690585 citing "viral infection"]. **Not substantiated** — do not curate as a mechanism node without a primary source.
- **Comorbid/associated conditions** (mostly case-report level, low confidence — curate as `association_signals` or `comorbidities`, not as pathophysiology):
  - **Sjögren syndrome ↔ nodular cutaneous amyloidosis** — the strongest of these. Eight patients across three amyloidosis centers; *"All of the patients were women in whom SS had been diagnosed at a median age of 47 years… The presence of the immunoglobulin light chain type of amyloid (AL amyloid) was confirmed in 4 patients. In 3 of these 4 patients as well as 2 other patients, a light chain-restricted plasma cell population was observed near the amyloid deposits."* **PMID:18576343** [cached]
  - Systemic sclerosis / limited cutaneous SSc, CREST, SLE, RA, primary biliary cholangitis, autoimmune thyroiditis, IgA nephropathy, sarcoidosis, ankylosing spondylitis — all case-report-level [lead].
  - **Central European cohort comorbidity profile** [lead, PMID:38137741]: endocrine/metabolic 41.5% (dyslipidemia 22%, thyroid disease 12.2%, diabetes 7.3%), cardiovascular 34.1% (hypertension 29.3%), atopy 12.2%, malignancy 12.2%. These are plausibly age-confounded background rates — **flag as uncontrolled**.

---

## 6. Mechanism / Pathophysiology

### Proposed causal chain (curation-ready pathograph)

```
[TRIGGER, MOLECULAR]
  OSMR / IL31RA FNIII-domain missense  ──┐
  (impaired receptor dimerization)       │
  GPNMB loss of function ────────────────┤   +  Chronic frictional / scratch-induced
                                          │      epidermal injury (environmental)
                                          ▼
[MOLECULAR] Loss of OSM/OSMRβ–gp130 signal transduction
            → failure to phosphorylate STAT5 (and STAT3), ERK1/2, AKT
                                          ▼
[MOLECULAR] Inactivation of the STAT5 → KLF7 axis
            (KLF7 is a direct STAT5 target gene)
                                          ▼
[CELLULAR]  De-repressed basal keratinocyte differentiation (↑KRT1, KRT10, FLG, LOR)
            + AHNAK upregulation → keratinocyte hyperproliferation (↑Ki67, ↑EdU)
            + Bcl-xL suppression → increased keratinocyte apoptosis
                                          ▼
[CELLULAR]  Filamentous degeneration / apoptosis of basal keratinocytes;
            keratin 5/14 tonofilament release into papillary dermis
                                          ▼
[MOLECULAR] Keratin misfolding, β-sheet conversion, fibrillogenesis
            (± galectin-7, actin, apolipoprotein E, serum amyloid P as co-deposits)
                                          ▼
[TISSUE]    Amyloid deposition in dermal papillae
            + impaired macrophage clearance (IL31RA→MCP-1 axis defect)
                                          ▼
[TISSUE]    Small-fibre neuropathy: ↓intraepidermal nerve fibres,
            ↑epidermal OSMRβ/IL-31RA expression → nerve-fibre hypersensitivity
                                          ▼
[ORGANISM]  Chronic intractable pruritus → scratching → further keratinocyte
            damage  ──────► FEEDS BACK to the injury node (vicious cycle)
```

### Molecular pathways

**IL-6-family cytokine receptor signaling** is the core pathway. OSMRβ is a shared subunit of *two* receptors: the **type II OSM receptor** (OSMRβ + gp130) and the **IL-31 receptor** (OSMRβ + IL-31RA). This explains why lesions in *both* genes produce the same phenotype.

> "OSMRbeta is a component of the oncostatin M (OSM) type II receptor and the interleukin (IL)-31 receptor, and cultured FPLCA keratinocytes showed reduced activation of Jak/STAT, MAPK, and PI3K/Akt pathways after OSM or IL-31 cytokine stimulation." — **PMID:18179886** [cached]

Suggested GO terms (OAK-verified):
- `GO:0038165` oncostatin-M-mediated signaling pathway
- `GO:0140370` type II oncostatin-M receptor complex (cellular component)
- `GO:0004924` oncostatin-M receptor activity (molecular function)
- `GO:0007259` cell surface receptor signaling pathway via JAK-STAT
- `GO:1990000` amyloid fibril formation
- `GO:1905908` positive regulation of amyloid fibril formation
- `GO:0030216` keratinocyte differentiation; `GO:0045618` positive regulation of keratinocyte differentiation
- `GO:0010838` positive regulation of keratinocyte proliferation
- `GO:0006915` apoptotic process
- `GO:0008544` epidermis development
- `GO:0072635` interleukin-31 production

### The STAT5/KLF7 axis (the strongest mechanistic result available)

Liu et al. established the directionality: **OSM is a negative regulator of keratinocyte differentiation**, acting through STAT5 → KLF7. Losing OSMRβ signaling therefore *de-represses* differentiation.

> "In summary, we identified OSM as a negative regulator of epidermal keratinocyte differentiation that acts via STAT5/KLF7 signaling in vivo and in vitro. Dysregulation of the OSM/OSMRβ/STAT5/KLF7 axis by OSMR mutation could lead to PLCA." — **PMID:33502684** [cached, full text]

Supporting chain of experiments in that paper (all IN_VITRO / MODEL_ORGANISM):
- GO analysis of PLCA-vs-control RNA profiles: dysregulated genes were dominated by **keratinocyte differentiation** processes
- PLCA lesional epidermis: ↑FLG, ↑LOR, ↑Ki67 in basal keratinocytes
- OSM stimulation of HaCaT/primary keratinocytes and 3D skin models **decreases** KRT1/KRT10/FLG/LOR; *OSMR* knockout rescues this
- STAT5 inhibitor "almost completely" rescues; STAT3 inhibitor partial; ERK1/2 and AKT inhibitors no effect → **STAT5 is the operative arm**
- ChIP-qPCR + luciferase reporter: STAT5 binds the *KLF7* locus on OSM stimulation; three STAT5 sites in the *KLF7* promoter all contribute
- *KLF7* overexpression ↓ differentiation markers; *KLF7* knockout blocks OSM-induced differentiation change
- RNA-seq accessions: **GEO: GSE150884, GSE150994, GSE151174** — directly usable as a dismech `datasets[]` entry

### AHNAK — the proliferation arm

> "we found that AHNAK peptide fragments were enriched in the lesions of PLCA patients, as detected by laser capture microdissection and mass spectrometry analysis… pre-treatment with OSM can inhibit AHNAK expression in HaCaT cells, NHEKs, and 3D human skin models, but OSMR knockout or OSMR mutations abolished this down-regulation trend… the knockdown of AHNAK could induce G1 phase cell cycle arrest and inhibit keratinocyte proliferation." — Liu et al., *J Dermatol Sci* 2023, **PMID:37100691** [cached]

> "these data indicated that the elevated expression of AHNAK by OSMR mutations led to hyperproliferation and overdifferentiation of keratinocytes" — **PMID:37100691** [cached]

### Integrated 2026 synthesis

The most current mechanistic review ties the arms together and adds the **clearance-failure** arm:

> "Oncostatin M (OSM) mediates keratinocyte proliferation through the STAT5-KLF7 axis upon OSMRβ engagement. Pathogenic variants in OSMR disrupt receptor dimerization, thereby suppressing signal transduction. These alterations together with cytokine dysregulation concomitantly elevate the expression of AHNAK and suppress that of Bcl-xL, which accelerate keratinocyte differentiation and apoptosis respectively, leading to the thickening of the stratum corneum and amyloid fibril deposition. Furthermore, dysregulated expression of chemokine monocyte chemoattractant protein-1 (MCP-1) by pathogenic variant in IL-31RA reduces monocyte-mediated clearance of amyloid fibrils, thereby promoting their pathological retention." — Teng et al., *Int J Dermatol* 2026, **PMID:42029085** [cached]

This gives a clean two-arm model: **overproduction** (keratinocyte apoptosis/differentiation) + **underclearance** (monocyte/macrophage failure).

### Pruritus mechanism — small-fibre neuropathy

> "WDT was significantly higher in patients at all sites and correlated with itch scores (r = 0·59; P < 0·01). Patient biopsies revealed lower IENF counts (P < 0·01 using protein gene product 9.5, β3-tubulin and Neurofilament 200 stains) and increased epidermal expression of OSMRβ (P < 0·01) and IL-31RA (P < 0·01)." — Tey et al., *Br J Dermatol* 2016, **PMID:26748444** [cached]

> "SFN is present in PLCA. Pruritus in PLCA is likely associated with hypersensitivity of cutaneous nerve fibres, which may be related to an increased expression of epidermal IL-31 receptors. Targeting IL-31 receptors is therefore a potential therapeutic approach." — **PMID:26748444** [cached]

Notably, cutaneous IL-31, NGF, and TrkA were **not** significantly increased, and serum IL-31 was **not** elevated — the abnormality is **receptor-side**, not ligand-side. This is an important negative result to curate faithfully.

**⚠️ Open controversy worth a `discussions:` KNOWLEDGE_GAP entry.** The 2026 review flags a direct conflict in the literature:
> "The mechanisms of IL-31-mediated pruritus remain to be elucidated, given the conflicting observations that while some studies report wider cutaneous innervation in FPLCA patients, others demonstrate opposing results in general lichen amyloidosis patients." — **PMID:42029085** [cached]

### Protein dysfunction and amyloid composition

- **Precursor:** basal keratins **K5/K14** (immuno-EM + LC-MS/MS) [cached, PMID:34459039 title-level]
- **Antigenic identity with epidermal keratin**, with disulfide bonds preserved (lichen form) [cached, PMID:6184423]
- **Co-deposited components:** galectin-7, actin, apolipoprotein E, serum amyloid P component, ubiquitin [lead: PMID:23278892, PMID:25172508]
- **⚠️ Contested:** a proteomic study concluded that *"the main constituent of subepidermal localized cutaneous amyloidosis is not galectin-7"* [lead: PMID:32867548 / PMC7962860]. **Curate galectin-7 with an explicit `supports: PARTIAL` or a paired REFUTE evidence item — do not present it as settled.**
- **ACD:** deposits are **DNA/keratin-positive**, with intracytoplasmic fibrillary aggregates in scattered lesional keratinocytes [cached, PMID:29336782]
- **Nodular:** AL — monoclonal immunoglobulin light chain from local clonal plasma cells [cached, PMID:18576343; lead: Medscape/JAMA Dermatol series]

### Cellular processes and cell types (CL terms, OAK-verified)

| Cell type | CL term | Role |
|---|---|---|
| Keratinocyte | `CL:0000312` | Primary amyloid precursor source |
| Basal cell of epidermis | `CL:0002187` | Site of hyperproliferation/de-repressed differentiation |
| Epidermal keratinocyte | `CL:4052061` | General epidermal compartment |
| Melanocyte | `CL:0000148` | Pigment incontinence; **lost** in ACD depigmented macules |
| Epithelial melanocyte | `CL:0002484` | Epidermal melanocyte specifically |
| Macrophage | `CL:0000235` (verify) | Melanophage pigment uptake; failed amyloid clearance |
| Fibroblast of papillary layer of dermis | `CL:1000302` | Deposition microenvironment |
| Plasma cell | `CL:0000786` (verify) | **Nodular form only** — clonal AL source |

### Immune involvement

PLCA is *not* classically an inflammatory dermatosis, and the older literature says so explicitly [cached, PMID:19690585 full text: *"Although PCA itself is not considered as an inflammatory skin disease…"*]. But the therapeutic response to dupilumab and nemolizumab, plus this observation, argues for a **type-2 inflammatory contribution** in at least a subset:
> "Studies have shown that serum and cutaneous levels of type 2 cytokines (IL-4, IL-13, IL-31) and their receptors were elevated in patients with PCA, and their expression were decreased when symptoms were alleviated, indicating that type 2 inflammation may involve in LA pathogenesis" — **PMID:39975679** [cached, full text]

GPNMB itself is a **negative regulator of inflammation** and a lysosomal-dysfunction/autophagy marker in macrophages, so ACD plausibly involves an inflammatory/clearance dimension [cached, PMID:29336782].

### Metabolic changes / biochemical abnormalities

**None identified.** No enzyme deficiency, no ion channel defect, no metabolomic or lipidomic signature reported. Explicitly record as "not applicable / not reported" rather than leaving the reader to infer.

### Molecular profiling summary

| Modality | Available? | Detail |
|---|---|---|
| Transcriptomics | ✅ | RNA-seq of PLCA lesional vs control skin; *Osmr*−/− mouse skin; OSM-treated HaCaT. **GEO: GSE150884, GSE150994, GSE151174** [cached, PMID:33502684] |
| Proteomics | ✅ | Laser-capture microdissection + MS identifying AHNAK enrichment [cached, PMID:37100691]; LC-MS/MS amyloid subtyping to K5/K14 [cached, PMID:34459039]; contested galectin-7 proteomics [lead] |
| Metabolomics / lipidomics | ❌ | None found |
| Epigenomics | ❌ | None found |
| Single-cell / spatial | ❌ | **None found — a genuine and citable knowledge gap.** Strong candidate for a `discussions: KNOWLEDGE_GAP` entry with a proposed scRNA-seq/spatial experiment on lesional vs perilesional skin |
| Functional genomics (CRISPR/RNAi) | ✅ (targeted, not screen-scale) | CRISPR/Cas9 knockout of *OSMR* and *KLF7* in HaCaT; siRNA *KLF7*; AHNAK knockdown [cached, PMID:33502684, PMID:37100691] |

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** skin (`UBERON:0002097` skin of body — verify), exclusively
- **Secondary organ involvement:** **none by definition.** Systemic/visceral deposition excludes the diagnosis. The one caveat: nodular PLCA may be the presenting lesion of, or progress to, systemic AL amyloidosis (heart, kidney, liver, GI, nerve).
- **Body system:** integumentary; peripheral nervous system secondarily (small-fibre)
- **Syndromic extension:** in MEN2A-associated CLA, thyroid (medullary carcinoma), adrenal (pheochromocytoma), parathyroid

### Tissue and cell level
- **Papillary dermis** — `UBERON:0001992` papillary layer of dermis (OAK-verified) — the amyloid deposition site
- **Epidermis** — hyperkeratosis, acanthosis, basal-layer degeneration
- **Dermoepidermal junction** — pigment incontinence
- Cell populations: see CL table in §6

### Subcellular level (GO Cellular Component)
- **Keratin filament / intermediate filament cytoskeleton** — the source structure; "filamentous degeneration" of tonofilaments
- **Extracellular space** / extracellular matrix — deposition compartment
- **Type II oncostatin-M receptor complex** `GO:0140370`; plasma membrane — the receptor lesion site
- **Lysosome / autophagosome** — relevant in the GPNMB/ACD arm
- **Melanosome** — GPNMB's canonical role; relevant to ACD dyschromia

### Localization and laterality

**Bilateral and typically symmetric.**
- **Lichen amyloidosis:** shins/pretibial (classic), calves, ankles, thighs, extensor forearms, back
- **Macular amyloidosis:** **interscapular upper back** (classic, rippled/reticulate), also arms, chest
- **MEN2A-associated CLA:** characteristically **interscapular**, overlapping the notalgia paresthetica dermatome (T2–T6)
- **Nodular:** acral, face, trunk, genitalia — often solitary or few
- **ACD:** generalized trunk and limbs
- Per the Chinese cohort: *"PLCA lesions are typically localized to the shins, forearm and back."* **PMID:30734345** [cached]
- **Atypical variants** (geographic and morphologic) are extensively catalogued — auricular concha, poikiloderma-like, vitiliginous, bullous, dyschromic [lead: PMID:34286474 Hamie 2021]

---

## 8. Temporal Development

**Onset.** Adult; insidious. Median 32 years (Chinese, wild-type/heterozygous), 20 years (*OSMR* homozygous) [cached, PMID:30734345]; mean 54.6 years at diagnosis in Central Europe [lead, PMID:38137741] — the diagnosis–onset gap suggests substantial diagnostic delay. **ACD onset is childhood/adolescence.** MEN2A-associated CLA: mean age at skin-lesion diagnosis 20 ± 13 years, preceding the endocrine components (mean 31 ± 17 years) [lead, PMC11587112] — clinically important, since CLA can be the earliest sign of MEN2A.

**Progression.** Slow, chronic, and essentially unremitting without treatment. No recognized staging system. Lichen and macular forms are *"one often overlapping process"* [cached, PMID:41528921], and biphasic amyloidosis represents patients manifesting both — so "progression" between subtypes is better modeled as phenotypic overlap than as staging.

**Course pattern.** Chronic-progressive with fluctuating pruritus intensity. Reported disease durations at presentation: 3–30 years [cached, PMID:39975679].

**Duration.** Lifelong.

**Remission.** **Spontaneous remission is not described.** Treatment-induced remission is achievable — complete lesion clearance occurred in 4/14 dupilumab-treated patients, with most others achieving significant improvement [cached, PMID:39975679]. Pruritus responds much faster than lesions (1–12 weeks vs 4–28 weeks).

**Critical periods / windows of intervention.** Two actionable ones:
1. **Early interruption of the itch–scratch–friction loop** before dense amyloid accumulates — the only plausibly disease-modifying non-drug intervention.
2. **CLA as a sentinel for MEN2A** — recognizing interscapular CLA in childhood/young adulthood can trigger *RET* testing years before MTC becomes clinically apparent, which is a genuine mortality-relevant window [cached, PMID:42194535].

---

## 9. Inheritance and Population

### Epidemiology
- **Asian population estimated prevalence ≈ 0.98 per 10,000** [lead — Pigment International 2023 review; corresponds to `prevalence_class: BAND_1_5_PER_10000`, `rate_per_100000: 9.8`]. **Verify this figure against a citable primary source before curating.**
- Singapore (Middle Road Hospital) annual incidence stable at **0.4% of dermatology attendances**, 1984–1986 [lead: PMID:2224732 — this is a *clinic proportion*, not a population rate; do NOT convert it to `rate_per_100000`]
- **Rare in Central/Northern Europe** — a single Swiss/Central European tertiary center accumulated only 41 cases [lead, PMID:38137741]
- **~10% of cases are familial** [lead, review-level]; in South America, Ollague et al. reported **~⅓ of PCA cases have a positive family history** [cached, PMID:19690585 full text]
- No GBD, SEER, or national registry data exist for PLCA

### Inheritance (genetic subset)
- **PLCA1 (*OSMR*), PLCA2 (*IL31RA*): autosomal dominant** — HPO `HP:0000006`
- **PLCA3 / ACD (*GPNMB*): autosomal recessive** — HPO `HP:0000007`
- **Consanguinity** is a clear contributor to the ACD arm: both Pakistani ACD families were consanguineous [cached, PMID:33687658]
- **Homozygous *OSMR* genotypes exist** and produce earlier, more severe disease with a striking sex skew: *"The male/female ratio of patients carrying a homozygous OSMR mutation (0.29) was significantly lower than that of patients carrying a heterozygous OSMR mutation (1.08; P < 0.05) and of patients with wildtype OSMR (1.75; P < 0.01)."* [cached, PMID:30734345]
- **Multi-locus:** within-family locus heterogeneity documented, but this is *not* digenic inheritance — do not use `HP:0010984`. It is two independent monogenic causes co-segregating in one pedigree.

**Penetrance.** Incomplete and age-dependent; not formally quantified. **Expressivity is markedly variable** — even within a single family (severity tracked with p.P694L carriage) [cached, PMID:19690585].

**Anticipation.** Not described. **Germline mosaicism.** Not reported. **Carrier frequency.** Not established for any of the three genes.

**Founder effect.** Yes — Taiwanese p.P694L on the shared `25-GAAAA` haplotype in 5/6 families plus 2 sporadic cases; the Chilean p.P694L carriers had a *different* haplotype background, establishing p.P694L as both ancestral and recurrent (CpG hotspot) [cached, PMID:19690585].

### Population demographics
- **Ethnic/geographic:** highest in Southern Chinese, Taiwanese, Southeast Asian, and South American (Brazil, Chile) populations; also over-represented in Middle Eastern and South Asian populations. Explicitly reported prevalence gradient within Southeast Asia: more common in Chinese than in Malays or Indians [cached, PMID:19690585 full text].
- **Sex ratio:** **female predominance overall.** Central Europe M:F = 0.64:1 [lead, PMID:38137741]; Chinese HRQoL cohort 43M:61F (59% female) [lead]; the Sjögren-associated nodular cohort was 8/8 female [cached, PMID:18576343]. But the *genotyped* Chinese cohort shows the direction depends on *OSMR* genotype (see above) — worth curating that nuance rather than a flat ratio.
- **Age distribution:** peaks 3rd–6th decade; ACD is pediatric-onset.

---

## 10. Diagnostics

### Clinical tests

**Biopsy + histochemistry is the diagnostic cornerstone.** Diagnosis is clinicopathologic; there is no blood test.

- **Histopathology:** hyperkeratosis, irregular acanthosis, expansion of the dermal papillae by eosinophilic globular amyloid deposits, pigment incontinence with dermal melanophages, sparse perivascular infiltrate [lead: PMC11947714 case series]
- **Congo red + polarized light microscopy (CR-PLM)** — the reference standard, showing **apple-green birefringence**. In PCA, *"most of the apple-green birefringence patterns were a short, curved line or dot-like; a lump-like pattern was rare"* [lead: PMID:39663859]. Because deposits are small and subepidermal, birefringence can be subtle and false negatives are common.
- **Congo red UV-emitted fluorescence microscopy (CR-UFM)** — a 2025 advance reported as *superior to CR-PLM, CR staining, crystal violet, and H&E in diagnosing PCA* [lead: PMID:39663859]. Worth curating as an emerging diagnostic.
- Other stains: crystal violet, thioflavin T, pagoda red, Dylon
- **Immunohistochemistry:** anti-cytokeratin (CK5/6, K5/K14 positivity supports keratinocyte origin — used in both dupilumab index cases [cached, PMID:39975679]); anti-κ/λ light chain to identify AL in nodular lesions; serum amyloid P
- **LC-MS/MS proteomic amyloid subtyping** — definitive typing, distinguishing keratin-derived from AL [cached, PMID:34459039]
- **Electron microscopy / immuno-EM** — non-branching 6–10 nm fibrils; identifies intracytoplasmic fibrillary aggregates in ACD keratinocytes [cached, PMID:29336782]
- **Dermoscopy** (non-invasive adjunct): the characteristic macular-amyloidosis pattern is *"a central hub of either white or brown surrounded by various configurations of brownish pigmentation, including fine radiating streaks, dots, leaf-like projections, and bulbous projections"* [lead: Pudasaini 2024, *Skin Health Dis*]
- **Quantitative sensory testing + IENF density on PGP9.5** — research-grade, demonstrates the small-fibre neuropathy [cached, PMID:26748444]. Not routine clinical practice.

### Laboratory work-up to *exclude* systemic disease (mandatory in nodular form)
Serum and urine protein electrophoresis with immunofixation, serum free light chain ratio, CBC, creatinine/eGFR, LFTs, NT-proBNP and troponin, ECG/echocardiography, and consideration of bone marrow biopsy and fat pad aspirate. For nodular PLCA, **long-term follow-up is recommended even when the initial systemic screen is negative.**

### Genetic testing
- **Recommended approach:** targeted **single-gene** or small-panel sequencing of ***OSMR*** first in familial/early-onset/severe cases (highest yield: 63.89% in familial and 34.38% in sporadic Chinese PLCA [cached, PMID:30734345]), then ***IL31RA***, then ***GPNMB*** if the phenotype is dyschromic/recessive.
- **DNA mass spectrometry** genotyping of recurrent *OSMR* alleles has been used as a rapid screen in sporadic disease [cached, PMID:24237668 — title/metadata only; the cached record has **no abstract body**, so no snippet is quotable. Cite by title or find an alternative source.]
- **WES** — the discovery route for *GPNMB*/ACD [cached, PMID:33687658]; appropriate for atypical/unsolved cases. **WGS** offers no established incremental value.
- ***RET*** **testing** should be considered in any patient with interscapular or generalized CLA, particularly with any endocrine sign or family history — CLA can precede MTC by a decade [cached, PMID:42194535].
- **Not indicated:** chromosomal microarray, karyotype, FISH, mtDNA testing, repeat-expansion testing.

### Omics-based diagnostics
Only **tissue proteomics (LC-MS/MS amyloid typing)** has real diagnostic utility. RNA-seq, metabolomics, epigenomics, and liquid biopsy have no established diagnostic role in PLCA.

### Clinical criteria and differential diagnosis
No formal consensus diagnostic criteria (ACR/EULAR/society-level) exist for PLCA — worth noting explicitly.

> "Historically, cutaneous amyloidosis has been misdiagnosed" — Janodia & Schwartz, *Dermatology* 2026, **PMID:41528921** [cached]

Differential diagnosis by subtype:
- **Lichen amyloidosis vs.** lichen simplex chronicus, prurigo nodularis, hypertrophic lichen planus, lichen planus, pretibial myxedema, papular mucinosis, colloid milium, nodular scabies. *(Discriminator: Congo red-positive papillary dermal deposits; keratin-derived on IHC.)*
- **Macular amyloidosis vs.** post-inflammatory hyperpigmentation, notalgia paresthetica (which may coexist and be causal), frictional melanosis, ashy dermatosis/erythema dyschromicum perstans, confluent and reticulated papillomatosis, Dowling-Degos disease.
- **Nodular amyloidosis vs.** systemic AL amyloidosis with skin involvement (**must be excluded**), colloid milium, cutaneous lymphoma, granuloma annulare, sarcoidosis.
- **ACD vs.** dyschromatosis symmetrica/universalis hereditaria, xeroderma pigmentosum, Dowling-Degos, poikiloderma syndromes.

### Screening
- **No population screening; no newborn screening; no carrier screening program.** PLCA does not meet screening criteria (benign, adult-onset, no preventive intervention).
- **Cascade screening is warranted in one situation:** a proband with CLA and a pathogenic *RET* variant — first-degree relatives require *RET* cascade testing with prophylactic thyroidectomy decision-making per MEN2 guidelines. This is a case where a *skin* finding drives a *cancer* screening cascade.
- Relatives of *OSMR*/*IL31RA* probands: predictive testing is technically possible but of limited clinical utility (no preventive action available) — counseling-only.

---

## 11. Outcome / Prognosis

### Survival and mortality
**PLCA of keratinocyte origin does not affect survival.** There is no disease-specific mortality, no reduction in life expectancy, and no reported malignant transformation of the amyloid deposits themselves. Do not curate survival statistics for the keratinocyte-derived forms.

**Two exceptions where prognosis is not benign:**
1. **Nodular PLCA** — reported progression to systemic AL amyloidosis of approximately **7%**, with some series citing a **7–50%** range on long-term follow-up [lead — the wide range reflects small heterogeneous series; curate the 7% figure with an explicit uncertainty note, not the 50% ceiling]. Systemic AL amyloidosis carries substantial cardiac and renal mortality. Reassuringly, in the Sjögren-associated nodular series: *"Progression to systemic amyloidosis was not observed in any patient during a median followup of 3.5 years."* [cached, PMID:18576343]
2. **MEN2A-associated CLA** — prognosis is driven entirely by the endocrine components. *"In both subtypes, nearly 100% of patients eventually develop medullary thyroid cancer (MTC), and up to 50% develop pheochromocytomas."* [cached, PMID:30085596]

### Morbidity and function
The burden is **symptomatic and psychosocial**, not organ-failure-driven:
- Mean DLQI 9.05 ± 3.88 (moderate impairment) [lead, PLOS One 2015]
- Intractable pruritus, sleep disruption, excoriation, secondary infection risk
- Cosmetic disfigurement from persistent hyperpigmentation — significant in visible/exposed sites
- Small-fibre neuropathy with thermal sensory deficits [cached, PMID:26748444]

No disability registry data; ICF-coded outcomes not reported.

### Complications
Secondary bacterial infection from excoriation; post-inflammatory dyschromia; lichenification; scarring from aggressive procedural treatment; in ACD, permanent depigmentation from melanocyte loss (*"Depigmentation of the lesions was attributable to loss of melanocytes."* [cached, PMID:29336782]).

### Recovery potential
Lesions do **not** resolve spontaneously. Amyloid deposits are slow to clear even with successful therapy — hence the consistent observation that pruritus improves in 1–12 weeks while lesions take 4–28 weeks [cached, PMID:39975679]. Complete resolution occurs in a minority (4/14 with dupilumab).

### Prognostic factors
- ***OSMR* homozygosity** → earlier onset, greater severity [cached, PMID:30734345; PMID:19690585]
- **Pruritus severity** → the dominant determinant of QoL, more so than lesion extent [lead, PLOS One 2015]
- **Younger age, female sex** → worse DLQI [lead, PLOS One 2015]
- **Nodular subtype + monoclonal gammopathy** → the one prognostic red flag requiring systemic surveillance
- **No validated molecular prognostic biomarkers exist.**

---

## 12. Treatment

**Overarching reality check** — this should be stated plainly in any KB entry:

> "The current standard of care, high-potency corticosteroids, can provide symptomatic relief. Newer therapies may decrease amyloid deposition and progression of disease." — **PMID:41528921** [cached]

> "PCA lesions are currently considered difficult to treat, since no consistently effective therapy has been reported despite many therapeutic modalities have been tried in PCA treatment" — **PMID:39975679** [cached, full text]

**There is no FDA/EMA-approved therapy for PLCA. Everything below is off-label.**

### Conventional / first-line (symptomatic)

| Treatment | NCIT (OAK-verified where shown) | Modality | Evidence |
|---|---|---|---|
| High-potency topical corticosteroids ± occlusion | `NCIT:C15986` Pharmacotherapy + agent `NCIT:C2322` Corticosteroid | SMALL_MOLECULE | Standard of care; improved symptoms in **13/28 (46%)** treated patients [lead, PMID:38137741] |
| Topical calcineurin inhibitors (tacrolimus, pimecrolimus) | `NCIT:C15986` | SMALL_MOLECULE | Objective improvement in 2 MA + 1 LA case [lead, PMID:38137741] |
| Oral antihistamines | `NCIT:C15986` | SMALL_MOLECULE | Widely used; consistently reported as **ineffective** [cached, PMID:39975679] |
| Topical/oral retinoids (acitretin) | `NCIT:C15986` + `NCIT:C985` Acitretin | SMALL_MOLECULE | Case-level benefit [lead, PMID:27828646] |
| Vitamin D3 analogues (calcipotriol) | `NCIT:C15986` | SMALL_MOLECULE | Case-level |
| Capsaicin, menthol, DMSO | `NCIT:C15986` | SMALL_MOLECULE | Antipruritic; low-quality evidence |
| Amitriptyline | `NCIT:C15986` | SMALL_MOLECULE | Effective for itch in familial lichen amyloidosis [lead] |
| Colchicine, cyclophosphamide, cyclosporine, cepharanthine | `NCIT:C15986` | SMALL_MOLECULE | Historical; inconsistent [lead, PMID:28342016 Weidner 2017] |
| Hydrocolloid dressings; **cessation of friction/nylon-towel use** | `NCIT:C15747` Supportive Care | BEHAVIORAL / DEVICE | Rational and low-risk; consensus-level |
| **Phototherapy** (NB-UVB, PUVA, UVB) | `NCIT:C15301` Phototherapy | RADIOTHERAPY/DEVICE — likely `OTHER` | Mixed/variable outcomes [lead, PMID:38137741] |

The Weidner systematic review (1985–2016) catalogues the full conventional armamentarium — "retinoids, corticosteroids, cyclophosphamide, cyclosporine, amitriptyline, colchicine, cepharanthin, tacrolimus, dimethyl sulfoxide, vitamin D3 analogs, capsaicin, menthol, hydrocolloid dressings, surgical modalities, and laser treatment" [lead: Weidner, Illing & Elsner, *Am J Clin Dermatol* 2017;18:629–642, doi:10.1007/s40257-017-0278-9].

### Biologics — the mechanistically motivated arm

**Dupilumab** (anti-IL-4Rα; blocks IL-4/IL-13) — the best-documented modern option. `NCIT:C162455` Dupilumab; `therapeutic_modality: MONOCLONAL_ANTIBODY`.

> "As of October 2024, 14 patients with PCA (including our 2 patients) tried dupilumab treatment, with female to male ratio of 7:7. These patients aged 20–76 years old, and their medical history of PCA ranged from 3–27 years. All of them resisted to traditional therapy for PCA, and achieved disease relief on dupilumab treatment. Itching usually alleviated firstly, with a reported remission time of 1–12 weeks after treatment. Skin lesions improved later, which began and largely resolved after 4 weeks and 28 weeks, respectively. 4 patient patients got complete skin lesions remission" — **PMID:39975679** [cached, full text]

Dosing used: 600 mg loading, then 300 mg q2w. Notably effective in **non-atopic** patients, which argues the benefit isn't purely treatment of concurrent eczema [cached, PMID:39975679]. Corroborated by **PMID:39953901** [cached — title/metadata only; no abstract body, so cite by title].

**Nemolizumab** (anti-IL-31RA) — the most mechanistically on-target agent, given the demonstrated **epidermal IL-31RA/OSMRβ overexpression** [cached, PMID:26748444]. `NCIT:C170211` Nemolizumab; `MONOCLONAL_ANTIBODY`. Reported successful in PLCA with atopic dermatitis [lead: Fukumoto 2024, *JEADV*, doi:10.1111/jdv.20039] and in a **refractory non-atopic** patient [lead: *JAAD Case Rep* 2025, PMC12256333]. This is the clearest example in PLCA of receptor biology directly nominating a drug.

### JAK inhibitors — the newest and arguably most promising arm

Rationale is direct: the *OSMR*/*IL31RA* receptors signal through JAK/STAT, and IL-4/IL-13/IL-31 itch signaling is JAK-dependent.

**Tofacitinib** — `NCIT:C95800`; `SMALL_MOLECULE`. Two independent 2025 reports:
- Retrospective series, **n=24**, tofacitinib 10 mg daily: *"significant improvements were observed in BSA (p < 0.05), PP-NRS (p < 0.001), and IGA (p < 0.01) at week 4"*; good tolerability, no serious AEs causing discontinuation [lead: Wang et al., *J Dermatol* 2025, **PMID:40908738**]
- Single-arm clinical trial, week 10: pruritus NRS 6.9 → 0.4; DLQI 11.8 → 2.6; Lesion Severity 13.3 → 4.9 [lead: *Clin Exp Dermatol* 2026;51(1):86, doi:10.1093/ced/llaf364]

**Others:** baricitinib (refractory CLA + AD), upadacitinib (case report of remission), abrocitinib (LA with AD) — all case-level [leads].

### Procedural / device

A 2025 systematic review of **16 studies, 432 patients** covering fractional CO₂ laser, Nd:YAG, Er:YAG, microneedling, and phototherapy [lead: *Lasers Med Sci* 2025, doi:10.1007/s10103-025-04783-3]. NCIT: `NCIT:C15466` Laser Therapy or `NCIT:C157901` Laser Resurfacing; `therapeutic_modality: DEVICE`. Also dermabrasion, surgical excision (nodular/localized lesions).

### Nodular-form-specific
Excision, intralesional corticosteroid, laser, and — for a monoclonal-gammopathy-associated case — **bortezomib + dexamethasone** (plasma-cell-directed, targeting the actual AL source) [lead: PMID:34894809].

### Pharmacogenomics
**No PharmGKB/CPIC guidance specific to PLCA.** Generic considerations apply for JAK inhibitors (thromboembolic/malignancy boxed warnings, TB screening) — not PLCA-specific.

### Advanced therapeutics
**No gene therapy, cell therapy, RNA-based therapy, or gene editing** is in development for PLCA. **No registered interventional clinical trials on ClinicalTrials.gov were identified** for PLCA in this search — the tofacitinib "single-arm clinical trial" appears to be investigator-initiated and may not carry an NCT ID. **Verify on ClinicalTrials.gov before adding any `clinical_trials:` block.**

### Treatment strategy / algorithm (synthesized, expert-consensus level)

1. **Confirm diagnosis** by biopsy with Congo red; **type the amyloid** if nodular.
2. **Exclude systemic disease** (mandatory for nodular; prudent for atypical/generalized).
3. **Screen for MEN2A** if interscapular or generalized CLA → *RET* testing.
4. **Remove the driver:** stop nylon towel/brush friction; treat any underlying pruritic dermatosis (especially atopic dermatitis).
5. **First line:** high-potency topical corticosteroid ± occlusion; topical calcineurin inhibitor; emollients; antipruritics.
6. **Second line:** phototherapy (NB-UVB); topical/oral retinoid; amitriptyline for neuropathic itch.
7. **Refractory:** **dupilumab** (best evidence base) or **nemolizumab** (most on-target) or an **oral JAK inhibitor** (fastest antipruritic effect, largest series).
8. **Adjunct/cosmetic:** fractional CO₂ or Nd:YAG laser, microneedling for pigmentation and texture.
9. **Nodular with monoclonal protein:** hematology referral; plasma-cell-directed therapy; lifelong systemic surveillance.

**No head-to-head comparisons exist. No combination-therapy regimens are established.** Personalized/genotype-guided treatment is aspirational — plausible but untested is the hypothesis that *IL31RA*/*OSMR*-mutant patients should preferentially receive IL-31-axis blockade (nemolizumab) or JAK inhibition. This is a good candidate for a `mechanistic_hypotheses` entry with `status: EMERGING`.

---

## 13. Prevention

**Primary prevention.** The only actionable measure is **avoidance of chronic frictional skin trauma** — discontinuing nylon towels, brushes, and loofahs, particularly in high-prevalence populations where this is a cultural bathing practice. Public-health education in Taiwan/Southeast Asia/Middle East is a plausible but **untested** intervention. Adequate treatment of pre-existing pruritic dermatoses (especially atopic dermatitis) to prevent the scratch–deposition cycle is a reasonable secondary aim.

**Secondary prevention.** Early recognition and biopsy of persistent pruritic hyperpigmented lesions, particularly in high-prevalence populations, to interrupt the cycle before dense amyloid accumulates.

**Tertiary prevention.**
- Aggressive itch control to prevent excoriation, lichenification, secondary infection, and further deposition
- **Nodular PLCA:** periodic surveillance for systemic AL amyloidosis (SPEP/UPEP/free light chains, NT-proBNP, renal function) — indefinite
- **MEN2A-associated CLA:** the highest-value preventive action in this whole disease area — *RET* genotype-directed prophylactic thyroidectomy and biochemical surveillance for pheochromocytoma/hyperparathyroidism per MEN2 guidelines

**Immunization.** Not applicable.

**Screening programs.** None; not indicated for keratinocyte-derived PLCA (see §10).

**Genetic screening / counseling.**
- **AD forms (*OSMR*/*IL31RA*):** 50% recurrence risk to offspring; counsel on variable expressivity and incomplete penetrance. PGD/prenatal testing is technically available but **not clinically indicated** for a non-life-threatening, non-disabling adult-onset skin condition — this should be stated explicitly to avoid implying otherwise.
- **AR form (*GPNMB*/ACD):** 25% sib recurrence risk; carrier testing relevant in consanguineous families (both reported Pakistani ACD families were consanguineous [cached, PMID:33687658]). Counseling on consanguinity risk is appropriate.
- ***RET*/MEN2A:** entirely different calculus — cascade testing is **strongly indicated** and life-saving.

**Risk stratification.** No validated risk models exist.

**Public health / environmental interventions.** Education about frictional bathing practices; no sanitation, vector-control, or pollutant-reduction dimension.

**Prophylaxis.** No prophylactic medication.

---

## 14. Other Species / Natural Disease

**Taxonomy.** Human (`NCBITaxon:9606`). Experimental models in *Mus musculus* (`NCBITaxon:10090`).

**Naturally occurring homologous disease: essentially absent.** No entry in OMIA corresponding to primary localized cutaneous amyloidosis was identified, and no companion-animal or wildlife counterpart is described. **This is a genuine negative finding and should be recorded as such**, not left blank.

Related but **not** homologous animal observations (do not conflate):
- **Cutaneous amyloidosis in horses** — nodular/plaque-forming, immunoglobulin-derived (AL-like); mechanistically the equine analog of *nodular* PLCA, not of lichen/macular PLCA [general veterinary dermatology; verify before citing]
- **DBA/2J mouse** — carries a truncating *Gpnmb* mutation causing iris pigment dispersion and pigmentary glaucoma. This is the same gene as human ACD but a **different organ and phenotype** [lead]. It is nonetheless the most informative naturally occurring *Gpnmb*-null model and is worth a `HUMAN_MODEL_MISMATCH` note.
- **Breeds (VBO):** none identified.

**Orthologous genes** (verify NCBI Gene IDs before curating): *Osmr* (mouse), *Il31ra* (mouse), *Gpnmb* (mouse; DBA/2J allele), *Ret* (mouse).

**Comparative biology.** The IL-6-family cytokine receptor architecture (gp130/OSMRβ/IL-31RA) is well conserved across mammals, and the *IL31RA* p.S521 codon is *"well conserved in mammals"* [cached, PMID:19690585]. However — and this is the key comparative point — **the downstream skin phenotype is NOT conserved** (see §15).

**Zoonotic potential / cross-species transmission.** None. Not an infectious or transmissible amyloidosis (unlike AA amyloidosis, which has demonstrated transmissible seeding in some animal systems).

---

## 15. Model Organisms

### Available models

**1. *Osmr*<sup>−/−</sup> C57BL/6 mouse (CRISPR/Cas9)** — the flagship model [cached, PMID:33502684]

Recapitulated features:
- Significantly increased tail epidermal thickness at P30 (n=19 across three litters, 10M/9F)
- RNA-seq: 2-fold change in 2,328 genes; GO enrichment for keratinocyte differentiation and skin development; 39 differentially expressed genes known to relate to epidermal keratinocyte differentiation
- Confirmed upregulation of *Krt1*, *Krt10*, *Flg*, *Lor* by qRT-PCR and Western blot
- Significantly increased basal keratinocyte proliferation (EdU incorporation) in tail and dorsal skin
- Decreased *Klf7* expression vs WT
- Hair follicle cycle changes at P30

**⚠️ Critical limitation — this is a textbook `HUMAN_MODEL_MISMATCH`, not a generic knowledge gap:**

> "Unfortunately, no PLCA-like phenotype was observed in these mice under physiological or pathological conditions (including UVA exposure and an itch challenge; data not shown)." — **PMID:33502684** [cached, full text]

The mouse reproduces the *upstream cellular* mechanism (differentiation/proliferation dysregulation) but **not the disease-defining outcome** (dermal amyloid deposition, pruritic lesions) — even when challenged with UVA and an itch stimulus. Note also that the mouse is a **complete knockout** whereas human disease arises from **heterozygous partial-loss-of-function missense** alleles, so the model isn't even genotype-matched. Recommended dismech treatment: a `discussions:` entry with `kind: HUMAN_MODEL_MISMATCH`, prompt phrased as a question ("Does murine *Osmr* loss fail to produce cutaneous amyloid because mouse epidermis lacks a human-specific keratin-amyloidogenic property, because heterozygous missense ≠ null, or because murine skin lacks the requisite frictional/pruritic environmental co-factor?"), with proposed experiments including knock-in of the human p.P694L allele, chronic mechanical friction challenge, and humanized-keratin backgrounds.

**2. *Osmr* knockout mouse — AHNAK arm** [cached, PMID:37100691]: gene-edited mice confirmed that *OSMR* knockout abolishes OSM-mediated AHNAK downregulation, matching human lesional findings.

**3. HaCaT immortalized human keratinocyte line** — the principal in vitro workhorse. Available derivatives: *OSMR*-knockout HaCaT (CRISPR), *KLF7*-knockout HaCaT (two independent clones), and *OSMR*-knockout HaCaT reconstituted with lentiviral WT / p.G513D / p.P694L OSMR-P2A-GFP. This last construct set is the definitive tool for variant functional assay [cached, PMID:33502684].

**4. NHEK — primary normal human epidermal keratinocytes** [cached, PMID:33502684, PMID:37100691]

**5. 3D reconstituted human epidermis / organotypic skin models** — used to confirm OSM-driven suppression of FLG/LOR and AHNAK regulation in a stratified tissue context [cached, PMID:33502684, PMID:37100691]

**6. Patient-derived primary keratinocyte cultures** — the original functional evidence: *"cultured FPLCA keratinocytes showed reduced activation of Jak/STAT, MAPK, and PI3K/Akt pathways after OSM or IL-31 cytokine stimulation"* [cached, PMID:18179886]

**7. HeLa cells** — used for GPNMB functional work [cached, PMID:29336782]

**8. HEK293T** — *KLF7* promoter luciferase reporter assays [cached, PMID:33502684]

**9. *In silico*:** I-TASSER 3D structural modeling of GPNMB variant stability [cached, PMID:33687658] — `evidence_source: COMPUTATIONAL`

**10. DBA/2J mouse** (spontaneous *Gpnmb* truncation) — relevant to the ACD arm but with an ocular, not cutaneous, phenotype [lead]

### Model limitations (aggregate)

| Limitation | Impact |
|---|---|
| **No model reproduces cutaneous amyloid deposition** | The disease-defining lesion cannot currently be studied in vivo |
| No model reproduces pruritus/scratching behavior | The dominant clinical symptom is unmodeled |
| Knockouts model nullizygosity, not human heterozygous missense | Genotype–model mismatch |
| Mouse keratins may differ in amyloidogenic propensity from human K5/K14 | Possible species-intrinsic barrier |
| HaCaT is aneuploid/immortalized | Differentiation program is not fully physiological |
| **No iPSC-derived keratinocyte model reported** | Clear opportunity |
| **No patient-derived organoid/skin-on-chip model reported** | Clear opportunity |

### Research applications
Validated uses: dissecting OSM/OSMRβ/STAT5/KLF7 signaling; variant functional classification (the reconstituted *OSMR*-KO HaCaT system is essentially a ready-made functional assay for ACMG PS3-level evidence); keratinocyte differentiation/proliferation biology; drug-target validation for JAK/STAT5 inhibition. **Not** currently usable for: amyloidogenesis kinetics, itch pharmacology, or anti-amyloid therapeutic screening.

### Resources
MGI (*Osmr*, *Il31ra*, *Gpnmb* alleles), IMPC/KOMP, IMSR, Cellosaurus (HaCaT: CVCL_0038), ATCC. RNA-seq data: **GEO GSE150884, GSE150994, GSE151174**.

---

## Appendix A — Suggested dismech modeling notes

**Module conformance.** This entry is a strong candidate to declare `conforms_to` against **`amyloidogenesis`** (already in `kb/modules/`), substituting the disease-specific precursor:

| `amyloidogenesis` node | PLCA substitution |
|---|---|
| `#Amyloidogenic Precursor Protein` | Epidermal keratins **K5/K14** from degenerating basal keratinocytes (AL light chain in the *nodular* subtype — a genuinely different precursor, so consider separate `has_subtypes` handling) |
| `#Protein Misfolding and Beta-Sheet Oligomerization` | Filamentous degeneration of tonofilaments; β-sheet conversion ± galectin-7/ApoE/SAP co-deposition |
| `#Amyloid Fibril Formation and Extracellular Deposition` | Papillary dermal deposition (`UBERON:0001992`) |
| `#Progressive Tissue Amyloid Accumulation` | Compounded by impaired MCP-1/monocyte clearance |
| `#Organ Dysfunction` | Pruritus, small-fibre neuropathy, dyschromia — **skin-limited** |

Consider also `epithelial_barrier_dysfunction` for the hyperkeratosis/differentiation arm, and note the **`peripheral_axonal_degeneration`** module as a possible partial conformer for the small-fibre neuropathy node.

**Subtype structure.** Model `has_subtypes` with short slug-friendly names: `Lichen`, `Macular`, `Biphasic`, `Nodular`, `ACD`, `MEN2A-CLA`. The **nodular** subtype is mechanistically a *different disease* (AL, plasma cell clone, systemic risk) — flag this prominently in its `description` and in a `grouping_rationale`-style note, since lumping it into a keratin-origin pathograph would be a substantive error.

**Grouping opportunity.** A `Cutaneous_Amyloidoses` grouping (`grouping_basis: [SHARED_PHENOTYPE, CLINICAL_CONVENTION]`) over PLCA + nodular + ACD + secondary cutaneous amyloidosis, with `criteria_semantics: NECESSARY`, would capture the boundary auditably.

**Evidence-source tagging discipline for this entry:**
- PMID:6184423, 18179886 (patient keratinocytes), 26748444, 29336782, 30734345, 18576343, 39975679, 42194535 → `HUMAN_CLINICAL` (18179886's cell work is IN_VITRO — split the evidence items)
- PMID:33502684 (Osmr−/− mouse), 37100691 (gene-edited mice) → `MODEL_ORGANISM`; split their HaCaT/3D-skin claims to `IN_VITRO`
- PMID:33687658 I-TASSER modeling → `COMPUTATIONAL`
- PMID:41528921, 42029085 → narrative reviews; prefer primary sources, use these for framing/synthesis statements only

**Do not curate without fetching first:** every PMID marked **[lead]** above. Run `just fetch-reference PMID:XXXXXXX` and verify snippet-as-exact-substring before writing any evidence item. Note specifically that **PMID:24237668, PMID:31478212, PMID:34459039, and PMID:39953901 have title/metadata-only cache records with no abstract body** — no snippet can be quoted from them; either cite by title with a `notes:`-level claim or find an alternative source.

---

## Appendix B — Explicit "not available" findings

For completeness, the following were searched for and **not found** — record as absent rather than omitting:

- Formal consensus diagnostic criteria (no society guideline)
- Population prevalence outside the single Asian estimate
- Any registered interventional clinical trial with an NCT identifier
- Any approved therapy
- Disease-specific mortality or survival data (keratinocyte-derived forms)
- Metabolomic, lipidomic, epigenomic, or single-cell/spatial transcriptomic data
- Validated prognostic or diagnostic circulating biomarkers
- Newborn/carrier/population screening programs
- Naturally occurring homologous disease in other species (OMIA)
- iPSC-derived or organoid disease models
- Pharmacogenomic (PharmGKB/CPIC) guidance
- Any animal model that reproduces cutaneous amyloid deposition

---

## Sources

**Verified from local reference cache (safe to quote):**
- [PMID:6184423](https://pubmed.ncbi.nlm.nih.gov/6184423/) — Kobayashi & Hashimoto, *J Invest Dermatol* 1983 — keratin origin of skin amyloid
- [PMID:18179886](https://pubmed.ncbi.nlm.nih.gov/18179886/) — Arita et al., *Am J Hum Genet* 2008 — *OSMR* mutations in FPLCA
- [PMID:18576343](https://pubmed.ncbi.nlm.nih.gov/18576343/) — Meijer et al., *Arthritis Rheum* 2008 — Sjögren + nodular amyloidosis
- [PMID:19690585](https://pubmed.ncbi.nlm.nih.gov/19690585/) — Lin et al., *Eur J Hum Genet* 2010 — *IL31RA* mutation, ancestral *OSMR* allele
- [PMID:24237668](https://pubmed.ncbi.nlm.nih.gov/24237668/) — Chang et al., *Br J Dermatol* 2014 — DNA mass spectrometry in sporadic PLCA
- [PMID:26748444](https://pubmed.ncbi.nlm.nih.gov/26748444/) — Tey et al., *Br J Dermatol* 2016 — pruritus/small-fibre neuropathy
- [PMID:29336782](https://pubmed.ncbi.nlm.nih.gov/29336782/) — Yang et al., *Am J Hum Genet* 2018 — *GPNMB* loss causes ACD
- [PMID:30085596](https://pubmed.ncbi.nlm.nih.gov/30085596/) — Lath et al., StatPearls — MEN2
- [PMID:30734345](https://pubmed.ncbi.nlm.nih.gov/30734345/) — Lu et al., *Clin Exp Dermatol* 2019 — Chinese *OSMR* mutation spectrum
- [PMID:31478212](https://pubmed.ncbi.nlm.nih.gov/31478212/) — Adams et al., *Clin Exp Dermatol* 2020 — novel OSM/IL-31 receptor mutation
- [PMID:33502684](https://pubmed.ncbi.nlm.nih.gov/33502684/) — Liu et al., *Protein Cell* 2021 — STAT5/KLF7 axis
- [PMID:33687658](https://pubmed.ncbi.nlm.nih.gov/33687658/) — Rahman et al., *Genes Genomics* 2021 — *GPNMB* missense in Pakistani families
- [PMID:34459039](https://pubmed.ncbi.nlm.nih.gov/34459039/) — Bourguiba et al., *JEADV* 2022 — keratin 5/14 amyloid subtyping
- [PMID:37100691](https://pubmed.ncbi.nlm.nih.gov/37100691/) — Liu et al., *J Dermatol Sci* 2023 — AHNAK
- [PMID:39953901](https://pubmed.ncbi.nlm.nih.gov/39953901/) — Te et al., *J Cutan Med Surg* 2025 — off-label dupilumab
- [PMID:39975679](https://pubmed.ncbi.nlm.nih.gov/39975679/) — Guo et al., *Front Med* 2025 — dupilumab cases + literature review
- [PMID:41528921](https://pubmed.ncbi.nlm.nih.gov/41528921/) — Janodia & Schwartz, *Dermatology* 2026 — updated approach
- [PMID:42029085](https://pubmed.ncbi.nlm.nih.gov/42029085/) — Teng et al., *Int J Dermatol* 2026 — OSM/IL-31 mechanistic review
- [PMID:42194535](https://pubmed.ncbi.nlm.nih.gov/42194535/) — Łabędź et al., *J Clin Med* 2026 — generalized CLA with RET Y806C

**Leads requiring verification:**
- [OMIM 105250 — PLCA1](https://omim.org/entry/105250) · [OMIM 613955 — PLCA2](https://omim.org/entry/613955) · [OMIM 601743 — OSMR](https://omim.org/entry/601743)
- [Orphanet 137807 — primary cutaneous amyloidosis](https://www.orpha.net/en/disease/detail/137807) · [Orphanet 137810 — nodular](https://www.orpha.net/en/disease/detail/137810)
- [PMID:38137741 — PLCA in Central Europe (PMC10743860)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743860/)
- [PMID:40908738 — Tofacitinib for PLCA](https://pubmed.ncbi.nlm.nih.gov/40908738/) · [Tofacitinib single-arm trial, *Clin Exp Dermatol* 2026](https://academic.oup.com/ced/article/51/1/86/8226010)
- [Weidner et al. 2017 — systematic treatment review](https://link.springer.com/article/10.1007/s40257-017-0278-9)
- [Hamie et al. 2021 — atypical clinical variants](https://link.springer.com/article/10.1007/s40257-021-00620-9)
- [2025 systematic review of procedural treatment, *Lasers Med Sci*](https://link.springer.com/article/10.1007/s10103-025-04783-3)
- [Nemolizumab in refractory non-atopic PLCA (PMC12256333)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12256333/) · [Nemolizumab with AD, *JEADV* 2024](https://onlinelibrary.wiley.com/doi/10.1111/jdv.20039)
- [PMID:39663859 — Congo red + fluorescence microscopy](https://pubmed.ncbi.nlm.nih.gov/39663859/)
- [PMID:32867548 — main constituent is not galectin-7](https://pubmed.ncbi.nlm.nih.gov/32867548/) · [PMID:23278892 — galectin-7 and actin](https://pubmed.ncbi.nlm.nih.gov/23278892/) · [PMID:25172508 — galectin-7 amyloidogenic peptides](https://pubmed.ncbi.nlm.nih.gov/25172508/)
- [PMID:12864791 — MEN2A and CLA association](https://pubmed.ncbi.nlm.nih.gov/12864791/) · [Endocrine perspective on CLA, RET C634 (PMC11587112)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11587112/)
- [Health-related QoL in PCA, *PLOS One* 2015 (PMC4370430)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4370430/)
- [PMID:2224732 — epidemiology of PCA in Southeast Asia](https://pubmed.ncbi.nlm.nih.gov/2224732/) · [PLCA review, *Pigment International* 2023](https://journals.lww.com/pigi/fulltext/2023/10010/primary_localized_cutaneous_amyloidosis___a_review.2.aspx)
- [PMID:19207438 — nylon towel friction](https://pubmed.ncbi.nlm.nih.gov/19207438/) · [PMID:9330050 — nylon cloth macular amyloidosis](https://pubmed.ncbi.nlm.nih.gov/9330050/) · [PMID:3391726 — friction amyloidosis](https://pubmed.ncbi.nlm.nih.gov/3391726/)
- [PMID:31260093 — three novel GPNMB mutations](https://pubmed.ncbi.nlm.nih.gov/31260093/) · [PMID:34894809 — bortezomib for nodular PLCA](https://pubmed.ncbi.nlm.nih.gov/34894809/)
- [ClinVar VCV000030221 — OSMR p.Pro694Leu](https://www.ncbi.nlm.nih.gov/clinvar/variation/30221/) · [Histopathological insights case series (PMC11947714)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11947714/) · [Dermatoscopy of PLCA, *Skin Health Dis* 2024](https://onlinelibrary.wiley.com/doi/full/10.1002/ski2.316) · [ICD-10 E85.4](https://icdlist.com/icd-10/E85.4)