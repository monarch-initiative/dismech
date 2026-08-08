---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-08T04:29:28.321555'
end_time: '2026-08-08T04:35:35.688807'
duration_seconds: 367.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Syphilis
  mondo_id: ''
  category: Infectious Disease
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
  web_search_requests: 18
  num_turns: 21
  total_cost_usd: 1.9655228
  session_id: b20bd498-c3d4-5201-8d0b-983a970fa830
  stop_reason: end_turn
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Syphilis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Syphilis** covering all of the
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

# Syphilis (*Treponema pallidum* subsp. *pallidum* Infection): Comprehensive Disease Characteristics Research Report

---

## 1. Disease Information

**Overview:** Syphilis is a chronic, multistage sexually transmitted infection (and vertically transmissible perinatal infection) caused by the spirochete bacterium *Treponema pallidum* subspecies *pallidum* (TPA). Untreated, it evolves through primary, secondary, latent, and tertiary stages over years to decades, and can involve virtually any organ system, giving rise to its historical epithet "the great imitator." It remains a major global public-health problem despite being fully curable with penicillin.

**Key identifiers:**
| System | Identifier | Notes |
|---|---|---|
| ICD-10-CM | A50 (congenital), A51 (early/primary-secondary), A52 (late), A53 (unspecified/latent) | A53.9 = "Syphilis, unspecified"; A51.2 = "Primary syphilis of other sites" |
| ICD-11 | 1A62 (Syphilis) with substrata for congenital/early/late forms | Verify exact foundation-layer code via ICD-11 MMS browser before curation |
| MeSH | D013587 *Syphilis* (with child terms D013590 Syphilis, Congenital; D013591 Neurosyphilis; D013589 Syphilis, Cardiovascular) | High confidence |
| MONDO | Likely MONDO:0005097 (verify via OLS/OAK — `sqlite:obo:mondo info` — before committing to KB) | |
| Disease Ontology (DOID) | DOID:8544 (verify) | |
| Causative organism (NCBITaxon) | NCBITaxon:160rest — *Treponema pallidum* subsp. *pallidum*, NCBITaxon:160 (genus level), specific subspecies taxon should be confirmed via NCBI Taxonomy browser | |

**Common synonyms:** Lues, lues venerea, "the great pox," "the great imitator" (clinical epithet, not a synonym), *Treponema pallidum* infection. Congenital forms are historically termed "hereditary syphilis." Related but taxonomically distinct non-venereal treponematoses caused by other *T. pallidum* subspecies are **yaws** (*T. pallidum* subsp. *pertenue*) and **bejel/endemic syphilis** (*T. pallidum* subsp. *endemicum*) — these are separate MONDO/ICD entities and should not be conflated with venereal syphilis in curation.

**Evidence base:** Information below is derived from aggregated disease-level resources — clinical guidelines (CDC STI Treatment Guidelines, USPSTF), textbook/review sources (StatPearls, AMBOSS), population surveillance (CDC NCHHSTP national STI surveillance), and primary/peer-reviewed literature (PubMed/PMC) — rather than individual patient-level EHR data.

