---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-19T13:25:04.918622'
end_time: '2026-07-19T13:31:13.792680'
duration_seconds: 368.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Prune Belly Syndrome
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
  - claude-sonnet-5
  web_search_requests: 26
  num_turns: 33
  total_cost_usd: 2.3738953
  session_id: 0edef908-90c1-526c-8a5f-903c85c41752
  stop_reason: end_turn
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Prune Belly Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Prune Belly Syndrome** covering all of the
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

I now have sufficient primary-literature-backed data across all sections. Here is the comprehensive research report.

---

# Prune Belly Syndrome — Comprehensive Research Report

## 1. Disease Information

**Overview:** Prune Belly Syndrome (PBS) is a rare, complex congenital disorder classically defined by a triad: (1) deficiency/agenesis of the ventral abdominal wall musculature producing a wrinkled, "prune-like" skin appearance, (2) massive dilation of the urinary tract (megacystis, megaureter, hydronephrosis) with poorly contractile, collagen-replaced smooth muscle, and (3) bilateral intra-abdominal cryptorchidism in males. It is now understood as a multisystem congenital myopathy/mesenchymal disorder rather than an isolated urologic anomaly, with an estimated 75% of patients having additional anomalies of the cardiac, gastrointestinal, respiratory, and musculoskeletal systems (StatPearls, NBK544248).

**Key identifiers:**
- **OMIM:** #100100 (PRUNE BELLY SYNDROME; PBS) — https://omim.org/entry/100100
- **Orphanet:** ORPHA:2970
- **ICD-10-CM:** Q79.4 (Prune belly syndrome)
- **MeSH:** Prune Belly Syndrome
- **GARD:** 7479

**Synonyms:** Eagle-Barrett syndrome, Obrinsky syndrome, Triad syndrome, Abdominal Muscle Deficiency Syndrome, Congenital Absence of the Abdominal Muscles, Fröhlich syndrome (rare usage), Abdominal muscular deficiency syndrome, Megacystis-megaureter-cryptorchidism.

**Source of information:** The evidence base is derived primarily from aggregated disease-level resources (OMIM, Orphanet, StatPearls, GeneReviews-style narrative reviews) supplemented by clinical case series/registries (e.g., ESPN/ERA-EDTA European dialysis registry, single-center surgical cohorts of 15–50 patients) and individual case reports/family reports for genetic findings (most causal-gene evidence derives from single consanguineous families or sporadic trios rather than large cohorts) (PMID:22077972; PMID:31441039; PMID:38184690; PMID:32085749).

---

## 2. Etiology

**Disease causal factors — two dominant, non-mutually-exclusive theories:**
1. **Mesenchymal (lateral plate mesoderm) developmental defect theory:** A primary injury to the lateral plate mesoderm between gestational weeks 6–10 — the tissue from which the abdominal wall musculature, ureters, bladder, prostate, and gubernaculum all arise — produces the full triad as parallel, not sequential, malformations (StatPearls NBK544248; ScienceDirect "Etiology and pathogenesis of the prune belly syndrome").
2. **Urethral/bladder-outlet obstruction (obstructive uropathy) theory:** A hypoplastic/dysplastic prostate or urethral anomaly (severe angulation at the prostatomembranous junction, or a hypoplastic-prostate "flap valve") obstructs urine outflow in utero, causing massive bladder distension that secondarily stretches and thins the abdominal wall and displaces the testes, with resultant oligohydramnios. Notably, most contemporary reviews conclude the urologic dilation is *not* a true fixed anatomic outlet obstruction, since post-mortem/post-natal series rarely find one (Medscape "Prune Belly Syndrome" pathophysiology overview; StatPearls NBK544248).
3. A minority "yolk sac" embryologic theory has also been proposed but is less supported (StatPearls NBK544248).

**Genetic risk factors:**
- **CHRM3** (cholinergic receptor muscarinic 3, chr 1q43) — homozygous/biallelic loss-of-function variants cause PBS or a Prune-Belly-like syndrome in consanguineous families (autosomal recessive). CHRM3 encodes the M3 muscarinic acetylcholine receptor, the major mediator of detrusor smooth-muscle contraction (PMID:22077972 — Weber S et al., *Am J Hum Genet* 2011;89(5):668-74: "Muscarinic Acetylcholine Receptor M3 Mutation Causes Urinary Bladder Disease and a Prune-Belly-like Syndrome"; a homozygous frameshift c.1173_1184delinsT (p.Pro392Alafs*43) truncates the third intracellular loop in a consanguineous Turkish kindred with six affected brothers exhibiting megacystis with detrusor hyporeflexia). A second family with a homozygous missense variant (c.352G>A; p.Gly118Arg) causing familial urinary bladder disease with impaired pupillary light reflex (a recognized CHRM3 phenotype feature) was reported by Beaman et al. (PMID:31441039, *Clin Genet* 2019;96(6):515-520). *Chrm3*-null mice phenocopy the megabladder phenotype, supporting causality.
- **PIEZO1** — compound heterozygous loss-of-function variants (c.757G>A p.Gly253Arg; c.6584C>T p.Ser2195Leu) identified by whole-exome sequencing in a PBS proband; PIEZO1 is the dominant mechanosensitive ion channel in bladder smooth muscle (PIEZO2 is absent there). Electrophysiology showed reduced pressure-induced channel open probability (NPo) without altered single-channel conductance; the PIEZO1 agonist Yoda1 rescued the NPo defect in vitro, nominating a candidate small-molecule therapeutic mechanism (PMID:38184690, *Nat Commun* 2024).
- **FLNA** (Filamin A, X-linked, Xq28) — hemizygous missense variants (p.A1448V, p.C2160R, p.G2236E) identified in surviving adult males with PBS, two of which map to the mechanosensing Ig19–21 region and enhance binding to β1-integrin tails; proposed as the first X-linked PBS mechanism, consistent with the strong male predominance (PMID:32085749, *BMC Med Genet* 2020;21:38, Iqbal NS, Jascur TA, Harrison SM, et al.).
- **HNF1B** — screened in a PBS cohort; one variant found in ~3% of patients but judged functionally normal in reporter assays, so HNF1B is not considered a major PBS gene despite some deletion case reports (PMID:22114815, *J Urol* 2012).
- **ACTA2 / ACTG2** — heterozygous variants reported in single cases, including one child with PBS, congenital mydriasis, and cerebrovascular anomalies attributed to an ACTA2 mutation (PMID:24998021) — these smooth-muscle actin genes overlap mechanistically with visceral myopathy/megacystis-microcolon spectrum disorders.
- **STIM1** — also reported as a plausible single-case candidate gene.
- Overall: "Five autosomal genes, including CHRM3, HNF1β, ACTA2, ACTG2 and STIM1, have been reported with potentially causal DNA variants, however these genes each only account for one or two PBS cases or one PBS multiplex consanguineous kindred" — the great majority of PBS remains genetically unsolved, and **no candidate gene yet explains the strong male/X-linked-appearing predominance** other than the recent FLNA report (PMID:32085749).
- A **CNV report**: a novel 16p11.2 duplication has been associated with PBS in a case report (PMC8496350).

