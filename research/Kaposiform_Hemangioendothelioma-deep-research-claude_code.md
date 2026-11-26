---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-21T00:07:44.140925'
end_time: '2026-11-21T00:26:32.025824'
duration_seconds: 1127.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Kaposiform Hemangioendothelioma
  mondo_id: MONDO:0016236
  category: Neoplasm. Scope rules for this report - state any NF1 or NF2 change at
    gene level only; do not name or discuss chromosome-arm changes (in particular
    1p36, 11q or 17q) or chromothripsis; add nothing on ALK. The Kasabach-Merritt
    phenomenon has its own entry; cover it here as one step of this tumour.
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
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 74
  num_turns: 77
  total_cost_usd: 7.1728662500000056
  session_id: 71e03ce0-744d-4a86-9d22-69c20ae0e0fd
  stop_reason: end_turn
  tool_calls: 76
  retrieval_calls: 76
  assistant_text_blocks: 2
citation_count: 164
reference_validation:
  total_references: 129
  verified: 127
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.016
  quotes_checked: 53
  quotes_valid: 17
  quotes_unsupported: 36
  unsupported_quote_references:
  - DOI:10.1002/ped4.70041
  - PMC:PMC13291430
  - PMC:PMC8141909
  - PMID:31887709
  - PMC:PMC7962213
  - PMC:PMC8633177
  - PMID:22871490
  - PMC:PMC3494787
  - PMID:39369447
  - DOI:10.1002/ijc.35344
  - PMC:PMC11032113
  - PMID:41834121
  - PMID:27990590
  - PMID:38439088
  - PMID:39553205
  - PMC:PMC11560810
  - DOI:10.3389/fonc.2024.1336763
  - DOI:10.1002/pd.70180
  - PMC:PMC13377337
  - PMID:26783326
  - PMID:41389323
  - PMC:PMC12701870
  - PMID:25755958
  - DOI:10.1354/vp.41-6-695
  quotes_not_checkable: 2
  relevance_assessed: 127
  on_topic: 73
  off_topic: 1
  off_topic_references:
  - PMC:PMC11493338
  unresolved_references:
  - PMID:37274236
  - DOI:10.1038/3800444
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 14
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0001873
    reported_labels:
    - Acute, can rebound
    ontology_label: Thrombocytopenia
  - term_id: HP:0011900
    reported_labels:
    - EBI OLS
    ontology_label: Hypofibrinogenemia
  - term_id: HP:0001892
    reported_labels:
    - Episodic
    ontology_label: Abnormal bleeding
  - term_id: HP:0012531
    reported_labels:
    - Progressive then persistent
    - Chronic, often irreversible
    ontology_label: Pain
  - term_id: HP:0001004
    reported_labels:
    - Chronic, **irreversible, sirolimus-resistant
    ontology_label: Lymphedema
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kaposiform Hemangioendothelioma
- **MONDO ID:** MONDO:0016236 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Neoplasm. Scope rules for this report - state any NF1 or NF2 change at gene level only; do not name or discuss chromosome-arm changes (in particular 1p36, 11q or 17q) or chromothripsis; add nothing on ALK. The Kasabach-Merritt phenomenon has its own entry; cover it here as one step of this tumour.

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Kaposiform Hemangioendothelioma** covering all of the
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

I'll research this systematically, starting with the molecular genetics and core disease definition.

# Kaposiform Hemangioendothelioma (KHE) — Comprehensive Disease Characteristics Report

**Target:** Kaposiform hemangioendothelioma · **MONDO:0016236** · Category: Neoplasm (vascular tumour)
**Report date:** 21 November 2026 · **Evidence retrieved:** this session, via web/PubMed/Orphanet/ClinicalTrials.gov search

**Interpretation and scope statements (stated up front, as required):**