Sources: [ICD-11 MMS — Syphilis](https://www.findacode.com/icd-11/block-455894495.html); [ICD-10-CM A53.9](https://www.icd10data.com/ICD10CM/Codes/A00-B99/A50-A64/A53-/A53.9); [ICD-10-CM A51.2](https://www.icd10data.com/ICD10CM/Codes/A00-B99/A50-A64/A51-/A51.2); [Mondo Disease Ontology — Monarch Initiative](https://mondo.monarchinitiative.org/)

---

## 2. Etiology

**Disease causal factor:** Infectious — direct causation by *Treponema pallidum* subsp. *pallidum*, a thin, tightly coiled, motile spirochete that cannot be cultured continuously in vitro (in vitro continuous culture was only first achieved in specialized co-culture systems in the mid-2010s; nearly all experimental work still uses the rabbit model). Transmission occurs primarily through direct contact with an infectious lesion (chancre, mucous patch, condyloma latum) during vaginal, anal, or oral sex, and via transplacental transmission from mother to fetus (congenital syphilis); less commonly via blood transfusion or needle-sharing.

**Risk factors:**
- *Behavioral/epidemiological:* Men who have sex with men (MSM) is the population with the highest per-capita incidence in most high-income countries; condomless sex; multiple/anonymous sexual partners; transactional/"rewarded" sex; younger age at sexual debut; history of another bacterial STI in the past 12 months (marker of ongoing risk, and the basis for doxy-PEP eligibility).
- *Coinfection:* HIV infection is strongly associated with syphilis acquisition and vice versa — a bidirectional, mutually potentiating relationship. A systematic review/meta-analysis found syphilis infection roughly doubles subsequent HIV acquisition risk (PMID:33219164). Male sex and MSM status were independently associated with HIV coinfection among incident syphilis cases (PMID:29451611).
- *Maternal/obstetric (congenital syphilis):* Lack of, late, or absent prenatal care is the dominant risk factor; untreated maternal primary/secondary syphilis in the third trimester carries the highest transplacental transmission risk (60–100%) versus early-latent (~40%) or late-latent (<8%) maternal infection.
- *Demographic disparities:* In the U.S., Native American/Alaska Native and Black populations bear disproportionately high and rising rates of maternal and congenital syphilis; the largest relative rise in maternal syphilis (2017–2022) was among Native Americans.

**Protective factors:**
- Consistent condom use reduces but does not eliminate transmission risk (chancres/lesions may occur outside condom-covered areas).
- Doxycycline post-exposure prophylaxis (doxy-PEP): CDC (2024) recommends 200 mg doxycycline within 72 hours of condomless sex for MSM/transgender women with a bacterial STI in the prior 12 months; randomized trials showed >70% reduction in incident syphilis and chlamydia, and ~50% reduction in gonorrhea.
- Universal prenatal syphilis screening and treatment (USPSTF Grade A, reaffirmed 2025) is highly effective primary/secondary prevention for congenital syphilis.
- No genetic protective variants are well established for syphilis (unlike, e.g., CCR5-Δ32 for HIV); this is an active research gap.

**Gene–environment interactions:** Data are sparse. A positive correlation between HLA-DR+CD8+ T-cell subsets and syphilis recurrence/reinfection/serofast state has been reported in HIV/syphilis coinfected cohorts, suggesting host immunogenetic factors may modulate clinical course and serologic response to treatment, but no validated causal susceptibility locus exists. This is best modeled as a curated `KNOWLEDGE_GAP` rather than an established GxE mechanism.

Sources: [Effect of syphilis infection on HIV acquisition — meta-analysis](https://pubmed.ncbi.nlm.nih.gov/33219164/); [Factors associated with HIV co-infection in acquired syphilis](https://pubmed.ncbi.nlm.nih.gov/29451611/); [CDC Doxy-PEP Guidelines 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11166373/); [USPSTF syphilis screening in pregnancy](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/syphilis-infection-in-pregnancy-screening); [Clinical/immunological characteristics of HIV/syphilis coinfection](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2023.1327896/full)

---

## 3. Phenotypes

### Primary syphilis (10–90 days, median 21–25 days post-exposure)
- **Chancre**: solitary (occasionally multiple), painless, indurated genital/anal/oral ulcer with clean base — HPO suggestion: HP:0200043-class skin ulcer terms (verify exact chancre-specific term via OAK; may need free-text `preferred_term` with a broader HP anchor such as "Skin ulcer").
- **Regional lymphadenopathy** (HP:0002716, verify), typically non-tender, "rubbery."
- Onset: acute; severity: mild locally (lesion is often unnoticed, especially in women/receptive anal partners, contributing to underdiagnosis); self-resolving in 3–6 weeks even without treatment (progression to latency, not cure).

### Secondary syphilis (weeks to a few months after chancre; may overlap with a healing chancre)
- **Diffuse maculopapular rash**, classically involving palms and soles (HP:0001028 Maculopapular rash — verify) — nearly pathognomonic when palmoplantar.
- **Condyloma lata**: broad, moist, wart-like plaques in warm intertriginous areas — highly infectious.
- **Mucous patches** on oral/genital mucosa.
- **Generalized lymphadenopathy**, low-grade fever, malaise, headache, sore throat.
- **Patchy alopecia** ("moth-eaten" alopecia; HP:0001596 Alopecia — verify).
- Hepatosplenomegaly, hepatitis (syphilitic hepatitis), glomerulonephritis (immune-complex mediated), and — rarely — periostitis in this stage.
- Frequency: rash occurs in a large majority of untreated secondary-stage patients; condyloma lata frequency is lower and site-dependent (case reports document unusual/extensive presentations, e.g. PMC12490915).
- Severity/progression: self-limited (resolves in weeks-to-months) but relapses can occur during early latency in ~25% of untreated cases.

### Latent syphilis
- **Asymptomatic by definition** — positive treponemal + nontreponemal serology with no clinical signs. Subdivided as early latent (<1 year from infection) vs. late latent/unknown duration (>1 year), a distinction that governs treatment duration and infectiousness (early latent remains contagious via occasional mucocutaneous relapse; late latent is not sexually contagious but remains vertically transmissible and can still progress to tertiary disease).

### Tertiary (late) syphilis (occurs in an estimated 15–40% of untreated individuals, typically years to decades after infection)
- **Gummatous syphilis** (benign tertiary): granulomatous, necrotic "gumma" lesions in skin, bone, and viscera — locally destructive but non-infectious.
- **Cardiovascular syphilis**: syphilitic aortitis, thoracic aortic aneurysm, aortic regurgitation, coronary ostial stenosis (see §6). Accounts for the majority (>80%) of tertiary vascular complications, historically the leading cause of syphilis-related mortality.
- **Neurosyphilis** (can occur at *any* stage, not only tertiary): meningovascular neurosyphilis (stroke syndromes), general paresis (progressive dementia, personality change, tremor), tabes dorsalis (posterior column degeneration → sensory ataxia, lightning pains, Argyll Robertson pupils, areflexia).
- **Ocular syphilis** (panuveitis, optic neuritis, retinitis) and **otosyphilis** (sensorineural hearing loss, tinnitus, vertigo) — CDC surveillance across 16 states found these under-recognized manifestations occurring across all stages, disproportionately in HIV-coinfected persons (PMID:35819903). Among HIV-positive patients with ophthalmic syphilis, ~85% also had neurosyphilis (case-series estimate).

### Congenital syphilis
- **Early congenital** (<2 years of age; pathophysiologically analogous to disseminated secondary syphilis): ranges from asymptomatic (~2/3 of live-born infected infants) to hepatosplenomegaly, maculopapular/desquamative rash, "snuffles" (mucopurulent/hemorrhagic rhinitis), condyloma lata, osteochondritis/periostitis (long-bone radiographic changes), lymphadenopathy, jaundice, hemolytic anemia, thrombocytopenia, and — in the most severe cases — non-immune **hydrops fetalis** (HP:0001789) and **stillbirth** (up to ~40% of untreated maternal infections).
- **Late congenital** (>2 years, ~1/3 of untreated survivors, from irreversible scarring during early disease): **Hutchinson triad** — interstitial keratitis (HP:0001139, verify), Hutchinson (notched, widely-spaced, peg-shaped) incisors and mulberry molars, and sensorineural hearing loss (HP:0000407); plus saddle nose (HP:0000431), frontal bossing, short maxilla/protuberant mandible, saber shins (anterior tibial bowing), rhagades (perioral fissures/scars), and Clutton joints (painless bilateral knee synovitis).

**Quality-of-life impact:** Acute-stage manifestations (chancre, rash) cause modest disability but resolve; the major QoL burden is concentrated in (a) neurosyphilis/tabes dorsalis (chronic neuropathic pain, gait ataxia, cognitive decline — general paresis was historically a leading cause of institutionalized psychiatric disability pre-antibiotic era), (b) sensorineural hearing/vision loss from oto-/ocular syphilis, and (c) the lifelong disability, cognitive impairment, and stigmata of untreated congenital syphilis in survivors. Dedicated disease-specific QoL instrument data (EQ-5D/SF-36) for syphilis specifically are not well represented in the literature; QoL burden is more typically captured indirectly via disability-adjusted life year (DALY) estimates in global-burden-of-disease reporting.

Sources: [Neurologic, Ocular, and Otic Manifestations Among Syphilis Cases — 16 states](https://pubmed.ncbi.nlm.nih.gov/35819903/); [Neurosyphilis, Ocular Syphilis, and Otosyphilis: Detection and Treatment](https://pubmed.ncbi.nlm.nih.gov/35977144/); [Congenital Syphilis — An Illustrative Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10453258/); [Congenital and Maternal Syphilis — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537087/); [Clinical aspects of congenital syphilis with Hutchinson's triad](https://pubmed.ncbi.nlm.nih.gov/22670010/); [Extensive Condyloma Lata Lesions in Unusual Sites](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12490915/); [Syphilis — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK534780/)

---

## 4. Genetic/Molecular Information

Syphilis is not a Mendelian genetic disease of the host, so this section covers **pathogen molecular biology** (the operative "genetics" for a dismech-style pathophysiology entry) plus what little is known about host genetic modifiers.

- **Causal organism genome:** *T. pallidum* subsp. *pallidum* has a small (~1.14 Mb), reduced genome reflecting extreme host-restriction and metabolic dependency (it lacks TCA-cycle enzymes and relies heavily on host-derived nutrients), consistent with obligate-pathogen biology. No plasmids; no classical LPS.
- **Key virulence/immune-evasion loci:**
  - ***tprK*** (*Treponema pallidum repeat* K): encodes an integral outer-membrane porin with seven surface-exposed variable (V1–V7) regions. Antigenic diversity is generated by **non-reciprocal segmental gene conversion**, transferring sequence from ~53 silent chromosomal donor cassettes into the single *tprK* expression locus (PMID:15186410). V-region diversity accumulates faster under host immune pressure (especially V6), directly implicating TprK antigenic variation as a mechanism of immune persistence; a TprK-variation-impaired mutant strain is attenuated in the rabbit model (bioRxiv/PMC10063172), and Seattle-area genomic surveillance (2021–2022) has identified circulating strains with diminished TprK variation capacity (academic.oup.com/jid/article/229/3/866/7283202).
  - **23S rRNA A2058G / A2059G point mutations**: the molecular basis of macrolide (azithromycin) resistance, first identified in San Francisco (2002) and now geographically widespread (U.S., Ireland, Canada, Taiwan, Indonesia); detected clinically by TaqMan real-time multiplex PCR. This has effectively removed azithromycin as a first-line agent in most jurisdictions (PMID:18192791; NEJM Lukehart et al. 2004).
  - Outer-membrane protein (OMP) repertoire (e.g., TP0856, TP0858 — FadL orthologs; BamA/TP0326): rare, low-density, surface-exposed OMPs identified via structural modeling as the principal syphilis vaccine antigen candidates (PMC8407342; journals.asm.org/doi/10.1128/jb.00082-21).
  - Strain typing (molecular epidemiology, not disease-causing per se): variable-number tandem repeats in the *arp* gene combined with RFLP of *tprE/tprG/tprJ* and *tp0548* sequence — the CDC "enhanced CDC typing" (ECDCT) scheme used for outbreak/lineage surveillance.
- **Host genetics:** No validated causal or susceptibility-conferring human gene/variant is established. The only host-genetic signal identified so far is an association between HLA-DR+CD8+ T-cell subset frequency and syphilis recurrence/serofast state in HIV coinfection — exploratory, not a validated ACMG-tier variant classification, and should be curated as a knowledge gap rather than a genetic risk locus.
- **Functional impact framing for dismech curation:** Antigenic variation (TprK) and macrolide-target mutation (23S rRNA) are both **qualitative, unbound** mechanisms in the `GAIN_OF_FUNCTION`/immune-evasion sense described in this repo's CLAUDE.md (no clean GO/PATO-bound "activity level" framing applies) — they would be modeled as `modifier: GAIN_OF_FUNCTION`-style pathogen mechanism nodes, not host `GeneticContext.functional_impact_category` entries, since there is no host variant involved.

Sources: [Gene conversion in tprK — Mol Microbiol](https://pubmed.ncbi.nlm.nih.gov/15186410/); [Genomic Epidemiology... Diminished tprK Variation, Seattle 2021–2022](https://academic.oup.com/jid/article/229/3/866/7283202); [TprK-impaired strain attenuated in rabbit model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10063172/); [Azithromycin resistance in T. pallidum](https://pubmed.ncbi.nlm.nih.gov/18192791/); [Macrolide Resistance in T. pallidum, US and Ireland — NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa040216); [Structural Modeling of T. pallidum OMP Repertoire](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8407342/); [FadL orthologs TP0856/TP0858 rabbit model — mBio](https://journals.asm.org/doi/full/10.1128/mbio.01639-22)

---

## 5. Environmental Information

- **Infectious agent:** *Treponema pallidum* subsp. *pallidum* (NCBITaxon — spirochete, phylum Spirochaetota). Transmission requires direct mucocutaneous contact with an active lesion; the organism does not survive well outside the host (fomite transmission is negligible).
- **Behavioral/lifestyle factors:** condomless sex, number of sexual partners, transactional sex, substance use associated with high-risk sexual behavior (e.g., methamphetamine use in some MSM sub-epidemics), incarceration history, and limited access to sexual-health/prenatal care are the dominant modifiable environmental drivers — these are social/behavioral rather than toxicant/occupational exposures.
- **No chemical/toxicological/occupational etiology** applies; syphilis is not caused by environmental toxins, radiation, or pollution. The "environmental" arm of a dismech entry for syphilis should be modeled almost entirely through `ECTO`-style sexual/vertical exposure-route terms and infectious-exposure framing rather than CTD/TOXNET-style chemical exposures.
- **Structural/social determinants:** lack of prenatal care access, rural/under-resourced healthcare infrastructure, and racial/ethnic health disparities are repeatedly identified in CDC and PAHO surveillance as the proximate drivers of the ongoing U.S. congenital syphilis surge (see §9).

Sources: [CDC Releases 2024 National STI Data](https://www.cdc.gov/nchhstp/director-letters/release-2024-sti-data.html); [The Rise of Congenital Syphilis as a Public Health Emergency](https://pmc.ncbi.nlm.nih.gov/articles/PMC12456561/)

---

## 6. Mechanism / Pathophysiology

### Causal chain overview
1. **Inoculation and dissemination:** *T. pallidum* penetrates intact mucosa or abraded skin, replicates locally, and disseminates hematogenously/lymphatically within days to weeks — spirochetemia is established even before the primary chancre becomes clinically apparent, explaining why congenital and disseminated (secondary-stage) disease can occur even from an unnoticed primary lesion.
2. **Local inflammatory/immune response (chancre formation):** infiltration by CD4+ T-helper-1 cells, macrophages, and plasma cells at the inoculation site; local vascular changes (endarteritis) produce the indurated, ulcerated chancre. Despite intense local immune infiltration, the organism largely evades clearance.
3. **Stealth-pathogen immune evasion (the central pathophysiological theme):** *T. pallidum*'s outer membrane is essentially devoid of surface-exposed, immunogenic integral membrane proteins and — critically — **lacks lipopolysaccharide (LPS)**, unlike most Gram-negative bacteria, denying the innate immune system its usual PAMP trigger (PMID:27721440; "making a living as a stealth pathogen"). Layered onto this "low-visibility" membrane architecture is **TprK antigenic variation** (§4), which continuously alters the few surface epitopes that do exist, outrunning adaptive humoral responses. Recent work (2025, PMID:40708500) frames pathogenesis as a dynamic host-immune-response-versus-pathogen-immune-evasion contest: dendritic cells present treponemal antigen to naive CD4+ T cells, driving a Th1-polarized response (IFN-γ-driven macrophage activation/phagocytosis) that is necessary for clearance from skin lesions but insufficient to eradicate the organism from immune-privileged sanctuary sites (CNS, eye, placenta).
4. **Dissemination to immune-privileged sites:** the organism's ability to cross the blood-brain barrier, blood-ocular barrier, and placental barrier explains why neurosyphilis, ocular syphilis, and congenital transmission can occur at any stage, including very early infection, rather than being restricted to "late" disease as classically taught.
5. **Secondary-stage systemic dissemination:** widespread hematogenous spread produces the generalized rash, condyloma lata, lymphadenopathy, and visceral involvement (hepatitis, immune-complex glomerulonephritis) of secondary syphilis.
6. **Latency:** partial host immune containment suppresses clinically detectable disease without eradicating the organism; low-level persistence (and stochastic local reactivation, particularly early in latency) maintains seropositivity and, in a minority, leads eventually to tertiary disease.
7. **Tertiary-stage vascular/granulomatous pathology:** chronic, low-grade treponemal presence in the vasa vasorum of medium/large arteries (classically the ascending aorta) triggers a slowly progressive **obliterative endarteritis** — lymphoplasmacytic infiltration of the adventitia with ischemic injury to the aortic media, destruction of elastic/muscular fibers, and consequent aneurysmal dilation, aortic regurgitation, and coronary ostial stenosis (>80% of tertiary manifestations are vascular in nature). **Gummas** (in skin, bone, viscera, or — as microgummas — within the aortic media) represent a delayed-type hypersensitivity granulomatous response with central necrosis and palisading macrophages/lymphocytes/plasma cells; treponemes are typically scant and hard to demonstrate within gumma tissue, consistent with a predominantly immune-mediated (rather than direct cytopathic) injury mechanism at this stage.
8. **Neurosyphilis mechanism:** direct CNS invasion with either a meningovascular pattern (endarteritis of cerebral vessels → stroke syndromes) or, later, parenchymal neuronal/glial injury (general paresis — cortical atrophy, gliosis; tabes dorsalis — dorsal column/dorsal root ganglion degeneration). HIV coinfection appears to accelerate and intensify this process, plausibly via impaired CD4+ T-cell-mediated containment (PMID:25890619).
9. **Congenital pathophysiology:** transplacental spirochetemia produces a disease process analogous to disseminated secondary syphilis in the fetus; severity is inversely related to gestational age at infection but transmission probability increases with advancing gestational age and untreated maternal spirochete burden.

### Molecular pathways / cellular processes (GO-term suggestions, verify via OAK)
- Innate recognition failure / LPS-independent pathogen sensing — contrast with canonical TLR4-LPS signaling (GO:0034142 Toll-like receptor 4 signaling pathway is notably *not* engaged in the way it is for classical Gram-negatives).
- GO:0002250 adaptive immune response; GO:0042088 T-helper 1 type immune response; GO:0006909 phagocytosis; GO:0006954 inflammatory response; GO:0020033 antigenic variation (a GO term specifically used for pathogen immune-evasion biology, appropriate for the TprK mechanism).
- Cellular processes: dendritic-cell antigen presentation → CD4+ Th1 polarization → IFN-γ–mediated macrophage activation and treponemal phagocytosis (partial clearance); obliterative vasculitis/endarteritis as the shared cellular mechanism linking chancre formation and tertiary aortitis.

### Cell types involved (CL-term suggestions)
- CL:0000624 CD4-positive, alpha-beta T cell (Th1 effector); CL:0000235 macrophage; CL:0000451 dendritic cell; CL:0000786 plasma cell (humoral response, and prominent in chancre/gumma histology); CL:0000115 endothelial cell (target of obliterative endarteritis in both chancre and aortitis); CL:0000058 cementoblast/CL bone-cell terms for periostitis/osteochondritis in congenital disease (verify specific term).

### Molecular/omics profiling
- Limited transcriptomic/proteomic host-response profiling exists for syphilis relative to other STIs; most mechanistic work is genomic/proteomic on the pathogen side (OMP structural modeling, TprK deep sequencing). A 2024 pan-proteome array study profiled the humoral (antibody) response to the full *T. pallidum* proteome as a pre-clinical diagnostic/vaccine-target discovery tool (bioRxiv 2024.04.20.590429).
- No well-established single-cell or spatial transcriptomic dataset specific to syphilis lesions was identified in this search; this is a plausible knowledge/data gap worth flagging in curation.

Sources: [Syphilis Pathogenesis: Host Immune Response vs Pathogen Immune Evasion (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12526937/); [T. pallidum: making a living as a stealth pathogen](https://pmc.ncbi.nlm.nih.gov/articles/PMC5106329/); [Investigation of the immune escape mechanism of T. pallidum](https://link.springer.com/article/10.1007/s15010-022-01939-z); [Syphilitic aortitis and its complications in the modern era](https://pubmed.ncbi.nlm.nih.gov/27982548/); [Pathology of syphilis — UCT](https://health.uct.ac.za/pathology-learning-centre/disease-themes-syphilis-isifo-sedolobha-disease-town/pathology-syphilis); [Neurosyphilis and the impact of HIV infection](https://pubmed.ncbi.nlm.nih.gov/25890619/); [Pan-proteome array humoral response study, 2024](https://www.biorxiv.org/content/10.1101/2024.04.20.590429.full.pdf)

---

## 7. Anatomical Structures Affected

- **Organ/system level:** integumentary system (chancre, secondary rash, gummas), lymphoreticular system (lymphadenopathy), cardiovascular system (aorta, aortic valve, coronary ostia — tertiary disease), central/peripheral nervous system (meninges, cerebral vasculature, spinal cord dorsal columns, cranial nerves — neurosyphilis), special senses (eye — uvea/retina/optic nerve; ear — cochlea/vestibular apparatus), hepatobiliary system (syphilitic hepatitis), renal system (immune-complex glomerulonephritis, secondary stage), skeletal system (periostitis/osteochondritis, gummatous bone lesions), and — in congenital disease — essentially every fetal organ system via hematogenous dissemination, plus the placenta itself as the transmission conduit.
- **UBERON suggestions (verify):** UBERON:0002097 skin of body; UBERON:0000947 aorta; UBERON:0002094 aortic valve (verify exact ID); UBERON:0001987 placenta; UBERON:0001017 central nervous system; UBERON:0000955 brain; UBERON:0002240 spinal cord; UBERON:0000970 eye; UBERON:0000959 cochlea (or UBERON:0001846 for broader otic region — verify); UBERON:0002107 liver; UBERON:0002113 kidney; UBERON:0001474 bone element; UBERON:0000474 external genitalia (chancre site); UBERON:0000030 lamina propria/oral mucosa (mucous patches).
- **Tissue/cell level:** vascular endothelium and adventitial vasa vasorum (obliterative endarteritis — the shared lesion of chancre, gumma, and aortitis); epidermis/dermis (rash, condyloma lata); hepatic parenchyma; glomerular basement membrane (immune-complex deposition); dorsal root ganglia and dorsal columns of the spinal cord (tabes dorsalis); cerebral cortex/white matter (general paresis).
- **Subcellular:** immune-complex deposition at the glomerular basement membrane (GO Cellular Component terms for basement membrane, e.g. GO:0005604); outer membrane of the pathogen itself is the key subcellular structure driving pathogenesis (low-density, LPS-negative OMP architecture — §6).
- **Lateralization:** generally bilateral/symmetric in systemic manifestations (e.g., bilateral interstitial keratitis, bilateral sensorineural hearing loss in Hutchinson triad); chancres and localized gummas are typically unilateral/focal by nature of inoculation site.

Sources: [Syphilitic Aortitis — ScienceDirect](https://www.sciencedirect.com/topics/medicine-and-dentistry/syphilitic-aortitis); [Pathology of syphilis — UCT Pathology Learning Centre](https://health.uct.ac.za/pathology-learning-centre/disease-themes-syphilis-isifo-sedolobha-disease-town/pathology-syphilis)

---

## 8. Temporal Development

- **Onset:** Acquired syphilis has a variable window from exposure to primary chancre of 10–90 days (median 21–25 days); congenital syphilis onset is defined relative to birth (early <2 years vs. late ≥2 years of age), reflecting time for irreversible developmental scarring to manifest rather than ongoing active infection in the late form.
- **Progression / staging:** Primary → Secondary (weeks after chancre, may overlap) → Latent (early <1 year, late ≥1 year/unknown duration) → Tertiary (years to decades later, in an estimated 15–40% of untreated persons). Neurologic, ocular, and otic invasion can occur at *any* stage and is not confined to "late/tertiary" disease — an important reframing versus older teaching, now emphasized by CDC and recent surveillance (PMID:35819903).
- **Progression rate:** Highly variable between individuals; some remain in asymptomatic latency indefinitely, others progress to destructive tertiary disease. HIV coinfection is associated with an accelerated, more fulminant course and earlier neurosyphilis onset (PMID:25890619).
- **Disease course pattern:** Predominantly a slowly progressive, staged natural history in untreated hosts; early latency carries a risk (~25%) of symptomatic mucocutaneous relapse (a "relapsing" sub-pattern within the latent stage). With treatment at any stage, the course is halted, though tertiary-stage structural damage (aortic aneurysm, tabetic neurologic deficits, gummatous scarring) is generally irreversible even after microbiological cure.
- **Duration:** Untreated syphilis is a lifelong condition (the organism is not spontaneously cleared); adequately treated syphilis in the pre-tertiary stages is curable without sequelae. Congenital, late-stage stigmata (Hutchinson triad, skeletal deformities) are permanent once established.
- **Remission:** No spontaneous cure; only antimicrobial treatment reliably clears infection at any stage (though tertiary structural damage does not "remit" with treatment). Serologic "cure" is monitored via declining nontreponemal titers (RPR/VDRL) post-treatment; treponemal tests typically remain reactive for life ("serofast").
- **Critical periods / windows for intervention:** (1) Early (primary/secondary/early-latent) syphilis is the window of highest infectiousness and easiest single-dose cure. (2) Pregnancy is the critical window for congenital-transmission prevention — treating the mother before the third trimester, and ideally before conception or in the first trimester, dramatically reduces transmission and severity. (3) Post-exposure (within 72 hours) is the window for doxy-PEP efficacy.

Sources: [Syphilis — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK534780/); [Reported Neurologic, Ocular, and Otic Manifestations Among Syphilis Cases — 16 states, 2019](https://pubmed.ncbi.nlm.nih.gov/35819903/); [Neurosyphilis and the impact of HIV infection](https://pubmed.ncbi.nlm.nih.gov/25890619/)

---

## 9. Inheritance and Population

**Inheritance pattern:** Not applicable — syphilis is an acquired infectious disease with no Mendelian inheritance pattern, penetrance, expressivity, anticipation, mosaicism, or founder-effect biology in the classical genetic-disease sense. "Congenital syphilis" denotes vertical (transplacental) transmission of infection, not genetic inheritance, and should not be modeled with an `Inheritance`/HP:00109xx-style mode-of-inheritance term in dismech curation.

**Epidemiology (U.S., CDC 2024 data):**
- More than 2.2 million combined chlamydia/gonorrhea/syphilis cases were reported in 2024; reported primary-and-secondary (P&S) syphilis cases **declined for the second consecutive year**, down ~22% since 2023 — the first sustained decline after roughly two decades of increases.
- **Congenital syphilis** continued to rise: nearly 4,000 cases reported in 2024 (up ~2% from 2023), a 12th consecutive year of increase, and congenital syphilis morbidity is ~700% higher than a decade earlier. Nationally, 2023 saw 3,882 congenital syphilis cases — the highest rate in >30 years — with an estimated ~90% judged preventable through timely maternal diagnosis/treatment.
- **Maternal syphilis rate** rose 222% from 2016 to 2022 (87.2 → 280.4 per 100,000 live births).
- **Global context:** Congenital syphilis (including stillbirths) remains a tracked PAHO regional indicator; syphilis in pregnancy is among the leading global causes of stillbirth.

**Population demographics / disparities:**
- MSM continue to bear a disproportionate share of P&S syphilis cases in high-income settings.
- Native American/Alaska Native populations show the steepest relative rise in maternal syphilis (2017–2022); White and Asian American populations show comparatively smaller increases — reflecting structural disparities in prenatal-care access rather than biological susceptibility.
- Age distribution: acquired syphilis peaks in sexually active adults (20s–30s); congenital syphilis risk tracks maternal age distribution and, most strongly, gaps in prenatal-care engagement rather than maternal age per se.
- Geographic distribution: U.S. congenital syphilis case growth has been documented even outside historically high-burden metropolitan areas (e.g., 21 cases reported outside New York City in 2025), indicating geographic spread of the epidemic beyond traditional urban hotspots.

**Carrier/susceptibility genetics:** No established human carrier-frequency or population-genetic-susceptibility data exist for syphilis (unlike a Mendelian disorder); population-level "susceptibility" is driven by behavioral/structural/healthcare-access epidemiology rather than germline variation.

Sources: [CDC Releases 2024 National STI Data](https://www.cdc.gov/nchhstp/director-letters/release-2024-sti-data.html); [CDC data show declines in STIs, rise in newborn syphilis — CIDRAP](https://www.cidrap.umn.edu/sexually-transmitted-infections/cdc-data-show-declines-sexually-transmitted-infections-rise-newborn); [The Rise of Congenital Syphilis as a Public Health Emergency](https://pmc.ncbi.nlm.nih.gov/articles/PMC12456561/); [PAHO — Incidence rate of congenital syphilis](https://pbdigital.paho.org/en/eob-2024-2025/impact-results/18-incidence-rate-congenital-syphilis-including-stillbirths); [USPSTF universal syphilis screening in pregnancy](https://www.news-medical.net/news/20250518/USPSTF-urges-universal-syphilis-screening-in-pregnancy-to-prevent-congenital-infections.aspx)

---

## 10. Diagnostics

**Serologic testing (the diagnostic backbone):**
- **Nontreponemal tests** (RPR, VDRL): detect non-specific anticardiolipin/lipoidal antibodies from host tissue damage; quantitative (titers used to track treatment response); can be falsely negative early (prozone phenomenon at very high titers) or falsely positive in unrelated conditions (autoimmune disease, pregnancy, other infections).
- **Treponemal tests** (TP-PA, FTA-ABS, and increasingly automated EIA/CIA immunoassays): specific for anti-*T. pallidum* antibody; remain reactive lifelong in most patients regardless of treatment ("serofast"), so cannot distinguish active from past-treated infection alone.
- **Traditional algorithm:** nontreponemal screen (RPR/VDRL) → confirm reactive results with a treponemal test.
- **Reverse-sequence algorithm** (increasingly standard in automated labs): treponemal immunoassay first → if reactive, quantitative RPR/VDRL; if the two are discordant, a second treponemal test (typically TP-PA) serves as tiebreaker. British Columbia's 2015–2020 experience documented outcomes of implementing this reverse algorithm alongside PCR (PMC9241594).
- **PCR (direct detection):** used especially for early lesional disease (chancre swabs, mucocutaneous lesions) where serology may still be non-reactive; reported sensitivity as high as 100% in some series versus ~53% for dark-field and immunofluorescence microscopy — though estimates vary by study and lesion type.
- **Dark-field microscopy / direct fluorescent antibody:** classic direct visualization from chancre exudate, largely supplanted by PCR where available.
- **Cerebrospinal fluid (CSF) studies:** CSF-VDRL (specific but insensitive), CSF pleocytosis and elevated protein, for suspected neurosyphilis.

**LOINC/SNOMED CT suggestions (verify):** LOINC panels exist for RPR titer, TP-PA, and FTA-ABS results; SNOMED CT carries specific concepts for each stage (primary/secondary/latent/tertiary/congenital syphilis) and for chancre, condyloma latum, and gumma findings.

**Genetic/molecular testing:** Not applicable in the human-genetic-testing sense (no GTR panels for host susceptibility); the relevant "molecular diagnostics" are pathogen-directed — PCR for treponemal DNA and, in reference/surveillance labs, 23S rRNA genotyping (A2058G/A2059G) to detect macrolide resistance before considering azithromycin as an off-label alternative.

**Imaging:** contrast-enhanced CT/MR angiography or echocardiography for suspected cardiovascular (aortic) syphilis; brain MRI for neurosyphilis (may show meningeal enhancement, infarcts, or nonspecific atrophy in general paresis); long-bone radiographs for congenital syphilis (periostitis, metaphyseal lucencies — "Wimberger sign").

**Screening programs:**
- USPSTF Grade A: universal syphilis screening in **all pregnant adolescents/adults**, regardless of risk factors, as early as possible in pregnancy and at any later missed opportunity (reaffirmed 2025).
- Risk-based screening recommended for MSM, people with HIV, and other higher-incidence populations at regular intervals (e.g., every 3–6 months for higher-risk MSM per CDC guidance).
- Newborn screening is not itself a standard "genetic newborn screen" but maternal serology at delivery (and infant testing when maternal status is unknown/reactive) functions as the congenital-syphilis case-finding mechanism.

**Differential diagnosis:** other causes of genital ulcer disease (HSV, chancroid, LGV, donovanosis); other causes of diffuse maculopapular rash (viral exanthems, drug eruption, pityriasis rosea); other causes of granulomatous/gummatous lesions (TB, deep fungal infection, sarcoidosis); other causes of aortitis (Takayasu, giant cell arteritis); other causes of dementia/ataxia for neurosyphilis.

Sources: [British Columbia reverse algorithm and PCR experience 2015-2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9241594/); [Traditional or Reverse Algorithm for Diagnosis of Syphilis: Pros and Cons](https://pmc.ncbi.nlm.nih.gov/articles/PMC7312234/); [CDC STI Treatment Guidelines — Syphilis](https://www.cdc.gov/std/treatment-guidelines/syphilis.htm); [Reverse Sequence Screening for Syphilis](https://myadlm.org/cln/articles/2014/november/screening-syphilis)

---

## 11. Outcome/Prognosis

- **With appropriate treatment:** Excellent prognosis for primary, secondary, and early-latent disease — microbiological cure with single-dose (or short-course) benzathine penicillin G; nontreponemal titers decline (typically ≥4-fold by 6–12 months) confirming adequate treatment response.
- **Untreated natural history:** Roughly one-third of untreated persons progress to tertiary disease (gummatous, cardiovascular, and/or neurologic), one-third remain in indefinite subclinical latency, and one-third experience spontaneous serologic/clinical resolution without treatment (classic Oslo/Rosahn-cohort-derived natural-history estimates, corroborated across StatPearls/AMBOSS summaries) — though a commonly cited range for progression to tertiary disease specifically is 15–40%.
- **Mortality:** Historically (pre-antibiotic era), cardiovascular and CNS tertiary complications were major causes of death; with modern treatment access, syphilis-specific mortality is low in treated populations but remains an important contributor to stillbirth and neonatal mortality in undertreated maternal populations (congenital syphilis carries substantial stillbirth/neonatal-death risk — up to 40% in untreated pregnancies).
- **Morbidity/disability outcomes:** Once established, tertiary structural damage (aortic aneurysm, tabetic sensory/motor deficits, sensorineural hearing loss, dental/skeletal stigmata of congenital disease) is generally **not reversed** by antimicrobial treatment — treatment halts progression and clears the organism but does not repair existing scarring/aneurysmal dilation, underscoring the outsized prognostic value of early detection.
- **Complications:** aortic rupture/dissection, congestive heart failure from aortic regurgitation, stroke (meningovascular neurosyphilis), progressive dementia (general paresis), blindness (ocular syphilis, untreated interstitial keratitis), permanent hearing loss, and — in HIV-coinfected patients — accelerated/atypical courses with higher risk of neurologic involvement.
- **Recovery potential:** High for early-stage disease treated promptly; poor for established tertiary structural or neurologic damage, where the goal of treatment shifts from cure-with-recovery to halting further progression.
- **Prognostic factors:** stage at diagnosis/treatment (dominant factor), HIV coinfection status, gestational timing of maternal treatment (for congenital disease), and — for treatment-response monitoring — the trajectory of nontreponemal titers.
- **Serofast state:** a subset of adequately treated patients retain persistently reactive (non-declining) nontreponemal titers ("serofast") without evidence of treatment failure or reinfection; this is an area of ongoing immunologic research (linked in some studies to HLA-DR+CD8+ T-cell subset frequency, §4).

Sources: [Congenital and Maternal Syphilis — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537087/); [Syphilitic aortitis and its complications in the modern era](https://pubmed.ncbi.nlm.nih.gov/27982548/); [Clinical/immunological characteristics of HIV/syphilis co-infected patients](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2023.1327896/full)

---

## 12. Treatment

**Pharmacotherapy (first-line):**
- **Penicillin G**, administered parenterally, is the treatment of choice for **all stages** of syphilis; the specific preparation, dose, and duration depend on stage:
  - Primary/secondary/early-latent: **Benzathine penicillin G** 2.4 million units IM as a single dose.
  - Late-latent/unknown-duration/tertiary (non-neurologic): benzathine penicillin G 2.4 million units IM weekly × 3 doses.
  - Neurosyphilis/ocular/otosyphilis: **Aqueous crystalline penicillin G** IV (continuous infusion or divided doses) for 10–14 days (or aqueous procaine penicillin + probenecid as an alternative).
  - Congenital syphilis: aqueous crystalline penicillin G IV (or procaine penicillin IM) for 10 days.
  - **Critical note (per CDC guidance):** neither oral penicillin preparations nor a benzathine+procaine penicillin combination are considered adequate therapy for syphilis at any stage.
- **Penicillin-allergic patients:** doxycycline (100 mg PO BID × 14 days for early syphilis, longer for late-stage) is the principal alternative for non-pregnant patients; **penicillin desensitization is required in pregnancy** and for neurosyphilis, since doxycycline/tetracyclines are not recommended in pregnancy and alternative regimens are less well validated.
- **Azithromycin:** historically used as an alternative but now compromised in many regions by 23S rRNA (A2058G/A2059G) resistance mutations (§4); generally not recommended as first-line where resistance prevalence is unknown or high.
- **Ceftriaxone:** an alternative under investigation/select use, particularly for neurosyphilis in penicillin-allergic patients, though evidence base is less robust than for penicillin.

**Pharmacogenomics:** No well-established pharmacogenomic (e.g., CPIC-tier) gene–drug interaction is documented for syphilis therapy; penicillin allergy assessment/desensitization is an immunologic (not pharmacogenomic) consideration.

**The Jarisch-Herxheimer reaction:** An acute febrile reaction (fever, headache, myalgia, sometimes transient worsening of lesions/rash) occurring within 24 hours of initiating *any* effective syphilis therapy (a treatment reaction to rapid spirochete lysis and endotoxin-like release, **not** a penicillin allergy). Reported incidence in early syphilis ranges from ~8% to 56% depending on the study; most frequent in early (high-organism-burden) stages. Management is supportive (antipyretics), though antipyretics have not been proven to *prevent* the reaction; patients should be counseled about it before treatment. Comparative data (azithromycin vs. benzathine penicillin G) in HIV-positive patients with early syphilis have specifically examined reaction rates by regimen (PMC4150017), and a JAMA Network Open secondary analysis further characterized Jarisch-Herxheimer incidence after benzathine penicillin G in a randomized trial of adults with early syphilis (2025).

**Advanced/experimental therapeutics:** No gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy applies to syphilis treatment (bacterial infection, not a genetic/oncologic/immune-dysregulation disease in the classical sense) — pharmacotherapy (antibiotics) and, in tertiary disease, supportive/surgical management (e.g., aortic aneurysm repair, valve replacement) are the relevant categories.

**Surgical/interventional:** aortic aneurysm repair or aortic valve replacement for advanced cardiovascular syphilis with hemodynamically significant regurgitation or aneurysmal disease; coronary revascularization (PCI) for ostial stenosis (case reports document PCI for syphilitic coronary ostial stenosis).

**Treatment monitoring/outcomes:** Serial quantitative nontreponemal titers (RPR/VDRL) at 6, 12, and 24 months to confirm adequate treatment response (target: ≥4-fold titer decline); failure to decline appropriately, or a 4-fold titer rise, suggests treatment failure or reinfection and warrants HIV testing and CSF evaluation for occult neurosyphilis.

**NCIT term suggestions (verify against `ncit` OAK adapter):** NCIT:C15986 Pharmacotherapy (generic action term) with `therapeutic_agent` bound to CHEBI (e.g., benzylpenicillin CHEBI:18208, doxycycline CHEBI:50845, azithromycin CHEBI:2955, ceftriaxone CHEBI:3508 — verify exact CHEBI IDs); NCIT:C15329 Surgical Procedure for aneurysm repair/valve replacement; a dedicated NCIT term for penicillin desensitization procedure should be looked up specifically.

Sources: [CDC STI Treatment Guidelines — Syphilis](https://www.cdc.gov/std/treatment-guidelines/syphilis.htm); [Updating the CDC's treatment guidelines: Syphilis](https://www.contemporaryobgyn.net/view/updating-cdcs-treatment-guidelines-syphilis); [Jarisch-Herxheimer reaction, HIV-positive patients, azithromycin vs benzathine penicillin G](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4150017/); [Jarisch-Herxheimer Reaction After Benzathine Penicillin G — JAMA Network Open](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2830226); [NIH HIV.gov Syphilis OI Guidelines](https://clinicalinfo.hiv.gov/en/guidelines/hiv-clinical-guidelines-adult-and-adolescent-opportunistic-infections/syphilis)

---

## 13. Prevention

- **Primary prevention:** condom use (partial protection), risk-reduction counseling, partner notification/treatment ("expedited partner therapy" in many U.S. jurisdictions), and — newly (2024 CDC guidance) — **doxycycline post-exposure prophylaxis (doxy-PEP)**: 200 mg doxycycline self-administered within 72 hours of condomless sex, recommended for MSM and transgender women with a bacterial STI diagnosis in the prior 12 months, following shared decision-making; trials show >70% reduction in incident syphilis/chlamydia and ~50% reduction in gonorrhea. Ongoing need should be reassessed every 3–6 months alongside repeat bacterial-STI testing at exposed anatomic sites.
- **No vaccine currently exists.** Vaccine development is an active research area centered on the small repertoire of surface-exposed, immunogenic outer-membrane proteins (OMPs; e.g., FadL orthologs TP0856/TP0858, BamA/TP0326) identified through structural modeling of the *T. pallidum* OMP repertoire; the rabbit model remains the key preclinical platform, and manufacturing/design alignment challenges for a subunit OMP vaccine were reviewed in 2024 (Vaccine journal/Taylor & Francis).
- **Secondary prevention (screening/early detection):** USPSTF Grade A universal prenatal syphilis screening (early in pregnancy, and at first opportunity if missed); routine/periodic screening in higher-incidence populations (MSM, people with HIV) per CDC guidance; reverse or traditional serologic algorithms for case detection (§10).
- **Tertiary prevention:** prompt treatment of latent syphilis to prevent progression to tertiary disease; monitoring and early intervention for neurosyphilis/ocular/otosyphilis in at-risk (especially HIV-positive) patients to prevent permanent neurologic, visual, or auditory sequelae.
- **Congenital-syphilis-specific prevention:** the single highest-yield intervention is ensuring pregnant people receive early, adequate prenatal care with syphilis screening and — if positive — timely, stage-appropriate penicillin treatment; CDC/USPSTF analyses estimate ~90% of 2023's record U.S. congenital syphilis cases were preventable through this pathway.
- **Public health interventions:** partner services/contact tracing, expedited partner therapy, community-based outreach and mobile testing in underserved/high-incidence areas, and — for populations with documented healthcare-access disparities (e.g., Native American communities bearing the steepest recent rise in maternal syphilis) — targeted prenatal-care-access programs.
- **Genetic/prenatal counseling:** not applicable in the classical genetic-counseling sense (non-heritable disease), though maternal-fetal medicine counseling regarding transmission risk and treatment timing during pregnancy is directly analogous in clinical workflow.

Sources: [CDC Clinical Guidelines on Doxycycline PEP, 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11166373/); [CDC Doxy-PEP for STI Prevention](https://www.cdc.gov/sti/hcp/doxy-pep/index.html); [Full article: Syphilis vaccine development — aligning design with manufacturing](https://www.tandfonline.com/doi/full/10.1080/21645515.2024.2399915); [USPSTF universal prenatal syphilis screening reaffirmed](https://www.pamedsoc.org/home/news-resources/pamed-news/articles/uspstf-reaffirms-universal-syphilis-screening-in-pregnancy); [CIDRAP — Task force recommends prenatal syphilis screening amid growing crisis](https://www.cidrap.umn.edu/sexually-transmitted-infections/task-force-recommends-prenatal-syphilis-screening-amid-growing)

---

## 14. Other Species / Natural Disease

- **Taxonomy of the pathogen and its relatives:** Three recognized pathogenic subspecies of *T. pallidum* cause distinct human diseases — **subsp. *pallidum*** (venereal syphilis, the subject of this report), **subsp. *pertenue*** (yaws, a non-venereal, primarily pediatric, tropical skin/bone treponematosis), and **subsp. *endemicum*** (bejel/endemic syphilis, arid-region non-venereal transmission). These are genomically very closely related but clinically and epidemiologically distinct — an important curation boundary (do not conflate their MONDO/ICD entries).
- **Natural disease in non-human primates:** Multiple sub-Saharan African non-human primate species (e.g., sooty mangabeys in Taï National Park, Côte d'Ivoire, and others across 11+ sites) are naturally infected with *T. pallidum* subsp. *pertenue*, presenting with orofacial and genital lesions. Genomic comparison of human and non-human-primate-derived TPE strains found **no consistent genomic distinctness** between them — i.e., NHP and human yaws-causing strains are not genomically differentiated as separate lineages, though phylogeographic structuring by geography has been documented, and interspecies transmission between NHPs and humans appears rare.
- **Venereal syphilis (subsp. *pallidum*) is considered essentially human-restricted** — unlike yaws/bejel, no robust sylvatic/zoonotic reservoir is established for venereal syphilis; NHP treponemal disease surveillance to date centers on the pertenue (yaws) subspecies.
- **Veterinary relevance:** No naturally occurring venereal-syphilis-equivalent disease is recognized in domestic companion animals; the veterinary/zoonotic relevance of *T. pallidum* biology is chiefly through the NHP yaws reservoir as a public-health consideration for yaws-eradication programs (WHO), not through companion-animal disease.
- **Comparative pathology:** the shared genomic backbone across subspecies, combined with divergent tissue tropism (skin/bone in yaws vs. genital/systemic/neurologic in venereal syphilis), makes *T. pallidum* an instructive case of subspecies-level phenotypic divergence from near-identical genomes — a point of active research interest for understanding what genomic elements (if any) determine tissue tropism and transmission route.

Sources: [Geographically structured genomic diversity of non-human primate-infecting T. pallidum subsp. pertenue](https://pubmed.ncbi.nlm.nih.gov/33125317/); [Genomes of the yaws bacterium... not genomically distinct — PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0011602); [Genetics of human and animal uncultivable treponemal pathogens](https://pubmed.ncbi.nlm.nih.gov/29578082/); [Strain diversity of T. pallidum subsp. pertenue in African NHPs — Scientific Reports](https://www.nature.com/articles/s41598-019-50779-9)

---

## 15. Model Organisms

- **Rabbit model (the gold-standard model):** *T. pallidum* subsp. *pallidum* cannot be reliably maintained in continuous axenic culture, so the **New Zealand White rabbit intratesticular/intradermal infection model** remains the principal in vivo experimental platform for propagating the organism and studying pathogenesis, immune response, and vaccine candidates. Recent work using this model directly tested a **TprK-antigenic-variation-impaired mutant strain**, which was shown to be attenuated relative to wild type — direct in vivo evidence linking TprK diversification to virulence/persistence (bioRxiv 2023.01.18.524629 / PMC10063172).
- **Vaccine antigen validation in rabbits:** extracellular loops of the FadL-ortholog outer-membrane proteins TP0856 and TP0858 were shown to elicit IgG antibody and antigen-specific B-cell responses in the rabbit model, supporting their candidacy as syphilis subunit-vaccine antigens (mBio, PMC/journals.asm.org 10.1128/mbio.01639-22).
- **Model recapitulation and limitations:** The rabbit model recapitulates chancre formation, dissemination, and (with intratesticular inoculation) orchitis as a surrogate readout of infection/immunity, and has been indispensable for genotype-phenotype (e.g., TprK, OMP) studies since the organism cannot be genetically manipulated and grown at scale outside a host. Its principal limitation is imperfect recapitulation of the full human multi-decade natural history (tertiary cardiovascular/neurologic disease, congenital transmission) within a tractable experimental timeframe, and species differences in immune system architecture relative to humans.
- **In vitro / cell-based systems:** Historically no robust continuous in vitro culture system existed; specialized co-culture systems (with mammalian cells) developed in the mid-2010s allow short-term propagation and are increasingly used to supplement (not replace) the rabbit model for genomic/proteomic and drug-susceptibility work, though this search did not surface a specific 2023–2024 primary reference for routine use of such systems in syphilis pathogenesis research — flagged as a `HUMAN_MODEL_MISMATCH`-relevant gap for curation, since in vitro-cultured organism behavior relative to the classic rabbit/human correlation is still being established.
- **No standard genetically engineered (knockout/transgenic) mouse model of syphilis exists**, reflecting both the organism's obligate-host-restricted biology and the practical difficulty of genetically manipulating an uncultivable pathogen; this is a further notable gap relative to genetic-disease model-organism resources (no MGI/IMPC knockout entries are relevant here, since the "gene" of interest is pathogen-, not host-, encoded).
- **Resources:** No dedicated syphilis-specific model-organism database exists analogous to MGI/ZFIN/FlyBase for host-genetic disease models; primary sourcing for rabbit-model syphilis research is the peer-reviewed literature (PubMed/PMC) and specialized STI-research consortia rather than a curated model-organism repository.

Sources: [TprK-impaired T. pallidum attenuated in rabbit model of syphilis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10063172/); [Extracellular Loops of FadL Orthologs TP0856/TP0858 elicit IgG in rabbit model — mBio](https://journals.asm.org/doi/full/10.1128/mbio.01639-22); [Structural Modeling of T. pallidum OMP Repertoire — road map for vaccine development](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8407342/)

---

## Curation Notes for dismech Integration

- **Ontology terms flagged "(verify)" above must be confirmed via `runoak`/OAK against HP, GO, CL, UBERON, CHEBI, NCIT, and MONDO before being written into any `term:` block** — several IDs in this report reflect strong-but-not-100%-certain recall and are exactly the class of claim the dismech anti-hallucination validation stack (`just validate-terms`) is designed to catch. Treat every ID above as a *lead*, not ground truth, per the repo's own DR-output guidance.
- **PMIDs actually surfaced with confidence during this research** (safe starting points for `just fetch-reference`): 40708500, 27721440 (older PMID, review still current), 25890619, 36776779, 35819903, 35977144, 33125317, 29578082, 27982548, 18192791, 15186410, 33219164, 29451611, 22670010. Several other claims above are sourced to non-PMID URLs (CDC/USPSTF/PMC full-text pages without a captured PMID) — these should be re-resolved to a PMID/DOI where a quotable snippet is needed for dismech evidence items.
- **Structural sources applicable:** given the disease's clinical-guideline-heavy evidence base, `ORPHA:` and `NCIT:` structured-source citation (per this repo's framework) may be more efficient than literature PMIDs for several treatment/epidemiology claims; an Orphanet entry for congenital syphilis specifically should be checked.
- **Mechanism-module fit:** syphilis' pathophysiology (obliterative endarteritis as a shared lesion across chancre, gumma, and tertiary aortitis; granulomatous gumma formation) is a strong candidate for `conforms_to: granuloma_formation` (gummas) and shows thematic overlap with `atherogenesis`/`thrombogenesis`-adjacent vascular-injury logic, though syphilitic aortitis is mechanistically an infectious obliterative endarteritis rather than atherosclerotic — worth an explicit differentiating note if conformance is declared.
- **NEC risk:** "syphilis" as a search term is not itself eponym-ambiguous, but curators should take care to keep venereal syphilis (subsp. *pallidum*) cleanly separated from yaws/bejel (subsp. *pertenue*/*endemicum*) literature when sourcing PMIDs — a Named-Entity-Confusion risk specific to this pathogen's close subspecies relatives.