**Environmental / non-genetic risk factors:**
- **Twin pregnancy:** incidence in twins reported as ~4× higher than in singletons (search synthesis from multiple epidemiology sources; StatPearls NBK544248).
- **Younger maternal age** associated with higher incidence (StatPearls NBK544248).
- **Race:** twice as common in Black vs. White populations in some U.S. series.
- **In vitro fertilization (IVF):** case reports of PBS (including in a female newborn) following IVF-induced pregnancy, suggesting assisted reproduction may be a risk-modifying exposure, though causality is not established (PMC10700981).
- Monozygotic (MZ) twin pairs have been reported both **concordant and discordant** for PBS, indicating that inherited genetic variants alone cannot fully explain pathogenesis — in one discordant identical female twin pair, twin-twin transfusion physiology (fetal anasarca) was implicated as an environmental/hemodynamic contributor to abdominal wall laxity (NEJM 1983;308:275). A separate discordant MZ twin case found DNA hypomethylation at 6q24 (TNDM), IGF2R, DIRAS3, and PEG1 loci only in the affected twin, raising an epigenetic/stochastic contribution (*Eur J Pediatr*).

**Protective factors:** No genetic or environmental protective factors for PBS have been established in the literature reviewed; this is an area of unmet knowledge.

**Gene-environment interactions:** Not formally characterized; the co-occurrence of genetic lesions (CHRM3/PIEZO1/FLNA loss-of-function in bladder smooth muscle/mechanotransduction machinery) with mechanical/hemodynamic amplifiers (twinning, IVF, bladder over-distension) is suggestive but not mechanistically proven as an interaction.

---

## 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Notes / suggested HPO |
|---|---|---|---|---|
| Deficient/absent abdominal wall musculature, wrinkled "prune" skin | Physical/congenital malformation | Congenital, evident at birth | Defining (~100% in classic triad) | HP:0004298 (Abdominal wall muscle deficiency) — verify label via OAK before use |
| Megacystis / massively distended, poorly contractile bladder | Structural/urologic | Congenital (often prenatally detectable 2nd trimester) | Defining | Suggest HP term for "enlarged bladder" — verify exact HPO ID/label via OAK |
| Bilateral hydroureteronephrosis | Structural/urologic | Congenital | Almost universal | HP:0000126 (Hydronephrosis) — verify |
| Vesicoureteral reflux | Functional/urologic | Congenital | ~75% | Verify HPO term |
| Renal dysplasia | Structural | Congenital | ~50% | HP:0000110 (Renal dysplasia) — verify |
| Bilateral intra-abdominal cryptorchidism (males) | Physical/congenital | Congenital | Defining in males | HP:0000028 (Cryptorchidism) — verify |
| Prostatic hypoplasia with dilated prostatic urethra | Structural | Congenital | Common | — |
| Pulmonary hypoplasia | Structural/respiratory | Congenital (2° to oligohydramnios) | ~58% of associated-anomaly cases; dominant driver of perinatal mortality | HP:0002089 (Pulmonary hypoplasia) — verify |
| Cardiac anomalies (PDA, VSD, ASD, tetralogy of Fallot) | Structural | Congenital | ~25% | Verify individual HPO terms |
| GI anomalies (midgut malrotation, bowel atresia, anorectal anomalies, Hirschsprung disease, gastroschisis) | Structural | Congenital | ~24% | — |
| Musculoskeletal anomalies (scoliosis, talipes equinovarus/clubfoot, hip dysplasia, torticollis, contractures) | Structural | Congenital | ~22% | HP:0001762 (Talipes equinovarus) — verify |
| Recurrent urinary tract infection | Clinical/functional | Infancy onward | ~80% of patients have ≥1 documented UTI | — |
| Impaired pupillary constriction (CHRM3-related cases) | Physical sign | Congenital | Reported in CHRM3-mutation-positive families | Reflects shared muscarinic receptor smooth-muscle biology (iris sphincter) |
| Chronic constipation | Functional | Childhood onward | Common (impaired Valsalva from abdominal wall deficiency) | — |
| Chronic kidney disease / ESRD | Laboratory/functional | Childhood–adolescence | ~30% of survivors | — |

**Onset/severity/progression:** Onset is congenital in essentially all cases; severity spans from lethal perinatal disease (Woodard/severity Category I) to mild, near-normal-life disease (Category III) — see Section 8 and 11. Course for the urinary tract component is generally progressive with respect to renal function in the more severe categories, but many patients with normal early renal function have a stable course into adulthood. A validated phenotypic severity scoring system (RUBACE — renal, ureter, bladder, abdominal wall, cryptorchidism, and other anomalies) has been developed and correlates with the Woodard categories (mean RUBACE scores 20.5, 13.8, and 10.6 for Categories 1, 2, 3 respectively) (PMID:30113772, Wong et al., *BJU Int* 2019).

**Quality of life:** Long-term studies of adults with PBS describe "good health-related quality of life and good social and sexual function," with patients participating in conventional physical, sexual, emotional, educational, and employment roles — except that patients who progress to require kidney transplantation score significantly lower on multiple QoL indices (multiple sources synthesized from Journal of Urology/Journal of Pediatric Urology adult-outcome literature).

---

## 4. Genetic/Molecular Information

