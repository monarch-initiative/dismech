---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-11-23T12:14:02.234467'
end_time: '2026-11-23T12:21:57.845249'
duration_seconds: 475.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Platelet-type Bleeding Disorder 11
  mondo_id: MONDO:0013623
  category: Mendelian
  causal_genes: GP6
  omim_id: OMIM:614201
  synonyms: BDPLT11; GP6 inherited bleeding disorder, platelet-type; GP6-related platelet
    disorder; inherited bleeding disorder, platelet-type caused by mutation in GP6
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 12
  total_cost_usd: 1.1875386149999998
  session_id: b80bec79-1a20-4efe-adab-3960329be1b0
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 32
  retrieval_calls: 30
  assistant_text_blocks: 3
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
citation_count: 12
reference_validation:
  total_references: 28
  verified: 27
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.036
  relevance_assessed: 27
  on_topic: 17
  unresolved_references:
  - PMID:32500636
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 36
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0013623
    reported_labels:
    - MONDO
    ontology_label: platelet-type bleeding disorder 11
  - term_id: HP:0030912
    reported_labels:
    - MedGen-listed
    ontology_label: Duplicated clitoris
  - term_id: NCIT:C809
    reported_labels:
    - "Antifibrinolytics** \u2014 tranexamic acid"
    ontology_label: Ricin
  - term_id: NCIT:C29066
    reported_labels:
    - Desmopressin / DDAVP
    ontology_label: Gamma Interferon-SCH
  labels_variant: 3
  obsolete_terms:
  - term_id: NCIT:C29066
    ontology_label: Gamma Interferon-SCH
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
- **Disease Name:** Platelet-type Bleeding Disorder 11
- **MONDO ID:** MONDO:0013623 (if available)
- **Causal gene(s):** GP6
- **OMIM:** OMIM:614201
- **Synonyms:** BDPLT11; GP6 inherited bleeding disorder, platelet-type; GP6-related platelet disorder; inherited bleeding disorder, platelet-type caused by mutation in GP6
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Platelet-type Bleeding Disorder 11** covering all of the
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

Most PubMed pages wouldn't load, so I'm getting the GP6 papers through the Europe PMC API instead.

# Platelet-type Bleeding Disorder 11 (BDPLT11; GP6 / glycoprotein VI deficiency): research report

**Scope.** This report covers the disease with MONDO:0013623 and OMIM:614201. Its causal gene is **GP6** (NCBI Gene 51206, chromosome 19q13.42), which encodes the platelet collagen receptor glycoprotein VI (GPVI). It does not cover other numbered "platelet-type bleeding disorders", which are caused by other genes. Acquired, autoimmune GPVI deficiency appears only where it matters for differential diagnosis.

**How sources were gathered.** PubMed pages and its E-utilities API could not be reached in this session. Abstracts came from the Europe PMC REST API, MedlinePlus Genetics and NCBI MedGen. Quotes marked "verbatim" were checked against the abstract text that Europe PMC returned. Quotes marked "(unverified)" came from a tool summary only. ClinVar, gnomAD, Orphanet, MGI and ClinicalTrials.gov could not be queried directly. Any section that relies on those resources says so.

---

## 1. Disease information

