---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-23T12:16:13.710806'
end_time: '2026-11-23T12:20:27.941552'
duration_seconds: 254.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: HIKESHI-Related Hypomyelinating Leukodystrophy
  mondo_id: MONDO:0014813
  category: Mendelian
  causal_genes: HIKESHI
  omim_id: OMIM:616881
  synonyms: HIKESHI leukodystrophy; HLD13; hypomyelinating leukodystrophy 13; hypomyelinating
    leukodystrophy type 13; leukodystrophy caused by mutation in HIKESHI; leukodystrophy,
    hypomyelinating, type 13
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
  web_search_requests: 5
  num_turns: 11
  total_cost_usd: 0.8098210750000001
  session_id: 9d610e4d-bba0-4083-8ab7-ca20915d3cc0
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 33
  retrieval_calls: 31
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 11
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:28000699
  relevance_assessed: 19
  on_topic: 15
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 1
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014813
    reported_labels:
    - MONDO
    ontology_label: leukodystrophy, hypomyelinating, 13
  - term_id: HP:0001332
    reported_labels:
    - Dystonia (evolving from hypotonia)
    ontology_label: Dystonia
  - term_id: UBERON:0002316
    reported_labels:
    - unverified
    ontology_label: white matter
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HIKESHI-Related Hypomyelinating Leukodystrophy
- **MONDO ID:** MONDO:0014813 (if available)
- **Causal gene(s):** HIKESHI
- **OMIM:** OMIM:616881
- **Synonyms:** HIKESHI leukodystrophy; HLD13; hypomyelinating leukodystrophy 13; hypomyelinating leukodystrophy type 13; leukodystrophy caused by mutation in HIKESHI; leukodystrophy, hypomyelinating, type 13
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **HIKESHI-Related Hypomyelinating Leukodystrophy** covering all of the
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

**Interpretation and scope:** This report covers HIKESHI-related hypomyelinating leukodystrophy (MONDO:0014813; OMIM:616881; HLD13). It is caused by biallelic variants in **HIKESHI**, which was formerly called *C11orf73* (OMIM gene 614908). I found sources through web search, PubMed listings, PMC full text and the Europe PMC API.

- **Quotes:** The fetch tools capped verbatim quotes at about 125 characters. The quotes below are therefore short excerpts from the abstracts, not full sentences of abstract text.
- **Ontology IDs:** Apart from MONDO, OMIM, the Orphanet code and the PMIDs, I did not look up any ontology IDs (HP, GO, CL, UBERON, NCIT, HGNC) in this session. Treat them as suggestions to check, for example with the linkml-term-validator skill.

---

## 1. Disease information

**Overview.** HLD13 is an autosomal recessive hypomyelinating leukodystrophy that starts in infancy, caused by loss of function of HIKESHI. HIKESHI is a nuclear import carrier that brings HSP70 chaperones into the nucleus during heat stress.

