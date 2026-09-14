---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-16T10:01:50.639526'
end_time: '2026-08-16T10:15:45.723137'
duration_seconds: 835.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Light Chain Deposition Disease
  mondo_id: ''
  category: Acquired
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
  - claude-opus-5[1m]
  web_search_requests: 5
  num_turns: 47
  total_cost_usd: 5.9609865
  session_id: 90566b88-e32f-4a61-9820-7911086e3f83
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 28
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Light Chain Deposition Disease
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Light Chain Deposition Disease** covering all of the
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

# Light Chain Deposition Disease (LCDD) — Comprehensive Research Report

**Prepared:** 2026-08-16 · **Target KB entry:** `kb/disorders/Light_Chain_Deposition_Disease.yaml` · **MONDO:0019730** · **Category:** Acquired

> **How to read this.** Every numbered claim below is anchored to a PMID I actually pulled from PubMed during this session, and where I quote, the quote is verbatim from the abstract text I retrieved (exception flagged explicitly in §16). Ontology CURIEs marked ✅ were checked against this repo's validated term caches (`cache/*/terms.csv`) or a live OLS lookup; anything unverified is called out as such. Where the literature genuinely doesn't know something, I say so instead of filling the gap with vibes.

---

## 0. The one-paragraph version

Plasma cells are little protein factories, and normally the antibody light chains they churn out are disposable offcuts that the kidney filters and chews up without comment. In LCDD, one clone starts producing a light chain with a *structurally weird* variable domain — extra hydrophobic patches, sometimes a sugar stuck on, an unusually basic surface charge — and that molecule stops behaving like waste and starts behaving like mortar. It plasters itself in a fine, powdery, non-fibrillar layer along basement membranes, and where it touches mesangial cells in the glomerulus it doesn't just sit there: it *signals*, flipping those cells into a scar-making phenotype that pours out collagen IV, laminin, fibronectin and tenascin while simultaneously turning down the enzymes that would clear them. The result is nodular glomerulosclerosis and a kidney that silts up. It is emphatically **not** amyloid — Congo red stays stubbornly negative — and that distinction is the whole diagnostic hinge.

---

## 1. Disease Information

### 1.1 Definition

Light chain deposition disease is a systemic disorder in which a clonal plasma-cell or B-cell population secretes a monoclonal immunoglobulin light chain that deposits as **Congo red–negative, non-fibrillar, granular ("powdery") material along basement membranes**, most consequentially in the kidney. It sits inside the broader family of **monoclonal immunoglobulin deposition disease (MIDD)**, also called **Randall-type MIDD**, which comprises three variants by deposit composition:

| Variant | Deposit | Approximate share of MIDD |
|---|---|---|
| **LCDD** | light chain only | 212/255 (83%) — Joly (PMID:30578255); 51/64 (80%) — Nasr (PMID:22156754) |
| **HCDD** | heavy chain only | 23/255 (9%); 7/64 (11%) |
| **LHCDD** | both | 20/255 (8%); 6/64 (9%) |

> "Monoclonal immunoglobulin deposition disease (MIDD) is a rare complication of B-cell clonal disorders, defined by Congo red negative-deposits of monoclonal light chain (LCDD), heavy chain (HCDD), or both (LHCDD). MIDD is a systemic disorder with prominent renal involvement, but little attention has been paid to the description of extrarenal manifestations." — Joly et al., *Blood* 2019 (PMID:30578255)

The condition was first delineated by **Randall et al. in 1976** (PMID:814812), which is why "Randall-type" persists in the European literature:

> "Clinical and pathologic correlations suggest that the retention and tissue deposition of light chains produced the organ dysfunction, inasmuch as free kappa light chain determinants were demonstrated histologically in the clinically affected organs. The deposition in these patients may be an extreme example of a common but previously unrecognized form of plasma cell dyscrasia." — Randall et al., *Am J Med* 1976 (PMID:814812)

### 1.2 Identifiers (verified via OLS, MONDO:0019730 cross-references)

| Resource | ID | Notes |
|---|---|---|
| **MONDO** | `MONDO:0019730` ✅ | label: *light chain deposition disease* |
| **Orphanet** | `ORPHA:93558` | MONDO `equivalentTo` |
| **NCIT** | `NCIT:C7727` | MONDO `equivalentTo` |
| **UMLS** | `C0238239` | MONDO `equivalentTo` |
| **SNOMED CT** | `373604002` | MONDO `equivalentTo` |
| **MedGen** | `65953` | MONDO `equivalentTo` |
| **GARD** | `0006906` | |
| **ICD-11 (foundation)** | `1612001446` | inherited from Orphanet:93558 |
| **OMIM** | *none* | Correct — LCDD is an acquired somatic clonal disorder with no Mendelian entry |
| **ICD-10** | *no dedicated code* | Coded by context (underlying myeloma C90.0, MGUS D47.2, or a renal N-code). Do not invent one. |

**⚠️ MeSH indexing trap worth recording in the KB.** There is no dedicated MeSH descriptor for LCDD. PubMed's automatic term mapping expands "monoclonal immunoglobulin deposition disease" to **`"immunoglobulin light-chain amyloidosis"[MeSH Terms]`** — which is the *wrong disease*. Any literature-mining pipeline for this entry that leans on MeSH will silently pull AL amyloidosis papers. Search by free text and by the specific phrases instead.

### 1.3 Synonyms

**Accurate:** LCDD; light-chain deposition disease; Randall-type monoclonal immunoglobulin deposition disease (as the parent class); monoclonal light chain deposition disease; non-amyloid light chain deposition disease.

**⚠️ MONDO synonyms to NOT propagate as exact matches.** MONDO:0019730 carries `Bence Jones myeloma`, `Light chain disease` and `Light chain gammopathy` in its synonym list. These are historical, overbroad, and actively misleading — "light chain disease" in hematology usually means light-chain-only myeloma, a *different* entity. Flag these rather than curating them.

### 1.4 Data provenance character

Evidence for LCDD is almost entirely **aggregated, retrospective, biopsy-anchored cohort data** from a handful of referral centers (Mayo, Columbia, the French national amyloidosis/MIDD network in Poitiers–Limoges, UK National Amyloidosis Centre), supplemented by case reports and a small mechanistic literature (rat mesangial cell culture + one transgenic mouse). There is **no randomized trial in LCDD** and no population registry. Frequency figures throughout this report are therefore biopsy-series proportions, not population rates, and carry heavy referral bias.

---

## 2. Etiology

### 2.1 Primary cause

**A clonal plasma-cell (or, less often, lymphoplasmacytic/B-cell) proliferation secreting a nephrotoxic monoclonal free light chain.** The causal agent is the *protein*, not the tumor burden — which is why most LCDD patients have a clone far too small to qualify as symptomatic myeloma.

Hematologic substrate across the three largest series:

| Series | MGRS / small clone | Symptomatic multiple myeloma | Other |
|---|---|---|---|
| Joly 2019, n=255 (PMID:30578255) | **64%** | **34%** | — |
| Nasr 2012, n=64 (PMID:22156754) | — | **59%** (38/64) | dysproteinemia evident in 97% |
| Pozzi 2003, n=63 (PMID:14655186) | 32% "idiopathic" | **65%** | lymphoproliferative 3% |
| Cohen 2015, n=49 (PMID:26176826) | 38/49 MGRS | 10/49 MM | 1 Waldenström |

> "Hematological diagnosis was monoclonal gammopathy of renal significance in 64% and symptomatic myeloma in 34%." — Joly et al. (PMID:30578255)

This is the definitional core of **MGRS (monoclonal gammopathy of renal significance)**:

> "the IKMG redefines MGRS as a clonal proliferative disorder that produces a nephrotoxic monoclonal immunoglobulin and does not meet previously defined haematological criteria for treatment of a specific malignancy." — Leung et al., *Nat Rev Nephrol* 2019 (PMID:30510265)

Rare LCDD cases occur with **no demonstrable plasma cell disorder at all**:

> "LCDD typically arises secondary to an underlying plasma cell dyscrasia, such as monoclonal gammopathy of undetermined significance or multiple myeloma. However, rare cases can occur in the absence of a demonstrable plasma cell disorder." — Rai et al., *AJNR* 2025 (PMID:38914431)

### 2.2 The proximate molecular cause — a light chain with a bad variable domain

The pathogenicity is encoded in the **V domain**, and this is the single most mechanistically important fact in the entry. Three converging lines:

**(a) Biased V-gene usage — the VκIV / IGKV4-1 subgroup.**
> "These data together with our previously published results, indicate the pathogenic potential of the rare V kappa IV subgroup and confirm the absence of detectable serum and urine free monoclonal light chains when they are N-glycosylated." — Denoroy, Déret & Aucouturier, *Immunol Lett* 1994 (PMID:7829131)

