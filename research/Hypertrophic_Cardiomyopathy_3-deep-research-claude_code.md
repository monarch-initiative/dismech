---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T20:53:48.059465'
end_time: '2026-08-01T21:17:38.021073'
duration_seconds: 1429.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 3
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 22
  num_turns: 51
  total_cost_usd: 4.48216425
  session_id: f22d2fb7-c002-47e3-97b8-a98eb24b3393
  stop_reason: end_turn
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 3
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 3** covering all of the
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

# Research Report: Hypertrophic Cardiomyopathy 3 (CMH3 / TPM1-Related HCM)

**Prepared:** 2026-08-01 · **Target:** `Hypertrophic Cardiomyopathy 3` · **MONDO:0007267** · **Gene:** *TPM1* (`hgnc:12010`)

> **Verification status of citations.** All PMIDs below were resolved against PubMed/PMC/ClinVar during this research except where explicitly marked **[PMID UNVERIFIED]**. Verbatim abstract text is given in quotation marks and marked *verbatim* where retrieved word-for-word; paraphrased content is unquoted. Before any of these are committed as dismech `evidence` items, run `just fetch-reference PMID:XXXX` + `just validate-references` per the repo SOP — several quotes here were retrieved through a summarizing fetch layer and must be re-checked as exact substrings of the cached abstract.

---

## 1. Disease Information

### Overview

Hypertrophic cardiomyopathy 3 (CMH3) is the *TPM1*-related molecular subtype of familial hypertrophic cardiomyopathy — an autosomal dominant sarcomeric (thin-filament) cardiomyopathy defined by increased left ventricular wall thickness in the absence of an abnormal loading condition, with the histologic triad of cardiomyocyte hypertrophy, myocyte/myofibrillar disarray, and replacement/interstitial fibrosis. It is one of the nine "definitive" monogenic sarcomere-gene HCM entities and one of the two original thin-filament HCM genes described in the landmark sarcomere paper of Thierfelder et al.

Thierfelder L, Watkins H, MacRae C, Lamas R, McKenna W, Vosberg HP, Seidman JG, Seidman CE. *Alpha-tropomyosin and cardiac troponin T mutations cause familial hypertrophic cardiomyopathy: a disease of the sarcomere.* Cell. 1994 Jun 3;77(5):701–12. **PMID:8205619**

> Key conclusion (paraphrased from abstract): missense substitutions **Asp175Asn** and **Glu180Gly** in the α-tropomyosin gene cause FHC linked to chromosome 15q2; because α-tropomyosin, cardiac troponin T, and β-myosin heavy chain mutations produce the same disease, **"FHC is a disease of the sarcomere."** The authors further propose that **"abnormal stoichiometry of sarcomeric proteins can cause cardiac hypertrophy."**

Two features distinguish CMH3 from thick-filament (MYH7/MYBPC3) HCM in the classical literature: (i) hypertrophy is often **milder / less impressive** relative to the clinical risk, and (ii) at least for some variants the arrhythmic/heart-failure burden is disproportionate to wall thickness. Watkins H, et al. *Mutations in the genes for cardiac troponin T and alpha-tropomyosin in hypertrophic cardiomyopathy.* N Engl J Med. 1995;332(16):1058–64. **PMID:7898523** — α-tropomyosin mutations account for **~3%** of FHC, and these mutations are "characterized by relatively mild and sometimes subclinical hypertrophy but a high incidence of sudden death."

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0007267** — `hypertrophic cardiomyopathy 3` (OAK-verified) |
| OMIM (phenotype) | **115196** — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 3; CMH3 |
| OMIM (gene) | **191010** — TROPOMYOSIN 1; TPM1 |
| MedGen | CUI **C1861863**, UID 349382 |
| UMLS | C1861863 |
| Disease Ontology | DOID:0110309 |
| MeSH | C566170 |
| GARD | GARD:0024541 |
| HGNC | **hgnc:12010** (*TPM1*) — note dismech lowercase convention |
| UniProt | **P09493** (Tropomyosin alpha-1 chain) |
| Cytoband | **15q22.2** |
| MONDO subsets | `rare`, `nord_rare`, `gard_rare` |

MONDO definition (OAK, verbatim): *"Any hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the TPM1 gene."* Parent: `MONDO:0024573` familial hypertrophic cardiomyopathy. Logical definition: `MONDO:0005045` **and** `RO:0004003 some HGNC:12010`.

### Synonyms (from MONDO/MedGen — all OAK-verified)

- CMH3
- TPM1 hypertrophic cardiomyopathy
- cardiomyopathy, familial hypertrophic, 3 / type 3
- cardiomyopathy, hypertrophic, 3
- hypertrophic cardiomyopathy type 3
- hypertrophic cardiomyopathy caused by mutation in TPM1
- TPM1-Related Familial Hypertrophic Cardiomyopathy (MedGen)
- α-tropomyosin–related HCM (literature usage)

### Data provenance character

CMH3 knowledge is overwhelmingly **aggregated disease-level and family-based**, not EHR-derived: OMIM/MONDO gene-series curation, ClinGen gene-disease validity curation, kindred-based genotype–phenotype series (Finnish D175N founder cohorts; the Iberian R21L cohort), sarcomere-gene registry cohorts (SHaRe-type, Italian/Russian centers), plus a large in-vitro/biophysical and transgenic-animal mechanistic literature. Population-scale variant frequency comes from gnomAD/ExAC case–control burden analyses. There is **no** dedicated CMH3 EHR phenotype or registry; individual-level data come from clinical genetics cohorts.

---

## 2. Etiology

### 2.1 Primary causal factor

Heterozygous (monoallelic) **missense** variants in *TPM1*, encoding α-tropomyosin — the ~284-residue, α-helical coiled-coil dimer that lies in the actin filament groove and, together with the troponin complex, gates myosin access to actin in a Ca²⁺-dependent, three-state (blocked → closed → open) manner. Mechanism of disease at the gene level per ClinGen: **altered gene product sequence**, autosomal dominant, monoallelic; reported pathogenic variant class is **missense**.

**Critically for variant interpretation:** truncating *TPM1* variants are **not** an HCM mechanism. In the largest published case–control burden analysis (4,447 HCM cases vs ExAC; Atlas of Cardiac Genetic Variation / cardiodb ACGV):

| Variant class | Case freq. | Reference freq. | Excess | Odds ratio (95% CI) |
|---|---|---|---|---|
| All rare protein-altering | 1.484% | 0.086% | 1.40% (p<0.0001) | **17.33 (11.83–25.51)** |
| Non-truncating | — | — | 1.40% (p<0.0001) | **18.04 (12.26–26.68)** |
| Truncating | — | — | 0.00% (p=1.0) | 0.00 (0.00–25.38) |

Etiological fraction **0.94 (0.92–0.96)** — i.e. ~94% of HCM patients carrying a rare *TPM1* variant are likely to have disease caused by it. Source: cardiodb ACGV TPM1/HCM page (derived from Walsh R, et al. *Reassessment of Mendelian gene pathogenicity using 7,855 cardiomyopathy cases and 60,706 reference samples.* Genet Med 2017 — **[PMID UNVERIFIED: commonly cited as 27532257]**).

### 2.2 Genetic risk factors

**Causal variants (see §4 for full detail).** The two archetypes are **p.Asp175Asn** and **p.Glu180Gly** (Thierfelder 1994, PMID:8205619). Residue 175/180 sits in a **troponin-T–binding region** of the tropomyosin molecule — this is the reason the substitutions are cardiac-specific and functionally potent (stated in the α-TM180 transgenic mouse literature, PMID:11603924).

**Recurrent mutation / hot spot.** Coviello DA, et al. *Clinical features of hypertrophic cardiomyopathy caused by mutation of a "hot spot" in the alpha-tropomyosin gene.* J Am Coll Cardiol. 1997;29(3):635–40 **[PMID UNVERIFIED]** — three kindreds with independently arising Asp175Asn; the authors propose that nucleotide 579 (G→A transition, exon 5) has increased susceptibility to mutation.

**De novo mutation is documented.** Watkins H, et al. *A de novo mutation in alpha-tropomyosin that causes hypertrophic cardiomyopathy.* Circulation. 1995. **PMID:7729014** — so a negative family history does not exclude CMH3.

**Modifier / background genetic risk.** Common-variant polygenic background substantially modifies both penetrance and expressivity in sarcomere-variant carriers: Harper AR, Goel A, Grace C, et al. *Common genetic variants and modifiable risk factors underpin hypertrophic cardiomyopathy susceptibility and expressivity.* Nat Genet. 2021 Feb;53(2):135–142. DOI 10.1038/s41588-020-00764-0. **[PMID UNVERIFIED — commonly cited as 33495597]** — GWAS of 2,780 cases / 47,486 controls identified **12 genome-wide-significant HCM susceptibility loci**; a genetic risk score **halved** HCM odds in the lowest quintile and **doubled** them in the highest, and influenced phenotypic severity in sarcomere-variant carriers.

**Sex as a genetic-background modifier.** Male sex is an independent predictor of conversion from genotype-positive/phenotype-negative to overt HCM: HR **2.91** (Lorenzini M, et al. *Penetrance of Hypertrophic Cardiomyopathy in Sarcomere Protein Mutation Carriers.* JACC. 2020;76(5):550–559. **PMID:32731933**). Concordantly, in the Iberian *TPM1* p.Arg21Leu cohort, cumulative diagnosis probability at age 50 was **50% in male vs 25% in female** carriers (PMID:33642254).

### 2.3 Environmental risk factors

CMH3 is monogenic; environment acts as a **modifier of expressivity and of arrhythmic/ischemic triggering**, not as a cause:

- **Elevated diastolic blood pressure** — Mendelian randomization in Harper et al. 2021 identified DBP as a key modifiable risk factor (a 1-SD DBP increase raised HCM risk ~4-fold in sarcomere-negative HCM). Afterload is therefore plausibly a modifier of hypertrophic expressivity in variant carriers, though this was derived in sarcomere-negative disease.
- **Intense/competitive exercise** — the classical trigger context for SCD in HCM; HCM is the most commonly reported cause of SCD in US athletes (~36% in some series) and >80% of affected individuals are asymptomatic before SCD.
- **Acidosis / ischemia as a decompensating exposure** — mechanistically supported specifically for tropomyosin FHC mutations: "Functional effects of a tropomyosin mutation linked to FHC contribute to maladaptation during acidosis" (PMC3035739).
- **Age** — penetrance is strongly age-dependent (§9).
- **Family history** — the dominant risk factor in practice; drives cascade screening.

No toxin, infectious, occupational, or radiation exposure is implicated in CMH3 causation. **Not applicable / no evidence found:** dietary, pollutant, or occupational etiologic factors.

### 2.4 Protective factors

- **Genetic:** low-percentile HCM polygenic score is associated with roughly halved odds of HCM expression (Harper 2021) — the closest thing to a documented protective genetic factor. No specific protective *TPM1* allele or modifier allele has been reported.
- **Environmental/therapeutic:** blood-pressure control (from the DBP MR result) and, at the level of secondary prevention, cardiac myosin inhibition and ICD therapy (§12). Historically, restriction from high-intensity competitive sport was considered protective; the 2024 AHA/ACC guideline substantially liberalized exercise recommendations (§12–13).
- **Not available:** no dietary, supplement, or gnomAD-derived protective-variant data specific to *TPM1*.

### 2.5 Gene–environment interactions

Documented interactions are (i) **genotype × sex** (male carriers convert to overt HCM ~3× more often; PMID:32731933, PMID:33642254); (ii) **rare variant × polygenic background** (Harper 2021); (iii) **rare variant × afterload/DBP** (Harper 2021, MR); (iv) **mutant tropomyosin × intracellular acidosis** — a true molecular GxE, where the mutant thin filament responds maladaptively to acidotic pH (PMC3035739, in vitro/model organism). No CTD-registered chemical–gene interaction relevant to CMH3 was identified.

---

## 3. Phenotypes

