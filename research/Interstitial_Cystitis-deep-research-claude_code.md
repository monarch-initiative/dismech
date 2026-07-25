---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-24T23:52:31.260693'
end_time: '2026-07-24T23:56:51.781473'
duration_seconds: 260.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Interstitial Cystitis
  mondo_id: MONDO:0018301
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
  web_search_requests: 21
  num_turns: 23
  total_cost_usd: 1.7875107000000001
  session_id: c65283f3-d64a-5c13-badf-57aca92d1874
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Interstitial Cystitis
- **MONDO ID:** MONDO:0018301 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Interstitial Cystitis** covering all of the
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

# Interstitial Cystitis / Bladder Pain Syndrome (IC/BPS) — Comprehensive Research Report

---

## 1. Disease Information

**Overview:** Interstitial cystitis/bladder pain syndrome (IC/BPS) is a chronic, non-infectious bladder disorder characterized by pelvic/bladder pain perceived as related to the urinary bladder, accompanied by at least one other urinary symptom (urgency and/or frequency), lasting more than 6 weeks, in the absence of infection or other identifiable causes (AUA definition). It is now understood as a heterogeneous syndrome that intersects with overactive bladder (OAB) and encompasses at least two distinct histologic/clinical phenotypes: **Hunner-lesion (classic/ulcerative) IC (HIC)** and **non-Hunner-lesion IC/BPS (NHIC)**.

**Key identifiers:**
- **MONDO:** MONDO:0018301
- **Orphanet:** ORPHA:37202
- **ICD-10-CM:** N30.1 (interstitial cystitis; N30.10 without hematuria, N30.11 with hematuria)
- **ICD-11:** GC00.3
- **OMIM:** No dedicated OMIM entry exists (IC/BPS is not classified as a single-gene Mendelian disorder), though a subset of patients carry rare pathogenic variants in Mendelian desquamating-skin-disorder genes (see §4)
- **MeSH:** D018856 (Cystitis, Interstitial)

**Synonyms:** Bladder pain syndrome (BPS); painful bladder syndrome (PBS); hypersensitive bladder syndrome (Japan/Asia terminology); chronic pelvic pain syndrome (overlapping, male-predominant terminology); Hunner's disease/Hunner ulcer disease (for the classic ulcerative subtype).

**Evidence base:** Predominantly aggregated disease-level literature — case series, cystoscopic/histopathologic cohorts, multicenter epidemiologic surveys (RAND RICE study), the NIH-funded MAPP (Multidisciplinary Approach to the Study of Chronic Pelvic Pain) Research Network, and a small but growing number of GWAS/exome-sequencing cohorts. There is no large-scale EHR biobank specific to IC/BPS to date.

---

## 2. Etiology

### Disease Causal Factors
IC/BPS is considered a **multifactorial syndrome** rather than a single-etiology disease, with several non-mutually-exclusive mechanistic hypotheses converging on bladder-wall injury and pain: (1) urothelial/glycosaminoglycan (GAG) barrier dysfunction permitting urinary solute leak, (2) mast cell activation and neurogenic inflammation, (3) autoimmune/antigen-driven chronic inflammation (particularly in Hunner-lesion disease), (4) occult or antecedent infection triggering persistent inflammation, and (5) central/peripheral neural sensitization producing pain independent of ongoing peripheral pathology (PMC9736130).

### Genetic Risk Factors
- **HLA/MHC locus (Hunner-type IC):** A Japanese GWAS of Hunner-type IC identified genome-wide significant association at **rs1794275** in the MHC region on chromosome 6p21.3 (OR = 2.32). Fine-mapping implicated **HLA-DQβ1** amino acid positions 71, 74, 75 (OR = 1.94) and **HLA-DPβ1** position 178, tagging **HLA-DPB1\*04:02** (OR = 2.35) — all located at the peptide-binding groove, supporting an antigen-presentation/autoimmune mechanism specific to the Hunner-lesion phenotype (Maeda et al., *Cell Reports Medicine* 2023; PMID:37467720).
- **Rare/ultra-rare variants (exome sequencing, all-phenotype IC/BPS):** A 2025 case-control exome study (348 IC/BPS cases vs. 11,981 controls) extended prior associations with **ATP2C1** and **ATP2A2** — genes causing the Mendelian desquamating skin disorders Hailey-Hailey disease and Darier disease, respectively — and nominated **SIX5** as a candidate gene. Increased burden of rare *ATP2C1* variants was found via SKAT analysis; pathway enrichment implicated the anaphase-promoting-complex-dependent catabolic process, MAPK cascade regulation, and integrin binding (medRxiv/PMC12933612, PMID:40034785).
- **Mendelian-disorder enrichment:** A separate cohort study found an enrichment of clinically recognized Mendelian connective-tissue/desquamation disorders among IC/BPS patients relative to expected population rates (PMC10000272), consistent with a shared epithelial-barrier vulnerability.
- No single Mendelian causal gene has been established; inheritance is best modeled as **polygenic/complex** with population-specific risk alleles (the HLA association above being specific to the Japanese Hunner-type cohort; replication in other ancestries is limited).