Note the second half of that sentence — **N-glycosylated pathogenic light chains can be invisible on standard serum/urine assays.** That is a diagnostic landmine.

**(b) Somatic hypermutation planting hydrophobic and glycosylation-site residues.**
> "Four unique amino acid substitutions were found at positions -8, -3, -2 and -1 in the leader sequence and probably resulted in an unusual cleavage by signal peptidase, thus making the LC truncated by one residue and accounting for its unique hydrophobic N-terminus: Ile-Ile-Leu. Additional peculiarities were observed in the V region, including a Thr74-->Asn substitution creating a N-glycosylation site, and Thr53-->Ile, which was only reported once among human kappa III chains, in another LCDD case, and may be of special significance at a position usually harbouring a polar amino acid." — Decourt, Cogné & Rocca, *Clin Exp Immunol* 1996 (PMID:8918585)

**(c) Surface charge — the CDRs run basic.**
> "Sequencing of 18 pathogenic LC showed high isoelectric point values of variable domain complementarity determining regions, possibly accounting for tissue deposition." — Joly et al. (PMID:30578255)

A basic (positively charged) CDR surface plus a polyanionic basement membrane is chemistry doing exactly what you'd expect — the light chain sticks where the charge complements it. That's the tidiest structure-to-lesion story in the whole disease.

**(d) The V domain is sufficient.** In the transgenic mouse (below), only the human V domain was transplanted:
> "The variable domain of the LC bears alone the structural properties involved in its pathogenicity." — Bender et al., *Blood* 2020 (PMID:32559766)

### 2.3 Risk factors

**Genetic (germline):** No germline susceptibility locus is established for LCDD specifically. Familial clustering has not been demonstrated. Inherited risk, if any, is presumed to be that of the upstream plasma cell dyscrasia (MGUS/MM heritability), not of the deposition phenotype. **Do not curate germline causal genes for this entry.**

**Somatic:** The relevant "genetics" is entirely somatic and clone-restricted — the rearranged, hypermutated **IGKV** gene of the pathogenic clone (see §4).

**Demographic / clinical:**
- **Age** — median 56 y (Nasr PMID:22156754; Sayed PMID:26392598); mean 58 ± 14.2 y (Pozzi PMID:14655186). Notably younger than AL amyloidosis or cast nephropathy: *"Patients with MIDD generally present at a younger age than those with light chain amyloidosis or light chain cast nephropathy."* (PMID:22156754). 36% of Nasr's cohort were ≤50 years.
- **Male sex** — 63.5% male (Pozzi PMID:14655186).
- **Pre-existing MGUS or multiple myeloma** — the dominant clinical risk state.
- **Age itself as a renal/patient risk multiplier** — Pozzi: age RR 1.05 (95% CI 1.009–1.086) for renal outcome; RR 1.06 (1.03–1.1) for survival.

**Environmental / occupational / infectious:** **None established for LCDD.** The general MM/MGUS risk-factor literature (age, male sex, African ancestry, obesity, ionizing radiation, some pesticide exposures) applies only upstream and has never been shown to select for the *depositing* phenotype. Record as a knowledge gap rather than importing myeloma risk factors wholesale.

### 2.4 Protective factors

None identified. There are no protective germline variants, dietary factors, or exposures reported for LCDD. The only genuinely "protective" intervention is **achieving a deep hematologic response** (§12) — which is treatment, not prevention.

### 2.5 Gene–environment interactions

**No data.** Nothing in CTD, PheGenI, or the primary literature addresses GxE in LCDD. This is an honest blank.

---

## 3. Phenotypes

### 3.1 Renal (essentially universal — the kidney is always involved)

| Phenotype | Suggested HP term | Frequency / evidence |
|---|---|---|
| Renal insufficiency | `HP:0000083` Renal insufficiency ✅ | **96%** at presentation (acute 52%, chronic 44%) — Pozzi (PMID:14655186) |
| Proteinuria | `HP:0000093` Proteinuria ✅ | **84%** with >1 g/day — Pozzi (PMID:14655186) |
| Nephrotic-range proteinuria | `HP:0012593` Nephrotic range proteinuria ✅ | frequent; "nephrotic proteinuria" in pure MIDD — Lin (PMID:11423577) |
| Nephrotic syndrome | `HP:0000100` Nephrotic syndrome ✅ | characteristic of the glomerular (nodular) form — Bender (PMID:32559766) |
| Elevated serum creatinine | `HP:0003259` Elevated circulating creatinine concentration ✅ | mean serum Cr **4.2 mg/dL** in pure MIDD; **7.8 mg/dL** in LCDD+cast nephropathy (P=0.01) — Lin (PMID:11423577) |
| Hypertension | `HP:0000822` Hypertension ✅ | listed as a presenting feature — Nasr (PMID:22156754) |
| Hematuria | `HP:0000790` Hematuria ✅ / `HP:0002907` Microscopic hematuria ✅ | listed as a presenting feature — Nasr (PMID:22156754) |
| Acute kidney injury | `HP:0001919` Acute kidney injury ✅ | the presentation when cast nephropathy coexists — Joly (PMID:30578255) |
| Chronic kidney disease | `HP:0012622` Chronic kidney disease ✅ | dominant course |
| End-stage kidney disease | `HP:0003774` Stage 5 chronic kidney disease ✅ | **39%** progressed to ESRD (Nasr PMID:22156754); **62%** required dialysis (Sayed PMID:26392598) |
| Bence Jones proteinuria | `HP:0030156` Bence Jones Proteinuria ✅ | context-dependent; **absent when the LC is N-glycosylated** (PMID:7829131) |
| Hypoalbuminemia / edema | `HP:0003073` ✅ / `HP:0000969` Edema ✅ | secondary to nephrotic syndrome |

> "Renal presentation was acute kidney injury in patients with LCCD and CN, and chronic glomerular disease in the other types" — Joly et al. (PMID:30578255)

**⚠️ Two ontology cautions for the curator:**
1. **There is no HPO term for "nodular glomerulosclerosis."** I checked HPO via OLS; the nearest hits are `HP:0033271` (Glomerular capillary microaneurysm) and `HP:0000097` (Focal segmental glomerulosclerosis) — neither means the right thing. Curate nodular mesangial sclerosis as a **histopathology finding**, not a forced HP annotation. *No term beats a bad one.*
2. **Never use `HP:0001917` Renal amyloidosis** on this entry. It exists in the cache and it is exactly the wrong claim — LCDD deposits are Congo-red-negative and non-fibrillar. This is the single highest-risk mis-annotation for LCDD.

### 3.2 Extrarenal — more common than the older literature suggested

The Joly nationwide cohort is the corrective here:

> "35% of whom had symptomatic extrarenal (mostly hepatic and cardiac) involvement." … "This study highlights an unexpected frequency of extrarenal manifestations in MIDD." — Joly et al. (PMID:30578255)

| Organ | Manifestations | Suggested HP term | Evidence |
|---|---|---|---|
| **Liver** | hepatomegaly, transaminase elevation, portal hypertension, fulminant hepatic failure; deposits in **hepatic sinusoids** | `HP:0002240` Hepatomegaly ✅, `HP:0001409` Portal hypertension ✅, `HP:0001399` Hepatic failure ✅ | Joly PMID:30578255; Cassano 2024 PMID:39196376 |
| **Heart** | diastolic dysfunction, conduction disturbance, arrhythmia, rarely an atrial mass; restrictive physiology | `HP:0011675` Arrhythmia ✅, `HP:0001635` Congestive heart failure ✅, `HP:0001723` Restrictive cardiomyopathy ✅ | Joly PMID:30578255; Cassano PMID:39196376 |
| **CNS** | intracerebral LCDD — mass-like or infiltrative lesions; **choroid plexus** deposits; a documented radiographic mimic of neoplasm | (no good HP term; curate as anatomic/imaging finding) | Rai et al. PMID:38914431 |
| **Lung** | usually an incidental finding; symptomatic pulmonary LCDD (cystic/nodular disease) rare | | Rai PMID:38914431; Cassano PMID:39196376 |
| **Peripheral nerve** | reported but uncommon | `HP:0009830` Peripheral neuropathy ✅ | Randall PMID:814812 (neurologic abnormalities in both index cases) |
| **GI / endocrine** | described in the original 1976 report | | Randall PMID:814812 |

**Prognostic weight of extrarenal disease:** independently worsens *patient* (not renal) survival — RR 2.24 (95% CI 1.15–4.35) (Pozzi PMID:14655186).

### 3.3 Onset, severity, progression

