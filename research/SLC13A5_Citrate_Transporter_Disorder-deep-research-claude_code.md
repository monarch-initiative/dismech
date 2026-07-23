---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-23T11:49:29.544170'
end_time: '2026-07-23T12:04:31.975673'
duration_seconds: 902.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SLC13A5 Citrate Transporter Disorder
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
  web_search_requests: 23
  num_turns: 59
  total_cost_usd: 6.219321000000002
  session_id: 5afb9cc6-33a6-4564-8361-376758dd1910
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SLC13A5 Citrate Transporter Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SLC13A5 Citrate Transporter Disorder** covering all of the
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

Got everything I need. Here's the report.

---

# SLC13A5 Citrate Transporter Disorder — Comprehensive Research Report

**Prepared:** 2026-07-23 · **Target MONDO:** `MONDO:0014392` · **Category:** Mendelian (autosomal recessive)

> **A framing note before the wall of text.** This disease is a lovely, awful little puzzle. Citrate is the molecule your cells hand around like petty cash — it's the first real product of the Krebs cycle, it's the carbon skeleton you build fat from, and it's the mineral-binding glue in bone and tooth enamel. `SLC13A5` encodes the doorway that lets citrate *into* a cell from outside. Break both copies of that door and citrate piles up in the street (blood, spinal fluid, urine) while, at least in theory, the rooms inside go hungry. Babies seize within hours of birth, and their teeth come in soft and brown. Everything below is the detail behind that sketch — and one genuinely surprising plot twist about zinc that has reframed the mechanism in the last two years.

---

## 1. Disease Information

### Overview

SLC13A5 citrate transporter disorder is an ultra-rare autosomal recessive developmental and epileptic encephalopathy caused by biallelic loss-of-function variants in `SLC13A5`, which encodes NaCT — the plasma-membrane sodium-coupled citrate transporter (also known as INDY, from the fly homolog "I'm Not Dead Yet"). The clinical triad is (1) seizure onset within the first hours to days of life, (2) severe global developmental delay with prominent motor and communication impairment, and (3) amelogenesis imperfecta — teeth that erupt with defective enamel.

The most authoritative recent framing comes from the natural-history cohort: *"The SLC13A5 gene encodes a sodium citrate co-transporter, with loss of function variants causing autosomal recessive developmental and epileptic encephalopathy 25, DEE25. DEE25 is an ultra-rare genetic disorder, known to cause neonatal onset epilepsy as well as later neurocognitive and motor impairments."* (PMID:41442826, Ozlu et al., *Epilepsy Res* 2026)

An important nosological wrinkle: despite the "epileptic encephalopathy" label, the EEG evidence argues the cognitive impairment is **not** driven by ongoing epileptiform activity. The EEG study concluded findings *"do not support an ongoing epileptic encephalopathy"* (PMID:32551328), and the 2026 cohort found *"less than a third had frequent or abundant interictal epileptiform activity, suggesting that interictal epileptiform activity was not a primary driver of neurocognitive dysfunction"* (PMID:41442826). In plain terms: this looks more like a *developmental* encephalopathy with epilepsy riding alongside than a disorder where the seizures themselves are eating the brain. That is a curation-relevant distinction — the mechanism chain should not route cognition through seizure burden.

### Key identifiers

| Resource | Identifier | Verified |
|---|---|---|
| MONDO | `MONDO:0014392` — developmental and epileptic encephalopathy, 25 | Yes, local OAK |
| OMIM (phenotype) | `615905` — DEE25 with amelogenesis imperfecta | Yes, MONDO xref |
| OMIM (gene) | `608305` — SLC13A5 | Secondary source only |
| HGNC | `hgnc:23089` — SLC13A5 | Yes, MONDO `RO:0004003` relation |
| DOID | `DOID:0080453` | Yes, MONDO xref |
| GARD | `GARD:0012901` | Yes, MONDO xref |
| MedGen | `MEDGEN:863058` | Yes, MONDO xref |
| UMLS | `UMLS:C4014621` | Yes, MONDO xref |
| NORD | `NORD:1914` | Yes, MONDO xref |
| Orphanet ORPHA | **Not confirmed** — see verification flags | No |
| ICD-10 / ICD-11 | **Not confirmed** — no disease-specific code located | No |
| MeSH | **Not confirmed** | No |

MONDO places it under two parents: `MONDO:0018614` (undetermined early-onset epileptic encephalopathy) and `MONDO:0100455` (neonatal-onset developmental and epileptic encephalopathy).

### Synonyms

From the MONDO synonym block (all verified locally): DEE25; EIEE25; SLC13A5 Citrate Transporter Disorder; SLC13A5 early infantile epileptic encephalopathy; early infantile epileptic encephalopathy 25; epileptic encephalopathy, early infantile, type 25; SLC13A5 deficiency (RELATED). Additional names in community use: SLC13A5 epilepsy; SLC13A5 deficiency disorder; citrate transporter disorder; "Kohlschütter–Tönz syndrome, non-*ROGDI*" (a historical label reflecting the shared epilepsy-plus-amelogenesis-imperfecta picture — **treat this as a named-entity-confusion hazard**, since true Kohlschütter–Tönz syndrome is `ROGDI`-associated and a distinct entity).

### Evidence provenance

Information is a mix of both aggregated and individual-patient sources, and the split matters for evidence typing:
- **Individual-patient / EHR-derived:** the Ciitizen cloud medical-record cohort (n=15, PMID:37025451) and the growth/health analysis on the same records (PMID:34822404).
- **Prospective clinical cohort:** the TESS-sponsored Natural History Study, running since 2020 across Stanford, UT Southwestern, and Brown (PMID:39091896), which generated the epilepsy phenotype (n=30, PMID:41442826), developmental/QoL (PMID:39710583), and sleep (PMID:39457450 — flagged) papers.
- **Aggregated disease-level:** OMIM, MONDO, GARD, NORD.
- **Registry:** the TESS Research Foundation variant registry, described as having *"the most extensive collection of known pathogenic mutations in SLC13A5"* (PMID:39091896).

---

## 2. Etiology

### Primary cause

Purely genetic and monogenic: homozygous or compound heterozygous loss-of-function variants in `SLC13A5` (chromosome 17p13). There is no infectious, toxic, or environmental contribution to disease causation. The original description established the inheritance model: Thevenon et al. identified the gene in two multiplex families, and *"Analysis of rare variants in genes consistent with an autosomal-recessive mode of inheritance led to identification of mutations in SLC13A5"* (PMID:24995870, *Am J Hum Genet* 2014;95(1):113-20).

Independent confirmation followed within a year in eight additional patients from four families, with functional proof of the loss-of-function mechanism: *"We hereby demonstrate that cells expressing mutant sodium-dependent citrate transporter have a complete loss of citrate uptake due to various cellular loss-of-function mechanisms."* (PMID:26384929, Hardies et al., *Brain* 2015;138:3238-50)

### Genetic risk factors

- **Causal variants:** biallelic `SLC13A5` LoF (see §4).
- **Carrier state:** heterozygotes are unaffected. No published evidence of a heterozygote phenotype, though the metabolic literature (see below) raises the theoretical question of subtle lipid/insulin phenotypes in carriers — **not established**.
- **Consanguinity:** a major contributor to case ascertainment. The Saudi series comprised *six affected individuals from three consanguineous families* (PMID:36923948).
- **Susceptibility loci / GWAS:** none relevant to the Mendelian disease. Note that common `SLC13A5` variation *has* been examined by Mendelian randomization for kidney stone and kidney disease risk (PMID:38110950) — that is a separate, population-genetics use of the gene and should not be conflated with DEE25 etiology.
- **Modifier genes:** none identified. This is a genuine knowledge gap — see §9 on expressivity.

### Environmental risk factors

None. This is a fully penetrant Mendelian disorder; no toxin, exposure, diet, occupation, or infectious trigger is implicated in causation. Age, sex, and ethnicity do not modify risk beyond consanguinity-driven founder effects.

### Protective factors

No genetic or environmental protective factors are established. Speculative but worth logging as an open question: the mouse and fly literature shows that *reduced* NaCT/INDY function is metabolically **protective** in adults — knockout mice are *"protected from metabolic syndrome"* with lower body weight, blood pressure and heart rate (PMID:39091896), and *Drosophila* INDY loss-of-function lines *"show lifespan extension and improved metabolism similar to calorie restriction"* (PMID:39091896). NaCT is, in fact, an active **anti-obesity and metabolic drug target**, which is why pharma has invested in NaCT *inhibitors* (PF-06649298, PF-06761281, BIO1383298, ETG-5773). The disorder is thus a striking case of antagonistic pleiotropy: the same loss that extends fly lifespan devastates a human newborn brain.

### Gene–environment interactions

None documented. The only environment-like modifiers reported are **therapeutic**: ketogenic diet response (variable — see §12) and the fever/illness-triggered seizure exacerbation typical of pediatric epilepsy generally, neither of which has SLC13A5-specific published evidence.

---

## 3. Phenotypes

Frequencies below are pooled from the small published cohorts. Because every cohort is under 35 patients and several overlap (the Ciitizen and Natural History cohorts share the TESS patient community), **treat all percentages as small-sample estimates**, and per the dismech frequency SOP, prefer omitting a `frequency:` band over asserting one that a snippet does not directly support.

