---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-21T00:48:11.370908'
end_time: '2026-11-21T01:09:28.454068'
duration_seconds: 1277.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pediatric Cystic Nephroma
  mondo_id: MONDO:0002385
  category: Neoplasm. Scope rules for this report - the childhood, DICER1-associated
    cystic nephroma only; name the adult cystic nephroma and cystic partially differentiated
    nephroblastoma only to say how they differ; state any NF1 or NF2 change at gene
    level only; do not name or discuss chromosome-arm changes (in particular 1p36,
    11q or 17q) or chromothripsis; add nothing on ALK.
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: benign multilocular cystic nephroma; cystic nephroma
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
  web_search_requests: 20
  num_turns: 118
  total_cost_usd: 7.518967750000002
  session_id: 3785b107-ec78-44b5-8a6c-7693f5c6d2d7
  stop_reason: end_turn
  tool_calls: 117
  retrieval_calls: 117
  assistant_text_blocks: 1
citation_count: 58
reference_validation:
  total_references: 74
  verified: 74
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 1
  quotes_unsupported: 2
  unsupported_quote_references:
  - DOI:10.3389/fonc.2026.1799009
  - PMID:33673661
  relevance_assessed: 74
  on_topic: 47
  off_topic: 1
  off_topic_references:
  - PMID:26925182
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 51
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0002385
    reported_labels:
    - benign cystic nephroma
    - OLS4
    ontology_label: benign cystic nephroma
  - term_id: MONDO:0100216
    reported_labels:
    - OLS4
    ontology_label: DICER1-related tumor predisposition
  - term_id: DOID:2673
    reported_labels:
    - DOID
    ontology_label: adult cystic nephroma
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  - EXT_ID
  - OMIM
  - OMIA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pediatric Cystic Nephroma
- **MONDO ID:** MONDO:0002385 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** benign multilocular cystic nephroma; cystic nephroma
- **Category:** Neoplasm. Scope rules for this report - the childhood, DICER1-associated cystic nephroma only; name the adult cystic nephroma and cystic partially differentiated nephroblastoma only to say how they differ; state any NF1 or NF2 change at gene level only; do not name or discuss chromosome-arm changes (in particular 1p36, 11q or 17q) or chromothripsis; add nothing on ALK.

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pediatric Cystic Nephroma** covering all of the
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

**Interpretation note (stated up front, as instructed).** The template gives MONDO:0002385 with no causal gene recorded. I retrieved MONDO:0002385 and it resolves to the generic term **"benign cystic nephroma"** (definition covering cystic nephroma of any age), not a pediatric‑specific class — no pediatric‑specific MONDO term exists (OLS4 MONDO search returned only MONDO:0002385, plus MONDO:0030604 cystic partially differentiated nephroblastoma and MONDO:0100216 DICER1‑related tumor predisposition). Per the scope rules supplied, this report covers **only childhood (pediatric) DICER1‑associated cystic nephroma**; adult cystic nephroma/MEST and cystic partially differentiated nephroblastoma (CPDN) appear only where needed to state how they differ. The causal gene is **DICER1** (HGNC:17098, 14q32.13, OMIM 606241) — named in §1 and §4 below. Per the scope rules, NF1/NF2 findings are stated at gene level only; chromosome‑arm–level changes and chromothripsis are excluded; ALK is not discussed.

---

# Pediatric Cystic Nephroma (DICER1‑Associated) — Comprehensive Disease Characteristics Report

---

## 1. Disease Information

### Overview

Pediatric cystic nephroma (PCN) is a **benign, well‑circumscribed, multiloculated cystic kidney neoplasm of infancy and early childhood** that is, in the large majority of cases, the renal manifestation of **DICER1‑related tumor predisposition** (DICER1 syndrome). GeneReviews describes it as "a benign neoplasm that presents as a multicystic parenchymal kidney tumor" and states it "represents the most common kidney manifestation in individuals with DICER1" ([GeneReviews, DICER1‑Related Tumor Predisposition, NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)).

The 2025 review by Capozzi et al. states: *"It is estimated that 90% of pediatric cystic nephroma harbor DICER1 mutations, two-thirds of them being germline mutations"* (Capozzi A, Jansen FA, Smetsers SE, Bakhuizen JJ, Hiemcke‑Jiwa LS, Kranendonk MEG, Flucke U, Alaggio R, de Krijger RR. *Pediatr Dev Pathol.* 2025;28(4):231–243. **PMID 40231379**; DOI 10.1177/10935266251329752).

