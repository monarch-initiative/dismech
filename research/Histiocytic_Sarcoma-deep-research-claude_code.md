---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-21T00:07:44.380334'
end_time: '2026-11-21T00:25:20.420183'
duration_seconds: 1056.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Histiocytic Sarcoma
  mondo_id: MONDO:0019479
  category: Neoplasm. Scope rules for this report - rely on series that apply the
    modern definition (immunophenotyped, with lymphoma and other mimics excluded);
    leave out ALK-positive histiocytosis (name it only as a separate disease), ALK
    staining, anaplastic large cell lymphoma and any ALK-directed treatment or trial;
    state any NF1 or NF2 change at gene level only; do not name or discuss chromosome-arm
    changes (in particular 1p36, 11q or 17q) or chromothripsis. It is mostly an adult
    disease; do not describe it as a childhood tumour unless a source says so.
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: sarcoma, histiocytic, malignant
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
  web_search_requests: 68
  num_turns: 71
  total_cost_usd: 6.209801000000002
  session_id: 230cb594-799e-4616-b04b-d99f1d76b80c
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  tool_calls: 70
  retrieval_calls: 69
  assistant_text_blocks: 1
citation_count: 181
reference_validation:
  total_references: 115
  verified: 114
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.009
  quotes_checked: 17
  quotes_valid: 1
  quotes_unsupported: 16
  unsupported_quote_references:
  - PMC:PMC11076448
  - PMID:41915766
  - PMID:16086090
  - PMID:36051154
  - PMID:33786289
  - PMID:18987551
  - PMC:PMC12429796
  - PMID:41135521
  - PMC:PMC12616613
  - PMC:PMC6190545
  - PMC:PMC10546704
  - PMID:30867592
  - PMID:40486162
  - PMC:PMC12144458
  - PMC:PMC13627489
  quotes_not_checkable: 2
  relevance_assessed: 114
  on_topic: 56
  off_topic: 1
  off_topic_references:
  - DOI:10.1177/0300985811430696
  unresolved_references:
  - PMC:PMC11452572
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 17
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - OMIA
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Histiocytic Sarcoma
- **MONDO ID:** MONDO:0019479 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** sarcoma, histiocytic, malignant
- **Category:** Neoplasm. Scope rules for this report - rely on series that apply the modern definition (immunophenotyped, with lymphoma and other mimics excluded); leave out ALK-positive histiocytosis (name it only as a separate disease), ALK staining, anaplastic large cell lymphoma and any ALK-directed treatment or trial; state any NF1 or NF2 change at gene level only; do not name or discuss chromosome-arm changes (in particular 1p36, 11q or 17q) or chromothripsis. It is mostly an adult disease; do not describe it as a childhood tumour unless a source says so.

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Histiocytic Sarcoma** covering all of the
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

**Scope, interpretation, and retrieval method (read first)**