### Environmental / Lifestyle Risk Factors
- Prior **urinary tract infection** history is commonly reported preceding symptom onset (mechanistically linked to GAG-layer disruption).
- **Dietary bladder irritants**: caffeine (coffee — both regular and decaffeinated, due to high acidity), alcohol, carbonated beverages, citrus fruits/juices, spicy foods, artificial sweeteners, and MSG are widely reported symptom triggers; in one series, 97% of patients reported symptom worsening with specific foods/drinks (PMC11474411; ichelp.org).
- Female sex, with symptom fluctuation across the menstrual cycle and reported remission in some patients during the 2nd–3rd trimester of pregnancy, supporting hormonal/immune modulation of disease activity.
- Pelvic floor trauma/surgery, and comorbid chronic pelvic pain conditions, are recognized clinical risk correlates.

### Protective Factors
No well-validated genetic protective variants have been reported. Dietary elimination of trigger foods is the best-documented modifiable protective/symptom-reducing intervention (up to 80% symptom reduction reported with elimination diets in observational series).

### Gene-Environment Interactions
The leading hypothesis links a genetically determined (HLA-mediated antigen-presentation, or epithelial-barrier-gene) susceptibility to an environmental trigger (infection, mechanical/chemical injury) that breaches the urothelial GAG barrier, initiating a self-sustaining cycle of mast-cell activation, neurogenic inflammation, and (in a subset) autoimmune pancystitis. Formal gene-by-environment interaction studies specific to IC/BPS are lacking in the literature reviewed.

---

## 3. Phenotypes

IC/BPS phenotypes span symptom, sign, and (for the Hunner subtype) histopathologic domains.

| Phenotype | Type | Frequency / Notes | Suggested HPO term |
|---|---|---|---|
| Suprapubic/pelvic pain related to bladder filling, relieved by voiding | Symptom | Core diagnostic criterion | HP:0030826 (Pelvic pain) / HP:0100518 (Dysuria, related) |
| Urinary urgency | Symptom | Core diagnostic criterion | HP:0100518 is dysuria; urgency best mapped HP:0032637 (Urinary urgency) |
| Urinary frequency (daytime) | Symptom | Core diagnostic criterion; often >8 voids/day | HP:0100515 (Polyuria, adjacent) — closer: HP:0000012 (Urinary frequency) |
| Nocturia | Symptom | Very common | HP:0033795 (Nocturia) |
| Dyspareunia / pain with sexual activity | Symptom | Reported in a substantial minority, more common with comorbid vulvodynia | HP:0030214 (Dyspareunia) |
| Hunner lesion (mucosal ulceration/erythematous patch with vessel disruption) | Clinical sign (cystoscopic) | Present in ~5–20% of clinically diagnosed IC/BPS cohorts (varies by referral pattern); defines the HIC subtype | — (procedural finding, not classically HPO-coded) |
| Glomerulations (post-hydrodistension petechial hemorrhages) | Clinical sign (cystoscopic) | Nonspecific; seen in both HIC and NHIC, and in asymptomatic controls after distension — AUA guideline states glomerulations are not required for diagnosis | — |
| Reduced bladder capacity under anesthesia | Clinical/functional sign | More pronounced in HIC | HP:0025144 (Reduced bladder capacity, if modeled) |
| Epithelial denudation / thinning | Histopathologic | Common finding on bladder biopsy, especially HIC | — |
| Subepithelial/detrusor mastocytosis | Histopathologic (laboratory) | Elevated mast cell density; central pathophysiologic finding | — |
| Lymphoplasmacytic infiltration (pancystitis) | Histopathologic | Substantial infiltration (≥200 cells/mm²) in 93% of HIC vs. 8% of NHIC specimens (PMID:26587589) | — |
| Clonal B-cell expansion (light-chain restricted) | Laboratory/molecular | ~31% of HIC specimens (PMID:26587589) | — |

**Age of onset:** Most commonly diagnosed in the 4th–6th decade of life, though onset can occur from adolescence through old age; Hunner-lesion disease tends to present at an **older age of onset** than non-Hunner disease.

