---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T14:05:44.309279'
end_time: '2026-09-07T14:10:34.198951'
duration_seconds: 289.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Kashin-Beck Disease
  mondo_id: MONDO:0005610
  category: Environmental Osteochondropathy
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
  web_search_requests: 19
  num_turns: 21
  total_cost_usd: 1.3261964000000002
  session_id: 4bf4a114-75db-54c3-885d-72412fe47716
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 71
reference_validation:
  total_references: 54
  verified: 51
  not_found: 3
  unverifiable: 0
  confabulation_rate: 0.056
  quotes_checked: 6
  quotes_valid: 2
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMC:PMC8999107
  - PMC:PMC6738986
  - PMID:22294316
  - DOI:10.1002/jor.22073
  relevance_assessed: 51
  on_topic: 25
  unresolved_references:
  - DOI:10.3967/bes2024.109
  - DOI:10.3967/bes2017.021
  - DOI:10.3967/bes2017.046
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 21
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0005610
    reported_labels:
    - classified as a subclass of osteochondrodysplasia
    - Disease
    ontology_label: Kashin-Beck disease
  - term_id: HP:0100729
    reported_labels:
    - "Large joint involvement \u2014 verify exact term"
    ontology_label: Large face
  - term_id: HP:0009824
    reported_labels:
    - "Osteolysis \u2014 not typical, avoid"
    ontology_label: Upper limb undergrowth
  - term_id: GO:0097707
    reported_labels:
    - "ferroptosis \u2014 if available as GO term/verify current OBO status"
    ontology_label: ferroptosis
  - term_id: CL:0000743
    reported_labels:
    - "growth plate chondrocyte context \u2014 verify exact CL binding"
    ontology_label: hypertrophic chondrocyte
  - term_id: CL:0000605
    reported_labels:
    - articular chondrocyte, if resolvable
    ontology_label: fungal asexual spore
  - term_id: UBERON:0001981
    reported_labels:
    - "growth plate cartilage \u2014 verify exact ID"
    ontology_label: blood vessel
  - term_id: UBERON:0001415
    reported_labels:
    - interphalangeal joint
    ontology_label: skin of pelvis
  - term_id: UBERON:0000004
    reported_labels:
    - "ankle joint region \u2014 verify"
    ontology_label: nose
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kashin-Beck Disease
- **MONDO ID:** MONDO:0005610 (if available)
- **Category:** Environmental Osteochondropathy

## Research Objectives

Please provide a comprehensive research report on **Kashin-Beck Disease** covering all of the
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

I'll research Kashin-Beck Disease using web search and fetch tools to compile a comprehensive report per the template.

I now have sufficient depth across all sections. Compiling the comprehensive research report.

# Kashin-Beck Disease: Comprehensive Research Report

## 1. Disease Information

