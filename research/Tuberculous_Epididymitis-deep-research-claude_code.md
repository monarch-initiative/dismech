---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T02:02:17.548666'
end_time: '2026-11-26T02:08:05.778705'
duration_seconds: 348.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Tuberculous Epididymitis
  mondo_id: MONDO:0001537
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 8
  num_turns: 16
  total_cost_usd: 0.9294852499999999
  session_id: 93368828-66bd-4b77-994d-44d03b06aab2
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 30
  retrieval_calls: 27
  assistant_text_blocks: 2
citation_count: 18
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 17
  validator_version: 0.8.0
term_validation:
  total_terms: 56
  verified: 52
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.019
  labels_checked: 30
  labels_matching: 16
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0001537
    reported_labels:
    - 'subsets: rare, gard_rare'
    - OLS4
    ontology_label: tuberculous epididymitis
  - term_id: DOID:1251
    reported_labels:
    - DOID
    ontology_label: tuberculous epididymitis
  - term_id: HP:0100845
    reported_labels:
    - testicular pain
    ontology_label: Anaphylactic shock
  - term_id: HP:0003565
    reported_labels:
    - 7/14 tested (50%)
    ontology_label: Elevated erythrocyte sedimentation rate
  - term_id: HP:0011227
    reported_labels:
    - 5/8 tested (62.5%)
    ontology_label: Elevated circulating C-reactive protein concentration
  - term_id: HP:0100639
    reported_labels:
    - 4.9% / 6.2% (Huang)
    ontology_label: Erectile dysfunction
  - term_id: UBERON:0001338
    reported_labels:
    - tunica vaginalis
    ontology_label: urethral gland
  - term_id: UBERON:0001300
    reported_labels:
    - scrotum and scrotal skin
    ontology_label: scrotum
  labels_variant: 6
  unresolved_terms:
  - CL:1000154
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  service_unreachable: 2
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tuberculous Epididymitis
- **MONDO ID:** MONDO:0001537 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Tuberculous Epididymitis** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

Bash network access isn't approved; I'll use WebSearch and the web-fetch agent.

I'm writing up the report now from the sources I've gathered.

# Tuberculous Epididymitis (MONDO:0001537): Disease Characteristics Report

**How I read the request:** Tuberculous epididymitis is an infectious disease, not a Mendelian one. **It has no causal human gene.** The cause is infection with organisms of the *Mycobacterium tuberculosis* complex (MTBC). That is mostly *M. tuberculosis*, and occasionally *M. bovis*, including the BCG strain given into the bladder. Sections about genes, variants, inheritance and genetic testing are therefore marked as not applicable.

**Limits of the sources:** PubMed pages and E-utilities could not be reached directly in this session. Abstracts and full text came through Europe PMC, PMC and web search. Quotes marked "verbatim" were retrieved in this session. Where only a search summary was available, I say so.

---

## 1. Disease Information