**Causal genes (biallelic/monogenic, each accounting for only single families/cases):**
- **CHRM3** (HGNC:2733; OMIM *118494) — chr 1q43; loss-of-function (frameshift, missense) causing autosomal recessive PBS/urinary bladder disease. Functional consequence: loss of M3 muscarinic receptor-mediated detrusor contraction → detrusor hyporeflexia/megacystis (PMID:22077972; PMID:31441039).
- **PIEZO1** (HGNC:26940) — chr 16q24.3; compound heterozygous loss-of-function affecting mechanosensitive channel gating in bladder smooth muscle (PMID:38184690).
- **FLNA** (HGNC:3754) — Xq28; hemizygous missense variants in surviving adult males, affecting the actin-crosslinking/mechanosensing scaffold function of filamin A in smooth muscle, altering β1-integrin binding (PMID:32085749). This is the only reported X-linked mechanism and is of particular interest given PBS's strong male bias.
- **HNF1B** (HGNC:11630) — rare/uncommon; functionally normal variant found in a small fraction, so its causal role is doubtful (PMID:22114815).
- **ACTA2** (HGNC:130), **ACTG2** (HGNC:144), **STIM1** (HGNC:11386) — single-case/single-family candidate genes overlapping with the visceral myopathy/megacystis-microcolon spectrum (PMID:24998021 for ACTA2 + congenital mydriasis + cerebrovascular anomalies).

**Variant classification/type:** Reported variants span missense (majority), frameshift/truncating, and one CNV report (16p11.2 duplication). Most are ultra-rare/private, reported in single consanguineous families or trios; population allele frequencies in gnomAD are expected to be extremely low or absent given the rarity and severity. No pathogenic variant to date is common enough to be a major population risk allele.

**Somatic vs. germline:** All reported PBS variants are germline (constitutional).

**Functional consequences:** Loss-of-function is the consistent mechanism across CHRM3, PIEZO1, and FLNA — i.e., PBS mechanistically converges on **impaired smooth-muscle contractility/mechanotransduction** in the developing bladder wall, whether via loss of the contraction-triggering receptor (CHRM3), loss of stretch-sensing (PIEZO1), or loss of the cytoskeletal mechanosensing scaffold (FLNA).

**Modifier genes / genetic heterogeneity:** No formal modifier genes are established; the syndrome is genetically heterogeneous, and "the currently suggested candidate genes [do not] fit an X-linked recessive mode of inheritance" as a class (except FLNA), and functional data are lacking for many variants.

**Epigenetic information:** Limited to a single case report describing loss of DNA methylation at 6q24 (TNDM locus), IGF2R, DIRAS3, and PEG1 in the PBS-affected member of a discordant monozygotic twin pair, with normal methylation in the healthy co-twin — suggestive of a possible epigenetic/imprinting contribution in at least some sporadic cases, though not replicated at scale.

**Chromosomal abnormalities:** A 16p11.2 duplication case report exists (PMC8496350); PBS is not classically associated with common aneuploidy syndromes, though it has occasionally been reported comorbid with Down syndrome and other chromosomal anomalies in case literature (not systematically quantified in the sources reviewed here).

---

## 5. Environmental Information

- **Twin gestation** (elevated incidence, ~4×) — likely reflecting a shared hemodynamic/mechanical mechanism (e.g., twin-twin transfusion producing fetal anasarca and abdominal wall thinning) rather than a toxin exposure per se.
- **IVF/assisted reproduction** — case-level association reported; mechanism unclear (possibly related to underlying subfertility factors, monozygotic twinning risk with IVF, or epigenetic dysregulation associated with assisted reproductive technology).
- **Maternal age** — younger maternal age associated with higher incidence in some series.
- No specific toxin, chemical, radiation, or infectious exposure has been established as causal in the literature surveyed. No infectious agent is implicated in PBS pathogenesis (this is a structural/mesenchymal developmental disorder, not an infectious one).

---

## 6. Mechanism / Pathophysiology

**Causal chain (synthesized from mesenchymal-defect and obstructive-uropathy theories, plus molecular data):**

1. **Trigger:** Either (a) a primary lateral-plate-mesoderm patterning defect during weeks 6–10 gestation, or (b) a molecular lesion impairing bladder-wall smooth-muscle mechanotransduction/contractility (CHRM3, PIEZO1, or FLNA loss-of-function).
2. **Detrusor/bladder-wall dysfunction:** Loss of M3-muscarinic-receptor-mediated contraction (CHRM3) and/or loss of PIEZO1-mediated stretch-sensing and/or loss of FLNA-mediated cytoskeletal force transmission → **detrusor hyporeflexia and failure of normal micturition** (PMID:22077972; PMID:38184690; PMID:32085749).
3. **Megacystis and urinary stasis:** Impaired bladder emptying → progressive bladder distension (megacystis) with high post-void residual volumes.
4. **Secondary mesenchymal/histologic remodeling:** Throughout the urinary tract (bladder, ureter), smooth muscle is progressively **replaced by collagen/fibrous tissue**, with the ratio of collagen to smooth muscle increasing distally (more severe in the distal, refluxing ureteral segments) — producing a compliant, "smooth-walled" (non-trabeculated) enlarged bladder and tortuous, poorly peristaltic ureters (ScienceDirect/StatPearls histopathology synthesis).
5. **Bidirectional propagation to adjacent structures:**
   - **Abdominal wall:** Sustained intra-abdominal distension from the massively enlarged bladder (and/or the shared mesenchymal defect) impairs normal abdominal wall muscle development, producing deficient/absent musculature and the classic wrinkled "prune" skin.
   - **Testes:** Displacement and/or failure of normal gubernacular-mesenchyme-guided descent leaves the testes intra-abdominal (bilateral cryptorchidism), since the gubernaculum arises from the same mesenchymal lineage.
   - **Prostate:** Hypoplastic development, producing a dilated, poorly supported prostatic urethra that further impairs voiding dynamics (a partial feedback loop into step 3).