- **Onset:** adult, insidious. Median 56–58 y; 36% ≤50 y (PMID:22156754).
- **Diagnostic delay is the rule.** *"The interval between albuminuria or elevation in creatinine and MIDD diagnosis was 12 months suggesting a delay in diagnosis."* — Kourelis et al. (PMID:27501122). And in Lin's series, *"Renal biopsy diagnosis preceded clinical evidence of dysproteinemia in 68% of all cases"* (PMID:11423577) — i.e., the kidney biopsy usually finds the clone, not the other way round.
- **Severity:** moderate to severe; 69% of Kourelis' cohort had GFR <30 mL/min/1.73 m², 18% already on renal replacement therapy at diagnosis (PMID:27501122).
- **Progression:** progressive, and the rate is *modifiable by treatment* — see the strikingly symmetric GFR slopes in §11.
- **Course pattern:** chronic progressive; not relapsing-remitting, though clonal relapse can drive renal relapse.

### 3.4 Quality of life

**No LCDD-specific QoL instrument data exists** (no EQ-5D/SF-36/PROMIS study identified). Impact must be inferred from the dominant clinical burden: dialysis dependence in a majority (62%, PMID:26392598), nephrotic edema, and — for the myeloma-associated subset — the QoL profile of plasma cell dyscrasia and its therapy. Record this as a knowledge gap.

---

## 4. Genetic / Molecular Information

**This is a somatic, clone-restricted molecular disease. There is no germline causal gene, no inheritance pattern, no carrier frequency, no penetrance.** Curating it as a genetic disease would be a category error.

### 4.1 The relevant "gene" is the clone's rearranged immunoglobulin light chain locus

- **IGK locus (chromosome 2p11.2)** — kappa light chains dominate. κ:λ = **68:32** (Pozzi PMID:14655186); **11 κ : 1 λ** among pure LCDD in Lin's series (PMID:11423577).
- **IGKV4-1 (VκIV subgroup)** — over-represented relative to its rarity in the normal repertoire (PMID:7829131). Suggested gene descriptor: HGNC symbol `IGKV4-1` (lowercase `hgnc:` prefix per repo convention; **CURIE not verified in this session — look it up before curating**).
- **IGKV3 (VκIII)** — also documented in LCDD with structural peculiarities (PMID:8918585).
- **IGL locus** — the minority λ cases; no subgroup bias established.
- **IGH CH1 deletion** — the defining lesion of *HCDD*, the sibling entity: *"Cases of HCDD were associated with a CH1 deletion"* (Lin, PMID:11423577). Mechanistically elegant: without CH1, the heavy chain escapes BiP-mediated ER retention and gets secreted without a partner light chain. Relevant as a differential/sibling, not for the LCDD entry itself.

### 4.2 Variant classification

ACMG/AMP classification **does not apply** — these are somatic hypermutations in a rearranged immunoglobulin V gene, evaluated by structural/biophysical consequence, not by pathogenicity tier. Population allele frequencies (gnomAD etc.) are meaningless here; the IG loci are somatically rearranged and hypermutated by design.

**Variant types documented in pathogenic LCDD light chains:**
| Type | Consequence | Evidence |
|---|---|---|
| Missense in CDR/FR (polar → hydrophobic) | exposes hydrophobic surface, promotes aggregation/tissue binding | PMID:8918585; PMID:39196376 |
| Missense creating N-glycosylation sequon (e.g. Thr74→Asn) | adds N-glycan; **renders FLC undetectable in serum/urine assays** | PMID:8918585; PMID:7829131 |
| Leader-sequence substitutions | aberrant signal peptidase cleavage → truncated LC with hydrophobic N-terminus (Ile-Ile-Leu) | PMID:8918585 |
| Cumulative basic-residue substitutions in CDRs | high CDR isoelectric point → charge-driven basement membrane binding | PMID:30578255 |
| Small truncations | altered folding/deposition | PMID:39196376 |

**Functional consequence class:** this is a **gain of pathological function** at the protein level (the chain acquires a tissue-binding, cell-signaling activity it should not have). In dismech's schema this belongs on the **light-chain descriptor as a `modifier: GAIN_OF_FUNCTION`-style activity claim on the process node** rather than on a `GeneticContext.functional_impact_category` — there is no germline variant to hang a `GeneticContext` on. Be careful here; the two slots are not interchangeable (see CLAUDE.md "Gain/Loss of Function: which slot?").

### 4.3 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none identified.
- **Epigenetics:** no DNA methylation or chromatin study specific to LCDD identified. Blank.
- **Clonal cytogenetics:** the underlying plasma cell clone can carry standard myeloma cytogenetics; FISH is recommended by the IKMG for clonal characterization (*"Additional genetic tests and fluorescent in situ hybridization studies are helpful for clonal identification and for generating treatment recommendations."* — PMID:30510265). No LCDD-specific cytogenetic signature (e.g. a t(11;14) enrichment analogous to AL amyloidosis) was confirmed in the sources I retrieved — treat as an open question, not as absence.

---

## 5. Environmental Information

- **Environmental factors:** none established.
- **Lifestyle factors:** none established.
- **Infectious agents:** none causal. One interesting confound from Lin's HCDD subgroup: *"frequently had hypocomplementemia and a positive hepatitis C virus antibody but negative hepatitis C virus PCR"* (PMID:11423577) — that is an HCDD observation, serology-positive/PCR-negative, and should **not** be imported into LCDD as an infectious trigger.

This section is genuinely empty for LCDD, and saying so is more useful than manufacturing plausible-sounding exposures.

---

## 6. Mechanism / Pathophysiology

Here is the causal chain, upstream → downstream, in the form the dismech pathograph wants.

### Node 1 — Clonal plasma cell expansion and excess free light chain secretion
**Scale:** CELLULAR · **Cell type:** `CL:0000786` plasma cell ✅ · **Site:** `UBERON:0002371` bone marrow ✅ · **Process:** `GO:0002377` immunoglobulin production ✅ (modifier: INCREASED)

A small clone — usually below the myeloma treatment threshold — secretes free light chains at high concentration. In the mouse model this had to be engineered deliberately: *"High free LC levels were achieved after backcrossing with mice presenting increased PC differentiation and no immunoglobulin heavy chain production."* (PMID:32559766)

### Node 2 — Structurally abnormal light chain variable domain
**Scale:** MOLECULAR

The V domain carries hydrophobic CDR substitutions, sometimes an N-glycan, and a high isoelectric point (PMID:30578255; PMID:8918585; PMID:7829131). This node is the disease's *actual* etiologic agent, and it is sufficient on its own: *"The variable domain of the LC bears alone the structural properties involved in its pathogenicity."* (PMID:32559766)

### Node 2b (parallel branch) — Plasma-cell endoplasmic reticulum stress
**Scale:** CELLULAR · **Process:** `GO:0034976` response to endoplasmic reticulum stress ✅, `GO:0030968` endoplasmic reticulum unfolded protein response ✅

> "RNA sequencing conducted on PCs demonstrated that LCDD LC induces endoplasmic reticulum stress, likely accounting for the high efficiency of proteasome inhibitor-based therapy." — Bender et al. (PMID:32559766)

This is the mechanistic *why* behind bortezomib working so well, and it deserves its own node with an `INHIBITS` treatment edge from the proteasome inhibitor (`GO:0043161` proteasome-mediated ubiquitin-dependent protein catabolic process ✅). The clone has effectively backed itself into a corner: it makes a protein so awkward to fold that its own quality-control machinery is running flat out, and a proteasome inhibitor tips it over.

### Node 3 — Non-fibrillar deposition along basement membranes
**Scale:** TISSUE · **Sites:** `UBERON:0005777` glomerular basement membrane ✅, `UBERON:0009773` renal tubule ✅ (tubular BM), `UBERON:0000074` renal glomerulus ✅

Linear/granular, Congo-red-negative, "powdery" on electron microscopy. The charge-complementarity story from Joly (high-pI CDRs vs. polyanionic BM) is the best current explanation.

### Node 4 — Mesangial cell surface engagement and phenotype transformation
**Scale:** CELLULAR · **Cell types:** `CL:0000650` mesangial cell ✅ → `CL:0000186` myofibroblast cell ✅ · **Processes:** `GO:0043123` positive regulation of canonical NF-kappaB signal transduction ✅, `GO:0048008` platelet-derived growth factor receptor signaling pathway ✅

**The critical mechanistic discriminator between LCDD and AL amyloidosis lives here**, and it is beautiful:

> "Monoclonal light chains associated with AL-Am but not those producing LCDD are avidly endocytosed by mesangial cells and delivered to the mature lysosomal compartment where amyloid fibrils are formed. Light chains from patients with LCDD exert their pathogenic signaling effect at the cell surface of mesangial cells." — Herrera et al., *Kidney Int Rep* 2020 (PMID:33163710)

Same cell, same class of ligand, two completely different intracellular itineraries — one goes *inside* to the lysosome and comes out as fibrils, the other never crosses the membrane and instead shouts at a receptor. AL hollows the mesangium out; LCDD makes it build.

