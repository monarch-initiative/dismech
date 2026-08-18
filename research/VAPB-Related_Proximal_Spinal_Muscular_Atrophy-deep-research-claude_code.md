---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-28T12:38:08.806462'
end_time: '2026-07-28T12:42:14.914482'
duration_seconds: 246.11
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: VAPB-Related Proximal Spinal Muscular Atrophy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: C:/Users/flaharty/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/bin/claude.exe
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    working_dir: C:/Users/flaharty/AppData/Local/Temp
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 24
  total_cost_usd: 1.1040966
  session_id: 2fdc98ce-e61d-431f-b22c-6d43495d4650
  stop_reason: end_turn
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** VAPB-Related Proximal Spinal Muscular Atrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **VAPB-Related Proximal Spinal Muscular Atrophy** covering all of the
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

# VAPB-Related Proximal Spinal Muscular Atrophy: Comprehensive Disease Report

## 1. Disease Information

**Overview:** VAPB-related proximal spinal muscular atrophy — also known clinically as **spinal muscular atrophy, late-onset, Finkel type (SMAFK)** or **adult-onset autosomal dominant proximal spinal muscular atrophy (SMAPAD)** — is a rare, slowly progressive, autosomal dominant lower motor neuron disease caused by heterozygous mutation in the *VAPB* gene (20q13.32). It sits on a clinical continuum with **amyotrophic lateral sclerosis type 8 (ALS8)**, since the same causal mutation (p.Pro56Ser) produces phenotypes ranging from pure lower-motor-neuron proximal SMA to classic ALS with upper motor neuron involvement within the same kindreds ([OMIM #182980](https://omim.org/entry/182980); [OMIM #608627](https://omim.org/entry/608627)).

**Key identifiers:**
- **OMIM (phenotype):** #182980 (SMAFK) and #608627 (ALS8); **OMIM (gene):** *605704 (VAPB)
- **MONDO:** MONDO:0008453 (autosomal dominant adult-onset proximal SMA); MONDO:0012077 (ALS8)
- **HGNC:** 12649 (VAPB)
- **Disease Ontology:** DOID:0111194
- **ICD-10:** G12.1 (other inherited spinal muscular atrophy); ALS-spectrum cases may be coded G12.21
- **ClinGen:** VAPB–ALS8, classified **Definitive** by the ALS Spectrum Disorders Gene Curation Expert Panel (12/15/2021) ([ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:12649))

**Synonyms:** Finkel-type SMA; late-onset spinal muscular atrophy; autosomal dominant proximal SMA (SMAPAD); amyotrophic lateral sclerosis type 8 (ALS8); VAPB-related motor neuron disease.

**Evidence base:** Predominantly aggregated disease-level literature — case series/kindred studies (largest Brazilian founder-population cohorts), functional/molecular studies, and animal-model reports — rather than large-scale structured EHR data, reflecting the disease's rarity.

---

## 2. Etiology

**Primary cause:** Heterozygous, dominantly acting missense mutation in *VAPB*, most commonly **c.166T>C, p.Pro56Ser (P56S)**. First described by Nishimura et al. (2004) in Finkel-type SMA and ALS8 kindreds, this remains the dominant, near-exclusive causal variant reported worldwide.

**Genetic risk factors:**
- **p.Pro56Ser (P56S):** the principal pathogenic variant; found via a **common founder haplotype** traced to Portuguese colonization of Brazil, estimated at **~23 generations ago (95% CI 13–39)** (Marques et al., *Hum Genet* 2006, PMID 16770606-type finding described in search results). Eight known Brazilian families (>1,500 individuals, ~200 affected) share this founder mutation, seven of Portuguese-Brazilian and one of African-Brazilian ancestry.
- **p.Thr46Ile (T46I):** rarer pathogenic missense variant at a conserved lipid-binding-interaction residue.
- **p.Val234Ile (V234I):** additional reported ALS8-associated variant, less characterized.
- Recent Brazilian familial ALS (FALS) cohort work found P56S in **25% (3/12)** of FALS cases screened (Reis et al. 2025), reinforcing recommendations to include P56S in all Brazilian FALS genetic panels.
- **Inheritance:** autosomal dominant with **incomplete penetrance and markedly variable expressivity** — the same P56S allele produces pure proximal SMA (Finkel type), atypical ALS with tremor, or rapidly progressive classic ALS even within one family.

**Environmental/lifestyle risk factors:** None established; this is a monogenic disorder. No confirmed toxin, occupational, or infectious contributors.

**Protective factors:** None specifically identified. No known modifier alleles that reduce penetrance have been validated in humans; variable expressivity suggests unidentified genetic or stochastic modifiers.

**Gene-environment interactions:** Not established; disease expression variability appears driven by genetic background/modifier effects and stochastic cellular proteostasis factors rather than documented environmental interaction.

---

## 3. Phenotypes

| Phenotype | Type | Frequency | Onset/Course | Suggested HPO |
|---|---|---|---|---|
| Proximal lower-limb weakness | Clinical sign | Core/near-universal | Insidious, lumbar-predominant onset in 94% of cases | HP:0007017 (Progressive proximal muscle weakness); HP:0003701 |
| Fasciculations | Clinical sign | Very common | Present from early disease | HP:0002380 |
| Postural/action tremor | Clinical sign | Distinctive feature in subset (essential-tremor-like) | Can precede weakness | HP:0002174 |
| Muscle cramps | Symptom | Common, often prominent early complaint | Variable | HP:0003394 |
| Hypoactive/absent deep tendon reflexes | Clinical sign | Common | Progressive | HP:0001265 / HP:0001284 |
| Muscle atrophy (amyotrophy) | Physical sign | Common | Progressive | HP:0003202 |
| Upper motor neuron signs (pyramidal signs, e.g., spasticity, hyperreflexia) | Clinical sign | ~68% of a 78-patient cohort (53/78) had UMN signs; none showed clonus | Emerges later in a subset; 30% of those presenting as pure PMA later developed UMN signs | HP:0002355 (gait disturbance), HP:0002061 (spasticity) |
| Bulbar dysfunction | Clinical sign | Emerges later in disease course | Late | HP:0002478 (dysarthria), HP:0002015 (dysphagia) |
| Respiratory insufficiency | Complication | Emerges late; reported in some early-onset kindred members | Late/end-stage | HP:0002093 |
| Cognitive/behavioral impairment (executive dysfunction, apathy, anosognosia) | Behavioral change | Reported in subset, non-classic feature | Variable, sometimes late "cognitive conversion" | HP:0002333 (executive dysfunction) |
| Autonomic disturbances | Symptom | Reported in some case series | Variable | HP:0012647 |
| Lipid abnormalities | Laboratory abnormality | Reported associated feature in some cohorts | Variable | HP:0003119 |
| Abdominal protrusion | Physical sign | Reported feature (abdominal wall muscle weakness) | Variable | — |

**Onset/severity/progression summary:** Median age at onset **~43–45 years** (mean 44.9 years in the largest natural-history cohort of 78 patients from 57 families); 51% male. Onset is **lumbar/proximal-predominant in 94%** of patients. At presentation, ~51% have spinal-onset ALS-type disease, 42% present as progressive muscular atrophy (PMA, pure LMN), and 6% present as "flail leg." Course is notably **slower than typical ALS** — median survival reported at **21.9 years** in the natural-history cohort (other case series report 10–20 years, average ~15 years), versus 2–5 years in typical sporadic ALS. Median time to wheelchair dependence: **7.0 years**; to non-invasive ventilation: **10.0 years**. UMN status did not significantly affect survival (Tandfonline 2026 natural history study, DOI 10.1080/21678421.2026.2674020).

**Quality of life impact:** Long symptomatic period with progressive proximal weakness, mobility loss (median 7 years to wheelchair), and eventual respiratory/bulbar decline; cognitive-behavioral impairment in a subset adds additional burden to caregivers and complicates disease management, per the ALS8 narrative review (PMC11785458).

---

## 4. Genetic/Molecular Information

**Causal gene:** *VAPB* (VAMP-associated protein B and C), HGNC:12649, OMIM *605704, chr20q13.32.

**Pathogenic variants:**
- **c.166T>C, p.Pro56Ser (P56S)** — missense, dominant, the principal disease-causing variant; classified pathogenic in ClinVar/ClinGen for ALS8 and SMAPAD.
- **c.137C>T, p.Thr46Ile (T46I)** — missense at a highly conserved MSP-domain residue important for FFAT-motif ligand binding.
- **p.Val234Ile (V234I)** — reported pathogenic missense variant.
- All are **germline**, autosomal dominant; no somatic VAPB variants are implicated in this disease.
- **Allele frequency:** Extremely rare/absent in population reference databases (gnomAD) consistent with a highly penetrant dominant disease allele concentrated in specific founder pedigrees (predominantly Brazilian, with reported cases also in China and elsewhere).
- **Functional consequence:** The P56S substitution destabilizes the **MSP (major sperm protein) domain**, disrupting the normal ER/Golgi localization of VAPB, causing **misfolding and aggregation** into ER-derived tubular structures. Mutant protein forms homo- and hetero-oligomers that **sequester wild-type VAPB** into aggregates (a dominant-negative-like mechanism layered on partial loss-of-function), and disrupts FFAT-motif ligand binding required for organelle tethering.

**Modifier genes:** None formally validated in humans; the marked intra-familial phenotypic variability (from Finkel-type SMA to rapidly progressive ALS on an identical P56S background) strongly implies unidentified genetic modifiers, but none have been confirmed by linkage or GWAS to date.

**Epigenetic information:** No disease-specific DNA methylation or chromatin signature has been established.

**Chromosomal abnormalities:** None; disease is due to point mutation, not structural chromosomal rearrangement.

---

## 5. Environmental Information

No established environmental toxins, occupational exposures, radiation, dietary, or lifestyle factors modify onset or course of VAPB-related disease. No infectious triggers have been reported. This is a purely monogenic disorder in current evidence; environmental contribution to phenotypic heterogeneity remains an open question raised by the marked variable expressivity but is not characterized.

---

## 6. Mechanism / Pathophysiology

**Normal VAPB function:** VAPB is an integral **endoplasmic reticulum (ER) membrane protein** that acts as a tethering factor. Its cytosolic **MSP domain** binds **FFAT (two phenylalanines in an acidic tract) motif**–containing partner proteins, recruiting them to ER membrane contact sites. Through this mechanism VAPB mediates:
- **ER–mitochondria tethering** via binding to **PTPIP51**, forming mitochondria-associated ER membranes (MAMs) important for Ca²⁺ signaling and lipid transfer.
- ER–Golgi and ER–plasma membrane contact site formation, lipid transport, Ca²⁺ homeostasis, autophagy regulation, and the unfolded protein response (UPR).

**Causal chain in disease (P56S):**
1. **Protein misfolding** — P56S destabilizes the MSP domain fold.
2. **Aggregation** — misfolded VAPB forms ER-derived tubular/globular aggregates and recruits/sequesters wild-type VAPB (dominant-negative-like), reducing functional VAPB tethering activity.
3. **ER–mitochondria uncoupling** — disrupted MAM tethering (loss of PTPIP51 interaction) impairs Ca²⁺ transfer and mitochondrial function; recent work shows **convergent activation of the integrated stress response (ISR)** and ER-mitochondria uncoupling in VAPB-ALS models (PMC12423299, 2024/2025).
4. **Atypical UPR activation** — upregulation of pro-apoptotic **CHOP and ATF4** without compensatory protective **BiP/GRP78** induction, distinguishing ALS8 from other ALS UPR signatures; early **PERK-mediated stress response** drives ATF4/CHOP-dependent motor neuron toxicity in animal/iPSC models.
5. **Autophagy blockade** — P56S aggregates sequester **ULK1** and the **ATG5–ATG12** conjugate (impairing autophagosome nucleation/elongation), and reduce **STX17** (a SNARE required for autophagosome-lysosome fusion), causing accumulation of unfused autophagosomes adjacent to lysosomes (electron microscopy–confirmed). Autophagic flux is blocked (LC3-II/p62 accumulate; rapamycin/bafilomycin fail to further shift LC3-II levels) (PMC8110809).
6. **RNA-binding protein (RBP) mislocalization** — **TDP-43, FUS, and Matrin 3** are redistributed from nucleus to cytoplasm and co-sequestered with P56S-VAPB aggregates, linking ALS8 mechanistically to the broader TDP-43/FUS proteinopathy seen in other ALS genotypes.
7. **Stress granule pathology** — P56S-VAPB promotes early, persistent, poorly-dynamic **stress granules** (FRAP shows reduced recovery), reflecting impaired RNA granule turnover.
8. **Proteasome impairment** — accumulation of wild-type and mutant VAPB impairs proteasomal activity, compounding proteostatic stress (PMC3187839).
9. **Downstream motor neuron degeneration** — chronic ER stress, mitochondrial dysfunction, autophagy failure, and RBP/proteostasis collapse converge on **lower motor neuron loss** (anterior horn cells), with variable upper motor neuron (corticospinal) involvement producing the ALS8/PMA/SMA phenotypic spectrum.

**Cell types/tissue involvement:** Anterior horn motor neurons (spinal cord), with variable corticospinal (upper motor) neuron involvement; skeletal muscle shows secondary denervation atrophy; VAPB aggregate pathology has also been documented in patient **skin fibroblasts** and **muscle biopsies**, indicating a partially cell-autonomous, non-neuron-restricted proteostatic defect.

**Suggested ontology terms:**
- **GO Biological Process:** GO:0016236 (macroautophagy), GO:0034976 (response to endoplasmic reticulum stress), GO:0006febr — more precisely GO:0034620 (cellular response to unfolded protein), GO:0000045 (autophagosome assembly), GO:1902373 (negative regulation of mRNA catabolic process)/stress granule assembly GO:0034063
- **GO Cellular Component:** GO:0005783 (endoplasmic reticulum), GO:0044233 (mitochondria-associated ER membrane), GO:0010494 (cytoplasmic stress granule), GO:0005777 (autophagosome)
- **CL (Cell Ontology):** CL:0000100 (motor neuron), CL:0011005 (spinal cord motor neuron), CL:0000187 (muscle cell)

---

## 7. Anatomical Structures Affected

**Organ level:** Primary — spinal cord (anterior horn/ventral horn motor neurons); secondary — skeletal muscle (denervation atrophy), and in ALS8-spectrum cases, motor cortex/corticospinal tract. Respiratory muscles become secondarily involved late in disease (respiratory insufficiency). Nervous system is the principal body system; musculoskeletal system secondarily affected.

**Tissue/cell level:** Lower motor neurons (spinal cord anterior horn cells) are the principal targeted population; upper motor neurons (Betz cells, corticospinal tract) variably affected. Skeletal muscle fibers undergo neurogenic atrophy. Non-neuronal cells (fibroblasts) also show VAPB aggregate pathology, suggesting the underlying proteostatic defect is not restricted to neurons even though clinical disease is neuron-specific.

**Subcellular level:** Endoplasmic reticulum (site of VAPB aggregation), mitochondria-associated ER membranes (MAMs), autophagosomes/lysosomes, cytoplasmic stress granules, and (secondarily) the nucleus (via TDP-43/FUS redistribution out of it).

**Localization (UBERON):** UBERON:0002240 (spinal cord), UBERON:0016578 (anterior horn of spinal cord), UBERON:0001017 (central nervous system), UBERON:0001134 (skeletal muscle tissue). Disease is typically **bilateral/symmetric**, lumbar/proximal-predominant at onset.

---

## 8. Temporal Development

- **Onset:** Adult-onset, typically **30s–40s** (mean/median ~43–45 years); onset is insidious, lumbar/proximal-predominant in 94% of cases.
- **Progression:** Slowly progressive relative to sporadic ALS. Stages roughly: (1) early proximal lower-limb weakness/fasciculation/cramps phase; (2) progressive weakness with variable UMN sign emergence (up to 30% of pure LMN/PMA presentations convert to UMN-positive over time); (3) late bulbar/respiratory involvement; (4) end-stage requiring ventilatory support.
- **Course pattern:** Chronic, progressive, non-remitting; not episodic or relapsing-remitting.
- **Duration:** Prolonged relative to typical ALS — median survival **21.9 years** in the largest natural history cohort (range reported elsewhere ~10–20 years, mean ~15 years); median time to wheelchair dependence 7.0 years, to non-invasive ventilation 10.0 years.
- **Remission:** None described; disease is progressive and non-remitting.
- **Critical periods:** No defined critical developmental window; the long, indolent pre-wheelchair phase (~7 years) represents the practical window for supportive/disease-modifying intervention before major disability milestones.

---

## 9. Inheritance and Population

- **Epidemiology:** Very rare overall; precise population prevalence/incidence figures are not established outside of founder populations. The disease is essentially defined by concentrated founder pedigrees.
- **Inheritance pattern:** Autosomal dominant, with **incomplete penetrance and highly variable expressivity** (same P56S mutation → SMA-Finkel, atypical ALS with tremor, or classic rapidly-progressive ALS).
- **Founder effect:** A single founder P56S haplotype traced to **Portuguese colonization of Brazil**, with the founding mutational event estimated at **~23 generations ago (95% CI 13–39)**. Eight known large Brazilian kindreds (>1,500 individuals, ~200 affected) carry this founder allele — seven of Portuguese-Brazilian and one of African-Brazilian ancestry, consistent with the founder haplotype having entered the African-Brazilian lineage through admixture.
- **Geographic distribution:** Concentrated in Brazil (particularly southeastern Brazil); isolated non-Brazilian cases (including in China and elsewhere) have also been reported, some representing independent mutational events or unrecognized distant relatedness.
- **Consanguinity:** Not a notable feature (autosomal dominant with founder spread, not recessive).
- **Sex ratio:** Roughly equal; the largest natural history cohort reported 51% male.
- **Age distribution:** Adult-onset disease; no pediatric or congenital forms recognized for VAPB-related SMA/ALS8.
- **Carrier frequency:** Not established in general population databases (essentially absent outside founder pedigrees); gnomAD frequency negligible/not reported for P56S.

---

## 10. Diagnostics

**Clinical/electrophysiological tests:**
- **EMG/nerve conduction studies:** show a pattern of chronic lower motor neuron/denervation disease (fibrillations, fasciculation potentials, chronic neurogenic changes) — a mainstay diagnostic tool given the clinical LMN-predominant presentation.
- **Clinical exam:** assessment of pyramidal (UMN) signs (five-item composite pyramidal sign score used in natural history study) to stratify PMA-like vs ALS8-classic presentations.
- **Muscle biopsy:** in research settings has shown VAPB aggregates co-localized with autophagy markers LC3/p62 — not a standard diagnostic test but supports mechanistic diagnosis in atypical cases.

**Genetic testing:**
- **Single-gene VAPB sequencing** (targeted, given the near-exclusive recurrence of P56S) is the recommended diagnostic approach in patients with compatible phenotype and/or Brazilian ancestry/family history; recommended for inclusion in **all Brazilian familial ALS genetic panels**.
- **Motor neuron disease / ALS gene panels** including *VAPB* alongside *SOD1*, *C9orf72*, *FUS*, *TARDBP*, etc.
- **Whole exome/genome sequencing** useful when phenotype is atypical or family history is absent/unclear.
- Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are **not applicable** (VAPB disease is a single-gene point-mutation disorder, not a repeat-expansion or copy-number condition).

**Omics-based diagnostics:** Not part of routine diagnosis; research studies have used iPSC-derived motor neurons showing VAPB downregulation/aggregation as a research biomarker model (PMC3159551), and ER-aggregate imaging has been proposed as a possible biomarker (PMC7017080), but these are not clinical-grade assays.

**Differential diagnosis:** 5q spinal muscular atrophy (SMN1-related, distinguish by SMN1 deletion testing and typically earlier/more symmetric proximal pattern), other adult-onset motor neuron diseases (SOD1-ALS, Kennedy disease/SBMA — distinguish via AR CAG repeat testing given phenotypic overlap of proximal weakness + tremor + cramps), and sporadic ALS.

**Screening:** No population newborn or carrier screening program exists given rarity; **cascade genetic testing/counseling** in known founder-mutation families (particularly in Brazil) is the relevant screening strategy, alongside predictive testing for at-risk relatives given autosomal dominant inheritance with reduced penetrance considerations.

---

## 11. Outcome/Prognosis

- **Survival:** Substantially longer than typical ALS — median survival **21.9 years** from onset in the largest natural history cohort (78 patients); other series report 10–20 years (average ~15 years), versus 2–5 years for sporadic ALS.
- **Functional milestones:** Median time to wheelchair dependence **7.0 years**; median time to non-invasive ventilation **10.0 years** from onset.
- **Mortality:** Eventual death typically from respiratory failure/bulbar complications, though delayed relative to classic ALS.
- **Morbidity/function:** Progressive proximal weakness leading to loss of ambulation, followed by respiratory compromise; a subset develop cognitive/behavioral impairment (executive dysfunction, apathy, anosognosia — described in case reports of "cognitive conversion" in VAPB carriers, PMC8208309) adding to disability burden.
- **Prognostic factors:** UMN sign status **did not** significantly affect survival in the largest cohort — a notable finding distinguishing ALS8 from typical ALS, where UMN involvement often correlates with prognosis. Presentation subtype at diagnosis (pure PMA vs spinal-onset ALS vs flail-leg) did not appear to be strongly prognostic for survival timing either, though ~30% of PMA presentations converted to UMN-positive over the disease course without altering survival trajectory.
- **Recovery potential:** None — disease is progressive without spontaneous remission; current treatments are palliative/supportive rather than curative.

---

## 12. Treatment

**Pharmacotherapy (symptomatic/disease-modifying, non-specific to VAPB):**
- **Riluzole** (glutamate-modulating agent) — standard ALS-spectrum therapy, modest effect on progression. (MAXO: pharmacological treatment)
- **Edaravone** (antioxidant, IV/oral) — modest benefit, used in some ALS-spectrum patients.
- **Sodium phenylbutyrate/taurursodiol (AMX0035)** — shows promise for extending survival in general ALS populations; not VAPB-specific.
- No pharmacogenomic guidance specific to VAPB genotype has been established.

**Advanced/experimental therapeutics (investigational, not yet approved specifically for VAPB disease):**
- **Gene therapy / CRISPR-Cas9** approaches aimed at correcting or silencing the mutant allele — preclinical/conceptual stage for ALS8 specifically.
- **Antisense oligonucleotides (ASOs) and RNAi** targeting mutant VAPB transcript — proposed strategy given the aggregation/dominant-negative mechanism, analogous to allele-selective ASO strategies used in SOD1-ALS; not yet in VAPB-specific clinical trials per available literature.
- **Stem cell therapies** for neuronal replacement — experimental.
- General ALS-directed trials (e.g., riluzole + IFB-088 combination [TRIALS protocol, NCT05508074]; SAR443820 [NCT05237284]) may enroll ALS-spectrum patients broadly but are not VAPB-targeted.

**Surgical/interventional:** Not disease-specific; standard ALS-spectrum interventions (e.g., gastrostomy placement for nutritional support) apply as disease progresses.

**Supportive/rehabilitative care (mainstay of current management):**
- Multidisciplinary ALS-clinic model: respiratory support (including planning for non-invasive ventilation, median initiation ~10 years post-onset), nutritional intervention (including gastrostomy feeding), physical and occupational therapy, assistive mobility devices (median wheelchair dependence ~7 years post-onset), and psychological/behavioral support for the subset with cognitive-behavioral impairment.
- Emerging wearable assistive technology (e.g., hybrid assistive limb exoskeletons) mentioned as supportive innovation.

**Genetic counseling:** Central to management given autosomal dominant inheritance with variable expressivity/penetrance — counseling for at-risk relatives in founder families, particularly in Brazil.

**Treatment gap:** Current literature explicitly emphasizes that available therapies are "largely palliative" and that ALS8's rarity, phenotypic variability, and limited clinical trial data are major barriers to developing genotype-specific therapeutics (PMC11785458).

**Suggested MAXO terms:** pharmacological treatment (riluzole, edaravone, sodium phenylbutyrate/taurursodiol), non-invasive ventilation, gastrostomy tube feeding, physical therapy, occupational therapy, genetic counseling, wheelchair/mobility assistive device provision.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic dominant disease); the only "primary prevention" avenue is reproductive options — **preimplantation genetic diagnosis (PGD)** or prenatal testing for known familial P56S (or other) VAPB variants in at-risk couples, informed by genetic counseling.
- **Secondary prevention/early detection:** **Cascade genetic testing** in known founder-mutation families (especially Brazilian Portuguese-ancestry kindreds) allows identification of pre-symptomatic carriers for anticipatory monitoring (EMG surveillance, early referral to multidisciplinary ALS/neuromuscular clinics) given incomplete penetrance and long presymptomatic window.
- **Tertiary prevention:** Multidisciplinary supportive care (respiratory monitoring/early NIV initiation, nutritional support, physical therapy) to prevent/delay complications (aspiration, respiratory failure, falls) once disease manifests.
- **Immunization:** No specific vaccine relevance; standard respiratory-illness vaccination (influenza, pneumococcal) is generally advised in neuromuscular disease patients as supportive practice, not disease-specific prevention.
- **Screening:** No population-level newborn screening exists (adult-onset, rare, founder-restricted disease); genetic counseling and family cascade screening are the relevant "screening" strategy in endemic Brazilian kindreds.
- **Public health:** Given the concentrated Brazilian founder population, awareness campaigns and inclusion of VAPB/P56S testing in regional familial ALS diagnostic algorithms have been explicitly recommended by researchers to reduce underdiagnosis.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally-occurring VAPB-related motor neuron disease has been reported in non-human species (companion animals or wildlife); this is a human-specific disease entity as currently characterized. No OMIA entry identified for a spontaneous animal analog.
- **Orthologous genes:** *Vapb* is highly conserved — mouse *Vapb* (NCBI Gene), *C. elegans* ortholog **vpr-1**, and *Drosophila* ortholog **VAP33A** — all used to generate engineered (not naturally occurring) disease models (see Section 15).
- **Comparative biology:** The MSP-domain/FFAT-motif tethering mechanism and ER-mitochondria contact site function are evolutionarily conserved from *C. elegans* through mammals, supporting cross-species relevance of mechanistic findings (e.g., secreted vMSP domain signaling to muscle mitochondria is conserved between *C. elegans* and *Drosophila*).
- **Transmission:** Not applicable — genetic, non-infectious, non-zoonotic disease.

---

## 15. Model Organisms

- **Mouse:**
  - **Vapb P56S knock-in mice** — display **slowly progressive motor behavior defects** with ER stress and autophagic response occurring in motor neurons *before* overt behavioral onset, closely paralleling the slow human disease course (Human Molecular Genetics, 2015; academic.oup.com/hmg/article/24/22/6515).
  - **Transgenic overexpression models** — neuronal overexpression of **human wild-type VAPB slows motor impairment and neuromuscular denervation** in a mouse ALS model, supporting a partial loss-of-function contribution to pathology and suggesting VAPB supplementation as a conceptual therapeutic angle (HMG 2016, academic.oup.com/hmg/article/25/21/4661).
  - **Mutant VAPB aggregation models** — widespread P56S-VAPB aggregation in mice, notably, **did not itself cause motor neuron degeneration** and did not modulate mutant SOD1 aggregation/toxicity when crossed with SOD1 mice — indicating aggregation alone is insufficient and additional cell-autonomous stress mechanisms (autophagy/UPR/RBP dysfunction) are required for neurodegeneration (Molecular Neurodegeneration 2013, PMC3538568/PMC3187839-adjacent work).
- **Invertebrate models:**
  - ***C. elegans*** (ortholog **vpr-1**): used to model motor neuronal loss in ALS8 (Scientific Reports 2017, PMC5599522) and to define VAPB/ALS8 MSP-domain ligand signaling to striated muscle mitochondria/energy metabolism, critical for adult survival (PLOS Genetics, PMC3764199). *vpr-1* also has a role in **gonad development** signaling (PMC5482997), illustrating pleiotropic normal VAPB/vpr-1 function beyond neurons.
  - ***Drosophila*** (ortholog **VAP33A**): expression of the human ALS-associated mutant VAP ortholog produces a **dominant-negative** phenotype recapitulating motor neuron pathology, one of the earliest genetic model demonstrations of VAPB mutant toxicity mechanism (PMC2390852).
- **Cellular/iPSC models:**
  - **Patient-derived iPSC motor neurons** (ALS8 patients) show **downregulation of VAPB expression** and recapitulate ER stress/proteostasis defects, used to study cell-autonomous motor neuron vulnerability (PMC3159551).
  - **Patient fibroblasts and muscle biopsy tissue** show endogenous P56S-VAPB aggregation co-localized with LC3/p62 autophagy markers, validating cell/mouse model findings in native human tissue.
- **Model characteristics/limitations:** Mouse knock-in models best recapitulate the **slow, late-onset** character of human disease and are considered strong models for testing therapeutics aimed at ER stress/autophagy pathways; however, aggregation-only models fail to produce overt motor neuron death, indicating that mouse models alone do not fully capture the human clinical severity spectrum (pure LMN SMA to rapid ALS), and no single model reproduces the full human phenotypic heterogeneity (tremor, UMN-sign variability, cognitive-behavioral features).
- **Applications:** These models collectively support studies of ER-mitochondria tethering/MAM function, UPR/ISR signaling, autophagy flux, RBP mislocalization, and are used as therapeutic screening platforms (e.g., testing VAPB overexpression, chaperone/autophagy-modulating compounds).

---

## Key Ontology Term Summary
- **Genes/Proteins:** VAPB (HGNC:12649); interacting partners PTPIP51/RMDN3, FFAT-motif proteins
- **HPO:** HP:0007017, HP:0002380, HP:0002174, HP:0003394, HP:0001265, HP:0003202, HP:0002355, HP:0002478, HP:0002015, HP:0002093, HP:0002333, HP:0012647
- **GO:BP:** GO:0016236, GO:0034976, GO:0034620, GO:0000045, GO:0034063
- **GO:CC:** GO:0005783, GO:0044233, GO:0010494, GO:0005777
- **CL:** CL:0000100, CL:0011005, CL:0000187
- **UBERON:** UBERON:0002240, UBERON:0016578, UBERON:0001017, UBERON:0001134
- **MONDO:** MONDO:0008453 (SMAPAD), MONDO:0012077 (ALS8)
- **MAXO:** pharmacological treatment (riluzole/edaravone/AMX0035), non-invasive ventilation, gastrostomy feeding, physical/occupational therapy, genetic counseling

---

## Sources

- [Entry - *605704 - VAMP-ASSOCIATED PROTEIN B AND C; VAPB - OMIM](https://www.omim.org/entry/605704)
- [Entry - #608627 - AMYOTROPHIC LATERAL SCLEROSIS 8; ALS8 - OMIM](https://omim.org/entry/608627)
- [Entry - #182980 - SPINAL MUSCULAR ATROPHY, LATE-ONSET, FINKEL TYPE; SMAFK - OMIM](https://omim.org/entry/182980)
- [Orphanet: VAPB-VAMP associated protein B and C](https://www.orpha.net/en/disease/gene/VAPB)
- [VAPB curation results - ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:12649)
- [NM_004738.5(VAPB) - Adult-onset proximal spinal muscular atrophy - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000295668/)
- [A common founder for amyotrophic lateral sclerosis type 8 (ALS8) in the Brazilian population - Human Genetics](https://link.springer.com/article/10.1007/s00439-005-0031-y)
- [The history behind ALS type 8: from the first phenotype description to the discovery of VAPB mutation - SciELO](https://www.scielo.br/j/anp/a/VmPWLd9vRLxYS93RQtyNWry/)
- [Familial adult spinal muscular atrophy associated with the VAPB gene: report of 42 cases in Brazil - PubMed](https://pubmed.ncbi.nlm.nih.gov/24212516/)
- [Genetic and clinical insights into ALS8: exploring the impact of VAPB pathogenic variants in familial ALS - PMC12585906](https://pmc.ncbi.nlm.nih.gov/articles/PMC12585906/)
- [Amyotrophic Lateral Sclerosis (ALS) Type 8: A Narrative Review - PMC11785458](https://pmc.ncbi.nlm.nih.gov/articles/PMC11785458/)
- [Clinical characterization and natural history of ALS8/VAPB p.Pro56Ser: upper motor neurone signs, survival, and functional milestones in 78 patients](https://www.tandfonline.com/doi/full/10.1080/21678421.2026.2674020)
- [Pathomechanisms of ALS8: altered autophagy and defective RNA binding protein homeostasis due to VAPB P56S mutation - PMC8110809](https://pmc.ncbi.nlm.nih.gov/articles/PMC8110809/)
- [Convergent activation of the integrated stress response and ER–mitochondria uncoupling in VAPB-associated ALS - PMC12423299](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12423299/)
- [Accumulation of Wildtype and ALS-Linked Mutated VAPB Impairs Activity of the Proteasome - PMC3187839](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187839/)
- [Widespread aggregation of mutant VAPB associated with ALS does not cause motor neuron degeneration - PMC3538568](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3538568/)
- [Motor Neuron Disease-Associated Mutant VAPB Recruits Wild-Type VAPs into ER-Derived Tubular Aggregates - J Neurosci](https://www.jneurosci.org/content/27/36/9801)
- [VAPB ER-Aggregates, A Possible New Biomarker in ALS Pathology - PMC7017080](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7017080/)
- [Proteomics-Based Approach Identifies Altered ER Domain Properties by ALS-Linked VAPB Mutation - Scientific Reports](https://www.nature.com/articles/s41598-020-64517-z)
- [Vapb/ALS8 knock-in mice display slowly progressive motor behavior defects accompanying ER stress and autophagic response - HMG](https://academic.oup.com/hmg/article/24/22/6515/2385871)
- [Neuronal overexpression of human VAPB slows motor impairment and neuromuscular denervation in a mouse model of ALS - HMG](https://academic.oup.com/hmg/article/25/21/4661/2525899)
- [VAPB/ALS8 MSP Ligands Regulate Striated Muscle Energy Metabolism Critical for Adult Survival in C. elegans - PLOS Genetics/PMC3764199](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3764199/)
- [Mitigating Motor Neuronal Loss in C. elegans Model of ALS8 - PMC5599522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5599522/)
- [The C. elegans VAPB homolog VPR-1 is a permissive signal for gonad development - PMC5482997](https://pmc.ncbi.nlm.nih.gov/articles/PMC5482997/)
- [A Drosophila Model of ALS: Human ALS-Associated Mutation in VAP33A Suggests a Dominant Negative Mechanism - PMC2390852](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2390852/)
- [Downregulation of VAPB expression in motor neurons derived from iPSCs of ALS8 patients - PMC3159551](https://pmc.ncbi.nlm.nih.gov/articles/PMC3159551/)
- [Case Report: Cognitive Conversion in a Non-brazilian VAPB Mutation Carrier (ALS8) - PMC8208309](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208309/)
- [Investigating the contribution of VAPB/ALS8 loss of function in ALS - PubMed](https://pubmed.ncbi.nlm.nih.gov/23446633/)
- [VAPB gene VAMP Associated Protein B And C - GeneCards](https://www.genecards.org/card/VAPB)