6. **Amniotic fluid dynamics:** Reduced effective fetal urine output/impaired voiding → **oligohydramnios**.
7. **Pulmonary consequence:** Oligohydramnios (± further restriction from abdominal wall deficiency and skeletal/thoracic anomalies) → **pulmonary hypoplasia**, the dominant driver of early neonatal/perinatal mortality (Potter-sequence-like physiology) (StatPearls NBK544248).
8. **Postnatal renal consequence:** Renal dysplasia (present in ~50%) plus chronic urinary stasis/reflux/infection → progressive nephron loss → chronic kidney disease/ESRD in ~30% of survivors, at a younger median age of renal-replacement-therapy initiation (7.0 years) than other congenital obstructive uropathies (9.6 years) (PMID:28779237, Yalcinkaya F et al., *Pediatr Nephrol* 2017;33:117-124).

**Upstream vs. downstream:** The bladder-wall contractile/mechanotransduction defect (molecular lesions) and/or primary mesenchymal patterning defect is upstream; megacystis, abdominal wall deficiency, and cryptorchidism are best modeled as parallel (not strictly sequential) downstream consequences of the shared upstream mesenchymal/myogenic insult, with oligohydramnios → pulmonary hypoplasia and chronic urinary stasis → CKD/ESRD as further downstream cascades.

**Cell types and biological processes involved (suggested ontology terms — verify via OAK before KB use):**
- **Cell types:** bladder detrusor smooth muscle cell, ureteral smooth muscle cell, urothelial cell, gubernacular mesenchymal cell, prostatic epithelial/stromal cell, myofibroblast (fibrotic remodeling)
- **Biological processes (GO):** smooth muscle contraction (GO:0006939), detection of mechanical stimulus involved in smooth muscle contraction, acetylcholine receptor signaling pathway, actin cytoskeleton organization, extracellular matrix organization / collagen fibril organization (fibrotic remodeling), testis descent

**Protein dysfunction:**
- CHRM3 — loss-of-function/truncation → reduced/absent G-protein-coupled muscarinic signaling in detrusor smooth muscle.
- PIEZO1 — loss-of-function → reduced pressure-induced channel open probability (mechanosensation failure), rescuable in vitro by the small-molecule PIEZO1 agonist Yoda1 (PMID:38184690).
- FLNA — altered mechanosensing scaffold function; PBS-associated variants enhance binding to β1-integrin cytoplasmic tails within the Ig19–21 stretch-sensing region, implying a gain- or altered-function mechanotransduction defect rather than simple loss of protein (PMID:32085749).

**Metabolic changes:** Not a primary feature; secondary uremic metabolic derangement occurs in advanced CKD/ESRD.

**Immune system involvement:** Not a primary immune-mediated disorder; recurrent UTI (in ~80% of patients) reflects urinary stasis/reflux rather than primary immunodeficiency.

**Tissue damage mechanisms:** Progressive fibrous/collagen replacement of smooth muscle (a fibrotic remodeling process) in bladder and ureter walls is the dominant tissue-level pathology; renal parenchymal damage arises from dysplasia (primary) plus obstructive/refluxive/infectious injury (secondary).

**Biochemical abnormalities:** Loss-of-function of the M3 muscarinic acetylcholine receptor and PIEZO1 mechanosensitive cation channel are the two best-characterized molecular lesions.

**Molecular/omics profiling:** No large-scale transcriptomic, proteomic, or single-cell atlas data specific to human PBS bladder tissue were identified in this search; the field currently relies on candidate-gene sequencing (WES/WGS in trios/families) and functional electrophysiology (patch-clamp of mutant PIEZO1 channels) rather than omics profiling. A 2023 whole-genome-sequencing study broadened the search for visceral myopathy genes including PBS (PMC10241726) but a comprehensive human PBS-tissue omics dataset does not appear to exist yet — **flag as a knowledge gap**.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** urinary bladder, ureters, kidneys, prostate, testes, abdominal wall musculature
- **Secondary/associated:** lungs (pulmonary hypoplasia), heart (PDA/VSD/ASD/TOF), gastrointestinal tract (malrotation, atresia, anorectal anomalies, Hirschsprung disease), musculoskeletal system (spine, hips, feet)
- **Body systems involved:** genitourinary, musculoskeletal (abdominal wall + skeleton), respiratory, cardiovascular, digestive

**Tissue/cell level:**
- Detrusor and ureteral smooth muscle (progressively replaced by fibrous/collagenous tissue), urothelium, renal parenchyma (dysplastic), prostatic stroma/epithelium, abdominal wall skeletal muscle (deficient/absent), skin/subcutis (redundant, wrinkled), testicular germinal epithelium (cryptorchid, at risk for impaired spermatogenesis)
- Suggested Cell Ontology terms (verify via OAK): smooth muscle cell of detrusor, smooth muscle cell of ureter, urothelial cell, skeletal muscle fiber, myofibroblast

**Subcellular level:** No PBS-specific subcellular/organelle pathology beyond cytoskeletal/membrane-receptor dysfunction (plasma membrane muscarinic receptor for CHRM3; plasma membrane mechanosensitive channel for PIEZO1; actin cytoskeleton/cortical scaffold for FLNA). Suggested GO Cellular Component terms: plasma membrane (GO:0005886), actin cytoskeleton (GO:0015629).

**Localization (UBERON — suggest, verify via OAK):** urinary bladder (UBERON:0001255), ureter (UBERON:0000056), kidney (UBERON:0002113), prostate gland (UBERON:0002367), testis (UBERON:0000473), abdominal wall / rectus abdominis (UBERON structures), lung (UBERON:0002048).

**Lateralization:** Bilateral in the defining features (bilateral cryptorchidism, bilateral hydroureteronephrosis); renal dysplasia severity can be asymmetric between kidneys, and unilateral vs. bilateral abnormal-kidney status is itself a documented prognostic factor (bilateral abnormal kidneys = worse prognosis) (StatPearls NBK544248).

---

## 8. Temporal Development

**Onset:** Congenital in essentially all cases; detectable on second-trimester prenatal ultrasound in many cases (distended bladder, dilated ureters, hydronephrosis, deficient abdominal wall echogenicity), with earlier (first-trimester) detection reported in some cases (PMC3784146).

**Onset pattern:** The structural anomalies are present from early-to-mid gestation (insidious in utero development rather than acute); clinical presentation at birth can range from an asymptomatic wrinkled abdomen to severe respiratory distress from pulmonary hypoplasia.