**Overview.** Kashin-Beck disease (KBD) is a chronic, endemic osteochondropathy — a degenerative, non-inflammatory disorder of growth-plate and articular cartilage — that produces symmetric joint enlargement, growth retardation, and in severe cases dwarfism. It is confined to a specific geographic belt and is considered a multifactorial environmental disease rather than a Mendelian genetic disorder, though genetic susceptibility loci have been identified. Onset is characteristically in childhood (ages 3–13), with progressive, largely irreversible skeletal changes ("Pathophysiological drivers include environmental toxins such as T-2 mycotoxin, nutritional deficiencies (notably selenium and iodine), and genetic predispositions that converge on dysregulated signalling pathways" — [Nature Index summary](https://www.nature.com/nature-index/topics/l4/pathophysiology-and-treatment-of-kashin-beck-disease)).

**Key identifiers:**
- **MONDO:** MONDO:0005610 — classified as a subclass of osteochondrodysplasia ([Monarch Initiative](https://monarchinitiative.org/MONDO:0005610))
- **ICD-11:** FA27.0
- **ICD-10:** M12.1 (Kaschin-Beck disease)
- **ICD-9:** 716.0
- OMIM does not carry a dedicated Mendelian entry (KBD is not modeled as single-gene disease in OMIM); Orphanet listing was not confirmed in available searches — verify directly before curation.

**Synonyms:** Kaschin-Beck disease, Kashin–Bek disease, "Big Bone Disease" (colloquial/regional), Urov disease (older Russian literature), endemic osteoarthritis, endemic deforming osteoarthrosis, endemic osteochondropathy.

**Data source note.** Virtually all available evidence is aggregated disease-level/epidemiological and mechanistic literature (national surveillance reports, cross-sectional and cohort studies, case series, animal-model and omics studies) rather than individual EHR-level records — consistent with KBD's status as a public-health/endemic-disease research area concentrated in Chinese, Tibetan, and Russian populations.

Sources: [ScienceDirect overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/kashin-beck-disease), [Wikidata](https://www.wikidata.org/wiki/Q500314), [Monarch Initiative MONDO:0005610](https://monarchinitiative.org/MONDO:0005610)

---

## 2. Etiology

KBD etiology is **unresolved and actively debated**; four historical hypotheses persist in the literature, now generally synthesized into a "compound etiology" model:

1. **Selenium (Se) deficiency hypothesis (biogeochemical)** — endemic regions overlap low-Se soil/food belts (shared with Keshan disease).
2. **Mycotoxin hypothesis** — grain (wheat/corn) stored under damp conditions becomes contaminated with *Fusarium* fungi producing **T-2 toxin** and other trichothecene mycotoxins.
3. **Organic water-pollution/humic-fulvic acid hypothesis** — high humic/fulvic acid content in local drinking water, generating free radicals via oxy/hydroxy functional groups that damage chondrocyte membranes and increase lipid peroxidation ([PubMed 10090708](https://pubmed.ncbi.nlm.nih.gov/10090708/); [Springer PMC3620638](https://pmc.ncbi.nlm.nih.gov/articles/PMC3620638/)).
4. **Compound/multifactorial etiology** — current consensus, integrating Se deficiency, T-2 toxin exposure, iodine deficiency, and genetic susceptibility as converging, synergistic factors rather than a single monocausal agent ([ScienceDirect animal models review](https://www.sciencedirect.com/science/article/pii/S0147651322002597)).

> "Four etiological hypotheses have been formed, including water of organic poisoning hypothesis represented by fulvic acid (FA), biogeochemical hypothesis represented by selenium (Se) deficiency, food mycotoxin poisoning hypothesis represented by T-2 toxin poisoning and compound etiology theory hypothesis." — [Animal models of KBD, ScienceDirect 2022](https://www.sciencedirect.com/science/article/pii/S0147651322002597)

### Genetic Risk Factors
- **ADAM12** — a bivariate GWAS (2,417 subjects, phenotypes = joint deformity + body height) found the top signal at rs1278300 (p = 9.25×10⁻⁹), replicated at rs1278300 (p=0.007) and rs1710287 (p=0.002); ADAM12 protein expression was significantly reduced in KBD articular cartilage by immunohistochemistry ([PMC4992896](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4992896/); [Sci Rep](https://www.nature.com/articles/srep31792)).
- **COL10A1, HABP2** — coding-region sequencing in Tibetan populations identified candidate susceptibility variants ([BMC Med Genet](https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-017-0423-6)).
- **Selenoprotein gene polymorphisms** (e.g., GPX1, SEPP1 family) associated with KBD risk and serum Se/iodine levels in Tibetan populations ([PMC3751926](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3751926/)).
- **GDF5 and DIO2** — bone-development genes implicated preferentially in pediatric-onset (vs adult) KBD by gene expression analysis ([PMC4114804](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114804/)); DIO2 encodes selenium-dependent type 2 deiodinase, mechanistically linking thyroid hormone activation to Se status.

### Environmental Risk Factors
- Low soil/dietary selenium (shared biogeochemical belt with Keshan disease, a cardiomyopathy).
- Grain (cereal) contamination with *Fusarium*-derived T-2 mycotoxin, especially in humid storage conditions.
- Humic/fulvic-acid-rich drinking water.
- Concurrent iodine deficiency, which appears to potentiate risk in severely Se-deficient areas ("In areas where severe selenium deficiency is endemic, iodine deficiency is a risk factor for Kashin-Beck disease" — [ScienceDirect](https://www.sciencedirect.com/topics/veterinary-science-and-veterinary-medicine/kashin-beck-disease)).
- Cold climate/seasonality has been proposed as a contributing modifier ([De Gruyter, "Cold weather and Kashin-Beck disease," 2023](https://www.degruyter.com/document/doi/10.2478/fzm-2023-0005/html?lang=en)).
- Age (childhood exposure window is critical) and rural/subsistence-agriculture lifestyle (dependence on locally grown grain and untreated well water).

### Protective Factors
- Adequate dietary/serum selenium (confirmed protective across multiple RCTs and ecological studies).
- Higher dietary protein intake — "certain combinations of food substances high in protein had a protective effect" ([PMC8999107](https://pmc.ncbi.nlm.nih.gov/articles/PMC8999107/)).
- Grain replacement (importing Se-adequate, non-locally-grown, non-fungally-contaminated grain) — a core public-health intervention, not merely a research finding.
- Improved drinking-water sourcing (piped/treated water displacing local humic-acid-rich wells).

### Gene-Environment Interaction
Selenoprotein genotype modulates individual susceptibility to a shared environmental (low-Se, high T-2 toxin) exposure — e.g., selenoprotein gene polymorphism studies show genotype-dependent serum Se/iodine associations with KBD risk in the same geographic cohort ([PMC3751926](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3751926/)). Recent work also frames KBD as a sarcopenia risk factor whose severity interacts with selenium status ("Kashin–Beck Disease: A Risk Factor for Sarcopenia and Its Interaction with Selenium" — [PMC11678709](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11678709/)).

---

## 3. Phenotypes

### Clinical/Physical Manifestations
- **Arthralgia and morning stiffness** (early symptom)
- **Symmetric joint enlargement** — particularly finger interphalangeal/metacarpophalangeal joints, wrists, ankles, knees, elbows
- **Shortened fingers/brachydactyly** — from premature epiphyseal closure
- **Restricted range of motion / joint stiffness**
- **Genu varum/valgum and other limb deformities**
- **Growth retardation → short stature → dwarfism** in severe cases
- **Muscle atrophy adjacent to affected joints** (secondary)
- **Sarcopenia** as a later-life comorbidity/consequence ([PMC11678709](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11678709/))

Suggested HP terms: HP:0002829 (Arthralgia), HP:0001367 (Abnormal joint morphology), HP:0002652 (Skeletal dysplasia), HP:0011800 (Midface retrusion — N/A, omit), HP:0001773 (Short foot), HP:0100729 (Large joint involvement — verify exact term), HP:0002980 (Joint stiffness/limitation of joint mobility — HP:0001376), HP:0004322 (Short stature), HP:0009824 (Osteolysis — not typical, avoid), HP:0002751 (Kyphoscoliosis — occasional secondary), HP:0001156 (Brachydactyly).

### Behavioral/Psychological
- Depression and anxiety are elevated in KBD patients relative to the general population; a 2025 study specifically examined prevalence and risk factors of depression in KBD ([PMC12440642](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440642/)).
- Reported psychosocial burden: "strong sense of inferiority compared with their peers," financial difficulty, restricted activity ([PMC10161486](https://pmc.ncbi.nlm.nih.gov/articles/PMC10161486/)).

### Laboratory Abnormalities
- Low serum/urinary selenium and zinc, especially in children in endemic areas, tracked longitudinally ([PMC9033266](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9033266/))
- Altered serum metabolomic profile: candidate biomarkers include kynurenic acid, N-α-acetylarginine, 6-hydroxymelatonin, sphinganine, ceramide, sphingosine-1-phosphate, spermidine, and glycine ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0895398820301768))
- Altered fecal metabolome reflecting disturbed selenium-centered metabolic bioprocesses ([PMC10650499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10650499/))
- Gut microbiota dysbiosis: elevated Fusobacteria and Bacteroidetes; enriched *Alloprevotella*, *Robinsoniella*, *Megamonas*, *Escherichia-Shigella* ([Cell Death & Disease / PMC8553765](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8553765/))

### Onset, Severity, Progression
- **Onset:** Predominantly childhood, ages 3–13 (some sources report 5–15); clinical deformity can appear by age 5 or earlier.
- **Severity/staging (Chinese national clinical grading, three grades):**
  - **Grade I:** enlarged finger joints, limited range of motion, limb-joint pain
  - **Grade II:** shortened fingers + Grade I features
  - **Grade III:** dwarfism + Grade II features
  ("stage I KBD is defined as enlarged finger joints, limited range of motion and pain... stage II as shortened fingers... stage III as dwarfism" — search synthesis of [academic.oup.com/rheumatology](https://academic.oup.com/rheumatology/article/61/4/1732/6299414) and related sources)
- **Progression:** chronic, largely irreversible once epiphyseal/growth-plate damage occurs; adult disease resembles accelerated, severe generalized osteoarthritis.
- **Frequency:** National X-ray detectable rate fell from 21.01% (1990) to <10% (2003), <5% (2007), <0.4% in children (2010–2018), and 0% since 2019 per Chinese national surveillance ([BES Journal](https://www.besjournal.com/en/article/doi/10.3967/bes2024.109)), though Tibet remains an active transmission area with occasional new cases.

### Quality of Life
- HRQoL is **lower in KBD than in ordinary osteoarthritis** patients across physical function, activity limitation, mental health, and general health domains ([PMC10161486](https://pmc.ncbi.nlm.nih.gov/articles/PMC10161486/); [EQ-5D study](https://link.springer.com/article/10.1007/s11136-010-9820-4)).
- Most affected EQ-5D dimension: pain/discomfort, followed by mobility, anxiety/depression, usual activities, self-care.
- Severe (Grade II/III) and older (≥60y) patients show the largest healthy-life-expectancy losses, with substantial indirect economic burden (112.74 million CNY reported in one 2021 national burden analysis — [PubMed 38250701](https://pubmed.ncbi.nlm.nih.gov/38250701/)).

---

## 4. Genetic/Molecular Information

KBD is **not a single-gene Mendelian disorder**; it is a gene–environment disease with polygenic susceptibility contributions.

- **Causal/susceptibility genes:** ADAM12 (hgnc:188) — strongest GWAS hit, reduced protein expression in cartilage ([PMC4992896](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4992896/)); GDF5, DIO2 (pediatric-predominant expression signature — [PMC4114804](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114804/)); COL10A1, HABP2 (candidate coding variants, Tibetan cohort); selenoprotein pathway genes.
- **Variant classification:** No ClinVar pathogenic/likely-pathogenic single-variant entries identified for KBD in these searches — susceptibility-variant framework (GWAS SNP associations), not ACMG/AMP monogenic classification.
- **Functional consequences:** Predominantly loss-of-expression/regulatory effects (e.g., decreased ADAM12 protein in affected cartilage) rather than classic LOF/GOF coding mutations.
- **Epigenetics:** Not deeply characterized in the literature surfaced; no dedicated DNA-methylation/ChIP dataset for KBD identified — flag as a knowledge gap.
- **Molecular/transcriptomic findings:**
  - **ADAM12** downregulation in cartilage.
  - **WISP1** (Wnt-inducible signaling pathway protein 1) overexpressed in KBD chondrocytes, modulating autophagy markers ATG4C and LC3-II and ECM synthesis ([MDPI 2023](https://www.mdpi.com/1422-0067/24/22/16037); [PMC10671535](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10671535/)).
  - **GPx6** downregulation drives ferroptosis via the SLC7A11/GPx4 axis, with decreased COL2A1/ACAN and increased MMP13/ADAMTS4 ([Apoptosis journal 2026](https://link.springer.com/article/10.1007/s10495-026-02389-w); [PMC13323611](https://pmc.ncbi.nlm.nih.gov/articles/PMC13323611/)).
  - **SIRT3** and primary cilia integrity implicated; magnetofection-delivered SIRT3-targeting siRNA ameliorates cartilage damage in a rat model ([Theranostics/PMC13440625](https://pmc.ncbi.nlm.nih.gov/articles/PMC13440625/)).
  - **RUNX2** overexpression (selenium-mediated) and associated transcriptome alterations linked to chondrocyte injury ([PMC12714888](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12714888/)).
  - **TSG-6** abnormal expression disturbs ECM homeostasis ([PMC9715581](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9715581/)).
  - **Zip6 (SLC39A6)** zinc transporter expression modulated by Se/T-2 toxin status, implicating Zn²⁺ dysregulation ([PubMed 39455492](https://pubmed.ncbi.nlm.nih.gov/39455492/)).
  - **p-ATF2** via JNK/p38 MAPK signaling drives chondrocyte apoptosis ([PMC3726291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3726291/)).
- **Chromosomal abnormalities:** None reported — KBD is not associated with aneuploidy/structural chromosomal rearrangement.

Suggested GO/molecular annotations: GO:0006915 (apoptotic process), GO:0034599 (cellular response to oxidative stress), GO:0006914 (autophagy), GO:0097707 (ferroptosis — if available as GO term/verify current OBO status), GO:0030198 (extracellular matrix organization), GO:0007179 (TGF-beta receptor signaling), GO:0060070 (canonical Wnt signaling pathway), GO:0038066 (p38MAPK cascade).

---

## 5. Environmental Information

- **Toxins/exposures:** T-2 toxin (trichothecene mycotoxin from *Fusarium* spp. contaminating stored grain) — chondrocyte-toxic, elevates apoptotic proteins Fas, p53, Bax while decreasing anti-apoptotic Bcl-xL. Fluorine co-exposure impairs carboxylesterase 1-mediated T-2 toxin hydrolysis, **increasing** its chondrotoxicity ([PMC9381868](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9381868/)) — a notable toxin-toxin interaction.
- **Water contaminant:** humic/fulvic acid in drinking water (free-radical generation, lipid peroxidation of chondrocyte membranes).
- **Lifestyle/dietary factors:** subsistence agriculture with locally grown, Se-poor, potentially fungally-contaminated grain as primary caloric source; low dietary protein; reliance on untreated local well water.
- **Infectious agents:** None — KBD is **not infectious**; the "fungal" association is toxicological (mycotoxin contamination of stored food), not an active infection of the host.
- Suggested ECTO terms: exposure to T-2 toxin via ingestion; exposure to humic/fulvic acid via drinking water; dietary selenium deficiency exposure.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, with inference flags)

1. Chronic environmental exposure — low dietary/soil selenium **plus** ingestion of T-2 mycotoxin-contaminated grain (and, in some regions, humic/fulvic-acid-rich drinking water) — **leads to** systemic selenium deficiency and direct mycotoxin/oxidant burden in growth-plate and articular chondrocytes. *(Demonstrated ecologically and in animal models; the relative causal weight of each co-factor is still debated — inferred compound mechanism.)*
2. Selenium deficiency **results in** reduced activity of selenoenzymes (glutathione peroxidases, including GPx6, and thioredoxin reductase), **which leads to** impaired antioxidant defense and accumulation of reactive oxygen species (ROS) in chondrocytes.
3. T-2 toxin (potentiated by co-exposures such as fluorine, which impairs its detoxifying hydrolysis) **directly triggers** oxidative stress, mitochondrial dysfunction, and disrupted AMPK/mTOR/ULK1-mediated autophagy signaling in chondrocytes ([ScienceDirect 2024](https://www.sciencedirect.com/science/article/pii/S0147651324005797)).
4. Combined oxidative stress and autophagy dysregulation **activate** multiple regulated chondrocyte death pathways in parallel (branch point):
   - **Apoptosis** — via JNK/p38 MAPK → ATF2/p-ATF2 signaling and mitochondrial Fas/p53/Bax-Bcl-xL imbalance ([PMC3726291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3726291/); [PMC10467099](https://pmc.ncbi.nlm.nih.gov/articles/PMC10467099/)).
   - **Necroptosis** — RIP3-dependent, predominating in the *middle* zone of cartilage in pediatric KBD samples, distinct from TUNEL/caspase-3-associated classic apoptosis ([PMC6384500](https://pmc.ncbi.nlm.nih.gov/articles/PMC6384500/)).
   - **Ferroptosis** — GPx6 downregulation disinhibits lipid peroxidation via the SLC7A11/GPx4 axis, producing characteristic mitochondrial cristae loss and matrix vacuolization, concentrated in the *deep* zone ([Apoptosis 2026](https://link.springer.com/article/10.1007/s10495-026-02389-w)).
5. Dysregulated **WISP1/Wnt–β-catenin signaling** and **TGF-β/Smad3** pathways **further impair** normal chondrocyte matrix-synthesis programs and autophagic flux (ATG4C, LC3-II), compounding the death signal ([PMC10671535](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10671535/)).
6. Widespread chondrocyte death (necrosis/apoptosis/necroptosis/ferroptosis acting in different cartilage zones) **causes** focal chondronecrosis, most pronounced in the **deep zone** of growth-plate and articular cartilage, accompanied by **loss of ECM components** — decreased type II collagen (COL2A1) and aggrecan (ACAN), and increased matrix-degrading enzymes MMP13 and ADAMTS4 ([PMC13323611](https://pmc.ncbi.nlm.nih.gov/articles/PMC13323611/)).
7. Progressive chondronecrosis and ECM degradation at the growth plate **lead to** disordered endochondral ossification: irregular epiphyseal/metaphyseal mineralization, premature epiphyseal-line closure, and cone-shaped epiphyses on imaging.
8. Disordered growth-plate ossification **results in** growth-plate arrest and asymmetric longitudinal bone growth, **manifesting clinically as** shortened fingers/limbs and, in severe cases, dwarfism.
9. In parallel, chondronecrosis and ECM loss in **articular** (non-growth-plate) cartilage **lead to** secondary degenerative joint changes indistinguishable in later life from severe generalized osteoarthritis — joint-space narrowing, osteophyte formation, joint enlargement, and pain.
10. Chronic joint pain, deformity, and restricted mobility **culminate in** functional disability, sarcopenia, reduced health-related quality of life, and elevated rates of depression/anxiety (downstream systemic/psychosocial consequence, well-documented but several inferential steps removed from the initiating molecular lesion).

### Detail by category
- **Molecular pathways:** p38 MAPK, JNK, TGF-β/Smad3, Wnt/β-catenin (via WISP1), AMPK/mTOR/ULK1 (autophagy), SLC7A11/GPx4 (ferroptosis axis).
- **Cellular processes:** apoptosis, necroptosis, ferroptosis, autophagy dysregulation, oxidative stress, mitochondrial dysfunction (altered mitochondrial density/cristae — [PubMed 20650322](https://pubmed.ncbi.nlm.nih.gov/20650322/)).
- **Protein dysfunction:** loss of ADAM12 and GPx6 expression; TSG-6 dysregulation; RUNX2 overexpression; SIRT3 loss affecting primary cilia.
- **Metabolic changes:** disturbed selenium-centered metabolic bioprocesses (fecal/serum metabolomics), altered lipid metabolism (unsaturated fatty acids, glycerophospholipids), disordered glycometabolism ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0014482714001773)).
- **Immune involvement:** Not a classical autoimmune/inflammatory arthropathy; gut microbiota alterations are proposed to influence chondrocyte injury via inflammatory-mediator signaling, but this is an emerging/inferred link rather than an established primary immune mechanism ([PMC8553765](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8553765/)).
- **Tissue damage mechanisms:** oxidative stress and lipid peroxidation (both Se-deficiency- and fulvic-acid-driven), chondronecrosis, cartilage matrix degeneration.
- **Molecular profiling:** transcriptomic (RUNX2 pathway study), metabolomic (serum + fecal), microbiome (16S/metagenomic) — no large-scale single-cell/spatial-transcriptomic KBD dataset was identified in this search; flag as a data gap, though "recent insights into chondrocyte heterogeneity reveal expansion of mitochondrial-rich and homeostatic subpopulations in affected cartilage" was referenced in a synthesis source (verify primary citation before using).

Suggested GO terms for pathophysiology nodes: GO:0006915 (apoptotic process), GO:0070266 (necroptotic process), GO:0060670 or emerging ferroptosis GO term (verify current OBO Foundry status for "ferroptosis"), GO:0016239 (positive regulation of macroautophagy), GO:0030199 (collagen fibril organization), GO:0022617 (extracellular matrix disassembly). Suggested CL terms: CL:0000138 (chondrocyte), CL:1001606 or CL:0000743 (growth plate chondrocyte context — verify exact CL binding), CL:0000605 (articular chondrocyte, if resolvable).

---

## 7. Anatomical Structures Affected

- **Organ level:** Skeletal system — primary target is **cartilage** (growth-plate/epiphyseal and articular). Secondary/complication-level involvement: skeletal muscle (sarcopenia), and indirectly the endocrine/thyroid axis (co-occurring iodine deficiency).
- **Tissue/cell level:** Growth-plate (physeal) cartilage and hyaline articular cartilage; chondrocytes are the principal affected cell type (CL:0000138), with zone-specific vulnerability — deep zone predominates for chondronecrosis/ferroptosis, middle zone for necroptosis.
- **Subcellular level:** Mitochondria (dysfunction, cristae loss — GO:0005739), lysosome/autophagosome machinery (ATG4C, LC3-II), primary cilium (SIRT3-dependent).
- **Localization (UBERON):** Most affected joints — interphalangeal and metacarpophalangeal joints of the hand, wrist, elbow, knee, and ankle. UBERON candidates: UBERON:0001981 (growth plate cartilage — verify exact ID), UBERON:0001415 (interphalangeal joint), UBERON:0001465 (knee joint), UBERON:0000004 (ankle joint region — verify).
- **Lateralization:** Predominantly **bilateral and symmetric** joint involvement — a distinguishing clinical feature from unilateral post-traumatic osteoarthritis.

---

## 8. Temporal Development

- **Onset:** Childhood, typically ages 3–13 (some sources cite 5–15); insidious onset with early symptoms of joint pain/enlargement, often first evident in finger joints by age 5.
- **Progression:** Chronic and largely irreversible once epiphyseal damage has occurred; disease severity is staged I→II→III as described above (§3). Progression from finger-joint enlargement (Grade I) to shortened digits (Grade II) to dwarfism (Grade III) reflects cumulative growth-plate injury during the pediatric growth window.
- **Disease course pattern:** Progressive during the pediatric exposure window; in adulthood the residual skeletal deformity is generally **stable** structurally, but articular cartilage continues to degenerate as a secondary osteoarthritis-like process, so functional/pain burden can still worsen with age.
- **Critical period:** Childhood (particularly early childhood through puberty, while growth plates remain open) is the critical vulnerability window — once growth plates fuse, new KBD-type growth-plate lesions cannot occur, though secondary joint degeneration continues.
- **Remission:** No spontaneous remission; selenium/grain-replacement intervention during the pediatric window can halt or reduce further metaphyseal lesion progression (radiographically demonstrated) but does not reverse established deformity.

---

## 9. Inheritance and Population

- **Epidemiology:** Historically affected a large population across a crescent-shaped endemic belt from northeastern China through central China to Tibet, and into Siberia, Mongolia, and North Korea. As of 2018 Chinese Ministry of Health statistics, **535,878 individuals** were affected across **379 counties in 13 provinces/autonomous regions**. National X-ray-detectable rate in children fell from 21.01% (1990) to <10% (2003), <5% (2007), <0.4% (2010–2018), and reportedly **0% since 2019**, with elimination-standard achievement reported in all monitored villages over the most recent 5-year evaluation period ([BES Journal 2024](https://www.besjournal.com/en/article/doi/10.3967/bes2024.109)). Tibet (e.g., Qamdo, Luolong County) remains an area of ongoing, if low-level, active transmission with occasional new clinical cases.
- **Inheritance pattern:** Not Mendelian — polygenic/multifactorial susceptibility (GWAS-identified risk alleles such as ADAM12 rs1278300) interacting with environmental exposure; no simple AD/AR/X-linked pattern applies.
- **Penetrance/expressivity:** Variable, environmentally gated — genetic susceptibility manifests only in the presence of the requisite low-Se/high-mycotoxin environmental exposure; severity (Grade I–III) is variably expressive.
- **Founder effects/consanguinity:** Not established as relevant given the environmental/polygenic model.
- **Population demographics:** Disproportionately affects rural, subsistence-farming populations, notably ethnic Tibetan and Han populations within the endemic belt; some studies note higher risk in older age and in girls in Tibetan cohorts (OR=1.86), while earlier Chinese cohort data reported roughly 2:1 male excess in some 12-year-old subgroups — sex-ratio findings are **inconsistent across studies/regions** and should not be over-generalized.
- **Geographic distribution:** Endemic, latitude-band distribution strongly correlated with Se-poor soil geochemistry; recent spatial-epidemiology work has mapped county-level hotspots in Gansu Province and used spatial regression to quantify health loss by county ([PubMed 41984302](https://pubmed.ncbi.nlm.nih.gov/41984302/); [PubMed 41255597](https://pubmed.ncbi.nlm.nih.gov/41255597/)).

---

## 10. Diagnostics

- **Clinical/radiographic criteria:** China's national standard is **"Diagnostic Criteria for Kashin-Beck Disease" (WS/T 207)**, most recently updated as **WS/T 207-2010** (superseding WS/T 207-2001), combining X-ray pathological signs with clinical manifestations, applied by trained examiners ([BES Journal validation study](https://www.besjournal.com/article/doi/10.3967/bes2017.021)).
- **Key radiographic (pediatric hand/wrist) signs:** large metaphyseal defects with cone-shaped alterations, early epiphyseal-line closure, cone-shaped epiphysis, sclerosis at the metacarpal base, irregular/sclerotic carpal margins ([PMC5818476](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5818476/)).
- **Adult ankle X-ray grading:** grades 0–IV (grade IV subdivided a–d), benchmarked against Kellgren-Lawrence OA grading; X-ray grade correlates moderately with ankle pain but only weakly with finger-joint clinical grading, underscoring that radiographic and clinical severity are not interchangeable measures ([PubMed 41342918](https://pubmed.ncbi.nlm.nih.gov/41342918/)).
- **Emerging computational diagnostics:** deep-learning/transfer-learning models for automated metaphyseal-sign detection on pediatric hand X-rays, and graph neural network (GNN)-based auxiliary diagnosis tools ([ACM DL 2024](https://dl.acm.org/doi/fullHtml/10.1145/3653876.3653901); [PMC11871940](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11871940/); [PubMed 41398140](https://pubmed.ncbi.nlm.nih.gov/41398140/)).
- **Laboratory tests:** serum/urinary selenium and zinc levels (surveillance biomarkers, not diagnostic per se); emerging serum/fecal metabolomic biomarker panels (kynurenic acid, sphingolipids, spermidine, etc.) are research-stage, not yet clinical diagnostics.
- **Genetic testing:** Not part of standard clinical diagnosis (KBD is diagnosed clinically/radiographically); GWAS/candidate-gene panels (ADAM12, DIO2, GDF5, selenoprotein genes) are research tools for susceptibility studies, not diagnostic assays.
- **Differential diagnosis:** Primary comparator is idiopathic/generalized osteoarthritis (KBD is distinguished by pediatric onset, symmetric small-joint predominance, growth-plate involvement/short stature, and endemic geographic exposure); rickets and other skeletal dysplasias should be excluded, though this specific comparison was not deeply sourced in this search — flag for direct lookup against UpToDate/DynaMed before finalizing curation.
- **Screening:** Community/school-based radiographic screening programs in endemic counties (part of China's national surveillance system) function as the de facto population screening mechanism; no genetic carrier-screening program applies (non-Mendelian disease).

---

## 11. Outcome/Prognosis

- **Mortality:** KBD is **not directly life-threatening**; no disease-specific mortality data were identified — it is a disabling, non-fatal osteochondropathy.
- **Morbidity/function:** Severe cases (Grade II/III) cause lifelong joint deformity, restricted mobility, and disability; loss of ability to work/self-care is reported in advanced cases ([search synthesis, multiple sources above]).
- **Complications:** Secondary/accelerated osteoarthritis in adulthood; sarcopenia (independent association, modulated by selenium status — [PMC11678709](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11678709/) and [OARSI 2025](https://www.oarsijournal.com/article/S1063-4584(25)00356-5/fulltext)); depression/anxiety ([PMC12440642](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440642/)).
- **Quality of life:** Substantially reduced versus both healthy controls and ordinary OA patients across EQ-5D and SF-36-type domains, most severely in pain/discomfort and mobility ([PMC10161486](https://pmc.ncbi.nlm.nih.gov/articles/PMC10161486/)).
- **Economic burden:** 2021 national burden analysis reported an indirect economic burden of 112.74 million CNY, concentrated in Grade II and ≥60-year-old patients ([PubMed 38250701](https://pubmed.ncbi.nlm.nih.gov/38250701/)); a 2019-vs-2023 county-level spatial-regression study further quantified "health loss" hotspots ([PubMed 41255597](https://pubmed.ncbi.nlm.nih.gov/41255597/)).
- **Prognostic factors:** disease grade (II/III much worse than I), age at diagnosis/treatment initiation (earlier selenium intervention preserves more growth-plate function), and residual selenium status.
- **Recovery potential:** Selenium/grain-replacement therapy during the open-growth-plate window can arrest new metaphyseal lesion formation and partially remodel existing lesions radiographically, but **established deformity and short stature are not reversible**.

---

## 12. Treatment

- **Pharmacotherapy — Selenium supplementation (children/pediatric prevention & treatment):** Effective for radiographic structural improvement and repair of metaphyseal lesions; a large network meta-analysis (44 RCTs, 9,815 participants) and a focused NMA (15 RCTs, 2,931 patients comparing 5 selenium-supplement types) both found selenium superior to placebo, though the comparative superiority among selenium formulations remains inconclusive due to evidence quality limits ([PubMed 29511006](https://pubmed.ncbi.nlm.nih.gov/29511006/); [PubMed 31376086](https://pubmed.ncbi.nlm.nih.gov/31376086/); [ResearchGate NMA](https://www.researchgate.net/publication/328103541_Selenium_supplementation_for_treatment_of_kashin-beck_disease_A_network_meta-analysis)). Iodine co-supplementation has also been trialed in Tibetan children ([PubMed 12816783](https://pubmed.ncbi.nlm.nih.gov/12816783/)).
  - Suggested NCIT term: NCIT:C15986 (Pharmacotherapy), with `therapeutic_agent` bound to selenium compound (e.g., sodium selenite — CHEBI term to be verified) as agent.
- **Pharmacotherapy — Adult symptom management:** Glucosamine, chondroitin, intra-articular hyaluronic acid (IAH), and NSAIDs are all reported effective for adult symptomatic relief; **chondroitin + glucosamine combination ranked best for pain** in the same network meta-analysis, followed by IAH, chondroitin, and glucosamine monotherapy versus placebo ([PubMed 31376086](https://pubmed.ncbi.nlm.nih.gov/31376086/)).
- **Surgical/interventional:** Corrective surgery and joint replacement/arthroplasty for severe deformity; a documented case example is conservative tibiotalocalcaneal fusion for partial talar avascular necrosis with ankle/subtalar osteoarthritis in KBD ([PMC6709310](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6709310/)). Evidence base for surgical/complementary interventions is noted as still limited/"yet to be established" in systematic review.
  - Suggested NCIT terms: NCIT:C15329 (Surgical Procedure), NCIT:C16186 (Orthopedic Surgical Procedure).
- **Supportive/rehabilitative:** Physical therapy to maintain mobility and prevent further deformity, pain management, nutritional support.
  - Suggested NCIT term: NCIT:C15302 (Physical Therapy).
- **Experimental/preclinical (not yet clinical):** siRNA targeting SIRT3 via magnetofection delivery to protect primary cilia and reduce cartilage damage — demonstrated in a rat model, not yet in human trials ([Theranostics/PMC13440625](https://pmc.ncbi.nlm.nih.gov/articles/PMC13440625/)); selenomethionine-mediated antagonism of T-2-toxin-induced apoptotic microRNAs, also rat-model stage ([PMC10467099](https://pmc.ncbi.nlm.nih.gov/articles/PMC10467099/)).
- **Treatment strategy:** Public-health strategy is explicitly two-pronged — **primary prevention** via grain replacement/selenium fortification (population level, pediatric-window focus) combined with **individual symptomatic/surgical management** for already-affected adults; no NCT-numbered active interventional trial registry entries were surfaced in this search (most identified RCTs are older, pre-registry-era or indexed only via PubMed/meta-analysis) — verify clinicaltrials.gov directly for any currently active protocol before citing an NCT identifier.

---

## 13. Prevention

- **Primary prevention (most emphasized in the literature):** **Grain replacement** — substituting non-locally-grown, non-fungally-contaminated, Se-adequate grain for local subsistence grain — combined with **selenium supplementation programs**, is repeatedly identified as the most effective population-level intervention ("Comprehensive measures and change of grain were the most effective measures in preventing new cases" — [PMC6738986](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6738986/)). Improved/piped drinking water supply is a secondary component targeting the humic-acid pathway.
- **Public health programs:** China's national KBD control program (grain replacement + Se supplementation + water improvement + surveillance) has driven the detectable-rate decline from >20% to ~0% in children since 2019, with formal "elimination standard" achieved across monitored villages in the most recent 5-year evaluation ([BES Journal 2024](https://www.besjournal.com/en/article/doi/10.3967/bes2024.109)).
- **Secondary prevention/screening:** School- and community-based radiographic (hand/wrist X-ray) screening in endemic counties for early metaphyseal-lesion detection, enabling earlier selenium intervention during the still-open growth-plate window.
- **Tertiary prevention:** Ongoing selenium/nutritional maintenance plus symptomatic/surgical management to limit progression of secondary osteoarthritis and disability in already-affected individuals.
- **Genetic/counseling interventions:** Not applicable — KBD is environmentally driven; no prenatal or carrier-screening framework exists.
- **Note on residual risk:** Despite major national progress, Tibet is repeatedly flagged as an area where the disease remains "relatively active" with occasional new cases, underscoring that grain-replacement/selenium programs require sustained implementation rather than being a one-time fix ([PMC7792790](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7792790/); search synthesis above).

---

## 14. Other Species / Natural Disease

- KBD is essentially a **human-specific clinical entity** in the epidemiological/nosological literature; no naturally occurring veterinary counterpart with the identical name was identified in this search (searches for a livestock/equine "big bone disease" analog returned only human-disease sources and general equine selenium-deficiency nutrition references, e.g., [Merck Veterinary Manual](https://www.merckvetmanual.com/management-and-nutrition/nutrition-horses/nutritional-diseases-of-horses-and-other-equids)). Colloquially "Big Bone Disease" is sometimes used as a lay synonym for KBD itself, not a distinct veterinary disease.
- **Relevant comparative pathology:** Selenium-deficiency osteopathy/osteopathology has been documented in wildlife (e.g., endangered Patagonian huemul deer, *Hippocamelus bisulcus* — [PMC4522092](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4522092/)), representing a related but etiologically distinct Se-deficiency skeletal disorder rather than a validated KBD ortholog. This is comparative/analogous evidence, not a direct animal model of KBD.
- **Model organisms are used experimentally to induce KBD-like pathology (see §15)** rather than representing naturally occurring disease.

---

## 15. Model Organisms

- **Rat models (most validated):** Selenium-deficient diet (typically 4 weeks) followed by T-2 toxin exposure (typically 4 weeks) reliably reproduces chondronecrosis in the deep zone of knee articular cartilage, closely resembling human KBD histopathology; considered "a suitable animal model for studying etiological factors contributing to the pathogenesis (chondronecrosis) observed in human KBD" ([PubMed 22258458](https://pubmed.ncbi.nlm.nih.gov/22258458/); [PubMed 22294316](https://pubmed.ncbi.nlm.nih.gov/22294316/); [J Orthop Res](https://onlinelibrary.wiley.com/doi/10.1002/jor.22073)). A low-nutrition-diet + T-2 toxin variant has also been reported ([PubMed 23701828](https://pubmed.ncbi.nlm.nih.gov/23701828/)).
- **Other species tested:** Monkey, dog, pig, chicken, and rabbit models have been used with varying environmental-risk-factor interventions ([ScienceDirect comparative review](https://www.sciencedirect.com/science/article/pii/S0147651322002597)). **Important negative finding:** "rats, chicken and rabbits administrated Se deficiency failed to replicate KBD when selenium deficiency was used alone" — i.e., **Se deficiency alone is insufficient**; combined Se-deficiency + T-2 toxin exposure is required to recapitulate the phenotype, supporting the compound-etiology model over any single-factor hypothesis.
- **Model limitations:** No model fully replicates the chronic, multi-decade, growth-plate-specific human clinical course (short stature, dwarfism); most models assess acute-to-subacute chondronecrosis rather than the full skeletal growth-retardation phenotype.
- **Applications:** Rat models have been used to study oxidative stress (SOD/GSH-Px depletion, lipid peroxidation), chondrocyte apoptosis (Fas/p53/Bax/Bcl-xL), autophagy pathway involvement (AMPK/mTOR/ULK1), and to test candidate interventions (selenomethionine antagonism of T-2-induced apoptotic microRNAs; SIRT3-targeting siRNA delivery).
- **Resources:** No dedicated public KBD model-organism database was identified; relevant strain/protocol details are documented within primary publications rather than centralized repositories like MGI/RGD (standard rat strains, e.g., Wistar or Sprague-Dawley, are used under custom dietary/toxin protocols rather than genetically engineered KBD-specific lines).

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term(s) | Notes |
|---|---|---|
| Disease | MONDO:0005610 | Confirm via direct MONDO lookup |
| Causal gene (susceptibility) | HGNC ADAM12 (hgnc:188, verify), DIO2, GDF5, COL10A1 | Susceptibility, not monogenic-causal |
| Cell type | CL:0000138 (chondrocyte) | Zone-specific subtypes need verification |
| Biological process | GO:0006915 (apoptosis), GO:0070266 (necroptosis), GO:0022617 (ECM disassembly), GO:0016239 (autophagy) | Ferroptosis GO term needs current-OBO verification |
| Anatomy | UBERON terms for growth plate, articular cartilage, interphalangeal/knee/ankle joints | Verify exact IDs before binding |
| Chemical/exposure | CHEBI for T-2 toxin, selenium/selenite, humic/fulvic acid | ECTO for exposure-route terms |
| Treatment | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent selenium; NCIT:C15329/C16186 (Surgical); NCIT:C15302 (Physical Therapy) | |
| Phenotype | HP terms for arthralgia, joint enlargement, brachydactyly, short stature, joint stiffness | Full HPO cross-check recommended before final binding |

---

## Sources

- [Selenomethionine Antagonized microRNAs Involved in Apoptosis of Rat Articular Cartilage Induced by T-2 Toxin (PMC10467099)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10467099/)
- [Low selenium and T-2 toxin may be involved in the pathogenesis of KBD by affecting AMPK/mTOR/ULK1 pathway (ScienceDirect 2024)](https://www.sciencedirect.com/science/article/pii/S0147651324005797)
- [The Impact of Selenium Deficiency and T-2 Toxin on Zip6 Expression in KBD (PubMed 39455492)](https://pubmed.ncbi.nlm.nih.gov/39455492/)
- [Summary Analysis of National Surveillance on Kashin-Beck Disease from 1990 to 2023 (BES Journal)](https://www.besjournal.com/en/article/doi/10.3967/bes2024.109)
- [Fluorine impairs carboxylesterase 1-mediated hydrolysis of T-2 toxin (PMC9381868)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9381868/)
- [Kashin-Beck disease: From etiology to prevention (PMC3620638)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3620638/)
- [Monarch Initiative MONDO:0005610](https://monarchinitiative.org/MONDO:0005610)
- [Kashin-Beck Disease overview (ScienceDirect Topics)](https://www.sciencedirect.com/topics/immunology-and-microbiology/kashin-beck-disease)
- [A Metabolomics Study of Feces (PMC10650499)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10650499/)
- [A bivariate GWAS identifies ADAM12 as a novel susceptibility gene for KBD (PMC4992896)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4992896/)
- [ADAM12 GWAS (Scientific Reports)](https://www.nature.com/articles/srep31792)
- [Association study of candidate genes for KBD susceptibility in Tibetan population (BMC Med Genet)](https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-017-0423-6)
- [GPx6 downregulation drives ferroptosis in KBD chondrocytes (Apoptosis journal)](https://link.springer.com/article/10.1007/s10495-026-02389-w)
- [GPx6/ferroptosis (PMC13323611)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13323611/)
- [Mitochondrial function altered in KBD chondrocytes (PubMed 20650322)](https://pubmed.ncbi.nlm.nih.gov/20650322/)
- [Death of chondrocytes in KBD: Apoptosis, necrosis or necroptosis? (PMC6384500)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6384500/)
- [Magnetofection-mediated siRNA delivery targeting SIRT3 (PMC13440625)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13440625/)
- [p-ATF2 in chondrocyte apoptosis (PMC3726291)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3726291/)
- [Effects of selenium-mediated RUNX2 overexpression (PMC12714888)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12714888/)
- [Severe deformity in long-term Kaschin-Beck disease (Rheumatology, Oxford)](https://academic.oup.com/rheumatology/article/61/4/1732/6299414)
- [Kashin-Beck Osteoarthropathy in Rural Tibet (NEJM 1998)](https://www.nejm.org/doi/full/10.1056/NEJM199810153391604)
- [Conservative tibiotalocalcaneal fusion case report (PMC6709310)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6709310/)
- [Selenium supplementation NMA (ResearchGate)](https://www.researchgate.net/publication/328103541_Selenium_supplementation_for_treatment_of_kashin-beck_disease_A_network_meta-analysis)
- [Effectiveness of treatments for KBD systematic review/NMA (PubMed 31376086)](https://pubmed.ncbi.nlm.nih.gov/31376086/)
- [Five types of selenium supplementation NMA (PubMed 29511006)](https://pubmed.ncbi.nlm.nih.gov/29511006/)
- [Selenium for preventing KBD osteoarthropathy meta-analysis (PubMed 18693119)](https://pubmed.ncbi.nlm.nih.gov/18693119/)
- [Study on radiographic grading of ankle joint in adult KBD (PubMed 41342918)](https://pubmed.ncbi.nlm.nih.gov/41342918/)
- [Deep learning X-ray diagnostic method for KBD (ACM DL)](https://dl.acm.org/doi/fullHtml/10.1145/3653876.3653901)
- [Positive and confusing hand X-ray signs in KBD children (PMC5818476)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5818476/)
- [Transfer Learning Metaphyseal Sign Diagnostic Models (PMC11871940)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11871940/)
- [New clinical diagnostic/classification criteria for KBD sensitivity/specificity (BES Journal)](https://www.besjournal.com/article/doi/10.3967/bes2017.021)
- [Fine-Grained Differentiation-Based GNN for KBD diagnosis (PubMed 41398140)](https://pubmed.ncbi.nlm.nih.gov/41398140/)
- [Animal models of KBD exposed to environmental risk factors (ScienceDirect 2022)](https://www.sciencedirect.com/science/article/pii/S0147651322002597)
- [Oxidant damage in KBD rat model (PubMed 22294316 / J Orthop Res)](https://onlinelibrary.wiley.com/doi/10.1002/jor.22073)
- [Histopathology of chondronecrosis rat model (PubMed 22258458)](https://pubmed.ncbi.nlm.nih.gov/22258458/)
- [Animal model induced by low-nutrition diet + T-2 toxin (PubMed 23701828)](https://pubmed.ncbi.nlm.nih.gov/23701828/)
- [Increased chondrocyte apoptosis in KBD and rat model (BES Journal)](https://www.besjournal.com/article/doi/10.3967/bes2017.046)
- [Role of humic substances in drinking water in KBD (PubMed 10090708)](https://pubmed.ncbi.nlm.nih.gov/10090708/)
- [WISP1 involved in KBD pathogenesis via autophagy (MDPI)](https://www.mdpi.com/1422-0067/24/22/16037)
- [WISP1/autophagy (PMC10671535)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10671535/)
- [Pathophysiology and Treatment of KBD (Nature Index)](https://www.nature.com/nature-index/topics/l4/pathophysiology-and-treatment-of-kashin-beck-disease)
- [Prevention and control strategies for children KBD in China (PMC6738986)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6738986/)
- [Alterations in gut microbiota and metabolite profiles of KBD patients (PMC8553765)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8553765/)
- [Exploring gut microbiota role in KBD pathogenesis (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0306987725000453)
- [Serum metabolomic biomarkers in pediatric KBD (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0895398820301768)
- [Kashin-Beck Disease: A Risk Factor for Sarcopenia (PMC11678709)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11678709/)
- [Growth surveillance indices and KBD in children (PMC8999107)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8999107/)
- [Status of selenium and zinc in urine of children in KBD endemic areas (PMC9033266)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9033266/)
- [Gene Expression Analysis: GDF5 and DIO2 in KBD children (PMC4114804)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114804/)
- [Association study of selenoprotein gene polymorphisms and KBD in Tibetan population (PMC3751926)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3751926/)
- [Abnormal expression of TSG-6 disturbs ECM homeostasis (PMC9715581)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9715581/)
- [Histology of Kashin-Beck lesions (PubMed 11482529)](https://pubmed.ncbi.nlm.nih.gov/11482529/)
- [Proteoglycan metabolism, cell death and KBD (Glycoconjugate Journal)](https://link.springer.com/article/10.1007/s10719-012-9421-2)
- [Health-related quality of life in KBD lower than OA (PMC10161486)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10161486/)
- [Measuring HRQoL in KBD using EQ-5D (Quality of Life Research)](https://link.springer.com/article/10.1007/s11136-010-9820-4)
- [County-Level Hotspot Identification and Spatial Regression of Health Loss from KBD (PubMed 41255597)](https://pubmed.ncbi.nlm.nih.gov/41255597/)
- [Disease and Economic Burden of KBD - China 2021 (PubMed 38250701)](https://pubmed.ncbi.nlm.nih.gov/38250701/)
- [Prevalence and Risk Factors of Depression in KBD (PMC12440642)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440642/)
- [Kashin-Beck osteoarthropathy in rural Tibet in relation to selenium and iodine status (PubMed 9770558)](https://pubmed.ncbi.nlm.nih.gov/9770558/)
- [Selenium and iodine supplementation of rural Tibetan children (PubMed 12816783)](https://pubmed.ncbi.nlm.nih.gov/12816783/)
- [Assessing Health Loss from KBD in Qamdo District, Tibet (PMC7792790)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7792790/)
- [Spatial Distribution and Determinants of KBD in Gansu Province (PubMed 41984302)](https://pubmed.ncbi.nlm.nih.gov/41984302/)
- [Cold weather and Kashin-Beck disease (De Gruyter 2023)](https://www.degruyter.com/document/doi/10.2478/fzm-2023-0005/html?lang=en)
- [Osteopathology and selenium deficiency in Patagonian huemul (PMC4522092)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4522092/)
- [Kashin–Beck Disease: Risk Factor for Sarcopenia and Interaction with Selenium (OARSI 2025)](https://www.oarsijournal.com/article/S1063-4584(25)00356-5/fulltext)
- [Disordered glycometabolism in KBD pathogenesis (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0014482714001773)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 54 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 3 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 51 |
| On topic | 25 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3967/bes2024.109` (5 mentions) - Identifier did not resolve to a record
- `DOI:10.3967/bes2017.021` (3 mentions) - Identifier did not resolve to a record
- `DOI:10.3967/bes2017.046` (2 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC8999107` *(abstract only)*: "certain combinations of food substances high in protein had a protective effect"
  - Text part not found as substring: 'certain combinations of food substances high in protein had a protective effect' (note: only abstract available for PMID:35419096, full text may contain this excerpt)
- `PMC:PMC6738986` *(abstract only)*: "Comprehensive measures and change of grain were the most effective measures in preventing new cases"
  - closest text in source: "CONCLUSION: Comprehensive measures and change of grain were the most effective measures in preventing new case, whereas improvement of water and salt-rich selenium resulted in clinical improvements in children KBD."
- `PMID:22294316` *(abstract only)*: "a suitable animal model for studying etiological factors contributing to the pathogenesis (chondronecrosis) observed in human KBD"
  - closest text in source: "These changes were similar to those observed previously in KBD"
- `DOI:10.1002/jor.22073` *(abstract only)*: "a suitable animal model for studying etiological factors contributing to the pathogenesis (chondronecrosis) observed in human KBD"
  - closest text in source: "These changes were similar to those observed previously in KBD"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 34 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005610` (8 mentions) - the report calls it "classified as a subclass of osteochondrodysplasia", "Disease"; MONDO calls it **Kashin-Beck disease**
- `HP:0100729` (1 mention) - the report calls it "Large joint involvement — verify exact term"; HP calls it **Large face**
- `HP:0009824` (1 mention) - the report calls it "Osteolysis — not typical, avoid"; HP calls it **Upper limb undergrowth**
- `GO:0097707` (1 mention) - the report calls it "ferroptosis — if available as GO term/verify current OBO status"; GO calls it **ferroptosis**
- `CL:0000743` (1 mention) - the report calls it "growth plate chondrocyte context — verify exact CL binding"; CL calls it **hypertrophic chondrocyte**
- `CL:0000605` (1 mention) - the report calls it "articular chondrocyte, if resolvable"; CL calls it **fungal asexual spore**
- `UBERON:0001981` (1 mention) - the report calls it "growth plate cartilage — verify exact ID"; UBERON calls it **blood vessel**
- `UBERON:0001415` (1 mention) - the report calls it "interphalangeal joint"; UBERON calls it **skin of pelvis**
- `UBERON:0000004` (1 mention) - the report calls it "ankle joint region — verify"; UBERON calls it **nose**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011800` (1 mention) - the report calls it "Midface retrusion — N/A, omit"; HP calls it **Midface retrusion**
- `HP:0002751` (1 mention) - the report calls it "Kyphoscoliosis — occasional secondary"; HP calls it **Kyphoscoliosis**
- `GO:0007179` (1 mention) - the report calls it "TGF-beta receptor signaling"; GO calls it **transforming growth factor beta receptor signaling pathway**, and lists "TGF-beta receptor signaling pathway" among its other names
- `UBERON:0001465` (1 mention) - the report calls it "knee joint"; UBERON calls it **knee**, and lists "knee region" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0005610` - called "classified as a subclass of osteochondrodysplasia", "Disease"