- The first report was Edvardson et al., 2016 (PMID 26545878). It described six patients from three Ashkenazi-Jewish families: *"All the patients were homozygous for a missense mutation, p.Val54Leu, in C11ORF73"*.
- Helman et al., 2021 (PMID 34111619; PMC8327280) extended the clinical picture. They concluded the pathology supports a primary disorder of myelin.

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0014813 |
| OMIM (phenotype) | 616881 |
| OMIM (gene) | 614908 ([MedGen/OMIM via search](https://ncbi.nlm.nih.gov/medgen/C3280644)) |
| Orphanet | ORPHA:495844, "C11orf73-related autosomal recessive hypomyelinating leukodystrophy". Taken from the [GARD record](https://rarediseases.info.nih.gov/assets/singles/17910.json); I could not open Orphanet to confirm it. |
| KEGG | H00679, hypomyelinating leukodystrophy group ([KEGG](https://www.kegg.jp/entry/H00679)) |
| ICD-10 / ICD-11 / MeSH | No disease-specific code found. The likely parent concepts are the leukodystrophy / hereditary CNS demyelinating disease groupings (not verified). |

**Synonyms:** HLD13; hypomyelinating leukodystrophy 13; HIKESHI leukodystrophy; C11orf73-related autosomal recessive hypomyelinating leukodystrophy; "infantile hypomyelinating leukoencephalopathy" (PMID 28000699); "leukoencephalopathy and early death" (PMID 26545878).

**Evidence base:** Everything known comes from individual case reports and small case series (about 16–18 patients in total), plus cell and mouse studies. There are no registries or aggregated EHR data.

## 2. Etiology

- **Cause:** The disease is genetic. Patients carry biallelic loss-of-function variants in HIKESHI.
- **Genetic risk:**
  - Ashkenazi-Jewish founder variant c.160G>C p.(Val54Leu). Edvardson et al. reported about 1 in 200 carriers. Genotyping of more than 125,000 Ashkenazi-Jewish people gave about **1 in 216** (PMID 34111619).
  - Consanguinity raises the risk for the private variants, such as the Finnish case (PMID 28000699) and the Christian Arab family (PMID 40649816). I could not retrieve the parental consanguinity details.
- **Environmental trigger (a modifier of the course, not a cause): fever / febrile illness.** In Helman et al., 5 of 9 affected individuals had severe illness or died during a febrile illness (PMID 34111619). Saleh et al. note that 8 of 16 reported patients died suddenly at a mean age of 7.5 years (range 1–15) after a febrile illness (PMID 40649816). This fits the biology: HIKESHI imports HSP70 into the nucleus specifically during heat stress (PMID 22541429).
- **Protective factors:** None identified. No modifier genes or protective alleles have been reported.
- **Gene–environment interaction:** This is the key one. Without HIKESHI, cells cannot move HSP70 into the nucleus during heat stress. The **genotype × temperature** interaction (fever) is the proposed reason for acute decompensation and death. This link is inferred from the cell biology and the clinical associations; it has not been shown directly in patients.

## 3. Phenotypes

Sources: Edvardson 2016 (PMID 26545878, n=6); Helman 2021 (PMID 34111619, n=9 including 2 previously reported); Vasilescu 2017 (PMID 28000699, n=1); Mallack 2024 (PMID 38922739, n=1); Saleh 2025 (PMID 40649816, n=1 index plus 2 iPSC donors).

| Phenotype | Suggested HPO (unverified) | Onset / course | Frequency |
|---|---|---|---|
| CNS hypomyelination (diffuse T2 hyperintensity) | HP:0003429 | Infancy; can progress to white-matter volume loss | 7/7 imaged (Helman) |
| Thin corpus callosum (posterior) | Thin corpus callosum / HP:0002079 | Infancy | 6/7 (Helman) |
| Axial hypotonia (early) | HP:0008936 | Infancy | Described as a shared core feature in the Helman series |
| Spasticity, progressive; spastic quadriplegia | HP:0001257 / HP:0002510 | Childhood, progressive | Core feature |
| Dystonia (evolving from hypotonia) | HP:0001332 | Childhood | Common |
| Hyperreflexia, clonus | HP:0001347, HP:0002169 | Childhood | Common |
| Nystagmus | HP:0000639 | Infancy | Core feature |
| Feeding difficulties, poor growth | HP:0011968, HP:0001510 | Infancy | Core feature |
| Global developmental delay / intellectual disability | HP:0001263 / HP:0001249 | Infancy | Universal in reported cases |
| Acquired microcephaly, short stature, epilepsy, anarthria | HP:0005484, HP:0004322, HP:0001250, HP:0002371 | Childhood to adolescence | Index case aged 21 y (PMID 40649816) |
| Deterioration or death with febrile illness | Fever-triggered decompensation (no exact HPO term; consider HP:0001945 Fever plus HP:0003819 Death in childhood) | Any age in childhood | 5/9 (Helman); 8/16 (Saleh review) |
| Reduced NAA on MRS | Abnormal MRS / reduced NAA | — | 2 cases (Helman) |

- **Severity:** Severe. Patients are profoundly disabled.
- **Quality of life:** No formal QoL instruments (EQ-5D, PedsQL) have been reported. The functional impact is inferred from the phenotype: quadriplegia, anarthria, feeding dependence, and repeated life-threatening febrile crises.

## 4. Genetic / molecular information

- **Gene:** HIKESHI (11q14; OMIM 614908; HGNC ID not verified here). It encodes a small protein that forms an asymmetric homodimer. The 1.8 Å crystal structure shows N-terminal hydrophobic pockets that bind FG-nucleoporins; *"Hikeshi forms an asymmetric homodimer that is responsible for the interaction with Hsp70s"* (PMID 25760597).

**Reported pathogenic variants** (all germline and homozygous, all missense):

| Variant | Population | Functional effect | Reference |
|---|---|---|---|
| c.160G>C p.(Val54Leu) | Ashkenazi-Jewish founder | Protein absent; no nuclear HSP70 during heat shock | PMID 26545878, 34111619 |
| c.11G>C p.(Cys4Ser) | Finnish | Protein instability (changes in hydrophobic pocket); impaired HSP70 nuclear translocation | PMID 28000699 |
| c.4T>G p.(Phe2Val) | Not stated in what I retrieved (US report) | Initially a VUS. Protein absent in fibroblasts; rescued by vector re-expression | PMID 38922739 |
| c.232C>T p.(Pro78Ser) | Christian Arab | Predicted to affect the dimerization domain. iPSCs show low HIKESHI after heat shock and impaired HSP70 nuclear translocation | PMID 40649816 |

- **Mechanism:** Loss of function, mostly through protein instability or absence of the protein.
- **Possible additional toxic effect:** The C4S mutant localizes to lysosomes and gains a new interaction with Filamin A in oligodendroglial cells (PMID 33535532). This was shown in vitro only.
- **Not retrieved:** ClinVar classifications and gnomAD frequencies. The Ashkenazi carrier rate (about 1/216) is the best population figure I have.
- **Modifier genes, epigenetics, chromosomal abnormalities:** None reported.

## 5. Environmental information

- There are no toxin, lifestyle or occupational causes.
- **Fever or hyperthermia** acts as a trigger for decompensation, as described in section 2.
- Infections matter only as the source of fever and sepsis. Deaths in Helman et al. were attributed to septic shock or multiorgan failure (ages about 3–5.5 years) and to febrile illness (age 12) (PMID 34111619). No specific pathogen is implicated.

## 6. Mechanism / pathophysiology

**Causal chain**

1. Biallelic HIKESHI missense variants **lead to** an unstable or absent HIKESHI protein (shown in patient cells: PMID 26545878, 28000699, 38922739, 40649816).
2. Loss of HIKESHI **results in** failure of the HIKESHI pathway, which imports ATP-bound HSP70 into the nucleus through FG-nucleoporins without using the Ran system (PMID 22541429). This happens:
   - under heat stress; and
   - at baseline, where it lowers nuclear HSP70 and **leads to** constitutive HSF1 activation and a disturbed heat-shock response (PMID 35580988).
3. **Branch A (developmental):** Without nuclear HSP70, the oligodendrocyte transcription factor SOX10 is not stabilized. This **results in** arrested oligodendrocyte differentiation (mouse, PMID 37865085). Rat OPCs expressing V54L or C4S show reduced MBP/CNPase and fewer MBP+/APC+ cells (PMID 37965292). In human iPSC-derived oligodendrocytes there are fewer Olig2+ cells and myelination is abnormal (PMID 42875792).
4. The differentiation failure **leads to** primary CNS hypomyelination. At autopsy myelin was almost entirely absent, U-fibres were not spared, axons were relatively preserved, Olig2 signal was markedly lost, and there was reactive astrogliosis and microgliosis without leukocyte infiltration (PMID 34111619).
5. Hypomyelination **results in** the clinical picture: nystagmus, hypotonia, then spasticity or dystonia, developmental delay, and a thin corpus callosum on MRI.
6. **Branch B (acute stress):** During fever, cells cannot import HSP70 into the nucleus to protect it from heat-induced damage. In HIKESHI-depleted cells this **leads to** nuclear damage and reduced survival (PMID 22541429). In patients, this is the **proposed (inferred)** cause of fever-associated decompensation and sudden death (PMID 34111619, 40649816).
7. **Branch C (possible gain of function, in vitro):** The C4S mutant goes to lysosomes and binds Filamin A, which **inhibits** morphological differentiation of oligodendroglial cells (PMID 33535532).

**Supporting detail**

- **Pathways:** heat-shock response / HSF1; HSP70 chaperone system; nucleocytoplasmic transport (Ran-independent).
- **Responses vary by cell type:** Hikeshi depletion reduced survival of HeLa cells under proteotoxic stress but increased survival of RPE cells (PMID 28980748).
- **Immune involvement:** Limited to reactive glia. There is no inflammatory infiltrate (PMID 34111619).
- **Omics:** No transcriptomic, proteomic or metabolomic datasets were found. The only expression finding is that HSP70 mRNA is raised in patient iPSCs (PMID 40649816).
- **Suggested GO terms (unverified):** protein import into nucleus (GO:0006606); response to heat (GO:0009408); cellular response to heat (GO:0034605); oligodendrocyte differentiation (GO:0048709); central nervous system myelination (GO:0022010); myelination (GO:0042552).
- **Suggested CL terms (unverified):** oligodendrocyte (CL:0000128); oligodendrocyte precursor cell (CL:0002453); astrocyte (CL:0000127); microglial cell (CL:0000129).

## 7. Anatomical structures affected

- **Primary:** CNS white matter, diffusely and bilaterally and symmetrically, including U-fibres. Suggested UBERON: white matter UBERON:0002316 (unverified).
- **Other CNS structures:** Corpus callosum, which is thin posteriorly (UBERON:0002336, unverified). Later on, white-matter and brainstem/cerebellar volume is lost (PMID 40649816). The cerebellum was normal in 6/7 on MRI (PMID 34111619).
- **Autopsy:** Mild hydrocephalus. Brain weight was 1250 g against about 1364 g expected for age (PMID 34111619).
- **Secondary effects:** Growth failure, short stature, acquired microcephaly, and multiorgan failure during sepsis.
- **Subcellular:** nucleus, cytoplasm, nuclear pore complex. The C4S mutant is lysosomal. Suggested GO CC terms (unverified): GO:0005634, GO:0005737, GO:0005643, GO:0005764.

## 8. Temporal development

- **Onset:** Infancy. Delayed myelination was already present on MRI at 10.5 months (PMID 40649816) and at 7 months (PMID 38922739). Onset is insidious.
- **Course:** Progressive. Axial hypotonia evolves into spasticity or dystonia. Over time there is progressive atrophy, punctuated by acute febrile crises.
- **Lifespan:** Survival ranges from early childhood deaths (1–5.5 years) to at least 21 years (PMID 34111619, 40649816).
- **Remission:** None.
- **Critical periods:** Each febrile episode is a window of vulnerability. Infancy, when myelination takes place, is the window in which gene therapy could in theory help.

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive. All reported patients are homozygous.
- **Penetrance:** Appears complete in homozygotes. Expressivity varies, both in survival and in severity.
- **Anticipation and mosaicism:** None reported.
- **Founder effect:** p.Val54Leu in Ashkenazi Jews; carrier frequency about 1/216 (PMID 34111619), or about 1/200 (PMID 26545878 as cited).
- **Other populations:** Finnish, Christian Arab, and a US case of unstated ancestry.
- **Prevalence:** Not established. Under Hardy-Weinberg, a 1/216 carrier rate implies roughly 1 in 187,000 Ashkenazi births. This is my own calculation, not a published figure.
- **Sex ratio:** Not reported.

## 10. Diagnostics

- **MRI:** The cornerstone. It shows diffuse hypomyelination (T2 hyperintensity with near-normal T1 signal, as is typical of hypomyelination), a thin posterior corpus callosum, and later atrophy. MRS may show reduced NAA (PMID 34111619).
- **Genetic testing:**
  - Exome or genome sequencing, or a leukodystrophy / hypomyelination gene panel that includes HIKESHI.
  - Targeted testing for c.160G>C in Ashkenazi-Jewish patients.
  - The disease was first identified by exome analysis (PMID 26545878).
- **Functional tests (research setting):**
  - Western blot for HIKESHI in fibroblasts.
  - Imaging of heat-induced nuclear HSP70 translocation.
  - These assays helped reclassify the p.Phe2Val VUS (PMID 38922739).
- **Pathology:** Near-total loss of myelin with preserved axons and loss of Olig2 (PMID 34111619).
- **Differential diagnosis:** Other hypomyelinating leukodystrophies. From general knowledge, not retrieved here: Pelizaeus-Merzbacher disease (*PLP1*), *GJC2*, POLR3-related, *TUBB4A*. Distinguishing clues for HLD13 are Ashkenazi ancestry, febrile decompensation, and homozygous HIKESHI variants.
- **Screening:** Helman et al. call for broader screening because of the high carrier rate. Whether p.Val54Leu is on current Ashkenazi carrier panels was not verified.

## 11. Outcome / prognosis

- **Mortality:** About 50% of reported patients died. Saleh et al. report 8 of 16 dying suddenly at a mean of 7.5 years (range 1–15) after febrile illness (PMID 40649816). Helman et al. report 4 of 9 deaths, at about 3, 3.5, 5.5 and 12 years (PMID 34111619).
- **Survival rates:** Formal survival statistics do not exist.
- **Morbidity:** Severe and lifelong: quadriplegia, intellectual disability, anarthria, feeding dependence, epilepsy.
- **Prognostic factors:** Febrile and septic illness is the main factor associated with death. No biomarkers are known.

## 12. Treatment

- **Approved therapy:** None.
- **Supportive care** (inferred standard leukodystrophy care; there is no HLD13-specific guideline):
  - Aggressive fever control and prompt treatment of infections. This is suggested by the fever association, not tested in a trial.
  - Nutrition support, including gastrostomy.
  - Management of spasticity and dystonia.
  - Antiseizure drugs.
  - Physical, occupational and speech therapy.
- **Experimental (preclinical only):**
  - **Gene replacement:** Vector-mediated re-expression of HIKESHI restored heat-induced HSP70 nuclear translocation in patient fibroblasts (PMID 38922739).
  - **Proteasome inhibitors:** In patient iPSC-derived oligodendrocytes they partly restored HIKESHI protein and HSP70 nuclear localization; *"PI treatment also rescued Olig2+ cell numbers, myelination, and cell morphology abnormalities."* (PMID 42875792, 2026). This fits a protein-instability mechanism.
  - **Therapeutic hyperthermia:** In mice, Hikeshi-dependent hyperthermia promoted remyelination after injury (PMID 37865085). This needs functional HIKESHI, so it is not applicable to patients.
- **Clinical trials:** No NCT trials were found. I did not search ClinicalTrials.gov directly.
- **Pharmacogenomics:** None.
- **Suggested NCIT concepts (IDs not verified):** Gene Therapy; Proteasome Inhibitor; Physical Therapy; Antipyretic Agent; Gastrostomy.

## 13. Prevention

- **Primary prevention:** Carrier screening, especially in Ashkenazi-Jewish people (p.Val54Leu). For known carrier couples: prenatal diagnosis and PGT-M. Edvardson's coauthors include a PGT group (Treff NR), but I did not retrieve the details.
- **Genetic counseling:** 25% recurrence risk per pregnancy for carrier parents.
- **Tertiary prevention:** Prevent and quickly treat fever and infections, keep vaccinations up to date (a general rationale), and have an emergency plan for febrile episodes. These are inferred recommendations.

## 14. Other species / natural disease

- **Naturally occurring disease:** None reported (OMIA not checked).
- **Conservation:** Hikeshi is conserved:
  - *S. pombe* Opi10 has similar biochemical functions but acts in different physiological contexts (PMID 24768994).
  - The Arabidopsis Hikeshi-like protein HLP1 interacts with HSP70 (PMID 24942879) and governs thermomemory (PMID 30890662).
- Ortholog gene IDs were not retrieved.

## 15. Model organisms

| Model | Findings | Reference |
|---|---|---|
| **Mouse** Hikeshi-deficient | "Hikeshi is essential for central nervous system (CNS) myelination." Oligodendrocyte maturation arrests; nuclear HSP70 stabilizes SOX10. Recapitulates hypomyelination. Febrile-death modelling not reported in what I retrieved. | PMID 37865085 (Li et al., Dev Cell 2023) |
| **Rat primary OPCs** expressing V54L/C4S | Less differentiation (MBP, CNPase); heat-induced HSP70 import blocked | PMID 37965292 |
| **Mouse oligodendroglial cell line** with C4S | Lysosomal mislocalization; new Filamin A binding; impaired morphological differentiation | PMID 33535532 |
| **Human iPSCs / iPSC-derived oligodendrocytes** (P78S and others) | Low HIKESHI after heat shock; high HSP70 mRNA; HSP70 import defect; fewer Olig2+ cells; rescue by proteasome inhibitors | PMID 40649816, 42875792 |
| **Patient fibroblasts** | HIKESHI absent; HSP70 translocation defect; rescue by transgene | PMID 26545878, 28000699, 38922739 |
| **HeLa / RPE knockdown** | Heat-shock and proteotoxic sensitivity; HSF1 dysregulation | PMID 22541429, 28980748, 35580988 |
| **Yeast / plant** | Conservation of the import function | PMID 24768994, 24942879 |

- **Limitations:** I did not retrieve whether mouse models reproduce fever-triggered death. Cell models lack the circuit-level phenotype. MGI/IMPC allele details were not retrieved.

---

### Key references (PMIDs)
- 26545878: Edvardson et al., J Med Genet 2016
- 34111619: Helman et al., Pediatr Neurol 2021 (PMC8327280)
- 28000699: Vasilescu et al., Eur J Hum Genet 2017
- 38922739: Mallack et al., Am J Med Genet A 2024
- 40649816: Saleh et al., Int J Mol Sci 2025 (PMC12250047)
- 42875792: Rathan-Kumar et al., J Transl Med 2026
- 37865085: Li et al., Dev Cell 2023
- 37965292: Miyamoto et al., Mol Genet Metab Rep 2023 (letter, PMC10641311)
- 33535532: Hattori et al., Medicines (Basel) 2021
- 22541429: Kose et al., Cell 2012
- 35580988: Kose et al., Life Sci Alliance 2022
- 25760597: Song et al., Acta Crystallogr D 2015
- 28980748: Rahman et al., Genes Cells 2017
- 29490261 and 39317134: Imamoto reviews, Curr Opin Cell Biol 2018 and 2024
- 24768994, 24942879, 30890662: yeast and Arabidopsis orthologs

### Sources
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8327280
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12250047/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10641311
- https://pubmed.ncbi.nlm.nih.gov/?term=HIKESHI
- https://www.ebi.ac.uk/europepmc/webservices/rest/search (records for the PMIDs above)
- https://pubmed.ncbi.nlm.nih.gov/22541429/
- https://rarediseases.info.nih.gov/assets/singles/17910.json
- https://ncbi.nlm.nih.gov/medgen/C3280644
- https://www.kegg.jp/entry/H00679
- https://vivo.weill.cornell.edu/display/pubid38922739
- https://disorders.eyes.arizona.edu/node/3051

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:28000699`: "infantile hypomyelinating leukoencephalopathy"
  - Text part not found as substring: 'infantile hypomyelinating leukoencephalopathy'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014813` (2 mentions) - the report calls it "MONDO"; MONDO calls it **leukodystrophy, hypomyelinating, 13**
- `HP:0001332` (1 mention) - the report calls it "Dystonia (evolving from hypotonia)"; HP calls it **Dystonia**
- `UBERON:0002316` (1 mention) - the report calls it "unverified"; UBERON calls it **white matter**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003429` (1 mention) - the report calls it "CNS hypomyelination (diffuse T2 hyperintensity)"; HP calls it **CNS hypomyelination**
- `HP:0008936` (1 mention) - the report calls it "Axial hypotonia (early)"; HP calls it **Axial hypotonia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.