CMH3 phenotype is the HCM phenotype with a thin-filament flavor: comparable or *lesser* wall thickness for a given clinical burden, high late-gadolinium-enhancement (fibrosis) prevalence, and faster progression to advanced heart failure. Frequencies below are drawn from thin-filament HCM cohorts (where *TPM1* is the largest constituent gene) and from *TPM1*-specific kindreds; **frequencies are cohort-specific and should be curated conservatively — per the dismech frequency-evidence SOP, omit `frequency:` where the snippet supports only the association.**

### 3.1 Core structural phenotypes

| Phenotype | HPO term (OAK-verified) | Onset | Severity/course | Frequency & evidence |
|---|---|---|---|---|
| Hypertrophic cardiomyopathy | **HP:0001639** Hypertrophic cardiomyopathy | Adolescent–adult (variable) | Progressive | Obligate/defining |
| Left ventricular hypertrophy | **HP:0001712** Left ventricular hypertrophy | Adult typical | Progressive | Defining; max wall thickness **17 mm** median in thin-filament vs **21 mm** thick-filament (p=0.024) — Chumakova OS, et al. *J Clin Med.* 2025;14(3):866 |
| Asymmetric septal hypertrophy | **HP:0001670** Asymmetric septal hypertrophy | Adult | Variable | *TPM1* characteristically anterior/septal; D175N kindreds: mean max wall thickness 24±4.5 mm anterior septum (family DT), 15±2.7 mm (family DB), 18±2.1 mm posterior septum (family MI) — Coviello 1997 **[PMID UNVERIFIED]** |
| Left ventricular outflow tract obstruction | **HP:0032092** Left ventricular outflow tract obstruction | Adult | Variable | 33% of thin-filament cohort (Chumakova 2025) |
| Myocardial fibrosis | **HP:0001685** Myocardial fibrosis | Adult | Progressive | LGE present in **88%** of thin-filament patients (Chumakova 2025); replacement fibrosis on histology in D175N (Coviello 1997) |
| LV diastolic dysfunction | **HP:0025168** Left ventricular diastolic dysfunction | Early, often pre-hypertrophic | Progressive | Central to mechanism; documented in α-TM180 mouse (PMID:11603924) and in S215L engineered tissue (20% slower relaxation; PMID:36896133) |
| Mitral regurgitation | **HP:0001653** Mitral regurgitation | Adult | Variable | Secondary to SAM/LVOTO in obstructive disease |

### 3.2 Arrhythmic and sudden-death phenotypes

| Phenotype | HPO term | Notes |
|---|---|---|
| Sudden cardiac death | **HP:0001645** Sudden cardiac death | α-tropomyosin mutations described with "relatively mild and sometimes subclinical hypertrophy but a high incidence of sudden death" (PMID:7898523). A novel *TPM1* missense variant produced a **malignant young-onset** pedigree: 12 affected members, **5 died young**, others only mildly affected — "malignant phenotype at young age with a variable clinical manifestation and penetrance at older age" (PMID:12651045) |
| Ventricular tachycardia (NSVT) | **HP:0004756** Ventricular tachycardia | 13% NSVT in the thin-filament cohort (Chumakova 2025); other cohorts report *higher* NSVT incidence in thin-filament/TPM1 HCM — literature is genuinely discordant |
| Atrial fibrillation | **HP:0005110** Atrial fibrillation | Standard HCM complication; atrial enlargement is an early feature of the α-TM180 mouse |
| Arrhythmia (general) | **HP:0011675** Arrhythmia | — |
| Cardiac arrest | **HP:0001695** Cardiac arrest | — |
| Abnormal EKG | **HP:0003115** Abnormal EKG | Abnormal ECG is the strongest predictor of phenotype conversion, HR **4.02** (PMID:32731933) — and frequently precedes hypertrophy |

### 3.3 Symptomatic phenotypes

| Phenotype | HPO term | Onset/course | Notes |
|---|---|---|---|
| Dyspnea | **HP:0002094** Dyspnea | Adult, progressive | 53% of thin-filament patients symptomatic at diagnosis (Chumakova 2025) |
| Chest pain | **HP:0100749** Chest pain | Episodic | Angina from microvascular ischemia/demand mismatch |
| Syncope | **HP:0001279** Syncope | Episodic | Major SCD risk marker |
| Palpitations | **HP:0001962** Palpitations | Episodic | — |
| Exercise intolerance | **HP:0003546** Exercise intolerance | Progressive | Peak VO₂ is the SEQUOIA-HCM primary endpoint domain |
| Congestive heart failure | **HP:0001635** Congestive heart failure | Late | **20%** of thin-filament patients progressed to advanced HF vs 7% thick-filament; mean survival free of advanced HF **5.2 ± 0.64 y vs 11.8 ± 1.04 y**, HR **5.6**, p=0.018 (Chumakova 2025) |

### 3.4 Cellular/histopathologic phenotypes (for `category: Cellular` and `histopathology`)

- **Cardiomyocyte hypertrophy** — >3-fold increased cardiomyocyte volume in *TPM1* S215L hiPSC-CM/engineered tissue (PMID:36896133); >3-fold peak force increase for E62Q (PMID:39436707).
- **Myocyte and myofibrillar disarray** — in the OMIM/MedGen definition itself: CMH3 is *"an autosomal dominant disorder characterized by increased myocardial mass with myocyte and myofibrillar disarray"* (MedGen C1861863, *verbatim*).
- **Replacement and interstitial fibrosis** — Coviello 1997; α-TM180 mouse (PMID:11603924).
- **Hypertrophic gene program activation** — upregulation of *MYH7*, *NPPB* (BNP), *NPPA* (ANP), *GATA4*, *FHL1* in S215L engineered heart tissue (PMID:36896133, IN_VITRO).

### 3.5 Quality-of-life impact

No CMH3-specific PRO study exists. Generalizable HCM data: aficamten produced "substantial improvements across a broad range of clinically relevant efficacy measures" including symptoms and health status (KCCQ) in SEQUOIA-HCM (NCT05186818), and EXPLORER-HCM (NCT03470545) met its primary and all secondary endpoints (p≤0.0006), which included KCCQ-CSS and NYHA class. Per-phenotype QoL attribution for CMH3 specifically is **not available**; the dominant QoL determinants in HCM are exertional dyspnea, exercise limitation, arrhythmia/ICD-related anxiety, and — for genotype-positive relatives — surveillance burden.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

***TPM1*** — tropomyosin 1 (alpha), `hgnc:12010`, OMIM *191010, chromosome **15q22.2**, UniProt **P09493**. The cardiac/striated-muscle isoform is transcript **NM_001018005.2** (MANE Select for variant nomenclature in ClinVar). Protein: 284-residue α-helical **coiled-coil homodimer** with a 7-fold quasi-repeat ("periods") of actin-binding sites; polymerizes head-to-tail into a continuous strand along both grooves of the actin filament; binds actin, troponin T, and (indirectly) troponin I. GO annotations of relevance: `GO:0051015` actin filament binding, `GO:0031014` troponin T binding, `GO:0005884` actin filament, `GO:0030017` sarcomere, `GO:0030016` myofibril (all OAK-verified).

**ClinGen gene–disease validity: DEFINITIVE for HCM.** Hespe S, Waddell A, Asatryan B, et al. *ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel: Reappraisal of Genes associated with Hypertrophic Cardiomyopathy.* **PMID:39132495** (medRxiv 2024; JACC 2025, doi 10.1016/j.jacc.2024.12.010). TPM1 retained its **Definitive** classification from the 2019 curation; Table 2 records autosomal dominant inheritance, monoallelic autosomal requirement, altered-gene-product-sequence mechanism, and **missense** as the reported pathogenic variant class. In the same reappraisal, 31 genes were re-curated + 5 new candidates; 17/31 (55%) changed classification (1 limited, 4 disputed from no-known-relationship, 9 disputed from limited, 3 definitive from moderate), and *TNNC1* was upgraded as a 9th definitive sarcomere gene. Panel: 29 individuals, 21 institutions, 6 countries.

### 4.2 Pathogenic variants

| Variant (protein) | cDNA (NM_001018005.2) | rsID | ClinVar germline | Phenotype notes | Key PMIDs |
|---|---|---|---|---|---|
| **p.Asp175Asn** (D175N) | **c.523G>A** | **rs104894503** | **Pathogenic**, 2★ ("criteria provided, multiple submitters, no conflicts"), 6 submissions, last eval. 2025-12-02; GRCh38 chr15:63060899 | Archetype; **Finnish founder**; mild–moderate HCM, favorable prognosis, high adult penetrance; recurrent (hot spot at nt 579) | 8205619, 22462493, 15000344, Coviello 1997 |
| **p.Glu180Gly** (E180G) | **c.539A>G** | **rs104894502** | **Pathogenic**, 0★ (no assertion criteria), 2 submissions, last eval. 1994-06-03; GRCh38 chr15:63060915 | Archetype; largest Ca²⁺-sensitization of the pair; basis of the severe α-TM180 mouse | 8205619, 11603924 |
| p.Val95Ala (V95A) | — | — | Reported pathogenic | "Mild cardiac phenotype, abnormal calcium binding to troponin, abnormal myosin cycling, and **poor prognosis**" | Karibe A, et al. Circulation. 2001;103(1):65 **[PMID UNVERIFIED]** |
| p.Arg21Leu (R21L) | — | — | Pathogenic | **Iberian founder** (Galicia, Extremadura, N. Portugal); 25/4,099 (0.61%) HCM probands, absent in 6,462 non-HCM inherited-cardiac controls (p<0.0001); 83 carriers/31 probands; late-onset, incomplete penetrance, generally favorable prognosis | **33642254** |
| p.Ser215Leu (S215L) | — | — | VUS→pathogenic by functional modeling | Full mechanistic pipeline: destabilized blocked state, +1.0 pCa₅₀ unit Ca²⁺ sensitization | **36896133** |
| p.Glu62Gln (E62Q) | — | — | HCM-associated | >3-fold ↑ peak force (hypercontractile); rescued by mavacamten | **39436707** |
| Novel missense (malignant pedigree) | — | — | Pathogenic | 12 affected, 5 young deaths; malignant young-onset with variable later penetrance | **12651045** |
| De novo variant | — | — | Pathogenic | Establishes de novo occurrence | **7729014** |

**Allele frequency.** ClinVar records D175N at *"extremely low frequency in the gnomAD v4.1.0 dataset (total allele frequency: <0.001%)"* (*verbatim*). E180G has no gnomAD frequency in its ClinVar record. Aggregate reference-population frequency for all rare protein-altering *TPM1* variants was **0.086%** in ExAC vs **1.484%** in 4,447 HCM cases (cardiodb ACGV).

**Variant type/class.** Exclusively **missense** (altered gene product sequence) for the HCM phenotype. **Truncating variants confer no HCM excess (OR 0.00)** — this is an important negative and should be curated explicitly: a *TPM1* truncating variant found in an HCM patient is not evidence for CMH3.

**Origin.** **Germline**, autosomal dominant, mostly inherited, with documented de novo occurrence (PMID:7729014). Somatic *TPM1* variation is not a CMH3 mechanism. No COSMIC/TCGA relevance.

**Functional consequence class.** Not loss of function and not haploinsufficiency — a **dominant, poison-peptide/altered-function** mechanism operating on the thin filament: the mutant α-tropomyosin incorporates into the filament and changes its mechanical stiffness and its regulatory-state equilibria (see §6). The most precise statement available for the HCM direction of effect is *increased thin-filament activation / hypercontractility with impaired relaxation* — arguably a gain of function at the level of filament activation, achieved by loss of the inhibitory (blocked-state) function of tropomyosin.

### 4.3 Allelic disorders (same gene, different disease — keep as separate dismech entries)

*TPM1* is a pleiotropic cardiac gene. These are **not** CMH3 and should be modeled as distinct entities:

- **Dilated cardiomyopathy 1Y (CMD1Y)** — e.g. **p.Glu54Lys (E54K)**: ~3-fold **decrease** in peak force, 42% faster time-to-peak, 50% faster relaxation (PMID:39436707).
- **Left ventricular noncompaction 9 (LVNC9)** — e.g. **p.Lys30Glu (K30E)**, pediatric LVNC + DCM via impaired structural/functional properties of cardiac tropomyosin (PMC11641563).
- **Restrictive cardiomyopathy** — **p.Glu181Lys (E181K, c.541G>A)**, sporadic pediatric RCM, proposed to act by suppressing **CaMKII/HDAC4** signaling (Fu J, Zhang J, et al., Frontiers in Genetics; PMC12818787). Note this residue is immediately adjacent to the classical E180G HCM residue — a striking example of position-adjacent phenotypic divergence.
- Congenital heart defects/septal defects have been reported for *TPM1* in some panels; evidence is weaker and should not be asserted without primary verification.

Suggested `Discussion` / `mechanistic_hypotheses` framing: the HCM-vs-DCM-vs-RCM divergence within *TPM1* is the flagship unresolved question for this gene, and is now partially explained (§6.6).

### 4.4 Modifier genes

- **Polygenic HCM background** (12 GWAS loci; PRS quintile effect) — Harper 2021, Nat Genet 53:135–142.
- **Sex** (male, HR 2.91) and **abnormal ECG** (HR 4.02) as clinical/biological modifiers of penetrance — PMID:32731933.
- **Compound/multi-variant sarcomere genotypes** are a recognized severity modifier in HCM generally; specific *TPM1* digenic reports were not identified in this search. **No named single-gene modifier locus is established for CMH3.**

### 4.5 Epigenetics

No CMH3-specific methylation or histone-modification dataset was identified. The only chromatin-adjacent mechanistic thread is the **CaMKII → HDAC4** axis implicated for the *TPM1* E181K restrictive phenotype (PMC12818787) — HDAC4 nuclear export is the canonical link from Ca²⁺/CaMKII signaling to MEF2-dependent hypertrophic transcription, so this is a plausible (but for CMH3 unproven) route from altered myofilament Ca²⁺ handling to a transcriptional hypertrophy program. **Flag as a knowledge gap.** ENCODE/Roadmap/DiseaseMeth: nothing CMH3-specific.

### 4.6 Chromosomal abnormalities

**Not applicable.** CMH3 is caused by single-nucleotide missense substitutions. No aneuploidy, translocation, inversion, or recurrent CNV mechanism; chromosomal microarray has no diagnostic role (§10).

---

## 5. Environmental Information

- **Environmental factors:** none causal. No CTD/TOXNET chemical–disease association for CMH3. Elevated diastolic blood pressure is the best-supported *modifiable* factor in the broader HCM genetics literature (Harper 2021, Mendelian randomization).
- **Lifestyle factors:** high-intensity/competitive athletics as an SCD trigger context (HCM = leading cause of SCD in US athletes in historical series; most HCM deaths nonetheless occur at rest); systemic hypertension and obesity as afterload/expressivity modifiers; alcohol as an AF trigger. **Note:** dehydration/vasodilators/large meals precipitate LVOT obstruction symptoms in obstructive HCM — a pharmacologic/behavioral, not etiologic, exposure.
- **Infectious agents:** **not applicable** — no pathogen is implicated in CMH3.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (proposed dismech pathograph)

```
[MOLECULAR]  TPM1 missense variant (e.g. D175N, E180G, S215L, E62Q)
                 ↓  incorporation of mutant α-tropomyosin into the cardiac thin filament
[MOLECULAR]  Altered tropomyosin mechanics + regulatory-state equilibria
             (↓ coiled-coil stiffness / ↑ flexibility; destabilized blocked state;
              azimuthal shift toward closed/open positions on actin)
                 ↓
[MOLECULAR]  Increased Ca²⁺ sensitivity of thin-filament activation
             + residual cross-bridge activity at diastolic [Ca²⁺]
                 ↓
[CELLULAR]   Cardiomyocyte hypercontractility + impaired/incomplete relaxation
             (diastolic dysfunction) + inefficient ATP utilization / energetic cost
                 ↓
[CELLULAR]   Hypertrophic signaling activation (Ca²⁺/CaMKII → HDAC4/MEF2 proposed;
             GATA4, MYH7, NPPA, NPPB, FHL1 upregulation) → cardiomyocyte hypertrophy
                 ↓
[TISSUE]     Myocyte + myofibrillar disarray; interstitial and replacement fibrosis;
             microvascular remodeling/ischemia; atrial enlargement
                 ↓
[TISSUE]     Asymmetric LV/septal hypertrophy; LVOT obstruction (± SAM, mitral regurg.);
             arrhythmogenic substrate (dispersion of repolarization, reentry around fibrosis)
                 ↓
[ORGANISM]   Diastolic heart failure / advanced HF; ventricular tachyarrhythmia;
             atrial fibrillation; syncope; sudden cardiac death
```

Upstream = the tropomyosin mechanical/regulatory defect (molecular). Downstream = hypertrophy, fibrosis, arrhythmic substrate, heart failure (tissue/organism). The **energetic-inefficiency** and **impaired-relaxation** nodes are the ones on which the therapeutic myosin inhibitors act.

### 6.2 Molecular pathway detail — thin filament regulation

The three-state (blocked–closed–open) steric-blocking model is the pathway. HCM *TPM1* variants shift the equilibrium away from "blocked":

Bing W, et al. *Effect of hypertrophic cardiomyopathy mutations in human cardiac muscle alpha-tropomyosin (Asp175Asn and Glu180Gly) on the regulatory properties of human cardiac troponin determined by in vitro motility assay.* J Mol Cell Cardiol. 2000 Aug. **PMID:10900175**. Abstract, *verbatim* excerpt:

> "The expected switching off of reconstituted filament movement at pCa9, and switching on at pCa5, was observed with no difference in fraction of filaments motile or filament velocity, between wild-type and mutant filaments. However, we observed increased Ca(2+) sensitivity of fraction of filaments motile using the mutant tropomyosin compared to wild-type (DeltaEC(50) +0.082+/-0.019 pCa units for Asp175Asn and +0.115+/-0.021 for Glu180Gly). Indirect measurements using immobilized alpha-actinin to retard filament movement showed that filaments reconstituted with mutant AStm produced the same force as wild-type filaments."

Note the nuance for careful curation: in this human-protein reconstituted system the mutants **sensitize** Ca²⁺ activation but produce **the same force** — i.e. Ca²⁺ sensitization, not raw force gain, is the primary in-vitro signature, and E180G > D175N.

Supporting structural/biophysical evidence (all IN_VITRO / COMPUTATIONAL):
- **PMID:21376702** — D175N and E180G "shift tropomyosin strands further towards the open position during the ATPase cycle."
- **PMID:22794249** — long-range effects of E180G and D175N on tropomyosin properties; changed affinity for actin, effect of E180G > D175N.
- **PMID:9109674** — Golitsina et al., effects of the two mutations on α-tropomyosin structure and function.
- **PMID:15454401** — altered thermal unfolding of actin-bound tropomyosin.
- Loong et al., FEBS Lett. 2012 — E180G "markedly reduces persistence length, implying increased flexibility"; F-actin affinity of E180G similar to wild type.
- Halder et al. (below) — **quantified** stiffness loss: 21% measured / 57% predicted reduction in tropomyosin stiffness for E62Q; **54% reduction for S215L**.

### 6.3 Integrated mechanism — S215L pipeline (the best-documented full chain)

Halder SS, Rynkiewicz MJ, Creso JG, et al. *Mechanisms of pathogenicity in the hypertrophic cardiomyopathy-associated TPM1 variant S215L.* PNAS Nexus. 2023 Jan;2(1):pgad011. **PMID:36896133**. Abstract, *verbatim* excerpt:

> "These data form a mechanistic description of TPM1 S215L pathogenicity that starts with disruption of the mechanical and regulatory properties of tropomyosin, leading thereafter to hypercontractility and finally induction of a hypertrophic phenotype."

Findings: destabilization of the blocked regulatory state with increased tropomyosin chain flexibility; ~**1.0 pCa₅₀ unit** increase in Ca²⁺ sensitivity; MD-derived **54% reduction in tropomyosin stiffness**; Markov modeling predicting hypercontractile twitches and prolonged relaxation; engineered heart tissue showing **3-fold increased isometric contraction, 20% slower relaxation, greater diastolic stiffness, >3-fold increased cardiomyocyte volume**, and upregulation of **MYH7, BNP, ANP, GATA4, FHL1**; and a **greater relative drop in diastolic stress after acute mavacamten** in S215L, indicating elevated residual cross-bridge activity in diastole.

### 6.4 The force-homeostasis framework (HCM vs DCM within *TPM1*)

Halder SS, Rynkiewicz MJ, Kim L, Barry ME, Zied AGA, Sewanan LR, Kirk JA, Moore JR, Lehman WJ, Campbell SG. *Distinct mechanisms drive divergent phenotypes in hypertrophic and dilated cardiomyopathy–associated TPM1 variants.* J Clin Invest. 2024 Dec 16;134(24):e179135. **PMID:39436707**. Abstract, *verbatim* excerpt:

> "Heritable forms of hypertrophic cardiomyopathy (HCM) and dilated cardiomyopathy (DCM) represent starkly diverging clinical phenotypes, yet may be caused by mutations to the same sarcomeric protein. The precise mechanisms by which point mutations within the same gene bring about phenotypic diversity remain unclear. Our objective was to develop a mechanistic explanation of diverging phenotypes in two TPM1 mutations, E62Q (HCM) and E54K (DCM)."

Results: **E62Q** — >3-fold increase in peak force, 21% decreased tropomyosin stiffness (57% predicted), increased blocked→closed equilibrium constant favoring the closed state and preventing effective myosin inhibition. **E54K** — ~3-fold decrease in peak force, 42% faster time-to-peak, 50% faster relaxation, driven by long-range allosteric increase in the association rate of the troponin-I mobile domain to tropomyosin/actin, reducing myosin recruitment. The two residues are **only 8 amino acids apart on the same actin-binding repeat**. The unifying claim: **mutations that elevate baseline contractility drive hypertrophy (HCM); those that reduce it drive elongation without hypertrophy (DCM)** — a contractile-force-homeostasis / mechanosensing framework. Myosin modulators reversed both directions (mavacamten for E62Q, danicamtiv for E54K), which the authors take as confirmation that the framework transcends the specific molecular lesion.

This is the single most useful citation for a dismech `mechanistic_hypotheses` block on CMH3.

### 6.5 Cellular processes and downstream tissue mechanisms

- **Impaired relaxation / incomplete diastolic deactivation** → elevated diastolic stress, subendocardial and microvascular ischemia.
- **Energetic inefficiency** — excess tension cost per ATP; the classical "energy compromise" hypothesis for sarcomeric HCM. Direct *TPM1* ATPase-cycle evidence: PMID:21376702.
- **Ca²⁺ handling remodeling** — differential between variants in vivo: in transgenic rats, "Ca²⁺ sensitivity of cardiac skinned-fiber preparations from animals with mutation Asp175Asn, but not Glu180Gly, was decreased," and "elevated frequency and amplitude of spontaneous Ca²⁺ waves were detected only in cardiomyocytes from animals with mutation Asp175Asn" (AJP Regul Integr Comp Physiol 2004, doi 10.1152/ajpregu.00620.2003) — i.e. an arrhythmogenic Ca²⁺-wave phenotype specifically in D175N.
- **Tropomyosin phosphorylation as a modifiable node** — "Decreasing Tropomyosin Phosphorylation Rescues Tropomyosin-induced Familial Hypertrophic Cardiomyopathy" (PMC3789987) — a druggable-node hypothesis worth recording.
- **Fibrosis** — interstitial and replacement fibrosis; in dismech terms, CMH3 is a candidate conformer to `fibrotic_response` at the myocardial-fibrosis node, and to `cardiomyopathy_maladaptive_remodeling` (see §Curation notes).
- **Immune system involvement** — **not applicable**; no autoimmune or immunodeficiency component. Sterile inflammatory amplification of fibrosis is plausible but not documented specifically for CMH3.
- **Metabolic changes** — increased tension cost/ATP consumption and impaired energetics (inferred from the sarcomeric-HCM literature); no *TPM1*-specific metabolomic dataset. HMDB/Metabolomics Workbench: nothing CMH3-specific.