### Neurological — core

**Seizures / epilepsy — HP:0001250 (Seizure), obligate (100%)**
Universal and near-universally neonatal. Yang et al.: *"Seizures began during the neonatal period in 22 patients"* of 23 (PMID:32551328). Thevenon: *"All seven affected individuals developed subclinical seizures as early as the first day of life"* (PMID:24995870). Brown et al. describe *"frequent, intractable seizures that develop hours or days after birth"* and *"a universal onset of seizures in the first days of life"* (PMID:39091896).
- Onset: neonatal — **HP:0003623 (Neonatal onset)**
- Severity: severe, frequently refractory
- Course: **episodic with age-dependent improvement** — the single most important natural-history finding. *"the highest seizure burden and number of ER visits occurred during the first decade of life, with decreased seizure burden and ER visits after 10 years of age. However, older patients remained on an average of 3 antiseizure medications, and some had breakthrough seizures, suggesting ongoing epilepsy risk."* (PMID:41442826)

**Seizure subtypes** — average 1.7 types per patient (PMID:32551328):
- Generalized tonic-clonic, ~74% — **HP:0002069 (Bilateral tonic-clonic seizure)**; note the OAK-verified label for HP:0007334 is *"Bilateral tonic-clonic seizure with focal onset"*, so pick the term matching the described semiology
- Focal motor seizures — **HP:0011153 (Focal motor seizure)**
- Myoclonic seizures — **HP:0032794 (Myoclonic seizure)** ✅ OAK-verified
- Epileptic/infantile spasms — **HP:0011097 (Epileptic spasm)** ✅ OAK-verified
- Absence seizures — **HP:0002121 (Absence seizure)**

**Status epilepticus — HP:0002133 (Status epilepticus)** ✅ OAK-verified. Common in the neonatal period; three EEGs in the first week of life showed status with seizures *"several times per hour"* (PMID:32551328). Brown et al.: patients *"have frequent emergency room visits and hospitalizations for status epilepticus"* (PMID:39091896).

**Global developmental delay — HP:0001263** ✅ OAK-verified, obligate (100%). All 15 Ciitizen patients (PMID:37025451); all 6 Saudi patients (PMID:36923948). The developmental study found *"significant global impairment across the cohort, with variable quality of life and limited genotype-phenotype correlation"* and that scores were *"largely stable across visits with modest early childhood gains, but skills plateaued in later childhood and adulthood"* (PMID:39710583).

**Delayed gross motor development — HP:0002194** ✅ OAK-verified, ~100%. Quantified milestones (PMID:37025451): unsupported sitting at mean 2.2 years; walking with assistance at 3.9 years; independent walking at 6.1 years. Critically, *"Patients continued to attain motor milestones, though much later than their typically developing peers"* — this is **delay, not degeneration**.

**Intellectual disability** — universal, severity variable. Saudi cohort recorded explicit ID diagnoses in 3/6 (50%) (PMID:36923948), but this reflects diagnostic coding rather than true frequency. Use **HP:0001249 (Intellectual disability)** and avoid asserting a severity band without a supporting quote.

**Hypotonia / mixed tone — HP:0001252 (Hypotonia)** ✅ OAK-verified, 13/15 (87%). *"low or mixed tone with several movement disorders"* (PMID:37025451). Where axial, **HP:0001290 (Generalized hypotonia)** ✅.

**Movement disorders — 6/15 (40%)** (PMID:37025451):
- Dystonia — **HP:0001332 (Dystonia)** ✅ OAK-verified
- Ataxia — **HP:0001251 (Ataxia)** ✅ OAK-verified
- Choreoathetosis — **HP:0001266 (Choreoathetosis)** / chorea **HP:0002072** ✅
Note this is a genuinely severe feature and a translational gap: *"the severe movement disorder in patients has not been reported in animal models"* (PMID:39091896).

**Speech and language impairment — HP:0000750 (Delayed speech and language development)** ✅ OAK-verified, 8/15 (53%) with formal language-disorder diagnoses (PMID:37025451); 3/6 (50%) in the Saudi series (PMID:36923948). Many patients are nonverbal; consider **HP:0001344 (Absent speech)** where documented.

**Developmental regression — HP:0002376** ✅ OAK-verified, 3/15 (20%) (PMID:37025451). Uncommon and generally mild — the disorder is best modeled as static-with-plateau rather than neurodegenerative.

**Microcephaly — HP:0000252** ✅ OAK-verified, 2/6 (33%) in the Saudi series (PMID:36923948). Notably **absent** from Thevenon's original description (*"profound developmental delay with no facial dysmorphism"*, PMID:24995870), and inconsistently reported elsewhere; one conference abstract describes *progressive* microcephaly. Frequency uncertain — flag as variable.

**Sleep disturbance — HP:0002360 (Sleep disturbance)** ✅ OAK-verified. Newly characterized: 26 patients assessed three times over a year with the Sleep Disturbance Scale for Children showed *significant behavioral sleep disturbances*, mirrored by altered sleep architecture in knockout mice (increased activity during the sleep period, decreased paradoxical/REM sleep, shifted EEG power spectra) (*Genes* 2024;15(10):1338, doi:10.3390/genes15101338). This is a well-supported dual human+model finding and a good candidate for a `MODEL_ORGANISM`-plus-`HUMAN_CLINICAL` evidence pair.

### Dental — the cardinal non-neurological sign

**Amelogenesis imperfecta — HP:0000705** ✅ OAK-verified; **Enamel hypoplasia — HP:0006297** ✅; **Abnormal dental enamel morphology — HP:0000682** ✅.

Near-universal. Brown et al. state *"most patients lack tooth enamel (amelogenesis imperfecta)"* (PMID:34822404). Hardies et al. explicitly recommend it as a diagnostic flag: they *"highlight teeth hypoplasia as a possible indicator for SLC13A5 screening"* (PMID:26384929). The Saudi cohort reported dental anomalies in 6/6 (100%): hypodontia, teeth hypoplasia, widely spaced teeth, gingival hyperplasia (PMID:36923948). Affected teeth are variably yellow-to-brown from eruption and involve both primary and permanent dentition.

Associated terms: **HP:0000687 (Widely spaced teeth)**, **HP:0000668 (Hypodontia)**, **HP:0000212 (Gingival overgrowth)**, **HP:0006480 (Abnormal tooth enamel color)**.

### Gastrointestinal and growth

Per PMID:34822404, a *"moderate number"* of problems related to feeding, reflux, vomiting, and weight gain — not precisely quantified in the retrieved abstract.
- Feeding difficulties — **HP:0011968** ✅ OAK-verified
- Dysphagia — **HP:0002015** ✅
- Gastroesophageal reflux — **HP:0002020** ✅
- Constipation — **HP:0002019** ✅
- Growth: *"mostly normal during early life"* with a *"trend toward slower growth in the few adolescent patients with data available"* (PMID:34822404)

The authors' own caveat is worth carrying into the entry: *"gastrointestinal and pulmonary issues may partially result from neurologic severity"* — i.e. these are plausibly **downstream of the neurological phenotype**, not independent organ involvement.

### Respiratory

A *"diverse number"* of respiratory complaints reported (PMID:34822404), unquantified; likely aspiration/tone-related rather than primary.

### Other organ systems — notably spared

Liver, renal, and cardiac systems showed *"single or no abnormal diagnoses"* (PMID:34822404). This is mechanistically interesting given that NaCT expression is **highest in liver**, and it is a real open question (see §6, knowledge gaps).

### Laboratory abnormalities

**Elevated plasma citrate** — the biochemical signature. No dedicated HPO term exists (OAK search of HPO for "citrate" returns only imported CHEBI classes). Closest available: **HP:0033097 / HP:0004364 (Abnormality of carboxylic acid metabolism)** family, or model as a `biochemical` marker rather than a phenotype. Concrete recent numbers from a diagnostic case report: plasma citrate 820 µmol/L (reference 19–83) and urinary citrate 5615 mmol/mol creatinine (reference 162–2200) (*Epileptic Disord* 2026, doi:10.1002/epd2.70178).

**Broader TCA-cycle perturbation** — Bainbridge et al. profiled plasma, CSF and urine by mass spectrometry across five subjects from three families and found *32 dysregulated metabolites*: citrate elevated in both CSF and plasma; fumarate perturbed in urine; isocitrate, 2-methylcitrate and aconitate perturbed in CSF (*Mol Genet Metab* 2017, PMC7539367). Their conclusion is that this constitutes *a diagnostic metabolic signature*.

### Quality of life

Formally measured and uniformly poor. *"All DEE25 pediatric epilepsy quality of life module scores were low, consistent with poor quality of life, and stable across the two years, with cognitive impairment, executive functioning being lower than mood and behavior."* (PMID:41442826). The developmental study likewise found *"variable quality of life"* alongside global impairment (PMID:39710583). The mood/behavior domains scoring *better* than cognitive/executive domains is a meaningful nuance — these children are not, by caregiver report, distressed so much as profoundly limited.

---

## 4. Genetic / Molecular Information