1. **Causal gene.** The template records "causal gene(s): not recorded," and this is correct in the germline sense — KHE is **not a Mendelian disorder and has no germline causal gene**. The recurrent **somatic (post-zygotic, mosaic) driver identified in KHE is *GNA14*** (G protein subunit alpha-14; OMIM \*604397, HGNC:4382, NCBI Gene 9630, 9q21.2), specifically the activating hotspot **c.614A>T, p.(Gln205Leu)** ([Lim et al., Am J Hum Genet 2016, PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/); [OMIM 604397](https://omim.org/entry/604397)). Single cases carry somatic *PIK3CA*, *GNAQ*, or *RAD50* variants instead (detailed in §4). All identifiers used below follow the identifiers supplied in the template.
2. **Scope rules applied as instructed.** Any *NF1*/*NF2* finding is reported at **gene level only**; no chromosome-arm change (including 1p36, 11q, 17q) or chromothripsis is named or discussed; **nothing is reported on ALK**. The **Kasabach–Merritt phenomenon (KMP)** is treated here as **one mechanistic step of this tumour**, not as a standalone disease (it has its own knowledge-base entry).
3. **Evidence-type labelling.** Claims are tagged *(human clinical)*, *(histopathology)*, *(in vitro)*, *(animal model)*, or *(inferred)* where the distinction matters.
4. **A note on direct quotes.** In this session I had web search but **no page-fetch tool**. Quoted fragments below are the verbatim strings returned in retrieved search-result content for the cited article; where I could not retrieve verbatim abstract text, I paraphrase and say so rather than fabricate a quote. Where a section could not be supported by retrieval, I say so explicitly instead of filling it from memory.

---

## 1. Disease Information

### Overview

Kaposiform hemangioendothelioma is a **rare, locally aggressive vascular tumour of intermediate (borderline) biological behaviour** that arises almost exclusively in neonates, infants and young children, presenting either as an infiltrative blue–purple cutaneous/subcutaneous mass or as a deep (retroperitoneal, mediastinal, visceral, osseous) lesion. Its defining complication is the **Kasabach–Merritt phenomenon** — profound thrombocytopenia with consumptive coagulopathy.

Orphanet defines it as "*a rare, locally aggressive, cutaneous or visceral vascular tumor characterized by either superficial lesions presenting as blue-purple infiltrated ill-defined plaques, or deep lesions usually manifesting with coagulation abnormality*," associated "*in about 3 out of 4 of cases with potentially lethal thrombocytopenia and consumption coagulopathy (Kasabach-Merritt phenomenon; KMP)*" ([Orphanet ORPHA:2122](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN)).

The authoritative modern review states that "*the main pathological features of KHE are abnormal angiogenesis and lymphangiogenesis*" and that KHE "*may develop into a life-threatening thrombocytopenia and consumptive coagulopathy, known as the Kasabach-Merritt phenomenon*" ([Ji et al., Orphanet J Rare Dis 2020;15:39, PMID 32014025](https://pmc.ncbi.nlm.nih.gov/articles/PMC6998257/)).

### Classification

- **ISSVA 2018 classification:** KHE sits in the category **"locally aggressive or borderline vascular tumours"** — i.e., between benign and malignant ([ISSVA Classification 2018](https://www.issva.org/UserFiles/file/ISSVA-Classification-2018.pdf); [Int J Mol Sci 2022;23:2358](https://www.mdpi.com/1422-0067/23/4/2358)).
- KHE and **tufted angioma (TA)** are widely regarded as **one clinicopathological spectrum** rather than two diseases ([Ann Diagn Pathol 2020, PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/); [PMC10173077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10173077/); [Clinical spectrum of KHE and TA, PMID 27607323](https://pubmed.ncbi.nlm.nih.gov/27607323/)).

### Key identifiers (retrieved)

| Resource | Identifier |
|---|---|
| Mondo | **MONDO:0016236** (as supplied; Mondo integrates Orphanet/OMIM/HPO — [Mondo via GARD](https://rarediseases.info.nih.gov/diseases/3077/kaposiform-hemangioendothelioma/)) |
| Orphanet | **ORPHA:2122** ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN)) |
| ICD-10 (per Orphanet mapping) | **C49.9** (malignant neoplasm of connective/soft tissue, unspecified) ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN)) |
| GARD | **3077** ([GARD](https://rarediseases.info.nih.gov/diseases/3077/kaposiform-hemangioendothelioma/)) |
| MalaCards | `kaposiform_hemangioendothelioma` ([MalaCards](https://www.malacards.org/card/kaposiform_hemangioendothelioma)) |
| Somatic driver gene | ***GNA14*** — OMIM **\*604397**, HGNC **4382**, NCBI Gene **9630**, 9q21.2 ([OMIM](https://omim.org/entry/604397)) |

**Not retrieved / not applicable:** There is **no OMIM phenotype MIM number** for KHE (expected, since it is a somatic-mosaic neoplasm, not a Mendelian phenotype) — I could not retrieve one. I could not retrieve a KHE-specific **ICD-11** code or a KHE-specific **MeSH** descriptor in this session (MeSH appears to subsume it under *Hemangioendothelioma*); these should be looked up directly before entry into the knowledge base.

### Synonyms and alternative names (retrieved usage)

- Kaposiform haemangioendothelioma (British spelling), **KHE**
- Within the KHE/TA spectrum: *tufted angioma* is a related/overlapping entity, not a synonym ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/))
- Historically conflated with **"Kasabach–Merritt syndrome"** and **"hemangioma with thrombocytopenia"** — MalaCards maintains a separate *Hemangioma-Thrombocytopenia Syndrome* card ([MalaCards](https://www.malacards.org/card/hemangioma_thrombocytopenia_syndrome_2)); this historical usage is a source of literature mis-indexing
- Descriptive synonym in older pathology literature: *"semi-malignant"/"low-grade malignant" vascular tumour of infancy* ([Altmeyers Encyclopedia](https://www.altmeyers.org/en/dermatology/kaposiform-hemangioendothelioma-128934))

### Information provenance

The evidence base is **almost entirely aggregated disease-level and case-series data, not EHR-derived population data.** The largest human datasets are single- or multi-centre referral cohorts: 107 referrals (Boston) ([PMID 22871490](https://pubmed.ncbi.nlm.nih.gov/22871490/)), 159 patients (multicentre, USA) ([Borst et al., Pediatr Blood Cancer 2024, doi:10.1002/pbc.30779](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779)), 269 patients with long follow-up (China) ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)), and a 2007–2024 Polish national multicentre series ([PMID 41466529](https://pubmed.ncbi.nlm.nih.gov/41466529/)). Expert consensus documents provide the normative layer ([Drolet et al., J Pediatr 2013, PMID 23796341](https://www.jpeds.com/article/S0022-3476(13)00399-5/fulltext); [Zhou et al., Int J Cancer 2025;156:1986–94, doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344); [VASCERN-VASCA, Eur J Pediatr 2026, PMID 41389323](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701870/)).

---

## 2. Etiology

### 2.1 Disease causal factors

KHE is a **sporadic, somatic-mosaic neoplasm**. The initiating lesion is a **post-zygotic activating mutation in an endothelial-lineage cell**, with no evidence of inheritance, infection, or environmental trigger.

- **Primary established cause:** somatic activating ***GNA14* p.(Gln205Leu)**. Lim et al. identified GNA14 Q205L in KHE alongside congenital tufted angiomas and childhood lobular capillary hemangiomas, and showed that "*GNA14 and GNA11 mutations induced changes in cellular morphology and rendered cells growth-factor independent by upregulating the MAPK pathway*" *(in vitro)* ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/)). The same hotspot causes tufted angioma with KMP ([PMID 31423605](https://pubmed.ncbi.nlm.nih.gov/31423605/)).
- **Alternative/rare drivers:** somatic ***PIK3CA*** (KHE reported as broadening the PIK3CA-related overgrowth spectrum — [Carli et al., Clin Genet 2021, doi:10.1111/cge.14047](https://onlinelibrary.wiley.com/doi/10.1111/cge.14047); sirolimus-responsive KHE with *PIK3CA* mutation, [PMID 37274236](https://pubmed.ncbi.nlm.nih.gov/37274236)); somatic ***GNAQ*** (a previously undescribed **GNAQ T96S** detected by droplet digital PCR in primary tibial KHE — [PMID 42103999](https://pubmed.ncbi.nlm.nih.gov/42103999/)); somatic ***RAD50*** in 1 of 5 KHEs ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)).
- **Mechanistic summary from the field's review:** "*Sporadic somatic mutations in genes such as GNA14, PIK3CA, and RAD50 have been identified in KHE*," and these "*are supposedly associated with abnormal VEGF-R activation and downstream PI3K/Akt/mTOR signaling in lymphatic endothelial cells (LECs), which trigger KHE growth*" *(inferred)* ([Tian et al., Pediatr Investig 2026, doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).
- **Important caveat:** driver detection is incomplete. In the 7-lesion (epi)genetic series, "*previously reported GNA14 mutations were not found*," with drivers identified in only 2/7 ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)). An unbiased exome study of one KHE found **germline missense variants in *TP53* and *APC* in both tumour and normal tissue** plus **81 candidate tumour-specific somatic events** (4 nonsense, 68 missense, 9 indels), highlighting *ITGB2*, *IL32*, *DIDO1* — none of which has been replicated ([PMID 28099595](https://pubmed.ncbi.nlm.nih.gov/28099595/)).
- The precise pathogenesis "*remains unclear*" by the field's own assessment ([doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).

### 2.2 Risk factors

**Genetic risk factors**
- **Causal somatic variants:** as above (*GNA14* Q205L principally). **No germline susceptibility locus, GWAS signal, or modifier gene has been reported** — I retrieved no GWAS Catalog, PheGenI, or ClinGen entry for KHE, and no familial clustering.
- **Co-occurring germline syndrome, gene level only (per scope rule):** a single adult-onset KHE has been reported in a patient with **neurofibromatosis type 1 (*NF1*)**; the authors note KHE "*had not previously been reported in patients with neurofibromatosis*," and that clinical suspicion was confounded because the skin findings mimicked neurofibromatosis-associated lesions ([PMID 30466240](https://pubmed.ncbi.nlm.nih.gov/30466240/)). This is **one case report and does not establish *NF1* as a KHE risk gene**. **No *NF2* alteration in KHE was retrieved.**
- Explicit negative: a somatic activating *NRAS* p.Q61R variant defines **kaposiform lymphangiomatosis (KLA)** and "*was absent in KHE samples*" — a useful molecular discriminator ([PMC6612206](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6612206/)).

**Non-genetic/clinical risk factors**
These are risk factors **for the severe KMP phenotype**, not for tumour occurrence:
- **Deep anatomical location:** "*The risk of KMP increases dramatically when tumor infiltrates muscle or when KHE arises in the retroperitoneum or mediastinum*" — retroperitoneal lesions 85% KMP, intrathoracic 100% ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)).
- **Younger age at onset (≤1 month), lesion size ≥6 cm, deep or non-extremity location** ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)).
- **Risk factors for chronic lymphedema:** lesion diameter ≥10 cm, mixed morphology, extremity involvement ([Orphanet J Rare Dis 2020, doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/)).
- **Risk factor for bone destruction:** later diagnosis (median age at diagnosis 19.0 months vs earlier in those without) ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)).
- **Age:** ~90% of KHE occurs under 1 year ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN)); 93% manifest in infancy, 60% as neonates ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)).
- **Sex, family history, toxins, lifestyle, occupation, radiation:** **no association retrieved.** Sex distribution is essentially equal (§9).

### 2.3 Protective factors

**None identified.** I retrieved **no genetic protective variant, modifier allele, dietary, lifestyle, or exposure-based protective factor** for KHE. gnomAD-type population-frequency arguments do not apply to a somatic-mosaic tumour driver. This section is genuinely empty in the literature, not merely unsearched.

### 2.4 Gene–environment interactions

**No gene–environment interaction has been described for KHE.** I retrieved no CTD, PheGenI, or GxE-database entry. The only quasi-"environmental" modifier with evidence is **pharmacological**: *PIK3CA*- and mTOR-pathway-mutant lesions respond to sirolimus ([PMID 37274236](https://pubmed.ncbi.nlm.nih.gov/37274236)), and *GNA14*-driven MAPK activation was proposed by Lim et al. as a **therapeutic target** — i.e., genotype-by-drug interaction rather than genotype-by-environment ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/)).

---

## 3. Phenotypes

Frequencies below are from the named cohorts; percentages differ between Western referral cohorts and Chinese tertiary cohorts, and both are shown where they diverge.

### 3.1 Core phenotype table

| Phenotype | Type | Frequency | Onset | Severity | Course | Suggested HPO |
|---|---|---|---|---|---|---|
| Enlarging infiltrative blue–purple cutaneous/subcutaneous mass | Clinical sign | 75% presenting feature ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)); 89% in Chinese cohort ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)) | Congenital–neonatal (84% present at birth in one cohort) | Moderate–severe | Progressive, rarely involutes | *Vascular neoplasm / cutaneous vascular tumour — specific HPO ID not verified in this session* |
| **Thrombocytopenia** | Laboratory abnormality | 56% at presentation ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)); 78% overall ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)) | Neonatal–infantile | Severe (often <25×10⁹/L; KMP defined broadly as <100×10⁹/L) | Acute, can rebound | **HP:0001873** |
| **Kasabach–Merritt phenomenon** (as one step of this tumour) | Composite lab + clinical | 71% ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)); 40.3% ([doi:10.1002/pbc.30779](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779)); range 42–71% ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)) | Usually at or soon after presentation; 11% develop it *after* initial presentation | Life-threatening | Acute/subacute, treatment-responsive | Composite: **HP:0001873** + **HP:0011900** + **HP:0001937** + **HP:0001892** |
| Hypofibrinogenemia / consumptive coagulopathy | Laboratory abnormality | Coagulation disorder in 100% of one Chinese cohort ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)) | With KMP | Severe | Acute | **HP:0011900**; **HP:0005521** (DIC-like) |
| Microangiopathic hemolytic anemia / anemia | Laboratory abnormality | Anemia 32.8% ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)) | With KMP | Moderate–severe | Acute | **HP:0001937**; **HP:0001903** |
| Bleeding / purpura / petechiae | Clinical sign | Reported as complication; frequency not retrieved | With KMP | Variable to life-threatening | Episodic | **HP:0001892** |
| Musculoskeletal pain / decreased function | Symptom | 23% presenting ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)); ~20% local pain/joint dysfunction ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)); 30–50% develop mild–moderate pain ([doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)) | Infantile–childhood; dominant presentation in older/non-cutaneous patients | Mild–severe, often chronic | Progressive then persistent | **HP:0012531** |
| Bone destruction / cortical erosion | Imaging + clinical sign | **26.0%** (70/269) ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)) | Median diagnosis 19.0 months | Severe | Progressive | *Osteolysis / bone destruction — HPO ID not verified* |
| Chronic pain + functional impairment in those with bone destruction | Symptom complex | **~70% within 2 years** ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)) | Childhood | Moderate–severe | Chronic, often irreversible | **HP:0012531** |
| **Chronic lymphedema** | Clinical sign | **11.0%** at 1 year post-onset; 84.6% of those moderate; **unilateral in all**, ipsilateral to KHE ([doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/)) | Childhood (post-onset) | Moderate | Chronic, **irreversible, sirolimus-resistant** | **HP:0001004** |
| Absent cutaneous findings (deep-only disease) | Presentation modifier | **11%** ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)) | Any | Associated with worse prognosis | — | — |
| Hyperhidrosis over lesion | Clinical sign | Reported as a differentiating feature between treatment groups ([PMID 43053660](https://pubmed.ncbi.nlm.nih.gov/43053660)) | Infantile | Mild | Variable | *Hyperhidrosis — HPO ID not verified* |
| Site-specific compressive complications | Clinical signs | Case-level: duodenal/intestinal obstruction, volvulus ([PMID 39709514](https://pubmed.ncbi.nlm.nih.gov/39709514/), [PMID 25755958](https://pubmed.ncbi.nlm.nih.gov/25755958/)); airway obstruction at birth ([PMC12651905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12651905/)); pericardial effusion ([JOVA 2024](https://journals.lww.com/jova/fulltext/2024/06000/kaposiform_hemangioendothelioma_of_the_mediastinum.5.aspx)); hydronephrosis, severe infection, hemorrhage ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)) | Neonatal–infantile | Severe | Acute | — |
| Raynaud phenomenon (rare) | Clinical sign | Single case ([PMC10655467](https://pmc.ncbi.nlm.nih.gov/articles/PMC10655467/)) | — | — | — | — |
| Immunological abnormality in neonatal KMP | Laboratory abnormality | 32 neonates: reduced CD3+CD4+ and CD3−CD19+ fractions, lower IgG vs controls; prolonged APTT and raised ferritin independently associated with severe thrombocytopenia ([PMID 42445171](https://pubmed.ncbi.nlm.nih.gov/42445171/)) | Neonatal | — | Acute | — |

**Behavioural phenotypes:** none intrinsic to KHE retrieved. No DSM/RDoC-mappable feature; psychosocial impact is secondary (see QOL).

### 3.2 Quality-of-life impact (per-phenotype where available)

A cross-sectional PedsQL™ 4.0 study of **91 children** with KHE (Infant Scales, Generic Core Scales, Family Impact Module) found that "*the scores of physiological and psychosocial domains in all age groups of patients with KHE were lower than those of normal children*," and that **KMP and activity dysfunction are independent risk factors for poor HRQOL** ([Ji group, PMID 35281237](https://pmc.ncbi.nlm.nih.gov/articles/PMC8907831/)).

- **Pain / functional phenotype → daily activity:** "*the infiltration of muscles, connective tissues and joint structures can cause pain and functional limitations, which may affect a patient's abilities to perform routine daily activities*" ([doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).
- **Caregiver burden:** family-impact scores were below 75 across physical, emotional, social, cognitive, communication, worry, daily-activity, family-relationship and **financial** domains ([PMID 35281237](https://pmc.ncbi.nlm.nih.gov/articles/PMC8907831/)).
- **Lymphedema phenotype → chronic disability:** irreversible and sirolimus-resistant, managed by compression ([doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/)); its clinical/management profile has been directly compared with primary lymphedema in children ([PMC11869848](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11869848/)).
- **EQ-5D / SF-36 / PROMIS data for KHE: none retrieved** (KHE is a paediatric disease; PedsQL is the instrument in use).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

| Gene | Identifiers | Role | Evidence |
|---|---|---|---|
| ***GNA14*** | OMIM \*604397; HGNC:4382; NCBI Gene 9630; 9q21.2; 7 exons; 355-aa protein ([OMIM](https://omim.org/entry/604397)) | **Principal recurrent somatic driver** | KHE, tufted angioma, lobular capillary hemangioma ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/)); TA+KMP ([PMID 31423605](https://pubmed.ncbi.nlm.nih.gov/31423605/)) |
| ***PIK3CA*** | — (ID not verified this session) | Rare alternative somatic driver | KHE within PIK3CA-related overgrowth spectrum ([doi:10.1111/cge.14047](https://onlinelibrary.wiley.com/doi/10.1111/cge.14047)); sirolimus-responsive case ([PMID 37274236](https://pubmed.ncbi.nlm.nih.gov/37274236)) |
| ***GNAQ*** | — | Rare alternative somatic driver | **GNAQ T96S**, previously undescribed, in primary tibial KHE by ddPCR ([PMID 42103999](https://pubmed.ncbi.nlm.nih.gov/42103999/)) |
| ***RAD50*** | — | Single-case somatic finding | 1/5 KHE ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)) |
| *ITGB2*, *IL32*, *DIDO1* | — | Unreplicated exome candidates | 1 KHE exome ([PMID 28099595](https://pubmed.ncbi.nlm.nih.gov/28099595/)) |

### 4.2 Pathogenic variants

- **Canonical variant:** ***GNA14* c.614A>T, p.(Gln205Leu)** — a **missense** change; "*All GNA14 mutations found were Q205L, with most caused by c.614A>T transversions*" across vascular-neoplasm series. ClinVar entry **VCV000548667** is annotated as reported "*in several unrelated individuals with GLUT-1 negative vascular tumors, including kaposiform hemangioendothelioma*" ([ClinVar 548667](https://www.ncbi.nlm.nih.gov/clinvar/variation/548667/?new_evidence=true)).
- **Variant class / consequence:** missense, **gain of function (constitutive activation)**. Mechanistically, Gln205 is the catalytic glutamine of the Gα GTPase: "*The conserved glutamine stabilizes the γ phosphate of GTP and orients a water molecule for nucleophilic attack*," and "*the Gln205Leu mutation shifts the residue 5.016 Å away from the catalytic water molecule, disrupting hydrolysis*," so that the mutant is "*predicted to impair GTP hydrolysis and lead to constitutive activation of the GTP-bound α-subunit*" ([Lim et al. 2016, AJHG PDF](https://www.cell.com/ajhg/pdf/S0002-9297(16)30213-0.pdf); mechanism review [Springer 2026](https://link.springer.com/article/10.1007/s00210-026-06088-w)).
- **Somatic vs germline:** **somatic/mosaic**, confined to lesional tissue. Detection typically requires high-sensitivity methods — ddPCR "*can detect GNA11 or GNA14 mutant cells with mutant allelic frequencies ranging from 0.3 to 5.0%*" and down to ~0.1% ([search-retrieved ddPCR performance data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4783707/); applied in KHE in [PMID 42103999](https://pubmed.ncbi.nlm.nih.gov/42103999/)).
- **Population allele frequency:** **not applicable / not meaningful.** As a somatic hotspot, Q205L is not expected in gnomAD/1000 Genomes constitutional data; I retrieved no population frequency and make no claim.
- **ACMG/AMP classification:** KHE variants are **somatic** and therefore classified under somatic (oncogenicity) frameworks, not germline ACMG/AMP tiers. I retrieved the ClinVar record's *reporting* context but **not** an explicit germline ACMG classification, and do not assert one.
- **Broader context:** *GNA14* is "*the most commonly mutated gene in vascular neoplasms*" per an 85-case cherry-hemangioma study, and GNA14/GNA11/GNAQ mutations are "*frequent in benign but not malignant cutaneous vascular tumors*" ([Nat/Mod Pathol 2019](https://www.nature.com/articles/s41379-019-0284-y); [PMC8141909](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8141909/)) — consistent with KHE's borderline, non-metastasising behaviour.

### 4.3 Modifier genes

**None identified.** No modifier-gene study for KHE was retrieved.

### 4.4 Epigenetic information

This is one of the better-characterised molecular layers:

> Genome-wide methylation profiling of **5 KHEs and 2 TAs**: "*Unsupervised hierarchical clustering analysis indicated a common methylation pattern of KHEs and TAs, which separated from the homogeneous methylation pattern of vascular malformations*," concluding that "*methylation profiling provided further evidence for KHEs and TAs potentially forming a spectrum of one entity*" ([ten Broek et al., Ann Diagn Pathol 2020, PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)).

No disease-specific DNA-methylation biomarker, histone modification, or chromatin-remodelling defect has been established beyond this classifier-style finding. I retrieved no ENCODE/Roadmap/DiseaseMeth KHE-specific entry.

### 4.5 Chromosomal abnormalities

**No recurrent cytogenetic abnormality is established in KHE.** A single **refractory** KHE has been reported in association with a **balanced chromosomal translocation** ([Zhou et al., Pediatr Dev Pathol 2016, doi:10.2350/15-09-1707-cr.1](https://doi.org/10.2350/15-09-1707-cr.1)); per this report's scope rules I do not restate the breakpoints. This observation is **unreplicated** and should not be treated as a diagnostic or classificatory feature. Chromosomal microarray and karyotyping have **no established role** in KHE diagnosis (see §10).

---

## 5. Environmental Information

- **Environmental factors:** **none identified.** No toxin, radiation, pollutant, or occupational exposure has been linked to KHE in the retrieved literature; I found no CTD/TOXNET/EPA entry for this disease. Given the congenital/neonatal onset in 60–84% of cases ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/); [PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)), a post-zygotic developmental mutational event is the operative model, leaving little temporal window for post-natal environmental causation *(inferred)*.
- **Lifestyle factors:** **not applicable** (paediatric, congenital-onset tumour). No maternal lifestyle association retrieved.
- **Infectious agents:** **explicitly excluded.** KHE is **HHV-8–negative**: "*HHV-8 immunohistochemical stain helps distinguish KS from KHE, as it is positive in KS while negative in KHE*," with HHV8 negative in 7/7 cases in one series, and "*the absence of human herpes virus 8 (HHV-8) in KHE indicates a different pathogenesis from Kaposi sarcoma despite the histological resemblance*" ([PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/); [PMC8633177](https://pmc.ncbi.nlm.nih.gov/articles/PMC8633177/)). No bacterial, fungal or parasitic agent implicated. *Secondary* infection is a treatment-related complication, not an etiology ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)).

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain — initiating lesion → clinical manifestation

1. **A post-zygotic somatic activating mutation arises in an endothelial-lineage precursor** in developing soft tissue — most often ***GNA14* c.614A>T p.(Gln205Leu)**; in individual cases *PIK3CA*, *GNAQ* (T96S), or *RAD50* instead — **which produces** a mosaic clone of mutant endothelial cells restricted to the lesion. *(human clinical + molecular: [PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/), [PMID 42103999](https://pubmed.ncbi.nlm.nih.gov/42103999/), [PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/))*
2. **Substitution of the catalytic Gln205 displaces the catalytic water and abolishes GTP hydrolysis**, **which results in** Gα14 being locked in its GTP-bound state → **constitutive Gq-family signalling**. *(structural/biochemical inference from Gα mechanism: [AJHG 2016](https://www.cell.com/ajhg/pdf/S0002-9297(16)30213-0.pdf))*
3. **Constitutive Gα14 signalling leads to MAPK/ERK pathway activation**, **which causes** altered endothelial-cell morphology and **growth-factor-independent proliferation** — demonstrated directly in transfected cells and in GNA14-Q205L endothelial xenografts, where "*ECs with GNA14 p.Gln205Leu implants displayed significantly higher vascularization compared to wild-type controls*." *(in vitro + animal model: [PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/); [Front Cell Dev Biol 2025](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1572909/full))*
4. **In parallel, VEGF-C→VEGFR-3 and ANGPT2→TIE2 receptor signalling converge on PI3K–AKT–mTOR in lymphatic endothelial cells**, **which drives** coupled **dysregulated angiogenesis and lymphangiogenesis** — the review states the "*pathophysiological basis is dysregulated lymphatic and blood vascular angiogenesis, primarily mediated by the vascular endothelial growth factor-C (VEGF-C)/vascular endothelial growth factor receptor-3 (VEGFR-3) and angiopoietin-2 signaling pathways*," and that "*Ang-2 ligand-induced Tie-2 activation triggers Akt/mTOR signaling, which in LECs is mainly mediated by PIK3CA*." **This step is inferred**, supported by pathway/expression data and by the therapeutic response to mTOR inhibition rather than by direct lineage-tracing in KHE. *([doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/); [PMID 32014025](https://pmc.ncbi.nlm.nih.gov/articles/PMC6998257/))*
5. **Clonal expansion of mutant endothelium produces the tumour mass**: infiltrating nodules and sheets of variably spindled endothelial cells with slit-like vascular channels, glomeruloid nests, and **malformed/abnormal lymphatic channels**, **which manifests as** an ill-defined mass crossing multiple tissue planes. *(histopathology: [EyeWiki/KHE histology synthesis](https://eyewiki.org/Kasabach-Merritt_Phenomenon); [PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/))*
6. **Hypoxic/HIF signalling amplifies the phenotype** — in a 3-D spheroid KHE model and EOMA xenografts, "*HIF-1α expression was significantly upregulated*," **which is proposed to further drive** angiogenic output. *(in vitro + animal model, mechanistically suggestive: [Front Cell Dev Biol 2025](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1572909/full))*

**Branch A — haematological (the Kasabach–Merritt step of this tumour; see its own entry):**

7. **Podoplanin-expressing, lymphatic-type tumour endothelium is exposed to flowing blood**, **which causes** platelet **CLEC-2** to engage tumour **podoplanin**: "*Binding of podoplanin to CLEC-2 transmits platelet activation signals via Src family kinases, which may account for platelet aggregation in kaposiform hemangioendothelioma*," and "*Platelet CLEC-2, tumor podoplanin interaction is considered the key mechanism of platelet clearance*." High-flow arteriovenous shunting within the lesion provides an additional activating stimulus. *(human clinical + in vitro: [PMID 32014025](https://pmc.ncbi.nlm.nih.gov/articles/PMC6998257/); [EyeWiki](https://eyewiki.org/Kasabach-Merritt_Phenomenon))*
8. **Platelet activation and physical trapping lead to intralesional platelet–fibrin microthrombi**, **which results in** secondary activation of the coagulation cascade and consumption of clotting factors → **profound thrombocytopenia, hypofibrinogenemia, raised D-dimer, microangiopathic hemolytic anemia = KMP**. *(human clinical + histopathology: microthrombi and hemosiderin are standard histological findings)*
9. **KMP leads to** purpura and bleeding diathesis, transfusion dependence, and — untreated — death; it also **feeds back** on the tumour, since Ang-2 release both marks and plausibly worsens endothelial destabilisation: Ang-2 was "*10-fold greater in KLA patients and 14-fold greater in KHE patients when the KMP coagulopathy was present but not when it was absent*." *(human clinical biomarker: [PMID 27990590](https://pubmed.ncbi.nlm.nih.gov/27990590/); [PMID 38439088](https://pubmed.ncbi.nlm.nih.gov/38439088/))*
10. **Chronic CLEC-2/GPVI engagement depletes platelet surface receptors**, **which causes** a superimposed **qualitative platelet defect**: "*CLEC-2 receptors on the platelet surface were significantly decreased in patients with KHE/Kasabach-Merritt phenomenon compared with healthy donors*," so that "*platelet responses induced by CLEC-2 or GPVI activation are impaired because of the diminished number of receptors*" — bleeding risk therefore exceeds what the platelet count alone predicts. *(human clinical: [Blood Adv 2023, PMID 37307200](https://pubmed.ncbi.nlm.nih.gov/37307200/))*
11. **Accompanying immune perturbation** — neonates with KMP show reduced CD3+CD4+ helper T-cell and CD19+ B-cell fractions and lower IgG, with prolonged APTT and raised ferritin independently associated with severe thrombocytopenia, **suggesting** an inflammatory/immune-activation component layered onto the coagulopathy. *(human clinical, associative: [PMID 42445171](https://pubmed.ncbi.nlm.nih.gov/42445171/))*

**Branch B — local structural/mechanical:**

12. **Infiltrative growth into muscle, fascia, joint capsule and bone leads to** cortical erosion and bone destruction (26.0% of patients), **which results in** periarticular and muscular **fibrosis** → chronic pain and decreased range of motion in ~70% of affected patients within 2 years, "*primarily attributed to the tumor's invasive growth and consequent periarticular and muscular fibrosis.*" *(human clinical: [J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340); [PMID 30233248](https://pubmed.ncbi.nlm.nih.gov/30233248/))*

**Branch C — lymphatic:**

13. **Involvement and obstruction of regional lymphatics leads to lymphatic stasis** — found in **100%** of involved lesions on lymphoscintigraphy — **which results in** chronic, largely **irreversible, sirolimus-resistant lymphedema** (11.0% at 1 year). *(human clinical: [PMC13545610](https://pmc.ncbi.nlm.nih.gov/articles/PMC13545610/); [doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/))*

**Therapeutic interruption of the chain (step 4 is the druggable node):**

14. **mTOR inhibition with sirolimus blocks the PI3K–AKT–mTOR node**, **which produces** reduced endothelial proliferation and migration, anti-lymphangiogenic and anti-fibrotic effects, and reduced platelet activation/inflammation: "*The prevention of platelet activation and inflammation, along with antiangiogenic effects, the inhibition of lymphangiogenesis, the attenuation of fibrosis, or a combination of all these effects, may be responsible for the therapeutic effects of sirolimus*" ([PMID 39369447](https://pubmed.ncbi.nlm.nih.gov/39369447/)). A direct cellular mechanism was identified in 2025: in CD31⁺ KHE cells isolated from patients, transcriptome sequencing "*revealed downregulation of ATG9B after sirolimus treatment*," and "*sirolimus may inhibit the proliferation of CD31+ KHE cells by suppressing the expression of ATG9B*," with reduced migration vs DMSO *(in vitro, patient-derived: [Li et al., J Cell Mol Med 2025, doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/))*.

### 6.2 Category checklist mapped onto the chain

- **Molecular pathways:** Gq/Gα14 → **MAPK/ERK** (steps 2–3); **VEGF-C/VEGFR-3** and **ANGPT2/TIE2** → **PI3K–AKT–mTOR** (step 4); **HIF-1α** (step 6); **CLEC-2 → Src/Syk** platelet signalling (step 7). Loss of TSC2 and PTEN function has also been invoked as a route to abnormal mTOR activation in KHE *(inferred, [doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/))*.
- **Cellular processes:** growth-factor-independent proliferation; angiogenesis; **lymphangiogenesis**; endothelial migration; platelet activation/aggregation and clearance; fibroblast-mediated fibrosis; inflammation with macrophage recruitment (CD68⁺ macrophages as a source of VEGF; IL-6 and TNFα as pro-angiogenic cytokines) *(partly general endothelial biology rather than KHE-specific — flagged as inferred)*; autophagy-related gene regulation (*ATG9B*).
- **Protein dysfunction:** **gain-of-function, GTPase-dead Gα14** (not misfolding/aggregation); constitutive GPCR-independent signalling output.
- **Metabolic changes:** **no KHE-specific metabolomic or energy-metabolism defect retrieved.** HIF-1α upregulation implies a hypoxia/glycolytic shift *(inferred only)*. Note the diagnostically relevant negative: lesional endothelium is **GLUT1 (SLC2A1)-negative**, distinguishing KHE from infantile hemangioma ([PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/)).
- **Immune involvement:** not autoimmune, not an immunodeficiency syndrome. Secondary findings: reduced helper-T/B fractions and IgG in neonatal KMP ([PMID 42445171](https://pubmed.ncbi.nlm.nih.gov/42445171/)); treatment-induced immunosuppression from sirolimus/corticosteroids is clinically important (§12).
- **Tissue damage mechanisms:** microthrombosis/ischemia within the lesion; **fibrosis** (periarticular, muscular) as the principal irreversible mechanism; bone erosion; haemorrhage.
- **Biochemical abnormalities:** no enzyme deficiency, receptor loss, or channelopathy. The core biochemical lesion is **defective GTP hydrolysis** by a Gα subunit.
- **Epigenetic changes:** shared KHE/TA methylation signature, distinct from vascular malformations ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)).
- **Molecular profiling:** **Transcriptomics** — bulk transcriptome sequencing of patient-derived CD31⁺ KHE cells ± sirolimus (*ATG9B*) ([doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)). **Proteomics, metabolomics, lipidomics: no KHE studies retrieved.** **Genomic structural features:** no recurrent structural variant (§4.5).
- **Advanced technologies:** **single-cell and spatial transcriptomics of KHE: none retrieved** — I searched specifically and found scRNA-seq studies only for Kaposi sarcoma and other sarcomas, not KHE. **Multi-omics integration and CRISPR/RNAi functional screens in KHE: none retrieved.** The field's stated obstacle is that "*KHE research faces challenges due to the lack of established cell lines and suitable animal models*" ([doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)).

### 6.3 Ontology term suggestions for mechanism

**Verified in this session:**
- **GO:0001946** — lymphangiogenesis ([AmiGO](https://amigo.geneontology.org/amigo/term/GO:0001946))
- **CL:0002138** — endothelial cell of lymphatic vessel (lymphatic endothelial cell / LEC) ([Cell Ontology](https://github.com/obophenotype/cell-ontology/blob/master/src/ontology/bridge/cl-bridge-to-uberon.obo))

**Suggested but ID not verified in this session (look up before ingestion):** *angiogenesis*; *platelet activation*; *platelet aggregation*; *blood coagulation*; *endothelial cell proliferation*; *endothelial cell migration*; *TOR signaling*; *Ras protein signal transduction / MAPK cascade*; *GTPase activity*; *response to hypoxia*; *autophagosome assembly*. Cell types: *blood vessel endothelial cell*; *platelet*; *fibroblast*; *macrophage*; *erythrocyte*.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary sites** (most-to-least frequent, per retrieved series): "*KHE most commonly involves the deep soft tissues of the extremities and the retroperitoneum, followed by the head and neck regions*," with additional primary sites including **pancreas** and **ischiorectal region** ([Springer Encyclopedia of Pathology entry](https://link.springer.com/rwe/10.1007/978-3-319-28845-1_5412-1); [PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/)).

Documented primary/involved organ sites in the retrieved case literature: skin and subcutis; skeletal muscle; **bone** (humerus [PMID 39031761](https://pubmed.ncbi.nlm.nih.gov/39031761/); femur [PMID 36405826](https://pubmed.ncbi.nlm.nih.gov/36405826/); tibia [PMID 42103999](https://pubmed.ncbi.nlm.nih.gov/42103999/); cervical spine [PMID 30896568](https://pubmed.ncbi.nlm.nih.gov/30896568); long bones, 12-case osseous series [PMID 41680958](https://pubmed.ncbi.nlm.nih.gov/41680958/)); **retroperitoneum** ([PMC10064051](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10064051/)); **mediastinum/thorax** ([JOVA 2024](https://journals.lww.com/jova/fulltext/2024/06000/kaposiform_hemangioendothelioma_of_the_mediastinum.5.aspx)); **pancreas** ([PMID 25755958](https://pubmed.ncbi.nlm.nih.gov/25755958/), [PMID 36072541](https://pubmed.ncbi.nlm.nih.gov/36072541/)); **spleen** ([Am J Hematol, doi:10.1002/ajh.26370](https://doi.org/10.1002/ajh.26370)); **GI tract** ([PMID 39709514](https://pubmed.ncbi.nlm.nih.gov/39709514/), [PMC6476061](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6476061/)); **liver, lung, bone marrow, brain** (adult multifocal case, [PMC10917883](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10917883/)); **skull base/cranial fossa with dural invasion** ([PMID 37354290](https://pubmed.ncbi.nlm.nih.gov/37354290), [PMID 36545011](https://pubmed.ncbi.nlm.nih.gov/36545011/)); **middle ear** ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2588910920300048)); **nasal cavity/endonasal** ([PMC13212465](https://pmc.ncbi.nlm.nih.gov/articles/PMC13212465/), [PMID 42026286](https://pubmed.ncbi.nlm.nih.gov/42026286/)); **oral cavity, gingiva, tonsil, sublingual gland** ([PMC8633177](https://pmc.ncbi.nlm.nih.gov/articles/PMC8633177/), [PMID 40281141](https://pubmed.ncbi.nlm.nih.gov/40281141/), [PMC3118378](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3118378/), [PMID 37275074](https://pubmed.ncbi.nlm.nih.gov/37275074/)); **eyelid** ([PMC10797699](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10797699/)).

**Secondary organ involvement / complications:** haematopoietic system (KMP); regional lymphatics (lymphedema, lymphatic stasis); joints (destruction, contracture); kidney (hydronephrosis from mass effect); heart (pericardial effusion, high-output states); airway (obstruction); intestine (obstruction, volvulus, intestinal failure — [PMC13365911](https://pmc.ncbi.nlm.nih.gov/articles/PMC13365911/)) ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)).

**Body systems involved:** integumentary, musculoskeletal, **cardiovascular (blood and lymphatic vasculature)**, haematological/coagulation, digestive, respiratory, and occasionally nervous (by local invasion). **Endocrine: not involved.**

### 7.2 Tissue and cell level

- **Tissues:** dermis and subcutaneous **adipose/connective tissue**; **skeletal muscle**; fascia; **bone (cortex, metaphysis, articular surface)**; synovium/periarticular soft tissue; visceral stroma.
- **Cell populations:** the neoplastic cell is an **endothelial cell with partial lymphatic differentiation**. Immunophenotype: diffusely **CD31+ and CD34+**; **focal/partial PROX1, D2-40 (podoplanin), LYVE-1 positivity**; **GLUT1-negative**; **HHV-8-negative** ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/); [PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/)). The original D2-40 study concluded that "*D2-40 positivity suggests lymphothelial differentiation of the neoplastic component of kaposiform hemangioendothelioma*" ([Mod Pathol, doi:10.1038/3800444](https://www.nature.com/articles/3800444)). Important nuance: in some cases D2-40/PROX1 expression is confined to **peripheral lymphatic channels rather than tumour cells**, and **glomeruloid structures lack these antigens** ([PMC13222785](https://pmc.ncbi.nlm.nih.gov/articles/PMC13222785/); [doi:10.1007/s00256-026-05245-9](https://link.springer.com/article/10.1007/s00256-026-05245-9)).
- **Non-neoplastic participants:** **platelets** (trapped/consumed); **erythrocytes** (microangiopathic fragmentation); **fibroblasts** (fibrosis); **macrophages** (VEGF source).
- **Cell Ontology:** **CL:0002138** (endothelial cell of lymphatic vessel) — verified. *Blood vessel endothelial cell*, *platelet*, *fibroblast*, *macrophage*, *erythrocyte* — IDs not verified here.

### 7.3 Subcellular level

No KHE-specific organelle pathology is described. Mechanistically implicated compartments *(inferred from the pathway, not from KHE imaging/proteomics)*: **plasma membrane** (Gα14 membrane association; VEGFR-3/TIE2 receptors; platelet CLEC-2–podoplanin interface), **cytosol** (MAPK and PI3K–AKT–mTOR cascades), **nucleus** (HIF-1α-driven transcription), and **autophagosome machinery** (*ATG9B*). **GO Cellular Component IDs not verified in this session.**

### 7.4 Localization and lateralization

- **UBERON (verified):** **UBERON:0002097** — skin of body ([Uberon](https://www.virtualflybrain.org/blog/2022/01/01/skin-of-body-uberon_0002097/)).
- **UBERON terms suggested, IDs not verified here:** subcutaneous adipose tissue; skeletal muscle tissue; retroperitoneal space; mediastinum; pancreas; spleen; long bone; synovial joint; lymphatic vessel.
- **Lateralization:** lesions are typically **solitary and unilateral**; in the lymphedema cohort, "*In all patients with lymphedema, a unilateral extremity was affected, along with ipsilateral KHE*" ([doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/)). **Multifocal disease occurs but is rare** ([multifocal KHE treated with sirolimus monotherapy, doi:10.1111/pde.70003](https://pmc.ncbi.nlm.nih.gov/articles/PMC12854918); multifocal neonatal KHE, [Pediatrics 2022](https://publications.aap.org/pediatrics/article/150/5/e2022056293/189664/Multifocal-Kaposiform-Hemangioendothelioma-in-a?autologincheck=redirected)); one report describes **bilateral symmetrical femoral KHE** ([PMID 36405826](https://pubmed.ncbi.nlm.nih.gov/36405826/)).

---

## 8. Temporal Development

### Onset

- **Age:** "*KHE manifested in infancy in 93% of cases, with 60% presenting as neonates*" ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)); Orphanet: "*about 90% of KHE occur in children under 1 year of age*," onset possible at all ages ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN)). In a Chinese cohort, 27% were neonates and lesions were present **at birth in 84%** ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)). Approximately half of cases are described as congenital ([encyclopedia entry](https://link.springer.com/rwe/10.1007/978-3-319-28845-1_5412-1)).
- **Median age at diagnosis:** 6.5 months (range 0.3–14.0) in the comparison with KLA ([PMC6612206](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6612206/)); **19.0 months** in those who develop bone destruction ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)).
- **Adult onset is genuinely rare** but established: the first adult series comprised 3 patients aged 64, 55 and 48 ([PMID 9322599](https://pubmed.ncbi.nlm.nih.gov/9322599/)); adult KHE lesions are smaller (two-thirds <2 cm) and **do not show thrombocytopenia**, in contrast to >50% of children ([PMID 30466240](https://pubmed.ncbi.nlm.nih.gov/30466240/)); adult multifocal and multi-bone presentations are described ([PMC10917883](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10917883/); [PMID 37522676](https://pubmed.ncbi.nlm.nih.gov/37522676/)).
- **Prenatal onset:** detectable antenatally; "*The combination of tumor growth, infiltrative margins, hypervascularity, and T2-hyperintense signal on MRI consistently supported the antenatal suspicion of KHE*," with 3 of 4 fetuses showing prenatal signs of evolving KMP ([Fraissenon et al., Prenat Diagn 2026, doi:10.1002/pd.70180](https://pmc.ncbi.nlm.nih.gov/articles/PMC13377337/)).
- **Onset pattern:** typically **acute to subacute** — a rapidly enlarging mass with abrupt haematological decompensation; deep/visceral lesions can be **insidious**, e.g. splenic KHE "*presenting as insidious consumptive coagulopathy*" ([doi:10.1002/ajh.26370](https://doi.org/10.1002/ajh.26370)).

### Progression

- **No formal staging system (AJCC/WHO) exists for KHE.** Instead, **risk stratification by severity of thrombocytopenia** is used: low-risk, high-risk, and extremely high-risk. In one cohort: **8 (11%) low-risk, 26 (37%) high-risk, 36 (52%) extremely high-risk**; "*Extremely high-risk cases have the highest mortality and the highest complication rate as well as irreversible functional damage; in contrast, patients in the low-risk group have minimal complications and the highest cure rate*" ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)).
- **Progression rate:** variable — rapid proliferative growth in infancy with acute KMP, then a slow chronic phase dominated by fibrosis. The tibial case showed "*lesion progression with cortical erosion and soft tissue extension*" over **11 months** ([PMID 42103999](https://pubmed.ncbi.nlm.nih.gov/42103999/)).
- **Course pattern:** **progressive, then chronic/stable with sequelae**, punctuated by episodic KMP flares and post-treatment rebound. "*Rebound growth occurred in 17.3% of patients upon sirolimus discontinuation*" ([PMID 39369447](https://pubmed.ncbi.nlm.nih.gov/39369447/)); a documented case of **KMP rebound during sirolimus therapy** exists ([PMC9391052](https://pmc.ncbi.nlm.nih.gov/articles/PMC9391052/)).
- **Duration:** **chronic**, frequently lifelong at the level of residual tissue change: "*residual lesions persist to some extent in all patients even after standard treatment*" and "*no intervention other than complete surgical excision can achieve a definitive 'cure'*" ([Zhou et al., Int J Cancer 2025, doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344); [doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)). At median 56 months' follow-up of 269 patients, **17.4% had active disease and/or altered body structures** ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)).
- **Treatment duration is severity-scaled:** "*patients without KMP or with small lesions typically require therapy for several months to a year, whereas those with extensive, infiltrative lesions complicated by KMP often require long-term management*" ([doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344)).

### Patterns

- **Spontaneous remission:** classically absent — "*Unlike infantile hemangiomas, KHE rarely undergoes spontaneous regression*" ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)) — but **now documented**: four infants with biopsy-proven KHE **without KMP** underwent spontaneous regression on conservative management, with serial MRI showing involution over **22–28 months** and no KMP or complications; the authors argue this "*challenges universal aggressive intervention, supporting observation for selected non-coagulopathic cases*" ([Xu et al., Pediatr Blood Cancer 2026, PMID 41834121](https://pubmed.ncbi.nlm.nih.gov/41834121/)). An older series followed five patients with cutaneous KHE long-term ([PMID 11706068](https://pubmed.ncbi.nlm.nih.gov/11706068/)).
- **Treatment-induced remission:** the norm with sirolimus ± prednisolone (§12).
- **Critical periods / windows of opportunity:**
 1. **Neonatal–early infantile window for KMP control** — KMP is the dominant mortality driver and responds within days–weeks to sirolimus + prednisolone ([Ji et al., Blood 2022;139:1619–30, doi:10.1182/blood.2021014027](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)).
 2. **The first ~2 years after diagnosis for musculoskeletal outcome** — ~70% of patients with bone destruction develop chronic pain/dysfunction within that window ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)); delayed diagnosis predicts bone destruction, making **early recognition the main modifiable determinant of disability**.
 3. **A prenatal window now exists** — first use of maternal sirolimus therapy for fetal KHE/KMP showed, on MRI 3 weeks after initiation, "*decreased extent of infiltration and reduced T2-signal intensity*," with postnatal platelet normalisation by 6 weeks on sirolimus + corticosteroid ([doi:10.1002/pd.70180](https://pmc.ncbi.nlm.nih.gov/articles/PMC13377337/)).

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| **Incidence** | **0.071 per 100,000 children per year** (Massachusetts, USA) | [Croteau et al. 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/) as cited in [doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/) and [Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN) |
| **Incidence (alternate expression)** | **~1/1,400,000 children per year** (North American study) | [Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN) |
| **Prevalence** | **0.91 per 100,000 children**; Orphanet lists overall prevalence as **"Unknown"** | [Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN); [doi:10.1002/ped4.70041](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/) |
| Trial-protocol incidence figure | ~0.071/100,000 | [NCT05324384](https://clinicaltrials.gov/study/NCT05324384) |

**No SEER, GBD, CDC or WHO KHE-specific estimate was retrieved** — KHE is not separately tabulated in these systems, and the available numbers derive from single-region referral-based ascertainment, so they likely **underestimate** true incidence (deep/visceral lesions without skin findings — 11% of cases — are easily missed).

### Genetic etiology parameters

Because KHE is caused by **post-zygotic somatic mutation**, the classical Mendelian parameters are **not applicable**, and I state this rather than inventing values:

- **Inheritance pattern:** **none — sporadic/somatic mosaic.** No familial case or vertical transmission retrieved. (Orphanet's gene page for *GNA14* exists as a gene record but does not establish Mendelian KHE inheritance — [Orphanet GNA14](https://www.orpha.net/en/disease/gene/GNA14?name=GNA14&amp=&mode=gene).)
- **Penetrance / expressivity / anticipation / carrier frequency / consanguinity / founder effects:** **not applicable**; none retrieved. (The exome study's incidental germline *TP53*/*APC* missense variants were present in both tumour and normal tissue of one patient and were not shown to be causal — [PMID 28099595](https://pubmed.ncbi.nlm.nih.gov/28099595/).)
- **Germline mosaicism:** no evidence; KHE mutations are **somatic and lesion-restricted** and would not be expected to recur in siblings *(inferred)*.
- **Geographic distribution of specific variants:** none described; *GNA14* Q205L has been reported across unrelated individuals without geographic clustering ([ClinVar 548667](https://www.ncbi.nlm.nih.gov/clinvar/variation/548667/?new_evidence=true)).

### Population demographics

- **Sex ratio:** essentially **1:1**. Two independent datasets: "*Equal gender distribution was observed*" ([PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/)); and 32 girls : 38 boys (slight male excess, 0.84:1 F:M) in a 70-patient cohort ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)).
- **Age distribution:** ~90% <1 year; 93% infantile; 60% neonatal; adult cases rare ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN); [PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/); [PMID 9322599](https://pubmed.ncbi.nlm.nih.gov/9322599/)).
- **Ethnic / geographic variation:** **none established.** Cohorts come from the USA, China, Poland, Egypt, Australia and Europe with broadly similar phenotypes ([doi:10.1002/pbc.30779](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779); [PMID 41466529](https://pubmed.ncbi.nlm.nih.gov/41466529/); [doi:10.1186/s43054-025-00362-x](https://link.springer.com/article/10.1186/s43054-025-00362-x); [PMID 42246503](https://pubmed.ncbi.nlm.nih.gov/42246503/)). Differences in reported KMP frequency (40% US vs 71% Boston referral vs ~78% thrombocytopenia in China) most plausibly reflect **referral and ascertainment bias, not population biology** *(inferred)*. One paper specifically addresses the under-recognised challenge of **diagnosing vascular anomalies in patients with skin of colour** ([PMC11495159](https://pmc.ncbi.nlm.nih.gov/articles/PMC11495159/)).

---

## 10. Diagnostics

### 10.1 Clinical/laboratory tests

**Core laboratory panel** (used for diagnosis, risk stratification, and monitoring):
- **Platelet count** — KMP broadly defined as **<100 ×10⁹/L** ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)); severity of thrombocytopenia drives risk group ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)).
- **Fibrinogen, D-dimer, PT/APTT** — hypofibrinogenemia and raised D-dimer define the consumptive coagulopathy; **fibrinogen stabilisation at week 4** was a trial endpoint ([doi:10.1182/blood.2021014027](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)). Prolonged **APTT** and raised **ferritin** independently associate with severe neonatal thrombocytopenia ([PMID 42445171](https://pubmed.ncbi.nlm.nih.gov/42445171/)).
- **CBC with film** — microangiopathic hemolytic anemia.
- **Platelet function testing** — CLEC-2/GPVI-induced aggregation is impaired, with reduced surface CLEC-2 ([PMID 37307200](https://pubmed.ncbi.nlm.nih.gov/37307200/)); currently a research-grade test.
- **LOINC codes:** not retrieved in this session; standard codes for platelet count, fibrinogen, D-dimer, APTT should be assigned at ingestion.

**Biomarkers**
- **Serum angiopoietin-2 (Ang-2)** is the best-supported circulating biomarker. Levels were "*14-fold greater in KHE patients when the KMP coagulopathy was present but not when it was absent*," and a **cut-off of 10,000 pg/mL** has been proposed to distinguish KLA and KHE-with-KMP from other vascular anomalies; after 12 months of sirolimus, Ang-2 falls, "*correlating with normalization of platelet counts and D-dimer reductions*" ([Le Cras et al., PMID 27990590](https://pubmed.ncbi.nlm.nih.gov/27990590/); [Hammill et al., PMID 38439088](https://pubmed.ncbi.nlm.nih.gov/38439088/); [Blood 2025 abstract on broader use](https://ashpublications.org/blood/article/146/Supplement%201/4877/555845/Use-of-angiopoietin-2-as-a-biomarker-in-vascular)). Ang-1 is also informative.
- **Genetic markers:** *GNA14* Q205L in lesional tissue (see §10.2).
- **No FDA-qualified biomarker for KHE** was retrieved.

**Imaging**
- **Ultrasound (first-line):** "*a poorly demarcated, heterogeneously mixed-echoic subcutaneous mass with rich vascularity, often displaying a characteristic 'branch-shape' flow pattern on 3-D color Doppler and increased stiffness on elastography*" ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)). Contrast-enhanced ultrasound has been applied in multi-organ abdominal KHE ([PMC12719487](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12719487/)).
- **MRI (modality of choice):** in a 64-case series, lesions are "*hypointense or isointense compared with muscle on T1-weighted sequences, and hyperintense on T2-weighted or inversion-recovery sequences*," with "*an infiltrative morphologic pattern that involves multiple tissue planes and has poorly defined borders, along with stranding of the adjacent subcutaneous fat and cutaneous thickening*," diffuse heterogeneous post-contrast enhancement, speckled/striated low-signal foci, and **no significant diffusion restriction** ([BMC Pediatr 2021;21:98, PMID 33657997](https://pubmed.ncbi.nlm.nih.gov/33657997/); [PMID 29536769](https://pubmed.ncbi.nlm.nih.gov/29536769/); [PMID 39511620](https://pubmed.ncbi.nlm.nih.gov/39511620/); [PMID 40495592](https://pubmed.ncbi.nlm.nih.gov/40495592/)).
- **Ultrasound radiomics (emerging):** diagnostic **accuracy 91.41%, sensitivity 77.44%, specificity 97.21%**, outperforming conventional ultrasound; "*radiomics showed excellent efficacy in the diagnosis of KHE, which is of great help in improving the early diagnosis rate*" ([PMID 39553205](https://pmc.ncbi.nlm.nih.gov/articles/PMC11560810/)).
- **Lymphoscintigraphy (emerging):** "*effectively characterizes lymphatic dysfunction in KHE, aiding in both initial diagnosis and long-term management of secondary lymphedema*," with **lymphatic stasis in 100%** of involved lesions ([PMC13545610](https://pmc.ncbi.nlm.nih.gov/articles/PMC13545610/)).
- **Angiography:** characterised for KHE with assessment of transcatheter arterial embolization value ([PMID 35070833](https://pubmed.ncbi.nlm.nih.gov/35070833/)).
- **¹⁸F-FDG PET/CT:** reported in retroperitoneal KHE with spinal involvement ([PMC9403054](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9403054/)).
- **Dermoscopy:** described for superficial lesions ([PMID 40653948](https://pubmed.ncbi.nlm.nih.gov/40653948/)).
- **Prenatal imaging:** fetal ultrasound (increased echogenicity, soft-tissue hypertrophy, hypervascularity), fetal MRI (T2-hyperintense infiltrative mass), plus **MCA Doppler, fetal echocardiography** for anemia/cardiac failure/hydrops ([doi:10.1002/pd.70180](https://pmc.ncbi.nlm.nih.gov/articles/PMC13377337/); [Egypt J Radiol Nucl Med 2023](https://link.springer.com/article/10.1186/s43055-023-01028-7)).
- **RadLex/DICOM codes:** not retrieved.

**Biopsy and pathology — the diagnostic gold standard**
"*The diagnosis is mostly based on pathological biopsy*" ([Front Oncol 2024](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1336763/full)).
- **Histology:** infiltrating nodules/sheets of **variably spindled endothelial cells**, **slit-like vascular channels**, **glomeruloid nests**, **absence of mitoses or nuclear atypia**, **microthrombi**, **hemosiderin deposition**, oedema, fibrosis, and **abnormal lymphatic channels** ([histology synthesis](https://eyewiki.org/Kasabach-Merritt_Phenomenon); [Pathology Outlines](https://www.pathologyoutlines.com/topic/softtissuehemangioendotheliomakaposiform.html)).
- **Immunohistochemistry panel:** **CD31+, CD34+**; **D2-40/podoplanin, PROX1, LYVE-1 focally or partially +** (sometimes only in peripheral lymphatics); **GLUT1 −**; **HHV-8 −** ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/); [PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/); [doi:10.1038/3800444](https://www.nature.com/articles/3800444)).
- A dedicated histological-differential review exists ([Pathology/Histopathology review](https://www.sciencedirect.com/science/article/abs/pii/S003130251640348X)).
- **Functional tests and electrophysiology (EEG/EMG/ECG/NCS):** **no role in KHE diagnosis**; not retrieved.

### 10.2 Genetic testing

- **Recommended approach:** **somatic (tumour-tissue) testing, not germline testing.** Because variant allele fractions are low, **high-sensitivity methods on lesional tissue** are required — ddPCR detected the *GNAQ* T96S in tibial KHE where other assays did not ([PMID 42103999](https://pubmed.ncbi.nlm.nih.gov/42103999/)), and ddPCR reaches ~0.1–5% VAF for GNA11/GNA14 ([retrieved ddPCR performance data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4783707/)).
- **Targeted single-gene/hotspot testing:** *GNA14* c.614A>T; consider *GNAQ*, *GNA11*, *PIK3CA* ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/); [doi:10.1111/cge.14047](https://onlinelibrary.wiley.com/doi/10.1111/cge.14047)).
- **Gene panels:** vascular-anomaly / childhood-cancer somatic panels have been piloted in vascular anomalies ([JOVA pilot study](https://www.ovid.com/jnls/jova/fulltext/10.1097/jova.0000000000000094~identifying-genetic-mutations-in-vascular-anomalies-using-a)). No KHE-specific validated panel was retrieved.
- **WES/WGS:** research utility demonstrated (identified GNA14 and the single-case candidate list) but **low clinical yield** given frequent driver-negative results ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/); [PMID 28099595](https://pubmed.ncbi.nlm.nih.gov/28099595/); [PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)).
- **Chromosomal microarray, karyotyping, FISH, mtDNA testing, repeat-expansion testing:** **no established role**; nothing retrieved supporting their use in KHE.
- **Clinical significance:** genetic testing is currently **confirmatory/research-oriented**, not required for diagnosis or treatment selection — sirolimus is given on clinical grounds.

### 10.3 Omics-based diagnostics

- **DNA methylation profiling** can separate KHE/TA from vascular malformations and is the most promising classifier-style omics assay, though it remains research-grade ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)).
- **RNA-seq:** used mechanistically on patient-derived CD31⁺ cells, not diagnostically ([doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)).
- **Proteomics, metabolomics, epigenomic clinical assays, liquid biopsy / circulating tumour DNA for KHE:** **none retrieved.** Serum Ang-2 is the only blood-based assay with clinical traction and is a protein biomarker rather than a liquid biopsy.

### 10.4 Clinical criteria and differential diagnosis

There is **no single validated diagnostic criterion set**; diagnosis rests on the triad of **clinical presentation + characteristic imaging + histopathology (with IHC)**, now formalised in three consensus documents: [Drolet et al. 2013 (PMID 23796341)](https://www.jpeds.com/article/S0022-3476(13)00399-5/fulltext), the [2025 Chinese/international consensus statement (doi:10.1002/ijc.35344)](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344) — developed by "*28 nationally peer-recognized experts in vascular anomalies and an expert in evidence-based medicine*" across three subgroups — and the European [VASCERN-VASCA pathways (PMID 41389323)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701870/), built using the nominal group technique.

**Differential diagnosis**

| Entity | Discriminating features |
|---|---|
| **Tufted angioma** | Same spectrum; epigenetically indistinguishable; usually less aggressive ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)) |
| **Infantile hemangioma** | **GLUT1-positive**; proliferates then involutes; KHE is GLUT1-negative ([PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/)) |
| **Congenital hemangioma (RICH/NICH)** | Distinct natural history; imaging and IHC differ ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)) |
| **Kaposi sarcoma** | **HHV-8 positive**; KHE HHV-8 negative and shows glomeruloid proliferations ([PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/)) |
| **Kaposiform lymphangiomatosis (KLA)** | **Somatic *NRAS* p.Q61R present in KLA, absent in KHE**; older at diagnosis (mean 52.8 vs median 6.5 months); multifocal mediastinal/pulmonary/abdominal/multi-bone; more refractory, overall survival ~34% ([doi:10.1186/s13023-019-1147-9](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6612206/)) |
| **Spindle cell hemangioma; verrucous venous malformation; cellular capillary hemangioma** | Histological distinction; spindle cell hemangioendothelioma is a key adult differential ([PMID 9322599](https://pubmed.ncbi.nlm.nih.gov/9322599/)) |
| **Klippel–Trénaunay syndrome** (prenatal differential) | Considered when unilateral limb hypertrophy + hypervascularity is seen antenatally ([Egypt J Radiol Nucl Med 2023](https://link.springer.com/article/10.1186/s43055-023-01028-7)) |
| **Post-traumatic hematoma** | KHE can mimic it clinically ([PMC9294492](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9294492/)) |

**Soft-tissue vascular tumour-like lesions in adults** are a documented source of ISSVA-classification pitfalls ([PMC11162993](https://pmc.ncbi.nlm.nih.gov/articles/PMC11162993/)).

### 10.5 Screening

**No screening programme exists or is indicated.** There is **no newborn screening, carrier screening, or cascade screening** for KHE — appropriate for a sporadic somatic neoplasm with no heritable risk. The only screening-like activity retrieved is **prenatal imaging surveillance of an already-suspicious fetal soft-tissue mass**, where "*The diagnosis of Kaposiform Hemangioendothelioma should be suspected in prenatal period if there is unilateral hypertrophy of limb which has evolved rapidly over a short interval of time and shows findings suggestive of Kasabach–Merritt Phenomenon*" ([Egypt J Radiol Nucl Med 2023](https://link.springer.com/article/10.1186/s43055-023-01028-7); [doi:10.1002/pd.70180](https://pmc.ncbi.nlm.nih.gov/articles/PMC13377337/)).

---

## 11. Outcome / Prognosis

### Survival and mortality

| Measure | Value | Source |
|---|---|---|
| Historical mortality (untreated/pre-sirolimus KMP) | **20–30%**; 12–30% across 1991–2009 | [PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/) |
| Historically quoted KMP mortality | 10–30% | [PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/) |
| **Current mortality (sirolimus era)** | **<2%** | [doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344) |
| Multicentre cohort (n=159) | **1.3%** (2 deaths) | [doi:10.1002/pbc.30779](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779) |

**No 5-year or 10-year survival rate, life-expectancy figure, or disease-specific mortality rate per 100,000 was retrieved** — KHE is not tabulated in SEER/CDC WONDER/GBD, and the field reports crude cohort case-fatality instead. I therefore do not state survival percentages beyond the above.

### Morbidity and function

Morbidity — not mortality — is now the dominant outcome problem:
- **Residual disease is universal:** "*residual lesions persist to some extent in all patients even after standard treatment*" ([doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344)).
- **17.4%** had active disease and/or altered body structures at median 56 months ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)).
- **Bone destruction in 26.0%**, with chronic pain and functional impairment in **~70% of those** within 2 years, predominantly lower extremity and worse with articular-surface/metaphyseal involvement ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)).
- **Chronic lymphedema in 11.0%** at one year, unilateral, mostly moderate, **irreversible and sirolimus-resistant** ([doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/)).
- **Pain in 30–50%**, with limb dysfunction from fibrosis/adhesion ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).
- **HRQOL is reduced across physiological and psychosocial domains in all age bands, with KMP and activity dysfunction as independent risk factors**; caregiver HRQOL is also impaired, including financial burden ([PMID 35281237](https://pmc.ncbi.nlm.nih.gov/articles/PMC8907831/)). **No ICF-coded disability dataset retrieved.**

### Complications

Hemorrhage; severe infection (both disease- and treatment-related); hydronephrosis; anemia (32.8%); airway, intestinal, duodenal and pericardial compromise by site; bone/joint destruction; chronic lymphedema; intestinal failure (resolved with medical therapy plus near-fat-free oral feeding in one report — [PMC13365911](https://pmc.ncbi.nlm.nih.gov/articles/PMC13365911/)); **sirolimus-related severe thrombocytopenia** in progressive disease ([PMID 36688881](https://pubmed.ncbi.nlm.nih.gov/36688881/)); **rebound growth in 17.3% on sirolimus discontinuation** ([PMID 39369447](https://pubmed.ncbi.nlm.nih.gov/39369447/)); **local recurrence ~15% after incomplete resection** ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).

### Recovery potential

- **With treatment:** haematological recovery is the rule — 35/37 achieved durable platelet response at week 4 on sirolimus + prednisolone ([doi:10.1182/blood.2021014027](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)); **92.2% (154 patients) had a durable response to sirolimus** in long-term follow-up ([Zhou et al., Int J Cancer 2023;153:600–608, doi:10.1002/ijc.34509](https://onlinelibrary.wiley.com/doi/10.1002/ijc.34509)). Complete anatomical cure requires complete excision, which is often not feasible.
- **Without treatment:** spontaneous regression is possible in **selected KMP-negative lesions** (4 infants, MRI involution over 22–28 months) ([PMID 41834121](https://pubmed.ncbi.nlm.nih.gov/41834121/)), but KHE "*does not regress spontaneously*" in the general case and "*tends to metastasize locally as well as to the regional lymph nodes*" ([PMC7962213](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/)).
- **Low-risk group:** "*no patients who underwent surgery experienced recurrence during the maximum follow-up of five years*"; this group has "*minimal complications and the highest cure rate*" ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)).

### Prognostic factors and biomarkers

- **Adverse:** presence/severity of KMP; **deep lesions without cutaneous involvement, especially retroperitoneal or mediastinal**; infiltration of muscle; large size (≥6 cm for KMP risk, ≥10 cm for lymphedema); **later diagnosis** (predicts bone destruction); extremely-high-risk stratum; delayed/inadequate treatment ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/); [PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/); [PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/); [PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)).
- **Prognostic/monitoring biomarkers:** platelet count (primary), fibrinogen, D-dimer, and **serum Ang-2** (falls with response, concordant with sirolimus response) ([PMID 27990590](https://pubmed.ncbi.nlm.nih.gov/27990590/); [PMID 38439088](https://pubmed.ncbi.nlm.nih.gov/38439088/)). In neonatal KMP, **prolonged APTT and elevated ferritin** independently predict severe thrombocytopenia ([PMID 42445171](https://pubmed.ncbi.nlm.nih.gov/42445171/)).
- **No validated multivariable prognostic model or clinical calculator for KHE was retrieved.**

---

## 12. Treatment

### 12.1 Pharmacotherapy

**First-line: sirolimus (rapamycin), an mTOR inhibitor — NCIT term: *Sirolimus* (NCIT code not verified in this session).**

- "*Sirolimus has been established as the first-line therapy for KHE*," and its introduction "*has fundamentally improved patient outcomes, reducing mortality to below 2%*" ([Front Oncol 2024](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1336763/full); [doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344)).
- **Mechanism:** mTOR/PI3K/AKT inhibition with reduced VEGF production, inhibition of endothelial growth and angiogenesis, anti-lymphangiogenic and anti-fibrotic effects, reduced platelet activation and inflammation, plus T-cell inhibition; at cellular level, suppression of **ATG9B** in CD31⁺ KHE cells ([PMID 39369447](https://pubmed.ncbi.nlm.nih.gov/39369447/); [doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)).
- **Pivotal prospective evidence:** Adams et al. phase II in complicated vascular anomalies — 12 courses of 28 days; "*sirolimus was efficacious and well tolerated in these study patients with complicated vascular anomalies, with clinical activity reported in the majority of the disorders*" ([PMID 26783326](https://pubmed.ncbi.nlm.nih.gov/26783326/)). Earlier KHE-specific experience: [PMID 26864138](https://pubmed.ncbi.nlm.nih.gov/26864138/); long-term single cases [PMID 30002799](https://pubmed.ncbi.nlm.nih.gov/30002799/).
- **Dosing (as used in the randomised trial):** sirolimus **0.8 mg/m² twice daily**, adjusted monthly to **trough 10–15 ng/mL** ([NCT03188068](https://clinicaltrials.gov/study/NCT03188068); [doi:10.1182/blood.2021014027](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)).
- **Dose intensity is now being de-escalated:** a randomised clinical trial compared **high- vs low-dose sirolimus** in KHE ([PMID 40107509](https://pubmed.ncbi.nlm.nih.gov/40107509/)); low-dose regimens have been reported successful in neonates/infants ([PMC12284785](https://pmc.ncbi.nlm.nih.gov/articles/PMC12284785/)).
- **Topical sirolimus** has been tested in a randomised phase II trial for cutaneous vascular anomalies ([PMID 40040594](https://pubmed.ncbi.nlm.nih.gov/40040594/)) and used with oral propranolol in superficial KHE ([PMC11180431](https://pmc.ncbi.nlm.nih.gov/articles/PMC11180431/)).

**Corticosteroids — NCIT term: *Prednisolone*.**
- **Sirolimus + prednisolone is superior to sirolimus alone for KHE with KMP.** In the randomised trial (n=73): "*At week 4, a durable platelet response was achieved by 35 of 37 patients given sirolimus and prednisolone compared with 24 of 36 patients given sirolimus monotherapy (difference 27.9%; 95% confidence interval, 10.0-44.7)*," with better median platelet counts weeks 1–4, more fibrinogen stabilisation at week 4, and better objective lesion response at month 12; the authors conclude "*sirolimus plus prednisolone should be considered a valid treatment of KHE with KMP*" ([Ji et al., Blood 2022;139:1619–30](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)). Prednisolone **2 mg/kg once daily**, taperable and stoppable within 4–6 weeks on satisfactory response ([NCT03188068](https://clinicaltrials.gov/study/NCT03188068)).
- **Corticosteroid-to-sirolimus sequential therapy** has been described as a strategy in infantile KHE with KMP ([PMID 41141660](https://pubmed.ncbi.nlm.nih.gov/41141660/)); sirolimus + glucocorticoid combinations are reported ([Medicine 2024](https://journals.lww.com/md-journal/fulltext/2024/04050/sirolimus_combined_with_glucocorticoids_in_the.10.aspx)).

**Vincristine — NCIT: *Vincristine* (NCIT C933, per retrieved NCIT reference).**
- The 2013 expert consensus recommended **vincristine (± corticosteroids) as first-line** for KHE with KMP ([PMID 23796341](https://www.jpeds.com/article/S0022-3476(13)00399-5/fulltext)).
- It remains important: a 19-year single-centre series (Sydney) found "*Vincristine remains a highly effective first-line treatment for kaposiform haemangioendothelioma with an acceptable safety profile*" — 16/21 (76%) received vincristine, 3 (14%) escalated to sirolimus; complications were "*common but mild in most cases*" ([Kirk et al., J Paediatr Child Health 2026, PMID 42246503](https://pubmed.ncbi.nlm.nih.gov/42246503/)).
- In the US multicentre cohort, vincristine gave **higher 3-month radiologic response than sirolimus (72.7% vs 20%, p = .03)** but no difference at 6 months and no difference in recurrence/progression ([doi:10.1002/pbc.30779](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779)).
- **VASCERN guidance:** "*In cases where there is a life-threatening localisation or failure to respond to sirolimus and corticosteroids, vincristine should be added to the therapeutic regimen*" ([PMID 41389323](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701870/)).

**Other agents reported in use** ([Front Oncol 2024](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1336763/full); [PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)): **propranolol / oral β-blockers**, **aspirin** (low-dose; three-case series in KHE with coagulopathy — [PMID 41895209](https://pubmed.ncbi.nlm.nih.gov/41895209/)), **intravenous immunoglobulin**, **platelet transfusion and cryoprecipitate** (supportive), anti-inflammatory therapy, haemostatic therapy. **Topical tacrolimus with compression bandaging** succeeded in one case ([PMID 35700108](https://pubmed.ncbi.nlm.nih.gov/35700108/)).
- **β-blocker vs sirolimus comparison (2026, Beijing):** 13 β-blocker vs 11 sirolimus patients; at 9 months, >25%/>50%/>75% regression in **76.9%/46.2%/23.1%** (β-blocker) vs **100.0%/72.7%/18.2%** (sirolimus); discontinuation in 9/13 vs 3/11 (median 40.0 vs 18.0 months) with **no recurrence after cessation**; safety events "*reversible and manageable*," but "*baseline imbalances limit direct comparison*" ([PMID 43053660](https://pubmed.ncbi.nlm.nih.gov/43053660)).

**Pharmacogenomics**
No KHE-specific pharmacogenomic study was retrieved. General sirolimus pharmacogenetics are directly relevant: sirolimus "*is a substrate of the ABCB1 pump (p-glycoprotein) and metabolized by the CYP3A4 and CYP3A5 enzymes*," and **weight plus *CYP3A5* genotype** are the covariates affecting clearance; a paediatric model recommended 0.20 mg/kg/day split BID for *CYP3A5\*3/\*3* vs 0.23 mg/kg/day for *CYP3A5\*1* carriers (5–30 kg) ([PMC7300220](https://pmc.ncbi.nlm.nih.gov/articles/PMC7300220/); [PMC4628029](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4628029/)). *ABCB1* SNP effects were not significant in one transplant study. Model-informed precision dosing in children is an active area ([PMC10069443](https://pmc.ncbi.nlm.nih.gov/articles/PMC10069443/)). **This is extrapolated from non-KHE sirolimus populations — flagged as inferred.**

### 12.2 Advanced therapeutics

- **Gene therapy, cell therapy, RNA-based therapy (ASO/siRNA/mRNA), CAR-T, checkpoint inhibitors, therapeutic monoclonal antibodies:** **none exist for KHE; none retrieved.** No clinical trial of any of these for KHE was found.
- **Targeted therapy** in KHE currently means **mTOR inhibition**. A rational but as-yet-untested extension follows from the biology: Lim et al. framed GNA14-driven MAPK activation as identifying "*potential targets for therapeutic intervention*" ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/)), and MEK inhibition is being used in adjacent complex lymphatic anomalies (trametinib efficacy/safety study — [PMID 41116710](https://pubmed.ncbi.nlm.nih.gov/41116710/)). **I found no trial or case series of MEK inhibition specifically in KHE**, and make no efficacy claim.

### 12.3 Surgical and interventional

- **Surgical resection** is the only modality that can cure: "*complete surgical resection has been touted as the gold standard for cure of KHE*," but "*total resection is often not a viable option given the high risk of morbidity and mortality*," and **incomplete resection carries ~15% local recurrence** with progression risk ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).
- **Indications:** "*small, well-localized lesions that are not complicated by KMP, or as an adjunct to systemic pharmacotherapy in the management of refractory disease*"; pharmacotherapy failure lowers the threshold for resecting a cosmetically or functionally problematic lesion ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/); [doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344)).
- **Risk-group practice:** surgery was primary for low-risk patients (no recurrence to 5 years) and used in 92% of the high-risk group; "*Early surgical intervention may be the most definitive treatment option for most patients with KHE*" ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)). Curative operations for visceral disease are documented, e.g. a neonate with pancreatic KHE and duodenal obstruction "*cured by Whipple operation*" ([PMID 25755958](https://pubmed.ncbi.nlm.nih.gov/25755958/)); chest-wall resection ([doi:10.1177/2050313x16684742](https://doi.org/10.1177/2050313x16684742)); congenital intracranial KHE resected ([PMC9012330](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9012330/)).
- **Transarterial embolization (TAE):** "*can be considered as a temporary measure for life-threatening KMP or as a preoperative adjunct*," but is "*relatively contraindicated for lesions involving critical regions such as the intracranial space or hepatic hilum*" ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)); angiographic characteristics and TAE value have been formally analysed ([PMID 35070833](https://pubmed.ncbi.nlm.nih.gov/35070833/)); commentary on TAE in neonatal KMP ([PMC9251004](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9251004/)).
- **NCIT intervention terms suggested (codes not verified here):** *Surgical Resection*, *Therapeutic Embolization*, *Compression Therapy*, *Platelet Transfusion*.

### 12.4 Supportive and rehabilitative

- **Haematological support:** platelet transfusion, cryoprecipitate, immunoglobulin — used judiciously, as transfused platelets are consumed by the same trapping mechanism *(mechanistic inference from §6 Branch A)* ([Front Oncol 2024](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1336763/full)).
- **Pain control** for the 30–50% with pain ([PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).
- **Compression therapy** is the mainstay for chronic lymphedema besides oral sirolimus ([doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/)); management parallels and differs from primary paediatric lymphedema ([PMC11869848](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11869848/)).
- **Nutritional support:** near-fat-free oral feeding plus medical therapy resolved KHE-related intestinal failure in one report ([PMC13365911](https://pmc.ncbi.nlm.nih.gov/articles/PMC13365911/)).
- **Physical/occupational therapy:** indicated for joint contracture and decreased range of motion given the ~70% rate of chronic functional impairment with bone destruction ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340); [PMID 30233248](https://pubmed.ncbi.nlm.nih.gov/30233248/)) — **I retrieved no KHE-specific rehabilitation protocol or trial**, so this is a clinical extrapolation.

### 12.5 Experimental treatments / active trials (ClinicalTrials.gov, retrieved)

| NCT | Title / question | Status (as retrieved) |
|---|---|---|
| [NCT03188068](https://clinicaltrials.gov/study/NCT03188068) | Sirolimus vs sirolimus + prednisolone for KHE | Published as [Blood 2022](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus) |
| [NCT02110069](https://clinicaltrials.gov/study/NCT02110069) | Vincristine vs sirolimus for high-risk vascular tumours (randomised phase 2) | Protocol public |
| [NCT04448873](https://clinicaltrials.gov/study/NCT04448873) | Guided discontinuation vs maintenance sirolimus in paediatric KHE (RCT) | **Completed** (primary completion Feb 2023) |
| [NCT04077515](https://clinicaltrials.gov/study/NCT04077515) | Safety/efficacy of low-dose sirolimus in KHE | Listed |
| [NCT04775173](https://clinicaltrials.gov/study/NCT04775173) | Different sirolimus concentrations in KHE | Listed |
| [NCT05324384](https://clinicaltrials.gov/study/NCT05324384) | Different sirolimus doses for maintenance | **Recruiting** (West China Hospital) |
| [NCT05351216](https://clinicaltrials.gov/study/NCT05351216) | Effect of sirolimus on **immunizations** during KHE treatment | Listed |
| [NCT07131644](https://clinicaltrials.gov/study/NCT07131644) | Three sirolimus **discontinuation strategies** (RCT) | **Recruiting** (started 13 Sep 2025; primary completion ~1 Sep 2027) |
| [NCT07656909](https://clinicaltrials.gov/study/NCT07656909) | **Low- vs high-dose sirolimus with prednisolone** for KHE and KMP | Listed |

The trial portfolio is notably **entirely sirolimus-centric**, now focused on dose minimisation and safe discontinuation rather than new agents.

### 12.6 Treatment outcomes and adverse events

- **Response rates:** overall response >70% ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)); >60% at 3 months and >70% at 6 months in the multicentre cohort ([doi:10.1002/pbc.30779](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779)); **92.2% durable response** to sirolimus long-term ([doi:10.1002/ijc.34509](https://onlinelibrary.wiley.com/doi/10.1002/ijc.34509)).
- **Sirolimus toxicity (phase II, grade ≥3 attributable):** **blood/bone marrow 27%**, gastrointestinal 3%, metabolic/laboratory 3% ([PMID 26783326](https://pubmed.ncbi.nlm.nih.gov/26783326/)). Paradoxical **sirolimus-related severe thrombocytopenia** in progressive KHE is reported ([PMID 36688881](https://pubmed.ncbi.nlm.nih.gov/36688881/)); a systematic review of oral sirolimus safety in childhood diseases is available ([PMC9497617](https://pmc.ncbi.nlm.nih.gov/articles/PMC9497617/)). Infection risk and **vaccination timing** are live clinical issues ([NCT05351216](https://clinicaltrials.gov/study/NCT05351216)).
- **Vincristine toxicity:** complications "*common but mild in most cases*," with one proven bloodstream infection and one central-line replacement in 16 treated patients ([PMID 42246503](https://pubmed.ncbi.nlm.nih.gov/42246503/)).
- **Resistance/relapse:** rebound growth in **17.3%** on discontinuation; sirolimus-resistance mechanisms remain unresolved ([PMID 39369447](https://pubmed.ncbi.nlm.nih.gov/39369447/)).
- **No FAERS-based KHE-specific adverse-event analysis was retrieved.**

### 12.7 Treatment strategy and algorithm

Synthesising the three consensus documents and the risk-group data:

1. **Confirm diagnosis** (clinical + MRI/US + biopsy with IHC; consider Ang-2) ([doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344); [PMID 41389323](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701870/)).
2. **Risk-stratify by thrombocytopenia severity and lesion extent/location** (low / high / extremely high) ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)).
3. **KMP-negative, small, resectable →** surgery, or **observation in selected cases** given documented spontaneous regression ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/); [PMID 41834121](https://pubmed.ncbi.nlm.nih.gov/41834121/)).
4. **KMP-positive →** **sirolimus + prednisolone** as the evidence-based combination ([doi:10.1182/blood.2021014027](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)); vincristine remains a legitimate first-line in some centres and is **added** for life-threatening localisation or sirolimus/steroid failure ([PMID 42246503](https://pubmed.ncbi.nlm.nih.gov/42246503/); [PMID 41389323](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701870/)).
5. **Extremely high-risk →** **multimodality therapy** is "*the best choice*," including interventional options; TAE as a bridge ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/); [PMC13291430](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)).
6. **Maintenance and withdrawal** individualised by severity; months-to-a-year for small/KMP-negative disease, long-term for extensive KMP disease; taper carefully given 17.3% rebound ([doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344); [PMID 39369447](https://pubmed.ncbi.nlm.nih.gov/39369447/); [NCT07131644](https://clinicaltrials.gov/study/NCT07131644)).
7. **Lifelong sequelae management:** compression for lymphedema, pain management, orthopaedic/rehabilitation follow-up, residual-lesion surveillance ([doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/); [J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)).

**Personalised/genotype-guided medicine:** not yet practised in KHE. Genotype currently does **not** alter therapy; sirolimus is used empirically regardless of *GNA14*/*PIK3CA* status, although *PIK3CA*-mutant KHE responding to sirolimus is mechanistically coherent ([PMID 37274236](https://pubmed.ncbi.nlm.nih.gov/37274236)). No OncoKB/CIViC/My Cancer Genome KHE entry was retrieved.

---

## 13. Prevention

**Framing caveat stated plainly:** KHE arises from a sporadic somatic mutation during development. **Primary prevention is not possible, and no preventive intervention exists.** What the literature supports is almost entirely **secondary and tertiary prevention** — earlier recognition and complication avoidance.

- **Primary prevention:** **none.** No modifiable risk factor, no vaccine-preventable or exposure-mediated cause ([§2, §5](#2-etiology)). No USPSTF/CDC/WHO recommendation exists for KHE.
- **Immunization:** no preventive vaccine. Vaccination is nonetheless a clinical concern *during* treatment because of sirolimus-induced immunosuppression — the subject of a dedicated trial ([NCT05351216](https://clinicaltrials.gov/study/NCT05351216)).
- **Secondary prevention (early detection) — the real opportunity:**
 - **Early diagnosis is the main modifiable determinant of disability.** Patients who develop bone destruction were "*diagnosed later than those without bone destruction*" (median 19.0 months) ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)); the field notes "*there is still a lack of early diagnosis approaches for KHE*" ([Front Oncol 2024](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1336763/full)).
 - **Ultrasound radiomics** is explicitly positioned as an early-detection tool: 91.41% accuracy, "*of great help in improving the early diagnosis rate*" ([PMID 39553205](https://pmc.ncbi.nlm.nih.gov/articles/PMC11560810/)).
 - **Prenatal recognition** permits planned delivery and, in a first report, **maternal sirolimus therapy** before birth ([doi:10.1002/pd.70180](https://pmc.ncbi.nlm.nih.gov/articles/PMC13377337/)).
 - **Awareness of atypical presentations** prevents missed diagnosis: 11% lack cutaneous findings and older children present with musculoskeletal complaints ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)).
- **Tertiary prevention (preventing complications in diagnosed patients):** prompt sirolimus ± prednisolone to abort KMP ([doi:10.1182/blood.2021014027](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)); early intervention to limit infiltration before fibrosis and bone erosion become irreversible ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)); compression to limit lymphedema progression ([doi:10.1186/s13023-020-01595-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/)); careful tapering to avoid the 17.3% rebound ([PMID 39369447](https://pubmed.ncbi.nlm.nih.gov/39369447/)).
- **Genetic screening / carrier screening / PGD / prenatal genetic testing:** **not indicated.** Because the driver is somatic and non-heritable, there is no carrier state, no PGD indication, and no cascade testing role. **No ACMG/ACOG recommendation for KHE was retrieved.**
- **Genetic counselling:** the appropriate content is **reassurance about non-heritability and negligible recurrence risk in future pregnancies** — a reasonable inference from the somatic-mosaic etiology, though **I retrieved no KHE-specific counselling guideline** and flag it as inferred rather than sourced.
- **Risk stratification for prevention:** the clinical risk-group scheme serves this purpose ([PMC11188338](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)); KMP risk prediction uses age ≤1 month, size ≥6 cm, deep/non-extremity location ([PMC11032113](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)).
- **Behavioural interventions, public-health interventions, environmental interventions, prophylactic medication:** **none applicable; none retrieved.** (Infection prophylaxis during immunosuppression is standard supportive care but I retrieved no KHE-specific prophylaxis protocol and do not state one.)

---

## 14. Other Species / Natural Disease

### Taxonomy and natural occurrence

KHE **does occur naturally in non-human animals**, though it is exceptionally rare.

- **Dog (*Canis lupus familiaris*)** — **the first reported case of KHE in any non-human animal species**: a **10-year-old male dog**; "*The lesion was completely reexcised, and the dog remained healthy 6 months later without evidence of recurrence or metastasis*" ([Vincek, Zaulyanov & Mirzabeigi, Vet Pathol 2004;41:695, doi:10.1354/vp.41-6-695](https://journals.sagepub.com/doi/10.1354/vp.41-6-695)).
- **Cat (*Felis catus*)** — **gastroduodenal junction KHE**, described as "*the first documented case involving the alimentary tract in animals*," with pathological findings and follow-up ([Vet Res Commun 2026;50:256, doi:10.1007/s11259-026-11195-3](https://pmc.ncbi.nlm.nih.gov/articles/PMC13056791/)).
- **NCBI Taxon IDs for these species were not retrieved in this session** and should be assigned at ingestion.

### Breed

**No breed predisposition reported.** Both published animal cases are single animals; **no VBO identifier applies.**

### Orthologous genes

**Not retrieved.** I did not retrieve NCBI Gene IDs for *GNA14* orthologues in dog, cat, mouse, rat or zebrafish in this session, and no animal KHE case has been genotyped for *GNA14*. This is a clear gap: **no molecular confirmation exists that spontaneous animal KHE shares the human driver.**

### Comparative biology and veterinary relevance

- **Classification parallel:** "*The spectrum of blood vessel neoplasms comprises benign (hemangioma), intermediate (hemangioendothelioma), and malignant (hemangiosarcoma) tumors*," and in veterinary medicine hemangioendothelioma "*is classified as an intermediate vascular tumor and is rare among animal species, with a low number of documented cases in dogs, cattle, and one bird*" — mirroring KHE's borderline position in ISSVA ([Vet Res Commun 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13056791/); [Merck Veterinary Manual](https://www.merckvetmanual.com/integumentary-system/tumors-of-the-skin-and-soft-tissues/connective-tissue-tumors-in-animals)).
- **Veterinary importance is low:** "*vascular tumors are common in dogs, occasionally observed in cats, but rare in other domestic or wild animals*," yet **hemangiosarcoma dominates**, and hemangioendothelioma "*seems rare in most species*," reported occasionally in canine skin, spleen, lung and brain ([Vet Res Commun 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13056791/); [review of CNS proliferative vascular disorders](https://journals.sagepub.com/doi/10.1177/0300985820980707)).
- **Key comparative difference:** the two animal KHE cases were **adult-onset and not reported with KMP**, whereas human KHE is an infantile tumour defined by KMP — i.e., the animal lesions reproduce the **histological** entity but not the **haematological** syndrome.
- **Evolutionary conservation:** the Gα/GTPase catalytic-glutamine mechanism is deeply conserved across Gα subunits and species ([mechanistic reviews](https://pmc.ncbi.nlm.nih.gov/articles/PMC11493338/)), making a conserved oncogenic route plausible *(inferred, not demonstrated in animals)*.
- **OMIA:** **no OMIA entry for hemangioendothelioma/KHE was retrieved**; I searched and the results explicitly did not contain OMIA records.

### Transmission

**Zoonotic potential: none.** KHE is a non-infectious somatic neoplasm, HHV-8-negative (§5), with no transmissible agent and therefore **no zoonotic or cross-species susceptibility**.

---

## 15. Model Organisms

The field's own assessment frames this section: "*KHE research faces challenges due to the lack of established cell lines and suitable animal models*" ([doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)).

### 15.1 Available models

| Model | Type | Construction | What it recapitulates | Key limitation |
|---|---|---|---|---|
| **Patient-derived tumour xenograft in nude mice** | Mammalian, in vivo | Fresh KHE tissue from a KMP patient implanted subcutaneously on the backs of nude mice | **Recapitulates KMP** — "*Blood tests showed a significant decrease in platelet numbers 2 weeks after transplantation*" | Immunodeficient host; single-donor dependence; low throughput ([PMID 39025210](https://pubmed.ncbi.nlm.nih.gov/39025210/)) |
| **GNA14 p.Gln205Leu endothelial-cell xenograft** | Engineered mammalian, in vivo | Mutant ECs implanted subcutaneously into immunodeficient mice | Genotype-specific vascular phenotype — mutant implants "*displayed significantly higher vascularization compared to wild-type controls*" | Not a KHE tumour per se; models the driver, not the disease architecture ([Front Cell Dev Biol 2025](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1572909/full)) |
| **GNA14 p.Gln205Leu ECs in vitro (tube-formation assay)** | In vitro | Transfected/edited endothelial cells vs wild-type | Growth-factor-independent proliferation, morphological change, **MAPK upregulation** | No coagulopathy, no tissue context ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/)) |
| **Patient-derived CD31⁺ KHE cells and spheroids** | In vitro, patient-derived | CD31-antibody sorting from surgical specimens; spheroid culture | Sirolimus response; proliferation/migration; **ATG9B** mechanism | **Succeeded in only 3 of 6 patients** — low establishment rate; no immortalised line ([doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)) |
| **EOMA cell line + syngeneic mouse model** | Mammalian, in vivo, immunocompetent | EOMA (murine hemangioendothelioma endothelial cells, arose spontaneously in a **129/J mouse**); 10⁶ cells SC in the flank | **Kasabach–Merritt-like syndrome**: tumours visible ~day 5, "*leading to death at an average of 16 d after inoculation from tumor burden and the associated bleeding diathesis that simulates Kasabach–Merritt syndrome of infancy*"; erythrocyte sequestration and falling haematocrit within 3–4 weeks | Murine tumour of unknown driver genotype — **not GNA14-defined**; models the *syndrome*, not human KHE genetics ([J Invest Dermatol](https://www.jidonline.org/article/S0022-202X(15)30482-6/fulltext); [Am J Physiol Cell Physiol 2003](https://journals.physiology.org/doi/full/10.1152/ajpcell.00238.2003)) |
| **EOMA 3-D spheroid in a rotary cell culture system** | In vitro, 3-D | RCCS-grown EOMA spheroids | **HIF-1α significantly upregulated** in spheroids and in EOMA xenografts | Murine, driver-agnostic ([Front Cell Dev Biol 2025](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1572909/full)) |
| **Transgenic endothelial-cell hemangioma mice** | Mammalian, in vivo | Transgenic ECs inducing hemangiomas | Historically described as "*A model for the Kasabach-Merritt syndrome*" | Historical; hemangioma rather than KHE ([Wikidata record of the publication](https://www.wikidata.org/wiki/Q33492534)) |

### 15.2 Genetic model types

- **Available:** somatic **knock-in-style expression of *GNA14* p.Gln205Leu in endothelial cells** (in vitro and xenograft) ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/); [Front Cell Dev Biol 2025](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1572909/full)).
- **Not available / not retrieved:** no *Gna14* **knockout, conditional (Cre-lox), inducible, or humanized mouse** for KHE; **no zebrafish, *Drosophila*, *C. elegans*, or yeast model**; **no iPSC or organoid model**; **no IMPC/KOMP/MGI KHE-phenotype line** was retrieved. A **mosaic, endothelium-restricted, inducible *Gna14*-Q205L mouse** is the obvious missing reagent *(my assessment, not a sourced claim)*.
- **Induced (non-genetic) models:** EOMA inoculation is the established induced model; **no drug-induced, surgical, or environmental KHE model** was retrieved.

### 15.3 Phenotype recapitulation and limitations

- **Best-recapitulated feature: KMP.** Both the patient-derived xenograft ([PMID 39025210](https://pubmed.ncbi.nlm.nih.gov/39025210/)) and EOMA models reproduce consumptive thrombocytopenia/bleeding diathesis — the single most clinically important phenotype.
- **Best-recapitulated molecular feature:** *GNA14*-driven MAPK activation and hypervascularisation ([PMID 27476652](https://pubmed.ncbi.nlm.nih.gov/27476652/)).
- **Not recapitulated:** the **infiltrative growth across tissue planes**, **bone destruction**, **periarticular/muscular fibrosis**, **chronic lymphedema**, and the **partial lymphatic (D2-40/PROX1) immunophenotype** of human KHE — none of these has been demonstrated in any retrieved model. There is also **no model with a defined human driver genotype that also produces KMP** (the GNA14 models give vascularisation; the KMP models are driver-undefined).
- **Translational use demonstrated:** sirolimus mechanism dissection in patient-derived CD31⁺ cells ([doi:10.1111/jcmm.70903](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)); anti-angiogenic/immunomodulatory intervention testing in EOMA mice (topical imiquimod — [J Invest Dermatol](https://www.jidonline.org/article/S0022-202X(15)30482-6/fulltext); IL-12 gene therapy — [J Invest Dermatol](https://www.sciencedirect.com/science/article/pii/S0022202X15404816); MCP-1 angiogenic role — [Am J Physiol 2003](https://journals.physiology.org/doi/full/10.1152/ajpcell.00238.2003)).

### 15.4 Resources

- **Cellosaurus** holds the EOMA line (searchable at [cellosaurus.org](https://www.cellosaurus.org/)); **I did not retrieve its CVCL accession in this session** and do not state one.
- **MGI, RGD, ZFIN, FlyBase, WormBase, SGD, IMSR, EMMA, MMRRC, DepMap:** **no KHE-relevant entry retrieved.** This is consistent with there being no germline genetic model of the disease.

---

## Evidence quality summary and principal gaps

**Strong evidence (human clinical, prospective/randomised):** sirolimus efficacy ([PMID 26783326](https://pubmed.ncbi.nlm.nih.gov/26783326/)); superiority of sirolimus + prednisolone for KMP ([doi:10.1182/blood.2021014027](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus)); high- vs low-dose sirolimus RCT ([PMID 40107509](https://pubmed.ncbi.nlm.nih.gov/40107509/)).

**Strong evidence (large cohorts / consensus):** KMP frequency and risk factors ([PMID 22871490](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)); mortality reduction to ~1.3–2% ([doi:10.1002/pbc.30779](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779); [doi:10.1002/ijc.35344](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344)); bone destruction 26% and its functional consequences ([J Pediatr Surg 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)); HRQOL impairment ([PMID 35281237](https://pmc.ncbi.nlm.nih.gov/articles/PMC8907831/)).

**Moderate evidence:** *GNA14* Q205L as driver (functionally validated in vitro, but reported in small numbers and absent in some series); Ang-2 as biomarker; methylation-based KHE/TA unification.

**Weak or absent — the real gaps for a knowledge base to flag:**
1. **Driver detection is incomplete** — a majority of sequenced KHEs in at least one series had no identified driver ([PMID 31887709](https://pubmed.ncbi.nlm.nih.gov/31887709/)).
2. **No single-cell, spatial, proteomic, metabolomic, or lipidomic data on KHE at all** (searched; none retrieved).
3. **No functional genomics screen (CRISPR/RNAi) in KHE.**
4. **No model combining a defined human driver genotype with the KMP phenotype**, and no germline/conditional mouse.
5. **No population-level epidemiology** beyond one US region; no ICD-11 or KHE-specific MeSH code retrieved.
6. **No therapeutic alternative to mTOR inhibition in trials** — the MAPK node implied by *GNA14* biology is untested in KHE.
7. **Formal HPO annotation set for ORPHA:2122/MONDO:0016236 could not be retrieved directly**; MalaCards reports 14 HPO terms for KHE but the full list was not retrievable in this session, so the phenotype table above proposes terms rather than reproducing the official annotation file. This should be resolved against hpo.jax.org before ingestion.

---

## Sources

- [Croteau et al., *J Pediatr* 2013 — KHE: atypical features and risks of KMP in 107 referrals (PMID 22871490)](https://pubmed.ncbi.nlm.nih.gov/22871490/) · [PMC3494787](https://pmc.ncbi.nlm.nih.gov/articles/PMC3494787/)
- [Lim et al., *Am J Hum Genet* 2016 — GNA14 somatic mutation causes congenital and sporadic vascular tumors by MAPK activation (PMID 27476652)](https://pubmed.ncbi.nlm.nih.gov/27476652/) · [full text PDF](https://www.cell.com/ajhg/pdf/S0002-9297(16)30213-0.pdf)
- [Ji et al., *Orphanet J Rare Dis* 2020;15:39 — KHE: current knowledge and future perspectives (PMID 32014025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6998257/)
- [Tian et al., *Pediatr Investig* 2026 — KHE: diagnosis and treatment (doi:10.1002/ped4.70041)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13291430/)
- [Zhou et al., *Int J Cancer* 2025;156:1986–94 — Consensus statement for diagnosis, treatment and prognosis of KHE](https://onlinelibrary.wiley.com/doi/10.1002/ijc.35344)
- [VASCERN-VASCA diagnostic and management pathways for KHE, *Eur J Pediatr* 2026 (PMID 41389323)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12701870/) · [VASCERN patient pathway PDF](https://vascern.eu/app/uploads/2024/11/VASCA-Patient-Pathway-Kaposiform-Hemangioendothelioma_KHE.pdf)
- [Drolet et al., *J Pediatr* 2013 — Consensus-derived practice standards plan for complicated KHE (PMID 23796341)](https://www.jpeds.com/article/S0022-3476(13)00399-5/fulltext)
- [Ji et al., *Blood* 2022;139:1619–30 — Sirolimus plus prednisolone vs sirolimus monotherapy (RCT)](https://ashpublications.org/blood/article/139/11/1619/483531/Sirolimus-plus-prednisolone-vs-sirolimus) · [ASH Clinical News summary](https://ashpublications.org/ashclinicalnews/news/6132/sirolimus-plus-prednisolone-superior-to-sirolimus)
- [Adams et al., *Pediatrics* 2016 — Efficacy and safety of sirolimus in complicated vascular anomalies (PMID 26783326)](https://pubmed.ncbi.nlm.nih.gov/26783326/)
- [High- vs low-dose sirolimus in KHE: a randomized clinical trial (PMID 40107509)](https://pubmed.ncbi.nlm.nih.gov/40107509/)
- [Zhou et al., *Int J Cancer* 2023 — Long-term outcomes of sirolimus treatment for KHE](https://onlinelibrary.wiley.com/doi/10.1002/ijc.34509)
- [Borst et al., *Pediatr Blood Cancer* 2024 — Treatment practices and response in KHE: multicenter cohort (doi:10.1002/pbc.30779)](https://onlinelibrary.wiley.com/doi/abs/10.1002/pbc.30779)
- [Treatment experience for different risk groups of KHE (PMC11188338)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11188338/)
- [KHE: clinical features, complications and risk factors for KMP (PMC11032113)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11032113/)
- [KHE with bone destruction: 16-year follow-up cohort, *J Pediatr Surg* 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022346823007340)
- [Chronic lymphedema in KHE, *Orphanet J Rare Dis* 2020 (doi:10.1186/s13023-020-01595-2)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648422/) · [primary lymphedema vs KHE-associated lymphedema (PMC11869848)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11869848/)
- [Health-related quality of life in children with KHE (PMID 35281237)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8907831/)
- [ten Broek et al., *Ann Diagn Pathol* 2020 — KHE and tufted angioma: (epi)genetic analysis incl. genome-wide methylation (PMID 31887709)](https://pubmed.ncbi.nlm.nih.gov/31887709/)
- [Exome sequence analysis of KHE: putative driver mutations (PMID 28099595)](https://pubmed.ncbi.nlm.nih.gov/28099595/)
- [KHE with PIK3CA mutation treated with sirolimus (PMID 37274236)](https://pubmed.ncbi.nlm.nih.gov/37274236) · [Carli et al., *Clin Genet* 2021 — KHE broadens PIK3CA-related overgrowth spectrum](https://onlinelibrary.wiley.com/doi/10.1111/cge.14047)
- [Primary KHE of the tibia with a previously undescribed GNAQ mutation, *Skeletal Radiol* 2026 (PMID 42103999)](https://pubmed.ncbi.nlm.nih.gov/42103999/)
- [Tufted angioma with KMP caused by somatic GNA14 mutation (PMID 31423605)](https://pubmed.ncbi.nlm.nih.gov/31423605/) · [GNA14/GNA11/GNAQ in benign vs malignant cutaneous vascular tumors (PMC8141909)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8141909/) · [GNA14 as most commonly mutated gene in vascular neoplasms](https://www.nature.com/articles/s41379-019-0284-y)
- [ClinVar VCV000548667 (GNA14)](https://www.ncbi.nlm.nih.gov/clinvar/variation/548667/?new_evidence=true) · [OMIM \*604397 GNA14](https://omim.org/entry/604397)
- [Le Cras et al. — Angiopoietins as serum biomarkers for lymphatic anomalies (PMID 27990590)](https://pubmed.ncbi.nlm.nih.gov/27990590/) · [How we use angiopoietin-2 in diagnosis and management of vascular anomalies (PMID 38439088)](https://pubmed.ncbi.nlm.nih.gov/38439088/) · [Ang-2 beyond complex lymphatic anomalies, *Blood* 2025](https://ashpublications.org/blood/article/146/Supplement%201/4877/555845/Use-of-angiopoietin-2-as-a-biomarker-in-vascular)
- [Platelet functional abnormalities in KHE/KMP, *Blood Adv* 2023 (PMID 37307200)](https://pubmed.ncbi.nlm.nih.gov/37307200/) · [Kasabach-Merritt Phenomenon — EyeWiki mechanism synthesis](https://eyewiki.org/Kasabach-Merritt_Phenomenon)
- [Sirolimus for KHE: potential mechanisms of action and resistance (PMID 39369447)](https://pubmed.ncbi.nlm.nih.gov/39369447/) · [Li et al., *J Cell Mol Med* 2025 — sirolimus in CD31⁺ KHE endothelial cells / ATG9B](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541234/)
- [Xenograft model of KHE in nude mice recapitulates KMP (PMID 39025210)](https://pubmed.ncbi.nlm.nih.gov/39025210/) · [GNA14-Q205L EC xenografts and KHE 3-D spheroid/HIF-1α review, *Front Cell Dev Biol* 2025](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1572909/full) · [EOMA model: imiquimod study](https://www.jidonline.org/article/S0022-202X(15)30482-6/fulltext) · [EOMA/MCP-1 angiogenesis](https://journals.physiology.org/doi/full/10.1152/ajpcell.00238.2003) · [IL-12 gene therapy in vascular tumour model](https://www.sciencedirect.com/science/article/pii/S0022202X15404816)
- [KHE MRI features in 64 cases, *BMC Pediatr* 2021 (PMID 33657997)](https://pubmed.ncbi.nlm.nih.gov/33657997/) · [Clinical and imaging features of KHE (PMID 29536769)](https://pubmed.ncbi.nlm.nih.gov/29536769/) · [US/MRI characteristics (PMID 39511620)](https://pubmed.ncbi.nlm.nih.gov/39511620/) · [Ultrasound radiomics for KHE (PMID 39553205)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11560810/) · [Lymphoscintigraphy in KHE (PMC13545610)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13545610/) · [Angiographic characteristics and TAE (PMID 35070833)](https://pubmed.ncbi.nlm.nih.gov/35070833/)
- [KHE clinicopathological characteristics of 8 cases (PMC7962213)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7962213/) · [D2-40 IHC in pediatric vascular tumors, *Mod Pathol* (doi:10.1038/3800444)](https://www.nature.com/articles/3800444) · [Pathology Outlines: KHE & tufted angioma](https://www.pathologyoutlines.com/topic/softtissuehemangioendotheliomakaposiform.html) · [Histological differential-diagnosis review](https://www.sciencedirect.com/science/article/abs/pii/S003130251640348X)
- [KLA vs KHE: similarities and differences, *Orphanet J Rare Dis* 2019 (PMC6612206)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6612206/) · [KHE and tufted angioma: one clinicopathological spectrum (PMC10173077)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10173077/) · [Clinical spectrum of KHE and TA (PMID 27607323)](https://pubmed.ncbi.nlm.nih.gov/27607323/)
- [ISSVA Classification 2018 (PDF)](https://www.issva.org/UserFiles/file/ISSVA-Classification-2018.pdf) · [ISSVA classification and molecular biology, *Int J Mol Sci* 2022](https://www.mdpi.com/1422-0067/23/4/2358) · [NCI PDQ: Childhood Vascular Tumors Treatment](https://www.cancer.gov/types/soft-tissue-sarcoma/hp/child-vascular-tumors-treatment-pdq)
- [Orphanet ORPHA:2122 — Kaposiform hemangioendothelioma](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2122&lng=EN) · [GARD 3077](https://rarediseases.info.nih.gov/diseases/3077/kaposiform-hemangioendothelioma/) · [MalaCards: Kaposiform hemangioendothelioma](https://www.malacards.org/card/kaposiform_hemangioendothelioma)
- [Spontaneous regression of KHE without KMP, *Pediatr Blood Cancer* 2026 (PMID 41834121)](https://pubmed.ncbi.nlm.nih.gov/41834121/) · [Superficial KHE without KMP (PMID 42232551)](https://pubmed.ncbi.nlm.nih.gov/42232551/) · [Five patients with cutaneous KHE, long follow-up (PMID 11706068)](https://pubmed.ncbi.nlm.nih.gov/11706068/)
- [Kirk et al., *J Paediatr Child Health* 2026 — vincristine in KHE (PMID 42246503)](https://pubmed.ncbi.nlm.nih.gov/42246503/) · [β-blockers vs sirolimus in KHE (PMID 43053660)](https://pubmed.ncbi.nlm.nih.gov/43053660) · [Low-dose aspirin in KHE with coagulopathy (PMID 41895209)](https://pubmed.ncbi.nlm.nih.gov/41895209/) · [Corticosteroid-to-sirolimus sequential therapy (PMID 41141660)](https://pubmed.ncbi.nlm.nih.gov/41141660/) · [Egyptian single-centre experience (doi:10.1186/s43054-025-00362-x)](https://link.springer.com/article/10.1186/s43054-025-00362-x) · [Polish multicentre study 2007–2024 (PMID 41466529)](https://pubmed.ncbi.nlm.nih.gov/41466529/)
- [Fraissenon et al., *Prenat Diagn* 2026 — prenatal diagnosis and first maternal sirolimus therapy for KHE/KMP](https://pmc.ncbi.nlm.nih.gov/articles/PMC13377337/) · [Prenatal detection of KHE with KMP (Egypt J Radiol Nucl Med 2023)](https://link.springer.com/article/10.1186/s43055-023-01028-7)
- [Adult KHE: clinicopathologic and IHC analysis of three cases (PMID 9322599)](https://pubmed.ncbi.nlm.nih.gov/9322599/) · [Adult-onset KHE with neurofibromatosis type 1 (PMID 30466240)](https://pubmed.ncbi.nlm.nih.gov/30466240/) · [Adult-onset multifocal KHE (PMC10917883)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10917883/) · [Adult KHE with multiple-bone invasion (PMID 37522676)](https://pubmed.ncbi.nlm.nih.gov/37522676/)
- [Immunological and clinical characteristics of severe thrombocytopenia in neonates with KMP (PMID 42445171)](https://pubmed.ncbi.nlm.nih.gov/42445171/) · [Musculoskeletal complications in KHE without KMP (PMID 30233248)](https://pubmed.ncbi.nlm.nih.gov/30233248/) · [Sirolimus-related severe thrombocytopenia in progressive KHE (PMID 36688881)](https://pubmed.ncbi.nlm.nih.gov/36688881/) · [KMP rebound during sirolimus (PMC9391052)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9391052/) · [Oral sirolimus safety in childhood diseases: systematic review (PMC9497617)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9497617/)
- [Vincek et al., *Vet Pathol* 2004 — KHE: first reported case in a nonhuman animal species (dog)](https://journals.sagepub.com/doi/10.1354/vp.41-6-695) · [Gastroduodenal junction KHE in a cat, *Vet Res Commun* 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13056791/) · [Merck Veterinary Manual: connective tissue tumors in animals](https://www.merckvetmanual.com/integumentary-system/tumors-of-the-skin-and-soft-tissues/connective-tissue-tumors-in-animals) · [Proliferative vascular disorders of the animal CNS](https://journals.sagepub.com/doi/10.1177/0300985820980707)
- Ontology/terminology: [HP:0011900 (EBI OLS)](https://www.ebi.ac.uk/ols4/ontologies/hp/terms?obo_id=HP%3A0011900) · [HPO portal](https://hpo.jax.org/) · [GO:0001946 lymphangiogenesis (AmiGO)](https://amigo.geneontology.org/amigo/term/GO:0001946) · [CL:0002138 bridge file](https://github.com/obophenotype/cell-ontology/blob/master/src/ontology/bridge/cl-bridge-to-uberon.obo) · [UBERON:0002097 skin of body](https://www.virtualflybrain.org/blog/2022/01/01/skin-of-body-uberon_0002097/) · [NCI Thesaurus](https://ncit.cancer.gov/) · [HPO in 2021 (PMC7778952)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778952/)
- Trials: [NCT03188068](https://clinicaltrials.gov/study/NCT03188068) · [NCT02110069](https://clinicaltrials.gov/study/NCT02110069) · [NCT04448873](https://clinicaltrials.gov/study/NCT04448873) · [NCT04077515](https://clinicaltrials.gov/study/NCT04077515) · [NCT04775173](https://clinicaltrials.gov/study/NCT04775173) · [NCT05324384](https://clinicaltrials.gov/study/NCT05324384) · [NCT05351216](https://clinicaltrials.gov/study/NCT05351216) · [NCT07131644](https://clinicaltrials.gov/study/NCT07131644) · [NCT07656909](https://clinicaltrials.gov/study/NCT07656909)
- Sirolimus pharmacogenetics (extrapolated, non-KHE): [Initial dosage recommendation for sirolimus in children with TSC (PMC7300220)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7300220/) · [CYP3A5/ABCB1 and sirolimus PK (PMC4628029)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4628029/) · [Precision sirolimus dosing in children (PMC10069443)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10069443/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 129 |
| Resolved | 127 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| Quoted claims checked | 53 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 36 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 127 |
| On topic | 73 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:37274236` (11 mentions) - Identifier did not resolve to a record
- `DOI:10.1038/3800444` (3 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `DOI:10.1002/ped4.70041` *(abstract only)*: "*the infiltration of muscles, connective tissues and joint structures can cause pain and functional limitations, which may affect a patient's abilities to perform routine daily activities*"
  - closest text in source: "Importantly, these tumors are frequently associated with Kasabach–Merritt phenomenon, a consumptive coagulopathy that represents a major cause of mortality in KHE"
- `PMC:PMC13291430` *(abstract only)*: "*the infiltration of muscles, connective tissues and joint structures can cause pain and functional limitations, which may affect a patient's abilities to perform routine daily activities*"
  - closest text in source: "Importantly, these tumors are frequently associated with Kasabach-Merritt phenomenon, a consumptive coagulopathy that represents a major cause of mortality in KHE"
- `PMC:PMC8141909` *(abstract only)*: "*frequent in benign but not malignant cutaneous vascular tumors*"
  - closest text in source: "These mutations were not identified in malignant vascular tumors, which could be of potential diagnostic value in distinguishing these entities."
- `PMID:31887709` *(abstract only)*: "*methylation profiling provided further evidence for KHEs and TAs potentially forming a spectrum of one entity*"
  - closest text in source: "In conclusion, methylation profiling provides further evidence for KHEs and TAs potentially forming a spectrum of one entity"
- `PMC:PMC7962213` *(abstract only)*: "*the absence of human herpes virus 8 (HHV-8) in KHE indicates a different pathogenesis from Kaposi sarcoma despite the histological resemblance*"
  - closest text in source: "Kaposi Sarcoma, hemangioma) and establishing the correct diagnosis is important for appropriate treatment"
- `PMC:PMC8633177` *(abstract only)*: "*the absence of human herpes virus 8 (HHV-8) in KHE indicates a different pathogenesis from Kaposi sarcoma despite the histological resemblance*"
  - closest text in source: "Microscopically, it is characterized by a vascular proliferation permeated by spindle-to-ovoid cells resembling Kaposi sarcoma"
- `PMID:22871490` *(abstract only)*: "*KHE manifested in infancy in 93% of cases, with 60% presenting as neonates*"
  - closest text in source: "KHE manifested in infancy in 93% of cases, with 60% as neonates"
- `PMC:PMC3494787` *(abstract only)*: "*KHE manifested in infancy in 93% of cases, with 60% presenting as neonates*"
  - closest text in source: "KHE manifested in infancy in 93% of cases, with 60% as neonates"
- `PMID:39369447` *(abstract only)*: "*Rebound growth occurred in 17.3% of patients upon sirolimus discontinuation*"
  - closest text in source: "In addition, the mechanism of sirolimus resistance in some KHE patients is discussed"
- `DOI:10.1002/ijc.35344` *(abstract only)*: "*no intervention other than complete surgical excision can achieve a definitive 'cure'*"
  - Text part not found as substring: '*no intervention other than complete surgical excision can achieve a definitive 'cure'*' (note: only abstract available for DOI:10.1002/ijc.35344, full text may contain this excerpt)
- `DOI:10.1002/ped4.70041` *(abstract only)*: "*no intervention other than complete surgical excision can achieve a definitive 'cure'*"
  - Text part not found as substring: '*no intervention other than complete surgical excision can achieve a definitive 'cure'*' (note: only abstract available for DOI:10.1002/ped4.70041, full text may contain this excerpt)
- `PMC:PMC13291430` *(abstract only)*: "*no intervention other than complete surgical excision can achieve a definitive 'cure'*"
  - Text part not found as substring: '*no intervention other than complete surgical excision can achieve a definitive 'cure'*' (note: only abstract available for PMID:42358898, full text may contain this excerpt)
- `DOI:10.1002/ijc.35344` *(abstract only)*: "*patients without KMP or with small lesions typically require therapy for several months to a year, whereas those with extensive, infiltrative lesions complicated by KMP often require long-term management*"
  - closest text in source: "The aim of this study was to integrate the literature and Chinese expert opinions to provide updated recommendations that will guide the diagnosis, treatment, and prognosis of patients with KHE"
- `PMC:PMC11032113` *(abstract only)*: "*Unlike infantile hemangiomas, KHE rarely undergoes spontaneous regression*"
  - closest text in source: "RESULTS: KHE precursors or lesions were present at birth in 52·1% of patients"
- `PMID:41834121` *(abstract only)*: "*challenges universal aggressive intervention, supporting observation for selected non-coagulopathic cases*"
  - closest text in source: "These findings challenge universal aggressive intervention, supporting observation for selected non-coagulopathic cases."
- `PMID:27990590` *(abstract only)*: "*correlating with normalization of platelet counts and D-dimer reductions*"
  - Text part not found as substring: '*correlating with normalization of platelet counts and D-dimer reductions*' (note: only abstract available for PMID:27990590, full text may contain this excerpt)
- `PMID:38439088` *(abstract only)*: "*correlating with normalization of platelet counts and D-dimer reductions*"
  - Text part not found as substring: '*correlating with normalization of platelet counts and D-dimer reductions*' (note: only abstract available for PMID:38439088, full text may contain this excerpt)
- `PMC:PMC13291430` *(abstract only)*: "*a poorly demarcated, heterogeneously mixed-echoic subcutaneous mass with rich vascularity, often displaying a characteristic 'branch-shape' flow pattern on 3-D color Doppler and increased stiffness on elastography*"
  - closest text in source: "The tumor typically originates in the skin and exhibits invasive growth into deeper tissues, often manifesting as a firm, poorly defined purplish-red mass"
- `PMID:39553205` *(abstract only)*: "*radiomics showed excellent efficacy in the diagnosis of KHE, which is of great help in improving the early diagnosis rate*"
  - closest text in source: "In conclusion, ultrasound radiomics analysis is highly effective in the diagnosis of KHE, which can contribute to the early diagnosis rate of KHE."
- `PMC:PMC11560810` *(abstract only)*: "*radiomics showed excellent efficacy in the diagnosis of KHE, which is of great help in improving the early diagnosis rate*"
  - closest text in source: "In conclusion, ultrasound radiomics analysis is highly effective in the diagnosis of KHE, which can contribute to the early diagnosis rate of KHE."
- `DOI:10.3389/fonc.2024.1336763` *(abstract only)*: "*The diagnosis is mostly based on pathological biopsy*"
  - closest text in source: "Methods Through a retrospective review of 70 patients diagnosed with KHE between 2017 and 2022 in our center, we classify lesions into three clinicopathological stages based on the tumor involving depth, and divided the severity of KHE into three levels by estimating clinicopathological stages and severity of thrombocytopenia"
- `DOI:10.1002/pd.70180` *(abstract only)*: "*The diagnosis of Kaposiform Hemangioendothelioma should be suspected in prenatal period if there is unilateral hypertrophy of limb which has evolved rapidly over a short interval of time and shows findings suggestive of Kasabach–Merritt Phenomenon*"
  - closest text in source: "ABSTRACT Objective To describe the prenatal diagnosis, evolution, and perinatal management of kaposiform hemangioendothelioma (KHE) complicated by the Kasabach–Merritt phenomenon (KMP), and to report the first documented use of maternal sirolimus therapy (MST) in this setting"
- `PMC:PMC13377337` *(abstract only)*: "*The diagnosis of Kaposiform Hemangioendothelioma should be suspected in prenatal period if there is unilateral hypertrophy of limb which has evolved rapidly over a short interval of time and shows findings suggestive of Kasabach–Merritt Phenomenon*"
  - closest text in source: "OBJECTIVE: To describe the prenatal diagnosis, evolution, and perinatal management of kaposiform hemangioendothelioma (KHE) complicated by the Kasabach-Merritt phenomenon (KMP), and to report the first documented use of maternal sirolimus therapy (MST) in this setting"
- `DOI:10.1002/ijc.35344` *(abstract only)*: "*residual lesions persist to some extent in all patients even after standard treatment*"
  - closest text in source: "The aim of this study was to integrate the literature and Chinese expert opinions to provide updated recommendations that will guide the diagnosis, treatment, and prognosis of patients with KHE"
- `PMC:PMC7962213` *(abstract only)*: "*tends to metastasize locally as well as to the regional lymph nodes*"
  - closest text in source: "BACKGROUND: Kaposiform Hemangioendothelioma (KHE) is a rare vascular tumor of intermediate malignant potential which shows locally aggressive growth but only rarely metastasizes"
- `DOI:10.3389/fonc.2024.1336763` *(abstract only)*: "*has fundamentally improved patient outcomes, reducing mortality to below 2%*"
  - closest text in source: "Background Kaposiform hemangioendothelioma (KHE) is a rare vascular tumor with a high risk of mortality"
- `DOI:10.1002/ijc.35344` *(abstract only)*: "*has fundamentally improved patient outcomes, reducing mortality to below 2%*"
  - closest text in source: "The recommendations presented herein are intended to assist in the guidance of clinical practice and decision‐making in patients with KHE, with the objective of improving patient outcomes."
- `PMID:26783326` *(abstract only)*: "*sirolimus was efficacious and well tolerated in these study patients with complicated vascular anomalies, with clinical activity reported in the majority of the disorders*"
  - closest text in source: "CONCLUSIONS: Sirolimus was efficacious and well tolerated in these study patients with complicated vascular anomalies"
- `PMID:41389323` *(abstract only)*: "*In cases where there is a life-threatening localisation or failure to respond to sirolimus and corticosteroids, vincristine should be added to the therapeutic regimen*"
  - closest text in source: "WHAT IS KNOWN: • Kaposiform hemangioendothelioma (KHE) is a rare, locally aggressive vascular tumor, often associated with a life threatening coagulopathy, and can be challenging to manage"
- `PMC:PMC12701870` *(abstract only)*: "*In cases where there is a life-threatening localisation or failure to respond to sirolimus and corticosteroids, vincristine should be added to the therapeutic regimen*"
  - closest text in source: "WHAT IS KNOWN: • Kaposiform hemangioendothelioma (KHE) is a rare, locally aggressive vascular tumor, often associated with a life threatening coagulopathy, and can be challenging to manage"
- `PMID:25755958` *(abstract only)*: "*cured by Whipple operation*"
  - Text part not found as substring: '*cured by Whipple operation*' (note: only abstract available for PMID:25755958, full text may contain this excerpt)
- `PMC:PMC13291430` *(abstract only)*: "*relatively contraindicated for lesions involving critical regions such as the intracranial space or hepatic hilum*"
  - closest text in source: "Cases of KHE involving visceral organs, including the bone, retroperitoneum, or mediastinum, have also been reported; however, their clinical features are often nonspecific, which may lead to delayed diagnosis"
- `DOI:10.3389/fonc.2024.1336763` *(abstract only)*: "*there is still a lack of early diagnosis approaches for KHE*"
  - closest text in source: "Conclusions Our study describes the largest assessment of high-risk patients with KHE who have undergone an operation to date, with 5 years of follow-up to track recovery, which provides invaluable knowledge for the future treatment of patients with KHE and KMP from different risk groups: Early surgical intervention may be the most definitive treatment option for most patients with KHE; multimodality treatment is the best choice for the extremely high-risk group."
- `PMID:39553205` *(abstract only)*: "*of great help in improving the early diagnosis rate*"
  - closest text in source: "In conclusion, ultrasound radiomics analysis is highly effective in the diagnosis of KHE, which can contribute to the early diagnosis rate of KHE."
- `PMC:PMC11560810` *(abstract only)*: "*of great help in improving the early diagnosis rate*"
  - closest text in source: "In conclusion, ultrasound radiomics analysis is highly effective in the diagnosis of KHE, which can contribute to the early diagnosis rate of KHE."
- `DOI:10.1354/vp.41-6-695` *(abstract only)*: "*The lesion was completely reexcised, and the dog remained healthy 6 months later without evidence of recurrence or metastasis*"
  - closest text in source: "Microscopic examination of the lesion revealed a multinodular tumor with sheets of spindled endothelial cells forming vascular slits similar to Kaposi's sarcoma and peripheral tumor lobules resembling capillary hemangioma."

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC11493338` (2 mentions) - Going Rogue: Mechanisms, Regulation, and Roles of Mutationally Activated Gα in Human Cancer.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `khe`, `kmp`, `sirolimus`, `lesion`, `patient`, `clinical`, `vascular`, `gna14`, `disease`, `bone`, `cell`, `blood`, `tumour`, `pediatr`, `tissue`, `somatic`, `gene`, `platelet`, `treatment`, `lymphedema`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1038/3800444`: "*D2-40 positivity suggests lymphothelial differentiation of the neoplastic component of kaposiform hemangioendothelioma*"
  - Reference did not resolve, so the quote could not be checked
- `DOI:10.1002/ajh.26370`: "*presenting as insidious consumptive coagulopathy*"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001873` (2 mentions) - the report calls it "Acute, can rebound"; HP calls it **Thrombocytopenia**
- `HP:0011900` (3 mentions) - the report calls it "EBI OLS"; HP calls it **Hypofibrinogenemia**
- `HP:0001892` (2 mentions) - the report calls it "Episodic"; HP calls it **Abnormal bleeding**
- `HP:0012531` (2 mentions) - the report calls it "Progressive then persistent", "Chronic, often irreversible"; HP calls it **Pain**
- `HP:0001004` (1 mention) - the report calls it "Chronic, **irreversible, sirolimus-resistant"; HP calls it **Lymphedema**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012531` - called "Progressive then persistent", "Chronic, often irreversible"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.