### 6.6 Suggested ontology terms for mechanism (all OAK-verified)

**GO biological process / molecular function:**
| Term | ID | Use |
|---|---|---|
| regulation of cardiac muscle contraction | GO:0055117 | core dysregulated process |
| regulation of cardiac muscle contraction by calcium ion signaling | GO:0010882 | Ca²⁺-sensitization node |
| regulation of muscle filament sliding | GO:0032971 | thin-filament gating |
| muscle filament sliding | GO:0030049 | cross-bridge cycling |
| regulation of actin filament-based movement | GO:1903115 | in-vitro motility readout |
| actin filament binding | GO:0051015 | α-tropomyosin MF |
| troponin T binding | GO:0031014 | residue 175/180 interaction region |
| cardiac muscle hypertrophy | GO:0003300 | downstream hypertrophy |
| positive regulation of cardiac muscle hypertrophy | GO:0010613 | signaling arm |
| sarcomere organization | GO:0045214 | disarray |
| ATP hydrolysis activity | GO:0016887 | energetics |
| regulation of calcium ion transport into cytosol | GO:0010522 | Ca²⁺-wave arm (D175N rat) |

**GO cellular component:** `GO:0030017` sarcomere, `GO:0030016` myofibril, `GO:0005884` actin filament, `GO:0005861` troponin complex, `GO:1990584` cardiac Troponin complex.

**CL cell types:** `CL:0000746` cardiac muscle cell; `CL:2000046` ventricular cardiac muscle cell (preferred for CMH3). Note `CL:0008023` cardiac fibroblast is **obsolete** — do not use; use a valid fibroblast term or omit.

**CHEBI:** `CHEBI:29108` calcium(2+); `CHEBI:15422` ATP.

### 6.7 Molecular profiling and advanced technologies

- **Transcriptomics:** hypertrophic marker induction (*MYH7*, *NPPA*, *NPPB*, *GATA4*, *FHL1*) in *TPM1* S215L engineered heart tissue (PMID:36896133). No published bulk or single-cell RNA-seq dataset of human CMH3 myocardium was identified. GEO/GTEx: nothing CMH3-specific.
- **Proteomics / metabolomics / lipidomics:** **no CMH3-specific dataset identified.** PRIDE/MetaboLights/LIPID MAPS: nothing found.
- **Single-cell and spatial transcriptomics:** **not available** for CMH3 specifically (general HCM myocardium snRNA-seq atlases exist but are not *TPM1*-stratified).
- **Structural/computational:** molecular dynamics of the actin–tropomyosin–troponin complex is the workhorse for CMH3 (PMID:36896133, PMID:39436707); Markov-model myofilament simulation ("Predicting Effects of Tropomyosin Mutations on Cardiac Muscle Contraction through Myofilament Modeling," Front Physiol 2016). AlphaFold/PDB: coiled-coil tropomyosin and cryo-EM thin-filament structures underpin the stiffness calculations.
- **Functional genomics screens (CRISPR/RNAi):** no *TPM1*-HCM screen identified; DepMap is not informative for this indication. CRISPR is used for **isogenic hiPSC-CM model construction**, not screening.
- **hiPSC-CM / engineered tissue:** the dominant modern platform. Patient-derived hiPSC-CMs carrying **TPM1-D175N** (Finnish founder) show "pathological phenotypes of HCM with differences in cellular size, Ca²⁺ handling, and electrophysiological properties" compared with MYBPC3-mutant lines (Ojala M, et al., PMC4707351). 3D genetically engineered heart tissues expressing *TPM1* variants show "hypercontractility, upregulation of hypertrophic gene markers, and diastolic dysfunction."

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ:** heart — **UBERON:0000948** (OAK-verified). Body system: cardiovascular.
- **Primary sub-structures:** **UBERON:0002084** heart left ventricle; **UBERON:0002094** interventricular septum (the characteristic *TPM1* anterior/septal distribution; `UBERON:0004667` interventricular septum muscular part for finer granularity); **UBERON:0002349** myocardium.
- **Secondary involvement:** left atrium (atrial enlargement, AF — atrial enlargement is an *early* feature in the α-TM180 mouse, within 1 month); mitral valve apparatus (SAM, mitral regurgitation); lungs (pulmonary congestion in diastolic HF); systemic circulation and brain (cardioembolic stroke from AF). Coronary microvasculature (microvascular remodeling/ischemia).

### Tissue and cell level
- **Tissue:** cardiac muscle tissue (striated muscle); cardiac interstitium/connective tissue (fibrosis).
- **Cells:** **CL:0000746** cardiac muscle cell / **CL:2000046** ventricular cardiac muscle cell (primary); cardiac fibroblasts (secondary, fibrotic arm — note the specific CL term is obsolete); endothelial cells of coronary microvasculature (secondary).

### Subcellular level
- **GO:0030017** sarcomere — the primary compartment; specifically the **thin (actin) filament** (`GO:0005884` actin filament) and the troponin–tropomyosin regulatory unit (`GO:0005861` troponin complex, `GO:1990584` cardiac Troponin complex).
- **GO:0030016** myofibril — the disorganized structure in myofibrillar disarray.
- Sarcoplasmic reticulum / cytosolic Ca²⁺ compartment implicated secondarily (Ca²⁺-wave phenotype in D175N rats).

### Localization / lateralization
- **Bilateral** in the sense of being a systemic genetic disease of the myocardium, but structurally **asymmetric**: septal-predominant, typically anterior septum, with a characteristically **asymmetric** hypertrophy pattern (`HP:0001670`). Left-ventricular predominant; right ventricular involvement uncommon. Apical and concentric variants occur.

---

## 8. Temporal Development

### Onset
- **Typical onset:** adolescent to adult. Mean age at diagnosis in a thin-filament HCM cohort (60% *TPM1*) was **44 years** (Chumakova 2025). Iberian R21L: cumulative diagnosis probability 50% by age 50 (males).
- **Pediatric/childhood onset occurs and can be lethal** — a novel *TPM1* missense pedigree with 12 affected members and 5 young deaths, described as a "malignant phenotype at young age" (PMID:12651045). Congenital onset is not typical for CMH3 (contrast the *TPM1* LVNC/RCM allelic phenotypes, which are pediatric).
- **Onset pattern:** insidious and chronic. Very often the first detectable abnormality is an **abnormal ECG preceding hypertrophy** — abnormal ECG was the strongest predictor of subsequent HCM development in mutation carriers (HR 4.02, PMID:32731933).
- Suggested `OnsetDescriptor`: `onset_category: ADULT_ONSET` at the entity level, with a documented pediatric/juvenile tail.

### Progression
- **Course:** chronic, lifelong, **progressive**, punctuated by **episodic** arrhythmic events. Never self-limited; spontaneous remission does not occur.
- **Stages:** (i) genotype-positive/phenotype-negative (G+/P−) — the surveillance stage, with subtle ECG/tissue-Doppler/CMR abnormalities; (ii) overt nonobstructive or obstructive HCM with preserved EF; (iii) adverse remodeling with progressive fibrosis, AF, and functional decline; (iv) end-stage/"burnt-out" HCM with systolic dysfunction (LVEF <50%) or restrictive physiology requiring advanced therapy/transplant.
- **Progression rate — thin-filament disease progresses faster to advanced HF.** Chumakova OS, Baklanova TN, Zateyshchikov DA. *Clinical Features and Prospective Outcomes of Thin-Filament Hypertrophic Cardiomyopathy.* J Clin Med. 2025;14(3):866, doi 10.3390/jcm14030866. Abstract, *verbatim*: **"In adults, thin-filament HCM is associated with a 'thinner' phenotype and a more rapid progression to advanced heart failure compared to thick-filament HCM. Data on a higher risk of malignant arrhythmias in thin-filament HCM remain controversial between studies."** Mean survival free of advanced HF: **"5.2 ± 0.64 years in the thin-filament group compared to 11.8 ± 1.04 years"** (thick-filament), HR 5.6, p=0.018; advanced HF 20% vs 7%.
- **Variant-dependent trajectory.** Finnish **D175N** is described as mild-to-moderate HCM with **favorable prognosis** and high adult penetrance (91–95%); the three D175N kindreds of Coviello 1997 had markedly different wall thickness but "survival was comparable and favorable." Conversely **V95A** was reported with a mild phenotype but **poor prognosis** (Karibe 2001), and some novel variants produce malignant young-onset disease (PMID:12651045). CMH3 is repeatedly singled out as "one of the clearest extreme examples of intra- and interfamilial variability among subjects carrying the same variant."

### Patterns
- **Remission:** none spontaneous. **Treatment-induced symptomatic remission** is achievable — LVOT gradient normalization and functional-class improvement with cardiac myosin inhibitors, myectomy, or alcohol septal ablation. This is symptom/hemodynamic remission, not disease reversal.
- **Critical periods / intervention windows:** (i) adolescence through the fourth–fifth decade — the highest-yield surveillance interval, when most conversion occurs; (ii) the **G+/P− window**, the target of prevention-of-phenotype trials; (iii) the peri-competitive-athletics period for SCD risk; (iv) pre-advanced-HF, before irreversible fibrosis accumulates (88% LGE prevalence in thin-filament disease argues this window is often already partly lost at diagnosis); (v) pregnancy and peripartum, requiring specialized management.

---

## 9. Inheritance and Population

### Epidemiology
- **HCM overall:** clinically detected prevalence ≈ **1 in 500 (0.2%)**; genotypic/subclinical prevalence estimated as high as ~1 in 200. HCM prevalence in highly trained athletes has been directly studied (PMID:18325444).
- **CMH3 share of HCM:** **~1–5%**, with important cohort dependence:
  - **~3%** of FHC classically (PMID:7898523).
  - **3.2%** of sarcomere-positive carriers: in 285 individuals from 156 families, gene distribution was MYBPC3 43.2%, MYH7 24.2%, TNNI3 13.7%, TNNT2 11.9%, **TPM1 3.2%**, MYL2 2.1%, ACTC1 0.4% (PMID:32731933).
  - **1.484%** of 4,447 HCM probands carried a rare protein-altering *TPM1* variant (cardiodb ACGV), of which ~94% are causal (etiological fraction 0.94) → ~1.4% attributable fraction.
  - Some contemporary series report **<1%**.
  - **Finland: 6.5–11%** (founder effect, below).
- **Derived CMH3 prevalence estimate:** ~1/500 × ~2% ≈ **~4 per 100,000** (`prevalence_class: BAND_1_9_PER_100000`), rising to perhaps ~20/100,000 in Finland. **This is a derivation, not a published figure** — curate as `notes` with the two source numbers, or use `prevalence_class` alone. Orphanet does not publish a CMH3-specific prevalence.
- **Incidence:** no CMH3-specific incidence figure available. HCM SCD incidence estimates range 0.5–13 per 100,000 in US data.

### Inheritance
- **Pattern:** **Autosomal dominant** (`HP:0000006`), monoallelic, with documented **de novo** occurrence (PMID:7729014). ClinGen records "monoallelic autosomal" as the genetic mechanism.
- **Penetrance: incomplete and age-dependent.** Lorenzini M, et al. JACC. 2020;76(5):550–559. **PMID:32731933** — 285 G+/P− carriers from 156 families, median age 14.2 y, 49.5% male; **"Estimated HCM penetrance at 15 years of follow-up was 46% (95% CI: 38% to 54%)"**; 86 (30.2%) developed HCM over median 8.0 y follow-up; independent predictors male sex (HR 2.91) and abnormal ECG (HR 4.02). **Gene-specific 15-year penetrance: TPM1 42%** (vs MYH7 66%, TNNT2 50%, MYBPC3 43%, TNNI3 17%).
  - Variant-specific penetrance differs sharply: Finnish **D175N** shows **high adult penetrance (91–95%)**, whereas Iberian **R21L** shows **late-onset, incomplete penetrance** — at age 70, 17% of male and 46% of female carriers remained unaffected (PMID:33642254).
