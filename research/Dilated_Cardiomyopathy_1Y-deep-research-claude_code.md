---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T14:40:15.867493'
end_time: '2026-08-27T14:44:35.421562'
duration_seconds: 259.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 1Y
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 22
  total_cost_usd: 1.1739290000000002
  session_id: 98b3127c-432a-57dc-acc9-774218ba8a79
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 11
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1Y
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1Y** covering all of the
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

I'll research Dilated Cardiomyopathy 1Y using web search and fetch tools to gather authoritative, current information.

I now have sufficient primary-source material to compile the full report.

# Dilated Cardiomyopathy 1Y (CMD1Y / TPM1-Related Dilated Cardiomyopathy): Comprehensive Research Report

## 1. Disease Information

**Overview.** Dilated Cardiomyopathy 1Y (CMD1Y) is a monogenic, autosomal dominant subtype of primary/familial dilated cardiomyopathy (DCM) caused by heterozygous missense mutations in **TPM1** (alpha-tropomyosin, tropomyosin-1), the gene encoding the major sarcomeric thin-filament protein that co-regulates calcium-dependent actin–myosin interaction with the troponin complex. The disease is characterized by left ventricular (and often biventricular) dilation with impaired systolic contractile function, leading to progressive congestive heart failure; some reported patients died in the third to sixth decades of life [OMIM #611878](https://omim.org/entry/611878). Ultrastructurally, electron microscopy of affected myocardium shows abnormal sarcomere structure [OMIM #611878](https://omim.org/entry/611878).

**Key identifiers:**
- **OMIM (phenotype):** #611878 — CARDIOMYOPATHY, DILATED, 1Y; CMD1Y
- **OMIM (gene):** *191010 — TROPOMYOSIN 1; TPM1
- **HGNC:** 12010 (TPM1) — [thegencc.org/genes/HGNC:12010](https://thegencc.org/genes/HGNC:12010)
- **UniProt:** P09493 (tropomyosin alpha-1 chain)
- **Locus:** 15q22.1–q22.2
- **MedGen:** C2678476 — [MedGen C2678476](https://www.ncbi.nlm.nih.gov/medgen/C2678476) / [NIH GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2678476/)
- **Orphanet (broader entity):** ORPHA:154 — Familial isolated dilated cardiomyopathy
- **Related MONDO/parent concept:** primary/idiopathic dilated cardiomyopathy, MONDO:0005021
- **Allelic disorders at the same TPM1 locus:** Familial Hypertrophic Cardiomyopathy 3 (HCM3), Left Ventricular Noncompaction 9 (LVNC9), and CMD1E (an earlier-numbered TPM1-linked DCM designation, illustrating that TPM1 maps to more than one historical CMD1x sub-label)

**Synonyms/alternative names:** Cardiomyopathy, dilated, 1Y; CMD1Y; TPM1-related dilated cardiomyopathy; alpha-tropomyosin cardiomyopathy; DCM type 1Y (DCM1Y).

**Evidence basis:** This entry is derived almost entirely from **aggregated case-level and small-pedigree reports** (individual families and probands identified through linkage analysis, targeted Sanger sequencing, or next-generation sequencing panels) rather than large disease registries — reflecting the rarity of TPM1-DCM as a cause of DCM overall. Functional/mechanistic characterization comes from in vitro biochemical, biophysical, and iPSC-cardiomyocyte/computational studies of specific variants.

---

## 2. Etiology

**Disease-causal factor.** CMD1Y is caused by **heterozygous missense mutations in TPM1** on chromosome 15q22.1, inherited in an **autosomal dominant** pattern [OMIM #611878](https://omim.org/entry/611878). Approximately 30 distinct TPM1 variants have been reported in association with DCM1Y to date (per aggregated literature review) [PMC8758022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8758022/).

**Genetic risk factors:**
- Causal missense variants cluster across the coiled-coil tropomyosin rod domain and disrupt either (a) surface charge distribution affecting actin binding, or (b) allosteric communication with the troponin complex.
- Documented pathogenic/likely pathogenic DCM-causing TPM1 variants include:
  - **E40K** and **E54K** — the founding CMD1Y mutations, identified by Olson et al. via linkage analysis of two DCM pedigrees; described as altering the surface charge of alpha-tropomyosin (PMID: [11273725](https://pubmed.ncbi.nlm.nih.gov/11273725/), *J Mol Cell Cardiol*, 2001).
  - **D230N (Asp230Asn)** — identified in two Caucasian probands and segregating with disease in 14 affected relatives; structural basis characterized by X-ray/biophysical study (PMID: [28600229](https://pubmed.ncbi.nlm.nih.gov/28600229/)); ClinVar RCV000036354.
  - **M8R (Met8Arg)** — DCM/LVNC-associated variant with in silico and in vitro modeling of hypocontractility mechanism (PMC11392859); ClinVar RCV000036318.
  - **K30E (Lys30Glu)** — de novo variant causing severe pediatric DCM with LV noncompaction; destabilizes the N-terminal tropomyosin domain (PMID: [39684770](https://pmc.ncbi.nlm.nih.gov/articles/PMC11641563/), 2024).
  - **E114Q** — novel missense variant (c.340G>C) identified in a Chinese Han family, segregating with maternal death from DCM at age 50 (PMID: [35029218](https://pmc.ncbi.nlm.nih.gov/articles/PMC8758022/), 2022).
  - **T237S** — reported as likely pathogenic in a DCM proband.
  - **E62Q** is the classic **HCM**-causing (not DCM) TPM1 variant, useful as a mechanistic contrast (see Section 6).
- **Allele frequency:** DCM-causing TPM1 variants are absent or present at extremely low frequency in population reference databases (gnomAD), consistent with pathogenicity and highly penetrant dominant disease; TPM1 as a whole gene shows constraint against missense variation in its functional (coiled-coil) domains.
- **Modifier genes:** No validated CMD1Y-specific modifier genes are established; general DCM modifier/second-hit loci (e.g., titin truncating variants) may exacerbate phenotype in digenic contexts, as recognized broadly in the DCM genetics literature (PMC4288017, "Genetic Causes of Dilated Cardiomyopathy").

**Environmental/other risk factors:** No disease-specific environmental triggers are established for CMD1Y; as with other genetic DCM, generic stressors that unmask or accelerate cardiomyopathy (pregnancy, alcohol, cardiotoxic chemotherapy, viral myocarditis, tachyarrhythmia) may in principle act as second hits, but this has not been specifically documented for TPM1 carriers in the literature reviewed.

**Protective factors:** None specifically documented for TPM1/CMD1Y.

**Gene–environment interactions:** Not specifically characterized for this subtype in the literature surveyed.

---

## 3. Phenotypes

Because DCM1Y is a form of DCM, its phenotype overlaps substantially with nonsyndromic/idiopathic DCM, with variable severity and age of onset reported across pedigrees — from neonatal-onset lethal disease (K30E case, onset at 2 weeks of life) to adult-onset disease with death in the third–sixth decades [OMIM #611878](https://omim.org/entry/611878).

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Dilated cardiomyopathy | HP:0001644 | Core defining feature; LV (and often RV) chamber enlargement with reduced ejection fraction |
| Left ventricular dilation | HP:0002944 (or related LV dilation term) | Documented on echocardiography (e.g., LVEDD 33.6 mm/m² in E114Q case) |
| Reduced left ventricular ejection fraction | HP:0012664 (Decreased left ventricular ejection fraction) | EF 43.1% (E114Q, adult-onset), EF 20% (K30E, pediatric/severe) |
| Congestive heart failure | HP:0001635 | Progressive; presenting symptom in most reported cases (dyspnea, chest tightness, abdominal distension/edema) |
| Cardiomegaly | HP:0001712 | On physical exam/imaging |
| Sinus tachycardia | HP:0011703 | e.g., HR 113 bpm in the E114Q proband |
| Left ventricular noncompaction | HP:0030702 (or "Left ventricular noncompaction cardiomyopathy") | Overlaps with the allelic LVNC9 phenotype; co-occurs with DCM in some TPM1 mutation carriers (K30E, M8R) |
| Cyanosis (infantile presentation) | HP:0000961 | Reported in the neonatal-onset K30E case |
| Hypotonia (infantile) | HP:0001252 | Reported in the neonatal-onset K30E case |
| Sudden cardiac death | HP:0001645 | Risk in undiagnosed/advanced disease, as in general DCM |
| Abnormal sarcomere morphology | (no precise HPO term; describe via ultrastructural finding) | Seen on electron microscopy of myocardium [OMIM #611878](https://omim.org/entry/611878) |

**Onset/severity/progression:** Highly variable — reported onset spans neonatal to adult; disease course is generally progressive, with several reported deaths from heart failure ranging from early childhood (age 3 years 8 months, K30E) to middle adulthood (ages 27–50 across different variant carriers). Severity correlates loosely with the degree of hypocontractility produced by the specific variant (see Section 6).

**Frequency among affected individuals:** Given the small numbers of reported families (case reports/small pedigrees), formal phenotype-frequency statistics (percentage penetrance for each sub-phenotype) are not established; qualitative HPO frequency terms (e.g., "typical" for cardiac dilation, "occasional" for LV noncompaction overlap) would be more appropriate than numeric percentages.

**Quality of life impact:** Not separately quantified for CMD1Y specifically; as with general heart-failure populations, expect substantial QoL burden proportional to NYHA functional class, captured generically via tools like the Kansas City Cardiomyopathy Questionnaire (KCCQ) in broader DCM literature — no disease-specific QoL study identified for this subtype.

---

## 4. Genetic/Molecular Information

**Causal gene:** TPM1 (Tropomyosin 1, alpha), OMIM *191010, HGNC:12010, UniProt P09493, located at 15q22.1–q22.2, encoding the major cardiac/striated-muscle tropomyosin isoform (a ~284-amino-acid, highly alpha-helical coiled-coil protein that polymerizes head-to-tail along the actin thin filament).

**Variant classification and type:** All reported CMD1Y-causing variants to date are **heterozygous missense** mutations (no frameshift/nonsense/splice-site DCM1Y variants identified in the literature reviewed), consistent with a dominant-negative or altered-function mechanism rather than simple haploinsufficiency. Representative variants and their ClinVar classifications:
- p.Asp230Asn (c.688G>A) — classified pathogenic for "Primary dilated cardiomyopathy" (ClinVar RCV000036354)
- p.Met8Arg (c.23T>G) — ClinVar RCV000036318
- p.Glu40Lys, p.Glu54Lys — originally described by Olson et al. 2001 (PMID: 11273725)
- p.Lys30Glu (c.88A>G) — de novo, functionally characterized 2024 (PMID: 39684770)
- p.Glu114Gln (c.340G>C) — novel, 2022 Chinese pedigree (PMID: 35029218)

**Population frequency:** DCM-causing TPM1 missense variants are essentially absent from gnomAD/population databases, consistent with rarity and pathogenicity; TPM1 as a gene shows regional missense constraint concentrated in actin-binding and troponin-interacting surfaces of the coiled-coil.

**Somatic vs. germline:** All reported CMD1Y variants are germline; most are familial (autosomal dominant transmission with variable expressivity), though de novo occurrence has been documented (K30E case, PMID: 39684770).

**Functional consequences — mechanism divides HCM vs. DCM at the same locus.** A key mechanistic insight, established by direct comparison of an HCM-causing (E62Q) and a DCM-causing (E54K) TPM1 variant using iPSC-derived cardiomyocytes and computational modeling (PMID: [39436707](https://pmc.ncbi.nlm.nih.gov/articles/PMC11645150/), *J Clin Invest*, 2024):
- **DCM variant E54K:** decreases calcium sensitivity and produces **hypocontractility** — via long-range allosteric effects that increase the association rate of the C-terminal troponin I mobile domain, yielding shorter-lived twitches, impaired length-dependent activation, and ~3-fold decreased peak force. Net effect: increased tissue compliance, chamber dilation without hypertrophy.
- **HCM variant E62Q** (contrast case): increases calcium sensitivity, reduces tropomyosin molecular stiffness, favors the "closed" (activating) regulatory state, and produces **hypercontractility** (>3-fold increased peak force), driving hypertrophy.
- This supports a unifying framework in which intrinsically *decreased* actomyosin contractility from TPM1 variants produces cardiomyocyte lengthening/dilation (DCM), while intrinsically *increased* contractility produces hypertrophy (HCM) — despite both classes of mutation affecting the same protein.

For the K30E variant specifically: differential scanning calorimetry showed decreased thermal/calorimetric stability of tropomyosin domains 2–3 and reduced thermal stability of the tropomyosin–actin complex; in vitro motility assays showed ~37% reduction in thin-filament sliding velocity across physiological calcium concentrations, with increased calcium sensitivity (pCa50 5.97 vs 5.83 WT) but impaired maximal force — indicating a complex, domain-destabilizing hypocontractile mechanism (PMID: 39684770).

For D230N: structural studies indicate the mutation perturbs local coiled-coil geometry, altering tropomyosin's positional regulation on the thin filament (PMID: 28600229).

**Modifier genes / epigenetics / chromosomal abnormalities:** None specifically reported for CMD1Y; not applicable as this is a single-gene missense disorder without described epigenetic modulation or chromosomal rearrangement mechanism in the literature surveyed.

**Gene Ontology / pathway suggestions:**
- GO:0003779 — actin binding
- GO:0005523 — tropomyosin binding
- GO:0060048 — cardiac muscle contraction
- GO:0086003 — cardiac muscle cell contraction
- GO:0055010 — ventricular cardiac muscle tissue morphogenesis
- GO Cellular Component: GO:0030017 — sarcomere; GO:0036379 — myofilament; GO:0005865 — striated muscle thin filament

---

## 5. Environmental Information

No disease-specific environmental, infectious, or occupational/toxin exposures are documented as causal for CMD1Y in the literature surveyed — it is a purely monogenic sarcomeric cardiomyopathy. As is generic to DCM broadly, comorbid exposures (alcohol, cardiotoxic chemotherapeutics, viral myocarditis) could theoretically modify phenotype expression/severity in a genetically susceptible carrier, but no CMD1Y-specific gene–environment study was identified.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Molecular trigger:** Heterozygous TPM1 missense mutation alters the tropomyosin coiled-coil structure (surface charge, domain stability, or troponin-interaction interface).
2. **Thin-filament regulatory defect:** Mutant tropomyosin shows reduced calcium sensitivity and/or destabilized interaction with actin and the troponin complex, shifting the tropomyosin-actin regulatory equilibrium and altering cross-bridge cycling kinetics.
3. **Cellular contractile defect:** Reduced peak isometric force generation and impaired length-dependent activation in cardiomyocytes (demonstrated directly via in vitro motility assays and iPSC-CM/engineered heart tissue force measurements) — net **hypocontractility**.
4. **Tissue/organ remodeling:** Chronic hypocontractility drives compensatory cardiomyocyte lengthening (sarcomere addition in series rather than parallel, as in hypertrophy), increased ventricular compliance, and progressive chamber dilation without wall thickening.
5. **Organism-level manifestation:** Reduced systolic function → reduced cardiac output → neurohormonal activation (renin-angiotensin-aldosterone, sympathetic) → progressive congestive heart failure, arrhythmia risk, and in severe/pediatric-onset cases, rapid decompensation and death.

**Molecular pathways:** Sarcomeric thin-filament calcium-regulated contraction (troponin–tropomyosin–actin regulatory unit); secondary activation of cardiac stress/remodeling pathways typical of heart failure (natriuretic peptide signaling, RAAS, sympathetic/adrenergic signaling) as downstream consequences rather than primary drivers.

**Cellular processes:** Altered actomyosin cross-bridge cycling; impaired calcium-dependent activation of the thin filament; cardiomyocyte structural remodeling (elongation).

**Protein dysfunction:** Structural destabilization of the tropomyosin coiled-coil (loss of thermal/calorimetric stability in specific domains, e.g., K30E; altered coiled-coil geometry, e.g., D230N; altered surface charge affecting actin-binding affinity, e.g., E40K/E54K).

**Biochemical/functional abnormalities:** Decreased calcium sensitivity of force generation in some variants; reduced maximal force and reduced thin-filament sliding velocity in in vitro motility assays; altered troponin I C-terminal mobile-domain dynamics (E54K, allosteric mechanism).

**Suggested ontology terms:**
- **GO (biological process):** GO:0060048 (cardiac muscle contraction), GO:0086001 (cardiac muscle cell action potential), GO:0055010 (ventricular cardiac muscle tissue morphogenesis), GO:0003009 (skeletal/cardiac muscle contraction - regulation of muscle contraction: GO:0006937)
- **GO (molecular function):** GO:0003785 (actin monomer binding), GO:0005523 (tropomyosin binding)
- **CL (cell type):** CL:0000746 (cardiac muscle cell); CL:0002098 (ventricular cardiac myocyte)
- **UBERON:** UBERON:0002082 (cardiac ventricle); UBERON:0002080 (heart left ventricle)

**Molecular profiling / advanced technologies:** The most recent mechanistic dissection (PMID: 39436707, 2024) used **human iPSC-derived cardiomyocytes**, engineered heart tissue force measurements, and **computational (myofilament) modeling** to directly compare HCM (E62Q) vs. DCM (E54K) TPM1 variants — representative of state-of-the-art functional genomics approaches for sarcomeric cardiomyopathy variant interpretation. No transcriptomic/proteomic/single-cell dataset specific to CMD1Y myocardium was identified in this search.

---

## 7. Anatomical Structures Affected

- **Organ level:** Heart (primary); specifically **left ventricle** (dilation, reduced EF) and frequently **right ventricle/biventricular** involvement; secondary systemic effects of heart failure (pulmonary congestion, hepatic congestion, renal hypoperfusion) as downstream complications. Body system: cardiovascular.
- **Tissue/cell level:** Cardiac (striated) muscle tissue; ventricular cardiomyocytes (CL:0002098) are the principal affected cell population.
- **Subcellular level:** Sarcomere/myofilament (GO:0030017 sarcomere; GO:0036379 myofilament) — specifically the thin filament (actin–tropomyosin–troponin complex).
- **Localization:** Diffuse myocardial involvement (not focal); in the LVNC9-overlap phenotype, additional apex/mid-ventricular noncompaction of the left ventricular wall is described, sometimes with Ebstein anomaly of the tricuspid valve or mitral insufficiency in the allelic condition [OMIM #611878](https://omim.org/entry/611878).
- **UBERON terms:** UBERON:0002079 (left cardiac ventricle), UBERON:0002080/UBERON:0002082 (cardiac ventricle), UBERON:0006566 (cardiac muscle tissue).

---

## 8. Temporal Development

- **Onset:** Highly variable — documented range from **neonatal** (2 weeks of life, K30E case, PMID 39684770) to **adult** onset (40s, E114Q case, PMID 35029218); OMIM describes death "in the third to sixth decades of life in some patients," implying typical adult-onset presentation is common but pediatric/severe presentations occur with specific variants.
- **Progression:** Generally **progressive** — chamber dilation and systolic dysfunction worsen over time; some patients decompensate despite guideline-directed medical therapy (e.g., the K30E infant died of progressive heart failure at 3 years 8 months despite treatment).
- **Disease course pattern:** Chronic, progressive heart failure course typical of sarcomeric DCM, punctuated by risk of malignant arrhythmia/sudden death.
- **Critical periods:** Neonatal/early-childhood presentation (as with de novo K30E) appears to portend a particularly aggressive, rapidly fatal course, suggesting these patients represent a high-risk subgroup warranting early transplant evaluation.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal dominant [OMIM #611878](https://omim.org/entry/611878).
- **Penetrance/expressivity:** Variable expressivity is evident from the literature — the same gene (and even overlapping variant positions) can produce DCM, LVNC, or HCM phenotypes depending on the specific substitution and its biophysical effect on tropomyosin (see Section 6); within-family phenotypic variability is also described (e.g., D230N segregating across 14 affected relatives with presumably variable severity).
- **De novo occurrence:** Documented (K30E, PMID 39684770), alongside clearly familial transmission (D230N in two large multigenerational families; E114Q in a Chinese Han pedigree with maternal death from DCM).
- **Genetic anticipation, germline mosaicism, founder effects, consanguinity:** Not specifically documented for CMD1Y in the literature surveyed.
- **Epidemiology (broader DCM context, since CMD1Y-specific incidence/prevalence figures are not separately tabulated):**
  - Overall DCM prevalence has historically been estimated at ~1:2,500, with more recent population-genomic reappraisals suggesting a substantially higher effective prevalence, potentially ≥1 in 250 individuals when including subclinical/genotype-positive cases ([NCBI Bookshelf NBK553847](https://www.ncbi.nlm.nih.gov/books/NBK553847/)).
  - Familial DCM accounts for roughly 20–50% of cases depending on screening rigor (historically underestimated at ~7%, revised upward to 30–60% of index cases with systematic family echocardiographic screening) ([JACC: Heart Failure 2022](https://www.jacc.org/doi/10.1016/j.jchf.2022.07.009)).
  - Up to 40 genes are implicated in genetic DCM overall, of which TPM1 is a well-established but relatively rare cause (encoding the thin-filament, not the more commonly implicated genes TTN, LMNA, MYH7, or BAG3) (PMC4288017).
  - TPM1-specific prevalence among genotyped DCM cohorts is low (a minority contributor relative to titin-truncating variants, which are the single largest genetic cause of DCM); exact percentage contribution of TPM1 to genetic DCM was not precisely quantified in the sources reviewed here and would benefit from a dedicated cohort-frequency search if needed for curation.
- **Population demographics:** No specific ethnic/geographic enrichment documented for TPM1-DCM; reported pedigrees span Caucasian (D230N families), Chinese Han (E114Q family), and other ancestries, consistent with a pan-ethnic distribution typical of private/rare sarcomeric variants rather than a founder mutation.
- **Sex ratio / age distribution:** Not specifically reported for CMD1Y; general DCM has a male predominance in adult-onset disease, though pediatric/de novo cases (as in K30E) affected a female proband.

---

## 10. Diagnostics

- **Clinical/imaging tests:**
  - **Echocardiography** — primary diagnostic modality; demonstrates LV (± RV) dilation, reduced ejection fraction/fractional shortening, and can detect associated LV noncompaction.
  - **Cardiac MRI** — for tissue characterization, fibrosis assessment (late gadolinium enhancement), and confirmation of noncompaction where suspected.
  - **Electrocardiography** — sinus tachycardia, conduction abnormalities, and arrhythmia surveillance.
  - **Electron microscopy of myocardial biopsy** — historically used to show abnormal sarcomere ultrastructure in early OMIM-cataloged cases, though endomyocardial biopsy is not standard first-line diagnostic practice today.
- **Biomarkers:** Standard heart-failure biomarkers (BNP/NT-proBNP) apply generically; no CMD1Y-specific biomarker identified.
- **Genetic testing:**
  - Clinical DCM gene panels commonly include TPM1 among ~40–100+ genes tested (panels of up to ~78 genes for hereditary DCM are commercially available).
  - Confirmatory approach in reported cases: **next-generation sequencing (whole-exome or targeted panel) followed by Sanger sequencing confirmation and familial segregation analysis** (as used for E114Q, PMID 35029218, and K30E, PMID 39684770).
  - Cascade/family genetic testing is recommended once a proband's causal variant is identified, given the autosomal dominant pattern.
- **Clinical criteria:** Standard DCM diagnostic criteria (LV dilation adjusted for body size + LV systolic dysfunction not explained by abnormal loading conditions or coronary artery disease) apply; differential diagnosis must exclude ischemic cardiomyopathy, myocarditis, toxic/metabolic cardiomyopathy, and other genetic causes (LMNA, TTN, MYH7, BAG3, FLNC, etc.) before attributing disease to TPM1.
- **Screening:** First-degree relatives of a confirmed CMD1Y proband should undergo clinical (echocardiographic) and/or genetic cascade screening given autosomal dominant inheritance and documented within-family segregation in reported pedigrees.

---

## 11. Outcome/Prognosis

- CMD1Y carries a **variable but potentially severe prognosis**: OMIM describes death from progressive cardiac failure in the third to sixth decades in some patients [OMIM #611878](https://omim.org/entry/611878); the E54K variant was originally identified in a 27-year-old man who died awaiting cardiac transplantation (per OMIM/Olson et al. 2001); the K30E de novo variant caused death at 3 years 8 months in a pediatric patient despite treatment (PMID 39684770).
- **Complications:** Progressive heart failure, arrhythmia (documented risk generically in DCM; specific arrhythmia burden not separately quantified for TPM1 carriers in this search), and need for advanced therapies (transplantation) in severe cases.
- **Prognostic factors:** Age of onset appears prognostically important — neonatal/early pediatric onset (as with de novo K30E) is associated with rapid, fatal progression, whereas adult-onset cases (E114Q) can show symptomatic improvement with standard heart-failure pharmacotherapy (beta-blocker) at one-year follow-up.
- No formal survival-curve or actuarial life-expectancy data specific to CMD1Y were identified; prognosis should be extrapolated cautiously from the general sarcomeric-DCM literature, where genotype (e.g., LMNA, FLNC, PLN, TTN) is increasingly used for arrhythmic risk stratification — TPM1 is not among the genes currently flagged for enhanced primary-prevention ICD thresholds in contemporary guidelines, unlike LMNA/FLNC/PLN.

---

## 12. Treatment

No CMD1Y-specific therapy exists; management follows **standard guideline-directed medical therapy (GDMT) for heart failure with reduced ejection fraction**, as used in the reported cases:

- **Pharmacotherapy (documented in CMD1Y case reports):**
  - Beta-blocker (metoprolol) — improved symptoms at 1-year follow-up in the E114Q adult case (NCIT:C15986 Pharmacotherapy; specific agent metoprolol)
  - ACE inhibitor (captopril) — used in the pediatric K30E case
  - Loop diuretic (furosemide) and mineralocorticoid receptor antagonist (spironolactone) — used in the K30E case for volume management
  - Digoxin — used in the K30E case
  - Electrolyte/cardioprotective supplementation (potassium, magnesium)
- **Broader GDMT framework applicable to DCM generally** (not CMD1Y-specific but standard of care): ACE inhibitors/ARBs, beta-blockers, mineralocorticoid receptor antagonists, and **angiotensin receptor–neprilysin inhibitor (ARNI)**, per contemporary heart-failure guidelines; SGLT2 inhibitors are now also part of standard quadruple therapy for HFrEF broadly (not specifically documented in the TPM1 case literature reviewed, but standard of care as of current guidelines).
- **Device therapy:** Implantable cardioverter-defibrillator (ICD) for symptomatic ventricular arrhythmia, resuscitated sudden cardiac death, or per standard EF-based primary-prevention criteria; cardiac resynchronization therapy (CRT) as indicated by QRS/conduction criteria in advanced disease.
- **Advanced/end-stage therapy:** Ventricular assist device (VAD) and/or cardiac transplantation for refractory heart failure — directly relevant, as the original E54K CMD1Y patient died awaiting transplantation.
- **Suggested NCIT terms:**
  - NCIT:C15986 — Pharmacotherapy
  - NCIT:C15747 — Supportive Care
  - NCIT:C15289 — Organ Transplantation (cardiac transplantation)
  - Device-based therapy (ICD/CRT — no precise NCIT clinical-action term readily available; would need `therapeutic_modality: DEVICE`)
- **Experimental/precision approaches:** No TPM1/CMD1Y-specific gene therapy, ASO, or targeted molecular therapy identified in current trials; myofilament-targeted small molecules (e.g., myosin modulators developed for HCM) are mechanistically informative but not established/approved therapies for TPM1-DCM specifically.
- **Genetic counseling:** Recommended given autosomal dominant inheritance and demonstrated family segregation (NCIT:C15240 — Genetic Counseling).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic disease); the closest analog is genetic/family counseling to identify at-risk relatives before symptom onset.
- **Secondary prevention/screening:** Cascade genetic testing of first-degree relatives once a proband's TPM1 variant is confirmed, paired with periodic clinical (echocardiographic) surveillance of genotype-positive, phenotype-negative relatives — standard practice for genetic DCM generally, though no CMD1Y-specific screening protocol/interval was identified in this search.
- **Tertiary prevention:** Early initiation of GDMT in genotype-positive/pre-clinical individuals is an area of active general-DCM management interest but is not specifically validated for TPM1 carriers in the literature reviewed.
- **Reproductive options:** Prenatal/preimplantation genetic testing could be considered for known familial variants, consistent with general practice for highly penetrant autosomal dominant cardiomyopathies, though not specifically documented for CMD1Y.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** TPM1 orthologs are broadly conserved across vertebrates. Mouse ortholog: *Tpm1* (MGI:98809), "tropomyosin 1, alpha."
- **Natural disease in other species:** No naturally occurring TPM1-associated cardiomyopathy in companion animals or wildlife was identified in this search (unlike, e.g., some MYBPC3-associated feline HCM); this appears to be an under-studied area for veterinary comparative pathology.
- **Comparative biology:** The tropomyosin–troponin–actin regulatory apparatus is deeply conserved across striated muscle in all vertebrates, supporting strong evolutionary conservation of the core disease mechanism (calcium-regulated thin-filament activation).

---

## 15. Model Organisms

- **Cellular/in vitro models:** The most current and mechanistically informative CMD1Y-relevant models are **human iPSC-derived cardiomyocytes** and **engineered heart tissue**, used to directly compare DCM-causing (E54K) versus HCM-causing (E62Q) TPM1 variants and demonstrate divergent contractile phenotypes (hypocontractility vs. hypercontractility) (PMID: 39436707, *J Clin Invest*, 2024). Recombinant mutant tropomyosin protein combined with in vitro motility assays and differential scanning calorimetry has also been used to characterize specific variants biophysically (e.g., K30E, PMID 39684770; D230N, PMID 28600229).
- **Computational models:** Myofilament/sarcomere computational modeling has been used alongside iPSC-CM data to mechanistically dissect how TPM1 variants shift the contractile force–calcium relationship (PMID 39436707); separately, myofilament modeling approaches for predicting tropomyosin mutation effects on cardiac contraction have been described generally (PMC5081029).
- **Animal models:** No CMD1Y (TPM1-DCM)-specific transgenic/knock-in mouse or zebrafish model was identified in this search (searches for TPM1 E54K/E40K knock-in mice or zebrafish models did not return a CMD1Y-specific in vivo model; the field currently relies predominantly on iPSC-CM and biophysical reconstitution systems for TPM1-DCM). This is a **notable knowledge gap** relative to other DCM genes (e.g., TNNT2 R141W, LMNA, and titin-based DCM, which all have established mouse knock-in models cited in the general DCM literature) — worth flagging explicitly as a `HUMAN_MODEL_MISMATCH`/knowledge-gap candidate in a dismech entry, since in vivo whole-organism validation of TPM1-DCM mechanisms is currently lacking relative to the strength of the in vitro/computational mechanistic data.
- **Model limitations:** iPSC-CM/engineered heart tissue systems capture sarcomeric contractile mechanics well but do not recapitulate whole-organ chamber remodeling, neurohormonal compensation, or long-term arrhythmic risk — meaning the "hypocontractility → dilation" causal link, while mechanistically well-supported at the cell/tissue level, has not been confirmed in an intact-organ in vivo model specific to CMD1Y.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Term |
|---|---|
| Disease (OMIM) | #611878 CMD1Y |
| Gene | HGNC:12010 (TPM1) |
| Causal variant examples | ClinVar RCV000036354 (D230N), RCV000036318 (M8R) |
| MONDO (parent) | MONDO:0005021 (dilated cardiomyopathy) |
| Orphanet | ORPHA:154 (Familial isolated dilated cardiomyopathy) |
| HP | HP:0001644 (Dilated cardiomyopathy), HP:0001635 (CHF), HP:0001712 (Cardiomegaly), HP:0012664 (Decreased LVEF), HP:0030702 (LV noncompaction) |
| GO (BP) | GO:0060048 (cardiac muscle contraction) |
| GO (MF) | GO:0005523 (tropomyosin binding), GO:0003779 (actin binding) |
| CL | CL:0002098 (ventricular cardiac myocyte) |
| UBERON | UBERON:0002079 (left cardiac ventricle) |
| NCIT (treatment) | C15986 (Pharmacotherapy), C15289 (Organ Transplantation), C15240 (Genetic Counseling) |

---

### Sources

- [OMIM #611878 — CARDIOMYOPATHY, DILATED, 1Y; CMD1Y](https://omim.org/entry/611878)
- [OMIM *191010 — TROPOMYOSIN 1; TPM1](https://omim.org/entry/191010)
- [MedGen C2678476 — Dilated cardiomyopathy 1Y](https://www.ncbi.nlm.nih.gov/medgen/C2678476)
- [NIH GTR — Dilated cardiomyopathy 1Y](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2678476/)
- Olson TM et al., "Mutations that alter the surface charge of alpha-tropomyosin are associated with dilated cardiomyopathy," PMID: [11273725](https://pubmed.ncbi.nlm.nih.gov/11273725/)
- "The structural basis of alpha-tropomyosin linked (Asp230Asn) familial dilated cardiomyopathy," PMID: [28600229](https://pubmed.ncbi.nlm.nih.gov/28600229/)
- ClinVar RCV000036354 — TPM1 D230N / Primary dilated cardiomyopathy
- ClinVar RCV000036318 — TPM1 M8R / Primary dilated cardiomyopathy
- "Novel Mutation Lys30Glu in the TPM1 Gene Leads to Pediatric Left Ventricular Non-Compaction and Dilated Cardiomyopathy," PMID: [39684770](https://pmc.ncbi.nlm.nih.gov/articles/PMC11641563/)
- "Identification of a novel missense mutation in the TPM1 gene via exome sequencing in a Chinese family with dilated cardiomyopathy," PMID: [35029218](https://pmc.ncbi.nlm.nih.gov/articles/PMC8758022/)
- "Distinct mechanisms drive divergent phenotypes in hypertrophic and dilated cardiomyopathy–associated TPM1 variants," *J Clin Invest*, PMID: [39436707](https://pmc.ncbi.nlm.nih.gov/articles/PMC11645150/) (2024)
- "In silico and in vitro models reveal the molecular mechanisms of hypocontractility caused by TPM1 M8R," PMC11392859
- "GENETIC CAUSES OF DILATED CARDIOMYOPATHY," PMC4288017
- "Epidemiology — Dilated Cardiomyopathy," NCBI Bookshelf NBK553847
- "Family Screening in Dilated Cardiomyopathy: Prevalence, Incidence, and Potential for Limiting Follow-Up," *JACC: Heart Failure* (2022), https://www.jacc.org/doi/10.1016/j.jchf.2022.07.009
- "Current Management and Treatment — Dilated Cardiomyopathy," NCBI Bookshelf NBK553842
- Orphanet — TPM1 gene-disease associations (ORPHA:154, ORPHA:54260, ORPHA:155)
- TPM1 gene, GenCC / ClinGen curation, https://thegencc.org/genes/HGNC:12010
- MGI — Tpm1 mouse gene detail, MGI:98809

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.