**Overview.** MONDO defines the disease as *"An urogenital tuberculosis involving a pathogenic inflammatory response in the epididymis"* (OLS4, MONDO:0001537; https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http://purl.obolibrary.org/obo/MONDO_0001537).
- The epididymis is the genital organ most often affected in male genital tuberculosis (TB).
- The disease often spreads to the testis, which is then called tuberculous epididymo-orchitis (TBEO).
- Urogenital TB as a whole is *"the second most frequent form of extrapulmonary tuberculosis"* (Figueiredo 2017, PMID 28087922).

**Identifiers** (all from the MONDO OLS4 record):

| Resource | ID |
|---|---|
| MONDO | MONDO:0001537 (subsets: rare, gard_rare) |
| DOID | DOID:1251 |
| GARD | 0022961 |
| ICD-9-CM | 016.4 (016.40–016.46) |
| ICD-11 foundation | 1092166548 |
| SNOMED CT | 83652003 |
| UMLS | C0152814 |
| MedGen | 509077 |
| Parent terms | MONDO:0004779 epididymitis (ICD-10-CM N45.1, MeSH D004823, NCIT C12328); MONDO:0006845 male genital tuberculosis (MeSH D014389 "Tuberculosis, Male Genital") |

- **OMIM / Orphanet:** none. This is not a Mendelian disorder.
- **ICD-10:** the MONDO term carries no direct ICD-10 cross-reference. In ICD-10 the condition is coded under A18.1 (tuberculosis of the genitourinary system). That code is my own mapping and was not confirmed by a source retrieved here.

**Synonyms.** MONDO lists none. Names used in the literature include epididymal tuberculosis, TB epididymitis, tuberculous epididymo-orchitis (TBEO), scrotal tuberculosis and genital tuberculosis of the epididymis (Huang 2021, PMID 34654377; Radiopaedia "scrotal tuberculosis", https://radiopaedia.org/articles/scrotal-tuberculosis).

**Source of evidence.** The evidence is aggregated at disease level. It comes from retrospective single-centre case series, case reports, imaging series and narrative reviews. There are no registries or EHR cohorts specific to this disease.

---

## 2. Etiology

**Causal factors.**
- **Infection:** MTBC organisms, mainly *M. tuberculosis*. *M. bovis* causes some cases, including after intravesical BCG for bladder cancer (Menke 2000, PMID 10772435; Okadome 2002, PMID 12056045; Mateos Colino 2003, PMID 12731446; Muttarak 2002, PMID 12060159).
- **Spread:** usually secondary to blood-borne spread from a lung focus, or to spread down the urinary tract from the kidney or prostate. Figueiredo writes: *"Starting with a pulmonary focus, 2 to 20% of patients develop urogenital tuberculosis through hematogenous spread"* (PMID 28087922).

**Risk factors.**
- **Earlier or concurrent TB elsewhere.** In Huang's series of 81 TBEO patients, 12.3% had a history of TB (lung 8, kidney 1, bone 1) and 7.4% had active lung TB on chest imaging (PMID 34654377, PMC8520285). Reviews report that more than half of men with male genital TB have lung and/or kidney TB (web review summary, PMC5422679).
- **HIV and other immunosuppression.** In a Thai series of 25 patients, 16% had HIV and one third had concurrent lung TB (Suankwan 2012, Southeast Asian J Trop Med Public Health; https://www.tm.mahidol.ac.th/seameo/2012-43-4/17-5170-21.pdf; PMID not retrieved).
- **Intravesical BCG therapy.** Epididymitis after BCG is rare. One source gives about 0.4% of treated patients (PMC6649823). Menke writes: *"The incidence of BCG-associated epididymoorchitis is rare"* (PMID 10772435). Recent instrumentation or catheterization and immunocompromise are listed as contributing factors (PMC3558260).
- **Age and sex.** By definition only males are affected. Figueiredo: *"predominant in males in their fourth and fifth decades"* (PMID 28087922).
- **Living in or coming from a high-TB-burden country.**
- **Genetic risk factors:** none described specifically for this disease. Host-susceptibility genes for TB in general (for example the IL-12/IFN-γ axis in Mendelian susceptibility to mycobacterial disease) were not searched for this site and are not documented for it.

**Protective factors.**
- **Genetic:** none documented.
- **Environmental:** preventing and treating TB infection, and finding and treating lung or kidney TB early. BCG vaccination protects mainly against severe childhood TB. No evidence specific to the epididymis was retrieved.

**Gene–environment interactions:** none documented for this disease.

---

## 3. Phenotypes

Frequencies come from Huang 2021 (n=81, PMID 34654377 / PMC8520285) unless another source is given.

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Scrotal swelling or mass | Sign | 58.0% (47/81); the main sign in most series | HP:0000045 (abnormality of the scrotum); scrotal swelling, if available |
| Scrotal or testicular pain | Symptom | 35.8% (29/81). Often painless or mildly painful; Viswaroop found painful swelling in 40% (PMID 16006701) | HP:0100845 (testicular pain) / scrotal pain |
| Enlarged, nodular epididymis | Sign / imaging | Nearly universal | Abnormal epididymis morphology (HP:0000033 group) |
| Testicular involvement (epididymo-orchitis) | Sign / imaging | 6/10 in Kim 1993 (PMID 8510282); 76.9% on ultrasound in Huang | Orchitis (HP:0100796) |
| Bilateral disease | Sign | 4.9% on exam (Huang); 12.5% (Viswaroop, PMID 16006701); 4/18 patients (Chung 1997, PMID 9282805) | — |
| Hydrocele | Sign | 12.3% (Huang); 12 of 22 hemiscrotums (Chung, PMID 9282805) | HP:0000034 (hydrocele testis) |
| Scrotal sinus tract | Sign | 1.2% (Huang); 4 of 22 hemiscrotums (Chung) | Cutaneous sinus tract (HP:0100621-type term) |
| Scrotal or epididymal abscess | Sign | 2.5% (Huang) | Abscess (HP:0025615) |
| Weight loss | Symptom | 13.6% | HP:0001824 |
| Fever | Symptom | 7.4% | HP:0001945 |
| Night sweats | Symptom | 1.2% | HP:0030166 |
| Dysuria / frequency / urgency | Symptom | 3.7% / 2.5% | HP:0100518 / HP:0100515 |
| Sterile pyuria | Lab | 27.2% | HP:0012085 (pyuria) |
| Microscopic hematuria | Lab | 9.9% | HP:0002907 |
| Raised ESR | Lab | 7/14 tested (50%) | HP:0003565 |
| Raised CRP | Lab | 5/8 tested (62.5%) | HP:0011227 |
| Anemia | Lab | 9.9% | HP:0001903 |
| Hypoalbuminemia | Lab | 14.8% | HP:0003073 |
| Extratesticular scrotal calcification | Imaging | 2 of 22 hemiscrotums (Chung) | — |
| Infertility / azoospermia | Late effect | Sterility 8.6% at follow-up (Huang) | HP:0000027 (azoospermia); HP:0000789 (infertility) |
| Erectile dysfunction / premature ejaculation | Late effect | 4.9% / 6.2% (Huang) | HP:0100639 |

- **Onset:** adult, with a mean age of 50.8 years (range 13–90) in Huang. The median was 32 years in the Indian series (PMID 16006701).
- **Course:** subacute to chronic and slowly progressive. Tuberculous abscesses had a *longer duration of symptoms and less scrotal tenderness* than pyogenic ones (Yang 2001, AJR 177:1131; summary via QxMD https://www.qxmd.com/r/11641187).
- **Quality of life:** no EQ-5D or SF-36 data were found. The main effects are on sexual function and fertility (Huang 2021).

---

## 4. Genetic / Molecular Information

- **Causal genes, pathogenic variants, modifier genes:** none in the host. This is an infectious disease.
- **ClinVar, gnomAD and ACMG variant classification:** not applicable.
- **Epigenetic findings and chromosomal abnormalities:** none reported.
- **Pathogen genetics:** relevant in practice.
  - Xpert MTB/RIF detects MTBC DNA and *rpoB* rifampicin-resistance mutations.
  - Species-specific PCR or whole-genome sequencing separates *M. bovis* BCG from *M. tuberculosis* in cases after BCG therapy (PMC6649823; Kyoto University case reports).
  - BCG strains are naturally resistant to pyrazinamide (general knowledge, not retrieved here). This matters when choosing drugs.

---

## 5. Environmental Information

- **Infectious agents:**
  - *Mycobacterium tuberculosis* (NCBITaxon:1773)
  - *Mycobacterium bovis* (NCBITaxon:1765), including BCG (NCBITaxon:33892)
- **Exposures:**
  - Exposure to people with infectious TB, especially in endemic countries.
  - Intravesical BCG therapy.
  - Unpasteurized milk, for zoonotic *M. bovis*.
- **Lifestyle factors** (general TB risk factors; no epididymis-specific data were retrieved): smoking, alcohol use, malnutrition and diabetes.
- **Toxins, radiation, pollution:** no data relevant to this disease.

---

## 6. Mechanism / Pathophysiology

**Causal chain.**
1. **Infection.** MTBC bacilli are inhaled and cause a primary lung infection, often latent. In the BCG pathway, live *M. bovis* BCG is instilled into the bladder instead.
2. **Spread.** Bacilli enter the blood and seed organs with a rich blood supply: the kidneys, prostate and epididymis (PMID 28087922; review summary PMC5422679). In the alternative branch, bacilli travel backward from infected urine or prostate down the vas deferens to the epididymis. This is the likely route after BCG and in kidney TB. It is inferred from clinical association rather than shown experimentally.
3. **Seeding.** Infection usually starts in the tail (cauda) of the epididymis, then spreads through the whole epididymis (PMC5960082 case review).
4. **Immune response.** Macrophages take up the bacilli, and a Th1/IFN-γ-driven cell-mediated response forms granulomas made of epithelioid histiocytes and Langhans giant cells.
5. **Tissue damage.** The granulomas undergo caseous necrosis, seen in 81/81 surgical specimens in Huang (PMID 34654377). This leads to an enlarged, mixed-echo epididymis, abscess formation and, when healing, fibrosis and calcification.
6. **Spread to the testis.** Disease extends directly from the epididymis to the testis, giving epididymo-orchitis. Isolated testicular TB is uncommon because the blood–testis barrier protects the testis (review summary PMC5422679). In the other direction, disease spreads outward to the tunica vaginalis and scrotal skin, causing hydrocele, abscess and draining scrotal sinuses (Chung, PMID 9282805).
7. **Obstruction and long-term effects.** Fibrosis or granulomas block the epididymis, vas or ejaculatory duct. This causes obstructive azoospermia or infertility, which can persist after successful drug treatment (PMC2684350; PMC5422679). Damage to the testis itself causes testicular loss, and chronic illness contributes to sexual dysfunction.
8. **Systemic effects.** In parallel, systemic inflammation causes weight loss, fever, anemia and raised ESR/CRP. Rarely the disease disseminates, for example to the psoas or adrenals, causing Addison disease (Skoutelis 2000, PMID 10879650).

**Checklist detail.**
- **Pathways.** Standard TB immunity applies: TLR2-mediated recognition of the bacteria, IL-12 → IFN-γ → macrophage activation, and TNF-dependent maintenance of granulomas. None of this has been studied in the epididymis specifically.
- **Cell types (CL):**
  - macrophage (CL:0000235)
  - epithelioid cell (CL:0000622-type term)
  - multinucleate giant cell (CL:0000647)
  - CD4+ T cell (CL:0000624)
  - epididymal principal cell (CL:1000154-type term)
  - spermatogenic cells in the testis (CL:0000586 germ cell)
- **GO biological processes:**
  - granuloma formation (GO:0002432)
  - inflammatory response (GO:0006954)
  - response to bacterium (GO:0009617)
  - type II interferon-mediated signaling (GO:0060333)
  - necrotic cell death (GO:0070265)
  - phagocytosis (GO:0006909)
- **Omics, single-cell, spatial or CRISPR data:** none found for this disease.

---

## 7. Anatomical Structures Affected

- **Primary site:**
  - epididymis (UBERON:0001301)
  - most often the tail (cauda epididymis, UBERON:0004630); head and body less often
- **Secondary sites:**
  - testis (UBERON:0000473)
  - tunica vaginalis (UBERON:0001338) and hydrocele
  - scrotum and scrotal skin (UBERON:0001300)
  - vas deferens (UBERON:0001000)
  - seminal vesicle (UBERON:0000998)
  - prostate (UBERON:0002367)
  - kidney (UBERON:0002113) and lung (UBERON:0002048) as associated foci
- **Body systems:** male reproductive system and urinary system.
- **Distribution in Huang 2021 (surgical series):** epididymis alone 38.3%, testis alone 28.4%, both 33.3%.
- **Laterality:**
  - usually unilateral; bilateral in 5–22% depending on the series (PMIDs 34654377, 16006701, 9282805)
  - bilateral involvement favors TB over non-tuberculous epididymitis (Radiopaedia)
  - in Huang, the right side was more common than the left on exam (33% vs 20%)
- **Subcellular level:** bacilli live inside macrophage phagosomes (GO:0045335) and lysosomes, and block phagosome maturation. This is general TB biology.

---

## 8. Temporal Development

- **Onset:** in adulthood, mostly in the 30s to 50s. Onset is insidious and subacute. It can present acutely and be mistaken for bacterial epididymitis.
- **Latency:** there can be years between the original infection and the scrotal disease. After BCG, epididymitis can appear long after treatment, in one report 35 months later. Menke concluded it *"should be considered a late complication"* (PMID 10772435).
- **Stages (descriptive, not formal):**
  1. early granulomatous epididymitis
  2. caseation and abscess
  3. spread to the testis and skin (sinus)
  4. healed fibrocalcific stage with obstruction
- **Remission:** treatment-induced. Viswaroop reported *"Anti TB treatment resulted in a complete response in 10 and partial response in 18"* (PMID 16006701). Spontaneous remission is not documented.
- **Window for intervention:** early diagnosis before abscess or sinus formation, and before damage to both sides, may preserve the testis and fertility. Muneer: *"Delay in diagnosis results in disease progression, irreversible tissue and organ damage"* (PMID 31548730).

---

## 9. Inheritance and Population

- **Inheritance, penetrance, anticipation, founder effects, carrier frequency:** not applicable.
- **Epidemiology:**
  - No population incidence for tuberculous epididymitis was found.
  - In proportional terms, 15–40% of TB cases are extrapulmonary, and urogenital TB is the second most common extrapulmonary form (Muneer 2019, PMID 31548730; Figueiredo 2017, PMID 28087922).
  - The epididymis is involved in about 22–55% of men with genitourinary TB (review summary, PMC5422679).
  - Viswaroop found 54 of 187 men with genitourinary TB had epididymal involvement (PMID 16006701).
  - MONDO tags the disease as "rare".
- **Geography:** mostly high-burden regions: South and Southeast Asia, China, Africa and South America. Series come from India, China, Thailand and Korea. In low-burden countries, cases occur in migrants and after BCG therapy.
- **Sex ratio:** 100% male by definition. Female genital TB is a separate entity.
- **Age:** wide range (13–90), with a peak at 30–50 (PMID 28087922; Gansu 47-case series via web summary).

---

## 10. Diagnostics

**Laboratory tests.**
- Urinalysis for sterile pyuria (27%).
- Early-morning urine for acid-fast bacilli (AFB) smear and mycobacterial culture. The yield is low: 0/16 positive in Huang, and *"10 showed no evidence of tuberculous infection in their urine"* in Ferrie (n=20, PMID 6683985).
- ESR and CRP.
- HIV testing.
- Interferon-gamma release assay (IGRA) or tuberculin skin test, which are supportive only.

**Molecular tests.**
- Xpert MTB/RIF or Ultra on tissue, pus or urine. Sensitivity against culture varies by specimen type. For pleural fluid, for example, it was *"49.5% (39.8 to 59.9)"* (Cochrane, Kohli 2021, PMID 33448348).
- PCR on tissue was positive in 55.8% in Huang.
- Combining urinary PCR with scrotal MRI *"allowed prompt diagnosis"* (Liu 2005, PMID 16110362).

**Imaging.**
- **Scrotal ultrasound with Doppler:**
  - An enlarged epididymis that is hypoechoic in 13 of 22 hemiscrotums, hyperechoic in 2 and mixed in 7 (Chung, PMID 9282805).
  - Patterns: diffusely heterogeneous, diffusely homogeneous, or nodular heterogeneous (Muttarak 2001, PMID 11373214; no abstract available).
  - An enlarged, heterogeneous epididymis helps separate TB from non-TB epididymitis (Kim 1993, PMID 8510282).
  - Tuberculous abscesses are larger and have less blood flow at their edge than pyogenic ones (Yang 2001, AJR; QxMD 11641187).
  - A 2024 nomogram combining ultrasound and clinical features was built to separate epididymal TB from non-TB epididymitis (PMC11220132).
- **CT/MRI:** CT showed infectious features in 87.8% in Huang.
- **Chest X-ray or CT** to look for lung TB.

**Pathology.**
- Caseating granulomas with Langhans giant cells (100% in Huang).
- AFB stain positive in 80.5% of surgical specimens.
- Fine-needle aspiration cytology (FNAC) is an option before surgery.
- Culture is the reference standard and gives drug-susceptibility testing.

**Genetic testing of the host:** not applicable (no host gene, panel, exome or CMA testing is indicated). Pathogen genotyping is useful for resistance and to identify BCG.

**Clinical criteria:**
- There are no formal criteria. Diagnosis rests on histology or microbiology.
- Before surgery, only 37% were correctly diagnosed as TBEO. In 34.6%, a tumor was suspected (Huang).

**Differential diagnosis:**
- **Bacterial (pyogenic) epididymitis:** acute and tender; responds to antibiotics.
- **Testicular tumor:** a lesion confined to the testis with a normal epididymis suggests cancer.
- **Brucella epididymo-orchitis**, which is endemic in overlapping regions.
- **Others:** testicular torsion or infarction, sarcoidosis, fungal infection, and granulomatous orchitis.

**Screening:** no screening of asymptomatic people. Figueiredo advises *"A systematic search for urogenital tuberculosis, regardless of symptoms"* in TB patients (PMID 18836557). Routine semen PCR for men with obstructive azoospermia is debated (J Hum Reprod Sci 2015, via web summary).

---

## 11. Outcome / Prognosis

- **Mortality:** low. In Huang there was 1 death (1.2%), from liver cirrhosis and unrelated to TB, and *"no recurrence was observed"* over a mean follow-up of 82 months (PMID 34654377).
- **Morbidity** (Huang):
  - loss of the testis: epididymo-orchidectomy in 64%
  - sterility 8.6%
  - erectile dysfunction 4.9%
  - premature ejaculation 6.2%
- **Infertility:** obstructive azoospermia can persist after cure (PMC2684350). Sperm retrieval with ICSI gives results similar to non-TB obstructive azoospermia (PMC3222923).
- **Complications:**
  - abscess
  - scrotal sinus or fistula
  - spread to the testis
  - spread to the other side
  - disseminated TB: psoas abscesses and Addison disease (PMID 10879650)
- **Prognostic factors:**
  - delay in diagnosis (PMID 31548730)
  - bilateral disease, which threatens fertility
  - abscess or sinus, which more often leads to surgery
  - HIV
  - drug resistance
- **Prognostic biomarkers:** none validated.

---

## 12. Treatment

**Drug treatment.**
- Standard first-line therapy:
  - isoniazid (CHEBI:6030; NCIT C574)
  - rifampicin (CHEBI:28077; NCIT C793)
  - pyrazinamide (CHEBI:45285; NCIT C772)
  - ethambutol (CHEBI:4877; NCIT C47518)
- Schedule: 2 months of all four, then 4 months of isoniazid and rifampicin.
- Duration: the ATS/CDC/IDSA 2016 guideline generally supports 6 months for most extrapulmonary sites (Nahid 2016, PMID 27516382). I could not retrieve its genitourinary-specific wording.
- In practice: 2–4 weeks of treatment before surgery and 6–12 months after surgery in Huang. A Gansu series used 3–6 months after surgery.
- After BCG: regimens omit pyrazinamide because BCG is naturally resistant to it (general knowledge, not retrieved here).
- Pharmacogenomics: NAT2 acetylator status affects isoniazid exposure and liver toxicity (general CPIC/PharmGKB knowledge, not retrieved here).
- NCIT intervention term: Antitubercular Agent (C281-type class).

**Surgery** (NCIT: Epididymectomy; Orchiectomy C15268):
- Indicated for:
  - abscess
  - sinus
  - a mass that does not respond to drugs
  - an uncertain diagnosis or suspected tumor
- In Huang: epididymectomy 33.3%, epididymo-orchidectomy 64.2%, orchiectomy 2.5%. The authors recommend *"triple therapy"* (chemotherapy + surgery + drugs) for advanced disease (PMID 34654377).
- In Gansu (n=47): epididymectomy 55.3%, epididymectomy plus orchiectomy 44.7%, with no recurrence.

**Supportive care and fertility:**
- pain relief
- fertility counseling
- sperm cryopreservation, or surgical sperm retrieval with ICSI

**Advanced therapies:** none apply (no gene, cell or RNA therapies). No clinical trials specific to this disease were found.

**Response:**
- Viswaroop: complete response in 10 and partial response in 18 with drugs alone (PMID 16006701).
- Recurrence after combined treatment is rare.
- Side effects are the standard ones for these drugs: liver toxicity, peripheral neuropathy (isoniazid) and optic neuritis (ethambutol).

---

## 13. Prevention

- **Primary prevention:**
  - TB control: case finding, contact tracing, and treatment of TB infection
  - BCG vaccination of infants, which mainly prevents severe childhood TB
  - pasteurization of milk to prevent *M. bovis*
  - aseptic, atraumatic bladder instillation of BCG, and not instilling after traumatic catheterization (PMC3558260)
- **Secondary prevention:**
  - Examine the genitourinary tract and urine of TB patients (PMID 18836557).
  - Suspect TB in a chronic scrotal mass, a scrotal sinus, or "epididymitis" that does not respond to antibiotics, especially in endemic settings or after BCG.
- **Tertiary prevention:**
  - Complete full drug treatment.
  - Check the other side.
  - Assess fertility and sexual function during follow-up (Huang).
- **Genetic counseling:** not applicable.

---

## 14. Other Species / Natural Disease

- **Cattle (*Bos taurus*, NCBITaxon:9913):**
  - Genital TB from *M. bovis* is rare in bulls.
  - Penile and preputial TB in a bull has been reported (J Comp Pathol 2020). The authors advise considering TB in granulomatous genital lesions of bulls.
  - Orchitis affects about 2–3% of bulls overall, from many causes including *M. tuberculosis*/*M. bovis*, *Brucella abortus* and BoHV-1 (MDPI review via web summary).
- **Zoonotic potential:**
  - *M. bovis* infects people through milk and contact with animals.
  - BCG epididymitis is iatrogenic, not zoonotic.
- **OMIA, breeds and orthologous genes:** not applicable.

---

## 15. Model Organisms

- No animal model of tuberculous epididymitis specifically was found.
- General TB models in mice, guinea pigs, rabbits and non-human primates, including *M. tuberculosis* aerosol infection, produce disseminated disease. Genital involvement has not been characterized as a model.
- Limitation: these models do not reproduce epididymal tropism, obstruction, or infertility outcomes.
- **Research gap:** there is a need for a model of epididymal or male reproductive tract mycobacterial infection, for example retrograde or intravesical BCG instillation in rodents. None was retrieved.

---

### Main evidence (PMIDs)
| PMID | Study |
|---|---|
| 34654377 | Huang 2021, 81 cases |
| 16006701 | Viswaroop 2005, 40 cases |
| 9282805 | Chung 1997, ultrasound |
| 8510282 | Kim 1993, ultrasound |
| 11373214 | Muttarak 2001, ultrasound |
| 6683985 | Ferrie 1983, 20 cases |
| 28087922 | Figueiredo 2017 review |
| 18836557 | Figueiredo 2008 review |
| 31548730 | Muneer 2019 review |
| 10772435 | Menke 2000, BCG |
| 10879650 | Skoutelis 2000, complications |
| 16110362 | Liu 2005 |
| 33448348 | Cochrane Xpert review |
| 27516382 | ATS/CDC/IDSA 2016 guideline |

### Sources
- [MONDO:0001537 (OLS4)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http://purl.obolibrary.org/obo/MONDO_0001537)
- [Huang 2021, PMC8520285](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8520285/)
- [Urogenital TB review, Muneer 2019](https://pubmed.ncbi.nlm.nih.gov/31548730/)
- [Genital TB review, PMC5422679](https://pmc.ncbi.nlm.nih.gov/articles/PMC5422679)
- [BCG epididymo-orchitis, PMC6649823](https://pmc.ncbi.nlm.nih.gov/articles/PMC6649823)
- [BCG complications case, PMC3558260](https://pmc.ncbi.nlm.nih.gov/articles/PMC3558260)
- [Menke 2000](https://pubmed.ncbi.nlm.nih.gov/10772435)
- [Suankwan 2012 (Thailand)](https://www.tm.mahidol.ac.th/seameo/2012-43-4/17-5170-21.pdf)
- [Radiopaedia: scrotal tuberculosis](https://radiopaedia.org/articles/scrotal-tuberculosis?lang=gb)
- [Yang 2001 AJR (QxMD)](https://www.qxmd.com/r/11641187)
- [Ultrasound nomogram, PMC11220132](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11220132/)
- [M. bovis necrotizing epididymitis, PMC5960082](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5960082/)
- [Genital TB and infertility, PMC2684350](https://pmc.ncbi.nlm.nih.gov/articles/PMC2684350)
- [Sperm retrieval in TB obstructive azoospermia, PMC3222923](https://pmc.ncbi.nlm.nih.gov/articles/PMC3222923)
- [ATS/CDC/IDSA 2016 guideline](https://pubmed.ncbi.nlm.nih.gov/27516382/)
- [Penile TB in a bull](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi.dedup.....310afc57f4d31bb3c45a2b63785e6426)
- [Bull orchitis review (MDPI)](https://www.mdpi.com/2076-2615/15/19/2804)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 30 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001537` (7 mentions) - the report calls it "subsets: rare, gard_rare", "OLS4"; MONDO calls it **tuberculous epididymitis**
- `DOID:1251` (1 mention) - the report calls it "DOID"; DOID calls it **tuberculous epididymitis**
- `HP:0100845` (1 mention) - the report calls it "testicular pain"; HP calls it **Anaphylactic shock**
- `HP:0003565` (1 mention) - the report calls it "7/14 tested (50%)"; HP calls it **Elevated erythrocyte sedimentation rate**
- `HP:0011227` (1 mention) - the report calls it "5/8 tested (62.5%)"; HP calls it **Elevated circulating C-reactive protein concentration**
- `HP:0100639` (1 mention) - the report calls it "4.9% / 6.2% (Huang)"; HP calls it **Erectile dysfunction**
- `UBERON:0001338` (1 mention) - the report calls it "tunica vaginalis"; UBERON calls it **urethral gland**
- `UBERON:0001300` (1 mention) - the report calls it "scrotum and scrotal skin"; UBERON calls it **scrotum**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `CL:1000154` (1 mention) - CL does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000045` (1 mention) - the report calls it "abnormality of the scrotum"; HP calls it **Abnormal scrotum morphology**, and lists "Abnormality of the scrotum" among its other names
- `NCBITaxon:1765` (1 mention) - the report calls it "Mycobacterium bovis"; NCBITaxon calls it **Mycobacterium tuberculosis variant bovis**, and lists "Mycobacterium bovis" among its other names
- `CL:0000624` (1 mention) - the report calls it "CD4+ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `GO:0060333` (1 mention) - the report calls it "type II interferon-mediated signaling"; GO calls it **type II interferon-mediated signaling pathway**
- `GO:0070265` (1 mention) - the report calls it "necrotic cell death"; GO calls it **obsolete necrotic cell death**
- `UBERON:0002367` (1 mention) - the report calls it "prostate"; UBERON calls it **prostate gland**, and lists "prostate" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0001537` - called "subsets: rare, gard_rare", "OLS4"

### Terms the ontology service could not be reached for

2 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `UBERON:0002048` (1 mention)
- `GO:0045335` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `UBERON:0002113` (1 mention)