- **Expressivity: highly variable**, both between and within families carrying the *same* variant — Coviello 1997 documented mean maximal wall thickness ranging 15±2.7 to 24±4.5 mm across three D175N kindreds; *TPM1* is cited as among the most extreme examples of intra/interfamilial variability in HCM.
- **Genetic anticipation:** **not applicable** — no repeat expansion mechanism; no anticipation reported.
- **Germline mosaicism:** not reported for *TPM1*; de novo variants are documented (PMID:7729014), so mosaicism cannot be excluded but is not established. **Knowledge gap.**
- **Founder effects — two well-documented:**
  1. **Finland, TPM1-D175N.** Jääskeläinen P, et al. *Two founder mutations in the alpha-tropomyosin and the cardiac myosin-binding protein C genes are common causes of hypertrophic cardiomyopathy in the Finnish population.* Ann Med. 2013. **PMID:22462493**. Abstract, *verbatim* excerpts: **"We screened for two founder mutations (TPM1-D175N and MYBPC3-Q1061X) in 306 unrelated Finnish patients with HCM from the regions covering a population of ∼4,000,000."** … **"The TPM1-D175N mutation was found in 20 patients (6.5%) and the MYBPC3-Q1061X in 35 patients (11.4%). Altogether, the two mutations accounted for 17.9% of the HCM cases. In addition, 61 and 59 relatives of the probands were found to be carriers of TPM1-D175N and MYBPC3-Q1061X, respectively. The mutations showed regional clustering. TPM1-D175N was prevalent in central and western Finland, and MYBPC3-Q1061X in central and eastern Finland."** In eastern Finland specifically, D175N accounted for ~11% of cases with haplotype evidence of a founder event (Jääskeläinen P, et al. *Genetics of hypertrophic cardiomyopathy in eastern Finland: few founder mutations with benign or intermediary phenotypes.* **PMID:15000344**). *TPM1* is the most prevalent thin-filament HCM gene in Finland (6–11%).
  2. **Iberia, TPM1-p.Arg21Leu.** PMID:33642254 — 25/4,099 (0.61%) HCM probands from 10,561 screened inherited-cardiac-disease probands; absent in 6,462 non-HCM controls (p<0.0001); 83 carriers in 31 pedigrees concentrated in **Galicia, Extremadura, and northern Portugal**, indicating a founder effect; pathogenic, late-onset/incomplete penetrance, generally favorable prognosis.
  - Additional recurrent-mutation caveat: the D175N G→A transition at nt 579 arose **independently** in multiple kindreds (Coviello 1997), so recurrence ≠ founder in every case.
- **Consanguinity:** no role — autosomal dominant, monoallelic disease.
- **Carrier frequency:** the concept does not apply as in recessive disease. The relevant population figure is the **rare *TPM1* variant frequency in reference populations: 0.086% (ExAC)**, with D175N at gnomAD v4.1 total AF <0.001%. In Finland, D175N carrier frequency is elevated relative to global (founder effect); a specific Finnish gnomAD figure was not retrieved.

### Population demographics
- **Higher-prevalence populations:** **Finns** (D175N, especially central/western Finland; 6.5% nationally, ~11% eastern Finland). **Galicians, Extremadurans, and northern Portuguese** (R21L). South African subpopulations have documented HCM founder profiles though not *TPM1*-specific in the retrieved source.
- **Geographic distribution of variants:** as above — D175N is pan-population but enriched in Finland; E180G is sporadic/global; R21L is Iberian; S215L, E62Q from North American/European cohorts; novel variants reported from India (PMC10784234) and Russia.
- **Sex ratio:** *TPM1* variants are transmitted 1:1, but **clinical expression is male-predominant**. Male sex HR 2.91 for phenotype conversion (PMID:32731933); R21L cumulative diagnosis by age 50 was 50% male vs 25% female (PMID:33642254). Ascertained clinical CMH3 cohorts should therefore be expected male-skewed; the underlying carrier sex ratio is 1:1.
- **Age distribution:** carriers span all ages; diagnosis clusters in the 4th–6th decades (mean 44 y in thin-filament cohort), with a clinically important pediatric/young-adult tail carrying disproportionate SCD risk.

---

## 10. Diagnostics

Diagnosis of CMH3 = clinical/imaging diagnosis of HCM + molecular confirmation of a pathogenic *TPM1* variant. The governing document is the **2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of Hypertrophic Cardiomyopathy**, Circulation/JACC 2024, **PMID:38718139**.

### Clinical / imaging tests
| Test | Role | Terms |
|---|---|---|
| **Transthoracic echocardiography** (± provocation/Valsalva, exercise stress echo) | First-line diagnosis: maximal wall thickness ≥15 mm (≥13 mm with family history), asymmetric septal hypertrophy, LVOT gradient, SAM, diastolic indices, LA size | NCIT:C16525 Echocardiography Test (OAK-verified) |
| **Cardiac MRI with late gadolinium enhancement** | Wall-thickness accuracy, apical/atypical variants, **fibrosis quantification** (LGE in 88% of thin-filament HCM — a key CMH3-relevant number), SCD risk refinement, phenocopy discrimination | NCIT cardiac-MRI term needs OAK lookup; RadLex applicable |
| **12-lead ECG** | Often the **earliest** abnormality, preceding hypertrophy; HR 4.02 for subsequent HCM in carriers (PMID:32731933) | HP:0003115 Abnormal EKG |
| **Ambulatory ECG (24–48 h / extended)** | NSVT detection for SCD risk stratification (13% NSVT in thin-filament cohort) | HP:0004756 |
| **Exercise testing / CPET (peak VO₂)** | Functional assessment; the SEQUOIA-HCM efficacy domain; exercise-induced hypotension as risk marker | — |
| **Cardiac biomarkers (NT-proBNP, hs-troponin)** | Prognostic/monitoring; NT-proBNP is a mavacamten dose-titration and monitoring input | LOINC applicable |
| **Endomyocardial biopsy / explant histopathology** | Not routine diagnostically; establishes the myocyte hypertrophy + disarray + replacement fibrosis triad (Coviello 1997) | — |
| **Electrophysiology study** | Selected cases; the D175N literature includes a study relating inducibility of life-threatening ventricular arrhythmias to maximum LV thickness and clinical SCD markers in D175N carriers (J Mol Cell Cardiol / Elsevier, S0022282803003237) | — |

### Genetic testing
- **Recommended approach:** multigene **cardiomyopathy/HCM panel** covering at minimum the definitive sarcomere genes (*MYH7, MYBPC3, TNNT2, TNNI3, TPM1, MYL2, MYL3, ACTC1, TNNC1*) plus phenocopy genes (*PRKAG2, GLA, LAMP2, TTR, DES, FHL1, ALPK3, FLNC, CSRP3, ACTN2, FHOD3, JPH2, TRIM63*), performed in the **proband** with pre-/post-test genetic counseling; followed by **targeted cascade (site-specific) testing** of at-risk relatives. This is a Class 1 pathway in the 2024 guideline (PMID:38718139) and the GTR/GeneReviews standard.
- **Single-gene *TPM1* testing:** appropriate only for cascade testing of a known familial variant, or in a founder population where a specific variant is being screened — the Finnish authors explicitly conclude: **"The TPM1-D175N and MYBPC3-Q1061X mutations account for a substantial part of all HCM cases in the Finnish population, indicating that routine genetic screening of these mutations is warranted in Finnish patients with HCM"** (PMID:22462493, *verbatim*).
- **WES/WGS:** reserved for panel-negative cases, syndromic presentations, or research; no established incremental yield for isolated HCM over a curated panel.
- **Variant interpretation caveats specific to *TPM1*:** (i) only **missense** variants are interpretable as HCM-causing — **truncating variants show zero case excess (OR 0.00)** and should not be reported as HCM-causal; (ii) ClinGen classifies TPM1–HCM as **Definitive**, so PP4/PS4-type evidence is usable; (iii) reference-population frequency for rare *TPM1* variants is only 0.086%, so BS1/BA1 thresholds are stringent; (iv) functional-modeling pipelines have been used to reclassify *TPM1* VUS (S215L, PMID:36896133) — an emerging PS3 evidence route.
- **Not applicable to CMH3:** chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, repeat-expansion testing. Each may be relevant in the *differential* (e.g. mtDNA testing for mitochondrial cardiomyopathy phenocopies, CMA for syndromic hypertrophy in infants) but not for CMH3 itself.

### Omics-based diagnostics
- **RNA-seq:** research use for splice-variant resolution; no established CMH3 diagnostic role.
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** **not applicable / not available** for CMH3 diagnosis.

### Clinical criteria and differential diagnosis
- **Criteria:** 2024 AHA/ACC HCM guideline (PMID:38718139) — LV wall thickness ≥15 mm (≥13 mm in relatives of affected individuals or genotype-positive individuals) not explained by abnormal loading conditions.
- **Differential diagnosis:**
  - *Physiologic:* athlete's heart; hypertensive LVH; aortic stenosis–related hypertrophy; obesity-related remodeling.
  - *Other genetic HCM:* MYBPC3, MYH7, TNNT2, TNNI3, TNNC1, MYL2, MYL3, ACTC1, ALPK3, FHOD3, CSRP3, ACTN2 — distinguished only by genotype.
  - *Phenocopies (critical to exclude, different treatment):* Fabry disease (*GLA*), Danon disease (*LAMP2*), PRKAG2 glycogen-storage cardiomyopathy, ATTR cardiac amyloidosis, Noonan/RASopathy cardiomyopathy, mitochondrial cardiomyopathy, Pompe disease (infantile), Friedreich ataxia cardiomyopathy.
  - *Other *TPM1* allelic entities:* CMD1Y (dilated), LVNC9, TPM1 restrictive cardiomyopathy — same gene, different phenotype; **do not merge with CMH3**.

### Screening
- **Cascade genetic screening** of first-degree relatives after proband variant identification — the cornerstone (Class 1).
- **Serial clinical surveillance of genotype-positive/phenotype-negative relatives** — ECG + echocardiography, typically every 1–2 years in children/adolescents and every 3–5 years in adults, informed by the 46% 15-year penetrance and the ECG-precedes-hypertrophy pattern (PMID:32731933).
- **Population/newborn screening:** **not indicated** and not performed.
- **Founder-variant population screening** is a defensible targeted strategy in Finland (PMID:22462493).

---

## 11. Outcome / Prognosis