> "The interaction with the pathogenic light chain elicits specific cellular processes, which include apoptosis, phenotype transformation, and secretion of extracellular matrix components and metalloproteinases." — Herrera et al. (PMID:33163710)

### Node 5 — TGF-β–driven extracellular matrix overproduction
**Scale:** CELLULAR/TISSUE · **Processes:** `GO:0007179` transforming growth factor beta receptor signaling pathway ✅ (modifier: INCREASED), `GO:0030198` extracellular matrix organization ✅, `GO:0085029` extracellular matrix assembly ✅

The landmark in-vitro demonstration:

> "These proteins inhibited mesangial cell proliferation and increased production of matrix proteins, including type IV collagen, laminin, and fibronectin. By immunocytochemistry and bioassay, transforming growth factor-beta (TGF-beta) production and activity increased when mesangial cells were exposed to these proteins. Furthermore, anti-TGF-beta antibody abolished the inhibition of cell proliferation and the increase of extracellular matrix protein production caused by these light chains." — Zhu, Herrera, Murphy-Ullrich, Huang & Sanders, *Am J Pathol* 1995 (PMID:7639331)

That anti-TGF-β rescue is the causal proof, not just a correlation — block the cytokine and the phenotype goes away.

And the specificity control matters: *"These findings were not observed in mesangial cells exposed to human albumin and two other light chains previously characterized to be tubulopathic."* (PMID:7639331) — i.e., **glomerulopathic and tubulopathic light chains are different populations**, which is exactly why one patient gets LCDD and another with a similar clone gets Fanconi syndrome or cast nephropathy.

### Node 6 — Failure of matrix degradation (the other half of the imbalance)
**Scale:** CELLULAR · **Process:** `GO:0022617` extracellular matrix disassembly ✅ (modifier: DECREASED)

> "When mesangial cells are incubated with LCDD-LCs, production of ECM proteins (collagen IV, laminin, fibronectin, and tenascin) is increased, with maximum effect at 72 hours post LC treatment. A concomitant decrease in collagenase IV activity further accentuates the accumulation of mesangial matrix. These effects are mediated through transforming growth factor-beta (TGF-beta) activation." — Herrera et al., *Ultrastruct Pathol* 1999 (PMID:10369104)

Same paper gives the mirror-image AL contrast: *"In contrast, when mesangial cells are incubated with Am-LCs, a decrease in ECM protein production and a stimulatory effect on collagenase IV is observed, which results in matrix degradation and facilitates amyloid deposition."*

The MMP-7 / tenascin-C axis is the more recently emphasized version of this: light chains suppress mesangial MMP-7 release, tenascin-C goes undegraded, matrix piles up (Cassano et al. 2024, PMID:39196376 — see §16 provenance caveat).

So the mesangium is caught in a two-sided vice: the faucet is opened and the drain is plugged. Neither alone would silt the glomerulus this fast.

### Node 7 — Nodular glomerulosclerosis
**Scale:** TISSUE · **Site:** `UBERON:0000074` renal glomerulus ✅

Nodular mesangial sclerosis in **61%** (39/64) of Nasr's MIDD cohort (PMID:22156754); **100%** of pure MIDD vs **18%** of LCDD-with-cast-nephropathy in Lin's series (P<0.0001) (PMID:11423577). κ deposition was more often associated with nodular sclerosing glomerulopathy than λ (PMID:14655186).

### Node 8 — Proteinuria, GFR decline, kidney failure
**Scale:** ORGANISM

> "Our mouse model recapitulates the characteristic features of LCDD, including progressive glomerulosclerosis, nephrotic-range proteinuria, and finally kidney failure." — Bender et al. (PMID:32559766)

### Node 9 (parallel) — Extrarenal deposition and organ dysfunction
Liver sinusoids, myocardium, choroid plexus, lung (§3.2).

### 6.1 What the mouse transcriptome says about *sequence* of events

> "Finally, transcriptome analysis of presclerotic glomeruli revealed that proliferation and extracellular matrix remodeling represented the first steps of glomerulosclerosis, paving the way for future therapeutic strategies in LCDD and other kidney diseases featuring diffuse glomerulosclerosis, particularly diabetic nephropathy." — Bender et al. (PMID:32559766)

Worth flagging: the mouse's *presclerotic* glomeruli show **proliferation** first, whereas the classic in-vitro data show light chains **inhibiting** mesangial proliferation (PMID:7639331). That is a genuine tension between the in-vitro and in-vivo models — an excellent candidate for a `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH` discussion in the entry rather than a paper-over.

### 6.2 Reversibility — the deposits are not permanent

> "Accordingly, reduction of circulating pathogenic LC was efficiently achieved and not only preserved renal function but also partially reversed kidney lesions." — Bender et al. (PMID:32559766)

This is mechanistically load-bearing: turn off the tap and the sink partially drains. It reframes LCDD as a **dynamic equilibrium**, not a one-way accretion, and justifies aggressive clone-directed therapy even in advanced renal disease.

### 6.3 Not covered by the literature

Metabolomics, lipidomics, single-cell/spatial transcriptomics, proteomics beyond mass-spec typing of deposits, and CRISPR/RNAi functional screens: **no LCDD-specific studies identified.** The Bender bulk RNA-seq (PMID:32559766) is the only omics dataset of consequence. Record the rest as gaps.

---

## 7. Anatomical Structures Affected

### Organ level
| Structure | UBERON | Role |
|---|---|---|
| Kidney | `UBERON:0002113` ✅ | **Primary — always involved** |
| Liver | `UBERON:0002107` ✅ | Secondary; most common extrarenal site (with heart) |
| Heart / myocardium | `UBERON:0000948` ✅ / `UBERON:0002349` ✅ | Secondary |
| Choroid plexus | `UBERON:0001886` ✅ | CNS deposition site |
| Lung | `UBERON:0002048` ✅ | Usually incidental |
| Peripheral nervous system | `UBERON:0000010` ✅ | Uncommon |
| Bone marrow | `UBERON:0002371` ✅ | Source compartment (the clone) |

**Body systems:** urinary/renal (primary); hepatobiliary, cardiovascular, nervous, respiratory (secondary); hematologic/immune (source).

### Tissue and cell level
| Structure | Term | Note |
|---|---|---|
| Glomerular basement membrane | `UBERON:0005777` ✅ | primary deposition surface |
| Renal tubule (tubular BM) | `UBERON:0009773` ✅ | linear LC staining along TBM is a classic IF finding |
| Renal glomerulus / mesangium | `UBERON:0000074` ✅ | site of nodular sclerosis |
| Mesangial cell | `CL:0000650` ✅ | **the effector cell** |
| Myofibroblast | `CL:0000186` ✅ | the transformed mesangial phenotype |
| Plasma cell | `CL:0000786` ✅ | source cell |
| Podocyte | `CL:0000653` ✅ | secondarily injured (proteinuria) — mechanistically less studied |
| Proximal tubule epithelial cell | `CL:1000838` ✅ | relevant to the *differential* (tubulopathic LC → Fanconi), not core LCDD |

### Subcellular level (GO Cellular Component — **not verified against cache; look up before curating**)
- Basement membrane (extracellular matrix compartment) — the deposition site
- Endoplasmic reticulum — plasma-cell stress compartment (PMID:32559766)
- Lysosome — notable by its *absence* in LCDD; it is the AL-amyloidosis route (PMID:33163710)

### Localization
Bilateral and diffuse in the kidney. Systemic/multi-organ. Not lateralized.

---

## 8. Temporal Development

**Onset:** adult; median 56 y (PMID:22156754; PMID:26392598), mean 58 y (PMID:14655186). Insidious in the glomerular form; abrupt (AKI) when light chain cast nephropathy coexists (PMID:30578255).

**Stages (no formal staging system exists — this is a descriptive synthesis):**
1. *Occult* — nephrotoxic monoclonal LC circulating; MGUS-level clone; no renal signal.
2. *Early renal* — albuminuria/proteinuria and a creatinine drift. Median ~12 months elapse here before diagnosis (PMID:27501122).
3. *Established* — nodular glomerulosclerosis, nephrotic-range proteinuria, GFR <30 in ~69% at diagnosis (PMID:27501122).
4. *End-stage* — dialysis dependence in 39–62% (PMID:22156754; PMID:26392598).
5. *Extrarenal/systemic* — hepatic and cardiac deposition; drives mortality independent of renal course (PMID:14655186).

**Progression rate — and its treatment dependence.** The Sayed dichotomy is the most useful single number pair in the disease:

> "with a mean improvement in glomerular filtration rate (GFR) of 6.1 mL/min/year among those achieving a complete or very good partial hematologic response (VGPR) with chemotherapy, most of whom remained dialysis independent, compared with a mean GFR loss of 6.5 mL/min/year among those achieving only a partial or no hematologic response (P < .009), most of whom developed end-stage renal disease (ESRD; P = .005)." — Sayed et al., *Blood* 2015 (PMID:26392598)

+6.1 vs −6.5 mL/min/year. The same disease, running in two directions, and the switch is the depth of the hematologic response.

**Course:** chronic progressive; lifelong. No spontaneous remission is described. Remission is treatment-induced and is a *hematologic* remission that the kidney then follows (or fails to follow, if fibrosis has already set).

**Critical intervention window:** before severe interstitial fibrosis and before GFR falls below ~30. Two independent series converge on this:
- *"Predictive factors were pre-treatment eGFR over 30 ml/min per 1.73 m(2) and post-treatment dFLC under 40 mg/l"* (Cohen, PMID:26176826)
- *"FLC response ≥ VGPR and absence of severe interstitial fibrosis were independent predictors of renal response."* (Joly, PMID:30578255)

---

## 9. Inheritance and Population

### Epidemiology
**No reliable incidence or prevalence figure exists.** Cassano et al. state it plainly: LCDD is *"a relatively rare condition with unknown incidence in literature because often its not diagnosed, in asymptomatic phases"* (PMID:39196376). For scale: the largest series ever assembled is **255 MIDD patients from an entire French national referral network** (PMID:30578255); Mayo accumulated **88 MIDD patients over 22 years** (1992–2014) (PMID:27501122). Orphanet classifies it as a rare disease (`ORPHA:93558`).

**For the dismech `prevalence` block:** use `measure_type: UNKNOWN` or `prevalence_class: RARE` with the source phrasing in `notes`. **Do not manufacture a rate_per_100000** — none is defensible from this literature.

### Inheritance
**Not heritable.** Acquired somatic clonal disorder. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency applies. Leave the `inheritance:` block absent rather than curating "not applicable" as a value.

### Demographics
- **Sex ratio:** male-predominant, 63.5% male (M:F ≈ 1.7:1) (PMID:14655186); male predominance also noted by PMID:39196376.
- **Light chain isotype:** κ ≫ λ; 68:32 (PMID:14655186), 11:1 in pure LCDD (PMID:11423577). *This is a far stronger κ bias than AL amyloidosis, where λ dominates* — a useful discriminating feature.
- **Age distribution:** peak 5th–6th decade; younger than AL amyloidosis and cast nephropathy (PMID:22156754); 36% ≤50 y.
- **Ethnicity / geography:** no established variation. All large series are from Western referral centers (US, France, UK, Italy) — ascertainment, not biology, likely explains that. Record as a gap.

---

## 10. Diagnostics

### 10.1 The diagnostic spine: kidney biopsy + monoclonal protein studies

> "The diagnosis of MGRS-related disease is established by kidney biopsy and immunofluorescence studies to identify the monotypic immunoglobulin deposits... Accordingly, the IKMG recommends a kidney biopsy in patients suspected of having MGRS to maximize the chance of correct diagnosis. Serum and urine protein electrophoresis and immunofixation, as well as analyses of serum free light chains, should also be performed to identify the monoclonal immunoglobulin... Finally, bone marrow aspiration and biopsy should be conducted to identify the lymphoproliferative clone. Flow cytometry can be helpful in identifying small clones." — Leung et al. (PMID:30510265)

### 10.2 Laboratory

| Test | Finding | Sensitivity |
|---|---|---|
| **Serum free light chain (sFLC) ratio** | abnormal | **100% (51/51 tested)** — Nasr (PMID:22156754). *"Serum free light chain ratio is abnormal in all MIDD patients, whereas only three-quarters have abnormal serum protein electrophoresis."* |
| **SPEP** | M-spike | **73% (47/64)** — Nasr (PMID:22156754) |
| Serum/urine immunofixation | monoclonal band | complements SPEP |
| Serum creatinine / eGFR | elevated / reduced | ~96% abnormal (PMID:14655186) |
| 24h urine protein | >1 g/d in 84% (PMID:14655186) | |
| Urinalysis / sediment | proteinuria ± hematuria | |
| dFLC (involved − uninvolved) | used for hematologic response; **<40 mg/L post-treatment predicts renal response** (PMID:26176826) | |
| Bone marrow aspirate/biopsy + flow + FISH | clone identification | per IKMG (PMID:30510265) |

**⚠️ The N-glycosylation blind spot.** Glycosylated pathogenic light chains may be **undetectable** in serum and urine (PMID:7829131). A negative FLC screen does not exclude LCDD when the biopsy shows monotypic deposits.

**LOINC anchors** (for `reference_ranges` if curated): serum kappa FLC, lambda FLC, and κ/λ ratio have LOINC codes; **I did not verify specific LOINC IDs in this session — look them up rather than guessing.**

### 10.3 Kidney biopsy — the definitive test

| Modality | Finding |
|---|---|
| **Light microscopy** | Nodular mesangial (glomerulo)sclerosis — 61% of MIDD (PMID:22156754), 100% of pure MIDD (PMID:11423577). Also membranoproliferative-like patterns, GBM duplication, increased lobulation (PMID:39196376). Tubulointerstitial fibrosis (a key prognostic feature, PMID:30578255). |
| **Congo red** | **NEGATIVE** — no apple-green birefringence. This is the defining negative. |
| **Immunofluorescence** | Monotypic (single-isotype) light chain staining, **linear along glomerular AND tubular basement membranes** and in mesangial nodules. κ in ~2/3 to 11/12 of cases. |
| **Electron microscopy** | Non-fibrillar, non-organized, finely granular/"powdery" electron-dense deposits along the inner aspect of the GBM and the outer aspect of the TBM (PMID:39196376). |
| **Mass spectrometry** | Laser-capture microdissection + LC-MS/MS for deposit typing when IF is equivocal — standard at referral centers. |

**Pathologic terminology now has a formal consensus** — worth citing in the entry for definitional grounding: Nasr SH, Royal V, et al. *"Renal Pathology Society/International Kidney and Monoclonal Gammopathy Research Group consensus on pathologic definitions and terminology of monoclonal gammopathy-associated kidney lesions."* Kidney Int. 2025 Aug;108(2):184-193 (PMID:40280412).

### 10.4 Imaging and functional testing

- **Kidney ultrasound** — pre-biopsy; nonspecific.
- **Echocardiography / cardiac MRI** — for cardiac involvement; diastolic dysfunction, wall thickening. Cardiac LCDD can mimic cardiac amyloidosis on imaging but is Congo-red-negative on biopsy.
- **Liver imaging / LFTs** — hepatic involvement.
- **Brain MRI** — for the rare intracerebral form; *"the diverse imaging presentations of this disease... can closely resemble other neurologic pathologies. Recognizing these potential mimics is crucial for avoiding misdiagnosis"* (PMID:38914431).
- **ECG / Holter** — conduction disease and arrhythmia (PMID:39196376).

### 10.5 Genetic testing

**Germline genetic testing has no role.** No WGS/WES/panel/CMA/karyotype/FISH/mtDNA/repeat-expansion indication for the patient's constitutional genome. FISH is used **on the clone** for hematologic risk stratification (PMID:30510265). Curate this as an explicit negative — it's the kind of thing that otherwise gets hallucinated into a rare-disease entry by pattern-matching.

### 10.6 Differential diagnosis (distinguishing features)

| Differential | How to tell it apart |
|---|---|
| **Diabetic nodular glomerulosclerosis (Kimmelstiel-Wilson)** | The #1 morphologic mimic. IF is negative for monotypic LC; no BM linear staining; diabetes history. |
| **AL amyloidosis** | Congo red **positive**, apple-green birefringence, fibrils 8–12 nm on EM; λ-predominant; mesangial LC is **endocytosed to lysosomes** rather than acting at the cell surface (PMID:33163710) |
| **Light chain cast nephropathy (myeloma kidney)** | Tubular casts, AKI presentation, higher creatinine (mean 7.8 vs 4.2 mg/dL), less nodular glomerulopathy (18% vs 100%), far more often overt MM (91% vs 31%) — all from Lin (PMID:11423577). **Can coexist with LCDD** (58/212 LCDD cases in Joly). |
| **HCDD / LHCDD** | IF shows heavy chain (± LC); HCDD associated with CH1 deletion and hypocomplementemia (PMID:11423577) |
| **Fibrillary GN / immunotactoid GN** | Organized fibrils/microtubules on EM |
| **MPGN / C3 glomerulopathy** | C3-dominant IF; MGRS-associated C3G has minimal Ig deposits (PMID:30510265) |
| **Fanconi syndrome from tubulopathic LC** | Different light chain population entirely — the tubulopathic LCs did *not* produce the mesangial phenotype in vitro (PMID:7639331) |
| **Amyloid-negative organized deposits, cryocrystalglobulinemia** | Crystalline deposits; distinct V-domain determinants (PMID:10828030) |

