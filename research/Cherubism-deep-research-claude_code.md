---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-22T09:38:13.749871'
end_time: '2026-07-22T09:44:58.143711'
duration_seconds: 404.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cherubism
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
  - claude-opus-4-8
  web_search_requests: 8
  num_turns: 13
  total_cost_usd: 1.8790139999999997
  session_id: bcf6e95d-88ad-40b6-bff4-85b587a63955
  stop_reason: end_turn
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cherubism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cherubism** covering all of the
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

Alright, I've got the whole picture — from the RSPPDG motif all the way to the denosumab case reports. Here's the full workup.

---

# Cherubism — Comprehensive Disease Research Report

> **Quick orientation before the deep dive:** Cherubism is a rare, mostly self-limiting childhood bone disease where the jaw quietly eats itself and refills with fluffy, giant-cell-rich fibrous tissue. The wild part is the biology — a single-letter change in an adapter protein makes it *un-killable* by the cell's normal disposal crew, and the whole thing behaves less like a bone tumor and more like a slow-burning autoinflammatory tantrum aimed at the jaws. Then, in most kids, it just... turns itself off around puberty. Below is everything the literature has to say, section by section.

---

## 1. Disease Information

Cherubism is a rare, benign, self-limiting fibro-osseous disorder in which bone of the mandible and maxilla is resorbed and replaced by expansile, soft, fibrous giant-cell-rich tissue, producing bilateral, symmetric jaw swelling. The name comes from the resulting round-cheeked face plus the upturned-eye look ("eyes raised to heaven") when the orbital floor is involved — reminiscent of cherubs in Renaissance art (first named by Jones in 1933).

**Key identifiers:**
- **OMIM:** #118400 (Cherubism); causal gene SH3BP2 is *602104
- **MONDO:** MONDO:0007038 *(suggested — curator should confirm via OAK)*
- **Orphanet:** ORPHA:184
- **MeSH:** D002636 (Cherubism)
- **ICD-10:** commonly coded K10.8 ("Other specified diseases of jaws"); ICD-11 near LB43/DA0D range *(coding is inconsistent across sources — flag for verification)*

**Synonyms / alternative names:** familial fibrous dysplasia of the jaws, familial multilocular cystic disease of the jaws, familial bilateral giant cell tumor of the jaw, cherubinism, bilateral giant cell tumor. (Note: "familial fibrous dysplasia" is a misnomer — cherubism is molecularly distinct from *GNAS*-driven fibrous dysplasia.)

**Data provenance:** The disease-level knowledge is drawn from aggregated resources (OMIM, Orphanet, GeneReviews) and a literature base of ~300–600 published cases/case series worldwide — not from large EHR cohorts. Individual-patient granularity comes from case reports and small family studies.

