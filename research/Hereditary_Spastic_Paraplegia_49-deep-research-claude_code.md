---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T14:11:17.094831'
end_time: '2026-08-27T14:15:26.309045'
duration_seconds: 249.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Spastic Paraplegia 49
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
  web_search_requests: 15
  num_turns: 20
  total_cost_usd: 1.2626286000000002
  session_id: 98b3127c-432a-57dc-acc9-774218ba8a79
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 10
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 49
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 49** covering all of the
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

I'll research Hereditary Spastic Paraplegia 49 (SPG49/TECPR2-related) now using web search and fetch tools to gather current, citable information.

# Hereditary Spastic Paraplegia 49 (SPG49) / TECPR2-Related Disorder — Comprehensive Research Report

## 1. Disease Information

**Overview.** Hereditary Spastic Paraplegia 49 (SPG49) is an ultra-rare, autosomal recessive, complex neurodevelopmental and neurodegenerative disorder caused by biallelic loss-of-function variants in **TECPR2** (tectonin beta-propeller repeat containing 2), a gene on chromosome 14q32.31 that regulates autophagosome–lysosome fusion and, separately, COPII-dependent ER export. It was first described in 2012 in five Bukharian Jewish patients as an autosomal-recessive complicated hereditary spastic paraplegia ([Oz-Levi et al. 2012, *Am J Hum Genet*, PMID:23176824](https://www.sciencedirect.com/science/article/pii/S000292971200523X)). Subsequent characterization of larger cohorts showed the phenotype is broader than isolated spasticity — a multisystem sensory, autonomic, and developmental disorder — leading to reclassification as **Hereditary Sensory and Autonomic Neuropathy type IX (HSAN9)**, sometimes written "TECPR2-related HSAN with intellectual disability." Both names (SPG49 and HSAN9) are used interchangeably in the literature and databases for the same gene-disease pair.

**Key identifiers:**
- **OMIM disease**: #615031, *Spastic Paraplegia 49, Autosomal Recessive*; **OMIM gene**: *615000, TECPR2* ([OMIM](https://www.omim.org/entry/615000))
- **MONDO**: MONDO:0014016
- **Orphanet**: ORPHA:320385, *Hereditary sensory and autonomic neuropathy due to TECPR2 mutation* ([Orphanet](https://www.orpha.net/en/disease/detail/320385))
- **ICD-10**: G11.4 (hereditary spastic paraplegia); relatedly G60.- for hereditary/idiopathic neuropathy
- **Gene**: TECPR2; HGNC:19957 (note: some secondary sources list HGNC:30346 — HGNC:19957 is the authoritative current ID); UniProt O15040; NCBI Gene ID 9895
- **GeneReviews**: "TECPR2-Related Hereditary Sensory and Autonomic Neuropathy with Intellectual Disability" ([NBK584409](https://www.ncbi.nlm.nih.gov/books/NBK584409/))
- **MedGen**: C3542549

**Synonyms/alternative names:** Spastic paraplegia 49, autosomal recessive; SPG49; Hereditary sensory and autonomic neuropathy type IX (HSAN9); HSAN9 with developmental delay; TECPR2-related neurodevelopmental disorder; complicated autosomal-recessive HSP with TECPR2 mutation.

**Source of information.** Nearly all clinical characterization derives from **aggregated disease-level resources** — case series and cohort reports pooled by international collaborators — rather than large EHR datasets, reflecting the disorder's ultra-rarity (>30–40 reported individuals worldwide as of the most recent cohort study).

---

## 2. Etiology

**Disease causal factor:** SPG49/HSAN9 is a **purely monogenic, autosomal-recessive Mendelian disorder**. There is no described environmental, infectious, or multifactorial contribution to primary disease causation — all reported cases carry biallelic pathogenic *TECPR2* variants.

**Genetic risk factors:**
- **Causal variants**: biallelic (homozygous or compound heterozygous) loss-of-function variants in *TECPR2* — nonsense, frameshift, canonical splice-site, and a smaller fraction of missense variants clustered in the N-terminal WD/beta-propeller and C-terminal TECPR-repeat domains ([Neuser et al. 2021, *Hum Mutat*, PMID:33847017](https://pubmed.ncbi.nlm.nih.gov/33847017/)).
- **Population founder variants** (act as genetic risk factors in specific ancestries — see §9):
  - Bukharian Jewish: c.3416delT, p.Leu1139ArgfsTer75 (original founder allele; PMID:23176824)
  - Ashkenazi Jewish: c.1319delT, p.Leu440ArgfsTer19 (PMID:26542466, Heimer et al. 2016)
- **Heterozygous (monoallelic) TECPR2 variants** have separately been reported to cause a distinct, milder, presumably dominant-negative or haploinsufficiency phenotype of progressive cerebellar atrophy with global developmental delay — genetically and mechanistically distinct from the classic biallelic HSAN9/SPG49 syndrome ([Ramsey et al. 2022, *Mol Genet Genomic Med*, PMID:34994087](https://pmc.ncbi.nlm.nih.gov/articles/PMC8830808/)).
- No modifier genes have been formally established, though phenotypic variability among individuals homozygous for the same founder allele is documented.

**Environmental risk factors:** None identified as causal; secondary environmental risk factors (e.g., aspiration risk from dysphagia, hypoventilation exacerbated by sedatives) act on disease *complications* rather than disease initiation (see §12, drugs to avoid).

**Protective factors:** None described in the literature; this is a fully penetrant recessive loss-of-function disorder with no known protective alleles or environmental modifiers.

**Gene-environment interactions:** Not applicable/not reported — the disorder is monogenic with no established GxE interaction.

---

## 3. Phenotypes

Frequencies below are drawn from the largest published cohort (28 individuals: 17 new + 11 previously reported; Neuser et al. 2021, PMID:33847017) and GeneReviews (NBK584409).

**Developmental/cognitive:**
- Global developmental delay / intellectual disability — **100%** (universal; often severe, many nonverbal) — HP:0001263 (Developmental delay), HP:0001249 (Intellectual disability)
- Speech delay, frequently absent expressive speech — HP:0000750 (Delayed speech and language development)
- Behavioral abnormalities (autism-spectrum features, stereotypies) — **~62.5%** — HP:0000708 (Behavioral abnormality)

**Neurological/motor:**
- Muscular hypotonia (infantile onset) — **100%** — HP:0001252 (Hypotonia)
- Gait ataxia — **100%** — HP:0002066 (Gait ataxia)
- Spastic paraparesis/lower-limb spasticity (emerging later, in childhood/adolescence) — HP:0001258 (Spasticity), HP:0007256 (Progressive spasticity)
- Lower-limb hypo/areflexia — **~85%** — HP:0002522 (Areflexia)
- Dysarthria — **~87.5%** — HP:0001260 (Dysarthria)
- Decreased pain and temperature sensitivity — **~50%** — HP:0002829 (Impaired pain sensation)
- Dystonia and Parkinsonian features can emerge in late childhood/adolescence — HP:0001332 (Dystonia)

**Autonomic:**
- Central hypoventilation/apnea (nocturnal) — **~82%** — HP:0004926 (Central sleep apnea)
- Gastroesophageal reflux disease — **~94%** — HP:0002020 (Gastroesophageal reflux)
- Dysphagia — **~53%**; recurrent aspiration — **~71%** — HP:0002015 (Dysphagia), HP:0002835 (Recurrent aspiration pneumonia)
- Gastrointestinal dysmotility — HP:0002579 (Intestinal pseudo-obstruction/dysmotility spectrum)

**Dysmorphic/growth:**
- Mild brachycephalic microcephaly — **~59%** — HP:0000252 (Microcephaly), HP:0000248 (Brachycephaly)
- Short stature — **~58%** — HP:0004322
- Short/broad neck, low anterior hairline, retrocollis posture — **~52%** — HP:0000470 (Short neck)
- Coarse facial features — HP:0000280

**Onset/severity/progression characteristics:**
- **Age of onset**: infancy (motor delay, hypotonia typically noted in the first year)
- **Severity**: variable but generally severe; most patients never achieve independent ambulation or full expressive speech
- **Progression**: progressive/neurodegenerative course — possible regression in the second decade with loss of previously acquired ambulation; not static like cerebral palsy
- **Course pattern**: chronic progressive, punctuated by acute respiratory/aspiration crises

**Quality-of-life impact:** Severe — near-universal loss of independent mobility and communication, lifelong dependence for feeding (often gastrostomy) and respiratory support (noninvasive ventilation), and premature mortality (see §11). No formal EQ-5D/SF-36 studies exist for this ultra-rare disorder; QoL data are qualitative, from natural-history/clinical cohort descriptions.

---

## 4. Genetic/Molecular Information

**Causal gene:** *TECPR2* (Tectonin Beta-Propeller Repeat Containing 2), chr14q32.31; OMIM *615000; HGNC:19957; NCBI Gene 9895; Ensembl ENSG00000122986; UniProt O15040 ([GeneCards](https://www.genecards.org/card/TECPR2); [UniProt](https://www.uniprot.org/uniprotkb/O15040/entry)).

**Variant classes (ClinVar/GeneReviews):** predominantly **frameshift, nonsense, and canonical splice-site variants** producing a truncated/degraded protein (loss-of-function mechanism); a substantial minority (~half of reported alleles) are **missense variants**, clustering in the N-terminal WD/beta-propeller domain and the C-terminal six-TECPR-repeat domain — but ACMG/AMP classification of these missense alleles remains challenging due to limited functional-assay throughput (PMID:33847017). Sequence analysis (panel/exome/genome) detects essentially all reported pathogenic variants; larger structural deletions/duplications are rare but should be tested if sequencing is negative.

**Representative pathogenic variants:**
- c.3416delT, p.Leu1139ArgfsTer75 — Bukharian Jewish founder (PMID:23176824)
- c.1319delT, p.Leu440ArgfsTer19 — Ashkenazi Jewish founder (PMID:26542466), later used as the target of a splice-modulating antisense oligonucleotide (see §12)
- c.2578+2T>C (splice donor variant) — reported in ClinVar for HSP49
- c.2599G>T, p.Glu867Ter — nonsense variant (ClinVar)
- Additional missense and truncating alleles reported in a Chinese patient ([PMID:35130874](https://pubmed.ncbi.nlm.nih.gov/35130874/)) and other worldwide cases, confirming genetic heterogeneity beyond the two founder populations.

**Allele frequency in population databases:** *TECPR2* is a loss-of-function-intolerant gene in gnomAD (constrained; specific LOEUF/pLI value not independently confirmed in this search but the gene shows depletion of predicted-LoF variants consistent with recessive-disease constraint). Carrier frequency estimates from founder populations: **~1.33% in Bukharian Jews**, **≥0.65% in Ashkenazi Jews** (GeneReviews NBK584409). Estimated disease incidence ranges from ~1:22,500 in the Bukharian Jewish population to ~1:5,961,640 in the general population.

**Somatic vs. germline:** All reported variants are **germline**; there is no somatic/mosaic or cancer association.

**Functional consequence:** **Loss of function** predominates — nonsense/frameshift alleles cause nonsense-mediated decay or produce a truncated, non-functional protein; missense alleles are hypothesized to destabilize the WD/beta-propeller or TECPR domains. No gain-of-function or dominant-negative mechanism has been established for the classic biallelic disease, though the separately-described **heterozygous cerebellar-atrophy phenotype** (PMID:34994087) raises the possibility of haploinsufficiency or dominant-negative effects for a subset of heterozygous variants.

**Modifier genes:** None formally established.

**Epigenetic information:** No disease-specific DNA methylation, histone modification, or chromatin studies have been reported for TECPR2-related disease.

**Chromosomal abnormalities:** Not a contiguous-gene/CNV disorder in the classic sense; disease is driven by point mutations/small indels within *TECPR2*, not large chromosomal rearrangements (though large deletion/duplication testing is part of the standard diagnostic algorithm when sequencing is uninformative).

---

## 5. Environmental Information

No environmental toxins, occupational exposures, radiation, or lifestyle factors are implicated in causing SPG49/HSAN9 — it is a fully penetrant monogenic recessive disorder. No infectious triggers or pathogens are causally implicated (though recurrent respiratory infections/pneumonia are a major **complication**, not a cause, driven by aspiration secondary to dysphagia and hypotonia). No CTD/TOXNET or CDC/WHO environmental-exposure signal was identified for this gene-disease pair.

---

## 6. Mechanism / Pathophysiology

**Core molecular lesion — autophagosome–lysosome fusion defect.** TECPR2 is a large multidomain protein: an N-terminal WD/beta-propeller domain, a middle unstructured region, and a C-terminal domain of six TECPR repeats followed by an LC3-interacting region (LIR) motif. TECPR2 was identified as a human **ATG8-family (LC3) interactor** and **positive regulator of autophagy**, functioning specifically in **targeting of autophagosomes to lysosomes** via its C-terminal TECPR domain (UniProt O15040; PMID:23176824). Loss of TECPR2 causes decreased levels of autophagy markers SQSTM1/p62 and lipidated LC3-II in patient fibroblasts, and — in mouse and dog models — **progressive, age-dependent accumulation of undegraded autophagosomes** in neurons.

**Second, distinct mechanism — ER exit site (ERES)/COPII secretory defect.** TECPR2 also cooperates with the ATG8-family protein **LC3C** to regulate **COPII-dependent ER export**: it associates with the COPII coat protein SEC24D, stabilizing SEC24D levels and maintaining functional ER exit sites; TECPR2-deficient patient cells show altered SEC24D abundance and impaired ER export efficiency ([Stadel et al. 2015, *Mol Cell*, PMID:26431026](https://pubmed.ncbi.nlm.nih.gov/26431026/); confirmed and extended by spatial proteomics in [Nature Communications 2023](https://www.nature.com/articles/s41467-023-36553-6)). This links TECPR2 loss to a broader **secretory-pathway disturbance**, not autophagy alone.

**Endolysosomal maturation defect (most recent mechanistic advance, 2025).** A newly published TECPR2 nonsense knock-in mouse model shows that TECPR2 interacts with the **HOPS (homotypic fusion and protein sorting) tethering complex** through its middle region and TECPR domain, and that loss of TECPR2 produces a broader **dysfunctional endolysosomal system** in both neurons and microglia — not merely blocked autophagosome-lysosome fusion. Affected axons accumulate swollen mitochondria, enlarged ER, autophagosomes, glycogen granules, and protein aggregates; microglia adopt a disease-associated phenotype with enlarged lysosomes but *reduced* capacity to clear neuronal debris, implicating impaired neuroimmune clearance in disease progression ([Cell Death & Disease, 2025, PMID:41173829, DOI:10.1038/s41419-025-08168-w]).

**Causal chain (upstream → downstream):**
1. Biallelic LoF *TECPR2* variants → loss of TECPR domain-mediated autophagosome-lysosome tethering and SEC24D/COPII stabilization (molecular)
2. → Impaired autophagic flux (LC3-II/p62 dysregulation) + impaired ER export/secretory pathway function + impaired HOPS-mediated endolysosomal maturation (cellular)
3. → Progressive accumulation of undegraded autophagosomes, protein aggregates, and organellar damage (swollen mitochondria, enlarged ER) selectively in **long axons** of sensory/autonomic pathways — particularly the dorsal column nuclei (gracile and cuneate nuclei) and corticospinal tracts (tissue/cellular)
4. → **Neuroaxonal dystrophy** with axonal spheroid formation, age-dependent neurodegeneration, and secondary microglial dysfunction/disease-associated gliosis that fails to clear debris (tissue)
5. → Clinical phenotype: progressive spastic-ataxic gait disorder, sensory neuropathy, autonomic dysfunction (central hypoventilation, dysmotility), developmental delay, and premature death from respiratory/aspiration complications (organism level)

**Suggested ontology terms:**
- GO (biological process): GO:0000045 (autophagosome assembly), GO:0000422 (autophagy of mitochondrion / mitophagy), GO:0016237 (lysosomal microautophagy) — most specifically **GO:0061908** (autophagosome-lysosome fusion, note: verify exact ID against OAK) or the closest reachable macroautophagy child term; GO:0048208 (COPII vesicle coating); GO:0006888 (ER to Golgi vesicle-mediated transport)
- GO (cellular component): GO:0005776 (autophagosome), GO:0005764 (lysosome), GO:0070081 (ER exit site — verify against OAK), GO:0030904 (HOPS complex if bindable)
- CL (cell type): CL:0000540 (neuron), CL:0000031 (central nervous system neuron — sensory dorsal-column neuron), CL:0000129 (microglial cell)
- UBERON: UBERON:0002771 (nucleus gracilis / dorsal column nuclei — verify exact term), UBERON:0002298 (dorsal column of spinal cord), UBERON:0001851 (corticospinal tract)

**Immune involvement:** Secondary — disease-associated microglial activation with impaired debris clearance (2025 knock-in mouse data), not primary autoimmunity.

**Molecular profiling data available:** Spatial proteomics of the secretory pathway in TECPR2-deficient cells (Nature Communications 2023); transcriptomic/proteomic/electron-microscopy characterization of the 2025 knock-in mouse model. No published human transcriptomic/GEO datasets specific to patient tissue were identified in this search.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary**: central and peripheral nervous system (brain, spinal cord — especially dorsal columns/gracile and cuneate nuclei, corticospinal tracts, cerebellum), autonomic nervous system
- **Secondary**: respiratory system (recurrent aspiration pneumonia, chronic lung disease from hypoventilation), gastrointestinal tract (dysmotility, reflux)
- **Body systems**: nervous system (primary), respiratory system, digestive system, musculoskeletal system (contractures secondary to spasticity)

**Tissue/cell level:**
- Long-tract sensory and motor axons (corticospinal tract, dorsal column pathways) — the primary site of neuroaxonal dystrophy
- Cerebellum — progressive cerebellar atrophy (particularly documented in the heterozygous phenotype, PMID:34994087, and as an MRI feature in some biallelic patients)
- Microglia — CNS resident immune cells implicated in the 2025 mechanistic model
- Cell Ontology: CL:0000540 (neuron), CL:0000129 (microglial cell), CL:11000015 (or nearest CL term for dorsal column/gracile nucleus neuron)

**Subcellular level:** autophagosomes (GO:0005776), lysosomes (GO:0005764), ER exit sites/COPII vesicles (GO:0070081), mitochondria (swollen/dysmorphic in affected axons per 2025 model)

**Localization/lateralization:** Bilateral, symmetric involvement — consistent with a metabolic/degenerative rather than focal-lesion process. Neuroimaging shows thin/dysplastic corpus callosum (~52% in the Neuser 2021 cohort), mild ventriculomegaly, delayed myelination, and cerebral/cerebellar atrophy.

---

## 8. Temporal Development

- **Onset**: Infancy — hypotonia and motor developmental delay are typically the presenting features, with delayed acquisition of independent walking (insidious, not acute onset).
- **Progression**: Neurodegenerative and progressive rather than static. Course: hypotonia in infancy → spastic-ataxic gait pattern emerging in childhood → possible **regression in the second decade** with loss of previously achieved independent ambulation → lower-limb spasticity, dystonia, and Parkinsonian features can emerge in late childhood/adolescence.
- **Disease stages**: no formal staging system exists (unlike cancer); natural-history descriptions divide the course into early developmental-delay phase, a plateau/functional phase, and a later regressive phase.
- **Rate**: variable but generally described as slowly-to-moderately progressive over years to a decade or more.
- **Duration/outcome**: chronic, lifelong, generally fatal in childhood/adolescence (see §11).
- **Remission**: none described — this is a monogenic neurodegenerative disorder without a relapsing-remitting pattern.
- **Critical periods**: early intervention (physical/occupational/speech therapy, early respiratory and nutritional surveillance) is emphasized in management guidance, though no data show a defined "window" that alters the underlying neurodegenerative trajectory.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence**: <1 per 1,000,000 (Orphanet ORPHA:320385) — an ultra-rare disease with >30–40 reported affected individuals in the literature to date.
- **Incidence estimates**: ~1:22,500 in the Bukharian Jewish population vs. ~1:5,961,640 in the general population (GeneReviews NBK584409), reflecting the founder-effect concentration of disease in specific communities.

**Inheritance pattern:** **Autosomal recessive** for the classic biallelic SPG49/HSAN9 phenotype. A separately reported **heterozygous** (monoallelic) TECPR2 variant phenotype causes progressive cerebellar atrophy with developmental delay — a milder, likely dominantly-acting or haploinsufficient presentation, genetically distinct from the recessive syndrome (PMID:34994087).

**Penetrance:** Complete/full penetrance reported for biallelic pathogenic variants (all identified biallelic carriers to date are symptomatic); carriers of a single pathogenic allele in the recessive form are asymptomatic.

**Expressivity:** Variable — even individuals homozygous for the same founder allele show a range of severity in developmental, respiratory, and orthopedic manifestations.

**Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed.

**Founder effects (population-specific mutations):**
- **Bukharian Jewish**: c.3416delT, p.Leu1139ArgfsTer75 — carrier frequency ~1.33%
- **Ashkenazi Jewish**: c.1319delT, p.Leu440ArgfsTer19 — carrier frequency ≥0.65%

**Consanguinity:** A substantial contributor — approximately half of affected individuals are born to consanguineous parents (GeneReviews), consistent with an autosomal recessive ultra-rare disease outside the two known founder populations.

**Carrier frequency:** See founder effects above; carrier screening panels for Ashkenazi and Bukharian Jewish populations increasingly include TECPR2.

**Affected populations / geographic distribution:** Original description in Bukharian Jewish families (Israel/Central Asian Jewish diaspora); Ashkenazi Jewish founder variant subsequently described; sporadic cases reported worldwide including a Chinese patient (PMID:35130874) and other non-founder populations reported in the 2021 international cohort (PMID:33847017), indicating global but very low-frequency occurrence outside founder populations.

**Sex ratio:** No sex predilection reported (autosomal gene).

**Age distribution:** Pediatric-onset disease; the affected population by definition skews toward children and adolescents given reduced life expectancy.

---

## 10. Diagnostics

**Establishing the diagnosis** requires identification of **biallelic pathogenic/likely pathogenic *TECPR2* variants** in an individual with the compatible phenotype (GeneReviews NBK584409).

**Molecular/genetic testing approaches:**
- **Targeted founder-variant testing** — first-line in Ashkenazi or Bukharian Jewish ancestry (c.1319delT / c.3416delT)
- **Multigene panels** for hereditary spastic paraplegia or hereditary sensory/autonomic neuropathy
- **Exome or genome sequencing** — comprehensive approach for non-founder-population or panel-negative cases; sequence analysis detects an estimated ~100% of reported pathogenic variant types (missense, nonsense, splice-site, small indels)
- **Deletion/duplication (CNV) analysis** — reserved for cases where sequencing is uninformative, since large structural variants are rare in this gene

**Neuroimaging (MRI) findings supporting diagnosis:** thin/dysplastic corpus callosum (~52%), mild ventriculomegaly, delayed myelination, cerebral and/or cerebellar atrophy, flattening of the pons (particularly noted in the heterozygous cerebellar-atrophy phenotype, PMID:34994087).

**Clinical/biochemical testing:** No specific validated biomarker or enzyme assay exists; diagnosis is clinical + molecular. Research-grade autophagy-flux assays (LC3-II, p62 immunoblotting in patient fibroblasts) were used investigationally in the original description but are not a standard diagnostic test.

**Differential diagnosis** (per GeneReviews):
- **HSAN3** (familial dysautonomia, *ELP1*/*IKBKAP*) — usually milder intellectual disability; distinguishing features include alacrima and decreased fungiform tongue papillae
- **HSAN4** (*NTRK1*) — painless deformities and anhidrosis with episodic fevers
- **HSAN5** (*NGF*) — painless deformities; borderline/mild intellectual disability
- **Cerebral palsy** — excluded by absence of perinatal risk factors and by the **progressive** course of SPG49/HSAN9 versus the static course of CP
- Other complex/AR hereditary spastic paraplegias in the broader SPG differential

**Screening:** No population newborn-screening program exists (ultra-rare disease); however, targeted **carrier screening** for the Ashkenazi and Bukharian Jewish founder variants is increasingly incorporated into expanded Jewish genetic disease panels, and **prenatal/preimplantation genetic testing** is available once familial variants are identified.

---

## 11. Outcome/Prognosis

**Prognosis is poor.** GeneReviews explicitly notes "reduced life expectancy," with **deaths occurring in the first or second decade of life** in a substantial proportion of reported cases.

**Leading causes of mortality:**
- Asphyxia from aspiration of solid foods
- Nocturnal central apnea
- Complications of chronic, progressive lung disease (recurrent aspiration pneumonia, respiratory failure)

**Morbidity/functional outcomes:**
- Progressive loss of independent ambulation (many patients regress and lose walking ability in the second decade)
- Persistent severe intellectual disability; many individuals remain nonverbal lifelong
- Chronic respiratory disease requiring long-term noninvasive ventilation in a majority of patients
- Feeding dependence (gastrostomy) common given the high rates of dysphagia (53%) and reflux (94%)
- Orthopedic complications (contractures) from progressive spasticity

**Recovery potential:** None — this is a progressive neurodegenerative disorder; there is no reported spontaneous improvement, and no disease-modifying therapy currently exists to alter the trajectory (see §12).

**Prognostic factors:** No formal validated prognostic scoring system exists; qualitatively, earlier/more severe respiratory and bulbar (dysphagia) involvement correlates with worse outcomes, consistent with the mortality causes above.

---

## 12. Treatment

**No curative or disease-modifying therapy is currently approved.** Management is entirely **supportive and multidisciplinary** (GeneReviews NBK584409):

- **Respiratory**: polysomnography for central hypoventilation/apnea surveillance, noninvasive ventilation, oxygen monitoring — NCIT:C15747 (Supportive Care); relevant NCIT concept for noninvasive ventilation/respiratory support
- **Gastroenterology/nutrition**: swallow evaluation, feeding adaptations, consideration of gastrostomy, reflux management — NCIT:C15447 (Dietary Intervention); NCIT:C15986 (Pharmacotherapy, for anti-reflux medication such as proton-pump inhibitors)
- **Orthopedic/rehabilitative**: bracing, physical therapy to prevent contractures — NCIT:C15302 (Physical Therapy), NCIT:C16186 (Orthopedic Surgical Procedure)
- **Behavioral**: applied behavior analysis for autism-spectrum features — NCIT:C181743 (Behavioral Counseling) or nearest behavioral-intervention term
- **Developmental**: early intervention services, special education, speech-language pathology — NCIT:C159273 (Speech Therapy)
- **Genetic counseling**: NCIT:C15240 (Genetic Counseling), given autosomal recessive inheritance and available carrier/prenatal testing

**Drugs to avoid:** Benzodiazepines and antihistamines are explicitly flagged because they risk decreased consciousness, hypopnea, and CO₂ retention in a population already prone to central hypoventilation.

**Experimental/investigational therapy — antisense oligonucleotide (ASO) exon-skipping:**
A 2022 study developed an **ASO exon-skipping strategy** targeting the Ashkenazi founder variant TECPR2 c.1319delT (p.Leu440Argfs*19), which causes a premature stop codon within exon 8 ([Molecular Therapy Nucleic Acids, PMID:35860385](https://pubmed.ncbi.nlm.nih.gov/35860385/)):
- Patient-derived fibroblasts and iPSC-derived neurons homozygous for this variant were used as disease models, both showing complete absence of TECPR2 protein.
- Lead candidate **ASO-005-02** achieved ~27 nM potency in patient fibroblasts, inducing skipping of exon 8 to restore an in-frame, partially functional TECPR2ΔEx8 protein that retained the characteristic punctate neuronal localization of wild-type TECPR2 in iPSC-derived neurons.
- In vivo testing in cynomolgus monkeys (single 20 mg intrathecal dose) showed an acceptable tolerability profile with broad CNS distribution and confirmed exon-8 skipping across multiple CNS tissues — representing a preclinical proof-of-concept for a **precision, genotype-specific splice-modulation therapy** (therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE; aso_mechanism: SPLICE_MODULATION_EXON_SKIPPING; target_gene: TECPR2 (hgnc — verify correct lowercase HGNC numeric ID); target_exon: exon 8).

This ASO has not, to my knowledge from this search, progressed to a registered human clinical trial (no NCT identifier found); it remains at the primate/preclinical stage as of the most recent identified publication (2022).

**No approved gene therapy, cell therapy, small-molecule, or targeted pharmacotherapy** exists for the underlying TECPR2 autophagy/secretory defect.

---

## 13. Prevention

- **Primary prevention**: genetic counseling and **carrier screening** in at-risk populations (Ashkenazi and Bukharian Jewish communities) to inform reproductive decision-making; the disease itself cannot be prevented once biallelic pathogenic genotype is present.
- **Secondary prevention**: prenatal diagnosis and preimplantation genetic testing (PGT) are available once familial pathogenic variants are identified, allowing at-risk couples to avoid transmission or to prepare for early postnatal management.
- **Tertiary prevention** (preventing complications in affected individuals): proactive respiratory surveillance (polysomnography, timely initiation of noninvasive ventilation) and aspiration-risk management (swallow studies, feeding modification/gastrostomy) are the most clinically consequential preventive measures, since aspiration and central apnea are the leading causes of death.
- **Immunization**: no disease-specific vaccine strategy; standard respiratory-pathogen vaccination (influenza, pneumococcal, RSV prophylaxis where age-appropriate) is prudent given the high burden of recurrent aspiration pneumonia, though this is general supportive practice rather than a TECPR2-specific published recommendation.
- **Screening programs**: no population-based newborn screening exists for this ultra-rare disorder; screening is limited to targeted carrier testing in founder populations.
- **Behavioral/public health interventions**: not applicable beyond genetic counseling, given the purely monogenic etiology.

---

## 14. Other Species / Natural Disease

**Naturally occurring TECPR2-related disease in animals — Spanish Water Dog neuroaxonal dystrophy:**
A naturally occurring, homologous disease was described in **Spanish Water Dogs** (*Canis lupus familiaris*, NCBITaxon:9615): four dogs presented with slowly progressive neurological signs (gait abnormalities, behavioral deficits) beginning at 6–11 months of age, segregating in an autosomal recessive pattern. Whole-genome/exome analysis identified a single, perfectly associated non-synonymous canine TECPR2 variant, **c.4009C>T (p.R1337W)** ([Hahn et al. 2015, *PLOS ONE*, PMID:26555167](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0141824)). Histopathology showed **axonal spheroid formation** concentrated in the grey matter of cerebral hemispheres, cerebellum, brainstem, and spinal cord sensory pathways — with no iron accumulation — and ultrastructurally the spheroids contained densely packed double-membraned vesicles characterized as **autophagosomes**, closely mirroring the human disease mechanism. This is catalogued in OMIA as **OMIA:001975-9615** (Neuroaxonal dystrophy, TECPR2-related, in dog). Commercial genetic panels (e.g., Paw Print Genetics) now offer this as a breed-specific test, giving it real veterinary screening relevance for Spanish Water Dog breeding programs.

**Comparative biology:** The dog phenotype (progressive neuroaxonal dystrophy with autophagosome accumulation in sensory/motor long tracts) closely parallels both the human disease and the engineered mouse models, supporting deep evolutionary conservation of TECPR2's role in axonal autophagosome clearance across mammals.

**Zoonotic potential/transmission:** Not applicable — this is a purely genetic, non-infectious, non-transmissible disorder.

---

## 15. Model Organisms

**Mouse models (Mus musculus, NCBITaxon:10090; MGI:2144865, *Tecpr2*):**

1. **CRISPR-Cas9 *Tecpr2*⁻/⁻ knockout mouse** ([Tamim-Yecheskel et al. 2021, *Autophagy*](https://www.tandfonline.com/doi/full/10.1080/15548627.2020.1852724); also referenced as PMID:33218264 in GeneReviews):
   - Recapitulates behavioral pathology seen in SPG49 patients.
   - Develops **age-dependent neuroaxonal dystrophy**, predominantly in the gracile (GrN) and cuneate nuclei (CuN) of the medulla oblongata and the dorsal white matter column of the spinal cord — anatomically matching the human dorsal-column sensory pathway involvement.
   - Shows age-dependent accumulation of autophagosomes, consistent with a defect in autophagosome-to-lysosome targeting.
   - **Limitation**: a knockout (complete null) model may not fully recapitulate the partial loss-of-function seen with some human missense alleles, and mice do not model the severe intellectual disability/speech phenotype central to the human disease (behavioral correlates in rodents are necessarily indirect).

2. **TECPR2 nonsense knock-in mouse (2025)** ([Cell Death & Disease, PMID:41173829](https://pmc.ncbi.nlm.nih.gov/articles/PMC12578842/)):
   - Carries the HSAN9-associated nonsense mutation directly (more genetically faithful than a full knockout).
   - Exhibits gait ataxia, axonal spheroids in sensory medullary regions, and progressive neuronal loss in dorsal column nuclei.
   - Reveals **broader endolysosomal dysfunction** beyond autophagosome-lysosome fusion, including TECPR2–HOPS complex interaction, organellar damage (swollen mitochondria, enlarged ER) in affected axons, and a maladaptive **microglial disease-associated phenotype** with enlarged lysosomes but reduced neuronal-debris clearance capacity.
   - This is the most mechanistically comprehensive model to date, integrating proteomics, transcriptomics, and electron microscopy.
   - **Applications**: studying endolysosomal/autophagy-microglia crosstalk in neurodegeneration; a platform for testing autophagy-enhancing or endolysosomal-targeted small molecules.

**Naturally occurring large-animal model:** The Spanish Water Dog (see §14) functions as a spontaneous, naturally occurring genetic model complementing the engineered mouse lines, valuable because it arises from an endogenous missense variant (p.R1337W) rather than an engineered null allele.

**Cellular models:**
- **Patient-derived dermal fibroblasts** — used in the original 2012 description to demonstrate reduced LC3-II/p62 (autophagy flux defect), and subsequently in the 2022 ASO study.
- **Patient-derived iPSC-derived neurons** (homozygous for c.1319delT) — used to confirm absence of TECPR2 protein and to validate ASO-induced exon-skipping and restoration of the characteristic punctate neuronal TECPR2 localization pattern (Molecular Therapy Nucleic Acids, PMID:35860385).

**Resources:** MGI (*Tecpr2*, MGI:2144865) for mouse strain/allele information; OMIA:001975-9615 for the canine model.

---

## Summary of Key Ontology-Term Suggestions for KB Curation

| Category | Suggested term(s) |
|---|---|
| Disease | MONDO:0014016; OMIM:615031; ORPHA:320385 |
| Gene | HGNC:19957 (TECPR2) — verify exact numeric HGNC ID against the local `hgnc` OAK adapter before curating |
| Core phenotypes (HP) | HP:0001263 (Developmental delay), HP:0001249 (Intellectual disability), HP:0001252 (Hypotonia), HP:0002066 (Gait ataxia), HP:0001258 (Spasticity), HP:0002522 (Areflexia), HP:0001260 (Dysarthria), HP:0002829 (Impaired pain sensation), HP:0004926 (Central sleep apnea), HP:0002020 (Gastroesophageal reflux), HP:0002015 (Dysphagia), HP:0002835 (Recurrent aspiration pneumonia), HP:0000252 (Microcephaly), HP:0000708 (Behavioral abnormality) |
| Biological process (GO) | macroautophagy / autophagosome maturation and fusion with lysosome, COPII vesicle coating, ER-to-Golgi transport |
| Cellular component (GO) | autophagosome (GO:0005776), lysosome (GO:0005764), ER exit site |
| Cell types (CL) | neuron (CL:0000540), microglial cell (CL:0000129) |
| Anatomy (UBERON) | dorsal column of spinal cord, gracile/cuneate nuclei, cerebellum, corticospinal tract |
| Treatment (NCIT) | C15747 (Supportive Care), C15302 (Physical Therapy), C15240 (Genetic Counseling), C15447 (Dietary Intervention) |
| Inheritance | HP:0000007 (Autosomal recessive inheritance) |

**Note on curation caveats:** Every ontology CURIE above should be verified against the dismech OAK adapters (`just validate-terms`) before use, since several (exact HGNC numeric ID, exact GO autophagosome-lysosome-fusion child term, exact UBERON dorsal-column-nucleus term) were not independently cross-checked against a live ontology lookup in this research pass and are offered as strong candidates rather than confirmed bindings.

---

### Sources

- [Oz-Levi et al. 2012, Am J Hum Genet, PMID:23176824](https://www.sciencedirect.com/science/article/pii/S000292971200523X) — original TECPR2/SPG49 description
- [OMIM *615000 TECPR2](https://www.omim.org/entry/615000)
- [GeneReviews: TECPR2-Related HSAN with Intellectual Disability (NBK584409)](https://www.ncbi.nlm.nih.gov/books/NBK584409/)
- [Orphanet ORPHA:320385](https://www.orpha.net/en/disease/detail/320385)
- [Neuser et al. 2021, Hum Mutat, PMID:33847017 — clinical/neuroimaging/molecular spectrum](https://pubmed.ncbi.nlm.nih.gov/33847017/)
- [Heimer et al. 2016, PMID:26542466 — Ashkenazi founder variant](https://pubmed.ncbi.nlm.nih.gov/26542466/)
- [Ramsey et al. 2022, Mol Genet Genomic Med, PMID:34994087 — heterozygous cerebellar atrophy](https://pmc.ncbi.nlm.nih.gov/articles/PMC8830808/)
- [Tamim-Yecheskel et al. 2020/2021, Autophagy — Tecpr2 knockout mouse](https://www.tandfonline.com/doi/full/10.1080/15548627.2020.1852724)
- [2025, Cell Death & Disease, PMID:41173829 — Tecpr2 knock-in mouse, endolysosomal/microglial mechanism](https://pmc.ncbi.nlm.nih.gov/articles/PMC12578842/)
- [Molecular Therapy Nucleic Acids 2022, PMID:35860385 — ASO exon-skipping therapy](https://pubmed.ncbi.nlm.nih.gov/35860385/)
- [Stadel et al. 2015, Mol Cell, PMID:26431026 — TECPR2/LC3C/COPII ER export](https://pubmed.ncbi.nlm.nih.gov/26431026/)
- [Nature Communications 2023 — spatial proteomics of TECPR2 secretory pathway disturbance](https://www.nature.com/articles/s41467-023-36553-6)
- [Hahn et al. 2015, PLOS ONE, PMID:26555167 — Spanish Water Dog TECPR2 neuroaxonal dystrophy](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0141824)
- [Novel Chinese HSP49 case report, PMID:35130874](https://pubmed.ncbi.nlm.nih.gov/35130874/)
- [UniProt O15040 (TECPR2)](https://www.uniprot.org/uniprotkb/O15040/entry)
- [GeneCards TECPR2](https://www.genecards.org/card/TECPR2)
- [OMIA:001975-9615 canine model](https://www.omia.org/OMIA001975/9615/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.