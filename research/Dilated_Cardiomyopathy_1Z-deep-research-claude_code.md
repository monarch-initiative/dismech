---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-02T16:42:54.559549'
end_time: '2026-08-02T16:48:01.616914'
duration_seconds: 307.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 1Z
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
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 22
  total_cost_usd: 1.9237819
  session_id: a621f8ee-004c-5093-b05e-8a97153805e1
  stop_reason: end_turn
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1Z
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1Z** covering all of the
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

# Dilated Cardiomyopathy 1Z (CMD1Z) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Dilated Cardiomyopathy 1Z (CMD1Z) is a rare, autosomal dominant form of familial isolated (non-syndromic) dilated cardiomyopathy caused by heterozygous mutation in **TNNC1**, the gene encoding cardiac (slow skeletal/cardiac-type) troponin C — the calcium-sensing subunit of the sarcomeric troponin complex. Affected individuals develop severe biventricular systolic dysfunction with markedly reduced left ventricular ejection fraction, often with early and aggressive disease progression requiring cardiac transplantation.

**Key identifiers:**
- **OMIM (phenotype):** #611879 — CARDIOMYOPATHY, DILATED, 1Z; CMD1Z ([OMIM.org](https://omim.org/entry/611879))
- **OMIM (gene):** *191040 — TROPONIN C, SLOW; TNNC1 ([OMIM.org](https://www.omim.org/entry/191040))
- **Gene locus:** 3p21.1
- **HGNC:** TNNC1 (HGNC:11940)
- **GTR/UMLS:** C2678475 ([NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2678475/))
- **ICD-10:** I42.0 (Dilated cardiomyopathy — non-gene-specific parent code; no TNNC1-specific ICD-10/11 code exists)
- **MONDO:** No TNNC1-subtype-specific MONDO term was identified in this search; CMD1Z falls under the broader "familial isolated dilated cardiomyopathy" umbrella (Orphanet ORPHA:154). **This should be verified directly against the MONDO ontology before curation** rather than assumed.
- **Orphanet:** TNNC1 is listed as a causal gene for familial isolated DCM (ORPHA:154) ([Orphanet gene page](https://www.orpha.net/en/disease/gene/TNNC1))

**Synonyms/alternative names:** CMD1Z; Cardiomyopathy, dilated, 1Z; TNNC1-related dilated cardiomyopathy; Troponin C-related dilated cardiomyopathy.

**Evidence basis:** All primary reports of CMD1Z derive from **individual patients and multi-generation pedigrees** studied via genetic screening of DCM cohorts (not aggregated registry/database-level statistics) — principally a single large kindred (Family A) originally reported by Mogensen et al. (2004), later supplemented by additional sporadic/small-family TNNC1 variant reports (Chung/Hershberger group, 2011) and functional/biophysical follow-up studies on explanted patient myocardium.

---

## 2. Etiology

**Disease causal factor:** CMD1Z is a **monogenic, sarcomeric-protein disease** — it is caused directly by heterozygous missense mutation of TNNC1, not by environmental, infectious, or purely mechanistic/acquired factors. It belongs to the broader category of sarcomere-gene dilated cardiomyopathies (alongside TNNT2, TPM1, MYH7, ACTC1, TTN, etc.).

**Genetic risk factors (causal variants):**
- The founding, best-characterized mutation is **c.476G>A (p.Gly159Asp / G159D)** in TNNC1, identified by Mogensen et al. in a large family (Family A) with severe DCM and complete penetrance (PMID: [15542288](https://pubmed.ncbi.nlm.nih.gov/15542288/), J Am Coll Cardiol 2004). ClinVar classifies this variant as **Pathogenic** for CMD1Z (ClinVar RCV000013254, based on OMIM assertion; 0-star/no independent criteria review status — flagging a curatorial caveat that this classification has not undergone contemporary ACMG/AMP multi-lab review).
  - The mutation was absent in unaffected family members and in 200 ethnically matched control chromosomes, consistent with segregation and rarity.
  - Located at a conserved residue within a TnC domain that is **constitutively occupied by Ca²⁺** (the structural C-domain, distinct from the regulatory N-domain).
- Four additional **rare TNNC1 variants** — **Y5H, M103I, D145E, I148V** — were functionally characterized by Chung, Hershberger and colleagues (PMID: [21832052](https://pubmed.ncbi.nlm.nih.gov/21832052/), *J Biol Chem* 2011), all previously reported in association with DCM cohorts, expanding the allelic series beyond the single founder G159D mutation.
- TNNC1 also harbors a distinct set of variants (e.g., **A8V, C84Y, E134D, D145E**) associated instead with **hypertrophic cardiomyopathy (CMH13)** — TNNC1 is a genetically pleiotropic locus where different missense substitutions produce opposing (dilated vs. hypertrophic) myofilament calcium-sensitivity phenotypes.
- **Modifier/susceptibility genetic factors:** Not specifically reported for CMD1Z; broader DCM literature implicates common variants and co-occurring "second hits" in genes such as TTN as modifiers of penetrance/severity in sarcomeric DCM generally, but no TNNC1-specific modifier locus has been published.

**Environmental/lifestyle risk factors:** None specifically documented for CMD1Z. As with other monogenic sarcomeric DCMs, generic DCM-exacerbating factors (alcohol, pregnancy/peripartum stress, tachyarrhythmia, viral myocarditis "second hits") could plausibly influence expressivity but have not been reported for TNNC1 carriers specifically.

**Protective factors:** None reported in the literature for TNNC1-associated DCM specifically.

**Gene-environment interactions:** Not established for CMD1Z; no CTD or GxE database entries specific to TNNC1-DCM were identified in this search.

---

## 3. Phenotypes

**Clinical signs/symptoms (cardiac):**
| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Dilated cardiomyopathy | HP:0001644 | Core defining feature |
| Reduced left ventricular ejection fraction | HP:0025168 | "Severely reduced" per OMIM clinical synopsis |
| Congestive heart failure | HP:0001635 | Presenting feature in most reported cases |
| Biventricular dysfunction | (map via HP:0001644 + right ventricular dysfunction term) | Explicitly noted — both ventricles affected, not left-only |
| Cardiomegaly | HP:0001640 | Expected secondary structural finding |
| Ventricular arrhythmia | HP:0004308 | Reported in some family members |
| Sudden cardiac death | HP:0001645 | Documented in affected relatives (severe/lethal course) |

**Phenotype characteristics:**
- **Age of onset:** Highly variable — **from infancy/early childhood to as late as the fifth decade** within the same kindred (per OMIM clinical synopsis for #611879). A 3-year-old boy (nephew of the original proband) required cardiac transplantation, illustrating a severe pediatric-onset presentation within the family.
- **Severity:** Described as "**severe reduction in cardiac function**" — among the more aggressive genetic DCM subtypes reported.
- **Progression:** Progressive, with disease course reported by Mogensen et al. as showing **complete penetrance** and high risk of premature death; the original paper's broader thesis (covering TNNC1 and TNNT2 mutation carriers together) was that troponin-gene DCM carries an adverse prognosis warranting early identification: *"disease expression associated with TNNC1 and TNNT2 mutations was severe with complete penetrance"* (PMID: 15542288).
- **Outcome burden:** Most affected individuals in the literature required **cardiac transplantation** for survival.
- **Frequency among affected individuals:** All reported carriers of the G159D mutation manifested disease (complete penetrance in the index family), though this is based on a single (small) kindred and should not be over-generalized as a population-level penetrance estimate.

**Quality of life impact:** Not separately quantified in TNNC1-specific literature; by extension from general severe pediatric/adult DCM with transplant dependence, substantial impact on functional status, growth (if pediatric-onset), and long-term quality of life would be expected, but no EQ-5D/SF-36 data specific to CMD1Z were located.

---

## 4. Genetic/Molecular Information

**Causal gene:** **TNNC1** (HGNC:11940; OMIM *191040), encoding cardiac/slow-skeletal troponin C (cTnC), UniProt P63316.

**Pathogenic variants:**
| Variant | Type | Classification | Notes |
|---|---|---|---|
| c.476G>A, p.Gly159Asp (G159D) | Missense | Pathogenic (ClinVar RCV000013254, OMIM-sourced, 0★) | Founder/index CMD1Z mutation; C-terminal domain, constitutively Ca²⁺-occupied site |
| p.Tyr5His (Y5H) | Missense | Reported DCM-associated | Functionally characterized (Chung 2011) |
| p.Met103Ile (M103I) | Missense | Reported DCM-associated | Decreased Ca²⁺ sensitivity of force development in vitro |
| p.Asp145Glu (D145E) | Missense | Reported DCM-associated (also reported in HCM context in other cohorts) | Altered α-helical content on CD spectroscopy |
| p.Ile148Val (I148V) | Missense | Reported DCM-associated | Altered α-helical content on CD spectroscopy |
| p.Ala8Val (A8V) | Missense | Predominantly HCM/restrictive phenotype (CMH13), not CMD1Z | Included for contrast — illustrates TNNC1 phenotypic pleiotropy |

- **Zygosity:** Heterozygous, autosomal dominant for the DCM phenotype (a compound-heterozygous TNNC1 presentation has also been separately reported in the DCM literature — "Familial Dilated Cardiomyopathy Associated With a Novel Combination of Compound Heterozygous TNNC1 Variants," *Frontiers in Physiology* 2019 — indicating rare biallelic/compound presentations exist alongside the classic dominant CMD1Z pattern).
- **Functional consequence — mechanistically complex, not simple loss-of-function:**
  - G159D: impairs interaction of mutant cTnC with wild-type troponin T (**decreased** TnC–TnT binding) while **enhancing** interaction with troponin I — an altered, not simply reduced, regulatory interaction.
  - In skinned muscle fibers/explanted human myocardium, G159D produced a **~50% decrease in the rate of activation** without significantly altering steady-state Ca²⁺ sensitivity or cooperativity of force generation (PMID: [17021793](https://pubmed.ncbi.nlm.nih.gov/17021793/), Preston et al., *Pflügers Arch* 2007).
  - In intact skinned ventricular myocytes from an explanted G159D heart, Ca²⁺ sensitivity was **higher** than donor myocytes, and dephosphorylation-induced Ca²⁺-sensitivity changes normally seen with wild-type troponin were **blunted** in mutant troponin — leading to the proposed mechanism of **"uncoupling of the relationship between troponin phosphorylation and myofilament Ca²⁺ sensitivity"** as a driver of the DCM phenotype (PMID: [19808376](https://www.ahajournals.org/doi/10.1161/CIRCHEARTFAILURE.108.818237), Dyer et al., *Circ Heart Fail* 2009; PMID: [17577574](https://pubmed.ncbi.nlm.nih.gov/17577574/), Biochem Biophys Res Commun 2007).
  - Other TNNC1-DCM variants (Y5H, M103I) instead show **decreased** myofilament Ca²⁺ sensitivity of force development, and all four (Y5H, M103I, D145E, I148V) show **reduced α-helical content** by circular dichroism, indicating variant-specific structural destabilization (PMID: 21832052).
  - This heterogeneity — some variants desensitizing, some sensitizing myofilament Ca²⁺ response — parallels the broader troponin-cardiomyopathy literature in which DCM- and HCM-causing troponin/tropomyosin mutations have **opposing effects on thin-filament Ca²⁺ affinity** (Circulation Research, PMC3627712).
- **Allele frequency:** Not found in 200 control chromosomes in the original description; specific gnomAD population allele frequency for G159D was not retrieved in this search and should be queried directly against gnomAD before curation (expected to be absent/extremely rare given pathogenicity and complete penetrance in the founder family).
- **Somatic vs. germline:** Germline (inherited, autosomal dominant).
- **Epigenetics/chromosomal abnormalities:** None reported — CMD1Z is a point-mutation (missense) disorder, not a copy-number or epigenetic disease.

---

## 5. Environmental Information

No specific environmental toxin, occupational exposure, or infectious trigger has been reported as causal or modifying for TNNC1/CMD1Z in the literature surveyed. No lifestyle-factor (diet, exercise, alcohol) association specific to TNNC1 carriers was identified. This section is **not applicable / not established** for CMD1Z beyond the generic considerations that apply to any DCM patient (e.g., avoidance of additional cardiotoxic stressors is standard clinical advice but is not disease-mechanism-specific).

---

## 6. Mechanism / Pathophysiology

**Causal chain (from molecular lesion to clinical phenotype):**

1. **Trigger (molecular):** Missense mutation in TNNC1 (e.g., G159D) alters the structure/protein-protein interaction surface of cardiac troponin C within the troponin complex on the thin filament.
2. **Molecular dysfunction:** Altered TnC–TnT and TnC–TnI binding (G159D: ↓TnT binding, ↑TnI binding); altered α-helical content/structural stability for other variants (Y5H, M103I, D145E, I148V); **uncoupling of the normal relationship between troponin I phosphorylation (via PKA, a beta-adrenergic effector) and myofilament Ca²⁺ sensitivity**.
3. **Cellular/sarcomeric consequence:** Abnormal Ca²⁺-dependent regulation of actin-myosin cross-bridge cycling — some variants increase resting/diastolic Ca²⁺ sensitivity (impairing relaxation and blunting the normal beta-adrenergic-driven desensitization needed for exercise/stress response), others decrease systolic force-generating Ca²⁺ sensitivity (directly impairing contractile force). Both routes converge on **impaired, dysregulated myofilament contractile performance** rather than a uniform "loss of function."
4. **Tissue/organ consequence:** Impaired sarcomere contractile efficiency across the myocardium → compensatory ventricular remodeling and progressive chamber dilation, biventricular systolic dysfunction, and reduced ejection fraction.
5. **Clinical/organism-level consequence:** Congestive heart failure, ventricular arrhythmia, and in severe cases sudden cardiac death or need for transplantation.

**Molecular pathway / protein context:** Cardiac troponin C is the **Ca²⁺-sensing subunit of the troponin complex** (TnC–TnI–TnT) on the thin filament, which in turn interacts with tropomyosin to gate myosin–actin interaction in a Ca²⁺-dependent manner (excitation–contraction coupling). This is the canonical **cardiac muscle contraction** pathway (GO: regulation of cardiac muscle contraction).

**Cellular process:** Sarcomeric/myofilament Ca²⁺-regulated contraction (not apoptosis- or inflammation-driven at the primary-lesion level, distinguishing this mechanistically from e.g. BAG3-related DCM, which involves proteostasis/Z-disc/apoptosis pathways).

**Protein dysfunction category:** Altered protein–protein interaction and reduced structural stability (not simple loss-of-function or aggregation); a **dominant-negative/altered-function** mechanism is implicated by the enhanced-TnI-binding/decreased-TnT-binding pattern and blunted phosphorylation response, consistent with autosomal dominant inheritance with a single mutant allele exerting effects within the assembled troponin complex.

**Suggested GO terms (biological process/molecular function/cellular component):**
- GO:0006936 muscle contraction
- GO:0055117 regulation of cardiac muscle contraction
- GO:0005509 calcium ion binding
- GO:0031014 troponin C binding (or GO:0030172 troponin binding, verify exact term)
- GO:0005861 troponin complex (cellular component)
- GO:0030017 sarcomere (cellular component)

**Suggested CL term:** CL:0000746 cardiac muscle cell (myocyte).

**Suggested UBERON terms:** UBERON:0000948 heart; UBERON:0002084 heart left ventricle; UBERON:0002078 heart right ventricle; UBERON:0002349 myocardium.

**Suggested CHEBI term:** CHEBI:29108 calcium(2+).

*(All ontology term suggestions above should be independently verified via OAK/`runoak info` before insertion into KB YAML per dismech's anti-hallucination policy — several are plausible-but-unverified in this research pass.)*

**Molecular profiling / advanced technologies:** No transcriptomic, proteomic, metabolomic, single-cell, or spatial-transcriptomic datasets specific to TNNC1-CMD1Z human myocardium were identified in this search. Biophysical/functional characterization (skinned-fiber mechanics, circular dichroism, mass spectrometry of expressed mutant protein) constitutes the primary "omics-adjacent" evidence base, performed in explanted patient myocardium and reconstituted/recombinant protein systems (in vitro, IN_VITRO evidence class) plus knock-in mouse models (MODEL_ORGANISM evidence class, see Section 15).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Heart (biventricular — both left and right ventricles affected, an important distinguishing clinical feature noted in the OMIM clinical synopsis).
- **Secondary/systemic involvement:** Congestive heart failure sequelae (pulmonary congestion, hepatic congestion) as downstream complications of pump failure; no primary extracardiac organ involvement is described (TNNC1's cardiac isoform is the relevant one for this phenotype — TNNC1 is also expressed in slow skeletal muscle, but no associated skeletal myopathy phenotype is reported for CMD1Z).
- **Body system:** Cardiovascular system (isolated, non-syndromic).
- **Tissue level:** Cardiac (striated) muscle tissue — specifically the sarcomere/myofibril of cardiomyocytes.
- **Cell level:** Cardiomyocytes (ventricular myocytes of both chambers).
- **Subcellular level:** Sarcomere thin filament / troponin complex (GO Cellular Component: troponin complex, thin filament).
- **Laterality:** Bilateral/biventricular — not unilateral.

---

## 8. Temporal Development

- **Onset:** Highly variable within the same family — ranges from **infancy/early childhood** to **the fifth decade of life**. No single modal onset age is established; this wide intrafamilial variability is itself a notable feature of the OMIM clinical synopsis.
- **Onset pattern:** Can present acutely with heart failure or be identified via family cascade screening in an initially asymptomatic carrier; disease course once manifest is progressive.
- **Progression:** Progressive systolic dysfunction; described as "severe" with complete penetrance in the index family, culminating in transplant-level heart failure in multiple reported individuals.
- **Disease course pattern:** Chronic, progressive (not episodic/relapsing-remitting) — consistent with structural/sarcomeric DCM generally, in contrast to arrhythmia-first channelopathies.
- **Duration:** Chronic, lifelong once manifest; not self-limited.
- **Remission:** No spontaneous remission reported; standard heart-failure therapy can produce partial functional improvement (as in any GDMT-responsive DCM) but no TNNC1-specific reverse-remodeling data were found.
- **Critical periods:** Early genetic diagnosis via family cascade screening is emphasized in the founding literature as clinically important given the "adverse prognosis and high risk of premature death" associated with troponin-gene DCM (PMID: 15542288) — i.e., the actionable window is pre-symptomatic identification of at-risk relatives.

---

## 9. Inheritance and Population

**Epidemiology:**
- **TNNC1-specific prevalence/incidence:** Not separately quantified in disease registries; CMD1Z is an ultra-rare DCM subtype. TNNC1 mutations account for only a small fraction of genotyped familial DCM cases (troponin-complex genes collectively represent a minority of the ~30–40 known DCM genes, with TNNC1 being one of the rarer contributors, based on original identification in a single large kindred plus scattered subsequent case reports).
- **General DCM epidemiology (context):** Overall DCM prevalence estimates range from ~1:250 (broader/CMR-based estimates) to 1:2,500 in older estimates, with incidence of ~5–7 cases per 100,000 person-years; ~30–50% of cases are familial, and a genetic cause is identifiable in ~35–40% of cases overall (Nature Reviews Cardiology, PMC4288017, PMC12393173).

**Inheritance pattern:** **Autosomal dominant**, based on heterozygous mutation transmission and multi-generational pedigree segregation in the founding CMD1Z family (a rare compound-heterozygous presentation has also been separately reported, suggesting biallelic modes can occur atypically).

**Penetrance:** **Complete** penetrance reported in the index G159D family — all mutation carriers manifested disease — though this is based on one kindred and should not be treated as a population-wide certainty.

**Expressivity:** **Highly variable** — age of onset spans from infancy to the fifth decade within the same family, and severity ranges from milder disease to transplant-requiring heart failure in early childhood, indicating substantial variable expressivity even among carriers of the identical G159D variant.

**Genetic anticipation:** Not reported/not applicable (TNNC1-DCM is not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for TNNC1.

**Founder effects:** The G159D mutation was identified in a single large kindred (Family A); whether it represents a true founder mutation recurring in additional unrelated families, or is private to this pedigree, was not established in the sources reviewed.

**Consanguinity:** Not implicated — autosomal dominant inheritance from a single mutant allele does not require consanguinity (contrast with the unrelated TNNC1-A8V homozygous restrictive-cardiomyopathy phenotype in infants, which does involve homozygosity, but that maps to a different, non-CMD1Z phenotype).

**Carrier frequency:** Not established; expected to be extremely low given the rarity/private nature of reported variants.

**Population demographics:** No specific ethnic, geographic, or sex-ratio data specific to CMD1Z/TNNC1 carriers were identified (contrast with general DCM, which shows a male predominance of roughly 2:1 in some population-based imaging studies).

---

## 10. Diagnostics

**Clinical/functional tests:**
- **Echocardiography / cardiac MRI:** Standard imaging to document left (and right) ventricular dilation and reduced ejection fraction — the core diagnostic modality for the DCM phenotype itself.
- **ECG:** May show nonspecific abnormalities and, per the mouse-model literature (Section 15), prolonged QRS/QT can accompany TnC-mutation cardiomyopathy, relevant to arrhythmia risk stratification.
- **Endomyocardial biopsy / explanted myocardium:** Used in the primary research literature (not routine clinical diagnosis) to perform functional/biophysical characterization of mutant troponin (skinned-fiber mechanics, myocyte Ca²⁺-sensitivity assays).

**Genetic testing:**
- **Recommended approach:** Given TNNC1's status as one of dozens of established DCM genes, **multigene DCM panel testing** (including TNNC1 alongside TTN, LMNA, MYH7, TNNT2, TPM1, SCN5A, RBM20, BAG3, DES, PLN, FLNC, etc.) is the standard first-tier genetic test, per current DCM genetic-testing practice, rather than single-gene TNNC1 sequencing as a first step (unless a familial variant is already known, in which case targeted single-gene/site testing is appropriate for cascade screening).
- **Whole exome/genome sequencing:** Useful when panel testing is uninformative or phenotype is atypical/syndromic.
- **Cascade family screening:** Emphasized in the founding literature as clinically important — once a pathogenic TNNC1 variant is identified in a proband, targeted testing of at-risk relatives is indicated given complete penetrance and "high risk of premature death" in the index family.
- **Chromosomal microarray/karyotype/FISH:** Not indicated — CMD1Z is a single-gene missense disorder, not a chromosomal disorder.
- **Mitochondrial DNA testing:** Not applicable.

**Clinical criteria:** Standard DCM diagnostic criteria (echocardiographic LV dilation + systolic dysfunction not explained by ischemic, valvular, or hypertensive disease) apply; TNNC1/CMD1Z is distinguished from other DCM etiologies purely by molecular genetic testing, not by distinctive clinical/imaging features.

**Differential diagnosis:** Other genetic DCM subtypes (TTN-truncating variants — the single most common identifiable cause of genetic DCM; LMNA-associated DCM with conduction disease; other troponin/sarcomeric-gene DCM such as TNNT2; BAG3-associated DCM); acquired DCM causes (ischemic, viral/myocarditis, alcohol-related, peripartum, tachycardia-induced) must be excluded clinically before/alongside genetic workup.

**Screening:** No population-based newborn screening program exists for TNNC1/CMD1Z (as with virtually all monogenic cardiomyopathies); the relevant screening paradigm is **genetic cascade screening of first-degree relatives** of a known proband.

---

## 11. Outcome/Prognosis

- **Prognosis:** Described in the founding literature as **"severe... with complete penetrance,"** with mutation analysis proposed as valuable for **"early identification of individuals with an adverse prognosis and a high risk of premature death"** (PMID: 15542288) — i.e., TNNC1 (and TNNT2) mutation-associated DCM was specifically flagged as carrying a *worse* prognosis than DCM overall.
- **Transplantation burden:** Multiple reported individuals, including a child as young as 3 years old, required cardiac transplantation, indicating that end-stage heart failure requiring transplant is a realistic outcome trajectory for this subtype, not a rare tail event.
- **Mortality:** No TNNC1-specific quantitative survival statistics (e.g., 5-/10-year survival rates) were located in this search; general severe pediatric/familial DCM carries substantial mortality/transplant risk without intervention, consistent with the qualitative "adverse prognosis" language used for this gene.
- **Complications:** Congestive heart failure, ventricular arrhythmia, sudden cardiac death (documented in family members), and transplant-related complications for those who progress to transplantation.
- **Prognostic factors:** Genotype itself (TNNC1/TNNT2 mutation carrier status) was proposed by Mogensen et al. as a prognostic marker justifying early genetic identification — i.e., this is one of the earliest examples in the DCM literature of genotype-based risk stratification informing clinical management recommendations.

---

## 12. Treatment

No TNNC1/CMD1Z-specific, genotype-targeted therapy exists. Management follows **standard guideline-directed medical therapy (GDMT) for heart failure with reduced ejection fraction**, applied to this genetic DCM subtype as to DCM generally:

**Pharmacotherapy (NCIT:C15986 Pharmacotherapy):**
- ACE inhibitors / ARBs / angiotensin receptor–neprilysin inhibitors (ARNI)
- Beta-blockers
- Mineralocorticoid receptor antagonists (MRAs)
- SGLT2 inhibitors (contemporary "quadruple therapy" per 2022 ACC/AHA/HFSA and ESC guidelines)

**Device therapy:**
- **Implantable cardioverter-defibrillator (ICD):** Class I recommendation for non-ischemic DCM with NYHA class II–III symptoms and LVEF ≤35% on optimal medical therapy (relevant given the documented ventricular arrhythmia/sudden death risk in CMD1Z families) — though the evidence base for ICD mortality benefit specifically in non-ischemic cardiomyopathy is debated (the DANISH trial did not show an overall mortality benefit).
- **Cardiac resynchronization therapy (CRT):** Indicated for persistent systolic dysfunction with significant intraventricular conduction delay.

**Surgical/advanced:**
- **Heart transplantation (NCIT:C15289 Organ Transplantation):** The definitive intervention for refractory disease — explicitly documented as required in multiple reported CMD1Z family members, including pediatric cases.
- **Mechanical circulatory support** (e.g., LVAD) as a bridge to transplant or destination therapy in critically ill patients who cannot be stabilized medically.

**Genetic counseling (NCIT:C15240 Genetic Counseling):** Recommended given autosomal dominant inheritance, complete penetrance in the index family, and the prognostic significance of genotype — supports cascade testing of at-risk relatives.

**Experimental/targeted therapy:** No TNNC1-targeted small-molecule, gene-therapy, or myofilament-modulating agent specific to this variant class was identified in this search (in contrast to some other genetic cardiomyopathies where myosin modulators are in active development). This remains an open area — no ClinicalTrials.gov entries specific to TNNC1-DCM were surfaced.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (a genetic, inherited structural mutation cannot be prevented); the closest analog is **reproductive genetic counseling / preimplantation genetic diagnosis** for known carrier families wishing to avoid transmission.
- **Secondary prevention:** **Cascade genetic screening** of at-risk first-degree relatives of a proband, enabling pre-symptomatic identification and early initiation of surveillance (serial echocardiography) and, if dysfunction emerges, early GDMT — directly supported by the founding literature's emphasis on early identification given adverse prognosis.
- **Tertiary prevention:** Standard heart-failure GDMT and device therapy (as above) to reduce progression to end-stage disease, arrhythmic death, and transplant need in those already diagnosed.
- **Immunization/public health/prophylaxis:** Not applicable — this is not an infectious or environmentally preventable disease.

---

## 14. Other Species / Natural Disease

No naturally occurring TNNC1-associated dilated cardiomyopathy in companion animals or wildlife was identified in this search (no OMIA entry surfaced). TNNC1 orthologs are highly conserved across vertebrates (troponin C is a core, evolutionarily ancient sarcomeric protein), making cross-species mechanistic conservation plausible, but no veterinary natural-disease case reports specific to this gene were found in the sources reviewed. This section should be treated as **not established / no data found** for CMD1Z specifically, pending a dedicated OMIA/veterinary-literature search.

---

## 15. Model Organisms

- **Mouse knock-in model (a related Ca²⁺-desensitizing TNNC1 mutation, D73N):** Heterozygous **D73N (+/–)** knock-in mice — D73N lies in the regulatory N-domain's second Ca²⁺-binding loop of cardiac troponin C — develop **early-onset dilated cardiomyopathy**: mice began dying at **6 weeks of age**, with **median survival of 12 weeks**; echocardiography showed ejection fraction reduced to **~28%** (vs. ~69% wild-type) and fractional shortening to **~13%** (vs. ~38% wild-type), with LV dilation, wall thinning, increased heart-weight/body-weight ratio, prolonged QRS/QT intervals, ~2.4-fold increase in β-myosin heavy chain (a molecular heart-failure marker), and **loss of ventricular myocyte responsiveness to β-adrenergic stimulation** (PMID: [26379556](https://pmc.ncbi.nlm.nih.gov/articles/PMC4550777/), *Frontiers in Physiology* 2015). Mechanistically, D73N increases the rate of Ca²⁺ dissociation from the regulatory domain, reducing myofilament Ca²⁺ sensitivity and impairing systolic function — directly recapitulating the human sarcomeric-DCM paradigm of impaired Ca²⁺-myofilament coupling, and providing an in vivo model for the general class of Ca²⁺-desensitizing TNNC1 mutations to which CMD1Z belongs (note: this is a distinct residue from the CMD1Z-defining G159D variant — no G159D-specific knock-in mouse model was identified in this search).
- **Reconstituted/recombinant protein systems (in vitro):** Recombinant mutant human cTnC (G159D, Y5H, M103I, D145E, I148V) reconstituted into TnC-depleted **porcine cardiac/papillary skinned muscle fibers** is the principal functional model system used to characterize Ca²⁺-sensitivity and force-generation effects of individual CMD1Z-associated variants (PMID: 21832052; PMID: 17021793).
- **Ex vivo human tissue:** Explanted failing human myocardium from a G159D-mutation carrier undergoing transplantation was directly studied (skinned myocyte force–Ca²⁺ relationships, troponin phosphorylation assays), providing a direct human-tissue functional correlate rather than relying solely on heterologous/animal systems (PMID: 19808376).
- **Model limitations:** The D73N mouse model, while mechanistically informative for the Ca²⁺-desensitization paradigm, is **not genotype-matched** to the G159D CMD1Z-defining mutation — a curatorial `HUMAN_MODEL_MISMATCH`-type caveat is warranted if this model is cited as direct support for CMD1Z pathophysiology specifically, since G159D's own functional profile (increased, not decreased, Ca²⁺ sensitivity in human myocytes; altered phosphorylation-coupling rather than straightforward desensitization) differs mechanistically from D73N.

---

## Summary Table — Key Curation-Ready Facts

| Field | Value | Primary source |
|---|---|---|
| Disease | Dilated Cardiomyopathy 1Z (CMD1Z) | OMIM #611879 |
| Gene | TNNC1 (cardiac troponin C) | OMIM *191040 |
| Locus | 3p21.1 | OMIM |
| Inheritance | Autosomal dominant (complete penetrance in index family) | Mogensen 2004, PMID 15542288 |
| Founder variant | c.476G>A, p.Gly159Asp (G159D) | ClinVar RCV000013254; PMID 15542288 |
| Other DCM-associated TNNC1 variants | Y5H, M103I, D145E, I148V | PMID 21832052 |
| Onset | Infancy–5th decade (variable) | OMIM clinical synopsis |
| Key mechanism | Altered TnC–TnT/TnI binding; uncoupled troponin-phosphorylation/Ca²⁺-sensitivity relationship; variant-dependent Ca²⁺ sensitization or desensitization | PMID 19808376, 17021793, 17577574, 21832052 |
| Severity/prognosis | Severe, adverse prognosis, high risk of premature death, transplant frequently required | PMID 15542288 |
| Treatment | Standard HFrEF GDMT, ICD/CRT, transplantation | General DCM guidelines (ACC/AHA/HFSA 2022; ESC 2023) |
| Mouse model (related variant) | D73N knock-in — 6-wk onset, 12-wk median survival, EF ~28% | PMID 26379556 |

---

### Notes on Evidence Quality / Curation Caveats
- The CMD1Z literature base is thin and centers on **one large founding kindred plus a handful of subsequent variant reports** — treat prevalence/penetrance figures as pedigree-specific, not population-validated.
- The ClinVar classification for G159D carries **0-star review status** (single OMIM-sourced submission, no independent multi-lab ACMG/AMP assertion) — flag as needing contemporary reclassification confirmation before treating as definitively "Pathogenic" in a modern curation context.
- No MONDO ID specific to CMD1Z was confirmed in this pass — verify directly against the MONDO ontology rather than assuming absence.
- OMIM's own full clinical-synopsis text could not be directly fetched (403 response) — the clinical details above were triangulated from search-engine-summarized OMIM content and secondary sources; **direct OMIM API/text confirmation is recommended before final KB entry**.
- The mouse model cited (D73N) is mechanistically related but **not variant-matched** to the CMD1Z-defining G159D mutation — this should be modeled as a `HUMAN_MODEL_MISMATCH`-style caveat if incorporated into a dismech entry, per project convention.

Sources:
- [OMIM #611879 — CARDIOMYOPATHY, DILATED, 1Z; CMD1Z](https://omim.org/entry/611879)
- [OMIM *191040 — TROPONIN C, SLOW; TNNC1](https://www.omim.org/entry/191040)
- [Severe disease expression of cardiac troponin C and T mutations in patients with idiopathic dilated cardiomyopathy — PubMed (PMID 15542288)](https://pubmed.ncbi.nlm.nih.gov/15542288/)
- [Functional characterization of TNNC1 rare variants identified in dilated cardiomyopathy — PubMed (PMID 21832052)](https://pubmed.ncbi.nlm.nih.gov/21832052/)
- [Functional effects of the DCM mutant Gly159Asp troponin C in skinned muscle fibres — PubMed (PMID 17021793)](https://pubmed.ncbi.nlm.nih.gov/17021793/)
- [DCM troponin C mutant Gly159Asp blunts the response to troponin phosphorylation — PubMed (PMID 17577574)](https://pubmed.ncbi.nlm.nih.gov/17577574/)
- [Functional Analysis of a Unique Troponin C Mutation, GLY159ASP... Studied in Explanted Heart Muscle — Circulation: Heart Failure (PMID 19808376)](https://www.ahajournals.org/doi/10.1161/CIRCHEARTFAILURE.108.818237)
- [NM_003280.3(TNNC1):c.476G>A (p.Gly159Asp) AND Dilated cardiomyopathy 1Z — ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000013254.24/)
- [Knock-in mice harboring a Ca2+ desensitizing mutation in cardiac troponin C develop early onset dilated cardiomyopathy — PMC (PMID 26379556)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4550777/)
- [Orphanet: TNNC1 — troponin C1, slow skeletal and cardiac type](https://www.orpha.net/en/disease/gene/TNNC1)
- [Familial Dilated Cardiomyopathy Associated With a Novel Combination of Compound Heterozygous TNNC1 Variants — Frontiers in Physiology](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2019.01612/full)
- [Epidemiology of the inherited cardiomyopathies — Nature Reviews Cardiology](https://www.nature.com/articles/s41569-020-0428-2)
- [GENETIC CAUSES OF DILATED CARDIOMYOPATHY — PMC (PMC4288017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4288017/)
- [Dilated Cardiomyopathy (DCM) Guidelines — 2022 ACC/AHA/HFSA, 2023 ESC — Medscape](https://emedicine.medscape.com/article/152696-guidelines)
- [Current Management and Treatment — Dilated Cardiomyopathy — NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK553842/)
- [NM_003280.3(TNNC1):c.23C>T (p.Ala8Val) AND Hypertrophic cardiomyopathy 13 — ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000013256/)