**Progression / disease stages — Woodard/clinical severity classification (three categories):**
- **Category I (~20%):** Severe renal dysplasia → oligohydramnios → severe pulmonary hypoplasia (Potter-sequence-like); most affected infants are stillborn or die within days of birth.
- **Category II (~40%):** Full triad present; renal function may be adequate at birth but is at risk of progressive deterioration over childhood; pulmonary function is typically normal.
- **Category III (~40%):** Incomplete/mild triad features; well-maintained renal function; no pulmonary insufficiency; generally good long-term prognosis, "near normal life."

This has been operationalized into a validated quantitative severity score (RUBACE) correlating with Woodard category (PMID:30113772).

**Progression rate/course pattern:** Variable — from rapidly fatal (Category I, days) to chronic/lifelong with slow renal functional decline over years-to-decades (Category II/III). Renal replacement therapy in PBS, when needed, begins at a younger median age (7.0 years) than in other congenital obstructive uropathies (9.6 years), implying a somewhat faster renal decline trajectory in the subset that does progress (PMID:28779237).

**Disease duration:** Lifelong for survivors; not self-limited, though the urologic manifestations can be surgically/medically managed rather than "cured."

**Remission patterns:** Not applicable in the classic sense; surgical/urologic management (vesicostomy, ureteral reimplantation, abdominoplasty, orchiopexy) improves function and cosmesis but does not reverse the underlying structural/muscular deficiency.

**Critical periods / windows for intervention:**
- **Prenatal:** vesicoamniotic shunting in carefully selected fetuses (normal karyotype, no other major malformations, preserved renal function by fetal urine electrolyte analysis) may reduce oligohydramnios-driven pulmonary hypoplasia and renal dysplasia (PMID:30018947).
- **~6 months of age:** the recommended window for orchiopexy (to optimize fertility potential and reduce malignancy risk from prolonged cryptorchidism), often combined with abdominoplasty.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** contemporary estimates 3.6–3.8 per 100,000 live male births; alternative/older estimates cite 1 in 29,000–50,000 live births overall, or roughly 1 in 35,000–40,000 births.
- **Prevalence:** Orphanet classifies PBS as an ultra-rare/rare disease (specific point-prevalence banding not separately retrieved in this search — recommend confirming via the Orphanet ORPHA:2970 epidemiology table directly, e.g., with `just fetch-reference ORPHA:2970`).

**Inheritance pattern:** For the minority of genetically solved cases: **autosomal recessive** (CHRM3-related, in consanguineous or biallelic-variant families) is the best-established Mendelian pattern; an **X-linked** mechanism has now been proposed via FLNA hemizygous variants in surviving adult males, which would be consistent with (though not fully explanatory of) the strong male bias (PMID:32085749). The great majority of sporadic PBS cases have no identified Mendelian cause, and multifactorial/non-genetic (mechanical, epigenetic) contributions are documented (see Section 2).

**Penetrance / expressivity:** Highly variable expressivity is a hallmark of PBS — even within the same CHRM3-mutant family, phenotype severity varied among six affected brothers; and the disease spectrum spans neonatal lethality to normal adult life (Woodard Categories I–III), indicating incomplete/variable expressivity even for a shared genetic lesion.

**Genetic anticipation:** Not reported/applicable (no repeat-expansion mechanism identified).

**Germline mosaicism:** Not specifically documented in the sources reviewed.

**Founder effects:** Not established; most reported causal variants are private to individual consanguineous families (e.g., the Turkish CHRM3 kindred) rather than population founder alleles.

**Consanguinity:** A significant contributor in the autosomal recessive (CHRM3) cases specifically — the original CHRM3 kindred was a consanguineous Turkish family.

**Carrier frequency:** Not established (variants are private/family-specific; no population carrier-frequency data identified).

**Population demographics:**
- **Sex ratio:** ~95–97% male; females represent <5% of cases and, when affected, typically present with the urinary tract/abdominal wall findings without gonadal involvement (since there are no testes to be cryptorchid).
- **Race/ethnicity:** reported roughly twice as common in Black vs. White populations in some U.S. clinical series (source synthesis, not independently re-verified against a primary epidemiologic study in this search pass — flag for confirmation).
- **Twinning:** ~4× higher incidence in twin gestations vs. singletons.
- **Maternal age:** younger maternal age associated with higher incidence.
- **Geographic distribution:** No endemic geographic clustering identified; case reports span multiple continents (e.g., Sudan, Cameroon, Somalia case series retrieved in this search), consistent with a globally distributed rare congenital disorder rather than a population-specific one.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Serum creatinine and renal function panel — nadir serum creatinine <0.7 mg/dL in the first year of life is a favorable prognostic marker; creatinine >0.7 mg/dL is an adverse prognostic factor (StatPearls NBK544248).
- Urinalysis/urine culture (recurrent UTI monitoring).

**Imaging:**
- **Prenatal ultrasound** (2nd trimester, occasionally 1st trimester): distended fetal bladder (megacystis), dilated ureters, hydronephrosis, oligohydramnios, deficient abdominal wall musculature/echogenicity.
- **Postnatal renal/bladder ultrasound:** assessment of hydroureteronephrosis severity, bladder wall/capacity, renal parenchymal echogenicity (dysplasia).
- **Voiding cystourethrogram (VCUG):** evaluates vesicoureteral reflux, bladder neck/urethral anomalies (including a dilated prostatic urethra).
- **Chest radiography:** assessment for pulmonary hypoplasia.
- **Echocardiography:** screening for the ~25% rate of cardiac anomalies.
- **Abdominal imaging:** screening for GI anomalies (malrotation etc.).

**Functional tests:**
- **Urodynamic studies:** demonstrate poor/absent detrusor contractility (detrusor hyporeflexia/acontractility).
- **Fetal urine electrolyte/biochemistry analysis:** used to assess fetal renal function prior to considering vesicoamniotic shunting (a normal fetal urine chemistry profile is one of the stated prerequisites for shunt candidacy).

