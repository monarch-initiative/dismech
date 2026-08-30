---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T17:52:38.503847'
end_time: '2026-08-20T17:56:56.616190'
duration_seconds: 258.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: McLeod Neuroacanthocytosis Syndrome
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
  web_search_requests: 12
  num_turns: 15
  total_cost_usd: 1.5874107000000002
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 19
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:8004674
  relevance_assessed: 18
  on_topic: 15
  off_topic: 1
  off_topic_references:
  - PMC:PMC8500837
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** McLeod Neuroacanthocytosis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **McLeod Neuroacanthocytosis Syndrome** covering all of the
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

# McLeod Neuroacanthocytosis Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview:** McLeod neuroacanthocytosis syndrome (McLeod syndrome, MLS) is an ultra-rare, X-linked, progressive multisystem disorder caused by loss-of-function variants in the *XK* gene at Xp21.1. It is one of the four "core" neuroacanthocytosis syndromes (alongside chorea-acanthocytosis/VPS13A disease, Huntington disease–like 2, and pantothenate-kinase-associated neurodegeneration) and is defined hematologically by the McLeod blood group phenotype — absence of the Kx erythrocyte antigen and markedly weakened expression of Kell blood group antigens — combined with red-cell acanthocytosis, compensated hemolysis, and a late-onset, Huntington's-disease-like neurodegenerative phenotype with prominent cardiac involvement (GeneReviews, [NBK1354](https://www.ncbi.nlm.nih.gov/books/NBK1354/), updated periodically; OMIM #300842).