**Severity/progression:** Highly variable — "mild," "moderate," and "severe" symptom tiers are used clinically (O'Leary-Sant ICSI/ICPI scoring), but the disease is not staged formally like cancer. Course is typically **fluctuating/relapsing-remitting** with flares and remissions rather than uniformly progressive (see §8).

**Quality of life impact:** IC/BPS carries a substantial QoL burden comparable to or exceeding other chronic pain conditions, with impacts on sleep (nocturia-driven), sexual function, work productivity, and mental health (elevated depression/anxiety prevalence). The **O'Leary-Sant Interstitial Cystitis Symptom Index (ICSI)** and **Problem Index (ICPI)** are the most widely used disease-specific PRO tools; a 5-point ICSI reduction is considered the minimal clinically important difference (PMC9300131).

---

## 4. Genetic/Molecular Information

- **Causal genes:** No single Mendelian causal gene. IC/BPS is best modeled as a complex trait with contributory rare and common variants (see §2).
- **Candidate/risk genes identified to date:**
  - **HLA-DQB1 / HLA-DPB1** (MHC class II) — common-variant/amino-acid association with Hunner-type IC specifically (PMID:37467720). HGNC: HLA-DQB1 (HGNC:4944), HLA-DPB1 (HGNC:4940).
  - **ATP2C1** (HGNC:13202) — rare-variant burden association; canonically causes Hailey-Hailey disease (benign familial pemphigus), a desquamating skin disorder affecting the SPCA1 Golgi Ca²⁺/Mn²⁺ ATPase.
  - **ATP2A2** (HGNC:812) — canonically causes Darier disease (SERCA2 ER Ca²⁺ ATPase); implicated as an IC/BPS candidate gene in exome analysis.
  - **SIX5** (HGNC:10891) — nominated candidate gene, myotonic-dystrophy-region homeobox transcription factor.
  - **FZD8** (Frizzled-8; HGNC:4045) — the antiproliferative factor (APF), a urinary biomarker specific to IC (see below), is a sialoglycopeptide with 100% peptide-sequence homology to the putative sixth transmembrane domain of the FZD8 receptor (PMID:15282374).
  - **CKAP4** (cytoskeleton-associated protein 4; HGNC:16147) — identified as the APF receptor; APF–CKAP4 binding underlies APF's antiproliferative signaling in bladder urothelium and is being developed as a diagnostic assay target.
- **Variant classification/allele frequency:** The implicated variants are predominantly rare, ultra-rare, or population-specific (Japanese cohort for the HLA finding); no ClinVar pathogenic/likely-pathogenic classifications exist specifically for "IC/BPS" as an indication, since these genes' primary disease associations are the Mendelian skin disorders. Allele-frequency data for the HLA risk haplotypes and ATP2C1/ATP2A2 rare variants should be queried in gnomAD/1000 Genomes on a variant-by-variant basis; the source studies report cohort-level burden rather than individual pathogenic-variant frequencies.
- **Somatic vs. germline:** All reported associations are **germline**.
- **Functional consequences:** ATP2C1/ATP2A2 loss-of-function is hypothesized to impair epithelial cell-cell adhesion and Ca²⁺-dependent desmosomal integrity, potentially extending a "leaky epithelial barrier" mechanism from skin to urothelium — mechanistically congruent with the GAG-layer/urothelial permeability hypothesis (§6).
- **Epigenetics:** No dedicated IC/BPS DNA methylation or histone-modification studies were identified in this search; this remains an evidence gap.
- **Chromosomal abnormalities:** None reported; IC/BPS is not associated with recurrent CNVs or aneuploidy.

---

## 5. Environmental Information

- **Environmental/toxin factors:** No specific industrial toxin or pollutant has been robustly linked to IC/BPS causation in the literature surveyed; this is an evidence gap relative to other bladder diseases (e.g., occupational carcinogen exposure in bladder cancer).
- **Lifestyle factors:** Dietary bladder irritants (caffeine, alcohol, acidic/citrus foods, carbonated beverages, spicy food, artificial sweeteners) are the best-characterized modifiable environmental factors, acting as symptom triggers/exacerbants rather than established initiating causes (PMC11474411).
- **Infectious agents:** No single pathogen has been confirmed as causal. Antecedent bacterial cystitis (culture-negative or culture-positive UTI) is a commonly reported trigger preceding symptom onset in patient histories, consistent with an infection-triggered, self-perpetuating urothelial injury/inflammation model, though a "final common pathogen" has not been identified and current IC/BPS is by definition non-infectious at diagnosis (routine urinalysis/urine culture must be negative to diagnose per AUA guideline).

---

## 6. Mechanism / Pathophysiology

IC/BPS pathophysiology is best understood as a **convergent, heterogeneous final-common-pathway syndrome** with at least two partially distinct mechanistic streams corresponding to the Hunner-lesion and non-Hunner phenotypes (PMID:31144757; einj.org pathomechanism review).

### Core causal chain (non-Hunner / urothelial-centric hypothesis)
1. **Trigger:** UTI, mechanical/chemical injury, or genetically determined epithelial vulnerability (e.g., ATP2C1/ATP2A2 hypofunction) → 
2. **Urothelial glycosaminoglycan (GAG) layer disruption/deficiency:** loss of the hydrophilic GAG barrier (hyaluronic acid, chondroitin sulfate, heparan sulfate) that normally excludes urinary solutes (PMC5442440; Wyndaele 2019) → 
3. **Increased urothelial permeability ("leaky urothelium"):** urinary potassium and other solutes diffuse into the suburothelium, depolarizing nerves and muscle, causing direct tissue injury → 
4. **Mast cell activation:** bladder mastocytosis with degranulation, histamine/cytokine release (PMID:17462477; PMC2346452 — mast-cell-derived histamine directly mediates cystitis pain) → 
5. **Neurogenic inflammation and peripheral sensitization:** sensory C-fiber and Aδ-fiber afferent sensitization, upregulation of TRPV1/purinergic signaling, sensitized bladder afferent pathways → 
6. **Central sensitization:** MAPP Network neuroimaging shows altered default-mode-network and sensorimotor-network connectivity, white-matter microstructural abnormalities correlating with symptom severity, and functional MRI evidence of amplified central pain processing (PMC11059973; PMC4604194) → 
7. **Chronic pelvic/bladder pain, urgency, frequency** — clinically overlapping with, and potentially converging into, the broader chronic-overlapping-pain-condition (COPC) phenotype.

### Core causal chain (Hunner-lesion / autoimmune-inflammatory hypothesis)
1. **Genetic susceptibility (HLA-DQB1/HLA-DPB1 peptide-binding-groove variants)** → 
2. **Antigen presentation and adaptive immune activation** → 
3. **Pancystitis:** dense lymphoplasmacytic infiltration throughout the full bladder wall thickness, with **light-chain-restricted clonal B-cell expansion** in ~31% of specimens and **APRIL/BAFF upregulation** driving that clonal expansion (PMID:26587589; Horie et al. 2024, *J Pathol*) → 
4. **Epithelial denudation** and **Hunner ulcer formation** with characteristic vessel disruption → 
5. **Macrophage polarization** (M1-skewing) contributing to disease progression (PMC10815545) → 
6. **Reduced bladder capacity, severe bladder-centric pain**, generally with fewer extra-pelvic comorbidities than NHIC, and better response to local ablative/immunosuppressive therapy (cyclosporine A, fulguration).

### Additional mechanistic contributors
- **TLR4 signaling:** Systemic TLR4-mediated inflammatory responses correlate with pain severity in IC/BPS patients; murine transgenic autoimmune cystitis models (URO-OVA) show TLR4-dependent bladder pain, with splenocyte IL-1β/IL-6/TNF-α production (PMID:31091120, MAPP Network animal study).
- **S100A9/TLR4/NF-κB and TLR4/p38 signaling** amplifies inflammatory damage in both human IC/BPS and experimental autoimmune cystitis (EAC) mouse models (PMC12065242).
- **Autoantibodies:** Anti-muscarinic M3 receptor autoantibodies are found in IC/BPS (shared with Sjögren syndrome patients); antinuclear and anti-bladder-epithelium antibodies are also reported, though generally considered secondary/epiphenomenal rather than primary drivers (nature.com/ncpuro0874).
- **Antiproliferative factor (APF):** A urine-detectable, IC-specific sialoglycopeptide (FZD8-related nonapeptide) that binds **CKAP4** and inhibits bladder urothelial cell proliferation, heparin-binding EGF-like growth factor (HB-EGF) production, and cell-cell adhesion protein expression — proposed as both a mechanistic driver of impaired urothelial healing and a candidate diagnostic biomarker (PMID:15282374, PNAS).
- **NLRP3 inflammasome:** Implicated in cyclophosphamide-induced experimental cystitis; the NLRP3 inhibitor dapansutrile attenuates disease in this model (PMC9205468), suggesting inflammasome-driven IL-1β signaling as a therapeutic target.

### Suggested GO / CL / Molecular terms
- GO:0002438 (acute inflammatory response to antigenic stimulus) / GO:0006954 (inflammatory response)
- GO:0002520 (immune system development, B-cell context) / GO:0042100 (B cell proliferation)
- GO:0045123 (cellular extravasation, mast cell) / GO:0002438 (mast cell mediated immunity, if using MC-specific terms)
- GO:0007204 (positive regulation of cytosolic calcium ion concentration) — relevant to ATP2C1/ATP2A2 mechanism
- CL:0000097 (mast cell)
- CL:0000542 (lymphocyte) / CL:0000236 (B cell) / CL:0000946 (plasma cell)
- CL:0000731 (urothelial cell) / CL:1001428 (bladder urothelial cell, if available)
- CL:0000235 (macrophage)

### Molecular profiling
- **Transcriptomics:** RNA-seq studies distinguishing chronic inflammatory bladder disease subtypes are emerging (Nature Sci Rep 2025, molecular characterization via NGS RNA sequencing and digital image analysis).
- **Proteomics/peptidomics:** Urinary peptidomics analyses reveal altered small urinary peptide profiles in IC/BPS (PMC9117215).
- **Single-cell/spatial:** Not yet extensively published for human IC/BPS bladder tissue based on this search; represents a research gap relative to other immune-mediated diseases.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Urinary bladder (UBERON:0001255), specifically the bladder wall — urothelium, lamina propria/suburothelium, and detrusor muscle.
- **Secondary/associated involvement:** Urethra (in feline model, urethral lamina propria COX-2 upregulation is also seen); pelvic floor musculature (myofascial pelvic floor dysfunction frequently co-occurs); in men, overlap with chronic prostatitis/CPPS implicates prostate.
- **Body systems:** Genitourinary system (primary); nervous system (peripheral sensory afferents and CNS pain-processing networks — default mode network, sensorimotor network); immune system (mast cells, B/plasma cells, macrophages); given COPC overlap, musculoskeletal (fibromyalgia), and gastrointestinal (IBS) systems are frequently co-affected but not primarily "affected organs" of IC/BPS itself.

**Tissue and cell level:**
- Bladder **urothelium** (transitional epithelium) — denudation, thinning, tight-junction barrier dysfunction (CL:0000731 or a bladder-urothelial-cell-specific CL term)
- **Lamina propria/suburothelium** — site of mast cell infiltration, mastocytosis, lymphoplasmacytic infiltration
- **Detrusor smooth muscle** — target of autoantibodies against M3 muscarinic receptors; site of pancystitis in Hunner-type disease
- Cell populations: mast cells (CL:0000097), B cells/plasma cells (CL:0000236/CL:0000946), macrophages (CL:0000235), sensory neurons/nociceptive afferents innervating the bladder wall

**Subcellular level:**
- Endoplasmic reticulum/Golgi Ca²⁺-ATPase compartments (implicated via ATP2C1/SPCA1, ATP2A2/SERCA2 — GO:0005789 endoplasmic reticulum membrane, GO:0000139 Golgi membrane)
- Cell-cell junction complexes (tight junctions, desmosomes) — GO:0005923 (bicellular tight junction), GO:0030057 (desmosome)
- Cytoskeleton-associated protein 4 (CKAP4) — endoplasmic reticulum/plasma membrane localized receptor for APF

**Localization / laterality:** Diffuse involvement of the bladder wall (not lateralized); Hunner lesions can be solitary or multiple, distributed anywhere on the bladder mucosa, occasionally extending to involve the ureteral orifices/distal ureters in rare reported cases (PMC12212936).

---

## 8. Temporal Development

**Onset:** Most commonly adult-onset, typically diagnosed in the 30s–50s, though pediatric and adolescent cases occur. Onset is usually **insidious**, with gradual symptom accumulation, though acute presentations following a UTI or pelvic surgery are reported. Hunner-lesion IC tends to present at an **older age** than non-Hunner IC.

**Progression / disease course:**
- The disease is characteristically **not uniformly progressive**; course is described as **fluctuating, with periods of exacerbation ("flares") and remission**.
- **Spontaneous remission** occurs in up to ~50% of patients, at a mean of ~8 months in some series, with or without treatment.
- Chronicity: for patients who do not remit, IC/BPS typically persists as a lifelong chronic condition, though many remain in a mild-to-moderate symptom range for years rather than steadily worsening.
- **Hormonal influence:** symptoms may fluctuate with the menstrual cycle; some patients report remission during the 2nd–3rd trimester of pregnancy.
- **Stages:** No formal, validated staging system analogous to cancer staging exists; clinical severity is tracked via validated symptom indices (ICSI/ICPI) rather than discrete "stages," though patient-education resources sometimes describe informal "early/moderate/severe" tiers.

**Critical periods / intervention windows:** Early diagnosis and initiation of conservative/behavioral therapy is generally advocated to reduce central sensitization risk, though this is based on clinical consensus rather than a specific validated "critical window" study identified in this search.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence (US women):** RAND RICE study — **2.7% to 6.5%** of US women ≥18 years meet IC/BPS symptom criteria (≈3.4–7.9 million women) (Berry et al., *J Urol* 2011; PMID:21683389). Other estimates: 60–70/100,000 women (Curhan et al.); 2004 Nurses' Health Study ≈2.3% prevalence; managed-care-population estimates of **≥197/100,000 women** and **≥41/100,000 men**.
- **Incidence:** Estimated annual incidence ≈2.6/100,000 women (US); one case-definition study found 1-year incidence of 21/100,000 women and 4/100,000 men.
- **Sex ratio:** Female:male ratio of approximately **5:1** in contemporary estimates (older literature cited 9–10:1), reflecting evolving, broader diagnostic criteria that now better capture male IC/BPS/CPPS overlap.
- IC/BPS is substantially **underdiagnosed**, so true population prevalence may exceed published estimates.

**Genetic etiology characteristics:**
- **Inheritance pattern:** Complex/multifactorial — not classically Mendelian; the disease behaves as a polygenic susceptibility trait modulated by environmental triggers. No autosomal dominant/recessive/X-linked pattern has been established.
- **Penetrance/expressivity:** Not formally quantified given the polygenic/complex model; the HLA risk alleles (OR ~2–2.4) confer modest, incomplete-penetrance risk rather than deterministic causation.
- **Genetic anticipation, germline mosaicism, founder effects:** Not reported/applicable given the non-Mendelian model.
- **Consanguinity:** No specific association reported.
- **Carrier frequency:** Not applicable in the traditional recessive-disease sense; HLA risk-allele frequency (e.g., HLA-DPB1\*04:02) would need to be queried in population-specific allele-frequency databases (not directly reported in the sources reviewed here).

**Population demographics:**
- Best-characterized in **US, Japanese, and Western European** cohorts (the GWAS underlying the HLA association was conducted in a Japanese Hunner-type IC cohort — this MHC association should not be assumed to generalize across all ancestries without replication).
- Geographic distribution of prevalence broadly mirrors availability of specialist urologic/gynecologic diagnostic services (ascertainment bias likely).
- Age distribution: peak diagnosis in middle adulthood, though a broad age range from adolescence to elderly is reported.

---

## 10. Diagnostics

**Diagnosis is clinical and one of exclusion** — there is no single confirmatory laboratory test.

### Clinical/laboratory tests
- **Urinalysis and urine culture** are mandatory first steps to exclude bacterial cystitis (a negative culture is required before diagnosing IC/BPS).
- **Potassium sensitivity test (PST):** **Not recommended** by AUA or CUA guidelines — insufficient sensitivity/specificity to change clinical management (PMC4801189).
- **Urinary biomarkers (research/emerging):** Antiproliferative factor (APF), HB-EGF, EGF, glycoprotein-51 (GP-51); APF/GP-51 currently show the best separation of IC cases from controls in research settings, though not yet standard-of-care diagnostics (PMID:11378044).

### Cystoscopy / hydrodistension
- **Cystoscopy with hydrodistension under anesthesia** is used selectively (not as a first-line/mandatory diagnostic step per current AUA guideline) — primarily when first/second-line treatments fail, or to (a) rule out other pathology (stones, tumors) and (b) identify Hunner lesions, which can then be directly treated (fulguration/triamcinolone injection/resection).
- **Glomerulations** (petechial submucosal hemorrhages post-distension) are a nonspecific finding — present in both HIC and NHIC and even asymptomatic individuals — and are **not required** for diagnosis per current guidelines.
- **Bladder biopsy:** Used to exclude carcinoma in situ and other pathology, and can demonstrate mastocytosis, epithelial denudation, and (in HIC) pancystitis with lymphoplasmacytic infiltration ± clonal B-cell expansion.

### Genetic testing
No clinically validated genetic test panel exists for IC/BPS. Given the emerging ATP2C1/ATP2A2/HLA associations, genetic testing is currently a research tool rather than a diagnostic standard; testing for these genes would presently be relevant only in the context of suspected co-occurring Mendelian skin disease (Hailey-Hailey, Darier disease) or research protocols.

### Omics-based diagnostics
Not yet in clinical use; urinary peptidomics/proteomics (APF-CKAP4 binding assay) remains investigational (patent-stage assay development referenced in freepatentsonline.com/y2014/0193835).

### Clinical criteria / diagnostic definitions
- **AUA (2011, amended 2014/2022) definition:** "An unpleasant sensation (pain, pressure, discomfort) perceived to be related to the urinary bladder, associated with lower urinary tract symptoms of more than six weeks duration, in the absence of infection or other identifiable causes."
- Validated symptom instruments: **O'Leary-Sant ICSI/ICPI**, Pelvic Pain and Urgency/Frequency (PUF) questionnaire.

### Differential diagnosis
Key conditions to exclude/distinguish: bacterial cystitis/recurrent UTI, overactive bladder (OAB), endometriosis (co-occurs in up to ~40% of IC patients per some series), vulvodynia, chronic pelvic pain syndrome/CP-CPPS (men), myofascial pelvic floor dysfunction ("myofascial frequency syndrome"), bladder carcinoma/carcinoma in situ, radiation cystitis, and urethral syndrome.

### Screening
No population-based or genetic screening program exists for IC/BPS; it is not amenable to newborn or carrier screening given its complex/late-onset nature.

---

## 11. Outcome / Prognosis

- **Mortality:** IC/BPS is **not a life-shortening disease**; it does not directly reduce life expectancy. Morbidity is driven by chronic pain and functional/psychosocial impact rather than mortality risk.
- **Disease course:** Chronic, typically lifelong once established, but frequently non-progressive — many patients plateau at a mild-moderate symptom level; spontaneous remission occurs in a substantial minority (~50% in some series, mean ~8 months).
- **Morbidity/QoL:** Substantial impact on sleep (nocturia), sexual function (dyspareunia, sexual dysfunction — RAND study specifically examined this), work productivity, and mental health; comorbid depression/anxiety are common.
- **Prognostic factors:**
  - **Hunner-lesion phenotype:** older age at onset, more severe bladder-centric symptoms, smaller bladder capacity, **fewer non-bladder comorbid syndromes**, but generally **more favorable response to targeted endoscopic/local treatment** (fulguration, cyclosporine A) — i.e., a more "treatable" localized-disease phenotype once identified.
  - **Non-Hunner phenotype:** more likely to have extensive extra-pelvic/COPC comorbidity (fibromyalgia, IBS, CFS — present in 39% and 19% respectively in one series), suggesting a centrally mediated, harder-to-treat pain phenotype.
  - Cystoscopic hydrodistension characteristics (e.g., bladder capacity, glomerulation grade) have been studied as long-term prognostic indicators (PMC7801576).
- **Complications:** Reduced functional bladder capacity in severe/refractory Hunner-lesion disease can necessitate escalation to cystectomy/urinary diversion/augmentation cystoplasty in a small minority of refractory cases (6th-line AUA treatment tier).

---

## 12. Treatment

Treatment follows a **stepwise, multimodal AUA guideline algorithm** (2011, updated 2022), escalating only as needed and avoiding irreversible therapies early.

### First/second-line (conservative)
- Patient education, self-care/behavioral modification (dietary trigger avoidance, stress management, bladder training)
- Manual physical therapy for pelvic floor myofascial dysfunction
- MAXO suggestion: MAXO:0000011 (physical therapy); MAXO:0000088 (dietary intervention)

### Oral pharmacotherapy (third-line-adjacent)
- **Amitriptyline** (tricyclic antidepressant; Grade B evidence)
- **Cimetidine** (H2-antagonist; Grade B)
- **Hydroxyzine** (antihistamine/mast-cell stabilizer; Grade C)
- **Pentosan polysulfate sodium (PPS)** (GAG-layer-replenishing oral agent; Grade B) — counseling required regarding rare risk of PPS-associated maculopathy/vision-related injury
- MAXO/NCIT: NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to CHEBI (e.g., amitriptyline CHEBI:2666; cimetidine CHEBI:3699; hydroxyzine CHEBI:5860; pentosan polysulfate — NCIT term as CHEBI coverage may be limited)

### Intravesical instillation
- **DMSO (dimethyl sulfoxide)**, **heparin**, **lidocaine** (Grade C) — direct bladder instillation, 15–20 min dwell, symptom relief lasting 3–6 months
- **GAG-replacement therapy**: intravesical hyaluronic acid and/or chondroitin sulfate (e.g., Cystistat) — investigated as barrier-restoring therapy (Wyndaele 2019; Cervigni review)

### Fourth-line / procedural
- **Cystoscopy with short-duration, low-pressure hydrodistension** (diagnostic + therapeutic)
- **Fulguration or triamcinolone injection of Hunner lesions** — targeted therapy specific to the HIC phenotype
- **Intradetrusor onabotulinumtoxin A (Botox)** injection (Grade C) — for refractory disease; O'Leary-Sant ICSI predicts treatment response (PMC4549729)
- **Neuromodulation** (sacral nerve stimulation / percutaneous tibial nerve stimulation)

### Fifth-line
- **Oral cyclosporine A** + pain management — particularly effective in Hunner-lesion IC (better response than non-Hunner)

### Sixth-line (last resort, irreversible)
- Urinary diversion ± cystectomy, pain management, substitution cystoplasty

### Pain management (adjunctive at all stages)
- Multimodal pain management including neuropathic pain agents, pelvic pain specialists, and management of COPC comorbidities.

### Experimental / emerging
- APF-CKAP4 pathway-targeted diagnostics/therapeutics (early-stage)
- NLRP3 inflammasome inhibition (dapansutrile) — preclinical (cyclophosphamide mouse model)
- Anti-CXCL10 antibody — ameliorates severity in experimental autoimmune cystitis model
- S100A9-targeted therapy — preclinical
- Naltrexone trial (IC PaIN Trial, NCT04313972) for pain improvement
- LiRIS® (intravesical drug-delivery device) trials in Hunner-lesion IC (NCT02395042)

### Treatment outcomes / adverse events
- PPS carries an FDA-flagged risk of pigmentary maculopathy with long-term use.
- Botox carries risk of urinary retention requiring intermittent self-catheterization.
- Response rates vary substantially by phenotype (HIC responds better to cyclosporine A and lesion-directed local therapy; NHIC often requires broader multimodal/central-pain-directed management).

---

## 13. Prevention

- **Primary prevention:** No established primary prevention strategy exists (etiology is multifactorial/idiopathic-adjacent); prompt treatment of UTIs and avoidance of known bladder-irritant triggers are reasonable but unproven preventive measures.
- **Secondary prevention (early detection):** No population screening program exists; early recognition of characteristic symptom clusters (to avoid prolonged misdiagnosis as recurrent UTI) is emphasized clinically to potentially limit progression to central sensitization, though this is a consensus-based rather than trial-validated recommendation.
- **Tertiary prevention:** Stepwise, guideline-concordant management (§12) aims to prevent progression to end-stage refractory disease requiring cystectomy/diversion; pelvic floor physical therapy and dietary modification are used to prevent flare escalation.
- **Genetic counseling:** Not applicable in the traditional sense given the complex/polygenic model; not a standard part of clinical care.
- **Public health / environmental interventions:** Not specifically established; general bladder-irritant avoidance guidance is patient-education-level, not a formal public health program.
- **Prophylaxis:** No pharmacologic prophylaxis is established for at-risk individuals (e.g., following UTI) to prevent IC/BPS onset.

---

## 14. Other Species / Natural Disease

**Feline Idiopathic Cystitis (FIC)** is the flagship **naturally occurring comparative model** for human IC/BPS:
- **Taxonomy:** *Felis catus* (NCBITaxon:9685)
- FIC is the most common form of feline lower urinary tract disease (FLUTD); it is **sterile** (no primary bacterial infection) and shares the "interstitial" (interstitium-localized) inflammation nomenclature with the human disease.
- Histologically, FIC most closely resembles the **non-Hunner BPS subtype**.
- Shared pathological features with human IC/BPS: increased degranulated mast cells, leukocyte accumulation, increased COX-1 expression in bladder lamina propria, increased COX-2 in urethral lamina propria (PMC5908978).
- FIC is considered by many comparative-medicine researchers to be a **preferred natural model** over induced rodent models because it arises spontaneously (not chemically induced) and shares stress-reactivity and neuro-immune features with human disease; primary feline uroepithelial cell culture is used to study norepinephrine/stress-driven inflammatory and barrier-function effects in vitro (PMC9961545, PMC10657828).
- **Veterinary relevance:** FIC is a major cause of feline veterinary visits and can precipitate life-threatening urethral obstruction in male cats, giving it independent clinical importance beyond its use as a human-disease model.
- **Comparative biology:** No systematic cross-species genetic-conservation studies (e.g., ATP2C1/ATP2A2 orthology in feline FIC) were identified in this search — a research gap.
- **Zoonotic potential:** None; FIC is not transmissible.

---

## 15. Model Organisms

No single genetically engineered "IC/BPS mouse" fully recapitulates the human syndrome; instead, **>20 induced and a smaller number of genetic/autoimmune models** are used, each capturing different mechanistic facets (PMC5798633; Frontiers 2023 review of animal models):

### Chemically induced models
- **Cyclophosphamide (CYP)-induced cystitis (mouse and rat):** Systemic (i.p.) CYP is hepatically metabolized to acrolein, which is excreted in urine and damages the bladder; produces submucosal edema, mastocytosis, and proinflammatory cytokine upregulation. A well-validated **chronic** rat model exists for repeated-dose, longer-duration study (PMC7485435, PMID/PMC4002240 — includes characterization of relationship to metabotropic glutamate receptors).
- **LPS-induced model (mouse):** Intravesical instillation via catheter; **C57BL/6 (B6) mice** show the most human-IC-like functional changes (altered peak bladder pressure, decreased intercontraction intervals) and are proposed as the best-fit strain for this model (PMC8585067).
- Other chemical agents: hydrochloric acid (HCl), protamine sulfate (bladder-permeabilizing), and combination-toxin models.

### Autoimmune/genetic models
- **URO-OVA transgenic experimental autoimmune cystitis (EAC) model:** mice engineered to express ovalbumin as a bladder-urothelium-restricted "self" antigen, then immunized to trigger urothelium-targeted autoimmunity — produces bladder pain, pelvic pain behaviors, and **TLR4-dependent** pain phenotype (PMID:31091120), used to model the Hunner-lesion/autoimmune pathophysiologic arm.
- **Uroplakin-peptide-specific autoimmunity model:** immunization against a bladder uroplakin peptide initiates an IC/painful-bladder-syndrome-like phenotype in mice (PMC3745386).

### Model characteristics / limitations
- Chemically induced models best recapitulate **acute/subacute inflammatory and barrier-injury** aspects but poorly capture the chronic, relapsing-remitting human course and central sensitization component.
- Autoimmune/genetic models better capture the **Hunner-lesion, antigen-driven pancystitis** mechanism but are more resource-intensive and strain-dependent.
- None of the current models robustly reproduce the **human COPC/central-sensitization phenotype** (fibromyalgia/IBS overlap) seen in a large subset of human non-Hunner IC/BPS patients — an acknowledged translational gap.

### Applications
- CYP and LPS models: used for testing GAG-replacement, anti-inflammatory, and analgesic candidate therapies, and for studying acute mast-cell/cytokine mechanisms.
- URO-OVA/uroplakin models: used for studying TLR4, autoantibody, and adaptive-immune-driven mechanisms relevant to Hunner-type disease and for testing immunomodulatory therapies (e.g., anti-CXCL10).
- Feline primary uroepithelial cell culture: used as an in vitro (non-rodent) model for studying stress/norepinephrine-driven barrier dysfunction.

### Resources
Standard rodent resources (MGI for mouse strain/allele data, IMSR for strain repositories) apply generically; no IC/BPS-dedicated model organism database exists distinct from the general rodent-model infrastructure.

---

## Summary Table: Suggested Ontology Term Bindings for KB Curation

| Domain | Suggested term(s) |
|---|---|
| Disease | MONDO:0018301 (interstitial cystitis); ORPHA:37202 |
| Key phenotypes | HP terms for pelvic pain, urinary urgency/frequency, nocturia, dyspareunia (see §3 table) |
| Cell types | CL:0000097 (mast cell), CL:0000236 (B cell), CL:0000946 (plasma cell), CL:0000235 (macrophage), CL:0000731 (urothelial-lineage cell) |
| Anatomy | UBERON:0001255 (urinary bladder); relevant sub-structures: urothelium, lamina propria, detrusor |
| Genes | HLA-DQB1 (HGNC:4944), HLA-DPB1 (HGNC:4940), ATP2C1 (HGNC:13202), ATP2A2 (HGNC:812), SIX5 (HGNC:10891), FZD8 (HGNC:4045) |
| Biological processes | GO:0006954 (inflammatory response), GO:0042100 (B cell proliferation), GO:0007204 (Ca²⁺ ion concentration regulation) |
| Treatments (MAXO/NCIT) | MAXO:0000011 (physical therapy); NCIT:C15986 (Pharmacotherapy) + therapeutic_agent (amitriptyline CHEBI:2666, hydroxyzine CHEBI:5860, cimetidine CHEBI:3699, pentosan polysulfate); MAXO:0000004 (surgical procedure) for cystectomy/diversion |
| Model organism | *Mus musculus* (NCBITaxon:10090) — CYP-, LPS-, URO-OVA-, uroplakin-induced models; *Felis catus* (NCBITaxon:9685) — natural FIC model |

---

## Key Citations (PMID-indexed)

1. Maeda D et al. GWAS identifies risk loci within the MHC region for Hunner-type interstitial cystitis. *Cell Rep Med* 2023. PMID:37467720
2. [Exome sequencing study] Interstitial Cystitis: a phenotype and rare variant exome sequencing study. medRxiv/PMC12933612, 2025. PMID:40034785
3. Maeda D, Akiyama Y, et al. Hunner-Type (Classic) Interstitial Cystitis: A Distinct Inflammatory Disorder Characterized by Pancystitis, with Frequent Expansion of Clonal B-Cells and Epithelial Denudation. *PLoS One* 2015;10:e0143316. PMID:26587589
4. Theoharides TC, Sant GR. The mast cell in interstitial cystitis: role in pathophysiology and pathogenesis. PMID:17462477
5. Chen J et al. Toll-like Receptor 4 and comorbid pain in IC/BPS (MAPP Network animal study). PMID:31091120
6. Kim SH et al. An antiproliferative factor from interstitial cystitis patients is a frizzled 8 protein-related sialoglycopeptide. *PNAS* 2004. PMID:15282374
7. Berry SH et al. Prevalence of symptoms of bladder pain syndrome/interstitial cystitis among adult females in the United States. *J Urol* 2011. PMID:21683389
8. Whitmore KE et al. Hunner lesion versus non-Hunner lesion interstitial cystitis/bladder pain syndrome. PMID:31144757
9. Homma Y et al. (mast-cell c-kit expression). PMID:9609630

**Evidence-source classification note:** Most claims above are HUMAN_CLINICAL (cohort/histopathology studies, epidemiologic surveys, GWAS). Mechanistic claims regarding TLR4, NLRP3, S100A9, and URO-OVA/uroplakin autoimmunity are MODEL_ORGANISM (mouse). APF-CKAP4 biochemical characterization is IN_VITRO/biochemical. FIC comparative data are MODEL_ORGANISM (naturally occurring, non-human).

**Explicit evidence gaps** (for downstream curation `KNOWLEDGE_GAP`/`HUMAN_MODEL_MISMATCH` framing): (a) no dedicated IC/BPS epigenomic (DNA methylation) dataset identified; (b) no single-cell/spatial transcriptomic atlas of human IC/BPS bladder tissue identified; (c) HLA-DQB1/DPB1 GWAS association reported in a Japanese Hunner-type cohort only — ancestry-generalizability unconfirmed; (d) no rodent or feline model fully recapitulates the central-sensitization/COPC phenotype of non-Hunner human IC/BPS, representing a HUMAN_MODEL_MISMATCH-eligible gap.