Sources: [OMIM 118400](https://omim.org/entry/118400), [GeneReviews NBK1137](https://www.ncbi.nlm.nih.gov/books/NBK1137/), [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=184)

---

## 2. Etiology

**Primary cause — genetic:**
- **SH3BP2 gain-of-function (≈80% of cases):** heterozygous missense variants clustered in exon 9, within the 6-residue motif **RSPPDG (p.Arg415–Gly420)**. Autosomal dominant. (Ueki et al., *Nat Genet* 2001, PMID:11381256 — "identified mutations in the SH3BP2 gene… All mutations were in exon 9 and affected 3 amino acids within a 6-amino acid sequence (RSPPDG).")
- **OGFRL1 biallelic loss-of-function (rare, recessive):** two consanguineous families (Syria, India) with homozygous loss-of-function *OGFRL1* variants; autosomal recessive. A newly recognized second locus. ([JBMR Plus 2024, ziae050](https://academic.oup.com/jbmrplus/article/8/6/ziae050/7642758), PMC11062026)
- ~20% of clinically classic cases have **no identified SH3BP2 variant** — genetic heterogeneity remains.

**Genetic risk factors:** having a pathogenic SH3BP2 allele is essentially deterministic (high penetrance); no established polygenic/susceptibility loci. De novo mutations account for a substantial share of simplex cases.

**Environmental risk / trigger factors:** Cherubism is genetically driven, but disease *expression and severity* are modulated by inflammatory challenge. In heterozygous cherubism mice, oral microbial burden (periodontal infection) dramatically worsens alveolar bone destruction — "microbe-dependent exacerbated alveolar bone destruction in heterozygous cherubism mice" ([PMC7285758](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7285758/)). This maps to the human observation that lesions flare with dental eruption, trauma, and infection. There is also anecdotal exacerbation with tooth extraction/surgery.

**Protective factors:** No genetic protective alleles described. Empirically, the strongest "protective" force is **puberty/aging itself** — most lesions spontaneously regress after adolescence. Avoiding elective jaw surgery during the active proliferative phase is considered protective against flare.

**Gene–environment interaction:** The unifying model is that mutant SH3BP2 lowers the threshold for a myeloid inflammatory response, so ordinary physiologic/microbial challenges to the jaw (tooth eruption, oral flora) that a normal jaw shrugs off instead ignite a self-amplifying TNF-α/RANKL loop. This explains both jaw-restriction (the tooth-bearing bones face the most microbial/eruption challenge) and the age-limited course.

---

## 3. Phenotypes

**Craniofacial / skeletal (core, near-universal):**
- **Bilateral, symmetric mandibular and/or maxillary swelling** — clinical hallmark; onset typically age 2–5 yr, progresses to puberty. Frequency ~100%. Suggested HPO: **HP:0000303 (Mandibular prognathia)**, **HP:0012802 (Abnormal maxilla morphology)**, plus round/full cheeks.
- **Multilocular radiolucent, expansile jaw lesions** with cortical thinning, at the mandibular angles/rami; condyles usually spared.
- **"Eyes to heaven" appearance / exposed inferior sclera / upward globe tilt** when infraorbital rim and orbital floor are involved. Suggested HPO: **HP:0000520 (Proptosis)** and exposure of sclera.

**Dental (very frequent):**
- Displaced, unerupted, ectopic, hypoplastic, or absent teeth; premature exfoliation of primary teeth; malocclusion. Suggested HPO: **HP:0000668 (Hypodontia)**, **HP:0000689 (Dental malocclusion)**, **HP:0006480/HP:0006349 (abnormal tooth morphology)**, premature tooth loss (**HP:0006480**).

**Regional / soft tissue:**
- **Submandibular and cervical lymphadenopathy** — common in early active disease, tends to regress. Suggested HPO: **HP:0002716 (Lymphadenopathy)**.

**Functional complications (severe cases):**
- **Obstructive sleep apnea / upper-airway obstruction** — GeneReviews: "Respiratory manifestations can include obstructive sleep apnea and upper-airway obstruction." Suggested HPO: **HP:0002870 (Obstructive sleep apnea)**.
- **Visual/ophthalmologic compromise** (proptosis, diplopia, rarely optic involvement) with severe maxillary/orbital disease. Suggested HPO: **HP:0000505 (Visual impairment)**, **HP:0000651 (Diplopia)**.
- Speech, chewing, and swallowing difficulty; psychosocial impact from facial disfigurement.

**Characteristics summary:** Onset early childhood; severity **highly variable** (mild grade-1 to grossly disfiguring grade-3); course **progressive then regressive** (grows to puberty, stabilizes, involutes in 2nd–3rd decade). **Intellect and general development are normal.**

**Quality-of-life impact:** Main burdens are cosmetic disfigurement (psychosocial, especially school-age), functional (mastication, speech, vision, sleep/airway), and — in a subset — surgical morbidity. No cherubism-specific validated QoL instrument; generic pediatric craniofacial QoL tools apply.

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1137/), [Cherubism: best clinical practice, Orphanet J Rare Dis 2012;7(Suppl 1):S6](https://link.springer.com/article/10.1186/1750-1172-7-S1-S6)

---

## 4. Genetic / Molecular Information

**Causal gene 1 — SH3BP2** (SH3-domain binding protein 2; a.k.a. 3BP2)
- Locus: **chromosome 4p16.3**; HGNC symbol SH3BP2 (HGNC:10825, lowercase `hgnc:` per repo convention — verify ID); OMIM *602104.
- Mapping: linkage to 4p16.3 established by Mangion et al. (*Am J Hum Genet* 1999). ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0002929707637380))
- Protein: 561-aa adapter with **PH domain** (membrane lipid binding), a **proline-rich (PR) region** with SH3-binding motifs, and a C-terminal **SH2 domain**.

**Pathogenic variants (SH3BP2):**
- Cluster in **exon 9**, within the **RSPPDG motif (codons 415–420)**.
- Recurrent variants: **p.Pro418Arg (c.1253C>G)** — most common; **p.Pro418Leu**, **p.Arg415Gln/Pro**, **p.Gly420Glu/Arg**, **p.Pro416Arg**, **p.Asp419** changes. ~13 distinct variants reported (12 missense + 1 single-base deletion), ~80% in exon 9.
- **Variant type:** overwhelmingly missense; **germline**; **gain-of-function** (not haploinsufficiency — Wolf-Hirschhorn 4p deletions that delete one *SH3BP2* copy do **not** cause cherubism).
- **Allele frequency:** absent/vanishingly rare in gnomAD (private/de novo pathogenic changes).
- **ACMG classification:** recurrent RSPPDG missense variants are classified Pathogenic/Likely Pathogenic (strong functional + genetic evidence).

**Causal gene 2 — OGFRL1** (opioid growth factor receptor-like 1)
- **Biallelic loss-of-function**, autosomal recessive; homozygous frameshift/LoF variants "not reported in any variant databases." Represents a mechanistically distinct route to a cherubism-like phenotype. ([JBMR Plus 2024](https://academic.oup.com/jbmrplus/article/8/6/ziae050/7642758))

**Modifier genes:** none formally validated; disease severity likely modified by inflammatory-response genetic background (inferred from mouse work) and sex.

**Epigenetics / chromosomal abnormalities:** No recurrent DNA-methylation/histone signature or large structural rearrangement is implicated. Cherubism is a point-mutation disease, not a copy-number/aneuploidy disorder. (Notably, 4p deletion *removing* SH3BP2 does **not** cause disease — reinforcing gain-of-function.)

Suggested ontology: gene GO annotations **GO:0017124 (SH3 domain binding)**, **GO:0035591 (signaling adaptor activity)**.

Sources: [Nature Genetics 2001](https://www.nature.com/articles/ng0601_125), [OMIM 602104](https://omim.org/entry/602104), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1137/)

---

## 5. Environmental Information

- **Environmental factors:** No toxin/radiation/occupational cause. The relevant environmental input is **local oral–microbial and mechanical challenge** to the jaws. Mouse data show oral microbes drive exacerbated alveolar bone destruction in heterozygous cherubism mice ([PMC7285758](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7285758/)).
- **Lifestyle factors:** none established. Good oral hygiene / periodontal-inflammation control is biologically rational given the microbe-dependence data.
- **Infectious agents:** No single pathogen causes cherubism. Periodontal/oral bacterial burden acts as a **modifier/trigger** of severity, not an etiologic agent. (Suggested taxon anchor if modeled: oral microbiota, NCBITaxon of specific periopathogens not disease-defining.)

---

## 6. Mechanism / Pathophysiology

This is the mechanistically richest part, so let me lay out the causal chain from mutation to melted jawbone.

**Upstream trigger — loss of protein disposal (the keystone lesion):**
Normally, the adapter protein **3BP2/SH3BP2** is kept on a short leash. **Tankyrase (TNKS/TNKS2, a PARP-family enzyme)** binds SH3BP2 at the **RSPPDG (RxxPDG) motif**, **poly-ADP-ribosylates** it, which flags it for the E3 ubiquitin ligase **RNF146**, which ubiquitylates it for **proteasomal degradation**. Cherubism mutations (R415G, P418L, P418R, G420R) **destroy the tankyrase recognition site** → SH3BP2 is no longer ADP-ribosylated, no longer ubiquitylated, and **accumulates**. So the defect isn't a broken protein — it's a protein the cell can't throw away. (Levaot et al., *Cell* 2011, PMID:22153076 — "Loss of Tankyrase-Mediated Destruction of 3BP2 Is the Underlying Pathogenic Mechanism of Cherubism"; Guettler et al., *Cell* 2011, companion paper on tankyrase substrate recognition.) Elegant corollary: **tankyrase inhibitors phenocopy cherubism**, inducing bone loss by accumulating SH3BP2 ([PMC6406327](https://ncbi.nlm.nih.gov/pmc/articles/PMC6406327)).

**Middle — two amplifying myeloid arms** (from the *Sh3bp2* P416R knock-in mouse; Ueki et al., *Cell* 2007, PMID:17218256):
1. **Osteoclast arm (bone destruction):** Stabilized SH3BP2 hyperactivates **SYK/SRC/VAV** and, downstream of RANKL–RANK, boosts **PLCγ2 phosphorylation → IP₃ → Ca²⁺ release → calcineurin → NFATc1 nuclear translocation** — NFATc1 being the master transcriptional switch for osteoclastogenesis. Result: more, more-active, bone-resorbing osteoclasts. (Mukai et al., *JBMR* 2014, doi:10.1002/jbmr.2295 — "SH3BP2 cherubism mutation potentiates TNF-α–induced osteoclastogenesis via NFATc1.")
2. **Macrophage/inflammation arm (the engine):** Mutant myeloid cells over-respond to **M-CSF and RANKL**, with elevated **ERK1/2** and **Syk (pTyr346)** signaling via an autocrine feedback loop, driving **excess TNF-α** production and systemic macrophage inflammation.

**Convergence & the self-amplifying loop:** Hyperactive macrophages pump out **TNF-α**, which drives systemic inflammation, stimulates stromal cells to secrete **RANKL and M-CSF**, and feeds back to generate still more hyperactive osteoclasts → **jaw bone resorption replaced by fibrous, giant-cell-rich tissue**. Osteoblasts are also perturbed (excess immature osteoblasts, ~20% fewer mature ones, **reduced osteoprotegerin/OPG** → higher RANKL:OPG ratio further favoring resorption; PMID:20691350).

**Genetic dissection of the causal chain (mouse epistasis):**
- Cross onto **TNF-α–null** → infiltrative lesions disappear, bone phenotype partially rescued → **TNF-α is necessary** for the inflammatory/infiltrative disease.
- Cross onto **M-CSF–deficient (op/op)** → bone loss and infiltrates essentially gone (TNF-α still high) → **M-CSF needed for the osteolytic output**.
- Cross onto **NFATc1 conditional KO** → skeletal phenotype **fully rescued** despite persistent high TNF-α → **NFATc1 is the essential bone-resorption node**, while TNF-α inflammation runs through a parallel, NFATc1-independent path.

**Framing:** The Reichenberger/Ueki review concludes cherubism is best understood as **"a systemic autoinflammatory response to physiologic challenges despite the localized appearance of bone resorption"** — a myeloid-cell disorder that happens to manifest in the jaws. ([Orphanet J Rare Dis 2012;7(Suppl 1):S5, PMC3359958](https://pmc.ncbi.nlm.nih.gov/articles/PMC3359958/))

**Why the jaws, and why self-limiting?** Best current explanation: the tooth-bearing jaws face the greatest eruption/microbial/mechanical challenge in childhood; once dentition is complete and the pubertal hormonal/immune milieu shifts, the driving stimulus wanes and lesions ossify and regress.

**Suggested ontology terms:**
- Biological processes (GO): **GO:0030316 (osteoclast differentiation)**, **GO:0045672 (positive regulation of osteoclast differentiation)**, **GO:0045453 (bone resorption)**, **GO:0032760 (positive regulation of TNF production)**, **GO:0042116 (macrophage activation)**, **GO:0033173 (calcineurin-NFAT signaling cascade)**, **GO:0070371 (ERK1/ERK2 cascade)**, **GO:0006471 (protein ADP-ribosylation)**, **GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process)**, **GO:0038095/RANK signaling**.
- Cell types (CL): **CL:0000092 (osteoclast)**, **CL:0000235 (macrophage)**, **CL:0000576 (monocyte)**, **CL:0000062 (osteoblast)**, multinucleated giant cell.
- Molecular players/chemicals: TNF-α, M-CSF (CSF1), RANKL (TNFSF11), NFATc1, SYK, poly-ADP-ribose.

Sources: [Levaot 2011 PMID:22153076](https://pubmed.ncbi.nlm.nih.gov/22153076/), [Ueki 2007 PMID:17218256](https://pubmed.ncbi.nlm.nih.gov/17218256/), [Mukai 2014 JBMR](https://onlinelibrary.wiley.com/doi/full/10.1002/jbmr.2295), [pathophysiology review PMC3359958](https://pmc.ncbi.nlm.nih.gov/articles/PMC3359958/)

---

## 7. Anatomical Structures Affected

**Organ / structure level (primary):**
- **Mandible** — UBERON:0001684; especially the **angle and ramus**; symphysis and body variably; **condyles typically spared**.
- **Maxilla** — UBERON:0002397; involvement drives orbital-floor/infraorbital-rim disease.
- **Jaw region overall** — UBERON:0003278 (jaw region) / UBERON:0001710 (lower jaw region).

**Secondary involvement:**
- **Bony orbit / orbital floor** (UBERON:0006800) → globe displacement, proptosis, "eyes to heaven."
- **Teeth / dentition** (UBERON:0001091) → displacement, agenesis, malocclusion.
- **Cervical & submandibular lymph nodes** (UBERON:0002429) → reactive lymphadenopathy.
- **Upper airway** → obstruction/OSA in severe maxillary/mandibular expansion.
- Rare extragnathic reports exist (e.g., ribs) but classic cherubism is **jaw-restricted** — a key diagnostic feature.

**Body systems:** skeletal (craniofacial), plus **innate immune/myeloid system** as the mechanistic driver; secondarily ophthalmic, respiratory, and dental systems.

**Tissue / cell level:** normal jaw bone tissue (UBERON:0002481) is replaced by **fibrous connective tissue stroma rich in multinucleated giant cells (osteoclast-like)** and spindle-shaped mesenchymal stromal cells. Target/effector cells: **osteoclasts (CL:0000092)** and **macrophages (CL:0000235)**.

**Subcellular / molecular compartment:** the pathology localizes to **cytoplasmic protein-degradation machinery** — SH3BP2 accumulates in the cytoplasm because it escapes the **proteasome** (GO:0000502) after failing tankyrase-directed ADP-ribosylation/RNF146 ubiquitylation. Downstream signaling touches the plasma membrane (RANK/M-CSFR) and nucleus (NFATc1 translocation).

**Localization / lateralization:** **bilateral and symmetric** — this bilaterality is the classic feature distinguishing cherubism from the usually **unilateral/solitary** central giant cell granuloma.

---

## 8. Temporal Development

- **Onset:** early childhood, typically **age 2–5 yr** (some series note emergence in the 2nd year); **insidious**, painless progressive swelling.
- **Progression / stages:**
  - **Active/proliferative phase** (early childhood → puberty): lesions grow, bone resorbs, swelling increases.
  - **Stabilization** (adolescence): growth arrests.
  - **Involution/regression** (2nd–3rd decade): lesions ossify, remodel, facial contour normalizes. GeneReviews: "By age 30 years, the facial abnormalities… are usually less obvious than during childhood."
- **Course pattern:** characteristically **progressive-then-spontaneously-regressive** — one of the few bone diseases that reliably self-corrects. Severity is graded (e.g., Raposo-Amaral/Motohashi/Seward grading systems, I–III, by anatomic extent).
- **Duration:** effectively a **time-limited disease of childhood/adolescence**, though residual bone deformity or dental sequelae can persist into adulthood.
- **Remission:** predominantly **spontaneous** with skeletal maturity; treatment-induced stabilization reported for aggressive cases.
- **Critical window for intervention:** the active phase — the rationale for deferring elective reconstructive surgery until after regression (to avoid provoking regrowth), while reserving early intervention for airway/vision-threatening disease.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** unknown/very rare; Orphanet class **<1 in 1,000,000**. ~**300–600 cases** reported worldwide across ethnic groups; no strong ethnic predilection.
- **Incidence:** not established (too rare for reliable incidence figures).

**Inheritance (genetic):**
- **Autosomal dominant** (SH3BP2, ~80% of molecularly solved cases). Many simplex cases are **de novo**.
- **Autosomal recessive** (OGFRL1) in rare consanguineous families.
- **Penetrance:** high; classically described as near-complete. Historically stated as "**complete by age 5**," though GeneReviews cautions it "has not been systematically studied"; some non-penetrant/very-mild carriers reported. One clinical–genetic series "found no evidence of non-penetrance."
- **Expressivity:** markedly **variable**, even within a family.
- **Sex effect:** older literature reported a male excess (~2:1), but this is now attributed to ascertainment; recent series report **females on average more severely affected than males** — an intriguing and clinically relevant reversal.
- **Genetic anticipation:** not a feature (not a repeat-expansion disorder).
- **Germline/gonadal mosaicism:** possible — reported basis for recurrence in apparently unaffected parents; relevant to counseling.
- **Founder effects / consanguinity:** no SH3BP2 founder mutations; **consanguinity** is central to the recessive OGFRL1 families.
- **Carrier frequency:** not defined (private mutations).

**Population demographics:** worldwide, pan-ethnic; onset in early childhood; no endemic geographic clustering. Recessive OGFRL1 form reported from consanguineous Middle Eastern/South Asian pedigrees.

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1137/), [Orphanet best clinical practice](https://link.springer.com/article/10.1186/1750-1172-7-S1-S6), [clinical & genetic analysis series (ResearchGate)](https://www.researchgate.net/publication/317850326_Clinical_and_genetic_analysis_of_patients_with_cherubism)

---

## 10. Diagnostics

**Diagnostic approach:** clinical + radiographic + (as needed) histologic pattern, confirmed by molecular testing.

**Clinical / imaging:**
- **Radiographs / CT (imaging is central):** **bilateral, symmetric, multilocular ("soap-bubble") radiolucencies**, expansile remodeling, cortical thinning, at mandibular angles/rami; often displaced/unerupted "floating" teeth. Condyles spared. Suggested modality terms (RadLex/DICOM): panoramic radiograph, CT maxillofacial.
- **CBCT/MRI:** delineate extent, airway, orbital involvement; MRI for soft-tissue characterization and follow-up.

**Laboratory / biomarkers:**
- **Serum calcium, phosphate, PTH are typically normal** (helps exclude hyperparathyroidism/brown tumors). **Alkaline phosphatase may be elevated** during active resorption. No validated circulating diagnostic biomarker; TNF-α elevation is mechanistically expected but not a clinical test.

**Biopsy / histopathology:**
- **Fibrous stroma with numerous multinucleated osteoclast-like giant cells**, hemorrhage, hemosiderin; **microscopically indistinguishable from central giant cell granuloma (CGCG)** — so histology alone cannot make the call; **bilaterality + genetics** distinguish it. ([PMID:6937832](https://pubmed.ncbi.nlm.nih.gov/6937832/)) Perivascular eosinophilic cuffing around vessels is a classically cited (if inconsistent) clue.

**Genetic testing:**
- **First-line: targeted SH3BP2 exon 9 sequencing** (single-gene), given the tight RSPPDG mutational hotspot. High yield for classic cases.
- **If negative:** broader SH3BP2 sequencing, then **exome/genome** (to catch OGFRL1 recessive form or novel loci) — especially with consanguinity or atypical/recessive pedigrees.
- Gene panels (bone dysplasia/giant-cell-lesion panels) where available; CMA/karyotype/FISH not indicated (no CNV mechanism); mtDNA/repeat testing N/A.

**Clinical criteria / differential diagnosis** — key mimics to exclude:
- **Central giant cell granuloma** (usually unilateral/solitary).
- **Fibrous dysplasia / McCune-Albright** (GNAS; ground-glass, often unilateral, extragnathic).
- **Hyperparathyroidism-jaw tumor syndrome** (CDC73/HRPT2; abnormal calcium/PTH), brown tumors of hyperparathyroidism.
- **Aneurysmal bone cyst, giant cell tumor, Noonan/RASopathy-associated giant-cell lesions**, and multiple giant cell lesion syndromes.

**Screening:** no population screening (too rare). **Cascade genetic testing** of at-risk relatives once a familial variant is known; prenatal/PGT available when the variant is identified.

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1137/), [JOMR clinicoradiographic review](https://www.ejomr.org/JOMR/archives/2010/2/e2/e2ht.htm)

---

## 11. Outcome / Prognosis

- **Survival / mortality:** **Excellent — cherubism is benign and non-lethal.** Normal life expectancy. Death is essentially never disease-attributable except vanishingly rare severe-airway scenarios.
- **Natural history:** the defining prognostic fact is **spontaneous regression after puberty**; most patients reach adulthood with substantial or complete cosmetic recovery.
- **Morbidity / disability:** driven by the active phase — facial disfigurement (psychosocial), dental/orthodontic problems, malocclusion, and in severe cases **vision compromise, airway obstruction/OSA, feeding/speech difficulty**. Long-term functional disability is uncommon with modern multidisciplinary care.
- **Complications:** OSA, orbital/visual compromise, tooth loss/agenesis, malocclusion, surgical morbidity or lesion regrowth if operated during the active phase, and rare rebound hypercalcemia after denosumab in children.
- **Recovery potential:** high — natural involution plus staged reconstruction after stabilization yields good outcomes in most.
- **Prognostic factors:** **age (regression expected with maturity)**, **anatomic grade/extent**, orbital/airway involvement, and possibly **sex** (females more severely affected in recent series). No molecular prognostic biomarker in clinical use, though specific SH3BP2 genotype–severity correlations are debated and imperfect.

---

## 12. Treatment

**Overarching strategy:** Most cases need only **observation ("watchful waiting")** through the active phase, with **staged reconstruction after regression**. Aggressive/function-threatening disease (airway, vision, rapid growth) warrants active intervention. Multidisciplinary craniofacial-clinic management. Suggested MAXO anchors: **MAXO:0000950 (supportive care)**, **MAXO:0000004 (surgical procedure)**, **MAXO:0000011 (physical/rehab therapy — speech)**, **MAXO:0000079 (genetic counseling)**; observation/active-surveillance.

**Pharmacotherapy (all off-label, evidence = small case reports/series; a 2023 systematic review pooled ~18 patients across 14 mostly-single-case studies — [PMC10044089](https://pmc.ncbi.nlm.nih.gov/articles/PMC10044089/)):**
- **Denosumab** (anti-RANKL monoclonal antibody; blocks osteoclastogenesis) — increasingly reported, including **successful adult cherubism control with a 60 mg every-6-months regimen** ([JBMR Plus 2024/25, ziae164, PMC11742083](https://pmc.ncbi.nlm.nih.gov/articles/PMC11742083/)). **Caution: rebound hypercalcemia reported in a child after denosumab** — a real pediatric safety concern. Suggested therapeutic_agent: denosumab (NCIT drug-class monoclonal antibody).
- **Tacrolimus** (calcineurin inhibitor) — hits the **calcineurin–NFATc1** node directly; a 4-yr-old with aggressive disease improved over 1 yr, with reduced TRAP+ osteoclasts and reduced NFATc1 nuclear staining on biopsy ([PMID:25491283](https://pubmed.ncbi.nlm.nih.gov/25491283/)). CHEBI: tacrolimus.
- **Imatinib** (tyrosine kinase inhibitor; targets SYK/downstream signaling) — "paradigm shift" preliminary reports and pediatric case(s) with marked lesion reduction, well tolerated ([JOMS 2019](https://www.joms.org/article/S0278-2391(19)30233-2/fulltext)). CHEBI:45783 (imatinib).
- **TNF-α blockers (adalimumab, etanercept)** — mechanistically apt (TNF-α is the disease engine); anecdotal benefit.
- **Calcitonin** — trialed in ≥5 pediatric cases (6–30 mo), **mixed results** (some regression, some none).
- **Bisphosphonates** (e.g., pamidronate) — anti-resorptive; limited/variable evidence.

**Advanced therapeutics:** No gene/cell/RNA therapy in clinical use. Tankyrase-pathway biology suggests future rational targets, but tankyrase *inhibitors would worsen* disease (they stabilize SH3BP2) — so the therapeutic logic runs toward TNF-α/RANKL/NFATc1/SYK blockade, not tankyrase inhibition.

**Surgical / interventional:**
- **Curettage ± bone grafting, contouring/recontouring osteotomies, orthognathic reconstruction** — best timed **after lesion regression** to limit recurrence/regrowth. Emergency surgery for airway or orbital decompression when function is threatened. Suggested: **NCIT:C15329 (Surgical Procedure)** / curettage.

**Supportive / rehabilitative:** orthodontics for malocclusion/dental management; speech-language therapy; ENT/sleep management for OSA; ophthalmology for orbital disease; psychosocial support.

**Treatment outcomes:** No RCT-level efficacy data; response is variable and agent-dependent. Given reliable spontaneous regression, the bar for systemic therapy is **aggressive, function-threatening disease**.

Sources: [Pharmacological management systematic review (PMC10044089)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10044089/), [Denosumab adult case (PMC11742083)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11742083/), [Tacrolimus (PMID:25491283)](https://pubmed.ncbi.nlm.nih.gov/25491283/), [Imatinib (JOMS)](https://www.joms.org/article/S0278-2391(19)30233-2/fulltext)

---

## 13. Prevention

- **Primary prevention:** none possible (monogenic). The actionable lever is **avoiding disease-provoking insults during the active phase** — meticulous **oral hygiene/periodontal-inflammation control** (biologically supported by the microbe-dependence mouse data) and **avoiding elective jaw surgery/extractions during active proliferation**.
- **Secondary prevention (early detection):** **cascade genetic testing** of at-risk relatives once a familial SH3BP2 variant is known; early clinical/radiographic monitoring of known carriers to catch airway/orbital compromise early.
- **Tertiary prevention (limit complications):** structured **surveillance** — GeneReviews: clinical/radiographic assessment **annually during active growth, then every 2–3 years** after growth stops; **dental review every 6 months**; respiratory/ophthalmologic evaluation as needed. Manage OSA, protect vision, orthodontic maintenance.
- **Reproductive prevention / counseling:** **genetic counseling** for AD 50% transmission risk (and AR 25% for OGFRL1 families); **prenatal diagnosis / preimplantation genetic testing** available once the variant is known; discuss **gonadal mosaicism** and **de novo** possibilities.
- **Immunization / public health / environmental:** not applicable (non-infectious, non-environmental etiology).

Suggested MAXO: **MAXO:0000079 (genetic counseling)**, surveillance/active monitoring, **MAXO:0000950 (supportive care)**.

---

## 14. Other Species / Natural Disease

- **Taxonomy affected:** Human disease (**NCBITaxon:9606, *Homo sapiens***). No well-characterized naturally occurring cherubism in companion animals or wildlife is documented in the veterinary literature (OMIA has no established spontaneous cherubism entry as of this review — flag as "not available").
- **Orthologous genes:** *Sh3bp2* is conserved in mouse (**Sh3bp2**, human p.Pro418 ↔ mouse Pro416), rat, and other mammals; the **tankyrase–RNF146 degradation axis is evolutionarily conserved**. *Ogfrl1* orthologs exist across vertebrates.
- **Comparative biology:** the **P416R knock-in mouse is the workhorse model** and recapitulates the core myeloid/inflammatory bone-loss biology (see §15). Interesting cross-species caveat: **OGFRL1 knockout / frameshift mice did NOT reproduce human cherubism**, implying the OGFRL1 loss-of-function effect diverges between human and mouse — a genuine **human–model mismatch** worth flagging for any KB entry.
- **Zoonotic / cross-species transmission:** not applicable (genetic, non-transmissible).

Sources: [OGFRL1 study (PMC11062026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11062026/)

---

## 15. Model Organisms

**Flagship model — *Sh3bp2* P416R knock-in mouse** (Ueki et al., *Cell* 2007, PMID:17218256):
- **Type:** mammalian germline **knock-in** (point mutation orthologous to human p.Pro418Arg). Heterozygous and homozygous lines.
- **Phenotype recapitulation:** homozygous KI/KI mice show **trabecular bone loss/osteoporosis, increased osteoclast numbers, TNF-α–dependent systemic macrophage inflammation, and cortical erosion**; mutant myeloid cells hyper-respond to M-CSF/RANKL with elevated ERK/Syk and high TNF-α. Captures the **autoinflammatory myeloid mechanism** beautifully.
- **Genetic-dissection value (epistatic crosses):** onto **TNF-α–null** (lesions resolve), **op/op M-CSF-deficient** (bone loss abrogated), and **NFATc1 conditional KO** (skeletal phenotype fully rescued) — these crosses established the causal hierarchy (TNF-α drives inflammation; NFATc1 is the essential bone-resorption effector; M-CSF is required for osteolysis).
- **Limitations:** mice develop **systemic/generalized inflammatory bone disease rather than the jaw-restricted human lesions** — the striking human jaw-specificity and spontaneous pubertal regression are **not** faithfully reproduced, a key translational gap. Heterozygous mice are relatively mild unless challenged (e.g., oral microbial/periodontal challenge unmasks alveolar bone destruction — [PMC7285758](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7285758/)).

**Related models:**
- ***Sh3bp2* knockout mice** — used to show SH3BP2 is needed for optimal bone formation/osteoblast differentiation (PMID:20691350); loss-of-function ≠ cherubism (consistent with gain-of-function human mechanism).
- **Tankyrase-inhibitor / pathway models** — pharmacologic tankyrase inhibition induces SH3BP2 accumulation and bone loss, phenocopying the mechanism ([PMC6406327](https://ncbi.nlm.nih.gov/pmc/articles/PMC6406327)).
- ***Ogfrl1* KO and Syrian-frameshift knock-in mice** — generated for the recessive form but **did not recapitulate human cherubism** (human–model mismatch; [PMC11062026](https://pmc.ncbi.nlm.nih.gov/articles/PMC11062026/)).
- **In vitro / cellular:** patient-derived and mutant myeloid cultures, osteoclast differentiation assays (M-CSF/RANKL), macrophage TNF-α assays; human lesion tissue immunohistochemistry (TRAP, NFATc1).

**Applications:** dissecting the tankyrase→SH3BP2→SYK/ERK→TNF-α/NFATc1→osteoclast axis; testing anti-TNF, anti-RANKL (denosumab), calcineurin inhibition, and SYK/TKI strategies.

**Resources:** MGI (mouse *Sh3bp2*), IMPC/KOMP for allele availability.

---

## Consolidated Ontology Term Suggestions (for KB population)

| Domain | Suggested terms |
|---|---|
| **MONDO** | MONDO:0007038 (cherubism) — *verify* |
| **Genes (HGNC)** | SH3BP2 (`hgnc:` — verify ID, OMIM *602104), OGFRL1 (recessive) |
| **HPO** | HP:0000303 (mandibular prognathia), HP:0012802 (abnormal maxilla morphology), HP:0000520 (proptosis), HP:0000668 (hypodontia), HP:0000689 (dental malocclusion), HP:0002716 (lymphadenopathy), HP:0002870 (obstructive sleep apnea), HP:0000505 (visual impairment) |
| **GO (process)** | GO:0045453 (bone resorption), GO:0030316 / GO:0045672 (osteoclast differentiation +reg), GO:0032760 (+reg TNF production), GO:0042116 (macrophage activation), GO:0033173 (calcineurin-NFAT cascade), GO:0006471 (protein ADP-ribosylation), GO:0043161 (proteasomal ubiquitin-dependent catabolism) |
| **CL (cell types)** | CL:0000092 (osteoclast), CL:0000235 (macrophage), CL:0000576 (monocyte), CL:0000062 (osteoblast) |
| **UBERON** | UBERON:0001684 (mandible), UBERON:0002397 (maxilla), UBERON:0003278 (jaw region), UBERON:0006800 (bony orbit), UBERON:0001091 (tooth) |
| **CHEBI (drugs)** | imatinib (CHEBI:45783), tacrolimus (CHEBI: verify), + antibody agents denosumab/adalimumab via NCIT |
| **MAXO (treatments)** | MAXO:0000950 (supportive care), MAXO:0000004 (surgical procedure), MAXO:0000079 (genetic counseling), MAXO:0000011 (physical/speech therapy), observation/surveillance |

---

## Evidence Anchor Summary (verify PMIDs/quotes with `just fetch-reference` before curating)

| Claim | Reference | Confidence |
|---|---|---|
| SH3BP2 exon 9 RSPPDG mutations cause cherubism | Ueki et al., *Nat Genet* 2001 (PMID:11381256) | High |
| Gene maps to 4p16.3 | Mangion et al., *Am J Hum Genet* 1999 | High |
| P416R knock-in mouse; TNF-α/M-CSF/RANKL myeloid mechanism | Ueki et al., *Cell* 2007 (**PMID:17218256**) | High (URL-confirmed) |
| Sh3bp2 needed for osteoblast/bone formation | *(KO study)* **PMID:20691350** | High (URL-confirmed) |
| Loss of tankyrase-mediated 3BP2 destruction = pathogenic mechanism | Levaot et al., *Cell* 2011 (**PMID:22153076**) | High (URL-confirmed) |
| Tankyrase substrate-recognition rules | Guettler et al., *Cell* 2011 | High |
| Mutation potentiates TNF-α osteoclastogenesis via NFATc1 | Mukai et al., *JBMR* 2014 (doi:10.1002/jbmr.2295) | High |
| Pathophysiology review ("systemic autoinflammatory response") | Reichenberger/Ueki, *Orphanet J Rare Dis* 2012;7(S1):S5 (PMC3359958) | High |
| Best clinical practice / management | *Orphanet J Rare Dis* 2012;7(S1):S6 | High |
| OGFRL1 recessive cherubism; mouse mismatch | *JBMR Plus* 2024, ziae050 (PMC11062026) | High |
| Tacrolimus therapy, ↓NFATc1/TRAP | **PMID:25491283** | High (URL-confirmed) |
| Denosumab 60 mg q6mo adult success | *JBMR Plus* 2024/25, ziae164 (PMC11742083) | High |
| Pharmacological management systematic review | PMC10044089 (2023) | High |
| Microbe-dependent alveolar bone destruction in het mice | PMC7285758 | High |

---

**Bottom line, Harry:** cherubism is a gorgeous little natural experiment in *protein garbage collection gone wrong* — knock out the tankyrase tag on SH3BP2 and the cell can't take out the trash, so an adapter protein piles up, cranks the myeloid TNF-α/RANKL machinery, and the jaws pay the price until puberty flips the switch back off. When you build the KB entry, the two things I'd flag hardest: (1) it's **gain-of-function via escape-from-degradation**, not a broken enzyme, and (2) the mouse models capture the *mechanism* but **not the jaw-restriction or the self-regression**, and the OGFRL1 mice fail outright — real human-model-mismatch material worth a `HUMAN_MODEL_MISMATCH` discussion node. Every PMID above should still get run through `just fetch-reference` before it lands in evidence, since I pulled some from search metadata rather than reading each abstract line-by-line.

**Sources:** [OMIM 118400](https://omim.org/entry/118400) · [OMIM 602104 (SH3BP2)](https://omim.org/entry/602104) · [GeneReviews NBK1137](https://www.ncbi.nlm.nih.gov/books/NBK1137/) · [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=184) · [Pathophysiology review (PMC3359958)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3359958/) · [Ueki 2007 Cell (PMID:17218256)](https://pubmed.ncbi.nlm.nih.gov/17218256/) · [Levaot 2011 tankyrase (PMID:22153076)](https://pubmed.ncbi.nlm.nih.gov/22153076/) · [Mukai 2014 JBMR](https://onlinelibrary.wiley.com/doi/full/10.1002/jbmr.2295) · [OGFRL1 recessive (PMC11062026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11062026/) · [Best clinical practice (OJRD S6)](https://link.springer.com/article/10.1186/1750-1172-7-S1-S6) · [Pharmacological review (PMC10044089)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10044089/) · [Denosumab adult (PMC11742083)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11742083/) · [Tacrolimus (PMID:25491283)](https://pubmed.ncbi.nlm.nih.gov/25491283/) · [Imatinib (JOMS)](https://www.joms.org/article/S0278-2391(19)30233-2/fulltext) · [Microbe-dependent bone destruction (PMC7285758)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7285758/) · [Nature Genetics 2001](https://www.nature.com/articles/ng0601_125)