### Causal gene

**`SLC13A5`** (HGNC:23089), chromosome 17p13, gene MIM 608305. Encodes NaCT (Na⁺-coupled citrate transporter), a 12-transmembrane-domain member of the SLC13 divalent-anion/sodium symporter family; ortholog of *Drosophila* INDY. Coding sequence is 1.7 kb (PMID: JCI 10.1172/JCI197503).

### Variant spectrum

- **Total known:** *"More than 40 known SLC13A5 variants lead to epilepsy"* (Goodspeed et al., *Genes* 2022;13(9):1622, PMID:36141051). Of these, approximately *"35 sequence-confirmed missense mutations"* are catalogued (PMID:39442909).
- **Most common:** `c.655G>A` (p.Gly219Arg) and `c.680C>T` (p.Thr227Met) (PMID:36141051). p.G219R is *"the most frequent found in 31 patients,"* followed by S427L in 7 patients (PMID:39442909).
- **Variant classes:** predominantly missense; also nonsense/premature-stop (two in the Hardies series), frameshift (`c.1227dupC`, recurrent in Saudi families), splice-site (`c.1437+5G>A`, novel), a nonstop variant (Chinese family, *Front Genet* 2025), and intronic variants of uncertain significance in ClinVar (e.g. `c.717-6T>C`).
- **Zygosity:** homozygous or compound heterozygous. All germline; no somatic component.
- **Founder effects:** the recurrent `c.1227dupC` in two of three unrelated consanguineous Saudi families (PMID:36923948) is suggestive of a regional founder allele, but the paper does not formally establish haplotype sharing — **do not assert a founder effect without that evidence**.
- **Population allele frequency:** gnomAD carrier frequency was not retrieved in this sweep. Flag as a gap.

### Functional consequences — the Class I / Class II split

This is the most important recent molecular advance and directly determines therapeutic strategy. Jaramillo-Martinez et al. mechanistically phenotyped six frequent missense variants:

> *"Mutants C50R, T142M, and T227M exhibit impaired citrate transport despite normal expression at the cell surface. In contrast, mutations G219R, S427L, and L488P show low total protein expression levels, absence of mature, glycosylated proteins at the cell surface, retention of the proteins in the endoplasmic reticulum, and diminished transport activity."* (PMID:39442909, *J Mol Biol* 2024;436(22))

| | **Class I** | **Class II** |
|---|---|---|
| Variants | C50R, T142M, T227M | G219R, S427L, L488P |
| Cell-surface expression | Normal | Absent |
| Glycosylation | Mature/complex | Immature core only |
| Localization | Plasma membrane | Retained in ER |
| Protein half-life | >24 h (like wildtype) | 1.6–3.3 h |
| mRNA level | Wildtype-like | Wildtype-like |
| Defect type | **Transport-dead but delivered** | **Folding/trafficking failure** |

The therapeutic implication is stated explicitly: *"The two classes of mutations will require fundamentally different approaches for treatment to either restore transport function of the mutant protein that is capable of reaching the cell surface (Class I), or therapies that enable the correction of protein folding defects to enable escape to the cell surface where it may restore transport function (Class II)."* (PMID:39442909)

Class II is, in other words, a **pharmacological-chaperone** problem — structurally the same logic as CFTR correctors in cystic fibrosis. Class I needs something else entirely (potentiator or bypass). Both are addressed indiscriminately by gene replacement, which is one argument for the AAV approach.

Thevenon's original variants disrupted *"residues essential for sodium binding, critical for citrate transport functionality"* (PMID:24995870) — a third mechanistic flavor (substrate/ion-coordination failure) that fits within Class I.

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifiers:** none identified. Given that *"individuals with the same variants vary in seizure frequency and developmental disability, indicating heterogeneity of the disease"* (PMID:36141051), modifiers almost certainly exist but are undiscovered. Good `KNOWLEDGE_GAP` discussion candidate.
- **Epigenetics:** no disease-specific methylation or chromatin data. Not applicable as currently understood.
- **Chromosomal abnormalities:** not a mechanism in this disorder. CMA/karyotype have no diagnostic role.

---

## 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents contribute to disease causation. This section should be explicitly marked as non-applicable rather than left blank, so downstream consumers don't read absence as ignorance.

The only environment-adjacent considerations are (a) dietary intervention as *therapy* (ketogenic diet, §12), and (b) the general pediatric-epilepsy observation that intercurrent illness and fever lower seizure threshold — for which no SLC13A5-specific evidence was located.

---

## 6. Mechanism / Pathophysiology

### The transporter

NaCT moves citrate from the extracellular space into the cytoplasm, powered by the inward sodium gradient — a symporter, so sodium coming downhill drags citrate uphill. The mechanism has been resolved structurally: cryo-EM structures of human NaCT were solved in complex with citrate and with a small-molecule inhibitor, revealing that the inhibitor *binds the same site as citrate and arrests the transport cycle* (Sauer et al., *Nature* 2021, doi:10.1038/s41586-021-03230-x). Brown et al. note it was resolved *"through cryo-electron microscopy at 2 Ångströms resolution"* (PMID:39091896).

A crucial species caveat for anyone reading mouse data: *"human NaCT is a low affinity, but high-capacity transporter and more highly selective for citrate, while rodent NaCT transports citrate and succinate equally well."* (PMID:39091896)

**GO terms:**
- `GO:0015137` citrate transmembrane transporter activity ✅ OAK-verified — molecular function
- `GO:0015746` citrate transport ✅ OAK-verified — biological process
- `GO:0006101` citrate metabolic process ✅
- `GO:0006099` tricarboxylic acid cycle ✅
- `GO:0097186` amelogenesis ✅ (for the dental arm)
- `GO:0007268` chemical synaptic transmission ✅

### Expression and cell types

Highest expression in **liver**, with lower expression in **brain** (PMID:39091896). Within brain, expression is described in **neurons** and **astrocytes**: *"in the brain where NaCT is expressed primarily in astrocytes and to some extent in neurons, citrate serves as an energy source as well as a precursor for the synthesis of the neurotransmitters acetylcholine, GABA, and glutamate"* — though note other sources (PMID:24995870) describe the carrier as *"notably expressed in neurons."* **The neuron-vs-astrocyte primacy is genuinely contested in the literature** and should be curated as such rather than resolved by fiat.

**CL terms:** `CL:0000540` neuron ✅ · `CL:0000127` astrocyte ✅ · `CL:0000059` ameloblast ✅ · `CL:0000182` hepatocyte ✅ · `CL:0000062` osteoblast ✅ (all OAK-verified)

**UBERON terms:** `UBERON:0000955` brain ✅ · `UBERON:0002421` hippocampal formation ✅ · `UBERON:0001954` Ammon's horn ✅ · `UBERON:0001752` enamel ✅ · `UBERON:0002107` liver ✅ · `UBERON:0001091` calcareous tooth ✅ · `UBERON:0001474` bone element ✅

**CHEBI:** `CHEBI:16947` citrate(3-) ✅ · `CHEBI:29105` zinc(2+) ✅

### Causal chain — Hypothesis A: intracellular energy/neurotransmitter failure (the original model)

```
biallelic SLC13A5 LoF  [MOLECULAR]
  → loss of NaCT citrate uptake at the neuronal/astrocytic plasma membrane  [MOLECULAR]
    → reduced cytosolic citrate available for TCA anaplerosis and for
      acetyl-CoA / glutamate / GABA / acetylcholine synthesis  [CELLULAR]
      → neuronal energy deficit + neurotransmitter imbalance  [CELLULAR]
        → neuronal hyperexcitability  [TISSUE]
          → neonatal-onset refractory seizures + impaired neurodevelopment  [ORGANISM]
```

The rationale for why neurons are uniquely vulnerable is stated well by Hardies: *"Neurons are considered incapable of de novo synthesis of tricarboxylic acid cycle intermediates; therefore they rely on the uptake of intermediates, such as citrate, to maintain their energy status and neurotransmitter production."* (PMID:26384929)

Metaphorically: most cells can bake their own bread; neurons buy theirs. Shut the bakery door and they starve while the loaves stack up outside.

**But this model has a serious problem.** Brown et al. report that tissue citrate measurements *contradict a simple loss-of-function model*: citrate is **decreased** in parahippocampal cortex but **not** in hippocampus, and is **increased** in other cell types such as osteoblasts, *"suggesting a potential compensatory mechanism possibly via mitochondrial citrate production"* (PMID:39091896). If intracellular starvation were the whole story, you would expect uniform intracellular depletion. You don't get it.

### Causal chain — Hypothesis B: extracellular citrate over-chelates zinc, disinhibiting NMDA receptors (the new model)

This is the most significant mechanistic development since the disease was described, and it inverts the logic — the problem is not what's missing inside, but what's accumulating outside.

```
biallelic SLC13A5 LoF  [MOLECULAR]
  → citrate accumulates in the extracellular space / CSF  [MOLECULAR]
    → excess extracellular citrate chelates free Zn2+  [MOLECULAR]
      → loss of tonic zinc inhibition of NMDA receptors  [MOLECULAR]
        → sustained NMDA channel opening, excess Ca2+ influx  [CELLULAR]
          → glutamatergic/GABAergic excitatory-inhibitory imbalance,
             neuronal hyperexcitation  [TISSUE]
            → seizures  [ORGANISM]
```