**Overview.** OMIM and MedGen define the disease this way: *"Platelet-type bleeding disorder-11 (BDPLT11) is an autosomal recessive mild to moderate bleeding disorder caused by defective platelet activation and aggregation in response to collagen."* ([MedGen 481750](https://www.ncbi.nlm.nih.gov/medgen/481750); [OMIM 614201 via MGI](https://www.informatics.jax.org/disease/OMIM:614201))

MedlinePlus describes it as *"a bleeding disorder associated with a decreased ability to form blood clots"* ([MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/glycoprotein-vi-deficiency/)).

**Identifiers** (from [MedGen 481750](https://www.ncbi.nlm.nih.gov/medgen/481750)):

| Resource | ID |
|---|---|
| MONDO | MONDO:0013623 |
| OMIM (phenotype) | 614201 |
| OMIM (gene, GP6) | 605546 |
| Orphanet | ORPHA:98885 |
| UMLS / MedGen | C3280120 / 481750 |
| SNOMED CT | 765977002 ("Bleeding disorder due to glycoprotein VI deficiency") |
| GARD | 13293 |
| Disease Ontology | DOID:0111057 ([DO](https://disease-ontology.org/term/DOID:0111057)) |
| ICD-10 / ICD-11 / MeSH | Not retrieved. No disease-specific code was found. By general classification it would fall under the qualitative platelet defects (ICD-10 D69.1). That is an inference, not a retrieved mapping. |

**Synonyms:** BDPLT11; glycoprotein VI deficiency; GP VI deficiency; bleeding diathesis due to a collagen receptor defect; bleeding disorder, platelet-type, 11 ([MedlinePlus](https://medlineplus.gov/genetics/condition/glycoprotein-vi-deficiency/); [MedGen](https://www.ncbi.nlm.nih.gov/medgen/481750)).

**MedGen parent classes:** "Hemorrhagic disorder due to a qualitative platelet defect"; "Bleeding diathesis due to a collagen receptor defect."

**Data source type.** Knowledge comes from aggregated disease-level resources (OMIM, Orphanet, MedlinePlus) plus case reports and small case series. There are no EHR- or registry-based cohorts.

---

## 2. Etiology

### Causal factors
- **Genetic.** Biallelic loss-of-function variants in GP6, either homozygous or compound heterozygous.
- **Verbatim, Matus et al. 2013 (PMID 23815599):** *"Complete or partial deficiency of GPVI in humans is a rare condition presenting as a mild bleeding disorder."*
- **Mechanism.** Without functional GPVI, platelets do not respond to collagen. MedlinePlus says GP6 mutations result in no GPVI, a truncated nonfunctional protein, or a protein with reduced collagen binding ([MedlinePlus](https://medlineplus.gov/genetics/condition/glycoprotein-vi-deficiency/)).

### Genetic risk factors
- **Chilean founder allele GP6 c.711_712insA.** Carrier frequency is 2.9% in Chile (see §4 and §9; PMID 32603422).
- **Variants in other genes.** A recent review-style abstract notes that heterozygous GP6 nonsense variants can lower both GPVI and FcRγ expression (Zamora-Cánovas 2025, PMID 41463295). It is unclear whether monoallelic variants add to bleeding risk.

### Environmental risk factors
- None are known to cause the inherited form.
- **Phenocopy (acquired GPVI deficiency).** Autoimmunity, through anti-GPVI autoantibodies, can cause an indistinguishable phenotype. Reported settings include ITP, Graves' disease and SLE ([MedlinePlus](https://medlineplus.gov/genetics/condition/glycoprotein-vi-deficiency/)).
- **Verbatim, Akiyama 2009 (PMID 19522742):** *"This is the first demonstration of platelet-associated anti-GPVI antibodies in GPVI-deficient subjects"*

### Exposures that could unmask bleeding (inferred, not studied)
- Trauma, surgery and menstruation are the usual triggers.
- Antiplatelet drugs could add to the defect. However, one patient with *immune* GPVI deficiency was *"treated with dual anti platelet therapy without bleeding"* (Loyau 2021, PMID 32627625).

### Protective factors
- **Genetic.** None were identified. Heterozygous carriers are protected from clinical bleeding because they keep one functional allele.
  - **Verbatim (PMID 23815599):** *"Heterozygous relatives had no pathological bleeding"*
- **Environmental.** None reported.

### Gene–environment interactions
No studies were found. In a mouse study, the antithrombotic effect of GPVI deficiency was lost under hyperglycaemia: *"supporting a role for GPVI in thrombosis under normoglycaemic conditions only"* (Gauer 2026, PMID 41870096; model organism evidence).

---

## 3. Phenotypes

The HPO annotations below are as listed in MedGen. Frequencies are qualitative, because cohorts are very small (MedlinePlus says *"At least 15 cases have been described"*; a 2025 abstract counts *"12 cases with molecular defects in GP6"*, PMID 41463295).

| Phenotype | HPO term | Type | Onset | Severity / course | Frequency / evidence |
|---|---|---|---|---|---|
| Easy bruising / ecchymoses | HP:0000978 Bruising susceptibility; HP:0031364 Ecchymosis | Sign | Infancy / childhood | Mild; lifelong, episodic | Common. *"This 10-year-old girl presented ecchymoses since infancy"* (Dumont 2009, PMID 19549989) |
| Epistaxis | HP:0000421 Epistaxis | Symptom | Childhood | Mild–moderate; episodic | Common (MedlinePlus; MedGen) |
| Mucocutaneous bleeding (general) | HP:0031010 Abnormal mucocutaneous bleeding (suggested) | Symptom | Childhood | Mild | Reported in all 4 Chilean probands (PMID 23815599) |
| Menorrhagia | HP:0000132 Menorrhagia | Symptom | Menarche | Moderate | Frequent in affected women (MedlinePlus) |
| Prolonged bleeding after surgery or trauma | HP:0011889 Bleeding with minor or no trauma; HP:0034077 Prolonged bleeding following surgery (suggested) | Sign | Any age | Mild–moderate | MedlinePlus |
| Prolonged bleeding time | HP:0003010 Prolonged bleeding time | Laboratory | – | Mild | *"mild bleeding time prolongation"* (Moroi 1989, PMID 2808700) |
| Impaired collagen-induced aggregation | HP:0031819 Impaired collagen-induced platelet aggregation (MedGen-listed) | Laboratory | – | Defining | ~100%. *"Collagen-induced platelet activation was null"* (PMID 19549989) |
| Absent convulxin/CRP response | (no HPO term; suggest a new term request) | Laboratory | – | Defining | *"absent platelet aggregation and (14) C-5-HT secretion with collagen, convulxin and collagen-related peptide"* (PMID 23815599) |
| Abnormal platelet count | HP:0011873 Abnormal platelet count (MedGen) | Laboratory | – | Usually normal in inherited cases | Thrombocytopenia mainly points to the acquired/immune form (PMIDs 19522742, 30046699) |
| Impaired ristocetin-induced aggregation | HP:0030912 (MedGen-listed) | Laboratory | – | Not substantiated in the abstracts retrieved | Unknown |

HPO IDs marked "suggested" were assigned by the author and should be checked against HPO. MedGen lists only the feature names.

**Quality of life.** No EQ-5D, SF-36 or other QoL data exist for this disease. Based on the clinical phenotype, the burden is probably limited to menorrhagia (with possible iron deficiency) and to managing procedures. This is inferred, not measured.

---

## 4. Genetic / molecular information

### Causal gene
- **GP6**, glycoprotein VI platelet: HGNC:14388 (from author knowledge; not retrieved this session), NCBI Gene 51206, OMIM 605546, 19q13.42.
- GPVI is an immunoglobulin-superfamily receptor with two Ig-like domains. It is carried on the platelet surface in complex with the FcR γ-chain (FCER1G), which contains an ITAM.
- Cys-338 in the cytoplasmic tail mediates disulfide-linked dimerization (Arthur 2007, PMID 17690106).

### Reported pathogenic variants (germline)

| Variant | Type | Zygosity / context | Evidence |
|---|---|---|---|
| c.711_712insA (exon 6), frameshift leading to a premature stop before the transmembrane domain | Frameshift / truncating | Homozygous in 4 unrelated Chilean families | *"All the patients had an adenine insertion in exon 6 (c.711_712insA), changing the reading frame"* (Matus 2013, PMID 23815599). Further families: Nagy 2020, PMID 32603422. Founder haplotype: Dalby 2022, PMID 35994634 |
| p.R38C (exon 3), together with a second allele | Missense (Ig-like D1, collagen-binding domain) | Compound heterozygous; 10-year-old girl | *"an R38C mutation in exon 3 of one allele"* (Dumont 2009, PMID 19549989). The second allele is described in the full text and was not retrieved |
| 16-bp out-of-frame deletion + p.S175N | Frameshift + missense | Compound heterozygous; parents are asymptomatic carriers | Hermans 2009, PMID 19552682 (unverified quote: "compound heterozygous for an out-of-frame 16-bp deletion and a missense mutation S175N") |
| Novel GP6 nonsense variant | Nonsense | Heterozygous; reduced GPVI and FcRγ | Zamora-Cánovas 2025, PMID 41463295: *"Decreased expression of both GPVI and FcRγ-chain was detected in patients carrying GPVI nonsense variant in heterozygosis."* |

- **ACMG/ClinVar classification.** Not retrieved, because ClinVar was not reachable. Under ACMG criteria, c.711_712insA would be expected to qualify as pathogenic (PVS1, PS3 and PM3, with a founder effect). That is an inference and should be checked in ClinVar.
- **Gene-level curation.** Genomics England PanelApp lists GP6 as **Green (high evidence)** on the "Bleeding and platelet disorders" panel ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/545/gene/GP6/)).
- **Allele frequency.** The founder allele has a 2.9% carrier frequency in Chile (1,212 donors). Verbatim: *"indicating that there are ∼4000 GP6hom individuals in Chile"* (PMID 32603422). gnomAD frequencies were not retrieved.
- **Origin.** All reported variants are germline. Somatic variants are not relevant.
- **Functional consequence.** Loss of function: either absent surface GPVI (truncation removes the transmembrane anchor, so the protein is not membrane-bound) or reduced collagen binding (missense variants in the Ig-like domains).
- **Common polymorphisms.** GPVI haplotype variants (e.g. 13254T>C) exist. In one study *"The presence of variant alleles was not related to increased risk of periprocedural bleeding"* (Sionova 2017, PMID 29056992; unverified quote).
- **Modifier genes.** None established. FCER1G is required for GPVI surface expression, so its status could plausibly modify the phenotype (inferred).
- **Epigenetics.** No data.
- **Chromosomal abnormalities.** None reported. 19q13.42 deletions would be expected to include GP6 together with the LRC/KIR gene cluster (inferred).

---

## 5. Environmental information
- **Environmental or toxic factors:** none for the inherited form.
- **Lifestyle factors:** none established. NSAIDs and aspirin are expected to add to the platelet defect (inferred; general platelet-disorder practice).
- **Infectious agents:** not causal. One related point: in a randomized trial of glenzocimab (a GPVI inhibitor) in COVID-19 ARDS, *"No Serious Adverse Event (SAE) was deemed related to study drug"* (Pottecher 2024, PMID 38885234; unverified quote). This suggests that blocking GPVI is tolerated even during infection.

---

## 6. Mechanism / pathophysiology

### Causal chain
1. **Biallelic GP6 loss-of-function variants** (truncating such as c.711_712insA, or missense such as p.R38C) **lead to** a lack of functional GPVI on the platelet surface.
   - Truncating variants: the stop codon falls before the transmembrane domain, so no membrane-anchored receptor is made (PMIDs 23815599, 32603422).
   - Missense variants in the Ig-like domains: collagen binding is impaired (PMID 19549989; MedlinePlus).
2. **Absence of the GPVI–FcRγ complex results in** failure of collagen, convulxin or CRP to trigger ITAM signalling. This includes Syk/LAT/PLCγ2 activation, which is inferred from GPVI biology and was not measured in the patient abstracts retrieved.
3. **Loss of collagen signalling leads to** absent collagen-induced aggregation and dense-granule (5-HT) secretion (PMID 23815599). Aggregation with ADP, arachidonic acid and thrombin stays intact (PMID 19552682, unverified).
4. **Under flow, this results in** defective aggregate growth, reduced procoagulant phosphatidylserine (PS) exposure and abolished spreading. Initial adhesion is preserved, because α2β1 and GPIb–VWF compensate. Verbatim: *"GPVI supports aggregation and PS exposure under flow on collagen and noncollagen surfaces, but not adhesion"* (PMID 32603422).
   - **Branch (coagulation):** GPVI also binds fibrin. In GPVI-deficient patients, *"tissue factor-triggered thrombin generation was impaired"* (Mammadova-Bach 2015, PMID 25977585).
5. **Smaller and less stable haemostatic plugs at sites of collagen exposure lead to** mucocutaneous bleeding: bruising, epistaxis, menorrhagia and post-procedural bleeding.
6. **The bleeding stays mild because** redundant pathways (thrombin/PAR, ADP and TxA2 feedback, α2β1, CLEC-2) support haemostasis.
   - **Mouse support:** *"tail bleeding time measurements revealed no severe bleeding tendency as a consequence of GP VI deficiency"* (Kato 2003, PMID 12738669).
   - **Human support:** Nagy 2020 says these defects *"may contribute to the mild bleeding diathesis"* (PMID 32603422).
   - **Thrombosis cont

I'll continue the report from where it stopped, picking up at the remaining sections.

## 6. Mechanism (continued)

**Molecular pathways.** GPVI signalling is the ITAM/Syk pathway: collagen binding to the GPVI Ig-like D1 domain induces receptor clustering and disulfide-dependent dimerization via Cys-338 (Arthur 2007, PMID 17690106 — verbatim: *"the penultimate residue of the GPVI cytoplasmic tail, Cys-338, mediates disulfide-dependent dimer formation"*), phosphorylation of the associated FcR γ-chain ITAM, Syk recruitment, and PLCγ2 activation with Ca²⁺ mobilization. The downstream steps (Src/Syk/LAT/PLCγ2) are drawn from GPVI biology generally and were not measured in the patient reports retrieved here. Suggested pathway resources: Reactome "GPVI-mediated activation cascade" (R-HSA-114604) — ID from author knowledge, not retrieved this session, so verify.

**Cellular processes (suggested GO terms).** Platelet activation (GO:0030168); platelet aggregation (GO:0070527); platelet degranulation (GO:0002576); cell adhesion mediated by integrin (GO:0033627); blood coagulation (GO:0007596). These were assigned by the author and should be checked against GO.

**Protein dysfunction.** Loss of function by two routes: absent surface expression (truncation before the transmembrane domain) and impaired ligand binding (missense in the collagen-binding Ig domain). Receptor shedding is a separate, regulated mechanism relevant to acquired deficiency: *"ADAM10, but not ADAM17, cleaved a GPVI-based synthetic peptide"* (Gardiner 2007, PMID 17445093).

**Immune involvement.** Not part of the inherited disease. It is the mechanism of the acquired phenocopy (PMID 19522742).

**Metabolic changes, epigenetic changes, metabolomics, lipidomics, single-cell and spatial data, CRISPR screens.** No disease-specific data were retrieved for any of these. For a receptor-deficiency platelet disorder, none would be expected to exist.

---

## 7. Anatomical structures affected

- **Body system:** haematological / haemostatic system. There is no organ parenchymal disease.
- **Primary cell type:** platelet (CL:0000233), and its precursor the megakaryocyte (CL:0000556). GP6 expression is restricted to the megakaryocyte lineage.
- **Tissue/organ:** blood (UBERON:0000178); bone marrow (UBERON:0002371) as the site of megakaryopoiesis. Bleeding manifests at mucosal surfaces — nasal mucosa (UBERON:0001826), endometrium (UBERON:0001295) — and in skin/subcutaneous tissue (UBERON:0002097) as ecchymoses. Terms assigned by the author; verify in UBERON.
- **Subcellular (suggested GO CC):** plasma membrane (GO:0005886); platelet dense granule (GO:0042582); platelet alpha granule (GO:0031091). The primary lesion is at the plasma membrane.
- **Localization/lateralization:** systemic and non-lateralized; bleeding sites are determined by trauma, not by anatomical predisposition.

---

## 8. Temporal development

- **Onset:** childhood, often infancy. Verbatim: *"This 10-year-old girl presented ecchymoses since infancy"* (PMID 19549989). Onset is insidious — easy bruising noticed by family rather than an acute event. In women, menorrhagia begins at menarche.
- **Course:** stable and non-progressive; the receptor defect is fixed from birth. Bleeding events are **episodic**, tied to trauma, surgery, dental work and menstruation.
- **Duration:** chronic, lifelong.
- **Stages:** none defined; no staging system exists.
- **Remission:** not applicable for the inherited form. The acquired form can remit — Akiyama 2009 reported *"restoration of GPVI expression"* in its title (PMID 19522742), which distinguishes it from the genetic disease.
- **Critical periods:** the windows that matter are peri-procedural and peri-partum (inferred from the phenotype; no natural-history study exists).

No longitudinal natural-history study or registry for this disease was found.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (MedGen, OMIM, MedlinePlus). Carriers are unaffected: *"Heterozygous relatives had no pathological bleeding"* (PMID 23815599); Hermans 2009 reports *"The parents without clinical bleeding problems are heterozygous carriers"* (PMID 19552682, unverified quote). Note the caveat from Zamora-Cánovas 2025 that heterozygotes can show reduced GPVI/FcRγ expression (PMID 41463295) — a biochemical, not clinical, finding.
- **Prevalence:** unknown. *"The prevalence of glycoprotein VI deficiency is unknown. At least 15 cases have been described in the scientific literature."* ([MedlinePlus](https://medlineplus.gov/genetics/condition/glycoprotein-vi-deficiency/)). A 2025 abstract counts *"12 cases with molecular defects in GP6"* (PMID 41463295). Orphanet's prevalence class could not be retrieved.
- **Incidence:** not established.
- **Founder effect — the key population finding.** The Chilean c.711_712insA allele has a carrier frequency of **2.9%** in 1,212 Chilean donors, *"indicating that there are ∼4000 GP6hom individuals in Chile"* (PMID 32603422). Dalby 2022 traced the haplotype and titled the work *"Introduction of an ancient founder glycoprotein VI mutation into the Chilean population"* (PMID 35994634; no abstract available). This implies the disease is substantially under-diagnosed: ~4,000 predicted homozygotes in one country against ~15 cases in the world literature.
- **Carrier frequency elsewhere:** not retrieved (gnomAD unavailable).
- **Consanguinity:** not required. Matus 2013 describes *"four unrelated patients"* from non-consanguineous families, consistent with a founder allele rather than consanguinity.
- **Penetrance/expressivity:** biochemical penetrance of the platelet-function defect appears complete in homozygotes (absent collagen aggregation in all reported cases). Clinical bleeding severity is variable and mild — which, with the Chilean carrier data, suggests many homozygotes never present.
- **Anticipation; germline mosaicism:** not applicable / not reported.
- **Sex ratio:** autosomal, so 1:1 expected. Women are likely over-represented among those who come to attention, because menorrhagia brings them in. That is an inference.
- **Geography:** cases reported from Chile (4 families, PMID 23815599; 3 families, PMID 32603422), France/Belgium (PMIDs 19549989, 19552682), Spain (PMID 41463295) and Japan (PMID 2808700, the index GPVI-deficient patient).

---

## 10. Diagnostics

**Laboratory and functional testing** (the diagnostic core):
1. **Light transmission aggregometry** — the signature is an isolated absence of collagen response with other agonists preserved. Verbatim: *"absent platelet aggregation and (14) C-5-HT secretion with collagen, convulxin and collagen-related peptide"* (PMID 23815599); *"Collagen-induced platelet activation was null"* (PMID 19549989). In a GPVI-pathway family, *"Platelet functional testing showed an isolated platelet defect of collagen-induced aggregation"* (PMID 30046699).
2. **GPVI-selective agonists** — convulxin and collagen-related peptide (CRP) activate GPVI without engaging α2β1, so they separate GPVI defects from integrin defects.
3. **Flow cytometry for surface GPVI** and for FcRγ-chain expression (PMID 41463295).
4. **Platelet count and morphology** — typically normal in the inherited form; thrombocytopenia should raise suspicion of the immune form (PMIDs 19522742, 30046699).
5. **Bleeding time / PFA** — historically *"mild bleeding time prolongation"* (PMID 2808700); bleeding time is now largely abandoned.
6. **Flow-based assays** (research-grade): abolished spreading on collagen and VWF, reduced aggregate formation and PS exposure (PMID 32603422).
7. **Thrombin generation** may be reduced: *"tissue factor-triggered thrombin generation was impaired in GPVI-deficient patients"* (PMID 25977585).

**Genetic testing.**
- **Single-gene GP6 sequencing** confirms the diagnosis; in Chilean patients, targeted testing for exon 6 c.711_712insA is the efficient first step (PMIDs 23815599, 32603422).
- **Gene panels** are the usual route in practice: GP6 is on the Genomics England "Bleeding and platelet disorders" panel with a Green rating ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/545/gene/GP6/)). A GTR entry exists (GTR C3280120, linked from MedlinePlus and MedGen).
- **WES/WGS** are appropriate for undiagnosed bleeding phenotypes; NGS was used to exclude GP6 in the immune case (PMID 30046699) and to find novel variants in the 2025 Spanish series (PMID 41463295).
- **CMA, karyotype, FISH, mtDNA and repeat-expansion testing:** not indicated.

**Omics-based diagnostics.** Not used clinically for this disease. Flow cytometry of receptor expression is the practical proteomic readout.

**Clinical criteria.** No disease-specific published criteria were retrieved. Diagnosis rests on: (a) mucocutaneous bleeding history, usually scored with a bleeding assessment tool; (b) isolated absent collagen/CRP/convulxin aggregation; (c) absent or reduced GPVI expression; (d) biallelic GP6 variants.

**Differential diagnosis.**

| Condition | Distinguishing feature |
|---|---|
| Acquired/immune GPVI deficiency | Anti-GPVI autoantibodies, no GP6 variant, often thrombocytopenia, potentially reversible (PMIDs 19522742, 30046699, 17059472) |
| GPVI-pathway signalling defects (FcRγ, Syk, PLCγ2) | GPVI protein present but non-functional; a familial case was described where *"A genetic defect in GPVI/Fcgamma signalling compromising platelet function is hypothesised in this family"* (Dunkley 2007, PMID 17539777) |
| α2β1 (ITGA2) deficiency | Collagen defect but preserved convulxin/CRP response |
| Glanzmann thrombasthenia | Aggregation absent to **all** agonists |
| Bernard–Soulier | Macrothrombocytopenia, absent ristocetin response |
| Von Willebrand disease | Abnormal VWF antigen/activity; collagen response normal |
| Secretion/storage pool defects | Broader agonist abnormalities, reduced granule content |

**Screening.** No newborn or population screening exists. Cascade testing of relatives of a proband is appropriate. In Chile, carrier screening for the founder allele is technically feasible — the 2.9% carrier frequency has been measured (PMID 32603422) — but no program was found.

---

## 11. Outcome / prognosis

- **Survival and mortality:** no excess mortality is described. OMIM/MedGen call it *"mild to moderate"*; life expectancy appears normal. No survival or mortality data exist, which is itself consistent with a non-life-limiting disorder. No registry data were retrievable.
- **Morbidity:** limited to bleeding episodes. Expected complications are iron-deficiency anaemia from menorrhagia or recurrent epistaxis, and peri-operative or post-partum haemorrhage. These are inferred from the phenotype; I found no study quantifying them in GP6 patients.
- **Quality of life:** no EQ-5D, SF-36 or PROMIS data for this disease.
- **Disability:** none expected.
- **Recovery:** the genetic defect is permanent; individual bleeding episodes resolve with treatment. The acquired form, by contrast, can show *"restoration of GPVI expression"* (PMID 19522742).
- **Prognostic factors:** not formally studied. Candidate predictors (inferred): complete versus partial GPVI loss, concurrent antiplatelet/anticoagulant exposure, and the frequency of haemostatic challenges.
- **A possible counterbalancing effect.** GPVI blockade is being developed as an *antithrombotic* strategy precisely because it reduces thrombosis with little bleeding (see §12). Whether GP6-deficient individuals are protected from arterial thrombosis has not been tested in humans. Mouse data support the direction: *"Ex vivo platelet thrombus formation on type I collagen fibrils was abolished"* (PMID 12738669), and *"GPVI-deficient mice lack collagen responses and are protected against experimentally induced pulmonary thromboembolism"* (Lockyer 2006, PMID 16139873).

---

## 12. Treatment

No disease-specific trials or guidelines for BDPLT11 were retrieved. Management follows general practice for inherited platelet function disorders. The items below are labelled by how well-supported they are for *this* disease.

**Pharmacotherapy** (standard of care for mild platelet function disorders; no GP6-specific trial evidence retrieved):
- **Antifibrinolytics** — tranexamic acid (NCIT:C809), aminocaproic acid (NCIT:C287) — for mucosal bleeding and procedural cover.
- **Desmopressin / DDAVP** (NCIT:C29066) — commonly used in platelet function disorders; its efficacy in GPVI deficiency specifically was not documented in the sources retrieved.
- **Hormonal therapy** — combined oral contraceptives or a levonorgestrel IUD for menorrhagia.
- **Iron supplementation** (NCIT:C1511, iron supplement) for iron deficiency.
- **Platelet transfusion** (NCIT:C15431) — reserved for major bleeding or major surgery.
- **Recombinant activated factor VII** — used in refractory platelet-disorder bleeding; no GP6-specific report retrieved.
- **Avoid** aspirin and NSAIDs (inferred, standard advice).

**Pharmacogenomics:** no PharmGKB/CPIC entry for GP6 was retrieved.

**Advanced therapeutics.** No gene therapy, cell therapy, RNA-based therapy or targeted therapy exists or is in trials for this disease. Allogeneic HSCT would be curative in principle but is not justified by a mild phenotype (inference).

**Surgical/interventional.** No disease-specific surgery. Local measures — nasal packing or cautery for epistaxis, endometrial management for menorrhagia — plus haemostatic cover for any procedure.

**Experimental treatments.** No ClinicalTrials.gov records for BDPLT11 were retrieved (the registry was not reachable this session).

**Important inverse context — GPVI as a drug target.** The pharmacology around this gene runs in the opposite direction: the disease phenotype is the rationale for inhibiting GPVI therapeutically.
- **Glenzocimab (ACT017)**, an anti-GPVI Fab, has reached randomized trials in acute ischaemic stroke. ACTISAVE: *"ACTISAVE failed to confirm a beneficial effect of glenzocimab on mRS"*, with *"no major safety signals with any intracerebral hemorrhage"* (Köhrmann 2026, PMID 42044230). A further trial with endovascular therapy is ongoing: *"This is the first randomized trial evaluating the efficacy of glenzocimab with EVT"* (Mazighi 2026, PMID 40866207). Phase I PK/PD: Renaud 2020, PMID 32500636.
- Additional inhibitors in development include **EMA601** and **Revacept** (Mangin 2025, PMID 40171661; Nieswandt 2025, PMID 40171679).

The clinical safety profile of these inhibitors is the pharmacological mirror of the human knockout phenotype — a point worth recording in a knowledge base entry, because it independently corroborates the mildness of GPVI loss.

**Treatment algorithm (synthesis, not a retrieved guideline):** baseline bleeding assessment → antifibrinolytics as first line for mucosal bleeding → hormonal control of menorrhagia → tranexamic acid ± DDAVP for minor procedures → platelet transfusion for major surgery or major bleeding → lifelong avoidance of antiplatelet agents, with a medical alert record.

---

## 13. Prevention

- **Primary prevention of the disease:** not possible — it is a germline Mendelian disorder. Prevention is reproductive: genetic counselling, carrier testing, and the options of prenatal diagnosis or preimplantation genetic testing. For an autosomal recessive condition, carrier parents have a 25% recurrence risk per pregnancy.
- **Secondary prevention (early detection):** cascade testing within families of a proband. In Chile, the measured 2.9% carrier frequency (PMID 32603422) makes founder-allele carrier screening technically feasible; no such program was found, and the mild phenotype weakens the case for population screening.
- **Tertiary prevention (preventing complications) — the main actionable area:**
  - Pre-procedural haemostatic planning for any surgery or dental extraction.
  - Prophylactic tranexamic acid around procedures.
  - Menorrhagia control to prevent iron-deficiency anaemia.
  - Avoidance of aspirin, NSAIDs and other antiplatelet agents.
  - Peri-partum planning.
  - A patient-held alert card documenting the platelet disorder.
  These are standard inherited-platelet-disorder measures, inferred for this disease rather than trial-proven in it.
- **Immunization:** no vaccine is relevant to pathogenesis. Routine immunization should proceed; subcutaneous rather than intramuscular route is sometimes preferred in bleeding disorders (general practice, not GP6-specific).
- **Genetic counselling:** should cover autosomal recessive inheritance, the benign carrier state (PMID 23815599), the mild and variable phenotype, and — notably — that many homozygotes may never be symptomatic, as implied by the Chilean carrier-frequency estimate.
- **Public health / environmental interventions:** not applicable.

---

## 14. Other species / natural disease

- **Taxonomy.** Species with characterized GPVI biology: *Homo sapiens* (NCBI:txid9606), *Mus musculus* (NCBI:txid10090), *Rattus norvegicus* (NCBI:txid10116). GPVI has also been studied in non-human primates and in cynomolgus macaque for antibody pharmacology, though I did not retrieve a source for that this session.
- **Orthologous genes.** Mouse *Gp6* and rat *Gp6* exist; the specific NCBI Gene IDs were not retrieved this session, so they should be looked up rather than quoted.
- **Naturally occurring disease in other species.** No naturally occurring GPVI deficiency in domestic or wild animals was retrieved. OMIA could not be queried this session, so I cannot state that none is recorded — only that I found none. All animal GPVI-deficiency evidence I retrieved comes from engineered mouse models.
- **Veterinary relevance.** None established.
- **Comparative pathology.** The informative cross-species difference is severity. Human patients have mild mucocutaneous bleeding, and GPVI-null mice likewise show *"no severe bleeding tendency"* (PMID 12738669) while losing collagen responses entirely. This concordance is unusually clean: both species lose the collagen pathway and both retain adequate haemostasis, confirming redundancy of collagen-induced activation across mammals.
- **Evolutionary conservation.** The GPVI/FcRγ ITAM mechanism is conserved in mammals. Note that GPVI is a relatively recent, mammal-restricted receptor; non-mammalian thrombocytes use other collagen receptors. This statement is from general knowledge; I did not retrieve an orthology analysis to support it.
- **Zoonotic potential / cross-species transmission:** not applicable — it is a germline genetic disease.

---

## 15. Model organisms

**Mouse (the principal model).**

| Model | Findings | Evidence |
|---|---|---|
| *Gp6*-null (targeted deletion) | Verbatim: *"GP VInull platelets failed to aggregate in response to type I fibrillar collagen or convulxin"*; *"Nevertheless, tail bleeding time measurements revealed no severe bleeding tendency as a consequence of GP VI deficiency"*; *"Ex vivo platelet thrombus formation on type I collagen fibrils was abolished"* | Kato 2003, PMID 12738669 |
| GPVI-deficient mice (independent line) | Title: *"GPVI-deficient mice lack collagen responses and are protected against experimentally induced pulmonary thromboembryism"* [sic — title reads "thromboembolism"]. Verbatim: *"Platelet glycoprotein VI (GPVI) is now considered to be a major player in platelet-collagen adhesive interactions"* | Lockyer 2006, PMID 16139873 |
| *Fcer1g*-null (FcRγ−/−; loses GPVI surface expression) | Verbatim: *"we demonstrate that deficiency of GPVI/FcRgamma is not associated with a major defect in arterial thrombus formation"*; *"with milder vascular injury deficiency of GPVI/FcRgamma was associated with a 30% reduction in thrombus growth"* | Mangin 2006, PMID 16391010 |
| GPVI-depleted / antibody-blocked mice in vivo | Verbatim: *"inhibition or absence of the major platelet collagen receptor, GPVI, abolishes platelet-vessel wall interactions"* | Massberg 2003, PMID 12515812 |
| GPVI-knockout under hyperglycaemia | Verbatim: *"supporting a role for GPVI in thrombosis under normoglycaemic conditions only"* | Gauer 2026, PMID 41870096 |

**Model types available.** Germline knockout mice are the established system. Conditional, knock-in and humanized GP6 models were not confirmed in this session — MGI and IMPC were not reachable, so availability should be checked at MGI (informatics.jax.org), IMPC, IMSR and KOMP. MGI does carry a page for this OMIM entry ([MGI OMIM:614201](https://www.informatics.jax.org/disease/OMIM:614201)).

**In vitro and cellular systems** (from the retrieved literature): human patient platelets studied under flow (PMID 32603422); chimeric GPVI–Fc receptor constructs for structure–function work (Dumont 2006, PMID 16876821); synthetic GPVI peptides for shedding assays (PMID 17445093). Patient-derived iPSC-megakaryocyte models for GP6 were not found.

**Phenotype recapitulation.** Good for the cellular phenotype — knockout mice reproduce the complete loss of collagen-induced aggregation and of thrombus formation on collagen, the defining human laboratory abnormality. Partial for the clinical phenotype: mice show minimal tail-bleeding prolongation, and the murine model does not reproduce the human mucocutaneous presentation (epistaxis, menorrhagia, ecchymoses), which depends on anatomy and on menstruation that mice lack.

**Limitations.** (a) No mouse model carries a patient-specific allele such as c.711_712insA, so truncation-specific effects are untested; (b) murine bleeding assays are poorly sensitive to mild human mucosal bleeding; (c) the human disease's variability and apparent under-penetrance cannot be modelled; (d) the hyperglycaemia finding (PMID 41870096) shows that murine GPVI phenotypes are metabolic-context dependent, which complicates extrapolation.

**Research applications.** These models have been used mainly for the inverse question — GPVI as an antithrombotic target — rather than for the bleeding disorder. They established that GPVI loss separates thrombosis from haemostasis, which is the scientific foundation of glenzocimab and related inhibitors (§12).

---

## Evidence summary and gaps

**Best-supported claims, with verbatim support:**

| Claim | PMID | Verbatim quote |
|---|---|---|
| Rare, mild bleeding disorder from GPVI deficiency | 23815599 | *"Complete or partial deficiency of GPVI in humans is a rare condition presenting as a mild bleeding disorder."* |
| Chilean founder frameshift, 4 unrelated families | 23815599 | *"All the patients had an adenine insertion in exon 6 (c.711_712insA), changing the reading frame"* |
| Autosomal recessive; carriers unaffected | 23815599 | *"Heterozygous relatives had no pathological bleeding"* |
| Diagnostic laboratory signature | 23815599 | *"They had absent platelet aggregation and (14) C-5-HT secretion with collagen, convulxin and collagen-related peptide."* |
| Under-diagnosis implied by carrier frequency | 32603422 | *"indicating that there are ∼4000 GP6hom individuals in Chile."* |
| GPVI's role under flow | 32603422 | *"GPVI supports aggregation and PS exposure under flow on collagen and noncollagen surfaces, but not adhesion."* |
| Compound heterozygous missense | 19549989 | *"an R38C mutation in exon 3 of one allele"*; *"Collagen-induced platelet activation was null"* |
| Onset in infancy | 19549989 | *"This 10-year-old girl presented ecchymoses since infancy"* |
| Index patient (pre-molecular) | 2808700 | *"Her platelets lacked collagen-induced aggregation and adhesion"*; *"The patient's parents' platelets contained approximately 50% the normal amount of GPVI"* |
| Mild phenotype confirmed in mouse | 12738669 | *"tail bleeding time measurements revealed no severe bleeding tendency as a consequence of GP VI deficiency."* |
| Impaired thrombin generation in patients | 25977585 | *"tissue factor-triggered thrombin generation was impaired in GPVI-deficient patients"* |
| Acquired phenocopy is autoimmune | 19522742 | *"strongly suggest an autoimmune mechanism in GPVI deficiency."* |
| Clinical defects are rare | 17910626 | *"Human patients with defects associated with the platelet collagen receptor, glycoprotein (GP)VI, are rare"* |

**Quotes needing verification before entry into a knowledge base** (retrieved via tool summary, not confirmed against source text): Hermans 2009 (PMID 19552682) 16-bp deletion + S175N and the parental carrier statement; Sionova 2017 (PMID 29056992); Kojima 2006 (PMID 17059472); Pottecher 2024 (PMID 38885234). Dalby 2022 (PMID 35994634) has **no abstract available**, so only its title can be cited.

**Significant gaps in this report, by cause:**
- **ClinVar / gnomAD not reachable:** no variant classifications, no ACMG assertions, no non-Chilean allele frequencies.
- **Orphanet not fetched directly:** no Orphanet prevalence class or natural-history text.
- **ClinicalTrials.gov not reachable:** no NCT identifiers, including for the glenzocimab trials cited above.
- **MGI / IMPC / IMSR not reachable:** no mouse allele IDs, no strain availability, no IMPC phenotype data.
- **HGNC, GO, HPO, UBERON, CL not queried:** all ontology IDs in this report that are marked "suggested" or that lack a retrieved source were assigned from author knowledge and must be validated before use.
- **No evidence found at all for:** QoL measures, survival/mortality statistics, treatment-response rates, epigenetics, metabolomics, gene–environment interaction, naturally occurring animal disease, ICD-10/ICD-11 and MeSH mappings.

**The single most important curation note.** The gap between ~15 published cases worldwide and ~4,000 predicted homozygotes in Chile alone (PMID 32603422) is the key quantitative fact about this disease. It indicates that published prevalence reflects ascertainment, not biology, and that the phenotype is mild enough that most homozygous individuals never reach haematological attention. Any prevalence figure entered into a knowledge base should carry that caveat.

**Sources:**
- [MedlinePlus Genetics: Glycoprotein VI deficiency](https://medlineplus.gov/genetics/condition/glycoprotein-vi-deficiency/)
- [NCBI MedGen 481750: Platelet-type bleeding disorder 11](https://www.ncbi.nlm.nih.gov/medgen/481750)
- [MGI disease page, OMIM:614201](https://www.informatics.jax.org/disease/OMIM:614201)
- [Genomics England PanelApp: GP6, Bleeding and platelet disorders panel](https://panelapp.genomicsengland.co.uk/panels/545/gene/GP6/)
- [Disease Ontology DOID:0111057](https://disease-ontology.org/term/DOID:0111057)
- [GARD entry 13293](https://rarediseases.info.nih.gov/diseases/13293)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/) — source for all PMID-cited abstracts above
- [PMID 23815599 (Matus 2013, J Thromb Haemost)](https://europepmc.org/article/MED/23815599)
- [PMID 32603422 (Nagy 2020, Blood Adv)](https://europepmc.org/article/MED/32603422)
- [PMID 19549989 (Dumont 2009, Blood)](https://europepmc.org/article/MED/19549989)
- [PMID 2808700 (Moroi 1989, J Clin Invest)](https://europepmc.org/article/MED/2808700)
- [PMID 12738669 (Kato 2003, Blood)](https://europepmc.org/article/MED/12738669)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 17 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:32500636` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013623` (2 mentions) - the report calls it "MONDO"; MONDO calls it **platelet-type bleeding disorder 11**
- `HP:0030912` (1 mention) - the report calls it "MedGen-listed"; HP calls it **Duplicated clitoris**
- `NCIT:C809` (1 mention) - the report calls it "Antifibrinolytics** — tranexamic acid"; NCIT calls it **Ricin**
- `NCIT:C29066` (1 mention) - the report calls it "Desmopressin / DDAVP"; NCIT calls it **Gamma Interferon-SCH**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C29066` (Gamma Interferon-SCH) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000233` (1 mention) - the report calls it "Primary cell type:** platelet"; CL calls it **platelet**, and lists "blood platelet" among its other names
- `UBERON:0000178` (1 mention) - the report calls it "Tissue/organ:** blood"; UBERON calls it **blood**, and lists "portion of blood" among its other names
- `NCIT:C15431` (1 mention) - the report calls it "Platelet transfusion"; NCIT calls it **Hematopoietic Cell Transplantation**, and lists "stem cell transplantation" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.