A pediatric cystic mass of this type is therefore a **sentinel lesion**: the International PPB/DICER1 Registry notes that "Cystic nephroma (CN) is a benign cystic tumor of the kidney" presenting as "multi-cystic lesions arising from one or both kidneys," and that "Risk for development of CN is highest in the first 4 years of life" ([PPB Registry, Renal Tumors](https://www.ppbregistry.org/renal-tumors/)).

### Key identifiers (all retrieved this session)

| Resource | Identifier | Source |
|---|---|---|
| MONDO | **MONDO:0002385** "benign cystic nephroma" | [OLS4/MONDO](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0002385) |
| DOID | DOID:2673 | OLS4/MONDO xref |
| ICD‑O | **8959/0** (morphology; "/0" = benign) | OLS4/MONDO xref |
| NCIT | C7504 | OLS4/MONDO xref |
| UMLS | C1266138 | OLS4/MONDO xref |
| MedGen | 220422 | OLS4/MONDO xref |
| SNOMED CT | 128757006 | [MedGen 220422](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=medgen&id=220422) |
| HPO | **HP:0034836** "Cystic nephroma" | MedGen 220422; [HPO API](https://ontology.jax.org/api/hp/terms/HP:0034836) |
| GTR | GTRT000050538, AN1481031 | MedGen 220422 |
| ICD‑10‑CM (topography, benign kidney neoplasm) | **D30.00 / D30.01 / D30.02** (unspecified / right / left kidney) | [NLM Clinical Table Search Service, ICD‑10‑CM](https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=D30) |
| MeSH | **No dedicated descriptor.** PubMed MeSH search for "cystic nephroma" returns Count = 0; "nephroma" maps to Wilms Tumor / text word | [E‑utilities esearch db=mesh](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=mesh&term=cystic+nephroma) |
| ICD‑11 | **Not retrieved** — the WHO ICD‑11 browser could not be read by the fetch tool. Not asserted here. | — |

**Associated syndrome entry (the genetic disease):** MONDO:0100216 "DICER1‑related tumor predisposition"; Orphanet **ORPHA:284343**; OMIM **601200** (syndrome) and **606241** (DICER1 gene); NCIT C123317; UMLS C3839822; MedGen 825667; SNOMED CT 702411003; DOID:0081063 ([OLS4/MONDO](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0100216); [MedGen 825667](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=medgen&id=825667)).

MONDO:0100216 is defined as: *"Pathogenic germline variation in DICER1 confers an autosomal dominant predisposition to tumor formation at multiple primary sites, including pleuropulmonary blastoma, pulmonary cysts, thyroid gland neoplasia, ovarian tumors, and cystic nephroma."*

### Synonyms

From MONDO:0002385: *benign cystic nephroma; benign multilocular cystic nephroma; cystic nephroma*. From HP:0034836: *Benign multilocular cystic nephroma; Multicystic nephroma; Multilocular cystic renal tumor/tumour; Polycystic nephroblastoma*. MedGen 220422 additionally lists *Cystic nephroma* and *Adult Cystic Nephroma* (the latter is a **different entity** in current practice — see §10). Clinical literature uses **"pediatric cystic nephroma" (PCN/pCN)** and "multilocular cystic nephroma (MLCN)".

### Provenance of the information in this report

A **mixture**, dominated by individual‑patient data aggregated into registries and systematic literature reviews rather than EHR‑derived population data:
- **Individual‑patient, registry‑aggregated:** International PPB/DICER1 Registry (713 germline carriers; 62 cystic nephromas) — Schultz et al. 2024, **PMID 39400264**; ASK series, Schoettler et al. 2024, **PMID 38807260**.
- **Individual‑patient, literature‑aggregated:** van Peer et al. 2021 narrative review of 167 CN patients, **PMID 33673661**.
- **Pathology case series:** Doros et al. 2014 (**PMID 24481001**); Li et al. 2017 (**PMID 28177962**).
- **Disease‑level/aggregated resources:** MONDO, HPO, MedGen, Orphanet, ClinGen, GeneReviews.
- **Genome‑first EHR cohorts (for DICER1 carrier prevalence/penetrance, not for CN specifically):** Geisinger MyCode (Mirshahi et al., *JAMA Netw Open* 2021) and UK Biobank.

---

## 2. Etiology

### 2.1 Disease causal factors

**Primary cause: biallelic inactivation/alteration of DICER1 in a renal progenitor cell**, usually as a germline loss‑of‑function (LOF) "first hit" plus a somatic RNase IIIb‑domain missense "second hit."

- Doros et al. concluded: *"DICER1 mutations are the major genetic event in the development of cystic nephroma"* (Doros LA, Rossi CT, Yang J, Field A, Williams GM, Messinger Y, Cajaiba MM, Perlman EJ, Schultz KA, Cathro HP, Legallo RD, LaFortune KA, Chikwava KR, Faria P, Geller JI, Dome JS, Mullen EA, Gratias EJ, Dehner LP, Hill DA. *Mod Pathol.* 2014;27:1267–1280. **PMID 24481001**; DOI 10.1038/modpathol.2013.242 — abstract retrieved via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24481001&resultType=core&format=json)).
- Li et al. (verbatim abstract): *"86% of pediatric cases demonstrated DICER1 mutations, whereas only 1 of 10 adult cases demonstrated a DICER1 mutation"* (Li Y, Pawel BR, Hill DA, Epstein JI, Argani P. *Am J Surg Pathol.* 2017;41(4):472–481. **PMID 28177962**; DOI 10.1097/PAS.0000000000000816 — [abstract](https://pure.johnshopkins.edu/en/publications/pediatric-cystic-nephroma-is-morphologically-immunohistochemicall/)).
- van Peer et al. (verbatim): *"Unlike CPDN, CN was strongly associated with somatic (n = 27/29) and germline (n = 12/12) DICER1-mutations"*; and *"DICER1 mutations (germline and/or somatic) were identified in 33/35 tested cases"* (van Peer SE, Pleijte CJH, de Krijger RR, Jongmans MCJ, Kuiper RP, Lilien MR, van Grotel M, Graf N, van den Heuvel‑Eibrink MM, Hol JA. *Cancers (Basel).* 2021;13(5):997. **PMID 33673661**; DOI 10.3390/cancers13050997).
- Familial proof of causality: *"DICER1 mutations cause familial CN and may be implicated in bilateral CN"* (Bahubeshi A, Bal N, Rio Frio T, Hamel N, Pouchet C, Yilmaz A, Bouron‑Dal Soglio D, Williams GM, Tischkowitz M, Priest JR, Foulkes WD. *J Med Genet.* 2010;47(12):863–866. **PMID 21036787**; DOI 10.1136/jmg.2010.081216).
- Direct two‑hit demonstration in a CN: *"Additional in trans DICER1 missense somatic mutations in the IIIb DICER1 domain were found both in the cystic nephroma and in the rhabdomyosarcoma"* (Fernández‑Martínez L, et al. *BMC Cancer.* 2017;17(1):146. **PMID 28222777**; DOI 10.1186/s12885-017-3136-5).

**No infectious, toxic, or mechanistic non‑genetic cause has been identified** in any source retrieved.

### 2.2 Risk factors

**Genetic**
- **Germline heterozygous DICER1 LOF pathogenic/likely‑pathogenic variant** — the dominant risk factor. ClinGen classifies DICER1–DICER1‑related tumor predisposition (MONDO:0100216) as **"Definitive"** gene–disease validity (Hereditary Cancer GCEP, 07/05/2023), with **haploinsufficiency score 3** ("Sufficient Evidence for Haploinsufficiency") and triplosensitivity score 0 ([ClinGen, HGNC:17098](https://search.clinicalgenome.org/kb/genes/HGNC:17098)).
- **Somatic mosaicism for an RNase IIIb hotspot variant** is a distinct, *higher*-risk genetic state for cystic renal disease. Brenneman et al.: *"Mosaic RNase IIIb domain hotspot missense mutations defines a special category of DICER1 syndrome patients, clinically distinguished from those with germline or mosaic LOF mutations by earlier onsets and numerous discrete foci of neoplastic disease involving multiple syndromic organ sites,"* and *"All presented with multiple cysts of the lungs and/or kidneys."* In their cohort, 6 of 7 mosaic‑hotspot patients had kidney cysts or cystic nephroma vs 12 of 90 germline‑LOF patients (Brenneman M, Field A, Yang J, et al. *F1000Res.* 2015;4:214 (v2 2018). **PMID 26925222**; DOI 10.12688/f1000research.6746.2).
- **Family history** of PPB, cystic nephroma, Sertoli‑Leydig cell tumor, multinodular goiter, or cervical embryonal rhabdomyosarcoma.
- No **susceptibility loci or modifier genes** for cystic nephroma specifically were identified in any retrieved source (no GWAS exists for this rare lesion).

**Demographic / environmental**
- **Young age** is the strongest non‑genetic correlate: GeneReviews — *"Pediatric CN is most common in children younger than age four years, although DICER1-associated pediatric CN has also been reported in older children and adolescents"*; Registry data — *"The median age at diagnosis of CN was 2.0 years (range: 4 months–15.3 years) with 90% occurring by 5 years of age"* (Schultz KAP, Nelson AT, Mallinger PHR, et al. *Clin Cancer Res.* 2024;30(24):5681–5692. **PMID 39400264**; DOI 10.1158/1078-0432.CCR-24-1532).
- **Male sex (modest excess):** van Peer et al. reported of 167 CN patients *"93 were male and 72 were female (for two patients, sex was not specified)"* (~1.3:1). Li et al.'s pathology series of 7 pediatric CN had male:female = 6:1.
- **No toxin, radiation, pollution, occupational, dietary, or lifestyle risk factor** was identified for pediatric cystic nephroma in any retrieved source. This is expected for an embryonal/developmental neoplasm of infancy.

### 2.3 Protective factors

**None identified.** No protective germline variants, modifier alleles, dietary, or lifestyle exposures were reported in any retrieved source. gnomAD‑based protective allele analyses do not exist for this phenotype. The only risk‑reducing intervention documented is **imaging surveillance** (secondary prevention — §13), which does not reduce incidence but changes the stage/extent at detection: *"The goal of renal screening is early detection to preserve renal function through less extensive surgery, especially in cases of bilateral disease, and to prevent progression to ASK"* (Schultz et al. 2024, PMID 39400264).

### 2.4 Gene–environment interactions

**No gene–environment interaction has been reported** for pediatric cystic nephroma in CTD, PubMed, or any source retrieved. The only interaction of mechanistic relevance is **gene × developmental timing** — an endogenous, not environmental, variable. Brenneman et al. proposed: *"acquisition of a neomorphic RNase IIIb domain mutation is the rate limiting event in DICER1-associated tumorigenesis, and that distinct clinical phenotypes associated with mutational categories reflect the temporal order in which LOF and RNase IIIb domain mutations are acquired during development"* (PMID 26925222). Under this model the *window of nephrogenesis* — not an external exposure — determines whether a renal cystic lesion forms.

---

## 3. Phenotypes

### 3.1 Core renal phenotype

| Phenotype | HPO term (verified) | Type | Onset | Severity | Progression | Frequency |
|---|---|---|---|---|---|---|
| Cystic nephroma (multilocular cystic renal neoplasm) | **HP:0034836** | Physical manifestation / neoplasm | Infancy–early childhood; median **2.0 y**, 90% by 5 y (PMID 39400264); range prenatal–16 y (PMID 33673661) | Moderate (large mass, nephron loss) but **benign** | Slowly enlarging; stable after complete resection | **≤10%** of DICER1 carriers (GeneReviews); 62/713 registry carriers ≈ 8.7% (PMID 39400264) |
| Palpable abdominal/flank mass | **HP:0031500** (Abdominal mass) | Clinical sign | At diagnosis | Variable | Progressive until resection | *"palpable abdominal mass was, when documented, the most frequently reported presenting symptom (62/88, 70%)"* (PMID 33673661) |
| Multiple renal cysts / renal cyst | **HP:0005562**, **HP:0000107** | Imaging/physical | Infancy | Mild–moderate | Variable | Characteristic radiologic appearance; multiple discrete foci especially in mosaic‑hotspot carriers (PMID 26925222) |
| Hypertension | **HP:0000822** | Clinical sign | Infancy–childhood | Can be severe (hypertensive urgency) | Resolves after nephrectomy | **Uncommon.** GeneReviews: "Hematuria, hypertension, and urinary tract infection are uncommon presentations." Documented case: 12‑month‑old with asymptomatic hypertensive urgency, BP controlled orally and *"resolution following left nephrectomy"* (Brown EA, Subramaniam A, Tumin D, Okolo FC, Cook C, Beng‑Ongey H. *Pediatr Nephrol.* 2026. **PMID 42704439**; DOI 10.1007/s00467-026-07501-5) |
| Hematuria | **HP:0000790** | Laboratory/clinical | Childhood | Mild | Episodic | Uncommon (GeneReviews); listed among presenting signs by the PPB Registry ("flank pain or blood in the urine") |
| Abdominal/flank pain | (HPO ID not verified this session) | Symptom | Childhood | Mild–moderate | Variable | PPB Registry: "The most common presenting sign/symptoms include an abdominal mass or abdominal pain" |
| Urinary tract infection | (HPO ID not verified) | Clinical | Childhood | Mild | Episodic | Uncommon (GeneReviews) |

**Laboratory abnormalities:** No diagnostic serum or urine biomarker exists for pediatric cystic nephroma. No LOINC‑coded analyte is specific to it; routine urinalysis may show hematuria (HP:0000790). This is a genuine gap, not an omission.

**Behavioral phenotypes:** None. Pediatric cystic nephroma has no neurobehavioral component (no DSM/RDoC relevance).

### 3.2 Syndromic (extrarenal) phenotypes in the same patients

Because ~2/3 of PCN cases are germline DICER1‑driven, the clinically relevant phenotype set is the DICER1 spectrum. Registry frequencies among **713 germline P/LP carriers** (PMID 39400264):

| Phenotype | HPO (where verified) | n | Median age at diagnosis |
|---|---|---|---|
| Pleuropulmonary blastoma, all types | **HP:0100528** | 267 | Type I 8 mo; Type Ir 2.4 y; Type II 2.8 y; Type III 3.5 y |
| Ovarian Sertoli‑Leydig cell tumor | — | 103 | 14 y (13% <8 y; 4% <4 y) |
| **Cystic nephroma** | **HP:0034836** | **62** | **2.0 y** |
| Thyroid carcinoma | — | 41 | 13 y |
| Simple renal cysts | **HP:0012581** | 32/286 (11%) | 27 y |
| Embryonal rhabdomyosarcoma | **HP:0002859** | 23 | 11 y |
| CNS tumors | — | 16 | 10 y |
| Nasal chondromesenchymal hamartoma | — | 15 | 10 y |
| **DICER1‑associated Wilms tumor** | **HP:0002667** | 7 | 4.2 y |
| Ciliary body medulloepithelioma | — | 7 | 7 y |
| **Anaplastic sarcoma of kidney (ASK)** | **HP:0009726** (renal neoplasm, nearest verified term) | 4 | ages 1, 6, 9, 23 y |
| Ovarian sarcoma | — | 4 | 7 y |
| Multinodular goiter | **HP:0005987** | (cumulative incidence of MNG or thyroidectomy by 40 y: **75% women, 17% men** vs 8% and 0% in controls — GeneReviews) | — |

**HPO disease annotation caveat:** the HPO annotation set for OMIM:601200 that I retrieved is sparse — only HP:0100528 (Pleuropulmonary blastoma, 11/14), HP:0002885 (Medulloblastoma, 1/86), HP:0002859 (Rhabdomyosarcoma), and HP:0000006 (Autosomal dominant inheritance, 20/20) ([HPO annotation API, OMIM:601200](https://ontology.jax.org/api/network/annotation/OMIM:601200)). **Cystic nephroma is not currently annotated to OMIM:601200 in HPO** — a concrete, actionable curation gap: HP:0034836 should be added with frequency ≈ 62/713 (PMID 39400264).

### 3.3 Quality‑of‑life impact

**No disease‑specific QoL instrument data (EQ‑5D, SF‑36, PROMIS, PedsQL) for pediatric cystic nephroma or for DICER1 syndrome was retrieved.** Searches surfaced only general statements that psychological support may help families balance surveillance benefit against cancer‑risk anxiety, plus QoL literature on other predisposition syndromes (e.g. Li‑Fraumeni). What *can* be said from retrieved data, per phenotype:

- **Cystic nephroma itself:** low long‑term functional burden when resected — van Peer et al.: *"an overall favorable outcome"* with a *"very low relapse rate."* The main durable impact is **loss of renal mass**: radical nephrectomy was used in 121 of 165 operated patients vs nephron‑sparing surgery in 28 (PMID 33673661), making single‑kidney status the commonest permanent sequela.
- **Bilateral disease (9/167, 5.4%)** carries real renal‑functional risk; in one bilateral case chemotherapy *"led to growth arrest, averting end-stage renal disease"* (PMID 33673661).
- **Surveillance burden:** six‑monthly abdominal ultrasound to age 8 then annually to 12, layered onto chest, thyroid, pelvic and ophthalmologic surveillance (GeneReviews; PMID 39400264) — a substantial but unquantified family burden. Bakhuizen et al. explicitly acknowledge that *"appraisal of potential benefits and harms vary"* and that *"patients have to be supported in choosing the surveillance program that best meets their needs"* (Bakhuizen JJ, Hanson H, van der Tuin K, Lalloo F, Tischkowitz M, Wadt K, Jongmans MCJ, et al. *Fam Cancer.* 2021;20(4):337–348. **PMID 34170462**; DOI 10.1007/s10689-021-00264-y).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**DICER1** — "dicer 1, ribonuclease III" ([HGNC REST](https://rest.genenames.org/fetch/symbol/DICER1)):

| Field | Value |
|---|---|
| HGNC ID | **HGNC:17098** |
| Location | **14q32.13** |
| OMIM | **606241** (gene); **601200** (DICER1‑related tumor predisposition / PPB familial tumor susceptibility) |
| Ensembl | ENSG00000100697 |
| NCBI Gene | **23405** |
| UniProt | **Q9UPY3** (Endoribonuclease Dicer, 1,922 aa) |
| Previous symbol | MNG1 |
| Aliases | Dicer, KIAA0928, K12H4.8‑LIKE, HERNA |

**Protein domain architecture** ([EBI Proteins API, Q9UPY3](https://www.ebi.ac.uk/proteins/api/proteins/Q9UPY3)): helicase ATP‑binding 51–227; helicase C‑terminal 433–602; Dicer dsRNA‑binding fold 630–722; **PAZ 895–1042**; **RNase III‑1 (IIIa) 1276–1403**; **RNase III‑2 (IIIb) 1666–1824**; dsRNA‑binding motif 1849–1914.

**No other causal gene, and no chromosomal abnormality, is established for pediatric cystic nephroma.** One germline event in the van Peer series was a 14q32 deletion encompassing DICER1 rather than a point variant (PMID 33673661) — i.e. whole‑gene deletion is an allelic mechanism, consistent with ClinGen's haploinsufficiency score of 3.

### 4.2 Pathogenic variants

**Two‑hit architecture (the defining molecular signature).** Brenneman et al. (PMID 26925222): *"tumors typically bear neomorphic missense mutations at one of five specific 'hotspot' codons within the RNase IIIb domain of DICER1, combined with complete loss of function (LOF) in the other allele."*

**Hit 1 — germline/constitutional LOF.** Typically **nonsense, frameshift (indel), splice‑site, or whole‑gene deletion**, truncating the ORF. Bahubeshi et al. found familial CN variants *"leading to premature stop codons"* that would impair essential protein domains (PMID 21036787). Brenneman et al.: *"Over 70% have inherited or de novo germline LOF mutations, most of which truncate the DICER1 open reading frame."*

**Hit 2 — somatic RNase IIIb hotspot missense.** The five hotspot codons, retrieved verbatim from Vedanayagam et al.: **E1705, D1709, D1810, E1813** plus **G1809** (Vedanayagam J, et al. *Nat Commun.* 2019;10:3682. **PMID 31417090**; DOI 10.1038/s41467-019-11610-1 — [PMC6695490](https://pmc.ncbi.nlm.nih.gov/articles/PMC6695490/)). Four of the five are acidic residues of the metal‑ion–coordinating catalytic cleft. A recurrent **RNase IIIa S1344L** variant phenocopies these: *"Structural and evolutionary coupling analyses reveal constrained proximity of RNase IIIa-S1344 to the RNase IIIb catalytic site, rationalizing why mutation of this site phenocopies known hotspot alterations."*

**Variant classification (ACMG/AMP, DICER1‑specific).** The **ClinGen DICER1 and miRNA‑Processing Gene Variant Curation Expert Panel** exists and is active, with **192 variant assertions: 5 Pathogenic, 26 Likely Pathogenic, 91 VUS, 39 Likely Benign, 6 Benign** ([ClinGen HGNC:17098](https://search.clinicalgenome.org/kb/genes/HGNC:17098)). Its published specification (Hatton JN, et al. *Hum Mutat.* 2023;2023:9537832. **PMID 38084291**; DOI 10.1155/2023/9537832 — [PMC10713350](https://pmc.ncbi.nlm.nih.gov/articles/PMC10713350/)) sets:
- **PVS1** NMD cutoff at **p.Pro1850**; "No criteria applied for disruption of start codon p.M1" (alternative methionines).
- **PM1**: *"putative missense variants at residues affecting RNase IIb domain metal ion-binding"*; **PM1_Supporting** for other RNase IIIb residues.
- **BA1**: AF > **0.003** in gnomAD (non‑cancer) subpopulations; **BS1**: AF > **0.0003**.
- **PS3**: *"patient-derived RNA assay demonstrates splicing impact that is out-of-frame OR in-frame with ≥193 residues affected."*
- Pilot: 40 variants; *"Clinically meaningful classifications…were achieved for 82.5% (33/40) of the pilot variants, with 100% concordance among the known P/LP and known B/LB variants."*

**ClinVar volume.** A ClinVar E‑utilities query `DICER1[gene] AND "clinsig pathogenic"[Properties]` returned **745 records** (query run this session; the count reflects that filter, not a curated P/LP variant tally).

**Variant spectrum at scale.** de Kock L, Wu MK, Foulkes WD catalogued **1,136 DICER1 alterations in 808 individuals** reported through 31 January 2019 (*Hum Mutat.* 2019;40(11):1939–1953. **PMID 31342592**; DOI 10.1002/humu.23877).

**Population allele frequency / carrier frequency** (germline LOF, all sources retrieved):
- GeneReviews: *"The prevalence of DICER1 is estimated at one in 6,099 to 8,416 individuals based on exome sequencing of two population cohorts."*
- Geisinger MyCode (92,296 adults): *"Germline DICER1 pLOF variants were observed in 1 in 3700 to 1 in 4600 participants, more than double the expected prevalence"* (Mirshahi UL, Kim J, Best AF, et al. *JAMA Netw Open.* 2021;4(2):e210112; DOI 10.1001/jamanetworkopen.2021.0112 — [full text](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2776900)).
- A later two‑cohort genome‑first analysis reported **1:8,242 in UK Biobank (46 unique pathogenic variants in 57 individuals)** and **1:8,119 in Geisinger (16 unique variants in 21 individuals)** (*Genetics in Medicine Open*, 2024 — retrieved via search summary of the [UK Biobank publication record](https://www.ukbiobank.ac.uk/publications/a-genome-first-approach-to-characterize-dicer1-pathogenic-variant-prevalence-penetrance-and-cancer-thyroid-and-other-phenotypes-in-2-population-scale-cohorts/); I was not able to fetch the primary article, so treat the exact figures as secondary).

**Somatic vs germline, with CN‑specific numbers** (van Peer et al., PMID 33673661): *"12 patients with confirmed germline DICER1 mutations (or 14q32 deletion in one case); six of them also had a somatic DICER1 mutation in the tumor"*; and *"In 21 patients, DICER1 mutations were identified in the tumor, but germline DNA was not analyzed. Among them, 16 tumors harbored both a missense and truncating mutation, the latter of which possibly represents germline events."*

**Functional consequence.** Hit 1 = **loss of function** (haploinsufficiency; ClinGen HI score 3). Hit 2 = **neomorphic / partial‑loss‑partial‑gain**, not simple LOF — see §6.

### 4.3 Modifier genes

**None identified** for pediatric cystic nephroma in any retrieved source.

### 4.4 Epigenetic information

DNA methylation profiling places cystic nephroma in a defined epigenetic class. Kommoss FKF, et al. (*Nat Commun.* 2023;14:1677. **PMID 36966138**; DOI 10.1038/s41467-023-37092-w — [PMC10039902](https://pmc.ncbi.nlm.nih.gov/articles/PMC10039902/)):
- *"This group of DICER1-associated mesenchymal tumors encompasses multiple well-established clinicopathological tumor entities and can be further divided into three clinically meaningful classes designated 'low-grade mesenchymal tumor with DICER1 alteration' (LGMT DICER1), 'sarcoma with DICER1 alteration' (SARC DICER1), and primary intracranial sarcoma with DICER1 alteration (PIS DICER1)."*
- *"The LGMT DICER1 class encompassed cases of cystic nephroma (CN, n = 7)…"*
- **Global methylation direction (verified on re‑read):** *"SARC DICER1 exhibited lower global DNA methylation levels as compared to LGMT DICER1, with the lowest global DNA methylation levels observed in PIS DICER1."* → cystic nephroma's class **retains relatively higher global methylation**; global hypomethylation accompanies sarcomatous progression.
- **Secondary gene‑level pathogenic variants:** *"TP53, KRAS/NRAS, and NF1 PVs were only observed in SARC DICER1 and PIS DICER1, underlining shared oncogenic mechanisms of these neoplasms."* (Stated at gene level, per scope. No TP53/RAS/**NF1** pathogenic variant was found in the LGMT DICER1 class that contains cystic nephroma.)
- No **NF2** alteration in cystic nephroma was reported in any retrieved source.
- The paper contains **no TERT/telomerase findings** (confirmed on targeted re‑read).

No histone‑modification or chromatin‑accessibility study specific to pediatric cystic nephroma was retrieved (no ENCODE/Roadmap dataset addresses this lesion).

### 4.5 Chromosomal abnormalities

**None characteristic.** The only large‑scale germline event retrieved is a **14q32 deletion** removing DICER1 in one patient (PMID 33673661) — i.e. a whole‑gene deletion mechanism, detectable by CMA. Per scope rules, chromosome‑arm–level somatic changes and chromothripsis are not discussed. Karyotype/FISH have no established role (§10).

---

## 5. Environmental Information

- **Environmental factors:** **None identified.** No toxin, radiation, pollution, or occupational exposure has been linked to pediatric cystic nephroma in any source retrieved (no CTD/TOXNET association exists for this phenotype). The etiology as documented is entirely genetic (§2.1).
- **Lifestyle factors:** **Not applicable.** The disease presents at a median age of 2.0 years (PMID 39400264); smoking, diet, exercise, and alcohol are not plausible or reported exposures.
- **Infectious agents:** **None.** No pathogen is implicated as cause or trigger in any retrieved source.

This section is a true negative, not a retrieval failure.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

1. **A germline (or, less often, post‑zygotic mosaic) loss‑of‑function DICER1 variant** — nonsense, frameshift, splice‑site, or whole‑gene deletion — is inherited or arises de novo, **leading to** every cell of the embryo carrying one non‑functional DICER1 allele (haploinsufficient state; PMID 26925222; PMID 21036787; ClinGen HI score 3).
2. **During nephrogenesis, a cell of the renal mesenchymal/progenitor lineage acquires a somatic missense substitution at one of the five RNase IIIb hotspot codons (E1705, D1709, G1809, D1810, E1813) on the remaining allele**, **resulting in** a biallelically altered cell — the "two‑hit variant" configuration (PMID 26925222; PMID 24481001; PMID 28222777; PMID 33673661). Brenneman et al. propose this second event is *"the rate limiting event in DICER1-associated tumorigenesis."*
3. **The hotspot substitution ablates metal‑ion coordination in the RNase IIIb catalytic centre**, **leading to** failure to cleave the **5′ (5p) arm** of pre‑miRNA hairpins while 3p‑arm cleavage by RNase IIIa persists — *"cancer hotspot mutations in DICER1 RNase IIIb selectively impair miRNA-5p processing"* (PMID 31417090). This is a **neomorphic, not null, allele**; siRNA processing is largely preserved.
4. **Branch A (loss of function): depletion of mature 5p miRNAs, including the tumour‑suppressive let‑7 family**, **results in** de‑repression of 5p‑miRNA targets. Vedanayagam et al. note the *"let-7 family has previously been suggested as a tumor suppressor miRNA family"* with derepression of targets such as **HMGA2**, and show *"derepression of specific miRNA target signatures"* in DICER1‑hotspot tumours (PMID 31417090).
5. **Branch B (gain of function — demonstrated 2025/2026, newer than the classic model): 3p‑arm‑nicked pre‑miRNAs preferentially load 3p passenger strands into Argonaute**, **leading to** a neomorphic repertoire of functional 3p guide miRNAs with increased repressive capacity. Verbatim: *"3p arm-nicked pre-miRNAs preferentially load miRNA-3p species into Argonaute, compared to corresponding duplexes. Moreover, activity assays, RNA-seq data, and Argonaute-mRNA profiling, confirm that these confer increased repression capacity"* (Jee D, Lee S, Yang D, Rickert R, Shang R, Huangfu D, Lai EC. bioRxiv 2025.10.15.682667; **PMID 41279602**; DOI 10.1101/2025.10.15.682667 — [PMC12632780](https://pmc.ncbi.nlm.nih.gov/articles/PMC12632780/); peer‑reviewed version in *Nat Struct Mol Biol*). A parallel line of work reports **HERVH endogenous‑retrovirus reactivation** in DICER1‑mutant cells and increased migratory capacity ([*Nat Commun* 2026, "DICER1-related tumour predisposition mutations increase 3p-miRNA function and HERVH activity"](https://www.nature.com/articles/s41467-026-76094-2); primary text not fetched — treat as an emerging finding).
6. **Loss of Dicer‑dependent miRNA activity in the developing kidney perturbs nephrogenesis**, **leading to** the cystic architecture. In mouse: removal from nephron progenitors caused *"elevated apoptosis and premature termination of nephrogenesis"*; removal from the ureteric bud led to *"the development of renal cysts"* preceded by excessive proliferation and apoptosis, with *"disrupted ciliogenesis"* and reduced **Wnt11** and **c‑Ret** expression (Nagalakshmi VK, Ren Q, Pugh MM, Valerius MT, McMahon AP, Yu J. *Kidney Int.* 2011. **PMID 20944551**; DOI 10.1038/ki.2010.385). Independently, *"Dicer1 is required for development of the female reproductive tract and also normal kidney morphogenesis,"* with ureteric‑bud deletion producing hydronephrosis and parenchymal cysts (Pastorelli LM, Wells S, Fray M, et al. *Mamm Genome.* 2009;20(3):140–151. **PMID 19169742**; DOI 10.1007/s00335-008-9169-y). **This step is inferred for human CN** — it is demonstrated in mouse developmental genetics (full Dicer1 ablation), not in human cystic nephroma tissue.
7. **Cell of origin (model‑based, 2026): a Hic1⁺ mesenchymal stromal/"universal fibroblast" population gives rise to the lesion.** Verbatim: *"Spatial single-cell transcriptomic analysis reveals a Hic1⁺Pdgfra⁺Dpt⁺Pi16⁺ fibroblastic progenitor population, corresponding to universal fibroblasts subjacent to transitional epithelium of renal collecting ducts, that can undergo rhabdomyoblastic differentiation or become proliferative sarcomatous cells"* (Kommoss FKF, Zhang JYH, Lynch BJ, Chen SY, Senz J, Moscovitz Y, Hill LA, Ma D, Scott RW, Bush J, Chen KS, Roth A, von Deimling A, Foulkes WD, Morin GB, Underhill TM, Wang Y, Huntsman DG. *Nat Commun.* 2026;17(1):4608. **PMID 41912509**; DOI 10.1038/s41467-026-70971-6 — [PMC13199431](https://pmc.ncbi.nlm.nih.gov/articles/PMC13199431/)).
8. **The resulting lesion is a multilocular cystic mass whose septa contain hypocellular primitive mesenchyme**, **producing** the diagnostic histology: *"multiple cystic structures lined by flat or cuboidal epithelium"* with *"thin septa separate[ing] cysts and composed of fibrous tissue with tubular structures, but lack[ing] blastema"* (PMID 40231379); cystic nephroma is described as *"hypocellular and primitive mesenchyme"* with *"focal condensation adjacent to cystically dilated renal ducts"* (PMID 41912509).
9. **Progressive enlargement produces mass effect**, **leading to** the clinical presentation — palpable abdominal/flank mass in 70% (PMID 33673661), with median tumour weight 540 g (range 120–4000 g) and median volume 292 mL. Occasional **hypertension** (PMID 42704439; mechanism in that case not molecularly established — renin‑mediated compression is the clinical inference, not a demonstrated finding), hematuria, or UTI.
10. **Branch C — malignant progression to anaplastic sarcoma of the kidney (ASK).** The primitive septal mesenchyme can acquire additional somatic drivers, **leading to** sarcomatous transformation:
 - **NRAS Q61R** in the incipient anaplastic focus only: *"Multi-region sequencing of PCN and anaplastic areas revealed an NRAS Q61R mutation exclusively in the latter. Germline and somatic DICER1 alterations were common to both. This is the first report of an oncogenic alteration in incipient sarcomatous transformation in a PCN"* (Cortes‑Santiago N, Whittle SB, Scollon S, Plon SE, Vasudevan S, Lucas BJ, Roy A. *Pediatr Blood Cancer.* 2026;73(2):e70068. **PMID 41431269**; DOI 10.1002/1545-5017.70068).
 - **TP53** alteration/expression in the majority of ASK: *"p53 expression…present in seven of ten"* registry cases (Schoettler PJ, et al. *Pediatr Blood Cancer.* 2024. **PMID 38807260**; DOI 10.1002/pbc.31090 — [PMC11590164](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590164/)); and biallelic DICER1 with **TP53 co-mutations** in anaplastic kidney sarcomas (Arizpe D, et al. *Hum Pathol.* 2026;172:106110. **PMID 41905669**; DOI 10.1016/j.humpath.2026.106110).
 - Class‑restricted gene‑level events: **TP53, KRAS/NRAS, NF1** pathogenic variants occur **only** in SARC/PIS DICER1, not in the LGMT class containing CN (PMID 36966138) — i.e. these are *progression* events, not initiating ones.
 - **Global DNA hypomethylation** accompanies the sarcoma classes (PMID 36966138).
 - **Immunophenotypic switch:** *"as lesions progressed from cystic to solid (pCN/anaplastic sarcoma of kidney, and PPB types I to III), ER expression was lost and PRAME expression increased"* (Thorner PS, et al. *Am J Surg Pathol.* 2024;48(6):733–741. **PMID 38539053**; and Thorner PS, et al. *J Pathol Clin Res.* 2022;8(3):294–304. **PMID 35297207**: *"PRAME may be a marker for the progression that certain DICER1-related lesions are thought to undergo, such as PPB and CN"*).
 - Witnessed in situ: a 7‑month‑old had a tumour with *"histologic features predominantly of a cystic nephroma, but with microscopic cellular foci which contained atypical mitotic figures and anaplastic nuclei"* — *"a unique 'nascent' anaplastic sarcoma of kidney"* (Wu MK, Cotter MB, Pears J, McDermott MB, Fabian MR, Foulkes WD, O'Sullivan MJ. *Hum Pathol.* 2016;53:114–120. **PMID 27036314**; DOI 10.1016/j.humpath.2016.03.002).
 - **Frequency of this branch is low:** *"As for PPB, pediatric cystic nephroma also has the potential for malignant transformation towards anaplastic sarcoma of the kidney, but this event seems far less common than in PPB"* (PMID 40231379). Only 4/713 registry carriers developed ASK (PMID 39400264).

### 6.2 Category‑by‑category detail

- **Molecular pathways:** the **miRNA biogenesis / RNA‑interference pathway** is the primary lesion (GO:0031054 pre‑miRNA processing; GO:0035195 miRNA‑mediated post‑transcriptional gene silencing; GO:0070578 RISC‑loading complex — all IDs verified via [OLS4/GO](https://www.ebi.ac.uk/ols4/api/search?q=pre-miRNA%20processing&ontology=go&rows=10); regulation terms GO:2000631/2000632/2000633). Downstream developmental signalling is implicated in mouse: **Wnt11** and **c‑Ret** at ureteric tips are reduced (PMID 20944551). In progression, **RAS–MAPK** (NRAS Q61R; also BRAF V600E and PDGFRA variants reported in isolated ASK cases — PMID 38807260) and **p53** pathways are engaged. No Wnt/mTOR/PI3K‑AKT dysregulation specific to human cystic nephroma was retrieved.
- **Cellular processes:** apoptosis (nephron‑progenitor apoptosis), cell‑cycle/proliferation dysregulation, **disrupted ciliogenesis**, branching morphogenesis failure, and perturbed mesenchymal differentiation (PMID 20944551; PMID 41912509). Inflammatory cells are noted within the cellular stroma of pediatric CN (PMID 28177962).
- **Protein dysfunction:** RNase IIIb hotspot substitutions are **catalytic‑site loss‑of‑function at the domain level** combined with **organism‑level neomorphism** (altered strand selection), not misfolding or aggregation. The second allele is typically **truncated/absent**.
- **Metabolic changes:** none reported. No KEGG/HMDB metabolic lesion is described for this disease.
- **Immune system involvement:** no autoimmunity or immunodeficiency. Only incidental stromal inflammatory infiltrate (PMID 28177962). PRAME — a cancer‑testis antigen upregulated in DICER1 malignancies — is of **immunotherapeutic**, not pathogenic, interest (PMID 35297207).
- **Tissue damage mechanisms:** parenchymal replacement and compression by expanding cysts (imaging "beak sign" of compressed rim of parenchyma), rather than oxidative stress, ischemia, or fibrosis as primary mechanisms. Septal fibrous tissue is a structural, not reactive‑fibrotic, element.
- **Biochemical abnormalities:** the single defect is **ribonuclease III (Dicer) catalytic dysfunction**. No enzyme deficiency measurable in blood/urine, no receptor or ion‑channel defect.
- **Molecular profiling:**
 - *Transcriptomics / spatial single‑cell:* PMID 41912509 defines cell states (Progen; Prolif; Ground; TR Diff Myo; Diff Myo) and shows human tumours recapitulate the model's states and trajectories.
 - *Small‑RNA profiling:* 5p depletion signature; TCGA small‑RNA analyses (PMID 31417090). A GEO series for the 3p gain‑of‑function work is indexed as **GSE313183** (seen via [OmicsDI](https://www.omicsdi.org/dataset/geo/GSE313183) — I did not fetch the GEO record itself).
 - *Epigenomics:* genome‑wide methylation classes; **534 DICER1‑syndrome tumours** analysed (PMID 36966138).
 - *Proteomics / metabolomics / lipidomics:* **no dedicated study of pediatric cystic nephroma retrieved** in PRIDE, MetaboLights, or LIPID MAPS‑adjacent literature. The only protein‑level markers are IHC (DICER1, ER, inhibin, PRAME, PAX8, TP53).
 - *Functional genomics (CRISPR/RNAi):* no DepMap or screen specific to cystic nephroma retrieved. The closest functional genomics is isogenic **Dicer1‑KO and Dicer1‑S1344L human ESC** lines (PMID 41279602).

### 6.3 Suggested ontology terms for mechanism

**GO biological process / cellular component (IDs verified this session):** GO:0031054 (pre‑miRNA processing); GO:0035195 (miRNA‑mediated post‑transcriptional gene silencing); GO:2000631/2000632/2000633 (regulation of pre‑miRNA processing); GO:0070578 (RISC‑loading complex). Additional processes that should be annotated but whose IDs I did **not** verify in this session, so I give names only: *kidney development*, *metanephros development*, *ureteric bud morphogenesis*, *branching involved in ureteric bud morphogenesis*, *apoptotic process*, *cilium assembly*, *ribonuclease III activity*.

**CL cell types (IDs verified):** **CL:0000057** fibroblast (the Hic1⁺Pdgfra⁺Dpt⁺Pi16⁺ universal‑fibroblast origin); **CL:0000134** mesenchymal stem cell (the Hic1⁺ MSC progenitor); **CL:0002518** kidney epithelial cell (cyst‑lining epithelium); CL:0020121 epithelial cell of mesonephric duct (developmental context).

**Subcellular (GO Cellular Component):** cytoplasmic RISC/RISC‑loading complex (GO:0070578). Dicer is cytoplasmic; no mitochondrial, ER, or lysosomal compartment is implicated.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ: kidney** — **UBERON:0002113** ("A paired organ of the urinary tract…"; verified via [OLS4/UBERON](https://www.ebi.ac.uk/ols4/api/search?q=kidney&ontology=uberon&exact=true&rows=5)). Developmentally the **metanephros, UBERON:0000081**.
- **Secondary organ involvement:** none intrinsic to the lesion. Mass effect on adjacent retroperitoneal structures; one documented systemic consequence is **hypertension** (PMID 42704439). **Metastasis does not occur**: *"None of the patients had metastatic disease"* and *"Information on lymph node involvement was documented for 24 patients and none were positive"* (PMID 33673661).
- **Body systems involved:** **urinary/renal** primarily. In the syndromic context, DICER1 affects the **respiratory** (PPB, lung cysts), **endocrine** (thyroid), **reproductive** (ovarian SLCT, cervical ERMS), **nervous/ocular** (CNS tumours, ciliary body medulloepithelioma), **musculoskeletal/soft tissue** (ERMS, sarcomas), and **upper airway** (nasal chondromesenchymal hamartoma) systems (PMID 39400264).

### Tissue and cell level
- **Tissues:** renal **parenchyma** with cysts lined by **epithelium** (flat/cuboidal/hobnail) and septa of **fibrous connective tissue** containing mature tubules (PMID 40231379). Pediatric CN shows *"subepithelial accentuation of stromal cellularity"* in 6/7 cases, the increased cellularity "frequently included inflammatory cells" (PMID 28177962).
- **Cell populations:**
 - Cyst‑lining **kidney epithelial cells** (**CL:0002518**) — flattened, cuboidal, or hobnail; PAX8‑positive in a reported case ([Zi et al., *Front Oncol.* 2026; DOI 10.3389/fonc.2026.1799009](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)).
 - Septal **primitive mesenchymal / fibroblastic cells** (**CL:0000057**, **CL:0000134**) — the compartment that carries the DICER1 lesion and that transforms in ASK; **ER‑positive in the stromal compartment** of pediatric CN (PMID 28177962; PMID 38539053).
 - **Absent by definition:** blastemal cells (cf. UBERON:0010531 metanephros induced blastemal cells) — *"By definition, CN does not contain any solid components or blastemal cells in the septa. Only mature epithelial tubules, possibly from pre-existent normal renal tissue, are acceptable for the diagnosis"* (PMID 33673661).

### Subcellular level
Cytoplasmic miRNA‑processing machinery — **RISC‑loading complex, GO:0070578**. No organellar pathology (no mitochondrial, ER, lysosomal, or nuclear‑aggregate phenotype) is reported.

### Localization and lateralization
- **Site:** renal parenchyma, any pole; **UBERON:0010533** (metanephros cortex), **UBERON:0004737** (metanephric collecting duct), **UBERON:0005249** (metanephric renal pelvis), **UBERON:0014706** (primitive renal collecting duct system) are the relevant UBERON terms verified this session. The 2026 mouse model localizes the progenitor **"subjacent to transitional epithelium of renal collecting ducts"** (PMID 41912509).
- **Lateralization:** predominantly **unilateral**. van Peer et al.: unilateral in 158 of 167; *"bilateral CN in 9 patients (5.4%), including one with metachronous tumors."* A bilateral, recurrent, DICER1‑associated pediatric CN has been separately reported (Caron CP, Turcotte B, Pelland‑Marcotte MC, Schultz KAP, Harvey I, Bolduc S. *Can Urol Assoc J.* 2021;15(5):E290–E292. **PMID 33119505**; DOI 10.5489/cuaj.6836).

---

## 8. Temporal Development

### Onset
- **Age:** infancy to early childhood. GeneReviews: *"Pediatric CN is most common in children younger than age four years, although DICER1-associated pediatric CN has also been reported in older children and adolescents."* Registry: *"The median age at diagnosis of CN was 2.0 years (range: 4 months–15.3 years) with 90% occurring by 5 years of age"* (PMID 39400264). Literature review median **16 months**, range *"prenatal diagnosis—16 years"* (PMID 33673661). The lesion is thus **pediatric‑onset, occasionally congenital/prenatally detected**, not congenital‑by‑definition.
- **Pattern:** **insidious and chronic** — a painless enlarging mass. GeneReviews: "Most cases present as a painless, enlarging abdominal or flank mass," though "Rapid growth may necessitate intervention due to mass effect concerns."

### Progression
- **Staging:** cystic nephroma is a benign neoplasm; where SIOP staging was applied, *"51 patients had stage I and one had stage III disease based on intraoperative tumor rupture"* (n=52; PMID 33673661). There is no AJCC/WHO grading scheme for a benign lesion. The adjacent malignant entity ASK is staged conventionally (13 stage I, 12 II, 10 III, 5 IV of 40; PMID 38807260).
- **Rate:** slow and variable. One documented trajectory: *"progressed over the span of 8 years to a growing multiloculated cyst and then ASK"* (Case 28, PMID 38807260).
- **Course:** **stable/slowly progressive before resection; cured and stable after complete resection.** Not relapsing‑remitting, not episodic.
- **Duration:** **self‑limited once resected.** The underlying *predisposition* is lifelong.

### Patterns
- **Remission:** **treatment‑induced (surgical)**. No spontaneous regression of cystic nephroma was reported in any retrieved source. *"One local relapse was described, most likely due to incomplete resection"* (PMID 33673661). A bilateral/recurrent case required repeat intervention (PMID 33119505). One bilateral case had chemotherapy‑induced *"growth arrest, averting end-stage renal disease"* (PMID 33673661).
- **Critical periods:**
 - **Birth to ~5 years** is the window of lesion formation (90% by 5 y; PMID 39400264) — hence surveillance begins at birth/diagnosis of the variant.
 - **Birth to 8 years** is the window of most intensive renal imaging, with annual imaging to 12 (GeneReviews; PMID 39400264). The Registry cautions: *"Some anaplastic sarcomas of the kidney have been diagnosed after age 12."*
 - **Interventional window:** detecting a small CN preserves nephrons — *"to preserve renal function through less extensive surgery, especially in cases of bilateral disease, and to prevent progression to ASK"* (PMID 39400264). NCI PDQ similarly notes surveillance aims to "identify cystic nephromas when they are small and nephron-sparing surgery is still possible" ([NCI PDQ, Wilms Tumor and Other Childhood Kidney Tumors Treatment](https://www.cancer.gov/types/kidney/hp/wilms-treatment-pdq)).
 - **Timing of synchronous/metachronous DICER1 tumours:** *"Of the 26 CN patients that developed other tumors, four developed these tumors before the CN, 14 were concomitant, and eight patients developed the other tumors after the CN. The time range between the tumors varied from 1 month to 4 years"* (PMID 33673661).

---

## 9. Inheritance and Population

### Epidemiology
- **No population incidence or prevalence rate (per 100,000) for pediatric cystic nephroma was retrievable.** No SEER, GBD, Orphanet prevalence class, or national registry figure exists for this lesion in the sources I reached. This is a genuine data gap.
- **Best available denominators:**
 - **167 CN patients** identifiable in the entire world literature up to 2021 (PMID 33673661) — the single most useful scale anchor.
 - **62 cystic nephromas among 713 germline DICER1 carriers from 38 countries** (≈8.7%) in the International PPB/DICER1 Registry (PMID 39400264); GeneReviews gives the carrier‑level frequency as **"≤10%."**
 - A Chilean review surfaced in search states cystic nephroma represents **2–4% of renal neoplasms** with **~200 cases described**; I did not fetch that article at source, so treat as **unverified secondary** ([SciELO, "Cystic nephroma in pediatrics"](https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S2452-60532021000500754)).
- **Carrier frequency of the predisposing genotype** (the upstream denominator): 1:3,700–1:4,600 (Geisinger, JAMA Netw Open 2021); 1:6,099–1:8,416 (GeneReviews, two exome cohorts); 1:8,242 UKB / 1:8,119 Geisinger (Genetics in Medicine Open 2024, secondary).

### Genetic parameters
| Parameter | Finding | Source |
|---|---|---|
| **Inheritance** | **Autosomal dominant** (HP:0000006). *"DICER1 is inherited in an autosomal dominant manner with reduced, age-related penetrance."* Recurrence risk: *"Each child of an individual with a germline constitutional DICER1 pathogenic variant has a 50% chance of inheriting the pathogenic variant."* | GeneReviews |
| **Penetrance** | **Incomplete and strongly age‑dependent.** *"By age ten years 5.3% (95% CI; 0.6%-9.7%) had developed a neoplasm (females: 4.0%; males: 6.6%). By age 50 years 19.3% (95% CI; 8.4%-29.0%) had developed a neoplasm (females: 26.5%; males: 10.2%)."* | GeneReviews, citing Stewart DR, Best AF, Williams GM, et al. *J Clin Oncol.* 2019;37(8):668–676. **PMID 30715996**; DOI 10.1200/JCO.2018.78.4678 |
| Penetrance, CN‑specific | ≤10% of carriers (GeneReviews); 8.7% in the Registry cohort — i.e. **low organ‑specific penetrance** | GeneReviews; PMID 39400264 |
| Penetrance, genome‑first check | *"Malignant tumors (primarily thyroid carcinoma) were observed in 4 of 25 participants (16%) with DICER1 pLOF variants, which is comparable (by 50 years of age) to the frequency of neoplasms in the largest registry- and clinic-based (phenotype-first) DICER1 studies"* — **no cystic nephroma was observed** in this adult cohort (expected, given the <5 y age window) | Mirshahi et al. 2021 |
| **Expressivity** | **Highly variable** — same germline variant yields PPB in one relative, CN in another, nothing in a third; illustrated in multi‑tumour pedigrees (PMID 28222777; PMID 21882293) | — |
| **Genetic anticipation** | **Not reported / not applicable** — DICER1 is not a repeat‑expansion locus | — |
| **Mosaicism** | *"Approximately 10% of individuals with a de novo DICER1 pathogenic variant have somatic mosaicism for the variant"* (GeneReviews). Mosaic RNase IIIb hotspot mosaicism is a distinct severe phenotype with multifocal renal/lung cysts (PMID 26925222) | GeneReviews; PMID 26925222 |
| **Proportion inherited** | *"Approximately 85% of individuals diagnosed with DICER1-associated PPB are thought to have inherited a DICER1 germline pathogenic variant from a parent"* (GeneReviews); the 2024 Registry paper notes approximately **87%** of germline DICER1 variants are inherited (PMID 39400264) | — |
| **Founder effects** | **None reported** in any retrieved source | — |
| **Consanguinity** | **Not a factor** — autosomal dominant, and the second hit is somatic | — |

### Population demographics
- **Ethnic/ancestral predisposition:** **none reported.** The Registry cohort spans 38 countries (PMID 39400264); the Geisinger cohort was 98% white, which **limits** ancestral inference rather than supporting any. No ancestry‑specific DICER1 variant distribution for cystic nephroma was retrieved.
- **Geographic distribution:** **worldwide; no endemic area.** No geographic clustering of specific variants was retrieved.
- **Sex ratio:** modest male excess — 93:72 (≈1.3:1) in the 167‑patient literature review (PMID 33673661); 6:1 in a 7‑case pathology series (PMID 28177962). A 2026 review states CN "is more common in male newborns (with a male-to-female ratio of 3:1)" ([Zi et al., *Front Oncol.* 2026](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)) — secondary. Note that *syndrome‑wide* penetrance is higher in females (26.5% vs 10.2% by 50 y), driven by gynaecologic and thyroid disease, not by renal disease.
- **Age distribution:** sharply concentrated — median 16–24 months; 90% by 5 years; rare cases to 16 years (PMID 33673661; PMID 39400264).

---

## 10. Diagnostics

### Clinical tests

**Laboratory tests / biomarkers.** There is **no serum, urine, or circulating biomarker** for pediatric cystic nephroma, and none is listed in FDA biomarker resources for this indication. Urinalysis may detect hematuria (HP:0000790). Blood pressure measurement is clinically relevant given documented hypertensive presentation (PMID 42704439). **This is the main diagnostic gap for the disease.**

**Imaging.** The lesion is defined radiologically as a sharply marginated, multiloculated cystic renal mass with enhancing thin septa.
- **Ultrasound (first‑line in children):** *"CN presents as multiloculated lesions, well circumscribed by the surrounding renal parenchyma with thin septa inside, and without evidence of vascularity or calcifications"* (Greco F, Faiella E, Santucci D, et al. *J Kidney Cancer VHL.* 2017;4(3):1–9. **PMID 28752022**; DOI 10.15586/jkcvhl.2017.79 — [PMC5519771](https://pmc.ncbi.nlm.nih.gov/articles/PMC5519771/)). Compressed parenchyma forms a thin rim ("beak sign").
- **CT:** sharply circumscribed, multiseptated mass with hypoattenuating locules; septa may enhance; no contrast excretion into the locules.
- **MRI:** rarely required; septa hypointense on all sequences, cyst signal varying with content.
- **Critical limitation:** *"It is challenging to correctly diagnose CPDN or CN based on clinical characteristics or radiology. Imaging studies do not seem to be able to reliably discriminate CN from CPDN"* (PMID 33673661). A pediatric CN has been misclassified as **Bosniak IV** ([Zi et al. 2026](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)).
- RadLex/DICOM descriptors specific to this entity were not retrieved.

**Functional tests and electrophysiology:** **not applicable.** No pulmonary‑function, cardiac‑stress, EEG/EMG/ECG, or nerve‑conduction test has a role. (Chest imaging is performed for the *syndrome*, not for the renal lesion.)

**Biopsy / pathology — the diagnostic standard.**
- **Gross:** well‑circumscribed multiloculated cystic mass; median weight 540 g (range 120–4,000 g), median volume 292 mL (PMID 33673661).
- **Microscopic (verbatim):** *"multiple cystic structures lined by flat or cuboidal epithelium"*; *"thin septa separate[ing] cysts and composed of fibrous tissue with tubular structures, but lack[ing] blastema typically present in Wilms tumor"*; *"pediatric cystic nephroma does not present any solid component or undifferentiated cells in the septa of cysts"* (PMID 40231379). Lining cells may be *"cuboidal or hobnail-like cells with eosinophilic cytoplasm"* with *"no cellular atypia or mitotic figures"* ([Zi et al. 2026](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)).
- **Sampling caveat (important):** thorough sampling is required because microscopic anaplastic foci can hide within an otherwise classic CN — PMID 27036314 describes *"microscopic cellular foci which contained atypical mitotic figures and anaplastic nuclei"* in a lesion otherwise read as cystic nephroma.
- **Immunohistochemistry:**
 - **ER: positive in stromal cells.** *"ER expression was seen in stromal cells in pCN and pleuropulmonary blastoma (PPB) types I and Ir"* but absent in solid tumours; the authors conclude *"ER expression in stromal cells is not a feature of DICER1 perturbation but rather is related to the presence of cystic components,"* and that antiestrogen therapy would therefore not be expected to help (PMID 38539053).
 - **Inhibin: negative** in pediatric CN — *"whereas most (83%) of adult cases labeled for inhibin at least focally, no pediatric case labeled for inhibin"* (PMID 28177962). **This is the single most useful discriminator from adult CN/MEST.**
 - **PRAME: negative in CN, positive in ASK**; one atypical CN with mesenchymal proliferation was PRAME‑positive (PMID 35297207) — a progression marker.
 - **TP53:** strong expression in most ASK (7/10 registry cases; PMID 38807260) — not expected in CN.
 - **PAX8:** positive in cyst‑lining epithelium in a reported case ([Zi et al. 2026](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)).
 - **DICER1 protein:** in PPB, *"DICER1 protein was undetectable in the epithelial component"* of tumours while retained in the malignant mesenchyme (Hill DA, Ivanovich J, Priest JR, et al. *Science.* 2009. **PMID 19556464**; DOI 10.1126/science.1174334). An analogous epithelial‑loss pattern in cystic nephroma is **the expected inference** from the shared two‑hit biology, but I did not retrieve a primary quotation establishing it specifically in CN; do not record it as fact.

### Genetic testing

**Recommended approach.** Any child with cystic nephroma should undergo **germline DICER1 testing with genetic counselling**, and tumour DICER1 sequencing where available. *"The presence of cystic nephroma in a child or young adult should alert the clinician to the possibility of a germline mutation in DICER1"* (position reflected across GeneReviews and PMID 33673661, which states *"Awareness of concomitant or subsequent tumors and genetic testing is important"*). The rationale is explicit: *"The benefits of DICER1 testing is that a diagnosis of DICER1-related tumor predisposition can be established and other family members can be identified so surveillance can be started"* ([Zi et al. 2026](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)).

| Modality | Utility for this disease |
|---|---|
| **Single‑gene DICER1 sequencing (germline, blood)** | **First‑line.** Detects the truncating/splice first hit. GTR entries: GTRT000050538 / AN1481031 (cystic nephroma); GTRT000013889 (DICER1‑related tumor predisposition). |
| **Tumour DICER1 sequencing (somatic)** | **High value** — identifies the RNase IIIb hotspot second hit and, where both a missense and a truncating variant are present in tumour, flags a probable germline event: *"16 tumors harbored both a missense and truncating mutation, the latter of which possibly represents germline events"* (PMID 33673661). A dedicated tumour NGS assay exists (Mayo Clinic Laboratories DICET). |
| **Gene panels** | Useful where DICER1 sits on a pediatric cancer‑predisposition or renal‑tumour panel; the DICER1 VCEP's scope is "DICER1 and miRNA‑processing genes" (ClinGen). |
| **WES / WGS** | Useful in diagnostic odysseys and for de novo/mosaic detection; the population prevalence estimates themselves came from exome cohorts (GeneReviews; Mirshahi 2021). WGS adds structural‑variant detection. |
| **Chromosomal microarray (CMA)** | **Indicated when sequencing is negative** — a **14q32 deletion** removing DICER1 accounted for one germline case (PMID 33673661); ClinGen HI score 3 supports deletion as a mechanism. |
| **Deep sequencing of multiple tissues** | **Required to exclude mosaicism**, which standard blood sequencing can miss and which defines a distinct severe phenotype (PMID 26925182 — see PMID 26925222). |
| **Karyotyping, FISH** | **No established role.** |
| **mtDNA testing, repeat‑expansion testing** | **Not applicable** — DICER1 is nuclear; no repeat mechanism. |

### Omics‑based diagnostics
- **DNA methylation profiling (epigenomics) is the one omics modality with demonstrated diagnostic utility.** Methylation classification assigns tumours to LGMT DICER1 (which contains CN), SARC DICER1, or PIS DICER1 (PMID 36966138), and can be *"helpful for correctly classifying tumors as one of three classes of mesenchymal tumors with DICER1 alteration or to exclude other DICER1-associated tumor entities."*
- **RNA sequencing:** used in research (spatial single‑cell, PMID 41912509); small‑RNA 5p‑depletion signatures are mechanistically diagnostic in principle (PMID 31417090) but are not a clinical assay.
- **Proteomics, metabolomics, liquid biopsy:** **no validated or reported application** to pediatric cystic nephroma was retrieved.

### Clinical criteria and differential diagnosis

**Diagnostic criteria** are **histopathological, not criteria‑based** (no DSM/ICD‑style criterion set exists). The operative definition is exclusionary: *"By definition, CN does not contain any solid components or blastemal cells in the septa. Only mature epithelial tubules, possibly from pre-existent normal renal tissue, are acceptable for the diagnosis"* (PMID 33673661).

| Differential | Distinguishing features |
|---|---|
| **Cystic partially differentiated nephroblastoma (CPDN)** — named only to differentiate | *"characterized by the presence of undifferentiated (blastemal) cells in the septa of the cysts, and by the lack of solid components"*; *"Somatic DICER1 mutations have never been identified in CPDN"* (PMID 33673661). Imaging cannot separate them (ibid.). |
| **Adult cystic nephroma / MEST** — named only to differentiate | Adults, almost all female (median 50.5 y, all female in the comparison series); **inhibin‑positive (83%)**; *"wavy, ropy collagen in association with cellular stroma"* in 58%; DICER1 mutated in only 1/10. Verbatim conclusion: *"These results support the current World Health Organization Classification's separation of adult and pediatric cystic nephromas as distinct entities"* (PMID 28177962). |
| **Wilms tumour (nephroblastoma, HP:0002667)** | *"generally has a prevalent solid pattern"* (PMID 40231379); on US *"nephroblastoma has the same echogenicity of the liver and contains a greater solid component than CN"* (PMID 28752022). Note DICER1 carriers can get Wilms tumour independently — NCI PDQ: *"DICER1 syndrome includes an elevated risk of Wilms tumor, which is not a consequence of a prior cystic nephroma."* |
| **Anaplastic sarcoma of the kidney (ASK)** | Solid/anaplastic areas, atypical mitoses, PRAME‑positive, TP53‑expressing; may be microscopic within a CN (PMID 27036314; PMID 38807260). |
| **Segmental multicystic dysplastic kidney** | Listed by GeneReviews among entities to exclude. |
| **Cystic renal cell carcinoma** | *"CRCC is very difficult to differentiate from CN using US, but the presence of intramural nodules and thick septa is suggestive of CRCC"* (PMID 28752022). |
| **Simple renal cysts (HP:0012581)** | Common incidental finding in adult DICER1 carriers (32/286, 11%, median age 27 y; PMID 39400264) — unilocular, non‑neoplastic. |

### Screening
See §13. In brief: **no newborn screening or population carrier screening** exists or is recommended. Screening is **cascade genetic testing of first‑degree relatives** plus **imaging surveillance of known carriers** — *"Abdominal ultrasounds for pediatric CN and other kidney tumors every six months until age eight years and then annually until age 12 years"* (GeneReviews; PMID 39400264).

---

## 11. Outcome / Prognosis

### Survival and mortality
- **Excellent.** van Peer et al. (167 CN patients): *"children with CPDN and CN are young, do not present with metastases, and have an excellent outcome."* Of patients with outcome data, *"161 patients"* were recorded as surviving/disease‑free.
- **Disease‑specific mortality is essentially zero.** *"Death was reported in six/103 patients with CPDN and six/118 CN patients, none directly due to disease."* Detail: *"Six patients died during follow up; in two cases related to CN treatment (post-operative sepsis), and in four cases due to complications caused by treating concomitant disease"* (PMID 33673661). **Mortality is treatment‑ and comorbidity‑attributable, not tumour‑attributable.**
- **No formal 5‑ or 10‑year survival rate, life expectancy estimate, or population mortality rate** is published for pediatric cystic nephroma — the lesion is too rare and too uniformly curable for such statistics. One case series reported *"no signs of recurrence in pediatric CN patients following a 10-year postoperative follow-up"* ([Zi et al. 2026](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)).
- **Contrast with the malignant branch (ASK):** two‑year EFS **81.8%** (stage I–II) vs **46.6%** (stage III–IV); two‑year OS **88.9%** vs **70.0%** (PMID 38807260). This asymmetry is the core prognostic argument for early detection.

### Morbidity and function
- Dominant morbidity is **surgical and nephron‑related**: radical nephrectomy in 121 vs nephron‑sparing surgery in 28 of 165 operated patients (PMID 33673661) → most survivors live with a single kidney. Bilateral disease (5.4%) carries genuine renal‑failure risk, mitigated in one case by chemotherapy‑induced growth arrest *"averting end-stage renal disease"* (ibid.).
- **Perioperative complications:** two deaths from post‑operative sepsis (ibid.) — the only directly treatment‑attributable mortality documented.
- **Lifelong surveillance morbidity:** repeated imaging and the psychological burden of a cancer‑predisposition diagnosis; Bakhuizen et al. formally acknowledge benefit/harm uncertainty (PMID 34170462).
- **Disability outcomes:** no ICF‑coded disability data; no disability registry figures retrieved. **No disease‑specific EQ‑5D/SF‑36/PROMIS data retrieved** (see §3.3).

### Disease course / complications
- **Local relapse:** one case, attributed to incomplete resection (PMID 33673661). Recurrent bilateral disease reported (PMID 33119505).
- **Metachronous/contralateral disease:** one metachronous bilateral case among nine bilateral patients (PMID 33673661).
- **Malignant progression to ASK:** the principal feared complication; *"this event seems far less common than in PPB"* (PMID 40231379); 4 ASK among 713 carriers (PMID 39400264). Progression over 8 years documented (PMID 38807260).
- **Second DICER1 primaries:** *"Among 12 CN patients with germline DICER1 mutations, ten had previously or subsequently developed other tumors in addition to CN,"* and 26/167 CN patients developed DICER1‑related tumours overall (PMID 33673661).
- **Recovery potential:** **complete with gross‑total resection.** Without resection, natural history is progressive enlargement with mass effect and a small risk of sarcomatous transformation.

### Prediction
**Prognostic factors (CN):** completeness of resection (the sole documented relapse driver); laterality/bilaterality (renal‑function risk); germline DICER1 status (predicts second primaries); presence of any solid or anaplastic focus on thorough sampling (reclassifies the lesion and the prognosis).

**Prognostic/progression biomarkers:**
- **PRAME gain and ER loss** mark the cystic→solid transition (PMID 35297207; PMID 38539053).
- **TP53 expression/alteration** marks ASK (7/10; PMID 38807260).
- **NRAS Q61R** marked the incipient anaplastic focus and was absent from the surrounding CN (PMID 41431269).
- **Global DNA hypomethylation** characterises the sarcoma classes (PMID 36966138).
- For ASK specifically, **stage** is the dominant prognostic variable, and chemotherapy was associated with improved EFS and OS (hazard ratios 0.09 and 0.08; PMID 38807260).

---

## 12. Treatment

### Surgical and interventional — the definitive treatment
- **Primary modality:** **complete surgical resection.** GeneReviews/PPB Registry: *"Treatment for cystic nephroma consists of surgical resection via partial or full nephrectomy."*
- **Observed practice:** *"Surgery (upfront or after chemotherapy) was performed in 165/167 patients,"* comprising *"radical nephrectomy in 121 cases and NSS in 28 cases"* (PMID 33673601 → PMID 33673661).
- **Preferred direction of practice:** nephron‑sparing surgery wherever feasible, which is the stated purpose of surveillance — to detect CN "when they are small and nephron-sparing surgery is still possible" (NCI PDQ) and *"to preserve renal function through less extensive surgery, especially in cases of bilateral disease"* (PMID 39400264).
- **Intraoperative conversion** from partial to radical nephrectomy is documented when extent is uncertain ([Zi et al. 2026](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)).
- **Avoid rupture:** the only stage III case in the literature review arose "based on intraoperative tumor rupture" (PMID 33673661).

**NCIT clinical‑intervention terms (IDs verified via [OLS4/NCIT](https://www.ebi.ac.uk/ols4/api/search?q=nephrectomy&ontology=ncit&rows=15)):** **NCIT:C15284** Nephrectomy; **NCIT:C51928** Partial Nephrectomy (synonym "Nephron Sparing Surgery (NSS)"); **NCIT:C51778** Radical Nephrectomy; **NCIT:C94459** Bilateral Nephrectomy; **NCIT:C51632** Total Nephrectomy; **NCIT:C165186** Open Partial Nephrectomy; **NCIT:C165181** Laparoscopic Partial Nephrectomy; **NCIT:C150387** Robot‑assisted Laparoscopic Partial Nephrectomy; **NCIT:C165187** Open Radical Nephrectomy; **NCIT:C165182** Laparoscopic Radical Nephrectomy.

### Pharmacotherapy
- **No pharmacological therapy is indicated for cystic nephroma.** The explicit recommendation: *"Chemotherapy and radiotherapy are generally not recommended for CN or CPDN"* (PMID 33673661).
- Historical/exceptional use: *"Nine patients were treated with upfront chemotherapy"*; response documented in only one bilateral case, where chemotherapy *"led to growth arrest, averting end-stage renal disease."* *"Post-operative chemotherapy administration was reported in five patients"* with unclear rationale. *"Pre-operative radiotherapy was administered in five patients, all in reports from before 1994"* (ibid.).
- For the malignant branch (**ASK**, not CN), chemotherapy ± radiation is standard: chemotherapy in 38/46 (83%), radiation in 14/37 (38%), with chemotherapy associated with improved EFS/OS (HR 0.09 and 0.08) (PMID 38807260). The PPB Registry states: *"Treatments for renal sarcoma and Wilms tumor generally includes chemotherapy with or without radiation."* **Specific agents and doses for ASK were not retrieved** and are not asserted here.
- **Antiestrogen therapy is explicitly argued against** despite stromal ER positivity, because ER expression tracks cystic architecture rather than DICER1 perturbation (PMID 38539053).
- **Antihypertensive management** where hypertension is present: in the documented case, BP was controlled with oral medication and resolved after nephrectomy (PMID 42704439). Specific agents not retrieved.
- **Pharmacogenomics:** **no DICER1‑specific pharmacogenomic guidance exists** in PharmGKB/CPIC/FDA PGx resources for this disease, per my searches. DICER1 genotype does not inform drug metabolism.

### Advanced therapeutics
- **Gene therapy, cell therapy, RNA‑based therapy:** **none exists, and none is in trial, for cystic nephroma.** A clinicaltrials.gov API query for "DICER1" returned 12 studies, of which **11 are observational** (registries, genetic‑basis studies, cascade‑testing studies) and the sole interventional study is **NCT06647953**, "Testing a Standardized Approach to Surgery and Chemotherapy for Type I PPB…" — i.e. lung, not kidney ([ClinicalTrials.gov API query](https://clinicaltrials.gov/api/v2/studies?query.term=DICER1&pageSize=30)).
- **Studies listing cystic nephroma as a condition (all observational):** **NCT03382158** International PPB/DICER1 Registry (Recruiting); **NCT01247597** DICER1‑related PPB Cancer Predisposition Syndrome natural history (Recruiting); **NCT00565903** Elucidating the Genetic Basis of the PPB Familial Cancer Syndrome (Completed). Related: **NCT01970696** International Ovarian & Testicular Stromal Tumor Registry; **NCT03050268** Familial Investigations of Childhood Cancer Predisposition.
- **Targeted therapy — speculative only.** The retrieved rationale is for **PRAME‑directed therapy**: Thorner et al. conclude that targeted therapy against PRAME *"could offer novel treatment options for DICER1 syndrome patients"* (PMID 35297207). The NRAS/RAS‑MAPK findings in transforming lesions (PMID 41431269) and BRAF V600E/PDGFRA variants in isolated ASK cases (PMID 38807260) raise but do not establish MAPK‑directed options. **No targeted or immunotherapeutic agent is approved or in trial for this disease.**

### Supportive, rehabilitative
- **Supportive care:** perioperative pain control and standard pediatric post‑nephrectomy care; blood‑pressure management where indicated. No disease‑specific supportive‑care guideline was retrieved.
- **Renal protection:** long‑term single‑kidney follow‑up (nephrology input) is the logical consequence of radical nephrectomy; no CN‑specific protocol was retrieved.
- **Rehabilitation (PT/OT/speech):** **not applicable.**

### Treatment strategy
A defensible algorithm, assembled from the retrieved guidance (no formal published decision tree for CN exists):
1. Multiloculated cystic renal mass in a child → imaging characterisation (US ± CT/MRI), recognising imaging cannot distinguish CN from CPDN (PMID 33673661).
2. **Upfront complete resection, nephron‑sparing where anatomically feasible**; avoid rupture. Radical nephrectomy when NSS is not feasible (PMID 33673661; PPB Registry).
3. **Thorough pathological sampling** to exclude microscopic anaplastic foci (PMID 27036314); IHC panel (inhibin, ER, PRAME, TP53) to separate CN from adult CN/MEST and from ASK.
4. **Tumour + germline DICER1 testing with genetic counselling** for every pediatric CN.
5. **No adjuvant chemotherapy or radiotherapy** for CN (PMID 33673661). Reserve chemotherapy for bilateral/unresectable disease aiming at growth arrest and renal preservation, or for confirmed ASK/Wilms tumour.
6. **Enrol in surveillance** (§13) and **extend cascade testing** to first‑degree relatives.
7. **Combination therapy:** no combination regimen is defined for CN. Surgery is monotherapy.
8. **Personalized/genotype‑guided therapy:** not yet actionable. Genotype currently guides **surveillance and family testing**, not drug selection.

---

## 13. Prevention

### Primary prevention
**None possible.** Because the initiating event is a germline or early somatic DICER1 variant and no environmental contributor is known (§5), **primary prevention of pediatric cystic nephroma does not exist.** The only pre‑conception options are reproductive: prenatal diagnosis and preimplantation genetic testing for a known familial DICER1 variant — these are standard offerings for autosomal dominant conditions and follow from GeneReviews' statement that *"Each child of an individual with a germline constitutional DICER1 pathogenic variant has a 50% chance of inheriting the pathogenic variant,"* though I did not retrieve a DICER1‑specific PGT recommendation statement.

### Secondary prevention — the mainstay

**International PPB/DICER1 Registry protocol, renal component:** *"Abdominal ultrasounds for pediatric CN and other kidney tumors every six months until age eight years and then annually until age 12 years"* (GeneReviews; PMID 39400264). Rationale: *"The goal of renal screening is early detection to preserve renal function through less extensive surgery, especially in cases of bilateral disease, and to prevent progression to ASK."* Caveat: *"Some anaplastic sarcomas of the kidney have been diagnosed after age 12."* For individuals diagnosed after age 12, baseline imaging is recommended (GeneReviews).

**Full Registry surveillance protocol** (context, GeneReviews/PMID 39400264):
- **Chest:** radiograph at birth, every 6 months to age 8, then annually to 12; **chest CT at 3 months and 30 months**.
- **Abdomen/kidney:** as above.
- **Thyroid:** ultrasound every 3 years from age 8; consider annual for 5 years after chemotherapy.
- **Pelvis (females):** ultrasound every 6 months until at least age 40. The 2024 update moved ovarian surveillance earlier: *"DICER1-related ovarian tumors were detected before 8 years of age, prompting the Registry to recommend earlier initiation of ovarian surveillance with pelvic ultrasound beginning at the time of detection of a germline DICER1 P/LP variant"* (PMID 39400264).
- **Eyes:** visual acuity and dilated examination annually from age 3 to 10.
- **CNS:** urgent brain MRI for concerning neurologic symptoms; shared decision‑making about asymptomatic screening MRI in late adolescence/early adulthood.

**Alternative European protocol (SIOPE/CanGene‑CanVar), which is deliberately lighter:** minimum programme of *"annual clinical examination from birth to age 20 years, six-monthly chest X-ray and renal ultrasound from birth to age 6 years, and thyroid ultrasound every 3 years from age 8 to age 40 years,"* with an extended version available, and the explicit framing that *"Developing surveillance protocols for this syndrome is challenging because uncertainty exists about the clinical efficacy of surveillance, and appraisal of potential benefits and harms vary"* and *"patients have to be supported in choosing the surveillance program that best meets their needs"* (PMID 34170462). **Clinicians should know these two protocols differ in the age at which renal ultrasound stops (6 vs 12 years).**

**Evidence that surveillance works** is strongest for the lung, not the kidney: *"To date, 5 cases of type I and 29 cases of type Ir PPB have been diagnosed by surveillance in enrolled individuals"*, and *"Ongoing data collection highlights the role of lung surveillance in the early detection of PPB and suggests that imaging-based detection and early resection may decrease the risk of advanced PPB"* (PMID 39400264). **An equivalent quantified benefit for renal surveillance was not retrieved** — the renal recommendation rests on biological rationale plus the ASK stage–outcome gradient.

### Tertiary prevention
Complete resection of the CN (prevents local relapse and removes the substrate for ASK); continued multi‑organ surveillance after a CN diagnosis, given that 26/167 CN patients developed other DICER1 tumours (PMID 33673661); and long‑term renal‑function monitoring after nephrectomy.

### Screening and early detection programmes
- **Newborn screening: none, and none proposed.** Not on any ACMG/CDC newborn‑screening panel retrieved.
- **Population carrier screening: not recommended.** Genome‑first studies demonstrate *feasibility* — Mirshahi et al. concluded *"Use of the genome-first approach may complement more traditional approaches to syndrome delineation and may be an efficient approach for risk estimation"* — but this is framed as a research/risk‑estimation strategy, not a screening recommendation.
- **Cascade screening: recommended.** *"genetic education, counseling, and testing in first-degree relatives (parents and siblings)"*, and where the inheritance pattern is established, *"cascade genetic education, counseling, and testing may then be indicated"* (PMID 39400264). GeneReviews: *"Sibs who inherit a DICER1 pathogenic variant are at increased risk for PPB, pulmonary cysts, thyroid gland neoplasia, ovarian tumors, cystic nephroma, and other DICER1-related features."*
- **Risk stratification:** mosaic RNase IIIb hotspot carriers constitute an identifiable **higher‑risk stratum** for multifocal renal/pulmonary cystic disease and earlier onset (PMID 26925222) — a practical argument for mosaicism‑sensitive testing before assigning a standard surveillance schedule.
- **Clinical actionability:** ClinGen rates DICER1‑related tumor predisposition as having **moderate actionability in the pediatric context** (8 assertions across two working groups; adult assertion pending) ([ClinGen HGNC:17098](https://search.clinicalgenome.org/kb/genes/HGNC:17098)).

### Immunization, behavioural interventions, public‑health and environmental interventions, prophylaxis
**All not applicable.** There is no vaccine‑preventable component, no behavioural risk factor to modify, no environmental exposure to abate, and no prophylactic medication or procedure (prophylactic nephrectomy is not practised and was not mentioned in any retrieved source). Genetic counselling is the counselling intervention of record.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologous genes (retrieved via [NCBI Datasets orthologs API, Gene 23405](https://api.ncbi.nlm.nih.gov/datasets/v2alpha/gene/id/23405/orthologs))

| Species | NCBI Taxon | Gene symbol | NCBI Gene ID |
|---|---|---|---|
| *Homo sapiens* | 9606 | **DICER1** | 23405 |
| *Mus musculus* (house mouse) | 10090 | Dicer1 | **192119** |
| *Rattus norvegicus* (Norway rat) | 10116 | Dicer1 | **299284** |
| *Danio rerio* (zebrafish) | 7955 | dicer1 | **324724** |
| *Canis lupus familiaris* (dog) | 9615 | DICER1 | **480426** |

All are assigned to NCBI ortholog group 23405. *Drosophila* Dcr‑1 and *C. elegans* dcr‑1 are well‑known Dicer homologues but were **not returned by my query**, so I do not assert their identifiers here.

### Breed
**Not applicable.** No breed association exists; no VBO identifier is relevant.

### Natural disease in other species
**None documented.** A direct OMIA advanced search by gene symbol DICER1 returned **"No phene records found"** ([OMIA](https://omia.org/results/?search_type=advanced&gene_symbol=DICER1)) — i.e. **no naturally occurring DICER1‑associated phene is recorded in any animal species.** Searches for naturally occurring cystic nephroma in companion animals surfaced only unrelated cystic renal diseases (OMIA:000807 polycystic kidney disease in dog and cat, PKD1‑related; OMIA:002929 nephronophthisis; feline renal cystadenoma case reports) — none is a DICER1 disease or a cystic nephroma analogue.

**Veterinary relevance: effectively nil.** Pediatric cystic nephroma has no recognised veterinary counterpart.

### Comparative biology
- **Evolutionary conservation of the mechanism is strong**, which is why mouse genetics is informative: the human hotspot residue **D1709** corresponds to mouse **D1693**, and a conditional knock‑in allele **Dicer1^f‑D1693N** exists (see §15) — a direct residue‑level correspondence.
- **Comparative pathology:** mouse *Dicer1* loss in the developing kidney produces **dysplasia and collecting‑duct cysts** rather than a human‑type benign multilocular neoplasm (PMID 19169742; PMID 20944551), whereas hotspot‑allele activation in Hic1⁺ mesenchymal cells produces tumours that *"closely mirror[] the developmental continuum of human DRTP sarcoma histologically and molecularly"* (PMID 41912509). So the **sarcomatous end** of the spectrum models better in mouse than the benign cystic end.
- Alliance of Genome Resources / HomoloGene records were not individually fetched.

### Transmission
**No zoonotic potential and no cross‑species transmissibility** — this is a germline/somatic genetic neoplasm, not a transmissible disease.

---

## 15. Model Organisms

### Model types available

**Mammalian (mouse) — genetic**

| Model | Design | Phenotype relevant to CN | Source |
|---|---|---|---|
| **Dicer1 conditional knockout, ureteric‑bud lineage (HoxB7‑Cre)** | Complete biallelic *Dicer1* ablation | *"the development of renal cysts"*, preceded by excessive proliferation and apoptosis; *"disrupted ciliogenesis"*; reduced Wnt11 and c‑Ret at ureteric tips; branching defects → renal hypoplasia | Nagalakshmi VK, Ren Q, Pugh MM, Valerius MT, McMahon AP, Yu J. *Kidney Int.* 2011. **PMID 20944551** |
| **Dicer1 conditional knockout, nephron progenitors** | Complete biallelic ablation | *"elevated apoptosis and premature termination of nephrogenesis"* | Same, PMID 20944551 |
| **Dicer1 conditional knockout, urogenital tract** | Conditional deletion incl. ureteric‑bud derivatives | *"Dicer1 is required for development of the female reproductive tract and also normal kidney morphogenesis"*; hydronephrosis and parenchymal cysts in both sexes | Pastorelli LM, Wells S, Fray M, Smith A, Hough T, Harfe BD, McManus MT, Smith L, Woolf AS, Cheeseman M, Greenfield A. *Mamm Genome.* 2009;20(3):140–151. **PMID 19169742** |
| **Dicer1^f‑D1693N conditional RNase IIIb knock‑in** | Cre‑dependent expression of the mouse equivalent of human **p.D1709N** hotspot; combinable with a null allele to recreate compound heterozygosity | Enables the authentic two‑hit genotype rather than full ablation | Described in the [biorxiv/Nature Communications model literature](https://www.biorxiv.org/content/10.1101/2024.11.30.624592v1.full); allele details retrieved via search summary — treat the allele name as secondary |
| **Hic1‑CreERT2 lineage‑traceable GEMM (2026)** | *"controlled activation of hemizygous Dicer1 RNase IIIb mutation in Hic1⁺ mesenchymal stromal cells"* | *"This causes renal tumors closely mirroring the developmental continuum of human DRTP sarcoma histologically and molecularly."* Identifies a Hic1⁺Pdgfra⁺Dpt⁺Pi16⁺ fibroblastic progenitor as the cell of origin; cystic nephroma is positioned in this continuum as LGMT DICER1 with *"hypocellular and primitive mesenchyme"* adjacent to *"cystically dilated renal ducts"* | Kommoss FKF, Zhang JYH, Lynch BJ, et al. *Nat Commun.* 2026;17(1):4608. **PMID 41912509**; DOI 10.1038/s41467-026-70971-6 |
| **Biallelic Dicer1 gynecologic‑tract mouse** | Conditional compound heterozygous Dicer1 | Lineage‑specific DICER1‑syndrome cancer; cited as fully recapitulating biallelic human genotypes | *Cancer Res.* 2023;83(21):3517 — [AACR record](https://aacrjournals.org/cancerres/article/83/21/3517/729717/Biallelic-Dicer1-Mutations-in-the-Gynecologic); primary text not fetched, secondary |

**Cellular / in vitro**
- **Human embryonic stem cells: Dicer1‑KO and Dicer1‑S1344L (homozygous and hemizygous).** Verbatim: *"we generated Dicer1-KO and Dicer1-S1344L (homozygous and hemizygous) human ESCs; the latter is a non-catalytic mutation in RNase IIIa that impairs RNase IIIb activity. Dicer1 knockouts lack canonical miRNAs, while S1344L induces two trends: ablation of miRNA-5p strands, and selective changes in miRNA-3p strands"* (Jee D, Lee S, Yang D, Rickert R, Shang R, Huangfu D, Lai EC. **PMID 41279602**; DOI 10.1101/2025.10.15.682667; peer‑reviewed in *Nat Struct Mol Biol*). This is the sharpest available system for dissecting hotspot biochemistry — but it models **miRNA biology, not renal cystogenesis**.
- Cell‑line and organoid/iPSC models of pediatric cystic nephroma specifically: **none retrieved** (no Cellosaurus‑registered pediatric cystic nephroma line was identified in my searches).

**Invertebrate models (*Drosophila*, *C. elegans*), zebrafish, yeast:** relevant to Dicer/miRNA biology generally; **no model of cystic nephroma** exists in these organisms (a cystic renal neoplasm has no anatomical counterpart in fly or worm). Zebrafish *dicer1* (Gene 324724) exists as an ortholog but no renal‑tumour model was retrieved.

**Induced (non‑genetic) models:** **none.** No drug, surgical, or environmental induction model of cystic nephroma exists — consistent with the absence of environmental etiology (§5).

### Genetic model types available
Knockout (conditional, lineage‑restricted via Cre), **knock‑in (hotspot missense, conditional)**, and compound‑heterozygous combinations. Humanized and transgenic overexpression models of DICER1 relevant to this disease were not retrieved.

### Phenotype recapitulation and limitations
**What the models capture well**
- The **developmental requirement** for Dicer‑dependent miRNAs in nephron progenitors and ureteric bud — apoptosis, premature arrest of nephrogenesis, disrupted ciliogenesis, collecting‑duct cysts (PMID 20944551; PMID 19169742). This provides the mechanistic plausibility for the cystic architecture of human CN.
- The **sarcomatous continuum** — the 2026 Hic1 model reproduces human DRTP sarcoma histology and molecular profile and identifies the cell of origin and differentiation trajectories, validated against human tumours (PMID 41912509).
- The **biochemistry of the hotspot allele** — 5p loss plus 3p gain‑of‑function via Argonaute strand switching, in isogenic human cells (PMID 41279602).

**What they do not capture — stated plainly**
- **No model has been shown to generate a bona fide benign multilocular cystic nephroma histologically indistinguishable from the human lesion.** A search summary asserted that *"Mouse models with conditional biallelic DICER1 ablation in ureteric bud epithelium have recapitulated the human phenotype of cystic nephroma"*; **I could not verify this claim in any primary source I retrieved.** The primary papers (PMID 19169742; PMID 20944551) describe renal **dysplasia, hypoplasia, hydronephrosis and collecting‑duct cysts** — developmental malformation phenotypes — not a discrete benign neoplasm. Treat the "recapitulates cystic nephroma" statement as **unverified**.
- Full **Dicer1 ablation is not the human genotype**: human tumours retain a neomorphic hotspot allele that selectively abolishes 5p processing. Null models therefore overshoot, and the field's move to Dicer1^f‑D1693N / hotspot knock‑in alleles is the correction.
- **Benign persistence** — the fact that most human CN never transform — is not modelled; the Hic1 model emphasises progression to sarcoma.
- The **germline‑plus‑stochastic‑somatic‑second‑hit timing** that Brenneman et al. argue determines human phenotype (PMID 26925222) is replaced in these models by **experimenter‑controlled Cre timing**, which is an advantage for mechanism and a limitation for natural‑history fidelity.

### Research applications
Cell‑of‑origin mapping and developmental hierarchy (PMID 41912509); miRNA strand‑selection biochemistry and target de‑repression (PMID 41279602; PMID 31417090); nephrogenesis and cystogenesis mechanism (PMID 20944551; PMID 19169742); and — prospectively — preclinical testing of MAPK‑ or PRAME‑directed strategies, for which no published preclinical study was retrieved.

### Resources
Retrieved: **NCBI Gene / NCBI Datasets orthologs** (IDs in §14); **OMIA** (searched — no DICER1 phene). **Not retrieved this session:** MGI allele/phenotype records for *Dicer1* — my fetch of MGI:107451 returned *Plcd3*, a different gene, and the MGI quick‑search endpoint returned no parsable results, so **I am not stating an MGI accession for mouse Dicer1.** IMPC, RGD, ZFIN, IMSR, EMMA, MMRRC, KOMP, and Cellosaurus records were likewise not retrieved; relevant alleles should be looked up directly in MGI/IMSR before use.

---

## Summary of Explicit Data Gaps

Recorded so the knowledge‑base entry does not imply coverage that does not exist:

1. **No population incidence or prevalence rate** for pediatric cystic nephroma (no SEER/GBD/Orphanet figure). Best anchors: 167 literature cases; 62/713 DICER1 carriers.
2. **No ICD‑11 code retrieved** (WHO browser unreadable by the fetch tool). **No dedicated MeSH descriptor** (confirmed Count = 0).
3. **No validated QoL instrument data** (EQ‑5D/SF‑36/PROMIS/PedsQL) for this disease or for DICER1 syndrome surveillance burden.
4. **No diagnostic biomarker** in blood or urine; no liquid‑biopsy, proteomic, metabolomic, or lipidomic study of this lesion.
5. **No environmental, lifestyle, infectious, or gene–environment factor** — a true negative, not a search failure.
6. **No protective factors and no modifier genes** identified.
7. **HPO disease annotation gap:** HP:0034836 (Cystic nephroma) is not annotated to OMIM:601200 despite 62/713 registry frequency.
8. **DICER1 IHC pattern in cystic nephroma specifically** not verified at source (only the PPB epithelial‑loss pattern, PMID 19556464).
9. **Quantified benefit of renal (as opposed to pulmonary) surveillance** not demonstrated in retrieved data.
10. **No mouse model verified to produce a true benign pediatric cystic nephroma**; the widely repeated claim that ureteric‑bud biallelic Dicer1 ablation "recapitulates cystic nephroma" could not be confirmed in a primary source.
11. **No MGI accession for mouse Dicer1 retrieved** (my MGI fetches failed or returned the wrong gene); no CHEBI identifiers retrieved for any therapeutic agent.
12. **No therapy specific to this disease** beyond surgery; the only interventional DICER1 trial (NCT06647953) addresses Type I PPB, not renal disease.

---

## Sources

- [GeneReviews: DICER1‑Related Tumor Predisposition (NBK196157)](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)
- [Li Y, Pawel BR, Hill DA, Epstein JI, Argani P. *Am J Surg Pathol.* 2017;41(4):472–481. PMID 28177962](https://pure.johnshopkins.edu/en/publications/pediatric-cystic-nephroma-is-morphologically-immunohistochemicall/)
- [van Peer SE, et al. *Cancers.* 2021;13(5):997. PMID 33673661](https://pmc.ncbi.nlm.nih.gov/articles/PMC7957568/)
- [Capozzi A, et al. *Pediatr Dev Pathol.* 2025;28(4):231–243. PMID 40231379](https://pmc.ncbi.nlm.nih.gov/articles/PMC13039238/)
- [Doros LA, et al. *Mod Pathol.* 2014;27:1267–1280. PMID 24481001](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24481001&resultType=core&format=json)
- [Hill DA, et al. *Science.* 2009. PMID 19556464](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=19556464&rettype=abstract&retmode=text)
- [Bahubeshi A, et al. *J Med Genet.* 2010;47(12):863–866. PMID 21036787](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21036787&rettype=abstract&retmode=text)
- [Foulkes WD, et al. *Hum Mutat.* 2011;32(12):1381–1384. PMID 21882293](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21882293&rettype=abstract&retmode=text)
- [Brenneman M, et al. *F1000Res.* 2015;4:214. PMID 26925222](https://pmc.ncbi.nlm.nih.gov/articles/PMC4712775/)
- [de Kock L, Wu MK, Foulkes WD. *Hum Mutat.* 2019;40(11):1939–1953. PMID 31342592](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31342592&rettype=abstract&retmode=text)
- [Vedanayagam J, et al. *Nat Commun.* 2019;10:3682. PMID 31417090](https://pmc.ncbi.nlm.nih.gov/articles/PMC6695490/)
- [Jee D, et al. bioRxiv 2025.10.15.682667. PMID 41279602](https://pmc.ncbi.nlm.nih.gov/articles/PMC12632780/)
- [Nature Communications 2026: DICER1-related tumour predisposition mutations increase 3p-miRNA function and HERVH activity](https://www.nature.com/articles/s41467-026-76094-2)
- [Kommoss FKF, et al. *Nat Commun.* 2023;14:1677. PMID 36966138](https://pmc.ncbi.nlm.nih.gov/articles/PMC10039902/)
- [Kommoss FKF, et al. *Nat Commun.* 2026;17(1):4608. PMID 41912509](https://pmc.ncbi.nlm.nih.gov/articles/PMC13199431/)
- [Schultz KAP, et al. *Clin Cancer Res.* 2024;30(24):5681–5692. PMID 39400264](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450/)
- [Schoettler PJ, et al. *Pediatr Blood Cancer.* 2024. PMID 38807260](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590164/)
- [Cortes‑Santiago N, et al. *Pediatr Blood Cancer.* 2026;73(2):e70068. PMID 41431269](https://pubmed.ncbi.nlm.nih.gov/41431269/)
- [Arizpe D, et al. *Hum Pathol.* 2026;172:106110. PMID 41905669](https://pubmed.ncbi.nlm.nih.gov/41905669/)
- [Wu MK, et al. *Hum Pathol.* 2016;53:114–120. PMID 27036314](https://www.sciencedirect.com/science/article/abs/pii/S0046817716300041)
- [Fernández‑Martínez L, et al. *BMC Cancer.* 2017;17(1):146. PMID 28222777](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5320664/)
- [Caron CP, et al. *Can Urol Assoc J.* 2021;15(5):E290–E292. PMID 33119505](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=33119505&rettype=abstract&retmode=text)
- [Chara AO, et al. *Case Rep Surg.* 2026;2026:2579487. PMID 42311827](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42311827&rettype=abstract&retmode=text)
- [Brown EA, et al. *Pediatr Nephrol.* 2026. PMID 42704439](https://link.springer.com/article/10.1007/s00467-026-07501-5)
- [Thorner PS, et al. *Am J Surg Pathol.* 2024;48(6):733–741. PMID 38539053](https://pubmed.ncbi.nlm.nih.gov/38539053)
- [Thorner PS, et al. *J Pathol Clin Res.* 2022;8(3):294–304. PMID 35297207](https://pmc.ncbi.nlm.nih.gov/articles/PMC8977278/)
- [Greco F, et al. *J Kidney Cancer VHL.* 2017;4(3):1–9. PMID 28752022](https://pmc.ncbi.nlm.nih.gov/articles/PMC5519771/)
- [Zi et al. *Front Oncol.* 2026. DOI 10.3389/fonc.2026.1799009](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2026.1799009/full)
- [Bakhuizen JJ, et al. *Fam Cancer.* 2021;20(4):337–348. PMID 34170462](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=34170462&rettype=abstract&retmode=text)
- [Stewart DR, et al. *J Clin Oncol.* 2019;37(8):668–676. PMID 30715996](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30715996&rettype=abstract&retmode=text)
- [Mirshahi UL, et al. *JAMA Netw Open.* 2021;4(2):e210112](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2776900)
- [Hatton JN, et al. *Hum Mutat.* 2023;2023:9537832. PMID 38084291](https://pmc.ncbi.nlm.nih.gov/articles/PMC10713350/)
- [ClinGen gene record, DICER1 (HGNC:17098)](https://search.clinicalgenome.org/kb/genes/HGNC:17098)
- [Nagalakshmi VK, et al. *Kidney Int.* 2011. PMID 20944551](https://pubmed.ncbi.nlm.nih.gov/20944551/)
- [Pastorelli LM, et al. *Mamm Genome.* 2009;20(3):140–151. PMID 19169742](https://link.springer.com/article/10.1007/s00335-008-9169-y)
- [International PPB/DICER1 Registry — Renal Tumors](https://www.ppbregistry.org/renal-tumors/)
- [NCI PDQ: Wilms Tumor and Other Childhood Kidney Tumors Treatment](https://www.cancer.gov/types/kidney/hp/wilms-treatment-pdq)
- [ClinicalTrials.gov API — DICER1 studies](https://clinicaltrials.gov/api/v2/studies?query.term=DICER1&pageSize=30)
- [MONDO:0002385 (OLS4)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0002385) · [MONDO:0100216 (OLS4)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0100216)
- [MedGen 220422](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=medgen&id=220422) · [MedGen 825667](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=medgen&id=825667)
- [HPO HP:0034836](https://ontology.jax.org/api/hp/terms/HP:0034836) · [HPO annotations for OMIM:601200](https://ontology.jax.org/api/network/annotation/OMIM:601200)
- [HGNC DICER1](https://rest.genenames.org/fetch/symbol/DICER1) · [UniProt Q9UPY3 (EBI Proteins API)](https://www.ebi.ac.uk/proteins/api/proteins/Q9UPY3) · [NCBI Datasets orthologs, Gene 23405](https://api.ncbi.nlm.nih.gov/datasets/v2alpha/gene/id/23405/orthologs)
- [OMIA advanced search, DICER1 — no phene records](https://omia.org/results/?search_type=advanced&gene_symbol=DICER1)
- [NLM Clinical Table Search Service, ICD‑10‑CM D30](https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=D30)
- [OLS4 NCIT nephrectomy terms](https://www.ebi.ac.uk/ols4/api/search?q=nephrectomy&ontology=ncit&rows=15) · [OLS4 UBERON kidney](https://www.ebi.ac.uk/ols4/api/search?q=kidney&ontology=uberon&exact=true&rows=5) · [OLS4 GO pre‑miRNA processing](https://www.ebi.ac.uk/ols4/api/search?q=pre-miRNA%20processing&ontology=go&rows=10)
- [GEO GSE313183 (via OmicsDI)](https://www.omicsdi.org/dataset/geo/GSE313183)
- [SciELO: Cystic nephroma in pediatrics (secondary, unverified at source)](https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S2452-60532021000500754) · [UK Biobank DICER1 genome‑first publication record (secondary)](https://www.ukbiobank.ac.uk/publications/a-genome-first-approach-to-characterize-dicer1-pathogenic-variant-prevalence-penetrance-and-cancer-thyroid-and-other-phenotypes-in-2-population-scale-cohorts/) · [Cancer Res 2023, biallelic Dicer1 gynecologic mouse (secondary)](https://aacrjournals.org/cancerres/article/83/21/3517/729717/Biallelic-Dicer1-Mutations-in-the-Gynecologic)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 74 |
| Resolved | 74 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 74 |
| On topic | 47 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `DOI:10.3389/fonc.2026.1799009` *(abstract only)*: "is more common in male newborns (with a male-to-female ratio of 3:1)"
  - Text part not found as substring: 'is more common in male newborns (with a male-to-female ratio of 3:1)' (note: only abstract available for DOI:10.3389/fonc.2026.1799009, full text may contain this excerpt)
- `PMID:33673661` *(abstract only)*: "based on intraoperative tumor rupture"
  - closest text in source: "In children presenting with a predominantly cystic renal tumor, the most likely diagnoses include cystic partially differentiated nephroblastoma (CPDN) and cystic nephroma (CN)"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:26925182` (1 mention) - Symptoms of Common Mental Disorders and Adverse Health Behaviours in Male Professional Soccer Players.
  - shared terms: none

Weighed against this report's own most characteristic terms: `dicer1`, `cystic`, `nephroma`, `renal`, `pediatric`, `disease`, `tumor`, `kidney`, `germline`, `gene`, `patient`, `registry`, `genetic`, `ppb`, `tumour`, `exist`, `ask`, `lesion`, `cyst`, `variant`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 16 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0002385` (6 mentions) - the report calls it "benign cystic nephroma", "OLS4"; MONDO calls it **benign cystic nephroma**
- `MONDO:0100216` (5 mentions) - the report calls it "OLS4"; MONDO calls it **DICER1-related tumor predisposition**
- `DOID:2673` (1 mention) - the report calls it "DOID"; DOID calls it **adult cystic nephroma**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0034836` (10 mentions) - the report calls it "Benign multilocular cystic nephroma", "Cystic nephroma (multilocular cystic renal neoplasm)", "Cystic nephroma"; HP calls it **Cystic nephroma**, and lists "Multilocular cystic renal tumor" among its other names
- `HP:0100528` (2 mentions) - the report calls it "Pleuropulmonary blastoma, all types", "Pleuropulmonary blastoma, 11/14"; HP calls it **Pleuropulmonary blastoma**
- `HP:0002859` (2 mentions) - the report calls it "Embryonal rhabdomyosarcoma", "Rhabdomyosarcoma"; HP calls it **Rhabdomyosarcoma**
- `HP:0002667` (2 mentions) - the report calls it "DICER1‑associated Wilms tumor"; HP calls it **Nephroblastoma**, and lists "Wilms tumor" among its other names
- `HP:0002885` (1 mention) - the report calls it "Medulloblastoma, 1/86"; HP calls it **Medulloblastoma**
- `HP:0000006` (2 mentions) - the report calls it "Autosomal dominant inheritance, 20/20", "Autosomal dominant"; HP calls it **Autosomal dominant inheritance**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0002385` - called "benign cystic nephroma", "OLS4"
- `HP:0034836` - called "Benign multilocular cystic nephroma", "Cystic nephroma (multilocular cystic renal neoplasm)", "Cystic nephroma"
- `HP:0100528` - called "Pleuropulmonary blastoma, all types", "Pleuropulmonary blastoma, 11/14"
- `HP:0002859` - called "Embryonal rhabdomyosarcoma", "Rhabdomyosarcoma"
- `HP:0000006` - called "Autosomal dominant inheritance, 20/20", "Autosomal dominant"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `EXT_ID`, `OMIM`, `OMIA`, `MGI`.