Direct evidence from the zebrafish model:

> *"Slc13a5 protein co-localizes with excitatory NMDA receptors in wild-type zebrafish and NMDA receptor expression is upregulated in the brain of slc13a5 mutant larvae. Additionally, low levels of zinc are found in the plasma membrane of slc13a5 mutants. NMDA receptor suppression and ZnCl2 treatment in slc13a5 mutant larvae rescued neurometabolic and hyperexcitable calcium events, as well as behavioral defects. These data provide empirical evidence in support of the hypothesis that excess extracellular citrate over-chelates the zinc ions needed to regulate NMDA receptor function, leading to sustained channel opening and an exaggerated excitatory response that manifests as seizures."* (PMID:40208862, Dogra et al., *PLoS Biol* 2025;23(4):e3002499)

Pharmacological rescue in that model: memantine 50 µM reduced calcium-event frequency ~73%; MK-801 50 µM comparable; ZnCl₂ 25 µM ~63% reduction with restored behavior. **Memantine and zinc supplementation are therefore the two most obvious repurposing candidates in this disease**, and both are already-approved, well-tolerated agents.

Note the JCI gene-therapy paper frames the disease around *"increased extracellular citrate"* and measures therapeutic success as *decreasing* it (10.1172/JCI197503) — consistent with Hypothesis B being ascendant.

**Curation guidance:** model these as two `mechanistic_hypotheses` groups (e.g. `intracellular_energy_deficit` = CANONICAL/ESTABLISHED and `extracellular_citrate_zinc_nmda` = EMERGING) with the relevant `downstream` edges opting into each via `hypothesis_groups`. They are not mutually exclusive — both could operate — but they predict opposite intracellular citrate directions and completely different drug strategies, so conflating them into one chain would lose real information.

### The dental arm (a separate, cleaner causal chain)

```
biallelic SLC13A5 LoF  [MOLECULAR]
  → loss of citrate uptake by ameloblasts / osteoblasts  [CELLULAR]
    → failure of citrate incorporation into mineralizing matrix  [TISSUE]
      → defective enamel formation and organization  [TISSUE]
        → amelogenesis imperfecta  [ORGANISM]
```

Citrate is not incidental to mineral — it binds and organizes the apatite crystal surface, so tooth and bone need a lot of it. Brown et al.: loss of NaCT *"leads to reduced enamel formation in rodents and human,"* and the `Slc13a5`^R337*/R337*^ mouse shows a *"severe tooth phenotype: disruption of enamel formation and organization"* (PMID:39091896). Osteoblast-specific conditional knockouts show *age-dependent bone phenotypes*, and an osteoblast-focused paper exists (*Bone Rep* 2023, doi:10.1016/j.bonr.2023.101665 — flagged, citation not fully verified).

This arm is mechanistically **independent of the seizure arm** and should be curated as a parallel branch from the same molecular trigger, not as a downstream consequence of the neurological phenotype.

### Systemic / metabolic arm

Untargeted metabolomics in `Slc13a5`-deficient mice revealed a *"critical liver–brain axis for lipid homeostasis"* (*Metabolites* 2022;12(4):351, doi:10.3390/metabo12040351). Citrate exported from mitochondria is the carbon source for de novo lipogenesis via ATP-citrate lyase, so NaCT loss plausibly perturbs brain lipid synthesis — relevant to myelination and to the white-matter changes seen on MRI in a minority of patients.

### Immune involvement, fibrosis, oxidative stress

No evidence of autoimmunity, immunodeficiency, or inflammation-driven pathology. No fibrotic or ischemic tissue-damage mechanism. The zebrafish model does show **increased apoptosis** and reduced neuron number in the optic tectum (PMID:40208862), which is the only direct cell-death evidence in any model — not yet confirmed in human tissue, and a good `HUMAN_MODEL_MISMATCH` candidate.

### Molecular profiling