### 10.7 Screening

There is **no population screening** for LCDD and none is warranted. The rational secondary-prevention approach is: in patients with a known monoclonal gammopathy, monitor **albuminuria/proteinuria and eGFR**, and biopsy the kidney on unexplained renal deterioration — precisely because the 12-month diagnostic lag (PMID:27501122) is where kidneys are lost.

---

## 11. Outcome / Prognosis

### Survival

| Metric | Value | Source |
|---|---|---|
| Median estimated patient survival | **14.0 years** | Sayed, n=53 (PMID:26392598) |
| Alive at censor | 64% | Sayed (PMID:26392598) |
| Mean patient survival | 90 months | Nasr, n=64 (PMID:22156754) |
| 5-year overall survival | **67%** | Kourelis, n=88 (PMID:27501122) |
| Mean patient survival, pure MIDD | 54 months | Lin (PMID:11423577) |
| Mean patient survival, LCDD + cast nephropathy | **22 months** | Lin (PMID:11423577) |
| Deaths in bortezomib-treated cohort | 5/49 at median 54 mo follow-up | Cohen (PMID:26176826) |

### Renal survival

| Metric | Value | Source |
|---|---|---|
| Median renal survival from diagnosis | **5.4 years** | Sayed (PMID:26392598) |
| Mean renal survival | 64 months | Nasr (PMID:22156754) |
| 5-year renal survival | **57%** | Kourelis (PMID:27501122) |
| Progression to ESRD | 39% (22/56) | Nasr (PMID:22156754) |
| Required dialysis | **62%** | Sayed (PMID:26392598) |
| Reached uremia (incidence rate) | 23.7 per 100 patient-years | Pozzi (PMID:14655186) |
| Median survival from starting dialysis | 5.2 years | Sayed (PMID:26392598) |
| Mean renal survival, LCDD + cast nephropathy | **4 months** | Lin (PMID:11423577) |

### Prognostic factors

**Renal outcome:**
- Baseline eGFR / serum creatinine (the single most consistent factor): *"On multivariate analysis, initial creatinine was the only predictor of renal and patient survival in pure MIDD"* (PMID:11423577); *"a baseline GFR < 20 mL/min/1.73 m2... independently predictive of progression to dialysis"* (PMID:27501122); pre-treatment eGFR >30 (PMID:26176826)
- **Depth of hematologic response** — ≥VGPR (PMID:30578255; PMID:26392598); post-treatment dFLC <40 mg/L, *"the sole predictive factor of renal response by multivariable analysis"* (PMID:26176826)
- **Absence of severe interstitial fibrosis** (PMID:30578255)
- Age (RR 1.05 per year) (PMID:14655186)
- Hard constraint: *"Renal response occurred in 62 patients (36%), all of whom had achieved hematological response."* (PMID:30578255) — **no renal response occurred without a hematologic response. Zero exceptions in 255 patients.**

**Patient outcome:** age (RR 1.06), symptomatic MM (RR 2.75, 95% CI 1.22–6.2), extrarenal LC deposition (RR 2.24, 95% CI 1.15–4.35) (PMID:14655186).

**Notably NOT prognostic:** histologic parameters. *"While kappa-LC deposition was more frequently associated with nodular sclerosing glomerulopathy, histological parameters were not predictors of renal/patient prognosis."* (PMID:14655186)

### Dialysis is worth doing
> "The survival of the uremic patients undergoing dialysis was similar to that of patients not reaching uremia." … "Dialysis is worth performing in uremic LCDD patients." — Pozzi et al. (PMID:14655186)

### Trend over time
> "The prognosis for MIDD is improving compared with historical controls, likely reflecting earlier detection and improved therapies." — Nasr et al. (PMID:22156754)

---

## 12. Treatment

**Governing principle: treat the clone, not the kidney.** There is no therapy that removes deposits directly; everything works by shutting off the supply of pathogenic light chain and letting the tissue partially remodel (PMID:32559766).

### 12.1 Proteasome inhibitor–based therapy — current backbone

**Bortezomib + dexamethasone ± cyclophosphamide** (the "VCd"-type regimen).

> "Here we retrospectively studied 49 patients with MIDD who received a median of 4.5 cycles of intravenous bortezomib plus dexamethasone... The overall hematologic response rate, based on the difference between involved and uninvolved serum-free light chains (dFLCs), was 91%... Renal response was achieved in 26 patients, with a 35% increase in median eGFR and an 86% decrease in median 24-h proteinuria... Thus, bortezomib-based therapy is a promising treatment strategy in MIDD, mainly when used early in the disease course." — Cohen et al., *Kidney Int* 2015 (PMID:26176826)

**Mechanistic justification** (a rare case where the drug rationale is directly evidenced): the pathogenic light chain puts the plasma cell under ER stress, so proteasome blockade is disproportionately lethal to that clone (PMID:32559766). Bortezomib may also act on the kidney directly via NF-κB inhibition and TGF-β1 reduction (PMID:39196376 — full-text claim, see §16).

Suggested annotation:
```yaml
treatment_term: {preferred_term: Pharmacotherapy, term: {id: NCIT:C15986, label: Pharmacotherapy}}   # ✅
therapeutic_agent:
  - {preferred_term: bortezomib, term: {id: CHEBI:52717, label: bortezomib}}                          # ✅
  - {preferred_term: dexamethasone, term: {id: CHEBI:41879, label: dexamethasone}}                    # ✅
  - {preferred_term: cyclophosphamide, term: {id: CHEBI:4027, label: cyclophosphamide}}               # ✅
therapeutic_modality: SMALL_MOLECULE
target_mechanisms:
  - target: <the plasma-cell ER-stress / LC-secretion node>
    treatment_effect: INHIBITS
```
(NCIT also has `NCIT:C1851` Bortezomib ✅ if a drug-class NCIT term is preferred; note the repo memory that NCIT drug terms often fail `therapeutic_agent` enum validation — **prefer CHEBI here**.)

### 12.2 Autologous stem cell transplantation

> "Fifty-three (60%) received an autologous stem cell transplant (ASCT) or proteasome inhibitor (PI)-based treatments. Patients receiving ASCT or PI-based therapies were more likely to achieve at least a hematologic CR/VGPR compared to those receiving other therapies: 66% vs 2%, p < 0.0001." — Kourelis et al. (PMID:27501122)

That 66% vs 2% gap is not subtle. But note the honest caveat from the 2024 review: ASCT patients *"seem to achieve deeper and durable hematologic remissions and organ responses,"* though *"no statistically significant superiority can be demonstrated over non-transplant approaches"* (PMID:39196376).

Terms: `NCIT:C16039` Autologous Hematopoietic Stem Cell Transplantation ✅ (or `NCIT:C15431` Hematopoietic Cell Transplantation ✅); `therapeutic_modality: CELL_THERAPY`; conditioning agent `CHEBI:28876` melphalan ✅.

### 12.3 Anti-CD38 monoclonal antibody (daratumumab)

Evidence in LCDD specifically is **thin but real** — a consolidation study that pooled AL amyloidosis and LCDD:

> "We used as a consolidation a short course of daratumumab in 25 patients with AL amyloidosis or light chain deposition disease (LCDD), who had not achieved a haematologic complete response (hemCR) after standard therapy with bortezomib, cyclophosphamide and dexamethasone (VCD)... One month after consolidation completion, 8 patients (32%) achieved a hemCR, of whom 5 (20%) became also MRD negative." — Kastritis et al., *Amyloid* 2021 (PMID:34468250)

**⚠️ Curation caution:** this cohort is *mixed* AL + LCDD. Do not quote the 32% hemCR as an LCDD-specific figure. There is **no dedicated daratumumab-in-LCDD trial** — my PubMed title search for daratumumab + deposition disease returned nothing.

Terms: `NCIT:C74007` Daratumumab ✅; `therapeutic_modality: MONOCLONAL_ANTIBODY`; `NCIT:C20401` Monoclonal Antibody ✅.

### 12.4 Immunomodulatory drugs

Thalidomide (`CHEBI:9513` ✅) and lenalidomide (`CHEBI:63791` ✅) were used as add-ons in 6/49 of the Cohen cohort (PMID:26176826). **Lenalidomide requires renal dose adjustment** and is generally second-line here. Weak evidence base.

### 12.5 Kidney transplantation — the genuinely contested question

The literature has moved, and the entry should capture *both* positions with their evidence:

**Position A — high recurrence, be cautious.** *"The disease recurred in three of four patients who received a kidney transplant."* — Nasr (PMID:22156754). The 2024 review: *"Renal allograft is not recommended, due to high incidence of relapse,"* with recurrence *"after a median of 33.3 months in 5 of the 7 patients"* (PMID:39196376).

**Position B — safe if the clone is in sustained remission first.** *"Seven patients received a renal transplant, and among those whose underlying clonal disorder was in sustained remission, there was no recurrence of LCDD up to 9.7 years later."* — Sayed (PMID:26392598). And case-level support that bortezomib can rescue a recurring graft: *"they have experienced a prolonged period of stable renal function with no clinically detectable disease. These unique cases highlight the possibility to achieve long-term stable graft function and disease remission after renal transplantation for LCDD."* (Kuppachi, PMID:26915878).

These are reconcilable — the discriminator is **hematologic remission status at the time of transplant**, not transplantation per se. That reconciliation is a good candidate for a `discussions` block rather than picking a winner.

Terms: `NCIT:C15265` Kidney Transplantation ✅; `NCIT:C15248` Hemodialysis ✅; `NCIT:C15289` Organ Transplantation ✅; `NCIT:C15747` Supportive Care ✅.

### 12.6 Supportive care

RAAS blockade for proteinuria, blood-pressure control, management of nephrotic syndrome, renal replacement therapy. No LCDD-specific supportive-care trial exists.

### 12.7 Treatment algorithm (synthesized)

1. Confirm by kidney biopsy (IF + EM + Congo red) and identify the clone (sFLC, SPEP/IFE, marrow, flow, FISH).
2. **Treat early — before eGFR <30 and before severe interstitial fibrosis** (PMID:26176826; PMID:30578255).
3. Bortezomib-based induction; **target ≥VGPR / dFLC <40 mg/L**, not merely "a response."
4. Consider ASCT in eligible patients for depth/durability (PMID:27501122).
5. Daratumumab consolidation if the hemCR target is missed (PMID:34468250, mixed cohort).
6. Kidney transplant only after sustained clonal remission (PMID:26392598).
7. Monitor sFLC/dFLC longitudinally as the surrogate for renal protection.

### 12.8 Response criteria — an active methodological problem

Renal response in MIDD has been assessed using criteria borrowed from AL amyloidosis or from IMWG (PMID:27501122), and a 2025 *Leukemia* paper explicitly addresses *"Refining renal response assessment in monoclonal immunoglobulin deposition disease: Challenges, limitations and need for consensus."* Worth recording as a live gap — cross-study response rates are not strictly comparable.

### 12.9 Pharmacogenomics, gene therapy, RNA therapy, gene editing

**None applicable / none reported for LCDD.** No PharmGKB/CPIC guidance specific to this disease. Don't invent an ASO or gene-therapy angle here.

### 12.10 Clinical trials

I identified **no LCDD-specific interventional trial with an NCT identifier.** LCDD patients are typically enrolled in AL amyloidosis or MGRS trials, or treated off-protocol on myeloma regimens. If the entry gets a `clinical_trials:` block, it should probably stay empty rather than importing AL amyloidosis trials — and remember `phase:`/`status:` are enums (`PHASE_III`, `COMPLETED`), not prose.

---

## 13. Prevention

- **Primary prevention: none exists.** You cannot prevent the emergence of a clone with a structurally unlucky V domain.
- **Secondary prevention (early detection): this is where the leverage is.** In anyone with a known monoclonal gammopathy, track proteinuria/albuminuria and eGFR, and biopsy on unexplained decline. The 12-month lag between the first renal signal and diagnosis (PMID:27501122) is an unforced loss, and the treatment window closes with fibrosis (PMID:30578255).
- **Tertiary prevention:** aggressive clone-directed therapy targeting ≥VGPR to prevent ESKD (PMID:26392598), and confirmed sustained remission before kidney transplant to prevent allograft recurrence (PMID:26392598).
- **Immunization / vaccines:** not applicable to the disease; standard immunosuppression-related vaccination applies to treated patients.
- **Genetic screening / counseling / prenatal testing / PGD:** **not applicable.** Somatic, non-heritable.
- **Public health and environmental interventions:** not applicable — no environmental cause is known.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human — `NCBITaxon:9606`. Experimental mouse — `NCBITaxon:10090`. Rat (in-vitro mesangial cell source) — `NCBITaxon:10116`. *(CURIEs standard; not verified against repo cache this session.)*
- **Breed (VBO):** not applicable.
- **Natural disease in other species:** **I found no report of naturally occurring LCDD in any non-human species.** Dogs, cats, and horses do develop plasma cell myeloma and AL amyloidosis, but a natural Randall-type non-amyloid light chain deposition disease is not documented in the sources I retrieved (no OMIA entry surfaced). Record as "not reported," not as "does not occur" — absence of evidence, and veterinary renal biopsy with immunofluorescence is uncommon.
- **Comparative pathology:** The disease is fundamentally a product of somatic hypermutation in an immunoglobulin V gene — a process conserved across jawed vertebrates — so there is no *a priori* barrier to it occurring in other mammals. It may simply be under-ascertained.
- **Evolutionary conservation of mechanism:** The downstream half (mesangial TGF-β–driven matrix accumulation) is deeply conserved and shared with diabetic nephropathy and other sclerosing glomerulopathies — the Bender authors say so explicitly (PMID:32559766). The upstream half (a specific human V-gene-derived pathogenic protein) is idiosyncratic to the individual patient's clone.
- **Zoonotic potential / cross-species transmission:** none. Not transmissible.

---

## 15. Model Organisms

### 15.1 The flagship model — transgenic LCDD mouse (Bender/Sirac 2020)

**Citation:** Bender S, Ayala MV, Bonaud A, Javaugue V, et al. *Blood.* 2020;136(14):1645-1656. **PMID:32559766**

| Attribute | Detail |
|---|---|
| Type | Genetically engineered mouse (mammalian, in vivo) |
| Construction | Site-directed insertion of the **variable domain of a pathogenic human LC gene into the mouse immunoglobulin κ locus**, so all plasma cells produce it; backcrossed onto a background with increased PC differentiation and no IgH production to achieve high free LC levels |
| Recapitulates | *"progressive glomerulosclerosis, nephrotic-range proteinuria, and finally kidney failure"* |
| Key mechanistic finding | LC induces **ER stress** in plasma cells (RNA-seq) → explains proteasome-inhibitor efficacy |
| Rescue arm | Reduction of circulating pathogenic LC *"not only preserved renal function but also partially reversed kidney lesions"* — a `RESTORED` readout |
| Novel biology | Presclerotic glomeruli show **proliferation and ECM remodeling as the first steps** |

**Suggested `modeled_mechanisms` links:**
| Target node | relationship | fidelity | limitations |
|---|---|---|---|
| Nodular glomerulosclerosis / progressive glomerulosclerosis | `RECAPITULATES` | HIGH | requires an engineered high-FLC background (IgH-null, enhanced PC differentiation) that does not correspond to any human hematologic state |
| Plasma cell ER stress | `RECAPITULATES` | MODERATE | transcriptomic inference; bulk RNA-seq |
| Nephrotic-range proteinuria / kidney failure | `RECAPITULATES` | HIGH | — |
| Extrarenal (hepatic/cardiac/CNS) deposition | *(not demonstrated)* | — | the model is renal-centric; the 35% extrarenal burden seen in humans (PMID:30578255) is not addressed |
| Reversibility on LC reduction | `RESCUES` | MODERATE | partial reversal only |