**Genetic testing:**
- No consensus single-gene or panel test is standard given how few cases are genetically solved; when pursued, **whole-exome or whole-genome sequencing** is the most informative approach (as used to identify PIEZO1 and FLNA variants), given extensive genetic heterogeneity and the very low yield of any single candidate gene.
- Targeted **CHRM3** sequencing may be considered specifically in consanguineous families or those with an associated impaired pupillary light reflex.
- **Karyotype/chromosomal microarray** is reasonable to exclude aneuploidy/CNV causes (e.g., the reported 16p11.2 duplication) and is also a prerequisite check before offering fetal intervention (vesicoamniotic shunting requires a normal karyotype).

**Clinical diagnostic criteria:** PBS is a clinical/radiologic diagnosis based on the triad (deficient abdominal wall musculature + urinary tract dilation with poor contractility + cryptorchidism in males); no formal consensus scoring system exists for diagnosis itself, though the RUBACE score (PMID:30113772) is used for severity grading once diagnosed.

**Differential diagnosis:**
- **"Pseudo-prune belly syndrome"** — urinary tract findings identical to PBS but with normal testicular position and/or normal (or near-normal) abdominal wall musculature; overlaps clinically with megacystis-megaureter syndrome.
- **Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome (MMIHS)** — shares megacystis, hydronephrosis, and abdominal wall laxity but is distinguished by microcolon and intestinal hypoperistalsis without mechanical obstruction; MMIHS and PBS have been reported within the same family, suggesting a possible shared/overlapping pathogenetic mechanism (visceral myopathy spectrum) (PMC4420383; PMID:15289943).
- Hirschsprung disease and chronic intestinal pseudo-obstruction are additional considerations in neonates presenting with abdominal distension and failure to pass meconium.

**Screening:** No population-based newborn or carrier screening program exists for PBS given its sporadic/heterogeneous genetic basis; case-by-case prenatal ultrasound detection is the primary "screening" modality.

---

## 11. Outcome/Prognosis

**Survival/mortality:**
- **Perinatal mortality:** 10–25% in contemporary series (older series report rates as high as 60% before modern neonatal/urologic management); mortality correlates directly with pulmonary hypoplasia severity.
- ~40% of PBS infants are born prematurely, and nearly half require mechanical ventilation at birth.
- **Renal-replacement-therapy population 10-year survival:** 85% for PBS vs. 94% for congenital obstructive uropathy and 91% for renal hypoplasia/dysplasia — i.e., PBS patients who reach ESRD have somewhat worse long-term survival than other congenital urologic ESRD etiologies (PMID:28779237).

**Morbidity/renal function:**
- ~30% of survivors develop chronic renal insufficiency or ESRD during childhood/adolescence and may require renal transplantation.
- In an adult PBS cohort, roughly 50% had normal eGFR, 20% mild renal impairment, and 30% moderate renal impairment.
- Patients with the mildest urinary tract involvement (no true obstruction) can have normal life expectancy.

**Complications:** Recurrent UTI (~80% of patients), constipation (impaired Valsalva from abdominal wall deficiency), progressive CKD/ESRD, and the complications of associated cardiac/GI/musculoskeletal anomalies.

**Recovery/functional potential:** Historically (pre-1992), males with PBS were considered universally infertile; with modern management, several men with PBS have fathered children naturally, though fertility remains reduced overall (attributed to cryptorchidism-related impaired spermatogenesis; libido and orgasmic function are typically normal, but retrograde ejaculation is common). Female fertility appears largely preserved, with documented successful pregnancy/vaginal delivery case reports.

**Prognostic factors:**
- Favorable: at least one normal-appearing kidney on ultrasound; nadir serum creatinine <0.7 mg/dL in year 1 of life; Woodard Category III disease.
- Unfavorable: bilateral abnormal kidneys, nadir creatinine >0.7 mg/dL, history of pyelonephritis, Woodard Category I disease (severe renal dysplasia + pulmonary hypoplasia).

**Prognostic biomarkers:** Serum creatinine trajectory in infancy is the best-established simple prognostic biomarker; the RUBACE composite severity score is a validated multidimensional prognostic tool (PMID:30113772).

---

## 12. Treatment

**Pharmacotherapy:**
- Prophylactic antibiotics to reduce UTI risk (given the ~80% lifetime UTI rate).
- Antibiotic coverage before any urinary tract instrumentation/manipulation.
- No disease-modifying pharmacotherapy currently exists for the underlying smooth-muscle contractility defect; suggested MAXO term: MAXO:0000647-adjacent pharmacotherapy concepts do not directly apply (chemotherapy), so use **NCIT:C15986 (Pharmacotherapy)** generically for antibiotic prophylaxis with a `therapeutic_agent` slot for the specific antibiotic class used.

**Advanced/experimental therapeutics:**
- **PIEZO1 agonism (Yoda1):** an in-vitro proof-of-concept finding — Yoda1 rescued the channel-gating (NPo) defect of PBS-associated PIEZO1 mutant channels, nominating a potential future small-molecule pharmacologic strategy specific to PIEZO1-associated PBS (PMID:38184690). This is preclinical/in vitro only — no human trials identified.
- No gene therapy, cell therapy, RNA-based therapy, or immunotherapy approaches for PBS were identified in this search (consistent with its status as a structural/developmental syndrome rather than a targetable single-pathway disease at present).

**Surgical/interventional (the mainstay of management):**
- **Prenatal vesicoamniotic shunting:** in carefully selected fetuses (normal karyotype, no other major malformations, preserved fetal renal function by serial urine biochemistry) to relieve bladder distension, potentially reducing oligohydramnios-driven pulmonary hypoplasia and renal dysplasia; outcomes remain "controversial" and shunting benefits a *subset* of patients rather than all (PMID:30018947 — suggested MAXO term: could map to a fetal surgical intervention MAXO/NCIT surgical-procedure term, verify via OAK).
- **Cutaneous vesicostomy:** temporizing bladder drainage in infancy while awaiting growth for more definitive reconstruction.
- **Orchiopexy** (bilateral): recommended at ~6 months of age to optimize fertility potential and reduce malignancy risk of prolonged cryptorchidism; laparoscopic orchiopexy with spermatic vessel preservation is now the preferred modality.
- **Urinary tract reconstruction** (ureteral reimplantation/tailoring): generally reserved for patients with recurrent febrile UTIs or progressive renal deterioration rather than performed prophylactically in all patients.
- **Abdominoplasty (abdominal wall reconstruction):** often performed concurrently with orchiopexy or urinary reconstruction; beyond cosmesis, may improve effective Valsalva-assisted bladder emptying by restoring abdominal wall tone.
- Suggested MAXO terms: MAXO:0000004 (surgical procedure) as a generic parent; more specific NCIT surgical-procedure terms for vesicostomy, orchiopexy, and abdominoplasty should be looked up via OAK/NCIT search before KB entry.