- **Metabolomics:** the richest layer. 32 dysregulated metabolites across plasma/CSF/urine (Bainbridge et al., PMC7539367); citrate, isocitrate, aconitate, 2-methylcitrate, fumarate.
- **Transcriptomics:** a 2026 weighted gene co-expression network analysis of large human brain transcriptomic datasets examined `SLC13A5` co-expression modules across the lifespan (*Brain Sci* 2026;16(2):163, doi:10.3390/brainsci16020163) — flagged, not fully retrieved.
- **Proteomics:** proteomic analysis was performed on knockout mouse brain/CSF as part of the Henke study (PMID:32682952).
- **Tools:** a genetically encoded **citrate biosensor** (cytoplasmic and mitochondrial variants) is available through Addgene, as are codon-optimized `SLC13A5` Gateway clones (PMID:39091896). These are exactly what you'd want for a compartment-resolved test of Hypothesis A vs B.
- **Single-cell / spatial:** none published for this disorder.
- **Functional genomics screens:** none disorder-specific.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
- **Brain** (`UBERON:0000955`) — the dominant target. Hippocampus/parahippocampal cortex specifically implicated by mouse citrate measurements and electrophysiology (`UBERON:0002421` hippocampal formation, `UBERON:0001954` Ammon's horn).
- **Teeth** (`UBERON:0001091` calcareous tooth; `UBERON:0001752` enamel) — the second cardinal target, and diagnostically the most specific.

**Secondary / complication-driven:**
- Gastrointestinal tract — feeding, reflux, constipation; likely secondary to tone and neurological severity.
- Respiratory tract — likely aspiration-related.
- Bone (`UBERON:0001474`) — subclinical in humans; demonstrated in osteoblast-conditional mice.

**Notably spared despite high expression:** liver (`UBERON:0002107`), kidney, heart — *"single or no abnormal diagnoses"* (PMID:34822404). The hepatic sparing despite hepatic being the highest-expression tissue is a real and underexplained asymmetry.

**Body systems:** nervous (primary), digestive/dental (primary for enamel, secondary for GI), musculoskeletal (tone, bone), respiratory (secondary).

### Tissue and cell level

- Nervous tissue: **neurons** (`CL:0000540`), **astrocytes** (`CL:0000127`) — relative primacy contested, see §6
- Dental epithelium: **ameloblasts** (`CL:0000059`)
- Bone: **osteoblasts** (`CL:0000062`)
- Liver: **hepatocytes** (`CL:0000182`) — highest expression, minimal phenotype

### Subcellular level

- **Plasma membrane** (`GO:0005886`) — normal NaCT location; Class I mutants reach it, Class II do not
- **Endoplasmic reticulum** (`GO:0005783`) — pathological retention site for Class II mutants
- **Mitochondrion** (`GO:0005739`) — where citrate is generated and consumed by the TCA cycle; the proposed site of compensatory citrate production
- **Cytosol** (`GO:0005829`) — where imported citrate would act
- **Extracellular space** (`GO:0005615`) — the site of pathological citrate accumulation under Hypothesis B

### Localization and lateralization

Bilateral and symmetric throughout. Brain MRI is *normal in the majority*: of 15 patients with imaging, *"7 showed at least one normal scan; 4 had white matter changes; remaining abnormalities were non-specific"* (PMID:37025451). The Saudi cohort likewise reported *most studies showed normal imaging*, with isolated findings of nonspecific pontine T2 hyperintensity in one patient and minimal frontal cortical thickening with focal cortical dysplasia in another (PMID:36923948). **Normal MRI in a neonate with severe seizures is itself a diagnostic clue**, and should be curated as an expected negative rather than omitted.

---

## 8. Temporal Development

### Onset

- **Age:** neonatal — hours to days after birth (`HP:0003623` Neonatal onset ✅). *"seizure onset within the first week of life"* (PMID:36141051); *"subclinical seizures as early as the first day of life"* (PMID:24995870); *"a universal onset of seizures in the first days of life"* (PMID:39091896).
- **Pattern:** acute onset of seizures against a background of chronic, static developmental impairment. Some seizures are initially *subclinical* — detectable only on EEG — which delays recognition.

### Progression and stages

The natural history is unusually well characterized for an ultra-rare disease, and the shape is distinctive:

| Stage | Age | Character |
|---|---|---|
| Neonatal/infantile | 0–2 y | Highest seizure burden, status epilepticus, frequent hospitalization |
| Early childhood | 2–10 y | Continued high seizure burden and ER visits; **modest developmental gains** |
| Late childhood/adolescence | >10 y | Seizure burden and ER visits fall; still ~3 ASMs; breakthrough seizures persist; **developmental plateau** |
| Adulthood | — | Skills static; ongoing epilepsy risk |

Key quote: *"the highest seizure burden and number of ER visits occurred during the first decade of life, with decreased seizure burden and ER visits after 10 years of age. However, older patients remained on an average of 3 antiseizure medications, and some had breakthrough seizures, suggesting ongoing epilepsy risk."* (PMID:41442826)

And developmentally: patient scores were *"largely stable across visits with modest early childhood gains, but skills plateaued in later childhood and adulthood"* (PMID:39710583).

- **Rate:** slow; **non-degenerative**. Regression occurs in ~20% and is generally mild (PMID:37025451).
- **Course pattern:** epilepsy is episodic-improving; development is delayed-then-plateaued. **This is not a progressive neurodegeneration** and should not be modeled as one.
- **Duration:** chronic, lifelong.

### Remission patterns

Seizure freedom is achievable in a minority: *"Although seizures are quite severe in many patients later in life, seizure freedom was attainable in a minority of patients"* (PMID:32551328). Whether the age-related seizure decline is treatment-induced or spontaneous is explicitly unresolved — Brown et al. note causality *"(medication efficacy vs. natural progression) remains undetermined"* (PMID:39091896). Excellent `KNOWLEDGE_GAP` candidate.

### Critical periods

Two, with opposite implications:
1. **Neonatal period** — window of maximum seizure burden and, presumably, maximum opportunity to alter developmental trajectory.
2. **Early brain development for intervention** — the gene-therapy data show *"Treatment benefits were achieved with administration during early brain development and in young adult mice, indicating therapeutic efficacy across developmental and postdevelopmental stages"* (10.1172/JCI197503). That the adult window is not closed is a genuinely hopeful and non-obvious finding for a neurodevelopmental disorder.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** no reliable published figure. Consistently described as "ultra-rare." Cohort sizes (30, 26, 23, 15, 6) and the variant tallies (G219R in 31 patients) suggest a **globally identified population in the low hundreds**. Orphanet prevalence class not retrieved — flag as a gap. For dismech, `prevalence_class: ULTRA_RARE` with `measure_type: CASES_IN_LITERATURE` is the defensible encoding; do not fabricate a `rate_per_100000`.
- **Incidence:** not established.
- **Carrier frequency:** not retrieved from gnomAD in this sweep — flag.

### Genetic parameters

- **Inheritance:** autosomal recessive — `HP:0000007 (Autosomal recessive inheritance)`. Firmly established across all cohorts.
- **Penetrance:** appears complete in biallelic carriers. No reported unaffected homozygotes.
- **Expressivity:** **variable** — and this is a headline finding. *"individuals with the same variants vary in seizure frequency and developmental disability, indicating heterogeneity of the disease"* (PMID:36141051), and the natural-history study found *"limited genotype-phenotype correlation"* (PMID:39710583). The Class I/II biochemical split does not map cleanly onto clinical severity.
- **Anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not reported.
- **Founder effects:** possible recurrent `c.1227dupC` in Saudi families (PMID:36923948) — suggestive, not proven.
- **Consanguinity:** a major factor in Middle Eastern ascertainment; three consanguineous Saudi families in one series.

### Population demographics

- **Ethnic distribution:** cases reported from Europe (France, Belgium/Netherlands via EuroEPINOMICS), North America (TESS cohorts), Saudi Arabia, and China. No evidence of true ethnic predilection beyond consanguinity-driven clustering.
- **Sex ratio:** approximately 1:1, as expected for autosomal recessive. Yang: 11 males / 12 females of 23 (PMID:32551328). Ciitizen: 8 female / 7 male of 15 (PMID:37025451).
- **Age distribution of living patients:** wide — the Yang cohort spanned *3 months to 29 years* (PMID:32551328), and the natural history study enrolls *"infants to adults"* (PMID:39091896). Survival into adulthood is clearly common.

---

## 10. Diagnostics

### Laboratory tests and biomarkers

**Plasma citrate is the key biochemical biomarker** and is emerging as a first-line test. Concrete values from a 2026 diagnostic case: plasma citrate 820 µmol/L against a reference range of 19–83 µmol/L, and urinary citrate 5615 mmol/mol creatinine against 162–2200 (*Epileptic Disord* 2026, doi:10.1002/epd2.70178). That paper argues *plasma and urinary citrate quantification are reliable and accessible biomarkers in the diagnostic workup of SLC13A5-DEE*, with particular value in **resolving variants of uncertain significance** — a functional assay you can order from any metabolic lab.

Supporting metabolic signature (Bainbridge et al., PMC7539367): citrate ↑ in plasma and CSF; isocitrate, aconitate, 2-methylcitrate ↑ in CSF; fumarate perturbed in urine. Their framing is that these *define a diagnostic metabolic signature that can aid in diagnosing children with this disease*.

Suggested LOINC anchors: citrate in serum/plasma and citrate in 24-hour urine — **specific LOINC codes not verified in this sweep**; look them up before curating a `reference_ranges` block.

Note that CSF and plasma citrate double as **pharmacodynamic biomarkers** — the gene-therapy study used exactly these as its primary readout (plasma citrate decreased to 65% ± 8.0% of WT; CSF citrate to 81% ± 3.9% of WT after high-dose treatment) (10.1172/JCI197503).

### Imaging

Brain MRI is **usually normal or nonspecific** and does not establish the diagnosis. White-matter changes in a minority (4/15), nonspecific pontine signal change, and one case of focal cortical dysplasia (PMID:37025451; PMID:36923948). MRI's main value is exclusionary.

### Electrophysiology

EEG is abnormal in most patients but **atypically well-preserved for the seizure burden**. Neonatal EEGs show discontinuous background and can capture status epilepticus. Older patients show *"normal or had mild theta range slowing"* with *"well-preserved background for age"* despite frequent seizures (PMID:32551328). The 2026 cohort: *"Most EEGs were abnormal, but less than a third had frequent or abundant interictal epileptiform activity"* (PMID:41442826). A neonate with frequent seizures and a surprisingly intact EEG background should raise this diagnosis.

### Genetic testing — the definitive route

- **Approach:** sequencing of `SLC13A5` demonstrating biallelic pathogenic variants. Wikipedia's clinical summary describes diagnosis via *"exome sequencing"* or an epilepsy-focused gene panel.
- **WES / WGS:** high utility; this is how the gene was originally found (PMID:24995870) and how most cases are ascertained. WGS adds coverage of deep-intronic and splice variants (e.g. `c.1437+5G>A`).
- **Gene panels:** neonatal/infantile epilepsy panels reliably include `SLC13A5`. Genomics England PanelApp also lists `SLC13A5` on the **Amelogenesis imperfecta** panel — meaning a child worked up for enamel defects can land on the diagnosis from the dental side.
- **Single-gene testing:** appropriate for targeted family testing after a proband is identified, and for known-founder populations.
- **CMA, karyotype, FISH, mtDNA, repeat expansion:** **no role.** Explicitly not applicable — worth stating so, since neonatal seizure workups often include them.

### Omics-based diagnostics

Targeted **metabolomics** (plasma/urine/CSF organic acids with citrate quantification) is the practically useful omics modality — see biomarkers above. RNA-seq has a theoretical role for splice-variant interpretation. Proteomics, epigenomics, and liquid biopsy: no established role.

### Clinical criteria and differential diagnosis

No formal consensus diagnostic criteria exist. Practical diagnostic gestalt: **neonatal-onset refractory seizures + normal-ish MRI + preserved EEG background + defective tooth enamel + elevated plasma citrate**.

Differential diagnosis:
- Other neonatal DEEs: `KCNQ2`, `KCNT1`, `SCN2A`, `STXBP1`, `CDKL5` — distinguished by genotype; none produce amelogenesis imperfecta.
- **Kohlschütter–Tönz syndrome** (`ROGDI`) — the closest phenocopy, sharing epilepsy plus amelogenesis imperfecta. **This is the primary named-entity-confusion hazard for this disease.** Distinguish by gene, and note KTS typically has later onset and progressive dementia.
- Pyridoxine-dependent epilepsy (`ALDH7A1`), pyridoxal-phosphate-responsive epilepsy (`PNPO`) — must be excluded early because they are treatable; distinguished by biochemical markers and trial of pyridoxine.
- GLUT1 deficiency (`SLC2A1`) — another transportopathy with a diet-based therapy; distinguished by low CSF glucose.
- Molybdenum cofactor deficiency / sulfite oxidase deficiency — neonatal refractory seizures with distinct biochemistry.
- Mitochondrial disorders — overlapping TCA-intermediate abnormalities; citrate elevation with otherwise-normal lactate favors SLC13A5.

### Screening

- **Newborn screening:** not currently included in any panel. Plasma citrate elevation is in principle detectable by the MS/MS platforms already used for NBS, making this a plausible future addition — **no published NBS program exists**; do not assert one.
- **Carrier screening:** `SLC13A5` is included on some expanded carrier-screening panels; relevant for consanguineous couples and known-carrier families.
- **Cascade screening:** standard for siblings of a proband (25% recurrence risk).

---

## 11. Outcome / Prognosis

### Survival and mortality

**No published survival rate, life expectancy, or mortality figure exists for this disorder.** This is a real gap and should be recorded as unknown rather than estimated. What we can say indirectly: patients survive into adulthood — the Yang cohort included a 29-year-old (PMID:32551328), and the natural history study enrolls adults (PMID:39091896). Risks that plausibly drive excess mortality (status epilepticus, aspiration, SUDEP) are present but unquantified.

### Morbidity and function

Severe and lifelong. Multi-domain impairment: motor (independent walking delayed to ~6 years, many never ambulate independently), communicative (many nonverbal), cognitive (severe ID), and behavioral. The developmental study documented *"significant global impairment across the cohort"* on Mullen Scales of Early Learning, Peabody Developmental Motor Scales, and Vineland Adaptive Behavior Scales, and concluded *"poor developmental prognosis across multiple age-appropriate measures"* (PMID:39710583).

### Quality of life

Measured with a validated instrument and uniformly poor: *"All DEE25 pediatric epilepsy quality of life module scores were low, consistent with poor quality of life, and stable across the two years, with cognitive impairment, executive functioning being lower than mood and behavior."* (PMID:41442826). Caregiver burden is substantial; the natural-history studies explicitly assess *"the impact on quality of life for caregivers and patients"* (PMID:39091896).

### Complications

Status epilepticus with hospitalization; dental disease requiring extensive restorative work; feeding difficulty and reflux; aspiration risk; respiratory complaints; sleep disruption (with knock-on effects on daytime function and caregiver wellbeing); orthopedic sequelae of impaired mobility.

### Recovery potential and prognostic factors

No recovery of lost function is expected, but crucially neither is progressive loss — the trajectory is **delay then plateau**, not decline. The one clearly favorable prognostic trend is **age**: seizure burden and emergency use fall after the first decade.

Established prognostic factors are absent. Genotype is explicitly a *poor* predictor (*"limited genotype-phenotype correlation"*, PMID:39710583) — which is itself useful information for genetic counseling. Plasma/CSF citrate is a diagnostic and pharmacodynamic biomarker, **not** yet a validated prognostic one.

---

## 12. Treatment

There is **no disease-modifying therapy approved**. Brown et al. are blunt: *"there is no cure for SLC13A5 citrate transporter disorder,"* and *"patients continue to rely on symptom management"* (PMID:39091896).

### Antiseizure medications (`MAXO` pharmacotherapy; `NCIT:C15986`)

Seizures are frequently medically intractable and polytherapy is the norm — older patients average **3 concurrent ASMs** (PMID:41442826). No single agent is established as first-line, but the natural-history data give the first real signal:

**Valproic acid** — the strongest evidence to date. *"Multiple antiseizure medications were felt to be of benefit by caregivers, with valproic acid having the highest utilization with 22 patients and 80 % of caregivers reporting it to be helpful or very helpful. Higher doses of valproic acid correlated with caregiver reported benefit."* (PMID:41442826). `therapeutic_agent`: `CHEBI:39867` valproic acid ✅ OAK-verified.

**Phenobarbital** — most-used in the earlier cohort (9 patients) and rated most effective by 5 caregivers (PMID:32551328). `CHEBI:8069` phenobarbital ✅.

**Acetazolamide** — a carbonic-anhydrase inhibitor with an interesting mechanistic rationale (it perturbs bicarbonate/pH handling that intersects with citrate transport). Used by 8 of 23 patients (PMID:32551328); Klotz et al. reported it *decreased seizures in four patients* (PMID:27261973). Response is variable. `CHEBI:27690` acetazolamide ✅ OAK-verified.

Others in use without SLC13A5-specific efficacy data: levetiracetam (`CHEBI:6437` ✅), topiramate (`CHEBI:63631` ✅), phenytoin (`CHEBI:8107` ✅), benzodiazepines (lorazepam `CHEBI:6539` ✅), stiripentol.

**Important caveat for the entry:** the caregiver-reported benefit data are observational, unblinded, and confounded by the natural age-related decline in seizures. Curate them as `HUMAN_CLINICAL` observational evidence, not as efficacy claims.

### Dietary therapy — ketogenic diet (`MAXO:0000088` dietary intervention ✅)

Genuinely conflicting evidence, and the entry should say so plainly. Hardies et al. reported: *"All three patients who tried the ketogenic diet responded well to this treatment, and future studies will allow us to ascertain whether this is a recurrent feature in this severe disorder."* (PMID:26384929) — a strikingly positive small signal. But the patient-community and later clinical experience is that *some patients improved and others worsened while on the ketogenic diet*. This is not a resolved question; model it as an open therapeutic hypothesis rather than a recommendation.

Note MAXO has no dedicated "ketogenic diet" term (OAK search returns only `MAXO:0000088` dietary intervention) — use the generic term with a specific `preferred_term`, per the dismech `preferred_term` convention.

### Triheptanoin

An anaplerotic odd-chain triglyceride that refills TCA intermediates — mechanistically the most rational metabolic therapy under Hypothesis A. Several children with SLC13A5 deficiency have tried it. **There are no published clinical trial outcomes in this disorder**, and anecdotal reports have not been encouraging. Curate as experimental with `NO_EVIDENCE` or omit.

### Repurposing candidates from the zinc/NMDA hypothesis

Not yet tried in humans, but the preclinical case is specific and the drugs are available:
- **Memantine** (`CHEBI:64312` ✅ OAK-verified) — NMDA antagonist; ~73% reduction in hyperexcitable calcium events in zebrafish (PMID:40208862)
- **Zinc supplementation** (ZnCl₂; `CHEBI:29105` zinc(2+) ✅) — ~63% reduction, with behavioral rescue (PMID:40208862)

The authors' own conclusion: *human studies suggest testing these compounds for SLC13A5 epilepsy treatment potential.* These belong in the entry as `IN_VITRO`/`MODEL_ORGANISM`-supported experimental treatments with an explicit `HUMAN_MODEL_MISMATCH` discussion — zebrafish larvae are not human neonates, and the citrate-zinc stoichiometry in human CSF has not been directly measured.

### Gene therapy (`MAXO:0001001` gene therapy ✅ OAK-verified)

**The most advanced disease-modifying approach, and it has just moved into humans.**

*Preclinical:* Bailey et al., *J Clin Invest* 2026;136(8), doi:10.1172/JCI197503 — a self-complementary AAV9 vector carrying codon-optimized human `SLC13A5` under a ubiquitous promoter, delivered into cerebrospinal fluid. The abstract:

> *"Cerebrospinal fluid delivery of AAV9/SLC13A5 decreased extracellular citrate levels, normalized electrophysiologic and sleep architecture abnormalities, and restored resistance to chemically induced seizures and death. Treatment benefits were achieved with administration during early brain development and in young adult mice, indicating therapeutic efficacy across developmental and postdevelopmental stages. Comparison of delivery routes in young adult KO mice showed that higher brain targeting achieved with intra–cisterna magna delivery resulted in greater treatment benefit as compared with intrathecal lumbar puncture delivery."*

Quantitatively: plasma citrate reduced to 65% ± 8.0% of WT; CSF citrate to 81% ± 3.9% of WT at 6 months; dose-dependent reduction in EEG spike trains; increased latency and reduced severity of pentylenetetrazol-induced seizures; mortality 29% untreated vs 18–21% treated. Safety was clean — *"Vector treatment in KO mice was well tolerated, with no adverse effects observed,"* with blood chemistry *"within normal ranges across all groups."*

*Clinical:* **NCT07102524** — *"A Phase 1/2 Open-Label Intrathecal Administration of TSHA-105 to Determine the Safety and Efficacy in Subjects With SLC13A5 Citrate Transporter Disorder Caused by a Mutation in the SLC13A5 Gene."*
- Intervention: TSHA-105, AAV9-based gene therapy expressing functional SLC13A5, single intrathecal (lumbar) dose
- Phase 1/2, open-label · Status: Recruiting · Sponsor: **TESS Research Foundation** (the patient-advocacy organization itself — notable)
- Enrollment: ~8 participants · Ages 2–20 years with confirmed biallelic `SLC13A5` variants
- Primary outcome: safety and tolerability over 5 years (AEs, safety labs, vitals, EKG, echo)
- Secondary: Peabody and Mullen scales, a disease-specific movement scale, adaptive behavior, QoL, seizure tracking, CGI
- Site: UT Southwestern Medical Center, Dallas, TX · Estimated start: 2026-07-15

TSHA-105 holds FDA **Orphan Drug** and **Rare Pediatric Disease** designations and an EC Orphan Drug designation.

**A discrepancy worth flagging for curation:** the JCI preclinical work favors **intra-cisterna magna** delivery as superior, while the trial uses **intrathecal lumbar** administration — presumably a safety/practicality tradeoff in children. Worth noting in the entry rather than smoothing over.

### Other advanced therapeutics

- **Cell therapy, RNA therapies (ASO/siRNA), immunotherapy:** none in development. **Not applicable.** Note that ASO approaches are conceptually poorly suited here — this is a loss-of-function recessive disorder needing protein *restoration*, not knockdown or splice correction (no recurrent splice-amenable allele has been identified).
- **Pharmacological chaperones:** the logical Class II approach, explicitly proposed (PMID:39442909), but no compound is in development.
- **Small-molecule NaCT modulators:** the existing chemical matter (PF-06649298, PF-06761281, BIO1383298, ETG-5773) are all **inhibitors** developed for metabolic disease — wrong direction for this disorder, though useful as structural probes.

### Surgical and interventional

- **Epilepsy surgery:** no role — this is a genetic, generalized/multifocal epilepsy without a resectable focus (aside from the single reported focal cortical dysplasia case).
- **Gastrostomy tube placement** (`MAXO:0000004` surgical procedure ✅) for feeding failure.
- **Restorative dental procedures** — crowns, composite restorations, extractions. Clinically significant and lifelong given the enamel defect.

### Supportive and rehabilitative

Explicitly documented as the mainstay: *"physical, occupational, and speech therapies"* (PMID:39091896).
- `MAXO:0000011` physical therapy ✅ OAK-verified
- `MAXO:0001351` occupational therapy ✅ OAK-verified
- `MAXO:0000930` speech therapy ✅ OAK-verified
- `MAXO:0000950` supportive care ✅ OAK-verified
- `MAXO:0000079` genetic counseling ✅ OAK-verified

Also: nutritional support, reflux and constipation management, sleep hygiene/management (newly justified by the sleep data), and orthopedic/positioning support.

### Treatment strategy

No published treatment algorithm or guideline exists. Practical sequence in current use: rapid genetic diagnosis → exclude treatable mimics (pyridoxine-dependent, PNPO, GLUT1) → ASM polytherapy with valproate/phenobarbital as commonly-used anchors → consider acetazolamide → consider ketogenic diet trial with close monitoring given bidirectional response → comprehensive rehabilitation and dental care → clinical trial referral.

### Pharmacogenomics

No SLC13A5-specific pharmacogenomic data. General ASM pharmacogenomics applies (e.g. *HLA-B\*15:02* for carbamazepine, *CYP2C9* for phenytoin) but is not disease-specific.

---

## 13. Prevention

### Primary prevention

Not preventable in the classical sense — this is a germline monogenic disorder. Prevention is entirely reproductive:
- **Genetic counseling** (`MAXO:0000079` ✅) — 25% recurrence risk per pregnancy for carrier couples; both parents obligate carriers.
- **Carrier screening** — expanded carrier panels; particularly valuable in consanguineous populations given the Saudi and other consanguinity-associated cases.
- **Preimplantation genetic testing (PGT-M)** and **prenatal diagnosis** (CVS/amniocentesis) — available once familial variants are known.
- **Consanguinity counseling** as a public-health measure in high-consanguinity populations.

### Secondary prevention

- **Early diagnosis** is the actionable lever. Rapid genomic sequencing in neonatal-onset refractory seizures; plasma citrate as a fast, cheap adjunct. The gene-therapy data showing benefit during *"early brain development"* (10.1172/JCI197503) mean that shortening the diagnostic odyssey may soon have direct therapeutic consequence.
- **Newborn screening:** not implemented; theoretically feasible via citrate on existing MS/MS platforms. Flag as speculative.
- **Cascade testing** of siblings.

### Tertiary prevention

Preventing complications in diagnosed patients:
- Seizure-action plans and rescue medication to reduce status epilepticus and ER utilization
- Proactive dental care from first eruption — because the enamel defect is predictable, restorative planning can start before decay
- Aspiration precautions, feeding assessment, reflux management
- Sleep assessment and management
- Bone-health monitoring (given the osteoblast biology and immobility risk)
- SUDEP counseling as for any refractory epilepsy

### Not applicable

Immunization (no infectious component), behavioral risk-factor modification, environmental interventions, chemoprophylaxis, public-health/vector control. Standard childhood immunization is of course recommended but is not disease-specific prevention.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBI Taxon | Gene | Notes |
|---|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | `SLC13A5` (HGNC:23089) | Low-affinity, high-capacity, citrate-selective |
| *Mus musculus* | `NCBITaxon:10090` | `Slc13a5` | Transports citrate **and succinate equally well** |
| *Rattus norvegicus* | `NCBITaxon:10116` | `Slc13a5` | Knockdown studies only |
| *Danio rerio* | `NCBITaxon:7955` | `slc13a5a`, `slc13a5b` (two paralogs) | Both must be disrupted |
| *Drosophila melanogaster* | `NCBITaxon:7227` | `Indy` | H⁺/citrate symporter; structures solved |

**The species difference in substrate selectivity is not a footnote — it is a first-order caveat.** *"human NaCT is a low affinity, but high-capacity transporter and more highly selective for citrate, while rodent NaCT transports citrate and succinate equally well"* (PMID:39091896). Any mouse result about citrate handling may be confounded by succinate.

### Natural disease in other species

**None reported.** No naturally occurring `SLC13A5` disorder has been described in companion animals, livestock, or wildlife. No OMIA entry located. No breed predisposition, therefore no VBO term applies. No veterinary relevance.

### Comparative biology

The comparative story is striking and inverted. In *Drosophila*, `Indy` loss-of-function lines *"show lifespan extension and improved metabolism similar to calorie restriction"* (PMID:39091896) — the gene is literally named for the fact that losing it makes flies live longer. In mice, knockout confers *protection from metabolic syndrome*, lower body weight, blood pressure and heart rate. In humans, the same loss causes catastrophic neonatal epilepsy.

The evolutionary reading: the citrate-uptake function is conserved, but its *criticality* shifted with the metabolic demands of the mammalian — and especially human — brain. Invertebrates and rodents tolerate NaCT loss because their neurons are less dependent on exogenous citrate (and/or their extracellular citrate/zinc balance differs). The transport machinery is ancient; the vulnerability is recent.

### Transmission

**Not applicable.** No zoonotic potential, no cross-species transmission — this is a germline genetic disorder.

---

## 15. Model Organisms

The model toolbox for this disorder is unusually rich for an ultra-rare disease, largely because of coordinated patient-advocacy investment (TESS Research Foundation). Brown et al. (PMID:39091896) is the definitive catalog.

### Mouse models (`NCBITaxon:10090`)

**Global `Slc13a5` knockout (C57BL/6J)** — the workhorse. Phenotype (PMID:39091896; PMID:32682952):
- Spontaneous seizure activity beginning ~7 weeks; approximately 50% of mice have spontaneous seizures
- Lowered seizure threshold to chemoconvulsants (PTZ)
- Pro-epileptogenic neuronal excitability changes in hippocampus
- Elevated CSF and plasma citrate; **decreased** citrate in parahippocampal cortex but not hippocampus
- Reduced body weight, lower blood pressure and heart rate, protection from metabolic syndrome
- Altered sleep architecture: increased activity during sleep period, decreased paradoxical (REM) sleep, shifted absolute EEG power spectral density (*Genes* 2024;15(10):1338)

The foundational characterization (Henke et al., *Neurobiol Dis* 2020;143:105018, PMID:32682952) used video-EEG monitoring, behavioral testing, electrophysiology, proteomics and metabolomics of brain and CSF, and concluded that *SLC13A5 is involved in brain citrate regulation and that abnormalities in this regulation can induce seizures.*

**`Slc13a5`^R337*/R337*^ knock-in** — carries a premature-stop allele and shows a *"severe tooth phenotype: disruption of enamel formation and organization"* (PMID:39091896). This is the model of choice for the dental arm.

**`Slc13a5`^fl/fl^ conditional knockout** — tissue-specific deletions, including osteoblast-specific lines showing *age-dependent bone phenotypes* (PMID:39091896).

**Humanized mice** — wildtype human `SLC13A5` and the most common patient variant **p.G219R** knocked into the endogenous mouse locus. **Currently uncharacterized** (PMID:39091896) — this is arguably the highest-value untapped resource in the field, since it would resolve the human-vs-rodent selectivity confound.

**Overexpression models** — neuronal overexpression produces *autistic-like behaviors and disrupted white matter integrity*; global overexpression produces a *progeria phenotype* (PMID:39091896). Both directions of dosage are pathological, which is mechanistically interesting.

**Rat knockdown** — reduced fasting plasma insulin and triglycerides (metabolic focus, not neurological).

**Phenotype recapitulation:** partial. Recapitulates seizure susceptibility, citrate elevation in CSF/plasma, sleep architecture disruption, enamel defect (in the R337* line), and metabolic phenotype. **Limitations, stated explicitly:** rodent models show a *"milder neurologic phenotype of the human disorder"*; *"the severe movement disorder in patients has not been reported in animal models"*; and the rodent transporter's dual citrate/succinate selectivity differs from human (PMID:39091896). Seizures also start at ~7 weeks in mice versus day 1 in humans — the developmental timing does not translate.

### Zebrafish (`NCBITaxon:7955`)

CRISPR/Cas9 double mutants in `slc13a5a` and `slc13a5b` (Dogra et al., PMID:40208862) — the best-characterized non-mammalian model and the source of the zinc/NMDA hypothesis. Phenotype: cognitive dysfunction, sleep disturbance, fewer neurons with increased apoptosis in the optic tectum, excitatory/inhibitory gene-expression imbalance, increased `fosab`, disrupted neurometabolism, and neuronal hyperexcitability by extracellular field recording and live calcium imaging.

**Applications:** high-throughput drug screening — this model directly generated three testable therapeutic leads (memantine, MK-801, ZnCl₂). Additional uncharacterized `slc13a5` mutants are available from ZIRC.

**Limitations:** two paralogs complicate genetics; larval zebrafish "seizure-like events" are not clinical seizures; zinc and citrate concentrations in fish extracellular fluid may not mirror human CSF. The zinc-chelation hypothesis is **empirically supported in zebrafish and inferred, not demonstrated, in humans** — a textbook `HUMAN_MODEL_MISMATCH`.

### *Drosophila* (`NCBITaxon:7227`)

Multiple `Indy` loss-of-function lines. Phenotype is **metabolic and longevity-related, not epileptic**: lifespan extension and improved metabolism resembling caloric restriction (PMID:39091896). Cryo-EM structures of *Drosophila* INDY revealed the H⁺/citrate symport mechanism (*Life Sci Alliance* 2025;8(4):e202402992). Useful for transport mechanism and metabolism; **not a disease model**.

### Cell and in vitro models

- **Patient-derived iPSC lines:** four lines with compound heterozygous variants (one with an isogenic corrected control; more isogenic controls in development), plus three heterozygous-carrier iPSC lines as controls. Owned by TESS Research Foundation (PMID:39091896).
- **Derived neural precursor cells** from those iPSCs.
- **Heterologous expression systems** — the platform for the Class I/II classification work: cell-surface biotinylation, glycosylation state, half-life, and citrate-uptake assays in transfected cells (PMID:39442909).
- **Genetically encoded citrate biosensor** — cytoplasmic and mitochondrial variants, plasmids at Addgene (PMID:39091896). Directly enables the compartment-resolved experiment that would discriminate Hypothesis A from Hypothesis B.
- **`SLC13A5` expression plasmids** — codon-optimized Gateway entry clones at Addgene.
- **NaCT inhibitor tool compounds:** PF-06649298 (Pfizer compound 2), PF-06761281, BIO1383298 (human-specific), ETG-5773 (cross-species, non-competitive).

### Resources

MGI, IMPC/KOMP, IMSR (mouse); ZFIN and ZIRC (zebrafish); FlyBase (*Drosophila*); Addgene (plasmids, biosensors); TESS Research Foundation (iPSCs, variant registry, natural-history data); Alliance of Genome Resources (ortholog integration).

---

## Verification Flags — read before curating

Per the dismech anti-hallucination SOP, here is exactly what I did and did not verify:

**Fully verified (verbatim abstract retrieved from PubMed/PMC/publisher):**
`PMID:24995870` (Thevenon 2014) · `PMID:26384929` (Hardies 2015) · `PMID:41442826` (Ozlu 2026 epilepsy phenotype) · `PMID:39710583` (Ozlu 2025 development/QoL) · `PMID:39442909` (Jaramillo-Martinez 2024, Class I/II) · `PMID:40208862` (Dogra 2025 zebrafish) · `PMID:39091896` (Brown 2024 toolbox) · `PMID:32551328` (Yang 2020 EEG) · `PMID:36923948` (AlQudairy 2023 Saudi) · `PMID:34822404` (Brown 2021 growth/health) · `PMID:37025451` (Spelbrink 2023 Ciitizen) · `PMID:36141051` (Goodspeed 2022 review) · `doi:10.1172/JCI197503` (Bailey 2026 gene therapy) · `NCT07102524`.

**Needs verification before use:**
- `PMID:32682952` vs `32682953` for Henke et al. 2020 *Neurobiol Dis* 143:105018 — **two sources gave different PMIDs.** Resolve with `just fetch-reference` before citing.
- The sleep paper (*Genes* 2024;15(10):1338, doi:10.3390/genes15101338) — PMID not retrieved; I have seen `39457450` referenced but did **not** confirm it. Do not use that PMID without checking.
- Bainbridge et al. TCA metabolomics — I have PMC7539367 and the journal (*Mol Genet Metab* 2017) but **not a confirmed PMID**.
- Klotz et al. 2016 *Mol Med* (`PMID:27261973`) — cited for the acetazolamide-in-four-patients claim from a search snippet, **abstract not directly retrieved**. Verify the snippet before quoting.
- Nou-Fontanet et al. citrate biomarker (*Epileptic Disord* 2026, doi:10.1002/epd2.70178) — publisher returned 403; the citrate values (820 µmol/L, 5615 mmol/mol creatinine) come from a search snippet. **Verify before curating those numbers.**
- The osteoblast paper (*Bone Rep* 2023) — citation incomplete.
- The WGCNA brain transcriptomics paper (*Brain Sci* 2026;16(2):163) — not retrieved beyond title.
- Sauer et al. *Nature* 2021 NaCT structure — DOI confirmed via nature.com listing, **abstract not directly retrieved**; PMID unknown.

**Could not retrieve (blocked/403):** OMIM 615905 full record, NORD entry, MDPI *Genes* 2022 HTML, Orphanet. Consequently: **Orphanet ORPHA number, ICD-10/ICD-11 codes, MeSH ID, gnomAD carrier frequency, and Orphanet prevalence class are all UNKNOWN** — please look these up rather than inferring them.

**Named-entity-confusion warning:** "Kohlschütter–Tönz syndrome" appears as an informal synonym in community materials, but true KTS is `ROGDI`-associated (`MONDO:0009162`). Any deep-research report on this disease that centers `ROGDI` is describing the wrong entity. Also watch the OMIM number split — **615905 is the phenotype, 608305 is the gene**; Wikipedia's infobox surfaces the gene number, which is an easy trap.

**Ontology terms:** every HP, GO, CL, UBERON, CHEBI, and MAXO term marked ✅ above was verified against the local OAK adapters in this session. Terms without ✅ (HP:0001249, HP:0002069, HP:0011153, HP:0002121, HP:0001266, HP:0001344, HP:0000687, HP:0000668, HP:0000212, HP:0006480, HP:0000007, HP:0033097, and the GO cellular-component terms) are my suggestions from memory and **must be run through `just validate-terms-file` before committing.** Note also: **HPO has no term for elevated citrate** — an OAK search returns only imported CHEBI classes — so model the biochemical signature as a `biochemical` marker with a LOINC binding rather than forcing a phenotype term.

---

## Sources

- [Thevenon et al. 2014, *Am J Hum Genet* — original gene discovery (PMID:24995870)](https://pubmed.ncbi.nlm.nih.gov/24995870/)
- [Hardies et al. 2015, *Brain* — functional confirmation, teeth hypoplasia (PMID:26384929)](https://pubmed.ncbi.nlm.nih.gov/26384929/)
- [Yang et al. 2020, *Child Neurol Open* — epilepsy and EEG phenotype (PMID:32551328)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7281881/)
- [Brown et al. 2021, *Metabolites* — growth and overall health (PMID:34822404)](https://pubmed.ncbi.nlm.nih.gov/34822404/)
- [Goodspeed et al. 2022, *Genes* — from genetics to gene therapy (PMID:36141051)](https://www.mdpi.com/2073-4425/13/9/1655)
- [Spelbrink et al. 2023, *Front Genet* — Ciitizen EHR cohort (PMID:37025451)](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2023.1109547/full)
- [AlQudairy et al. 2023, *Front Pediatr* — Saudi families (PMID:36923948)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10008858/)
- [Brown et al. 2024, *Ther Adv Rare Dis* — research toolbox (PMID:39091896)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11292725/)
- [Jaramillo-Martinez et al. 2024, *J Mol Biol* — Class I/II mutants (PMID:39442909)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11929159/)
- [Sleep Abnormalities in SLC13A5 Citrate Transporter Disorder, *Genes* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11507356/)
- [Ozlu et al. 2025, *Dev Med Child Neurol* — development and QoL (PMID:39710583)](https://pubmed.ncbi.nlm.nih.gov/39710583/)
- [Dogra et al. 2025, *PLoS Biol* — zebrafish, zinc/NMDA hypothesis (PMID:40208862)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12047791/)
- [Ozlu et al. 2026, *Epilepsy Res* — epilepsy phenotype, n=30 (PMID:41442826)](https://pubmed.ncbi.nlm.nih.gov/41442826/)
- [Bailey et al. 2026, *J Clin Invest* — AAV9 gene therapy](https://www.jci.org/articles/view/197503)
- [Nou-Fontanet et al. 2026, *Epileptic Disord* — citrate as diagnostic biomarker](https://onlinelibrary.wiley.com/doi/10.1002/epd2.70178)
- [NCT07102524 — TSHA-105 Phase 1/2 trial](https://clinicaltrials.gov/study/NCT07102524)
- [Sauer et al. 2021, *Nature* — human NaCT structure](https://www.nature.com/articles/s41586-021-03230-x)
- [TESS Research Foundation](https://www.tessresearch.org/understanding-slc13a5/)
- [NORD — SLC13A5 Citrate Transporter Disorder](https://rarediseases.org/rare-diseases/slc13a5-epileptic-encephalopathy/)

---

**TL;DR for the curation entry:** the two things that would be easiest to get wrong here are (1) modeling this as a progressive encephalopathy — it isn't, the EEG and developmental data both say delay-then-plateau with seizures that *improve* after age 10; and (2) collapsing the mechanism into a single chain. There are genuinely two competing causal models — intracellular citrate starvation versus extracellular citrate stealing zinc away from NMDA receptors — and they point at completely different drugs. Curate them as separate `mechanistic_hypotheses` groups. The tooth phenotype is a third, independent branch off the same molecular trigger, and it's the cheapest diagnostic clue anyone will ever get for free.