- **Disease researched:** histiocytic sarcoma (HS), **MONDO:0019479** — the mature-histiocyte/macrophage malignancy in the WHO histiocytic/dendritic cell neoplasm family ([MONDO/NORD entry](https://rarediseases.org/mondo-disease/histiocytic-sarcoma/); [Orphanet ORPHA:86896](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)). **There is no germline causal gene for this disease.** It is driven by *somatic* mutations, overwhelmingly in the RAS–MAPK pathway: **MAP2K1, KRAS, NRAS, BRAF, PTPN11, NF1 and CBL**, with a secondary PI3K–AKT–mTOR group and recurrent **CDKN2A** and **TP53** lesions ([Egan et al., *Mod Pathol* 2019;32:830–843, PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [Massoth et al., *The Oncologist* 2021;26:e1263](https://academic.oup.com/oncolo/article/26/7/e1263/6510483)). Where the template asked for a germline "causal gene", the correct answer for this entity is "none — somatic driver genes as above".
- **Per the scope rules in the request:** only series applying the modern immunophenotype-based definition (lymphoma and other mimics excluded) are used; ALK-positive histiocytosis is named here *only* as a separate disease and is otherwise excluded, as are ALK immunostaining, anaplastic large cell lymphoma, and ALK-directed therapy/trials; *NF1* is reported at gene level only; chromosome-arm–level changes and chromothripsis are not discussed. HS is treated as a predominantly **adult** disease, with pediatric occurrence noted only where a source states it.
- **Retrieval limitation (important for provenance):** in this run only a web-search tool was available; direct page/PDF fetching was blocked in this environment. Every claim below is anchored to a source I retrieved **in this session via search** (title + URL, plus PMID/DOI where the retrieval surfaced one), and the factual content comes from the retrieved search extractions of those pages. I have **not** pasted verbatim abstract text that I could not see; where a retrieved extraction appeared to quote source wording, I mark it "**quoted via retrieved extraction**". Ontology identifiers are given only where I retrieved them in this session; where I could not verify an ID, I give the label and say so explicitly.

---

# Histiocytic Sarcoma (MONDO:0019479) — Comprehensive Disease Characteristics Report

## 1. Disease Information

**Overview.** Histiocytic sarcoma is an ultra-rare, highly aggressive haematopoietic neoplasm whose cells show the morphology and immunophenotype of **mature tissue histiocytes (macrophages)**. Orphanet defines it as "a rare histiocytic tumor characterized by a malignant proliferation of cells showing morphological and immunophenotypic features of mature tissue histiocytes" ([Orphanet ORPHA:86896](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)). It accounts for **<1% of haematological malignancies**, arises most often at **extranodal** sites in adults, and may be **de novo (primary)** or **secondary**, i.e. associated with/transdifferentiated from another haematological neoplasm or a mediastinal germ cell tumour ([*Histiocytic Sarcoma: A Review and Update*, Int J Mol Sci 2025;26(17):8554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/), [doi:10.3390/ijms26178554](https://doi.org/10.3390/ijms26178554)).

**Classification.** In the WHO 5th-edition classification of haematolymphoid tumours, HS sits in the **histiocyte/macrophage neoplasm** group of "histiocytic/dendritic cell neoplasms", placed after myeloid neoplasms "in recognition of their derivation from common myeloid progenitors that give rise to cells of the monocytic/histiocytic/dendritic lineages" (quoted via retrieved extraction; [*WHO 5th edition: Myeloid and Histiocytic/Dendritic Neoplasms*, PMC9252913](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9252913/); [*Pathologic characteristics of histiocytic and dendritic cell neoplasms*, PMC11076448](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11076448/)). A 2026 Histiocyte Society international consensus proposes the unified designation **malignant histiocytic neoplasm (MHN)** covering histiocytic, Langerhans cell and interdigitating dendritic cell sarcomas ([Goyal et al., *Blood* 2026;148(3):275–288, PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/); [doi:10.1182/blood.2026033049](https://doi.org/10.1182/blood.2026033049)).

**Key identifiers (all retrieved this session).**

| Resource | Identifier |
|---|---|
| Mondo | **MONDO:0019479** ([NORD/MONDO](https://rarediseases.org/mondo-disease/histiocytic-sarcoma/)) |
| Orphanet | **ORPHA:86896**, age of onset "Adult" ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)) |
| ICD-O-3 morphology | **9755/3** (category 975, neoplasms of histiocytes and accessory lymphoid cells) ([SEER ICD-O-3 site/histology list](https://seer.cancer.gov/icd-o-3/sitetype.icdo3.20220429.pdf); [Pathology Outlines](https://www.pathologyoutlines.com/topic/lymphnodeshistiocyticsarcoma.html)) |
| ICD-10-CM (US) | **C96.A** "Histiocytic sarcoma", billable, introduced FY2016 ([ICD-10-CM C96.A](https://icdlist.com/icd-10/C96.A); [icd10data C96\*](https://www.icd10data.com/ICD10CM/Codes/C00-D49/C81-C96/C96-)) |
| ICD-10 (Orphanet cross-ref) | **C96.8** ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)) |
| ICD-11 | **2B31.1** (per Orphanet cross-reference) |
| MeSH | **D054747** (per Orphanet cross-reference) |
| UMLS | **C0334663** (per Orphanet cross-reference) |
| OMIM | **No OMIM entry applies** — HS is a somatic neoplasm, not a Mendelian disorder (no OMIM cross-reference retrieved in Orphanet/MONDO entries) |

**Synonyms / alternative names.** "Sarcoma, histiocytic, malignant"; "malignant histiocytosis" (historical, and still used for disseminated disease); "true histiocytic lymphoma" (obsolete); within the WHO/consensus framework, "malignant histiocytic neoplasm, histiocytic type" ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896); [SEER heme/lymph tool, category 975](https://seer.cancer.gov/seertools/hemelymph/51f6cf59e3e27c3994bd5471/); [Blood 2026 consensus, PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/); [Wikipedia: Malignant histiocytosis](https://en.wikipedia.org/wiki/Malignant_histiocytosis)).

**Source type of the information.** Mixed, and skewed toward **aggregated, pathology-reviewed case-level data** rather than EHR-derived cohorts: (i) population cancer-registry data (SEER: [Kommalapati et al., *Blood* 2018;131:265–268](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes)); (ii) single-centre and national retrospective series with central histological review ([MD Anderson series, PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [French national series of 141 malignant histiocytoses, *Blood Adv* 2025;9(10):2530](https://ashpublications.org/bloodadvances/article/9/10/2530/535782/Characterization-and-treatment-outcomes-of)); (iii) molecular case series ([Haematologica 2020;105(4):951–960](https://haematologica.org/article/view/9331)); (iv) individual case reports, which remain a large share of the literature.

---

## 2. Etiology

### 2.1 Disease causal factors
HS is a **clonal neoplasm caused by somatic activating lesions of the RAS–MAPK pathway**, arising in a cell of the mononuclear phagocyte lineage or in an upstream haematopoietic progenitor. Egan et al. identified "recurrent mutations involving the RAS-MAPK signaling pathway (MAP2K1, KRAS, NRAS, BRAF, PTPN11, NF1, CBL) in a majority (**57%**) of histiocytic sarcoma cases" and PI3K-activating mutations in a further **21%** (quoted via retrieved extraction; [*Mod Pathol* 2019;32:830–843, PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/)). Across the broader malignant-histiocytosis spectrum, "activating mutations in MAPK-pathway genes were identified in **80%** of MH cases; **29%** had mutations in the PI3k-AKT-mTOR pathway and **59%** had mutations in epigenetic modulating genes" (quoted via retrieved extraction; [Mayo/UAB Histiocytosis Working Group, *Mod Pathol* 2023;36:100268](https://www.modernpathology.org/article/S0893-3952(23)00173-4/fulltext)). Summarised ranges across series: RAS/MAPK **57–90%**; MAP2K1 **15–24%**; KRAS **12–50%**; BRAF V600E up to **62.5%** in selected series; PTPN11 **5–19%** ([Int J Mol Sci 2025;26:8554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)).

A second, distinct causal route is **lineage transdifferentiation from a pre-existing lymphoid neoplasm** (see §4.4): the lymphoid clone acquires RAS/MAPK alterations and converts phenotype. "The critical 'transdifferentiation' step to HDT appears to be associated with the acquisition of RAS/MAPK pathway alterations" (quoted via retrieved extraction; [Egan et al., *Mod Pathol* 2021;34:336–347](https://www.nature.com/articles/s41379-020-00673-x)).

### 2.2 Risk factors
**Genetic (constitutional).** No germline predisposition syndrome, susceptibility locus or GWAS signal for human HS was retrieved in this session. All recurrent lesions reported are somatic/tumour-restricted. Family-history data are absent from the retrieved human literature. (By contrast, heritable predisposition is established in dogs — §14.)

**Acquired/clinical risk factors (strongest evidence).**
- **A prior or concurrent haematological malignancy**, especially follicular lymphoma, chronic lymphocytic leukaemia/SLL, mantle cell lymphoma, B-lymphoblastic leukaemia/lymphoma, multiple myeloma and Hodgkin lymphoma ([*Mod Pathol* 2021;34:336–347](https://www.nature.com/articles/s41379-020-00673-x); [clonally related FL + HS, *Blood Cancer J* 2025](https://www.nature.com/articles/s41408-025-01335-4); [clonally related HDS and CLL/SLL, 7 cases, *Mod Pathol*](https://www.modernpathology.org/article/S0893-3952(22)02794-6/fulltext); [HS with CCND1 rearrangement from mantle cell lymphoma, *AJCP* 2022](https://doi.org/10.1093/ajcp/aqac087); [myeloma→HS transdifferentiation, PMC12270463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12270463/); [HS in nodular lymphocyte-predominant Hodgkin lymphoma background, PMC12310312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12310312/)). The 2026 consensus explicitly asks clinicians to **document prior haematopoietic malignancy** as part of diagnosis ([PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)).
- **Mediastinal (non-seminomatous) germ cell tumour**, where histiocytic proliferations ranging from haemophagocytic syndrome to disseminated HS occur, with evidence interpreted as "hematologic malignancy and MGCTs aris[ing] from a common progenitor cell" (quoted via retrieved extraction; [PMID 16086090](https://pubmed.ncbi.nlm.nih.gov/16086090/); [PMID 36051154](https://pubmed.ncbi.nlm.nih.gov/36051154/); [post-chemotherapy HS after mediastinal GCT, PMID 33786289](https://pubmed.ncbi.nlm.nih.gov/33786289/); [PMID 18987551](https://pubmed.ncbi.nlm.nih.gov/18987551/)).
- **Iatrogenic immunosuppression after solid-organ transplantation** — rare but documented, including EBV-negative cases ([*Histiocytic sarcoma in renal transplant patients: a literature review*, PMID 37784161 / PMC10546704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10546704/); [kidney-transplant case, PMC5066022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5066022/); [PMC4544561](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4544561/)).
- **Prior cytotoxic therapy** is temporally associated in secondary cases (e.g. HS after combination chemotherapy for mediastinal GCT; HS after hyperfractionated cyclophosphamide/vincristine/doxorubicin/dexamethasone for B-ALL), but the retrieved reports describe association in clonally related disease rather than establishing therapy as an independent carcinogenic cause ([PMID 33786289](https://pubmed.ncbi.nlm.nih.gov/33786289/); [*Blood* 2016;128:2475](https://ashpublications.org/blood/article/128/20/2475/35616/Histiocytic-sarcoma-secondary-neoplasm-or)).
- **Demographics:** older adult age and male sex (SEER: 99 men vs 60 women; female:male incidence ratio **0.49**) ([Kommalapati et al., *Blood* 2018](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes)).

**Environmental/occupational/lifestyle risk factors.** **No evidence retrieved.** No CTD/TOXNET-type exposure association, no tobacco, alcohol, diet, radiation or occupational signal for human HS was found in this session's searches. This should be recorded in a knowledge base as "no established environmental risk factor", not as "absent".

### 2.3 Protective factors
**None identified.** No genetic protective variant, modifier allele, dietary or lifestyle protective factor for HS was retrieved. gnomAD-type allele-frequency reasoning does not apply to somatic drivers.

### 2.4 Gene–environment interactions
**No human gene–environment interaction data retrieved.** The only interaction-like observations are *therapy–genotype* interactions (acquired **CBL** mutations emerging with MEK-inhibitor exposure and conferring resistance, [*Leukemia* 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/); class III **MEK1/2** mutations associating with progression on MEK inhibitors, [*Cancer Cell* 2025, PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)) — pharmacological rather than environmental.

---

## 3. Phenotypes

HS has no single stereotyped presentation; the phenotype is dictated by site. Orphanet's clinical description lists: "a solitary mass, lymphadenopathy, a skin rash or numerous tumors on the trunk and extremities, lytic bone lesions, hepatosplenomegaly with pancytopenia, intestinal obstruction, and/or systemic symptoms" (quoted via retrieved extraction; [ORPHA:86896](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)).

| Phenotype | Type | Onset / course | Frequency & source | HPO suggestion |
|---|---|---|---|---|
| Tumour mass at an extranodal site (GI tract, skin/soft tissue, spleen, CNS, bone) | Clinical sign / physical manifestation | Adult-onset; subacute, progressive | Dominant presentation; extranodal predilection, purely nodal primary disease reported as <1% of cases in a recent review ([Front Oncol 2025](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1505737/xml)) | "Neoplasm" branch; no verified single HP ID retrieved |
| Lymphadenopathy | Clinical sign | Adult; progressive | Lymph node involvement in **50%** of a 27-patient tertiary-centre cohort ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)) | **HP:0002716** Lymphadenopathy ([Monarch](https://monarchinitiative.org/HP:0002716)) |
| Soft-tissue / bone involvement | Clinical sign; imaging | Adult; progressive | Soft tissue **40%**, bone **36%** ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)); lytic bone lesions ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)) | Label "Lytic bone lesion"; ID not verified this session |
| Cutaneous tumours / rash | Physical manifestation | Adult; progressive | Skin + connective tissue the most common site group (**41%**) in a large literature review ([Front Oncol 2025](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1505737/xml)); primary cutaneous cases reported ([PMC12400779](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12400779/)) | Label "Cutaneous neoplasm"; ID not verified |
| Hepatosplenomegaly | Clinical sign | Adult; progressive | Listed by Orphanet; splenic primary disease documented ([PMC9124500](https://pmc.ncbi.nlm.nih.gov/articles/PMC9124500/)) | **HP:0001433** Hepatosplenomegaly; **HP:0001744** Splenomegaly (IDs retrieved via HPO/Monarch listing in this session) |
| Cytopenias / pancytopenia, marrow infiltration | Laboratory abnormality | Adult; progressive, severe | Bone marrow involvement **22%** ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)); marrow involvement described as uncommon overall ([PMC6170302](https://pmc.ncbi.nlm.nih.gov/articles/PMC6170302/)) | Label "Pancytopenia"; ID not verified. (Anaemia/thrombocytopenia labels likewise unverified) |
| Fever, weight loss, other constitutional ("B") symptoms | Symptom | Adult; progressive | "systemic symptoms" ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)) | **HP:0001945** Fever; **HP:0001824** Weight loss (IDs retrieved via HPO/Monarch listing) |
| Intestinal obstruction / GI bleeding / bowel infarction | Clinical sign; complication | Subacute to acute | GI tract **12%** of sites ([Front Oncol 2025](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1505737/xml)); gastric HS ([PMC13478121](https://pmc.ncbi.nlm.nih.gov/articles/PMC13478121/)); fatal enteric necrosis from tumour embolism ([PMC11452572](https://pmc.ncbi.nlm.nih.gov/articles/PMC11452572/)) | Label "Intestinal obstruction"; ID not verified |
| Neurological deficits (focal deficit, cranial neuropathy, myelopathy) | Clinical sign | Subacute; rapidly progressive | Primary CNS HS, including intramedullary disease with leptomeningeal dissemination ([Diagnostics 2026;16:2623](https://doi.org/10.3390/diagnostics16162623)); primary CNS HS case pair ([PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/)); CNS mimicking glioblastoma in older patients ([PMC12279446](https://pmc.ncbi.nlm.nih.gov/articles/PMC12279446/)) | Label "Abnormal CNS imaging"; ID not verified |
| Haemophagocytic syndrome (HLH-like) | Laboratory + clinical syndrome | Acute, severe, often terminal | Reported with splenic HS and with HS arising from FL ([PMC9124500](https://pmc.ncbi.nlm.nih.gov/articles/PMC9124500/); [PMC7481156](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7481156/)); with mediastinal GCT ([PMID 18987551](https://pubmed.ncbi.nlm.nih.gov/18987551/)) | Label "Hemophagocytosis"; ID not verified |

**Severity and progression.** Uniformly aggressive: Orphanet records "The neoplasm is aggressive with typically poor therapy response" ([ORPHA:86896](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)); the 2025 review describes an "aggressive clinical course with a limited response to therapy and a high mortality rate" ([Int J Mol Sci 2025;26:8554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)). Severity is bimodal by extent rather than by site: unifocal disease can be indolent after resection, multifocal disease is rapidly progressive (§11).

**Quality-of-life impact.** **No HS-specific QoL instrument data were retrieved.** The nearest evidence is from the broader histiocytic-neoplasm population: a prospective registry of **215** patients with histiocytic neoplasms using the Hospital Anxiety and Depression Scale found anxiety and depression were "stable over time and correlated with financial burden, symptom severity, and health-related quality of life" (quoted via retrieved extraction; [*Blood Adv* 2025;9(6):1376](https://ashpublications.org/bloodadvances/article/9/6/1376/534302/Anxiety-and-depression-in-patients-with)); survivorship issues in adult histiocytic neoplasms are reviewed in [PMC10481619](https://pmc.ncbi.nlm.nih.gov/articles/PMC10481619), and a Histiocytic Disorder Survivor Study with parallel HRQoL assessment was launched in September 2022 ([Blood Cancer United award page](https://bloodcancerunited.org/research/award/patient-reported-outcomes-and-survivorship-histiocytic-neoplasms)).

---

## 4. Genetic / Molecular Information

### 4.1 "Causal" genes (somatic drivers)
No germline causal gene exists. The recurrent somatic drivers, with gene symbols as retrieved (HGNC IDs could **not** be verified in this session and are therefore omitted rather than guessed):

- **RAS–MAPK:** *MAP2K1*, *KRAS*, *NRAS*, *BRAF*, *PTPN11*, *NF1*, *CBL* ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/))
- **PI3K–AKT–mTOR:** mutations activating this pathway in ~21–29% of cases ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [*Mod Pathol* 2023;36:100268](https://www.modernpathology.org/article/S0893-3952(23)00173-4/fulltext))
- **Tumour suppressors / cell cycle:** *CDKN2A* (39% of HS), *TP53* (24% of HS) ([Massoth et al., *The Oncologist* 2021;26:e1263](https://academic.oup.com/oncolo/article/26/7/e1263/6510483))
- **Chromatin/epigenetic modifiers:** *SETD2* (a defining feature of one molecular subgroup) ([Haematologica 2020;105(4):951–960](https://haematologica.org/article/view/9331)); epigenetic-modifier mutations in 59% of malignant histiocytoses ([*Mod Pathol* 2023;36:100268](https://www.modernpathology.org/article/S0893-3952(23)00173-4/fulltext))
- **Other reported in individual cases:** *FLT3*, *NOTCH2*, *KMT2A* in primary splenic HS with HLH ([PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/)); *NF1* mutation with *TUBB3* amplification in gastric HS ([Springer 2024, doi:10.1007/s00795-024-00393-0](https://link.springer.com/article/10.1007/s00795-024-00393-0))

### 4.2 Molecular subgroups
Whole-exome + RNA-sequencing of **21 archival primary HS** cases defined **two molecular subgroups** separating on the presence/absence of *NF1/PTPN11* alterations and the prevalence of *SETD2* mutations, confirmed by unsupervised clustering of RNA-seq data; the *NF1/PTPN11* wild-type cluster "was comprised primarily of cases with prototypic RAS/MAPK pathway activating mutations involving KRAS, NRAS, BRAF and MAP2K1" (quoted via retrieved extraction; [Haematologica 2020;105(4):951–960, doi:10.3324/haematol.2019.230375](https://haematologica.org/article/view/9331); accompanying editorial [PMID 32238464](https://pubmed.ncbi.nlm.nih.gov/32238464/)).

### 4.3 Variant classes and functional consequences
- **Activating missense hotspots**: *KRAS/NRAS* codons 12, 13 and 146; *PTPN11* gain-of-function mutations in the SH2 domain; *MAP2K1* mutations in the negative-regulatory helix and the core kinase domain; *BRAF* V600E ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)).
- **RAF-independent ("class III") *MEK1/2* mutations**, including the in-frame deletion **MEK1 E102_I103del**, are "common in patients with systemic histiocytic neoplasms, drive disease in a conditional knock-in mouse model, and associate with progression on FDA-approved MEK inhibitors" (quoted via retrieved extraction; [*Cancer Cell* 2025, PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/); [PMC12616613](https://pmc.ncbi.nlm.nih.gov/articles/PMC12616613/)).
- **Loss-of-function**: *NF1* (loss of RAS-GAP function → RAS-GTP accumulation), *CBL* (loss of E3-ubiquitin-ligase–mediated receptor downregulation), *CDKN2A* (mutation/deletion → loss of CDK4/6 restraint), *TP53* ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [*The Oncologist* 2021](https://academic.oup.com/oncolo/article/26/7/e1263/6510483); [*Leukemia* 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/)).
- **Structural/fusion events**: a novel **MIGA2::BRAF** fusion in primary CNS HS, "implicated in possible constitutive activation of the MAP kinase pathway"; the same tumour harboured two BRAF-related fusions ([*J Neuropathol Exp Neurol* 2024;83(10):882, PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/)). *IGH::BCL2* and *CCND1* rearrangements occur in HS transdifferentiated from FL and mantle cell lymphoma respectively ([AJCP 2025 abstract 509](https://academic.oup.com/ajcp/article/164/Supplement_1/aqaf121.281/8321081); [AJCP 2022](https://doi.org/10.1093/ajcp/aqac087)).
- **Somatic vs germline / ACMG classification**: all of the above are **somatic**; ACMG/AMP germline classification is not applicable, and the relevant framework is somatic tiering (e.g. OncoKB/AMP-ASCO-CAP). No HS-specific ClinVar germline curation was retrieved.
- **Population allele frequencies**: not applicable to somatic drivers; no HS-relevant gnomAD data retrieved.

### 4.4 Clonal relationships (the "secondary HS" genetics)
- **Follicular lymphoma → HS**: shared *IGH::BCL2* and identical *IGH* rearrangements establish common clonal origin; one case shared canonical FL mutations (*CREBBP*, *PIM1*) plus **MAP2K1 E203K**, "suggesting this mutation preceded transdifferentiation of the FL to HS" (quoted via retrieved extraction; [*Blood Cancer J* 2025](https://www.nature.com/articles/s41408-025-01335-4); [*KRAS* mutation in secondary malignant histiocytosis from low-grade FL, PMC6190545](https://pmc.ncbi.nlm.nih.gov/articles/PMC6190545/)).
- **B-lymphoblastic leukaemia/lymphoma → HS**: identical *IGH-MYC* and *IGK* rearrangements ([AJCP, doi:10.1093/ajcp/aqz056](https://dx.doi.org/10.1093/ajcp/aqz056)); shared *IGK/TCRB* rearrangements and *PAX5* alterations, with *PTPN11* mutation hypothesised as a transdifferentiation driver ([*Blood* 2016;128:2475](https://ashpublications.org/blood/article/128/20/2475/35616/Histiocytic-sarcoma-secondary-neoplasm-or); [*Am J Hematol*, doi:10.1002/ajh.26983](https://onlinelibrary.wiley.com/doi/full/10.1002/ajh.26983)); a clonally related HS emerging **33 years** after B-ALL ([PMC13472141](https://pmc.ncbi.nlm.nih.gov/articles/PMC13472141/)).
- **CLL/SLL, mantle cell lymphoma, myeloma, Hodgkin lymphoma**: documented clonal relationships ([*Mod Pathol* 7-case CLL/SLL series](https://www.modernpathology.org/article/S0893-3952(22)02794-6/fulltext); [AJCP 2022 *CCND1*](https://doi.org/10.1093/ajcp/aqac087); [PMC12270463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12270463/); [PMC12310312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12310312/)).
- **Cell of origin**: driver mutations traceable to **both myeloid and lymphoid** lineage cells in patients with histiocytic neoplasms "point[s] toward multipotent progenitors as the cell of origin"; the same *KRAS* or *BRAF* mutation was detected in lesions developing **up to 25 years apart**, implying long-lived mutated progenitors ([*Blood Neoplasia* 2025;2(2):100074, PMC12067900](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12067900/)); reviewed in [*J Pathol* 2026 (Kemps et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13432202/) and [*Nat Rev Dis Primers* "Histiocytic disorders"](https://www.nature.com/articles/s41572-021-00307-9).

### 4.5 Modifier genes
**None established for human HS.** Candidate modifiers emerge only from secondary/transdifferentiated disease (e.g. *PAX5* in B-ALL-derived HS; [*Am J Hematol*](https://onlinelibrary.wiley.com/doi/full/10.1002/ajh.26983)) and from canine genetics (§14).

### 4.6 Epigenetic information
- **Methylation classification works for HS**: in primary CNS HS, DNA-methylation data realigned to the NIH HEME classifier gave "a high confidence match (methylation class score 0.99) to HS", while the DKFZ sarcoma classifier gave no definite match ([PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/)); methylation profiling against the sarcoma classifier was decisive in other CNS histiocytic cases ([PMC12279446](https://pmc.ncbi.nlm.nih.gov/articles/PMC12279446/)).
- **Broader classifier context**: DNA-methylation classes have been defined across >1,400 haematolymphoid neoplasms with 97% diagnostic concordance in high-confidence cases ([*Blood Adv*, doi:10.1182/bloodadvances.2024015275](https://doi.org/10.1182/bloodadvances.2024015275)), and a nanopore-deployed classifier ("Lamprey") spans 86 haematologic entities including histiocytic disorders ([medRxiv 2026](https://www.medrxiv.org/content/10.64898/2026.07.02.26356825v1.full)).
- **Histiocytosis methylome biology** (non-HS histiocytoses, mechanistically relevant): 23,322 differentially methylated sites between controls and histiocytoses, with differentially methylated genes in inflammatory response, RAS, TNF and PI3K-mTOR signalling, and hypermethylation of the let-7b–encoding region ([PMC11794134](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11794134/); [ASH 2023 "Deciphering the Epigenetic Landscape in Histiocytic Neoplasms"](https://ashpublications.org/blood/article/142/Supplement%201/1161/505458/Deciphering-the-Epigenetic-Landscape-in)).
- Mutations in **epigenetic modulating genes in 59%** of malignant histiocytoses provide a genetic route to the same phenotype ([*Mod Pathol* 2023;36:100268](https://www.modernpathology.org/article/S0893-3952(23)00173-4/fulltext)).

### 4.7 Chromosomal abnormalities
Per the scope rules of this request, arm-level copy-number changes and chromothripsis are not described. At gene level, recurrent **CDKN2A deletions/mutations** are the best-documented copy-number lesion ([*The Oncologist* 2021;26:e1263](https://academic.oup.com/oncolo/article/26/7/e1263/6510483)), and gene-level fusions are listed in §4.3. Clonality-defining rearrangements in secondary HS (*IGH::BCL2*, *CCND1*, *IGH-MYC*, *IGK*) are detectable by FISH/PCR and are diagnostically useful (§10).

---

## 5. Environmental Information

- **Environmental factors / toxins / radiation / pollution / occupational exposure:** **no established associations retrieved.** No HS-specific entries in toxicogenomic or exposure-based sources surfaced in this session's searches.
- **Lifestyle factors:** **no evidence retrieved** (no smoking, alcohol, diet, obesity or physical-activity association).
- **Iatrogenic/host-state factors (the only non-genetic contributors with supporting reports):** chronic pharmacological immunosuppression after solid-organ transplantation ([PMC10546704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10546704/); [PMC5066022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5066022/)) and prior cytotoxic chemotherapy in the setting of an antecedent neoplasm ([PMID 33786289](https://pubmed.ncbi.nlm.nih.gov/33786289/)).
- **Infectious agents:** no pathogen is implicated as a cause. **EBV is characteristically not required**: in the renal-transplant HS literature review, EBV was positive in 2 cases and negative in another, with one report explicitly "the first report of HS in a solid organ recipient without evidence of EBV infection" (quoted via retrieved extraction; [PMC10546704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10546704/)). An in-vitro study models extracellular-vesicle secretion from histiocytic sarcoma cells in the context of bacterial co-infection, i.e. infection as a modifier of tumour-cell behaviour rather than a cause ([Int J Mol Sci, doi:10.3390/ijms27114949](https://doi.org/10.3390/ijms27114949)).

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (initiating lesion → clinical manifestation)

1. **A somatic activating lesion arises in the RAS–MAPK pathway** — *MAP2K1*, *KRAS*, *NRAS*, *BRAF* (including V600E and BRAF fusions such as MIGA2::BRAF), *PTPN11* (SH2-domain gain of function), or loss-of-function in the negative regulators *NF1* and *CBL* — **in a haematopoietic cell of the mononuclear-phagocyte lineage or in an upstream multipotent progenitor** ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/); [*Blood Neoplasia* 2025, PMC12067900](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12067900/)).
2. **This lesion leads to constitutive, ligand-independent flux through the MAPK cascade** (MAP3K→MEK1/2→ERK1/2; **GO:0000165** "MAPK cascade", [AmiGO](https://amigo.geneontology.org/amigo/term/GO:0000165)). The functional proof is pharmacological and in vivo: histiocytic neoplasms show "a notable dependence on MAPK signalling and are consequently responsive to MEK inhibition" (quoted via retrieved extraction; [*Nature* 2019, PMID 30867592](https://pubmed.ncbi.nlm.nih.gov/30867592/)), and conditional knock-in of MEK1 E102_I103del alone **drives a lethal histiocytic-like neoplasm in mice** ([*Cancer Cell* 2025, PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)).
3. **Constitutive ERK signalling results in a self-sustaining programme of proliferation and survival in the histiocyte/macrophage compartment**, together with blocked terminal quiescence — inferred for human HS from genotype–response concordance and demonstrated directly in the murine MEK1-mutant model ([PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)).
   - **Branch 3a — co-operating PI3K–AKT–mTOR activation** in ~21–29% of cases adds growth/metabolic signalling and a second survival input ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [*Mod Pathol* 2023](https://www.modernpathology.org/article/S0893-3952(23)00173-4/fulltext)). Canine whole-exome/transcriptome work independently shows concurrent **ERK and Akt pathway activation** in histiocytic sarcoma ([*Sci Rep* 2023, PMC10212919](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10212919/)).
   - **Branch 3b — loss of cell-cycle and genome-integrity brakes**: *CDKN2A* (39%) and *TP53* (24%) lesions remove G1 restraint and p53-dependent apoptosis/senescence, permitting the high-grade cytology and mitotic rate that define the tumour ([*The Oncologist* 2021](https://academic.oup.com/oncolo/article/26/7/e1263/6510483)). Canine transcriptomes show the downstream consequence as co-ordinated **cell-cycle activation (FOXM1, AURKB, PLK1, E2F)** ([*Cancers* 2025, PMC11940154](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940154/)).
   - **Branch 3c — epigenetic reprogramming**: mutations in epigenetic modulators (59% of malignant histiocytoses) and disease-associated methylome remodelling (including hypermethylation at the let-7b locus, with downstream *BCL2L1/BCL2* effects) stabilise the malignant macrophage state; HS has a methylation class distinct enough to be recognised by a haematologic classifier ([*Mod Pathol* 2023](https://www.modernpathology.org/article/S0893-3952(23)00173-4/fulltext); [PMC11794134](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11794134/); [PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/)).
   - **Branch 3d — transdifferentiation route**: when the mutation is acquired **within an existing lymphoid clone** (FL, CLL/SLL, MCL, B-ALL, myeloma), the RAS/MAPK lesion drives **lineage conversion to a histiocytic phenotype**, producing a secondary HS that carries the lymphoid clone's rearrangements. "The critical 'transdifferentiation' step to HDT appears to be associated with the acquisition of RAS/MAPK pathway alterations"; an epigenetic contribution has been hypothesised but not proven (quoted via retrieved extraction; [*Mod Pathol* 2021;34:336–347](https://www.nature.com/articles/s41379-020-00673-x); [*Blood Cancer J* 2025](https://www.nature.com/articles/s41408-025-01335-4)).
4. **Clonal expansion of malignant histiocytes produces a mass of large, non-cohesive, atypical cells with abundant eosinophilic cytoplasm**, retaining macrophage differentiation markers (CD163, CD68, lysozyme, CD4, CD11c, HLA-DR, PU.1) — the diagnostic phenotype ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/); [PMC11076448](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11076448/); [*Mod Pathol* CD163 series](https://www.nature.com/articles/3800346)).
5. **Local infiltration destroys the host tissue**, with the clinical consequence determined by site: bowel wall infiltration **leads to** obstruction, bleeding or (rarely) tumour-embolic necrosis ([PMC11452572](https://pmc.ncbi.nlm.nih.gov/articles/PMC11452572/)); bone infiltration **results in** lytic lesions; CNS infiltration **results in** focal deficits and leptomeningeal dissemination ([Diagnostics 2026;16:2623](https://doi.org/10.3390/diagnostics16162623)).
6. **Dissemination to lymph nodes, spleen, liver, marrow and other organs** follows, giving lymphadenopathy, hepatosplenomegaly and marrow infiltration ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896); [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [PMC6170302](https://pmc.ncbi.nlm.nih.gov/articles/PMC6170302/)).
7. **Marrow replacement plus macrophage-driven cytokine activation leads to cytopenias and, in a subset, a haemophagocytic (HLH-like) syndrome** with fever, hepatosplenomegaly and multilineage cytopenias — the tumour cells being competent phagocytes ([PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/); [PMC7481156](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7481156/)). *The cytokine step is inferred from HLH pathophysiology plus the macrophage phenotype, not demonstrated for HS specifically.*
8. **High glycolytic flux in the tumour cells makes the lesions intensely FDG-avid** (e.g. SUVmax 19.4), which is how extent and response are measured clinically ([*J Nucl Med Technol* 2021;49:358, PMID 34330800](https://pubmed.ncbi.nlm.nih.gov/34330800/)).
9. **Untreated or multifocal disease leads to progressive organ compromise and death**, with a median overall survival of roughly 6 months in aggregate series ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)).
10. **Therapeutic interruption of step 2 reverses the phenotype** — MEK inhibition yields complete and partial responses, and in MEK-inhibitor-resistant class III MEK1 mutants, **ERK inhibition** restores control; acquired *CBL* mutation is one route to MEK-inhibitor resistance, bypassable by **CSF1R inhibition** ([*Nature* 2019, PMID 30867592](https://pubmed.ncbi.nlm.nih.gov/30867592/); [*Cancer Cell* 2025, PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/); [*Leukemia* 2023, PMC10400417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/)). This pharmacological reversal is the strongest evidence that step 2 is the mechanistic bottleneck.

### 6.2 Category detail
- **Molecular pathways:** RAS–MAPK (dominant, upstream), PI3K–AKT–mTOR (co-operating), CDKN2A–CDK4/6–RB and p53 (downstream brakes removed), CSF1R-receptor signalling (ligand-receptor axis exploitable therapeutically) ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [PMC10400417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/)).
- **Cellular processes:** proliferation and cell-cycle dysregulation (FOXM1/AURKB/PLK1/E2F programme in the canine orthologous disease), evasion of apoptosis, tissue-infiltrative behaviour, phagocytosis/haemophagocytosis ([PMC11940154](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940154/); [PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/)).
- **Protein dysfunction:** gain of function (MEK1/2 kinase, mutant RAS, BRAF V600E and BRAF-fusion kinases, SHP2/PTPN11 phosphatase) and loss of function (neurofibromin's RAS-GAP activity; CBL ubiquitin-ligase activity; p16/CDKN2A; p53) ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/); [PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)).
- **Metabolic changes:** the only HS-specific metabolic read-out retrieved is **high FDG avidity**, i.e. elevated glucose uptake ([PMID 34330800](https://pubmed.ncbi.nlm.nih.gov/34330800/)). **No metabolomics or lipidomics studies of HS were retrieved.**
- **Immune system involvement:** the neoplastic cell is itself an immune (macrophage-lineage) cell; **PD-L1 is expressed in ~50% of HS cases**, and PD-L1 level correlates with checkpoint-inhibitor response (responders median 88% vs non-responders 30%), with loss of PD-L1 at a resistant site in one patient ([*Leuk Lymphoma* 2025, doi:10.1080/10428194.2025.2561114](https://dx.doi.org/10.1080/10428194.2025.2561114); [PMID 38098600](https://pubmed.ncbi.nlm.nih.gov/38098600/)). Secondary immune dysregulation manifests as HLH-like syndrome.
- **Tissue damage mechanisms:** direct infiltrative destruction and mass effect; obstruction; rarely vascular occlusion with infarction ([PMC11452572](https://pmc.ncbi.nlm.nih.gov/articles/PMC11452572/)). Fibrosis/oxidative-stress mechanisms specific to HS were not retrieved.
- **Biochemical abnormalities:** no enzyme deficiency, receptor-trafficking defect or channelopathy applies; the biochemistry is kinase hyperactivity (above).
- **Molecular profiling:** transcriptomics in human HS is limited to the RNA-seq clustering that defined the two molecular subgroups ([Haematologica 2020](https://haematologica.org/article/view/9331)); the deepest transcriptomic resource is canine ([PMC11940154](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940154/); [PMC10212919](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10212919/)). **No HS proteomics, metabolomics, lipidomics, single-cell or spatial-transcriptomics datasets were retrieved**, and no HS-specific CRISPR/RNAi dependency screen was found — these are genuine gaps.
- **Suggested ontology terms:** processes — **GO:0000165** MAPK cascade ([verified](https://amigo.geneontology.org/amigo/term/GO:0000165)); additional candidate labels (PI3K signalling, positive regulation of cell proliferation, macrophage differentiation) are listed by label only, IDs unverified this session. Cell types — **CL:0000235** macrophage and **CL:0000576** monocyte ([OLS4 CL:0000235](https://www.ebi.ac.uk/ols4/ontologies/cl/entities/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0000235); [CellGuide](https://cellxgene.cziscience.com/cellguide/CL:0000235)).

---

## 7. Anatomical Structures Affected

**Organ level — primary.** HS is predominantly **extranodal**. Orphanet: "Most cases occur in extranodal sites, most commonly the intestinal tract, skin, and soft tissue" ([ORPHA:86896](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)). A recent review reports the site distribution as **skin and connective tissue 41%, lymph nodes 14%, gastrointestinal tract 12%, haematopoietic system 9%** ([Front Oncol 2025](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1505737/xml)); the same review notes primary disease confined strictly to lymph nodes is "exceptionally unusual, accounting for less than 1% of documented cases". In the 27-patient tertiary-centre cohort, involvement was **lymph node 50%, soft tissue 40%, bone 36%, bone marrow 22%** ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)). Documented primary sites in the retrieved case literature include stomach ([PMC13478121](https://pmc.ncbi.nlm.nih.gov/articles/PMC13478121/)), oral cavity/jaws ([PMID 39048487](https://pubmed.ncbi.nlm.nih.gov/39048487)), head and neck ([Diagn Pathol 2007;2:7](https://diagnosticpathology.biomedcentral.com/articles/10.1186/1746-1596-2-7)), breast ([PMC11149727](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11149727/)), lung ([PMC10918721](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10918721/); [PMC12920180](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12920180/)), spleen ([PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/)), liver ([PMID 42405293](https://pubmed.ncbi.nlm.nih.gov/42405293/)), bladder ([PMC7888511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7888511/)), skin ([PMC12400779](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12400779/)), vertebra ([PMID 35884764](https://pubmed.ncbi.nlm.nih.gov/35884764/)) and CNS, including intramedullary spinal cord ([Diagnostics 2026;16:2623](https://doi.org/10.3390/diagnostics16162623); [PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/)).

**Organ level — secondary.** Multifocal spread to liver, spleen, marrow, lung and CNS (including CNS metastasis from a pulmonary primary, [PMC12920180](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12920180/)); marrow replacement causing cytopenias ([PMC6170302](https://pmc.ncbi.nlm.nih.gov/articles/PMC6170302/)).

**Body systems involved.** Haematopoietic/lymphoreticular (primary system of origin, reflected in the ICD-10 C96 placement), integumentary, digestive, musculoskeletal, nervous, respiratory, and genitourinary systems depending on site ([ICD-10-CM C96.A](https://icdlist.com/icd-10/C96.A); site citations above).

**Tissue and cell level.** The neoplastic population is the **mature macrophage/histiocyte** (**CL:0000235**, [verified](https://www.ebi.ac.uk/ols4/ontologies/cl/entities/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0000235)), developmentally downstream of the **monocyte** (**CL:0000576**) and, per lineage-tracing of driver mutations, of a multipotent haematopoietic progenitor ([PMC12067900](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12067900/)). Affected host tissues are connective/soft tissue, mucosa and submucosa of the gut, dermis, lymphoid tissue and marrow stroma; spindle-cell morphology can dominate in some tumours ([Diagn Pathol 2007;2:7](https://diagnosticpathology.biomedcentral.com/articles/10.1186/1746-1596-2-7)).

**Subcellular level.** Diagnostic localisations rather than mechanistic ones: **CD163 and CD68** are membrane/lysosomal-granule antigens, **lysozyme** is a granule/secreted protein and **PU.1 (SPI1)** is nuclear ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)). Signalling occurs at the plasma membrane–cytosol interface (RAS/RAF/MEK/ERK) with nuclear effector output. **GO cellular-component IDs were not verified in this session** and are therefore not asserted.

**Localisation / lateralisation.** Lesions are typically **unifocal and unilateral at presentation when localised**, or **multifocal/disseminated and asymmetric** when advanced; the unifocal/multifocal split is the main prognostic axis ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)). Verified UBERON terms for the principal sites: **UBERON:0000029** lymph node ([BioPortal/BCGO entry](https://m.bioportal.bioontology.org/ontologies/OBI_BCGO?conceptid=http://purl.obolibrary.org/obo/UBERON_0000029&p=classes)), **UBERON:0002106** spleen, **UBERON:0002371** bone marrow (both retrieved via ontology listings this session). Skin, intestine, brain and liver terms exist in UBERON but their exact IDs could not be confirmed in this session and are intentionally omitted.

---

## 8. Temporal Development

**Onset.** Adult-onset; Orphanet records age of onset simply as "Adult" ([ORPHA:86896](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)). Median age at diagnosis differs by cohort and ascertainment: **63 years (range 18–96)** in SEER ([Kommalapati et al., *Blood* 2018](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes)); **59 years (range 3–83)** in a 27-patient referral cohort ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)); **55 years (range 15–89)** in the 14-case extranodal series ([Hornick, Jaffe & Fletcher, *Am J Surg Pathol* 2004;28:1133–44](https://www.uptodate.com/contents/histiocytic-sarcoma/abstract/2)). One recent pediatric case review reports a median age of 46 years with a bimodal pattern (0–29 and 50–69 years) and notes HS is "more commonly reported in adults, typically in the sixth decade of life, [while] pediatric cases are distinctly uncommon" ([*Uncommon but intriguing: a pediatric primary histiocytic sarcoma case*, PMID 40486162 / PMC12144458](https://pmc.ncbi.nlm.nih.gov/articles/PMC12144458/)). **Onset pattern:** subacute, often with a painless mass or nonspecific systemic symptoms, then rapid progression; diagnostic delay from misdiagnosis is common ([PMID 41049224](https://pubmed.ncbi.nlm.nih.gov/41049224/); [PMID 40260333](https://pubmed.ncbi.nlm.nih.gov/40260333/)).

**Staging / stages.** No HS-specific staging system exists; MONDO-linked descriptions note it "usually present[s] as stage III/IV disease" ([MONDO/NORD](https://rarediseases.org/mondo-disease/histiocytic-sarcoma/)). Practically, disease is stratified as **unifocal/localised vs multifocal/disseminated**, with marrow involvement as an additional axis ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [*Blood* 2026 consensus, PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)).

**Progression rate and course.** Typically **rapid and progressive**: median OS ≈6 months overall ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)), and "the rate of survival does not improve over time" in population data ([PMC9297408](https://pmc.ncbi.nlm.nih.gov/articles/PMC9297408/)). However, the course is genuinely heterogeneous — the French national series of 141 malignant histiocytoses concluded that behaviour is heterogeneous and warrants tailored therapy ([*Blood Adv* 2025;9(10):2530](https://ashpublications.org/bloodadvances/article/9/10/2530/535782/Characterization-and-treatment-outcomes-of)), and localised disease can be chronic/curable (12 years disease-free after resection of oesophageal HS; [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)).

**Remission patterns.** Remissions are **treatment-induced**, not spontaneous: complete responses occur with chemotherapy (but with frequent relapse), with targeted MAPK-pathway inhibition (including durable CR >2 years on trametinib), with checkpoint blockade, and after allogeneic transplantation (3 of 4 allo-SCT patients in one review achieving CR, 2 with long-term remission) ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [JNCCN 2022, doi:10.6004/jnccn.2022.7001](https://doi.org/10.6004/jnccn.2022.7001); [PMID 38098600](https://pubmed.ncbi.nlm.nih.gov/38098600/); [TCT 2025 systematic review](https://www.sciencedirect.com/science/article/abs/pii/S2666636725002908)).

**Critical periods / windows of opportunity.** (i) **At first presentation of a localised lesion** — complete resection ± radiotherapy is when cure is realistically achievable ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [*Blood* 2026 consensus](https://pubmed.ncbi.nlm.nih.gov/41915766/)). (ii) **Before marrow involvement develops** — marrow involvement collapses median OS from 43 to 3 months in one cohort ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)). (iii) **At molecular profiling** — identifying an actionable MAPK lesion or high PD-L1 early opens the targeted/immunotherapeutic options that produce the most durable responses ([PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)).

---

## 9. Inheritance and Population

**Epidemiology.**
- **Incidence (US, SEER):** **0.17 per 1,000,000 per year** (159 cases captured); described as "ultra-rare" ([Kommalapati et al., *Blood* 2018;131:265–268](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes); [Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)).
- **Incidence (Europe, Orphanet):** annual incidence **<1/1,000,000** ([ORPHA:86896](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896)).
- **Prevalence:** no point-prevalence estimate was retrieved; given median survival of months, prevalence approximates incidence.
- **Share of haematological malignancies:** **<1%** ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)).

**Genetic-etiology items (all N/A for this disease, stated explicitly for the knowledge base).** Inheritance pattern: **not applicable — somatic, non-heritable**. Penetrance, expressivity, genetic anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency: **not applicable / no data**; no germline predisposition gene for human HS was retrieved in this session. (Heritability is established only in the canine disease — §14.)

**Population demographics.**
- **Sex:** male predominance — 99 men vs 60 women in SEER, female:male incidence ratio **0.49** ([*Blood* 2018](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes)); 63% male in the 27-patient cohort ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)). The extranodal 14-case series was female-weighted (8F/6M), illustrating small-series variance ([Hornick 2004](https://www.uptodate.com/contents/histiocytic-sarcoma/abstract/2)).
- **Age distribution:** adults, peaking in the sixth–seventh decades, with rare pediatric cases ([*Blood* 2018](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes); [PMC12144458](https://pmc.ncbi.nlm.nih.gov/articles/PMC12144458/)).
- **Ethnic/geographic distribution:** the SEER analysis was framed around "demographic disparities", but specific race/ethnicity effect sizes were not recoverable from the retrieved extraction; **no endemic area, geographic cluster, or population-specific variant distribution was retrieved.** Cases are reported worldwide (US, Europe, China, Japan, India, Brazil, Middle East across the case literature cited above).

---

## 10. Diagnostics

### 10.1 Biopsy, histopathology and immunohistochemistry (the diagnostic core)
**Histology:** diffuse growth of large, non-cohesive, polygonal/epithelioid cells with abundant eosinophilic cytoplasm; cytological atypia and prominent (including atypical) mitoses are treated as critical criteria for calling histiocytes malignant; spindle-cell morphology occurs ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/); [PMC11076448](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11076448/); [Diagn Pathol 2007;2:7](https://diagnosticpathology.biomedcentral.com/articles/10.1186/1746-1596-2-7)).

**Positive immunophenotype:** CD163, CD68 (KP1/PGM1), lysozyme, PU.1/SPI1, plus CD4, CD11c, CD45/LCA and HLA-DR ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/); [*Mod Pathol* five-case CD163 study](https://www.nature.com/articles/3800346)). **CD163 is preferred over CD68 for specificity, and "the combination of CD163 and PU.1 (SPI1) is highly specific for histiocytic sarcoma"** (quoted via retrieved extraction; [ScienceDirect topic page](https://www.sciencedirect.com/topics/medicine-and-dentistry/histiocytic-sarcoma); [*Arch Pathol Lab Med* review](https://meridian.allenpress.com/aplm/article/142/11/1322/103148/Histiocytic-Sarcoma-Review-Discussion-of)).

**Required negatives (to exclude mimics):** CD1a and Langerin (Langerhans cell neoplasms), CD21/CD35 (follicular dendritic cell sarcoma), strong S100 (interdigitating dendritic cell sarcoma), MPO/CD13 (myeloid sarcoma), CD20/CD30 (B-cell and other lymphomas), HMB-45/SOX10/S100 (melanoma), cytokeratins/EMA (carcinoma) ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/); [JCDR 2024 case](https://jcdr.net/articles/PDF/19763/70351_CE%5BRa1%5D_F(IS)_QC_Ref_Pat(PS_IS)_PF1(AG_KM)_PFA(AG_KM)_PN(KM).pdf)).

**Consensus minimum panel (2026):** the panel "should adequately confirm that the malignant cells show immunophenotypic differentiation toward mature cells of the mononuclear phagocytic lineage ... with **≥2 lineage-specific markers** expressed in the malignant cells"; and "among patients with abnormal peripheral blood counts, a bone marrow aspirate/biopsy is warranted to rule out a concomitant hematopoietic malignancy" (quoted via retrieved extraction; [*Blood* 2026;148(3):275–288, PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)).

Cytology/FNA can suggest the diagnosis but is not definitive alone ([PMC4349012](https://pmc.ncbi.nlm.nih.gov/articles/PMC4349012/); [PMID 29676378](https://pubmed.ncbi.nlm.nih.gov/29676378)).

### 10.2 Laboratory tests and biomarkers
No diagnostic serum biomarker exists. Relevant labs are supportive: full blood count (cytopenias), marrow examination when counts are abnormal, and the HLH work-up (ferritin, triglycerides, fibrinogen, soluble markers) when a haemophagocytic syndrome is suspected ([PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/); [PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/)). **PD-L1 immunohistochemistry functions as a predictive biomarker** and routine testing has been recommended, particularly in advanced disease ([*Leuk Lymphoma* 2025](https://dx.doi.org/10.1080/10428194.2025.2561114); [PMC10918721](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10918721/)).

### 10.3 Imaging
**¹⁸F-FDG PET/CT is the imaging backbone**: lesions show intense uptake (example SUVmax 19.4), and PET/CT "is a valuable tool in staging this rare entity and in assessing the response to therapy", also guiding biopsy site selection ([PMID 34330800](https://pubmed.ncbi.nlm.nih.gov/34330800/); [*J Nucl Med Technol* 49:358](https://tech.snmjournals.org/content/49/4/358)). NCCN recommends ¹⁸F-FDG-PET supplemented by organ-specific imaging for initial diagnosis, response assessment and follow-up ([*Histiocytic Neoplasms*, NCCN v2.2021, JNCCN 19(11), PMID 34781268](https://pubmed.ncbi.nlm.nih.gov/34781268/)). MRI is used for CNS/spinal disease, where HS can mimic glioblastoma radiologically in older adults ([PMC12279446](https://pmc.ncbi.nlm.nih.gov/articles/PMC12279446/); [Diagnostics 2026;16:2623](https://doi.org/10.3390/diagnostics16162623)).

**Functional tests, electrophysiology:** not part of HS diagnosis; no data retrieved.

### 10.4 Genetic and molecular testing
- **Recommended approach:** **broad molecular profiling (NGS panel covering MAPK/PI3K pathway genes and fusions) on tumour tissue** is a consensus recommendation, because results are directly actionable ([PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)). Published diagnostic series used targeted panels, whole-exome and RNA sequencing ([Haematologica 2020](https://haematologica.org/article/view/9331); [*The Oncologist* 2021](https://academic.oup.com/oncolo/article/26/7/e1263/6510483)).
- **WES/WGS:** research-grade utility demonstrated (WES+RNA-seq defined the two molecular subgroups) rather than routine clinical requirement ([Haematologica 2020](https://haematologica.org/article/view/9331)).
- **RNA sequencing / fusion testing:** needed to detect BRAF fusions such as MIGA2::BRAF that panel DNA sequencing may miss ([PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/)).
- **Single-gene testing:** BRAF V600E assessment (IHC/PCR) is the pragmatic minimum where broad panels are unavailable, given BRAF-inhibitor availability ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)).
- **FISH / clonality assays:** essential when a lymphoid neoplasm is present or suspected — t(14;18)/*IGH::BCL2* FISH and identical *IGH*/*IGK* rearrangement analysis establish clonal relatedness and the diagnosis of secondary/transdifferentiated HS ([*Blood Cancer J* 2025](https://www.nature.com/articles/s41408-025-01335-4); [AJCP 2025 abstract 509](https://academic.oup.com/ajcp/article/164/Supplement_1/aqaf121.281/8321081); [AJCP, doi:10.1093/ajcp/aqz056](https://dx.doi.org/10.1093/ajcp/aqz056)).
- **Chromosomal microarray / karyotype / mtDNA / repeat-expansion testing:** **no established role**; no HS-specific data retrieved. Germline genetic testing is not indicated (no germline predisposition gene known).
- **Epigenomic diagnostics:** DNA-methylation classification is an emerging adjunct and was decisive in difficult CNS cases, with a methylation class score of 0.99 against a haematologic classifier ([PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/); [PMC12279446](https://pmc.ncbi.nlm.nih.gov/articles/PMC12279446/); classifier context: [*Blood Adv*](https://doi.org/10.1182/bloodadvances.2024015275)).
- **Liquid biopsy:** droplet-digital-PCR detection of BRAF V600E in plasma/urine cell-free DNA is validated in LCH/ECD as a non-invasive mutation and response biomarker ([PMID 25324352](https://pubmed.ncbi.nlm.nih.gov/25324352/?dopt=Abstract); [PMC5705028](https://pmc.ncbi.nlm.nih.gov/articles/PMC5705028/)), **but** in a large cohort of adults with diverse histiocytic neoplasms there was "poor correlation between tumor and plasma cfDNA molecular findings ... possibly related to low tumor shedding especially among non-BRAF V600E cases" (quoted via retrieved extraction; [ASH 2023 abstract 6332](https://ashpublications.org/blood/article/142/Supplement%201/6332/506171/Molecular-Findings-on-Plasma-Cell-Free-DNA)). Tissue remains the reference specimen.
- **Proteomics / metabolomics diagnostics:** none retrieved.

### 10.5 Clinical criteria and differential diagnosis
There are no DSM/ICD-style criteria; diagnosis is **integrated histopathologic + immunophenotypic + molecular**, now codified by the WHO 5th edition and the 2026 consensus minimum criteria ([PMC9252913](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9252913/); [PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)). **Differential diagnosis** includes diffuse large B-cell lymphoma, other large-cell lymphomas, myeloid sarcoma, Langerhans cell sarcoma, interdigitating dendritic cell sarcoma, follicular dendritic cell sarcoma, melanoma, poorly differentiated carcinoma, pleomorphic sarcomas, and reactive/benign histiocytic proliferations and other histiocytoses; **ALK-positive histiocytosis is a separate disease entity and is excluded from this report per scope** ([*Arch Pathol Lab Med* 2018;142:1322](https://meridian.allenpress.com/aplm/article/142/11/1322/103148/Histiocytic-Sarcoma-Review-Discussion-of); [*Arch Pathol Lab Med* 2020;144:650](https://meridian.allenpress.com/aplm/article/144/5/650/427448/Histiocytic-Sarcoma); [SEER heme/lymph tool](https://seer.cancer.gov/seertools/hemelymph/51f6cf59e3e27c3994bd5471/)). A practical pitfall: tumours whose stroma is heavily enriched in reactive histiocytes were specifically excluded on central review in the French national series — i.e. histiocyte-rich ≠ histiocytic sarcoma ([*Blood Adv* 2025;9(10):2530](https://ashpublications.org/bloodadvances/article/9/10/2530/535782/Characterization-and-treatment-outcomes-of)).

### 10.6 Screening
**No screening is applicable or recommended**: there is no asymptomatic screening test, no newborn/carrier screening (no germline gene), and no cascade testing. The only surveillance context retrieved is clinical vigilance for secondary HS in patients with a known lymphoid malignancy or mediastinal germ cell tumour ([*Mod Pathol* 2021](https://www.nature.com/articles/s41379-020-00673-x); [PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)).

---

## 11. Outcome / Prognosis

**Survival and mortality.**
- **Median overall survival from diagnosis ≈6 months** in aggregate/population-level reporting, and survival has not improved over time ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/); [PMC9297408](https://pmc.ncbi.nlm.nih.gov/articles/PMC9297408/)).
- Referral-centre cohorts report longer medians, reflecting selection: **median OS 12 months** in a 27-patient cohort; a six-patient series reported median OS **52 months (range 0–153)** ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)).
- **5-/10-year survival figures specific to HS were not retrievable** in this session (the SEER letter's long-term outcome numbers could not be extracted); this is a gap to fill from the primary SEER publication.
- Mortality is overwhelmingly **disease-specific**: in the renal-transplant HS review, all 4 cases died despite chemotherapy in 3 ([PMC10546704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10546704/)).

**Prognostic factors (human, retrieved).**
| Factor | Effect | Source |
|---|---|---|
| **Multifocal vs unifocal disease** | Median OS **10 vs 125 months** (and 10 vs 50 months in a related analysis) | [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/) |
| **Bone marrow involvement** | Median OS **3 vs 43 months** | [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/) |
| Treatment modality (proxy for resectability) | Surgery median OS **42 months** vs chemotherapy **12 months** | [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/) |
| Localised, completely resected disease ± radiotherapy | Long-term disease-free survival achievable (e.g. 12 years) | [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/) |
| Actionable MAPK lesion | Enables targeted therapy with high response rates and durable responses | [*Nature* 2019, PMID 30867592](https://pubmed.ncbi.nlm.nih.gov/30867592/); [JNCCN 2022](https://doi.org/10.6004/jnccn.2022.7001) |
| High PD-L1 expression | Associated with response to checkpoint blockade (responders median 88% vs 30%) | [*Leuk Lymphoma* 2025](https://dx.doi.org/10.1080/10428194.2025.2561114) |
| Class III (RAF-independent) MEK1/2 mutation | Predicts **progression on MEK inhibitors**; predicts ERK-inhibitor sensitivity | [*Cancer Cell* 2025, PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/) |
| Acquired *CBL* mutation | MEK-inhibitor resistance | [*Leukemia* 2023, PMC10400417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/) |

**Morbidity, disability and function.** No ICF-coded disability data or HS-specific disability registry data were retrieved. Morbidity is driven by site (bowel obstruction, neurological deficit, pathological bone lesions), by cytopenias, and by treatment toxicity. The histiocytic-neoplasm QoL evidence summarised in §3 (anxiety/depression correlating with symptom severity and financial burden) is the closest available surrogate ([*Blood Adv* 2025;9(6):1376](https://ashpublications.org/bloodadvances/article/9/6/1376/534302/Anxiety-and-depression-in-patients-with)).

**Complications and recovery potential.** Complications include haemophagocytic syndrome ([PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/)), marrow failure ([PMC6170302](https://pmc.ncbi.nlm.nih.gov/articles/PMC6170302/)), bowel obstruction/perforation/infarction ([PMC11452572](https://pmc.ncbi.nlm.nih.gov/articles/PMC11452572/)), CNS dissemination ([Diagnostics 2026;16:2623](https://doi.org/10.3390/diagnostics16162623)), and in secondary disease, evolution of the companion lymphoid malignancy — one BRAF-mutated histiocytic/dendritic cell sarcoma transdifferentiated from FL responded durably to BRAF/MEK inhibition and then evolved to high-grade B-cell lymphoma ([PMID 42264920](https://pubmed.ncbi.nlm.nih.gov/42264920/)). Recovery potential is **good only for completely resected unifocal disease**; without effective therapy, disseminated disease is fatal within months.

---

## 12. Treatment

> There is no randomised evidence in HS. All recommendations below derive from retrospective series, consensus statements and trials in the broader histiocytic-neoplasm population. NCIT identifiers are given only where retrieved.

### 12.1 Treatment strategy / algorithm
The 2026 international consensus algorithm: **surgical resection for unifocal disease**, and for multifocal disease **targeted therapy or immune checkpoint inhibition when actionable mutations or PD-L1 expression are present** ([*Blood* 2026;148(3):275–288, PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)). NCCN (Histiocytic Neoplasms v2.2021) positions **systemic chemotherapy** as primary therapy for HS, specifically for multifocal/multi-organ, recurrent or refractory disease, with **watch-and-wait** an option in asymptomatic cases, and lists genotype-matched options as clinically indicated — including **selpercatinib** for RET rearrangements, **pexidartinib** for activating CSF1R mutations, and **larotrectinib/entrectinib** for NTRK fusions ([JNCCN 2021;19(11), PMID 34781268](https://pubmed.ncbi.nlm.nih.gov/34781268/); [NCCN guideline PDF](https://www.erdheim-chester.org/wp-content/uploads/2022/08/NCCN-Guidelines-for-Histiocytic-Neoplasms.pdf)). The French national series concluded that "prospective follow-up and a standardized treatment approach in specialized reference centers are crucial to improving patient survival" (quoted via retrieved extraction; [*Blood Adv* 2025;9(10):2530](https://ashpublications.org/bloodadvances/article/9/10/2530/535782/Characterization-and-treatment-outcomes-of)).

### 12.2 Conventional pharmacotherapy (cytotoxic)
Most-used regimens are **CHOP** (cyclophosphamide, doxorubicin, vincristine, prednisone) and **ICE** (ifosfamide, carboplatin/cisplatin, etoposide), with ABVD also reported; "the two most commonly utilized regimens are CHOP or ICE though response rates are poor", and relapse after CHOP is frequent ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [Front Oncol 2025](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1505737/xml); [Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)). In pediatric malignant histiocytosis, **topotecan + temozolomide** produced CR in 2 of 7 treated children (28%) in the French series ([*Blood Adv* 2025](https://ashpublications.org/bloodadvances/article/9/10/2530/535782/Characterization-and-treatment-outcomes-of)).

### 12.3 Targeted therapy (the highest-yield modality)
- **MEK inhibitors.** **Cobimetinib** (NCIT **C68923**; MEK-inhibitor class NCIT **C69145**) was **FDA-approved on 28 October 2022 for adult patients with histiocytic neoplasms** — the first approval for this disease family — on the basis of the MSK phase 2 single-agent trial (NCT02649972), in which the overall response rate was **89%** (90% CI 73–100%) by PET with 13 CR and 3 PR among 18 patients; at one year 100% of responses were ongoing and 94% remained progression-free, with responses across ARAF, BRAF, RAF1, NRAS, KRAS, MEK1 and MEK2 genotypes ([*Nature* 2019, PMID 30867592](https://pubmed.ncbi.nlm.nih.gov/30867592/); [MSK news release](https://www.mskcc.org/news-releases/fda-approves-oral-mek-inhibitor-cobimetinib-histiocytic-neoplasms-research-led-msk-cancer); [ASCO Post](https://ascopost.com/issues/december-10-2022/fda-approves-oral-mek-inhibitor-cobimetinib-for-histiocytic-neoplasms/); [ASH 2023 phase 2 report](https://ashpublications.org/blood/article/142/Supplement%201/1812/505051/Phase-2-Trial-of-Single-Agent-Cobimetinib-for)). Note: that trial population was dominated by other histiocytoses; HS-specific efficacy rests on case-level evidence.
- **Trametinib** (NCIT **C77908**; [EVS Explore](https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C77908)) in HS: rapid, durable **complete response >2 years** with a *MAP2K1* F53L mutation; **near-complete response** with somatic *KRAS* Q61H ([ResearchGate record of the MAP2K1 case](https://www.researchgate.net/publication/325191894_Trametinib_in_Histiocytic_Sarcoma_with_an_Activating_MAP2K1_MEK1_Mutation); [JNCCN 2022;20(6), doi:10.6004/jnccn.2022.7001](https://doi.org/10.6004/jnccn.2022.7001)); multifocal HS responding to trametinib + imatinib but stopped at 5 months for grade 3 toxicity ([Haematologica](https://haematologica.org/article/view/8337)); a *PTPN11*-variant case achieved only partial response with progression at 5 months ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)).
- **Cobimetinib in HS specifically:** clinical response reported in an *NF1*-mutated HS ([PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/)); switching from poorly tolerated/partially effective trametinib to cobimetinib produced a dramatic response with the patient disease-free 3 years later ([*J Hematol*](https://www.thejh.org/index.php/jh/article/view/1030/678)).
- **Luvometinib (FCN-159)**, a selective MEK1/2 inhibitor, in a single-arm multicentre phase 2 in histiocytic neoplasms (29 evaluable; 22 LCH, 3 ECD, 4 other subtypes): confirmed **ORR 61.5%**, all 15 PET-evaluated patients achieving a metabolic response (80% complete metabolic response), ORR 94.4% in BRAF-altered and 42.9% in *MAP2K1*-mutant disease ([*eClinicalMedicine* 2025, PMID 41035796 / PMC12481021](https://pmc.ncbi.nlm.nih.gov/articles/PMC12481021/)).
- **BRAF inhibitors** (vemurafenib, dabrafenib) for BRAF V600E disease, including combined BRAF/MEK inhibition with prolonged response in secondary BRAF-mutated histiocytic/dendritic cell sarcoma arising from FL ([Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/); [PMID 42264920](https://pubmed.ncbi.nlm.nih.gov/42264920/)).
- **ERK inhibition for MEK-inhibitor resistance:** five patients with MEK1 E102_I103del (four MEK-inhibitor-refractory) were treated with **ulixertinib** with response; a focused phase 2 of ulixertinib in adults with histiocytoses is planned ([*Cancer Cell* 2025, PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/); [*Cancer Discov* highlight](https://aacrjournals.org/cancerdiscovery/article-abstract/16/1/OF1/771345/RAF-independent-MEK1-mutant-Histiocytoses-Respond?redirectedFrom=fulltext)).
- **CSF1R inhibition:** dramatic, lasting response to CSF1R inhibition in a histiocytosis patient with acquired *CBL* mutations refractory to MEK1/2 inhibition, broadening CSF1R inhibition beyond CSF1R-mutant disease ([*Leukemia* 2023, PMC10400417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/)); pexidartinib is the NCCN-listed CSF1R option ([PMID 34781268](https://pubmed.ncbi.nlm.nih.gov/34781268/)). Non-MAPK targets in histiocytic disorders are reviewed in [*JCO Precision Oncology* 2025](https://ascopubs.org/doi/10.1200/PO-24-00471).
- **Selumetinib** produced effective disease control in HS evolving from B-ALL ([PMID 41798885](https://pubmed.ncbi.nlm.nih.gov/41798885/)).

### 12.4 Immunotherapy
- **Pembrolizumab** gave a durable long-term response in widespread PD-L1-high HS — reported as the first such documented case ([PMID 38098600 / PMC10718375](https://pmc.ncbi.nlm.nih.gov/articles/PMC10718375/)).
- **PD-L1 expression in ~50% of HS**; in a combined patient + literature ICI cohort (N=20), responders had higher median PD-L1 than non-responders (**88% vs 30%**), and loss of PD-L1 was found at a resistant site ([*Leuk Lymphoma* 2025, doi:10.1080/10428194.2025.2561114](https://dx.doi.org/10.1080/10428194.2025.2561114)).
- **Pembrolizumab + GDP chemotherapy** induced sustained remission in a case report ([PMC11366101](https://pmc.ncbi.nlm.nih.gov/articles/PMC11366101/)); immunotherapy benefit also reported in PD-L1-high primary pulmonary HS ([*Clin Respir J* 2024, doi:10.1111/crj.13741](https://onlinelibrary.wiley.com/doi/10.1111/crj.13741)); long-term remission with combined immune-targeted treatment in HS accompanying FL ([Int J Mol Sci 2024;25:7293](https://www.mdpi.com/1422-0067/25/13/7293)).

### 12.5 Cell therapy / transplantation
- **Autologous HSCT** has been used as consolidation after anthracycline-based induction ([PMID 41580890 / PMC12853904](https://pmc.ncbi.nlm.nih.gov/articles/PMC12853904/); [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/)).
- **Allogeneic HSCT** is recommended in refractory/relapsed disease: a PRISMA systematic review (99 studies, adults ≥18 years) of allo-HSCT for HS reported 10 transplanted patients (5 allogeneic, 5 consolidative autologous); among 4 allo-SCT patients, 3 achieved CR and 2 maintained long-term remission ([*Transplant Cell Ther* 2025](https://www.sciencedirect.com/science/article/abs/pii/S2666636725002908); [ASH 2024 abstract, doi:10.1182/blood-2024-208929](https://doi.org/10.1182/blood-2024-208929); durable response case: [*Hematol Rep* 2026, doi:10.3390/hematolrep18010002](https://doi.org/10.3390/hematolrep18010002)). Reduced-intensity allo-SCT has also been used for mediastinal-GCT-associated histiocytic proliferations ([PMC4718299](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4718299/)).
- **CAR-T, gene therapy, RNA-based therapy:** **no HS-specific evidence retrieved.**

### 12.6 Surgery, radiotherapy, supportive care
- **Surgery:** complete resection is the treatment of choice for unifocal disease, with the best survival in retrospective comparison (median OS 42 months for surgically treated vs 12 months for chemotherapy-treated patients) ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/)).
- **Radiotherapy:** effective for localised lesions and as adjuvant therapy to reduce recurrence; successful CNS HS management with craniectomy plus adjuvant radiotherapy is documented ([PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [PMC9162887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9162887/)).
- **Supportive/rehabilitative care:** no HS-specific guideline retrieved; palliative care use in disseminated disease is documented in the case literature ([palliative home care in secondary HS](https://www.researchgate.net/publication/276347560_Palliative_care_in_the_home_a_case_study_of_secondary_histiocytic_sarcoma_in_a_3-year-old_child)).

### 12.7 Experimental treatments and trials (NCT identifiers retrieved)
| Trial | Agent / population | Status per retrieval |
|---|---|---|
| [NCT02649972](https://clinicaltrials.gov/study/NCT02649972) | Single-agent cobimetinib, adults with histiocytic disorders (basis of FDA approval) | Completed/reported |
| [NCT04079179](https://clinicaltrials.gov/study/NCT04079179) | Cobimetinib in refractory LCH and other histiocytic disorders | Recruiting; primary completion est. 2028-01 |
| [NCT04007848](https://clinicaltrials.gov/study/NCT04007848) | Cobimetinib for BRAF-wild-type or mutated histiocytoses | Listed |
| [NCT04437381](https://clinicaltrials.gov/study/NCT04437381) | Molecular targets for the treatment of histiocytosis (French molecular study) | Underway |
| Planned | Phase 2 **ulixertinib** (ERK inhibitor) in adults with histiocytoses | "soon-to-be initiated" per [*Cancer Cell* 2025](https://pubmed.ncbi.nlm.nih.gov/41135521/) |

### 12.8 Response rates, adverse events, pharmacogenomics
Response rates are summarised above (chemotherapy: poor and non-durable; MEK inhibition: 89% ORR in the approval trial population, 61.5% with luvometinib; BRAF/MEK combinations and ICI: case-level durable responses). **Toxicity** signals retrieved: grade 3 adverse events forcing discontinuation of trametinib+imatinib at 5 months, and poor tolerance of trametinib prompting a switch to cobimetinib ([Haematologica](https://haematologica.org/article/view/8337); [*J Hematol*](https://www.thejh.org/index.php/jh/article/view/1030/678)). **No HS-specific pharmacogenomic (PharmGKB/CPIC) guidance was retrieved**; the actionable "pharmacogenomics" here is **somatic genotype-guided therapy** (BRAF V600E → BRAF±MEK inhibitor; MAP2K1/KRAS/NRAS/NF1 → MEK inhibitor; class III MEK1/2 → ERK inhibitor; CBL → CSF1R inhibitor; high PD-L1 → checkpoint inhibitor).

**NCIT suggestions (verified in session):** cobimetinib **NCIT:C68923**; trametinib **NCIT:C77908**; MEK-inhibitor class **NCIT:C69145**. NCIT codes for CHOP, ICE, allogeneic HSCT, radiotherapy and pembrolizumab exist but **were not verified in this session** and are therefore not asserted.

---

## 13. Prevention

- **Primary prevention:** **none available or established.** There is no known modifiable exposure, no vaccine-preventable cause, and no germline risk to counsel about. This follows directly from §2.2/§5, where no environmental or lifestyle risk factor was retrieved.
- **Secondary prevention / early detection:** no population screening exists and none is justified at an incidence of ~0.17/1,000,000 ([*Blood* 2018](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes)). The actionable early-detection practice is **clinical and pathological vigilance in high-risk clinical contexts**: new mass, cytopenias or FDG-avid lesions in a patient with FL, CLL/SLL, MCL, B-ALL, myeloma or Hodgkin lymphoma, or after a mediastinal germ cell tumour, should prompt biopsy with histiocytic-marker IHC and clonality testing ([*Mod Pathol* 2021](https://www.nature.com/articles/s41379-020-00673-x); [PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/); [PMID 33786289](https://pubmed.ncbi.nlm.nih.gov/33786289/)). Transplant recipients with unexplained masses are a second such context ([PMC10546704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10546704/)).
- **Tertiary prevention (preventing complications in diagnosed patients):** complete resection ± radiotherapy of unifocal disease to prevent dissemination; bone marrow evaluation when counts are abnormal to detect concomitant haematopoietic malignancy; broad molecular profiling at diagnosis so that resistance-relevant genotypes (class III MEK1/2, CBL) are known before committing to MEK inhibition; recognition and management of haemophagocytic syndrome ([PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/); [PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/); [PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/); [PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/)).
- **Immunization, genetic screening, PGD/prenatal testing, carrier screening, genetic counselling, risk stratification models, behavioural interventions, public-health or environmental interventions, prophylactic medication:** **not applicable** — no germline basis, no infectious cause, no environmental cause, and no validated risk model for HS was retrieved.

---

## 14. Other Species / Natural Disease

**Taxonomy and veterinary importance.** The **domestic dog** (*Canis lupus familiaris*, **NCBI taxon 9615**, as encoded in the OMIA record identifier) has a naturally occurring, clinically and molecularly homologous disease: **OMIA:000620-9615 "Histiocytosis, malignant"** ([OMIA entry](https://omia.org/OMIA000620/9615/)). It is a major veterinary problem, not a curiosity: canine histiocytic sarcoma affects **15–25% of Bernese Mountain Dogs**, with disseminated disease accounting for up to **~25% of deaths in the breed** ([*Breed-predispositions to cancer in pedigree dogs*, PMC3658424](https://pmc.ncbi.nlm.nih.gov/articles/PMC3658424/); [*Epidemiology, pathology, and genetics of histiocytic sarcoma in the Bernese mountain dog breed*, PMID 19531730](https://pubmed.ncbi.nlm.nih.gov/19531730/)).

**Breeds (VBO identifiers not retrieved; breed names as recorded).** Bernese Mountain Dog, Flat-Coated Retriever, Rottweiler, Golden Retriever and Miniature Schnauzer are recorded in OMIA, with sporadic cases in many breeds ([OMIA:000620-9615](https://omia.org/OMIA000620/9615/); [UC Davis histiocytosis program](https://www.histiocytosis.ucdavis.edu/); [NC State canine HS page](https://hospital.cvm.ncsu.edu/services/small-animals/cancer-oncology/oncology/canine-histiocytic-sarcoma/)). Clinical phenotypes differ between predisposed breeds ([*Comparison of the clinical characteristics of histiocytic sarcoma in Bernese Mountain Dogs and Flat-Coated Retrievers*, PMC9504151](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9504151/)).

**Genes and orthologues (gene symbols; NCBI Gene IDs not retrieved).**
- **Germline susceptibility:** the **MTAP–CDKN2A locus** confers susceptibility to canine HS — the first GWAS for histiocytic sarcoma in any species — with evidence that risk-haplotype variants affect *CDKN2A/CDKN2B* expression in susceptible dogs ([*Cancer Epidemiol Biomarkers Prev* 2012;21:1019](https://cebp.aacrjournals.org/content/21/7/1019)). A four-breed study confirmed the main role of the CDKN2A locus and identified four additional predisposing loci; an oligogenic mode of transmission is proposed, with no single Mendelian mode established ([PMC8016107](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8016107/); [OMIA:000620-9615](https://omia.org/OMIA000620/9615/)).
- **Somatic drivers shared with humans:** activating **PTPN11** and **KRAS** mutations in canine histiocytic sarcoma, and *PTPN11* mutations described jointly in canine and human disseminated HS ([PMC6678586](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6678586/); [ResearchGate record: *PTPN11 mutations in canine and human disseminated histiocytic sarcoma*](https://www.researchgate.net/publication/340167279_PTPN11_mutations_in_canine_and_human_disseminated_histiocytic_sarcoma)).
- **Pathway concordance:** canine whole-exome + transcriptome analysis demonstrates **ERK and Akt pathway activation**, mirroring the human MAPK + PI3K architecture ([*Sci Rep* 2023, PMC10212919](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10212919/)).

**Comparative pathology and evolutionary conservation.** Canine localised and disseminated histiocytic sarcomas are considered to be of myeloid dendritic cell origin, a notable difference from the mature-macrophage phenotype emphasised in human HS ([Wikipedia: Canine histiocytic diseases](https://en.wikipedia.org/wiki/Canine_histiocytic_diseases); [*Canine histiocytic malignancies — challenges and opportunities*, PMC5644619](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5644619/)). Shared features: aggressive multi-organ disease, poor prognosis, MAPK/PI3K dependence, and cell-cycle-driven transcriptomes. Canine therapy response: **lomustine (CCNU)** at 60–90 mg/m² gave a **46% overall response rate in 56 dogs with gross measurable disease**, with **median survival of 106 days across 59 dogs**; thrombocytopenia (<100,000/µL) and hypoalbuminaemia predicted <1-month survival ([Skorupski et al., PMID 17338159](https://pubmed.ncbi.nlm.nih.gov/17338159/); [doi:10.1111/j.1939-1676.2007.tb02937.x](https://doi.org/10.1111/j.1939-1676.2007.tb02937.x)); lomustine+doxorubicin combinations have also been evaluated ([ResearchGate record](https://www.researchgate.net/publication/274402918_Evaluation_of_a_combination_chemotherapy_protocol_including_lomustine_and_doxorubicin_in_canine_histiocytic_sarcoma)). Risk-factor epidemiology within the breed has been studied formally ([*J Vet Intern Med*, doi:10.1111/jvim.13964](https://doi.org/10.1111/jvim.13964)).

**Other species.** Histiocytic sarcoma occurs naturally in **laboratory mice** (see §15) and has been reported in a **degu (*Octodon degus*)** ([PMID 38556322 / PMC11144536](https://pmc.ncbi.nlm.nih.gov/articles/PMC11144536/)) and an **Amami spiny rat (*Tokudaia osimensis*)** ([PMC11442397](https://pmc.ncbi.nlm.nih.gov/articles/PMC11442397/)).

**Transmission.** **No zoonotic potential and no cross-species transmissibility** — HS is a non-infectious clonal neoplasm; cross-species relevance is comparative/translational only.

---

## 15. Model Organisms

**Mouse — spontaneous and background disease.** Histiocytic sarcoma is a well-recognised spontaneous neoplasm of laboratory mice; Janke & Rehg catalogued its morphological range in **C57BL/6J** mice, noting that spindle cells and small round cells co-occur, often within the same tissue, in ~80% of cases ([*Vet Pathol* 2023;60(4):443–460, doi:10.1177/03009858231166658](https://journals.sagepub.com/doi/10.1177/03009858231166658)). Additional spontaneous reports: epididymal HS in a **CD-1** mouse ([PMC11219191](https://pmc.ncbi.nlm.nih.gov/articles/PMC11219191/)); concurrent B-lymphoblastic lymphoma and HS in a C57BL/6 mouse ([PMC12906819](https://pmc.ncbi.nlm.nih.gov/articles/PMC12906819/)); abdominal distension in an aged female mouse ([PMID 40783184](https://pubmed.ncbi.nlm.nih.gov/40783184/)). Background incidence in aging mice and GEM lines is reviewed by [Brayton, Treuting & Ward (*Vet Pathol* 2012)](https://journals.sagepub.com/doi/10.1177/0300985811430696). **Implication for model use:** spontaneous murine HS is a confounder in aging/toxicology studies as well as a resource.

**Mouse — genetic models.**
- **Conditional knock-in of the human class III mutation MEK1 E102_I103del** drives a **lethal histiocytic-like neoplasm**, sensitive to the ERK1/2 inhibitor ulixertinib — the most mechanistically faithful model retrieved, since it reproduces both disease and the clinically observed drug-resistance/sensitivity pattern ([*Cancer Cell* 2025, PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)).
- **Forward-genetic (Sleeping Beauty transposon) screen** with myeloid-restricted mutagenesis via the *Lysozyme2* promoter: mice had significantly shortened lifespan and most developed tumours resembling human HS; 27 common insertion sites yielded **28 candidate cancer genes**, including *Raf1*, *Fli1*, *Mitf*, *Nf1*, *Myc*, *Jak2* and *Pten* ([*PLoS ONE* 2014;9(5):e97280](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0097280); [PMC4020815](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4020815/)).
- **Elevated HS incidence in engineered lines**: *Ing2*, *p21^Waf1/Cip1/Sdi1^*, *Trp53*-family mutants, and *Dok1/Dok2/Dok3* triple-deficient mice; the field explicitly notes that **GEMs carrying the common human HS drivers (e.g. BRAF^V600E^) would be valuable for therapeutic testing** ([Int J Mol Sci 2025 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/)). Nonsense-mutant p53 mice develop frequent multicentric/metastatic tumours including histiocytic lesions ([bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.03.12.642796v2.full)).
- **Inflammation-associated, age-dependent model:** *CD4Cre*-driven SHIP1 (*Inpp5d*) deletion produces spontaneous widely disseminated histiocytic sarcoma correlating with age, "in the absence of engineered oncogenic drivers" ([PMC13627489](https://pmc.ncbi.nlm.nih.gov/articles/PMC13627489)).
- **Induced model:** histiocytic sarcoma can be induced in mouse skeletal muscle ([*PLoS ONE* 2012;7:e44044 / PMC3432091](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3432091/)).

**Cell lines / in vitro.** A significant limitation: a canine-model paper states that **no human histiocytic sarcoma cell line is available for research**, which is why the human **U-937** histiocytic *lymphoma* line (**CVCL_0007**, [Cellosaurus](https://www.cellosaurus.org/CVCL_0007)) and animal lines are used as surrogates ([*A novel canine histiocytic sarcoma cell line*, PMC5831740](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5831740/)). Available models include canine **CHS-2** (CVCL_L315, Shetland Sheepdog, skin; [Cellosaurus](https://www.cellosaurus.org/CVCL_L315)), **PWC-HS01** (CVCL_IU62, Pembroke Welsh Corgi, brain; [Cellosaurus](https://www.cellosaurus.org/CVCL_IU62)), **DH82**, and the murine **M5076** (CVCL_3997, ovarian histiocytic sarcoma; [Cellosaurus](https://www.cellosaurus.org/CVCL_3997)), **HS-MM** (CVCL_W472) and **J774A.1**, the latter used as a direct analogue of human HS in vitro ([doi:10.3390/ijms27114949](https://doi.org/10.3390/ijms27114949)). A permanent human **dendritic** sarcoma line (U-DCS) exists for the related dendritic-cell tumours ([PMC7718904](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7718904/)). **No HS organoid or iPSC model was retrieved.**

**Phenotype recapitulation and limitations.**
- *Recapitulated:* macrophage/histiocyte-lineage tumours with multi-organ dissemination; MAPK dependence and MEK/ERK-inhibitor pharmacology (MEK1-mutant knock-in); cell-cycle-driven transcriptional programmes and AURK-inhibitor/trametinib synergy (canine lines) ([PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/); [*Cancers* 2025, PMC11940154](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940154/)).
- *Not recapitulated:* the human **secondary/transdifferentiation** route from a lymphoid clone; the human extranodal site distribution; germline susceptibility (modelled only in dogs); and human immune-microenvironment features such as PD-L1-dependent checkpoint response. The absence of a human HS cell line is the single biggest resource gap ([PMC5831740](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5831740/)).

**Applications.** Driver-gene discovery (transposon screen), causal proof of MEK-mutant pathogenicity and resistance biology (knock-in mouse), drug screening and combination discovery (canine cell lines ± trametinib and aurora-kinase inhibitors), and comparative-oncology trials in dogs as a bridge to human trials ([*PLoS ONE* 2014](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0097280); [PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/); [PMC11940154](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940154/); [PMC5644619](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5644619/)).

**Model resources.** OMIA (canine entry above); Cellosaurus (cell lines above). MGI/IMPC/IMSR/MMRRC-specific allele records for HS-relevant lines were **not retrieved in this session** and should be looked up directly when populating the knowledge base.

---

## Explicit gaps (retrieved as absent, not assumed)

1. **HS-specific 5- and 10-year survival** from SEER — the primary letter's long-term figures could not be extracted in this session.
2. **HGNC IDs, NCBI Gene IDs, VBO breed IDs, and several HPO/UBERON/GO cellular-component IDs** — not verifiable with the tooling available here; labels are given instead, and unverified IDs are deliberately omitted.
3. **Proteomics, metabolomics, lipidomics, single-cell and spatial transcriptomics of human HS; CRISPR/RNAi dependency screens in HS** — none retrieved; these appear not to exist for this entity at present.
4. **Environmental, occupational, lifestyle, and gene–environment risk data** — none retrieved.
5. **HS-specific quality-of-life/PRO instruments** — none retrieved; only histiocytic-neoplasm-wide PRO data.
6. **A current NCCN version later than Histiocytic Neoplasms v2.2021** — not retrieved; the 2026 Histiocyte Society consensus is the most recent guidance found.

---

## Sources

- [Histiocytic Sarcoma: A Review and Update (Int J Mol Sci 2025;26:8554) — PMC12429796](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/) · [doi:10.3390/ijms26178554](https://doi.org/10.3390/ijms26178554) · [MDPI](https://www.mdpi.com/1422-0067/26/17/8554)
- [Orphanet: Histiocytic sarcoma (ORPHA:86896)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896) · [MONDO/NORD: histiocytic sarcoma](https://rarediseases.org/mondo-disease/histiocytic-sarcoma/) · [MalaCards](https://www.malacards.org/card/histiocytic_sarcoma)
- [ICD-10-CM C96.A — Histiocytic sarcoma](https://icdlist.com/icd-10/C96.A) · [icd10data C96\*](https://www.icd10data.com/ICD10CM/Codes/C00-D49/C81-C96/C96-) · [SEER ICD-O-3 site/histology validation list](https://seer.cancer.gov/icd-o-3/sitetype.icdo3.20220429.pdf) · [SEER heme/lymph tool](https://seer.cancer.gov/seertools/hemelymph/51f6cf59e3e27c3994bd5471/)
- [WHO 5th edition: Myeloid and Histiocytic/Dendritic Neoplasms — PMC9252913](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9252913/) · [Pathologic characteristics of histiocytic and dendritic cell neoplasms — PMC11076448](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11076448/) · [Mature B, T/NK, plasma cell and histiocytic/dendritic neoplasms: WHO vs ICC — PMC11232355](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11232355/)
- [Goyal et al. Consensus recommendations for malignant histiocytic neoplasms, Blood 2026;148(3):275–288 — PMID 41915766](https://pubmed.ncbi.nlm.nih.gov/41915766/) · [doi:10.1182/blood.2026033049](https://doi.org/10.1182/blood.2026033049) · [ASH page](https://ashpublications.org/blood/article/148/3/275/567492/Consensus-recommendations-for-malignant)
- [Egan et al. RAS-MAPK mutations in histiocytic sarcoma, Mod Pathol 2019;32:830–843 — PMID 30626916](https://pubmed.ncbi.nlm.nih.gov/30626916/) · [Nature](https://www.nature.com/articles/s41379-018-0200-x)
- [Genomic profiling of primary histiocytic sarcoma reveals two molecular subgroups, Haematologica 2020;105(4):951–960](https://haematologica.org/article/view/9331) · [editorial PMID 32238464](https://pubmed.ncbi.nlm.nih.gov/32238464/)
- [Egan et al. Mutational landscape of histiocytic sarcoma associated with lymphoid malignancy, Mod Pathol 2021;34:336–347](https://www.nature.com/articles/s41379-020-00673-x) · [PMC9161669](https://pmc.ncbi.nlm.nih.gov/articles/PMC9161669/)
- [Mayo/UAB: Malignant histiocytosis phenotypic spectrum, Mod Pathol 2023;36:100268](https://www.modernpathology.org/article/S0893-3952(23)00173-4/fulltext)
- [Massoth et al. Histiocytic and dendritic cell sarcomas share targetable alterations, The Oncologist 2021;26:e1263](https://academic.oup.com/oncolo/article/26/7/e1263/6510483) · [doi:10.1002/onco.13801](https://dx.doi.org/10.1002/onco.13801)
- [Kommalapati et al. Histiocytic sarcoma SEER population analysis, Blood 2018;131:265–268](https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes)
- [Histiocytic Sarcoma: Clinical Features and Outcomes at a Tertiary Cancer Center — PMC9271260](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/) · [Moffitt 25-year experience — PMC4276966](https://pmc.ncbi.nlm.nih.gov/articles/PMC4276966/) · [Case series — PMC11891036](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891036/) · [Front Oncol 2025 review](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1505737/xml)
- [Characterization and treatment outcomes of malignant histiocytoses, 141 cases, Blood Adv 2025;9(10):2530](https://ashpublications.org/bloodadvances/article/9/10/2530/535782/Characterization-and-treatment-outcomes-of)
- [Diamond et al. Efficacy of MEK inhibition in histiocytic neoplasms, Nature 2019 — PMID 30867592](https://pubmed.ncbi.nlm.nih.gov/30867592/) · [MSK FDA-approval release (28 Oct 2022)](https://www.mskcc.org/news-releases/fda-approves-oral-mek-inhibitor-cobimetinib-histiocytic-neoplasms-research-led-msk-cancer) · [ASCO Post](https://ascopost.com/issues/december-10-2022/fda-approves-oral-mek-inhibitor-cobimetinib-for-histiocytic-neoplasms/) · [ASH 2023 phase 2 report](https://ashpublications.org/blood/article/142/Supplement%201/1812/505051/Phase-2-Trial-of-Single-Agent-Cobimetinib-for)
- [RAF-independent MEK mutations respond to ERK inhibition, Cancer Cell 2025 — PMID 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/) · [PMC12616613](https://pmc.ncbi.nlm.nih.gov/articles/PMC12616613/) · [Cancer Discov highlight](https://aacrjournals.org/cancerdiscovery/article-abstract/16/1/OF1/771345/RAF-independent-MEK1-mutant-Histiocytoses-Respond?redirectedFrom=fulltext)
- [CSF1R inhibition for CBL-mutant histiocytic neoplasm, Leukemia 2023 — PMC10400417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/) · [Personalized medicine in histiocytic disorders, JCO PO 2025](https://ascopubs.org/doi/10.1200/PO-24-00471)
- [Trametinib near-CR with KRAS Q61H, JNCCN 2022;20(6)](https://doi.org/10.6004/jnccn.2022.7001) · [Trametinib in MAP2K1-mutant HS](https://www.researchgate.net/publication/325191894_Trametinib_in_Histiocytic_Sarcoma_with_an_Activating_MAP2K1_MEK1_Mutation) · [Trametinib+imatinib, Haematologica](https://haematologica.org/article/view/8337) · [MEK-inhibitor switch to cobimetinib, J Hematol](https://www.thejh.org/index.php/jh/article/view/1030/678)
- [Luvometinib phase 2 in histiocytic neoplasms, eClinicalMedicine 2025 — PMID 41035796 / PMC12481021](https://pmc.ncbi.nlm.nih.gov/articles/PMC12481021/)
- [Pembrolizumab durable response in HS — PMID 38098600 / PMC10718375](https://pmc.ncbi.nlm.nih.gov/articles/PMC10718375/) · [PD-L1 and ICI response in malignant histiocytic neoplasms, Leuk Lymphoma 2025](https://dx.doi.org/10.1080/10428194.2025.2561114) · [Pembrolizumab+GDP — PMC11366101](https://pmc.ncbi.nlm.nih.gov/articles/PMC11366101/) · [PD-L1-high pulmonary HS, Clin Respir J 2024](https://onlinelibrary.wiley.com/doi/10.1111/crj.13741) · [Combined immune-targeted treatment with FL, Int J Mol Sci 2024;25:7293](https://www.mdpi.com/1422-0067/25/13/7293)
- [Allogeneic HSCT for HS: systematic review, Transplant Cell Ther 2025](https://www.sciencedirect.com/science/article/abs/pii/S2666636725002908) · [ASH 2024 abstract](https://doi.org/10.1182/blood-2024-208929) · [Autologous SCT case + review — PMID 41580890 / PMC12853904](https://pmc.ncbi.nlm.nih.gov/articles/PMC12853904/) · [Durable response after allo-SCT, Hematol Rep 2026](https://doi.org/10.3390/hematolrep18010002)
- [NCCN Histiocytic Neoplasms v2.2021, JNCCN 19(11) — PMID 34781268](https://pubmed.ncbi.nlm.nih.gov/34781268/) · [guideline PDF](https://www.erdheim-chester.org/wp-content/uploads/2022/08/NCCN-Guidelines-for-Histiocytic-Neoplasms.pdf)
- Trials: [NCT02649972](https://clinicaltrials.gov/study/NCT02649972) · [NCT04079179](https://clinicaltrials.gov/study/NCT04079179) · [NCT04007848](https://clinicaltrials.gov/study/NCT04007848) · [NCT04437381](https://clinicaltrials.gov/study/NCT04437381)
- Clonal relationships: [FL+HS clonally related, Blood Cancer J 2025](https://www.nature.com/articles/s41408-025-01335-4) · [KRAS in secondary malignant histiocytosis from FL — PMC6190545](https://pmc.ncbi.nlm.nih.gov/articles/PMC6190545/) · [HS with IGH::BCL2 from FL, AJCP 2025](https://academic.oup.com/ajcp/article/164/Supplement_1/aqaf121.281/8321081) · [CCND1-rearranged HS from MCL, AJCP 2022](https://doi.org/10.1093/ajcp/aqac087) · [CLL/SLL-related HDS, Mod Pathol](https://www.modernpathology.org/article/S0893-3952(22)02794-6/fulltext) · [B-ALL → HS, Blood 2016;128:2475](https://ashpublications.org/blood/article/128/20/2475/35616/Histiocytic-sarcoma-secondary-neoplasm-or) · [B-ALL transdifferentiation after immunotherapy, Am J Hematol](https://onlinelibrary.wiley.com/doi/full/10.1002/ajh.26983) · [IGH-MYC/IGK after B-LBL, AJCP](https://dx.doi.org/10.1093/ajcp/aqz056) · [HS 33 years after B-ALL — PMC13472141](https://pmc.ncbi.nlm.nih.gov/articles/PMC13472141/) · [Selumetinib in B-ALL-derived HS — PMID 41798885](https://pubmed.ncbi.nlm.nih.gov/41798885/) · [Myeloma → HS — PMC12270463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12270463/) · [HS in NLPHL background — PMC12310312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12310312/) · [BRAF-mutated secondary HDS, BRAF/MEK response — PMID 42264920](https://pubmed.ncbi.nlm.nih.gov/42264920/)
- Cell of origin / epigenetics: [Driver mutations point to multipotent progenitor origin, Blood Neoplasia 2025 — PMC12067900](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12067900/) · [Histiocytosis genomics review, J Pathol 2026 — PMC13432202](https://pmc.ncbi.nlm.nih.gov/articles/PMC13432202/) · [Histiocytic disorders, Nat Rev Dis Primers](https://www.nature.com/articles/s41572-021-00307-9) · [let-7–BCL2L1/BCL2 methylation axis — PMC11794134](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11794134/) · [ASH 2023 epigenetic landscape](https://ashpublications.org/blood/article/142/Supplement%201/1161/505458/Deciphering-the-Epigenetic-Landscape-in) · [DNA-methylation classification of haematolymphoid neoplasms, Blood Adv](https://doi.org/10.1182/bloodadvances.2024015275)
- CNS/diagnostics/imaging: [Primary CNS HS with MIGA2::BRAF and methylation profiling, JNEN 2024 — PMC11413427](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/) · [CNS HS vs glioblastoma, methylation analysis — PMC12279446](https://pmc.ncbi.nlm.nih.gov/articles/PMC12279446/) · [Intramedullary HS, Diagnostics 2026](https://doi.org/10.3390/diagnostics16162623) · [Multisystem HS on FDG PET/CT — PMID 34330800](https://pubmed.ncbi.nlm.nih.gov/34330800/) · [JNMT 49:358](https://tech.snmjournals.org/content/49/4/358) · [cfDNA BRAF V600E in histiocytic disorders — PMID 25324352 / PMC5705028](https://pmc.ncbi.nlm.nih.gov/articles/PMC5705028/) · [Plasma cfDNA in adult histiocytic neoplasms, ASH 2023](https://ashpublications.org/blood/article/142/Supplement%201/6332/506171/Molecular-Findings-on-Plasma-Cell-Free-DNA)
- Pathology/differential: [HS: five cases incl. CD163, Mod Pathol](https://www.nature.com/articles/3800346) · [HS review & transformation from B-cell lymphoma, Arch Pathol Lab Med 2018;142:1322](https://meridian.allenpress.com/aplm/article/142/11/1322/103148/Histiocytic-Sarcoma-Review-Discussion-of) · [Arch Pathol Lab Med 2020;144:650](https://meridian.allenpress.com/aplm/article/144/5/650/427448/Histiocytic-Sarcoma) · [Pathology Outlines](https://www.pathologyoutlines.com/topic/lymphnodeshistiocyticsarcoma.html) · [Hornick et al. extranodal HS, Am J Surg Pathol 2004;28:1133 (abstract via UpToDate)](https://www.uptodate.com/contents/histiocytic-sarcoma/abstract/2) · [FNA of HS — PMC4349012](https://pmc.ncbi.nlm.nih.gov/articles/PMC4349012/) · [Spindle-cell head/neck HS, Diagn Pathol 2007;2:7](https://diagnosticpathology.biomedcentral.com/articles/10.1186/1746-1596-2-7)
- Clinical sites/complications: [Gastric HS — PMC13478121](https://pmc.ncbi.nlm.nih.gov/articles/PMC13478121/) · [Oral HS — PMID 39048487](https://pubmed.ncbi.nlm.nih.gov/39048487) · [Breast — PMC11149727](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11149727/) · [Pulmonary with CNS metastasis — PMC12920180](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12920180/) · [Splenic HS with HLH — PMC9124500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/) · [HS from FL mimicking HLH — PMC7481156](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7481156/) · [Marrow infiltration — PMC6170302](https://pmc.ncbi.nlm.nih.gov/articles/PMC6170302/) · [Enteric necrosis from tumour embolism — PMC11452572](https://pmc.ncbi.nlm.nih.gov/articles/PMC11452572/) · [Bladder HS — PMC7888511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7888511/) · [Hepatic HS — PMID 42405293](https://pubmed.ncbi.nlm.nih.gov/42405293/) · [Cutaneous HS — PMC12400779](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12400779/) · [Vertebral HS — PMID 35884764](https://pubmed.ncbi.nlm.nih.gov/35884764/) · [CNS HS craniectomy + RT — PMC9162887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9162887/) · [Challenging course, dismal outcome, Diagnostics 2021 — PMC7918796](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7918796/)
- Secondary associations: [Mediastinal GCT + splenic HS — PMID 16086090](https://pubmed.ncbi.nlm.nih.gov/16086090/) · [Malignant histiocytosis with mediastinal GCT — PMID 36051154 / PMC9297408](https://pmc.ncbi.nlm.nih.gov/articles/PMC9297408/) · [HS after chemotherapy for mediastinal GCT — PMID 33786289](https://pubmed.ncbi.nlm.nih.gov/33786289/) · [Disseminated HS with haemophagocytic syndrome and mediastinal GCT — PMID 18987551](https://pubmed.ncbi.nlm.nih.gov/18987551/) · [Thalidomide + RIC allo-PBSCT — PMC4718299](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4718299/) · [HS secondary to GIST — PMC9882698](https://pmc.ncbi.nlm.nih.gov/articles/PMC9882698/) · [HS in renal transplant recipients — PMID 37784161 / PMC10546704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10546704/) · [Kidney transplant case — PMC5066022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5066022/) · [PMC4544561](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4544561/) · [NF1 mutation + TUBB3 amplification, gastric HS](https://link.springer.com/article/10.1007/s00795-024-00393-0)
- QoL/survivorship: [Anxiety and depression in histiocytic neoplasms, Blood Adv 2025;9(6):1376](https://ashpublications.org/bloodadvances/article/9/6/1376/534302/Anxiety-and-depression-in-patients-with) · [Survivorship issues — PMC10481619](https://pmc.ncbi.nlm.nih.gov/articles/PMC10481619) · [Histiocytic Disorder Survivor Study](https://bloodcancerunited.org/research/award/patient-reported-outcomes-and-survivorship-histiocytic-neoplasms)
- Pediatric: [Pediatric primary HS case + review — PMID 40486162 / PMC12144458](https://pmc.ncbi.nlm.nih.gov/articles/PMC12144458/) · [Successful treatment of HS in childhood — PMID 41835761](https://pubmed.ncbi.nlm.nih.gov/41835761/) · [Maxilla/mandible pediatric HS — PMC5124769](https://pmc.ncbi.nlm.nih.gov/articles/PMC5124769/) · [Extranodal HS in a child with ALL — PMID 29676378](https://pubmed.ncbi.nlm.nih.gov/29676378)
- Veterinary/comparative: [OMIA:000620-9615 Histiocytosis, malignant (dog)](https://omia.org/OMIA000620/9615/) · [MTAP-CDKN2A locus GWAS, CEBP 2012;21:1019](https://cebp.aacrjournals.org/content/21/7/1019) · [Common predisposing loci in four dog breeds — PMC8016107](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8016107/) · [PTPN11/KRAS in canine HS — PMC6678586](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6678586/) · [PTPN11 in canine and human disseminated HS](https://www.researchgate.net/publication/340167279_PTPN11_mutations_in_canine_and_human_disseminated_histiocytic_sarcoma) · [Canine HS transcriptome + AURK/trametinib synergy, Cancers 2025 — PMC11940154](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940154/) · [Canine WES/transcriptome ERK+Akt, Sci Rep 2023 — PMC10212919](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10212919/) · [CCNU in canine HS — PMID 17338159](https://pubmed.ncbi.nlm.nih.gov/17338159/) · [Lomustine+doxorubicin protocol](https://www.researchgate.net/publication/274402918_Evaluation_of_a_combination_chemotherapy_protocol_including_lomustine_and_doxorubicin_in_canine_histiocytic_sarcoma) · [BMD epidemiology/pathology/genetics — PMID 19531730](https://pubmed.ncbi.nlm.nih.gov/19531730/) · [BMD risk factors, JVIM](https://doi.org/10.1111/jvim.13964) · [BMD vs Flat-Coated Retriever — PMC9504151](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9504151/) · [Canine histiocytic malignancies — PMC5644619](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5644619/) · [Breed predispositions — PMC3658424](https://pmc.ncbi.nlm.nih.gov/articles/PMC3658424/) · [Degu — PMID 38556322](https://pmc.ncbi.nlm.nih.gov/articles/PMC11144536/) · [Amami spiny rat — PMC11442397](https://pmc.ncbi.nlm.nih.gov/articles/PMC11442397/)
- Models/cell lines: [Janke & Rehg, Vet Pathol 2023;60:443](https://journals.sagepub.com/doi/10.1177/03009858231166658) · [Sleeping Beauty screen, PLoS ONE 2014;9:e97280](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0097280) · [PMC4020815](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4020815/) · [Induction in mouse skeletal muscle — PMC3432091](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3432091/) · [SHIP1 model — PMC13627489](https://pmc.ncbi.nlm.nih.gov/articles/PMC13627489) · [Aging mice/GEM pathobiology](https://journals.sagepub.com/doi/10.1177/0300985811430696) · [CD-1 epididymal HS — PMC11219191](https://pmc.ncbi.nlm.nih.gov/articles/PMC11219191/) · [C57BL/6 concurrent B-LBL + HS — PMC12906819](https://pmc.ncbi.nlm.nih.gov/articles/PMC12906819/) · [Novel canine HS cell line — PMC5831740](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5831740/) · Cellosaurus: [U-937 CVCL_0007](https://www.cellosaurus.org/CVCL_0007), [CHS-2 CVCL_L315](https://www.cellosaurus.org/CVCL_L315), [PWC-HS01 CVCL_IU62](https://www.cellosaurus.org/CVCL_IU62), [M5076 CVCL_3997](https://www.cellosaurus.org/CVCL_3997), [HS-MM CVCL_W472](https://www.cellosaurus.org/CVCL_W472) · [U-DCS dendritic sarcoma line — PMC7718904](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7718904/) · [J774A.1 EV study](https://doi.org/10.3390/ijms27114949)
- Ontology lookups: [HP:0002716 Lymphadenopathy (Monarch)](https://monarchinitiative.org/HP:0002716) · [CL:0000235 macrophage (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/cl/entities/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0000235) · [CL:0000235 CellGuide](https://cellxgene.cziscience.com/cellguide/CL:0000235) · [UBERON:0000029 lymph node](https://m.bioportal.bioontology.org/ontologies/OBI_BCGO?conceptid=http://purl.obolibrary.org/obo/UBERON_0000029&p=classes) · [GO:0000165 MAPK cascade (AmiGO)](https://amigo.geneontology.org/amigo/term/GO:0000165) · [NCIT C77908 trametinib (EVS Explore)](https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C77908) · [NCIT C69145 MEK inhibitor](https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C69145)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 115 |
| Resolved | 114 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 16 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 114 |
| On topic | 56 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMC:PMC11452572` (11 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

15 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC11076448` *(abstract only)*: "in recognition of their derivation from common myeloid progenitors that give rise to cells of the monocytic/histiocytic/dendritic lineages"
  - closest text in source: "There are frequent genomic alterations in these neoplasms, especially in the mitogen-activated protein kinase pathway, including BRAF (notably BRAF V600E), MAP2K1, KRAS, and NRAS mutations, and ALK gene translocation.This review aims to offer a comprehensive and updated overview of histiocytic and dendritic cell neoplasms, focusing on their ontogeny, morphological aspects, immunophenotypic profiles, and molecular genetics"
- `PMID:41915766` *(abstract only)*: "malignant histiocytic neoplasm, histiocytic type"
  - closest text in source: "Malignant histiocytic neoplasms (MHNs) are rare tumors derived from the mononuclear phagocyte system (MPS), encompassing histiocytic sarcoma, Langerhans cell sarcoma, interdigitating dendritic cell sarcoma, and other high-grade MPS lineage tumors"
- `PMID:16086090` *(abstract only)*: "hematologic malignancy and MGCTs aris[ing] from a common progenitor cell"
  - closest text in source: "We present an unusual association of mediastinal germ cell tumor containing seminoma and angiosarcoma components and splenic histiocytic sarcoma"
- `PMID:36051154` *(abstract only)*: "hematologic malignancy and MGCTs aris[ing] from a common progenitor cell"
  - closest text in source: "BACKGROUND: Germ cell tumors (GCTs) account for 2% of human malignancies but are the most common malignant tumors among males aged 15-35"
- `PMID:33786289` *(abstract only)*: "hematologic malignancy and MGCTs aris[ing] from a common progenitor cell"
  - closest text in source: "We herein report on a case of histiocytic sarcoma following combination chemotherapy for a primary mediastinal germ cell tumor in a 26-year-old Asian man who visited the General Medicine Department of a hospital with complaints of cough and high fever"
- `PMID:18987551` *(abstract only)*: "hematologic malignancy and MGCTs aris[ing] from a common progenitor cell"
  - closest text in source: "We describe a case of a 24-year-old man with a large anterior mediastinal mass showing a nonseminomatous germ cell tumor then subsequently developed hemophagocytic syndrome involving the bone marrow and liver"
- `PMC:PMC12429796` *(abstract only)*: "aggressive clinical course with a limited response to therapy and a high mortality rate"
  - closest text in source: "Recent studies have demonstrated a high rate of PD-L1 expression, suggesting a potential therapeutic target"
- `PMID:41135521` *(abstract only)*: "common in patients with systemic histiocytic neoplasms, drive disease in a conditional knock-in mouse model, and associate with progression on FDA-approved MEK inhibitors"
  - closest text in source: "Here, aided by a prospective registry of patients with histiocytoses (NCT03329274), we identify that MEK1/2 mutations which constitutively activate MEK independently of RAF are associated with worse progression-free survival with MEK1/2 inhibition as compared to patients with other MEK1/2 mutational classes"
- `PMC:PMC12616613` *(abstract only)*: "common in patients with systemic histiocytic neoplasms, drive disease in a conditional knock-in mouse model, and associate with progression on FDA-approved MEK inhibitors"
  - closest text in source: "Here, aided by a prospective registry of patients with histiocytoses (NCT03329274), we identify that MEK1/2 mutations which constitutively activate MEK independently of RAF are associated with worse progression-free survival with MEK1/2 inhibition as compared to patients with other MEK1/2 mutational classes"
- `PMC:PMC6190545` *(abstract only)*: "suggesting this mutation preceded transdifferentiation of the FL to HS"
  - closest text in source: "CONCLUSIONS: This report highlights genetic alterations, in particular an acquired somatic KRAS mutation, that may occur during transdifferentiation, with additional significance of KRAS mutation as a possible therapeutic target in cases which otherwise would have limited treatment options."
- `PMC:PMC10546704` *(abstract only)*: "the first report of HS in a solid organ recipient without evidence of EBV infection"
  - closest text in source: "EBV was positive in 2 cases and negative in one of them"
- `PMID:30867592`: "a notable dependence on MAPK signalling and are consequently responsive to MEK inhibition"
  - closest text in source: "Collectively, these data demonstrate that histiocytic neoplasms are characterized by a notable dependence on MAPK signalling-and that they are consequently responsive to MEK inhibition"
- `PMID:40486162` *(abstract only)*: "more commonly reported in adults, typically in the sixth decade of life, [while] pediatric cases are distinctly uncommon"
  - closest text in source: "This case highlights the rarity of soft tissue histiocytic sarcoma in pediatric patients and the importance of multimodal treatment to achieve long-term remission."
- `PMC:PMC12144458` *(abstract only)*: "more commonly reported in adults, typically in the sixth decade of life, [while] pediatric cases are distinctly uncommon"
  - closest text in source: "This case highlights the rarity of soft tissue histiocytic sarcoma in pediatric patients and the importance of multimodal treatment to achieve long-term remission."
- `PMID:41915766` *(abstract only)*: "among patients with abnormal peripheral blood counts, a bone marrow aspirate/biopsy is warranted to rule out a concomitant hematopoietic malignancy"
  - closest text in source: "Key recommendations include the adoption of a unified MHN designation, use of a minimum immunophenotypic panel, integration of broad molecular profiling, and the documentation of previous hematopoietic malignancy"
- `PMC:PMC13627489` *(abstract only)*: "in the absence of engineered oncogenic drivers"
  - closest text in source: "T cell specific ablation of SHIP1 expression in CD4CreSHIP1flox/flox mice also results in Crohn's disease-like ileitis, but less severe than in their germline SHIP1-/- counterparts due to the absence of a SHIP1 deficient neutrophil compartment"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1177/0300985811430696` (3 mentions) - Pathobiology of Aging Mice and GEM
  - shared terms: disease

Weighed against this report's own most characteristic terms: `histiocytic`, `cell`, `disease`, `neoplasm`, `mutation`, `blood`, `sci`, `sarcoma`, `response`, `patient`, `int`, `mol`, `secondary`, `pathol`, `via`, `primary`, `braf`, `gene`, `lesion`, `extraction`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:32238464`: "was comprised primarily of cases with prototypic RAS/MAPK pathway activating mutations involving KRAS, NRAS, BRAF and MAP2K1"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.3324/haematol.2019.230375`: "was comprised primarily of cases with prototypic RAS/MAPK pathway activating mutations involving KRAS, NRAS, BRAF and MAP2K1"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`.

15 of 17 terms resolved to a current term; the rest could not be looked up either way.