**Supportive/rehabilitative care:**
- Management of constipation (from impaired Valsalva).
- Long-term multidisciplinary follow-up: neonatology, pediatric urology, nephrology, cardiology, orthopedics, pulmonology — reflecting the multisystem nature of associated anomalies.

**Renal replacement therapy:** Hemodialysis or peritoneal dialysis followed by renal transplantation for the ~30% of patients progressing to ESRD; multiple renal transplants have been reported in individual PBS patients over a lifetime (e.g., a reported third renal transplant case, PMC8720038).

**Treatment outcomes:** Contemporary multidisciplinary management (prenatal detection, selective shunting, staged surgery) is associated with improved survival compared to historical cohorts, though vesicoamniotic shunting benefits only a defined subset of patients meeting strict candidacy criteria.

**Treatment strategy/algorithm:** Broadly staged as (1) prenatal risk stratification ± shunting, (2) neonatal stabilization (respiratory support for pulmonary hypoplasia, temporizing urinary drainage if needed), (3) infancy: orchiopexy ± abdominoplasty around 6 months, (4) individualized decision for urinary tract reconstruction based on UTI/renal-function trajectory, and (5) lifelong nephrology/urology surveillance with renal replacement therapy as needed.

---

## 13. Prevention

- **Primary prevention:** None established — PBS arises from a largely non-preventable congenital developmental/genetic mechanism; no modifiable maternal exposure has been definitively identified as causal (see Section 2), so no specific primary-prevention intervention (vaccination, risk-factor modification) is applicable.
- **Secondary prevention (early detection):** Routine second-trimester (and occasionally first-trimester) obstetric ultrasound serves as the practical secondary-prevention/early-detection tool, enabling risk stratification and consideration of vesicoamniotic shunting in candidate fetuses to mitigate oligohydramnios-driven pulmonary hypoplasia and renal dysplasia.
- **Genetic counseling:** Recommended for families with a CHRM3-associated (autosomal recessive) case, particularly in consanguineous unions, given the demonstrated recurrence in siblings in the original Turkish kindred; recurrence-risk counseling for sporadic (non-Mendelian) cases should emphasize the current uncertainty around inheritance given genetic heterogeneity and documented MZ twin discordance.
- **Prenatal genetic testing:** Karyotype/chromosomal microarray is advisable in a prenatally suspected case to exclude CNV etiologies (e.g., 16p11.2 duplication) and is also a prerequisite for vesicoamniotic shunt candidacy.
- **Tertiary prevention:** Prophylactic antibiotics and elective circumcision are used to reduce UTI risk/complications in diagnosed infants; timely orchiopexy (~6 months) is a tertiary-prevention measure against infertility and testicular malignancy risk from prolonged cryptorchidism; proactive nephrology surveillance aims to prevent/delay progression to ESRD.
- **Public health / behavioral interventions:** Not applicable in the traditional sense (not an infectious or lifestyle-driven disease).

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease in other species:** No robust literature on spontaneously occurring "prune belly syndrome" as a natural veterinary disease entity was identified in this search (unlike, e.g., some other congenital urologic malformations catalogued in OMIA). This appears to be a knowledge gap / absence of documented natural-disease analogs rather than an established negative finding — recommend a targeted OMIA search before concluding no comparative natural disease exists.
- **Comparative/evolutionary biology:** The core molecular players (CHRM3, PIEZO1, FLNA) are highly conserved across mammals, which is precisely why the mouse *Chrm3*-null model phenocopies the human bladder phenotype (see Section 15) — this supports deep evolutionary conservation of the underlying bladder-smooth-muscle contractile/mechanotransduction pathway rather than species-specific natural disease per se.
- **Zoonotic potential / transmission:** Not applicable — PBS is a non-infectious congenital developmental disorder.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*) — Chrm3 knockout:** The *Chrm3*-null mouse develops a megabladder phenotype (detrusor hyporeflexia, distended bladder) that "strikingly phenocopies" the human CHRM3-mutant PBS/urinary-bladder-disease phenotype, providing strong causal/functional validation of CHRM3 loss-of-function as a bladder-specific PBS mechanism (cited in PMID:22077972 and subsequent CHRM3 literature). This is a genetic (constitutive knockout) model.
- **In vitro/heterologous expression systems — PIEZO1 electrophysiology:** Patch-clamp recordings of wild-type vs. PBS-patient-derived mutant PIEZO1 channels expressed heterologously demonstrated the pressure-induced open-probability (NPo) defect, and the small-molecule PIEZO1 agonist Yoda1 rescued channel function — an induced/pharmacological cellular model rather than a whole-organism model (PMID:38184690).
- **Model limitations:** The existing models (Chrm3-null mouse; heterologous PIEZO1 channel expression) recapitulate the bladder-smooth-muscle contractile/mechanosensory defect specifically, but **do not model the full multisystem PBS phenotype** (abdominal wall muscle deficiency, cryptorchidism, associated cardiac/GI/skeletal anomalies) — this is a significant translational gap, since it remains unresolved whether the same primary lesion mechanistically produces the abdominal-wall and gonadal phenotypes, or whether these require a separate (mesenchymal-patterning) mechanism acting in parallel. This would be an appropriate candidate for a `HUMAN_MODEL_MISMATCH`-type knowledge-gap annotation if this disease is curated into the dismech KB, given that current animal/cellular models validate only the urinary-tract component of the triad.
- **No FLNA-mutant PBS-specific mouse model** was identified in this search (the FLNA PBS report is a human-genetics case series without an accompanying animal model).
- **Resources:** MGI (Mouse Genome Informatics) would be the primary resource to confirm/locate the specific *Chrm3* knockout allele(s) used; not independently queried in this pass.

---

## Summary of Key Evidence Gaps (for curation planning)