### Survival and mortality
- No CMH3-specific survival curve exists. In the thin-filament cohort (60% *TPM1*), **all-cause mortality was 0** and **stroke 0** over 4.7 years' follow-up, with no significant mortality difference vs thick-filament HCM (Chumakova 2025) — a small cohort (n=15) whose zero-event arms should be read as low short-term event rates, not as absence of risk.
- Counterbalancing this, the historical α-tropomyosin literature emphasizes **"relatively mild and sometimes subclinical hypertrophy but a high incidence of sudden death"** (PMID:7898523), and specific pedigrees have been catastrophic (12 affected, 5 young deaths; PMID:12651045). **Prognosis in CMH3 is variant-specific, not gene-specific** — the single most important curation caveat for this entry.
- Variant-level prognosis: **D175N — favorable** ("survival was comparable and favorable," Coviello 1997; "mild-moderate HCM phenotype and favorable prognosis," Finnish cohorts). **R21L — generally favorable** (PMID:33642254). **V95A — mild phenotype but poor prognosis** (Karibe 2001 **[PMID UNVERIFIED]**). Contemporary registry analyses suggest *TNNI3* and *TPM1* trend toward higher risk of death/advanced therapies and a combined HF/arrhythmia endpoint than *MYH7*/*MYBPC3* groups.

### Morbidity and function
- **Advanced heart failure is the standout CMH3/thin-filament morbidity:** 20% vs 7% progression, with survival free of advanced HF 5.2 vs 11.8 years, HR 5.6 (Chumakova 2025).
- Other morbidity: exertional limitation, AF with stroke risk and anticoagulation burden, ICD implantation and its complications, need for septal reduction therapy (7% in thin-filament vs 17% thick-filament, p=0.025 — lower, consistent with less obstruction in a "thinner" phenotype).
- **Disability outcomes and ICF-coded functional data: not available** for CMH3.
- **QoL instruments:** KCCQ (HCM standard, used in EXPLORER-HCM and SEQUOIA-HCM), HCMSQ (HCM Symptom Questionnaire), SF-36/EQ-5D generically. No CMH3-specific PRO data.

### Disease course / complications
Sudden cardiac death; ventricular tachyarrhythmia; atrial fibrillation → cardioembolic stroke; progressive diastolic then systolic HF; "burnt-out"/end-stage HCM; infective endocarditis (rare, obstructive disease); pregnancy-related decompensation; procedural complications of myectomy/ablation (AV block, need for pacing). **Recovery potential:** the structural disease is not reversible with current therapy; symptomatic and hemodynamic recovery is achievable and often substantial.

### Prognostic factors
- Established HCM SCD risk factors (used by the 2024 guideline and HCM Risk-SCD): prior cardiac arrest/sustained VT, family history of SCD, unexplained syncope, maximal wall thickness, NSVT, LV apical aneurysm, LVEF <50%, and **extensive LGE on CMR** (particularly relevant here given 88% LGE prevalence in thin-filament disease). Note the thin-filament cohort had a *lower* 5-year HCM Risk-SCD score (2.0% vs 3.3%, p=0.002) despite worse HF trajectory — i.e. **conventional risk scores may under-call risk in thin-filament HCM**, since the scores are wall-thickness-weighted and thin-filament walls are thinner.
- **Genotype as prognostic factor:** sarcomere-positive status generally, and the specific *TPM1* variant, carry prognostic weight (D175N/R21L favorable vs V95A and malignant novel variants). **Polygenic score** modifies expressivity (Harper 2021).
- **Prognostic biomarkers:** NT-proBNP and hs-troponin (nonspecific but validated in HCM); **LGE burden** on CMR is arguably the strongest imaging biomarker. No *TPM1*-specific molecular prognostic biomarker exists.

---

## 12. Treatment

There is no CMH3-specific therapy; management follows HCM guidelines, and the mechanistic literature makes a strong case that **cardiac myosin inhibition is particularly rational for *TPM1* HCM** (below). Governing document: **PMID:38718139** (2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM guideline).

### 12.1 Pharmacotherapy

| Treatment | Mechanism | Suggested NCIT | Modality |
|---|---|---|---|
| **Beta blockers** (metoprolol, propranolol, bisoprolol) | First-line for obstructive and symptomatic HCM; ↓HR, ↑diastolic filling, ↓dynamic gradient | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` **NCIT:C61845** Metoprolol (OAK-verified) | SMALL_MOLECULE |
| **Non-dihydropyridine CCB** (verapamil, diltiazem) | Alternative first-line when beta blockers not tolerated; caution in severe obstruction/high gradients | `NCIT:C15986` + **NCIT:C928** Verapamil (OAK-verified) | SMALL_MOLECULE |
| **Disopyramide** | Negative inotrope added to beta blocker/CCB for refractory obstruction | `NCIT:C15986` + **NCIT:C61730** Disopyramide (OAK-verified) | SMALL_MOLECULE |
| **Mavacamten** | **Cardiac myosin inhibitor** — reduces actin–myosin cross-bridge formation, ↓contractility, ↓LVOT gradient; FDA-approved for symptomatic obstructive HCM; REMS program (echo LVEF monitoring, CYP2C19/CYP3A4 interactions) | `NCIT:C15986` + **NCIT:C174901** Mavacamten (OAK-verified); consider `NCIT:C93352` Targeted Therapy | SMALL_MOLECULE |
| **Aficamten** | Next-generation cardiac myosin inhibitor; SEQUOIA-HCM positive | `NCIT:C15986` + **NCIT:C179072** Aficamten (OAK-verified) | SMALL_MOLECULE |
| **Anticoagulation** (DOAC preferred) | AF thromboembolic prophylaxis — Class 1 in HCM regardless of CHA₂DS₂-VASc | `NCIT:C15986` + agent term | SMALL_MOLECULE |
| **Antiarrhythmics** (amiodarone, sotalol), **rate control** | AF rhythm/rate control; VT suppression adjunct to ICD | `NCIT:C15986` | SMALL_MOLECULE |
| **Standard HF therapy** (ACEi/ARB/ARNI, beta blocker, MRA, SGLT2i) | Only in the **end-stage/systolic** phase — vasodilators and afterload reduction are otherwise **contraindicated** in obstructive HCM | `NCIT:C15986` | SMALL_MOLECULE |
| **Avoid:** dihydropyridine CCB, high-dose diuretics, nitrates, digoxin, other positive inotropes in obstructive disease | Worsen gradient | — | — |

**Why myosin inhibition is mechanistically apt for CMH3:** the *TPM1* lesion is loss of the tropomyosin-mediated block on myosin access to actin, producing residual diastolic cross-bridge activity and hypercontractility. Direct myosin inhibition acts immediately downstream. Two independent *TPM1* studies show rescue: mavacamten normalized the E62Q hypercontractile phenotype (danicamtiv normalized the E54K hypocontractile DCM phenotype) — PMID:39436707; and in S215L engineered tissue, myosin inhibition produced a **"greater relative drop in diastolic stress after acute mavacamten"** than in wild type, confirming elevated residual cross-bridge activity as the target — PMID:36896133. These are IN_VITRO / COMPUTATIONAL evidence, not CMH3 clinical trial data, and must be tagged as such.

**Pharmacogenomics:** **CYP2C19** genotype materially affects mavacamten exposure (poor metabolizers require lower dosing; labeled dosing is CYP2C19-informed) — check PharmGKB/CPIC and the FDA label before curating specifics. No *TPM1*-genotype-guided drug selection exists.

### 12.2 Advanced therapeutics
- **Gene therapy / gene editing:** no clinical program for *TPM1*. AAV-based approaches are furthest advanced for *MYBPC3* HCM (e.g. TN-201) and *PKP2* ACM; base/prime editing of dominant missense sarcomere alleles is preclinical. **Not available for CMH3.**
- **RNA-based therapies (ASO, siRNA):** conceptually attractive for a dominant missense allele (allele-selective knockdown), but **no *TPM1* program identified**. Worth recording as a rational-but-absent modality; dismech's `antisense_oligonucleotide_therapy` module is the relevant reference pattern if one emerges.
- **Cell therapy / immunotherapy:** not applicable.
- **Targeted therapy:** the cardiac myosin inhibitors are the de facto targeted therapy class; also of note, "**Decreasing tropomyosin phosphorylation rescues tropomyosin-induced familial hypertrophic cardiomyopathy**" (PMC3789987, MODEL_ORGANISM) identifies tropomyosin phosphorylation as an unexploited target, and transgenic rescue was demonstrated in the α-TM mouse (AJP Heart 2007, doi 10.1152/ajpheart.01341.2006).

### 12.3 Surgical and interventional
| Intervention | Role | NCIT |
|---|---|---|
| **Surgical septal myectomy** | Gold standard for drug-refractory severe LVOTO at experienced centers; low mortality, durable gradient relief | Needs OAK lookup — `NCIT:C15329` Surgical Procedure or a specific cardiac-surgery term |
| **Alcohol septal ablation** | Percutaneous alternative in selected anatomy/comorbidity | **NCIT:C80439** Septal Ablation (OAK-verified) |
| **ICD implantation** | Secondary prevention (Class 1) and primary prevention by risk stratification | **NCIT:C80435** Implantable Cardioverter-Defibrillator Placement / **NCIT:C93238** device (OAK-verified) |
| **Heart transplantation** | End-stage/burnt-out HCM or intractable arrhythmia | **NCIT:C15246** Heart Transplantation (OAK-verified) |
| Mitral valve intervention; AF catheter ablation; LAA occlusion | Adjunctive | — |

Guideline framing (2024): "Invasive septal reduction therapies (surgical septal myectomy and alcohol septal ablation), when performed by experienced HCM teams at dedicated centers, can provide safe and effective symptomatic relief for patients with drug-refractory or severe outflow tract obstruction"; and following mavacamten's approval the guideline "now includes it as an option before more invasive therapies when first-line treatments like beta blockers or calcium channel blockers are not effective."

### 12.4 Supportive, rehabilitative, lifestyle
- **Genetic counseling** — **NCIT:C15240** Genetic Counseling (OAK-verified); modality `BEHAVIORAL`.
- **Cardiac rehabilitation / supervised exercise** — the 2024 guideline substantially **liberalized** exercise and return-to-play recommendations relative to prior guidance, endorsing an expanded role for exercise with shared decision-making. Suggested `NCIT:C15315` Rehabilitation / `NCIT:C15302` Physical Therapy.
- **Multidisciplinary HCM center care and shared decision-making** — explicit guideline recommendation: patients "should be engaged in shared decision making to develop a care plan, with multidisciplinary HCM centers helping to confirm diagnosis, facilitate genetic testing, and guide advanced treatment options." `NCIT:C15747` Supportive Care.
- Volume/hydration management, avoidance of dehydration and precipitants; pregnancy planning and specialized peripartum care.

### 12.5 Experimental treatments / clinical trials
- **NCT03470545** — EXPLORER-HCM, phase 3, mavacamten in symptomatic obstructive HCM; **primary and all secondary endpoints met (p≤0.0006)**.
- **NCT03723655** — MAVA-LTE, long-term safety extension for EXPLORER-HCM/MAVERICK-HCM completers.
- **NCT05186818** — SEQUOIA-HCM, phase 3, aficamten; "aficamten compared with placebo led to significant improvements in peak oxygen uptake, symptoms, and health status and reductions in LVOT gradients at rest and with Valsalva maneuver"; benefit extended to patients with mild symptoms (PMC12539928).
- MAVERICK-HCM (nonobstructive HCM, mavacamten); ODYSSEY-HCM and other nonobstructive-HCM myosin-inhibitor programs; *MYBPC3* gene-therapy trials (not applicable to *TPM1*).
- **No CMH3- or *TPM1*-specific interventional trial exists.** Trials enroll by phenotype (obstructive/nonobstructive HCM), not genotype.

### 12.6 Treatment strategy / algorithm
1. Confirm HCM and exclude phenocopies (CMR, Fabry/amyloid/Danon workup as indicated).
2. Genetic testing + cascade screening; genetic counseling.
3. SCD risk stratification → ICD decision.
4. Obstructive + symptomatic: beta blocker → non-DHP CCB → add disopyramide **or** cardiac myosin inhibitor → septal reduction therapy (myectomy or alcohol ablation).
5. Nonobstructive + symptomatic: beta blocker/CCB, diuretics cautiously, treat AF, consider myosin inhibitor per emerging evidence.
6. AF: anticoagulate (Class 1), rate/rhythm control, consider ablation.
7. End-stage (LVEF <50%): guideline-directed HF therapy → advanced therapies/transplant.
8. Lifelong surveillance; family surveillance of G+/P− relatives.

**Combination therapy** is the norm (beta blocker + disopyramide; beta blocker + myosin inhibitor; anticoagulant + rate control). **Personalized medicine:** currently genotype informs *diagnosis, family screening, and prognostic counseling* rather than drug choice; CYP2C19 genotype informs mavacamten dosing; the force-homeostasis framework (PMID:39436707) is the first credible basis for **genotype-directed modulator selection** (myosin inhibitor for hypercontractile variants, myotrope for hypocontractile ones) — currently preclinical.

---

## 13. Prevention

- **Primary prevention (of disease occurrence):** not possible for a monogenic dominant disorder. Reproductive prevention options: **preimplantation genetic testing for monogenic disease (PGT-M)** and **prenatal diagnosis** for a known familial *TPM1* variant; genetic counseling for 50% transmission risk. Prevention of *phenotype* in carriers is an active research question — the modifiable-risk-factor finding (diastolic BP; Harper 2021) and the concept of pre-emptive myosin inhibition in G+/P− carriers are the leading directions; neither is guideline-endorsed.
- **Secondary prevention (early detection):** **cascade genetic testing** of first-degree relatives plus **serial ECG/echo surveillance of genotype-positive relatives** — the highest-value intervention in CMH3, justified by 46% 15-year penetrance and the ECG-precedes-hypertrophy pattern (PMID:32731933). Targeted founder-variant screening is defensible in Finland (PMID:22462493). Pre-participation athlete screening is the population-level analogue.
- **Tertiary prevention (of complications):** ICD for SCD; anticoagulation for AF-related stroke; septal reduction/myosin inhibition to prevent HF progression; endocarditis and precipitant avoidance; specialized pregnancy management; treatment of hypertension and obesity to limit expressivity.
- **Immunization:** not disease-specific; standard influenza/COVID/pneumococcal vaccination is reasonable in patients with structural heart disease. Not a CMH3 prevention strategy.
- **Risk stratification:** HCM Risk-SCD / 2024 AHA-ACC risk-marker approach, with the caveat that thin-filament HCM had a *lower* calculated 5-year SCD score despite worse HF trajectory (Chumakova 2025) — potential under-estimation.
- **Genetic counseling:** Class 1; covers 50% transmission, incomplete/age-dependent and sex-modified penetrance, extreme intrafamilial variability, PGT-M/prenatal options, and insurance/psychosocial implications. **NCIT:C15240**.
- **Behavioral interventions:** BP and weight control; avoidance of dehydration and known precipitants; individualized (and, per 2024, substantially liberalized) exercise prescription with shared decision-making.
- **Public health / environmental interventions:** not applicable beyond athlete screening programs and public AED/CPR availability, which reduce SCD case fatality rather than disease incidence.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs
- **Homo sapiens** — NCBITaxon:9606 (the disease entity).
- Orthologs of *TPM1* exist across vertebrates and are highly conserved (tropomyosin is among the most conserved cytoskeletal/contractile proteins): *Mus musculus* `Tpm1` (NCBITaxon:10090), *Rattus norvegicus* `Tpm1` (NCBITaxon:10116), *Danio rerio* `tpma` (NCBITaxon:7955). Specific NCBI Gene IDs should be looked up before curation rather than asserted here.

### Natural disease in other species
- **No naturally occurring *TPM1*-associated hypertrophic cardiomyopathy has been reported in any non-human species.** A targeted OMIA search returned feline HCM loci in **MYBPC3** (Maine Coon **A31P**, Ragdoll **R820W**; OMIA:000515-9685), **MYH7** (OMIA:002212-9685), **ALMS1** (OMIA:002316-9685), and **TNNT2** — but **no TPM1 entry for cat or dog**. Feline HCM is the closest naturally occurring animal counterpart of human HCM: HCM prevalence was highest in Maine Coon **A31P homozygotes** with penetrance increasing with age, and the A31P/R820W variants are breed-restricted (2013 survey).
- **Breed (VBO):** not applicable to *TPM1*; VBO terms for Maine Coon and Ragdoll would apply to the MYBPC3 feline entity, not CMH3.
- **Veterinary relevance:** feline HCM is a major cause of morbidity/mortality in cats and a well-used spontaneous large-animal model of human HCM pathophysiology — but as a **gene-non-identical** comparator for CMH3.

### Comparative biology
- **Comparative pathology:** the myocyte hypertrophy / myofibrillar disarray / interstitial fibrosis triad is conserved across human HCM, feline HCM, and the *TPM1* transgenic rodents (§15) — supporting that the tissue-level program is species-general.
- **Evolutionary conservation of mechanism:** tropomyosin's period/coiled-coil architecture, its actin-groove positioning, and the three-state steric-blocking regulatory mechanism are conserved from invertebrates to mammals; residues 175/180 lie in a conserved troponin-T-interaction region. This conservation is what makes rodent transgenesis informative, and it is also why the human-vs-rodent isoform and troponin-partner context matters (see the isoform caveat in PMID:10900175).
- **Zoonotic potential / cross-species transmission:** **not applicable** — genetic, non-communicable.

---

## 15. Model Organisms

### 15.1 Transgenic mouse — α-TM180 (Glu180Gly): the flagship in vivo model
*A familial hypertrophic cardiomyopathy alpha-tropomyosin mutation causes severe cardiac hypertrophy and death in mice.* J Mol Cell Cardiol. 2001. **PMID:11603924** (Prasad/Wieczorek-lab lineage; the first in vivo transgenic systems for thin-filament HCM mutations).

- Construct: cardiac-restricted expression of α-tropomyosin with **Glu180Gly**, a substitution "which occurs in a troponin T binding region."
- Phenotype: initial pathologic changes — **ventricular concentric hypertrophy, fibrosis, and atrial enlargement — detected within 1 month**; progressive worsening with **death between 4 and 5 months** (a companion review states mice "die by 6 months of age" — note this minor discrepancy across sources and cite the primary paper).
- Physiology: significant **diastolic dysfunction**; myofilaments show **increased thin-filament activation through enhanced Ca²⁺ sensitivity of steady-state force**.
- Histology: concentric LV hypertrophy, interstitial fibrosis, **myocyte disarray**.
- Contrast with the **D175N mouse**, which has **normal heart weight-to-body weight ratio with only patchy areas of myocyte hypertrophy** — i.e. the mouse models **recapitulate the human genotype–severity gradient (E180G ≫ D175N)**, which is a genuinely strong validity argument for this model pair.

### 15.2 Transgenic rat — D175N vs E180G
*α-Tropomyosin mutations Asp175Asn and Glu180Gly affect cardiac function in transgenic rats in different ways.* Am J Physiol Regul Integr Comp Physiol. 2004; doi 10.1152/ajpregu.00620.2003. Key results: "Ca²⁺ sensitivity of cardiac skinned-fiber preparations from animals with mutation Asp175Asn, but not Glu180Gly, was decreased," and "elevated frequency and amplitude of spontaneous Ca²⁺ waves were detected only in cardiomyocytes from animals with mutation Asp175Asn." A companion paper analyzed autonomic cardiac control/HRV variability in these rats (Biomed Tech 2007, doi 10.1515/BMT.2007.010). **Important nuance:** the rat D175N Ca²⁺-sensitivity direction is *opposite* to the human in-vitro motility result (PMID:10900175) — a real cross-system discordance, and a good candidate for a dismech `HUMAN_MODEL_MISMATCH` discussion.

### 15.3 Rescue / mechanism-probing models
- *Rescue of tropomyosin-induced familial hypertrophic cardiomyopathy mice by transgenesis.* Am J Physiol Heart Circ Physiol. 2007; doi 10.1152/ajpheart.01341.2006.
- *Decreasing Tropomyosin Phosphorylation Rescues Tropomyosin-induced Familial Hypertrophic Cardiomyopathy* (PMC3789987) — identifies tropomyosin phosphorylation as a modifiable disease node.
- *Functional effects of a tropomyosin mutation linked to FHC contribute to maladaptation during acidosis* (PMC3035739) — the gene–environment (acidosis) model.

### 15.4 Human cellular models (the current workhorses)
- **Patient-derived hiPSC-CMs, TPM1-D175N** (Finnish founder): "displayed pathological phenotypes of HCM with differences in cellular size, Ca²⁺ handling, and electrophysiological properties" relative to MYBPC3-mutant lines — Ojala M, et al., PMC4707351. Model type: iPSC-derived cardiomyocyte, patient-specific.
- **Isogenic CRISPR-edited hiPSC-CM + 3D engineered heart tissue (EHT)** for S215L, E62Q, E54K — Halder et al., PMID:36896133 and PMID:39436707. Readouts: isometric twitch force, relaxation kinetics, diastolic stiffness, cardiomyocyte volume, hypertrophic marker qPCR, acute drug response (mavacamten, danicamtiv). This platform is currently the best available human-context model of CMH3.
- **Reconstituted in-vitro systems:** recombinant human α-tropomyosin with N-terminal Ala-Ser extension (to mimic acetylation) + purified native human cardiac troponin, in-vitro motility assay (PMID:10900175); actin-bound tropomyosin thermal unfolding (PMID:15454401); ATPase-cycle strand-position measurements (PMID:21376702).
- **Computational models:** Markov-state myofilament models and all-atom MD of the actin–Tm–Tn complex; "Predicting Effects of Tropomyosin Mutations on Cardiac Muscle Contraction through Myofilament Modeling" (Front Physiol 2016).

### 15.5 Genetic model types available
Transgenic overexpression (mouse, rat — the historical standard for *TPM1*); CRISPR knock-in isogenic hiPSC lines (current standard for human context). Knock-in mouse models of specific *TPM1* HCM alleles at the endogenous locus are less prominent in the literature than the transgenic lines — worth verifying against **MGI/IMSR** before asserting availability. Conditional and humanized *Tpm1* models: **not identified**.

### 15.6 Phenotype recapitulation and limitations

**Recapitulated:** concentric/asymmetric hypertrophy, interstitial fibrosis, myocyte disarray, atrial enlargement, diastolic dysfunction, increased myofilament Ca²⁺ sensitivity, premature death (E180G mouse), and — importantly — the **variant-severity ordering** (E180G > D175N).

**Limitations (candidate `HUMAN_MODEL_MISMATCH` items):**
1. **Transgenic overexpression** does not reproduce the human 1:1 mutant:wild-type allelic stoichiometry, and Thierfelder's own hypothesis was that *stoichiometry itself* matters.
2. **Isoform/partner context is decisive and species-divergent.** PMID:10900175 explicitly concludes: *"The results using human cardiac regulatory proteins reveal different effects of the HCM mutations in tropomyosin compared to studies using heterologous systems"* — i.e. non-human/heterologous systems can give the wrong answer for *TPM1*.
3. **Direction-of-effect discordance:** rat D175N showed *decreased* skinned-fiber Ca²⁺ sensitivity while human reconstituted filaments showed *increased* Ca²⁺ sensitivity.
4. **Rodent heart rate, β-MHC/α-MHC isoform composition, and Ca²⁺-handling kinetics** differ fundamentally from human, limiting translation of relaxation/energetics phenotypes.
5. **hiPSC-CMs are immature** (fetal-like sarcomere, ion channel, and metabolic profile), lack chronic hemodynamic loading, and cannot model LVOT obstruction, arrhythmic SCD, or decades-long fibrotic remodeling.
6. **No animal model reproduces sudden cardiac death** as the human clinical endpoint, nor human penetrance/expressivity variability.
7. **No natural animal *TPM1* HCM** exists to serve as a spontaneous-disease comparator.

### 15.7 Research applications
Thin-filament regulatory mechanism and Ca²⁺-sensitivity measurement; tropomyosin mechanics (stiffness/persistence length); genotype-specific contractile phenotyping (hyper- vs hypocontractile); hypertrophic gene-program induction; drug screening and acute pharmacologic rescue (mavacamten, danicamtiv, tropomyosin-phosphorylation modulation); VUS reclassification pipelines (the S215L precedent); gene–environment stress testing (acidosis).

### 15.8 Model resources
MGI (mouse *Tpm1*), RGD (rat *Tpm1*), ZFIN (*tpma*), Alliance of Genome Resources, IMSR/MMRRC/EMMA for strain availability, Cellosaurus for hiPSC lines. Specific strain and line accessions should be pulled from MGI/IMSR at curation time rather than inferred.

---

## Curation notes for the dismech entry

**Confirmed correct in the existing draft:** `disease_term` MONDO:0007267 / label `hypertrophic cardiomyopathy 3` (OAK-verified), `category: Genetic`, synonyms, `parents: [Hypertrophic Cardiomyopathy, Genetic Disorder]`.

**Module conformance candidates** (declare with `conforms_to`, substituting the *TPM1*-specific driver):
- `cardiomyopathy_maladaptive_remodeling` — the structural/contractile HCM module; key target `#Ventricular Remodeling`. **Primary conformance target for this entry.**
- `fibrotic_response` — at the myocardial-fibrosis node (88% LGE; replacement fibrosis on histology).
- `cardiac_ion_channel_repolarization` — **use with care.** That module is explicitly scoped to inherited arrhythmia syndromes *in structurally normal hearts*; CMH3 arrhythmia is substrate-driven (fibrosis/disarray). A partial conformance at the `#Arrhythmogenic Substrate and Triggered Activity` node is defensible for the D175N spontaneous-Ca²⁺-wave arm (rat data), but should be flagged rather than asserted broadly.

**Suggested `mechanistic_hypotheses` groups:**
1. `force_homeostasis_hcm_dcm_divergence` (status `EMERGING`) — hypercontractility → hypertrophy vs hypocontractility → dilation, anchored on PMID:39436707. Edges from the hypercontractility node to the hypertrophy node opt in.
2. `camkii_hdac4_hypertrophic_signaling` (status `EMERGING`) — the Ca²⁺/CaMKII → HDAC4 route from myofilament Ca²⁺ sensitization to a transcriptional program; anchored on the *TPM1* E181K RCM work (PMC12818787), and explicitly **extrapolated** from a different *TPM1* phenotype — mark as such.
3. `tropomyosin_phosphorylation_as_target` (status `EMERGING`) — PMC3789987, MODEL_ORGANISM.

**Suggested `discussions` entries:**
- `kind: HUMAN_MODEL_MISMATCH` — human reconstituted filaments show *increased* Ca²⁺ sensitivity for D175N (PMID:10900175) while transgenic rat skinned fibers show *decreased* Ca²⁺ sensitivity (AJP Regul 2004); and PMID:10900175 states directly that heterologous systems give different answers. Propose: isogenic human hiPSC-CM/EHT measurement of D175N Ca²⁺ sensitivity with human cardiac troponin.
- `kind: KNOWLEDGE_GAP` — no CMH3-specific transcriptomic, proteomic, metabolomic, or single-cell dataset; no CMH3-specific survival curve; no *TPM1*-genotype-stratified myosin-inhibitor trial data; germline mosaicism unassessed; no epigenomic data.
- `kind: KNOWLEDGE_GAP` — conventional wall-thickness-weighted SCD risk scores may systematically under-call risk in thin-filament HCM (5-y score 2.0% vs 3.3% despite worse HF trajectory; Chumakova 2025), yet the classical literature reports "high incidence of sudden death" for α-tropomyosin mutations (PMID:7898523). This tension is unresolved and clinically consequential.

**Evidence-source tagging reminders:** PMID:8205619, 7898523, 7729014, 22462493, 15000344, 32731933, 33642254, 12651045, 38718139, Chumakova 2025, Coviello 1997 → `HUMAN_CLINICAL`. PMID:11603924, AJP Regul 2004, AJP Heart 2007, PMC3789987 → `MODEL_ORGANISM`. PMID:10900175, 9109674, 15454401, 21376702, 22794249, PMC4707351, PMC3035739 → `IN_VITRO`. PMID:36896133 and 39436707 are **mixed** (MD/Markov modeling + hiPSC-CM/EHT experiments) — **split into separate evidence items**, one `COMPUTATIONAL` and one `IN_VITRO`, per the repo rule that each item carries a single `evidence_source`. PMID:39132495 (ClinGen) and cardiodb ACGV burden statistics → `OTHER` (expert-panel consensus / aggregate case–control resource).

**NEC preflight result (per CLAUDE.md §2b):** clean. MONDO:0007267's `def:` and logical definition name **TPM1** (`RO:0004003 HGNC:12010`); the OMIM xref is **115196**, matching every source used; and the synonyms `CMH3` / `TPM1 hypertrophic cardiomyopathy` are the exact labels the literature keyed off. No gene-frequency or OMIM mismatch. **However, CMH3 sits in a high-NEC-risk class** — it is a numbered series (CMH1–CMH27) *and* the gene is pleiotropic across four cardiomyopathy phenotypes. Two concrete confusion traps to guard against: (i) **CMH3 vs other numbered CMH entries** (CMH1/MYH7, CMH2/TNNT2, CMH4/MYBPC3 …); (ii) **CMH3 vs the *TPM1* allelic non-HCM entities** — CMD1Y, LVNC9, and *TPM1* restrictive cardiomyopathy. Note especially that **E180G (HCM) and E181K (restrictive) are adjacent residues in the same gene** — any DR report mixing these must be treated as suspect.

**Structured-source citations available for this entry:** an `ORPHA:` record for familial HCM and, most valuably, a **`CGGV:` ClinGen Gene-Disease Validity record for TPM1–HCM (Definitive)** — that assertion row is a cleaner, snippet-validatable evidence anchor for the gene–disease claim than the PMID:39132495 abstract. Run `just clingen-list` / `just clingen-rebuild --id CGGV:<id>` to locate and cache it.

---

## Sources

- [OMIM 115196 — Cardiomyopathy, familial hypertrophic, 3](https://omim.org/entry/115196) (403 on direct fetch; content accessed via MedGen/MONDO mirrors)
- [OMIM *191010 — TPM1](https://omim.org/entry/191010)
- [MedGen C1861863 — Hypertrophic cardiomyopathy 3](https://www.ncbi.nlm.nih.gov/medgen/?term=Hypertrophic+cardiomyopathy+3)
- [MONDO:0007267 (local OAK `sqlite:obo:mondo`)](https://monarchinitiative.org/MONDO:0007267)
- [GTR — Hypertrophic cardiomyopathy 3](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1861863/)
- [Thierfelder et al., Cell 1994 — PMID:8205619](https://pubmed.ncbi.nlm.nih.gov/8205619/)
- [Watkins et al., NEJM 1995 — PMID:7898523](https://pubmed.ncbi.nlm.nih.gov/7898523/)
- [Watkins et al., de novo TPM1 mutation — PMID:7729014](https://pubmed.ncbi.nlm.nih.gov/7729014/)
- [Bing et al., J Mol Cell Cardiol 2000 — PMID:10900175](https://pubmed.ncbi.nlm.nih.gov/10900175/)
- [Golitsina et al. — PMID:9109674](https://pubmed.ncbi.nlm.nih.gov/9109674/)
- [Tm strand position/ATPase cycle — PMID:21376702](https://pubmed.ncbi.nlm.nih.gov/21376702/)
- [Long-range effects of E180G and D175N — PMID:22794249](https://ncbi.nlm.nih.gov/pmc/articles/PMC3447992)
- [Thermal unfolding of actin-bound Tm — PMID:15454401](https://pubmed.ncbi.nlm.nih.gov/15454401/)
- [Loong et al., FEBS Lett 2012 — E180G flexibility](https://febs.onlinelibrary.wiley.com/doi/pdf/10.1016/j.febslet.2012.08.005)
- [Halder et al., J Clin Invest 2024 — PMID:39436707](https://pmc.ncbi.nlm.nih.gov/articles/PMC11645150/)
- [Halder et al., PNAS Nexus 2023 (S215L) — PMID:36896133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9991458/)
- [Prasad et al., α-TM180 mouse — PMID:11603924](https://pubmed.ncbi.nlm.nih.gov/11603924/)
- [Transgenic rats D175N vs E180G — AJP Regul 2004](https://journals.physiology.org/doi/full/10.1152/ajpregu.00620.2003)
- [Transgenic rescue — AJP Heart 2007](https://journals.physiology.org/doi/full/10.1152/ajpheart.01341.2006)
- [Decreasing tropomyosin phosphorylation rescues FHC — PMC3789987](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3789987/)
- [Tropomyosin mutation and acidosis — PMC3035739](https://pmc.ncbi.nlm.nih.gov/articles/PMC3035739/)
- [Ojala et al., hiPSC-CM MYBPC3 vs TPM1 — PMC4707351](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4707351/)
- [Jääskeläinen et al., Ann Med — PMID:22462493](https://pubmed.ncbi.nlm.nih.gov/22462493/)
- [Genetics of HCM in eastern Finland — PMID:15000344](https://pubmed.ncbi.nlm.nih.gov/15000344/)
- [TPM1 p.Arg21Leu Portugal/Spain — PMID:33642254](https://pubmed.ncbi.nlm.nih.gov/33642254/)
- [Variable clinical manifestation of a novel TPM1 mutation — PMID:12651045](https://pubmed.ncbi.nlm.nih.gov/12651045/?dopt=Abstract)
- [Coviello et al., JACC 1997 — "hot spot" in the alpha-tropomyosin gene](https://www.sciencedirect.com/science/article/pii/S0735109796005384)
- [Karibe et al., Circulation 2001 — TPM1 V95A](https://www.ahajournals.org/doi/10.1161/01.CIR.103.1.65)
- [Inducibility of VT in Asp175Asn carriers — J Mol Cell Cardiol 2003](https://www.sciencedirect.com/science/article/abs/pii/S0022282803003237)
- [Lorenzini et al., JACC 2020 — PMID:32731933](https://pubmed.ncbi.nlm.nih.gov/32731933/)
- [ClinGen HCVD-GCEP HCM reappraisal — PMID:39132495](https://pmc.ncbi.nlm.nih.gov/articles/PMC11312670/)
- [ClinGen — Genes associated with HCM: a reappraisal](https://clinicalgenome.org/docs/genes-associated-with-hypertrophic-cardiomyopathy-a-reappraisal-by-the-clingen-hereditary-cardiovascular-disease-gene-curation/)
- [Atlas of Cardiac Genetic Variation — TPM1 in HCM (cardiodb)](https://www.cardiodb.org/acgv/acgv_gene_disease.php?gene=TPM1&icc=HCM)
- [ClinVar RCV000013272 — TPM1 c.523G>A (p.Asp175Asn)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000013272/)
- [ClinVar RCV000013271 — TPM1 c.539A>G (p.Glu180Gly)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000013271/)
- [Chumakova et al., J Clin Med 2025 — thin-filament HCM outcomes](https://pmc.ncbi.nlm.nih.gov/articles/PMC11818361/)
- [Saul et al., ESC Heart Failure 2024 — thin filament HCM natural history](https://onlinelibrary.wiley.com/doi/10.1002/ehf2.14848)
- [Harper et al., Nat Genet 2021 — common variants and HCM expressivity](https://www.nature.com/articles/s41588-020-00764-0)
- [Novel TPM1 mutation, Indian family — PMC10784234](https://pmc.ncbi.nlm.nih.gov/articles/PMC10784234/)
- [TPM1 K30E — pediatric LVNC/DCM, PMC11641563](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11641563/)
- [TPM1 p.E181K restrictive cardiomyopathy / CaMKII-HDAC4 — PMC12818787](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12818787/)
- [2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM Guideline — PMID:38718139](https://pubmed.ncbi.nlm.nih.gov/38718139/)
- [2024 HCM Guideline (Circulation full text)](https://www.ahajournals.org/doi/10.1161/CIR.0000000000001250)
- [ACC — 2024 HCM Guideline Key Points](https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2024/05/06/15/12/2024-hypertrophic-cardiomyopathy-gl)
- [EXPLORER-HCM — NCT03470545](https://clinicaltrials.gov/study/NCT03470545)
- [MAVA-LTE — NCT03723655](https://clinicaltrials.gov/study/NCT03723655)
- [SEQUOIA-HCM aficamten — JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.09.003)
- [Aficamten in mild symptoms, SEQUOIA-HCM — PMC12539928](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12539928/)
- [HCM prevalence in highly trained athletes — PMID:18325444](https://pubmed.ncbi.nlm.nih.gov/18325444/)
- [OMIA:000515-9685 — hypertrophic cardiomyopathy, Felis catus](https://omia.org/OMIA000515/9685/)
- [OMIA:002212-9685 — HCM, MYH7-related, Felis catus](https://omia.org/OMIA002212/9685/)
- [OMIA:002316-9685 — HCM, ALMS1-related, Felis catus](https://omia.org/OMIA002316/9685/)
- [Predicting effects of tropomyosin mutations through myofilament modeling — Front Physiol 2016](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2016.00473/full)