**Key identifiers:**
- **OMIM disease:** #300842 (MCLEOD SYNDROME; MCLDS)
- **OMIM gene:** *314850 (KELL BLOOD GROUP PROTEIN, MCLEOD SYNDROME-ASSOCIATED; XK)
- **MONDO:** MONDO:0018945 (McLeod neuroacanthocytosis syndrome)
- **Orphanet:** ORPHA:35069 (McLeod syndrome)
- **GeneReviews:** [NBK1354](https://www.ncbi.nlm.nih.gov/books/NBK1354/) (Jung, Danek, Walker)
- **ICD-10:** part of G25.8/G25.9 movement-disorder codes and D75.8 (other hematologic); no dedicated ICD-10 code — typically coded under "other specified hemolytic anemias" / neuroacanthocytosis
- **MeSH:** "Neuroacanthocytosis" (D054874); "McLeod Syndrome" indexed as a supplementary concept
- **Disease Ontology:** DOID:0112107

**Synonyms:** McLeod phenotype; McLeod neuroacanthocytosis syndrome (MLS); XK-related neurodegenerative disease; Kell/McLeod syndrome; X-linked chorea-acanthocytosis (older, discouraged term — risks conflation with autosomal-recessive VPS13A disease).

**Evidence base:** Predominantly aggregated disease-level literature (GeneReviews synthesis; OMIM; multi-decade case series and pedigree reports from the international neuroacanthocytosis registries, e.g., Danek et al. and Jung et al.), supplemented by individual case reports/case series (typically single or small pedigrees) and a handful of molecular/cell-biology studies in patient-derived cells and mouse models. There is no large EHR-derived cohort given the extreme rarity (~250 published cases worldwide).

---

## 2. Etiology

**Disease causal factor:** MLS is a monogenic disorder — **loss-of-function pathogenic variants in *XK*** (Xp21.1) are both necessary and sufficient to cause the phenotype. No environmental or infectious trigger is implicated in disease causation itself (though environmental/pharmacologic factors modulate symptom expression — see below).

**Genetic risk factors:**
- Hemizygous pathogenic *XK* variants in males: nonsense, frameshift, splice-site, and missense variants, as well as partial/whole-gene deletions, account for the full mutational spectrum (~90% intragenic variants, ~10% larger deletions per GeneReviews).
- Founding molecular genetics: Ho et al. (1994) isolated the *XK* gene by positional cloning after identifying a 50-kb genomic deletion in patients with the McLeod phenotype, describing XK as "a novel membrane transport protein" (Ho M, Chelly J, Carter N, Danek A, Crocker P, Monaco AP. *Isolation of the gene for McLeod syndrome that encodes a novel membrane transport protein.* Cell. 1994;77(6):869–880. PMID:[8004674](https://pubmed.ncbi.nlm.nih.gov/8004674/)).
- **Contiguous gene deletion syndrome:** Larger Xp21.1 deletions that remove *XK* together with neighboring genes produce combined phenotypes — most notably with *CYBB* (X-linked chronic granulomatous disease), and less commonly with *DMD* (Duchenne muscular dystrophy) and *RPGR* (X-linked retinitis pigmentosa) — described as "Chronic granulomatous disease, the McLeod phenotype and the contiguous gene deletion syndrome" (PMID:[22111908](https://pubmed.ncbi.nlm.nih.gov/22111908/); PMC3267648).
- **Carrier/heterozygous females:** Because *XK* is X-linked, heterozygous females show mosaic Kell/Kx expression and partial acanthocytosis due to random X-chromosome inactivation, and are usually clinically unaffected. Rare "manifesting carriers" with chorea or late-onset cognitive decline have been reported and are attributed to **skewed X-inactivation** favoring inactivation of the wild-type allele.

**Environmental/behavioral risk factors:** None established as causal. However, exposure to **typical (first-generation) antipsychotics/neuroleptics** can precipitate or worsen extrapyramidal symptoms, rhabdomyolysis, or neuroleptic malignant syndrome–like reactions in MLS patients with subclinical myopathy — this is a recognized clinical management hazard rather than a disease-causing exposure (GeneReviews management section).

**Protective factors:** None specifically documented in the literature; no protective alleles or modifier variants have been characterized. Given the near-fully penetrant hemizygous male phenotype, protective genetic modifiers have not been systematically sought.

**Gene–environment interaction:** The principal interaction reported is pharmacogenomic/pharmacologic: subclinical myopathy (elevated CK) predisposes to drug-induced rhabdomyolysis, and dopamine-receptor-blocking agents used for chorea can unmask or worsen parkinsonian/myopathic features — this is a gene-drug interaction rather than a classical gene-environment susceptibility interaction.

---

## 3. Phenotypes

MLS phenotypes span hematologic, neurologic, neuromuscular, psychiatric, and cardiac domains, with a mean neurologic onset in the 30s–40s (range 18–61 years reported; some series cite 25–60).

### Hematologic (laboratory abnormalities)
| Phenotype | Frequency | Onset | HPO suggestion |
|---|---|---|---|
| Acanthocytosis (red cell) | Virtually all affected males (8–30% acanthocytes on smear) | Present from birth/early, often incidental | HP:0001927 (Acanthocytosis) |
| Compensated hemolysis without overt anemia | Nearly universal | Lifelong | HP:0001878 (Hemolytic anemia) — used cautiously since often compensated |
| Weakened Kell antigen expression / absent Kx antigen | Diagnostic, 100% | Congenital | (blood-group phenotype; no dedicated HPO term — describe in `notes`) |
| Elevated serum creatine kinase (CK) | Reported in ~100% of examined males, up to 4,000 U/L | From young adulthood | HP:0003236 (Elevated CK) |

### Neurological — movement disorder
- **Chorea** (choreiform/choreoathetotic movements): presenting symptom in ~30%, eventually present in ~95% of cases over the disease course. HPO: HP:0002072 (Chorea).
- Occasional orofacial dyskinesia, dystonia, tics, and parkinsonism reported in subsets.
- **Seizures**: presenting feature in ~20%, developing in up to 40% over time; typically generalized tonic-clonic. HPO: HP:0001250 (Seizure) / HP:0002069 (Generalized tonic-clonic seizures).

### Neuromuscular
- **Areflexia/hyporeflexia** from subclinical sensorimotor axonal peripheral neuropathy — almost universal. HPO: HP:0001284 (Areflexia); HP:0007141 (Axonal degeneration).
- **Muscle weakness/atrophy** (predominantly neurogenic, with myopathic features) in ~50%. HPO: HP:0003324 (Generalized muscle weakness); HP:0003202 (Skeletal muscle atrophy).
- Severe myopathy has been described as an atypical presentation ("McLeod myopathy revisited: more neurogenic and less benign," PMID:[18055495](https://pubmed.ncbi.nlm.nih.gov/18055495/)).

### Cognitive/Psychiatric
- **Cognitive decline**, frontal-executive type deficits in ≥50% of patients over the disease course. HPO: HP:0002354 (Memory impairment), HP:0002354/HP:0000726 (Dementia).
- **Psychiatric manifestations** are the initial manifestation in ~20% and develop in ~80% overall — personality change, depression, anxiety, obsessive-compulsive symptoms, and bipolar-spectrum disorder. HPO: HP:0000708 (Behavioral abnormality); HP:0000716 (Depressivity); HP:0000722 (Obsessive-compulsive behavior).

### Cardiac
- **Dilated cardiomyopathy** develops in ~60% of patients over time and is the leading cause of premature death. HPO: HP:0001644 (Dilated cardiomyopathy).
- **Atrial fibrillation**, **ventricular tachycardia**, sudden cardiac death. HPO: HP:0005110 (Atrial fibrillation); HP:0004756 (Ventricular tachycardia); HP:0001645 (Sudden cardiac death).
- Cardiac MRI: focal late gadolinium enhancement and interstitial fibrosis (structural correlate).

### Hepatosplenomegaly
- Reported as part of the "classic" multisystem phenotype, related to chronic hemolysis. HPO: HP:0001433 (Hepatosplenomegaly).

**Progression/severity:** Slowly progressive over decades; disease duration from diagnosis to death averages ~21 years, mean age at death 53 (range 31–69). Basal ganglia (caudate) volumes correlate inversely with disease duration on longitudinal MRI.

**Quality of life:** Not systematically studied with formal instruments (EQ-5D/SF-36) in the literature reviewed; qualitative descriptions emphasize progressive loss of independence from chorea, cognitive decline, and psychiatric morbidity, plus cardiac-related functional limitation. Suicide is a documented cause of death, underscoring psychiatric-driven QoL burden.

---

## 4. Genetic/Molecular Information

**Causal gene:** *XK* (HGNC:12811; NCBI Gene ID 7504; Xp21.1). OMIM gene *314850.

**Gene product:** The XK protein is a 444-amino-acid, 10-transmembrane-domain integral membrane protein belonging to the XK-related (XKR) family, structurally resembling a membrane transporter/lipid scramblase. It is covalently linked via a single disulfide bond to the Kell glycoprotein (encoded by *KEL* on chromosome 7q34, a 93-kDa type II membrane glycoprotein with endothelin-3-converting enzyme/zinc endopeptidase activity) to form the Kell-XK complex on the erythrocyte membrane (PMID:[10895256](https://pubmed.ncbi.nlm.nih.gov/10895256/), "Kell, Kx and the McLeod syndrome").

**Molecular function (recently clarified):** XK is a **Ca²⁺-activated phospholipid scramblase** and functions as an obligate partner of **VPS13A** (chorein, the gene mutated in autosomal-recessive chorea-acanthocytosis). XK forms a complex with VPS13A at ER–plasma-membrane contact sites, and when overexpressed relocalizes VPS13A from lipid droplets to ER subdomains — providing a direct molecular link between the two major neuroacanthocytosis syndromes (Park & Neiman, "XK is a partner for VPS13A: a molecular link between Chorea-Acanthocytosis and McLeod Syndrome," PMID:[32845802](https://pubmed.ncbi.nlm.nih.gov/32845802/); and PMC9436381, "A partnership between the lipid scramblase XK and the lipid transfer protein VPS13A at the plasma membrane"). XK residues Arg222 and Glu327, mutated in McLeod syndrome, are conserved across XKR family members including XKR8, the apoptotic phosphatidylserine scramblase (functions in a complex with basigin/BSG or neuroplastin/NPTN; PMID:[27503893](https://pubmed.ncbi.nlm.nih.gov/27503893/)).

**Pathogenic variant spectrum:**
- Missense, nonsense, frameshift indels, and canonical splice-site variants (Ho et al. 1994 identified point mutations at invariant 5′/3′ splice-donor residues).
- Gross deletions spanning part or all of the *XK* coding region (can extend into contiguous genes — see Etiology).
- ClinVar/ClinGen classification follows standard ACMG/AMP criteria; because *XK* loss-of-function is an established mechanism, truncating/null variants are typically classified pathogenic when segregating with the McLeod blood-group phenotype.
- **Functional impact category:** predominantly `LOSS_OF_FUNCTION` (complete or partial); no gain-of-function mechanism reported.
- **Allele frequency:** Given extreme rarity (prevalence <1–5 per 1,000,000; genereviews cites ~1:10,000,000), pathogenic *XK* variants are essentially absent from gnomAD/population databases; the McLeod blood group phenotype itself (not necessarily neurologic disease) has been noted incidentally in some blood-donor screening studies ("Spontaneously arising red cells with a McLeod-like phenotype in normal donors," PMC2794671) but true null *XK* alleles causing MLS remain private/family-specific.
- **Somatic vs germline:** Germline only; no somatic/mosaic oncologic relevance.

**Modifier genes:** None formally established; disease severity variability among affected males and manifesting carrier females is attributed largely to variant type (null vs. hypomorphic) and, in females, to X-inactivation skewing rather than to trans-acting modifier loci.

**Epigenetics:** The dominant epigenetic mechanism relevant to MLS is **X-chromosome inactivation (XCI) mosaicism** in heterozygous females — producing a bimodal (mosaic) Kell/Kx blood-group phenotype and variable, usually mild, hematologic/neurologic expression; skewed XCI toward inactivation of the normal allele explains rare manifesting female carriers.

**Chromosomal abnormalities:** Large Xp21.1 deletions removing *XK* plus *CYBB* (± *DMD*, ± *RPGR*) constitute a recognized **contiguous gene deletion syndrome** producing combined McLeod/CGD (±muscular dystrophy, ±retinitis pigmentosa) phenotypes (PMID:[22111908](https://pubmed.ncbi.nlm.nih.gov/22111908/); PMID:[3334897](https://pubmed.ncbi.nlm.nih.gov/3334897/), "Gene deletion in a patient with chronic granulomatous disease and McLeod syndrome: fine mapping of the Xk gene locus").

**Suggested ontology terms:**
- HGNC: XK (HGNC:12811), KEL (HGNC:6339, partner protein), VPS13A (HGNC:12175, functional partner), CYBB (HGNC:2578, contiguous-deletion partner)
- GO Molecular Function: phospholipid scramblase activity (GO:0017128); transmembrane transporter activity (GO:0022857)
- GO Biological Process: phospholipid translocation (GO:0045332); cellular response to calcium ion (GO:0071277)
- GO Cellular Component: plasma membrane (GO:0005886); endoplasmic reticulum-plasma membrane contact site (GO:0140268)

---

## 5. Environmental Information

MLS is a purely monogenic disorder; no environmental, occupational, or infectious factor contributes to disease **causation**. Environmental relevance is limited to two clinical-management contexts:

- **Pharmacologic exposure:** Typical antipsychotics/dopamine antagonists can precipitate rhabdomyolysis or worsen extrapyramidal symptoms in patients with subclinical myopathy; management guidance favors atypical antipsychotics (clozapine, quetiapine) or tetrabenazine over typical neuroleptics, and recommends avoiding long-term benzodiazepine use for seizures (GeneReviews management section).
- **Transfusion exposure:** Affected males who develop anti-Kx/anti-Km alloantibodies are at risk of severe hemolytic transfusion reactions if transfused with Kx-positive blood; Kx-negative (McLeod-phenotype) blood or banked autologous/homologous blood is required (PMID:[18167163](https://pubmed.ncbi.nlm.nih.gov/18167163/), "Transfusion support for a patient with McLeod phenotype without chronic granulomatous disease and with antibodies to Kx and Km").

No infectious agents are implicated, except indirectly in contiguous-deletion patients who also have chronic granulomatous disease (CGD) and are consequently susceptible to catalase-positive bacterial and fungal infections (*Aspergillus*, *Candida*) due to the co-deleted *CYBB*/NADPH oxidase gene — this is a feature of the CGD component of contiguous gene deletion, not of MLS/*XK* loss-of-function itself.

---

## 6. Mechanism / Pathophysiology

**Causal chain (proposed, from molecular lesion to clinical phenotype):**

1. **Molecular trigger:** Hemizygous loss-of-function *XK* variant → absent/reduced XK protein.
2. **Membrane complex disruption:** Loss of XK disrupts the disulfide-linked Kell-XK erythrocyte membrane complex, producing the McLeod blood group phenotype (weak Kell antigens, absent Kx) and destabilizing the erythrocyte cytoskeleton-membrane linkage.
3. **Erythrocyte pathology:** Abnormal membrane lipid scrambling/cytoskeletal anchoring → acanthocyte formation (spiculated red cells) → shortened red-cell lifespan → chronic compensated hemolysis, splenic sequestration, and (in the contiguous-deletion form) hepatosplenomegaly.
4. **Neuronal/muscular pathology:** Loss of XK-dependent, VPS13A-partnered phospholipid scrambling and lipid transfer at ER–plasma-membrane contact sites in neurons and myocytes → disrupted lipid homeostasis and membrane trafficking → selective vulnerability of the striatum (caudate > putamen > pallidum), peripheral motor/sensory axons, and skeletal/cardiac muscle.
5. **Basal ganglia dysfunction:** Progressive striatal neurodegeneration (caudate atrophy, decreasing striatal glucose metabolism on FDG-PET; PMID:[11254778](https://pubmed.ncbi.nlm.nih.gov/11254778/), "Reduction of striatal glucose metabolism in McLeod choreoacanthocytosis") → chorea, cognitive (frontostriatal) decline, and psychiatric symptoms, in a pattern resembling Huntington disease.
6. **Peripheral nerve/muscle pathology:** Axonal sensorimotor neuropathy (areflexia) and neurogenic ± myopathic muscle involvement (elevated CK, weakness/atrophy).
7. **Cardiac pathology:** Interstitial myocardial fibrosis (seen as late gadolinium enhancement on cardiac MRI) → dilated cardiomyopathy, arrhythmia (atrial fibrillation, ventricular tachycardia), and sudden cardiac death.

**Molecular pathways/cellular processes:**
- Phospholipid scrambling / membrane asymmetry maintenance (GO:0017128, phospholipid scramblase activity) — the central biochemical process disrupted.
- Lipid transfer at membrane contact sites (VPS13A/XK partnership; PMC9436381).
- Erythrocyte membrane skeleton–lipid bilayer coupling defect underlying acanthocyte morphology.
- Calcium-dependent T-cell phospholipid scrambling: Xk and Vps13a are jointly required for P2X7-receptor-mediated phosphatidylserine exposure and cell lysis in mouse splenic T cells, suggesting a broader immune/cell-death role for the XK-VPS13A axis (PMID via PNAS, "Requirement of Xk and Vps13a for the P2X7-mediated phospholipid scrambling and cell lysis in mouse T cells," 2022).

**Neuropathology:** A 2025 study proposed a new neuropathological grading system for MLS, confirming a **decreasing gradient of neurodegenerative severity from caudate nucleus to putamen**, correlating with the volumetric MRI findings (Reuss et al., "Neuropathological Characterisation of McLeod Syndrome With a Proposed New Grading System," *Neuropathology and Applied Neurobiology* 2025, PMID:[40898647](https://pubmed.ncbi.nlm.nih.gov/40898647/); PMC12547491).

**Tissue damage mechanisms:** Chronic mechanical/oxidative erythrocyte membrane stress (acanthocyte fragility) driving compensated hemolysis; progressive neurodegeneration via disrupted lipid/membrane trafficking rather than classic protein aggregation; myocardial interstitial fibrosis as the structural cardiac lesion.

**Biochemical abnormalities:** Elevated serum CK (muscle membrane leak marker); reduced/absent Kx and weak Kell antigen expression (diagnostic membrane biochemistry); reduced striatal glucose metabolism on FDG-PET (functional biomarker of neurodegeneration).

**Suggested ontology terms:**
- GO Biological Process: erythrocyte membrane organization (GO:0043249); regulation of striatal neuron death; neuron apoptotic process (GO:0051402)
- GO Cellular Component: erythrocyte plasma membrane; sarcolemma (GO:0042383)
- CL: erythrocyte (CL:0000232); medium spiny neuron (CL:1001474, principal striatal cell type); skeletal muscle fiber (CL:0000188); cardiac muscle cell (CL:0000746)
- UBERON: caudate nucleus (UBERON:0001873); putamen (UBERON:0001874); striatum (UBERON:0002435); myocardium (UBERON:0002349); peripheral nerve (UBERON:0002011)

**Omics:** No large-scale transcriptomic, proteomic, or metabolomic datasets specific to MLS were identified in this search (consistent with its extreme rarity); mechanistic insight to date derives from targeted cell-biology and biochemical studies of the XK-VPS13A partnership and from mouse T-cell scrambling assays rather than unbiased multi-omic profiling.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (basal ganglia — caudate, putamen, pallidum), peripheral nervous system (peripheral nerves), skeletal muscle, heart, erythrocytes/hematopoietic system.
- **Secondary:** Spleen and liver (hepatosplenomegaly from chronic hemolysis); in contiguous-deletion cases, phagocytes (CGD), retina (RP), and skeletal muscle (Duchenne).
- **Body systems:** Nervous system, musculoskeletal system, cardiovascular system, hematologic/immune system.

**Tissue/cell level:**
- Erythrocytes (acanthocytosis) — CL:0000232.
- Striatal neurons, particularly medium spiny neurons of the caudate nucleus — CL:1001474.
- Peripheral motor and sensory axons — axonal (not demyelinating) pathology.
- Skeletal muscle fibers (neurogenic atrophy ± myopathic change).
- Cardiac myocytes / interstitial fibroblasts (fibrosis).

**Subcellular level:**
- Plasma membrane (site of Kell-XK complex and phospholipid scrambling; GO:0005886).
- Endoplasmic reticulum–plasma membrane contact sites (site of VPS13A-XK lipid transfer; GO:0140268).
- Erythrocyte membrane skeleton.

**Localization:** Bilateral, symmetric basal ganglia involvement (predominantly caudate, decreasing gradient to putamen/pallidum); generalized (non-focal) peripheral neuropathy and myopathy; diffuse/patchy interstitial cardiac fibrosis.

**Suggested UBERON terms:** caudate nucleus (UBERON:0001873), putamen (UBERON:0001874), globus pallidus (UBERON:0002476), striatum (UBERON:0002435), spleen (UBERON:0002106), liver (UBERON:0002107), heart left ventricle (UBERON:0002084), peripheral nervous system (UBERON:0000010), skeletal muscle tissue (UBERON:0001134).

---

## 8. Temporal Development

**Onset:** Congenital/lifelong hematologic phenotype (acanthocytosis, weak Kell/absent Kx antigens present from birth, often detected incidentally on routine blood typing or crossmatch difficulty). Neurologic/neuromuscular/cardiac disease is **adult-onset**, typically emerging between ages 18–61 years, with the majority presenting before age 40 and mean onset in the 30s–40s. About 30% of affected males have no CNS/neuromuscular findings at the time their McLeod blood phenotype is first identified, but most develop symptoms on follow-up (Danek et al. 2001).

**Progression pattern:** Insidious, slowly progressive over years to decades — not episodic or relapsing-remitting. Chorea, cognitive decline, and psychiatric symptoms accumulate progressively; peripheral neuropathy (areflexia) and elevated CK are typically present from early adulthood, often preceding overt weakness. Cardiomyopathy and arrhythmia risk increase with disease duration (develops in ~60% over time).

**Disease stages:** No formally staged clinical classification exists (unlike, e.g., Huntington disease's Shoulson-Fahn staging), though the new neuropathological grading system (Reuss et al. 2025) proposes histopathologic staging correlating with the caudate>putamen>pallidum severity gradient and disease duration.

**Disease course:** Chronic, progressive, ultimately fatal — mean age at death 53 years (range 31–69); mean disease duration from diagnosis to death ~21 years. Cause of death includes cardiac tachyarrhythmia/sudden cardiac death, pneumonia, seizures, suicide, and sepsis.

**Remission:** None reported — MLS is not known to remit spontaneously; symptomatic (not disease-modifying) treatments can improve chorea and psychiatric symptoms but do not alter the underlying neurodegenerative or cardiac trajectory.

**Critical periods/intervention windows:** Early diagnosis via blood-group phenotyping (often incidental, pre-symptomatic) creates an opportunity window for **presymptomatic cardiac surveillance** (biennial Holter/echocardiography per GeneReviews) before overt cardiomyopathy develops, and for genetic counseling before neurologic onset.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Estimated <1 per 1,000,000 to as high as 1:10,000,000 depending on source; GeneReviews cites ~1:10,000,000. Orphanet epidemiology class would correspond to "<1/1,000,000" (BELOW_1_IN_1000000 in dismech's `PrevalenceClassEnum`).
- **Cases reported:** Only ~250 cases reported worldwide in the literature to date (extremely rare, ultra-orphan disease).
- **Incidence:** Not separately reported (X-linked, essentially a fixed birth-prevalence disorder given no evidence of reduced reproductive fitness before disease onset).

**Inheritance pattern:** **X-linked recessive.** Hemizygous males are affected; heterozygous females are typically unaffected carriers with mosaic (bimodal) Kell/Kx blood group expression due to random X-inactivation.

**Penetrance:** Neurologic/cardiac disease in hemizygous males appears **fully penetrant** given sufficient lifespan, though age-dependent (subclinical in a subset at the time of blood-group diagnosis, with most developing symptoms on follow-up). The hematologic (McLeod blood-group) phenotype is congenital and fully penetrant in hemizygous males.

**Expressivity:** Variable — age of neurologic onset, relative prominence of chorea vs. psychiatric vs. cardiac vs. myopathic features, and rate of progression vary between families and even within families, likely influenced by variant type (null vs. partial loss-of-function) and possibly X-linked contiguous deletion extent.

**Genetic anticipation:** Not reported; MLS is not a repeat-expansion disorder.

**Germline mosaicism:** Not specifically documented in the reviewed literature, though possible in principle for any X-linked disorder with de novo variants in a carrier mother.

**Founder effects:** Not established; the mutational spectrum is heterogeneous (private variants per family) rather than showing recurrent founder alleles.

**Consanguinity:** Not a relevant risk factor given X-linked recessive (not autosomal recessive) inheritance — consanguinity does not increase risk to sons of carrier mothers beyond the standard 50% transmission risk.

**Carrier frequency:** Not established in population databases given extreme rarity; pathogenic *XK* alleles are essentially absent from gnomAD.

**Population demographics:**
- **Affected populations:** No specific ethnic or geographic predilection reported; cases described across European, North American, and Asian cohorts (e.g., Japanese and Chinese case reports of novel *XK* variants).
- **Sex ratio:** Neurologic disease occurs "almost exclusively in boys and men" — i.e., markedly male-predominant, consistent with X-linked recessive inheritance; rare manifesting female carriers exist due to skewed X-inactivation.
- **Age distribution:** Hematologic phenotype from birth; neurologic disease onset concentrated in the 3rd–5th decades of life.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Peripheral blood smear:** Acanthocytosis (spiculated red cells), typically 8–30% of erythrocytes.
- **Blood bank serology:** McLeod blood group phenotype — weak/absent Kell antigen expression, negativity for Kx antigen — is the diagnostic hallmark, highly specific for MLS.
- **Serum creatine kinase (CK):** Elevated in essentially all affected males (up to 4,000 U/L), useful screening/monitoring biomarker.
- **Hemolysis markers:** Reticulocytosis, elevated LDH/bilirubin consistent with compensated hemolysis (usually without overt anemia).
- **Cardiac biomarkers/Holter ECG/echocardiography:** For surveillance and diagnosis of cardiomyopathy/arrhythmia.
- **EEG:** When seizures are suspected.
- **Cardiac MRI:** Late gadolinium enhancement/interstitial fibrosis pattern.
- **Brain MRI:** Caudate (> putamen > pallidum) atrophy; T2-hyperintense white matter changes in some cases.
- **FDG-PET:** Reduced striatal glucose metabolism, described as an early/obligate finding (PMID:[11254778](https://pubmed.ncbi.nlm.nih.gov/11254778/)).
- **Electrophysiology (NCS/EMG):** Confirms axonal sensorimotor peripheral neuropathy; can show neurogenic ± myopathic muscle changes.

**Genetic testing (per GeneReviews):**
1. McLeod blood group phenotyping **plus chromosomal microarray analysis** (to detect contiguous gene deletions, e.g., co-deletion of *CYBB*, *DMD*, *RPGR*).
2. McLeod blood group phenotyping **plus single-gene *XK* testing** — sequence analysis first (~60% detection), followed by gene-targeted deletion/duplication analysis if negative (~40% detection among remaining cases).
3. **Multigene panel or comprehensive genomic testing** (exome/genome sequencing) for undiagnosed symptomatic individuals presenting with chorea/neuroacanthocytosis of unclear cause.

**Differential diagnosis:**
- **Huntington disease:** Distinguished by absence of acanthocytosis and normal CK in HD; MLS and HD share the choreatic-cognitive-psychiatric triad ("Huntington's disease-like phenotype").
- **Chorea-acanthocytosis (VPS13A disease):** Autosomal recessive (vs. MLS's X-linked pattern); VPS13A disease features more prominent orofacial dyskinesia with habitual tongue/lip biting and self-mutilation, and generally less severe cardiac involvement than MLS.
- Other HD-phenocopies (HDL2, SCA17, PKAN/NBIA) should also be considered in the neuroacanthocytosis differential.

**Screening:** No population newborn or carrier screening program exists given extreme rarity; diagnosis typically follows either (a) incidental pre-transfusion blood-bank discovery of the McLeod phenotype, or (b) targeted workup of adult-onset chorea/neuroacanthocytosis. Cascade testing of at-risk female relatives (via blood-group phenotyping and/or *XK* sequencing) is appropriate for genetic counseling.

**Suggested NCIT/LOINC:** NCIT clinical-intervention terms for genetic testing (e.g., NCIT:C15709 Genetic Testing), gene panel sequencing, chromosomal microarray; LOINC codes for creatine kinase, reticulocyte count, and blood group phenotyping panels.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Mean age at death **53 years** (range 31–69). Disease duration from diagnosis to death averages **~21 years**. Causes of death include cardiac tachyarrhythmia/sudden cardiac death, pneumonia (likely aspiration-related in advanced disease), seizure-related death, suicide, and sepsis — indicating that **cardiac disease is the leading cause of premature death**, with psychiatric morbidity (suicide) a significant secondary contributor.

**Morbidity/function:** Progressive functional decline driven by the combination of chorea (motor disability), cognitive decline (executive dysfunction), psychiatric illness, and neuromuscular weakness. No formal disability/QoL instrument data were identified in the literature reviewed for this report.

**Disease course/complications:** Rhabdomyolysis risk (particularly if exposed to typical neuroleptics); transfusion-related hemolytic reactions in alloimmunized patients; progressive cardiomyopathy leading to heart failure, arrhythmia, and candidacy for ICD/pacemaker or transplantation; seizures.

**Prognostic factors:** Cardiac involvement (dilated cardiomyopathy, arrhythmia) is the strongest driver of mortality; basal ganglia (caudate) volume loss correlates with disease duration and likely with neurologic severity. Variant type (complete vs. partial loss-of-function) and, in the contiguous-deletion form, co-morbid CGD/CYBB status, likely modify overall prognosis, though this is not rigorously quantified in the literature.

**Prognostic biomarkers:** Serial cardiac MRI/echocardiography and Holter monitoring for early arrhythmia/cardiomyopathy detection; longitudinal caudate volumetric MRI as a neurodegeneration biomarker (used in small longitudinal cohorts, e.g., a 7-year follow-up of three MLS individuals showing decreasing caudate volumes).

---

## 12. Treatment

MLS has **no disease-modifying or curative therapy**; management is entirely symptomatic/supportive, following the multidisciplinary approach detailed in GeneReviews (Jung, Danek, Walker).

**Pharmacotherapy:**
- **Chorea:** Dopamine-receptor antagonists — **tiapride**, **clozapine**, **quetiapine** — or the VMAT2 inhibitor **tetrabenazine**; typical (first-generation) neuroleptics are specifically discouraged due to elevated risk of extrapyramidal side effects and precipitating myopathic/rhabdomyolysis complications in patients with subclinical myopathy.
  - NCIT: Pharmacotherapy (NCIT:C15986); therapeutic_agent candidates — tetrabenazine (CHEBI/NCIT), clozapine, quetiapine.
- **Seizures:** Standard anti-seizure medications selected per seizure type; **long-term benzodiazepine use is discouraged**.
- **Psychiatric symptoms:** Standard psychiatric pharmacotherapy (antidepressants, mood stabilizers) as clinically indicated, though no MLS-specific trial data exist.

**Cardiac management:**
- Standard guideline-directed dilated cardiomyopathy/heart failure therapy.
- **Prophylactic pacemaker or implantable cardioverter-defibrillator (ICD)** consideration given arrhythmia and sudden-death risk.
- **Cardiac transplantation** as an option in advanced cardiomyopathy.
- NCIT: Therapeutic Procedure (NCIT:C49236); Cardiac Pacemaker Implantation; Heart Transplantation (NCIT:C15289, Organ Transplantation).

**Hematologic/transfusion management:**
- Use of **Kx-negative (McLeod phenotype) blood**, or banked autologous/homologous blood, to avoid severe hemolytic transfusion reactions from anti-Kx/anti-Km alloantibodies.

**Supportive/rehabilitative care:**
- Physical, occupational, and speech therapy as needed for movement-disorder-related functional decline.
- Psychosocial support and psychiatric care given the high burden of depression, personality change, and suicide risk.

**Experimental/investigational therapy:** No gene therapy, cell therapy, or targeted molecular therapy specific to MLS was identified in the literature reviewed; given the loss-of-function *XK* mechanism and the recently defined XK-VPS13A lipid-scramblase partnership, **gene replacement or scramblase-restoring approaches** are conceptually plausible future directions but are not yet in clinical development based on available sources. No MLS-specific interventional trials were surfaced in this search (searches of ClinicalTrials.gov specific to MLS were not separately queried in this pass but no trial citations were found via the general literature search).

**Treatment strategy/surveillance schedule (per GeneReviews):**
- Cardiac: Holter ECG, echocardiography, and cardiac biomarkers **every 2 years** in individuals without known cardiac involvement (more frequently once disease is detected).
- Neurologic: EEG when seizures are suspected.
- Muscular: Regular serum CK monitoring, with heightened vigilance when neuroleptics are used.
- Psychosocial: Evaluation at each clinical visit.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable risk-factor or vaccination strategy exists for this monogenic disorder). The principal "primary prevention" tool is **genetic counseling and reproductive planning** for known carrier families (prenatal diagnosis, preimplantation genetic testing) given the X-linked recessive inheritance pattern and 50% transmission risk to sons of carrier mothers.

**Secondary prevention (early detection):** Presymptomatic identification via blood-bank serologic screening (McLeod phenotype often discovered incidentally during routine blood typing or difficult crossmatch) allows early genetic confirmation and initiation of the surveillance protocols above (biennial cardiac screening) **before** overt cardiomyopathy or neurologic symptoms develop — this is the single most actionable secondary-prevention strategy documented in the literature.

**Tertiary prevention:** Avoidance of typical neuroleptics to prevent rhabdomyolysis/extrapyramidal complications; use of Kx-negative blood products to prevent hemolytic transfusion reactions; proactive cardiac rhythm monitoring/device therapy to prevent sudden cardiac death.

**Genetic counseling:** Central to management — includes carrier testing for at-risk female relatives (with attention to X-inactivation-related variable expressivity), reproductive counseling, and family segregation studies to clarify pathogenicity of novel *XK* variants.

**Public health/screening programs:** No population-level newborn or carrier screening program exists for MLS given its extreme rarity; case detection remains opportunistic (via blood banking) or clinically triggered (via chorea/neuroacanthocytosis workup).

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring McLeod-syndrome-like disease has been documented in non-human species in the literature reviewed here (unlike some other neuroacanthocytosis-spectrum or lipid-membrane disorders that have recognized veterinary correlates). *XK* orthologs exist across mammals (used for the mouse knockout studies below), but no spontaneous veterinary McLeod phenotype was identified in this search.

**Comparative biology:** The XK-VPS13A functional partnership is evolutionarily conserved — XK residues mutated in human McLeod syndrome (Arg222, Glu327) are conserved across the broader XKR gene family (including XKR8), underscoring deep conservation of the phospholipid-scramblase mechanism across paralogs and likely across species.

**Transmission:** Not applicable — MLS is a purely genetic, non-communicable, non-zoonotic disorder.

---

## 15. Model Organisms

**Mouse models:**
- ***Xk* knockout mice:** Used to study the requirement of Xk (with its partner Vps13a) for **P2X7-receptor-mediated phospholipid scrambling and cell lysis in splenic T cells**, demonstrating that Xk is essential for ATP-induced phosphatidylserine exposure and cytolysis in CD25⁺CD4⁺ T cells — establishing an immunologic/cell-biology role for Xk beyond the erythrocyte membrane (PNAS 2022, "Requirement of Xk and Vps13a for the P2X7-mediated phospholipid scrambling and cell lysis in mouse T cells").
- ***Vps13a* knockout mice** (the chorea-acanthocytosis/VPS13A-disease model, studied comparatively because of the XK-VPS13A partnership): show **increased reticulocytes but notably do NOT reproduce acanthocytosis** on peripheral smear, and are valuable primarily for studying male infertility and select hematologic aspects of chorea-acanthocytosis rather than the full neurologic phenotype — illustrating a **fidelity gap (HUMAN_MODEL_MISMATCH-type limitation)** between rodent knockouts and the human acanthocytic/neurodegenerative phenotype (Yamamoto et al./Ueno et al., "Analysis of Brain, Blood, and Testis Phenotypes Lacking the Vps13a Gene in C57BL/6N Mice," 2024, PMC11277237; and "VPS13A knockdown impairs corticostriatal synaptic plasticity and locomotor behavior in a new mouse model of chorea-acanthocytosis").
- No dedicated *Xk*-knockout mouse study specifically modeling the full MLS neurodegenerative/cardiomyopathic phenotype (chorea, caudate atrophy, cardiomyopathy) was identified in this search — the existing *Xk*-KO literature focuses on T-cell/immune phospholipid scrambling rather than CNS or cardiac phenotyping, representing a **translational gap**: the immunologic Xk-KO mouse work has not yet been extended to systematically recapitulate the human basal-ganglia/cardiac phenotype.

**Cellular/in vitro models:**
- Patient-derived erythrocytes and lymphoblasts have been used to characterize the biochemical Kell-XK complex defect and acanthocyte morphology.
- Heterologous overexpression systems (human cell lines) were used to demonstrate the XK-VPS13A physical interaction and ER-relocalization phenotype (PMC9436381).
- Structural biology of the related **XKR8-Basigin scramblase complex** (cryo-EM structure, PMC8500837) provides a structural template for understanding XK's presumed scramblase mechanism, though the McLeod-specific XK structure itself has not yet been solved.

**Model limitations:** No model to date fully recapitulates the human triad of acanthocytosis + basal ganglia neurodegeneration + dilated cardiomyopathy. Available mouse data are fragmented across an immune/T-cell-focused *Xk*-KO line and a hematology/reproduction-focused *Vps13a*-KO line, neither of which is a complete phenocopy — this is a **HUMAN_MODEL_MISMATCH**-worthy gap for a future dismech entry: rodent Vps13a loss does not reproduce acanthocytosis despite being the direct genetic/molecular partner of XK, suggesting species-specific differences in erythrocyte membrane biology or compensatory mechanisms that limit translational inference from mouse hematologic data to human MLS.

**Resources:** MGI (Mouse Genome Informatics) records for *Xk* and *Vps13a* alleles; no dedicated *Xk*-KO strain repository entry with a validated MLS-recapitulating phenotype was surfaced in this search.

---

## Summary Table: Key Ontology Term Suggestions for KB Curation

| Category | Term |
|---|---|
| MONDO | MONDO:0018945 (McLeod neuroacanthocytosis syndrome) |
| OMIM | #300842 (disease); *314850 (XK gene) |
| Gene (HGNC) | XK (HGNC:12811); partner: KEL (HGNC:6339), VPS13A (HGNC:12175) |
| Inheritance (HP) | HP:0001417 (X-linked recessive inheritance) |
| Key phenotypes (HP) | HP:0001927 (Acanthocytosis), HP:0002072 (Chorea), HP:0001284 (Areflexia), HP:0001644 (Dilated cardiomyopathy), HP:0003236 (Elevated CK), HP:0001878 (Hemolytic anemia), HP:0001250 (Seizures), HP:0000708 (Behavioral abnormality) |
| GO | GO:0017128 (phospholipid scramblase activity), GO:0140268 (ER-PM contact site) |
| CL | CL:0000232 (erythrocyte), CL:1001474 (medium spiny neuron), CL:0000746 (cardiac muscle cell) |
| UBERON | UBERON:0001873 (caudate nucleus), UBERON:0002435 (striatum), UBERON:0002106 (spleen) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15289 (Organ Transplantation), NCIT:C15709 (Genetic Testing) |

---

## Sources

- [McLeod Neuroacanthocytosis Syndrome – GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1354/)
- [OMIM #300842 – MCLEOD SYNDROME](https://omim.org/entry/300842)
- [OMIM *314850 – XK gene](https://omim.org/entry/314850)
- [Kell, Kx and the McLeod syndrome – PubMed 10895256](https://pubmed.ncbi.nlm.nih.gov/10895256/)
- [Neuroacanthocytosis Syndromes – PMC3212896](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3212896/)
- [Isolation of the gene for McLeod syndrome – PubMed 8004674](https://pubmed.ncbi.nlm.nih.gov/8004674/)
- [Chronic granulomatous disease, the McLeod phenotype and the contiguous gene deletion syndrome – PubMed 22111908](https://pubmed.ncbi.nlm.nih.gov/22111908/)
- [Gene deletion in a patient with CGD and McLeod syndrome – PubMed 3334897](https://pubmed.ncbi.nlm.nih.gov/3334897/)
- [XK is a partner for VPS13A – PubMed 32845802](https://pubmed.ncbi.nlm.nih.gov/32845802/)
- [A partnership between XK and VPS13A – PMC9436381](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9436381/)
- [Xkr8 phospholipid scrambling complex – PubMed 27503893](https://pubmed.ncbi.nlm.nih.gov/27503893/)
- [Requirement of Xk and Vps13a for P2X7-mediated phospholipid scrambling – PNAS](https://www.pnas.org/doi/10.1073/pnas.2119286119)
- [Analysis of Brain, Blood, and Testis Phenotypes Lacking Vps13a – PMC11277237](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11277237/)
- [Reduction of striatal glucose metabolism in McLeod choreoacanthocytosis – PubMed 11254778](https://pubmed.ncbi.nlm.nih.gov/11254778/)
- [Neuropathological Characterisation of McLeod Syndrome – PubMed 40898647](https://pubmed.ncbi.nlm.nih.gov/40898647/)
- [McLeod myopathy revisited: more neurogenic and less benign – PubMed 18055495](https://pubmed.ncbi.nlm.nih.gov/18055495/)
- [Transfusion support for a patient with McLeod phenotype – PubMed 18167163](https://pubmed.ncbi.nlm.nih.gov/18167163/)
- [XK-Associated McLeod Syndrome: Nonhematological Manifestations and Relation to VPS13A Disease – Karger](https://karger.com/tmh/article/49/1/4/826976/XK-Associated-McLeod-Syndrome-Nonhematological)
- [McLeod neuroacanthocytosis syndrome – MedlinePlus](https://medlineplus.gov/download/genetics/condition/mcleod-neuroacanthocytosis-syndrome.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 15 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:8004674` *(abstract only)*: "a novel membrane transport protein"
  - closest text in source: "XK encodes a novel protein with structural characteristics of prokaryotic and eukaryotic membrane transport proteins"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC8500837` (1 mention) - The tertiary structure of the human Xkr8-Basigin complex that scrambles phospholipids at plasma membranes.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `phenotype`, `disease`, `mcleod`, `cardiac`, `mls`, `chorea`, `blood`, `gene`, `cell`, `syndrome`, `genetic`, `cardiomyopathy`, `kell`, `symptom`, `hematologic`, `caudate`, `neurologic`, `vps13a`, `psychiatric`, `risk`.