1. **Genetic architecture is largely unsolved** — CHRM3, PIEZO1, FLNA, HNF1B, ACTA2/ACTG2, STIM1 collectively explain only a small minority of cases; the majority of PBS (especially sporadic, non-consanguineous cases) has no identified molecular cause.
2. **No unifying mechanism yet connects the bladder-smooth-muscle molecular lesions to the abdominal-wall and testicular-descent components of the triad** — an explicit `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP` candidate.
3. **No dedicated human PBS-tissue omics dataset** (transcriptomic/proteomic/single-cell) was located.
4. **The X-linked/FLNA hypothesis for the strong male predominance is recent (2020) and not yet independently replicated at scale.**
5. **PIEZO1-Yoda1 rescue is an in-vitro finding only** — no in vivo or human therapeutic data yet.
6. Overlap with MMIHS (shared family reports) suggests a broader "visceral myopathy" spectrum that could be modeled as a dismech grouping if multiple related entries (PBS, MMIHS, megacystis-megaureter syndrome) are curated.

---

## Sources

- [OMIM #100100 — Prune Belly Syndrome](https://omim.org/entry/100100) / [Clinical Synopsis](https://www.omim.org/clinicalSynopsis/100100)
- [OMIM *118494 — CHRM3](https://www.omim.org/entry/118494)
- [NORD — Prune Belly Syndrome](https://rarediseases.org/rare-diseases/prune-belly-syndrome/)
- [GARD — Prune belly syndrome](https://rarediseases.info.nih.gov/diseases/7479/prune-belly-syndrome)
- [StatPearls — Prune Belly Syndrome (NBK544248)](https://www.ncbi.nlm.nih.gov/books/NBK544248/)
- Weber S, et al. "Muscarinic Acetylcholine Receptor M3 Mutation Causes Urinary Bladder Disease and a Prune-Belly-like Syndrome." *Am J Hum Genet.* 2011;89(5):668-74. PMID: [22077972](https://pubmed.ncbi.nlm.nih.gov/22077972/) — [PMC3213389](https://pmc.ncbi.nlm.nih.gov/articles/PMC3213389/)
- Beaman GM, et al. "A homozygous missense variant in CHRM3 associated with familial urinary bladder disease." *Clin Genet.* 2019;96(6):515-520. PMID: [31441039](https://pubmed.ncbi.nlm.nih.gov/31441039/) — [PMC6899476](https://pmc.ncbi.nlm.nih.gov/articles/PMC6899476/)
- "PIEZO1 loss-of-function compound heterozygous mutations in the rare congenital human disorder Prune Belly Syndrome." *Nat Commun.* 2024. PMID: [38184690](https://pubmed.ncbi.nlm.nih.gov/38184690/) — [PMC10771463](https://pmc.ncbi.nlm.nih.gov/articles/PMC10771463/)
- Iqbal NS, Jascur TA, Harrison SM, et al. "Prune belly syndrome in surviving males can be caused by Hemizygous missense mutations in the X-linked Filamin A gene." *BMC Med Genet.* 2020;21:38. PMID: [32085749](https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-020-0973-x) — [PMC7035669](https://pmc.ncbi.nlm.nih.gov/articles/PMC7035669/)
- "Genetic Basis of Prune Belly Syndrome: Screening for HNF1β Gene." *J Urol.* 2012. PMID: [22114815](https://pubmed.ncbi.nlm.nih.gov/22114815/)
- "Congenital mydriasis and prune belly syndrome in a child with an ACTA2 mutation." PMID: [24998021](https://pubmed.ncbi.nlm.nih.gov/24998021/)
- Wong et al. "Phenotypic severity scoring system and categorisation for prune belly syndrome: application to a pilot cohort of 50 living patients." *BJU Int.* 2019. PMID: [30113772](https://pubmed.ncbi.nlm.nih.gov/30113772/) — [PMC7368761](https://pmc.ncbi.nlm.nih.gov/articles/PMC7368761/)
- Yalcinkaya F, Bonthuis M, Erdogan BD, et al. "Outcomes of renal replacement therapy in boys with prune belly syndrome: findings from the ESPN/ERA-EDTA Registry." *Pediatr Nephrol.* 2017;33(1):117-124. PMID: [28779237](https://pmc.ncbi.nlm.nih.gov/articles/PMC5700229/)
- White JT, Sheth KR, Bilgutay AN, et al. "Vesicoamniotic Shunting Improves Outcomes in a Subset of Prune Belly Syndrome Patients at a Single Tertiary Center." *Front Pediatr.* 2018;6:180. PMID: [30018947](https://pmc.ncbi.nlm.nih.gov/articles/PMC6038357/)
- [Case Report: Novel Copy Number Variant 16p11.2 Duplication Associated With Prune Belly Syndrome (PMC8496350)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8496350/)
- [Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome Associated With Prune Belly Syndrome: A Case Report (PMC4420383)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4420383/)
- ["Megacystis-microcolon-intestinal hypoperistalsis and prune belly: overlapping syndromes" (PMID:15289943)](https://pubmed.ncbi.nlm.nih.gov/15289943/)
- ["Transient Fetal Hydrops and Prune Belly in One Identical Female Twin" — NEJM 1983](https://www.nejm.org/doi/abs/10.1056/NEJM198302033080505)
- ["Prune Belly Syndrome in a Female Newborn following In Vitro Fertilization-Induced Pregnancy" (PMC10700981)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10700981/)
- [Third Renal Transplant in a Patient With Prune Belly Syndrome (PMC8720038)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8720038/)
- [Prune belly syndrome — Wikipedia](https://en.wikipedia.org/wiki/Prune_belly_syndrome)
- [ICD-10-CM Q79.4 — Prune belly syndrome](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q65-Q79/Q79-/Q79.4)
- Medscape — [Prune Belly Syndrome: Practice Essentials, Pathophysiology](https://emedicine.medscape.com/article/447619-overview) and [Treatment & Management](https://emedicine.medscape.com/article/447619-treatment)

**Note on ontology terms:** Per this project's anti-hallucination policy, every HP/GO/CL/UBERON/CHEBI/MAXO/NCIT term suggested above is a *candidate* only and must be independently verified with OAK (`runoak -i sqlite:obo:<ontology> info <ID>`) for exact label match before being written into any `kb/disorders/` YAML entry.