**Model limitations to record honestly:** single human V domain (one patient's clone, not a panel); mouse Igκ-locus context; no myeloma tumor burden; extrarenal involvement not modeled; the proliferation-first finding is in tension with in-vitro anti-proliferative LC data (PMID:7639331).

### 15.2 In vitro — cultured mesangial cells + patient-derived light chains

**The workhorse system**, and it's genuinely elegant: purify light chains from the *urine of biopsy-proven patients*, put them on cultured mesangial cells grown on an artificial matrix, and watch the human lesion reassemble in a dish.

| Study | System | Finding |
|---|---|---|
| Zhu et al. 1995 (**PMID:7639331**) | Cultured **rat** mesangial cells + 2 urinary LCs from biopsy-proven LCDD patients; human albumin and 2 tubulopathic LCs as controls | ↓ proliferation, ↑ collagen IV/laminin/fibronectin, ↑ TGF-β; **anti-TGF-β abolishes both effects** |
| Herrera et al. 1999 (**PMID:10369104**) | Mesangial cells on artificial matrix + LCDD-LC vs amyloidogenic-LC | ↑ ECM (incl. tenascin) peaking at 72 h, ↓ collagenase IV; *"The immunomorphologic mesangial alterations observed in biopsy material are closely reproduced in vitro"* |
| Herrera et al. 2020 review (**PMID:33163710**) | Synthesis | LCDD-LC signals **at the cell surface**; AL-LC is **endocytosed to lysosomes** |

**Evidence-source tagging:** all three are `IN_VITRO` (rat-derived *cells*, not a whole animal — per the repo's classification rules, cultured cells are IN_VITRO even when the cells are animal-derived).

### 15.3 Related engineered models (adjacent, cite with care)

- **Cryocrystalglobulinemia hybridoma-graft mouse** (Rengers et al., *Blood* 2000, **PMID:10828030**) — not LCDD, but directly relevant to the "V domain determines the lesion" principle: *"A limited variation in the V(kappa) domain thus proved able to increase secretion, to abrogate crystallization, and to modify patterns of glomerular lesions and deposits."* A three-amino-acid deletion in Vκ CDR1 switched the entire renal phenotype. Use this as supporting evidence for the V-domain-determines-pathology node, clearly labeled as a *different* deposition disease.
- **HCDD mouse models** exist in the Limoges group's output but I did not verify a specific PMID in this session — **do not cite one from memory.**

### 15.4 Not available

No zebrafish, Drosophila, *C. elegans*, yeast, iPSC, organoid, or organ-chip model of LCDD identified. No CRISPR/RNAi functional screen. No immortalized LCDD cell line in Cellosaurus that I could confirm. These are real gaps and worth stating as such — a NAM (organ-chip glomerulus + patient LC) is an obvious unbuilt experiment.

### 15.5 Resources
MGI (for the transgenic line), Alliance of Genome Resources. No dedicated LCDD model repository.

---

## 16. Provenance, verification status, and curation cautions

**Sources whose quotes are verbatim from PubMed abstracts I retrieved this session** (safe for `snippet:` after a `just fetch-reference` + `just count-verified-snippets` check): PMIDs 814812, 7639331, 7829131, 8918585, 10369104, 10828030, 11423577, 14655186, 22156754, 26176826, 26392598, 26915878, 27501122, 30510265, 30578255, 31767034, 32559766, 33163710, 33801393, 34468250, 38914431.

**⚠️ PMID:39196376 (Cassano et al., *Ann Hematol* 2024) — quotes in this report come from the article FULL TEXT via PMC, not the abstract.** Under this repo's rules, `just validate-disorders` runs with `--no-full-text`, so a snippet drawn from the body **will fail CI even though the text is genuine**. Either find the equivalent claim in another paper's abstract, or commit the full-text cache file, or drop the snippet and keep the description.

**PMID:40280412** (RPS/IKMG pathologic definitions consensus, *Kidney Int* 2025) — I have the citation and title but did **not** retrieve its abstract body. Cite it structurally; do not quote it.

**Other verification notes:**
- The 2025 *Leukemia* paper on refining renal response assessment in MIDD was seen in search results only — **I did not retrieve a PMID for it.** Look it up before citing.
- HGNC CURIEs for `IGKV4-1` etc. are **not verified**; GO Cellular Component and LOINC IDs are **not verified**; NCBITaxon CURIEs are standard but **not cache-checked**.
- All HP / GO / CL / UBERON / CHEBI / NCIT CURIEs marked ✅ were read directly from this repository's validated caches, or (for the "no nodular glomerulosclerosis term" finding) from a live OLS query.
- **Highest-risk mis-annotation for this entry:** `HP:0001917` Renal amyloidosis. LCDD is Congo-red-negative and non-fibrillar. Using an amyloid term here would encode the exact error the whole diagnostic literature exists to prevent.
- **Second-highest risk:** importing MONDO's loose synonyms (`Bence Jones myeloma`, `Light chain disease`) as exact synonyms.
- **Third:** treating MeSH-mapped search results as LCDD literature — PubMed silently rewrites the query to AL amyloidosis.

---

## Sources

Primary literature (PubMed):
- [PMID:814812 — Randall et al., Manifestations of systemic light chain deposition, *Am J Med* 1976](https://pubmed.ncbi.nlm.nih.gov/814812/)
- [PMID:7639331 — Zhu et al., Pathogenesis of glomerulosclerosis in LCDD: role for TGF-β, *Am J Pathol* 1995](https://pubmed.ncbi.nlm.nih.gov/7639331/)
- [PMID:7829131 — Denoroy et al., Overrepresentation of the VκIV subgroup in LCDD, *Immunol Lett* 1994](https://pubmed.ncbi.nlm.nih.gov/7829131/)
- [PMID:8918585 — Decourt et al., Structural peculiarities of a truncated VκIII light chain, *Clin Exp Immunol* 1996](https://pubmed.ncbi.nlm.nih.gov/8918585/)
- [PMID:10369104 — Herrera et al., Glomerulopathic light chain–mesangial cell interactions, *Ultrastruct Pathol* 1999](https://pubmed.ncbi.nlm.nih.gov/10369104/)
- [PMID:10828030 — Rengers et al., Heavy and light chain primary structures control IgG3 nephritogenicity, *Blood* 2000](https://pubmed.ncbi.nlm.nih.gov/10828030/)
- [PMID:11423577 — Lin et al., Renal MIDD: the disease spectrum, *JASN* 2001](https://pubmed.ncbi.nlm.nih.gov/11423577/)
- [PMID:14655186 — Pozzi et al., LCDD with renal involvement, *Am J Kidney Dis* 2003](https://pubmed.ncbi.nlm.nih.gov/14655186/)
- [PMID:22156754 — Nasr et al., Renal MIDD: 64 patients, *CJASN* 2012](https://pubmed.ncbi.nlm.nih.gov/22156754/)
- [PMID:26176826 — Cohen et al., Bortezomib in MIDD, *Kidney Int* 2015](https://pubmed.ncbi.nlm.nih.gov/26176826/)
- [PMID:26392598 — Sayed et al., Natural history and outcome of LCDD, *Blood* 2015](https://pubmed.ncbi.nlm.nih.gov/26392598/)
- [PMID:26915878 — Kuppachi et al., LCDD after kidney transplantation, *Transplant Proc* 2016](https://pubmed.ncbi.nlm.nih.gov/26915878/)
- [PMID:27501122 — Kourelis et al., Outcomes of patients with renal MIDD, *Am J Hematol* 2016](https://pubmed.ncbi.nlm.nih.gov/27501122/)
- [PMID:30510265 — Leung et al., IKMG consensus on MGRS, *Nat Rev Nephrol* 2019](https://pubmed.ncbi.nlm.nih.gov/30510265/)
- [PMID:30578255 — Joly et al., Randall-type MIDD nationwide cohort, *Blood* 2019](https://pubmed.ncbi.nlm.nih.gov/30578255/)
- [PMID:31767034 — Wang et al., Pathogenesis of renal injury and treatment in LCDD, *J Transl Med* 2019](https://pubmed.ncbi.nlm.nih.gov/31767034/)
- [PMID:32559766 — Bender et al., Immunoglobulin light-chain toxicity in a mouse model of LCDD, *Blood* 2020](https://pubmed.ncbi.nlm.nih.gov/32559766/)
- [PMID:33163710 — Herrera et al., Understanding mesangial pathobiology in AL-amyloidosis and LCDD, *Kidney Int Rep* 2020](https://pubmed.ncbi.nlm.nih.gov/33163710/)
- [PMID:33801393 — Cohen et al., Randall-type MIDD: new insights, *Diagnostics* 2021](https://pubmed.ncbi.nlm.nih.gov/33801393/)
- [PMID:34468250 — Kastritis et al., Daratumumab consolidation in AL amyloidosis or LCDD, *Amyloid* 2021](https://pubmed.ncbi.nlm.nih.gov/34468250/)
- [PMID:38914431 — Rai et al., Light-chain deposition diseases of the CNS, *AJNR* 2025](https://pubmed.ncbi.nlm.nih.gov/38914431/)
- [PMID:39196376 — Cassano et al., LCDD: pathogenesis, clinical characteristics and treatment strategies, *Ann Hematol* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052853/)
- [PMID:40280412 — Nasr, Royal et al., RPS/IKMG consensus on pathologic definitions, *Kidney Int* 2025](https://www.kidney-international.org/article/S0085-2538(25)00336-9/abstract)

Ontology / terminology resources:
- [MONDO:0019730 via EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0019730)
- [Orphanet ORPHA:93558](https://www.orpha.net/en/disease/detail/93558)
- [Pathology Outlines — Light chain deposition disease](https://www.pathologyoutlines.com/topic/kidneylightchaindepositiondisease.html)
- [Kidney International — Diagnosis of monoclonal gammopathy of renal significance](https://www.kidney-international.org/article/S0085-2538(15)30217-9/fulltext)
- [Nature/Leukemia — Refining renal response assessment in MIDD (2025)](https://www.nature.com/articles/s41375-025-02686-4)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.